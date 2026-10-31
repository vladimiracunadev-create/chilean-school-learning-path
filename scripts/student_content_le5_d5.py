"""Cuaderno del estudiante, 5.º básico Lenguaje y Comunicación: OA 30 (clases 3 a 6)."""
from __future__ import annotations

from student_content_le5_d import E, reg
from student_lessons import arith

OA30 = "LE05 OA 30"

# ================================================================ OA 30 · clase 3
reg(
    OA30, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar tu forma de decir el poema.",
    "Aprenderé a localizar y seleccionar los recursos de un poema (rima, repetición, pausas) y los datos clave de una noticia (qué, quién, cuándo, dónde y por qué). Sirve para preparar un texto oral con evidencia del propio texto.",
    ["Sé reconocer distintos tipos de texto oral.", "Sé planificar una narración."],
    [
        "Para planificar un texto oral, primero lo leemos con atención y seleccionamos lo importante. En un poema buscamos los recursos expresivos. La rima ocurre cuando las palabras finales de dos versos suenan parecido. La repetición es decir la misma palabra varias veces. Las pausas son silencios breves al final de un verso o donde hay una coma. Estos recursos indican cómo decirlo.",
        "Poema de ejemplo: «Llueve sobre el techo, / llueve sobre el patio, / llueve y en mi ventana / baila un charco despacio». Aquí «patio» y «despacio» riman, y «llueve» se repite al comienzo de tres versos. Al decirlo, podemos dar énfasis a «llueve» y hacer una pausa breve en cada coma.",
        "En una noticia seleccionamos datos que responden cinco preguntas: qué ocurrió, quién participó, cuándo, dónde y por qué. Noticia de ejemplo: «Ayer por la tarde, en el gimnasio de la escuela Los Aromos, el cuarto básico ganó el torneo de ajedrez escolar. Participaron 12 estudiantes. Ganaron porque ensayaron todos los viernes». Cada dato se puede señalar con una frase exacta del texto, y las opiniones se dejan fuera.",
    ],
    [("rima", "sonido parecido al final de dos versos"), ("repetición", "decir la misma palabra varias veces"), ("verso", "cada línea de un poema"), ("pausa", "silencio breve al hablar"), ("dato clave", "información central, como quién o cuándo")],
    [
        ("Localizar la rima", "Poema «Llueve»: «Llueve sobre el techo, / llueve sobre el patio, / llueve y en mi ventana / baila un charco despacio». ¿Qué palabras riman?", ["Miro las palabras finales de cada verso.", "Los versos 2 y 4 terminan en «patio» y «despacio».", "Suenan parecido."], "«Patio» y «despacio»."),
        ("Seleccionar datos", "En la noticia del torneo de ajedrez, ¿qué frase responde «cuándo» ocurrió?", ["Busco la expresión de tiempo.", "Aparece al inicio.", "Es «Ayer por la tarde»."], "«Ayer por la tarde»."),
    ],
    [("Decir el poema como si fuera prosa, sin respetar la rima ni las pausas.", "No se localizaron los recursos.", "Marca la rima, la repetición y las pausas antes de ensayar."), ("Incluir opiniones en una noticia.", "Se mezcla lo que pasó con lo que pensamos.", "Selecciona solo los datos que responden qué, quién, cuándo, dónde y por qué.")],
    [
        E("En el poema «Llueve», ¿cuántas veces se repite «llueve» al comienzo de los versos?", "Tres", "Aparece en los versos 1, 2 y 3."),
        E("En la noticia, ¿quién ganó el torneo?", "El cuarto básico", "Lo dice la primera oración."),
        E("¿Dónde ocurrió la noticia?", "En el gimnasio de la escuela Los Aromos", "Es el dato de lugar."),
    ],
    [
        E("¿Qué recurso es repetir «llueve» al comienzo de los versos: la repetición o la rima?", "La repetición", "Se vuelve a decir la misma palabra."),
        E("La frase «Ganaron porque ensayaron todos los viernes», ¿responde cuándo o por qué?", "Por qué", "Explica la causa."),
        E("En un poema, ¿dónde conviene hacer una pausa breve: a) donde hay una coma o el verso termina b) en medio de cada palabra?", "a", "Las pausas marcan el ritmo."),
    ],
    [
        arith("En el torneo participaron 12 estudiantes. Si 5 eran de cuarto básico, ¿cuántos eran de otros cursos?", "12-5", "Se restan los de cuarto al total.", " estudiantes"),
        E("¿Cuál oración no es un dato de la noticia: a) «Participaron 12 estudiantes.» b) «El ajedrez es el mejor juego del mundo.»", "b", "Es una opinión y no un hecho de la noticia."),
        E("Para decir el poema con ritmo, ¿qué conviene hacer con la palabra «llueve»: a) decirla con más fuerza b) hablar todo en un solo tono?", "a", "El énfasis destaca la repetición."),
    ],
    [
        E("Dos formas de dar la noticia: A) «Ganaron.» B) «Ayer, el cuarto básico ganó el torneo de ajedrez en el gimnasio.» ¿Cuál incluye más datos clave?", "B", "Dice cuándo, quién, qué y dónde."),
        E("Un niño dice que el poema habla de la lluvia. ¿Qué verso lo muestra: a) «Llueve sobre el techo» b) «baila un charco despacio»?", "a", "Nombra la lluvia directamente."),
    ],
    [
        E("Quieres convertir la noticia en el testimonio de un participante. ¿Qué cambias: a) hablar en primera persona («Participé en el torneo…») b) quitar todos los datos?", "a", "El testimonio relata lo vivido en primera persona."),
        E("¿Qué recurso del poema ayuda a que «patio» y «despacio» se noten al decirlos: la rima o el chiste?", "La rima", "El sonido parecido da musicalidad."),
    ],
    [E("Debes dar la noticia del torneo en el acto, con solo 20 segundos. ¿Qué datos eliges primero: a) qué ocurrió, quién, cuándo y dónde b) todos los detalles del almuerzo?", "a", "Son los datos clave de una noticia.")],
    [
        E("¿La rima ocurre cuando dos versos terminan con sonidos parecidos? Responde sí o no.", "Sí", "Esa es su definición."),
        E("Una noticia responde qué, quién, cuándo, dónde y por qué. Responde sí o no.", "Sí", "Son los datos clave."),
        E("¿Se deben incluir opiniones personales en una noticia? Responde sí o no.", "No", "La noticia informa hechos."),
    ],
    ("Elige A o B. A) Copia el poema «Llueve» en tu cuaderno, subraya la rima, marca con / las pausas y con ■ la palabra que dirás con más fuerza; luego dilo en voz alta. B) Con estos datos arma una noticia de dos o tres oraciones: lo que ocurrió: la escuela hizo una colecta de ropa; quién: el quinto básico; cuándo: el lunes; dónde: en el patio; por qué: para ayudar a familias del barrio. Marca en tu texto la frase de cada dato.",
     "A) «Llueve / sobre el techo, / llueve / sobre el patio…» con rima en patio y despacio y énfasis en «llueve». B) «El lunes, en el patio de la escuela, el quinto básico hizo una colecta de ropa. Lo hicieron para ayudar a familias del barrio».",
     ["ubica rima, repetición o datos clave", "respeta pausas o responde las cinco preguntas", "lo dice o lo escribe con claridad"], ["texto marcado", "versión oral"], ["mezclar opiniones en la noticia", "decir el poema sin pausas"],
     "Si algo no se ve en tu texto, vuelve a leer y subraya la palabra o frase exacta que respalda lo que marcaste."),
    "Escribe dos versos propios con rima y marca las pausas.",
    "Escucha una noticia breve y anota el qué, el quién y el cuándo.",
)

