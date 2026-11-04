"""Student material for 1.º medio Música, OA 03 (cantar y tocar repertorio diverso relacionado con la música escuchada: estilo, identificación de voces en un grupo, propósito expresivo, laboriosidad y compromiso).

Todas las piezas, partes y pautas de los ejercicios son inventadas («de ejemplo»); el repertorio real lo selecciona el docente.
"""
from __future__ import annotations

from student_content_mu_m1_a import L
from student_lessons import arith, ex

OA3 = "MU1M OA 03"

EST = ("Estilo X (de ejemplo, canto de fiesta): notas cortas y separadas, 120 pulsos por minuto, voz abierta y fuerte, palmas marcando el pulso. "
       "Estilo Y (de ejemplo, balada): notas largas y unidas, 66 pulsos por minuto, voz suave, guitarra que acompaña")

# ---------------------------------------------------------------- OA 03 · clase 1 (rasgos de estilo)
L(
    OA3, 1,
    f"Lápiz y papel; voz baja o tarareo si quieres probar. Fichas de ejemplo, que se repiten en los ejercicios: {EST}. Canta siempre con volumen cómodo, sin gritar ni forzar la garganta.",
    "Aprenderé a reconocer los rasgos que forman el estilo de una música (articulación, fraseo, tempo, dinámica y manera de cantar o tocar) para poder interpretarla con ese estilo. Sirve para cantar y tocar repertorio variado respetando lo que lo hace reconocible.",
    ["Sé comparar dos músicas por tempo y volumen.", "Sé que el timbre es el color del sonido.", "Sé que el pulso se mide en pulsos por minuto."],
    [
        "El estilo es el conjunto de rasgos que hace reconocible una música y la distingue de otra. Para interpretar con estilo hay que fijarse en cómo se tocan o cantan las notas. La articulación es la manera de unir o separar los sonidos: si están unidos y fluidos se llama legato, y si son cortos y separados se llama staccato. El fraseo es la manera de agrupar las notas en frases, con su inicio, su avance y un pequeño descanso para respirar al final.",
        "También forman parte del estilo el tempo, la dinámica y la manera de emitir la voz o tocar el instrumento: una voz abierta y fuerte da un estilo de fiesta, y una voz suave y cercana da un estilo íntimo. Si se interpreta una balada con notas cortas y muy fuertes, la música pierde su carácter, aunque las notas sean correctas. Respetar el estilo no es copiar sin pensar, sino reconocer los rasgos y reproducirlos con intención.",
        "Cuidar la voz y el cuerpo también es parte de interpretar bien: se canta con volumen cómodo, se bebe agua y se calienta antes de empezar, sin forzar ni gritar. Para tocar un instrumento se cuida la postura y las manos. Si algo duele, se detiene el ensayo y se avisa a una persona adulta. La técnica y la salud trabajan juntas.",
    ],
    [("estilo", "conjunto de rasgos que hace reconocible una música"), ("articulación", "manera de unir o separar los sonidos"), ("legato", "sonidos unidos y fluidos"), ("staccato", "sonidos cortos y separados"), ("fraseo", "manera de agrupar las notas en frases")],
    [
        ("Elegir la articulación", f"{EST}. ¿Qué articulación pide el estilo X: legato o staccato?", ["Sus notas son cortas y separadas.", "Eso es staccato."], "Staccato"),
        ("Respetar el estilo", f"{EST}. Un grupo canta el estilo Y con voz fuerte y notas muy cortas. ¿Qué rasgos del estilo Y pierde?", ["Y pide notas largas y unidas, y voz suave.", "El grupo usa justo lo contrario."], "Pierde las notas unidas (legato) y la voz suave"),
    ],
    [
        ("Cantar fuerte para «mostrar estilo».", "Forzar la voz daña la garganta y no es lo que pide un estilo suave.", "Elige el volumen según el estilo y cuida la voz."),
        ("Creer que acertar las notas basta.", "Un estilo también exige articulación, fraseo, tempo y dinámica propios.", "Revisa cada rasgo del estilo antes de interpretar."),
    ],
    [
        ex(f"{EST}. Una canción usa palmas marcando el pulso y notas cortas y separadas. ¿Con qué estilo coincide: X o Y?", "X", "Esos rasgos están en la ficha del estilo X."),
        ex("Notas unidas y fluidas, sin cortes entre ellas: ¿legato o staccato?", "Legato", "Legato significa sonidos unidos."),
        ex("Notas cortas y separadas, con pequeños silencios entre ellas: ¿legato o staccato?", "Staccato", "Staccato significa sonidos cortos y separados."),
    ],
    [
        ex(f"{EST}. ¿Qué voz corresponde al estilo Y? A) Suave y cercana. B) Abierta y fuerte.", "A", "La ficha de Y indica voz suave y guitarra de acompañamiento."),
        ex("¿Qué es el fraseo? A) Agrupar las notas en frases, con un pequeño descanso al final. B) Cantar siempre más fuerte.", "A", "Es la manera de dar forma a la melodía en frases."),
        ex("Si te duele la garganta al cantar, ¿qué haces primero? A) Detener el ensayo y avisar a una persona adulta. B) Cantar más fuerte para pasar la molestia.", "A", "Forzar una voz que duele puede dañarla."),
    ],
    [
        arith(f"{EST}. ¿Cuántos pulsos más por minuto tiene el estilo X que el estilo Y?", "120-66", "Se restan los pulsos por minuto del estilo Y a los del X.", " pulsos"),
        ex("Un grupo debe interpretar una balada: notas largas, unidas, voz suave, 66 pulsos por minuto. Canta con notas separadas, voz fuerte y 120 pulsos por minuto. ¿Cuántos de esos tres rasgos (articulación, voz y tempo) están equivocados?", "3", "Los tres son contrarios a los de la balada."),
        ex("¿Qué cambia si una frase pasa de staccato a legato? A) Las notas se unen y la frase suena más fluida. B) El tempo sube a 120 pulsos por minuto.", "A", "Legato une los sonidos; el tempo es otro rasgo."),
    ],
    [
        ex(f"{EST}. Un estudiante dice: «Si canto las notas del estilo X unidas, sigue siendo X porque las notas son las mismas». ¿Es cierto, sí o no?", "No", "El estilo X depende también de la articulación staccato; unidas se parece más a otro estilo."),
        arith(f"{EST}. Un ensayo del estilo X dura 3 minutos y se marca el pulso con una palma por pulso. ¿Cuántas palmas se dan?", "120*3", "Se multiplican los pulsos por minuto por los minutos.", " palmas"),
    ],
    [
        arith(f"{EST}. Un grupo canta el estilo X durante 2 minutos y luego el estilo Y durante 2 minutos. ¿Cuántos pulsos suenan en total?", "120*2+66*2", "Se calculan los pulsos de cada estilo y se suman.", " pulsos"),
        ex(f"{EST}. En las fichas aparecen cuatro rasgos: la duración de las notas, el tempo, la voz y el acompañamiento. ¿Cuántos de ellos cambia un grupo al pasar de cantar X a cantar Y?", "4", "Los cuatro rasgos son distintos en las dos fichas."),
    ],
    [ex(f"{EST}. Te piden cantar en un cumpleaños una canción de estilo X. ¿Qué decisión de interpretación conviene? A) Notas cortas, voz abierta y palmas marcando el pulso. B) Notas largas y unidas, voz muy suave.", "A", "Esos son los rasgos del estilo X de la ficha.")],
    [ex("En Música: ¿qué es el estilo de una pieza?", "El conjunto de rasgos que la hace reconocible", "Incluye articulación, fraseo, tempo y dinámica."), ex("¿Qué articulación tiene notas unidas?", "Legato", "Legato significa unidas y fluidas."), ex("¿Qué significa «fraseo»?", "Agrupar las notas en frases", "Cada frase tiene inicio, avance y un pequeño descanso.")],
    (
        "Elige el estilo X o el estilo Y de las fichas de ejemplo. Escribe: a) tres rasgos del estilo que vas a respetar, b) cómo cantarías o tocarías la frase «la tarde ya llegó» (que repites dos veces) en ese estilo, con articulación, volumen y tempo, c) una acción para cuidar tu voz. Si quieres, pruébalo tarareando.",
        "Estilo Y. a) Notas largas y unidas, voz suave, 66 pulsos por minuto. b) La frase en legato, volumen suave y tempo lento, con una respiración entre las dos repeticiones. c) Tomar agua y no cantar más fuerte de lo cómodo.",
        ["elige rasgos que están en la ficha", "describe articulación, volumen y tempo", "incluye una acción segura para cuidar la voz"],
        ["tres rasgos del estilo", "descripción de la interpretación y acción de cuidado"],
        ["mezclar rasgos de los dos estilos", "forzar la voz"],
        "Reconoce la ficha y pide indicar qué cambiaría en la interpretación si el estilo fuera el otro.",
    ),
    "Tararea la misma frase con notas unidas y luego con notas cortas, y anota qué cambia.",
    "Escribe los rasgos de estilo de una canción que cantes en tu casa: articulación, tempo y voz.",
)

