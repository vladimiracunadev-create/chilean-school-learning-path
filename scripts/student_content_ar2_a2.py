"""Cuaderno del estudiante de 2.º básico Artes Visuales, AR02 OA 03 (materiales y procedimientos), OA 04 (comunicar impresiones de obras) y OA 05 (explicar preferencias)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA3 = "AR02 OA 03"
OA4 = "AR02 OA 04"
OA5 = "AR02 OA 05"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def w(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def m(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=[ctx], selfcheck=sc, open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 03
# ---------------------------------------------------------------- Clase 1
lesson(
    OA3, 1,
    "Plasticina o masa de sal hecha con un adulto (una taza de harina, media taza de sal y un poco de agua; no se come). Una tapa, una hoja de árbol y un palito para marcar. Lávate las manos al terminar.",
    "Aprenderé a modelar con un material blando: pellizcar, enrollar, aplastar y unir, y a dejar huellas. Sirve para expresar una emoción o una idea con una escultura.",
    ["Sé apretar y estirar la plasticina o la masa.", "Sé que una escultura tiene volumen."],
    [
        "Modelar es dar forma a un material blando con las manos. La plasticina, la arcilla y la masa de sal sirven para eso. Con ellas haces volumen: una obra que ocupa espacio y que puedes mirar por todos lados. Las técnicas más simples son pellizcar, enrollar, aplastar, alisar y unir.",
        "Para unir dos trozos, presiónalos y alisa la unión con el dedo. Así no se caen. También puedes hacer una huella: presionas un objeto, como una tapa o una hoja, sobre la masa y lo sacas. Queda la marca de su forma. Las huellas dan textura a tu obra.",
        "Antes de modelar, piensa qué quieres expresar. Un animal hecho una bolita puede mostrar susto o frío. Un animal con el cuerpo estirado puede mostrar alegría. Elige formas redondas y suaves para calma, o con puntas para susto o enojo. Tu obra cuenta lo que sientes.",
    ],
    [("modelar", "dar forma a un material blando con las manos"), ("volumen", "lo que ocupa espacio y se puede rodear con la vista"), ("huella", "marca que deja un objeto presionado sobre la masa"), ("textura", "cómo se ve o se siente la superficie"), ("alisar", "pasar el dedo hasta dejar la superficie pareja")],
    [
        w("Un gusano de masa", "Quieres hacer un gusano que se ve contento. ¿Qué pasos sigues?", ["Hago varias bolitas de masa.", "Las uno presionando y alisando las uniones.", "Doblo el cuerpo hacia arriba para que se vea contento."], "Bolitas unidas, con el cuerpo doblado hacia arriba"),
        w("Una huella de hoja", "Quieres dejar la huella de una hoja en una plancha de masa. ¿Qué haces?", ["Aplano la masa con las manos.", "Presiono la hoja con cuidado.", "La saco despacio: queda la marca de las nervaduras."], "Una huella con las líneas de la hoja"),
    ],
    [
        m("Pegar las patas de un animal sin presionar ni alisar.", "Las partes quedan sueltas y se caen.", "Presiona las partes y alisa la unión con el dedo."),
        m("Aplastar la masa tan fina que se rompe.", "Se aprieta sin cuidar el grosor.", "Deja la masa con un grosor parejo, ni muy fino ni muy grueso."),
    ],
    [
        ex("Pellizcar es apretar un trozo de masa con los dedos. ¿Con qué lo haces: con las tijeras o con los dedos?", "Con los dedos", "La definición dice que se aprieta con los dedos."),
        ex("Presionas la tapa de un frasco sobre la masa y la sacas. ¿Cómo se llama la marca que queda?", "Huella", "La marca que deja un objeto presionado es una huella."),
        ex("Una escultura se puede rodear y mirar por todos lados. ¿Tiene volumen o es plana?", "Volumen", "Lo que se rodea con la vista ocupa espacio."),
    ],
    [
        ex("¿Qué técnica usas para hacer un cordón largo de masa? A: aplastar la masa. B: enrollarla entre las manos y la mesa. C: pintarla.", "B", "Al enrollar, la masa se estira en forma de cordón."),
        ex("Para unir dos trozos de masa, ¿los presionas y alisas la unión o los dejas solo apoyados?", "Los presionas y alisas la unión", "Alisar la unión evita que se caigan."),
        ex("Presionas una hoja con nervaduras sobre la masa. ¿Qué te queda en la masa?", "Una huella con las líneas de la hoja", "La huella copia la forma de lo presionado."),
    ],
    [
        arith("Haces un gusano con 5 bolitas de masa y le agregas 2 bolitas pequeñas de ojos. ¿Cuántas bolitas usaste?", "5 + 2", "Se suman las bolitas del cuerpo y las de los ojos."),
        ex("Quieres modelar un animal asustado. ¿Haces el cuerpo estirado o hecho una bolita?", "Hecho una bolita", "Un cuerpo encogido muestra susto o frío."),
        ex("Ordena para unir dos bolitas: A alisar la unión, B hacer las dos bolitas, C presionarlas juntas.", "B, C, A", "Primero se hacen, luego se juntan y al final se alisa."),
    ],
    [
        ex("Ana modeló un perro y sus patas se caen. ¿Qué puede hacer: unir mejor las patas presionando y alisando, o dejarlas sueltas?", "Unir mejor presionando y alisando", "Una buena unión mantiene las partes firmes."),
        ex("Beto dice: «Una huella es lo mismo que una escultura». ¿Tiene razón?", "No", "La huella es una marca que queda; la escultura es una obra con volumen."),
    ],
    [
        arith("Tienes masa para 12 bolitas y usas 3 bolitas en cada flor. ¿Cuántas flores completas puedes hacer?", "12 // 3", "Se reparten las 12 bolitas en grupos de 3."),
        ex("Quieres que tu escultura se vea tranquila. ¿Eliges formas redondas y suaves o con puntas y filos?", "Redondas y suaves", "Las formas redondas y alisadas dan sensación de calma."),
    ],
    ex("Con un adulto, hicieron masa de sal (harina, sal y agua). Terminaste tu escultura. ¿Se puede comer la masa de sal?", "No", "Es un material para modelar y no es comida."),
    [
        ex("¿Cómo se llama la técnica de pasar el dedo hasta dejar una superficie pareja?", "Alisar", "Alisar deja la superficie pareja."),
        ex("Verdadero o falso: una huella deja una marca de textura.", "Verdadero", "La marca copia la superficie del objeto presionado."),
        ex("Si quieres expresar alegría, ¿estiras o encoges el cuerpo de tu animal?", "Lo estiras", "Un cuerpo estirado se ve más animado."),
    ],
    task(
        "Elige UNA emoción: alegría, susto o calma. Modela un animal con masa o plasticina que exprese esa emoción. Usa al menos dos técnicas (pellizcar, enrollar, aplastar, alisar o unir) y deja una huella con una tapa o una hoja. Escribe qué técnicas usaste y cómo se ve la emoción en tu obra.",
        "Elegí susto. Modelé un conejo hecho una bolita con las orejas pegadas hacia atrás. Usé enrollar para las orejas y alisar para las uniones. Dejé la huella de una tapa en la panza.",
        ["usa al menos dos técnicas", "deja una huella", "la forma expresa la emoción", "explica lo que hizo"],
        ["escultura de masa", "una frase con las técnicas y la emoción"],
        ["partes sueltas sin unir", "no mostrar la emoción en la forma"],
        "Reconoce la técnica mejor usada y pide que muestre qué parte de la forma comunica la emoción.",
    ),
    "Presiona un botón o una tapa sobre masa y observa la huella. Di en voz alta qué forma tiene.",
    "Haz el mismo animal con la emoción contraria y compara qué cambió en la forma.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA3, 2,
    "Una caja de cartón pequeña, tubos de cartón, tapas plásticas, cinta adhesiva o cola fría. Todo limpio y seco. Tijeras de punta roma, solo con un adulto. Nada de latas, vidrio ni envases con bordes filosos.",
    "Aprenderé a transformar materiales de reciclaje limpios en una escultura que se sostenga sola. Sirve para dar nueva vida a lo que ya no usamos y expresar una idea.",
    ["Sé pegar y unir piezas.", "Sé que algunos objetos se pueden volver a usar."],
    [
        "Reciclar es usar de nuevo materiales que ya se usaron, como cajas, tubos de cartón y tapas. Con ellos puedes hacer esculturas. Antes de usarlos, deben estar limpios, secos y sin bordes filosos. Si tienes dudas, pide ayuda a un adulto.",
        "Una buena escultura debe sostenerse sola. Para eso necesita una estructura firme. Pon las piezas más anchas y pesadas abajo, y las más livianas arriba. Una base ancha da equilibrio. Una torre con la base angosta se cae con facilidad.",
        "Pega las piezas con cola fría o cinta y espera un momento a que se sostengan. Prueba tu escultura sobre la mesa. Si se cae, cambia la base o las uniones. Después decide qué quieres expresar y agrega colores o detalles. Un robot, un animal o una ciudad pueden salir de las mismas piezas.",
    ],
    [("reciclar", "usar de nuevo materiales que ya se usaron"), ("estructura", "el armazón que sostiene una obra"), ("equilibrio", "cuando algo se mantiene firme sin caerse"), ("base", "la parte de abajo que sostiene todo"), ("transformar", "cambiar algo para que sea otra cosa")],
    [
        w("Una torre firme", "Tienes una caja grande y una caja chica. ¿Cuál va abajo para que tu torre no se caiga?", ["La caja grande ocupa más espacio en la mesa.", "Eso da una base ancha.", "La caja chica va encima."], "La caja grande va abajo"),
        w("Un robot con tubos", "Usas un tubo de cartón de cuerpo, dos tapas de ojos y una caja pequeña de cabeza. ¿Cómo lo armas para que se sostenga?", ["Pego el tubo parado sobre una base de cartón ancha.", "Pego la caja pequeña arriba.", "Pego las tapas en la caja como ojos."], "Tubo sobre base ancha, caja arriba y tapas como ojos"),
    ],
    [
        m("Poner la caja más grande arriba y la más pequeña abajo.", "La base angosta no sostiene el peso de arriba.", "Pon las piezas más anchas y pesadas abajo."),
        m("Usar una lata con borde filoso porque se ve brillante.", "No se piensa en la seguridad.", "Usa solo envases limpios, secos y sin bordes filosos."),
    ],
    [
        ex("Para reciclar un tubo de cartón, ¿debe estar limpio y seco o sucio y mojado?", "Limpio y seco", "Así se pega mejor y se cuida la salud."),
        ex("Si una torre tiene la base angosta, ¿se cae con facilidad o queda firme?", "Se cae con facilidad", "La base angosta no da equilibrio."),
        ex("¿Qué va abajo en una escultura: las piezas anchas y pesadas, o las livianas?", "Las anchas y pesadas", "Dan una base firme."),
    ],
    [
        ex("¿Qué es la estructura de una escultura? A: el armazón que la sostiene. B: el color. C: el nombre.", "A", "La estructura es lo que mantiene firme la obra."),
        ex("Para cortar cartón con tijeras, ¿necesitas ayuda de un adulto?", "Sí", "Las tijeras requieren cuidado."),
        ex("Quieres hacer un animal con una caja de cuerpo y un tubo de cuello. ¿Dónde pegas el tubo: sobre la caja o debajo?", "Sobre la caja", "El cuello sale desde el cuerpo hacia arriba."),
    ],
    [
        arith("Armas un robot con 1 caja de cuerpo, 2 tubos de brazos, 2 tubos de piernas y 3 tapas de botones. ¿Cuántas piezas usaste?", "1 + 2 + 2 + 3", "Se suman todas las piezas."),
        ex("Tu torre se cae. ¿Cambias la base por una más ancha o la dejas igual?", "La cambias por una más ancha", "Una base ancha da más equilibrio."),
        ex("Ordena: A probar si se sostiene, B limpiar los materiales, C pegar las piezas.", "B, C, A", "Se limpian, se pegan y se prueba."),
    ],
    [
        ex("Ema dice: «Mi robot está firme porque lo apoyé sobre un tubo muy angosto». ¿Tiene razón?", "No", "Un apoyo angosto da poco equilibrio."),
        ex("Pía quiere usar vidrio roto como detalle. ¿Es buena idea? Explica.", "No; es peligroso", "El vidrio corta y no es un material seguro."),
    ],
    [
        arith("Tienes 18 tapas y pegas 6 en cada escultura. ¿Cuántas esculturas con 6 tapas puedes hacer?", "18 // 6", "Se reparten las 18 tapas en grupos de 6."),
        ex("Tu escultura de ciudad tiene una caja ancha abajo, una mediana al medio y una pequeña arriba. ¿Es una estructura estable?", "Sí", "Cada pieza es más pequeña que la de abajo."),
    ],
    ex("En tu casa guardan cajas de cereal limpias y secas. Quieres usarlas para una escultura. ¿Qué haces primero: ver que no tengan bordes filosos o pegarlas de inmediato?", "Ver que no tengan bordes filosos", "La seguridad va primero."),
    [
        ex("¿Qué significa reciclar?", "Usar de nuevo", "Reciclar es dar otro uso a materiales."),
        ex("Verdadero o falso: una base ancha da equilibrio.", "Verdadero", "Una base ancha mantiene firme la obra."),
        ex("¿Qué pieza va arriba: la más pesada o la más liviana?", "La más liviana", "Lo liviano arriba no desequilibra."),
    ],
    task(
        "Elige UNA idea: un robot, un animal o una ciudad. Constrúyela con materiales reciclados limpios (cajas, tubos y tapas). Debe sostenerse sola. Escribe cuántas piezas usaste y cómo hiciste la base.",
        "Elegí un animal. Usé 1 caja grande de cuerpo, 1 tubo de cuello, 1 caja pequeña de cabeza y 2 tapas de ojos. Total 5 piezas. La base es la caja grande, ancha y firme.",
        ["usa materiales limpios y seguros", "se sostiene sola", "explica su base", "anota cuántas piezas usó"],
        ["escultura reciclada", "una frase con piezas y base"],
        ["base angosta", "usar materiales peligrosos"],
        "Reconoce la parte más firme y pide que pruebe qué pasa si cambia la base para mejorar el equilibrio.",
    ),
    "Busca en casa tres materiales limpios que podrías reciclar y di qué objeto podrías armar.",
    "Haz una segunda versión con una pieza más pesada abajo y otra más liviana arriba. Anota cuál es más firme.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA3, 3,
    "Hojas de papel de distintos colores (de revista limpia, de envolver o de cuaderno), retazos de tela o lana, cola fría o barra adhesiva, una hoja de cartón de base y tijeras de punta roma con un adulto.",
    "Aprenderé a hacer un collage rasgando, recortando y superponiendo papeles y telas. Sirve para crear profundidad y contraste con materiales simples.",
    ["Sé pegar papel sobre papel.", "Sé cortar con tijeras con cuidado."],
    [
        "Un collage es una obra hecha pegando materiales distintos sobre una base, como papeles, telas y lana. Se pueden rasgar o recortar. El papel rasgado tiene un borde irregular y suave. El papel recortado tiene un borde recto y firme.",
        "Superponer es poner un material sobre otro. Si pegas un papel encima de otro, el de arriba parece más cerca y el de abajo más lejos. Así creas profundidad. Los materiales de textura distinta, como la tela y el papel, también hacen contraste. Los textiles son materiales hechos de hilos, como la tela y la lana. Pueden ser suaves, ásperos o con pelitos. Puedes recortarlos, pegarlos y también entrelazar hilos de lana. Si quieres, agrega materiales naturales, como una hoja seca o una ramita que encuentres en el suelo.",
        "Planifica tu collage antes de pegar. Ubica las piezas sobre la base y mueve hasta que te guste. Después pega de abajo hacia arriba. Usa poca cola para que no se arrugue. Con papeles rasgados puedes hacer nubes, pasto o agua. Con recortados puedes hacer casas o ventanas.",
    ],
    [("collage", "obra hecha pegando materiales distintos sobre una base"), ("rasgar", "romper el papel con las manos"), ("recortar", "cortar con tijeras"), ("superponer", "poner una pieza encima de otra"), ("profundidad", "sensación de que algo está más cerca y algo más lejos")],
    [
        w("Un paisaje de papel", "Quieres hacer un paisaje con cielo azul, un cerro y una casa. ¿Qué técnica usas para cada parte?", ["El cielo y el cerro son suaves: los hago con papel rasgado.", "La casa tiene bordes rectos: la hago con papel recortado.", "Pego el cerro sobre el cielo y la casa sobre el cerro."], "Cielo y cerro rasgados, casa recortada, todo superpuesto"),
        w("Textura con tela", "Quieres que un oso se vea suave. ¿Qué material usas para su cuerpo?", ["Busco un material de textura suave.", "Una tela de felpa o lana se ve suave.", "La pego sobre un papel recortado con forma de oso."], "Tela suave sobre papel recortado"),
    ],
    [
        m("Pegar mucha cola y dejar el papel arrugado.", "Se piensa que más cola pega mejor.", "Usa poca cola, en los bordes, y alisa con el dedo."),
        m("Pegar todas las piezas al mismo nivel, sin superponer.", "No se busca profundidad.", "Pega unas piezas sobre otras, de las más lejanas a las más cercanas."),
    ],
    [
        ex("Un papel rasgado tiene el borde irregular. ¿Es un borde recto o irregular?", "Irregular", "El papel rasgado no se corta parejo."),
        ex("Un papel recortado con tijeras suele tener el borde recto. ¿Verdadero o falso?", "Verdadero", "Las tijeras cortan en línea más pareja."),
        ex("Tomás pega un papel verde encima de un papel café para que el verde parezca más cerca. ¿Qué técnica usó?", "Superponer", "Poner una pieza sobre otra se llama superponer."),
    ],
    [
        ex("Si pegas un papel amarillo sobre uno azul, ¿cuál parece más cerca: el amarillo o el azul?", "El amarillo", "La pieza de arriba parece más cerca."),
        ex("¿Qué técnica usas para hacer una nube suave? A: rasgar papel. B: recortar con regla. C: pintar con rotulador.", "A", "El borde irregular se parece a una nube."),
        ex("Un textil es un material hecho de hilos. ¿Cuál es un textil: la lana o el cartón?", "La lana", "La lana se hace con hilos; el cartón no."),
    ],
    [
        arith("Tu collage lleva 3 papeles rasgados para el cielo, 2 para las montañas y 4 recortados para las casas. ¿Cuántos papeles usaste?", "3 + 2 + 4", "Se suman los papeles de cada parte."),
        ex("Quieres una ventana cuadrada en tu casa de papel. ¿La rasgas o la recortas?", "La recortas", "El borde recto se logra con tijeras."),
        ex("Ordena: A pegar de abajo hacia arriba, B ubicar las piezas sobre la base, C alisar con el dedo.", "B, A, C", "Se ubica primero, luego se pega y al final se alisa."),
    ],
    [
        ex("Tomás recortó con tijeras una nube y quedó con bordes rectos. ¿Qué técnica podría haber usado para que se vea más suave?", "Rasgar", "Un borde rasgado se ve más suave."),
        ex("Lola dice: «Si pego todo al mismo nivel, hay mucha profundidad». ¿Tiene razón?", "No", "Sin superponer no hay sensación de cerca y lejos."),
    ],
    [
        arith("Tienes 15 papeles y pegas 5 por cada árbol. ¿Cuántos árboles puedes completar?", "15 // 5", "Se reparten los 15 papeles en grupos de 5."),
        ex("En un collage del mar, el agua es de papel azul, la ola es de papel blanco encima y la espuma es lana. ¿Cuántos materiales o papeles diferentes hay?", "3", "Hay papel azul, papel blanco y lana."),
    ],
    ex("Para una tarjeta de cumpleaños quieres un pastel de papel café con una vela de papel rosado y una llama de lana amarilla en la punta. ¿Qué pegas primero: el pastel de papel café o la llama de lana amarilla?", "El pastel", "La llama va encima del pastel, así que se pega después."),
    [
        ex("¿Qué es un collage?", "Obra hecha pegando materiales", "El collage une materiales distintos."),
        ex("¿Qué se pega primero: lo que está más lejos o lo más cercano?", "Lo más lejano", "Se pega de abajo hacia arriba."),
        ex("Verdadero o falso: los papeles rasgados tienen bordes irregulares.", "Verdadero", "Al rasgar el borde queda irregular."),
    ],
    task(
        "Elige UNA idea: un paisaje, un animal o una ciudad. Haz un collage con papeles rasgados y recortados, y agrega un trozo de tela o de lana. Superpone al menos tres piezas. Escribe qué técnica usaste en cada parte.",
        "Elegí un paisaje. Rasgué papel azul para el cielo y verde para el cerro. Recorté una casa roja y pegué lana para el humo. Superpuse el cerro sobre el cielo y la casa sobre el cerro.",
        ["usa papeles rasgados y recortados", "agrega tela o lana", "superpone al menos tres piezas", "explica cada técnica"],
        ["collage terminado", "una frase por técnica"],
        ["pegar todo al mismo nivel", "mucha cola"],
        "Reconoce la técnica más lograda y pide que cambie el orden de una pieza para ver cómo cambia la profundidad.",
    ),
    "Rasga un papel y recorta otro. Compara los bordes y di en voz alta en qué se diferencian.",
    "Haz el mismo collage cambiando el orden de las capas y compara la profundidad.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA3, 4,
    "Témperas o acuarelas, un pincel grueso y uno fino, una esponja pequeña, un palito de helado o un cotonito, una tapa para mezclar, un diario viejo para proteger la mesa y una hoja gruesa.",
    "Aprenderé a pintar con herramientas distintas y a ver qué marca deja cada una. Sirve para expresar emociones con trazos suaves, fuertes, finos o gruesos.",
    ["Sé mojar el pincel en pintura.", "Conozco los colores primarios y secundarios."],
    [
        "Cada herramienta de pintura deja una marca distinta. El pincel grueso hace trazos anchos. El pincel fino hace líneas delgadas. La esponja deja una textura de puntitos. El palito o el cotonito hacen puntos y líneas pequeñas.",
        "Los trazos también expresan emociones. Trazos grandes y rápidos pueden mostrar energía. Trazos pequeños y suaves pueden mostrar calma. Los colores también ayudan. Puedes pintar un mismo cielo con la esponja para que se vea nublado o con el pincel grueso para que se vea tranquilo.",
        "Antes de pintar, prueba cada herramienta en una esquina de la hoja. Así descubres qué marca deja. Después elige la que mejor expresa tu idea. Limpia el pincel con agua al cambiar de color. Al terminar, lava las herramientas y lávate las manos.",
    ],
    [("herramienta", "objeto que uso para pintar, como un pincel o una esponja"), ("trazo", "la marca que deja el pincel al moverse"), ("textura", "cómo se ve o se siente la superficie"), ("procedimiento", "la manera de hacer algo, como pintar o modelar"), ("probar", "ensayar antes de hacer el trabajo final")],
    [
        w("Elegir la herramienta para un pasto", "Quieres pintar un pasto lleno de hierbitas. ¿Qué herramienta usas?", ["Las hierbitas son líneas delgadas y cortas.", "El pincel fino deja líneas delgadas.", "Pinto muchas líneas verdes cortas hacia arriba."], "Pincel fino"),
        w("Elegir la herramienta para nubes", "Quieres pintar nubes esponjosas. ¿Qué herramienta usas?", ["Las nubes tienen textura blanda.", "La esponja deja puntitos y bordes suaves.", "Mojo la esponja un poco en pintura blanca y la apoyo varias veces."], "Esponja"),
    ],
    [
        m("Usar el pincel grueso para dibujar detalles pequeños.", "No se elige la herramienta según el efecto.", "Prueba en una esquina y usa el fino para los detalles."),
        m("Cambiar de color sin limpiar el pincel.", "Se olvida limpiar.", "Limpia el pincel con agua y sécalo antes de usar otro color."),
    ],
    [
        ex("¿Qué herramienta deja un trazo ancho: el pincel grueso o el pincel fino?", "El pincel grueso", "El pincel grueso deja trazos anchos."),
        ex("¿Qué herramienta deja una textura de puntitos: la esponja o el pincel fino?", "La esponja", "La esponja deja puntitos al apoyarla."),
        ex("Antes de pintar, ¿pruebas la herramienta en una esquina o directo en el centro del trabajo?", "En una esquina", "Así sabes qué marca deja sin arruinar el trabajo."),
    ],
    [
        ex("¿Qué es un trazo? A: la marca que deja el pincel. B: un color. C: un tipo de papel.", "A", "El trazo es la huella del movimiento del pincel."),
        ex("Quieres mostrar calma con tu pintura. ¿Haces trazos pequeños y suaves o grandes y rápidos?", "Pequeños y suaves", "Los trazos suaves dan calma."),
        ex("Quieres pintar el tronco de un árbol. ¿Qué herramienta usas: pincel grueso o cotonito?", "Pincel grueso", "El tronco es ancho y se pinta con un trazo grueso."),
    ],
    [
        arith("Pintas un cielo con 4 manchas de esponja grandes y 6 manchas pequeñas. ¿Cuántas manchas hiciste?", "4 + 6", "Se suman las manchas grandes y las pequeñas."),
        ex("Quieres hacer las pecas de un niño en un dibujo. ¿Usas el cotonito o el pincel grueso?", "El cotonito", "Las pecas son puntos pequeños."),
        ex("Ordena: A limpiar el pincel, B pintar el color nuevo, C probar el trazo en una esquina.", "C, A, B", "Se prueba, se limpia el pincel y luego se pinta."),
    ],
    [
        ex("Ana pintó el mar con trazos pequeños y rápidos, pero quería mostrar calma. ¿Qué podría cambiar?", "Hacer trazos largos y suaves", "Los trazos largos y suaves dan sensación de calma."),
        ex("Beto dice: «Todas las herramientas dejan la misma marca». ¿Tiene razón?", "No", "Cada herramienta deja una marca distinta."),
    ],
    [
        ex("Quieres pintar una lluvia fuerte con líneas finas y rápidas. ¿Qué herramienta usas: pincel fino o esponja?", "Pincel fino", "Las gotas se representan con líneas delgadas."),
        arith("Pintas 3 filas de puntos con el cotonito y cada fila tiene 7 puntos. ¿Cuántos puntos pintas?", "3 * 7", "Se multiplica el número de filas por los puntos de cada una."),
    ],
    ex("En una clase pintan un atardecer. Una niña usa la esponja para el cielo y el pincel fino para las gaviotas. ¿Por qué eligió el pincel fino para las gaviotas?", "Porque son pequeñas y delgadas", "El pincel fino permite hacer detalles pequeños."),
    [
        ex("¿Qué herramienta hace líneas delgadas?", "Pincel fino", "Su punta es angosta."),
        ex("Verdadero o falso: es bueno probar la herramienta antes de pintar.", "Verdadero", "Se descubre la marca antes de empezar."),
        ex("Si mojas mucho la esponja, ¿la pintura se escurre o se mantiene firme?", "Se escurre", "Con mucha pintura la esponja chorrea."),
    ],
    task(
        "Elige UNA emoción: calma, alegría o energía. Pinta un paisaje con al menos tres herramientas distintas (pincel grueso, pincel fino, esponja, cotonito o palito). Antes de empezar, prueba cada herramienta en una esquina. Anota qué herramienta usaste para cada parte.",
        "Elegí alegría. Con el pincel grueso pinté un sol grande. Con la esponja hice nubes de puntitos. Con el cotonito pinté flores pequeñas. Probé todo en una esquina.",
        ["usa al menos tres herramientas", "prueba antes de pintar", "los trazos expresan la emoción", "anota qué usó en cada parte"],
        ["pintura terminada", "pruebas en la esquina", "una frase por herramienta"],
        ["no probar", "no limpiar el pincel al cambiar de color"],
        "Reconoce el trazo más expresivo y pide que pruebe otro trazo en una esquina para comparar.",
    ),
    "Haz en una hoja una marca con cada herramienta que tengas y di cuál es la más gruesa y cuál la más fina.",
    "Pinta el mismo objeto con trazos suaves y luego con trazos fuertes. Compara la emoción.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA3, 5,
    "Si hay un computador o tablet con programa de dibujo, úsalo con un adulto cerca (sin internet y sin datos personales). Si no, usa una hoja cuadriculada y lápices de colores: es la alternativa de esta clase.",
    "Aprenderé a dibujar con herramientas digitales, como lápiz, goma, relleno y deshacer, o con una cuadrícula en papel que funciona como una pantalla. Sirve para crear imágenes también sin papel.",
    ["Sé dibujar con lápiz en papel.", "Sé contar filas y columnas."],
    [
        "Un dibujo digital se hace en una pantalla con un programa de dibujo. Se dibuja con el ratón, con el dedo en una pantalla táctil o con un lápiz táctil. Las herramientas son parecidas a las de papel. El lápiz sirve para trazar. La goma borra. El relleno pinta una zona cerrada con un solo color. Deshacer vuelve atrás si te equivocas.",
        "Las imágenes digitales están hechas de cuadritos muy pequeños llamados píxeles. Si no tienes pantalla, puedes imitar esto en papel cuadriculado: pintas cuadritos para formar una imagen. Una imagen de 5 filas y 5 columnas tiene 25 cuadritos en total. Cada cuadrito que pintas es como un píxel.",
        "Planifica antes de dibujar. Elige la imagen, los colores y el tamaño. Empieza con el contorno y luego rellena. Una foto tomada con una cámara también es una imagen digital, pero hazlo siempre con ayuda de un adulto y no fotografíes a nadie sin permiso. Guarda tu trabajo y ponle un nombre que no incluya datos personales. Descansa la vista: mira lejos cada pocos minutos. El cuerpo y los ojos también cuentan.",
    ],
    [("píxel", "cuadradito muy pequeño que forma una imagen digital"), ("herramienta digital", "opción del programa para dibujar, borrar o pintar"), ("relleno", "herramienta que pinta una zona cerrada con un color"), ("deshacer", "volver atrás en el último paso"), ("cuadrícula", "hoja con cuadritos iguales en filas y columnas")],
    [
        w("Contar cuadritos de una imagen", "Un corazón en cuadrícula tiene en cada fila estos cuadritos pintados: 2, 5, 5, 3 y 1. ¿Cuántos cuadritos pintados tiene?", ["Anoto los números de cada fila: 2, 5, 5, 3, 1.", "Sumo 2 + 5 + 5 + 3 + 1."], "16 cuadritos"),
        w("Elegir la herramienta", "Pintaste un contorno de pez cerrado y quieres pintar todo su cuerpo de naranja. ¿Qué herramienta usas?", ["El cuerpo es una zona cerrada.", "El relleno pinta una zona cerrada con un solo color.", "Elijo naranja y hago clic dentro del contorno."], "Relleno"),
    ],
    [
        m("Usar el relleno en un contorno que tiene un hueco.", "El color se escapa a toda la imagen.", "Cierra el contorno y luego usa el relleno."),
        m("Poner mi nombre completo y mi dirección como título del archivo.", "No se cuida la información personal.", "Usa un título sencillo, como «Mi pez naranja»."),
    ],
    [
        ex("La herramienta que borra en un programa de dibujo, ¿es la goma o el relleno?", "La goma", "La goma borra lo que dibujaste."),
        ex("La herramienta que vuelve atrás un paso, ¿se llama deshacer o relleno?", "Deshacer", "Deshacer anula el último cambio."),
        ex("Una imagen digital está hecha de cuadritos muy pequeños. ¿Cómo se llaman?", "Píxeles", "Ese es el nombre de los cuadritos que forman la imagen."),
    ],
    [
        ex("¿Qué hace la herramienta relleno? A: pinta una zona cerrada con un color. B: borra todo. C: apaga la pantalla.", "A", "El relleno cubre una zona cerrada."),
        ex("En una pantalla táctil, ¿con qué puedes dibujar: con el dedo o con una tijera?", "Con el dedo", "En una pantalla táctil se dibuja con el dedo o con un lápiz táctil."),
        ex("Si no tienes pantalla, ¿qué puedes usar para imitar los píxeles: una hoja cuadriculada o una hoja lisa?", "Una hoja cuadriculada", "Los cuadritos del papel funcionan como píxeles."),
    ],
    [
        arith("Una imagen en cuadrícula tiene 5 filas y 5 columnas. ¿Cuántos cuadritos tiene en total?", "5 * 5", "Se multiplica el número de filas por el de columnas."),
        arith("Un corazón en cuadrícula tiene estos cuadritos pintados por fila: 2, 5, 5, 3 y 1. ¿Cuántos cuadritos pintaste en total?", "2 + 5 + 5 + 3 + 1", "Se suman los cuadritos pintados de cada fila."),
        ex("Ordena: A usar el relleno, B dibujar el contorno cerrado, C elegir la imagen.", "C, B, A", "Se elige, se dibuja el contorno y se rellena."),
    ],
    [
        ex("Ema usó el relleno en un contorno abierto y todo el fondo se pintó del mismo color. ¿Qué debe hacer?", "Deshacer y cerrar el contorno", "Con el contorno cerrado el color queda adentro."),
        ex("Pedro dice: «Pongo mi nombre y mi dirección al archivo para no olvidarlo». ¿Es buena idea?", "No", "No se comparten datos personales."),
    ],
    [
        arith("Una flor en cuadrícula tiene 3 filas de 4 cuadritos pintados. ¿Cuántos cuadritos pintados tiene?", "3 * 4", "Se multiplican las filas por los cuadritos de cada una."),
        arith("En esa cuadrícula de 5 × 5 hay 16 cuadritos pintados. ¿Cuántos quedaron sin pintar?", "25 - 16", "Se resta lo pintado al total de 25."),
    ],
    ex("Tu profesora te pide guardar tu dibujo digital con un nombre. ¿Eliges «Mi casa de colores» o tu nombre completo con tu curso?", "Mi casa de colores", "El título debe describir el dibujo sin datos personales."),
    [
        ex("¿Qué herramienta pinta una zona cerrada?", "Relleno", "Eso hace el relleno."),
        ex("Verdadero o falso: se puede hacer un dibujo digital sin computador usando una cuadrícula.", "Verdadero", "La cuadrícula imita los píxeles."),
        ex("¿Qué debes hacer con la vista cada pocos minutos?", "Mirar lejos", "Descansar la vista cuida los ojos."),
    ],
    task(
        "Elige UNA imagen: una flor, un pez o un corazón. Hazla en un programa de dibujo con al menos tres herramientas (lápiz, goma, relleno o deshacer), o en papel cuadriculado de 8 filas y 8 columnas pintando cuadritos. Anota qué herramientas usaste o cuántos cuadritos pintaste. Título sin datos personales.",
        "Elegí un pez en cuadrícula de 8 × 8. Pinté 20 cuadritos: 14 naranjas y 6 azules. Título: «Mi pez naranja».",
        ["crea la imagen con herramientas digitales o cuadrícula", "anota herramientas o cuadritos", "titula sin datos personales"],
        ["imagen terminada", "una frase con el conteo o las herramientas"],
        ["poner datos personales en el título", "usar el relleno sin cerrar el contorno"],
        "Reconoce una decisión bien tomada y pide que cuente de nuevo los cuadritos o repase las herramientas.",
    ),
    "Dibuja con el dedo en el aire una forma y luego imagina cómo la harías con cuadritos. Cuéntaselo a alguien.",
    "Haz la misma imagen en una cuadrícula más grande y compara cuántos cuadritos necesitas.",
)

# ================================================================ OA 04
# ---------------------------------------------------------------- Clase 1
lesson(
    OA4, 1,
    "Lápiz y una hoja para anotar. Las obras de esta clase son tres descripciones inventadas para practicar. Si puedes, un adulto te muestra imágenes de obras reales de museos o libros.",
    "Aprenderé a describir lo que veo en una obra antes de decir lo que creo que significa. Sirve para mirar con cuidado y no apresurarme.",
    ["Sé nombrar colores y formas.", "Sé decir qué siento ante una imagen."],
    [
        "Cuando miras una obra de arte, primero describe lo que ves. Describir es decir qué hay, sin agregar historias: los colores, las formas, las líneas, cuántos objetos hay y dónde están. Después puedes interpretar, que es decir qué crees que significa o qué historia cuenta.",
        "Mira la obra G, descrita para esta clase: una pintura de una casa pequeña en un campo oscuro. Tiene una sola ventana amarilla encendida, un cielo azul oscuro con nubes y líneas horizontales largas en el suelo. Describir sería decir: veo una casa, una ventana amarilla y un cielo azul oscuro. Interpretar sería decir: creo que alguien espera a su familia.",
        "Primero describe y después interpreta. Si te saltas la descripción, puedes inventar cosas que la obra no tiene. Esto sirve con cualquier obra: una local de tu barrio, una chilena, una latinoamericana o una de otro continente. Las obras G, H e I están inventadas para practicar; pide a tu docente o a un adulto que te muestre obras reales. Una buena forma de empezar es contar cuántas cosas ves, nombrar los colores y decir dónde están. Con esos datos tus ideas son más firmes.",
    ],
    [("describir", "decir lo que veo, sin agregar historias"), ("interpretar", "decir lo que creo que significa o cuenta"), ("detalle", "una parte pequeña pero importante"), ("obra", "trabajo que hace un artista"), ("impresión", "lo que siento o pienso al mirar")],
    [
        w("Describir la obra G", "Obra G: casa pequeña, ventana amarilla, cielo azul oscuro con nubes y suelo con líneas horizontales largas. Escribe una descripción de tres datos.", ["Anoto lo que se ve: una casa pequeña.", "Anoto un detalle: una sola ventana amarilla encendida.", "Anoto el fondo: cielo azul oscuro con nubes."], "Casa pequeña, ventana amarilla y cielo azul oscuro"),
        w("Separar describir de interpretar", "Un niño dice: «Hay una ventana amarilla, y creo que la familia está unida». ¿Qué parte describe y cuál interpreta?", ["«Hay una ventana amarilla» es algo que se ve.", "«La familia está unida» es una idea que no se ve en la obra.", "La primera frase describe y la segunda interpreta."], "Describe la ventana; interpreta la unión de la familia"),
    ],
    [
        m("Decir «hay una familia feliz» cuando la obra solo muestra una casa y una ventana.", "Se interpreta sin describir antes lo que hay.", "Di primero: hay una casa y una ventana amarilla. Luego di qué piensas."),
        m("Decir solo «es bonita» y nada más.", "No se observa nada concreto.", "Agrega al menos un detalle que veas."),
    ],
    [
        ex("En la obra G, ¿cuántas ventanas hay encendidas?", "1", "La descripción dice que hay una sola ventana amarilla encendida."),
        ex("En la obra G, ¿de qué color es el cielo?", "Azul oscuro", "La descripción dice cielo azul oscuro con nubes."),
        ex("Un niño dice: «Veo una casa pequeña». ¿Eso describe o interpreta la obra G?", "Describe", "Dice lo que se ve sin agregar historias."),
    ],
    [
        ex("¿Qué es interpretar una obra? A: decir qué creo que significa. B: contar los colores. C: copiar la obra.", "A", "Interpretar es dar una idea de lo que cuenta la obra."),
        ex("«Creo que alguien espera a su familia». ¿Describe o interpreta?", "Interpreta", "No es algo que se vea; es una idea."),
        ex("¿Qué haces primero: describir lo que ves o interpretar?", "Describir lo que veo", "La descripción da datos para interpretar mejor."),
    ],
    [
        arith("La obra G tiene 1 casa, 1 ventana y 3 nubes. ¿Cuántas cosas cuentas en total?", "1 + 1 + 3", "Se suman la casa, la ventana y las nubes."),
        ex("Ordena de lo que se ve a lo que se piensa: A «creo que es de noche y hay silencio», B «veo un cielo azul oscuro», C «veo una ventana amarilla».", "B, C, A", "Primero se describen el cielo y la ventana, y al final se interpreta."),
        ex("Clasifica: «hay líneas horizontales largas en el suelo». ¿Describe o interpreta?", "Describe", "Habla de líneas que se ven."),
    ],
    [
        ex("Ema dice: «La casa de la obra G es triste y tiene problemas». ¿Qué debe hacer antes de decir eso?", "Describir lo que ve", "Antes de interpretar, conviene decir qué hay en la obra."),
        ex("Beto dice: «No necesito mirar la obra, ya sé qué cuenta». ¿Tiene razón?", "No", "Sin mirar no se puede describir ni interpretar bien."),
    ],
    [
        ex("En una frase hay dos partes: «Veo una ventana amarilla y creo que alguien la dejó encendida para esperar». ¿Cuántas ideas son descripción?", "1", "Solo «veo una ventana amarilla» es descripción; la otra es interpretación."),
        ex("Obra H, descrita para esta clase: una escultura de barro con dos figuras muy juntas, de color terracota. Un niño dice: «Las figuras se quieren mucho». ¿Describe o interpreta?", "Interpreta", "El cariño no se ve directamente; es una idea sobre la obra."),
    ],
    ex("En la escuela miran la obra I, descrita así: un collage con círculos rojos y naranjas que giran en espiral sobre un fondo amarillo. Un niño dice «hay círculos rojos y naranjas». ¿Describe o interpreta?", "Describe", "Dice lo que se ve sin agregar una historia."),
    [
        ex("¿Qué se hace al describir una obra?", "Decir lo que se ve", "Describir es nombrar lo que hay."),
        ex("Verdadero o falso: puedes interpretar sin haber descrito.", "Falso", "Primero se describe para tener datos."),
        ex("«Creo que es un día feliz». ¿Describe o interpreta?", "Interpreta", "Es una idea, no un dato visible."),
    ],
    task(
        "Elige UNA obra de las descritas en este cuaderno: G (casa con ventana amarilla en un campo oscuro), H (dos figuras de barro color terracota muy juntas) o I (círculos rojos y naranjas en espiral sobre un fondo amarillo). Escribe tres frases que describan lo que ves (colores, formas y cuántas hay). Después escribe una frase que interprete.",
        "Elegí la obra I. Veo círculos rojos y naranjas. Veo una espiral. El fondo es amarillo. Creo que el collage es un día de mucha energía.",
        ["escribe tres frases de descripción", "separa descripción de interpretación", "usa datos que están en la descripción de la obra"],
        ["tres frases descriptivas", "una frase interpretativa"],
        ["mezclar descripción con historia", "no mencionar ni un color o forma"],
        "Reconoce los datos bien observados y pide que identifique cuál frase es interpretación.",
    ),
    "Mira un objeto de tu casa durante un minuto y di tres cosas que ves, sin agregar historias.",
    "Con ayuda de tu docente o de un adulto, mira una obra real y descríbela con tres datos. Anota si es local, chilena, latinoamericana o de otro continente.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA4, 2,
    "Lápiz y una hoja para anotar. Las obras G, H e I son descripciones inventadas, escritas en este cuaderno. Si puedes, un adulto te muestra imágenes de obras reales.",
    "Aprenderé a comunicar lo que siento al mirar una obra y a decir qué elemento visual me hace sentirlo. Sirve para explicar mis impresiones con razones.",
    ["Sé describir lo que veo en una obra.", "Sé nombrar emociones como calma, alegría o susto."],
    [
        "Una impresión es lo que sientes o piensas al mirar una obra. No hay impresiones correctas o incorrectas: lo que sientes es tuyo. Pero para comunicarla bien, une tu impresión con algo que ves. Así tu impresión no queda en el aire.",
        "Usa esta frase: «Siento ___ porque veo ___». Por ejemplo, en la obra G: «Siento calma porque veo líneas horizontales y un cielo azul oscuro». El cielo y las líneas son los elementos visuales. Los elementos visuales son el color, la línea, la forma y el material.",
        "Sostener una impresión significa explicar por qué la tienes. Una frase como «me gusta porque sí» no ayuda a otros a entenderte. En cambio, «me alegra porque hay círculos naranjas que giran» deja claro qué observaste. Puedes comunicar tu impresión hablando, escribiendo o dibujando.",
    ],
    [("impresión", "lo que siento o pienso al mirar una obra"), ("elemento visual", "color, línea, forma o material que veo en una obra"), ("sostener", "dar razones de por qué pienso o siento algo"), ("comunicar", "contar a otros lo que pienso o siento"), ("razón", "el motivo que explica una idea")],
    [
        w("Impresión con razón", "Obra I: círculos rojos y naranjas que giran sobre un fondo amarillo. Escribe una impresión con razón.", ["Digo qué siento: alegría.", "Busco qué veo que me hace sentirlo: los colores cálidos y las vueltas.", "Uno las dos partes."], "Siento alegría porque veo colores cálidos que giran"),
        w("Mejorar una frase sin razón", "Un niño dice: «La obra H me gusta porque sí». ¿Cómo la mejoras?", ["Miro la obra: dos figuras de barro muy juntas.", "Digo qué elemento me llama la atención: el color terracota.", "Escribo: me gusta porque el color terracota se ve cálido."], "Me gusta porque el color terracota se ve cálido"),
    ],
    [
        m("Decir «me gusta porque sí» o «es linda».", "No se explica qué se ve.", "Agrega un elemento visual: color, línea, forma o material."),
        m("Pensar que mi impresión es incorrecta porque es distinta a la de otra persona.", "Se cree que hay una impresión única.", "Cada persona siente distinto; lo importante es dar una razón desde lo que ve."),
    ],
    [
        ex("En la frase «Siento calma porque veo líneas horizontales», ¿cuál es el elemento visual?", "Líneas horizontales", "Es lo que se ve y explica la calma."),
        ex("En esa misma frase, ¿qué siente la persona?", "Calma", "La emoción nombrada es calma."),
        ex("¿Los elementos visuales son color, línea, forma y material, o nombre del artista?", "Color, línea, forma y material", "Son lo que vemos en la obra."),
    ],
    [
        ex("¿Qué significa sostener una impresión? A: dar razones de por qué la siento. B: guardarla en secreto. C: copiar la de otro.", "A", "Sostener es explicar el motivo."),
        ex("Obra G. «Siento tranquilidad porque veo una ventana amarilla encendida». ¿Cuál es el elemento visual?", "Una ventana amarilla encendida", "Eso es lo que se ve y causa la impresión."),
        ex("Dos niñas sienten distinto ante la misma obra. ¿Hay una impresión correcta y otra incorrecta?", "No", "Cada una puede sentir distinto si da razones desde lo que ve."),
    ],
    [
        ex("Completa: «Siento energía porque veo ___». ¿Qué elemento de la obra I sirve como razón? A: círculos que giran. B: un museo. C: el nombre del autor.", "A", "Los círculos que giran se ven en la obra I; las otras opciones no son elementos visuales."),
        ex("Ordena para comunicar una impresión: A nombrar la emoción, B decir el elemento visual que la causa, C mirar la obra con atención.", "C, A, B", "Primero se mira, luego se nombra la emoción y después se da la razón."),
        arith("Una niña nombra 2 colores y 3 formas de una obra. ¿Cuántos elementos visuales nombró?", "2 + 3", "Se suman los colores y las formas."),
    ],
    [
        ex("Tomás dice: «La obra H me da tristeza porque sí». ¿Qué le falta a su frase?", "Un elemento visual como razón", "Falta decir qué ve que lo hace sentir así."),
        ex("Eva dice: «Mi impresión no importa porque la maestra piensa otra cosa». ¿Tiene razón?", "No", "Toda impresión importa si se explica con razones."),
    ],
    [
        ex("En «Siento miedo porque el campo es oscuro y solo hay una luz», ¿cuántos elementos visuales nombra?", "2", "Nombra el campo oscuro y la luz."),
        ex("Obra H: dos figuras de barro muy juntas, color terracota. Una niña dice «Siento cariño porque las figuras están muy juntas». ¿Qué elemento visual usa?", "Que las figuras están muy juntas", "Lo que ve es la cercanía entre las figuras."),
    ],
    ex("En un museo escolar, tu curso mira la obra I. Un compañero dice: «Siento energía porque veo círculos que giran». ¿Su impresión tiene una razón visual o no?", "Tiene una razón visual", "Une lo que siente con lo que ve."),
    [
        ex("¿Qué dos partes tiene una buena impresión?", "Lo que siento y lo que veo", "Se une la emoción con una razón visual."),
        ex("Verdadero o falso: puedo sentir algo distinto a mis compañeros ante la misma obra.", "Verdadero", "Las impresiones son personales."),
        ex("¿Es un elemento visual el color amarillo?", "Sí", "El color es uno de los elementos visuales."),
    ],
    task(
        "Elige UNA obra: G (casa con ventana amarilla en un campo oscuro), H (dos figuras de barro color terracota muy juntas) o I (círculos rojos y naranjas en espiral sobre un fondo amarillo). Escribe tres frases con esta forma: «Siento ___ porque veo ___». En cada frase usa un elemento visual distinto (color, línea, forma o material).",
        "Elegí la obra G. 1) Siento calma porque veo un cielo azul oscuro. 2) Siento un poco de soledad porque veo una sola casa. 3) Siento tibieza porque veo una ventana amarilla.",
        ["usa la forma «siento… porque veo…» tres veces", "cada razón es un elemento visual distinto", "las razones están en la descripción de la obra"],
        ["tres frases escritas"],
        ["frases sin razón", "razones que no están en la obra"],
        "Reconoce la razón mejor argumentada y pide que mire de nuevo la obra para encontrar otro elemento visual.",
    ),
    "Mira un objeto de tu casa y di cómo te hace sentir y por qué, usando un color o una forma.",
    "Explica la misma impresión dibujando en vez de escribir. Elige un color y una forma que la muestren.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA4, 3,
    "Lápiz y una hoja para anotar. La obra G es una descripción inventada, escrita en este cuaderno: una casa pequeña con una ventana amarilla encendida en un campo oscuro, cielo azul oscuro con nubes y líneas horizontales largas en el suelo.",
    "Aprenderé a ver que una misma obra puede interpretarse de dos maneras y a comparar esas miradas con respeto. Sirve para escuchar a otros y aprender de ellos.",
    ["Sé describir lo que veo en una obra.", "Sé explicar lo que siento con una razón."],
    [
        "Una misma obra puede interpretarse de distintas maneras. No porque alguien esté equivocado, sino porque cada persona mira con sus propias experiencias. Una interpretación es válida si se apoya en algo que se ve en la obra.",
        "Mira la obra G. Ana dice: «Se ve solitaria porque hay una sola casa en un campo oscuro y grande». Luis dice: «Se ve acogedora porque la ventana amarilla da una luz cálida». Ambos usan elementos visuales distintos. Ana mira el campo oscuro y la única casa. Luis mira la ventana amarilla.",
        "Para comparar interpretaciones, pregúntate: ¿qué ve cada persona? ¿Qué elemento usa como razón? ¿En qué se parecen y en qué no? Puedes decir: «Veo lo mismo que tú, pero lo interpreto distinto». Esto sirve con obras de cualquier lugar, también con las reales que te muestre tu docente. Aceptar otra mirada no significa cambiar la tuya. Significa que puedes ver más cosas.",
    ],
    [("interpretación", "idea sobre lo que cuenta o significa una obra"), ("mirada", "la manera personal de ver algo"), ("válida", "que se apoya en algo que se ve"), ("comparar", "mirar en qué se parecen y en qué se diferencian dos ideas"), ("acogedora", "que se siente cálida y agradable")],
    [
        w("Dos miradas, una obra", "Ana dice que la obra G es solitaria por el campo oscuro. Luis dice que es acogedora por la ventana amarilla. ¿Cuál elemento usa cada uno?", ["Ana usa el campo oscuro y la única casa.", "Luis usa la ventana amarilla y su luz cálida."], "Ana: campo oscuro y una casa. Luis: ventana amarilla"),
        w("Aceptar otra mirada", "Tú ves la obra G como tranquila. Un amigo la ve como solitaria. ¿Qué puedes decir?", ["Veo lo mismo que él: una casa, un campo oscuro y una ventana.", "Lo interpreto distinto, y su razón también se apoya en algo que se ve.", "Puedo decir: veo lo mismo, pero lo interpreto de otra manera."], "Veo lo mismo, pero lo interpreto distinto"),
    ],
    [
        m("Decir «tu interpretación está mal» a otra persona.", "Se cree que hay una sola manera de interpretar.", "Pregunta qué elemento visual usó para su razón y compara con el tuyo."),
        m("Cambiar mi opinión solo porque alguien la dijo más fuerte.", "No se piensa en las razones.", "Compara las razones y mantén tu mirada si tiene sentido para ti."),
    ],
    [
        ex("Ana ve la obra G como solitaria. ¿Qué elemento usa: el campo oscuro o la ventana amarilla?", "El campo oscuro", "Ana menciona el campo oscuro y la única casa."),
        ex("Luis ve la obra G como acogedora. ¿Qué elemento usa?", "La ventana amarilla", "Luis menciona la luz cálida de la ventana amarilla."),
        ex("¿Pueden dos personas mirar la misma obra y verla distinto?", "Sí", "Cada persona mira con sus propias experiencias."),
    ],
    [
        ex("¿Cuándo una interpretación es válida? A: cuando se apoya en algo que se ve. B: cuando todos opinan igual. C: cuando es la más fuerte.", "A", "Una interpretación válida tiene una razón visual."),
        ex("Ana y Luis miran la misma obra. ¿Ven los mismos objetos (casa, ventana, campo)?", "Sí", "Ven lo mismo pero lo interpretan distinto."),
        ex("«Esta obra es acogedora» sin ninguna razón, ¿es una interpretación bien apoyada?", "No", "Falta decir qué elemento visual la sostiene."),
    ],
    [
        ex("Ordena para comparar dos miradas: A decir en qué se parecen, B escuchar la razón del otro, C decir mi razón.", "C, B, A", "Primero explico, luego escucho y al final comparo."),
        arith("Ana nombra 2 elementos visuales y Luis nombra 1. ¿Cuántos elementos nombran en total?", "2 + 1", "Se suman los elementos de ambos."),
        ex("Tú dices «veo tranquilidad porque las líneas del suelo son horizontales». ¿Cuál es tu elemento visual?", "Las líneas horizontales del suelo", "Es lo que se ve y apoya tu razón."),
    ],
    [
        ex("Mario dice: «Si Luis ve la obra acogedora, entonces yo también debo verla así». ¿Tiene razón?", "No", "Cada uno puede mirar con sus razones."),
        ex("Ema dice: «Mi amiga y yo vemos distinto, así que una de las dos se equivoca». ¿Es cierto?", "No", "Puede haber dos interpretaciones válidas si ambas se apoyan en lo que se ve."),
    ],
    [
        ex("En la obra G, una niña dice «Se ve misteriosa porque el cielo es muy oscuro». Otro dice «Se ve tranquila porque el cielo es muy oscuro». ¿Usan el mismo elemento visual?", "Sí", "Ambos usan el cielo oscuro, pero lo interpretan distinto."),
        ex("En la misma discusión, ¿cuántas interpretaciones distintas hay?", "2", "Una dice misteriosa y la otra tranquila."),
    ],
    ex("En la clase comparan la obra G. Un compañero dice que da frío y tú dices que da calidez. Ambos dicen su razón. ¿Qué haces después: discutir para ganar o escuchar y comparar?", "Escuchar y comparar", "Se aprende más al ver las razones de ambos."),
    [
        ex("¿Qué elemento usó Luis?", "La ventana amarilla", "Luis habla de la luz cálida de la ventana."),
        ex("Verdadero o falso: dos miradas pueden ser válidas a la vez.", "Verdadero", "Si ambas se apoyan en lo que se ve."),
        ex("¿Qué puedes decir para aceptar otra mirada: «veo lo mismo pero lo interpreto distinto» o «estás equivocado»?", "Veo lo mismo pero lo interpreto distinto", "Es respetuoso y claro."),
    ],
    task(
        "Mira la obra G. Escribe dos interpretaciones distintas de ella, cada una con su razón visual (por ejemplo: «solitaria porque…» y «acogedora porque…»). Después escribe qué elemento usó cada una y una frase que empiece con «Veo lo mismo, pero…».",
        "Interpretación 1: se ve solitaria porque hay una sola casa en un campo grande. Interpretación 2: se ve acogedora porque la ventana amarilla da luz. Elemento 1: la única casa. Elemento 2: la ventana. Veo lo mismo, pero uno mira el campo y otro mira la luz.",
        ["escribe dos interpretaciones", "cada una tiene una razón visual", "identifica el elemento", "usa la frase «veo lo mismo, pero…»"],
        ["dos interpretaciones escritas", "una frase de comparación"],
        ["interpretaciones sin razón", "decir que una está mal"],
        "Reconoce la razón mejor apoyada y pide que explique qué cambió entre ambas miradas.",
    ),
    "Pregunta a alguien de tu casa qué siente ante una imagen que veas y compara su razón con la tuya.",
    "Busca una tercera interpretación de la obra G y escribe su razón visual.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA4, 4,
    "Hoja, lápices de colores, lápiz de mina. Para el movimiento no necesitas materiales. La obra I está descrita en este cuaderno: un collage con círculos rojos y naranjas que giran en espiral sobre un fondo amarillo.",
    "Aprenderé a responder a una obra por otro medio, como un dibujo, unas palabras, un color o un movimiento. Sirve para expresar lo que siento cuando no encuentro las palabras.",
    ["Sé describir y dar una impresión con una razón.", "Sé que hay muchas formas de comunicar."],
    [
        "No siempre hay que responder a una obra hablando. Puedes responder con un dibujo, con palabras escritas, con un color, con un sonido hecho con tu voz o con un movimiento. Se llama responder por otro medio. Cada medio muestra tu impresión de manera distinta.",
        "Mira la obra I: círculos rojos y naranjas que giran en espiral sobre un fondo amarillo. Si sientes energía, puedes dibujar una espiral con colores cálidos. Puedes escribir dos líneas: «Giro, giro / como el sol». Puedes pintar un cuadrado solo con rojo y naranja. O puedes mover los brazos en círculos.",
        "Para responder por otro medio, sigue tres pasos. Primero, mira la obra y di qué sientes. Segundo, elige el medio que mejor muestra eso. Tercero, explica en una frase qué elemento de la obra te inspiró. Así otros entienden tu respuesta, aunque no uses muchas palabras.",
    ],
    [("responder", "contestar a una obra con mi impresión"), ("medio", "la manera en que expreso algo: dibujo, palabras, color o movimiento"), ("movimiento", "usar el cuerpo para mostrar una idea"), ("espiral", "línea que da vueltas alrededor de un centro"), ("inspirar", "darme una idea para crear")],
    [
        w("Responder con un dibujo", "Obra I: círculos rojos y naranjas que giran. Sientes energía. ¿Cómo respondes con un dibujo?", ["Miro la obra: colores cálidos y vueltas.", "Elijo dibujar una espiral con rojo y naranja.", "Escribo una frase: me inspiraron los círculos que giran."], "Una espiral roja y naranja con una frase de explicación"),
        w("Responder con movimiento", "Obra I: sientes que todo gira. ¿Cómo respondes con movimiento?", ["Elijo mover los brazos en círculos.", "Lo hago lento y luego rápido.", "Explico: giré porque en la obra todo da vueltas."], "Mover los brazos en círculos y explicar por qué"),
    ],
    [
        m("Pensar que solo hablar vale como respuesta.", "Se olvidan otros medios.", "Elige dibujar, escribir, pintar un color o moverte."),
        m("Responder con un dibujo sin explicar qué te inspiró.", "Los demás no entienden la relación con la obra.", "Escribe una frase que diga qué elemento te inspiró."),
    ],
    [
        ex("Responder a una obra dibujando, ¿es responder por otro medio?", "Sí", "El dibujo es un medio distinto a hablar."),
        ex("En la obra I, ¿qué forma gira?", "Círculos", "La descripción habla de círculos que giran en espiral."),
        ex("Mover los brazos en círculos para responder a la obra I, ¿es un medio de movimiento?", "Sí", "El cuerpo es el medio."),
    ],
    [
        ex("¿Cuál NO es un medio para responder a una obra? A: dibujar. B: escribir dos líneas. C: ignorar la obra.", "C", "Ignorar no es responder."),
        ex("Si respondes con un color, ¿qué colores usarías para la energía de la obra I?", "Rojo y naranja", "Son los colores cálidos de la obra."),
        ex("¿Para qué sirve la frase que explica tu respuesta?", "Para que otros entiendan qué te inspiró", "Une tu respuesta con la obra."),
    ],
    [
        ex("Ordena para responder por otro medio: A explicar qué te inspiró, B elegir el medio, C mirar la obra y decir qué sientes.", "C, B, A", "Se mira, se elige el medio y se explica."),
        arith("Respondes con 3 espirales dibujadas y 2 frases escritas. ¿Cuántas cosas hiciste en total?", "3 + 2", "Se suman espirales y frases."),
        ex("Quieres responder a la obra I con un sonido hecho con tu voz. ¿Haces un sonido que gira y sube o uno quieto y bajo?", "Un sonido que gira y sube", "La obra tiene círculos que giran, con energía."),
    ],
    [
        ex("Pía dibujó una espiral roja. Dice: «Me inspiró la obra». ¿Qué le falta a su respuesta?", "Explicar qué elemento la inspiró", "Falta decir que fue la espiral de la obra."),
        ex("Juan dice: «Yo no sé qué decir, así que no puedo responder». ¿Qué puede hacer?", "Elegir otro medio, como dibujar o moverse", "Hay otros medios para responder."),
    ],
    [
        ex("Una niña responde a la obra I con un color amarillo suave. Dice: «Me inspiró el fondo». ¿Qué elemento de la obra usó?", "El fondo amarillo", "Tomó el fondo como inspiración."),
        ex("Un niño responde con un movimiento de giro y con dos palabras. ¿Cuántos medios usó?", "2", "El movimiento es un medio y las palabras son otro."),
    ],
    ex("En clase comparten respuestas a la obra I. Una compañera dibuja, otro escribe y una más se mueve. ¿Cuántos medios distintos hay?", "3", "Dibujo, escritura y movimiento son tres medios."),
    [
        ex("¿Qué debes hacer primero al responder a una obra?", "Mirarla y decir qué siento", "Primero se mira, luego se elige el medio."),
        ex("Verdadero o falso: se puede responder a una obra con un movimiento.", "Verdadero", "El movimiento es un medio válido."),
        ex("¿Qué escribes en la frase de explicación?", "Qué elemento de la obra me inspiró", "Eso conecta mi respuesta con la obra."),
    ],
    task(
        "Elige UNA obra: G (casa con ventana amarilla en un campo oscuro), H (dos figuras de barro color terracota muy juntas) o I (círculos rojos y naranjas en espiral sobre un fondo amarillo). Responde a ella por UN medio distinto a hablar: un dibujo, dos líneas de palabras, un color pintado o un movimiento. Después escribe una frase: «Me inspiró ___».",
        "Elegí la obra H. Respondí con un dibujo: dos círculos terracota muy juntos. Me inspiró que las figuras estaban muy juntas.",
        ["responde por un medio distinto a hablar", "se nota la relación con la obra", "escribe la frase de inspiración"],
        ["respuesta (dibujo, palabras, color o movimiento)", "frase de inspiración"],
        ["no explicar qué lo inspiró", "responder sin mirar la obra"],
        "Reconoce el medio elegido y pide que explique qué parte de la obra se ve en su respuesta.",
    ),
    "Responde con un movimiento a una canción que escuches en casa y di qué sentiste.",
    "Responde a la misma obra por un segundo medio distinto y compara cuál muestra mejor lo que sentiste.",
)

# ================================================================ OA 05
# ---------------------------------------------------------------- Clase 1
lesson(
    OA5, 1,
    "Lápiz y una hoja para anotar. Los tres trabajos de esta clase son descripciones inventadas de dibujos de otros niños. Trabajo 1: pintura con muchos puntos azules y una luna amarilla grande. Trabajo 2: collage de papel rasgado verde y café con una casa. Trabajo 3: dibujo de líneas quebradas rojas.",
    "Aprenderé a explicar qué me gusta de un trabajo de arte usando color, línea, forma o material. Sirve para decir mis preferencias con razones.",
    ["Sé nombrar colores, líneas y formas.", "Sé decir si algo me gusta o no."],
    [
        "Una preferencia es lo que te gusta más. Todos tenemos preferencias distintas, y está bien. Para explicarla bien, usa los elementos del lenguaje visual: el color, la línea, la forma y el material. Así no solo dices «me gusta», sino por qué.",
        "Mira los tres trabajos. En el trabajo 1, los puntos azules y la luna amarilla tienen colores que contrastan. En el trabajo 2, el papel rasgado tiene bordes suaves. En el trabajo 3, las líneas quebradas rojas parecen tener energía. Puedes decir: «Me gusta el trabajo 3 porque las líneas quebradas se ven con energía».",
        "Una buena explicación tiene tres partes. Primero, di cuál trabajo prefieres. Segundo, nombra un elemento visual. Tercero, di qué efecto te produce. Si dices «me gusta porque es bonito», no se entiende qué ves. Mira con cuidado y usa las palabras del arte.",
    ],
    [("preferencia", "lo que me gusta más"), ("elemento del lenguaje visual", "color, línea, forma o material"), ("efecto", "lo que me produce lo que veo"), ("explicar", "decir las razones de algo"), ("trabajo de arte", "dibujo, pintura, collage o escultura que alguien crea")],
    [
        w("Explicar una preferencia", "Prefieres el trabajo 1 (puntos azules y luna amarilla). ¿Cómo lo explicas?", ["Digo cuál prefiero: el trabajo 1.", "Nombro el elemento: el contraste entre el azul y el amarillo.", "Digo el efecto: la luna se destaca mucho."], "Prefiero el trabajo 1 porque el amarillo contrasta con el azul"),
        w("Mejorar una explicación", "Un niño dice: «Me gusta el trabajo 2 porque es bonito». ¿Cómo la mejoras?", ["Miro el trabajo 2: papel rasgado verde y café.", "Nombro un elemento: los bordes rasgados.", "Escribo: me gusta porque los bordes rasgados se ven suaves."], "Me gusta porque los bordes rasgados se ven suaves"),
    ],
    [
        m("Decir «me gusta porque es bonito».", "No se nombra ningún elemento.", "Nombra un color, una línea, una forma o un material."),
        m("Pensar que mi preferencia debe ser igual a la de mi amigo.", "Se cree que hay una preferencia correcta.", "Cada persona prefiere cosas distintas, lo importante es explicar por qué."),
    ],
    [
        ex("En el trabajo 3, ¿qué tipo de líneas hay?", "Líneas quebradas", "La descripción dice líneas quebradas rojas."),
        ex("En el trabajo 2, ¿de qué materiales es el collage?", "Papel rasgado verde y café", "La descripción nombra papel rasgado verde y café."),
        ex("En el trabajo 1, ¿de qué color es la luna?", "Amarilla", "La descripción dice luna amarilla grande."),
    ],
    [
        ex("¿Qué es una preferencia? A: lo que me gusta más. B: una regla. C: un color.", "A", "La preferencia es lo que cada persona elige."),
        ex("«Me gusta porque el amarillo contrasta con el azul». ¿Qué elemento visual nombra?", "El color", "Habla de amarillo y azul."),
        ex("«Me gusta el trabajo 3 porque las líneas se ven con energía». ¿Qué elemento nombra: línea o material?", "Línea", "Habla de las líneas quebradas."),
    ],
    [
        ex("Ordena una buena explicación: A decir el efecto que me produce, B decir cuál trabajo prefiero, C nombrar un elemento visual.", "B, C, A", "Primero cuál, luego qué elemento y al final el efecto."),
        arith("Un niño nombra 2 colores y 1 línea del trabajo que prefiere. ¿Cuántos elementos nombra en total?", "2 + 1", "Se suman los dos colores y la línea."),
        ex("Prefieres el trabajo 2 por su papel rasgado verde y café. ¿Qué elemento explica tu preferencia: material o línea?", "Material", "El papel es el material del collage."),
    ],
    [
        ex("Ana dice: «Me gusta el trabajo 1 porque sí». ¿Qué le falta a su frase?", "Un elemento visual", "Falta decir qué color, línea, forma o material le gusta."),
        ex("Pedro dice: «Mi preferencia es equivocada porque nadie más prefiere ese trabajo». ¿Tiene razón?", "No", "Las preferencias no son correctas ni incorrectas."),
    ],
    [
        ex("Dos niñas prefieren el trabajo 3. Una dice «por las líneas quebradas» y la otra «por el color rojo». ¿Prefieren el mismo trabajo por el mismo elemento?", "No", "Prefieren el mismo trabajo pero nombran elementos distintos."),
        ex("Un niño dice: «Me gusta el trabajo 2 por los bordes rasgados y por el color café». ¿Cuántos elementos nombra?", "2", "Nombra el borde rasgado y el color café."),
    ],
    ex("En tu escuela cuelgan los tres trabajos y piden votar con un argumento. Escribes: «Voto por el trabajo 1 porque la luna amarilla se ve mucho». ¿Qué elemento visual usaste: el color o el material?", "El color", "Hablas del amarillo de la luna."),
    [
        ex("¿Qué se debe decir además de «me gusta»?", "Por qué", "Una razón con elementos visuales."),
        ex("Verdadero o falso: cada persona puede preferir un trabajo distinto.", "Verdadero", "Las preferencias son personales."),
        ex("El color rojo, ¿es un elemento visual?", "Sí", "El color es uno de los elementos del lenguaje visual."),
    ],
    task(
        "Elige UNO de los tres trabajos descritos (1: puntos azules y luna amarilla; 2: collage de papel rasgado verde y café con una casa; 3: líneas quebradas rojas). Escribe una explicación de tu preferencia con tres partes: cuál prefieres, qué elemento visual (color, línea, forma o material) y qué efecto te produce. Después escribe cuál te gusta menos y por qué, con respeto.",
        "Prefiero el trabajo 3 porque las líneas quebradas rojas se ven con mucha energía. Me gusta menos el trabajo 2 porque los colores verde y café me parecen apagados, pero entiendo que a otros les guste.",
        ["dice cuál prefiere", "nombra un elemento visual", "dice el efecto", "habla con respeto del trabajo que menos le gusta"],
        ["explicación escrita", "frase sobre el trabajo que menos le gusta"],
        ["decir solo «es bonito»", "burlarse de un trabajo"],
        "Reconoce el elemento mejor nombrado y pide que agregue qué efecto le produce.",
    ),
    "Mira tu ropa o un objeto de tu casa y di qué es lo que más te gusta, usando un color, una línea o una forma.",
    "Explica por qué NO te gusta un trabajo, pero sin criticar a la persona que lo hizo. Usa elementos visuales.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA5, 2,
    "Un trabajo de arte propio (un dibujo, una pintura o una escultura que hayas hecho), lápiz y una hoja para anotar. Si no tienes uno a mano, usa el ejemplo escrito en este cuaderno.",
    "Aprenderé a hablar de mi propio proceso: qué decisión me salió bien y cuál quiero revisar. Sirve para aprender de mi trabajo y mejorar sin sentirme mal.",
    ["Sé explicar una preferencia con un elemento visual.", "Sé que revisar un trabajo ayuda a mejorarlo."],
    [
        "El proceso es todo lo que haces mientras creas: miras, pruebas, eliges, cambias y terminas. Hablar de tu proceso significa contar qué decidiste y por qué. No es decir si salió bien o mal, sino explicar las decisiones que tomaste.",
        "Cuando hables de tu trabajo, nombra una decisión lograda: algo que te salió como querías. Por ejemplo: «Usé el naranja detrás de la luna para que se destacara». Nombra también una decisión para revisar: algo que cambiarías. Por ejemplo: «Pinté muy fuerte el cielo y las estrellas casi no se ven».",
        "Usa estas frases: «Lo que me salió bien fue… porque…» y «Lo que revisaría es… y lo cambiaría por…». Siempre menciona un elemento visual: color, línea, forma o material. Revisar no es un fracaso. Los artistas cambian sus decisiones para que la obra diga mejor lo que quieren.",
    ],
    [("proceso", "todo lo que hago desde la idea hasta terminar"), ("decisión", "elección que hago al crear"), ("lograda", "que salió como yo quería"), ("revisar", "mirar de nuevo para ver qué cambiar"), ("mejorar", "hacer que algo quede mejor")],
    [
        w("Hablar de mi proceso", "Pintaste una luna amarilla en un cielo azul oscuro y las estrellas se ven poco. ¿Qué dices?", ["Decisión lograda: la luna amarilla destaca sobre el azul oscuro.", "Decisión por revisar: las estrellas se ven poco.", "Cambio: usaré el pincel fino con amarillo claro para las estrellas."], "Lograda: contraste de la luna. Revisar: estrellas poco visibles"),
        w("De «salió mal» a una decisión", "Un niño dice: «Mi dibujo salió mal». ¿Cómo lo dice mejor?", ["Miro el dibujo y busco qué quedó bien.", "Identifico una decisión por revisar.", "Escribo: me salió bien el color; revisaría el tamaño de las casas."], "Me salió bien el color; revisaría el tamaño de las casas"),
    ],
    [
        m("Decir «salió mal» sin explicar qué decisión cambiarías.", "No se miran las decisiones, solo el resultado.", "Nombra qué decisión revisarías y por cuál la cambiarías."),
        m("Decir solo cosas buenas y ninguna por revisar.", "Se piensa que revisar es malo.", "Todos los trabajos tienen algo por revisar. Es parte de aprender."),
    ],
    [
        ex("En «Usé naranja detrás de la luna para que se destacara», ¿qué elemento visual se menciona?", "Color", "El naranja es un color."),
        ex("En «Pinté muy fuerte y las estrellas casi no se ven», ¿es una decisión lograda o por revisar?", "Por revisar", "Las estrellas casi no se ven, así que conviene cambiar algo."),
        ex("El proceso, ¿es todo lo que haces desde la idea hasta terminar o solo el resultado final?", "Todo lo que haces desde la idea hasta terminar", "Incluye mirar, probar, elegir y cambiar."),
    ],
    [
        ex("¿Qué es revisar un trabajo? A: mirarlo de nuevo para ver qué cambiar. B: botarlo. C: esconderlo.", "A", "Revisar es observar con intención de mejorar."),
        ex("«Lo que me salió bien fue el contraste entre la luna y el cielo». ¿Qué elemento visual menciona?", "El color", "El contraste es de colores."),
        ex("¿Revisar un trabajo significa que fracasaste?", "No", "Es parte normal del proceso."),
    ],
    [
        ex("Ordena una buena explicación: A decir qué cambiaría, B decir una decisión lograda, C mirar el trabajo.", "C, B, A", "Primero se mira, luego se dice lo logrado y al final lo que se cambiaría."),
        arith("Tu pintura tiene 4 decisiones logradas y 2 por revisar. ¿Cuántas decisiones nombraste?", "4 + 2", "Se suman las logradas y las por revisar."),
        ex("Un niño dice: «El pasto verde me salió bien porque combina con el cielo». ¿Es una decisión lograda o por revisar?", "Lograda", "Dice que algo salió bien y da una razón."),
    ],
    [
        ex("Lalo dice: «Mi trabajo es horrible» sin dar razones. ¿Qué podría decir mejor?", "Una decisión lograda y una por revisar", "Así describe su proceso sin juzgarse sin motivo."),
        ex("Eva dice: «Los artistas no revisan, hacen todo bien a la primera». ¿Tiene razón?", "No", "Los artistas prueban y cambian decisiones."),
    ],
    [
        ex("Dos niños dicen: «Revisaría el color» y «revisaría el color de las casas». ¿Cuál explicación es más clara?", "Revisaría el color de las casas", "Indica qué parte exacta cambiaría."),
        ex("Un niño nombró 3 decisiones logradas y 1 por revisar. ¿Cuántas decisiones por revisar nombró?", "1", "El enunciado lo dice."),
    ],
    ex("Tu profesor te pide contar tu proceso al terminar un dibujo de un bosque. Dices: «Las líneas verticales de los árboles me salieron bien, y revisaría el cielo porque quedó demasiado oscuro». ¿Cuántas decisiones nombras?", "2", "Una lograda y una por revisar."),
    [
        ex("¿Qué dos cosas dices al hablar de tu proceso?", "Una decisión lograda y una por revisar", "Así miras tu trabajo de forma equilibrada."),
        ex("Verdadero o falso: revisar es parte del trabajo del artista.", "Verdadero", "Revisar ayuda a mejorar."),
        ex("«Salió mal» ¿es una explicación clara?", "No", "No dice qué decisión cambiar."),
    ],
    task(
        "Usa un trabajo tuyo, o este ejemplo: un dibujo de una casa con un techo rojo pequeño y un sol amarillo grande. Escribe dos frases: «Lo que me salió bien fue… porque…» y «Lo que revisaría es… y lo cambiaría por…». Cada frase debe nombrar un elemento visual.",
        "Lo que me salió bien fue el sol amarillo grande porque se ve mucho sobre el cielo celeste. Lo que revisaría es el techo rojo, que quedó pequeño, y lo cambiaría por uno más grande.",
        ["nombra una decisión lograda", "nombra una decisión por revisar", "usa un elemento visual en cada frase"],
        ["dos frases escritas"],
        ["decir solo «salió mal»", "no dar razones"],
        "Reconoce la decisión mejor explicada y pide que diga cómo haría el cambio concreto.",
    ),
    "Mira un dibujo tuyo y di en voz alta una cosa que te salió bien y otra que cambiarías.",
    "Haz el cambio que dijiste y compara las dos versiones. Anota qué mejoró.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA5, 3,
    "Lápiz y una hoja para anotar. El trabajo de Mía es una descripción inventada: un dibujo de un gato con el cuerpo hecho de círculos de distintos tamaños, pintado con azul y naranja, y un fondo blanco.",
    "Aprenderé a dar una opinión sobre el trabajo de un compañero con una observación y una pregunta respetuosa, sin quedarme con su idea ni cambiar su trabajo. Sirve para ayudar a otros y cuidar sus ideas.",
    ["Sé explicar una preferencia con un elemento visual.", "Sé hablar con respeto."],
    [
        "Retroalimentar es decirle a otra persona qué viste en su trabajo para ayudarla a pensar. No es decir qué hacer ni cómo debería quedar. Una buena retroalimentación tiene dos partes: una observación y una pregunta respetuosa.",
        "La observación dice algo que ves y que te gusta: «Me gustó cómo usaste círculos de distintos tamaños en el cuerpo del gato». La pregunta invita a pensar: «¿Por qué elegiste azul y naranja?». No se dice «lo hiciste mal» ni «yo lo haría así». Tampoco se toca el trabajo de otro sin permiso.",
        "También respetamos las ideas de los demás. Apropiarse es quedarse con la idea de otro y decir que es tuya, o cambiar su trabajo sin permiso. Si te gusta una idea, puedes preguntar al autor si puedes inspirarte y decir de quién fue. Así cuidamos el trabajo de todos.",
    ],
    [("retroalimentar", "decir lo que veo en el trabajo de otro para ayudarle a pensar"), ("observación", "algo que veo y lo digo con claridad"), ("pregunta respetuosa", "pregunta que invita a pensar sin criticar"), ("apropiarse", "quedarse con la idea de otro como si fuera mía"), ("autor", "la persona que creó el trabajo")],
    [
        w("Observación y pregunta", "El trabajo de Mía es un gato hecho de círculos de distintos tamaños, azul y naranja. ¿Qué le dices?", ["Observación: me gustó cómo usaste círculos de distintos tamaños.", "Pregunta: ¿por qué elegiste el azul y el naranja?"], "Observación sobre los círculos y pregunta sobre los colores"),
        w("Respetar una idea", "Te gustan los círculos de Mía y quieres usar la idea. ¿Qué haces?", ["No copio su trabajo.", "Le pregunto si puedo inspirarme en sus círculos.", "Cuando lo uso, digo que la idea fue de Mía."], "Preguntar y decir de quién fue la idea"),
    ],
    [
        m("Decir «yo lo habría hecho mejor».", "Se compara con lo que yo haría en vez de mirar su trabajo.", "Di qué viste y haz una pregunta para entender su decisión."),
        m("Tomar el lápiz y cambiar el dibujo de un compañero.", "Se corrige sin permiso.", "Nunca cambies el trabajo de otro: dile lo que observas."),
    ],
    [
        ex("«Me gustó cómo usaste círculos de distintos tamaños». ¿Es una observación o una pregunta?", "Una observación", "Dice algo que se ve."),
        ex("«¿Por qué elegiste el azul y el naranja?». ¿Es una observación o una pregunta?", "Una pregunta", "Invita a explicar una decisión."),
        ex("Si me gusta la idea de un compañero, ¿digo que fue mía o digo de quién fue?", "Digo de quién fue", "Así se respeta al autor."),
    ],
    [
        ex("¿Qué dos partes tiene una buena retroalimentación? A: una observación y una pregunta respetuosa. B: un consejo y una orden. C: una burla y una risa.", "A", "Esas dos partes respetan al autor."),
        ex("¿Cuál es respetuosa: «Tu gato está feo» o «Me gustaron los círculos de tu gato»?", "Me gustaron los círculos de tu gato", "Habla de lo que se ve sin criticar."),
        ex("¿Se puede cambiar el trabajo de un compañero sin pedir permiso?", "No", "El trabajo es de su autor."),
    ],
    [
        ex("Ordena una retroalimentación: A hacer una pregunta, B mirar el trabajo con atención, C decir una observación.", "B, C, A", "Primero se mira, luego se observa y al final se pregunta."),
        arith("Escribes 2 observaciones y 1 pregunta para Mía. ¿Cuántas frases escribiste?", "2 + 1", "Se suman las observaciones y la pregunta."),
        ex("Elige una pregunta respetuosa sobre los colores del gato de Mía: A «¿Por qué usaste esos colores horribles?», B «¿Qué te hizo elegir el azul y el naranja?».", "B", "No juzga y pide explicar la decisión."),
    ],
    [
        ex("Ema dice: «Tomé la idea de Mía y dije que era mía». ¿Qué hizo?", "Se apropió de la idea", "Se quedó con una idea ajena sin decirlo."),
        ex("Tomás borró un detalle del dibujo de Sol para «arreglarlo». ¿Fue respetuoso?", "No", "Cambió su trabajo sin permiso."),
    ],
    [
        ex("Mía responde: «Elegí azul y naranja porque contrastan». ¿Qué elemento visual nombra?", "Color", "Habla de dos colores."),
        ex("Un compañero te dice: «Me gustó cómo sombreaste el cielo. ¿Qué lápiz usaste?». ¿Cuántas partes tiene su retroalimentación?", "2", "Hay una observación y una pregunta."),
    ],
    ex("En la exposición del curso te piden dejar un comentario en un papelito para el trabajo de un compañero. ¿Escribes «No me gustó» o «Me gustó la forma de las casas. ¿Cómo las dibujaste?»?", "Me gustó la forma de las casas. ¿Cómo las dibujaste?", "Tiene observación y pregunta, y es respetuoso."),
    [
        ex("¿Qué es apropiarse de una idea?", "Quedarse con una idea ajena", "Se hace pasar la idea de otro por propia."),
        ex("Verdadero o falso: se puede preguntar al autor si podemos inspirarnos en su idea.", "Verdadero", "Es una forma respetuosa de aprender."),
        ex("¿Qué haces con el trabajo de otro: lo cambias o lo respetas?", "Lo respetas", "El trabajo es de su autor."),
    ],
    task(
        "Lee el trabajo de Mía: un gato con el cuerpo hecho de círculos de distintos tamaños, pintado con azul y naranja sobre fondo blanco. Escribe una retroalimentación con dos partes: una observación que nombre un elemento visual y una pregunta respetuosa. Después escribe cómo pedirías permiso para inspirarte en su idea.",
        "Observación: me gustó cómo usaste círculos de distintos tamaños para el cuerpo. Pregunta: ¿por qué elegiste azul y naranja? Para inspirarme: «Mía, ¿puedo usar tu idea de hacer el cuerpo con círculos? Diré que fue tuya».",
        ["escribe una observación con elemento visual", "escribe una pregunta respetuosa", "pide permiso para inspirarse", "reconoce al autor"],
        ["observación", "pregunta", "frase para pedir permiso"],
        ["criticar sin respeto", "cambiar el trabajo de otro", "quedarse con la idea"],
        "Reconoce la observación mejor lograda y pide que revise si la pregunta invita a explicar y no a defender.",
    ),
    "Dile a alguien de tu casa una cosa que te gustó de un dibujo suyo y haz una pregunta amable.",
    "Escribe retroalimentación para otro trabajo de este cuaderno, usando otra observación y otra pregunta.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA5, 4,
    "Lápiz y una hoja para anotar. Cinco trabajos descritos para esta clase. A: pintura azul y verde con líneas horizontales. B: collage rojo y naranja con triángulos. C: dibujo en blanco y negro con líneas quebradas. D: escultura de masa con formas redondas, café. E: pintura amarilla y violeta con círculos.",
    "Aprenderé a elegir y organizar trabajos para una exposición usando criterios del lenguaje visual. Sirve para explicar mis elecciones con razones y mostrar trabajos con sentido.",
    ["Sé explicar una preferencia con un elemento visual.", "Sé que los trabajos de otros se respetan."],
    [
        "Una exposición muestra trabajos de arte para que otras personas los vean. Quien elige y ordena los trabajos se llama curador o curadora. Para elegir, usa un criterio: una razón que dice por qué esos trabajos van juntos. El criterio puede ser un color, una línea, una forma o un material.",
        "Por ejemplo, el criterio «colores cálidos» incluye el trabajo B (rojo y naranja) y el trabajo E, que tiene amarillo. El criterio «líneas rectas» puede incluir el trabajo A (horizontales). El criterio «formas redondas» incluye el trabajo D y el trabajo E (círculos). Un trabajo entra en un criterio si tiene al menos uno de esos colores o esa forma. Un mismo trabajo puede entrar en varios criterios.",
        "Para presentar tu selección, escribe un cartel corto: el título de la exposición, el criterio y por qué cada trabajo lo cumple. Respeta a los autores: no cambies sus trabajos, no los escondas y escribe su nombre solo si ellos están de acuerdo. Una exposición se arma pensando en quienes la visitarán.",
    ],
    [("exposición", "muestra de trabajos de arte para que otros los vean"), ("curador", "persona que elige y ordena los trabajos de una exposición"), ("criterio", "razón que usamos para elegir o agrupar"), ("selección", "conjunto de trabajos que elijo"), ("cartel", "texto corto que explica una exposición")],
    [
        w("Elegir con un criterio", "Criterio: colores cálidos. Trabajos: A azul y verde, B rojo y naranja, C blanco y negro, D café, E amarillo y violeta. ¿Cuáles eliges?", ["Los colores cálidos son rojo, naranja y amarillo.", "B tiene rojo y naranja: entra.", "E tiene amarillo: entra, aunque también tenga violeta.", "A, C y D no los tienen."], "B y E"),
        w("Escribir un cartel", "Criterio: formas redondas. Eliges D y E. ¿Qué escribes en el cartel?", ["Título: «Mundo redondo».", "Criterio: formas redondas.", "D: la escultura tiene formas redondas. E: la pintura tiene círculos."], "Título, criterio y razón para D y E"),
    ],
    [
        m("Elegir los trabajos solo porque me gustan, sin criterio.", "No se explica por qué van juntos.", "Elige un criterio visual y explica por qué cada trabajo lo cumple."),
        m("Dejar fuera un trabajo porque no me gusta, sin que incumpla el criterio.", "Se mezcla gusto personal con criterio.", "Si el trabajo cumple el criterio, debe entrar."),
    ],
    [
        ex("¿Quién elige y ordena los trabajos de una exposición?", "El curador o la curadora", "Esa es su función."),
        ex("Con el criterio «colores cálidos», ¿entra el trabajo B (rojo y naranja)?", "Sí", "Rojo y naranja son cálidos."),
        ex("¿Cuál trabajo es una escultura: D o E?", "D", "D es una escultura de masa; E es una pintura."),
    ],
    [
        ex("¿Qué es un criterio? A: la razón para elegir o agrupar. B: el nombre del autor. C: un tipo de papel.", "A", "El criterio explica por qué van juntos."),
        ex("Criterio: formas redondas. ¿Entra el trabajo C (líneas quebradas en blanco y negro)?", "No", "C no se describe con formas redondas."),
        ex("¿Qué trabajos tienen círculos o formas redondas: D y E, o A y C?", "D y E", "D es de formas redondas y E tiene círculos."),
    ],
    [
        arith("Tu exposición tiene 3 trabajos con colores cálidos y 2 con colores fríos. ¿Cuántos trabajos hay?", "3 + 2", "Se suman los trabajos de ambos grupos."),
        ex("Criterio: líneas. Eliges A (horizontales) y C (quebradas). ¿Cuántos trabajos eliges?", "2", "Son A y C."),
        ex("Ordena para armar una exposición: A escribir el cartel, B elegir los trabajos que cumplen, C pensar un criterio.", "C, B, A", "Primero el criterio, luego la selección y al final el cartel."),
    ],
    [
        ex("Pía dejó fuera el trabajo B de la exposición de colores cálidos porque no le gusta. ¿Fue una buena decisión de curadora? Explica.", "No; B cumple el criterio", "El criterio debe decidir, no solo el gusto."),
        ex("Luz cambió el color de un trabajo de otro niño para que entrara en su exposición. ¿Fue correcto?", "No", "Los trabajos de otros no se cambian."),
    ],
    [
        ex("Con el criterio «colores fríos», ¿qué trabajos de la lista entran? Revisa: A azul y verde, B rojo y naranja, C blanco y negro, D café, E amarillo y violeta.", "A y E", "A tiene azul y verde, y E tiene violeta, que es frío."),
        ex("Con el criterio «formas con puntas», ¿entra el trabajo B (triángulos)?", "Sí", "Los triángulos tienen puntas."),
    ],
    ex("Tu escuela organiza una exposición «Colores del recreo» y te piden elegir tres trabajos. Eliges tres que tienen amarillo, naranja y rojo. ¿Cuál es tu criterio?", "Colores cálidos", "Amarillo, naranja y rojo son colores cálidos."),
    [
        ex("¿Qué es un criterio?", "La razón para elegir", "Explica por qué se agrupan."),
        ex("Verdadero o falso: un curador respeta los trabajos de los demás.", "Verdadero", "No los cambia ni los esconde."),
        ex("Un cartel de exposición, ¿lleva título y criterio?", "Sí", "El cartel explica la exposición."),
    ],
    task(
        "Elige UN criterio: colores cálidos, colores fríos o formas redondas. De los cinco trabajos descritos (A: azul y verde con líneas horizontales; B: rojo y naranja con triángulos; C: blanco y negro con líneas quebradas; D: escultura de masa redonda, café; E: amarillo y violeta con círculos), elige los que lo cumplen (un trabajo entra si tiene al menos uno de esos colores o esa forma). Escribe un cartel con un título, tu criterio y una razón para cada trabajo.",
        "Criterio: formas redondas. Título: «Mundo redondo». Trabajos: D porque la escultura tiene formas redondas; E porque tiene círculos.",
        ["elige un criterio visual", "elige solo trabajos que lo cumplen", "escribe título y razón para cada trabajo"],
        ["lista de trabajos elegidos", "cartel escrito"],
        ["elegir por gusto sin criterio", "incluir un trabajo que no cumple el criterio"],
        "Reconoce el criterio más claro y pide que revise si cada trabajo elegido realmente lo cumple.",
    ),
    "Agrupa en tu casa cinco objetos con un criterio (color, forma o material) y di cuál usaste.",
    "Arma una segunda exposición con otro criterio y compara qué trabajos cambiaron.",
)
