"""Student material for 6.º básico Música, OA 05 (improvisar y crear ideas musicales con un propósito dado y un adecuado dominio del lenguaje musical).

Todas las ideas musicales son melodías numeradas (1 = do … 8 = do agudo), patrones rítmicos con figuras o descripciones originales inventadas para esta clase.
"""
from __future__ import annotations

from student_content_mu6_a import BLA, BP, CC, LEY, NEG, NOTAS, RED, SB, SN, L, N, P, leaps, moves, pulses, sounds
from student_lessons import arith, ex

OA5 = "MU06 OA 05"
PENTA = {1, 2, 3, 5, 6}


def cumple(m: tuple, ini: int = 1, fin: int = 1, tope: int = 5, saltos: int = 2, largo: int = 8) -> bool:
    return len(m) == largo and m[0] == ini and m[-1] == fin and max(m) <= tope and leaps(m) <= saltos


def en_penta(m: tuple) -> bool:
    return set(m) <= PENTA and len(m) == 8 and m[-1] == 1


def cual(candidatos: dict, prueba) -> str:
    buenos = [k for k, v in candidatos.items() if prueba(v)]
    assert len(buenos) == 1, buenos
    return buenos[0]


# ---------------------------------------------------------------- OA 05 · clase 1 (improvisar con un propósito)
IA, IB, IC = (1, 3, 5, 6, 5, 3, 2, 1), (1, 3, 4, 5, 6, 5, 3, 1), (1, 2, 3, 5, 6, 5, 3, 2)
CAND1 = {"A": IA, "B": IB, "C": IC}
REG1 = "reglas de la improvisación de práctica: 8 notas de un pulso cada una; solo las notas 1, 2, 3, 5 y 6; terminar en 1; pulso estable"

