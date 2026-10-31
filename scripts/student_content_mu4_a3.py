"""Student material for 4.º básico Música, OA 05 (improvisación y creación con propósito) y OA 06 (presentación musical responsable)."""
from __future__ import annotations

from student_content_mu4_a import LEY, SIL, TA, TAA, TIRI, TT, L, P, diff, pulses
from student_lessons import arith, ex

OA5, OA6 = "MU04 OA 05", "MU04 OA 06"

# ---------------------------------------------------------------- OA 05 · clase 1
CONSIGNA = "Lluvia: dura 8 pulsos, usa como máximo 3 sonidos distintos del cuerpo (dedos en la mesa, palmas, pies) y va de suave a fuerte"
IMPRO = [
    (1, 8, ["dedos", "palmas"], "de suave a fuerte"),
    (2, 8, ["dedos", "palmas", "pies"], "de fuerte a suave"),
    (3, 10, ["dedos"], "de suave a fuerte"),
    (4, 8, ["dedos", "palmas", "pies", "chasquidos"], "de suave a fuerte"),
]


def cumple(p: int, dur: int, sonidos: list, direccion: str) -> bool:
    return dur == 8 and len(sonidos) <= 3 and direccion == "de suave a fuerte"


IMPRO_TXT = " ".join(f"Improvisación {n}: {d} pulsos, sonidos: {', '.join(s)}, {r}." for n, d, s, r in IMPRO)
CUMPLEN = [n for n, d, s, r in IMPRO if cumple(n, d, s, r)]
assert CUMPLEN == [1]

L(
    OA5, 1,
    f"Lápiz y papel. Para practicar usa solo sonidos del cuerpo (palmas, dedos sobre una mesa, pies suaves) y objetos seguros, a volumen bajo. Consigna de ejemplo: «{CONSIGNA}». Improvisaciones de ejemplo, descritas por escrito: {IMPRO_TXT}",
    "Aprenderé a improvisar dentro de una consigna: inventar sonidos en el momento, pero respetando un propósito y unos límites. Sirve para crear con libertad sin perder el rumbo.",
    ["Sé explorar sonidos con mi cuerpo.", "Sé mantener un pulso.", "Sé nombrar cualidades del sonido."],
    [
        "Improvisar es inventar música en el momento, mientras la tocas. No es tocar cualquier cosa: se improvisa dentro de una consigna. La consigna dice el propósito, es decir, para qué haces la música, y los límites: cuántos pulsos dura, qué sonidos puedes usar y cómo cambia la intensidad. Los límites no impiden crear, ayudan a decidir.",
        f"Veamos una consigna: «{CONSIGNA}». Tiene tres límites: dura 8 pulsos, usa como máximo 3 sonidos distintos y va de suave a fuerte. Para saber si una improvisación cumple, se revisa cada límite. {IMPRO_TXT} Solo la primera cumple los tres límites; las otras fallan en uno.",
        "Antes de improvisar, lee la consigna, elige tus sonidos y cuenta un pulso de entrada. Mientras tocas, escucha lo que haces y sigue el pulso. Cuando termines, revisa si cumpliste los límites. Si no, puedes volver a improvisar. Usa solo sonidos seguros y un volumen que permita conversar sin gritar.",
    ],
    [("improvisar", "inventar música en el momento"), ("consigna", "indicación que da el propósito y los límites de una creación"), ("propósito", "para qué se hace la música"), ("límite", "regla de la consigna: duración, sonidos, intensidad"), ("explorar", "probar sonidos para descubrir cómo suenan")],
    [
        ("Revisar los límites", f"Consigna: «{CONSIGNA}». Improvisación: 8 pulsos, dedos y palmas, de suave a fuerte. ¿Cumple los tres límites?", ["Dura 8 pulsos: cumple.", "Usa 2 sonidos, máximo 3: cumple.", "Va de suave a fuerte: cumple."], "Sí, cumple los tres"),
        ("Encontrar el límite que falla", f"Consigna: «{CONSIGNA}». Improvisación: 10 pulsos, solo dedos, de suave a fuerte. ¿Qué límite no cumple?", ["Duración: 10 en vez de 8.", "Sonidos: 1, está bien.", "Intensidad: suave a fuerte, está bien."], "La duración"),
    ],
    [
        ("Pensar que improvisar es tocar sin pensar.", "Se improvisa dentro de una consigna y con atención al pulso.", "Lee la consigna y escucha mientras tocas."),
        ("Olvidar contar los pulsos y pasarse de la duración.", "La consigna fija la duración.", "Cuenta los pulsos mientras improvisas."),
    ],
    [
        ex("¿Improvisar es inventar música en el momento o leerla de una partitura?", "Inventarla en el momento", "La improvisación no está escrita antes."),
        ex(f"Consigna: «{CONSIGNA}». ¿Cuántos pulsos debe durar la improvisación?", "8", "La consigna dice 8 pulsos."),
        ex("¿Qué palabra nombra «para qué haces la música»?", "Propósito", "El propósito es la razón de la música."),
    ],
    [
        ex(f"{IMPRO_TXT} Escribe el número de la improvisación que usa 4 sonidos distintos.", "4", "La improvisación 4 usa dedos, palmas, pies y chasquidos."),
        ex(f"Consigna: «{CONSIGNA}». {IMPRO_TXT} ¿Qué límite no cumple la improvisación 2?", "La intensidad", "Va de fuerte a suave, y la consigna pide de suave a fuerte."),
        ex(f"Consigna: «{CONSIGNA}». {IMPRO_TXT} ¿Cuál es la única improvisación que cumple todos los límites?", "La 1", "Las demás fallan en la intensidad, en la duración o en los sonidos."),
    ],
    [
        arith("Una improvisación dura 8 pulsos y llevas 5. ¿Cuántos pulsos te faltan?", "8-5", "Se resta lo ya tocado de la duración total.", " pulsos"),
        arith("Tocas 3 improvisaciones seguidas de 8 pulsos cada una, con 2 pulsos de pausa entre ellas. ¿Cuántos pulsos hay en total?", "3*8+2*2", "Se suman las 3 improvisaciones y las 2 pausas.", " pulsos"),
        ex("Una consigna pide máximo 3 sonidos y tú usas 2. ¿Puedes añadir uno más sin romper la consigna?", "Sí", "Con 3 sonidos todavía cumples el máximo."),
    ],
    [
        ex("Ana dice: «improvisar es fácil porque cualquier cosa vale». ¿Qué le falta entender?", "Que se improvisa dentro de una consigna", "Los límites de la consigna guían la creación."),
        ex(f"Consigna: «{CONSIGNA}». Un niño improvisa y para en el pulso 6. Dice que «ya terminó». ¿Qué límite incumple?", "La duración", "Debía durar 8 pulsos y se detuvo antes."),
    ],
    [
        ex("Cambia la consigna: ahora pide 6 pulsos, 2 sonidos como máximo y de fuerte a suave. Una improvisación dura 6 pulsos, usa dedos y palmas y va de fuerte a suave. ¿Cumple?", "Sí", "Respeta duración, cantidad de sonidos e intensidad."),
        ex("Una consigna dice «una tormenta de 8 pulsos que termina en silencio». ¿Qué debe pasar en el último pulso?", "Silencio", "La consigna pide terminar en silencio."),
    ],
    [ex("En una obra de teatro escolar necesitas el sonido de unos pasos que se acercan, de 8 pulsos y cada vez más fuertes, con dos sonidos corporales. ¿Qué tres límites tiene esa consigna?", "8 pulsos, 2 sonidos, cada vez más fuerte", "Son la duración, la cantidad de sonidos y el cambio de intensidad.")],
    [ex("¿Qué dos cosas fija una consigna?", "El propósito y los límites", "Dice para qué y cómo."), ex("¿Se improvisa con atención al pulso?", "Sí", "El pulso mantiene el orden."), ex("Si tu improvisación no cumple la consigna, ¿qué puedes hacer?", "Volver a improvisar", "Puedes repetirla ajustando el límite que falló.")],
    (
        f"Elige una de estas dos consignas: (A) «Pasos en el bosque: 8 pulsos, máximo 2 sonidos del cuerpo, de suave a fuerte» o (B) «{CONSIGNA}». Improvisa tres veces con sonidos seguros y volumen bajo. Después anota, para cada vez, cuántos pulsos duró, cuántos sonidos usaste y si cumpliste los límites. Si fallaste en un límite, anota en cuál.",
        "Consigna A. Vez 1: 8 pulsos, 2 sonidos, suave a fuerte; cumplí. Vez 2: 7 pulsos; fallé en la duración. Vez 3: 8 pulsos, 2 sonidos, suave a fuerte; cumplí.",
        ["improvisa tres veces dentro de la consigna", "cuenta pulsos y sonidos en cada vez", "revisa cada límite con honestidad"],
        ["improvisación", "registro escrito"],
        ["no contar los pulsos", "usar más sonidos que el máximo"],
        "Reconoce la revisión honesta de los límites y pregunta qué ajustó entre una vez y otra; no juzga la creatividad.",
    ),
    "Improvisa con tres golpes en una mesa durante 4 pulsos, de suave a fuerte.",
    "Escribe una consigna con propósito, duración y un límite de sonidos, y pide a otra persona que improvise.",
)

