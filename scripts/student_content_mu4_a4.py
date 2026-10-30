"""Student material for 4.º básico Música, OA 07 (experiencias musicales y sonoras en la vida y la sociedad) y OA 08 (reflexión sobre fortalezas y áreas de mejora).

Todos los casos son ficticios; compartir experiencias personales es siempre opcional.
"""
from __future__ import annotations

from student_content_mu4_a import L
from student_lessons import arith, ex

OA7, OA8 = "MU04 OA 07", "MU04 OA 08"

# ---------------------------------------------------------------- OA 07 · clase 1
DIA = [
    (1, "7:30", "casa", "un despertador con un pitido", "sonido"),
    (2, "7:45", "casa", "una radio con una canción en el desayuno", "música"),
    (3, "8:15", "calle", "la bocina de un auto", "sonido"),
    (4, "10:00", "patio", "un curso que canta una ronda en el recreo", "música"),
    (5, "13:00", "casa", "conversación y cubiertos en el almuerzo", "sonido"),
    (6, "17:00", "casa", "una persona que tararea mientras ordena", "música"),
    (7, "21:00", "casa", "una canción suave en la radio antes de dormir", "música"),
]
DIA_TXT = " ".join(f"{n}) a las {h}, en {l}: {s} ({t})." for n, h, l, s, t in DIA)
DIA_MUS = sum(1 for d in DIA if d[4] == "música")
DIA_SON = sum(1 for d in DIA if d[4] == "sonido")

L(
    OA7, 1,
    f"Lápiz y papel. El «día de Camila» es un caso inventado: {DIA_TXT} Si quieres hacer tu propio mapa, compartir tus experiencias es opcional; puedes usar el día de Camila en su lugar.",
    "Aprenderé a mapear los sonidos y las músicas de situaciones cotidianas, distinguiendo la música de otros sonidos del entorno. Sirve para darme cuenta de cuánta música y sonido hay en la vida diaria.",
    ["Sé nombrar cualidades del sonido.", "Sé qué es una canción.", "Sé leer una lista ordenada por la hora."],
    [
        "Una situación cotidiana es algo que ocurre en la vida de todos los días: despertar, ir al colegio, almorzar, jugar, dormir. En cada una hay sonidos. Una experiencia sonora es el momento en que escuchas los sonidos de tu entorno. Una experiencia musical es el momento en que haces o escuchas música, es decir, sonidos organizados con una intención musical.",
        f"No todo sonido es música. Un despertador, una bocina o los cubiertos son sonidos del entorno. Una canción, una ronda o un tarareo son música. En el día de Camila: {DIA_TXT} Hay {DIA_MUS} experiencias musicales y {DIA_SON} sonidos del entorno. A veces es difícil decidir, y por eso se pregunta si alguien organizó los sonidos con intención musical.",
        "Un mapa de sonidos es una lista o dibujo que ordena las experiencias sonoras y musicales de un día, con la hora, el lugar y el tipo. Sirve para ver cuándo aparece la música y cuándo solo hay sonidos. Cuando hagas tu mapa, puedes anotar solo lo que quieras compartir. Si prefieres, usa un caso inventado o el de Camila.",
    ],
    [("cotidiano", "de todos los días"), ("experiencia sonora", "momento en que escuchas sonidos de tu entorno"), ("experiencia musical", "momento en que haces o escuchas música"), ("sonido del entorno", "sonido que no tiene intención musical"), ("mapa de sonidos", "lista o dibujo ordenado de los sonidos de un día")],
    [
        ("Clasificar", f"Día de Camila: {DIA_TXT} ¿Qué experiencia es la número 3: musical o sonora del entorno?", ["Es la bocina de un auto.", "Nadie la organizó como música."], "Un sonido del entorno"),
        ("Contar", f"Día de Camila: {DIA_TXT} ¿Cuántas experiencias musicales hay?", ["Musicales: 2, 4, 6 y 7.", "Son 4."], f"{DIA_MUS} experiencias musicales"),
    ],
    [
        ("Pensar que todo sonido es música.", "La música tiene una intención y una organización.", "Pregunta si alguien organizó los sonidos como música."),
        ("Decir que en tu día no hay música porque no escuchaste un concierto.", "La música también está en tarareos, rondas o canciones de la radio.", "Revisa cada momento del día."),
    ],
    [
        ex(f"Día de Camila: {DIA_TXT} ¿En qué lugar ocurre la experiencia 4?", "En el patio", "Así lo dice el mapa."),
        ex(f"Día de Camila: {DIA_TXT} ¿A qué hora suena la canción suave antes de dormir?", "A las 21:00", "El mapa lo indica en la experiencia 7."),
        ex("¿Un tarareo mientras se ordena es música o sonido del entorno?", "Música", "Tararear organiza sonidos con intención musical."),
    ],
    [
        ex(f"Día de Camila: {DIA_TXT} Escribe los números de las experiencias que ocurren en la casa y son música.", "2, 6 y 7", "Son la radio, el tarareo y la canción suave antes de dormir."),
        ex(f"Día de Camila: {DIA_TXT} ¿Cuántas experiencias son sonidos del entorno?", str(DIA_SON), "Son el despertador, la bocina y los cubiertos."),
        ex("¿Qué diferencia hay entre una experiencia sonora y una musical?", "La musical tiene intención musical; la sonora es cualquier sonido del entorno", "No todo sonido se organiza como música."),
    ],
    [
        arith(f"En el día de Camila hay {len(DIA)} experiencias. Si {DIA_MUS} son musicales, ¿cuántas no lo son?", f"{len(DIA)}-{DIA_MUS}", "Se restan las musicales del total.", " experiencias"),
        arith("Camila despierta a las 7:30 y la canción de la radio suena a las 7:45. ¿Cuántos minutos pasan entre las dos experiencias?", "45-30", "Se restan los minutos: de 7:30 a 7:45.", " minutos"),
        ex(f"Día de Camila: {DIA_TXT} ¿Entre qué números hay más horas de diferencia: entre la 1 y la 2, o entre la 5 y la 6?", "Entre la 5 y la 6", "De 13:00 a 17:00 hay 4 horas, y de 7:30 a 7:45 hay 15 minutos."),
    ],
    [
        ex("Un niño dice que su mapa de sonidos no tiene música porque no fue a un concierto, pero cantó una ronda en el recreo. ¿Qué error comete?", "Piensa que la música solo está en conciertos", "La ronda es una experiencia musical."),
        ex("Una compañera no quiere compartir su día. ¿Qué puede hacer para participar en la actividad?", "Usar el día de Camila o un caso inventado", "Compartir experiencias personales es opcional."),
    ],
    [
        arith("Un mapa de sonidos tiene 10 experiencias. Si 6 son musicales y el resto son sonidos del entorno, ¿cuántos sonidos del entorno tiene?", "10-6", "Se restan las musicales del total.", " sonidos"),
        ex("Un mapa muestra la hora, el lugar y el tipo de cada experiencia. ¿Qué dato falta para saber qué sonó: la hora o lo que se escuchó?", "Lo que se escuchó", "Hay que anotar qué sonido o música fue."),
    ],
    [ex("En la mañana, en un bus escolar, suena una música de la radio y luego el motor. ¿Cuál de las dos es una experiencia musical?", "La música de la radio", "El motor es un sonido del entorno.")],
    [ex("¿Qué es una experiencia musical?", "Un momento en que haces o escuchas música", "Hay intención musical."), ex("¿Una bocina es música?", "No", "Es un sonido del entorno."), ex("¿Compartir tus experiencias personales es obligatorio?", "No", "Siempre es opcional.")],
    (
        "Haz un mapa de sonidos de un día con 5 experiencias. Puedes usar tu día (anotando solo lo que quieras compartir), un día inventado o el de Camila. Para cada una escribe la hora aproximada, el lugar, qué se oyó y si es música o sonido del entorno. Al final cuenta cuántas son musicales.",
        "Mapa inventado: 1) 8:00, casa, radio con canción (música). 2) 9:30, calle, bocina (sonido). 3) 12:00, patio, ronda (música). 4) 15:00, casa, batidora (sonido). 5) 20:00, casa, tarareo (música). Musicales: 3.",
        ["anota cinco experiencias con hora, lugar y qué se oyó", "clasifica cada una como música o sonido", "cuenta las musicales"],
        ["mapa escrito"],
        ["clasificar todo como música", "anotar datos personales que no quiere compartir"],
        "Reconoce el mapa y pregunta cómo decidió si algo es música; respeta si prefiere un caso inventado.",
    ),
    "Anota dos sonidos de tu casa y di cuál es música y cuál es un sonido del entorno.",
    "Pregunta a una persona de tu casa qué canción recuerda de su infancia, si quiere contártelo.",
)

