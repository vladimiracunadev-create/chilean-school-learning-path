"""Student material for 2.º básico Música, OA 03 (escucha abundante de músicas diversas) y OA 04 (canto al unísono y percusión)."""
from __future__ import annotations

import re

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA3, OA4 = "MU02 OA 03", "MU02 OA 04"

TA, TT, SIL = "TA", "ti-ti", "SIL"
LEY = "TA = 1 sonido en 1 pulso; ti-ti = 2 sonidos rápidos en 1 pulso; SIL = 1 pulso de silencio"
SILABAS = "Las sílabas se cuentan como se escriben, separadas con guiones; cada sílaba es un golpe de palmas."


def P(*tokens: str) -> str:
    return " – ".join(tokens)


def sounds(*tokens: str) -> int:
    return sum({TA: 1, TT: 2, SIL: 0}[t] for t in tokens)


def S(text: str) -> int:
    """Syllables of a hyphenated phrase: each hyphen-separated piece is one syllable."""
    return len([piece for piece in re.split(r"[-\s]+", text.strip()) if piece])


def plain(text: str) -> str:
    return text.replace("-", "")


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, tk, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[dict(title=t, problem=p, steps=s, answer=a) for t, p, s, a in worked],
        mistakes=[dict(wrong=w, why=y, fix=f) for w, y, f in mistakes],
        tiers=dict(recovery=R, understand=C, apply=A, reason=Z, challenge=D),
        context=ctx, selfcheck=sc, open_task=task(*tk), reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- OA 03 · clase 1
L(
    OA3, 1,
    "Lápiz y papel. Las tres músicas de trabajo (A, B y C) están descritas por escrito y son ficticias; un adulto puede imitarlas con la voz, palmas y objetos de la casa.",
    "Aprenderé a escuchar primero lo que se oye y después a ponerle nombre. Sirve para disfrutar músicas de cualquier lugar y tiempo sin pensar que unas valen más que otras.",
    ["Sé decir si un sonido es rápido o lento.", "Sé decir si un sonido es fuerte o suave.", "Sé que hay músicas de muchos lugares."],
    [
        "Existe música en todas partes del mundo y de todos los tiempos. Para escucharla bien, primero describe lo que oyes: si es rápida o lenta, fuerte o suave, qué instrumentos o voces suenan y si hay una parte que se repite. Solo después se le pone nombre al tipo de música.",
        "Un nombre como «rock» o «folclor» es una etiqueta. Una etiqueta sirve para ordenar, pero no reemplaza escuchar. Dos músicas con la misma etiqueta pueden sonar muy distinto. Y ninguna música es mejor que otra solo por su origen o por la época en que nació.",
        "Una buena escucha tiene tres pasos: escuchar sin hablar, anotar dos rasgos audibles y, al final, decir de dónde viene la música si ya lo sabes. Si no lo sabes, no pasa nada: se pregunta o se investiga después.",
    ],
    [("describir", "decir cómo suena algo"), ("etiqueta", "nombre que se da a un tipo de música"), ("rasgo audible", "algo que se puede oír, como rápido o con tambor"), ("origen", "lugar y tiempo donde nació una música"), ("escucha atenta", "escuchar con silencio y con interés")],
    [
        ("Describir antes de etiquetar", "La música A suena así: una flauta sola, lenta y suave. ¿Cuáles son dos rasgos audibles?", ["Rasgo 1: el instrumento es una flauta sola.", "Rasgo 2: la música es lenta y suave.", "Todavía no le ponemos nombre de estilo."], "Flauta sola y lenta y suave"),
        ("Distinguir rasgo y etiqueta", "¿«Suena fuerte con batería» es un rasgo o una etiqueta? ¿Y «es rock»?", ["«Fuerte» y «con batería» se pueden oír: es un rasgo.", "«Rock» es el nombre de un tipo de música: es una etiqueta."], "El primero es un rasgo y el segundo una etiqueta"),
    ],
    [
        ("Decir «esa música no vale» solo porque es de otro lugar.", "Ninguna música vale menos por su origen.", "Describe qué se oye y pregunta de dónde viene."),
        ("Poner una etiqueta sin haber escuchado.", "La etiqueta no dice cómo suena.", "Escucha primero y anota dos rasgos audibles."),
    ],
    [
        ex("¿Qué haces primero al escuchar una música nueva: describir lo que oyes o ponerle un nombre?", "Describir lo que oigo", "Primero se escucha; el nombre se pone después."),
        ex("«Suena rápida y con tambores» ¿es un rasgo audible o una etiqueta?", "Un rasgo audible", "Rápida y con tambores se pueden oír."),
        ex("¿Una música es mejor porque viene de un lugar famoso? Responde sí o no.", "No", "El origen no hace mejor o peor a una música."),
    ],
    [
        ex("La música B suena así: voces y tambor, rápido, fuerte, y un coro responde a un solista. Escribe tres rasgos audibles.", "Voces y tambor, rápido y fuerte; también el coro que responde", "Son los datos que se pueden oír en la descripción."),
        ex("Une cada frase con rasgo o etiqueta: (a) «Es folclor» (b) «Tiene un coro que responde».", "(a) etiqueta; (b) rasgo", "El folclor es un nombre del tipo de música; el coro se puede oír."),
        ex("La música C suena así: guitarra eléctrica y batería, fuerte y rápida. ¿Qué instrumentos se escuchan?", "Guitarra eléctrica y batería", "Se nombran en la descripción."),
    ],
    [
        ex("La música A es una flauta sola, lenta y suave. La música B son voces y tambor, rápido y fuerte. ¿Cuál es más rápida?", "La música B", "B se describe como rápida y A como lenta."),
        ex("Anota dos rasgos audibles de una música que suena así: una guitarra suave que repite una melodía corta.", "Guitarra suave y melodía corta que se repite", "Son datos que se oyen en la descripción."),
        ex("Pía dice «esta música es de la ciudad». ¿Esa frase es un rasgo audible o un dato de origen?", "Un dato de origen", "Dónde nació una música no se oye directamente."),
    ],
    [
        ex("Mateo dice: «es del campo, entonces es aburrida». ¿Qué error comete?", "Juzga por el origen y no por lo que oyó", "Hay que describir primero lo que suena."),
        ex("Dos músicas distintas, una suave con flauta y otra fuerte con guitarra eléctrica, llevan la misma etiqueta «popular». ¿Eso significa que suenan igual?", "No", "Una etiqueta junta muchas músicas que pueden sonar muy distinto."),
    ],
    [
        ex("Tienes las músicas A (flauta sola, lenta y suave) y B (voces y tambor, rápido y fuerte). Escribe un rasgo que las diferencie y uno que sea de A solamente.", "Por ejemplo: A es lenta y B es rápida; la flauta sola es de A", "Se comparan velocidad e instrumentos."),
        ex("Quieres anotar una música de otro país sin saber su nombre. ¿Qué puedes escribir de todas maneras?", "Dos rasgos audibles", "Siempre se puede describir lo que se oye."),
    ],
    [ex("En una fiesta familiar suena una música que no conoces. Alguien dice «qué mala». ¿Qué le propones decir antes?", "Que describa cómo suena: si es rápida o lenta, fuerte o suave y qué instrumentos oye", "Describir con rasgos audibles permite escuchar sin prejuicio.")],
    [ex("¿Qué se hace primero: etiquetar o describir?", "Describir", "Se escucha antes de ponerle nombre."), ex("Menciona un rasgo audible.", "Por ejemplo: lenta", "Es algo que se puede oír."), ex("¿Una música de otro lugar es peor?", "No", "Ninguna vale menos por su origen.")],
    (
        "Elige un sonido o una canción corta que haya en tu casa (puede ser cantada por alguien de tu familia). Si no tienes, usa la música A: una flauta sola, lenta y suave. Escucha en silencio y escribe dos rasgos audibles. Después escribe el nombre del tipo de música solo si lo sabes. Termina diciendo una cosa que te llamó la atención.",
        "Música A: la flauta suena sola, lenta y suave. No sé qué tipo de música es, y lo pregunto después. Me llamó la atención que se oye muy tranquila.",
        ["escucha antes de hablar", "anota dos rasgos audibles", "separa rasgo de etiqueta"],
        ["escucha atenta", "dos rasgos escritos", "frase final"],
        ["poner una etiqueta como si fuera un rasgo", "juzgar la música por su origen"],
        "Reconoce los rasgos audibles; si usa solo una etiqueta, pregunta qué oyó para decir eso.",
    ),
    "Escucha un sonido de tu casa y anota dos rasgos audibles.",
    "Escribe una lista de cuatro rasgos audibles que podrías usar con cualquier música.",
)