# ---------------------------------------------------------------- OA 05 · clase 2
M = (TA, TA, TT, TAA)
SEQ = [("motivo", M), ("otro", (TIRI, SIL)), ("motivo", M), ("otro", (TAA, TAA)), ("motivo", M)]
SEQ_TXT = " | ".join(P(*s) if k == "otro" else "MOTIVO" for k, s in SEQ)
SEQ_PULSOS = sum(pulses(*s) for _k, s in SEQ)
SEQ_MOT = sum(1 for k, _s in SEQ if k == "motivo")

L(
    OA5, 2,
    f"Lápiz y palmas. Leyenda de ritmo: {LEY}. El motivo de ejemplo es MOTIVO = {P(*M)}.",
    "Aprenderé a crear un motivo reconocible: una idea musical breve que se oye y se recuerda porque vuelve. Sirve para que una pieza tenga identidad.",
    ["Sé tocar ritmos con TA, ti-ti y TAA.", "Sé reconocer una repetición.", "Sé contar pulsos."],
    [
        "Un motivo es una idea musical muy breve que da identidad a una música. Se reconoce porque vuelve, igual o parecido, varias veces. Un buen motivo es corto, fácil de recordar y tiene algo particular que lo distingue. En esta clase usaremos tres reglas: que tenga entre 3 y 5 símbolos de ritmo, que no sean todos iguales y que se repita al menos 2 veces en la pieza.",
        f"Un ejemplo: MOTIVO = {P(*M)}. Tiene 4 símbolos, no son todos iguales (TA, TA, ti-ti, TAA) y dura {pulses(*M)} pulsos. Si lo repetimos con otras ideas entre medio queda así: {SEQ_TXT}. El motivo suena {SEQ_MOT} veces, y por eso lo reconocemos.",
        "Para crear tu propio motivo, elige 3 a 5 símbolos, tócalos, cámbialos hasta que te guste y comprueba las tres reglas. Si es demasiado largo no se recuerda. Si es demasiado corto o todo igual, no se distingue. Un motivo puede ser rítmico, como los de hoy, o también tener sonidos más agudos o graves.",
    ],
    [("motivo", "idea musical breve que se reconoce porque vuelve"), ("identidad", "lo que hace que una música se reconozca"), ("símbolo", "cada sonido o silencio del ritmo: TA, ti-ti, TAA, SIL, tiri-tiri"), ("recordar", "poder repetir algo después"), ("distinguir", "reconocer algo como diferente de otras cosas")],
    [
        ("Probar un motivo", f"¿{P(TA, TA, TA, TA)} cumple las reglas de un motivo reconocible?", ["Tiene 4 símbolos: bien.", "Los 4 son iguales: falla la segunda regla."], "No: todos los símbolos son iguales"),
        ("Contar apariciones", f"Pieza: {SEQ_TXT}. El MOTIVO es {P(*M)}. ¿Cuántas veces suena y cuántos pulsos dura la pieza?", ["MOTIVO aparece 3 veces de 5 partes.", f"Pulsos: 3 × {pulses(*M)} + {pulses(TIRI, SIL)} + {pulses(TAA, TAA)}."], f"{SEQ_MOT} veces; {SEQ_PULSOS} pulsos"),
    ],
    [
        ("Hacer un motivo larguísimo.", "No se recuerda ni se reconoce cuando vuelve.", "Usa entre 3 y 5 símbolos."),
        ("Crear un motivo y no volver a tocarlo.", "Para reconocerlo debe volver.", "Repítelo al menos 2 veces."),
    ],
    [
        ex("¿Un motivo es una idea musical larga o breve?", "Breve", "Un motivo es una idea musical muy breve."),
        ex(f"¿Cuántos símbolos tiene {P(*M)}?", "4", "Son TA, TA, ti-ti y TAA."),
        ex("Para que un motivo se reconozca, ¿debe volver o no repetirse?", "Debe volver", "Se reconoce porque se repite."),
    ],
    [
        ex(f"¿{P(TA, TAA)} cumple la regla del largo (3 a 5 símbolos)?", "No", "Tiene solo 2 símbolos, uno menos del mínimo."),
        ex(f"¿{P(TA, TT, TA, TIRI, TAA)} cumple la regla del largo?", "Sí", "Tiene 5 símbolos, dentro del rango de 3 a 5."),
        ex(f"¿{P(TA, TT, TA, TT, TA, TT)} cumple la regla del largo?", "No", "Tiene 6 símbolos, uno más que el máximo."),
    ],
    [
        arith(f"Pieza: {SEQ_TXT}. El MOTIVO es {P(*M)}. ¿Cuántos pulsos dura la pieza?", f"3*{pulses(*M)}+{pulses(TIRI, SIL)}+{pulses(TAA, TAA)}", "Se suman las tres veces del motivo y las dos ideas intermedias.", " pulsos"),
        ex(f"Compara {P(*M)} con {P(TA, TA, TT, TA)}. ¿En cuántos lugares difieren?", str(diff(M, (TA, TA, TT, TA))), "Solo el último símbolo cambia, de TAA a TA."),
        ex(f"¿Cuál de estos dos ritmos es mejor motivo según las reglas: (a) {P(TA, TA, TA, TA)} o (b) {P(TA, TT, TA, TAA)}?", "(b)", "La (a) tiene todos los símbolos iguales y la (b) los combina."),
    ],
    [
        ex("Un niño dice que su motivo es muy bueno porque tiene 8 símbolos y lo toca una sola vez. ¿Qué dos reglas incumple?", "El largo y la repetición", "Tiene más de 5 símbolos y no vuelve a sonar."),
        ex("Dos compañeras escuchan una pieza y reconocen enseguida la idea que vuelve tres veces. ¿Qué cualidad del motivo muestran?", "Que es reconocible porque se repite", "Se reconoce por su repetición."),
    ],
    [
        ex("Un motivo de 3 símbolos usa TA, ti-ti y TAA una sola vez cada uno, empieza con ti-ti y termina con TAA. ¿Cuál es su segundo símbolo?", "TA", "Falta solo el TA para completar el orden ti-ti, TA, TAA."),
        arith(f"Tocas el motivo {P(*M)} 4 veces seguidas. ¿Cuántos sonidos tocas?", f"{1+1+2+1}*4", "Cada vez suenan TA (1), TA (1), ti-ti (2) y TAA (1): 5 sonidos, por 4 vueltas.", " sonidos"),
    ],
    [ex("Una pieza para un cumpleaños usa el mismo ritmo corto cada vez que aparece el nombre de la persona. ¿Qué es ese ritmo corto que vuelve?", "El motivo", "El motivo es la idea breve que vuelve.")],
    [ex("¿Cuántas veces debe volver un motivo, como mínimo?", "2", "Debe repetirse al menos 2 veces."), ex("¿Un motivo con todos los símbolos iguales se distingue bien?", "No", "Falta algo particular que lo distinga."), ex("¿Qué es un motivo?", "Una idea musical breve que se reconoce porque vuelve", "Esa es su definición.")],
    (
        "Crea un motivo de 3 a 5 símbolos con TA, ti-ti, tiri-tiri, TAA y SIL (por ejemplo TA – ti-ti – TA – TAA). Toca el motivo con las palmas. Luego arma una pieza corta de 5 partes donde tu motivo aparezca 3 veces, con otras ideas entre medio. Anota el motivo, la pieza y cuántos pulsos dura.",
        "Motivo: TA – ti-ti – TA – TAA (5 pulsos). Pieza: MOTIVO | TAA – TAA | MOTIVO | tiri-tiri – SIL | MOTIVO. Duración: 3 × 5 + 4 + 2 = 21 pulsos.",
        ["crea un motivo de 3 a 5 símbolos no todos iguales", "lo repite al menos 2 veces", "calcula los pulsos de la pieza"],
        ["motivo y pieza escritos", "interpretación con palmas"],
        ["hacer un motivo muy largo", "no repetirlo"],
        "Reconoce el motivo y pide tocarlo igual cada vez que vuelve; si hay error, corrige el conteo sumando parte por parte.",
    ),
    "Toca tu nombre como un ritmo con palmas y di si es un buen motivo según las reglas.",
    "Crea dos motivos distintos y compara cuál se recuerda más fácil.",
)

# ---------------------------------------------------------------- OA 05 · clase 3
VAR_TXT = (
    "Versión 0 (el motivo original): ritmo TA – TA – ti-ti – TAA, suave, tempo normal, con palmas. "
    "Versión 1: el mismo ritmo, fuerte, tempo normal, con palmas. "
    "Versión 2: el mismo ritmo, suave, el doble de rápido, con palmas. "
    "Versión 3: el mismo ritmo, suave, tempo normal, con dos cucharas de madera sobre una mesa. "
    "Versión 4: otro ritmo, TAA – TAA – SIL – TA, suave, tempo normal, con palmas. "
    "Versión 5: el mismo ritmo, fuerte, el doble de rápido, con cucharas de madera."
)

