"""Cuaderno del estudiante, 5.º básico Orientación: OA 07 (estrategias autónomas para resolver conflictos) y OA 08 (participación democrática y organización del curso)."""
from __future__ import annotations

from student_lessons import arith, ex
from student_content_or5_a import M, T, W, lesson

OA7, OA8 = "OR05 OA 07", "OR05 OA 08"

# ================================================================ OA 07
lesson(
    OA7, 1,
    "Una hoja y un lápiz. El caso de Sam y Noa está escrito en los ejercicios. Trabajas con personajes inventados.",
    "Aprenderé a reconocer qué es un conflicto, en qué se diferencia de la violencia y cuál es el problema de fondo. Sirve para resolver desacuerdos con calma y de forma autónoma.",
    ["Sé separar hecho, emoción y límite.", "Sé usar un mensaje «yo»."],
    [
        "Un conflicto es un desacuerdo entre personas que quieren cosas distintas o que piensan distinto. Los conflictos son normales y pueden resolverse. No son lo mismo que la violencia. La violencia hiere. Un conflicto puede resolverse con diálogo, pero si se resuelve con golpes, insultos o amenazas, deja de ser solo un conflicto y pasa a ser violencia.",
        "En un conflicto hay tres partes que conviene distinguir. El problema es el motivo del desacuerdo. La posición es lo que cada persona dice que quiere: «yo quiero el balón». El interés es la razón detrás: «quiero jugar con mi equipo». Dos posiciones distintas pueden tener intereses que se pueden combinar. Mirar los intereses ayuda a encontrar soluciones.",
        "Por ejemplo, Sam y Noa, dos estudiantes inventados, quieren usar la única mesa grande de la sala. Sam dice «yo la uso primero» y Noa dice «yo ya estaba aquí». El problema es que hay una mesa para dos grupos. Los intereses son terminar sus trabajos a tiempo. Una solución puede ser turnarse o dividir la mesa.",
    ],
    [("conflicto", "desacuerdo entre personas que quieren o piensan cosas distintas"), ("violencia", "acción que hiere a otro"), ("posición", "lo que cada persona dice que quiere"), ("interés", "la razón que hay detrás de lo que quiere"), ("solución", "salida que resuelve el problema")],
    [
        W("Conflicto o violencia", "Dos niños discuten por el turno en el computador y uno empuja al otro. ¿Qué parte es violencia?", ["La discusión es el desacuerdo.", "Empujar hiere.", "Eso es violencia."], "El empujón"),
        W("Posición e interés", "Sam dice: «Yo quiero la mesa». Su razón: «Necesito terminar el cartel hoy». ¿Cuál es la posición y cuál el interés?", ["Lo que dice que quiere es la posición.", "La razón detrás es el interés.", "El interés es terminar el cartel hoy."], "Posición: quiere la mesa. Interés: terminar el cartel hoy"),
    ],
    [
        M("Pensar que tener un conflicto significa ser mala persona.", "Se confunde desacuerdo con maldad.", "Los conflictos son normales; lo importante es cómo se resuelven."),
        M("Creer que gana el que grita más fuerte.", "Se piensa que la fuerza resuelve.", "La fuerza no resuelve el problema, solo lo empeora."),
    ],
    R=[
        ex("Un desacuerdo por el turno del balón, ¿es un conflicto?", "Sí", "Hay dos personas que quieren algo distinto."),
        ex("Empujar a alguien, ¿es violencia?", "Sí", "Empujar hiere el cuerpo de otra persona."),
        ex("«Quiero la mesa» ¿es una posición o un interés?", "Una posición", "Dice lo que la persona quiere, no la razón."),
    ],
    U=[
        ex("¿Por qué un conflicto no siempre es violencia?", "Porque puede resolverse con diálogo", "Solo es violencia si hiere."),
        ex("En Orientación: ¿qué es el interés en un conflicto?", "La razón que hay detrás de lo que alguien quiere", "Explica por qué lo quiere."),
        ex("¿Por qué mirar los intereses ayuda a encontrar soluciones?", "Porque se pueden combinar", "Dos posiciones distintas pueden tener intereses compatibles."),
    ],
    A=[
        ex("Frases: 1) «Quiero el balón», 2) «Necesito el balón para entrenar con mi equipo», 3) «Tú no juegas». ¿Cuál es el interés?", "La frase 2", "Explica la razón detrás de lo que quiere."),
        ex("Sam y Noa quieren la mesa. ¿Qué solución combina sus intereses: turnarse o pelear?", "Turnarse", "Ambos pueden terminar sus trabajos."),
        ex("Situaciones: 1) discutir por un lápiz, 2) insultar, 3) amenazar, 4) turnarse. ¿Cuántas son violencia?", "2", "Insultar y amenazar hieren; las otras no."),
    ],
    Z=[
        ex("¿Por qué gritar no resuelve el problema aunque parezca que gana?", "Porque el problema sigue y se suma otro", "El otro se defiende y no se resuelve."),
        ex("Dos niños quieren sentarse junto a la ventana. ¿Cuál es el problema de fondo: hay un solo asiento junto a la ventana o uno de los dos es mejor que el otro?", "Hay un solo asiento junto a la ventana", "El problema es que dos quieren lo mismo y solo hay uno."),
    ],
    D=[
        arith("En un curso de 30 estudiantes, 18 dicen que han tenido un desacuerdo esta semana y lo resolvieron con diálogo. ¿Cuántos no lo han tenido?", "30-18", "Se restan los que lo tuvieron al total."),
        arith("Sam y Noa dividen una mesa de 120 centímetros en partes iguales. ¿Cuántos centímetros recibe cada uno?", "120//2", "Se divide la mesa entre dos."),
    ],
    context=[ex("Dos estudiantes inventados quieren el mismo libro de la biblioteca de aula. Uno lo quiere para un trabajo y el otro para leerlo por gusto. ¿Cuál es el problema?", "Hay un solo libro para dos personas", "Dos personas quieren lo mismo y hay uno.")],
    selfcheck=[ex("En Orientación: ¿los conflictos son normales?", "Sí", "Aparecen cuando hay opiniones distintas."), ex("¿La violencia resuelve conflictos?", "No", "La violencia empeora los conflictos."), ex("¿Mirar los intereses ayuda?", "Sí", "Entender las razones abre soluciones.")],
    task=T("Lee el caso: «Sam y Noa necesitan la mesa grande al mismo tiempo. Sam dice: “yo la uso primero”, porque necesita terminar un cartel hoy. Noa dice: “yo ya estaba aquí”, porque debe pegar su informe antes del recreo». Escribe: el problema, la posición de cada uno, el interés de cada uno y una solución que sirva a ambos.", "Problema: una mesa para dos. Posición de Sam: usarla primero. Interés de Sam: terminar el cartel. Posición de Noa: ya estaba aquí. Interés: pegar el informe. Solución: Noa pega en 5 minutos y luego Sam usa la mesa.", ["escribe el problema", "posición e interés de cada uno", "solución que sirve a ambos"], ["tabla escrita"], ["confundir posición con interés", "solución con violencia"], "Reconoce la distinción y pregunta cómo se sentiría cada uno."),
    reinforce="Escribe un conflicto cotidiano del colegio y separa problema, posiciones e intereses.",
    extend="Explica la diferencia entre un conflicto y un acto de violencia.",
)

