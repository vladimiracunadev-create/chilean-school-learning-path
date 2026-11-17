"""Atención de Párvulos TP 3.º y 4.º medio: OAE-09 (atender a niños y niñas menores de seis años en las horas de descanso y recreación, con alternativas de uso del tiempo libre) y OAE-10 (registrar, archivar y mantener actualizados los antecedentes de niños, niñas y familias, de forma manual y digital). Todo en papel: jardines, niños, niñas y familias inventados y rotulados «de ejemplo»."""
from __future__ import annotations

from tp_atpa_common import LIM, build

O9 = "TP-ATPA-3y4-OAE-09"
O10 = "TP-ATPA-3y4-OAE-10"

# ============================================================ OAE-09, clase 1
F = ("Ficha 1 (jornada de ejemplo, nivel medio, 16 niños y niñas). Almuerzo hasta las 12:45; descanso (siesta o reposo tranquilo) de 13:00 a 14:30; juego en el patio de 15:00 a 15:45. "
     "Reglas de ejemplo: en el patio los adultos se ubican para ver a todos los niños en todo momento; en el descanso hay siempre un adulto en la sala, con luz tenue; los niños que no duermen hacen reposo tranquilo con un libro blando o un objeto suave. La cantidad de adultos por niños la fija la norma vigente.")
build(
    O9, 1, F,
    use="Aprenderé qué son el descanso y la recreación de niños y niñas menores de seis años, por qué cada uno necesita algo distinto y cómo se cuida su seguridad.",
    prior=["Conozco el rol de la técnica y de la educadora.", "Sé leer horarios.", "Sé que la supervisión es constante."],
    explain=[
        "En Atención de Párvulos, el descanso es el tiempo para reponer energías, ya sea durmiendo una siesta o en reposo tranquilo. La recreación es el tiempo de juego libre para disfrutar, moverse y relacionarse. Ambos son parte del aprendizaje y del bienestar. No todos los niños necesitan lo mismo: unos duermen, otros solo descansan y otros se despiertan antes. Se respeta la necesidad de cada uno.",
        "Para propiciar el descanso se prepara un ambiente tranquilo, con luz tenue, poco ruido y, si el niño lo tiene, su objeto querido. Para el tiempo libre se ofrecen alternativas: juegos tranquilos con libros blandos, construcción con bloques grandes y juegos en el patio. En ambos momentos un adulto observa a todos los niños todo el tiempo.",
        "La cantidad de adultos por niños la fija la norma vigente. En el patio, los adultos se ubican para ver todo el espacio y revisan que no haya objetos peligrosos antes de salir." + LIM,
    ],
    vocab=[("descanso", "tiempo para reponer energías, durmiendo o en reposo tranquilo"), ("recreación", "tiempo de juego libre para disfrutar y moverse"), ("reposo tranquilo", "descanso sin dormir, con un libro o un objeto suave"), ("luz tenue", "luz suave y baja"), ("objeto querido", "objeto de la casa que acompaña al niño"), ("tiempo libre", "momento sin actividad dirigida, con juego elegido por el niño")],
    worked=[
        ("Duración del descanso", "En otra sala de ejemplo el descanso va de 13:15 a 14:45. ¿Cuántos minutos dura?", ["De 13:15 a 14:45 hay 1 hora y 30 minutos.", "Son 90 minutos."], "90 minutos"),
        ("Qué ofrecer a quien no duerme", "Un niño de ejemplo no se duerme en la siesta. ¿Qué se ofrece?", ["Se respeta su necesidad.", "Reposo tranquilo con un libro blando."], "Reposo tranquilo con un libro blando"),
    ],
    mistakes=[("Obligar a dormir a un niño que no tiene sueño.", "Genera angustia y no logra descanso.", "Ofrece reposo tranquilo con un libro blando u objeto suave."),
              ("Ubicarse en un rincón del patio de espaldas al resto.", "Hay niños sin supervisión visual.", "Ubícate para ver a todos los niños.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué es la recreación?", "El tiempo de juego libre para disfrutar y moverse", "El tiempo de siesta", "El tiempo de comida", "La recreación es el tiempo de juego libre."),
        ("abc", "{F} ¿Qué hacen los niños que no duermen?", "Reposo tranquilo con un libro blando o un objeto suave", "Salir al patio solos", "Jugar con pelotas dentro de la sala", "La ficha dice que hacen reposo tranquilo."),
        ("abc", "{F} ¿Cómo debe ser la luz en el descanso?", "Tenue", "Muy fuerte", "Apagada del todo, sin adulto", "Una luz suave ayuda a descansar y permite ver a los niños."),
        ("=", "{F} ¿Cuántos minutos dura el descanso, de 13:00 a 14:30?", "(14*60+30)-(13*60)", "Se restan las horas, convertidas a minutos.", " minutos"),
        ("abc", "{F} ¿Dónde debe estar siempre un adulto durante el descanso?", "En la sala, con los niños", "En la oficina", "En el patio", "La regla dice que hay siempre un adulto en la sala."),
        ("abc", "{F} ¿Cómo se ubican los adultos en el patio?", "De modo que vean a todos los niños en todo momento", "Todos juntos en un rincón", "Sentados dentro de la sala", "La supervisión visual constante es la regla del patio."),
        ("=", "{F} ¿Cuántos minutos dura el juego en el patio, de 15:00 a 15:45?", "(15*60+45)-(15*60)", "Se restan las horas, convertidas a minutos.", " minutos"),
        ("=", "{F} Si de los 16 niños duermen 11, ¿cuántos hacen reposo tranquilo?", "16-11", "Al total de niños se le restan los que duermen.", " niños"),
        ("abc", "{F} Un niño tiene un peluche que lo tranquiliza para dormir. ¿Qué hace la técnica?", "Lo deja tenerlo, si el protocolo lo permite, y consulta a la educadora si hay dudas", "Se lo quita para que aprenda a dormir", "Le dice que es muy grande para eso", "Su objeto querido le da seguridad."),
        ("abc", "{F} Antes de salir al patio, la técnica ve un palo grande en el suelo. ¿Qué hace?", "Lo retira y avisa a la educadora", "Lo deja porque los niños lo verán", "Pide a un niño que lo mueva", "Se revisa el patio antes de salir."),
        ("abc", "{F} Un niño se despierta llorando a la mitad del descanso. ¿Qué hace la técnica?", "Se acerca con calma, lo acompaña en voz baja y avisa a la educadora si no se calma", "Lo levanta y lo lleva al patio solo", "Lo deja llorar hasta que pase", "Se lo acompaña sin despertar a los demás."),
        ("=", "{F} Si los niños pasan 30 minutos en el patio, de los 45 minutos, y el resto en filas para entrar, ¿cuántos minutos son de filas?", "45-30", "Al tiempo total se le resta el tiempo de juego.", " minutos"),
        ("abc", "{F} Una técnica quiere salir al patio solo con 10 de los 16 niños para «dividir». ¿Qué observación corresponde?", "Hay que consultar a la educadora, porque los otros niños necesitan supervisión y la cantidad de adultos la fija la norma vigente", "Está bien: así es más fácil", "Está bien si los demás duermen", "Todos los niños necesitan supervisión constante."),
    ],
    ctx=("abc", "{F} A las 13:30 la técnica nota que dos niños conversan en voz alta y despiertan a otros. ¿Qué hace?", "Se acerca, les habla en voz baja y les ofrece un libro blando para su reposo", "Les grita desde la puerta", "Los saca de la sala sin avisar", "Se interviene con calma y se ofrece una alternativa."),
    sc=[
        ("En Atención de Párvulos: ¿qué hacen los niños que no duermen en el descanso?", "Reposo tranquilo", "Se respeta su necesidad sin forzar."),
        ("¿Cómo se ubican los adultos en el patio?", "De modo que vean a todos los niños", "La supervisión es constante, porque los niños pequeños no se dejan solos."),
        ("¿Quién fija la cantidad de adultos por niños?", "La norma vigente", "Los números del cuaderno son de ejemplo."),
    ],
    op=("Jornada de ejemplo: nivel de transición con 20 niños y niñas; descanso de 13:00 a 14:15, patio de 15:00 a 15:40. Después del almuerzo, 13 niños duermen y los demás no. Una niña, Sofía, siempre duerme con un osito. "
        "Escribe: cuántos minutos dura el descanso; cuántos niños hacen reposo tranquilo; qué ofrecerías a quienes no duermen; y cómo organizar la vigilancia en el patio.",
        "El descanso dura 75 minutos. Hacen reposo tranquilo 20 − 13 = 7 niños. Les ofrecería libros blandos y objetos suaves, en un rincón tranquilo. A Sofía le dejaría su osito si el protocolo lo permite. En el patio: los adultos se ubican para ver a todos los niños en todo momento y se revisa el patio antes de salir.",
        ["calcula minutos y niños", "ofrece alternativas de reposo", "organiza la supervisión"],
        ["hoja con dos cálculos y dos propuestas"],
        ["forzar a dormir", "no calcular bien", "dejar niños sin supervisión"],
        "Pregunta: «¿qué harías si un niño que no duerme molesta a los demás?». Debe acercarse con calma y ofrecerle una alternativa."),
    reinforce="Escribe tres alternativas para los niños que no duermen en el descanso.",
    extend="Explica por qué obligar a dormir a un niño no logra que descanse.",
)

