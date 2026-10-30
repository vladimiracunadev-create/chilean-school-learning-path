"""Cuaderno del estudiante, 2.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF05 (uso de recursos digitales para escuchar, ver y transcribir lengua indígena) y
OA LR01 (relatos y palabras significativas, contexto de revitalización).

Los guiones, fichas y relatos de práctica están en castellano, son inventados y no pertenecen a
ningún pueblo. Las únicas palabras de mapuzugun son «mari mari», «mapu», «ko», «antü» y «kuyen».
Las palabras del castellano de Chile de origen quechua (papa, palta, choclo, guagua, cóndor) y
mapuche (copihue, quiltro) se mencionan como préstamos ampliamente atestiguados. La escritura, la
pronunciación y el uso de cualquier palabra indígena los confirma el educador/a tradicional.
"""
from __future__ import annotations

from student_lessons import arith, ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


LF05 = "LC02 OA LF05"
LR01 = "LC02 OA LR01"

GUION = ("Audio de práctica (lo lee un adulto): «Mari mari. Hoy les cuento sobre el río de mi pueblo. "
         "Es ancho y tranquilo. Los niños llegan en la tarde a mirar los patos.»")

# ================================================================ LF05
register(
    LF05, 1,
    materials="Este cuaderno y lápiz. No necesitas internet: el audio de práctica lo lee un adulto con el guion escrito aquí. Si usas un aparato, hazlo con un adulto.",
    use="Aprenderé a elegir un recurso digital de audio o video que sea seguro y autorizado. Sirve para escuchar y ver la lengua de un pueblo sin faltarle el respeto a su comunidad.",
    prior=["Sé qué es una fuente.", "Sé que debo pedir permiso."],
    explain=[
        "Un recurso digital es un audio, un video o una imagen que se escucha o se ve con un aparato, como un computador o un teléfono. Hay recursos hechos por comunidades y por instituciones con permiso de ellas. También hay otros sin autor ni permiso. No todos sirven para aprender.",
        "Un recurso autorizado cumple cuatro cosas: dice quién habla o quién lo hizo, dice a qué comunidad o pueblo pertenece, tiene fecha y tiene permiso para usarlo. Si falta alguna, pregunta a un adulto o al educador tradicional antes de usarlo. Revisa también que no pida datos personales ni dinero.",
        "Con un adulto a tu lado, escucha el audio entero una primera vez sin hacer nada. Después puedes repetirlo. Si el audio habla en una lengua indígena y no entiendes, pide ayuda del educador. No grabes ni publiques a otras personas sin su permiso.",
    ],
    vocab=[("recurso digital", "audio, video o imagen que se usa con un aparato"), ("autorizado", "con permiso de quien corresponde"), ("fecha", "día en que se hizo o publicó algo"), ("audio", "sonido grabado"), ("permiso", "aprobación para usar algo")],
    worked=[
        {"title": "Revisar un recurso", "problem": "Te muestran un audio con esta ficha: «Habla: la señora Rosa. Comunidad: se indica. Fecha: este año. Permiso: sí, de la comunidad». ¿Es un recurso autorizado?", "steps": ["Dice quién habla: la señora Rosa.", "Dice la comunidad.", "Tiene fecha y permiso.", "Cumple las cuatro cosas."], "answer": "Sí, es un recurso autorizado"},
        {"title": "Detectar lo que falta", "problem": "Un video dice solo «canto de un pueblo». No dice quién lo hizo, ni fecha, ni permiso. ¿Qué haces?", "steps": ["Faltan autor, comunidad y permiso.", "No lo uso para aprender.", "Pregunto a un adulto o al educador tradicional."], "answer": "No lo uso y pregunto a un adulto o al educador"},
    ],
    mistakes=[
        {"wrong": "Usar el primer video que aparece sin ver quién lo hizo.", "why": "Puede no tener permiso o decir cosas falsas.", "fix": "Revisa quién habla, comunidad, fecha y permiso."},
        {"wrong": "Grabar a una persona sin avisarle para tener un audio.", "why": "Su voz es suya y necesitas su permiso.", "fix": "Pide permiso antes de grabar."},
    ],
    tiers={
        "recovery": [
            ex("Un recurso digital es un audio, video o imagen que se usa con un aparato. ¿Un audio es un recurso digital?", "Sí", "Se escucha con un aparato."),
            ex("¿Cuántas cosas debe tener un recurso autorizado: dos o cuatro?", "Cuatro", "Quién habla, comunidad, fecha y permiso."),
            ex("Si un video no dice quién lo hizo, ¿lo usas para aprender o primero preguntas?", "Primero pregunto", "Falta la autoría."),
        ],
        "understand": [
            ex("¿Cuál es una de las cuatro cosas de un recurso autorizado: la fecha o el color del video?", "La fecha", "La fecha es un dato de la fuente."),
            ex("¿Con quién escuchas el recurso: solo o con un adulto?", "Con un adulto", "Así estás seguro."),
            ex("Un sitio pide tu nombre completo y tu dirección para ver un video. ¿Lo haces?", "No", "No se entregan datos personales."),
        ],
        "apply": [
            ex("Ficha 1: «Habla: sin nombre. Comunidad: no dice. Permiso: no dice». Ficha 2: «Habla: Don Luis. Comunidad: se indica. Fecha: sí. Permiso: sí». ¿Cuál es autorizada?", "La ficha 2", "Tiene los cuatro datos."),
            arith("Un audio dura 2 minutos y 30 segundos. ¿Cuántos segundos son en total? (1 minuto son 60 segundos)", "2*60+30", "Se convierten los minutos a segundos y se suman."),
            ex("Ordena: a) escucho de nuevo, b) reviso quién habla, c) escucho completo una vez. Escribe las letras en orden.", "b, c, a", "Primero reviso la fuente, luego escucho y luego repito."),
        ],
        "reason": [
            ex("Pedro grabó a su abuela cantando para subirlo a una red social sin avisarle. ¿Qué paso se saltó?", "Pedir permiso", "El permiso es lo primero."),
            ex("Un compañero dice que un video es bueno porque tiene muchos «me gusta». ¿Por qué no basta?", "Porque no dice quién lo hizo ni si tiene permiso", "Los «me gusta» no muestran autoría."),
        ],
        "challenge": [
            ex("Tres recursos: A) audio sin autor, B) video de una escuela con permiso de la comunidad y fecha, C) imagen sin fecha ni comunidad. ¿Cuál es el más seguro?", "B", "Es el único con permiso."),
            ex("Lee: «Audio de la señora Elena, de una comunidad del norte, grabado este año, con permiso para usarlo en las escuelas». Cuenta los cuatro datos que tiene.", "Quién habla, comunidad, fecha y permiso", "Los cuatro están en la frase."),
        ],
    },
    context=[ex("Tu curso quiere escuchar una canción de una comunidad. Encuentran un video sin autor. ¿Qué proponen?", "Buscar uno con autoría y permiso o pedir ayuda al educador", "Solo se usan recursos autorizados.")],
    selfcheck=[
        ex("¿Qué es un recurso digital?", "Audio, video o imagen que se usa con un aparato", "Se ve o escucha con un aparato."),
        ex("¿Qué cuatro datos tiene uno autorizado?", "Quién habla, comunidad, fecha y permiso", "Son los datos de la fuente."),
        ex("¿Con quién usas los aparatos?", "Con un adulto", "Es más seguro."),
    ],
    open_task=task(
        f"Con ayuda de un adulto, lee este guion de práctica: {GUION} Antes de escucharlo, completa esta ficha inventada: «Habla: una educadora tradicional. Comunidad: se indica. Fecha: este año. Permiso: sí». Escribe si es un recurso autorizado y por qué. Luego escúchalo entero (que un adulto lo lea) y escribe qué te llamó la atención.",
        "Sí es autorizado porque dice quién habla, comunidad, fecha y permiso. Me llamó la atención que dice «mari mari» al comienzo.",
        ["revisa los cuatro datos", "dice si es autorizado y por qué", "escucha entero", "escribe lo que le llamó la atención"],
        ["ficha revisada", "una frase"],
        ["no revisar la ficha", "decir que sirve sin mirar el permiso"],
        "Reconoce que revisó la ficha antes de escuchar. El audio es de práctica, leído por un adulto.",
    ),
    reinforce="Escucha una canción de tu casa y anota quién la canta y de qué año es, si lo sabes.",
    extend="Haz una ficha de recurso con los cuatro datos para un audio de tu casa.",
)