# ================================================================ OA 30 · clase 4
reg(
    OA30, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar dos formas de decir el mismo texto.",
    "Aprenderé a comparar distintas formas de decir un mismo texto oral y a decidir cuál calza mejor con el sentido, la audiencia y el propósito. Sirve para tomar decisiones expresivas fundamentadas.",
    ["Sé localizar rima, repetición y pausas.", "Sé planificar una narración y una noticia."],
    [
        "Un mismo texto puede decirse de distintas formas. Al interpretarlo podemos cambiar la velocidad, el volumen, las pausas, el énfasis y el tono. Por ejemplo, «El río corre cantando, / baja de la montaña…» suena bien con voz alegre y ágil, porque «corre cantando» habla de movimiento y alegría. Decirlo muy lento y con voz triste no calzaría con el sentido.",
        "Para decidir, comparamos versiones y nos preguntamos: ¿qué dice el texto?, ¿qué siente o muestra?, ¿a quién le hablo? y ¿qué quiero lograr? Si el verso dice «baila un charco despacio», la palabra «despacio» se dice más lenta. Si cuento la historia de Julia cuando pierde el paraguas, bajo la voz y hablo más lento para mostrar tristeza.",
        "También comparamos tipos de texto. Una noticia informa en tercera persona: «El cuarto básico ganó el torneo». Un testimonio relata en primera persona lo vivido: «Yo jugué en el torneo y me sentí nervioso». Una descripción de actividad es más fácil de seguir si usa marcadores de orden como «primero», «luego» y «por último». No hay una única forma correcta, pero toda decisión debe poder explicarse con el texto.",
    ],
    [("interpretar", "decidir cómo decir un texto según su sentido"), ("tono", "manera de la voz que muestra un sentimiento"), ("ritmo", "velocidad y pausas con que se dice un texto"), ("audiencia", "personas que escuchan"), ("justificar", "explicar una decisión con razones")],
    [
        ("Comparar interpretaciones", "Verso: «El río corre cantando». Versión A: voz alegre y ágil. Versión B: voz triste y muy lenta. ¿Cuál calza mejor y por qué?", ["Busco qué dice el verso: corre y canta.", "Eso es movimiento y alegría.", "La versión A lo muestra."], "La A, porque «corre cantando» expresa movimiento y alegría."),
        ("Comparar textos", "Versión 1: «El cuarto básico ganó el torneo». Versión 2: «Yo jugué en el torneo y me sentí nervioso». ¿Cuál es testimonio?", ["Miro la persona gramatical.", "La versión 2 usa «yo».", "Relata lo vivido."], "La versión 2."),
    ],
    [("Creer que hay una sola forma correcta de decir un poema.", "Se piensa que existe una voz obligatoria.", "Elige una forma y justifícala con lo que dice el texto."), ("Elegir un tono que no calza con el sentido.", "No se leyó lo que expresa.", "Lee primero qué siente o muestra el texto.")],
    [
        E("Para «El río corre cantando», ¿qué voz conviene: alegre y ágil o triste y lenta?", "Alegre y ágil", "El verso habla de movimiento y canto."),
        E("En «baila un charco despacio», ¿cómo dices «despacio»: más lento o más rápido?", "Más lento", "La palabra expresa lentitud."),
        E("Descripción del poroto: A) «Primero se humedece algodón; luego se pone el poroto; por último se riega.» B) «Regar. Poroto. Algodón.» ¿Cuál se sigue mejor?", "A", "Los marcadores indican el orden."),
    ],
    [
        E("Al interpretar un poema, ¿qué puedes cambiar sin cambiar las palabras: a) la velocidad y las pausas b) los versos?", "a", "Cambian la manera de decirlo, no el texto."),
        E("¿Cuál es testimonio: a) «Yo jugué en el torneo y me sentí nervioso.» b) «El cuarto básico ganó el torneo.»", "a", "Relata lo vivido en primera persona."),
        E("¿Qué volumen calza con un verso suave como «baila un charco despacio»: a) suave b) muy fuerte?", "a", "El verso expresa calma."),
    ],
    [
        E("Ordena los pasos para decidir cómo interpretar. a) probar dos formas b) leer el texto y pensar qué muestra c) elegir la que mejor calza d) justificar la elección. Escribe las letras.", "b, a, c, d", "Primero se comprende, luego se compara y se decide."),
        arith("Una narración dura 120 segundos en versión lenta y 90 en versión rápida. ¿Cuántos segundos más dura la lenta?", "120-90", "Se restan los tiempos.", " segundos"),
        E("Al contar que Julia pierde el paraguas, para mostrar tristeza, ¿cómo cambias la voz: más baja y lenta o más fuerte y rápida?", "Más baja y lenta", "Ese cambio transmite tristeza."),
    ],
    [
        E("Ema dice que hay una sola forma correcta de decir un poema. Leo dice que hay varias si calzan con el sentido. ¿Quién tiene razón?", "Leo", "Varias interpretaciones pueden ser válidas si se justifican."),
        E("Una niña dice «El río corre cantando» con voz muy triste y lenta. ¿Qué falla en su decisión: a) el tono no calza con el sentido b) lo dice en voz alta?", "a", "El verso expresa alegría y movimiento."),
    ],
    [
        E("Compara dos formas de decir «lleva en su espalda de agua / el sol de la mañana»: A) dos pausas largas en medio de cada verso; B) pausa breve al final de cada verso. ¿Cuál respeta mejor la idea completa?", "B", "No corta la frase en el medio."),
        E("La audiencia son niños de primero. ¿Qué narración conviene: a) voz expresiva, frases cortas y gestos b) voz plana y frases largas?", "a", "Se adapta a la audiencia."),
    ],
    [E("Vas a decir el poema del río en el acto. ¿Cuál opción eliges: a) leer apurado mirando la hoja b) decirlo con ritmo, mirando al público y con pausas al final de los versos?", "b", "Respeta el texto y se conecta con la audiencia.")],
    [
        E("¿Un texto puede decirse de varias formas? Responde sí o no.", "Sí", "Pueden cambiar velocidad, volumen y tono."),
        E("¿Una decisión de interpretación se justifica con el sentido del texto? Responde sí o no.", "Sí", "Debe apoyarse en lo que dice."),
        E("¿Un testimonio habla en primera persona? Responde sí o no.", "Sí", "Relata lo que se vivió."),
    ],
    ("Elige el verso «baila un charco despacio», el inicio de la narración «Una mañana de lluvia, Julia subió al bus» o los pasos «Primero se humedece algodón; luego se coloca el poroto; por último se riega». Prueba dos interpretaciones distintas (por ejemplo, rápida y alegre; lenta y suave), dilo en voz alta ante una persona de tu casa y escribe tres líneas: 1) qué cambiaste (velocidad, tono, pausas), 2) cuál prefieres, 3) por qué, con una razón basada en el texto.",
     "Verso: «baila un charco despacio». Cambié la velocidad: A) rápida, B) lenta y suave. Prefiero B porque «despacio» pide lentitud y el verso habla de un charco que baila suavemente.",
     ["prueba dos interpretaciones distintas", "describe qué cambió", "justifica con el texto"], ["tres líneas escritas", "dos versiones dichas"], ["no justificar", "elegir un tono que no calza con el texto"],
     "Si tu razón no usa el texto, busca la palabra o frase que respalda tu decisión."),
    "Escribe dos versiones de una misma frase de narración: una para niños pequeños y otra para tu profesor.",
    "Escucha una noticia y un testimonio sobre un mismo tema y anota dos diferencias.",
)

