"""Student material for 8.º básico Música, OA 01 (comunicar sentimientos, sensaciones e ideas al escuchar músicas de Chile y el mundo, de tradición oral, escrita y popular, por medios verbales, visuales, sonoros y corporales).

Todas las audiciones de los ejercicios son descripciones y mapas inventados («de ejemplo») para esta clase; las audiciones reales las selecciona y pone el docente.
Este módulo define el ayudante L (y task) que usan los demás módulos mu8_*.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1 = "MU08 OA 01"


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, tk, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[dict(title=t, problem=p, steps=s, answer=a) for t, p, s, a in worked],
        mistakes=[dict(wrong=w, why=y, fix=f) for w, y, f in mistakes],
        tiers=dict(recovery=R, understand=C, apply=A, reason=Z, challenge=D),
        context=ctx, selfcheck=sc, open_task=task(*tk), reinforce=reinforce, extend=extend,
    )


MAPA = ("0–12 s: flauta sola, suave. 12–30 s: guitarra y bombo, volumen medio. 30–45 s: guitarra, bombo y flauta, fuerte. "
        "45–50 s: silencio. 50–70 s: flauta sola, suave")

# ---------------------------------------------------------------- OA 01 · clase 1 (registrar antes de nombrar)
L(
    OA1, 1,
    "Lápiz y papel. Los fragmentos musicales están descritos con palabras en los ejercicios (son de ejemplo). Si una persona de tu casa puede tararear una melodía o poner una canción a volumen bajo, también sirve, pero no es necesario.",
    "Aprenderé a registrar lo que se oye antes de ponerle nombre, y a separar cuatro tipos de frase: hecho audible, sensación, imagen e interpretación. Sirve para responder a la música con evidencia y sin decir que todos sienten lo mismo.",
    ["Sé que la música tiene pulso, ritmo, melodía y volumen.", "Sé distinguir lo fuerte de lo suave y lo rápido de lo lento.", "Sé escribir una frase con «porque»."],
    [
        "Al escuchar música conviene registrar primero y nombrar después. Un hecho audible es algo que cualquiera puede comprobar volviendo a escuchar, como «la melodía sube» o «entra un tambor». Una sensación es lo que siento, como calma o inquietud. Una imagen es una escena que imagino, como «una procesión por una calle». Una interpretación es mi idea sobre lo que la música comunica, apoyada en un hecho audible.",
        "La interpretación es válida cuando dice de quién es y cuál es su evidencia: «Para mí comunica tensión, porque el bajo repite la misma nota y el volumen sube». Es un error presentar una sensación como significado universal, por ejemplo «esta música es triste para todos». Dos personas pueden interpretar distinto el mismo fragmento y ambas pueden tener razón, si cada una cita lo que se oye.",
        "Una buena respuesta sigue tres pasos: escuchar y anotar un hecho audible; nombrar mi sensación o imagen; unirlas con «porque». Si falta el hecho audible, la frase es solo una opinión. Para anotar sin demora, conviene escuchar el fragmento más de una vez: la primera para sentir y las siguientes para comprobar qué se oye y en qué momento.",
    ],
    [("hecho audible", "algo que se oye y que cualquiera puede comprobar"), ("sensación", "lo que siento al escuchar, como calma o inquietud"), ("imagen", "escena o recuerdo que imagino al escuchar"), ("interpretación", "mi idea de lo que la música comunica, apoyada en un hecho audible"), ("evidencia", "el dato audible que sostiene lo que digo")],
    [
        ("Clasificar una frase", "Clasifica la frase «Un violonchelo repite tres notas graves» como hecho audible, sensación, imagen o interpretación.", ["Se puede comprobar escuchando: instrumento, repetición y notas graves.", "No dice qué siento ni qué imagino."], "Es un hecho audible"),
        ("Corregir una afirmación universal", "Una compañera dice: «Esta música es triste para todos». ¿Cómo la convertimos en una interpretación válida si lo que se oye es una melodía lenta que baja?", ["Se cambia «para todos» por «para mí».", "Se agrega la evidencia con «porque»."], "«Para mí suena triste, porque la melodía es lenta y baja»"),
    ],
    [
        ("Creer que, si dos personas interpretan distinto, una se equivoca.", "Las interpretaciones pueden diferir; lo que se revisa es si cada una cita algo audible.", "Pregunta a cada persona qué escuchó que sostiene su idea."),
        ("Poner «es alegre» como si fuera un hecho audible.", "Alegre es una sensación; lo que se oye es, por ejemplo, un tempo rápido.", "Cambia «es alegre» por «me alegra porque va rápido y fuerte»."),
    ],
    [
        ex("La frase «Siento inquietud» ¿es un hecho audible, una sensación, una imagen o una interpretación?", "Una sensación", "Dice lo que siente la persona, no lo que suena."),
        ex("La frase «Me hace ver una procesión que avanza por una calle de pueblo» ¿es hecho audible, sensación, imagen o interpretación?", "Una imagen", "Es una escena que la persona imagina."),
        ex("La frase «Los tambores suenan más fuerte que la guitarra» ¿es hecho audible, sensación, imagen o interpretación?", "Un hecho audible", "Cualquiera puede comprobarlo volviendo a escuchar."),
    ],
    [
        ex("¿Cuál frase es un hecho audible? A) Es una música muy bonita. B) El bajo repite la misma nota cuatro veces.", "B", "Repetir una nota cuatro veces se puede comprobar; «bonita» es una opinión."),
        ex("Una persona dice: «Esa música comunica soledad para todo el mundo». ¿Qué defecto tiene? A) Presenta su sensación como si fuera universal. B) Nombra demasiados instrumentos.", "A", "Una sensación personal no se puede declarar válida para todos."),
        ex("Tomás siente alegría con un fragmento y Ana siente nostalgia con el mismo, y cada uno cita lo que escuchó. ¿Pueden tener razón los dos? Responde sí o no.", "Sí", "Las interpretaciones pueden diferir si cada una se apoya en un hecho audible."),
    ],
    [
        ex("Lee: «Una guitarra toca acordes lentos. Me da nostalgia. Un coro entra en el segundo 20. Imagino un atardecer». ¿Cuántos hechos audibles hay?", "2", "Son los acordes lentos de la guitarra y la entrada del coro; la nostalgia y el atardecer no se oyen."),
        ex("Fragmento: un bombo suena fuerte y rápido. ¿Qué evidencia sostiene la frase «siento energía»? A) El bombo suena fuerte y rápido. B) El fragmento dura un minuto.", "A", "El volumen y la velocidad se oyen y explican la energía; la duración no la explica."),
        ex("Ordena los pasos de una buena respuesta: 1) nombrar mi sensación; 2) escuchar y anotar un hecho audible; 3) unirlos con «porque». Escribe los números en orden.", "2, 1, 3", "Primero se registra lo que se oye, luego se nombra la sensación y al final se unen."),
    ],
    [
        ex("Pedro escribió: «La melodía sube, por eso toda persona sentirá esperanza». ¿Qué parte de su frase hay que cambiar para que sea una interpretación válida: «la melodía sube» o «toda persona»?", "«Toda persona»", "Hay que decir «yo» o «para mí», porque la sensación es personal; que la melodía sube es evidencia."),
        ex("Dos descripciones del mismo fragmento. A) «Se oye muy antiguo». B) «A los 10 segundos un violín toca una melodía que baja». ¿Cuál entrega mejor evidencia?", "B", "Dice qué instrumento, cuándo y qué hace la melodía; la otra es una impresión."),
    ],
    [
        arith("Un fragmento dura 1 minuto 30 segundos (90 segundos). Lo escuchas 3 veces seguidas con 10 segundos de pausa entre una escucha y otra. ¿Cuántos segundos dura toda la sesión?", "90*3+10*2", "Hay tres escuchas y dos pausas entre ellas.", " segundos"),
        ex("Un estudiante anota en la primera escucha lo que siente y en la segunda y tercera escucha anota hechos audibles. ¿En qué escucha comprueba la evidencia por primera vez: en la primera, la segunda o la tercera?", "En la segunda", "La primera escucha es para sentir; desde la segunda busca y comprueba qué se oye."),
    ],
    [ex("En un acto escolar suena un fragmento rápido con percusión. Un compañero dice «eso significa fiesta para todos». ¿Qué respuesta es más adecuada? A) «Para mí suena a fiesta, porque el pulso es rápido y entra la percusión». B) «Tienes razón: esa música siempre significa fiesta».", "A", "Usa «para mí» y da evidencia audible, sin declarar un significado universal.")],
    [ex("¿Qué palabra une la sensación con la evidencia?", "Porque", "Conecta lo que siento con lo que se oye."), ex("«Me acuerdo de una fiesta de mi barrio»: ¿es hecho audible, sensación, imagen o interpretación?", "Una imagen", "Es un recuerdo o escena que la música despierta."), ex("¿Qué conviene hacer primero: registrar lo que se oye o poner un nombre a lo que comunica?", "Registrar lo que se oye", "Se anota el hecho audible antes de interpretar.")],
    (
        "Lee estos dos fragmentos de ejemplo. Fragmento 1: un piano toca notas largas y graves, muy suave, y la melodía baja despacio. Fragmento 2: un tambor y una flauta tocan rápido y fuerte, con notas cortas, y la melodía sube. Elige uno y completa una tabla con cuatro columnas: «Se oye» (dos hechos audibles), «Siento» (una sensación), «Imagino» (una escena) y «Interpreto» (una frase con «para mí… porque…»).",
        "Fragmento 1. Se oye: notas graves y largas; melodía que baja despacio. Siento: calma. Imagino: una noche sin viento. Interpreto: «Para mí comunica quietud, porque el piano toca grave, muy suave y la melodía baja despacio».",
        ["separa hechos audibles, sensación, imagen e interpretación", "da al menos dos hechos audibles", "usa «para mí» y «porque» en la interpretación"],
        ["tabla de cuatro columnas", "frase final con evidencia"],
        ["poner una sensación en la columna «Se oye»", "decir «es triste para todos»"],
        "Reconoce la tabla y pide señalar, para la sensación elegida, qué dato de la columna «Se oye» la sostiene.",
    ),
    "Escribe tres frases sobre una música que conozcas: un hecho audible, una sensación y una imagen.",
    "Escribe dos interpretaciones distintas del mismo fragmento, cada una con su propia evidencia audible.",
)

# ---------------------------------------------------------------- OA 01 · clase 2 (localizar rasgos en el tiempo: mapa de escucha)
L(
    OA1, 2,
    f"Lápiz y papel. Mapa de escucha de ejemplo, que se repite en los ejercicios: {MAPA}. Si quieres, usa un reloj con segundos para seguir el mapa mientras tarareas.",
    "Aprenderé a hacer un mapa de escucha: anotar en qué segundo cambia lo que suena (instrumentos, dinámica, silencio). Sirve para localizar rasgos audibles con exactitud y sostener mis respuestas con el momento preciso.",
    ["Sé separar hechos audibles de sensaciones.", "Sé que la dinámica es qué tan fuerte o suave suena la música.", "Sé leer minutos y segundos."],
    [
        "Un mapa de escucha es una línea de tiempo donde se anota qué pasa en cada tramo: qué instrumentos suenan, qué tan fuerte, y dónde hay silencio. Cada tramo se marca con segundos de inicio y de término. Así dejamos de decir «al medio cambia» y podemos decir «a los 30 segundos entra la flauta y sube el volumen». Esa precisión es lo que permite que otra persona compruebe mi respuesta.",
        "Para armar un mapa, se escucha una vez completa sin anotar y luego se vuelve a escuchar buscando los cambios. Cada cambio es una marca: la entrada de un instrumento, el paso de suave a fuerte, o un silencio. Entre dos marcas hay un tramo, y la duración del tramo se calcula restando: si un tramo va de 12 a 30 segundos, dura 30 − 12 = 18 segundos.",
        "Con un mapa también se pueden hacer cálculos. Si el pulso es de 60 por minuto, hay un pulso por segundo; a 120 por minuto hay dos por segundo. Un tramo de 15 segundos tiene entonces 15 pulsos a 60 por minuto y 30 pulsos a 120. Un silencio en el mapa sigue contando como tiempo de la pieza, porque la música también se organiza con pausas.",
    ],
    [("mapa de escucha", "línea de tiempo que anota qué suena en cada tramo"), ("marca", "segundo exacto en que cambia algo"), ("tramo", "parte de la pieza entre dos marcas"), ("dinámica", "qué tan fuerte o suave suena la música"), ("silencio", "pausa en que no suena nada, pero que también cuenta como tiempo")],
    [
        ("Medir un tramo", f"Mapa: {MAPA}. ¿Cuántos segundos dura el tramo en que la música es fuerte?", ["El tramo fuerte va de 30 a 45 segundos.", "45 − 30 = 15."], "15 segundos"),
        ("Buscar un momento", f"Mapa: {MAPA}. ¿Qué suena en el segundo 60?", ["El segundo 60 está entre 50 y 70.", "En ese tramo suena la flauta sola, suave."], "La flauta sola, suave"),
    ],
    [
        ("Anotar «en el medio» sin decir el segundo.", "Otra persona no puede comprobar un momento que no está ubicado.", "Anota siempre el segundo de inicio y el de término."),
        ("Olvidar el silencio como parte del mapa.", "El silencio también ocupa tiempo y cambia el efecto de la música.", "Márcalo como un tramo con sus segundos."),
    ],
    [
        ex(f"Mapa: {MAPA}. ¿Qué suena en el segundo 20?", "Guitarra y bombo", "El segundo 20 está en el tramo de 12 a 30 segundos."),
        ex(f"Mapa: {MAPA}. ¿En qué segundo comienza el silencio?", "En el segundo 45", "El tramo fuerte termina en 45 y ahí empieza el silencio."),
        ex(f"Mapa: {MAPA}. ¿Cuántos instrumentos distintos suenan entre los segundos 30 y 45?", "3", "Suenan guitarra, bombo y flauta."),
    ],
    [
        arith(f"Mapa: {MAPA}. ¿Cuántos segundos dura el silencio?", "50-45", "Se resta el segundo en que empieza del segundo en que termina.", " segundos"),
        ex(f"Mapa: {MAPA}. ¿Cuántas veces cambia lo que suena a lo largo de toda la pieza? Cuenta las marcas interiores (12, 30, 45 y 50).", "4", "Hay cuatro marcas interiores, que separan cinco tramos."),
        ex(f"Mapa: {MAPA}. La flauta suena sola al comienzo y al final. ¿En qué dos tramos? A) De 0 a 12 y de 50 a 70 segundos. B) De 12 a 30 y de 45 a 50 segundos.", "A", "Esos son los tramos en que solo suena la flauta."),
    ],
    [
        arith(f"Mapa: {MAPA}. ¿Cuántos segundos de la pieza tienen sonido, sin contar el silencio? La pieza dura 70 segundos.", "70-5", "Se resta el silencio de 5 segundos al total.", " segundos"),
        arith(f"Mapa: {MAPA}. ¿Cuántos segundos suena la flauta sola en total, sumando el comienzo y el final?", "12+(70-50)", "Se suma el primer tramo de 12 segundos y el último de 20.", " segundos"),
        ex("Quieres anotar el momento en que el bombo entra por primera vez en el mapa de ejemplo. ¿Qué segundo anotas?", "El segundo 12", "El bombo aparece en el tramo que empieza en 12."),
    ],
    [
        ex(f"Mapa: {MAPA}. Luis dice «el volumen es siempre fuerte». ¿Cuántos tramos con sonido lo contradicen? Son los tramos suaves o de volumen medio.", "3", "Contradicen los tramos de 0–12, 12–30 y 50–70."),
        ex(f"Mapa: {MAPA}. Camila dice «al final vuelve el comienzo». ¿Es un hecho audible comprobable con el mapa? Responde sí o no.", "Sí", "Los tramos de 0–12 y 50–70 se describen igual: flauta sola y suave."),
    ],
    [
        arith("Una pieza va a 120 pulsos por minuto, es decir, 2 pulsos por segundo. En el mapa de ejemplo, el silencio dura 5 segundos. ¿Cuántos pulsos caben en ese silencio?", "2*5", "Se multiplican los pulsos por segundo por los segundos de silencio.", " pulsos"),
        arith("Una pieza va a 60 pulsos por minuto, es decir, 1 pulso por segundo. En el mapa de ejemplo, el tramo de 12 a 30 segundos tiene guitarra y bombo. ¿Cuántos pulsos tiene ese tramo?", "30-12", "A un pulso por segundo, los pulsos coinciden con los segundos del tramo.", " pulsos"),
    ],
    [ex("En un ensayo de la banda escolar graban 40 segundos de música. Marcan una entrada de trompeta en el segundo 14 y otra en el segundo 31. ¿Cuántos segundos hay entre las dos entradas?", "17 segundos", "Se resta 31 − 14 y da 17.")],
    [ex("¿Qué es una marca en un mapa de escucha?", "El segundo exacto en que cambia algo", "Sirve para ubicar con precisión el cambio."), ex("¿Cómo se calcula la duración de un tramo?", "Restando el segundo de inicio al de término", "Por ejemplo, 30 − 12 da 18 segundos."), ex("¿El silencio cuenta como parte del tiempo de la pieza? Responde sí o no.", "Sí", "Ocupa tiempo aunque no suene nada.")],
    (
        "Usa este guion de ejemplo: «0–8 s: tambor solo, fuerte. 8–20 s: tambor y voz, volumen medio. 20–24 s: silencio. 24–40 s: tambor, voz y flauta, fuerte». Dibuja una línea de tiempo con las marcas 0, 8, 20, 24 y 40, escribe qué suena en cada tramo y calcula cuánto dura cada uno. Termina con una frase: «A los … segundos pasa …, y por eso siento …».",
        "Tramos: 8 s (tambor solo), 12 s (tambor y voz), 4 s (silencio), 16 s (tambor, voz y flauta). Frase: «A los 24 segundos entra la flauta y el volumen sube, y por eso siento más energía».",
        ["marca bien los cinco puntos de tiempo", "calcula las duraciones restando", "da un segundo exacto en la frase final"],
        ["línea de tiempo", "cuatro duraciones", "frase con segundo exacto"],
        ["olvidar el silencio como tramo", "no restar bien los segundos"],
        "Reconoce la línea de tiempo y pide comprobar una de las duraciones restando de nuevo.",
    ),
    "Cuenta 10 segundos mirando un reloj y anota un sonido que ocurra en tu casa en ese tiempo.",
    "Haz un mapa de escucha de 30 segundos de los sonidos de tu casa o de tu calle, con tres marcas.",
)

# ---------------------------------------------------------------- OA 01 · clase 3 (lenguaje musical, propósito y tradición oral, escrita y popular)
L(
    OA1, 3,
    "Lápiz y papel. Todas las músicas están descritas con palabras en los ejercicios (son de ejemplo). Si quieres, tararea cada propósito: una canción para dormir, una marcha y una música para bailar.",
    "Aprenderé a relacionar lo que se oye (pulso, tempo, dinámica) con el propósito de una música, y a reconocer si una música es de tradición oral, escrita o popular. Sirve para comprender por qué una música suena como suena.",
    ["Sé que el pulso es el latido parejo de la música.", "Sé distinguir un tempo lento de uno rápido.", "Sé que una partitura es música escrita."],
    [
        "Muchas músicas se hacen con un propósito: arrullar, marchar, bailar, acompañar un trabajo o celebrar. El propósito influye en cómo suena. Una música para arrullar suele ser lenta, suave y con una melodía que se repite. Una marcha tiene un pulso muy marcado, para que un grupo camine al mismo paso. Una música para bailar necesita un pulso claro y constante, para saber cuándo mover el cuerpo.",
        "Según cómo se transmite, la música puede ser de tradición oral, escrita o popular. La tradición oral se aprende de oído, de persona a persona, sin partitura, y cada versión cambia un poco. La tradición escrita se guarda en una partitura que otras personas leen para interpretarla casi igual. La música popular circula entre mucha gente por la radio, internet o las fiestas, y se escucha y se baila en la vida cotidiana. Una misma pieza puede ser a la vez popular y oral, por eso en cada ejercicio se dice cómo se transmite.",
        "Escuchar con propósito significa preguntarse para qué sirve la música y qué rasgos lo muestran. Para argumentar, se nombra el propósito y se cita el rasgo audible que lo sostiene: «Es una marcha, porque el pulso es fuerte y parejo». El mismo rasgo puede servir a propósitos distintos, así que siempre conviene cruzarlo con el contexto, que dice quién la toca, dónde y para qué.",
    ],
    [("propósito", "para qué se hace o se usa una música"), ("tradición oral", "música que se aprende de oído, de persona a persona, sin partitura"), ("tradición escrita", "música que se guarda en una partitura para interpretarla casi igual"), ("música popular", "música que circula entre mucha gente por medios masivos y por la vida cotidiana"), ("marcha", "música de pulso fuerte y parejo para caminar al mismo paso")],
    [
        ("Hallar el propósito", "Un fragmento es lento, suave, con una melodía corta que se repite cuatro veces. ¿Cuál es su propósito más probable: arrullar o marchar?", ["Lento, suave y repetido calma.", "Una marcha necesita pulso fuerte y marcado."], "Arrullar"),
        ("Hallar la tradición", "Una melodía se la enseñó una vecina a otra cantando, nadie la escribió y cada vez cambia un poco. ¿Es de tradición oral, escrita o popular según cómo se transmite?", ["Se aprende de oído y sin partitura.", "Cada versión cambia."], "De tradición oral"),
    ],
    [
        ("Creer que lo rápido siempre es para bailar.", "Una marcha también puede ser rápida; lo que define el propósito es el rasgo junto con el contexto.", "Nombra el rasgo y el contexto antes de decidir el propósito."),
        ("Pensar que la música escrita no puede ser popular ni la oral, valiosa.", "Son formas de transmisión, no jerarquías de calidad.", "Describe cómo se transmite sin decir cuál vale más."),
    ],
    [
        ex("Un grupo debe caminar al mismo paso y la música tiene un pulso fuerte y parejo. ¿Es una marcha o un arrullo?", "Una marcha", "El pulso fuerte y parejo ordena los pasos."),
        ex("Una música se guarda en partitura y distintas personas la tocan leyendo las mismas notas. ¿Es de tradición oral o escrita?", "Escrita", "Se transmite por partitura."),
        ex("Una canción suena en la radio y miles de personas la bailan en fiestas. ¿Qué tipo de música es por su circulación?", "Popular", "Circula entre mucha gente por medios masivos y fiestas."),
    ],
    [
        ex("Un fragmento tiene tempo lento, volumen suave y una melodía que se repite. ¿Qué propósito sostiene mejor esos rasgos? A) Dormir a un bebé. B) Hacer marchar a un desfile.", "A", "Lo lento, suave y repetido calma; el desfile necesita pulso fuerte."),
        ex("Una melodía se canta en las fiestas de un pueblo y se aprende escuchando a los mayores, sin partitura. ¿Es de tradición oral o escrita?", "Oral", "Se aprende de oído y de persona a persona."),
        ex("Un tambor marca un pulso claro y constante a 100 pulsos por minuto para que un grupo baile. ¿Cuál es el propósito: bailar o arrullar?", "Bailar", "El pulso claro y constante permite moverse al compás."),
    ],
    [
        ex("Une cada música con su rasgo principal: 1) arrullo, 2) marcha, 3) música para bailar; a) pulso fuerte y parejo, b) pulso claro y constante a tempo movido, c) tempo lento y suave. Escribe las parejas.", "1-c, 2-a, 3-b", "El arrullo es lento y suave, la marcha tiene pulso fuerte y la música para bailar un pulso claro y movido."),
        arith("Una marcha va a 100 pulsos por minuto y un grupo da un paso por pulso. ¿Cuántos pasos da en 3 minutos?", "100*3", "Se multiplican los pulsos por minuto por los minutos.", " pasos"),
        ex("Una partitura se publica y se toca igual en tres ciudades, y una canción de cuna se canta de oído y cambia en cada casa. ¿Cuál de las dos cambia más entre versiones: la de partitura o la de oído?", "La de oído", "La tradición oral cambia con cada persona que la transmite."),
    ],
    [
        ex("Ana dice «esta música es rápida, así que es para bailar». ¿Qué le falta a su argumento: el contexto de uso o una partitura?", "El contexto de uso", "Una marcha también puede ser rápida; el contexto dice para qué se usa."),
        ex("Dos músicas tienen el mismo tempo, pero una se toca en un desfile y la otra en una fiesta de plaza. ¿Qué dato distingue su propósito: el tempo o el contexto?", "El contexto", "El tempo es igual, así que lo que las diferencia es dónde y para qué se tocan."),
    ],
    [
        arith("Un desfile escolar de 8 cursos avanza al ritmo de una marcha a 120 pulsos por minuto, dando un paso por pulso. ¿Cuántos pasos da cada estudiante en medio minuto?", "120//2", "Medio minuto es la mitad de los pulsos de un minuto.", " pasos"),
        ex("Un arrullo de ejemplo tiene 4 grupos de 3 pulsos cada uno, y se canta tres veces seguidas. ¿Cuántos pulsos suenan en total?", "36", "Cada vuelta tiene 4 × 3 = 12 pulsos y 12 × 3 = 36."),
    ],
    [ex("Una familia canta para dormir a un niño una melodía lenta y suave que aprendió de la abuela, sin partitura. ¿Cuál es el propósito y la tradición? A) Arrullar; tradición oral. B) Marchar; tradición escrita.", "A", "Lento y suave sirve para arrullar y se aprendió de oído.")],
    [ex("¿Qué rasgo suele tener una marcha?", "Pulso fuerte y parejo", "Ordena el paso de un grupo."), ex("¿Cómo se transmite la música de tradición oral?", "De oído, de persona a persona", "No necesita partitura."), ex("¿La música escrita vale más que la oral? Responde sí o no.", "No", "Son formas distintas de transmitir, no jerarquías.")],
    (
        "Lee estas tres descripciones de ejemplo. 1) Una melodía lenta y suave que una abuela canta de oído para dormir a su nieta. 2) Una pieza con partitura, con pulso fuerte y parejo, que toca una banda en un desfile. 3) Una canción rápida, con pulso claro, que suena en la radio y se baila en una fiesta. Para cada una escribe: propósito, tradición (oral, escrita o popular) y un rasgo audible que lo sostenga.",
        "1) Arrullar; oral; tempo lento y suave. 2) Marchar; escrita; pulso fuerte y parejo. 3) Bailar; popular; pulso claro y tempo rápido.",
        ["relaciona propósito con un rasgo audible", "nombra la tradición según cómo se transmite", "no declara una música mejor que otra"],
        ["tabla de tres filas", "un rasgo audible por fila"],
        ["decidir por el tempo sin mirar el contexto", "decir que lo escrito vale más"],
        "Reconoce la tabla y pide explicar por qué, en una de las filas, el contexto cambia la respuesta.",
    ),
    "Tararea una canción de cuna y una marcha y di qué cambia en el pulso y en el volumen.",
    "Describe una música que conozcas, su propósito y cómo se transmite, con un rasgo audible.",
)

# ---------------------------------------------------------------- OA 01 · clase 4 (responder por vías verbal, visual, sonora y corporal)
L(
    OA1, 4,
    "Lápiz, papel y, si quieres, lápices de colores. Los fragmentos están descritos en los ejercicios (son de ejemplo). Para la respuesta corporal basta un espacio despejado, movimientos suaves de brazos y cuerpo sin saltos, y volumen bajo.",
    "Aprenderé a responder a una música por cuatro vías (verbal, visual, sonora y corporal) cuidando que cada respuesta sea coherente con lo que se oye. Sirve para comunicar lo que siento y pienso al escuchar, de más de una manera.",
    ["Sé separar hechos audibles de sensaciones.", "Sé hacer un mapa de escucha con segundos.", "Sé que la dinámica es lo fuerte o suave que suena la música."],
    [
        "Una respuesta multimodal expresa lo que siento al escuchar usando distintos lenguajes. La respuesta verbal usa palabras: describe lo que se oye y lo que comunica. La visual usa líneas, formas y colores sobre el papel. La sonora usa mi voz, palmas u objetos para responder con sonido. La corporal usa movimientos del cuerpo hechos con seguridad, sin saltos, en un espacio libre de obstáculos y sin empujar a nadie.",
        "Una respuesta es coherente cuando copia un rasgo audible. Si la melodía sube, mi mano o mi línea dibujada también suben. Si el volumen crece de suave a fuerte, el trazo se engrosa, mi voz sube de volumen o mis brazos se abren cada vez más. Si las notas son cortas y separadas, hago puntos, golpecitos o movimientos breves. Si las notas son largas, hago líneas largas o movimientos continuos.",
        "Para responder bien, primero escucho y anoto el rasgo, luego elijo la vía y por último explico la relación: «Dibujé una línea que sube porque la melodía sube». Siempre se puede explicar la respuesta en una frase verbal. Nadie está obligado a mostrar su respuesta corporal ante el curso: también se puede describir o dibujar, y eso es igual de válido.",
    ],
    [("respuesta multimodal", "expresar lo que escucho por más de una vía: palabras, dibujo, sonido o movimiento"), ("coherente", "que copia un rasgo audible de la música"), ("trazo", "línea que se dibuja sobre el papel"), ("vía", "forma de responder: verbal, visual, sonora o corporal"), ("ascendente", "que sube de agudo a más agudo")],
    [
        ("Elegir una respuesta coherente", "El volumen de un fragmento crece poco a poco de suave a fuerte. ¿Qué trazo es coherente: una línea que se engrosa o una línea que se adelgaza?", ["El volumen aumenta.", "El trazo que se engrosa copia ese aumento."], "Una línea que se engrosa"),
        ("Explicar la relación", "Una estudiante hizo golpecitos suaves con los dedos sobre la mesa mientras sonaban notas muy cortas y separadas. ¿Qué rasgo copió?", ["Los golpecitos son breves y separados.", "Las notas cortas y separadas se parecen a golpes breves."], "La duración corta de las notas"),
    ],
    [
        ("Hacer una respuesta que no se parece a nada de lo que suena.", "Una respuesta vale cuando se puede relacionar con un rasgo audible.", "Anota el rasgo antes de elegir cómo responder."),
        ("Sentirse obligado a mostrar el movimiento ante todo el curso.", "La respuesta corporal es una vía más; se puede describir o dibujar en su lugar.", "Elige la vía con la que te sientas cómodo o cómoda, y explícala."),
    ],
    [
        ex("La melodía de un fragmento sube de nota en nota. ¿Qué línea dibujas: una que sube o una que baja?", "Una que sube", "El dibujo debe copiar la dirección de la melodía."),
        ex("Un fragmento tiene notas largas y continuas. ¿Qué dibujas: puntos separados o una línea larga?", "Una línea larga", "Las notas largas se parecen a una línea continua."),
        ex("Al responder con el cuerpo, ¿se puede saltar cerca de otras personas? Responde sí o no.", "No", "La respuesta corporal se hace con seguridad, sin saltos y sin empujar."),
    ],
    [
        ex("Un fragmento empieza fuerte y termina suave. ¿Qué movimiento de brazos es coherente? A) Brazos abiertos que se van cerrando poco a poco. B) Brazos cerrados que se abren cada vez más.", "A", "Pasar de fuerte a suave se parece a ir cerrando poco a poco."),
        ex("Una persona no quiere mostrar un movimiento ante el curso. ¿Qué vía puede usar para responder igual? A) Dibujar y explicar con una frase. B) No responder.", "A", "Hay cuatro vías, y cualquiera es una respuesta válida."),
        ex("Un tambor suena con golpes cortos y secos. ¿Qué respuesta sonora es coherente: palmadas cortas o un silbido largo?", "Palmadas cortas", "Los golpes cortos se copian con sonidos cortos."),
    ],
    [
        ex("Un fragmento tiene tres rasgos: melodía que sube, notas cortas y volumen que crece. Un dibujo tiene puntos separados que se ubican cada vez más arriba y con trazo más grueso. ¿Cuántos rasgos copia?", "3", "Los puntos copian las notas cortas, la altura copia la melodía y el grosor copia el volumen."),
        ex("Un dibujo tiene una línea larga, ondulada y siempre del mismo grosor. ¿Qué rasgos del fragmento pudo copiar: notas largas y volumen constante, o notas cortas y volumen que crece?", "Notas largas y volumen constante", "La línea larga copia las notas largas y el grosor igual copia un volumen estable."),
        arith("Un fragmento dura 60 segundos. Haces una respuesta visual con una línea por cada 15 segundos. ¿Cuántas líneas dibujas?", "60//15", "Se divide el total de segundos por los segundos de cada línea.", " líneas"),
    ],
    [
        ex("Julia dice «mi dibujo es correcto porque me gustó». ¿Qué le falta a su explicación: relacionar el dibujo con un rasgo audible o usar más colores?", "Relacionar el dibujo con un rasgo audible", "Una respuesta se justifica con lo que se oye, no con el gusto."),
        ex("Un compañero respondió con un movimiento muy rápido a un fragmento lento y suave. ¿Qué rasgo no copió?", "El tempo (la velocidad)", "Lo lento se parece a movimientos lentos, no rápidos."),
    ],
    [
        arith("Un fragmento de 80 segundos se divide en 4 tramos iguales. En cada tramo haces una respuesta corporal distinta. ¿Cuántos segundos dura cada tramo?", "80//4", "Se reparten los 80 segundos entre los 4 tramos iguales.", " segundos"),
        ex("Un fragmento tiene un tramo de 20 segundos suave y un tramo de 20 segundos fuerte. Para representarlo con una sola línea dibujada de 40 trazos iguales, ¿cuántos trazos finos y cuántos gruesos dibujas, si cada trazo equivale a 1 segundo?", "20 finos y 20 gruesos", "Cada tramo dura 20 segundos y hay un trazo por segundo."),
    ],
    [ex("En la feria de tu escuela suena un fragmento de ejemplo: la melodía sube, el volumen crece y las notas son cortas. Quieres responder con una vía sonora. ¿Cuál es coherente? A) Palmadas cortas que suben de volumen. B) Un silbido largo y siempre suave.", "A", "Las palmadas cortas copian las notas cortas y el aumento de volumen copia el crescendo.")],
    [ex("¿Cuáles son las cuatro vías de respuesta?", "Verbal, visual, sonora y corporal", "Son las formas de responder de la clase."), ex("Si la melodía baja, ¿cómo es una línea coherente: que baja o que sube?", "Que baja", "Copia la dirección de la melodía."), ex("¿Qué debe tener toda respuesta para ser coherente?", "Relación con un rasgo audible", "Se justifica con lo que se oye.")],
    (
        "Usa este fragmento de ejemplo: «0–10 s: flauta aguda, notas cortas, volumen suave. 10–20 s: se agregan tambores, la melodía sube y el volumen crece. 20–30 s: todo suena fuerte y las notas son largas». Elige una vía (dibujo, sonido o movimiento) y crea una respuesta de tres partes, una por tramo. Debajo, escribe tres frases «Hice … porque …» con un rasgo audible en cada una.",
        "Dibujo: tramo 1, puntitos finos arriba; tramo 2, puntos que suben y se engrosan; tramo 3, líneas largas y gruesas. Frases: «Hice puntitos finos porque las notas son cortas y suaves», «Hice puntos más gruesos y altos porque la melodía sube y crece el volumen», «Hice líneas largas y gruesas porque las notas son largas y fuertes».",
        ["copia al menos un rasgo audible en cada tramo", "escribe tres frases con «porque»", "elige una vía segura y viable en casa"],
        ["respuesta de tres partes", "tres frases con evidencia"],
        ["responder sin relación con lo que suena", "usar un movimiento inseguro"],
        "Reconoce la respuesta y pide mostrar, en una de las tres partes, cuál rasgo audible copia.",
    ),
    "Dibuja una línea que suba y otra que baje, y tararea una melodía que haga lo mismo.",
    "Responde al mismo fragmento por dos vías distintas y explica qué rasgo copia cada una.",
)