# ---------------------------------------------------------------- OA 07 · clase 2
CEL = (
    "Caso A: en un cumpleaños, todos cantan una canción para felicitar a quien cumple años. "
    "Caso B: en una fiesta patria se baila cueca, una danza de pareja con pañuelo. "
    "Caso C: en una ceremonia de graduación suena una marcha mientras los estudiantes entran a la sala. "
    "Caso D: en la despedida de fin de año, un curso canta una canción que compuso para recordar lo vivido."
)

L(
    OA7, 2,
    f"Lápiz y papel. Los casos son ejemplos inventados: {CEL} Si quieres hablar de una celebración de tu familia o comunidad, es opcional y con las palabras que quieras.",
    "Aprenderé a relacionar la música con celebraciones, reuniones y festividades, y a explicar qué función cumple en cada una. Sirve para entender por qué la música acompaña los momentos importantes.",
    ["Sé qué es una experiencia musical.", "Sé que la música tiene intención.", "Sé comparar dos situaciones."],
    [
        "Una celebración es un momento en que las personas se reúnen para festejar o recordar algo. Una festividad es una celebración que se repite cada cierto tiempo, como las fiestas de un pueblo o de un país. En muchas celebraciones hay música. La música puede cumplir una función: reunir a las personas, marcar un momento importante, ayudar a bailar, felicitar o despedir.",
        f"Veamos cuatro casos. {CEL} En el caso A la música felicita y reúne. En el B ayuda a bailar y mantiene una tradición. En el C marca un momento importante: la entrada. En el D sirve para recordar y despedirse. Una misma música puede cumplir varias funciones.",
        "Para relacionar música y celebración, hazte tres preguntas: ¿qué se celebra?, ¿qué música suena y quién la hace?, ¿para qué sirve en ese momento? Las celebraciones de cada familia y comunidad son distintas, y todas se respetan. Si no quieres contar la tuya, usa un caso inventado.",
    ],
    [("celebración", "momento en que se festeja o se recuerda algo"), ("festividad", "celebración que se repite cada cierto tiempo"), ("función", "para qué sirve la música en un momento"), ("reunión", "encuentro de personas en un lugar"), ("tradición", "costumbre que pasa de generación en generación")],
    [
        ("Identificar la función", f"{CEL} ¿Qué función cumple la marcha del caso C?", ["Suena mientras los estudiantes entran.", "Marca el momento de la entrada."], "Marca un momento importante: la entrada"),
        ("Relacionar", f"{CEL} ¿En qué caso la música ayuda a bailar?", ["La cueca es una danza de pareja.", "Se baila en la fiesta patria."], "En el caso B"),
    ],
    [
        ("Creer que solo hay música en celebraciones grandes.", "También hay música en reuniones pequeñas y momentos cotidianos.", "Revisa todos los momentos, grandes y pequeños."),
        ("Decir que una celebración es mejor porque tiene más música.", "Cada comunidad celebra a su manera y todas se respetan.", "Describe qué música hay y para qué sirve, sin juzgar."),
    ],
    [
        ex(f"{CEL} ¿En qué caso la música sirve para felicitar a alguien?", "En el caso A", "Se canta para felicitar a quien cumple años."),
        ex(f"{CEL} ¿Qué se baila en el caso B?", "Cueca", "El caso B lo dice."),
        ex("¿Una festividad se repite cada cierto tiempo o ocurre una sola vez?", "Se repite cada cierto tiempo", "Esa es la diferencia con una celebración única."),
    ],
    [
        ex(f"{CEL} ¿Qué caso usa música para despedirse y recordar?", "El caso D", "El curso canta su canción en la despedida de fin de año."),
        ex(f"{CEL} ¿En qué casos las personas cantan?", "En los casos A y D", "En A cantan para felicitar y en D cantan su canción."),
        ex(f"{CEL} ¿En qué caso suena música mientras las personas entran a una sala?", "En el caso C", "La marcha suena mientras los estudiantes entran."),
    ],
    [
        arith("Un curso ensaya la canción de despedida 3 veces por semana durante 4 semanas. ¿Cuántos ensayos hace?", "3*4", "Se multiplican los ensayos semanales por las semanas.", " ensayos"),
        ex("En una fiesta del barrio suena música para que todos bailen y otra para el brindis. ¿Cuántas funciones distintas mencionamos?", "2", "Una sirve para bailar y la otra para el brindis, que marca un momento."),
        ex(f"{CEL} Una niña dice que la música del caso C no es importante porque nadie baila. ¿Qué error comete?", "Piensa que solo sirve la música para bailar", "La marcha cumple otra función: marcar el momento de la entrada."),
    ],
    [
        ex("Dos familias celebran de forma muy distinta, con músicas diferentes. ¿Una celebración es mejor que la otra?", "No", "Cada comunidad celebra a su manera y todas se respetan."),
        ex("Una niña cuenta que en su celebración casi no hay música, solo conversación. ¿Su celebración vale menos?", "No", "Cada familia celebra a su manera y todas se respetan."),
    ],
    [
        ex("Para un acto escolar, el curso debe elegir música que marque la entrada del director. ¿Qué función busca: bailar o marcar un momento?", "Marcar un momento", "La música anuncia la entrada."),
        arith("Una festividad dura 3 días y cada día tiene 2 momentos con música. ¿Cuántos momentos con música hay en total?", "3*2", "Se multiplican los días por los momentos.", " momentos"),
    ],
    [ex("En un cumpleaños, mientras todos cantan, una persona lleva la torta. ¿Qué función cumple la canción: felicitar o marcar el paso de una marcha?", "Felicitar", "Cantan para felicitar a quien cumple años.")],
    [ex("¿Qué es una celebración?", "Un momento en que se festeja o se recuerda algo", "Hay música en muchas."), ex("¿Qué función cumple una canción de cumpleaños?", "Felicitar", "Se canta para saludar a quien cumple años."), ex("¿Puedes contar una celebración de tu familia si no quieres?", "No es obligatorio", "Siempre puedes usar un caso inventado.")],
    (
        "Elige una celebración (puede ser una de los casos, una que conozcas o una inventada). Escribe: qué se celebra, qué música suena y quién la hace, para qué sirve y una cualidad del sonido que lo muestra (por ejemplo, rápida para bailar). Compartir una celebración propia es opcional.",
        "Se celebra un cumpleaños. Suena una canción cantada por todos. Sirve para felicitar. La cantamos fuerte y alegre.",
        ["describe la celebración y su música", "explica la función de la música", "da una cualidad del sonido como evidencia"],
        ["ficha escrita"],
        ["no explicar la función", "describir solo la fiesta y no la música"],
        "Reconoce la ficha y pregunta qué cambiaría si faltara la música; respeta si usa un caso inventado.",
    ),
    "Escribe una celebración y una función que cumple la música en ella.",
    "Pregunta a una persona de tu casa qué música recuerda de una fiesta, si quiere contártelo.",
)