register(
    LF05, 2,
    materials="Este cuaderno y lápiz. Un adulto lee el guion en voz alta; no se necesita internet.",
    use="Aprenderé a escuchar un audio con apoyo y a sacar la información importante usando pausas y repeticiones. Sirve para comprender sin apuro lo que dice una persona.",
    prior=["Sé revisar si un recurso es autorizado.", "Sé escuchar completo la primera vez."],
    explain=[
        "Escuchar con apoyo quiere decir usar ayudas para comprender: pausar, repetir y mirar imágenes o un guion. En un audio puedes detener la reproducción después de cada idea. Con la pausa piensas, anotas y vuelves a escuchar si hace falta. No tienes que entender todo a la primera.",
        "Para comprender un audio, primero escucha entero. Después escucha por partes y anota palabras clave, que son las palabras más importantes. Las palabras clave responden: ¿quién habla?, ¿de qué habla?, ¿dónde?, ¿cuándo? Con ellas puedes decir lo que comprendiste con tus palabras.",
        "Si el audio está en una lengua indígena, no traduzcas palabra por palabra. Usa el apoyo que da la comunidad: un guion, una imagen o la explicación del educador tradicional. Si no entiendes algo, anótalo como duda y pregunta.",
    ],
    vocab=[("pausar", "detener un audio por un momento"), ("repetir", "escuchar otra vez"), ("palabra clave", "palabra importante del mensaje"), ("duda", "algo que no entiendo"), ("apoyo", "ayuda para comprender")],
    worked=[
        {"title": "Escuchar por partes", "problem": f"Un adulto lee este guion: {GUION} Anota las palabras clave.", "steps": ["¿Quién habla? Una persona de un pueblo.", "¿De qué habla? Del río.", "¿Cómo es? Ancho y tranquilo.", "¿Quiénes van? Los niños, en la tarde, a mirar patos."], "answer": "Palabras clave: río, ancho, tranquilo, niños, tarde, patos"},
        {"title": "Anotar una duda", "problem": "En el audio, la persona dice una palabra que no conoces. ¿Qué haces?", "steps": ["Pauso el audio.", "Anoto que no entendí esa palabra.", "Pregunto al educador después."], "answer": "Pausar, anotar la duda y preguntar al educador"},
    ],
    mistakes=[
        {"wrong": "Querer anotar todo lo que dice el audio sin pausar.", "why": "No alcanzas y pierdes el sentido.", "fix": "Pausa después de cada idea y anota palabras clave."},
        {"wrong": "Inventar lo que no oíste.", "why": "Puedes decir algo falso.", "fix": "Anota «no entendí» y pregunta."},
    ],
    tiers={
        "recovery": [
            ex("Pausar es detener un audio por un momento. ¿Pausas para pensar o para dejar de escuchar?", "Para pensar", "La pausa ayuda a comprender."),
            ex("Repetir es escuchar otra vez. Si no entendiste una idea, ¿qué haces: repetir esa parte o seguir sin pensar?", "Repetir esa parte", "Así comprendes mejor."),
            ex(f"En el guion de práctica: {GUION} ¿Cómo es el río?", "Ancho y tranquilo", "El guion lo dice."),
        ],
        "understand": [
            ex("Una palabra clave es una palabra importante del mensaje. En «El río es ancho», ¿cuál es una palabra clave?", "Río o ancho", "Ambas dicen lo importante."),
            ex("¿Para qué sirve anotar una duda?", "Para preguntar después y no inventar", "Así evitas errores al comprender."),
            ex("¿Escuchas primero entero o por partes?", "Entero", "Primero comprendes la idea general."),
        ],
        "apply": [
            ex(f"Según el guion, ¿a qué hora del día llegan los niños? {GUION}", "En la tarde", "El guion dice «en la tarde»."),
            ex("Con el mismo guion, ¿qué animales miran los niños?", "Patos", "El guion lo dice."),
            arith("Un audio tiene 4 partes y cada parte dura 30 segundos. ¿Cuántos segundos dura el audio?", "4*30", "Se suman 30 segundos cuatro veces."),
        ],
        "reason": [
            ex("Sol anotó que el río era «peligroso» pero el audio no lo dice. ¿Qué error cometió?", "Inventó algo que no oyó", "Debe anotar solo lo que dice el audio."),
            ex("Un niño quiere traducir cada palabra del audio antes de comprender el tema. ¿Qué le sugieres?", "Primero escuchar entero y buscar el tema", "Así comprende la idea principal."),
        ],
        "challenge": [
            ex("Lee: «Audio de práctica: Hoy hay viento. Mi abuela cierra la ventana. Después hace té». Anota la secuencia con primero, después.", "Primero hay viento; después la abuela cierra la ventana; después hace té", "Se ordenan los tres hechos."),
            ex("Audio de práctica: «Hoy hay viento. Mi abuela cierra la ventana. Después hace té». ¿Cuántos hechos suceden?", "3", "Hay viento, cierra la ventana y hace té."),
        ],
    },
    context=[ex("Tu profesor reproduce un audio y hablan muy rápido. ¿Qué le pides: pausar y repetir o apagarlo?", "Pausar y repetir", "Son apoyos para comprender.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Qué es una palabra clave?", "Una palabra importante del mensaje", "Resume la idea."),
        ex("¿Qué haces con una duda?", "La anoto y pregunto", "No se inventa."),
        ex("¿Qué haces primero con un audio?", "Escucharlo entero", "Para ver la idea general."),
    ],
    open_task=task(
        "Pide a un adulto que lea dos veces este audio inventado: «Mari mari. Hoy visité la feria del pueblo. Había tejidos de colores y mucha gente. Compré pan amasado y volví a casa». La primera vez escucha entero. La segunda vez pausa después de cada oración y anota una palabra clave. Escribe tus cuatro palabras clave y una duda.",
        "Palabras clave: feria, tejidos, pan, casa. Duda: ¿cuándo se dice «mari mari»?",
        ["escucha entero y luego por partes", "anota cuatro palabras clave", "escribe una duda"],
        ["cuatro palabras clave", "una duda"],
        ["inventar datos", "traducir sin comprender el tema"],
        "Reconoce el uso de pausas y que anotó una duda en lugar de inventar.",
    ),
    reinforce="Escucha un audio corto de tu casa, párate después de cada frase y di una palabra clave.",
    extend="Anota la secuencia de tres hechos de un audio con primero, después y al final.",
)

