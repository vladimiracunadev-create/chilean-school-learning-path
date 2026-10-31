"""Cuaderno del estudiante, 6.º básico Orientación: OA 07 (resolver conflictos de convivencia) y OA 08 (participación en la comunidad escolar)."""
from __future__ import annotations

from student_lessons import arith, ex
from student_content_or6_a import M, T, W, lesson

OA7, OA8 = "OR06 OA 07", "OR06 OA 08"

# ================================================================ OA 07
lesson(
    OA7, 1,
    "Una hoja y un lápiz. El caso del balón y del turno del computador, con personajes inventados, está escrito en los ejercicios.",
    "Aprenderé a identificar un conflicto: quiénes participan, qué pasó y qué necesita cada uno. Sirve para resolverlo por mí mismo en vez de pelear o esperar a que alguien lo arregle.",
    ["Sé separar hechos de suposiciones.", "Sé decir lo que siento con un mensaje «yo»."],
    [
        "Un conflicto de convivencia es un desacuerdo entre personas porque quieren cosas distintas o no se entienden. Tener un conflicto no es malo; es normal. Lo que importa es cómo se resuelve. Para resolverlo de forma autónoma, es decir, por tus propios medios y sin esperar a que otro lo haga, primero hay que entenderlo.",
        "Para entenderlo, responde cuatro preguntas. ¿Quiénes son las partes, es decir, las personas involucradas? ¿Qué pasó, solo con hechos? ¿Qué quiere cada uno? ¿Por qué lo quiere? Distingue la posición, que es lo que alguien dice que quiere («quiero el balón»), del interés, que es la necesidad detrás («quiero jugar un partido con mi equipo»). A veces las posiciones chocan, pero los intereses se pueden conciliar.",
        "Por ejemplo, Rocío y Beto discuten por un computador del colegio. Rocío dice «lo necesito ahora» porque debe entregar una tarea; Beto dice «yo estaba antes» porque quiere terminar su ficha. Sus posiciones chocan, pero sus intereses (terminar un trabajo) permiten un acuerdo, como turnarse 15 minutos cada uno. Entender el conflicto es el primer paso para encontrar una solución justa.",
    ],
    [("conflicto", "desacuerdo entre personas por querer cosas distintas o no entenderse"), ("partes", "personas involucradas en el conflicto"), ("posición", "lo que alguien dice que quiere"), ("interés", "necesidad que hay detrás de lo que alguien pide"), ("autónomo", "por mis propios medios y con responsabilidad")],
    [
        W("Identificar las partes y los hechos", "Rocío y Beto discuten porque ambos quieren usar el único computador libre. ¿Quiénes son las partes y cuál es el hecho?", ["Las partes son Rocío y Beto.", "El hecho es que hay un solo computador libre y ambos lo quieren.", "No sabemos aún por qué lo quiere cada uno."], "Partes: Rocío y Beto. Hecho: hay un solo computador libre y ambos lo quieren"),
        W("Separar posición e interés", "Beto dice «yo estaba antes» porque necesita terminar su ficha. ¿Cuál es la posición y cuál el interés?", ["Lo que dice es 'yo estaba antes': la posición.", "Lo que necesita es terminar su ficha: el interés.", "Con el interés se puede negociar."], "Posición: «yo estaba antes». Interés: terminar su ficha"),
    ],
    [
        M("Pensar que en un conflicto alguien gana y el otro pierde.", "Se confunde lo que dicen con lo que necesitan.", "Busca los intereses: a veces ambos pueden ganar un poco."),
        M("Culpar al otro antes de entender qué pasó.", "Se parte de una suposición.", "Primero cuenta los hechos y pregunta qué necesita cada uno."),
    ],
    R=[
        ex("Las personas involucradas en un conflicto, ¿son las partes o los testigos?", "Las partes", "Son quienes tienen el desacuerdo."),
        ex("«Quiero el balón ahora» es lo que alguien pide. ¿Es una posición o un interés?", "Una posición", "Dice lo que quiere, no la necesidad que hay detrás."),
        ex("¿Tener un conflicto es siempre algo malo? Responde sí o no.", "No", "Es normal; lo importante es cómo se resuelve."),
    ],
    U=[
        ex("¿Por qué conviene preguntar «¿por qué lo quieres?» en un conflicto?", "Para descubrir la necesidad detrás", "Permite encontrar el interés y buscar acuerdos."),
        ex("¿Qué significa resolver un conflicto de forma autónoma?", "Resolverlo con mis propios medios y responsabilidad", "No espera que otro lo arregle por mí."),
        ex("Dos estudiantes piden el mismo libro. Uno lo quiere para una tarea y el otro para leer por gusto. ¿Los intereses son iguales?", "No", "Uno lo necesita para una tarea y otro por entretención."),
    ],
    A=[
        ex("Datos: 1) Ema y Luz discuten; 2) Ema quiere la mesa grande para su afiche; 3) Luz quiere la mesa grande para armar una maqueta; 4) hay dos mesas pequeñas libres. ¿Cuántas partes hay?", "2", "Las partes son Ema y Luz."),
        ex("Tomás dice «no me dejaron entrar al juego». ¿Qué debes preguntar para entender el conflicto: «¿quién tuvo la culpa?» o «¿qué pasó y qué necesitabas?»", "«¿Qué pasó y qué necesitabas?»", "Busca hechos e intereses, no culpables."),
        ex("Dani quiere cambiar de puesto «porque no veo». ¿Cuál es el interés? A) Cambiarse de puesto. B) Ver bien la pizarra. C) Molestar a otro.", "B", "La necesidad es ver la pizarra; cambiarse es una posición."),
    ],
    Z=[
        ex("Dos posiciones chocan: «yo uso el balón» y «yo lo uso». Si los intereses son jugar un partido, ¿qué solución permite ambos intereses?", "Jugar un partido juntos", "Ambos quieren jugar, así que pueden compartir."),
        ex("¿Por qué culpar al otro al principio dificulta resolver un conflicto?", "Porque el otro se defiende y no escucha", "Culpar provoca defensa."),
    ],
    D=[
        arith("En el curso hubo 12 conflictos en un mes. Se resolvieron 8 con diálogo. ¿Cuántos quedaron sin resolver?", "12-8", "Se restan los resueltos al total."),
        arith("Rocío y Beto se turnan el computador: 15 minutos cada uno, 2 turnos cada uno. ¿Cuántos minutos usan entre los dos?", "15*2*2", "Se multiplican los minutos por los turnos y por las dos personas."),
    ],
    context=[ex("Dos estudiantes discuten por el uso de la cancha: uno quiere jugar fútbol y el otro basquetbol, y ambos tienen 30 minutos de recreo. Un compañero propone que cada uno use la cancha 15 minutos. ¿Atiende ambos intereses?", "Sí", "Ambos pueden jugar la mitad del tiempo.")],
    selfcheck=[ex("En Orientación: ¿las partes son las personas involucradas en el conflicto?", "Sí", "Son quienes tienen el desacuerdo."), ex("¿El interés es la necesidad detrás de lo que alguien pide?", "Sí", "Explica por qué lo quiere."), ex("¿Hay que buscar culpables antes de entender el conflicto?", "No", "Primero se entienden hechos e intereses.")],
    task=T("Lee el conflicto de Mati y Sofi, personajes inventados: ambas quieren usar la única impresora de la sala; Mati necesita imprimir su afiche para mañana y Sofi necesita imprimir una guía para estudiar. Identifica las partes, los hechos, la posición y el interés de cada una.", "Partes: Mati y Sofi. Hecho: hay una sola impresora y ambas la necesitan. Mati: posición «uso la impresora ahora»; interés: entregar su afiche mañana. Sofi: posición «yo la uso ahora»; interés: estudiar con su guía.", ["identifica las dos partes", "dice el hecho sin culpar", "separa posición e interés de cada una", "no cuenta una vivencia propia"], ["tabla escrita"], ["culpar a una parte", "confundir posición con interés"], "Reconoce la tabla y pregunta qué solución atendería los dos intereses."),
    reinforce="Describe un conflicto de un cuento con sus partes, el hecho, la posición y el interés de cada uno.",
    extend="Explica por qué dos personas pueden tener intereses distintos aunque pidan lo mismo.",
)

