"""Student material for 6.º básico Música, OA 07 (explicar la relación entre las obras interpretadas y/o escuchadas y elementos del contexto en que surgen).

Todas las obras de los ejercicios son fichas inventadas para esta clase; no corresponden a obras reales ni a datos históricos. Los repertorios reales los elige el docente.
Lo que se afirma del contexto es general (función, lugar, comunidad, materiales); los usos y significados de la música de pueblos originarios los enseña el educador/a tradicional o la comunidad.
"""
from __future__ import annotations

from student_content_mu6_a import L
from student_lessons import arith, ex

OA7 = "MU06 OA 07"
CTX = "elementos del contexto: lugar, comunidad (quiénes la hacen y para quiénes), función u ocasión, materiales e instrumentos que hay, tecnología disponible y época"
FA = "Obra A, canción de trabajo en una cosecha: tempo 100 pulsos por minuto, voz y palmas, un solista llama y el grupo responde"
FB = "Obra B, música de baile de una fiesta de pueblo: tempo 126 pulsos por minuto, guitarra, tambor y voces, con un estribillo que se repite"
FC = "Obra C, fanfarria de apertura de un acto escolar: trompetas y timbal, dinámica f, 8 compases"
FD = "Obra D, canción de cuna: una voz sola, tempo 56 pulsos por minuto, dinámica p, melodía por grados"
FE = "Obra E, rock urbano de un concierto: guitarra eléctrica, bajo, batería, dinámica f, tempo 130 pulsos por minuto"

