"""Cuaderno del estudiante, 7.º básico Orientación: OA 03 (riesgos y presión social) y OA 04 (bienestar y vida saludable)."""
from __future__ import annotations

from student_content_or7_a import M, T, W, lesson
from student_lessons import arith, ex

OA3, OA4 = "OR07 OA 03", "OR07 OA 04"

# ================================================================ OA 03
lesson(
    OA3, 1,
    "Una hoja y un lápiz. El caso de la fiesta de Joaquín, un estudiante inventado, y la lista de situaciones están escritos en los ejercicios. No cuentes nada personal.",
    "Aprenderé a reconocer situaciones que pueden exponer a adolescentes al consumo de sustancias, a conductas sexuales riesgosas o a la violencia. Sirve para anticipar el riesgo y decidir con tiempo.",
    ["Sé que mi cuerpo es mío y que puedo poner límites.", "Sé que hay fuentes de información confiables."],
    [
        "Un riesgo es la posibilidad de que algo dañe tu salud, tu seguridad o la de otros. En la adolescencia hay situaciones que pueden exponer a tres tipos de riesgo. El primero es el consumo de sustancias nocivas, como alcohol, tabaco, vapeadores u otras drogas. El segundo son las conductas sexuales riesgosas, como presionar o ser presionado, o tomar decisiones sin información ni cuidado. El tercero son las conductas violentas: peleas, acoso, amenazas o grabar y difundir agresiones.",
        "Los riesgos aumentan en ciertas situaciones: reuniones sin adultos, grupos que presionan, chats con desconocidos, lugares aislados o momentos en que te sientes excluido y quieres encajar. Se llaman factores de riesgo. También existen factores protectores, que disminuyen el riesgo: tener adultos de confianza, un proyecto que te motive, amigos que respetan tus decisiones, conocer las consecuencias y saber decir que no.",
        "Reconocer el riesgo no significa tener miedo de todo. Significa darte cuenta a tiempo para elegir con calma. En el caso de Joaquín, un estudiante inventado, lo invitan a una reunión en una casa sin adultos donde habrá alcohol, un grupo graba peleas y un mayor de 18 años le escribe para que se encuentren. Hay tres riesgos distintos y varios factores que se pueden detectar antes de ir.",
    ],
    [("riesgo", "posibilidad de que algo dañe la salud o la seguridad"), ("factor de riesgo", "situación que aumenta la posibilidad de daño"), ("factor protector", "situación o recurso que disminuye la posibilidad de daño"), ("sustancia nociva", "sustancia que daña el organismo"), ("conducta violenta", "acción que daña a otra persona con golpes, amenazas o humillaciones")],
    [
        W("Clasificar un riesgo", "En el caso de Joaquín, un grupo graba peleas entre estudiantes para subirlas a redes. ¿Qué tipo de riesgo es?", ["Las peleas son agresiones.", "Grabarlas y difundirlas las multiplica.", "Es una conducta violenta."], "Una conducta violenta"),
        W("Distinguir factor de riesgo y factor protector", "Joaquín tiene un entrenamiento de básquetbol que le gusta, y la reunión es sin adultos. ¿Cuál es factor protector y cuál de riesgo?", ["El entrenamiento le da un proyecto y buenos hábitos: protege.", "Una reunión sin adultos y con alcohol aumenta el riesgo.", "Se diferencian por lo que disminuye o aumenta el daño posible."], "Protector: el entrenamiento. De riesgo: la reunión sin adultos"),
    ],
    [
        M("Pensar que reconocer un riesgo es tenerle miedo a todo.", "Se confunde ser cuidadoso con ser temeroso.", "Reconocerlo a tiempo permite elegir con calma."),
        M("Creer que el riesgo solo existe cuando hay desconocidos.", "Se piensa que las personas conocidas no pueden presionar.", "La presión puede venir de amigos o conocidos."),
    ],
    R=[
        ex("El consumo de alcohol, ¿es un riesgo por sustancias o por conducta violenta?", "Por sustancias", "El alcohol es una sustancia nociva para adolescentes."),
        ex("Una reunión sin adultos donde hay alcohol, ¿es un factor de riesgo o un factor protector?", "Un factor de riesgo", "Aumenta la posibilidad de daño."),
        ex("Tener un adulto de confianza con quien conversar, ¿es un factor de riesgo o protector?", "Un factor protector", "Disminuye la posibilidad de daño porque hay quien ayude."),
    ],
    U=[
        ex("¿Por qué un chat con un desconocido mayor puede ser un riesgo?", "Porque puede buscar engañar o dañar a un menor", "No se sabe quién es ni qué intenciones tiene."),
        ex("¿Qué diferencia hay entre un factor de riesgo y uno protector?", "El de riesgo aumenta el daño y el protector lo disminuye", "Cada uno cambia la probabilidad de daño en un sentido distinto."),
        ex("¿Estar excluido y querer encajar puede aumentar el riesgo, sí o no?", "Sí", "Se acepta lo que otros proponen para no quedar fuera."),
    ],
    A=[
        ex("Situaciones: 1) fiesta sin adultos con alcohol; 2) entrenar en un club con entrenador; 3) un mayor pide verlo a solas por chat; 4) conversar con la orientadora. ¿Cuántas son factores de riesgo?", "2", "La 1 y la 3 aumentan el riesgo; la 2 y la 4 protegen."),
        ex("Un grupo graba una pelea y la sube. ¿Qué tipo de riesgo suma además de la violencia? A) Difusión que humilla y se queda en internet. B) Que la pelea sea más segura porque hay testigos.", "A", "La grabación multiplica el daño y no se puede borrar del todo."),
        ex("Joaquín nota que en la reunión habrá alcohol y no habrá adultos. ¿Qué hace en el momento de decidir si va? A) Piensa en los riesgos antes de ir. B) Decide al llegar sin pensar.", "A", "Anticipar permite elegir con calma."),
    ],
    Z=[
        ex("Marcelo dice: «Solo los desconocidos son peligrosos». ¿Qué error hay?", "La presión también puede venir de conocidos", "Los riesgos aparecen con cualquiera que presione o proponga algo dañino."),
        ex("¿Por qué conviene identificar los factores de riesgo antes de ir a un lugar y no después?", "Porque permite decidir con calma", "Al estar en medio de la presión es más difícil pensar."),
    ],
    D=[
        arith("En un listado de 15 situaciones, 6 son de sustancias, 5 de violencia y el resto de conductas sexuales riesgosas. ¿Cuántas son de conductas sexuales riesgosas?", "15-6-5", "Al total se le restan las de los otros dos tipos."),
        ex("Una compañera dice: «Si hay un adulto que sabe dónde estoy, igual da lo mismo si hay alcohol». ¿Es correcto?", "No", "Un adulto que sabe dónde estás es protector, pero el alcohol sigue siendo un riesgo."),
    ],
    context=[ex("Una compañera cuenta que en su barrio hay una plaza donde los fines de semana se junta un grupo a beber. A ella la invitaron varias veces. ¿Qué es lo primero que le conviene hacer?", "Reconocer el riesgo y decidir de antemano no ir sin un adulto de confianza", "Anticipar la situación permite decidir antes de estar bajo presión.")],
    selfcheck=[ex("En Orientación: ¿los factores de riesgo aumentan la posibilidad de daño?", "Sí", "Por eso hay que identificarlos."), ex("¿Los factores protectores ayudan a disminuir el riesgo?", "Sí", "Por ejemplo un adulto de confianza."), ex("¿La presión puede venir de personas conocidas?", "Sí", "No solo de desconocidos.")],
    task=T("Lee el caso de Bastián, un estudiante inventado: lo invitan a una salida sin adultos el sábado; llevarán alcohol y vapeadores; un compañero dice que «grabarán una pelea de curso»; un chat de un mayor le propone verse a solas. Escribe tres factores de riesgo, clasificados por tipo, y dos factores protectores que Bastián podría usar.", "Riesgos: salida sin adultos con alcohol y vapeadores (sustancias); grabar una pelea (violencia); mayor que propone verse a solas (riesgo sexual o de engaño). Protectores: avisar a un adulto de confianza y quedarse en un lugar con adultos.", ["identifica tres factores de riesgo", "los clasifica por tipo", "propone dos factores protectores", "no cuenta nada personal"], ["texto escrito", "tabla de dos columnas"], ["no clasificar el riesgo", "olvidar los factores protectores"], "Reconoce lo identificado y pregunta qué factor protector sería más fácil de usar para Bastián."),
    reinforce="Anota tres situaciones de riesgo de un personaje de película y clasifícalas por tipo.",
    extend="Explica por qué tener un proyecto que te motive puede ser un factor protector.",
)

