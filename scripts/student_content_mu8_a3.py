"""Student material for 8.º básico Música, OA 03 (cantar y tocar repertorio relacionado con la música escuchada: comprensión rítmica y melódica, conciencia de textura y estilo, expresividad, rigurosidad, fluidez de fraseo y dinámica).

Todas las melodías y patrones de los ejercicios son esquemas inventados para esta clase; el repertorio real lo selecciona el docente.
"""
from __future__ import annotations

from student_content_mu8_a import L
from student_lessons import arith, ex

OA3 = "MU08 OA 03"

NOTAS = "1 = do, 2 = re, 3 = mi, 4 = fa, 5 = sol, 6 = la, 7 = si, 8 = do agudo"
DINAMICA = "pp (muy suave) < p (suave) < mp (algo suave) < mf (algo fuerte) < f (fuerte) < ff (muy fuerte)"

# ---------------------------------------------------------------- OA 03 · clase 1 (comprensión rítmica y rigurosidad)
L(
    OA3, 1,
    "Lápiz y papel. Los patrones rítmicos están escritos con palabras en los ejercicios. Para practicar, basta marcar el pulso con el pie y palmear el ritmo a volumen bajo o golpear suavemente una mesa con la mano.",
    "Aprenderé a comprender y ejecutar un ritmo con rigurosidad: mantener un pulso parejo, contar los silencios y calcular cuánto dura un patrón según su tempo. Sirve para interpretar repertorio con precisión y sin acelerar.",
    ["Sé que el pulso es el latido parejo de la música.", "Sé que un compás de 4/4 tiene 4 pulsos.", "Sé multiplicar y dividir números pequeños."],
    [
        "Comprender un ritmo es entender cómo se reparten las duraciones sobre el pulso antes de tocarlo. El tempo se mide en pulsos por minuto. A 60 pulsos por minuto hay un pulso por segundo. A 120 hay dos por segundo. Para calcular cuánto dura un patrón se multiplican los pulsos por 60 y se divide por el tempo. Por ejemplo, 8 pulsos a 60 por minuto duran 8 × 60 ÷ 60 = 8 segundos.",
        "La rigurosidad consiste en cuidar cada detalle de la ejecución. El pulso debe mantenerse parejo: no se acelera cuando hay muchas notas ni se frena cuando hay pocas. Cada figura debe durar lo que dice la partitura. Los silencios se cuentan en voz baja o en la mente, porque también ocupan tiempo. Para dividir los pulsos en dos, se cuenta «1 y 2 y 3 y 4 y»: cada número es un pulso y cada «y» es la mitad.",
        "Un buen método de práctica es contar primero el patrón sin sonidos, luego palmearlo despacio y por último subir el tempo poco a poco. Si algo falla, se vuelve más lento. Fluidez no significa tocar rápido, sino tocar sin detenerse ni tropezar. Una ejecución rigurosa se reconoce porque el mismo patrón suena igual cada vez que se repite.",
    ],
    [("tempo", "velocidad del pulso, en pulsos por minuto"), ("rigurosidad", "cuidar cada detalle: pulso parejo y cada figura con su duración"), ("subdivisión", "dividir cada pulso en partes iguales, por ejemplo en dos corcheas"), ("fluidez", "tocar sin detenerse ni tropezar"), ("pulsos por minuto", "cantidad de pulsos que caben en un minuto")],
    [
        ("Calcular una duración", "Un patrón de 8 pulsos se toca a 120 pulsos por minuto. ¿Cuántos segundos dura?", ["A 120 por minuto hay 2 pulsos por segundo.", "8 pulsos ÷ 2 = 4 segundos."], "4 segundos"),
        ("Contar un silencio", "En 4/4 el patrón es: negra, silencio de negra, negra, negra. ¿Cuántos pulsos suenan y cuántos se cuentan sin sonar?", ["Hay 3 negras que suenan.", "El silencio ocupa 1 pulso, que se cuenta igual."], "Suenan 3 pulsos y 1 se cuenta en silencio"),
    ],
    [
        ("Acelerar donde hay muchas notas.", "El pulso debe mantenerse parejo aunque cambie la cantidad de notas.", "Marca el pulso con el pie y no lo sueltes."),
        ("No contar los silencios.", "Los silencios duran lo que dice la partitura y su tiempo cuenta.", "Cuenta el silencio en voz baja."),
    ],
    [
        ex("¿Cuántas corcheas caben en una negra?", "2", "Cada pulso se divide en dos corcheas."),
        ex("En el patrón negra, silencio de negra, negra, negra (4/4), ¿se cuenta el pulso del silencio? Responde sí o no.", "Sí", "El silencio ocupa tiempo aunque no suene."),
        ex("¿Se toca más rápido a 80 pulsos por minuto o a 60 pulsos por minuto?", "A 80 pulsos por minuto", "Más pulsos por minuto significa mayor velocidad."),
    ],
    [
        arith("¿Cuántas corcheas hay en un compás de 3/4, si cada pulso se divide en 2?", "3*2", "Son tres pulsos con dos corcheas cada uno.", " corcheas"),
        ex("¿Qué es la rigurosidad al tocar un ritmo? A) Mantener un pulso parejo y dar a cada figura su duración. B) Tocar lo más rápido que se pueda.", "A", "La precisión se logra cuidando el pulso y las duraciones, no la velocidad."),
        ex("En 4/4, el patrón es negra, corchea, corchea, negra, silencio de negra. ¿Cuántos sonidos suenan?", "4", "Suenan una negra, dos corcheas y una negra; el silencio no suena."),
    ],
    [
        arith("Un patrón de 6 compases de 4/4 se toca a 80 pulsos por minuto. ¿Cuántos segundos dura?", "6*4*60//80", "Se calculan los 24 pulsos y se convierten a segundos con el tempo.", " segundos"),
        arith("A 60 pulsos por minuto, debían sonar 10 pulsos en 10 segundos, pero una estudiante tocó 12 pulsos en ese tiempo. ¿Cuántos pulsos de más tocó?", "12-10", "Se resta lo que debía tocar de lo que tocó.", " pulsos de más"),
        ex("Una estudiante toca 8 pulsos en 6 segundos y otra toca 8 pulsos en 8 segundos. ¿Quién mantiene los 60 pulsos por minuto?", "La que tocó en 8 segundos", "A 60 por minuto, 8 pulsos duran 8 segundos."),
    ],
    [
        ex("Un compañero dice: «Cuando hay muchas notas, hay que acelerar». ¿Es correcto? Responde sí o no.", "No", "El pulso debe mantenerse parejo aunque haya muchas notas."),
        ex("Una persona toca un patrón difícil cada vez más rápido, y no logra tocarlo bien. ¿Qué conviene hacer: bajar el tempo o subirlo más?", "Bajar el tempo", "La práctica rigurosa vuelve más lento hasta que sale sin errores."),
    ],
    [
        arith("Un patrón de 2 compases de 6/8 tiene 12 corcheas. Se toca a 120 corcheas por minuto. ¿Cuántos segundos dura?", "12*60//120", "Se pasa de corcheas a segundos con el tempo.", " segundos"),
        arith("Un patrón de 2 compases de 4/4 se repite 3 veces a 120 pulsos por minuto. ¿Cuántos segundos dura todo?", "3*2*4*60//120", "Son 24 pulsos y a 120 por minuto cada pulso dura medio segundo.", " segundos"),
    ],
    [arith("Un grupo de percusión de tu curso practica un patrón de 4 compases de 4/4 a 60 pulsos por minuto y lo repite 5 veces seguidas. ¿Cuántos segundos practica?", "4*4*5*60//60", "Son 80 pulsos y a 60 por minuto cada uno dura un segundo.", " segundos")],
    [ex("¿Cuántos pulsos por segundo hay a 120 pulsos por minuto?", "2", "120 ÷ 60 da 2."), ex("¿Qué hay que hacer con los silencios al tocar?", "Contarlos", "Ocupan tiempo aunque no suenen."), ex("¿Qué se hace primero al practicar un patrón difícil: contarlo sin sonar o tocarlo rápido?", "Contarlo sin sonar", "Primero se comprende el ritmo y luego se sube el tempo.")],
    (
        "Practica este patrón de ejemplo en 4/4, a 60 pulsos por minuto: «negra, corchea, corchea, silencio de negra, negra». 1) Cuéntalo con «1 y 2 y 3 y 4 y» y marca cada pulso con el pie. 2) Escríbelo con palabras y calcula cuántos segundos dura un compás. 3) Repítelo 4 veces seguidas y calcula la duración total. 4) Anota si mantuviste el pulso parejo o aceleraste.",
        "Un compás dura 4 segundos (4 pulsos a 60 por minuto). Cuatro repeticiones duran 16 segundos. Anotó: «Aceleré en la segunda vuelta; bajé el tempo y salió parejo».",
        ["cuenta el silencio", "calcula bien la duración", "reconoce y corrige una aceleración"],
        ["cuenta con «y» anotada", "duración de un compás y del total"],
        ["acelerar en los grupos de corcheas", "no contar el silencio"],
        "Reconoce el cálculo y pide palmear de nuevo el patrón mientras otra persona marca el pulso con el pie.",
    ),
    "Palmea cuatro veces seguidas el patrón negra, negra, negra, silencio de negra, a un pulso parejo.",
    "Escribe un patrón propio de 4/4 que tenga un silencio y corcheas, y calcula cuánto dura a 60 pulsos por minuto.",
)

