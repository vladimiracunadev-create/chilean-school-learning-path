"""Student material for 5.º básico Música, OA 04 (canto al unísono y a más voces, e interpretación instrumental) y OA 05 (improvisación y creación con propósito).

Las canciones, partituras y patrones de los ejercicios son originales e inventados; las canciones y repertorio reales los selecciona el docente.
Seguridad: voz sin gritar, volumen cómodo, una flauta dulce nunca se comparte sin limpiarla, baquetas solo sobre el instrumento.
"""
from __future__ import annotations

from student_content_mu5_a import LEY, N, P, L, pulses, sounds
from student_lessons import arith, ex

OA4, OA5 = "MU05 OA 04", "MU05 OA 05"
TA, TT, TAA, SIL = "TA", "ti-ti", "TAA", "SIL"

# ---------------------------------------------------------------- OA 04 · clase 1 (canto al unísono y a más voces)
L(
    OA4, 1,
    "Tu voz, un lugar tranquilo, un vaso de agua a mano y otra persona si quieres cantar acompañada. Canta siempre a un volumen cómodo y sin gritar; descansa si la voz se cansa. Melodía de práctica (números, 1 = do), con un sonido por pulso: 1-2-3-1 | 3-4-5-5 (8 pulsos).",
    "Aprenderé a cantar al unísono y a más voces (canon y ostinato) cuidando la voz y escuchando a los demás. Sirve para que un grupo suene junto y afinado.",
    ["Sé mantener el pulso con las palmas.", "Sé que una melodía tiene sonidos agudos y graves.", "Sé cuidar mi voz sin gritar."],
    [
        "Cantar al unísono es cantar todas las personas la misma melodía a la vez, en la misma altura. Para lograrlo hay que escuchar a quienes te rodean y ajustar tu altura a la del grupo. La buena postura ayuda: espalda recta, hombros relajados y respirar profundo antes de cada frase, sin levantar los hombros.",
        "Cantar a más voces es cantar líneas distintas a la vez. En un canon todas las voces cantan la misma melodía, pero cada voz entra un momento después de la anterior. Por ejemplo, si cada voz entra 4 pulsos después, la voz 2 empieza en el pulso 5 y la voz 3, en el pulso 9. Un ostinato es un patrón corto que se repite una y otra vez mientras otras voces cantan la melodía.",
        "Cantar más voces no es cantar más fuerte. Cada persona debe poder oír a quien tiene al lado; si no la oyes, estás cantando demasiado fuerte. Si algo sale mal, no grites: escucha, vuelve a empezar juntos y ajusta. Cuida tu voz: toma agua y descansa si te duele la garganta.",
    ],
    [("unísono", "todos cantan la misma melodía a la vez"), ("canon", "la misma melodía entra en momentos distintos"), ("ostinato", "patrón corto que se repite sin parar"), ("voz", "cada línea que se canta"), ("afinar", "ajustar la altura para coincidir con el grupo")],
    [
        ("Ubicar una entrada", "En un canon a 3 voces, cada voz entra 4 pulsos después de la anterior. ¿En qué pulso empieza la voz 3?", ["La voz 1 empieza en el pulso 1.", "La voz 2 entra 4 pulsos después: pulso 5.", "La voz 3 entra 4 pulsos después: pulso 9."], "En el pulso 9"),
        ("Contar repeticiones", "Un ostinato de 4 pulsos suena mientras dura una canción de 16 pulsos. ¿Cuántas veces se repite el ostinato?", ["Cada vuelta tiene 4 pulsos.", "16 ÷ 4 = 4."], "4 veces"),
    ],
    [
        ("Cantar más fuerte que el grupo para sonar mejor.", "Si no oyes a los demás, no puedes ajustar tu altura.", "Canta a un volumen en que oigas a quien tienes al lado."),
        ("Gritar para corregir un error.", "Gritar daña la voz y no corrige nada.", "Escucha, para y empieza de nuevo juntos."),
    ],
    [
        ex("Todos cantan la misma melodía a la vez, en la misma altura. ¿Cómo se llama esto?", "Unísono", "Unísono es cantar lo mismo y a la vez."),
        ex("Una voz repite «pa-ra-pa-pam» una y otra vez mientras las demás cantan la melodía. ¿Qué recurso es?", "Ostinato", "Un ostinato es un patrón que se repite."),
        ex("¿Cuántas voces hay en un canon a 3 voces?", "3", "Cada voz es una entrada de la melodía."),
    ],
    [
        ex("¿Cuál es una buena postura para cantar: (a) espalda recta y hombros relajados o (b) cuerpo encorvado?", "(a)", "Facilita respirar y cantar."),
        ex("Para saber si cantas demasiado fuerte, ¿qué compruebas: (a) si oyes a quien tienes al lado o (b) si te oyen desde el patio?", "(a)", "Si no oyes a tu vecino, cantas demasiado fuerte."),
        ex("En un canon, ¿qué hace cada voz: (a) canta lo mismo, pero entra en un momento distinto o (b) canta una melodía diferente?", "(a)", "El canon repite la misma melodía con entradas escalonadas."),
    ],
    [
        arith("Un canon a 3 voces dura 16 pulsos por voz y cada voz entra 4 pulsos después de la anterior. ¿En qué pulso termina la voz 3?", "16+2*4", "La voz 3 empieza 8 pulsos tarde y canta 16: termina en el pulso 24.", ""),
        arith("En un canon a 2 voces la melodía dura 12 pulsos y la voz 2 entra 4 pulsos después. ¿Cuántos pulsos suenan las dos voces a la vez?", "12-4", "Suenan juntas desde la entrada de la voz 2 hasta el final de la voz 1.", " pulsos"),
        ex("Un grupo canta al unísono y suena desafinado. ¿Qué haces primero: (a) gritar más o (b) escuchar y ajustar tu altura?", "(b)", "Escuchar permite acercarte a la altura del grupo."),
    ],
    [
        ex("Luis dice que cantar a dos voces es cantar más fuerte porque hay más personas. ¿Qué es en realidad cantar a dos voces?", "Cantar dos líneas distintas a la vez", "No se trata del volumen, sino del número de líneas."),
        ex("Marta dice que en un canon cada voz canta una melodía distinta. ¿Es cierto?", "No", "Todas cantan la misma melodía, pero entran en momentos distintos."),
    ],
    [
        arith("Un coro de 24 personas se reparte por igual en 3 voces para un canon. ¿Cuántas personas hay en cada voz?", "24//3", "Se reparten las personas en 3 grupos iguales.", " personas"),
        arith("En un canon a 4 voces, cada voz entra 2 compases después de la anterior. La voz 1 empieza en el compás 1. ¿En qué compás empieza la voz 4?", "1+3*2", "Hay 3 entradas posteriores, cada una 2 compases más tarde.", ""),
    ],
    [ex("Una niña canta con su curso y nota que su voz suena más fuerte que la de sus compañeros. ¿Qué debe hacer?", "Bajar el volumen para oír a los demás", "Debe poder oír a los que la rodean.")],
    [ex("¿Qué es un canon?", "La misma melodía con entradas escalonadas", "Cada voz entra después de la anterior."), ex("¿Cantar a más voces es cantar más fuerte?", "No", "Es cantar líneas distintas."), ex("¿Qué haces si tu garganta se cansa?", "Descanso y tomo agua", "Cuidar la voz es parte del canto.")],
    (
        "Con otra persona (o tú solo con una grabación hecha por ti), prueba cantar la melodía 1-2-3-1 | 3-4-5-5 con la sílaba «la» de dos modos: al unísono y en canon a 2 voces, con la segunda voz entrando 4 pulsos después. Escribe en qué pulso entra la voz 2, cuántos pulsos suenan juntas ambas voces y qué hiciste para cuidar tu voz.",
        "Unísono: ambas cantan a la vez. Canon: la voz 2 entra en el pulso 5. La melodía dura 8 pulsos, así que ambas voces suenan juntas 8 − 4 = 4 pulsos. Cuidé la voz cantando suave y tomando agua.",
        ["canta en unísono y en canon", "indica correctamente el pulso de entrada", "calcula los pulsos juntos", "menciona un cuidado de la voz"],
        ["interpretación", "respuestas escritas"],
        ["cantar muy fuerte", "confundir canon con unísono"],
        "Reconoce que cada voz entra a tiempo; pregunta cuántos pulsos suenan juntas ambas voces y cómo supo que cantaba afinado.",
    ),
    "Canta una frase conocida en voz suave y luego repite con una persona al unísono, y di qué te costó más.",
    "Haz un ostinato de 4 pulsos con una sílaba y cántalo mientras alguien más canta una melodía.",
)

# ---------------------------------------------------------------- OA 04 · clase 2 (instrumentos de percusión y melódicos)
MEL = (1, 2, 3, 5)