# ---------------------------------------------------------------- OA 03 · clase 2
L(
    OA3, 2,
    "Lápiz, papel y una línea de tiempo dibujada con tres marcas: «hace muchos siglos», «siglo XVIII» y «siglo XIX». Las piezas se describen por escrito; no hace falta escuchar grabaciones.",
    "Aprenderé qué es la música de tradición escrita (docta) y a conocer tres ejemplos: danzas medievales, el Cuaderno de Ana Magdalena Bach y el ballet «Cascanueces». Sirve para escuchar música muy antigua con curiosidad.",
    ["Sé que una música puede venir de otro tiempo.", "Sé qué es una sección y un pulso."],
    [
        "La música de tradición escrita se anota con símbolos en un papel llamado partitura. Así, personas de distintos lugares y tiempos pueden tocar lo mismo leyendo. A este tipo de música también se le llama docta. Las piezas las escribe un compositor, aunque de las danzas medievales muchas veces no se conoce el nombre de quien las creó.",
        "Tres ejemplos: las danzas medievales, hechas para bailar en Europa hace muchos siglos, con flautas, tambores y cuerdas. El Cuaderno de Ana Magdalena Bach, un libro de piezas breves para teclado, de hace unos 300 años (siglo XVIII). Y el ballet «Cascanueces», del compositor ruso Piotr Chaikovski, del siglo XIX: un ballet cuenta una historia con baile y música, sin palabras.",
        "Aunque se escriban, estas músicas también se disfrutan con el oído. Cuando las escuches, describe primero: lento o rápido, qué instrumentos, si hay secciones que regresan. Muchas de estas piezas son cortas y se pueden volver a escuchar.",
    ],
    [("partitura", "papel donde se escribe una música con símbolos"), ("compositor", "persona que crea una música"), ("docta", "música de tradición escrita"), ("danza medieval", "música para bailar de hace muchos siglos"), ("ballet", "historia contada con baile y música")],
    [
        ("Ordenar en el tiempo", "Ordena de la más antigua a la más reciente: Cuaderno de Ana Magdalena Bach (siglo XVIII), danzas medievales (hace muchos siglos), «Cascanueces» (siglo XIX).", ["Las danzas medievales son de hace muchos siglos: las más antiguas.", "El siglo XVIII viene antes que el XIX.", "Orden: danzas, Bach, Cascanueces."], "Danzas medievales, Cuaderno de Ana Magdalena Bach, Cascanueces"),
        ("Reconocer qué es un ballet", "¿Un ballet usa palabras o baile para contar una historia?", ["Un ballet es una historia contada con baile y música.", "No lleva palabras."], "Con baile y música, sin palabras"),
    ],
    [
        ("Pensar que la música docta es solo para personas adultas.", "Hay piezas breves que se pueden disfrutar a cualquier edad.", "Escucha una pieza corta y describe lo que oyes."),
        ("Creer que la partitura es la música misma.", "La partitura es solo el papel con símbolos.", "La música se completa cuando se toca."),
    ],
    [
        ex("¿En qué se escribe la música de tradición escrita?", "En una partitura", "La partitura es el papel con símbolos musicales."),
        ex("¿Cómo se llama la persona que crea una música?", "Compositor", "El compositor escribe y crea las piezas."),
        ex("Las danzas medievales, ¿son de hace muchos siglos o de este año?", "De hace muchos siglos", "Medieval se refiere a la Edad Media, hace siglos."),
    ],
    [
        ex("¿Qué es el «Cascanueces»: un ballet o un cuento sin música?", "Un ballet", "Es una historia contada con baile y música."),
        ex("El Cuaderno de Ana Magdalena Bach es un libro de piezas breves. ¿Es de una sola pieza larga o de varias piezas cortas?", "De varias piezas cortas", "Es un cuaderno, es decir, un libro con varias piezas breves."),
        ex("¿De qué país era el compositor del «Cascanueces», Piotr Chaikovski?", "Rusia", "Chaikovski fue un compositor ruso."),
    ],
    [
        ex("Ordena de la más reciente a la más antigua: «Cascanueces» (siglo XIX), danzas medievales (hace muchos siglos), Cuaderno de Ana Magdalena Bach (siglo XVIII).", "Cascanueces, Cuaderno de Ana Magdalena Bach, danzas medievales", "El siglo XIX es el más cercano a hoy y las danzas medievales son las más lejanas."),
        ex("Une cada obra con su descripción. Obras: danzas medievales, ballet «Cascanueces». Descripciones: historia contada con baile; música para bailar de hace siglos.", "Danzas medievales: música para bailar de hace siglos; Cascanueces: historia contada con baile", "Cada obra encaja con su descripción."),
        ex("Un compositor escribe su música en una partitura. ¿La partitura es el papel o el sonido?", "El papel", "La partitura es la hoja con símbolos; el sonido ocurre al tocar."),
    ],
    [
        ex("Ana dice: «Para tocar la misma música en dos países, basta tener la partitura». ¿Por qué es útil la partitura?", "Porque anota la música con símbolos que todos pueden leer", "Permite que personas distantes toquen lo mismo."),
        ex("Cuenta: si el Cuaderno tiene piezas de 2 minutos y escuchas 3 de ellas, ¿cuánto escuchaste?", "6 minutos", "2 + 2 + 2 = 6 minutos."),
    ],
    [
        ex("Una pieza dura 3 minutos y escuchas 4 veces la misma. ¿Cuántos minutos escuchaste en total?", "12 minutos", "3 × 4 = 12 minutos."),
        ex("En la línea de tiempo, ¿qué va más a la izquierda: «siglo XIX» o «hace muchos siglos»?", "Hace muchos siglos", "Lo más antiguo va primero, a la izquierda."),
    ],
    [ex("Quieres describir una danza medieval para bailar con tu curso. Dices: «Es para bailar, de hace muchos siglos». Agrega un rasgo audible que podrías escuchar.", "Por ejemplo: suenan flautas y tambores; tiene un pulso claro", "Un rasgo audible es algo que se oye: instrumentos, pulso, velocidad.")],
    [ex("¿Qué es una partitura?", "Papel donde se escribe una música con símbolos", "Es la forma de anotar la música."), ex("¿Un ballet es una música para cantar o para bailar y contar una historia?", "Para bailar y contar una historia", "El ballet usa baile y música sin palabras."), ex("¿Quién creó el Cuaderno de piezas que se llama de Ana Magdalena Bach: un compositor o un pintor?", "Un compositor", "Las piezas son música de compositores.")],
    (
        "Dibuja una línea de tiempo con tres marcas («hace muchos siglos», «siglo XVIII» y «siglo XIX») y ubica en ella: danzas medievales, Cuaderno de Ana Magdalena Bach y «Cascanueces». Debajo de cada una escribe un rasgo: «para bailar», «piezas breves para teclado» e «historia con baile». Si puedes, canta o aplaude un pulso lento y otro rápido para imaginar cada música.",
        "Hace muchos siglos: danzas medievales, para bailar. Siglo XVIII: Cuaderno de Ana Magdalena Bach, piezas breves para teclado. Siglo XIX: Cascanueces, historia con baile.",
        ["ubica las tres músicas en el orden correcto", "escribe un rasgo para cada una", "mantiene separados los nombres y las épocas"],
        ["línea de tiempo dibujada", "tres frases cortas"],
        ["ordenar al revés", "confundir ballet con canción"],
        "Reconoce el orden correcto y pide que explique con sus palabras qué es una partitura.",
    ),
    "Cuenta a alguien de tu casa qué es una partitura y un ballet.",
    "Investiga con un adulto otra música de tradición escrita y agrégala a tu línea de tiempo.",
)

