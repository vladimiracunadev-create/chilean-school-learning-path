"""Cuaderno del estudiante, 2.º básico Orientación: OA 03 (afecto y cuidado con consentimiento) y OA 04 (autocuidado, intimidad e información personal)."""
from __future__ import annotations

from student_content_or2_a import lesson, T, W, M
from student_lessons import ex

OA3, OA4 = "OR02 OA 03", "OR02 OA 04"

# ================================================================ OA 03
lesson(
    OA3, 1,
    "Una hoja y lápiz. Las escenas de familia, curso y barrio están escritas en los ejercicios. Cada familia es distinta y todas valen.",
    "Aprenderé a ver las muchas formas de mostrar cariño y cuidado: tiempo, escucha, palabras y ayuda. Sirve para reconocer el afecto que doy y recibo.",
    ["Sé que las personas se quieren de maneras distintas.", "Sé que hay personas que me cuidan."],
    [
        "El afecto es el cariño que sientes por alguien. El cuidado es hacer algo para que esa persona esté bien. Hay muchas formas de mostrar afecto. Se puede compartir tiempo, escuchar, decir palabras amables o ayudar.",
        "Estas formas ocurren en tres lugares. En la familia, por ejemplo cuando alguien te prepara la once. En la escuela, cuando un compañero te presta un lápiz. En el barrio o la comunidad, cuando un vecino te saluda con una sonrisa. Cada familia expresa el cariño a su manera, y todas valen.",
        "El afecto no siempre es un abrazo ni un regalo. Un regalo caro no muestra más cariño que escuchar con atención. Tú también das afecto: puedes saludar, esperar, ayudar a cargar algo o dar las gracias. Observar estas muestras de cariño te ayuda a valorarlas.",
    ],
    [("afecto", "cariño que siento por alguien"), ("cuidado", "hacer algo para que otro esté bien"), ("compartir", "usar algo o estar juntos con otro"), ("escuchar", "poner atención a lo que otro dice"), ("agradecer", "decir gracias por lo que alguien hizo")],
    [
        W("Descubrir el afecto", "El papá de Ema se sienta a escuchar cómo le fue en el colegio. ¿Qué forma de afecto es?", ["No le da un regalo.", "Dedica tiempo y atención.", "Eso es escuchar y compartir tiempo."], "Escuchar y compartir tiempo"),
        W("Afecto en la escuela", "Beto le presta su estuche a Luis, que olvidó el suyo. ¿En qué lugar y de qué forma hay afecto?", ["El lugar es la escuela.", "Beto ayuda con un objeto.", "La forma es dar ayuda."], "En la escuela, ayudando con un objeto"),
    ],
    [
        M("Pensar que solo es cariño si hay un abrazo o un regalo.", "Son las formas más conocidas.", "El cariño también se muestra con tiempo, escucha, palabras y ayuda."),
        M("Creer que solo mi familia puede darme afecto.", "Lo vemos más en casa.", "El afecto también ocurre en la escuela y en la comunidad."),
    ],
    R=[
        ex("Un vecino saluda con una sonrisa a Rosa cada mañana. ¿Es una muestra de afecto?", "Sí", "Un saludo amable muestra cuidado por el otro."),
        ex("Una abuela escucha con atención a su nieta. ¿Qué forma de afecto usa?", "Escuchar", "Presta atención a lo que la niña dice."),
        ex("¿Se puede mostrar cariño con palabras amables?", "Sí", "Las palabras también cuidan a las personas."),
    ],
    U=[
        ex("Nombra las cuatro formas de afecto de esta clase.", "Tiempo, escucha, palabras y ayuda", "Son las formas que vimos en la explicación."),
        ex("¿Un regalo caro muestra siempre más cariño que escuchar?", "No", "El cariño no se mide por el precio."),
        ex("¿En qué tres lugares se ve el afecto en la clase?", "Familia, escuela y comunidad", "Son los ámbitos que vimos."),
    ],
    A=[
        ex("Pedro ayudó a su compañera a levantar sus cuadernos. Escribe la forma de afecto.", "Dar ayuda", "Levantar los cuadernos es una ayuda concreta."),
        ex("Una profesora espera con paciencia a que un niño termine de hablar. ¿Qué forma de afecto es: escuchar o regalar?", "Escuchar", "Espera y pone atención."),
        ex("Elige qué muestra afecto en la familia: preparar la once, borrar la pizarra o cruzar la calle. Piensa en un hogar cualquiera.", "Preparar la once", "Es un cuidado dentro de casa."),
    ],
    Z=[
        ex("Dos niñas dicen: «Mi mamá me quiere porque me escucha» y «Mi tío me quiere porque me ayuda con las tareas». ¿Una tiene razón y la otra no?", "No, ambas muestran afecto", "Hay muchas formas de afecto y todas valen."),
        ex("Un niño dice: «En mi casa no nos abrazamos, entonces no hay cariño». ¿Qué le falta considerar?", "Que hay otras formas de cariño como escuchar y ayudar", "El cariño se expresa de muchas maneras."),
    ],
    D=[
        ex("Hoy Ema recibió 3 muestras de afecto: un saludo, una ayuda y un «gracias». ¿Cuántas formas distintas hay?", "3", "Cada una es una forma distinta."),
        ex("Si das 2 muestras de afecto en la mañana y 3 en la tarde, ¿cuántas diste?", "5", "2 más 3 es 5."),
    ],
    context=[ex("En el curso, Sofía llega con un dibujo de su abuelo que la cuida en la tarde y dice: «Él me espera y escucha mis cuentos». ¿Qué formas de afecto describió?", "Esperar y escuchar", "Su abuelo comparte tiempo y escucha.")],
    selfcheck=[ex("¿El afecto se muestra solo con abrazos?", "No", "Hay muchas formas."), ex("¿Escuchar es una forma de cuidar?", "Sí", "Presta atención a otro."), ex("¿Hay afecto en la escuela?", "Sí", "También ocurre entre compañeros y con quienes enseñan.")],
    task=T("Escribe o dibuja tres muestras de afecto: una que recibiste en tu familia o en tu hogar, una en la escuela y una que tú diste. Si prefieres, usa estas: «alguien me escuchó», «alguien me prestó algo», «yo ayudé a un compañero».", "Familia: mi mamá me preparó la once. Escuela: Luis me prestó un lápiz. Yo di: ayudé a guardar los libros.", ["tres muestras", "dice la forma de cada una", "incluye una que él o ella dio"], ["dibujo o frases"], ["listar solo regalos", "no incluir una que él mismo dio"], "Reconoce las formas de afecto y pregunta cuál le gustó más dar."),
    reinforce="Hoy da una muestra de afecto sencilla, como decir gracias o escuchar a alguien.",
    extend="Observa en tu casa o curso tres muestras de cuidado y anótalas.",
)