L(
    OA4, 2,
    f"Lápiz y papel; si tienes un metalófono, una flauta dulce o un teclado, puedes tocar las melodías, pero no es necesario. Cuida el volumen. Escala: 1 = do, 2 = re, 3 = mi, 4 = fa, 5 = sol, 6 = la, 7 = si, 8 = do agudo. Leyenda de ritmo: {LEY}.",
    "Aprenderé a distinguir instrumentos de percusión y melódicos (metalófono, flauta dulce) y a leer notas y ritmos para tocarlos. Sirve para tocar en conjunto con cuidado y precisión.",
    ["Sé el nombre de las notas con números del 1 al 8.", "Sé leer los símbolos de ritmo de la clase.", "Sé que los sonidos pueden ser agudos o graves."],
    [
        "Los instrumentos de percusión se tocan golpeando, sacudiendo o raspando. Algunos no tienen una altura definida: claves, maracas, pandero y triángulo. Otros sí tienen alturas y pueden tocar melodías: el metalófono, con sus barras de metal. Los instrumentos melódicos tocan sobre todo un sonido a la vez y forman melodías: el metalófono y la flauta dulce. Los instrumentos armónicos pueden tocar varios sonidos a la vez: la guitarra y el teclado.",
        "En el metalófono, cada barra suena distinto. Las barras más largas suenan más graves y las más cortas, más agudas. Con la escala de la clase, la barra 1 (do) es la más larga y la barra 8 (do agudo) es la más corta. Se golpea la barra en su centro con una baqueta suave. En la flauta dulce se sopla suave, tapando los agujeros que corresponden; soplar fuerte la hace chillar. Nunca compartas la boquilla de una flauta sin limpiarla.",
        f"Para tocar una melodía, lee las notas y el ritmo. Con los símbolos de la clase, una melodía como {N(*MEL)} se puede tocar con un TA en cada nota. Un instrumento de percusión sin altura toca solo el ritmo; uno melódico toca ritmo y notas. En un conjunto, cada instrumento cumple un papel: el pulso, la melodía o el acompañamiento.",
    ],
    [("percusión", "instrumentos que se tocan golpeando, sacudiendo o raspando"), ("melódico", "toca sobre todo un sonido a la vez y forma melodías"), ("armónico", "puede tocar varios sonidos a la vez"), ("metalófono", "instrumento con barras de metal de distinta altura"), ("baqueta", "palillo con que se golpea un instrumento")],
    [
        ("Clasificar", "Las maracas, el pandero y las claves son instrumentos de percusión. ¿Tienen una altura definida? Responde sí o no.", ["Se usan para marcar el ritmo.", "No producen notas distintas como un metalófono."], "No"),
        ("Leer una barra", "En un metalófono de 8 barras, ¿qué barra es la más corta: la 1 o la 8?", ["La barra más corta es la más aguda.", "El número 8 es el do agudo."], "La barra 8"),
    ],
    [
        ("Golpear el borde de la barra o con fuerza.", "El sonido sale apagado y puede dañar el instrumento.", "Golpea el centro de la barra con una baqueta, de modo suave."),
        ("Soplar fuerte la flauta dulce para que suene más.", "Chilla y suena desafinada.", "Sopla suave y parejo."),
    ],
    [
        ex("¿La flauta dulce es un instrumento de percusión o de viento?", "De viento", "Suena al soplar."),
        ex("¿Las barras más largas de un metalófono suenan más graves o más agudas?", "Más graves", "Mientras más larga, más grave."),
        ex("La guitarra puede tocar varios sonidos a la vez. ¿Es un instrumento melódico o armónico?", "Armónico", "Los armónicos tocan varios sonidos a la vez."),
    ],
    [
        ex("¿Dónde se golpea una barra del metalófono?", "En el centro, con una baqueta suave", "Así suena bien y no se daña."),
        ex(f"Con la escala de la clase, ¿qué barra es la más larga en la melodía {N(*MEL)}?", "La barra 1", "La más larga es la más grave, que es el do (1)."),
        ex(f"¿Cuántas barras distintas golpea quien toca la melodía {N(*MEL)}?", "4", "Toca cuatro notas distintas."),
    ],
    [
        arith("En un grupo de 20 estudiantes, 6 tocan percusión sin altura, 8 tocan metalófonos y el resto flautas dulces. ¿Cuántos tocan flauta?", "20-6-8", "Se restan los otros grupos del total.", " estudiantes"),
        ex(f"Cada nota de la melodía {N(*MEL)} se toca con un TA. ¿Cuántos pulsos dura la melodía?", str(pulses(TA, TA, TA, TA)), "Cuatro TA ocupan 4 pulsos."),
        ex(f"Un percusionista toca el ritmo {P(TA, TT, TAA)} en un pandero. ¿Cuántos sonidos da?", str(sounds(TA, TT, TAA)), "TA da 1, ti-ti da 2 y TAA da 1."),
    ],
    [
        ex("Ana dice que la barra más larga del metalófono suena más aguda. ¿Es cierto?", "No", "La barra más larga suena más grave."),
        ex("Un niño quiere compartir su flauta dulce sin limpiarla. ¿Qué debes decirle?", "Que no se comparte sin limpiar la boquilla", "Por higiene, la boquilla se limpia antes de usarla otra persona."),
    ],
    [
        arith(f"Se toca la melodía {N(1, 2, 3, 5)} con cuatro TA, tres veces seguidas. ¿Cuántos pulsos suenan?", "4*3", "Cada vuelta tiene 4 pulsos y hay tres vueltas.", " pulsos"),
        arith("Un conjunto tiene 3 metalófonos, 4 flautas dulces y 2 panderos. ¿Cuántos instrumentos son melódicos?", "3+4", "Los metalófonos y las flautas son melódicos; los panderos no.", " instrumentos"),
    ],
    [ex("Para tocar el pulso de una canción sin molestar a la melodía, ¿conviene que lo toque (a) un pandero suave o (b) una maraca fuerte?", "(a)", "El pulso debe oírse sin tapar la melodía.")],
    [ex("¿De qué material son las barras del metalófono?", "Metal", "Por eso se llama metalófono."), ex("¿Qué se golpea con una baqueta?", "El instrumento de percusión", "La baqueta golpea la barra o el cuerpo."), ex("¿Una flauta dulce toca un sonido o varios a la vez?", "Un sonido a la vez", "La flauta dulce es un instrumento melódico.")],
    (
        f"Elige un instrumento que tengas en casa o usa tus palmas, tu voz o una caja de cartón. Toca tres veces la melodía {N(*MEL)} con la voz «la», un TA por nota, y la misma melodía en ritmo {P(TA, TT, TAA)} con palmas. Escribe qué instrumento imitarías con cada una (percusión o melódico) y cuántos pulsos suena cada versión.",
        "Melodía 1-2-3-5 con voz (como metalófono): 4 pulsos por vuelta, 12 en 3 vueltas. Ritmo TA – ti-ti – TAA con palmas (como pandero): 4 pulsos por vuelta.",
        ["toca ambas versiones", "clasifica cada una como melódica o de percusión", "calcula los pulsos"],
        ["interpretación", "respuesta escrita"],
        ["confundir percusión con melódico", "contar mal los pulsos"],
        "Reconoce el papel de cada instrumento y pide que cuente en voz alta los pulsos mientras toca.",
    ),
    "Nombra dos instrumentos de percusión y uno melódico.",
    "Con una caja y una cuchara de madera, toca un TA por cada nota de la melodía 1-2-3-5.",
)

# ---------------------------------------------------------------- OA 04 · clase 3 (acompañamiento armónico)
ACORDES = {"Do": (1, 3, 5), "Sol": (5, 7, 2), "Fa": (4, 6, 1)}
PLAN = ["Do", "Do", "Fa", "Do", "Do", "Sol", "Do", "Do"]
PLAN_TXT = " | ".join(PLAN)
CAMBIOS = sum(1 for a, b in zip(PLAN, PLAN[1:]) if a != b)