lesson(
    OA3, 2,
    "Una hoja y un lápiz. El caso de Ema y la tabla de mitos están escritos en los ejercicios.",
    "Aprenderé a separar hechos, emociones y derechos frente a la presión de un grupo, y a distinguir mitos de hechos sobre sustancias. Sirve para decir que no sin perder mi lugar y mis derechos.",
    ["Sé reconocer factores de riesgo y factores protectores.", "Sé que mi cuerpo es mío."],
    [
        "La presión social es la influencia de un grupo para que hagas algo que no quieres. Puede ser directa («pruébalo, no seas aburrida») o indirecta (ver que todos lo hacen). Cuando la sientes, es normal que aparezcan emociones como miedo a quedar fuera, nerviosismo o ganas de encajar. Esas emociones son reales, pero no te obligan a actuar. Tienes derecho a decidir sobre tu cuerpo y tu salud, y a decir «no» sin dar explicaciones largas. Si la presión te da miedo, no hace falta discutir: puedes irte y avisar a un adulto de confianza.",
        "Conviene separar los hechos de los mitos. Un hecho: el alcohol afecta la coordinación y el juicio, y la venta de alcohol y tabaco a menores de 18 años está prohibida en Chile. Otro hecho: el tabaco y los vapeadores con nicotina generan dependencia, es decir, el cuerpo la pide y cuesta dejarla. Otro: el cerebro de un adolescente sigue en desarrollo, por eso las sustancias pueden afectar más la atención, la memoria y el aprendizaje. Un mito: «todos lo hacen». No todos lo hacen, y que otros lo hagan no lo vuelve seguro.",
        "Tampoco es verdad que quien consume sea una mala persona. Hay personas que necesitan ayuda y no juicio. Y en las relaciones sexuales, la presión es una señal de alerta: nadie debería hacerte sentir culpable por no querer. Tienes derecho a esperar, a decidir con información y a pedir orientación al personal de salud.",
    ],
    [("presión social", "influencia de un grupo para que alguien haga algo que no quiere"), ("mito", "idea falsa que mucha gente repite"), ("dependencia", "necesidad del cuerpo de seguir consumiendo y dificultad para dejarlo"), ("nicotina", "sustancia del tabaco y de muchos vapeadores que genera dependencia"), ("juicio", "capacidad de pensar con claridad y decidir bien")],
    [
        W("Separar hecho y mito", "Ema, una estudiante inventada, escucha: «Todos en el curso prueban un vapeador». ¿Es un hecho o un mito?", ["«Todos» es una exageración.", "Que otros lo hagan no lo vuelve seguro.", "Es un mito."], "Un mito"),
        W("Reconocer la emoción", "Ema siente miedo a quedar fuera si dice que no. ¿Esa emoción la obliga a aceptar?", ["La emoción es real.", "Pero una emoción no es una orden.", "Tiene derecho a decidir."], "No, puede sentir miedo y decidir que no"),
    ],
    [
        M("Pensar que si todos lo hacen, no puede ser tan malo.", "Se confunde la cantidad de personas con la seguridad.", "Algo dañino lo es aunque muchos lo hagan; además, no todos lo hacen."),
        M("Creer que decir que no obliga a dar una larga explicación.", "Se cree que necesito justificarme ante el grupo.", "Basta con decir «no, gracias»."),
    ],
    R=[
        ex("«El alcohol afecta la coordinación y el juicio». ¿Es un hecho o un mito?", "Un hecho", "Es un efecto conocido del alcohol."),
        ex("«Todos lo hacen». ¿Es un hecho o un mito?", "Un mito", "No todos lo hacen y no lo vuelve seguro."),
        ex("¿Tienes derecho a decir que no sin dar explicaciones largas, sí o no?", "Sí", "Es un derecho sobre tu cuerpo y tu salud."),
    ],
    U=[
        ex("¿Por qué el cerebro adolescente puede verse más afectado por las sustancias?", "Porque todavía está en desarrollo", "Puede afectarse la atención, la memoria y el aprendizaje."),
        ex("¿La nicotina genera dependencia, sí o no?", "Sí", "El cuerpo la pide y cuesta dejarla."),
        ex("Sentir miedo a quedar fuera, ¿obliga a aceptar lo que propone el grupo?", "No", "Una emoción no es una orden."),
    ],
    A=[
        ex("Frases: 1) «Todos lo hacen»; 2) «La venta de alcohol a menores de 18 está prohibida»; 3) «Una vez no pasa nada»; 4) «La nicotina genera dependencia». ¿Cuántas son mitos?", "2", "La 1 y la 3 son mitos; la 2 y la 4 son hechos."),
        ex("Un compañero dice: «Si no lo pruebas, eres un cobarde». ¿Cuál respuesta es firme y respetuosa? A) «No, gracias. Yo decido sobre mi cuerpo». B) «Está bien, lo hago para que no se enojen».", "A", "Dice que no sin agredir ni justificarse."),
        ex("Ema siente presión por decir que sí a algo sexual con un compañero. ¿Qué derecho tiene?", "A decidir esperar y no sentir culpa", "Nadie debe presionar a otra persona por su cuerpo."),
    ],
    Z=[
        ex("Gonzalo dice: «Quien consume es mala persona y hay que evitarla». ¿Qué error hay?", "Juzga a la persona en vez de ver que puede necesitar ayuda", "Las personas pueden necesitar ayuda y no solo juicio."),
        ex("¿Por qué «una sola vez» no es una razón para probar?", "Porque algunas sustancias generan dependencia o dañan el cerebro", "El daño no depende de que sea la primera vez."),
    ],
    D=[
        arith("De 40 estudiantes ficticios encuestados, 31 dijeron que no consumirían nunca. ¿Cuántos no dijeron eso?", "40-31", "Al total se le restan los que sí lo dijeron."),
        arith("Ema repasó 3 mitos por día durante 4 días. ¿Cuántos mitos repasó?", "3*4", "Se multiplican mitos por días."),
    ],
    context=[ex("En un cumpleaños, alguien dice: «El que no tome una cerveza no es parte del grupo». Julián no quiere. ¿Qué puede decir con firmeza?", "«No, gracias»", "Basta con rechazar sin dar explicaciones largas.")],
    selfcheck=[ex("En Orientación: ¿puedo decir que no aunque el grupo insista?", "Sí", "Es mi derecho."), ex("¿«Todos lo hacen» es un hecho?", "No", "Es un mito."), ex("¿Sentir miedo a quedar fuera es normal?", "Sí", "Es una emoción común, pero no decide por mí.")],
    task=T("Lee las frases inventadas que oye Mateo: «todos lo hacen», «probar una vez no daña», «tomar alcohol te hace más grande», «la venta a menores está prohibida». Escribe cuáles son mitos y cuáles hechos, una respuesta firme y respetuosa para la presión y la emoción que podría sentir.", "Mitos: las tres primeras. Hecho: la cuarta. Respuesta: «No, gracias; yo decido». Emoción: miedo a quedar fuera.", ["distingue mitos y hechos", "escribe una respuesta firme", "nombra la emoción", "no cuenta nada personal"], ["lista"], ["creer que hay que dar muchas explicaciones", "confundir hechos con mitos"], "Reconoce el análisis y pregunta qué otro argumento daría a un compañero."),
    reinforce="Escribe dos mitos sobre sustancias y una frase que los corrija.",
    extend="Explica por qué la presión puede venir de amigos y no solo de desconocidos.",
)