# ---------------------------------------------------------------- OA 03 · clase 2 (comprensión melódica y afinación)
L(
    OA3, 2,
    f"Lápiz y papel. Escala de números: {NOTAS}. Las melodías están escritas en los ejercicios. Puedes cantarlas con «la», tocarlas o tararearlas a volumen cómodo.",
    "Aprenderé a leer una melodía (contorno, grados conjuntos y saltos), a afinarla con una nota de referencia y a practicarla por células. Sirve para interpretar una melodía con precisión y sin tropiezos.",
    ["Sé leer una melodía escrita con números.", "Sé que un intervalo se cuenta en grados con ambas notas.", "Sé que una melodía puede subir, bajar o repetirse."],
    [
        "Comprender una melodía es leerla antes de cantarla. Primero se mira su contorno: si sube, baja o se mantiene. Después se miran los movimientos entre notas. Si dos notas son vecinas, como 3 y 4, el movimiento es por grado conjunto. Si la distancia es de tres grados o más, como de 3 a 5 (que son 3 grados contando ambas), se llama salto. Los saltos suelen ser más difíciles de afinar.",
        "Afinar es cantar o tocar la altura exacta de la nota. Para lograrlo, se parte desde una nota de referencia: se canta la primera nota, se comprueba que está bien y se canta la segunda escuchando la distancia. Si una nota queda un poco baja, se dice que está desafinada hacia lo grave, y hay que subirla un poco. Escuchar con atención mientras se canta es más útil que subir el volumen.",
        "Para estudiar una melodía con rigurosidad se divide en células, que son grupos pequeños de notas o de compases. Se practica cada célula despacio hasta que sale bien y después se unen de dos en dos. Así se reducen los errores y se logra una ejecución fluida. Una melodía de 8 compases, practicada en células de 2 compases, tiene 4 células.",
    ],
    [("contorno", "forma que dibuja la melodía: sube, baja o se mantiene"), ("grado conjunto", "movimiento entre notas vecinas"), ("salto", "movimiento de tres grados o más entre dos notas"), ("afinar", "cantar o tocar la altura exacta de la nota"), ("célula", "grupo pequeño de notas o compases que se practica por separado")],
    [
        ("Contar los saltos", f"En la melodía 1-2-3-5-3-2-1, ¿cuántos saltos (tres grados o más) hay? Escala: {NOTAS}.", ["Los movimientos son 1-2, 2-3, 3-5, 5-3, 3-2 y 2-1.", "Solo 3-5 y 5-3 son de tres grados."], "2 saltos"),
        ("Dividir en células", "Una melodía de 12 compases se practica en células de 4 compases. ¿Cuántas células son?", ["Se divide el total de compases por el largo de la célula.", "12 ÷ 4 = 3."], "3 células"),
    ],
    [
        ("Cantar más fuerte para afinar.", "Afinar depende de escuchar la altura, no del volumen.", "Canta suave y compara con la nota de referencia."),
        ("Practicar toda la melodía de corrido cuando falla un trozo.", "Si un trozo falla, se aísla en una célula y se practica despacio.", "Repite solo la célula difícil y luego únela con las otras."),
    ],
    [
        ex("El movimiento de 3 a 4, ¿es un grado conjunto o un salto?", "Grado conjunto", "Son notas vecinas."),
        ex("El movimiento de 1 a 5, ¿es un grado conjunto o un salto?", "Salto", "Hay 5 grados contando ambas notas."),
        ex("La melodía 1-3-5, ¿sube o baja?", "Sube", "Cada nota es más aguda que la anterior."),
    ],
    [
        arith("¿Cuántos grados hay de la nota 2 a la nota 6, contando ambas?", "6-2+1", "Se cuentan las dos notas del intervalo.", " grados"),
        ex("La melodía 5-4-3-2-1, ¿se mueve por grados conjuntos o por saltos?", "Por grados conjuntos", "Cada movimiento es entre notas vecinas."),
        ex("¿Para qué se canta primero la nota de partida? A) Para tener una referencia de afinación. B) Para cantar más fuerte.", "A", "Con esa referencia se comprueba la altura de las notas siguientes."),
    ],
    [
        arith("Una frase de 8 compases se practica en células de 2 compases. ¿Cuántas células son?", "8//2", "Se divide el total de compases por el largo de la célula.", " células"),
        ex("En la melodía 1-3-5-3-1, ¿en qué nota está el punto más alto?", "En la nota 5", "Es la nota más aguda de la melodía."),
        ex("En la melodía 4-5-6-5-4, ¿cuántos movimientos por grado conjunto hay?", "4", "Los cuatro movimientos son entre notas vecinas."),
    ],
    [
        ex("Quieres afinar un salto de 1 a 5, pero cantas el 5 un poco bajo. ¿Qué haces? A) Vuelvo a la nota de referencia, escucho la distancia y subo el 5. B) Canto el 5 más fuerte.", "A", "Se corrige escuchando la altura, no subiendo el volumen."),
        ex("Una persona canta el 3 un poco más grave de lo que corresponde. ¿Está desafinada hacia lo grave o hacia lo agudo?", "Hacia lo grave", "Cantó más bajo que la altura correcta."),
    ],
    [
        arith("Una melodía de 16 notas se divide en células de 4 notas y cada célula se canta 3 veces. ¿Cuántas notas se cantan en total?", "16*3", "Cada nota se canta 3 veces al practicar todas las células.", " notas"),
        arith("La melodía 5-4-3-2-1 va de la nota 5 a la nota 1. ¿Cuántos pasos de grado conjunto baja en total?", "5-1", "Se resta la nota final de la inicial.", " pasos"),
    ],
    [arith("El coro de tu curso aprende una canción de 18 compases dividida en células de 3 compases. ¿Cuántas células ensaya?", "18//3", "Se divide el total de compases por el largo de cada célula.", " células")],
    [ex("¿Qué es un salto en una melodía?", "Un movimiento de tres grados o más", "Así se definió en la clase."), ex("¿Qué se hace si una célula falla?", "Se practica aparte y despacio", "Se aísla antes de unirla de nuevo."), ex("¿Qué se escucha para afinar mejor?", "La nota de referencia", "Sirve para comparar la altura.")],
    (
        f"Con la escala ({NOTAS}), estudia esta melodía de ejemplo de 4 compases: compás 1: 1-2-3-1; compás 2: 3-4-5-3; compás 3: 5-6-5-4; compás 4: 3-2-1-1. 1) Describe el contorno general. 2) Cuenta los saltos (tres grados o más) de la melodía. 3) Divídela en células de 2 compases y escribe cuáles son. 4) Practica cada célula despacio con «la» y anota si afinaste la primera nota de la célula con una referencia.",
        "Contorno: sube hasta el compás 3, donde está la nota más aguda (6), y luego baja. Saltos: hay 4, que son 3 a 1 (dentro del compás 1), 1 a 3 (del compás 1 al 2), 5 a 3 (dentro del compás 2) y 3 a 5 (del compás 2 al 3). Células: compases 1 y 2, y compases 3 y 4.",
        ["describe el contorno con datos", "cuenta los saltos con la regla de tres grados", "divide en células y practica por separado"],
        ["contorno descrito", "saltos contados", "dos células"],
        ["contar un grado conjunto como salto", "practicar todo de corrido"],
        "Reconoce la descripción y pide cantar solo la célula más difícil, partiendo de una nota de referencia.",
    ),
    "Canta con «la» 1-2-3-4-5 y luego 5-4-3-2-1 y nota si suben o bajan por grados conjuntos.",
    "Inventa una melodía de cuatro notas con un salto y practícala por células.",
)