lesson(
    OA7, 2,
    "Una hoja y un lápiz. Las frases de los personajes y las escenas están escritas en los ejercicios.",
    "Aprenderé a escuchar de forma activa y a manejar mis emociones y límites durante un conflicto. Sirve para que la conversación avance y nadie se sienta atacado.",
    ["Sé identificar partes, posiciones e intereses.", "Sé expresar emociones con un mensaje «yo»."],
    [
        "Cuando hay un conflicto, las emociones suben. Antes de hablar de la solución, conviene calmarse y escuchar. La escucha activa consiste en prestar atención total, no interrumpir, mirar a la persona y comprobar que entendiste. Una forma es parafrasear, es decir, repetir con tus palabras lo que escuchaste: «Entonces te enojaste porque pasé sin avisar, ¿es así?». Si no entendiste bien, la otra persona te corrige.",
        "También hay que cuidar los límites. Un límite en un conflicto es lo que no vas a permitir ni hacer: no gritar, no insultar, no empujar y no hablar de lo que no corresponde. Puedes decir «Quiero resolver esto, pero necesito que hablemos sin gritar». Si la emoción es muy fuerte, puedes pedir una pausa: «Necesito 5 minutos y luego seguimos». Esa pausa no evita el problema; permite hablar mejor.",
        "Un mensaje «yo» ayuda a explicar tu parte: «Cuando tomaste mi estuche sin preguntar, me sentí molesto. Me gustaría que me preguntes primero». Combinado con la escucha activa, genera más confianza y más posibilidades de acuerdo. Si alguien amenaza con golpear o se pone violento, el límite es alejarte y pedir ayuda a un adulto de inmediato.",
    ],
    [("escucha activa", "prestar atención total y comprobar que entendí"), ("parafrasear", "repetir con mis palabras lo que escuché"), ("límite", "lo que no voy a permitir ni hacer en la conversación"), ("pausa", "momento para calmarme antes de seguir"), ("violencia", "acción que daña a otro con golpes, amenazas o insultos")],
    [
        W("Parafrasear", "Ema dice: «Me molestó que te llevaras mi cuaderno sin avisarme». ¿Cómo parafrasea Luz: «Entonces te molestó que tomara el cuaderno sin avisarte, ¿cierto?» o «Ya, pero igual lo necesitaba»?", ["La primera repite lo que entendió.", "La segunda no comprueba nada.", "Parafrasear es repetir con tus palabras."], "«Entonces te molestó que tomara el cuaderno sin avisarte, ¿cierto?»"),
        W("Poner un límite", "En una discusión, Beto empieza a gritar. ¿Qué límite respetuoso puede poner Rocío?", ["No sirve gritar de vuelta.", "Puede pedir calma y proponer hablar sin gritar.", "O pedir una pausa."], "«Quiero resolver esto, pero necesito que hablemos sin gritar»"),
    ],
    [
        M("Pensar mi respuesta mientras el otro habla para ganar la discusión.", "Se escucha para contestar y no para entender.", "Escucha primero, parafrasea y luego responde."),
        M("Seguir discutiendo aunque la rabia me desborde.", "Se cree que parar es perder.", "Pide una pausa de unos minutos y vuelve a conversar."),
    ],
    R=[
        ex("Repetir con tus palabras lo que escuchaste, ¿es parafrasear o interrumpir?", "Parafrasear", "Comprueba que entendiste."),
        ex("¿Pedir una pausa cuando estás muy alterado es una forma de cuidar la conversación? Responde sí o no.", "Sí", "Permite calmarse antes de hablar."),
        ex("Si alguien amenaza con golpear, ¿qué haces primero: alejarte y pedir ayuda adulta o seguir discutiendo?", "Alejarme y pedir ayuda adulta", "La seguridad es lo primero."),
    ],
    U=[
        ex("¿Por qué parafrasear ayuda a que el otro se sienta escuchado?", "Porque muestra que presté atención", "El otro ve que lo entendí."),
        ex("¿Por qué conviene calmarse antes de buscar la solución?", "Porque con emociones muy altas se piensa peor", "Calmarse permite escuchar y proponer."),
        ex("¿Qué es un límite en un conflicto: lo que no voy a permitir ni hacer, o lo que quiero ganar?", "Lo que no voy a permitir ni hacer", "Cuida el respeto de ambos."),
    ],
    A=[
        ex("Conductas: 1) mirar a la persona; 2) interrumpir; 3) parafrasear; 4) gritar; 5) pedir una pausa. ¿Cuántas son de escucha activa o autocuidado?", "3", "Mirar, parafrasear y pedir una pausa ayudan; interrumpir y gritar no."),
        ex("Luz dice: «Me enojó que no me esperaras para la fila». ¿Cómo parafrasea Dani? A) «Tú siempre te enojas por todo». B) «Entonces te enojó que no te esperara en la fila, ¿es así?» C) «No fue para tanto».", "B", "Repite con sus palabras y comprueba."),
        ex("Tomás está muy alterado en una discusión. ¿Qué frase sirve? A) «Necesito 5 minutos y luego seguimos». B) «No voy a hablar nunca más contigo». C) «Tú tienes la culpa».", "A", "Pide una pausa y promete volver."),
    ],
    Z=[
        ex("¿Por qué parafrasear no significa estar de acuerdo con el otro?", "Porque solo comprueba lo entendido", "Se puede entender sin aceptar."),
        ex("¿Por qué el límite 'no gritar' protege a ambas partes?", "Porque evita que la discusión se vuelva violenta", "Ambos pueden hablar sin sentirse atacados."),
    ],
    D=[
        arith("Una discusión duró 10 minutos antes de pedir una pausa y 5 minutos de pausa. ¿Cuántos minutos pasaron en total?", "10+5", "Se suman los dos tiempos."),
        arith("En una semana, Dani parafraseó 3 veces por día durante 4 días. ¿Cuántas veces parafraseó?", "3*4", "Se multiplican las veces por los días."),
    ],
    context=[ex("Valentina y Bruno discuten por un trabajo en grupo. Bruno dice: «No hiciste tu parte». Valentina responde: «Entonces te molesta que no entregué mi parte, ¿cierto? Tienes razón; me falta terminar. ¿Podemos organizarnos para hoy?». ¿Usó escucha activa?", "Sí", "Parafraseó lo que escuchó y propuso seguir conversando.")],
    selfcheck=[ex("En Orientación: ¿parafrasear es repetir con mis palabras lo que escuché?", "Sí", "Comprueba que entendí."), ex("¿Es buena idea gritar para que me escuchen?", "No", "Provoca defensa en el otro."), ex("¿Pedir una pausa puede ayudar?", "Sí", "Permite calmarse y volver a hablar.")],
    task=T("Lee este diálogo inventado entre Isidora y Ian: Ian dice «No me dejaste entrar a tu grupo y me sentí excluido». Escribe cómo Isidora puede (1) parafrasear lo que escuchó, (2) decir su versión con un mensaje «yo» y (3) poner un límite si Ian empieza a gritar.", "(1) «Entonces te sentiste excluido porque no te dejé entrar, ¿es así?» (2) «Cuando no te invité, me faltaban cupos y me sentí presionada; me gustaría explicártelo». (3) «Quiero seguir hablando, pero necesito que no grites».", ["parafrasea con sus palabras", "usa un mensaje «yo»", "pone un límite respetuoso", "no cuenta una vivencia propia"], ["diálogo escrito o dramatizado"], ["no comprobar lo entendido", "poner un límite agresivo"], "Reconoce el diálogo y pregunta qué haría si Ian no se calma."),
    reinforce="Escribe tres paráfrasis para frases como «me molestó que no me esperaras».",
    extend="Explica por qué escuchar bien suele acortar un conflicto.",
)

