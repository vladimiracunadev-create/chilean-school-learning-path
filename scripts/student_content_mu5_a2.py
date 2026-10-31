"""Student material for 5.º básico Música, OA 01 (clases 3 a 5: variación, dinámica y tempo, formas y texturas).

Todas las músicas de los ejercicios son descripciones o patrones originales inventados para esta clase; las audiciones reales las selecciona el docente.
"""
from __future__ import annotations

from student_content_mu5_a import NOTAS, OA1, L, N, diff
from student_lessons import arith, ex

# ---------------------------------------------------------------- OA 01 · clase 3 (reiteración, contraste, variación, pregunta-respuesta)
Fa, Fe, Fd = (1, 2, 3, 1), (1, 2, 4, 1), (8, 7, 6, 5)
FQ = (1, 2, 3, 5)
REGLA = "si no cambia ningún lugar es repetición (reiteración); si cambian 1 o 2 de los 4 lugares es variación; si cambian 3 o 4 lugares es contraste"


def recurso(a: tuple, b: tuple) -> str:
    d = diff(a, b)
    return "Repetición" if d == 0 else "Variación" if d <= 2 else "Contraste"


L(
    OA1, 3,
    f"Lápiz y papel. Escala: {NOTAS}. Regla de la clase para frases de 4 notas: {REGLA}. Todas las frases están escritas con números.",
    "Aprenderé a comparar frases melódicas para decidir si hay repetición (reiteración), contraste o variación, y a reconocer la pregunta y la respuesta musicales. Sirve para explicar cómo está armada una melodía.",
    ["Sé que la melodía se escribe con números del 1 al 8.", "Sé comparar dos listas de números.", "Sé que una frase es un grupo corto de sonidos."],
    [
        f"Una música se arma con frases, que son grupos cortos de sonidos. Para comparar dos frases, mira lugar por lugar qué notas cambian. Regla de la clase: {REGLA}. Por ejemplo, {N(*Fa)} y {N(*Fe)} cambian en un solo lugar (la tercera nota): es variación. En cambio {N(*Fa)} y {N(*Fd)} cambian los cuatro lugares: es contraste.",
        "El contraste también puede ser de otras cualidades: una frase suave y luego una fuerte, una de flauta y luego una de tambor, una lenta y luego una rápida. La repetición da sensación de orden y de algo conocido. El contraste da sorpresa. La variación mantiene lo conocido, pero lo hace nuevo.",
        f"La pregunta y respuesta es otra forma de organizar frases. La pregunta termina en una nota que deja la sensación de «¿y qué más?», como el 5. La respuesta termina en la nota 1, que da sensación de llegada. Ejemplo: pregunta {N(*FQ)} y respuesta {N(*Fa)}. Cambian solo la última nota, así que la respuesta es una variación de la pregunta.",
    ],
    [("repetición (reiteración)", "una frase vuelve igual"), ("contraste", "llega algo muy distinto"), ("variación", "vuelve casi igual, con una parte cambiada"), ("pregunta y respuesta", "una frase que queda abierta y otra que la cierra"), ("frase", "grupo corto de sonidos que forma una idea musical")],
    [
        ("Clasificar con la regla", f"Frase 1: {N(*Fa)}. Frase 2: {N(1, 3, 3, 2)}. ¿Repetición, variación o contraste?", ["Compara lugar por lugar: 1 y 1 igual; 2 y 3 cambia; 3 y 3 igual; 1 y 2 cambia.", "Cambian 2 lugares.", "Con 1 o 2 cambios es variación."], "Variación"),
        ("Reconocer la respuesta", f"Pregunta: {N(*FQ)}. ¿Cuál es una buena respuesta: (a) {N(1, 2, 3, 1)} o (b) {N(1, 2, 3, 6)}?", ["La pregunta termina en 5 (abierta).", "La respuesta debe terminar en 1.", "La (a) termina en 1."], "(a)"),
    ],
    [
        ("Llamar contraste a toda frase que cambia un poco.", "Con uno o dos cambios la frase sigue reconociéndose: es variación.", "Cuenta los lugares que cambian y aplica la regla."),
        ("Pensar que la respuesta debe terminar igual que la pregunta.", "Si termina igual, no cierra: la respuesta termina en 1.", "Pregunta abierta en 5; respuesta cerrada en 1."),
    ],
    [
        ex("Dos frases son idénticas de principio a fin. ¿Hay repetición, variación o contraste?", "Repetición", "No cambia ningún lugar."),
        ex("Una frase termina en la nota 5 y deja la sensación de «falta algo». ¿Es pregunta o respuesta?", "Pregunta", "La nota 5 deja la frase abierta."),
        ex("Después de una frase suave llega otra muy distinta, fuerte y de otro instrumento. ¿Qué recurso aparece?", "Contraste", "Cambian varias cualidades a la vez."),
    ],
    [
        ex(f"Compara {N(*Fa)} con {N(*Fe)}. ¿Cuántos lugares cambian?", str(diff(Fa, Fe)), "Solo cambia la tercera nota, de 3 a 4."),
        ex(f"Compara {N(*Fa)} con {N(*Fd)}. ¿Qué recurso hay según la regla de la clase?", recurso(Fa, Fd), "Cambian los cuatro lugares."),
        ex(f"Pregunta: {N(*FQ)}. ¿Cuál cierra como respuesta: (a) {N(1, 2, 4, 3)} o (b) {N(1, 2, 3, 1)}?", "(b)", "La respuesta termina en 1; la (a) termina en 3."),
    ],
    [
        ex(f"Una pieza tiene la frase 1: {N(*Fa)}, la frase 2: {N(*Fa)}, la frase 3: {N(*Fe)} y la frase 4: {N(*Fd)}. ¿Qué recurso hay entre la frase 2 y la 3?", "Variación", "Solo cambia un lugar."),
        ex(f"En la misma pieza (frases {N(*Fa)}, {N(*Fa)}, {N(*Fe)}, {N(*Fd)}), ¿qué recurso hay entre la frase 3 y la 4?", recurso(Fe, Fd), "Cambian los cuatro lugares."),
        ex(f"Escribe la frase que resulta de cambiar solo la tercera nota de {N(*Fa)} por un 5.", N(1, 2, 5, 1), "Se reemplaza la tercera nota y las demás quedan igual."),
    ],
    [
        ex(f"Marta toca {N(*Fa)} con flauta y luego {N(*Fa)} con violín. Dice que hay contraste. ¿Qué se repite y qué contrasta?", "Se repite la melodía y contrasta el timbre", "Las notas son las mismas; cambia el instrumento."),
        ex(f"Pregunta: {N(*FQ)}. Respuesta: {N(*Fa)}. ¿En cuántos lugares se diferencian y qué relación tiene la respuesta con la pregunta?", "En 1 lugar; la respuesta es una variación de la pregunta", "Cambia solo la última nota, de 5 a 1."),
    ],
    [
        arith("Una pieza tiene 5 frases de 4 compases cada una. Dos de ellas son repeticiones exactas de la primera y las otras dos son distintas entre sí y de la primera. ¿Cuántos compases son material distinto?", "(5-2)*4", "Las frases distintas son 3 y cada una tiene 4 compases.", " compases"),
        ex(f"Escribe una respuesta a la pregunta {N(2, 3, 4, 5)} que cambie solo la última nota y termine en 1.", N(2, 3, 4, 1), "Se cambia solo el último lugar por 1 para cerrar."),
    ],
    [ex(f"En un juego de eco, una niña canta {N(5, 3, 1, 5)} y otro responde {N(5, 3, 1, 1)}. ¿En cuántos lugares cambia la respuesta y cómo se llama esta organización?", "En 1 lugar; pregunta y respuesta", "Termina en 5 la pregunta y en 1 la respuesta.")],
    [ex("¿Cómo se llama que una frase vuelva casi igual con una parte cambiada?", "Variación", "Cambia una parte, pero se reconoce."), ex("¿En qué nota termina una respuesta que cierra?", "1", "El 1 da sensación de llegada."), ex("¿Qué recurso mantiene lo conocido pero lo hace nuevo?", "Variación", "Repite lo esencial y cambia un detalle.")],
    (
        "Crea una pregunta y una respuesta de 4 notas con números del 1 al 5. La pregunta debe terminar en 5 y la respuesta en 1, y la respuesta debe cambiar solo 1 o 2 lugares de la pregunta. Escríbelas, cuenta los lugares que cambian y di qué recurso hay entre ellas. Si puedes, cántalas con «la».",
        "Pregunta: 1-3-2-5. Respuesta: 1-3-2-1. Cambia 1 lugar (el último): variación y pregunta-respuesta.",
        ["la pregunta termina en 5 y la respuesta en 1", "cambian solo 1 o 2 lugares", "cuenta los cambios y nombra el recurso"],
        ["melodías escritas", "conteo de cambios"],
        ["cambiar más de dos lugares y llamarlo variación", "terminar la respuesta en la misma nota de la pregunta"],
        "Reconoce el cierre en 1; pide comparar lugar por lugar con el dedo para contar los cambios.",
    ),
    "Escribe una frase de 4 notas y otra que sea su repetición exacta.",
    "Escribe tres frases: una repetición, una variación y un contraste de la frase 1-2-3-1.",
)

