"""Student material for 8.º básico Música, OA 02 (describir analíticamente los elementos del lenguaje musical y los procedimientos compositivos evidentes y su relación con el propósito expresivo).

Todas las músicas de los ejercicios son esquemas, números de nota y descripciones inventados para esta clase; las audiciones reales las selecciona y pone el docente.
"""
from __future__ import annotations

from student_content_mu8_a import L
from student_lessons import arith, ex

OA2 = "MU08 OA 02"

NOTAS = "1 = do, 2 = re, 3 = mi, 4 = fa, 5 = sol, 6 = la, 7 = si, 8 = do agudo"
LEY = ("semicorchea = 1 unidad; corchea = 2; negra = 4 (un pulso en 4/4 y 3/4); negra con puntillo = 6; blanca = 8; "
       "blanca con puntillo = 12; redonda = 16; cada silencio dura lo mismo que su figura")
ACORDES = "I = do-mi-sol; IV = fa-la-do; V = sol-si-re"

# ---------------------------------------------------------------- OA 02 · clase 1 (compás de 6/8 y síncopa)
L(
    OA2, 1,
    f"Lápiz y papel. Leyenda de duraciones de la clase: {LEY}. Todos los patrones están escritos en los ejercicios. Si quieres, palmea cada patrón a volumen bajo.",
    "Aprenderé a medir el compás de 6/8 y a reconocer la síncopa, dos rasgos del ritmo. Sirve para describir con exactitud cómo está organizado un ritmo y qué efecto produce.",
    ["Sé que un compás agrupa pulsos y que 4/4 tiene 16 unidades.", "Sé sumar la duración de las figuras con la leyenda.", "Sé que el puntillo suma la mitad de la figura."],
    [
        "Un compás de 6/8 tiene seis corcheas, o sea 6 × 2 = 12 unidades. Parece igual a un compás de 3/4, que también tiene 12 unidades, pero se agrupa distinto. El 3/4 se siente en tres pulsos de dos corcheas. El 6/8 se siente en dos pulsos grandes de tres corcheas cada uno, y cada pulso grande equivale a una negra con puntillo, que dura 6 unidades.",
        "La síncopa ocurre cuando una nota empieza entre dos pulsos y sigue sonando cuando llega el pulso siguiente. Así, el acento parece correrse. Si en un compás de 4/4 los pulsos caen en las unidades 0, 4, 8 y 12, una nota que empieza en la unidad 2 y dura 4 unidades llega hasta la 6 y pasa sobre el pulso de la unidad 4: es una síncopa. Una nota que empieza justo en un pulso, o que termina antes del pulso siguiente, no es síncopa.",
        "Para describir un ritmo se suman las unidades de cada figura, silencios incluidos, y se compara con las del compás. También se revisa dónde empieza cada nota y si cruza un pulso. El ritmo se relaciona con el propósito: el 6/8 da una sensación de balanceo, y la síncopa da impulso y sorpresa, porque la nota parece adelantarse al pulso.",
    ],
    [("6/8", "compás de seis corcheas, con dos pulsos grandes de tres corcheas"), ("pulso grande", "grupo de tres corcheas en 6/8; equivale a una negra con puntillo"), ("síncopa", "nota que empieza entre dos pulsos y sigue sonando sobre el pulso siguiente"), ("unidad", "duración de una semicorchea, que sirve para medir el ritmo"), ("puntillo", "punto que suma a una figura la mitad de su duración")],
    [
        ("Llenar un compás de 6/8", "En un compás de 6/8 hay una negra con puntillo, una corchea, una corchea y una corchea. ¿Llena el compás?", ["Suma: 6 + 2 + 2 + 2 = 12 unidades.", "El 6/8 tiene 6 × 2 = 12 unidades."], "Sí, lo llena justo"),
        ("Detectar una síncopa", "En un compás de 4/4 (pulsos en las unidades 0, 4, 8 y 12), una nota empieza en la unidad 6 y dura 4 unidades. ¿Es síncopa?", ["Empieza en 6, entre los pulsos 4 y 8.", "Dura hasta la unidad 10 y pasa sobre el pulso de la unidad 8."], "Sí, es síncopa"),
    ],
    [
        ("Pensar que 6/8 y 3/4 son el mismo ritmo porque suman igual.", "Suman 12 unidades los dos, pero 3/4 se agrupa de a dos corcheas y 6/8 de a tres.", "Fíjate en cómo se agrupan las corcheas, no solo en la suma."),
        ("Creer que la síncopa es un silencio.", "La síncopa es una nota que cruza un pulso; el silencio no suena.", "Revisa si una nota empieza entre pulsos y llega al pulso siguiente."),
    ],
    [
        ex("¿Cuántas corcheas tiene un compás de 6/8?", "6", "El número de arriba indica cuántas corcheas hay en el compás."),
        ex("Según la leyenda de la clase, ¿cuántas unidades dura una negra con puntillo?", "6", "La negra dura 4 y el puntillo suma la mitad, 2."),
        ex("Una nota empieza justo sobre un pulso y termina antes del pulso siguiente. ¿Es síncopa? Responde sí o no.", "No", "No empieza entre pulsos ni cruza el pulso siguiente."),
    ],
    [
        arith("¿Cuántas unidades tiene un compás de 6/8?", "6*2", "Son seis corcheas de 2 unidades cada una.", " unidades"),
        ex("¿En cuántos pulsos grandes se siente un compás de 6/8 y de cuántas corcheas es cada uno?", "En 2 pulsos de 3 corcheas", "Seis corcheas se agrupan de a tres."),
        ex("Un compás de 3/4 y uno de 6/8 duran lo mismo. ¿Qué cambia entre ellos? A) Cómo se agrupan las corcheas. B) Cuántas unidades tienen.", "A", "Los dos suman 12 unidades; el 3/4 agrupa de a dos y el 6/8 de a tres."),
    ],
    [
        ex("Un compás de 6/8 tiene una negra con puntillo y dos corcheas. ¿Qué figura le falta para llenarlo?", "Una corchea", "6 + 2 + 2 = 10 y faltan 2 unidades, que es una corchea."),
        arith("Una pieza en 6/8 dura 96 unidades. ¿Cuántos compases completos tiene?", "96//12", "Cada compás de 6/8 tiene 12 unidades.", " compases"),
        ex("En 4/4 (pulsos en las unidades 0, 4, 8 y 12), una nota empieza en la unidad 2 y dura 6 unidades. ¿Hay síncopa? Responde sí o no.", "Sí", "Empieza entre pulsos y llega a la unidad 8, pasando sobre el pulso de la unidad 4."),
    ],
    [
        ex("En 4/4 (pulsos en las unidades 0, 4, 8 y 12) suena una corchea y luego una negra, una corchea y una blanca. La negra empieza en la unidad 2 y termina en la 6. ¿Hay síncopa en la negra? Responde sí o no.", "Sí", "Empieza entre pulsos y pasa sobre el pulso de la unidad 4."),
        ex("Clara dice que un compás de 6/8 dura lo mismo que uno de 3/4. ¿Tiene razón? Responde sí o no.", "Sí", "Los dos suman 12 unidades."),
    ],
    [
        arith("Un compás de 6/8 lleva una negra, una corchea y una negra con puntillo. ¿Cuántas unidades suma?", "4+2+6", "Se suman las unidades de cada figura; coincide con las 12 del compás.", " unidades"),
        arith("¿Cuántas corcheas hay en 4 compases de 6/8?", "6*4", "Cada compás tiene seis corcheas.", " corcheas"),
    ],
    [arith("En una pieza de baile en 6/8 de 30 compases, una bailarina cuenta dos pulsos grandes por compás. ¿Cuántos pulsos grandes cuenta en toda la pieza?", "2*30", "Se multiplican los pulsos grandes por compás por los compases.", " pulsos grandes")],
    [ex("¿Cuántas unidades dura una corchea?", "2", "Es la mitad de una negra de 4 unidades."), ex("¿Cuántos pulsos grandes tiene un compás de 6/8?", "2", "Son dos grupos de tres corcheas."), ex("¿Qué hace que una nota sea síncopa?", "Empieza entre pulsos y cruza el pulso siguiente", "Eso la hace parecer un adelanto del pulso.")],
    (
        f"Con la leyenda ({LEY}), escribe dos compases. Uno de 6/8 que sume 12 unidades y uno de 4/4 que sume 16 e incluya una síncopa. Debajo de cada compás escribe la suma de unidades. En el de 4/4, indica en qué unidad empieza la nota sincopada y hasta cuál llega, sabiendo que los pulsos caen en las unidades 0, 4, 8 y 12.",
        "6/8: negra con puntillo, corchea, corchea, corchea = 6 + 2 + 2 + 2 = 12. 4/4: corchea, negra, corchea, blanca = 2 + 4 + 2 + 8 = 16, con la negra empezando en la unidad 2 y llegando a la 6, donde cruza el pulso de la unidad 4.",
        ["cada compás suma lo que debe", "la síncopa empieza entre pulsos y cruza un pulso", "muestra las sumas"],
        ["dos compases escritos", "sumas de unidades", "unidad de inicio y término de la síncopa"],
        ["no contar los silencios", "poner una nota que empieza en un pulso y llamarla síncopa"],
        "Reconoce las sumas y pide verificar, en la nota sincopada, en qué unidad empieza y qué pulso cruza.",
    ),
    "Escribe cuántas unidades tiene un compás de 6/8 y un compás de 3/4, y compara los números.",
    "Escribe un compás de 6/8 que no use negra con puntillo y compruébalo con la suma.",
)