# ============================================================ OAE-09, clase 2
F = ("Ficha 2 (tipos de juego, de ejemplo). Juego libre: el niño elige a qué y cómo jugar. Juego dirigido: el adulto propone y guía. Juego simbólico: hacer «como si» (cocinar, ser doctora). Juego de construcción: armar con bloques. "
     "Juego de reglas: seguir reglas simples, como esperar el turno. Juego motor: correr, saltar o trepar con supervisión. Los rincones de la sala son zonas con material para un tipo de juego.")
build(
    O9, 2, F,
    use="Aprenderé los tipos de juego y los rincones, y a ofrecer alternativas de uso del tiempo libre según la necesidad de cada niño o niña.",
    prior=["Conozco el descanso y la recreación.", "Sé que cada niño tiene su ritmo.", "Sé leer una ficha."],
    explain=[
        "El juego es la forma en que los niños aprenden. Hay distintos tipos: el juego libre, donde el niño elige; el dirigido, donde el adulto propone; el simbólico, donde se hace «como si»; el de construcción, con bloques; el de reglas, con reglas simples como esperar el turno; y el motor, de movimiento. Un mismo juego puede combinar varios tipos.",
        "Los rincones de la sala son zonas con material para un tipo de juego, como el rincón de construcción, el de lectura o el de juego simbólico. En el tiempo libre se ofrecen varios rincones a la vez, para que cada niño elija según su necesidad. Los materiales deben ser seguros y estar a la altura de los niños. El adulto observa, acompaña y, si hace falta, propone, sin imponer.",
        "No hay juegos «de niñas» ni «de niños»: todos pueden elegir cualquier rincón. Tampoco se compara a los niños por cómo juegan." + LIM,
    ],
    vocab=[("juego libre", "el niño elige a qué y cómo jugar"), ("juego dirigido", "el adulto propone y guía"), ("juego simbólico", "hacer «como si», como cocinar o ser doctora"), ("juego de construcción", "armar cosas con bloques"), ("juego de reglas", "juego con reglas simples, como esperar el turno"), ("rincón", "zona de la sala con material para un tipo de juego")],
    worked=[
        ("Clasificar un juego", "Dos niños de ejemplo juegan a que cocinan una sopa con cucharas y ollas de plástico. ¿Qué tipo de juego es?", ["Hacen «como si» cocinaran.", "Es juego simbólico."], "Juego simbólico"),
        ("Repartir en rincones", "En una sala de ejemplo hay 12 niños y 3 rincones iguales. ¿Cuántos niños caben por rincón?", ["Se divide el total entre los rincones.", "12 ÷ 3 = 4."], "4 niños"),
    ],
    mistakes=[("Decirle a un niño «el rincón de cocinar es de niñas».", "Es un estereotipo y le limita su elección.", "Invita a todos a elegir cualquier rincón."),
              ("Obligar a un niño a cambiar de rincón porque «juega siempre a lo mismo».", "Lo obliga a abandonar su elección sin motivo.", "Propón una alternativa y respeta su elección.")],
    T=[
        ("abc", "{F} ¿Qué tipo de juego es armar una torre con bloques?", "De construcción", "Simbólico", "De reglas", "Armar con bloques es juego de construcción."),
        ("abc", "{F} ¿Qué tipo de juego es hacer «como si» fuera un doctor?", "Simbólico", "Motor", "De construcción", "Hacer «como si» es juego simbólico."),
        ("abc", "{F} ¿Qué tipo de juego es esperar el turno para tirar una pelota blanda?", "De reglas", "Libre sin reglas", "Simbólico", "Esperar el turno es una regla simple."),
        ("abc", "{F} Un niño elige a qué jugar y cómo hacerlo. ¿Qué tipo de juego es?", "Libre", "Dirigido", "De reglas", "En el juego libre el niño decide."),
        ("abc", "{F} Una técnica propone: «hoy vamos a imitar a los animales y yo voy diciendo qué hacer». ¿Qué tipo de juego es?", "Dirigido", "Libre", "De construcción", "El adulto propone y guía, por eso es dirigido."),
        ("=", "{F} Hay 18 niños y 3 rincones con cupo igual. ¿Cuántos niños caben en cada rincón?", "18//3", "Se divide el total entre los rincones.", " niños"),
        ("abc", "{F} Un niño quiere cocinar en el rincón simbólico y alguien le dice que «eso es de niñas». ¿Qué hace la técnica?", "Aclara que todos pueden elegir cualquier rincón e invita al niño a jugar", "Le dice que cambie de rincón", "No dice nada y lo deja ir", "No hay juegos de niñas o niños; todos pueden elegir."),
        ("abc", "{F} ¿Dónde se ubica el material de uso diario en cada rincón?", "A la altura de los niños", "En un estante alto", "En la oficina", "Así los niños pueden elegir y guardar solos."),
        ("=", "{F} Si cada rincón recibe 4 niños y hay 5 rincones, ¿cuántos niños caben en total?", "4*5", "Se multiplican los niños por rincón por los rincones.", " niños"),
        ("abc", "{F} Un niño juega siempre solo con los mismos bloques. ¿Qué hace la técnica?", "Lo observa, le ofrece sumarse con otros si él quiere y respeta su ritmo", "Lo obliga a jugar con otros", "Le quita los bloques", "Se ofrece una alternativa sin imponer."),
        ("abc", "{F} Una niña usa una silla como «bus» y reparte tarjetas como «boletos». ¿Qué tipo de juego predomina?", "Simbólico", "De reglas", "Motor", "Hacer como si la silla fuera un bus es simbólico."),
        ("=", "{F} Entre los 18 niños, 6 eligen construcción, 7 el rincón simbólico y el resto lectura. ¿Cuántos niños eligen lectura?", "18-6-7", "Al total se le restan los que eligen los otros rincones.", " niños"),
        ("abc", "{F} Dos niños discuten por un juguete en el rincón de construcción. ¿Qué hace la técnica?", "Se acerca, escucha a ambos y les ayuda a acordar un turno", "Quita el juguete a los dos", "Elige al más grande", "Se ayuda con calma a resolver y se aplica la regla de esperar turno."),
    ],
    ctx=("abc", "{F} Un niño con baja visión no puede ver bien el rincón de construcción. ¿Qué hace la técnica?", "Consulta a la educadora y ajusta el espacio y el material para que pueda participar", "Le dice que mejor juegue en otra parte", "Lo deja mirar desde lejos", "Se adapta el espacio para que participe, con la guía de la educadora."),
    sc=[
        ("En Atención de Párvulos: ¿qué es el juego libre?", "El juego donde el niño elige a qué y cómo jugar", "El niño decide y el adulto observa."),
        ("¿Hay juegos de niñas y juegos de niños?", "No", "Todos pueden elegir cualquier juego, sin importar si son niñas o niños."),
        ("¿Qué es un rincón?", "Una zona con material para un tipo de juego", "Cada rincón ofrece una alternativa distinta de juego para elegir."),
    ],
    op=("Sala de ejemplo de nivel medio con 15 niños y niñas. Rincones: construcción (bloques grandes), lectura (libros blandos), simbólico (ollas y cucharas de plástico) y motor (colchonetas bajas para rodar). "
        "Escribe: cuántos niños caben por rincón si se reparten por igual en los 3 primeros rincones; qué tipo de juego predomina en los rincones de construcción, simbólico y motor; cómo invitarías a un niño que prefiere mirar; y qué harías si dicen que cocinar «es de niñas».",
        "En 3 rincones caben 15 ÷ 3 = 5 niños por rincón. Construcción: juego de construcción; simbólico: juego simbólico; motor: juego motor. Al niño que mira: «Cuando quieras, puedes sumarte aquí». Si dicen que cocinar es de niñas: «Todos podemos cocinar y jugar donde queramos».",
        ["calcula la cantidad por rincón", "nombra el tipo de juego", "respeta el ritmo y evita estereotipos"],
        ["hoja con un cálculo y tres respuestas breves"],
        ["asignar juegos por género", "obligar a jugar", "confundir los tipos de juego"],
        "Pregunta: «¿qué harías si hay más niños que cupo?». Debe proponer turnos o rotación."),
    reinforce="Escribe un ejemplo de cada tipo de juego de la ficha.",
    extend="Explica por qué ofrecer varios rincones al mismo tiempo respeta las necesidades de cada niño.",
)