lesson(
    OA3, 2,
    "Una hoja y lápiz. Las escenas con distintas respuestas están escritas en los ejercicios.",
    "Aprenderé que dar y recibir afecto tiene límites y que puedo decir «no, gracias». Sirve para sentirme cómodo y respetar a los demás.",
    ["Sé que existen distintas muestras de afecto.", "Sé que mi cuerpo es mío."],
    [
        "Dar afecto también significa respetar. Antes de abrazar, besar o tocar a alguien, debes preguntar y esperar una respuesta. Eso se llama consentimiento: la persona dice que sí porque quiere. Si dice que no, o no responde, se respeta.",
        "Tú también puedes decir «no, gracias» a un abrazo, un beso o un saludo que no quieres, aunque sea de alguien conocido o querido. Puedes ofrecer otra forma: chocar la mano, saludar con la mano o decir una palabra amable. Decir que no no es ser maleducado.",
        "Un límite es lo que cada persona marca para sentirse cómoda. Los límites pueden cambiar de un día a otro. Si algo te hace sentir incómodo, nadie te debe obligar a aceptarlo. Si alguien insiste, avisa a un adulto de confianza.",
    ],
    [("consentimiento", "decir que sí porque yo quiero"), ("límite", "lo que marco para sentirme cómodo"), ("respetar", "aceptar lo que otro decide"), ("incómodo", "que no se siente bien o seguro"), ("alternativa", "otra forma de hacer lo mismo")],
    [
        W("Preguntar antes", "Pía quiere abrazar a su amiga Sara, que tiene mala cara. ¿Qué puede hacer: abrazarla de golpe o preguntar «¿Quieres un abrazo?»?", ["Abrazar de golpe no respeta la decisión de Sara.", "Preguntar le da a Sara la posibilidad de elegir.", "Si dice que no, se respeta."], "Preguntar «¿Quieres un abrazo?»"),
        W("Decir no con una alternativa", "Un tío quiere darle un beso a Tomás, pero Tomás no quiere. ¿Qué puede decir?", ["Puede decir «no, gracias».", "Puede ofrecer otra forma de saludo.", "Por ejemplo, chocar la mano."], "«No, gracias, mejor choquemos la mano»"),
    ],
    [
        M("Pensar que debo aceptar un beso o abrazo para ser educado.", "Nos enseñan a agradar a los demás.", "Puedo decir «no, gracias» y ofrecer otra forma amable."),
        M("Creer que si la otra persona no dice nada, quiere el abrazo.", "Se confunde silencio con consentimiento.", "Si no hay un sí claro, no se hace."),
    ],
    R=[
        ex("Antes de abrazar a alguien, ¿qué debes hacer?", "Preguntar", "Así la persona puede elegir."),
        ex("Si alguien dice «no, gracias» a un abrazo, ¿se respeta?", "Sí", "Es su decisión."),
        ex("¿Puedes decir «no, gracias» a un beso aunque sea de alguien conocido?", "Sí", "Tu cuerpo es tuyo."),
    ],
    U=[
        ex("En Orientación: ¿Qué es el consentimiento?", "Decir que sí porque yo quiero", "El sí debe ser libre."),
        ex("En Orientación: ¿Qué es un límite?", "Lo que marco para sentirme cómodo", "Cada persona tiene los suyos."),
        ex("¿Los límites pueden cambiar de un día a otro?", "Sí", "Hoy puedo querer un abrazo y mañana no."),
    ],
    A=[
        ex("Rosa no quiere un abrazo. Escribe una frase para decirlo con respeto.", "No, gracias, hoy no quiero un abrazo", "Dice que no sin ofender."),
        ex("Dani quiere saludar a un compañero. Elige una forma que no incomoda: chocar la mano o abrazarlo sin avisar.", "Chocar la mano", "Es un saludo suave que se puede aceptar."),
        ex("Luis dice «mejor no». Su amigo igual lo abraza. ¿Respetó?", "No", "No aceptó el no de Luis."),
    ],
    Z=[
        ex("Una niña calla cuando le preguntan si quiere un abrazo, y mira hacia otro lado. ¿Es un sí?", "No", "Sin un sí claro, se respeta el silencio como no."),
        ex("Un adulto le dice a un niño: «Dame un beso o me pongo triste». ¿Está bien insistir así?", "No", "Un adulto no debe presionar con culpa; el niño puede decir no."),
    ],
    D=[
        ex("Hay 3 formas de saludo seguras: chocar la mano, saludar con la mano y decir «hola». Si un niño descarta 1, ¿cuántas quedan?", "2", "3 menos 1 es 2."),
        ex("Si alguien insiste después de tu no y te sientes incómodo, ¿qué haces?", "Avisar a un adulto de confianza", "Insistir sobre tu no no es correcto."),
    ],
    context=[ex("En una reunión familiar, una prima se acerca para darle un beso a Ema, y Ema no quiere. Ema dice: «Prefiero chocar la mano». ¿Hizo bien?", "Sí", "Dijo su límite con una alternativa amable.")],
    selfcheck=[ex("¿Hay que preguntar antes de abrazar?", "Sí", "Para respetar la decisión."), ex("¿Puedo decir no gracias a un beso?", "Sí", "Mi cuerpo es mío."), ex("¿El silencio es un sí?", "No", "Hace falta un sí claro.")],
    task=T("Escribe o di tres frases para estas situaciones: (1) quieres abrazar a una amiga, (2) no quieres un beso de saludo, (3) un amigo dijo «no» a tu abrazo. Usa estas ideas: preguntar, decir no gracias con otra forma, y respetar.", "(1) «¿Quieres un abrazo?» (2) «No, gracias, mejor choquemos la mano.» (3) «Bueno, está bien, cuando quieras me avisas.»", ["pregunta antes de dar afecto", "dice no con respeto y una alternativa", "respeta el no del otro"], ["tres frases escritas o dichas"], ["no esperar la respuesta", "usar el silencio como sí"], "Reconoce cada frase y recuerda que siempre puede avisar a un adulto si alguien insiste."),
    reinforce="Practica con un adulto la frase «No, gracias, mejor…» y ofrece otro saludo.",
    extend="Escribe dos formas de saludo que no necesitan tocarse.",
)