# ---------------------------------------------------------------- OA 03 · clase 3 (conciencia de textura y estilo)
L(
    OA3, 3,
    f"Lápiz y papel. Orden de dinámicas: {DINAMICA}. Los grupos y las piezas están descritos en los ejercicios (son de ejemplo). Si cantas o tocas con otra persona, usen volumen cómodo.",
    "Aprenderé a tocar o cantar con conciencia de la textura (saber si llevo la melodía o el acompañamiento) y del estilo (compás, tempo, articulación y carácter). Sirve para interpretar en grupo equilibrando las voces y respetando el carácter de la pieza.",
    ["Sé que una textura homofónica tiene melodía y acompañamiento.", "Sé que el compás agrupa pulsos.", "Sé que la dinámica es qué tan fuerte o suave suena la música."],
    [
        "Tener conciencia de la textura significa saber qué papel tiene mi voz o mi instrumento. Si llevo la melodía, debo sonar más claro que quienes acompañan. Si acompaño, debo sostener a la melodía sin taparla. Para eso se ajusta la dinámica: si la melodía suena mf, el acompañamiento puede sonar mp, un nivel más suave. En una textura polifónica, cada línea es importante y se escuchan las demás para entrar a tiempo.",
        "El estilo es el conjunto de rasgos que le dan carácter a una pieza: el compás, el tempo, la articulación y la dinámica. Un vals va en compás de 3/4 y acentúa el primer pulso: «uno, dos, tres; uno, dos, tres». Una marcha lleva un pulso firme y parejo, en 2/4 o 4/4, con notas separadas. Una música tranquila y cantable suele ir lenta, con notas ligadas, que se llaman legato, y volumen suave.",
        "Interpretar bien en grupo exige escuchar a las demás voces mientras se toca. Si quien acompaña tapa la melodía, ajusta su dinámica. Si una pieza pide estilo de marcha, se mantiene el pulso firme y las notas separadas, que se llaman staccato. El estilo no se agrega al final: se decide desde el compás, el tempo y la articulación, antes de empezar.",
    ],
    [("textura", "forma en que se combinan las líneas musicales"), ("estilo", "conjunto de rasgos (compás, tempo, articulación, dinámica) que dan carácter a una pieza"), ("legato", "notas unidas, sin cortes entre ellas"), ("staccato", "notas cortas y separadas"), ("equilibrio", "que cada voz suene con la fuerza adecuada a su papel")],
    [
        ("Ajustar un acompañamiento", "La melodía suena mf y el acompañamiento suena también mf y la tapa. ¿Qué nivel de dinámica puede usar el acompañamiento según el orden de la clase?", ["El acompañamiento debe ir un nivel más suave.", "Un nivel más suave que mf es mp."], "mp"),
        ("Calcular una duración de estilo", "Un vals de 16 compases en 3/4 va a 90 pulsos por minuto. ¿Cuántos segundos dura?", ["Pulsos: 16 × 3 = 48.", "48 × 60 ÷ 90 = 32 segundos."], "32 segundos"),
    ],
    [
        ("Pensar que el acompañamiento debe sonar igual de fuerte que la melodía.", "El acompañamiento sostiene; si tapa la melodía, se pierde lo principal.", "Baja un nivel la dinámica de quien acompaña."),
        ("Elegir el estilo al final de la ejecución.", "El estilo depende del compás, el tempo y la articulación, que se deciden desde el comienzo.", "Antes de empezar, lee el compás, el tempo y las marcas de articulación."),
    ],
    [
        ex("En una pieza con voz y guitarra de acompañamiento, ¿quién lleva la melodía?", "La voz", "La guitarra acompaña con acordes."),
        ex("¿Quién debe sonar con más claridad: la melodía o el acompañamiento?", "La melodía", "Es la línea principal."),
        ex("¿Cuántos pulsos tiene un compás de vals?", "3", "El vals va en 3/4."),
    ],
    [
        ex("Para no tapar a la melodía, ¿qué hace quien acompaña: baja su dinámica o la sube?", "La baja", "Así la melodía se oye con claridad."),
        ex("En un vals, ¿qué pulso se acentúa más: el primero o el tercero?", "El primero", "El vals acentúa el primer pulso del compás."),
        ex("¿Qué define el estilo de una pieza? A) Su compás, tempo, articulación y carácter. B) Solo su título.", "A", "El título no dice cómo suena la música."),
    ],
    [
        arith("Un vals de 8 compases en 3/4 se toca una vez. ¿Cuántos pulsos suenan?", "8*3", "Son 8 compases de 3 pulsos cada uno.", " pulsos"),
        arith("Una marcha en 4/4 de 25 compases se toca a 100 pulsos por minuto. ¿Cuántos segundos dura?", "25*4*60//100", "Son 100 pulsos y a 100 por minuto, un minuto completo.", " segundos"),
        ex("La melodía suena mf. ¿Qué dinámica es adecuada para el acompañamiento: mp o f?", "mp", "El acompañamiento va más suave que la melodía."),
    ],
    [
        ex("Un grupo toca una melodía en 4/4, a 90 pulsos por minuto, con notas separadas y fuerte. Otro grupo la toca en 4/4, a 60 pulsos por minuto, con notas ligadas y suave. ¿Cuál suena más tranquilo y cantable?", "El segundo grupo", "Más lento, ligado y suave."),
        ex("En un grupo, quien acompaña toca f y tapa la melodía, que va en mf. ¿Quién debe ajustar su dinámica: la melodía o el acompañamiento?", "El acompañamiento", "Es quien debe sostener sin tapar."),
    ],
    [
        arith("Un vals de 12 compases en 3/4 se toca a 72 pulsos por minuto. ¿Cuántos segundos dura?", "12*3*60//72", "Son 36 pulsos que se convierten a segundos con el tempo.", " segundos"),
        arith("Una marcha en 2/4 de 30 compases se toca a 100 pulsos por minuto. ¿Cuántos segundos dura?", "30*2*60//100", "Son 60 pulsos que se convierten a segundos con el tempo.", " segundos"),
    ],
    [ex("En el acto de tu curso, el coro canta con una guitarra y la guitarra tapa las voces. ¿Qué ajuste corresponde? A) La guitarra baja su dinámica un nivel. B) El coro canta más fuerte que la guitarra.", "A", "Quien acompaña debe sostener a la melodía sin taparla.")],
    [ex("¿Qué significa legato?", "Notas unidas, sin cortes", "Así se tocan las melodías tranquilas y cantables."), ex("¿Cómo se llama tocar las notas cortas y separadas?", "Staccato", "Es la articulación típica de una marcha."), ex("Si acompañas, ¿debes sonar igual de fuerte que la melodía? Responde sí o no.", "No", "Debes sostenerla, no taparla.")],
    (
        f"Con el orden de dinámicas ({DINAMICA}), prepara esta pieza de ejemplo para dos personas: una canta o toca la melodía en mf y la otra acompaña con un pulso por compás. Escribe 1) el estilo de la pieza (compás, tempo, articulación) para una marcha y para una música tranquila, 2) la dinámica de quien acompaña, 3) cuántos segundos dura una marcha de 20 compases en 4/4 a 80 pulsos por minuto. Si puedes, ensáyenla y anota qué ajuste hizo cada persona para escucharse.",
        "Marcha: 4/4, tempo firme a 80, notas separadas (staccato). Música tranquila: 3/4 o 4/4 lento, notas ligadas (legato), volumen suave. Acompañamiento: mp. Duración: 20 × 4 × 60 ÷ 80 = 60 segundos.",
        ["describe estilo con compás, tempo y articulación", "ajusta la dinámica del acompañamiento", "calcula bien la duración"],
        ["estilo descrito", "dinámica elegida", "duración calculada"],
        ["describir el estilo solo con el título", "acompañar tan fuerte como la melodía"],
        "Reconoce el estilo y pide explicar cuál dato de la partitura lo define.",
    ),
    "Cuenta «uno, dos, tres» con el primer pulso más fuerte y di en qué compás está.",
    "Elige una canción y explica cuál es su compás, su tempo aproximado y su articulación.",
)

