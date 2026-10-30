"""Student material for 1.º básico Música, OA 05 (exploración e improvisación), OA 06 (presentación) y OA 07 (vida cotidiana)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_content_mu_a import LEY, SIL, TA, TT, P, sounds
from student_lessons import ex, register

OA5, OA6, OA7 = "MU01 OA 05", "MU01 OA 06", "MU01 OA 07"

# ---------------------------------------------------------------- OA 05
register(
    OA5, 1,
    materials="Un tarro con tapa, una cuchara de madera y tus manos. Si quieres, también una botella con un poco de arroz. Todos los objetos deben ser seguros: nada que corte, nada de vidrio.",
    use="Aprenderé a explorar una fuente sonora y encontrar tres formas controladas de hacerla sonar. Sirve para descubrir ideas musicales antes de inventar una.",
    prior=["Sé golpear con suavidad.", "Sé quedarme en silencio para escuchar."],
    explain=[
        "Explorar es probar con curiosidad cómo suena una fuente sonora. Una fuente sonora es cualquier cosa que produce sonido: tu voz, un tarro, una cuchara, tus manos. Un mismo tarro puede sonar de muchas maneras si lo golpeas, lo raspas o lo tapas.",
        "Para explorar de manera controlada, cambia una cosa a la vez. Puedes cambiar dónde golpeas: en el borde suena fino, en el centro suena más hondo. Puedes cambiar con qué golpeas: con la yema del dedo suena suave y con la cuchara más fuerte. Puedes cambiar cuánto dura: dejar sonar o apagar con la mano.",
        "Después de probar, escoge tres posibilidades y descríbelas con las cualidades: agudo o grave, fuerte o suave, largo o corto. Escucha entre una prueba y otra, y quédate en silencio un momento. Explorar no es hacer ruido sin escuchar.",
    ],
    vocab=[("explorar", "probar con curiosidad cómo suena algo"), ("fuente sonora", "lo que produce sonido"), ("controlado", "hecho con cuidado y pensando lo que hago"), ("posibilidad", "una de las formas en que algo puede sonar"), ("apagar", "detener el sonido con la mano")],
    worked=[
        {"title": "Tres posibilidades con un tarro", "problem": "Con un tarro con tapa, encuentra tres formas de hacerlo sonar y descríbelas.", "steps": ["Golpeo la tapa con la cuchara: suena fuerte y corto.", "Golpeo el costado con la yema del dedo: suena suave y grave.", "Raspo la tapa con la uña: suena fino y largo."], "answer": "Golpe en la tapa (fuerte y corto), golpe en el costado (suave y grave), raspado (fino y largo)"},
        {"title": "Cambiar una sola cosa", "problem": "Quieres saber si el borde suena distinto del centro. ¿Qué cosa cambias y qué dejas igual?", "steps": ["Dejo igual la cuchara y la fuerza.", "Cambio solo el lugar donde golpeo.", "Escucho la diferencia."], "answer": "Cambio el lugar y dejo igual la cuchara y la fuerza"},
    ],
    mistakes=[
        {"wrong": "Golpear sin parar y sin escuchar.", "why": "Se piensa que explorar es hacer mucho sonido.", "fix": "Haz una prueba, escucha en silencio y luego haz otra."},
        {"wrong": "Cambiar tres cosas a la vez.", "why": "No se sabe cuál produjo el cambio.", "fix": "Cambia una sola cosa y escucha qué pasó."},
    ],
    tiers={
        "recovery": [
            ex("Una cuchara, ¿es una fuente sonora?", "Sí", "Al golpearla produce sonido."),
            ex("Golpeas un tarro con la cuchara y suena fuerte. ¿Qué cualidad describes: intensidad o duración?", "Intensidad", "Fuerte habla de la intensidad."),
            ex("Cuando apagas el sonido con la mano, ¿haces el sonido más largo o más corto?", "Más corto", "Detenerlo acorta su duración."),
        ],
        "understand": [
            ex("¿Por qué conviene cambiar una sola cosa al explorar?", "Para saber qué produjo el cambio", "Si cambias varias a la vez no sabes cuál influyó."),
            ex("¿Qué haces entre una prueba y otra?", "Escucho en silencio", "Escuchar es parte de explorar."),
            ex("¿Explorar es hacer ruido sin parar?", "No", "Se prueba con cuidado y atención."),
        ],
        "apply": [
            ex("Un tarro suena fino cuando lo golpeas en el borde y hondo en el centro. ¿Cuántas posibilidades distintas de altura encontraste?", "2", "Una fina y una honda."),
            ex("Con una botella con arroz puedes sacudirla, rodarla o golpearla suave con un dedo. ¿Cuántas formas de hacerla sonar hay?", "3", "Sacudir, rodar y golpear suave."),
            ex("Quieres un sonido suave y largo con un tarro. Describe cómo lo harías.", "Rozando la tapa suavemente con la yema del dedo y dejando sonar", "Suave se logra con poca fuerza y largo dejando que suene."),
        ],
        "reason": [
            ex("Luz golpeó el tarro con la cuchara con mucha fuerza y luego, con la misma cuchara, con poca fuerza. ¿Qué cualidad cambió?", "La intensidad", "Cambió qué tan fuerte suena."),
            ex("Marco probó diez golpes seguidos sin parar y dice que exploró. ¿Qué le falta?", "Escuchar entre una prueba y otra", "Explorar necesita atención al sonido."),
        ],
        "challenge": [
            ex("Con tu voz encuentra tres sonidos distintos: uno agudo, uno grave y uno largo. Escribe cómo los haces.", "Agudo: voz fina como un pajarito; grave: voz honda como un oso; largo: una vocal sostenida", "Cada uno se hace con un cambio de la voz."),
            ex("Escribe tres posibilidades de sonido de una cuchara de madera y un vaso de plástico.", "Golpear el borde, golpear el fondo y raspar el borde", "Son tres formas distintas de sonar."),
        ],
    },
    context=[ex("Estás en la cocina con una olla, una cuchara de madera y una tapa. Quieres encontrar un sonido grave y otro agudo sin hacer mucho ruido. ¿Qué pruebas?", "Golpear suavemente el fondo de la olla (grave) y el borde de la tapa (agudo)", "El fondo de la olla suena más hondo y la tapa más fino.")],
    selfcheck=[ex("¿Qué es una fuente sonora?", "Lo que produce sonido", "Puede ser un objeto o la voz."), ex("¿Qué cambias al explorar con control?", "Una sola cosa", "Así entiendes el efecto."), ex("¿Qué haces después de cada prueba?", "Escuchar en silencio", "Sirve para notar lo que pasó.")],
    open_task=task(
        "Toma un tarro con tapa y una cuchara de madera. Prueba estas tres formas y descríbelas con sus cualidades: (1) golpear la tapa con la cuchara; (2) golpear el costado con el dedo; (3) raspar la tapa con la uña. Para cada una escribe si suena agudo o grave, fuerte o suave y largo o corto. Tus respuestas pueden variar según tu tarro: lo importante es lo que tú oyes.",
        "(1) Tapa con la cuchara: agudo, fuerte y corto. (2) Costado con el dedo: grave, suave y corto. (3) Raspado con la uña: agudo, suave y largo.",
        ["prueba las tres formas con cuidado", "describe cada una con las tres cualidades", "escucha entre una prueba y otra"],
        ["interpretación", "tabla con las tres descripciones", "explicación oral"],
        ["golpear sin escuchar", "describir con «me gustó» en vez de cualidades"],
        "Reconoce el cuidado y la descripción con cualidades; si las tres suenan igual, que cambie el lugar o la fuerza.",
    ),
    reinforce="Encuentra dos formas de hacer sonar tu voz y descríbelas con una cualidad cada una.",
    extend="Descubre una cuarta forma de sonar con el mismo tarro y compárala con las tres anteriores.",
)

register(
    OA5, 2,
    materials=f"Tus palmas y una persona con quien conversar con sonidos. Patrón de la pregunta: {P(TT, TA, TT, TA)} ({LEY}). Una persona puede ser reemplazada por un peluche si estás solo.",
    use="Aprenderé a improvisar una respuesta musical breve que escucha una pregunta. Sirve para conversar con sonidos y crear ideas nuevas.",
    prior=["Sé tocar un patrón con palmas.", "Sé esperar mi turno."],
    explain=[
        "Improvisar es inventar música en el momento, escuchando. No es hacer ruido sin sentido. Una forma sencilla de improvisar es el juego de pregunta y respuesta. Una persona toca una frase corta, que es la pregunta. Otra persona contesta con otra frase del mismo largo, que es la respuesta.",
        f"Por ejemplo, la pregunta es {P(TT, TA, TT, TA)}. Una respuesta posible es {P(TA, TA, TT, SIL)}: también dura 4 pulsos, pero suena distinto. Una respuesta puede parecerse a la pregunta o cambiar algo. Lo importante es que dure lo mismo y que se note que escuchaste.",
        "Mantén el pulso mientras juegas. Primero escucha la pregunta completa, espera un instante y contesta. Nadie corrige si es bonita o fea; se mira si es breve, si mantuvo el pulso y si dialogó con la pregunta.",
    ],
    vocab=[("improvisar", "inventar música en el momento"), ("pregunta", "frase musical que se toca primero"), ("respuesta", "frase musical que contesta"), ("frase", "grupo corto de sonidos con sentido"), ("turno", "momento en que me toca tocar")],
    worked=[
        {"title": "Responder con el mismo largo", "problem": f"La pregunta es {P(TT, TA, TT, TA)}, de 4 pulsos. ¿Cuántos pulsos debe tener tu respuesta?", "steps": ["La pregunta dura 4 pulsos.", "Mi respuesta debe durar lo mismo.", "Invento una frase de 4 pulsos."], "answer": f"4 pulsos, por ejemplo {P(TA, TA, TT, SIL)}"},
        {"title": "Responder cambiando algo", "problem": f"Escuchas {P(TT, TA, TT, TA)}. Quieres responder parecido pero distinto. ¿Qué haces?", "steps": ["Mantengo el ritmo de ti-ti y TA.", "Cambio un ti-ti por un TA.", "Respondo con una variación."], "answer": f"Por ejemplo {P(TA, TA, TT, TA)}"},
    ],
    mistakes=[
        {"wrong": "Responder antes de que termine la pregunta.", "why": "No se escucha completa.", "fix": "Espera el último sonido y respira."},
        {"wrong": "Responder con una frase mucho más larga.", "why": "No se cuenta el largo de la pregunta.", "fix": "Cuenta los pulsos de la pregunta y responde con la misma cantidad."},
    ],
    tiers={
        "recovery": [
            ex("En un juego de pregunta y respuesta, ¿quién toca primero: la pregunta o la respuesta?", "La pregunta", "Es la frase inicial."),
            ex(f"La pregunta es {P(TA, TA, TA, SIL)}. ¿Cuántos pulsos tiene?", "4", "Cada símbolo ocupa un pulso."),
            ex("Improvisar, ¿es inventar música en el momento o leer una partitura?", "Inventar música en el momento", "No hay partitura previa."),
        ],
        "understand": [
            ex("¿Por qué hay que esperar el final de la pregunta?", "Para escucharla completa", "Así se puede responder bien."),
            ex("¿Qué debe mantener todo el juego?", "El pulso", "Sin pulso común no hay diálogo."),
            ex("¿Una respuesta tiene que ser igual a la pregunta?", "No", "Puede parecerse o cambiar algo."),
        ],
        "apply": [
            ex(f"La pregunta es {P(TA, TT, TA, TA)}. ¿Cuántos sonidos tiene?", str(sounds(TA, TT, TA, TA)), "1 + 2 + 1 + 1 = 5."),
            ex(f"Escribe una respuesta de 4 pulsos a la pregunta {P(TA, TA, TT, SIL)} que use ti-ti.", f"Por ejemplo {P(TT, TA, TT, TA)}", "Una frase de 4 pulsos con ti-ti responde bien."),
            ex(f"Cambia un símbolo de {P(TA, TA, TT, TA)} para hacer una variación de 4 pulsos.", f"Por ejemplo {P(TA, TT, TT, TA)}", "Se cambia un TA por ti-ti y se mantienen 4 pulsos."),
        ],
        "reason": [
            ex("Teo responde con una frase de 8 pulsos a una pregunta de 4. ¿Qué cambiarías?", "Haría la respuesta de 4 pulsos", "La respuesta debe durar lo mismo."),
            ex("¿Cómo sabes que una respuesta escuchó a la pregunta?", "Porque mantiene el pulso y se parece o se relaciona con ella", "Eso muestra que hubo escucha."),
        ],
        "challenge": [
            ex(f"Inventa dos respuestas distintas de 4 pulsos para la pregunta {P(TT, TA, TT, TA)}.", f"Por ejemplo {P(TA, TA, TA, SIL)} y {P(TT, TT, TA, SIL)}", "Ambas duran 4 pulsos y son distintas."),
            ex("Explica con tus palabras por qué improvisar necesita escuchar.", "Porque la respuesta depende de lo que acabo de oír", "Sin escuchar no hay diálogo."),
        ],
    },
    context=[ex("Juegas con tu hermano: él golpea la mesa dos veces rápido y una vez lento. Tú debes contestar. ¿Qué haces primero?", "Escuchar toda la pregunta y esperar un instante", "Responder bien requiere escuchar completa.")],
    selfcheck=[ex("¿Qué es una frase musical?", "Un grupo corto de sonidos con sentido", "Es la pregunta o la respuesta."), ex("¿Cuántos pulsos debe durar la respuesta si la pregunta dura 4?", "4", "Debe durar lo mismo."), ex("¿Improvisar es inventar en el momento?", "Sí", "No se prepara antes.")],
    open_task=task(
        f"Juega a pregunta y respuesta con una persona o con un peluche. La pregunta siempre es {P(TT, TA, TT, TA)}. Tú inventas cuatro respuestas distintas de 4 pulsos cada una; si quieres, copia una y cambia solo un símbolo: {P(TA, TA, TT, SIL)}. Anota cada respuesta con símbolos.",
        f"Pregunta: {P(TT, TA, TT, TA)}. Respuestas: {P(TA, TA, TT, SIL)}; {P(TT, TT, TA, SIL)}; {P(TA, TT, TA, SIL)}; {P(TT, TA, TA, TA)}.",
        ["responde con 4 pulsos", "mantiene el pulso", "inventa respuestas distintas"],
        ["interpretación", "respuestas escritas con símbolos"],
        ["responder sin esperar", "usar respuestas de distinto largo"],
        "Reconoce que respondió escuchando y pide que muestre cómo contó los pulsos; si se alargó, que cuente en voz baja.",
    ),
    reinforce="Haz un juego de pregunta y respuesta con tus manos: una mano pregunta y la otra contesta.",
    extend="Haz que la respuesta termine con un silencio y compara cómo suena.",
)

register(
    OA5, 3,
    materials=f"Tus palmas y una cuchara con un tarro. Tarjetas de reglas que puedes escribir en papeles: «solo 3 sonidos», «solo suave» y «con un silencio». Patrón base: {P(TA, TT, TA, SIL)} ({LEY}).",
    use="Aprenderé a crear dentro de un límite: cambiar una cualidad pero mantener una regla. Sirve para que la improvisación tenga forma y no se desordene.",
    prior=["Sé tocar un patrón corto.", "Sé qué significa suave y fuerte."],
    explain=[
        "Una regla no quita creatividad. Al contrario, la ayuda. Si te digo «improvisa lo que quieras», cuesta empezar. Si te digo «usa solo tres sonidos» o «hazlo todo suave», es más fácil decidir. La regla es el límite; dentro de él, eliges tú.",
        "Cuando improvisas con una regla, varías una cualidad y mantienes el límite. Por ejemplo, la regla es «4 pulsos». Puedes cambiar la fuerza: una vez suave y una vez fuerte. Puedes cambiar la altura: una vez con el borde del tarro y otra con el costado. El largo se mantiene.",
        "Revisa si cumpliste la regla. Cuenta los pulsos, escucha la intensidad y comprueba que el silencio esté donde corresponde. Si te saliste de la regla, tampoco pasa nada: vuelve a intentar. La idea es probar y aprender.",
    ],
    vocab=[("regla", "límite que acuerdo antes de improvisar"), ("variar", "cambiar algo"), ("límite", "lo que no debo pasar"), ("cualidad", "altura, timbre, intensidad o duración"), ("revisar", "comprobar si cumplí la regla")],
    worked=[
        {"title": "Cumplir una regla", "problem": "La regla es «solo 3 sonidos». Improvisas TA, TA, TA, SIL. ¿Cumples la regla?", "steps": ["Cuento los sonidos: TA, TA, TA son 3.", "El silencio no suena.", "Son 3 sonidos."], "answer": "Sí, cumple: son 3 sonidos"},
        {"title": "Variar manteniendo el límite", "problem": f"El patrón base es {P(TA, TT, TA, SIL)} y la regla es «4 pulsos». ¿Cómo varías la intensidad?", "steps": ["Toco el patrón completo con 4 pulsos.", "La primera vez lo hago suave.", "La segunda vez lo hago fuerte y mantengo los 4 pulsos."], "answer": "Cambio suave a fuerte y mantengo los 4 pulsos"},
    ],
    mistakes=[
        {"wrong": "Pensar que con una regla no puedo crear.", "why": "Se cree que la libertad es no tener límites.", "fix": "Dentro del límite hay muchas decisiones que tomar."},
        {"wrong": "Cambiar varias cosas y saltarme la regla.", "why": "Se deja de contar o de escuchar.", "fix": "Cambia una cosa a la vez y comprueba la regla."},
    ],
    tiers={
        "recovery": [
            ex("Una regla, ¿es un límite o una libertad total?", "Un límite", "Marca hasta dónde se puede llegar."),
            ex("Con la regla «solo suave», ¿puedes tocar fuerte?", "No", "Sería salirse de la regla."),
            ex("Con la regla «4 pulsos», ¿puedes tocar 6 pulsos?", "No", "Excede el límite de 4."),
        ],
        "understand": [
            ex("¿Por qué una regla ayuda a improvisar?", "Porque facilita decidir", "Limita las opciones y es más fácil elegir."),
            ex("¿Qué haces para comprobar la regla de pulsos?", "Cuento los pulsos", "Contar permite revisar el largo."),
            ex("Si te sales de la regla, ¿qué haces?", "Vuelvo a intentarlo", "Probar es parte de aprender."),
        ],
        "apply": [
            ex("La regla es «solo 2 sonidos». ¿Cuál cumple: TA – TA – SIL – SIL o TA – ti-ti – SIL – SIL?", "TA – TA – SIL – SIL", "Suenan 2 TA; en el otro suenan 3."),
            ex(f"Toca {P(TA, TT, TA, SIL)} una vez suave y una vez fuerte. ¿Qué cualidad varió?", "La intensidad", "Pasó de suave a fuerte."),
            ex("La regla es «incluir un silencio». ¿Qué patrón cumple: TA – TA – TA – TA o TA – TA – SIL – TA?", "TA – TA – SIL – TA", "Es el único que tiene un silencio."),
        ],
        "reason": [
            ex("Diana dice «con reglas ya no puedo inventar». ¿Qué le responderías?", "Que dentro de la regla puede elegir sonidos, fuerza y silencios", "Las decisiones siguen existiendo."),
            ex("¿Por qué conviene cambiar una sola cualidad a la vez?", "Para entender qué cambió", "Se escucha el efecto con claridad."),
        ],
        "challenge": [
            ex("Crea tu propia regla de improvisación de una línea y escríbela.", "Por ejemplo: solo 4 pulsos y con un silencio al final", "Una regla clara se puede comprobar."),
            ex("Inventa un patrón de 4 pulsos con exactamente 3 sonidos y al menos un silencio.", f"Por ejemplo {P(TA, TA, TA, SIL)} o {P(TA, TT, SIL, SIL)}", "Debe sumar 3 sonidos (TA vale 1 y ti-ti vale 2) y contener un silencio."),
        ],
    },
    context=[ex("Tu profesora dice: «improvisen con la regla de usar solo el tarro y tocar suave». ¿Qué cosas puedes elegir tú?", "Dónde golpear, cuántos golpes y los silencios", "Esas decisiones siguen siendo tuyas.")],
    selfcheck=[ex("¿Qué es una regla de improvisación?", "Un límite acordado", "Marca lo que no se puede pasar."), ex("¿Qué haces para comprobar tu regla?", "Contar y escuchar", "Así sé si la cumplí."), ex("¿Una regla impide crear?", "No", "Ayuda a crear.")],
    open_task=task(
        f"Elige una de estas reglas: (a) solo 3 sonidos, (b) todo suave, (c) con un silencio al final. Improvisa un patrón de 4 pulsos que cumpla la regla, tócalo con palmas dos veces y cámbiale una cualidad la segunda vez sin romper la regla (por ejemplo, el lugar donde golpeas; si elegiste «todo suave», no lo toques fuerte). Escribe tu patrón con símbolos y comprueba la regla. Puedes partir de {P(TA, TT, TA, SIL)}.",
        f"Elegí (c). Mi patrón fue {P(TA, TA, TT, SIL)}. Cumple la regla porque termina en silencio. La segunda vez lo toqué más suave.",
        ["cumple la regla elegida", "mantiene 4 pulsos", "cambia una cualidad en la segunda vez"],
        ["interpretación", "patrón escrito", "comprobación oral"],
        ["salirse de la regla sin darse cuenta", "cambiar varias cosas a la vez"],
        "Reconoce la regla cumplida y pide que muestre cómo la comprobó; si se salió, que cuente los pulsos en voz alta.",
    ),
    reinforce="Toca un patrón de 4 pulsos con la regla «solo suave».",
    extend="Combina dos reglas a la vez y comprueba si puedes cumplirlas.",
)

register(
    OA5, 4,
    materials=f"Una cuchara, un tarro y tus palmas. Papel y colores. Patrón de apoyo: {P(TA, TT, TA, SIL)} y {P(TA, TA, TT, SIL)} ({LEY}).",
    use="Aprenderé a organizar una miniatura musical con inicio, contraste y cierre. Sirve para que mis ideas se conviertan en una pieza breve.",
    prior=["Sé improvisar un patrón corto.", "Sé qué es una sección que regresa."],
    explain=[
        "Una miniatura musical es una pieza muy corta que tiene tres partes: inicio, contraste y cierre. El inicio presenta la idea. El contraste muestra algo distinto. El cierre termina la pieza, muchas veces regresando a la idea del inicio.",
        f"Por ejemplo, el inicio puede ser el patrón {P(TA, TT, TA, SIL)} tocado suave. El contraste puede ser {P(TA, TA, TT, SIL)} tocado fuerte. El cierre puede volver al primer patrón. Así la forma es A – B – A y cada parte dura 4 pulsos.",
        "Para que una miniatura tenga sentido, decide antes cuánto dura cada parte y qué cambia entre una y otra. Puedes cambiar la intensidad, el instrumento o el patrón. Al final, queda un silencio breve. Anota tu miniatura en un papel con símbolos para poder repetirla.",
    ],
    vocab=[("miniatura", "pieza musical muy corta"), ("inicio", "primera parte; presenta la idea"), ("contraste", "parte distinta de la anterior"), ("cierre", "parte final"), ("forma", "orden de las partes de una pieza")],
    worked=[
        {"title": "Armar A – B – A", "problem": f"Usa {P(TA, TT, TA, SIL)} como A y {P(TA, TA, TT, SIL)} como B. Escribe la miniatura completa.", "steps": ["Inicio: A suave.", "Contraste: B fuerte.", "Cierre: A suave."], "answer": f"{P(TA, TT, TA, SIL)} (suave) / {P(TA, TA, TT, SIL)} (fuerte) / {P(TA, TT, TA, SIL)} (suave)"},
        {"title": "Contar pulsos", "problem": "Si cada parte dura 4 pulsos y hay tres partes, ¿cuántos pulsos dura la miniatura?", "steps": ["Cada parte son 4 pulsos.", "Hay 3 partes.", "4 × 3 = 12."], "answer": "12 pulsos"},
    ],
    mistakes=[
        {"wrong": "Hacer tres partes iguales y creer que hay contraste.", "why": "No se cambia nada entre ellas.", "fix": "Cambia al menos una cualidad en la parte del medio."},
        {"wrong": "No terminar la pieza con un cierre claro.", "why": "Se deja de tocar sin plan.", "fix": "Vuelve a la idea inicial o termina con un silencio."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuáles son las tres partes de una miniatura?", "Inicio, contraste y cierre", "Son las partes que organizan la pieza."),
            ex("¿Qué parte presenta la idea?", "El inicio", "Es la primera parte."),
            ex("¿Qué parte termina la pieza?", "El cierre", "Es la última parte."),
        ],
        "understand": [
            ex("¿Para qué sirve el contraste?", "Para mostrar algo distinto", "Cambia respecto del inicio."),
            ex("¿Cómo puede ser el cierre?", "Volviendo a la idea del inicio o con un silencio", "Así termina con sentido."),
            ex("Si A y B son iguales, ¿hay contraste?", "No", "Contraste es que haya diferencia."),
        ],
        "apply": [
            ex("Una miniatura tiene tres partes de 4 pulsos cada una. ¿Cuántos pulsos dura?", "12", "4 + 4 + 4 = 12."),
            ex("Escribe la forma de una miniatura con inicio, contraste y cierre que regresa.", "A – B – A", "El cierre regresa a la idea del inicio."),
            ex("Tu miniatura tiene el inicio suave y el contraste fuerte. ¿Qué cualidad cambió?", "La intensidad", "Pasó de suave a fuerte."),
        ],
        "reason": [
            ex("Santi tocó tres partes iguales de 4 pulsos. ¿Qué le sugerirías cambiar?", "Cambiar la parte del medio, por ejemplo tocarla más fuerte", "Un contraste necesita una diferencia."),
            ex("¿Por qué anotar la miniatura con símbolos?", "Para poder repetirla", "Lo anotado se recuerda y se toca igual."),
        ],
        "challenge": [
            ex(f"Inventa una miniatura de forma A – B – A. Usa {P(TA, TT, TA, SIL)} para A y escribe tú el patrón B de 4 pulsos.", f"Por ejemplo B = {P(TA, TA, TA, SIL)}", "B es distinto de A y dura 4 pulsos."),
            ex("Tu miniatura es A – B – A, con cada parte de 4 pulsos y una pausa de 2 pulsos al final. ¿Cuántos pulsos suman en total?", "14", "12 pulsos más 2 de pausa."),
        ],
    },
    context=[ex("Quieres tocar para tu abuela una miniatura con tarro y cuchara. Decides empezar suave, seguir fuerte y terminar suave. ¿Qué forma tiene?", "A – B – A", "Empieza y termina igual con un contraste en medio.")],
    selfcheck=[ex("¿Qué es una miniatura musical?", "Una pieza muy corta", "Tiene inicio, contraste y cierre."), ex("¿Cuántas partes tiene?", "3", "Inicio, contraste y cierre."), ex("¿Qué parte puede regresar al final?", "El inicio", "Así se cierra la forma.")],
    open_task=task(
        f"Crea tu miniatura musical. Usa A = {P(TA, TT, TA, SIL)} y B = {P(TA, TA, TT, SIL)}. Tócala en el orden A – B – A con un tarro y una cuchara: A suave, B fuerte, A suave. Anótala con símbolos, cuenta cuántos pulsos dura y dile a alguien cuál es el inicio, el contraste y el cierre.",
        f"Mi miniatura: A suave ({P(TA, TT, TA, SIL)}), B fuerte ({P(TA, TA, TT, SIL)}) y A suave. Dura 12 pulsos. El contraste es B y el cierre es A.",
        ["tiene inicio, contraste y cierre", "cambia una cualidad en el contraste", "cuenta los pulsos correctamente"],
        ["interpretación", "partitura con símbolos", "explicación oral"],
        ["partes sin contraste", "no marcar el cierre"],
        "Reconoce la forma completa y pregunta cómo contó los pulsos; si el contraste no se oye, que cambie la fuerza.",
    ),
    reinforce="Toca solo el inicio y el cierre de tu miniatura, sin el contraste, y compara.",
    extend="Agrega una pausa de 2 pulsos entre las partes y cuenta qué cambia.",
)

# ---------------------------------------------------------------- OA 06
register(
    OA6, 1,
    materials=f"Lápiz y papel. Dos trabajos musicales entre los que puedes elegir: (1) el patrón {P(TA, TT, TA, SIL)} con palmas, suave y lento; (2) el patrón {P(TA, TA, TT, SIL)} con tarro y cuchara, fuerte y rápido. Leyenda: {LEY}.",
    use="Aprenderé a decidir qué quiero comunicar y a quién. Sirve para elegir y preparar un trabajo musical que quiero compartir.",
    prior=["Sé tocar un patrón corto.", "Sé decir cómo se siente un sonido."],
    explain=[
        "Antes de presentar un trabajo musical, hay que pensar para qué y para quién. El propósito es lo que quiero lograr: calmar, hacer bailar, contar una idea o alegrar. La audiencia son las personas que van a escuchar: mi familia, mis compañeros o mi curso.",
        "El propósito ayuda a decidir cómo toco. Si quiero calmar, elijo sonidos suaves y lentos. Si quiero hacer bailar, elijo un pulso claro y rápido. Si la audiencia es pequeña, puedo tocar más suave. Si es grande, necesito que se oiga más.",
        "También decido qué mostrar: una canción, un patrón, una miniatura. Presentar no es buscar la perfección. Es compartir con cuidado lo que preparé. Puedo equivocarme y seguir; lo que importa es que quede claro qué quise comunicar.",
    ],
    vocab=[("propósito", "lo que quiero lograr con mi música"), ("audiencia", "las personas que escuchan"), ("comunicar", "hacer que otros entiendan una idea"), ("elegir", "decidir entre varias opciones"), ("compartir", "mostrar a otros lo que hice")],
    worked=[
        {"title": "Elegir según el propósito", "problem": "Quieres calmar a tu hermano antes de dormir. ¿Qué trabajo eliges de los dos de esta clase?", "steps": ["Calmar pide sonidos suaves y lentos.", "El trabajo 1 es suave y lento.", "El trabajo 2 es fuerte y rápido."], "answer": "El trabajo 1, suave y lento"},
        {"title": "Pensar en la audiencia", "problem": "Vas a tocar para 30 niños en un patio. ¿Qué cualidad cuidas?", "steps": ["Mucha gente necesita oír bien.", "Cuido la intensidad: que no sea tan suave.", "Sin gritar ni golpear muy fuerte."], "answer": "Que la intensidad sea suficiente para oírse"},
    ],
    mistakes=[
        {"wrong": "Elegir un trabajo solo porque «es el más fácil».", "why": "No se piensa en el propósito.", "fix": "Pregunta para qué lo voy a mostrar y a quién."},
        {"wrong": "Querer presentar solo cuando todo es perfecto.", "why": "Se cree que compartir exige no equivocarse.", "fix": "Presentar es compartir con cuidado; si te equivocas, sigues."},
    ],
    tiers={
        "recovery": [
            ex("La audiencia, ¿son las personas que escuchan o las que tocan?", "Las que escuchan", "Es el público."),
            ex("El propósito, ¿es lo que quiero lograr o lo que me gusta?", "Lo que quiero lograr", "Define el para qué."),
            ex("¿Hay que ser perfecto para compartir música?", "No", "Compartir es mostrar con cuidado."),
        ],
        "understand": [
            ex("¿Por qué se piensa en la audiencia antes de tocar?", "Para que todos puedan oír y entender", "La audiencia define cómo tocar."),
            ex("Si el propósito es hacer bailar, ¿qué cualidad ayuda: pulso claro o silencio largo?", "Pulso claro", "El pulso marcado invita a moverse."),
            ex("¿Qué haces si te equivocas al presentar?", "Sigo adelante", "Se puede continuar con calma."),
        ],
        "apply": [
            ex(f"Quieres hacer bailar a tu curso. ¿Eliges {P(TA, TT, TA, SIL)} suave y lento o {P(TA, TA, TT, SIL)} fuerte y rápido?", f"{P(TA, TA, TT, SIL)} fuerte y rápido", "Fuerte y rápido tiene un pulso claro para bailar."),
            ex("Vas a tocar para tu abuela, que oye poco. ¿Qué cualidad cuidas?", "La intensidad, que no sea muy suave", "Debe oírse bien."),
            ex("Quieres que tu mamá se relaje. ¿Tocas rápido y fuerte o lento y suave?", "Lento y suave", "Calmar pide suavidad y lentitud."),
        ],
        "reason": [
            ex("Un niño dice: «Voy a tocar lo más fuerte para que todos me aplaudan». ¿Qué falta?", "Pensar en el propósito y en cómo se sentirá la audiencia", "Fuerte no siempre es lo mejor."),
            ex("¿Por qué el mismo trabajo puede cambiar según la audiencia?", "Porque hay que adaptar la fuerza y el espacio", "No es igual tocar para dos personas que para treinta."),
        ],
        "challenge": [
            ex("Escribe en una frase el propósito y la audiencia de una presentación inventada por ti.", "Por ejemplo: quiero calmar a mi hermano con un patrón suave", "Dice para qué y para quién."),
            ex("Si tu propósito es alegrar a tu curso, ¿qué dos cualidades eliges para tu trabajo?", "Rápido y fuerte, por ejemplo", "Esas cualidades dan energía."),
        ],
    },
    context=[ex("Tu curso hará una muestra para las familias en el patio. Tienes dos trabajos: uno muy suave y otro fuerte. El patio es grande. ¿Cuál eliges y por qué?", "El fuerte, porque en el patio se necesita que se oiga", "Un espacio grande necesita más intensidad.")],
    selfcheck=[ex("En Música, ¿qué es el propósito?", "Lo que quiero lograr", "Es el para qué."), ex("¿Quién es la audiencia?", "Las personas que escuchan", "Es el público."), ex("¿Es obligatorio no equivocarse?", "No", "Compartir no es buscar perfección.")],
    open_task=task(
        f"Elige entre estos dos trabajos: (1) {P(TA, TT, TA, SIL)} con palmas, suave y lento; (2) {P(TA, TA, TT, SIL)} con tarro y cuchara, fuerte y rápido. Escribe tu propósito y tu audiencia en una frase y explica por qué elegiste ese trabajo. Tócalo una vez.",
        "Elegí el 1. Mi propósito es calmar a mi hermano y mi audiencia es mi hermano. Elegí el 1 porque es suave y lento.",
        ["elige un trabajo", "escribe propósito y audiencia", "explica la elección con una cualidad"],
        ["frase escrita", "interpretación", "explicación oral"],
        ["no explicar la elección", "elegir sin pensar en la audiencia"],
        "Reconoce que su elección tiene razón y pregunta qué cualidad la apoya; si no hay propósito, que lo escriba.",
    ),
    reinforce="Escribe una frase con el propósito de una música que conoces.",
    extend="Elige el mismo trabajo para dos audiencias y cuenta qué cambiarías en cada una.",
)

register(
    OA6, 2,
    materials=f"Lápiz y tarjetas de papel con los roles: director, intérprete y presentador. Trabajo para presentar: el patrón {P(TA, TT, TA, SIL)} tocado tres veces ({LEY}). Señales: mano arriba prepara, mano baja empieza, puño cierra.",
    use="Aprenderé a repartir roles y a usar señales para coordinar inicio, desarrollo y final. Sirve para presentar en grupo sin perderme.",
    prior=["Sé tocar un patrón corto.", "Sé usar señales de empezar y terminar."],
    explain=[
        "Cuando varias personas presentan juntas, cada una tiene un rol. El presentador dice qué se va a tocar. El director da las señales. Los intérpretes tocan o cantan. Si es un trabajo individual, una sola persona hace todo, pero también puede pensar en cada rol.",
        "Una presentación tiene tres momentos: inicio, desarrollo y final. En el inicio, el presentador saluda y dice el nombre del trabajo. En el desarrollo, se toca. En el final, el director cierra el puño, se hace silencio y se agradece. Todos saben cuándo les toca.",
        "Las señales son parte del trabajo. Antes de empezar, cuenten pulsos en voz baja. Si alguien se pierde, no se detiene: busca el pulso y vuelve. Decidan antes quién hace qué y cuántas veces se repite el patrón. Ensayen una vez completa.",
    ],
    vocab=[("rol", "tarea de cada persona en el grupo"), ("presentador", "persona que dice qué se va a tocar"), ("director", "persona que da señales"), ("desarrollo", "parte del medio, cuando se toca"), ("agradecer", "decir gracias al terminar")],
    worked=[
        {"title": "Repartir roles", "problem": "Son tres niños y deben presentar el patrón TA – ti-ti – TA – SIL. ¿Cómo reparten los roles?", "steps": ["Uno es presentador.", "Otro es director.", "El tercero es intérprete."], "answer": "Presentador, director e intérprete"},
        {"title": "Ordenar los momentos", "problem": "Ordena: tocar el patrón; saludar y decir el nombre; agradecer en silencio.", "steps": ["Primero se saluda y se dice el nombre (inicio).", "Luego se toca (desarrollo).", "Al final se agradece (final)."], "answer": "Saludar y decir el nombre; tocar; agradecer"},
    ],
    mistakes=[
        {"wrong": "Empezar a tocar sin la señal del director.", "why": "No se espera la señal acordada.", "fix": "Mira la mano que baja y empieza."},
        {"wrong": "Olvidar el final y salir corriendo.", "why": "No se planea el final.", "fix": "Haz silencio un instante y agradece."},
    ],
    tiers={
        "recovery": [
            ex("¿Quién da las señales en una presentación?", "El director", "Es su rol."),
            ex("¿Quién dice qué se va a tocar?", "El presentador", "Es su rol."),
            ex("¿Qué se hace al final de la presentación?", "Se hace silencio y se agradece", "Así se cierra con claridad."),
        ],
        "understand": [
            ex("¿Para qué sirve repartir roles?", "Para que todos sepan qué hacer", "Así se evitan las confusiones."),
            ex("¿Cuáles son los tres momentos de una presentación?", "Inicio, desarrollo y final", "Organizan lo que se hace."),
            ex("Si alguien se pierde, ¿qué hace?", "Busca el pulso y vuelve", "No se detiene todo el grupo."),
        ],
        "apply": [
            ex(f"Cuentan el patrón {P(TA, TT, TA, SIL)} tres veces. ¿Cuántos pulsos tocan?", "12", "4 pulsos × 3 veces = 12."),
            ex("Son cuatro niños: un presentador, un director y dos intérpretes. ¿Cuántos intérpretes hay?", "2", "Los otros dos tienen otros roles."),
            ex("Escribe una frase para el inicio de la presentación.", "Por ejemplo: Hola, vamos a presentar un patrón de palmas", "El inicio saluda y anuncia."),
        ],
        "reason": [
            ex("Un niño toca antes de la señal. ¿Qué debió esperar?", "La señal del director", "La mano que baja dice cuándo empezar."),
            ex("¿Por qué conviene ensayar una vez completa antes de presentar?", "Para detectar problemas y mejorar", "Ensayar ayuda a corregir."),
        ],
        "challenge": [
            ex("Arma un plan de presentación para dos personas: roles y señal de inicio.", "Una toca y otra dirige; la mano baja empieza", "Debe asignar roles y señal."),
            ex("Escribe qué dices al final de tu presentación.", "Gracias por escuchar", "Es una forma de cerrar con respeto."),
        ],
    },
    context=[ex("Tu grupo tiene un presentador, un director y un intérprete. En medio de la presentación el intérprete pierde el pulso. ¿Qué puede hacer el director?", "Mostrar el pulso con la mano para que lo recupere", "La señal ayuda a volver al pulso.")],
    selfcheck=[ex("¿Qué rol dice el nombre del trabajo?", "El presentador", "Anuncia lo que se toca."), ex("¿Cuántos momentos tiene una presentación?", "3", "Inicio, desarrollo y final."), ex("¿Qué haces antes de empezar?", "Contar pulsos en voz baja", "Así empiezan juntos.")],
    open_task=task(
        f"Con un peluche o una persona prepara esta presentación: (1) el presentador saluda y dice «Vamos a tocar un patrón de palmas»; (2) el director levanta la mano, cuenta 1, 2, 3, 4 y la baja; (3) todos tocan {P(TA, TT, TA, SIL)} tres veces; (4) el director cierra el puño y todos agradecen. Anota qué rol hizo cada uno.",
        "Yo fui presentador y mi hermana directora. Dije mi saludo, ella contó y tocamos el patrón tres veces. Terminamos con el puño y dijimos gracias.",
        ["reparte roles", "sigue los cuatro pasos en orden", "usa las señales"],
        ["presentación observada", "roles escritos"],
        ["olvidar el saludo o el final", "empezar antes de la señal"],
        "Reconoce el orden de los pasos y pide que cuente quién hizo qué; si faltó el final, que lo repita con agradecimiento.",
    ),
    reinforce="Ensaya el saludo y el final de una presentación frente a un espejo.",
    extend="Cambia los roles y presenta de nuevo para ver qué cambia.",
)

register(
    OA6, 3,
    materials=f"Lápiz, tarro y cuchara. Patrón: {P(TA, TA, TT, SIL)} ({LEY}). Pauta de ensayo con tres criterios: mantiene el pulso, empieza y termina con la señal y se oye clara la fuerza pedida.",
    use="Aprenderé a ensayar mejorando un aspecto audible usando evidencia. Sirve para que mi presentación esté mejor preparada.",
    prior=["Sé tocar un patrón corto.", "Sé qué es el pulso y la intensidad."],
    explain=[
        "Ensayar es repetir para mejorar, pero con un objetivo. No se repite por repetir. Antes de ensayar elige un aspecto audible para mejorar: el pulso parejo, la fuerza, el final claro. Después de tocar, comprueba si mejoró.",
        "La evidencia es algo que se oye o se ve y que prueba si mejoró. Por ejemplo, contar en voz baja los pulsos y ver si el patrón coincide. O pedir a alguien que diga si oyó el silencio en su lugar. La evidencia es mejor que decir «me parece que sí».",
        "Usa una pauta de ensayo, que es una lista de lo que debe cumplirse. Toca tu patrón dos veces y compara la primera vez con la segunda. Mejorar un solo aspecto a la vez es suficiente. Tampoco hay que buscar la perfección, sino un paso adelante.",
    ],
    vocab=[("ensayar", "repetir para mejorar"), ("aspecto", "una parte que se puede mejorar"), ("evidencia", "algo que se oye o se ve y lo prueba"), ("pauta", "lista de criterios para revisar"), ("comparar", "mirar en qué cambió entre dos intentos")],
    worked=[
        {"title": "Elegir un aspecto", "problem": "Tu patrón se acelera al final. ¿Qué aspecto eliges mejorar?", "steps": ["Noto que pierdo el pulso.", "El aspecto es mantener el pulso parejo.", "Ensayo con el pie marcando."], "answer": "Mantener el pulso parejo"},
        {"title": "Usar evidencia", "problem": "¿Cómo compruebas que mejoraste el pulso?", "steps": ["Marco el pulso con el pie.", "Cuento si los TA coinciden con los pasos.", "Si coinciden, mejoré."], "answer": "Los golpes coinciden con los pasos"},
    ],
    mistakes=[
        {"wrong": "Repetir sin pensar qué mejorar.", "why": "No hay objetivo.", "fix": "Elige un aspecto antes de tocar."},
        {"wrong": "Decir «mejoró» sin evidencia.", "why": "Solo se tiene la impresión.", "fix": "Apóyate en algo que se pueda oír o contar."},
    ],
    tiers={
        "recovery": [
            ex("¿Para qué se ensaya?", "Para mejorar", "Es repetir con objetivo."),
            ex("Una pauta, ¿es una lista de criterios o un instrumento?", "Una lista de criterios", "Dice qué revisar."),
            ex("¿Se mejora de una vez todo?", "No, un aspecto a la vez", "Es más fácil enfocarse."),
        ],
        "understand": [
            ex("En Música: ¿Qué es la evidencia?", "Algo que se oye o se ve y prueba la mejora", "Sirve para comprobar."),
            ex("¿Por qué elegir un aspecto antes de ensayar?", "Para tener un objetivo", "Así se sabe qué comprobar."),
            ex("¿Qué comparas entre dos ensayos?", "En qué cambió", "Se ve la mejora."),
        ],
        "apply": [
            ex(f"Tocas {P(TA, TA, TT, SIL)} y quieres mejorar el silencio final. ¿Qué puedes hacer?", "Contar en voz baja el cuarto pulso y no tocar", "El cuarto pulso es el silencio."),
            ex("Ensayas dos veces. En la primera falló el pulso 3 veces; en la segunda, 1 vez. ¿Cuántas veces menos falló?", "2", "3 menos 1 es 2."),
            ex("Quieres comprobar que no aceleras. ¿Qué evidencia usas?", "Que los golpes coincidan con el pie", "El pie marca el pulso."),
        ],
        "reason": [
            ex("Un niño dice «mejoré» pero no sabe en qué. ¿Qué le falta?", "Evidencia", "Necesita algo que lo pruebe."),
            ex("¿Por qué es mejor mejorar un aspecto a la vez?", "Porque es más fácil comprobar", "Se enfoca la atención."),
        ],
        "challenge": [
            ex("Escribe una pauta de ensayo con tres criterios para tu presentación.", "Por ejemplo: pulso parejo, empezar con la señal y terminar juntos", "Cada criterio se puede comprobar."),
            ex("Cuenta una evidencia para comprobar que la fuerza fue suave.", "Que la persona que escucha diga que se oyó suave", "Otra persona puede comprobarlo."),
        ],
    },
    context=[ex("Mañana presentas en el curso. Ensayaste una vez y notaste que te adelantas. ¿Qué haces hoy?", "Ensayo marcando el pulso con el pie", "Un objetivo claro permite mejorar.")],
    selfcheck=[ex("¿Qué es una pauta?", "Una lista de criterios", "Sirve para revisar."), ex("¿Cuántos aspectos mejoras primero?", "Uno", "Un aspecto a la vez."), ex("En un ensayo, ¿qué llamamos evidencia?", "Algo que se oye o se ve", "Prueba la mejora del ensayo.")],
    open_task=task(
        f"Ensaya el patrón {P(TA, TA, TT, SIL)} con un tarro y cuchara dos veces. Antes elige un aspecto de la pauta: (a) pulso parejo, (b) silencio en su lugar, (c) empezar y terminar con señal. Anota cómo te fue en el primer intento y en el segundo, y qué evidencia usaste.",
        "Elegí (a). En el primer intento me adelanté en el tercer pulso. En el segundo marqué con el pie y coincidió. La evidencia fue que mis golpes coincidían con los pasos.",
        ["elige un aspecto", "compara dos intentos", "nombra una evidencia"],
        ["registro escrito", "interpretación"],
        ["no elegir un aspecto", "decir que mejoró sin evidencia"],
        "Reconoce el aspecto elegido y pregunta qué evidencia usó; si no hay diferencia, que cambie algo en el segundo intento.",
    ),
    reinforce="Ensaya una vez tu patrón y cuenta cuántas veces perdiste el pulso.",
    extend="Pide a alguien que escuche tu ensayo y te diga si oyó el silencio.",
)

register(
    OA6, 4,
    materials=f"Lápiz y papel. Trabajo para presentar: {P(TA, TT, TA, SIL)} tocado tres veces con palmas ({LEY}). Una persona o un peluche como audiencia. Frases para conversar escritas en la clase.",
    use="Aprenderé a presentar mi música y a responder con respeto una pregunta. Sirve para compartir lo que hago y escuchar a los demás.",
    prior=["Sé tocar un patrón corto.", "Sé escuchar sin interrumpir."],
    explain=[
        "Presentar es mostrar tu trabajo a otras personas. Puedes sentir nervios, y eso es normal. Respira, mira a la audiencia, di el nombre de tu trabajo, toca y agradece. Si te equivocas, sigue como puedas; lo importante es compartir.",
        "Después de presentar, la audiencia puede comentar y preguntar. Hay comentarios que ayudan: «Me gustó cuando tocaste suave porque se oyó el silencio». Hay preguntas respetuosas: «¿Cómo hiciste el silencio?». No se opina sobre la persona, sino sobre lo que se oyó.",
        "Cuando te hagan una pregunta, escucha completa y responde con calma. Si no sabes, di «no lo sé todavía». Cuando seas audiencia, aplaude al final y espera tu turno para hablar. Una buena conversación hace que todos aprendan.",
    ],
    vocab=[("presentar", "mostrar mi trabajo a otros"), ("comentario", "lo que digo sobre lo que oí"), ("pregunta respetuosa", "pregunta que no juzga a la persona"), ("nervios", "sensación antes de mostrar algo; es normal"), ("turno", "momento de hablar")],
    worked=[
        {"title": "Un buen comentario", "problem": "Tu compañero tocó un patrón suave. ¿Cuál es un buen comentario?", "steps": ["Digo lo que me gustó.", "Doy la pista que oí.", "Hablo del trabajo, no de la persona."], "answer": "Me gustó que tocaras suave porque se oyó el silencio"},
        {"title": "Responder una pregunta", "problem": "Te preguntan «¿cómo hiciste el silencio?». No lo tenías pensado. ¿Qué respondes?", "steps": ["Escucho la pregunta completa.", "Respondo lo que sé: conté el cuarto pulso.", "Si no sé, digo que no lo sé todavía."], "answer": "Conté el cuarto pulso y no toqué"},
    ],
    mistakes=[
        {"wrong": "Burlarse de un error del compañero.", "why": "Se evalúa a la persona.", "fix": "Comenta lo que oíste con respeto."},
        {"wrong": "Quedarse callado y no responder la pregunta.", "why": "Se siente miedo de equivocarse.", "fix": "Responde lo que sabes o di «no lo sé todavía»."},
    ],
    tiers={
        "recovery": [
            ex("Al comenzar tu presentación, ¿qué anuncias?", "El nombre de mi trabajo", "Anuncia lo que vas a mostrar."),
            ex("Sentir nervios al presentar, ¿es normal o es malo?", "Normal", "Muchas personas los sienten."),
            ex("Al final de la presentación, ¿qué haces?", "Agradezco", "Es una forma respetuosa de cerrar."),
        ],
        "understand": [
            ex("¿Sobre qué se opina en un comentario?", "Sobre lo que se oyó", "No sobre la persona."),
            ex("¿Qué haces si no sabes responder una pregunta?", "Digo que no lo sé todavía", "Es una respuesta honesta."),
            ex("¿Cuándo se habla en la conversación?", "En el turno propio", "Se respeta a los demás."),
        ],
        "apply": [
            ex("Completa: Me gustó que ___ porque se oyó ___. Usa «tocaste suave» y «el silencio».", "Me gustó que tocaras suave porque se oyó el silencio", "Une lo que gustó con la pista."),
            ex("Escribe una pregunta respetuosa sobre cómo se hizo el patrón.", "¿Cómo lo practicaste?", "La pregunta pide información sin juzgar."),
            ex("Tocas el patrón TA – ti-ti – TA – SIL tres veces. ¿Cuántos pulsos tocas?", "12", "4 pulsos × 3 veces = 12."),
        ],
        "reason": [
            ex("Un niño dice «tocas feo». ¿Por qué no es un buen comentario?", "Porque juzga y no dice qué se oyó", "No da una pista ni respeta."),
            ex("¿Por qué es mejor responder que quedarse callado?", "Porque se comparte lo que se sabe", "Una conversación es compartir."),
        ],
        "challenge": [
            ex("Escribe un comentario con dos partes: lo que te gustó y la pista sonora.", "Me gustó la fuerza porque se oyó claro el pulso", "Incluye gusto y pista."),
            ex("Cuenta tres pasos para presentar con calma cuando tienes nervios.", "Respirar, mirar a la audiencia y empezar con la señal", "Son pasos que ayudan a calmarse."),
        ],
    },
    context=[ex("Presentas tu patrón al curso y una compañera pregunta: «¿por qué elegiste ese patrón?». ¿Cómo respondes?", "Digo el propósito y una cualidad, por ejemplo: porque quería calmar y es suave", "Respondes con razones propias.")],
    selfcheck=[ex("¿Sobre qué se comenta?", "Sobre lo que se oyó", "No sobre la persona."), ex("En Música, ¿qué dices si no sabes?", "No lo sé todavía", "Es una respuesta honesta."), ex("En Música, ¿qué haces al terminar?", "Agradezco", "Cierra con respeto.")],
    open_task=task(
        f"Presenta a una persona o a un peluche tu patrón {P(TA, TT, TA, SIL)} tocado tres veces con palmas. Di el nombre del trabajo, toca y agradece. Luego pide que te hagan una pregunta. Si no hay nadie, escribe tú una pregunta respetuosa y tu respuesta. Anota un comentario sobre lo que oíste.",
        "Dije: «Presento un patrón de palmas». Lo toqué tres veces y agradecí. Mi mamá preguntó cómo conté el silencio. Respondí que conté el cuarto pulso. Mi comentario: se oyó el silencio bien.",
        ["presenta con saludo, interpretación y agradecimiento", "responde una pregunta", "escribe un comentario sobre lo que oyó"],
        ["presentación observada", "pregunta y respuesta escritas", "comentario"],
        ["opinar sobre la persona", "no responder la pregunta"],
        "Reconoce el valor de compartir y pregunta qué pista usó en su comentario; si se equivocó, valora que siguió adelante.",
    ),
    reinforce="Practica en voz alta una frase de saludo y una de agradecimiento.",
    extend="Inventa tres preguntas respetuosas para hacer a un compañero después de una presentación.",
)

# ---------------------------------------------------------------- OA 07
register(
    OA7, 1,
    materials="Lápiz, papel y colores. Rutina de ejemplo escrita en la clase: despertar, desayunar, ir al colegio, jugar en el patio, volver a casa, bañarse y dormir.",
    use="Aprenderé a localizar los sonidos que hay en mi rutina del día. Sirve para darme cuenta de cuánta música y sonido hay en mi vida.",
    prior=["Sé nombrar momentos de mi día.", "Sé quedarme en silencio y escuchar."],
    explain=[
        "En nuestra vida hay sonidos y música todo el día. Algunos son sonidos de la casa, como el agua o los pasos. Otros son música que alguien pone o canta. Un mapa sonoro es un dibujo que muestra qué sonidos hay y dónde y cuándo suenan.",
        "Para armar un mapa sonoro, piensa en una rutina. Por ejemplo: despertar, desayunar, ir al colegio, jugar en el patio, volver a casa, bañarse y dormir. En cada momento escribe uno o dos sonidos y descríbelos con las cualidades: fuerte o suave, largo o corto, agudo o grave.",
        "Escucha a tu alrededor sin grabar a nadie. Si quieres, toma nota con palabras o dibujos. No hace falta escribir nombres de personas ni lugares exactos. Solo di «mi casa», «el patio» o «la calle».",
    ],
    vocab=[("rutina", "lo que hago cada día en orden"), ("mapa sonoro", "dibujo que muestra sonidos y lugares"), ("sonido cotidiano", "sonido que oigo todos los días"), ("lugar", "dónde suena"), ("momento", "cuándo suena")],
    worked=[
        {"title": "Ubicar un sonido", "problem": "Por la mañana suena el agua del lavamanos: es fina y dura mientras te lavas. ¿Dónde y cuándo suena y cómo es?", "steps": ["Lugar: el baño. Momento: al despertar.", "Altura: agudo, porque es fino.", "Duración: largo, porque dura todo el lavado."], "answer": "En el baño, al despertar; agudo y largo"},
        {"title": "Describir un sonido de recreo", "problem": "En el patio suena un balón rebotando: golpes cortos, parejos y fuertes. Descríbelo.", "steps": ["Lugar: el patio. Momento: el recreo.", "Duración: corto cada golpe.", "Intensidad: fuerte; además es parejo, como un pulso."], "answer": "En el patio, en el recreo; corto, fuerte y parejo"},
    ],
    mistakes=[
        {"wrong": "Escribir solo una lista de sonidos sin decir dónde ni cuándo.", "why": "No se ubica el sonido.", "fix": "Agrega lugar y momento de cada sonido."},
        {"wrong": "Grabar a otras personas sin su permiso.", "why": "No se piensa en la privacidad.", "fix": "Escucha, anota con palabras y no grabes a nadie."},
    ],
    tiers={
        "recovery": [
            ex("Un mapa sonoro, ¿muestra sonidos o colores?", "Sonidos", "Es un mapa de lo que se oye."),
            ex("El despertador suena fuerte y corto. ¿Qué cualidad describe «fuerte»?", "La intensidad", "Habla de qué tan fuerte suena."),
            ex("¿Escribes el nombre de las personas en tu mapa sonoro?", "No", "Se evitan datos personales."),
        ],
        "understand": [
            ex("¿Qué dos datos agregas a cada sonido además de cómo suena?", "Dónde y cuándo suena", "Ubican el sonido."),
            ex("¿Por qué no se graba a otras personas sin permiso?", "Para respetar su privacidad", "Es un derecho de las personas."),
            ex("¿Todos los sonidos de la rutina son música?", "No, pero todos se pueden escuchar", "Hay sonidos y hay música."),
        ],
        "apply": [
            ex("La tetera pita fino y largo en la cocina por la mañana. Describe el sonido con altura y duración.", "Agudo y largo", "Fino es agudo y mucho tiempo es largo."),
            ex("La puerta del colegio se cierra con un golpe hondo y breve. ¿Cómo es su altura y su duración?", "Grave y corto", "Hondo es grave y breve es corto."),
            ex("Tu rutina tiene 7 momentos y en cada uno anotas 2 sonidos. ¿Cuántos sonidos anotas?", "14", "7 × 2 = 14."),
        ],
        "reason": [
            ex("Un niño anota «hay ruidos» en su mapa. ¿Qué le falta?", "Decir cuáles son, dónde y cuándo suenan", "No describe los sonidos."),
            ex("Dos niños tienen rutinas distintas. ¿Pueden tener mapas sonoros diferentes?", "Sí", "Cada rutina tiene sus propios sonidos."),
        ],
        "challenge": [
            ex("Completa tu mapa sonoro para 3 momentos: despertar, patio y dormir. Escribe un sonido para cada uno.", "Por ejemplo: despertador; balón; canción de cuna", "Cada sonido se ubica en un momento."),
            ex("Elige un sonido de tu noche y descríbelo con tres cualidades.", "Por ejemplo: el reloj, agudo, suave y corto", "Debe tener altura, intensidad y duración."),
        ],
    },
    context=[ex("Al volver a casa, escuchas la olla donde cocinan, el agua que hierve y a alguien que canta bajito. Anota un sonido y dónde está.", "Por ejemplo: el agua que hierve en la cocina", "Un sonido con su lugar.")],
    selfcheck=[ex("En Música, ¿qué es una rutina?", "Lo que hago cada día", "Son momentos de mi día."), ex("¿Qué se agrega a cada sonido en un mapa sonoro?", "Dónde y cuándo", "Ubica el sonido."), ex("¿Se escriben nombres personales?", "No", "Se protege la privacidad.")],
    open_task=task(
        "Completa este mapa sonoro con la rutina de ejemplo: despertar, desayunar, ir al colegio, jugar en el patio, volver a casa, bañarse y dormir. Para cada momento escribe un sonido que oigas en tu vida y descríbelo con una cualidad (fuerte o suave, largo o corto, agudo o grave). No escribas nombres de personas.",
        "Despertar: despertador, fuerte y corto. Desayunar: cuchara en la taza, agudo y corto. Colegio: timbre, fuerte y largo. Patio: balón, fuerte y corto. Casa: llaves, agudo y corto. Baño: agua, suave y largo. Dormir: silencio con un reloj, suave y corto.",
        ["completa los siete momentos", "describe cada sonido con una cualidad", "no escribe datos privados"],
        ["mapa sonoro", "explicación oral"],
        ["listar sonidos sin lugar ni cualidad", "incluir nombres de personas"],
        "Reconoce la variedad de sonidos y pide que explique una descripción; si falta una cualidad, que vuelva a escuchar ese momento.",
    ),
    reinforce="Escucha 1 minuto en silencio y anota tres sonidos de tu casa.",
    extend="Compara los sonidos de la mañana con los de la noche y cuenta cuáles son más suaves.",
)

register(
    OA7, 2,
    materials="Lápiz y papel. Cinco ocasiones escritas en la clase: cumpleaños, dormir, jugar en el patio, un acto del colegio y una fiesta del barrio. Música descrita por escrito para cada ocasión.",
    use="Aprenderé a relacionar una música con su ocasión y su función. Sirve para entender por qué usamos cierta música en ciertos momentos.",
    prior=["Sé nombrar celebraciones y rutinas.", "Sé describir una música como lenta, rápida, fuerte o suave."],
    explain=[
        "La música aparece en ocasiones: un cumpleaños, la hora de dormir, un acto, una fiesta. En cada una cumple una función, que es para qué sirve. Una canción de cumpleaños sirve para celebrar. Una canción de cuna sirve para tranquilizar. Una marcha sirve para caminar al mismo paso.",
        "La función se relaciona con cómo suena. Para dormir, la música suele ser lenta, suave y larga. Para jugar o bailar, suele ser rápida y con pulso claro. Para celebrar, suele ser alegre y cantada por muchos. Si cambias la ocasión, puede cambiar la música.",
        "Para describir una experiencia musical, di tres cosas: cuál era la ocasión, cómo sonaba y para qué servía. Por ejemplo: «En la hora de dormir, mi mamá canta una canción lenta y suave para que me tranquilice». Así cuentas más que si solo dices «me gusta».",
    ],
    vocab=[("ocasión", "momento especial o habitual en que hay música"), ("función", "para qué sirve la música"), ("celebrar", "festejar algo con alegría"), ("tranquilizar", "dar calma"), ("marcha", "música para caminar al mismo paso")],
    worked=[
        {"title": "Ocasión, sonido y función", "problem": "En la hora de dormir tu mamá canta una canción lenta y suave. Describe ocasión, sonido y función.", "steps": ["Ocasión: la hora de dormir.", "Sonido: lento y suave.", "Función: tranquilizar para que duerma."], "answer": "Hora de dormir; lenta y suave; sirve para tranquilizar"},
        {"title": "Elegir según la ocasión", "problem": "En una fiesta de curso quieren bailar. ¿Eliges una música lenta y suave o rápida y con pulso claro?", "steps": ["Bailar necesita movimiento.", "Un pulso claro ayuda a seguir el paso.", "Por eso elijo la rápida con pulso claro."], "answer": "Rápida y con pulso claro"},
    ],
    mistakes=[
        {"wrong": "Decir solo «me gusta» al describir una experiencia musical.", "why": "Una opinión no cuenta la ocasión ni la función.", "fix": "Cuenta la ocasión, cómo sonaba y para qué servía."},
        {"wrong": "Creer que una misma música sirve igual para todas las ocasiones.", "why": "No se considera la función.", "fix": "Piensa si la música calma, hace bailar o celebra."},
    ],
    tiers={
        "recovery": [
            ex("Una canción de cuna, ¿sirve para dormir o para bailar?", "Dormir", "Es lenta y suave para tranquilizar."),
            ex("Una canción de cumpleaños, ¿sirve para celebrar o para hacer silencio?", "Celebrar", "Se canta para festejar."),
            ex("Una marcha, ¿sirve para caminar al mismo paso o para dormir?", "Caminar al mismo paso", "Tiene un pulso muy claro."),
        ],
        "understand": [
            ex("¿Qué es la función de una música?", "Para qué sirve", "Explica su uso en la ocasión."),
            ex("¿Por qué la música para dormir suele ser suave?", "Porque debe tranquilizar", "Lo suave calma."),
            ex("¿Qué tres cosas dices al describir una experiencia musical?", "Ocasión, cómo sonaba y para qué servía", "Cuenta más que una opinión."),
        ],
        "apply": [
            ex("Un acto del colegio comienza con música de pulso muy marcado para entrar en fila. ¿Cuál es la función?", "Entrar caminando al mismo paso", "El pulso marcado organiza el paso."),
            ex("En una fiesta del barrio todos bailan en círculo. Describe la ocasión y la función.", "Fiesta del barrio; bailar y celebrar", "Se baila para celebrar."),
            ex("Tienes cinco ocasiones y una canción para cada una. ¿Cuántas canciones tienes?", "5", "Una por ocasión."),
        ],
        "reason": [
            ex("Un niño usa una música fuerte y rápida para dormir a su hermano. ¿Qué problema tiene?", "No cumple la función de tranquilizar", "Lo fuerte y rápido despierta."),
            ex("Si la ocasión cambia, ¿puede cambiar la música?", "Sí", "Cada ocasión pide una función distinta."),
        ],
        "challenge": [
            ex("Escribe una frase con ocasión, cómo sonaba y función para un cumpleaños.", "Por ejemplo: en un cumpleaños se canta una canción alegre y fuerte para celebrar", "Incluye las tres partes."),
            ex("Inventa una ocasión nueva con su música y su función.", "Por ejemplo: la hora de ordenar, con una canción rápida para animar", "Una ocasión con función clara."),
        ],
    },
    context=[ex("En tu casa se escucha una música tranquila mientras todos cenan en silencio. ¿Cuál puede ser su función?", "Crear un ambiente calmado", "Una música tranquila acompaña con calma.")],
    selfcheck=[ex("¿Qué función tiene una canción de cuna?", "Tranquilizar para dormir", "Es lenta y suave."), ex("¿Qué es una ocasión?", "Un momento en que hay música", "Por ejemplo un cumpleaños."), ex("En Música, ¿qué es la función?", "Para qué sirve la música", "Explica su uso.")],
    open_task=task(
        "Completa esta tabla de cinco ocasiones con una música y una función: cumpleaños, dormir, jugar en el patio, un acto del colegio, una fiesta del barrio. Escribe para cada una cómo suena (lenta o rápida, fuerte o suave) y para qué sirve.",
        "Cumpleaños: alegre y fuerte, para celebrar. Dormir: lenta y suave, para tranquilizar. Patio: rápida y con pulso claro, para jugar. Acto: con pulso marcado, para entrar en fila. Fiesta: rápida y cantada por muchos, para bailar.",
        ["completa las cinco ocasiones", "relaciona cómo suena con la función", "no usa solo me gusta"],
        ["tabla escrita", "explicación oral"],
        ["función sin relación con el sonido", "solo opinar"],
        "Reconoce las relaciones lógicas y pide que justifique una; si una función no coincide con el sonido, que la cambie.",
    ),
    reinforce="Escribe la ocasión y función de una canción que escuches hoy.",
    extend="Elige una ocasión y propone dos músicas distintas que podrían servir, explicando por qué.",
)

register(
    OA7, 3,
    materials="Lápiz y papel. Tres experiencias de ejemplo escritas en la clase para practicar cómo contar sin datos privados.",
    use="Aprenderé a describir una experiencia musical de mi vida sin contar datos privados. Sirve para compartir mis vivencias cuidando mi intimidad y la de otros.",
    prior=["Sé contar algo que me pasó.", "Sé que algunos datos son privados."],
    explain=[
        "Una memoria sonora es un recuerdo de un sonido o de una música. Puede ser la voz de una canción de cuna, el sonido de la lluvia en el techo o una fiesta. Al compartirla, conviene contar el sonido, no los datos privados.",
        "Los datos privados son cosas como nombres completos, direcciones, teléfonos, el nombre exacto de tu colegio o fotos y grabaciones de personas. No hay que compartirlos. En vez de decir «mi tía Pamela Núñez canta», puedes decir «una persona de mi familia canta».",
        "Para describir una memoria sonora sin datos privados, usa palabras generales: «mi casa», «el patio», «una persona de mi familia», «un amigo». Cuenta cómo sonaba, cuándo y qué sentiste. Así compartes tu experiencia y cuidas la privacidad de todos.",
    ],
    vocab=[("memoria sonora", "recuerdo de un sonido o una música"), ("dato privado", "información personal que no hay que compartir"), ("privacidad", "derecho a cuidar lo personal"), ("palabra general", "palabra que no dice nombres ni lugares exactos"), ("recuerdo", "algo que viví y recuerdo")],
    worked=[
        {"title": "Cambiar un dato privado", "problem": "Quieres contar: «Mi abuela Rosa Pérez canta en la calle Los Olmos 123». ¿Cómo lo cuentas cuidando los datos?", "steps": ["Quito el nombre completo y la dirección.", "Uso palabras generales.", "Queda: una persona de mi familia canta en su casa."], "answer": "Una persona de mi familia canta en su casa"},
        {"title": "Contar el sonido", "problem": "Recuerdas la lluvia sobre el techo de tu casa. ¿Cómo la describes?", "steps": ["Digo cuándo: en una noche de invierno.", "Digo cómo sonaba: suave, parejo y largo.", "Digo qué sentí: calma."], "answer": "En una noche de invierno, la lluvia sonaba suave, pareja y larga, y sentí calma"},
    ],
    mistakes=[
        {"wrong": "Decir el nombre completo y la dirección de alguien.", "why": "No se piensa en la privacidad.", "fix": "Usa «una persona de mi familia» y «mi casa»."},
        {"wrong": "Contar solo datos y no cómo sonaba.", "why": "Se pierde la experiencia sonora.", "fix": "Agrega cómo sonaba: fuerte o suave, largo o corto."},
    ],
    tiers={
        "recovery": [
            ex("Una dirección, ¿es un dato privado o general?", "Privado", "Dice dónde vive una persona."),
            ex("«Mi casa», ¿es una palabra general o un dato privado?", "General", "No dice una dirección exacta."),
            ex("¿Se cuenta el sonido o los datos privados?", "El sonido", "Eso es lo que importa en la memoria sonora."),
        ],
        "understand": [
            ex("¿Por qué no se comparten datos privados?", "Para cuidar la privacidad de las personas", "Es un derecho de todos."),
            ex("¿Qué palabra general puedes usar en vez del nombre de tu tía?", "Una persona de mi familia", "No nombra a la persona."),
            ex("¿Qué cuentas de la memoria sonora?", "Cómo sonaba, cuándo y qué sentí", "Son los datos de la experiencia."),
        ],
        "apply": [
            ex("Reescribe sin datos privados: «Mi amigo Tomás Rojos tocó guitarra en la plaza Italia».", "Un amigo tocó guitarra en una plaza", "Se quitan nombres y lugar exacto."),
            ex("Describe una lluvia que sonaba suave y larga con dos cualidades.", "Suave y larga", "Intensidad y duración."),
            ex("Entre «el teléfono de mi mamá» y «mi mamá canta», ¿cuál es un dato privado?", "El teléfono de mi mamá", "Un teléfono es información personal."),
        ],
        "reason": [
            ex("Un niño cuenta su memoria sonora con la dirección de su casa. ¿Qué le sugieres?", "Quitar la dirección y decir mi casa", "Evitar datos privados."),
            ex("¿Por qué conviene decir cómo sonaba en vez de solo qué pasó?", "Porque la experiencia es sonora", "Describir el sonido es el objetivo."),
        ],
        "challenge": [
            ex("Escribe una memoria sonora de 2 frases sin datos privados.", "Por ejemplo: En una noche de lluvia, el agua sonaba suave y larga. Sentí calma", "Cuenta el sonido y la emoción sin nombres."),
            ex("Identifica el dato privado: «Mi vecina Luisa Torres canta en el pasaje Las Rosas».", "Luisa Torres y el pasaje Las Rosas", "Son nombre completo y lugar."),
        ],
    },
    context=[ex("En clase te piden contar un recuerdo musical y quieres hablar del cumpleaños de tu primo con su nombre completo. ¿Qué haces?", "Digo mi primo y no uso su nombre completo", "Se cuida su privacidad.")],
    selfcheck=[ex("¿Qué es un dato privado?", "Información personal que no se comparte", "Por ejemplo una dirección."), ex("¿Qué usas en vez de un nombre?", "Una palabra general", "Por ejemplo una persona de mi familia."), ex("¿Qué es una memoria sonora?", "Un recuerdo de un sonido o música", "Se cuenta cómo sonaba.")],
    open_task=task(
        "Elige uno de estos tres recuerdos y cuéntalo sin datos privados, con 3 frases: (a) la lluvia sobre el techo de una casa; (b) una canción de cuna cantada por una persona de la familia; (c) música en una fiesta con muchas personas. Di cuándo era, cómo sonaba y qué sentiste.",
        "Elegí (a). Era una noche de invierno. La lluvia sonaba suave y larga sobre el techo. Sentí calma.",
        ["elige uno de los recuerdos", "dice cuándo, cómo sonaba y qué sintió", "no incluye datos privados"],
        ["texto escrito", "relato oral"],
        ["usar nombres completos o direcciones", "contar solo qué pasó sin el sonido"],
        "Reconoce el cuidado de la privacidad y pide que añada una cualidad del sonido; si hay datos privados, que los cambie por palabras generales.",
    ),
    reinforce="Cuenta un sonido favorito sin decir nombres ni lugares exactos.",
    extend="Compara dos memorias sonoras, una tranquila y una alegre, usando cualidades.",
)

register(
    OA7, 4,
    materials="Lápiz y papel. Formato de autobiografía musical en tres frases escrito en la clase. Opciones de experiencias escritas: cantar una canción de cuna, bailar en una fiesta, escuchar la lluvia, jugar con una caja como tambor.",
    use="Aprenderé a comunicar una relación personal con la música usando evidencia sonora. Sirve para presentar quién soy a través de mis experiencias musicales.",
    prior=["Sé contar una experiencia sin datos privados.", "Sé describir cualidades del sonido."],
    explain=[
        "Una autobiografía musical es una historia corta de mi vida con la música. No hace falta contar toda tu vida. Con tres frases es suficiente: qué experiencia musical viví, cómo sonaba y qué sentí o para qué servía.",
        "Para que sea clara, usa evidencia sonora: cualidades que se pueden oír. En vez de decir «era bonita», di «era lenta, suave y con un pulso parejo». La evidencia hace que otra persona imagine el sonido y entienda tu experiencia.",
        "Cuida la privacidad: sin nombres completos, direcciones ni teléfonos. Usa palabras generales como «mi casa» o «una persona de mi familia». Puedes agregar un dibujo de la experiencia. Al compartir, lee con calma y escucha con respeto las historias de los demás.",
    ],
    vocab=[("autobiografía", "historia de mi propia vida"), ("evidencia sonora", "cualidades que se pueden oír y respaldan lo que digo"), ("experiencia", "algo que viví"), ("comunicar", "contar para que otros entiendan"), ("relación personal", "lo que significa algo para mí")],
    worked=[
        {"title": "Armar tres frases", "problem": "Quieres contar que en tu casa se canta antes de dormir. ¿Cómo armas tres frases?", "steps": ["Frase 1: la experiencia (antes de dormir se canta en mi casa).", "Frase 2: cómo suena (lento, suave y con pulso parejo).", "Frase 3: qué siento (calma)."], "answer": "Antes de dormir se canta en mi casa. Suena lento, suave y con pulso parejo. Siento calma"},
        {"title": "Agregar evidencia sonora", "problem": "Una niña escribe «mi música favorita es bonita». ¿Cómo agregas evidencia?", "steps": ["«Bonita» no se puede oír.", "Pregunto cómo suena: ¿lenta?, ¿fuerte?", "Escribo: es lenta, suave y con un tambor grave."], "answer": "Es lenta, suave y con un tambor grave"},
    ],
    mistakes=[
        {"wrong": "Escribir solo gustos como «me gusta la música».", "why": "No cuenta dónde, cuándo ni para qué.", "fix": "Cuenta una experiencia y cómo sonaba."},
        {"wrong": "Incluir nombres y direcciones.", "why": "No se piensa en la privacidad.", "fix": "Usa palabras generales."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántas frases tiene tu autobiografía musical de la clase?", "3", "Experiencia, sonido y sentimiento."),
            ex("Evidencia sonora, ¿es algo que se puede oír o algo que se siente?", "Algo que se puede oír", "Por eso sirve de prueba."),
            ex("¿Cuál va primero: la experiencia o el sentimiento?", "La experiencia", "Se parte contando qué pasó."),
        ],
        "understand": [
            ex("¿Por qué «bonita» no es evidencia sonora?", "Porque no se puede oír", "No dice cómo suena."),
            ex("¿Qué dos palabras generales cuidan la privacidad?", "Mi casa y una persona de mi familia", "No dicen nombres ni direcciones."),
            ex("¿Para qué sirve agregar un dibujo?", "Para mostrar mi experiencia", "El dibujo ayuda a comunicar."),
        ],
        "apply": [
            ex("Reescribe con evidencia sonora: «mi canción favorita es linda».", "Mi canción favorita es lenta y suave", "Se cambian palabras de gusto por cualidades."),
            ex("Escribe una frase de sentimiento para una canción de cuna.", "Siento calma", "Es lo que produce la canción."),
            ex("Escoge una experiencia de la lista de materiales y escribe una frase que la describa.", "Por ejemplo: bailo en una fiesta con música rápida", "Es una de las experiencias dadas."),
        ],
        "reason": [
            ex("Un niño escribe «mi música es buena». ¿Qué falta?", "Cómo suena y en qué ocasión", "No hay evidencia ni experiencia."),
            ex("¿Por qué es mejor contar cómo suena que decir solo «me gusta»?", "Porque otros pueden imaginarlo", "La evidencia hace comprensible el relato."),
        ],
        "challenge": [
            ex("Escribe tu autobiografía musical en tres frases: experiencia, sonido y sentimiento.", "Por ejemplo: Canto con mi familia. Suena parejo y suave. Me siento contento", "Tiene las tres partes y no tiene datos privados."),
            ex("Cambia esta frase para proteger la privacidad: «mi hermano Pedro Soto toca tambor en el pasaje Los Pinos».", "Mi hermano toca tambor en mi casa", "Se quitan nombre completo y dirección."),
        ],
    },
    context=[ex("En el curso, cada niño leerá su autobiografía musical. Tú quieres decir que a veces bailas con tu familia con música rápida. ¿Cómo lo dices?", "Bailo con mi familia con música rápida y siento alegría", "Incluye experiencia, sonido y sentimiento.")],
    selfcheck=[ex("¿Qué es una autobiografía?", "La historia de mi propia vida", "Se cuenta en primera persona."), ex("¿Qué es evidencia sonora?", "Lo que se puede oír", "Prueba cómo suena."), ex("¿Qué cuidamos al contar?", "La privacidad", "Sin nombres ni direcciones.")],
    open_task=task(
        "Escribe tu autobiografía musical en tres frases usando una de las experiencias de la lista: cantar una canción de cuna, bailar en una fiesta, escuchar la lluvia, jugar con una caja como tambor. Frase 1: qué experiencia; frase 2: cómo sonaba (una cualidad); frase 3: qué sentiste. Puedes agregar un dibujo. No uses nombres ni direcciones.",
        "Juego con una caja como tambor. Suena fuerte y con un pulso parejo. Me siento contento.",
        ["incluye experiencia, sonido y sentimiento", "usa una cualidad sonora como evidencia", "no incluye datos privados"],
        ["texto de tres frases", "dibujo", "lectura oral"],
        ["escribir solo gustos", "incluir nombres o direcciones"],
        "Reconoce la experiencia y pregunta qué cualidad la respalda; si hay datos privados, que los cambie por palabras generales.",
    ),
    reinforce="Completa la frase: «Mi música favorita suena ___ y me hace sentir ___».",
    extend="Agrega una cuarta frase con lo que te gustaría escuchar o tocar en el futuro.",
)