# ---------------------------------------------------------------- OA 03 · clase 3
V1 = "a-pren-do de ti, tú de mí"
V2 = "can-ta con-mi-go hoy"
L(
    OA3, 3,
    f"Lápiz y papel. {SILABAS} Versos rítmicos de trabajo: «{V1}» y «{V2}». Los instrumentos mencionados se describen por escrito.",
    "Aprenderé que en las tradiciones orales la música se aprende escuchando y repitiendo, sin partitura. Conoceré folclor, rondas, versos rítmicos y música de pueblos originarios. Sirve para valorar la música que viene de nuestra gente.",
    ["Sé repetir una frase que me enseñan.", "Sé contar sílabas con las palmas."],
    [
        "En las tradiciones orales la música pasa de persona en persona hablando, cantando y tocando. No se anota en papel: se aprende escuchando y repitiendo. Así llegan hasta nosotros el folclor, las rondas, los juegos de palmas y los versos rítmicos.",
        "La cueca es el baile nacional de Chile, y la gente de distintas zonas la baila con sus propios estilos. Los pueblos originarios también tienen sus músicas. Por ejemplo, el pueblo mapuche usa instrumentos como el kultrún (un tambor) y la trutruka (una trompeta larga). La forma tradicional de esas músicas la enseñan las personas que las cuidan, como las y los educadores tradicionales y las comunidades; aquí solo las conocemos de manera general y con respeto.",
        "Un verso rítmico tiene sílabas que se marcan con palmas. Para contarlas, golpea una palma por sílaba. Por ejemplo, en «can-ta con-mi-go hoy» hay 6 sílabas: can, ta, con, mi, go, hoy.",
    ],
    [("tradición oral", "música que se aprende de boca en boca"), ("folclor", "cultura y música propias de la gente de un lugar"), ("ronda", "canto de juego en círculo"), ("verso rítmico", "frase con ritmo que se marca con palmas"), ("pueblo originario", "pueblo que vive en un territorio desde antes de la llegada de otros")],
    [
        ("Contar un verso", f"¿Cuántas sílabas tiene «{V2}»?", ["Separo y cuento: can, ta, con, mi, go, hoy.", f"Son {S(V2)}."], f"{S(V2)} sílabas"),
        ("Sílabas de otro verso", f"¿Cuántas palmas das en «{V1}»?", ["Una palma por sílaba: a, pren, do, de, ti, tú, de, mí.", f"Son {S(V1)} sílabas."], f"{S(V1)} palmas"),
    ],
    [
        ("Pensar que la música oral «no existe» porque no tiene partitura.", "La música oral vive en las personas que la cantan.", "Se aprende repitiendo y escuchando."),
        ("Inventar cómo se toca un instrumento de un pueblo originario.", "Las formas tradicionales las enseña la comunidad.", "Aprende lo que se sabe con certeza y pregunta al educador tradicional."),
    ],
    [
        ex("En una tradición oral, ¿la música se aprende escuchando y repitiendo o leyendo una partitura?", "Escuchando y repitiendo", "No necesita papel: se pasa de persona en persona."),
        ex("¿Cómo se llama el baile nacional de Chile?", "La cueca", "La cueca es la danza nacional de nuestro país."),
        ex("El kultrún, ¿es un tambor o una flauta?", "Un tambor", "El kultrún es un tambor del pueblo mapuche."),
    ],
    [
        ex(f"Cuenta las sílabas de «{V2}».", str(S(V2)), "Se cuenta una por cada trozo separado con guion."),
        ex("Una ronda es un canto de juego en círculo. ¿Es de tradición oral o escrita en su origen?", "Oral", "Las rondas se aprenden cantándolas con otros."),
        ex("La trutruka es una trompeta larga. ¿De qué pueblo originario de Chile es un instrumento tradicional?", "Del pueblo mapuche", "La trutruka es un instrumento mapuche."),
    ],
    [
        ex(f"Cuenta las sílabas de «{V1}».", str(S(V1)), "Hay 3 en la primera palabra y una en cada una de las otras cinco."),
        arith(f"Das una palma por sílaba. Cantas «{V2}» dos veces seguidas. ¿Cuántas palmas das?", f"{S(V2)}*2", "Se repite el verso: 6 palmas más 6 palmas.", " palmas"),
        ex("Une cada tradición oral con su descripción. Tradiciones: ronda, cueca. Descripciones: baile nacional de Chile; canto de juego en círculo.", "Ronda: canto de juego en círculo; cueca: baile nacional de Chile", "Cada nombre corresponde a su descripción."),
    ],
    [
        ex("Rosa dice: «Si no hay partitura, no hay música». ¿Qué le respondes?", "Que la música oral existe en quienes la cantan y la pasan de persona en persona", "La música se transmite por la voz y el cuerpo."),
        ex("Tu abuela te enseña una canción que aprendió de su mamá. ¿Es tradición oral? ¿Por qué?", "Sí; se pasó de persona en persona sin partitura", "Una música aprendida escuchando y repitiendo es oral."),
    ],
    [
        ex(f"Compara «{V1}» y «{V2}». ¿Cuál tiene más sílabas y por cuántas?", f"El primero, por {S(V1) - S(V2)}", "Uno tiene 8 y el otro 6; 8 − 6 = 2."),
        ex("Quieres que el verso «can-ta con-mi-go hoy» ocupe 6 pulsos, una sílaba por pulso. Luego un silencio de 2 pulsos. ¿Cuántos pulsos dura todo?", "8", "6 pulsos de sílabas más 2 de silencio: 8."),
    ],
    [ex("Un niño dice que no sabe cantar una ronda porque no tiene el papel. ¿Cómo puede aprenderla?", "Escuchando a otros y repitiendo", "La tradición oral se aprende con la voz de otros.")],
    [ex("¿Una tradición oral se escribe en partitura?", "No necesariamente; se aprende escuchando", "Se pasa de persona en persona."), ex("Menciona un instrumento mapuche.", "El kultrún", "El kultrún es un tambor mapuche."), ex(f"¿Cuántas sílabas tiene «{V2}»?", str(S(V2)), "Can, ta, con, mi, go, hoy.")],
    (
        f"Aprende de memoria el verso «{V2}». Dilo con palmas, una palma por sílaba, cuatro veces seguidas. Pide a alguien de tu casa que te enseñe un juego de palmas, canto o ronda que conozca. Anota su nombre (solo el primer nombre o «mi abuela», «mi tío») y de qué trata. Recuerda: lo que no sabes de una música de pueblo originario, se lo preguntas a un educador tradicional.",
        f"Dije «{V2}» con 6 palmas, 4 veces: 24 palmas. Mi abuela me enseñó una ronda; se llama «la ronda del sol» y trata del día.",
        ["dice el verso con una palma por sílaba", "cuenta sus palmas con cuidado", "anota de dónde aprendió la tradición oral sin dar datos privados"],
        ["interpretación con palmas", "registro escrito", "conteo"],
        ["contar mal las sílabas", "inventar cosas sobre música de pueblos originarios"],
        "Reconoce el esfuerzo de aprender de otro y pide que explique cómo aprendió; si falta una palma, repite despacio.",
    ),
    "Aprende una ronda o un juego de palmas de alguien de tu familia y enséñala a otra persona.",
    "Escribe un verso rítmico propio de 6 sílabas y compruébalo con palmas.",
)

