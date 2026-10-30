"""Cuaderno del estudiante de 2.º básico Artes Visuales, AR02 OA 01 (creación desde el entorno y las obras) y AR02 OA 02 (lenguaje visual)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "AR02 OA 01"
OA2 = "AR02 OA 02"


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


# ================================================================ OA 01
# ---------------------------------------------------------------- Clase 1
lesson(
    OA1, 1,
    "Una hoja de papel, un lápiz de mina y, si quieres, un espejo para mirarte en una pose. Si no tienes espejo, usa las poses escritas en este cuaderno.",
    "Aprenderé a dibujar una figura humana que se mueve, usando una línea de acción y doblando el cuerpo en las articulaciones. Sirve para contar con un dibujo qué está haciendo una persona.",
    ["Sé dibujar círculos y líneas con el lápiz.", "Sé que el cuerpo se dobla en el codo y en la rodilla."],
    [
        "Una figura humana en acción muestra a una persona que hace algo: correr, saltar, agacharse o estirarse. Para que se note el movimiento no basta con un cuerpo recto y quieto. Hay que mirar cómo se dobla y se estira el cuerpo.",
        "Primero mira la pose completa. Después dibuja la línea de acción: una línea larga, a veces curva, que va de la cabeza a los pies y muestra hacia dónde va el cuerpo. Sobre ella pon un círculo para la cabeza y líneas para el cuerpo, los brazos y las piernas. Dóblalas en las articulaciones: hombros, codos, caderas y rodillas.",
        "Tu figura no tiene que medir lo mismo que un adulto ni parecerse a nadie. Puede ser de palitos, de manchas o de formas redondas. Lo importante es que la pose se note. Además, cualquier persona puede hacer cualquier acción: niñas, niños, mujeres y hombres corren, saltan y bailan.",
    ],
    [("figura humana", "dibujo o escultura de una persona"), ("pose", "la posición que tiene el cuerpo en un momento"), ("articulación", "lugar donde el cuerpo se dobla, como el codo o la rodilla"), ("línea de acción", "línea que muestra hacia dónde se mueve el cuerpo"), ("figura de palitos", "figura hecha con círculo y líneas")],
    [
        w("Una persona que corre", "Dibuja con palitos a alguien que corre: un brazo va adelante, el otro atrás, y las rodillas están dobladas.", ["Mi línea de acción es una curva suave que se inclina hacia adelante.", "Pongo un círculo para la cabeza sobre la línea.", "Dibujo el brazo derecho doblado hacia adelante y el izquierdo doblado hacia atrás.", "Dibujo las dos rodillas dobladas, una más arriba que la otra."], "Figura inclinada con brazos opuestos y rodillas dobladas"),
        w("Una persona que se agacha", "Dibuja con palitos a alguien que se agacha a recoger una piedra del suelo.", ["Mi línea de acción baja desde la cabeza hacia el suelo.", "Doblo mucho las rodillas y las caderas.", "Estiro un brazo hacia la piedra, con el codo casi recto."], "Figura que baja, con rodillas muy dobladas y un brazo estirado"),
    ],
    [
        m("Dibujar a la persona que corre con brazos y piernas rectos, pegados al cuerpo.", "Se dibuja el cuerpo sin doblarlo en las articulaciones.", "Dobla los codos y las rodillas y deja un brazo adelante y otro atrás."),
        m("Pensar que la figura está mal porque no mide lo mismo que un adulto.", "Se cree que hay una sola medida correcta para el cuerpo.", "En este trabajo lo que importa es que se note el movimiento, no la medida."),
    ],
    [
        ex("Una figura de palitos lleva un círculo para la cabeza y líneas para el resto del cuerpo. ¿Qué forma se usa para la cabeza?", "Un círculo", "La descripción dice que la cabeza se hace con un círculo."),
        ex("Lee: «El niño lanza una pelota con el brazo estirado hacia atrás». ¿Qué parte del cuerpo está estirada hacia atrás?", "El brazo", "La frase nombra el brazo estirado hacia atrás."),
        ex("Pose A: de pie con los brazos pegados al cuerpo. Pose B: corriendo, con un brazo adelante y otro atrás. ¿Cuál muestra más movimiento?", "B", "En la pose B los brazos están en posiciones distintas, como en una carrera."),
    ],
    [
        ex("¿Qué es una articulación? A: un lugar donde el cuerpo se dobla, como el codo. B: un tipo de lápiz. C: un color.", "A", "El codo, la rodilla y la cadera son articulaciones porque ahí el cuerpo se dobla."),
        ex("La línea de acción de una persona que salta hacia arriba es una curva que sube. ¿Hacia dónde apunta esa línea?", "Hacia arriba", "La línea de acción apunta hacia donde va el cuerpo."),
        ex("Entre rodilla, pelo y uña, ¿cuál es una articulación?", "La rodilla", "Es el lugar donde la pierna se dobla."),
    ],
    [
        arith("Una figura de palitos tiene 1 línea para el cuerpo, 2 líneas para los brazos y 2 líneas para las piernas. ¿Cuántas líneas dibujas, sin contar la cabeza?", "1 + 2 + 2", "Se suman las líneas del cuerpo, los brazos y las piernas."),
        ex("Quieres dibujar a alguien que se agacha. ¿Qué articulación de las piernas se dobla mucho: la rodilla o el codo?", "La rodilla", "El codo es del brazo; al agacharse se doblan las rodillas."),
        ex("Ordena los pasos: A dibujar la cabeza, B dibujar brazos y piernas doblados, C mirar la pose, D trazar la línea de acción.", "C, D, A, B", "Primero se mira la pose, luego se traza la línea, después la cabeza y al final los brazos y piernas."),
    ],
    [
        ex("Sofía dibuja a una persona que corre con los dos brazos y las dos piernas rectos, pegados al cuerpo. ¿Se ve movimiento? Explica.", "No; faltan articulaciones dobladas", "Una carrera necesita codos y rodillas doblados y brazos en posiciones distintas."),
        ex("Pedro dice: «Mi figura solo es buena si mide igual que un adulto». ¿Tiene razón?", "No", "En este trabajo importa mostrar la pose, no copiar la medida de un adulto."),
    ],
    [
        ex("Dibujas a tres amigos: uno salta, otro gira y otro se agacha, cada uno con su propia línea de acción. ¿Cuántas líneas de acción dibujas?", "3", "Hay una línea de acción por cada figura."),
        ex("Lee: «Una persona está sentada en el suelo con la espalda inclinada hacia adelante y los codos apoyados en las rodillas». ¿Qué dos articulaciones se nombran?", "Los codos y las rodillas", "La frase nombra exactamente esas dos partes del cuerpo."),
    ],
    ex("Quieres mostrar a un niño que patea una pelota con la pierna derecha estirada hacia adelante, mientras la pierna izquierda lo sostiene en el suelo. ¿Qué pierna dibujas estirada?", "La derecha", "El enunciado dice que patea con la pierna derecha."),
    [
        ex("¿Qué dibujas primero: la línea de acción o los dedos de las manos?", "La línea de acción", "Se parte por lo grande, que da el movimiento a toda la figura."),
        ex("Verdadero o falso: una persona corriendo suele tener las rodillas rectas.", "Falso", "Al correr las rodillas se doblan."),
        ex("¿Cómo se llama el lugar donde el brazo se dobla?", "Codo", "El codo es la articulación del brazo."),
    ],
    task(
        "Elige UNA acción: saltar, agacharse o estirarse para alcanzar algo alto. Haz esa pose frente a un espejo o imagínala. Dibuja dos figuras de palitos con la misma acción pero distinta línea de acción, y elige la que muestra mejor el movimiento. Escribe por qué. Dibuja personas imaginadas, no personas reales con nombre.",
        "Elegí saltar. Mi dibujo 1 tiene una línea recta y se ve quieto. Mi dibujo 2 tiene una curva que sube, los brazos arriba y las rodillas dobladas. Elijo el 2 porque se nota que salta.",
        ["dibuja dos figuras con la misma acción", "dobla las articulaciones", "usa una línea de acción", "explica su elección con una razón del dibujo"],
        ["dos figuras de palitos", "una frase de elección"],
        ["figuras rectas y sin doblar", "elegir solo porque «se ve bonito» sin mirar el movimiento"],
        "Reconoce la pose lograda y pide que muestre dónde doblaste una articulación para que se note la acción.",
    ),
    "Mírate un minuto en un espejo mientras estiras un brazo hacia arriba. Di en voz alta qué articulaciones se doblaron o se estiraron.",
    "Dibuja la misma acción vista desde otro lado, por ejemplo corriendo hacia el lado contrario, y anota qué cambió en la línea de acción.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA1, 2,
    "Una hoja, lápices de colores y un marco de papel: recorta un rectángulo en el centro de una hoja o cartulina. Si no puedes, usa los paisajes escritos en este cuaderno.",
    "Aprenderé a elegir qué parte de un paisaje chileno dibujar y a ordenar el primer plano, el fondo y el horizonte. Sirve para que mis dibujos de paisajes se vean con profundidad.",
    ["Sé dibujar montañas, árboles y casas simples.", "Sé que lo que está lejos se ve más pequeño."],
    [
        "Un paisaje es lo que se ve de un lugar al aire libre: montañas, mar, bosque, desierto o campo. Chile tiene paisajes muy distintos, como el desierto del norte, los bosques del sur y la cordillera de los Andes. Antes de dibujar, elige qué parte vas a mostrar. Esa elección se llama encuadre.",
        "Luego ordena el paisaje en tres lugares. El primer plano es lo que está más cerca y se dibuja más grande. El fondo es lo que está lejos y se dibuja más pequeño. En el medio queda el plano medio. El horizonte es la línea donde parece que se juntan el cielo y la tierra o el mar.",
        "También puedes cambiar el punto de vista: mirar desde lo alto de un cerro, desde el suelo o desde una ventana. El mismo lugar se verá distinto. Para elegir el encuadre, mira por el marco de papel y mueve el marco hasta que quede solo lo que quieres dibujar.",
    ],
    [("paisaje", "vista de un lugar al aire libre"), ("encuadre", "la parte del paisaje que elijo mostrar"), ("primer plano", "lo que está más cerca de mí"), ("fondo", "lo que está más lejos"), ("horizonte", "línea donde parece que se juntan el cielo y la tierra o el mar")],
    [
        w("Una playa del Pacífico", "Una playa tiene una roca grande y arena al frente, olas en el medio y un cerro azul a lo lejos. ¿Qué va en el primer plano y qué en el fondo?", ["Miro lo que está más cerca: la roca grande y la arena.", "Miro lo que está más lejos: el cerro azul.", "Dibujo la roca grande abajo y el cerro pequeño arriba, cerca del horizonte."], "Primer plano: roca y arena. Fondo: cerro azul"),
        w("El desierto del norte", "Quieres mostrar mucho cielo sobre un desierto. ¿Dónde pones el horizonte?", ["Si quiero mucho cielo, necesito mucho espacio arriba.", "Entonces bajo la línea del horizonte hacia la parte de abajo de la hoja."], "El horizonte va abajo en la hoja"),
    ],
    [
        m("Dibujar los árboles lejanos igual de grandes que los cercanos.", "No se piensa en la distancia.", "Dibuja pequeño y más arriba lo que está lejos, y grande y abajo lo que está cerca."),
        m("Pensar que todos los paisajes de Chile tienen nieve y montañas.", "Se conoce solo un tipo de paisaje.", "Chile tiene desierto, playas, bosques y campos. Elige el lugar que observaste."),
    ],
    [
        ex("Paisaje: roca grande y arena al frente, olas en el medio, cerro azul a lo lejos. ¿Qué cosas están en el primer plano?", "La roca grande y la arena", "Son las que están al frente, es decir, más cerca."),
        ex("En ese mismo paisaje, ¿qué está más lejos: la roca o el cerro azul?", "El cerro azul", "El cerro está a lo lejos, la roca está al frente."),
        ex("La línea del horizonte es donde parece que se juntan el cielo y el mar. ¿Es verdad? Responde sí o no.", "Sí", "Esa es justamente la definición de horizonte."),
    ],
    [
        ex("Dibujas un árbol grande abajo y un árbol muy pequeño arriba, cerca del horizonte. ¿Cuál parece estar más lejos?", "El pequeño", "Lo que está lejos se dibuja más pequeño y más arriba."),
        ex("¿Qué es el encuadre? A: el color del cielo. B: la parte del paisaje que elijo mostrar. C: el lápiz que uso.", "B", "Encuadrar es decidir qué parte entra en el dibujo."),
        ex("Tomás mira un valle desde lo alto de un cerro y Ana lo mira desde el suelo. ¿Cambió el punto de vista?", "Sí", "Cada uno mira desde un lugar distinto y ve el valle de otra manera."),
    ],
    [
        arith("En tu dibujo hay 2 rocas en el primer plano, 3 árboles en el plano medio y 4 cerros en el fondo. ¿Cuántas cosas dibujaste en total?", "2 + 3 + 4", "Se suman los elementos de los tres lugares del dibujo."),
        ex("Ordena de más cerca a más lejos: A un cerro nevado, B un cactus pequeño a tu lado, C unos postes de luz en el camino.", "B, C, A", "El cactus está a tu lado, los postes están más lejos y el cerro es lo más lejano."),
        ex("Quieres un paisaje del desierto con mucho cielo. ¿Pones el horizonte arriba o abajo en la hoja?", "Abajo", "Con el horizonte abajo queda mucho espacio para el cielo."),
    ],
    [
        ex("Luz dibuja un bosque con todos los árboles, grandes y chicos, pegados al borde de abajo. ¿Se nota la distancia entre ellos? Explica.", "No; lo lejano debe ir más arriba y más chico", "Todos están a la misma altura y parecen estar a la misma distancia."),
        ex("Ema dice: «Un paisaje chileno siempre debe tener nieve». ¿Tiene razón?", "No", "Chile tiene desierto, playas, bosques y campos sin nieve."),
    ],
    [
        ex("Lee: «Un camino de tierra parte abajo y se hace más angosto hasta llegar a una casa pequeña al pie de un volcán enorme». ¿En qué plano está el volcán?", "En el fondo", "El volcán es enorme pero se ve lejano, detrás de la casa."),
        ex("En la misma descripción el camino se hace más angosto. ¿Qué indica eso de la casa: que está cerca o lejos?", "Lejos", "Lo angosto del camino sugiere que la casa está lejos."),
    ],
    ex("Tu familia viaja a un lago del sur. Quieres dibujar solo el lago y el volcán detrás, no la carretera. ¿Qué haces: dibujar toda la vista o mover tu marco de papel hasta encuadrar solo eso?", "Mover el marco hasta encuadrar lago y volcán", "El marco ayuda a elegir qué parte entra en el dibujo."),
    [
        ex("¿Cómo se llama lo que está más cerca de ti en el dibujo?", "Primer plano", "Así se llama la zona más cercana."),
        ex("¿Dónde dibujas una montaña lejana: grande y abajo o pequeña y arriba?", "Pequeña y arriba", "Lo lejano se ve más pequeño y cerca del horizonte."),
        ex("Si cambias de lugar para mirar el paisaje, ¿qué cambias?", "El punto de vista", "Mirar desde otro sitio cambia el punto de vista."),
    ],
    task(
        "Elige UNO de estos paisajes: A) una playa con una roca grande al frente, olas en el medio y un cerro lejano; B) un desierto con mucho cielo, un cactus cerca y cerros muy lejos; C) un bosque del sur con un tronco grande al frente y árboles que se hacen más pequeños. Dibújalo con primer plano, fondo y horizonte. Escribe qué pusiste en cada lugar.",
        "Elegí B. Pongo el horizonte abajo para tener mucho cielo. En el primer plano hay un cactus grande, en el plano medio dos piedras y en el fondo unos cerros pequeños.",
        ["dibuja primer plano, fondo y horizonte", "lo cercano es más grande que lo lejano", "explica qué puso en cada lugar"],
        ["dibujo del paisaje", "una frase por cada lugar del dibujo"],
        ["todo del mismo tamaño y a la misma altura", "sin línea de horizonte"],
        "Reconoce el plano que quedó bien y pide que ubique un elemento más cerca o más lejos para mejorar la profundidad.",
    ),
    "Mira por una ventana de tu casa durante un minuto. Di en voz alta qué ves en el primer plano y qué ves al fondo.",
    "Dibuja el mismo paisaje con otro encuadre: ahora mostrando solo la mitad de abajo. Anota qué cambió.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA1, 3,
    "Hoja, lápiz de mina y lápices de colores. Usa las escenas escritas en este cuaderno o recuerda una situación general que hayas visto (sin nombrar personas reales).",
    "Aprenderé a dibujar escenas de personas haciendo cosas de todos los días, mostrando variedad y sin estereotipos. Sirve para contar con dibujos cómo vivimos.",
    ["Sé dibujar figuras de palitos con movimiento.", "Sé que las personas hacen muchas actividades distintas."],
    [
        "Las personas están en todas partes: en la feria, en la plaza, en una panadería o en una cancha. Para dibujar una escena de la vida de todos los días, mira qué hace cada persona. Fíjate en sus manos, en su postura y en lo que usa. Así tu dibujo cuenta una historia sin palabras.",
        "Un estereotipo es una idea fija sobre cómo es un grupo de personas. Por ejemplo, pensar que solo las mujeres cocinan o que solo los hombres arreglan cosas. Eso no es verdad: cualquier persona puede cocinar, arreglar, cuidar, cantar o construir. Cuando dibujes, muestra personas distintas haciendo actividades distintas.",
        "También puedes variar las edades, la ropa, la altura y la forma del cuerpo. No necesitas dibujar caras con muchos detalles: la postura y los objetos ya muestran lo que ocurre. Dibuja personas imaginadas o situaciones generales. No dibujes ni escribas nombres de personas reales sin su permiso.",
    ],
    [("escena", "momento en que pasa algo, dibujado o contado"), ("vida cotidiana", "las cosas que hacemos todos los días"), ("estereotipo", "idea repetida que dice que un grupo siempre es de una sola manera"), ("postura", "cómo está puesto el cuerpo"), ("variedad", "cosas distintas dentro de un mismo dibujo")],
    [
        w("Una escena de feria", "En una feria hay un hombre que pesa fruta, una niña que elige paltas, una abuela que cuenta monedas y una joven que carga cajas. ¿Cuántas personas hay y qué hace cada una?", ["Cuento las personas que se nombran: hombre, niña, abuela y joven.", "Anoto la acción de cada una: pesar, elegir, contar y cargar.", "Dibujo cada una con una postura distinta."], "4 personas con 4 acciones distintas"),
        w("Evitar un estereotipo", "Quieres dibujar a alguien que cocina en una casa. ¿Cómo evitas repetir una idea fija?", ["Pienso que cualquier persona puede cocinar.", "Dibujo a un papá o a un abuelo con delantal, y también a alguien que arregla una bicicleta."], "Mostrar a personas distintas en cada actividad"),
    ],
    [
        m("Dibujar siempre a las mujeres cocinando y a los hombres trabajando afuera.", "Se repite una idea fija y no se mira la variedad real.", "Cambia las actividades y muestra a cualquier persona haciendo cualquier tarea."),
        m("Dibujar a todas las personas con el mismo cuerpo, la misma ropa y la misma postura.", "Se copia un modelo de memoria en vez de observar.", "Varía la altura, la edad y la postura según lo que hace cada persona."),
    ],
    [
        ex("Escena de feria: un hombre pesa fruta, una niña elige paltas, una abuela cuenta monedas y una joven carga cajas. ¿Cuántas personas hay?", "4", "Se nombran cuatro personas distintas."),
        ex("En esa escena, ¿qué hace la abuela?", "Cuenta monedas", "La frase dice que la abuela cuenta monedas."),
        ex("¿Qué dice más sobre la acción de una persona en un dibujo: su postura o el color de su polera?", "Su postura", "El cuerpo y las manos muestran lo que hace."),
    ],
    [
        ex("¿Qué es un estereotipo? A: una idea fija sobre cómo es o qué hace un grupo. B: un lápiz grueso. C: un paisaje.", "A", "Un estereotipo repite una idea simple sobre un grupo de personas."),
        ex("Un dibujo muestra a un niño y a un adulto cuidando plantas en la plaza. ¿Es una actividad que solo puede hacer una persona de un solo tipo?", "No", "Cuidar plantas lo puede hacer cualquier persona."),
        ex("En una escena de panadería hay una persona que hornea, otra que atiende y otra que compra. ¿Cuántas actividades distintas se muestran?", "3", "Hornear, atender y comprar son tres actividades."),
    ],
    [
        arith("En tu escena de plaza dibujas 3 personas que juegan, 2 que conversan y 1 que lee. ¿Cuántas personas hay en total?", "3 + 2 + 1", "Se suman las personas de cada grupo."),
        ex("Quieres dibujar a alguien que arregla una bicicleta. ¿Qué dibujas para que se entienda lo que hace: la herramienta en la mano y la bicicleta, o un fondo de estrellas?", "La herramienta en la mano y la bicicleta", "Los objetos que usa la persona cuentan qué está haciendo."),
        ex("Dos dibujos de cocina. Dibujo A: solo una mujer cocina. Dibujo B: un abuelo y una niña cocinan juntos. ¿Cuál se esfuerza más por mostrar variedad?", "B", "Muestra a personas de distintas edades y no repite una idea fija."),
    ],
    [
        ex("Julia dibuja una cancha y pone solo niños jugando, y a las niñas mirando desde afuera. ¿Qué podría cambiar para evitar el estereotipo?", "Mostrar niñas y niños jugando", "Cualquier persona puede jugar, así que ambos deben aparecer en la acción."),
        ex("Beto dice: «Para dibujar personas siempre debo dibujar sus caras con todos los detalles». ¿Es necesario?", "No", "La postura y los objetos ya muestran lo que ocurre."),
    ],
    [
        ex("Una escena tiene 5 personas: una barre, dos conversan, una vende pan y una compra. Las dos que conversan hacen la misma actividad. ¿Cuántas actividades distintas hay?", "4", "Barrer, conversar, vender y comprar son cuatro actividades distintas."),
        ex("En la misma escena, si agregas a una persona que corta el pelo, ¿cuántas actividades distintas habría?", "5", "Se suma una actividad nueva a las cuatro anteriores."),
    ],
    ex("Te piden dibujar a una familia haciendo el aseo. Dibujas a una persona pasando la aspiradora, otra lavando los platos y otra ordenando libros. ¿Cuántas acciones distintas muestran?", "3", "Aspirar, lavar y ordenar son tres acciones."),
    [
        ex("¿Qué miras para mostrar lo que hace una persona: sus manos y su postura, o su nombre?", "Sus manos y su postura", "El cuerpo cuenta la acción."),
        ex("Verdadero o falso: solo las mujeres pueden cuidar a otras personas.", "Falso", "Cualquier persona puede cuidar a otras."),
        ex("En una escena hay un grupo de personas que hacen todas lo mismo. ¿Hay mucha variedad o poca?", "Poca", "Variedad significa actividades distintas."),
    ],
    task(
        "Elige UNA de estas escenas: A) una feria con un puesto de frutas, otro de flores y gente que compra; B) una plaza con personas jugando, leyendo y conversando; C) una panadería con alguien que hornea, alguien que atiende y alguien que compra. Dibuja al menos cuatro personas con acciones distintas. Escribe en una frase por qué tu escena no repite una idea fija.",
        "Elegí la plaza. Dibujé a un abuelo que lee, a una niña que salta la cuerda, a un papá que conversa con una vecina y a un joven que pinta un banco. Mostré personas distintas en actividades distintas.",
        ["dibuja al menos cuatro personas", "cada una hace una acción distinta", "usa la postura para mostrar la acción", "explica cómo evitó repetir una idea fija"],
        ["dibujo de la escena", "una frase de explicación"],
        ["todas las personas iguales y haciendo lo mismo", "repetir que cada tarea es solo de un tipo de persona"],
        "Reconoce una acción bien mostrada y pide que cambie una actividad para ampliar la variedad, sin criticar a la persona.",
    ),
    "Observa durante un minuto a tu familia haciendo una tarea en casa. Di en voz alta qué hacen las manos de cada persona, sin escribir nombres.",
    "Dibuja la misma escena con una actividad nueva en cada persona y compara qué cambió.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA1, 4,
    "Hoja, lápiz de mina y lápices de colores. No necesitas ver el lugar: usa las descripciones de este cuaderno sobre las iglesias de madera de Chiloé, los moai de Rapa Nui y la greda de Pomaire.",
    "Aprenderé a mirar un patrimonio cultural de Chile y a usarlo como punto de partida para crear algo propio. Sirve para valorar lo que otros crearon y cuidarlo.",
    ["Sé dibujar formas simples.", "Sé que algunas cosas se cuidan porque son importantes para muchas personas."],
    [
        "El patrimonio cultural son las cosas que nuestros antepasados crearon y que hoy cuidamos para que otras personas las conozcan: lugares, objetos, fiestas y saberes. En Chile hay muchos, como las iglesias de madera de Chiloé, los moai de piedra de Rapa Nui y las ollas de greda de Pomaire.",
        "Puedes partir de un patrimonio para crear. Observa su material, su forma y sus detalles. Una iglesia de Chiloé es de madera, con una torre y tablitas pequeñas llamadas tejuelas que cubren las paredes. Los moai son grandes figuras de piedra con rostro. La greda es una arcilla con la que se hacen ollas y figuras.",
        "No copies el patrimonio tal cual. Elige una parte, como la forma, el material o el patrón, y crea algo tuyo. Por ejemplo, una casa con paredes de tablitas. Cuida el patrimonio con respeto: se mira, no se raya ni se rompe. Los moai son importantes para el pueblo rapanui, y los dibujamos con respeto.",
    ],
    [("patrimonio cultural", "lo que nos dejaron nuestros antepasados y cuidamos hoy"), ("material", "de qué está hecho algo, como madera o piedra"), ("greda", "arcilla con la que se hacen ollas y figuras"), ("tejuela", "tablita pequeña que cubre una pared de madera"), ("punto de partida", "la idea o parte que uso para empezar a crear")],
    [
        w("Mirar una iglesia de madera", "Una iglesia de Chiloé es de madera, tiene una torre y sus paredes están cubiertas de tejuelas. ¿Qué tres datos observas?", ["El material: madera.", "La parte: una torre.", "El detalle: tejuelas pequeñas en las paredes."], "Madera, torre y tejuelas"),
        w("Crear a partir de la greda", "Una olla de greda es redonda y de color tierra. Quieres crear algo tuyo a partir de ella. ¿Qué parte tomas?", ["Tomo la forma redonda.", "Cambio el uso: hago una maceta redonda con tres flores dibujadas.", "No copio la olla: hago una creación nueva."], "Tomo la forma redonda y creo una maceta"),
    ],
    [
        m("Dibujar un moai con muecas graciosas o burlarse de él.", "No se piensa que es un patrimonio importante para un pueblo.", "Dibuja con respeto, mirando sus rasgos con atención."),
        m("Copiar el dibujo de una iglesia tal cual y decir que es una creación propia.", "No se toma una decisión personal.", "Toma una parte (la torre, las tejuelas) y combínala con tus ideas."),
    ],
    [
        ex("Las iglesias de Chiloé son de madera. ¿De qué material están hechas?", "De madera", "El texto dice que su material es la madera."),
        ex("Los moai son figuras grandes. ¿De qué material son: piedra o plástico?", "Piedra", "Los moai son figuras de piedra con rostro."),
        ex("Las ollas de Pomaire se hacen con una arcilla. ¿Cómo se llama esa arcilla?", "Greda", "El cuaderno nombra la greda como la arcilla de Pomaire."),
    ],
    [
        ex("¿Qué es el patrimonio cultural? A: lo que nuestros antepasados dejaron y hoy cuidamos. B: un lápiz. C: un tipo de pintura.", "A", "El patrimonio se hereda y se cuida."),
        ex("Las tejuelas son tablitas pequeñas. ¿Dónde se ponen en una iglesia de Chiloé?", "En las paredes", "Cubren las paredes de madera."),
        ex("Quieres respetar un patrimonio. ¿Haces rayas en él o lo miras con cuidado?", "Lo miro con cuidado", "Cuidar significa no dañarlo ni rayarlo."),
    ],
    [
        arith("Una iglesia dibujada tiene 1 torre, 2 puertas y 3 ventanas. ¿Cuántas partes distintas dibujas en total?", "1 + 2 + 3", "Se suman las torres, las puertas y las ventanas."),
        ex("Quieres usar la forma redonda de una olla de greda para crear una luna. ¿Estás copiando la olla o usándola como punto de partida?", "Usándola como punto de partida", "Tomas una forma y la conviertes en algo nuevo."),
        ex("Ordena para crear a partir de un patrimonio: A hacer tu dibujo propio, B elegir una parte para usar, C mirar el patrimonio con atención.", "C, B, A", "Se mira primero, luego se elige una parte y al final se crea."),
    ],
    [
        ex("Luz dice: «Si copio una iglesia exactamente, es mi creación». ¿Tiene razón?", "No", "Copiar tal cual no incluye decisiones propias."),
        ex("Mateo dibuja un moai con una nariz de payaso para hacer reír. ¿Respeta el patrimonio? Explica.", "No; el moai es importante para un pueblo y se dibuja con respeto", "Convertirlo en burla no lo trata con respeto."),
    ],
    [
        ex("Quieres crear un animal con paredes de tejuelas, como las iglesias de Chiloé. ¿Qué detalle tomaste del patrimonio?", "Las tejuelas", "Usas el patrón de tablitas pequeñas."),
        ex("Quieres crear una casa con una torre de madera. ¿Qué dos datos del patrimonio usas: material y parte?", "Madera y torre", "El material es la madera y la parte es la torre."),
    ],
    ex("En tu colegio piden dibujar un patrimonio para una exposición. Escoges una olla de greda. Escribes que es redonda, de color tierra y que se hace con arcilla. ¿Cuántos datos observados escribiste?", "3", "Forma redonda, color tierra y material arcilla son tres datos."),
    [
        ex("¿De qué material son los moai?", "De piedra", "Son figuras de piedra."),
        ex("¿Qué se puede hacer con la greda de Pomaire?", "Ollas y figuras", "El cuaderno dice que sirve para ollas y figuras."),
        ex("Si usas solo la forma de un patrimonio y la mezclas con tus ideas, ¿copias o creas?", "Creas", "Tomas una parte y haces algo nuevo."),
    ],
    task(
        "Elige UNO de estos patrimonios: A) una iglesia de madera de Chiloé, con torre y tejuelas; B) una olla de greda de Pomaire, redonda y de color tierra; C) un moai de piedra de Rapa Nui. Anota dos datos que observas. Después crea un dibujo propio que tome UNA parte (la forma, el material o el patrón) sin copiarlo tal cual. Escribe qué parte tomaste.",
        "Elegí la iglesia. Datos: es de madera y tiene tejuelas. Tomé las tejuelas y dibujé un pez con escamas hechas de tablitas.",
        ["anota dos datos del patrimonio", "toma una parte y no lo copia tal cual", "trata el patrimonio con respeto", "explica qué parte tomó"],
        ["dos datos anotados", "dibujo propio", "una frase sobre la parte elegida"],
        ["copiar tal cual", "hacer burla de un patrimonio"],
        "Reconoce la parte que tomó y pide que muestre qué agregó él o ella para hacerlo suyo.",
    ),
    "Cuenta a alguien de tu casa un lugar o un objeto antiguo que se cuida porque es importante para muchas personas.",
    "Busca en un libro, con ayuda de un adulto, otro patrimonio de tu región y anota su material y una parte que podrías usar para crear.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA1, 5,
    "Hoja, lápiz y lápices de colores. Las obras de este cuaderno son descripciones inventadas para practicar la observación. Si puedes, un adulto o tu docente te muestra imágenes de obras reales de la biblioteca o de tu escuela: un mural de tu barrio, una arpillera chilena y un tejido de lana de los Andes.",
    "Aprenderé a mirar obras de arte de Chile y Latinoamérica y a usar una de sus ideas para crear una obra mía. Sirve para aprender de otros artistas sin copiarlos.",
    ["Sé que una obra de arte tiene colores, formas y materiales.", "Sé decir qué veo en una imagen."],
    [
        "Una obra de arte es algo que un artista crea para expresar una idea o un sentimiento. Hay obras de Chile, de otros países de Latinoamérica y del mundo. Pueden ser pinturas, murales, esculturas, tejidos o cerámicas. Para mirarlas, pregúntate: ¿qué hay? ¿De qué material es? ¿Qué colores y líneas usa?",
        "Mira estas tres obras que se describen en este cuaderno. Obra A: un mural en el muro de una plaza, con peces de colores y un sol amarillo. Obra B: una escultura de piedra pulida con forma de ave de alas abiertas. Obra C: un tejido de lana con rombos rojos y negros. Son descripciones inventadas para practicar la mirada.",
        "Hay obras de tu comunidad, como un mural en un muro de tu barrio. Hay obras de Chile, como las arpilleras, que son cuadros hechos con retazos de tela cosidos. Hay obras de Latinoamérica, como los tejidos de lana de los Andes. Cuando una obra te inspira, no la copies. Toma una sola idea de ella, como la forma, el color o el material, y mézclala con tu propia idea. Así creas algo nuevo. Escribe siempre de dónde sacaste la idea.",
    ],
    [("obra de arte", "algo que crea un artista para expresar una idea"), ("mural", "pintura grande hecha sobre un muro"), ("escultura", "obra con volumen que se puede rodear"), ("tejido", "obra hecha entrecruzando hilos o lana"), ("inspirarse", "tomar una idea de una obra para crear algo propio")],
    [
        w("Mirar el mural", "Obra A: un mural con peces de colores y un sol amarillo. ¿Qué preguntas te haces y qué respondes?", ["¿Qué hay? Peces y un sol.", "¿Qué colores? Colores variados y amarillo.", "¿Qué tipo de obra es? Un mural, pintado sobre un muro."], "Peces y sol, colores variados y amarillo, es un mural"),
        w("Inspirarse sin copiar", "Te gusta la forma del ave de alas abiertas de la obra B. ¿Cómo la usas?", ["Tomo la forma de alas abiertas.", "Dibujo una mariposa con alas abiertas de mis colores favoritos.", "Anoto: me inspiré en la obra B."], "Una mariposa con alas abiertas, inspirada en la obra B"),
    ],
    [
        m("Dibujar el mismo mural con peces y sol, igualito, y decir que es mi obra.", "Se confunde inspirarse con copiar.", "Toma una idea (el sol, los peces) y cámbiala con tu propia idea."),
        m("Mirar una obra y decir solo «es linda» o «es fea».", "No se observan los elementos de la obra.", "Di qué colores, formas y materiales ves."),
    ],
    [
        ex("Obra A es un mural con peces de colores y un sol amarillo. ¿Sobre qué soporte está pintado un mural?", "Un muro", "Mural quiere decir pintura hecha sobre un muro."),
        ex("Obra B es una escultura de piedra pulida con forma de ave. ¿De qué material es?", "De piedra", "El texto dice que es de piedra pulida."),
        ex("Obra C es un tejido de lana con rombos. ¿De qué material es?", "De lana", "El texto dice que el tejido es de lana."),
    ],
    [
        ex("¿Qué forma geométrica se repite en la obra C? A: círculos. B: rombos. C: triángulos.", "B", "La descripción dice que el tejido tiene rombos rojos y negros."),
        ex("¿Qué colores tiene el tejido de la obra C?", "Rojo y negro", "La descripción nombra rombos rojos y negros."),
        ex("Los tejidos de lana de los Andes son obras de Latinoamérica. ¿Es verdad? Responde sí o no.", "Sí", "Los Andes son una cordillera de América del Sur, así que esos tejidos son latinoamericanos."),
    ],
    [
        arith("En la obra A hay 4 peces rojos y 3 peces azules. ¿Cuántos peces hay en total?", "4 + 3", "Se suman los peces de cada color."),
        ex("Te inspira el tejido de la obra C y haces un pez con rombos rojos y negros en el cuerpo. ¿Qué tomaste de la obra?", "Los rombos y los colores", "Usaste el patrón de la obra en tu propio pez."),
        ex("Ordena para inspirarte: A anotar de qué obra tomaste la idea, B crear tu dibujo, C mirar y elegir una idea de la obra.", "C, B, A", "Se mira primero, luego se crea y al final se anota la fuente."),
    ],
    [
        ex("Ana dibuja un mural idéntico al de la obra A y escribe su nombre. ¿Se inspiró o copió?", "Copió", "El dibujo es idéntico, sin ideas propias."),
        ex("Bruno dice: «Si solo digo que la obra B es linda, ya la observé». ¿Es cierto?", "No", "Observar es decir qué hay, de qué es y qué colores tiene."),
    ],
    [
        ex("Combinas la forma del ave de la obra B con el sol de la obra A. ¿Cuántas obras usaste como inspiración?", "2", "Tomaste una idea de A y otra de B."),
        ex("Una niña dice: «Tomo los rombos de la obra C y los pinto de azul y verde en mi tela». ¿Cambió el color o la forma?", "El color", "La forma sigue siendo rombos; lo que cambió son los colores."),
    ],
    ex("Tu escuela hace una exposición «Inspirados en obras». Escoges la obra A. Escribes en la etiqueta: «Me inspiré en un mural con peces y un sol». ¿Qué dato incluiste: la fuente de tu idea o tu nombre completo?", "La fuente de tu idea", "Contaste de qué obra sacaste la idea."),
    [
        ex("¿De qué es la obra C?", "Lana", "Es un tejido de lana."),
        ex("Verdadero o falso: inspirarse es copiar todo igual.", "Falso", "Inspirarse es tomar una idea y hacer algo nuevo."),
        ex("Una arpillera es un cuadro hecho con retazos de tela cosidos. ¿Con qué material se hace: con retazos de tela o con piedra?", "Con retazos de tela", "La arpillera se arma cosiendo trozos de tela."),
    ],
    task(
        "Elige UNA de las obras A, B o C descritas en este cuaderno. Anota qué ves en ella (dos datos). Crea un dibujo propio que tome UNA idea de la obra (forma, color o material) mezclada con una idea tuya. Escribe qué tomaste.",
        "Elegí la obra B. Veo un ave y alas abiertas. Tomé las alas abiertas y dibujé una mariposa con alas de mis colores favoritos.",
        ["anota dos datos de la obra", "toma una sola idea", "agrega una idea propia", "escribe qué tomó"],
        ["dos datos escritos", "dibujo propio", "una frase de fuente"],
        ["copiar la obra completa", "no decir de dónde vino la idea"],
        "Reconoce lo que agregó de propio y pide que explique qué cambió respecto de la obra.",
    ),
    "Pregunta a alguien de tu casa si conoce un mural, una escultura o un tejido de tu ciudad. Cuenta qué materiales tiene.",
    "Con ayuda de tu docente o de un adulto, mira imágenes de una obra real de tu comunidad, una de Chile y una de Latinoamérica. Anota de qué material es cada una y qué colores tiene. Elige otra obra descrita y crea una segunda versión con otra idea distinta.",
)

# ---------------------------------------------------------------- Clase 6
lesson(
    OA1, 6,
    "Hoja, lápices de colores y un marco de papel en forma de ventana. Las obras de este cuaderno son descripciones inventadas; si puedes, un adulto te muestra imágenes de obras de otros lugares.",
    "Aprenderé a mirar obras de otros lugares del mundo como si fuera por una ventana y a crear algo mío a partir de una idea. Sirve para conocer cómo se hace arte en otros lugares.",
    ["Sé mirar una obra y decir qué materiales y colores tiene.", "Sé que inspirarse no es copiar."],
    [
        "El arte se hace en todo el mundo. Cada lugar tiene sus propios materiales, colores y formas de ver. Mirar obras de otros lugares es como abrir una ventana: te deja ver cosas distintas a las que ves cada día. Hay pinturas, esculturas, máscaras y tejidos de Asia, África, Europa, Oceanía y América. Para mirar, pregunta qué hay, de qué está hecha y qué te hace pensar.",
        "Mira estas tres obras descritas. Obra D: una pintura de montañas azules cubiertas de nieve junto a un lago quieto. Obra E: una máscara de madera con ojos grandes y rayas en las mejillas. Obra F: una escultura pequeña de metal con forma de caballo. No sabemos de qué país son: son ejemplos inventados para practicar.",
        "Compara con tu entorno. En Chile también hay montañas con nieve, como la cordillera de los Andes. Puedes ver parecidos y diferencias. Luego toma una idea, como las rayas o el lago quieto, y crea algo tuyo. Mira con respeto: cada obra viene de personas con su propia historia.",
    ],
    [("obra universal", "obra de cualquier lugar del mundo"), ("semejanza", "algo que se parece entre dos cosas"), ("diferencia", "algo que no se parece entre dos cosas"), ("máscara", "obra que cubre o representa un rostro"), ("comparar", "mirar dos cosas para ver en qué se parecen y en qué no")],
    [
        w("Comparar con mi entorno", "Obra D: montañas azules con nieve y un lago quieto. En Chile también hay montañas con nieve. ¿Qué semejanza y qué diferencia hay entre la obra D y la cordillera?", ["Semejanza: ambas tienen montañas con nieve.", "Diferencia: la obra D tiene un lago quieto junto a las montañas azules."], "Semejanza: montañas con nieve. Diferencia: la obra D tiene lago"),
        w("Tomar una idea", "Te gustan las rayas en las mejillas de la máscara de la obra E. ¿Cómo las usas?", ["Tomo la idea de rayas en el rostro.", "Dibujo un gato con rayas de colores en las mejillas.", "Anoto: la idea vino de la obra E."], "Un gato con rayas de colores, inspirado en la obra E"),
    ],
    [
        m("Pensar que el arte de otros lugares es raro o menos importante.", "Se mira desde lo que ya conocemos.", "Pregunta qué materiales y formas tiene y mira con respeto."),
        m("Dibujar la misma máscara igual y decir que es mía.", "Se confunde copiar con inspirarse.", "Toma una idea y mézclala con una tuya."),
    ],
    [
        ex("Obra D tiene montañas azules con nieve y un lago. ¿Qué agua se ve en la obra?", "Un lago", "La descripción nombra un lago quieto."),
        ex("Obra E es una máscara de madera. ¿De qué material es?", "De madera", "El texto dice que la máscara es de madera."),
        ex("Obra F es una escultura de metal con forma de caballo. ¿Qué animal representa?", "Un caballo", "La descripción nombra el caballo."),
    ],
    [
        ex("¿Qué colores domina la obra D? A: azul y blanco. B: rojo y negro. C: verde y rosado.", "A", "Tiene montañas azules con nieve blanca."),
        ex("En la obra E, ¿qué hay en las mejillas?", "Rayas", "La máscara tiene ojos grandes y rayas en las mejillas."),
        ex("Una semejanza es algo que se parece. ¿La nieve en las montañas de la obra D y de los Andes es una semejanza o una diferencia?", "Una semejanza", "En ambos lugares hay montañas con nieve."),
    ],
    [
        arith("En tu dibujo inspirado en la obra E pones 2 rayas en cada mejilla. Tiene 2 mejillas. ¿Cuántas rayas dibujas?", "2 * 2", "Se multiplica 2 rayas por 2 mejillas."),
        ex("Comparas la obra F (metal, caballo pequeño) con un caballo de greda de Pomaire. ¿Qué es diferente: el material o el animal?", "El material", "Ambos son caballos, pero uno es de metal y el otro de greda."),
        ex("Ordena: A comparar con tu entorno, B mirar la obra con atención, C crear algo propio con una idea.", "B, A, C", "Primero se mira, luego se compara y al final se crea."),
    ],
    [
        ex("Mia dice: «El arte de otros lugares no me interesa porque no es de Chile». ¿Es una buena razón?", "No", "Mirar obras de otros lugares nos enseña formas nuevas de ver y de crear."),
        ex("Diego mira la máscara de la obra E y dice: «Es rara, no sirve». ¿Qué debería hacer en vez de eso?", "Observar sus materiales, formas y colores", "Mirar con atención y respeto permite entender mejor la obra."),
    ],
    [
        ex("Comparas las obras D y F: ¿qué tienen en común, si D es una pintura de montañas y F es un caballo de metal?", "Ambas son obras de arte", "No comparten material ni tema, pero las dos son obras creadas por artistas."),
        ex("Mezclas montañas con nieve de la obra D con rayas de colores de la obra E. ¿Cuántas ideas tomaste?", "2", "Tomaste una de cada obra."),
    ],
    ex("En clases hacen una «ventana al mundo». Tú pegas tu dibujo del lago y las montañas junto a una tarjeta que dice: «Me inspiré en la obra D». ¿Qué dato incluyó la tarjeta: la fuente o el precio?", "La fuente", "La tarjeta dice de qué obra tomaste la idea."),
    [
        ex("¿Cómo se llama una cosa que no se parece entre dos obras?", "Diferencia", "Eso es una diferencia."),
        ex("¿De qué material es la obra E?", "Madera", "Es una máscara de madera."),
        ex("Una máscara de madera hecha en otro continente, ¿es una obra del resto del mundo o una obra local de tu barrio?", "Del resto del mundo", "Las obras de otros continentes forman parte del arte universal."),
    ],
    task(
        "Elige UNA de las obras D, E o F descritas en este cuaderno. Anota una semejanza y una diferencia con algo de tu entorno (por ejemplo, un paisaje, un objeto o un animal). Crea un dibujo tuyo que tome UNA idea de la obra mezclada con algo de tu entorno. Escribe qué idea tomaste.",
        "Elegí la obra D. Semejanza: en Chile también hay montañas con nieve. Diferencia: la obra D tiene un lago quieto y yo vi un río. Dibujé un río entre montañas azules. Tomé el color azul de la obra D.",
        ["anota una semejanza y una diferencia", "toma una idea de la obra", "agrega algo de su entorno", "dice qué tomó"],
        ["una semejanza y una diferencia escritas", "dibujo propio", "una frase de fuente"],
        ["copiar la obra descrita", "decir que la obra es rara sin observarla"],
        "Reconoce la comparación hecha y pide que explique qué agregó de su entorno.",
    ),
    "Pregunta a alguien de tu familia si conoce una artesanía de otro lugar, y cuéntale qué material y colores tiene.",
    "Con ayuda de tu docente o de un adulto, mira una imagen real de una obra de otro continente. Anota de qué material es y qué colores tiene. Compara las obras D, E y F: ¿cuál te gusta más y qué elemento visual te atrae?",
)

# ================================================================ OA 02
# ---------------------------------------------------------------- Clase 1
lesson(
    OA2, 1,
    "Hoja, lápiz de mina y lápices de colores. Si lo deseas, una regla. Todo lo necesario está descrito en este cuaderno.",
    "Aprenderé a usar líneas verticales, horizontales, diagonales, en espiral y quebradas para dar movimiento y carácter a mis dibujos. Sirve para que un dibujo muestre calma, energía o giro.",
    ["Sé trazar líneas rectas y curvas.", "Conozco las palabras arriba, abajo, izquierda y derecha."],
    [
        "La línea es el elemento más simple del arte y puede tener distintas formas. La línea vertical va de arriba hacia abajo, como un poste. La línea horizontal va de lado a lado, como el horizonte. La línea diagonal está inclinada, como una escalera apoyada en una pared.",
        "La línea en espiral da vueltas alrededor de un centro, como un caracol. La línea quebrada tiene puntas y cambios de dirección, como un zigzag o un rayo. Cada línea da una sensación: la vertical parece firme y alta, la horizontal parece calma y descansada, la diagonal parece movimiento, la espiral parece giro y la quebrada parece energía.",
        "También cambia el carácter de una línea según cómo la dibujes. Puede ser gruesa o fina, fuerte o suave, larga o corta. Para producir una sensación, elige primero el tipo de línea. Por ejemplo, para dibujar un día de lluvia fuerte puedes usar muchas líneas diagonales finas.",
    ],
    [("línea vertical", "línea que va de arriba hacia abajo"), ("línea horizontal", "línea que va de lado a lado"), ("línea diagonal", "línea inclinada"), ("línea en espiral", "línea que da vueltas alrededor de un centro"), ("línea quebrada", "línea con puntas y cambios de dirección")],
    [
        w("Elegir líneas para un mar calmo", "Quieres dibujar un mar tranquilo. ¿Qué línea usas y cómo?", ["Para algo tranquilo elijo una línea horizontal.", "La dibujo larga, suave y fina.", "Repito varias líneas horizontales una sobre otra."], "Líneas horizontales largas y suaves"),
        w("Elegir líneas para una tormenta", "Quieres dibujar un rayo en una tormenta. ¿Qué línea usas?", ["Un rayo cambia de dirección con puntas.", "Uso una línea quebrada, gruesa y fuerte."], "Línea quebrada gruesa y fuerte"),
    ],
    [
        m("Llamar vertical a una línea que está inclinada.", "Se confunde cuánto se inclina la línea.", "Si va derecho de arriba a abajo es vertical; si está inclinada, es diagonal."),
        m("Usar líneas horizontales suaves para dibujar un rayo.", "No se piensa en la sensación que se quiere producir.", "Elige líneas quebradas para algo fuerte y con energía."),
    ],
    [
        ex("¿Cómo se llama la línea que va de lado a lado, como el horizonte?", "Línea horizontal", "Horizontal es la que va de un lado al otro."),
        ex("¿Cómo se llama la línea que da vueltas alrededor de un centro, como un caracol?", "Línea en espiral", "Las vueltas alrededor de un centro forman una espiral."),
        ex("Un poste de luz va derecho de arriba a abajo. ¿Qué línea lo dibuja?", "Línea vertical", "Vertical es la que va de arriba hacia abajo."),
    ],
    [
        ex("¿Qué sensación da una línea horizontal larga y suave? A: calma. B: susto. C: velocidad.", "A", "La horizontal se parece al descanso y a la calma."),
        ex("Una escalera apoyada en una pared está inclinada. ¿Qué línea la representa?", "Línea diagonal", "Diagonal es la línea inclinada."),
        ex("¿Cómo es una línea quebrada: tiene puntas o es perfectamente recta?", "Tiene puntas", "La quebrada cambia de dirección formando puntas."),
    ],
    [
        arith("Dibujas 3 líneas verticales y 2 líneas horizontales para formar una reja. ¿Cuántas líneas dibujaste?", "3 + 2", "Se suman las líneas de cada tipo."),
        ex("Quieres dibujar el humo que sube en vueltas. ¿Qué línea eliges: espiral o vertical recta?", "Espiral", "El humo que da vueltas se representa con una espiral."),
        ex("Ordena de más calma a más energía: A línea quebrada gruesa, B línea horizontal suave, C línea diagonal.", "B, C, A", "La horizontal da calma, la diagonal da movimiento y la quebrada gruesa da mucha energía."),
    ],
    [
        ex("Luz quiere dibujar una lluvia fuerte con líneas horizontales. ¿Es buena elección? Explica.", "No; mejor líneas diagonales", "Las horizontales dan calma y la lluvia fuerte cae con movimiento."),
        ex("Pía dice: «Una línea gruesa y una fina de la misma dirección dan la misma sensación». ¿Tiene razón?", "No", "El grosor también cambia el carácter de la línea."),
    ],
    [
        ex("Quieres que un dibujo de una casa se vea firme. Usas líneas verticales en las paredes y una horizontal en el suelo. ¿Cuántos tipos de línea usaste?", "2", "Usaste líneas verticales y horizontales."),
        ex("En el dibujo de la tormenta pones una línea quebrada para el rayo, líneas diagonales para la lluvia y una espiral para el viento. ¿Cuántos tipos de línea hay?", "3", "Hay quebrada, diagonal y espiral."),
    ],
    ex("Te piden decorar un cartel de una fiesta con mucha energía. ¿Qué línea eliges: quebrada gruesa o horizontal suave?", "Quebrada gruesa", "La quebrada gruesa da mucha energía."),
    [
        ex("¿Qué línea va de arriba hacia abajo?", "Vertical", "Esa es la definición de vertical."),
        ex("¿Qué línea parece un rayo?", "Quebrada", "El rayo cambia de dirección con puntas."),
        ex("Verdadero o falso: una línea inclinada es una línea diagonal.", "Verdadero", "La diagonal es la inclinada."),
    ],
    task(
        "Elige UNA sensación: calma, energía o giro. Dibuja una hoja con tres tipos de línea distintos que expresen esa sensación (por ejemplo: calma con horizontales suaves, energía con quebradas gruesas, giro con espirales). Escribe qué líneas usaste y por qué.",
        "Elegí energía. Usé líneas quebradas gruesas, diagonales fuertes y espirales pequeñas. Elegí esas porque cambian de dirección y se ven con movimiento.",
        ["usa al menos tres tipos de línea", "todas expresan la misma sensación", "explica su elección"],
        ["hoja con líneas", "una frase de explicación"],
        ["líneas sin relación con la sensación", "una sola línea repetida"],
        "Reconoce una línea bien elegida y pide que cambie el grosor o la fuerza de otra para mejorar la sensación.",
    ),
    "Camina por tu casa y encuentra tres líneas: una vertical, una horizontal y una diagonal. Di dónde las ves.",
    "Dibuja un paisaje solo con líneas y cambia el grosor de cada una. Compara qué sensación da cada tipo.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA2, 2,
    "Lápices de colores rojo, amarillo y azul (o témperas o acuarelas, si las tienes) y una hoja. Para mezclar con lápices, pinta una capa de un color y otra encima.",
    "Aprenderé a mezclar los colores primarios para formar los secundarios y a anotar cada mezcla. Sirve para obtener más colores con pocos materiales.",
    ["Conozco los colores rojo, amarillo y azul.", "Sé que algunos colores se mezclan."],
    [
        "Los colores primarios son rojo, amarillo y azul. Con ellos se pueden formar muchos otros colores. Cuando mezclas dos primarios distintos, obtienes un color secundario. Los secundarios son naranja, verde y violeta.",
        "Las mezclas son: rojo con amarillo da naranja. Amarillo con azul da verde. Azul con rojo da violeta. Si usas lápices, pinta una capa de un color y otra encima. Si usas pintura, mezcla en un plato o en una tapa limpia con un poco de cada color.",
        "Para registrar tu mezcla, haz un cuadro: dos cuadritos con los colores primarios y un tercero con el secundario. Escribe el nombre debajo. Si pones más de un color que de otro, el resultado cambia un poco de tono. Prueba y anota lo que ves.",
    ],
    [("color primario", "color que sirve para formar otros: rojo, amarillo y azul"), ("color secundario", "color que sale de mezclar dos primarios: naranja, verde y violeta"), ("mezcla", "unir dos colores para hacer uno nuevo"), ("tono", "qué tan claro u oscuro es un color"), ("muestrario", "cuadro con pruebas de colores")],
    [
        w("Hacer naranja", "Tienes rojo y amarillo. ¿Qué color secundario puedes hacer?", ["Mezclo rojo con amarillo.", "Pinto un cuadrito rojo, otro amarillo y uno con los dos juntos.", "El tercer cuadrito se ve naranja."], "Naranja"),
        w("Hacer verde", "Tienes amarillo y azul. ¿Qué color secundario haces?", ["Mezclo amarillo con azul.", "Anoto la mezcla en un muestrario.", "El resultado es verde."], "Verde"),
    ],
    [
        m("Pensar que rojo con azul da verde.", "Se confunden las mezclas.", "Recuerda: azul con rojo da violeta y azul con amarillo da verde."),
        m("Mezclar y no anotar nada.", "Se olvida qué colores usó.", "Haz un muestrario con los dos primarios y el secundario que salió."),
    ],
    [
        ex("¿Qué color sale de mezclar rojo y amarillo?", "Naranja", "Rojo con amarillo da naranja."),
        ex("¿Qué color sale de mezclar amarillo y azul?", "Verde", "Amarillo con azul da verde."),
        ex("¿Qué color sale de mezclar azul y rojo?", "Violeta", "Azul con rojo da violeta."),
    ],
    [
        ex("¿Cuáles son los tres colores primarios? A: rojo, amarillo y azul. B: verde, naranja y violeta. C: negro, blanco y gris.", "A", "Los primarios son rojo, amarillo y azul."),
        ex("¿Verde es un color primario o secundario?", "Secundario", "Sale de mezclar amarillo y azul."),
        ex("Quieres hacer violeta. ¿Qué dos primarios mezclas?", "Azul y rojo", "Azul con rojo da violeta."),
    ],
    [
        arith("Tienes 3 colores primarios. Mezclas cada color con cada uno de los otros dos, de a dos distintos. Tres mezclas posibles: rojo con amarillo, amarillo con azul y azul con rojo. ¿Cuántos colores secundarios puedes formar?", "1 + 1 + 1", "Cada mezcla da un secundario distinto."),
        ex("Quieres pintar una hoja verde y solo tienes amarillo y azul. ¿Qué haces?", "Mezclar amarillo con azul", "Esa mezcla da verde."),
        ex("Ordena: A anotar el resultado, B poner un primer color, C poner el segundo color encima.", "B, C, A", "Primero se pinta un color, luego el otro encima y al final se anota."),
    ],
    [
        ex("Ema mezcla rojo con azul y dice que le salió verde. ¿Está bien? Explica.", "No; sale violeta", "Rojo con azul da violeta, no verde."),
        ex("Lalo dice: «Con tres primarios se pueden hacer tres secundarios». ¿Tiene razón?", "Sí", "Las tres mezclas de a dos dan naranja, verde y violeta."),
    ],
    [
        ex("Tienes un muestrario con naranja, verde y violeta. ¿Qué color primario aparece en las mezclas de naranja y violeta, pero no en verde?", "Rojo", "El naranja lleva rojo y amarillo, el violeta lleva azul y rojo; el verde lleva amarillo y azul."),
        ex("Si mezclas un poquito de rojo con mucho amarillo, ¿qué color secundario obtienes, aunque se vea más amarillo?", "Naranja", "Siempre es rojo con amarillo, aunque cambie el tono."),
    ],
    ex("Quieres pintar una hoja de otoño con naranja y solo tienes rojo y amarillo. ¿Qué haces?", "Mezclar rojo con amarillo", "Esa mezcla da naranja."),
    [
        ex("Si mezclas pintura roja con pintura amarilla, ¿de qué color queda la mezcla?", "Naranja", "Es la mezcla del rojo con el amarillo."),
        ex("¿Violeta es primario o secundario?", "Secundario", "Se forma mezclando azul con rojo."),
        ex("¿Qué mezclas para formar verde?", "Amarillo y azul", "Esa mezcla da verde."),
    ],
    task(
        "Haz un muestrario con tres filas. Fila 1: rojo + amarillo = ___. Fila 2: amarillo + azul = ___. Fila 3: azul + rojo = ___. Pinta los dos primarios y la mezcla en cada fila y escribe el nombre del color. Después pinta una pequeña fruta, una flor o un animal usando uno de tus colores secundarios.",
        "Fila 1: rojo + amarillo = naranja. Fila 2: amarillo + azul = verde. Fila 3: azul + rojo = violeta. Pinté una mariposa violeta.",
        ["pinta los dos primarios y la mezcla en cada fila", "anota el nombre del color correcto", "usa un secundario en una pintura"],
        ["muestrario con tres filas", "pintura con un color secundario"],
        ["cambiar el nombre de las mezclas", "no pintar la mezcla"],
        "Reconoce las mezclas bien anotadas y pide que repita la que se confundió y compare con su registro.",
    ),
    "Encuentra en tu casa un objeto naranja, uno verde y uno violeta. Di qué dos primarios mezclarías para hacer cada color.",
    "Mezcla más de un color que de otro y anota qué cambió en el tono.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA2, 3,
    "Lápices de colores o témperas (amarillo, violeta, rojo, verde, azul y naranja) y una hoja. Usa los colores que tengas.",
    "Aprenderé a elegir colores que contrastan para destacar una forma o que se parecen para acercarlas. Sirve para que lo importante de mi dibujo se vea.",
    ["Conozco los colores primarios y secundarios.", "Sé que unos colores son claros y otros oscuros."],
    [
        "El contraste es la diferencia entre dos colores. Cuando dos colores son muy distintos, uno destaca sobre el otro. Por ejemplo, un círculo amarillo se ve mucho en un fondo violeta. En cambio, un círculo amarillo sobre un fondo amarillo claro casi no se nota.",
        "Algunos pares de colores contrastan mucho: rojo con verde, azul con naranja y amarillo con violeta. También contrastan los colores claros con los oscuros. Si usas colores parecidos, las formas se acercan y se ven juntas, como una familia.",
        "Los colores cálidos son el rojo, el naranja y el amarillo. Los colores fríos son el azul, el verde y el violeta. En un dibujo, los cálidos suelen parecer más cercanos y los fríos más lejanos. Elige tus colores según lo que quieras destacar, acercar o separar.",
    ],
    [("contraste", "diferencia fuerte entre dos colores"), ("destacar", "hacer que algo se note más"), ("colores cálidos", "rojo, naranja y amarillo"), ("colores fríos", "azul, verde y violeta"), ("colores parecidos", "colores que se ven casi iguales")],
    [
        w("Destacar una estrella", "Dibujas una estrella amarilla. ¿Qué fondo eliges para que se destaque?", ["Busco un color muy distinto al amarillo.", "El violeta contrasta con el amarillo.", "Pinto el fondo violeta."], "Fondo violeta"),
        w("Acercar dos formas", "Quieres que dos peces se vean juntos, como una familia. ¿Qué colores usas?", ["Elijo colores parecidos, como azul y verde.", "Así las dos formas se acercan."], "Colores parecidos, azul y verde"),
    ],
    [
        m("Pintar una estrella amarilla sobre un fondo amarillo claro y esperar que se vea.", "No se piensa en el contraste.", "Elige un color muy distinto para el fondo."),
        m("Usar solo colores parecidos y pensar que todo se va a destacar.", "Se confunde acercar con destacar.", "Para destacar, usa colores muy distintos o claros y oscuros."),
    ],
    [
        ex("¿Qué colores son cálidos: rojo, naranja y amarillo, o azul, verde y violeta?", "Rojo, naranja y amarillo", "Esos se llaman cálidos."),
        ex("¿Qué colores son fríos: azul, verde y violeta, o rojo, naranja y amarillo?", "Azul, verde y violeta", "Esos se llaman fríos."),
        ex("Un círculo amarillo sobre fondo violeta, ¿se destaca mucho o poco?", "Mucho", "Amarillo y violeta contrastan fuerte."),
    ],
    [
        ex("¿Qué es el contraste? A: la diferencia entre dos colores. B: un lápiz. C: un color nuevo.", "A", "El contraste mide qué tan distintos son dos colores."),
        ex("Quieres que un cuadrado azul destaque. ¿Qué fondo contrasta más: naranja o azul claro?", "Naranja", "Azul y naranja forman un par que contrasta."),
        ex("Para acercar dos formas, ¿usas colores muy distintos o colores parecidos?", "Colores parecidos", "Colores parecidos hacen que las formas se vean juntas."),
    ],
    [
        arith("Pintas 4 flores rojas sobre un fondo verde y 3 flores azules sobre un fondo naranja. ¿Cuántas flores pintaste en total?", "4 + 3", "Se suman las flores de ambos fondos."),
        ex("Quieres que una luna amarilla destaque en un cielo. ¿Usas cielo violeta o cielo amarillo claro?", "Cielo violeta", "El violeta contrasta con el amarillo."),
        ex("Ordena de menos a más contraste con un círculo amarillo: A fondo violeta, B fondo amarillo claro, C fondo naranja.", "B, C, A", "Amarillo claro casi no contrasta, naranja contrasta poco y violeta mucho."),
    ],
    [
        ex("Tomás pinta un conejo gris sobre fondo gris claro. Dice que no se ve. ¿Qué podría cambiar?", "El fondo, a un color muy distinto", "Un fondo con más contraste hace que el conejo se destaque."),
        ex("Eva dice: «Si pinto todo de colores fríos, parecerán más cercanos». ¿Tiene razón?", "No", "Los fríos suelen parecer más lejanos; los cálidos más cercanos."),
    ],
    [
        ex("Quieres un dibujo donde una casa roja parezca cerca y las montañas parezcan lejos. ¿Qué colores usas en las montañas: cálidos o fríos?", "Fríos", "Los fríos suelen parecer más lejanos."),
        ex("Un cartel tiene letras violeta sobre un fondo amarillo. ¿Tiene mucho o poco contraste?", "Mucho", "Violeta y amarillo son un par que contrasta."),
    ],
    ex("Te piden hacer un cartel de «cuidemos el parque» con letras que se lean desde lejos. ¿Eliges letras amarillas sobre fondo violeta o letras amarillo claro sobre fondo blanco?", "Letras amarillas sobre fondo violeta", "Hay mucho contraste y se leen mejor."),
    [
        ex("¿Qué colores contrastan con el rojo?", "Verde", "Rojo y verde son un par que contrasta."),
        ex("¿Un color cálido parece más cercano o más lejano?", "Más cercano", "Los cálidos suelen parecer más cercanos."),
        ex("Si quieres destacar algo, ¿usas colores muy distintos o parecidos?", "Muy distintos", "El contraste hace que se note."),
    ],
    task(
        "Elige UNA forma: una estrella, una hoja o un pez. Dibújala tres veces. En la primera, sobre un fondo de color muy distinto. En la segunda, sobre un fondo de color parecido. En la tercera, sobre un fondo claro si la forma es oscura, o sobre un fondo oscuro si la forma es clara. Escribe cuál se destaca más y por qué.",
        "Elegí la estrella amarilla. En la primera la pinté sobre violeta y se ve mucho. En la segunda, sobre amarillo claro y casi desaparece. En la tercera, sobre azul oscuro y también se ve bien. Se destaca más la primera porque los colores son muy distintos.",
        ["hace tres versiones", "una tiene contraste fuerte y otra colores parecidos", "explica cuál se destaca y por qué"],
        ["tres dibujos de la misma forma", "una frase de explicación"],
        ["no hay diferencia entre las tres versiones", "elegir colores parecidos esperando destacar"],
        "Reconoce la versión con mejor contraste y pide que explique qué haría para acercar la forma al fondo.",
    ),
    "Mira tu ropa o tu cuaderno y busca dos colores que contrasten mucho y dos que se parezcan. Dilo en voz alta.",
    "Dibuja el mismo paisaje con colores cálidos y luego con colores fríos. Compara qué cambió.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA2, 4,
    "Hoja, lápices de colores y, si quieres, papel de colores y tijera de punta roma con ayuda de un adulto. Las formas están descritas en este cuaderno.",
    "Aprenderé a construir imágenes combinando formas geométricas como el círculo, el cuadrado, el rectángulo y el triángulo. Sirve para dibujar casi cualquier cosa con formas simples.",
    ["Reconozco círculo, cuadrado y triángulo.", "Sé contar hasta 20."],
    [
        "Las formas geométricas son figuras con medidas y bordes regulares. El círculo es redondo y no tiene esquinas. El cuadrado tiene 4 lados iguales y 4 esquinas. El rectángulo tiene 4 lados y 4 esquinas, con dos lados largos y dos cortos. El triángulo tiene 3 lados y 3 esquinas.",
        "Con formas geométricas puedes construir imágenes. Una casa puede hacerse con un cuadrado para la pared, un triángulo para el techo, un rectángulo para la puerta y un cuadrado pequeño para la ventana. Un robot puede tener rectángulos en el cuerpo y círculos en los ojos.",
        "Para construir una imagen, piensa primero qué formas necesitas. Dibuja las grandes primero y luego las pequeñas. Puedes poner unas encima de otras para formar partes nuevas. Cambia el tamaño y los colores de las formas para darle carácter a tu imagen.",
    ],
    [("forma geométrica", "figura con bordes regulares, como círculo o cuadrado"), ("lado", "cada línea que forma el borde de una figura"), ("esquina", "lugar donde se juntan dos lados"), ("rectángulo", "figura de 4 lados con dos largos y dos cortos"), ("triángulo", "figura de 3 lados y 3 esquinas")],
    [
        w("Construir una casa", "Quieres dibujar una casa con un cuadrado, un triángulo y un rectángulo. ¿Dónde va cada forma?", ["El cuadrado es la pared.", "El triángulo va arriba como techo.", "El rectángulo es la puerta, dentro del cuadrado."], "Cuadrado: pared. Triángulo: techo. Rectángulo: puerta"),
        w("Construir un robot", "Quieres un robot con un rectángulo grande de cuerpo, dos círculos de ojos y un cuadrado de cabeza. ¿Cuántas formas usas?", ["Cuento el rectángulo: 1.", "Cuento los dos círculos: 2.", "Cuento el cuadrado: 1.", "Sumo 1 + 2 + 1."], "4 formas"),
    ],
    [
        m("Contar 5 lados en un triángulo.", "Se cuentan las esquinas y los lados juntos.", "Cuenta solo los lados: el triángulo tiene 3."),
        m("Decir que un círculo tiene 4 esquinas.", "Se confunde con el cuadrado.", "El círculo es redondo y no tiene esquinas."),
    ],
    [
        ex("Una señal de tránsito tiene forma de triángulo. ¿Cuántos lados tiene esa señal?", "3", "Triángulo quiere decir tres lados."),
        ex("¿Cuántas esquinas tiene un cuadrado?", "4", "El cuadrado tiene cuatro esquinas."),
        ex("¿Qué forma geométrica no tiene esquinas: círculo o rectángulo?", "Círculo", "El círculo es redondo y no tiene esquinas."),
    ],
    [
        ex("¿Qué forma sirve para hacer el techo de una casa simple? A: triángulo. B: círculo. C: espiral.", "A", "El triángulo con punta arriba parece un techo."),
        ex("Un robot tiene dos círculos de ojos. ¿Cuántos ojos tiene?", "2", "Hay un círculo por cada ojo."),
        ex("¿En qué se diferencia un cuadrado de un rectángulo normal?", "El cuadrado tiene los 4 lados iguales", "El rectángulo tiene dos lados largos y dos cortos."),
    ],
    [
        arith("Tu casa tiene 1 cuadrado de pared, 1 triángulo de techo, 1 rectángulo de puerta y 2 cuadrados pequeños de ventana. ¿Cuántas formas usaste?", "1 + 1 + 1 + 2", "Se suman todas las formas de la casa."),
        arith("Dibujas 3 triángulos y cada uno tiene 3 lados. ¿Cuántos lados dibujaste en total?", "3 * 3", "Cada uno de los 3 triángulos tiene 3 lados."),
        ex("Quieres dibujar un sol con una forma. ¿Eliges círculo o triángulo?", "Círculo", "El sol se ve redondo."),
    ],
    [
        ex("Pedro dice que un rectángulo tiene 3 lados. ¿Tiene razón?", "No", "El rectángulo tiene 4 lados y 4 esquinas."),
        ex("Un dibujo tiene 6 círculos, 2 cuadrados y 1 triángulo. Ana dice que hay 8 formas. ¿Se equivocó?", "Sí; hay 9", "6 + 2 + 1 = 9."),
    ],
    [
        ex("Construyes un gato con un círculo grande de cuerpo, un círculo pequeño de cabeza y dos triángulos de orejas. ¿Cuántas formas diferentes usas: círculos y triángulos?", "2", "Hay dos tipos de formas: círculos y triángulos."),
        ex("En ese mismo gato, ¿cuántas formas hay en total, contando cada círculo y cada triángulo?", "4", "Hay 2 círculos y 2 triángulos."),
    ],
    ex("Te piden hacer un cartel de bienvenida con un barco hecho con formas. Usas 1 rectángulo grande de casco, 2 triángulos de velas y 3 círculos de ventanas. ¿Cuántas formas hay?", "6", "Se suma 1 + 2 + 3."),
    [
        ex("¿Qué forma tiene 3 lados?", "Triángulo", "Triángulo = tres lados."),
        ex("Verdadero o falso: el círculo tiene esquinas.", "Falso", "El círculo es redondo."),
        ex("¿Qué forma sirve para una puerta: rectángulo o círculo?", "Rectángulo", "Una puerta suele ser alargada."),
    ],
    task(
        "Elige UNA de estas imágenes: un barco, un animal o una casa. Constrúyela solo con círculos, cuadrados, rectángulos y triángulos. Usa al menos tres formas distintas. Escribe cuántas formas usaste en total y de cuáles.",
        "Elegí un barco. Usé 1 rectángulo grande de casco, 2 triángulos de velas y 3 círculos de ventanas. En total 6 formas.",
        ["usa al menos tres formas distintas", "reconoce la imagen", "anota cuántas formas usó"],
        ["dibujo con formas", "una frase con el total de formas"],
        ["no usar formas geométricas regulares", "contar mal las formas"],
        "Reconoce la forma mejor aprovechada y pide que cuente de nuevo para comprobar el total.",
    ),
    "Busca en tu casa un objeto con forma de círculo, otro de rectángulo y otro de triángulo. Di cuáles son.",
    "Repite tu dibujo cambiando solo el tamaño de las formas. Anota qué cambió.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA2, 5,
    "Hoja, lápiz de mina y lápices de colores rojo, amarillo, azul, naranja, verde y violeta. Usa los colores que tengas.",
    "Aprenderé a juntar línea, color y forma en un solo dibujo, tomando decisiones para cada uno. Sirve para planificar mis dibujos y revisar si resultan como quería.",
    ["Conozco los tipos de línea: vertical, horizontal, diagonal, espiral y quebrada.", "Sé combinar colores y formas."],
    [
        "Una composición junta varios elementos del lenguaje visual en un mismo trabajo. Los tres que aprendiste son la línea, el color y la forma. Cada uno tiene una tarea. La línea da recorrido y sensación. El color destaca o acerca. La forma construye la imagen.",
        "Para planificar tu composición, elige primero qué quieres expresar, por ejemplo calma o energía. Luego elige una línea, dos o tres colores y dos o tres formas que ayuden. Si quieres calma, usa líneas horizontales, colores fríos y formas redondas. Si quieres energía, usa líneas quebradas, colores cálidos y formas con puntas. Si quieres alegría, usa líneas diagonales, colores cálidos y círculos pequeños.",
        "Cuando termines, revisa con una lista. ¿Usé al menos un tipo de línea elegido? ¿Mis colores contrastan donde quiero destacar? ¿Reconozco las formas? Si algo no funciona, cámbialo y anota qué cambiaste. Revisar también es parte del trabajo del artista.",
    ],
    [("composición", "la manera de organizar los elementos en una obra"), ("lenguaje visual", "los elementos con los que comunicamos con imágenes: línea, color y forma"), ("decisión", "elección que hago para lograr un efecto"), ("planificar", "pensar y ordenar antes de hacer"), ("revisar", "mirar el trabajo para ver si cumplió lo que quería")],
    [
        w("Planificar una composición de calma", "Quieres expresar calma. ¿Qué eliges para línea, color y forma?", ["Línea: horizontal y suave.", "Color: azul y verde, que son fríos.", "Forma: círculos."], "Línea horizontal, colores fríos y formas redondas"),
        w("Planificar una composición de energía", "Quieres expresar energía. ¿Qué eliges?", ["Línea: quebrada y gruesa.", "Color: rojo, naranja y amarillo.", "Forma: triángulos."], "Línea quebrada, colores cálidos y triángulos"),
    ],
    [
        m("Hacer el dibujo sin elegir antes qué quiero expresar.", "No se planifica y las decisiones no se conectan.", "Elige primero la sensación y luego línea, color y forma que la ayuden."),
        m("Terminar el dibujo sin mirar si funciona.", "Se olvida revisar.", "Revisa con la lista y cambia lo que no funcione."),
    ],
    [
        ex("¿Cuáles son los tres elementos del lenguaje visual que usas en esta clase?", "Línea, color y forma", "Son los que se combinan en la composición."),
        ex("Quieres expresar calma. ¿Qué línea eliges: horizontal suave o quebrada gruesa?", "Horizontal suave", "La horizontal suave da calma."),
        ex("¿Qué es planificar: pensar antes de hacer o hacer sin pensar?", "Pensar antes de hacer", "Planificar es ordenar las ideas antes de comenzar."),
    ],
    [
        ex("Para energía, ¿qué colores eliges? A: rojo, naranja y amarillo. B: azul y verde. C: gris claro.", "A", "Los colores cálidos dan energía."),
        ex("Una composición tiene líneas horizontales, colores azul y verde y círculos. ¿Qué expresa: calma o energía?", "Calma", "Esos elementos dan sensación de tranquilidad."),
        ex("Revisar tu trabajo, ¿es parte del proceso o no es necesario?", "Es parte del proceso", "Revisar permite mejorar el trabajo."),
    ],
    [
        arith("Tu composición tiene 3 líneas quebradas, 2 triángulos y 4 círculos pequeños. ¿Cuántos elementos tiene?", "3 + 2 + 4", "Se suman líneas, triángulos y círculos."),
        ex("Quieres que tu composición exprese energía y que un triángulo amarillo destaque. ¿Qué fondo eliges: violeta o amarillo claro?", "Violeta", "El violeta contrasta con el amarillo."),
        ex("Ordena: A revisar con la lista, B hacer el dibujo, C elegir qué quiero expresar, D elegir línea, color y forma.", "C, D, B, A", "Se decide la intención, se eligen los elementos, se hace y se revisa."),
    ],
    [
        ex("Una composición quiere expresar calma pero usa líneas quebradas gruesas y colores rojos. ¿Qué no funciona?", "Las líneas y los colores dan energía", "Contradicen la sensación de calma."),
        ex("Pía dice: «Si cambio una cosa, todo mi dibujo queda mal». ¿Tiene razón?", "No", "Cambiar un elemento y revisar permite mejorar sin empezar de nuevo."),
    ],
    [
        ex("Tu composición de energía tiene líneas quebradas, rojo y naranja, y triángulos. ¿Qué elemento podrías cambiar para que una forma destaque aún más?", "El color del fondo", "Un fondo con contraste fuerte hace que la forma se note."),
        ex("En tu composición hay 2 líneas, 3 colores y 4 formas. ¿Cuántos elementos distintos del lenguaje visual aparecen: línea, color y forma?", "3", "Aparecen tres tipos de elemento."),
    ],
    ex("Debes hacer una tarjeta para felicitar a alguien alegre. Eliges líneas diagonales, colores cálidos y círculos pequeños. ¿Qué sensación quieres expresar?", "Alegría y energía", "Esos elementos dan sensación de movimiento y animación."),
    [
        ex("¿Qué haces antes de empezar a dibujar tu composición?", "Planifico", "Primero se piensa qué expresar."),
        ex("¿Qué elemento da recorrido y sensación?", "La línea", "La línea marca recorrido."),
        ex("Verdadero o falso: revisar es parte del trabajo del artista.", "Verdadero", "Revisar ayuda a mejorar."),
    ],
    task(
        "Elige UNA sensación: calma, energía o alegría. Planifica y dibuja una composición con al menos un tipo de línea, tres colores y dos formas. Antes de empezar, escribe qué elegiste para línea, color y forma. Al terminar, revisa con esta lista: ¿la línea ayuda?, ¿el color contrasta donde quiero destacar?, ¿se reconocen las formas? Anota un cambio que hiciste.",
        "Elegí calma. Línea: horizontales suaves. Colores: azul, verde y violeta. Formas: círculos y cuadrados. Revisé y cambié un fondo muy oscuro por uno más claro para que los círculos se vieran.",
        ["planifica antes de dibujar", "usa línea, color y forma", "revisa con la lista", "anota un cambio"],
        ["plan escrito", "dibujo", "una frase sobre el cambio"],
        ["no planificar", "no revisar", "elegir elementos que contradicen la sensación"],
        "Reconoce una decisión que ayudó y pide que explique qué cambiaría para reforzar la sensación elegida.",
    ),
    "Dibuja una mini composición con una sensación y pregunta a alguien de tu casa cuál crees que es. Anota si adivinó.",
    "Haz la misma composición con la sensación contraria y compara qué decisiones cambiaste.",
)