lesson(
    OA3, 3,
    "Una hoja y lápiz. Las escenas de ayuda están escritas en los ejercicios.",
    "Aprenderé a ayudar de una forma que respeta lo que la otra persona puede y quiere hacer. Sirve para ayudar sin quitar el esfuerzo de nadie.",
    ["Sé que ayudar es una muestra de afecto.", "Sé que puedo decir «no, gracias»."],
    [
        "Ayudar es una muestra de cariño. Pero ayudar bien significa preguntar primero: «¿Quieres ayuda?». Algunas veces la persona prefiere intentarlo sola. Eso se llama autonomía: poder hacer algo por uno mismo. La autonomía también se cuida.",
        "Hay tres tipos de ayuda. Puedes ayudar con una pista, como «prueba por este lado». Puedes ayudar haciendo una parte, como sujetar mientras otro corta. O puedes hacerlo todo tú, pero solo si la persona lo pide o no puede hacerlo. Hacerlo todo, sin que lo pidan, a veces le quita a la persona la oportunidad de aprender.",
        "Cuando recibas ayuda, puedes decir «gracias» o «prefiero hacerlo solo». Cuando alguien rechace tu ayuda, no te enojes: respeta. Si ves que alguien está en peligro o muy mal, no esperes a que pida ayuda: avisa de inmediato a un adulto.",
    ],
    [("autonomía", "poder hacer algo por uno mismo"), ("pista", "ayuda pequeña que no resuelve todo"), ("preguntar", "pedir permiso antes de ayudar"), ("rechazar", "decir que no a algo que se ofrece"), ("emergencia", "situación de peligro que necesita un adulto")],
    [
        W("Preguntar antes", "Mateo ve que Ema trata de abrocharse la mochila. ¿Qué debe hacer primero: abrocharla él o preguntar «¿Quieres ayuda?»?", ["Si la abrocha él, quita su esfuerzo.", "Preguntar respeta que Ema decida.", "Si ella dice que sí, ayuda."], "Preguntar «¿Quieres ayuda?»"),
        W("Elegir el tipo de ayuda", "Tomás está armando un rompecabezas y pide ayuda con una pieza. ¿Qué ayuda es mejor: armarlo todo o dar una pista?", ["Armarlo todo quita el logro a Tomás.", "Una pista le deja seguir solo.", "Dar una pista cuida su autonomía."], "Dar una pista"),
    ],
    [
        M("Hacer todo por el otro para ayudarlo.", "Queremos terminar rápido.", "Pregunta y ofrece la ayuda más pequeña que sirva."),
        M("Enojarse si el otro dice «prefiero solo».", "Sentimos que no nos valoran.", "Respeta: también ayudar es dejar que el otro decida."),
    ],
    R=[
        ex("Antes de ayudar, ¿qué conviene preguntar?", "¿Quieres ayuda?", "Así el otro decide."),
        ex("Si alguien dice «prefiero hacerlo solo», ¿se respeta?", "Sí", "Es su autonomía."),
        ex("¿Dar una pista es una ayuda?", "Sí", "Ayuda sin quitar el esfuerzo."),
    ],
    U=[
        ex("¿Qué es la autonomía?", "Poder hacer algo por uno mismo", "Cada persona puede hacer cosas sola."),
        ex("¿Hacerlo todo por el otro siempre es la mejor ayuda?", "No", "A veces le quita la oportunidad de aprender."),
        ex("¿Si alguien está en peligro hay que esperar a que pida ayuda?", "No", "Hay que avisar de inmediato a un adulto."),
    ],
    A=[
        ex("Pedro tiene problemas para abrir un jugo. Escribe una frase para ofrecer ayuda.", "¿Quieres que te ayude con el jugo?", "Pregunta y ofrece."),
        ex("Rosa está resolviendo un laberinto en una hoja y pide ayuda. Elige la mejor ayuda: «mira por la izquierda» o dibujar toda la ruta.", "«Mira por la izquierda»", "Es una pista que deja trabajar a Rosa."),
        ex("Luisa le dice a su amigo: «Gracias, pero prefiero hacerlo yo». ¿Está bien decirlo?", "Sí", "Es su decisión y lo dijo con respeto."),
    ],
    Z=[
        ex("Un niño ayuda mucho a otro sin preguntar y el otro se queda callado y se va. ¿Qué pudo faltar?", "Preguntar si quería ayuda", "Sin preguntar, no se sabe si la ayuda era deseada."),
        ex("Una niña ve a un compañero caerse y llorar con un dolor fuerte. ¿Debe preguntar «quieres ayuda» y esperar?", "No, debe avisar de inmediato a un adulto", "En una emergencia no se espera."),
    ],
    D=[
        ex("Hay 3 tipos de ayuda: pista, parte y todo. Si eliges la que más cuida la autonomía, ¿cuál es?", "La pista", "Es la más pequeña."),
        ex("Si ayudas a 2 compañeros por la mañana y a 3 por la tarde, ¿a cuántos ayudaste?", "5", "2 más 3 es 5."),
    ],
    context=[ex("En la clase de arte, Pía dice «no sé cómo pegar esto». Su compañero Leo dice: «Si quieres, te muestro cómo pegar la esquina». ¿Cómo ayudó Leo?", "Preguntó y dio una pista", "Ofreció mostrar una parte y dejó que Pía siguiera.")],
    selfcheck=[ex("¿Hay que preguntar antes de ayudar?", "Sí", "Para respetar la decisión del otro."), ex("¿Una pista cuida la autonomía?", "Sí", "No resuelve todo por el otro."), ex("¿En una emergencia hay que avisar a un adulto?", "Sí", "No se espera a que pidan.")],
    task=T("Elige una de estas escenas y escribe cómo ayudarías respetando la autonomía: (1) un compañero no puede subir el cierre de su chaqueta, (2) una amiga trata de leer una palabra difícil, (3) tu hermano pequeño intenta atarse los cordones. Escribe la pregunta que harías y el tipo de ayuda.", "Escena 3: «¿Quieres que te muestre el primer nudo?» Ayuda: hago una parte y él termina.", ["pregunta antes de ayudar", "elige un tipo de ayuda que deja hacer al otro", "acepta un no"], ["frases escritas o dichas"], ["hacer todo por el otro", "no esperar la respuesta"], "Reconoce la pregunta y sugiere la ayuda más pequeña posible."),
    reinforce="Esta semana, antes de ayudar a alguien, pregunta «¿quieres ayuda?».",
    extend="Escribe un ejemplo en que no hay que esperar a que pidan ayuda y es mejor avisar de inmediato a un adulto.",
)