lesson(
    OA7, 2,
    "Una hoja y un lápiz. El caso de Noa y Sam y las frases están escritos en los ejercicios.",
    "Aprenderé a escuchar, a distinguir hechos de interpretaciones y a decir mis emociones en un conflicto. Sirve para entender al otro antes de buscar soluciones.",
    ["Sé qué es un conflicto y sus partes.", "Sé usar un mensaje «yo»."],
    [
        "Antes de buscar soluciones hay que entender al otro. Escuchar activamente es mirar a la persona, no interrumpir y repetir con tus palabras lo que entendiste: «Entiendo que te molestó que usara la mesa sin avisar. ¿Es así?». Así la otra persona se siente escuchada y baja la tensión.",
        "En un conflicto se mezclan hechos, interpretaciones y emociones. El hecho es lo que ocurrió: «Sam tomó la mesa». La interpretación es lo que uno cree que significa: «lo hizo para fastidiarme». La interpretación puede estar equivocada. La emoción es lo que sientes: rabia o frustración. Cuenta primero el hecho y la emoción, y pregunta antes de suponer.",
        "También puedes poner un límite: «No te permito que me grites, pero quiero escucharte». Un límite protege el respeto. Si la discusión se vuelve muy intensa, pide una pausa: «Necesito unos minutos para calmarme y luego seguimos». Pausar no es huir; es cuidar la conversación.",
    ],
    [("escucha activa", "mirar, no interrumpir y repetir lo que entendí"), ("interpretación", "lo que uno cree que significa algo, sin comprobarlo"), ("pausa", "detener la conversación unos minutos para calmarse"), ("tensión", "clima de molestia entre personas"), ("límite", "lo que no acepto en la conversación")],
    [
        W("Hecho o interpretación", "Noa dice: «Sam tomó la mesa porque quiere fastidiarme». ¿Qué parte es la interpretación?", ["El hecho es que tomó la mesa.", "«Quiere fastidiarme» es lo que Noa cree.", "No lo comprobó."], "«Quiere fastidiarme»"),
        W("Escucha activa", "Sam dice: «Me enojé porque usaste la mesa sin avisarme». Noa responde: «Entiendo que te enojó que la usara sin avisar. ¿Es así?». ¿Qué técnica usó?", ["Repite con sus palabras lo que entendió.", "Pregunta si lo entendió bien.", "Eso es escucha activa."], "Escucha activa"),
    ],
    [
        M("Interrumpir para explicar mi versión primero.", "Se teme que no me crean.", "Escucha primero y luego cuenta tu parte."),
        M("Creer que mi interpretación es un hecho.", "Se confunde suponer con saber.", "Pregunta antes de suponer."),
    ],
    R=[
        ex("Repetir con tus palabras lo que entendiste, ¿es escucha activa?", "Sí", "Muestra que escuchaste."),
        ex("«Lo hizo para fastidiarme». ¿Es un hecho o una interpretación?", "Una interpretación", "Es lo que uno cree, no lo que se comprobó."),
        ex("Pedir una pausa para calmarte, ¿es cuidar la conversación?", "Sí", "Evita decir cosas que hieren."),
    ],
    U=[
        ex("¿Por qué conviene preguntar antes de suponer?", "Porque la interpretación puede estar equivocada", "Preguntar permite comprobar."),
        ex("¿Por qué escuchar al otro baja la tensión?", "Porque se siente escuchado", "Cuando alguien se siente escuchado, se calma."),
        ex("¿Qué diferencia hay entre pausar y huir?", "La pausa tiene la intención de seguir hablando", "Se vuelve a conversar con calma."),
    ],
    A=[
        ex("Frases: 1) «Sam tomó la mesa», 2) «Seguro lo hizo a propósito», 3) «Me enojé». ¿Cuál es el hecho?", "La frase 1", "Cuenta lo ocurrido sin suponer."),
        ex("Noa quiere poner un límite sin ofender. ¿Cuál frase sirve: «No te permito que me grites, pero quiero escucharte» o «Cállate»?", "«No te permito que me grites, pero quiero escucharte»", "Pone un límite y mantiene el respeto."),
        ex("Completa con la técnica: «Entiendo que te molestó…, ¿es así?». ¿Se llama escucha activa o interrupción?", "Escucha activa", "Repite lo entendido y pregunta."),
    ],
    Z=[
        ex("Dos estudiantes discuten y se interrumpen todo el tiempo. ¿Qué paso falta para entenderse?", "Escuchar sin interrumpir", "Sin escucha, cada uno solo defiende lo suyo."),
        ex("¿Por qué una interpretación equivocada puede empeorar un conflicto?", "Porque se reacciona a algo que quizás no es cierto", "La reacción no corresponde a la realidad."),
    ],
    D=[
        arith("Una pausa de calma dura 3 minutos. Si Sam y Noa hacen 2 pausas en una discusión, ¿cuántos minutos de pausa fueron?", "3*2", "Son 3 minutos repetidos dos veces."),
        arith("En una conversación, Noa habló 5 minutos y Sam 4. ¿Cuántos minutos duró en total?", "5+4", "Se suman los dos tiempos."),
    ],
    context=[ex("Mía y Luz discuten por un trabajo en grupo. Luz dice: «Entiendo que sentiste que no te tomé en cuenta. ¿Es así?». ¿Qué hizo Luz?", "Escucha activa", "Repitió lo entendido y preguntó.")],
    selfcheck=[ex("En Orientación: ¿conviene escuchar antes de hablar?", "Sí", "Permite entender al otro."), ex("¿Una interpretación es siempre un hecho?", "No", "Puede estar equivocada."), ex("¿Una pausa puede ayudar?", "Sí", "Una pausa permite calmarse.")],
    task=T("Lee la discusión: Sam: «Me enojé porque usaste la mesa sin avisarme». Noa: «¡No es tu mesa!». Reescribe la respuesta de Noa usando escucha activa, un mensaje «yo» y, si hace falta, una pausa. Luego escribe qué hecho, qué interpretación y qué emoción hay en la frase de Sam.", "Noa: «Entiendo que te enojó que usara la mesa sin avisar. Yo no sabía que la necesitabas; me sentí sorprendida. ¿Podemos hablar con calma?». Hecho: usé la mesa. Interpretación: no hay. Emoción: enojo.", ["usa escucha activa", "usa mensaje «yo»", "identifica hecho, interpretación y emoción"], ["texto escrito o dicho"], ["responder con ataque", "confundir interpretación con hecho"], "Reconoce el cambio y pregunta cómo respondería Sam."),
    reinforce="Escribe tres frases de escucha activa que podrías usar.",
    extend="Escribe una situación en que supusiste algo y estabas equivocado (inventada) y qué habrías preguntado.",
)