# ---------------------------------------------------------------- OA 01 · clase 4 (dinámica, tempo y propósito expresivo)
L(
    OA1, 4,
    "Lápiz, tus palmas y un reloj con segundero, o cuenta «mil uno, mil dos…» como un segundo cada uno. Cuida el volumen: nunca más fuerte que una conversación animada.",
    "Aprenderé a leer la dinámica (de pp a ff, con crescendo y diminuendo) y el tempo (lento, andante, allegro, acelerando, ritardando), y a elegirlos según lo que la música quiere expresar. Sirve para que la música diga lo que quiero.",
    ["Sé que fuerte y suave son intensidades.", "Sé qué es un pulso.", "Sé que rápido y lento hablan de la velocidad del pulso."],
    [
        "La dinámica es cómo cambia la intensidad de la música. Se escribe con letras de menos a más fuerte: pp (muy suave), p (suave), mf (medio fuerte), f (fuerte) y ff (muy fuerte). Una flecha que se abre « < » es crescendo: sube poco a poco. Una flecha que se cierra « > » es diminuendo: baja poco a poco.",
        "El tempo es qué tan rápido va el pulso. En las partituras se usan palabras en italiano: lento es muy pausado, andante es a paso de caminata y allegro es rápido. Acelerando es ir cada vez más rápido y ritardando, cada vez más lento. Si das 2 pulsos por segundo, en 10 segundos das 20. Si das 1 por segundo, solo 10.",
        "Dinámica y tempo son distintos: se puede tocar fuerte y lento, o suave y rápido. También sirven para expresar algo. Una canción para dormir suena tranquila con p y lento. Una marcha para animar suena enérgica con f y allegro. Para decidir, pregúntate qué quieres que sienta quien escucha y elige la dinámica y el tempo que lo logran.",
    ],
    [("dinámica", "cómo cambia la intensidad"), ("pp, p, mf, f, ff", "muy suave, suave, medio fuerte, fuerte, muy fuerte"), ("crescendo / diminuendo", "sube / baja poco a poco"), ("tempo", "qué tan rápido va el pulso"), ("lento, andante, allegro", "lento, a paso de caminata, rápido"), ("acelerando / ritardando", "cada vez más rápido / cada vez más lento")],
    [
        ("Calcular una duración", "Una marcha tiene 48 pulsos y va a 2 pulsos por segundo. ¿Cuántos segundos dura?", ["Cada segundo pasan 2 pulsos.", "Se reparten 48 pulsos de a 2 por segundo.", "48 ÷ 2 = 24."], "24 segundos"),
        ("Elegir según el propósito", "Una pieza debe sonar como una canción para calmar a un bebé. ¿Qué eliges: (a) ff y allegro o (b) p y lento?", ["Calmar pide poca intensidad.", "También pide un pulso tranquilo.", "Eso es p y lento."], "(b)"),
    ],
    [
        ("Pensar que crescendo significa ir más rápido.", "El crescendo cambia la intensidad, no la velocidad.", "Ir más rápido se llama acelerando."),
        ("Creer que lento significa suave.", "Lento habla del pulso y suave habla de la intensidad.", "Pregunta por separado: ¿cuán fuerte?, ¿cuán seguidos van los pulsos?"),
    ],
    [
        ex("Ordena de más suave a más fuerte: f, p, ff, mf.", "p, mf, f, ff", "Es el orden de la escala de intensidades."),
        ex("¿Qué significa la palabra allegro en una partitura?", "Rápido", "Es la palabra italiana para un tempo rápido."),
        ex("La flecha « < » entre p y f, ¿qué hace con la intensidad?", "Sube poco a poco", "Es un crescendo."),
    ],
    [
        ex("¿Qué significa mf?", "Medio fuerte", "Está entre p y f."),
        ex("En ritardando, ¿qué pasa con los pulsos en cada segundo?", "Hay cada vez menos", "El pulso se va haciendo más lento."),
        ex("Una canción para dormir busca calma. ¿Qué conviene: (a) p y lento o (b) f y allegro?", "(a)", "Suave y lento transmiten tranquilidad."),
    ],
    [
        arith("Una pieza tiene 40 pulsos y va a 2 pulsos por segundo. ¿Cuántos segundos dura?", "40//2", "Se reparten los pulsos entre los que pasan en cada segundo.", " segundos"),
        arith("La misma pieza de 40 pulsos va ahora a 1 pulso por segundo. ¿Cuántos segundos más dura que a 2 pulsos por segundo?", "40//1-40//2", "A 1 por segundo dura 40 s y a 2 por segundo dura 20 s; se restan.", " segundos más"),
        ex("Escribe con signos una música que parta en p, suba poco a poco hasta ff y quede en ff.", "p – < – ff", "Parte suave, la flecha abierta sube y llega a muy fuerte."),
    ],
    [
        ex("Rosa dice: «acelerando es lo mismo que crescendo». ¿Qué cambia en cada uno?", "Acelerando cambia la velocidad; crescendo cambia la intensidad", "Uno habla del tempo y el otro de la dinámica."),
        arith("Dos versiones de una melodía de 24 pulsos: A va a 1 pulso por segundo y B a 2 pulsos por segundo. ¿Cuántos segundos antes termina B?", "24//1-24//2", "A dura 24 s y B dura 12 s; se restan.", " segundos antes"),
    ],
    [
        ex("Un grupo debe terminar su pieza de 40 pulsos en 20 segundos exactos. ¿Cuántos pulsos por segundo debe dar?", "2", "40 pulsos en 20 segundos son 2 pulsos cada segundo."),
        ex("Una marcha de 16 pulsos va a 1 pulso por segundo, pero al final hace un ritardando. ¿Dura más o menos de 16 segundos?", "Más de 16 segundos", "Al ir cada vez más lento, los últimos pulsos tardan más de un segundo cada uno."),
    ],
    [ex("Una pieza para despedir con ternura a un compañero que se cambia de colegio debe sonar tranquila. ¿Eliges (a) ff y allegro o (b) p y andante?", "(b)", "Suave y a paso de caminata transmiten ternura y calma.")],
    [ex("¿Qué letras significan muy suave y muy fuerte?", "pp y ff", "Las letras se repiten para decir «muy»."), ex("¿Qué cambia un diminuendo?", "La intensidad, que baja poco a poco", "Es una dinámica."), ex("Más pulsos en el mismo tiempo, ¿es más lento o más rápido?", "Más rápido", "El tempo habla de cuántos pulsos hay.")],
    (
        "Elige un propósito: dormir a un bebé, animar una carrera o despedir a un amigo. Toca el patrón TA – TA – TA – SIL con palmas, tres veces seguidas, con la dinámica y el tempo que expresen ese propósito. Escribe con signos la dinámica (por ejemplo p – < – mf), nombra el tempo (lento, andante o allegro) y explica en una frase por qué esa elección expresa tu propósito.",
        "Propósito: animar una carrera. Dinámica mf – < – f, tempo allegro. Es rápido y sube de fuerza, como quien acelera hacia la meta.",
        ["elige un propósito", "escribe una dinámica con signos y un tempo", "explica por qué expresan el propósito"],
        ["interpretación con palmas", "signos escritos", "explicación breve"],
        ["usar f para algo que pide calma", "confundir tempo con intensidad al explicar"],
        "Reconoce el propósito y pregunta qué cambiaría si la música fuera al revés (por ejemplo, fuerte y rápida para dormir).",
    ),
    "Di una frase en voz suave y luego en voz fuerte y escribe p y f en el orden en que sonaron.",
    "Aplaude tres veces un patrón con acelerando y dibuja una flecha o línea que muestre cómo se acorta el tiempo entre aplausos.",
)