lesson(
    OA3, 4,
    "Una hoja y lápiz. Los esquemas de redes de cuidado están escritos en los ejercicios. Cada familia es distinta, y todas pueden formar una red.",
    "Aprenderé a reconocer a las personas que me cuidan y a quién acudir si necesito ayuda. Sirve para saber que no estoy solo.",
    ["Sé que hay muchas formas de dar y recibir cariño.", "Sé que puedo pedir ayuda a un adulto de confianza."],
    [
        "Una red de cuidado es el grupo de personas que te cuidan y a quienes puedes acudir. Puede incluir a quienes viven contigo y también a otras personas: una abuela, un tío, una vecina, una profesora, una inspectora o un entrenador. Cada familia tiene una red distinta y todas valen.",
        "Una red tiene más de una persona porque a veces alguien no está. Si una persona de tu casa no puede escucharte, puedes buscar a tu profesora. Si tu profesora no está, puedes buscar a otra persona de tu red. Tener al menos tres personas en tu red te da más seguridad.",
        "También eres parte de las redes de otros. Puedes cuidar a un compañero, saludar a un vecino y avisar si alguien está en problemas. Para pedir ayuda a alguien de tu red, usa palabras simples: «Necesito ayuda» o «Me pasó algo y quiero contarte».",
    ],
    [("red de cuidado", "personas que me cuidan y a quienes puedo acudir"), ("confianza", "sentir que alguien me cuida y me escucha"), ("vecino", "persona que vive cerca de mí"), ("comunidad", "grupo de personas que viven o trabajan cerca"), ("acudir", "ir donde alguien para pedir ayuda")],
    [
        W("Armar una red", "Ema vive con su abuela. Tiene una tía que la visita, una profesora que la escucha y una vecina que le presta ayuda. ¿Cuántas personas hay en su red, sin contar a su abuela?", ["Tía: 1.", "Profesora: 2.", "Vecina: 3."], "3 personas más su abuela"),
        W("Elegir a quién acudir", "Pablo tiene un problema en el colegio y su mamá está trabajando. ¿A quién puede acudir de su red?", ["Debe buscar a una persona de confianza en el colegio.", "Puede ser su profesora o la inspectora.", "No tiene por qué quedarse solo."], "A su profesora o a otro adulto de confianza del colegio"),
    ],
    [
        M("Creer que solo mi familia más cercana puede cuidarme.", "Pensamos que la red es solo la casa.", "La red puede incluir a la escuela y a la comunidad."),
        M("Pensar que pedir ayuda a varias personas molesta.", "Sentimos vergüenza.", "Tener varias personas en la red es parte de estar protegido."),
    ],
    R=[
        ex("¿Una profesora puede ser parte de la red de cuidado?", "Sí", "Es un adulto que cuida en la escuela."),
        ex("¿Una red de cuidado es igual en todas las familias?", "No", "Cada familia y cada niño tienen una red distinta."),
        ex("¿Una vecina de confianza puede ser parte de la red?", "Sí", "Vive cerca y puede ayudar."),
    ],
    U=[
        ex("¿Por qué conviene que la red tenga varias personas?", "Porque a veces alguien no está", "Si uno falta, otro puede ayudar."),
        ex("¿Cuántas personas conviene tener al menos en la red?", "Tres", "Así hay opciones si una no está."),
        ex("¿Tú también eres parte de la red de otros?", "Sí", "Puedes cuidar a un compañero o a un vecino."),
    ],
    A=[
        ex("Rosa nombra a su mamá, su tío y su profesora. ¿Cuántas personas tiene en su red?", "3", "Son tres personas."),
        ex("Escribe una frase simple para pedir ayuda a alguien de tu red.", "Necesito ayuda, ¿puedes escucharme?", "Es clara y corta."),
        ex("Un compañero está llorando solo. Elige una acción de red: avisar a la profesora o hacer como que no ves.", "Avisar a la profesora", "Cuidar al otro es parte de la red."),
    ],
    Z=[
        ex("Un niño dice: «Mi red es solo mi papá». ¿Qué otras personas podría sumar?", "Una profesora, un vecino o un familiar de confianza", "Más personas le dan más seguridad."),
        ex("Una niña vive con sus tíos y otra vive con su mamá. ¿Cuál tiene una red mejor?", "Ninguna es mejor, ambas pueden tener buenas redes", "No se compara a las familias; lo que importa es que haya personas de confianza."),
    ],
    D=[
        ex("Pía tiene a 2 personas en la escuela y 2 en su casa. ¿Cuántas hay en total?", "4", "2 más 2 es 4."),
        ex("Si alguien le dice a un niño: «No le cuentes a nadie», pero lo hizo sentir mal, ¿qué debe hacer?", "Contárselo a un adulto de su red", "Los secretos que hacen sentir mal se cuentan."),
    ],
    context=[ex("Camila tiene un problema que le da vergüenza. Su abuela está dormida. Camila piensa en su tía o en su profesora. ¿Qué es lo mejor?", "Buscar a su tía o a su profesora", "Acude a otra persona de su red.")],
    selfcheck=[ex("¿Una red tiene más de una persona?", "Sí", "Conviene tener varias."), ex("¿Todas las familias tienen la misma red?", "No", "Cada red es distinta."), ex("¿Puedes pedir ayuda con palabras simples?", "Sí", "Con «necesito ayuda» basta.")],
    task=T("Dibuja una red de cuidado con cuatro círculos, cada uno con el nombre o el dibujo de una persona de confianza: dos en tu casa o con quien vives y dos fuera (colegio, vecindario, familia). Si no quieres poner nombres, usa roles: «mi profesora», «mi vecina».", "Círculos: mi mamá, mi tío, mi profesora, mi vecina.", ["cuatro personas", "incluye personas de casa y de fuera", "puede usar roles si prefiere"], ["dibujo de la red"], ["incluir solo una persona", "comparar su red con la de otros"], "Reconoce la red y sugiere sumar una persona más si tiene menos de tres."),
    reinforce="Aprende de memoria el nombre de dos adultos de tu red.",
    extend="Escribe cómo puedes ser parte de la red de otra persona esta semana.",
)