# ---------------------------------------------------------------- OA 07 · clase 3
FUN = (
    "Caso 1, canción de cuna: se canta suave y lenta, en una habitación, para calmar y ayudar a dormir. "
    "Caso 2, marcha de desfile: tiene un pulso firme y fuerte, para que muchas personas caminen juntas. "
    "Caso 3, canción de trabajo: tiene un ritmo parejo y se canta mientras un grupo realiza una tarea larga, para que sea más ameno. "
    "Caso 4, música de baile de una fiesta: va rápida, con un pulso claro, para que todos bailen."
)

L(
    OA7, 3,
    f"Lápiz y papel. Los casos son ejemplos inventados: {FUN}",
    "Aprenderé a comparar las funciones sociales de la música (calmar, caminar juntos, acompañar el trabajo, bailar) y a relacionarlas con sus cualidades. Sirve para entender por qué cada música suena como suena.",
    ["Sé qué es una función de la música.", "Sé nombrar cualidades del sonido.", "Sé comparar con los mismos criterios."],
    [
        "La función social de la música es el papel que cumple para las personas: calmar, acompañar una actividad, reunir, celebrar, recordar o bailar. Comparar funciones es mirar dos casos con los mismos criterios: cuándo y dónde suena, qué cualidades tiene y para qué sirve. Así vemos que cada música se parece a su función.",
        f"Veamos cuatro casos. {FUN} La canción de cuna es suave y lenta porque calma. La marcha es fuerte y con pulso firme porque ordena los pasos de muchas personas. La canción de trabajo tiene ritmo parejo porque acompaña una tarea larga. La música de baile es rápida y con pulso claro porque invita a moverse.",
        "Cuando compares, usa los mismos criterios en todos los casos y no digas cuál es mejor. Una canción de cuna no es mejor ni peor que una marcha: sirven para cosas distintas. También recuerda que una misma música puede cumplir varias funciones, según el lugar y las personas.",
    ],
    [("función social", "papel que cumple la música para las personas"), ("calmar", "dar tranquilidad"), ("acompañar", "estar presente con otra actividad"), ("criterio", "pregunta que se usa para comparar"), ("ameno", "agradable y entretenido")],
    [
        ("Relacionar cualidad y función", f"{FUN} ¿Por qué la canción de cuna es suave y lenta?", ["Su función es calmar.", "Lo suave y lento tranquiliza."], "Porque su función es calmar y ayudar a dormir"),
        ("Comparar", f"{FUN} Compara el caso 2 y el caso 4 por el pulso y la función.", ["Caso 2: pulso firme, para caminar juntos.", "Caso 4: pulso claro, para bailar."], "Los dos tienen pulso marcado; el 2 sirve para caminar juntos y el 4 para bailar"),
    ],
    [
        ("Creer que la música de baile es mejor que una canción de cuna.", "Cada una sirve para algo distinto.", "Compara funciones, no pongas una por encima de otra."),
        ("Pensar que una música solo sirve para una función.", "Puede cumplir varias según el lugar y las personas.", "Pregunta dónde y para qué suena en ese momento."),
    ],
    [
        ex(f"{FUN} ¿Cuál es la función de la canción de cuna?", "Calmar y ayudar a dormir", "Así lo dice el caso 1."),
        ex(f"{FUN} ¿Qué caso se canta mientras se hace una tarea larga?", "El caso 3", "Es la canción de trabajo."),
        ex(f"{FUN} ¿Qué cualidad tiene la música de baile: rápida o lenta?", "Rápida", "El caso 4 va rápida."),
    ],
    [
        ex(f"{FUN} ¿En qué caso muchas personas caminan juntas?", "En el caso 2", "La marcha de desfile ordena los pasos."),
        ex(f"{FUN} ¿En qué casos la ficha describe el pulso como «firme» o «claro»?", "El 2 y el 4", "La marcha y la música de baile lo tienen."),
        ex(f"{FUN} ¿Cuál es el caso más suave y lento?", "El caso 1", "Es la canción de cuna."),
    ],
    [
        arith("Una canción de trabajo se canta durante 4 horas, 2 veces por semana. ¿Cuántas horas se canta en una semana?", "4*2", "Se multiplican las horas por las veces.", " horas"),
        ex(f"{FUN} Un niño dice que podrías usar la música de baile para dormir a un bebé. ¿Por qué no es lo más adecuado?", "Porque es rápida y no calma", "Su función es invitar a moverse, no tranquilizar."),
        ex("Una canción suave y lenta se usa para dormir a un bebé y también para tranquilizar a un niño asustado. ¿Una misma música puede tener más de una función?", "Sí", "La función depende de la situación y de las personas."),
    ],
    [
        ex("Ana dice que la marcha es más importante que la canción de cuna porque la oyen más personas. ¿Qué error comete?", "Jerarquiza las músicas", "Cada música tiene su función y ninguna es más importante."),
        ex("En un desfile la música es suave y lenta. ¿Cumpliría bien su función de ordenar los pasos?", "No", "Un desfile necesita un pulso firme y claro."),
    ],
    [
        ex(f"{FUN} Escribe el número del caso que sirve para el trabajo en grupo.", "3", "Es la canción de trabajo."),
        arith("Un curso ensaya 1 marcha de 3 minutos y 2 canciones de cuna de 2 minutos cada una. ¿Cuántos minutos ensaya?", "3+2*2", "Se suma la marcha y las dos canciones.", " minutos"),
    ],
    [ex("En una casa suena una música suave y lenta cuando un bebé duerme y una música rápida cuando se limpia la casa. ¿Qué función cumple cada una?", "La suave calma; la rápida acompaña la actividad", "Cada música coincide con lo que se necesita en ese momento.")],
    [ex("¿Qué función cumple una marcha?", "Ayudar a caminar juntos", "Su pulso firme ordena los pasos."), ex("¿Qué función cumple una canción de cuna?", "Calmar", "Es suave y lenta."), ex("¿Se puede decir cuál función es mejor?", "No", "Todas son útiles.")],
    (
        "Compara dos músicas de funciones distintas (pueden ser dos de los casos de la clase, o dos que conozcas) usando estos tres criterios: dónde y cuándo suena, qué cualidades tiene (rápida o lenta, suave o fuerte) y para qué sirve. Escribe una tabla y una frase final sin decir cuál es mejor.",
        "Cuna: de noche, en una habitación; suave y lenta; calmar. Marcha: en un desfile; fuerte y con pulso firme; caminar juntos. Frase: la cuna calma y la marcha ordena los pasos; sirven para cosas distintas.",
        ["usa los mismos tres criterios en las dos músicas", "relaciona cualidad y función", "no juzga cuál es mejor"],
        ["tabla escrita", "frase final"],
        ["usar criterios distintos para cada música", "decir cuál es mejor"],
        "Reconoce el uso de criterios iguales; si aparece un juicio de «mejor», pide reformularlo como una descripción.",
    ),
    "Escribe una función que cumple la música en tu día y una cualidad que lo muestra.",
    "Explica a una persona de tu casa por qué una canción de cuna es suave y lenta.",
)