lesson(
    OA7, 3,
    "Una hoja y un lápiz. Las opciones y el caso de Sam y Noa están escritos en los ejercicios.",
    "Aprenderé a comparar estrategias para resolver conflictos (dialogar, negociar, turnos, sorteo, mediación y pedir ayuda) y sus consecuencias. Sirve para elegir una estrategia que deje a todos conformes.",
    ["Sé escuchar y distinguir hecho de interpretación.", "Sé separar posición e interés."],
    [
        "Hay varias estrategias para resolver un conflicto. Dialogar es conversar con respeto para entender y buscar una salida. Negociar es buscar un acuerdo en que cada uno cede algo. Turnarse es usar algo uno después del otro. Sortear es dejar que decida el azar, como lanzar una moneda, cuando ambos están de acuerdo. La mediación es pedir a una tercera persona, como un compañero o un adulto, que ayude a conversar sin tomar partido. Y pedir ayuda a un adulto es una opción si el conflicto no avanza o hay violencia.",
        "Cada estrategia tiene consecuencias. Ganar-perder es cuando uno consigue todo y el otro nada: deja resentimiento. Perder-perder es cuando nadie consigue nada y se enojan los dos. Ganar-ganar es cuando ambos consiguen algo importante: es lo más estable. Para elegir, pregúntate: ¿sirve a los intereses de ambos?, ¿es justa?, ¿se puede cumplir?",
        "Por ejemplo, Sam y Noa pueden turnarse la mesa 10 minutos cada uno. Si Sam usa la mesa todo el rato y Noa nada, es ganar-perder. Si ambos se quedan sin mesa, es perder-perder. Y si cada uno la usa un rato, es ganar-ganar.",
    ],
    [("negociar", "buscar un acuerdo en que cada uno cede algo"), ("mediación", "ayuda de una tercera persona que no toma partido"), ("ganar-ganar", "solución en que ambos consiguen algo importante"), ("sortear", "dejar que decida el azar"), ("acuerdo", "decisión que ambos aceptan")],
    [
        W("Tipo de solución", "Sam usa la mesa toda la mañana y Noa no la usa. ¿Es ganar-ganar, ganar-perder o perder-perder?", ["Uno consigue todo.", "El otro no consigue nada.", "Es ganar-perder."], "Ganar-perder"),
        W("Elegir una estrategia", "Sam y Noa se turnan la mesa 10 minutos cada uno. ¿Qué estrategia usan y qué tipo de solución es?", ["Usan la mesa uno después del otro.", "Turnarse sirve a los dos.", "Es ganar-ganar."], "Turnarse; ganar-ganar"),
    ],
    [
        M("Creer que resolver un conflicto es que yo gane.", "Se confunde ganar con resolver.", "Busca una solución en que ambos consigan algo."),
        M("Esperar que la profesora lo resuelva siempre.", "Se piensa que solo los adultos pueden.", "Prueba primero el diálogo y pide ayuda si no avanza."),
    ],
    R=[
        ex("Usar algo uno después del otro, ¿se llama turnarse o sortear?", "Turnarse", "Cada uno lo usa en su turno."),
        ex("Una tercera persona que ayuda a conversar sin tomar partido, ¿hace mediación?", "Sí", "Su papel es ayudar a que se entiendan."),
        ex("Una solución en que ambos consiguen algo importante, ¿es ganar-ganar?", "Sí", "Ambos quedan conformes."),
    ],
    U=[
        ex("¿Por qué ganar-perder deja resentimiento?", "Porque el que pierde se siente injustamente tratado", "El que pierde queda enojado."),
        ex("¿Cuándo es mejor pedir ayuda a un adulto?", "Cuando el conflicto no avanza o hay violencia", "Un adulto puede ayudar con calma y seguridad."),
        ex("¿Qué tres preguntas ayudan a elegir una estrategia?", "Si sirve a ambos, si es justa y si se puede cumplir", "Eso asegura un acuerdo estable."),
    ],
    A=[
        ex("Estrategias: 1) dialogar, 2) gritar, 3) turnarse, 4) sortear con acuerdo de ambos. ¿Cuántas sirven para resolver sin violencia?", "3", "Dialogar, turnarse y sortear con acuerdo no hieren; gritar sí."),
        ex("Sam y Noa quieren el mismo balón. Se turnan 5 minutos cada uno. ¿Qué tipo de solución es?", "Ganar-ganar", "Los dos juegan."),
        ex("Si los dos se quedan sin balón porque se enojaron, ¿qué tipo de solución es?", "Perder-perder", "Ninguno consiguió lo que quería."),
    ],
    Z=[
        ex("¿Por qué sortear con una moneda solo es justo si ambos están de acuerdo?", "Porque si uno no acepta, no será un acuerdo", "El acuerdo es lo que lo hace justo."),
        ex("Dos niños no logran ponerse de acuerdo y se están insultando. ¿Qué estrategia conviene?", "Pedir ayuda a un adulto", "Hay riesgo de violencia."),
    ],
    D=[
        arith("Sam y Noa se turnan la mesa en bloques de 10 minutos durante 1 hora (60 minutos). ¿Cuántos bloques de 10 minutos hay?", "60//10", "Se divide el tiempo en bloques."),
        arith("De 5 estrategias propuestas por un curso, 3 fueron ganar-ganar. ¿Cuántas no lo fueron?", "5-3", "Se restan las ganar-ganar al total."),
    ],
    context=[ex("Dos estudiantes inventados quieren el único computador. Acuerdan 15 minutos cada uno, y un compañero que no participa del conflicto los ayudó a conversar sin tomar partido. ¿Qué estrategias usaron?", "Turnarse y mediación", "Se turnan y un tercero los ayuda a ponerse de acuerdo.")],
    selfcheck=[ex("En Orientación: ¿ganar-ganar deja conformes a ambos?", "Sí", "Ambos consiguen algo."), ex("¿Conviene pedir ayuda si hay violencia?", "Sí", "Es una opción segura."), ex("¿Negociar es que cada uno cede algo?", "Sí", "Se llega a un acuerdo.")],
    task=T("Lee: «Tres estudiantes quieren usar el único balón en un recreo de 18 minutos». Propón tres estrategias (por ejemplo: turnarse, negociar, sortear). Para cada una escribe qué pasaría y si es ganar-ganar, ganar-perder o perder-perder. Elige la mejor con las tres preguntas.", "Turnarse 6 minutos cada uno: ganar-ganar; es justa y se puede cumplir. Sorteo: uno juega todo el rato; ganar-perder. Pelear: nadie juega; perder-perder. Elijo turnarse.", ["tres estrategias", "tipo de solución de cada una", "elige la mejor con las tres preguntas"], ["tabla escrita"], ["elegir pelear", "no considerar a los tres"], "Reconoce la comparación y pregunta cómo se cumpliría el acuerdo."),
    reinforce="Escribe una solución ganar-ganar para dos niños que quieren sentarse en el mismo lugar.",
    extend="Explica cuándo conviene pedir mediación de un compañero.",
)

