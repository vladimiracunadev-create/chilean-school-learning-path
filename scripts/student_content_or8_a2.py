"""Cuaderno del estudiante, 8.º básico Orientación: OA 03 (prevención de riesgos y búsqueda de ayuda) y OA 04 (bienestar cotidiano y seguridad digital)."""
from __future__ import annotations

from student_content_or8_a import M, T, W, lesson
from student_lessons import arith, ex

OA3, OA4 = "OR08 OA 03", "OR08 OA 04"

# ================================================================ OA 03
lesson(
    OA3, 1,
    "Una hoja y un lápiz. El caso de Joaquín, un estudiante inventado, y todas las situaciones están escritos en los ejercicios. No necesitas contar nada propio.",
    "Aprenderé a identificar situaciones que exponen a adolescentes al consumo de sustancias nocivas, a conductas sexuales riesgosas y a conductas violentas, y a distinguir factores de riesgo y de protección. Sirve para reconocer el peligro a tiempo.",
    ["Sé que tengo derecho a decir «no».", "Sé que pedir ayuda a una persona adulta de confianza es una forma de cuidarme."],
    [
        "Una situación de riesgo es aquella en que puedes sufrir un daño o causarlo. En la adolescencia, tres tipos son frecuentes. El consumo de sustancias nocivas incluye alcohol, tabaco, vapeadores, drogas ilegales y medicamentos usados sin indicación médica. Las conductas sexuales riesgosas son las que ocurren sin consentimiento, sin información, bajo presión o bajo los efectos del alcohol. Las conductas violentas son peleas, amenazas, acoso y violencia en el pololeo.",
        "Un factor de riesgo es algo que aumenta la probabilidad de un daño, como una fiesta sin adultos donde se ofrece alcohol, la presión del grupo o el aislamiento. Un factor de protección es algo que la disminuye: tener una persona adulta de confianza, saber decir «no», mantener actividades que te gustan y contar con amistades que te respetan. Reconocer ambos te ayuda a decidir.",
        "Identificar una situación de riesgo no significa sentir miedo todo el tiempo, sino prestar atención a las señales: ofrecimientos de sustancias, presiones, lugares sin supervisión, personas que te hacen sentir incómodo. Con las señales a la vista, puedes preparar estrategias, como la comunicación asertiva y la ayuda de personas de confianza dentro o fuera del colegio.",
    ],
    [("situación de riesgo", "momento en que alguien puede sufrir o causar un daño"), ("sustancia nociva", "sustancia que daña el organismo, como el alcohol o el tabaco"), ("factor de riesgo", "algo que aumenta la probabilidad de un daño"), ("factor de protección", "algo que disminuye la probabilidad de un daño"), ("presión de grupo", "empuje de un grupo para que alguien haga lo que no quiere")],
    [
        W("Clasificar una situación", "Invitan a Joaquín a una fiesta sin adultos donde algunos beberán alcohol y otros usarán vapeadores. ¿Es una situación de riesgo? ¿De qué tipo?", ["Hay alcohol y vapeadores, que son sustancias nocivas.", "No hay adultos que supervisen.", "Es una situación de riesgo por consumo de sustancias."], "Sí, de consumo de sustancias nocivas"),
        W("Factores de riesgo y de protección", "Joaquín piensa: «Si voy, mi amigo Teo estará allí y le puedo decir que me retiro si algo pasa; además una persona adulta de mi familia sabe dónde estaré». ¿Qué factor de protección aparece?", ["Teo es una amistad que lo respeta.", "Una persona adulta de su familia sabe dónde estará.", "Ambos son factores de protección."], "Tener una persona adulta informada y una amistad que lo respeta"),
    ],
    [
        M("Creer que solo hay riesgo en las drogas ilegales.", "Se olvida que el alcohol, el tabaco y los vapeadores también son sustancias nocivas.", "Incluye todas las sustancias nocivas, legales o no."),
        M("Pensar que reconocer un riesgo es exagerar.", "Se confunde prudencia con miedo.", "Observar las señales permite prepararse y decidir mejor."),
    ],
    R=[
        ex("El alcohol, ¿es una sustancia nociva para el organismo, sí o no?", "Sí", "Daña el organismo y afecta el juicio y la coordinación."),
        ex("Una pelea a golpes en el patio, ¿es una conducta violenta o una conducta de cuidado?", "Una conducta violenta", "Hay agresión física."),
        ex("Tener una persona adulta de confianza, ¿es un factor de riesgo o de protección?", "De protección", "Disminuye la probabilidad de un daño."),
    ],
    U=[
        ex("Marca el factor de riesgo: A) Una fiesta sin adultos donde ofrecen alcohol. B) Una salida a una plaza con la familia.", "A", "Sin supervisión y con ofrecimiento de sustancias, aumenta la probabilidad de daño."),
        ex("¿Por qué el alcohol puede aumentar una conducta sexual riesgosa?", "Porque afecta el juicio y la capacidad de decidir", "Bajo sus efectos es más difícil decir no o respetar un no."),
        ex("Un vapeador, ¿es solo un juguete o una sustancia que puede contener nicotina?", "Puede contener nicotina", "Muchos vapeadores contienen nicotina, que genera adicción."),
    ],
    A=[
        ex("Joaquín anotó: 1) «alguien ofrece cigarrillos electrónicos»; 2) «una amiga estudia conmigo»; 3) «amenazan a un compañero»; 4) «presionan a alguien para tener relaciones sexuales». ¿Cuántas son situaciones de riesgo?", "3", "La 1, la 3 y la 4 exponen a un daño; la 2 es una conducta de cuidado."),
        ex("Clasifica «un grupo graba una pelea para burlarse»: A) Conducta violenta. B) Conducta de cuidado.", "A", "Participar o difundir una pelea alimenta la violencia."),
        ex("Un adolescente no tiene a quién contarle sus problemas y se aísla. ¿Aumenta o disminuye su riesgo?", "Aumenta", "El aislamiento es un factor de riesgo."),
    ],
    Z=[
        ex("Explica por qué decir «solo es una vez» no hace segura una situación de riesgo.", "Porque un solo episodio puede causar un daño grave", "El daño puede ocurrir en una ocasión y repetirse."),
        ex("Un curso anota como protección «tener un grupo de amigos que se cuida y avisa a un adulto». ¿Por qué lo es?", "Porque disminuye el riesgo y hay apoyo", "Una amistad que se cuida y avisa ayuda a decidir bien."),
    ],
    D=[
        arith("En una encuesta ficticia de 40 estudiantes, 15 mencionaron el alcohol como riesgo, 12 los vapeadores y 8 la violencia en redes. El resto mencionó otros riesgos. ¿Cuántos mencionaron otros?", "40-15-12-8", "Al total se le restan los grupos nombrados."),
        arith("Un curso identificó 5 factores de protección por cada uno de sus 6 grupos de trabajo. ¿Cuántos factores anotaron en total?", "5*6", "Se multiplican los grupos por los factores de cada uno."),
    ],
    context=[ex("En Orientación, un grupo analiza este caso ficticio: Antonia recibe una invitación a una casa donde «no habrá nadie mayor» y un primo le dice que habrá «de todo». ¿Qué señal de riesgo hay en la invitación?", "No hay adultos y se anuncian sustancias", "La falta de supervisión y la presencia de sustancias aumentan el riesgo.")],
    selfcheck=[ex("En Orientación: ¿el alcohol y los vapeadores son sustancias nocivas?", "Sí", "Dañan el organismo."), ex("¿Un factor de protección disminuye el riesgo?", "Sí", "Así se define."), ex("¿Una pelea grabada para burlarse es una conducta de cuidado?", "No", "Alimenta la violencia.")],
    task=T("Lee el caso de Isabel, una estudiante inventada: la invitan a una fiesta de curso el sábado, sin adultos, donde dos compañeros prometen llevar alcohol; una amiga quiere ir y ella no está segura; una persona adulta de su familia le dijo que puede llamarla si se siente incómoda. Escribe un cuadro con dos columnas: factores de riesgo y factores de protección que aparecen en el caso. Después escribe una frase con la señal que más te preocuparía.", "Riesgo: no hay adultos, hay alcohol, una amiga insiste. Protección: un adulto de su familia le ofrece ayuda y ella duda en vez de ir por presión. Me preocupa la falta de adultos con alcohol.", ["clasifica factores de riesgo y de protección", "usa los datos del caso", "elige una señal y la justifica", "no cuenta nada personal"], ["cuadro de dos columnas"], ["mezclar riesgo con protección", "pensar solo en el alcohol"], "Reconoce los factores bien clasificados y pregunta qué estrategia usaría Isabel."),
    reinforce="Escribe tres situaciones de riesgo para un personaje de cuento y un factor de protección para cada una.",
    extend="Explica la diferencia entre factor de riesgo y factor de protección con un ejemplo propio inventado.",
)