# ============================================================ OAE-09, clase 3
F = ("Ficha 3 (caso de ejemplo, nivel medio, 16 niños y niñas). Después del almuerzo, 11 niños se duermen y 5 no. Rincón tranquilo con libros blandos y cojines. Emilia usa silla de ruedas y quiere jugar en el patio; el patio tiene un sector de arena y otro con rampa y pasto. "
     "Mateo se despierta llorando a las 14:00. Hay una educadora y una técnica; la norma vigente fija cuántos adultos corresponden.")
build(
    O9, 3, F,
    use="Aprenderé a analizar un caso de descanso y recreación: qué alternativas ofrecer, cómo incluir a todos y cómo reaccionar ante un despertar difícil.",
    prior=["Conozco los tipos de juego y los rincones.", "Sé que cada niño tiene su ritmo.", "Sé que el patio exige supervisión constante."],
    explain=[
        "Para analizar un caso de descanso y recreación se leen los datos: cuántos niños duermen y cuántos no, qué espacios hay y qué necesita cada niño. Con eso se organiza: a quienes no duermen se les ofrece un rincón tranquilo con libros blandos y cojines, y a los demás se les deja dormir en silencio. Un adulto vigila siempre la sala.",
        "La inclusión en el patio significa que todos los niños puedan jugar: si hay un sector con rampa, se elige para que quien usa silla de ruedas participe con los demás, sin separarlo del grupo. Un despertar difícil, como llorar al abrir los ojos, se acompaña con calma, voz baja y contacto cercano, y se informa a la educadora si se repite.",
        "Todo lo ocurrido se registra con hechos y se informa a la educadora, sin etiquetas sobre los niños." + LIM,
    ],
    vocab=[("rincón tranquilo", "zona con libros blandos y cojines para el reposo"), ("rampa", "superficie inclinada que permite avanzar con silla de ruedas"), ("inclusión", "participación de todos con los apoyos necesarios"), ("despertar difícil", "despertar con llanto o malestar"), ("acompañar", "estar cerca del niño con calma")],
    worked=[
        ("Contar los que no duermen", "En una sala de ejemplo hay 14 niños y duermen 9. ¿Cuántos no duermen?", ["Se resta lo que duermen al total.", "14 − 9 = 5."], "5 niños"),
        ("Elegir el sector", "Un niño de ejemplo usa muletas. El patio tiene un sector de arena suelta y otro con piso firme. ¿Cuál conviene?", ["La arena suelta dificulta avanzar.", "El piso firme permite que juegue con los demás."], "El sector de piso firme")
    ],
    mistakes=[("Dejar a Emilia mirando desde la ventana «porque el patio es difícil para ella».", "La excluye en vez de adaptar el espacio.", "Elige el sector con rampa y juega con ella."),
              ("Levantar a un niño que despierta llorando para llevarlo rápidamente al patio.", "Le quita el tiempo de calmarse y puede despertar a los demás.", "Acompáñalo en voz baja hasta que se calme.")],
    T=[
        ("=", "{F} ¿Cuántos niños no se duermen?", "16-11", "Al total se le restan los que duermen.", " niños"),
        ("abc", "{F} ¿Qué se ofrece a los niños que no duermen?", "El rincón tranquilo con libros blandos y cojines", "Un juego de pelotas", "Quedarse de pie en la sala", "El rincón tranquilo permite reposar sin molestar a otros."),
        ("abc", "{F} ¿Qué sector del patio conviene para Emilia?", "El sector con rampa y pasto, donde pueda jugar con los demás", "El sector de arena suelta", "Ninguno; se queda adentro", "La rampa permite que participe junto con sus compañeros de juego."),
        ("abc", "{F} Mateo se despierta llorando. ¿Qué hace la técnica?", "Se acerca, le habla en voz baja y lo acompaña hasta que se calme", "Lo manda al patio", "Lo deja llorar solo", "Un despertar difícil se acompaña con calma."),
        ("abc", "{F} Si Mateo llora todos los días al despertar, ¿qué hace la técnica?", "Informa a la educadora lo observado, con hechos y horas", "Le dice a la madre qué le pasa", "Anota que es un niño llorón", "La educadora evalúa; la técnica informa hechos."),
        ("=", "{F} Si Mateo se despierta a las 14:00 y se tranquiliza a las 14:12, ¿cuántos minutos tardó?", "(14*60+12)-(14*60)", "Se restan las horas, convertidas a minutos.", " minutos"),
        ("abc", "{F} Un compañero dice: «Emilia no puede jugar con los demás en el patio». ¿Qué observación corresponde?", "Se adapta el espacio y se juega junto, con la rampa", "Tiene razón", "Es mejor que juegue sola", "La inclusión busca la participación de todos."),
        ("abc", "{F} Hay 5 niños en el rincón tranquilo y uno empieza a hacer ruido. ¿Qué hace la técnica?", "Se acerca, le habla en voz baja y le ofrece otro libro", "Lo saca de la sala", "Le dice que se calle fuerte", "Se interviene en voz baja y con una alternativa."),
        ("=", "{F} Si Emilia tarda 6 minutos en bajar la rampa y lo repite 3 veces durante el patio, ¿cuántos minutos suma?", "6*3", "Se multiplican los minutos de cada vez por las repeticiones.", " minutos"),
        ("abc", "{F} Otra técnica propone dejar a los que no duermen en el patio, porque «así descansan los otros». ¿Qué observación corresponde?", "No: los niños necesitan supervisión y el patio no es un lugar de reposo en ese horario", "Está bien", "Está bien si juegan callados", "El reposo tranquilo se hace en la sala, con un adulto."),
        ("abc", "{F} Emilia pide ayuda para bajar de la rampa. ¿Qué hace la técnica?", "Le ofrece ayuda, la acompaña y le pregunta cómo prefiere recibirla", "La baja sin preguntar", "Le dice que se las arregle", "Se pregunta cómo quiere recibir ayuda."),
        ("=", "{F} De los 5 niños sin sueño, 3 eligen libros y el resto un osito. ¿Cuántos eligen el osito?", "5-3", "Al total se le restan los que eligen libros.", " niños"),
        ("abc", "{F} Antes de salir al patio, ¿qué hace la técnica?", "Revisa que no haya objetos peligrosos y el espacio sea seguro", "Sale de inmediato", "Pide a los niños que revisen", "La revisión previa es parte de la seguridad."),
    ],
    ctx=("abc", "{F} Una familia llega a las 14:20 a retirar a su hijo, que sigue dormido. ¿Qué hace la técnica?", "Le explica con calma y lo despierta suavemente con la educadora, sin apurarlo", "Lo despierta de golpe", "Le pide a la familia que espere en silencio una hora", "Se coordina con la educadora y se despierta con suavidad."),
    sc=[
        ("En Atención de Párvulos: ¿qué ofreces a los niños que no duermen?", "Un rincón tranquilo con libros blandos", "Así reposan sin molestar a los otros."),
        ("¿Cómo incluyes a una niña que usa silla de ruedas en el patio?", "Eligiendo un sector con rampa y jugando con ella", "La inclusión adapta el espacio para que todos puedan participar."),
        ("¿Qué haces si un niño despierta llorando?", "Lo acompaño con calma y en voz baja", "Necesita tiempo y compañía para tranquilizarse sin sentirse presionado."),
    ],
    op=("Caso de ejemplo. Nivel de transición, 20 niños y niñas. Después del almuerzo, 14 niños duermen y el resto no. Amaru usa andador y quiere jugar en el patio, que tiene un sector con piso firme y otro con piedras sueltas. Lía se despierta llorando a las 14:15. "
        "Escribe: cuántos niños no duermen y qué les ofrecerías; qué sector elegirías para Amaru; qué harías con Lía; y qué informarías a la educadora.",
        "No duermen 20 − 14 = 6 niños; les ofrecería libros blandos y objetos suaves en un rincón tranquilo. Para Amaru, el sector de piso firme, jugando junto con los demás. A Lía la acompañaría con calma, en voz baja. A la educadora: «Lía despertó llorando a las 14:15 y se calmó a las 14:25», con hechos.",
        ["calcula los niños sin sueño", "elige sector inclusivo", "acompaña con calma e informa con hechos"],
        ["hoja con un cálculo, dos acciones y un aviso"],
        ["dejar fuera a Amaru", "forzar a Lía a calmarse", "etiquetar a los niños"],
        "Pregunta: «¿qué harías si Amaru no quiere salir al patio?». Debe respetar su decisión y ofrecer otra alternativa."),
    reinforce="Escribe tres alternativas de juego tranquilo para niños que no duermen.",
    extend="Explica por qué adaptar el patio es mejor que dejar a un niño mirando desde la sala.",
)