# ---------------------------------------------------------------- OA 03 · clase 4
L(
    OA3, 4,
    "Lápiz y papel. Las músicas se describen por escrito. Los instrumentos mencionados son guitarra eléctrica, bajo, batería, piano y voz. Un adulto puede dar golpes con las palmas para marcar el pulso.",
    "Aprenderé qué es la música popular (jazz, rock, fusión, música infantil y de películas) y a reconocer sus rasgos. Sirve para escuchar con atención las músicas que oímos todos los días.",
    ["Sé nombrar instrumentos como guitarra y batería.", "Sé describir una música con dos rasgos."],
    [
        "La música popular es la que escuchamos en la radio, en películas, en fiestas y en la calle. Hay muchos estilos. El jazz nació en Estados Unidos a comienzos del siglo XX y se destaca por la improvisación: los músicos inventan al tocar. El rock suele usar guitarra eléctrica, bajo y batería con fuerza.",
        "La fusión mezcla músicas de distintos lugares o estilos, como un ritmo tradicional con guitarra eléctrica. La música infantil tiene letras simples y partes que se repiten. La música de películas ayuda a contar la historia: puede dar miedo, alegría o suspenso.",
        "Para escuchar música popular, describe: ¿qué instrumentos suenan?, ¿es fuerte o suave?, ¿hay una parte que se repite? Los estilos se mezclan, así que una misma música puede tener rasgos de varios.",
    ],
    [("jazz", "estilo que usa mucho la improvisación"), ("rock", "estilo con guitarra eléctrica, bajo y batería"), ("fusión", "mezcla de estilos o ritmos"), ("improvisar", "inventar música mientras se toca"), ("música de película", "música que ayuda a contar la historia")],
    [
        ("Reconocer improvisación", "Un grupo toca y cada músico inventa una parte nueva en el momento. ¿Qué rasgo del jazz muestra?", ["Inventar mientras se toca es improvisar.", "El jazz se destaca por eso."], "La improvisación"),
        ("Reconocer instrumentos del rock", "Una música usa guitarra eléctrica, bajo y batería con fuerza. ¿Qué estilo se parece?", ["Guitarra eléctrica, bajo y batería son los tres instrumentos típicos del rock.", "Además suena con fuerza, como se describe."], "Rock"),
    ],
    [
        ("Pensar que cada música tiene un solo estilo.", "Los estilos se mezclan.", "Describe los rasgos y di a qué estilos se parece."),
        ("Creer que la música infantil es «más fácil» y no vale la pena escucharla.", "Tiene rasgos que se pueden describir y disfrutar.", "Escucha y anota dos rasgos."),
    ],
    [
        ex("¿Cómo se llama inventar música mientras se toca?", "Improvisar", "Improvisar es crear en el momento."),
        ex("El rock usa guitarra eléctrica, bajo y... ¿cuál otro instrumento: batería o flauta dulce?", "Batería", "Esos tres forman el sonido típico del rock."),
        ex("La música de una película que da miedo, ¿ayuda a contar la historia o la detiene?", "Ayuda a contar la historia", "La música crea emociones que acompañan lo que se ve."),
    ],
    [
        ex("Una música mezcla un ritmo tradicional de tambor con guitarra eléctrica. ¿Cómo se llama esa mezcla?", "Fusión", "Fusión es juntar estilos."),
        ex("Una canción infantil tiene letra simple y un estribillo que se repite. ¿Qué rasgos son esos: de música infantil o de la improvisación del jazz?", "De música infantil", "Letra simple y repetición son rasgos infantiles."),
        ex("En el jazz, ¿se improvisa o todo está siempre igual?", "Se improvisa", "La improvisación es muy importante en el jazz."),
    ],
    [
        ex("Descripción: piano y bajo tocan suave, y un músico inventa una melodía distinta cada vez. ¿A qué estilo se parece?", "Al jazz", "Hay improvisación con instrumentos y suavidad."),
        ex("Una película muestra una persecución. La música es rápida, fuerte y con sonidos que se repiten. ¿Qué efecto produce?", "Da emoción y tensión", "Rápido y fuerte aumenta la tensión de lo que se ve."),
        ex("Una niña dice «el rock es solo ruido». ¿Qué puedes decirle usando rasgos audibles?", "Que el rock tiene pulso fuerte, guitarra eléctrica y partes que se repiten", "Se pueden describir sus rasgos con lo que se oye."),
    ],
    [
        ex("Un grupo toca un ritmo del campo chileno con guitarra eléctrica. ¿Qué estilo lo describe mejor: fusión o ballet?", "Fusión", "Mezcla un ritmo tradicional con instrumentos modernos."),
        ex("En una escena alegre, la música cambia de pronto a lenta y grave. ¿Qué podría estar pasando en la historia?", "Algo triste o misterioso", "El cambio de música anuncia otro ánimo."),
    ],
    [
        ex("Tienes 20 minutos para escuchar. Escuchas 3 músicas de 4 minutos cada una. ¿Cuántos minutos te sobran?", "8", "3 × 4 = 12 minutos; 20 − 12 = 8."),
        ex("Una canción infantil tiene 4 estribillos de 8 pulsos cada uno. ¿Cuántos pulsos de estribillo hay en total?", "32", "4 × 8 = 32 pulsos."),
    ],
    [ex("En tu casa suena una canción infantil y otra de película. ¿Qué rasgo puedes comparar para saber cuál es más lenta?", "La velocidad", "La velocidad es un rasgo audible que se puede comparar.")],
    [ex("¿Qué es la fusión en música?", "Una mezcla de estilos", "Junta rasgos de distintas músicas."), ex("¿Qué se destaca en el jazz?", "La improvisación", "Se inventa mientras se toca."), ex("¿Para qué sirve la música de una película?", "Para ayudar a contar la historia", "Crea el ánimo de cada escena.")],
    (
        "Elige una música popular que conozcas (infantil, de película o de un estilo que se escuche en tu casa). Si no encuentras, usa esta: una canción infantil con letra simple y estribillo repetido. Escribe: nombre del estilo o de la música, dos rasgos audibles y qué emoción da. Marca el pulso con las palmas durante 8 pulsos y di si es rápida o lenta.",
        "Música: canción infantil. Rasgos: letra simple y estribillo repetido. Da alegría. El pulso fue medio rápido.",
        ["nombra una música popular o la que se propone", "da dos rasgos audibles", "marca 8 pulsos y dice si es rápida o lenta"],
        ["registro escrito", "demostración de pulso"],
        ["dar solo opinión sin rasgos", "confundir estilo con instrumento"],
        "Reconoce los rasgos audibles y pregunta qué instrumento o voz escuchó con más claridad.",
    ),
    "Pide a alguien de tu casa que te cante una canción que le guste y anota un rasgo audible.",
    "Compara dos músicas populares usando tres rasgos: velocidad, fuerza e instrumentos.",
)