L(
    OA4, 3,
    f"Lápiz y papel. Notas: 1 = do, 2 = re, 3 = mi, 4 = fa, 5 = sol, 6 = la, 7 = si. Acordes de la clase: Do = {N(*ACORDES['Do'])}, Sol = {N(*ACORDES['Sol'])}, Fa = {N(*ACORDES['Fa'])}. Plan de acordes de una canción de 8 compases: {PLAN_TXT}. Si tienes una guitarra o un teclado, puedes probarlos; no es necesario.",
    "Aprenderé qué es un acorde y cómo un instrumento armónico (guitarra, teclado) acompaña una melodía cambiando de acorde en cada compás. Sirve para acompañar una canción en un grupo.",
    ["Sé que una melodía se escribe con notas.", "Sé que un compás tiene pulsos.", "Sé que la guitarra y el teclado son instrumentos armónicos."],
    [
        "Un acorde son varios sonidos que suenan a la vez. El acorde de Do mayor reúne las notas do, mi y sol (1-3-5). El acorde de Sol reúne sol, si y re (5-7-2) y el acorde de Fa, fa, la y do (4-6-1). Los instrumentos armónicos, como la guitarra y el teclado, pueden tocar acordes completos, por eso sirven para acompañar.",
        f"El acompañamiento arma una base para la melodía. Un plan de acordes dice qué acorde suena en cada compás. En el plan de la clase hay 8 compases: {PLAN_TXT}. Se toca un acorde por compás, por ejemplo 4 golpes seguidos si el compás tiene 4 pulsos. Cada vez que cambia el acorde, el instrumento armónico debe estar preparado un poco antes.",
        "En un conjunto, la melodía va en la voz o en un instrumento melódico, el acompañamiento en un instrumento armónico y el pulso en la percusión. Para que suene bien, el acompañamiento no debe tapar la melodía. Si hay una guitarra, se rasguea suave y parejo. Si hay un teclado, se tocan las notas del acorde juntas, sin golpearlas.",
    ],
    [("acorde", "varios sonidos que suenan a la vez"), ("acompañamiento", "base armónica que apoya la melodía"), ("plan de acordes", "lista de qué acorde suena en cada compás"), ("rasguear", "pasar la mano o la púa sobre las cuerdas de la guitarra"), ("instrumento armónico", "toca varios sonidos a la vez")],
    [
        ("Notas de un acorde", "¿Qué notas forman el acorde de Sol de la clase?", ["Lo dice el acorde de Sol: 5-7-2.", "Son sol, si y re."], "Sol, si y re (5-7-2)"),
        ("Contar cambios", f"En el plan {PLAN_TXT}, ¿cuántas veces cambia el acorde de un compás al siguiente?", ["Do a Do: no cambia.", "Do a Fa: cambia (1).", "Fa a Do: cambia (2).", "Do a Do no cambia.", "Do a Sol: cambia (3).", "Sol a Do: cambia (4).", "Do a Do no cambia."], f"{CAMBIOS} veces"),
    ],
    [
        ("Tocar el acompañamiento más fuerte que la melodía.", "Tapa la melodía, que es la protagonista.", "Toca más suave que quien lleva la melodía."),
        ("Pensar que un acorde es una sola nota.", "Un acorde reúne varios sonidos a la vez.", "Cuenta las notas que suenan juntas."),
    ],
    [
        ex("¿Cuántas notas forman cada acorde de la clase?", "3", "Todos tienen tres notas."),
        ex(f"¿Qué acorde reúne las notas {N(*ACORDES['Fa'])}?", "Fa", "Así está definido en la clase."),
        ex("La guitarra puede tocar varias notas a la vez. ¿Sirve para acompañar?", "Sí", "Un instrumento armónico puede tocar acordes."),
    ],
    [
        ex(f"El plan de la canción es {PLAN_TXT}. ¿Qué acorde suena en el compás 3?", "Fa", "El tercer lugar del plan es Fa."),
        ex(f"El plan de la canción es {PLAN_TXT}. ¿Qué acorde suena en el compás 6?", "Sol", "El sexto lugar del plan es Sol."),
        ex("Una guitarrista rasguea 4 golpes por compás. ¿Cuántos golpes da en 2 compases?", "8", "4 golpes por 2 compases."),
    ],
    [
        arith("Una guitarrista rasguea 4 golpes por compás en una canción de 8 compases. ¿Cuántos golpes da en total?", "4*8", "Se multiplican los golpes por los compases.", " golpes"),
        ex(f"En el plan {PLAN_TXT}, ¿cuántos compases suenan con acorde de Do?", str(PLAN.count("Do")), "Do está en los compases 1, 2, 4, 5, 7 y 8."),
        ex(f"Según las notas de la clase, ¿qué nota comparten los acordes de Do ({N(*ACORDES['Do'])}) y de Fa ({N(*ACORDES['Fa'])})?", "La nota 1 (do)", "Do tiene 1-3-5 y Fa tiene 4-6-1; solo se repite el 1."),
    ],
    [
        ex("Luis dice que un acorde de tres notas es tres acordes. ¿Es cierto?", "No", "Es un solo acorde formado por tres notas que suenan a la vez."),
        ex("Si el acompañamiento suena más fuerte que la melodía, ¿qué debe hacer el guitarrista?", "Tocar más suave", "La melodía debe oírse bien."),
    ],
    [
        arith("Un plan de 8 compases usa Do en 6 compases, Fa en 1 compás y Sol en el resto. ¿Cuántos compases usan Sol?", "8-6-1", "Se restan los compases de Do y de Fa del total.", " compases"),
        arith(f"En el plan {PLAN_TXT} cada compás tiene 4 pulsos. ¿Cuántos pulsos dura la canción?", "8*4", "Hay 8 compases de 4 pulsos.", " pulsos"),
    ],
    [ex("En un grupo, una voz canta, un metalófono toca la melodía y una guitarra rasguea acordes. ¿Cuál de los tres es el instrumento armónico?", "La guitarra", "Puede tocar acordes completos.")],
    [ex("¿Qué es un acorde?", "Varios sonidos que suenan a la vez", "Reúne al menos tres notas."), ex("¿Qué notas tiene el acorde de Do?", "Do, mi y sol", "Así lo define la clase: 1-3-5."), ex("¿Quién lleva la melodía en una guitarra que acompaña?", "Otra voz u otro instrumento", "La guitarra apoya con acordes.")],
    (
        f"Con el plan de acordes {PLAN_TXT} (8 compases de 4 pulsos), haz un acompañamiento con palmas: en los compases con Do da 4 palmas suaves, en los de Fa da 2 palmas y 2 golpes en las rodillas, y en los de Sol da 1 palma y 3 golpes en las rodillas. Escribe cuántas palmas diste en toda la canción y cuántas veces cambió el tipo de golpe.",
        "Do (6 compases): 24 palmas. Fa (1 compás): 2 palmas. Sol (1 compás): 1 palma. Total 24 + 2 + 1 = 27 palmas. El tipo de golpe cambió 4 veces, como los acordes.",
        ["sigue el plan compás por compás", "calcula correctamente las palmas", "cuenta bien los cambios"],
        ["interpretación", "cálculo escrito"],
        ["olvidar un compás", "tocar con más fuerza que quien lleva la melodía"],
        "Reconoce que sigue el plan y pide mostrar con el dedo en el plan dónde está tocando.",
    ),
    "Di cuántas notas tiene un acorde.",
    "Cambia el plan a Do–Sol–Do–Fa y toca el acompañamiento con palmas y rodillas.",
)

# ---------------------------------------------------------------- OA 04 · clase 4 (conjunto: coordinar voces e instrumentos)
PARTES = {"Voz": set(range(1, 9)), "Metalófono": set(range(3, 9)), "Percusión": {1, 2, 3, 4, 7, 8}}
PARTES_TXT = "; ".join(f"{k} toca en los compases {', '.join(str(c) for c in sorted(v))}" for k, v in PARTES.items())
TODOS = sorted(PARTES["Voz"] & PARTES["Metalófono"] & PARTES["Percusión"])
SOLO_PERC_DESC = sorted(set(range(1, 9)) - PARTES["Percusión"])

