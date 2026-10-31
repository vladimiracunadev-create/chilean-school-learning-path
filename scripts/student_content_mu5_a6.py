"""Student material for 5.º básico Música, OA 06 (presentación responsable, dominada y musical) y OA 07 (relación entre las obras y su contexto).

Todos los casos, regiones y obras son ficticios e inventados para esta clase; las obras reales y su contexto los selecciona el docente.
Compartir experiencias personales o familiares es siempre opcional.
"""
from __future__ import annotations

from student_content_mu5_a import L
from student_lessons import arith, ex

OA6, OA7 = "MU05 OA 06", "MU05 OA 07"

# ---------------------------------------------------------------- OA 06 · clase 1 (preparar con responsabilidad)
ROLES = ("presentador o presentadora (saluda y explica en pocas palabras), intérpretes (cantan o tocan), "
         "responsable de la señal (cuenta 4 pulsos para empezar) y apoyo de materiales (prepara y guarda los instrumentos)")
PROG = [("Canon de bienvenida", 3), ("Ritmo con palmas", 4), ("Canción en dúo", 2), ("Melodía en metalófono", 5), ("Ronda final", 3)]
PROG_TXT = ", ".join(f"{i}) {t} ({m} minutos)" for i, (t, m) in enumerate(PROG, 1))
PROG_SUM = sum(m for _t, m in PROG)
CAMBIO = 1
PROG_TOT = PROG_SUM + CAMBIO * (len(PROG) - 1)

L(
    OA6, 1,
    f"Lápiz y papel. Roles de una presentación: {ROLES}. Programa de ejemplo (inventado): {PROG_TXT}. Entre un número y el siguiente se usa {CAMBIO} minuto para cambiar de lugar.",
    "Aprenderé a preparar una presentación musical con responsabilidad: repartir roles, calcular el tiempo y revisar los materiales. Sirve para que el trabajo salga ordenado y respetando a quienes escuchan.",
    ["Sé tocar o cantar una pieza breve en grupo.", "Sé sumar minutos.", "Sé escuchar con respeto."],
    [
        "Presentar un trabajo musical al curso o a la comunidad requiere responsabilidad. Primero, se reparten los roles para que cada persona sepa qué hacer: " + ROLES + ". Tener un rol hace que todos participen y que nadie quede sin saber qué hacer.",
        f"Segundo, se organiza el tiempo. Un programa es la lista de números en el orden en que se presentarán, con su duración. El de la clase: {PROG_TXT}. Los números suman {PROG_SUM} minutos y, con {CAMBIO} minuto de cambio entre cada número (son {len(PROG) - 1} cambios), la presentación dura {PROG_TOT} minutos. Conviene calcular también la hora de término para no pasarse del tiempo disponible.",
        "Tercero, se revisan los materiales y el lugar: instrumentos limpios y en buen estado, un volumen cómodo para el lugar, sillas ordenadas y un camino despejado para no tropezar. Se guarda lo que no se usa. Y cuando alguien presenta, el público escucha en silencio y aplaude al final. La responsabilidad también es cuidar a las demás personas.",
    ],
    [("presentación", "momento en que se muestra un trabajo musical a otras personas"), ("programa", "lista de números en orden, con su duración"), ("rol", "tarea que cumple cada persona"), ("ensayo general", "ensayo completo antes de presentar"), ("público", "personas que escuchan")],
    [
        ("Calcular la duración", f"Programa: {PROG_TXT}. Entre un número y el siguiente hay {CAMBIO} minuto de cambio. ¿Cuánto dura en total?", [f"Suma de los números: {' + '.join(str(m) for _t, m in PROG)} = {PROG_SUM}.", f"Hay {len(PROG) - 1} cambios de {CAMBIO} minuto: {len(PROG) - 1}.", f"{PROG_SUM} + {len(PROG) - 1} = {PROG_TOT}."], f"{PROG_TOT} minutos"),
        ("Asignar un rol", "Una estudiante prepara y guarda los instrumentos antes y después de la presentación. ¿Qué rol cumple?", ["Revisa la lista de roles de la clase.", "Preparar y guardar materiales es el apoyo de materiales."], "Apoyo de materiales"),
    ],
    [
        ("Dejar todos los roles para el último momento.", "Se pierde tiempo y alguien queda sin tarea.", "Reparte los roles en el primer ensayo."),
        ("Calcular el tiempo sin contar los cambios entre números.", "Los cambios también ocupan tiempo.", "Suma los números y los minutos de cambio."),
    ],
    [
        ex("¿Qué hace la persona responsable de la señal?", "Cuenta 4 pulsos para empezar", "Marca el inicio para que todos entren juntos."),
        ex(f"Programa: {PROG_TXT}. ¿Cuánto dura el número 4?", "5 minutos", "El número 4 dura 5 minutos."),
        ex("Mientras alguien presenta, ¿el público conversa o escucha en silencio?", "Escucha en silencio", "Escuchar con respeto es parte de la presentación."),
    ],
    [
        ex(f"Programa: {PROG_TXT}. ¿Cuántos números tiene el programa?", str(len(PROG)), "Se cuentan los cinco números."),
        ex(f"Programa: {PROG_TXT}. ¿Cuántos cambios de lugar hay entre los números?", str(len(PROG) - 1), "Hay un cambio entre cada par de números seguidos."),
        ex("¿Qué debe hacer el apoyo de materiales después de la presentación?", "Guardar los instrumentos", "Su rol incluye preparar y guardar."),
    ],
    [
        arith(f"Programa: {PROG_TXT}. ¿Cuántos minutos suman solo los números, sin contar los cambios?", "+".join(str(m) for _t, m in PROG), "Se suman las duraciones de los cinco números.", " minutos"),
        arith(f"Programa: {PROG_TXT}. Si la presentación empieza a las 10:00 (es decir, en el minuto 0), ¿cuántos minutos después de las 10:00 termina?", f"{PROG_SUM}+{CAMBIO}*{len(PROG) - 1}", "Se suman los números y los cuatro cambios.", " minutos"),
        ex("Un curso tiene 15 minutos disponibles. Su programa dura 21 minutos. ¿Cuántos minutos debe recortar?", "6", "21 menos 15 son 6 minutos."),
    ],
    [
        ex("Un grupo dice que no necesita ensayo general porque ya practicaron cada número por separado. ¿Qué problema puede tener?", "Pueden fallar los cambios y las entradas entre números", "El ensayo general permite ensayar el programa completo."),
        ex("Para una presentación en un patio muy abierto, ¿qué ajustas: (a) un volumen cómodo y que todos oigan o (b) tocar lo más fuerte posible?", "(a)", "El volumen debe servir al público sin dañar el oído."),
    ],
    [
        arith("Un curso de 24 estudiantes se reparte en 4 grupos iguales para presentar. ¿Cuántos estudiantes tiene cada grupo?", "24//4", "Se reparten en partes iguales.", " estudiantes"),
        arith("Cada uno de los 4 grupos presenta 5 minutos y hay 1 minuto de cambio entre grupos. ¿Cuántos minutos dura todo?", "4*5+1*3", "Hay 4 presentaciones de 5 minutos y 3 cambios entre ellas.", " minutos"),
    ],
    [ex("Un grupo acaba de terminar su número y deja los instrumentos tirados. ¿Qué rol debería haber cuidado esto?", "El apoyo de materiales", "Su tarea incluye guardar los instrumentos.")],
    [ex("¿Qué es un programa?", "La lista de números en orden con su duración", "Organiza el tiempo."), ex("¿Qué rol cuenta 4 pulsos?", "El responsable de la señal", "Marca el inicio."), ex("¿Qué hace el público al escuchar?", "Escucha en silencio y aplaude al final", "Es parte de la presentación.")],
    (
        "Prepara un programa de tres números para presentar a tu curso o a un grupo que tú elijas. Puedes usar piezas que ya conozcas, como una ronda, un ritmo con palmas y una canción corta. Escribe el título y la duración de cada número, calcula el tiempo total (con 1 minuto de cambio entre números), reparte los cuatro roles entre tú y quienes participen y escribe qué revisarás antes de empezar.",
        "Programa: 1) Ronda (3 min). 2) Ritmo con palmas (2 min). 3) Canción corta (4 min). Total: 3 + 2 + 4 + 2 cambios = 11 minutos. Roles: presentador, intérpretes, responsable de la señal y apoyo de materiales. Reviso: instrumentos, volumen y espacio.",
        ["tres números con duración", "tiempo total bien calculado con los cambios", "cuatro roles repartidos", "lista de lo que revisará"],
        ["programa escrito", "cálculo"],
        ["no contar los cambios", "dejar un rol sin asignar"],
        "Reconoce el programa y pide mostrar el cálculo del tiempo total; recuerda que compartir la presentación con familia es opcional.",
    ),
    "Escribe el nombre de los cuatro roles de una presentación.",
    "Calcula la hora de término de un programa de 18 minutos que parte a las 10:05.",
)

