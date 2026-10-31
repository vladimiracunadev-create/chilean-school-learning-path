"""Student material for 6.º básico Música, OA 04 (cantar al unísono y a más voces; tocar instrumentos de percusión, melódicos y armónicos).

Todas las melodías y esquemas son originales inventados, escritos con números (1 = do … 8 = do agudo) o con descripciones; no se usa repertorio con derechos.
Los instrumentos reales (metalófono, flauta dulce, guitarra, teclado) y el cuidado de la voz los guía el docente; en casa basta con la voz, las palmas y los ejercicios escritos.
"""
from __future__ import annotations

from student_content_mu6_a import L, N
from student_lessons import arith, ex

OA4 = "MU06 OA 04"
VOZ = "Cuidado de la voz: calentar con respiración suave y un «mmm» tranquilo, cantar sin gritar, tomar agua y parar si duele la garganta"

# ---------------------------------------------------------------- OA 04 · clase 1 (canto al unísono y a más voces)
MEL = (3, 4, 5, 5, 6, 5, 4, 3)
BAJA = tuple(n - 2 for n in MEL)

L(
    OA4, 1,
    f"Lápiz y papel; tu voz. {VOZ}. Melodías escritas con números (1 = do … 8 = do agudo); si no conoces los sonidos, canta con «la» siguiendo si sube o baja. Volumen moderado.",
    "Aprenderé a cantar al unísono (todos la misma melodía) y a más voces (voces distintas a la vez): canon, ostinato y voz paralela. Sirve para cantar en grupo cuidando la voz y escuchando a los demás.",
    ["Sé que una melodía se escribe con números.", "Sé que una frase puede repetirse o cambiar.", "Sé contar compases."],
    [
        "Cantar al unísono es cantar todos la misma melodía a la vez, con el mismo ritmo y las mismas notas. Cantar a más voces es cantar melodías o partes distintas al mismo tiempo, y se oye más rico porque suenan varias capas. Para lograrlo todos necesitan un pulso común y escuchar a los demás mientras cantan.",
        "Hay varias maneras de cantar a más voces. En el canon, todos cantan la misma melodía pero entran uno después de otro, por ejemplo cada 2 compases. En el ostinato, un grupo repite una frase corta una y otra vez mientras otro canta la melodía. En la voz paralela, una segunda voz canta lo mismo pero más grave; en esta clase la baja dos números (una tercera abajo): si la melodía es 5-6-5, la segunda voz es 3-4-3.",
        f"{VOZ}. Cuando cantes a más voces, escucha tu parte y también las de los demás: si no oyes a los otros, estás cantando muy fuerte. Es normal equivocarse al comienzo: se repite por partes, lento, y luego se junta todo. Un coro suena bien cuando cada voz sabe cuándo entra, cuándo calla y cuánto volumen usar.",
    ],
    [("unísono", "todos cantan la misma melodía a la vez"), ("a más voces", "se cantan partes distintas al mismo tiempo"), ("canon", "la misma melodía entra en distintos momentos"), ("ostinato", "frase corta que se repite sin parar como fondo"), ("voz paralela", "segunda voz que sigue a la melodía a la misma distancia")],
    [
        ("Calcular un canon", "Una melodía de 8 compases se canta en canon con 3 voces que entran cada 2 compases. ¿En qué compás termina la última voz?", ["La voz 1 entra en el compás 1 y termina en el 8.", "La voz 2 entra en el 3 y termina en el 10; la voz 3 entra en el 5 y termina en el 12."], "En el compás 12"),
        ("Voz paralela", f"La melodía es {N(6, 5, 4, 5)}. ¿Cuál es la segunda voz, dos números más abajo?", ["Resto 2 a cada número: 6→4, 5→3, 4→2, 5→3.", "Escribo los resultados en el mismo orden."], f"{N(4, 3, 2, 3)}"),
    ],
    [
        ("Cantar más fuerte para sonar más.", "Gritar daña la voz y no deja oír a los demás.", "Canta suave y escucha al grupo."),
        ("Entrar a destiempo en el canon por no contar compases.", "Cada voz debe esperar el número exacto de compases.", "Cuenta en silencio y entra en el pulso 1."),
    ],
    [
        ex("Todos cantan la misma melodía a la vez. ¿Es unísono o a más voces?", "Unísono", "Todos hacen lo mismo."),
        ex("Un grupo canta una melodía y otro canta una parte distinta al mismo tiempo. ¿Es unísono o a más voces?", "A más voces", "Las partes son distintas."),
        ex("Antes de cantar, ¿qué conviene hacer: calentar con respiración suave o gritar para abrir la voz?", "Calentar con respiración suave", "Gritar daña la voz."),
    ],
    [
        ex("Una voz canta una melodía y otra entra con la misma melodía 2 compases después. ¿Es un canon o un ostinato?", "Canon", "La misma melodía entra desfasada."),
        ex("Un grupo repite sin parar una frase de 2 compases mientras otro canta la melodía. ¿Es un ostinato o un canon?", "Ostinato", "La frase corta se repite como fondo."),
        ex(f"La melodía de la clase es {N(*MEL)}. ¿Con qué número termina la voz paralela dos números más abajo?", str(BAJA[-1]), "El último número de la melodía es 3 y 3 − 2 = 1."),
    ],
    [
        arith("En un canon de 3 voces que entran cada 4 compases, la melodía dura 12 compases. ¿En qué compás termina la última voz?", "12+2*4", "La voz 3 entra en el compás 9 (1 + 2 × 4) y canta 12 compases, del 9 al 20.", ""),
        ex(f"Escribe la voz paralela de {N(5, 6, 5, 4)}, dos números más abajo.", N(3, 4, 3, 2), "Se resta 2 a cada nota."),
        arith("Un coro de 24 estudiantes se divide en 3 voces iguales. ¿Cuántos cantan en cada voz?", "24//3", "Se reparten por igual.", " estudiantes"),
    ],
    [
        ex("Ana dice que si todos cantan con distinto volumen están cantando a más voces. ¿Tiene razón?", "No: cantar a más voces exige partes distintas, no solo volumen distinto", "Con una misma melodía, aunque cambie el volumen, sigue siendo unísono."),
        ex("En un canon de 2 voces con melodía de 8 compases y entrada a 4 compases, ¿cuántas voces suenan en los compases 5 a 8?", "2", "La voz 1 está terminando y la voz 2 ya entró."),
    ],
    [
        ex("En un canon de 3 voces con melodía de 12 compases y entradas cada 4 compases, ¿durante cuántos compases suenan las tres voces a la vez?", "4", "La voz 3 entra en el compás 9 y la voz 1 termina en el 12: son los compases 9 a 12."),
        arith("Una canción de 16 compases de 4 pulsos va a 96 pulsos por minuto. ¿Cuántos segundos dura?", "16*4*60//96", "Son 64 pulsos y cada uno dura 0,625 segundos.", " segundos"),
    ],
    [ex("Un coro escolar de 30 estudiantes canta una voz paralela con 12 estudiantes y el resto canta la melodía. ¿Cuántos cantan la melodía?", "18", "30 − 12 = 18.")],
    [ex("¿Qué es el unísono?", "Cantar todos la misma melodía a la vez", "Es la definición de la clase."), ex("¿Cómo se llama la frase que se repite sin parar como fondo?", "Ostinato", "Es la definición de ostinato."), ex("¿Qué se hace si te duele la garganta?", "Parar y descansar la voz", "El cuidado de la voz es primero.")],
    (
        "Canta con «la» esta melodía de 4 compases inventada: 3-4-5-5 | 6-5-4-3 | 5-6-5-4 | 3-4-3-3. Primero cántala 2 veces al unísono. Luego escribe la voz paralela dos números más abajo y, si puedes, cántala en una segunda vuelta solo la voz paralela. Escribe cuál fue la parte más difícil y qué hiciste para mejorarla.",
        "Voz paralela: 1-2-3-3 | 4-3-2-1 | 3-4-3-2 | 1-2-1-1. Lo más difícil fue la bajada del segundo compás; la practiqué lento y por partes hasta que quedó parejo.",
        ["canta la melodía con pulso estable", "escribe bien la voz paralela", "explica una dificultad y su solución"],
        ["voz paralela escrita", "ensayo realizado"],
        ["gritar al cantar", "restar mal en la voz paralela"],
        "Reconoce el ensayo y pide cantar solo el compás más difícil, lento.",
    ),
    "Calienta tu voz con respiración suave y un «mmm» tranquilo.",
    "Escribe un ostinato de 2 compases que acompañe la melodía de la actividad abierta.",
)

