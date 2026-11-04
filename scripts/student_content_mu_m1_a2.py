"""Student material for 1.º medio Música, OA 02 (comparar músicas con características diferentes según elementos del lenguaje musical, procedimientos compositivos y propósito expresivo).

Todas las piezas, melodías y esquemas de los ejercicios son inventados («de ejemplo»); las audiciones reales las selecciona y pone el docente.
"""
from __future__ import annotations

from student_content_mu_m1_a import L
from student_lessons import arith, ex

OA2 = "MU1M OA 02"

FXY = ("Pieza X (de ejemplo): 60 pulsos por minuto, 3 pulsos por compás, modo menor, una voz con guitarra, cuerdas pulsadas suaves. "
       "Pieza Y (de ejemplo): 132 pulsos por minuto, 4 pulsos por compás, modo mayor, varios instrumentos a la vez (vientos y percusión), volumen fuerte")

# ---------------------------------------------------------------- OA 02 · clase 1 (elementos del lenguaje musical)
L(
    OA2, 1,
    f"Lápiz y papel. Fichas de ejemplo, que se repiten en los ejercicios: {FXY}.",
    "Aprenderé a comparar dos músicas elemento por elemento (tempo, compás, modo, textura, timbre y dinámica) usando una tabla. Sirve para decir con precisión en qué se parecen y en qué se diferencian dos músicas.",
    ["Sé que el tempo se mide en pulsos por minuto.", "Sé distinguir volumen fuerte y suave.", "Sé que el timbre es el «color» propio de cada instrumento o voz."],
    [
        "Comparar dos músicas es decir en qué se parecen y en qué se diferencian, elemento por elemento. El tempo es la velocidad del pulso, en pulsos por minuto. El compás agrupa los pulsos: en 3 pulsos por compás se cuenta 1-2-3, 1-2-3, y en 4 se cuenta 1-2-3-4. El modo puede ser mayor o menor: el mayor suele sonar más luminoso y el menor más sombrío, aunque esto depende de cada música.",
        "La textura es la manera en que se combinan los sonidos. Puede haber una melodía sola, una melodía con acompañamiento, como una voz con guitarra, o varias melodías o instrumentos sonando a la vez. El timbre es el color del sonido de cada voz o instrumento, y la dinámica es qué tan fuerte o suave suena. Para comparar con orden, se arma una tabla con una columna por pieza y una fila por elemento.",
        "Compara sin juicios de valor. No se dice «esta es mejor», sino «esta es más rápida: 132 contra 60 pulsos por minuto». También se pueden hacer cálculos con los datos: si una pieza va a 60 pulsos por minuto y tiene 3 pulsos por compás, en un minuto suenan 60 ÷ 3 = 20 compases. Describir con cifras y con elementos permite que otra persona compruebe la comparación.",
    ],
    [("tempo", "velocidad del pulso, en pulsos por minuto"), ("compás", "agrupación de pulsos, como 3 o 4 por compás"), ("modo", "mayor o menor; cambia el carácter de la música"), ("textura", "manera en que se combinan los sonidos: sola, con acompañamiento o varias a la vez"), ("dinámica", "qué tan fuerte o suave suena la música")],
    [
        ("Comparar un elemento", f"{FXY}. ¿Qué pieza tiene el tempo más rápido y cuánto más?", ["Y tiene 132 y X tiene 60.", "132 − 60 = 72."], "Y, con 72 pulsos por minuto más"),
        ("Calcular compases", f"{FXY}. ¿Cuántos compases suenan en 1 minuto de la pieza X?", ["X va a 60 pulsos por minuto.", "Tiene 3 pulsos por compás: 60 ÷ 3 = 20."], "20 compases"),
    ],
    [
        ("Decir «una es mejor» en lugar de comparar.", "Un juicio de valor no muestra en qué elemento se diferencian las piezas.", "Compara con la tabla: elemento, dato de cada pieza y diferencia."),
        ("Creer que el modo menor siempre es triste.", "El modo es solo un rasgo: el carácter depende también del tempo, la dinámica y el contexto.", "Di «suele sonar más sombrío» y apóyate en otros elementos."),
    ],
    [
        ex(f"{FXY}. ¿Cuántos pulsos por compás tiene la pieza X?", "3", "Así lo dice la ficha de la pieza X."),
        ex(f"{FXY}. ¿En qué modo está la pieza Y: mayor o menor?", "Mayor", "La ficha indica modo mayor para la pieza Y."),
        ex(f"{FXY}. ¿Qué pieza suena más fuerte?", "La pieza Y", "Su volumen es fuerte, mientras que X usa cuerdas suaves."),
    ],
    [
        ex("¿Qué es el compás? A) La agrupación de los pulsos, por ejemplo de a 3 o de a 4. B) La velocidad del pulso.", "A", "La velocidad es el tempo; el compás agrupa los pulsos."),
        ex("Una voz con guitarra de acompañamiento es un ejemplo de textura. ¿De qué tipo? A) Melodía con acompañamiento. B) Melodía sola.", "A", "La guitarra acompaña a la voz, que lleva la melodía."),
        ex("¿Qué elemento describe qué tan fuerte o suave suena una música: la dinámica o el modo?", "La dinámica", "El modo es mayor o menor; la dinámica es el volumen."),
    ],
    [
        arith(f"{FXY}. ¿Cuántos compases más suenan en un minuto de la pieza Y que en uno de la pieza X? Calcula los compases de cada una.", "132//4-60//3", "Y tiene 132 ÷ 4 = 33 compases por minuto y X tiene 60 ÷ 3 = 20; se restan.", " compases"),
        ex("Pieza W (de ejemplo): 60 pulsos por minuto, 3 pulsos por compás, modo mayor, una voz con guitarra, cuerdas pulsadas suaves. Pieza X: 60 pulsos por minuto, 3 pulsos por compás, modo menor, una voz con guitarra, cuerdas pulsadas suaves. ¿En qué único elemento se diferencian W y X?", "En el modo", "Los demás datos coinciden y solo cambia mayor por menor."),
        ex("Un estudiante dice: «La pieza Y es mejor que la X porque es más rápida». ¿Qué corrección de la comparación es válida? A) Decir «la Y es más rápida: 132 contra 60 pulsos por minuto». B) Decir «la X es mejor porque es más lenta».", "A", "La comparación describe una diferencia con datos y no emite un juicio de valor."),
    ],
    [
        arith(f"{FXY}. ¿Cuántos pulsos suenan en 2 minutos de la pieza Y?", "132*2", "Se multiplican los pulsos por minuto por los 2 minutos.", " pulsos"),
        ex(f"{FXY}. En la tabla de comparación hay cinco elementos: tempo, compás, modo, textura y timbre. ¿En cuántos se diferencian X e Y?", "5", "El tempo, el compás, el modo, la textura y el timbre son distintos en las fichas."),
    ],
    [
        arith(f"{FXY}. ¿Cuántos compases suenan en 2 minutos de la pieza Y?", "132*2//4", "Primero se calculan los pulsos de 2 minutos y se agrupan de a 4.", " compases"),
        ex("Un homenaje silencioso necesita una música de carácter calmado y solemne. Comparando X e Y de ejemplo, ¿cuál conviene? A) La pieza X. B) La pieza Y.", "A", "X es lenta, suave y de modo menor, rasgos que suelen sonar calmados."),
    ],
    [ex("Comparas en la radio del liceo dos músicas: una de 70 pulsos por minuto y otra de 128. Una compañera dice que son «iguales». ¿Qué elemento prueba que no? A) El tempo: 128 es mucho más rápido que 70. B) El nombre del programa.", "A", "El tempo es un dato que se compara con números.")],
    [ex("¿Qué elemento nombra el color del sonido de una voz o de un instrumento?", "El timbre", "Es lo que distingue a una guitarra de una flauta."), ex("Si una música va a 120 pulsos por minuto con 4 pulsos por compás, ¿cuántos compases suenan en 1 minuto?", "30", "Se divide 120 entre 4."), ex("¿Se compara con juicios («es mejor») o con datos?", "Con datos", "Los datos permiten comprobar la comparación.")],
    (
        "Usa las fichas de ejemplo de las piezas X e Y. Haz una tabla con cinco filas (tempo, compás, modo, textura, timbre) y dos columnas (X e Y). Luego escribe tres frases de comparación, cada una con un dato de cada pieza, y una frase final sobre un propósito para el que serviría mejor cada una.",
        "Tempo: X 60, Y 132. Frase: «Y es más rápida: 132 contra 60 pulsos por minuto». Propósito: X serviría para un momento de calma, porque es lenta y suave; Y para una celebración, porque es rápida y fuerte.",
        ["usa los datos de las fichas", "compara sin juicios de valor", "relaciona cada pieza con un propósito razonable"],
        ["tabla de cinco filas", "tres frases con datos y una frase de propósito"],
        ["decir «es mejor»", "usar datos que no están en las fichas"],
        "Reconoce la tabla y pide elegir el elemento que más cambia el carácter de cada pieza, con una razón.",
    ),
    "Compara dos canciones que conozcas en tempo (rápida o lenta) y en volumen (fuerte o suave).",
    "Haz la tabla de comparación entre una canción de tu casa y la pieza X de ejemplo.",
)

