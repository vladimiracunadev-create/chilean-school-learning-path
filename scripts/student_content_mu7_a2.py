"""Student material for 7.º básico Música, OA 02 (identificar los elementos del lenguaje musical y los procedimientos compositivos evidentes).

Todas las músicas de los ejercicios son esquemas, números de nota y descripciones inventados para esta clase; las audiciones reales las selecciona y pone el docente.
"""
from __future__ import annotations

from student_content_mu7_a import L
from student_lessons import arith, ex

OA2 = "MU07 OA 02"

NOTAS = "1 = do, 2 = re, 3 = mi, 4 = fa, 5 = sol, 6 = la, 7 = si, 8 = do agudo"
LEY = ("semicorchea = 1 unidad; corchea = 2; corchea con puntillo = 3; negra = 4 (un pulso); negra con puntillo = 6; blanca = 8; "
       "blanca con puntillo = 12; redonda = 16; cada silencio dura lo mismo que su figura")

# ---------------------------------------------------------------- OA 02 · clase 1 (ritmo y compás medidos en unidades)
L(
    OA2, 1,
    f"Lápiz y papel. Leyenda de duraciones de la clase: {LEY}. Todos los patrones están escritos en los ejercicios. Si quieres, palmea cada patrón a volumen bajo.",
    "Aprenderé a medir el ritmo con una unidad pequeña (la semicorchea) para saber si un patrón llena un compás de 2/4, 3/4 o 4/4. Sirve para identificar el ritmo con precisión, sin adivinar.",
    ["Sé que el pulso es el latido parejo de la música.", "Sé que un compás agrupa pulsos y que 4/4 tiene 4 pulsos.", "Sé sumar y dividir números pequeños."],
    [
        "El ritmo es la forma en que se combinan sonidos largos, cortos y silencios sobre el pulso. Para medirlo usamos una unidad pequeña: la duración de una semicorchea. Con esa unidad, la negra (un pulso) dura 4 unidades y la corchea dura 2. Como cada pulso tiene 4 unidades, un compás de 2/4 tiene 8 unidades, uno de 3/4 tiene 12 y uno de 4/4 tiene 16.",
        "El puntillo es un punto que se escribe junto a una figura y le suma la mitad de su duración. Por eso la negra con puntillo dura 4 + 2 = 6 unidades y la blanca con puntillo dura 8 + 4 = 12. Los silencios cuentan igual que los sonidos, porque ocupan el mismo tiempo aunque no suenen. Para ver si un patrón llena un compás, se suman las unidades de todas sus figuras.",
        "Si la suma es igual a las unidades del compás, el patrón lo llena justo. Si es menor, falta una figura; si es mayor, se pasa. Por ejemplo, negra, corchea, corchea y blanca suman 4 + 2 + 2 + 8 = 16 y llenan un compás de 4/4. Medir así permite identificar un ritmo con exactitud y descubrir qué figura falta para completarlo.",
    ],
    [("unidad", "duración de una semicorchea, que sirve para medir el ritmo"), ("puntillo", "punto que suma a una figura la mitad de su duración"), ("silencio", "pausa que dura lo mismo que su figura pero no suena"), ("compás 2/4, 3/4, 4/4", "grupo de 2, 3 o 4 pulsos"), ("semicorchea", "figura que dura la cuarta parte de un pulso")],
    [
        ("Ver qué falta", "En un compás de 4/4 hay una blanca, una negra, una corchea y una semicorchea. ¿Qué le falta para llenarlo?", ["Suma: 8 + 4 + 2 + 1 = 15 unidades.", "El compás de 4/4 tiene 16, así que falta 1 unidad."], "Falta 1 unidad: una semicorchea"),
        ("Contar compases", "Una pieza en 3/4 dura 60 unidades. ¿Cuántos compases completos tiene?", ["Cada compás de 3/4 tiene 12 unidades.", "60 ÷ 12 = 5."], "5 compases"),
    ],
    [
        ("Contar las figuras en vez de sumar lo que duran.", "Una figura larga ocupa más tiempo que una corta, aunque cada una cuente como una.", "Suma las unidades de cada figura, silencios incluidos."),
        ("Olvidar que el puntillo suma la mitad.", "Sin el puntillo la negra dura 4 y con él dura 6.", "Pon la mitad de la figura y súmala."),
    ],
    [
        ex("Según la leyenda de la clase, ¿cuántas unidades dura una negra?", "4", "La leyenda dice que la negra dura 4 unidades (un pulso)."),
        ex("¿Cuántas corcheas caben en una negra?", "2", "La corchea dura 2 unidades y la negra 4."),
        arith("¿Cuántas unidades tiene un compás de 3/4?", "3*4", "Son 3 pulsos de 4 unidades cada uno.", " unidades"),
    ],
    [
        ex("¿Llena exactamente un compás de 4/4 el patrón negra, corchea, corchea, blanca? Responde sí o no.", "Sí", "4 + 2 + 2 + 8 suman 16 unidades, igual que el compás."),
        ex("Una corchea con puntillo más una semicorchea, ¿a qué figura equivalen en duración?", "A una negra", "3 + 1 = 4 unidades, igual que una negra."),
        ex("¿Dura más una blanca con puntillo o cinco corcheas?", "La blanca con puntillo", "La blanca con puntillo dura 12 unidades y cinco corcheas suman 10."),
    ],
    [
        arith("Un compás de 4/4 tiene cuatro semicorcheas, una negra, dos corcheas y una negra. ¿Cuántas unidades suma?", "4*1+4+2*2+4", "Se suman las unidades de cada grupo de figuras.", " unidades"),
        ex("En un compás de 4/4 aparece una blanca con puntillo. ¿Qué figura falta para llenarlo: una negra o una corchea?", "Una negra", "Falta 16 − 12 = 4 unidades, que es una negra."),
        ex("Un compás de 2/4 contiene negra, corchea, silencio de corchea y semicorchea. ¿Llena el compás, le falta o se pasa? Di por cuántas unidades.", "Se pasa por 1 unidad", "Suman 4 + 2 + 2 + 1 = 9 y el compás de 2/4 tiene 8."),
    ],
    [
        ex("Beto dice que una corchea con puntillo más una semicorchea dura lo mismo que una negra. ¿Tiene razón? Responde sí o no.", "Sí", "3 + 1 = 4, igual que la negra."),
        arith("Ana quiere llenar un compás de 3/4 usando solo corcheas. ¿Cuántas corcheas necesita?", "12//2", "El compás tiene 12 unidades y cada corchea ocupa 2.", " corcheas"),
    ],
    [
        arith("Una pieza en 4/4 dura 80 unidades. ¿Cuántos compases completos tiene?", "80//16", "Cada compás de 4/4 tiene 16 unidades.", " compases"),
        ex("Un compás de 4/4 tiene negra, silencio de corchea, corchea y una figura final. ¿Cuántas unidades debe durar la figura final?", "8", "4 + 2 + 2 = 8 y faltan 16 − 8 = 8 unidades, o sea una blanca."),
    ],
    [arith("En una banda escolar, el patrón de marcha en 2/4 es corchea con puntillo, semicorchea, corchea y corchea. ¿Cuántas unidades suma?", "3+1+2+2", "Suma las unidades de cada figura; coincide con las 8 unidades de un compás de 2/4.", " unidades")],
    [ex("¿Cuántas unidades dura una semicorchea?", "1", "Es la unidad de medida de la clase."), ex("¿Cuántas unidades tiene un compás de 4/4?", "16", "Son 4 pulsos de 4 unidades."), ex("¿Qué hace el puntillo con una figura?", "Le suma la mitad de su duración", "Por eso una negra con puntillo dura 6 unidades.")],
    (
        f"Con la leyenda ({LEY}), escribe dos compases de 4/4 distintos. En cada uno usa al menos dos tipos de figura distintos y puedes usar silencios. Debajo de cada compás escribe la suma de unidades y comprueba que da 16. Si quieres, palmea cada compás a volumen bajo con un pulso de negras.",
        "Compás 1: negra con puntillo, corchea, blanca = 6 + 2 + 8 = 16. Compás 2: cuatro semicorcheas, silencio de negra, corchea, corchea, negra = 4 + 4 + 2 + 2 + 4 = 16.",
        ["cada compás suma exactamente 16", "usa figuras distintas", "muestra la suma"],
        ["dos compases escritos", "suma de unidades"],
        ["olvidar la mitad que suma el puntillo", "no contar los silencios"],
        "Reconoce la suma y pide revisar, figura por figura, cuántas unidades aporta cada una.",
    ),
    "Escribe las unidades de blanca, negra, corchea y semicorchea y súmalas.",
    "Escribe un compás de 3/4 con una corchea con puntillo y comprueba que suma 12 unidades.",
)