# ---------------------------------------------------------------- OA 03 · clase 5
BIT_TXT = "Bitácora de ejemplo: 1) danza medieval, escrita, flauta y tambor; 2) ronda, oral, voces de niños; 3) canción infantil, popular, voz y guitarra; 4) pieza breve para teclado, escrita, teclado; 5) cueca, oral, guitarra y palmas; 6) música de película, popular, orquesta."
L(
    OA3, 5,
    "Lápiz y una hoja para hacer una tabla de 20 filas con cuatro columnas: número, nombre o descripción, tradición (escrita, oral o popular) y un rasgo audible. Se propone una bitácora de ejemplo con 6 filas: " + BIT_TXT,
    "Aprenderé a llevar una bitácora para registrar 20 músicas escuchadas durante el año, de tradición escrita, oral y popular. Sirve para escuchar con constancia y para ver cuánto hemos escuchado.",
    ["Sé describir una música con un rasgo audible.", "Sé contar hasta 20.", "Sé reconocer las tres tradiciones."],
    [
        "Una bitácora es un cuaderno donde anotas lo que haces. En música, anotas cada escucha: número, nombre o descripción, tradición (escrita, oral o popular) y un rasgo audible. Durante el año escucharás 20 músicas o más; para lograrlo, escucha de a poco, por ejemplo una o dos por semana.",
        "Para que la bitácora sea justa, mezcla las tradiciones. No hace falta que sean exactamente iguales, pero conviene que ninguna se quede en cero. Con 20 escuchas, un reparto posible es 7 escritas, 7 orales y 6 populares. Las músicas son cortas, de unos pocos minutos.",
        "Anota con tus palabras, sin copiar textos ni letras de canciones. Si no sabes el nombre exacto, escribe una descripción: «canción de cuna que cantaba una tía». No anotes datos privados como direcciones o apellidos.",
    ],
    [("bitácora", "cuaderno donde se anotan escuchas"), ("registro", "anotación de lo que escuchas"), ("tradición", "escrita, oral o popular"), ("rasgo", "algo que se oye"), ("constancia", "hacer algo poco a poco, de manera regular")],
    [
        ("Contar lo que falta", "Ya registraste 6 escuchas. La meta del año es 20. ¿Cuántas faltan?", ["Se restan las 6 que hay de las 20 de la meta.", "20 − 6 = 14."], "14 escuchas"),
        ("Revisar el reparto", f"{BIT_TXT} ¿Está balanceada entre escritas, orales y populares?", ["Cuento cada tradición.", "Las tres tienen 2."], "Sí, está balanceada"),
    ],
    [
        ("Anotar solo canciones de una misma tradición.", "Se pierde la variedad.", "Mezcla escrita, oral y popular."),
        ("Copiar la letra completa de una canción.", "No hace falta y puede infringir derechos de autor.", "Anota solo el nombre o una descripción y un rasgo audible."),
    ],
    [
        ex("La meta es escuchar 20 músicas. Ya llevas 10. ¿Cuántas faltan?", "10", "20 − 10 = 10."),
        ex("En una bitácora, ¿anotas la dirección de tu casa? Responde sí o no.", "No", "No se anotan datos privados."),
        ex("La cueca es de tradición oral. ¿En qué columna de tradición la anotas?", "Oral", "La cueca se transmite por práctica y tradición."),
    ],
    [
        ex(f"{BIT_TXT} ¿Cuántas escuchas son de tradición escrita?", "2", "Son la 1 (danza medieval) y la 4 (pieza para teclado)."),
        ex(f"{BIT_TXT} ¿Qué número de escucha es la cueca?", "5", "La fila 5 es la cueca."),
        arith("Si escuchas 2 músicas por semana desde cero, ¿cuántas semanas necesitas para llegar a 20?", "20//2", "Se reparten las 20 escuchas en grupos de 2 por semana.", " semanas"),
    ],
    [
        ex(f"{BIT_TXT} ¿Cuántas escuchas hay de tradición popular?", "2", "Son la 3 (canción infantil) y la 6 (música de película)."),
        ex(f"{BIT_TXT} ¿Cuántas escuchas tienen una voz o voces entre sus instrumentos?", "2", "Son la 2 (voces de niños) y la 3 (voz y guitarra)."),
        ex("La meta es 20. Llevas 6. Si escuchas 2 músicas por semana, ¿cuántas semanas necesitas para llegar a 20?", "7", "Faltan 14 escuchas; 14 ÷ 2 = 7 semanas."),
    ],
    [
        ex("Un reparto de 20 escuchas es 7 escritas, 7 orales y 6 populares. Compruébalo sumando.", "7 + 7 + 6 = 20", "La suma da exactamente la meta."),
        ex("Tienes 5 escritas, 9 orales y 3 populares registradas. ¿Cuál tradición tiene menos registros?", "Las populares", "Tres es menos que cinco y que nueve."),
    ],
    [
        arith("Tienes 5 escritas, 9 orales y 3 populares. ¿Cuántas escuchas llevas?", "5+9+3", "Se suman las escuchas de las tres tradiciones.", " escuchas"),
        ex("Quieres llegar a 20 con las 17 que llevas, escuchando una por día. ¿Cuántos días necesitas?", "3", "20 − 17 = 3 escuchas, una por día."),
    ],
    [ex("Un niño escucha una canción de cuna que cantaba su abuela. ¿Cómo puede anotarla sin dar datos privados?", "Con una descripción como «canción de cuna que cantaba una persona de mi familia» y un rasgo audible", "Sirve para anotar sin dar nombres ni datos privados.")],
    [ex("¿Para qué sirve una bitácora?", "Para anotar las escuchas", "Registra lo que escuchamos."), ex("¿Cuántas músicas escucharás al año como meta?", "Al menos 20", "Es la meta de la bitácora."), ex("¿Qué tradiciones debes mezclar?", "Escrita, oral y popular", "Para que la bitácora sea variada.")],
    (
        "Completa una bitácora de 6 escuchas con esta tabla: número, nombre o descripción, tradición (escrita, oral o popular) y un rasgo audible. Usa la bitácora de ejemplo si aún no escuchas: copia una fila y añade tus propios rasgos. Luego cuenta cuántas escuchas tienes de cada tradición y cuántas te faltan para llegar a 20.",
        "Tengo 6 escuchas: 2 escritas, 2 orales y 2 populares. Me faltan 14 para llegar a 20.",
        ["registra 6 escuchas con las cuatro columnas", "cuenta cada tradición", "calcula cuántas faltan"],
        ["tabla escrita", "conteo por tradición", "resta con la meta"],
        ["no mezclar tradiciones", "anotar datos privados"],
        "Reconoce la tabla clara y pide que explique cómo eligió sus músicas; si falta una tradición, sugiere una para la próxima semana.",
    ),
    "Escucha una música hoy y anótala en tu bitácora con un rasgo audible.",
    "Planifica en una tabla cuántas músicas escucharás por mes para llegar a 20 en el año.",
)

# ---------------------------------------------------------------- OA 04 · clase 1
F1 = "can-ta-mos jun-tos hoy"
F2 = "la lu-na sa-le por el cer-ro"
L(
    OA4, 1,
    f"Lápiz, papel y tu voz. {SILABAS} Frases de trabajo para cantar: «{F1}» y «{F2}». No hace falta saber la melodía: se pueden decir con ritmo parejo.",
    "Aprenderé a cantar al unísono con otros: empezar juntos, respirar juntos y terminar juntos. Sirve para que muchas voces suenen como una sola.",
    ["Sé repetir una frase que me enseñan.", "Sé mantener un pulso parejo.", "Sé contar sílabas."],
    [
        "Cantar al unísono es cantar todos la misma melodía, con las mismas palabras y al mismo tiempo. Para lograrlo, cuida tres momentos: la entrada, la respiración y el final. La entrada es empezar juntos con una señal. La respiración es tomar aire en el mismo lugar. El final es terminar juntos.",
        f"Piensa en la frase «{F1}». Tiene {S(F1)} sílabas. Si cantas una sílaba por pulso, la frase dura {S(F1)} pulsos. Para entrar juntos, el grupo cuenta antes: «uno, dos, tres, cuatro» en silencio y comienza en el siguiente pulso.",
        "Para cantar bien al unísono: de pie o sentado derecho, voz suave y clara, sin gritar. Escucha al grupo más que a ti. Si oyes que te sobresales, baja un poco. Si un compañero se pierde, ayúdale con voz suave y pulso parejo.",
    ],
    [("unísono", "todas las voces cantan lo mismo a la vez"), ("entrada", "momento en que empezamos juntos"), ("respiración", "tomar aire en el mismo lugar"), ("final", "terminar juntos"), ("voz clara", "voz suave y limpia, sin gritar")],
    [
        ("Contar sílabas", f"¿Cuántas sílabas tiene «{F1}»?", ["Cuento: can, ta, mos, jun, tos, hoy.", f"Son {S(F1)}."], f"{S(F1)} sílabas"),
        ("Planear el final", f"Cantas «{F1}» con una sílaba por pulso y luego descansas 2 pulsos para respirar. ¿Cuántos pulsos ocupa todo?", [f"La frase ocupa {S(F1)} pulsos.", "Se suman los 2 pulsos de descanso."], f"{S(F1) + 2} pulsos"),
    ],
    [
        ("Cantar muy fuerte para destacar.", "Se pierde el unísono.", "Escucha al grupo y canta con la misma fuerza."),
        ("Respirar cada persona en un momento distinto.", "Se cortan las frases en lugares distintos.", "Acuerden dónde respirar."),
    ],
    [
        ex("Cantar todos lo mismo a la vez se llama...", "Cantar al unísono", "Unísono significa una sola voz del grupo."),
        ex("Antes de entrar a cantar, ¿qué hace el grupo: cuenta en silencio o grita?", "Cuenta en silencio", "La cuenta en silencio ayuda a entrar juntos."),
        ex("¿Dónde respira el grupo: en el mismo lugar o cada uno cuando quiere?", "En el mismo lugar", "Así las frases suenan completas."),
    ],
    [
        ex(f"Cuenta las sílabas de «{F2}».", str(S(F2)), "Cada trozo separado con guion o espacio es una sílaba."),
        ex("Un coro de 10 niños canta. ¿Cuántas voces debería oírse: una sola o diez distintas?", "Una sola", "En el unísono todas las voces suenan como una."),
        ex("Si te sobresales con una voz muy fuerte, ¿qué debes hacer?", "Bajar un poco la fuerza y escuchar al grupo", "El unísono se logra igualando la fuerza."),
    ],
    [
        ex(f"Cantas «{F2}» con una sílaba por pulso. ¿Cuántos pulsos ocupa?", str(S(F2)), "Una sílaba por pulso hace que los pulsos y las sílabas sean iguales."),
        arith(f"Cantas «{F1}» dos veces seguidas, una sílaba por pulso. ¿Cuántos pulsos ocupan las dos?", f"{S(F1)}*2", "Cada vez ocupa 6 pulsos y se repite dos veces.", " pulsos"),
        ex("El grupo cuenta 4 pulsos en silencio y entra en el siguiente. ¿En qué número de pulso empieza la canción?", "5", "Cuatro pulsos de cuenta y entra en el quinto."),
    ],
    [
        ex("Una niña canta un poquito antes que el grupo. ¿Qué parte del unísono falló?", "La entrada", "Entrar juntos exige esperar la señal."),
        ex("Dos niños terminan una frase después que el resto. ¿Qué parte falló?", "El final", "Terminar juntos es parte del unísono."),
    ],
    [
        ex(f"Planea el aire: la frase «{F2}» ocupa {S(F2)} pulsos y respiras 2 pulsos antes de repetirla. ¿Cuántos pulsos hay entre una entrada y la siguiente?", str(S(F2) + 2), "9 pulsos de canto más 2 de respiración: 11."),
        ex("Ordena para un buen unísono: (a) cantar, (b) cuenta en silencio, (c) terminar juntos.", "b, a, c", "Primero se cuenta, luego se canta y al final se termina juntos."),
    ],
    [ex("En un acto escolar, 30 niños cantan el himno de su curso (o una canción conocida). Si empiezan en distintos momentos, ¿qué pueden hacer para entrar juntos?", "Contar en silencio y entrar en el mismo pulso con una señal", "Una señal y una cuenta en silencio sincronizan al grupo.")],
    [ex("¿Qué significa unísono?", "Todas las voces cantan lo mismo a la vez", "Es una sola voz colectiva."), ex("¿Qué tres momentos cuidas al cantar juntos?", "Entrada, respiración y final", "Son las tres partes del unísono."), ex("¿Cantas muy fuerte para destacar?", "No", "Se escucha al grupo.")],
    (
        f"Aprende la frase «{F1}». Con una sílaba por pulso, dila con palmas parejas. Haz esto tres veces: (1) cuenta 4 pulsos en silencio; (2) di la frase; (3) respira 2 pulsos. Pide a alguien que cante contigo y logren entrar y terminar juntos. Anota cuántos pulsos ocupa cada vuelta completa.",
        f"Cada vuelta dura 4 + {S(F1)} + 2 = {4 + S(F1)+ 2} pulsos. Entramos juntos en el pulso 5 y terminamos juntos.",
        ["usa cuenta en silencio", "dice la frase con una sílaba por pulso", "respira en el mismo lugar con su compañero"],
        ["canto o recitado con palmas", "conteo de pulsos", "registro de si entraron y terminaron juntos"],
        ["gritar para destacar", "empezar antes de la señal"],
        "Reconoce la entrada conjunta y pregunta cómo supo cuándo empezar; si se separan, repite más despacio con pulso visible.",
    ),
    "Canta suavemente una canción que conozcas junto a alguien de tu casa y traten de empezar y terminar juntos.",
    "Elige otra frase de 8 sílabas y planea dónde respirarán.",
)