# ============================================================ OAE-09, clase 4
F = ("Ficha 4 (planificación del tiempo libre, de ejemplo). Nivel medio, 18 niños y niñas; patio de 15:00 a 15:45 con 3 zonas (construcción con bloques grandes, juego simbólico y juego motor con colchonetas bajas). Se rota entre zonas cada 15 minutos. "
     "Después del almuerzo: 12 niños duermen, 4 hacen reposo tranquilo y 2 se levantan antes. Hay dos adultos y cada uno se ubica en un extremo del patio. La cantidad de adultos por niños la fija la norma vigente.")
build(
    O9, 4, F,
    use="Aprenderé a aplicar un criterio con datos para planificar el descanso y el tiempo libre: calcular grupos, rotaciones y tiempos, y verificar la supervisión.",
    prior=["Conozco tipos de juego y rincones.", "Sé calcular tiempos y dividir.", "Sé que la supervisión es constante."],
    explain=[
        "Planificar el tiempo libre es repartir a los niños en zonas y tiempos de modo que todos jueguen y estén seguros. Se divide el total de niños entre las zonas y se calcula cuánto tarda la rotación: si el tiempo total se divide por los minutos de cada zona, se sabe cuántas zonas alcanza a visitar cada grupo. Estos números son de ejemplo y la educadora puede cambiarlos.",
        "También se verifica la supervisión: los adultos se ubican para ver a todos los niños y las zonas deben ser visibles desde su posición. Después del descanso se registra cuántos niños durmieron, cuántos hicieron reposo tranquilo y cuántos se levantaron antes, sin juicios. Si algo no cuadra, se informa a la educadora.",
        "A los niños que se levantan antes se les ofrece otra alternativa de juego tranquilo para no despertar a los demás." + LIM,
    ],
    vocab=[("zona", "parte del patio con un tipo de juego"), ("rotación", "cambio ordenado de cada grupo a la zona siguiente"), ("registro del descanso", "anotación de cuántos niños durmieron, reposaron o se levantaron antes"), ("visible", "que se puede ver desde donde está el adulto"), ("ajuste", "cambio que decide la educadora")],
    worked=[
        ("Dividir en zonas", "En otro patio de ejemplo hay 12 niños y 3 zonas iguales. ¿Cuántos niños caben por zona?", ["Se divide el total entre las zonas.", "12 ÷ 3 = 4."], "4 niños"),
        ("Número de rotaciones", "El patio de ejemplo dura 30 minutos y cada zona 10. ¿Cuántas zonas alcanza a visitar cada grupo?", ["Se divide el tiempo por los minutos de cada zona.", "30 ÷ 10 = 3."], "3 zonas")
    ],
    mistakes=[("Calcular las zonas sin tener en cuenta a los niños que se levantan antes.", "Algunas zonas quedan con demasiados niños.", "Rehace el cálculo con los niños presentes en el patio."),
              ("Ubicar a los dos adultos en el mismo extremo del patio.", "Quedan zonas sin supervisión visual.", "Ubícalos para que, juntos, vean todas las zonas.")],
    T=[
        ("=", "{F} ¿Cuántos niños caben por zona si los 18 se reparten por igual en las 3 zonas?", "18//3", "Se divide el total entre las zonas.", " niños"),
        ("=", "{F} ¿Cuántos minutos dura el patio, de 15:00 a 15:45?", "(15*60+45)-(15*60)", "Se restan las horas, convertidas a minutos.", " minutos"),
        ("=", "{F} Si cada zona dura 15 minutos, ¿cuántas zonas alcanza a visitar cada grupo?", "45//15", "Se divide el tiempo total entre los minutos de cada zona.", " zonas"),
        ("=", "{F} ¿Cuántos niños se quedaron durmiendo o en reposo tranquilo?", "12+4", "Se suman los que duermen y los que hacen reposo.", " niños"),
        ("=", "{F} ¿Cuántos niños están en el registro del descanso?", "12+4+2", "Se suman los tres grupos del registro.", " niños"),
        ("abc", "{F} ¿Cómo se ubican los dos adultos?", "En lugares desde los que, juntos, vean todas las zonas", "Ambos en la zona de construcción", "Ambos en la sala", "La supervisión visual debe cubrir todo el patio."),
        ("abc", "{F} ¿Qué hace la técnica con los 2 niños que se levantan antes?", "Ofrece una alternativa tranquila para no despertar a los demás", "Los deja salir solos al patio", "Los obliga a dormir", "Se les ofrece un juego tranquilo."),
        ("=", "{F} Si hoy hay 3 niños ausentes, ¿cuántos niños hay en el patio?", "18-3", "A los niños de la ficha se les restan los ausentes.", " niños"),
        ("abc", "{F} Una de las zonas no se ve bien desde donde está el adulto. ¿Qué hace?", "Cambia su posición o avisa a la educadora para ajustar la zona", "Deja la zona sin adulto", "Pide a un niño que vigile", "Se corrige para tener supervisión visual."),
        ("abc", "{F} Un niño no quiere ir a la zona de juego motor porque tiene miedo. ¿Qué hace la técnica?", "Respeta su decisión y le ofrece otra zona", "Lo obliga a entrar", "Le dice que es miedoso", "Se respeta su ritmo y se le ofrece otra alternativa de juego."),
        ("=", "{F} Si se reparten los 18 niños en 3 zonas y 2 faltan, ¿cuántos niños hay en el patio?", "18-2", "Se restan los ausentes al total.", " niños"),
        ("abc", "{F} El registro dice 12 durmieron, 4 reposaron y 3 se levantaron antes. ¿Qué observación corresponde?", "Suma 19 y hay 18 niños: hay que revisar", "Está perfecto", "Está mal porque falta una zona", "12 + 4 + 3 = 19 no coincide con 18."),
        ("abc", "{F} A mitad del patio llueve. ¿Qué hace la técnica?", "Avisa a la educadora, que indica cómo volver a la sala en orden", "Sigue jugando", "Deja salir a los niños corriendo", "El cambio de plan lo decide la educadora y se hace con orden."),
    ],
    ctx=("abc", "{F} Tras el descanso, la técnica anota: «Camila durmió mal porque es inquieta». ¿Qué falla?", "Interpreta; debe anotar el hecho: «Camila no se durmió y estuvo en reposo tranquilo»", "Nada", "Que usó el nombre", "Los registros solo llevan hechos y no opiniones sobre los niños."),
    sc=[
        ("En Atención de Párvulos: ¿cómo se reparten los niños en las zonas?", "Dividiendo el total entre las zonas", "Así cada zona tiene una cantidad similar."),
        ("¿Qué haces si una zona no se ve desde tu posición?", "Cambio mi posición o aviso a la educadora", "La supervisión visual es constante, y las zonas deben verse desde donde está el adulto."),
        ("¿Cómo se registra el descanso?", "Con hechos y sin juicios", "Los hechos permiten evaluar y las opiniones no se pueden comprobar."),
    ],
    op=("Datos de ejemplo. Nivel de transición con 24 niños y niñas. Patio de 16:00 a 16:45, 3 zonas, rotación cada 15 minutos. Después del almuerzo, 15 duermen, 6 hacen reposo y el resto se levanta antes. Hay 2 adultos. "
        "Escribe: cuántos niños por zona; cuántas zonas visita cada grupo; cuántos niños se levantaron antes; cómo ubicarías a los adultos; y qué harías si el registro del descanso no suma 24.",
        "Por zona: 24 ÷ 3 = 8 niños. Cada grupo visita 45 ÷ 15 = 3 zonas. Se levantaron antes 24 − 15 − 6 = 3. Los adultos se ubican en extremos opuestos para ver todas las zonas. Si el registro no suma 24, lo reviso y aviso a la educadora.",
        ["calcula niños, zonas y tiempo", "ubica a los adultos para ver todo", "revisa el registro y avisa"],
        ["hoja con tres cálculos y dos acciones"],
        ["calcular mal la rotación", "dejar zonas sin supervisión", "no revisar el registro"],
        "Pregunta: «¿qué cambia si faltan 4 niños?». Debe recalcular con 20."),
    reinforce="Reparte 20 niños en 4 zonas y calcula cuántos hay en cada una.",
    extend="Explica por qué se rehace el cálculo cuando hay niños ausentes.",
)