L(
    OA5, 3,
    f"Lápiz y palmas, y para el timbre dos cucharas de madera sobre una mesa a volumen bajo. Versiones de ejemplo: {VAR_TXT}",
    "Aprenderé a variar una cualidad del sonido (intensidad, tempo o timbre) conservando la identidad del motivo. Sirve para que una pieza avance sin perder su idea.",
    ["Sé crear un motivo reconocible.", "Sé nombrar las cualidades del sonido.", "Sé la diferencia entre variación y contraste."],
    [
        "Una variación cambia algo de una idea musical y conserva lo esencial. Para un motivo, lo esencial es su ritmo, porque es lo que se reconoce. Si cambias casi todo el ritmo, ya es otra idea, como en un contraste. Si cambias una cualidad del sonido, como la intensidad, el tempo o el timbre, el motivo sigue siendo el mismo con otro aspecto.",
        f"Veamos las versiones del ejemplo. {VAR_TXT} La versión 1 cambia solo la intensidad. La versión 2 cambia solo el tempo. La versión 3 cambia solo el timbre. La versión 4 cambia el ritmo, por eso ya no es una variación del motivo. La versión 5 cambia tres cualidades a la vez, pero conserva el ritmo.",
        "Al variar, cambia pocas cualidades para que se siga reconociendo. Si cambias solo una, la variación es suave. Si cambias dos o tres, es más fuerte, pero sigue valiendo si el ritmo es el mismo. Para comprobar la identidad pregunta: ¿alguien que conoce el motivo lo reconocería? Si la respuesta es sí, hay variación.",
    ],
    [("variación", "cambio de algo que conserva lo esencial"), ("identidad", "lo que hace reconocible al motivo; su ritmo"), ("intensidad", "qué tan fuerte o suave suena"), ("tempo", "qué tan rápido va el pulso"), ("timbre", "el «color» del sonido; depende de lo que lo produce")],
    [
        ("Detectar qué cambia", f"{VAR_TXT} ¿Qué cualidad cambia en la versión 2 respecto de la versión 0?", ["Ritmo: igual.", "Intensidad: igual, suave.", "Tempo: el doble de rápido.", "Timbre: igual, palmas."], "El tempo"),
        ("Decidir si hay identidad", f"{VAR_TXT} ¿La versión 4 es una variación del motivo?", ["El ritmo es otro: TAA – TAA – SIL – TA.", "Sin el ritmo se pierde la identidad."], "No; cambia el ritmo, que es lo esencial"),
    ],
    [
        ("Cambiar el ritmo y decir que es solo una variación de intensidad.", "El ritmo es lo que da identidad al motivo.", "Si cambias el ritmo, ya no es una variación."),
        ("Cambiar tantas cosas que no se reconoce la idea.", "Sin identidad no hay variación.", "Mantén el ritmo y cambia pocas cualidades."),
    ],
    [
        ex(f"{VAR_TXT} ¿Qué cualidad cambia en la versión 1?", "La intensidad", "Pasa de suave a fuerte; todo lo demás es igual."),
        ex(f"{VAR_TXT} ¿Qué cualidad cambia en la versión 3?", "El timbre", "Se tocan cucharas en vez de palmas."),
        ex("¿Qué se conserva en una variación del motivo: el ritmo o el volumen?", "El ritmo", "El ritmo es lo que da identidad al motivo."),
    ],
    [
        ex(f"{VAR_TXT} ¿Cuántas cualidades cambian en la versión 5 respecto de la versión 0?", "3", "Cambian la intensidad, el tempo y el timbre."),
        ex(f"{VAR_TXT} Escribe los números de las versiones que conservan el ritmo del motivo.", "1, 2, 3 y 5", "Solo la versión 4 cambia el ritmo."),
        ex(f"{VAR_TXT} ¿Cuál es la única versión que no es una variación del motivo?", "La versión 4", "Tiene otro ritmo, así que pierde la identidad."),
    ],
    [
        arith(f"El motivo dura {pulses(TA, TA, TT, TAA)} pulsos. Tocas el original y tres variaciones que conservan el ritmo. ¿Cuántos pulsos tocas en total?", f"4*{pulses(TA, TA, TT, TAA)}", "Son 4 versiones de 5 pulsos cada una; cambiar el tempo no cambia los pulsos del motivo.", " pulsos"),
        ex("Un niño toca el motivo suave y luego el mismo motivo fuerte con las mismas notas y el mismo ritmo. ¿Qué cualidad varió?", "La intensidad", "Solo cambió suave por fuerte."),
        ex("Una niña toca el motivo primero con palmas y luego con una caja de cartón, sin cambiar nada más. ¿Qué cualidad varió?", "El timbre", "Cambió el objeto que produce el sonido."),
    ],
    [
        ex("Pedro dice que cambió el tempo y la intensidad y que por eso «ya es otra música». ¿Tiene razón si mantuvo el ritmo?", "No; sigue siendo la misma idea variada", "Conservó el ritmo, que da la identidad."),
        ex("Ana quiere una variación suave del motivo. ¿Cuántas cualidades debe cambiar: una o las tres?", "Una", "Cambiar pocas cualidades mantiene la identidad más clara."),
    ],
    [
        ex(f"Se quiere una variación de {P(*M)} que cambie solo la intensidad. ¿Cuál sirve: (a) igual ritmo, fuerte, mismo tempo y mismo timbre o (b) otro ritmo, suave, mismo tempo?", "(a)", "Solo la (a) conserva el ritmo y cambia solo la intensidad."),
        arith(f"Tocas el motivo {P(*M)} 4 veces en tempo normal y otras 4 veces al doble de rápido. ¿Cuántos pulsos del motivo tocas en total?", f"4*{pulses(*M)}+4*{pulses(*M)}", "Los pulsos del motivo no cambian con el tempo: son 5 por vuelta y hay 8 vueltas.", " pulsos"),
    ],
    [ex("Cuando un cantante repite una estrofa más suave y luego más fuerte, pero con la misma melodía, ¿qué hace con la melodía y qué cualidad varía?", "Conserva la melodía y varía la intensidad", "La identidad queda y cambia el volumen.")],
    [ex("¿Cuál cualidad cambia si pasas de palmas a cucharas?", "El timbre", "Cambia el objeto que suena."), ex("¿Qué se debe conservar en una variación?", "La identidad del motivo", "Es lo que permite reconocer la idea."), ex("¿Variar el tempo cambia el ritmo del motivo?", "No", "El ritmo queda igual; solo va más rápido o más lento.")],
    (
        f"Elige tu motivo de la clase anterior (o usa {P(*M)}). Toca el original y tres variaciones: una que cambie solo la intensidad, otra solo el tempo y otra solo el timbre (usa dos cucharas de madera sobre una mesa o una caja, a volumen bajo). Escribe una tabla con las cuatro versiones y marca qué cualidad cambió en cada una y si el ritmo se conservó.",
        "Original: suave, tempo normal, palmas. Variación 1: fuerte (cambia intensidad). Variación 2: el doble de rápido (cambia tempo). Variación 3: con cucharas (cambia timbre). En las tres el ritmo se conservó.",
        ["toca tres variaciones que conservan el ritmo", "cambia una sola cualidad en cada variación", "completa la tabla con las cualidades"],
        ["interpretación", "tabla escrita"],
        ["cambiar el ritmo sin darse cuenta", "cambiar dos cualidades a la vez cuando se pedía una"],
        "Reconoce la tabla y pide tocar el original antes de cada variación para comprobar que se reconoce.",
    ),
    "Toca tu motivo suave y luego fuerte, y di qué cualidad cambió.",
    "Crea una variación que cambie dos cualidades y comprueba si una persona de tu casa aún reconoce el motivo.",
)

# ---------------------------------------------------------------- OA 05 · clase 4
Q = (TA, TT, TA, SIL)
RESPUESTAS = {
    1: (TA, TT, TAA),
    2: (TIRI, TIRI, TA, SIL),
    3: (TA, TT, TA, TAA),
    4: (TAA, TAA),
}
RESP_TXT = " ".join(f"Respuesta {n}: {P(*r)}." for n, r in RESPUESTAS.items())
REGLAS = "(1) dura lo mismo que la pregunta, (2) conserva los dos primeros símbolos de la pregunta y (3) termina en un sonido largo, TAA, que «cierra»"


def es_buena(r: tuple) -> bool:
    return pulses(*r) == pulses(*Q) and diff(r[:2], Q[:2]) == 0 and r[-1] == TAA


BUENAS = [n for n, r in RESPUESTAS.items() if es_buena(r)]
assert BUENAS == [1]

