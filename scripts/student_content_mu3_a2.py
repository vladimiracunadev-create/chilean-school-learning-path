"""Student material for 3.º básico Música, OA 03 (escucha abundante de músicas de diversos contextos) y OA 04 (canto e interpretación instrumental)."""
from __future__ import annotations

import re

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA3, OA4 = "MU03 OA 03", "MU03 OA 04"


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, tk, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[dict(title=t, problem=p, steps=s, answer=a) for t, p, s, a in worked],
        mistakes=[dict(wrong=w, why=y, fix=f) for w, y, f in mistakes],
        tiers=dict(recovery=R, understand=C, apply=A, reason=Z, challenge=D),
        context=ctx, selfcheck=sc, open_task=task(*tk), reinforce=reinforce, extend=extend,
    )


def syl(text: str) -> int:
    """Syllables as written: words are separated by spaces and syllables by hyphens."""
    return len([t for t in re.split(r"[\s-]+", text.strip()) if t])


NOTA_SIGLOS = "«Hace más de 100 años» es una época muy antigua; «hace cerca de 100 años» es antigua, pero más reciente"
FICHAS = {
    "Danzas eslavas": ("Antonín Dvořák", "checo", "compuesta hace más de 100 años", "inspirada en danzas folclóricas de pueblos eslavos"),
    "El Carnaval de los Animales": ("Camille Saint-Saëns", "francés", "compuesta hace más de 100 años", "música descriptiva: retrata animales con sonidos"),
    "Gran Cañón (suite)": ("Ferde Grofé", "estadounidense", "compuesta hace cerca de 100 años", "música descriptiva: retrata un paisaje"),
}
FICHAS_TXT = " ".join(f"Ficha {i}: «{t}», de {c}, compositor {p}, {s}; {d}." for i, (t, (c, p, s, d)) in enumerate(FICHAS.items(), 1))

# ---------------------------------------------------------------- OA 03 · clase 1
L(
    OA3, 1,
    f"Lápiz y papel. Las obras se conocen por tres fichas escritas (no necesitas audio). Si puedes, un adulto puede poner un fragmento corto de una de ellas a volumen bajo, pero no es necesario. {NOTA_SIGLOS}.",
    "Aprenderé a escuchar con contexto la música de tradición escrita: quién la compuso, cuándo y para qué. Sirve para entender mejor lo que se escucha.",
    ["Sé escuchar en silencio y por turnos.", "Sé nombrar cualidades del sonido.", "Sé qué es un instrumento."],
    [
        "La música de tradición escrita, también llamada docta, la compone una persona, el compositor, y la anota en una partitura para que la interpreten otras personas. El intérprete es quien la toca o la canta. Esta música se puede tocar igual muchos años después, porque está escrita.",
        f"Para escuchar con contexto, preguntamos: ¿quién la compuso?, ¿hace cuánto tiempo?, ¿de qué país era?, ¿qué quiso mostrar? Fichas de trabajo: {FICHAS_TXT} Con esos datos sabemos qué esperar antes de escuchar.",
        "Una parte de esta música es descriptiva: usa los sonidos para mostrar animales, paisajes o historias. Otra parte se inspira en bailes del folclor. Al escuchar, respeta el silencio, espera tu turno para hablar y mantén un volumen que no moleste a nadie.",
    ],
    [("compositor", "persona que crea una obra musical"), ("partitura", "papel donde se escribe la música"), ("intérprete", "persona que toca o canta la obra"), ("música descriptiva", "música que retrata animales, paisajes o historias"), ("contexto", "datos de quién, cuándo y para qué se hizo la música")],
    [
        ("Leer una ficha", f"{FICHAS_TXT} ¿Quién es el compositor de «Gran Cañón (suite)» y hace cuánto tiempo se compuso?", ["Busco la ficha 3.", "El compositor es Ferde Grofé.", "Se compuso hace cerca de 100 años."], "Ferde Grofé; hace cerca de 100 años"),
        ("Contar con un criterio", f"{FICHAS_TXT} {NOTA_SIGLOS}. ¿Cuántas obras de las fichas se compusieron hace más de 100 años?", ["Reviso la época de cada ficha.", "Danzas eslavas: más de 100 años; Carnaval de los Animales: más de 100 años; Gran Cañón: cerca de 100 años."], "2 obras"),
    ],
    [
        ("Pensar que el compositor y el intérprete son la misma persona siempre.", "El compositor crea la obra; el intérprete la toca.", "Pregunta quién la creó y quién la toca."),
        ("Creer que la música escrita es mejor que la que no está escrita.", "Son tradiciones distintas, no mejores ni peores.", "Describe cómo se transmite cada una, sin comparar valor."),
    ],
    [
        ex(f"{FICHAS_TXT} ¿De qué nacionalidad es el compositor de «El Carnaval de los Animales»?", "Francés", "La ficha 2 dice que Camille Saint-Saëns es francés."),
        ex("¿Cómo se llama la persona que crea una obra musical?", "Compositor", "El compositor es quien crea la obra."),
        ex("¿Dónde se anota la música de tradición escrita?", "En una partitura", "La partitura es el papel donde se escribe la música."),
    ],
    [
        ex(f"{FICHAS_TXT} ¿Cuál de las obras retrata animales?", "El Carnaval de los Animales", "La ficha 2 dice que retrata animales."),
        ex(f"{FICHAS_TXT} ¿Cuál es el compositor de las «Danzas eslavas»?", "Antonín Dvořák", "La ficha 1 nombra a Dvořák."),
        ex(f"{FICHAS_TXT} ¿Cuáles dos fichas son música descriptiva?", "La 2 y la 3", "Ambas dicen «música descriptiva»."),
    ],
    [
        ex(f"{FICHAS_TXT} ¿Qué ficha dice que está inspirada en danzas folclóricas?", "La ficha 1", "Solo las «Danzas eslavas» están descritas así."),
        arith("Una persona escucha un fragmento de cada una de las tres fichas, y cada fragmento dura 2 minutos. ¿Cuántos minutos escucha en total?", "3*2", "Son 3 fragmentos de 2 minutos cada uno.", " minutos"),
        ex(f"{FICHAS_TXT} Un niño dice que el compositor de «Gran Cañón (suite)» es checo. ¿Qué dato de la ficha lo corrige?", "Que es estadounidense", "La ficha 3 dice «estadounidense»."),
    ],
    [
        ex("Luisa dice: «la música de tradición escrita es más importante que otras». ¿Es una descripción o una jerarquía?", "Una jerarquía", "Dice que una vale más, en vez de describir cómo es."),
        ex("Una obra no está escrita en partitura, sino que se aprende cantándola entre vecinos. ¿Es tradición escrita?", "No", "La tradición escrita necesita una partitura."),
    ],
    [
        ex("Escribes el nombre del compositor, cuándo se compuso y de qué país era. ¿Cómo se llama ese conjunto de datos?", "Contexto", "Los datos de quién, cuándo y de dónde forman el contexto."),
        arith("Preparas una escucha con 3 fichas y escribes 2 preguntas de contexto para cada una. ¿Cuántas preguntas escribes en total?", "3*2", "Son 3 fichas y 2 preguntas por ficha.", " preguntas"),
    ],
    [ex("Una escuela organiza una escucha de «El Carnaval de los Animales». ¿Qué datos de contexto conviene contar antes de escuchar?", "Compositor, país, época y que retrata animales", "Esos datos ayudan a imaginar qué sonará.")],
    [ex("¿Quién interpreta una obra?", "El intérprete", "Es quien la toca o la canta."), ex("¿La música descriptiva retrata qué cosas?", "Animales, paisajes o historias", "Usa sonidos para mostrarlos."), ex("¿Qué debes respetar al escuchar música en grupo?", "El silencio y los turnos", "Así todos pueden escuchar.")],
    (
        f"Usa las fichas de la clase: {FICHAS_TXT} Elige una ficha y escribe: el nombre de la obra, el compositor, cuándo se compuso y tres preguntas que harías antes de escucharla. Después, si un adulto puede poner un fragmento corto a volumen bajo, escucha y escribe una cualidad del sonido que oíste. Si no hay audio, escribe una cualidad que esperas oír y por qué.",
        "Obra: Danzas eslavas, de Antonín Dvořák, compuesta hace más de 100 años. Preguntas: ¿qué danzas imita?, ¿qué instrumentos suenan?, ¿es rápida o lenta? Espero oír ritmos de baile porque la ficha dice que se inspira en danzas.",
        ["usa datos de la ficha", "formula tres preguntas de contexto", "justifica con un dato"],
        ["escrito breve", "conversación"],
        ["inventar datos que no están en la ficha", "decir solo «me gustó» sin evidencia"],
        "Reconoce el uso de la ficha y pregunta qué dato apoya cada expectativa; no acepta datos nuevos sin comprobarlos.",
    ),
    "Cuenta a una persona de tu casa la diferencia entre compositor e intérprete.",
    "Escribe tres preguntas de contexto que servirían para cualquier obra de tradición escrita.",
)