register(
    LF05, 3,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a transcribir, es decir, a escribir lo que oigo, con cuidado y con ayuda. Sirve para guardar lo que dice una persona sin cambiar sus palabras.",
    prior=["Sé escuchar por partes.", "Sé copiar palabras de un modelo."],
    explain=[
        "Transcribir es escribir con letras lo que alguien dice en un audio. Se escribe exactamente lo que se oye, sin agregar ni quitar palabras. Se usa el modelo de quien enseña para escribir las palabras de una lengua indígena. Si no sabes cómo se escribe, no la inventes.",
        "Si no se entiende una parte, escribe [no se entiende] en lugar de adivinar. Por ejemplo: «Hoy fuimos al [no se entiende] con mi abuela». Así otra persona verá dónde falta algo y podrá ayudarte. Marcar la duda es honesto.",
        "Antes de transcribir a una persona, pide su permiso. Su voz es suya y lo que dice también. Cuando termines, escribe quién habló y la fecha. Y muestra tu transcripción a quien te enseñó para que la corrija. No la publiques sin permiso.",
    ],
    vocab=[("transcribir", "escribir lo que se oye"), ("[no se entiende]", "marca para lo que no se oyó bien"), ("fiel", "igual a lo que se dijo"), ("permiso", "aprobación para usar algo"), ("corrección", "cambio para mejorar")],
    worked=[
        {"title": "Transcribir fiel", "problem": "Un adulto lee: «El río está tranquilo hoy». Transcribe.", "steps": ["Escucho la frase entera.", "Escribo cada palabra en orden.", "Reviso que no falte ninguna."], "answer": "El río está tranquilo hoy"},
        {"title": "Marcar lo que no se entiende", "problem": "El audio dice «Llegamos al ... con mi tía» y no entiendes la palabra del medio. ¿Cómo lo transcribes?", "steps": ["No adivino la palabra.", "Escribo [no se entiende] en su lugar."], "answer": "Llegamos al [no se entiende] con mi tía"},
    ],
    mistakes=[
        {"wrong": "Cambiar palabras para que la frase suene mejor.", "why": "Ya no es lo que la persona dijo.", "fix": "Escribe lo que se oyó, aunque suene distinto."},
        {"wrong": "Adivinar una palabra que no se oyó.", "why": "Puedes escribir algo falso.", "fix": "Marca [no se entiende]."},
    ],
    tiers={
        "recovery": [
            ex("Transcribir es escribir lo que se oye. Si oyes «hola amigos», ¿escribes «hola amigos» o «buenos días»?", "Hola amigos", "Se escribe lo que se oye."),
            ex("Si no entiendes una parte, ¿qué escribes: [no se entiende] o una palabra adivinada?", "[no se entiende]", "No se adivina."),
            ex("Antes de transcribir a una persona, ¿qué haces?", "Pedir permiso", "Su voz es suya."),
        ],
        "understand": [
            ex("¿Por qué una transcripción debe ser fiel?", "Para no cambiar lo que la persona dijo", "Es de quien lo dijo."),
            ex("Una transcripción dice: «Fuimos al [no se entiende] con mamá». ¿Qué palabra falta?", "La palabra después de «al»", "Se marcó con el corchete."),
            ex("¿Qué dos datos agregas al final de tu transcripción además del texto?", "Quién habló y la fecha", "Son datos de la fuente."),
        ],
        "apply": [
            ex("Transcribe lo que lee el adulto: «Sol sale en la mañana». Elige: a) «Sol sale en la mañana», b) «El sol sale en la tarde». Letra:", "a", "Es igual a lo dicho."),
            arith("Tu transcripción tiene 12 palabras y marcaste 2 como [no se entiende]. ¿Cuántas palabras sí se entendieron?", "12-2", "Se restan las dudas."),
            ex("Audio: «Mari mari. Estamos en el patio». Transcribe el comienzo y cuenta cuántas palabras hay en total.", "Mari mari. Estamos en el patio; 6 palabras", "Mari, mari, estamos, en, el y patio."),
        ],
        "reason": [
            ex("Teo transcribió una palabra indígena como suena en castellano y cambió letras. ¿Qué debió hacer?", "Copiar del modelo que da el educador", "La escritura la confirma la comunidad."),
            ex("Beto subió a internet una transcripción de la abuela sin avisarle. ¿Qué debió hacer antes?", "Pedir permiso", "Su voz y sus palabras son suyas."),
        ],
        "challenge": [
            ex("Transcripción: «Plantamos [no se entiende] en el huerto». ¿Cuántas palabras sí se entendieron, sin contar la marca?", "4", "Plantamos, en, el y huerto."),
            ex("Dos transcripciones del mismo audio: A) «Fuimos al cerro y comimos pan». B) «Fuimos al [no se entiende] y comimos pan». El educador dice que la palabra era «cerro». ¿Cuál era más honesta antes de la ayuda?", "La B", "Marcó la duda en vez de adivinar."),
        ],
    },
    context=[ex("Vas a transcribir una entrevista a tu vecina. ¿Qué dices antes de empezar?", "¿Me da permiso para escribir lo que diga?", "Primero se pide permiso.")],
    selfcheck=[
        ex("¿Qué es transcribir?", "Escribir lo que se oye", "Es escribir lo escuchado."),
        ex("¿Qué escribes si no oyes bien?", "[no se entiende]", "No se adivina."),
        ex("¿Qué debes pedir antes?", "Permiso", "A la persona que habla."),
    ],
    open_task=task(
        "Pide a un adulto que lea este audio inventado dos veces: «Hola, soy Camila. Hoy fui a la plaza con mi tío. Vimos una exposición de [una palabra que no se entiende]. Después comimos helado». Transcribe lo que oyes. Usa [no se entiende] donde el adulto indique una parte confusa. Al final escribe quién habló y una pregunta para el educador.",
        "Hola, soy Camila. Hoy fui a la plaza con mi tío. Vimos una exposición de [no se entiende]. Después comimos helado. Habló: Camila (personaje inventado). Pregunta: ¿cómo se escribe la palabra?",
        ["transcribe sin agregar", "marca la parte confusa", "escribe quién habló", "escribe una pregunta"],
        ["transcripción", "pregunta"],
        ["adivinar la palabra", "cambiar la frase"],
        "Reconoce que fue fiel y marcó la duda. El audio es de práctica, leído por un adulto.",
    ),
    reinforce="Transcribe una frase corta que te diga alguien de tu casa y léesela para comprobar.",
    extend="Transcribe tres frases de un cuento que te lea un adulto y marca lo que no entendiste.",
)