lesson(
    OA3, 3,
    "Una hoja y un lápiz. El caso de Rafael y las tarjetas de opciones están escritos en los ejercicios.",
    "Aprenderé a comparar opciones frente a una presión y a anticipar consecuencias a corto y a largo plazo. Sirve para elegir con visión y no solo por impulso.",
    ["Sé separar hechos, emociones y mitos.", "Sé que puedo decir que no."],
    [
        "Cada decisión tiene consecuencias. Algunas llegan pronto, que se llaman de corto plazo, como el aplauso del grupo o una molestia. Otras llegan más tarde, de largo plazo, como una dependencia, un problema de salud, una sanción o perder la confianza de tu familia. Para comparar opciones conviene mirar ambas. Una opción que alivia hoy puede traer un problema grande mañana.",
        "Ante una presión puedes: aceptar, ceder a medias, decir que no con firmeza, proponer otra actividad, irte o avisar a un adulto. Por ejemplo, si te invitan a probar un vapeador, aceptar puede dar aprobación inmediata pero expone a la dependencia. Decir «no, gracias» puede traer una burla breve, pero protege tu salud y tu autonomía. Proponer otra actividad, como jugar fútbol, puede cambiar el rumbo del grupo.",
        "En situaciones de violencia también hay opciones. Participar en una pelea o grabarla da atención, pero hace daño a otros y puede traer sanciones escolares y legales. Alejarte y avisar a un adulto protege a todos. Y ante la presión sexual, decir «no estoy listo» y hablar con un adulto de confianza protege tu integridad. Elegir la opción más segura no es cobardía: es valentía.",
    ],
    [("corto plazo", "lo que ocurre pronto después de una decisión"), ("largo plazo", "lo que ocurre mucho tiempo después de una decisión"), ("sanción", "castigo por una conducta que daña a otros"), ("autonomía", "capacidad de decidir por uno mismo"), ("alternativa", "otra opción posible")],
    [
        W("Comparar plazos", "A Rafael, un estudiante inventado, le ofrecen un vapeador. Aceptar da aprobación del grupo hoy. ¿Cuál es una consecuencia de largo plazo?", ["La aprobación es de corto plazo.", "La nicotina genera dependencia con el tiempo.", "Esa es de largo plazo."], "Puede generar dependencia"),
        W("Elegir la opción más segura", "Rafael ve que un grupo se prepara para pelear y grabar. Puede (a) mirar, (b) grabar, (c) alejarse y avisar a un adulto. ¿Cuál protege a todos?", ["Mirar o grabar mantiene la pelea.", "Alejarse y avisar puede detenerla.", "La tercera es más segura."], "Alejarse y avisar a un adulto"),
    ],
    [
        M("Elegir solo por lo que pasa hoy.", "Se ignoran los efectos de largo plazo.", "Mira consecuencias de corto y de largo plazo."),
        M("Pensar que alejarme de una pelea es cobardía.", "Se confunde valentía con mostrarse fuerte.", "Alejarse y avisar protege a las personas."),
    ],
    R=[
        ex("La aprobación del grupo hoy, ¿es una consecuencia de corto o de largo plazo?", "De corto plazo", "Ocurre pronto después de la decisión."),
        ex("La dependencia a la nicotina, ¿es una consecuencia de corto o de largo plazo?", "De largo plazo", "Aparece con el tiempo."),
        ex("Proponer jugar fútbol en vez de beber, ¿es una alternativa o es aceptar la presión?", "Una alternativa", "Es otra opción para cambiar el rumbo."),
    ],
    U=[
        ex("¿Por qué conviene mirar tanto el corto como el largo plazo?", "Porque lo que alivia hoy puede dañar mañana", "Una opción puede tener buenas consecuencias pronto y malas después."),
        ex("¿Alejarse de una pelea y avisar a un adulto es una opción valiente o cobarde?", "Valiente", "Protege a todos y detiene el daño."),
        ex("Si participas en una pelea grabada, ¿puede haber sanciones, sí o no?", "Sí", "Dañar a otros puede traer sanciones escolares y legales."),
    ],
    A=[
        ex("Opciones ante una invitación a probar alcohol: 1) aceptar; 2) decir «no, gracias»; 3) proponer jugar fútbol; 4) irse y avisar a un adulto. ¿Cuántas protegen su salud?", "3", "Las opciones 2, 3 y 4 evitan consumir; la 1 lo expone."),
        ex("Una pareja ficticia presiona a Rafael para dar un paso sexual. Opciones: A) Decir «no estoy listo» y hablar con un adulto de confianza. B) Aceptar para que no se enoje.", "A", "Protege su integridad y respeta su ritmo."),
        ex("Rafael pregunta qué consecuencia de largo plazo tiene decir una mentira para encajar. ¿Cuál es? A) Perder la confianza de otros. B) Que la mentira deje de importar con el tiempo.", "A", "La confianza se pierde cuando se descubre la mentira."),
    ],
    Z=[
        ex("Pía dice: «Si cedo una vez, después me dejarán en paz». ¿Qué problema tiene ese razonamiento?", "Que ceder puede aumentar la presión", "Aceptar una vez muestra que la presión funciona y la repite."),
        ex("¿Por qué proponer una alternativa puede ser más efectiva que solo decir que no?", "Porque cambia el rumbo del grupo", "Ofrece algo distinto y evita quedar aislado."),
    ],
    D=[
        arith("Una tabla ficticia muestra 5 opciones, cada una con 2 consecuencias de corto plazo y 2 de largo plazo. ¿Cuántas consecuencias hay en total?", "5*(2+2)", "Se suman las consecuencias de cada opción y se multiplica por 5."),
        arith("De 18 opciones evaluadas por el curso, 11 fueron seguras. ¿Cuántas no lo fueron?", "18-11", "Al total se le restan las seguras."),
    ],
    context=[ex("En un grupo de mensajes, un compañero reta: «Quien no suba un video de la pelea es un cobarde». Paulina decide no subirlo y avisar a la orientadora. ¿Cuál es una consecuencia positiva de largo plazo de su decisión?", "Proteger a las personas y evitar sanciones", "Detener la difusión evita daño a los demás y problemas posteriores.")],
    selfcheck=[ex("En Orientación: ¿conviene pensar en las consecuencias de largo plazo?", "Sí", "Ayudan a decidir mejor."), ex("¿Una alternativa puede cambiar el rumbo del grupo?", "Sí", "Ofrece otra actividad."), ex("¿Alejarse de una pelea es cobardía?", "No", "Es una decisión segura y valiente.")],
    task=T("Lee el caso inventado de Ignacia: en una plaza, un grupo le ofrece fumar y le dice que si no lo hace «no es del grupo». Completa un cuadro con tres opciones (aceptar, decir no con firmeza, proponer otra actividad), su consecuencia de corto plazo y su consecuencia de largo plazo. Luego elige una y explica por qué.", "Aceptar: corto, aprobación; largo, dependencia. Decir no: corto, burla breve; largo, cuida su salud. Alternativa: corto, cambia el rumbo; largo, amigos que respetan. Elige decir no o la alternativa.", ["completa el cuadro con tres opciones", "incluye corto y largo plazo", "elige y justifica", "no cuenta nada personal"], ["cuadro escrito"], ["mirar solo el corto plazo", "no justificar"], "Reconoce el cuadro y pregunta qué otra alternativa agregaría."),
    reinforce="Escribe una decisión de un personaje con una consecuencia de corto y una de largo plazo.",
    extend="Explica por qué la valentía puede ser alejarse en vez de enfrentar.",
)

lesson(
    OA3, 4,
    "Una hoja y un lápiz. El caso del plan de protección de Camila y las frases de ejemplo están escritos en los ejercicios.",
    "Aprenderé a armar un plan de protección antes de una salida o reunión. Sirve para decidir con calma y saber qué hacer si surge alcohol, drogas, presión sexual o violencia.",
    ["Sé comparar opciones y consecuencias.", "Sé separar hechos, mitos y emociones."],
    [
        "Un plan de protección es una decisión tomada con calma antes de una situación de riesgo. Tiene tres partes. Antes: avisar a una persona adulta de confianza adónde vas, con quién y a qué hora volverás, y llevar el teléfono con batería. Durante: tener lista una frase para decir que no, estar cerca de personas que te respetan y mantenerte atento a señales de riesgo. Después: contar lo ocurrido a un adulto de confianza si algo te inquietó.",
        "Algunas reglas del plan son claras. No subas a un auto con un conductor que haya bebido o consumido otra sustancia: pide a un adulto que te busque. No dejes tu bebida sin cuidado ni aceptes bebidas que no viste preparar. Si la situación se vuelve peligrosa, sal del lugar y llama a un adulto de confianza. Si hay una pelea, no te metas ni la grabes: aléjate y avisa a un adulto.",
        "Un plan también incluye un código con tu familia: una palabra o mensaje acordado que significa «necesito que me vengan a buscar, sin preguntas por ahora». Pedir que te busquen es una decisión inteligente, no un fracaso. Y recuerda que si alguien te presiona para tener relaciones sexuales o te toca sin tu permiso, no es tu culpa y debes avisar a un adulto.",
    ],
    [("plan de protección", "decisión tomada antes de una situación de riesgo para saber qué hacer"), ("código", "palabra o mensaje acordado con la familia para pedir que te busquen"), ("conductor", "persona que maneja un vehículo"), ("señal de riesgo", "indicio de que la situación puede dañar"), ("salir del lugar", "alejarse para protegerse")],
    [
        W("Completar un plan", "Camila, una estudiante inventada, irá a una reunión de cumpleaños. ¿Qué debe hacer antes de ir?", ["Avisar adónde va y con quién.", "Informar la hora de regreso.", "Llevar el teléfono con batería."], "Avisar a un adulto de confianza adónde va, con quién y a qué hora volverá"),
        W("Usar el código", "En el cumpleaños, un grupo empieza a beber y le ofrecen. Camila no quiere seguir ahí. ¿Qué hace?", ["La situación se volvió de riesgo.", "Usa el código acordado con su familia.", "Sale del lugar y espera a un adulto."], "Usar el código, salir del lugar y esperar a que la busquen"),
    ],
    [
        M("Pensar que si me aviso solo después de lo ocurrido, es suficiente.", "Se espera a que ocurra el problema para pedir ayuda.", "El plan incluye avisar antes y tener una salida lista."),
        M("Creer que pedir que me busquen es un fracaso.", "Se confunde pedir ayuda con perder.", "Pedir que te busquen es una decisión inteligente."),
    ],
    R=[
        ex("¿Debes avisar a un adulto de confianza adónde vas, sí o no?", "Sí", "Es la parte de «antes» del plan."),
        ex("¿Se debe subir a un auto cuyo conductor bebió alcohol, sí o no?", "No", "Pone en riesgo a todos."),
        ex("Si estalla una pelea, ¿te metes o te alejas y avisas?", "Te alejas y avisas", "Evita daño y permite que un adulto actúe."),
    ],
    U=[
        ex("¿Por qué conviene decidir el plan antes de la salida y no durante?", "Porque durante la presión es más difícil pensar", "Una decisión previa se aplica con más calma."),
        ex("¿Qué es un código con la familia?", "Una palabra acordada para pedir que te busquen", "Permite pedir ayuda sin dar explicaciones inmediatas."),
        ex("¿Dejar tu bebida sin cuidado es una acción segura, sí o no?", "No", "Alguien podría agregarle algo."),
    ],
    A=[
        ex("Ordena el plan: 1) avisar adónde voy; 2) salir si hay riesgo; 3) contar lo ocurrido a un adulto. ¿Cuál va en «antes»?", "1", "Avisar adónde vas se hace antes de ir."),
        ex("Un amigo mayor ofrece llevar a Camila, pero tomó alcohol. Opciones: A) Llamar a un adulto de confianza para que la busquen. B) Subir porque «solo vive cerca».", "A", "Un conductor que bebió es un riesgo grave."),
        ex("Camila se queda sola en un lugar donde alguien intenta tocarla sin su permiso. ¿Qué hace primero? A) Salir del lugar y avisar a un adulto. B) Esperar a ver si se detiene.", "A", "Debe protegerse y contar; la responsabilidad no es suya."),
    ],
    Z=[
        ex("Sebastián dice: «Si uso el código, mis papás se van a enojar». ¿Qué argumento lo ayuda a verlo distinto?", "Que el código sirve para cuidarse y se acordó antes", "Es una forma planeada de protegerse, no de fallar."),
        ex("¿Por qué no es buena idea aceptar una bebida que no viste preparar?", "Porque pueden haberle agregado algo", "No puedes saber su contenido."),
    ],
    D=[
        arith("Camila saldrá a las 17 horas y volverá a las 21 horas. ¿Cuántas horas durará la salida?", "21-17", "Se resta la hora de salida a la de regreso."),
        ex("Camila acuerda con su familia un código, pero lo cuenta en el chat del curso. ¿Qué problema tiene eso?", "Que ya no es secreto", "Un código deja de servir si otras personas lo conocen."),
    ],
    context=[ex("Una compañera cuenta que fue a una fiesta y al final quedó sin cómo volver, porque el que la llevó había bebido. No dijo nada a nadie. ¿Qué parte del plan de protección faltó?", "Tener un código y avisar antes a un adulto", "Con aviso y un código habría tenido a quién llamar.")],
    selfcheck=[ex("En Orientación: ¿un plan de protección se decide antes?", "Sí", "Se piensa con calma antes."), ex("¿Puedo usar un código para pedir que me busquen?", "Sí", "Es una forma de protegerme."), ex("¿Es mi culpa si alguien me presiona sexualmente?", "No", "La responsabilidad es de quien presiona.")],
    task=T("Lee el caso de Felipe, un estudiante inventado: el viernes irá a una reunión de un compañero en una casa; no sabe si habrá adultos. Escribe su plan de protección con tres partes: qué hará antes, qué hará si hay alcohol o presión durante, y qué hará después. Incluye un código con su familia.", "Antes: avisar a un adulto de confianza adónde va y la hora; llevar el teléfono cargado. Durante: «no, gracias»; si hay riesgo, usar el código y salir. Después: contar lo ocurrido a un adulto. Código: la frase acordada.", ["escribe las tres partes del plan", "incluye un código", "nombra una acción para salir del lugar", "no cuenta nada personal"], ["plan escrito"], ["olvidar el antes", "no decir cómo salir"], "Reconoce el plan y pregunta qué cambiaría si no hay teléfono."),
    reinforce="Anota un código posible con tu familia que no revele nada personal.",
    extend="Explica por qué un plan protege incluso a quien sabe decir que no.",
)