# ---------------------------------------------------------------- OA 03 · clase 2
L(
    OA3, 2,
    "Lápiz y papel. Todas las descripciones están escritas. No necesitas audio; si un adulto desea poner un fragmento a volumen bajo, puede hacerlo, pero no es parte de ningún ejercicio.",
    "Aprenderé a reconocer música inspirada en raíces folclóricas y a distinguirla de la música folclórica misma. Sirve para entender de dónde vienen las ideas de una obra.",
    ["Sé qué es tradición escrita.", "Sé qué es una danza.", "Sé qué es un compositor."],
    [
        "El folclor reúne canciones, bailes y costumbres de un pueblo que la gente aprende de otras personas, sin partitura. Esa música se transmite de boca en boca y es de tradición oral. Una música inspirada en raíces folclóricas es otra cosa: una persona la compone y la escribe, pero usa melodías, ritmos o bailes del folclor como inspiración.",
        "Hay ejemplos conocidos. Antonín Dvořák, compositor checo de hace más de 100 años, escribió «Danzas eslavas» inspirándose en danzas de pueblos eslavos. En Chile, el currículo oficial menciona «Chile en cuatro cuerdas», de G. Soublette, como una obra inspirada en raíces folclóricas del país. No tenemos que conocer sus notas para entender la idea: la obra está escrita, pero toma algo del folclor.",
        "Para decidir, pregúntate dos cosas: ¿la hace una comunidad y se aprende sin partitura?, entonces es folclor, de tradición oral. ¿La compuso una persona y está escrita, pero usa cosas del folclor?, entonces es música inspirada en raíces folclóricas. Si la música viene de un pueblo originario, cada pueblo y cada comunidad decide qué se enseña y cómo; pregunta siempre a un educador o educadora tradicional.",
    ],
    [("folclor", "canciones, bailes y costumbres que un pueblo transmite de persona a persona"), ("raíz folclórica", "origen en el folclor de un pueblo"), ("inspirada en", "que toma ideas de algo, pero es una obra nueva"), ("tradición oral", "se transmite sin partitura, de persona a persona"), ("danza", "baile con una música propia")],
    [
        ("Distinguir folclor de obra inspirada", "Un grupo de vecinos canta una canción antigua que aprendió de personas mayores de su barrio, sin partitura. ¿Es folclor o es obra inspirada en el folclor?", ["Se aprende sin partitura y pasa de persona a persona.", "No la compuso un compositor conocido para escribirla."], "Folclor, de tradición oral"),
        ("Distinguir obra inspirada", "Un compositor escribe en partitura una obra para orquesta, con ritmos de un baile tradicional de su país. ¿Es folclor o es obra inspirada en el folclor?", ["Tiene un compositor y una partitura.", "Usa ritmos del baile tradicional como inspiración."], "Obra inspirada en raíces folclóricas"),
    ],
    [
        ("Decir que «Danzas eslavas» es folclor porque nombra danzas.", "La obra fue compuesta y escrita por Dvořák.", "Es una obra inspirada en el folclor, no el folclor mismo."),
        ("Pensar que el folclor se aprende leyendo partituras.", "Se transmite de persona a persona.", "El folclor se aprende de otras personas, oyendo y practicando."),
    ],
    [
        ex("Una canción se aprende de personas mayores de la comunidad y se canta en las fiestas, sin partitura. ¿Folclor u obra inspirada en el folclor?", "Folclor", "Se transmite de persona a persona, sin partitura."),
        ex("Una obra con compositor y partitura toma ritmos de un baile tradicional. ¿Folclor u obra inspirada en el folclor?", "Obra inspirada en el folclor", "Tiene compositor y partitura, y toma ideas del folclor."),
        ex("¿De qué nacionalidad era el compositor Antonín Dvořák?", "Checo", "Dvořák era compositor checo."),
    ],
    [
        ex("¿Cómo se llama la tradición en que la música se transmite sin partitura?", "Tradición oral", "Se transmite de persona a persona."),
        ex("Según el currículo oficial, la obra «Chile en cuatro cuerdas», de G. Soublette, ¿es del folclor mismo o está inspirada en raíces folclóricas de Chile?", "Inspirada en raíces folclóricas de Chile", "Es una obra compuesta que toma ideas del folclor chileno."),
        ex("¿«Danzas eslavas» es una danza folclórica o una obra que se inspiró en danzas folclóricas?", "Una obra que se inspiró en danzas folclóricas", "Dvořák la compuso tomando ideas de esas danzas."),
    ],
    [
        ex("Una obra tiene partitura y compositor, y no usa nada del folclor. ¿Es inspirada en raíces folclóricas?", "No", "No toma ideas del folclor."),
        ex("Una danza se baila en una fiesta de un pueblo, la enseñan los mayores y nadie la escribió. ¿Qué tradición es?", "Tradición oral", "Se transmite sin partitura."),
        ex("Una persona quiere aprender una música de un pueblo originario. ¿A quién conviene consultar?", "A un educador o educadora tradicional", "Cada comunidad decide cómo y qué se enseña."),
    ],
    [
        ex("Dos niños discuten: uno dice que «Danzas eslavas» es mejor que una canción que se aprende de oído porque está escrita. ¿Qué respuesta describe sin jerarquizar?", "Son distintas: una está escrita y la otra se transmite oralmente", "Describir diferencias de transmisión evita decir cuál vale más."),
        ex("Un curso aprende una canción oyéndola y repitiéndola. Otro curso toca una obra leyendo la partitura. ¿Cuál de los dos usa la tradición oral?", "El primero", "La tradición oral se aprende de persona a persona, sin partitura."),
    ],
    [
        ex("Una obra compuesta hace más de 100 años se inspira en danzas de un pueblo. ¿Qué dato la distingue del folclor mismo: (a) tiene compositor y partitura, (b) se transmite sin partitura?", "(a)", "El compositor y la partitura la hacen una obra inspirada; la (b) describe el folclor."),
        ex("Una obra con compositor y partitura usa ritmos de un baile del campo. ¿Puede ser a la vez de tradición escrita e inspirada en el folclor?", "Sí", "Está escrita por un compositor y toma ideas del folclor."),
    ],
    [ex("En una escuela los estudiantes aprenden una canción tradicional cantándola con la profesora, sin papel. ¿Es tradición oral o escrita?", "Oral", "No usan partitura.")],
    [ex("¿Qué es el folclor?", "Canciones, bailes y costumbres que un pueblo transmite de persona a persona", "Es tradición oral."), ex("¿Una obra inspirada en el folclor tiene partitura?", "Sí", "La compone y escribe una persona."), ex("¿Quién decide qué se enseña de la música de un pueblo originario?", "La comunidad", "Por eso se consulta a un educador tradicional.")],
    (
        "Escribe una tabla de dos columnas: «Folclor (tradición oral)» y «Obra inspirada en el folclor (tradición escrita)». Clasifica estas cinco descripciones: (1) una canción que personas mayores de la comunidad enseñaron cantando, (2) «Danzas eslavas», (3) un baile de fiesta que se aprende bailando, (4) una obra con partitura que usa ritmos de un baile de su país, (5) un juego cantado que se pasa entre niños. Después explica con una frase por qué pusiste la 4 donde la pusiste.",
        "Folclor: 1, 3 y 5. Obra inspirada: 2 y 4. La 4 está escrita y la compuso una persona, aunque use ritmos de un baile.",
        ["clasifica las cinco descripciones", "justifica con partitura o transmisión oral", "no jerarquiza"],
        ["tabla escrita", "frase de justificación"],
        ["clasificar por parecido y no por cómo se transmite", "decir que una vale más que la otra"],
        "Reconoce la clasificación y pregunta cómo se transmite cada música; revisa que no use «mejor» ni «peor».",
    ),
    "Pregunta a una persona de tu casa qué canción aprendió de sus mayores y cómo la aprendió.",
    "Escribe una regla de respeto para conversar sobre músicas de otros pueblos.",
)