lesson(
    OA7, 4,
    "Una hoja y un lápiz. El caso de Alex y los pasos están escritos en los ejercicios.",
    "Aprenderé a aplicar una secuencia de pasos para resolver un conflicto y a reconocer cuándo debo pedir ayuda. Sirve para resolver problemas de convivencia de manera segura y autónoma.",
    ["Sé comparar estrategias para resolver conflictos.", "Sé escuchar de forma activa."],
    [
        "Para resolver un conflicto de forma autónoma puedes seguir siete pasos. 1) Parar y calmarte. 2) Escuchar a la otra persona. 3) Contar tu parte con un mensaje «yo». 4) Pensar en varias soluciones. 5) Elegir una que sirva a ambos. 6) Hacer un acuerdo claro: quién hace qué y hasta cuándo. 7) Revisar después si el acuerdo funcionó.",
        "Un acuerdo claro dice quién, qué y cuándo. «Nos turnaremos la mesa: Sam 10 minutos y luego Noa 10 minutos». Un acuerdo vago, como «nos portaremos bien», no se puede comprobar. Si el acuerdo no funciona, se vuelve a conversar y se ajusta.",
        "No todos los conflictos se resuelven solos. Si hay golpes, amenazas, acoso o una persona se siente en peligro, no intentes resolverlo solo: avisa a un adulto de inmediato. Pedir ayuda en esos casos es la acción más segura y responsable.",
    ],
    [("acuerdo claro", "dice quién hace qué y hasta cuándo"), ("revisar", "mirar después si algo funcionó"), ("autónomo", "que lo hago por mí mismo"), ("amenaza", "palabra o gesto que busca asustar"), ("acoso", "agresión que se repite contra una persona")],
    [
        W("Ordenar los pasos", "Alex y Mía discuten por un trabajo. ¿Qué paso va primero: parar y calmarse o hacer un acuerdo?", ["Primero hay que calmarse.", "Luego se escucha y se cuenta.", "Al final se acuerda y se revisa."], "Parar y calmarse"),
        W("Acuerdo claro", "¿Qué acuerdo es más claro: «nos turnaremos el computador 15 minutos cada uno hasta el recreo» o «nos portaremos bien»?", ["El primero dice quién, cuánto y hasta cuándo.", "El segundo es vago.", "Se puede comprobar."], "«Nos turnaremos el computador 15 minutos cada uno hasta el recreo»"),
    ],
    [
        M("Hacer un acuerdo vago para terminar rápido.", "Se quiere evitar más discusión.", "Escribe quién hace qué y hasta cuándo."),
        M("Intentar resolver solo una amenaza.", "Se cree que pedir ayuda es debilidad.", "Si hay amenazas o violencia, avisa a un adulto."),
    ],
    R=[
        ex("Calmarse, ¿es el primer paso para resolver un conflicto?", "Sí", "Con calma se piensa mejor."),
        ex("Un acuerdo claro, ¿dice quién, qué y cuándo?", "Sí", "Así se puede comprobar."),
        ex("Si hay amenazas, ¿resuelves solo o avisas a un adulto?", "Avisas a un adulto", "Es la acción más segura."),
    ],
    U=[
        ex("¿Por qué revisar el acuerdo después es el último paso?", "Para ver si funcionó y ajustarlo", "Sin revisión no se sabe si sirvió."),
        ex("¿Por qué «nos portaremos bien» es un acuerdo débil?", "Porque no se puede comprobar", "No dice quién, qué ni cuándo."),
        ex("¿Qué hacer si el acuerdo no funciona?", "Volver a conversar y ajustar", "Un acuerdo puede mejorarse."),
    ],
    A=[
        ex("Pasos: 1) escuchar, 2) parar y calmarse, 3) revisar el acuerdo, 4) elegir la solución. ¿Cuál va primero?", "Parar y calmarse", "Es el paso inicial."),
        ex("Alex y Mía acuerdan: «Mía lee el lunes y Alex el martes». ¿El acuerdo es claro?", "Sí", "Dice quién, qué y cuándo."),
        ex("Un compañero amenaza con pegarle a Alex si no le da su merienda. ¿Qué paso es el más seguro?", "Avisar a un adulto", "Hay una amenaza."),
    ],
    Z=[
        ex("¿Por qué es mejor pensar varias soluciones antes de elegir una?", "Porque así se encuentra la que sirve a ambos", "Más opciones permiten elegir mejor."),
        ex("¿Por qué ciertos conflictos no deben resolverse solos?", "Porque hay riesgo de daño", "Con golpes o amenazas se necesita un adulto."),
    ],
    D=[
        arith("Un acuerdo de turnos dura 40 minutos y se divide entre 4 estudiantes por igual. ¿Cuántos minutos tiene cada uno?", "40//4", "Se divide el tiempo entre los cuatro."),
        arith("Alex revisó su acuerdo 3 veces la primera semana y 2 la segunda. ¿Cuántas veces lo revisó?", "3+2", "Se suman las revisiones."),
    ],
    context=[ex("Tras una discusión, dos niños inventados acuerdan: «Cada uno usará el computador 10 minutos por turno; el viernes revisaremos si funcionó». ¿Cumplen los pasos de acuerdo y revisión?", "Sí", "El acuerdo es claro y tiene fecha de revisión.")],
    selfcheck=[ex("En Orientación: ¿hay que calmarse antes de resolver?", "Sí", "Con calma se decide mejor."), ex("¿Un acuerdo claro dice quién, qué y cuándo?", "Sí", "Se puede comprobar."), ex("¿Se avisa a un adulto si hay amenazas?", "Sí", "Es lo más seguro.")],
    task=T("Lee el caso: «Alex y Mía tienen un trabajo en grupo y discuten porque Alex no llevó su parte. Mía está enojada». Aplica los siete pasos: escribe una frase o acción para cada paso. Incluye un acuerdo claro con quién, qué y cuándo.", "1) Respiramos. 2) Escucho a Mía. 3) «Me siento mal por no haber llevado mi parte». 4) Soluciones: hacerlo hoy, pedir más tiempo. 5) Elegimos hoy. 6) Alex lleva su parte mañana a las 9. 7) El viernes revisamos.", ["los siete pasos", "acuerdo claro", "usa mensaje «yo»"], ["lista escrita"], ["saltar pasos", "acuerdo vago"], "Reconoce la secuencia y pregunta cómo saben si funcionó."),
    reinforce="Escribe un acuerdo claro para repartir tareas de una exposición entre tres personas.",
    extend="Escribe dos señales de que un conflicto necesita la ayuda de un adulto.",
)