L(
    OA4, 4,
    f"Lápiz y papel. Es un arreglo inventado de 8 compases de 4 pulsos. {PARTES_TXT}. En los demás compases esa parte descansa (silencio). Cuida el volumen y no compartas boquillas.",
    "Aprenderé a coordinar voz y varios instrumentos en un conjunto: seguir la partitura, entrar a tiempo, contar silencios y escucharnos. Sirve para tocar y cantar juntos con calidad.",
    ["Sé cantar al unísono y en canon.", "Sé diferenciar instrumentos de percusión, melódicos y armónicos.", "Sé contar compases de 4 pulsos."],
    [
        "Un conjunto es un grupo que canta y toca junto. Cada parte tiene un papel: la voz o un instrumento melódico lleva la melodía, un armónico acompaña con acordes y la percusión marca el pulso. Para que suenen juntos, todos siguen un mismo pulso y un mismo tempo. Alguien da la señal de inicio contando 4 pulsos en voz baja («1, 2, 3, 4») antes de empezar.",
        f"En una partitura de conjunto, cada parte tiene su línea y hay compases en que descansa. En el arreglo de la clase: {PARTES_TXT}. Contar los silencios es importante, porque hay que entrar a tiempo después de descansar. Si una parte se pierde, no se detiene a todos: busca el compás en que va el grupo y se incorpora en la siguiente entrada.",
        "Para mejorar el conjunto se ensaya por partes y luego todos juntos. Se graba o se escucha el resultado y se ajusta: ¿entramos juntos?, ¿se oye la melodía?, ¿el volumen es cómodo? Cada persona es responsable de su parte, pero también de escuchar a las demás. Esto se llama tocar con atención al conjunto.",
    ],
    [("conjunto", "grupo que canta y toca junto"), ("parte", "línea que toca cada voz o instrumento"), ("entrada", "momento en que una parte empieza a tocar"), ("silencio", "compás o pulso en que una parte descansa"), ("señal de inicio", "cuenta de 4 pulsos que da quien dirige")],
    [
        ("Compases en que todos tocan", f"{PARTES_TXT}. ¿En qué compases tocan las tres partes a la vez?", ["La voz toca todos.", "El metalófono toca del 3 al 8.", "La percusión toca 1, 2, 3, 4, 7 y 8.", "Los compases comunes son 3, 4, 7 y 8."], f"En los compases {', '.join(str(c) for c in TODOS)}"),
        ("Contar pulsos de silencio", f"{PARTES_TXT}. ¿Cuántos pulsos descansa el metalófono al principio?", ["No toca en los compases 1 y 2.", "Cada compás tiene 4 pulsos.", "2 × 4 = 8."], "8 pulsos"),
    ],
    [
        ("Entrar antes de tiempo después de un silencio.", "Se pierde la sincronía con el grupo.", "Cuenta los compases de silencio y entra en el que te corresponde."),
        ("Detener a todo el grupo cuando una persona se pierde.", "El ensayo se corta para todos.", "Busca el compás en que va el grupo y entra en la siguiente entrada."),
    ],
    [
        ex("¿Qué hace quien da la señal de inicio?", "Cuenta 4 pulsos para que todos empiecen juntos", "Marca el pulso y el tempo."),
        ex(f"{PARTES_TXT}. ¿Toca la voz en el compás 5?", "Sí", "La voz toca en todos los compases."),
        ex(f"{PARTES_TXT}. ¿Toca la percusión en el compás 5?", "No", "La percusión descansa en los compases 5 y 6."),
    ],
    [
        ex(f"{PARTES_TXT}. ¿Cuántos compases toca el metalófono?", str(len(PARTES["Metalófono"])), "Toca del compás 3 al 8."),
        ex(f"{PARTES_TXT}. ¿Cuántos compases descansa la percusión?", str(len(SOLO_PERC_DESC)), "Descansa en los compases 5 y 6."),
        ex(f"{PARTES_TXT}. ¿En qué compás entra el metalófono por primera vez?", "En el compás 3", "Descansa en el 1 y el 2."),
    ],
    [
        arith(f"{PARTES_TXT}. ¿Cuántos pulsos toca la percusión en total (cada compás tiene 4 pulsos)?", f"{len(PARTES['Percusión'])}*4", "Toca en 6 compases de 4 pulsos.", " pulsos"),
        arith(f"{PARTES_TXT}. ¿Cuántos pulsos tocan las tres partes juntas (cada compás tiene 4 pulsos)?", f"{len(TODOS)}*4", "Las tres coinciden en 4 compases de 4 pulsos.", " pulsos"),
        ex(f"{PARTES_TXT}. En el compás 5, ¿qué partes tocan?", "La voz y el metalófono", "La percusión descansa en el compás 5."),
    ],
    [
        ex("Un niño se pierde en el compás 4. ¿Qué es mejor: (a) detener a todos o (b) buscar el compás en que va el grupo y entrar en la siguiente entrada?", "(b)", "Así el conjunto no se detiene."),
        ex("Si todos tocan y no se oye la melodía, ¿qué ajusta el conjunto: el volumen del acompañamiento o el de la melodía?", "El del acompañamiento", "La melodía debe oírse; el acompañamiento baja."),
    ],
    [
        arith("En un conjunto de 18 estudiantes, 8 cantan, 4 tocan metalófono, 3 tocan guitarra y el resto, percusión. ¿Cuántos tocan percusión?", "18-8-4-3", "Se restan los otros grupos del total.", " estudiantes"),
        arith("Un conjunto ensaya 3 veces por semana durante 25 minutos cada vez. ¿Cuántos minutos ensaya en una semana?", "3*25", "Se multiplican los ensayos por los minutos.", " minutos"),
    ],
    [ex("Antes de empezar, una niña cuenta «1, 2, 3, 4» en voz baja para el grupo. ¿Para qué sirve?", "Para que todos empiecen juntos y en el mismo tempo", "Marca el pulso de entrada.")],
    [ex("¿Qué es una parte?", "La línea que toca cada voz o instrumento", "Cada grupo tiene la suya."), ex("¿Qué haces durante un silencio?", "Cuento los compases y espero mi entrada", "Así entro a tiempo."), ex("¿Qué debes cuidar al tocar en conjunto?", "Escuchar a los demás y el volumen", "El conjunto suena bien si nos escuchamos.")],
    (
        f"Con dos o tres personas (o tú solo, cambiando de parte), ensayen el arreglo de la clase: {PARTES_TXT}. La voz canta «la» sobre la melodía 1-2-3-5 en cada compás, el metalófono se imita con un objeto seguro (como una cuchara de madera sobre una caja) y la percusión con palmas. Antes de empezar, cuenten 4 pulsos. Después de tocar, escribe en qué compases hubo más partes juntas y qué ajustaron.",
        "Más partes juntas: compases 3, 4, 7 y 8, con las tres partes. Ajustamos el volumen de las palmas para que se oyera la voz.",
        ["comienzan juntos con la señal de 4 pulsos", "cada parte toca en sus compases", "ajustan algo después de escucharse"],
        ["interpretación", "respuesta escrita"],
        ["no contar los compases de silencio", "tocar más fuerte que la melodía"],
        "Reconoce la sincronía y pregunta qué ajuste hizo el grupo después de escucharse.",
    ),
    "Cuenta «1, 2, 3, 4» y aplaude 8 compases de 4 pulsos con un pulso parejo.",
    "Cambia las partes: la voz descansa en los compases 5 y 6 y cuenta cuántos compases tocan las tres partes juntas.",
)

# ---------------------------------------------------------------- OA 05 · clase 1 (improvisar con un propósito)
CONS = "«Amanecer»: dura 8 pulsos, usa al menos 2 sonidos distintos (palmas, dedos en la mesa o voz) y va de suave a fuerte"
IMP = [
    (1, 8, ["palmas", "voz"], "de suave a fuerte"),
    (2, 8, ["palmas"], "de suave a fuerte"),
    (3, 6, ["dedos", "voz"], "de suave a fuerte"),
    (4, 8, ["dedos", "palmas", "voz"], "de fuerte a suave"),
    (5, 8, ["dedos", "voz"], "de suave a fuerte"),
]


def cumple(dur: int, sonidos: list, direccion: str) -> bool:
    return dur == 8 and len(sonidos) >= 2 and direccion == "de suave a fuerte"


IMP_TXT = " ".join(f"Improvisación {n}: {d} pulsos, sonidos: {', '.join(s)}, {r}." for n, d, s, r in IMP)
CUMPLEN = [n for n, d, s, r in IMP if cumple(d, s, r)]