# ---------------------------------------------------------------- OA 02 · clase 2 (procedimientos compositivos)
ESQ = "Melodía de ejemplo, un compás entre barras (1 = do, 2 = re, 3 = mi, 5 = sol): | 1 2 3 1 | 1 2 3 1 | 1 2 3 5 | 1 2 3 1 |"
L(
    OA2, 2,
    f"Lápiz y papel. Esquema de ejemplo, que se repite en los ejercicios: {ESQ}.",
    "Aprenderé a reconocer procedimientos compositivos (repetición, variación, contraste, ostinato, imitación o canon y pregunta-respuesta) y a nombrar la forma de una pieza con letras. Sirve para comparar cómo están construidas dos músicas, no solo cómo suenan.",
    ["Sé comparar piezas por tempo, compás y modo.", "Sé que una melodía es una sucesión de notas.", "Sé que una frase musical se puede escribir con números."],
    [
        "Los procedimientos compositivos son las maneras en que una persona compositora organiza el material musical. La repetición vuelve a presentar una idea igual. La variación la presenta con algún cambio, y se marca con una prima: A y A'. El contraste introduce algo distinto, que se marca con otra letra: B. Con estas letras se describe la forma: A A' B A significa una idea, su variación, una idea distinta y el regreso de la primera.",
        "Otros procedimientos son el ostinato, un patrón corto que se repite muchas veces, casi siempre en el acompañamiento; la imitación, cuando una voz repite lo que acaba de tocar otra, y el canon, que es una imitación completa en que la segunda voz entra después y canta lo mismo. También existe la pregunta y respuesta, donde una frase queda abierta y la siguiente la contesta.",
        "Para reconocerlos, se escucha o se lee la pieza y se marca cada sección con una letra. Si dos secciones suenan igual, llevan la misma letra; si cambian un poco, la misma letra con prima; si cambian mucho, otra letra. Conocer el procedimiento ayuda a comparar: dos piezas pueden tener el mismo tempo y modo, y aun así estar construidas de forma muy distinta.",
    ],
    [("repetición", "volver a presentar una idea musical igual"), ("variación", "presentar una idea con algún cambio"), ("contraste", "presentar una idea distinta"), ("ostinato", "patrón corto que se repite muchas veces"), ("canon", "imitación en que una voz entra después y repite la melodía de la primera")],
    [
        ("Leer una forma", "Una pieza de ejemplo tiene la forma A A' B A. ¿Cuántas ideas distintas usa y cuál se repite al final?", ["Hay dos letras distintas: A y B.", "A' es una variación de A.", "Termina con A."], "Dos ideas distintas, y al final vuelve A"),
        ("Calcular un canon", "Una melodía de 8 compases se canta en canon: la voz 2 entra 2 compases después de la voz 1. ¿Cuántos compases suenan juntas las dos voces?", ["La voz 1 suena en los compases 1 a 8.", "La voz 2 suena en los compases 3 a 10.", "Coinciden de 3 a 8: 6 compases."], "6 compases"),
    ],
    [
        ("Llamar «variación» a cualquier cambio completo.", "Si lo que aparece es muy distinto, es un contraste y lleva otra letra.", "Usa la prima solo si se reconoce la idea original."),
        ("Pensar que repetir es hacer lo mismo sin intención.", "La repetición fija una idea en el oído y da unidad a la pieza.", "Pregúntate qué efecto produce volver a oír la misma idea."),
    ],
    [
        ex(f"{ESQ}. ¿Qué procedimiento hay entre el compás 1 y el compás 2: repetición o contraste?", "Repetición", "Los dos compases tienen las mismas notas: 1 2 3 1."),
        ex(f"{ESQ}. ¿Qué compás es una variación de la idea inicial: el 3 o el 4?", "El compás 3", "Mantiene 1 2 3, pero termina en 5 en lugar de 1."),
        ex("¿Cómo se llama un patrón corto que se repite muchas veces, casi siempre en el acompañamiento?", "Ostinato", "Ese es el significado de ostinato."),
    ],
    [
        ex("Una pieza tiene la forma A B A. ¿Cuántas ideas distintas tiene? A) Dos. B) Tres.", "A", "Las letras distintas son solo A y B; A vuelve al final."),
        ex("Una voz canta una frase y otra voz la repite con las mismas notas dos compases después. ¿Qué procedimiento es? A) Un canon. B) Una pregunta y respuesta.", "A", "La segunda voz imita completamente a la primera, entrando más tarde."),
        ex("Una frase queda abierta, como una pregunta, y la siguiente la responde. ¿Cómo se llama ese procedimiento? A) Pregunta y respuesta. B) Ostinato.", "A", "Una frase abierta seguida de una que responde es pregunta y respuesta."),
    ],
    [
        ex(f"{ESQ}. Si se marca la forma con letras, ¿cuál es la forma de la melodía? Considera que el compás 3 es una variación. Usa A y A'.", "A A A' A", "Los compases 1 y 2 son iguales, el 3 es variación y el 4 vuelve a la idea inicial."),
        ex("Una segunda frase empieza igual que la primera, pero con la última nota cambiada. ¿Es repetición, variación o contraste?", "Variación", "Se reconoce la idea original, con un cambio pequeño."),
    ],
    [
        ex("Dos piezas de ejemplo tienen el mismo tempo y el mismo modo. La primera tiene la forma A B A y la segunda A A' A''. ¿Por qué siguen siendo distintas? A) Porque la primera contrasta y la segunda solo varía la misma idea. B) Porque cambia el volumen.", "A", "Una introduce una idea nueva (B) y la otra solo transforma la misma idea."),
        ex("Una pieza de ejemplo tiene la forma A A' B A'. ¿En cuántas secciones aparece la idea A, original o variada?", "3", "Aparece en la primera sección, en la segunda (A') y en la cuarta (A')."),
    ],
    [
        arith("En un canon de 12 compases, la voz 2 entra 4 compases después de la voz 1. ¿Cuántos compases suenan las dos voces juntas?", "12-4", "Las dos coinciden desde que entra la voz 2 hasta que termina la voz 1.", " compases"),
        arith("Un ostinato de 2 pulsos se repite durante 6 compases de 4 pulsos cada uno. ¿Cuántas veces suena el ostinato?", "6*4//2", "En 6 compases hay 24 pulsos y cada ostinato ocupa 2.", " veces"),
    ],
    [ex("Un grupo toca un ostinato de 4 pulsos que se repite durante 8 compases de 4 pulsos cada uno. ¿Cuántas veces suena el ostinato completo?", "8", "Cada compás de 4 pulsos contiene un ostinato entero.")],
    [ex("¿Qué letra se usa para una idea distinta que contrasta con A?", "B", "Una idea nueva lleva otra letra."), ex("¿Cómo se marca una variación de A?", "A'", "La prima indica que es A con cambios."), ex("En un canon, ¿la segunda voz canta lo mismo o algo distinto?", "Lo mismo", "Imita la melodía de la primera, entrando después.")],
    (
        "Usa la melodía de ejemplo del enunciado (| 1 2 3 1 | 1 2 3 1 | 1 2 3 5 | 1 2 3 1 |). Con 1 = do, 2 = re, 3 = mi, 5 = sol, tararea o toca cada compás. Responde: a) qué compases se repiten, b) cuál es la variación y qué cambió, c) qué forma tiene con letras. Luego escribe un compás nuevo de contraste con otros cuatro números del 1 al 5 y di qué letra le pondrías.",
        "a) Los compases 1, 2 y 4. b) El compás 3, porque la última nota cambia de 1 a 5. c) A A A' A. Contraste: | 5 4 3 2 | y letra B.",
        ["identifica repetición y variación con datos de la melodía", "escribe la forma con letras", "propone un contraste y lo marca con otra letra"],
        ["respuestas a), b) y c)", "compás nuevo escrito con números"],
        ["llamar variación a algo totalmente distinto", "olvidar la prima"],
        "Reconoce la forma y pide explicar qué efecto produce que al final vuelva la idea inicial.",
    ),
    "Tararea dos veces una frase corta y luego cámbiale una nota: anota qué procedimiento usaste.",
    "Escribe la forma con letras de una canción de tu casa que tenga estrofas y estribillo.",
)

