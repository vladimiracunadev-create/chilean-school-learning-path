"""Filosofía 3.º medio FG: OA 05 (diálogo sobre problemas ontológicos y epistemológicos). Diálogos y casos de ejemplo inventados."""
from __future__ import annotations

from fg_filo_common import build

O5 = "FG-FILO-3M-OAC-05"

# ============================================================ OA 05, clase 1
F = ("Ficha 1 (diálogo de ejemplo): Lía dice «Esa mesa existe aunque nadie la mire». Mateo responde «No sé: yo solo conozco lo que veo. Si cierro los ojos, ¿cómo sé que sigue ahí?». "
     "Lía contesta «Si me tropiezo con ella, me duele». Mateo replica «Ese dolor lo siento yo; no prueba que la mesa exista fuera de mí».")
build(
    O5, 1, F,
    use="Aprenderé a reconocer en una conversación cotidiana un problema ontológico (qué existe) y uno epistemológico (cómo lo sabemos), y a dialogar sobre ellos con razones.",
    prior=["Sé que la epistemología estudia el conocimiento.", "Sé distinguir creer de saber.", "Sé que una razón puede revisarse."],
    explain=[
        "La ontología es la rama de la filosofía que pregunta qué existe y cómo es la realidad. Una pregunta ontológica es, por ejemplo, «¿existe esa mesa aunque nadie la mire?». La epistemología pregunta cómo sabemos las cosas: «¿cómo sé que la mesa sigue ahí si cierro los ojos?». Ambas se mezclan en las conversaciones, y conviene separarlas para que el diálogo avance.",
        "La realidad es lo que existe; la apariencia es cómo algo se nos muestra. A veces coinciden y a veces no: una torre lejana se ve pequeña, pero no es pequeña. Por eso Mateo pregunta si basta con lo que percibe. Un diálogo filosófico es una conversación en que dos o más personas examinan razones para entender mejor un problema, no para ganar.",
        "Para dialogar bien se siguen cuatro reglas: formular con claridad la pregunta; pedir y dar razones; reconocer lo que se acepta de la otra persona; y estar dispuesto a cambiar de opinión si aparecen razones mejores. Problematizar la situación es descubrir qué se afirma, qué se da por supuesto y qué pregunta queda abierta.",
    ],
    vocab=[("ontología", "rama de la filosofía que estudia qué existe y cómo es la realidad"), ("realidad", "lo que existe"), ("apariencia", "modo en que algo se nos muestra, que puede coincidir o no con cómo es"), ("diálogo filosófico", "conversación en que se examinan razones para entender un problema, no para ganar"), ("supuesto", "idea que se da por cierta sin haberla mostrado")],
    worked=[
        ("Clasificar una pregunta", "Una compañera de ejemplo pregunta: «¿Existen los sueños aunque nadie los recuerde?». ¿La pregunta es ontológica o epistemológica?", ["Pregunta si algo existe.", "No pregunta cómo lo sabemos."], "Ontológica"),
        ("Detectar un supuesto", "Un amigo de ejemplo dice: «Veo un charco en la carretera, por lo tanto hay agua». ¿Qué supone?", ["Supone que lo que se ve coincide con lo que hay.", "Pero un espejismo muestra agua donde no la hay."], "Que la apariencia coincide con la realidad"),
    ],
    mistakes=[("Mezclar la pregunta «qué existe» con «cómo lo sé» y responder solo una.", "Son preguntas distintas aunque conectadas.", "Anota por separado la pregunta ontológica y la epistemológica."),
              ("Tomar el diálogo como una competencia para ganar.", "Se buscan razones, no victorias.", "Pide razones, reconoce aciertos y cambia de opinión si hay razones mejores.")],
    T=[
        ('abc', '{F} ¿Cuál es la pregunta ontológica de la ficha?', '¿Existe la mesa aunque nadie la mire?', '¿Cómo puedo asegurarme de que la mesa sigue ahí?', '¿Quién tiene mejor argumento, Lía o Mateo?', 'La ontológica pregunta si algo existe; la otra pregunta cómo se sabe y la tercera evalúa personas.'),
        ('abc', '{F} ¿Cuál es la pregunta epistemológica de la ficha?', '¿Cómo sé que la mesa sigue ahí si cierro los ojos?', '¿Existe la mesa aunque nadie la mire?', '¿Es correcto que Mateo dude de lo que dice Lía?', 'La epistemológica pregunta por el modo de saber; la segunda es ontológica y la tercera un juicio de valor.'),
        ('abc', '{F} ¿Qué razón da Lía a favor de que la mesa existe fuera de ella?', 'Que se tropieza con la mesa y le duele', 'Que todas las personas ven siempre la mesa', 'Que la mesa es de madera y pesa mucho', 'Lía nombra el tropiezo y el dolor; no habla de lo que ven otras personas ni de la madera.'),
        ('abc', '{F} ¿Qué objeción plantea Mateo a esa razón?', 'Que el dolor lo siente él y no prueba que la mesa exista fuera de él', 'Que Lía nunca se ha tropezado con una mesa y no puede hablar de dolor', 'Que las mesas no pueden causar dolor a nadie', 'Mateo no niega el dolor: discute qué demuestra, que es una pregunta sobre la evidencia.'),
        ('abc', '{F} Mateo dice «solo conozco lo que veo». ¿Qué supone?', 'Que lo conocido se limita a lo que percibe, sin salir de ello', 'Que la mesa no puede ser vista por otras personas y solo existe para él', 'Que Lía miente cuando habla de su dolor', 'Pone la percepción como límite del conocimiento; eso es un supuesto que se puede discutir.'),
        ('abc', 'En un diálogo filosófico, ¿qué conducta va contra sus reglas?', 'Responder «tú no entiendes nada» en vez de dar razones', 'Pedir a la otra persona que explique su razón', 'Reconocer que un argumento de la otra persona es bueno', 'El diálogo filosófico pide razones; descalificar a la persona las reemplaza por un ataque.'),
        ('abc', 'Una torre lejana se ve más pequeña que una cercana, pero mide lo mismo. ¿Qué se distingue aquí?', 'La apariencia, que cambia con la distancia, y la realidad, que no cambia', 'La opinión de quien mira y los datos de quien mide', 'La razón, que sabe, y los sentidos, que no sirven para nada', 'Cómo se ve la torre cambia; cómo es no cambia. Los sentidos informan aunque a veces engañen.'),
        ('abc', '{F} ¿Qué observación apoyaría más la tesis de Lía de que la mesa existe fuera de ellos?', 'Que otra persona distinta la toque y la describa igual', 'Que Lía repita su afirmación con más fuerza', 'Que Mateo olvide la mesa por un rato', 'Que dos personas independientes coincidan es evidencia compartida; repetir con fuerza no lo es.'),
        ('abc', '{F} ¿Qué punto de acuerdo hay entre Lía y Mateo?', 'Ambos aceptan que hay una experiencia, el dolor o la visión, y discuten qué muestra', 'Ambos aceptan que la mesa existe y discuten de qué color es', 'Ambos aceptan que no se puede saber nada, por lo que no hay más que preguntar', 'Mateo no niega la experiencia, solo pregunta qué prueba; en eso coinciden.'),
        ('abc', '¿Cuál es una pregunta ontológica?', '¿Existen los números aunque nadie los piense?', '¿Cómo se comprueba que un dato es verdadero?', '¿Qué hacer si un amigo me pide copiar en una prueba?', 'Pregunta si algo existe; las otras son de conocimiento y de ética.'),
        ('{F} Escribe la objeción de Mateo como una pregunta que Lía pueda responder.', '¿Cómo sabes que el dolor viene de la mesa y no solo de ti?', 'Convierte la duda sobre la evidencia en una pregunta que pide una razón.'),
        ('abc', '{F} Lía dice: «Si Mateo sigue dudando es porque no quiere entender». ¿Qué error comete?', 'Atribuye una mala intención a Mateo en vez de responder su razón', 'Pide una razón a Mateo y la analiza con cuidado', 'Acepta la objeción de Mateo y cambia de postura', 'Atacar las intenciones de la persona evita contestar su argumento.'),
        ('abc', '{F} ¿Qué conclusión prudente es posible después de este diálogo?', 'Falta una razón que muestre que el dolor tiene una causa fuera de Mateo', 'Mateo demostró que la mesa no existe fuera de la mente', 'Lía demostró que cualquier objeto existe sin que nadie lo perciba, y que Mateo debe aceptarlo', 'Ninguno probó su tesis todavía; conviene reconocer lo que falta en vez de declarar ganador.'),
    ],
    ctx=('abc', 'En el recreo, una amiga de ejemplo dice: «La luna sigue ahí aunque esté nublado y no se vea». Otra pregunta: «¿Cómo lo sabes si no la ves?». ¿Qué tipo de pregunta hizo la segunda?', 'Epistemológica: pide cómo se sabe que la luna sigue allí', 'Ontológica: pregunta si la luna existe aunque nadie la mire desde la Tierra', 'Ética: pregunta si está bien mirar la luna', 'Pregunta por el modo de saber y no si existe ni qué debemos hacer.'),
    sc=[
        ('En Filosofía: ¿qué estudia la ontología?', 'Qué existe y cómo es la realidad', 'Es la rama que pregunta por lo que existe.'),
        ('abc', '¿Qué es una apariencia?', 'El modo en que algo se nos muestra, que puede coincidir o no con cómo es', 'Lo que existe realmente aunque nadie lo vea', 'Una opinión que comparte la mayoría del grupo', 'La apariencia es cómo algo se muestra; no siempre coincide con cómo es.'),
        ('¿Cuál es el objetivo del diálogo filosófico?', 'Entender mejor un problema examinando razones', 'No es ganar, sino examinar razones para comprender mejor.'),
    ],
    op=("Usa la {F} Escribe cinco líneas: (1) una pregunta ontológica; (2) una epistemológica; (3) un supuesto de cada persona; (4) una razón que Lía podría añadir; (5) una pregunta nueva para continuar el diálogo.",
        "(1) ¿Existe la mesa si nadie la mira? (2) ¿Cómo sé que sigue ahí? (3) Lía supone que el dolor viene de la mesa; Mateo supone que solo conoce lo que percibe. (4) Otra persona la toca y la describe igual. (5) ¿Qué lograría convencer a Mateo?",
        ["separa las dos preguntas", "nombra supuestos", "añade una razón", "formula una pregunta que continúa"], ["cinco líneas"], ["mezclar las preguntas", "decidir quién gana"],
        "Pide que explique por qué su pregunta final ayuda al diálogo."),
    reinforce="Escribe una pregunta ontológica y una epistemológica sobre un objeto de tu casa.",
    extend="Conversa con una persona de confianza sobre qué razón la convencería de algo que duda y anota qué reglas del diálogo usaron.",
)

