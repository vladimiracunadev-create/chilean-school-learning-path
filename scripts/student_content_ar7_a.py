"""Cuaderno del estudiante de 7.º básico Artes Visuales: AR07 OA 01 (crear a partir de percepciones, sentimientos e ideas tras observar manifestaciones sobre diversidad cultural, género e íconos sociales, patrimoniales y contemporáneos)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "AR07 OA 01"


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


# ---------------------------------------------------------------- Clase 1
lesson(
    OA1, 1,
    "Un cuaderno o varias hojas, lápiz de mina y lápices de colores. Las tres manifestaciones que se observan están descritas en esta clase; no necesitas buscarlas.",
    "Aprenderé a observar una manifestación estética con atención y a anotar en una bitácora dos detalles, una pregunta y una posibilidad para crear. Sirve para empezar una obra propia sin copiar.",
    ["Sé que una intención dice qué quiero comunicar, cómo y por qué.", "Sé separar lo que se ve (dato) de lo que opino."],
    [
        "Una manifestación estética es cualquier obra, objeto, espacio o imagen hecha para ser vista, sentida o interpretada: un mural, una artesanía, un afiche, una fotografía, una plaza. Puede ser patrimonial, si una comunidad la heredó y la cuida, o contemporánea, si se hace en nuestra época. Un ícono social es una imagen que muchas personas reconocen y que representa una idea o un grupo, como una bandera o el símbolo de un equipo.",
        "Para observar con cuidado uso una bitácora, un cuaderno donde anoto sin apuro. En cada manifestación registro cuatro cosas: dos detalles que veo (color, forma, material, tamaño), una pregunta abierta que me deja pensando y una posibilidad expresiva, es decir, una decisión visual que yo podría probar en mi propia obra. La pregunta abierta puede tener varias respuestas, como «¿qué querrá decir el color de este fondo?».",
        "También miro cómo se muestra a las personas: si aparecen mujeres, hombres o personas de distintas culturas, qué hacen y cómo se ven. Un estereotipo es una idea fija y simplificada sobre un grupo, como pensar que todas las personas de un mismo lugar son iguales. Una sola imagen no representa a toda una cultura: solo muestra lo que su autor o autora decidió mostrar. Por eso uso frases como «en esta imagen se ve…» y no «todas las personas son…».",
    ],
    [("manifestación estética", "obra, objeto, espacio o imagen hecha para ser vista y sentida"), ("patrimonial", "heredado y cuidado por una comunidad"), ("ícono social", "imagen que muchas personas reconocen y que representa una idea o un grupo"), ("bitácora", "cuaderno donde se anotan observaciones y pruebas"), ("estereotipo", "idea fija y simplificada sobre un grupo de personas")],
    [
        w("Llenar la bitácora", "Observas esta imagen de ejemplo: un mural en un muro de barrio muestra a una mujer con casco que sostiene una escalera, con un fondo azul y líneas amarillas que salen de sus manos. Registra dos detalles, una pregunta y una posibilidad.", ["Detalle 1: el fondo es azul y las líneas son amarillas.", "Detalle 2: la mujer lleva casco y sostiene una escalera.", "Pregunta abierta: ¿qué significarán las líneas que salen de sus manos?", "Posibilidad: en mi obra podría usar líneas de un solo color que salgan de las manos de mi personaje."], "Dos detalles (fondo azul con líneas amarillas, casco y escalera), una pregunta abierta sobre las líneas y una posibilidad de usar líneas que salgan de las manos"),
        w("Evitar la generalización", "Escribiste: «Este bordado muestra cómo son todas las familias de esa región». Corrígelo.", ["La frase habla de todas las familias, y un solo bordado no puede mostrarlas.", "Un bordado muestra lo que su autora decidió mostrar.", "Reescribo hablando solo de lo que se ve."], "«En este bordado se ven dos personas junto a una casa, según lo que decidió mostrar su autora»"),
    ],
    [
        m("Anotar solo «es lindo» o «no me gusta» en la bitácora.", "No hay un dato que se pueda comprobar ni una idea que sirva para crear.", "Escribe qué ves (color, forma, material) y después tu opinión."),
        m("Decir que una imagen muestra a toda una cultura o a todo un género.", "Una sola imagen es una elección de su autor o autora, no un retrato completo.", "Habla solo de lo que se ve en esa imagen y de su autoría."),
    ],
    [
        ex("En la bitácora anotaste: «El afiche tiene letras rojas muy grandes». ¿Es un detalle que se ve o una pregunta?", "Un detalle que se ve", "Describe color y tamaño de algo que se puede comprobar mirando."),
        ex("¿Cuál de estas anotaciones es una pregunta abierta? A. «¿Por qué el artista dejó vacío el centro?» B. «¿El centro está vacío, sí o no?».", "A", "La A admite varias explicaciones; la B se responde con un sí o un no."),
        ex("Una plaza con una estatua que su comunidad cuida desde hace generaciones, ¿es una manifestación patrimonial o contemporánea?", "Patrimonial", "Una comunidad la heredó y la sigue cuidando."),
    ],
    [
        ex("Tu bitácora pide dos detalles, una pregunta y una posibilidad. Anotaste: «Detalle: el mural es azul. Pregunta: ¿por qué esa mujer sonríe? Posibilidad: pintaría un fondo anaranjado». ¿Qué falta?", "Un segundo detalle", "Piden dos detalles y solo hay uno."),
        ex("Una imagen muestra a un hombre cocinando y a una mujer arreglando un techo. ¿Qué observarías para pensar en los estereotipos de género? A. Si lo que hacen sigue una idea fija sobre hombres y mujeres o la rompe B. Solo de qué color es la ropa.", "A", "Un estereotipo se revisa mirando qué se muestra que hagan las personas."),
        ex("¿Cuál frase generaliza una cultura entera a partir de una imagen? A. «Esta foto de una feria muestra a una vendedora y a un niño» B. «Esta foto de una feria demuestra cómo es toda esa cultura».", "B", "La B pasa de una foto a toda una cultura; la A solo describe lo que se ve."),
    ],
    [
        ex("Observas una bandera de un club deportivo pintada en un muro: franjas verticales verdes y blancas, y un círculo al centro. Muchas personas del barrio la reconocen. ¿Qué tipo de imagen es? A. Un ícono social B. Una artesanía patrimonial.", "A", "Es una imagen que muchas personas reconocen y que representa un grupo."),
        ex("Un afiche tiene tres personas del mismo tamaño, un fondo liso y letras grandes arriba. ¿Cuál anotación sirve como detalle en la bitácora? A. «Las tres personas tienen el mismo tamaño» B. «El afiche es bonito».", "A", "Es un dato visible; «bonito» es una opinión que no se puede comprobar."),
        ex("Una fotografía muestra una artesanía de cestería hecha en fibra vegetal, trenzada en espiral. ¿Qué detalle de material anotarías: fibra vegetal trenzada o pintura brillante?", "Fibra vegetal trenzada", "El material que describe la foto es la fibra trenzada; la pintura no aparece."),
    ],
    [
        ex("Anotaste una posibilidad: «Podría usar muchas manos pequeñas en vez de una mano grande». ¿Es una posibilidad expresiva o una copia del mural?", "Una posibilidad expresiva", "Es una decisión visual propia que se puede probar, no la imagen repetida."),
        ex("Dos compañeros miran el mismo afiche. Uno anota «las personas parecen cansadas». La otra anota «hay tres personas con la cabeza inclinada». ¿Cuál anotación es un dato más comprobable?", "La de la cabeza inclinada", "Se puede ver y contar; «cansadas» ya es una interpretación."),
    ],
    [
        ex("Un cartel de fiesta tiene un sol dorado enorme y personas pequeñas abajo. ¿Qué pregunta abierta sirve para tu bitácora? A. «¿Por qué el sol es tan grande frente a las personas?» B. «¿El sol es dorado?».", "A", "La A invita a pensar en una decisión; la B se responde mirando."),
        ex("Si una persona escribe «todas las mujeres del mural cuidan niños» tras ver una sola imagen con una mujer y un bebé, ¿qué error cometió?", "Generalizó a partir de una sola imagen", "Una imagen no puede mostrar a todas las mujeres; solo a lo que su autor decidió mostrar."),
    ],
    ex("En una feria artesanal ves un mantel bordado con flores rojas, hilos gruesos y un borde de triángulos. Para tu bitácora, ¿cuál posibilidad es expresiva y no copia? A. copiar el bordado exacto en tu cuaderno B. probar tus propios triángulos en otro color.", "B", "Probar triángulos propios es una decisión nueva; copiar el bordado exacto no deja idea propia."),
    [
        ex("¿Qué cuatro cosas se registran de cada manifestación?", "Dos detalles, una pregunta y una posibilidad", "Eso pide la bitácora de observación."),
        ex("Verdadero o falso: una imagen basta para decir cómo es una cultura completa.", "Falso", "Una imagen muestra solo lo que su autor decidió mostrar."),
        ex("En Artes Visuales, ¿qué es un estereotipo?", "Una idea fija y simplificada sobre un grupo", "Ignora que las personas de un grupo son distintas entre sí."),
    ],
    task(
        "Elige UNA manifestación descrita aquí. A) Un mural de barrio: una mujer con casco y una escalera, fondo azul y líneas amarillas. B) Un bordado: dos personas junto a una casa, hilos gruesos y un borde de triángulos. C) Un afiche de fiesta: un sol dorado enorme y personas pequeñas abajo. En tu bitácora anota dos detalles, una pregunta abierta y una posibilidad expresiva propia, y haz un dibujo rápido de esa posibilidad.",
        "Elegí la C. Detalle 1: el sol es dorado y ocupa la mitad del afiche. Detalle 2: las personas son pequeñas y están abajo. Pregunta: ¿por qué el sol es tan grande frente a las personas? Posibilidad: dibujaré una luna grande y una sola persona pequeña, con colores fríos.",
        ["anota dos detalles que se ven", "escribe una pregunta abierta", "propone una posibilidad expresiva propia", "no generaliza una cultura ni copia la imagen"],
        ["bitácora con dos detalles, pregunta y posibilidad", "dibujo rápido de la posibilidad"],
        ["anotar solo opiniones", "copiar la imagen en vez de proponer algo propio"],
        "Señala el detalle más comprobable y pregunta qué decisión visual de la imagen lo provocó.",
    ),
    "Mira durante un minuto un envase, un afiche o un objeto de tu casa y di en voz alta un detalle que ves y una pregunta abierta sobre él.",
    "Escribe dos preguntas abiertas distintas para la misma imagen y explica cuál te ayuda más a imaginar una obra propia.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA1, 2,
    "Una hoja, lápiz de mina y lápices de colores o témpera. Las tres escenas de partida están escritas en esta clase.",
    "Aprenderé a relacionar lo que percibo, lo que siento y lo que pienso para formar una idea propia. Sirve para crear una obra con sentido, sin usar fórmulas como «el rojo siempre es enojo».",
    ["Sé registrar detalles y preguntas en una bitácora.", "Sé que una idea propia no es una copia."],
    [
        "Percibir es captar algo con los sentidos: veo un color, siento una textura, oigo un ruido. Una emoción es lo que siento por eso que percibo: tranquilidad, sorpresa, tristeza, alegría. Una idea es lo que pienso o interpreto a partir de ambas: «este lugar me hace sentir cuidado». El camino es percepción, emoción e idea, y cada persona puede recorrerlo distinto frente a la misma imagen.",
        "No existe una fórmula fija. El rojo puede sentirse como calor, como peligro o como fiesta, según el contexto y quien lo mire. En una imagen de una cocina, el rojo puede dar sensación de hogar; en una señal de tránsito, de alerta. Por eso no digo «el rojo significa enojo», sino «en este afiche, el rojo me hace sentir energía, porque está junto a figuras en movimiento». Siempre apoyo lo que siento en un detalle que se ve.",
        "Después convierto la idea en una decisión visual: elijo un color, una forma, una línea o un material que ayude a comunicarla, y pruebo cómo cambia el efecto. Mis emociones son una fuente válida, pero no tengo que contar mi vida personal para crear: puedo partir de lo que me provoca un lugar, un objeto o una imagen. Lo importante es poder explicar qué vi, qué sentí y qué decidí.",
    ],
    [("percepción", "lo que capto con los sentidos"), ("emoción", "lo que siento frente a algo"), ("idea", "lo que pienso o interpreto a partir de lo que percibo y siento"), ("interpretar", "dar un sentido propio a lo que veo, apoyado en detalles"), ("fórmula", "regla fija que se repite sin pensar, como «rojo = enojo»")],
    [
        w("Del detalle a la idea", "Ves una fotografía de ejemplo: una lámpara amarilla encendida en una ventana, en medio de un barrio oscuro y gris. Escribe percepción, emoción e idea.", ["Percibo: un punto amarillo muy pequeño en un fondo gris y oscuro.", "Siento: calma y un poco de soledad.", "Pienso: que hay alguien despierto y acompañando la noche."], "Percepción: lámpara amarilla en un fondo gris; emoción: calma; idea: alguien acompaña la noche"),
        w("Rechazar la fórmula", "Un compañero dice: «El azul siempre muestra tristeza». Responde con un ejemplo.", ["Un cielo azul de verano puede dar alegría.", "Un uniforme azul puede dar sensación de orden.", "La emoción depende del contexto y de cada persona."], "El azul no siempre muestra tristeza: en un cielo de verano puede dar alegría y en un uniforme, orden"),
    ],
    [
        m("Decir que cada color tiene un único significado que sirve para todas las imágenes.", "El mismo color cambia de efecto según el contexto, la forma y quien lo mira.", "Explica el efecto de un color apoyándote en lo que lo rodea en esa imagen."),
        m("Escribir solo la emoción («me da pena») sin decir qué detalle la provocó.", "Sin un detalle visible, no se puede transformar en una decisión para crear.", "Une siempre lo que percibes con lo que sientes y con la idea que formas."),
    ],
    [
        ex("¿«Veo una textura áspera de lana gruesa» es una percepción o una emoción?", "Una percepción", "Capta algo con los sentidos, la vista y el tacto."),
        ex("«Esta imagen me da tranquilidad» ¿qué es: percepción, emoción o idea?", "Emoción", "Dice lo que siento frente a lo que veo."),
        ex("Ordena el camino: idea, percepción, emoción. ¿Cuál va primero?", "La percepción", "Primero capto algo con los sentidos; después siento y finalmente pienso."),
    ],
    [
        ex("Un cuadro de ejemplo muestra una mesa con muchas sillas vacías y una sola persona sentada. Una compañera siente soledad y otro siente espacio para llegar. ¿Es posible que ambas emociones sean válidas? A. Sí, mientras cada uno las apoye en detalles B. No, solo una puede ser la correcta.", "A", "Una misma imagen puede provocar emociones distintas si se apoyan en lo que se ve."),
        ex("¿Qué frase evita la fórmula? A. «El verde siempre es naturaleza» B. «En esta foto el verde me da frescura porque rodea un río».", "B", "La B apoya la emoción en un detalle de esa imagen."),
        ex("Percibes el ruido fuerte y repetido de la lluvia sobre un techo de zinc. ¿Qué frase apoya su emoción en un detalle que se percibe? A. «Me siento acompañado porque el ruido constante llena la casa» B. «Me siento acompañado porque el techo es azul».", "A", "La A parte del ruido que se percibe; el color del techo no aparece en la escena."),
    ],
    [
        ex("Tu idea es «los lugares vacíos esperan a alguien». Para mostrarla, ¿qué decisión sirve más: dejar un gran espacio blanco con una puerta entreabierta o llenar toda la hoja de figuras?", "Dejar un gran espacio blanco con una puerta entreabierta", "El espacio vacío y la puerta sugieren espera; llenar la hoja contradice la idea."),
        ex("Quieres comunicar energía de fiesta. ¿Qué línea usas: curvas rápidas que se cruzan o una línea horizontal fina y quieta?", "Curvas rápidas que se cruzan", "Las curvas movidas transmiten movimiento y celebración."),
        ex("Para una obra sobre calma usas azul pálido. Si el mismo azul se pone junto a rojos muy fuertes y líneas quebradas, ¿sigue dando calma?", "No", "El contexto de rojos fuertes y líneas quebradas agrega tensión."),
    ],
    [
        ex("Dos estudiantes miran la misma foto de un mercado: uno escribe «me siento acogido» y apoya con «los toldos amarillos están juntos». La otra escribe «me siento agobiada» y apoya con «hay demasiadas personas». ¿Cuál escrito tiene su emoción apoyada en un detalle?", "Los dos", "Ambos citan un detalle visible que respalda lo que sienten."),
        ex("Un compañero afirma que su dibujo «da miedo porque usa negro». Su dibujo es un gato negro durmiendo sobre una frazada amarilla. ¿Es sólida su afirmación?", "No", "El negro, junto a un gato dormido y una frazada cálida, puede dar abrigo; no es una regla."),
    ],
    [
        ex("Tu idea es «el recuerdo de un verano». Escribe qué elemento visual eliges entre estos y por qué: A. tonos cálidos en manchas suaves, B. líneas negras muy duras. Elige el que mejor lo transmite.", "A", "Los tonos cálidos y suaves se asocian a calor y recuerdo; las líneas duras lo contradicen."),
        arith("Para probar tu idea haces 3 versiones con 2 colores principales cada una. ¿Cuántos colores principales usaste en total, si no repites ninguno?", "3*2", "Son 3 versiones con 2 colores distintos cada una."),
    ],
    ex("Ves por la ventana un patio con ropa colgada que se mueve con el viento: sábanas blancas, una toalla roja y dos calcetines azules. Escribe una frase con percepción, emoción e idea apoyada en esos detalles. Después elige si esta frase está bien formada: A. «Veo sábanas blancas moviéndose, me da calma y pienso que el viento ordena el día» B. «Esto es calma porque el blanco siempre es calma».", "A", "La A parte de lo que se ve y llega a una idea; la B usa una fórmula."),
    [
        ex("En Artes Visuales, ¿qué es percibir?", "Captar algo con los sentidos", "Es el primer paso antes de sentir y pensar."),
        ex("Verdadero o falso: un color tiene siempre el mismo significado.", "Falso", "Su efecto cambia con el contexto y con quien lo mira."),
        ex("¿Con qué tengo que apoyar una emoción al explicar una obra?", "Con un detalle que se ve", "Sin un detalle, la emoción no se puede comprobar ni transformar en decisión."),
    ],
    task(
        "Elige UNA escena. A) Una lámpara amarilla encendida en una ventana, en un barrio gris y oscuro. B) Un patio con ropa colgada que se mueve: sábanas blancas, una toalla roja y dos calcetines azules. C) Una micro llena a la hora de salida, con vidrios empañados y luces anaranjadas. Escribe percepción, emoción e idea; luego haz un dibujo de una decisión visual (color, línea o espacio) que comunique esa idea.",
        "Elegí la B. Percibo: telas que se mueven y colores claros con un toque rojo. Siento: alegría tranquila. Pienso: que el día se ordena con cosas simples. Decisión: líneas curvas largas, colores claros y un solo toque rojo en el centro.",
        ["escribe percepción, emoción e idea", "apoya la emoción en un detalle", "evita fórmulas de color", "su dibujo muestra una decisión visual coherente con la idea"],
        ["escrito con las tres partes", "dibujo con una decisión visual"],
        ["usar «el rojo siempre significa…»", "no relacionar el dibujo con la idea"],
        "Pregunta qué detalle de la escena provocó la emoción y cómo se ve esa emoción en el dibujo.",
    ),
    "Observa durante un minuto la luz en una pared de tu casa y di en voz alta qué percibes, qué sientes y qué idea se te ocurre.",
    "Explica por qué el mismo color puede dar sensaciones distintas en dos imágenes y dibuja un ejemplo corto de cada una.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA1, 3,
    "Dos hojas de papel, lápiz de mina, lápices de colores o témpera y un retazo de papel de diario o de caja limpia. El texto de partida está escrito en esta clase.",
    "Aprenderé a traducir una idea o una palabra a un lenguaje visual haciendo dos pruebas distintas y a elegir la mejor según mi intención. Sirve para ver cómo cambian el efecto y el significado cuando cambio una decisión.",
    ["Sé relacionar percepción, emoción e idea.", "Sé que una variable visual es una decisión que puedo cambiar para ver su efecto."],
    [
        "Traducir visualmente es llevar una idea, una sensación o una frase a imágenes, formas, colores o materiales. No es dibujar la frase tal cual, sino buscar cómo se vería lo que quiere decir. Por ejemplo, la frase «el barrio despierta» puede traducirse con luz que crece desde un borde de la hoja, con líneas que se alargan o con formas que se abren.",
        "Para experimentar hago dos pruebas con la misma idea y cambio una variable por vez: puede ser el color, la línea, la forma, la textura, el tamaño o el material. Con el mismo tema pruebo, por ejemplo, una versión con líneas rectas y una con líneas curvas. Pongo las dos lado a lado y comparo cuál comunica mejor mi intención. Una prueba que no resultó también enseña algo y la anoto.",
        "Cuando elijo una prueba explico por qué: «Elegí la de líneas curvas porque se siente más cercana». Esta explicación dice qué cambié, qué efecto vi y cómo se relaciona con mi idea. No necesito materiales especiales: sirven papel recortado, pintura escolar, papel de diario, lápices y objetos limpios de la casa. Trabajo con tijeras de punta redonda y sobre una superficie protegida.",
    ],
    [("traducir visualmente", "llevar una idea o sensación a imágenes, formas, colores o materiales"), ("variable visual", "decisión que se puede cambiar para ver su efecto"), ("prueba", "intento pequeño para comparar un efecto"), ("textura", "cómo se ve o se siente la superficie de algo"), ("comparar", "mirar dos cosas juntas para ver en qué se parecen y en qué se diferencian")],
    [
        w("Dos pruebas para una frase", "Debes traducir la frase «la ciudad nunca duerme». Haces la prueba A con rectángulos amarillos pequeños y muchos sobre fondo azul oscuro, y la prueba B con un solo círculo azul pálido. ¿Cuál se acerca más a la idea?", ["La frase habla de actividad constante, de muchas luces encendidas.", "La prueba A muestra muchas luces pequeñas sobre la noche.", "La prueba B tiene una sola forma quieta, sin actividad."], "La prueba A"),
        w("Cambiar una sola variable", "Quieres comparar el efecto de la línea. Tu prueba 1 tiene líneas rectas en azul. Escribe cómo debe ser la prueba 2.", ["Solo debe cambiar la línea.", "Mantengo el azul y el mismo tamaño de hoja.", "Dibujo líneas curvas en lugar de rectas."], "Líneas curvas en azul, del mismo tamaño de hoja"),
    ],
    [
        m("Cambiar color, tamaño y línea a la vez entre la prueba 1 y la prueba 2.", "No se sabe cuál cambio produjo el efecto.", "Cambia solo una variable en cada comparación."),
        m("Dibujar la frase de manera literal, por ejemplo un reloj con ojos para «el tiempo vuela».", "La frase dice una idea y se pierde el efecto expresivo.", "Busca cómo se vería la sensación con color, línea, forma o material."),
    ],
    [
        ex("Traducir visualmente una idea es: A. llevarla a imágenes, formas, colores o materiales B. copiar una frase con letras bonitas.", "A", "Es buscar cómo se vería lo que la idea quiere decir."),
        ex("Tienes la prueba 1 con un dibujo sobre papel liso y la prueba 2 con el mismo dibujo, del mismo tamaño, sobre papel de caja arrugado. ¿Qué variable cambió: la textura o la línea?", "La textura", "Solo cambió la superficie, de lisa a arrugada; la línea y el tamaño son los mismos."),
        ex("Una prueba que no resultó, ¿se anota o se borra de la bitácora?", "Se anota", "También enseña qué efecto no ayuda a la idea."),
    ],
    [
        ex("La frase «el viento se lleva los problemas» se traduce con líneas diagonales largas y formas pequeñas que salen de la hoja. ¿Qué tipo de línea usa para mostrar el viento: diagonales largas o puntos?", "Diagonales largas", "Las diagonales largas dan sensación de movimiento."),
        ex("Quieres mostrar «silencio» y haces dos pruebas. A. un fondo gris claro casi vacío con una figura pequeña B. colores fuertes y mucha mezcla de líneas. ¿Cuál se acerca más?", "A", "Poco contenido y colores suaves se sienten silenciosos."),
        ex("Una compañera cambia a la vez el color, la forma y el tamaño entre sus dos pruebas y dice que la segunda comunica mejor. ¿Puede saber qué cambio ayudó?", "No", "Al cambiar tres cosas juntas no se puede saber cuál produjo el efecto."),
    ],
    [
        ex("Para traducir «mi barrio por la mañana» tienes retazos de papel anaranjado, azul y gris. Haces la prueba 1 con anaranjado y azul y la prueba 2 con puro gris. Tu idea es mostrar un barrio que despierta con luz. ¿Qué prueba eliges?", "La prueba 1", "El anaranjado y el azul sugieren luz de amanecer; el gris solo no."),
        ex("Quieres comparar el tamaño de una figura. Prueba 1: figura de 2 cm en una hoja grande. Prueba 2: la misma figura de 15 cm. Si tu idea es «sentirse pequeño en un lugar enorme», ¿qué prueba sirve?", "La prueba 1", "La figura pequeña en un espacio grande transmite lo pequeño que se siente."),
        arith("Cortas 4 tiras de papel para la prueba 1 y 3 tiras más para la prueba 2. ¿Cuántas tiras cortaste en total?", "4+3", "Se suman las tiras de ambas pruebas."),
    ],
    [
        ex("Tu idea es «el apuro de la mañana». En la prueba A usas líneas rectas, rojas y muy juntas. En la prueba B usas círculos azules separados. Si eliges A, ¿qué explicación es mejor? A. «Elegí A porque las líneas rectas y juntas dan sensación de prisa» B. «Elegí A porque me gusta el rojo».", "A", "La A relaciona lo que se ve con la idea; la B solo da una preferencia."),
        ex("Dos estudiantes traducen «la lluvia». Una dibuja gotas realistas, la otra usa manchas largas azules y grises que bajan por la hoja. Ambas respetan su idea. ¿Cuál se mueve más allá de dibujar la frase literal?", "La segunda", "Las manchas largas traducen la sensación de lluvia sin dibujarla literalmente."),
    ],
    [
        ex("Quieres traducir «desorden creativo» con retazos. Prueba 1: los pegas en una cuadrícula perfecta. Prueba 2: los pegas en distintas direcciones, superpuestos. ¿Cuál comunica mejor la idea?", "La prueba 2", "Las direcciones distintas y las superposiciones sugieren desorden."),
        ex("Tienes 12 retazos. Usas 5 en la prueba 1 y el resto en la prueba 2. ¿Cuántos usas en la prueba 2?", "7", "Se restan los 5 usados de los 12: 12 − 5 = 7."),
    ],
    ex("Debes traducir la palabra «tormenta» con tres retazos: uno gris oscuro, uno amarillo brillante y uno azul. ¿Cuál traduce mejor la idea de tormenta? A. pegar el amarillo en forma de rayo cortado sobre el gris B. pegar el azul liso y centrado", "A", "El rayo amarillo sobre fondo oscuro sugiere el relámpago en una tormenta."),
    [
        ex("En Artes Visuales, ¿qué es una variable visual?", "Una decisión que se puede cambiar para ver su efecto", "Color, línea, forma, textura, tamaño o material son ejemplos."),
        ex("¿Cuántas variables conviene cambiar entre dos pruebas para compararlas?", "Una", "Así se ve qué cambio produjo el efecto."),
        ex("Verdadero o falso: traducir visualmente es dibujar la frase tal cual.", "Falso", "Es buscar cómo se vería lo que la frase quiere decir."),
    ],
    task(
        "Elige UNA frase. A) «El barrio despierta». B) «La ciudad nunca duerme». C) «El silencio también ocupa lugar». Haz dos pruebas pequeñas en una hoja (papel, lápices o retazos): cambia SOLO una variable entre ellas. Anota qué variable cambiaste, cuál prueba eliges y por qué.",
        "Elegí la A. Prueba 1: líneas rectas anaranjadas que salen de abajo. Prueba 2: las mismas líneas, pero curvas. Cambié solo la forma de la línea. Elijo la 2 porque las curvas parecen una luz que se abre, como cuando amanece.",
        ["hace dos pruebas distintas", "cambia solo una variable", "elige una prueba", "explica la elección con lo que se ve"],
        ["dos pruebas en la hoja", "explicación de la elección"],
        ["cambiar muchas variables a la vez", "explicar solo con «me gusta»"],
        "Destaca la variable que cambió y pregunta qué efecto vio entre las dos pruebas.",
    ),
    "Mira dos objetos de tu casa con la misma forma pero textura distinta y di qué sensación te da cada uno.",
    "Elige una palabra (por ejemplo «frío») y haz tres pruebas pequeñas cambiando una variable distinta en cada una; di cuál es más expresiva.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA1, 4,
    "Una hoja grande, lápiz de mina, lápices de colores o témpera y materiales reutilizables limpios (cartón, papel de diario, retazos de tela). Las situaciones que se mencionan están escritas en esta clase.",
    "Aprenderé a crear una propuesta propia a partir de una manifestación sobre diversidad cultural, género o un ícono, cuidando no caer en estereotipos ni copiar. Sirve para planificar mi obra con intención, boceto y materiales.",
    ["Sé traducir una idea con dos pruebas.", "Sé explicar una elección con un detalle que se ve."],
    [
        "Una propuesta propia tiene cuatro partes: una intención (qué quiero comunicar, cómo y por qué), un boceto (dibujo previo y rápido), una lista de materiales y una decisión sobre cómo mostrar a las personas o los símbolos. Parto de una manifestación que observé, pero la transformo con mi punto de vista. Un referente me inspira; no se copia. Si copio la forma exacta, la obra deja de ser mía.",
        "La diversidad cultural es la presencia de muchas culturas, con sus costumbres, oficios y formas de vestir. Para representarla con respeto, evito mostrar a un grupo con un solo rasgo, como un traje o una comida, y pregunto de dónde viene lo que dibujo. Si no conozco algo, dibujo lo que conozco o consulto a una persona adulta. Con el género hago lo mismo: puedo mostrar a mujeres y hombres haciendo toda clase de tareas, sin reglas fijas sobre qué les corresponde.",
        "Un ícono social, como una bandera, un uniforme o un monumento, se puede reinterpretar: lo cambio de color, tamaño o material para decir algo nuevo. Así creo una obra propia sin burlarme de nadie. Antes de ejecutar, reviso mi propuesta con tres preguntas: ¿mi idea se ve en el boceto?, ¿evito estereotipos y copias?, ¿puedo hacerla con los materiales que tengo?",
    ],
    [("propuesta", "plan de una obra con intención, boceto y materiales"), ("boceto", "dibujo previo y rápido para probar ideas"), ("diversidad cultural", "presencia de muchas culturas con costumbres y formas distintas"), ("reinterpretar", "cambiar algo conocido para decir una idea nueva"), ("referente", "obra o imagen que inspira, sin copiarse")],
    [
        w("Reinterpretar un ícono", "Quieres usar una bandera de club deportivo (franjas verdes y blancas) para hablar de la amistad entre hinchas rivales. Escribe una decisión propia.", ["No copio la bandera: la uso como referente.", "Cambio una variable: pinto franjas mezcladas, verdes y rojas, entrelazadas.", "La mezcla de colores dice que dos grupos pueden compartir."], "Franjas verdes y rojas entrelazadas, para hablar de amistad entre grupos"),
        w("Revisar con tres preguntas", "Tu propuesta: dibujar a una mujer cocinando y a un hombre mirándola, «porque así son las familias». Revísala.", ["¿La idea se ve? Sí, pero se apoya en una regla fija.", "¿Evita estereotipos? No, porque reparte tareas por género.", "Cambio: ambos cocinan juntos y dividen las tareas."], "Cambiar el boceto para que ambos cocinen y eliminar la regla fija sobre las familias"),
    ],
    [
        m("Mostrar a un grupo con un solo rasgo, como un traje, para que «se note» su cultura.", "Reduce un grupo a un símbolo y repite un estereotipo.", "Muestra personas haciendo cosas distintas y consulta lo que no conoces."),
        m("Copiar el boceto o el ícono tal cual y cambiarle apenas el color.", "La idea sigue siendo la del referente, no la propia.", "Cambia una decisión importante y explica la intención nueva."),
    ],
    [
        ex("Una propuesta propia tiene intención, boceto, materiales y una decisión sobre cómo mostrar a las personas o los símbolos. ¿Cuántas partes son en total?", "Cuatro", "Se cuentan: intención, boceto, materiales y la decisión sobre personas o símbolos."),
        ex("Un referente sirve para: A. inspirar tu obra con una idea propia B. copiarlo exactamente para ahorrar tiempo.", "A", "Un referente inspira, no se copia."),
        ex("En Artes Visuales, ¿qué es un boceto?", "Un dibujo previo y rápido para probar ideas", "Sirve para decidir antes de hacer la obra final."),
    ],
    [
        ex("Quieres mostrar la diversidad cultural de un curso con cuatro estudiantes que traen distintas costumbres. ¿Qué propuesta evita el estereotipo? A. Dibujarlos conversando y compartiendo cosas distintas que traen de sus casas B. Dibujar a cada uno con un traje típico distinto, de pie y sin hacer nada.", "A", "La A muestra personas haciendo cosas, no reducidas a un símbolo."),
        ex("Tu intención es «agradecer el trabajo de los bomberos». ¿Qué boceto lo muestra mejor? A. Un uniforme de bombero grande al centro, con personas sonriendo alrededor B. Un uniforme pequeño en una esquina, con el resto de la hoja vacía.", "A", "El tamaño grande y las personas sonriendo destacan y agradecen su trabajo."),
        ex("Reinterpretas un monumento de piedra en cartón pintado de colores vivos para hablar de la alegría. ¿Qué variable cambiaste: material o color?", "Ambos", "Cambiaste de piedra a cartón y de tonos de piedra a colores vivos."),
    ],
    [
        ex("Quieres mostrar a una mujer y a un hombre en el mismo oficio de constructores, sin que uno parezca ayudante del otro. ¿Qué decisión de tamaño usas: figuras del mismo tamaño con herramientas similares o una figura mucho más grande?", "Figuras del mismo tamaño con herramientas similares", "El mismo tamaño y herramientas muestran igual importancia."),
        ex("Tienes cartón, dos retazos de tela y papel de diario. Quieres hacer una escultura de un ícono con tres materiales. ¿Alcanza con esos materiales?", "Sí", "Son cartón, tela y papel de diario: tres materiales."),
        arith("Tu boceto tiene 6 personas dibujadas y quieres sumar 2 más en el fondo. ¿Cuántas personas tendrá el boceto?", "6+2", "Se suman las personas nuevas a las que ya había."),
    ],
    [
        ex("Una compañera quiere pintar a un grupo de personas de otra cultura vistiendo solo su ropa tradicional de fiesta, porque «así se las reconoce». ¿Qué le recomiendas? A. Mostrar a las personas también haciendo cosas cotidianas, no solo su ropa de fiesta B. Dibujar todavía más ropa de fiesta.", "A", "Mostrar actividades variadas evita reducir una cultura a un solo rasgo."),
        ex("Dos propuestas reinterpretan la misma bandera. La primera la copia y le cambia el borde. La segunda cambia los colores y los entrelaza para hablar de unión. ¿Cuál es más propia?", "La segunda", "Cambia una decisión importante y comunica una idea nueva."),
    ],
    [
        ex("Tu boceto muestra solo a hombres en un taller y solo a mujeres en una cocina. ¿Qué cambio evita el estereotipo de género? A. Mostrar mujeres y hombres en ambos lugares B. Poner la cocina más grande.", "A", "Así no se asigna un lugar o tarea según el género."),
        ex("Copiaste casi entero un afiche que viste y solo cambiaste los colores. Para que sea más propio, ¿qué cambio añades? A. Ordenar las figuras de otra manera y decir qué idea nueva muestra B. Cambiar el color otra vez.", "A", "Cambiar la composición y explicar la idea nueva vuelve la obra propia."),
    ],
    ex("Quieres hacer un ícono con retazos y tu lista dice: cartón, retazos de tela y papel de diario. Llegas a casa y no tienes cartón. ¿Qué haces con la propuesta? A. Cambias el soporte por una caja o papel grueso y mantienes la idea B. Abandonas la idea.", "A", "Un soporte parecido permite mantener la intención con otros materiales."),
    [
        ex("¿Qué tres preguntas se hacen al revisar una propuesta?", "Si se ve la idea, si evita estereotipos y copias, y si se puede hacer", "Revisan intención, respeto y viabilidad."),
        ex("Verdadero o falso: un ícono social no puede reinterpretarse.", "Falso", "Se puede cambiar su color, tamaño o material para decir algo nuevo."),
        ex("¿Qué se hace cuando no conoces algo de otra cultura que quieres representar?", "Se dibuja lo que se conoce o se consulta a una persona adulta", "Evita inventar datos o mostrar a un grupo con un solo rasgo."),
    ],
    task(
        "Elige UNA opción para tu propuesta. A) Reinterpretar una bandera de club (franjas verdes y blancas) para hablar de amistad. B) Mostrar el trabajo de cuatro oficios (panadero, bombera, profesor, constructora) sin estereotipos de género. C) Mostrar la diversidad de un curso donde cada estudiante trae una costumbre distinta a la mesa. Haz un boceto, escribe tu intención (qué, cómo, por qué), la lista de materiales y una decisión para no caer en estereotipos.",
        "Elegí la B. Boceto: cuatro personas con herramientas de su oficio, del mismo tamaño y en un círculo. Intención: quiero mostrar que cualquier persona puede tener cualquier oficio, con figuras del mismo tamaño y colores cálidos, porque todos los oficios importan. Materiales: cartón, retazos y lápices. Decisión: cada oficio lo hace alguien distinto de lo que se espera.",
        ["hace un boceto", "escribe intención con qué, cómo y por qué", "lista materiales viables", "explica una decisión para evitar estereotipos o copia"],
        ["boceto", "intención escrita", "lista de materiales"],
        ["copiar el referente", "mostrar a un grupo con un solo rasgo"],
        "Destaca la decisión que evita el estereotipo y pregunta qué cambiaría si tuviera que usar un solo material.",
    ),
    "Mira un uniforme o un ícono de tu entorno y di en voz alta una forma de cambiarlo para decir una idea nueva.",
    "Reinterpreta el mismo ícono de dos maneras (una con otro color y otra con otro material) y explica qué mensaje distinto transmite cada una.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA1, 5,
    "Una hoja, lápiz y el boceto o la prueba de la clase anterior (o el ejemplo escrito en esta clase). Se puede trabajar sin materiales especiales.",
    "Aprenderé a explicar las decisiones de mi obra con una ficha breve y a revisarla con un comentario sin perder mi voz. Sirve para mostrar que mi trabajo fue pensado y que puedo mejorarlo.",
    ["Sé escribir una intención con qué, cómo y por qué.", "Sé que un comentario ayuda, pero la decisión final es de quien crea."],
    [
        "Una ficha de obra explica mi trabajo en pocas líneas. Incluye el título, los materiales, la intención y dos decisiones visuales con su efecto. Por ejemplo: «Usé líneas curvas porque se ven suaves y cercanas». Si cito un referente, escribo cuál fue y qué cambié. Cuando la ficha dice qué decidí y por qué, quien mira entiende mi obra sin que yo esté al lado.",
        "Revisar es mirar mi obra otra vez con un criterio. Mis criterios son: ¿se nota mi intención?, ¿lo que muestro evita estereotipos?, ¿es propia y no una copia?, ¿los materiales ayudan? Con eso puedo detectar qué cambiar. Un comentario de otra persona me da información, pero yo decido si lo incorporo. Si lo hago, lo anoto: «Cambié el fondo porque mi compañera dijo que no se veía el personaje».",
        "Una buena revisión conserva la voz propia: no borro mi idea para hacer lo que otros esperan. Cambio una decisión a la vez y anoto qué efecto tuvo. Al final comparo la versión inicial con la revisada y escribo qué mejoró. Esto sirve en todas las obras, sean dibujos, esculturas o fotografías. El contraste es la diferencia clara entre dos cosas, como un personaje claro sobre un fondo oscuro.",
    ],
    [("ficha de obra", "texto breve que explica título, materiales, intención y decisiones"), ("criterio", "regla para juzgar si algo cumple su propósito"), ("revisar", "mirar de nuevo la obra para decidir qué cambiar"), ("retroalimentación", "comentario que ayuda a mejorar"), ("voz propia", "manera personal de decir una idea, que no se pierde al cambiar")],
    [
        w("Escribir la ficha", "Hiciste un collage con retazos azules y un solo retazo rojo sobre una calle gris para hablar de una persona que cuida su barrio. Escribe dos líneas de ficha.", ["Intención: mostrar a quien cuida el barrio.", "Decisión 1: un solo retazo rojo, para que se note entre lo gris.", "Efecto: el rojo llama la atención al centro."], "Título del collage, materiales y: «Usé un solo retazo rojo para destacar a quien cuida el barrio entre lo gris»"),
        w("Decidir un comentario", "Una compañera dice: «Pon el personaje más grande, no se ve». Tu intención era mostrar que se siente pequeño. ¿Qué haces?", ["Reviso mi criterio: ¿se nota mi intención?", "Si agrando el personaje, cambia el sentido de la obra.", "Puedo mejorar su visibilidad sin agrandarlo, por ejemplo con más contraste de color."], "Mantener el tamaño pequeño y aumentar el contraste de color del personaje"),
    ],
    [
        m("Cambiar toda la obra para seguir cada comentario que me dan.", "Se pierde la intención y la voz propia.", "Decide qué comentarios sirven a tu intención y anota por qué los usas o no."),
        m("Escribir una ficha con solo el título y «es mi obra».", "No dice las decisiones ni la intención.", "Agrega materiales, intención y dos decisiones con su efecto."),
    ],
    [
        ex("¿Cuál de estas partes NO pertenece a una ficha de obra? A. La intención B. El precio que le pondrías a la obra.", "B", "La ficha contiene título, materiales, intención y decisiones; el precio no explica la obra."),
        ex("Una persona mira tu obra y dice que le gustó. ¿Es una retroalimentación útil para mejorar? A. Sí, porque dice qué cambiar B. No, porque no dice qué decisión funciona ni qué cambiar.", "B", "Para mejorar necesito un comentario que se refiera a un criterio."),
        ex("Si decides no cambiar algo que te sugirieron, ¿pierdes tu voz propia?", "No", "La decisión final es de quien crea."),
    ],
    [
        ex("Tu ficha dice: «Usé líneas curvas porque se ven suaves y cercanas». ¿Esa frase explica una decisión y su efecto?", "Sí", "Dice qué usaste y qué efecto produce."),
        ex("Un comentario dice: «El fondo tapa a tu personaje». Tu criterio es que se note la intención de destacar al personaje. ¿El comentario es útil? A. Sí, apunta a un problema con tu criterio B. No, no tiene relación con tu obra.", "A", "El fondo que tapa al personaje afecta tu intención."),
        ex("Haces la revisión cambiando el fondo y el tamaño del personaje al mismo tiempo. ¿Podrás saber cuál cambio mejoró la obra?", "No", "Al cambiar dos cosas juntas no se sabe cuál funcionó."),
    ],
    [
        ex("Tu obra tiene tres criterios: intención clara, evita estereotipos y es propia. Revisas y encuentras que cumple dos. ¿Cuántos criterios te faltan por cumplir?", "1", "De 3 criterios cumples 2; falta 3 − 2 = 1."),
        ex("Tu obra muestra solo hombres con casco en una construcción. Tu criterio es evitar estereotipos de género. ¿Qué cambio revisarías en la obra?", "Incluir también mujeres con casco en la construcción", "Así no se asocia el oficio solo a un género."),
        arith("Anotas 4 cambios en la revisión y cada uno te toma 5 minutos. ¿Cuántos minutos necesitas?", "4*5", "Se multiplican los cambios por el tiempo de cada uno."),
    ],
    [
        ex("Dos estudiantes recibieron el mismo comentario: «Hay poco contraste». Uno dibuja todo con negro. La otra solo oscurece el fondo y deja su personaje claro. ¿Quién conserva mejor su intención de destacar al personaje?", "La segunda", "El personaje claro contra un fondo oscuro mantiene su protagonismo."),
        ex("Tu ficha final dice «copié un mural pero cambié el color». Si tu criterio es que la obra sea propia, ¿cumple?", "No", "Copiar con un cambio mínimo no es una obra propia."),
    ],
    [
        ex("Escribe en una frase qué cambio te parece mejor tras este comentario: «Los colores se mezclan y no se nota el centro». A. Separar el centro con un borde más claro B. Pintar toda la obra de un solo color.", "A", "Un borde claro destaca el centro sin perder la idea de los colores."),
        ex("Comparas tu versión inicial y la revisada. En la inicial no se veía el personaje; en la revisada sí. ¿Qué criterio mejoró?", "Que se note la intención", "Ahora se ve al personaje, que era el centro de la idea."),
    ],
    ex("Tu compañero te muestra una ficha: «Título: Mi barrio. Materiales: cartón. Intención: mostrar mi barrio». ¿Qué le falta para que tenga dos decisiones con su efecto? A. Una frase como «Usé azul para que se vea tranquilo» B. Un segundo título.", "A", "Falta explicar decisiones visuales y su efecto."),
    [
        ex("¿Qué incluye una ficha de obra?", "Título, materiales, intención y decisiones con su efecto", "Con eso se entiende la obra sin que su autor esté presente."),
        ex("Verdadero o falso: debo cambiar mi obra según todos los comentarios.", "Falso", "Decido qué comentarios sirven a mi intención."),
        ex("¿Cuántas decisiones conviene cambiar a la vez al revisar?", "Una", "Así se ve qué efecto tuvo cada cambio."),
    ],
    task(
        "Elige UNA obra para explicar. A) Un collage con retazos azules y un solo retazo rojo sobre una calle gris. B) Un dibujo de dos personas del mismo tamaño que comparten un oficio. C) Una reinterpretación de una bandera con franjas verdes y rojas entrelazadas. Escribe su ficha (título, materiales, intención, dos decisiones con su efecto) y revisa con este comentario: «No se entiende cuál es el centro». Anota qué cambiaste y qué mantuviste.",
        "Elegí la A. Título: «El que cuida». Materiales: retazos y papel. Intención: mostrar a quien cuida el barrio. Decisiones: un solo retazo rojo para destacarlo; fondo gris para que contraste. Revisión: agrandé un poco el retazo rojo y mantuve el fondo gris, porque sigue mostrando que cuida un barrio apagado.",
        ["escribe título, materiales e intención", "explica dos decisiones con su efecto", "toma un comentario y decide qué cambiar", "conserva su idea propia"],
        ["ficha escrita", "registro de la revisión"],
        ["seguir el comentario y perder la idea", "no explicar el efecto"],
        "Señala la decisión mejor explicada y pregunta qué mantuvo y por qué.",
    ),
    "Cuenta a una persona de tu casa qué idea quieres mostrar en una obra y escucha una sugerencia; di si la usarías o no, y por qué.",
    "Escribe una segunda ficha para la misma obra pero con otra intención, y explica qué decisión visual cambiarías.",
)