# ---------------------------------------------------------------- OA 02 · clase 2 (melodía, intervalos y armonía)
L(
    OA2, 2,
    f"Lápiz y papel. Escala de números: {NOTAS}. Acordes de do mayor: {ACORDES}. Semitonos entre notas vecinas: do–re 2, re–mi 2, mi–fa 1, fa–sol 2, sol–la 2, la–si 2, si–do 1. Todo está escrito en los ejercicios.",
    "Aprenderé a describir la melodía por su contorno y sus intervalos, y la armonía por sus acordes. Sirve para explicar cómo se construye una música y qué sensación de tensión o reposo produce.",
    ["Sé leer una melodía escrita con números.", "Sé que una melodía puede subir, bajar o repetirse.", "Sé sumar y restar números pequeños."],
    [
        f"La melodía es una sucesión de notas con ritmo. Su contorno es la forma que dibuja: sube, baja o se mantiene. Un intervalo es la distancia entre dos notas, y se cuenta en grados incluyendo ambas notas ({NOTAS}). De 1 a 3 hay 3 − 1 + 1 = 3 grados, una tercera. De 1 a 5 hay una quinta. También se puede medir en semitonos, la distancia más pequeña entre notas vecinas.",
        f"La armonía son las notas que suenan a la vez. Un acorde se forma con tres notas apiladas de tres en tres. En do mayor, los acordes principales son {ACORDES}. Si las dos terceras suman 4 y 3 semitonos, el acorde es mayor; si suman 3 y 4, es menor. El acorde de V crea tensión y deja la frase en suspenso, mientras que el I da sensación de llegada y reposo.",
        "Para armonizar una melodía se mira qué notas suenan en cada compás y se elige el acorde que las contiene. Si el compás tiene fa y la, el acorde IV las incluye a ambas. Describir bien significa nombrar el contorno, los intervalos y los acordes con datos concretos, y relacionarlos con la sensación: una frase que termina en V queda en suspenso y una que termina en I se siente cerrada.",
    ],
    [("contorno", "forma que dibuja una melodía: sube, baja o se mantiene"), ("intervalo", "distancia entre dos notas, contada en grados con ambas notas"), ("semitono", "distancia más pequeña entre dos notas vecinas"), ("acorde", "tres notas apiladas que suenan a la vez"), ("reposo y tensión", "sensación de llegada (acorde I) y de suspenso (acorde V)")],
    [
        ("Medir un intervalo", f"¿Qué intervalo hay de la nota 2 a la nota 6? Escala: {NOTAS}.", ["Se cuenta con ambas notas: 6 − 2 + 1.", "Da 5 grados."], "Una quinta (5 grados)"),
        ("Elegir un acorde", f"Un compás de la melodía tiene las notas fa y la. Acordes: {ACORDES}. ¿Qué acorde las contiene?", ["El I tiene do, mi y sol: no tiene fa ni la.", "El IV tiene fa, la y do."], "El IV"),
    ],
    [
        ("Contar los grados sin incluir la nota de partida.", "El intervalo se cuenta con ambas notas: de 1 a 3 son tres grados, no dos.", "Resta y suma uno al final."),
        ("Creer que un acorde mayor y uno menor tienen las mismas distancias.", "El mayor suma 4 y 3 semitonos y el menor 3 y 4.", "Cuenta los semitonos de cada tercera."),
    ],
    [
        ex("Tres notas apiladas que suenan a la vez, ¿son una melodía o un acorde?", "Un acorde", "Un acorde reúne tres notas que suenan juntas."),
        ex("La melodía 1-2-3-4, ¿sube o baja?", "Sube", "Cada nota es mayor que la anterior."),
        ex(f"¿Qué acorde está formado por fa, la y do? Acordes: {ACORDES}.", "El IV", "Es el acorde que reúne esas tres notas."),
    ],
    [
        arith("¿Cuántos grados hay del 1 al 5, contando ambas notas?", "5-1+1", "Se cuentan las dos notas del intervalo.", " grados"),
        ex(f"¿Qué acorde contiene la nota mi? Acordes: {ACORDES}.", "El I", "Solo el I (do-mi-sol) tiene mi."),
        ex("Un acorde tiene terceras de 4 y 3 semitonos, en ese orden. ¿Es mayor o menor?", "Mayor", "El acorde mayor suma 4 y luego 3 semitonos."),
    ],
    [
        arith("¿Cuántos semitonos hay de do a mi? Suma do–re 2 y re–mi 2.", "2+2", "Se suman los semitonos de las dos distancias vecinas.", " semitonos"),
        ex("Las notas do, mi y sol suenan juntas. ¿Qué acorde forman: I, IV o V?", "I", "Es el acorde do-mi-sol."),
        arith("¿Cuántos grados hay de la nota 3 a la nota 8, contando ambas?", "8-3+1", "Se cuentan las dos notas del intervalo.", " grados"),
    ],
    [
        ex(f"Un compás de una melodía es re-si-re-si. ¿Qué acorde lo acompaña mejor? Acordes: {ACORDES}.", "El V", "Re y si solo están juntos en el V."),
        ex("El acorde la-do-mi tiene la–do de 3 semitonos y do–mi de 4. ¿Es mayor o menor?", "Menor", "El acorde menor suma 3 y luego 4 semitonos."),
    ],
    [
        arith("¿Cuántos semitonos hay de do a sol? Suma do–re 2, re–mi 2, mi–fa 1 y fa–sol 2.", "2+2+1+2", "Se suman todos los semitonos entre las notas vecinas.", " semitonos"),
        ex("Una frase termina en el acorde V. ¿Se siente de reposo o queda en suspenso?", "En suspenso", "El V crea tensión y pide un acorde de llegada."),
    ],
    [ex("Quieres armonizar dos compases: el primero tiene fa, la y do; el segundo tiene sol, si y re. ¿Qué dos acordes eliges, en ese orden?", "IV y luego V", "El primer compás calza con el IV y el segundo con el V.")],
    [ex("¿Qué es un intervalo?", "La distancia entre dos notas", "Se cuenta en grados con ambas notas."), ex("¿Cuántas notas tiene un acorde de los de la clase?", "3", "Son tres notas apiladas."), ex("¿Qué acorde da sensación de reposo al terminar una frase?", "El I", "Es el acorde de llegada.")],
    (
        f"Con la escala ({NOTAS}) y los acordes ({ACORDES}), analiza esta melodía de ejemplo de dos compases: compás 1: 4-6-4-6; compás 2: 5-7-5-2. Escribe 1) el contorno de cada compás, 2) el intervalo en grados entre la primera y la segunda nota del compás 1, 3) un acorde para cada compás, 4) cuál de los dos acordes deja la frase en suspenso y qué acorde de la lista daría reposo al final.",
        "Compás 1: sube y baja (4-6-4-6); intervalo de 4 a 6 = 3 grados (tercera); acorde IV. Compás 2: 5-7-5-2, sube, baja y baja más; acorde V. El V deja la frase en suspenso; el I daría el reposo.",
        ["describe el contorno con datos", "calcula bien el intervalo en grados", "elige los acordes que contienen las notas"],
        ["análisis escrito", "acordes elegidos"],
        ["contar los grados sin la nota de partida", "elegir un acorde que no contiene las notas del compás"],
        "Reconoce el análisis y pide comprobar, nota por nota, que cada una está en el acorde elegido.",
    ),
    "Tararea 1-2-3-4-5 y 5-4-3-2-1 y di cuál sube y cuál baja.",
    "Inventa un compás de cuatro notas que pertenezca al acorde I y escríbelo con números.",
)