L(
    OA5, 4,
    f"Lápiz y palmas. Leyenda de ritmo: {LEY}. Pregunta de ejemplo: {P(*Q)}. {RESP_TXT} Reglas de la clase para una buena respuesta: {REGLAS}.",
    "Aprenderé a organizar una pieza en pregunta y respuesta: una frase que queda abierta y otra que la contesta y cierra. Sirve para armar música que «conversa».",
    ["Sé contar pulsos de un patrón.", "Sé reconocer repetición, contraste y variación.", "Sé crear un motivo."],
    [
        "En una pregunta y respuesta, una frase musical se oye «abierta», como una pregunta que espera respuesta, y la siguiente la contesta y se oye «cerrada». En el ritmo, la pregunta suele terminar con un sonido corto o con un silencio, y la respuesta suele terminar con un sonido largo que cierra, como un TAA.",
        f"En esta clase usaremos tres reglas para una buena respuesta: {REGLAS}. La pregunta de ejemplo es {P(*Q)} y dura {pulses(*Q)} pulsos. Revisemos las respuestas. {RESP_TXT} La respuesta 1 dura {pulses(*RESPUESTAS[1])} pulsos, conserva los dos primeros símbolos y termina en TAA: cumple. La 2 termina en SIL y no conserva nada. La 3 dura 5 pulsos. La 4 no conserva nada de la pregunta.",
        "Las preguntas y respuestas se pueden tocar entre dos personas, con una pregunta y la otra responde, o con dos instrumentos. Si quien responde conserva una parte de la pregunta, se oye que realmente contesta. Si responde con algo muy distinto, la frase sigue siendo música, pero se oye más como un contraste que como una respuesta.",
    ],
    [("pregunta", "frase que queda abierta"), ("respuesta", "frase que contesta y cierra"), ("abierta", "que suena como si faltara algo"), ("cerrada", "que suena terminada"), ("conversar", "turnarse para hablar, también con música")],
    [
        ("Revisar una respuesta", f"Pregunta: {P(*Q)}. Respuesta: {P(*RESPUESTAS[1])}. ¿Cumple las tres reglas ({REGLAS})?", [f"Duración: ambas {pulses(*Q)} pulsos.", "Conserva los dos primeros símbolos: TA y ti-ti.", "Termina en TAA."], "Sí, cumple las tres reglas"),
        ("Encontrar el error", f"Pregunta: {P(*Q)}. Respuesta: {P(*RESPUESTAS[3])}. ¿Qué regla no cumple?", [f"Pregunta: {pulses(*Q)} pulsos; respuesta: {pulses(*RESPUESTAS[3])} pulsos.", "Duración distinta: falla la regla 1."], "Dura 5 pulsos y la pregunta 4"),
    ],
    [
        ("Terminar la pregunta con un sonido largo que cierra.", "La pregunta debe quedar abierta.", "Termina la pregunta con un sonido corto o un silencio."),
        ("Responder con algo que no tiene nada que ver.", "No se oye que contesta.", "Conserva los dos primeros símbolos de la pregunta."),
    ],
    [
        ex("¿Qué frase suena «abierta»: la pregunta o la respuesta?", "La pregunta", "La pregunta queda esperando una respuesta."),
        ex(f"La pregunta {P(*Q)}, ¿cuántos pulsos dura?", str(pulses(*Q)), "Cada símbolo ocupa un pulso."),
        ex("¿Con qué sonido suele terminar la respuesta en esta clase: TA o TAA?", "TAA", "El TAA es un sonido largo que cierra."),
    ],
    [
        ex(f"{RESP_TXT} ¿Cuántos pulsos dura la respuesta 4?", str(pulses(*RESPUESTAS[4])), "TAA y TAA suman 2 + 2 pulsos."),
        ex(f"Pregunta: {P(*Q)}. {RESP_TXT} ¿Cuál respuesta cumple las tres reglas? Escribe su número.", "1", "Solo la 1 dura 4 pulsos, conserva dos símbolos y termina en TAA."),
        ex(f"Pregunta: {P(*Q)}. ¿La respuesta 2 ({P(*RESPUESTAS[2])}) termina con un sonido que cierra?", "No", "Termina en SIL, no en TAA."),
    ],
    [
        arith(f"Una pregunta de {pulses(*Q)} pulsos y su respuesta de {pulses(*RESPUESTAS[1])} pulsos se tocan 3 veces seguidas. ¿Cuántos pulsos son en total?", f"3*({pulses(*Q)}+{pulses(*RESPUESTAS[1])})", "Cada vuelta suma pregunta y respuesta; se repite 3 veces.", " pulsos"),
        ex(f"Compara la respuesta 3 ({P(*RESPUESTAS[3])}) con la pregunta {P(*Q)}. ¿En cuántos lugares cambia?", str(diff(RESPUESTAS[3], Q)), "Solo cambia el último símbolo, de SIL a TAA."),
        ex("Dos personas se turnan: una toca la pregunta, la otra la respuesta. Si la pregunta se toca 4 veces, ¿cuántas respuestas se tocan?", "4", "Cada pregunta tiene su respuesta."),
    ],
    [
        ex("Un niño dice: «la respuesta 4 es la mejor porque suena larga». ¿Qué regla incumple, aunque termine en TAA?", "Conservar los dos primeros símbolos de la pregunta", "No tiene nada en común con la pregunta."),
        ex("Una niña responde repitiendo la pregunta exacta, también terminando en SIL. ¿Es una respuesta que cierra?", "No", "Termina en silencio, igual que la pregunta, y queda abierta."),
    ],
    [
        ex(f"Crea una respuesta para la pregunta {P(TA, TA, TT, SIL)} que dure 4 pulsos, conserve los dos primeros símbolos y termine en TAA. ¿Cuál es? (usa TA, ti-ti y TAA)", P(TA, TA, TAA), "Dura 1 + 1 + 2 = 4 pulsos, conserva TA – TA y termina en TAA."),
        arith("Una pieza tiene 3 pares de pregunta y respuesta. Cada pregunta dura 4 pulsos y cada respuesta 4. ¿Cuántos pulsos dura la pieza?", "3*(4+4)", "Cada par suma 8 pulsos y son 3 pares.", " pulsos"),
    ],
    [ex("En una conversación con tambores, un niño toca una frase corta que termina en silencio y otra niña le responde con una frase igual al comienzo pero que termina en un golpe largo. ¿Qué organización musical hacen?", "Pregunta y respuesta", "Una frase queda abierta y la otra la contesta y cierra.")],
    [ex("¿Cómo termina una pregunta rítmica en esta clase: en sonido corto o silencio, o en TAA?", "En sonido corto o silencio", "Así queda abierta."), ex("¿Una respuesta debe durar lo mismo que la pregunta?", "Sí", "Es la primera regla."), ex("¿Qué debe conservar una respuesta de la pregunta, según las reglas de la clase?", "Los dos primeros símbolos", "Así se oye que contesta.")],
    (
        f"Con una persona de tu casa, o tú solo con dos sonidos distintos, crea tres pares de pregunta y respuesta rítmicas. Cada pregunta debe durar 4 pulsos y terminar en sonido corto o SIL. Cada respuesta debe durar 4 pulsos, conservar los dos primeros símbolos de la pregunta y terminar en TAA. Escríbelos, revisa las tres reglas y tócalos por turnos.",
        f"Pregunta 1: {P(*Q)}. Respuesta 1: {P(*RESPUESTAS[1])}. Pregunta 2: {P(TA, TA, TA, SIL)}. Respuesta 2: {P(TA, TA, TAA)}. Pregunta 3: {P(TT, TA, SIL, TA)}. Respuesta 3: {P(TT, TA, TAA)}.",
        ["crea tres pares de 4 pulsos cada frase", "las respuestas conservan los dos primeros símbolos de su pregunta", "termina cada respuesta en TAA y cada pregunta abierta"],
        ["pares escritos", "interpretación por turnos"],
        ["responder con una frase que dura distinto", "terminar la pregunta en sonido largo"],
        "Reconoce el cumplimiento de las reglas y pide cantar la respuesta pensando en el final; ayuda a contar los pulsos de cada frase.",
    ),
    "Toca una pregunta de 4 pulsos con palmas y responde con tus pies, terminando en un golpe largo.",
    "Crea una pregunta y dos respuestas distintas, y elige la que más cierre.",
)

# ---------------------------------------------------------------- OA 05 · clase 5
BORR = {
    "X": dict(proposito=True, forma=True, motivo=True, variacion=False, duracion=True),
    "Y": dict(proposito=True, forma=True, motivo=False, variacion=True, duracion=False),
}
CRIT = ["propósito claro", "forma definida (por ejemplo ABA)", "un motivo reconocible que vuelve", "una variación del motivo", "duración acordada"]
BORR_TXT = (
    "Borrador X: propósito «una carrera»; forma A B A; el motivo TA – TA – ti-ti – TAA aparece en las dos A; no hay variación; dura 12 pulsos, como se acordó. "
    "Borrador Y: propósito «un baile»; forma A B; el motivo no aparece; la B es una variación de la A; dura 14 pulsos, pero se había acordado 12."
)
CUM_X = sum(BORR["X"].values())
CUM_Y = sum(BORR["Y"].values())
assert (CUM_X, CUM_Y) == (4, 3)