# ============================================================ OA 05, clase 2
F = ("Ficha 2 (cuatro afirmaciones de ejemplo): (1) «La pared de la sala mide 4 metros de largo». (2) «El azul es el color más tranquilo». "
     "(3) «Los números primos son infinitos, aunque nadie los esté pensando». (4) «Aquella figura parece una persona, pero es un abrigo colgado de una percha».")
build(
    O5, 2, F,
    use="Aprenderé a definir los conceptos con que se discuten problemas ontológicos y epistemológicos: realidad, apariencia, objetivo, subjetivo, realismo e idealismo.",
    prior=["Sé que la ontología pregunta qué existe.", "Sé distinguir apariencia y realidad.", "Sé que un diálogo se apoya en razones."],
    explain=[
        "Un concepto es una idea general que usamos para pensar y para hablar. Definirlo es decir qué incluye y qué deja fuera. Algo es objetivo cuando es verdadero o existe con independencia de lo que cada persona piense o sienta: el largo de una pared se puede medir y otras personas obtienen lo mismo. Algo es subjetivo cuando depende de cada persona, como un gusto o una sensación.",
        "El realismo es la postura que sostiene que la realidad existe independiente de que alguien la perciba o la piense. El idealismo sostiene que la realidad depende de la mente: lo que llamamos mundo son ideas o experiencias de quien lo conoce. Son posturas generales, y existen versiones moderadas de cada una. Una apariencia engaña cuando se toma como si fuera la realidad: la figura que parece una persona, pero es un abrigo.",
        "Distinguir bien evita discusiones sin salida. Que algo sea subjetivo no significa que sea falso ni que no importe, sino que su verdad depende de quien lo experimenta. Y que algo sea objetivo no significa que alguien lo haya medido: puede ser objetivo aunque nadie lo haya comprobado todavía.",
    ],
    vocab=[("concepto", "idea general que usamos para pensar y hablar, cuyo alcance se define"), ("objetivo", "que existe o es verdadero con independencia de lo que cada persona piense o sienta"), ("subjetivo", "que depende de cada persona, como un gusto o una sensación"), ("realismo", "postura según la cual la realidad existe aunque nadie la perciba"), ("idealismo", "postura según la cual la realidad depende de la mente que la conoce")],
    worked=[
        ("Objetivo o subjetivo", "«Esta sopa está muy rica», dice Ema de ejemplo. «La sopa tiene 60 grados», dice su hermano tras medirla. ¿Cuál es objetiva?", ["La temperatura se mide y otros obtienen lo mismo.", "«Rica» depende del gusto de cada persona."], "La temperatura es objetiva; «rica» es subjetiva"),
        ("Realismo o idealismo", "Un estudiante de ejemplo afirma: «La montaña existe aunque nadie la mire». ¿Qué postura expresa?", ["Afirma que la realidad es independiente de ser percibida.", "Eso es el realismo."], "Realismo"),
    ],
    mistakes=[("Creer que lo subjetivo es siempre falso o sin importancia.", "Se confunde depender de la persona con ser falso.", "Lo subjetivo es verdadero para quien lo experimenta, pero no se mide igual para todos."),
              ("Decir que algo solo es objetivo si alguien lo ha comprobado.", "Se confunde ser objetivo con haber sido comprobado.", "Objetivo es existir con independencia de lo que se piense; se comprueba aparte.")],
    T=[
        ('abc', '¿Qué significa que algo sea objetivo?', 'Que existe o es verdadero con independencia de lo que piense cada persona', 'Que casi todas las personas están de acuerdo con ello, aunque nadie lo haya medido jamás', 'Que ya fue comprobado por alguien con instrumentos', 'Objetivo se refiere a independencia de las opiniones; el acuerdo o la comprobación son otra cosa.'),
        ('abc', '{F} ¿Cuál afirmación es subjetiva?', 'La 2, porque depende de lo que cada persona siente', 'La 1, porque la mide una sola persona con una cinta y puede equivocarse', 'La 3, porque habla de algo que nadie ve', 'La 2 expresa una sensación sobre un color; las otras se refieren a medidas o a propiedades de los números.'),
        ('abc', '{F} ¿Cómo se puede comprobar la afirmación 1?', 'Midiendo la pared con un instrumento que otras personas también usen', 'Preguntando qué piensa la mayoría del curso sobre el tamaño de la sala', 'Imaginando una sala del mismo tamaño y comparándola', 'Una medida repetible por otros es la forma de comprobar algo objetivo como el largo.'),
        ('abc', '{F} La afirmación 3 dice que algo es verdadero aunque nadie lo piense. ¿Qué idea expresa?', 'Que lo verdadero no depende de lo que alguien piense', 'Que lo verdadero depende de lo que piensa cada persona', 'Que nada puede ser verdadero si nadie lo piensa', 'Es una idea cercana a lo objetivo: la verdad no depende de que alguien la piense.'),
        ('abc', '{F} En la afirmación 4, ¿cuál es la apariencia?', 'Que la figura parece una persona', 'Que hay un abrigo colgado de una percha', 'Que alguien dice que no es una persona', 'Parece una persona es cómo se muestra; el abrigo es lo que realmente es.'),
        ('abc', '{F} En la afirmación 4, ¿cuál es la realidad?', 'Que es un abrigo colgado', 'Que parece una persona', 'Que alguien se asustó con la figura', 'La realidad es lo que existe: un abrigo; que parezca una persona es solo la apariencia.'),
        ('abc', '¿Qué sostiene el realismo?', 'Que la realidad existe aunque nadie la perciba o la piense', 'Que solo existe lo que alguien percibe en cada momento', 'Que todo conocimiento nace de la razón y no de los sentidos', 'El realismo dice que lo real es independiente; la segunda es idealista y la tercera es un debate sobre el conocimiento.'),
        ('abc', '¿Qué sostiene el idealismo?', 'Que la realidad depende de la mente que la conoce', 'Que lo real existe aunque nadie lo piense', 'Que lo importante es actuar de manera ideal en la vida', 'Idealismo aquí es una tesis sobre qué es lo real; no se refiere a tener metas elevadas.'),
        ('abc', 'Una estudiante dice: «Como el helado me gusta, el helado de ese sabor es verdadero para todos». ¿Qué confunde?', 'Confunde un gusto subjetivo con algo objetivo', 'Confunde la apariencia con la realidad de un objeto', 'Confunde un hecho medible con un deseo', 'Un gusto depende de cada persona y no se vuelve verdadero para todos.'),
        ('abc', '{F} ¿Qué diría una persona realista sobre la afirmación 3?', 'Que es verdadera aunque nadie la esté pensando', 'Que solo es verdadera mientras alguien la piensa', 'Que no puede decirse nada, porque no se puede medir', 'El realismo sostiene que lo real y lo verdadero no dependen de que alguien lo piense.'),
        ('abc', 'Dos amigos discuten: uno dice «el rojo es más bonito», el otro «el rojo tiene mayor longitud de onda que el azul». ¿Cuál afirmación es objetiva?', 'La segunda, porque puede medirse y comprobarse', 'La primera, porque cada persona la siente con más fuerza', 'Ambas, porque las dijeron personas distintas', 'Una medida se comprueba; «más bonito» es gusto.'),
        ('Si algo es subjetivo, ¿significa por eso que es falso?', 'No: depende de la persona, pero puede ser verdadero para quien lo siente', 'Subjetivo no es falso: es verdadero según quien lo experimenta, como un dolor que alguien siente.'),
        ('abc', '{F} ¿Qué se pierde si se toma la apariencia de la afirmación 4 como si fuera la realidad?', 'Se cree que hay una persona donde solo hay un abrigo', 'Se cree que el abrigo no tiene percha', 'Se cree que las personas no pueden ser vistas', 'Tomar la apariencia por realidad lleva a creer algo que no hay.'),
    ],
    ctx=('abc', 'Una profesora de ejemplo dice: «No sé si el cuaderno que estaba sobre el escritorio sigue ahí; pero creo que existe aunque nadie lo mire». ¿Qué postura expresa?', 'Realista, porque afirma que el cuaderno existe sin que nadie lo perciba', 'Idealista, porque depende de lo que alguien piense', 'Escéptica, porque duda de que el cuaderno exista', 'Afirma que lo real existe independiente de ser percibido, que es el realismo.'),
    sc=[
        ('En Filosofía: ¿qué es algo subjetivo?', 'Algo que depende de cada persona', 'Es lo que cambia según quien lo experimenta.'),
        ('abc', '¿Cuál es un ejemplo de afirmación objetiva?', 'El agua del vaso está a 20 grados', 'Ese paisaje me da paz', 'La música de ese cantante es la mejor', 'Una temperatura se mide y otros obtienen lo mismo; las otras expresan gustos o sensaciones.'),
        ('¿Qué sostiene el idealismo en este cuaderno?', 'Que la realidad depende de la mente que la conoce', 'Es la tesis de que lo real depende de la mente.'),
    ],
    op=("Usa la {F} Clasifica las cuatro afirmaciones en objetivas o subjetivas y para cada una escribe una razón de una línea. Luego explica en dos líneas cómo se vería el realismo y cómo el idealismo en la afirmación 3.",
        "1 objetiva (se mide); 2 subjetiva (gusto); 3 objetiva (propiedad de los números); 4 objetiva en su realidad (es un abrigo) aunque su apariencia engañe. Realismo: es verdadera aunque nadie la piense. Idealismo: su verdad depende de que alguien la piense.",
        ["clasifica con razón", "distingue realismo e idealismo", "no mezcla apariencia y realidad"], ["cuatro clasificaciones", "dos líneas de explicación"], ["decir que subjetivo es falso", "mezclar los conceptos"],
        "Pregunta cómo cambiaría su clasificación si la afirmación 2 fuera «el azul se asocia con calma en esa comunidad»."),
    reinforce="Escribe un ejemplo objetivo y uno subjetivo de tu vida diaria.",
    extend="Busca una apariencia que haya sido engañosa para ti o alguien cercano y escribe cómo se descubrió la realidad.",
)