# ---------------------------------------------------------------- OA 07 · clase 4
FICHA = (
    "Experiencia de Camila (caso inventado). Qué: su curso cantó una ronda. Cuándo: un recreo de la semana pasada. Dónde: en el patio. "
    "Quiénes: 12 compañeros. Qué se oyó: voces y palmas, a tempo rápido. Para qué: jugar. Lo que no sabemos: si otros cursos también cantan rondas."
)

L(
    OA7, 4,
    f"Lápiz y papel. Ficha de ejemplo: {FICHA} Documentar una experiencia propia es opcional; puedes usar un caso inventado y no escribir datos personales (nombres completos, direcciones, teléfonos).",
    "Aprenderé a documentar una experiencia musical o sonora con datos claros y sin generalizar, es decir, sin decir que lo que pasó en un caso pasa siempre o en todas partes. Sirve para contar lo que ocurrió con precisión y respeto.",
    ["Sé qué es una experiencia musical.", "Sé relacionar música y función.", "Sé escribir una ficha."],
    [
        "Documentar es registrar por escrito lo que ocurrió para poder revisarlo y compartirlo. Una buena ficha de una experiencia responde: qué pasó, cuándo, dónde, quiénes participaron (sin datos personales), qué se oyó y para qué sirvió. Estos datos hacen que otras personas entiendan lo que ocurrió aunque no hayan estado.",
        f"Generalizar es decir que lo que pasó en un caso pasa siempre o en todas partes. Veamos la ficha de ejemplo: {FICHA} Podemos decir «el curso de Camila cantó una ronda en el recreo», pero no podemos decir «todos los cursos cantan rondas», porque la ficha dice que no sabemos si otros cursos lo hacen. Para no generalizar usamos palabras como «en este caso», «en mi curso», «algunos» o «varios».",
        "También conviene separar lo que viste de lo que supones. «Cantaron una ronda» es un dato. «Seguramente les gusta cantar» es una suposición. Anota los datos y marca las suposiciones. Si compartes una experiencia propia, hazlo solo si quieres y sin datos personales. Así respetas a las personas y a ti mismo.",
    ],
    [("documentar", "registrar por escrito lo que ocurrió"), ("ficha", "hoja con datos ordenados sobre una experiencia"), ("generalizar", "decir que algo pasa siempre o en todas partes"), ("dato", "información que se observó"), ("suposición", "idea que no se comprobó")],
    [
        ("Separar dato y suposición", f"{FICHA} ¿«Cantaron una ronda» es un dato o una suposición?", ["La ficha lo dice en «Qué».", "Es lo que ocurrió."], "Un dato"),
        ("Evitar la generalización", f"{FICHA} ¿Se puede afirmar «todos los cursos cantan rondas en el recreo»? Explica.", ["La ficha cuenta un caso.", "Dice que no se sabe qué hacen otros cursos."], "No; la ficha solo cuenta un curso"),
    ],
    [
        ("Escribir «todos» o «siempre» para algo que viste una vez.", "Un caso no basta para hablar de todos.", "Usa «en este caso», «algunos» o «en mi curso»."),
        ("Incluir nombres completos y direcciones en la ficha.", "Son datos personales.", "Anota solo lo necesario: «un compañero», «el patio»."),
    ],
    [
        ex(f"{FICHA} ¿Cuántos compañeros participaron?", "12", "La ficha indica 12 compañeros."),
        ex(f"{FICHA} ¿Para qué cantaron la ronda?", "Para jugar", "Así lo indica la ficha."),
        ex(f"{FICHA} ¿Dónde ocurrió?", "En el patio", "El patio es el lugar de la ficha."),
    ],
    [
        ex("¿«Todas las familias cantan en las fiestas» documenta una experiencia o generaliza?", "Generaliza", "Habla de todas las familias sin saberlo."),
        ex("¿«En mi casa, la semana pasada, cantamos en un cumpleaños» documenta una experiencia o generaliza?", "Documenta una experiencia", "Dice dónde y cuándo, sin hablar de todos."),
        ex(f"{FICHA} ¿Qué dato desconocemos según la ficha?", "Si otros cursos también cantan rondas", "Es lo que la ficha señala que no se sabe."),
    ],
    [
        arith("Si 12 compañeros cantan y 5 de ellos además tocan palmas, ¿cuántos solo cantan?", "12-5", "Se restan los que también tocan palmas.", " compañeros"),
        ex("Elige la frase que no generaliza: (a) «Siempre se canta en las fiestas», (b) «En esta fiesta se cantó».", "(b)", "La (b) habla de un caso concreto."),
        ex("Elige el dato y no la suposición: (a) «Cantaron una ronda», (b) «Seguramente les gusta cantar».", "(a)", "La (a) es lo que ocurrió y la (b) es una suposición."),
    ],
    [
        ex("Un niño anota en su ficha el nombre completo y la dirección de un vecino. ¿Qué error comete?", "Incluye datos personales", "No deben aparecer en una ficha."),
        ex("Una niña dice: «como mi curso canta rondas, todos los cursos del colegio las cantan». ¿Qué falta para afirmarlo?", "Preguntar o comprobar con los otros cursos", "Un caso no basta; se necesita evidencia de todos."),
    ],
    [
        ex("Reescribe para no generalizar: «Nadie escucha música clásica». Elige: (a) «En mi curso, nadie dijo que escucha música clásica», (b) «Nadie escucha música clásica en Chile».", "(a)", "La (a) habla solo de lo que se observó en el curso."),
        arith("Una ficha tiene 7 campos y Camila llenó 4. ¿Cuántos campos le faltan?", "7-4", "Se restan los campos llenos del total.", " campos"),
    ],
    [ex("Una niña documenta que en su casa hubo un tarareo durante la limpieza. Dice: «las personas tararean al limpiar». ¿Qué cambio haces para no generalizar: decir «en mi casa, esa vez» o dejarlo igual?", "Decir «en mi casa, esa vez»", "Así habla solo de lo que observó.")],
    [ex("En Música: ¿Qué es generalizar?", "Decir que algo pasa siempre o en todas partes", "Va más allá del caso observado."), ex("¿Qué palabra ayuda a no generalizar: «todos» o «algunos»?", "Algunos", "Limita la afirmación."), ex("¿Qué debes evitar poner en una ficha?", "Datos personales", "Se protege a las personas.")],
    (
        "Documenta una experiencia musical o sonora de la semana (puede ser inventada, la de Camila o una propia que quieras compartir). Escribe una ficha con: qué, cuándo, dónde, quiénes (sin datos personales), qué se oyó, para qué y lo que no sabes. Después escribe una frase que describa lo ocurrido sin generalizar.",
        "Qué: se escuchó una canción en la radio. Cuándo: ayer en la tarde. Dónde: en mi casa. Quiénes: tres personas de mi casa. Qué se oyó: voz y guitarra, suave. Para qué: acompañar la limpieza. No sé: si en otras casas pasa lo mismo. Frase: en mi casa, ayer, escuchamos una canción mientras limpiábamos.",
        ["completa los siete campos de la ficha", "no incluye datos personales", "escribe una frase sin generalizar"],
        ["ficha escrita", "frase final"],
        ["escribir «todos» o «siempre»", "incluir datos personales"],
        "Reconoce la ficha y pregunta qué dato podría cambiar si fuera otra casa; ayuda a reemplazar «todos» por «en este caso».",
    ),
    "Cambia «siempre cantamos en el recreo» por una frase que no generalice.",
    "Documenta con una ficha la música que oíste en un trayecto o en un recreo.",
)