# ================================================================ OA 04
lesson(
    OA4, 1,
    "Una hoja y lápiz. Las rutinas y horarios están escritos en los ejercicios. Cada familia tiene horarios distintos.",
    "Aprenderé qué rutinas de higiene, descanso y movimiento cuidan mi cuerpo. Sirve para sentirme bien y evitar enfermarme.",
    ["Sé lavarme las manos y los dientes.", "Sé que dormir me ayuda a estar bien."],
    [
        "El autocuidado son las cosas que haces para cuidarte. La higiene es una parte: lavarte las manos con agua y jabón durante unos 20 segundos, antes de comer y después de ir al baño. También lavarte los dientes dos veces al día, unos dos minutos.",
        "El descanso es otra parte. A tu edad el cuerpo necesita dormir entre 9 y 11 horas cada noche. Dormir bien ayuda a aprender, a tener buen ánimo y a crecer. También necesitas momentos de recreación, como jugar, dibujar o leer, para que tu mente descanse.",
        "El cuerpo también necesita moverse. Jugar, correr, bailar o caminar son actividad física. Se recomienda mover el cuerpo cerca de una hora al día, repartida en juegos. No todos los cuerpos hacen lo mismo y eso está bien: cada uno se mueve como puede.",
    ],
    [("higiene", "limpieza que cuida mi cuerpo"), ("rutina", "cosas que hago más o menos igual cada día"), ("descanso", "tiempo para dormir o relajarme"), ("recreación", "actividades para jugar y disfrutar"), ("autocuidado", "lo que hago para cuidarme")],
    [
        W("Lavado de manos", "Mateo se lava las manos solo 5 segundos. Se recomienda unos 20. ¿Cuántos segundos más debe lavarse?", ["Meta: 20 segundos.", "Hoy hace 5.", "20 menos 5 es 15."], "15 segundos más"),
        W("Sueño", "Ema duerme 8 horas. Se recomienda entre 9 y 11. ¿Duerme lo suficiente?", ["Mínimo recomendado: 9 horas.", "Ella duerme 8.", "8 es menos que 9."], "No, le falta al menos 1 hora"),
    ],
    [
        M("Pensar que lavarse las manos rápido con agua sola es suficiente.", "Se cree que el jabón no hace falta.", "Usa agua y jabón unos 20 segundos."),
        M("Pensar que dormir poco no importa si tengo energía.", "Nos sentimos bien un rato.", "El cuerpo necesita dormir bien para aprender y crecer."),
    ],
    R=[
        ex("¿Con qué te lavas las manos para que queden limpias?", "Agua y jabón", "El jabón saca la suciedad."),
        ex("¿Cuántas veces al día se recomienda lavarse los dientes?", "Dos", "Una vez al despertar y otra antes de dormir."),
        ex("Jugar a las escondidas, ¿es actividad física?", "Sí", "Mueve el cuerpo."),
    ],
    U=[
        ex("¿Cuántas horas necesita dormir un niño de tu edad?", "Entre 9 y 11 horas", "Así su cuerpo descansa y aprende mejor."),
        ex("¿Para qué sirve la recreación?", "Para jugar, descansar la mente y disfrutar", "Equilibra el trabajo escolar."),
        ex("¿Todos los cuerpos se mueven igual?", "No", "Cada persona se mueve como puede."),
    ],
    A=[
        ex("Pedro duerme de las 9 de la noche a las 7 de la mañana. ¿Cuántas horas duerme?", "10", "De las 9 a las 7 son 10 horas."),
        ex("Rosa se lava los dientes 2 minutos por la mañana y 2 por la noche. ¿Cuántos minutos son al día?", "4", "2 más 2 es 4."),
        ex("Elige la mejor rutina antes de comer: lavarse las manos con jabón o sacudirse las manos.", "Lavarse las manos con jabón", "El jabón quita los gérmenes."),
    ],
    Z=[
        ex("Dos niños: uno juega 1 hora al aire libre y otro mira pantalla 3 horas seguidas. ¿Quién cuida mejor su cuerpo con movimiento?", "El que juega al aire libre", "Se mueve más."),
        ex("Una niña usa silla de ruedas y no puede correr. ¿Puede hacer actividad física?", "Sí, con juegos que pueda hacer", "Cada cuerpo tiene sus formas de moverse."),
    ],
    D=[
        ex("Si una niña juega 20 minutos antes del colegio, 20 en el recreo y 20 en la tarde, ¿cuántos minutos juega?", "60", "20 más 20 más 20 es 60 minutos."),
        ex("Si un niño se lava las manos 4 veces al día, ¿cuántas veces lo hace en 3 días?", "12", "4 más 4 más 4 es 12."),
    ],
    context=[ex("Tomás quiere jugar un rato más y no se lava los dientes antes de dormir. Su mamá le pide que lo haga. ¿Qué rutina cuida su cuerpo?", "Lavarse los dientes antes de dormir", "Mantiene los dientes limpios.")],
    selfcheck=[ex("¿Hay que lavarse las manos con jabón?", "Sí", "Quita la suciedad."), ex("¿Es bueno dormir entre 9 y 11 horas?", "Sí", "El cuerpo lo necesita."), ex("¿Jugar mueve el cuerpo?", "Sí", "Es actividad física.")],
    task=T("Completa esta rutina del día con una acción de higiene, una de descanso y una de movimiento. Puedes elegir: lavarme las manos con jabón, lavarme los dientes, dormir 9 horas o más, jugar al aire libre, bailar, caminar. Si algo no se puede en tu hogar, cámbialo por otra opción parecida.", "Mañana: lavarme los dientes. Tarde: jugar 30 minutos. Noche: acostarme temprano para dormir 9 horas.", ["una acción de higiene", "una de descanso", "una de movimiento"], ["rutina escrita o dibujada"], ["no incluir los tres tipos", "horarios imposibles"], "Reconoce lo que cumple y propone ajustar un horario si hace falta."),
    reinforce="Hoy lávate las manos con jabón contando hasta 20.",
    extend="Calcula cuántas horas duermes y compáralas con 9 a 11.",
)

lesson(
    OA4, 2,
    "Una hoja y lápiz. Las comidas y los menús están escritos en los ejercicios. Cada familia come distinto, según su cultura, presupuesto y salud.",
    "Aprenderé a escuchar mi hambre y a elegir alimentos variados sin sentir culpa. Sirve para cuidar mi cuerpo con tranquilidad.",
    ["Sé que comer me da energía.", "Sé que beber agua es importante."],
    [
        "Comer te da energía para jugar y aprender. El cuerpo necesita alimentos variados: frutas, verduras, cereales como pan y arroz, legumbres como lentejas, huevos o carnes, y lácteos. También necesita agua. Comer de todo un poco ayuda a crecer sanos.",
        "No hay comidas «buenas» ni «malas» para sentirte culpable. Hay alimentos que conviene comer todos los días y otros de vez en cuando, como los dulces. Comer un dulce en una fiesta no es malo. Pensar que «soy malo por comer algo» no ayuda.",
        "Tu cuerpo te avisa cuando tiene hambre y cuando ya está satisfecho. Come despacio y escúchalo. Cada familia come según su cultura y sus posibilidades, y todas son válidas. Si tienes una alergia, avisa a un adulto y no comas lo que te hace mal. No nos burlamos ni comparamos lo que traen los demás.",
    ],
    [("alimentación", "lo que comemos y bebemos para vivir"), ("variado", "de muchos tipos distintos"), ("hambre", "señal del cuerpo que pide comida"), ("satisfecho", "que ya comió lo suficiente"), ("alergia", "reacción del cuerpo a un alimento que le hace mal")],
    [
        W("Plato variado", "En el almuerzo hay arroz, lentejas, ensalada de tomate y agua. ¿Hay alimentos variados?", ["Arroz es cereal.", "Lentejas son legumbre y el tomate es verdura.", "Hay agua para beber. Sí hay variedad."], "Sí, el almuerzo es variado"),
        W("Escuchar el cuerpo", "Pía come despacio y siente que ya está satisfecha, aunque queda un poco en el plato. ¿Qué puede hacer?", ["Su cuerpo avisa que ya comió suficiente.", "No tiene que sentirse culpable.", "Puede dejar el resto o guardarlo."], "Dejar de comer y no sentir culpa"),
    ],
    [
        M("Pensar que un alimento es «malo» y que soy malo por comerlo.", "Se mezcla comida con culpa.", "Hay alimentos de todos los días y otros de vez en cuando, sin culpa."),
        M("Comparar mi colación con la de otro niño para burlarme.", "Cada familia come distinto.", "Respeta lo que cada uno trae."),
    ],
    R=[
        ex("¿Las frutas y verduras son parte de una alimentación variada?", "Sí", "Dan vitaminas y fibra."),
        ex("¿Qué debes beber más: agua o jugo con mucha azúcar?", "Agua", "El agua es lo que el cuerpo necesita todos los días."),
        ex("Si tienes una alergia a un alimento, ¿lo comes?", "No", "Te puede hacer mal."),
    ],
    U=[
        ex("¿Qué señal te avisa que necesitas comer?", "El hambre", "Es la señal del cuerpo."),
        ex("¿Hay alimentos que provocan culpa por comerlos?", "No", "No se debe sentir culpa por comer."),
        ex("¿Todas las familias comen lo mismo?", "No", "Cada una come según su cultura y posibilidades."),
    ],
    A=[
        ex("Menú: pan, tomate, huevo y agua. ¿Qué alimento es un cereal?", "El pan", "El pan viene de los cereales."),
        ex("En una fiesta, Dani come una torta. ¿Hizo algo malo?", "No", "Comer dulces de vez en cuando está bien."),
        ex("Elige la mejor bebida para acompañar el almuerzo todos los días: agua o bebida azucarada.", "Agua", "Hidrata sin exceso de azúcar."),
    ],
    Z=[
        ex("Un niño dice: «Mi colación es mejor que la tuya». ¿Qué falta respetar?", "Que cada familia come distinto", "Comparar con burla no ayuda."),
        ex("Una niña siente que ya no tiene hambre y su plato aún tiene comida. Alguien le dice «termina todo». ¿Qué le avisa su cuerpo?", "Que está satisfecha", "Su cuerpo le indica que ya comió suficiente."),
    ],
    D=[
        ex("Si un niño bebe 1 vaso de agua en la mañana, 2 en la tarde y 1 en la noche, ¿cuántos vasos son?", "4", "1 más 2 más 1 es 4."),
        ex("Un plato tiene arroz, lentejas, zanahoria y agua. Sin contar el agua, ¿cuántos tipos distintos de alimento hay?", "3", "Arroz es cereal, lentejas son legumbre y zanahoria es verdura: son 3 tipos."),
    ],
    context=[ex("En la hora de colación, Rosa trae pan con palta y una manzana. Luis trae galletas. Luis le dice a Rosa que su colación es aburrida. ¿Qué podría decir Rosa?", "Cada uno trae lo que su familia puede y quiere", "Respeta la diversidad de las familias sin pelear.")],
    selfcheck=[ex("¿Hay que comer alimentos variados?", "Sí", "El cuerpo necesita de todo un poco."), ex("¿Se debe sentir culpa por comer un dulce en una fiesta?", "No", "Es parte de comer de forma variada."), ex("¿Mi cuerpo me avisa cuando tengo hambre?", "Sí", "Escucharlo es parte de cuidarse.")],
    task=T("Arma un menú de un día con alimentos que tengas en casa o que conozcas: desayuno, almuerzo y once, e incluye agua. Marca un alimento de cada tipo: fruta o verdura, cereal, legumbre o proteína. Si algo no lo comes en tu casa, cámbialo por otro parecido.", "Desayuno: pan con huevo y leche. Almuerzo: arroz con lentejas y ensalada. Once: pan con palta y una manzana. Agua todo el día.", ["menú de tres comidas", "alimentos variados", "incluye agua"], ["menú escrito o dibujado"], ["usar etiquetas como «comida mala»", "olvidar el agua"], "Reconoce la variedad y no juzga lo que cada familia come."),
    reinforce="Hoy come despacio y nota cuándo ya estás satisfecho.",
    extend="Haz una lista de cinco alimentos que se comen en tu casa y di de qué tipo son.",
)

