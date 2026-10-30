"""Cuaderno del estudiante de 1.º básico Artes Visuales, AR01 OA 01 (creación desde la observación del entorno)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "AR01 OA 01"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- Clase 1
register(
    OA1, 1,
    materials="Una hoja de papel, un lápiz de mina y un objeto pequeño de la naturaleza (una hoja, una piedra, una concha o una flor). Si no tienes uno, usa las descripciones escritas en este cuaderno.",
    use="Aprenderé a mirar con calma un objeto de la naturaleza y a anotar sus formas y detalles antes de dibujar. Sirve para que mi dibujo muestre lo que de verdad veo y no solo lo que imagino.",
    prior=["Sé usar un lápiz para hacer líneas.", "Conozco los nombres de algunas formas: círculo, óvalo, triángulo."],
    explain=[
        "Observar es mirar con atención, sin apuro. Antes de dibujar, el artista se detiene y se pregunta: ¿qué forma tiene en total? ¿Qué detalles tiene? ¿De qué color es? ¿Cómo se siente al tocarlo? Las respuestas son pistas para dibujar.",
        "Una buena observación va de lo grande a lo pequeño. Primero miras la forma general, por ejemplo un óvalo largo. Después buscas los detalles, como una línea en el centro, manchas o bordes con dientitos. Por último miras los colores.",
        "Cuando dibujas lo que sabes y no lo que ves, todas las hojas salen iguales. Cuando dibujas lo que ves, tu hoja es única, porque nadie más tiene exactamente esa hoja. Por eso se mira varias veces: cada vez aparece un detalle nuevo.",
    ],
    vocab=[("observar", "mirar con atención para descubrir detalles"), ("forma", "cómo se ve el contorno de algo, por ejemplo redonda u ovalada"), ("detalle", "una parte pequeña pero importante, como una grieta o una mancha"), ("contorno", "la línea que rodea una figura"), ("entorno natural", "lo que nos rodea y no fabricó una persona: plantas, piedras, animales")],
    worked=[
        {"title": "Observar una piedra", "problem": "Tienes una piedra de río: es lisa, gris, tiene forma de huevo aplastado y una raya blanca que la cruza. ¿Qué anotas antes de dibujar?", "steps": ["Miro la forma general: huevo aplastado, es decir, ovalada.", "Busco el detalle: una raya blanca que la cruza.", "Miro el color: gris, con la raya clara.", "Anoto cómo se siente: lisa."], "answer": "Forma ovalada, raya blanca, color gris, superficie lisa"},
        {"title": "De lo grande a lo pequeño", "problem": "Un caracol de jardín tiene la concha en espiral, el cuerpo largo y dos antenas. ¿En qué orden miras sus partes para dibujarlo?", "steps": ["Primero la parte más grande: la concha en espiral.", "Después el cuerpo largo que sale de la concha.", "Al final las antenas, que son lo más pequeño."], "answer": "Concha, cuerpo y antenas"},
    ],
    mistakes=[
        {"wrong": "Dibujar una hoja como un corazón verde con un palito, porque así «se dibujan» las hojas.", "why": "Se dibuja lo que se sabe y no lo que se ve.", "fix": "Mira la hoja que tienes: anota su forma, su borde y sus líneas antes de dibujar."},
        {"wrong": "Mirar el objeto una sola vez y dibujar de memoria.", "why": "Se olvidan los detalles, que aparecen al mirar de nuevo.", "fix": "Mira el objeto, dibuja un trozo, vuelve a mirar y sigue."},
    ],
    tiers={
        "recovery": [
            ex("Una concha es redonda, tiene rayitas que salen desde un punto y es de color crema. ¿Qué forma tiene?", "Redonda", "La descripción dice que es redonda."),
            ex("En la frase «una concha de color crema», ¿la palabra crema habla de la forma o del color?", "Del color", "Crema nombra un tono, no una figura."),
            ex("Antes de dibujar una hoja, ¿qué haces primero: mirarla con atención o dibujar enseguida?", "Mirarla con atención", "Observar viene antes de dibujar."),
        ],
        "understand": [
            ex("¿Para qué conviene mirar el objeto varias veces mientras dibujas? A: para terminar antes. B: para descubrir detalles nuevos. C: para dibujar sin mirar.", "B", "Cada nueva mirada muestra detalles que antes no veías."),
            ex("Lee: «Un caracol de jardín tiene concha en espiral, cuerpo largo y dos antenas». ¿Cuántas partes distintas se nombran?", "3", "Se nombran la concha, el cuerpo y las antenas."),
            ex("¿Qué es el contorno de una piedra? A: su color. B: la línea que la rodea. C: su peso.", "B", "El contorno es el borde que dibuja su forma."),
        ],
        "apply": [
            arith("Una flor tiene 5 pétalos redondos y un centro redondo. Si dibujas cada uno con un círculo, ¿cuántos círculos dibujas en total?", "5 + 1", "Se suman los pétalos y el centro."),
            arith("Una hoja tiene una línea gruesa en el centro y 4 líneas finas a cada lado de ella. ¿Cuántas líneas finas hay en total?", "4 + 4", "Hay líneas finas en los dos lados."),
            ex("Ordena los pasos con letras: A dibujar el contorno, B mirar el objeto, C pintar el color, D agregar los detalles.", "B, A, D, C", "Se mira, se dibuja la forma, se agregan detalles y al final se pinta."),
        ],
        "reason": [
            ex("El gato que Ana mira tiene orejas puntiagudas y cola larga. Ana dibuja orejas redondas y cola corta. ¿Dibujó lo que veía o lo que se imaginaba?", "Lo que se imaginaba", "Su dibujo no coincide con el gato que tenía delante."),
            ex("Tomás dice: «Si miro una vez ya lo sé todo, no necesito mirar más». ¿Tiene razón?", "No", "Al mirar de nuevo se descubren detalles que se habían escapado."),
        ],
        "challenge": [
            arith("Una piña de pino tiene 3 filas de escamas con 4 escamas en cada fila. Si dibujas todas, ¿cuántas escamas dibujas?", "4 + 4 + 4", "Son tres filas iguales de cuatro: se suma tres veces 4."),
            ex("Cuenta los detalles de esta frase: «El trozo de corteza es áspero, café oscuro, tiene grietas largas y un hongo pequeño». ¿Cuántos detalles se nombran?", "4", "Se nombran áspero, café oscuro, grietas largas y un hongo pequeño."),
        ],
    },
    context=[ex("Te piden dibujar el limón del frutero. Es amarillo, ovalado con una punta en cada extremo y su cáscara tiene puntitos. Nombra las tres cosas que anotas antes de dibujar.", "Forma ovalada con puntas, color amarillo y cáscara con puntitos", "Son la forma, el color y el detalle de la superficie.")],
    selfcheck=[
        ex("¿Qué se mira primero: la forma general o los detalles pequeños?", "La forma general", "Se va de lo grande a lo pequeño."),
        ex("¿Qué dibujas cuando observas bien: lo que sabes o lo que ves?", "Lo que ves", "Observar es dibujar lo que realmente se ve."),
        ex("Una piedra tiene una raya blanca. ¿La raya es un detalle o la forma general?", "Un detalle", "Es una parte pequeña dentro de la piedra."),
    ],
    open_task=task(
        "Elige UNO de estos objetos: una hoja, una piedra o una concha (si no tienes, usa esta descripción: una hoja ovalada, con punta, borde con dientitos, una línea gruesa al centro y líneas finas que salen de ella, verde oscura). Anota en tres renglones su forma, sus detalles y su color. Después haz dos dibujos pequeños y quédate con el que más se parece a lo que ves.",
        "Elegí una hoja. Forma: óvalo con punta. Detalles: borde con dientitos y una línea en el centro. Color: verde oscuro. Mi dibujo 2 se parece más porque marqué los dientitos.",
        ["anota forma, detalles y color", "hace dos dibujos distintos", "elige uno y dice por qué"],
        ["tres renglones de anotación", "dos dibujos pequeños", "una frase de elección"],
        ["dibujar un símbolo conocido en vez del objeto", "no anotar ningún detalle"],
        "Reconoce lo que observó y pide mirar otra vez para encontrar un detalle más que aún no dibujó.",
    ),
    reinforce="Mira durante un minuto una hoja o una piedra y di en voz alta tres cosas que ves en ella.",
    extend="Dibuja el mismo objeto desde otro lado y anota qué detalle cambió al mirarlo desde ahí.",
)

# ---------------------------------------------------------------- Clase 2
register(
    OA1, 2,
    materials="Una hoja, lápiz de mina, un rectángulo de cartón o papel con un hueco en el centro (visor) y colores. Los paisajes están descritos en el cuaderno.",
    use="Aprenderé a elegir qué parte de un paisaje, un animal o una planta quiero mostrar y dónde ponerla en la hoja. Sirve para que mi dibujo tenga un protagonista claro.",
    prior=["Sé observar las formas y detalles de un objeto.", "Sé dibujar formas simples."],
    explain=[
        "Un paisaje tiene muchas cosas, pero un dibujo no puede mostrarlas todas. El artista elige un foco: lo más importante, lo que quiere que miremos primero. Puede ser un árbol, una oveja o un río.",
        "Para elegir, usa un visor: un marco con un hueco que mueves frente al paisaje. Lo que queda dentro del hueco es lo que dibujarás. Eso se llama encuadrar. Si alejas el visor de tu ojo, estirando el brazo, ves menos cosas, pero más grandes.",
        "Después decides dónde poner cada cosa. Lo que está cerca, en el primer plano, se dibuja abajo y más grande. Lo que está lejos, en el fondo, se dibuja arriba y más pequeño. Colocar así las cosas se llama componer.",
    ],
    vocab=[("foco", "lo más importante del dibujo"), ("encuadrar", "elegir con un marco qué parte se va a dibujar"), ("primer plano", "lo que está más cerca y se dibuja abajo y grande"), ("fondo", "lo que está lejos y se dibuja arriba y pequeño"), ("componer", "decidir dónde se pone cada cosa en la hoja")],
    worked=[
        {"title": "Elegir el foco", "problem": "Paisaje: un cerro azul al fondo, un árbol grande a la izquierda, un río en el centro y tres ovejas en el pasto delante. Quieres mostrar la vida del campo. ¿Cuál es tu foco?", "steps": ["Pienso en lo que quiero mostrar: la vida del campo.", "Las ovejas son seres vivos y están cerca.", "Las pongo grandes, abajo y en el centro."], "answer": "Las tres ovejas"},
        {"title": "Primer plano y fondo", "problem": "En el mismo paisaje, ¿qué va en el primer plano y qué va en el fondo?", "steps": ["Lo más cercano son las ovejas en el pasto: primer plano.", "El río está en el medio.", "El cerro es lo más lejano: fondo, arriba y pequeño."], "answer": "Primer plano: ovejas. Fondo: cerro"},
    ],
    mistakes=[
        {"wrong": "Dibujar todo del mismo tamaño y repartido por la hoja.", "why": "No se eligió un foco y nada destaca.", "fix": "Elige lo más importante y dibújalo más grande y cerca del centro."},
        {"wrong": "Poner el cerro lejano abajo y grande.", "why": "Se confunde la posición de lo cercano y lo lejano.", "fix": "Lo lejano va arriba y pequeño; lo cercano abajo y grande."},
    ],
    tiers={
        "recovery": [
            ex("En un paisaje hay un perro grande y cerca, y una casa pequeña y lejana. ¿Cuál está en el primer plano?", "El perro", "Lo grande y cercano va en el primer plano."),
            ex("¿Cómo se llama el marco con un hueco que sirve para elegir qué dibujar?", "Visor", "El visor encuadra una parte del paisaje."),
            ex("Una montaña muy lejana, ¿va en el fondo o en el primer plano?", "En el fondo", "Lo lejano se ubica en el fondo."),
        ],
        "understand": [
            ex("¿Qué es el foco de un dibujo? A: el color más oscuro. B: lo más importante que se quiere mostrar. C: el borde de la hoja.", "B", "El foco es lo que el artista quiere que miremos primero."),
            ex("Si alejas el visor de tu ojo, estirando el brazo, ¿ves más cosas o menos cosas por el hueco?", "Menos cosas", "El hueco abarca una parte más pequeña del paisaje."),
            ex("¿Para qué sirve componer un dibujo? A: para decidir dónde poner cada cosa. B: para borrar. C: para pintar rápido.", "A", "Componer es ordenar las cosas en la hoja."),
        ],
        "apply": [
            ex("Paisaje: un huemul pequeño en un valle con montañas y un cielo lleno de nubes. Quieres que el foco sea el huemul. ¿Lo dibujas grande o pequeño?", "Grande", "El foco debe destacar por su tamaño."),
            ex("Ordena de más lejano a más cercano: A una flor en el pasto, B un cerro nevado, C un árbol en la mitad del campo.", "B, C, A", "El cerro está más lejos; el árbol, a media distancia; la flor, al lado tuyo."),
            arith("Un árbol tiene 6 manzanas en las ramas de arriba y 3 caídas en el pasto. Si quieres dibujar todas, ¿cuántas manzanas dibujas?", "6 + 3", "Se suman las de las ramas y las del suelo."),
        ],
        "reason": [
            ex("Luz dibujó un pájaro del mismo tamaño que el árbol, y los dos en el centro. Dice que su foco es el pájaro. ¿Se nota el foco?", "No", "Ni el tamaño ni el lugar destacan al pájaro."),
            ex("Pía quiere mostrar un conejo en un jardín. ¿Qué cambio ayuda más: A pintar el conejo más grande y en el centro, o B dibujar más flores alrededor?", "A", "Agrandar el conejo y ponerlo al centro lo vuelve protagonista."),
        ],
        "challenge": [
            arith("Un paisaje tiene 4 cerros al fondo, 3 árboles en el medio y 2 ovejas adelante. ¿Cuántas cosas dibujas en total?", "4 + 3 + 2", "Se suman las tres zonas del paisaje."),
            ex("En una hoja doblada por la mitad de arriba a abajo, ¿en qué mitad pones el cielo y las nubes: arriba o abajo?", "Arriba", "El cielo está en la parte alta del paisaje."),
        ],
    },
    context=[ex("Miras por la ventana: hay un perro dormido en el pasto, un árbol más atrás y cerros muy lejos. Quieres dibujar al perro como protagonista. Escribe qué cosa va grande abajo y qué cosa va pequeña arriba.", "El perro grande abajo; los cerros pequeños arriba", "El foco cercano se agranda y lo lejano se achica.")],
    selfcheck=[
        ex("¿Cómo se llama lo más importante de un dibujo?", "Foco", "Es el protagonista que se quiere destacar."),
        ex("Lo que está lejos, ¿se dibuja arriba y pequeño o abajo y grande?", "Arriba y pequeño", "La distancia hace que algo parezca pequeño."),
        ex("¿Para qué sirve encuadrar?", "Para elegir qué parte se va a dibujar", "El marco recorta una porción del paisaje."),
    ],
    open_task=task(
        "Elige UNO de estos paisajes escritos: (A) un cerro nevado al fondo, un lago y un pato que nada cerca; (B) una playa con rocas lejanas, olas y una gaviota parada en la arena; (C) un jardín con una cerca lejana, un árbol y una mariposa sobre una flor cercana. Decide cuál es tu foco, ponlo grande en el primer plano y dibuja el resto más pequeño y arriba. Escribe una frase: «Mi foco es… porque…».",
        "Elegí el paisaje A. Mi foco es el pato porque quiero mostrar un animal tranquilo. Lo dibujé grande abajo y el cerro pequeño arriba.",
        ["elige un foco", "pone lo cercano abajo y grande", "pone lo lejano arriba y pequeño"],
        ["dibujo con foco claro", "frase con la razón de su elección"],
        ["todo del mismo tamaño", "no decir cuál es el foco"],
        "Valora el foco elegido y sugiere agrandarlo o acercarlo más al centro si aún no destaca.",
    ),
    reinforce="Mira por una ventana o una puerta y con tu visor decide qué cosa será el foco de un dibujo.",
    extend="Dibuja el mismo paisaje dos veces cambiando el foco y cuenta qué cambia en cada dibujo.",
)

# ---------------------------------------------------------------- Clase 3
register(
    OA1, 3,
    materials="Una hoja, lápiz de mina, lápices de colores. Las escenas de la vida cotidiana están descritas en el cuaderno; no necesitas dibujar a personas reales ni escribir sus nombres.",
    use="Aprenderé a observar escenas de la vida de todos los días y a transformarlas en una idea para dibujar. Sirve para contar con imágenes lo que pasa en mi casa y en mi barrio.",
    prior=["Sé dibujar personas, objetos y lugares simples.", "Sé elegir un foco."],
    explain=[
        "El arte no solo muestra paisajes. También muestra lo que hacemos cada día: tomar once, cocinar, jugar en la plaza, esperar la micro. Esas escenas se llaman vida cotidiana y familiar. Muchos artistas las han pintado porque son importantes para las personas.",
        "Para transformar una observación en una idea visual, respondes cuatro preguntas: ¿quiénes están? ¿dónde están? ¿qué hacen? ¿qué objetos hay? Con las respuestas haces un boceto: un dibujo rápido y simple para probar ideas.",
        "Después decides qué mostrar y qué dejar fuera. Si quieres mostrar una conversación, dibujas a las personas cerca, mirándose. Si quieres mostrar soledad, las dibujas lejos. Las decisiones del artista cambian lo que se cuenta.",
    ],
    vocab=[("vida cotidiana", "lo que hacemos todos los días"), ("escena", "un momento donde pasa algo, con personas y lugar"), ("boceto", "dibujo rápido para probar una idea"), ("idea visual", "algo que quiero contar con una imagen"), ("objeto", "cosa que forma parte de la escena, como una taza o una silla")],
    worked=[
        {"title": "De la observación a la idea", "problem": "Observas: una abuela y su nieta tejen en la cocina, hay una tetera sobre la mesa y entra luz por la ventana. ¿Qué anotas para tu boceto?", "steps": ["¿Quiénes? Una abuela y una niña.", "¿Dónde? En la cocina.", "¿Qué hacen? Tejen.", "¿Qué objetos hay? Una tetera, lana y una ventana."], "answer": "Abuela y niña tejiendo en la cocina con tetera, lana y ventana"},
        {"title": "Decidir qué mostrar", "problem": "Quieres mostrar que la hora de la once es un momento compartido. ¿Cómo ubicas a las personas en el boceto?", "steps": ["Para mostrar que comparten, las dibujo cerca de la mesa.", "Las pongo mirándose o mirando la mesa.", "Dibujo grande la mesa con pan y tazas, porque es el foco."], "answer": "Personas juntas alrededor de la mesa con pan y tazas"},
    ],
    mistakes=[
        {"wrong": "Dibujar solo personas flotando sin lugar ni objetos.", "why": "Falta el lugar y lo que hacen, y no se entiende la escena.", "fix": "Agrega dónde están y un objeto que muestre qué hacen."},
        {"wrong": "Querer dibujar todo lo que pasa en la casa en un solo dibujo.", "why": "Hay demasiadas cosas y no hay foco.", "fix": "Elige un solo momento: la once, o jugar, o cocinar."},
    ],
    tiers={
        "recovery": [
            ex("Escena: dos niños juegan a la pelota en la plaza. ¿Dónde están?", "En la plaza", "La frase dice el lugar de la escena."),
            ex("Escena: un papá cocina arroz en la cocina. ¿Qué hace?", "Cocina arroz", "La acción es cocinar."),
            ex("Un boceto, ¿es un dibujo rápido o un dibujo terminado en muchos días?", "Un dibujo rápido", "El boceto es para probar ideas."),
        ],
        "understand": [
            ex("¿Cuáles son las cuatro preguntas para observar una escena? A: quiénes, dónde, qué hacen, qué objetos. B: cuánto, cuándo, cuántos, cuál. C: rojo, azul, verde, amarillo.", "A", "Esas preguntas describen la escena completa."),
            ex("¿Cuál NO es vida cotidiana? A: tomar once en familia. B: esperar la micro. C: un volcán en erupción en un cuento.", "C", "La vida cotidiana es lo de todos los días, no un hecho imaginario."),
            ex("Si dibujas dos personas muy lejos una de otra, ¿qué idea transmites con más probabilidad: compañía o distancia?", "Distancia", "La separación en el dibujo se lee como lejanía."),
        ],
        "apply": [
            ex("Observas: una niña riega las plantas del patio con un regador. Completa: quién = una niña, dónde = en el patio, qué hace = ___.", "Riega las plantas", "La acción es regar."),
            arith("En la mesa de la once hay 4 tazas y 3 panes. ¿Cuántos objetos dibujas en la mesa?", "4 + 3", "Se juntan tazas y panes."),
            ex("Quieres mostrar una escena de compartir en la plaza. ¿Qué dibujas: A dos niños que comparten una bicicleta, o B un niño solo mirando el suelo?", "A", "Compartir se ve cuando los dos usan lo mismo."),
        ],
        "reason": [
            ex("Raúl quiere mostrar «la mañana en mi casa» y dibujó diez cosas muy pequeñas. Dice que no se entiende. ¿Qué le conviene hacer: A elegir un momento y un foco, o B dibujar aún más cosas?", "A", "Elegir un solo momento aclara la escena."),
            ex("En un boceto hay una olla humeante y una cuchara de palo. ¿Qué acción es más probable: cocinar o dormir?", "Cocinar", "La olla y la cuchara pertenecen a la cocina."),
        ],
        "challenge": [
            arith("Una escena de plaza tiene 2 columpios con 1 niño cada uno, 3 niños en la arena y 1 perro. ¿Cuántos seres vivos hay?", "2 + 3 + 1", "Se cuentan los niños en los columpios, en la arena y el perro."),
            ex("Escribe en una frase una idea visual con quiénes, dónde y qué hacen para esta observación: dos hermanos ayudan a tender la ropa en un patio.", "Dos hermanos tienden la ropa en el patio", "La frase reúne quiénes, qué hacen y dónde."),
        ],
    },
    context=[ex("Tu familia ve una película en el living: hay un sofá, una manta, un tazón de cabritas y la luz azul de la pantalla. Escribe dónde están y dos objetos que dibujarías.", "En el living; el sofá y el tazón de cabritas", "El lugar es el living y los objetos están nombrados.")],
    selfcheck=[
        ex("¿Qué es la vida cotidiana?", "Lo que hacemos todos los días", "Son las rutinas de cada día."),
        ex("¿Para qué sirve un boceto?", "Para probar ideas", "Es un dibujo rápido de ensayo."),
        ex("En el patio dibujas un regador y una planta. ¿Qué acción cuentan?", "Regar", "El regador y la planta cuentan que se riega."),
    ],
    open_task=task(
        "Elige UNA escena escrita: (A) una familia toma once en la mesa con pan, mantequilla y tazas; (B) un niño y un abuelo plantan una semilla en una maceta del patio; (C) dos amigas esperan la micro en un paradero bajo la lluvia con paraguas. Haz un boceto respondiendo: quiénes, dónde, qué hacen y qué objetos hay. No escribas nombres reales.",
        "Elegí la escena B. Quiénes: un niño y un abuelo. Dónde: en el patio. Qué hacen: plantan una semilla. Objetos: maceta, tierra y pala. Los dibujé cerca porque quiero mostrar que trabajan juntos.",
        ["responde las cuatro preguntas", "hace un boceto con lugar y objetos", "explica una decisión"],
        ["boceto", "las cuatro respuestas escritas o dichas"],
        ["dibujar figuras sin lugar", "poner demasiadas cosas sin foco"],
        "Reconoce la escena clara y sugiere un objeto más que muestre mejor la acción.",
    ),
    reinforce="Observa a tu familia durante la once y di quiénes están, dónde y qué hacen.",
    extend="Haz dos bocetos de la misma escena cambiando la distancia entre las personas y cuenta qué cambia.",
)

# ---------------------------------------------------------------- Clase 4
register(
    OA1, 4,
    materials="Una hoja y lápiz. Las obras están descritas por escrito en el cuaderno; no necesitas verlas en imágenes, aunque una persona adulta puede mostrarte fotos de ellas.",
    use="Aprenderé a mirar obras de artistas chilenos y a reconocer qué decisiones tomaron con sus materiales, formas y colores. Sirve para aprender de ellos y tener ideas para mis propios trabajos.",
    prior=["Sé nombrar formas y colores.", "Sé decir qué veo en una imagen."],
    explain=[
        "Los artistas chilenos también miraron su entorno para crear. Violeta Parra, que vivió entre 1917 y 1967, bordó con lanas de colores sobre tela de saco unas obras llamadas arpilleras, que cuentan escenas de la vida y la música. En 1964 las expuso en París, en el palacio del Louvre.",
        "Roberto Matta nació en Santiago en 1911. En muchas de sus pinturas hay formas que flotan, líneas que cruzan y colores muy vivos, como si el espacio estuviera en movimiento. Claudio Bravo, que nació en Valparaíso en 1936, pintó objetos como paquetes envueltos en papel con tanto detalle que parecen reales.",
        "Cuando miras una obra puedes preguntarte qué decidió el artista: ¿qué material usó? ¿qué colores eligió? ¿qué forma repitió? Reconocer esas decisiones te ayuda a pensar tus propias decisiones, sin copiar la obra.",
    ],
    vocab=[("arpillera", "obra hecha con lanas y telas cosidas sobre un fondo de tela de saco"), ("pintura", "obra hecha con colores aplicados sobre una superficie"), ("decisión del artista", "elección de material, color o forma que cambia cómo se ve la obra"), ("artista", "persona que crea obras para expresar ideas o emociones"), ("local o chileno", "creado en Chile o por artistas de Chile")],
    worked=[
        {"title": "Reconocer el material", "problem": "Una arpillera de Violeta Parra muestra una escena hecha con lanas de colores cosidas sobre tela de saco. ¿Qué material eligió para el fondo?", "steps": ["Leo cómo se describe la obra.", "El fondo es de tela de saco.", "Las figuras son de lana cosida."], "answer": "Tela de saco"},
        {"title": "Reconocer una forma repetida", "problem": "En una pintura de Matta hay muchas líneas finas que cruzan el cuadro, formas redondeadas flotando y colores brillantes. ¿Qué decisión de forma se nota?", "steps": ["Miro las formas: redondeadas y flotando.", "Miro las líneas: finas y cruzadas.", "Las dos dan sensación de movimiento."], "answer": "Formas flotando y líneas que cruzan"},
    ],
    mistakes=[
        {"wrong": "Decir «este artista no sabía dibujar» porque la obra no se parece a la realidad.", "why": "Se confunde parecido con calidad; el artista pudo decidir otra forma de mostrar.", "fix": "Pregunta qué decidió mostrar y con qué material."},
        {"wrong": "Querer copiar la obra exactamente.", "why": "Se copia y no se toman decisiones propias.", "fix": "Elige solo una idea que te guste, como el material o el tipo de línea, y úsala en tu propio tema."},
    ],
    tiers={
        "recovery": [
            ex("¿Quién bordó arpilleras y las expuso en el Louvre en 1964?", "Violeta Parra", "La exposición en París fue de ella en 1964."),
            ex("¿En qué ciudad chilena nació Claudio Bravo?", "Valparaíso", "Bravo nació en Valparaíso en 1936."),
            ex("Una arpillera se hace con lana y telas cosidas. ¿Se pinta con témpera o se cose?", "Se cose", "Sus figuras se bordan y se cosen sobre la tela."),
        ],
        "understand": [
            ex("¿Cuál de estos artistas pintó formas que flotan y líneas que cruzan? A: Roberto Matta. B: Claudio Bravo.", "A", "Matta pintó espacios con movimiento y formas flotantes."),
            ex("¿Qué es una decisión del artista? A: elegir un material, color o forma. B: copiar una foto. C: no usar ningún color.", "A", "Esas elecciones cambian el aspecto de la obra."),
            ex("Claudio Bravo pintó paquetes que parecen reales. ¿Mostró mucho detalle o poco detalle?", "Mucho detalle", "Para que parezcan reales hay que pintar con detalle."),
        ],
        "apply": [
            ex("Mira la descripción: «lanas rojas, amarillas y verdes sobre tela de saco café». ¿Cuántos colores de lana se nombran?", "3", "Se nombran rojo, amarillo y verde."),
            ex("Una obra tiene un paquete envuelto en papel café con un cordel, pintado con muchos pliegues. ¿Qué decisión de detalle tomó el artista?", "Pintar los pliegues del papel", "Los pliegues son un detalle que se ve en la obra."),
            ex("Una arpillera tiene 2 casas, 3 árboles y 1 sol bordados con lana. ¿Cuántas figuras bordadas hay?", "6", "Se juntan 2, 3 y 1: son 6 figuras."),
        ],
        "reason": [
            ex("Un amigo dice: «Matta pintó mal porque no hay casas ni árboles». ¿Es buena razón?", "No", "El artista decidió mostrar formas y espacio, no objetos conocidos."),
            ex("Quieres tomar una idea de Violeta Parra para tu obra. ¿Qué tomas: A usar lana de colores sobre un fondo de tela o papel grueso, o B copiar su obra tal cual?", "A", "Usar un material es una idea propia; copiar la obra no."),
        ],
        "challenge": [
            ex("Una pintura de Matta tiene 5 formas flotantes y 4 líneas que cruzan. ¿Cuántas cosas ves en total?", "9", "Se juntan 5 y 4: son 9."),
            ex("Escribe una decisión de Matta y una de Bravo que sean distintas.", "Matta: formas que flotan; Bravo: objetos muy detallados", "Una decisión es de movimiento y la otra de detalle realista."),
        ],
    },
    context=[ex("En tu escuela hay un mural pintado por artistas del barrio con una playa, barcos de colores y gaviotas. Nombra una decisión que tomaron los artistas.", "Elegir barcos de colores", "Los barcos y sus colores son una elección visible.")],
    selfcheck=[
        ex("¿Qué es una arpillera?", "Una obra con lanas y telas cosidas sobre tela de saco", "Es una técnica textil, no pintura."),
        ex("¿En qué año Violeta Parra expuso en el Louvre?", "1964", "Esa fue la fecha de su exposición en París."),
        ex("¿Qué debes hacer al ver una obra famosa: copiarla o reconocer decisiones del artista?", "Reconocer decisiones del artista", "Se aprende de las elecciones, no de la copia."),
    ],
    open_task=task(
        "Elige UNA obra de las descritas: (A) una arpillera con lanas de colores sobre tela de saco; (B) una pintura de Matta con formas flotantes y líneas que cruzan; (C) una pintura de Bravo de un paquete envuelto, muy detallado. Escribe o dibuja una decisión que podrías tomar tú en tu propia obra, por ejemplo cambiar el material, sin copiarla.",
        "Elegí la obra A. Yo haré una escena de mi plaza con retazos de tela y lana pegados sobre cartón. Tomé la idea del material, pero mi tema es distinto.",
        ["elige una obra descrita", "señala una decisión que tomará", "evita copiarla"],
        ["una frase escrita o dicha", "un dibujo pequeño de su idea"],
        ["copiar la composición completa", "decir solo si le gusta o no"],
        "Valora que reconoce la decisión del artista y pide precisar su tema propio.",
    ),
    reinforce="Pide a un adulto que te muestre una foto de una arpillera y cuenta qué ves en ella.",
    extend="Busca en tu casa un material que podrías cambiar por lana o tela y di qué efecto tendría en tu obra.",
)

# ---------------------------------------------------------------- Clase 5
register(
    OA1, 5,
    materials="Una hoja y lápiz. Las obras de América Latina y del mundo están descritas por escrito en el cuaderno; una persona adulta puede mostrarte fotos si quiere.",
    use="Aprenderé a comparar cómo distintos artistas de América Latina y de otros lugares muestran lo que ven. Sirve para ver que hay muchas maneras de representar el mismo mundo.",
    prior=["Sé que los artistas toman decisiones.", "Sé nombrar colores y formas."],
    explain=[
        "El arte de América Latina tiene muchas voces. Joaquín Torres García, de Uruguay, dibujó en 1943 un mapa de Sudamérica con el sur arriba, y dijo que nuestro norte es el sur. Tarsila do Amaral, de Brasil, pintó en 1928 una obra llamada Abaporu: una figura con un pie enorme, cabeza pequeña y un cactus. Fernando Botero, de Colombia, pintó personas y animales de formas redondas y voluminosas.",
        "También hay arte de otros lugares del mundo. Vincent van Gogh, de los Países Bajos, pintó en 1889 La noche estrellada, con un cielo azul lleno de remolinos amarillos. Claude Monet, de Francia, pintó en 1872 Impresión, sol naciente, con un sol naranja entre neblina azul y gris.",
        "Cada artista representa de otra manera: unos exageran las formas, otros las simplifican, otros usan pinceladas visibles. Comparar es buscar parecidos y diferencias. No hay una forma correcta de mostrar el mundo, sino muchas formas posibles.",
    ],
    vocab=[("representar", "mostrar algo con dibujo, pintura u otro medio"), ("comparar", "buscar en qué dos cosas se parecen y en qué se diferencian"), ("exagerar", "hacer algo más grande o más fuerte de lo que es"), ("simplificar", "dejar solo las formas más importantes"), ("pincelada", "huella que deja el pincel con pintura")],
    worked=[
        {"title": "Comparar dos obras", "problem": "Botero pinta figuras redondas y voluminosas. Torres García dibuja un mapa con el sur arriba. ¿En qué se diferencian sus obras?", "steps": ["Botero muestra personas y animales de formas redondas.", "Torres García muestra un mapa de América dado vuelta.", "Una obra muestra volumen y la otra un mapa: son distintas."], "answer": "Botero muestra figuras redondas; Torres García, un mapa con el sur arriba"},
        {"title": "Reconocer cómo se representa", "problem": "En La noche estrellada hay un cielo azul con remolinos amarillos. ¿Van Gogh representó el cielo de forma quieta o con movimiento?", "steps": ["Miro los remolinos: son curvos y marcan giros.", "Giros dan idea de movimiento.", "El cielo parece moverse."], "answer": "Con movimiento"},
    ],
    mistakes=[
        {"wrong": "Decir que una obra es mejor porque se parece más a una foto.", "why": "Se piensa que solo vale lo realista.", "fix": "Compara cómo cada artista decidió mostrar: exagerar, simplificar o repetir pinceladas."},
        {"wrong": "Mezclar a los artistas y sus países.", "why": "Se memoriza sin ordenar los datos.", "fix": "Anota artista, país y una característica en una tabla pequeña."},
    ],
    tiers={
        "recovery": [
            ex("¿De qué país es Fernando Botero?", "Colombia", "Botero nació en Colombia."),
            ex("¿De qué país es Tarsila do Amaral?", "Brasil", "Tarsila nació en Brasil."),
            ex("¿Quién pintó La noche estrellada?", "Vincent van Gogh", "Es su obra de 1889."),
        ],
        "understand": [
            ex("¿Cuál de estas obras tiene el sur arriba en un mapa de Sudamérica? A: de Torres García. B: de Monet.", "A", "Torres García dibujó la América invertida."),
            ex("Botero pinta figuras redondas y grandes. ¿Exagera o simplifica el volumen?", "Exagera", "Hace los cuerpos mucho más voluminosos."),
            ex("¿Qué significa comparar dos obras? A: elegir la más cara. B: buscar parecidos y diferencias. C: copiar la más antigua.", "B", "Comparar es observar semejanzas y diferencias."),
        ],
        "apply": [
            ex("Según la clase, en Abaporu hay un pie enorme, una cabeza pequeña y un cactus. ¿Cuántas partes se nombran?", "3", "Se nombran el pie, la cabeza y el cactus."),
            ex("Monet pintó en Impresión, sol naciente un sol de color naranja entre neblina azul y gris. ¿Cuántos colores se nombran?", "3", "Se nombran naranja, azul y gris."),
            ex("Ordena de la figura más pequeña a la más grande: A un pie enorme, B una cabeza pequeña, C un cuerpo mediano.", "B, C, A", "La cabeza es la más pequeña, el cuerpo es mediano y el pie es enorme."),
        ],
        "reason": [
            ex("Una compañera dice: «La figura de Botero está mal dibujada porque es muy gorda». ¿Qué le explicas: A que el artista decidió hacer los volúmenes grandes, o B que no sabía dibujar?", "A", "Exagerar el volumen es una decisión y no un error."),
            ex("¿Por qué Torres García puso el sur arriba? A: por un error de dibujo. B: para mostrar que el sur es importante para América. C: porque se le cayó el papel.", "B", "Escribió que el norte es el sur, como idea sobre América."),
        ],
        "challenge": [
            arith("Una tabla tiene 3 obras latinoamericanas y 2 obras del mundo. ¿Cuántas obras hay en la tabla?", "3 + 2", "Se juntan ambos grupos."),
            ex("Escribe una diferencia entre La noche estrellada y Abaporu.", "Una tiene cielo con remolinos y la otra una figura con pie enorme", "Se nombra una característica distinta de cada obra."),
        ],
    },
    context=[ex("En una exposición del colegio ves dos pinturas: en una hay una persona de cuerpo muy redondo y en otra un campo hecho con pinceladas cortas de colores. Di cuál tiene formas exageradas.", "La de la persona de cuerpo muy redondo", "El cuerpo muy redondo exagera el volumen.")],
    selfcheck=[
        ex("¿Qué artista pintó figuras redondas y voluminosas?", "Fernando Botero", "Es su marca más conocida."),
        ex("¿En qué país nació Joaquín Torres García: Uruguay o Brasil?", "Uruguay", "Torres García es uruguayo."),
        ex("¿Existe una sola manera correcta de representar el mundo?", "No", "Hay muchas maneras de mostrar lo que vemos."),
    ],
    open_task=task(
        "Elige DOS obras descritas: (A) La noche estrellada de Van Gogh; (B) Abaporu de Tarsila do Amaral; (C) una figura redonda de Botero; (D) el mapa invertido de Torres García. Dibuja un cuadrado para cada una con una forma o color que la recuerde, y escribe una frase que diga en qué se parecen o en qué se diferencian.",
        "Elegí A y C. En A el cielo tiene remolinos y en C las figuras son redondas. Se parecen en que las formas curvas son muy importantes.",
        ["elige dos obras", "dibuja una pista visual de cada una", "compara con una frase"],
        ["dos dibujos pequeños", "una frase de comparación"],
        ["decir cuál es mejor sin razones visuales", "confundir artista y país"],
        "Valora la comparación y pide nombrar el elemento visual exacto que tienen en común.",
    ),
    reinforce="Con ayuda de un adulto, busca una foto de La noche estrellada y cuenta cuántos colores distintos ves.",
    extend="Elige un artista de esta clase, anota su país y una característica de su obra, y compártelo con alguien.",
)

# ---------------------------------------------------------------- Clase 6
register(
    OA1, 6,
    materials="Hojas para pruebas, lápiz de mina, lápices de colores o témperas, y un objeto de la naturaleza o una escena de tu casa. Las opciones de tema están escritas en el cuaderno.",
    use="Aprenderé a crear una obra propia a partir de lo que observo y a explicar las decisiones que tomé. Sirve para que mi trabajo muestre mi manera de mirar y no una copia.",
    prior=["Sé observar formas, colores y detalles.", "Sé elegir un foco y pensar una composición."],
    explain=[
        "Una obra con punto de vista propio es aquella donde tú decides qué mostrar y cómo mostrarlo. Dos personas pueden mirar la misma hoja y dibujarla distinto, y las dos obras valen, porque cada una muestra una manera de mirar.",
        "El proceso tiene pasos: primero observas y anotas; luego haces dos pruebas pequeñas con ideas distintas; después eliges una prueba y dices por qué; finalmente desarrollas la obra y puedes cambiar algo si ves que mejora.",
        "Al terminar explicas tus decisiones con una frase: «Elegí… porque…». La razón debe hablar de lo que se ve en tu obra: una línea, un color, una forma o un material. No es una razón decir solo «porque sí» o «porque me quedó bonito».",
    ],
    vocab=[("punto de vista", "mi manera de mirar y de mostrar algo"), ("prueba", "ensayo pequeño para probar una idea"), ("decisión", "elección que hago al crear"), ("proceso", "los pasos que sigo para crear una obra"), ("fundamentar", "dar una razón basada en lo que se ve")],
    worked=[
        {"title": "Dos pruebas y una elección", "problem": "Observas una hoja de parra: tiene cinco puntas y líneas que salen como un abanico. Haces la prueba 1 con un solo trazo grueso por cada punta, y la prueba 2 con líneas finas bien marcadas. Eliges la 2. ¿Cómo lo explicas?", "steps": ["Miro la prueba 2: se ven las líneas del abanico.", "Eso era lo que más me llamó la atención de la hoja.", "Escribo: elegí la prueba 2 porque se ven las líneas finas que salen como un abanico."], "answer": "Elegí la prueba 2 porque muestra las líneas finas en forma de abanico"},
        {"title": "Cambiar una decisión", "problem": "Pintaste un girasol con el centro café y los pétalos amarillos pálidos, pero el girasol real tiene pétalos amarillo fuerte. ¿Qué cambias y cómo lo registras?", "steps": ["Comparo mi pintura con lo que observo.", "Cambio el amarillo pálido por uno más fuerte.", "Anoto: cambié el color de los pétalos porque el girasol real es amarillo fuerte."], "answer": "Cambié el color de los pétalos porque el girasol real es amarillo fuerte"},
    ],
    mistakes=[
        {"wrong": "Explicar «lo hice porque me gustó» y nada más.", "why": "La razón no habla de lo que se ve en la obra.", "fix": "Agrega un elemento visible: «porque usé líneas finas» o «porque el azul se ve frío»."},
        {"wrong": "Hacer una sola prueba y no cambiar nada.", "why": "Sin ensayar no se descubren otras posibilidades.", "fix": "Haz dos pruebas distintas y elige una."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué haces primero: observar o terminar la obra?", "Observar", "El proceso parte mirando lo que se va a representar."),
            ex("¿Qué es una prueba? A: un ensayo pequeño. B: una nota de cuaderno. C: una obra terminada.", "A", "La prueba permite ensayar una idea sin gastar la obra final."),
            ex("En la frase «Elegí el azul porque se ve frío», ¿qué palabra es la razón: azul o frío?", "Frío", "El efecto del color es lo que explica la elección."),
        ],
        "understand": [
            ex("¿Qué quiere decir tener punto de vista propio? A: copiar al compañero. B: decidir cómo mostrar lo que observo. C: no usar colores.", "B", "Es mostrar el mundo desde mi manera de mirar."),
            ex("¿Cuál es una buena razón? A: «Porque sí». B: «Porque las líneas finas muestran las nervaduras de la hoja».", "B", "La razón nombra algo que se ve en la obra."),
            ex("Si dos niños dibujan la misma piedra de manera distinta, ¿una está obligatoriamente mal?", "No", "Cada una muestra una forma de mirar."),
        ],
        "apply": [
            ex("Ordena el proceso con letras: A elegir una prueba, B observar y anotar, C hacer dos pruebas, D explicar la decisión final.", "B, C, A, D", "Se observa, se prueba, se elige y se explica."),
            arith("Hiciste 2 pruebas con 3 hojas de girasol cada una. ¿Cuántas hojas de girasol dibujaste en total?", "3 + 3", "Son dos grupos de tres hojas: 3 y 3."),
            ex("Completa: «Cambié el verde claro por verde oscuro porque la hoja real es oscura». ¿Qué decisión cambió: la forma o el color?", "El color", "El verde claro y el oscuro son colores."),
        ],
        "reason": [
            ex("Beto dice: «Elegí la prueba 1 porque sí». ¿Qué le falta a su explicación?", "Una razón basada en lo que se ve", "Hay que nombrar un elemento visible de su obra."),
            ex("Carla compara su dibujo con la concha real y ve que le faltan las rayitas. ¿Qué debe hacer: A agregar las rayitas, B borrar todo?", "A", "Agrega el detalle observado para acercarse a lo que ve."),
        ],
        "challenge": [
            arith("En tu cuaderno de proceso anotaste 4 cosas que observaste, 2 pruebas y 1 decisión final. ¿Cuántas anotaciones hay en total?", "4 + 2 + 1", "Se suman las tres clases de anotaciones."),
            ex("Escribe una frase con «Elegí… porque…» para una obra con una piedra gris donde usaste solo lápiz de mina.", "Elegí el lápiz de mina porque la piedra es gris", "La razón relaciona el material con el color observado."),
        ],
    },
    context=[ex("Tu curso observó un cactus del patio. Mía lo dibujó con líneas rectas porque tiene espinas largas. Ema lo pintó con manchas verdes porque le interesó su color. ¿Una de las dos obras está equivocada?", "No, muestran dos puntos de vista", "Cada una elige un aspecto distinto del cactus.")],
    selfcheck=[
        ex("¿Cuántas pruebas se hacen antes de elegir una?", "Dos", "Se ensayan dos ideas distintas."),
        ex("¿Qué palabra usas para dar una razón: porque o también?", "Porque", "Porque introduce la razón."),
        ex("¿Qué debe nombrar una razón: algo que se ve o algo que se siente solo?", "Algo que se ve", "La razón se apoya en la obra."),
    ],
    open_task=task(
        "Elige UNO de estos temas: (A) una hoja con borde de dientitos; (B) una escena de tu casa con alguien tomando once; (C) un animal pequeño del patio, como un caracol. Haz dos pruebas pequeñas con ideas distintas, elige una, desarróllala en una hoja entera y escribe: «Elegí… porque…» y «Cambié… porque…».",
        "Elegí la hoja (A). Prueba 1: relleno de verde. Prueba 2: solo líneas. Elegí la 2 porque se ven los dientitos. Cambié el contorno porque tenía menos picos que la hoja.",
        ["hace dos pruebas distintas", "elige con una razón visible", "registra un cambio"],
        ["dos pruebas pequeñas", "obra final", "frases «Elegí… porque…» y «Cambié… porque…»"],
        ["copiar un modelo", "dar razones que no se ven en la obra"],
        "Reconoce la decisión propia y propone una pregunta que ayude a justificar con mayor precisión.",
    ),
    reinforce="Elige un objeto de tu casa, haz una prueba pequeña y cuenta qué cambiarías.",
    extend="Haz una tercera prueba con un material distinto y explica en qué se diferencia de las otras dos.",
)