# ---------------------------------------------------------------- OA 02 · clase 3 (comparar según el propósito expresivo)
FPQ = ("Pieza P (de ejemplo): se toca en una celebración pública; 140 pulsos por minuto, 2 pulsos por compás, modo mayor, coro y percusión, volumen fuerte. "
       "Pieza Q (de ejemplo): se toca en un homenaje; 56 pulsos por minuto, 4 pulsos por compás, modo menor, cuarteto de cuerdas, volumen suave")
L(
    OA2, 3,
    f"Lápiz y papel. Fichas de ejemplo, que se repiten en los ejercicios: {FPQ}.",
    "Aprenderé a comparar dos músicas relacionando cada diferencia con el propósito expresivo de cada una, escribiendo frases con tres partes: dato, efecto y propósito. Sirve para explicar por qué dos músicas distintas pueden ser igualmente adecuadas para lo que buscan.",
    ["Sé comparar tempo, compás, modo, textura y timbre.", "Sé reconocer repetición, variación y contraste.", "Sé que el propósito es lo que la música busca lograr."],
    [
        "El propósito expresivo es lo que una música busca comunicar o lograr: alegría compartida, solemnidad, calma, energía. Comparar bien no termina en listar diferencias; hay que unir cada diferencia con ese propósito. Una frase completa tiene tres partes: el dato (qué se oye), el efecto (qué produce) y el propósito (para qué sirve). Por ejemplo: «La pieza Q va a 56 pulsos por minuto; eso da un aire solemne, adecuado para un homenaje».",
        "Dos músicas muy distintas pueden ser adecuadas, cada una para su propósito. Una pieza rápida, fuerte y de modo mayor sirve para celebrar, y una lenta, suave y de modo menor sirve para recordar con calma. Por eso no se dice cuál es mejor en general, sino cuál es mejor para qué. Si cambia el propósito, cambia la mejor elección.",
        "También se puede comprobar con cálculos. Si P va a 140 pulsos por minuto y tiene 2 pulsos por compás, en un minuto suenan 140 ÷ 2 = 70 compases; Q, con 56 pulsos y 4 por compás, tiene 14. Esa gran diferencia de compases por minuto muestra que P se siente mucho más movida. Al ensayar, se cambia un elemento de una pieza y se comprueba si el cambio ayuda o perjudica su propósito.",
    ],
    [("propósito expresivo", "lo que una música busca comunicar o lograr"), ("dato", "lo que se oye o se mide en la música"), ("efecto", "lo que produce en quien escucha"), ("solemne", "serio y respetuoso, propio de una ceremonia"), ("adecuado", "que sirve bien a un propósito")],
    [
        ("Frase de tres partes", f"{FPQ}. Escribe una frase con dato, efecto y propósito sobre el tempo de P.", ["Dato: 140 pulsos por minuto.", "Efecto: sensación de movimiento.", "Propósito: celebrar."], "P va a 140 pulsos por minuto; eso da movimiento, adecuado para una celebración"),
        ("Cambiar un elemento", f"{FPQ}. Si se toca P a 56 pulsos por minuto y suave, ¿sirve igual para una celebración?", ["Ahora es lenta y suave.", "Pierde el movimiento que pide una celebración."], "No: se parece más a un homenaje que a una celebración"),
    ],
    [
        ("Decidir qué pieza es mejor sin decir para qué.", "Cada pieza es adecuada para su propósito; no hay una mejor en general.", "Escribe «es mejor para… porque…»."),
        ("Listar diferencias sin explicar su efecto.", "Una lista de datos no muestra por qué cada pieza sirve a su propósito.", "Cada dato debe terminar en un efecto y un propósito."),
    ],
    [
        ex(f"{FPQ}. ¿Para qué se toca la pieza Q?", "Para un homenaje", "Así lo dice su ficha."),
        ex(f"{FPQ}. ¿Qué pieza tiene el volumen más suave?", "La pieza Q", "Q es suave y P es fuerte."),
        ex(f"{FPQ}. ¿Qué pieza tiene menos pulsos por compás?", "La pieza P", "P tiene 2 pulsos por compás y Q tiene 4."),
    ],
    [
        ex("¿Cuáles son las tres partes de una buena frase de comparación? A) Dato, efecto y propósito. B) Nombre, fecha y lugar.", "A", "Se une lo que se oye con lo que produce y con su finalidad."),
        ex("¿Qué enunciado compara bien? A) «P es más rápida que Q, y eso da movimiento a la celebración.» B) «P es mejor que Q.»", "A", "El primero da un dato, un efecto y un propósito; el segundo es un juicio sin razón."),
        ex("Si cambia el propósito de una música, ¿qué debe cambiar en la comparación? A) La elección de la pieza más adecuada. B) El nombre de las notas.", "A", "La mejor elección depende de lo que la música busca lograr."),
    ],
    [
        arith(f"{FPQ}. ¿Cuántos compases suenan en 2 minutos de la pieza P?", "140*2//2", "Se dividen los pulsos por minuto entre los pulsos de cada compás.", " compases"),
        arith(f"{FPQ}. ¿Cuántos compases suenan en 3 minutos de la pieza Q?", "56*3//4", "Se dividen los pulsos por minuto entre los pulsos de cada compás.", " compases"),
        ex(f"{FPQ}. Una persona dice que Q no sirve para un homenaje porque «es muy lenta». ¿Qué respuesta usa un criterio válido? A) Que su lentitud y su volumen suave dan solemnidad, adecuada para recordar. B) Que Q no tiene percusión.", "A", "El tempo lento y el volumen suave encajan con el propósito del homenaje."),
    ],
    [
        arith(f"{FPQ}. ¿Cuántos pulsos suenan en 3 minutos de la pieza P?", "140*3", "Se multiplican los pulsos por minuto por los 3 minutos.", " pulsos"),
        ex("Un liceo quiere una música para una despedida de promoción que combine alegría y emoción. Dice que podría tomar de P el modo mayor y de Q el volumen suave. ¿Qué comparación sostiene esa idea? A) Que el modo mayor suele sonar luminoso y lo suave da cercanía. B) Que las dos tienen el mismo tempo.", "A", "Cada elemento tomado se justifica por el efecto que produce."),
    ],
    [
        arith(f"{FPQ}. Para un acto que dura 6 minutos, la pieza P suena los 6 minutos y la pieza Q suena 6 minutos. ¿Cuántos pulsos más suenan en P que en Q?", "140*6-56*6", "Se calculan los pulsos de cada pieza en 6 minutos y se restan.", " pulsos"),
        ex(f"{FPQ}. Para una ceremonia de recuerdo de una persona querida, un liceo debe elegir entre P y Q. ¿Qué pieza conviene y por qué razón? A) Q, porque su tempo lento y su volumen suave dan solemnidad. B) P, porque su coro y su percusión animan al público.", "A", "El propósito de recordar con respeto pide solemnidad, que Q ofrece."),
    ],
    [ex("Un curso debe elegir una música para animar la salida a un patio con juegos. Compara una pieza de 60 pulsos por minuto y suave con otra de 130 y fuerte. ¿Cuál conviene? A) La de 130 pulsos por minuto y fuerte. B) La de 60 pulsos por minuto y suave.", "A", "Para animar se necesita movimiento y energía.")],
    [ex("¿Para qué se toca la pieza P de ejemplo?", "Para una celebración pública", "Así lo dice su ficha."), ex("Una pieza de ejemplo va a 90 pulsos por minuto con 3 pulsos por compás. ¿Cuántos compases suenan en 1 minuto?", "30", "Se divide 90 entre 3."), ex("¿Cuál es la última parte de una frase de comparación: el dato, el efecto o el propósito?", "El propósito", "Se termina diciendo para qué sirve.")],
    (
        "Usa las fichas de ejemplo P y Q. Escribe tres frases de comparación, cada una con dato, efecto y propósito (una sobre el tempo, otra sobre el modo y otra sobre el volumen). Después escribe qué elemento de Q cambiarías para que sirviera a una fiesta, y qué efecto esperas.",
        "Tempo: P va a 140 pulsos por minuto y Q a 56; P da movimiento para celebrar y Q da calma para recordar. Cambio: subiría el tempo de Q a unos 120 pulsos por minuto, para que se sintiera más animada, aunque seguiría suave.",
        ["cada frase tiene dato, efecto y propósito", "usa los datos de las fichas", "propone un cambio coherente y anticipa su efecto"],
        ["tres frases de comparación", "cambio propuesto con efecto"],
        ["listar datos sin efecto", "decidir cuál es mejor sin decir para qué"],
        "Reconoce las frases y pide revisar cuál de las tres es más sólida y por qué.",
    ),
    "Elige una música de tu casa y completa: «Dato: …; efecto: …; propósito: …».",
    "Cambia el propósito de la pieza Q de ejemplo (por ejemplo, para una carrera) y escribe tres cambios que le harías.",
)