lesson(
    OA3, 2,
    "Una hoja y un lápiz. La lista de afirmaciones y la encuesta de ejemplo están escritas en los ejercicios. Los datos son de ejemplo, no reales.",
    "Aprenderé a separar mitos de hechos sobre sustancias, a nombrar la emoción de la presión de grupo y a defender mi derecho a decir no. Sirve para decidir con información y no por lo que «dicen todos».",
    ["Reconozco situaciones y factores de riesgo.", "Sé que tengo derecho a no ser presionado."],
    [
        "Un mito es una creencia que circula sin comprobarse. Un hecho se puede comprobar con fuentes confiables. Algunos mitos frecuentes: «el vapeo es inofensivo», «el alcohol solo afecta a los adultos» o «lo hacen todos». Los hechos son otros: muchos vapeadores contienen nicotina, que genera adicción; el alcohol altera el juicio, la coordinación y la capacidad de reaccionar; y las drogas ilegales afectan la atención y la memoria y pueden tener consecuencias legales. En Chile no se puede vender alcohol ni tabaco a menores de 18 años.",
        "La presión de grupo despierta emociones: miedo a quedar fuera, ganas de pertenecer, vergüenza. Son emociones normales y no significan que debas ceder. Detrás de «lo hacen todos» suele haber una exageración: casi siempre, una parte importante del grupo no lo hace. Preguntarte «¿esto es un hecho o un mito?» te da un momento para pensar.",
        "Tienes derecho a decir «no» sin dar más explicaciones y a que tu «no» sea respetado. También tienes derecho a cambiar de opinión y a irte de un lugar donde no te sientes seguro. Un límite es una frase corta y clara. Si alguien insiste, se burla o te amenaza, ya no es una invitación: es presión, y puedes pedir ayuda a una persona adulta de confianza.",
    ],
    [("mito", "creencia que circula sin comprobarse"), ("nicotina", "sustancia que genera adicción, presente en el tabaco y en muchos vapeadores"), ("adicción", "necesidad fuerte de consumir algo que cuesta controlar"), ("presión de grupo", "empuje de un grupo para hacer lo que no se quiere"), ("exageración", "decir que algo es más grande o más general de lo que es")],
    [
        W("Mito o hecho", "Un compañero dice: «El vapeo no hace nada porque solo es vapor». ¿Mito o hecho?", ["Muchos vapeadores contienen nicotina.", "La nicotina genera adicción.", "La afirmación omite esos datos."], "Mito"),
        W("Revisar «lo hacen todos»", "En una encuesta de ejemplo de 40 estudiantes, 9 dicen haber probado alcohol. Marcos afirma: «lo hacen todos». ¿Es cierto?", ["9 de 40 es menos de la mitad.", "Eso no son «todos».", "La frase exagera."], "No: 9 de 40 no es «todos»"),
    ],
    [
        M("Creer que lo que dicen muchos en redes es un hecho.", "Se confunde repetición con comprobación.", "Un hecho se comprueba en fuentes confiables."),
        M("Pensar que decir «no» exige una gran explicación.", "Se cree que hay que justificarse ante el grupo.", "Un «no» corto y firme es suficiente."),
    ],
    R=[
        ex("«El vapeo no hace daño». ¿Es un mito o un hecho?", "Un mito", "Muchos vapeadores contienen nicotina, que genera adicción."),
        ex("¿Un «no» corto y claro es suficiente para poner un límite, sí o no?", "Sí", "No necesitas dar más explicaciones."),
        ex("¿Se puede vender alcohol a menores de 18 años en Chile, sí o no?", "No", "Su venta a menores de 18 está prohibida."),
    ],
    U=[
        ex("¿Qué afecta el alcohol? A) El juicio y la coordinación. B) Solo el sueño.", "A", "Altera la forma de decidir y de moverse."),
        ex("¿Sentir miedo a quedar fuera es una emoción normal ante la presión de grupo, sí o no?", "Sí", "Es normal y no obliga a ceder."),
        ex("Un amigo se burla y amenaza porque no aceptas una sustancia. ¿Es una invitación o una presión?", "Una presión", "La burla y la amenaza no respetan tu decisión."),
    ],
    A=[
        ex("Clasifica: 1) «el alcohol altera la coordinación»; 2) «solo los adultos se ven afectados»; 3) «la nicotina genera adicción»; 4) «a los de 14 no les pasa nada». ¿Cuántas son hechos?", "2", "La 1 y la 3 son hechos; la 2 y la 4 son mitos."),
        ex("Valentina lee: «80 % de los jóvenes consume». No dice quién lo midió ni cuándo. ¿Qué debe hacer? A) Dudar y buscar la fuente. B) Creerlo porque tiene una cifra.", "A", "Un dato sin fuente no se puede comprobar."),
        arith("En una encuesta de ejemplo de 50 personas, 10 dicen probar sustancias. ¿Cuántas no lo hacen?", "50-10", "Al total se le restan quienes sí lo hacen; la mayoría no lo hace."),
    ],
    Z=[
        ex("¿Por qué «lo hacen todos» ayuda a presionar a otras personas?", "Porque hace creer que no hacerlo es raro", "Exagera lo que hace el grupo y genera miedo a quedar fuera."),
        ex("Un joven dice: «Solo pruebo un poco, no pasa nada». Con lo aprendido, ¿qué riesgo no considera?", "Que la nicotina u otra sustancia puede generar adicción o dañar", "Aunque sea poco, algunas sustancias pueden afectar la salud."),
    ],
    D=[
        arith("En una encuesta de ejemplo de 45 estudiantes, 12 dicen haber probado vapeadores. ¿Cuántos no lo han hecho?", "45-12", "Al total se le restan los que sí lo han hecho."),
        arith("En una encuesta de ejemplo de 60 jóvenes, 1 de cada 6 dice haber probado alcohol. ¿Cuántos de los 60 lo dicen?", "60//6", "Se divide el total entre 6 para hallar la sexta parte."),
    ],
    context=[ex("En la hora de Orientación, Pía dice que le cuesta decir «no» porque teme que sus amigas se rían. ¿Qué dos cosas puede recordar sobre sus derechos?", "Que puede decir no sin explicar y puede irse", "Tiene derecho a un «no» respetado y a cambiar de opinión.")],
    selfcheck=[ex("En Orientación: ¿un mito se puede comprobar?", "No", "Circula sin comprobarse."), ex("¿Tienes derecho a decir «no» sin dar muchas explicaciones?", "Sí", "Un «no» firme es suficiente."), ex("¿Los vapeadores pueden contener nicotina?", "Sí", "La nicotina genera adicción.")],
    task=T("Lee las cuatro afirmaciones inventadas de un chat: (a) «Si es solo vapor, no hace nada»; (b) «El alcohol cambia cómo reaccionas»; (c) «Lo hacen todos en octavo»; (d) «Probar una sola vez no tiene ningún riesgo». Marca cada una como mito o hecho y escribe una frase de por qué. Después escribe una respuesta corta de límite si alguien las usa para presionarte.", "(a) Mito: muchos vapeadores tienen nicotina. (b) Hecho: el alcohol altera la reacción. (c) Mito: exagera, no son todos. (d) Mito: aun una sola vez hay riesgos, como una intoxicación, y la nicotina puede generar dependencia. Límite: «No me interesa, gracias».", ["clasifica las cuatro afirmaciones", "justifica cada una", "escribe un límite breve y firme", "no cuenta nada personal"], ["tabla de mito o hecho"], ["creer una cifra sin fuente", "no distinguir hecho de exageración"], "Reconoce las clasificaciones y pregunta qué fuente confiable usaría para comprobarlas."),
    reinforce="Escribe un mito y un hecho sobre alcohol o tabaco para un cartel inventado del curso.",
    extend="Explica por qué «lo hacen todos» suele ser una exageración.",
)

