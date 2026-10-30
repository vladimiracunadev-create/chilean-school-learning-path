"""Cuaderno del estudiante de 1.º básico Artes Visuales, AR01 OA 04 (primeras impresiones) y AR01 OA 05 (preferencias y retroalimentación)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA4, OA5 = "AR01 OA 04", "AR01 OA 05"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 04
register(
    OA4, 1,
    materials="Una hoja y lápiz. Las obras están descritas por escrito; un adulto puede mostrarte fotos si quiere. Para mirar, usa un reloj o cuenta despacio hasta 60.",
    use="Aprenderé a mirar una obra con calma y a describir lo que veo antes de decir qué pienso. Sirve para hablar de las obras con claridad y respeto.",
    prior=["Sé nombrar colores y formas.", "Sé hablar en voz alta ante otras personas."],
    explain=[
        "Observar una obra de arte es mirar sin apuro. Un buen método es mirar en silencio durante un minuto, recorriendo la obra por zonas: arriba, al medio y abajo, a la izquierda y a la derecha. Luego dices lo que ves: colores, formas, líneas y objetos.",
        "Describir es decir lo que se ve, como «hay un sol naranja pequeño». Interpretar es decir lo que pienso o imagino, como «parece que es de madrugada». Primero se describe y después se interpreta, porque así las ideas se apoyan en lo que realmente hay en la obra.",
        "Por ejemplo, Impresión, sol naciente, de Claude Monet, de 1872, muestra un sol naranja pequeño, una neblina azul y gris, y botes oscuros sobre el agua, pintados con pinceladas cortas. Con esos datos puedes decir qué sientes o piensas sin inventar cosas.",
    ],
    vocab=[("observar", "mirar con atención y sin apuro"), ("describir", "decir lo que se ve en la obra"), ("interpretar", "decir lo que pienso o imagino al verla"), ("pincelada", "huella que deja el pincel"), ("zona", "parte de la obra, como arriba o abajo")],
    worked=[
        {"title": "Describir con zonas", "problem": "Describe Impresión, sol naciente por zonas: arriba, al medio y abajo.", "steps": ["Arriba: hay un cielo con colores azules y grises.", "Al medio: hay un sol naranja pequeño entre la neblina.", "Abajo: hay agua con botes oscuros y pinceladas cortas."], "answer": "Arriba cielo gris azulado, al medio sol naranja, abajo botes y agua"},
        {"title": "Describir o interpretar", "problem": "¿«Hay botes oscuros sobre el agua» es una descripción o una interpretación?", "steps": ["Pregunto: ¿se ve en la obra? Sí, los botes están pintados.", "Si se ve, es una descripción."], "answer": "Descripción"},
    ],
    mistakes=[
        {"wrong": "Decir lo que siento sin mirar la obra antes.", "why": "No se apoya en nada visible.", "fix": "Primero mira un minuto y nombra lo que ves."},
        {"wrong": "Mezclar descripción e interpretación en la misma frase sin separarlas.", "why": "No se distingue qué está en la obra y qué es mi idea.", "fix": "Di primero qué ves y después qué pienso."},
    ],
    tiers={
        "recovery": [
            ex("En Impresión, sol naciente, ¿de qué color es el sol: naranja o verde?", "Naranja", "Así está descrito en la obra."),
            ex("¿Cuánto tiempo conviene mirar en silencio una obra antes de hablar: un minuto o dos segundos?", "Un minuto", "Mirar con calma permite ver detalles."),
            ex("Si dices «hay un sol naranja», ¿estás describiendo o interpretando?", "Describiendo", "Es algo que se ve."),
        ],
        "understand": [
            ex("¿Qué significa interpretar una obra? A: decir lo que pienso o imagino al verla. B: contar los lados del cuadro.", "A", "La interpretación es personal."),
            ex("¿Qué va primero: describir o interpretar?", "Describir", "Se parte de lo que se ve."),
            ex("¿Por qué se recorre la obra por zonas? A: para no olvidar partes. B: para tardar más.", "A", "Así se mira toda la obra, no un solo lugar."),
        ],
        "apply": [
            ex("Clasifica: «parece una mañana fría». ¿Es descripción o interpretación?", "Interpretación", "No se ve directamente, se imagina."),
            ex("Clasifica: «los botes son oscuros». ¿Es descripción o interpretación?", "Descripción", "El color oscuro se ve en los botes."),
            arith("En la obra hay 3 botes oscuros y 2 siluetas de personas pequeñas. ¿Cuántas figuras oscuras describes?", "3 + 2", "Se suman botes y siluetas."),
        ],
        "reason": [
            ex("Un niño dice «la obra me da pena» sin decir qué ve. ¿Qué le falta para describir bien?", "Decir qué ve en la obra", "Falta apoyar la idea en algo visible."),
            ex("Compara: A «hay mucho gris y azul», B «el pintor estaba cansado». ¿Cuál es descripción?", "A", "B es una idea sobre el pintor, no se ve."),
        ],
        "challenge": [
            ex("Describe en una frase la obra Composición II con rojo, azul y amarillo de Piet Mondrian: tiene líneas negras rectas y rectángulos de colores rojo, azul, amarillo y blanco.", "Hay líneas negras rectas y rectángulos rojos, azules, amarillos y blancos", "Solo nombra lo que se ve."),
            arith("En una obra cuentas 4 rectángulos rojos, 2 azules y 1 amarillo. ¿Cuántos rectángulos de colores hay?", "4 + 2 + 1", "Se suman los tres colores."),
        ],
    },
    context=[ex("En la sala de arte ves una pintura: arriba hay un cielo naranja, abajo un mar azul y en el centro un barco pequeño. Escribe una frase que solo describa lo que ves.", "Arriba hay un cielo naranja, abajo un mar azul y en el centro un barco pequeño", "Nombra colores y lugares sin agregar ideas.")],
    selfcheck=[
        ex("¿Qué significa describir?", "Decir lo que se ve", "Se nombra solo lo visible."),
        ex("¿Qué haces primero ante una obra: mirar en silencio o hablar rápido?", "Mirar en silencio", "Primero se observa."),
        ex("¿«Parece que va a llover» es descripción o interpretación?", "Interpretación", "Es lo que se imagina."),
    ],
    open_task=task(
        "Elige UNA de las obras descritas: (A) Impresión, sol naciente, de Monet (1872): sol naranja pequeño, neblina azul y gris, botes oscuros; (B) Composición con rojo, azul y amarillo, de Mondrian: líneas negras rectas y rectángulos de colores. Mírala (o imagínala) un minuto en silencio. Escribe o di tres frases que solo describan y una que interprete.",
        "Elegí A. Descripción: hay un sol naranja pequeño. Hay botes oscuros. El cielo es gris y azul. Interpretación: parece que es de madrugada.",
        ["escribe tres descripciones", "escribe una interpretación", "no mezcla lo que ve con lo que imagina"],
        ["cuatro frases escritas o dichas"],
        ["decir solo opiniones", "mezclar descripción e interpretación"],
        "Reconoce las descripciones claras y pide marcar con una palabra cuál frase es interpretación.",
    ),
    reinforce="Mira una foto o una lámina durante un minuto y di tres cosas que ves.",
    extend="Mira la misma obra otro día y busca un detalle nuevo que no habías descrito.",
)

register(
    OA4, 2,
    materials="Una hoja y lápices de colores. Las obras de esta clase están descritas por escrito en el cuaderno.",
    use="Aprenderé a unir lo que siento y pienso con algo que veo en la obra. Sirve para que mis opiniones sobre el arte tengan razones y no solo gustos.",
    prior=["Sé describir lo que veo.", "Sé nombrar emociones."],
    explain=[
        "Una obra de arte puede hacerte sentir cosas. La noche estrellada, que Vincent van Gogh pintó en 1889, muestra un cielo azul oscuro lleno de remolinos amarillos, una luna, estrellas y un pueblo pequeño debajo. Unas personas sienten calma y otras sienten movimiento.",
        "Para explicar lo que sientes, usa una frase con dos partes: «Siento… porque veo…». La segunda parte debe nombrar algo de la obra: un color, una línea, una forma. Por ejemplo: «Siento movimiento porque veo remolinos curvos en el cielo».",
        "Cuando uno dice «me gusta» o «no me gusta» sin razón, es difícil entenderlo. Cuando agrega lo que ve, los demás pueden mirar lo mismo y entender mejor. Dos personas pueden sentir distinto y las dos pueden tener razón si sus ideas se apoyan en lo que se ve.",
    ],
    vocab=[("sentir", "lo que me hace sentir una imagen, como calma o alegría"), ("pensar", "lo que imagino o entiendo al mirar la obra"), ("razón", "algo que se ve y apoya lo que digo"), ("remolino", "línea que gira formando espirales"), ("impresión", "primera idea o sensación al mirar")],
    worked=[
        {"title": "Siento… porque veo…", "problem": "Sientes movimiento al mirar La noche estrellada. ¿Qué frase escribes?", "steps": ["Nombro lo que siento: movimiento.", "Busco lo que veo que lo causa: remolinos curvos amarillos.", "Uno las dos partes con porque."], "answer": "Siento movimiento porque veo remolinos curvos en el cielo"},
        {"title": "Completar con una razón visible", "problem": "Alguien dice «Me da calma el cuadro». ¿Qué falta para explicarlo?", "steps": ["Pregunto: ¿qué se ve que da calma?", "Puede ser el azul oscuro o el pueblo quieto abajo.", "Agrego: porque veo un pueblo pequeño y quieto."], "answer": "Falta decir qué se ve, por ejemplo el pueblo quieto"},
    ],
    mistakes=[
        {"wrong": "Decir «me gusta» y nada más.", "why": "No hay razón que otras personas puedan ver.", "fix": "Agrega «porque veo…» y nombra un color o una forma."},
        {"wrong": "Pensar que si siento algo distinto a mi compañero, estoy equivocado.", "why": "Cada persona siente distinto.", "fix": "Las dos opiniones sirven si se apoyan en lo que se ve."},
    ],
    tiers={
        "recovery": [
            ex("En La noche estrellada, ¿de qué color son los remolinos: amarillos o rojos?", "Amarillos", "Así se describe la obra."),
            ex("¿Qué palabra une lo que siento con lo que veo: porque o pero?", "Porque", "Porque introduce la razón."),
            ex("«Siento calma porque veo un pueblo pequeño y quieto». ¿Qué es lo que se ve?", "Un pueblo pequeño y quieto", "Es la parte después de porque."),
        ],
        "understand": [
            ex("¿Qué debe tener una buena razón? A: algo que se ve en la obra. B: el precio del cuadro.", "A", "La razón se apoya en lo visible."),
            ex("¿Dos personas pueden sentir cosas distintas ante la misma obra?", "Sí", "Cada persona siente a su manera."),
            ex("¿Qué es una impresión? A: la primera sensación al mirar una obra. B: una copia en papel.", "A", "Es el primer sentir ante la obra."),
        ],
        "apply": [
            ex("Completa: «Siento movimiento porque veo ___» (en La noche estrellada hay remolinos).", "remolinos en el cielo", "Los remolinos curvos sugieren giro."),
            ex("Henri Matisse hizo en 1953 El caracol con papeles recortados de colores. Completa: «Siento alegría porque veo ___».", "papeles de muchos colores", "Los colores variados dan sensación de fiesta."),
            arith("En una obra hay 5 estrellas y 1 luna. ¿Cuántos astros hay en el cielo?", "5 + 1", "Se suman estrellas y luna."),
        ],
        "reason": [
            ex("Lola dice «Me da miedo la obra porque sí». ¿Qué le falta?", "Una razón basada en lo que ve", "Debe nombrar un color, una forma o una línea."),
            ex("Compara: A «Siento calma porque hay muchos azules suaves», B «Siento calma porque me gusta». ¿Cuál tiene mejor razón?", "A", "Nombra algo visible en la obra."),
        ],
        "challenge": [
            ex("Escribe una frase completa de «Siento… porque veo…» para una obra donde hay un sol naranja y un cielo gris.", "Siento tranquilidad porque veo un sol naranja entre el cielo gris", "La razón nombra colores que se ven."),
            arith("Tu frase usa 2 colores y 1 forma como razones. ¿Cuántas razones visibles nombraste?", "2 + 1", "Se suman colores y forma."),
        ],
    },
    context=[ex("Tu curso mira El caracol de Matisse. Un compañero dice que siente alegría. Tú ves que hay muchos colores y formas recortadas girando. Escribe tu frase con «porque veo».", "Siento alegría porque veo muchos colores y formas recortadas que giran", "La razón nombra colores y formas visibles.")],
    selfcheck=[
        ex("¿Qué palabra introduce la razón?", "Porque", "Es la que conecta lo que siento con lo que veo."),
        ex("¿Una razón debe nombrar un color, una forma o una línea?", "Sí", "Debe apoyarse en lo que se ve."),
        ex("¿Está bien sentir algo distinto a otra persona?", "Sí", "Cada uno siente a su manera."),
    ],
    open_task=task(
        "Elige UNA obra descrita: (A) La noche estrellada, de Van Gogh (1889); (B) El caracol, de Matisse (1953); (C) Impresión, sol naciente, de Monet (1872). Di lo que sientes con una palabra y completa: «Siento… porque veo…». Dibuja un pequeño cuadro con el detalle que nombraste.",
        "Elegí B. Siento alegría porque veo muchos colores. Dibujé tres papeles de colores en espiral.",
        ["dice una emoción", "nombra algo que se ve", "dibuja ese detalle"],
        ["frase completa", "dibujo pequeño del detalle"],
        ["decir solo me gusta", "inventar cosas que no están en la obra"],
        "Valora la razón visible y pide precisar con la palabra de color o forma exacta.",
    ),
    reinforce="Mira un afiche en tu casa y di qué sientes y qué ves que te hace sentirlo.",
    extend="Haz una segunda frase con otra emoción distinta sobre la misma obra y compáralas.",
)

register(
    OA4, 3,
    materials="Una hoja y lápiz. La obra Abaporu está descrita en el cuaderno; no necesitas verla. Las opiniones de los niños son ficticias.",
    use="Aprenderé que una misma obra puede interpretarse de maneras distintas y que todas valen si se apoyan en lo que se ve. Sirve para escuchar a otros y aprender de ellos.",
    prior=["Sé describir lo que veo.", "Sé decir «siento… porque veo…»."],
    explain=[
        "Abaporu es una pintura de Tarsila do Amaral, una artista de Brasil, de 1928. Se ve una figura humana sentada con un pie enorme, una cabeza muy pequeña y una mano apoyada. A un lado hay un cactus. Detrás hay un sol y el cielo es azul y el suelo verde.",
        "Cuando muchas personas miran la misma obra, cada una puede decir algo distinto: unas ven cansancio, porque la figura está sentada y apoyada; otras ven fuerza, por el pie tan grande; otras ven calor, por el cactus y el sol. Eso se llama tener distintas interpretaciones.",
        "Todas las interpretaciones son valiosas si se apoyan en algo que se ve. Si alguien dice «es un robot» sin mostrar qué ve, falta una razón. Escuchar a los demás nos ayuda a mirar de nuevo y descubrir cosas que no habíamos visto.",
    ],
    vocab=[("interpretación", "lo que cada persona entiende o imagina de una obra"), ("distinto", "que no es igual"), ("apoyar", "dar una razón basada en lo que se ve"), ("respeto", "escuchar y valorar a los demás aunque piensen distinto"), ("figura", "persona o forma dibujada en una obra")],
    worked=[
        {"title": "Dos interpretaciones válidas", "problem": "Ana ve cansancio porque la figura está sentada con la cabeza apoyada. Beto ve fuerza porque el pie es enorme. ¿Quién tiene razón?", "steps": ["Reviso si cada uno nombra algo que se ve.", "Ana nombra la figura sentada y apoyada.", "Beto nombra el pie enorme.", "Las dos se apoyan en la obra."], "answer": "Las dos son válidas"},
        {"title": "Una idea sin apoyo", "problem": "Carla dice «es una máquina del tiempo» y no nombra nada que se vea. ¿Qué le pides?", "steps": ["Pregunto: ¿qué ves que te hace pensar eso?", "Si nombra un detalle visible, su idea tiene apoyo.", "Si no lo hace, falta una razón."], "answer": "Pedirle que diga qué ve que la hace pensar así"},
    ],
    mistakes=[
        {"wrong": "Decir que la interpretación de otro niño es tonta.", "why": "No se respeta una idea distinta.", "fix": "Pregunta qué ve y escucha su razón."},
        {"wrong": "Creer que hay una sola respuesta correcta para cada obra.", "why": "Las obras permiten varias interpretaciones.", "fix": "Reconoce que varias ideas pueden ser válidas si se apoyan en lo visible."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué cosa muy grande tiene la figura de Abaporu: un pie o una oreja?", "Un pie", "La obra muestra un pie enorme."),
            ex("En Abaporu, ¿hay un cactus o un barco?", "Un cactus", "Así está descrita la obra."),
            ex("¿De qué país es Tarsila do Amaral?", "Brasil", "La artista nació en Brasil."),
        ],
        "understand": [
            ex("¿Qué significa tener distintas interpretaciones? A: cada persona entiende algo distinto. B: todos dicen lo mismo.", "A", "Cada persona mira desde su experiencia."),
            ex("¿Cuándo vale una interpretación? A: cuando se apoya en algo que se ve. B: cuando es la de la profesora.", "A", "La razón visible la hace válida."),
            ex("Si un compañero piensa distinto a ti, ¿qué haces: escucharlo o burlarte?", "Escucharlo", "El respeto es parte de la apreciación."),
        ],
        "apply": [
            ex("Leo ve calor porque hay un sol y un cactus. ¿Su razón es visible?", "Sí", "El sol y el cactus están en la obra."),
            ex("Mía dice que la figura está contenta, pero no nombra nada. ¿Qué le preguntas?", "¿Qué ves que te hace pensar eso?", "Pide un apoyo visible."),
            arith("Si 3 niños ven cansancio, 2 ven fuerza y 1 ve calor, ¿cuántos niños opinaron?", "3 + 2 + 1", "Se suman las opiniones."),
        ],
        "reason": [
            ex("Dos niños ven la figura de manera distinta: uno la ve quieta y otro ve que se mueve. ¿Uno está obligatoriamente equivocado?", "No", "Pueden apoyarse en detalles diferentes."),
            ex("Una niña dice «ese pie es ridículo». ¿Es una interpretación respetuosa y apoyada?", "No", "Descalifica al artista y no explica lo que ve."),
        ],
        "challenge": [
            ex("Escribe una interpretación tuya para Abaporu con «porque veo».", "Veo fuerza porque el pie es enorme", "Las respuestas deben nombrar algo visible de la obra."),
            arith("Un grupo de 8 niños opina sobre la obra. Si 5 ven fuerza, ¿cuántos ven otra cosa?", "8 - 5", "Se resta de los 8 los que ven fuerza."),
        ],
    },
    context=[ex("Tu amiga mira la figura sentada y dice que está descansando después de caminar mucho. Tú ves el sol y piensas en calor. ¿Pueden tener razón las dos?", "Sí, si cada una se apoya en algo que se ve", "Tienen interpretaciones distintas pero ambas visibles.")],
    selfcheck=[
        ex("¿Qué es una interpretación?", "Lo que cada persona entiende de una obra", "Es personal y se apoya en lo visible."),
        ex("¿Se puede pensar distinto de otro y que ambos tengan razón?", "Sí", "Si ambos se apoyan en lo visible."),
        ex("¿Qué haces cuando otro opina distinto: lo escuchas o lo interrumpes?", "Lo escucho", "El respeto es clave."),
    ],
    open_task=task(
        "Con alguien de tu familia, miren la descripción de Abaporu. Cada uno dice una interpretación con «porque veo». Escribe o dibuja las dos y marca con un círculo lo que se ve en la obra que apoya cada una. Si estás solo, escribe dos interpretaciones tuyas distintas.",
        "Mamá dice cansancio porque la figura está sentada. Yo digo fuerza porque el pie es enorme. Las dos nombran algo visible.",
        ["escucha otra interpretación", "apoya cada una en algo visible", "las compara con respeto"],
        ["dos frases escritas", "círculos o marcas en lo visible"],
        ["decir que una está equivocada", "no apoyar con lo visible"],
        "Reconoce la escucha y pide precisar el detalle visible que apoya cada interpretación.",
    ),
    reinforce="Pregunta a una persona de tu casa qué ve en una foto familiar y compara con lo que tú ves.",
    extend="Busca una segunda obra y recoge dos interpretaciones distintas.",
)

register(
    OA4, 4,
    materials="Una hoja, lápices de colores y una cinta o cordel opcional para colgar tu mini galería. Las obras están descritas por escrito.",
    use="Aprenderé a comparar varias obras y a comunicar mi impresión de muchas maneras: hablando, dibujando, escribiendo o con el cuerpo. Sirve para compartir lo que pienso de distintos modos.",
    prior=["Sé describir y decir «siento… porque veo…».", "Conozco algunas obras de la unidad."],
    explain=[
        "Una galería es un lugar donde se muestran varias obras. Comparar obras es mirar en qué se parecen y en qué se diferencian. Mira esta galería: La noche estrellada (Van Gogh, 1889) tiene un cielo con remolinos; Composición II (Mondrian) tiene líneas rectas negras; El caracol (Matisse, 1953) tiene papeles recortados de colores; Abaporu (Tarsila do Amaral, 1928) tiene una figura con un pie enorme.",
        "Hay muchas maneras de comunicar una impresión. Puedes decirla en voz alta, escribirla, dibujarla, hacer un gesto o una pose que muestre lo que sientes, o elegir un color. Todas son válidas si dejan ver tu impresión y la razón visible.",
        "Para comparar, elige dos obras y completa: «Se parecen en… y se diferencian en…». Por ejemplo: La noche estrellada y El caracol se parecen en que tienen líneas o formas que giran, y se diferencian en el material: una es pintura y la otra es papel recortado.",
    ],
    vocab=[("galería", "lugar donde se muestran varias obras"), ("comparar", "mirar en qué se parecen y en qué se diferencian"), ("comunicar", "contar a otros lo que pienso o siento"), ("medio", "forma de comunicar: palabra, dibujo, gesto o escritura"), ("semejanza", "algo que se parece entre dos cosas")],
    worked=[
        {"title": "Comparar dos obras", "problem": "Compara Composición II de Mondrian con El caracol de Matisse.", "steps": ["Mondrian usa líneas rectas negras y rectángulos de colores.", "Matisse usa formas recortadas que giran en espiral.", "Se parecen en que usan color y formas simples; se diferencian en que una es recta y la otra gira."], "answer": "Se parecen en el color; una es recta y la otra gira"},
        {"title": "Comunicar con un gesto", "problem": "Quieres mostrar lo que sientes ante La noche estrellada sin hablar. ¿Cómo lo haces?", "steps": ["Pienso en lo que veo: remolinos.", "Hago un movimiento circular con los brazos.", "Explico con una frase: sentí movimiento por los remolinos."], "answer": "Un movimiento circular de brazos y una frase"},
    ],
    mistakes=[
        {"wrong": "Decir cuál obra es mejor sin explicar.", "why": "No se compara con razones.", "fix": "Di en qué se parecen y se diferencian."},
        {"wrong": "Pensar que solo se puede comunicar hablando.", "why": "Se olvidan otras formas válidas.", "fix": "También puedes dibujar, escribir o mostrar con el cuerpo."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué obra tiene un cielo con remolinos?", "La noche estrellada", "Los remolinos son su rasgo principal."),
            ex("¿Qué obra tiene líneas rectas negras?", "Composición II de Mondrian", "Esas líneas son su rasgo principal."),
            ex("¿Qué es una galería?", "Un lugar donde se muestran varias obras", "Reúne obras para mirarlas."),
        ],
        "understand": [
            ex("¿Qué significa comparar dos obras? A: buscar parecidos y diferencias. B: elegir la más famosa.", "A", "Comparar es mirar semejanzas y diferencias."),
            ex("¿Puedes comunicar tu impresión con un dibujo?", "Sí", "El dibujo es otro medio válido."),
            ex("¿Qué debe acompañar a una impresión? A: una razón visible. B: un precio.", "A", "La razón la hace comprensible."),
        ],
        "apply": [
            arith("En la galería hay 4 obras y cada una tiene 2 colores principales. ¿Cuántos colores principales hay en total?", "4 * 2", "Son cuatro obras con dos colores cada una."),
            ex("Ordena de más antigua a más reciente: Matisse 1953, Van Gogh 1889, Tarsila do Amaral 1928.", "Van Gogh, Tarsila do Amaral, Matisse", "Los años en orden son 1889, 1928 y 1953."),
            ex("Completa: «La noche estrellada y El caracol se parecen en que tienen ___».", "formas que giran", "Remolinos en una y espiral en la otra."),
        ],
        "reason": [
            ex("Un niño dice: «La obra de Mondrian es mejor porque sí». ¿Qué le falta?", "Una razón visible y una comparación", "Debe decir en qué se parecen y diferencian."),
            ex("Una niña dibuja un cuadro con azul y amarillo para mostrar lo que sintió. ¿Comunicó su impresión de manera válida?", "Sí, si explica qué colores eligió y por qué", "El dibujo es un medio válido con razón."),
        ],
        "challenge": [
            ex("Completa: «Abaporu y La noche estrellada se diferencian en que una muestra ___ y la otra ___».", "una figura con un pie enorme; un cielo con remolinos", "Cada obra tiene un rasgo distinto."),
            arith("Comparaste 3 pares de obras y para cada par escribiste 2 semejanzas. ¿Cuántas semejanzas escribiste?", "3 * 2", "Son tres pares con dos semejanzas cada uno."),
        ],
    },
    context=[ex("En tu escuela montarán una galería con cuatro cuadros. Un niño quiere explicar su impresión con una canción inventada y otro con un dibujo. ¿Son medios válidos?", "Sí, si dicen qué ven que los hace sentir así", "Cada medio sirve si se apoya en lo visible.")],
    selfcheck=[
        ex("¿Qué significa comunicar una impresión?", "Contar a otros lo que pienso o siento", "Es compartir lo que se vivió al mirar."),
        ex("Nombra dos medios para comunicar una impresión.", "Hablar y dibujar", "Hay medios orales, visuales, escritos y corporales."),
        ex("¿Qué completas al comparar: «Se parecen en… y se diferencian en…»?", "Parecidos y diferencias", "Esa frase organiza la comparación."),
    ],
    open_task=task(
        "Elige DOS obras de la galería descrita: La noche estrellada, Composición II, El caracol o Abaporu. Escribe «Se parecen en… y se diferencian en…». Después comunica tu impresión de una de ellas con un medio que elijas: dibujo, gesto, escritura o palabras. Explica con «porque veo…».",
        "Elegí El caracol y Composición II. Se parecen en que usan colores y formas simples. Se diferencian en que una gira y la otra es recta. Dibujé una espiral de colores porque veo papeles que giran.",
        ["compara dos obras", "comunica con un medio elegido", "da una razón visible"],
        ["frase de comparación", "dibujo, gesto o escritura", "frase con porque veo"],
        ["decir cuál es mejor sin razones", "no explicar el medio elegido"],
        "Valora la comparación y pide ampliar la razón visible para el medio elegido.",
    ),
    reinforce="Dibuja una mini galería con tres cuadros y cuéntame qué hay en cada uno.",
    extend="Elige una tercera obra y compárala con las dos anteriores.",
)

# ================================================================ OA 05
register(
    OA5, 1,
    materials="Una hoja y lápiz. Los trabajos están descritos por escrito; son ejemplos inventados de otros niños y niñas.",
    use="Aprenderé a decir qué trabajo de arte prefiero y a dar una razón basada en un elemento visual: línea, color, forma o textura. Sirve para explicar mis gustos con claridad y respeto.",
    prior=["Conozco las líneas, los colores y las texturas.", "Sé decir «siento… porque veo…»."],
    explain=[
        "Preferir es elegir algo porque nos gusta más. En arte puedes preferir un trabajo sobre otro, pero también puedes dar una razón. La razón debe nombrar un elemento visual: una línea, un color, una forma o una textura que se vean en el trabajo.",
        "Una frase útil es: «Prefiero… porque tiene… (elemento visual)». Por ejemplo: «Prefiero el dibujo del cerro porque tiene líneas gruesas y firmes». También puedes decir lo contrario con respeto: «Me gusta menos el otro porque tiene muchos colores mezclados que no se distinguen».",
        "Decir «es más lindo» no explica nada. Decir «tiene colores fríos» o «tiene líneas onduladas» sí explica. Preferir con razones no es decir que otro trabajo es malo, sino mostrar qué te llama la atención de lo que miras.",
    ],
    vocab=[("preferir", "elegir algo porque me gusta más"), ("razón", "algo que se ve y explica mi elección"), ("elemento visual", "línea, color, forma o textura"), ("trabajo", "obra hecha por una persona"), ("respeto", "decir mi opinión sin herir a nadie")],
    worked=[
        {"title": "Preferir con razón", "problem": "Trabajo A: un mar con líneas onduladas azules. Trabajo B: un mar con manchas rojas. Prefieres A. ¿Cómo lo explicas?", "steps": ["Nombro el trabajo: A.", "Nombro un elemento visual: líneas onduladas azules.", "Armo la frase."], "answer": "Prefiero A porque tiene líneas onduladas azules que parecen olas"},
        {"title": "Una razón que no sirve", "problem": "Un niño dice «prefiero B porque es más lindo». ¿Qué le pides?", "steps": ["«Más lindo» no dice qué se ve.", "Le pido nombrar un color, línea, forma o textura.", "Él completa: tiene manchas rojas que se ven fuertes."], "answer": "Pedirle que diga qué elemento visual le gusta"},
    ],
    mistakes=[
        {"wrong": "Decir «prefiero este porque está mejor hecho».", "why": "No nombra qué elemento visual explica la preferencia.", "fix": "Di qué línea, color, forma o textura te llama la atención."},
        {"wrong": "Decir «el otro es feo».", "why": "Es una crítica que puede herir y no explica.", "fix": "Di qué te gusta del que prefieres o qué ves distinto en el otro."},
    ],
    tiers={
        "recovery": [
            ex("Trabajo A tiene líneas onduladas azules y Trabajo B manchas rojas. ¿Cuál tiene líneas?", "A", "Las líneas onduladas están en A."),
            ex("¿Qué palabra introduce la razón: porque o pero?", "Porque", "Porque une la elección con la razón."),
            ex("¿Línea es un elemento visual o un objeto?", "Un elemento visual", "Junto con color, forma y textura."),
        ],
        "understand": [
            ex("¿Qué es preferir con razones? A: elegir y explicar con un elemento visual. B: elegir sin explicar.", "A", "Hay elección y razón visible."),
            ex("¿Cuál es una razón visual? A: «tiene colores cálidos». B: «es de mi amigo».", "A", "Los colores cálidos se ven en el trabajo."),
            ex("¿Está bien decir «es feo» de un trabajo?", "No", "Puede herir y no explica."),
        ],
        "apply": [
            ex("Completa: «Prefiero el dibujo del sol porque tiene ___». (Tiene rayos amarillos gruesos).", "rayos amarillos gruesos", "Nombra líneas y color que se ven."),
            ex("Dibujo X: 4 flores rojas y 1 verde. Dibujo Z: 4 flores rojas, 1 verde y 3 azules. Prefieres Z por los colores. ¿Cuántos colores distintos tiene Z?", "3", "Tiene rojo, verde y azul."),
            arith("Dibujo X tiene 6 estrellas y dibujo Y tiene 9. ¿Cuántas estrellas hay entre los dos?", "6 + 9", "Se suman las estrellas de ambos."),
        ],
        "reason": [
            ex("Nico dice «prefiero el de mi amiga porque es mi amiga». ¿Es una razón visual?", "No", "No nombra nada que se vea en el trabajo."),
            ex("Compara: A «me gusta porque tiene líneas gruesas», B «me gusta porque sí». ¿Cuál es mejor razón?", "A", "Nombra un elemento visual."),
        ],
        "challenge": [
            ex("Escribe una frase de preferencia para este dibujo: una casa con tejado rojo, puerta azul y ventanas amarillas.", "Prefiero este dibujo porque tiene colores cálidos y fríos que se distinguen", "La frase nombra colores visibles."),
            arith("Un trabajo tiene 3 colores cálidos y 2 colores fríos. ¿Cuántos colores tiene?", "3 + 2", "Se suman ambos grupos."),
        ],
    },
    context=[ex("En el pasillo de tu escuela cuelgan dos dibujos de un perro. Uno usa líneas gruesas negras y el otro usa manchas suaves de café. Tú prefieres las líneas gruesas. ¿Cuál razón visual das?", "Porque tiene líneas gruesas negras", "Esa característica se ve en el dibujo.")],
    selfcheck=[
        ex("¿Qué significa preferir?", "Elegir porque me gusta más", "Es una elección personal."),
        ex("¿La razón debe nombrar algo que se ve?", "Sí", "Una línea, un color, una forma o una textura."),
        ex("¿Está bien decir «el otro es feo»?", "No", "Hay que ser respetuoso."),
    ],
    open_task=task(
        "Mira estos dos trabajos descritos: (A) un cerro hecho con líneas gruesas y marrones, con pasto verde; (B) un cerro hecho con puntitos pequeños de colores fríos. Di cuál prefieres y completa: «Prefiero… porque tiene… (elemento visual)». Escribe también una cosa que te gusta del que no elegiste.",
        "Prefiero A porque tiene líneas gruesas marrones. Del B me gusta que los puntitos fríos dan sensación de lejanía.",
        ["elige un trabajo", "da una razón visual", "reconoce algo del otro con respeto"],
        ["frase de preferencia", "frase sobre el otro trabajo"],
        ["decir solo me gusta", "criticar sin respeto"],
        "Valora la razón visual y pide nombrar con más exactitud el elemento que lo hace destacar.",
    ),
    reinforce="Elige entre dos dibujos de tu cuaderno y di una razón visual para tu preferencia.",
    extend="Explica una razón visual por la que a otra persona le podría gustar el trabajo que no elegiste.",
)

register(
    OA5, 2,
    materials="Una hoja con tu trabajo de arte reciente (o una obra de ejemplo descrita en el cuaderno) y lápiz. No uses nombres de otras personas.",
    use="Aprenderé a contar cómo hice mi trabajo, qué decisión tomé y qué cambié. Sirve para que otras personas entiendan mi proceso y yo recuerde lo que aprendí.",
    prior=["Sé que un procedimiento tiene pasos.", "Sé explicar con porque."],
    explain=[
        "Hablar de mi proceso es contar cómo hice mi trabajo, paso a paso. Un modelo de frase es: «Primero hice…, después…, al final…». También puedes decir qué decidiste: «Elegí… porque…». Y qué cambiaste: «Cambié… porque…».",
        "Una explicación tiene tres partes. La primera cuenta lo que hiciste, como «hice un collage de un barco con papel azul». La segunda explica una decisión, como «elegí azul porque quería mostrar el mar». La tercera cuenta un cambio, como «cambié el sol porque tapaba el barco».",
        "No hace falta decir que tu trabajo quedó perfecto. Lo importante es que expliques lo que hiciste y que uses palabras del arte: línea, color, textura, forma, material. Así otras personas entienden tu mirada.",
    ],
    vocab=[("proceso", "los pasos que seguí para hacer mi trabajo"), ("decisión", "elección que hice al crear"), ("cambio", "algo que modifiqué para mejorar"), ("explicar", "contar con claridad lo que hice y por qué"), ("al final", "lo último que hice")],
    worked=[
        {"title": "Contar el proceso", "problem": "Hiciste un collage de un barco. Primero rasgaste papel azul, después cortaste un barco naranja y al final pegaste todo. ¿Cómo lo cuentas?", "steps": ["Uso «primero…, después…, al final…».", "Primero rasgué papel azul para el mar.", "Después corté un barco naranja.", "Al final pegué todo."], "answer": "Primero rasgué papel azul, después corté el barco naranja y al final pegué todo"},
        {"title": "Explicar un cambio", "problem": "El sol amarillo tapaba el barco, por eso lo hiciste más pequeño. ¿Qué frase dices?", "steps": ["Nombro el cambio: hice el sol más pequeño.", "Digo la razón: tapaba el barco.", "Uno con porque."], "answer": "Cambié el sol a más pequeño porque tapaba el barco"},
    ],
    mistakes=[
        {"wrong": "Decir «solo lo hice» sin contar los pasos.", "why": "No se entiende cómo se llegó al resultado.", "fix": "Usa primero, después y al final."},
        {"wrong": "Explicar lo que habría querido hacer en vez de lo que hiciste.", "why": "Se pierde la verdad del proceso.", "fix": "Cuenta lo que realmente hiciste."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué palabra usas para contar el primer paso: primero o después?", "Primero", "Es la palabra del inicio."),
            ex("En «Cambié el color porque tapaba la flor», ¿cuál es la razón?", "Porque tapaba la flor", "Después de porque va la razón."),
            ex("¿Qué usa un artista para contar su proceso: pasos ordenados o una lista desordenada?", "Pasos ordenados", "Primero, después y al final."),
        ],
        "understand": [
            ex("¿Qué tres partes tiene una buena explicación? A: lo que hice, una decisión y un cambio. B: nombre, edad y curso.", "A", "Esas partes explican el proceso."),
            ex("¿Cuál frase es un cambio? A: «Cambié el verde por azul». B: «Hice un collage».", "A", "Cambié nombra una modificación."),
            ex("¿Cuál frase es una decisión? A: «Elegí rojo porque quería mostrar calor». B: «Pegué el papel».", "A", "Elegí con porque marca una decisión."),
        ],
        "apply": [
            ex("Ordena para contar: A al final pegué, B después corté, C primero rasgué.", "C, B, A", "Primero, después y al final."),
            ex("Completa: «Elegí azul porque quería mostrar ___». (Es un trabajo sobre el mar).", "el mar", "Azul se relaciona con el agua."),
            arith("En tu trabajo hiciste 3 pruebas y cambiaste 1 cosa. ¿Cuántas pruebas conservaste sin cambiar?", "3 - 1", "Se resta la que cambiaste."),
        ],
        "reason": [
            ex("Sara dice «yo no cambié nada porque me quedó perfecto» sin haber hecho pruebas. ¿Qué le sugieres?", "Mirar su obra de nuevo y buscar qué podría mejorar", "Siempre se puede observar y ajustar."),
            ex("Compara: A «Hice un collage», B «Primero rasgué papel azul, después corté un barco y al final pegué». ¿Cuál cuenta mejor el proceso?", "B", "Tiene pasos ordenados."),
        ],
        "challenge": [
            ex("Escribe una frase de cambio para: hiciste un dibujo con lápiz muy suave y no se veía; lo repasaste con lápiz más fuerte.", "Cambié el lápiz suave por uno más fuerte porque no se veía", "La frase une cambio y razón."),
            arith("Tu explicación tiene 1 frase de lo que hiciste, 1 de decisión y 1 de cambio. ¿Cuántas frases tiene?", "1 + 1 + 1", "Se suman las tres partes."),
        ],
    },
    context=[ex("Tu mamá te pregunta cómo hiciste el dibujo de la plaza. Usaste lápiz para el contorno, pintaste con témpera y agregaste detalles con cera. Cuéntaselo con primero, después y al final.", "Primero hice el contorno con lápiz, después pinté con témpera y al final agregué detalles con cera", "Respeta el orden real de los pasos.")],
    selfcheck=[
        ex("¿Qué palabras ordenan un proceso?", "Primero, después y al final", "Marcan el orden de los pasos."),
        ex("¿Qué palabra introduce una razón?", "Porque", "Conecta lo que hice con la causa."),
        ex("¿Debes contar lo que hiciste o lo que no hiciste?", "Lo que hice", "La explicación debe ser verdadera."),
    ],
    open_task=task(
        "Usa un trabajo reciente tuyo o este ejemplo: un dibujo de una casa con techo rojo, hecho primero con lápiz, luego pintado con témpera, y al final con detalles de cera. Escribe o dile a alguien tres frases: lo que hiciste con «primero, después, al final», una decisión con «elegí… porque…» y un cambio con «cambié… porque…».",
        "Primero dibujé la casa con lápiz, después la pinté con témpera y al final agregué detalles de cera. Elegí rojo porque quería un techo que destaque. Cambié la ventana a amarillo porque se perdía.",
        ["cuenta el proceso en orden", "explica una decisión", "explica un cambio"],
        ["tres frases escritas o dichas"],
        ["no usar primero, después, al final", "no dar razones"],
        "Reconoce el orden y pide una razón más específica con un elemento visual.",
    ),
    reinforce="Cuenta a alguien en tres frases cómo hiciste tu último dibujo.",
    extend="Compara tu explicación con la de un compañero y busca qué palabras de arte usaron ambos.",
)

register(
    OA5, 3,
    materials="Una hoja y lápiz. Los trabajos de otros niños son ejemplos inventados, descritos en el cuaderno, sin nombres reales.",
    use="Aprenderé a decir algo respetuoso y útil sobre el trabajo de otra persona. Sirve para ayudar a mis compañeros a seguir creando y para aprender de lo que ellos hacen.",
    prior=["Sé decir qué prefiero con una razón.", "Sé escuchar con respeto."],
    explain=[
        "Mirar el trabajo de otra persona es una forma de aprender. Cuando das una observación, ayudas a que la otra persona vea su trabajo de otra manera. Una observación respetuosa tiene tres partes: lo que me gustó, lo que veo y una pregunta o idea.",
        "Por ejemplo: «Me gustó el color azul del mar (lo que me gustó). Veo que usaste líneas onduladas (lo que veo). ¿Qué pasaría si agregas un barco pequeño? (idea)». No se dice «está feo» ni «lo hiciste mal», porque eso no ayuda y puede herir.",
        "También escuchas con atención cuando alguien opina sobre tu trabajo. Puedes preguntar: «¿qué viste?» y decidir si cambias algo. Tú eres quien decide si usar la sugerencia o no. El objetivo es entender y aprender.",
    ],
    vocab=[("observación", "algo que digo sobre lo que veo en un trabajo"), ("respetuoso", "que cuida los sentimientos de la otra persona"), ("sugerencia", "idea para mejorar o probar algo"), ("escuchar", "prestar atención a lo que dice otra persona"), ("pregunta", "forma amable de ofrecer una idea")],
    worked=[
        {"title": "Una observación en tres partes", "problem": "Miras un dibujo de un gato con bigotes largos y ojos amarillos. ¿Qué dices?", "steps": ["Lo que me gustó: los ojos amarillos.", "Lo que veo: bigotes largos y delgados.", "Idea: ¿qué pasaría si le agregas rayas en el pelo?"], "answer": "Me gustaron los ojos amarillos. Veo bigotes largos. ¿Qué pasaría si agregas rayas?"},
        {"title": "Cambiar una frase hiriente", "problem": "Alguien dice «tu casa está fea». ¿Cómo lo dices de manera respetuosa?", "steps": ["Busco algo que me gusta: el color rojo.", "Digo lo que veo: el techo está muy grande.", "Propongo: ¿probamos un techo más pequeño?"], "answer": "Me gusta el rojo; veo un techo muy grande; ¿probamos uno más pequeño?"},
    ],
    mistakes=[
        {"wrong": "Decir «te quedó mal».", "why": "Hiere y no explica qué mejorar.", "fix": "Di qué te gustó y qué idea podría probar."},
        {"wrong": "Hablar sin mirar el trabajo con atención.", "why": "La observación no se apoya en lo que hay.", "fix": "Mira primero un momento y nombra algo que veas."},
    ],
    tiers={
        "recovery": [
            ex("«Me gustó el color azul» ¿es respetuoso o hiriente?", "Respetuoso", "Nombra lo que gusta sin herir."),
            ex("«Está feo» ¿es respetuoso o hiriente?", "Hiriente", "No explica y puede herir."),
            ex("¿Cuántas partes tiene una observación respetuosa?", "Tres", "Lo que me gustó, lo que veo y una idea."),
        ],
        "understand": [
            ex("¿Para qué sirve una sugerencia? A: para ofrecer una idea de mejora. B: para decir que algo está mal.", "A", "Ayuda a pensar otra posibilidad."),
            ex("Una observación respetuosa, ¿empieza con algo que gusta o con una crítica?", "Con algo que gusta", "Así se cuida a la persona."),
            ex("Si te hacen una sugerencia, ¿quién decide si la usas?", "Tú", "El autor del trabajo decide."),
        ],
        "apply": [
            ex("Ordena: A ¿Qué pasaría si agregas una luna?, B Me gustaron los colores, C Veo muchas estrellas pequeñas.", "B, C, A", "Primero lo que me gustó, luego lo que veo y al final la idea."),
            ex("Cambia a respetuoso: «Tu dibujo es horrible». Escribe una frase mejor.", "Me gustaron los colores y me pregunto qué pasaría si agregas más detalles", "Reemplaza la crítica por algo que gusta y una idea."),
            arith("En una exposición de aula hay 6 dibujos y haces una observación a cada uno. ¿Cuántas observaciones haces?", "6 * 1", "Una observación por cada dibujo."),
        ],
        "reason": [
            ex("Un compañero te dice: «no me gustó tu dibujo». ¿Qué le preguntas para entender?", "¿Qué viste?", "Pide una razón visual."),
            ex("¿Por qué conviene empezar con algo que me gustó del trabajo? A: porque cuida a la persona. B: porque es obligatorio.", "A", "Hace que la conversación sea respetuosa."),
        ],
        "challenge": [
            ex("Escribe una observación respetuosa para este dibujo: un tren amarillo con muchas ventanas pequeñas y humo gris.", "Me gustó el tren amarillo, veo muchas ventanas pequeñas, ¿qué pasaría si el humo fuera más grande?", "Tiene las tres partes."),
            arith("Una persona recibe 3 observaciones de cada uno de 4 compañeros. ¿Cuántas observaciones recibe?", "3 * 4", "Son cuatro compañeros con tres cada uno."),
        ],
    },
    context=[ex("En el taller, tu compañera te muestra un dibujo de una montaña con la cumbre blanca. Tú ves que las rocas están hechas con líneas quebradas. Escribe una observación en tres partes.", "Me gustó la cumbre blanca, veo líneas quebradas en las rocas, ¿qué pasaría si agregas un cielo?", "Combina agrado, observación y pregunta.")],
    selfcheck=[
        ex("¿Qué es una sugerencia?", "Una idea para probar algo distinto", "Es una forma amable de ayudar."),
        ex("¿Se puede decir «tu trabajo es feo»?", "No", "Hiere y no ayuda."),
        ex("¿Qué haces cuando otro habla de tu trabajo: lo escuchas o lo interrumpes?", "Lo escucho", "Escuchar es parte del respeto."),
    ],
    open_task=task(
        "Mira estos dos trabajos ficticios: (A) una flor con un círculo amarillo y cuatro pétalos rojos; (B) una nube de lana blanca pegada sobre un cielo azul. Para cada uno escribe una observación con tres partes: «Me gustó…, veo…, ¿qué pasaría si…?». Usa palabras de color, línea o textura.",
        "A: Me gustó el centro amarillo. Veo cuatro pétalos rojos. ¿Qué pasaría si agregas un tallo verde? B: Me gustó la textura de la lana. Veo que la nube es blanca. ¿Qué pasaría si pegas otra nube?",
        ["escribe las tres partes", "usa palabras de arte", "es respetuoso"],
        ["dos observaciones escritas"],
        ["usar palabras hirientes", "omitir la pregunta"],
        "Reconoce la amabilidad y pide una pregunta que invite a probar sin imponer.",
    ),
    reinforce="Dile a alguien en casa algo que te gustó de un dibujo suyo y una pregunta.",
    extend="Escribe una pregunta distinta para cada uno de los dos trabajos de la actividad.",
)

register(
    OA5, 4,
    materials="Una hoja, lápiz y los datos de un círculo de apreciación de un curso de ejemplo, escritos en el cuaderno.",
    use="Aprenderé a participar en un círculo donde cada persona cuenta qué trabajo prefiere y por qué, sin decir que alguien vale más o menos. Sirve para aprender de todos y respetar los gustos.",
    prior=["Sé dar una razón visual.", "Sé dar una observación respetuosa."],
    explain=[
        "Un círculo de apreciación es una conversación donde todos se sientan en círculo y cada persona habla por turnos. Cada una dice qué trabajo prefiere y por qué, usando un elemento visual. Mientras alguien habla, los demás escuchan en silencio.",
        "En el círculo se comparan preferencias, no personas. Se puede decir «a seis personas les gustó el azul» o «a cuatro personas les gustaron las líneas gruesas». No se dice «ella es mejor que él». Los trabajos no se ordenan como en una competencia, sino que se describe lo que cada uno muestra.",
        "Una forma de registrar es hacer una tabla de preferencias. Cada persona pone una marca bajo el trabajo que prefirió y escribe su razón. Al final se cuentan las marcas y se observa qué elementos visuales se mencionaron más.",
    ],
    vocab=[("círculo de apreciación", "conversación en círculo para compartir lo que preferimos y por qué"), ("turno", "momento en que habla cada persona"), ("preferencia", "lo que cada persona elige por gusto"), ("tabla", "cuadro donde se anotan datos"), ("sin jerarquizar", "sin decir que una persona o un trabajo vale más que otro")],
    worked=[
        {"title": "Contar preferencias", "problem": "En un círculo, 5 personas prefirieron el trabajo A, 3 el B y 2 el C. ¿Cuántas personas hay en el círculo?", "steps": ["Sumo las personas de cada preferencia.", "5 + 3 + 2 = 10."], "answer": "10 personas"},
        {"title": "Decir una preferencia sin jerarquizar", "problem": "Quieres decir que te gustó más el trabajo B, sin decir que los otros son peores. ¿Qué frase usas?", "steps": ["Digo mi preferencia: B.", "Doy la razón visual: tiene líneas onduladas.", "No comparo a las personas."], "answer": "Prefiero B porque tiene líneas onduladas"},
    ],
    mistakes=[
        {"wrong": "Decir «gané yo» o «el tuyo perdió».", "why": "El círculo no es una competencia.", "fix": "Cuenta preferencias y razones sin ordenar a las personas."},
        {"wrong": "Interrumpir cuando otra persona habla.", "why": "No se respeta el turno.", "fix": "Espera tu turno y escucha en silencio."},
    ],
    tiers={
        "recovery": [
            ex("En el círculo, ¿se habla por turnos o todos a la vez?", "Por turnos", "Así todos pueden hablar y escuchar."),
            ex("¿Se compara a las personas o a las preferencias?", "A las preferencias", "No se jerarquiza a nadie."),
            ex("¿Qué se hace mientras otra persona habla: escuchar o interrumpir?", "Escuchar", "El respeto lo requiere."),
        ],
        "understand": [
            ex("¿Para qué sirve una tabla de preferencias? A: para anotar y contar las elecciones. B: para castigar.", "A", "Organiza los datos."),
            ex("¿Qué significa «sin jerarquizar»? A: no decir que una persona o trabajo vale más. B: no hablar.", "A", "Jerarquizar es ordenar por valor."),
            ex("En un círculo, ¿se dice «el trabajo de ella es peor»?", "No", "Se comparan preferencias, no personas."),
        ],
        "apply": [
            arith("En la tabla, 4 marcas están en el trabajo A, 5 en el B y 3 en el C. ¿Cuántas marcas hay?", "4 + 5 + 3", "Se suman las marcas de los tres."),
            arith("En el círculo hay 12 personas y 7 prefirieron el trabajo A. ¿Cuántas prefirieron otro?", "12 - 7", "Se restan las que prefirieron A."),
            ex("En la tabla: A 6 marcas, B 2 marcas, C 4 marcas. ¿Qué trabajo tiene más marcas?", "A", "Seis es el número mayor."),
        ],
        "reason": [
            ex("Un niño dice: «Mi dibujo ganó porque tiene más marcas». ¿Qué le explicas?", "Que no es una competencia, solo se cuentan preferencias", "El círculo no ordena trabajos como ganadores."),
            ex("Una tabla muestra A 5, B 5, C 5. ¿Qué dice sobre las preferencias del grupo?", "Que están repartidas por igual", "Los tres trabajos tienen el mismo número."),
        ],
        "challenge": [
            arith("Hay 3 grupos de 4 personas y todos prefieren el azul. ¿Cuántas personas prefieren el azul?", "3 * 4", "Son tres grupos de cuatro."),
            ex("Escribe una frase sobre la tabla: A 7, B 3. Sin jerarquizar.", "Siete personas prefirieron A y tres prefirieron B", "Cuenta sin decir quién es mejor."),
        ],
    },
    context=[ex("Tu curso hace un círculo con tres dibujos de un gato. 5 niños eligen el de líneas gruesas, 3 el de colores y 2 el de texturas. ¿Cuántos niños participaron?", "10", "Se suman 5, 3 y 2.")],
    selfcheck=[
        ex("¿Qué es un círculo de apreciación?", "Una conversación en círculo para compartir lo que preferimos y por qué", "Se habla por turnos."),
        ex("¿Se puede decir que una persona es mejor que otra por su dibujo?", "No", "Se comparan preferencias y no valores."),
        ex("¿Qué se hace con los datos de la tabla: contar las marcas o castigar?", "Contar las marcas", "Se observa qué prefiere el grupo."),
    ],
    open_task=task(
        "Con tu familia o con tu curso, haz un círculo de apreciación pequeño con tres trabajos: (A) un dibujo con líneas gruesas, (B) un dibujo con colores cálidos, (C) un dibujo con texturas. Cada persona dice cuál prefiere y por qué, usando un elemento visual. Anota las preferencias en una tabla y cuéntalas sin decir quién es mejor. Si estás solo, escribe cuál prefieres tú y dos razones.",
        "Fuimos 5. A tuvo 2 marcas, B 2 y C 1. Una razón fue: líneas gruesas. Otra fue: colores cálidos.",
        ["participa por turnos", "da una razón visual", "cuenta sin jerarquizar"],
        ["tabla de preferencias", "frases de razones"],
        ["usar palabras de competencia", "no anotar razones"],
        "Reconoce el respeto de los turnos y pide anotar siempre el elemento visual de cada razón.",
    ),
    reinforce="Haz una tabla con dos dibujos de tu casa y pregunta a tres personas cuál prefieren y por qué.",
    extend="Compara dos círculos de apreciación distintos y busca qué razones visuales se repiten.",
)