register(
    LF05, 4,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a compartir lo que escuché o transcribí citando el recurso y diciendo qué no sé. Sirve para devolver con respeto lo aprendido a la comunidad y no publicar lo que no corresponde.",
    prior=["Sé transcribir con cuidado.", "Sé qué es un recurso autorizado."],
    explain=[
        "Compartir lo que aprendiste de un recurso digital incluye citarlo: di el título o de qué trata, quién habló, la fecha y de qué comunidad es. Por ejemplo: «Escuché el audio de la señora Elena, de este año, con permiso». Citar es reconocer la fuente.",
        "También di qué no sabes. Si no entendiste algo o no sabes cómo se pronuncia una palabra, dilo. Si usaste una palabra confirmada, puedes decir «la confirmó el educador». Y si no tienes permiso para compartir una grabación, no la compartas: puedes contar lo que aprendiste con tus propias palabras.",
        "Antes de publicar, pregunta tres cosas: ¿tengo permiso de la persona?, ¿tengo permiso de la comunidad? y ¿mi trabajo cuenta con respeto lo que escuché? Si alguna respuesta es no, no lo publiques. Puedes mostrárselo a la persona que te enseñó y pedirle su opinión.",
    ],
    vocab=[("citar", "decir de dónde viene la información"), ("publicar", "mostrar algo a muchas personas"), ("límite", "lo que no sé o no puedo hacer"), ("permiso", "aprobación para usar o publicar algo"), ("devolver", "mostrar a quien enseñó lo que hice")],
    worked=[
        {"title": "Citar el recurso", "problem": "Escuchaste un audio de la señora Elena, grabado este año, con permiso. Escribe la cita.", "steps": ["Digo quién habló: la señora Elena.", "Digo la fecha: este año.", "Digo que hay permiso."], "answer": "Audio de la señora Elena, de este año, con permiso"},
        {"title": "Cuándo no publicar", "problem": "Tienes la grabación de tu abuelo, pero él no te ha dado permiso para mostrarla en clases. ¿La compartes?", "steps": ["Falta el permiso de la persona.", "No la comparto.", "Cuento con mis palabras lo que aprendí o le pido permiso."], "answer": "No, hasta tener su permiso"},
    ],
    mistakes=[
        {"wrong": "Publicar una grabación porque «es para el colegio».", "why": "El permiso es necesario aunque sea para el colegio.", "fix": "Pregunta primero a la persona y a la comunidad."},
        {"wrong": "Decir «lo encontré en internet» como fuente.", "why": "No dice quién habló ni si tiene permiso.", "fix": "Anota quién habló, la fecha y de qué comunidad es."},
    ],
    tiers={
        "recovery": [
            ex("Citar es decir de dónde viene la información. Si escuchaste a Don Luis, ¿a quién citas?", "A Don Luis", "Él es la fuente."),
            ex("Antes de publicar una grabación de una persona, ¿qué necesitas: su permiso o nada?", "Su permiso", "Es lo primero."),
            ex("Si no sabes algo, ¿lo dices o lo inventas?", "Lo digo", "No se inventa."),
        ],
        "understand": [
            ex("¿Cuáles son los datos de una buena cita: quién habló, fecha y comunidad, o el color de la pantalla?", "Quién habló, fecha y comunidad", "Son datos de la fuente."),
            ex("¿Por qué no basta con decir «lo vi en internet»?", "Porque no dice quién habló ni si hay permiso", "Falta la fuente."),
            ex("Si no tienes permiso para compartir una grabación, ¿qué puedes hacer?", "Contar con mis palabras lo que aprendí", "Sin mostrar la grabación."),
        ],
        "apply": [
            ex("Elige la mejor cita: a) «Audio de la señora Elena, de este año, con permiso», b) «Un audio de internet». Letra:", "a", "Dice quién, cuándo y permiso."),
            arith("Un curso tiene 3 audios y escribe 4 datos de cita por cada uno. ¿Cuántos datos escriben en total?", "3*4", "Se suman 4 datos tres veces."),
            ex("Las tres preguntas antes de publicar son: permiso de la persona, permiso de la comunidad y respeto en el trabajo. ¿Cuántas son?", "3", "Se cuentan tres."),
        ],
        "reason": [
            ex("Marta dice que puede publicar cualquier video de una comunidad porque «es público». ¿Qué le falta considerar?", "El permiso de la comunidad", "Aunque se vea, puede no tener permiso."),
            ex("Luis mostró su trabajo a la educadora antes de publicarlo. ¿Qué hizo bien?", "Devolvió su trabajo para que lo revisara", "Así cuidó la fuente."),
        ],
        "challenge": [
            ex("Lee: «Escuché el audio de la señora Elena, con permiso de la comunidad. No entendí una palabra». Escribe la fuente, el permiso y el límite.", "Fuente: la señora Elena; permiso: sí; límite: no entendí una palabra", "Separa quién, permiso y lo que falta."),
            ex("Tres compañeros quieren publicar sus trabajos. Ana tiene permiso de la persona y de la comunidad. Beto solo de la persona. Camila de ninguno. ¿Quién puede publicar?", "Ana", "Solo ella tiene ambos permisos."),
        ],
    },
    context=[ex("Quieres subir a una red social un audio de la fiesta de una comunidad. ¿Qué pides primero?", "Permiso de la persona y de la comunidad", "Sin permiso no se publica.")],
    selfcheck=[
        ex("¿Qué dices al citar un audio?", "Quién habló, fecha y comunidad", "Son los datos de la fuente."),
        ex("¿Qué haces si no tienes permiso?", "No publico", "Cuento con mis palabras."),
        ex("¿Qué es devolver?", "Mostrar a quien enseñó lo que hice", "Para que lo revise."),
    ],
    open_task=task(
        "Con este audio inventado: «Audio de la señora Elena, de este año, con permiso. Dice que el río está tranquilo y que los patos llegan en la tarde». Escribe una presentación de tres frases: 1) cita del audio, 2) lo que aprendiste en una frase y 3) un límite. Agrega una frase que diga si publicarías el audio y por qué.",
        "Escuché el audio de la señora Elena, de este año, con permiso. Aprendí que el río está tranquilo y los patos llegan en la tarde. No sé cómo se pronuncia el nombre del río. No lo publicaría sin pedir permiso a la persona y a la comunidad.",
        ["cita el audio", "resume lo aprendido", "dice un límite", "dice si publicaría y por qué"],
        ["tres frases y una decisión"],
        ["publicar sin permiso", "no citar la fuente"],
        "Reconoce la cita y la decisión de pedir permiso. El audio es de práctica; la señora Elena es un personaje inventado.",
    ),
    reinforce="Escribe la cita de un video o audio de tu casa con quién habló y la fecha.",
    extend="Haz una lista con tres preguntas que harías antes de publicar una grabación.",
)

