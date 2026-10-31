"""Student material for 7.º básico Música, OA 03 (cantar y tocar repertorio diverso con precisión rítmica y melódica, expresividad, fraseo y dinámica).

Todas las piezas, patrones y letras de los ejercicios son inventados para esta clase; el repertorio real lo elige el docente. Las prácticas son voluntarias en su formato: se pueden hacer en privado, en parejas o en grupo pequeño, sin forzar la exposición de nadie.
"""
from __future__ import annotations

from student_content_mu7_a import L
from student_lessons import arith, ex

OA3 = "MU07 OA 03"
NOTAS = "1 = do, 2 = re, 3 = mi, 4 = fa, 5 = sol, 6 = la, 7 = si, 8 = do agudo"

# ---------------------------------------------------------------- OA 03 · clase 1 (cuerpo, voz y hábitos para interpretar)
L(
    OA3, 1,
    "Lápiz y papel. Los planes y tiempos están escritos en los ejercicios. Para practicar usa tu voz a volumen cómodo, sin gritar, y un vaso de agua cerca. Si algo duele o te cansa, paras.",
    "Aprenderé a preparar el cuerpo y la voz antes de cantar o tocar, y a planear una práctica segura. Sirve para interpretar mejor y sin dañar la voz ni el cuerpo, tanto solo como en grupo.",
    ["Sé cantar o tocar una pieza breve.", "Sé que el pulso es el latido parejo de la música.", "Sé sumar y multiplicar números pequeños."],
    [
        "Cantar y tocar son actividades físicas, y por eso se preparan. La postura ayuda: pies a la altura de los hombros, espalda erguida, hombros y cuello relajados. La respiración da el aire para sostener una frase: se inhala por la nariz o la boca sin levantar los hombros y se exhala despacio. Un ejercicio simple es inhalar 4 tiempos y exhalar 8 tiempos. Un ciclo completo dura entonces 4 + 8 = 12 tiempos.",
        "El calentamiento prepara la voz y las manos antes de la pieza. Tiene cuatro pasos en este orden: 1) respirar, 2) soltar hombros y cuello, 3) tararear suave y 4) vocalizar con una «a» suave. Se hace a volumen cómodo. Si sientes dolor o la garganta rasposa, no cantes más fuerte: descansa, toma agua y avisa a una persona adulta. Cantar fuerte no es cantar mejor; gritar cansa la voz.",
        "La práctica también se planea. Conviene trabajar en bloques cortos con pausas, por ejemplo 10 minutos de práctica y 2 de descanso. En un grupo, cada persona cumple un rol: cantar, tocar, marcar el pulso o dirigir. El interés por hacer música crece cuando cada una y cada uno puede aportar de una forma con la que se siente cómodo. Nadie está obligado a exponerse solo ante el curso.",
    ],
    [("postura", "forma de colocar el cuerpo para cantar o tocar con comodidad"), ("respiración", "aire que se toma y se suelta para sostener la voz"), ("calentamiento", "ejercicios previos que preparan la voz y las manos"), ("vocalizar", "cantar una vocal suave, como «a», para ejercitar la voz"), ("rol", "tarea que cumple cada persona en el grupo")],
    [
        ("Medir la respiración", "Haces un ciclo de respiración de 4 tiempos para inhalar y 8 para exhalar, 5 veces seguidas. ¿Cuántos tiempos de exhalación hiciste?", ["Cada ciclo exhala 8 tiempos.", "5 ciclos: 5 × 8 = 40."], "40 tiempos"),
        ("Ordenar el calentamiento", "¿Qué paso del calentamiento viene justo antes de vocalizar con una «a» suave?", ["Orden: respirar, soltar hombros y cuello, tararear, vocalizar.", "Antes de vocalizar viene tararear suave."], "Tararear suave"),
    ],
    [
        ("Gritar para que la voz suene más fuerte y más segura.", "Gritar cansa y puede dañar la voz; la fuerza viene de la respiración, no del grito.", "Usa más aire y buena postura, y mantén un volumen cómodo."),
        ("Seguir cantando aunque duela la garganta.", "El dolor es una señal para parar; seguir puede lastimar la voz.", "Descansa, toma agua y avisa a una persona adulta."),
    ],
    [
        ex("Para cantar, ¿conviene tener la espalda erguida y los hombros relajados o el cuerpo encogido?", "Espalda erguida y hombros relajados", "Esa postura deja pasar bien el aire."),
        ex("Si te duele la garganta al cantar, ¿qué haces: cantar más fuerte o descansar y avisar a una persona adulta?", "Descansar y avisar a una persona adulta", "El dolor es una señal de parar."),
        ex("¿Qué va primero: el calentamiento o la pieza completa?", "El calentamiento", "Se prepara la voz antes de exigirla."),
    ],
    [
        arith("En el ejercicio de respiración inhalas 4 tiempos y exhalas 8. ¿Cuántos tiempos dura un ciclo completo?", "4+8", "Se suman los tiempos de inhalar y de exhalar.", " tiempos"),
        ex("Según el orden de la clase, ¿cuál es el último paso del calentamiento?", "Vocalizar con una «a» suave", "El orden es respirar, soltar hombros y cuello, tararear y vocalizar."),
        ex("¿Para qué sirve exhalar largo y despacio al cantar: para tener aire hasta el final de la frase o para cantar más rápido?", "Para tener aire hasta el final de la frase", "Una exhalación lenta sostiene la frase."),
    ],
    [
        arith("Un calentamiento tiene 4 pasos de 3 minutos cada uno. ¿Cuántos minutos dura?", "4*3", "Se multiplican los pasos por su duración.", " minutos"),
        ex("¿Qué plan es más seguro: A) cantar 30 minutos seguidos sin pausas o B) cantar 10 minutos y descansar 2 con un poco de agua?", "B", "Los bloques cortos con pausas cuidan la voz."),
        arith("Un ensayo tiene 4 bloques de 10 minutos de práctica y después de cada uno un descanso de 2 minutos. ¿Cuántos minutos de descanso hay en total?", "4*2", "Hay un descanso por cada bloque.", " minutos"),
    ],
    [
        ex("Pedro dice que cantar más fuerte siempre es cantar mejor. ¿Tiene razón? Responde sí o no.", "No", "La fuerza viene del aire y de la técnica; gritar no mejora el canto."),
        ex("En un grupo, una compañera prefiere no cantar sola frente al curso. ¿Qué es más adecuado: obligarla o proponerle otro rol, como marcar el pulso?", "Proponerle otro rol", "Todos pueden aportar sin exponerse si no quieren."),
    ],
    [
        arith("Tienes 20 minutos para ensayar: 6 de calentamiento y 10 de práctica de la pieza. ¿Cuántos minutos quedan para descansar y tomar agua?", "20-6-10", "Se restan las dos partes al total.", " minutos"),
        arith("Necesitas practicar 60 minutos en total y planeas 3 días de 15 minutos. ¿Cuántos minutos te faltan?", "60-3*15", "3 días de 15 minutos suman 45.", " minutos"),
    ],
    [arith("Un coro escolar hace 2 ciclos de respiración de 4 + 8 tiempos antes de cada una de 3 canciones. ¿Cuántos tiempos respiran en total?", "2*3*(4+8)", "Hay 6 ciclos de 12 tiempos.", " tiempos")],
    [ex("¿Qué se hace con la voz si ya está cansada?", "Se descansa", "La voz cansada necesita pausa."), ex("¿Cuántos pasos tiene el calentamiento de la clase?", "4", "Respirar, soltar hombros y cuello, tararear y vocalizar."), ex("¿Qué rol puede cumplir alguien que no quiere cantar solo?", "Marcar el pulso, dirigir o acompañar", "Hay roles de apoyo igual de valiosos.")],
    (
        "Haz este calentamiento de cuatro pasos a volumen cómodo y anota cuánto duró cada uno: 1) 3 ciclos de respiración 4-8; 2) soltar hombros y cuello 6 veces; 3) tararear suave una nota larga 3 veces; 4) vocalizar «a» suave subiendo y bajando 3 veces. Después escribe en tres frases cómo sentiste la voz y el cuerpo y qué plan de práctica de 12 minutos harías mañana con pausas.",
        "Paso 1: 36 tiempos de respiración (3 ciclos de 12), unos 36 segundos si cada tiempo dura un segundo. Mi voz quedó más tranquila y los hombros más sueltos. Plan de 12 minutos: 4 de calentamiento, 6 de práctica de la pieza y 2 de descanso con agua.",
        ["completa los cuatro pasos en orden", "mantiene volumen cómodo", "planea una práctica con pausas"],
        ["registro del calentamiento", "plan de 12 minutos"],
        ["gritar o forzar la voz", "practicar sin descansos"],
        "Reconoce el registro y pide explicar para qué sirve cada paso y por qué el plan incluye pausas.",
    ),
    "Practica 3 ciclos de respiración 4-8 con una mano en el abdomen y cuéntalos.",
    "Inventa un calentamiento de 5 pasos para tocar un instrumento y explica el orden.",
)