# ================================================================ OA 08
lesson(
    OA8, 1,
    "Una hoja y un lápiz. El caso del curso de Sam y los datos están escritos en los ejercicios. Trabajas con un curso inventado.",
    "Aprenderé qué es participar en la organización del curso y cómo se planifica una actividad con un objetivo. Sirve para colaborar en la comunidad escolar.",
    ["Sé que el buen trato mejora la convivencia.", "Sé trabajar en equipo."],
    [
        "Participar en el curso es involucrarse en las decisiones y en las tareas que afectan a todos. La comunidad escolar la formamos estudiantes, profesores, familias y el resto de las personas del colegio. Cada uno tiene derechos y responsabilidades. Una responsabilidad es algo que te comprometes a hacer por el bien del grupo.",
        "Para planificar una actividad con un objetivo, sigue estos pasos. Primero, define el objetivo: qué quieres lograr. Segundo, haz una lista de tareas. Tercero, reparte responsabilidades: quién hace qué. Cuarto, fija una fecha. Quinto, reúne los materiales. Y al final, evalúa: ¿se logró el objetivo?, ¿qué mejoraría?",
        "También hay problemas cotidianos que el curso puede resolver organizándose. Por ejemplo, si hay papeles en el piso al terminar el recreo, el curso puede crear turnos de limpieza. Sam, un estudiante inventado, propone una campaña para mantener la sala limpia: objetivo, tareas, responsables y fecha.",
    ],
    [("participar", "involucrarse en decisiones y tareas del grupo"), ("comunidad escolar", "estudiantes, profesores, familias y funcionarios del colegio"), ("objetivo", "lo que quiero lograr"), ("responsabilidad", "algo que me comprometo a hacer por el grupo"), ("evaluar", "revisar si se logró lo planeado")],
    [
        W("Definir un objetivo", "Sam quiere una sala limpia. ¿Qué objetivo es más claro: «Que no haya papeles en el piso después de cada recreo» o «Una sala bonita»?", ["El primero se puede comprobar.", "El segundo es vago.", "Un objetivo debe poder verificarse."], "«Que no haya papeles en el piso después de cada recreo»"),
        W("Repartir responsabilidades", "En el curso de 30 estudiantes se forman 5 equipos de limpieza iguales. ¿Cuántos estudiantes hay en cada equipo?", ["Se reparten los 30 estudiantes entre 5 equipos.", "30 dividido en 5.", "Cada equipo tiene 6."], "6 estudiantes por equipo"),
    ],
    [
        M("Creer que participar es solo mandar.", "Se confunde liderar con ordenar.", "Participar es proponer, escuchar y cumplir tu parte."),
        M("Planificar sin definir quién hace cada cosa.", "Se asume que alguien lo hará.", "Reparte responsabilidades con nombres."),
    ],
    R=[
        ex("Una responsabilidad, ¿es algo que me comprometo a hacer por el grupo?", "Sí", "Es una tarea que asumo."),
        ex("El objetivo, ¿es lo que quiero lograr?", "Sí", "Es la meta de la actividad."),
        ex("Evaluar una actividad, ¿es revisar si se logró el objetivo?", "Sí", "Permite saber qué mejorar."),
    ],
    U=[
        ex("¿Por qué conviene repartir responsabilidades con nombres?", "Para que se sepa quién hace qué", "Evita que todos esperen que otro lo haga."),
        ex("¿Qué quiere decir que un objetivo se puede comprobar?", "Que al final se puede ver si se logró", "Es claro y medible."),
        ex("En Orientación: ¿Quiénes forman la comunidad escolar?", "Estudiantes, profesores, familias y funcionarios", "Todos participan en la vida del colegio."),
    ],
    A=[
        arith("Un curso de 36 estudiantes forma 4 equipos de turnos del diario mural, todos iguales. ¿Cuántos estudiantes tiene cada equipo?", "36//4", "Se reparten los estudiantes en partes iguales."),
        ex("Un plan tiene objetivo, tareas, fecha y materiales, pero no dice quién hace cada tarea. ¿Qué paso falta?", "Responsables", "Falta decir quién hace cada tarea."),
        ex("Sam propone que cada equipo limpie un día de la semana. ¿Qué organiza: turnos de responsabilidad o una votación?", "Turnos de responsabilidad", "Reparte la tarea entre equipos."),
    ],
    Z=[
        ex("¿Por qué es mejor evaluar una actividad al final?", "Para saber si se logró y qué mejorar", "Sin evaluación no se aprende de la experiencia."),
        ex("Un curso quiere hacer una campaña, pero nadie sabe quién hace qué. ¿Qué problema habrá?", "Que cada uno piense que lo hará otro", "Sin responsables, no se cumple."),
    ],
    D=[
        arith("Una campaña dura 4 semanas y cada semana trabajan 6 estudiantes distintos. ¿Cuántos estudiantes participan en total?", "4*6", "Son 6 por semana durante 4 semanas."),
        arith("De 30 estudiantes, 22 aceptaron una tarea de la campaña. ¿Cuántos no la aceptaron?", "30-22", "Se restan los que aceptaron al total."),
    ],
    context=[ex("En un curso inventado, los estudiantes proponen la campaña «Sala sin papeles». Definen el objetivo, reparten 5 equipos y fijan una fecha. ¿Qué paso falta para completar el ciclo?", "Evaluar", "Falta revisar si se logró el objetivo.")],
    selfcheck=[ex("En Orientación: ¿participar es asumir responsabilidades?", "Sí", "Es cumplir tu parte."), ex("¿Un objetivo debe poder comprobarse?", "Sí", "Así se sabe si se logró."), ex("¿Se evalúa al final de una actividad?", "Sí", "Para mejorar la próxima vez.")],
    task=T("Planifica una actividad corta del curso para mejorar un problema cotidiano de la lista: papeles en el piso, ruido en la sala, materiales perdidos. Escribe objetivo, tres tareas, responsables (usa «Equipo 1», «Equipo 2», «Equipo 3»), una fecha y cómo evaluarás.", "Problema: papeles en el piso. Objetivo: que no haya papeles al final de cada recreo. Tareas: poner un tarro, recoger, revisar. Responsables: Equipo 1, 2 y 3. Fecha: lunes a viernes. Evaluación: contar papeles el viernes.", ["objetivo claro", "tres tareas con responsables", "fecha", "forma de evaluar"], ["plan escrito"], ["objetivo vago", "sin responsables"], "Reconoce el plan y pregunta cómo sabrán si funcionó."),
    reinforce="Escribe un objetivo claro para una campaña del curso.",
    extend="Explica por qué una actividad sin evaluación no mejora.",
)

lesson(
    OA8, 2,
    "Una hoja y un lápiz. Los resultados de la votación y los casos están escritos en los ejercicios.",
    "Aprenderé cómo funcionan las elecciones de curso, cómo se cuentan los votos y cómo aceptar los resultados con respeto. Sirve para participar de forma democrática.",
    ["Sé que participar es asumir responsabilidades.", "Sé separar hecho, emoción y límite."],
    [
        "En una elección de curso, los estudiantes eligen a su directiva, que es el grupo que representa al curso. Para que sea democrática, todos pueden votar y ser candidatos, el voto es secreto (nadie dice por quién votó) y se cuentan los votos frente al curso. Gana quien tiene más votos; en este cuaderno a eso le llamamos mayoría simple. Todos deben aceptar el resultado.",
        "Si pierdes, es normal sentir desilusión. Distingue tres cosas. El hecho: tu candidato no ganó. La emoción: sientes tristeza o rabia. Y la conducta: aceptas el resultado, felicitas a quien ganó y sigues colaborando. Si ganas, también hay responsabilidad: representar a todos, no solo a quienes te votaron.",
        "Un límite importante es no discriminar. Nadie puede quedar fuera de ser candidato o votar por su género, origen, religión o forma de ser. Tampoco se puede presionar a otros para votar por alguien ni burlarse de quienes pierden. Si hay una duda sobre el conteo, se pide revisar con respeto, delante del profesor.",
    ],
    [("directiva", "grupo de estudiantes elegido para representar al curso"), ("voto secreto", "voto en que nadie dice por quién votó"), ("mayoría simple", "gana quien tiene más votos"), ("candidato", "persona que se propone para ser elegida"), ("representar", "hablar y actuar en nombre del grupo")],
    [
        W("Contar votos", "Se cuentan los votos: Ana 12, Beto 9 y Cata 7. ¿Quién gana por mayoría simple y cuántos votos hay en total?", ["Se suman los votos: 12 + 9 + 7.", "Gana quien tiene más votos.", "Ana tiene 12."], "Gana Ana; hay 28 votos"),
        W("Aceptar el resultado", "Beto perdió. ¿Cuál conducta acepta el resultado: «Felicito a Ana y sigo colaborando» o «La elección fue injusta, no ayudaré»?", ["Aceptar es respetar la decisión.", "La primera felicita y colabora.", "La segunda rechaza el resultado sin prueba."], "«Felicito a Ana y sigo colaborando»"),
    ],
    [
        M("Pensar que debo decir por quién voté si mi amigo me lo pregunta.", "Se cree que hay que decir por quién se votó.", "El voto es secreto; puedes decir «prefiero no contarlo»."),
        M("Creer que si pierdo, la elección no vale.", "Se mide por si ganó mi candidato.", "Una elección vale por sus reglas, no por quién gana."),
    ],
    R=[
        ex("¿La directiva representa al curso?", "Sí", "Habla y actúa en nombre de todos."),
        ex("En una votación secreta, ¿hay que decir por quién votaste?", "No", "El voto es secreto."),
        ex("Mayoría simple, ¿significa que gana quien tiene más votos?", "Sí", "Se cuenta cuántos votos tiene cada uno."),
    ],
    U=[
        ex("¿Por qué el voto debe ser secreto?", "Para votar libremente sin presión", "Nadie debe sentirse obligado."),
        ex("¿Por qué quien gana debe representar a todos?", "Porque la directiva es de todo el curso", "No solo de quienes lo votaron."),
        ex("Si pierdes, ¿qué conducta respeta el resultado?", "Aceptar, felicitar y seguir colaborando", "Así se respeta la decisión del curso."),
    ],
    A=[
        arith("En otra elección, Luz tuvo 15 votos, Pía 10 y Noa 7. ¿Cuántos votos se contaron en total?", "15+10+7", "Se suman los votos de las tres candidatas."),
        ex("Votos: Luz 15, Pía 10, Noa 7. ¿Quién gana por mayoría simple?", "Luz", "Tiene más votos que las otras."),
        arith("Luz tuvo 15 votos y Pía 10. ¿Cuántos votos más tuvo Luz?", "15-10", "Se resta la menor a la mayor."),
    ],
    Z=[
        ex("Alguien presiona a otro: «Vota por mí o no te hablo». ¿Es una elección democrática?", "No", "Hay presión; el voto debe ser libre."),
        ex("¿Por qué no se puede impedir que alguien sea candidato por ser niña o niño?", "Porque eso es discriminar", "Todos tienen el mismo derecho."),
    ],
    D=[
        arith("Un curso de 30 estudiantes vota. 28 votaron y el resto se ausentó. ¿Cuántos no votaron?", "30-28", "Se resta los que votaron al total."),
        arith("Tres candidatos reciben 9, 8 y 6 votos. ¿Cuántos votos más tiene el primero que el tercero?", "9-6", "Se resta el menor al mayor."),
    ],
    context=[ex("Tras una elección, Beto dice: «Perdí, me da pena, pero felicito a Ana». ¿Distinguió hecho, emoción y conducta?", "Sí", "Dijo el hecho (perdió), la emoción (pena) y la conducta (felicitar).")],
    selfcheck=[ex("En Orientación: ¿el voto es secreto?", "Sí", "Para votar con libertad."), ex("¿Se acepta el resultado aunque pierda mi candidato?", "Sí", "Respeta la decisión."), ex("¿Se puede discriminar a un candidato?", "No", "Todos tienen derecho.")],
    task=T("Simula en papel una elección de curso con tres candidatos inventados: Ana, Beto y Cata. Escribe una lista de 20 votos usando solo las letras A, B y C (por ejemplo, A A B C…), de modo que no haya empate en el primer lugar. Cuenta los votos, indica quién gana por mayoría simple y escribe qué haría quien pierde.", "Voto: A=9, B=6, C=5 (suman 20). Gana A. Quien pierde felicita y sigue colaborando.", ["lista de 20 votos", "recuento correcto", "gana quien tiene más votos", "conducta de aceptación"], ["tabla o conteo escrito"], ["errores de conteo", "no aceptar"], "Reconoce el conteo y pregunta cómo se sentiría un perdedor."),
    reinforce="Cuenta votos de una lista inventada y di quién gana.",
    extend="Escribe tres reglas para una elección justa en el curso.",
)