# ---------------------------------------------------------------- OA 06 · clase 2 (dominio: ensayar con método)
ENS = [("A", 5, 4), ("B", 5, 2), ("C", 4, 4)]
ENS_TXT = " ".join(f"Sección {s}: {i} intentos, {b} sin errores." for s, i, b in ENS)
ENS_ERR = {s: i - b for s, i, b in ENS}
ENS_MAX = max(ENS_ERR, key=ENS_ERR.get)

L(
    OA6, 2,
    f"Lápiz y papel, y tu pieza breve para ensayar (cantada o con instrumento a volumen bajo). Registro de ensayo de ejemplo: {ENS_TXT}",
    "Aprenderé a ensayar con método para dominar mi parte: practicar por partes, bajar el tempo cuando algo falla y llevar un registro de intentos. Sirve para tocar o cantar con seguridad ante el público.",
    ["Sé mantener un pulso parejo.", "Sé leer mi parte.", "Sé qué es un compás."],
    [
        "Dominar una pieza es tocarla o cantarla con seguridad, a tiempo y sin detenerse. No se logra repitiendo todo de principio a fin una y otra vez. Un método eficaz tiene tres pasos: dividir la pieza en secciones, practicar más las secciones que fallan y volver a unirlas. Si una parte sale mal, baja el tempo, hasta que salga bien, y recién después súbelo.",
        f"Un registro de ensayo ayuda a decidir qué practicar. Anota cuántos intentos hiciste de cada sección y cuántos salieron sin errores. En el ejemplo: {ENS_TXT} Los errores son los intentos que no salieron bien: en A hubo {ENS_ERR['A']}, en B hubo {ENS_ERR['B']} y en C hubo {ENS_ERR['C']}. La sección con más errores es la {ENS_MAX}, así que ahí conviene practicar más.",
        "Durante la presentación, si te equivocas, no te detengas ni pongas cara de enojo: mantén el pulso y sigue con la parte que viene. El público casi nunca nota un error pequeño si continúas con seguridad. Y antes de empezar, respira profundo para calmar los nervios y mira el punto de entrada de tu parte.",
    ],
    [("dominio", "tocar o cantar con seguridad y sin detenerse"), ("ensayo por partes", "practicar secciones cortas por separado"), ("registro de ensayo", "anotación de intentos y errores"), ("tempo lento", "ir más despacio para corregir"), ("entrada", "momento en que empieza mi parte")],
    [
        ("Elegir qué practicar", f"{ENS_TXT} ¿En qué sección conviene practicar más y por qué?", [f"Errores en A: {ENS_ERR['A']}.", f"Errores en B: {ENS_ERR['B']}.", f"Errores en C: {ENS_ERR['C']}.", "B tiene más errores."], "En la B, porque tuvo más intentos con errores"),
        ("Corregir un error", "Un niño falla siempre en el compás 6 al tempo normal. ¿Qué debe hacer: (a) bajar el tempo en ese compás hasta que salga bien o (b) tocar todo más rápido?", ["Primero hay que lograr que salga bien.", "Para lograrlo se baja el tempo."], "(a)"),
    ],
    [
        ("Repetir toda la pieza completa sin practicar lo que falla.", "Gastas tiempo en lo que ya sabes y no corriges lo difícil.", "Practica por partes las secciones con errores."),
        ("Detenerse y enojarse al equivocarse en la presentación.", "El público nota más la detención que el error.", "Mantén el pulso y sigue con la parte que viene."),
    ],
    [
        ex(f"{ENS_TXT} ¿Cuántos intentos con errores hubo en la sección A?", str(ENS_ERR["A"]), "5 intentos menos 4 sin errores es 1."),
        ex("Si te equivocas durante la presentación, ¿qué haces: (a) sigues con el pulso o (b) te detienes y empiezas de nuevo?", "(a)", "Mantener el pulso evita cortar la música."),
        ex("Al ensayar una parte difícil, ¿bajas o subes el tempo?", "Bajo el tempo", "A un tempo lento puedes corregir con calma."),
    ],
    [
        ex(f"{ENS_TXT} ¿Cuántos intentos con errores hubo en la sección B?", str(ENS_ERR["B"]), "5 intentos menos 2 sin errores es 3."),
        ex(f"{ENS_TXT} ¿En qué sección hubo menos errores: A o C?", "C", "En C no hubo errores y en A hubo uno."),
        ex("¿Cuál es el primer paso del método de ensayo de la clase?", "Dividir la pieza en secciones", "Los otros pasos son practicar las que fallan y unirlas."),
    ],
    [
        arith(f"{ENS_TXT} ¿Cuántos intentos con errores hubo en total?", "(5-4)+(5-2)+(4-4)", "Se restan los intentos sin errores de los intentos de cada sección y se suman.", " intentos"),
        arith(f"{ENS_TXT} ¿Cuántos intentos se hicieron en total?", "5+5+4", "Se suman los intentos de las tres secciones.", " intentos"),
        ex("Un estudiante practica una sección de 4 compases a tempo lento y le sale sin errores 3 veces seguidas. ¿Qué hace ahora: (a) sube un poco el tempo o (b) la da por perdida?", "(a)", "Cuando sale bien, se sube el tempo de a poco."),
    ],
    [
        ex("Luis dice que para dominar una pieza basta con repetirla completa muchas veces. ¿Qué paso del método de la clase omite?", "Practicar por partes las secciones que fallan", "El método pide dividir, practicar lo difícil y unir."),
        ex("Ana tuvo 3 intentos con errores de 5 en la sección B y 1 intento con errores de 5 en la sección A. ¿Es acertado dedicar más ensayo a la sección A?", "No", "B tiene más errores."),
    ],
    [
        arith("Un estudiante ensaya 4 días a la semana, 15 minutos cada día. ¿Cuántos minutos ensaya en una semana?", "4*15", "Se multiplican los días por los minutos.", " minutos"),
        arith("Un grupo tiene 60 minutos de ensayo. Usa 25 en la sección más difícil y 15 en cada una de las otras dos. ¿Cuántos minutos le quedan para repasar todo junto?", "60-25-15-15", "Se restan los tres tiempos del total.", " minutos"),
    ],
    [ex("Durante una presentación, un niño se equivoca en una nota y sigue sin detenerse. ¿Qué acertó: mantener el pulso o corregir en voz alta?", "Mantener el pulso", "Así la música no se corta.")],
    [ex("¿Qué haces con una sección que falla?", "La practico por separado y más lento", "Es parte del método."), ex("¿Qué haces si te equivocas en la presentación?", "Sigo con el pulso", "No detengo la música."), ex("¿Qué anota un registro de ensayo?", "Intentos y errores", "Sirve para decidir qué practicar.")],
    (
        "Elige una pieza breve que sepas (una ronda o una canción corta) y divídela en tres secciones. Ensaya cada una 5 veces, primero a tempo lento. Anota cuántos intentos salieron sin errores en cada sección, calcula cuántos tuvieron errores y escribe a qué sección dedicarás más ensayo. Ensaya a volumen bajo y con descansos.",
        "Sección 1: 5 intentos, 4 sin errores. Sección 2: 5 intentos, 2 sin errores. Sección 3: 5 intentos, 5 sin errores. Más errores: sección 2 (3). Dedicaré más ensayo a la sección 2.",
        ["divide la pieza en tres secciones", "registra intentos y errores con números", "elige con datos qué sección practicar"],
        ["registro escrito", "ensayo"],
        ["ensayar todo sin separar", "elegir sin mirar los datos"],
        "Reconoce el registro y pide mostrar con el dedo la sección con más errores y cómo piensa corregirla.",
    ),
    "Anota cuántas veces ensayaste hoy una pieza y cuántas salió sin errores.",
    "Escribe un plan de ensayo de 10 minutos por día durante 5 días.",
)