# ================================================================ LR01
register(
    LR01, 1,
    materials="Este cuaderno y lápiz. Las listas de palabras son ejemplos conocidos; el educador/a tradicional puede completar y corregir.",
    use="Aprenderé a recordar palabras y expresiones que ya tengo cerca, en mi casa o en el castellano de Chile, sin juzgar a nadie. Sirve para sentir que la lengua indígena está presente y cuidarla.",
    prior=["Sé qué es una palabra.", "Sé que las lenguas se cuidan."],
    explain=[
        "Revitalización de una lengua quiere decir hacerla vivir otra vez cuando hay pocas personas que la hablan. Todos pueden ayudar de maneras distintas. Una manera es reconocer las palabras que ya están cerca, sin juzgar a nadie y sin evaluar quién sabe más.",
        "En el castellano de Chile hay palabras que vienen de lenguas indígenas. Del quechua vienen papa, palta, choclo, guagua y cóndor. Del mapuzugun vienen copihue y quiltro. Cada una cuenta una historia de contacto entre lenguas. Si dices «choclo» o «palta», ya estás usando palabras de origen indígena.",
        "También puede haber palabras que tu familia usa, como saludos o nombres de lugares. Anótalas con el nombre de quien las dijo. No importa si no sabes qué significan: lo importante es no juzgar ni burlarse. Si alguien no conoce palabras de su pueblo, no está en falta: hay muchas razones por las que se dejaron de transmitir.",
    ],
    vocab=[("revitalización", "hacer vivir otra vez una lengua"), ("préstamo", "palabra que una lengua toma de otra"), ("origen", "de dónde viene una palabra"), ("quechua", "lengua de un pueblo originario"), ("mapuzugun", "lengua del pueblo Mapuche")],
    worked=[
        {"title": "Reconocer palabras", "problem": "Tu mamá dice: «Compré papas, paltas y choclos». ¿Cuántas palabras de origen quechua dijo?", "steps": ["Papa viene del quechua.", "Palta viene del quechua.", "Choclo viene del quechua.", "Son tres."], "answer": "3 palabras"},
        {"title": "Sin juzgar", "problem": "Un compañero dice que no sabe ninguna palabra de la lengua de su abuela. Otro se ríe. ¿Qué dices?", "steps": ["No importa cuántas palabras sepa.", "Hay muchas razones para que una lengua se deje de hablar.", "Respeto y le pido que aprenda junto con el curso."], "answer": "Que no está en falta, que lo respetamos y aprendemos juntos"},
    ],
    mistakes=[
        {"wrong": "Burlarse de quien no sabe palabras de su pueblo.", "why": "Hay muchas razones por las que una lengua deja de transmitirse.", "fix": "Respeta y ayuda a aprender, sin juzgar."},
        {"wrong": "Decir «yo no tengo palabras indígenas».", "why": "En el castellano de Chile ya usamos varias.", "fix": "Revisa palabras como papa, palta, choclo y guagua."},
    ],
    tiers={
        "recovery": [
            ex("Papa, palta, choclo, guagua y cóndor vienen del quechua. ¿De qué lengua viene «choclo»?", "Del quechua", "Está en la lista del quechua."),
            ex("Copihue y quiltro vienen del mapuzugun. ¿De qué lengua viene «copihue»?", "Del mapuzugun", "Está en la lista del mapuzugun."),
            ex("Revitalizar una lengua es hacerla vivir otra vez. ¿Se logra burlándose de quien no la sabe?", "No", "Se logra respetando y aprendiendo."),
        ],
        "understand": [
            ex("Una palabra de origen indígena en tu castellano, ¿es un préstamo?", "Sí", "Es una palabra tomada de otra lengua."),
            ex("¿Por qué no se evalúa quién sabe más palabras?", "Porque hay muchas razones por las que se dejó de hablar", "No se juzga a nadie."),
            ex("Lía dijo «guagua» para hablar de un bebé. ¿Usó una palabra de origen quechua?", "Sí", "Guagua viene del quechua."),
        ],
        "apply": [
            ex("Lista: papa, copihue, palta, quiltro, choclo. ¿Cuántas vienen del quechua?", "3", "Papa, palta y choclo."),
            ex("De esa misma lista, ¿cuántas vienen del mapuzugun?", "2", "Copihue y quiltro."),
            arith("En una caja hay 4 papas, 3 paltas y 2 choclos. ¿Cuántos alimentos de origen quechua hay en total?", "4+3+2", "Se suman los tres tipos."),
        ],
        "reason": [
            ex("Camila dice que su familia «no tiene nada indígena». Sin embargo, comen choclo y papas. ¿Qué le dices?", "Que sus palabras ya tienen origen indígena", "Choclo y papa son préstamos."),
            ex("Un niño se burla de otro que no sabe saludar en mapuzugun. ¿Qué error comete?", "Juzga a alguien por lo que no sabe", "No debe evaluar a nadie."),
        ],
        "challenge": [
            ex("Lee: «Mi tío llevó un quiltro a ver el copihue en el patio, y comió choclo». ¿Cuántas palabras de origen indígena hay y cuáles?", "3: quiltro, copihue y choclo", "Se cuentan tres préstamos."),
            ex("Una compañera dice «aquí hay cinco palabras de origen quechua: papa, palta, choclo, guagua y copihue». ¿Cuál se equivocó de lengua?", "Copihue", "Copihue es del mapuzugun."),
        ],
    },
    context=[ex("En el almuerzo, tu abuela dice «guagua» para hablar de tu hermano pequeño. ¿Qué puedes decirle?", "Que esa palabra viene del quechua y que nos gusta usarla", "Reconoce el origen sin burlarse.")],
    selfcheck=[
        ex("¿Qué es revitalizar una lengua?", "Hacerla vivir otra vez", "Es cuidarla para que se hable."),
        ex("¿Qué palabra viene del quechua: palta o copihue?", "Palta", "Copihue viene del mapuzugun."),
        ex("¿Se juzga a quien no sabe palabras de su pueblo?", "No", "A esa persona se la respeta."),
    ],
    open_task=task(
        "Mira esta lista de palabras: papa, palta, choclo, guagua, cóndor, copihue, quiltro. Escribe cuántas son de origen quechua (papa, palta, choclo, guagua y cóndor) y cuántas del mapuzugun (copihue y quiltro). Elige tres y escribe una oración con cada una. Después pregunta a un adulto de tu casa si usa alguna de esas palabras y anota cuál con su nombre.",
        "Quechua: papa, palta, choclo, guagua, cóndor (5). Mapuzugun: copihue, quiltro (2). Oraciones: Comí papas. El cóndor vuela. El copihue es rojo. Mi mamá usa «guagua» (mamá Ana).",
        ["cuenta 5 y 2", "escribe tres oraciones", "anota una palabra con el nombre de quien la usa"],
        ["conteo", "tres oraciones", "nota con nombre"],
        ["confundir la lengua de origen", "juzgar a un adulto por no usar palabras"],
        "Reconoce el conteo y las oraciones. Si hay dudas sobre el origen, un especialista puede confirmarlo.",
    ),
    reinforce="Haz una lista con cinco alimentos de tu casa y marca cuáles tienen nombre de origen quechua.",
    extend="Pregunta a un adulto qué palabras de otra lengua usaba su abuela y anótalas con su nombre.",
)

register(
    LR01, 2,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a preguntar por el significado, la pronunciación y el contexto de una palabra a quien la conoce. Sirve para aprender palabras de una lengua indígena a partir de una fuente de la comunidad.",
    prior=["Sé qué es una fuente.", "Sé qué son mari mari, mapu, ko, antü y kuyen."],
    explain=[
        "Cuando una persona de la comunidad te enseña una palabra, hay tres cosas que debes preguntar. El significado: ¿qué quiere decir? La pronunciación: ¿cómo se dice? El contexto: ¿cuándo y con quién se usa? Con las tres respuestas puedes usar la palabra con cuidado.",
        "Por ejemplo, «mari mari» es un saludo en mapuzugun. Su significado es saludar. Su pronunciación la muestra el educador o educadora tradicional con su voz. Su contexto es cuando saludas a alguien. Otra palabra puede tener otro contexto: una palabra solo para ocasiones especiales no debe usarse en el recreo.",
        "Escucha atento sin interrumpir. Anota lo que te dicen con el nombre de quien enseña. Si no entiendes, pide que repita. Nunca corrijas a la persona que enseña ni digas que lo hace «mal»: ella es la fuente. Esto vale también para un relato breve que cuente la comunidad: escúchalo entero, anota quién lo contó y qué palabras importantes oíste, y pregunta lo que no entiendas. Por qué ese relato es importante para el pueblo lo explica su comunidad.",
    ],
    vocab=[("significado", "lo que quiere decir una palabra"), ("pronunciación", "cómo se dice una palabra"), ("contexto", "cuándo y con quién se usa"), ("fuente comunitaria", "persona de la comunidad que enseña"), ("repetir", "decir otra vez")],
    worked=[
        {"title": "Tres preguntas", "problem": "El educador te enseña «ko». ¿Qué tres preguntas haces?", "steps": ["¿Qué quiere decir? (significado)", "¿Cómo se dice? (pronunciación)", "¿Cuándo y con quién se usa? (contexto)"], "answer": "Significado, pronunciación y contexto"},
        {"title": "Anotar con la fuente", "problem": "La educadora Doña Elena te enseñó que «mapu» quiere decir tierra. Anótalo bien.", "steps": ["Escribo la palabra: mapu.", "Escribo el significado: tierra.", "Escribo la fuente: Doña Elena."], "answer": "mapu: tierra (enseñó Doña Elena)"},
    ],
    mistakes=[
        {"wrong": "Pensar que si sabes el significado ya puedes usar la palabra en cualquier lugar.", "why": "El contexto también importa.", "fix": "Pregunta cuándo y con quién se usa."},
        {"wrong": "Corregir a la persona que enseña.", "why": "Ella es la fuente.", "fix": "Si tienes dudas, pregunta con respeto."},
    ],
    tiers={
        "recovery": [
            ex("Las tres cosas que preguntas son significado, pronunciación y contexto. ¿Cuántas son?", "3", "Se cuentan tres."),
            ex("«Mari mari» es un saludo. ¿Para qué sirve?", "Para saludar", "Es un saludo."),
            ex("Si no entiendes una explicación, ¿qué haces: pides que repita o te vas?", "Pido que repita", "Repetir te ayuda a aprender."),
        ],
        "understand": [
            ex("¿Qué es el contexto de una palabra?", "Cuándo y con quién se usa", "Dice la situación."),
            ex("¿Qué te dice la pronunciación?", "Cómo se dice la palabra", "Es el sonido."),
            ex("¿Por qué no corriges a quien te enseña?", "Porque es la fuente", "Conoce la lengua."),
        ],
        "apply": [
            ex("Ficha: «ko / agua / lo dijo Don Luis». ¿Cuál es el significado y quién enseñó?", "Agua; Don Luis", "La ficha dice los dos datos."),
            ex("Anota con las tres preguntas: la palabra «antü» quiere decir sol. Falta saber... ¿qué dos datos?", "Pronunciación y contexto", "Ya tienes el significado."),
            arith("Aprendes 2 palabras cada semana durante 5 semanas. ¿Cuántas palabras aprendes?", "2*5", "Se suman 2 palabras cinco veces."),
        ],
        "reason": [
            ex("Beto dijo «mari mari» para burlarse en el recreo. ¿Qué dato del contexto no respetó?", "Que es un saludo y no una burla", "El contexto es saludar."),
            ex("Ema corrigió la pronunciación de la educadora. ¿Qué error cometió?", "Corregir a la fuente", "Ella es quien sabe."),
        ],
        "challenge": [
            ex("Completa la ficha: «Palabra: kuyen. Significado: ___. Pronunciación: la dice el educador. Contexto: se pregunta».", "luna", "Kuyen significa luna."),
            ex("Escuchas un relato breve que cuenta una persona de la comunidad. ¿Qué anotas primero: quién lo contó o el final que imaginas?", "Quién lo contó", "La fuente va primero y el final no se inventa."),
        ],
    },
    context=[ex("La educadora te enseña una palabra y dice que solo se usa en ceremonias. ¿La usas en el recreo?", "No", "El contexto no es el recreo.")],
    selfcheck=[
        ex("¿Qué tres cosas preguntas?", "Significado, pronunciación y contexto", "Son las tres preguntas."),
        ex("¿Qué quiere decir «ko»?", "Agua", "Es una palabra de mapuzugun."),
        ex("¿Quién es la fuente?", "La persona de la comunidad que enseña", "Ella conoce la lengua."),
    ],
    open_task=task(
        "Completa esta ficha para dos de las cinco palabras conocidas (mari mari, mapu, ko, antü, kuyen). Escribe: palabra, significado, y deja dos líneas para pronunciación y contexto. Cuando venga el educador tradicional, pregúntale esos dos datos y anótalos con su nombre. Si no puedes preguntarle, escribe qué le preguntarías.",
        "Palabra: ko. Significado: agua. Pronunciación: (la dirá el educador). Contexto: (se lo preguntaré). Palabra: antü. Significado: sol. Pronunciación y contexto: le preguntaré.",
        ["completa dos fichas", "escribe el significado correcto", "deja o completa pronunciación y contexto", "anota el nombre de la fuente si la tiene"],
        ["dos fichas"],
        ["inventar la pronunciación", "usar la palabra fuera de contexto"],
        "Reconoce que dejó espacio para preguntar. Refuerza que la pronunciación la enseña la fuente.",
    ),
    reinforce="Pregunta a un adulto si usa un saludo especial y anota qué significa y cuándo se usa.",
    extend="Haz una ficha con tres preguntas para entrevistar a un educador tradicional.",
)