# ---------------------------------------------------------------- OA 08 · clase 1
REG = [("audición", 4), ("interpretación", 3), ("creación", 5)]
REG_TXT = (
    "Registro de Camila (caso inventado), puntos de 0 a 5: en audición describió bien 4 de 5 sonidos que se le pidieron; "
    "en interpretación mantuvo el pulso parejo en 3 de 5 ensayos; en creación su pieza cumplió 5 de 5 criterios de revisión."
)

L(
    OA8, 1,
    f"Lápiz y papel. Criterios conocidos antes de evaluar: en audición, describir bien los sonidos; en interpretación, mantener el pulso parejo; en creación, cumplir los criterios de revisión de la pieza. {REG_TXT}",
    "Aprenderé a identificar una fortaleza propia con evidencia: un dato de mis registros que muestra en qué voy bien. Sirve para saber qué mantener y celebrar mi progreso con honestidad.",
    ["Sé escuchar, tocar o crear música a mi nivel.", "Sé llevar un registro.", "Sé comparar números de 0 a 5."],
    [
        "Una fortaleza es algo que haces bien. Para identificarla no basta con decir «soy bueno en esto»: necesitas evidencia, es decir, un dato de tus registros o de tus trabajos que lo muestre. Los criterios son las reglas con las que decides si algo salió bien, y deben conocerse antes de evaluar.",
        f"Veamos un ejemplo. {REG_TXT} Los tres resultados son: audición {REG[0][1]} de 5, interpretación {REG[1][1]} de 5 y creación {REG[2][1]} de 5. La fortaleza más clara de Camila es la creación, porque tiene el puntaje más alto. Puede decir: «mi fortaleza es la creación porque mi pieza cumplió 5 de 5 criterios».",
        "Puedes reflexionar sobre tres áreas: la audición (escuchar), la interpretación (cantar o tocar) y la creación (inventar). Revisa cada una con su evidencia y escribe una frase con «porque». Reflexionar no es compararte con otras personas, sino mirar tu propio avance. Todas las personas tienen fortalezas, aunque no se noten a primera vista.",
    ],
    [("fortaleza", "algo que haces bien"), ("evidencia", "dato de tus registros que lo muestra"), ("criterio", "regla para decidir si algo salió bien"), ("audición", "escuchar música con atención"), ("interpretación", "cantar o tocar música")],
    [
        ("Elegir con evidencia", f"{REG_TXT} ¿Cuál es la fortaleza más clara de Camila?", ["Audición 4, interpretación 3, creación 5.", "El mayor puntaje es 5."], "La creación, con 5 de 5"),
        ("Escribir la frase", "Camila quiere decir su fortaleza con evidencia. ¿Qué frase sirve: (a) «Soy buena en todo» o (b) «Mi fortaleza es la creación porque mi pieza cumplió 5 de 5 criterios»?", ["La (a) no tiene dato.", "La (b) tiene la fortaleza y el dato."], "(b)"),
    ],
    [
        ("Decir una fortaleza sin ningún dato.", "No se puede comprobar.", "Agrega un dato de tus registros."),
        ("Compararte con otros para decidir tu fortaleza.", "La reflexión mira tu propio avance.", "Usa tu registro y tus criterios."),
    ],
    [
        ex(f"{REG_TXT} ¿Cuántos criterios cumplió la pieza de Camila?", "5", "El registro dice 5 de 5."),
        ex(f"{REG_TXT} ¿En qué ensayos mantuvo el pulso parejo: en 3 de 5 o en 5 de 5?", "En 3 de 5", "Así lo dice el registro."),
        ex("¿Una fortaleza es algo que haces bien o algo que te cuesta?", "Algo que haces bien", "Esa es su definición."),
    ],
    [
        ex(f"{REG_TXT} ¿Cuál es el puntaje de Camila en audición?", "4 de 5", "Describió bien 4 de 5 sonidos."),
        ex(f"{REG_TXT} Ordena de mayor a menor puntaje: audición, interpretación y creación.", "Creación, audición, interpretación", "5, 4 y 3."),
        ex("¿Qué necesitas para identificar una fortaleza: evidencia o solo una opinión?", "Evidencia", "El dato respalda la fortaleza."),
    ],
    [
        arith(f"{REG_TXT} ¿Cuántos puntos hay de diferencia entre la creación y la interpretación?", "5-3", "Se restan los puntajes.", " puntos"),
        arith(f"{REG_TXT} ¿Cuántos puntos suma Camila en las tres áreas?", "4+3+5", "Se suman los tres puntajes.", " puntos"),
        ex("Un niño tiene 4 de 5 en audición y 4 de 5 en creación. ¿Cuál es su fortaleza más clara?", "Ninguna sola: tiene dos con igual puntaje", "Con puntajes iguales las dos áreas son fortalezas."),
    ],
    [
        ex("Luis dice «soy el mejor del curso en música». ¿Por qué no sirve como fortaleza con evidencia?", "Porque se compara con otros y no da datos", "La reflexión usa evidencia propia, no comparación con otros."),
        ex(f"{REG_TXT} Camila dice que su fortaleza es la interpretación porque lo siente así. ¿Qué dato lo contradice?", "El 3 de 5 en interpretación es su puntaje más bajo", "La evidencia no respalda esa fortaleza."),
    ],
    [
        ex("Alguien dice «mi fortaleza es la audición» y no muestra ningún registro. ¿Qué le falta a su afirmación?", "Evidencia: un dato de sus registros", "Una fortaleza se respalda con un dato."),
        arith("Un registro tiene 5 ensayos y 4 salieron con el pulso parejo. ¿Cuántos no?", "5-4", "Se restan los ensayos logrados del total.", " ensayo"),
    ],
    [ex("Un niño toca la caja con pulso parejo en 5 de 5 ensayos de una semana. ¿Qué fortaleza puede decir y cuál es su evidencia?", "Su pulso parejo; 5 de 5 ensayos", "El registro lo respalda.")],
    [ex("¿Qué es una fortaleza?", "Algo que haces bien", "Se muestra con evidencia."), ex("En Música: ¿Qué es la evidencia?", "Un dato de tus registros", "Respalda lo que dices."), ex("¿Compararte con otros te sirve para esta reflexión?", "No", "Se mira el avance propio.")],
    (
        "Revisa tus registros de la audición, la interpretación y la creación (o usa el registro de Camila si prefieres no compartir los tuyos). Escribe un dato de cada área, decide cuál es tu fortaleza más clara y escribe una frase con «porque» que use ese dato. Hazlo con honestidad: no se evalúan la personalidad ni el talento.",
        "Audición: describí bien 4 de 5 sonidos. Interpretación: pulso parejo en 3 de 5 ensayos. Creación: 5 de 5 criterios. Mi fortaleza es la creación porque mi pieza cumplió 5 de 5 criterios.",
        ["anota un dato de cada área", "elige la fortaleza con evidencia", "escribe la frase con «porque»"],
        ["registro escrito", "frase final"],
        ["decir una fortaleza sin dato", "compararse con otras personas"],
        "Reconoce el dato y pregunta qué hizo para lograrlo; respeta que elija usar el caso inventado.",
    ),
    "Escribe una cosa que hiciste bien en música esta semana y un dato que lo muestre.",
    "Pide a una persona de tu casa que te diga qué ve que haces bien al cantar o tocar.",
)