# ---------------------------------------------------------------- OA 06 · clase 3 (musicalidad)
CRIT6 = ["mantiene el pulso parejo", "cambia la dinámica como pide la pieza", "termina las frases con calma", "cuida el volumen y el timbre", "transmite el carácter con la postura y el rostro"]
CRIT6_TXT = ", ".join(f"({i}) {c}" for i, c in enumerate(CRIT6, 1))
INT6 = {"X": {1, 2, 3, 5}, "Y": {1, 4}}

L(
    OA6, 3,
    f"Lápiz y papel; tu pieza breve para probar la expresión, a volumen bajo. Criterios de musicalidad de la clase: {CRIT6_TXT}. Interpretaciones de ejemplo: X cumple los criterios 1, 2, 3 y 5; Y cumple los criterios 1 y 4.",
    "Aprenderé qué es la musicalidad: tocar o cantar con expresión usando dinámica, frases y carácter, y no solo con las notas correctas. Sirve para que mi presentación comunique algo.",
    ["Sé usar p, f, crescendo y diminuendo.", "Sé qué es una frase musical.", "Sé mantener el pulso."],
    [
        "La musicalidad es la capacidad de interpretar la música con expresión. No basta con tocar las notas correctas: hay que decir algo con ellas. Una interpretación musical mantiene el pulso, cambia la dinámica como pide la pieza (por ejemplo, un crescendo se siente que crece), y termina cada frase con calma, como si respiraras al final.",
        f"Los criterios de la clase son: {CRIT6_TXT}. Cada criterio cumplido suma un punto. En el ejemplo, la interpretación X cumple 4 de 5 y la Y cumple 2 de 5. La interpretación X expresa más porque cuida el pulso, la dinámica, las frases y el carácter.",
        "El cuerpo también expresa. Si la música es tranquila, tu postura es relajada y tu rostro es sereno. Si es alegre, puedes sonreír y moverte con el pulso. Pero la expresión no es exagerar: no debe distraer ni molestar a quien escucha. Y cuida siempre el volumen: expresar no significa tocar más fuerte de lo cómodo.",
    ],
    [("musicalidad", "interpretar con expresión, más allá de tocar las notas"), ("frase", "grupo de sonidos que forma una idea musical"), ("carácter", "sentimiento que transmite la música"), ("expresión", "forma de mostrar el carácter con sonido y cuerpo"), ("criterio", "pregunta con que se revisa una interpretación")],
    [
        ("Contar criterios", f"Criterios: {CRIT6_TXT}. La interpretación Y cumple los criterios 1 y 4. ¿Cuántos cumple y cuáles le faltan?", ["Cumple 2 de 5.", "Le faltan el 2, el 3 y el 5."], "Cumple 2; le faltan el 2, el 3 y el 5"),
        ("Elegir la más expresiva", "Dos interpretaciones tocan las mismas notas. X varía la dinámica y termina las frases con calma. Y toca todo igual de fuerte. ¿Cuál es más musical?", ["La musicalidad pide expresión.", "X cambia la dinámica y cuida las frases."], "X"),
    ],
    [
        ("Pensar que tocar más fuerte es tocar con más expresión.", "La expresión usa contrastes, no solo volumen.", "Cambia la dinámica como pide la pieza."),
        ("Exagerar gestos que distraen.", "La expresión debe acompañar la música.", "Usa la postura y el rostro con naturalidad."),
    ],
    [
        ex("¿Qué es la musicalidad?", "Interpretar con expresión", "Va más allá de tocar las notas correctas."),
        ex("En una música tranquila, ¿tu postura es relajada o tensa?", "Relajada", "El cuerpo acompaña el carácter."),
        ex("¿Una interpretación musical mantiene el pulso parejo? Responde sí o no.", "Sí", "Mantener el pulso es el primer criterio."),
    ],
    [
        ex(f"Criterios: {CRIT6_TXT}. ¿Cuántos criterios cumple la interpretación X (criterios 1, 2, 3 y 5)?", str(len(INT6["X"])), "Son cuatro criterios."),
        ex(f"Criterios: {CRIT6_TXT}. ¿Cuál criterio trata de cuidar el volumen?", "El criterio 4", "Es «cuida el volumen y el timbre»."),
        ex("Un crescendo debe sentirse como un sonido que, ¿crece o baja poco a poco?", "Crece", "El crescendo sube la intensidad."),
    ],
    [
        ex("Una niña toca todas las notas correctas, pero siempre con la misma fuerza y sin pausas entre frases. ¿Qué criterios le faltan, según la clase?", "Cambiar la dinámica y terminar las frases con calma", "Toca sin contraste de dinámica y sin cerrar las frases."),
        ex("Un niño sonríe y se mueve mucho mientras toca una música muy tranquila. ¿Está transmitiendo su carácter?", "No", "El carácter tranquilo pide postura y rostro serenos."),
        arith("Una interpretación cumplía 2 criterios de musicalidad y, tras ensayar, cumple 5. ¿Cuántos criterios sumó?", "5-2", "Se resta lo que cumplía antes de lo que cumple ahora.", " criterios"),
    ],
    [
        ex("Luis dice que una interpretación es mejor que otra solo porque suena más fuerte. ¿Qué responderías con los criterios de la clase?", "Que el volumen alto no es expresión: hay que revisar los cinco criterios", "El volumen alto no mide musicalidad."),
        ex("En el criterio 3, ¿qué significa terminar las frases con calma?", "Cerrar la frase sin apuro, como cuando respiras", "Las frases se sienten completas."),
    ],
    [
        arith("En un curso de 28 estudiantes, 7 cumplieron 2 criterios, 11 cumplieron 3 y el resto cumplió 4. ¿Cuántos cumplieron 4?", "28-7-11", "Se restan los otros grupos del total.", " estudiantes"),
        arith("Una canción de 4 frases tiene 8 pulsos por frase. ¿Cuántos pulsos dura?", "4*8", "Se multiplican las frases por los pulsos.", " pulsos"),
    ],
    [ex("Quieres que una canción de cuna suene tierna. ¿Qué eliges: (a) volumen suave, tempo lento y postura serena o (b) volumen fuerte y tempo rápido?", "(a)", "Esas decisiones transmiten ternura.")],
    [ex("¿Qué tres cosas expresan carácter además de las notas?", "Dinámica, frases y postura", "Son parte de la musicalidad."), ex("¿Expresar es tocar más fuerte?", "No", "La expresión usa contrastes."), ex("¿Qué haces al terminar una frase?", "La cierro con calma", "Se siente completa.")],
    (
        "Elige una canción corta o una ronda que sepas. Interprétala dos veces, a volumen bajo: primero sin expresión (todo igual) y luego con musicalidad (dinámica, frases con calma, postura que acompañe). Escribe qué criterios de la clase cumplió cada versión y cuántos suman. Compartir tu interpretación con otras personas es opcional.",
        "Versión 1: cumple el criterio 1 (1 de 5). Versión 2: cumple 1, 2, 3 y 5 (4 de 5).",
        ["interpreta dos versiones", "aplica los criterios", "cuenta los puntos"],
        ["interpretación", "registro escrito"],
        ["exagerar gestos", "tocar más fuerte en vez de cambiar la dinámica"],
        "Reconoce el contraste entre las versiones y pide señalar en cuál frase cambió la dinámica y por qué.",
    ),
    "Canta una frase con calma al final y otra sin cuidar el final, y di cuál sonó mejor.",
    "Haz tres versiones de una frase con distinta dinámica y elige la que mejor expresa tu propósito.",
)