# ---------------------------------------------------------------- OA 07 · clase 1 (elementos del contexto)
L(
    OA7, 1,
    f"Lápiz y papel. {CTX.capitalize()}. Fichas de la clase: {FA}; {FB}; {FC}; {FD}; {FE}. Todo está escrito en los ejercicios.",
    "Aprenderé a reconocer los elementos del contexto en que surge una música: dónde, quiénes, para qué, con qué materiales y en qué tiempo. Sirve para entender por qué una obra suena como suena.",
    ["Sé reconocer músicas de tradición escrita, oral y popular.", "Sé describir tempo, dinámica y textura.", "Sé qué es el propósito expresivo."],
    [
        f"Una obra musical no aparece de la nada: surge en un contexto, es decir, en las circunstancias en que se crea y se usa. En esta clase usamos estos {CTX}. Preguntarse por el contexto ayuda a comprender por qué una música tiene ciertos rasgos y no otros.",
        f"Por ejemplo, {FD}. Su contexto es doméstico: una persona arrulla a un bebé en un hogar. La función es dormir, y por eso es lenta, suave y de melodía tranquila, por grados. En cambio, {FC}. Su contexto es un acto colectivo y su función es anunciar, y por eso suena fuerte y con instrumentos que se oyen a lo lejos.",
        "No todos los elementos del contexto aparecen siempre en una obra: a veces solo conocemos la función y los instrumentos, y no la época. Al explicar, solo afirmamos lo que sabemos. Si algo no se sabe, se dice «no sé» o se pregunta a quien enseña. Inventar datos del contexto es un error, porque la explicación deja de ser verdadera.",
    ],
    [("contexto", "circunstancias en que se crea y se usa una música"), ("función", "para qué se usa una música: dormir, bailar, trabajar, anunciar"), ("comunidad", "las personas que hacen y escuchan la música"), ("ocasión", "momento en que se hace la música, como una fiesta"), ("rasgo sonoro", "algo que se oye: tempo, dinámica, instrumentos, textura")],
    [
        ("Reconocer la función", f"{FD}. ¿Cuál es la función más probable de esta música: dormir a un bebé o animar un baile?", ["La obra es lenta y suave.", "Eso encaja con arrullar."], "Dormir a un bebé"),
        ("Reconocer un elemento del contexto", f"{FC}. ¿Qué elemento del contexto indica la frase «de apertura de un acto escolar»: la ocasión o el material?", ["Un acto escolar es un momento y un lugar colectivo.", "Eso es la ocasión."], "La ocasión"),
    ],
    [
        ("Afirmar datos del contexto que no se conocen.", "La explicación debe apoyarse en lo que se sabe de la obra.", "Di solo lo que sabes y marca lo que no."),
        ("Pensar que solo existe la letra o la melodía y el contexto no importa.", "El contexto explica por qué la música suena como suena.", "Pregunta dónde, quiénes, para qué y con qué."),
    ],
    [
        ex("¿Cómo se llaman las circunstancias en que se crea y se usa una música?", "Contexto", "Incluye lugar, comunidad y función."),
        ex(f"{FB}. ¿Cuál es su función: bailar o dormir?", "Bailar", "Es música de baile de una fiesta."),
        ex(f"{FA}. ¿Dónde se usa esa canción: en una cosecha o en un concierto de rock?", "En una cosecha", "La ficha dice que es una canción de trabajo en una cosecha."),
    ],
    [
        ex(f"{FE}. ¿Qué material hace posible su sonido: la guitarra eléctrica o el pandero?", "La guitarra eléctrica", "La ficha nombra guitarra eléctrica, bajo y batería."),
        ex(f"{FA}. ¿Qué comunidad participa: un solista y un grupo que responde, o una sola persona que toca sin público?", "Un solista y un grupo que responde", "La ficha dice que un solista llama y el grupo responde."),
        ex(f"{FC}. ¿Cuáles instrumentos usa: trompetas y timbal o guitarra eléctrica y batería?", "Trompetas y timbal", "La ficha de la obra C los nombra."),
    ],
    [
        arith(f"{FB}. Esta música se baila durante una fiesta de 3 horas con la misma música en bloques de 20 minutos. ¿Cuántos bloques de música hay?", "3*60//20", "3 horas son 180 minutos y cada bloque dura 20 minutos.", " bloques"),
        ex("Cuenta cuántas de estas obras tienen función de acompañar un movimiento (trabajo o baile): A cosecha, B baile, C fanfarria, D cuna, E concierto.", "2", "Son la A (trabajo) y la B (baile)."),
        arith(f"{FD}. La canción de cuna dura 28 pulsos a 56 pulsos por minuto. ¿Cuántos segundos dura?", "28*60//56", "Cada pulso dura poco más de un segundo y 28 pulsos son medio minuto.", " segundos"),
    ],
    [
        ex(f"Luis dice que la obra D es lenta porque su compositor era perezoso. ¿Qué afirmación es más sólida?", "Es lenta y suave porque su función es dormir a un bebé", "La función explica el rasgo y se puede comprobar en la ficha."),
        ex(f"Nadie sabe en qué año se creó la obra A. Una estudiante dice que fue en 1970. ¿Es correcto afirmarlo?", "No: no se conoce ese dato", "Inventar el contexto vuelve falsa la explicación."),
    ],
    [
        ex(f"Si la obra E se tocara en una plaza sin electricidad, ¿qué elemento del contexto cambiaría: la tecnología disponible o la función?", "La tecnología disponible", "Sin electricidad no se puede usar guitarra eléctrica."),
        ex(f"{FB}. ¿Qué rasgo sonoro ayuda a que se pueda bailar: el tempo de 126 pulsos por minuto o la partitura?", "El tempo de 126 pulsos por minuto", "El pulso marcado y rápido permite bailar."),
    ],
    [ex("En una fiesta de curso, tu grupo canta una canción para esperar el inicio de un acto, y otra para despedir. ¿Qué elemento del contexto es «esperar el inicio de un acto»: la función o el material?", "La función", "Indica para qué se usa la música.")],
    [ex("¿Qué elemento del contexto indica para qué se usa la música?", "La función", "Es el propósito de uso."), ex("¿Qué elemento del contexto son las personas que hacen y escuchan la música?", "La comunidad", "Son quienes la crean y escuchan."), ex("¿Qué se hace si no se sabe un dato del contexto?", "Decir que no se sabe o preguntar", "No se inventa.")],
    (
        f"Lee la ficha: «{FA}». Completa una tabla con cinco filas: función, comunidad, materiales o instrumentos, un rasgo sonoro y una pregunta que quedaría por averiguar sobre el contexto. Responde solo con lo que dice la ficha; en la pregunta, escribe algo que no se sabe.",
        "Función: acompañar el trabajo de la cosecha. Comunidad: un solista y un grupo que participa. Materiales: voz y palmas. Rasgo sonoro: tempo de 100 pulsos por minuto y llamado y respuesta. Pregunta: ¿cuántas personas del grupo cantan en la cosecha?",
        ["usa solo lo que dice la ficha", "completa las cinco filas", "formula una pregunta sobre lo que no se sabe"],
        ["tabla escrita"],
        ["inventar datos", "dejar filas sin completar"],
        "Reconoce la tabla y pide señalar en la ficha dónde aparece cada dato.",
    ),
    "Escribe dos elementos del contexto de una música que escuches en tu casa.",
    "Elige una música de tu casa y escribe cinco preguntas sobre su contexto que podrías hacer a una persona.",
)