register(
    LR01, 3,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a usar una expresión conocida en una situación adecuada y segura. Sirve para dar un uso real y respetuoso a la lengua.",
    prior=["Sé las tres preguntas.", "Sé que el contexto importa."],
    explain=[
        "Usar una expresión de una lengua indígena en la vida real ayuda a que la lengua viva. Pero hay que hacerlo en el momento correcto. Una situación pertinente es una situación adecuada: la persona que escucha la comprende, hay respeto y la fuente lo permite. Un lugar seguro es donde nadie se burla.",
        "Por ejemplo, «mari mari» se usa para saludar. Puedes decirlo a una visita de la comunidad si el educador lo permite, o en una actividad del curso donde todos lo practican. No sirve para hacer una broma ni para sorprender a alguien que no lo espera.",
        "Antes de usar una expresión pregunta: ¿me enseñó alguien de la comunidad?, ¿sé qué significa?, ¿es adecuado el momento?, ¿puedo equivocarme sin que nadie se ría? Si respondes sí a todo, úsala con calma. Si te equivocas, pide ayuda y vuelve a intentar.",
    ],
    vocab=[("pertinente", "adecuado para la situación"), ("seguro", "donde nadie se burla"), ("saludo", "palabra para recibir a alguien"), ("practicar", "hacer varias veces para aprender"), ("equivocarse", "hacer algo mal sin querer")],
    worked=[
        {"title": "Elegir la situación", "problem": "Quieres usar «mari mari». ¿Cuál situación es adecuada: a) saludar a la educadora cuando llega al curso, b) gritarlo para asustar a un compañero?", "steps": ["En a) se usa para saludar.", "En b) se usa para asustar y no respeta.", "La situación adecuada es la a)."], "answer": "La a) saludar a la educadora cuando llega"},
        {"title": "Preguntas antes de usar", "problem": "Quieres usar «mari mari» para saludar a una visita de la comunidad. ¿Qué preguntas te haces?", "steps": ["¿Me la enseñó alguien de la comunidad?", "¿Sé qué significa?", "¿Es adecuado el momento y nadie se burlará?"], "answer": "Si me la enseñó la comunidad, sé su significado y es un momento adecuado"},
    ],
    mistakes=[
        {"wrong": "Usar una expresión para bromear.", "why": "Es una lengua viva y se usa con respeto.", "fix": "Úsala en situaciones de saludo o práctica real."},
        {"wrong": "No intentar por miedo a equivocarte.", "why": "Todos aprenden practicando.", "fix": "Practica en un ambiente seguro y pide ayuda."},
    ],
    tiers={
        "recovery": [
            ex("«Mari mari» sirve para saludar. ¿La usas para saludar o para asustar a alguien?", "Para saludar", "Esa es su función."),
            ex("Un lugar seguro es donde nadie se burla. ¿Practicas allí o donde se ríen de ti?", "Donde nadie se burla", "Allí te sientes tranquilo."),
            ex("Si te equivocas al decir una palabra, ¿pides ayuda o te rindes?", "Pido ayuda", "Se aprende practicando."),
        ],
        "understand": [
            ex("¿Cuál es una situación pertinente para «mari mari»: recibir a una visita o hacer una broma?", "Recibir a una visita", "Es un saludo."),
            ex("¿Por qué es importante que te la haya enseñado alguien de la comunidad?", "Porque es la fuente", "Conoce el significado y el uso."),
            ex("¿Para qué sirve practicar?", "Para aprender", "Se mejora repitiendo."),
        ],
        "apply": [
            ex("Tres situaciones: A) saludar a una visita, B) gritar en la biblioteca, C) bromear con un amigo. ¿En cuál usarías «mari mari»?", "A", "Es un saludo."),
            ex("Cuatro preguntas antes de usar una expresión: ¿me enseñó la comunidad?, ¿sé qué significa?, ¿es el momento adecuado?, ¿puedo equivocarme sin burlas? ¿Cuántas son?", "4", "Se cuentan cuatro."),
            arith("Tu curso practica el saludo 3 veces por semana durante 4 semanas. ¿Cuántas veces lo practican?", "3*4", "Se suman 3 veces cuatro semanas."),
        ],
        "reason": [
            ex("Teo usó «ko» para llamar a un compañero «agua» como apodo ofensivo. ¿Qué error cometió?", "Usó la palabra para burlarse", "La palabra no es para burlas."),
            ex("Una niña quiere usar «mari mari» pero no sabe cómo se dice. ¿Qué hace?", "Pregunta al educador cómo se dice", "La pronunciación la enseña la fuente."),
        ],
        "challenge": [
            ex("Lee: «Don Luis llega al curso. Los niños dicen mari mari con el educador, uno por uno, y Don Luis sonríe». ¿Qué cuatro preguntas cumple esta situación?", "Se la enseñó la comunidad, saben el significado, el momento es adecuado y nadie se burla", "Cumple las cuatro preguntas."),
            ex("Dos amigos usan «mari mari». Uno lo dice al recibir a una visita. El otro lo grita para asustar. ¿Quién respetó el uso?", "El que lo dijo al recibir a la visita", "Respetó el contexto."),
        ],
    },
    context=[ex("Una visita de la comunidad llega a tu escuela. ¿Cómo la recibes si el educador está de acuerdo?", "La saludo con «mari mari»", "Es un saludo pertinente.")],
    selfcheck=[
        ex("¿Qué es una situación pertinente?", "Una situación adecuada", "Es el momento correcto."),
        ex("En Lengua y Cultura: ¿Qué haces si te equivocas?", "Pido ayuda y lo intento de nuevo", "Se aprende practicando."),
        ex("¿Para qué se usa «mari mari»?", "Para saludar", "Es un saludo."),
    ],
    open_task=task(
        "Mira estas cuatro situaciones: A) recibir a una visita de la comunidad, B) hacer una broma, C) saludar a un amigo en una actividad del curso donde todos practican, D) gritar en el patio. Escribe las letras de las situaciones pertinentes para decir «mari mari» y explica en una frase por qué. Después practica el saludo con un adulto de tu casa, en un lugar seguro, si el educador te lo ha enseñado.",
        "Pertinentes: A y C, porque son saludos con respeto y práctica real. Practiqué con mi mamá en un lugar seguro.",
        ["escribe A y C", "explica en una frase", "practica en lugar seguro"],
        ["letras", "una frase"],
        ["incluir B o D", "usar el saludo sin que el educador lo haya enseñado"],
        "Reconoce que eligió con criterio y practicó en un lugar seguro. Recuerda que el saludo lo enseña el educador tradicional.",
    ),
    reinforce="Practica en voz baja con un adulto la situación de recibir una visita.",
    extend="Escribe tres situaciones donde NO usarías un saludo de una lengua indígena y por qué.",
)