# ---------------------------------------------------------------- OA 03 · clase 2 (identificar voces en un grupo)
CORO = ("Coro de ejemplo de 20 personas: 8 sopranos (voz aguda), 5 contraltos (voz media-aguda), 4 tenores (voz media-grave) y el resto bajos (voz grave). "
        "En la pieza de ejemplo, la melodía principal la canta la voz 1; la voz 2 canta una segunda melodía más grave y la guitarra marca el pulso")
L(
    OA3, 2,
    f"Lápiz y papel. Datos de ejemplo, que se repiten en los ejercicios: {CORO}.",
    "Aprenderé a identificar las voces de un grupo (unísono, voz principal, voces de acompañamiento y tipos de voz) y a reconocer el rol que cumple cada una. Sirve para saber qué parte me toca cantar o tocar y cómo escuchar a las demás.",
    ["Sé reconocer rasgos de estilo.", "Sé que una melodía puede ser aguda o grave.", "Sé distinguir un sonido fuerte de uno suave."],
    [
        "En un grupo musical no todas las personas hacen lo mismo. Cuando todas cantan la misma melodía a la misma altura, cantan al unísono. Cuando hay varias partes, se llaman voces: la voz principal lleva la melodía más importante y las otras voces la acompañan, es decir, la apoyan sin taparla. Escuchar a las demás es tan importante como cantar o tocar bien la propia parte.",
        "Los tipos de voz humana se ordenan de aguda a grave: soprano, contralto, tenor y bajo. En un coro, cada cuerda se agrupa y canta su parte. En un grupo instrumental ocurre algo parecido: unos instrumentos llevan la melodía, otros la armonía (varios sonidos a la vez que acompañan) y otros marcan el pulso. Identificar la voz propia permite ensayar solo esa parte y luego unirla con las otras.",
        "Para transmitir el propósito expresivo de una pieza, el grupo decide quién se destaca en cada momento. Si la voz principal debe oírse, las demás bajan su volumen. Si hay un cambio de carácter, todas cambian a la vez. Esto exige comunicación: mirar a la persona que dirige, respirar juntas y empezar en el mismo pulso. Un grupo bien coordinado no suena más fuerte, sino más claro.",
    ],
    [("unísono", "todas las personas cantan o tocan la misma melodía a la misma altura"), ("voz principal", "la que lleva la melodía más importante"), ("acompañamiento", "voces o instrumentos que apoyan sin tapar la melodía"), ("armonía", "varios sonidos que suenan a la vez"), ("cuerda de voces", "grupo de voces del mismo tipo: sopranos, contraltos, tenores o bajos")],
    [
        ("Contar voces", f"{CORO}. ¿Cuántos bajos hay en el coro?", ["El coro tiene 20 personas.", "20 − (8 + 5 + 4) = 3."], "3 bajos"),
        ("Reconocer un rol", f"{CORO}. ¿Qué rol cumple la guitarra en la pieza?", ["La guitarra marca el pulso.", "No lleva la melodía principal."], "Acompaña marcando el pulso"),
    ],
    [
        ("Cantar más fuerte que las demás voces para lucirse.", "Si tapa la voz principal, se pierde la melodía y el grupo suena confuso.", "Baja el volumen cuando tu parte es de acompañamiento."),
        ("Ensayar solo la propia parte y nunca oír a las demás.", "La música de grupo exige escuchar para empezar y terminar juntas.", "Escucha las otras voces mientras cantas."),
    ],
    [
        ex(f"{CORO}. ¿Cuántas sopranos hay?", "8", "Así lo indican los datos del coro."),
        ex("Todas las personas del grupo cantan la misma melodía a la misma altura. ¿Cómo se llama eso?", "Unísono", "Eso es cantar al unísono."),
        ex(f"{CORO}. ¿Qué voz canta la melodía principal?", "La voz 1", "Los datos indican que la voz 1 lleva la melodía principal."),
    ],
    [
        ex("¿Qué debe hacer una voz de acompañamiento cuando suena la voz principal? A) Apoyar sin taparla. B) Cantar lo más fuerte posible.", "A", "El acompañamiento sirve a la melodía, no compite con ella."),
        ex("De las voces humanas, ¿cuál es la más grave? A) Bajo. B) Soprano.", "A", "El orden de aguda a grave es soprano, contralto, tenor y bajo."),
        ex("Un grupo suena confuso porque nadie baja el volumen. ¿Qué mejora más su claridad? A) Que las voces de acompañamiento bajen el volumen cuando entra la principal. B) Que todas canten con mayor fuerza.", "A", "Equilibrar volúmenes deja oír la melodía."),
    ],
    [
        arith(f"{CORO}. ¿Cuántas personas cantan voces más agudas que las de los tenores (sopranos y contraltos)?", "8+5", "Se suman las sopranos y las contraltos.", " personas"),
        ex(f"{CORO}. Si la pieza se canta al unísono, ¿cuántas melodías distintas suenan al mismo tiempo en el coro?", "1", "Al unísono todas cantan la misma melodía."),
        ex("En un ensayo, la persona que dirige hace una señal de entrada para que todas las voces empiecen juntas. ¿Qué valor del trabajo en grupo practican? A) Comunicación y escucha. B) Competencia por sonar más fuerte.", "A", "Entrar juntas exige mirarse y escucharse."),
    ],
    [
        ex(f"{CORO}. Una estudiante dice que, si todas las voces cantan fuerte, la pieza suena más expresiva. ¿Qué argumento lo contradice? A) Que la voz principal quedaría tapada y la melodía se perdería. B) Que en un coro de 20 personas una voz fuerte siempre se oye mejor.", "A", "Expresividad también es equilibrio, no solo volumen."),
        arith(f"{CORO}. Si 3 contraltos y 2 bajos faltan al ensayo, ¿cuántas personas quedan en el coro?", "20-3-2", "Se restan las personas que faltan del total.", " personas"),
    ],
    [
        arith(f"{CORO}. ¿Cuántas personas cantan las voces más graves del coro (tenores y bajos)?", "4+3", "Hay 4 tenores y 3 bajos (20 − 8 − 5 − 4).", " personas"),
        ex("Dos guitarristas deben tocar juntos una pieza. Uno toca la melodía y el otro la armonía. Para que la melodía se oiga, ¿quién baja el volumen? A) El que toca la armonía. B) El que toca la melodía.", "A", "La armonía acompaña y no debe tapar la melodía."),
    ],
    [ex(f"{CORO}. Estás en la cuerda de los tenores. ¿Con qué grupo tienes más cosas en común para ensayar tu parte? A) Con los otros 3 tenores. B) Con las 8 sopranos.", "A", "Una cuerda comparte la misma parte; los tenores son 4 en total y tú eres uno.")],
    [ex("¿Qué voz humana es la más aguda?", "La soprano", "El orden de aguda a grave empieza por soprano."), ex("¿Qué hace la voz de acompañamiento?", "Apoya sin tapar la melodía", "Equilibra el sonido del grupo."), ex("¿Cómo se llama cantar la misma melodía a la misma altura?", "Unísono", "Todas las personas cantan igual.")],
    (
        "Imagina que formas parte de un grupo de 6 personas que canta una canción de ejemplo con estas partes: 2 personas cantan la voz principal, 2 cantan una voz de acompañamiento más grave y 2 marcan el pulso con palmas suaves. Escribe: a) cuántas personas hay en cada rol, b) qué volumen usa cada rol, c) una señal para empezar todos juntos, d) una frase sobre cómo escucharías a las demás.",
        "a) 2, 2 y 2. b) La principal, volumen medio; el acompañamiento, más suave; las palmas, suaves y regulares. c) La persona que dirige levanta la mano y todas respiran juntas. d) Escucharía la voz principal para no taparla.",
        ["asigna volumen según el rol", "incluye una señal de entrada", "dice cómo escucha a las demás"],
        ["cuatro partes a) a d)", "volumen por rol"],
        ["cantar más fuerte para lucirse", "no escuchar a las demás"],
        "Reconoce el plan y pide explicar qué cambiaría si una de las voces de acompañamiento faltara.",
    ),
    "Canta una melodía conocida y pide a otra persona que marque el pulso suavemente; anota si el grupo sonó claro.",
    "Escribe qué rol te gustaría cumplir en un grupo y qué necesitarías practicar.",
)