lesson(
    OA3, 3,
    "Una hoja y un lápiz. El caso de Andrea y las tres formas de responder están escritos en los ejercicios. Todo ocurre con personajes inventados.",
    "Aprenderé a comparar respuestas pasivas, agresivas y asertivas ante una presión y a prever sus consecuencias, también ante la presión sexual. Sirve para elegir la que cuida mi bienestar.",
    ["Sé separar mitos y hechos sobre sustancias.", "Sé que tengo derecho a decir «no»."],
    [
        "Ante una presión puedes responder de tres maneras. La respuesta pasiva cede o se calla para evitar el conflicto: «bueno, está bien». La agresiva ataca o insulta: «eres un tonto». La asertiva dice lo que piensa con claridad y respeto: «No quiero, gracias. Si quieres, caminamos». Cada una tiene consecuencias distintas para ti y para la relación.",
        "La respuesta pasiva puede traer arrepentimiento y que la presión se repita. La agresiva puede generar una pelea y problemas de convivencia. La asertiva suele proteger tu decisión y mantiene la relación si el otro respeta. Cuando la presión es sexual, por ejemplo cuando una pareja insiste en tener relaciones sexuales «para demostrar amor», la respuesta asertiva es la misma: tienes derecho a decir «no quiero», a esperar y a hablar con una persona adulta o con un profesional de salud sobre cómo cuidarte.",
        "Ceder bajo presión puede traer consecuencias duraderas: un embarazo no planificado, infecciones de transmisión sexual, un daño emocional o problemas de salud por consumo. Decidir informado, sin presión y con respeto es una forma de cuidarte. Tampoco debes presionar a otros: cuando alguien dice «no», se respeta.",
    ],
    [("pasivo", "que cede o se calla para evitar el conflicto"), ("agresivo", "que ataca o insulta para imponerse"), ("asertivo", "que dice lo que piensa con claridad y respeto"), ("infección de transmisión sexual", "enfermedad que se contagia por contacto sexual"), ("arrepentimiento", "malestar por haber hecho algo que no se quería")],
    [
        W("Clasificar respuestas", "Andrea recibe una oferta de vapeador. Responde: «No quiero, gracias. Si quieres, juguemos a las cartas». ¿Es pasiva, agresiva o asertiva?", ["Dice lo que quiere con claridad.", "No ataca ni cede.", "Propone una alternativa."], "Asertiva"),
        W("Comparar consecuencias", "Un compañero presiona a Andrea para probar un vapeador. Opción A: acepta para no quedar mal. Opción B: dice «no» y se queda con otras amigas. Compara.", ["A cede para evitar el conflicto: es pasiva.", "Puede arrepentirse y le seguirán insistiendo.", "B mantiene su decisión y la relación con quienes la respetan."], "B protege su decisión; A puede traer arrepentimiento y más presión"),
    ],
    [
        M("Pensar que ser asertivo es lo mismo que ser agresivo.", "Se confunde firmeza con ataque.", "La asertividad es firme y respetuosa."),
        M("Creer que ceder una vez evita el problema para siempre.", "Se piensa que la presión desaparece.", "Quien cede suele recibir más presión."),
    ],
    R=[
        ex("«Eres un tonto, déjame en paz». ¿Es una respuesta pasiva o agresiva?", "Agresiva", "Ataca con un insulto."),
        ex("«No quiero, gracias» dicho con calma, ¿es asertivo o agresivo?", "Asertivo", "Dice su decisión con respeto."),
        ex("Quedarse callado y aceptar para evitar conflicto, ¿es una respuesta pasiva o asertiva?", "Pasiva", "Cede para no discutir."),
    ],
    U=[
        ex("¿Qué respuesta suele mantener tu decisión y la relación si la otra persona respeta? A) La asertiva. B) La agresiva.", "A", "Es firme y respetuosa."),
        ex("Una pareja dice: «si me quieres, tenemos relaciones sexuales». ¿Es una presión o una forma de cuidado?", "Una presión", "Usa el cariño para obligar y no respeta su decisión."),
        ex("¿Ceder a una presión puede traer arrepentimiento, sí o no?", "Sí", "Se hace algo que no se quería."),
    ],
    A=[
        ex("Ante una oferta de alcohol, cuatro respuestas: 1) «Bueno, uno solo»; 2) «Eres un pesado»; 3) «No quiero, gracias»; 4) silencio y se toma el vaso. ¿Cuál es asertiva?", "La 3", "Es clara, breve y respetuosa."),
        ex("Pía responde a la presión de su pareja: «No estoy lista, y espero que lo respetes». ¿Qué tipo de respuesta es? A) Asertiva. B) Pasiva.", "A", "Dice su decisión sin atacar ni ceder."),
        ex("Si un joven insiste después del «no» de su pareja, ¿qué principio se rompe? A) Que la decisión debe ser libre y respetada. B) Que la pareja decide por los dos.", "A", "Insistir presiona y no respeta su decisión."),
    ],
    Z=[
        ex("¿Por qué responder con un insulto puede agravar el problema?", "Porque puede generar una pelea y no resuelve la presión", "La agresión aumenta el conflicto sin proteger la decisión."),
        ex("Un joven dice: «Si digo no, pierdo a mis amigos». ¿Qué le responderías?", "Que quien lo respeta aceptará su no", "Las amistades respetuosas no exigen ceder."),
    ],
    D=[
        arith("De 36 estudiantes de una encuesta de ejemplo, 14 elegirían la respuesta asertiva, 9 la pasiva y el resto la agresiva. ¿Cuántos elegirían la agresiva?", "36-14-9", "Al total se le restan los otros dos grupos."),
        arith("Un grupo ensaya 4 frases asertivas por cada una de 5 situaciones de presión. ¿Cuántas frases ensayan?", "4*5", "Se multiplican las frases por las situaciones."),
    ],
    context=[ex("En una fiesta ficticia, Sebastián le dice a Lucía: «No seas aburrida, prueba esto». Ella responde: «No quiero, gracias. Voy a buscar algo de tomar sin alcohol». ¿Qué tipo de respuesta usó y por qué sirve?", "Asertiva, porque dice su decisión con respeto y propone otra cosa", "Mantiene su decisión sin agredir ni ceder.")],
    selfcheck=[ex("En Orientación: ¿una respuesta asertiva dice lo que piensas con respeto?", "Sí", "Es firme y respetuosa."), ex("¿Ceder siempre evita que la presión se repita?", "No", "Puede aumentar la presión."), ex("¿Una presión sexual se responde con el derecho a decir «no quiero»?", "Sí", "Tienes derecho a decir no.")],
    task=T("Lee el caso inventado de Tomás: en una plaza, un grupo le ofrece fumar un cigarrillo electrónico. Escribe tres respuestas posibles (una pasiva, una agresiva y una asertiva) con la frase exacta que diría, y para cada una anota la consecuencia más probable. Cierra eligiendo una y explicando por qué cuida su bienestar.", "Pasiva: «Bueno, solo una vez»; puede arrepentirse y le insistirán. Agresiva: «Ustedes son unos tontos»; habrá pelea. Asertiva: «No, gracias, no me interesa. Voy a jugar pelota»; mantiene su decisión. Elijo la asertiva.", ["escribe las tres respuestas con frases exactas", "anota una consecuencia para cada una", "elige la asertiva y justifica", "no cuenta nada personal"], ["tabla de tres filas"], ["confundir asertividad con agresión", "no prever consecuencias"], "Valora la comparación y pregunta qué haría Tomás si el grupo insistiera."),
    reinforce="Escribe una frase pasiva, una agresiva y una asertiva para decir que no a una invitación a una pelea.",
    extend="Explica por qué las consecuencias de la respuesta asertiva suelen proteger mejor a la persona.",
)

lesson(
    OA3, 4,
    "Una hoja y un lápiz. El caso de la fiesta de Camila y las alternativas de acción están escritos en los ejercicios. Todo ocurre con personajes inventados.",
    "Aprenderé a elegir una acción segura ante el consumo de sustancias y las conductas violentas, y a ayudar a un amigo sin ponerme en peligro. Sirve para saber qué hacer cuando ya estoy frente al problema.",
    ["Sé comparar respuestas pasivas, agresivas y asertivas.", "Sé que debo avisar a una persona adulta de confianza ante un riesgo."],
    [
        "Una acción segura protege tu integridad y la de otros, y suele incluir tres pasos: alejarte del peligro, avisar a una persona adulta de confianza y no actuar solo en una situación que te supera. No es de cobardes salir de un lugar donde hay riesgo: es una decisión inteligente. Puedes decir «tengo que irme» sin dar más explicaciones.",
        "Si ves que un amigo consumió mucho alcohol o una sustancia y se siente mal, no lo dejes solo ni le pidas que «se aguante». Pide a otra persona que se quede con él mientras buscas de inmediato a una persona adulta y pides ayuda al servicio de emergencia que corresponda. Nunca te subas a un vehículo cuyo conductor consumió alcohol u otras sustancias; avisa a tu familia para que te vaya a buscar.",
        "Ante una pelea, no intervengas con golpes ni la grabes para burlarte. Aléjate, llama a una persona adulta del colegio o del lugar y cuida a quien salió lastimado. Si se trata de violencia en el pololeo, como empujones o amenazas, tampoco es un asunto privado: hay que avisar a una persona adulta. Pedir ayuda no es acusar, es proteger.",
    ],
    [("acción segura", "decisión que protege la integridad de todos y cuenta con ayuda adulta"), ("integridad", "bienestar físico y emocional de una persona"), ("servicio de emergencia", "ayuda profesional que se llama ante un peligro grave"), ("intervenir", "meterse en una situación para cambiarla"), ("vehículo", "medio de transporte, como un auto o una moto")],
    [
        W("Elegir ante un amigo con malestar", "En una fiesta, Rafael ve que su amigo bebió mucho y está mareado y vomitando. ¿Qué hace?", ["No debe dejarlo solo.", "Si va a buscar ayuda, pide a otra persona que se quede con él.", "Debe buscar a una persona adulta y pedir ayuda al servicio de emergencia que corresponda."], "Que alguien se quede con su amigo mientras busca a una persona adulta y pide ayuda"),
        W("Elegir ante una pelea", "Dos estudiantes pelean a golpes en el patio y un grupo grita para que sigan. ¿Cuál es la acción segura de Camila?", ["Intervenir con golpes la pondría en riesgo.", "Grabarla para burlarse alimenta la violencia.", "Avisar a una persona adulta protege a todos."], "Alejarse y avisar a una persona adulta del colegio"),
    ],
    [
        M("Creer que avisar a un adulto es «acusar» y traicionar al amigo.", "Se confunde lealtad con guardar un secreto peligroso.", "Avisar protege a quien está en peligro."),
        M("Pensar que se puede subir a un auto si el conductor «maneja bien» aunque haya bebido.", "Se confía en la apariencia de control.", "No viajes con quien consumió; avisa a tu familia."),
    ],
    R=[
        ex("Si un amigo está muy mal por beber, ¿lo dejas solo o buscas a un adulto?", "Buscas a un adulto", "Necesita ayuda y no debe quedar solo."),
        ex("¿Te subes a un auto cuyo conductor bebió alcohol, sí o no?", "No", "Maneja con el juicio alterado y es muy peligroso."),
        ex("Ante una pelea, ¿grabas para burlarte o te alejas y avisas a un adulto?", "Te alejas y avisas", "Grabar burlándote alimenta la violencia."),
    ],
    U=[
        ex("¿Por qué salir de un lugar con riesgo es una decisión inteligente?", "Porque protege tu integridad", "Evita el daño y no depende de convencer a otros."),
        ex("Un empujón y una amenaza en el pololeo, ¿son un asunto privado o violencia que se debe avisar?", "Violencia que se debe avisar", "La violencia no es privada y necesita ayuda adulta."),
        ex("Nunca dejes solo a un amigo que se siente mal. ¿Es verdadero o falso?", "Verdadero", "Puede empeorar y necesita ayuda."),
    ],
    A=[
        ex("Camila está en una fiesta y ve que alguien le agrega una sustancia a una bebida ajena sin avisar. Opciones: 1) mirar y callar; 2) avisar al dueño y a una persona adulta; 3) reírse; 4) tomarla. ¿Cuál es segura?", "La 2", "Previene el daño y suma ayuda adulta."),
        ex("Un amigo quiere manejar tras beber. ¿Qué haces? A) Avisar a tu familia y no subirte. B) Subirte para que no maneje solo.", "A", "No te expones al riesgo y buscas apoyo."),
        ex("Lucas ve que un compañero empuja con rabia a su polola. ¿Cuál es una acción segura?", "Avisar a una persona adulta de confianza", "La violencia debe ser atendida por una persona adulta."),
    ],
    Z=[
        ex("¿Por qué avisar a un adulto no es una traición a la amistad?", "Porque protege al amigo de un daño", "La amistad cuida, no oculta peligros."),
        ex("Un grupo decide no llamar a nadie porque «se van a enojar». ¿Qué riesgo corren?", "Que el amigo empeore", "Esperar puede agravar el estado de la persona."),
    ],
    D=[
        arith("En un curso de 30 estudiantes, 22 saben que no deben subirse a un auto con un conductor que bebió y el resto no lo sabe. ¿Cuántos no lo saben?", "30-22", "Al total se le restan los que sí lo saben."),
        arith("Un protocolo de acción segura tiene 3 pasos y el curso lo ensaya con 7 casos. ¿Cuántos pasos ensaya en total?", "3*7", "Se multiplican los pasos por los casos."),
    ],
    context=[ex("En el patio, Daniel ve que a un compañero lo rodean tres jóvenes que lo amenazan para quitarle dinero. ¿Cuál es la acción segura para Daniel?", "Alejarse y avisar a una persona adulta del colegio", "Interviniendo solo podría resultar herido; el adulto puede actuar.")],
    selfcheck=[ex("En Orientación: ¿alejarse de un lugar con riesgo es una decisión inteligente?", "Sí", "Protege tu integridad."), ex("¿Se debe avisar a un adulto cuando un amigo está muy mal?", "Sí", "El amigo necesita ayuda."), ex("¿Grabar una pelea para reírse es una acción segura?", "No", "Alimenta la violencia.")],
    task=T("Lee el caso inventado de Martina: en una casa sin adultos, un grupo comparte alcohol; su amigo Teo empieza a sentirse mal y alguien propone llevarlo en el auto de un joven que ya bebió. Escribe un plan de cuatro pasos para Martina: qué hace primero, a quién avisa, qué evita y qué le dice a Teo. Usa frases cortas y claras.", "1) No dejar solo a Teo. 2) Avisar a una persona adulta y pedir ayuda al servicio de emergencia. 3) Evitar que se suba al auto de quien bebió. 4) Decirle a Teo: «Estoy contigo, voy a buscar ayuda».", ["plan de cuatro pasos", "incluye avisar a una persona adulta", "evita subir a un conductor que bebió", "usa frases claras y respetuosas"], ["lista de pasos"], ["dejar solo al amigo", "viajar con quien bebió"], "Reconoce los pasos seguros y pregunta qué haría si no hay adultos cerca."),
    reinforce="Escribe tres pasos seguros ante una pelea para un personaje de cuento.",
    extend="Explica por qué pedir ayuda adulta ante un riesgo es una acción de cuidado.",
)