L(
    OA5, 1,
    f"Tus palmas, tu voz y dedos sobre la mesa (a volumen bajo). Propósito de trabajo: {CONS}. Improvisaciones de ejemplo, descritas por escrito: {IMP_TXT}",
    "Aprenderé a improvisar música con un propósito: partir de una consigna (qué quiero expresar y qué reglas debo cumplir) y decidir mis sonidos sobre la marcha. Sirve para crear con libertad, pero con sentido.",
    ["Sé usar el pulso, la dinámica y el tempo.", "Sé que hay sonidos del cuerpo y de la voz.", "Sé que una música puede expresar una idea."],
    [
        "Improvisar es inventar música en el momento, sin escribirla antes. Crear es inventar música con más tiempo, ensayarla y a veces escribirla. En los dos casos conviene partir de un propósito, que es lo que quiero expresar: un amanecer, una lluvia, una carrera. El propósito se acompaña de reglas, por ejemplo cuánto dura, cuántos sonidos usa y cómo cambia la dinámica.",
        f"Un ejemplo de consigna: {CONS}. Una improvisación cumple la consigna si respeta todas las reglas. Revisa una por una: la duración, la cantidad de sonidos y la dirección de la dinámica. Si falla una sola, no cumple, aunque haya quedado bonita. Improvisar no es tocar cualquier cosa: es tomar decisiones rápidas dentro de reglas.",
        "Para improvisar, mantén el pulso parejo, escucha lo que vas tocando y decide qué viene después. Si te quedas sin ideas, repite lo último que hiciste o cambia solo un elemento, como la fuerza. Y si algo no sale como querías, no pasa nada: se puede intentar de nuevo con una nueva versión.",
    ],
    [("improvisar", "inventar música en el momento"), ("crear", "inventar música con tiempo para ensayarla"), ("propósito", "lo que quiero expresar"), ("consigna", "reglas que debe cumplir una improvisación"), ("decisión musical", "elección de un sonido, ritmo o dinámica")],
    [
        ("Revisar una improvisación", f"{CONS}. Improvisación 3: {IMP[2][1]} pulsos, sonidos: dedos y voz, de suave a fuerte. ¿Cumple la consigna?", ["Duración pedida: 8 pulsos.", "La improvisación 3 dura 6 pulsos.", "Falla una regla."], "No: dura 6 pulsos y debía durar 8"),
        ("Contar las que cumplen", f"{CONS}. {IMP_TXT} ¿Cuáles cumplen todas las reglas?", ["Reviso una por una.", "La 1 cumple las tres reglas.", "La 5 también.", "Las demás fallan una regla."], f"La {CUMPLEN[0]} y la {CUMPLEN[1]}"),
    ],
    [
        ("Creer que improvisar es tocar cualquier cosa.", "Una improvisación con propósito respeta reglas.", "Revisa la consigna mientras improvisas."),
        ("Decir que cumple la consigna porque quedó bonita.", "Hay que revisar cada regla de la consigna.", "Comprueba duración, sonidos y dinámica."),
    ],
    [
        ex("Improvisar es inventar música: ¿en el momento o después de ensayar mucho?", "En el momento", "Esa es la diferencia con crear."),
        ex("¿Qué es el propósito de una improvisación?", "Lo que quiero expresar", "Orienta las decisiones musicales."),
        ex(f"{CONS}. ¿Cuántos pulsos debe durar la improvisación?", "8", "La consigna lo dice."),
    ],
    [
        ex(f"{CONS}. La improvisación 2 usa solo palmas. ¿Cumple la regla de los sonidos distintos?", "No", "Pide al menos 2 sonidos distintos y usa uno."),
        ex(f"{CONS}. La improvisación 4 va de fuerte a suave. ¿Cumple la regla de la dinámica?", "No", "Debía ir de suave a fuerte."),
        ex(f"{CONS}. ¿Cuántas de las cinco improvisaciones de la clase cumplen todas las reglas?", str(len(CUMPLEN)), "Cumplen la 1 y la 5."),
    ],
    [
        ex("Quieres improvisar «una lluvia que empieza fina y termina fuerte». ¿Cómo cambia la dinámica: de suave a fuerte o de fuerte a suave?", "De suave a fuerte", "Empieza fina (suave) y termina fuerte."),
        ex("Te quedas sin ideas improvisando. ¿Qué conviene: (a) parar y salir del grupo o (b) repetir lo último que tocaste o cambiar solo la fuerza?", "(b)", "Repetir o cambiar un elemento mantiene el sentido y el pulso."),
        arith("Una improvisación de 8 pulsos tiene 2 pulsos de silencio. ¿Cuántos pulsos suenan?", "8-2", "Se restan los pulsos de silencio del total.", " pulsos"),
    ],
    [
        ex("Una estudiante improvisó muy bonito, pero 10 pulsos en vez de 8. Dice que cumple igual porque quedó bonito. ¿Cumple?", "No", "La consigna pide 8 pulsos."),
        ex("¿Por qué conviene mantener el pulso parejo al improvisar?", "Porque da una base para decidir qué sigue", "Sin pulso se pierde la organización."),
    ],
    [
        arith("En una sesión, 24 estudiantes improvisan en grupos de 4. ¿Cuántos grupos hay?", "24//4", "Se reparten los estudiantes en grupos de 4.", " grupos"),
        arith("Cada grupo improvisa durante 8 pulsos y hay 6 grupos, uno tras otro, sin pausas. ¿Cuántos pulsos dura toda la sesión?", "8*6", "Se multiplican los pulsos por los grupos.", " pulsos"),
    ],
    [ex("Quieres improvisar «una carrera de hormigas». ¿Qué conviene: (a) sonidos agudos, suaves y rápidos o (b) sonidos graves, fuertes y lentos?", "(a)", "Las hormigas son pequeñas y rápidas.")],
    [ex("¿Qué es una consigna?", "Reglas que debe cumplir la improvisación", "Dice qué cumplir."), ex("¿Qué haces si te quedas sin ideas?", "Repito lo último o cambio un elemento", "Mantengo el sentido."), ex("¿Cuál de las dos incluye ensayar y revisar con más tiempo: improvisar o crear?", "Crear", "Crear incluye ensayo y revisión.")],
    (
        f"Elige una consigna: {CONS}, u otra: «Lluvia»: dura 8 pulsos, usa al menos 2 sonidos distintos y va de suave a fuerte. Improvisa tres veces con tus palmas, tus dedos y tu voz, a volumen bajo. Anota para cada una cuántos pulsos duró, cuántos sonidos distintos usó y si cumplió la consigna. Quédate con la mejor y di por qué.",
        "Intento 1: 8 pulsos, 2 sonidos, de suave a fuerte: cumple. Intento 2: 6 pulsos: no cumple. Me quedo con el 1 porque cumple las tres reglas.",
        ["improvisa tres veces", "revisa las tres reglas en cada intento", "justifica con las reglas"],
        ["interpretación", "registro escrito"],
        ["no contar los pulsos", "decir que cumple solo porque le gustó"],
        "Reconoce el registro y pide mostrar cómo contó los pulsos; si falla una regla, que pruebe otra vez cambiando solo eso.",
    ),
    "Improvisa 4 pulsos con palmas y 4 pulsos con la voz.",
    "Improvisa una carrera de hormigas y escribe qué reglas pusiste.",
)

# ---------------------------------------------------------------- OA 05 · clase 2 (crear ritmos con un compás)
COMP = [
    (1, (TA, TT, TA, TA)), (2, (TA, TA, TAA, TA)), (3, (TT, TA, TA, TA)), (4, (TA, TAA, TT)), (5, (TA, TA, TA, SIL)),
]


def ok_comp(c: tuple) -> bool:
    return pulses(*c) == 4 and c[0] == TA and TT in c


COMP_TXT = " ".join(f"Compás {n}: {P(*c)}." for n, c in COMP)
VALEN = [n for n, c in COMP if ok_comp(c)]
REG2 = "Regla de la clase para «Marcha»: el compás ocupa exactamente 4 pulsos, empieza con TA y lleva al menos un ti-ti"