# ---------------------------------------------------------------- OA 03 · clase 3
L(
    OA3, 3,
    "Lápiz y papel. Las descripciones de la música popular están escritas en los ejercicios. Si quieres, pide a una persona de tu casa que te cuente qué música escucha, pero no es necesario.",
    "Aprenderé a escuchar música popular situándola: dónde, cuándo y para qué se escucha. Sirve para entender que cada música tiene un contexto.",
    ["Sé reconocer instrumentos.", "Sé comparar tempo y dinámica.", "Sé qué es tradición escrita y oral."],
    [
        "La música popular se difunde ampliamente por la radio, los conciertos, las grabaciones y las fiestas, y llega a mucha gente. Incluye estilos como el jazz, el rock y la fusión. El jazz nació en Estados Unidos, tiene mucha improvisación y se toca con instrumentos como trompeta, saxofón y contrabajo.",
        "La fusión mezcla estilos. Los Jaivas y Congreso son grupos chilenos que mezclan rock, jazz o música de raíces folclóricas y andinas. Son ejemplos de fusión con raíces folclóricas. Para escucharlos situados preguntamos: ¿dónde se toca esta música?, ¿quiénes la escuchan?, ¿para qué se usa: bailar, conversar, celebrar?",
        "Escuchar situado quiere decir ubicar la música en su contexto. Una misma música puede servir para bailar en una fiesta, acompañar un viaje o escucharse con atención en un concierto. El contexto no cambia los sonidos, pero cambia el sentido que le damos. Describe lo que oyes y el lugar donde la oyes, sin decir que un estilo vale más que otro.",
    ],
    [("música popular", "música difundida ampliamente por radio, conciertos y grabaciones"), ("jazz", "estilo con mucha improvisación, nacido en Estados Unidos"), ("fusión", "mezcla de estilos"), ("intérprete", "persona o grupo que toca la música"), ("situada", "ubicada en su contexto: dónde, cuándo y para qué")],
    [
        ("Situar una música", "Una banda toca en una plaza un sábado para que la gente baile. ¿Para qué se usa esa música en ese lugar?", ["Dice que la gente baila.", "El uso es bailar y celebrar."], "Para bailar"),
        ("Reconocer fusión", "Un grupo mezcla rock con instrumentos de raíz andina. ¿Es fusión con raíces folclóricas?", ["Mezcla dos estilos: rock y música andina.", "Una de las partes tiene raíz folclórica."], "Sí, es fusión con raíces folclóricas"),
    ],
    [
        ("Pensar que la música popular y la folclórica son iguales.", "La popular se difunde ampliamente por medios; el folclor se transmite de persona a persona.", "Mira cómo llega la música a la gente."),
        ("Decir que la música popular no sirve para aprender.", "Tiene contexto, elementos y estructuras que se pueden describir.", "Describe sonidos y contexto sin juzgar el estilo."),
    ],
    [
        ex("¿En qué país nació el jazz?", "Estados Unidos", "El jazz nació en Estados Unidos."),
        ex("¿Qué es fusión en música?", "Mezcla de estilos", "Une elementos de varios estilos."),
        ex("Una canción se escucha en una fiesta para bailar. ¿Para qué se usa?", "Para bailar", "El uso es el baile."),
    ],
    [
        ex("¿De qué país son los grupos Los Jaivas y Congreso?", "Chile", "Ambos son grupos chilenos."),
        ex("Un grupo de música popular mezcla rock con música folclórica. ¿Cómo se llama esa mezcla?", "Fusión con raíces folclóricas", "Unir rock con raíces del folclor es fusión."),
        ex("Una música se escucha en un concierto con atención y en silencio. Otra se escucha en una fiesta para bailar. ¿Qué cambia entre las dos?", "El uso o contexto", "Una se usa para escuchar con atención y la otra para bailar."),
    ],
    [
        ex("¿Cuál de estos es un rasgo del jazz: (a) mucha improvisación, (b) ninguna improvisación?", "(a)", "El jazz tiene mucha improvisación."),
        arith("Un concierto tiene 8 canciones y cada una dura 4 minutos. ¿Cuántos minutos dura el concierto, sin pausas?", "8*4", "Se multiplican las canciones por los minutos de cada una.", " minutos"),
        ex("Ana dice que una canción de rock no tiene raíces folclóricas. Pedro dice que un grupo de rock puede tenerlas. ¿Quién tiene razón en que es posible?", "Pedro", "La fusión puede mezclar rock con raíces folclóricas."),
    ],
    [
        ex("Una música se difunde a mucha gente por la radio, las grabaciones y los conciertos. ¿Es popular o de tradición oral?", "Popular", "La música popular se difunde ampliamente por esos medios."),
        ex("Ana dice «el jazz es mejor que el folclor». ¿Qué respuesta describe sin jerarquizar?", "Son distintos: el jazz improvisa mucho y el folclor se transmite de persona a persona", "Compara rasgos sin decir cuál vale más."),
    ],
    [
        arith("Una radio pone 5 canciones por hora. ¿Cuántas canciones pone en 4 horas?", "5*4", "Son 5 canciones por hora y 4 horas.", " canciones"),
        ex("Un grupo de jazz toca en un concierto y su música también suena en la radio. ¿Es música popular, de tradición oral o de tradición escrita?", "Música popular", "Se difunde por conciertos y radio, como la música popular."),
    ],
    [ex("Una niña ve una banda tocar en una plaza y la gente baila. Otra ve el mismo estilo en una sala silenciosa y todos escuchan sentados. ¿Qué cambió: la música o el contexto?", "El contexto", "El uso y el lugar fueron distintos.")],
    [ex("¿Cuál de estos es un estilo de música popular: (a) jazz, (b) partitura?", "(a)", "El jazz es un estilo; la partitura es un papel donde se escribe la música."), ex("¿Qué significa situar una música?", "Ubicarla en dónde, cuándo y para qué se escucha", "Es describir su contexto."), ex("¿Los Jaivas y Congreso son ejemplos de fusión con raíces folclóricas?", "Sí", "Mezclan estilos con raíces folclóricas.")],
    (
        "Escribe una ficha de «escucha situada» de tres músicas populares que conozcas, sin copiar letras: (1) una que se oiga en fiestas, (2) una que se oiga en la radio y (3) una que se toque en un concierto. Para cada una escribe: estilo (jazz, rock, fusión u otro), dónde se oye, para qué se usa y una cualidad del sonido (fuerte o suave, rápida o lenta).",
        "1) Cumbia: se oye en fiestas, sirve para bailar, rápida y fuerte. 2) Balada: radio, para acompañar, lenta y suave. 3) Jazz: concierto, para escuchar con atención, con improvisación.",
        ["escribe tres fichas", "indica dónde y para qué se oye", "agrega una cualidad del sonido"],
        ["ficha escrita"],
        ["describir solo el gusto personal", "no indicar el uso o el lugar"],
        "Reconoce el uso de datos de contexto y pide una cualidad del sonido cuando falte.",
    ),
    "Pregunta a una persona de tu casa dónde escuchaba música cuando era niña.",
    "Escribe una regla para conversar sobre música popular sin burlarte de los gustos.",
)

# ---------------------------------------------------------------- OA 03 · clase 4
CRIT = ("instrumentos", "tempo", "intensidad", "para qué se usa", "cómo se transmite")
MUS_A = {"instrumentos": "orquesta", "tempo": "moderado", "intensidad": "variada, sube y baja", "para qué se usa": "escuchar con atención", "cómo se transmite": "partitura"}
MUS_B = {"instrumentos": "guitarra eléctrica y batería", "tempo": "rápido", "intensidad": "fuerte", "para qué se usa": "bailar", "cómo se transmite": "grabación"}
MUS_C = {"instrumentos": "voz y guitarra", "tempo": "moderado", "intensidad": "suave", "para qué se usa": "bailar", "cómo se transmite": "persona a persona"}


def fmt_m(name, d):
    return f"Música {name}: " + "; ".join(f"{k}: {v}" for k, v in d.items()) + "."


def matches(d1, d2):
    return [k for k in CRIT if d1[k] == d2[k]]