lesson(
    OA7, 3,
    "Una hoja y un lápiz. Los conflictos y la tabla de estrategias están escritos en los ejercicios.",
    "Aprenderé a comparar estrategias para resolver un conflicto (turnarse, repartir, acordar condiciones, pedir mediación) y a prever sus consecuencias. Sirve para elegir una solución justa.",
    ["Sé identificar intereses.", "Sé escuchar de forma activa."],
    [
        "Hay varias estrategias para resolver un conflicto. Turnarse es que cada uno use algo por un tiempo igual. Repartir es dividir lo que se disputa entre las partes. Acordar condiciones es establecer reglas claras, como «yo uso el balón ahora y tú después del recreo». La mediación es pedir a una tercera persona neutral, como un compañero o un adulto, que ayude a conversar sin tomar partido. Y también existe ceder, cuando una parte renuncia a algo, y buscar una tercera opción que mejore la situación para ambos.",
        "Para elegir bien, compara cada estrategia con tres preguntas: ¿atiende los intereses de ambos?, ¿es justa?, ¿se puede cumplir? Piensa en las consecuencias. Si uno cede siempre, se puede sentir injusto. Si se impone el más fuerte, el conflicto vuelve. Si se acuerdan turnos claros, es probable que funcione. Una buena solución suele ser aquella con la que ambos quedan conformes aunque ninguno consiga todo.",
        "No todos los conflictos se resuelven solos. Si hay golpes, amenazas, burlas repetidas o miedo, la estrategia correcta es pedir ayuda a un adulto de inmediato. Pedir mediación no significa fracasar; significa usar una buena estrategia.",
    ],
    [("turnarse", "usar algo por tiempos iguales cada uno"), ("mediación", "ayuda de una tercera persona neutral para conversar"), ("ceder", "renunciar a una parte de lo que se quería"), ("acuerdo justo", "solución con la que ambas partes quedan conformes"), ("consecuencia", "lo que ocurre después de una decisión")],
    [
        W("Comparar dos estrategias", "Ema y Luz quieren la misma pelota en el recreo de 30 minutos. Opciones: A) turnarse 15 minutos cada una; B) la más alta la usa todo el tiempo. ¿Cuál es más justa?", ["A atiende los intereses de las dos.", "B favorece solo a una.", "A se puede cumplir."], "A"),
        W("Prever una consecuencia", "Si Bruno cede siempre en los conflictos del grupo, ¿qué consecuencia probable tendrá?", ["Cede aunque no esté de acuerdo.", "Puede sentir que es injusto.", "El conflicto puede volver o acumular enojo."], "Puede sentirse injustamente tratado y acumular enojo"),
    ],
    [
        M("Creer que la única solución justa es dividir todo por la mitad.", "Se piensa que el acuerdo siempre debe ser igual.", "Busca un acuerdo con el que ambos queden conformes, aunque no sea igual."),
        M("Pensar que pedir mediación es fracasar.", "Se confunde pedir ayuda con perder.", "La mediación es una estrategia válida y madura."),
    ],
    R=[
        ex("Usar algo por tiempos iguales cada uno, ¿es turnarse o ceder?", "Turnarse", "Cada uno lo usa por turnos."),
        ex("Pedir a una tercera persona neutral que ayude a conversar, ¿es mediación o castigo?", "Mediación", "El mediador no toma partido."),
        ex("Si hay golpes o amenazas, ¿conviene pedir ayuda a un adulto de inmediato? Responde sí o no.", "Sí", "La seguridad es lo primero."),
    ],
    U=[
        ex("¿Por qué conviene preguntar si la solución es justa y posible de cumplir?", "Porque una solución injusta o imposible no dura", "El acuerdo debe ser justo y viable."),
        ex("¿Qué desventaja tiene que siempre ceda la misma persona?", "Puede sentirse injustamente tratada", "El conflicto puede volver más fuerte."),
        ex("¿Una buena solución exige que uno gane todo y el otro pierda todo? Responde sí o no.", "No", "Suele ser un acuerdo con el que ambos quedan conformes."),
    ],
    A=[
        ex("Estrategias: 1) turnarse; 2) pedir mediación; 3) imponerse con fuerza; 4) acordar condiciones; 5) ignorar al otro. ¿Cuántas son estrategias constructivas?", "3", "Turnarse, pedir mediación y acordar condiciones ayudan; imponerse e ignorar no."),
        ex("Dos estudiantes necesitan el mismo diccionario hoy. Uno lo necesita 20 minutos y el otro 15. El recreo tiene 40 minutos. ¿Qué estrategia es más práctica? A) Turnarse uno primero y otro después. B) Pelear por él. C) Que lo use solo el más fuerte.", "A", "Hay tiempo suficiente para que ambos lo usen por turnos."),
        ex("Tomás y Valentina no logran ponerse de acuerdo y ya empezaron a gritarse. ¿Qué estrategia conviene? A) Pedir mediación a un adulto. B) Gritar más fuerte. C) Dejar de hablarse para siempre.", "A", "Un tercero neutral puede ayudarles a conversar."),
    ],
    Z=[
        ex("¿Por qué es importante que los acuerdos sean claros, como «tú ahora y yo después del recreo»?", "Porque se pueden cumplir y revisar", "Las reglas claras evitan nuevos conflictos."),
        ex("¿Por qué, si un conflicto ya tiene golpes o amenazas, no conviene resolverlo solo?", "Porque hay riesgo de daño y se necesita ayuda adulta", "La seguridad y la protección son prioritarias."),
    ],
    D=[
        arith("Un recreo dura 30 minutos. Ema usa la pelota 15 minutos y Luz 15. Si cada una necesita 20 minutos para jugar tranquila, ¿cuántos minutos le faltan a cada una?", "20-15", "Se restan los minutos disponibles a los necesarios."),
        arith("De 25 conflictos registrados, 10 se resolvieron turnándose y 8 con mediación. ¿Cuántos se resolvieron de otra forma?", "25-10-8", "Al total se le restan los dos grupos."),
    ],
    context=[ex("Dos amigas quieren cada una usar el único proyector del curso para su exposición. Acuerdan que una expone primero hoy y la otra mañana, y lo anotan en la agenda del curso. ¿Eligieron una estrategia constructiva?", "Sí", "Se turnan con un acuerdo claro y escrito.")],
    selfcheck=[ex("En Orientación: ¿la mediación es pedir ayuda a una tercera persona neutral?", "Sí", "Ayuda a conversar."), ex("¿Imponerse con fuerza resuelve bien un conflicto?", "No", "El conflicto vuelve."), ex("¿Un acuerdo justo busca que ambos queden conformes?", "Sí", "No necesariamente iguales.")],
    task=T("Lee el conflicto inventado: Mati y Teo quieren el único balón de la sala para el recreo largo (40 minutos). Mati quiere jugar fútbol y Teo quiere jugar con sus amigos otro juego de pelota. Completa una tabla con tres estrategias (turnarse, repartir o acordar condiciones, pedir mediación): qué haría cada uno y qué consecuencia tendría. Elige una y justifica.", "Turnarse: 20 minutos cada uno; ambos juegan. Acordar condiciones: juegan juntos un partido con reglas simples. Mediación: piden ayuda a la inspectora; puede llevar tiempo pero evita discusiones. Elijo turnarse porque es justa y se puede cumplir.", ["describe tres estrategias", "anticipa una consecuencia para cada una", "elige una y justifica", "no cuenta una vivencia propia"], ["tabla escrita"], ["no considerar la consecuencia", "elegir una solución injusta"], "Reconoce la tabla y pregunta cómo comprobarían si el acuerdo se cumple."),
    reinforce="Escribe tres estrategias para resolver un conflicto de un cuento y la consecuencia de cada una.",
    extend="Explica cuándo una mediación es mejor que resolverlo solo.",
)