lesson(
    OA4, 3,
    "Una hoja y lápiz. Las escenas están escritas en los ejercicios. Esta clase se puede hacer con un adulto cerca.",
    "Aprenderé que mi cuerpo es mío y que tengo derecho a decir no a lo que me incomoda. Sirve para protegerme y saber a quién contar.",
    ["Sé el nombre de las partes del cuerpo.", "Sé que puedo decir «no, gracias» a un abrazo."],
    [
        "Tu cuerpo es tuyo. Las partes que cubre la ropa interior o el traje de baño son tus partes íntimas, y son privadas. Nadie debe tocarlas ni pedirte que las muestres. Tampoco debes tocar las de otros ni mostrar o mirar imágenes de eso. Las únicas excepciones son los cuidados de salud o de higiene, cuando un adulto de tu familia está cerca y te explica lo que pasa. Aun así, puedes decir si algo te incomoda.",
        "Tienes derecho a decir «no» y a alejarte de lo que te incomoda, aunque la persona sea conocida o mayor. Tu cuerpo te da señales: nervios, ganas de huir, una sensación rara en el estómago. Esas señales son importantes. Hazles caso y busca a un adulto de confianza.",
        "Los secretos que te dan miedo o que te hacen sentir mal no se guardan. Ningún adulto debe pedirte que escondas algo sobre tu cuerpo. Si alguien lo hace, cuéntalo a otro adulto de confianza. Si el primero no te cree, sigue contando hasta que alguien te escuche. Una sorpresa, como un regalo de cumpleaños, es distinta: es alegre y pronto se cuenta. Nada de esto es tu culpa.",
    ],
    [("íntimo", "privado, que solo es mío"), ("límite", "lo que marco para sentirme seguro"), ("señal", "algo que me avisa que algo no está bien"), ("secreto", "algo que no se cuenta"), ("culpa", "sentir que hice algo mal, aunque no sea así")],
    [
        W("Decir no", "Un compañero le pide a Tomás que le muestre una parte íntima de su cuerpo. ¿Qué debe hacer Tomás?", ["Tomás puede decir «no».", "Debe alejarse.", "Debe contárselo a un adulto de confianza."], "Decir no, alejarse y contarle a un adulto"),
        W("Hacer caso a las señales", "Ema siente nervios y ganas de irse cuando alguien la mira con insistencia. ¿Qué debe hacer?", ["Son señales de su cuerpo.", "Debe hacerles caso.", "Debe ir donde hay otras personas y avisar a un adulto."], "Alejarse y avisar a un adulto de confianza"),
    ],
    [
        M("Pensar que debo obedecer a un adulto aunque me incomode.", "Nos enseñan a ser educados.", "Puedo decir no y avisar a otro adulto de confianza."),
        M("Creer que si me pasó algo es mi culpa.", "A veces sentimos vergüenza.", "Nunca es tu culpa; contarlo es lo correcto."),
    ],
    R=[
        ex("¿Tu cuerpo es tuyo?", "Sí", "Nadie puede decidir por ti sobre tu cuerpo."),
        ex("Si algo te incomoda, ¿puedes decir no?", "Sí", "Es tu derecho."),
        ex("Si alguien te pide guardar un secreto que te da miedo, ¿lo guardas?", "No", "Se lo cuentas a un adulto de confianza."),
    ],
    U=[
        ex("¿Qué partes del cuerpo son íntimas?", "Las que cubre la ropa interior o el traje de baño", "Son partes privadas de tu cuerpo."),
        ex("¿Es tu culpa si alguien te incomoda o te toca sin permiso?", "No", "La responsabilidad es de quien lo hace."),
        ex("Si el primer adulto no te cree, ¿qué haces?", "Sigo contando hasta que alguien me escuche", "Siempre hay otro adulto que te puede ayudar."),
    ],
    A=[
        ex("Un adulto dice: «Es nuestro secreto, no le cuentes a nadie sobre tu cuerpo». ¿Qué haces?", "Se lo cuento a otro adulto de confianza", "Un adulto no debe pedir ese secreto."),
        ex("Escribe una frase para decir no a algo que te incomoda.", "No quiero, déjame", "Es clara y firme."),
        ex("Elige qué hacer si sientes nervios y ganas de huir: ignorarlo o buscar un adulto de confianza.", "Buscar un adulto de confianza", "Las señales del cuerpo importan."),
    ],
    Z=[
        ex("Alguien te hace sentir incómodo con tu cuerpo y te dice: «No le cuentes a nadie». ¿Debes guardar ese secreto?", "No, hay que contarlo a un adulto de confianza", "Un secreto que incomoda o preocupa se cuenta; no es tu culpa."),
        ex("Una niña dice: «No quiero contar porque me da vergüenza». ¿Qué puede ayudarla?", "Recordar que no es su culpa y buscar a un adulto de confianza", "Contar a tiempo protege a quien lo vive."),
    ],
    D=[
        ex("Si alguien tiene tres adultos de confianza y el primero no le cree, ¿a cuántos más puede acudir?", "2", "Quedan dos adultos más."),
        ex("En el baño de la escuela, otro niño te pide que le muestres tu cuerpo. ¿Qué haces?", "Decir no, salir y avisar a un adulto", "Es una situación que debe saber un adulto."),
    ],
    context=[ex("Un adulto desconocido le dice a Pía en la plaza: «Ven, te muestro algo secreto». Pía se siente incómoda. ¿Qué es lo mejor?", "Decir no, alejarse y avisar a un adulto", "Ir con un desconocido a un lugar a solas no es seguro.")],
    selfcheck=[ex("¿Puedes decir no a lo que te incomoda?", "Sí", "Tu cuerpo es tuyo."), ex("¿Un secreto que te da miedo se cuenta?", "Sí", "Se lo cuentas a un adulto de confianza."), ex("¿Es tu culpa?", "No", "Nunca es tu culpa.")],
    task=T("Escribe o di tres cosas: (1) una frase para decir no, (2) a quién le contarías si algo te incomoda (un rol, como «mi profesora»), (3) qué señal de tu cuerpo te avisa que algo no está bien. Puedes usar esta frase: «Mi cuerpo es mío».", "(1) «No quiero, déjame.» (2) Mi tía. (3) Me da un nudo en el estómago.", ["una frase firme", "nombra un adulto de confianza", "reconoce una señal del cuerpo"], ["frases escritas o dichas"], ["pensar que debe guardar un secreto", "culparse"], "Reconoce cada respuesta y recuerda que si algo pasó, contar nunca es un error."),
    reinforce="Repite en voz alta: «Mi cuerpo es mío y puedo decir no».",
    extend="Escribe los nombres de dos adultos de confianza a quienes puedes contarles.",
)