L(
    OA5, 1,
    f"Lápiz y papel; tu voz o un instrumento melódico si hay. Notas: {NOTAS}. {REG1}. Cuida el volumen.",
    "Aprenderé a improvisar con un propósito dado y con reglas claras: inventar música en el momento sin salirme del plan. Sirve para crear con libertad y orden a la vez.",
    ["Sé que una melodía se escribe con números.", "Sé que el pulso es el latido parejo.", "Sé qué es la dinámica y el tempo."],
    [
        "Improvisar es inventar música en el momento, sin escribirla antes. No es tocar cualquier cosa: una buena improvisación tiene un propósito, por ejemplo «una tormenta que se acerca», y reglas que ordenan lo que haces. Las reglas ayudan a tener ideas, porque limitan las opciones y permiten concentrarte en lo que quieres expresar.",
        f"Una regla muy útil es elegir pocas notas. En esta clase usamos solo cinco: 1, 2, 3, 5 y 6 (do, re, mi, sol y la). Esa escala se llama pentatónica y tiene la ventaja de que casi cualquier combinación suena bien, porque no tiene notas que choquen entre sí. Otras reglas son mantener el pulso y terminar en 1, que da sensación de llegada. {REG1}.",
        "Para que la improvisación exprese el propósito se eligen la dinámica y el tempo: una tormenta que se acerca pide crescendo y accelerando, y una noche tranquila pide p y tempo lento. Después de improvisar, se revisa: ¿cumplí las reglas?, ¿se oyó el propósito? Improvisar es distinto de componer: al improvisar no puedes borrar, y al componer pruebas, escribes y corriges.",
    ],
    [("improvisar", "inventar música en el momento, con propósito y reglas"), ("propósito", "lo que quiero expresar con la música"), ("pentatónica", "escala de cinco notas que casi siempre suena bien"), ("regla", "condición que ordena lo que se improvisa"), ("componer", "crear música probando, escribiendo y corrigiendo")],
    [
        ("Revisar con las reglas", f"Improvisación: {N(2, 3, 5, 6, 5, 3, 2, 1)}. ¿Cumple las reglas de práctica?", ["Tiene 8 notas.", "Usa solo 2, 3, 5 y 6, que están permitidas.", "Termina en 1."], "Sí, cumple las tres reglas"),
        ("Detectar un error", f"Improvisación: {N(1, 2, 4, 5, 6, 5, 3, 1)}. ¿Qué regla no cumple?", ["Tiene 8 notas y termina en 1.", "El 4 no está en el grupo de notas permitidas."], "Usa la nota 4, que no está permitida"),
    ],
    [
        ("Pensar que improvisar es tocar al azar.", "Improvisar tiene propósito y reglas.", "Antes de empezar, di el propósito y las reglas."),
        ("Parar apenas hay una nota equivocada.", "Al improvisar se sigue con el pulso y se corrige en la siguiente frase.", "Mantén el pulso y vuelve a las notas permitidas."),
    ],
    [
        ex("Inventar música en el momento, ¿es improvisar o componer en partitura?", "Improvisar", "Se hace en el momento, sin escribir antes."),
        ex("¿La nota 4 está permitida en las reglas de práctica de la clase?", "No", "Las notas permitidas son 1, 2, 3, 5 y 6."),
        ex("Si el propósito es «una tormenta que se acerca», ¿qué dinámica conviene: crescendo o diminuendo?", "Crescendo", "La tormenta que se acerca suena cada vez más fuerte."),
    ],
    [
        ex(f"¿Cuál de estas improvisaciones cumple las reglas de práctica: A {N(*IA)}, B {N(*IB)} o C {N(*IC)}?", cual(CAND1, en_penta), "Solo A tiene 8 notas de las permitidas y termina en 1: B usa el 4 y C termina en 2."),
        ex(f"¿Cuántas notas de la improvisación B {N(*IB)} no están permitidas?", str(sum(1 for n in IB if n not in PENTA)), "Solo el 4 está fuera del grupo permitido."),
        ex("¿Debe mantenerse el pulso estable mientras se improvisa? Responde sí o no.", "Sí", "El pulso estable da el orden sobre el que se inventa."),
    ],
    [
        arith("Improvisas 4 compases de 4 pulsos con una nota por pulso. ¿Cuántas notas tocas?", "4*4", "Se multiplican los compases por los pulsos.", " notas"),
        ex("¿Cuántas notas distintas puedes usar con las reglas de práctica?", "5", "Son 1, 2, 3, 5 y 6."),
        ex("Quieres improvisar 8 notas distintas usando solo las notas permitidas. ¿Es posible sin repetir ninguna?", "No", "Solo hay 5 notas permitidas, y 8 es más que 5."),
    ],
    [
        ex("Pedro dice que improvisar es tocar cualquier cosa. ¿Tiene razón?", "No: improvisar tiene un propósito y reglas", "Las reglas y el propósito ordenan la improvisación."),
        ex(f"Ana improvisó {N(2, 3, 5, 6, 5, 3, 2, 1)} para el propósito «una noche tranquila» con p y tempo lento. ¿Es coherente con el propósito?", "Sí", "p y lento expresan calma, y la melodía sube y baja suavemente."),
    ],
    [
        arith("Tu improvisación tiene 16 notas de un pulso y va a 80 pulsos por minuto. ¿Cuántos segundos dura?", "16*60//80", "Cada pulso dura 0,75 segundos.", " segundos"),
        ex(f"¿Cuántos saltos (pasos de 2 o más números) hay en {N(*IA)}?", str(leaps(IA)), "Son 1→3, 3→5 y 5→3; el resto son pasos por grado."),
    ],
    [ex("Un grupo improvisa la banda sonora de «el bosque de noche». ¿Qué combinación es más coherente: p y tempo lento o ff y tempo rápido?", "p y tempo lento", "Una noche tranquila en el bosque pide suavidad y calma.")],
    [ex("En Música: ¿Qué es improvisar?", "Inventar música en el momento con propósito y reglas", "Es la definición de la clase."), ex("¿En qué nota se termina en las reglas de práctica?", "En 1", "Da sensación de llegada."), ex("¿Qué escala usamos de práctica?", "La pentatónica", "Tiene cinco notas.")],
    (
        f"Elige uno de estos propósitos: A) «el amanecer en el campo», B) «un perro que corre feliz» o C) «una nave que se aleja». Escribe tu improvisación como 8 números con las reglas de práctica ({REG1}), y decide dinámica y tempo coherentes con el propósito. Si puedes, cántala con «la» o tócala en un instrumento melódico, manteniendo el pulso. Anota si cumpliste las reglas y si se oyó el propósito.",
        "Propósito A. Improvisación: 1-2-3-5-6-5-3-1. Dinámica: parte en p y hace crescendo hasta mf; tempo moderado y creciente. Cumplí las reglas (8 notas de las permitidas, terminé en 1). Se oye el amanecer porque sube poco a poco y luego baja suave.",
        ["cumple las reglas de práctica", "elige dinámica y tempo coherentes con el propósito", "revisa si se oyó el propósito"],
        ["melodía escrita", "improvisación realizada"],
        ["usar la nota 4", "no terminar en 1", "elegir recursos que no expresan el propósito"],
        "Reconoce la improvisación y pide señalar qué parte expresa el propósito y por qué.",
    ),
    "Improvisa 4 notas con las reglas de práctica y termina en 1.",
    "Improvisa dos veces el mismo propósito y compara qué cambió en cada intento.",
)