lesson(
    OA7, 4,
    "Una hoja y un lápiz. El caso de Camila y Joaquín y la pauta de pasos están escritos en los ejercicios.",
    "Aprenderé a aplicar un plan de cinco pasos para resolver un conflicto y a evaluar el resultado. Sirve para resolver problemas de convivencia de forma autónoma y segura.",
    ["Sé identificar intereses.", "Sé escuchar de forma activa y comparar estrategias."],
    [
        "Un plan de cinco pasos ayuda a resolver conflictos con orden. Paso 1: calmarse y elegir un momento tranquilo. Paso 2: escuchar a cada parte y contar los hechos sin culpar. Paso 3: identificar los intereses de cada uno. Paso 4: proponer varias opciones y elegir una que sea justa y posible. Paso 5: acordar cómo se hará, quién hace qué y cuándo se revisará.",
        "Después de aplicar el plan hay que evaluar: ¿el acuerdo se cumplió?, ¿ambos quedaron conformes?, ¿mejoró la convivencia? Si no funcionó, se ajusta el acuerdo o se prueba otra estrategia, y si el problema es grave se pide ayuda a un adulto. Evaluar no es buscar culpables; es aprender para la próxima vez.",
        "Hay situaciones en que no se debe aplicar el plan por tu cuenta: golpes, amenazas, acoso repetido, discriminación o cuando alguien tiene miedo. Ahí, avisa a un adulto de inmediato. Resolver de forma autónoma incluye saber cuándo necesitas ayuda.",
    ],
    [("plan", "serie de pasos ordenados para lograr algo"), ("acuerdo", "decisión tomada entre las partes sobre qué hacer"), ("evaluar", "revisar si algo funcionó y por qué"), ("ajustar", "cambiar un poco un acuerdo para que funcione mejor"), ("acoso", "maltrato repetido hacia una persona")],
    [
        W("Ordenar los pasos", "Camila y Joaquín discuten por los turnos de la mesa grande de la sala de arte. ¿Qué paso va justo después de «escuchar a cada parte y contar los hechos»?", ["Los pasos son: calmarse, escuchar, intereses, opciones y acordar.", "Después de escuchar viene identificar intereses.", "El paso 3 es identificar intereses."], "Identificar los intereses de cada uno"),
        W("Evaluar un acuerdo", "Camila y Joaquín acordaron turnos de 10 minutos y los cumplieron durante una semana. ¿Funcionó el acuerdo?", ["Se cumplió durante la semana.", "Ambos quedaron conformes.", "Se puede mantener."], "Sí, funcionó"),
    ],
    [
        M("Aplicar el plan cuando la otra persona me amenaza.", "Se piensa que hay que resolverlo solo.", "Si hay amenaza o golpes, avisa a un adulto de inmediato."),
        M("Creer que si el acuerdo falla, ya no hay solución.", "Se toma el fallo como un fin.", "Evalúa, ajusta o prueba otra estrategia."),
    ],
    R=[
        ex("¿El primer paso del plan es calmarse y elegir un momento tranquilo? Responde sí o no.", "Sí", "Con calma se puede conversar mejor."),
        ex("¿Qué se hace en el paso 5: acordar quién hace qué y cuándo se revisa, o buscar culpables?", "Acordar quién hace qué y cuándo se revisa", "Cierra con un acuerdo claro."),
        ex("Si hay golpes o amenazas, ¿se aplica el plan por cuenta propia? Responde sí o no.", "No", "Se debe avisar a un adulto."),
    ],
    U=[
        ex("¿Por qué conviene evaluar el acuerdo después?", "Para saber si funcionó y mejorarlo", "Evaluar permite ajustar."),
        ex("¿Qué hacer si un acuerdo no funcionó: abandonarlo o ajustarlo?", "Ajustarlo", "Se cambia un poco para mejorar."),
        ex("¿Por qué el paso 2 pide contar hechos sin culpar?", "Porque culpar provoca defensa", "Los hechos permiten entender sin atacar."),
    ],
    A=[
        ex("Pasos desordenados: A) proponer opciones; B) calmarse; C) escuchar y contar hechos; D) identificar intereses; E) acordar y revisar. ¿Cuál va en cuarto lugar?", "A", "El orden es B, C, D, A, E."),
        arith("Camila y Joaquín acordaron turnos de 10 minutos. Revisaron en la semana: de 5 días cumplieron 4. ¿Cuántos días no cumplieron?", "5-4", "Se restan los días cumplidos a los 5 de la semana."),
        ex("Un compañero amenaza a Dani con golpearlo. ¿Qué debe hacer Dani? A) Aplicar el plan solo. B) Alejarse y avisar a un adulto. C) Amenazarlo de vuelta.", "B", "La seguridad es prioritaria."),
    ],
    Z=[
        ex("¿Por qué evaluar un acuerdo no es lo mismo que buscar culpables?", "Porque busca mejorar y no castigar", "El propósito es aprender para la próxima vez."),
        ex("¿Por qué saber cuándo pedir ayuda es parte de resolver conflictos de forma autónoma?", "Porque decidir pedir ayuda es una decisión responsable", "Ser autónomo es elegir lo mejor, no hacerlo todo solo."),
    ],
    D=[
        arith("El acuerdo duró 4 semanas y cada semana tuvo 5 turnos. ¿Cuántos turnos hubo en total?", "4*5", "Se multiplican las semanas por los turnos."),
        arith("De 20 turnos acordados, se cumplieron 17. ¿Cuántos no se cumplieron?", "20-17", "Se restan los cumplidos al total."),
    ],
    context=[ex("Después de una discusión, Luz y Ema siguieron los cinco pasos y acordaron alternar el uso del único computador por 15 minutos. A los 3 días revisaron y descubrieron que 15 minutos no alcanzaban. Cambiaron a 20 minutos. ¿Usaron bien la evaluación?", "Sí", "Revisaron el acuerdo y lo ajustaron.")],
    selfcheck=[ex("En Orientación: ¿evaluar un acuerdo ayuda a mejorarlo?", "Sí", "Permite ajustar lo que falla."), ex("¿Si hay amenazas se debe avisar a un adulto?", "Sí", "La seguridad es prioridad."), ex("¿El plan tiene cinco pasos?", "Sí", "Calmarse, escuchar, intereses, opciones y acordar.")],
    task=T("Aplica los cinco pasos al conflicto inventado entre Rocío y Beto: ambos quieren organizar el rincón de lectura del curso a su manera. Escribe qué harías en cada paso y cómo evaluarías el acuerdo después de una semana.", "1) Calmarse y elegir un momento tranquilo. 2) Escuchar a cada uno y contar los hechos. 3) Intereses: Rocío quiere silencio; Beto quiere acceso fácil a los libros. 4) Opciones: libros a la altura de todos y una zona silenciosa. 5) Acordar: turnos para ordenarlos cada viernes. Evaluar: revisar el viernes si ambos quedaron conformes.", ["incluye los cinco pasos", "identifica los intereses", "propone cómo evaluar", "no cuenta una vivencia propia"], ["plan escrito"], ["saltarse un paso", "no evaluar"], "Reconoce el plan y pregunta qué ajustaría si no funciona."),
    reinforce="Escribe los cinco pasos con tus palabras y un ejemplo breve para cada uno.",
    extend="Explica por qué evaluar un acuerdo es una forma de mejorar la convivencia del curso.",
)