# ---------------------------------------------------------------- OA 07 · clase 2 (función y rasgos sonoros)
L(
    OA7, 2,
    f"Lápiz y papel. Fichas: {FA}; {FB}; {FC}; {FD}; {FE}. Todo está escrito en los ejercicios. Cuida el volumen si pruebas los ritmos con palmas.",
    "Aprenderé a relacionar la función de una música con sus rasgos sonoros: tempo, dinámica, instrumentos, textura y forma. Sirve para explicar por qué una obra suena como suena a partir de para qué se usa.",
    ["Sé reconocer elementos del contexto.", "Sé describir tempo, dinámica y textura.", "Sé qué es el llamado y respuesta."],
    [
        "La función de una música influye mucho en sus rasgos. Una música para dormir busca calma y tiene tempo lento, dinámica suave y una melodía tranquila, por grados. Una música para bailar necesita un pulso marcado y un tempo que se pueda seguir con el cuerpo. Una música para anunciar algo se oye a distancia y usa dinámica fuerte y sonidos que llaman la atención.",
        "También la comunidad influye. Si muchas personas participan, la música suele tener partes fáciles de repetir, como un estribillo o un llamado y respuesta, en que un solista llama y el grupo responde. Si la música se hace para coordinar un trabajo, tiene un pulso muy parejo para mover el cuerpo a la vez. Por eso, el mismo tipo de rasgo se repite en músicas de funciones parecidas.",
        "Para explicar la relación, se usa una frase con «porque»: «La obra A tiene pulso marcado porque se usa para acompañar un trabajo colectivo». La frase une la función con un rasgo sonoro que se puede comprobar en la ficha. Si el rasgo no aparece en la ficha o no tiene relación con la función, la explicación no es válida.",
    ],
    [("función", "para qué se usa una música"), ("pulso marcado", "pulso fácil de sentir y seguir con el cuerpo"), ("llamado y respuesta", "un solista llama y el grupo responde"), ("estribillo", "parte que se repite igual y que todos aprenden"), ("explicación con «porque»", "frase que une una función con un rasgo sonoro")],
    [
        ("Unir función y rasgo", f"{FD}. ¿Qué rasgo sonoro se relaciona con su función de dormir: dinámica p o dinámica f?", ["Dormir pide calma.", "Calma se relaciona con dinámica suave."], "Dinámica p"),
        ("Escribir la explicación", f"{FB}. Completa: «La obra B tiene un tempo rápido de 126 porque su función es…».", ["La ficha dice que es música de baile.", "El tempo permite seguir el baile."], "Bailar en la fiesta"),
    ],
    [
        ("Unir una función con un rasgo que no tiene relación.", "La explicación debe ser verdadera y relacionada.", "Revisa que el rasgo aparezca en la ficha y tenga sentido con la función."),
        ("Explicar sin decir «porque».", "Sin «porque» no hay relación entre función y rasgo.", "Escribe una frase: «tiene X porque se usa para Y»."),
    ],
    [
        ex("Una música para dormir, ¿suena más probable lenta y suave o rápida y fuerte?", "Lenta y suave", "La función de dormir pide calma."),
        ex("Una música para anunciar algo de lejos, ¿suena más probable con dinámica f o p?", "Con dinámica f", "Debe oírse a distancia."),
        ex("¿Qué es el llamado y respuesta?", "Un solista llama y el grupo responde", "Permite que todo el grupo participe."),
    ],
    [
        ex(f"{FA}. ¿Qué rasgo ayuda a que todo el grupo participe: el llamado y respuesta o la guitarra eléctrica?", "El llamado y respuesta", "La ficha dice que el solista llama y el grupo responde."),
        ex(f"{FC}. ¿Qué rasgo se relaciona con su función de anunciar: dinámica f o tempo de 56 pulsos por minuto?", "Dinámica f", "La ficha dice f, que se oye a lo lejos."),
        ex(f"{FE}. ¿Qué rasgo se relaciona con un concierto grande: dinámica f con instrumentos eléctricos o voz sola en p?", "Dinámica f con instrumentos eléctricos", "Un concierto grande necesita volumen que llegue al público."),
    ],
    [
        ex(f"Cuenta cuántas de estas obras tienen dinámica f según las fichas: A, B, C, D y E.", "2", "Las fichas C y E dicen f; A y B no indican f, y D es p."),
        arith(f"{FA}. Hay 8 llamados del solista y cada uno recibe 1 respuesta del grupo. ¿Cuántas intervenciones hay entre solista y grupo?", "8+8", "Se suman llamados y respuestas.", " intervenciones"),
        arith(f"{FB}. El estribillo dura 4 compases de 4 pulsos y se repite 5 veces. ¿Cuántos pulsos suena el estribillo en total?", "4*4*5", "Se multiplican los compases, los pulsos y las repeticiones.", " pulsos"),
    ],
    [
        ex(f"Ana dice: «La obra D tiene tempo lento porque es una fanfarria». ¿Es correcta su explicación?", "No: la obra D es una canción de cuna, no una fanfarria", "La explicación debe usar la función real de la ficha."),
        ex(f"Compara A y D. ¿Cuál tiene un pulso más rápido: la A o la D?", "La A", "A va a 100 y D va a 56 pulsos por minuto."),
    ],
    [
        arith(f"La obra B va a 126 y la D va a 56 pulsos por minuto. ¿Cuántos pulsos por minuto más rápida es la B?", "126-56", "Se restan los dos tempos.", " pulsos por minuto"),
        ex("Entre las obras A, B, D y E de las fichas, ¿cuál tiene el tempo más lento?", "La D", "La D va a 56 pulsos por minuto y las otras van a 100 o más."),
    ],
    [ex("Un grupo de personas que van caminando juntas cantan una canción con un pulso marcado y una melodía muy simple. ¿Qué función sugiere ese pulso: coordinar los pasos o dormir?", "Coordinar los pasos", "Un pulso marcado ayuda a caminar o trabajar al mismo ritmo.")],
    [ex("¿Qué rasgo tiene una música de cuna?", "Tempo lento y dinámica suave", "Es lo que pide la función de dormir."), ex("¿Qué rasgo ayuda a bailar?", "Un pulso marcado", "Permite seguirlo con el cuerpo."), ex("¿Cómo se escribe una explicación?", "Con «porque»: rasgo y función", "Une el rasgo con la función.")],
    (
        f"Elige una de estas fichas: A) «{FA}», B) «{FB}» o C) «{FE}». Escribe tres frases con «porque» que expliquen la relación entre la función de la obra y tres rasgos sonoros distintos de la ficha. Comprueba que cada rasgo aparece en la ficha.",
        "Ficha B. 1) Tiene tempo rápido de 126 porque se usa para bailar. 2) Tiene un estribillo que se repite porque así todos pueden cantarlo en la fiesta. 3) Usa tambor y guitarra porque son instrumentos que marcan el pulso y llenan el sonido en una fiesta de pueblo.",
        ["escribe tres frases con «porque»", "los rasgos aparecen en la ficha", "los rasgos se relacionan con la función"],
        ["tres frases escritas"],
        ["no usar «porque»", "usar rasgos que no están en la ficha"],
        "Reconoce las frases y pide señalar en la ficha cada rasgo que se menciona.",
    ),
    "Escribe una frase con «porque» sobre una música que oyes seguido.",
    "Escribe una explicación comparando la función y los rasgos de las obras A y D.",
)