# ================================================================ OA 30 · clase 5
reg(
    OA30, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: dos o tres personas de tu casa para repartir los personajes y probar la escena.",
    "Aprenderé a planificar y producir una dramatización: escribir un guion con diálogos y acotaciones, repartir personajes y representar con voz y cuerpo. Sirve para expresar una historia de manera creativa y segura.",
    ["Sé reconocer distintos tipos de texto oral.", "Sé interpretar un texto con la voz."],
    [
        "Una dramatización es la representación de una escena por personajes que hablan y se mueven. Se prepara con un guion, que es el texto con lo que dice cada personaje. En el guion, cada línea indica quién habla. Las acotaciones, escritas entre paréntesis, indican cómo decir algo o qué hacer: (llega corriendo), (aliviada), (negando con la cabeza). Las acotaciones no se dicen en voz alta; se interpretan.",
        "Escena de ejemplo. JULIA: (llega corriendo, preocupada) ¿Han visto mi paraguas amarillo? MATÍAS: (negando con la cabeza) No lo he visto. ¿Lo dejaste en el bus? JULIA: (se lleva las manos a la cara) ¡Sí! Lo olvidé en el asiento. CONDUCTOR: (entra sonriendo) Aquí está, lo guardé para ti. JULIA: (aliviada) ¡Muchas gracias! Esta escena tiene tres personajes y cinco intervenciones.",
        "Para planificar, seguimos pasos: elegir la escena, escribir el guion con acotaciones, repartir personajes y ensayar. Para convertir una narración en diálogo, pasamos lo que los personajes dicen a su propia voz. Y siempre cuidamos la seguridad: usamos objetos simples e inofensivos, sin fuego, sin objetos cortantes y sin movimientos peligrosos.",
    ],
    [("dramatización", "representación de una escena con voz y cuerpo"), ("guion", "texto con lo que dice cada personaje"), ("acotación", "indicación entre paréntesis sobre cómo decir o hacer algo"), ("intervención", "cada vez que un personaje habla"), ("personaje", "quien actúa o habla en la escena")],
    [
        ("Reconocer una acotación", "En «JULIA: (llega corriendo, preocupada) ¿Han visto mi paraguas amarillo?», ¿qué es «llega corriendo, preocupada»?", ["Está entre paréntesis.", "No lo dice el personaje; indica cómo actuar.", "Es una acotación."], "Una acotación."),
        ("Convertir narración en diálogo", "Narración: «Julia preguntó si habían visto su paraguas». ¿Cómo queda como guion?", ["Paso lo que dice Julia a su propia voz.", "Pongo el nombre del personaje.", "JULIA: ¿Han visto mi paraguas?"], "JULIA: ¿Han visto mi paraguas?"),
    ],
    [("Leer las acotaciones en voz alta como parte del diálogo.", "Se confunden con lo que dice el personaje.", "Interprétalas con la voz y el cuerpo."), ("Incluir objetos peligrosos para que la escena se vea real.", "Se piensa que así luce mejor.", "Usa objetos simples y seguros; sin fuego ni cosas cortantes.")],
    [
        E("¿Cuántos personajes hay en la escena del paraguas?", "Tres", "Son Julia, Matías y el conductor."),
        E("¿Qué dice el conductor en la escena?", "Aquí está, lo guardé para ti", "Es su única intervención."),
        E("¿Qué indica «(negando con la cabeza)»: un gesto o una frase que se dice en voz alta?", "Un gesto", "Las acotaciones se interpretan."),
    ],
    [
        E("Las acotaciones sirven para: a) indicar cómo decir y qué hacer b) agregar chistes al final?", "a", "Orientan la interpretación."),
        E("¿Quién tiene más intervenciones en la escena: Julia, Matías o el conductor?", "Julia", "Habla tres veces."),
        E("¿Cuál acotación indica un gesto: a) «(se lleva las manos a la cara)» b) «Aquí está»?", "a", "Describe un movimiento."),
    ],
    [
        arith("La escena tiene 5 intervenciones y cada una dura 8 segundos. ¿Cuánto dura la escena?", "5*8", "Se multiplican las intervenciones por su duración.", " segundos"),
        E("Cambia a guion: «Matías respondió que no lo había visto». ¿Cuál queda mejor: a) MATÍAS: No lo he visto. b) Matías respondió que no lo había visto.", "a", "El guion pone la voz del personaje."),
        E("Ordena la escena. a) El conductor entra y devuelve el paraguas. b) Julia pregunta por su paraguas. c) Matías le responde. d) Julia agradece. Escribe las letras.", "b, c, a, d", "Es el orden del guion."),
    ],
    [
        E("Un compañero propone usar una vela encendida como parte de la escena. ¿Es adecuado? Responde sí o no.", "No", "El fuego es peligroso y no debe usarse."),
        E("Julia dice «¡Sí! Lo olvidé en el asiento» con voz tranquila y sonriendo, aunque el guion dice que está preocupada y se lleva las manos a la cara. ¿Hay coherencia entre voz, gesto y guion? Responde sí o no.", "No", "El guion indica preocupación, no calma."),
    ],
    [
        E("En el guion, el conductor entra sonriendo. ¿Cómo debe sonar su voz: amable y alegre o enojada?", "Amable y alegre", "La acotación muestra una actitud positiva."),
        E("Si se agrega a la profesora como cuarto personaje, ¿cuántos personajes hay en la escena?", "Cuatro", "Son Julia, Matías, el conductor y la profesora."),
    ],
    [E("Planificas una dramatización de un minuto con tres compañeros. Ordena los pasos. a) ensayar b) repartir personajes c) escribir el guion con acotaciones d) elegir la escena. Escribe las letras.", "d, c, b, a", "Primero se decide la escena y se escribe; luego se reparte y se ensaya.")],
    [
        E("¿Un guion indica quién habla? Responde sí o no.", "Sí", "Cada línea nombra al personaje."),
        E("¿Las acotaciones se dicen en voz alta? Responde sí o no.", "No", "Se interpretan con voz y cuerpo."),
        E("¿Se pueden usar objetos peligrosos en una dramatización? Responde sí o no.", "No", "Siempre se usan objetos seguros."),
    ],
    ("Escribe el guion de una escena de 1 minuto con dos personajes, a partir de esta narración: «Lía buscaba un libro de dinosaurios en la biblioteca, pero no lo encontraba. Un bibliotecario la ayudó a buscarlo y por fin lo hallaron». Incluye al menos cuatro intervenciones y tres acotaciones, sin objetos peligrosos. Si puedes, represéntala con una o dos personas de tu casa.",
     "LÍA: (mirando los estantes) No encuentro el libro. BIBLIOTECARIO: (sonriendo) Busquemos juntos en el estante azul. LÍA: (señalando) ¡Aquí está! BIBLIOTECARIO: (asintiendo) Qué bueno que lo hallamos.",
     ["escribe al menos cuatro intervenciones", "incluye tres acotaciones", "es seguro y coherente"], ["guion escrito", "representación"], ["leer las acotaciones en voz alta", "incluir objetos peligrosos"],
     "Si las acotaciones no se notan, usa gestos y tono de voz al interpretarlas."),
    "Convierte esta frase en diálogo: «Pía le dijo a su amigo que tenía hambre».",
    "Mira una escena de una obra o programa familiar y anota dos acotaciones que podrías escribir para ella.",
)

