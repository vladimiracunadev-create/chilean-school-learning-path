"""Cuaderno del estudiante de 1.º básico Artes Visuales, AR01 OA 03 (materiales, herramientas y procedimientos)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA3 = "AR01 OA 03"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- Clase 1
register(
    OA3, 1,
    materials="Una hoja, lápiz de mina, lápiz de cera, témpera o acuarela y agua, papel de diario, un trozo de lana o hilo, masa o plasticina. Si falta alguno, usa solo los que tengas.",
    use="Aprenderé a probar materiales y a descubrir qué pueden hacer y qué no. Sirve para elegir el material que mejor expresa lo que quiero mostrar.",
    prior=["Sé dibujar y pintar de manera simple.", "Sé cuidar los materiales."],
    explain=[
        "Un material es aquello con lo que haces una obra: lápiz, pintura, papel, lana, masa o tapas recicladas. Cada material tiene posibilidades, es decir, cosas que puede hacer bien, y límites, cosas que no puede hacer o le salen difícil.",
        "Con un lápiz de cera puedes hacer líneas gruesas y colores fuertes, pero es difícil dibujar detalles muy finos. La témpera cubre mucho y se puede usar espesa o con agua, pero se mancha si la tocas húmeda. El papel de diario se puede rasgar con borde irregular o cortar con borde recto.",
        "Un laboratorio de materiales es probar cada material en un cuadrito de la hoja y anotar qué descubriste. Una prueba muy interesante es la resistencia: si pintas con lápiz de cera y luego pasas témpera con agua encima, la cera rechaza el agua y el dibujo aparece.",
    ],
    vocab=[("material", "lo que se usa para hacer una obra"), ("posibilidad", "algo que el material puede hacer"), ("límite", "algo que al material le cuesta o no puede hacer"), ("laboratorio", "lugar o momento para probar y descubrir"), ("resistencia", "técnica donde la cera rechaza el agua de la pintura")],
    worked=[
        {"title": "Probar el papel de diario", "problem": "Rasgas un papel de diario con las manos y luego lo cortas con tijera. ¿Qué diferencia hay en el borde?", "steps": ["Al rasgar con las manos el borde queda irregular y desflecado.", "Al cortar con tijera el borde queda recto y limpio."], "answer": "Rasgado: borde irregular; cortado: borde recto"},
        {"title": "La prueba de resistencia", "problem": "Dibujas una estrella con lápiz de cera blanca y pasas témpera azul diluida encima. ¿Qué pasa?", "steps": ["La cera rechaza el agua de la pintura.", "La témpera azul cubre el papel, pero no donde está la cera.", "La estrella blanca aparece sobre el fondo azul."], "answer": "La estrella blanca queda visible sobre el azul"},
    ],
    mistakes=[
        {"wrong": "Decir que un material es malo porque no sirve para todo.", "why": "Cada material tiene límites y posibilidades distintas.", "fix": "Pregunta para qué sirve mejor y qué efecto logra."},
        {"wrong": "Probar sin anotar lo que pasó.", "why": "Se olvida el descubrimiento.", "fix": "Escribe una frase corta junto a cada prueba."},
    ],
    tiers={
        "recovery": [
            ex("¿El lápiz de cera hace líneas gruesas o muy finas con facilidad?", "Gruesas", "Su punta es ancha y blanda."),
            ex("Un papel rasgado a mano, ¿tiene borde recto o irregular?", "Irregular", "Las fibras se desgarran sin orden."),
            ex("La lana, ¿sirve para hacer una línea o para hacer un detalle muy chiquito?", "Una línea", "Es un hilo largo y grueso."),
        ],
        "understand": [
            ex("¿Qué es un límite de un material? A: algo que le cuesta o no puede hacer. B: su precio. C: su color.", "A", "Un límite es una dificultad propia del material."),
            ex("¿Qué es una posibilidad de un material? A: algo que hace bien. B: algo que ensucia.", "A", "Posibilidad es una acción que puede lograr."),
            ex("¿Qué ocurre en la técnica de resistencia con cera y témpera?", "La cera rechaza el agua y el dibujo aparece", "La cera no deja pasar la pintura húmeda."),
        ],
        "apply": [
            ex("Quieres hacer una línea gruesa y de color fuerte. ¿Qué material eliges: lápiz de cera o lápiz de mina fino?", "Lápiz de cera", "Marca un trazo ancho y de color vivo."),
            ex("Quieres un borde recto para una casa de papel. ¿Rasgas o cortas?", "Cortas", "La tijera deja bordes rectos."),
            arith("En tu laboratorio pruebas 4 materiales y haces 2 cuadritos con cada uno. ¿Cuántos cuadritos haces?", "2 + 2 + 2 + 2", "Son cuatro materiales con dos cuadritos cada uno: se suma 2 cuatro veces."),
        ],
        "reason": [
            ex("Mario quiso dibujar las pestañas de un ojo con témpera espesa y pincel grueso. Le quedó un manchón. ¿Qué herramienta le conviene usar para las pestañas: un pincel fino o uno más grueso?", "Un pincel fino", "Las pestañas son líneas delgadas y un pincel fino las puede hacer."),
            ex("Bea dice: «La plasticina es mala porque no se puede dibujar con ella». ¿Qué le explicas?", "Que sirve para modelar y no para dibujar", "Cada material sirve mejor para algo distinto."),
        ],
        "challenge": [
            arith("Una tabla de laboratorio tiene 3 materiales de dibujo, 2 de modelado y 3 reciclados. ¿Cuántos materiales hay?", "3 + 2 + 3", "Se suman los tres grupos."),
            ex("Escribe una posibilidad y un límite de la témpera.", "Posibilidad: cubre mucho; límite: se mancha húmeda", "Se nombra una ventaja y una dificultad de la pintura."),
        ],
    },
    context=[ex("En tu casa tienes tapas de botella, cartón de caja y lana. Quieres hacer un rostro: ¿qué material sirve para los ojos redondos y cuál para el pelo?", "Tapas para los ojos y lana para el pelo", "Las tapas son redondas y la lana parece cabello.")],
    selfcheck=[
        ex("¿Dónde pruebas un material antes de usarlo en tu obra: en un cuadrito de ensayo o en la obra final?", "En un cuadrito de ensayo", "Las pruebas se hacen aparte."),
        ex("¿Qué material deja un borde irregular al rasgarlo?", "El papel", "El papel se desgarra con borde sin orden."),
        ex("¿Qué es un laboratorio de materiales?", "Un lugar para probar materiales", "Se experimenta con lo que cada uno hace."),
    ],
    open_task=task(
        "Haz una hoja de pruebas con seis cuadritos del tamaño de una tarjeta. Prueba en cada uno un material de esta lista y escribe debajo una frase corta: (1) lápiz de mina, (2) lápiz de cera, (3) témpera, (4) papel de diario rasgado, (5) lana pegada, (6) resistencia con cera y témpera con agua.",
        "Cuadro 2: lápiz de cera, líneas gruesas y colores fuertes. Cuadro 6: la estrella de cera queda blanca bajo la témpera azul.",
        ["prueba al menos cuatro materiales", "anota un descubrimiento por prueba", "reconoce una posibilidad y un límite"],
        ["hoja de pruebas con cuadritos", "frases breves de descubrimiento"],
        ["probar sin anotar", "usar el mismo material en todos los cuadros"],
        "Reconoce el orden de la hoja de pruebas y pide precisar un límite que descubrió.",
    ),
    reinforce="Prueba con lápiz de cera y agua si el dibujo aparece, en un cuadrito pequeño.",
    extend="Elige dos materiales de la lista y combínalos en una prueba nueva; anota qué efecto sorpresivo apareció.",
)

# ---------------------------------------------------------------- Clase 2
register(
    OA3, 2,
    materials="Pincel, tijera de punta redondeada, pegamento en barra, un palito de helado como esteca, masa o plasticina, hojas de papel y, si hay, un computador o tableta con un programa de dibujo sencillo.",
    use="Aprenderé a usar herramientas para dibujar, pintar, cortar, unir y modelar, y a cuidarme al hacerlo. Sirve para trabajar con seguridad y con buenos resultados.",
    prior=["Sé tomar objetos con las dos manos.", "Sé seguir indicaciones de seguridad."],
    explain=[
        "Una herramienta es un objeto que ayuda a trabajar el material. Con el pincel pintas, con la tijera cortas, con el pegamento unes, con la esteca modelas una masa y con el computador puedes dibujar en una pantalla. Cada herramienta tiene su uso.",
        "Para trabajar con seguridad: te sientas para cortar; usas tijera de punta redondeada; cortas solo papel o cartulina; pasas la tijera tomándola por la punta cerrada, con el mango hacia la otra persona; no pruebas ni llevas materiales a la boca; y te lavas las manos al terminar.",
        "También se cuida la herramienta: el pincel se lava con agua y se deja con la punta hacia arriba, el pegamento se cierra al terminar y el computador se usa con las manos limpias y se guarda el trabajo antes de apagar.",
    ],
    vocab=[("herramienta", "objeto que ayuda a trabajar un material"), ("pincel", "herramienta para pintar con pintura líquida"), ("tijera", "herramienta para cortar papel"), ("esteca", "palito para modelar y dar forma a la masa"), ("seguridad", "cuidarme para no hacerme daño ni dañar a otros")],
    worked=[
        {"title": "Elegir la herramienta", "problem": "Quieres cortar una forma de papel. ¿Qué herramienta usas y cómo la pasas a un compañero?", "steps": ["Para cortar uso la tijera de punta redondeada.", "Para pasarla la tomo por la punta cerrada.", "El mango queda hacia mi compañero."], "answer": "Tijera; se pasa con el mango hacia el otro"},
        {"title": "Modelar con esteca", "problem": "Tienes una bolita de masa y quieres hacer los dientes de un dinosaurio. ¿Qué haces?", "steps": ["Aplasto un trozo de masa.", "Con la esteca marco pequeñas líneas o cortes.", "Obtengo dientes con forma."], "answer": "Usar la esteca para marcar los dientes"},
    ],
    mistakes=[
        {"wrong": "Cortar de pie o caminando con la tijera abierta.", "why": "Puede pinchar o cortar a alguien si tropiezas.", "fix": "Siéntate, corta con calma y deja la tijera cerrada al caminar."},
        {"wrong": "Usar el pincel con la punta apoyada en el agua.", "why": "Se deforma y se estropea.", "fix": "Lava y deja el pincel con la punta hacia arriba."},
    ],
    tiers={
        "recovery": [
            ex("¿Con qué herramienta cortas papel: pincel o tijera?", "Tijera", "La tijera corta."),
            ex("¿Con qué herramienta pintas: pincel o esteca?", "Pincel", "El pincel aplica la pintura."),
            ex("¿Con qué herramienta unes dos papeles: pegamento o pincel?", "Pegamento", "El pegamento une."),
        ],
        "understand": [
            ex("¿Para qué sirve la esteca? A: para cortar cartón. B: para modelar masa. C: para borrar.", "B", "La esteca da forma a la masa."),
            ex("¿Cómo se pasa una tijera a otra persona? A: con el mango hacia ella. B: con las puntas hacia ella.", "A", "Así nadie se pincha."),
            ex("¿Qué se hace con el pincel al terminar de pintar?", "Se lava y se deja con la punta hacia arriba", "Se cuida para que no se deforme."),
        ],
        "apply": [
            ex("Une cada verbo con su herramienta: pintar, cortar, unir, modelar. Herramientas: tijera, pegamento, esteca, pincel. Escribe en orden las herramientas.", "Pincel, tijera, pegamento, esteca", "Cada verbo corresponde a la herramienta que hace esa acción."),
            ex("Quieres recortar un círculo de cartulina. ¿Qué tijera usas: de punta redondeada o una muy puntiaguda?", "De punta redondeada", "Es más segura para niños de tu edad."),
            arith("Tienes 3 pinceles en un vaso y sacas 1 para usarlo. ¿Cuántos pinceles quedan en el vaso?", "3 - 1", "Se resta el que sacaste."),
        ],
        "reason": [
            ex("Pablo corta caminando por la sala con la tijera abierta. ¿Está trabajando con seguridad?", "No", "Podría lastimarse o lastimar a otro."),
            ex("Una compañera dice que probó un poco de témpera con la lengua para ver cómo sabía. ¿Qué debes decirle?", "Que no se lleva la pintura a la boca", "La seguridad indica no probar materiales."),
        ],
        "challenge": [
            ex("Quieres hacer un dibujo en el computador. Ordena: A guardar el trabajo, B dibujar con el programa, C abrir el programa de dibujo.", "C, B, A", "Se abre, se dibuja y se guarda."),
            arith("Para una maqueta cortas 4 tiras de cartulina y de cada una sacas 3 cuadrados. ¿Cuántos cuadrados cortaste?", "3 + 3 + 3 + 3", "Son cuatro tiras con tres cuadrados cada una: se suma 3 cuatro veces."),
        ],
    },
    context=[ex("Vas a hacer una máscara de cartulina: cortas los ojos, pintas las mejillas y pegas lana como pelo. Nombra las tres herramientas que usas.", "Tijera, pincel y pegamento", "Cortar, pintar y unir usan esas tres herramientas.")],
    selfcheck=[
        ex("¿Qué herramienta modela masa?", "La esteca", "Con ella se marcan formas."),
        ex("Para cortar, ¿te quedas sentado o caminas por la sala con la tijera?", "Me quedo sentado", "Se corta sentado para no hacerse daño ni dañar a otros."),
        ex("¿Qué haces con las manos al terminar de trabajar?", "Me las lavo", "Se limpian restos de pintura y pegamento."),
    ],
    open_task=task(
        "Con ayuda de un adulto, haz un pequeño trabajo que use cuatro herramientas: corta tres formas de cartulina con la tijera, pégalas sobre una hoja con pegamento en barra, pinta detalles con un pincel y modela una bolita de masa que pegues como adorno. Escribe una lista: «Usé… para… y me cuidé de…».",
        "Usé la tijera para cortar un triángulo, un cuadrado y un círculo. Usé el pegamento para unirlos. Me cuidé de cortar sentado.",
        ["usa cuatro herramientas", "nombra qué hizo con cada una", "cumple una regla de seguridad"],
        ["pequeño trabajo", "lista de herramientas y usos"],
        ["cortar de pie", "no nombrar un cuidado"],
        "Reconoce el cuidado y el uso correcto de las herramientas y pide detallar cómo guardó cada una.",
    ),
    reinforce="Con un adulto, practica pasar una tijera de modo seguro y cortar tiras de papel de diario.",
    extend="Haz un cartel con tres reglas de seguridad para usar herramientas en casa.",
)

# ---------------------------------------------------------------- Clase 3
register(
    OA3, 3,
    materials="Lápiz de cera, lana, papel de diario, plasticina o masa, témpera y una hoja. Las emociones y sus propuestas están escritas en el cuaderno.",
    use="Aprenderé a expresar una misma emoción con materiales distintos y a comparar qué efecto logra cada uno. Sirve para elegir el material que mejor muestra lo que siento.",
    prior=["Conozco emociones como alegría, calma, enojo y miedo.", "Sé que los materiales tienen posibilidades y límites."],
    explain=[
        "Los materiales también expresan emociones. Una línea gruesa de cera con rojo fuerte puede mostrar enojo. Un hilo de lana suave puede mostrar calma. Papel rasgado en trozos pequeños puede mostrar nervios. Una masa blanda puede mostrar ternura.",
        "Una misma emoción se puede mostrar con materiales distintos. La alegría se puede hacer con pinceladas rápidas y amarillas, o con papelitos de colores pegados como confeti. Las dos obras muestran alegría, pero se sienten distintas.",
        "Para elegir, comparas: pruebas la emoción con dos materiales, miras el efecto y decides cuál lo expresa mejor. Siempre explicas con algo que se ve: «El papel rasgado muestra enojo porque sus bordes son irregulares y bruscos».",
    ],
    vocab=[("emoción", "lo que siento por dentro, como alegría o miedo"), ("expresar", "mostrar lo que siento o pienso"), ("materialidad", "el material que se eligió para una obra"), ("efecto", "lo que se logra con un material, como suavidad o fuerza"), ("comparar", "mirar en qué se parecen y en qué se diferencian dos pruebas")],
    worked=[
        {"title": "Dos materiales para la calma", "problem": "Quieres expresar calma. Pruebas lana en curvas suaves y papel rasgado en trozos pequeños. ¿Cuál expresa mejor la calma?", "steps": ["La lana en curvas suaves forma líneas largas y tranquilas.", "El papel rasgado en trozos pequeños tiene bordes bruscos y mucho movimiento.", "La lana se parece más a la calma."], "answer": "La lana en curvas suaves"},
        {"title": "Explicar la elección", "problem": "Eliges cera roja gruesa para el enojo. ¿Qué frase escribes?", "steps": ["Nombro el material: cera roja gruesa.", "Nombro lo que se ve: líneas fuertes y rojas.", "Escribo: elegí cera roja gruesa porque sus líneas fuertes muestran enojo."], "answer": "Elegí cera roja gruesa porque sus líneas fuertes muestran enojo"},
    ],
    mistakes=[
        {"wrong": "Pensar que cada emoción solo se puede hacer con un material.", "why": "Muchos materiales pueden expresar lo mismo con efectos distintos.", "fix": "Prueba dos materiales y compara."},
        {"wrong": "Explicar «la lana es calma» sin decir qué se ve.", "why": "No explica por qué la lana ayuda.", "fix": "Di qué se ve: «sus curvas suaves son tranquilas»."},
    ],
    tiers={
        "recovery": [
            ex("Líneas gruesas y rojas con cera, ¿expresan más enojo o más calma?", "Enojo", "La fuerza y el rojo transmiten tensión."),
            ex("Lana en curvas suaves, ¿expresa más calma o más enojo?", "Calma", "Las curvas suaves son tranquilas."),
            ex("Papelitos de colores pegados como confeti, ¿expresan más alegría o más tristeza?", "Alegría", "Los muchos colores recuerdan una fiesta."),
        ],
        "understand": [
            ex("¿Qué significa expresar una emoción en una obra? A: mostrarla con colores, líneas o materiales. B: escribir su nombre.", "A", "Expresar es hacerla visible en la obra."),
            ex("Dos obras muestran alegría: una con pinceladas amarillas y otra con papelitos. ¿Las dos expresan lo mismo con el mismo efecto?", "No, el efecto cambia", "Cada material da una sensación distinta."),
            ex("¿Qué debe nombrar una buena explicación? A: algo que se ve en la obra. B: el precio.", "A", "La razón se apoya en lo visible."),
        ],
        "apply": [
            ex("Quieres expresar ternura. ¿Qué material eliges: masa blanda y redondeada o papel rasgado con puntas?", "Masa blanda y redondeada", "La suavidad y las formas redondas transmiten ternura."),
            ex("Quieres expresar nervios. ¿Qué eliges: papel rasgado en trocitos o lana en una sola curva larga?", "Papel rasgado en trocitos", "Los bordes irregulares dan sensación de inquietud."),
            arith("Pegas 5 papelitos amarillos y 4 papelitos naranjos para mostrar alegría. ¿Cuántos papelitos pegaste?", "5 + 4", "Se suman ambos colores."),
        ],
        "reason": [
            ex("Mía usó lana azul en curvas suaves para el miedo y dijo que lo expresa bien. ¿La explicación nombra algo que se ve?", "No", "Habría que decir qué se ve que causa miedo."),
            ex("Compara: A cera negra en trazos fuertes y quebrados; B lana celeste en curvas largas. ¿Cuál se acerca más a la calma?", "B", "Las curvas largas y suaves son tranquilas."),
        ],
        "challenge": [
            ex("Escribe una frase con «porque» para explicar por qué usarías papel rasgado en una obra de enojo.", "Usaría papel rasgado porque sus bordes irregulares se ven bruscos", "La frase relaciona el borde con la emoción."),
            arith("En una obra de enojo usas 8 trozos de papel rojo y 6 de negro. ¿Cuántos trozos usas?", "8 + 6", "Se suman los dos colores."),
        ],
    },
    context=[ex("Quieres hacer una tarjeta de cumpleaños que muestre alegría. ¿Qué material eliges: confeti de papel de colores o lana gris?", "Confeti de papel de colores", "Los colores vivos y los muchos papelitos dan idea de fiesta.")],
    selfcheck=[
        ex("¿Qué emoción muestra mejor la lana en curvas suaves: calma o enojo?", "Calma", "Es suave y tranquila."),
        ex("¿Se puede expresar una emoción con más de un material?", "Sí", "Cada material da un efecto distinto."),
        ex("¿Qué haces antes de elegir el material: probar dos o elegir sin ver?", "Probar dos", "Se compara para decidir."),
    ],
    open_task=task(
        "Elige UNA emoción: (A) alegría; (B) calma; (C) enojo. Haz dos pruebas pequeñas con dos materiales distintos de esta lista: cera, lana, papel rasgado, masa, témpera. Elige la prueba que mejor muestre tu emoción y escribe: «Elegí… porque… se ve…».",
        "Elegí calma. Probé lana y papel rasgado. Elegí lana porque sus curvas suaves se ven tranquilas.",
        ["hace dos pruebas con materiales distintos", "elige una", "explica con algo que se ve"],
        ["dos pruebas pequeñas", "frase de elección"],
        ["usar el mismo material dos veces", "no explicar el efecto visual"],
        "Valora la comparación y pide nombrar con más precisión la característica visible del material.",
    ),
    reinforce="Con lana, forma en una mesa una curva suave y una línea quebrada y di qué emoción te da cada una.",
    extend="Elige otra emoción y pruébala con un tercer material de la lista; compara los tres.",
)

# ---------------------------------------------------------------- Clase 4
register(
    OA3, 4,
    materials="Papel de diario o revistas viejas, hoja de cartulina o cartón, pegamento en barra, tijera de punta redondeada, lápiz y lápices de colores. Los pasos están en el cuaderno.",
    use="Aprenderé a hacer una obra siguiendo los pasos de un procedimiento: el collage. Sirve para crear imágenes pegando papeles, aunque no sepa dibujar muy bien.",
    prior=["Sé rasgar y cortar papel.", "Sé usar pegamento con cuidado."],
    explain=[
        "Un procedimiento es un conjunto de pasos ordenados para hacer una obra. El collage es un procedimiento donde pegas pedazos de papel u otros materiales sobre una superficie para formar una imagen. Henri Matisse, un artista francés, hizo en 1953 una obra llamada El caracol con papeles pintados y recortados que forman una espiral de colores.",
        "Pasos del collage: 1. Planifica con un boceto qué quieres mostrar. 2. Rasga o corta los papeles que necesitas. 3. Ordénalos en la hoja sin pegar y mira cómo quedan. 4. Pega empezando por el fondo y terminando por los detalles. 5. Deja secar.",
        "Antes de pegar, prueba las posiciones. Mover los papeles es parte del proceso. Si te gusta cómo quedó, pegas. Si no, cambias de lugar. Pegas primero lo que va atrás y al final lo que va adelante, para que nada quede tapado.",
    ],
    vocab=[("procedimiento", "pasos ordenados para hacer algo"), ("collage", "obra hecha pegando trozos de papel u otros materiales"), ("recortar", "cortar una forma con tijera"), ("rasgar", "romper el papel con las manos"), ("fondo", "lo que va atrás de todo y se pega primero")],
    worked=[
        {"title": "Ordenar el collage", "problem": "Ordena los pasos: pegar, planificar, ordenar sin pegar, rasgar o cortar papeles.", "steps": ["Primero planifico con un boceto.", "Luego rasgo o corto los papeles.", "Después los ordeno sin pegar.", "Por último pego."], "answer": "Planificar, rasgar o cortar, ordenar sin pegar, pegar"},
        {"title": "Qué se pega primero", "problem": "Haces un collage de un barco en el mar bajo un sol. ¿Qué pegas primero?", "steps": ["Lo que está atrás es el cielo y el mar.", "Después pego el barco.", "Al final el sol o los detalles pequeños."], "answer": "Primero el cielo y el mar"},
    ],
    mistakes=[
        {"wrong": "Pegar los papeles de inmediato sin ordenar.", "why": "No se prueba la composición y es difícil corregir.", "fix": "Ordena los papeles sobre la hoja, mira, mueve y recién ahí pega."},
        {"wrong": "Pegar primero los detalles pequeños y después el fondo.", "why": "El fondo los tapa o los despega.", "fix": "Pega de atrás hacia adelante."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es un collage? A: una obra hecha pegando papeles u otros materiales. B: una obra hecha con barro.", "A", "Collage viene de pegar."),
            ex("¿Qué se hace con el papel para tener un borde irregular: rasgar o cortar?", "Rasgar", "Al rasgar se rompe sin orden."),
            ex("Antes de pegar, ¿qué haces: ordenar los papeles sobre la hoja o dejarlos en la mesa?", "Ordenarlos sobre la hoja", "Así pruebas cómo queda."),
        ],
        "understand": [
            ex("¿Qué es un procedimiento? A: pasos ordenados para hacer una obra. B: un material.", "A", "Es el camino para crear."),
            ex("¿Qué obra de Matisse usa papeles pintados y recortados que forman una espiral?", "El caracol", "Es su obra de 1953."),
            ex("¿Por qué se pega primero el fondo?", "Para que los detalles queden encima y no tapados", "Lo de atrás va antes."),
        ],
        "apply": [
            ex("Ordena con letras los pasos del collage: A pegar, B planificar con un boceto, C ordenar sin pegar, D rasgar o cortar.", "B, D, C, A", "Primero se planifica, luego se prepara el papel, se prueba y se pega."),
            arith("Para un collage de un jardín usas 6 flores de papel rojo y 4 de papel amarillo. ¿Cuántas flores pegas?", "6 + 4", "Se juntan ambos colores."),
            ex("En un collage de una casa, ¿qué pegas primero: el cielo de fondo o la puerta pequeña?", "El cielo de fondo", "El fondo se pega primero."),
        ],
        "reason": [
            ex("Teo pegó el sol amarillo y después el cielo azul encima de todo. Ya no se ve el sol. ¿En qué se equivocó?", "Pegó el fondo después que el sol", "Primero debía pegar el cielo y luego el sol."),
            ex("Nora rasgó papel verde para el pasto y cortó papel con tijera para las ventanas rectas de la casa. ¿Eligió bien?", "Sí", "El borde irregular imita pasto y los recortes rectos hacen ventanas."),
        ],
        "challenge": [
            arith("Haces un collage con 3 filas de 5 cuadraditos de papel. ¿Cuántos cuadraditos pegas?", "5 + 5 + 5", "Son tres filas iguales de cinco: se suma 5 tres veces."),
            ex("Escribe tres pasos para hacer un collage de una playa con papeles de diario y de colores.", "Planificar, rasgar el mar y la arena, pegar de atrás hacia adelante", "Los pasos siguen el orden del procedimiento."),
        ],
    },
    context=[ex("En tu escuela harán un collage grande sobre el parque del barrio con papeles reciclados. ¿Qué pegan primero: el pasto y el cielo o los pajaritos?", "El pasto y el cielo", "Lo que está atrás o abajo va primero.")],
    selfcheck=[
        ex("¿Cuál es el primer paso de un collage?", "Planificar con un boceto", "Primero se piensa qué se quiere mostrar."),
        ex("¿Se pega el fondo antes o después de los detalles?", "Antes", "Los detalles quedan encima."),
        ex("¿Qué artista francés hizo El caracol con papeles recortados?", "Henri Matisse", "Su obra de 1953 es un collage de colores."),
    ],
    open_task=task(
        "Elige UNO de estos temas: (A) un pez en el mar; (B) una casa con árbol; (C) un gato sentado en una ventana. Haz un collage con papeles rasgados y cortados siguiendo los cinco pasos del procedimiento. Anota los pasos que seguiste con una lista numerada.",
        "Elegí el pez. 1. Hice un boceto. 2. Rasgué papel azul para el mar y corté un óvalo anaranjado para el pez. 3. Los ordené. 4. Pegué primero el mar y luego el pez. 5. Lo dejé secar.",
        ["sigue los pasos del procedimiento", "usa papeles rasgados y cortados", "pega de atrás hacia adelante"],
        ["collage terminado", "lista numerada de pasos"],
        ["pegar sin ordenar", "pegar los detalles antes del fondo"],
        "Reconoce el orden y pide probar dos posiciones antes de pegar.",
    ),
    reinforce="Rasga cinco papeles de diario y di qué forma tiene cada uno antes de pegarlos.",
    extend="Haz un segundo collage con el mismo tema pero con solo tres colores y compara.",
)

# ---------------------------------------------------------------- Clase 5
register(
    OA3, 5,
    materials="Tu obra de la clase anterior o un dibujo simple, una hoja, lápiz y lápices de colores. Las fichas de revisión están escritas en el cuaderno.",
    use="Aprenderé a mirar mi propio proceso, a cambiar una decisión si mejora mi obra y a anotar por qué. Sirve para aprender de lo que hice y mejorar la próxima vez.",
    prior=["Sé que un procedimiento tiene pasos.", "Sé explicar mis decisiones con algo que se ve."],
    explain=[
        "Revisar el proceso es mirar lo que hiciste y preguntarte qué funcionó y qué se puede mejorar. Un artista no termina de inmediato: mira, cambia y vuelve a mirar. Eso se llama ajustar.",
        "Para revisar usa tres preguntas: ¿qué decisión tomé? ¿cómo se ve el resultado? ¿qué cambiaría? Después registras en una ficha: «Cambié… porque…». La razón debe hablar de lo que se ve: un color, una forma, un borde o un material.",
        "Los errores son parte de crear. Si un papel quedó mal pegado o un color se mezcló, eso te enseña algo. Lo importante es anotar qué pasó y qué harás distinto, sin decir «lo hice mal», sino «la próxima vez haré…».",
    ],
    vocab=[("revisar", "mirar lo que hice para ver qué se puede mejorar"), ("ajustar", "cambiar algo pequeño para mejorar"), ("registro", "nota donde escribo lo que hice y por qué"), ("resultado", "cómo quedó la obra"), ("mejorar", "hacer que algo se vea mejor para lo que quiero mostrar")],
    worked=[
        {"title": "Un cambio con razón", "problem": "En tu collage del mar, el azul del mar y el azul del cielo son iguales y no se distinguen. ¿Qué cambias y cómo lo registras?", "steps": ["Miro el resultado: no se distingue el mar del cielo.", "Cambio el mar por un papel azul más oscuro.", "Escribo: cambié el papel del mar a azul oscuro porque así se distingue del cielo."], "answer": "Cambié el mar a azul oscuro porque así se distingue del cielo"},
        {"title": "Aprender de un error", "problem": "Pegaste el barco sin esperar a que se secara el pegamento y se despegó. ¿Qué anotas?", "steps": ["Nombro lo que pasó: el barco se despegó.", "Digo la causa: pegué sin esperar.", "Anoto: la próxima vez dejaré secar."], "answer": "La próxima vez dejaré secar antes de mover"},
    ],
    mistakes=[
        {"wrong": "Decir «mi obra está mal» sin explicar.", "why": "No se indica qué mejorar.", "fix": "Di qué parte te gustaría cambiar y por qué."},
        {"wrong": "Cambiarlo todo y perder lo que estaba bien.", "why": "No se distingue qué funciona y qué no.", "fix": "Cambia una sola cosa a la vez y conserva lo que ya funciona."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué significa revisar tu proceso: mirar lo que hiciste o empezar de nuevo?", "Mirar lo que hiciste", "Revisar es observar y pensar."),
            ex("¿Cómo se llama la nota donde escribes qué cambiaste y por qué?", "Registro", "Registrar es anotar el proceso."),
            ex("En la frase «Cambié el color porque no se distinguía», ¿cuál es la razón?", "Porque no se distinguía", "Después de porque va la razón."),
        ],
        "understand": [
            ex("¿Cuál de estas frases es una buena razón? A: «lo cambié porque sí». B: «lo cambié porque las dos partes eran del mismo color y no se separaban».", "B", "La razón nombra lo que se ve."),
            ex("¿Los errores sirven para aprender?", "Sí", "Muestran qué hacer distinto la próxima vez."),
            ex("¿Cuántas cosas conviene cambiar a la vez? A: una. B: todas.", "A", "Así se ve el efecto del cambio."),
        ],
        "apply": [
            ex("En tu dibujo el sol amarillo se pierde sobre un fondo amarillo pálido. ¿Qué cambias: el fondo a azul o el sol a amarillo pálido?", "El fondo a azul", "El azul contrasta con el amarillo."),
            arith("Revisaste 6 papeles de tu collage y cambiaste 2. ¿Cuántos conservaste?", "6 - 2", "Se restan los que cambiaste."),
            ex("Escribe la frase de registro para esta decisión: cambiaste la lana roja por lana azul porque el rojo tapaba una flor.", "Cambié la lana roja por azul porque el rojo tapaba la flor", "La frase une el cambio con la razón."),
        ],
        "reason": [
            ex("Luis dice «mi collage quedó horrible» y no explica nada. ¿Qué pregunta le haces para ayudarlo a revisar?", "¿Qué parte te gustaría cambiar y por qué?", "Pide una parte concreta y una razón visible."),
            ex("Sofi cambió todos los colores de su obra y ahora no le gusta nada. ¿Qué podría haber hecho distinto?", "Cambiar una sola cosa a la vez", "Cambiar de a una permite ver su efecto."),
        ],
        "challenge": [
            arith("Tu ficha tiene 3 decisiones, 3 resultados y 3 cambios anotados. ¿Cuántas anotaciones hay?", "3 + 3 + 3", "Se suman los tres grupos."),
            ex("Escribe una frase de «la próxima vez» para esta situación: el pegamento no secó y el papel se arrugó.", "La próxima vez usaré menos pegamento", "La frase propone un cambio concreto."),
        ],
    },
    context=[ex("Hiciste un animal con masa y se le cayó la cola. Anota qué harás distinto para que la cola se sostenga.", "La próxima vez la apoyaré con más masa o la uniré con presión", "Es una acción concreta que resuelve el problema.")],
    selfcheck=[
        ex("¿Qué frase usas para registrar un cambio: «Cambié… porque…» o «Está mal»?", "Cambié… porque…", "Une el cambio con la razón."),
        ex("¿Los errores son parte de crear?", "Sí", "De ellos se aprende."),
        ex("¿Qué se mira para revisar: lo que se ve en la obra o solo la opinión de otra persona?", "Lo que se ve en la obra", "La revisión se apoya en la observación."),
    ],
    open_task=task(
        "Toma tu collage de la clase anterior, o dibuja un barco en el mar con tres colores. Mira tu obra y completa esta ficha: «Lo que mejor funciona es… Lo que cambiaría es… porque… Lo hice (o lo haré) así:…». Haz el cambio si puedes y toma nota.",
        "Lo que mejor funciona es el barco naranja. Cambiaría el cielo porque es del mismo azul que el mar. Lo hice con papel celeste. Ahora se distinguen.",
        ["nombra algo que funciona", "propone un cambio con razón", "hace o planifica el ajuste"],
        ["ficha completa", "obra con el ajuste"],
        ["decir que todo está mal", "cambiar sin decir por qué"],
        "Reconoce el ajuste y pide comparar antes y después con una palabra de color o forma.",
    ),
    reinforce="Mira tu obra de ayer y di una cosa que te gusta y una que cambiarías.",
    extend="Haz una segunda versión con el cambio y compara las dos obras en una frase.",
)