# ---------------------------------------------------------------- OA 04 · clase 2
G1 = "can-ta-mos y so-na-mos hoy"
G2 = "tam-bor y voz van con-ti-go"
L(
    OA4, 2,
    f"Lápiz, tus palmas y tu voz. {SILABAS} Frases de trabajo: «{G1}» y «{G2}». Percusión corporal: palmas suaves y pasos sin saltar.",
    "Aprenderé a mantener un pulso parejo con percusión corporal mientras canto. Sirve para que la voz y el cuerpo vayan juntos y para no apurarme.",
    ["Sé caminar al pulso.", "Sé cantar una frase corta.", "Sé contar sílabas."],
    [
        "La percusión corporal es hacer música con el cuerpo: palmas, golpes suaves en las piernas o pasos. Si marcas un pulso parejo mientras cantas, la canción se mantiene firme. El pulso es el latido que no cambia aunque las sílabas sean rápidas o lentas.",
        f"Una forma de unir voz y cuerpo es dar una palma por cada sílaba. Así «{G1}» tiene {S(G1)} sílabas y {S(G1)} palmas. Otra forma es dar una palma solo cada 2 sílabas: así hay {S(G1)//2} palmas. En ambos casos el pulso sigue parejo.",
        "Para mantener el pulso, no mires solo tus manos: escucha el latido del grupo. Si te adelantas, espera un instante. Si te atrasas, ve un poco más rápido con calma. Cantar suave ayuda a oír el pulso.",
    ],
    [("percusión corporal", "hacer sonidos con el cuerpo"), ("pulso parejo", "latido que no se apura ni se atrasa"), ("sílaba", "golpe de voz"), ("adelantarse", "ir más rápido que el grupo"), ("atrasarse", "ir más lento que el grupo")],
    [
        ("Palma por sílaba", f"¿Cuántas palmas das en «{G1}» con una palma por sílaba?", ["Cuento las sílabas: can, ta, mos, y, so, na, mos, hoy.", f"Son {S(G1)}."], f"{S(G1)} palmas"),
        ("Palma cada dos sílabas", f"Das una palma cada 2 sílabas en «{G1}». ¿Cuántas palmas das?", [f"La frase tiene {S(G1)} sílabas.", f"{S(G1)} ÷ 2 = {S(G1)//2}."], f"{S(G1)//2} palmas"),
    ],
    [
        ("Apurar el pulso cuando las sílabas son rápidas.", "El pulso se descontrola.", "Mantén el latido parejo y adapta la voz."),
        ("Mirar solo las manos.", "No se oye al grupo.", "Escucha el latido de todos."),
    ],
    [
        ex("¿Qué es la percusión corporal?", "Hacer sonidos con el cuerpo", "Palmas y golpes suaves son ejemplos."),
        ex("El pulso parejo, ¿se apura o se mantiene?", "Se mantiene", "Pulso parejo significa que no cambia."),
        ex(f"Das una palma por sílaba en «{G2}». ¿Cuántas palmas das?", str(S(G2)), "Una palma por cada una de las 8 sílabas."),
    ],
    [
        ex("Si te adelantas al grupo, ¿qué haces: esperar un instante o apurarte más?", "Esperar un instante", "Esperar vuelve a poner tu pulso con el del grupo."),
        ex(f"Das una palma cada 2 sílabas en «{G2}». ¿Cuántas palmas das?", str(S(G2) // 2), "8 sílabas entre 2 dan 4 palmas."),
        ex("Cantas más suave. ¿Eso ayuda a oír el pulso del grupo?", "Sí", "Con menos fuerza se escucha mejor a los demás."),
    ],
    [
        ex(f"Una palma por sílaba. Si cantas «{G1}» y después «{G2}», ¿cuántas palmas en total?", str(S(G1) + S(G2)), "8 + 8 = 16 palmas."),
        arith(f"Cantas «{G2}» tres veces seguidas con una palma por sílaba. ¿Cuántas palmas das?", f"{S(G2)}*3", "Cada vez hay 8 palmas y se repite 3 veces.", " palmas"),
        ex(f"En «{G1}» das una palma por sílaba y una pisada en las sílabas 1 y 5. ¿Cuántas pisadas das?", "2", "Solo hay pisadas en dos sílabas."),
    ],
    [
        ex("Tomás da palmas muy rápidas en las sílabas cortas y lentas en las largas. ¿Mantiene un pulso parejo?", "No", "El pulso parejo no cambia con las sílabas."),
        ex("Sara canta bien, pero sus palmas se atrasan. ¿Qué puede hacer?", "Escuchar el latido del grupo y ajustar sus palmas", "Debe ajustarse al pulso común."),
    ],
    [
        ex(f"Cantas «{G1}» con palma por sílaba y después descansas 4 pulsos. Cantas otra vez. ¿Cuántos pulsos pasan desde la primera sílaba hasta empezar de nuevo?", str(S(G1) + 4), "8 pulsos de canto y 4 de descanso: 12."),
        ex("Quieres dar 6 palmas por vuelta. ¿Cuántas vueltas das para llegar a 30 palmas?", "5", "6 × 5 = 30, así que son 5 vueltas."),
    ],
    [arith("Marchas en un desfile escolar: das un paso por pulso durante 24 pulsos. ¿Cuántos pasos das?", "24", "Un paso por cada pulso.", " pasos")],
    [ex("¿Qué debe hacer el pulso mientras cantas?", "Mantenerse parejo", "Es el latido que sostiene la canción."), ex(f"¿Cuántas sílabas tiene «{G1}»?", str(S(G1)), "Hay 8 trozos separados."), ex("Si te atrasas, ¿qué haces?", "Escucho al grupo y ajusto con calma", "El pulso se recupera escuchando.")],
    (
        f"Di «{G2}» con una palma por sílaba y marca un paso con el pie derecho en la primera sílaba de cada vuelta. Haz 3 vueltas seguidas sin cambiar la velocidad. Anota cuántas palmas diste y cuántos pasos.",
        "Dije 8 palmas por vuelta, 24 palmas en 3 vueltas, y 3 pasos. El pulso fue parejo.",
        ["una palma por cada una de las 8 sílabas", "el paso solo en la primera sílaba de cada vuelta", "velocidad pareja durante 3 vueltas"],
        ["canto o recitado con palmas", "registro de palmas y pasos", "explicación de cómo mantuvo el pulso"],
        ["apurarse en las sílabas cortas", "olvidar el paso de la primera sílaba"],
        "Reconoce el pulso parejo; si se apura, repite más despacio con una persona marcando el latido.",
    ),
    "Camina por tu casa al pulso mientras dices la frase con una palma por sílaba.",
    "Cambia la velocidad de la frase a la mitad y cuenta cuántas palmas necesitarás en el mismo tiempo.",
)

# ---------------------------------------------------------------- OA 04 · clase 3
PA = (TA, TA, TT, SIL)
PB = (TA, SIL, TA, SIL)


def coinciden(a, b):
    return sum(1 for x, y in zip(a, b) if x != SIL and y != SIL)


L(
    OA4, 3,
    f"Lápiz, papel y percusión segura: un tarro de plástico o una caja de cartón con tapa, dos cucharas de madera, un par de claves de madera, un pandero o tus palmas. Nada de vidrio ni objetos que se puedan romper o lastimar. Leyenda: {LEY}.",
    "Aprenderé a tocar un patrón instrumental con instrumentos de percusión convencionales y no convencionales, respetando el sonido y el silencio. Sirve para tocar acompañamientos con otros.",
    ["Sé contar pulsos y sonidos.", "Sé tocar un patrón con las palmas."],
    [
        "Los instrumentos de percusión se tocan golpeando, raspando o sacudiendo. Algunos son convencionales: claves, pandero, triángulo, tambor y maracas. Otros son no convencionales: un tarro de plástico, una caja de cartón o dos cucharas de madera. Los dos tipos sirven para tocar patrones, siempre que sean seguros.",
        f"Un patrón instrumental es una secuencia de sonidos y silencios sobre el pulso. Por ejemplo, el patrón A es {P(*PA)} y el patrón B es {P(*PB)}. Si dos personas tocan A y B a la vez, a veces suenan juntas y a veces una descansa mientras la otra toca. Contar bien los silencios es parte de tocar bien.",
        "Para cuidar los instrumentos: golpea con suavidad, no apuntes a las orejas de otros y baja el volumen en espacios pequeños. Antes de tocar, cuenta los pulsos en silencio; así entras juntos.",
    ],
    [("percusión", "instrumentos que se golpean, raspan o sacuden"), ("convencional", "instrumento hecho para hacer música"), ("no convencional", "objeto que se usa para hacer música sin haber sido hecho para eso"), ("patrón instrumental", "secuencia de sonidos y silencios que se toca"), ("silencio", "pulso en que no suena nada")],
    [
        ("Contar sonidos de un patrón", f"¿Cuántos sonidos tiene el patrón A: {P(*PA)}?", [f"TA suena 1, TA suena 1, ti-ti suena 2 y SIL suena 0.", f"1 + 1 + 2 + 0 = {sounds(*PA)}."], f"{sounds(*PA)} sonidos"),
        ("Pulsos en que suenan los dos", f"A es {P(*PA)} y B es {P(*PB)}. ¿En cuántos pulsos suenan A y B al mismo tiempo?", ["Pulso 1: A suena y B suena: coinciden.", "Pulso 2: A suena y B tiene SIL.", "Pulso 3: A suena y B suena: coinciden.", "Pulso 4: ambos tienen SIL."], f"{coinciden(PA, PB)} pulsos"),
    ],
    [
        ("Golpear fuerte un tarro o una caja para que suene más.", "Se puede romper el objeto o lastimar los oídos.", "Golpea con suavidad y ajusta la fuerza."),
        ("No contar el silencio y tocar sin pausa.", "El patrón cambia.", "Cuenta el silencio como un pulso."),
    ],
    [
        ex("Un tambor es un instrumento convencional. Una caja de cartón usada para tocar, ¿qué tipo es?", "No convencional", "Se usa para hacer música sin haber sido hecha para eso."),
        ex("¿Cuál instrumento es seguro: dos cucharas de madera o un vaso de vidrio?", "Dos cucharas de madera", "El vidrio puede romperse y lastimar."),
        ex("Un SIL en un patrón, ¿se toca o se descansa?", "Se descansa", "SIL es un pulso en que no suena nada."),
    ],
    [
        ex(f"Cuenta los pulsos del patrón B: {P(*PB)}.", str(len(PB)), "Cada símbolo ocupa un pulso, incluso los silencios."),
        ex(f"Cuenta los sonidos del patrón B: {P(*PB)}.", str(sounds(*PB)), "Solo suenan los dos TA."),
        ex("Dos niños tocan al mismo tiempo. Uno toca claves y otro un tarro. ¿Qué cuidan para que se escuchen bien los dos?", "La fuerza: tocan con suavidad y escuchan al otro", "Escuchar al otro evita que uno tape al otro."),
    ],
    [
        ex(f"A es {P(*PA)} y B es {P(*PB)}. ¿En qué pulsos suenan juntos?", "En los pulsos 1 y 3", "Ambos tienen sonido en esos dos pulsos."),
        arith(f"El patrón A ({P(*PA)}) se toca 4 vueltas. ¿Cuántos sonidos suenan en total?", f"{sounds(*PA)}*4", "Cada vuelta tiene 4 sonidos y se repite 4 veces.", " sonidos"),
        ex(f"Escribe un patrón C de 4 pulsos que sea igual a B en los pulsos 1 y 3, pero con TA en el pulso 2 y SIL en el 4.", P(TA, TA, TA, SIL), "Se mantienen TA en 1 y 3, se agrega TA en 2 y se deja SIL en 4."),
    ],
    [
        ex(f"Mara toca {P(*PA)}. Su compañero Beto toca {P(*PA)} también. ¿Están tocando el mismo patrón?", "Sí", "Los cuatro símbolos son iguales."),
        ex("Un niño cambia el SIL del patrón A por un TA. ¿Sigue siendo el mismo patrón?", "No", "Cambió un símbolo y por eso es otro patrón."),
    ],
    [
        ex(f"Si A ({P(*PA)}) y B ({P(*PB)}) se tocan a la vez, ¿cuántos pulsos suena solo A (B descansa)?", "1", "En el pulso 2 A suena y B tiene SIL."),
        ex(f"Dos instrumentos tocan el mismo patrón {P(*PA)}. ¿En cuántos pulsos suenan juntos?", str(sum(1 for t in PA if t != SIL)), "Como tocan lo mismo, coinciden en todos los pulsos con sonido."),
    ],
    [ex("En tu casa, para tocar un patrón con otra persona quieren usar una olla grande y una caja de cartón. ¿Cómo cuidan los oídos y los objetos?", "Golpean con suavidad con cucharas de madera y no tocan cerca de los oídos", "La seguridad primero: poca fuerza y distancia.")],
    [ex("¿Qué instrumento no convencional puedes usar?", "Un tarro de plástico", "Es un objeto cotidiano que suena al golpearlo con suavidad."), ex(f"¿Cuántos sonidos tiene {P(TA, SIL, TA, SIL)}?", "2", "Solo suenan los dos TA."), ex("¿Qué haces con un silencio?", "Lo cuento como un pulso sin sonido", "El silencio es parte del patrón.")],
    (
        f"Toca el patrón {P(*PA)} cuatro veces con un instrumento seguro de los que tengas (tarro, caja de cartón o cucharas de madera sobre una silla acolchada). Después pide a otra persona que toque {P(*PB)} a la vez. Anota en qué pulsos suenan juntos y en cuál toca solo uno.",
        "Juntos sonamos en los pulsos 1 y 3. Solo yo toco en el pulso 2. En el pulso 4 hubo silencio de los dos.",
        ["toca el patrón A con el silencio en su lugar", "usa objetos seguros", "anota los pulsos en que coinciden y en cuál suena uno solo"],
        ["interpretación", "registro escrito de pulsos", "explicación de la seguridad de sus objetos"],
        ["no respetar el silencio", "golpear fuerte un objeto frágil"],
        "Reconoce el patrón completo con sus silencios; si pierde el pulso, vuelve al conteo en voz alta.",
    ),
    "Toca el patrón A con palmas, luego con una cuchara de madera sobre un tarro de plástico.",
    "Inventa un patrón D de 4 pulsos con 3 sonidos y compáralo con el A.",
)

# ---------------------------------------------------------------- OA 04 · clase 4
L(
    OA4, 4,
    f"Lápiz, papel y percusión segura (palmas, claves, tarro de plástico, cucharas de madera). Señales del director: mano abierta arriba = prepararse; bajar la mano = entrar; puño cerrado = parar; palma hacia abajo = más suave; palma hacia arriba = más fuerte. Leyenda: {LEY}.",
    "Aprenderé a tocar y cantar en grupo siguiendo señales: preparar, entrar, bajar la fuerza y terminar. Sirve para formar un pequeño ensamble y trabajar con otras personas.",
    ["Sé cantar al unísono.", "Sé mantener un pulso.", "Sé tocar un patrón con silencio."],
    [
        "Un ensamble es un grupo de personas que hacen música juntas. Para que suene ordenado, una persona puede dirigir con señales de las manos. Cada señal tiene un significado que todos conocen. Estas señales son un acuerdo de esta clase; otros grupos pueden usar señales distintas. Una mano abierta arriba dice «prepárense». Al bajar la mano, entran. Un puño cerrado dice «paren».",
        "Con las señales también se cambia la fuerza: la palma hacia abajo pide tocar más suave, y la palma hacia arriba, más fuerte. El director marca el pulso con la mano y todos lo siguen. Para que el ensamble suene bien, los tres grupos (voz, tambor y claves) pueden entrar uno tras otro, cada 4 pulsos.",
        "Lo más importante en un ensamble es mirar y escuchar. Mira al director, escucha al grupo y cuida tu fuerza. Si te equivocas, no te detengas ni mires con enojo: sigue al pulso y vuelve a entrar en la próxima oportunidad.",
    ],
    [("ensamble", "grupo que hace música junto"), ("director", "quien da las señales"), ("señal", "gesto con un significado acordado"), ("entrada", "momento en que empieza un grupo"), ("volumen", "qué tan fuerte o suave suena el grupo")],
    [
        ("Seguir las señales", "El director levanta la mano abierta, la baja, y luego cierra el puño. ¿Qué hace el grupo, en orden?", ["Mano abierta arriba: prepararse.", "Bajar la mano: entrar.", "Puño cerrado: parar."], "Se prepara, entra y para"),
        ("Entradas escalonadas", "Tres grupos entran cada 4 pulsos: la voz en el pulso 1, el tambor en el 5 y las claves en el 9. La pieza dura 16 pulsos. ¿En cuántos pulsos suenan los tres grupos juntos?", ["Los tres suenan juntos desde el pulso 9.", "Del pulso 9 al 16 hay 8 pulsos."], "8 pulsos"),
    ],
    [
        ("Entrar cuando uno quiere y no con la señal.", "Se pierde el orden.", "Mira al director y entra al bajar su mano."),
        ("Tocar más fuerte cuando el director pide suave.", "No se sigue la señal.", "Palma hacia abajo significa más suave."),
    ],
    [
        ex("Mano abierta hacia arriba: ¿qué señal es?", "Prepararse", "Significa que el grupo se alista para entrar."),
        ex("Puño cerrado: ¿empiezas o paras?", "Paras", "El puño cerrado indica detenerse."),
        ex("Palma hacia abajo: ¿tocas más suave o más fuerte?", "Más suave", "La palma baja pide bajar la intensidad."),
    ],
    [
        ex("¿Qué haces cuando te equivocas en un ensamble: sigo el pulso o me detengo con enojo?", "Sigo el pulso", "No detener el ensamble permite volver a entrar."),
        ex("Si el director baja la mano, ¿qué hace el grupo?", "Entra", "Bajar la mano es la señal de entrada."),
        ex("Tres grupos entran uno tras otro cada 4 pulsos. Si el primero entra en el pulso 1, ¿en qué pulso entra el segundo?", "5", "1 + 4 = 5."),
    ],
    [
        ex("La voz entra en el pulso 1, el tambor en el 5 y las claves en el 9. ¿En qué pulso entran las claves?", "9", "Es el pulso de la tercera entrada."),
        arith("Una pieza dura 16 pulsos. La voz entra en el pulso 1 y el tambor en el 5. ¿Cuántos pulsos suena la voz sola antes de que entre el tambor?", "5-1", "Del pulso 1 al 4 solo suena la voz; son 4 pulsos.", " pulsos"),
        ex("Una pieza dura 16 pulsos. Las claves entran en el pulso 9. ¿Cuántos pulsos tocan?", "8", "Del pulso 9 al 16 hay 8 pulsos."),
    ],
    [
        ex("Un niño entra antes de la señal. ¿Qué cualidad del ensamble se pierde: el orden o el color del sonido?", "El orden", "La entrada conjunta marca el orden."),
        ex("El director pide más suave y todos tocan igual. ¿Falló la entrada o la intensidad?", "La intensidad", "No siguieron la señal de volumen."),
    ],
    [
        ex("Diseña las señales para una pieza de 12 pulsos: (a) mano arriba, (b) mano baja y todos entran, (c) palma hacia abajo, (d) puño. Pon en orden lo que pasa.", "a, b, c, d", "Primero se prepara, luego entra, baja la fuerza y finalmente para."),
        arith("Quieres que cada grupo toque 12 pulsos antes de parar. Son 3 grupos. ¿Cuántos pulsos suman todos los grupos?", "12*3", "Cada uno toca 12 pulsos y son 3 grupos.", " pulsos"),
    ],
    [ex("Una orquesta escolar necesita empezar junta. El director levanta la mano abierta y baja. ¿Qué deben hacer los músicos justo en ese momento?", "Empezar a tocar juntos", "Bajar la mano es la señal de entrada.")],
    [ex("¿Qué significa mano abierta arriba?", "Prepararse", "Es el aviso antes de entrar."), ex("¿Quién da las señales en un ensamble?", "El director", "Dirige con gestos."), ex("¿Qué debes hacer además de tocar?", "Mirar y escuchar", "Es lo más importante en un ensamble.")],
    (
        f"Forma un pequeño ensamble con dos personas de tu casa (o usa tus manos como tres «grupos»: voz, palmas y pies). Una persona dirige con las señales y los demás siguen. Pieza de 12 pulsos: la voz entra en el pulso 1 con {P(TA, TA, TA, SIL)}; las palmas, en el pulso 5; los pies, en el pulso 9. Termina con puño cerrado. Cuenta cuántos pulsos tocó cada grupo y escribe qué señales usaste.",
        "Voz: 12 pulsos. Palmas: 8 pulsos. Pies: 4 pulsos. Usamos mano abierta, mano que baja, palma hacia abajo y puño.",
        ["sigue las señales del director", "entra en el pulso correcto", "cuenta correctamente los pulsos que tocó cada grupo"],
        ["interpretación en ensamble", "registro de señales", "conteo de pulsos"],
        ["entrar antes de la señal", "tocar más fuerte cuando piden suave"],
        "Reconoce el orden de las entradas y pregunta cómo supo cuándo entrar; si se separan, practica la cuenta en silencio.",
    ),
    "Practica las cinco señales frente a un espejo, diciendo qué hace el grupo en cada una.",
    "Inventa una señal nueva con un significado y enséñasela a alguien.",
)