# ================================================================ OA 08
lesson(
    OA8, 1,
    "Una hoja y un lápiz. El proyecto del curso y la tabla de tareas están escritos en los ejercicios.",
    "Aprenderé a planificar una actividad del curso con objetivo, tareas, responsables y plazos. Sirve para organizarnos y lograr lo que nos propusimos.",
    ["Sé trabajar en equipo.", "Sé decir mis ideas con respeto."],
    [
        "Participar activamente en la comunidad escolar significa aportar ideas y trabajo para el curso, no solo opinar. Una forma es planificar actividades. Planificar es decidir con anticipación qué se quiere lograr y cómo. Una planificación clara tiene un objetivo, tareas, responsables, materiales, un plazo y una forma de revisar si funcionó.",
        "El objetivo debe ser concreto: «Juntar 20 libros para la biblioteca del curso antes del 30 de noviembre». Con él se definen las tareas: hacer un afiche, pasar por los cursos, ordenar los libros y llevar un registro. Cada tarea necesita un responsable y un plazo. Así nadie queda sin trabajo y todos saben qué se espera. También conviene anticipar problemas, como que falte alguien, y pensar qué hacer.",
        "Planificar bien reparte el trabajo de forma justa y evita apuros de última hora. Además, ayuda a evaluar al final: si el objetivo se logró o no, y por qué. Planificar y evaluar son dos mitades del mismo proceso.",
    ],
    [("planificar", "decidir con anticipación qué hacer y cómo"), ("objetivo", "lo que quiero lograr, dicho con claridad"), ("responsable", "persona encargada de una tarea"), ("plazo", "fecha límite para terminar algo"), ("registro", "lista donde se anota lo que se hace")],
    [
        W("Escribir un objetivo claro", "El curso quiere reunir ropa de abrigo para una campaña. ¿Cuál objetivo es claro: «Ayudar mucho» o «Reunir 30 abrigos en dos semanas»?", ["El segundo dice cuánto y para cuándo.", "El primero es vago.", "Un objetivo claro se puede comprobar."], "«Reunir 30 abrigos en dos semanas»"),
        W("Asignar responsables", "Tareas: hacer el afiche, pasar por los cursos, contar los abrigos. Hay tres integrantes: Ema, Luz y Teo. ¿Qué conviene hacer?", ["Cada tarea necesita un responsable.", "Se reparten entre tres personas.", "Así se reparte el trabajo."], "Asignar una tarea a cada integrante"),
    ],
    [
        M("Empezar a trabajar sin definir quién hace qué.", "Se piensa que se organizarán sobre la marcha.", "Anota tareas, responsables y plazos antes de empezar."),
        M("Poner un objetivo muy grande sin plazo.", "Se cree que más grande es mejor.", "Escribe un objetivo posible y con fecha."),
    ],
    R=[
        ex("Decidir con anticipación qué hacer y cómo, ¿es planificar o improvisar?", "Planificar", "Planificar es decidir antes de actuar."),
        ex("¿Una tarea necesita un responsable y un plazo? Responde sí o no.", "Sí", "Así se sabe quién hace qué y cuándo."),
        ex("El objetivo «Juntar 20 libros antes del 30 de noviembre», ¿es claro? Responde sí o no.", "Sí", "Dice cuánto y para cuándo."),
    ],
    U=[
        ex("¿Por qué un objetivo con cantidad y fecha se puede comprobar mejor?", "Porque se puede saber si se logró", "Con números y plazo se mide el resultado."),
        ex("¿Por qué es útil pensar problemas posibles al planificar?", "Para tener un plan si algo falla", "Anticipar evita que la actividad se detenga."),
        ex("¿Por qué repartir el trabajo entre todos es más justo?", "Porque nadie queda con todo ni sin nada", "Cada uno aporta una parte."),
    ],
    A=[
        ex("Planifica: tareas A) hacer afiche, B) pedir permiso a dirección, C) juntar libros, D) registrar. Cuatro estudiantes asumen una tarea cada uno. ¿Cuántas tareas tiene cada estudiante?", "1", "Con cuatro tareas y cuatro personas, cada una asume una."),
        arith("Un curso quiere juntar 60 libros en 3 semanas, la misma cantidad cada semana. ¿Cuántos libros por semana?", "60//3", "Se divide el total entre las semanas."),
        ex("Objetivos: A) «Ser solidarios»; B) «Juntar 25 abrigos para el 15 de junio»; C) «Hacer algo». ¿Cuál es claro?", "B", "Es el único con cantidad y fecha."),
    ],
    Z=[
        ex("¿Por qué una actividad sin responsables puede quedar a medias?", "Porque nadie se hace cargo", "Si todos pueden hacerlo, nadie lo hace."),
        ex("¿Por qué conviene anotar el plan por escrito y no solo recordarlo?", "Porque todos pueden revisarlo", "Un plan escrito evita olvidos."),
    ],
    D=[
        arith("Para una campaña, 24 estudiantes se reparten en equipos de 4. ¿Cuántos equipos hay?", "24//4", "Se divide el total entre los integrantes por equipo."),
        arith("Un curso ya juntó 18 de los 30 abrigos de su meta. ¿Cuántos faltan?", "30-18", "Se resta lo juntado a la meta."),
    ],
    context=[ex("El curso decide organizar una feria de libros usados. Definen: objetivo (juntar 40 libros en 2 semanas), tareas (afiche, recolección, registro), responsables y plazos. ¿Tienen un buen plan?", "Sí", "Incluye objetivo claro, tareas, responsables y plazos.")],
    selfcheck=[ex("En Orientación: ¿planificar es decidir con anticipación?", "Sí", "Permite organizarse con anticipación."), ex("¿Un objetivo vago sirve igual que uno claro?", "No", "No se puede comprobar."), ex("¿Cada tarea necesita un responsable?", "Sí", "Para saber quién la hace.")],
    task=T("Planifica una actividad inventada para tu curso: una campaña para juntar 30 libros para la biblioteca. Escribe el objetivo con cantidad y fecha, cuatro tareas con responsables y plazos, y un problema posible con su solución.", "Objetivo: juntar 30 libros antes del 20 de junio. Tareas: afiche (Ema, lunes), recolección (Luz y Teo, hasta el jueves), registro (Mati, viernes), entrega a la bibliotecaria (Camila, lunes siguiente). Problema posible: poca recolección; solución: pasar por otros cursos.", ["objetivo con cantidad y fecha", "cuatro tareas con responsable y plazo", "un problema posible con solución", "no cuenta una vivencia propia"], ["tabla escrita"], ["tareas sin responsable", "objetivo sin fecha"], "Reconoce el plan y pregunta cómo evaluarían si se cumplió."),
    reinforce="Planifica con tabla (tarea, responsable, plazo) una actividad pequeña del curso.",
    extend="Explica por qué una buena planificación hace que el trabajo en equipo sea más justo.",
)

lesson(
    OA8, 2,
    "Una hoja y un lápiz. Las tablas de acuerdos y los resultados están escritos en los ejercicios.",
    "Aprenderé a evaluar actividades y el cumplimiento de los acuerdos del curso con indicadores. Sirve para saber qué mejorar y mantener lo que funciona.",
    ["Sé planificar una actividad con objetivo y plazo.", "Sé decir mi opinión con respeto."],
    [
        "Evaluar es revisar si se logró lo que se quería y por qué. Para evaluar una actividad del curso, se compara lo planificado con lo que ocurrió. Un indicador es una señal que se puede medir: por ejemplo, cuántos libros se juntaron frente a la meta, cuántos asistieron o cuántas tareas se cumplieron a tiempo. Con indicadores, la evaluación no depende de opiniones sueltas.",
        "También se evalúa el cumplimiento de los acuerdos del curso. Un acuerdo es una decisión tomada entre todos, como «hablar bajo en el trabajo grupal». Se puede revisar cada semana con una tabla: cuántas veces se cumplió, cuántas no y qué ayudó o dificultó. Es mejor hablar de hechos que de personas, y terminar con propuestas de mejora.",
        "Evaluar sirve para aprender, no para castigar. Una buena evaluación reconoce lo logrado, identifica lo que falta y propone cambios concretos. Así el curso mejora y todos sienten que su participación importa.",
    ],
    [("evaluar", "revisar si se logró lo planificado y por qué"), ("indicador", "señal que se puede medir para saber si algo funciona"), ("meta", "cantidad o resultado que se quería lograr"), ("acuerdo de curso", "decisión tomada entre todos"), ("propuesta de mejora", "cambio concreto para hacerlo mejor")],
    [
        W("Calcular un indicador", "La meta era juntar 40 libros y se juntaron 34. ¿Cuántos faltaron?", ["Se resta lo juntado a la meta.", "40 − 34 = 6.", "Faltaron 6 libros."], "6 libros"),
        W("Hacer una propuesta de mejora", "En 5 semanas, el curso cumplió el acuerdo de hablar bajo solo en 2. ¿Qué propuesta de mejora es concreta: «Portarse mejor» o «Poner un recordatorio visible y revisar cada viernes»?", ["La primera es vaga.", "La segunda es concreta y revisable.", "Una mejora debe poder cumplirse."], "«Poner un recordatorio visible y revisar cada viernes»"),
    ],
    [
        M("Evaluar solo con opiniones como 'estuvo bien' o 'estuvo mal'.", "Se piensa que la opinión basta.", "Usa indicadores como cantidades, fechas y asistencia."),
        M("Usar la evaluación para señalar culpables.", "Se confunde evaluar con castigar.", "Habla de hechos y propone mejoras."),
    ],
    R=[
        ex("Una señal que se puede medir para saber si algo funciona, ¿es un indicador o una opinión?", "Un indicador", "Se puede contar o medir."),
        ex("¿Evaluar sirve para aprender y mejorar? Responde sí o no.", "Sí", "Ese es su propósito."),
        ex("«Poner un recordatorio visible» es una propuesta de mejora, ¿concreta o vaga?", "Concreta", "Dice qué hacer y se puede cumplir."),
    ],
    U=[
        ex("¿Por qué conviene usar indicadores al evaluar?", "Porque dan datos que se pueden comprobar", "No dependen de opiniones sueltas."),
        ex("¿Por qué conviene hablar de hechos y no de personas al evaluar?", "Porque así nadie se siente atacado", "Los hechos permiten mejorar sin culpar."),
        ex("¿Qué debe incluir una buena evaluación además de lo logrado: lo que falta o solo felicitaciones?", "Lo que falta y propuestas", "Así se puede mejorar después."),
    ],
    A=[
        ex("Resultados: 1) meta de 50 libros, se juntaron 42; 2) meta de 5 tareas, se cumplieron 5; 3) meta de 30 asistentes, llegaron 18. ¿En cuántos se alcanzó la meta?", "1", "Solo en el 2 se alcanzó la meta completa."),
        arith("Un curso se propuso 20 puntos de convivencia por mes y logró 14. ¿Cuántos puntos faltaron?", "20-14", "Se resta lo logrado a la meta."),
        ex("El acuerdo era 'no interrumpir'. Se cumplió 3 de 5 clases. ¿Qué propuesta es más concreta? A) «Mejoremos» B) «Usar una señal de mano para pedir la palabra» C) «Que se porten bien»", "B", "Es una acción concreta que se puede revisar."),
    ],
    Z=[
        ex("La meta era juntar 40 libros y se juntaron 46. ¿Se alcanzó la meta?", "Sí", "Se superó la cantidad propuesta."),
        ex("¿Por qué conviene evaluar el acuerdo cada semana y no solo al final del año?", "Porque se puede corregir a tiempo", "Revisar seguido evita que los problemas crezcan."),
    ],
    D=[
        arith("En 4 semanas, el curso cumplió el acuerdo 3, 4, 2 y 5 veces. ¿Cuántas veces lo cumplió en total?", "3+4+2+5", "Se suman las veces de cada semana."),
        arith("Un curso de 32 estudiantes tuvo 28 asistentes a una actividad. ¿Cuántos no asistieron?", "32-28", "Se restan los asistentes al total."),
    ],
    context=[ex("El curso revisó su acuerdo de puntualidad: en la semana 1 llegaron a tiempo 20 de 30 estudiantes y en la semana 2, 26 de 30. ¿Mejoró el indicador?", "Sí", "Pasó de 20 a 26 estudiantes puntuales.")],
    selfcheck=[ex("En Orientación: ¿un indicador se puede medir?", "Sí", "Por eso sirve para evaluar."), ex("¿Evaluar es lo mismo que castigar?", "No", "Evaluar busca mejorar."), ex("¿Una propuesta de mejora debe ser concreta?", "Sí", "Así se puede cumplir.")],
    task=T("Evalúa esta actividad inventada: el curso quería juntar 50 libros en 3 semanas y juntó 43; de 6 tareas, se cumplieron 5; asistieron 24 de 30 estudiantes a la entrega. Escribe tres indicadores con su resultado, qué se logró, qué faltó y una propuesta de mejora concreta.", "Indicadores: libros 43 de 50 (faltaron 7); tareas 5 de 6; asistencia 24 de 30. Logrado: casi toda la meta y la mayoría de las tareas. Faltó: 7 libros y 6 asistentes. Mejora: avisar con una semana de anticipación y pasar por otros cursos.", ["tres indicadores con resultado", "dice lo logrado y lo que faltó", "una propuesta concreta", "no cuenta una vivencia propia"], ["tabla escrita"], ["evaluar solo con opinión", "culpar a personas"], "Reconoce la tabla y pregunta cómo revisaría la mejora."),
    reinforce="Escribe tres indicadores posibles para evaluar una actividad del curso.",
    extend="Explica por qué evaluar con indicadores es más justo que opinar sin datos.",
)