L(
    OA5, 5,
    f"Lápiz y palmas. Criterios de revisión: {', '.join(f'({i}) {c}' for i, c in enumerate(CRIT, 1))}. Borradores de ejemplo, descritos por escrito: {BORR_TXT}",
    "Aprenderé a construir una pieza breve que use un motivo, una variación y una forma, y a revisarla con criterios. Sirve para mejorar mi creación con decisiones fundadas.",
    ["Sé improvisar dentro de una consigna.", "Sé crear y variar un motivo.", "Sé organizar pregunta y respuesta."],
    [
        "Construir una pieza breve es juntar lo aprendido en una creación con un propósito. Primero decide para qué es la pieza, por ejemplo una carrera, un baile o la lluvia. Después elige la forma, como ABA, y un motivo reconocible que vuelva. Incluye al menos una variación del motivo para que no sea repetición pura. Por último acuerda cuánto dura.",
        f"Revisar es comparar tu pieza con criterios. Los cinco criterios de la clase son: {', '.join(f'({i}) {c}' for i, c in enumerate(CRIT, 1))}. Cada criterio cumplido suma un punto. {BORR_TXT} El borrador X cumple {CUM_X} de 5: le falta la variación. El borrador Y cumple {CUM_Y} de 5: le falta el motivo y la duración acordada.",
        "Después de revisar, decide qué cambiar. No tienes que cambiar todo: elige el criterio que falta y arréglalo. Para el borrador X, agrega una variación en la segunda A. Para el Y, incluye el motivo y recorta 2 pulsos. Vuelve a tocar y revisa otra vez. La pieza final es el resultado de varias versiones, no de una sola.",
    ],
    [("pieza breve", "música corta con propósito, forma y duración"), ("borrador", "versión de prueba que aún se puede cambiar"), ("criterio de revisión", "pregunta con que se evalúa la pieza"), ("forma", "orden de las secciones, como ABA"), ("versión", "cada intento de la pieza")],
    [
        ("Contar criterios cumplidos", f"{BORR_TXT} ¿Cuántos de los 5 criterios cumple el borrador X y cuál le falta?", ["Propósito: sí.", "Forma: sí.", "Motivo: sí.", "Variación: no.", "Duración: sí."], f"{CUM_X} de 5; le falta la variación"),
        ("Decidir un arreglo", f"{BORR_TXT} El borrador Y dura 14 pulsos y se acordó 12. ¿Cuántos pulsos debe recortar?", ["Duración actual: 14 pulsos.", "Duración acordada: 12 pulsos.", "14 − 12 = 2."], "2 pulsos"),
    ],
    [
        ("Cambiar toda la pieza al primer problema.", "Se pierde lo que ya funciona.", "Arregla solo el criterio que falta y vuelve a revisar."),
        ("Terminar sin revisar con los criterios.", "No sabes si cumple lo que te propusiste.", "Revisa los cinco criterios antes de dar por terminada la pieza."),
    ],
    [
        ex(f"{BORR_TXT} ¿Cuál es el propósito del borrador Y?", "Un baile", "Así lo dice la descripción del borrador."),
        ex("¿Cuántos criterios tiene la revisión de la clase?", "5", "Son propósito, forma, motivo, variación y duración."),
        ex(f"{BORR_TXT} ¿Qué forma tiene el borrador X?", "A B A", "La descripción lo indica."),
    ],
    [
        ex(f"{BORR_TXT} ¿Qué criterio no cumple el borrador X?", "La variación", "No tiene ninguna variación del motivo."),
        ex(f"{BORR_TXT} ¿Cuántos criterios cumple el borrador Y?", str(CUM_Y), "Cumple el propósito, la forma y la variación; no cumple el motivo ni la duración."),
        ex(f"{BORR_TXT} ¿Cuántas veces suena el motivo en el borrador X?", "2", "Aparece en las dos secciones A."),
    ],
    [
        arith("Una pieza ABA tiene secciones de 4 pulsos cada una. ¿Cuántos pulsos dura?", "3*4", "Son tres secciones de 4 pulsos.", " pulsos"),
        arith("Una pieza ABA acordada para 12 pulsos tiene A de 4 pulsos, B de 6 pulsos y A de 4 pulsos. ¿Cuántos pulsos se pasa?", "4+6+4-12", "Se suma lo que dura y se resta lo acordado.", " pulsos"),
        ex(f"{BORR_TXT} Para arreglar el borrador X, ¿dónde conviene poner la variación: en la segunda A o eliminar la B?", "En la segunda A", "Se agrega una variación sin quitar lo que ya cumple."),
    ],
    [
        ex(f"{BORR_TXT} Un niño dice que el borrador Y es mejor que el X porque tiene variación. ¿Por qué no basta ese argumento?", "Porque el Y cumple menos criterios en total", "El X cumple 4 de 5 y el Y cumple 3 de 5."),
        ex("Una pieza cumple 5 de 5 criterios y un compañero dice: «entonces no hace falta ensayarla». ¿Tiene razón?", "No", "Cumplir los criterios no asegura que se toque bien; hay que ensayar la interpretación."),
    ],
    [
        ex(f"Pieza de ejemplo: propósito «la lluvia»; forma A B A; el motivo vuelve en las dos A; la B es una variación del motivo; dura 12 pulsos como se acordó. ¿Cuántos criterios cumple?", "5", "Cumple propósito, forma, motivo, variación y duración."),
        arith("Un grupo hace 4 versiones de su pieza y cada versión dura 12 pulsos. Si se toca cada versión una vez, ¿cuántos pulsos tocan?", "4*12", "Se multiplican las versiones por su duración.", " pulsos"),
    ],
    [ex("Para el recreo, un curso quiere una pieza corta de 12 pulsos que suene como una carrera: una parte rápida, otra más lenta y otra rápida otra vez. ¿Qué forma musical tiene esa idea?", "ABA", "Rápida, lenta y rápida: la primera vuelve al final.")],
    [ex("¿Qué se hace después de revisar la pieza?", "Decidir qué cambiar y volver a tocar", "La revisión sirve para mejorar."), ex("¿Cuántos puntos suma cada criterio cumplido?", "Uno", "Cada criterio cumplido suma un punto."), ex("En Música: ¿Qué es un borrador?", "Una versión de prueba que se puede cambiar", "Es un intento que aún se mejora.")],
    (
        "Construye una pieza breve de forma ABA con un motivo de 3 a 5 símbolos (de la clase 2), una variación del motivo (de la clase 3) y, si quieres, una pregunta y respuesta en la B. Dale un propósito y una duración acordada (por ejemplo 12 pulsos). Escribe un borrador, revísalo con los cinco criterios, cambia lo que falte y escribe la versión final. Toca la pieza con sonidos del cuerpo o con objetos seguros, a volumen bajo.",
        f"Propósito: una carrera. Forma A B A. Motivo: {P(TA, TT, TA, TA)} (4 pulsos) en cada A. B: el mismo motivo con tempo más rápido. Final: A. Duración: 4 + 4 + 4 = 12 pulsos, como se acordó. Cumple 5 de 5 criterios.",
        ["define el propósito, la forma y la duración", "incluye un motivo reconocible y una variación", "revisa los cinco criterios y corrige"],
        ["borrador y versión final", "interpretación"],
        ["no revisar con los criterios", "pasarse de la duración acordada"],
        "Reconoce el proceso de revisión y pregunta qué criterio mejoró; si hay error de duración, sugiere recontar pulsos sección por sección.",
    ),
    "Elige un propósito (lluvia, carrera o baile) y escribe una forma ABA para él.",
    "Toca tu pieza a una persona de tu casa y pídele que diga cuál es el motivo.",
)

# ---------------------------------------------------------------- OA 06 · clase 1
ROLES = "presentador o presentadora (saluda y explica en pocas palabras), intérpretes (tocan o cantan), responsable de la señal (cuenta 4 pulsos para empezar) y apoyo de materiales (prepara y guarda los instrumentos)"