lesson(
    OA3, 5,
    "Una hoja y un lápiz. Los tres estilos de comunicación y la lista de personas de ayuda están escritos en los ejercicios.",
    "Aprenderé a comunicarme de forma asertiva y a buscar ayuda en personas significativas y especializadas, dentro y fuera del colegio. Sirve para enfrentar presiones y pedir ayuda a tiempo.",
    ["Sé armar un plan de protección.", "Sé que puedo pedir ayuda a un adulto de confianza."],
    [
        "Hay tres formas de comunicarse cuando te presionan. En la pasiva callas o cedes aunque no quieras. En la agresiva gritas, insultas o amenazas. En la asertiva dices lo que piensas y sientes con claridad y respeto. Una fórmula asertiva sencilla es «yo + siento + necesito»: «Yo me siento incómodo cuando insisten; necesito que respeten mi decisión». Con la mirada firme, voz tranquila y mensaje corto, es más fácil que te escuchen. Si sientes miedo o la situación es peligrosa, no hace falta que lo digas: aléjate y avisa a un adulto.",
        "La comunicación asertiva no siempre basta. Cuando la presión sigue, cuando hay violencia, abuso, consumo de sustancias propio o de alguien cercano, o cuando te sientes muy mal, necesitas ayuda. Las personas significativas son aquellas importantes para ti y en las que confías: alguien de tu familia, un profesor o profesora, el orientador o la orientadora. Las personas especializadas son profesionales como psicólogos, el equipo de convivencia escolar y el personal de salud del consultorio.",
        "Dentro del colegio, puedes acudir a tu profesor jefe, a orientación y al equipo de convivencia escolar. Fuera, al consultorio o a la persona de tu familia. Si no te escuchan la primera vez, insiste con otra persona. Si necesitas ayuda y eres niño, niña o adolescente, también puedes llamar gratis al Fono Niños 147 de Carabineros. Pedir ayuda no es delatar: es cuidarse y cuidar a otros.",
    ],
    [("comunicación asertiva", "decir lo que pienso y siento con claridad y respeto"), ("pasivo", "que calla o cede sin decir lo que quiere"), ("agresivo", "que grita, insulta o amenaza"), ("persona significativa", "persona importante para mí y de confianza"), ("persona especializada", "profesional preparado para ayudar, como un psicólogo o personal de salud")],
    [
        W("Clasificar el estilo", "Ante la presión, Tomás grita «¡Déjenme, son unos tontos!». ¿Qué estilo usa?", ["Grita e insulta.", "Eso es agredir.", "Estilo agresivo."], "Agresivo"),
        W("Armar una frase asertiva", "Sofía quiere pedir que dejen de insistirle. Usa «yo + siento + necesito».", ["Yo me siento incómoda cuando insisten.", "Necesito que respeten mi decisión.", "Se dice con calma."], "«Me siento incómoda cuando insisten; necesito que respeten mi decisión»"),
    ],
    [
        M("Pensar que ser asertivo es ser grosero.", "Se confunde firmeza con agredir.", "Asertivo es claro y respetuoso."),
        M("Creer que pedir ayuda es delatar.", "Se piensa que contar traiciona a los demás.", "Pedir ayuda protege a las personas en riesgo."),
    ],
    R=[
        ex("Callar y ceder aunque no quieras, ¿es un estilo pasivo o asertivo?", "Pasivo", "No expresa lo que se quiere."),
        ex("Gritar e insultar, ¿es un estilo agresivo o asertivo?", "Agresivo", "Daña a la otra persona."),
        ex("Decir con claridad y respeto lo que piensas, ¿es un estilo asertivo o pasivo?", "Asertivo", "Combina firmeza y respeto."),
    ],
    U=[
        ex("¿Por qué «yo + siento + necesito» es una buena fórmula asertiva?", "Porque habla de lo propio sin acusar", "Expresa lo que siento y necesito sin atacar."),
        ex("¿Puede el personal de salud del consultorio ser una persona especializada, sí o no?", "Sí", "Es un profesional preparado para ayudar."),
        ex("Si el primer adulto no te escucha, ¿insistes con otra persona o te rindes?", "Insistes con otra persona", "Debes seguir hasta recibir ayuda."),
    ],
    A=[
        ex("Frases: 1) «Eres un pesado, déjame en paz»; 2) «Está bien, lo hago»; 3) «Me siento incómodo cuando insisten; necesito que paren»; 4) «Si sigues, te pego». ¿Cuántas son asertivas?", "1", "Solo la 3 expresa lo que siente y necesita con respeto; la 1 y la 4 agreden y la 2 cede."),
        ex("Un amigo se siente obligado a consumir algo y no sabe a quién acudir. ¿Cuál de estas personas le sirve? A) El orientador del colegio. B) Un compañero que también está preocupado.", "A", "Es una persona adulta del colegio, preparada para ayudar."),
        ex("Tomás ve que a un compañero lo golpean en el baño. ¿Qué hace? A) Aviso al equipo de convivencia escolar. B) Grabo para subirlo.", "A", "Pedir ayuda protege; grabar y difundir aumenta el daño."),
    ],
    Z=[
        ex("Lucía dice: «Si cuento, soy una soplona». ¿Qué respuesta la ayuda a ver distinto?", "Pedir ayuda protege a alguien que está en riesgo", "Avisar a un adulto es cuidar, no traicionar."),
        ex("¿Por qué la comunicación asertiva no siempre basta frente a la violencia?", "Porque algunas situaciones requieren ayuda de adultos", "Hay riesgos que una persona sola no puede resolver."),
    ],
    D=[
        arith("En una actividad ficticia, 25 estudiantes ensayan frases y 17 las dicen en forma asertiva. ¿Cuántos no lo hacen?", "25-17", "Al total se le restan los que sí lo hacen."),
        arith("Cada uno de los 6 grupos prepara 3 frases asertivas. ¿Cuántas frases hay?", "6*3", "Se multiplican grupos por frases."),
    ],
    context=[ex("Camila nota que un compañero llega con olor a alcohol al colegio y dice que lo hace «para aguantar». Está preocupada. ¿A quién puede acudir?", "A la orientadora o al equipo de convivencia escolar", "Son personas del colegio preparadas para ayudar a un estudiante.")],
    selfcheck=[ex("En Orientación: ¿ser asertivo es decir lo que pienso con respeto?", "Sí", "Es firmeza sin agresión."), ex("¿Pedir ayuda es delatar?", "No", "Es una forma de cuidar a otros."), ex("¿Puedo llamar gratis al Fono Niños 147 si lo necesito?", "Sí", "Es un recurso de Carabineros.")],
    task=T("Lee el caso inventado de Martina: dos compañeros la presionan a que pruebe un vapeador y se burlan si no lo hace. Escribe una frase asertiva con la fórmula «yo + siento + necesito», una frase de qué haría si siguen y dos personas, una significativa y otra especializada, a quienes recurriría.", "Frase: «Me siento incómoda cuando insisten; necesito que respeten mi decisión». Si siguen: irse y avisar. Personas: su profesora jefe (significativa) y la orientadora o el personal de salud del consultorio (especializada).", ["usa la fórmula asertiva", "dice qué hace si siguen", "nombra una persona significativa y una especializada", "no cuenta nada personal"], ["texto escrito o ensayo oral"], ["responder con agresión", "no nombrar ayuda"], "Reconoce la fórmula y pregunta qué haría si la presión sigue por mensajes."),
    reinforce="Escribe una frase asertiva para otro tema, como un amigo que quiere copiar en una prueba.",
    extend="Explica la diferencia entre persona significativa y persona especializada.",
)