# ============================================================ OA 05, clase 3
F = ("Ficha 3 (dos posturas de ejemplo): "
     "Postura realista: «El mundo existe aunque nadie lo perciba. Si una roca cae en un bosque vacío, cae igual. Además, el mundo me sorprende: si dependiera de mí, no me llevaría sorpresas.» "
     "Postura idealista: «Solo conozco mis ideas y mis sensaciones. Lo que llamo mundo es lo que se me presenta en la mente, y no puedo salir de ella para comprobar una realidad aparte.»")
build(
    O5, 3, F,
    use="Aprenderé a reconstruir con fidelidad dos perspectivas sobre la realidad (realista e idealista), a contrastarlas y a explicar en qué coinciden y en qué no.",
    prior=["Sé qué sostienen el realismo y el idealismo.", "Sé que reconstruir es exponer tesis, razones, ejemplo y límite.", "Sé que no hay que deformar la postura de otra persona."],
    explain=[
        "Reconstruir una perspectiva sobre un problema ontológico es decir con fidelidad su tesis, sus razones, su ejemplo y el límite que se le puede señalar. La postura realista tiene como tesis que el mundo existe independiente de la mente. Sus razones son el ejemplo de la roca que cae en el bosque vacío y que el mundo nos sorprende. Un límite es que, para comprobarlo, siempre dependemos de nuestra experiencia.",
        "La postura idealista tiene como tesis que la realidad depende de la mente. Su razón es que solo conocemos ideas y sensaciones, y que no podemos salir de nuestra mente para comparar con algo exterior. Un límite es que debe explicar por qué las experiencias de distintas personas coinciden y por qué el mundo nos sorprende.",
        "Contrastar es buscar puntos de acuerdo y de desacuerdo. Ambas posturas aceptan que existe la experiencia; discrepan sobre si esa experiencia remite a algo fuera de la mente. Una réplica es la respuesta que una postura daría a la objeción de la otra. Una buena réplica reconoce lo acertado de la objeción antes de responder.",
    ],
    vocab=[("reconstruir", "exponer con fidelidad la tesis, las razones, el ejemplo y el límite de una postura"), ("réplica", "respuesta que una postura da a una objeción"), ("coincidir", "estar de acuerdo en un punto"), ("independiente de la mente", "que existe aunque nadie lo piense ni lo perciba"), ("remitir", "apuntar hacia algo que está fuera de lo que se experimenta")],
    worked=[
        ("Reconstruir una tesis", "Un compañero de ejemplo resume la postura idealista así: «Los idealistas creen que el mundo es una mentira». ¿Es fiel?", ["La postura dice que la realidad depende de la mente.", "No dice que sea una mentira; el resumen la deforma."], "No es fiel"),
        ("Dar una réplica", "Objeción de ejemplo al realismo: «Siempre conocemos el mundo a través de la experiencia». ¿Qué réplica podría darse?", ["Reconoce que se conoce por experiencia.", "Responde que la sorpresa muestra algo que no controlamos."], "Reconocer la objeción y responder con la sorpresa"),
    ],
    mistakes=[("Contrastar posturas diciendo cuál tiene razón antes de reconstruirlas.", "Se juzga sin haber entendido.", "Primero expón tesis, razones y límite de cada una."),
              ("Creer que si dos posturas coinciden en un punto, son la misma.", "Se confunde coincidir con ser idénticas.", "Anota coincidencias y desacuerdos por separado.")],
    T=[
        ('abc', '{F} ¿Cuál es la tesis de la postura realista?', 'El mundo existe aunque nadie lo perciba', 'El mundo es una ilusión creada por cada mente', 'Solo existen las ideas que alguien piensa', 'La tesis es la afirmación central; las otras opciones describen el idealismo.'),
        ('abc', '{F} ¿Qué ejemplo usa la postura realista?', 'Una roca que cae en un bosque vacío', 'Un sueño que se olvida al despertar', 'Una torre que se ve pequeña a lo lejos', 'El ejemplo de la ficha es la roca; los otros no aparecen en la postura.'),
        ('abc', '{F} ¿Qué razón da la postura idealista?', 'Que solo conocemos nuestras ideas y no podemos salir de la mente para comprobar algo aparte', 'Que el mundo cambia cuando cambia de opinión una persona', 'Que las sorpresas del mundo prueban que no dependemos de la mente', 'La razón es que solo accedemos a nuestras ideas; la tercera opción es una razón del realismo.'),
        ('abc', '{F} ¿Qué límite se le puede plantear a la postura idealista?', 'Explicar por qué distintas personas tienen experiencias que coinciden', 'Que niega que las personas tengan experiencias propias', 'Que afirma que el mundo existe sin que nadie lo piense', 'Si la realidad depende de cada mente, hay que explicar la coincidencia entre mentes.'),
        ('abc', '{F} ¿Qué límite se le puede plantear a la postura realista?', 'Que para comprobar que el mundo existe siempre dependemos de nuestra experiencia', 'Que no puede explicar por qué el mundo nos sorprende', 'Que necesita estudiar ciencias para entenderse', 'El límite es cómo comprobar algo exterior a la experiencia sin usar la experiencia.'),
        ('abc', '{F} ¿En qué coinciden ambas posturas?', 'En que existe la experiencia y hay que explicarla', 'En que el mundo existe solo cuando alguien lo mira', 'En que los sentidos no sirven para conocer', 'Ambas aceptan que tenemos experiencias; discrepan sobre a qué remiten.'),
        ('abc', '{F} ¿En qué discrepan?', 'En si la experiencia remite a algo fuera de la mente', 'En si hay experiencias o no las hay', 'En si conviene dialogar o callar', 'Su desacuerdo es sobre qué hay detrás de la experiencia.'),
        ('abc', '{F} Un compañero dice: «Los realistas niegan que la mente participe en el conocimiento». ¿Es fiel?', 'No: el realismo afirma que la realidad es independiente, no que la mente no participe', 'Sí: el realismo cree que la mente no sirve para conocer y que solo los sentidos cuentan', 'Sí: el realismo sostiene que solo existe la mente', 'La tesis realista se refiere a la existencia del mundo, no niega que se conozca con la mente.'),
        ('abc', '{F} Un idealista objeta: «Tu roca solo existe en tu pensamiento al imaginarla». ¿Qué réplica realista reconoce la objeción y responde?', 'Imaginarla es una idea mía; pero que el mundo me sorprenda sugiere algo que no depende de mí', 'No hay objeción posible: las rocas existen y no hace falta dar razones', 'Tienes razón: nada existe fuera de la mente', 'Una buena réplica reconoce algo de la objeción y responde con una razón, no la ignora ni se rinde.'),
        ('abc', '{F} Una réplica idealista a «el mundo me sorprende» podría ser…', 'Que las sorpresas también son experiencias y no prueban que hay algo exterior', 'Que si el mundo sorprende, es que existe fuera de la mente', 'Que la sorpresa es mala para pensar con claridad', 'Es una réplica coherente con su tesis: la sorpresa es otra experiencia de la mente.'),
        ('abc', 'Para contrastar dos posturas con justicia, ¿qué conviene hacer primero?', 'Exponer cada una con su tesis, razones y límite antes de juzgar', 'Elegir la que más se parezca a lo que ya pensamos', 'Buscar el error más grande de cada una y quedarse con eso', 'Primero se comprende; juzgar antes puede deformar lo que dicen.'),
        ('{F} Escribe una pregunta que un realista podría hacerle a un idealista.', '¿Cómo explicas que dos personas distintas tengan experiencias que coinciden?', 'Apunta al límite del idealismo: cómo explicar la coincidencia entre mentes.'),
        ('abc', '{F} ¿Qué dato nuevo sería más difícil de explicar para el idealismo?', 'Que dos personas distintas describan lo mismo sin haberse comunicado', 'Que una persona sueñe con algo que no existe y lo recuerde con mucha claridad', 'Que alguien dude de lo que ve', 'La coincidencia independiente entre mentes presiona a explicar qué la causa.'),
    ],
    ctx=('abc', 'En una clase de ejemplo, Gonzalo dice: «Para mí, el mundo existe aunque nadie lo vea». Rocío responde: «Pero tú solo lo sabes porque lo percibes». ¿Qué hace Rocío?', 'Plantea una objeción basada en que conocemos por la experiencia', 'Afirma que Gonzalo se equivoca porque el mundo no existe', 'Cambia de tema para evitar la discusión', 'Su objeción es epistemológica: señala el límite de comprobar algo sin experiencia.'),
    sc=[
        ('En Filosofía: ¿qué es una réplica?', 'La respuesta que una postura da a una objeción', 'Es la respuesta a una objeción hecha desde la otra postura.'),
        ('abc', '¿Qué conviene incluir al reconstruir una postura?', 'Tesis, razones, ejemplo y límite', 'Una opinión personal sobre su autor', 'Una lista de las personas que la apoyan', 'Reconstruir es exponer con fidelidad su contenido, no a quién pertenece ni cuántos la apoyan.'),
        ('¿En qué punto coinciden realistas e idealistas?', 'En que existe la experiencia', 'Ambos parten de que tenemos experiencias y discrepan en lo que hay tras ellas.'),
    ],
    op=("Usa la {F} Escribe una tabla de dos columnas (realista, idealista) con filas: tesis, una razón, un ejemplo o apoyo, un límite y una réplica. Termina con una frase sobre en qué coinciden.",
        "Realista: tesis, el mundo existe aunque nadie lo perciba; razón, la sorpresa; ejemplo, la roca; límite, depende de la experiencia; réplica, la sorpresa sugiere algo exterior. Idealista: tesis, la realidad depende de la mente; razón, solo conocemos ideas; límite, explicar la coincidencia entre mentes. Coinciden en que hay experiencia.",
        ["reconstruye ambas posturas con fidelidad", "señala límites y réplicas", "indica una coincidencia"], ["tabla de cinco filas", "frase final"], ["deformar una postura", "concluir cuál es mejor sin argumentos"],
        "Pregunta qué evidencia nueva haría dudar a cada postura."),
    reinforce="Escribe en tres líneas la tesis, una razón y un límite del realismo.",
    extend="Explica a una persona de tu casa la diferencia entre realismo e idealismo con un ejemplo cotidiano.",
)