L(
    OA6, 1,
    f"Lápiz y papel. Roles de ejemplo: {ROLES}. Todas las situaciones están descritas por escrito.",
    "Aprenderé a definir el propósito, la audiencia y los roles de una presentación musical, y a asumir mi parte con responsabilidad. Sirve para compartir mi trabajo con otras personas de forma ordenada.",
    ["Sé tocar o cantar una pieza breve.", "Sé trabajar en grupo.", "Sé cuidar los instrumentos."],
    [
        "Presentar es compartir tu trabajo musical con otras personas, que son la audiencia: el curso, la familia o la comunidad. Antes de presentar, el grupo decide el propósito: para qué comparte la música, por ejemplo para alegrar un recreo, mostrar lo aprendido o celebrar algo. El propósito ayuda a elegir qué tocar y cuánto dura.",
        f"Cada integrante cumple un rol. Los roles de esta clase son: {ROLES}. Puede haber más de un intérprete y una persona puede tener dos roles. Si a alguien le da vergüenza presentarse ante todos, hay alternativas: tocar en grupo, hacerlo ante un grupo pequeño o ser responsable de la señal o de los materiales. Todos los roles son importantes.",
        "Responsabilidad significa cumplir lo que prometiste: llegar a los ensayos, aprender tu parte, cuidar el material y respetar el tiempo acordado. Compromiso es querer que la presentación salga bien para todos. Respetar a la audiencia es presentarse a tiempo, hablar claro y agradecer.",
    ],
    [("presentación", "compartir un trabajo ante otras personas"), ("audiencia", "las personas que escuchan"), ("propósito", "para qué se comparte la música"), ("rol", "la tarea que cumple cada integrante"), ("responsabilidad", "cumplir lo que prometiste hacer")],
    [
        ("Asignar roles", "Un grupo de 6 personas tiene 1 presentador, 1 responsable de la señal y 1 de materiales. El resto son intérpretes. ¿Cuántos intérpretes hay?", ["Roles que no tocan: 1 + 1 + 1 = 3.", "6 − 3 = 3."], "3 intérpretes"),
        ("Elegir según la audiencia", "El propósito es alegrar un recreo del curso con una pieza de 1 minuto. ¿Qué audiencia tiene y cuánto debe durar como máximo?", ["La audiencia es el curso.", "La pieza dura 1 minuto."], "El curso; 1 minuto como máximo"),
    ],
    [
        ("Pensar que quien no se presenta ante todos no participa.", "Los roles de señal y materiales también son esenciales.", "Elige un rol que te acomode y cúmplelo."),
        ("Llegar tarde al ensayo porque «se puede arreglar en la presentación».", "Afecta al grupo.", "Cumple tu compromiso y avisa si no puedes."),
    ],
    [
        ex("¿Quién saluda y explica en pocas palabras: el presentador o el responsable de materiales?", "El presentador o presentadora", "Ese es el rol que habla a la audiencia."),
        ex("¿Quiénes forman la audiencia si presentas ante tu curso?", "Tu curso", "Son quienes escuchan."),
        ex("¿Qué rol prepara y guarda los instrumentos?", "El apoyo de materiales", "Su tarea es cuidar el material."),
    ],
    [
        ex("¿Qué rol cuenta 4 pulsos para empezar?", "El responsable de la señal", "La señal hace que todos entren juntos."),
        ex("Una niña no quiere hablar frente al curso. ¿Qué opción mantiene su participación: (a) retirarse del grupo o (b) ser responsable de la señal o de los materiales?", "(b)", "Hay roles que no requieren hablar ante todos y que son esenciales."),
        ex("El propósito es «celebrar el cumpleaños de una compañera». ¿Para qué se comparte la música?", "Para celebrar", "El propósito es la razón de compartirla."),
    ],
    [
        arith("Un grupo de 8 personas tiene 1 presentador, 1 responsable de la señal y 2 de materiales. El resto son intérpretes. ¿Cuántos intérpretes hay?", "8-1-1-2", "Se restan los roles que no tocan del total.", " intérpretes"),
        arith("Una presentación tiene un saludo de 10 segundos, una pieza de 60 segundos y un agradecimiento de 10 segundos. ¿Cuántos segundos dura?", "10+60+10", "Se suman las tres partes.", " segundos"),
        arith("Cada ensayo dura 15 minutos y el grupo ensaya 2 veces por semana. ¿Cuántos minutos ensaya en una semana?", "15*2", "Se multiplica la duración por los ensayos.", " minutos"),
    ],
    [
        ex("Luis dice: «yo soy de materiales, entonces no tengo que ir a los ensayos». ¿Qué le responderías?", "Que todos los roles necesitan ir a los ensayos", "El rol de materiales también debe coordinarse con el grupo."),
        ex("Si la audiencia son familiares que no conocen la pieza, ¿qué conviene agregar al saludo: una frase que explique qué se tocará o nada?", "Una frase que explique qué se tocará", "La audiencia entiende mejor si sabe qué escuchará."),
    ],
    [
        ex("Un grupo de 5 personas reparte los roles presentador, señal, materiales e intérpretes, y necesita un presentador y al menos 2 intérpretes. ¿Qué reparto sirve: (a) 1, 1, 1 y 2 o (b) 0, 1, 1 y 3?", "(a)", "(a) incluye un presentador y suma 5; (b) deja al grupo sin presentador."),
        arith("En un grupo de 5 personas, una tiene dos roles (presentador y señal). Si los otros 4 son intérpretes, ¿cuántas personas intervienen como intérpretes?", "5-1", "La persona con dos roles no toca; las demás sí.", " intérpretes"),
    ],
    [arith("Un grupo presenta una canción de 60 segundos con un saludo de 10 segundos y un agradecimiento de 5 segundos. ¿Cuántos segundos dura todo?", "60+10+5", "Se suman la canción, el saludo y el agradecimiento.", " segundos")],
    [ex("¿Quién es la audiencia?", "Las personas que escuchan", "Son quienes reciben la presentación."), ex("¿Qué es el propósito de una presentación?", "Para qué se comparte la música", "Es la razón de presentarla."), ex("¿Qué significa responsabilidad?", "Cumplir lo que prometiste", "Es hacerte cargo de tu parte.")],
    (
        "Con tu grupo (o imaginando uno de 4 a 6 personas), elige una pieza breve que ya conozcan o una de las que crearon en OA 05. Escribe: el propósito, la audiencia, la duración total y quién cumple cada rol (presentador, intérpretes, señal, materiales). Cada persona debe tener al menos un rol. Si alguien prefiere no presentarse ante todos, asígnale un rol de señal o de materiales.",
        "Propósito: mostrar lo aprendido. Audiencia: el curso. Duración: 75 segundos (10 de saludo, 60 de pieza, 5 de agradecimiento). Roles: Ana presenta; Luis y Marta tocan; Pedro da la señal; Sofía, materiales y también toca.",
        ["define propósito y audiencia", "asigna al menos un rol a cada integrante", "calcula la duración total"],
        ["plan escrito"],
        ["dejar a alguien sin rol", "no pensar en la audiencia"],
        "Reconoce el plan claro; si falta algún rol, pregunta quién da la señal o quién cuida los materiales; ofrece alternativas a la exposición individual.",
    ),
    "Escribe tu rol favorito en una presentación y por qué, sin que sea necesario presentarte ante todos.",
    "Imagina una presentación para la comunidad y escribe cómo cambiarías el saludo.",
)

# ---------------------------------------------------------------- OA 06 · clase 2
ENS = [("A", 5, 4), ("B", 5, 2), ("C", 4, 4)]
ENS_TXT = " ".join(f"Sección {s}: {i} intentos, {b} sin errores." for s, i, b in ENS)
ENS_ERR = {s: i - b for s, i, b in ENS}
assert max(ENS_ERR, key=ENS_ERR.get) == "B"

L(
    OA6, 2,
    f"Lápiz y papel. Tabla de ensayo de ejemplo: {ENS_TXT} Para practicar puedes usar una pieza breve ya conocida, a volumen bajo.",
    "Aprenderé a ensayar por secciones y a usar evidencia (intentos sin errores) para decidir qué ensayar más. Sirve para mejorar con orden y sin cansarte.",
    ["Sé dividir una pieza en secciones.", "Sé mi rol en el grupo.", "Sé qué es una evidencia."],
    [
        "Ensayar es repetir para mejorar. Una pieza se ensaya mejor por secciones, es decir, por partes pequeñas como la A, la B y la C, y no siempre completa. Así puedes concentrarte en lo que más cuesta. La evidencia es lo que registras: cuántos intentos hiciste y cuántos salieron sin errores.",
        f"Ejemplo de tabla de ensayo. {ENS_TXT} La sección A tuvo {ENS_ERR['A']} intento con error, la B tuvo {ENS_ERR['B']} y la C tuvo {ENS_ERR['C']}. La sección que más necesita ensayo es la B, porque tuvo más intentos con errores. La C ya está lista.",
        "Después de ensayar por secciones, junta las partes: toca A y B juntas y luego toda la pieza. Cuida la voz y las manos: descansa si te cansas y no repitas hasta el cansancio. Ensayar un poco todos los días rinde más que ensayar mucho un solo día. Cada ensayo debe tener una meta, por ejemplo «hacer la sección B sin errores 3 veces seguidas».",
    ],
    [("ensayar", "repetir para mejorar"), ("sección", "parte de la pieza que se ensaya por separado"), ("evidencia", "datos que registras: intentos y errores"), ("meta", "lo que quieres lograr en el ensayo"), ("juntar", "tocar varias secciones seguidas")],
    [
        ("Elegir qué ensayar", f"{ENS_TXT} ¿Qué sección conviene ensayar primero?", ["Errores: A 1, B 3, C 0.", "Hay más errores en B."], "La sección B"),
        ("Fijar una meta", "Un grupo logró la sección B sin errores 2 veces seguidas. Su meta es 3 veces seguidas. ¿Cuántas veces más debe lograrlo?", ["Meta: 3.", "Lleva 2.", "3 − 2 = 1."], "1 vez más"),
    ],
    [
        ("Ensayar toda la pieza una y otra vez aunque una sección falle siempre.", "No se resuelve la parte difícil.", "Ensaya esa sección sola y luego júntala."),
        ("Decidir «ya está lista» sin registrar nada.", "No hay evidencia.", "Anota intentos y errores antes de decidir."),
    ],
    [
        ex(f"{ENS_TXT} ¿Cuántos intentos hizo la sección C?", "4", "La tabla dice 4 intentos."),
        ex(f"{ENS_TXT} ¿Cuántos intentos sin errores tuvo la sección A?", "4", "La tabla dice 4 sin errores."),
        ex("¿Se ensaya mejor una pieza por secciones o siempre completa?", "Por secciones", "Así te concentras en lo que más cuesta."),
    ],
    [
        ex(f"{ENS_TXT} ¿Cuántos intentos con errores tuvo la sección A?", "1", "Hizo 5 intentos y 4 salieron sin errores."),
        ex(f"{ENS_TXT} ¿Qué sección no tuvo ningún intento con errores?", "La C", "Hizo 4 intentos y los 4 salieron sin errores."),
        ex("Después de ensayar las secciones por separado, ¿qué es lo siguiente: juntarlas o dejar de ensayar?", "Juntarlas", "Hay que comprobar que funcionen en conjunto."),
    ],
    [
        arith(f"{ENS_TXT} ¿Cuántos intentos con errores hubo entre las tres secciones?", "(5-4)+(5-2)+(4-4)", "Se suman los intentos con errores de cada sección.", " intentos"),
        arith(f"{ENS_TXT} ¿Cuántos intentos hicieron en total?", "5+5+4", "Se suman los intentos de las tres secciones.", " intentos"),
        arith("Un grupo ensaya 10 minutos por sección en 3 secciones y deja 5 minutos para juntarlas. ¿Cuántos minutos ensaya?", "3*10+5", "Se suman los ensayos por sección y el tiempo de juntarlas.", " minutos"),
    ],
    [
        ex("Un niño dice: «la sección A tuvo 1 error, entonces la A es la que hay que ensayar más». ¿Qué datos ignora?", "Que la B tuvo más intentos con errores", "La sección B tuvo 3 intentos con errores."),
        ex("Ana ensaya 1 hora seguida el sábado y nada el resto de la semana. Su amiga ensaya 20 minutos al día. ¿Cuál forma ayuda más al cuerpo y a la voz?", "Ensayar poco cada día", "Descansar y repetir un poco cada día rinde más."),
    ],
    [
        ex("Escribe una meta de ensayo adecuada para la sección B: (a) «tocar B bien», (b) «tocar B sin errores 3 veces seguidas».", "(b)", "La (b) es medible: se puede contar si se logró."),
        arith("Para una meta de 3 veces seguidas sin errores, un grupo intenta 6 veces y las 3 últimas salen sin errores. ¿Cuántas salieron con error?", "6-3", "A los intentos totales se les restan los exitosos.", " intentos"),
    ],
    [ex("Antes de presentar, un grupo tiene tres secciones y 15 minutos de ensayo. La sección B es la que falla. ¿Cómo conviene repartir el tiempo: más para B o igual para todas?", "Más para B", "La evidencia muestra que la sección B necesita más ensayo.")],
    [ex("¿Qué es una sección?", "Una parte de la pieza que se ensaya por separado", "Se ensayan las partes más difíciles."), ex("¿Qué es una meta de ensayo?", "Lo que quieres lograr", "Permite saber si avanzaste."), ex("¿Qué datos forman la evidencia?", "Intentos y errores", "Se anotan en la tabla de ensayo.")],
    (
        "Elige una pieza breve de tres secciones que tu grupo conozca (o la que crearon en OA 05). Ensaya cada sección 5 veces y anota en una tabla cuántos intentos salieron sin errores. Usa la evidencia para decidir qué sección ensayar más, fija una meta medible (por ejemplo 3 veces seguidas sin errores) y vuelve a ensayar esa sección. Escribe tu decisión y qué pasó.",
        "Sección A: 5 intentos, 4 sin errores. B: 5 intentos, 2 sin errores. C: 5 intentos, 5 sin errores. Decisión: ensayar B. Meta: 3 veces seguidas sin errores. Después de 6 intentos lo logré.",
        ["registra intentos y errores por sección", "decide con la evidencia", "fija una meta medible", "descansa si se cansa"],
        ["tabla de ensayo", "decisión escrita"],
        ["no registrar los datos", "elegir la sección sin mirar la evidencia"],
        "Reconoce el registro y pide justificar la decisión con los números; sugiere una meta medible si es vaga.",
    ),
    "Cuenta cuántas veces tocas bien una frase de 8 pulsos en 5 intentos.",
    "Ensaya una sección durante 10 minutos con pausas y anota tu progreso.",
)