L(
    OA5, 2,
    f"Lápiz y palmas. Leyenda de ritmo: {LEY}. {REG2}. Compases de ejemplo: {COMP_TXT}",
    "Aprenderé a crear un patrón rítmico de un compás con un propósito, usando los símbolos de ritmo y comprobando que cumpla las reglas. Sirve para crear ritmos propios con precisión.",
    ["Sé contar pulsos de un patrón.", "Sé que un compás tiene un número de pulsos.", "Sé tocar TA, ti-ti, TAA y SIL."],
    [
        f"Para crear un ritmo con propósito se parte de una idea y de reglas. En esta clase el propósito es una «Marcha». {REG2}. Después se arman los símbolos y se comprueba con una suma. Por ejemplo, {P(*COMP[0][1])} ocupa 1 + 1 + 1 + 1 = 4 pulsos, empieza con TA y tiene un ti-ti: cumple las tres condiciones.",
        f"Una creación puede fallar de varias formas. {P(*COMP[1][1])} no cumple porque ocupa 1 + 1 + 2 + 1 = 5 pulsos, uno de más. {P(*COMP[2][1])} no cumple porque empieza con ti-ti. {P(*COMP[4][1])} no cumple porque no tiene ningún ti-ti. Aunque a veces un ritmo suene bien, no cumple la consigna si rompe una regla.",
        "Una vez que tengas un compás, puedes crear una variación: cambiar un símbolo sin romper las reglas. Por ejemplo, de TA – ti-ti – TA – TA puedes pasar a TA – ti-ti – TA – SIL, que también cumple. Toca tus compases con un pulso parejo, a volumen bajo, y revisa en cada uno las tres reglas.",
    ],
    [("compás", "grupo de pulsos del mismo tamaño"), ("consigna rítmica", "reglas que debe cumplir un ritmo creado"), ("variación", "cambio pequeño que mantiene las reglas"), ("marcha", "música de pulso firme para desfilar"), ("comprobar", "revisar que se cumplen las reglas")],
    [
        ("Revisar un compás", f"{REG2}. ¿Cumple el compás {P(*COMP[0][1])}?", ["Pulsos: 1 + 1 + 1 + 1 = 4.", "Empieza con TA.", "Lleva un ti-ti."], "Sí, cumple las tres reglas"),
        ("Descubrir qué falla", f"{REG2}. El compás {P(*COMP[1][1])}, ¿qué regla no cumple?", ["Pulsos: 1 + 1 + 2 + 1 = 5.", "La regla pide 4."], "Ocupa 5 pulsos y no 4"),
    ],
    [
        ("Contar símbolos en vez de pulsos.", "Un TAA ocupa 2 pulsos aunque sea un solo símbolo.", "Suma los pulsos de cada símbolo."),
        ("Olvidar una regla porque suena bien.", "El propósito exige cumplir todas las reglas.", "Revisa una por una antes de decidir."),
    ],
    [
        ex(f"{REG2}. ¿Cuántos pulsos debe ocupar el compás?", "4", "La regla dice exactamente 4 pulsos."),
        ex(f"{REG2}. ¿Con qué símbolo debe empezar el compás?", "TA", "Esa es la segunda regla."),
        ex(f"¿Cuántos pulsos ocupa {P(*COMP[3][1])}?", str(pulses(*COMP[3][1])), "TA 1, TAA 2 y ti-ti 1."),
    ],
    [
        ex(f"{REG2}. ¿Cumple el compás {P(*COMP[2][1])}?", "No", "Empieza con ti-ti y debe empezar con TA."),
        ex(f"{REG2}. ¿Cumple el compás {P(*COMP[4][1])}?", "No", "No lleva ningún ti-ti."),
        ex(f"{REG2}. Compases de la clase: {COMP_TXT} ¿Cuántos compases cumplen las tres reglas?", str(len(VALEN)), "Cumplen el 1 y el 4."),
    ],
    [
        ex(f"{REG2}. ¿Cumple el compás {P(*COMP[3][1])}?", "Sí", "Ocupa 4 pulsos, empieza con TA y lleva un ti-ti."),
        ex("Completa el compás TA – ti-ti – ___ para que ocupe 4 pulsos con un solo símbolo. ¿Qué símbolo falta?", "TAA", "Hasta ahora ocupa 2 pulsos y faltan 2, que es lo que dura un TAA."),
        arith(f"Una persona repite {P(*COMP[0][1])} cuatro veces. ¿Cuántos pulsos toca?", f"{pulses(*COMP[0][1])}*4", "Cada compás ocupa 4 pulsos.", " pulsos"),
    ],
    [
        ex("Una niña dice que TA – TA – TA – TA cumple la regla de la marcha porque empieza con TA y ocupa 4 pulsos. ¿Qué regla no cumple?", "Le falta un ti-ti", "No lleva ningún ti-ti."),
        ex("Cambia solo el tercer símbolo de TA – TA – TA – TA por un ti-ti para que cumpla las tres reglas. ¿Cómo queda?", "TA – TA – ti-ti – TA", "Un ti-ti ocupa 1 pulso, así que sigue ocupando 4 pulsos, empieza con TA y ahora lleva ti-ti."),
    ],
    [
        arith(f"Compases de la clase: {COMP_TXT} Si se tocan en orden el compás 1, el 4 y el 1 de nuevo, ¿cuántos pulsos suenan?", "4+4+4", "Cada compás que cumple la regla ocupa 4 pulsos.", " pulsos"),
        arith(f"El compás {P(*COMP[0][1])} tiene 5 sonidos. Se toca 3 veces. ¿Cuántos sonidos suenan?", f"{sounds(*COMP[0][1])}*3", "Una vuelta tiene 1 + 2 + 1 + 1 sonidos.", " sonidos"),
    ],
    [ex("Para una marcha en el patio se necesita un ritmo firme y claro. ¿Qué conviene más: (a) TA – TA – TA – TA o (b) tiri-tiri – tiri-tiri – tiri-tiri – tiri-tiri?", "(a)", "Los pulsos firmes y claros sirven para marchar.")],
    [ex("¿Cuántos pulsos ocupa un compás de la marcha de la clase?", "4", "Es la primera regla."), ex("¿Cuánto ocupa un TAA?", "2 pulsos", "Es un sonido largo."), ex("¿Qué haces para comprobar un ritmo?", "Sumo los pulsos y reviso las reglas", "Así compruebo la consigna.")],
    (
        f"Crea un ritmo de 2 compases para la «Marcha». {REG2}. Cada compás debe ser distinto del otro. Escríbelos con los símbolos, comprueba con una suma que cada uno ocupa 4 pulsos y tócalos con tus palmas varias veces. Escribe cuál de los dos te gustó más y qué reglas cumple.",
        "Compás 1: TA – ti-ti – TA – TA (4 pulsos). Compás 2: TA – TA – ti-ti – SIL (4 pulsos). Ambos empiezan con TA y llevan ti-ti.",
        ["dos compases distintos", "cada uno ocupa 4 pulsos", "ambos empiezan con TA y tienen ti-ti", "comprueba con una suma"],
        ["ritmo escrito", "interpretación con palmas", "suma escrita"],
        ["contar símbolos en vez de pulsos", "olvidar el ti-ti"],
        "Reconoce la comprobación y pide que muestre la suma de cada compás con el dedo.",
    ),
    "Escribe un compás de 4 pulsos con TA, ti-ti y TAA.",
    "Crea una variación de tu compás cambiando solo un símbolo y comprueba que sigue cumpliendo.",
)

# ---------------------------------------------------------------- OA 05 · clase 3 (crear una melodía con reglas)
PENTA = (1, 2, 3, 5, 6)
CANDI = {1: (1, 2, 3, 5, 2, 1), 2: (1, 2, 4, 3, 2, 1), 3: (1, 3, 5, 6, 5, 3), 4: (1, 1, 2, 3, 2, 1), 5: (2, 3, 5, 6, 3, 1)}


def ok_mel(m: tuple) -> bool:
    return len(m) == 6 and m[0] == 1 and m[-1] == 1 and all(x in PENTA for x in m)


MEL_TXT = " ".join(f"Melodía {n}: {N(*m)}." for n, m in CANDI.items())
VALIDAS = [n for n, m in CANDI.items() if ok_mel(m)]
REG3 = "Regla de la clase para «Lluvia suave»: 6 notas, solo las notas 1, 2, 3, 5 y 6, que empiece y termine en 1"

L(
    OA5, 3,
    f"Lápiz y papel; si tienes un instrumento melódico, puedes tocar tus melodías, pero también puedes cantarlas con «la». Notas: 1 = do, 2 = re, 3 = mi, 4 = fa, 5 = sol, 6 = la. {REG3}. Melodías de ejemplo: {MEL_TXT}",
    "Aprenderé a crear e improvisar una melodía corta usando un conjunto de notas y reglas (pentatónica), comprobando que cumpla su propósito. Sirve para inventar melodías que suenen bien juntas.",
    ["Sé leer notas con números.", "Sé qué es una frase musical.", "Sé qué es empezar y terminar en la misma nota."],
    [
        "Una melodía creada con propósito parte de un conjunto de notas. En esta clase usamos las notas 1, 2, 3, 5 y 6 (do, re, mi, sol, la), llamadas escala pentatónica. Es fácil improvisar con ellas porque suenan bien en casi cualquier orden. Las notas 4 y 7 no están en este conjunto.",
        f"Las reglas dan forma a la melodía. {REG3}. Terminar en 1 hace sentir que la melodía llega a un descanso. Para comprobar una melodía, revisa que tenga 6 notas, que todas pertenezcan al conjunto y que empiece y termine en 1. Por ejemplo, {N(*CANDI[1])} cumple las tres cosas. En cambio {N(*CANDI[2])} no cumple porque usa el 4.",
        "Una buena melodía también tiene un diseño: puede subir, bajar y volver. Prueba dibujar la melodía como una línea que sube y baja. Después, crea una variación cambiando una o dos notas sin romper las reglas. Si puedes cantarla o tocarla, escucha cómo suena y ajusta lo que no te guste.",
    ],
    [("pentatónica", "conjunto de cinco notas: 1, 2, 3, 5 y 6"), ("conjunto de notas", "notas permitidas para crear"), ("diseño melódico", "forma que dibuja la melodía"), ("variación", "cambio pequeño que mantiene las reglas"), ("comprobar", "revisar que se cumple cada regla")],
    [
        ("Revisar una melodía", f"{REG3}. ¿Cumple la melodía {N(*CANDI[1])}?", ["Tiene 6 notas.", "Las notas son 1, 2, 3, 5, 2 y 1: todas son del conjunto.", "Empieza y termina en 1."], "Sí, cumple las reglas"),
        ("Encontrar el error", f"{REG3}. La melodía {N(*CANDI[2])}, ¿qué regla rompe?", ["Usa el 4.", "El 4 no está en el conjunto."], "Usa la nota 4, que no está en el conjunto"),
    ],
    [
        ("Terminar en cualquier nota.", "La regla pide terminar en 1 para llegar a un descanso.", "Comprueba la primera y la última nota."),
        ("Usar notas de afuera del conjunto.", "Rompe la regla del conjunto de notas.", "Comprueba cada nota con la lista 1, 2, 3, 5 y 6."),
    ],
    [
        ex(f"{REG3}. ¿Con qué nota debe empezar la melodía?", "1", "Es la primera regla de inicio."),
        ex("¿Cuántas notas tiene el conjunto pentatónico de la clase?", "5", "Son 1, 2, 3, 5 y 6."),
        ex(f"{REG3}. ¿Está la nota 4 en el conjunto?", "No", "El conjunto son las notas 1, 2, 3, 5 y 6."),
    ],
    [
        ex(f"{REG3}. ¿Cumple la melodía {N(*CANDI[3])}?", "No", "Termina en 3 y debe terminar en 1."),
        ex(f"{REG3}. ¿Cumple la melodía {N(*CANDI[5])}?", "No", "Empieza en 2 y debe empezar en 1."),
        ex(f"{REG3}. Melodías de la clase: {MEL_TXT} ¿Cuántas cumplen todas las reglas?", str(len(VALIDAS)), "Cumplen la 1 y la 4."),
    ],
    [
        ex(f"{REG3}. ¿Cumple la melodía {N(*CANDI[4])}?", "Sí", "Tiene 6 notas del conjunto, empieza y termina en 1."),
        ex(f"Cambia solo la cuarta nota de {N(*CANDI[1])} por un 6, sin romper las reglas. ¿Cómo queda?", N(1, 2, 3, 6, 2, 1), "Se reemplaza la cuarta nota y las demás quedan igual."),
        ex(f"En la melodía {N(*CANDI[4])}, ¿cuál es la nota más aguda?", "3", "Es el número mayor de la lista."),
    ],
    [
        ex("Un niño dice que la melodía 1-2-3-5-6-1 cumple las reglas. ¿Tiene razón?", "Sí", "Tiene 6 notas del conjunto y empieza y termina en 1."),
        ex("Una melodía parte en 1, sube hasta 6 y termina en 1, con 6 notas. ¿Puede tener un 4 sin romper la regla?", "No", "El 4 no pertenece al conjunto."),
    ],
    [
        arith("Una melodía de 6 notas se toca con un TA por nota y se repite 3 veces. ¿Cuántos pulsos suenan?", "6*3", "Cada vuelta ocupa 6 pulsos.", " pulsos"),
        ex("Una melodía parte en 1, sube por grados a 2 y a 3, y luego salta al 5. ¿Cuántos saltos (pasos de dos o más números) tiene hasta ahora?", "1", "Los pasos 1→2 y 2→3 son de un grado; solo 3→5 es un salto."),
    ],
    [ex("Para una canción de cuna se quiere que la melodía termine con sensación de descanso. ¿En qué nota conviene terminar: 1 o 5?", "1", "Terminar en 1 da sensación de llegada.")],
    [ex("¿Cuántas notas tiene la melodía de la clase?", "6", "Es la regla de largo."), ex("¿Con qué nota empieza y termina?", "1", "Es la regla."), ex("¿Qué conjunto de notas se usa?", "1, 2, 3, 5 y 6", "Es la pentatónica de la clase.")],
    (
        f"Crea una melodía para «Lluvia suave» que cumpla: {REG3}. Escribe tres versiones y marca cuáles cumplen las reglas. Elige la que más te guste y cántala o tócala varias veces. Escribe por qué la elegiste y cómo la variaste.",
        "Versión A: 1-2-3-5-2-1 (cumple). Versión B: 1-3-5-6-5-1 (cumple). Versión C: 1-2-4-3-2-1 (no cumple). Elijo B porque sube y baja suave. La variaría cambiando la cuarta nota.",
        ["tres versiones escritas", "marca correctamente las que cumplen", "justifica la elección", "propone una variación"],
        ["melodías escritas", "interpretación"],
        ["usar la nota 4", "no terminar en 1"],
        "Reconoce la comprobación y pide que señale qué nota rompe la regla en las versiones que no cumplen.",
    ),
    "Escribe una melodía de 6 notas que empiece y termine en 1 y use solo el 1 y el 3.",
    "Canta tu melodía y dibuja su diseño con una línea que sube y baja.",
)