L(
    OA3, 4,
    f"Lápiz y papel. Las tres músicas son descripciones de trabajo, no obras reales. {fmt_m('A', MUS_A)} {fmt_m('B', MUS_B)} {fmt_m('C', MUS_C)}",
    "Aprenderé a comparar músicas de distintos estilos con criterios, sin decir cuál es mejor. Sirve para respetar y entender la diversidad musical.",
    ["Sé describir instrumentos y tempo.", "Sé que hay músicas escritas, orales y populares.", "Sé que cada música tiene un contexto."],
    [
        f"Comparar es mirar parecidos y diferencias con los mismos criterios. Usamos cinco: {', '.join(CRIT)}. Con ellos describimos cada música igual. No usamos «mejor» ni «peor», porque cada estilo nace para un uso y una comunidad distintos.",
        f"Un ejemplo. {fmt_m('A', MUS_A)} {fmt_m('B', MUS_B)} Coinciden en {len(matches(MUS_A, MUS_B))} criterios. Difieren en {len(CRIT) - len(matches(MUS_A, MUS_B))}. No decimos cuál es mejor: solo describimos que A se usa para escuchar con atención y B para bailar.",
        "Para una comparación respetuosa: usa la misma pregunta para cada música, nombra primero algo que se oye, y termina con una frase como «son distintas porque…» o «se parecen en…». Evita burlarte del gusto de otras personas.",
    ],
    [("criterio", "pregunta que usamos igual en cada música para compararlas"), ("parecido", "algo que dos músicas comparten"), ("diferencia", "algo que dos músicas no comparten"), ("jerarquizar", "decir que una música vale más que otra"), ("respeto", "aceptar que hay músicas distintas")],
    [
        ("Contar coincidencias", f"{fmt_m('A', MUS_A)} {fmt_m('C', MUS_C)} ¿En cuántos criterios coinciden A y C?", ["Comparo criterio por criterio.", "Tempo: moderado y moderado, coinciden.", "Los otros cuatro son distintos."], f"En {len(matches(MUS_A, MUS_C))} criterio: el tempo"),
        ("Frase respetuosa", "Un niño dice «B es mejor que A». Escribe una frase respetuosa que describa.", ["Cambio «mejor» por una descripción.", "Digo qué cambia: tempo y uso."], "«B y A son distintas: B es rápida y se usa para bailar; A es moderada y se escucha con atención»"),
    ],
    [
        ("Usar «mejor» o «peor» para comparar.", "Se jerarquiza en vez de describir.", "Usa «se parecen» y «son distintas»."),
        ("Comparar músicas con criterios distintos cada vez.", "No se puede comparar bien.", "Usa los mismos criterios para todas."),
    ],
    [
        ex(f"{fmt_m('A', MUS_A)} {fmt_m('B', MUS_B)} ¿Cuál de las dos es más rápida?", "La B", "B es rápida y A es moderada."),
        ex(f"{fmt_m('B', MUS_B)} {fmt_m('C', MUS_C)} ¿Para qué se usan las dos?", "Para bailar", "Las dos tienen «para qué se usa: bailar»."),
        ex("¿Qué palabra evitas al comparar estilos: «distintas» o «mejor»?", "Mejor", "La palabra «mejor» jerarquiza y no describe."),
    ],
    [
        ex(f"{fmt_m('A', MUS_A)} {fmt_m('B', MUS_B)} ¿En cuántos criterios coinciden A y B?", str(len(matches(MUS_A, MUS_B))), "Ninguno de los cinco criterios coincide entre A y B."),
        ex(f"{fmt_m('B', MUS_B)} {fmt_m('C', MUS_C)} ¿En cuántos criterios coinciden B y C?", str(len(matches(MUS_B, MUS_C))), "Coincide solo «para qué se usa: bailar»."),
        ex(f"{fmt_m('A', MUS_A)} ¿Cómo se transmite la música A?", "Por partitura", "El criterio «cómo se transmite» dice partitura."),
    ],
    [
        ex(f"{fmt_m('A', MUS_A)} {fmt_m('C', MUS_C)} ¿Qué criterio comparten A y C?", "El tempo (moderado)", "Los otros cuatro criterios son distintos."),
        ex(f"{fmt_m('A', MUS_A)} {fmt_m('C', MUS_C)} ¿En cuántos criterios difieren A y C?", str(len(CRIT) - len(matches(MUS_A, MUS_C))), "Son 5 criterios y solo el tempo coincide: 5 − 1."),
    ],
    [
        ex("Dos músicas coinciden en 2 de 5 criterios. ¿En cuántos criterios difieren?", "3", "5 criterios menos 2 coincidencias."),
        ex("Un niño dice «la música de partitura es aburrida». ¿Qué falta para que su frase sea una descripción?", "Un criterio y un dato que se oye", "Debe decir qué se oye o para qué se usa, no su gusto."),
    ],
    [
        ex(f"{fmt_m('B', MUS_B)} {fmt_m('C', MUS_C)} Un niño dice que B es mejor que C porque es más rápida. ¿Eso describe la música o la jerarquiza?", "La jerarquiza", "Decir «mejor» ordena por valor; «es más rápida» solo describiría."),
        arith("Comparas 3 músicas de dos en dos: A con B, A con C y B con C. Cada comparación revisa 5 criterios. ¿Cuántos criterios revisas en total?", "3*5", "Son 3 comparaciones de 5 criterios cada una.", " criterios"),
    ],
    [ex("Un grupo escucha música moderada y suave para conversar; otro, música rápida y fuerte para bailar. ¿En qué dos criterios difieren más claramente?", "Tempo e intensidad", "Una es moderada y suave y la otra rápida y fuerte.")],
    [ex("¿Qué haces al comparar: describes o dices cuál es mejor?", "Describes", "Se comparan parecidos y diferencias."), ex("¿Cuántos criterios usamos en la clase?", "5", "Instrumentos, tempo, intensidad, uso y transmisión."), ex("¿Se compara con los mismos criterios para cada música?", "Sí", "Así la comparación es justa.")],
    (
        f"Compara con los cinco criterios la música A con la música B (están descritas arriba): {fmt_m('A', MUS_A)} {fmt_m('B', MUS_B)} Escribe cuántos criterios coinciden, cuántos difieren y una frase respetuosa que empiece con «Son distintas porque…».",
        "Coinciden 0 criterios y difieren 5. Son distintas porque A es moderada y suave, y B rápida y fuerte, y se usan para cosas diferentes.",
        ["compara usando los cinco criterios", "cuenta bien las coincidencias", "usa una frase sin jerarquizar"],
        ["comparación escrita"],
        ["decir mejor o peor", "no usar los cinco criterios"],
        "Reconoce la frase sin jerarquía y revisa las coincidencias criterio por criterio.",
    ),
    "Elige dos músicas que conozcas y compáralas en tempo y para qué se usan.",
    "Escribe una frase de comparación que use «se parecen en» y «se diferencian en».",
)

# ---------------------------------------------------------------- OA 03 · clase 5
BITA = [
    (1, "orquesta", "tradición escrita", "escuchar en silencio", "suave que crece"),
    (2, "canto tradicional de una comunidad", "tradición oral", "cantar entre personas", "suave y lenta"),
    (3, "banda de rock", "popular", "bailar en una fiesta", "fuerte y rápida"),
    (4, "danza de un pueblo", "tradición oral", "celebrar", "con pulso marcado"),
    (5, "cuarteto de cuerdas", "tradición escrita", "concierto", "moderada"),
    (6, "grupo de fusión", "popular", "escuchar en la radio", "rápida y fuerte"),
]
BITA_TXT = " ".join(f"N.º {n}: {m}, {t}, {u}, {c}." for n, m, t, u, c in BITA)
CONT = {t: sum(1 for b in BITA if b[2] == t) for t in ("tradición escrita", "tradición oral", "popular")}