# ---------------------------------------------------------------- OA 02 · clase 4 (crear dos patrones que contrastan)
L(
    OA2, 4,
    "Lápiz y papel; si quieres, palmas o dos objetos livianos para golpear suavemente una mesa. Los patrones están escritos en los ejercicios con x (golpe) y - (silencio), un símbolo por pulso.",
    "Aprenderé a crear dos patrones rítmicos de 8 pulsos que contrasten (uno más movido y otro más calmado) y a compararlos con datos. Sirve para practicar la comparación creando música, no solo escuchándola.",
    ["Sé comparar dos músicas por sus elementos.", "Sé relacionar una diferencia con el propósito.", "Sé marcar un pulso con palmas."],
    [
        "Un patrón rítmico es una serie de golpes y silencios ordenados en pulsos. En la escritura de este cuaderno, la x es un golpe y el guion es un silencio, y cada símbolo ocupa un pulso. Así, x - x x son cuatro pulsos con tres golpes. La densidad es la cantidad de golpes que hay en un número de pulsos: más golpes en el mismo número de pulsos significa un patrón más movido.",
        "Para comparar dos patrones se cuentan los golpes y los silencios, se mira dónde caen y se calcula la densidad. Un patrón con muchos golpes seguidos suena activo e insistente; uno con silencios largos suena espaciado y calmado. Si el pulso va a 120 por minuto, cada pulso dura medio segundo, de modo que 8 pulsos duran 4 segundos.",
        "Al crear, se parte del propósito: si quiero un patrón movido, pongo más golpes y pocos silencios; si busco uno calmado, dejo silencios largos. Después se tocan ambos con palmas, se comparan y se explica la diferencia con datos. Se puede mejorar cambiando un solo símbolo y comprobando qué cambia en el sonido. Todo se hace con golpes suaves, que no molestan ni dañan las manos.",
    ],
    [("patrón rítmico", "serie de golpes y silencios ordenados en pulsos"), ("golpe", "sonido corto, escrito x"), ("silencio", "pulso en que no suena nada, escrito -"), ("densidad", "cantidad de golpes que hay en cierto número de pulsos"), ("contraste", "diferencia clara entre dos patrones")],
    [
        ("Contar golpes", "Patrón de ejemplo de 8 pulsos: x - x x x - x -. ¿Cuántos golpes y cuántos silencios tiene?", ["Los golpes están en los pulsos 1, 3, 4, 5 y 7.", "Los silencios en los pulsos 2, 6 y 8."], "5 golpes y 3 silencios"),
        ("Duración en segundos", "Un patrón de 8 pulsos se toca a 120 pulsos por minuto. ¿Cuántos segundos dura?", ["A 120 por minuto, cada pulso dura medio segundo.", "8 × medio segundo = 4 segundos."], "4 segundos"),
    ],
    [
        ("Hacer dos patrones casi iguales y llamarlos contraste.", "Un contraste necesita una diferencia clara, como mucha densidad contra poca.", "Compara el número de golpes de los dos patrones."),
        ("Contar mal los silencios al comparar.", "El silencio también ocupa un pulso y cambia la densidad.", "Marca cada pulso con x o con guion antes de contar."),
    ],
    [
        ex("Patrón de ejemplo: x x - x. ¿Cuántos golpes tiene?", "3", "Hay golpes en los pulsos 1, 2 y 4."),
        ex("Patrón de ejemplo: x - - - x - - -. ¿Cuántos silencios tiene?", "6", "Solo los pulsos 1 y 5 son golpes; los otros seis son silencios."),
        ex("Patrón de ejemplo: x x x x x x - -. ¿Cuántos pulsos tiene en total?", "8", "Cada símbolo es un pulso y hay ocho símbolos."),
    ],
    [
        ex("Patrón 1: x x x - x x x -. Patrón 2: x - - - x - - -. ¿Cuál es más movido? A) El patrón 1. B) El patrón 2.", "A", "El patrón 1 tiene 6 golpes en 8 pulsos y el 2 solo 2."),
        ex("Quieres un patrón de 8 pulsos calmado. ¿Cuál conviene? A) x - - - x - - -. B) x x x x x x x x.", "A", "Tiene silencios largos y pocos golpes."),
        ex("Un patrón de 8 pulsos tiene 4 golpes. ¿Cuántos silencios tiene?", "4", "Los 8 pulsos se reparten entre golpes y silencios: 8 − 4."),
    ],
    [
        arith("Patrón A de ejemplo: x x - x x - x -. Patrón B de ejemplo: x - - - x - - -. ¿Cuántos golpes más tiene el patrón A que el B?", "5-2", "Se restan los golpes del patrón B a los del patrón A.", " golpes"),
        ex("Patrón de ejemplo de 8 pulsos: x - - x x - x x. Al cambiar el pulso 2 de silencio a golpe, ¿cuántos golpes tiene el nuevo patrón?", "6", "Tenía 5 golpes (pulsos 1, 4, 5, 7 y 8) y se agrega 1."),
        ex("Patrón de ejemplo de 8 pulsos: x x - x - x x -. ¿Cuántos golpes tiene?", "5", "Hay golpes en los pulsos 1, 2, 4, 6 y 7."),
    ],
    [
        arith("Se tocan, uno tras otro, un patrón movido de 8 pulsos y uno calmado de 8 pulsos, ambos a 120 pulsos por minuto. ¿Cuántos segundos dura todo?", "(8+8)//2", "En total son 16 pulsos y, a 120 por minuto, cada pulso dura medio segundo.", " segundos"),
        ex("Un estudiante dice que sus patrones contrastan porque uno tiene 5 golpes y el otro 4 en 8 pulsos. ¿Es un buen contraste? Responde sí o no.", "No", "La diferencia es de un solo golpe; falta una diferencia clara de densidad."),
    ],
    [
        arith("Un patrón de 8 pulsos con 5 golpes se repite dos veces seguidas. ¿Cuántos golpes suenan en total?", "5*2", "Cada repetición tiene 5 golpes y son 2 repeticiones.", " golpes"),
        arith("Una pieza repite 15 veces un patrón de 8 pulsos a 120 pulsos por minuto. ¿Cuántos segundos dura?", "15*8//2", "Son 120 pulsos y cada pulso dura medio segundo.", " segundos"),
    ],
    [ex("Quieres crear dos patrones de 8 pulsos para una escena: uno para correr y otro para esperar. ¿Cuál asignas a correr? A) x x x x - x x x. B) x - - - - - x -.", "A", "El patrón de muchos golpes seguidos suena activo, como una carrera.")],
    [ex("¿Qué símbolo marca un silencio en este cuaderno?", "El guion", "El guion ocupa un pulso sin sonido."), ex("¿Qué significa más densidad?", "Más golpes en los mismos pulsos", "Densidad es cantidad de golpes por pulsos."), ex("A 120 pulsos por minuto, ¿cuánto dura un pulso?", "Medio segundo", "60 segundos entre 120 pulsos.")],
    (
        "Crea dos patrones de 8 pulsos con x y guion: el patrón M, movido, y el patrón C, calmado. Para ayudarte, parte de este modelo: M = x x - x x x - x y C = x - - - x - - -; cambia al menos dos símbolos de cada uno. Responde: a) cuántos golpes tiene cada patrón, b) cuál es su densidad, c) una frase de comparación con dato, efecto y propósito. Tócalos con palmas suaves.",
        "M = x x x x x x x - (cambié tres símbolos): 7 golpes. C = x - - - - - x - (cambié dos símbolos): 2 golpes. M tiene 7 golpes en 8 pulsos y C tiene 2; M suena movido y sirve para correr; C suena espaciado y sirve para esperar.",
        ["cambia al menos dos símbolos de cada modelo", "cuenta bien los golpes", "compara con dato, efecto y propósito"],
        ["dos patrones escritos", "frase de comparación"],
        ["patrones casi iguales", "contar mal los silencios"],
        "Reconoce los patrones y pide cambiar un símbolo del patrón C para que sea aún más calmado.",
    ),
    "Toca con palmas suaves el patrón x - x x x - x - y cuenta cuántos golpes sonaron.",
    "Crea un tercer patrón de 8 pulsos con exactamente 4 golpes y explica en qué se parece a los otros dos.",
)