# ---------------------------------------------------------------- OA 01 · clase 5 (secciones y texturas)
S1 = [("A", "flauta sola, suave", 8), ("B", "flauta con guitarra que toca acordes, algo más fuerte", 12), ("A", "flauta sola, suave", 8)]
S1_TXT = "; ".join(f"sección {i}: {d}, {n} pulsos" for i, (_l, d, n) in enumerate(S1, 1))
S1_TOTAL = sum(n for *_x, n in S1)

L(
    OA1, 5,
    "Lápiz y papel. Las músicas están descritas por escrito, con secciones marcadas con letras. Para practicar puedes aplaudir una sección suave y otra fuerte, y cantar una melodía sola o con otra persona que lleve el pulso.",
    "Aprenderé a reconocer las formas A, AB, ABA y otras (como ABACA) y las texturas (melodía sola, melodía con acompañamiento y varias melodías a la vez). Sirve para explicar cómo está construida una música y qué efecto tiene.",
    ["Sé reconocer repetición y contraste.", "Sé sumar pulsos.", "Sé que una melodía es una sucesión de sonidos."],
    [
        "Una sección es una parte de la música con carácter propio. La forma es el orden en que aparecen las secciones. A es la primera sección; si llega una distinta, es B; si llega otra distinta, es C. Con A sola, la forma es A. Con A y B, es AB. Si la A vuelve al final, es ABA. Hay otras formas, como ABACA o rondó, donde la A vuelve varias veces entre secciones distintas.",
        f"La textura es cómo se combinan las líneas sonoras. Hay tres básicas. Melodía sola: una sola línea, aunque la canten muchas personas al unísono (monofonía). Melodía con acompañamiento: una línea principal y otra que la apoya, como una voz con guitarra (homofonía). Varias melodías a la vez: líneas distintas que suenan juntas, como un canon (polifonía). Ejemplo de la clase: {S1_TXT}. Tiene forma ABA, y la textura cambia de melodía sola a melodía con acompañamiento y vuelve.",
        "La forma y la textura se eligen para expresar algo. Una sección con más instrumentos suena más llena y festiva. Volver a la sección A da sensación de regreso y de calma. Para describir una música, di su forma, su textura en cada sección y qué efecto tienen.",
    ],
    [("sección", "parte de la música con carácter propio"), ("forma", "orden de las secciones"), ("ABA / ABACA (rondó)", "vuelve la A / la A vuelve varias veces"), ("textura", "cómo se combinan las líneas sonoras"), ("melodía sola, con acompañamiento, varias melodías a la vez", "tres texturas básicas"), ("canon", "la misma melodía entra en momentos distintos")],
    [
        ("Forma y total", f"Una música tiene {S1_TXT}. ¿Qué forma tiene y cuántos pulsos dura en total?", ["Ordeno: A, B, A.", f"Total: 8 + 12 + 8 = {S1_TOTAL}."], f"ABA; {S1_TOTAL} pulsos"),
        ("Reconocer textura", "Un coro de 20 personas canta la misma melodía a la vez, sin instrumentos. ¿Qué textura tiene: melodía sola o varias melodías a la vez?", ["Hay una sola línea melódica.", "Que muchas personas la canten no crea otra línea."], "Melodía sola"),
    ],
    [
        ("Pensar que muchas voces siempre son varias melodías.", "Si todos cantan lo mismo a la vez, hay una sola línea.", "Cuenta las líneas distintas, no las personas."),
        ("Decir que ABACA es igual a ABA.", "ABACA tiene una sección distinta más y la A suena tres veces.", "Cuenta las letras distintas y cuántas veces suena la A."),
    ],
    [
        ex("Una música tiene una sola sección. ¿Qué forma tiene?", "A", "Una sección es forma A."),
        ex("Una voz canta y una guitarra toca acordes que la acompañan. ¿Qué textura hay?", "Melodía con acompañamiento", "Hay una línea principal apoyada por otra."),
        ex("En la forma ABACA, ¿qué sección suena más veces?", "La A", "La A suena tres veces."),
    ],
    [
        ex("En ABACA, ¿cuántas secciones distintas hay?", "3", "Son A, B y C."),
        ex("Tres grupos cantan la misma melodía, pero cada uno entra un momento después del anterior. ¿Qué textura es?", "Varias melodías a la vez", "Es un canon: las entradas desfasadas superponen la melodía."),
        ex(f"En la música de la clase ({S1_TXT}), ¿qué textura tiene la sección 2?", "Melodía con acompañamiento", "La flauta lleva la melodía y la guitarra acompaña."),
    ],
    [
        ex(f"Una música tiene {S1_TXT}. ¿En cuántas de sus tres secciones suena la melodía sola?", "2", "Suena sola en las secciones 1 y 3."),
        arith("Una música A–B–A–B tiene secciones de 8 pulsos cada una. ¿Cuántos pulsos dura?", "8*4", "Hay cuatro secciones de 8 pulsos.", " pulsos"),
        ex("Una música tiene las secciones A, B y A. ¿Cuál es su forma escrita con cajas?", "A | B | A", "Una caja por sección, en el orden en que suenan."),
    ],
    [
        ex("Pedro dice que ABA y ABACA son la misma forma porque ambas empiezan y terminan en A. ¿Qué diferencia hay?", "ABACA tiene una sección más (C) y la A suena tres veces", "ABA tiene dos secciones distintas y ABACA tiene tres."),
        ex("Un trío toca tres melodías diferentes al mismo tiempo. Otra pieza tiene una voz sola. ¿Cuál tiene más líneas sonoras y cuántas más?", "El trío, con 2 líneas más", "Tres líneas menos una línea son dos más."),
    ],
    [
        arith("Una pieza ABACA tiene A de 8 pulsos, B de 6 y C de 6. ¿Cuántos pulsos dura en total?", "8*3+6+6", "La A suena tres veces; se suman B y C.", " pulsos"),
        ex("Una pieza ABA quiere que su parte central suene más llena y festiva que el inicio. ¿Qué textura conviene en B: melodía sola o melodía con acompañamiento?", "Melodía con acompañamiento", "Sumar un acompañamiento hace sonar más llena la sección."),
    ],
    [ex("Para un acto escolar se compone una pieza que debe terminar con sensación de regreso y de calma. ¿Qué forma conviene: (a) AB o (b) ABA?", "(b)", "Al volver la A se siente que se regresa al inicio.")],
    [ex("¿Qué es la textura de una música?", "Cómo se combinan las líneas sonoras", "Es la combinación de melodías y acompañamientos."), ex("¿Cuántas veces suena la A en ABA?", "2", "Al inicio y al final."), ex("Un canon, ¿tiene una o varias melodías sonando a la vez?", "Varias melodías a la vez", "La misma melodía suena desfasada.")],
    (
        "Crea una pieza de forma ABA con tu voz y tus palmas. La A es suave y dura 4 pulsos: solo la voz canta «la» sobre una melodía corta. La B es más fuerte y dura 4 pulsos: la voz sigue cantando «la» y las palmas marcan el pulso. Vuelve la A. Escribe la forma con cajas, la textura de cada sección y el total de pulsos.",
        "Forma A | B | A. A: solo la voz, melodía sola; B: voz con melodía y palmas que marcan el pulso, melodía con acompañamiento; A igual a la primera. Total 4 + 4 + 4 = 12 pulsos.",
        ["la forma es ABA con A igual al inicio y al final", "la B contrasta en intensidad o textura", "escribe la textura de cada sección y el total correcto"],
        ["interpretación", "dibujo de cajas", "cálculo escrito"],
        ["que B suene casi igual que A", "contar mal los pulsos del total"],
        "Reconoce que la A vuelve igual y pregunta qué hizo distinta a la B; revisa el total sumando de a una sección.",
    ),
    "Canta una frase conocida sola y luego con otra persona que lleve el pulso con palmas; di cuál es melodía sola y cuál con acompañamiento.",
    "Crea una pieza ABACA con tres sonidos del cuerpo distintos y escribe cuántos pulsos dura si cada sección dura 4.",
)