# ============================================================ OAE-10, clase 1
F = ("Ficha 1 (antecedentes, de ejemplo). Ficha de matrícula: nombre del niño o niña, fecha de nacimiento, adultos responsables, teléfono y dirección. Ficha de salud: información entregada por la familia (por ejemplo, alergias) para que la educadora la conozca. "
     "Autorización de retiro: lista de personas autorizadas para retirar al niño. Registro de asistencia diario. Reglas de ejemplo: los antecedentes son confidenciales; se guardan bajo llave o en el sistema con clave personal; solo accede el personal autorizado; se actualizan cuando la familia informa un cambio.")
build(
    O10, 1, F,
    use="Aprenderé qué son los antecedentes de niños y familias, por qué son confidenciales y qué reglas generales rigen su registro y archivo, manual y digital.",
    prior=["Sé que los datos de los niños son confidenciales.", "Sé leer una ficha.", "Sé ordenar documentos."],
    explain=[
        "En Atención de Párvulos, los antecedentes son los datos de cada niño o niña y de su familia: matrícula, información de salud entregada por la familia, personas autorizadas para retirarlo y asistencia. Se registran para cuidar mejor al niño y para cumplir los requerimientos del establecimiento. Pueden estar en papel, en una carpeta, o de forma digital, en un sistema con clave.",
        "Son datos personales y confidenciales. Se guardan bajo llave o con clave personal, y solo accede el personal autorizado. No se dejan a la vista, no se publican ni se comentan con otras familias. Se actualizan cuando la familia informa un cambio, como un nuevo teléfono. La técnica ayuda a registrarlos y ordenarlos según las instrucciones de la educadora o de la dirección, y la norma vigente regula su protección.",
        "Si alguien pide datos de un niño, la técnica no los entrega y deriva a la educadora o a la dirección." + LIM,
    ],
    vocab=[("antecedentes", "datos de un niño y de su familia, como matrícula, salud y retiro"), ("ficha de matrícula", "documento con los datos básicos del niño y sus adultos responsables"), ("autorización de retiro", "lista de personas que pueden retirar al niño"), ("confidencial", "que no se comparte con personas no autorizadas"), ("clave personal", "contraseña propia que no se comparte"), ("actualizar", "cambiar un dato cuando la familia informa un cambio")],
    worked=[
        ("Quién puede retirar", "Una persona que no está en la lista llega a retirar a un niño de ejemplo. ¿Qué hace la técnica?", ["La lista de retiro es la regla.", "No entrega al niño y avisa a la educadora o dirección."], "No lo entrega y avisa a la educadora o dirección"),
        ("Guardar una ficha", "La ficha de salud de un niño de ejemplo queda abierta sobre la mesa. ¿Qué corresponde?", ["Es un dato confidencial.", "Se guarda bajo llave o en el archivo."], "Guardarla bajo llave o en el archivo"),
    ],
    mistakes=[("Compartir la clave del sistema con una compañera «para ir más rápido».", "La clave es personal y se pierde el control de quién accede.", "Cada persona usa su propia clave."),
              ("Entregar el teléfono de una familia a otra «porque se llevan bien».", "Son datos personales que solo la familia puede autorizar.", "Deriva a la educadora para que consulte a la familia.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué son los antecedentes de un niño?", "Datos de él y de su familia, como matrícula, salud, retiro y asistencia", "Los juguetes que más le gustan", "Las notas de los juegos", "Los antecedentes son los datos personales y de la familia."),
        ("abc", "{F} ¿Qué es la autorización de retiro?", "La lista de personas autorizadas para retirar al niño", "El horario de salida", "El registro de asistencia", "La lista dice quién puede retirar al niño."),
        ("abc", "{F} ¿Dónde se guardan los antecedentes?", "Bajo llave o en el sistema con clave personal", "En una mesa de la sala", "En la mochila del niño", "La regla pide guardarlos en un lugar protegido."),
        ("abc", "{F} ¿Quién accede a los antecedentes?", "Solo el personal autorizado", "Cualquier persona del jardín", "Las familias de otros niños", "Son confidenciales y solo los conoce el personal autorizado."),
        ("abc", "{F} Una abuela que figura en la lista de autorización llega a retirar a una niña. ¿Qué hace la técnica?", "Comprueba en la lista que figura, entrega a la niña según el protocolo y lo anota en el registro", "No la entrega, porque la abuela no es la madre", "Le pide que espere una hora sin explicar", "Quien figura en la lista puede retirar al niño; el retiro se comprueba y se registra."),
        ("abc", "{F} ¿Cuándo se actualiza una ficha?", "Cuando la familia informa un cambio", "Cada vez que el niño cumple años", "Nunca", "Se actualiza cuando hay un dato nuevo informado por la familia."),
        ("=", "{F} La carpeta del grupo tiene 20 fichas de matrícula y 3 aún están sin firmar. ¿Cuántas están firmadas?", "20-3", "Al total se le restan las que faltan firmar.", " fichas"),
        ("abc", "{F} Una compañera quiere llevarse a su casa las fichas de matrícula para avanzar el trabajo. ¿Qué corresponde?", "No hacerlo: los antecedentes se quedan guardados en el jardín y solo accede el personal autorizado", "Está bien si las devuelve al día siguiente", "Está bien si las lleva en su mochila", "Los antecedentes se guardan en el lugar protegido del jardín y no se sacan por cuenta propia."),
        ("abc", "{F} Una madre pide por teléfono el número de otra familia. ¿Qué responde la técnica?", "Que no puede entregarlo y que la educadora puede consultar a esa familia", "Se lo entrega", "Le da el número del jardín y de la otra familia", "Los datos personales solo se entregan con autorización."),
        ("=", "{F} Hay 18 niños y cada ficha de matrícula lleva 3 hojas. ¿Cuántas hojas hay en total?", "18*3", "Se multiplican las fichas por las hojas de cada una.", " hojas"),
        ("abc", "{F} ¿Por qué no se comparte la clave del sistema?", "Porque es personal y se pierde el control de quién accede", "Porque cuesta mucho", "Porque es más lento", "La clave identifica a cada persona autorizada."),
        ("abc", "{F} Una familia informa que cambió su número de teléfono. ¿Qué hace la técnica?", "Anota el cambio con la fecha en la ficha y avisa a la educadora", "No lo anota hasta fin de año", "Lo anota en un papel suelto", "Se actualiza la ficha para poder contactar."),
        ("abc", "{F} Alguien llama por teléfono preguntando si un niño asiste al jardín. ¿Qué responde la técnica?", "Que no puede dar información y que se comunique con la dirección", "Que sí asiste", "Que no sabe, pero que pregunte mañana", "No se confirma información de niños a personas desconocidas."),
    ],
    ctx=("abc", "{F} Un adulto llega a retirar a un niño. No está en la lista, pero tiene una nota firmada por la madre. ¿Qué hace la técnica?", "No entrega al niño y avisa de inmediato a la educadora o dirección para verificar", "Lo entrega por la nota", "Lo entrega si el niño lo conoce", "La verificación la hace la dirección con la familia."),
    sc=[
        ("En Atención de Párvulos: ¿quién puede retirar a un niño?", "Solo las personas de la lista de autorización", "La lista protege al niño porque nombra a quienes pueden retirarlo."),
        ("¿Dónde se guardan las fichas?", "Bajo llave o en el sistema con clave personal", "Así solo acceden las personas autorizadas."),
        ("¿Compartes tu clave?", "No", "La clave es personal y no se comparte con nadie."),
    ],
    op=("Caso de ejemplo. En un jardín de ejemplo hay 16 niños y niñas. Hoy una compañera dejó una carpeta con 16 fichas de matrícula abierta en la mesa. Alguien llama preguntando si «el niño de la ficha 7» está en el jardín. Un adulto desconocido quiere retirar a una niña. "
        "Escribe: qué harías con la carpeta; qué responderías a la llamada; qué harías con el adulto desconocido; y cuántas hojas hay si cada ficha tiene 2.",
        "Guardaría la carpeta bajo llave o en el archivo. A la llamada: «No puedo dar información; comuníquese con la dirección». Al adulto desconocido: no entregaría a la niña y avisaría de inmediato a la educadora o dirección. Hay 16 × 2 = 32 hojas.",
        ["protege los datos", "no entrega información ni entrega a la niña", "calcula las hojas"],
        ["hoja con tres acciones y un cálculo"],
        ["entregar a la niña", "dar información por teléfono", "dejar la carpeta abierta"],
        "Pregunta: «¿qué harías si el adulto se enoja?». Debe mantener la calma y avisar a la educadora o dirección."),
    reinforce="Escribe tres reglas para guardar y compartir antecedentes de niños.",
    extend="Explica por qué la lista de retiro protege a los niños.",
)