lesson(
    OA8, 3,
    "Una hoja y un lápiz. Los casos de roles y de decisiones están escritos en los ejercicios.",
    "Aprenderé a comparar formas de tomar decisiones y de repartir roles sin discriminar. Sirve para decidir de manera justa en el curso.",
    ["Sé cómo funcionan las elecciones.", "Sé qué es discriminar."],
    [
        "Un curso puede tomar decisiones de varias maneras. Puede votar, que es contar opiniones. Puede buscar consenso, que es llegar a un acuerdo que todos pueden aceptar. Puede sortear si todos están de acuerdo. O una sola persona puede imponer una decisión. Cada forma tiene consecuencias. Votar es rápido y justo si todos participan. El consenso toma más tiempo, pero deja más conformes. Imponer rápido molesta a quienes no fueron escuchados.",
        "Al repartir roles y responsabilidades, el curso no debe discriminar. Por ejemplo, no se puede decir «los niños llevan las mesas y las niñas limpian». Cada rol debe poder hacerlo cualquier persona que quiera y pueda. Una buena manera es rotar los roles, para que todos prueben distintas tareas. También se toma en cuenta lo que cada persona puede hacer con seguridad, sin excluirla.",
        "Para elegir cómo decidir, hazte tres preguntas: ¿todos fueron escuchados?, ¿es justa?, ¿se puede cumplir? La mejor opción es la que cumple las tres.",
    ],
    [("consenso", "acuerdo que todos pueden aceptar"), ("rotar", "cambiar los roles para que todos prueben"), ("imponer", "decidir sin escuchar a los demás"), ("rol", "tarea o función que cumple alguien en el grupo"), ("excluir", "dejar a alguien fuera")],
    [
        W("Elegir cómo decidir", "El curso debe elegir el color del cartel. 30 estudiantes tienen opiniones distintas. ¿Qué forma es más justa: votar o que decida solo uno?", ["Votar escucha a todos.", "Que decida uno no considera a los demás.", "La votación es más justa."], "Votar"),
        W("Roles sin discriminar", "Un grupo dice «las niñas ordenan y los niños cargan». ¿Es discriminación?", ["Divide por género.", "Impide que alguien elija su rol.", "Sí, es discriminación."], "Sí, es discriminación"),
    ],
    [
        M("Pensar que lo mejor siempre es lo más rápido.", "Se confunde rapidez con justicia.", "Elige la forma que escuche a todos y se pueda cumplir."),
        M("Repartir roles según lo que «suele hacer» cada género.", "Se sigue una costumbre.", "Cada rol puede hacerlo quien quiera y pueda."),
    ],
    R=[
        ex("Rotar los roles, ¿es cambiarlos para que todos prueben?", "Sí", "Así nadie se queda siempre con el mismo."),
        ex("Imponer una decisión, ¿escucha a todos?", "No", "Una persona decide sin escuchar."),
        ex("Un consenso, ¿es un acuerdo que todos pueden aceptar?", "Sí", "Todos están de acuerdo."),
    ],
    U=[
        ex("¿Por qué el consenso toma más tiempo?", "Porque hay que escuchar y negociar con todos", "Se busca un acuerdo para todos."),
        ex("¿Por qué rotar los roles evita discriminar?", "Porque todos pueden probar todas las tareas", "No se asigna por género."),
        ex("¿Qué tres preguntas ayudan a elegir cómo decidir?", "Si todos fueron escuchados, si es justa y si se puede cumplir", "Así se elige la forma más adecuada."),
    ],
    A=[
        ex("Formas de decidir: 1) votar, 2) consenso, 3) imponer, 4) sorteo con acuerdo de todos. ¿Cuántas escuchan a todos?", "3", "Votar, consenso y sorteo acordado incluyen a todos."),
        ex("Roles: 1) ordenar libros, 2) cargar sillas, 3) revisar la fecha del calendario. ¿Cuál debe asignarse solo a niñas?", "Ninguno", "Cualquier persona puede hacerlos."),
        ex("Un curso rota 4 roles entre 4 grupos, un rol nuevo por grupo cada semana. ¿Cuántas semanas pasan hasta que cada grupo haya hecho los 4 roles?", "4 semanas", "Cada semana cada grupo prueba un rol distinto, así que 4 roles toman 4 semanas."),
    ],
    Z=[
        ex("Si siempre decide la misma persona, ¿qué problema aparece?", "Los demás no se sienten escuchados", "No hay participación de todos."),
        ex("¿Por qué una decisión justa no siempre es la más popular?", "Porque debe respetar a todos y los derechos", "La mayoría no puede excluir a nadie."),
    ],
    D=[
        arith("En una votación, 18 estudiantes prefieren una opción y 12 otra. ¿Cuántos votaron?", "18+12", "Se suman los dos grupos."),
        arith("Un curso de 24 estudiantes forma 4 grupos iguales para rotar roles. ¿Cuántos estudiantes tiene cada grupo?", "24//4", "Se reparten en partes iguales."),
    ],
    context=[ex("Un curso inventado decide cómo organizar los turnos del diario mural. Acuerdan rotar entre todos cada semana. ¿Aplicaron una forma justa de repartir roles?", "Sí", "Rotar incluye a todos y evita discriminar.")],
    selfcheck=[ex("En Orientación: ¿rotar roles ayuda a no discriminar?", "Sí", "Todos prueban distintas tareas."), ex("¿Imponer escucha a todos?", "No", "Decide uno solo."), ex("¿Votar es una forma democrática?", "Sí", "Se cuentan las opiniones de todos.")],
    task=T("Un curso debe repartir seis roles para una exposición: presentar, cuidar el tiempo, escribir, dibujar, ordenar el material y despedir. Hay seis integrantes: A, B, C, D, E y F. Escribe: cómo repartirías los roles sin discriminar, cómo decidirían quién hace cada uno (votar, sortear o consenso) y cómo rotarían en la próxima exposición.", "Sorteo con acuerdo de todos para repartir. Resultado: A presenta, B tiempo, C escribe, D dibuja, E ordena, F despide. En la próxima rotamos: todos se mueven un rol.", ["reparte los seis roles", "elige un método justo", "plan de rotación", "no usa género para asignar"], ["texto escrito", "tabla"], ["asignar por género", "decide una sola persona"], "Reconoce el método y pregunta si todos estuvieron de acuerdo."),
    reinforce="Escribe una forma justa de elegir quién lleva cada cosa a una excursión.",
    extend="Explica por qué la votación no puede quitar derechos a una minoría.",
)