# ---------------------------------------------------------------- OA 04 · clase 2 (instrumentos de percusión y melódicos)
L(
    OA4, 2,
    "Lápiz y papel. Objetos seguros para practicar en casa: palmas, golpes suaves con la yema de los dedos sobre una mesa o un cuaderno, y tu voz. Instrumentos del colegio: metalófono, flauta dulce, pandero, claves, maracas y bombo. Sin vidrios, ni objetos pequeños. Cuida el volumen.",
    "Aprenderé a reconocer y tocar con cuidado instrumentos de percusión y melódicos (metalófono y flauta dulce). Sirve para elegir qué instrumento usar y tocarlo con buen sonido y a tiempo.",
    ["Sé mantener un pulso con palmas.", "Sé que un sonido puede ser agudo o grave.", "Sé que una melodía se escribe con números."],
    [
        "Los instrumentos de percusión se tocan golpeándolos, sacudiéndolos o raspándolos. Unos no tienen altura definida, como las claves, las maracas, el pandero y el bombo; sirven sobre todo para marcar el pulso y el ritmo. Otros, como el metalófono, tienen barras afinadas y también tocan melodías. La flauta dulce es un instrumento melódico de viento: se sopla y se tapan agujeros con los dedos.",
        "En el metalófono cada barra suena a una altura: las barras más largas suenan más graves y las más cortas más agudas. Se toca con mazos y se golpea el centro de la barra, soltando el mazo rápido para que el sonido vibre. En la flauta dulce, mientras más agujeros se tapan, más grave suena la nota; hay que soplar suave y parejo, porque soplar fuerte la hace chillar.",
        "Cuidar los instrumentos y a las personas es parte de tocar: no se golpean con fuerza, no se comparte una flauta sin lavarla y secarla con ayuda de una persona adulta, y se cuida el volumen para proteger los oídos. Para tocar en grupo, cada instrumento tiene un papel: la percusión marca el pulso, los melódicos llevan la melodía y todos escuchan.",
    ],
    [("percusión", "instrumentos que se tocan golpeando, sacudiendo o raspando"), ("metalófono", "instrumento de barras afinadas que se toca con mazos"), ("flauta dulce", "instrumento de viento melódico con agujeros que se tapan"), ("altura definida", "capacidad de un instrumento de dar notas distintas (agudas o graves)"), ("mazo", "palito con cabeza para golpear las barras del metalófono")],
    [
        ("Clasificar instrumentos", "Las maracas, ¿son un instrumento melódico o de percusión sin altura definida?", ["Las maracas se sacuden.", "No dan notas distintas."], "De percusión sin altura definida"),
        ("Barras del metalófono", "En un metalófono, una barra de 20 cm y otra de 12 cm. ¿Cuál suena más grave?", ["Barra más larga = nota más grave.", "20 cm es más largo que 12 cm."], "La de 20 cm"),
    ],
    [
        ("Golpear el metalófono con mucha fuerza para que se oiga más.", "El golpe fuerte daña el instrumento y suena mal; basta un golpe firme al centro.", "Golpea al centro y suelta el mazo rápido."),
        ("Soplar muy fuerte la flauta dulce.", "Soplar fuerte la hace chillar; la nota queda desafinada.", "Sopla suave y parejo."),
    ],
    [
        ex("El bombo, ¿es de percusión o de viento?", "De percusión", "Se toca golpeándolo."),
        ex("En el metalófono, ¿dónde se golpea la barra para mejor sonido: al centro o al borde?", "Al centro", "El centro de la barra suena mejor."),
        ex("En la flauta dulce, ¿se sopla suave o muy fuerte?", "Suave y parejo", "Soplar fuerte hace chillar."),
    ],
    [
        ex("Si destapas agujeros en la flauta dulce, ¿la nota sube o baja?", "Sube", "Mientras más agujeros destapados, más aguda."),
        ex("El metalófono, ¿es un instrumento melódico o sin altura definida?", "Melódico", "Cada barra tiene una altura distinta."),
        ex("Dos estudiantes quieren compartir una flauta dulce. ¿Qué debe pasar antes: lavarla y secarla con ayuda de un adulto o pasarla sin más?", "Lavarla y secarla con ayuda de un adulto", "Se cuida la higiene."),
    ],
    [
        arith("Una pieza en 4/4 tiene 6 compases, y el bombo suena en el pulso 1 y en el pulso 3 de cada compás. ¿Cuántos golpes de bombo hay?", "6*2", "Son 2 golpes por compás durante 6 compases.", " golpes"),
        arith("Las claves suenan en todos los pulsos de 8 compases de 4 pulsos. ¿Cuántos golpes de claves hay?", "8*4", "Hay 4 pulsos por compás en 8 compases.", " golpes"),
        ex("Un metalófono tiene 8 barras. Tocas una melodía con las barras 1, 3, 5, 3, 1. ¿Cuántas barras distintas usas?", "3", "Son las barras 1, 3 y 5; se repiten la 3 y la 1."),
    ],
    [
        ex("Juan sopla muy fuerte la flauta para que se oiga más. ¿Qué pasa en el sonido: queda más lindo o chillón?", "Chillón", "Soplar fuerte hace que la nota se desafine."),
        ex("Para marcar un pulso grave y firme, ¿qué sirve mejor: bombo, flauta dulce o maracas?", "Bombo", "Es de percusión y grave."),
    ],
    [
        ex("Un grupo toca una melodía con flauta, pulso con bombo y ritmo con claves. ¿Cuántos papeles distintos hay: melodía, pulso y ritmo?", "3", "Cada instrumento hace un papel distinto."),
        arith("En un ensayo, 5 estudiantes tocan metalófono, 8 flauta dulce y 12 percusión. ¿Cuántos músicos hay?", "5+8+12", "Se suman los tres grupos.", " músicos"),
    ],
    [ex("Tu curso toca una pieza con 3 instrumentos: pandero para el pulso, metalófono para la melodía y claves para un ritmo. ¿Cuál de los tres es melódico?", "El metalófono", "Los otros dos son de percusión sin altura definida.")],
    [ex("¿Cuál instrumento tiene barras afinadas?", "El metalófono", "Cada barra tiene una nota."), ex("¿Qué se debe cuidar al tocar en grupo?", "El volumen y el pulso común", "Protege los oídos y mantiene el conjunto."), ex("¿Dónde se golpea la barra del metalófono?", "Al centro", "Ahí suena mejor.")],
    (
        "Lee este plan de 4 compases en 4/4 inventado: bombo en los pulsos 1 y 3, claves en todos los pulsos, y una melodía para metalófono o voz: 3-3-4-5 | 5-4-3-2 | 1-2-3-3 | 2-2-1-1 (un número por pulso). Si no tienes instrumentos, usa palmas fuertes en vez de bombo, golpecitos de dedos en vez de claves y «la» para la melodía. Escribe cuántos golpes hay en el bombo y en las claves en los 4 compases y toca cada parte por separado, lento.",
        "Bombo: 2 golpes por compás × 4 compases = 8 golpes. Claves: 4 por compás × 4 compases = 16 golpes. La melodía tiene 16 notas, una por pulso.",
        ["cuenta bien los golpes", "mantiene el pulso al tocar cada parte", "cuida el volumen y los instrumentos"],
        ["conteo escrito", "ensayo realizado"],
        ["tocar muy fuerte", "no mantener el pulso"],
        "Reconoce el conteo y pide tocar solo el bombo con las claves para comprobar que coinciden en el pulso 1.",
    ),
    "Practica 8 pulsos de claves con golpecitos de dedos y descansa 4 pulsos.",
    "Inventa un ritmo de 2 compases para pandero y claves y escríbelo con figuras.",
)