lesson(
    OA3, 5,
    "Una hoja y un lápiz. Las situaciones y la lista de personas de ayuda están escritas en los ejercicios. Los personajes son inventados.",
    "Aprenderé a practicar la comunicación asertiva y a buscar ayuda en personas significativas y especializadas, dentro o fuera del colegio. Sirve para saber a quién acudir y qué decir ante un riesgo.",
    ["Sé elegir una acción segura.", "Sé la diferencia entre respuesta pasiva, agresiva y asertiva."],
    [
        "La comunicación asertiva se puede ensayar. Una técnica útil, distinta del mensaje «cuando… me siento… por favor…» de la clase de sexualidad, tiene tres partes: decir «no» con claridad, dar una razón breve si quieres y proponer una alternativa. Por ejemplo: «No, gracias, no fumo. Vamos a jugar pelota». Si la persona insiste, repites la frase con calma, sin discutir y sin cambiar de opinión.",
        "Las personas significativas son aquellas en quienes confías: familiares, profesores, amigos que te cuidan. Las personas especializadas tienen formación para ayudar en problemas específicos: la psicóloga o el orientador del colegio, el equipo de convivencia escolar, los profesionales del Cesfam (centro de salud familiar) y los servicios de salud. Dentro del colegio puedes recurrir al profesor jefe, al orientador o a convivencia escolar. Fuera, a tu familia y a los centros de salud. Si necesitas hablar con alguien y no sabes con quién, puedes llamar al Fono Niños 147.",
        "Al pedir ayuda, sé concreto: cuenta qué pasó, cómo te sientes y qué necesitas. Por ejemplo: «Me ofrecieron vapeadores y me siento presionado; necesito ayuda para saber qué hacer». No tienes que resolver todo solo. Si la primera persona no te escucha, busca a otra. También puedes acompañar a un amigo que no se atreve a pedir ayuda y ofrecerte a ir con él.",
    ],
    [("personas significativas", "personas de confianza que son importantes para alguien"), ("personas especializadas", "profesionales con formación para ayudar en un problema específico"), ("convivencia escolar", "equipo y forma de relacionarse en el colegio"), ("técnica asertiva", "pasos para decir que no con claridad y respeto"), ("alternativa", "otra opción que se propone")],
    [
        W("Construir una frase asertiva", "Ante la oferta de un vapeador, arma una frase con las tres partes: no, razón breve y alternativa.", ["Dice no con claridad: «No, gracias».", "Da una razón breve: «no me interesa».", "Propone una alternativa: «vamos a conversar».", "Se une todo en una frase."], "«No, gracias, no me interesa. Vamos a conversar»"),
        W("Elegir a quién acudir", "Dante recibe presiones constantes para probar drogas. ¿A quién puede acudir?", ["Dentro del colegio: profesor jefe, orientador o convivencia escolar.", "Fuera: familia o Cesfam.", "Todas son personas de confianza o especializadas."], "Al orientador o convivencia escolar y a su familia; puede llamar al 147"),
    ],
    [
        M("Pensar que hay que resolver los problemas solo.", "Se cree que pedir ayuda es debilidad.", "Pedir ayuda es una decisión de cuidado."),
        M("Contar un problema de forma muy vaga: «me pasa algo».", "Se omite lo que se necesita.", "Cuenta qué pasó, cómo te sientes y qué necesitas."),
    ],
    R=[
        ex("¿La psicóloga del colegio es una persona especializada, sí o no?", "Sí", "Tiene formación para ayudar en problemas específicos."),
        ex("Si no sabes con quién hablar, ¿esta clase nombra al Fono Niños 147 como una línea a la que puedes llamar, sí o no?", "Sí", "Es la línea de ayuda que nombra esta clase."),
        ex("Si la primera persona no te escucha, ¿te rindes o buscas a otra?", "Buscas a otra", "Hay más personas que pueden ayudar."),
    ],
    U=[
        ex("¿Qué tres partes tiene la técnica asertiva? A) No, razón breve y alternativa. B) Insulto, grito y silencio.", "A", "Esa es la técnica asertiva de esta clase."),
        ex("Si la persona insiste, ¿repites tu frase con calma o discutes?", "Repites tu frase con calma", "Mantiene tu decisión sin pelear."),
        ex("¿Un familiar de confianza es una persona significativa, sí o no?", "Sí", "Es alguien importante en quien confías."),
    ],
    A=[
        ex("Marca la frase que sirve para pedir ayuda: 1) «Me pasa algo»; 2) «Me presionan para probar alcohol y necesito ayuda»; 3) «Nada, olvídalo»; 4) «Déjame solo». ¿Cuál es?", "La 2", "Cuenta qué pasa y qué necesita."),
        ex("Ámbar quiere ayudar a su amiga que se siente presionada, pero ella no se atreve a hablar. ¿Qué puede hacer? A) Ofrecerse a acompañarla. B) Callarse.", "A", "Acompañar facilita que pida ayuda."),
        ex("Una estudiante se siente muy angustiada por un riesgo que vive. ¿Qué especialista del colegio puede ayudarla?", "La psicóloga u orientadora", "Tienen formación para apoyar en estos problemas."),
    ],
    Z=[
        ex("¿Por qué conviene dar una alternativa al decir que no?", "Porque mantiene la relación y muestra otra opción", "Evita que el rechazo se sienta como un ataque."),
        ex("Un joven dice: «Si cuento, empeora todo». ¿Qué le responderías?", "Que un adulto puede protegerlo y buscar solución", "Pedir ayuda evita que el problema crezca."),
    ],
    D=[
        arith("Un curso de 40 estudiantes anotó a quién acudiría: 15 a la familia, 12 al profesor jefe, 8 al orientador y el resto a un profesional de salud. ¿Cuántos eligieron a un profesional de salud?", "40-15-12-8", "Al total se le restan los otros grupos."),
        arith("En un taller, cada grupo de 4 estudiantes ensaya 3 frases. Si hay 9 grupos, ¿cuántas frases ensayan?", "9*4*3", "Se multiplican los grupos, los estudiantes y las frases."),
    ],
    context=[ex("Un estudiante ficticio llamado Gabo ve que un compañero vende sustancias cerca del colegio. Le da miedo hablar. ¿A quién puede contarle y qué debe evitar?", "A una persona adulta del colegio o de su familia; no enfrentar al compañero", "Un adulto puede actuar con protocolos y evitar riesgos para Gabo.")],
    selfcheck=[ex("En Orientación: ¿el orientador del colegio puede ayudar ante un riesgo?", "Sí", "Es una persona de ayuda."), ex("¿Hace falta resolver los problemas solo?", "No", "Pedir ayuda es una decisión de cuidado."), ex("¿Una frase asertiva incluye una alternativa?", "Sí", "Sirve para mantener la relación.")],
    task=T("Lee las tres situaciones inventadas: (1) te ofrecen un cigarrillo electrónico; (2) un compañero te presiona para tener una conducta sexual de riesgo; (3) observas que un grupo amenaza a un estudiante. Para cada una escribe: la frase asertiva o de aviso que dirías y a qué persona significativa o especializada acudirías.", "(1) «No, gracias, no me interesa. Vamos a la cancha»; a mi profesor jefe si insisten. (2) «No quiero. Respeta mi decisión»; a la orientadora o a un profesional de salud. (3) Me alejo y aviso al encargado de convivencia escolar.", ["completa las tres situaciones", "la frase es asertiva o un aviso claro", "nombra personas de ayuda", "no cuenta nada personal"], ["tabla escrita"], ["frases agresivas", "no nombrar personas de ayuda"], "Valora las frases claras y pregunta qué haría si la primera persona no la escuchara."),
    reinforce="Escribe una frase asertiva de tres partes para rechazar una invitación a un lugar sin adultos.",
    extend="Explica la diferencia entre una persona significativa y una persona especializada.",
)