# ---------------------------------------------------------------- OA 03 · clase 2 (precisión rítmica)
L(
    OA3, 2,
    "Lápiz y papel. Duraciones de la clase: semicorchea = 1 unidad; corchea = 2; negra = 4 (un pulso); blanca = 8; redonda = 16. Todos los patrones están escritos en los ejercicios; se palmean a volumen bajo.",
    "Aprenderé a tocar o cantar un patrón rítmico con precisión: que cada sonido empiece y dure lo que está escrito. Sirve para que la interpretación suene ordenada, sola o con el grupo.",
    ["Sé medir figuras en unidades de semicorchea.", "Sé que un compás de 4/4 tiene 16 unidades.", "Sé que el tempo se mide en pulsos por minuto."],
    [
        "La precisión rítmica es tocar o cantar cada sonido en el momento y con la duración que indica la partitura, sobre un pulso parejo. No depende de la velocidad ni del volumen: se puede ser muy preciso lento y suave. El primer paso es mantener un pulso estable, marcándolo con el pie o con la mano en silencio. Si el pulso se apura o se frena, todo el patrón se desordena.",
        "Para estudiar un patrón se usa una estrategia por pasos. Primero se lee y se cuentan las unidades de cada compás. Después se palmea lento, por ejemplo a 60 pulsos por minuto, donde cada pulso dura 1 segundo. Cuando sale limpio dos veces seguidas, se sube el tempo de a poco. Si hay un error, no se repite toda la pieza: se aísla el compás con error y se practica lento hasta que salga bien.",
        "Para detectar un error se compara lo escrito con lo tocado, figura por figura. Puede haber una figura partida en dos, dos figuras unidas en una, un silencio que se llenó con sonido o una entrada atrasada. Anotar el error con precisión (en qué figura y por cuántas unidades) permite corregirlo. Tocar en grupo exige además escuchar a las demás voces para mantener todos el mismo pulso.",
    ],
    [("precisión rítmica", "tocar cada sonido a tiempo y con la duración escrita"), ("pulso estable", "latido que no se apura ni se frena"), ("aislar", "separar un compás con error para practicarlo solo"), ("entrada", "momento en que empieza a sonar una voz o un instrumento"), ("palmear", "marcar un ritmo con las palmas")],
    [
        ("Comparar lo escrito con lo tocado", "Escrito: negra, negra, blanca (4, 4, 8 unidades). Tocado: negra, negra, negra, negra (4, 4, 4, 4). ¿Qué error hubo?", ["Las dos primeras figuras coinciden.", "La blanca de 8 unidades se tocó como dos negras."], "La blanca se partió en dos negras"),
        ("Calcular una duración", "Una pieza tiene 12 compases de 4/4 y va a 60 pulsos por minuto. ¿Cuántos segundos dura?", ["12 compases × 4 pulsos = 48 pulsos.", "A 60 por minuto cada pulso dura 1 segundo."], "48 segundos"),
    ],
    [
        ("Creer que tocar más rápido es tocar más preciso.", "La precisión es tocar a tiempo y con la duración escrita, no con velocidad.", "Empieza lento y sube el tempo cuando salga limpio."),
        ("Repetir toda la pieza cuando falla un compás.", "Así se repite el error y se pierde tiempo.", "Aísla el compás con error y practícalo lento."),
    ],
    [
        ex("Para tener precisión rítmica, ¿debe ser parejo el pulso o el volumen?", "El pulso", "Si el pulso se apura o se frena, el patrón se desordena."),
        ex("Si te equivocas en un compás, ¿repites toda la pieza o aíslas ese compás y lo practicas lento?", "Aíslo ese compás y lo practico lento", "Así se corrige el error sin gastar tiempo."),
        ex("A 60 pulsos por minuto, ¿cuánto dura un pulso en segundos?", "1 segundo", "60 pulsos en 60 segundos: uno por segundo."),
    ],
    [
        ex("Escrito: negra, corchea, corchea, negra (4, 2, 2, 4). Tocado: negra, negra, negra. ¿Qué error hubo?", "Las dos corcheas se tocaron como una negra", "El total es 12 unidades en ambos, pero cambió el ritmo."),
        ex("¿Coincide el ritmo tocado con el escrito en este caso? Escrito: negra, negra, blanca (4, 4, 8). Tocado: negra, blanca, negra (4, 8, 4). Responde sí o no.", "No", "Las dos versiones suman 16 unidades, pero la blanca quedó en otro lugar y el ritmo cambió."),
        arith("A 60 pulsos por minuto, ¿cuántos segundos dura un compás de 4/4?", "4*60//60", "Hay 4 pulsos y cada uno dura un segundo.", " segundos"),
    ],
    [
        arith("Practicas a 60 pulsos por minuto y subes 10 cada vez que sale limpio dos veces. ¿Cuántas veces subes hasta llegar a 100?", "(100-60)//10", "Subes de 10 en 10 desde 60 hasta 100.", " veces"),
        arith("Una pieza de 12 compases de 4/4 va a 80 pulsos por minuto. ¿Cuántos segundos dura?", "12*4*60//80", "Hay 48 pulsos, que a 80 por minuto duran 36 segundos.", " segundos"),
        ex("Un compás de 3/4 tiene: negra, silencio de negra, negra. ¿En qué pulsos suena y en cuál hay silencio?", "Suena en 1 y 3; hay silencio en 2", "El silencio ocupa el segundo pulso."),
    ],
    [
        ex("Ana toca a toda velocidad y dice que así es más precisa. ¿Tiene razón? Responde sí o no.", "No", "La precisión es tocar a tiempo y con la duración escrita, no tocar rápido."),
        ex("Debía tocarse en 4/4: corchea con puntillo, semicorchea, negra y blanca (3, 1, 4, 8 unidades). Un estudiante tocó la corchea con puntillo como corchea simple (2 unidades). ¿Cuántas unidades le faltaron al compás?", "1", "Debía sumar 3 + 1 + 4 + 8 = 16 y sumó 15."),
    ],
    [
        arith("Dos estudiantes tocan 8 compases de 4/4. Uno va a 120 pulsos por minuto y la otra a 60. ¿Cuántos segundos más tarda la que va a 60?", "32*60//60-32*60//120", "Son 32 pulsos: 32 segundos a 60 y 16 segundos a 120.", " segundos"),
        ex("Las entradas escritas caen en las unidades 0, 4, 8 y 12. Un estudiante entró en 0, 4, 9 y 12. ¿En qué entrada se equivocó y cuántas unidades tarde?", "En la tercera, 1 unidad tarde", "La tercera debía ser en la unidad 8 y entró en la 9."),
    ],
    [arith("Un estudiante practica un compás de 4/4 a 60 pulsos por minuto y lo repite 15 veces seguidas. ¿Cuántos segundos practica?", "15*4*60//60", "Son 60 pulsos de un segundo cada uno.", " segundos")],
    [ex("¿Qué debe mantenerse para tocar con precisión?", "Un pulso estable", "Sin pulso parejo el ritmo se desordena."), ex("¿Qué se hace con un compás que sale mal?", "Se aísla y se practica lento", "Es la estrategia de la clase."), ex("¿A cuántos pulsos por minuto empieza la estrategia de la clase?", "60", "Se empieza lento, a 60 por minuto.")],
    (
        "Palmea este compás de 4/4 inventado: negra, corchea, corchea, blanca (4, 2, 2, 8 unidades). Hazlo 4 veces seguidas con un pulso de 60 por minuto, marcado con el pie en silencio. Anota en una tabla de 4 filas (intento 1 a 4) si salió «limpio» o qué error hubo, y escribe cuántas unidades suma el compás y cuántos segundos duraron tus 4 intentos.",
        "El compás suma 16 unidades. Los 4 intentos duraron 16 segundos (4 compases × 4 pulsos × 1 segundo). Intento 1: apuré las corcheas. Intento 2: limpio. Intento 3: limpio. Intento 4: limpio.",
        ["calcula 16 unidades y 16 segundos", "registra los errores con precisión", "usa un pulso estable"],
        ["tabla de intentos", "cálculos escritos"],
        ["tocar más rápido para terminar antes", "no registrar los errores"],
        "Reconoce la tabla y pide explicar qué error hubo en cada intento y cómo lo corrigió.",
    ),
    "Palmea cuatro veces un compás de 4 negras a 60 por minuto, sin apurarte.",
    "Escribe un compás de 3/4 con un silencio y práctícalo palmeando lento, anotando tus errores.",
)