# ---------------------------------------------------------------- OA 06 · clase 4 (presentación grupal a la comunidad)
SILLAS = (4, 6)

L(
    OA6, 4,
    "Lápiz y papel. Plan de presentación de ejemplo (inventado): un grupo de 24 intérpretes se ubica en 4 filas de 6 personas. Si presentas al curso o a otras personas, es opcional invitar a más; compartir tu trabajo siempre es voluntario.",
    "Aprenderé a presentar un trabajo musical en grupo al curso o a la comunidad: organizar el espacio, entrar y salir con orden, coordinarnos y recibir comentarios con respeto. Sirve para que la presentación salga bien y cuide a todos.",
    ["Sé repartir roles.", "Sé ensayar con método.", "Sé interpretar con expresión."],
    [
        "Presentar al curso o a la comunidad significa que el público puede ser tus compañeros, las familias del curso u otras personas del colegio. Antes de presentar, el grupo organiza el espacio: dónde se ubican los intérpretes, por dónde entran y salen, y que no haya objetos en el suelo. Un grupo de 24 intérpretes puede ubicarse en 4 filas de 6 personas.",
        "En el momento de presentar, el orden es: el presentador o presentadora saluda y dice el nombre de la pieza, el grupo se ubica en silencio, la persona responsable de la señal cuenta 4 pulsos y todos empiezan juntos. Al terminar, el grupo agradece y sale con orden. Si hay nervios, respira profundo y mira un punto fijo. Si algo falla, el grupo sigue sin detenerse.",
        "Después de la presentación, el grupo conversa sobre lo que resultó bien y lo que puede mejorar, hablando de la música y no de las personas. También recibe con gratitud los comentarios del público. Presentar es un trabajo en equipo: la calidad depende de que cada persona cumpla su parte y escuche a las demás.",
    ],
    [("comunidad", "personas que comparten un lugar o un grupo, como el curso o el colegio"), ("ubicación", "lugar donde se ubica cada intérprete"), ("entrar y salir con orden", "hacerlo sin apuro y en silencio"), ("agradecer", "dar las gracias al público al terminar"), ("comentario", "opinión sobre lo que se presentó")],
    [
        ("Calcular la ubicación", "Un grupo de 24 intérpretes se ubica en filas de 6 personas. ¿Cuántas filas necesita?", ["Cada fila tiene 6 personas.", "24 ÷ 6 = 4."], "4 filas"),
        ("Ordenar la presentación", "Una presentación tiene estos pasos: (a) cuenta de 4 pulsos, (b) saludo y presentación de la pieza, (c) el grupo se ubica en silencio. ¿En qué orden van?", ["Primero se saluda.", "Luego el grupo se ubica.", "Por último se cuentan los 4 pulsos."], "b, c, a"),
    ],
    [
        ("Entrar corriendo y hablando.", "Distrae al público y genera accidentes.", "Entra con orden y en silencio."),
        ("Criticar a una persona del grupo después de presentar.", "Los comentarios deben tratar sobre la música, no sobre las personas.", "Habla de la música y de cómo mejorar juntos."),
    ],
    [
        ex("Antes de empezar, ¿quién cuenta 4 pulsos?", "La persona responsable de la señal", "Marca el inicio del grupo."),
        ex("Si algo falla durante la presentación, ¿el grupo se detiene o sigue?", "Sigue", "Mantener la música evita cortar la presentación."),
        ex("Al terminar, ¿qué hace el grupo con el público?", "Agradece", "Agradecer es parte de la presentación."),
    ],
    [
        ex("Un grupo de 20 intérpretes se ubica en 4 filas iguales. ¿Cuántas personas hay en cada fila?", "5", "20 repartido en 4 filas es 5."),
        ex("Para evitar accidentes, ¿qué debe estar despejado antes de entrar al escenario?", "El suelo", "No debe haber objetos con los que tropezar."),
        ex("¿Los comentarios después de presentar deben hablar de la música o de las personas?", "De la música", "Así se cuida el respeto."),
    ],
    [
        arith("Un grupo de 24 intérpretes se ubica en 4 filas iguales. ¿Cuántas personas hay en cada fila?", "24//4", "Se reparten en partes iguales.", " personas"),
        arith("Una presentación en el colegio tiene 5 grupos. Cada uno presenta 4 minutos y hay 1 minuto de cambio entre grupos. ¿Cuántos minutos dura en total?", "5*4+1*4", "Hay 5 presentaciones y 4 cambios entre ellas.", " minutos"),
        ex("Una presentación empieza con el saludo, sigue con la ubicación del grupo y la señal de inicio. ¿Cuántos pasos de preparación hay antes de que suene la música?", "3", "Son tres: saludo, ubicación y señal."),
    ],
    [
        ex("Un niño del grupo se pierde en medio de la presentación y se queda quieto, sin tocar. ¿Qué debe hacer?", "Buscar el compás en que va el grupo y volver a entrar", "Así se incorpora sin cortar la música."),
        ex("Una persona del público comenta: «tu parte fue floja». ¿Qué comentario sobre la música ayuda más: (a) «mejor, a esa parte le falta más fuerza al principio» o (b) «eres malo»?", "(a)", "Habla de la música y dice qué mejorar."),
    ],
    [
        arith("Un curso de 28 estudiantes prepara una muestra para la comunidad. Cada estudiante invita como máximo a 2 personas. ¿Cuántas personas pueden ir como máximo?", "28*2", "Se multiplican los estudiantes por las invitaciones de cada uno.", " personas"),
        arith("La sala tiene 60 sillas. Ya hay 28 estudiantes sentados. ¿Cuántas sillas quedan para el público?", "60-28", "Se restan las sillas ocupadas.", " sillas"),
    ],
    [ex("Un grupo termina de presentar y el público aplaude. ¿Qué hace el grupo: agradece y sale con orden o sale corriendo?", "Agradece y sale con orden", "Cierra la presentación con respeto.")],
    [ex("¿Qué haces con el nerviosismo antes de presentar?", "Respiro profundo y miro un punto fijo", "Calma el cuerpo."), ex("¿Qué señal permite que todos empiecen juntos?", "La cuenta de 4 pulsos", "Marca el inicio común."), ex("¿De qué hablan los comentarios?", "De la música", "Así se cuida el respeto.")],
    (
        "Organiza una pequeña presentación grupal de un número breve (una ronda o un ritmo con palmas) ante tu curso o un grupo que tú elijas, si quieres. Escribe: cuántos intérpretes, cómo los ubicarás (filas y personas por fila), el orden de la presentación (saludo, ubicación, señal, música, agradecimiento) y un comentario de mejora sobre la música que pedirías después.",
        "6 intérpretes en 2 filas de 3. Orden: saludo, ubicación, señal de 4 pulsos, música, agradecimiento. Comentario: «¿Se oyó bien la melodía?»",
        ["calcula la ubicación", "ordena los pasos de la presentación", "propone un comentario sobre la música"],
        ["plan escrito"],
        ["olvidar la señal de inicio", "pedir comentarios sobre las personas"],
        "Reconoce el plan y pide comprobar el cálculo de filas; recuerda que mostrar el trabajo a otras personas es voluntario.",
    ),
    "Ordena: saludo, señal, música, agradecimiento, ubicación.",
    "Haz una lista de dos cosas que cuidarías para que el público disfrute tu presentación.",
)