# ---------------------------------------------------------------- OA 02 · clase 2 (melodía y armonía)
L(
    OA2, 2,
    f"Lápiz y papel. Escala de números: {NOTAS}. Acordes de la clase: I = 1-3-5; IV = 4-6-8; V = 5-7-2. Todo está escrito en los ejercicios; si tienes un teclado puedes comprobarlos, pero no es necesario.",
    "Aprenderé la diferencia entre melodía (notas una tras otra) y armonía (notas al mismo tiempo), y a reconocer tres acordes básicos y su progresión. Sirve para identificar de qué está hecha una música.",
    ["Sé que una melodía se puede escribir con números del 1 al 8.", "Sé que algunos sonidos pueden sonar a la vez.", "Sé sumar y multiplicar números pequeños."],
    [
        f"La melodía son los sonidos de distinta altura que suenan uno tras otro, como los de una canción cantada. La armonía son los sonidos distintos que suenan al mismo tiempo. Tres sonidos que suenan juntos forman un acorde. Con la escala de números ({NOTAS}) podemos escribir los acordes de la clase: el acorde I es 1-3-5 (do-mi-sol), el acorde IV es 4-6-8 (fa-la-do) y el acorde V es 5-7-2 (sol-si-re).",
        "Una progresión armónica es el orden en que suenan los acordes. La más conocida es I – IV – V – I. El acorde I suena a reposo, a lugar de llegada. El acorde V suele dar tensión, como una pregunta sin cerrar, y por eso muchas músicas lo usan antes de volver al I. El acorde IV suena a movimiento intermedio, entre el reposo y la tensión.",
        "Para identificar la armonía de una música, se mira qué notas suenan juntas. Si suenan 4, 6 y 8 a la vez, hay un acorde IV. Una melodía puede acompañarse con acordes que contengan sus notas: si la melodía usa la nota 3, el acorde I encaja porque la contiene. Escuchar la armonía nos ayuda a explicar por qué una música suena estable o tensa.",
    ],
    [("melodía", "sonidos de distinta altura que suenan uno tras otro"), ("armonía", "sonidos distintos que suenan al mismo tiempo"), ("acorde", "tres sonidos que suenan juntos"), ("progresión", "orden en que suenan los acordes"), ("reposo y tensión", "sensación de llegada o de algo sin cerrar")],
    [
        ("Buscar el acorde", "La nota 6 (la) suena en una melodía. ¿Cuál de los tres acordes de la clase la contiene?", ["I = 1-3-5, no tiene el 6.", "IV = 4-6-8, sí lo tiene.", "V = 5-7-2, no lo tiene."], "El acorde IV"),
        ("Escribir una progresión", "Escribe los números de las notas de la progresión I – IV – V.", ["I = 1-3-5.", "IV = 4-6-8.", "V = 5-7-2."], "1-3-5, 4-6-8, 5-7-2"),
    ],
    [
        ("Llamar melodía a tres notas que suenan juntas.", "Tres notas a la vez son un acorde; la melodía va una nota tras otra.", "Pregunta si las notas suenan juntas o una después de otra."),
        ("Creer que el acorde V descansa.", "El V suele dar tensión; el reposo lo da el I.", "Después del V suele volver el I."),
    ],
    [
        ex("Notas que suenan una tras otra, ¿forman una melodía o un acorde?", "Una melodía", "La melodía son sonidos sucesivos."),
        ex("En el acorde I = 1-3-5, ¿qué número falta si se escribe 1-3-_?", "5", "El acorde I tiene las notas 1, 3 y 5."),
        ex("¿Cuántas notas tiene cada acorde de la clase?", "3", "Los acordes I, IV y V tienen tres notas."),
    ],
    [
        ex("La nota 7 (si) aparece en un solo acorde de la clase. ¿En cuál: I, IV o V?", "V", "El acorde V es 5-7-2."),
        ex("¿Cuál de los acordes de la clase suena a reposo?", "El acorde I", "El I es la llegada; el V da tensión."),
        ex("Si suenan a la vez las notas 4, 6 y 8, ¿qué acorde es?", "El acorde IV", "Esas son las notas del IV."),
    ],
    [
        ex("La progresión es I – IV – V – I. Escribe los números de las notas del segundo acorde.", "4-6-8", "El segundo acorde de la progresión es el IV."),
        ex("La nota 2 (re) aparece en uno solo de los acordes de la clase. ¿En cuál?", "V", "Solo el acorde V = 5-7-2 la contiene."),
        arith("Cada acorde de la progresión I – IV – V – I dura un compás de 3 pulsos. ¿Cuántos pulsos dura la progresión completa?", "4*3", "Hay 4 acordes de 3 pulsos cada uno.", " pulsos"),
    ],
    [
        ex("Carla dice que 1-3-5 es una melodía porque son números. ¿Qué tendría que ocurrir para que sea un acorde?", "Que las tres notas suenen al mismo tiempo", "El acorde se define por sonar junto, no por sus números."),
        ex("Una melodía usa solo las notas 4, 6 y 8. ¿Qué acorde la acompaña mejor porque contiene todas sus notas?", "El acorde IV", "Contiene exactamente 4, 6 y 8."),
    ],
    [
        ex("¿Qué número tienen en común los acordes I = 1-3-5 y V = 5-7-2?", "El 5", "Es el único número que aparece en ambos."),
        ex("Una melodía usa en su primer compás las notas 5, 7 y 2 y en el segundo las notas 1, 3 y 5. ¿Qué acordes la acompañan en ese orden?", "V y luego I", "El primer compás tiene las notas del V y el segundo las del I."),
    ],
    [arith("Un guitarrista toca la progresión I – IV – V – I, un acorde por compás, en una canción de 16 compases. ¿Cuántas veces toca el acorde V?", "16//4", "La progresión de 4 compases se repite 16 ÷ 4 veces y trae un V cada vez.", " veces")],
    [ex("¿Qué es la armonía?", "Sonidos distintos que suenan al mismo tiempo", "Se diferencia de la melodía, que va una nota tras otra."), ex("¿Qué número de la escala corresponde a la nota fa?", "4", "En la escala de la clase 4 = fa."), ex("¿Qué progresión es la más conocida de la clase?", "I – IV – V – I", "Es la que combina reposo, movimiento y tensión.")],
    (
        f"Con los acordes I = 1-3-5, IV = 4-6-8 y V = 5-7-2, escribe una progresión de 4 acordes que empiece y termine en I. Debajo de cada acorde escribe sus tres números y marca cuál da reposo y cuál da tensión. Después escribe una melodía de 4 notas que use solo números que aparezcan en el primer acorde de tu progresión. Si tienes un teclado, tócalas despacio.",
        "Progresión: I – IV – V – I = 1-3-5, 4-6-8, 5-7-2, 1-3-5. Reposo: I; tensión: V. Melodía sobre el primer acorde: 1-3-5-3, que usa solo números de 1-3-5.",
        ["progresión de 4 acordes que empieza y termina en I", "escribe bien los números de cada acorde", "la melodía usa solo notas del acorde elegido"],
        ["progresión escrita", "melodía de 4 notas"],
        ["confundir melodía con acorde", "usar notas que no están en el acorde"],
        "Reconoce la progresión y pide comprobar nota por nota que la melodía solo usa números del acorde.",
    ),
    "Escribe los números de los tres acordes de la clase sin mirar.",
    "Escribe una progresión de 6 acordes con I, IV y V que termine en I y explica dónde hay tensión.",
)