# ---------------------------------------------------------------- OA 07 · clase 3 (materiales, comunidad y época)
L(
    OA7, 3,
    f"Lápiz y papel. {CTX.capitalize()}. Fichas inventadas en los ejercicios. Todo lo que se dice de la época es general; no se afirman fechas.",
    "Aprenderé cómo los materiales, la tecnología y la comunidad de cada época influyen en la música. Sirve para explicar por qué hay instrumentos y formas de hacer música distintos en lugares y tiempos distintos.",
    ["Sé reconocer función y rasgos sonoros.", "Sé qué es una comunidad.", "Sé distinguir instrumentos acústicos de eléctricos."],
    [
        "La música depende de los materiales y la tecnología disponibles. Los instrumentos acústicos, como el pandero o la flauta, se hacen con materiales como madera, cuero o caña y no necesitan electricidad. Los instrumentos eléctricos, como la guitarra eléctrica, necesitan amplificación y solo existen desde que hay electricidad y aparatos para amplificar el sonido.",
        "La comunidad también influye. En una comunidad pequeña, muchas personas participan cantando y tocando, y la música suele ser fácil de aprender de oído. Cuando existen escuelas de música y partituras, se pueden hacer obras más largas y complejas que se interpretan igual en muchos lugares. Con las grabaciones y las plataformas, personas de lugares lejanos pueden oír la misma música sin estar presentes.",
        "La época cambia lo que se puede hacer, pero no vale más una época que otra: cada música responde a las necesidades de su gente. Al explicar, conviene decir qué elemento del contexto influye y cómo se nota en la música: «porque había solo instrumentos acústicos, la música se hizo con palmas, tambor y voces». Y si no se conoce un dato, se dice «no se sabe».",
    ],
    [("acústico", "instrumento que suena sin electricidad"), ("eléctrico", "instrumento que usa electricidad y amplificación"), ("tecnología", "herramientas y aparatos que se usan para hacer o difundir música"), ("grabación", "registro del sonido que permite escucharlo después"), ("época", "periodo de tiempo con ciertas costumbres y recursos")],
    [
        ("Elegir el instrumento", "En una plaza sin electricidad, ¿qué instrumento se puede usar: un pandero o una guitarra eléctrica?", ["La guitarra eléctrica necesita electricidad.", "El pandero es acústico."], "Un pandero"),
        ("Relacionar la tecnología", "Antes de las grabaciones, ¿cómo se podía oír una canción lejos del lugar donde se cantaba: aprendiéndola de personas que la cantaban en persona o con un archivo digital?", ["Antes no había grabaciones.", "La canción viajaba con las personas que la cantaban."], "Aprendiéndola de personas que la cantaban en persona"),
    ],
    [
        ("Pensar que la música de una época es mejor que la de otra.", "Cada música responde a las necesidades y recursos de su gente.", "Explica qué elementos del contexto influyen sin decir cuál es mejor."),
        ("Afirmar fechas sin conocerlas.", "Una explicación debe apoyarse en datos seguros.", "Di «hace mucho tiempo» o «no se sabe» si no hay certeza."),
    ],
    [
        ex("El pandero, ¿es un instrumento acústico o eléctrico?", "Acústico", "Suena sin electricidad."),
        ex("La guitarra eléctrica, ¿necesita electricidad para sonar fuerte?", "Sí", "Para sonar fuerte usa amplificación eléctrica."),
        ex("¿Qué permite que una canción se escuche en lugares lejanos sin que viaje quien la canta: la grabación o el ensayo general?", "La grabación", "Registra el sonido para escucharlo después."),
    ],
    [
        ex("Una comunidad pequeña tiene solo instrumentos acústicos: tambor, flauta y voces. ¿Qué tipo de obra es más probable que haga: una con guitarra eléctrica o una con voces y percusión?", "Una con voces y percusión", "Los instrumentos disponibles condicionan la música."),
        ex("Una escuela de música que usa partituras permite que una obra se interprete en distintos lugares con las mismas notas. ¿Qué elemento del contexto es la partitura: tecnología o función?", "Tecnología", "La partitura es una herramienta para registrar la música."),
        ex("¿Qué dice el texto sobre cuál época es mejor?", "Que ninguna vale más que otra", "Cada una responde a sus necesidades."),
    ],
    [
        ex("Cuenta cuántos de estos instrumentos son acústicos: pandero, guitarra eléctrica, flauta, bajo eléctrico, tambor.", "3", "Son el pandero, la flauta y el tambor."),
        arith("Un pueblo tiene 5 flautas, 7 panderos y 3 tambores. ¿Cuántos instrumentos acústicos tiene?", "5+7+3", "Todos son acústicos y se suman.", " instrumentos"),
        ex("Una canción se aprendió de oído de generación en generación y no se escribió. ¿Qué elemento del contexto lo explica: la tradición oral de la comunidad o la tecnología de grabación?", "La tradición oral de la comunidad", "Se transmitió sin partitura ni grabación."),
    ],
    [
        ex("Un estudiante dice que la música de hace mucho tiempo era mala porque no tenía guitarra eléctrica. ¿Qué responderías?", "Que cada música usa los recursos de su gente y no se compara por tener o no electricidad", "Los recursos explican las diferencias, no el valor."),
        ex("Un cuaderno escolar dice que una canción «se creó en 1850». Nadie sabe la fecha. ¿Qué es más correcto escribir: «hace mucho tiempo, no se conoce la fecha exacta» o «en 1850»?", "Hace mucho tiempo, no se conoce la fecha exacta", "Se evita afirmar datos inseguros."),
    ],
    [
        arith("Un grupo escucha 6 músicas acústicas de 3 minutos y 4 eléctricas de 5 minutos. ¿Cuántos minutos escuchan?", "6*3+4*5", "Se calcula cada grupo y se suma.", " minutos"),
        ex("Una canción tiene versiones distintas porque se aprendió de oído en tres pueblos. ¿Qué contexto lo explica: la comunidad y la tradición oral o la tecnología eléctrica?", "La comunidad y la tradición oral", "Las versiones nacen al aprender de oído."),
    ],
    [ex("En una escuela sin amplificación se presenta una obra con voces y panderos en un patio grande. ¿Qué debe hacer el grupo para que se oiga: cantar con buena proyección y ubicarse cerca del público o cantar bajito y lejos?", "Cantar con buena proyección y ubicarse cerca del público", "Sin amplificación, el sonido depende de la voz y la distancia.")],
    [ex("¿Qué es un instrumento acústico?", "Uno que suena sin electricidad", "Se toca sin amplificación."), ex("¿Qué permite escuchar música lejos del lugar donde se toca?", "La grabación", "Registra el sonido."), ex("¿Cuál época es mejor?", "Ninguna", "Cada música responde a su contexto.")],
    (
        "Compara estas dos fichas: A) un canto en una cosecha con voz y palmas, B) un rock con guitarra eléctrica, bajo y batería en un concierto. Escribe una tabla con tres filas (materiales, comunidad y tecnología disponible) para cada una y una frase de cierre que compare cómo el contexto influye en el sonido. No afirmes fechas.",
        "Obra A: materiales: voz y palmas; comunidad: personas que trabajan juntas; tecnología: no necesita electricidad. Obra B: materiales: guitarra eléctrica, bajo y batería; comunidad: banda y público de concierto; tecnología: amplificación y electricidad. Cierre: la obra A se puede hacer en un campo sin electricidad porque usa solo el cuerpo y la voz, y la B necesita electricidad y amplificación porque usa instrumentos eléctricos.",
        ["completa las tres filas para ambas obras", "relaciona contexto y sonido", "no afirma fechas"],
        ["tabla escrita", "frase de cierre"],
        ["afirmar fechas", "decir cuál época es mejor"],
        "Reconoce la tabla y pide señalar qué dato de cada fila se ve en el sonido.",
    ),
    "Escribe tres instrumentos acústicos y tres eléctricos que conozcas.",
    "Escribe una explicación sobre cómo cambia la forma de compartir música cuando existen grabaciones.",
)