# ================================================================ OA 04
lesson(
    OA4, 1,
    "Una hoja y un lápiz. El diario de un día de Emilia, una estudiante inventada, está escrito en los ejercicios.",
    "Aprenderé qué hábitos de alimentación, descanso y actividad física favorecen el bienestar. Sirve para revisar mi propio día con criterios claros.",
    ["Sé que cuidar mi cuerpo es un derecho y una responsabilidad.", "Sé leer datos simples de una tabla."],
    [
        "El bienestar es sentirse bien en el cuerpo, en las emociones y con los demás. Se construye con hábitos diarios. La alimentación saludable incluye variedad: frutas, verduras, legumbres, cereales, lácteos y agua. En Chile, los envases traen sellos negros «ALTO EN» (azúcares, grasas saturadas, sodio o calorías): indican que ese producto conviene comerlo poco. Un desayuno y una colación equilibrados dan energía para estudiar.",
        "El descanso también es salud. Los adolescentes necesitan dormir entre 8 y 10 horas por noche. Dormir poco afecta la atención, la memoria y el ánimo. Las pantallas antes de dormir dificultan el sueño. Conviene tener horarios regulares y apagar el celular un rato antes de acostarse.",
        "La actividad física ayuda al cuerpo y al ánimo. La Organización Mundial de la Salud recomienda para esta edad un promedio de al menos 60 minutos diarios de actividad moderada o intensa, como caminar rápido, jugar, bailar o hacer deporte. Cuando varios hábitos se cuidan juntos, el bienestar mejora. Y una comunidad escolar que ofrece buenas colaciones, tiempo de juego y pausas activas ayuda a todos.",
    ],
    [("bienestar", "sentirse bien en el cuerpo, en las emociones y con los demás"), ("hábito", "acción que se repite con regularidad"), ("alimentación saludable", "comer variado y con poca cantidad de productos con sellos «ALTO EN»"), ("descanso", "tiempo de sueño y pausa que repone al cuerpo y a la mente"), ("actividad física", "movimiento del cuerpo que gasta energía")],
    [
        W("Revisar un hábito", "Emilia duerme 6 horas porque usa el celular hasta tarde. ¿Cumple con las horas de sueño recomendadas para su edad?", ["Se recomiendan 8 a 10 horas.", "6 es menos que 8.", "No cumple."], "No, duerme menos de lo recomendado"),
        W("Leer un sello", "El envase de unas galletas tiene el sello «ALTO EN azúcares». ¿Qué indica?", ["Es un sello negro que alerta.", "Dice que tiene mucha azúcar.", "Conviene comerlo poco."], "Que tiene mucha azúcar y conviene comerlo poco"),
    ],
    [
        M("Creer que mientras más dulces, más energía.", "Se confunde sentir energía rápida con una buena alimentación.", "Elige variedad y revisa los sellos «ALTO EN»."),
        M("Pensar que dormir poco no importa si compenso el fin de semana.", "Se piensa que el sueño se recupera sin costo.", "Dormir regularmente es mejor para la atención y el ánimo."),
    ],
    R=[
        ex("¿Cuántas horas de sueño necesitan los adolescentes: entre 8 y 10 o entre 3 y 5?", "Entre 8 y 10", "Es el rango recomendado para esta edad."),
        ex("El agua, ¿es parte de una alimentación saludable, sí o no?", "Sí", "Mantiene hidratado el cuerpo."),
        ex("Un sello negro «ALTO EN sodio», ¿avisa que tiene mucha sal o poca sal?", "Mucha sal", "El sodio proviene de la sal."),
    ],
    U=[
        ex("¿Por qué conviene apagar las pantallas un rato antes de dormir?", "Porque dificultan el sueño", "La luz y el contenido mantienen despierta a la persona."),
        ex("¿Cuántos minutos diarios de actividad física se recomiendan en promedio a esta edad: 60 o 10?", "60", "Es la recomendación de la OMS."),
        ex("¿Caminar rápido cuenta como actividad física, sí o no?", "Sí", "Es una actividad moderada."),
    ],
    A=[
        ex("Día de Emilia: desayuno con fruta y pan; 7 horas de sueño; colación con un jugo con sello «ALTO EN azúcares»; 60 minutos entre caminata y juego. ¿Cuántos hábitos cumplen lo recomendado?", "2", "El desayuno variado y los 60 minutos cumplen; las 7 horas y el jugo con sello no."),
        ex("Un compañero se salta el desayuno y se siente cansado a la 2.ª hora. ¿Qué cambio le ayuda? A) Tomar un desayuno equilibrado. B) Tomar solo una bebida energética.", "A", "Un desayuno equilibrado da energía sostenida."),
        ex("Emilia se acuesta a las 22 y despierta a las 6 de la mañana siguiente. ¿Cumple con las horas de sueño recomendadas para su edad?", "Sí, duerme 8 horas", "De las 22 a las 6 pasan 8 horas, que está dentro del rango de 8 a 10."),
    ],
    Z=[
        ex("Diego dice: «Si hago ejercicio una hora el sábado, ya no necesito moverme el resto de la semana». ¿Qué error hay?", "La recomendación es un promedio diario", "Mantener el movimiento todos los días protege mejor."),
        ex("¿Por qué una buena colación en el colegio es parte de la vida saludable de la comunidad escolar?", "Porque ayuda a todos a rendir y sentirse bien", "Los hábitos compartidos se refuerzan."),
    ],
    D=[
        arith("Si Emilia camina 20 minutos y juega 25 minutos de fútbol, ¿cuántos minutos de actividad física suma?", "20+25", "Se suman los minutos."),
        arith("Emilia ya hizo 45 minutos de actividad física hoy y la recomendación es de 60 minutos. ¿Cuántos minutos le faltan?", "60-45", "Se resta lo hecho a lo recomendado."),
    ],
    context=[ex("En el kiosco del colegio solo hay productos con sellos «ALTO EN». Un grupo de estudiantes propone sumar frutas y agua. ¿Qué hábito de la comunidad escolar mejora esta propuesta?", "La alimentación saludable", "Ofrece opciones variadas y con menos sellos.")],
    selfcheck=[ex("En Orientación: ¿los sellos «ALTO EN» avisan que conviene comer poco ese producto?", "Sí", "Alertan sobre exceso de azúcar, grasas, sodio o calorías."), ex("¿Dormir entre 8 y 10 horas es lo recomendado?", "Sí", "Es el rango indicado para adolescentes."), ex("¿La actividad física ayuda también al ánimo?", "Sí", "Mejora el bienestar emocional.")],
    task=T("Lee el día inventado de Pablo: se acuesta a las 00:00 y se levanta a las 7:00; desayuna una bebida con azúcar y una galleta con sello «ALTO EN grasas saturadas»; en el recreo juega 15 minutos; en la tarde ve 3 horas de series. Escribe cuántas horas durmió, qué hábito mejorarías en alimentación, uno en descanso y uno en actividad física.", "Durmió 7 horas, menos de lo recomendado. Alimentación: agregar fruta y agua al desayuno. Descanso: acostarse más temprano. Actividad física: sumar 30 minutos de caminata o juego después del colegio.", ["calcula las horas de sueño", "propone un cambio en cada hábito", "usa datos del día de Pablo", "no cuenta nada personal"], ["texto escrito"], ["no usar los datos", "proponer cambios irreales"], "Reconoce los cambios y pregunta cuál sería el primero que aplicaría."),
    reinforce="Anota un hábito saludable de alimentación, uno de descanso y uno de actividad física para un personaje de cuento.",
    extend="Explica cómo un kiosco saludable ayuda a toda la comunidad escolar.",
)

