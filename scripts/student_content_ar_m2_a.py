"""Cuaderno del estudiante de 2.º medio Artes Visuales: AR2M OA 01 (proyectos visuales sobre problemáticas sociales y juveniles)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "AR2M OA 01"


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
    "Hojas, lápiz y lápices de colores. Las fichas de las manifestaciones de ejemplo están escritas en esta clase; no necesitas buscar ni fotografiar nada.",
    "Aprenderé a observar una manifestación visual sobre una problemática social o juvenil mirando su contexto, su lenguaje visual y su propósito. Sirve para valorarla con razones y no solo con gusto.",
    ["Sé leer un espacio público con contexto, lenguaje visual y propósito.", "Sé que una opinión no es lo mismo que un rasgo que se ve."],
    [
        "Una problemática social es una situación que afecta a muchas personas de una comunidad, como la basura en una cancha, el ruido en un barrio o la falta de lugares para juntarse. Una manifestación visual es una imagen hecha para mostrar esa situación: un afiche, un mural o una intervención. Una intervención es una pieza o acción que cambia un lugar por un tiempo. Para valorarla miro tres cosas: el contexto (dónde y para quién está), el lenguaje visual (cómo está hecha) y el propósito (qué busca provocar).",
        "En el espacio público el lugar también comunica. El mismo afiche dice cosas distintas sobre un lavamanos que en un paradero muy concurrido. Importan la ubicación, la escala (el tamaño comparado con quien mira), el tiempo que una persona puede detenerse a mirar y lo que rodea a la pieza. Si el texto debe leerse de lejos, las letras deben ser más grandes; si la persona espera diez minutos, puede leer un mensaje más largo.",
        "Una valoración crítica no es decir «me gusta». Primero describo rasgos que cualquiera puede comprobar, luego interpreto con verbos como «podría sugerir» y al final doy un juicio apoyado en un criterio, que es la razón con que juzgo. Por ejemplo: «se lee desde lejos porque las letras son grandes y contrastan con el fondo». Hablo de situaciones y no ridiculizo a personas reales. Si un tema me afecta, lo converso con una persona adulta de confianza.",
    ],
    [("problemática social", "situación que afecta a muchas personas de una comunidad"), ("manifestación visual", "imagen hecha para mostrar o provocar algo, como un afiche o un mural"), ("intervención", "pieza o acción que cambia un lugar por un tiempo"), ("escala", "tamaño de algo comparado con quien lo mira"), ("criterio", "razón con la que se juzga una manifestación")],
    [
        w("Leer una ficha", "Ficha de ejemplo, afiche «Agua que no vuelve»: fondo azul oscuro; una gota blanca muy grande al centro; texto «Cierra la llave» en letras blancas gruesas; pegado a la altura de los ojos sobre los lavamanos de los baños de un liceo. Separa contexto, lenguaje visual y propósito probable.", ["Contexto: los baños de un liceo, donde estudiantes se lavan las manos.", "Lenguaje visual: fondo azul oscuro, gota blanca grande y letras gruesas.", "Propósito probable: lograr que quien se lava las manos cierre la llave."], "Contexto: baños del liceo; lenguaje visual: azul, gota blanca, letras gruesas; propósito: que se cierre la llave"),
        w("Efecto del lugar", "El mismo afiche, con letras de 2 cm de alto, se pega en un paradero muy concurrido y la gente pasa a 5 metros. ¿Qué rasgo falla en ese lugar?", ["Dato del lugar: se mira desde lejos y de paso.", "Rasgo que falla: las letras de 2 cm son pequeñas para esa distancia.", "Ajuste: agrandar el texto y dejar una frase muy corta."], "Falla el tamaño de las letras; hay que agrandarlas y acortar la frase"),
    ],
    [
        m("Escribir «el mural es feo» y creer que eso es observar.", "Una opinión no se puede comprobar mirando la pieza.", "Anota rasgos visibles, como «las siluetas son negras sobre fondo azul», y deja el juicio para el final con un criterio."),
        m("Mirar solo la imagen y olvidar el lugar donde está.", "La misma imagen funciona distinto en un baño que en una calle.", "Pregunta siempre quién la ve, desde dónde y por cuánto tiempo."),
    ],
    [
        ex("En Artes Visuales, ¿qué es una intervención en el espacio público? A. Una pieza o acción que cambia un lugar por un tiempo B. Un cuadro guardado en una sala cerrada C. Una pintura con marco dorado.", "A", "Una intervención actúa sobre un lugar; las otras opciones describen obras que no cambian el espacio."),
        ex("Del afiche «Agua que no vuelve», el dato «está pegado sobre los lavamanos de un liceo», ¿es de contexto o de lenguaje visual?", "De contexto", "Dice dónde está y quién lo ve, no cómo está hecho."),
        ex("Datos del afiche: 1) fondo azul oscuro, 2) pegado en los baños de un liceo, 3) letras blancas gruesas, 4) lo ven estudiantes al lavarse las manos. ¿Cuántos son de lenguaje visual?", "2", "El fondo azul y las letras blancas gruesas son rasgos de cómo está hecho; los otros dos son de contexto."),
    ],
    [
        ex("¿Cuál describe una problemática social? A. Basura acumulada en la cancha del barrio que usan cientos de jóvenes B. Una paleta de colores azul y blanca C. Un marco de madera.", "A", "Es una situación que afecta a una comunidad; las otras opciones son rasgos de una imagen."),
        ex("Un afiche con letras de 2 cm de alto se pegará en un paradero donde la gente pasa a 5 metros. ¿Qué cambio responde al contexto? A. Agrandar las letras y acortar la frase B. Hacer las letras más pequeñas para que quepa más texto.", "A", "A más distancia se necesita texto más grande y breve."),
        ex("El afiche muestra una gota blanca grande y dice «Cierra la llave». ¿Cuál es su propósito más probable? A. Que quien se lava las manos cierre la llave B. Mostrar que el liceo tiene baños nuevos.", "A", "El mensaje es un llamado a actuar en ese lugar."),
    ],
    [
        ex("¿Cuál es una interpretación bien escrita del afiche? A. «La gota gigante podría sugerir que cada pequeña pérdida de agua cuenta» B. «La gota es blanca y está al centro».", "A", "Propone un significado con «podría»; la otra frase solo describe."),
        ex("En el muro de la cancha, quienes miran están a 15 m. ¿Qué pieza se leerá mejor por su escala? A. El mural de 12 m de largo con letras amarillas grandes B. Un afiche tamaño carta con el mismo texto en letras de 1 cm.", "A", "Un tamaño grande en relación con la distancia permite leer; el afiche carta queda demasiado pequeño a 15 m."),
        ex("Una compañera escribe sobre el mural «Cancha de todos»: «es feo». ¿Cuál lo convierte en una descripción observable? A. «Las siluetas son negras sobre un fondo azul» B. «Es bastante feo y aburrido».", "A", "Nombra rasgos que cualquiera puede comprobar."),
    ],
    [
        ex("El afiche del agua se pega en el techo de un pasillo, donde nadie mira hacia arriba. ¿Qué pierde? A. Que su mensaje llegue a quien debe verlo B. Nada, porque el mensaje funciona igual en cualquier lugar.", "A", "El lugar impide que el público lo vea; el color no cambia."),
        ex("Un grupo quiere pintar un mural sobre la basura en el muro de una cancha. ¿Qué debe hacer primero? A. Pedir permiso a quien administra el muro B. Pintarlo un fin de semana, cuando nadie lo vea.", "A", "Una intervención en un lugar público necesita autorización; hacerlo sin permiso daña el espacio."),
    ],
    [
        ex("Dos manifestaciones de ejemplo sobre el ruido en un barrio: X es un afiche pequeño dentro de un buzón; Y es un mural de 6 m de largo en una plaza con mucho tránsito. El propósito es llegar a muchas personas que pasan caminando. ¿Cuál es más pertinente?", "Y, el mural en la plaza", "Lo verá más gente al pasar; el afiche dentro del buzón casi no se ve."),
        ex("Frase: «El mural se lee desde lejos porque las letras amarillas contrastan con el fondo azul». ¿Cuál es el criterio de ese juicio? A. El contraste entre colores B. Que el mural es muy grande.", "A", "La razón del juicio es el contraste, que se puede comprobar mirando."),
    ],
    ex("El centro de estudiantes quiere un afiche contra la basura en el patio y lo pegará junto al kiosco, donde se hace fila cerca de diez minutos. ¿Qué rasgo del contexto conviene aprovechar? A. Que hay tiempo para leer un mensaje un poco más largo B. Que nadie pasa por ahí.", "A", "La fila da minutos de lectura, así que el mensaje puede tener dos o tres líneas."),
    [
        ex("¿Qué tres cosas se miran de una manifestación visual en esta clase?", "Contexto, lenguaje visual y propósito", "Juntas explican dónde está, cómo está hecha y para qué."),
        ex("Verdadero o falso: «me gusta» es un criterio para valorar una manifestación visual.", "Falso", "Un criterio es una razón comprobable, como la legibilidad."),
        ex("¿Qué debe hacer un grupo antes de intervenir un muro público?", "Pedir permiso", "Así el trabajo es legal y cuida el espacio."),
    ],
    task(
        "Elige UNA manifestación de ejemplo. A) Afiche «Agua que no vuelve»: fondo azul oscuro, gota blanca grande, texto «Cierra la llave», sobre los lavamanos de un liceo. B) Mural «Cancha de todos»: 12 m de largo, siluetas negras de personas de varias edades jugando sobre fondo azul, letras amarillas, en el muro de una cancha de barrio, con permiso. C) Pizarra comunitaria en un paradero: una cartulina grande con la pregunta «¿Qué le falta a tu barrio?» y lápices atados con cordel. Escribe una ficha con contexto, dos rasgos de lenguaje visual y un propósito; agrega una interpretación con «podría» y un juicio apoyado en un criterio.",
        "Elegí la B. Contexto: muro de una cancha de barrio, lo ven quienes juegan y pasan. Rasgos: siluetas negras sobre fondo azul; letras amarillas grandes. Propósito: invitar a compartir la cancha. Interpretación: las siluetas de varias edades podrían sugerir que la cancha es de todos. Juicio: se lee desde lejos porque el amarillo contrasta con el azul.",
        ["separa contexto, lenguaje visual y propósito", "escribe una interpretación con «podría»", "apoya un juicio en un criterio comprobable", "no ridiculiza a personas"],
        ["ficha de observación", "interpretación y juicio con criterio"],
        ["escribir opiniones como si fueran rasgos", "olvidar el lugar donde está la pieza"],
        "Pregunta qué rasgo respalda su juicio y qué parte de su ficha es una descripción y cuál una interpretación.",
    ),
    "Mira un letrero, afiche o mural de tu barrio por un minuto y di en voz alta dos rasgos visibles y para quién parece hecho.",
    "Explica con tres frases cómo cambiaría el mensaje del afiche del agua si se pegara en un paradero en vez de en un baño.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA1, 2,
    "Hojas, lápiz, un trozo de cartón y papel de reciclaje limpio. Los referentes y materiales están descritos en esta clase; no necesitas buscarlos.",
    "Aprenderé a explorar materiales y referentes para una manifestación en el espacio público y a elegir según el lugar y el mensaje. Sirve para que mis decisiones tengan una razón y no copien a nadie.",
    ["Sé observar contexto, lenguaje visual y propósito.", "Sé que no se interviene un lugar sin permiso."],
    [
        "La materialidad son los materiales de una pieza y lo que comunican. Para el espacio público comparo cuatro criterios. Durabilidad: cuánto resiste sol y lluvia. Reversibilidad: si puedo retirarla sin dañar el lugar. Legibilidad: si se lee desde la distancia del público. Acceso: si consigo el material sin gastar mucho. Un afiche en papel es barato y fácil de retirar, pero se arruina con la lluvia. La tiza sobre el suelo se borra sola. Un esténcil es una plantilla de cartón recortada que permite repetir una forma con pintura al agua.",
        "Un referente es una obra que observo para aprender de ella. No la copio: tomo un recurso, como el contraste entre letras claras y fondo oscuro, y lo transformo cambiando al menos dos decisiones, por ejemplo el tema, la composición, el color o el material. Siempre anoto la procedencia: quién la hizo, dónde está y qué sé con certeza. Si no estoy seguro de un dato, escribo «dato por confirmar».",
        "Para probar materiales uso restos limpios: cartón, papel, tapas y témpera. Hago una muestra pequeña de cada uno y la comparo con los criterios. Tomo decisiones por el lugar y el mensaje, no por moda. Trabajo con tijeras de punta redonda y sin productos químicos. Solo uso imágenes propias o autorizadas y sin rostros de personas que no hayan dado permiso.",
    ],
    [("materialidad", "materiales de una pieza y lo que comunican"), ("durabilidad", "capacidad de resistir el sol, la lluvia y el uso"), ("reversibilidad", "posibilidad de retirar una pieza sin dañar el lugar"), ("esténcil", "plantilla recortada para repetir una forma con pintura"), ("referente", "obra que se observa para aprender de ella sin copiarla")],
    [
        w("Elegir material para un paradero", "Quieres difundir por una semana un mensaje sobre el reciclaje en un paradero techado y sin lluvia, y debes retirarlo sin dañar el lugar. Comparas papel pegado con cinta removible y pintura directa sobre el muro. ¿Cuál eliges?", ["Reversibilidad: la cinta se retira sin dañar; la pintura directa deja huella.", "Durabilidad: una semana sin lluvia basta para el papel.", "Decisión: papel con cinta removible."], "Papel con cinta removible, porque dura la semana y se retira sin dañar"),
        w("Transformar un referente", "Referente de ejemplo: un afiche con letras blancas sobre fondo negro que invita a donar útiles escolares. Tu tema es cuidar una plaza. ¿Cómo tomas el recurso sin copiar?", ["Recurso: letras claras sobre fondo oscuro para lograr contraste.", "Cambios propios: otro tema, otra frase y una silueta de árbol.", "Procedencia: anoto que el recurso viene del afiche de ejemplo."], "Letras claras sobre fondo oscuro, con tema, frase e imagen propios y la procedencia anotada"),
    ],
    [
        m("Elegir el material por lo que se ve bonito en una foto.", "No considera si dura, si se retira o si se lee desde la distancia.", "Compara al menos dos criterios de uso antes de decidir."),
        m("Cambiar solo el color de un referente y presentarlo como propio.", "La composición y la idea siguen siendo de otra persona.", "Cambia al menos dos decisiones y anota la procedencia."),
    ],
    [
        ex("En Artes Visuales, ¿qué es la reversibilidad de una pieza en el espacio público? A. Poder retirarla sin dañar el lugar B. Que se pueda dar vuelta C. Que dure muchos años.", "A", "Reversible significa que no deja daño al retirarla."),
        ex("Una plantilla de cartón recortada que sirve para repetir una forma con pintura al agua, ¿cómo se llama?", "Esténcil", "Esa es la definición de esténcil."),
        ex("La tiza sobre una vereda se borra sola con el tiempo y la lluvia. ¿Qué criterio de material cumple muy bien? A. Reversibilidad B. Durabilidad.", "A", "Se borra sin dañar el suelo, pero no dura: cumple con la reversibilidad."),
    ],
    [
        ex("Un mensaje debe verse todo el mes bajo sol y lluvia en una reja. ¿Qué material tiene el mayor problema de durabilidad? A. Papel común pegado B. Tela gruesa con letras de pintura para exterior.", "A", "El papel común se arruga y se deshace con la lluvia."),
        arith("Un grupo de ejemplo compra 4 pliegos de papel a $500 cada uno y 2 témperas a $1.000 cada una. ¿Cuánto gasta en total?", "4 * 500 + 2 * 1000", "Se suma lo gastado en papel y en témperas.", " pesos"),
        ex("Un referente de ejemplo usa letras blancas sobre fondo negro. ¿Cuál es una transformación válida? A. Tomar el contraste claro-oscuro y cambiar tema, frase e imagen B. Copiar el afiche igual y cambiarle la firma.", "A", "Se conserva un recurso y se cambian varias decisiones propias."),
    ],
    [
        ex("Tienes 20 minutos para un mensaje en una pared del colegio con autorización, y debe poder repetirse en seis lugares iguales. ¿Qué técnica conviene? A. Esténcil, porque repite la forma rápido B. Dibujar cada versión a mano con detalles distintos.", "A", "La plantilla permite repetir la misma forma sin rehacerla."),
        ex("Una muestra de cartón pintado con témpera se deforma al pasarle un paño húmedo. ¿Qué criterio muestra que falla? A. Durabilidad B. Acceso.", "A", "Se deforma con la humedad, así que no resistiría la lluvia; el acceso se refiere a conseguir el material."),
        ex("Anotas un referente como «afiche que vi, no recuerdo de quién». ¿Qué falta para citarlo bien? A. Quién lo hizo, dónde está y qué datos son seguros B. Un título más largo.", "A", "La procedencia exige autoría, lugar y datos confirmados."),
    ],
    [
        ex("Un compañero dice: «Mi referente es la foto de una amiga que sale en primer plano y la usaré sin preguntarle». ¿Qué cuidado falta?", "Pedir permiso o usar otra imagen sin rostros", "Una imagen de una persona se usa solo con su autorización."),
        ex("Dos opciones para una plaza lluviosa: afiche de papel o letras de pintura para exterior sobre un panel de plástico reutilizado. Debe durar el mes entero. ¿Cuál elige quien prioriza la durabilidad?", "El panel de plástico con pintura para exterior", "El papel se deshace con la lluvia; el panel resiste mejor la humedad."),
    ],
    [
        ex("Puntajes de ejemplo de 1 a 3 (durabilidad, reversibilidad, legibilidad, acceso). Papel con cinta: 1, 3, 2, 3. Panel reutilizado con letras de pintura para exterior: 3, 2, 2, 2. El mensaje debe resistir un mes de lluvia, así que la durabilidad es el criterio prioritario. ¿Cuál eliges? A. El panel reutilizado, porque ambos suman 9 y decide la durabilidad B. El papel, porque su reversibilidad es la más alta.", "A", "Ambos suman 9; al empatar decide el criterio prioritario, que es la durabilidad."),
        ex("Dos criterios chocan: el papel es barato pero dura poco; el panel resiste, pero cuesta más. El mensaje es para un solo fin de semana sin lluvia. ¿Qué eliges? A. El papel, porque dura lo suficiente y cuesta menos B. El panel, porque siempre es mejor.", "A", "La decisión depende del uso: para dos días sin lluvia basta el papel."),
    ],
    ex("Tu curso quiere un mensaje sobre convivencia para un pasillo del liceo durante dos semanas. Necesita ser barato, retirarse sin dañar la pared y leerse a dos metros. ¿Qué opción cumple los tres criterios? A. Cartulinas grandes con letras gruesas y cinta removible B. Pintura al óleo directa sobre la pared.", "A", "La cartulina es barata, la cinta removible no daña y las letras gruesas se leen a dos metros."),
    [
        ex("¿Qué cuatro criterios se comparan al elegir un material para el espacio público?", "Durabilidad, reversibilidad, legibilidad y acceso", "Juntos muestran si el material sirve para ese lugar."),
        ex("Verdadero o falso: basta cambiar el color de un referente para que la obra sea propia.", "Falso", "Hay que cambiar al menos dos decisiones y citar la procedencia."),
        ex("¿Qué se escribe cuando un dato de un referente no es seguro?", "Dato por confirmar", "No se afirman datos dudosos."),
    ],
    task(
        "Elige UN mensaje de ejemplo. A) «Cuida la plaza»: se verá una semana en una reja al aire libre, sin lluvia. B) «Apaga la luz al salir»: se verá en el pasillo del liceo por dos semanas. C) «Separa tu basura»: debe repetirse en cuatro lugares iguales. Con cartón, papel y restos limpios haz dos muestras de materialidades distintas, compáralas con dos criterios (por ejemplo durabilidad y reversibilidad) y elige una. Anota un referente de ejemplo del que tomas un recurso y qué dos decisiones cambiaste.",
        "Elegí la C. Muestra 1: esténcil de cartón con un contenedor; muestra 2: dibujo a mano en papel. Criterios: rapidez y repetición. Elegí el esténcil porque repite la forma en cuatro lugares. Referente de ejemplo: afiche con letras blancas sobre negro; tomé el contraste y cambié el tema y la imagen.",
        ["hace dos muestras con materialidades distintas", "compara con dos criterios", "elige una y explica por qué", "cita el referente y dos cambios propios"],
        ["dos muestras", "comparación con criterios", "referente citado con cambios"],
        ["elegir por moda y no por uso", "copiar un referente cambiando solo el color"],
        "Pregunta qué criterio decidió su elección y qué dos decisiones cambió respecto del referente.",
    ),
    "Revisa dos objetos de papel o cartón de tu casa y di cuál soportaría mejor la lluvia y cuál se retiraría sin dañar una pared.",
    "Escribe tres frases sobre qué material usarías para un mensaje de un mes en una plaza y por qué.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA1, 3,
    "Hojas, lápices de colores y regla. Los bocetos y resultados de ejemplo están escritos en esta clase; no necesitas aplicar encuestas reales.",
    "Aprenderé a probar decisiones visuales cambiando una sola variable y comparando el efecto con un criterio. Sirve para elegir con evidencia y no por costumbre.",
    ["Sé elegir materiales según durabilidad, reversibilidad, legibilidad y acceso.", "Sé que debo transformar un referente y no copiarlo."],
    [
        "Probar una decisión visual es hacer dos versiones de un boceto que se diferencian en una sola cosa y comparar qué efecto produce el cambio. Esa cosa es la variable. Puede ser el color del fondo, el tamaño de la letra, la posición de la imagen o el tipo de frase. Si cambio dos cosas a la vez, no sé cuál causó el efecto. Un boceto es un dibujo rápido para ensayar ideas antes de hacer la pieza final.",
        "Para comparar uso un criterio claro. Por ejemplo, legibilidad a tres metros: ¿se entiende el mensaje desde esa distancia? Puedo pedir a cuatro o cinco compañeros que miren cada versión por cinco segundos y me digan qué mensaje entendieron. Cuento cuántos acertaron en cada versión y registro el resultado en una tabla. Es una prueba pequeña, de ejemplo: sirve para decidir, no para demostrar algo definitivo.",
        "También pruebo el tipo de recurso. Una frase de orden, como «Cuida tu plaza», da una instrucción directa. Una pregunta, como «¿Quién cuida tu plaza?», invita a pensar. Una imagen literal muestra la situación; una imagen simbólica, como una gota que representa el agua, sugiere una idea. Guardo también la versión que descarto: es parte de mi proceso. No ridiculizo a ninguna persona en mis bocetos.",
    ],
    [("variable", "lo único que se cambia entre dos versiones para comparar"), ("boceto", "dibujo rápido para ensayar una idea"), ("legibilidad", "facilidad con que se lee un texto o se entiende una imagen"), ("frase de orden", "frase que da una instrucción directa, como «Cuida tu plaza»"), ("símbolo", "imagen que representa una idea más allá de lo que muestra")],
    [
        w("Comparar dos versiones", "Boceto A: letras blancas sobre fondo azul. Boceto B: letras amarillas sobre fondo azul; todo lo demás es igual. Cinco compañeros ven cada versión por cinco segundos desde tres metros. Con A, 4 entienden el mensaje; con B, 2. ¿Qué decisión conservas?", ["Variable cambiada: solo el color de las letras.", "Resultado: A obtuvo 4 de 5 y B obtuvo 2 de 5.", "Decisión: conservar las letras blancas."], "Conservo las letras blancas, que 4 de 5 entendieron frente a 2 de 5"),
        w("Elegir tipo de frase", "Para un panel en un pasillo, comparas la orden «Cuida tu plaza» con la pregunta «¿Quién cuida tu plaza?». El propósito es que el público se detenga a pensar. ¿Cuál eliges?", ["Criterio: que el público se detenga a pensar.", "La orden manda; la pregunta invita a responder.", "Decisión: la pregunta."], "La pregunta, porque invita a pensar y a detenerse"),
    ],
    [
        m("Cambiar color, tamaño y frase a la vez entre dos versiones.", "No se sabe cuál de los cambios produjo el efecto.", "Cambia una sola variable por prueba y deja lo demás igual."),
        m("Elegir la versión que «me gusta más» sin comparar con un criterio.", "El gusto personal no demuestra que el mensaje se entienda.", "Compara con un criterio como la legibilidad a tres metros."),
    ],
    [
        ex("En Artes Visuales, ¿qué es una variable al comparar dos bocetos? A. Lo único que se cambia entre las dos versiones B. Todas las diferencias entre las dos versiones C. El resultado final de la prueba.", "A", "Si solo cambia una cosa, se puede atribuir el efecto a ella."),
        ex("Dos bocetos tienen letras de distinto tamaño, y además colores distintos. ¿Es una buena prueba de una sola variable?", "No", "Cambian dos cosas a la vez y no se sabe cuál causa el efecto."),
        ex("En una prueba de legibilidad, ¿qué se pide a los compañeros? A. Decir qué mensaje entendieron tras mirar cada versión cinco segundos B. Elegir el color que más les gusta.", "A", "La prueba mide si el mensaje se entiende, no el gusto."),
    ],
    [
        ex("Un boceto muestra una gota que representa el agua del planeta. ¿Qué tipo de imagen es? A. Simbólica B. Literal.", "A", "Una gota que representa una idea más amplia es símbolo."),
        ex("Quieres saber si el tamaño de la letra mejora la legibilidad. ¿Qué dejas igual entre las dos versiones? A. Color, frase e imagen B. Nada, para que las dos versiones sean más distintas.", "A", "Para probar el tamaño, el resto debe mantenerse."),
        ex("Un grupo compara dos bocetos que son iguales salvo la imagen: uno muestra una llave goteando y el otro una gota gigante que representa el agua del planeta. ¿Qué variable prueba? A. Imagen literal o simbólica B. Color de las letras.", "A", "Lo único que cambia es el tipo de imagen."),
    ],
    [
        ex("Prueba de ejemplo con 5 compañeros: la versión A fue entendida por 3 y la versión B por 5. Criterio: entender el mensaje en cinco segundos. ¿Cuál versión conservas?", "B", "Fue entendida por más personas, y ese es el criterio."),
        ex("Para comparar con justicia dos versiones de un afiche, ¿qué debe ser igual en ambas pruebas? A. La distancia, el tiempo de observación y la pregunta B. Nada, porque las versiones ya son distintas.", "A", "Si cambian las condiciones, no se sabe si el resultado se debe a la versión."),
        ex("Quieres que el público se detenga a reflexionar sobre cuánto tiempo pasa en el celular. ¿Qué frase usas? A. «¿Cuánto tiempo miraste hoy tu pantalla?» B. «Apaga ya tu celular».", "A", "La pregunta invita a pensar; la orden no abre reflexión."),
    ],
    [
        ex("Un compañero prueba solo con dos amigos que ya conocen el tema. ¿Qué limitación tiene su prueba? A. Pocas personas y ya informadas, así que no muestran cómo reaccionará un público nuevo B. Que usó papel.", "A", "Quien ya conoce el tema entiende más fácil; la muestra es chica y sesgada."),
        ex("Descartaste la versión B, pero la botas sin guardarla. ¿Qué pierdes? A. La evidencia del proceso y la comparación B. Nada, porque no sirve.", "A", "Las versiones descartadas muestran cómo decidiste."),
    ],
    [
        ex("Una prueba de ejemplo cambió dos variables: fondo oscuro y letra más grande. La versión nueva se entendió mejor. ¿Qué puedes afirmar con seguridad? A. Que el conjunto de cambios ayudó, pero no cuál de los dos B. Que el fondo oscuro es el culpable.", "A", "No se puede separar el efecto de cada cambio."),
        ex("Prueba de ejemplo: 8 de 10 personas entendieron la versión A y 7 de 10 la versión B. ¿Qué conclusión es más prudente? A. La diferencia es pequeña y el grupo chico: conviene repetir la prueba con más personas B. La A es claramente mejor porque 8 es mayor que 7.", "A", "Una diferencia de una persona en un grupo pequeño puede deberse al azar; la prueba sirve para decidir, no para demostrar."),
    ],
    ex("Tu grupo diseña un afiche sobre ahorrar agua. Versión 1: gota azul pequeña y frase larga. Versión 2: gota azul grande y frase corta. En la prueba, 5 de 6 personas entienden la versión 2 y 2 de 6 entienden la versión 1. ¿Cuál es una conclusión justa? A. La versión 2 se entiende mejor, pero cambió imagen y frase a la vez B. La versión 1 es peor porque es fea.", "A", "Reconoce el resultado y también el límite de haber cambiado dos variables."),
    [
        ex("¿Cuántas cosas cambias entre dos versiones en una prueba de una variable?", "Una", "Así el efecto se atribuye a ese cambio."),
        ex("Verdadero o falso: la versión que descartas se bota sin guardar.", "Falso", "Se guarda como evidencia del proceso."),
        ex("¿Qué criterio puede usarse para comparar dos afiches vistos desde lejos?", "Legibilidad a tres metros", "Mide si se entiende desde esa distancia."),
    ],
    task(
        "Elige UN problema de ejemplo. A) Basura en la cancha del barrio. B) Poco tiempo para descansar de las pantallas. C) Falta de bancas en el paradero. Haz dos bocetos pequeños de un afiche que se diferencien en UNA variable (color de las letras, tamaño de la imagen, orden o tipo de frase). Muéstralos a tres personas por cinco segundos y pregunta qué mensaje entendieron, o simula el resultado con datos de ejemplo escritos por ti. Anota la tabla de resultados y decide cuál conservas.",
        "Elegí el problema A. Variable: tipo de frase. Boceto 1: «Cuida tu cancha». Boceto 2: «¿Quién cuida tu cancha?». Entendieron el mensaje 2 de 3 personas en el 1 y 3 de 3 en el 2. Conservo el 2, porque lo entendieron las 3 personas, frente a 2 de 3 con el boceto 1.",
        ["cambia una sola variable", "registra los resultados en una tabla", "decide con un criterio", "guarda la versión descartada"],
        ["dos bocetos", "tabla de resultados y decisión"],
        ["cambiar varias variables a la vez", "decidir por gusto"],
        "Pregunta qué variable cambió y qué resultado respalda su decisión.",
    ),
    "Dibuja dos versiones de una misma frase corta en un papel y pregunta a una persona de tu casa cuál se lee mejor desde lejos.",
    "Explica con tres frases qué prueba harías para decidir entre una imagen literal y una simbólica.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA1, 4,
    "Hojas, lápices, regla y papel de reciclaje. La ficha de proyecto y el ejemplo del grupo Farol están en esta clase.",
    "Aprenderé a desarrollar una propuesta propia: definir la problemática, el público, el lugar, el permiso, el boceto y un plan de retiro. Sirve para pasar de una idea suelta a un proyecto que se pueda hacer.",
    ["Sé probar decisiones cambiando una variable.", "Sé elegir materiales según criterios de uso."],
    [
        "Una propuesta de proyecto visual responde a siete preguntas. 1) Problemática: ¿qué situación muestro? 2) Público: ¿quiénes lo verán? 3) Mensaje: lo resumo en una frase. 4) Lugar: ¿dónde estará y quién lo autoriza? 5) Formato y materiales: ¿qué decisiones visuales tomé y por qué? 6) Boceto: dibujo con medidas. 7) Plan: cuánto durará y cómo se retirará. Escribirlas en una ficha me ayuda a no olvidar nada.",
        "El mensaje se resume en una frase de unas ocho palabras, de modo que se lea en pocos segundos. La autoría es la responsabilidad de quien crea. Aunque trabaje con un referente, las decisiones deben ser mías y anoto cuáles son. Un proyecto sobre una problemática juvenil se cuida de no señalar a nadie. Si el tema es delicado, como la convivencia entre compañeros, muestro la situación y propongo una salida, sin exhibir a personas reales, y converso con una persona adulta de confianza.",
        "El cronograma reparte el tiempo entre tareas. Si tengo cuatro sesiones de 45 minutos, destino la primera al boceto, la segunda y tercera a hacer la pieza y la cuarta a instalarla y registrarla. Dejo siempre un margen por si algo se retrasa. También calculo el presupuesto, que es el dinero que gastaré. Prefiero materiales reutilizados, que cuestan menos y cuidan el ambiente.",
    ],
    [("propuesta", "plan escrito de un proyecto antes de hacerlo"), ("autoría", "responsabilidad de quien crea una obra"), ("cronograma", "reparto del tiempo entre las tareas de un proyecto"), ("presupuesto", "dinero que se calcula gastar en un proyecto"), ("plan de retiro", "forma en que se sacará la pieza sin dañar el lugar")],
    [
        w("Armar una ficha", "Grupo Farol (de ejemplo): problemática, poca iluminación en la cancha de noche. Público: jóvenes del barrio. Lugar: panel exterior de la sede vecinal, con permiso. Escribe el mensaje en una frase corta y el plan de retiro.", ["Mensaje de ocho palabras o menos: «Una cancha con luz es de todos».", "Material: cartulinas pegadas con cinta removible.", "Plan de retiro: sacar las cartulinas a las dos semanas y limpiar el panel."], "Mensaje: «Una cancha con luz es de todos»; retiro a las dos semanas, sin dejar marcas"),
        w("Repartir el tiempo", "El grupo tiene 4 sesiones de 45 minutos. ¿Cómo las reparte si la primera es para el boceto, dos para hacer la pieza y una para instalarla y registrarla?", ["Sesión 1: boceto, 45 minutos.", "Sesiones 2 y 3: hacer la pieza, 90 minutos en total.", "Sesión 4: instalar y registrar, 45 minutos."], "Boceto 45 min; pieza 90 min; instalación y registro 45 min"),
    ],
    [
        m("Pasar directo a la pieza final sin ficha ni boceto.", "No se resuelven lugar, permiso, medidas ni retiro.", "Completa las siete preguntas de la ficha antes de hacer la pieza."),
        m("Mostrar el rostro o la situación de un compañero real para denunciar un problema de convivencia.", "Expone a una persona y puede dañarla.", "Muestra la situación con personajes inventados y conversa con una persona adulta de confianza."),
    ],
    [
        ex("En la ficha de siete preguntas, ¿dónde se anota quién autoriza el espacio? A. En la pregunta de lugar B. En la pregunta de público C. En la pregunta de mensaje.", "A", "El lugar y quien lo autoriza van juntos en la pregunta 4."),
        ex("En Artes Visuales, ¿qué es un cronograma? A. El reparto del tiempo entre las tareas de un proyecto B. El nombre de la obra C. La lista de colores.", "A", "El cronograma organiza el tiempo de trabajo."),
        ex("Para una propuesta sobre iluminación de una cancha, ¿quién es el público? A. Jóvenes del barrio que usan la cancha B. Quien administra la sede.", "A", "El público son las personas que verán la pieza."),
    ],
    [
        ex("¿Cuál es un mensaje bien resumido en pocas palabras? A. «Una plaza viva es de todos» B. «Hay muchas razones por las cuales la plaza del barrio necesitaría más cuidado y se debe considerar».", "A", "Es breve y se lee en pocos segundos."),
        arith("Una pieza usa 3 cartulinas a $450 cada una y cinta removible de $600. ¿Cuánto cuesta en total?", "3 * 450 + 600", "Se suman las cartulinas y la cinta.", " pesos"),
        ex("Se pondrá la pieza en la fachada de una sede vecinal. ¿Qué permiso se necesita? A. El de quien administra la sede B. Ninguno, porque está en la calle.", "A", "Un lugar con responsable exige su autorización."),
    ],
    [
        ex("Al terminar la sesión 3, al grupo Farol le falta pintar un tercio de la pieza, y el permiso vence en una semana. Dejaron un margen en el cronograma. ¿Qué conviene? A. Usar el margen para terminarla y recién entonces instalarla B. Instalarla incompleta para cumplir la fecha.", "A", "El margen existe para los retrasos; una pieza incompleta no cumple el propósito."),
        ex("Un proyecto quiere mostrar la convivencia entre compañeros. ¿Cuál es la forma cuidadosa? A. Personajes inventados que muestran la situación y una salida B. La foto de un compañero real en la situación.", "A", "No se expone a ninguna persona real."),
        ex("En el plan de retiro de una pieza con cinta removible, ¿cuál está bien escrito? A. «Se sacará a las dos semanas y se limpiará el panel» B. «Se sacará cuando se vea sucia».", "A", "Fija cuándo y cómo se retira."),
    ],
    [
        ex("El grupo Farol cambió el color de un referente, pero mantuvo la misma composición y el mismo tema. ¿Qué falta para que la autoría sea propia? A. Cambiar más decisiones propias, como el tema o la composición B. Nada, porque cambió el color.", "A", "Cambiar solo un rasgo deja la obra muy parecida al referente."),
        ex("Tienes el boceto, pero el muro donde irá no tiene dueño conocido. ¿Qué haces? A. Averiguar quién puede autorizarlo antes de instalar B. Instalar igual, porque nadie reclama.", "A", "Sin autorización, no se interviene."),
    ],
    [
        arith("Presupuesto de ejemplo: $6.000. Ya gastaste $2.400 en cartulinas y $1.800 en pintura. ¿Cuánto dinero te queda?", "6000 - 2400 - 1800", "Se restan los dos gastos del presupuesto.", " pesos"),
        ex("Dos plazos de ejemplo: instalar el lunes y retirar el viernes de la misma semana, o instalar un lunes y retirar tres semanas después. El permiso del lugar es solo por 7 días corridos. ¿Cuál cumple el permiso?", "Lunes a viernes de la misma semana", "Son 5 días, dentro de los 7 permitidos."),
    ],
    ex("Tu curso quiere un proyecto sobre el uso excesivo de pantallas, para el patio del liceo. Tienes un panel, 4 sesiones de 45 minutos y $3.000. ¿Cuál es el mejor primer paso? A. Completar la ficha de siete preguntas con un boceto con medidas B. Comprar todos los materiales antes de definir el mensaje.", "A", "La ficha ordena las decisiones y evita gastar en vano."),
    [
        ex("¿Qué se resume en una frase corta en la ficha?", "El mensaje", "Es la idea central que el público debe entender."),
        ex("Verdadero o falso: un proyecto sobre convivencia debe mostrar el rostro de un compañero real.", "Falso", "Se usan personajes inventados y se avisa a un adulto de confianza."),
        ex("¿Qué incluye un buen plan de retiro?", "Cuándo y cómo se saca la pieza sin dañar el lugar", "Así el espacio queda como estaba."),
    ],
    task(
        "Elige UNA problemática de ejemplo. A) Poca iluminación en la cancha de noche. B) Basura en la plaza del barrio. C) Pocos lugares para que jóvenes se junten sin gastar dinero. Completa la ficha de siete preguntas: problemática, público, mensaje en ocho palabras o menos, lugar y quién lo autoriza, formato y materiales (con dos decisiones justificadas), un boceto con medidas y un plan de retiro. Agrega un cronograma de cuatro sesiones de 45 minutos.",
        "Elegí la B. Público: vecinos y jóvenes que pasan por la plaza. Mensaje: «La plaza limpia es de todos». Lugar: reja de la plaza, con permiso de la junta de vecinos. Materiales: cartulinas con letras gruesas, porque se leen a dos metros, y cinta removible. Boceto de 60 por 40 cm. Retiro: a las dos semanas. Cronograma: boceto, dos sesiones de pieza, instalación.",
        ["completa las siete preguntas", "mensaje breve", "señala quién autoriza el lugar", "incluye cronograma y plan de retiro"],
        ["ficha completa", "boceto con medidas", "cronograma"],
        ["pasar a la pieza sin ficha", "no considerar permiso ni retiro"],
        "Pregunta quién autoriza el lugar y qué decisión visual propia tomó respecto de su referente.",
    ),
    "Cuenta a una persona de tu casa tu mensaje en una frase y pregunta si lo entendió.",
    "Escribe tres frases sobre qué cambiarías de tu ficha si el lugar fuera una plaza al aire libre.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA1, 5,
    "Hojas, lápiz y la ficha de la clase anterior. La pauta y los proyectos de ejemplo están escritos en esta clase.",
    "Aprenderé a contrastar mi propuesta con criterios y a dar y recibir retroalimentación sin perder la autoría. Sirve para mejorar el proyecto con razones.",
    ["Sé completar la ficha de un proyecto visual.", "Sé que copiar un referente sin transformarlo no cuenta como autoría."],
    [
        "Contrastar es poner una propuesta frente a criterios para ver qué cumple y qué falta. Para un proyecto sobre una problemática social uso cinco criterios: pertinencia (responde al problema y al público), legibilidad (se entiende desde la distancia), transformación del referente (cambia al menos dos decisiones), cuidado del lugar (tiene permiso y se retira sin daño) y autoría (las decisiones son propias). Cada criterio se puntúa de 0 a 3: 0 no aparece, 1 es débil, 2 es suficiente y 3 es muy logrado. El máximo es 15.",
        "La retroalimentación sirve si es útil. Uso tres pasos: describo lo que veo, nombro el criterio y propongo una sugerencia. Por ejemplo: «Las letras miden 1 cm; el criterio es legibilidad a tres metros; podrías agrandarlas al triple». Evito frases como «está feo» o «me gusta», porque no dicen qué cambiar. Recibo los comentarios con calma, anoto lo útil y decido yo qué cambio, porque la obra sigue siendo mía.",
        "Después de contrastar reviso una sola cosa a la vez y vuelvo a mirar. Si un criterio está bajo, hago un cambio concreto y lo anoto en mi registro. Reconozco con respeto el trabajo de mis compañeros y no comparo personas, sino proyectos. Si recibo un comentario que me hiere o ridiculiza, aviso a una persona adulta de confianza. Una pieza terminada incluye la ficha, el boceto, las versiones descartadas y la revisión.",
    ],
    [("pertinencia", "grado en que una propuesta responde al problema y al público"), ("retroalimentación", "comentario que ayuda a mejorar una obra"), ("pauta", "lista de criterios con puntajes para evaluar"), ("transformación", "cambio de varias decisiones de un referente para hacer algo propio"), ("registro de proceso", "conjunto de notas, bocetos y versiones que muestran cómo se hizo la obra")],
    [
        w("Puntuar con la pauta", "Proyecto de ejemplo: responde bien al problema (3), se lee desde lejos (3), cambió solo el color de su referente (1), tiene permiso y retiro (2) y sus decisiones son propias (2). Suma el puntaje de 15.", ["Pertinencia 3, legibilidad 3.", "Transformación 1, cuidado del lugar 2, autoría 2.", "Suma: 3 + 3 + 1 + 2 + 2."], "11 de 15"),
        w("Retroalimentar en tres pasos", "Proyecto de ejemplo con letras de 1 cm que se verá a tres metros. Escribe un comentario con descripción, criterio y sugerencia.", ["Describo: las letras miden 1 cm.", "Criterio: legibilidad a tres metros.", "Sugerencia: aumentarlas hasta unos 3 cm, el triple."], "Las letras miden 1 cm; para la legibilidad a tres metros podrías aumentarlas a 3 cm"),
    ],
    [
        m("Comentar «está feo» o «me encantó» y creer que ayuda.", "No dice qué rasgo cambiar ni con qué criterio.", "Describe, nombra el criterio y sugiere un cambio."),
        m("Aceptar todos los comentarios y cambiar el proyecto entero.", "Se pierde la autoría y la intención.", "Anota lo útil y decide tú qué cambiar."),
    ],
    [
        ex("¿Qué criterio de la pauta revisa si la pieza tiene permiso y se retira sin dañar el lugar? A. Cuidado del lugar B. Pertinencia C. Autoría.", "A", "Ese criterio reúne el permiso y el plan de retiro."),
        ex("En la pauta, ¿qué puntaje corresponde a un criterio que no aparece? A. 0 B. 3.", "A", "0 significa que no aparece; 3 es muy logrado."),
        ex("En Artes Visuales, ¿qué es la retroalimentación? A. Un comentario que ayuda a mejorar una obra B. Una copia de la obra C. El precio de los materiales.", "A", "Sirve para mejorar el trabajo con razones."),
    ],
    [
        arith("Un proyecto de ejemplo obtiene 2, 3, 1, 3 y 2 puntos en los cinco criterios. ¿Cuántos puntos suma de 15?", "2 + 3 + 1 + 3 + 2", "Se suman los cinco puntajes.", " puntos"),
        ex("¿Cuál comentario es útil? A. «Las letras miden 1 cm: para leerse a tres metros podrías agrandarlas» B. «No me gusta cómo quedó».", "A", "Describe un rasgo, nombra un criterio y propone un cambio."),
        ex("Un proyecto cambió solo el color de su referente. ¿Qué puntaje le corresponde más probablemente en transformación? A. 1 B. 3.", "A", "Hay un cambio mínimo, no varias decisiones nuevas."),
    ],
    [
        ex("Proyecto de ejemplo: puntajes 3, 2, 2, 3 y 3. ¿Cuántos puntos le faltan para llegar al máximo de 15?", "2", "La suma es 13; 15 − 13 = 2.", "15-(3+2+2+3+3)"),
        ex("El criterio con menor puntaje es cuidado del lugar: el proyecto no tiene permiso. ¿Qué cambio concreto haces primero? A. Pedir autorización por escrito a quien administra el lugar B. Hacer las letras más gruesas.", "A", "El problema es el permiso; el grosor de las letras no lo resuelve."),
        ex("Un compañero te dice que todo tu proyecto debe ser cambiado por completo. ¿Qué haces? A. Anotar lo útil y decidir qué cambiar según tus criterios B. Cambiar todo para no discutir.", "A", "La autoría es tuya y las decisiones se toman con razones."),
    ],
    [
        ex("Dos comentarios sobre el mismo afiche. C1: «Es muy bonito». C2: «El fondo azul y las letras blancas se leen desde lejos; podrías sumar un símbolo del agua». ¿Cuál ayuda más a mejorar y por qué?", "C2, porque describe un rasgo, usa un criterio y sugiere un cambio", "C1 no dice qué mantener o cambiar."),
        ex("En tu proyecto, la pertinencia es 3, pero la transformación es 1. ¿Qué combinación de cambios es más razonable? A. Cambiar otras dos decisiones del referente y mantener la pertinencia B. Rehacer la pertinencia desde cero.", "A", "El punto débil es la transformación, no la pertinencia."),
    ],
    [
        ex("Dos revisores puntúan la legibilidad del mismo afiche: uno pone 3 y otro 1. ¿Qué conviene hacer primero? A. Pedir a cada uno el rasgo observable en que se apoya B. Promediar los dos puntajes sin preguntar.", "A", "Con la evidencia sobre la mesa se ve si midieron lo mismo y se decide con razones."),
        ex("Un compañero se burla de tu boceto con un comentario que te hiere. ¿Qué haces? A. Aviso a una persona adulta de confianza B. Respondo con otra burla.", "A", "Las burlas se informan; responder con otra burla escala el problema."),
    ],
    ex("Un grupo pegó un afiche sin permiso en una reja pública. ¿Qué criterio de la pauta resulta más afectado por ese hecho? A. Cuidado del lugar B. Legibilidad C. Pertinencia.", "A", "El permiso y el retiro sin daño pertenecen al cuidado del lugar."),
    [
        ex("¿Qué tres pasos tiene una retroalimentación útil en esta clase?", "Describir, nombrar el criterio y sugerir", "Así el comentario dice qué ver, por qué y qué cambiar."),
        ex("Verdadero o falso: al recibir un comentario debo cambiar todo mi proyecto.", "Falso", "Se anota lo útil y se decide qué cambiar."),
        ex("¿Cuál es el puntaje máximo de la pauta de cinco criterios?", "15", "Cinco criterios por un máximo de 3 puntos cada uno."),
    ],
    task(
        "Elige UN proyecto de ejemplo. A) Afiche «Una cancha con luz es de todos»: letras blancas de 6 cm sobre azul, con permiso, se retira a las dos semanas; cambió el tema y la composición de su referente. B) Panel «La plaza limpia es de todos»: letras amarillas de 1 cm, sin permiso, copia el diseño de un referente. C) Mural de cartulinas «¿Cuánto miraste tu pantalla hoy?»: letras negras de 8 cm, con permiso, cambió el color y la frase de su referente. Puntúa de 0 a 3 los cinco criterios de la pauta, calcula el total y escribe un comentario de tres pasos para el criterio más bajo. Luego propone un cambio concreto.",
        "Elegí la B. Pertinencia 2, legibilidad 1, transformación 0, cuidado del lugar 0, autoría 0: total 3 de 15. Comentario: el proyecto no tiene permiso y su diseño es igual al del referente; el criterio es cuidado del lugar; sugiero pedir autorización a la junta de vecinos antes de instalar.",
        ["puntúa los cinco criterios", "calcula el total", "escribe un comentario de tres pasos", "propone un cambio concreto"],
        ["pauta puntuada", "comentario de tres pasos"],
        ["comentar solo si gusta o no", "olvidar el permiso"],
        "Pregunta qué criterio tuvo el puntaje más bajo y cómo lo mejoraría su comentario.",
    ),
    "Revisa tu ficha con la pauta de cinco criterios y marca cuál quedó más bajo.",
    "Escribe un comentario de tres pasos para el proyecto de un compañero imaginario que usa letras muy pequeñas.",
)