# ---------------------------------------------------------------- OA 06 · clase 3
TRANS = [("sección 1", 24), ("transición", 5), ("sección 2", 30), ("transición", 5), ("sección 3", 20)]
TRANS_TXT = ", ".join(f"{n}: {s} s" for n, s in TRANS)
TRANS_TOTAL = sum(s for _n, s in TRANS)
TIEMPO_ACORDADO = 90

L(
    OA6, 3,
    f"Lápiz y papel. Programa de ejemplo de una presentación: {TRANS_TXT}. Tiempo acordado para toda la presentación: {TIEMPO_ACORDADO} segundos. Para practicar, usa instrumentos seguros a volumen bajo.",
    "Aprenderé a ajustar las transiciones entre secciones y a cuidar el sonido (volumen) y los instrumentos. Sirve para presentar sin pausas largas ni desorden.",
    ["Sé que una pieza tiene secciones.", "Sé usar una señal de entrada.", "Sé calcular una duración."],
    [
        "Una transición es el paso de una sección a otra. Si no se planea, puede haber silencios largos, golpes, risas o confusión. Para ajustarla, el grupo acuerda qué hace cada persona: quién da la señal, quién cambia de instrumento y cuánto dura el cambio. Una buena transición es corta, silenciosa y avisada por una señal.",
        f"Veamos el programa de ejemplo. {TRANS_TXT}. La suma es {TRANS_TOTAL} segundos y el tiempo acordado es {TIEMPO_ACORDADO}. Por eso sobran {TIEMPO_ACORDADO - TRANS_TOTAL} segundos. Planificar las transiciones ayuda a no pasarse del tiempo.",
        "El cuidado sonoro es tocar a un volumen que no moleste ni dañe los oídos. Una regla simple: si quienes están a un metro de ti no pueden conversar sin gritar, el volumen es demasiado alto. También se cuida el material: los instrumentos se dejan sobre una mesa, no se lanzan y se guardan al terminar. El silencio después de una pieza también es parte de la música.",
    ],
    [("transición", "paso de una sección a otra"), ("señal", "gesto o cuenta que avisa cuándo empezar"), ("cuidado sonoro", "tocar a un volumen seguro para todos"), ("volumen", "qué tan fuerte suena"), ("programa", "orden y duración de las partes de la presentación")],
    [
        ("Calcular el tiempo", f"Programa: {TRANS_TXT}. ¿Cuántos segundos dura toda la presentación?", ["Sumo: 24 + 5 + 30 + 5 + 20.", f"= {TRANS_TOTAL}."], f"{TRANS_TOTAL} segundos"),
        ("Controlar el volumen", "Una persona toca un tambor tan fuerte que quien está a un metro debe gritar para hablar. ¿Debe subir o bajar el volumen?", ["La regla dice que no se puede gritar a un metro.", "Si hay que gritar, el volumen es demasiado alto."], "Bajarlo"),
    ],
    [
        ("Hacer la transición sin avisar.", "El grupo entra desordenado.", "Usa una señal acordada."),
        ("Lanzar el instrumento a la mesa al terminar.", "Se daña y molesta a otros.", "Déjalo con cuidado sobre una mesa o en su lugar."),
    ],
    [
        ex(f"Programa: {TRANS_TXT}. ¿Cuántos segundos dura la sección 2?", "30", "El programa lo indica."),
        ex("¿Qué avisa cuándo empezar la siguiente sección: la señal o el aplauso del público?", "La señal", "La señal ordena la entrada del grupo."),
        ex("¿Qué se debe hacer con los instrumentos al terminar: lanzarlos o dejarlos con cuidado?", "Dejarlos con cuidado", "Cuidar el material evita daños."),
    ],
    [
        ex(f"Programa: {TRANS_TXT}. ¿Cuántas transiciones tiene?", "2", "Aparecen dos veces en el programa."),
        ex("Si quien está a un metro debe gritar para hablarte, ¿tu volumen es seguro o demasiado alto?", "Demasiado alto", "Esa es la regla de la clase."),
        ex("En una buena transición, ¿hay mucho ruido o poco ruido?", "Poco ruido", "Debe ser corta y silenciosa."),
    ],
    [
        arith(f"Programa: {TRANS_TXT}. El tiempo acordado es {TIEMPO_ACORDADO} segundos. ¿Cuántos segundos sobran?", f"{TIEMPO_ACORDADO}-({'+'.join(str(s) for _n, s in TRANS)})", "Se resta la duración del programa al tiempo acordado.", " segundos"),
        arith("Cada transición dura 5 segundos y la presentación tiene 3 secciones. ¿Cuántos segundos hay en transiciones?", "2*5", "Entre 3 secciones hay 2 transiciones de 5 segundos.", " segundos"),
        arith("Un grupo planea dos transiciones de 20 segundos en vez de 5 segundos. ¿Cuántos segundos más dura el programa?", "2*(20-5)", "Cada transición se alarga 15 segundos y son 2.", " segundos más"),
    ],
    [
        arith("Un grupo tiene una sección de 30 segundos que se pasa del tiempo acordado. Quita una repetición de 8 segundos. ¿Cuántos segundos dura ahora?", "30-8", "Se resta la repetición de la duración.", " segundos"),
        ex("Un niño dice: «mientras más fuerte toquemos, mejor se escucha todo». ¿Qué problema tiene eso?", "Puede molestar y dañar los oídos; hay que cuidar el volumen", "El cuidado sonoro importa más que tocar fuerte."),
    ],
    [
        ex("Un grupo toca su última nota y rápidamente empieza a guardar los instrumentos con ruido mientras el público aplaude. ¿Qué parte de su presentación debían cuidar mejor?", "El cierre y el cuidado sonoro después de tocar", "El silencio y el cuidado del material también forman parte de la presentación."),
        arith("Un programa dura 80 segundos y cada transición se acorta de 8 a 5 segundos. Hay 2 transiciones. ¿Cuántos segundos dura ahora el programa?", "80-2*(8-5)", "Cada transición ahorra 3 segundos y son 2.", " segundos"),
    ],
    [ex("Un grupo debe pasar de tocar con palmas a tocar con un tambor. ¿Qué hace más ordenado el cambio: acordar una señal y quién cambia el instrumento, o improvisar cuando llegue el momento?", "Acordar una señal y quién cambia el instrumento", "La señal avisa y el reparto evita el desorden.")],
    [ex("¿Qué es una transición?", "El paso de una sección a otra", "Une las partes."), ex("¿Qué regla sirve para saber si tu volumen es seguro?", "Que puedan conversar a un metro sin gritar", "Si no, es demasiado alto."), ex("¿Cómo debe ser una transición: corta o larga?", "Corta", "Se planea para no perder tiempo.")],
    (
        "Con tu grupo o por escrito, planifica el programa de una presentación de 90 segundos con tres secciones y dos transiciones. Anota la duración de cada parte, la señal que usarán y quién cambia los instrumentos. Comprueba que la suma no pase de 90 segundos. Ensaya una transición en silencio y revisa el volumen con la regla de la conversación a un metro.",
        "Sección 1: 25 s. Transición 1: 5 s (señal con la cabeza, Pedro cambia las cajas). Sección 2: 30 s. Transición 2: 5 s. Sección 3: 20 s. Total: 85 s, sobran 5. Volumen: se puede hablar a un metro sin gritar.",
        ["incluye tres secciones y dos transiciones con sus segundos", "acuerda la señal y quién cambia los instrumentos", "comprueba la suma y el volumen"],
        ["programa escrito", "ensayo de la transición"],
        ["pasarse del tiempo acordado", "no acordar la señal"],
        "Reconoce el programa y pide sumar de nuevo si el total se pasa; sugiere ensayar solo la transición en silencio.",
    ),
    "Cuenta con tu pie 5 pulsos de silencio y empieza a tocar al sexto, como si fuera una transición.",
    "Calcula cuántos segundos ahorra tu grupo si acorta cada transición en 2 segundos.",
)