# ---------------------------------------------------------------- OA 07 · clase 1 (elementos del contexto)
CTX1 = [
    ("Obra 1: una canción de cuna", "se canta en casa, en la noche, para que un bebé se duerma", "lugar: casa; momento: noche; función: dormir"),
    ("Obra 2: una marcha", "se toca en un desfile al aire libre, con tambores y trompetas", "lugar: calle o plaza; función: desfilar"),
    ("Obra 3: una danza de fiesta", "se baila en la plaza durante una celebración del pueblo, con un tambor y una guitarra", "lugar: plaza; función: bailar y celebrar"),
]
CTX1_TXT = " ".join(f"{a}: {b}." for a, b, _c in CTX1)

L(
    OA7, 1,
    f"Lápiz y papel. Las obras son ejemplos inventados. {CTX1_TXT} Elementos del contexto de la clase: lugar, momento, personas, función (para qué se usa) y materiales o instrumentos disponibles.",
    "Aprenderé a reconocer los elementos del contexto de una música: dónde, cuándo, quiénes y para qué surge. Sirve para entender por qué una música suena como suena.",
    ["Sé que la música puede ser lenta, rápida, fuerte o suave.", "Sé que la música tiene instrumentos.", "Sé escuchar con respeto."],
    [
        "El contexto de una música son las circunstancias en que surge y se usa. Los elementos del contexto de la clase son: el lugar (dónde se canta o toca), el momento (cuándo), las personas (quiénes la cantan o escuchan), la función (para qué sirve: dormir, desfilar, bailar, celebrar, trabajar) y los materiales o instrumentos disponibles. Una música no existe en el vacío: siempre se hace en un contexto.",
        f"Con las obras de la clase: {CTX1_TXT} En la obra 1, el lugar es la casa, el momento es la noche y la función es dormir a un bebé. En la obra 2, el lugar es la calle o la plaza y la función es desfilar. En la obra 3, la función es bailar y celebrar. Cada contexto lleva a distintas decisiones musicales.",
        "Para identificar el contexto, hazte cuatro preguntas: ¿dónde?, ¿cuándo?, ¿quiénes? y ¿para qué? A veces no se sabe todo, y está bien decirlo en lugar de inventar. Cuando una música viene de una comunidad, el contexto lo cuentan las personas de esa comunidad. Compartir experiencias personales es siempre opcional.",
    ],
    [("contexto", "circunstancias en que surge y se usa una música"), ("lugar", "dónde se canta o toca"), ("momento", "cuándo se canta o toca"), ("función", "para qué sirve la música"), ("comunidad", "grupo de personas que comparte una cultura")],
    [
        ("Reconocer la función", f"{CTX1_TXT} ¿Cuál es la función de la obra 2?", ["La obra 2 es una marcha en un desfile.", "Se usa para desfilar."], "Desfilar"),
        ("Reconocer el lugar", f"{CTX1_TXT} ¿En qué lugar se canta la obra 1?", ["La obra 1 es una canción de cuna.", "Se canta en casa."], "En casa"),
    ],
    [
        ("Pensar que la música solo sirve para entretener.", "Cumple muchas funciones: dormir, marchar, celebrar, trabajar.", "Pregunta siempre para qué se usa."),
        ("Inventar el contexto de una música que no conoces.", "Puedes equivocarte y faltarle el respeto a esa comunidad.", "Di qué sabes y pregunta lo que no sabes."),
    ],
    [
        ex("¿Cuáles son las cuatro preguntas que ayudan a identificar el contexto de una música?", "¿Dónde?, ¿cuándo?, ¿quiénes? y ¿para qué?", "Son las cuatro preguntas de la clase."),
        ex(f"{CTX1_TXT} ¿Para qué sirve la obra 1?", "Para dormir a un bebé", "Es una canción de cuna."),
        ex(f"{CTX1_TXT} ¿Qué instrumentos se usan en la obra 3?", "Un tambor y una guitarra", "Lo dice la descripción."),
    ],
    [
        ex(f"{CTX1_TXT} ¿En qué momento del día se canta la obra 1?", "En la noche", "La descripción dice que es de noche."),
        ex("Una música se toca en una procesión por la calle. ¿Qué elemento del contexto es la calle?", "El lugar", "Dice dónde ocurre."),
        ex("Una música para trabajar en grupo ayuda a mantener un ritmo común. ¿Qué elemento del contexto es «para trabajar»?", "La función", "Dice para qué sirve."),
    ],
    [
        ex(f"{CTX1_TXT} ¿Cuántas de las tres obras se usan al aire libre?", "2", "La marcha y la danza de fiesta se usan afuera."),
        arith("Un curso describe el contexto de 3 músicas con 5 elementos cada una (lugar, momento, personas, función y materiales). ¿Cuántos elementos describe en total?", "3*5", "Se multiplican las músicas por los elementos de cada una.", " elementos"),
        ex(f"{CTX1_TXT} ¿Qué obra se usa para bailar?", "La obra 3", "La descripción dice que es una danza de fiesta."),
    ],
    [
        ex("Marta describe la música de un pueblo originario inventando su lugar y su función, sin preguntar a nadie. ¿Qué error comete?", "Inventa el contexto en vez de preguntar a la comunidad", "El contexto de una música lo cuenta quien la practica."),
        ex("Luis dice que la obra 1 y la obra 2 tienen el mismo contexto porque ambas son música. ¿Es cierto?", "No", "Tienen lugares y funciones distintos."),
    ],
    [
        arith("En un mapa de contextos hay 4 músicas y se describen sus 5 elementos. Se anota que de cada una se conocen 4 elementos. ¿Cuántos elementos faltan por conocer en total?", "4*5-4*4", "Hay 20 elementos y se conocen 16.", " elementos"),
        arith("Un curso escucha 6 músicas: 2 de función de dormir, 1 de marchar y las demás de bailar. ¿Cuántas son de bailar?", "6-2-1", "Se restan las de dormir y marchar del total.", " músicas"),
    ],
    [ex("Una música se canta en un huerto para coordinar el trabajo de un grupo. ¿Qué elemento del contexto es «en un huerto» y cuál es «coordinar el trabajo»?", "El lugar y la función", "Uno dice dónde y el otro dice para qué se canta.")],
    [ex("¿Cuáles son los elementos del contexto de la clase?", "Lugar, momento, personas, función y materiales", "Son los cinco de la clase."), ex("¿Qué es la función de una música?", "Para qué sirve", "Puede ser dormir, desfilar o bailar."), ex("¿Qué haces si no conoces el contexto de una música?", "Pregunto y no lo invento", "Así respeto a quien la practica.")],
    (
        "Elige una música que conozcas de tu vida diaria (como una canción de cuna, una música de fiesta o una de deporte) o usa la obra 3 de la clase. Escribe sus cinco elementos del contexto: lugar, momento, personas, función y materiales o instrumentos. Si no sabes uno, escribe «no lo sé». Compartir experiencias personales es opcional; puedes usar la obra 3.",
        "Obra 3: lugar, plaza; momento, durante una celebración; personas, gente del pueblo; función, bailar y celebrar; instrumentos, tambor y guitarra.",
        ["escribe los cinco elementos", "no inventa lo que no sabe", "usa datos coherentes"],
        ["ficha escrita"],
        ["inventar datos", "confundir lugar con función"],
        "Reconoce la ficha y valora que diga «no lo sé» cuando corresponde.",
    ),
    "Escribe la función de una canción que te guste.",
    "Pregunta a una persona mayor de tu confianza para qué se usaba una música de su infancia, si quiere contártelo.",
)