lesson(
    OA8, 3,
    "Una hoja y un lápiz. Los roles, las tareas y las situaciones del curso están escritos en los ejercicios.",
    "Aprenderé a asumir y cumplir responsabilidades y a repartir roles sin discriminar. Sirve para que todos participen y sientan que su aporte vale.",
    ["Sé planificar una actividad.", "Sé que todas las personas tienen los mismos derechos."],
    [
        "Una responsabilidad es una tarea que asumes y cumples, porque otros cuentan contigo. En el curso hay muchas: ser encargado del aseo, del diario mural, de la lista o de las comunicaciones. Asumir una responsabilidad significa decir qué harás, cumplirlo a tiempo y avisar con anticipación si no puedes. Cumplir genera confianza.",
        "Los roles se deben repartir sin discriminar. Discriminar es excluir o asignar tareas por características como el género, la etnia, la religión o la nacionalidad. Por ejemplo, no es justo que solo las niñas hagan el aseo o solo los niños muevan las mesas. Los roles se pueden repartir según intereses, habilidades y turnos, y rotarlos para que todos prueben distintas tareas. Todas las tareas valen.",
        "Respetar los derechos de los demás incluye escuchar quién quiere asumir un rol y dar a todos la oportunidad. Si un compañero tiene una dificultad, se pueden buscar ajustes. Si alguien no cumple, primero se conversa: ¿qué pasó?, ¿qué necesita?, ¿cómo se puede apoyar?, y luego se acuerda cómo compensar.",
    ],
    [("responsabilidad", "tarea que asumo y cumplo porque otros cuentan conmigo"), ("rol", "función que cumple una persona en un grupo"), ("rotar", "cambiar quién hace cada tarea por turnos"), ("discriminar", "excluir o tratar distinto sin una razón justa"), ("compensar", "reparar con una acción lo que no se cumplió")],
    [
        W("Detectar discriminación en roles", "El curso asigna el aseo solo a las niñas y mover mesas solo a los niños. ¿Es justo?", ["Se reparte por género.", "Todas las personas pueden hacer ambas tareas.", "Es discriminación."], "No, es discriminación por género"),
        W("Repartir roles de forma justa", "Hay 4 tareas y 4 estudiantes. ¿Qué forma es más justa: rotar las tareas cada semana o que siempre las haga la misma persona?", ["Rotar permite que todos prueben.", "Siempre la misma persona puede ser injusto.", "La rotación es más justa."], "Rotar las tareas cada semana"),
    ],
    [
        M("Creer que hay tareas 'de niñas' y 'de niños'.", "Se repiten estereotipos sin pensarlos.", "Reparte por intereses, habilidades y turnos."),
        M("Aceptar un rol y no avisar cuando no puedo.", "Se teme decepcionar.", "Avisa con anticipación para que otro pueda ayudar."),
    ],
    R=[
        ex("Una tarea que asumes y cumples porque otros cuentan contigo, ¿es una responsabilidad o un castigo?", "Una responsabilidad", "Es un compromiso con el grupo."),
        ex("Asignar tareas solo por el género, ¿es discriminar? Responde sí o no.", "Sí", "Se excluye por una característica."),
        ex("Rotar los roles por turnos, ¿es una forma justa de repartir? Responde sí o no.", "Sí", "Todos prueban distintas tareas."),
    ],
    U=[
        ex("¿Por qué es importante avisar con anticipación si no puedes cumplir una tarea?", "Para que otro pueda ayudar a tiempo", "Evita que la actividad se detenga."),
        ex("¿Por qué conviene preguntar quién quiere asumir cada rol?", "Porque se respetan intereses y habilidades", "Todos participan con gusto."),
        ex("Si alguien no cumplió, ¿qué conviene hacer primero: conversar o castigar?", "Conversar", "Se entiende qué pasó y cómo apoyar."),
    ],
    A=[
        ex("Reparto: 1) «El aseo es de las niñas»; 2) «El aseo lo hacemos por turnos»; 3) «Los niños cargan las mesas»; 4) «Cargamos las mesas quienes queramos y rotamos». ¿Cuántos repartos discriminan?", "2", "Los números 1 y 3 asignan por género."),
        ex("Un estudiante en silla de ruedas quiere participar en el aseo. ¿Qué es lo justo? A) Excluirlo. B) Buscar una tarea adecuada y ajustar la forma. C) Darle solo tareas pequeñas siempre.", "B", "Se respetan sus derechos con ajustes."),
        ex("Ema aceptó traer el afiche para el miércoles pero no podrá. ¿Qué debe hacer? A) Avisar con anticipación. B) No decir nada. C) Dar excusas el miércoles.", "A", "Permite que otro ayude a tiempo."),
    ],
    Z=[
        ex("¿Por qué «las tareas de aseo son para quien se porte mal» no es un reparto justo?", "Porque usa una tarea como castigo y la desvaloriza", "Todas las tareas valen y deben compartirse."),
        ex("Un rol se rota cada semana entre 5 estudiantes, uno distinto cada semana. ¿Cuántas semanas dura un ciclo completo hasta que todos hayan tenido el rol una vez?", "5", "Hay un estudiante por semana y son cinco estudiantes."),
    ],
    D=[
        arith("El curso tiene 30 estudiantes y 6 roles. Si cada rol lo asumen 5 personas, ¿cuántos estudiantes tienen rol?", "6*5", "Se multiplican los roles por las personas de cada uno."),
        arith("Un curso de 32 estudiantes reparte las tareas de aseo en equipos de 4. ¿Cuántos equipos hay?", "32//4", "Se divide el total entre el tamaño de cada equipo."),
    ],
    context=[ex("Para el aseo semanal, el curso hace una tabla donde cada semana un equipo distinto asume cada tarea, sin importar si son niños o niñas. ¿Repartieron los roles sin discriminar?", "Sí", "Rotan los roles y no usan el género.")],
    selfcheck=[ex("En Orientación: ¿asumir una responsabilidad es cumplir lo que me comprometí?", "Sí", "Otros cuentan conmigo."), ex("¿Hay tareas solo para niñas o solo para niños?", "No", "Todos pueden hacerlas."), ex("¿Rotar roles ayuda a que todos participen?", "Sí", "Da oportunidades a todos.")],
    task=T("Lee el caso inventado: el curso debe repartir seis roles (diario mural, aseo, lista de asistencia, materiales, comunicaciones y cuidado de las plantas). Hay 6 estudiantes en un grupo. Arma una tabla que reparta los roles sin discriminar y explica cómo rotarán. Escribe además qué harán si alguien no puede cumplir su rol.", "Tabla: Ema diario mural, Luz aseo, Teo lista, Mati materiales, Camila comunicaciones, Dani plantas; rotan cada semana en el sentido de la lista. Si alguien no puede cumplir, avisa con anticipación y busca apoyo o intercambia el rol.", ["reparte los seis roles", "explica cómo rotan", "incluye qué hacer si alguien no cumple", "no discrimina por género ni otra característica"], ["tabla escrita"], ["asignar por género", "no incluir plan si alguien falla"], "Reconoce la tabla y pregunta cómo revisarían que se cumple."),
    reinforce="Escribe una tabla de turnos de aseo para cuatro compañeros por cuatro semanas sin discriminar.",
    extend="Explica por qué todas las tareas del curso merecen el mismo respeto.",
)