# ================================================================ OA 04
lesson(
    OA4, 1,
    "Una hoja y un lápiz. La semana de Tomás, un estudiante inventado, y las recomendaciones están escritas en los ejercicios. Los datos son de ejemplo.",
    "Aprenderé a revisar mis hábitos de alimentación, descanso y actividad física con criterios sencillos. Sirve para tomar decisiones de vida saludable en lo personal y en el colegio.",
    ["Sé que dormir, comer bien y moverme cuida mi salud.", "Sé que un hábito es algo que repito a diario."],
    [
        "El bienestar cotidiano se construye con hábitos. Una alimentación saludable incluye frutas, verduras, legumbres, agua y pocos alimentos con sellos negros de «ALTO EN» azúcares, grasas saturadas, sodio o calorías. El descanso apropiado para adolescentes es de 8 a 10 horas de sueño por noche, como recomendación general. La actividad física recomendada es de al menos 60 minutos diarios de movimiento de moderado a intenso, que puede sumarse en partes.",
        "Para examinar un caso se compara lo que hace una persona con esos criterios. Si Tomás duerme 6 horas, está por debajo de lo recomendado. Si camina 20 minutos al día, le faltan 40 para llegar a 60. Observar con datos permite proponer cambios concretos y no culpar. Un cambio pequeño y sostenido, como acostarse 30 minutos antes, suele ser más efectivo que uno grande que dura un día.",
        "El bienestar también se cuida en comunidad: un recreo con juegos activos, un kiosco con opciones saludables o el respeto a los horarios de descanso ayudan a todo el curso. Y se cuida en lo emocional: hablar de lo que te preocupa y pedir ayuda a una persona adulta forma parte de una vida saludable.",
    ],
    [("hábito", "conducta que se repite a diario"), ("alimentación saludable", "forma de comer que incluye variedad y poco de lo que dice «ALTO EN»"), ("descanso", "tiempo de sueño y pausas que recuperan el cuerpo"), ("actividad física", "cualquier movimiento del cuerpo que gasta energía"), ("sello «ALTO EN»", "octágono negro que advierte exceso de azúcares, grasas saturadas, sodio o calorías")],
    [
        W("Revisar el sueño", "Tomás duerme 6 horas por noche. El criterio es de 8 a 10 horas. ¿Cumple y cuánto le falta como mínimo?", ["Compara 6 con el mínimo de 8.", "No cumple.", "Faltan 8 − 6 = 2 horas."], "No cumple; le faltan al menos 2 horas"),
        W("Sumar actividad física", "Tomás camina 20 minutos al ir al colegio, juega pelota 25 minutos y baila 10 minutos. ¿Llega a 60 minutos?", ["Suma 20 + 25 + 10.", "El total es 55 minutos.", "55 es menor que 60: faltan 5."], "No: suma 55 minutos y le faltan 5"),
    ],
    [
        M("Creer que basta con comer saludable y no importa dormir.", "Se ve cada hábito por separado.", "El bienestar combina alimentación, descanso y movimiento."),
        M("Querer cambiar todo en un día.", "Se piensa que el cambio debe ser grande.", "Un cambio pequeño y sostenido es más efectivo."),
    ],
    R=[
        ex("¿Cuántos minutos de actividad física al día se recomiendan como mínimo en esta clase: 30 o 60?", "60", "Se recomienda al menos 60 minutos diarios."),
        ex("¿Cuántas horas de sueño recomienda esta clase para adolescentes: de 8 a 10 o de 4 a 5?", "De 8 a 10", "Es la recomendación general indicada."),
        ex("El sello negro «ALTO EN» ¿advierte un exceso o una cualidad saludable?", "Un exceso", "Advierte exceso de azúcares, grasas saturadas, sodio o calorías."),
    ],
    U=[
        ex("¿Por qué un cambio pequeño y sostenido suele servir más que uno grande de un día? A) Porque se mantiene. B) Porque es más fácil de olvidar.", "A", "Un hábito se forma con repetición."),
        ex("¿La actividad física puede sumarse en partes durante el día, sí o no?", "Sí", "Se pueden sumar caminatas, juegos y deporte."),
        ex("¿Dormir poco afecta solo el estado de ánimo o también la atención en clases?", "También la atención en clases", "El descanso insuficiente afecta la concentración y el ánimo."),
    ],
    A=[
        ex("Tomás tomó 3 vasos de bebida azucarada con sello «ALTO EN» y 1 vaso de agua. ¿Qué cambio concreto sería razonable? A) Cambiar un vaso de bebida por agua. B) Cambiar el vaso de agua por otra bebida con sello.", "A", "Es un cambio pequeño, realista y saludable."),
        ex("Un curso ve que a la hora del recreo el 70 % se queda sentado. ¿Qué podría proponer para la comunidad escolar?", "Juegos activos en el recreo", "Aumentan el movimiento de todo el curso."),
        arith("Tomás duerme 7 horas en promedio por noche y quiere llegar a 9. ¿Cuántas horas más debe dormir cada noche?", "9-7", "Se resta lo que duerme de lo que quiere dormir."),
    ],
    Z=[
        ex("Explica por qué decir «soy flojo» no ayuda a mejorar los hábitos.", "Porque es una etiqueta y no propone un cambio concreto", "Observar datos y proponer un paso pequeño sí ayuda."),
        ex("Un kiosco escolar ofrece solo productos con sello «ALTO EN». ¿Qué propuesta razonable haría un curso?", "Pedir también fruta, agua y otras opciones saludables", "Amplía las opciones sin prohibir."),
    ],
    D=[
        arith("Un estudiante hace 40 minutos de actividad el lunes, 30 el martes, 50 el miércoles y 60 el jueves. ¿Cuántos minutos suma en los cuatro días?", "40+30+50+60", "Se suman los minutos de cada día."),
        arith("La recomendación es de 60 minutos diarios. ¿Cuántos minutos serían en una semana de 7 días?", "60*7", "Se multiplican los minutos diarios por los días."),
    ],
    context=[ex("En Orientación, Lucía anota que duerme 6 horas, no come verduras y camina 15 minutos al día. ¿Cuál de los tres hábitos conviene cambiar primero para que el cambio sea alcanzable?", "El que ella elija y pueda sostener, por ejemplo acostarse 30 minutos antes", "Un cambio pequeño y sostenido es más fácil de mantener.")],
    selfcheck=[ex("En Orientación: ¿la alimentación saludable incluye frutas y verduras?", "Sí", "Es parte de una alimentación saludable."), ex("¿Se recomiendan 8 a 10 horas de sueño para adolescentes?", "Sí", "Es la recomendación general."), ex("¿El sello «ALTO EN» indica un exceso?", "Sí", "Advierte exceso de algún nutriente.")],
    task=T("Lee los datos de la semana de Camila, una estudiante inventada: duerme 6 horas; hace 20 minutos de actividad física; toma 2 bebidas con sello «ALTO EN» y 1 vaso de agua al día; come una fruta. Haz una tabla con tres filas (alimentación, descanso, actividad física): lo que hace, el criterio y un cambio pequeño para la próxima semana.", "Descanso: 6 h; criterio 8 a 10 h; acostarse 30 minutos antes. Actividad: 20 min; criterio 60 min; sumar una caminata de 15 min. Alimentación: 2 bebidas ALTO EN; criterio pocas; cambiar una por agua.", ["compara con el criterio", "propone un cambio pequeño por hábito", "usa los datos del caso", "no cuenta nada personal"], ["tabla escrita"], ["proponer cambios gigantes", "no comparar con el criterio"], "Reconoce el uso de datos y pregunta cómo sabrá Camila si el cambio funciona."),
    reinforce="Escribe tres hábitos saludables y un cambio pequeño para uno de ellos.",
    extend="Explica por qué el bienestar incluye hábitos personales y acuerdos de la comunidad escolar.",
)