# ---------------------------------------------------------------- OA 03 · clase 3 (ensayar con laboriosidad y compromiso)
PLAN = ("Plan de ejemplo de un ensayo de 30 minutos: 5 minutos de calentamiento; 20 minutos para la pieza dividida en 4 frases, con el mismo tiempo para cada frase; "
        "5 minutos para unir todas las frases y anotar qué mejorar")
L(
    OA3, 3,
    f"Lápiz y papel; tu voz o un instrumento, si lo tienes. Plan de ejemplo, que se repite en los ejercicios: {PLAN}.",
    "Aprenderé a planificar un ensayo con laboriosidad y compromiso: dividir la pieza en frases, subir el tempo por etapas, repetir con atención y registrar avances. Sirve para mejorar de manera constante y cumplir con el grupo.",
    ["Sé reconocer el estilo de una pieza.", "Sé identificar mi voz o mi parte en un grupo.", "Sé que el tempo se mide en pulsos por minuto."],
    [
        "Un buen ensayo no es repetir toda la pieza sin pensar, sino trabajar con un plan. Primero se calienta la voz o las manos. Luego se divide la pieza en frases y se trabaja una por una, sobre todo las difíciles. Se empieza lento, con un tempo en que se pueda tocar o cantar sin errores, y se sube de a poco, por ejemplo de 10 en 10 pulsos por minuto, solo cuando la frase sale bien varias veces seguidas.",
        "La laboriosidad es el esfuerzo constante y atento que se pone en una tarea: practicar un poco cada día vale más que hacerlo todo la noche anterior. El compromiso es cumplir lo que se acordó con el grupo: llegar a tiempo, saber la parte y avisar si no se puede asistir. Registrar cada ensayo en una libreta (qué frase, qué tempo, qué error y cómo se corrigió) ayuda a ver los avances.",
        "Cuando algo sale mal, se vuelve a la frase corta, se baja el tempo y se repite con atención. Equivocarse es parte del aprendizaje. También se cuida el cuerpo: pausas breves, agua y postura cómoda. Un ensayo corto y bien planificado rinde más que uno largo y desordenado. Al terminar, conviene decidir cuál será el siguiente paso, con una meta concreta.",
    ],
    [("laboriosidad", "esfuerzo constante y atento en una tarea"), ("compromiso", "cumplir lo que se acordó con el grupo"), ("calentamiento", "preparación breve del cuerpo o de la voz antes de ensayar"), ("frase", "parte corta de una pieza que se ensaya por separado"), ("meta", "objetivo concreto que se quiere lograr")],
    [
        ("Repartir el tiempo", f"{PLAN}. ¿Cuántos minutos se dedican a cada frase?", ["Se dedican 20 minutos a 4 frases iguales.", "20 ÷ 4 = 5."], "5 minutos"),
        ("Subir el tempo por etapas", "Una frase sale bien a 60 pulsos por minuto y se quiere llegar a 90, subiendo de 10 en 10. ¿Cuántas etapas hay?", ["Los tempos son 70, 80 y 90.", "Son 3 etapas."], "3 etapas"),
    ],
    [
        ("Repetir la pieza entera sin parar cuando hay un error.", "El error se repite y se aprende mal; conviene aislar la frase difícil.", "Aísla la frase, baja el tempo y repite con atención."),
        ("Practicar solo la noche antes.", "Un esfuerzo constante rinde más que uno concentrado en un solo día.", "Practica poco, pero cada día."),
    ],
    [
        ex(f"{PLAN}. ¿Cuántos minutos del ensayo se dedican a trabajar con la pieza completa unida, no por frases?", "5", "Solo los 5 minutos finales unen todas las frases."),
        ex(f"{PLAN}. ¿Para qué sirven los 5 minutos finales?", "Para unir las frases y anotar qué mejorar", "Así lo dice el plan."),
        ex("¿Cuál acción cumple un compromiso con el grupo? A) Llegar a tiempo al ensayo sabiendo mi parte. B) Llegar tarde y pedir que repitan todo para mí.", "A", "El compromiso es cumplir lo que se acordó con el grupo."),
    ],
    [
        ex("Una frase sale con errores a 100 pulsos por minuto. ¿Qué conviene hacer? A) Bajar el tempo y repetirla con atención. B) Subir el tempo para que los errores pasen más rápido.", "A", "Con un tempo cómodo se aprende bien la frase y luego se sube."),
        ex("¿Qué rinde más? A) Practicar 15 minutos cada día. B) Practicar 105 minutos la noche anterior.", "A", "La práctica constante da un aprendizaje más firme y menos cansancio."),
        ex("¿Cuándo se sube el tempo? A) Cuando la frase sale bien varias veces seguidas. B) Cuando ya pasaron 5 minutos.", "A", "Subir sin dominar la frase repite errores."),
    ],
    [
        arith(f"{PLAN}. El ensayo se repite 4 veces por semana. ¿Cuántos minutos de ensayo hay en la semana?", "30*4", "Se multiplica la duración de un ensayo por las veces que se repite.", " minutos"),
        ex("Una frase se trabaja con estos tempos, uno tras otro: 60, 70, 80 y 90 pulsos por minuto. Si cada etapa dura 2 minutos, ¿cuántos minutos se necesitan?", "8", "Son 4 etapas de 2 minutos cada una."),
        ex("Una libreta de ensayo anota: «frase 2, 70 por minuto, error en el tercer compás, lo corregí tocando solo ese compás tres veces». ¿Qué tres datos registró? A) Frase, tempo y error corregido. B) Nombre, curso y fecha.", "A", "Registra qué frase, qué tempo y cómo corrigió."),
    ],
    [
        ex("Mateo practicó 10 minutos cada día durante 6 días, y Sofía practicó 50 minutos solo el séptimo día. ¿Quién practicó más tiempo en total?", "Mateo", "Mateo hizo 10 × 6 = 60 minutos y Sofía 50, y además la práctica repartida suele rendir más."),
        arith("Un grupo de 5 personas promete llegar a tiempo a 6 ensayos. ¿Cuántas llegadas a tiempo deben cumplirse en total?", "5*6", "Cada persona cumple 6 llegadas.", " llegadas"),
    ],
    [
        ex("Una frase difícil de 8 compases se practica 3 veces por etapa en 4 etapas de tempo. ¿Cuántas veces se repite en total?", "12", "Son 3 repeticiones por 4 etapas."),
        arith("Para llegar de 60 a 120 pulsos por minuto subiendo de 20 en 20, ¿cuántas etapas de subida hay?", "(120-60)//20", "Se divide la diferencia entre el tamaño de cada subida.", " etapas"),
    ],
    [ex(f"{PLAN}. Un integrante avisa que no puede asistir al ensayo y envía su parte grabada al grupo, que lo había acordado. ¿Qué compromiso cumple? A) Avisar con anticipación y aportar su parte. B) Faltar sin avisar.", "A", "Avisar y colaborar es parte de cumplir con el grupo.")],
    [ex("Otro plan de ejemplo dura 40 minutos: 5 de calentamiento, 30 para 5 frases con el mismo tiempo cada una y 5 de unión final. ¿Cuántos minutos se dedican a cada frase?", "6", "Se dividen los 30 minutos entre las 5 frases."), ex("Una frase sale mal dentro de la pieza completa. ¿Qué conviene: ensayarla aislada y más lenta, o repetir toda la pieza sin parar?", "Aislada y más lenta", "Así se corrige el error sin repetirlo."), ex("¿Qué es una meta de ensayo?", "Un objetivo concreto que se quiere lograr", "Orienta el siguiente ensayo.")],
    (
        "Planifica un ensayo de 30 minutos para esta pieza de ejemplo: «una canción de 3 frases, cada frase de 4 compases». Escribe: a) el reparto de minutos (calentamiento, cada frase, unión final), b) el tempo con que empiezas y los pasos de subida (por ejemplo, de 60 a 80), c) una meta para el siguiente ensayo, d) un compromiso que cumplirás con el grupo.",
        "a) 5 minutos de calentamiento, 6 minutos para cada una de las 3 frases (18), 7 minutos para unir y anotar. b) Empiezo a 60 y subo a 70 y 80 cuando la frase sale bien tres veces seguidas. c) Cantar la frase 2 sin errores a 80. d) Llegar a tiempo y saber mi parte.",
        ["el reparto suma exactamente 30 minutos", "usa tempos con pasos concretos", "incluye meta y compromiso"],
        ["plan con cuatro partes a) a d)", "suma de minutos correcta"],
        ["repartos que no suman 30", "metas poco concretas"],
        "Reconoce el plan y pide ajustar la distribución si la frase 3 resulta más difícil que las otras.",
    ),
    "Practica una frase corta de una canción tres veces, cada vez un poco más rápido, y anota qué mejoró.",
    "Escribe una meta de ensayo de una semana con tres pasos y una fecha para revisarla.",
)