L(
    OA3, 5,
    f"Lápiz y papel. Tabla de ejemplo (bitácora con 6 entradas): {BITA_TXT} La meta del año es llegar a 20 músicas distintas.",
    "Aprenderé a llevar una bitácora de escucha diversa: registrar cada música con su tradición, su contexto y una cualidad del sonido. Sirve para llegar a escuchar al menos 20 músicas variadas.",
    ["Sé distinguir tradición escrita, oral y popular.", "Sé nombrar cualidades del sonido.", "Sé comparar sin jerarquizar."],
    [
        "Una bitácora es un cuaderno donde anotas lo que escuchas. En cada fila escribes: número, qué música es, su tradición (escrita, oral o popular), el contexto (dónde y para qué) y una cualidad del sonido. Así nunca olvidas lo que escuchaste y puedes comparar.",
        f"La meta es escuchar al menos 20 músicas variadas, de corta duración. «Variadas» significa que haya de las tres tradiciones. En nuestro ejemplo hay {CONT['tradición escrita']} escritas, {CONT['tradición oral']} orales y {CONT['popular']} populares, en total {len(BITA)}. Para llegar a 20 faltan {20 - len(BITA)}.",
        "Cuando una música viene de un pueblo originario, anota solo lo que sabes con seguridad y pregunta a un educador o educadora tradicional lo que no sepas, como cuándo se toca o quién puede tocarla. Por ejemplo, el kultrún es un tambor del pueblo mapuche. No inventes significados ni nombres que no conozcas.",
    ],
    [("bitácora", "cuaderno donde se registra lo que se escucha"), ("variadas", "de distintas tradiciones y estilos"), ("registro", "anotación de una escucha"), ("fuente", "dónde o de quién conoces esa música"), ("diversa", "con muchas formas distintas")],
    [
        ("Contar entradas por tradición", f"{BITA_TXT} ¿Cuántas músicas de tradición oral hay anotadas?", ["Busco la palabra «tradición oral» en las entradas.", "Aparece en la 2 y en la 4."], f"{CONT['tradición oral']} músicas"),
        ("Calcular lo que falta", f"{BITA_TXT} La meta es 20. ¿Cuántas faltan?", ["Tengo 6 entradas.", "20 − 6 = 14."], f"{20 - len(BITA)} músicas"),
    ],
    [
        ("Anotar solo el gusto: «me gustó» o «me aburrió».", "No registra qué se oyó ni el contexto.", "Anota tradición, contexto y una cualidad del sonido."),
        ("Llenar la bitácora con una sola tradición.", "No es una escucha diversa.", "Busca que estén las tres tradiciones."),
    ],
    [
        ex(f"{BITA_TXT} ¿De qué tradición es la entrada n.º 3?", "Popular", "La entrada 3 dice «popular»."),
        ex(f"{BITA_TXT} ¿Cuántas músicas hay anotadas en total?", str(len(BITA)), "Son las entradas de la 1 a la 6."),
        ex("¿Cuántas músicas debe tener la bitácora al final del año?", "Al menos 20", "La meta es escuchar al menos 20 músicas variadas."),
    ],
    [
        ex(f"{BITA_TXT} ¿Cuántas músicas son de tradición escrita?", str(CONT["tradición escrita"]), "Son la 1 y la 5."),
        ex(f"{BITA_TXT} ¿Cuántas músicas populares hay?", str(CONT["popular"]), "Son la 3 y la 6."),
        ex(f"{BITA_TXT} ¿Cuál entrada se escuchó para bailar en una fiesta?", "La n.º 3", "La entrada 3 dice «bailar en una fiesta»."),
    ],
    [
        arith("Tienes 6 músicas anotadas y escuchas 3 más cada semana. ¿Cuántas tendrás después de 4 semanas?", "6+3*4", "Se suman las 6 iniciales y las 12 nuevas.", " músicas"),
        ex("¿Qué falta en esta entrada de bitácora: «N.º 7: una canción, me gustó»?", "Tradición, contexto y una cualidad del sonido", "Solo tiene gusto personal."),
    ],
    [
        ex("Una bitácora de 20 músicas tiene 12 populares, 6 orales y 2 escritas. ¿Qué tradición se debería buscar más?", "Escrita", "Es la que tiene menos entradas."),
        arith("En una bitácora de 20 músicas hay 12 populares y 6 orales. ¿Cuántas son de tradición escrita?", "20-12-6", "Al total se le quitan las populares y las orales.", " músicas"),
    ],
    [
        arith("Escuchas 2 músicas nuevas cada día, de lunes a viernes. ¿Cuántas músicas anotas en la semana?", "2*5", "Son 2 músicas por día durante 5 días.", " músicas"),
        arith("Tu bitácora tiene 6 entradas y quieres llegar a 20 en 7 semanas, con la misma cantidad de músicas nuevas cada semana. ¿Cuántas músicas nuevas por semana?", "(20-6)//7", "Faltan 14 músicas y se reparten en 7 semanas.", " músicas por semana"),
    ],
    [ex("Un niño anota una música del pueblo mapuche y escribe un significado que no conoce. ¿Qué conviene hacer?", "Borrar el significado y consultar a un educador tradicional", "No se inventan significados de otros pueblos.")],
    [ex("¿Qué datos lleva una entrada de la bitácora?", "Número, qué música es, tradición, contexto y una cualidad del sonido", "Esos datos permiten comparar después."), ex("¿Qué significa «variadas»?", "De distintas tradiciones", "Evita anotar solo un estilo."), ex("¿A quién consultas por una música de un pueblo originario?", "A un educador o educadora tradicional", "Ellos conocen cómo y cuándo se toca.")],
    (
        "Completa tu bitácora con estas tres músicas descritas (no hace falta audio): (a) un cuarteto de cuerdas que toca una obra con partitura en un concierto, suave y lenta; (b) un juego cantado que se pasa entre niños en el recreo, rápido y suave; (c) una banda de rock en una radio, fuerte y rápida. Para cada una anota: número (7, 8 y 9), tradición, contexto y una cualidad del sonido. Después escribe cuántas músicas llevas y cuántas faltan para 20.",
        "N.º 7: cuarteto, tradición escrita, concierto, suave y lenta. N.º 8: juego cantado, tradición oral, recreo, rápido y suave. N.º 9: banda de rock, popular, radio, fuerte y rápida. Llevo 9 y faltan 11.",
        ["completa las tres entradas con datos", "clasifica bien las tradiciones", "calcula 9 y 11"],
        ["tabla escrita", "cálculo"],
        ["clasificar por gusto", "olvidar el contexto"],
        "Reconoce las tres entradas completas y revisa que 9 + 11 dé 20.",
    ),
    "Cuenta a una persona de tu casa qué tradiciones hay en tu bitácora.",
    "Diseña una tabla para tu propia bitácora con cinco columnas y llena una fila.",
)

# ---------------------------------------------------------------- OA 04 · clase 1
V1 = ["Su-be la lu-na", "so-bre el ce-rro", "y el vien-to duer-me", "en el sen-de-ro"]
V1_TXT = " / ".join(V1)
V1_SIL = [syl(v) for v in V1]

L(
    OA4, 1,
    f"Lápiz y papel. Un lugar tranquilo y un vaso de agua para beber antes de cantar. El texto de trabajo es una canción hablada original: «{V1_TXT}». Las sílabas se cuentan como se escriben, separadas con guiones, y cada sílaba es un golpe de palmas.",
    "Aprenderé a cantar al unísono cuidando la respiración y la escucha. Sirve para que un grupo cante como una sola voz.",
    ["Sé mantener el pulso con palmas.", "Sé que cantar fuerte no es gritar.", "Sé contar sílabas."],
    [
        "Cantar al unísono es cantar todos la misma melodía al mismo tiempo, con las mismas palabras y la misma duración. Para que el grupo suene como uno solo, cada persona escucha a los demás y mantiene el mismo pulso. Si oyes tu voz sobresalir, baja un poco.",
        f"Para contar sílabas, cada golpe de voz de una palabra es una sílaba, y los guiones del texto las separan. Las palabras cortas como «y» o «el» también cuentan una sílaba. La respiración marca las frases. Una frase es un trozo del texto que se canta en una sola respiración. En nuestro texto hay 4 frases: «{V1_TXT}». Tomas aire por la nariz, sin levantar los hombros, antes de cada frase. Si una frase tiene sílabas de más, puedes cantar más rápido, no cortar el aire.",
        "Cuida la voz: canta sin gritar, toma agua antes de cantar y haz un calentamiento suave, como un «mmm» y un suspiro largo. Si la garganta duele, descansa. Cantar bien no es cantar fuerte, es cantar parejo y atento a los demás.",
    ],
    [("unísono", "todos cantan la misma melodía a la vez"), ("frase", "trozo de música que se canta en una respiración"), ("respiración", "tomar y soltar aire para sostener la voz"), ("calentamiento", "ejercicios suaves antes de cantar"), ("pulso", "latido parejo")],
    [
        ("Contar sílabas de una frase", f"Frase: «{V1[0]}». ¿Cuántas sílabas tiene?", ["Se separan por guiones y espacios: Su, be, la, lu, na.", "Son 5 sílabas."], f"{V1_SIL[0]} sílabas"),
        ("Contar sílabas del texto", f"Texto: «{V1_TXT}». ¿Cuántas sílabas tiene en total?", [f"Frases de {', '.join(str(x) for x in V1_SIL)} sílabas.", f"{' + '.join(str(x) for x in V1_SIL)} = {sum(V1_SIL)}."], f"{sum(V1_SIL)} sílabas"),
    ],
    [
        ("Cantar más fuerte para escucharse bien.", "Un volumen alto cansa la voz y tapa a los demás.", "Escucha al grupo y canta a un volumen parejo."),
        ("Tomar aire en medio de una frase.", "Se corta la idea del texto.", "Respira entre frases, no dentro de ellas."),
    ],
    [
        ex(f"Frase: «{V1[1]}». ¿Cuántas sílabas tiene?", str(V1_SIL[1]), "so, bre, el, ce, rro: cinco."),
        ex(f"Frase: «{V1[2]}». ¿Cuántas sílabas tiene?", str(V1_SIL[2]), "y, el, vien, to, duer, me: seis."),
        ex("¿Cantar al unísono es cantar la misma melodía a la vez o cantar cada uno una melodía distinta?", "La misma melodía a la vez", "Unísono significa una misma melodía y al mismo tiempo."),
    ],
    [
        ex(f"Frase: «{V1[3]}». ¿Cuántas sílabas tiene?", str(V1_SIL[3]), "en, el, sen, de, ro: cinco."),
        ex(f"Texto: «{V1_TXT}». ¿Cuántas frases tiene?", "4", "Hay cuatro trozos separados por barras."),
        ex(f"Texto: «{V1_TXT}». ¿Cuál es la frase con más sílabas?", V1[2], "Tiene 6 sílabas y las otras 5."),
    ],
    [
        arith(f"Cantas las cuatro frases del texto «{V1_TXT}», una sílaba por pulso. ¿Cuántos pulsos cantas?", "+".join(str(x) for x in V1_SIL), "Se suman las sílabas de las cuatro frases.", " pulsos"),
        ex("Un grupo canta al unísono, pero una niña grita y se la oye más que a todos. ¿Qué debe hacer para mantener el unísono?", "Bajar el volumen y escuchar a los demás", "El unísono pide sonar parejo."),
    ],
    [
        ex("Pedro dice: «si respiro en el medio de una frase, canto mejor». ¿Es buena idea?", "No", "Respirar en medio de la frase corta la idea del texto."),
        arith(f"El texto «{V1_TXT}» se canta 3 veces seguidas. ¿Cuántas sílabas se cantan en total?", f"{sum(V1_SIL)}*3", "Se multiplican las sílabas del texto por 3.", " sílabas"),
    ],
    [
        arith("Cantas el texto completo 2 veces, con una respiración al comienzo de cada frase. ¿Cuántas respiraciones haces?", "4*2", "El texto tiene 4 frases y se canta 2 veces.", " respiraciones"),
        arith(f"La frase «{V1[2]}» tiene {V1_SIL[2]} sílabas y la frase «{V1[0]}» tiene {V1_SIL[0]}. ¿Cuántas sílabas más tiene la primera?", f"{V1_SIL[2]}-{V1_SIL[0]}", "Se restan las sílabas de las dos frases.", " sílaba"),
    ],
    [ex("Un curso canta al unísono el himno de su escuela y algunos se adelantan. ¿Qué pueden hacer para cantar parejo?", "Escuchar al grupo y marcar el mismo pulso", "Así todos cantan juntos.")],
    [ex("¿Qué es un unísono?", "Cantar la misma melodía a la vez", "Todos cantan lo mismo y al mismo tiempo."), ex("¿Dónde respiras: entre frases o dentro de ellas?", "Entre frases", "Así no se corta el texto."), ex("¿Cantar bien es cantar fuerte o cantar parejo?", "Cantar parejo", "Lo importante es sonar parejo y atento.")],
    (
        f"Di en voz suave el texto «{V1_TXT}» con una persona de tu casa, o tú solo, a un pulso parejo, con una palmada por sílaba. Haz un círculo en el papel donde respiras. Cuenta en voz baja las sílabas de cada frase y escribe cuántas sílabas hay en total. Luego repítelo cantando sobre un solo sonido cómodo, sin gritar.",
        f"Respiré al final de cada frase. Las sílabas fueron {', '.join(str(x) for x in V1_SIL)}, en total {sum(V1_SIL)}.",
        ["mantiene el pulso parejo", "respira entre frases", "cuenta las sílabas correctamente"],
        ["interpretación", "conteo escrito"],
        ["respirar en medio de la frase", "subir el volumen para sobresalir"],
        "Reconoce el pulso parejo y pide marcar con círculos las respiraciones; si grita, modela un volumen suave.",
    ),
    "Haz el calentamiento de voz: un «mmm» largo y un suspiro, tres veces.",
    "Inventa una frase de 5 sílabas, escríbela con guiones y dila al pulso con palmas.",
)