lesson(
    OA4, 2,
    "Una hoja y un lápiz. El caso de Valentina y la lista de datos están escritos en los ejercicios; no hay imágenes ni datos reales. Todo ocurre con personajes inventados.",
    "Aprenderé a distinguir qué datos y fotos conviene mantener privados, qué derechos tengo sobre mi imagen y cómo cuidar la integridad de mi cuerpo en lo digital. Sirve para usar las redes con seguridad.",
    ["Sé que la intimidad es mi mundo privado.", "Sé que no debo enviar imágenes íntimas."],
    [
        "Todo lo que publicas o envías puede copiarse, guardarse y circular sin tu control. Esa huella queda como tu huella digital. Por eso conviene distinguir los datos privados de los que se pueden compartir. Son privados: tu dirección, tu horario de salidas, tu colegio con tu nombre completo, tu ubicación en tiempo real, tus claves y tus fotos íntimas. Puedes compartir cosas que no te expongan, como un dibujo o una opinión.",
        "Tienes derecho sobre tu imagen: nadie debe publicar fotos tuyas ni compartir mensajes privados sin tu permiso, y tú tampoco debes hacerlo con otros. Tu cuerpo es tuyo también en lo digital: nadie debe pedirte imágenes íntimas ni presionarte. Un límite digital es una decisión como «no acepto solicitudes de personas que no conozco».",
        "Distingue hechos, emociones y límites. El hecho: alguien te pide una foto o tu dirección. La emoción: incomodidad o curiosidad. El derecho: a tu privacidad. El límite: decir que no, guardar una captura, bloquear y avisar. Las ganas de recibir «me gusta» o de pertenecer son normales, pero no valen más que tu seguridad.",
    ],
    [("huella digital", "rastro de lo que una persona publica o hace en internet"), ("privacidad", "derecho a mantener en reserva datos y vida personal"), ("dato privado", "información que no se debe compartir con desconocidos"), ("ubicación en tiempo real", "lugar exacto donde alguien está en este momento"), ("solicitud", "pedido para ser contacto o seguidor")],
    [
        W("Clasificar datos", "Valentina piensa publicar: (a) una foto de su perro; (b) su dirección y horario de salida del colegio. ¿Cuál es un dato privado?", ["La foto del perro no revela dónde vive.", "La dirección y el horario sí permiten ubicarla.", "Es privado lo que la expone."], "El b: su dirección y horario"),
        W("Aplicar hecho, derecho y límite", "Un desconocido le escribe a Valentina: «Mándame una foto tuya». Aplica el análisis.", ["Hecho: un desconocido pide una foto.", "Derecho: a su privacidad e imagen.", "Límite: no enviar, guardar una captura, bloquear y avisar."], "No enviar, guardar una captura, bloquear y avisar a una persona adulta de confianza"),
    ],
    [
        M("Pensar que publicar algo y borrarlo después lo elimina del todo.", "Se olvida que otros pueden copiarlo.", "Piensa antes de publicar; la huella digital puede quedar."),
        M("Creer que es seguro aceptar solicitudes de gente «que tiene amigos en común».", "Se confunde conocidos de conocidos con confianza.", "Acepta solo a quien conoces y puedes confirmar."),
    ],
    R=[
        ex("Tu dirección y tu clave, ¿son datos privados, sí o no?", "Sí", "Revelan dónde estás o dan acceso a tus cuentas."),
        ex("Una foto de tu dibujo, ¿expone tu seguridad, sí o no?", "No", "No revela datos que permitan ubicarte."),
        ex("Si un desconocido te pide una foto, ¿la envías o la rechazas?", "La rechazas", "Tienes derecho a tu privacidad y a rechazarla."),
    ],
    U=[
        ex("¿Qué es la huella digital? A) El rastro de lo que haces en internet. B) Una marca en el celular.", "A", "Es lo que queda de lo que publicas o haces en línea."),
        ex("Si compartes en tiempo real tu ubicación, ¿qué riesgo aumenta?", "Que alguien sepa dónde estás", "Permite ubicarte en cualquier momento."),
        ex("¿Tienes derecho a que no publiquen tu foto sin tu permiso, sí o no?", "Sí", "Tienes derecho sobre tu imagen."),
    ],
    A=[
        ex("Lista de Valentina: 1) su opinión sobre una película; 2) su ubicación en tiempo real; 3) su clave del correo; 4) una foto de un paisaje. ¿Cuántos datos son privados?", "2", "La ubicación en tiempo real y la clave son privadas."),
        ex("Un compañero sube una foto de Valentina sin su permiso. ¿Qué derecho se vulnera? A) El derecho sobre su imagen. B) El derecho a ganar.", "A", "Nadie debe publicar fotos sin permiso."),
        ex("Camila recibe una solicitud de una cuenta sin foto ni datos. ¿Qué límite digital conviene? A) No aceptar. B) Aceptar por curiosidad.", "A", "No conoce a la persona y no puede confirmar quién es."),
    ],
    Z=[
        ex("¿Por qué «borrar» una foto íntima enviada no asegura que desaparezca?", "Porque la otra persona pudo guardarla o reenviarla", "Una vez enviada, ya no la controlas."),
        ex("Un grupo dice que quien no comparte su ubicación «es aburrido». ¿Qué argumento defiende tu seguridad?", "Que tu seguridad vale más que la aprobación", "Compartir la ubicación puede exponerte a riesgos."),
    ],
    D=[
        arith("Una encuesta de ejemplo de 50 estudiantes muestra que 18 tienen perfil público, 24 privado y el resto no tiene perfil. ¿Cuántos no tienen perfil?", "50-18-24", "Al total se le restan los que tienen perfil público o privado."),
        arith("Un curso revisa su privacidad con 5 preguntas por cuenta. Si cada estudiante revisa 3 cuentas, ¿cuántas respuestas escribe cada uno?", "5*3", "Se multiplican las preguntas por las cuentas."),
    ],
    context=[ex("En el curso circula una foto de Lucía en traje de baño, tomada en una piscina, que alguien subió a un grupo. A ella le molesta. ¿Qué acción es más segura para Lucía?", "Pedir que la eliminen del grupo y contárselo a un adulto de confianza", "Pone el límite y busca ayuda.")],
    selfcheck=[ex("En Orientación: ¿tu dirección es un dato privado?", "Sí", "Permite ubicarte con facilidad."), ex("¿Nadie debe publicar tu foto sin permiso?", "Sí", "Es un derecho sobre tu imagen."), ex("¿Puedes bloquear a quien te pide fotos?", "Sí", "Es un límite digital.")],
    task=T("Lee los cinco datos que una estudiante inventada, Noelia, piensa publicar: (a) su colegio y curso con su nombre completo; (b) una foto de su mascota; (c) su ubicación en tiempo real; (d) un dibujo que hizo; (e) su clave de correo para un amigo. Clasifica cada uno como compartible o privado y explica por qué dos de los privados exponen a Noelia.", "Compartible: b y d. Privado: a, c y e. Dos que la exponen: c, porque permite saber dónde está, y e, porque cede el acceso a su cuenta.", ["clasifica los cinco datos", "explica por qué dos datos privados la exponen", "usa los conceptos de privacidad", "no cuenta datos propios"], ["tabla de clasificación"], ["compartir ubicación", "creer que una clave se comparte con amigos"], "Reconoce las clasificaciones y pregunta qué límite digital pondría Noelia."),
    reinforce="Escribe tres datos privados y tres compartibles para un perfil inventado.",
    extend="Explica por qué la huella digital obliga a pensar antes de publicar.",
)