lesson(
    OA8, 4,
    "Una hoja y un lápiz. Las listas de candidatos y los resultados de votación están escritos en los ejercicios. Todos los nombres son inventados.",
    "Aprenderé cómo funcionan las elecciones de curso: candidaturas, voto, conteo y aceptar los resultados. Sirve para participar en decisiones democráticas.",
    ["Sé que todas las personas tienen derecho a opinar.", "Sé planificar y evaluar."],
    [
        "Una elección de curso sirve para elegir a quienes representarán al curso, como la directiva. Es una forma de decisión democrática: todos los integrantes tienen derecho a votar y cada voto vale lo mismo. Las etapas son: presentar candidaturas, escuchar las propuestas, votar de forma secreta, contar los votos frente al curso y comunicar el resultado.",
        "En el conteo, gana quien obtiene más votos, es decir, la mayoría simple. Un voto en blanco es el que no marca a nadie y un voto nulo es el que está mal marcado; ninguno se suma a un candidato. Para evitar desacuerdos, se cuenta en voz alta y se anota en la pizarra. Si hay empate, se acuerda antes cómo desempatar, por ejemplo, con una nueva votación entre los empatados.",
        "Aceptar los resultados es parte de la democracia. Quien no ganó puede seguir participando y apoyar al curso. Quien ganó debe representar a todos, incluso a quienes no lo votaron. Respetar el resultado y a las personas elegidas fortalece la convivencia.",
    ],
    [("elección", "proceso en que el curso elige a sus representantes con votos"), ("candidatura", "persona que se presenta para ser elegida"), ("mayoría simple", "ganar con más votos que cada otra opción"), ("voto blanco", "voto que no marca a ninguna persona"), ("voto nulo", "voto mal marcado que no se cuenta")],
    [
        W("Contar los votos", "En una elección de presidenta del curso hubo 30 votos válidos: Ema 12, Luz 10 y Dani 8. ¿Quién ganó y por cuántos votos le ganó a la segunda?", ["La que tiene más votos gana: Ema con 12.", "La segunda es Luz con 10.", "12 − 10 = 2."], "Ganó Ema por 2 votos"),
        W("Aceptar los resultados", "Luz quería ganar pero quedó segunda. ¿Qué actitud democrática es la adecuada: aceptar el resultado y colaborar o desconocer la elección?", ["Los votos decidieron.", "Luz puede seguir participando.", "Aceptar los resultados fortalece la convivencia."], "Aceptar el resultado y colaborar"),
    ],
    [
        M("Pensar que quien gana manda y no tiene que escuchar a los demás.", "Se confunde ganar con tener poder absoluto.", "Quien gana representa a todo el curso, incluso a quienes no lo votaron."),
        M("Creer que si mi candidata pierde, la elección no vale.", "Se mide el resultado por el deseo propio.", "Respeta el resultado: los votos decidieron."),
    ],
    R=[
        ex("¿Gana quien obtiene más votos en una elección con mayoría simple? Responde sí o no.", "Sí", "Esa es la regla de la mayoría simple."),
        ex("¿El voto debe ser secreto o debe decirse en voz alta?", "Secreto", "Protege la libertad de elegir."),
        ex("Un voto que no marca a nadie, ¿es voto blanco o nulo?", "Blanco", "Un voto nulo es el que está mal marcado."),
    ],
    U=[
        ex("¿Por qué cada voto vale lo mismo en una elección democrática?", "Porque todos tienen los mismos derechos", "Nadie vale más que otro."),
        ex("¿Por qué es importante escuchar las propuestas antes de votar?", "Para elegir con información", "Se decide mejor si se conocen las ideas."),
        ex("Si hay empate, ¿qué conviene acordar antes: cómo desempatar o dejar que decidan los más fuertes?", "Cómo desempatar", "Una regla acordada evita conflictos."),
    ],
    A=[
        arith("Resultados de 32 votos: Teo 14, Mati 11, blancos 3 y nulos 4. ¿Cuántos votos fueron para candidatos?", "14+11", "Los blancos y nulos no se suman a ningún candidato."),
        ex("Con esos resultados (Teo 14 y Mati 11), ¿quién ganó?", "Teo", "Obtuvo más votos que Mati."),
        ex("Una candidata dice: «Si no gano, no participaré en nada». ¿Qué opinión es democrática? A) «Aceptaré el resultado y seguiré ayudando». B) «Las elecciones no valen». C) «Pediré repetirla».", "A", "Respeta el resultado y sigue aportando."),
    ],
    Z=[
        ex("Dos candidatos tienen 13 votos cada uno en una elección. ¿Quién gana?", "Nadie todavía", "Hay empate y se debe desempatar con la regla acordada."),
        ex("¿Por qué la persona elegida debe representar también a quienes no la votaron?", "Porque fue elegida por todo el curso", "Representa al curso completo."),
    ],
    D=[
        arith("En un curso de 36 estudiantes votaron 33. ¿Cuántos no votaron?", "36-33", "Se restan los que votaron al total."),
        arith("Tres candidatos obtuvieron 9, 14 y 7 votos. ¿Cuántos votos válidos hubo en total?", "9+14+7", "Se suman los votos de los tres candidatos."),
    ],
    context=[ex("En la elección de directiva, el curso presentó cuatro candidaturas, escuchó propuestas, votó en secreto y contó los votos en voz alta. Al terminar, la candidata con menos votos felicitó a la ganadora. ¿Siguieron un proceso democrático?", "Sí", "Hubo candidaturas, voto secreto, conteo público y aceptación del resultado.")],
    selfcheck=[ex("En Orientación: ¿en una elección democrática cada voto vale lo mismo?", "Sí", "Todos tienen los mismos derechos."), ex("¿Hay que aceptar los resultados?", "Sí", "Es parte de la democracia."), ex("¿El voto debe ser secreto?", "Sí", "Protege la libertad.")],
    task=T("Simula una elección inventada de encargado de biblioteca del curso con tres candidatos: Luz, Dani y Tomás. Escribe un afiche breve con dos propuestas de Luz, una lista de 15 votos (Luz 6, Dani 5, Tomás 3, blanco 1), el conteo con el resultado y una frase de aceptación del resultado de quien perdió.", "Propuestas de Luz: ordenar los libros por tema y hacer un registro de préstamos. Conteo: Luz 6, Dani 5, Tomás 3, blanco 1; total 15. Gana Luz. Frase de Dani: «Acepto el resultado y ofrezco ayudar a ordenar los libros».", ["escribe dos propuestas", "cuenta bien los votos y declara ganador", "escribe una frase de aceptación", "no cuenta una vivencia propia"], ["afiche y conteo escritos"], ["contar mal", "no aceptar el resultado"], "Reconoce el conteo y pregunta qué harían si hubiera empate."),
    reinforce="Escribe los cinco pasos de una elección de curso en orden.",
    extend="Explica por qué el voto secreto protege la libertad de elegir.",
)