# ---------------------------------------------------------------- OA 04 · clase 2
FRASE_P = 4
FRASES = 4
TOTAL1 = FRASE_P * FRASES

L(
    OA4, 2,
    f"Lápiz y papel. Una cuerda o una línea dibujada para ordenar entradas. Canon de trabajo: un texto de {FRASES} frases de {FRASE_P} pulsos cada una (por ejemplo, el texto de la clase anterior). Una persona puede cantar sola y marcar las entradas con la mano.",
    "Aprenderé a sostener mi parte en un canon simple: entrar a tiempo y seguir mi propia línea. Sirve para cantar juntos partes que no empiezan a la vez.",
    ["Sé cantar al unísono.", "Sé mantener el pulso.", "Sé qué es una frase."],
    [
        "Un canon es una música en que todos cantan la misma melodía, pero cada voz entra en un momento distinto. La primera voz empieza sola. La segunda voz empieza cuando la primera termina su primera frase, y canta lo mismo desde el comienzo. Así las voces se superponen.",
        f"Cada entrada se cuenta en pulsos. Si cada frase tiene {FRASE_P} pulsos, la segunda voz entra después de {FRASE_P} pulsos. Si el texto tiene {FRASES} frases, el total de una voz es {FRASE_P} × {FRASES} = {TOTAL1} pulsos. Cuando entra la segunda voz, la primera va por su segunda frase.",
        "Para sostener tu parte: no te dejes llevar por la otra voz. Marca el pulso con el pie, mira la señal de entrada y canta tu línea. Si te pierdes, no pares: toma el pulso y vuelve a entrar al comienzo de la siguiente frase. Un canon sale bien cuando todas las voces mantienen el mismo pulso.",
    ],
    [("canon", "música en que las voces cantan lo mismo, entrando una después de otra"), ("entrada", "momento en que una voz comienza"), ("voz", "cada línea que se canta por separado"), ("señal", "gesto que avisa cuándo entrar"), ("superponerse", "sonar juntas en el mismo momento")],
    [
        ("Calcular el total de dos voces", f"Un canon a 2 voces tiene {FRASES} frases de {FRASE_P} pulsos. La segunda voz entra después de la primera frase. ¿Cuántos pulsos pasan hasta que ambas terminan?", [f"Una voz canta {FRASES} × {FRASE_P} = {TOTAL1} pulsos.", f"La segunda comienza {FRASE_P} pulsos más tarde.", f"{TOTAL1} + {FRASE_P} = {TOTAL1 + FRASE_P}."], f"{TOTAL1 + FRASE_P} pulsos"),
        ("Pulsos con las dos voces juntas", f"En el mismo canon, ¿cuántos pulsos suenan las dos voces a la vez?", [f"La voz 1 está sola los primeros {FRASE_P} pulsos.", f"La voz 2 está sola los últimos {FRASE_P}.", f"Juntas: {TOTAL1 + FRASE_P} − {FRASE_P} − {FRASE_P} = {TOTAL1 - FRASE_P}."], f"{TOTAL1 - FRASE_P} pulsos"),
    ],
    [
        ("Seguir a la otra voz y cantar su línea.", "Se pierde la propia parte.", "Escucha a las demás, pero canta lo tuyo."),
        ("Entrar apurado, antes de la señal.", "Se rompe el orden de las entradas.", "Cuenta los pulsos y entra en la señal."),
    ],
    [
        ex("En un canon, ¿cantan todas las voces lo mismo, entrando en distintos momentos, o cantan melodías diferentes?", "Lo mismo, en distintos momentos", "Esa es la idea de un canon."),
        ex(f"Si cada frase tiene {FRASE_P} pulsos, ¿después de cuántos pulsos entra la segunda voz?", str(FRASE_P), "La segunda voz entra al terminar la primera frase."),
        ex("Pierdes tu parte. ¿Sigues parando el canto o vuelves a entrar en la siguiente frase?", "Vuelves a entrar en la siguiente frase", "Así el canon no se detiene."),
    ],
    [
        arith(f"Un canon tiene {FRASES} frases de {FRASE_P} pulsos. ¿Cuántos pulsos canta una sola voz?", f"{FRASES}*{FRASE_P}", "Se multiplican las frases por los pulsos de cada una.", " pulsos"),
        ex(f"Con {FRASES} frases de {FRASE_P} pulsos, la segunda voz entra después de una frase. ¿En qué pulso empieza a cantar? (cuenta el 1 como el primer pulso)", str(FRASE_P + 1), "La primera voz usó los pulsos 1 a 4 y la segunda comienza en el 5."),
        ex("¿Qué debes hacer antes de entrar: contar pulsos y mirar la señal, o cantar apenas oigas a la otra voz?", "Contar pulsos y mirar la señal", "La entrada se hace por pulsos, no por imitar."),
    ],
    [
        arith(f"Un canon a 3 voces tiene {FRASES} frases de {FRASE_P} pulsos. Cada voz entra una frase después de la anterior. ¿Cuántos pulsos pasan hasta que terminan las tres?", f"{FRASES}*{FRASE_P}+2*{FRASE_P}", "La voz 3 entra 8 pulsos más tarde y canta 16: 8 + 16.", " pulsos"),
        ex("Un canon a 3 voces con frases de 4 pulsos. ¿En qué pulso entra la tercera voz? (el primer pulso es el 1)", "9", "La voz 3 entra tras dos frases (8 pulsos), así que empieza en el pulso 9."),
    ],
    [
        ex("Ana canta más fuerte para no perderse. Pedro dice que mejor marcar el pulso con el pie. ¿Qué consejo ayuda a mantener la parte?", "Marcar el pulso con el pie", "El pulso estable ayuda a mantener la parte sin gritar."),
        arith("Un grupo canta un canon a 2 voces de 12 pulsos cada una; la segunda voz entra 4 pulsos después. ¿Cuántos pulsos duran las dos juntas?", "12+4-4-4", "Total 16 menos 4 solo de la voz 1 y 4 solo de la voz 2.", " pulsos"),
    ],
    [
        arith("Un canon a 2 voces tiene 3 frases de 4 pulsos y la voz 2 entra después de una frase. ¿Cuántos pulsos pasan hasta que terminan las dos voces?", "3*4+4", "Una voz canta 12 pulsos y la otra empieza 4 después.", " pulsos"),
        arith("En ese mismo canon de 3 frases de 4 pulsos, ¿cuántos pulsos cantan las dos voces a la vez?", "3*4-4", "De los 12 pulsos de la voz 1, los primeros 4 los canta sola.", " pulsos"),
    ],
    [ex("En una ronda del recreo, un grupo canta un canon a 2 voces y una niña entra tarde. ¿Qué debe hacer el grupo para ayudarla?", "Marcar el pulso y mostrar la señal de entrada", "El pulso y la señal ayudan a reubicar su entrada.")],
    [ex("¿Qué es una entrada?", "El momento en que una voz comienza", "Es cuando una voz empieza a cantar."), ex("En un canon, ¿cantan todas lo mismo?", "Sí", "Cada voz canta la misma melodía."), ex("¿Cuánto dura un canon de 3 frases de 4 pulsos para una sola voz?", "12 pulsos", "3 × 4 = 12.")],
    (
        f"Con una persona de tu casa, canten o digan al pulso el texto «{V1_TXT}» como canon a 2 voces: una persona empieza y la otra entra al terminar la primera frase. Marquen el pulso con el pie y usen una señal de la mano para la entrada. Escribe cuántos pulsos canta una voz sola, en qué pulso entra la segunda y cuántos pulsos pasan hasta que las dos terminan, suponiendo que cada frase dura {FRASE_P} pulsos.",
        f"Una voz canta {TOTAL1} pulsos. La segunda entra en el pulso {FRASE_P + 1}. Las dos terminan a los {TOTAL1 + FRASE_P} pulsos.",
        ["mantiene su parte", "entra con la señal", "calcula los pulsos correctos"],
        ["interpretación en pareja", "cálculo escrito"],
        ["cantar la línea de la otra voz", "entrar antes de la señal"],
        "Reconoce la entrada a tiempo y pide que cuente en voz baja los pulsos; si se pierde, practica la frase sola.",
    ),
    "Canta dos frases con el pie marcando el pulso y cuenta en voz baja hasta 4 en cada frase.",
    "Dibuja con líneas dos voces de un canon, una empezando 4 pulsos después de la otra.",
)