# ---------------------------------------------------------------- OA 02 · clase 3 (timbre y textura)
L(
    OA2, 3,
    "Lápiz y papel. Los conjuntos instrumentales están descritos en los ejercicios. Puedes imitar con tu voz o con objetos limpios y seguros las capas de sonido, a volumen bajo.",
    "Aprenderé a reconocer el timbre por familias de instrumentos y la textura de una música (monofonía, homofonía y polifonía). Sirve para describir quién suena, cuántas capas hay y cómo se relacionan.",
    ["Sé que cada instrumento suena distinto.", "Sé que hay melodía y acompañamiento.", "Sé contar elementos de una lista."],
    [
        "El timbre es el color propio de un sonido, y permite distinguir un instrumento de otro. Los instrumentos se agrupan en familias. En las cuerdas el sonido nace de cuerdas que vibran: violín, viola, violonchelo, guitarra, charango. En los vientos el sonido nace del aire: flauta, clarinete, trompeta y también la quena y la zampoña. En la percusión se golpea, sacude o raspa: bombo, tambor, maracas. La voz humana es otro timbre, y puede ser aguda o grave.",
        "La textura es cuántas capas suenan y cómo se relacionan. En la monofonía hay una sola melodía, aunque la canten o toquen muchas personas todas en las mismas notas. En la homofonía hay una melodía principal acompañada por acordes o un ritmo de fondo. En la polifonía suenan dos o más melodías distintas a la vez, como en un canon, donde una voz imita a otra unos compases después.",
        "Contar instrumentos no basta para saber la textura: lo que importa es qué hace cada uno. Diez instrumentos que tocan la misma melodía forman una monofonía. Una cantante con una guitarra que hace acordes forman una homofonía. Dos flautas que tocan melodías distintas a la vez forman una polifonía. Identificar timbres y texturas nos ayuda a describir con precisión una música que escuchamos o creamos.",
    ],
    [("timbre", "color propio de un instrumento o voz"), ("familia de instrumentos", "grupo de instrumentos que producen el sonido de manera parecida"), ("monofonía", "una sola melodía, tocada por una o muchas personas"), ("homofonía", "una melodía principal con acordes o ritmo de fondo"), ("polifonía", "dos o más melodías distintas a la vez")],
    [
        ("Reconocer la textura", "Una cantante canta la melodía y un guitarrista toca acordes. ¿Qué textura hay?", ["Hay una melodía principal.", "Otro instrumento acompaña con acordes."], "Homofonía"),
        ("Contar familias", "Un grupo tiene guitarra, flauta, charango, bombo y tambor. ¿Cuántas familias distintas hay?", ["Guitarra y charango: cuerdas.", "Flauta: vientos.", "Bombo y tambor: percusión."], "3 familias"),
    ],
    [
        ("Decir que muchos instrumentos siempre hacen polifonía.", "Si todos tocan la misma melodía hay monofonía; la polifonía exige melodías distintas.", "Pregunta cuántas melodías distintas suenan a la vez."),
        ("Confundir el timbre con el registro.", "El timbre es el color del instrumento; el registro es qué tan grave o agudo suena.", "Pregunta: ¿qué instrumento es? (timbre) ¿qué tan alto suena? (registro)."),
    ],
    [
        ex("La guitarra, ¿es de la familia de las cuerdas, los vientos o la percusión?", "Cuerdas", "Su sonido nace de cuerdas que vibran."),
        ex("La trompeta, ¿es de la familia de las cuerdas, los vientos o la percusión?", "Vientos", "Su sonido nace del aire."),
        ex("El bombo, ¿es de la familia de las cuerdas, los vientos o la percusión?", "Percusión", "Se toca golpeándolo."),
    ],
    [
        ex("Cinco personas cantan la misma melodía en las mismas notas a la vez. ¿Qué textura hay: monofonía, homofonía o polifonía?", "Monofonía", "Hay una sola melodía, aunque la canten varias personas."),
        ex("Dos voces cantan melodías distintas a la vez, cada una con su propio ritmo. ¿Qué textura hay?", "Polifonía", "Hay dos melodías distintas al mismo tiempo."),
        ex("Una voz canta una melodía y un piano repite acordes de fondo. ¿Qué textura es?", "Homofonía", "Melodía principal con acompañamiento de acordes."),
    ],
    [
        ex("Un grupo tiene violín, flauta, bombo, guitarra y clarinete. ¿Cuántos son de la familia de los vientos?", "2", "La flauta y el clarinete son vientos."),
        ex("Un cuarteto tiene dos violines, una viola y un violonchelo. ¿Cuántos instrumentos de cuerda hay?", "4", "Los cuatro son de cuerda."),
        ex("Un grupo tiene quena, charango, zampoña y bombo. ¿Cuántos instrumentos de viento hay?", "2", "La quena y la zampoña son vientos."),
    ],
    [
        ex("Tomás dice que diez instrumentos que tocan la misma melodía hacen polifonía. ¿Tiene razón? Responde sí o no.", "No", "Si tocan la misma melodía hay monofonía, no polifonía."),
        ex("Un canon a dos voces: la segunda voz repite la melodía de la primera cuatro compases después. ¿Qué textura es?", "Polifonía", "Hay dos líneas sonando a la vez, aunque con la misma melodía desfasada."),
    ],
    [
        ex("Una pieza tiene la sección A con una voz sola, la B con una voz y una guitarra con acordes, y la C con dos voces de melodías distintas. ¿Qué texturas hay en A, B y C en ese orden?", "Monofonía, homofonía y polifonía", "Una voz sola es monofonía, voz con acordes es homofonía y dos melodías distintas es polifonía."),
        ex("Un grupo toca así: dos instrumentos tocan la misma melodía, uno toca acordes y uno marca el pulso. ¿Cuántas capas distintas hay: melodía, acordes y pulso?", "3", "Cada función distinta es una capa; los dos que tocan la melodía hacen una sola."),
    ],
    [ex("Un grupo toca una melodía con quena y zampoña a la vez (las mismas notas), mientras el charango toca acordes y el bombo marca el pulso. ¿Qué textura tiene: monofonía, homofonía o polifonía?", "Homofonía", "Hay una melodía principal con acompañamiento de acordes y pulso.")],
    [ex("¿Qué familia de instrumentos produce el sonido con cuerdas que vibran?", "Las cuerdas", "El violín, la guitarra y el charango son ejemplos."), ex("¿Qué textura tiene una sola melodía sin acompañamiento?", "Monofonía", "Hay una sola línea."), ex("¿Qué textura exige dos o más melodías distintas a la vez?", "Polifonía", "Es su definición.")],
    (
        "Describe este conjunto inventado: «Una cantante canta una melodía. Una guitarra toca acordes. Un bombo marca el pulso. En la segunda parte entra otra voz que canta una melodía distinta, a la vez que la primera.» Escribe las familias de instrumentos que aparecen, cuántas capas hay en la primera parte, la textura de la primera parte y la textura de la segunda parte.",
        "Familias: voz, cuerdas (guitarra) y percusión (bombo). Primera parte: 3 capas (melodía, acordes y pulso), textura homofonía. Segunda parte: dos melodías distintas a la vez, polifonía.",
        ["nombra las familias de instrumentos", "cuenta las capas de la primera parte", "identifica la textura de las dos partes"],
        ["descripción escrita", "familias y texturas"],
        ["llamar polifonía a la primera parte", "no distinguir voz de instrumento"],
        "Reconoce la descripción y pide señalar en el texto qué instrumento hace la melodía y cuál el acompañamiento.",
    ),
    "Nombra tres instrumentos de cada familia: cuerdas, vientos y percusión.",
    "Describe con familias y textura un conjunto de cuatro instrumentos que tú imagines.",
)