# ---------------------------------------------------------------- OA 07 · clase 2 (función y rasgos sonoros)
FUN = {
    "dormir": "suave, lenta y con frases que se repiten",
    "marchar": "con pulso firme y acento marcado en cada compás",
    "bailar": "con pulso claro y tempo animado",
    "trabajar en grupo": "con un ritmo parejo que ayuda a moverse al mismo tiempo",
}
FUN_TXT = "; ".join(f"para {f}: {r}" for f, r in FUN.items())

L(
    OA7, 2,
    f"Lápiz y papel; si quieres, canta o toca con palmas a volumen bajo. Regla de la clase (rasgos sonoros según la función): {FUN_TXT}.",
    "Aprenderé a relacionar la función de una música (para qué se usa) con sus rasgos sonoros (dinámica, tempo, pulso, repetición). Sirve para explicar por qué una música suena como suena.",
    ["Sé que el contexto tiene lugar, momento, personas, función y materiales.", "Sé que la dinámica y el tempo son rasgos sonoros.", "Sé reconocer el pulso."],
    [
        "La función de una música influye en cómo suena. Una música para dormir busca calma, por eso suele ser suave, lenta y con frases que se repiten. Una marcha busca que muchas personas caminen juntas, por eso tiene un pulso firme y un acento marcado en cada compás. Una música para bailar tiene un pulso claro y un tempo animado. Una música para trabajar en grupo mantiene un ritmo parejo que ayuda a moverse al mismo tiempo.",
        f"Esta relación se puede expresar con una frase: «Esta música suena [rasgo] porque se usa para [función]». Por ejemplo: «La canción de cuna suena suave y lenta porque se usa para dormir a un bebé». La regla de la clase resume los rasgos: {FUN_TXT}. Son rasgos frecuentes, no reglas obligatorias: hay excepciones.",
        "Para relacionar, empieza por la función y busca el rasgo sonoro que la ayuda. Después, comprueba escuchando o leyendo la descripción de la música. Si el rasgo no coincide con la función, puede ser una excepción o un contexto distinto. No des por segura una relación que no puedes comprobar.",
    ],
    [("función", "para qué sirve una música"), ("rasgo sonoro", "algo que se oye, como tempo, dinámica o pulso"), ("relación", "vínculo entre la función y los rasgos sonoros"), ("acento", "pulso que se marca más fuerte"), ("excepción", "caso que no sigue la regla general")],
    [
        ("Relacionar función y rasgos", "Una música suave, lenta y con frases que se repiten, ¿para qué función encaja mejor según la regla de la clase: dormir o marchar?", ["Suave y lenta calman.", "Eso corresponde a dormir."], "Dormir"),
        ("Escribir una relación", "Completa con una frase: la marcha tiene un pulso firme porque ____.", ["La marcha se usa para caminar juntos.", "Un pulso firme ayuda a caminar al mismo paso."], "Porque se usa para marchar y un pulso firme ayuda a caminar juntos"),
    ],
    [
        ("Creer que todas las músicas de la misma función suenan idénticas.", "Son rasgos frecuentes, con excepciones.", "Compara con lo que realmente se oye."),
        ("Dar la relación sin probarla con lo que se oye.", "Se puede afirmar algo falso.", "Comprueba escuchando o leyendo la descripción."),
    ],
    [
        ex(f"Regla de la clase: {FUN_TXT}. ¿Qué rasgo tiene una música para marchar?", "Pulso firme y acento marcado en cada compás", "Eso dice la regla."),
        ex(f"Regla de la clase: {FUN_TXT}. ¿Una música para dormir es lenta o rápida?", "Lenta", "Así lo dice la regla."),
        ex("Una música para bailar, ¿tiene un pulso claro o un pulso difícil de encontrar?", "Un pulso claro", "El baile necesita un pulso claro."),
    ],
    [
        ex("Una música para trabajar en grupo tiene un ritmo parejo. ¿Para qué sirve ese rasgo?", "Para moverse al mismo tiempo", "El ritmo parejo coordina los movimientos."),
        ex("Una música se canta en un desfile con tambores. ¿Qué función cumple: bailar o marchar?", "Marchar", "Un desfile es para caminar juntos."),
        ex("Una canción de cuna con voz muy fuerte y tempo muy rápido, ¿sigue la regla de la clase?", "No", "La regla dice que es suave y lenta."),
    ],
    [
        ex("Una música para dormir es suave, lenta y repite una frase 6 veces en 24 pulsos. ¿Cuántos pulsos dura cada frase?", "4", "24 dividido en 6 frases son 4 pulsos cada una."),
        arith("Una marcha tiene 8 compases de 4 pulsos, con un acento por compás. ¿Cuántos pulsos sin acento tiene en total?", "8*4-8", "Hay 32 pulsos y 8 de ellos llevan acento.", " pulsos"),
        ex("Una música para bailar va a 2 pulsos por segundo y otra, a 1 pulso por segundo. ¿Cuál tiene un tempo más animado?", "La de 2 pulsos por segundo", "Más pulsos en el mismo tiempo es más rápido."),
    ],
    [
        ex("Ana dice: «la música para marchar es suave y lenta porque se usa de noche». ¿Qué error comete con la regla de la clase?", "La marcha tiene pulso firme y acento marcado, no es suave y lenta", "No sigue la regla de la marcha."),
        ex("Pedro escucha una música para dormir que es un poco más fuerte de lo habitual. ¿Debe decir que la regla es falsa?", "No, puede ser una excepción", "La regla describe rasgos frecuentes, no obligatorios."),
    ],
    [
        arith("En una escucha de 12 músicas, 4 eran para dormir, 3 para marchar y el resto para bailar. ¿Cuántas eran para bailar?", "12-4-3", "Se restan las de dormir y marchar del total.", " músicas"),
        arith("Una marcha de 16 compases de 4 pulsos va a 2 pulsos por segundo. ¿Cuántos segundos dura?", "16*4//2", "Primero se calculan los pulsos y luego se reparten.", " segundos"),
    ],
    [ex("Quieres componer una música para que un curso camine al mismo paso. ¿Qué rasgos eliges: (a) pulso firme y acento marcado o (b) tempo lento, suave y repetido?", "(a)", "Para caminar juntos hace falta un pulso firme.")],
    [ex("¿Qué rasgos tiene una música para dormir?", "Suave, lenta y con frases repetidas", "Esos rasgos ayudan a buscar calma."), ex("¿Qué rasgo ayuda a caminar al mismo paso?", "El pulso firme", "Marca el paso."), ex("¿La regla de la clase es obligatoria o describe rasgos frecuentes?", "Describe rasgos frecuentes", "Existen casos que son excepciones.")],
    (
        "Elige una función entre las cuatro de la clase (dormir, marchar, bailar o trabajar en grupo). Crea 4 pulsos de ritmo con palmas y voz que sigan los rasgos de esa función, a volumen bajo. Escribe una frase con «suena… porque se usa para…» y una excepción posible a la regla.",
        "Función: marchar. Ritmo: TA – TA – TA – TA, con acento fuerte en el primero. Frase: suena con pulso firme porque se usa para marchar. Excepción: una marcha lenta para una ceremonia solemne.",
        ["el ritmo sigue la función", "la frase tiene «porque»", "propone una excepción posible"],
        ["interpretación", "frase escrita"],
        ["relacionar sin explicar por qué", "decir que la regla no tiene excepciones"],
        "Reconoce la relación y pide que muestre en el ritmo el rasgo que eligió para la función.",
    ),
    "Escribe una frase con «suena… porque se usa para…».",
    "Escucha, con permiso, la música de un deporte o actividad y di qué rasgos ayudan a su función.",
)