# ---------------------------------------------------------------- OA 04 · clase 3 (acompañamiento armónico)
ACORDES = "acorde I = 1-3-5 (do, mi, sol); acorde IV = 4-6-8 (fa, la, do agudo); acorde V = 5-7-2 (sol, si, re)"

L(
    OA4, 3,
    f"Lápiz y papel. Acordes de la clase: {ACORDES}. Si hay guitarra o teclado en el colegio, el docente muestra los acordes; en casa trabaja con los números y tu voz. Cuida el volumen.",
    "Aprenderé qué es un acorde y cómo acompañar una melodía con acordes en guitarra o teclado (instrumentos armónicos). Sirve para que una melodía suene respaldada por una armonía.",
    ["Sé que una melodía se escribe con números.", "Sé que varios sonidos pueden sonar a la vez.", "Sé contar compases y pulsos."],
    [
        f"Un acorde es un grupo de tres o más sonidos que suenan a la vez. Los instrumentos armónicos, como la guitarra y el teclado, pueden tocar acordes mientras otra voz canta la melodía. En esta clase usamos tres: {ACORDES}. Un conjunto de acordes uno tras otro se llama progresión. En el acorde V, el 2 es el re que queda justo arriba del 7.",
        "Para acompañar una melodía, se elige para cada compás un acorde que contenga la nota más importante de la melodía en ese compás, por ejemplo la que cae en el primer pulso. Si esa nota es 3, sirve el acorde I (1-3-5). Si es 6, sirve el IV (4-6-8). Si es 7, sirve el V (5-7-2). Algunas notas están en dos acordes, y entonces hay más de una elección.",
        "Los acordes se tocan de varias formas: todas las notas a la vez o una por una (arpegio). En la guitarra se rasguea con la mano; en el teclado se pulsan varias teclas. Una progresión muy usada es I – IV – V – I, que se siente como salir de la casa, viajar y volver. Lo importante es que el acompañamiento mantenga el pulso y no tape la melodía.",
    ],
    [("acorde", "tres o más sonidos que suenan a la vez"), ("progresión", "acordes que suenan uno tras otro"), ("instrumento armónico", "instrumento que toca acordes, como guitarra y teclado"), ("arpegio", "las notas de un acorde tocadas una por una"), ("acompañamiento", "música de fondo que respalda a la melodía")],
    [
        ("Elegir el acorde", "La nota más importante de un compás es 6. ¿Qué acorde sirve: I, IV o V?", ["I tiene 1-3-5: no contiene 6.", "IV tiene 4-6-8: contiene 6.", "V tiene 5-7-2: no contiene 6."], "El acorde IV"),
        ("Completar la progresión", "En la progresión I – IV – V – I, ¿cuántos acordes distintos se usan?", ["Los acordes son I, IV, V e I.", "El I se repite; las ideas distintas son 3."], "3 acordes distintos"),
    ],
    [
        ("Elegir un acorde que no contiene la nota de la melodía.", "El acorde debe incluir la nota principal del compás.", "Revisa las notas del acorde antes de elegir."),
        ("Tocar el acompañamiento muy fuerte.", "El acompañamiento no debe tapar la melodía.", "Usa dinámica suave en el acompañamiento."),
    ],
    [
        ex("¿Cuántos sonidos tiene como mínimo un acorde?", "Tres", "Un acorde reúne tres o más sonidos."),
        ex("¿Cuál instrumento puede tocar acordes: la guitarra o la flauta dulce?", "La guitarra", "La flauta dulce da un solo sonido a la vez."),
        ex("¿Qué notas tiene el acorde I?", "1-3-5", "Así lo define la clase."),
    ],
    [
        ex("La nota principal de un compás es 7. ¿Qué acorde sirve?", "El V", "El V tiene 5-7-2."),
        ex("La nota principal de un compás es 4. ¿Qué acorde sirve?", "El IV", "El IV tiene 4-6-8."),
        ex("La nota principal de un compás es 2. ¿Qué acorde sirve?", "El V", "Solo el V contiene 2."),
    ],
    [
        ex("Las notas principales de 4 compases son 3, 6, 7 y 3. ¿Qué progresión de acordes sirve?", "I – IV – V – I", "Se elige el acorde que contiene cada nota."),
        arith("En una canción de 8 compases, una guitarrista rasguea 4 veces por compás. ¿Cuántos rasgueos hace?", "8*4", "Se multiplica por los compases.", " rasgueos"),
        ex("Tocas el acorde V una nota por vez: 5, 7, 2. ¿Cómo se llama esa forma de tocar el acorde?", "Arpegio", "Las notas del acorde suenan una por una."),
    ],
    [
        ex("Ana dice que la nota 5 solo está en el acorde I. ¿Tiene razón?", "No: el 5 está en el acorde I y también en el V", "El I tiene 1-3-5 y el V tiene 5-7-2."),
        ex("Un acompañamiento suena tan fuerte que no se oye la melodía. ¿Qué debe cambiar: la dinámica del acompañamiento o la melodía?", "La dinámica del acompañamiento", "Debe sonar más suave que la melodía."),
    ],
    [
        ex("Las notas principales de 4 compases son 3, 4, 7 y 3. ¿Qué progresión sirve?", "I – IV – V – I", "El 4 está en el IV y el 7 en el V."),
        arith("Una progresión I – IV – V – I dura un compás de 4 pulsos por acorde y se repite 5 veces. ¿Cuántos pulsos suena?", "4*4*5", "Son 4 acordes por vuelta, 4 pulsos cada uno, 5 veces.", " pulsos"),
    ],
    [ex("Un cantante entona una melodía cuya nota principal en el primer compás es 3 y en el segundo es 6. ¿Qué dos acordes tocarías en una guitarra para esos dos compases?", "I y luego IV", "El 3 está en el I y el 6 en el IV.")],
    [ex("¿Qué es una progresión?", "Acordes que suenan uno tras otro", "Define el concepto de la clase."), ex("¿Qué es un instrumento armónico?", "Uno que toca acordes", "Por ejemplo guitarra y teclado."), ex("¿Qué acorde contiene el 7?", "El V", "El V es 5-7-2.")],
    (
        "Acompaña esta melodía inventada de 4 compases, con una nota principal en el primer pulso de cada compás: compás 1: 3, compás 2: 6, compás 3: 7, compás 4: 3. Escribe qué acorde (I, IV o V) usarás en cada compás y por qué. Si tienes guitarra o teclado, tócalos con ayuda; si no, canta las notas del acorde con «la», una por una (arpegio). Cuida que el acompañamiento sea más suave que la melodía.",
        "Compás 1: I (contiene 3). Compás 2: IV (contiene 6). Compás 3: V (contiene 7). Compás 4: I (contiene 3). La progresión es I – IV – V – I. Como arpegio canto: 1-3-5, 4-6-8, 5-7-2, 1-3-5.",
        ["elige el acorde correcto para cada nota", "justifica con las notas del acorde", "mantiene el acompañamiento suave"],
        ["tabla escrita", "arpegio cantado"],
        ["elegir un acorde sin la nota de la melodía", "tapar la melodía con el acompañamiento"],
        "Reconoce la elección y pide mostrar con el dedo la nota de la melodía dentro del acorde elegido.",
    ),
    "Canta con «la» las notas del acorde I una por una.",
    "Cambia la nota principal del compás 3 por 2 y escribe qué acorde usarías.",
)

