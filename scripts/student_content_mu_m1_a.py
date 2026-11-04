"""Student material for 1.º medio Música, OA 01 (apreciar músicas de Chile y el mundo de tradición oral, escrita y popular, expresándose por medios verbales, visuales, sonoros y corporales).

Todas las músicas de los ejercicios son descripciones inventadas («de ejemplo»); las audiciones reales las selecciona y pone el docente.
Este módulo define el ayudante L que usan los demás módulos mu_m1_*.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1 = "MU1M OA 01"


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, tk, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[dict(title=t, problem=p, steps=s, answer=a) for t, p, s, a in worked],
        mistakes=[dict(wrong=w, why=y, fix=f) for w, y, f in mistakes],
        tiers=dict(recovery=R, understand=C, apply=A, reason=Z, challenge=D),
        context=ctx, selfcheck=sc, open_task=task(*tk), reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- OA 01 · clase 1 (tradición oral, escrita y popular)
L(
    OA1, 1,
    "Lápiz y papel. Las músicas están descritas con palabras en los ejercicios (son de ejemplo). Si una persona de tu casa puede cantarte una canción que aprendió de memoria, sirve, pero no es necesario.",
    "Aprenderé a distinguir tres tradiciones musicales (oral, escrita y popular) según cómo se transmiten y se difunden. Sirve para apreciar una música ubicándola en su origen y su modo de circular, sin decir que una vale más que otra.",
    ["Sé separar lo que se oye de lo que siento.", "Sé que una partitura es música escrita con signos.", "Sé que una canción puede tener versiones distintas."],
    [
        "Una música de tradición oral se transmite de persona en persona, escuchando, repitiendo y recordando, sin necesidad de partitura. Suele no tener un autor conocido y, como cada persona la recuerda a su modo, aparecen variantes: versiones algo distintas de una misma música. Los arrullos, las rondas y muchos cantos de fiesta de los pueblos de Chile se conservan así.",
        "Una música de tradición escrita se fija con signos en una partitura. Tiene un autor o una autora conocidos, y quienes la interpretan leen las mismas notas y ritmos, de modo que la obra puede sonar parecida en lugares y épocas distintos. La música popular, en cambio, se define por su difusión masiva: circula por la radio, las grabaciones, los conciertos y las plataformas digitales, y la conoce mucha gente.",
        "Estas tradiciones no son cajones cerrados. Una misma música puede ser a la vez oral y popular: por ejemplo, una canción aprendida de memoria que luego una banda graba y difunde. Para apreciarla conviene preguntarse cómo se transmite, quién la conserva y cómo llega a la gente. Clasificar bien no significa que una tradición sea mejor: cada una cumple un papel distinto.",
    ],
    [("tradición oral", "música que se transmite de persona en persona, de memoria y sin partitura"), ("tradición escrita", "música fijada en partitura, con autor conocido"), ("música popular", "música de difusión masiva, que circula por los medios y la conoce mucha gente"), ("variante", "versión algo distinta de una misma música oral"), ("partitura", "escritura de las notas y los ritmos de una obra")],
    [
        ("Clasificar por cómo se transmite", "Un cuento cantado se aprende escuchando a un abuelo, sin papel, y cada nieto lo cambia un poco. ¿A qué tradición pertenece?", ["No hay partitura: se aprende de memoria.", "Hay variantes entre nietos."], "A la tradición oral"),
        ("Una música en dos tradiciones", "Una canción aprendida de memoria en un pueblo es grabada por una banda y suena en la radio. ¿Con qué dos tradiciones se relaciona?", ["Se transmitió de memoria: oral.", "Luego se difundió por los medios: popular."], "Con la oral y la popular"),
    ],
    [
        ("Creer que la música oral es «menos música» que la escrita.", "Son formas distintas de conservar y compartir la música; ninguna es mejor por sí sola.", "Describe cómo se transmite cada una y para qué sirve."),
        ("Pensar que una música solo puede estar en una tradición.", "Una misma música puede ser oral y popular, o escrita y popular.", "Pregunta cómo se transmite y cómo se difunde, por separado."),
    ],
    [
        ex("Una melodía se aprende escuchando a una abuela, sin partitura, y cada familia la canta con pequeños cambios. ¿A qué tradición pertenece principalmente: oral, escrita o popular?", "Oral", "Se transmite de persona en persona y tiene variantes."),
        ex("Una obra está escrita en partitura por una compositora conocida y se toca igual cada vez que se lee. ¿A qué tradición pertenece principalmente: oral, escrita o popular?", "Escrita", "Está fijada con signos y tiene autora conocida."),
        ex("Una canción se difunde por radio y plataformas, tiene una grabación oficial y la conoce mucha gente. ¿Qué tradición describe mejor su difusión: oral, escrita o popular?", "Popular", "Su rasgo principal es la difusión masiva por los medios."),
    ],
    [
        ex("¿Qué es una variante en la tradición oral? A) Cada versión algo distinta de una misma música, que cambia al pasar de persona en persona. B) Una copia exacta fijada en partitura.", "A", "Al transmitirse de memoria, cada persona recuerda la música a su modo."),
        ex("¿Por qué una partitura permite que dos grupos distintos toquen la misma obra? A) Porque fija por escrito las notas y los ritmos. B) Porque cada grupo la recuerda de memoria a su manera.", "A", "La escritura deja los datos de la obra a la vista de quien la lee."),
        ex("Una música se conoce en todo el país gracias a la radio y a las plataformas digitales. ¿Qué rasgo de la música popular muestra? A) Su difusión masiva por los medios. B) Su transmisión solo de abuelos a nietos.", "A", "Popular significa que circula ampliamente por medios de difusión."),
    ],
    [
        ex("De estas cuatro músicas de ejemplo, ¿cuántas son de tradición escrita? (1) Una sonata en partitura de un compositor conocido. (2) Un arrullo aprendido de memoria. (3) Una obra coral con una partitura para cada voz. (4) Una canción que se aprende de la grabación de la radio.", "2", "Solo la sonata y la obra coral están fijadas en partitura: son la 1 y la 3."),
        ex("Una cueca de ejemplo la aprendieron los abuelos escuchando y hoy una banda la graba y la difunde por radio. ¿Con qué tradiciones se relaciona? A) Oral y popular. B) Escrita y popular.", "A", "Se transmitió de oído (oral) y luego circuló por los medios (popular)."),
        ex("Una escuela escribe en partitura una canción de cuna que antes solo se cantaba de memoria. ¿Qué ganó esa canción? A) Un registro que permite tocarla igual en lugares distintos. B) Un autor conocido que antes no existía.", "A", "La partitura la fija y facilita compartirla, aunque no inventa un autor."),
    ],
    [
        ex("Dos estudiantes justifican que un arrullo es oral. A) «Es oral porque suena antiguo.» B) «Es oral porque se aprende de memoria y cada familia lo canta con cambios.» ¿Cuál justificación usa criterios válidos?", "B", "Habla de la transmisión de memoria y de las variantes, no de una impresión."),
        ex("Pablo afirma: «si una música es popular, no puede ser oral». ¿Qué ejemplo lo contradice? A) Una canción aprendida de oído que además suena en la radio. B) Una sonata que solo existe en partitura.", "A", "Esa canción es oral por transmisión y popular por difusión a la vez."),
    ],
    [
        ex("Una música de ejemplo se escribió en partitura, la compuso una persona conocida y hoy tiene miles de reproducciones en plataformas. ¿Cuántas de las tres tradiciones la describen bien?", "2", "Describen bien la escrita (partitura y autor) y la popular (difusión masiva)."),
        arith("Un concierto escolar tiene 12 piezas: 5 de tradición oral con 3 minutos cada una, 4 de tradición escrita con 6 minutos cada una y el resto populares con 4 minutos cada una. ¿Cuántos minutos dura en total?", "5*3+4*6+(12-5-4)*4", "Se calculan las piezas populares restando y se suman los minutos de cada grupo.", " minutos"),
    ],
    [ex("Una persona de tu casa te canta un arrullo que aprendió de su madre y que nunca escribió. ¿Cómo lo describes? A) Música de tradición oral, transmitida de memoria. B) Música de tradición escrita, porque tiene autor.", "A", "Se aprendió de memoria y no hay partitura.")],
    [ex("¿Qué se necesita para leer una música de tradición escrita?", "Una partitura", "Es la escritura que fija las notas y los ritmos."), ex("¿Cómo se llama cada versión algo distinta de una misma canción de tradición oral?", "Variante", "Nace porque cada persona la recuerda a su modo."), ex("¿Por qué medios circula la música popular?", "Radio, grabaciones y plataformas", "Son medios de difusión masiva.")],
    (
        "Elige una de estas tres músicas de ejemplo. Pieza 1: arrullo cantado por una sola voz, aprendido de una persona mayor, con palabras algo distintas en cada casa. Pieza 2: obra para cuarteto de cuerdas, escrita en partitura por una compositora conocida. Pieza 3: canción de una banda, difundida por radio y plataformas. Escribe: a) a qué tradición pertenece, b) dos rasgos que lo prueban, c) una frase «Esta música cumple el papel de… porque…».",
        "Pieza 1. a) Oral. b) Se aprende de una persona mayor y tiene palabras distintas en cada casa. c) Esta música cumple el papel de acompañar el sueño de un bebé, porque se canta en la casa y pasa de voz en voz.",
        ["clasifica con un criterio de transmisión o de difusión", "da al menos dos rasgos tomados de la descripción", "no dice que una tradición sea mejor que otra"],
        ["ficha con a), b) y c)", "frase final con «porque»"],
        ["clasificar por «suena antiguo»", "decir que la música oral vale menos"],
        "Reconoce la ficha y pide indicar, para la tradición elegida, qué cambiaría si se transmitiera por otro medio.",
    ),
    "Pide a una persona de tu casa que te cante una canción y anota en tres frases cómo la aprendió.",
    "Escribe tres músicas que conozcas y di si cada una es oral, escrita o popular (o varias), con una razón.",
)

# ---------------------------------------------------------------- OA 01 · clase 2 (lenguaje, contexto y propósito)
CTX = ("Arrullo: se canta en una casa, de noche, para dormir a un bebé; 60 pulsos por minuto, una voz sola, notas largas, volumen suave. "
       "Marcha: suena en un desfile, para ordenar el paso de la gente; 100 pulsos por minuto, bombo y vientos, volumen fuerte. "
       "Canción de baile: suena en una fiesta, para bailar; 120 pulsos por minuto, guitarra y palmas, ritmo muy marcado")
L(
    OA1, 2,
    f"Lápiz y papel. Tabla de ejemplo, que se repite en los ejercicios: {CTX}.",
    "Aprenderé a relacionar los rasgos audibles de una música (lenguaje) con el lugar donde suena (contexto) y para qué sirve (propósito). Sirve para apreciar por qué una música suena como suena.",
    ["Sé distinguir tradición oral, escrita y popular.", "Sé que el tempo se mide en pulsos por minuto.", "Sé nombrar rasgos como volumen, timbre y duración de las notas."],
    [
        "Toda música se hace en un contexto, que es el lugar, el momento y el grupo de personas donde suena, y con un propósito, que es lo que busca lograr: dormir a alguien, ordenar un paso, acompañar un baile, contar una historia o recordar a alguien. El lenguaje musical son los rasgos que se oyen: tempo, volumen, timbre, duración de las notas, melodía y ritmo. Los tres elementos se relacionan.",
        "Cuando el propósito es calmar, el lenguaje suele ser lento, suave y de notas largas, como en un arrullo. Cuando es ordenar el paso de un grupo, el pulso es fuerte y regular, como en una marcha. Cuando es bailar, el ritmo está muy marcado y el tempo permite moverse. No es casualidad: las personas que hacen música eligen rasgos que sirven a su propósito dentro de su contexto.",
        "Para apreciar una música conviene preguntar tres cosas: ¿dónde suena?, ¿para qué sirve?, ¿qué rasgos audibles ayudan a ese propósito? Después se une todo con una frase como «Esta música es lenta y suave porque sirve para dormir». Atención: un mismo rasgo puede servir a propósitos distintos, y la misma música puede cambiar de propósito si cambia el contexto.",
    ],
    [("contexto", "lugar, momento y grupo de personas donde suena una música"), ("propósito", "lo que una música busca lograr en su contexto"), ("lenguaje musical", "conjunto de rasgos que se oyen: tempo, volumen, timbre, ritmo y melodía"), ("tempo", "velocidad del pulso, medida en pulsos por minuto"), ("pulso", "latido regular de la música")],
    [
        ("Unir propósito y rasgo", f"Tabla: {CTX}. ¿Qué rasgo de la marcha ayuda a ordenar el paso de la gente?", ["La marcha sirve para ordenar el paso.", "Su pulso es fuerte y regular, a 100 por minuto."], "El pulso fuerte y regular"),
        ("Calcular pulsos", f"Tabla: {CTX}. ¿Cuántos pasos da una persona en 2 minutos si da un paso en cada pulso de la marcha?", ["La marcha tiene 100 pulsos por minuto.", "100 × 2 = 200."], "200 pasos"),
    ],
    [
        ("Elegir los rasgos sin pensar en el propósito.", "Los rasgos se eligen porque sirven a lo que la música busca lograr.", "Pregunta primero para qué suena la música."),
        ("Creer que un rasgo siempre significa lo mismo.", "Un volumen fuerte sirve para una marcha, pero no para un arrullo; depende del contexto.", "Relaciona el rasgo con el contexto antes de interpretarlo."),
    ],
    [
        ex(f"Tabla: {CTX}. ¿Para qué sirve el arrullo?", "Para dormir a un bebé", "Su propósito está en la descripción del contexto."),
        ex(f"Tabla: {CTX}. ¿Cuál de las tres músicas tiene el tempo más lento?", "El arrullo", "Tiene 60 pulsos por minuto, menos que 100 y 120."),
        ex(f"Tabla: {CTX}. ¿En qué contexto suena la canción de baile?", "En una fiesta", "Así lo dice la descripción de esa música."),
    ],
    [
        ex("¿Qué rasgo del arrullo ayuda a calmar a un bebé? A) Notas largas y volumen suave. B) Bombo fuerte y vientos.", "A", "Lo suave y lo largo transmiten calma; lo fuerte se parece a una marcha."),
        ex("¿Por qué la marcha tiene un pulso fuerte y regular? A) Porque sirve para ordenar el paso de un grupo. B) Porque busca dormir al público.", "A", "El propósito de ordenar el paso exige un pulso que se escuche claro."),
        ex("Una música alegre para bailar cambia su ritmo por uno casi sin marcar. ¿Qué pasa con su propósito? A) Se vuelve difícil bailarla con el grupo. B) Mejora porque es más suave.", "A", "Sin ritmo marcado, las personas pierden el apoyo para moverse juntas."),
    ],
    [
        arith(f"Tabla: {CTX}. ¿Cuántos pulsos más por minuto tiene la canción de baile que el arrullo?", "120-60", "Se resta el tempo del arrullo al de la canción de baile.", " pulsos"),
        ex("Un desfile de una banda dura 3 minutos y la marcha va a 100 pulsos por minuto. Alguien dice que la banda dio 250 pasos. ¿Es correcto? Responde sí o no.", "No", "En 3 minutos hay 300 pulsos y, por lo tanto, 300 pasos, no 250."),
        arith("El arrullo de ejemplo va a 60 pulsos por minuto. ¿Cuántos pulsos suenan en 30 segundos?", "60//2", "Medio minuto tiene la mitad de los pulsos de un minuto.", " pulsos"),
    ],
    [
        ex(f"Tabla: {CTX}. Dos amigos dicen que el arrullo y la canción de baile tienen el mismo propósito. ¿Es cierto, sí o no?", "No", "Uno busca calmar para dormir y la otra busca mover el cuerpo para bailar."),
        arith("La canción de baile de ejemplo va a 120 pulsos por minuto. Un grupo baila durante 4 minutos sin parar. ¿Cuántos pulsos suenan?", "120*4", "Se multiplican los pulsos por minuto por los minutos.", " pulsos"),
    ],
    [
        arith("En una fiesta se tocan 5 minutos de marcha a 100 pulsos por minuto y luego 5 minutos de canción de baile a 120 pulsos por minuto. ¿Cuántos pulsos suenan en total?", "100*5+120*5", "Se calculan los pulsos de cada parte y se suman.", " pulsos"),
        ex("El arrullo de ejemplo se toca a 60 pulsos por minuto. Alguien quiere usarlo como marcha de desfile y cambia solo el tempo a 100. ¿Basta con ese cambio? A) No: también hay que subir el volumen y marcar el pulso con un bombo. B) Sí: el tempo es el único rasgo que importa.", "A", "Para ordenar el paso se necesita además un pulso fuerte y claro."),
    ],
    [ex("En una fiesta del curso quieren que todos bailen en pareja, pero la música que ponen tiene un ritmo suave y casi sin marcar. ¿Qué rasgo conviene cambiar? A) Marcar más el ritmo. B) Bajar aún más el volumen.", "A", "Un ritmo marcado da el apoyo que se necesita para bailar juntos.")],
    [ex("¿Qué es el propósito de una música?", "Lo que busca lograr en su contexto", "Es para qué suena."), ex("¿Qué es el contexto de una música?", "Lugar, momento y grupo donde suena", "Es la situación donde se hace."), ex("¿Qué se mide en pulsos por minuto?", "El tempo", "Dice qué tan rápido es el pulso.")],
    (
        "Usa la tabla de ejemplo (arrullo, marcha y canción de baile). Elige una música y escribe: a) contexto, b) propósito, c) tres rasgos audibles, d) una frase «Esta música es… porque sirve para…». Luego escribe cómo cambiaría un rasgo si se usara con otro propósito (por ejemplo, el arrullo para un desfile).",
        "Arrullo. a) Una casa de noche. b) Dormir a un bebé. c) 60 pulsos por minuto, una voz sola, notas largas. d) Esta música es lenta y suave porque sirve para dormir. Para un desfile habría que subir el volumen y marcar un pulso más fuerte.",
        ["usa la tabla del enunciado", "relaciona al menos dos rasgos con el propósito", "propone un cambio coherente de rasgo"],
        ["ficha con a), b), c) y d)", "cambio de rasgo explicado"],
        ["dar rasgos que no están en la tabla", "no relacionar rasgo y propósito"],
        "Reconoce la ficha y pide señalar qué rasgo no cambiaría aunque cambie el propósito, y por qué.",
    ),
    "Anota en tres líneas dónde suena una música de tu casa y para qué sirve.",
    "Escribe un propósito distinto (por ejemplo, concentrarse) y qué tempo y volumen elegirías para una música con ese propósito.",
)

# ---------------------------------------------------------------- OA 01 · clase 3 (ensayar una decisión musical)
L(
    OA1, 3,
    "Lápiz y papel; si quieres, palmas y voz baja para marcar el pulso. Las dos versiones de la canción están descritas en los ejercicios (son de ejemplo).",
    "Aprenderé a ensayar una decisión musical con el método «versión 1, cambio, versión 2, comparación»: cambio un solo rasgo, escucho qué efecto produce y decido qué versión sirve mejor a mi propósito. Sirve para apreciar una música a partir de lo que cambia al oírla de otra manera.",
    ["Sé relacionar rasgos con propósito.", "Sé que tempo, volumen y timbre son rasgos que se oyen.", "Sé que el tempo se mide en pulsos por minuto."],
    [
        "Una decisión musical es una elección sobre cómo suena la música: más rápido o más lento, más fuerte o más suave, con una voz o con varias, con un instrumento u otro. Para ensayar una decisión de forma ordenada se usa un método: primero se escucha una versión 1, luego se cambia un solo rasgo, se escucha la versión 2 y se compara qué efecto tuvo el cambio.",
        "Es importante cambiar un solo rasgo cada vez. Si en la versión 2 cambio a la vez el tempo, el volumen y el instrumento, no sabré cuál produjo el efecto. Después de comparar se escribe una frase con tres partes: qué cambié, qué se oye distinto y qué versión sirve mejor al propósito. La decisión final no depende de qué versión me gusta más, sino de qué versión cumple mejor lo que la música busca lograr.",
        "El tempo se puede cambiar con números. Si una canción va a 80 pulsos por minuto y la subo a 100, aumenta 20 pulsos por minuto y la música se siente más animada. Si la bajo a 60, se siente más tranquila. Anotar el cambio con la cifra permite que otra persona repita mi ensayo y compruebe mi comparación.",
    ],
    [("decisión musical", "elección sobre cómo suena la música"), ("versión", "forma concreta en que se interpreta una música"), ("comparar", "oír dos versiones y anotar qué cambia"), ("rasgo", "característica que se oye, como el tempo o el volumen"), ("efecto", "cambio que se oye o se siente al modificar un rasgo")],
    [
        ("Cambiar un solo rasgo", "Una canción va a 80 pulsos por minuto y suena suave. Para la versión 2 quieres probar el efecto del tempo. ¿Qué cambias?", ["Se prueba un solo rasgo: el tempo.", "El volumen se deja igual."], "Solo el tempo, por ejemplo a 100 pulsos por minuto"),
        ("Decidir por el propósito", "La canción será para calmar a un grupo antes de dormir. Versión 1: 60 pulsos por minuto. Versión 2: 110 pulsos por minuto. Las dos tienen el mismo volumen suave. ¿Cuál sirve mejor?", ["El propósito es calmar.", "Lento y suave calma mejor."], "La versión 1"),
    ],
    [
        ("Cambiar tres rasgos a la vez.", "No se sabe cuál produjo el efecto.", "Cambia un solo rasgo en cada versión."),
        ("Decidir por «esta me gusta más».", "El gusto no dice si la música cumple su propósito.", "Compara con el propósito y con lo que se oye."),
    ],
    [
        ex("En el método de ensayo, ¿cuántos rasgos se cambian de una versión a la otra?", "Uno", "Se cambia un solo rasgo para saber qué produjo el efecto."),
        ex("Una canción pasa de 90 a 120 pulsos por minuto. ¿Se siente más animada o más tranquila?", "Más animada", "Un tempo mayor da una sensación de más movimiento."),
        ex("¿Qué se escribe después de comparar las dos versiones: qué cambié, qué se oye distinto y qué versión sirve mejor al propósito, o solo cuál me gustó más?", "Qué cambié, qué se oye distinto y qué versión sirve mejor", "La decisión se apoya en el cambio, el efecto y el propósito."),
    ],
    [
        ex("Un grupo cambia en la versión 2 el tempo, el volumen y el instrumento. ¿Qué problema tiene su ensayo? A) No sabrán cuál de los cambios produjo el efecto. B) La versión 2 será necesariamente más lenta que la versión 1.", "A", "Cuando cambian tres rasgos a la vez, no se puede asignar el efecto a ninguno."),
        ex("Una música debe acompañar a un grupo que desfila con paso enérgico. Versión 1: 70 pulsos por minuto. Versión 2: 110 pulsos por minuto. Las dos tienen el mismo volumen fuerte y el mismo bombo. ¿Cuál sirve mejor? A) Versión 1. B) Versión 2.", "B", "Un paso enérgico pide un pulso animado y regular que oriente el paso; solo cambia el tempo."),
        ex("Un estudiante escribe: «Elijo la versión 2 porque me gusta más». ¿Qué le falta a su decisión? A) Relacionarla con el propósito y con lo que se oye. B) Agregar cuánto dura la canción.", "A", "El gusto no basta: debe mostrar qué efecto produce el cambio."),
    ],
    [
        arith("Una canción de ejemplo va a 80 pulsos por minuto. Para la versión 2 se sube a 100. ¿Cuántos pulsos por minuto se agregaron?", "100-80", "Se resta el tempo inicial al tempo final.", " pulsos por minuto"),
        arith("Una versión suena a 60 pulsos por minuto durante 2 minutos. ¿Cuántos pulsos suenan?", "60*2", "Se multiplican los pulsos por minuto por los minutos.", " pulsos"),
        ex("En la versión 2 de un ensayo solo se cambió el volumen de fuerte a suave. ¿Qué rasgo se está probando?", "El volumen", "Es el único rasgo que cambió entre las versiones."),
    ],
    [
        arith("En un ensayo, la versión 1 a 80 pulsos por minuto dura 2 minutos y la versión 2 a 100 pulsos por minuto dura 2 minutos. ¿Cuántos pulsos más suenan en la versión 2?", "100*2-80*2", "Se calculan los pulsos de cada versión y se restan.", " pulsos"),
        ex("Una canción de ejemplo es para animar a un equipo antes de un partido. Se ensayan tres versiones: 60, 90 y 120 pulsos por minuto, todas con el mismo volumen. ¿Cuál sirve mejor al propósito?", "La de 120 pulsos por minuto", "Animar pide un tempo rápido, y las tres tienen igual volumen, así que solo cambia el tempo."),
    ],
    [
        ex("Un grupo ensaya una versión 1 con flauta a 90 pulsos por minuto y una versión 2 con flauta y guitarra, más fuerte, a 90 pulsos por minuto. ¿Cuál es el defecto del ensayo? A) Cambió el volumen y el timbre a la vez, así que no se sabe cuál causó el efecto. B) Mantuvo el mismo tempo en las dos versiones.", "A", "Dos rasgos cambiaron juntos; mantener el tempo no es un defecto."),
        arith("Una banda prueba tres tempos de una pieza, cada ensayo dura 120 segundos y entre un ensayo y otro hay 30 segundos de pausa. ¿Cuántos segundos dura todo el trabajo?", "3*120+2*30", "Hay tres ensayos y dos pausas entre ellos.", " segundos"),
    ],
    [ex("Para una presentación en que quieren que el público escuche con calma, ensayan la versión 1 con voz y guitarra suaves, y la versión 2 con la misma voz y guitarra, pero fuertes. ¿Cuál conviene? A) Versión 1. B) Versión 2.", "A", "Lo suave favorece la calma; el volumen fuerte agrega energía que no se busca.")],
    [ex("¿Cuántos rasgos conviene cambiar en cada ensayo?", "Uno", "Así se sabe qué produjo el efecto."), ex("¿En qué se apoya la decisión final: en el gusto o en el propósito?", "En el propósito", "Se elige la versión que mejor cumple lo que la música busca."), ex("Si el tempo pasa de 100 a 120, ¿cuánto aumentó?", "20 pulsos por minuto", "Se resta 120 − 100.")],
    (
        "Usa esta canción de ejemplo: «una melodía lenta de cinco notas, cantada por una voz a 70 pulsos por minuto, volumen medio». Tu propósito es que la oigan sin sobresaltar a personas que descansan. Escribe: a) un rasgo que cambiarás, b) cómo sonará la versión 2 (con cifras), c) qué efecto esperas, d) una decisión final con «porque».",
        "a) El volumen. b) Versión 2: misma melodía a 70 pulsos por minuto, pero con volumen suave. c) Espero que suene más tranquila. d) Elijo la versión 2 porque sirve mejor para no sobresaltar a quienes descansan.",
        ["cambia un solo rasgo", "usa una cifra en la versión 2", "justifica con el propósito y no con el gusto"],
        ["cuatro partes a) a d)", "decisión con «porque»"],
        ["cambiar varios rasgos a la vez", "decidir por gusto"],
        "Reconoce el ensayo y pide explicar qué otro rasgo habría podido probar en una tercera versión.",
    ),
    "Tararea una canción a dos velocidades distintas y anota qué cambia.",
    "Prueba el cambio de un segundo rasgo (por ejemplo, el volumen) en la misma canción y anota el efecto.",
)

# ---------------------------------------------------------------- OA 01 · clase 4 (expresarse por medios verbales, visuales, sonoros y corporales)
L(
    OA1, 4,
    "Lápiz, papel y, si quieres, lápices de colores. Los fragmentos están descritos en los ejercicios (son de ejemplo). Para la vía corporal basta un espacio despejado, movimientos suaves de brazos y cuerpo, sin saltos, y volumen bajo.",
    "Aprenderé a expresar mi apreciación de una música por cuatro medios (verbal, visual, sonoro y corporal) y a explicar con un rasgo audible por qué mi respuesta se parece a la música. Sirve para compartir lo que me comunica una música de una manera que otra persona pueda comprobar.",
    ["Sé separar hechos audibles de sensaciones.", "Sé relacionar rasgos con contexto y propósito.", "Sé que el pulso es el latido regular de la música."],
    [
        "Apreciar una música es escucharla con atención, comprender cómo está hecha y valorar lo que comunica. Para expresarlo hay cuatro medios. El medio verbal usa palabras: describo lo que oigo y lo que me comunica. El medio visual usa líneas, formas y colores. El medio sonoro responde con voz, palmas u objetos. El medio corporal usa movimientos hechos con seguridad, en un espacio libre y sin empujar a nadie.",
        "Una buena respuesta es coherente con la música: copia un rasgo audible. Si la melodía sube, mi línea sube. Si el volumen crece, mi trazo se engrosa o mi voz sube. Si las notas son cortas, hago puntos o golpecitos. Además, una apreciación completa tiene tres pasos: describir lo que se oye, relacionarlo con el contexto y el propósito, y valorar con una razón, por ejemplo «me parece eficaz porque…».",
        "No todos tienen que responder por la misma vía. Quien prefiere no mostrar un movimiento ante el curso puede dibujarlo o describirlo; esa respuesta también vale. Lo importante es poder explicar, en una frase, qué rasgo de la música copia mi respuesta. Valorar no es decir si la música me gusta o no, sino explicar qué hace bien para su propósito.",
    ],
    [("apreciar", "escuchar con atención, comprender cómo está hecha una música y valorar lo que comunica"), ("medio", "forma de responder: verbal, visual, sonora o corporal"), ("coherente", "que copia un rasgo audible de la música"), ("valorar", "explicar con una razón qué hace bien una música para su propósito"), ("trazo", "línea que se dibuja sobre el papel")],
    [
        ("Elegir una respuesta coherente", "Un fragmento de ejemplo empieza suave y termina fuerte. ¿Qué respuesta visual es coherente: una línea que se engrosa o una línea que se adelgaza?", ["El volumen aumenta.", "El trazo que se engrosa lo copia."], "Una línea que se engrosa"),
        ("Apreciar en tres pasos", "Fragmento de ejemplo: marcha lenta, de pulso fuerte, usada en un homenaje silencioso. Escribe una apreciación en tres pasos.", ["Describir: pulso fuerte y lento.", "Relacionar: sirve a un homenaje.", "Valorar con razón."], "Es lenta y de pulso fuerte; sirve al homenaje; me parece eficaz porque el pulso lento da solemnidad"),
    ],
    [
        ("Responder sin relación con lo que suena.", "Una respuesta vale cuando se puede relacionar con un rasgo audible.", "Anota el rasgo antes de elegir el medio."),
        ("Confundir valorar con decir si me gusta.", "Valorar es explicar qué hace bien la música para su propósito.", "Termina con «me parece eficaz porque…»."),
    ],
    [
        ex("¿Cuáles son los cuatro medios para expresar una apreciación?", "Verbal, visual, sonoro y corporal", "Son las formas de responder de la clase."),
        ex("La melodía de un fragmento baja de nota en nota. ¿Qué línea dibujas: una que baja o una que sube?", "Una que baja", "El dibujo copia la dirección de la melodía."),
        ex("Respondes a un fragmento con un dibujo de líneas y colores. ¿Qué medio de expresión usaste: verbal, visual, sonoro o corporal?", "Visual", "Las líneas, formas y colores son el medio visual."),
    ],
    [
        ex("Un fragmento tiene notas muy cortas y separadas. ¿Qué respuesta sonora es coherente? A) Golpecitos cortos con los dedos. B) Un sonido largo y continuo con la voz.", "A", "Los sonidos cortos copian las notas cortas."),
        ex("Una persona no quiere mostrar un movimiento ante el curso. ¿Qué puede hacer? A) Dibujarlo y explicarlo con una frase. B) No responder.", "A", "Hay cuatro medios y cualquiera de ellos es una respuesta válida."),
        ex("¿Qué falta en esta valoración: «Me gusta esta marcha»? A) Una razón basada en lo que se oye y en su propósito. B) Más adjetivos.", "A", "Valorar exige explicar con evidencia, no solo decir que gusta."),
    ],
    [
        ex("Un fragmento tiene tres rasgos: melodía que sube, notas cortas y volumen que crece. Un dibujo muestra puntos separados que suben y se engrosan. ¿Cuántos rasgos copia?", "3", "Los puntos copian las notas cortas, la altura la melodía y el grosor el volumen."),
        ex("Un compañero respondió con un movimiento muy rápido a un fragmento lento y suave. ¿Qué rasgo no copió?", "El tempo", "Lo lento se parece a movimientos lentos, no rápidos."),
        ex("Un estudiante apreció un arrullo así: «Es lenta y suave; sirve para dormir; me parece eficaz porque la voz sola da calma». ¿Cuántos pasos de la apreciación tiene?", "3", "Hay descripción, relación con el propósito y valoración con razón."),
    ],
    [
        arith("Un fragmento dura 90 segundos y haces una respuesta visual con una línea por cada 15 segundos. ¿Cuántas líneas dibujas?", "90//15", "Se divide el total de segundos por los segundos de cada línea.", " líneas"),
        ex("Un estudiante escribió: «El fragmento sube de suave a fuerte. Sirve para un cierre festivo». ¿Qué paso de la apreciación le falta?", "Valorar con una razón", "Tiene la descripción y la relación con el propósito, pero no dice por qué es eficaz."),
    ],
    [
        ex("Un fragmento de ejemplo tiene un tramo de 20 segundos suave y otro de 20 segundos fuerte. Dibujas un trazo por segundo, fino si el tramo es suave y grueso si es fuerte. ¿Cuántos trazos finos y cuántos gruesos dibujas?", "20 finos y 20 gruesos", "Cada tramo dura 20 segundos y hay un trazo por segundo."),
        arith("Un fragmento dura 120 segundos y lo divides en 4 tramos iguales; en cada tramo respondes con un medio distinto. ¿Cuántos segundos dura cada tramo?", "120//4", "Se reparten los 120 segundos entre los 4 tramos.", " segundos"),
    ],
    [ex("En el acto de tu liceo suena un fragmento de ejemplo: melodía que sube, volumen que crece, notas cortas. Quieres responder con el medio sonoro. ¿Cuál es coherente? A) Palmadas cortas que suben de volumen. B) Un silbido largo y siempre suave.", "A", "Las palmadas cortas copian las notas cortas y el aumento de volumen copia el crecimiento del fragmento.")],
    [ex("¿Qué debe tener toda respuesta para ser coherente?", "Relación con un rasgo audible", "Se justifica con lo que se oye."), ex("¿Cuáles son los tres pasos de una apreciación completa?", "Describir, relacionar y valorar", "Van de lo que se oye a la razón."), ex("¿Quién decide el medio de respuesta: obligatoriamente el curso o cada estudiante dentro de las cuatro vías?", "Cada estudiante", "Todos los medios valen si son coherentes.")],
    (
        "Usa este fragmento de ejemplo: «0–10 s: flauta aguda, notas cortas, suave. 10–20 s: entran tambores, la melodía sube, el volumen crece. 20–30 s: todo suena fuerte y las notas son largas». Elige un medio (dibujo, sonido o movimiento) y crea una respuesta de tres partes, una por tramo. Debajo, escribe una apreciación en tres pasos: describo, relaciono con un posible propósito y valoro con una razón.",
        "Dibujo: tramo 1, puntitos finos arriba; tramo 2, puntos que suben y se engrosan; tramo 3, líneas largas y gruesas. Apreciación: describo: crece de suave a fuerte; relaciono: sirve para un cierre festivo; valoro: me parece eficaz porque el crecimiento prepara el final.",
        ["copia al menos un rasgo audible por tramo", "escribe los tres pasos de la apreciación", "usa un medio seguro y viable en casa"],
        ["respuesta de tres partes", "apreciación en tres pasos"],
        ["responder sin relación con lo que suena", "valorar solo por gusto"],
        "Reconoce la respuesta y pide mostrar, en un tramo, cuál rasgo audible copia.",
    ),
    "Dibuja una línea que suba y otra que baje y tararea una melodía que haga lo mismo.",
    "Responde al mismo fragmento por dos medios distintos y explica qué rasgo copia cada uno.",
)