# ---------------------------------------------------------------- OA 07 · clase 3 (materiales, comunidad y época)
ISLA = ("En la «isla de las cañas» (una región inventada) crecen cañas y hay cabras. Allí se hacen flautas con cañas y tambores con cuero de cabra. "
        "No hay metales. Antes de que llegaran las radios, la música se aprendía escuchando; hoy una radio permite escuchar música de otros lugares.")

L(
    OA7, 3,
    f"Lápiz y papel. Región inventada para la clase: {ISLA}",
    "Aprenderé a relacionar una música con los materiales de su entorno, con la comunidad que la practica y con la época en que se escucha (antes y después de las grabaciones). Sirve para explicar por qué una música usa ciertos instrumentos y se escucha de cierta manera.",
    ["Sé que hay instrumentos de viento y de percusión.", "Sé que una música puede venir de una comunidad.", "Sé que antes no existían las radios."],
    [
        "Los instrumentos suelen hacerse con los materiales que hay cerca. Donde crecen cañas se hacen flautas de caña, y donde hay animales con cuero se hacen tambores. Por eso el entorno influye en el timbre de una música. En la región inventada de la clase: " + ISLA,
        "La comunidad también da forma a la música. Si una comunidad se junta a celebrar, la música se canta y baila entre muchas personas. Si trabaja en grupo, hay cantos que ayudan a coordinarse. Cuando la música es de un pueblo originario, su significado lo enseñan los educadores o educadoras tradicionales y la comunidad; no hay que inventarlo.",
        "La época cambia cómo se escucha la música. Antes de las grabaciones y de la radio, la música se aprendía en vivo: escuchando a otras personas o leyendo una partitura. Hoy se puede escuchar una música de otro país con una grabación. Por eso los contextos cambian, pero muchas músicas siguen vivas porque las personas las siguen cantando y tocando.",
    ],
    [("entorno", "lo que rodea a una comunidad: plantas, animales, clima"), ("material", "cosa con que se hace un instrumento, como caña o cuero"), ("época", "tiempo en que se vive o se hizo una música"), ("grabación", "registro de sonido que permite volver a escuchar"), ("tradicional", "que se transmite en una comunidad por mucho tiempo")],
    [
        ("Relacionar material e instrumento", f"{ISLA} ¿Con qué materiales se hacen los instrumentos de la isla?", ["Se mencionan cañas y cuero de cabra.", "Las cañas sirven para flautas y el cuero para tambores."], "Con cañas (flautas) y cuero de cabra (tambores)"),
        ("Explicar una ausencia", f"{ISLA} ¿Por qué en la isla no se tocan instrumentos de metal?", ["El texto dice que no hay metales.", "Los instrumentos se hacen con lo que hay cerca."], "Porque no hay metales en el entorno"),
    ],
    [
        ("Pensar que todos los pueblos usan los mismos instrumentos.", "Cada entorno ofrece materiales distintos.", "Pregunta qué materiales hay y qué usa cada comunidad."),
        ("Explicar la música de un pueblo originario sin conocerla.", "Cada pueblo decide su significado y uso.", "Pregunta al educador o educadora tradicional o a la comunidad."),
    ],
    [
        ex(f"{ISLA} ¿De qué material son las flautas de la isla?", "De cañas", "El texto lo dice."),
        ex(f"{ISLA} ¿Con qué se hacen los tambores de la isla?", "Con cuero de cabra", "Así lo dice la descripción."),
        ex("Antes de que existieran las radios, ¿cómo se aprendía la música principalmente?", "Escuchando a otras personas", "La música se transmitía en vivo."),
    ],
    [
        ex(f"{ISLA} Una trompeta es un instrumento de metal. ¿Se pudo hacer con materiales de la isla?", "No", "En la isla no hay metales."),
        ex("Un tambor suena grave y otro, agudo. ¿Qué cualidad del sonido cambió: altura o duración?", "Altura", "Grave y agudo hablan de la altura."),
        ex("¿Una radio permite escuchar música de un lugar lejano o solo del lugar donde se vive?", "De un lugar lejano también", "La radio lleva música a otras partes."),
    ],
    [
        arith("En la isla hay 30 flautas de caña y 12 tambores de cuero. ¿Cuántos instrumentos hay en total?", "30+12", "Se suman las flautas y los tambores.", " instrumentos"),
        arith("Cada tambor necesita 1 cuero de cabra. Si hay 12 tambores y 5 cabras dieron cuero para 2 tambores cada una, ¿cuántos tambores aún no tienen cuero?", "12-5*2", "Las cabras aportaron 10 cueros; se restan de 12.", " tambores"),
        ex("Una comunidad canta mientras trabaja la tierra en grupo. ¿Qué función cumple ese canto?", "Ayudar a coordinar el trabajo", "El canto marca un ritmo común."),
    ],
    [
        ex("Luis dice que, como en la isla no hay metales, allí no puede haber música. ¿Es cierto?", "No", "La isla tiene flautas de caña y tambores de cuero."),
        ex("Marta dice que la música de un pueblo originario siempre significa lo mismo para todos. ¿Qué debe hacer para saber su significado?", "Preguntar al educador o educadora tradicional o a la comunidad", "Cada pueblo decide el significado de su música."),
    ],
    [
        arith("Una escuela tiene 20 estudiantes, y cada uno quiere una flauta de caña. Cada caña da 2 flautas. ¿Cuántas cañas necesita?", "20//2", "Se reparten los estudiantes entre las flautas por caña.", " cañas"),
        arith("Un grupo escucha una grabación de 5 minutos 3 veces para analizarla. ¿Cuántos minutos escucha?", "5*3", "Se multiplican los minutos por las veces.", " minutos"),
    ],
    [ex("Una comunidad fabrica tambores y flautas con lo que hay en su entorno. ¿Qué explica esa decisión: el entorno o la moda?", "El entorno", "Los materiales disponibles determinan los instrumentos.")],
    [ex("¿Con qué se hacen los instrumentos de una comunidad?", "Con materiales de su entorno", "Dependen de lo que hay."), ex("¿Quién enseña el significado de la música de un pueblo originario?", "Los educadores tradicionales y la comunidad", "Ellos la practican."), ex("¿Qué cambió con la radio y las grabaciones?", "Se puede escuchar música de otros lugares", "Amplía lo que se escucha.")],
    (
        "Inventa una región nueva (con su entorno, sus materiales y sus animales), como la isla de las cañas. Escribe cuál es su entorno, qué instrumentos se hacen allí con esos materiales, cuál es su función en la comunidad y una cosa que cambió con las grabaciones. Debe ser una región inventada: no atribuyas tu invención a ningún pueblo real.",
        "Región de las piedras blancas: hay piedras lisas y madera. Instrumentos: piedras que se golpean y palos que se frotan. Función: acompañar el baile. Con las grabaciones se puede escuchar esa música en otras partes.",
        ["describe un entorno y sus materiales", "relaciona materiales con instrumentos", "indica su función y un cambio por las grabaciones", "no usa un pueblo real"],
        ["texto escrito"],
        ["atribuir datos inventados a un pueblo real", "instrumentos sin relación con el entorno"],
        "Reconoce la coherencia entre entorno e instrumentos y recuerda no inventar datos de pueblos reales.",
    ),
    "Nombra un material con el que se podría hacer un instrumento de percusión.",
    "Pregunta a una persona mayor de tu confianza cómo escuchaba música cuando era niña o niño, si quiere contártelo.",
)