# ============================================================ OAE-10, clase 2
F = ("Ficha 2 (documentos de ejemplo). Registro de asistencia: lista diaria con presente (P), ausente (A) y justificada (J). Ficha de salud: información de la familia (por ejemplo, alergias), actualizada cada vez que la familia informa un cambio. "
     "Archivo: carpeta por niño ordenada por apellido, en un mueble con llave. Respaldo digital: copia de los datos en otro lugar protegido, con clave. Dato sensible: información de salud o de la situación familiar. Fecha de ejemplo: 14 de marzo.")
build(
    O10, 2, F,
    use="Aprenderé los documentos del registro de antecedentes, el orden del archivo manual y digital, los respaldos y la diferencia entre datos comunes y sensibles.",
    prior=["Conozco los antecedentes y su confidencialidad.", "Sé ordenar por apellido.", "Sé leer una ficha."],
    explain=[
        "Los documentos de antecedentes más comunes son: el registro de asistencia, con presentes, ausentes y justificadas; la ficha de matrícula; la ficha de salud, con información que entrega la familia; y la autorización de retiro. Cada niño tiene una carpeta ordenada por apellido, en un mueble con llave. Si se usa un sistema digital, se entra con clave personal y se hace un respaldo, que es una copia en otro lugar protegido para no perder los datos.",
        "Los datos se dividen en comunes, como el nombre, y sensibles, como la información de salud o de la situación familiar. Los sensibles tienen aún más reserva: solo los conoce quien los necesita para cuidar al niño. Cada dato se escribe con letra clara o se digita sin errores, con la fecha de registro, y las correcciones se hacen tachando con una línea, sin borrar.",
        "Mantener actualizados los antecedentes es revisar con las familias, cuando la educadora lo indica, si los datos siguen vigentes." + LIM,
    ],
    vocab=[("registro de asistencia", "lista diaria con presentes, ausentes y justificadas"), ("archivo", "conjunto de carpetas ordenadas y guardadas"), ("respaldo", "copia de los datos en otro lugar protegido"), ("dato sensible", "información de salud o de la situación familiar"), ("justificada", "ausencia que la familia explicó"), ("vigente", "que sigue siendo válido")],
    worked=[
        ("Ordenar por apellido", "Tres apellidos de ejemplo: Mora, Araya, Pérez. ¿Cuál es el orden alfabético?", ["Se ordena por la primera letra.", "A, M, P."], "Araya, Mora, Pérez"),
        ("Dato sensible", "¿«Alergia a un alimento» es un dato común o sensible?", ["Es información de salud.", "Es sensible."], "Sensible")
    ],
    mistakes=[("Archivar las carpetas por nombre de pila en vez de apellido.", "Se pierde el orden acordado y cuesta encontrarlas.", "Usa el orden por apellido indicado."),
              ("Guardar el respaldo digital en el mismo computador, sin clave.", "Si se pierde, se pierde todo y cualquiera accede.", "Guarda una copia en otro lugar protegido y con clave.")],
    T=[
        ("abc", "{F} ¿Qué significa «J» en el registro de asistencia?", "Ausencia justificada", "Presente", "Juego", "J es justificada; P es presente."),
        ("abc", "{F} ¿Cómo se ordena el archivo?", "Una carpeta por niño, ordenada por apellido", "Todo mezclado en una caja", "Ordenado por la altura de los niños", "La ficha fija el orden por apellido."),
        ("abc", "{F} ¿Qué es un respaldo digital?", "Una copia de los datos en otro lugar protegido, con clave", "Un papel con la clave", "Un archivo sin protección", "El respaldo evita perder los datos."),
        ("abc", "{F} ¿Cuál de estos datos es sensible?", "La información de salud del niño", "El nombre del niño", "El nivel del jardín", "La salud es un dato sensible."),
        ("abc", "{F} ¿Qué se hace con un error al escribir un dato?", "Se tacha con una línea y se anota el valor correcto", "Se borra con corrector", "Se rompe la hoja", "Con una línea se conserva el rastro."),
        ("abc", "Tres apellidos de ejemplo: Soto, Alarcón, Núñez. ¿Cuál es el orden alfabético?", "Alarcón, Núñez, Soto", "Soto, Núñez, Alarcón", "Núñez, Alarcón, Soto", "A, N, S es el orden correcto."),
        ("=", "{F} En el registro de asistencia de un día hay 20 matriculados, 17 presentes y 2 ausentes justificadas. ¿Cuántos ausentes sin justificar hay?", "20-17-2", "Al total se le restan presentes y justificadas.", " niños"),
        ("abc", "{F} Una compañera deja el respaldo digital en el mismo computador, sin clave. ¿Qué falla?", "Si el computador falla o se pierde, se pierden también los datos y cualquiera puede acceder", "Nada, es lo más rápido", "Que debería guardarlo en papel solamente", "Un respaldo se guarda en otro lugar y con clave."),
        ("=", "{F} Hay 20 carpetas y cada una lleva 4 hojas. ¿Cuántas hojas hay en total?", "20*4", "Se multiplican las carpetas por las hojas de cada una.", " hojas"),
        ("abc", "{F} Una madre informa que su hijo tiene una alergia nueva. ¿Qué hace la técnica?", "Le pide que informe a la educadora para actualizar la ficha de salud", "La anota en un papel suelto", "La comenta con otras familias", "La ficha de salud la actualiza la educadora con la información de la familia."),
        ("abc", "{F} Una técnica anota la dirección de una familia en el registro de asistencia. ¿Qué observación corresponde?", "La dirección va en la ficha de matrícula, no en el registro de asistencia", "Está bien", "Debe anotarla en el panel", "Cada dato va en el documento correspondiente."),
        ("=", "{F} Si el 14 de marzo hay 20 matriculados y 16 presentes, ¿cuántos faltaron?", "20-16", "Al total se le restan los presentes.", " niños"),
        ("abc", "{F} ¿Por qué es mejor revisar los datos con las familias cada cierto tiempo?", "Para mantenerlos vigentes", "Para cambiar a los niños de grupo", "Para pedir más documentos sin motivo", "Los datos cambian con el tiempo; actualizarlos protege al niño."),
    ],
    ctx=("abc", "{F} Al ordenar el archivo, la técnica nota que una carpeta tiene una ficha de salud con una anotación que no entiende. ¿Qué hace?", "Consulta a la educadora y no cambia nada por su cuenta", "La borra", "Pregunta a otras familias", "Los datos sensibles solo se revisan con la educadora."),
    sc=[
        ("En Atención de Párvulos: ¿cómo se ordena el archivo de fichas?", "Por apellido", "Así se encuentran las fichas más rápido cuando se necesitan."),
        ("En educación de párvulos: ¿qué es un dato sensible?", "Información de salud o de la situación familiar", "Tiene más reserva porque revela información íntima de la familia."),
        ("¿Dónde se guarda el respaldo digital?", "En otro lugar protegido, con clave", "Así no se pierde todo si falla el computador principal."),
    ],
    op=("Datos de ejemplo. Archivo de un nivel con 15 niños y niñas. Apellidos de ejemplo de cuatro de ellos: Vera, Araya, Muñoz, Díaz. Hoy asistieron 12; 1 faltó con justificación. "
        "Escribe: el orden alfabético de los cuatro apellidos; cuántos faltaron sin justificar; qué datos son sensibles en una ficha; y cómo guardarías el respaldo digital.",
        "Orden: Araya, Díaz, Muñoz, Vera. Faltaron 15 − 12 = 3, de los cuales 1 justificada, así que 2 sin justificar. Sensibles: información de salud y de la situación familiar. Respaldo: una copia en otro lugar protegido, con clave.",
        ["ordena correctamente", "calcula los ausentes sin justificar", "distingue datos sensibles y protege el respaldo"],
        ["hoja con un orden, un cálculo y dos respuestas"],
        ["ordenar por nombre de pila", "confundir ausentes", "guardar el respaldo sin clave"],
        "Pregunta: «¿qué pasaría si el computador falla?». Debe decir que el respaldo permite recuperar los datos."),
    reinforce="Ordena por apellido seis nombres de ejemplo que inventes.",
    extend="Explica por qué las correcciones se hacen tachando y no borrando.",
)