# ---------------------------------------------------------------- OA 02 · clase 3 (timbre, textura y forma)
L(
    OA2, 3,
    "Lápiz y papel. Las músicas están descritas con palabras o con letras de forma en los ejercicios (son de ejemplo). Si quieres, marca con palmas cada sección de una canción que conozcas.",
    "Aprenderé a describir el timbre, la textura (monofónica, homofónica y polifónica) y la forma (AB, ABA, rondó y estrofa-estribillo). Sirve para explicar cómo está organizada una música y qué roles tienen las voces e instrumentos.",
    ["Sé que el timbre es el color propio de cada instrumento o voz.", "Sé que una melodía es una sucesión de notas.", "Sé contar secciones y compases."],
    [
        "El timbre es el color propio de cada voz o instrumento. Los instrumentos se agrupan en familias: cuerdas, vientos, percusión y voces. Dos instrumentos pueden tocar las mismas notas y sonar distinto, porque su timbre es otro. La textura es la manera en que se combinan las líneas musicales. En la textura monofónica suena una sola melodía, aunque la toquen muchas personas a la vez.",
        "En la textura homofónica hay una melodía principal y un acompañamiento de acordes que la sostiene. En la polifónica suenan a la vez dos o más melodías con vida propia, como en un canon. La forma es el orden de las secciones. Cada sección distinta se nombra con una letra: A, B, C. En una forma ABA, la sección A vuelve al final. En el rondó, A vuelve entre secciones nuevas: ABACA. En una canción, las estrofas cambian y el estribillo regresa. A veces aparece un puente, una parte distinta que une dos secciones.",
        "Para describir una música se nombra el timbre, la textura y la forma con datos concretos. Por ejemplo: «una voz y una guitarra, textura homofónica, en forma ABA con A de 8 compases». También se calcula: si cada sección dura lo mismo, el total es el número de secciones por los compases de cada una. Describir con estos nombres permite comparar músicas y explicar por qué una se siente más sencilla, más llena o más variada.",
    ],
    [("timbre", "color propio de cada voz o instrumento"), ("textura monofónica, homofónica y polifónica", "una melodía sola; melodía con acordes de acompañamiento; varias melodías a la vez"), ("forma", "orden de las secciones de una pieza"), ("rondó", "forma en que A vuelve entre secciones nuevas: ABACA"), ("estribillo", "parte de una canción que regresa igual entre las estrofas")],
    [
        ("Reconocer la textura", "Una flauta toca una melodía y una guitarra toca acordes que la acompañan. ¿Qué textura hay?", ["Hay una melodía principal.", "La guitarra la sostiene con acordes."], "Homofónica"),
        ("Calcular la forma", "Una pieza en forma ABA tiene A de 8 compases y B de 12 compases. ¿Cuántos compases tiene la pieza?", ["La A aparece dos veces.", "8 + 12 + 8 = 28."], "28 compases"),
    ],
    [
        ("Pensar que, si muchas personas cantan, la textura es polifónica.", "Si todas cantan la misma melodía, la textura es monofónica; la polifonía necesita líneas distintas.", "Cuenta cuántas melodías distintas suenan, no cuántas personas."),
        ("Creer que la forma ABA tiene tres secciones distintas.", "Tiene tres secciones, pero solo dos son distintas porque la A se repite.", "Cuenta las letras diferentes."),
    ],
    [
        ex("Suena una sola melodía, sin acompañamiento. ¿Qué textura hay?", "Monofónica", "Hay una sola línea musical."),
        ex("En la forma ABA, ¿cuántas secciones distintas hay?", "2", "Las secciones distintas son A y B."),
        ex("Dos instrumentos tocan las mismas notas y suenan distinto. ¿Qué elemento los diferencia?", "El timbre", "El timbre es el color propio de cada instrumento."),
    ],
    [
        ex("Dos melodías distintas suenan a la vez, cada una con su propia línea. ¿Qué textura es? A) Polifónica. B) Homofónica.", "A", "En la polifonía las líneas son independientes."),
        ex("En un rondó ABACA, ¿cuántas veces suena la sección A?", "3", "La A abre, aparece en el medio y cierra."),
        ex("Cinco flautas tocan la misma melodía al mismo tiempo. ¿La textura es monofónica o polifónica?", "Monofónica", "Aunque sean cinco, es una sola melodía."),
    ],
    [
        arith("Una pieza en forma ABA tiene secciones de 8 compases cada una. ¿Cuántos compases tiene?", "8*3", "Son tres secciones del mismo largo.", " compases"),
        arith("Un rondó ABACA tiene cinco secciones de 4 compases. ¿Cuántos compases tiene?", "5*4", "Cada una de las cinco secciones tiene 4 compases.", " compases"),
        ex("Una voz canta la melodía y una guitarra marca acordes que la acompañan. ¿Qué textura describe esto y qué familia de instrumentos toca los acordes?", "Homofónica; cuerdas", "Hay melodía con acompañamiento de acordes, y la guitarra es de la familia de las cuerdas."),
    ],
    [
        ex("Una canción usa la misma música en las estrofas 1 y 2 (la llamamos A) y entre ellas suena un estribillo (B): estrofa 1, estribillo, estrofa 2, estribillo. ¿Qué forma de letras tiene: ABAB o ABCB?", "ABAB", "La música de la estrofa vuelve (A) y el estribillo vuelve (B), alternados."),
        ex("Una voz canta una melodía y otra entra después con la misma melodía, y ambas siguen sonando a la vez. ¿Qué textura aparece? A) Homofónica. B) Polifónica.", "B", "Dos líneas distintas en el tiempo suenan a la vez."),
    ],
    [
        arith("Una pieza ABA tiene A de 8 compases y B de 12 compases. Se repite completa 2 veces. ¿Cuántos compases suenan?", "(8+12+8)*2", "Se calcula una vuelta y se duplica.", " compases"),
        arith("Un rondó ABACA tiene A de 8, B de 8 y C de 12 compases. ¿Cuántos compases suma?", "8+8+8+12+8", "La A suena tres veces, la B una vez y la C una vez.", " compases"),
    ],
    [ex("Escuchas una canción de ejemplo: estrofa 1, estribillo, estrofa 2, estribillo, puente, estribillo. ¿Cuántas veces suena el estribillo?", "3", "Aparece después de la estrofa 1, después de la 2 y al final.")],
    [ex("¿Qué es la textura polifónica?", "Varias melodías a la vez", "Cada línea tiene vida propia."), ex("¿Qué forma tiene una pieza cuya sección A vuelve al final?", "ABA", "Es la forma con regreso."), ex("¿Qué elemento permite distinguir una flauta de un violín?", "El timbre", "Es el color propio del instrumento.")],
    (
        "Analiza esta pieza de ejemplo: «Sección A (8 compases): una flauta sola toca una melodía. Sección B (8 compases): la flauta toca otra melodía y una guitarra la acompaña con acordes. Sección A (8 compases): la flauta sola vuelve a tocar la melodía del principio». Escribe 1) la forma con letras, 2) la textura de cada sección, 3) cuántos compases tiene en total, 4) qué cambia entre A y B.",
        "Forma ABA. Textura: A monofónica; B homofónica; A monofónica. Total 8 + 8 + 8 = 24 compases. Entre A y B cambian la melodía y el acompañamiento: la B tiene otra melodía y se agrega la guitarra con acordes.",
        ["nombra la forma con letras", "distingue monofónica de homofónica", "calcula el total de compases"],
        ["análisis escrito", "total de compases"],
        ["llamar polifónica a una melodía con acompañamiento", "contar mal las secciones"],
        "Reconoce el análisis y pide señalar qué dato del texto distingue la textura de A y la de B.",
    ),
    "Escucha o recuerda una canción y cuenta cuántas veces se repite su estribillo.",
    "Inventa una forma de cuatro secciones con letras (por ejemplo, ABAC) y descríbela con timbres.",
)