lesson(
    OA4, 2,
    "Una hoja y un lápiz. Los casos de Lucas y Amanda, estudiantes inventados, y la lista de situaciones de privacidad están escritos en los ejercicios.",
    "Aprenderé a distinguir hechos, emociones y derechos cuando se trata de mi cuerpo, mi imagen y mi intimidad en la vida diaria. Sirve para resguardar mi integridad en el colegio y en línea.",
    ["Sé que mi cuerpo es mío.", "Sé que las fotos íntimas no se envían."],
    [
        "Resguardar la intimidad y la integridad del cuerpo es parte del bienestar. La intimidad es tu mundo privado; la integridad es que nadie dañe tu cuerpo ni tu dignidad. En el colegio, por ejemplo, en el baño o en los camarines, tienes derecho a privacidad: nadie debe mirarte, tomarte fotos o grabarte sin tu permiso. Hacerlo puede ser un delito y siempre es una falta grave.",
        "La imagen también es tuya. Una foto o video tuyo no debe subirse a redes sin tu permiso, y no tienes que aceptar que te etiqueten si no quieres. Tampoco debes publicar fotos de otros sin su acuerdo. Si alguien sube una imagen tuya que te incomoda, puedes pedir que la borren, bloquear, reportar y avisar a un adulto.",
        "Frente a comentarios sobre el cuerpo, las dietas «milagro» o las rutinas extremas que se promocionan en redes, recuerda: el cuerpo de cada persona es distinto, no existe un cuerpo ideal, y cambiar la alimentación de forma extrema puede dañar la salud. Si te sientes mal con tu cuerpo o con la comida, habla con un adulto de confianza o con el personal de salud.",
    ],
    [("integridad", "que nadie dañe mi cuerpo ni mi dignidad"), ("privacidad", "derecho a mantener en reserva mis cosas personales"), ("camarín", "lugar donde los estudiantes se cambian de ropa"), ("dieta milagro", "plan de alimentación que promete resultados rápidos sin respaldo de salud"), ("etiquetar", "señalar a una persona en una foto o publicación")],
    [
        W("Identificar una vulneración", "Un estudiante graba con el celular a un compañero en el camarín. ¿Se respeta su privacidad?", ["En el camarín hay derecho a privacidad.", "Grabar sin permiso lo vulnera.", "No se respeta."], "No, vulnera su privacidad e integridad"),
        W("Actuar ante una foto subida", "Amanda ve que subieron una foto suya en una red sin permiso, y no le gusta. ¿Qué puede hacer?", ["Puede pedir que la borren.", "Puede reportar la publicación.", "Debe contárselo a un adulto de confianza."], "Pedir que la borren, reportar y avisar a un adulto"),
    ],
    [
        M("Creer que si es una broma, grabar a alguien en el baño no es grave.", "Se confunde la intención de reír con el daño.", "Grabar sin permiso es una falta grave; la privacidad se respeta."),
        M("Pensar que existe un cuerpo ideal y debo parecerme a él.", "Se confunde lo que muestran las redes con la realidad.", "Cada cuerpo es distinto; no hay un cuerpo ideal."),
    ],
    R=[
        ex("¿Tienes derecho a privacidad en el baño y en los camarines, sí o no?", "Sí", "Nadie debe mirarte ni grabarte sin permiso."),
        ex("Subir la foto de otra persona sin su permiso, ¿respeta su imagen, sí o no?", "No", "Su imagen también le pertenece."),
        ex("¿Existe un cuerpo ideal igual para todos, sí o no?", "No", "Cada cuerpo es distinto."),
    ],
    U=[
        ex("¿Por qué grabar en un camarín es una falta grave y no una broma?", "Porque vulnera la privacidad y la dignidad", "Daña a la persona sin su permiso."),
        ex("¿Qué es una dieta «milagro»?", "Un plan que promete resultados rápidos sin respaldo de salud", "Puede dañar el cuerpo."),
        ex("Si te sientes mal con tu cuerpo, ¿es buena idea hablar con un adulto de confianza, sí o no?", "Sí", "Es una forma de cuidarse."),
    ],
    A=[
        ex("Situaciones: 1) tomar una foto con permiso; 2) grabar a alguien en el baño; 3) subir una foto de otro sin avisar; 4) pedir permiso antes de etiquetar. ¿Cuántas respetan la privacidad?", "2", "La 1 y la 4 piden permiso; la 2 y la 3 no."),
        ex("Un compañero se burla del cuerpo de Lucas y dice «es para que te cuides». ¿Qué corresponde? A) Poner un límite y avisar a un adulto si sigue. B) Aceptarlo porque es por su bien.", "A", "Una burla no es cuidado."),
        ex("Una influencer promete «bajar 5 kilos en una semana sin comer». ¿Qué haces con esa información?", "No la sigo y consulto a profesionales de salud", "Es una dieta milagro que puede dañar la salud."),
    ],
    Z=[
        ex("Bruno dice: «Si le saco una foto en el camarín y no la subo, no pasa nada». ¿Qué error hay?", "La falta es tomar la foto sin permiso", "La privacidad se vulnera aunque no se publique."),
        ex("¿Por qué conviene pedir permiso antes de subir una foto de otros?", "Porque su imagen es suya", "Cada persona decide sobre su imagen."),
    ],
    D=[
        arith("En un curso de 28 estudiantes, 3 dicen que no quieren que se suba su foto a redes. ¿A cuántos sí se les podría pedir permiso?", "28-3", "Se restan los que no quieren."),
        ex("Un estudiante dice: «Si no se ve la cara, no es mi imagen». ¿Es correcto pensar que no necesitas permiso si no se ve la cara de la persona?", "No", "Aunque no se vea la cara, la persona puede ser reconocida y su cuerpo es suyo."),
    ],
    context=[ex("En una clase de Educación Física, varios quieren grabar un baile del curso para subirlo. Una estudiante dice que no quiere salir. ¿Qué corresponde?", "Respetar su decisión y no grabarla", "Su imagen es suya y puede decidir.")],
    selfcheck=[ex("En Orientación: ¿mi imagen es mía?", "Sí", "Nadie puede usarla sin mi permiso."), ex("¿Grabar a alguien en el baño es grave?", "Sí", "Vulnera la privacidad."), ex("¿Existe un cuerpo ideal?", "No", "Cada cuerpo es distinto.")],
    task=T("Lee el caso inventado de Nicolás: en el camarín, un compañero le saca una foto mientras se cambia y dice «es para reírnos». Nicolás se siente muy mal. Escribe el hecho, la emoción, el derecho vulnerado y tres acciones que Nicolás puede tomar para protegerse.", "Hecho: lo fotografiaron sin permiso. Emoción: se siente mal. Derecho: privacidad e integridad. Acciones: pedir que la borre, avisar a un adulto y no responder con agresión.", ["separa hecho, emoción y derecho", "propone tres acciones", "no culpa a Nicolás", "no cuenta nada personal"], ["texto escrito"], ["justificar la foto como broma", "no avisar a un adulto"], "Reconoce el análisis y pregunta a quién avisaría primero."),
    reinforce="Escribe una regla de privacidad para camarines y baños de tu colegio.",
    extend="Explica por qué una dieta milagro puede ser peligrosa.",
)