lesson(
    OA8, 4,
    "Una hoja y un lápiz. Los acuerdos del curso y los registros están escritos en los ejercicios.",
    "Aprenderé a asumir y cumplir responsabilidades y a establecer acuerdos de curso por diálogo. Sirve para que el curso funcione y todos se sientan parte.",
    ["Sé planificar una actividad con objetivo.", "Sé decidir sin discriminar."],
    [
        "Un acuerdo de curso es una regla que el curso decide por diálogo y que todos se comprometen a cumplir. Para que sea bueno, debe ser claro (qué), posible (se puede cumplir) y justo (vale para todos). Se establece escuchando opiniones, buscando consenso o votando, y escribiéndolo para recordarlo. Por ejemplo: «Cada persona recoge sus papeles antes de salir al recreo».",
        "Cumplir una responsabilidad significa hacer lo que prometiste en el plazo acordado. Si no puedes cumplirla, avisas con anticipación y propones una solución: «No alcanzo a llevar los materiales hoy; ¿puedo hacerlo mañana o alguien me ayuda?». Incumplir en silencio perjudica al grupo.",
        "Los acuerdos deben respetar los derechos de todos: no pueden excluir ni humillar a nadie. Si un acuerdo no funciona o es injusto, se puede proponer cambiarlo en una reunión de curso, con respeto.",
    ],
    [("acuerdo de curso", "regla que el curso decide por diálogo y todos cumplen"), ("cumplir", "hacer lo prometido en el plazo"), ("avisar", "decir con anticipación que algo no se podrá hacer"), ("justo", "que vale igual para todos"), ("reunión de curso", "momento en que el curso conversa y decide")],
    [
        W("Un acuerdo bueno", "¿Qué acuerdo es mejor: «Cada persona recoge sus papeles antes de salir al recreo» o «Hay que portarse bien»?", ["El primero es claro y posible.", "El segundo es vago.", "Un acuerdo debe poder comprobarse."], "«Cada persona recoge sus papeles antes de salir al recreo»"),
        W("Avisar a tiempo", "Noa no podrá llevar los materiales mañana. ¿Qué hace: avisa hoy y propone una solución, o no dice nada?", ["Avisar da tiempo al grupo.", "Proponer solución ayuda.", "El silencio perjudica."], "Avisa hoy y propone una solución"),
    ],
    [
        M("Pensar que un acuerdo vale solo para los demás.", "Se cree que uno puede quedar fuera.", "Un acuerdo de curso vale para todos, también para ti."),
        M("No decir nada si no puedo cumplir.", "Se espera que nadie se dé cuenta.", "Avisa con anticipación y propone una solución."),
    ],
    R=[
        ex("Un acuerdo de curso, ¿vale para todos?", "Sí", "Se compromete todo el curso."),
        ex("Si no puedes cumplir una responsabilidad, ¿avisas con anticipación o no dices nada?", "Avisas con anticipación", "Así el grupo puede ajustar."),
        ex("Un acuerdo claro, ¿se puede comprobar?", "Sí", "Dice qué hacer."),
    ],
    U=[
        ex("¿Por qué «hay que portarse bien» es un acuerdo débil?", "Porque no dice qué hacer", "No se puede comprobar."),
        ex("¿Cuáles son tres cualidades de un buen acuerdo?", "Claro, posible y justo", "Así se puede cumplir y vale para todos."),
        ex("¿Qué se hace si un acuerdo es injusto?", "Proponer cambiarlo en una reunión con respeto", "Los acuerdos se pueden mejorar."),
    ],
    A=[
        ex("Acuerdos: 1) recoger los papeles antes del recreo, 2) portarse bien, 3) levantar la mano para hablar, 4) ser bueno. ¿Cuántos son claros?", "2", "El 1 y el 3 dicen qué hacer; los otros son vagos."),
        ex("Un registro semanal muestra que de 5 días, el curso cumplió el acuerdo de los papeles 3 días. ¿Cuántos días no lo cumplió?", "2", "5 − 3 = 2.", calc="5-3"),
        ex("Un niño dice: «Mi tarea es traer el pizarrón. Hoy no puedo; ¿alguien me ayuda mañana?». ¿Qué hizo bien: avisar a tiempo o ignorar?", "Avisar a tiempo", "Permite que el grupo se ajuste."),
    ],
    Z=[
        ex("Si el curso acuerda una regla que deja fuera a una compañera, ¿es un buen acuerdo?", "No", "Debe valer para todos y respetar derechos."),
        ex("¿Por qué anotar los acuerdos ayuda?", "Porque se pueden recordar y revisar", "Lo escrito evita olvidos."),
    ],
    D=[
        arith("El curso hizo 4 acuerdos y cumplió 3. ¿Cuántos faltan?", "4-3", "Se resta lo cumplido a los acuerdos."),
        arith("Una semana de cumplimiento: lunes 25 estudiantes cumplieron, martes 27 y miércoles 28. ¿Cuántos cumplimientos individuales se registraron en los tres días?", "25+27+28", "Se suman los tres días."),
    ],
    context=[ex("En una reunión, el curso decide por votación que, antes del recreo, todos guardan sus útiles. Escriben el acuerdo en el diario mural. ¿Qué características de un buen acuerdo cumple?", "Claro, posible y justo", "Dice qué hacer, se puede cumplir y vale para todos.")],
    selfcheck=[ex("En Orientación: ¿un acuerdo de curso se decide por diálogo?", "Sí", "Se escuchan las opiniones."), ex("¿Se avisa si no se puede cumplir?", "Sí", "Se avisa con anticipación."), ex("¿Un acuerdo debe valer para todos?", "Sí", "Ese es el sentido de un acuerdo.")],
    task=T("Escribe tres acuerdos de curso claros, posibles y justos para: el orden de la sala, el uso de los materiales y el trato entre compañeros. Después escribe cómo avisarías si no puedes cumplir una responsabilidad.", "Orden: cada persona recoge sus papeles. Materiales: los devolvemos a su lugar. Trato: escuchamos sin interrumpir. Aviso: «No alcanzo a hacerlo hoy; ¿puedo hacerlo mañana?»", ["tres acuerdos claros", "posibles y justos", "frase para avisar"], ["lista escrita"], ["acuerdos vagos", "no proponer solución"], "Reconoce la claridad y pregunta cómo se revisaría."),
    reinforce="Escribe un acuerdo de curso claro para el trabajo en grupo.",
    extend="Explica por qué un acuerdo debe poder revisarse y mejorarse.",
)