lesson(
    OA4, 3,
    "Una hoja y un lápiz. Las configuraciones de redes y las claves de ejemplo están escritas en los ejercicios. No uses ninguna clave real tuya.",
    "Aprenderé a comparar opciones de seguridad en redes sociales y sus consecuencias: perfil público o privado, solicitudes, claves y ubicación. Sirve para elegir medidas que protejan mi intimidad.",
    ["Sé qué datos son privados.", "Sé que tengo derecho sobre mi imagen."],
    [
        "Cada decisión en una red social tiene consecuencias. Un perfil público puede ser visto por cualquiera, incluso por quienes buscan información para engañar. Un perfil privado solo es visto por quienes aceptas. Aceptar solo a quienes conoces en la vida real reduce el riesgo de engaños, suplantación y acoso.",
        "Las claves son la llave de tus cuentas. Una clave fuerte es larga, por ejemplo una frase de varias palabras con números, y distinta para cada cuenta. Una clave débil es corta, como un nombre o una fecha. Nunca compartas tus claves, ni siquiera con amigos o pareja. Activar la verificación en dos pasos, cuando existe, suma una barrera extra.",
        "Otras medidas: desactivar la ubicación en las publicaciones, pensar antes de etiquetar a otros, revisar quién puede ver tus fotos y cerrar sesión en equipos que no son tuyos. Al comparar opciones, pregunta: ¿qué ganó y qué arriesgo? Una decisión segura no depende de la suerte: reduce los riesgos antes de que ocurran.",
    ],
    [("perfil privado", "cuenta que solo ven las personas que el dueño acepta"), ("suplantación", "hacerse pasar por otra persona"), ("clave fuerte", "contraseña larga y distinta para cada cuenta"), ("verificación en dos pasos", "medida extra para entrar a una cuenta"), ("etiquetar", "mencionar a una persona en una publicación")],
    [
        W("Elegir entre dos claves", "Opción 1: «lucas2011». Opción 2: «mi gato come 3 sardinas azules». ¿Cuál es más fuerte?", ["La opción 1 es corta y usa un nombre y un año.", "La opción 2 es larga y combina palabras y número.", "La más larga y difícil de adivinar es mejor."], "La opción 2"),
        W("Comparar perfiles", "Ana tiene un perfil público con 400 seguidores desconocidos. Bruno tiene uno privado con 60 conocidos. ¿Cuál reduce más el riesgo de engaños?", ["Los desconocidos pueden ver y escribir al perfil público.", "El perfil privado limita quién ve el contenido.", "Conocidos reales son más seguros."], "El perfil privado de Bruno"),
    ],
    [
        M("Pensar que una clave con tu nombre es fácil de recordar y suficiente.", "Se prioriza la comodidad.", "Usa una frase larga y distinta para cada cuenta."),
        M("Creer que compartir la clave con la pareja demuestra confianza.", "Se confunde confianza con control.", "Las claves no se comparten; la confianza no exige revisar cuentas."),
    ],
    R=[
        ex("Una clave fuerte, ¿es larga o corta?", "Larga", "Es más difícil de adivinar."),
        ex("Un perfil privado, ¿lo ve cualquier persona o solo quien aceptas?", "Solo quien aceptas", "Esa es la diferencia con un perfil público."),
        ex("¿Se debe compartir la clave con un amigo, sí o no?", "No", "Las claves no se comparten con nadie."),
    ],
    U=[
        ex("¿Por qué conviene usar una clave distinta para cada cuenta? A) Porque si una se filtra, las otras siguen protegidas. B) Porque así se olvida más fácil.", "A", "Limita el daño si una clave se conoce."),
        ex("¿Qué riesgo disminuye al aceptar solo a quienes conoces en persona?", "Los engaños y el acoso", "Menos desconocidos pueden acercarse con malas intenciones."),
        ex("Si activas la verificación en dos pasos, ¿tu cuenta tiene una barrera extra o menos?", "Una barrera extra", "Es una medida adicional de seguridad."),
    ],
    A=[
        ex("Cuatro claves: 1) «123456»; 2) «Camila2012»; 3) «mi perro salta 4 veces al sol»; 4) «hola». ¿Cuál es la más fuerte?", "La 3", "Es larga, mezcla palabras y número y no es fácil de adivinar."),
        ex("Pía va a publicar una foto en la plaza de su barrio y su cuenta registra la ubicación exacta. ¿Qué medida conviene? A) Desactivar la ubicación de la publicación. B) Agregar más etiquetas.", "A", "Evita que desconocidos sepan dónde está."),
        ex("Un amigo pide la clave de Rafael para «jugar un nivel». ¿Qué conviene hacer?", "No dársela", "Las claves no se comparten ni siquiera con amigos."),
    ],
    Z=[
        ex("¿Por qué una cuenta con 800 seguidores desconocidos puede ser riesgosa?", "Porque alguien puede engañar o acosar", "No se sabe quién es cada persona ni qué busca."),
        ex("Valentina dice: «Mi pareja merece mi clave por confianza». ¿Qué la rebate?", "Que la confianza no exige revisar su intimidad", "La clave protege el mundo privado de cada persona."),
    ],
    D=[
        arith("Un curso de 36 estudiantes revisó sus perfiles: 15 los tenían públicos y pasaron 11 a privado. ¿Cuántos siguen públicos?", "15-11", "Se restan los que cambiaron."),
        arith("Una clave de 8 caracteres se alarga a una frase que tiene el triple de caracteres. ¿Cuántos caracteres tiene la frase?", "8*3", "Se multiplican por 3 los caracteres de la clave corta."),
    ],
    context=[ex("En Orientación, Matías dice que su cuenta es pública porque «así tiene más amigos». ¿Qué dos riesgos puedes nombrarle?", "Engaños y acoso por parte de desconocidos", "Una cuenta pública permite que cualquiera lo contacte.")],
    selfcheck=[ex("En Orientación: ¿una clave larga y distinta es más segura?", "Sí", "Es más difícil de adivinar."), ex("¿Un perfil privado reduce quién ve tu contenido?", "Sí", "Solo lo ven quienes aceptas."), ex("¿Puedes compartir tu clave con tu pareja?", "No", "Las claves no se comparten.")],
    task=T("Lee las cuentas de ejemplo de Sofía y Diego, inventados: Sofía tiene perfil público, acepta a cualquiera, usa «sofia2011» en todas sus cuentas y comparte su ubicación; Diego tiene perfil privado, acepta a quienes conoce, usa claves largas distintas y desactiva la ubicación. Haz una tabla con cuatro medidas, qué hace cada uno y cuál es la consecuencia más probable.", "Perfil: Sofía público, riesgo de engaños; Diego privado. Solicitudes: Sofía acepta a cualquiera, riesgo de acoso. Claves: Sofía usa una débil repetida, riesgo de robo; Diego usa fuertes. Ubicación: Sofía la comparte y se la puede ubicar; Diego la desactiva.", ["compara cuatro medidas", "describe una consecuencia por medida", "usa los datos del caso", "no cuenta datos propios"], ["tabla de comparación"], ["no ver las consecuencias", "creer que lo público es inofensivo"], "Reconoce las comparaciones y pregunta qué cambiaría Sofía primero."),
    reinforce="Escribe una clave fuerte de ejemplo para un personaje de cuento, con una frase y un número.",
    extend="Explica por qué una decisión de seguridad reduce riesgos antes de que ocurran.",
)

lesson(
    OA4, 4,
    "Una hoja y un lápiz. Los mensajes del caso están escritos en los ejercicios; no contienen contenido explícito. Los personajes son inventados.",
    "Aprenderé a reconocer las señales de grooming y a elegir una acción segura cuando un adulto desconocido contacta a una persona menor en línea. Sirve para resguardar mi intimidad y mi integridad.",
    ["Sé qué datos son privados.", "Sé que debo avisar a un adulto de confianza ante un riesgo."],
    [
        "El grooming es cuando una persona adulta contacta a un niño, niña o adolescente por internet, se gana su confianza y después busca engañarlo o abusar de él. Suele hacerse pasar por alguien de su edad, regalar cosas, elogiar mucho, pedir secretos y pedir fotos o encuentros. Es un delito grave. La responsabilidad nunca es de quien fue contactado.",
        "Señales de alerta: una persona desconocida que te escribe mucho y te hace sentir especial; te pide que guardes el secreto; te pide fotos, videos o datos personales; te ofrece regalos o dinero; te propone un encuentro o te lleva a otra aplicación más privada. Si ves una de estas señales, detente.",
        "La acción segura tiene pasos: no respondas más, no envíes nada, no te juntes con esa persona, guarda capturas de pantalla como evidencia, bloquea la cuenta (primero las capturas y después el bloqueo, para no perder los mensajes) y cuéntaselo de inmediato a una persona adulta de confianza. Si en el chat hay imágenes íntimas, no las guardes ni las reenvíes, y no borres el chat: muéstraselo a la persona adulta. No la confrontes, no la amenaces ni intentes resolverlo solo. Si te sientes asustado o culpable, recuerda que no hiciste nada malo y que pedir ayuda es lo correcto.",
    ],
    [("grooming", "engaño de una persona adulta a un menor por internet para ganar su confianza y dañarlo"), ("señal de alerta", "indicio de que algo no es seguro"), ("evidencia", "prueba que muestra lo ocurrido, como una captura de pantalla"), ("bloquear", "impedir que una cuenta nos contacte"), ("delito", "acto que la ley castiga")],
    [
        W("Reconocer señales", "Una cuenta que dice ser «de 14 años» le escribe todos los días a Camila, le dice que es «especial», le pide que no cuente a nadie y que le envíe una foto. ¿Hay señales de grooming?", ["Le pide que guarde el secreto.", "Le pide una foto.", "Le hace sentir especial."], "Sí: secreto, foto y trato especial"),
        W("Elegir la acción segura", "Camila no ha enviado nada. ¿Qué hace, en orden?", ["No responde más.", "Guarda capturas y bloquea.", "Avisa a una persona adulta de confianza."], "No responder, guardar capturas, bloquear y avisar a una persona adulta"),
    ],
    [
        M("Creer que quien lo contactó «es de mi edad» solo porque lo dice.", "Se cree lo que dice una cuenta que no se puede comprobar.", "En internet cualquiera puede mentir sobre quién es."),
        M("Pensar que hay que confrontar a la persona para que pare.", "Se quiere resolver solo.", "No confrontes: bloquea y cuéntaselo a un adulto de confianza."),
    ],
    R=[
        ex("Una persona desconocida que te pide guardar un secreto, ¿es una señal de alerta, sí o no?", "Sí", "Un secreto sobre una conversación es típico del grooming."),
        ex("Si alguien te pide fotos, ¿las envías o avisas a un adulto?", "Avisas a un adulto", "Enviarlas te expone y avisar te protege."),
        ex("¿La responsabilidad es de quien fue contactado, sí o no?", "No", "Es de quien engaña."),
    ],
    U=[
        ex("¿Por qué guardar capturas de pantalla ayuda? A) Porque muestran lo ocurrido a quien debe actuar. B) Porque permiten seguir hablando con esa persona.", "A", "Son evidencia de lo ocurrido."),
        ex("¿Un regalo o dinero de un desconocido por internet es una señal de alerta, sí o no?", "Sí", "Es una forma de ganar confianza."),
        ex("Si te propone encontrarse en persona, ¿es seguro aceptar, sí o no?", "No", "Un encuentro con un desconocido es muy riesgoso."),
    ],
    A=[
        ex("Camila recibe: 1) «¿Cómo estás?» de una amiga del curso; 2) «Eres tan madura, no se lo cuentes a nadie» de un desconocido; 3) «¿Estudiamos?» de un compañero; 4) «Te mando regalos si me das tu dirección» de un desconocido. ¿Cuáles son señales de grooming?", "2 y 4", "Piden secreto y datos a cambio de regalos."),
        ex("Una cuenta desconocida pide una foto a Pía. ¿Qué conviene? A) Bloquearla, guardar capturas y avisar a un adulto. B) Hacerle preguntas para ver si miente.", "A", "No sigue el contacto y pide ayuda."),
        ex("Tomás ya envió una foto antes de darse cuenta. ¿Qué debe hacer ahora?", "Contárselo a una persona adulta de confianza, sin borrar el chat", "Debe pedir ayuda; no es culpa suya y la conversación sirve de prueba."),
    ],
    Z=[
        ex("Un joven dice: «Si cuento, me van a retar». ¿Qué le responderías?", "Que no hizo nada malo y que pedir ayuda lo protege", "La responsabilidad es de quien engaña."),
        ex("¿Por qué no se debe confrontar a la persona que hace grooming?", "Porque puede aumentar el riesgo y destruir pruebas", "Un adulto puede actuar con protocolos y proteger."),
    ],
    D=[
        arith("En un curso de 32 estudiantes, 20 conocían el grooming y el resto no. ¿Cuántos no lo conocían?", "32-20", "Al total se le restan los que sí lo conocían."),
        arith("Un protocolo tiene 5 pasos y el curso lo ensaya con 6 casos. ¿Cuántos pasos ensaya en total?", "5*6", "Se multiplican los pasos por los casos."),
    ],
    context=[ex("Lucía recibe mensajes de una cuenta que dice ser una modelo de 15 años que le ofrece dinero por «fotos especiales». ¿Qué acciones seguras corresponden, en orden?", "No responder, no enviar nada, guardar capturas, bloquear y avisar a un adulto", "Evita el riesgo y activa la ayuda.")],
    selfcheck=[ex("En Orientación: ¿el grooming es un engaño de un adulto a un menor?", "Sí", "Es su definición."), ex("¿Debes guardar capturas y avisar a un adulto?", "Sí", "Sirve para protegerte."), ex("¿Debes encontrarte con esa persona?", "No", "Es muy riesgoso.")],
    task=T("Lee el caso inventado de Emilia: una cuenta nueva le escribe, dice ser de su edad, le regala pases para un juego en línea, le pide su dirección «para mandarle un regalo» y que no se lo cuente a nadie. Escribe un cuadro con tres columnas: señales de alerta del caso, qué NO hace Emilia y qué SÍ hace (en orden).", "Señales: regalos, pide dirección, pide secreto. No: responder, enviar datos, juntarse. Sí: guardar capturas, bloquear, avisar a una persona adulta de confianza.", ["identifica al menos tres señales", "indica lo que no debe hacer", "ordena las acciones seguras", "no cuenta nada personal"], ["cuadro de tres columnas"], ["confrontar", "pensar que es culpa de Emilia"], "Reconoce los pasos y pregunta cómo se lo contaría a la persona adulta."),
    reinforce="Escribe tres señales de alerta de grooming y una acción para cada una.",
    extend="Explica por qué en internet no se puede confiar en lo que dice una cuenta sobre su edad.",
)

