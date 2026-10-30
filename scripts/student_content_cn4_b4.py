"""Cuaderno del estudiante, 4.º básico Ciencias Naturales: OA 17 (medidas de prevención y seguridad ante riesgos naturales)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA17 = "CN04 OA 17"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


register(
    OA17, 1,
    materials="Papel y lápiz. Para observar riesgos, recorre con una persona adulta una sala o una pieza de tu casa, sin mover muebles pesados. Las medidas que necesiten herramientas, como sujetar un estante, las hace una persona adulta. También puedes trabajar con las listas escritas.",
    use="Aprenderé a reconocer riesgos naturales y qué cosas de la escuela, la calle y el hogar los hacen más peligrosos. Sirve para empezar a prevenir daños antes de que ocurran.",
    prior=["Sé que los sismos, los tsunamis y las erupciones se relacionan con el movimiento de las placas.", "Sé que Chile está en una zona con muchos sismos y volcanes."],
    explain=[
        "Un riesgo natural es la posibilidad de que un fenómeno de la naturaleza, como un sismo, un tsunami, una erupción volcánica o un temporal, cause daño a las personas o a las cosas. El fenómeno por sí solo no es el riesgo: hay riesgo cuando hay personas o bienes que pueden salir dañados.",
        "Prevenir es prepararse antes para disminuir el daño. Una medida de prevención puede ser sujetar un estante a la pared, dejar libre el paso a la salida o saber a dónde ir. Una medida de seguridad es lo que hago durante la emergencia, como alejarme de las ventanas.",
        "Para reconocer riesgos, observo tres lugares: la escuela, la calle y el hogar. En cada uno busco objetos que puedan caer, salidas bloqueadas y lugares sin protección. Por ejemplo, un macetero en un balcón puede caer en un sismo, y un estante alto con cosas pesadas puede volcarse.",
    ],
    vocab=[("riesgo natural", "posibilidad de que un fenómeno de la naturaleza cause daño"), ("prevención", "preparación antes de que ocurra un fenómeno para reducir el daño"), ("seguridad", "cuidado para protegerse durante una emergencia"), ("emergencia", "situación grave que ocurre de pronto"), ("zona de seguridad", "lugar marcado como más seguro durante una emergencia")],
    worked=[
        {"title": "Riesgo en el hogar", "problem": "En una pieza hay un estante alto, con libros pesados arriba, sin sujetar a la pared. ¿Qué riesgo hay en un sismo y qué medida de prevención propones?", "steps": ["En un sismo el estante puede volcarse y los libros caerían.", "Sujetar el estante a la pared y poner lo pesado abajo disminuye el daño."], "answer": "Riesgo de volcamiento; sujetar el estante y poner lo pesado abajo"},
        {"title": "Riesgo en la escuela", "problem": "En el pasillo de la escuela hay mochilas apiladas frente a la puerta de salida. ¿Qué riesgo crean en una emergencia?", "steps": ["La puerta es la vía de salida.", "Las mochilas pueden bloquear el paso."], "answer": "Bloquean la vía de evacuación"},
    ],
    mistakes=[
        {"wrong": "Pensar que prevenir es lo que hago cuando ya empezó el sismo.", "why": "Se mezcla la prevención con la acción durante la emergencia.", "fix": "Prevenir es prepararse antes; lo que hago durante es seguridad."},
        {"wrong": "Decir que un riesgo natural existe solo si hay un desastre.", "why": "Se asocia con daños ya ocurridos.", "fix": "El riesgo es la posibilidad de daño; se puede reducir antes."},
    ],
    tiers={
        "recovery": [
            ex("¿Un sismo es un fenómeno natural o un objeto de la casa?", "Un fenómeno natural", "Ocurre por el movimiento de las placas."),
            ex("¿Sujetar un estante a la pared se hace antes o después de un sismo?", "Antes", "Es una medida de prevención."),
            ex("Completa: la ___ es prepararse antes para disminuir el daño (prevención o emergencia).", "prevención", "Se hace antes de que ocurra el fenómeno."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es un riesgo natural?", "La posibilidad de que un fenómeno natural cause daño", "Hay riesgo cuando personas o bienes pueden dañarse."),
            ex("¿Cuál es la diferencia entre prevención y seguridad?", "Prevención es antes y seguridad es durante la emergencia", "Una prepara y la otra protege en el momento."),
            ex("¿Por qué el macetero de un balcón puede ser un riesgo en un sismo?", "Porque puede caer sobre las personas", "Los objetos altos pueden caerse al temblar."),
        ],
        "apply": [
            ex("Clasifica como prevención o seguridad: sujetar la biblioteca a la pared; alejarse de la ventana cuando tiembla.", "Sujetar la biblioteca: prevención. Alejarse de la ventana: seguridad", "Una es antes y la otra, durante."),
            ex("En una sala, los pasillos entre bancas están despejados y las mochilas, en el fondo. ¿Esta situación es de riesgo o de prevención?", "De prevención", "Deja libre el paso para evacuar."),
            ex("En una calle, un cable cuelga de un poste y está suelto. ¿Qué haces: acercarte a mirarlo o avisar a una persona adulta y alejarte?", "Avisar a una persona adulta y alejarte", "Puede ser peligroso y no se toca."),
        ],
        "reason": [
            ex("Un compañero dice que no hace falta prevenir porque no sabemos cuándo habrá un sismo. ¿Qué argumento le das?", "Porque en Chile los sismos son frecuentes y estar preparado reduce el daño", "Prevenir sirve justo porque no se sabe cuándo ocurrirá."),
            ex("En una casa, un estante con adornos pesados está al lado de la cama. ¿Qué cambio de lugar propones y por qué?", "Poner los adornos pesados abajo o lejos de la cama, para que no caigan sobre alguien", "Los objetos que caen pueden lastimar."),
        ],
        "challenge": [
            arith("Una sala tiene 3 estantes sin sujetar, el pasillo de la escuela tiene 2 y la entrada de una casa tiene 1. ¿Cuántos estantes sin sujetar hay en total?", "3+2+1", "Se suman los estantes de los tres lugares.", " estantes"),
            ex("En una sala, la puerta de salida está tapada por una mesa. ¿Qué medida de prevención corresponde?", "Retirar la mesa y dejar la salida libre", "Una salida libre permite evacuar con rapidez."),
        ],
    },
    context=[ex("Camila revisa su sala y encuentra: una mochila en el pasillo, una repisa sin sujetar sobre el pizarrón y un enchufe flojo. Si solo puede arreglar una cosa que se relacione con un sismo, ¿cuál elige primero?", "La repisa sin sujetar", "Puede caer sobre personas durante un sismo.")],
    selfcheck=[
        ex("¿Qué es la prevención?", "Prepararse antes para disminuir el daño", "Se hace antes del fenómeno."),
        ex("¿Dónde observamos riesgos en esta clase?", "En la escuela, la calle y el hogar", "Son los tres lugares del objetivo."),
        ex("¿Una salida bloqueada por mochilas es un riesgo?", "Sí", "Impide evacuar con rapidez."),
    ],
    open_task=task(
        "Haz una tabla con tres lugares (escuela, calle, hogar). Usa estas situaciones: escuela, mochilas en el pasillo; calle, un macetero en un balcón de un edificio; hogar, un estante alto sin sujetar. Para cada una escribe el riesgo y una medida de prevención. Si puedes, agrega una situación que veas en tu casa o en tu sala.",
        "Escuela: mochilas en el pasillo bloquean la salida; guardarlas en el fondo. Calle: macetero puede caer; afirmarlo o ponerlo en el piso. Hogar: estante puede volcarse; sujetarlo a la pared.",
        ["identifica el riesgo de cada situación", "propone una medida de prevención realista", "cubre escuela, calle y hogar"],
        ["tabla de tres filas", "frase final"],
        ["confundir prevención con acciones durante el sismo", "medidas imposibles de hacer"],
        "Reconoce las medidas bien pensadas y pide aclarar el riesgo cuando falta.",
    ),
    reinforce="Con una persona de tu casa, mira una pieza y anota dos cosas que podrían caer en un sismo.",
    extend="Averigua qué es el plan de seguridad de tu escuela y dónde está la zona de seguridad.",
)

register(
    OA17, 2,
    materials="Papel y lápiz. Si quieres practicar, hazlo con una persona adulta en una pieza despejada, sin carreras ni empujones.",
    use="Aprenderé qué hacer en un sismo en la escuela, la calle y el hogar. Sirve para actuar con calma y proteger mi cuerpo.",
    prior=["Sé que un sismo es un temblor de la tierra.", "Sé que prevenir es prepararse antes."],
    explain=[
        "En un sismo, lo primero es mantener la calma y no correr ni empujar. Si estoy adentro, me agacho, me cubro la cabeza y el cuello y me sujeto de algo firme, y me alejo de ventanas, espejos y estantes. Una mesa resistente es un buen lugar para cubrirse.",
        "En la escuela sigo las instrucciones del profesor o profesora y voy a la zona de seguridad por la vía de evacuación marcada, caminando. No uso el ascensor. En la calle me alejo de postes, cables y fachadas, y me ubico en un lugar abierto. En un vehículo, me quedo adentro hasta que pare el temblor.",
        "Cuando el temblor termina, salgo con calma por la ruta marcada. Si estoy cerca del mar y el temblor fue fuerte y largo, me alejo de la costa hacia un lugar alto por mi ruta de evacuación. Cada escuela y cada casa deben tener su plan, que se practica en simulacros.",
    ],
    vocab=[("simulacro", "práctica de lo que se hace en una emergencia"), ("zona de seguridad", "lugar marcado como más seguro"), ("vía de evacuación", "camino marcado para salir de un lugar"), ("evacuar", "salir de un lugar peligroso"), ("calma", "estado tranquilo para pensar bien")],
    worked=[
        {"title": "En la sala durante un sismo", "problem": "Estás en la sala cuando comienza un temblor fuerte. ¿Qué haces primero?", "steps": ["Mantengo la calma y no corro.", "Me agacho, me cubro la cabeza y el cuello y me sujeto, lejos de las ventanas."], "answer": "Agacharme, cubrirme y sujetarme lejos de ventanas"},
        {"title": "En la calle", "problem": "Estás en la calle y comienza un sismo. ¿Hacia dónde te mueves?", "steps": ["Los postes, los cables y las fachadas pueden caer.", "Voy a un lugar abierto, lejos de ellos."], "answer": "A un lugar abierto, lejos de postes, cables y fachadas"},
    ],
    mistakes=[
        {"wrong": "Correr hacia la salida durante el temblor.", "why": "Se quiere escapar rápido.", "fix": "Primero protégete; cuando pare, evacúa caminando por la ruta."},
        {"wrong": "Usar el ascensor para evacuar después de un sismo.", "why": "Parece más rápido.", "fix": "El ascensor puede quedar detenido; usa las escaleras."},
    ],
    tiers={
        "recovery": [
            ex("Durante un sismo, ¿te quedas tranquilo o corres sin parar?", "Me quedo tranquilo", "La calma ayuda a actuar bien."),
            ex("Si estás adentro, ¿te alejas o te acercas a las ventanas?", "Me alejo", "Los vidrios pueden romperse."),
            ex("Completa: después del sismo, se evacúa por la vía de ___ (evacuación o diversión).", "evacuación", "Es el camino marcado para salir."),
        ],
        "understand": [
            ex("¿Por qué se cubre la cabeza y el cuello durante un sismo?", "Porque pueden caer objetos", "Son partes importantes que hay que proteger."),
            ex("¿Por qué no se usa el ascensor en una evacuación?", "Porque puede quedarse detenido", "Es más seguro usar las escaleras."),
            ex("¿Para qué sirven los simulacros?", "Para practicar lo que se hace en una emergencia", "Así se aprende a actuar con calma."),
        ],
        "apply": [
            ex("Estás en la calle y comienza un sismo. ¿Qué eliges: pararte al lado de un poste o ir a una plaza abierta?", "Ir a una plaza abierta", "Los postes pueden caer."),
            ex("Estás en tu pieza cuando comienza un temblor y tienes un escritorio firme a un lado y una ventana grande al otro. ¿Dónde te cubres?", "Bajo o junto al escritorio firme", "Te proteges de objetos que caen y te alejas del vidrio."),
            ex("Ordena las acciones durante un sismo en la sala: caminar a la zona de seguridad; agacharse y cubrirse; esperar que pase el temblor.", "Agacharse y cubrirse; esperar que pase el temblor; caminar a la zona de seguridad", "Primero te proteges y luego evacúas."),
        ],
        "reason": [
            ex("Un compañero propone gritar y correr cuando comience el temblor. ¿Qué riesgo tiene?", "Puede caerse o chocar con otros y lastimarse", "Correr durante el temblor es peligroso."),
            ex("Estás en un auto que se detiene durante un sismo. ¿Qué haces?", "Me quedo adentro hasta que pase el temblor", "El auto protege mejor que la calle."),
        ],
        "challenge": [
            arith("En la sala hay 30 estudiantes. En un simulacro, salen en grupos de 5. ¿Cuántos grupos salen?", "30//5", "Se reparten los estudiantes en grupos iguales.", " grupos"),
            ex("Estás en la playa y el sismo fue tan fuerte que no podías mantenerte en pie. ¿Qué haces cuando termina?", "Me alejo de la costa hacia un lugar alto", "Puede venir un tsunami."),
        ],
    },
    context=[ex("Durante un simulacro en la escuela, Joaquín ve que el profesor ya está en la puerta. Joaquín quiere pasar corriendo a otro compañero. ¿Qué debe hacer?", "Caminar y esperar su turno", "Correr y empujar causa accidentes.")],
    selfcheck=[
        ex("¿Qué haces primero en un sismo en la sala?", "Mantener la calma, agacharme y cubrirme", "Te proteges antes de moverte."),
        ex("¿Se usa el ascensor para evacuar?", "No", "Puede quedarse detenido."),
        ex("¿Hacia dónde vas si estás en la calle?", "A un lugar abierto, lejos de postes y fachadas", "Allí hay menos riesgo de caída de objetos."),
    ],
    open_task=task(
        "Escribe un guion con cinco pasos para actuar en un sismo en la sala de clases. Si quieres, practícalo con tu familia en tu casa con una persona adulta, sin correr. Usa estas palabras: calma, agacharse, cubrirse, ventanas, zona de seguridad. Agrega un paso para la calle y un paso para tu casa.",
        "1. Mantener la calma. 2. Agacharme y cubrirme la cabeza y el cuello. 3. Alejarme de las ventanas. 4. Al terminar, caminar a la zona de seguridad. 5. Esperar instrucciones. Calle: ir a un lugar abierto. Casa: cubrirme bajo una mesa firme.",
        ["cinco pasos ordenados", "usa las cinco palabras", "agrega calle y casa"],
        ["guion escrito", "práctica opcional con adulto"],
        ["incluir correr o usar el ascensor", "no ordenar los pasos"],
        "Reconoce un guion seguro y pide revisar el orden de los pasos.",
    ),
    reinforce="Pregunta a una persona de tu casa dónde estaría el lugar más seguro de la pieza si temblara.",
    extend="Averigua qué es el Plan Integral de Seguridad Escolar y quién lo prepara en una escuela.",
)

register(
    OA17, 3,
    materials="Papel, lápiz y un mapa simple de tu barrio dibujado a mano, si quieres. No es necesario salir de casa: los casos están escritos.",
    use="Aprenderé qué hacer ante un tsunami y una erupción volcánica. Sirve para saber a dónde ir y cómo protegerme según el riesgo del lugar donde vivo.",
    prior=["Sé que un tsunami se forma por el movimiento del fondo del mar.", "Sé que un volcán puede lanzar lava, gases y ceniza."],
    explain=[
        "El tsunami llega desde el mar. Si estoy en la costa y siento un sismo tan fuerte que no puedo mantenerme en pie, o si suena una alarma de evacuación, debo irme de inmediato a una zona alta por la ruta de evacuación señalada. No espero a ver el mar retirarse ni a que me avisen. Las olas pueden llegar varias veces, así que no vuelvo hasta que las autoridades lo indiquen.",
        "Una erupción volcánica puede lanzar ceniza, gases y material caliente. Si vivo cerca de un volcán, estoy atento a las alertas y sigo las indicaciones de los organismos de emergencia. Si cae ceniza, me cubro la nariz y la boca con un paño húmedo, protejo el agua y los alimentos y evito salir si no es necesario. Si las autoridades piden evacuar, me voy por la ruta indicada.",
        "Cada riesgo se maneja de forma distinta. Para el tsunami cuenta la altura y la distancia al mar. Para la erupción cuenta estar atento a las alertas y proteger la respiración. En ambos casos el plan familiar, la mochila de emergencia y la información oficial ayudan a decidir bien.",
    ],
    vocab=[("zona de evacuación", "área marcada que se debe dejar ante un tsunami"), ("zona alta", "lugar elevado, lejos del mar"), ("alerta", "aviso oficial de que hay un peligro"), ("ceniza", "trocitos muy pequeños de roca que expulsa un volcán"), ("autoridad de emergencia", "organismo que da instrucciones en una emergencia")],
    worked=[
        {"title": "Tsunami en la costa", "problem": "Estás en una playa y el sismo es tan fuerte que no puedes mantenerte en pie. ¿Qué haces cuando termina?", "steps": ["Puede venir un tsunami.", "Voy de inmediato a una zona alta, caminando por la ruta de evacuación."], "answer": "Evacuar de inmediato a una zona alta"},
        {"title": "Caída de ceniza", "problem": "Cae ceniza de un volcán cerca de tu casa. ¿Cómo proteges tu respiración?", "steps": ["La ceniza puede irritar la nariz y la garganta.", "Me cubro nariz y boca con un paño húmedo y evito salir."], "answer": "Cubrirme nariz y boca con un paño húmedo y evitar salir"},
    ],
    mistakes=[
        {"wrong": "Esperar a ver si el mar se retira antes de evacuar.", "why": "Se piensa que se puede ver venir el tsunami.", "fix": "Si el sismo es fuerte, evacúa de inmediato sin esperar señales del mar."},
        {"wrong": "Volver a la playa apenas pasa la primera ola.", "why": "Se cree que el peligro terminó.", "fix": "Pueden venir más olas; espera la autorización oficial."},
    ],
    tiers={
        "recovery": [
            ex("Si hay peligro de tsunami, ¿vas a una zona alta o a la playa?", "A una zona alta", "El mar no llega a los lugares altos."),
            ex("Cuando cae ceniza volcánica, ¿te cubres la nariz y la boca o las dejas descubiertas?", "Me las cubro", "La ceniza irrita la respiración."),
            ex("Completa: una ___ es un aviso oficial de peligro (alerta o fiesta).", "alerta", "Avisa de un posible peligro."),
        ],
        "understand": [
            ex("¿Por qué no se debe esperar a ver el mar retirarse para evacuar?", "Porque puede no haber señal y el tiempo es poco", "Hay que irse apenas termina el sismo fuerte."),
            ex("¿Por qué no se vuelve a la playa tras la primera ola?", "Porque pueden llegar más olas", "El peligro puede continuar."),
            ex("¿Qué indicaciones debe seguir una familia que vive cerca de un volcán?", "Las de las autoridades de emergencia", "Ellas informan sobre las alertas."),
        ],
        "apply": [
            ex("Clasifica cada medida como tsunami o erupción: ir a una zona alta; cubrirse nariz y boca con un paño húmedo.", "Ir a una zona alta: tsunami. Cubrirse nariz y boca: erupción", "Cada medida protege del peligro propio de cada fenómeno."),
            ex("Después de un sismo fuerte en la costa, una niña ve que el mar sigue tranquilo. ¿Debe evacuar igual?", "Sí", "El tsunami puede llegar aunque el mar parezca normal."),
            arith("La zona alta queda a 800 m de la casa. Si caminas 100 m por minuto, ¿cuántos minutos tardas?", "800//100", "Se divide la distancia por los metros por minuto.", " minutos"),
        ],
        "reason": [
            ex("Un compañero dice que, como su casa está lejos del volcán, no necesita estar atento a las alertas. ¿Qué respondes?", "La ceniza puede viajar lejos y las alertas dicen si hay peligro", "Hay que informarse aunque se viva lejos."),
            ex("Dos rutas hacia la zona alta: una de 500 m por calle despejada y otra de 400 m cruzando una zona de escombros. ¿Cuál eliges y por qué?", "La de 500 m despejada, porque es más segura", "Una ruta libre evita riesgos."),
        ],
        "challenge": [
            arith("Un barrio costero tiene 240 personas y se evacúan en 6 grupos iguales. ¿Cuántas personas hay en cada grupo?", "240//6", "Se divide el total en grupos iguales.", " personas"),
            ex("Una familia de la costa sale del sismo y quiere volver a buscar un juguete a la casa. ¿Es una buena decisión?", "No", "Hay que evacuar primero y no regresar hasta que indiquen."),
        ],
    },
    context=[ex("En un balneario, un guardia explica: «si sienten un temblor muy fuerte, no esperen aviso, vayan al cerro». ¿Qué fenómeno quiere prevenir?", "Un tsunami", "Un sismo fuerte cerca de la costa puede provocarlo.")],
    selfcheck=[
        ex("¿Adónde se evacúa ante un tsunami?", "A una zona alta", "Lejos del mar."),
        ex("¿Qué cubrimos si cae ceniza?", "La nariz y la boca", "Se protege la respiración."),
        ex("¿De quién son las indicaciones que seguimos en una alerta?", "De las autoridades de emergencia", "Ellas informan y coordinan."),
    ],
    open_task=task(
        "Haz un cuadro con dos columnas: tsunami y erupción volcánica. Anota para cada una tres medidas de seguridad. Si vives lejos de la costa o de un volcán, igual escribe cómo se preparan las personas que sí viven cerca. Agrega una pregunta que harías en tu barrio sobre qué zona es segura.",
        "Tsunami: ir a una zona alta, no esperar aviso, no volver hasta que lo indiquen. Erupción: cubrir nariz y boca, proteger agua y alimentos, estar atento a las alertas. Pregunta: ¿dónde queda la zona alta más cercana?",
        ["tres medidas por fenómeno", "las medidas corresponden al riesgo", "formula una pregunta"],
        ["cuadro de dos columnas", "pregunta escrita"],
        ["mezclar medidas de los dos fenómenos", "proponer volver pronto a la playa"],
        "Valora las medidas correctas y pide revisar las que no corresponden al fenómeno.",
    ),
    reinforce="Con una persona de tu casa, averigua cuál es el cerro o la calle más alta cerca de tu casa o de tu escuela.",
    extend="Averigua cómo se ven los letreros de «zona de evacuación por tsunami» en Chile.",
)

register(
    OA17, 4,
    materials="Papel, lápiz y una mochila vacía o una lista. No hace falta comprar nada: la lista se escribe y se conversa con una persona de tu casa.",
    use="Aprenderé a proponer un plan de prevención para la escuela, la calle y el hogar, con medidas claras. Sirve para crear una cultura preventiva, es decir, cuidarnos entre todas y todos los días.",
    prior=["Sé qué hacer en un sismo, un tsunami y una erupción.", "Sé distinguir prevención y seguridad."],
    explain=[
        "Una cultura preventiva es una forma de vivir en la que todas las personas se preparan, se cuidan y se informan antes de que ocurra una emergencia. No depende de una sola persona: lo practican la familia, la escuela y la comunidad.",
        "Una buena propuesta de prevención tiene un problema claro, una medida concreta, una persona responsable y un plazo. Por ejemplo: «La delegada o el delegado revisa que las salidas de la sala estén despejadas el lunes próximo». Si una medida es muy general, como «tener cuidado», no sirve porque no dice qué hacer.",
        "Una mochila de emergencia ayuda en el hogar. Puede tener agua, alimentos que no se echen a perder, una linterna con pilas, un radio a pilas, abrigo y copias de documentos. También ayuda un plan familiar con punto de encuentro y números de emergencia: 131 ambulancia, 132 bomberos y 133 Carabineros.",
    ],
    vocab=[("cultura preventiva", "forma de vivir en que todos se preparan y se cuidan antes de una emergencia"), ("mochila de emergencia", "mochila con lo básico para sobrevivir unas horas o días"), ("punto de encuentro", "lugar acordado para reunirse después de una emergencia"), ("responsable", "persona que se encarga de una tarea"), ("plazo", "fecha o tiempo para cumplir algo")],
    worked=[
        {"title": "Medida concreta", "problem": "¿Cuál es mejor medida: «tener cuidado» o «sujetar la biblioteca a la pared esta semana»?", "steps": ["La segunda dice qué hacer y cuándo.", "La primera es demasiado general."], "answer": "Sujetar la biblioteca a la pared esta semana"},
        {"title": "Mochila de emergencia", "problem": "Elige lo básico para una mochila de emergencia entre estas tres cosas: linterna con pilas, agua, un juguete. ¿Qué no debe faltar?", "steps": ["El agua y la linterna son básicas en una emergencia.", "El juguete es opcional."], "answer": "Agua y linterna con pilas"},
    ],
    mistakes=[
        {"wrong": "Proponer medidas generales como «ser cuidadosos».", "why": "No dicen qué hacer ni quién.", "fix": "Escribe una acción, un responsable y un plazo."},
        {"wrong": "Creer que la prevención es solo tarea de los adultos.", "why": "Parece difícil para estudiantes.", "fix": "Los niños y niñas también pueden participar, por ejemplo practicando el simulacro."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál número llamas para pedir Bomberos?", "132", "Es el número de Bomberos en Chile."),
            ex("¿Cuál número llamas para pedir Carabineros?", "133", "Es el número de Carabineros."),
            ex("¿Cuál número llamas para pedir una ambulancia?", "131", "Es el número de ambulancia."),
        ],
        "understand": [
            ex("¿Qué es una cultura preventiva?", "Que todos se preparan y se cuidan antes de una emergencia", "No depende de una sola persona."),
            ex("¿Para qué sirve un punto de encuentro familiar?", "Para reunirse después de una emergencia", "Así nadie se pierde de la familia."),
            ex("¿Por qué una medida debe tener un plazo?", "Para saber cuándo se cumple", "Sin fecha no se sabe si se hizo."),
        ],
        "apply": [
            ex("Elige la medida bien escrita: A) «tener cuidado»; B) «el curso despeja la salida de la sala antes del viernes».", "B", "Dice qué hacer, quién y cuándo."),
            ex("Clasifica como imprescindible o no para una mochila de emergencia: linterna con pilas; videojuego; agua.", "Linterna: imprescindible. Videojuego: no imprescindible. Agua: imprescindible", "Los dos necesarios sirven para sobrevivir en una emergencia."),
            arith("Supón que una familia de 4 personas necesita 2 litros de agua por persona para un día. ¿Cuántos litros necesita para 1 día?", "4*2", "Se multiplica el número de personas por los litros de cada una.", " litros"),
        ],
        "reason": [
            ex("Dos propuestas para la calle: A) «los vecinos revisan los maceteros de los balcones del edificio cada mes»; B) «cuidar la calle». ¿Cuál es más útil y por qué?", "La A, porque dice qué hacer y cada cuánto", "Es concreta y puede cumplirse."),
            ex("Ana dice que su familia no necesita un plan porque nunca ha pasado nada. ¿Qué respondes?", "Prevenir sirve justo para cuando ocurra un fenómeno", "Los sismos son frecuentes en Chile."),
        ],
        "challenge": [
            arith("Supón que una familia de 4 personas necesita 2 litros de agua por persona por día y la mochila debe alcanzar para 3 días. ¿Cuántos litros se necesitan?", "4*2*3", "Se multiplican personas, litros y días.", " litros"),
            ex("¿Cuál medida tiene acción, responsable y plazo? A) «cuidar los estantes»; B) «la familia sujeta el estante de la pieza este sábado»; C) «ojalá no se caigan».", "B", "Dice qué se hace, quién y cuándo."),
        ],
    },
    context=[ex("La directora de una escuela pregunta qué medida conviene primero para el patio: pintar la zona de seguridad con color visible o hacer una charla general. ¿Cuál es una medida más concreta para disminuir el riesgo?", "Pintar la zona de seguridad con color visible", "Todos pueden ver y reconocer el lugar.")],
    selfcheck=[
        ex("¿Qué debe tener una buena propuesta de prevención?", "Una acción concreta, un responsable y un plazo", "Así se puede cumplir."),
        ex("¿Qué número llamas para Bomberos?", "132", "Es el número de emergencia de Bomberos."),
        ex("¿Quiénes participan de la cultura preventiva?", "Toda la familia, la escuela y la comunidad", "Es tarea de todos."),
    ],
    open_task=task(
        "Escribe una propuesta de prevención para cada lugar: escuela, calle y hogar. Cada una debe decir qué se hace, quién lo hace y cuándo. Puedes usar estos ejemplos como guía: escuela, despejar la vía de evacuación; calle, avisar de un cable suelto a una persona adulta; hogar, armar una mochila de emergencia con una persona de tu casa. Agrega los tres números de emergencia.",
        "Escuela: el curso despeja la vía de evacuación antes del viernes. Calle: aviso de un cable suelto a un adulto cuando lo veo. Hogar: armamos la mochila este mes. Números: 131, 132 y 133.",
        ["tres propuestas en tres lugares", "cada una con acción, responsable y plazo", "incluye los números de emergencia"],
        ["tabla de tres filas", "lista de números"],
        ["propuestas demasiado generales", "olvidar el responsable o el plazo"],
        "Reconoce propuestas concretas y pide precisar el responsable o el plazo cuando falte.",
    ),
    reinforce="Conversa con una persona de tu casa sobre un punto de encuentro y anótalo.",
    extend="Averigua qué hace el organismo nacional que informa sobre las emergencias en Chile y cómo puedes enterarte de sus alertas.",
)