lesson(
    OA4, 3,
    "Una hoja y un lápiz. Las tarjetas de decisiones de Sebastián, un estudiante inventado, y el horario de ejemplo están escritos en los ejercicios.",
    "Aprenderé a comparar opciones y sus consecuencias en mi día: sueño, pantalla, colación y movimiento. Sirve para elegir lo que cuida mi bienestar sin dejar de disfrutar.",
    ["Sé qué hábitos favorecen el bienestar.", "Sé que cada decisión tiene consecuencias."],
    [
        "Cada día tomas pequeñas decisiones que suman. A la hora de dormir puedes elegir seguir viendo videos o apagar el celular; la primera opción da entretención hoy, pero al día siguiente te sientes cansado. En el recreo puedes sentarte a ver el teléfono o jugar; moverte te ayuda a concentrarte en clases. En la colación puedes elegir algo con sello «ALTO EN» o una fruta; la primera da gusto rápido, la segunda da energía más estable.",
        "Elegir bien no significa nunca más comer un dulce. Significa que el hábito principal sea saludable, y que los gustos ocasionales no lo reemplacen. Un día de cumpleaños con torta no arruina la salud; lo que pesa es lo que haces la mayoría de los días. Fíjate en tu cuerpo: si te sientes sin energía o con sueño en clases, puede ser una señal de que necesitas cambiar un hábito.",
        "En la comunidad escolar también hay decisiones colectivas. Un curso puede proponer una pausa activa de 5 minutos, llevar botellas de agua o organizar una caminata. Estas decisiones mejoran el bienestar de todos y se mantienen si los estudiantes las cuidan juntos. Compara siempre dos o tres opciones, anticipa qué pasará con cada una y elige la que mejor cuida tu bienestar.",
    ],
    [("decisión", "elección entre varias opciones"), ("consecuencia", "lo que ocurre después de una decisión"), ("pausa activa", "pausa breve para mover el cuerpo durante la jornada"), ("ocasional", "que ocurre de vez en cuando"), ("hidratarse", "tomar agua para mantener el cuerpo con líquido")],
    [
        W("Comparar dos opciones", "Sebastián debe elegir en la noche: ver videos hasta las 24 h o dormir a las 22 h para levantarse a las 6 h. ¿Cuál opción le da más horas de sueño para el día siguiente?", ["Con la segunda duerme de 22 a 6.", "Eso son 8 horas.", "La primera lo deja con menos horas."], "Dormir a las 22 h, porque suma 8 horas"),
        W("Elegir la colación", "Opciones: papas fritas con sello «ALTO EN sodio» o un plátano. ¿Cuál aporta energía más estable?", ["La fruta no tiene sellos.", "Aporta energía de forma gradual.", "Es mejor el plátano."], "El plátano"),
    ],
    [
        M("Pensar que si un día no como saludable, ya perdí todo.", "Se confunde un día con el hábito.", "Lo que pesa es lo que haces la mayoría de los días."),
        M("Creer que moverme en el recreo me cansa y rinde menos.", "Se piensa que el movimiento quita energía.", "Moverte ayuda a concentrarte."),
    ],
    R=[
        ex("¿Apagar el celular antes de dormir ayuda al sueño, sí o no?", "Sí", "Evita que la pantalla mantenga despierto."),
        ex("Un plátano en la colación, ¿tiene sello «ALTO EN», sí o no?", "No", "Es una fruta natural, sin sellos."),
        ex("¿Una pausa activa es un breve momento para mover el cuerpo, sí o no?", "Sí", "Ayuda a concentrarse."),
    ],
    U=[
        ex("¿Por qué una torta en un cumpleaños no arruina la alimentación saludable?", "Porque es ocasional", "Lo que pesa es lo que se hace la mayoría de los días."),
        ex("Si te sientes con mucho sueño en clases, ¿puede ser una señal de que debes revisar tu descanso?", "Sí", "Dormir poco afecta la atención."),
        ex("¿Una pausa activa mejora el bienestar de todo el curso, sí o no?", "Sí", "Todos se mueven y se concentran mejor."),
    ],
    A=[
        ex("Tarjetas: 1) jugar 15 minutos en el recreo; 2) ver el teléfono sentado todo el recreo; 3) tomar agua; 4) saltarse el desayuno. ¿Cuántas ayudan al bienestar?", "2", "Jugar y tomar agua ayudan; las otras no."),
        ex("Sebastián se acuesta a las 23 y debe levantarse a las 6:30. ¿Cuál opción lo acerca más a las 8 horas de sueño? A) Acostarse a las 23. B) Acostarse a las 22.", "B", "Con las 22 h duerme más y se acerca a lo recomendado."),
        ex("El curso propone una pausa activa de 5 minutos al día durante una semana de clases (5 días). Opciones: A) Cada día se mueven 5 minutos. B) Se mueven solo el primer día.", "A", "La constancia cada día produce el hábito."),
    ],
    Z=[
        ex("Valentina dice: «Si me muevo en el recreo, voy a quedar muy cansada para estudiar». ¿Qué responderías?", "Que moverse ayuda a concentrarse", "La actividad física mejora la atención."),
        ex("¿Por qué comparar al menos dos opciones antes de decidir ayuda a elegir mejor?", "Porque permite ver consecuencias distintas", "Se ve qué opción cuida más el bienestar."),
    ],
    D=[
        ex("Sebastián duerme de 23 a 7 una noche y de 1 a 7 otra noche. ¿En cuál de las dos duerme menos horas?", "En la segunda: de 1 a 7 son 6 horas", "La primera suma 8 horas y la segunda solo 6."),
        arith("Si cada pausa activa dura 5 minutos y hay 3 pausas al día, ¿cuántos minutos de movimiento suma al día?", "5*3", "Se multiplican los minutos por las pausas."),
    ],
    context=[ex("El curso decide organizar una caminata de 30 minutos cada viernes. A Matías le da flojera, pero va. ¿Cuál es una consecuencia positiva de corto plazo?", "Se siente con más energía y ánimo", "El movimiento mejora el ánimo pronto.")],
    selfcheck=[ex("En Orientación: ¿cada decisión del día tiene consecuencias?", "Sí", "Algunas pronto y otras después."), ex("¿Un gusto ocasional arruina la salud?", "No", "Lo que pesa es el hábito."), ex("¿Una pausa activa ayuda a concentrarse?", "Sí", "El movimiento mejora la atención.")],
    task=T("Lee el caso inventado de Camilo: tiene que decidir en la noche si ve videos hasta tarde o duerme temprano; en el recreo, si juega o mira el teléfono; en la colación, si come una galleta con sello «ALTO EN azúcares» o una fruta. Para cada decisión escribe las dos opciones, la consecuencia de cada una y cuál elegirías.", "Noche: dormir temprano (descansa) vs videos (cansancio); elige dormir. Recreo: jugar (concentración) vs teléfono (sedentarismo); elige jugar. Colación: fruta (energía estable) vs galleta (energía rápida); elige fruta.", ["escribe las dos opciones de cada decisión", "dice la consecuencia", "elige una y justifica", "no cuenta nada personal"], ["tabla escrita"], ["no mirar consecuencias", "elegir sin justificar"], "Reconoce la tabla y pregunta cuál decisión sería más difícil de cumplir."),
    reinforce="Escribe dos opciones y sus consecuencias para una decisión de tu día de un personaje.",
    extend="Propón una pausa activa de 3 minutos para tu curso que se haga en la sala.",
)

lesson(
    OA4, 4,
    "Una hoja y un lápiz. El caso de Paz, una estudiante inventada, y la lista de ajustes de seguridad están escritos en los ejercicios.",
    "Aprenderé a tomar medidas de seguridad al usar redes sociales y mensajería: privacidad, contraseñas, datos y contactos. Sirve para cuidar mi intimidad y mi bienestar en línea.",
    ["Sé que mi imagen y mi intimidad son mías.", "Sé que no se envían imágenes íntimas."],
    [
        "En redes sociales y aplicaciones de mensajes, las medidas de seguridad ayudan a proteger tu intimidad. Primero, configura tu cuenta como privada para que solo vean tus publicaciones las personas que aceptes. Segundo, usa contraseñas largas, distintas para cada cuenta, y no las compartas con nadie, ni siquiera con amigos o pareja. Tercero, no publiques datos que permitan ubicarte: dirección, colegio, horarios o lugares en tiempo real.",
        "Cuarto, acepta solo personas que conoces de verdad. Un perfil puede ser falso: puede tener fotos de otra persona o un adulto puede fingir ser un adolescente. Quinto, no abras enlaces desconocidos ni descargues archivos de desconocidos, porque pueden robar tus datos. Sexto, ten en cuenta que muchas redes exigen tener al menos 13 años; si usas una, es mejor hacerlo con el conocimiento de un adulto de tu casa.",
        "Además, cuida tu tiempo: usar pantallas sin pausas cansa los ojos y quita horas de sueño. Si algo te incomoda, como un mensaje agresivo o la petición de una foto, bloquea, reporta y avisa a un adulto de confianza. No respondas con agresión ni borres todo antes de mostrarlo: guarda capturas de pantalla como evidencia. Si el mensaje trae una imagen íntima, no la reenvíes ni la guardes: avisa a un adulto.",
    ],
    [("configuración privada", "ajuste que hace que solo vean mi perfil quienes yo acepto"), ("contraseña segura", "clave larga y distinta, que no comparto"), ("perfil falso", "cuenta que finge ser otra persona"), ("reportar", "avisar a la plataforma que una cuenta o mensaje es dañino"), ("evidencia", "prueba, como una captura de pantalla")],
    [
        W("Elegir una contraseña", "Paz debe elegir entre «123456» y una frase larga con números y símbolos que solo ella conoce. ¿Cuál es más segura?", ["«123456» es fácil de adivinar.", "Una frase larga es difícil de adivinar.", "Es más segura la frase larga."], "La frase larga con números y símbolos"),
        W("Responder a un contacto desconocido", "Un perfil con foto de adolescente le pide a Paz su dirección y el horario de salida. ¿Qué hace?", ["Puede ser un perfil falso.", "Pide datos que permiten ubicarla.", "Debe bloquear, reportar y avisar a un adulto."], "Bloquear, reportar y avisar a un adulto de confianza"),
    ],
    [
        M("Creer que compartir mi contraseña con mi pareja demuestra confianza.", "Se confunde confianza con perder privacidad.", "La contraseña no se comparte con nadie."),
        M("Pensar que aceptar a todas las personas que me siguen aumenta mi seguridad.", "Se confunde popularidad con seguridad.", "Acepta solo a quienes conoces de verdad."),
    ],
    R=[
        ex("¿Una cuenta privada deja que cualquiera vea tus publicaciones, sí o no?", "No", "Solo las ven las personas que aceptas."),
        ex("¿Se puede compartir la contraseña con un amigo, sí o no?", "No", "Compartirla aumenta el riesgo."),
        ex("Un perfil desconocido pide tu dirección. ¿Respondes o bloqueas?", "Bloqueas", "Pide datos que permiten ubicarte."),
    ],
    U=[
        ex("¿Por qué un perfil con foto de adolescente puede ser falso?", "Porque puede ser un adulto que finge", "Las fotos y datos pueden ser inventados."),
        ex("¿Por qué conviene guardar capturas de pantalla de un mensaje agresivo antes de bloquear?", "Porque sirven de evidencia", "Un adulto puede usarlas para ayudar."),
        ex("¿Los enlaces de desconocidos son seguros de abrir, sí o no?", "No", "Pueden robar tus datos."),
    ],
    A=[
        ex("Ajustes: 1) cuenta privada; 2) contraseña única por cuenta; 3) publicar tu ubicación en vivo; 4) aceptar a todos. ¿Cuántos mejoran la seguridad?", "2", "Los dos primeros protegen; los otros dos aumentan el riesgo."),
        ex("Paz recibe un mensaje: «Soy de tu colegio, mándame una foto y no le cuentes a nadie». ¿Qué hace? A) Bloquear, reportar y avisar a un adulto. B) Enviar la foto y guardar el secreto.", "A", "Es una señal de peligro; el secreto no se guarda."),
        ex("Un compañero publica el horario en que su casa queda sola. ¿Qué riesgo corre?", "Que desconocidos sepan cuándo está sola la casa", "Los datos de ubicación y horarios no deben publicarse."),
    ],
    Z=[
        ex("Tomás dice: «Si tengo muchos seguidores, soy más popular y más seguro». ¿Qué error hay?", "Más seguidores no significa más seguridad", "Muchos seguidores desconocidos aumentan el riesgo."),
        ex("¿Por qué conviene que un adulto de tu casa sepa que usas una red?", "Porque puede ayudarte si surge un problema", "El apoyo adulto es un factor protector."),
    ],
    D=[
        arith("Paz revisa 8 ajustes de seguridad y 5 ya están bien. ¿Cuántos faltan por corregir?", "8-5", "Se resta lo que ya está bien."),
        ex("Paz usa la misma contraseña en sus cuentas y la filtran en una de ellas. ¿Qué riesgo corren las otras cuentas?", "Que también puedan ser abiertas", "Si la clave es igual, quien la obtiene puede entrar a todas."),
    ],
    context=[ex("En un grupo del curso piden a todos compartir su ubicación para «saber dónde andan». Rocío no quiere. ¿Qué corresponde?", "Respetar su decisión de no compartir", "La ubicación es un dato privado.")],
    selfcheck=[ex("En Orientación: ¿una contraseña segura es larga y no se comparte?", "Sí", "Dificulta que otros accedan."), ex("¿Debo aceptar a todos los que piden seguirme?", "No", "Solo a quienes conozco."), ex("¿Puedo bloquear, reportar y avisar a un adulto si algo me incomoda?", "Sí", "Es una acción segura.")],
    task=T("Lee el caso de Isidro, un estudiante inventado: tiene una cuenta pública; usa la misma contraseña en todo; un perfil desconocido le pide una foto con su uniforme y el nombre del colegio. Escribe tres medidas de seguridad que Isidro debe aplicar y qué hace con el perfil desconocido, sin responderle.", "Medidas: cuenta privada, contraseñas distintas, no compartir datos. Con el perfil desconocido: no responde, bloquea, reporta y avisa a un adulto de confianza.", ["propone tres medidas", "dice que no responde al perfil", "dice que bloquea, reporta y avisa", "no cuenta nada personal"], ["lista escrita"], ["compartir datos", "no avisar a un adulto"], "Reconoce las medidas y pregunta cuál le costaría más aplicar."),
    reinforce="Anota tres datos que no debes publicar en una red.",
    extend="Explica por qué un perfil falso puede ser peligroso.",
)