# ---------------------------------------------------------------- OA 04 · clase 4 (conjunto: coordinar voces e instrumentos)
PLAN4 = "Compases 1 a 4: solo percusión; compases 5 a 8: percusión y flauta; compases 9 a 12: percusión, flauta y voces; compases 13 a 16: todos los anteriores más guitarra"

L(
    OA4, 4,
    f"Lápiz y papel. Plan de conjunto de práctica: {PLAN4}. Todas las partes están descritas en los ejercicios. Cuida el volumen y descansa los oídos entre ensayos.",
    "Aprenderé a tocar y cantar en conjunto: mantener un pulso común, entrar a tiempo, equilibrar los volúmenes y escucharnos. Sirve para que un grupo suene como uno solo.",
    ["Sé cantar al unísono y a más voces.", "Sé qué hacen la percusión, los instrumentos melódicos y los armónicos.", "Sé contar compases."],
    [
        "Un conjunto es un grupo que toca o canta junto. Para que suene bien, todos necesitan el mismo pulso, que lo marca la percusión o una persona que dirige con la mano. También necesitan una señal clara de inicio, por ejemplo una cuenta de un compás en silencio, y un plan que diga en qué compás entra cada parte.",
        "Cada parte tiene un papel: la percusión marca el pulso y el ritmo, la voz o un instrumento melódico lleva la melodía y la guitarra o el teclado hacen el acompañamiento. El equilibrio es que se oiga la melodía por sobre el acompañamiento, y que ningún instrumento tape a los otros. Si alguien se pierde, no se detiene a todos: escucha el pulso y vuelve a entrar en el próximo compás.",
        "Un buen ensayo trabaja por partes. Primero cada grupo ensaya lento y por separado; luego se juntan de a dos; después todos. Después de cada vuelta, el grupo conversa: ¿se mantuvo el pulso?, ¿entramos juntos?, ¿se oyó la melodía? Esa revisión permite ajustar sin culpar a nadie y mejora el resultado.",
    ],
    [("conjunto", "grupo que toca o canta junto"), ("pulso común", "latido compartido por todo el grupo"), ("entrada", "momento en que una parte empieza a sonar"), ("equilibrio", "que cada parte se oiga con el volumen adecuado"), ("ensayo", "práctica del grupo para mejorar su interpretación")],
    [
        ("Leer el plan", "En el plan «compases 1 a 4: percusión; 5 a 8: percusión y flauta; 9 a 12: todos», ¿en qué compás entra la flauta?", ["La flauta aparece en la segunda parte.", "La segunda parte empieza en el compás 5."], "En el compás 5"),
        ("Contar los que suenan", "En ese mismo plan, ¿cuántos grupos suenan en el compás 10?", ["El compás 10 está en la tercera parte.", "Ahí suenan percusión, flauta y el resto: todos."], "Todos los grupos"),
    ],
    [
        ("Seguir tocando fuerte para que no se pierda mi parte.", "El volumen excesivo tapa a los demás y rompe el equilibrio.", "Toca a un volumen que deje oír la melodía."),
        ("Detener a todo el grupo cada vez que alguien se equivoca.", "Detener a todos corta el pulso; es mejor volver a entrar en el siguiente compás.", "Escucha el pulso y reingresa."),
    ],
    [
        ex("¿Qué es un conjunto?", "Un grupo que toca o canta junto", "Es la definición de la clase."),
        ex("¿Quién marca el pulso en el plan de práctica: la percusión o la guitarra?", "La percusión", "En el plan, la percusión suena desde el compás 1."),
        ex("Si alguien se pierde, ¿qué debe hacer: parar a todos o volver a entrar en el siguiente compás?", "Volver a entrar en el siguiente compás", "Así se mantiene el pulso del grupo."),
    ],
    [
        ex(f"Según el plan «{PLAN4}», ¿en qué compás entran las voces?", "9", "La entrada de las voces está en la tercera parte."),
        ex(f"Según ese plan, ¿cuántos grupos suenan en el compás 6?", "2", "Suenan la percusión y la flauta."),
        ex(f"Según ese plan, ¿qué grupo entra al final, en el compás 13?", "La guitarra", "Se suma en la cuarta parte."),
    ],
    [
        arith("Según el plan de práctica, los compases con solo percusión son 4. Si cada compás tiene 4 pulsos y el tempo es 80 por minuto, ¿cuántos segundos dura esa parte?", "4*4*60//80", "Son 16 pulsos y cada pulso dura 0,75 segundos.", " segundos"),
        arith("En el plan de práctica, ¿cuántos compases suenan con flauta (desde el compás 5 hasta el 16)?", "16-5+1", "Se cuentan los compases 5 a 16 inclusive.", " compases"),
        ex("Un conjunto de 20 estudiantes se reparte en percusión (6), flauta (7) y el resto en voces. ¿Cuántos son las voces?", "7", "20 − 6 − 7 = 7."),
    ],
    [
        ex("Mara dice que el conjunto está equilibrado porque se oye muy fuerte la guitarra. ¿Tiene razón?", "No: si tapa a la melodía, el equilibrio falló", "El equilibrio busca que cada parte se oiga con el volumen adecuado."),
        ex("Un conjunto no logra entrar junto en el compás 9. ¿Qué ayuda más: una cuenta en silencio de un compás antes de la entrada o tocar más fuerte?", "Una cuenta en silencio de un compás antes de la entrada", "Da la señal de inicio para entrar a tiempo."),
    ],
    [
        ex(f"Con el plan «{PLAN4}», ¿cuántos compases suenan los cuatro grupos a la vez?", "4", "Es la última parte, compases 13 a 16."),
        arith("Un conjunto ensaya primero 3 partes por separado, de 5 minutos cada una, y luego junta todo durante 6 minutos. ¿Cuántos minutos ensaya?", "3*5+6", "Se suman los tres ensayos por separado y el ensayo conjunto.", " minutos"),
    ],
    [ex("Un coro y una guitarra ensayan una canción de 8 compases. En el ensayo, la guitarra tapa la voz. ¿Qué cambio es mejor: que la guitarra toque más suave o que el coro grite más?", "Que la guitarra toque más suave", "Gritar daña la voz y el equilibrio se logra con un acompañamiento más suave.")],
    [ex("¿Qué es el equilibrio en un conjunto?", "Que cada parte se oiga con el volumen adecuado", "La melodía no debe quedar tapada."), ex("En un plan de conjunto, ¿cómo se llama el momento en que una parte empieza a sonar?", "Entrada", "Se planifica en compases."), ex("¿Con qué se ensaya primero?", "Por partes, lento y por separado", "Es el orden de trabajo.")],
    (
        f"Usa este plan de conjunto: «{PLAN4}». Tu tarea: elige un papel (percusión, flauta, voces o guitarra) y escribe en qué compás entras, cuántos compases tocas y qué volumen usarás en cada parte (suave, medio o fuerte) para mantener el equilibrio. Luego ensaya tu papel con tu voz o con golpecitos de dedos, cuidando el pulso. Si trabajas con otras personas, ensayen los cuatro roles por separado y luego juntos, y conversen al final qué mejoró.",
        "Elijo voces. Entro en el compás 9 y canto 8 compases (9 a 16). Volumen: medio en los compases 9 a 16, para que la melodía se oiga sobre la percusión y la flauta; en el compás 13 la guitarra entra más suave que las voces para no taparlas. Ensayé por partes y conté un compás en silencio antes de entrar.",
        ["indica correctamente la entrada y los compases", "describe un volumen adecuado para el equilibrio", "ensaya cuidando el pulso"],
        ["plan escrito", "ensayo realizado"],
        ["contar mal los compases", "usar volumen excesivo"],
        "Reconoce el plan y pide mostrar cómo marcaría el pulso antes de entrar.",
    ),
    "Cuenta en silencio un compás de 4 pulsos y comienza a tocar o cantar en el pulso 1.",
    "Escribe un plan de conjunto de 16 compases para tres grupos con una entrada distinta cada 4 compases.",
)