# ---------------------------------------------------------------- OA 02 · clase 4 (procedimientos compositivos y propósito expresivo)
L(
    OA2, 4,
    f"Lápiz y papel. Escala de números: {NOTAS}. Todas las melodías están escritas en los ejercicios. Puedes cantarlas con «la» o tocarlas, solo o con alguien más, a volumen cómodo.",
    "Aprenderé a reconocer procedimientos compositivos evidentes (repetición, variación, contraste, secuencia, imitación y ostinato) y a explicar qué efecto buscan. Sirve para entender por qué una música se siente insistente, sorprendente o cerrada.",
    ["Sé leer una melodía escrita con números.", "Sé que una melodía puede repetirse.", "Sé distinguir contrastes de tempo y de volumen."],
    [
        "Un procedimiento compositivo es una manera de organizar el material musical. La repetición vuelve a presentar algo igual. La variación lo presenta con un cambio pequeño, de modo que todavía se reconoce. El contraste presenta algo distinto, como una parte lenta seguida de una rápida. Un motivo es una idea musical corta, de pocas notas. La secuencia repite un motivo más arriba o más abajo: 1-2-3 y luego 2-3-4, un escalón más arriba. Un escalón es pasar de una nota a la nota vecina de la escala, como de 1 a 2. La imitación hace que otra voz repita el motivo después. El ostinato es un patrón corto que se repite sin parar.",
        "Cada procedimiento produce un efecto. La repetición da seguridad y ayuda a recordar. El ostinato crea insistencia, como una marcha o un suspenso. La variación mantiene el interés sin perder lo conocido. El contraste produce sorpresa o cambio de ánimo. La secuencia que sube genera impulso y tensión. La imitación da sensación de diálogo, como en un canon.",
        "Para describir una música se señala el procedimiento con la evidencia: «Es una secuencia, porque el motivo 1-2-3 se repite como 2-3-4, un escalón más arriba». Luego se relaciona con el propósito expresivo: «Sirve para dar impulso». Un mismo fragmento puede tener varios procedimientos. Lo importante es decir cuál se oye, dónde, y qué efecto tiene en el conjunto.",
    ],
    [("repetición", "volver a presentar algo igual"), ("variación", "presentar algo con un cambio pequeño, pero todavía reconocible"), ("contraste", "presentar algo distinto"), ("secuencia", "repetir un motivo más arriba o más abajo"), ("ostinato", "patrón corto que se repite sin parar")],
    [
        ("Reconocer una secuencia", "Un compás tiene 3-4-5 y el siguiente 4-5-6. ¿Qué procedimiento es?", ["El motivo es el mismo.", "Cada nota subió un escalón."], "Una secuencia ascendente"),
        ("Reconocer una variación", "El compás 1 es 1-2-3-1 y el compás 3 es 1-2-3-5. ¿Qué procedimiento aparece en el compás 3?", ["Es casi igual.", "Solo cambia la última nota."], "Una variación"),
    ],
    [
        ("Llamar repetición a cualquier parecido.", "La repetición es igual; si hay un cambio pequeño, es variación.", "Compara nota por nota con el original."),
        ("Pensar que un ostinato cambia de nota cada vuelta.", "El ostinato repite el mismo patrón corto sin parar.", "Busca un patrón corto que vuelva idéntico."),
    ],
    [
        ex("La melodía 1-2-3 suena dos veces seguidas igual. ¿Qué procedimiento es?", "Repetición", "Se vuelve a presentar lo mismo."),
        ex("El patrón 1-5-1-5 suena una y otra vez en el bajo. ¿Qué procedimiento es?", "Ostinato", "Es un patrón corto que se repite sin parar."),
        ex("Un motivo es 5-4-3 y el siguiente es 6-5-4. ¿Qué procedimiento es?", "Secuencia", "El motivo se repite un escalón más arriba."),
    ],
    [
        ex("Una parte lenta y suave es seguida por otra rápida y fuerte. ¿Qué procedimiento es? A) Contraste. B) Repetición.", "A", "La segunda parte es distinta de la primera."),
        ex("La secuencia 5-4-3 y 6-5-4, ¿sube o baja de un motivo al siguiente?", "Sube", "Cada nota del motivo subió un escalón."),
        ex("Una voz canta 5-6-5-3 y otra voz canta lo mismo, pero entra dos pulsos más tarde. ¿Qué procedimiento hay?", "Imitación", "Una voz repite el motivo después de la otra."),
    ],
    [
        ex("El motivo 1-3-2 se repite en secuencia un escalón más arriba. ¿Qué notas tiene la repetición?", "2-4-3", "Cada nota sube un escalón: 1 pasa a 2, 3 a 4 y 2 a 3."),
        arith("Un motivo de 4 notas aparece 4 veces en secuencia. ¿Cuántas notas suenan en total?", "4*4", "Se multiplican las notas del motivo por las veces que aparece.", " notas"),
        ex("Quieres que una música dé una idea de persecución, con insistencia y tensión. ¿Qué procedimiento eliges? A) Un ostinato rápido y fuerte. B) Una melodía lenta y suave que no se repite.", "A", "El patrón insistente y rápido crea tensión."),
    ],
    [
        ex("Compás 1: 1-2-3. Compás 2: 1-2-3. Compás 3: 1-2-5. ¿Qué procedimiento aparece en el compás 3 respecto del compás 1: variación o contraste?", "Variación", "Casi todo es igual y solo cambia la última nota."),
        ex("Un compositor quiere una sorpresa después de una frase tranquila. ¿Le sirve más el contraste o la repetición exacta?", "El contraste", "Presenta algo distinto, y eso sorprende."),
    ],
    [
        arith("Tres compases en secuencia empiezan en 1, luego en 2 y luego en 3. ¿Cuántos escalones subió el inicio entre el primer y el tercer compás?", "3-1", "Se resta la nota inicial del primer compás de la del tercero.", " escalones"),
        ex("Una pieza tiene una parte A lenta y suave de 8 compases, una parte B rápida y fuerte de 8 compases y vuelve la A. ¿Qué dos procedimientos hay?", "Contraste y repetición", "La B contrasta con la A, y la A vuelve igual."),
    ],
    [ex("En una escena de ejemplo, una música crea suspenso con un ostinato grave y suave que se repite sin cambiar. ¿Qué efecto produce la repetición: insistencia o sorpresa?", "Insistencia", "El patrón que no cambia mantiene la tensión.")],
    [ex("¿Qué procedimiento repite un motivo más arriba o más abajo?", "La secuencia", "Es la definición de la clase."), ex("¿Qué procedimiento hace que una voz repita el motivo después de otra?", "La imitación", "Así funciona el canon."), ex("¿Qué procedimiento presenta algo con un cambio pequeño?", "La variación", "Todavía se reconoce lo anterior.")],
    (
        f"Analiza esta melodía de ejemplo ({NOTAS}): compás 1: 1-2-3; compás 2: 2-3-4; compás 3: 3-4-5; compás 4: 5-5-1. Escribe 1) qué procedimiento aparece entre los compases 1, 2 y 3 y cuántos escalones sube el inicio del compás 1 al 3; 2) qué hace distinto al compás 4 y qué efecto produce; 3) una frase con el propósito expresivo de todo el fragmento (por ejemplo, impulso que llega a una conclusión).",
        "Compases 1 a 3: secuencia ascendente; el inicio sube de 1 a 3, o sea 2 escalones. El compás 4 contrasta: cambia el motivo y termina en la nota 1, lo que cierra la frase. Propósito: dar impulso y llevar a una conclusión.",
        ["nombra el procedimiento con su evidencia", "calcula bien los escalones", "relaciona el procedimiento con el efecto"],
        ["análisis escrito", "frase de propósito expresivo"],
        ["llamar repetición a una secuencia", "no explicar el efecto"],
        "Reconoce el análisis y pide mostrar, en la partitura numérica, la nota donde empieza cada compás.",
    ),
    "Canta 1-2-3 y luego 2-3-4 y di qué procedimiento acabas de hacer.",
    "Inventa una melodía de cuatro compases con una secuencia y un contraste, y márcalos.",
)