# ============================================================ OA 05, clase 4
F = ("Ficha 4 (argumento de ejemplo): «Premisa 1: si las cosas existieran solo cuando las percibo, mi silla desaparecería cuando salgo del cuarto. "
     "Premisa 2: cuando vuelvo, la silla está donde la dejé, y mi hermana dice que estuvo ahí todo el rato. Conclusión: las cosas no existen solo cuando las percibo». "
     "Objeción de ejemplo: «Tu hermana también aparece en tu experiencia; lo que dice es parte de lo que percibes».")
build(
    O5, 4, F,
    use="Aprenderé a formular un argumento propio sobre un problema ontológico o epistemológico, a evaluarlo, a recibir una objeción y a responderla con razones.",
    prior=["Sé reconstruir posturas realista e idealista.", "Sé que un argumento tiene premisas y conclusión.", "Sé qué es una réplica."],
    explain=[
        "Un argumento propio se arma con tres partes: una tesis (lo que sostengo), premisas (las razones) y una conclusión coherente con ellas. Para que las razones apoyen la tesis, deben ser verdaderas o creíbles, relevantes y suficientes. En la ficha, la conclusión dice que las cosas no existen solo cuando las percibo; las premisas dan una razón de la vida diaria.",
        "Una objeción es una razón que cuestiona el argumento: puede atacar una premisa, la relación entre premisas y conclusión, o un supuesto. La objeción de ejemplo ataca la premisa 2: dice que el testimonio de la hermana también es parte de mi experiencia, por lo que no sale de ella. Una buena respuesta no ignora la objeción: la reconoce, dice qué parte acepta y qué razón nueva agrega.",
        "Al final conviene expresar la posición con prudencia: qué sostengo, qué razones tengo, qué objeción me parece más fuerte y qué podría hacerme cambiar de idea. Una posición revisable es una tesis que se defiende con razones y que se cambia si aparecen razones mejores; eso no es debilidad, es honestidad intelectual.",
    ],
    vocab=[("tesis", "lo que se sostiene y se defiende con razones"), ("objeción", "razón que cuestiona un argumento"), ("posición revisable", "tesis defendida con razones y abierta a cambiar si aparecen razones mejores"), ("coherente", "que no se contradice con lo que se dijo antes"), ("honestidad intelectual", "decir hasta dónde llegan mis razones y reconocer lo que no sé")],
    worked=[
        ("Ubicar la objeción", "Un argumento de ejemplo dice: «Todos los que conozco usan reloj, así que todas las personas usan reloj». Un compañero objeta: «Tu muestra es muy pequeña». ¿Qué ataca la objeción?", ["La conclusión pasa de pocos casos a todos.", "La objeción ataca que las razones no bastan."], "Ataca la suficiencia de las premisas"),
        ("Responder una objeción", "Objeción de ejemplo: «Tu prueba depende de la palabra de tu amigo». ¿Qué respuesta es más honesta?", ["Reconoce que depende de su palabra.", "Agrega una razón independiente."], "Aceptar la parte cierta y agregar otra razón"),
    ],
    mistakes=[("Responder a una objeción repitiendo la tesis con más fuerza.", "Repetir no es dar razones nuevas.", "Reconoce lo cierto de la objeción y añade una razón."),
              ("Cambiar de tesis sin avisar para no perder la discusión.", "Se oculta el cambio y se pierde coherencia.", "Si cambias, di qué razón te hizo cambiar.")],
    T=[
        ('abc', '{F} ¿Cuál es la tesis del argumento?', 'Que las cosas no existen solo cuando las percibo', 'Que la silla está donde la dejó el autor del argumento', 'Que la hermana siempre dice la verdad en todo', 'La conclusión que se defiende es la tesis; la silla es parte de las razones.'),
        ('abc', '{F} ¿Qué dato apoya la premisa 2?', 'Que la silla está donde se dejó y que la hermana dice que estuvo ahí', 'Que la silla desaparece al salir', 'Que las cosas cambian cuando nadie las mira', 'La premisa 2 menciona dos hechos: la silla en su lugar y el testimonio.'),
        ('abc', '{F} ¿Qué parte del argumento ataca la objeción de ejemplo?', 'La premisa 2, al decir que el testimonio también es parte de lo que percibo', 'La conclusión, al decir que las sillas se perciben mal', 'La premisa 1, al negar que la silla desaparezca al salir', 'La objeción discute el valor del testimonio de la hermana, que es la premisa 2.'),
        ('abc', '{F} ¿Qué respuesta a la objeción reconoce lo cierto y agrega una razón?', 'Es cierto que su palabra es parte de mi experiencia; pero además la silla estaba intacta y nadie pudo moverla', 'No hay nada que responder, porque mi hermana nunca miente', 'La objeción no vale, porque quien la dijo no tiene razón', 'Reconocer la parte válida y agregar una razón nueva es una respuesta honesta.'),
        ('abc', '{F} ¿Qué respuesta NO responde la objeción?', 'Repetir que las cosas existen aunque no las percibo, cada vez más fuerte', 'Agregar una razón independiente del testimonio de la hermana, como un registro hecho por otra persona', 'Aceptar que el testimonio no basta y buscar otro dato', 'Repetir la tesis no entrega razones nuevas.'),
        ('abc', 'Una posición revisable es…', 'Una tesis defendida con razones y abierta a cambiar si aparecen razones mejores', 'Una tesis que cambia cada vez que alguien la critica', 'Una tesis que nadie puede discutir porque ya fue revisada', 'Se defiende con razones, pero se mantiene abierta a corregirse; ni cambia por presión ni se cierra.'),
        ('abc', '{F} ¿Qué haría más fuerte la premisa 2 ante la objeción?', 'Un dato distinto del testimonio, como una cámara que registre la silla', 'Que la hermana lo repita con seguridad', 'Que otra persona de la casa diga que no sabe', 'Agrega una razón distinta del testimonio de la hermana, que era lo objetado.'),
        ('abc', '{F} Si la conclusión dijera «las cosas existen siempre, también cuando nadie las percibe», ¿qué faltaría?', 'Más razones, porque las premisas solo muestran un caso con una silla', 'Ninguna: una silla basta para hablar de todas las cosas', 'Una opinión de quien no vio la silla', 'Una sola silla no basta para una conclusión general sobre todas las cosas.'),
        ('abc', '¿Cuál es la mejor forma de cerrar una argumentación propia?', 'Decir qué sostengo, qué razones tengo, qué objeción es la más fuerte y qué me haría cambiar', 'Decir que tengo razón y que quien piense distinto no entiende', 'Decir que todas las posturas valen lo mismo, así no hay que dar razones', 'Una posición revisable muestra razones y reconoce objeciones; no cierra con ataques ni con falta de criterio.'),
        ('abc', '{F} ¿Qué es coherente con el argumento?', 'Concluir que algunas cosas probablemente existen aunque no las perciba', 'Concluir que nada existe si no lo percibo', 'Concluir que mi hermana no existe', 'La conclusión debe ser consistente con la premisa: la silla sigue estando.'),
        ('{F} Escribe una objeción a la premisa 2 distinta de la de la ficha.', 'Que la silla podría haber sido movida y regresada sin que mi hermana lo notara.', 'Cuestiona el hecho de que nadie pudo moverla, que es lo que sostiene la premisa 2.'),
        ('abc', 'Una compañera de ejemplo cambia de tesis después de oír una objeción. ¿Qué conviene que haga?', 'Decir qué razón la hizo cambiar', 'Hacer como si siempre hubiera pensado lo mismo', 'Dejar de participar en el diálogo', 'Cambiar de posición con razones muestra honestidad intelectual.'),
        ('abc', '{F} Un argumento con dos premisas verdaderas y una conclusión que no se desprende de ellas es…', 'Débil, porque las razones no bastan para sostener la conclusión', 'Fuerte, porque las premisas son verdaderas', 'Sólido, porque la conclusión suena interesante', 'La verdad de las premisas no basta si no apoyan la conclusión.'),
    ],
    ctx=('abc', 'Alguien de ejemplo argumenta: «Si el mundo no existiera fuera de mi mente, nunca me sorprendería; me sorprendo; luego, el mundo existe fuera de mi mente». Un amigo objeta: «Las sorpresas en un sueño también existen». ¿Qué parte ataca la objeción?', 'La relación entre «me sorprendo» y «existe fuera de la mente»', 'La conclusión, diciendo que el mundo no existe', 'La premisa que dice que el mundo no existe', 'Muestra que sorprenderse también ocurre en un sueño, así que la razón no basta.'),
    sc=[
        ('En Filosofía: ¿qué es una objeción?', 'Una razón que cuestiona un argumento', 'Es una razón dirigida a una premisa, a la relación entre razones y conclusión o a un supuesto.'),
        ('abc', '¿Qué es una posición revisable?', 'Tesis defendida con razones, abierta a cambiar si hay razones mejores', 'Tesis que se repite aunque haya objeciones', 'Tesis que se cambia por presión del grupo', 'Revisable es abierta a razones, no a presiones ni a rigidez.'),
        ('¿Qué conviene hacer ante una objeción válida?', 'Reconocer lo cierto y agregar una razón o ajustar la tesis', 'Una objeción válida se reconoce y se responde con una razón nueva o con un ajuste de la tesis.'),
    ],
    op=("Usa la {F} Reescribe el argumento con tus palabras: tesis, dos premisas, la objeción de ejemplo y tu respuesta (reconoce algo y agrega una razón). Cierra con una frase que diga qué te haría cambiar de idea.",
        "Tesis: las cosas existen aunque no las perciba. Premisa 1: la silla sigue donde la dejé. Premisa 2: mi hermana confirma que estuvo allí. Objeción: su palabra es parte de mi experiencia. Respuesta: es cierto, pero además una cámara registró la silla. Cambiaría si la cámara mostrara que alguien movió la silla.",
        ["tesis y premisas claras", "respuesta que reconoce y agrega razón", "indica qué le haría cambiar"], ["argumento de cinco partes"], ["repetir la tesis como respuesta", "no decir qué razón haría cambiar"],
        "Pregunta cuál de sus premisas es la más débil y por qué."),
    reinforce="Escribe una tesis sobre un problema ontológico y una razón que la apoye.",
    extend="Anota una objeción que puedas hacerte a tu propia tesis.",
)