register(
    LR01, 4,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a anotar una palabra o relato sin decir que existe una sola forma correcta. Sirve para respetar que la misma lengua puede decirse o escribirse de más de una manera según la comunidad.",
    prior=["Sé qué es una variante.", "Sé anotar la fuente."],
    explain=[
        "Una variante es otra forma de decir o escribir lo mismo. En castellano también hay variantes: la fruta que en Chile llamamos «palta» se llama «aguacate» en otros países, y el «poroto» de Chile es «frijol» en otros. Ninguna es la correcta: cada lugar usa la suya. En las lenguas indígenas también hay variantes entre comunidades y entre libros.",
        "Un ejemplo es el nombre de la lengua mapuche, que se escribe «mapudungun» o «mapuzugun». Otro es Rapa Nui o Rapanui. Cuando registres una palabra, anota quién la dijo o escribió, de qué comunidad es y cómo la escribe. Así sabrás de dónde viene.",
        "Una ficha de registro tiene: palabra, significado, quién la dijo o escribió, comunidad y variante. Si dos fuentes dicen cosas distintas, anota las dos con sus nombres. No decidas cuál es mejor ni borres una. Si quieres saber más, pregunta por qué cada comunidad la usa así.",
    ],
    vocab=[("variante", "otra forma de decir o escribir lo mismo"), ("registro", "anotación que guarda un dato"), ("ficha", "hoja con datos ordenados"), ("comunidad", "grupo de personas que viven juntas"), ("fuente", "quien dijo o escribió el dato")],
    worked=[
        {"title": "Registrar dos formas", "problem": "Dos libros escriben el nombre de la lengua mapuche de forma distinta: uno «mapudungun» y otro «mapuzugun». Haz una ficha.", "steps": ["Anoto la primera forma con su libro.", "Anoto la segunda con su libro.", "No digo que una sea mejor."], "answer": "Dos fichas: «mapudungun» (libro 1) y «mapuzugun» (libro 2), sin decir cuál es mejor"},
        {"title": "Variantes en castellano", "problem": "Una compañera de otro país dice «aguacate» y tú dices «palta». ¿Quién tiene razón?", "steps": ["Las dos palabras nombran la misma fruta.", "Cada lugar usa la suya.", "Ambas son correctas."], "answer": "Las dos tienen razón porque son variantes"},
    ],
    mistakes=[
        {"wrong": "Decir que una variante es la correcta y la otra está mal.", "why": "Cada comunidad o libro usa su forma.", "fix": "Anota las dos con sus fuentes."},
        {"wrong": "Borrar una variante cuando dos fuentes dicen cosas distintas.", "why": "Pierdes información valiosa.", "fix": "Guarda las dos y pregunta por qué."},
    ],
    tiers={
        "recovery": [
            ex("Palta y aguacate son nombres de la misma fruta. ¿Son variantes?", "Sí", "Son dos formas de decir lo mismo."),
            ex("En una ficha de registro, ¿anotas quién dijo la palabra?", "Sí", "La fuente es un dato esencial."),
            ex("«Mapudungun» y «mapuzugun» son dos escrituras. ¿Una es un error?", "No", "Las dos son variantes válidas."),
        ],
        "understand": [
            ex("Poroto y frijol nombran la misma legumbre. ¿Cuál de las dos palabras usamos en Chile?", "Poroto", "En Chile decimos poroto."),
            ex("¿Por qué anotas la comunidad de quien dijo la palabra?", "Porque otras comunidades pueden decirla distinto", "Así sabes de dónde viene."),
            ex("Si dos fuentes dicen cosas distintas, ¿qué haces: anotar las dos o borrar una?", "Anotar las dos", "No se pierde información."),
        ],
        "apply": [
            ex("Ficha 1: «Rapa Nui, Don Luis». Ficha 2: «Rapanui, libro de la escuela». ¿Cuántas variantes se registran?", "2", "Hay dos escrituras."),
            ex("En la ficha «palabra: ko, significado: agua, quién: educadora Elena», ¿qué dato de la ficha es la fuente?", "La educadora Elena", "Es quien enseñó."),
            arith("Tienes 3 fichas de registro con 5 datos cada una. ¿Cuántos datos hay en total?", "3*5", "Se suman 5 datos tres veces."),
        ],
        "reason": [
            ex("Beto dice que «aguacate» está mal porque en Chile decimos «palta». ¿Qué le respondes?", "Que son variantes y ambas están bien", "Cada lugar usa la suya."),
            ex("Una compañera anota solo una escritura y borra la otra. ¿Qué error cometió?", "Perdió información al borrar una variante", "Debe anotar las dos."),
        ],
        "challenge": [
            ex("Lee: «Don Luis escribe Rapa Nui. El libro de la biblioteca escribe Rapanui». Haz una ficha con fuente de cada una.", "Rapa Nui (Don Luis); Rapanui (libro de la biblioteca)", "Cada variante con su fuente."),
            ex("Dos amigos discuten si es «palta» o «aguacate». Beto dice «las dos están bien». ¿Por qué?", "Porque cada lugar usa su variante", "Es la idea de variante."),
        ],
    },
    context=[ex("Tu curso escribe el nombre de la lengua en un cartel. Una niña dice que se escribe de otra forma. ¿Qué proponen?", "Anotar las dos formas con sus fuentes", "No se descarta ninguna.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Qué es una variante?", "Otra forma de decir o escribir lo mismo", "Es una forma distinta."),
        ex("¿Qué anotas junto a la palabra?", "Quién la dijo y su comunidad", "Es la fuente."),
        ex("¿Se dice que una variante es la correcta?", "No", "Ninguna se jerarquiza."),
    ],
    open_task=task(
        "Arma dos fichas de registro. Ficha 1: palabra «palta». Ficha 2: palabra «aguacate». Para cada una escribe significado (la misma fruta), quién la usa (Chile / otro país) y una frase de ejemplo. Después escribe una frase que explique por qué ninguna es incorrecta. Si puedes, pregunta a un adulto de tu casa si conoce otras variantes de una palabra.",
        "Ficha 1: palta, una fruta, la usan en Chile. Ficha 2: aguacate, la misma fruta, otros países. Ninguna es incorrecta porque cada lugar usa la suya.",
        ["completa dos fichas", "escribe la frase de explicación", "no dice que una está mal"],
        ["dos fichas", "una frase"],
        ["decir que una variante es incorrecta"],
        "Reconoce que aplicó la idea de variante con un ejemplo cercano. Para variantes de lenguas indígenas, la comunidad es la fuente.",
    ),
    reinforce="Pregunta a alguien de otra región o país cómo llama a un alimento y compara con el tuyo.",
    extend="Haz una tabla con tres alimentos y sus nombres en dos lugares distintos.",
)