# ---------------------------------------------------------------- OA 06 · clase 4
COMENT = (
    "Comentario 1: «Me gustó que entraron juntos con la cuenta de 4 pulsos.» "
    "Comentario 2: «Estuvo malo.» "
    "Comentario 3: «Podrían bajar un poco el tambor para que se oiga la voz.» "
    "Comentario 4: «Eres desafinado.»"
)

L(
    OA6, 4,
    f"Lápiz y papel. Comentarios de ejemplo: {COMENT} Si presentas de verdad, hazlo ante tu curso o personas de tu casa, a volumen bajo.",
    "Aprenderé a presentar mi trabajo con un saludo, la pieza y un agradecimiento, y a recibir y dar retroalimentación respetuosa y útil. Sirve para mejorar con ayuda de otras personas.",
    ["Sé ensayar por secciones.", "Sé ajustar transiciones.", "Sé respetar a quien presenta."],
    [
        "Una presentación tiene tres momentos. Primero, el saludo y una frase que dice qué se tocará. Segundo, la pieza, con una señal clara de entrada. Tercero, el agradecimiento, cuando la audiencia aplaude, y la salida ordenada. La audiencia escucha en silencio, aplaude al final y no se burla.",
        f"La retroalimentación es lo que la audiencia le dice al grupo para ayudarlo a mejorar. Un comentario útil es respetuoso, habla de lo que se oyó o vio y no de la persona. {COMENT} El comentario 1 dice algo concreto que funcionó. El 2 no sirve porque no dice qué. El 3 es una sugerencia que se puede aplicar. El 4 habla de la persona y no de la música, por eso no es respetuoso.",
        "Una fórmula simple es dos fortalezas y una sugerencia: primero dices dos cosas que funcionaron y luego una cosa que podría mejorar. Quien recibe los comentarios escucha sin interrumpir, agradece y decide qué usará. Elegir una sugerencia y convertirla en acción, por ejemplo «bajar el tambor», es lo que hace que la retroalimentación sirva.",
    ],
    [("saludo", "las primeras palabras para la audiencia"), ("agradecimiento", "dar las gracias al terminar"), ("retroalimentación", "comentarios para ayudar a mejorar"), ("sugerencia", "idea para mejorar algo"), ("fortaleza", "algo que funcionó bien")],
    [
        ("Clasificar un comentario", f"{COMENT} ¿Qué comentario es una sugerencia aplicable?", ["Una sugerencia propone un cambio concreto.", "El comentario 3 propone bajar el tambor."], "El comentario 3"),
        ("Pasar a la acción", "El comentario dice «podrían bajar el tambor para que se oiga la voz». ¿Qué acción concreta puede hacer el grupo?", ["La sugerencia habla del tambor.", "Hay que tocarlo con menos intensidad."], "Tocar el tambor más suave en el próximo ensayo"),
    ],
    [
        ("Decir «estuvo bueno» o «estuvo malo» sin explicar.", "No dice qué cambiar o mantener.", "Di qué se oyó y qué podría mejorar."),
        ("Hablar de la persona y no de la música.", "Puede dañar y no ayuda a mejorar.", "Habla de lo que se oyó o vio."),
    ],
    [
        ex(f"{COMENT} ¿Qué comentario dice algo concreto que funcionó bien?", "El comentario 1", "Menciona que entraron juntos con la cuenta."),
        ex("¿Qué se hace al terminar la pieza: agradecer o irse sin decir nada?", "Agradecer", "El agradecimiento forma parte de la presentación."),
        ex("¿Cómo debe escuchar la audiencia: en silencio o conversando?", "En silencio", "Así respeta a quienes presentan."),
    ],
    [
        ex(f"{COMENT} ¿Cuál comentario no es respetuoso porque habla de la persona?", "El comentario 4", "Se refiere a la persona y no a la música."),
        ex(f"{COMENT} ¿Qué comentario no sirve para mejorar porque no dice nada concreto?", "El comentario 2", "«Estuvo malo» no dice qué mejorar."),
        ex("Un grupo recibe: «entraron juntos» y «se oyó bien la voz». ¿Qué tipo de comentarios son?", "Fortalezas", "Dicen qué funcionó."),
    ],
    [
        arith("Una presentación tiene un saludo de 10 segundos, una pieza de 60 segundos, un agradecimiento de 5 segundos y 15 segundos para comentarios. ¿Cuántos segundos dura todo?", "10+60+5+15", "Se suman las cuatro partes.", " segundos"),
        arith("Siguiendo «dos fortalezas y una sugerencia», un curso da 3 comentarios por grupo y hay 4 grupos. ¿Cuántos comentarios se dan en total?", "3*4", "Se multiplican los comentarios por los grupos.", " comentarios"),
        ex("Si en el comentario 3 el grupo baja el tambor, ¿qué cualidad del sonido está ajustando?", "La intensidad", "Bajar el tambor es tocar más suave."),
    ],
    [
        ex("Luis recibe una sugerencia y responde enojado «eso no es verdad». ¿Qué debería hacer para sacar provecho?", "Escuchar sin interrumpir, agradecer y decidir qué usar", "Así la retroalimentación le sirve."),
        ex("Un niño dice «tu voz suena como un pato». ¿Es un comentario respetuoso y útil?", "No", "Se burla de la persona y no dice cómo mejorar."),
    ],
    [
        ex("Ordena las tres partes de una presentación: (a) pieza, (b) saludo, (c) agradecimiento.", "b, a, c", "Primero se saluda, luego se toca y al final se agradece."),
        arith("Un grupo recibe 3 sugerencias, aplica 2 en el siguiente ensayo y deja 1 para después. ¿Cuántas sugerencias le quedan por aplicar?", "3-2", "Se restan las aplicadas de las recibidas.", " sugerencia"),
    ],
    [ex("Tras una presentación, un compañero dice: «Me gustó que cuidaron el volumen; podrían mirar a la audiencia al saludar». ¿Qué parte es una fortaleza y qué parte es una sugerencia?", "Fortaleza: cuidaron el volumen; sugerencia: mirar a la audiencia al saludar", "La primera parte dice qué funcionó y la segunda propone mejorar.")],
    [ex("En Música: ¿Qué es la retroalimentación?", "Comentarios para ayudar a mejorar", "Sirve para aprender de los demás."), ex("¿Qué fórmula usa la clase para dar comentarios?", "Dos fortalezas y una sugerencia", "Combina lo bueno con lo que puede mejorar."), ex("¿Se puede burlar de quien presenta?", "No", "Hay que respetar siempre.")],
    (
        "Presenta una pieza breve (la tuya o la del grupo) a una persona de tu casa o a tu curso, a volumen bajo y con saludo, señal de entrada, pieza y agradecimiento. Pide un comentario con la fórmula «dos fortalezas y una sugerencia». Escribe los tres comentarios que recibiste, elige la sugerencia, conviértela en una acción concreta y anota cuándo la aplicarás.",
        "Fortalezas: entraron juntos; se oyó la voz. Sugerencia: mirar a la audiencia al saludar. Acción: en el próximo ensayo practicar el saludo mirando al frente. La aplicaré el jueves.",
        ["presenta con saludo, pieza y agradecimiento", "recibe dos fortalezas y una sugerencia", "convierte la sugerencia en una acción con fecha"],
        ["presentación", "registro escrito de comentarios"],
        ["interrumpir los comentarios", "no pasar a la acción"],
        "Reconoce la acción concreta; si algún comentario es descalificador, ayuda a reformularlo en fortaleza o sugerencia.",
    ),
    "Escribe un comentario de dos fortalezas y una sugerencia para una música que hayas escuchado hoy.",
    "Practica el saludo y el agradecimiento de tu presentación frente a un espejo.",
)