lesson(
    OA4, 4,
    "Una hoja y lápiz. Las listas de datos y las situaciones están escritas en los ejercicios. No escribas tus datos reales; usa datos inventados.",
    "Aprenderé qué datos personales debo cuidar y cuándo avisar a un adulto antes de compartirlos. Sirve para estar seguro en la calle y en internet.",
    ["Sé mi nombre y mi curso.", "Sé que hay personas que no conozco."],
    [
        "La información personal son los datos que dicen quién eres y dónde estás. Por ejemplo: tu nombre completo, tu dirección, tu teléfono, tu colegio, tus fotos y tus claves. Es información privada. Antes de compartirla debes preguntar a un adulto de confianza.",
        "Con personas desconocidas, y también en internet, no entregues esos datos. Una persona que no conoces no necesita saber dónde vives ni a qué colegio vas. Tampoco debes decir las claves de tus cuentas ni mandar fotos tuyas sin permiso de un adulto de tu familia.",
        "A veces alguien te pide un dato con un buen motivo, como la profesora para la lista del curso. Esas peticiones están bien porque conoces a la persona y su motivo. Si no estás seguro, di «le voy a preguntar a mi mamá» o «a mi adulto de confianza» y espera la respuesta.",
    ],
    [("información personal", "datos que dicen quién soy y dónde estoy"), ("dirección", "lugar donde vivo"), ("clave", "palabra secreta para entrar a una cuenta"), ("desconocido", "persona que no conozco"), ("privado", "que no se comparte con cualquiera")],
    [
        W("Dato personal o no", "¿Tu color favorito es información personal que debes cuidar mucho, como tu dirección?", ["El color favorito no dice dónde estás.", "La dirección sí dice dónde vives.", "La dirección es la que debes cuidar."], "No, la dirección es la que debes cuidar"),
        W("Qué hacer si piden un dato", "Un desconocido en un juego en línea le pide a Ema su colegio. ¿Qué debe hacer?", ["No debe dar datos a desconocidos.", "Debe decir que no.", "Debe contar a un adulto de confianza."], "No dar el dato y contárselo a un adulto"),
    ],
    [
        M("Dar mi dirección a alguien que se ve amable.", "Pensamos que ser amable significa ser seguro.", "Los datos solo se dan con permiso de un adulto de confianza."),
        M("Contar mi clave a un amigo para probar su confianza.", "Creemos que es un juego.", "Las claves son privadas; solo las sabe un adulto de la familia."),
    ],
    R=[
        ex("¿Tu dirección es información personal?", "Sí", "Dice dónde vives."),
        ex("¿Debes dar tu clave a un amigo?", "No", "Las claves son privadas."),
        ex("¿Debes dar tus datos a un desconocido?", "No", "No sabes si es seguro."),
    ],
    U=[
        ex("¿Qué es información personal?", "Datos que dicen quién soy y dónde estoy", "Por ejemplo nombre completo, dirección o colegio."),
        ex("¿Qué haces si no estás seguro si compartir un dato?", "Preguntar a un adulto de confianza", "Ellos pueden ayudar a decidir."),
        ex("¿Puedes mandar fotos tuyas a alguien que no conoces?", "No", "Primero se pide permiso a un adulto."),
    ],
    A=[
        ex("Lista: color favorito, nombre del colegio, comida preferida, dirección. ¿Cuáles son datos personales que cuidar?", "Nombre del colegio y dirección", "Dicen dónde estás."),
        ex("Un desconocido pregunta por tu teléfono. Escribe tu respuesta.", "No, voy a preguntarle a un adulto", "Es una respuesta firme y segura."),
        ex("Tu profesora pide tu nombre para la lista del curso. ¿Puedes darlo?", "Sí", "Conoces a la persona y el motivo es claro."),
    ],
    Z=[
        ex("Alguien en un juego dice: «Dime tu dirección y te regalo algo». ¿Qué hay que pensar?", "Que puede ser peligroso y no hay que darla", "Pedir datos a cambio de regalos es una señal de alerta."),
        ex("Una amiga dice: «Dame tu clave, te prometo no mirarla». ¿Se la das?", "No", "Las claves no se comparten."),
    ],
    D=[
        ex("Beto tiene 5 datos personales. Ya aprendió a cuidar 3. ¿Cuántos le faltan por aprender a cuidar?", "2", "5 menos 3 es 2."),
        ex("Si alguien te insiste mucho por un dato, ¿qué haces?", "Me alejo y le aviso a un adulto de confianza", "La insistencia es una señal de alerta."),
    ],
    context=[ex("Luis juega un juego en una tablet y aparece un mensaje: «¿Cómo te llamas y dónde vives?». No sabe quién escribe. ¿Qué hace?", "No responde y avisa a un adulto", "No se dan datos a desconocidos.")],
    selfcheck=[ex("¿La dirección es privada?", "Sí", "Dice dónde vives."), ex("¿Se comparten las claves?", "No", "Las claves son privadas."), ex("¿Se pregunta a un adulto antes de compartir un dato?", "Sí", "Es una forma de cuidarse.")],
    task=T("Mira estos datos inventados de un niño llamado Beto: nombre completo, color favorito, dirección, colegio, comida favorita, clave de su cuenta. Marca con una X los que Beto debe cuidar y escribe una frase que diría si un desconocido le pide uno.", "Cuidar: nombre completo, dirección, colegio y clave. Frase: «No te voy a dar eso, voy a preguntar a mi adulto».", ["marca los datos que dicen quién es y dónde está", "escribe una frase de respuesta", "no usa datos reales propios"], ["lista marcada", "frase escrita o dicha"], ["marcar solo uno", "usar datos reales"], "Reconoce los datos cuidados y sugiere avisar a un adulto."),
    reinforce="Repite: «Mis datos son privados y le pregunto a un adulto».",
    extend="Inventa una regla de tres pasos para cuando alguien te pida un dato por internet.",
)