# ---------------------------------------------------------------- OA 02 · clase 4 (procedimientos compositivos evidentes)
L(
    OA2, 4,
    f"Lápiz y papel. Escala de números: {NOTAS}. Todas las melodías están escritas con números en los ejercicios; puedes cantarlas con «la» si quieres, a volumen bajo.",
    "Aprenderé a reconocer procedimientos compositivos que se oyen con claridad: repetición, variación, contraste, secuencia, imitación, ostinato y formas como AB, ABA y rondó. Sirve para explicar cómo está construida una música.",
    ["Sé que una melodía puede escribirse con números.", "Sé que una frase puede repetirse o cambiar.", "Sé contar secciones de una pieza."],
    [
        "Los procedimientos compositivos son recursos que usa quien crea música. Hay tres básicos: la repetición vuelve igual, la variación vuelve con algún cambio y el contraste trae algo distinto. Otros se reconocen por su forma. La secuencia repite un motivo más arriba o más abajo, como 1-2-3 y luego 2-3-4. La imitación hace que una voz repita lo que cantó otra, un poco después. El ostinato es un patrón corto que se repite sin parar mientras otras partes cambian.",
        "Con las secciones se arman formas. En la forma AB hay dos ideas distintas. En la ABA la primera idea vuelve al final. En el rondó la sección A vuelve al menos dos veces, entre secciones distintas, como en ABACA. Cada recurso produce un efecto: la repetición da orden, la variación mantiene el interés, el contraste da novedad y el ostinato da una base firme sobre la que se apoya el resto.",
        "Para identificar un procedimiento hay que comparar. Se escribe cada melodía o sección y se miran las diferencias. Si todo coincide, es repetición. Si cambia poco, variación. Si todo cambia, contraste. Si el motivo conserva su forma pero parte de otra nota, secuencia. Una buena descripción nombra el procedimiento y da la evidencia: qué se mantiene y qué cambia.",
    ],
    [("secuencia", "un motivo que vuelve empezando en otra nota"), ("imitación", "una voz repite lo que cantó otra, un poco después"), ("ostinato", "patrón corto que se repite sin parar"), ("rondó", "forma en que A vuelve al menos dos veces entre secciones distintas"), ("procedimiento compositivo", "recurso que usa quien compone para construir la música"), ("motivo", "idea musical corta, de pocas notas, que se reconoce al oírla")],
    [
        ("Continuar una secuencia", "Un motivo suena 1-2-3, luego 2-3-4 y luego 3-4-5. Si sigue la secuencia, ¿cuál es el siguiente?", ["Cada motivo parte un número más arriba.", "Después de 3-4-5 viene 4-5-6."], "4-5-6"),
        ("Contar secciones", "Una pieza tiene la forma ABACA. ¿Cuántas veces suena A y cuántas secciones distintas hay?", ["Las letras son A, B, A, C, A.", "A suena 3 veces.", "Las distintas son A, B y C."], "A suena 3 veces y hay 3 secciones distintas"),
    ],
    [
        ("Llamar repetición a una idea que vuelve más arriba.", "Si el motivo vuelve en otras notas, es secuencia y no repetición exacta.", "Compara nota por nota si coinciden."),
        ("Pensar que cualquier pieza con A al principio y al final es rondó.", "El rondó pide que A vuelva al menos dos veces; en ABA vuelve una sola.", "Cuenta cuántas veces vuelve A."),
    ],
    [
        ex("Un patrón corto que se repite sin parar mientras otras partes cambian, ¿cómo se llama?", "Ostinato", "Es su definición."),
        ex("Una voz repite lo que cantó otra, un poco después. ¿Qué procedimiento es?", "Imitación", "La segunda voz imita a la primera."),
        ex("Un motivo vuelve empezando en otra nota. ¿Cómo se llama ese procedimiento?", "Secuencia", "Conserva la forma pero cambia la nota de partida."),
    ],
    [
        ex("Una pieza tiene la forma AB. ¿Cuántas ideas distintas tiene?", "2", "A y B son distintas."),
        ex("¿Es un rondó una pieza con la forma ABA? Responde sí o no.", "No", "En ABA la A vuelve solo una vez, y el rondó pide al menos dos regresos."),
        ex("En la forma ABACADA, ¿cuántas secciones distintas hay?", "4", "Las distintas son A, B, C y D."),
    ],
    [
        ex("Voz 1: 3-4-5-3. La voz 2 entra dos pulsos después con 3-4-5-3. ¿Qué procedimiento hay?", "Imitación", "La segunda voz repite la melodía de la primera con retraso."),
        arith("Un ostinato de 4 notas (1-5-1-5) se repite 6 veces. ¿Cuántas notas suenan?", "4*6", "Cada repetición tiene 4 notas.", " notas"),
        ex("Tema: 1-3-5-3-1-3-5. Variación: 1-3-5-3-1-3-6. ¿Cuántas notas cambian?", "1", "Solo la última pasa de 5 a 6."),
    ],
    [
        ex("Marta dice que si un motivo vuelve más arriba es repetición. ¿Es repetición o secuencia?", "Secuencia", "En la repetición las notas son las mismas; aquí cambian de altura."),
        ex("Una pieza va ABACA. ¿Qué forma es: rondó o ABA?", "Rondó", "A vuelve dos veces entre secciones distintas."),
    ],
    [
        arith("En un rondó ABACA, A dura 8 compases, B dura 4 y C dura 4. ¿Cuántos compases tiene en total?", "8*3+4+4", "A suena tres veces; B y C una vez.", " compases"),
        ex("Una melodía repite 1-2-3 sobre un ostinato de 5-5-5. Después de una vuelta, el ostinato sigue y la melodía cambia a 4-5-6. ¿Qué procedimiento hay en la melodía: secuencia o ostinato?", "Secuencia", "El motivo parte más arriba; el ostinato es el patrón que no cambia."),
    ],
    [ex("Una canción tiene verso, coro, verso, puente, coro. Si verso es A, coro es B y puente es C, ¿cómo se escribe su forma?", "ABACB", "Las letras siguen el orden en que aparecen las secciones.")],
    [ex("¿Cómo se llama el patrón corto que se repite sin parar?", "Ostinato", "Es la definición de la clase."), ex("¿Cómo se llama la forma en que A vuelve entre secciones distintas?", "Rondó", "Un ejemplo es la forma ABACA."), ex("¿Qué recurso trae algo totalmente distinto?", "El contraste", "No guarda relación con lo anterior.")],
    (
        "Analiza esta pieza inventada: A = 1-2-3-1; B = 5-6-5-3; A' = 1-2-3-3; C = 8-7-6-5; A = 1-2-3-1. Escribe la forma de la pieza, cuántas veces suena la idea A (incluida su variación), cuál sección es contraste, y cuál procedimiento hay entre A y A'. Justifica con lo que se mantiene y lo que cambia.",
        "Forma: A B A' C A. La idea A suena 3 veces (dos iguales y una variada). B y C son contraste: usan otras notas. Entre A y A' hay variación: se mantienen 1-2-3 y cambia la última nota, de 1 a 3. Es un rondó porque A vuelve dos veces.",
        ["escribe bien la forma", "identifica la variación con evidencia", "reconoce el rondó"],
        ["forma escrita", "justificación"],
        ["llamar contraste a la variación", "no contar la variación como A"],
        "Reconoce la forma y pide mostrar con el dedo nota por nota qué cambia entre A y A'.",
    ),
    "Escribe un motivo de 3 notas y repítelo dos veces en secuencia, un número más alto cada vez (por ejemplo 1-2-3, luego 2-3-4).",
    "Inventa una pieza de forma ABACA con una melodía de 4 números por sección.",
)