# ============================================================ OAE-10, clase 3
F = ("Ficha 3 (ficha con errores, de ejemplo, ficticia). Nombre: Niño A (ejemplo). Fecha de nacimiento: 31 de abril. Teléfono: 7 dígitos (debería tener 9). Autorización de retiro: «cualquier adulto». Última actualización: hace 2 años. "
     "Contraseña del sistema: anotada en un papel pegado en el monitor. Regla: los antecedentes se mantienen actualizados y completos, y las contraseñas son personales y no se anotan a la vista.")
build(
    O10, 3, F,
    use="Aprenderé a analizar un caso de registros con errores y a detectar problemas de datos, de actualización y de seguridad, y a comunicarlos a la educadora.",
    prior=["Conozco los documentos de antecedentes.", "Sé que las claves son personales.", "Sé revisar datos."],
    explain=[
        "Revisar una ficha es buscar datos imposibles, incompletos o desactualizados. Una fecha que no existe, como el 31 de abril, es un dato imposible, porque abril tiene 30 días. Un teléfono con menos dígitos de lo normal es incompleto. Una autorización de retiro que dice «cualquier adulto» no protege al niño, porque debe nombrar a personas concretas. Una ficha sin actualizar por mucho tiempo puede tener datos que ya no sirven.",
        "También se revisa la seguridad: una contraseña anotada a la vista permite que cualquiera entre al sistema. La técnica no corrige datos por su cuenta: informa a la educadora o a la dirección, que se comunican con la familia para actualizarlos. Los cambios se anotan con fecha y sin borrar lo anterior.",
        "Los errores no se comentan con otras familias ni se atribuyen a una persona; se corrigen con reserva y respeto." + LIM,
    ],
    vocab=[("dato imposible", "dato que no puede ser cierto, como una fecha que no existe"), ("dato incompleto", "dato al que le faltan partes, como un teléfono con menos dígitos"), ("desactualizado", "que ya no corresponde a la situación actual"), ("contraseña", "clave personal para entrar a un sistema"), ("verificar", "comprobar con la familia y con la educadora")],
    worked=[
        ("Detectar un dato imposible", "Una ficha de ejemplo dice «nacido el 30 de febrero». ¿Qué falla?", ["Febrero no tiene 30 días.", "Es una fecha imposible."], "Es una fecha imposible"),
        ("Qué hacer con un error", "Una compañera descubre que el teléfono de una ficha tiene un dígito de menos. ¿Qué hace?", ["No lo inventa ni lo corrige por su cuenta.", "Avisa a la educadora para consultar a la familia."], "Avisar a la educadora para consultar a la familia")
    ],
    mistakes=[("Completar un dígito faltante del teléfono «con el que parece».", "Puede quedar un número equivocado.", "Consulta a la familia a través de la educadora."),
              ("Anotar la contraseña en un papel pegado al monitor.", "Cualquiera podría entrar al sistema.", "Memorízala y no la anotes a la vista.")],
    T=[
        ("abc", "{F} ¿Qué falla en la fecha de nacimiento?", "El 31 de abril no existe, porque abril tiene 30 días", "Que está en abril", "Que falta el año", "Abril tiene 30 días, por eso esa fecha es imposible."),
        ("abc", "{F} ¿Qué falla en el teléfono?", "Está incompleto: tiene 7 dígitos y deberían ser 9", "Tiene dígitos repetidos", "Está escrito con guiones", "La ficha dice que debería tener 9 dígitos."),
        ("abc", "{F} ¿Qué falla en la autorización de retiro?", "Dice «cualquier adulto» y debería nombrar personas concretas", "Tiene demasiadas personas", "Está en el archivo", "Una autorización genérica no protege al niño."),
        ("abc", "{F} ¿Qué falla con la contraseña?", "Está anotada a la vista en el monitor", "Es muy larga", "Es personal", "Una contraseña a la vista permite el acceso de cualquiera."),
        ("abc", "{F} ¿Qué hace la técnica ante estos errores?", "Informa a la educadora o dirección, que verifican con la familia", "Los corrige ella misma con lo que le parece", "Los comenta con otras familias", "La técnica no corrige datos por su cuenta."),
        ("abc", "{F} La ficha lleva 2 años sin actualizarse. ¿Por qué es un problema?", "Los datos pueden haber cambiado y ya no servir", "Porque ocupa mucho espacio", "Porque el niño creció", "Datos viejos pueden impedir contactar a la familia en una emergencia."),
        ("=", "{F} Si el teléfono debería tener 9 dígitos y la ficha dice 7, ¿cuántos dígitos faltan?", "9-7", "Se restan los dígitos que tiene a los que debería tener.", " dígitos"),
        ("abc", "{F} ¿Cuál de estas es una fecha imposible?", "31 de noviembre", "30 de noviembre", "1 de noviembre", "Noviembre tiene 30 días, por eso el 31 no existe."),
        ("abc", "{F} Una compañera propone borrar el dato con corrector y escribir otro. ¿Qué observación corresponde?", "Se tacha con una línea y se anota el correcto con la fecha", "Está bien: así queda limpio", "Está bien si nadie lo ve", "No se pierde el rastro de lo anotado."),
        ("=", "{F} Si de las 20 fichas del grupo 6 llevan más de 1 año sin actualizar, ¿cuántas están al día?", "20-6", "Al total se le restan las desactualizadas.", " fichas"),
        ("abc", "{F} Un sistema digital pide cambiar la contraseña. ¿Qué hace la técnica?", "La cambia y la memoriza, sin anotarla a la vista", "La deja igual", "La comparte con una compañera", "Cambiar la contraseña protege el acceso."),
        ("abc", "{F} Al corregir la ficha, la técnica descubre que el error lo cometió una compañera. ¿Qué hace?", "Informa el dato a corregir a la educadora, sin culpar a nadie", "Le avisa a toda la sala quién se equivocó", "Escribe el nombre de la compañera en la ficha", "El objetivo es corregir con reserva y respeto."),
        ("abc", "{F} Una familia informa un cambio de teléfono en la puerta. ¿Qué hace la técnica?", "Lo anota con la fecha, lo comunica a la educadora y actualiza la ficha según la indicación", "Lo olvida", "Lo anota en la mano", "Los cambios se registran con fecha para mantener los datos al día."),
    ],
    ctx=("abc", "{F} Una persona llama diciendo que es la madre de un niño y pide cambiar el número de teléfono en la ficha. ¿Qué hace la técnica?", "Le pide que se comunique con la dirección o la educadora para verificar su identidad", "Cambia el número de inmediato", "Le pide que envíe el cambio por mensaje", "Los cambios de datos se verifican para evitar suplantaciones."),
    sc=[
        ("En Atención de Párvulos: ¿qué falla tiene una fecha como el 31 de abril?", "No existe", "Abril tiene 30 días, por eso el 31 no existe."),
        ("¿Quién corrige los datos erróneos?", "La educadora o dirección, con la familia", "La técnica informa y no corrige por su cuenta."),
        ("¿Anotas tu contraseña a la vista?", "No", "La contraseña es personal y no debe estar a la vista."),
    ],
    op=("Ficha de ejemplo (ficticia): Niña B. Fecha de nacimiento: 31 de junio. Teléfono: 8 dígitos (deberían ser 9). Retiro: «la abuela y su tío». Última actualización: hace 18 meses. La contraseña del sistema está anotada en un post-it. "
        "Escribe: los problemas que ves; qué harías con cada uno; a quién informarías; y cómo evitarías que vuelva a pasar.",
        "Problemas: fecha inexistente (junio tiene 30 días), teléfono incompleto (falta 1 dígito), retiro sin nombres completos, ficha desactualizada y contraseña a la vista. Informaría a la educadora o dirección para verificar con la familia; no corrijo nada por mi cuenta. Para evitarlo: actualizar fichas en fechas fijas y memorizar contraseñas.",
        ["detecta los cinco problemas", "no corrige por su cuenta e informa", "propone prevenir"],
        ["hoja con cinco problemas, una acción y una prevención"],
        ["inventar datos", "no ver la contraseña a la vista", "culpar a alguien"],
        "Pregunta: «¿qué pasaría si no se corrige la autorización de retiro?». Debe decir que podrían retirarlo personas no autorizadas."),
    reinforce="Revisa una ficha de ejemplo que inventes y marca dos datos que habría que verificar.",
    extend="Explica por qué una autorización de retiro con nombres concretos protege más al niño.",
)