lesson(
    OA4, 5,
    "Una hoja y lápiz. Las situaciones están escritas en los ejercicios. Se puede hacer con un adulto cerca.",
    "Aprenderé a armar un plan simple para protegerme: decir no, ir a un lugar seguro y contar. Sirve para actuar con calma si algo me incomoda.",
    ["Sé que mi cuerpo es mío.", "Sé que debo cuidar mi información personal."],
    [
        "Un plan de protección son pasos simples que haces cuando algo te incomoda o te da miedo, con una persona conocida o desconocida. Tiene tres pasos. Primero, decir «no» con voz firme o alejarte. Segundo, ir a un lugar seguro, donde haya gente de confianza. Tercero, contárselo a un adulto de confianza.",
        "Tu plan incluye a las personas a quienes puedes acudir. Piensa en tres: una en tu casa, una en la escuela y una más. También puedes saber números de ayuda. En Chile, 133 es Carabineros y 147 es Fono Niños. Pide a un adulto que te explique cuándo usarlos.",
        "Ningún adulto debe pedirte que guardes secretos sobre tu cuerpo. Si cuentas y no te creen, cuéntalo a otro adulto hasta que te ayuden. Practicar el plan con un adulto, como un juego, ayuda a recordarlo. Recuerda siempre que no es tu culpa.",
    ],
    [("plan", "pasos para saber qué hacer"), ("protección", "cuidar que no me pase algo malo"), ("lugar seguro", "sitio con gente de confianza"), ("firme", "que se dice con seguridad"), ("ayuda", "apoyo de un adulto")],
    [
        W("Los tres pasos", "Una persona desconocida insiste en que Tomás suba a un auto. ¿Qué pasos sigue?", ["Paso 1: decir «no» y alejarse.", "Paso 2: ir a un lugar con gente, como una tienda.", "Paso 3: contar a un adulto de confianza."], "Decir no y alejarse, ir a un lugar seguro y contar"),
        W("Elegir el lugar seguro", "Pía está en la plaza y se siente incómoda. ¿Dónde es más seguro ir: a un rincón solo o donde hay familias y un comerciante conocido?", ["Un rincón solo no tiene ayuda.", "Donde hay gente puede recibir ayuda.", "Elige el lugar con gente."], "Donde hay familias y un comerciante conocido"),
    ],
    [
        M("Quedarme callado por miedo a que me reten.", "Pensamos que contar traerá problemas.", "Contar es lo correcto y no es tu culpa."),
        M("Contar solo a un adulto y quedarme si no me cree.", "Nos rendimos pronto.", "Sigo contando a otro adulto hasta que me ayuden."),
    ],
    R=[
        ex("¿Cuál es el primer paso del plan de protección?", "Decir no o alejarme", "Es lo que me protege primero."),
        ex("¿Debes guardar un secreto que te asusta?", "No", "Se cuenta a un adulto de confianza."),
        ex("¿Puedes contar si algo te incomoda?", "Sí", "Contar te ayuda a protegerte."),
    ],
    U=[
        ex("¿Cuáles son los tres pasos del plan?", "Decir no y alejarme, ir a un lugar seguro y contar", "Son los pasos que vimos."),
        ex("¿Qué es un lugar seguro?", "Un sitio con gente de confianza", "Ahí puedo recibir ayuda."),
        ex("¿Por qué conviene tener más de un adulto de confianza?", "Porque uno puede no estar o no creerme", "Más personas dan más protección."),
    ],
    A=[
        ex("Un desconocido se acerca a Ema en la calle y le pide que lo acompañe. ¿Qué hace primero?", "Decir no y alejarse", "Es el primer paso del plan."),
        ex("Rosa necesita ayuda en la calle. Elige a quién acudir: un carabinero o una persona que no se ve confiable.", "Un carabinero", "Es una persona que ayuda."),
        ex("Si estás en peligro y puedes llamar a Carabineros, ¿qué número marcas?", "133", "Es el número de Carabineros."),
    ],
    Z=[
        ex("Un niño dice: «Si cuento, me van a retar». ¿Qué le dirías?", "Que contar protege y no es su culpa", "Los adultos de confianza cuidan, no castigan por pedir ayuda."),
        ex("Una niña le contó a su vecina y no le creyó. ¿Qué hace?", "Cuenta a otro adulto de confianza", "Debe seguir hasta ser escuchada."),
    ],
    D=[
        ex("Mi plan tiene 3 pasos y hago 2. ¿Cuántos faltan?", "1", "3 menos 2 es 1."),
        ex("Si tienes que ayudar a un compañero que se siente incómodo, ¿qué haces?", "Lo acompaño y aviso a un adulto", "Los pasos de protección sirven para los demás."),
    ],
    context=[ex("Mateo sale de la escuela y un adulto que no conoce le dice que su mamá lo mandó a buscar. Su mamá no le avisó nada. ¿Qué hace Mateo?", "Decir no, volver donde hay adultos del colegio y contar", "Sigue el plan de tres pasos.")],
    selfcheck=[ex("¿El plan tiene tres pasos?", "Sí", "Decir no, ir a un lugar seguro y contar."), ex("¿Se cuenta aunque dé vergüenza?", "Sí", "Contar te ayuda a protegerte."), ex("¿Es tu culpa?", "No", "Nunca es tu culpa.")],
    task=T("Arma tu plan de protección con tres cosas: (1) la frase firme que dirías, (2) un lugar seguro cercano (por ejemplo, la sala de profesores, una tienda conocida o la casa de un familiar), (3) los nombres o roles de dos adultos de confianza. Puedes usar los números 133 y 147 si un adulto te los explica.", "(1) «No, déjame.» (2) La oficina del colegio. (3) Mi mamá y mi profesora.", ["frase firme", "lugar seguro con gente", "dos adultos de confianza"], ["plan escrito o dibujado"], ["no incluir adultos", "lugar sin gente"], "Reconoce el plan y sugiere practicarlo con un adulto de su confianza."),
    reinforce="Cuéntale tu plan a un adulto de tu casa.",
    extend="Practica con un adulto: él te pide algo y tú dices tu frase y sigues los pasos.",
)