# ---------------------------------------------------------------- OA 03 · clase 3 (precisión melódica y afinación)
L(
    OA3, 3,
    f"Lápiz y papel. Escala de números: {NOTAS}. Las melodías están escritas con números y se pueden cantar con «la» o tocar en un instrumento melódico, pero no es necesario. Canta a volumen cómodo.",
    "Aprenderé a cantar o tocar una melodía con precisión melódica: las notas correctas, en el orden correcto y afinadas. Sirve para que la interpretación se reconozca y suene bien, sola o en grupo.",
    ["Sé escribir una melodía con números del 1 al 8.", "Sé que un sonido puede ser grave o agudo.", "Sé comparar dos listas de números."],
    [
        f"La precisión melódica es cantar o tocar las notas escritas, en el orden escrito y con la altura correcta. Con la escala de números ({NOTAS}) una melodía se puede escribir como 1-3-5-3-1. La afinación es que el sonido coincida con la altura de la nota: si es más grave de lo que debe, se dice que está bajo; si es más agudo, que está alto. Cantar afinado se aprende escuchando.",
        "Para cantar una melodía con precisión se sigue una estrategia. Primero se escucha la nota de partida, por ejemplo una referencia en el teclado o dada por quien dirige. Luego se canta la melodía en frases cortas, despacio. Después se compara lo cantado con lo escrito, nota por nota. Si una nota sale distinta, se identifica en qué posición y si quedó más grave o más aguda, y se corrige escuchando la nota de referencia.",
        "También ayuda mirar la distancia entre las notas. Si pasamos de 1 a 5, la diferencia es 5 − 1 = 4 números; es un salto grande y conviene prepararlo. Si pasamos de 4 a 5, la diferencia es 1 y es un paso por grado. Calcular la distancia anticipa la dificultad. En un grupo, todos deben escuchar a los demás para ajustar la altura y cantar «como una sola voz» cuando la melodía es la misma.",
    ],
    [("precisión melódica", "cantar o tocar las notas escritas, en orden y con la altura correcta"), ("afinación", "que el sonido coincida con la altura de la nota"), ("nota de referencia", "sonido que se escucha antes de cantar para tener la altura"), ("grado y salto", "grado: a la nota vecina; salto: cambio de dos o más números"), ("distancia", "diferencia entre dos notas, que se calcula restando")],
    [
        ("Encontrar el error", "Escrito: 1-3-5-3-1. Cantado: 1-3-4-3-1. ¿En qué posición hay error y cómo quedó la nota?", ["Comparo posición por posición: 1=1, 3=3, 5≠4.", "La tercera nota debía ser 5 y se cantó 4, un número más bajo."], "En la posición 3, quedó más grave"),
        ("Medir la distancia", "En la melodía 2-4-7, ¿cuál es la distancia del segundo al tercer sonido?", ["Los sonidos son 4 y 7.", "7 − 4 = 3."], "3 números"),
    ],
    [
        ("Pensar que una melodía «parecida» ya es precisa.", "Una sola nota distinta cambia la melodía y se nota.", "Compara nota por nota con la partitura."),
        ("Cantar sin escuchar la nota de referencia.", "Sin referencia es fácil partir en una altura equivocada.", "Escucha o toma la referencia antes de empezar."),
    ],
    [
        ex("Antes de cantar, ¿conviene escuchar la nota de partida o cantar de inmediato?", "Escuchar la nota de partida", "Así empiezas en la altura correcta."),
        ex("Si cantas más bajo que la nota de referencia, ¿tu sonido está más grave o más agudo?", "Más grave", "Más bajo es más grave."),
        ex("¿Cuántas notas tiene la melodía 1-3-5-3-1?", "5", "Los números son 1, 3, 5, 3 y 1."),
    ],
    [
        ex("Escrito: 1-3-5-3-1. Cantado: 1-3-4-3-1. ¿La nota equivocada quedó más grave o más aguda que la escrita?", "Más grave", "Se cantó 4 en vez de 5, que es más bajo."),
        ex("Escrito: 2-4-6-4-2. Cantado: 2-4-5-4-2. ¿Cuántas notas coinciden?", "4", "Solo la tercera nota es distinta."),
        ex("¿Cuál es la nota que escribe «fa» en la escala de la clase?", "4", "En la escala 4 = fa."),
    ],
    [
        ex("Escrito: 3-4-5-6-5-4-3. Cantado: 3-4-5-5-5-4-3. ¿En cuántas posiciones coincide lo cantado con lo escrito?", "6", "Solo la cuarta posición es distinta, de las 7."),
        arith("En la melodía 1-5 hay un salto del 1 al 5. ¿Cuántos números hay de diferencia?", "5-1", "Se resta la nota menor a la mayor.", " números"),
        ex("En la melodía 1-3-5-8, ¿cuántos saltos tienen exactamente 2 números de diferencia?", "2", "De 1 a 3 y de 3 a 5 hay 2; de 5 a 8 hay 3."),
    ],
    [
        ex("Laura dice que, si la melodía suena parecida, ya está bien. ¿Tiene razón? Responde sí o no.", "No", "Una nota distinta cambia la melodía, por eso se compara nota por nota."),
        ex("Ana canta 1-3-5-3-1 y Beto canta 1-3-5-5-1, siendo 1-3-5-3-1 la melodía escrita. ¿Quién se equivocó y en qué posición?", "Beto, en la posición 4", "En la posición 4 debía ir 3 y Beto cantó 5."),
    ],
    [
        ex("Escrito: 5-5-6-5-8-7. Cantado: 5-5-6-5-7-7. ¿Cuántos errores hubo y de cuántos números fue el error?", "1 error, de 1 número más grave", "Solo la quinta posición cambió: se cantó 7 en vez de 8."),
        arith("Una melodía tiene 16 notas de un pulso y se canta a 60 pulsos por minuto. ¿Cuántos segundos dura?", "16*60//60", "Cada pulso dura un segundo.", " segundos"),
    ],
    [ex("Un coro canta la escala descendente 8-7-6-5-4-3-2-1. Un estudiante canta 8-7-6-4-3-2-1. ¿Cuántas notas le faltaron?", "1", "Se saltó la nota 5; debía cantar 8 notas y cantó 7.")],
    [ex("¿Qué es la afinación?", "Que el sonido coincida con la altura de la nota", "Es la definición de la clase."), ex("¿Cómo se calcula la distancia entre dos notas?", "Restando", "Se resta la menor a la mayor."), ex("¿Qué se hace con una nota que sale distinta?", "Se identifica y se corrige escuchando la referencia", "Esa es la estrategia de la clase.")],
    (
        "Mira esta melodía inventada: 2-3-4-6-4-3-2. Cántala despacio con «la» (o tócala) tres veces y completa una tabla de 3 intentos: en cada uno escribe «correcto» o qué número cambió, en qué posición y si quedó más grave o más agudo. Escribe también la distancia entre su nota más grave y su nota más aguda.",
        "La distancia entre 2 y 6 es 4 números. Intento 1: la nota 6 quedó más grave (5), en la posición 4. Intento 2: correcto. Intento 3: correcto.",
        ["registra posición y tipo de error", "calcula la distancia 4", "mejora entre intentos"],
        ["tabla de intentos", "cálculo de la distancia"],
        ["no comparar nota por nota", "cantar sin la nota de referencia"],
        "Reconoce el registro y pide cantar solo la nota que falló, escuchando su referencia, antes de volver a la melodía completa.",
    ),
    "Canta despacio la escala 1-2-3-4-5-6-7-8 y baja hasta el 1.",
    "Escribe una melodía de 6 notas con un salto y pide a alguien que la cante; registra sus errores.",
)