# ---------------------------------------------------------------- OA 03 · clase 4 (expresividad, fraseo y dinámica)
L(
    OA3, 4,
    f"Lápiz y papel. Orden de dinámicas: {DINAMICA}. Las frases están descritas en los ejercicios con números de compás. Puedes cantarlas con «la» o tocarlas, a volumen cómodo.",
    "Aprenderé a dar expresividad a una interpretación con el fraseo (frases con inicio y llegada), la dinámica (p, f, crescendo, diminuendo) y la articulación (legato y staccato). Sirve para que la música se oiga cantada y con sentido, y no como notas sueltas.",
    ["Sé que la dinámica es qué tan fuerte o suave suena la música.", "Sé que un compás agrupa pulsos.", "Sé distinguir notas ligadas de notas separadas."],
    [
        "Una frase musical es una idea completa, como una oración en el lenguaje. Suele durar 2 o 4 compases, y tiene un comienzo, un punto de mayor intensidad y una llegada. Al cantar, se respira al final de la frase y no en la mitad. En un instrumento, se hace una pequeña pausa o se suaviza el sonido al terminar. Cortar una frase en la mitad hace que la música suene entrecortada.",
        f"La dinámica son los cambios de volumen. Se escribe con letras: {DINAMICA}. Un crescendo es un aumento gradual del volumen y se indica con el signo «<». Un diminuendo es una disminución gradual y se indica con «>». Con la dinámica se da forma a la frase: por ejemplo, empezar en p, crecer hasta f en el punto más intenso y volver a p al llegar.",
        "La articulación es la manera de unir o separar las notas. Legato es notas unidas y cantadas. Staccato es notas cortas y separadas. La fluidez del fraseo se logra cuando se canta sin detenerse en la mitad, con la dinámica planeada de antemano. Cada pieza pide una expresión distinta: una nana pide p y legato, y una marcha pide notas firmes y separadas.",
    ],
    [("frase", "idea musical completa, de 2 o 4 compases, con inicio y llegada"), ("crescendo", "aumento gradual del volumen"), ("diminuendo", "disminución gradual del volumen"), ("articulación", "manera de unir o separar las notas"), ("fluidez de fraseo", "cantar o tocar la frase completa sin cortarla")],
    [
        ("Ordenar las dinámicas", "Ordena de la más suave a la más fuerte: f, p, mf, ff.", ["Se usa el orden pp < p < mp < mf < f < ff.", "p es la más suave de las cuatro y ff la más fuerte."], "p, mf, f, ff"),
        ("Dividir en frases", "Una canción de 16 compases tiene frases de 4 compases. ¿Cuántas pausas hay entre frases?", ["16 ÷ 4 = 4 frases.", "Entre 4 frases hay 3 pausas."], "3 pausas entre frases"),
    ],
    [
        ("Respirar o hacer una pausa en la mitad de la frase.", "Cortar una frase hace que la música suene entrecortada.", "Planea la respiración al final de cada frase."),
        ("Tocar toda la pieza con el mismo volumen.", "Sin cambios de dinámica, la música pierde expresividad.", "Marca en la partitura dónde crece y dónde baja el volumen."),
    ],
    [
        ex("¿Qué significa la letra f en una partitura?", "Fuerte", "Es la abreviatura de fuerte."),
        ex("Un crescendo, ¿aumenta o disminuye el volumen poco a poco?", "Lo aumenta poco a poco", "Es la definición de crescendo."),
        ex("Notas unidas, sin cortes entre ellas, ¿se llaman legato o staccato?", "Legato", "Staccato es separado y corto."),
    ],
    [
        ex("Una frase tiene 4 compases. ¿Dónde conviene respirar: al final del compás 4 o en la mitad del compás 2?", "Al final del compás 4", "Se respira al terminar la frase, no en la mitad."),
        ex("¿Qué articulación tienen las notas cortas y separadas: legato o staccato?", "Staccato", "Así se definió en la clase."),
        ex("Ordena de la más suave a la más fuerte: mp, ff, p, mf.", "p, mp, mf, ff", "Siguen el orden p < mp < mf < ff."),
    ],
    [
        arith("Una canción de 20 compases tiene frases de 4 compases. ¿Cuántas frases tiene?", "20//4", "Se divide el total de compases por el largo de la frase.", " frases"),
        ex("Una frase de 4 compases crece de p a f con un cambio de nivel por compás: p, mp, mf, f. ¿Qué dinámica tiene el compás 3?", "mf", "El compás 3 es el tercer nivel de la secuencia."),
        arith("Una pieza tiene 4 frases de 4 compases en 4/4 y se toca a 80 pulsos por minuto. ¿Cuántos segundos dura?", "16*4*60//80", "Son 64 pulsos y se convierten a segundos con el tempo.", " segundos"),
    ],
    [
        ex("Marta toca una frase de 4 compases, pero hace una pausa larga en el compás 2 para buscar la nota. ¿Qué pierde su interpretación: la fluidez del fraseo o el compás?", "La fluidez del fraseo", "La frase se corta en la mitad."),
        ex("Una nana pide volumen p y legato. Si se toca en ff, ¿qué propósito pierde: arrullar o marchar?", "Arrullar", "El volumen muy fuerte no calma."),
    ],
    [
        arith("Una pieza de 16 compases tiene compases 1–4 en p, compases 5–8 en crescendo, compases 9–12 en f y compases 13–16 en diminuendo. ¿En cuántos compases el volumen se mantiene estable?", "4+4", "Se suman los compases en p y los compases en f.", " compases"),
        ex("En esa misma pieza de 16 compases, ¿en qué compás empieza el diminuendo?", "En el compás 13", "El diminuendo empieza después del compás 12."),
    ],
    [arith("En el acto de fin de año, el coro canta una canción de 24 compases con 6 frases de 4 compases, y la directora pide respirar solo entre una frase y otra. ¿Cuántas respiraciones hay dentro de la canción?", "6-1", "Entre 6 frases hay una pausa menos que frases.", " respiraciones")],
    [ex("¿Cuál es la dinámica más suave de la lista pp, p, mp?", "pp", "pp significa muy suave."), ex("¿Qué signo indica un diminuendo?", ">", "Indica disminución gradual del volumen."), ex("¿Cuántos compases tiene una frase típica de la clase?", "2 o 4", "Las frases de repertorio sencillo duran 2 o 4 compases.")],
    (
        f"Prepara esta frase de ejemplo de 4 compases con la dinámica indicada ({DINAMICA}). Compás 1: p, notas 1-1-5-5. Compás 2: crescendo, notas 6-6-5. Compás 3: f, notas 4-4-3-3. Compás 4: diminuendo, notas 2-2-1. Escribe 1) en qué compás está el punto de mayor intensidad, 2) dónde respiras, 3) qué articulación usas para una canción tranquila. Cántala o tararéala con «la» cuidando la dinámica, y anota si lograste cantar la frase completa sin detenerte.",
        "Mayor intensidad: compás 3 (f). Respiro al final del compás 4. Articulación tranquila: legato. Anotó: «Canté la frase completa sin detenerme y el volumen creció en el compás 2 y bajó en el 4».",
        ["identifica el punto de mayor intensidad", "ubica la respiración al final de la frase", "relaciona la articulación con el carácter"],
        ["tres respuestas escritas", "anotación sobre la fluidez"],
        ["respirar en la mitad", "cantar toda la frase con el mismo volumen"],
        "Reconoce las respuestas y pide cantar la frase marcando con la mano cómo sube y baja el volumen.",
    ),
    "Cuenta una frase de 4 compases con 4 pulsos cada uno y señala dónde respirarías.",
    "Escribe una frase de 4 compases con p, crescendo, f y diminuendo, y explica qué carácter expresa.",
)