lesson(
    OA8, 5,
    "Una hoja y un lápiz. La tabla de seguimiento y el caso están escritos en los ejercicios.",
    "Aprenderé a evaluar si el curso cumple sus acuerdos, a comunicar un desacuerdo con respeto y a pedir ayuda cuando haga falta. Sirve para mejorar la organización del curso.",
    ["Sé establecer acuerdos de curso.", "Sé decir mi opinión con respeto."],
    [
        "Evaluar el cumplimiento de acuerdos es revisar si el curso hizo lo acordado. Una forma simple es un registro semanal: una tabla donde se marca cada día si se cumplió el acuerdo. Al final se cuenta cuántos días se cumplió y se conversa: ¿qué ayudó?, ¿qué dificultó?, ¿qué ajustamos? Evaluar no es buscar culpables, sino mejorar.",
        "En una reunión de curso puedes decir un desacuerdo con respeto. Usa una frase como: «Yo veo que no hemos cumplido el acuerdo de los papeles. Propongo que nos turnemos para revisar». Habla de hechos, usa un mensaje «yo», escucha las respuestas y propón algo posible.",
        "Si el curso no logra resolver un problema, o hay un acuerdo que se rompe todas las semanas, puedes pedir ayuda al profesor jefe o al encargado de convivencia. Pedir ayuda no es acusar: ayuda a que se cumplan los derechos de todos.",
    ],
    [("evaluar", "revisar si se cumplió lo acordado"), ("registro", "anotación de lo que ocurrió"), ("desacuerdo", "cuando pienso distinto"), ("profesor jefe", "profesor responsable del curso"), ("ajustar", "cambiar algo para que funcione mejor")],
    [
        W("Leer un registro", "Un registro de 5 días muestra que se cumplió el acuerdo 2 días. ¿Cuántos días no se cumplió?", ["Total: 5 días.", "Cumplió: 2.", "No cumplió: 5 menos 2."], "3 días"),
        W("Desacuerdo respetuoso", "¿Qué frase expresa un desacuerdo con respeto: «Yo veo que no cumplimos el acuerdo; propongo turnarnos» o «Ustedes nunca cumplen»?", ["La primera habla de hechos.", "Incluye una propuesta.", "La segunda acusa."], "«Yo veo que no cumplimos el acuerdo; propongo turnarnos»"),
    ],
    [
        M("Evaluar para encontrar a los culpables.", "Se confunde evaluar con castigar.", "Evaluar sirve para mejorar los acuerdos."),
        M("Callarme en la reunión por miedo a opinar distinto.", "Se cree que opinar distinto molesta.", "Opinar con respeto ayuda a mejorar."),
    ],
    R=[
        ex("Un registro semanal, ¿ayuda a evaluar si se cumplió un acuerdo?", "Sí", "Muestra qué días se cumplió."),
        ex("Evaluar, ¿es buscar culpables o mejorar?", "Mejorar", "Busca aprender y ajustar."),
        ex("El profesor jefe, ¿puede ayudar si un acuerdo se rompe siempre?", "Sí", "Es un adulto responsable del curso."),
    ],
    U=[
        ex("¿Por qué conviene hablar de hechos en la evaluación?", "Porque se puede comprobar", "Los hechos evitan acusaciones."),
        ex("¿Qué incluye una frase de desacuerdo respetuoso?", "Un hecho, un mensaje «yo» y una propuesta", "Así se opina sin atacar."),
        ex("¿Por qué pedir ayuda al profesor jefe no es acusar?", "Porque busca que se cumplan los derechos de todos", "Es una forma de cuidar el curso."),
    ],
    A=[
        ex("Registro de 5 días con ✔ y ✘: ✔ ✔ ✘ ✔ ✘. ¿Cuántos días se cumplió?", "3", "Hay tres ✔ en cinco días."),
        ex("Registro: ✔ ✔ ✘ ✔ ✘. ¿Se cumplió el acuerdo en más de la mitad o en menos de la mitad de los días?", "Más de la mitad", "3 de 5 días es más que la mitad."),
        ex("Completa un ajuste: «Si no recogemos los papeles, ponemos un tarro en cada fila». ¿Qué hace esta frase: ajusta el acuerdo o lo elimina?", "Lo ajusta", "Busca una forma de cumplirlo."),
    ],
    Z=[
        ex("¿Por qué no basta con crear un acuerdo y olvidarlo?", "Porque hay que revisar si se cumple", "Sin revisión, se pierde."),
        ex("Si un acuerdo nunca se cumple, ¿qué puede significar?", "Que quizá es difícil de cumplir y hay que ajustarlo", "A veces hay que cambiar el acuerdo."),
    ],
    D=[
        arith("En 4 semanas se cumplió el acuerdo 3, 4, 5 y 5 días. ¿Cuántos días se cumplió en total?", "3+4+5+5", "Se suman los días de cada semana."),
        arith("En un mes de 20 días de clase se cumplió el acuerdo 16 días. ¿Cuántos días no se cumplió?", "20-16", "Se restan los días cumplidos al total."),
    ],
    context=[ex("En una reunión, una estudiante inventada dice: «Veo que de 5 días solo cumplimos 2. Propongo que cada fila revise sus papeles». ¿Qué hizo?", "Evaluó con hechos y propuso", "Usó datos y una propuesta respetuosa.")],
    selfcheck=[ex("En Orientación: ¿evaluar sirve para mejorar?", "Sí", "No para culpar."), ex("¿Se puede opinar distinto con respeto?", "Sí", "Con hechos y propuestas."), ex("¿Se puede pedir ayuda al profesor jefe?", "Sí", "Si el problema no se resuelve.")],
    task=T("Lee el registro: lunes ✔, martes ✘, miércoles ✘, jueves ✔, viernes ✘ (acuerdo: «recoger los papeles antes del recreo»). Escribe: cuántos días se cumplió y cuántos no; una frase de desacuerdo respetuoso para la reunión; un ajuste posible; y cuándo pedirías ayuda al profesor jefe.", "Se cumplió 2 días; no 3. Frase: «Veo que cumplimos solo 2 de 5 días; propongo poner un tarro en cada fila». Ajuste: tarros. Pediría ayuda si el problema sigue 2 semanas.", ["cuenta bien los días", "frase respetuosa", "ajuste posible", "cuándo pedir ayuda"], ["texto escrito"], ["culpar a personas", "no proponer nada"], "Reconoce la evaluación y pregunta cómo revisarían de nuevo."),
    reinforce="Haz un registro de 5 días para un acuerdo inventado y cuéntalo.",
    extend="Escribe cómo dirías un desacuerdo con respeto en una reunión.",
)