lesson(
    OA4, 5,
    "Una hoja y un lápiz. Las situaciones de ayuda y la propuesta de Valentina, una estudiante inventada, están escritas en los ejercicios.",
    "Aprenderé a pedir ayuda cuando mi bienestar o el de otros está en riesgo y a proponer acciones saludables para el curso. Sirve para cuidar mi bienestar y mejorar la convivencia en el colegio.",
    ["Sé decidir qué hábitos cuidan mi bienestar.", "Sé aplicar medidas de seguridad en redes."],
    [
        "A veces el bienestar se ve afectado y no basta con un buen hábito. Algunas señales son: dormir muy poco por varias semanas, perder el apetito, sentirse muy triste o ansioso, o recibir mensajes en línea que te asustan. En esos casos conviene pedir ayuda. Puedes acudir a tu familia, a tu profesor jefe, a orientación o al personal de salud del consultorio. Contar lo que te pasa no es debilidad: es cuidar de ti.",
        "Para pedir ayuda, organiza lo que quieres decir en tres pasos. Primero, nombra lo que ocurre con hechos: «llevo dos semanas durmiendo menos de 6 horas». Segundo, di cómo te sientes: «estoy muy cansada y me cuesta concentrarme». Tercero, pide algo concreto: «necesito ayuda para organizar mi horario». Si no te entienden, insiste con otra persona. Si no sabes a quién acudir, puedes llamar gratis al Fono Niños 147.",
        "También puedes mejorar el bienestar de tu comunidad escolar con propuestas concretas: pausas activas, colaciones saludables, un acuerdo para no usar celulares en ciertos momentos o un día de la caminata. Una buena propuesta dice qué se hará, quién lo hará, cuándo y cómo se evaluará. Presentarla en el Consejo de Curso o a la dirección ayuda a que se concrete.",
    ],
    [("señal de alerta", "cambio que indica que necesito apoyo"), ("propuesta", "idea concreta para mejorar algo"), ("Consejo de Curso", "espacio donde el curso conversa y decide cosas en conjunto"), ("evaluar", "revisar si lo que se hizo funcionó"), ("comunidad escolar", "estudiantes, familias, docentes y funcionarios del colegio")],
    [
        W("Pedir ayuda en tres pasos", "Valentina, una estudiante inventada, duerme menos de 6 horas hace dos semanas y se siente cansada. ¿Cómo pide ayuda?", ["Nombra los hechos.", "Dice cómo se siente.", "Pide algo concreto."], "«Hace dos semanas duermo menos de 6 horas, estoy muy cansada y necesito ayuda para organizar mi horario»"),
        W("Evaluar una propuesta", "Un curso propone «hacer algo para estar mejor». ¿Es una buena propuesta?", ["No dice qué se hará ni quién.", "No tiene fecha ni forma de evaluar.", "Es poco clara."], "No, porque es poco clara"),
    ],
    [
        M("Pensar que pedir ayuda por cansancio o tristeza es exagerar.", "Se minimiza el malestar.", "Si dura semanas, conviene consultar."),
        M("Creer que una propuesta basta con una buena idea.", "Se omite el plan para concretarla.", "Define quién, cuándo y cómo evaluar."),
    ],
    R=[
        ex("¿El personal de salud del consultorio puede ayudar con el bienestar, sí o no?", "Sí", "Es una persona especializada."),
        ex("Dormir muy poco por varias semanas, ¿es una señal de alerta, sí o no?", "Sí", "Afecta la atención y el ánimo."),
        ex("¿Una propuesta clara dice quién, cuándo y cómo, sí o no?", "Sí", "Así se puede llevar a cabo."),
    ],
    U=[
        ex("¿Por qué conviene nombrar hechos al pedir ayuda?", "Porque ayuda a que entiendan qué ocurre", "Los hechos son concretos."),
        ex("¿Dónde puede presentarse la propuesta de una pausa activa: en el Consejo de Curso o en el recreo?", "En el Consejo de Curso", "Es el espacio del curso para decidir."),
        ex("Si el primer adulto no te entiende, ¿qué haces?", "Insistes con otra persona", "Hay más adultos de confianza."),
    ],
    A=[
        ex("Pasos de una petición de ayuda: 1) pedir algo concreto; 2) nombrar el hecho; 3) decir cómo me siento. ¿Cuál va primero?", "2", "Se parte nombrando lo que ocurre."),
        ex("Propuesta A: «Pausa activa de 5 minutos cada día a las 10:30, dirigida por turnos, revisada en un mes». Propuesta B: «Hagamos algo saludable». ¿Cuál es mejor?", "A", "Tiene qué, cuándo, quién y cómo evaluar."),
        ex("Un estudiante recibe mensajes que lo asustan y se siente mal. ¿Qué hace? A) Pedir ayuda a un adulto de confianza. B) Guardarlo para no preocupar.", "A", "Un malestar prolongado necesita apoyo."),
    ],
    Z=[
        ex("Camila dice: «No voy a pedir ayuda porque nadie se va a preocupar». ¿Qué argumento le darías?", "Que los adultos de confianza están para ayudar", "Hay personas preparadas que quieren apoyar."),
        ex("¿Por qué evaluar una propuesta después de un tiempo ayuda a mejorarla?", "Porque se ve si funcionó", "Permite ajustar lo que no resultó."),
    ],
    D=[
        arith("Un curso de 30 estudiantes propone pausas activas y 24 votan a favor. ¿Cuántos no votan a favor?", "30-24", "Se restan los que votaron a favor."),
        arith("Si cada pausa activa dura 5 minutos y se hacen 4 por semana, ¿cuántos minutos son al mes (4 semanas)?", "5*4*4", "Se multiplican minutos, pausas y semanas."),
    ],
    context=[ex("En el colegio hay mucho ruido y estudiantes cansados por las mañanas. Un grupo propone retrasar el uso del celular hasta después del primer recreo. ¿Qué debe incluir la propuesta para ser clara?", "Quién, cuándo y cómo se evaluará", "Una propuesta clara se puede llevar a cabo y revisar.")],
    selfcheck=[ex("En Orientación: ¿puedo pedir ayuda si mi bienestar está afectado?", "Sí", "Es una forma de cuidarme."), ex("¿Una propuesta clara dice quién y cuándo?", "Sí", "Así se puede ejecutar."), ex("¿Debo insistir con otro adulto si el primero no me escucha?", "Sí", "Debo seguir hasta recibir ayuda.")],
    task=T("Lee el caso de Joaquín, un estudiante inventado: hace tres semanas duerme menos de 6 horas y lleva la mochila llena de dulces como comida. Escribe cómo pediría ayuda con los tres pasos (hecho, sentimiento, petición) y una propuesta para su curso con quién, cuándo y cómo se evaluará.", "Ayuda: «Hace tres semanas duermo menos de 6 horas; me siento cansado; necesito ayuda para organizar mi horario». Propuesta: pausa activa de 5 minutos a las 10:30 con turnos de estudiantes; evaluar en un mes.", ["pide ayuda con tres pasos", "propone algo concreto para el curso", "dice quién, cuándo y cómo evaluar", "no cuenta nada personal"], ["texto escrito"], ["propuesta vaga", "no pedir algo concreto"], "Reconoce la claridad y pregunta ante quién la presentaría."),
    reinforce="Escribe una petición de ayuda con tres pasos para un personaje de cuento.",
    extend="Redacta una propuesta de bienestar para tu curso con qué, quién, cuándo y evaluación.",
)