register(
    LR01, 5,
    materials="Este cuaderno, lápiz y lápices de colores.",
    use="Aprenderé a crear un recurso pequeño que ayude a la lengua, diciendo quién me enseñó y sin reemplazar a las personas que la hablan. Sirve para aportar a la revitalización con respeto.",
    prior=["Sé hacer tarjetas de palabras.", "Sé citar la fuente y la autoría."],
    explain=[
        "Un recurso pequeño puede ser un cartel, una tarjeta o un cuadro de palabras. Su objetivo es ayudar a que otras personas recuerden o aprendan palabras de una lengua, sin cambiar nada. Debe llevar la palabra confirmada, su significado, el nombre de quien enseñó y tu nombre como autor o autora.",
        "Un recurso así nunca reemplaza a una persona que habla la lengua. Es un apoyo, no un profesor. Por eso, incluye una frase como: «Esta tarjeta no reemplaza a los hablantes: para aprender bien, escucha al educador o educadora de tu comunidad». Así dejas claro que quien sabe es la comunidad.",
        "Antes de mostrarlo, revísalo con la lista: ¿las letras son iguales al modelo?, ¿el significado es correcto?, ¿puse a quien me enseñó?, ¿dije que no reemplaza a los hablantes? Después muéstralo a quien te enseñó y pide su opinión.",
    ],
    vocab=[("recurso", "material que ayuda a aprender"), ("autoría", "quién hizo un recurso"), ("reemplazar", "ocupar el lugar de otra persona"), ("aportar", "ayudar con algo"), ("hablante", "persona que habla una lengua")],
    worked=[
        {"title": "Armar el recurso", "problem": "Arma una tarjeta con «mapu» (tierra) que cumpla la lista.", "steps": ["Escribo «mapu» como en el modelo.", "Escribo el significado: tierra.", "Escribo quién enseñó: el educador.", "Escribo mi nombre como autor.", "Agrego: «No reemplaza a los hablantes»."], "answer": "Tarjeta «mapu / tierra», fuente: el educador, autor: yo, con la frase de que no reemplaza a los hablantes"},
        {"title": "Revisar con la lista", "problem": "Tu tarjeta tiene la palabra y el significado, pero no tiene a quien enseñó. ¿Está lista?", "steps": ["Reviso la lista de cuatro preguntas.", "Falta la fuente.", "Todavía no está lista."], "answer": "No, falta la fuente"},
    ],
    mistakes=[
        {"wrong": "Hacer un recurso sin decir quién enseñó.", "why": "La fuente merece reconocimiento.", "fix": "Escribe el nombre de quien enseñó."},
        {"wrong": "Pensar que el recurso reemplaza al hablante.", "why": "Las lenguas se aprenden escuchando a quienes las hablan.", "fix": "Agrega la frase de que no reemplaza a los hablantes."},
    ],
    tiers={
        "recovery": [
            ex("Un recurso pequeño ayuda a aprender. ¿Una tarjeta de palabra es un recurso pequeño?", "Sí", "Ayuda a recordar palabras."),
            ex("Reemplazar es ocupar el lugar de otra persona. ¿Un recurso debe reemplazar a un hablante?", "No", "Solo es un apoyo."),
            ex("¿Qué escribes junto a la palabra: el significado o solo un dibujo?", "El significado", "Sin significado no sirve."),
        ],
        "understand": [
            ex("Las cuatro preguntas son: letras iguales al modelo, significado correcto, fuente puesta y frase de no reemplazo. ¿Cuántas son?", "4", "Se cuentan cuatro."),
            ex("¿Por qué pones tu nombre en la tarjeta?", "Para mostrar quién la hizo", "Es la autoría."),
            ex("¿Para qué sirve la frase «no reemplaza a los hablantes»?", "Para decir que quien sabe es la comunidad", "Reconoce a los hablantes."),
        ],
        "apply": [
            ex("Tarjeta A: «ko / agua / enseñó: Doña Elena / autor: Sol / no reemplaza a los hablantes». Tarjeta B: «ko / sol». ¿Cuál está bien hecha?", "A", "B tiene un error y le faltan datos."),
            arith("Un curso hace 6 tarjetas y cada una lleva 5 datos (palabra, significado, fuente, autor y frase). ¿Cuántos datos hay en total?", "6*5", "Se suman 5 datos seis veces."),
            ex("Arma con palabras la tarjeta de «kuyen»: palabra, significado y fuente. Escribe: «kuyen / ___ / enseñó: ___». Usa luna y el educador.", "kuyen / luna / enseñó: el educador", "Kuyen significa luna."),
        ],
        "reason": [
            ex("Ema dice que su tarjeta es suficiente para aprender mapuzugun. ¿Qué le dices?", "Que la lengua se aprende escuchando a los hablantes", "El recurso es solo apoyo."),
            ex("Una tarjeta tiene «antü / luna». ¿Qué error tiene?", "El significado: antü es sol", "Antü es sol."),
        ],
        "challenge": [
            ex("Tres compañeros: Luis hizo su tarjeta con fuente y frase de no reemplazo, Beto sin fuente, Camila con significado equivocado. ¿Quién cumplió mejor?", "Luis", "Es el único con todo."),
            ex("Tu tarjeta está lista. ¿A quién se la muestras primero para que la revise: a quien te enseñó o a un compañero?", "A quien me enseñó", "Es la fuente."),
        ],
    },
    context=[ex("Quieres regalar tu tarjeta de «mari mari» al curso. ¿Qué frase agregas para cuidar la lengua?", "Esta tarjeta no reemplaza a los hablantes", "Reconoce a quienes hablan la lengua.")],
    selfcheck=[
        ex("¿Qué cuatro cosas lleva tu recurso?", "Palabra, significado, fuente y autoría", "Más la frase de no reemplazo."),
        ex("¿Reemplaza un recurso a un hablante?", "No", "Solo es un apoyo."),
        ex("¿A quién muestras tu recurso al terminar?", "A quien me enseñó", "Para que lo revise."),
    ],
    open_task=task(
        "Haz un cartel pequeño con dos palabras confirmadas de esta lista: mari mari (saludo), mapu (tierra), ko (agua), antü (sol), kuyen (luna). Para cada palabra escribe: la palabra, el significado y un dibujo. Abajo escribe: «Enseñó: el educador/a tradicional (nombre). Autor/a: tu nombre. Este cartel no reemplaza a los hablantes». Muéstralo a quien te enseñó para que lo revise.",
        "Cartel: «ko / agua» con una gota y «antü / sol» con un sol. Enseñó: el educador (nombre). Autor: yo. Este cartel no reemplaza a los hablantes.",
        ["dos palabras copiadas sin cambiar", "significados correctos", "dibujos", "fuente, autoría y frase de no reemplazo"],
        ["cartel terminado"],
        ["cambiar letras", "olvidar la fuente", "decir que reemplaza a un hablante"],
        "Reconoce el cartel y que lo mostró a quien lo enseñó. La escritura la confirma el educador.",
    ),
    reinforce="Haz otra tarjeta con una palabra diferente de la lista.",
    extend="Prepara una frase de dos líneas para invitar a otros a escuchar a los hablantes de una lengua.",
)