# ---------------------------------------------------------------- OA 08 · clase 2
ENSAYO = [("pulso parejo", 5), ("afinación al cantar", 3), ("entrada juntos", 2), ("volumen seguro", 4)]
ENS_TXT = " ".join(f"{c}: {n} de 5." for c, n in ENSAYO)

L(
    OA8, 2,
    f"Lápiz y papel. Registro de ensayo de ejemplo (caso inventado) de un grupo en cuatro criterios, cada uno sobre 5 intentos: {ENS_TXT}",
    "Aprenderé a localizar un área de mejora: la parte concreta de mi audición, interpretación o creación que puedo mejorar, con evidencia. Sirve para saber en qué enfocar mi práctica.",
    ["Sé identificar una fortaleza con evidencia.", "Sé leer un registro de ensayo.", "Sé comparar puntajes."],
    [
        "Un área de mejora es algo que todavía puedo hacer mejor. No es un defecto ni una falta: es una oportunidad de aprender. Para localizarla necesito evidencia, igual que para la fortaleza. Mi registro me muestra en qué criterio salieron menos intentos bien. Localizar es decir con precisión dónde está la dificultad.",
        f"Veamos el registro. {ENS_TXT} El pulso parejo salió 5 de 5, así que es una fortaleza. La entrada juntos salió solo 2 de 5, el puntaje más bajo, así que es el área de mejora principal. La afinación (3 de 5) y el volumen (4 de 5) también pueden mejorar, pero menos.",
        "Para decir un área de mejora usa palabras precisas y amables: no «soy malo en esto» sino «necesito mejorar la entrada juntos porque solo salió 2 de 5 veces». Elige una sola área para enfocarte primero, la que tenga el puntaje más bajo o la que más afecte a la música. Mejorar es un proceso, y todos lo hacemos.",
    ],
    [("área de mejora", "algo que todavía puedo hacer mejor"), ("localizar", "decir con precisión dónde está algo"), ("criterio", "regla para decidir si algo salió bien"), ("registro de ensayo", "lista de intentos y resultados por criterio"), ("proceso", "camino de varias etapas para lograr algo")],
    [
        ("Localizar el área", f"Registro: {ENS_TXT} ¿Cuál es el área de mejora principal?", ["Pulso 5, afinación 3, entrada 2, volumen 4.", "El menor es 2."], "La entrada juntos, con 2 de 5"),
        ("Decirlo con precisión", "Elige la frase precisa y amable: (a) «Soy malo en esto» o (b) «Necesito mejorar la entrada juntos porque solo salió 2 de 5 veces».", ["La (a) no dice el criterio ni el dato.", "La (b) dice dónde y por qué."], "(b)"),
    ],
    [
        ("Pensar que un área de mejora es un defecto de la persona.", "Es una oportunidad de aprender.", "Habla del criterio y del dato, no de ti como persona."),
        ("Elegir muchas áreas a la vez.", "Es difícil mejorar todo junto.", "Elige una sola para enfocarte primero."),
    ],
    [
        ex(f"Registro: {ENS_TXT} ¿Cuántos intentos de 5 salieron bien en la afinación?", "3", "El registro dice 3 de 5."),
        ex(f"Registro: {ENS_TXT} ¿Qué criterio salió 5 de 5?", "El pulso parejo", "Es la fortaleza del grupo."),
        ex("¿Un área de mejora es una oportunidad de aprender o una falta?", "Una oportunidad de aprender", "No es un defecto."),
    ],
    [
        ex(f"Registro: {ENS_TXT} Ordena los criterios de menor a mayor puntaje.", "Entrada juntos, afinación, volumen, pulso", "2, 3, 4 y 5."),
        ex(f"Registro: {ENS_TXT} ¿Cuál criterio sigue a la entrada juntos en necesidad de mejora?", "La afinación", "Tiene 3 de 5, el segundo puntaje más bajo."),
        ex(f"Registro: {ENS_TXT} ¿Por qué el volumen seguro con 4 de 5 no es el área principal?", "Porque tiene un puntaje más alto que la entrada y la afinación", "Hay criterios con menos intentos logrados."),
    ],
    [
        arith(f"Registro: {ENS_TXT} ¿Cuántos intentos no salieron bien en la entrada juntos?", "5-2", "Se restan los logrados del total.", " intentos"),
        arith(f"Registro: {ENS_TXT} ¿Cuántos intentos salieron bien en total sumando los cuatro criterios?", "5+3+2+4", "Se suman los puntajes de los cuatro criterios.", " intentos"),
        arith(f"Registro: {ENS_TXT} ¿Cuántos puntos hay de diferencia entre el criterio más alto y el más bajo?", "5-2", "Se restan los puntajes extremos.", " puntos"),
    ],
    [
        ex("Ana dice «la entrada juntos es mi culpa». ¿La entrada juntos depende solo de ella?", "No; depende de todo el grupo", "Entrar juntos es un criterio del grupo y se mejora con práctica."),
        ex("Un grupo elige mejorar tres áreas a la vez. ¿Qué dificultad tiene?", "Es difícil mejorar todo junto", "Conviene enfocarse primero en una área."),
    ],
    [
        ex("Un grupo tiene afinación 3 de 5 y entrada juntos 3 de 5. ¿Alcanzan los puntajes para elegir cuál mejorar primero?", "No; están empatados y hay que usar otro criterio", "Con puntajes iguales se decide según cuál afecta más a la música."),
        arith("Un criterio tiene 2 intentos logrados de 5. La meta es llegar a 4 de 5. ¿Cuántos intentos logrados más necesita?", "4-2", "Se resta lo que tiene de la meta.", " intentos"),
    ],
    [ex("Una niña ve que en su creación el motivo no se reconocía en 2 de 3 repeticiones. ¿Cuál puede ser su área de mejora: (a) hacer el motivo más reconocible o (b) hacer la pieza más larga?", "(a)", "El dato apunta a la identidad del motivo.")],
    [ex("¿Qué es un área de mejora?", "Algo que todavía puedo hacer mejor", "Es una oportunidad."), ex("¿Cuántas áreas conviene elegir primero?", "Una", "Así te enfocas."), ex("¿Con qué se localiza el área de mejora?", "Con evidencia del registro", "Los datos muestran dónde está.")],
    (
        "Revisa un registro de ensayo (el tuyo o el de ejemplo). Anota los criterios con su puntaje de 5. Localiza el área de mejora con el puntaje más bajo y escribe una frase precisa y amable: «Necesito mejorar… porque salió… de 5 veces». Si no quieres compartir tu registro, usa el de ejemplo. No se evalúan personalidad ni talento.",
        "Registro: pulso 5, afinación 3, entrada juntos 2, volumen 4. Necesito mejorar la entrada juntos porque salió solo 2 de 5 veces.",
        ["anota los criterios con puntajes", "elige el área con el puntaje más bajo", "escribe una frase precisa y amable"],
        ["registro escrito", "frase final"],
        ["decir «soy malo»", "elegir muchas áreas a la vez"],
        "Reconoce la precisión del criterio y el dato; si usa expresiones negativas sobre sí, ayuda a reformularlas hacia el criterio.",
    ),
    "Escribe un criterio de tu música que quieras mejorar y el dato que lo muestra.",
    "Pide a una persona de tu casa que escuche tu práctica y diga una cosa concreta que podrías mejorar.",
)