lesson(
    OA8, 5,
    "Una hoja y un lápiz. El problema del curso, los acuerdos y la votación están escritos en los ejercicios.",
    "Aprenderé a establecer acuerdos con diálogo y decisiones democráticas para resolver problemas cotidianos del curso. Sirve para organizarnos y cumplir lo que decidimos.",
    ["Sé planificar, evaluar y votar.", "Sé escuchar y respetar opiniones."],
    [
        "Un problema cotidiano del curso, como el desorden del rincón de lectura o el uso del celular, se resuelve mejor cuando todos participan. El primer paso es dialogar: cada persona expone su opinión con respeto y se escucha sin interrumpir. Luego se proponen alternativas, se analiza cuál atiende mejor a todos y se decide. Si hay consenso, es decir, acuerdo de todos, se anota. Si no, se vota y se aplica la mayoría simple.",
        "Un buen acuerdo es claro, posible de cumplir, justo para todos y tiene un plazo de revisión. Por ejemplo: «El rincón de lectura se ordena cada viernes por un equipo distinto; lo revisaremos en tres semanas». Se escribe en un lugar visible, se asignan responsables y se programa su evaluación. Un acuerdo sin responsables ni revisión se olvida con facilidad.",
        "También hay límites: una decisión de la mayoría no puede violar derechos de nadie ni las normas del colegio. Y quien perdió la votación tiene derecho a seguir opinando y a proponer mejoras. La democracia es un compromiso con el diálogo y con los acuerdos.",
    ],
    [("diálogo", "conversación en que se escucha y se habla por turnos"), ("consenso", "acuerdo en el que todos están de acuerdo"), ("mayoría simple", "ganar con más votos que las otras opciones"), ("acuerdo", "decisión que se escribe y se cumple"), ("democrático", "que se decide entre todos respetando derechos")],
    [
        W("Redactar un acuerdo", "El curso decide cuidar el rincón de lectura. ¿Qué acuerdo es mejor: «Cuidar el rincón» o «Cada viernes un equipo distinto ordena el rincón; lo revisaremos en tres semanas»?", ["El segundo dice quién, cuándo y cuándo revisar.", "El primero es vago.", "Un acuerdo claro se puede cumplir."], "«Cada viernes un equipo distinto ordena el rincón; lo revisaremos en tres semanas»"),
        W("Decidir con votación", "El curso vota entre A, B y C: A 11 votos, B 9 votos y C 6 votos. ¿Qué opción se aplica?", ["Se aplica la mayoría simple.", "La que tiene más votos es A con 11.", "A gana."], "La opción A"),
    ],
    [
        M("Pensar que la mayoría siempre puede decidir cualquier cosa.", "Se olvida que hay derechos y normas.", "Una decisión no puede violar derechos de nadie."),
        M("Hacer un acuerdo sin responsables ni revisión.", "Se cree que todos lo recordarán.", "Anota quién hace qué y cuándo se revisa."),
    ],
    R=[
        ex("Un acuerdo en el que todos están de acuerdo, ¿es consenso o mayoría simple?", "Consenso", "Todos aceptan la decisión."),
        ex("Si no hay consenso, ¿se puede votar? Responde sí o no.", "Sí", "La votación es una forma democrática de decidir."),
        ex("¿Un buen acuerdo debe ser claro y tener un plazo de revisión? Responde sí o no.", "Sí", "Así se puede cumplir y evaluar."),
    ],
    U=[
        ex("¿Por qué conviene anotar los acuerdos y dejarlos visibles?", "Para que todos los recuerden y los cumplan", "Lo escrito se puede revisar."),
        ex("¿Por qué una decisión de la mayoría no puede violar los derechos de nadie?", "Porque todos tienen los mismos derechos", "El voto no autoriza a dañar a una minoría."),
        ex("¿Quien perdió una votación puede seguir proponiendo mejoras? Responde sí o no.", "Sí", "Participar no termina con la votación."),
    ],
    A=[
        arith("Votación entre dos opciones: 17 a favor del horario A y 13 a favor del horario B. ¿Cuántos votos de diferencia hubo?", "17-13", "Se resta el menor al mayor."),
        ex("Un curso propone esta norma: «Quien hable fuerte será expulsado». ¿Se puede aprobar por mayoría? A) Sí, si todos votan. B) No, no se pueden vulnerar derechos ni normas del colegio. C) Sí, porque es rápida.", "B", "La mayoría no puede vulnerar derechos."),
        ex("Acuerdo A: «Ser más ordenados». Acuerdo B: «Dejar los materiales en la caja azul a las 12:00; revisaremos en dos semanas». ¿Cuál es más claro?", "B", "Dice qué, cuándo y cuándo se revisa."),
    ],
    Z=[
        ex("¿Por qué conviene dialogar antes de votar?", "Para conocer todas las opiniones y encontrar mejores opciones", "El diálogo mejora la decisión."),
        ex("Después de acordar que el equipo de turno ordenaría el rincón, nadie lo revisó y el acuerdo se olvidó. ¿Qué faltó?", "Una revisión programada", "Sin revisión el acuerdo se olvida."),
    ],
    D=[
        arith("Una votación entre tres opciones tuvo 12, 8 y 10 votos. ¿Cuántos votos fueron en total?", "12+8+10", "Se suman los votos de las tres opciones."),
        arith("El curso tiene 30 estudiantes y 24 votaron a favor de una propuesta. ¿Cuántos no votaron a favor?", "30-24", "Se restan los votos a favor al total."),
    ],
    context=[ex("El curso tiene desorden en el rincón de lectura. Dialogan, proponen tres soluciones, votan, escriben el acuerdo con responsables y lo pegan en la sala. A las tres semanas lo evalúan. ¿Usaron un proceso democrático completo?", "Sí", "Dialogaron, votaron, anotaron, asignaron y evaluaron.")],
    selfcheck=[ex("En Orientación: ¿el diálogo es parte de una decisión democrática?", "Sí", "Se escuchan todas las opiniones."), ex("¿Un acuerdo debe tener responsables y revisión?", "Sí", "Así se cumple."), ex("¿La mayoría puede violar derechos de otros?", "No", "Los derechos son para todos.")],
    task=T("El curso inventado tiene un problema: el patio queda con papeles después del recreo. Escribe: dos propuestas distintas, cómo decidirían (diálogo y votación), el acuerdo final con responsables, plazo y fecha de revisión, y una frase para quien perdió la votación.", "Propuestas: A) un equipo recoge cada día; B) un recipiente en cada banca. Decidir: dialogar y votar. Acuerdo: el equipo de turno recoge los papeles al final del recreo; se rota cada semana; revisaremos en dos semanas. Frase: «Tu idea también nos sirve; ¿puedes ayudarnos con el recipiente?»", ["dos propuestas", "cómo se decide", "acuerdo con responsables, plazo y revisión", "frase respetuosa", "no cuenta una vivencia propia"], ["texto escrito o dramatizado"], ["acuerdo sin revisión", "frase que excluye"], "Reconoce el acuerdo y pregunta cómo comprobarían que funciona."),
    reinforce="Redacta un acuerdo con quién, qué, cuándo y revisión para un problema del curso.",
    extend="Explica por qué el diálogo antes de votar mejora la decisión.",
)