# ---------------------------------------------------------------- OA 04 · clase 3
VA = (1, 1, 1, 1, 1, 1, 1, 1)          # 1 sonido por pulso
VB = (1, 0, 2, 1, 0, 2, 1, 1)           # TA SIL TT TA SIL TT TA TA -> sonidos por pulso (TT=2 sonidos)


def coinciden(a, b):
    return sum(1 for x, y in zip(a, b) if x and y)


def letras(v):
    return " ".join({0: "SIL", 1: "TA", 2: "ti-ti"}[x] for x in v)


L(
    OA4, 3,
    f"Lápiz y papel. Si quieres practicar, usa dos recipientes de plástico o cajas para golpear con las manos, a volumen bajo. Parte A (pulso): {letras(VA)}. Parte B (ritmo): {letras(VB)}.",
    "Aprenderé a coordinar percusión con el pulso y los acentos. Sirve para tocar en grupo sin tapar a los demás.",
    ["Sé contar pulsos.", "Sé qué es un acento.", "Sé leer TA, ti-ti y SIL."],
    [
        "Los instrumentos de percusión se tocan golpeando, sacudiendo o raspando. Pueden ser de parche (tambores), de madera (claves) o de metal (triángulo). En un grupo, uno puede llevar el pulso y otro tocar un ritmo sobre ese pulso. Los dos deben escuchar al otro para no tapar su sonido.",
        f"Un ejemplo con ocho pulsos. Parte A, que lleva el pulso: {letras(VA)}. Parte B, que toca un ritmo: {letras(VB)}. En el pulso 2 de B hay silencio y en el 3 hay ti-ti. Las partes coinciden cuando suenan en el mismo pulso: aquí coinciden en {coinciden(VA, VB)} de 8 pulsos.",
        "El acento marca el primer pulso de cada grupo. En grupos de 4, el acento va en los pulsos 1 y 5. Para tocarlo, golpea un poco más fuerte, sin gritar con el instrumento. Cuida también tus oídos y tus instrumentos: toca a volumen bajo, no golpees con demasiada fuerza y guarda el material ordenado.",
    ],
    [("percusión", "instrumentos que se tocan golpeando, sacudiendo o raspando"), ("parche", "piel o plástico tenso de un tambor"), ("acento", "pulso que se marca más fuerte"), ("coordinar", "tocar juntos de manera ordenada"), ("silencio", "pulso en que no suena nada")],
    [
        ("Contar coincidencias", f"Parte A: {letras(VA)}. Parte B: {letras(VB)}. ¿En cuántos de los 8 pulsos suenan las dos a la vez?", ["Reviso pulso por pulso.", "B suena en 1, 3, 4, 6, 7 y 8; en 2 y 5 hay silencio.", "A suena en todos."], f"{coinciden(VA, VB)} pulsos"),
        ("Ubicar los acentos", "Se cuenta de a 4 durante 12 pulsos. ¿En qué pulsos va el acento?", ["Los grupos son 1-4, 5-8 y 9-12.", "El acento va al inicio de cada grupo."], "En los pulsos 1, 5 y 9"),
    ],
    [
        ("Golpear fuerte para que se oiga más.", "Tapa a los demás y cansa los oídos.", "Toca parejo y escucha al grupo."),
        ("Saltarse el pulso en silencio.", "El silencio también ocupa un pulso.", "Cuenta el silencio en voz baja."),
    ],
    [
        ex(f"Parte A: {letras(VA)}. ¿Cuántos pulsos tiene?", "8", "Hay 8 símbolos y cada uno ocupa un pulso."),
        ex("Se cuenta de a 4. ¿En qué pulsos va el acento si son 8 pulsos?", "1 y 5", "Cada grupo de 4 empieza con un acento."),
        ex("¿De qué material es un triángulo de percusión?", "Metal", "El triángulo es de metal."),
    ],
    [
        ex(f"Parte B: {letras(VB)}. ¿Cuántos pulsos tienen silencio?", "2", "Hay SIL en los pulsos 2 y 5."),
        ex(f"Parte B: {letras(VB)}. ¿Cuántos sonidos tocas en total (ti-ti cuenta dos)?", str(sum(VB)), "1 + 0 + 2 + 1 + 0 + 2 + 1 + 1."),
        ex("Un tambor de parche, unas claves de madera y un triángulo de metal. ¿Cuál es el de madera?", "Las claves", "Las claves son de madera."),
    ],
    [
        ex(f"Parte A: {letras(VA)}. Parte B: {letras(VB)}. ¿En qué pulsos de B hay silencio, mientras A sigue sonando?", "2 y 5", "B tiene SIL en esos dos pulsos y A suena siempre."),
        arith("Si el pulso se toca 8 veces por vuelta y das 5 vueltas, ¿cuántos pulsos tocas?", "8*5", "8 pulsos por vuelta por 5 vueltas.", " pulsos"),
        ex("Un grupo toca de a 4 durante 16 pulsos. ¿Cuántos acentos hay?", "4", "16 pulsos en grupos de 4 son 4 grupos."),
    ],
    [
        ex("Ana toca el pulso con un tambor y Pedro un ritmo con claves, pero Pedro suena tan fuerte que no se oye el tambor. ¿Qué debe hacer?", "Tocar más suave", "Debe tocar a un volumen que deje oír al otro."),
        ex(f"Parte A: {letras(VA)}. Parte B: {letras(VB)}. ¿En qué pulsos de B suenan dos sonidos rápidos?", "3 y 6", "Son los pulsos con ti-ti."),
    ],
    [
        arith("En una práctica, 3 grupos tocan 8 pulsos cada uno en fila, uno después del otro. ¿Cuántos pulsos suenan en total?", "3*8", "Son 3 grupos de 8 pulsos.", " pulsos"),
        ex("Un curso toca percusión en grupos de 4 durante 16 pulsos, con acento en cada primer pulso. Si el acento dura un golpe más fuerte, ¿cuántos golpes fuertes se dan?", "4", "Hay un golpe fuerte por grupo de 4 pulsos."),
    ],
    [ex("En la banda del curso, una niña toca triángulo y otro tambor. ¿Qué deben acordar antes de empezar?", "El pulso y el volumen", "Acordar pulso y volumen evita taparse.")],
    [ex("¿Para qué sirve el acento?", "Marca el primer pulso de cada grupo", "Ayuda a no perderse."), ex("¿Qué haces con un pulso en silencio?", "Lo cuentas", "El silencio ocupa un pulso."), ex("¿Cómo cuidas tus oídos al tocar percusión?", "Tocas a volumen bajo", "Evita golpear con demasiada fuerza.")],
    (
        f"Con dos recipientes de plástico (o con las palmas y los muslos), toca la Parte A (pulso) con una mano y la Parte B (ritmo) con la otra: A: {letras(VA)}; B: {letras(VB)}. Hazlo despacio, a volumen bajo y marcando el acento en los pulsos 1 y 5. Después escribe en cuántos pulsos suenan A y B a la vez y cuáles son los pulsos con silencio en B.",
        f"Suenan juntas en {coinciden(VA, VB)} pulsos. Los silencios de B son los pulsos 2 y 5.",
        ["mantiene el pulso parejo", "marca los acentos en 1 y 5", "responde las dos preguntas"],
        ["interpretación", "respuesta escrita"],
        ["tocar tan fuerte que tapa la otra parte", "saltarse los silencios"],
        "Reconoce el pulso estable y pide que diga el pulso del silencio; si acelera, vuelve a tocar despacio.",
    ),
    "Golpea suavemente 8 pulsos con las palmas y marca más fuerte el 1 y el 5.",
    "Crea una Parte B distinta de 8 pulsos con TA, ti-ti y SIL, y cuenta sus sonidos.",
)