# ---------------------------------------------------------------- OA 05 · clase 2 (crear ritmos con un compás)
L(
    OA5, 2,
    f"Lápiz y papel; palmas y golpecitos con la yema de los dedos sobre una mesa. Leyenda de figuras: {LEY}. Cuida el volumen.",
    "Aprenderé a crear ritmos que llenen un compás con figuras y a elegirlos según un propósito: marcha, cuna o baile. Sirve para inventar patrones rítmicos escritos que otros puedan tocar.",
    ["Sé cuántos pulsos dura cada figura.", "Sé que los compases son 2/4, 3/4 y 4/4.", "Sé sumar para ver si un patrón llena un compás."],
    [
        f"Para crear un ritmo primero se elige el compás y se calcula cuántos pulsos hay que llenar. Con la leyenda de la clase ({LEY}), se eligen figuras y silencios que sumen exactamente los pulsos del compás. Si el compás es 3/4, las figuras deben sumar 3; si es 4/4, 4. Un silencio vale como una figura: ocupa su tiempo aunque no suene.",
        f"El propósito guía la elección. Una marcha pide pulso firme y figuras parejas, como {P(NEG, NEG, NEG, NEG)} en 4/4. Una canción de cuna pide figuras largas y tranquilas, como {P(BLA, NEG)} en 3/4. Un baile alegre usa figuras cortas, como {P(CC, CC, NEG, NEG)} en 4/4. El contraste entre figuras largas y cortas hace que el ritmo sea interesante.",
        "Cuando termines, comprueba con una suma que cada compás está completo, y tócalo con palmas manteniendo el pulso. Si lo repites cuatro veces, ya tienes un ostinato rítmico que sirve de acompañamiento. Un ritmo creado se puede variar cambiando una figura por otra del mismo valor, por ejemplo una negra por dos corcheas.",
    ],
    [("compás completo", "compás cuyas figuras suman exactamente sus pulsos"), ("silencio", "pausa que ocupa tiempo sin sonar"), ("ostinato rítmico", "patrón de ritmo que se repite como acompañamiento"), ("figuras largas y cortas", "blanca y redonda son largas; corcheas son cortas"), ("variar un ritmo", "cambiar una figura por otra del mismo valor")],
    [
        ("Completar un compás", f"En 4/4 tienes {P(BLA, NEG)}. ¿Qué falta para completar el compás?", ["Blanca = 2 y negra = 1: suman 3.", "Faltan 4 − 3 = 1 pulso."], "Una negra o un silencio de negra"),
        ("Elegir según el propósito", f"Para una canción de cuna lenta y tranquila en 3/4, ¿qué ritmo elegirías: {P(BLA, NEG)} o {P(CC, CC, CC)}?", ["La cuna pide figuras largas.", f"{P(BLA, NEG)} suma 3 y es largo; el otro suma 3 pero es muy rápido."], f"{P(BLA, NEG)}"),
    ],
    [
        ("Olvidar que el silencio ocupa tiempo.", "Un silencio de negra dura 1 pulso aunque no suene.", "Cuenta los silencios al sumar."),
        ("Crear un ritmo largo sin comprobar la suma.", "Un compás que no suma sus pulsos queda incompleto o sobrante.", "Suma las figuras antes de tocar."),
    ],
    [
        ex("¿Cuántos pulsos tiene un compás 2/4?", "2", "El número de arriba indica los pulsos."),
        ex("¿Qué figura dura 2 pulsos?", "La blanca", "Así lo dice la leyenda de la clase."),
        ex("Un silencio de negra, ¿cuánto dura?", "1 pulso", "Aunque no suene, ocupa su tiempo."),
    ],
    [
        ex(f"En 3/4 tienes {P(NEG, NEG)}. ¿Qué figura completa el compás: una negra o una blanca?", "Una negra", "Faltan 3 − 2 = 1 pulso."),
        ex(f"¿Cuántos pulsos suma {P(CC, NEG, SN, NEG)}?", str(pulses(CC, NEG, SN, NEG)), "2 corcheas = 1, más negra 1, silencio 1 y negra 1."),
        ex(f"¿Llena un compás 4/4 el patrón {P(RED)}?", "Sí", "La redonda dura 4 pulsos."),
    ],
    [
        ex(f"¿Cuál de estos llena un 3/4 y tiene exactamente 4 sonidos: (a) {P(NEG, CC, NEG)}, (b) {P(BLA, NEG)} o (c) {P(NEG, NEG, NEG)}?", "(a)", f"(a) suma {pulses(NEG, CC, NEG)} pulsos y tiene {sounds(NEG, CC, NEG)} sonidos; (b) tiene 2 y (c) tiene 3."),
        arith("Un ritmo de 4/4 se repite 6 veces como ostinato. ¿Cuántos pulsos suena?", "6*4", "Se multiplican las repeticiones por los pulsos del compás.", " pulsos"),
        ex(f"Varía {P(NEG, NEG, BLA)} cambiando una negra por dos corcheas del mismo valor. ¿Cuántos pulsos tiene el resultado?", "4", "El valor no cambia: sigue sumando 4 pulsos."),
    ],
    [
        ex(f"Marta quiere un ritmo de cuna lento y tranquilo. ¿Cuál elige: (a) {P(CC, CC, CC, CC)} o (b) {P(BLA, BLA)}?", "(b)", "Las figuras largas son más tranquilas."),
        ex(f"Luis dice que {P(BP, SN)} no llena un 4/4 porque el silencio no suena. ¿Tiene razón?", "No: suma 3 + 1 = 4", "Un silencio de negra ocupa 1 pulso."),
    ],
    [
        arith("Un ritmo de 4/4 usa negra, 2 corcheas y blanca (4 pulsos) y se repite 4 compases. ¿Cuántos sonidos suenan en total? Sabes que la negra da 1 sonido, las 2 corcheas dan 2 y la blanca 1.", "4*(1+2+1)", "En un compás hay 4 sonidos y se repite 4 veces.", " sonidos"),
        ex("Un compás 4/4 ya tiene una redonda. ¿Cuántas figuras más caben en él?", "Ninguna", "La redonda ocupa los 4 pulsos."),
    ],
    [ex("Una marcha de desfile en 2/4 necesita un ritmo que marque cada pulso con un golpe. ¿Qué eliges: negra – negra o blanca?", "Negra – negra", "Da un golpe en cada uno de los dos pulsos del compás; la blanca llena el compás con un solo golpe.")],
    [ex("¿Cuánto debe sumar un compás 3/4?", "3 pulsos", "El número de arriba es 3."), ex("¿Qué se comprueba con una suma?", "Que el compás esté completo", "La suma debe dar los pulsos del compás."), ex("¿Qué figura es una versión equivalente de una negra?", "Dos corcheas", "Ambas suman 1 pulso.")],
    (
        f"Crea un ritmo de 4 compases en 4/4 para una de estas ideas: A) «marcha de soldaditos de juguete» o B) «baile de la lluvia». Escribe los 4 compases con figuras de la leyenda ({LEY}), comprueba con una suma que cada compás dura 4 pulsos, y explica por qué elegiste esas figuras. Tócalo con palmas a pulso parejo.",
        "Idea A. Compás 1: negra – negra – negra – negra (4). Compás 2: negra – negra – blanca (4). Compás 3: 2 corcheas – 2 corcheas – negra – negra (4). Compás 4: blanca – blanca (4). Elegí figuras parejas para marcar un paso firme y terminé con figuras largas para frenar.",
        ["cada compás suma 4 pulsos", "las figuras coinciden con la idea", "lo toca con pulso parejo"],
        ["ritmo escrito con sumas", "ritmo tocado"],
        ["compases que no suman 4", "olvidar el silencio"],
        "Reconoce el ritmo y pide mostrar la suma de un compás con el dedo sobre cada figura.",
    ),
    "Escribe dos compases de 3/4 con figuras distintas y comprueba que suman 3 pulsos.",
    "Crea una variación del ritmo de la actividad cambiando una negra por dos corcheas en un compás.",
)