# ================================================================ OA 30 · clase 6
reg(
    OA30, 6,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para dar retroalimentación sobre tu texto oral.",
    "Aprenderé a revisar un texto oral con una pauta, a dar y recibir retroalimentación y a mejorar mi versión. Sirve para que mis poemas, narraciones, noticias, testimonios y dramatizaciones sean más claros y expresivos.",
    ["Sé reconocer y planificar textos orales.", "Sé decidir cómo interpretarlos."],
    [
        "Revisar un texto oral es compararlo con una pauta de criterios. Una pauta puede preguntar: ¿hay un esquema claro, con inicio, problema y final?, ¿el orden es comprensible?, ¿la voz tiene volumen, ritmo y énfasis?, ¿se evitan las muletillas como «eh»?, ¿hay detalles que ayuden a imaginar?, ¿el cierre es claro? Cada respuesta se apoya en algo que se escuchó.",
        "Ejemplo de relato para revisar: «Yo fui al parque y, eh, jugué, y después, eh, me fui. Fue lindo». Cumple el orden, pero tiene dos muletillas «eh», no dice con quién fue ni a qué jugó y su cierre no explica nada. Una retroalimentación útil sería: «Tu relato tiene un orden claro. Evita ‘eh’ haciendo una pausa breve y agrega con quién fuiste y por qué fue lindo».",
        "La retroalimentación debe ser amable y específica: un logro, algo que mejorar y un cambio posible. Después de recibirla, hacemos una segunda versión y la ensayamos. Conviene mejorar un criterio a la vez y comprobar que el cambio se nota. Así vemos el progreso y aprendemos a decidir cómo comunicar mejor.",
    ],
    [("pauta", "lista de criterios para revisar"), ("muletilla", "palabra repetida sin necesidad, como «eh»"), ("retroalimentación", "comentario que ayuda a mejorar"), ("versión", "forma en que se presenta un texto"), ("detalle", "dato que ayuda a imaginar mejor")],
    [
        ("Revisar con la pauta", "Relato: «Yo fui al parque y, eh, jugué, y después, eh, me fui. Fue lindo». ¿Cuántas muletillas «eh» tiene?", ["Leo el relato con atención.", "Aparece «eh» después de «y,» dos veces.", "Cuento: dos."], "Dos."),
        ("Mejorar una parte", "¿Cuál cierre es mejor: a) «Fue lindo porque jugué a las escondidas con mis amigos y reímos mucho.» b) «Fue lindo.»?", ["Busco el que da razones y detalles.", "La a dice con quién y qué hizo.", "La b no explica nada."], "La a."),
    ],
    [("Cambiar todo el texto por una crítica.", "Se quiere arreglar demasiado a la vez.", "Mejora un criterio a la vez y comprueba el cambio."), ("Dar retroalimentación diciendo «hablaste feo».", "No se piensa en cómo ayudar.", "Di un logro, algo que mejorar y un cambio posible.")],
    [
        E("¿Dice el relato del parque con quién fue la persona? Responde sí o no.", "No", "No lo menciona."),
        E("¿Qué criterio revisa si la voz tiene ritmo y énfasis: la expresividad o el título?", "La expresividad", "Evalúa cómo se usa la voz."),
        E("¿Qué comentario ayuda más: a) «Hablaste feo.» b) «Tu relato tiene orden. Haz una pausa en vez de decir ‘eh’.»", "b", "Dice un logro y un cambio."),
    ],
    [
        E("En «Yo fui al parque y, eh, jugué, y después, eh, me fui», ¿cuántas veces aparece la palabra «y»?", "Dos", "Aparece después de «parque» y antes de «después»."),
        E("¿Qué mejora agregar detalles como «jugué a las escondidas con mis amigos»: a) ayuda a imaginar la historia b) alarga la espera?", "a", "Los detalles hacen el relato más claro."),
        E("¿Qué se debe evitar para mejorar la fluidez: las pausas breves o las muletillas?", "Las muletillas", "Se reemplazan por pausas."),
    ],
    [
        E("Ordena el proceso de mejora. a) ensayar la versión mejorada b) revisar con la pauta c) decir la primera versión d) recibir retroalimentación. Escribe las letras.", "c, b, d, a", "Primero se dice, luego se revisa, se recibe retroalimentación y se ensaya."),
        arith("La pauta de esta clase tiene 6 criterios y el relato del parque cumple solo 1 (el orden). ¿Cuántos criterios quedan por mejorar?", "6-1", "Se restan los criterios cumplidos al total.", " criterios"),
        E("¿Cuál mensaje es una retroalimentación completa: a) «Tu inicio fue claro. Cambia los ‘eh’ por silencios cortos y agrega con quién fuiste.» b) «Mejórelo.»", "a", "Tiene un logro y cambios concretos."),
    ],
    [
        E("Un compañero cambia todo su texto después de una crítica y ya no se parece al original. ¿Qué convendría hacer: a) mejorar un criterio a la vez b) cambiar todo cada vez?", "a", "Así se ve el progreso y se conserva lo bueno."),
        E("Dos cierres: «Y bueno, eso.» y «Fue un día especial porque aprendí a compartir. Gracias por escucharme». ¿Cuál cierra mejor y por qué?", "El segundo, porque resume y agradece", "El primero no cierra la idea."),
    ],
    [
        arith("Valeria grabó su relato y duró 120 segundos. El tiempo asignado era de 90 segundos. ¿Cuántos segundos se pasó?", "120-90", "Se resta el tiempo asignado al tiempo usado.", " segundos"),
        E("Pablo tenía cuatro «eh» en su primera versión y uno en la segunda. ¿Mejoró en el criterio de las muletillas? Responde sí o no.", "Sí", "Disminuyó la cantidad."),
    ],
    [E("Presentas el poema del río y un compañero dice: «Se oyó muy bajo». ¿Qué cambio propones: a) subir un poco el volumen y mirar al público b) hablar más rápido?", "a", "El problema era de volumen.")],
    [
        E("¿La retroalimentación debe incluir un cambio posible? Responde sí o no.", "Sí", "Así sirve para mejorar."),
        E("¿Conviene mejorar un criterio a la vez? Responde sí o no.", "Sí", "Permite comprobar el cambio."),
        E("¿Una muletilla ayuda a la fluidez? Responde sí o no.", "No", "Interrumpe el texto."),
    ],
    ("Elige uno de tus textos orales de esta unidad (poema, narración, noticia, testimonio o dramatización). Dilo ante una persona de tu casa. Luego haz tres cosas: 1) revisa con la pauta y anota dos criterios que cumpliste y dos que debes mejorar, con una frase que lo muestre; 2) pide o escribe una retroalimentación con un logro, algo que mejorar y un cambio; 3) prepara una segunda versión cambiando un criterio y dila otra vez.",
     "1) Cumplí orden y volumen. Debo mejorar muletillas («eh» dos veces) y detalles. 2) «Tu relato tiene orden. Cambia ‘eh’ por pausas y agrega con quién fuiste». 3) Nueva versión: «Fui al parque con mis amigos. Jugamos a las escondidas y reímos mucho. Fue un día especial».",
     ["revisa con la pauta usando evidencia", "la retroalimentación tiene logro, mejora y cambio", "la segunda versión mejora un criterio"], ["pauta completada", "retroalimentación", "segunda versión"], ["revisar sin ejemplos", "cambiarlo todo"],
     "Si no notas diferencia entre versiones, elige un solo criterio y cámbialo de forma visible."),
    "Escribe una pauta de cinco criterios para revisar un texto oral propio.",
    "Pide a una persona de tu casa que te escuche y anota un logro y una mejora.",
)