# ---------------------------------------------------------------- OA 03 · clase 4 (expresividad, fraseo y dinámica)
TEXTO = "La luna sube despacio / sobre el cerro del lugar, / los grillos cantan bajito / y el río sigue al pasar."

L(
    OA3, 4,
    f"Lápiz y papel. Texto original de la clase (inventado): «{TEXTO}». Dinámicas: pp = muy suave; p = suave; mp = medio suave; mf = medio fuerte; f = fuerte. Canta o recita a volumen cómodo.",
    "Aprenderé a dar expresividad a una interpretación con fraseo, dinámica y tempo, y a trabajar con el grupo. Sirve para que lo que cantamos o tocamos comunique una idea y no solo suene a tiempo.",
    ["Sé que la dinámica es qué tan fuerte o suave suena la música.", "Sé que el tempo es la velocidad del pulso.", "Sé trabajar en grupo escuchando a los demás."],
    [
        "La expresividad es usar los recursos de la música para comunicar una idea. El fraseo agrupa los sonidos en frases, como las oraciones de un texto, y se respira entre frases, no en medio de ellas. Una frase suele tener un punto de mayor intensidad y luego se relaja. Se puede tocar ligado, con notas unidas (legato), o picado, con notas cortas y separadas (staccato), y cada forma da un carácter distinto.",
        "La dinámica se planea para toda la pieza: puede empezar en p, crecer poco a poco con un crescendo hasta f y volver a p con un diminuendo. El tempo también comunica: una canción de cuna va lenta y suave, y una marcha va firme y más fuerte. Las decisiones de expresividad se anotan en la partitura o en un plan escrito, para que todos las sigan y puedan repetirlas.",
        "En un grupo, la expresividad es de todos. Quien lleva la melodía se oye más y quien acompaña toca más suave, para que la melodía se distinga. Se escucha al resto, se mira a quien dirige y se ajusta el volumen para formar una sola interpretación. Hacer música en grupo también es disfrutar: cada persona aporta con su voz o su instrumento y todas cuidan el resultado común.",
    ],
    [("fraseo", "agrupar los sonidos en frases, con respiro al final de cada una"), ("legato y staccato", "notas unidas y suaves; o cortas y separadas"), ("crescendo y diminuendo", "subir o bajar el volumen poco a poco"), ("expresividad", "usar dinámica, tempo y fraseo para comunicar una idea"), ("plan de interpretación", "lista escrita de decisiones de expresividad")],
    [
        ("Planear las frases", f"El texto «{TEXTO}» tiene 4 versos, y cada verso es una frase. ¿Cuántos respiros se hacen si se respira solo al final de cada frase, menos al final de la última?", ["Hay 4 frases.", "Se respira al final de las tres primeras; después de la última se termina."], "3 respiros"),
        ("Elegir la dinámica", "Quieres cantar una canción de cuna lenta. ¿Qué dinámica conviene: p o f?", ["Una canción de cuna busca calma.", "La dinámica suave (p) calza con la calma."], "p"),
    ],
    [
        ("Pensar que expresivo es lo mismo que fuerte.", "Se expresa también con suavidad, tempo, fraseo y silencio.", "Elige la dinámica que calce con la idea."),
        ("Respirar en medio de una frase.", "Se corta la idea y la frase pierde sentido.", "Planea los respiros al final de las frases."),
    ],
    [
        ex("¿Dónde se respira en el fraseo: en medio de la frase o al final?", "Al final", "Así no se corta la idea."),
        ex("Notas cortas y separadas se llaman staccato. Notas unidas y suaves, ¿legato o staccato?", "Legato", "Es la forma ligada de tocar."),
        ex("Ordena de más suave a más fuerte: pp, mf, p.", "pp, p, mf", "El orden de la lista es pp, p, mp, mf, f."),
    ],
    [
        ex("Una marcha de desfile, ¿pide un tempo firme y parejo o uno que se frena y se apaga?", "Un tempo firme y parejo", "La marcha acompaña el paso y necesita un pulso constante."),
        arith("Una pieza tiene 8 compases y se divide en frases de 4 compases. ¿Cuántas frases tiene?", "8//4", "Se reparten los compases en frases iguales.", " frases"),
        ex("En un grupo, ¿quien acompaña toca más fuerte o más suave que quien lleva la melodía?", "Más suave", "Así la melodía se distingue."),
    ],
    [
        ex("El plan dinámico es: frase 1 en p, frase 2 en mp, frase 3 en mf, frase 4 en f. ¿Cuántas veces sube la dinámica entre frases?", "3", "Sube de la 1 a la 2, de la 2 a la 3 y de la 3 a la 4."),
        ex("Una pieza de 16 compases tiene 4 frases iguales y el crescendo empieza en la tercera frase. ¿En qué compás empieza?", "En el compás 9", "Cada frase tiene 4 compases; la tercera empieza después de 8."),
        ex("Cuatro notas cortas y separadas, ¿suenan ligadas o picadas?", "Picadas", "Notas cortas y separadas son staccato."),
    ],
    [
        ex("Tomás dice que expresividad es cantar fuerte. ¿Tiene razón? Responde sí o no.", "No", "La expresividad usa dinámica, tempo y fraseo según la idea."),
        ex("Un grupo tiene 6 personas: 2 cantan la melodía y 4 acompañan. Para que se oiga la melodía, ¿quiénes bajan el volumen?", "Quienes acompañan", "El acompañamiento debe quedar por debajo de la melodía."),
    ],
    [
        ex("El plan es: frase 1 en p; frase 2 con crescendo hasta f; frase 3 en f; frase 4 con diminuendo hasta p. ¿En qué frases cambia la dinámica poco a poco?", "En la 2 y en la 4", "Allí hay crescendo y diminuendo."),
        arith("Un grupo ensaya cada una de las 4 frases por separado 3 veces y después la pieza completa 2 veces. ¿Cuántas pasadas hace en total?", "4*3+2", "12 pasadas por frases más 2 de la pieza completa.", " pasadas"),
    ],
    [ex("Una banda escolar ensaya una marcha y un coro ensaya una canción de cuna. ¿Cuál de las dos pedirá un tempo más lento y suave?", "La canción de cuna", "La calma de la cuna pide lento y suave; la marcha es firme.")],
    [ex("¿Qué es un crescendo?", "Subir el volumen poco a poco", "Es lo contrario del diminuendo."), ex("¿Con qué letra se escribe la dinámica suave?", "p", "En la lista p = suave."), ex("¿Quién se oye más en un grupo: la melodía o el acompañamiento?", "La melodía", "El acompañamiento queda por debajo.")],
    (
        f"Usa el texto «{TEXTO}». Hazle un plan de interpretación: dónde respiras (marca con /), qué dinámica tiene cada verso (usa pp, p, mp, mf o f), si hay crescendo o diminuendo y qué tempo eliges (lento, moderado o rápido). Después recítalo o cántalo con una melodía inventada por ti, a volumen cómodo, siguiendo tu plan. Explica en una frase qué idea quisiste comunicar.",
        "Respiros: al final de cada verso. Verso 1: p; verso 2: mp con crescendo; verso 3: mf; verso 4: diminuendo hasta pp. Tempo lento. Idea: una noche tranquila que se va apagando.",
        ["marca respiros al final de las frases", "asigna una dinámica a cada verso", "explica la idea que comunica"],
        ["plan escrito", "interpretación"],
        ["respirar a mitad de verso", "elegir f para todo"],
        "Reconoce el plan y pide cantar un verso con dos dinámicas distintas para comparar cuál calza mejor con la idea.",
    ),
    "Recita dos veces el texto de la clase, una en p y otra en f, y di cuál calza mejor.",
    "Escribe un plan de interpretación de 6 compases para un instrumento con una frase ligada y otra picada.",
)