# ---------------------------------------------------------------- OA 05 · clase 3 (crear una melodía con reglas)
REG3 = "reglas de melodía: 8 notas; empieza y termina en 1; ninguna nota mayor que 5; como máximo 2 saltos (pasos de 2 o más números)"
KA, KB, KC = (1, 2, 3, 3, 4, 3, 2, 1), (1, 3, 5, 3, 5, 3, 2, 1), (1, 2, 3, 4, 5, 6, 5, 1)
CAND3 = {"A": KA, "B": KB, "C": KC}

L(
    OA5, 3,
    f"Lápiz y papel; tu voz o un instrumento melódico. Notas: {NOTAS}. {REG3}. Cuida el volumen.",
    "Aprenderé a crear una melodía que cumpla reglas (inicio, final, rango y saltos) y a revisarla escuchándola. Sirve para componer melodías que se puedan cantar y que tengan un propósito.",
    ["Sé que una melodía se escribe con números.", "Sé qué es un salto y un grado.", "Sé calcular el rango restando."],
    [
        f"Crear una melodía es elegir notas y ordenarlas para decir algo. Para empezar conviene ponerle reglas, como las de esta clase: {REG3}. Empezar y terminar en 1 da sensación de comienzo y de llegada. Limitar el rango y los saltos hace que la melodía sea fácil de cantar.",
        "Una melodía suele dividirse en frases, como las oraciones. Dos frases de 4 notas pueden dialogar como pregunta y respuesta: la primera termina en una nota abierta, como 3 o 5, y la segunda termina en 1. Una melodía interesante mezcla pasos por grado, que dan suavidad, con un salto que da sorpresa, y puede tener una nota más aguda en el medio que funcione como punto alto.",
        "Después de escribirla, se revisa escuchándola o cantándola: ¿cumple las reglas?, ¿se canta fácil?, ¿expresa el propósito? Si no, se cambia una nota por vez. Cambiar una sola nota a la vez permite saber cuál cambio mejoró o empeoró la melodía. Así se trabaja una creación: se prueba, se escucha, se ajusta.",
    ],
    [("frase", "trozo de melodía con sentido, como una oración"), ("punto alto", "la nota más aguda de la melodía"), ("pregunta y respuesta", "dos frases: una abierta y otra que termina en 1"), ("ajustar", "cambiar algo para mejorar tras escuchar"), ("propósito de la melodía", "lo que quiere expresar o para qué se crea")],
    [
        ("Verificar una melodía", f"Melodía {N(1, 2, 3, 5, 4, 3, 2, 1)}. ¿Cumple las reglas de melodía de la clase?", ["Tiene 8 notas y parte y termina en 1.", "La nota más alta es 5.", "El único salto es 3→5, así que hay 1 salto."], "Sí, cumple todas"),
        ("Detectar un error", f"Melodía {N(1, 3, 5, 6, 5, 3, 2, 1)}. ¿Qué reglas no cumple?", ["Parte y termina en 1 y tiene 8 notas.", "Usa el 6, mayor que 5.", "Los saltos son 1→3, 3→5 y 5→3: son 3, más de 2."], "Dos: usa la nota 6, mayor que 5, y tiene 3 saltos"),
    ],
    [
        ("Cambiar muchas notas a la vez al ajustar.", "Así no se sabe cuál cambio mejoró la melodía.", "Cambia una nota por vez y escucha."),
        ("Poner muchos saltos grandes porque «suena más interesante».", "Con muchos saltos la melodía se vuelve difícil de cantar y no cumple la regla.", "Combina pasos por grado con uno o dos saltos."),
    ],
    [
        ex("Según las reglas de la clase, ¿en qué nota empieza y termina la melodía?", "En 1", "Así lo piden las reglas de melodía."),
        ex("Según las reglas, ¿cuántas notas tiene la melodía?", "8", "El enunciado de las reglas dice 8 notas."),
        ex("¿Qué nota más aguda se permite en la clase?", "5", "Ninguna nota puede ser mayor que 5."),
    ],
    [
        ex(f"¿Cuál de estas melodías cumple las reglas: A {N(*KA)}, B {N(*KB)} o C {N(*KC)}?", cual(CAND3, cumple), "A cumple todo; B tiene demasiados saltos y C llega a 6 y termina con un salto grande."),
        ex(f"¿Cuántos saltos tiene la melodía B {N(*KB)}?", str(leaps(KB)), "Los pasos 1→3, 3→5, 5→3, 3→5 y 5→3 son saltos; los otros dos son grados."),
        ex(f"¿Cuál es el rango de la melodía A {N(*KA)}?", "3", "La nota más aguda es 4 y la más grave es 1; 4 − 1 = 3."),
    ],
    [
        ex(f"La frase {N(1, 2, 3, 3)} es una pregunta porque termina en una nota abierta. ¿Cuál es una buena respuesta: {N(4, 3, 2, 1)} o {N(4, 3, 2, 3)}?", N(4, 3, 2, 1), "La respuesta debe terminar en 1 para dar sensación de llegada."),
        arith("Una melodía de 8 notas tiene una nota por pulso en 4/4. ¿Cuántos compases dura?", "8//4", "Cada compás tiene 4 pulsos.", " compases"),
        ex("Una melodía de 8 notas parte en 1 y sus 7 pasos son todos de un grado: sube, sube, sube, baja, baja, baja y repite. ¿Cuál es su nota más aguda y en qué nota termina?", "4 y termina en 1", "Sube de 1 a 4 en tres pasos, baja de 4 a 1 en tres pasos y repite el 1."),
    ],
    [
        ex("Julia dice que su melodía está lista porque cumple las reglas, aunque no la cantó. ¿Qué le falta?", "Cantarla o escucharla para ver si es fácil de cantar y expresa su propósito", "Cumplir reglas no basta: hay que escucharla y ajustarla."),
        ex(f"Compara {N(1, 2, 3, 3, 4, 3, 2, 1)} con {N(1, 2, 3, 3, 4, 3, 1, 1)}. ¿Cuántas notas cambian?", "1", "Solo la séptima pasa de 2 a 1."),
    ],
    [
        ex(f"La melodía {N(1, 2, 3, 4, 3, 2, 2, 1)} tiene 8 notas. ¿Cuántos saltos tiene y cuál es su rango?", "0 saltos y rango 3", "Todos sus pasos son por grado o repiten; la nota más aguda es 4 y la más grave 1: 4 − 1 = 3."),
        arith("Un grupo crea 3 melodías de 8 notas que tienen 1, 2 y 2 saltos. ¿Cuántos saltos hay en total?", "1+2+2", "Se suman los saltos de las tres melodías.", " saltos"),
    ],
    [ex("Quieres una melodía suave para dormir a un hermano pequeño. ¿Qué eliges: muchos pasos por grado o muchos saltos grandes?", "Muchos pasos por grado", "Los grados suenan suaves.")],
    [ex("¿Cuántos saltos máximo permiten las reglas?", "2", "Las reglas fijan máximo 2 saltos."), ex("¿Qué se hace cuando una melodía no cumple?", "Se cambia una nota por vez y se escucha", "Se ajusta paso a paso."), ex("¿En qué nota termina una buena respuesta?", "En 1", "Da sensación de llegada.")],
    (
        f"Crea una melodía de 8 notas para una de estas ideas: A) «una canción de cuna», B) «una marcha sencilla» o C) «un saludo al amanecer». Debe cumplir las reglas: {REG3}. Escríbela con números, marca los saltos y calcula su rango. Cántala con «la» y ajusta una nota si no se canta fácil. Anota qué cambiaste.",
        "Idea A. Melodía: 1-2-3-3-4-3-2-1, con 0 saltos y rango 4 − 1 = 3. Al cantarla me pareció muy plana, así que cambié la tercera nota de 3 a 5 y quedó 1-2-5-3-4-3-2-1: tiene 2 saltos (2→5 y 5→3), su nota más aguda es 5, su rango ahora es 5 − 1 = 4 y sigue cumpliendo las reglas.",
        ["cumple las reglas", "marca los saltos y calcula bien el rango", "ajusta cambiando una nota a la vez y lo explica"],
        ["melodía escrita", "melodía cantada"],
        ["pasar de 5 o de 2 saltos", "cambiar muchas notas a la vez"],
        "Reconoce la melodía y pide señalar con el dedo los saltos y cantar cada frase.",
    ),
    "Canta con «la» la melodía de la clase y marca con la mano cuándo sube y cuándo baja.",
    "Crea una respuesta de 4 notas que termine en 1 para la frase 1-3-2-3.",
)