# ---------------------------------------------------------------- OA 07 · clase 4 (explicar la relación con evidencia)
EST = "una explicación sólida tiene cuatro partes: 1) nombra la obra; 2) nombra un elemento del contexto; 3) nombra un rasgo sonoro; 4) los une con «porque» y se puede comprobar en la ficha"

L(
    OA7, 4,
    f"Lápiz y papel. Estructura de la clase: {EST}. Fichas: {FA}; {FB}; {FC}; {FD}; {FE}.",
    "Aprenderé a explicar con evidencia la relación entre una obra y su contexto, usando una estructura de cuatro partes que se puede comprobar. Sirve para escribir o decir una explicación clara y verdadera.",
    ["Sé reconocer función y rasgos sonoros.", "Sé reconocer materiales y comunidad.", "Sé usar «porque» para unir ideas."],
    [
        f"Para explicar la relación entre una obra y su contexto se usa una estructura. {EST}. Por ejemplo: «La obra D (nombre de la obra) es una canción de cuna (elemento del contexto: función) y tiene dinámica p y tempo lento (rasgo sonoro) porque busca dormir a un bebé (unión con porque)».",
        "Comprobar significa volver a la ficha o a la audición y verificar que cada dato esté ahí. Si dices «tiene guitarra eléctrica» y la ficha no la menciona, la explicación es falsa. Si dices «tempo rápido» pero la ficha dice 56 pulsos por minuto, también es falsa. Una explicación con muchos datos falsos es peor que una corta pero verdadera.",
        "También se puede comparar dos obras con la misma estructura: se explican ambas y se dice qué rasgo cambia y por qué. Por ejemplo, la cuna va lenta y la fiesta va rápida porque tienen funciones distintas. Al terminar se revisa la explicación con los cuatro puntos, y se mejora lo que falte. Una explicación se puede mejorar siempre.",
    ],
    [("explicación sólida", "explicación que nombra obra, contexto y rasgo y los une con «porque»"), ("comprobar", "revisar que cada dato esté en la ficha o en la audición"), ("evidencia", "dato que respalda lo que se dice"), ("comparar", "decir qué se parece y qué cambia entre dos obras"), ("revisar", "leer la explicación y ajustarla")],
    [
        ("Contar las partes", f"«La obra B (fiesta de pueblo) tiene tempo rápido de 126.» ¿Cuántas partes de la estructura cumple?", ["Nombra la obra y el contexto (fiesta de pueblo).", "Nombra el rasgo sonoro (tempo 126).", "No usa «porque», así que no une."], "3 partes"),
        ("Corregir una explicación falsa", f"«La obra D es una fanfarria con trompetas.» La ficha dice que es una canción de cuna con una voz sola. ¿Qué debe cambiarse?", ["La ficha dice cuna y voz sola.", "No hay fanfarria ni trompetas."], "El tipo de obra y los instrumentos"),
    ],
    [
        ("Agregar muchos datos sin comprobarlos.", "Un dato falso hace falsa toda la explicación.", "Verifica cada dato en la ficha."),
        ("Olvidar la unión con «porque».", "Sin ella no hay relación entre contexto y rasgo.", "Escribe el porqué."),
    ],
    [
        ex("¿Cuántas partes tiene una explicación sólida en la clase?", "4", "La estructura de la clase tiene cuatro partes."),
        ex("¿Qué se hace para comprobar un dato?", "Volver a la ficha y verificar que esté", "Comprobar es revisar en la ficha."),
        ex("Una explicación corta y verdadera, ¿es mejor o peor que una larga con datos falsos?", "Mejor", "Un dato falso la invalida."),
    ],
    [
        ex(f"«La obra E (rock de concierto) tiene dinámica f porque es música de concierto.» ¿Está bien comprobada con la ficha?", "Sí", "La ficha dice que E tiene dinámica f y es música de concierto."),
        ex(f"«La obra A tiene guitarra eléctrica porque es una canción de trabajo.» ¿Está bien comprobada?", "No: la ficha de A dice voz y palmas", "El dato de la guitarra eléctrica no aparece."),
        ex(f"«La obra C tiene trompetas y timbal porque se usa en la apertura de un acto escolar.» ¿Cuántas partes de la estructura tiene?", "4", "Nombra la obra, el contexto, el rasgo y los une con «porque»."),
    ],
    [
        ex("Cuenta cuántas de estas explicaciones tienen las 4 partes: (1) «La obra B se baila porque es música de fiesta y tiene un tempo de 126.» (2) «La obra D es lenta.» (3) «La obra A usa palmas porque se usa en el trabajo.» (4) «La obra E es de rock.»", "2", "Cumplen las partes la (1) y la (3); la (2) y la (4) no unen con «porque» ni nombran contexto y rasgo."),
        arith(f"{FB}. Esta obra se toca con un tempo de 126 pulsos por minuto y tiene 63 pulsos. ¿Cuántos segundos dura?", "63*60//126", "63 pulsos a 126 por minuto duran 30 segundos.", " segundos"),
        ex("Comparas las obras D (56 pulsos por minuto) y B (126 pulsos por minuto). ¿Cuál es la explicación sólida: (a) «D va más lento que B porque su función es dormir y la de B es bailar» o (b) «D va más lento que B porque sí»?", "(a)", "Une el rasgo con las funciones."),
    ],
    [
        ex("Ana dice que no hace falta comprobar si el dato está en la ficha porque lo recuerda. ¿Qué puede pasar?", "Que mencione un dato falso", "Comprobar evita errores de memoria."),
        ex("Dos estudiantes explican la obra D. Uno dice «dinámica p porque busca calma» y otro «dinámica f porque busca calma». ¿Quién tiene la explicación correcta con la ficha?", "El primero", "La ficha dice p, y p corresponde a la calma."),
    ],
    [
        arith("Un curso revisó 20 explicaciones y 14 cumplieron las 4 partes. ¿Cuántas no las cumplieron?", "20-14", "Se restan las que cumplieron del total.", " explicaciones"),
        ex(f"Escribe una explicación sólida para la obra D (usa la ficha: {FD}). Responde con la parte que debe aparecer después de «porque».", "su función es dormir a un bebé", "La unión explica el rasgo con la función."),
    ],
    [ex("En un trabajo, dos estudiantes explican la obra C. Una dice «Es una fanfarria con trompetas y timbal porque anuncia el inicio del acto». El otro dice «Es linda». ¿Cuál cumple mejor la estructura?", "La primera", "Tiene obra, contexto, rasgo y porque; la segunda solo da una opinión.")],
    [ex("¿Qué palabra une el contexto y el rasgo?", "Porque", "Hace la relación explícita."), ex("¿Qué hay que hacer con un dato que no está en la ficha?", "No usarlo o corregirlo", "Una explicación debe ser verdadera."), ex("¿Se puede mejorar una explicación?", "Sí", "Se revisa y se ajusta.")],
    (
        f"Escribe una explicación para cada una de estas dos obras: {FD}; y {FE}. Cada explicación debe cumplir las cuatro partes: {EST}. Luego escribe una frase que compare las dos obras y diga qué rasgo cambia y por qué. Revisa que todos los datos estén en las fichas.",
        "Obra D: es una canción de cuna con una voz sola y dinámica p porque busca dormir a un bebé. Obra E: es rock de concierto con guitarra eléctrica, bajo y batería y dinámica f porque es música de concierto. Comparación: la D es más lenta (56) que la E (130) porque una busca calma y la otra energía para un concierto.",
        ["cumple las cuatro partes en cada explicación", "los datos están en las fichas", "compara con «porque»"],
        ["dos explicaciones escritas", "una comparación"],
        ["usar datos que no están en la ficha", "no usar «porque»"],
        "Reconoce las explicaciones y pide señalar en la ficha cada dato.",
    ),
    "Revisa una explicación tuya y marca qué parte de la estructura le falta.",
    "Escribe una comparación entre dos músicas que conozcas usando la estructura de cuatro partes.",
)