lesson(
    OA4, 5,
    "Una hoja y un lápiz. El plan semanal de ejemplo y el mensaje del caso están escritos en los ejercicios. Los personajes son inventados.",
    "Aprenderé a armar un plan semanal de bienestar, a acordar reglas de uso de pantallas con mi familia y a pedir ayuda por situaciones en línea. Sirve para mantener hábitos saludables y comunicar lo que me incomoda.",
    ["Sé qué hábitos cuidan mi salud.", "Sé qué hacer ante señales de riesgo en línea."],
    [
        "Un plan semanal de bienestar fija metas pequeñas y medibles para alimentación, descanso, actividad física y uso de pantallas. Por ejemplo: dormir a las 22:30 de lunes a jueves, caminar 20 minutos cada día y dejar el celular fuera de la cama. Se revisa al final de la semana: ¿lo cumplí? ¿Qué ajusto?",
        "Para cuidarte en línea también conviene acordar reglas en casa con una persona adulta: horarios de uso, qué aplicaciones usar, quién puede ser contacto y qué hacer si algo te incomoda. Acordar no es perder libertad: es tener un camino claro y un apoyo si algo falla. Cuando algo te incomode en línea, avisa pronto con un mensaje claro: «Me pasó algo en línea que me incomoda; ¿podemos conversar?».",
        "Tu bienestar también se cuida en el colegio. Un curso puede proponer recreos activos, un kiosco con opciones saludables, un acuerdo para no grabar a compañeros sin permiso y un espacio para conversar sobre lo digital. Proponer con datos y respeto, y escuchar a otros, fortalece la convivencia y la vida saludable de toda la comunidad.",
    ],
    [("plan semanal", "organización de metas pequeñas para siete días"), ("meta medible", "meta que se puede contar o comprobar"), ("regla de uso", "acuerdo sobre cómo usar las pantallas"), ("revisar", "mirar al final qué se cumplió y qué se ajusta"), ("convivencia", "forma de relacionarse en una comunidad")],
    [
        W("Revisar un plan", "Meta: caminar 20 minutos por día durante 5 días. Resultado: 4 días de 20 minutos. ¿Cuántos minutos caminó y cuántos le faltaron?", ["4 días por 20 minutos son 80 minutos.", "La meta era 5 por 20, es decir, 100 minutos.", "Le faltaron 100 − 80 = 20 minutos."], "Caminó 80 minutos y le faltaron 20"),
        W("Redactar un aviso", "Mateo vio un mensaje raro en línea y le incomoda. Escribe su aviso a un adulto en tres partes.", ["Dice que le pasó algo en línea.", "Dice que le incomoda.", "Pide conversar."], "«Me pasó algo en línea que me incomoda; ¿podemos conversar?»"),
    ],
    [
        M("Fijar metas imposibles, como «hacer deporte dos horas diarias desde mañana».", "Se quiere cambiarlo todo de golpe.", "Empieza con metas pequeñas y revísalas cada semana."),
        M("Creer que acordar reglas en casa es perder libertad.", "Se ve la regla solo como prohibición.", "El acuerdo da claridad y apoyo."),
    ],
    R=[
        ex("Una meta medible, ¿se puede contar o es solo un deseo vago?", "Se puede contar", "Una meta medible tiene una cantidad o un hecho comprobable."),
        ex("¿El plan semanal se revisa al final de la semana, sí o no?", "Sí", "Revisar permite ajustar."),
        ex("Acordar reglas de uso en casa, ¿da un camino claro o quita todo apoyo?", "Da un camino claro", "Un acuerdo ayuda a saber qué hacer."),
    ],
    U=[
        ex("¿Qué meta es medible? A) Dormir a las 22:30 de lunes a jueves. B) Dormir mejor.", "A", "Tiene hora y días."),
        ex("Si algo te incomoda en línea, ¿avisas pronto o esperas semanas?", "Avisas pronto", "Avisar a tiempo evita que el problema crezca."),
        ex("Un kiosco con opciones saludables, ¿beneficia a toda la comunidad escolar, sí o no?", "Sí", "Aumenta las opciones para todos."),
    ],
    A=[
        ex("Plan de Camila: lunes 20 minutos de caminata, martes 20, miércoles 0, jueves 20, viernes 20. ¿Cumplió los 5 días?", "No", "El miércoles no hizo la actividad."),
        ex("Marta debe acordar reglas de pantallas con una persona de su casa. ¿Qué punto conviene incluir? A) Qué hacer si algo le incomoda en línea. B) Cuántos juegos tiene.", "A", "Un acuerdo claro cubre cómo actuar ante el riesgo."),
        ex("Un curso propone «no grabar a compañeros sin su permiso». ¿Qué derecho protege?", "El derecho sobre la imagen", "Evita que usen su imagen sin consentimiento."),
    ],
    Z=[
        ex("Explica por qué revisar el plan cada semana ayuda a mejorarlo.", "Porque muestra qué se cumplió y qué ajustar", "Con datos se pueden hacer cambios realistas."),
        ex("Un estudiante dice: «No pido ayuda porque me quitarán el celular». ¿Qué le responderías?", "Que avisar protege y que un acuerdo puede cuidar el uso", "Su bienestar es más importante que perder el celular un tiempo."),
    ],
    D=[
        arith("Un estudiante se propone dormir 9 horas por noche durante 6 noches. ¿Cuántas horas de sueño suma en total?", "9*6", "Se multiplican las horas por las noches."),
        arith("Un curso de 33 estudiantes votó por propuestas: 14 para recreos activos, 12 para kiosco saludable y el resto para un taller. ¿Cuántos votaron por el taller?", "33-14-12", "Al total se le restan los otros votos."),
    ],
    context=[ex("En el Consejo de Curso, Valentina propone un acuerdo: «no grabaremos en el colegio sin permiso». Rafael dice que es exagerado. ¿Qué argumento a favor puede dar Valentina?", "Que protege la imagen y la privacidad de todos", "Todos tienen derecho a no ser grabados sin permiso.")],
    selfcheck=[ex("En Orientación: ¿una meta medible se puede contar?", "Sí", "Tiene cantidades o hechos."), ex("¿Conviene avisar pronto si algo te incomoda en línea?", "Sí", "Se evita que crezca."), ex("¿El bienestar se cuida solo en lo personal?", "No", "También en la comunidad escolar.")],
    task=T("Lee los datos de Nicolás, un estudiante inventado: duerme tarde, usa el celular en la cama, camina poco y no sabe qué hacer si le escribe un desconocido. Escribe un plan de 7 días con tres metas medibles (una de descanso, una de actividad y una de seguridad digital) y un mensaje de tres partes para avisar a una persona adulta si algo le incomoda en línea.", "Descanso: dejar el celular fuera de la cama de lunes a viernes. Actividad: caminar 20 minutos 5 días. Digital: no responder a desconocidos y avisar. Mensaje: «Me escribió alguien desconocido y me incomoda; ¿podemos conversar?».", ["tres metas medibles", "mensaje de tres partes", "incluye revisión al final de la semana", "no cuenta nada personal"], ["plan escrito"], ["metas vagas", "mensaje sin pedido"], "Valora las metas medibles y pregunta cómo revisará el plan."),
    reinforce="Escribe una meta medible de descanso y otra de actividad física para un personaje de cuento.",
    extend="Explica por qué las reglas acordadas en casa ayudan a usar las redes con seguridad.",
)