# ---------------------------------------------------------------- OA 05 · clase 4 (forma, motivo y variación)
MOT = (3, 3, 4)

L(
    OA5, 4,
    f"Lápiz y papel; tu voz o un instrumento melódico. Notas: {NOTAS}. Motivo de práctica: {N(*MOT)}. Cuida el volumen.",
    "Aprenderé a crear una pieza a partir de un motivo: repetirlo, moverlo en secuencia, variarlo y ordenarlo en una forma (AB o ABA). Sirve para armar una música completa a partir de una idea corta.",
    ["Sé qué son un motivo y una secuencia.", "Sé qué es la forma ABA.", "Sé sumar compases."],
    [
        f"Un motivo es una idea musical corta, como {N(*MOT)}. Con un motivo se puede construir mucha música. Se puede repetir igual (reiteración), mover a otra altura (secuencia: {N(*MOT)} y luego {N(4, 4, 5)}), cambiar un poco (variación: {N(3, 3, 5)}) o contrastar con otra idea totalmente distinta.",
        "Las ideas se ordenan en secciones. En la forma AB hay una sección con el motivo y otra con una idea contrastante. En la forma ABA vuelve la primera sección al final, y eso da sensación de cierre. Cada sección puede tener la misma cantidad de compases o distinta, y la forma ayuda al oyente a seguir el recorrido de la pieza.",
        "Para decidir cuánto repetir y cuánto cambiar, piensa en el equilibrio: si todo se repite igual, la música aburre; si todo cambia, el oyente se pierde. Una buena regla es repetir una idea y luego variarla o contrastarla. Anota la forma con letras (A, B, A') y explica qué cambió en cada sección.",
    ],
    [("motivo", "idea musical corta que se desarrolla"), ("secuencia", "motivo repetido desde otra nota"), ("variación", "motivo que vuelve con algún cambio"), ("sección", "parte grande de una pieza, nombrada con una letra"), ("cierre", "sensación de llegada al final")],
    [
        ("Hacer una secuencia", f"El motivo es {N(2, 3, 4)}. ¿Cómo queda en secuencia, un grado más alto?", ["Sumo 1 a cada nota: 2→3, 3→4, 4→5.", "Escribo los resultados en el mismo orden."], f"{N(3, 4, 5)}"),
        ("Planear una forma", "Una pieza tiene sección A de 4 compases, sección B de 4 compases y vuelve A. ¿Cuántos compases tiene y qué forma es?", ["Las secciones son A, B y A.", "4 + 4 + 4 = 12 compases."], "ABA, 12 compases"),
    ],
    [
        ("Repetir el motivo tantas veces que la pieza aburre.", "Sin cambios la música se vuelve monótona.", "Repite y luego varía o contrasta."),
        ("Cambiar todo en cada sección.", "Sin ideas que vuelvan, el oyente no reconoce la pieza.", "Haz que una sección vuelva, como en ABA."),
    ],
    [
        ex(f"El motivo {N(*MOT)} vuelve igual. ¿Es reiteración, variación o contraste?", "Reiteración", "Vuelve exactamente igual."),
        ex(f"El motivo {N(*MOT)} vuelve como {N(3, 3, 5)}. ¿Es reiteración o variación?", "Variación", "Cambia solo la última nota."),
        ex("En una pieza ABA, ¿qué letra se repite al final?", "A", "La primera sección regresa."),
    ],
    [
        ex(f"Escribe en secuencia, un grado más alto, el motivo {N(*MOT)}.", N(4, 4, 5), "Se suma 1 a cada nota."),
        ex("Una pieza tiene la forma AB: A de 6 compases y B de 4 compases. ¿Cuántos compases tiene?", "10", "6 + 4 = 10 compases."),
        ex(f"Compara {N(*MOT)} con {N(3, 3, 5)}. ¿Cuántas notas cambian?", "1", "Solo la tercera pasa de 4 a 5."),
    ],
    [
        arith("Una pieza ABA tiene A de 8 compases y B de 4 compases. ¿Cuántos compases dura?", "8+4+8", "A aparece dos veces y B una vez.", " compases"),
        arith("Cada compás tiene 3 pulsos y la pieza tiene 12 compases. ¿Cuántos pulsos tiene?", "12*3", "Se multiplican los compases por los pulsos.", " pulsos"),
        ex(f"Tienes {N(*MOT)}, luego {N(4, 4, 5)} y luego {N(5, 5, 6)}. ¿Qué recurso se usa al repetir el motivo cada vez más alto?", "Secuencia", "El motivo vuelve desde otra nota."),
    ],
    [
        ex("Pedro dice que una pieza AB tiene una sección que vuelve al final. ¿Tiene razón?", "No: en AB la sección A no vuelve; eso ocurre en ABA", "AB tiene dos secciones sin regreso."),
        ex("Una pieza va A, A, B, A. ¿Cuántas veces suena A y cuántas B?", "A tres veces y B una vez", "La letra A aparece en la primera, segunda y cuarta sección."),
    ],
    [
        arith("Una pieza A, A, B, A tiene A de 4 compases y B de 4 compases. ¿Cuántos compases dura?", "3*4+4", "Tres secciones A y una B, todas de 4 compases.", " compases"),
        ex(f"Escribe una variación de {N(3, 3, 4)} que cambie solo la primera nota por 1. ¿Cómo queda?", N(1, 3, 4), "Se cambia solo la primera nota."),
    ],
    [ex("Una compositora crea una canción con un motivo de 3 notas. Lo repite, lo mueve en secuencia, lo varía y termina con el motivo original. ¿Qué sensación da el regreso del motivo original al final?", "Cierre", "Volver a la idea inicial da sensación de llegada.")],
    [ex("¿Cómo se llama la idea musical corta que se desarrolla para armar una pieza?", "Motivo", "Es la idea musical corta que se desarrolla."), ex("En Música: ¿Qué es una secuencia?", "El motivo repetido desde otra nota", "Suena igual pero más agudo o grave."), ex("¿Qué forma tiene A, B, A?", "ABA", "Vuelve la primera sección.")],
    (
        f"Crea una pieza breve de forma ABA con este motivo: {N(*MOT)}. Sección A: el motivo dos veces, la segunda en secuencia un grado más alto. Sección B: una idea contrastante de 3 notas (por ejemplo, que baje). Sección A': el motivo original con una variación de la última nota. Escribe las tres secciones con números, calcula cuántas notas tiene la pieza y explica qué recurso usaste en cada sección. Cántala con «la».",
        "A: 3-3-4 y 4-4-5. B: 5-4-2. A': 3-3-5. Total: 6 + 3 + 3 = 12 notas. Recursos: A usa reiteración y secuencia; B contrasta bajando; A' varía la última nota.",
        ["la forma es ABA", "usa secuencia, contraste y variación", "calcula bien las notas y explica"],
        ["pieza escrita", "pieza cantada"],
        ["no hacer regresar A", "cambiar todo en cada sección"],
        "Reconoce la pieza y pide señalar en qué nota cambia la variación.",
    ),
    "Escribe el motivo de la clase en secuencia dos veces seguidas.",
    "Crea una pieza AABA con un motivo de tu invención y cuenta sus compases.",
)