# ---------------------------------------------------------------- OA 08 · clase 3
ESTR = (
    "Problema 1: en una sección se cometen errores. Estrategia: ensayar solo esa sección, por partes. "
    "Problema 2: se pierde el pulso. Estrategia: tocar más lento y marcar el pulso con un pie. "
    "Problema 3: no entran juntos. Estrategia: acordar una señal, como una cuenta de 4 pulsos. "
    "Problema 4: se cansa la voz. Estrategia: ensayar poco rato y descansar, tomando agua."
)

L(
    OA8, 3,
    f"Lápiz y papel. Estrategias de la clase (cada problema con su estrategia): {ESTR}",
    "Aprenderé a elegir una estrategia de práctica que responda a mi área de mejora y a planificarla. Sirve para practicar con un plan y no solo repetir sin pensar.",
    ["Sé localizar un área de mejora.", "Sé ensayar por secciones.", "Sé usar una meta medible."],
    [
        "Una estrategia de práctica es una forma planificada de practicar para mejorar algo. No cualquier estrategia sirve para cualquier problema: debe responder al área de mejora. Si el problema es la entrada, la estrategia es una señal; si el problema es el pulso, la estrategia es tocar más lento. Elegir bien ahorra tiempo.",
        f"Veamos estrategias. {ESTR} Después de elegir la estrategia, se arma un plan con tres datos: cuánto tiempo practicas cada vez, cuántas veces a la semana y qué meta mides. Por ejemplo: «10 minutos, 3 veces a la semana, hasta lograr 4 de 5 entradas juntos».",
        "Un buen plan es pequeño y posible. Practicar poco rato muchas veces rinde más que practicar mucho una sola vez. También cuida tu voz y tu cuerpo: descansa y no fuerces. Al final de cada práctica anota un dato, como cuántos intentos salieron bien. Esa evidencia te servirá en la próxima clase para comprobar tu progreso.",
    ],
    [("estrategia", "forma planificada de practicar"), ("plan", "lista de qué, cuánto y cuándo practicarás"), ("meta", "lo que quieres lograr, con un número"), ("respuesta al problema", "que la estrategia sirve para ese problema"), ("descansar", "parar un rato para no cansarte")],
    [
        ("Elegir según el problema", f"{ESTR} Un grupo no entra junto a la música. ¿Qué estrategia elige?", ["Es el problema 3.", "La estrategia es acordar una señal."], "Acordar una señal, como una cuenta de 4 pulsos"),
        ("Calcular el plan", "Un plan dice 10 minutos de práctica, 3 veces a la semana. ¿Cuántos minutos son en una semana?", ["Cada vez son 10 minutos.", "Son 3 veces: 10 × 3."], "30 minutos"),
    ],
    [
        ("Elegir una estrategia que no tiene que ver con el problema.", "No resuelve la dificultad.", "Mira cuál problema tienes y elige la estrategia que le corresponde."),
        ("Practicar mucho rato sin descansar.", "Cansa la voz y el cuerpo.", "Practica poco y con pausas."),
    ],
    [
        ex(f"{ESTR} ¿Qué estrategia sirve cuando se pierde el pulso?", "Tocar más lento y marcar el pulso con un pie", "Está en el problema 2."),
        ex(f"{ESTR} ¿Qué estrategia sirve cuando se cansa la voz?", "Ensayar poco rato y descansar", "Está en el problema 4."),
        ex("¿Una estrategia de práctica es una forma planificada o una forma al azar de practicar?", "Planificada", "Se elige según el problema."),
    ],
    [
        ex(f"{ESTR} Una sección falla siempre. ¿Qué estrategia conviene: tocar toda la pieza muchas veces o ensayar solo esa sección?", "Ensayar solo esa sección", "Es el problema 1."),
        ex("Un plan dice «3 veces a la semana». ¿Qué dos datos faltan para que sea un plan completo?", "Cuánto tiempo cada vez y la meta", "Un plan lleva tiempo, frecuencia y meta."),
        ex("¿Qué conviene más: practicar 10 minutos tres veces o 30 minutos seguidos una vez?", "10 minutos tres veces", "Poco rato muchas veces rinde más."),
    ],
    [
        arith("Un plan dice 15 minutos de práctica, 4 veces a la semana. ¿Cuántos minutos son en una semana?", "15*4", "Se multiplica el tiempo por las veces.", " minutos"),
        arith("Un grupo practica 10 minutos 3 veces por semana durante 4 semanas. ¿Cuántos minutos practica?", "10*3*4", "Se multiplica el tiempo por las veces y por las semanas.", " minutos"),
        ex(f"{ESTR} Un niño elige «tocar más lento» para el problema de no entrar juntos. ¿Es una estrategia adecuada?", "No", "Para el problema 3 corresponde acordar una señal."),
    ],
    [
        ex("Ana quiere mejorar su pulso y propone gritar más fuerte al cantar. ¿Por qué no es una buena estrategia?", "No responde al problema y fuerza la voz", "El pulso se mejora tocando más lento y marcándolo."),
        ex("Un grupo practica tres veces con un plan y no anota nada. ¿Qué pierde?", "La evidencia para comprobar el progreso", "Sin datos no se sabe si mejoró."),
    ],
    [
        ex("Un plan dice «lograr entrar juntos 3 veces seguidas con la cuenta de 4 pulsos». ¿Cuál es la meta medible del plan?", "Entrar juntos 3 veces seguidas", "Lleva un número que se puede contar."),
        arith("Un grupo quiere practicar 60 minutos en total en una semana, en sesiones de 15 minutos. ¿Cuántas sesiones necesita?", "60//15", "Se divide el tiempo total por la duración de cada sesión.", " sesiones"),
    ],
    [ex("Un niño toca bien una melodía lenta pero la acelera y se equivoca. ¿Qué estrategia de la clase le conviene: tocar más lento y marcar el pulso o ensayar solo una sección?", "Tocar más lento y marcar el pulso", "Su problema es el pulso al acelerar.")],
    [ex("¿Qué es una estrategia de práctica?", "Una forma planificada de practicar", "Responde a un problema."), ex("¿Qué debe llevar una meta?", "Un número", "Así se puede comprobar."), ex("¿Qué haces al final de cada práctica?", "Anotar un dato", "Sirve de evidencia.")],
    (
        "Elige tu área de mejora (de la clase 2 o la del ejemplo). Elige una estrategia de la lista de la clase que responda a ese problema. Arma un plan con tres datos: cuánto tiempo practicas, cuántas veces a la semana y qué meta con número vas a medir. Calcula cuántos minutos practicarás en una semana. Practica sin forzar la voz ni el cuerpo.",
        "Área: entrada juntos. Estrategia: acordar una señal con una cuenta de 4 pulsos. Plan: 10 minutos, 3 veces a la semana, meta: entrar juntos 3 veces seguidas. En una semana practicaré 30 minutos.",
        ["la estrategia responde al área de mejora", "el plan tiene tiempo, frecuencia y meta con número", "calcula los minutos semanales"],
        ["plan escrito"],
        ["elegir una estrategia que no corresponde", "plan sin meta medible"],
        "Reconoce el plan y pregunta cómo sabrá si la estrategia funciona; si falta la meta, ayuda a ponerle un número.",
    ),
    "Elige una estrategia de la clase y di para qué problema sirve.",
    "Escribe un plan de 10 minutos, 2 veces a la semana, para mejorar una parte de tu música.",
)