# ---------------------------------------------------------------- OA 05 · clase 4 (forma, motivo y variación)
CRIT5 = ["propósito escrito en una frase", "forma definida (por ejemplo ABA)", "un cambio de dinámica planeado", "un motivo que vuelve", "dura lo acordado"]
CUMP5 = {"P": {1, 2, 4, 5}, "Q": {1, 3}}
BORR5 = "Borrador P: propósito escrito, forma ABA, un motivo que vuelve y dura lo acordado, pero sin cambio de dinámica. Borrador Q: propósito escrito y cambio de dinámica planeado, pero sin forma definida, sin motivo y sin la duración acordada."
CRIT5_TXT = ", ".join(f"({i}) {c}" for i, c in enumerate(CRIT5, 1))

L(
    OA5, 4,
    f"Lápiz y palmas. Criterios de revisión de la clase: {CRIT5_TXT}. Borradores de ejemplo (descritos por escrito): {BORR5}",
    "Aprenderé a organizar una creación breve con una forma, un motivo que vuelve y una dinámica planeada, y a revisarla con criterios. Sirve para mejorar una creación con decisiones claras.",
    ["Sé reconocer formas como ABA.", "Sé qué es un motivo y una variación.", "Sé cambiar la dinámica."],
    [
        "Una creación breve se organiza con un plan. Primero, el propósito: qué quiero expresar. Segundo, la forma: cómo se ordenan las secciones, por ejemplo ABA. Tercero, el motivo: una idea corta que vuelve, a veces con una variación. Cuarto, la dinámica: dónde suena suave, fuerte o cambia poco a poco. Quinto, la duración: cuántos pulsos o segundos dura.",
        f"Revisar es comparar la creación con criterios. Los criterios de la clase son: {CRIT5_TXT}. Cada criterio cumplido suma un punto. {BORR5} El borrador P cumple 4 de 5. El borrador Q cumple 2 de 5.",
        "Después de revisar se decide qué mejorar. No hace falta cambiar todo: elige el criterio que falta y arréglalo. Para el borrador P, agrega un crescendo en la sección B. Para el Q, define una forma ABA, incluye un motivo y acuerda la duración. Toca de nuevo y vuelve a revisar. Una creación final es el resultado de varias versiones.",
    ],
    [("forma", "orden de las secciones"), ("motivo", "idea musical corta que vuelve"), ("dinámica planeada", "decisión de dónde suena suave, fuerte o cambia"), ("criterio", "pregunta con que se revisa la creación"), ("borrador", "versión de prueba que aún se puede mejorar")],
    [
        ("Contar criterios", f"{BORR5} ¿Cuántos de los cinco criterios cumple el borrador P y cuál le falta?", ["Propósito: sí.", "Forma: sí.", "Dinámica: no.", "Motivo: sí.", "Duración: sí."], "Cumple 4; le falta la dinámica planeada"),
        ("Decidir qué mejorar", f"{BORR5} Para mejorar el borrador P, ¿qué se agrega?", ["Le falta el criterio 3.", "Se agrega un cambio de dinámica planeado."], "Un cambio de dinámica planeado"),
    ],
    [
        ("Cambiar todo el borrador por un solo problema.", "Se pierde lo que ya funciona.", "Arregla solo el criterio que falta."),
        ("Terminar sin revisar con los criterios.", "No sabes si cumple lo que te propusiste.", "Revisa los cinco criterios antes de dar por terminada la creación."),
    ],
    [
        ex("¿Cuántos criterios tiene la revisión de la clase?", "5", "Son propósito, forma, dinámica, motivo y duración."),
        ex(f"{BORR5} ¿Qué forma tiene el borrador P?", "ABA", "Lo dice la descripción."),
        ex("¿Qué es un motivo?", "Una idea musical corta que vuelve", "Se repite o se varía a lo largo de la creación."),
    ],
    [
        ex(f"{BORR5} ¿Cuántos criterios cumple el borrador Q?", str(len(CUMP5["Q"])), "Cumple el propósito escrito y el cambio de dinámica."),
        ex(f"{BORR5} ¿Cuál es el único criterio que le falta al borrador P?", "El cambio de dinámica planeado", "Cumple los otros cuatro."),
        ex(f"{BORR5} ¿Cuántos criterios le faltan al borrador Q?", str(5 - len(CUMP5["Q"])), "Le faltan la forma, el motivo y la duración."),
    ],
    [
        arith("Un borrador cumplía 2 criterios y, después de mejorarlo, cumple 5. ¿Cuántos criterios agregó?", "5-2", "Se resta lo que cumplía antes de lo que cumple ahora.", " criterios"),
        arith("Una creación ABA tiene A de 8 pulsos y B de 4 pulsos. ¿Cuántos pulsos dura en total?", "8+4+8", "La A suena dos veces; se suman las tres secciones.", " pulsos"),
        ex("Una creación ABA acordó durar 20 pulsos y su A dura 6. Si la B dura 8, ¿cumple lo acordado?", "Sí", "6 + 8 + 6 = 20 pulsos."),
    ],
    [
        ex("Una niña dice que su creación ya está terminada porque le gustó. ¿Qué debe revisar antes?", "Si cumple los criterios", "Gustar no basta para saber si cumple lo que se propuso."),
        ex("Un motivo de 4 pulsos aparece 3 veces en una creación de 20 pulsos. ¿Cuántos pulsos ocupan los motivos en total?", "12", "4 pulsos por 3 veces son 12 pulsos."),
    ],
    [
        arith("Una creación de 24 pulsos usa 3 motivos distintos de 4 pulsos cada uno y el resto es silencio. ¿Cuántos pulsos de silencio hay?", "24-3*4", "Se restan los pulsos de los motivos del total.", " pulsos"),
        arith("Un grupo revisa 6 borradores con 5 criterios cada uno. ¿Cuántas revisiones de criterio hace?", "6*5", "Se multiplican los borradores por los criterios.", " revisiones"),
    ],
    [ex("Quieres que una creación sobre una tormenta termine suave y calmada. ¿Qué dinámica planeas al final: (a) ff o (b) p?", "(b)", "Suave y calmada corresponde a p.")],
    [ex("¿Qué forma define el borrador P?", "ABA", "Lo dice la ficha."), ex("En Música: ¿Qué es un criterio?", "Una pregunta con que se revisa", "Sirve para evaluar."), ex("¿Qué haces después de revisar?", "Mejoro el criterio que falta", "Es el paso siguiente.")],
    (
        "Crea una pieza breve de forma ABA de 12 pulsos en total, con tus palmas y tu voz (a volumen bajo). Define un propósito en una frase, un motivo de 4 pulsos que vuelva al final, una dinámica planeada (por ejemplo p – < – f) y revísala con los cinco criterios. Escribe cuántos cumple tu primera versión y qué mejoraste.",
        "Propósito: despedir el día. Motivo: TA – TA – TT – SIL. Forma ABA con 4 pulsos cada sección. Dinámica p – < – f – p. Total 12 pulsos. Primera versión cumplía 4 de 5 (faltaba el cambio de dinámica); lo agregué y ahora cumple 5.",
        ["propósito en una frase", "forma ABA de 12 pulsos", "motivo que vuelve", "dinámica planeada", "revisa con criterios"],
        ["pieza interpretada", "revisión escrita"],
        ["no ajustar la duración", "no revisar con los cinco criterios"],
        "Reconoce el plan y pide mostrar los 12 pulsos con un dibujo de tres cajas.",
    ),
    "Escribe una frase que sea el propósito de una creación.",
    "Mejora tu pieza agregando una variación del motivo en la última sección.",
)