# ---------------------------------------------------------------- OA 03 · clase 4 (interpretar transmitiendo el propósito expresivo)
PAUTA = ("Pauta de ejemplo (cada criterio vale de 0 a 2 puntos): 1) pulso estable; 2) entrada en el momento justo; 3) estilo respetado (articulación y volumen); "
         "4) expresividad: transmite el propósito de la pieza; 5) compromiso: ensayó según el plan")
L(
    OA3, 4,
    f"Lápiz y papel; tu voz o un instrumento, si lo tienes. Pauta de ejemplo, que se repite en los ejercicios: {PAUTA}.",
    "Aprenderé a interpretar una pieza transmitiendo su propósito expresivo y a evaluar mi interpretación con una pauta de criterios observables. Sirve para mejorar con evidencia y no con impresiones sobre mí mismo o mi grupo.",
    ["Sé reconocer el estilo de una pieza.", "Sé cuál es mi rol en un grupo.", "Sé planificar un ensayo."],
    [
        "Interpretar es hacer sonar una música para que comunique algo. La interpretación expresiva transmite el propósito de la pieza: calma en un arrullo, energía en una marcha, solemnidad en un homenaje. Para lograrlo hay que decidir el tempo, la dinámica y el fraseo, y mantenerlos mientras se canta o toca. La expresividad se oye en los cambios de volumen, en las respiraciones entre frases y en la forma de comenzar y terminar.",
        "Para evaluar una interpretación se usa una pauta con criterios observables, es decir, cosas que se pueden oír o ver: pulso estable, entrada justa, estilo respetado, expresividad y compromiso. Cada criterio se puntúa y se anota la evidencia. Por ejemplo: «Pulso estable: 1 punto, porque aceleré en la segunda frase». Evaluar la interpretación no es evaluar a la persona: se habla de lo que sonó, no de cómo es quien lo interpretó.",
        "Si durante una presentación aparece un error, se sigue adelante con calma, sin detener al grupo, y se corrige después. Los nervios son normales: respirar hondo, mirar el comienzo de la pieza y recordar el plan ayuda. Si los nervios son muy fuertes o duran mucho, conviene contárselo a una persona adulta de confianza. Luego de presentar, se revisa la pauta y se decide una mejora concreta para la próxima vez.",
    ],
    [("interpretación", "hacer sonar una música para que comunique algo"), ("expresividad", "forma en que la interpretación transmite el propósito de la pieza"), ("criterio", "aspecto observable que se evalúa en una pauta"), ("evidencia", "dato que se oye o se ve y que justifica un puntaje"), ("pulso estable", "pulso que no se acelera ni se frena sin querer")],
    [
        ("Sumar la pauta", f"{PAUTA}. Un grupo obtuvo 2, 1, 2, 1 y 2 puntos en los cinco criterios. ¿Cuántos puntos sumó de un máximo de 10?", ["Se suman los cinco puntajes.", "2 + 1 + 2 + 1 + 2 = 8."], "8 de 10"),
        ("Justificar un puntaje", "Un grupo se equivocó en una nota de la tercera frase pero siguió sin detenerse y el pulso se mantuvo. ¿Qué evidencia sostiene un buen puntaje en pulso estable?", ["Un error de nota no rompe el pulso.", "El grupo siguió sin acelerar ni frenar."], "Que el pulso se mantuvo aunque hubo un error de nota"),
    ],
    [
        ("Evaluar a la persona en lugar de la interpretación.", "La pauta evalúa lo que sonó, no cómo es quien interpreta.", "Escribe la evidencia audible, sin juicios sobre la persona."),
        ("Detener todo el grupo por un error pequeño.", "Seguir con calma mantiene el pulso y el propósito; el error se corrige después.", "Continúa y anota el error para el próximo ensayo."),
    ],
    [
        ex(f"{PAUTA}. ¿Cuántos criterios tiene la pauta?", "5", "Están numerados del 1 al 5."),
        ex(f"{PAUTA}. ¿Qué criterio revisa si el grupo ensayó según su plan?", "Compromiso", "El criterio 5 trata del ensayo según el plan."),
        ex("Una persona se equivoca en una nota durante una presentación. ¿Qué hace el grupo: sigue con calma o se detiene a empezar de nuevo?", "Sigue con calma", "Seguir mantiene el pulso y el propósito de la pieza."),
    ],
    [
        ex("¿Qué es una evidencia en una pauta? A) Un dato que se oye o se ve y que justifica el puntaje. B) Una opinión sobre la persona.", "A", "La evidencia permite comprobar el puntaje."),
        ex(f"{PAUTA}. Un grupo cantó una balada con notas cortas y voz fuerte. ¿Qué criterio baja? A) Estilo respetado. B) Entrada en el momento justo.", "A", "La articulación y la voz no corresponden al estilo."),
        ex("Si los nervios antes de presentar son muy fuertes y duran mucho, ¿qué conviene hacer? A) Contárselo a una persona adulta de confianza. B) Esconderlo y no decir nada.", "A", "Contarlo ayuda a recibir apoyo."),
    ],
    [
        arith(f"{PAUTA}. Un grupo obtuvo 1, 2, 1, 1 y 2 puntos en los cinco criterios. ¿Cuántos puntos le faltaron para el máximo de 10?", "10-(1+2+1+1+2)", "Se suman los puntos obtenidos y se restan del máximo.", " puntos"),
        ex(f"{PAUTA}. Un grupo sacó 0 en «entrada en el momento justo» porque entraron tarde. ¿Qué mejora concreta propone la evidencia? A) Acordar una señal de entrada y respirar juntos. B) Cantar más fuerte.", "A", "Un problema de entrada se mejora con una señal y respiración común."),
        ex("Dos comentarios sobre una presentación. A) «Aceleramos en la segunda frase: de 90 a 110 por minuto.» B) «Nos salió horrible.» ¿Cuál es evidencia observable?", "A", "Da un dato que se oyó y se puede comprobar."),
    ],
    [
        arith(f"{PAUTA}. Un grupo sacó 5 puntos de 10 en su primera presentación y 8 puntos de 10 en la segunda. ¿Cuántos puntos subió?", "8-5", "Se restan los puntos de la primera presentación a los de la segunda.", " puntos"),
        ex("Una compañera dice «yo sé que nunca voy a cantar bien». ¿Qué respuesta ayuda más? A) Mirar la pauta, elegir un criterio con evidencia y proponer una mejora concreta. B) Decirle que algunas personas no tienen talento para la música.", "A", "La pauta convierte la impresión en pasos concretos."),
    ],
    [
        arith("Un grupo presenta 3 piezas de 4 minutos cada una, con 1 minuto de pausa entre piezas. ¿Cuántos minutos dura la presentación?", "3*4+2*1", "Hay tres piezas y dos pausas entre ellas.", " minutos"),
        ex("Un grupo debe interpretar un arrullo de ejemplo con propósito de calmar. Tiene tres opciones: 60 pulsos por minuto y suave, 100 y fuerte, o 60 y fuerte. ¿Cuál transmite mejor el propósito?", "60 pulsos por minuto y suave", "Lento y suave calma; las otras opciones agregan energía."),
    ],
    [ex(f"{PAUTA}. Antes de la presentación, el grupo marca el pulso con una palma suave durante 4 pulsos. ¿Qué criterio ayuda a cumplir? A) Entrada en el momento justo. B) Compromiso.", "A", "Contar juntos marca el instante de empezar.")],
    [ex("¿Qué se evalúa en una pauta: la interpretación o a la persona?", "La interpretación", "Se habla de lo que sonó."), ex("¿Qué haces si hay un error mientras presentas?", "Sigo con calma", "Así se mantiene el pulso y el propósito."), ex("¿Qué se decide al terminar la pauta?", "Una mejora concreta para la próxima vez", "La evaluación sirve para mejorar.")],
    (
        "Usa la pauta de ejemplo para evaluar esta presentación imaginaria: un trío cantó una balada de 66 pulsos por minuto; el pulso se mantuvo estable; entraron juntos; usaron notas cortas y voz fuerte (el estilo pedía notas unidas y voz suave); transmitieron poca calma y ensayaron siguiendo su plan. Escribe: a) un puntaje de 0 a 2 para cada criterio, con una evidencia, b) el total sobre 10, c) una mejora concreta para el próximo ensayo.",
        "Pulso 2 (se mantuvo estable). Entrada 2 (entraron juntos). Estilo 0 (notas cortas y voz fuerte en una balada). Expresividad 1 (poca calma). Compromiso 2 (siguió su plan). Total 7 de 10. Mejora: cantar con notas unidas y voz suave, a 66 pulsos por minuto.",
        ["usa los cinco criterios de la pauta", "justifica cada puntaje con evidencia del enunciado", "propone una mejora concreta"],
        ["pauta con cinco puntajes", "total y mejora"],
        ["evaluar a las personas", "puntajes sin evidencia"],
        "Reconoce la pauta y pide explicar por qué otro puntaje no sería razonable.",
    ),
    "Canta una frase conocida con el propósito de calmar y luego con el propósito de animar; anota qué cambiaste.",
    "Evalúa con la pauta de ejemplo una interpretación tuya (aunque sea tarareada) y propone una mejora.",
)