# ---------------------------------------------------------------- OA 07 · clase 4 (explicar la relación con evidencia)
EXPL = [
    ("A", "La música suena lenta y suave porque se usa para dormir a un bebé."),
    ("B", "La música es bonita porque es de un pueblo."),
    ("C", "La marcha tiene un pulso firme porque se toca en un desfile y la gente debe caminar al mismo paso."),
    ("D", "Los tambores suenan graves porque las personas se juntan."),
]
EXPL_TXT = " ".join(f"Explicación {n}: «{t}»" for n, t in EXPL)
BUENAS = ["A", "C"]

L(
    OA7, 4,
    f"Lápiz y papel. Explicaciones de ejemplo: {EXPL_TXT} Criterio de la clase: una buena explicación nombra un rasgo sonoro que se oye, un elemento del contexto y los une con «porque».",
    "Aprenderé a explicar la relación entre una obra y su contexto con evidencia: nombrar un rasgo sonoro, nombrar un elemento del contexto y unirlos con «porque». Sirve para argumentar con claridad lo que entiendo de la música.",
    ["Sé reconocer los elementos del contexto.", "Sé relacionar función y rasgos sonoros.", "Sé nombrar rasgos sonoros."],
    [
        "Explicar la relación entre una obra y su contexto es decir por qué suena como suena según las circunstancias en que surge. Una buena explicación tiene tres partes: un rasgo sonoro que se oye (por ejemplo, lenta y suave), un elemento del contexto (por ejemplo, la función de dormir) y una conexión con «porque». Si falta una de las tres partes, la explicación queda incompleta.",
        f"Con el criterio de la clase, revisa las explicaciones de ejemplo: {EXPL_TXT} La A es buena: tiene el rasgo (lenta y suave), el contexto (dormir) y el «porque». La B no lo es: «bonita» no es un rasgo que se oiga y «de un pueblo» no explica nada. La C es buena. La D tiene el rasgo (graves) y un contexto vago (las personas se juntan) que no explica por qué serían graves.",
        "Para mejorar una explicación, pregúntate: ¿qué rasgo se oye?, ¿qué circunstancia lo explica?, ¿tiene sentido esa conexión? También se puede comparar dos obras: «La obra X es suave porque es para dormir; la obra Y es fuerte porque es para desfilar». Comparar ayuda a ver cómo el contexto cambia las decisiones musicales.",
    ],
    [("evidencia", "dato que se oye o se sabe y apoya una explicación"), ("rasgo sonoro", "algo que se oye, como tempo, dinámica o timbre"), ("conexión", "unión entre el rasgo y el contexto"), ("argumentar", "explicar con razones"), ("comparar", "ver semejanzas y diferencias")],
    [
        ("Revisar una explicación", f"Explicación B: «{EXPL[1][1]}». ¿Qué partes de una buena explicación le faltan?", ["Busca un rasgo sonoro: «bonita» no se oye.", "Busca un contexto claro: «de un pueblo» es muy vago."], "Le faltan un rasgo sonoro que se oiga y un contexto que explique el rasgo"),
        ("Mejorar una explicación", "«Los tambores suenan graves porque las personas se juntan.» ¿Qué conviene cambiar para que sea una buena explicación?", ["El contexto debe explicar el rasgo.", "Hay que decir un contexto claro, como la función o el material."], "Dar un contexto claro que explique por qué son graves"),
    ],
    [
        ("Explicar con «es bonita» o «me gusta».", "No son rasgos sonoros ni contexto.", "Nombra un rasgo que se oiga y una circunstancia."),
        ("Unir un rasgo con un contexto que no tiene relación.", "La conexión debe tener sentido.", "Pregunta si el contexto explica el rasgo."),
    ],
    [
        ex("¿Cuántas partes tiene una buena explicación de la clase?", "3", "Son un rasgo sonoro, un elemento del contexto y una conexión con «porque»."),
        ex("¿Qué palabra une el rasgo sonoro con el contexto?", "Porque", "Marca la conexión."),
        ex(f"{EXPL_TXT} ¿Cuál es el rasgo sonoro de la explicación A?", "Lenta y suave", "Lo dice la explicación."),
    ],
    [
        ex(f"{EXPL_TXT} ¿Cuál es el elemento del contexto de la explicación C?", "El desfile, donde la gente debe caminar al mismo paso", "Es la función de marchar."),
        ex(f"{EXPL_TXT} ¿Cuáles de las explicaciones A, B, C y D son buenas según el criterio de la clase?", "A y C", "Tienen rasgo, contexto y «porque» con sentido."),
        ex("«La canción suena rápida porque es lunes.» ¿Es una buena explicación?", "No", "Lunes no explica por qué suena rápida."),
    ],
    [
        ex("¿Cuál es una buena explicación para una música de baile: (a) «Suena con pulso claro porque se usa para bailar» o (b) «Suena con pulso claro porque es bonita»?", "(a)", "La (a) une el rasgo con la función; «bonita» no es una razón."),
        ex("Obra X: suave y lenta, para dormir. Obra Y: fuerte y con pulso firme, para desfilar. ¿Qué diferencia de contexto explica la diferencia de sonido?", "La función: dormir y desfilar", "Cada función pide rasgos distintos."),
        arith("De 12 explicaciones del curso, 5 estaban completas, 4 tenían rasgo sin contexto y el resto tenía contexto sin rasgo. ¿Cuántas tenían contexto sin rasgo?", "12-5-4", "Se restan los otros dos grupos del total.", " explicaciones"),
    ],
    [
        ex("Una niña dice: «Los tambores suenan graves porque los hacen con cuero grueso de animales grandes». ¿Qué debería comprobar antes de afirmarlo?", "Si es verdad en esa comunidad, preguntando o investigando", "No se debe afirmar un dato del contexto sin comprobarlo."),
        ex("Pedro cree que cualquier contexto sirve para explicar cualquier rasgo. ¿Qué le responderías?", "Que la conexión debe tener sentido", "No cualquier contexto explica cualquier rasgo."),
    ],
    [
        arith("Un grupo explica 4 músicas con 3 partes cada una (rasgo, contexto y conexión). ¿Cuántas partes escribe en total?", "4*3", "Se multiplican las músicas por las partes.", " partes"),
        arith("Un curso de 28 estudiantes hace explicaciones en parejas. ¿Cuántas explicaciones hay?", "28//2", "Se reparten los estudiantes en parejas.", " explicaciones"),
    ],
    [ex("Quieres explicar por qué una música de fiesta del pueblo es rápida y con tambores fuertes. ¿Qué tres partes debe tener tu explicación?", "Rasgo sonoro, elemento del contexto y «porque»", "Son las partes de una buena explicación.")],
    [ex("En Música: ¿Qué es la evidencia?", "Un dato que apoya mi explicación", "Sostiene lo que digo."), ex("¿Basta con decir «me gusta»?", "No", "Falta un rasgo y un contexto."), ex("¿Qué haces para comparar dos obras?", "Veo qué cambia en el sonido y en el contexto", "Así se explica la relación.")],
    (
        "Elige dos músicas de funciones distintas que conozcas (por ejemplo, una canción de cuna y una marcha) o usa las obras X e Y de la clase. Escribe una explicación con las tres partes para cada una (rasgo sonoro, elemento del contexto y «porque») y una frase de comparación entre las dos. Compartir experiencias personales es opcional.",
        "Obra X: suena suave y lenta porque se usa para dormir. Obra Y: suena fuerte y con pulso firme porque se usa para desfilar. Comparación: cambian la dinámica y el tempo porque cambian las funciones.",
        ["dos explicaciones con rasgo, contexto y «porque»", "una frase de comparación", "no inventa datos que no sabe"],
        ["texto escrito"],
        ["usar «es bonita» como razón", "unir un contexto sin relación con el rasgo"],
        "Reconoce las explicaciones y pide subrayar en cada una el rasgo, el contexto y el «porque».",
    ),
    "Escribe una explicación con rasgo, contexto y «porque» para una canción de cuna.",
    "Compara dos músicas de funciones distintas con una frase.",
)