# ---------------------------------------------------------------- OA 08 · clase 4
PROG = (
    "Registro de un grupo (caso inventado). Área de mejora: la entrada juntos. Meta: 4 de 5 intentos. "
    "Antes de la estrategia: 2 de 5. Después de 2 semanas de práctica: 4 de 5."
)

L(
    OA8, 4,
    f"Lápiz y papel. {PROG}",
    "Aprenderé a comprobar mi progreso comparando mi registro de antes y de después, y a decidir el siguiente paso. Sirve para saber si mi estrategia funcionó y qué hacer enseguida.",
    ["Sé localizar un área de mejora.", "Sé elegir una estrategia.", "Sé restar números pequeños."],
    [
        "El progreso es la diferencia entre cómo estabas antes y cómo estás ahora. Para comprobarlo comparas dos registros hechos con el mismo criterio. Si el número sube, hay progreso. Progresar no significa ser perfecto: significa avanzar desde donde estabas.",
        f"Veamos un ejemplo. {PROG} El progreso es 4 − 2 = 2 intentos más. La meta era 4 de 5 y la alcanzó, así que la estrategia funcionó. El siguiente paso puede ser mantener la práctica para no olvidar, o elegir una nueva área de mejora, como la afinación.",
        "Si la meta no se alcanza, el siguiente paso es ajustar el plan: practicar más veces, cambiar de estrategia o pedir ayuda. Si hay progreso pero no se llegó a la meta, se sigue con la misma estrategia. Cada vez que compruebas tu progreso, escribe una frase honesta: «mejoré de… a… y mi siguiente paso es…». Reconocer tu avance también es parte de reflexionar.",
    ],
    [("progreso", "diferencia entre cómo estabas antes y cómo estás ahora"), ("comparar", "mirar dos registros con el mismo criterio"), ("meta alcanzada", "se llegó al número propuesto"), ("siguiente paso", "lo que haces después de comprobar"), ("honesto", "que dice lo que realmente pasó")],
    [
        ("Calcular el progreso", f"{PROG} ¿Cuántos intentos más lograron después?", ["Antes: 2.", "Después: 4.", "4 − 2 = 2."], "2 intentos más"),
        ("Decidir el siguiente paso", f"{PROG} ¿Alcanzaron la meta? ¿Qué pueden hacer ahora?", ["La meta era 4 de 5.", "Llegaron a 4 de 5.", "Pueden mantener la práctica o elegir una nueva área."], "Sí; mantener la práctica o elegir otra área de mejora"),
    ],
    [
        ("Decir «no mejoré» cuando solo faltó llegar a la meta.", "Hubo progreso aunque no se alcanzó.", "Compara antes y después; el número que subió es progreso."),
        ("Cambiar de área sin comprobar si la estrategia funcionó.", "No sabes si resolviste el problema.", "Compara los registros antes de decidir."),
    ],
    [
        ex(f"{PROG} ¿Cuál era la meta?", "4 de 5 intentos", "El registro lo indica."),
        ex(f"{PROG} ¿Cuántos intentos salieron bien antes de la estrategia?", "2", "El registro dice 2 de 5."),
        ex("¿Progreso es ser perfecto o avanzar desde donde estabas?", "Avanzar desde donde estabas", "Es la diferencia entre antes y después."),
    ],
    [
        ex(f"{PROG} ¿Alcanzaron la meta?", "Sí", "Llegaron a 4 de 5, que era la meta."),
        ex("Un grupo tenía 2 de 5 y ahora tiene 3 de 5. ¿Hubo progreso?", "Sí", "El número subió de 2 a 3."),
        ex("Un grupo tenía 3 de 5 y sigue con 3 de 5 después de la estrategia. ¿Hubo progreso?", "No", "No hubo diferencia entre antes y después."),
    ],
    [
        arith("Un grupo pasó de 2 de 5 a 4 de 5 entradas juntos. ¿Cuántos intentos más logra?", "4-2", "Se restan los logrados antes de los logrados después.", " intentos"),
        arith("Un grupo pasó de 1 de 5 a 3 de 5, y su meta es 4 de 5. ¿Cuántos intentos le faltan para la meta?", "4-3", "Se resta lo que tiene de la meta.", " intento"),
        ex("Un grupo con meta 4 de 5 llega a 3 de 5, con progreso desde 1. ¿Qué siguiente paso conviene: seguir con la misma estrategia o cambiar de área?", "Seguir con la misma estrategia", "Hubo progreso pero aún no llegan a la meta."),
    ],
    [
        ex("Una niña dice «no mejoré» porque no llegó a la meta, pero pasó de 1 a 3 intentos. ¿Qué datos muestran su error?", "El aumento de 1 a 3 es progreso", "Hubo avance aunque falte llegar a la meta."),
        ex("Un grupo alcanzó su meta y dice: «ya no necesitamos practicar nunca más». ¿Qué problema tiene?", "Sin mantener la práctica puede olvidar lo logrado", "El progreso se mantiene practicando."),
    ],
    [
        ex("Un grupo mejoró de 2 a 4 y alcanzó su meta de 4. ¿Qué siguiente paso es coherente: (a) abandonar el criterio o (b) mantener la práctica y elegir una nueva área de mejora?", "(b)", "Con la meta alcanzada, se mantiene lo logrado y se avanza hacia algo nuevo."),
        arith("Un grupo tenía 1 de 5, luego 3 de 5 y después 5 de 5. ¿Cuántos intentos mejoró en total desde el inicio?", "5-1", "Se restan los logrados al inicio de los del final.", " intentos"),
    ],
    [arith("Una niña anotó que al principio acertaba 2 de 5 al reconocer cualidades del sonido y ahora acierta 4 de 5. ¿Cuántos aciertos más tiene?", "4-2", "Se restan los aciertos de antes de los de ahora.", " aciertos más")],
    [ex("¿Qué es el progreso?", "La diferencia entre antes y ahora", "Se comprueba con dos registros."), ex("Si mejoraste pero no llegaste a la meta, ¿qué haces según la clase?", "Sigues con la misma estrategia", "Hubo avance, así que conviene continuar y ajustar el plan."), ex("¿Con qué debes comparar tu registro de ahora?", "Con el de antes", "Con el mismo criterio.")],
    (
        "Compara dos registros tuyos (o los del ejemplo) del mismo criterio: uno de antes de la estrategia y otro de después. Escribe los dos números, calcula el progreso, di si alcanzaste la meta y escribe tu siguiente paso con una frase honesta: «Mejoré de… a… y mi siguiente paso es…». Si no quieres compartir tus registros, usa el caso inventado.",
        "Antes: 2 de 5. Después: 4 de 5. Progreso: 2 intentos más. La meta de 4 de 5 se alcanzó. Mejoré de 2 a 4 y mi siguiente paso es seguir practicando 10 minutos y elegir la afinación como nueva área.",
        ["compara dos registros del mismo criterio", "calcula el progreso", "escribe un siguiente paso coherente"],
        ["registros comparados", "frase final"],
        ["comparar criterios distintos", "ignorar el progreso si no llegó a la meta"],
        "Reconoce el cálculo y la honestidad; si no hubo progreso, ayuda a ajustar la estrategia sin juzgar.",
    ),
    "Escribe dos números, antes y después, que muestren un progreso tuyo en música.",
    "Cuéntale a una persona de tu casa qué mejoraste y qué harás ahora.",
)