# ============================================================ OAE-10, clase 4
F = ("Ficha 4 (asistencia de ejemplo, semana de 5 días). 20 niños y niñas matriculados. Presentes: lunes 18, martes 17, miércoles 19, jueves 16, viernes 18. Regla de ejemplo: si un niño falta 3 días seguidos, se avisa a la educadora. "
     "Respaldo digital: se hace los viernes. Archivo: 20 carpetas, cada una con 3 documentos (matrícula, salud y retiro).")
build(
    O10, 4, F,
    use="Aprenderé a aplicar un criterio con datos para el registro de asistencia, el archivo y los respaldos: calcular totales, porcentajes y documentos faltantes, y comunicarlos a la educadora.",
    prior=["Conozco los documentos de antecedentes.", "Sé multiplicar, sumar y dividir.", "Sé que los datos son confidenciales."],
    explain=[
        "Con el registro de asistencia se calcula cuántas asistencias hubo en la semana: se suman los presentes de cada día. Las asistencias posibles son los matriculados por los días. El porcentaje de asistencia se calcula multiplicando las asistencias por 100 y dividiendo por las posibles. Estos números se informan a la educadora tal como son, sin juicios sobre las familias.",
        "El archivo se revisa multiplicando carpetas por documentos que debe haber y comparando con los que hay, para saber cuántos faltan. Si falta un documento, se avisa a la educadora, que lo solicita a la familia. Los respaldos digitales se hacen en una fecha fija y se anota cuándo se hicieron.",
        "Cuando un niño falta varios días seguidos, la técnica avisa a la educadora, que se comunica con la familia; la técnica no llama por su cuenta ni opina sobre los motivos." + LIM,
    ],
    vocab=[("asistencia", "presencia de un niño en el jardín en un día"), ("asistencias posibles", "matriculados multiplicados por los días"), ("porcentaje de asistencia", "asistencias por 100 divididas por las posibles"), ("documento faltante", "documento que debería estar en la carpeta y no está"), ("fecha fija", "fecha acordada para repetir una tarea, como el respaldo")],
    worked=[
        ("Asistencias de la semana", "Un grupo de ejemplo tuvo 10, 12 y 11 presentes en tres días. ¿Cuántas asistencias suma?", ["Se suman los presentes de cada día.", "10 + 12 + 11 = 33."], "33 asistencias"),
        ("Porcentaje", "En un grupo de ejemplo hubo 45 asistencias de 50 posibles. ¿Qué porcentaje es?", ["Se multiplica por 100 y se divide por las posibles.", "45 × 100 ÷ 50 = 90."], "90 %")
    ],
    mistakes=[("Calcular el porcentaje dividiendo por los días en vez de por las asistencias posibles.", "Se obtiene un valor que no tiene sentido.", "Divide por matriculados por días."),
              ("Llamar a la familia de un niño ausente para preguntar el motivo, por cuenta propia.", "La comunicación con la familia la conduce la educadora.", "Avisa a la educadora, que decide.")],
    T=[
        ("=", "{F} ¿Cuántas asistencias suma la semana?", "18+17+19+16+18", "Se suman los presentes de los cinco días.", " asistencias"),
        ("=", "{F} ¿Cuántas asistencias posibles hay en la semana?", "20*5", "Se multiplican los matriculados por los días.", " asistencias"),
        ("=", "{F} ¿Cuál fue el porcentaje de asistencia de la semana?", "(18+17+19+16+18)*100//(20*5)", "Se multiplican las asistencias por 100 y se dividen por las posibles.", " %"),
        ("=", "{F} ¿Cuántos niños faltaron el jueves?", "20-16", "Al total de matriculados se le restan los presentes.", " niños"),
        ("abc", "{F} Un niño falta lunes, martes y miércoles. ¿Qué hace la técnica?", "Avisa a la educadora, según la regla de ejemplo", "Llama a la familia por su cuenta", "Lo da de baja del registro", "Según la regla, se avisa a la educadora."),
        ("=", "{F} ¿Cuántos documentos debe haber en el archivo completo?", "20*3", "Se multiplican las carpetas por los documentos de cada una.", " documentos"),
        ("=", "{F} Si en el archivo hay 54 documentos, ¿cuántos faltan?", "20*3-54", "Se restan los documentos que hay a los que deberían haber.", " documentos"),
        ("abc", "{F} Faltan 6 documentos en el archivo. ¿Qué hace la técnica?", "Informa a la educadora, que los solicita a las familias", "Los completa con información del jardín", "Los pide a las familias directamente", "La solicitud a la familia la hace la educadora."),
        ("abc", "{F} ¿Cuándo se hace el respaldo digital?", "Los viernes", "Los lunes", "Nunca", "La ficha fija el viernes como fecha de respaldo semanal."),
        ("=", "{F} El miércoles hubo 19 presentes. ¿Cuántos más que el jueves?", "19-16", "Se restan los presentes del jueves a los del miércoles.", " niños"),
        ("abc", "{F} Una compañera dice: «con 88 % de asistencia, esas familias no se preocupan». ¿Qué observación corresponde?", "No se hacen juicios sobre las familias a partir de un número", "Tiene razón", "Hay que llamarlas a todas", "Los números se informan sin juicios."),
        ("=", "{F} Si el viernes faltaran 3 niños más (quedan 15 presentes), ¿cuántas asistencias sumaría la semana?", "18+17+19+16+15", "Se suman los presentes de los días, cambiando el del viernes.", " asistencias"),
        ("abc", "{F} Olvidó hacer el respaldo del viernes. ¿Qué hace la técnica?", "Lo hace apenas pueda y anota la fecha real", "Anota que lo hizo el viernes", "No lo hace nunca", "Se registra con honestidad la fecha en que se hizo."),
    ],
    ctx=("abc", "{F} Al informar a la educadora, la técnica quiere decir que las familias de los niños ausentes «no son responsables». ¿Qué corresponde?", "Informar solo las cifras y los hechos, sin juicios", "Decirlo con tono suave", "Decirlo solo a una compañera", "Los juicios no ayudan; las cifras sí."),
    sc=[
        ("En Atención de Párvulos: ¿cómo se calculan las asistencias posibles?", "Matriculados por días", "Eso da el total posible de asistencias en la semana."),
        ("¿Quién llama a la familia de un niño que falta varios días?", "La educadora", "Ella conduce la comunicación con las familias."),
        ("¿Cuándo se hace el respaldo?", "En una fecha fija", "Así no se pierden los datos."),
    ],
    op=("Datos de ejemplo. 25 niños y niñas matriculados. Presentes en cuatro días: 22, 23, 21 y 24. Cada niño tiene una carpeta con 3 documentos y hay 70 documentos en el archivo. "
        "Escribe: cuántas asistencias hubo; cuántas eran posibles; el porcentaje de asistencia; cuántos documentos faltan; y qué avisarías a la educadora.",
        "Asistencias: 22 + 23 + 21 + 24 = 90. Posibles: 25 × 4 = 100. Porcentaje: 90 × 100 ÷ 100 = 90 %. Documentos: 25 × 3 = 75 y hay 70, faltan 5. Aviso: «Hubo 90 % de asistencia y faltan 5 documentos en el archivo».",
        ["calcula asistencias, posibles y porcentaje", "calcula los documentos faltantes", "informa sin juicios"],
        ["hoja con cuatro cálculos y un aviso"],
        ["calcular mal el porcentaje", "olvidar los documentos faltantes", "agregar juicios"],
        "Pregunta: «¿qué harías si un niño falta tres días seguidos?». Debe avisar a la educadora según la regla de ejemplo."),
    reinforce="Calcula el porcentaje de asistencia de un grupo de ejemplo de 10 niños en 2 días con 9 y 8 presentes.",
    extend="Explica por qué los números de asistencia se informan sin juicios sobre las familias.",
)