# ---------------------------------------------------------------- OA 05 · clase 5 (comunicar y explicar la creación)
CRIT5 = "una buena explicación de una creación dice: 1) el propósito; 2) una decisión musical (recurso) y su efecto; 3) cómo se oye (evidencia); 4) qué se ajustó después de escuchar"

L(
    OA5, 5,
    f"Lápiz y papel. {CRIT5}. Las creaciones que se analizan están descritas en los ejercicios; tus creaciones anteriores te sirven para practicar. Cuida el volumen.",
    "Aprenderé a comunicar mi creación musical: decir su propósito, explicar mis decisiones con evidencia audible y mostrar cómo la ajusté. Sirve para que otras personas entiendan y evalúen mi idea.",
    ["Sé improvisar y crear ritmos y melodías con reglas.", "Sé qué es una forma musical.", "Sé usar la evidencia audible."],
    [
        f"Crear música incluye poder explicarla. {CRIT5}. Quien escucha tu creación entiende mejor si le dices para qué la hiciste y qué decisiones tomaste. «Me salió así» no explica nada; «usé un tempo lento y notas largas para expresar calma» sí.",
        "El proceso creativo tiene pasos: pensar el propósito, probar ideas, elegir la mejor, escribirla o grabarla, escucharla y ajustarla. Escribir permite recordar la idea y compartirla con otras personas; puede ser con números, con figuras, con un dibujo (partitura gráfica) o con una grabación, siempre que otra persona pueda entender qué tocar.",
        "Comunicar también es escuchar la opinión de otros. Se pide a quien escucha que diga qué entendió, qué le gustó con evidencia y qué haría distinto, y tú decides si ajustar o no. Hay que recibir los comentarios con respeto: el comentario habla de la música, no de la persona. Al final, un buen cierre dice qué aprendiste y qué mejorarías en una próxima creación.",
    ],
    [("proceso creativo", "pasos para crear: propósito, probar, elegir, escribir, escuchar, ajustar"), ("decisión musical", "elección de un recurso para lograr un efecto"), ("notación", "forma de escribir la música para que otros la entiendan"), ("partitura gráfica", "dibujo que representa los sonidos"), ("comentario respetuoso", "opinión sobre la música, no sobre la persona")],
    [
        ("Evaluar una explicación", "«Hice esta melodía porque me salió.» ¿Cuántos criterios de la lista cumple?", ["No dice el propósito.", "No explica decisiones ni evidencia.", "No cuenta ajustes."], "0 criterios"),
        ("Ordenar pasos", "En el proceso creativo, ¿qué paso viene después de «probar ideas»?", ["Los pasos son: propósito, probar, elegir, escribir o grabar, escuchar, ajustar.", "Después de probar se elige la mejor idea."], "Elegir la mejor idea"),
    ],
    [
        ("Explicar una creación diciendo solo «me gusta».", "Una explicación necesita propósito, decisiones y evidencia.", "Usa la lista de cuatro criterios."),
        ("Tomarse a pecho un comentario como un ataque.", "El comentario habla de la música, no de la persona.", "Escucha y decide qué ajustar."),
    ],
    [
        ex("¿Cuántos criterios tiene una buena explicación de una creación?", "4", "La lista de la clase tiene propósito, decisión, evidencia y ajuste."),
        ex("Dibujar los sonidos con líneas y puntos para que otros los entiendan, ¿cómo se llama?", "Partitura gráfica", "Es la notación con dibujo."),
        ex("Al comentar una creación ajena, ¿un buen comentario se centra en la música o en quien la hizo?", "En la música", "Se evalúa lo que se oye."),
    ],
    [
        ex("«Usé un tempo lento y notas largas para que suene tranquila.» ¿Qué criterio muestra: el ajuste o la decisión con su efecto?", "La decisión con su efecto", "Dice un recurso (tempo lento y notas largas) y para qué."),
        ex("«Al escucharla vi que el final era muy fuerte y lo cambié a p.» ¿Qué criterio cumple?", "El ajuste después de escuchar", "Cuenta qué cambió tras escuchar."),
        ex("¿Qué paso va primero en el proceso creativo: escribir la música o pensar el propósito?", "Pensar el propósito", "El propósito guía todas las decisiones."),
    ],
    [
        ex("Una explicación dice: «Compuse una marcha (propósito) con negras parejas (decisión) para que suene firme (efecto); se oye un paso parejo en todos los compases (evidencia); en la segunda frase bajé el volumen porque tapaba la flauta (ajuste).» ¿Cuántos criterios cumple?", "4", "Tiene propósito, decisión con efecto, evidencia (se oye un paso parejo) y ajuste."),
        arith("Un grupo explica 5 creaciones y cada una cumple 3 criterios. ¿Cuántos criterios cumplen en total?", "5*3", "Se multiplican las creaciones por los criterios.", " criterios"),
        ex("Tres estudiantes comentan una creación. Ana: «Me gustó cómo sube la melodía y se calma al final». Beto: «Tú siempre haces cosas feas». Carla: «No se oyó la flauta en el compás 5». ¿Cuál comentario NO es respetuoso?", "El de Beto", "Habla de la persona y no de la música."),
    ],
    [
        ex("Pedro dice que no necesita escribir su creación porque la recuerda. ¿Qué ventaja tiene escribirla o grabarla?", "Que otras personas pueden entenderla y tocarla, y él no la olvida", "La notación permite compartir y recordar."),
        ex("Julia recibió un comentario sobre el volumen de su flauta en el compás 5. ¿Qué es mejor: probar un ajuste de volumen o enojarse con quien lo dijo?", "Probar un ajuste de volumen", "El comentario es sobre la música y puede servir para mejorarla."),
    ],
    [
        arith("Tu creación dura 24 pulsos a 72 pulsos por minuto. ¿Cuántos segundos dura?", "24*60//72", "Son 24 pulsos y se multiplican por 60 segundos antes de dividir por 72.", " segundos"),
        ex("Pides comentarios a 4 personas y 3 dicen que se oye poco la flauta. ¿Qué ajuste es más probable que ayude: subir un poco su volumen o bajarlo?", "Subir un poco su volumen", "La mayoría dice que no se oye bien."),
    ],
    [ex("Presentas tu creación al curso. Dices: «La hice para expresar un amanecer; usé crescendo y notas que suben para dar la idea de que sale el sol; se oye cómo crece el volumen compás a compás; después de escucharla bajé el volumen del acompañamiento». ¿Qué criterio falta de la lista?", "Ninguno", "Tiene propósito, decisión con efecto, evidencia (crece el volumen compás a compás) y ajuste.")],
    [ex("¿Qué dice el propósito?", "Para qué hice la música", "Es el primer criterio."), ex("¿Qué es el ajuste?", "Lo que cambié después de escuchar", "Es el cuarto criterio."), ex("¿Cómo se debe recibir un comentario?", "Con respeto, pensando en la música", "El comentario habla de la música.")],
    (
        f"Elige una creación tuya de las clases anteriores (un ritmo, una melodía o una pieza ABA) o usa esta: «Melodía 1-2-3-5-3-2-1-1 en 4/4 para una canción de cuna, tempo lento y dinámica p». Escribe una explicación de cuatro frases que cumpla los cuatro criterios ({CRIT5}). Luego pide a una persona que escuche o lea tu creación y te diga un comentario respetuoso sobre la música; anota qué ajustarías.",
        "Propósito: una canción de cuna para dormir. Decisión: tempo lento, p y una melodía con solo dos saltos, para que suene tranquila. Evidencia: casi todos los pasos son por grado y todo suena bajito. Ajuste: una persona dijo que el último sonido se cortaba muy rápido y lo alargué.",
        ["incluye los cuatro criterios", "usa evidencia audible", "recibe el comentario con respeto"],
        ["explicación escrita", "comentario recibido"],
        ["explicar solo con «me gusta»", "tomar el comentario como ataque"],
        "Reconoce la explicación y pide señalar qué frase corresponde a cada criterio.",
    ),
    "Escribe una frase que cumpla el criterio del propósito para una creación tuya.",
    "Escribe una partitura gráfica con líneas y puntos para tu melodía y explica cómo se lee.",
)