# ---------------------------------------------------------------- OA 05 · clase 5 (comunicar y explicar la creación)
GRAF = [("p", (TA, TA, TA, SIL)), ("<", (TT, TT, TA, SIL)), ("f", (TAA, TAA))]
GRAF_TXT = " | ".join(f"{d}: {P(*t)}" for d, t in GRAF)
GRAF_TOT = sum(pulses(*t) for _d, t in GRAF)

L(
    OA5, 5,
    f"Lápiz y papel; palmas y voz a volumen bajo. Partitura gráfica de ejemplo (cada sección lleva su dinámica y su ritmo): {GRAF_TXT}. Leyenda de ritmo: {LEY}.",
    "Aprenderé a anotar mi creación con una partitura gráfica y a explicar mis decisiones musicales usando el lenguaje de la música (pulso, ritmo, dinámica, forma). Sirve para que otras personas puedan tocar y entender mi creación.",
    ["Sé crear un ritmo con reglas.", "Sé revisar con criterios.", "Sé leer p, f y las flechas de dinámica."],
    [
        "Una partitura gráfica es una forma sencilla de anotar una creación con símbolos que cualquiera pueda leer. En la de la clase, cada sección lleva primero su dinámica y después su ritmo: " + GRAF_TXT + ". La dinámica p significa suave, el signo « < » es crescendo y f es fuerte.",
        f"Con esa partitura, otra persona puede tocar tu creación sin que estés presente. Esta pieza tiene tres secciones y ocupa 4 + 4 + 4 = {GRAF_TOT} pulsos. Primero suena suave con TA – TA – TA – SIL; luego sube poco a poco con ti-ti – ti-ti – TA – SIL; y termina fuerte con dos TAA. Para anotar bien, escribe los símbolos en orden y sin dejar dudas.",
        "Además de anotar, hay que poder explicar las decisiones. Una buena explicación dice qué decidiste y por qué, usando lenguaje musical: «Elegí empezar suave (p) y subir hasta fuerte (f) para mostrar un amanecer». Una explicación débil solo dice «me gustó». Presentar tu creación y explicarla con respeto ayuda a que otras personas la comprendan.",
    ],
    [("partitura gráfica", "anotación sencilla de la música con símbolos"), ("explicar una decisión", "decir qué elegí y por qué"), ("lenguaje musical", "palabras de la música: pulso, ritmo, dinámica, forma"), ("sección", "parte de la creación"), ("propósito", "lo que quiero expresar")],
    [
        ("Leer una partitura", f"Partitura: {GRAF_TXT}. ¿Cuántos pulsos ocupa en total?", [f"Primera sección: 1 + 1 + 1 + 1 = {pulses(*GRAF[0][1])}.", f"Segunda: 1 + 1 + 1 + 1 = {pulses(*GRAF[1][1])}.", f"Tercera: 2 + 2 = {pulses(*GRAF[2][1])}.", f"Total {GRAF_TOT}."], f"{GRAF_TOT} pulsos"),
        ("Elegir la mejor explicación", "¿Cuál explica mejor una decisión: (a) «Me gustó así» o (b) «Subí de p a f para mostrar un amanecer»?", ["(a) solo dice un gusto.", "(b) dice qué se hizo y para qué, con lenguaje musical."], "(b)"),
    ],
    [
        ("Anotar sin orden, de modo que nadie entienda.", "La partitura debe poder leerse sin ayuda.", "Escribe los símbolos en el orden en que suenan."),
        ("Explicar solo con «me gustó».", "No muestra qué decidiste.", "Di qué elegiste y para qué."),
    ],
    [
        ex(f"Partitura: {GRAF_TXT}. ¿Con qué dinámica empieza la creación?", "p", "La primera sección es p."),
        ex(f"Partitura: {GRAF_TXT}. ¿Con qué dinámica termina la creación?", "f", "La tercera sección es f."),
        ex("¿Qué indica el signo « < » en una partitura gráfica?", "Que el sonido sube poco a poco", "Es el crescendo."),
    ],
    [
        ex(f"Partitura: {GRAF_TXT}. ¿Cuántos pulsos ocupa la primera sección?", str(pulses(*GRAF[0][1])), "Los tres TA y el silencio ocupan 1 pulso cada uno."),
        ex(f"Partitura: {GRAF_TXT}. ¿Qué símbolo tiene la última sección: TA o TAA?", "TAA", "La última sección tiene dos TAA."),
        ex("¿Cuál es una explicación con lenguaje musical: (a) «Está linda» o (b) «Usé un crescendo para que se sintiera cada vez más cerca»?", "(b)", "Nombra una decisión musical y su razón."),
    ],
    [
        arith(f"Partitura: {GRAF_TXT}. Si se toca dos veces completa, ¿cuántos pulsos suenan?", f"{GRAF_TOT}*2", "Una vuelta ocupa 12 pulsos y se repite.", " pulsos"),
        ex(f"Partitura: {GRAF_TXT}. ¿Cuántos sonidos suenan en la segunda sección?", str(sounds(*GRAF[1][1])), "Cada ti-ti son 2 sonidos (2 + 2) y el TA suma 1; el silencio no suena."),
        ex("Completa: «Elegí ___ para mostrar un amanecer». ¿Qué opción tiene sentido: (a) empezar en p y subir a f o (b) empezar en f y bajar a p?", "(a)", "Un amanecer va de poca luz a mucha."),
    ],
    [
        ex("Un niño explica su creación diciendo solo «es bonita». ¿Qué debería agregar para que sea una explicación musical?", "Qué decidió y por qué, usando lenguaje musical", "Una decisión musical se explica con razones."),
        ex("Una creación está anotada en desorden: primero la sección fuerte y luego la suave, pero suena al revés. ¿Qué problema tiene la partitura?", "No sigue el orden en que suenan las secciones", "La partitura debe escribirse en el orden en que suena."),
    ],
    [
        arith("Un curso presenta 8 creaciones. Cada estudiante explica su creación en 2 minutos y se dedican 3 minutos en total a los saludos. ¿Cuántos minutos dura la presentación?", "8*2+3", "Se suman las explicaciones y los saludos.", " minutos"),
        ex("Una creación de 12 pulsos dura 6 segundos. ¿A cuántos pulsos por segundo va?", "2", "12 pulsos en 6 segundos son 2 pulsos cada segundo."),
    ],
    [ex("Quieres que otra persona toque tu creación sin que estés presente. ¿Qué necesitas: (a) una partitura gráfica clara o (b) recordarla de memoria?", "(a)", "La partitura permite repetirla sin que estés presente.")],
    [ex("¿Para qué sirve una partitura gráfica?", "Para anotar la creación y que otros la toquen", "Guarda lo que se creó."), ex("¿Qué dice una buena explicación musical?", "Qué decidí y por qué", "Usa lenguaje musical."), ex("¿Qué dinámica tiene « < »?", "Crescendo", "Sube poco a poco.")],
    (
        "Anota tu creación (puedes usar una de las clases anteriores) en una partitura gráfica de tres secciones, con su dinámica y su ritmo, como la de la clase. Tócala. Luego explica en 3 frases tres decisiones que tomaste, con lenguaje musical: una sobre la dinámica, una sobre el ritmo y una sobre la forma. Cada frase debe empezar con «Elegí… porque…».",
        "Elegí empezar en p porque quería mostrar un amanecer suave. Elegí ti-ti en la segunda sección porque quería más movimiento. Elegí terminar en f porque el amanecer termina con mucha luz.",
        ["la partitura tiene tres secciones con dinámica y ritmo", "las tres frases explican decisiones con «porque»", "usa lenguaje musical"],
        ["partitura escrita", "frases escritas", "interpretación"],
        ["explicar con «me gustó»", "partitura sin orden"],
        "Reconoce las decisiones y pregunta qué cambiaría si el propósito fuera otro.",
    ),
    "Escribe una explicación de una decisión musical con «porque».",
    "Entrega tu partitura a otra persona y observa si la toca como querías; anota qué ajustarías.",
)