# ---------------------------------------------------------------- OA 04 · clase 4
INTRO, VUELTAS, VPUL, FINAL = 4, 3, 16, 2
TOTAL_INT = INTRO + VUELTAS * VPUL + FINAL

L(
    OA4, 4,
    f"Lápiz y papel. Si tienes un instrumento melódico en el colegio (metalófono o flauta dulce) úsalo con la guía de tu profesor; si no, usa tu voz. Plan de trabajo: introducción de {INTRO} pulsos, {VUELTAS} vueltas de {VPUL} pulsos y final de {FINAL} pulsos.",
    "Aprenderé a integrar voz e instrumento en una interpretación, cuidando el equilibrio y el orden de las entradas. Sirve para tocar y cantar juntos sin taparnos.",
    ["Sé cantar al unísono.", "Sé tocar un pulso con percusión.", "Sé seguir una señal de entrada."],
    [
        "Un instrumento melódico toca notas distintas. El metalófono tiene barras de metal: las barras largas suenan graves y las cortas suenan agudas. Se golpea con un macillo en el centro de la barra y se levanta rápido para que suene; los macillos se alternan, derecho e izquierdo. La flauta dulce se sopla suave; si se sopla fuerte, chilla. Cada estudiante usa su propia flauta o la limpia con ayuda de un adulto antes de compartirla.",
        "Tres notas para empezar en la flauta dulce, con la mano izquierda arriba (el pulgar tapa el agujero de atrás y los demás dedos tapan los agujeros de adelante, de arriba hacia abajo). SI: pulgar e índice, 2 dedos. LA: pulgar, índice y medio, 3 dedos. SOL: pulgar, índice, medio y anular, 4 dedos. Para pasar de SOL a LA se levanta el anular, y de LA a SI se levanta el medio. Tapa los agujeros con la yema del dedo, sin apretar, y sopla suave.",
        f"Para integrar voz e instrumento, ensayamos un plan de trabajo. Por ejemplo: introducción de {INTRO} pulsos, {VUELTAS} vueltas de {VPUL} pulsos y un final de {FINAL} pulsos. En total son {INTRO} + {VUELTAS} × {VPUL} + {FINAL} = {TOTAL_INT} pulsos. Con ese plan todos saben cuándo entrar, cuándo cantar y cuándo terminar.",
        "Lo más importante es el equilibrio: la voz y el instrumento deben oírse parejo. Si el instrumento suena más fuerte, baja su volumen. Entra con la señal, mantiene el pulso y escucha a quien canta. Al terminar, guarda el material con cuidado y agradece al grupo.",
    ],
    [("instrumento melódico", "instrumento que toca notas distintas"), ("metalófono", "instrumento de barras de metal que se toca con macillos"), ("flauta dulce", "instrumento de viento que se sopla suave"), ("equilibrio", "que voz e instrumento se oigan parejo"), ("plan de trabajo", "orden de las partes de una interpretación")],
    [
        ("Calcular la duración", f"Plan: introducción de {INTRO} pulsos, {VUELTAS} vueltas de {VPUL} y final de {FINAL}. ¿Cuántos pulsos suenan en total?", [f"{VUELTAS} × {VPUL} = {VUELTAS * VPUL}.", f"{INTRO} + {VUELTAS * VPUL} + {FINAL} = {TOTAL_INT}."], f"{TOTAL_INT} pulsos"),
        ("Barra grave", "En un metalófono, ¿qué barra suena más grave: la más larga o la más corta?", ["En los instrumentos de barras, lo largo suena más hondo.", "La barra larga vibra más lento."], "La más larga"),
    ],
    [
        ("Soplar fuerte la flauta dulce para que se oiga.", "Chilla y suena desafinada.", "Sopla suave y parejo."),
        ("Tocar el metalófono sin esperar la señal de entrada.", "Se rompe el orden del plan de trabajo.", "Cuenta los pulsos y entra con la señal."),
    ],
    [
        ex("¿La barra corta de un metalófono suena aguda o grave?", "Aguda", "Las barras cortas suenan agudas."),
        ex("¿La flauta dulce se sopla suave o fuerte?", "Suave", "Si se sopla fuerte, chilla."),
        ex("Para tocar LA en la flauta dulce, ¿qué dedos tapan los agujeros de la mano izquierda?", "Pulgar, índice y medio", "LA usa 3 dedos: pulgar, índice y medio."),
    ],
    [
        ex(f"Plan: introducción de {INTRO} pulsos y {VUELTAS} vueltas de {VPUL} pulsos. ¿Cuántos pulsos hay en las tres vueltas?", str(VUELTAS * VPUL), "3 × 16."),
        ex("¿Qué haces si el instrumento suena más fuerte que la voz?", "Bajar el volumen del instrumento", "Así se mantiene el equilibrio."),
        ex("Pasas de SOL a LA en la flauta dulce. ¿Qué dedo levantas?", "El anular", "SOL tapa también con el anular; LA no."),
    ],
    [
        arith(f"El plan tiene introducción de {INTRO}, {VUELTAS} vueltas de {VPUL} y final de {FINAL}. ¿Cuántos pulsos hay antes del final?", f"{INTRO}+{VUELTAS}*{VPUL}", "Se suman la introducción y las vueltas.", " pulsos"),
        ex(f"Cantas en las 3 vueltas, pero no en la introducción ni en el final. ¿Cuántos pulsos cantas?", str(VUELTAS * VPUL), "Solo cantas en las vueltas: 3 × 16."),
        ex("¿Qué nota de la flauta dulce de esta clase usa menos dedos: SI, LA o SOL?", "SI", "SI usa solo 2 dedos: pulgar e índice."),
    ],
    [
        ex("Ana toca la flauta dulce con tanta fuerza que se oye chillar. ¿Qué debe cambiar?", "Soplar más suave", "Un soplido suave evita el chillido."),
        arith("Para tocar SOL usas 4 dedos y para tocar SI usas 2. ¿Cuántos dedos más usas en SOL que en SI?", "4-2", "Se restan los dedos de SI a los de SOL.", " dedos"),
    ],
    [
        ex("Una niña sopla la flauta de otra persona sin limpiarla. ¿Por qué no es buena idea?", "Por higiene", "La boquilla se comparte solo con limpieza."),
        arith(f"El plan de {TOTAL_INT} pulsos se ensaya 2 veces seguidas. ¿Cuántos pulsos se ensayan?", f"{TOTAL_INT}*2", "Se multiplica la duración del plan por 2.", " pulsos"),
    ],
    [ex("En un acto del colegio, un grupo canta y toca metalófono. ¿Qué dos acuerdos hacen que suene mejor?", "Mantener el pulso y cuidar el equilibrio", "Así voz e instrumento suenan parejo.")],
    [ex("¿Cómo suena una barra larga?", "Grave", "Las barras largas suenan graves."), ex("¿Qué es el equilibrio?", "Que la voz y el instrumento se oigan parejo", "Ninguno tapa al otro."), ex("En Música: ¿Qué haces con el material al terminar?", "Lo guardas con cuidado", "Cuidar los instrumentos es parte de tocar.")],
    (
        f"Con voz y un objeto que haga de instrumento (dos recipientes de plástico, por ejemplo), ensaya este plan: introducción de {INTRO} pulsos tocando solo el objeto, {VUELTAS} vueltas de {VPUL} pulsos cantando el texto «{V1_TXT}» con el objeto marcando el pulso suave (cada frase del texto ocupa 4 pulsos, así que cada vuelta es el texto completo), y final de {FINAL} pulsos solo con el objeto. Escribe cuántos pulsos suenan en total y cómo cuidaste que la voz y el objeto se oyeran parejo.",
        f"Suenan {TOTAL_INT} pulsos en total. Toqué el objeto más suave que mi voz para mantener el equilibrio.",
        ["sigue el plan de trabajo", "mantiene el equilibrio entre voz y objeto", "calcula el total de pulsos"],
        ["interpretación", "explicación escrita"],
        ["tocar el objeto tan fuerte que tapa la voz", "perder el orden de entradas"],
        "Reconoce el cumplimiento del plan y pregunta cómo supo que la voz se oía; si hay descuido, sugiere bajar el objeto.",
    ),
    "Practica soplar suave sin instrumento, como para empañar un espejo, durante 4 pulsos. Con una flauta de tu colegio, practica SI con la mano izquierda.",
    "Escribe un plan de trabajo con introducción, tres vueltas y final para otro texto.",
)
