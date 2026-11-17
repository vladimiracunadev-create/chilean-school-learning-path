"""Interpretación musical 3.º y 4.º medio HC: OAC-06 (evaluar críticamente procesos y resultados de trabajos de interpretación, propios y de pares: propósitos, decisiones, instrumentos y planes de mejora). Casos inventados."""
from __future__ import annotations

from hc_imus_common import build

O6 = "AR-IMUS-3y4-OAC-06"

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (proyecto de ejemplo «Vuelo de papel», inventado, de un trío con voz, guitarra y percusión de mesa). "
     "Propósito expresivo: transmitir ligereza y alegría en un acto del liceo. "
     "Proceso (bitácora): ensayo 1, se eligió el tempo de 100 pulsos por minuto; ensayo 2, se acortó el saludo; ensayo 3, la guitarra bajó a p cuando entra la voz; ensayo 4, se agregó una pausa de silencio entre pasadas. "
     "Resultado (interpretación final): 100 pulsos por minuto; dinámica entre mf y f; en 4 pasadas hubo 1 desfase entre guitarra y percusión; duración de 3 minutos; el público de prueba oyó bien la voz. "
     "Aspectos estéticos mencionados: el ritmo saltarín y la voz clara.")
build(
    O6, 1, F,
    use="Aprenderé a distinguir el proceso del resultado de una interpretación y a reconocer el propósito expresivo y los aspectos estéticos que sirven de base para evaluar críticamente un trabajo.",
    prior=["Sé llevar una bitácora de ensayo.", "Sé aplicar criterios con evidencia.", "Sé que evaluar es distinto de opinar."],
    explain=[
        "Evaluar críticamente un trabajo de interpretación es valorarlo con criterios y evidencia, no con gusto. Se evalúan dos cosas distintas. El resultado es la interpretación final tal como se oye: su tempo, dinámica, ejecución y duración. El proceso es el camino que llevó hasta ella: las decisiones que se tomaron, las pruebas, los ajustes y el cuidado del grupo. Un buen resultado puede venir de un proceso desordenado, y un buen proceso puede dar un resultado que todavía no es el esperado.",
        "Para evaluar se necesita un punto de comparación. El propósito expresivo es lo que el trabajo quiere comunicar («ligereza y alegría»). Los aspectos estéticos son las cualidades que la obra muestra al oído (ritmo saltarín, voz clara, fuerza media a alta). Un trabajo se evalúa preguntando si el resultado cumple el propósito y si las decisiones del proceso lo apoyaron. Sin propósito claro, no hay cómo juzgar si una decisión fue acertada.",
        "Evaluar también implica ser justo: se cita evidencia del proceso (la bitácora) y del resultado (la ejecución final), se reconoce lo que funcionó y se señala lo que puede mejorar. La evaluación se hace sobre el trabajo, no sobre las personas. Si el ensayo exigió esfuerzo físico, se evalúa también si se cuidó la voz, las manos y el oído con pausas y volumen moderado.",
    ],
    vocab=[("proceso", "camino de decisiones, pruebas y ajustes que lleva a la interpretación"), ("resultado", "interpretación final tal como se oye"), ("propósito expresivo", "lo que el trabajo quiere comunicar"),
           ("aspecto estético", "cualidad que la obra muestra al oído"), ("evidencia", "dato de la bitácora o de la ejecución que respalda una evaluación"), ("evaluación crítica", "valoración con criterios y evidencia")],
    worked=[
        ("Clasificar un dato", "Un dato de ejemplo dice: «en el ensayo 2 se cambió el orden de las piezas». ¿Es del proceso o del resultado?",
         ["Describe una decisión que se tomó durante los ensayos.", "Es un dato del proceso."],
         "Del proceso"),
        ("Comparar con el propósito", "Un trabajo de ejemplo quiere transmitir calma y su interpretación final va a 150 pulsos por minuto y en f. ¿Cumple el propósito?",
         ["Un tempo rápido y una fuerza alta apuntan a energía, no a calma.", "El resultado no cumple el propósito."],
         "No cumple: tempo rápido y fuerza alta no transmiten calma"),
    ],
    mistakes=[("Evaluar solo el resultado y olvidar lo que se decidió en el camino.", "Se pierde información para mejorar el próximo trabajo.", "Revisa la bitácora y evalúa también las decisiones del proceso."),
              ("Evaluar sin conocer el propósito del trabajo.", "No hay con qué comparar el resultado.", "Parte siempre del propósito expresivo.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es el proceso de un trabajo?', 'El camino de decisiones y ajustes hacia la interpretación final', 'La interpretación final tal como se oye ante el público presente en el acto', 'La lista de personas que escucharon el trabajo en el acto del liceo', 'El proceso es el camino; el resultado es la interpretación final.'),
        ('abc', '{F} ¿Cuál es el propósito expresivo del trío?', 'Transmitir ligereza y alegría en un acto del liceo', 'Transmitir calma y silencio en una sala de espera', 'Demostrar la técnica de cada integrante del grupo', 'La ficha indica que el propósito es ligereza y alegría.'),
        ('abc', '{F} ¿Cuál de estos datos es del proceso?', 'En el ensayo 3 la guitarra bajó a p cuando entra la voz', 'En la interpretación final hubo 1 desfase en 4 pasadas', 'La interpretación final dura 3 minutos', 'El ensayo 3 es una decisión de la bitácora, o sea del proceso.'),
        ('abc', '{F} ¿Cuál de estos datos es del resultado?', 'Hubo 1 desfase entre guitarra y percusión', 'En el ensayo 2 se acortó el saludo del grupo de trabajo', 'En el ensayo 4 se agregó una pausa de silencio entre las pasadas', 'Los desfases se miden en la interpretación final.'),
        ('=', '{F} La interpretación final dura 3 minutos a 100 pulsos por minuto. ¿Cuántos pulsos tiene?', '3*100', 'Se multiplican los minutos por los pulsos de cada minuto.', ' pulsos'),
        ('abc', '{F} ¿El tempo de 100 pulsos y la dinámica entre mf y f apoyan el propósito de ligereza y alegría?', 'Sí, porque un pulso animado y una fuerza media suenan alegres', 'No, porque la alegría solo se logra con un tempo muy lento y suave', 'No se puede saber, porque el tempo no influye en el carácter de una pieza', 'Un tempo animado y una fuerza de media a alta se asocian con alegría.'),
        ('abc', '{F} ¿Qué aspecto estético menciona la ficha para el trabajo?', 'El ritmo saltarín y la voz clara', 'La forma A B A y los acordes de piano', 'El eco y los sonidos electrónicos', 'La ficha menciona ritmo saltarín y voz clara.'),
        ('=', '{F} En 4 pasadas hubo 1 desfase, en una sola pasada. ¿Qué porcentaje de las pasadas tuvo desfase?', '1*100//4', 'Se divide la pasada con desfase por el total de pasadas y se multiplica por 100.', ' %'),
        ('abc', '{F} Un estudiante dice «el resultado fue bueno, así que el proceso fue perfecto». ¿Qué falla en esa conclusión?', 'Un buen resultado no prueba que cada decisión haya sido buena', 'Un buen resultado siempre significa que el proceso fue totalmente correcto', 'El proceso no se puede evaluar porque no se oye en la interpretación final', 'El proceso se evalúa con la bitácora, aparte del resultado.'),
        ('abc', '{F} ¿Qué decisión del proceso apoya el propósito de que la voz se oiga con claridad?', 'La guitarra baja a p cuando entra la voz', 'Se acorta el saludo del grupo en el ensayo 2', 'Se agrega una pausa de silencio entre las pasadas', 'Bajar el acompañamiento deja oír la voz, que es la melodía.'),
        ('abc', '{F} ¿Qué decisión del proceso cuida la salud del grupo?', 'La pausa de silencio, que descansa voz y manos', 'El tempo de 100 pulsos, que permite tocar con más rapidez', 'El saludo más corto, que reduce las palabras que se dicen', 'Una pausa de silencio descansa voz, oído y manos.'),
        ('abc', '{F} Un integrante dice «evaluemos solo cómo suena, porque la bitácora no importa». ¿Qué respuesta es correcta?', 'La bitácora aporta evidencia de las decisiones del proceso', 'Tiene razón, porque lo único que se evalúa es el sonido final del trabajo', 'Tiene razón, porque la bitácora solo sirve para ordenar las notas de la pieza', 'El proceso se evalúa con la bitácora y complementa la evaluación del resultado.'),
        ('=', '{F} A 100 pulsos por minuto, ¿cuántos pulsos suenan en 45 segundos?', '100*45//60', 'Se multiplican los pulsos por minuto por los segundos y se divide por 60.', ' pulsos'),
    ],
    ctx=('abc', 'Tu grupo recibe un comentario que dice «su trabajo estuvo bien». ¿Qué le pides a quien lo dijo para poder usarlo?', 'Que cite un dato del resultado o del proceso que respalde esa valoración', 'Que diga si es amigo o amiga del grupo para saber su sesgo', 'Que vuelva a escuchar el trabajo cuantas veces quiera sin volver a opinar', 'Una valoración útil se apoya en evidencia del proceso o del resultado.'),
    sc=[
        ("En Interpretación musical: ¿qué es el propósito expresivo?", "Lo que el trabajo quiere comunicar", "Sirve de punto de comparación para evaluar el resultado."),
        ('abc', 'Los desfases entre partes en la versión final son datos:', 'Del resultado', 'Del proceso', 'Del propósito', 'Se miden en la interpretación final, es decir, el resultado.'),
        ("¿Por qué se evalúa también el cuidado de la voz y las manos durante el proceso?", "Porque ensayar de manera segura es parte de un buen trabajo", "Un proceso sano evita fatiga y lesiones."),
    ],
    op=("Con la {F}, escribe una evaluación de cuatro frases: una sobre el propósito, una sobre el resultado con un dato, una sobre el proceso con una decisión de la bitácora y una conclusión. Cada frase debe citar un dato de la ficha.",
        "Propósito: transmitir ligereza y alegría. Resultado: va a 100 pulsos por minuto y entre mf y f, lo que suena animado; hubo 1 desfase en 4 pasadas. Proceso: en el ensayo 3 la guitarra bajó a p cuando entra la voz, lo que ayuda a oír la melodía. Conclusión: el trabajo cumple su propósito y puede mejorar el pulso compartido.",
        ["nombra el propósito", "cita un dato del resultado", "cita una decisión del proceso", "cierra con una conclusión justificada"],
        ["hoja con las cuatro frases"],
        ["no citar datos de la ficha", "mezclar proceso y resultado", "evaluar sin propósito"],
        "Pregunta: «¿esa frase habla del proceso o del resultado?». Si no sabe, pídele que busque el dato en la ficha."),
    reinforce="Escribe tres datos del proceso y tres datos del resultado de un trabajo inventado y compara ambos con su propósito.",
    extend="Explica con un ejemplo por qué un buen resultado puede esconder un proceso con problemas y cómo lo detectarías.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (instrumentos de evaluación de ejemplo, inventados) para evaluar el trabajo «Vuelo de papel». "
     "Lista de cotejo: se responde sí o no a cada punto (pulso estable; voz se oye; entradas claras; duración dentro del máximo). "
     "Rúbrica: cada criterio se califica con un nivel de 1 a 4 (1, aún no; 2, en desarrollo; 3, logrado; 4, destacado). Criterios: A, coherencia con el propósito; B, ejecución; C, ensamble; D, comunicación del proceso. "
     "Registro de bitácora: texto breve con problema, ajuste y resultado de cada ensayo. "
     "Resultados de ejemplo: lista de cotejo, 3 «sí» de 4 puntos; rúbrica, A: 4, B: 3, C: 3, D: 2.")
build(
    O6, 2, F,
    use="Aprenderé a elegir y usar instrumentos de evaluación (lista de cotejo, rúbrica y bitácora), a calcular un resultado con ellos y a decidir cuál conviene según lo que se quiere evaluar.",
    prior=["Distingo proceso y resultado.", "Sé usar una pauta de criterios.", "Sé sumar y promediar números sencillos."],
    explain=[
        "Un instrumento de evaluación es una herramienta para recoger evidencia de manera ordenada. La lista de cotejo se responde con «sí» o «no» a cada punto y sirve para comprobar que algo se cumple o no se cumple. La rúbrica describe varios niveles de logro para cada criterio (por ejemplo de 1 a 4) y sirve para valorar cuánto se logró, no solo si se logró. La bitácora registra el proceso con texto breve y sirve para evaluar decisiones y ajustes.",
        "Elegir el instrumento depende de lo que se quiere saber. Si se quiere comprobar algo puntual (¿cabe en el tiempo?), conviene una lista de cotejo. Si se quiere valorar la calidad de una ejecución (¿qué tan bien se logra el ensamble?), conviene una rúbrica. Si se quiere evaluar cómo se decidió, conviene la bitácora. Muchas veces se combinan, porque cada uno entrega una parte de la evidencia.",
        "Los instrumentos también se calculan. En una rúbrica con tres criterios de 1 a 4, el puntaje máximo es 12, y el promedio es la suma de los niveles dividida por la cantidad de criterios. Un número no reemplaza al análisis: se acompaña de una frase que explique qué se observó. Evaluar con instrumentos ayuda a ser justo, porque todas las personas se miden con los mismos criterios.",
    ],
    vocab=[("instrumento de evaluación", "herramienta para recoger evidencia de manera ordenada"), ("lista de cotejo", "lista de puntos que se responden con sí o no"), ("rúbrica", "tabla que describe niveles de logro por criterio"),
           ("nivel de logro", "grado en que se cumple un criterio"), ("puntaje máximo", "mayor valor posible de un instrumento"), ("promedio", "suma de los valores dividida por la cantidad de valores")],
    worked=[
        ("Elegir el instrumento", "Un grupo quiere saber si su presentación cabe en 5 minutos. ¿Qué instrumento conviene?",
         ["Es una comprobación puntual con respuesta de sí o no.", "Conviene una lista de cotejo."],
         "Una lista de cotejo"),
        ("Calcular un puntaje", "Una rúbrica de ejemplo tiene cuatro criterios con niveles 3, 4, 2 y 3. ¿Cuál es el puntaje total y el promedio?",
         ["El total es 3 + 4 + 2 + 3 = 12 puntos.", "El promedio es 12 dividido por 4 criterios, o sea 3."],
         "Total 12 puntos y promedio 3"),
    ],
    mistakes=[("Usar una lista de cotejo para decidir cuánto se logró algo.", "Solo responde sí o no, sin graduar.", "Usa una rúbrica cuando importa cuánto se logró."),
              ("Entregar solo un número sin explicar qué se observó.", "El número no dice qué mejorar.", "Agrega una frase con la evidencia que justifica el nivel.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una rúbrica?', 'Una tabla de niveles de logro por criterio', 'Una lista de preguntas que se contestan con sí o con no cada una', 'Un texto que cuenta qué pasó en cada ensayo del grupo de trabajo', 'La rúbrica gradúa el logro; la lista de cotejo es de sí o no y la bitácora cuenta lo ocurrido.'),
        ('abc', '{F} ¿Cuántos puntos tiene la lista de cotejo de la ficha?', 'Cuatro puntos, que se responden con sí o no', 'Tres puntos, que se califican de 1 a 4', 'Dos puntos, que se explican con un texto breve', 'La ficha enumera cuatro puntos de la lista de cotejo.'),
        ('abc', '{F} ¿Qué nivel de la rúbrica significa «logrado»?', 'El nivel 3', 'El nivel 2', 'El nivel 4', 'La ficha define 3 como logrado, 2 como en desarrollo y 4 como destacado.'),
        ('=', '{F} ¿Cuál es el puntaje total de la rúbrica con A: 4, B: 3, C: 3 y D: 2?', '4+3+3+2', 'Se suman los niveles de los cuatro criterios.', ' puntos'),
        ('=', '{F} ¿Cuál es el puntaje máximo posible de la rúbrica con cuatro criterios de nivel 4 como máximo?', '4*4', 'Se multiplica el nivel máximo por la cantidad de criterios.', ' puntos'),
        ('abc', '{F} El grupo quiere saber si cumplió el máximo de duración del acto. ¿Qué instrumento conviene?', 'La lista de cotejo, porque es una comprobación de sí o no', 'La rúbrica, porque entrega cuatro niveles para cada criterio', 'La bitácora, porque cuenta cómo se decidió cada ensayo', 'Una comprobación puntual se resuelve con una lista de cotejo.'),
        ('abc', '{F} El grupo quiere valorar cuánto se logró el ensamble. ¿Qué instrumento conviene?', 'La rúbrica, porque gradúa el logro del criterio C', 'La lista de cotejo, porque solo responde sí o no', 'Ninguno, porque el ensamble no se puede evaluar', 'La rúbrica describe niveles de logro, útil para el ensamble.'),
        ('=', '{F} ¿Cuál es el promedio de los niveles de la rúbrica (4, 3, 3 y 2)? (La suma es 12.)', '12//4', 'Se divide el total de puntos por la cantidad de criterios.', ' puntos'),
        ('abc', '{F} En la lista de cotejo hay 3 «sí» de 4 puntos. ¿Qué observación es correcta?', 'Cumple 3 de los 4 puntos y falta uno', 'Cumple todos los puntos, porque la mayoría es «sí» en la lista', 'No cumple ninguno, porque no son los cuatro puntos de la lista', 'Tres «sí» de cuatro significa que falta un punto por cumplir.'),
        ('abc', '{F} ¿En cuál criterio de la rúbrica el grupo tiene el nivel más bajo?', 'En el D, comunicación del proceso, con nivel 2', 'En el A, coherencia con el propósito, con nivel 4', 'En el B, ejecución, con nivel 3', 'El nivel 2 del criterio D es el más bajo de los cuatro.'),
        ('abc', '{F} Un estudiante dice: «con 12 de 16 puntos, el trabajo está perfecto». ¿Qué falla?', 'Un número no reemplaza la evidencia de lo observado', 'Que 12 de 16 puntos es menos de la mitad del puntaje máximo', 'La rúbrica no se puede sumar nunca ni calcular su promedio', 'El número se acompaña de una frase con evidencia sobre lo observado.'),
        ('abc', '{F} El grupo quiere evaluar cómo decidió ajustar el saludo y la pausa. ¿Qué instrumento entrega mejor la evidencia?', 'La bitácora, que registra las decisiones', 'La lista de cotejo de cuatro puntos de sí o no del trabajo', 'La rúbrica, que solo mide el resultado final del grupo', 'La bitácora guarda las decisiones del proceso.'),
        ('=', '{F} Si el grupo mejora el criterio D de nivel 2 a nivel 4 y los demás no cambian, ¿cuál sería el nuevo puntaje total?', '4+3+3+4', 'Se suman los niveles nuevos de los cuatro criterios.', ' puntos'),
    ],
    ctx=('abc', 'Tu docente quiere saber si cada integrante del grupo tocó su parte completa, y también cuán bien lo hizo. ¿Qué combinación de instrumentos conviene?', 'Una lista de cotejo y una rúbrica para valorar', 'Solo una bitácora, porque cuenta todo lo ocurrido en los ensayos', 'Ningún instrumento, porque la evaluación se hace de memoria de cada persona', 'Cada instrumento aporta un tipo de evidencia distinto, y juntos son más completos.'),
    sc=[
        ("En Interpretación musical: ¿qué es una lista de cotejo?", "Una lista de puntos que se responden con sí o no", "Sirve para comprobar si algo se cumple."),
        ('abc', 'Una rúbrica sirve para:', 'Valorar cuánto se logró un criterio', 'Responder solo sí o no a cada punto', 'Contar lo que pasó en cada ensayo del grupo', 'La rúbrica describe niveles de logro.'),
        ("¿Qué se agrega a un número para que la evaluación sea útil?", "Una frase con la evidencia que lo justifica", "El número solo no dice qué mejorar."),
    ],
    op=("Con la {F}, elige el instrumento que usarías para evaluar cada una de estas tres preguntas y explica por qué: (a) ¿cabe en el tiempo? (b) ¿qué tan bien se logró el ensamble? (c) ¿cómo se decidió el orden de las piezas? Luego calcula el promedio de la rúbrica de ejemplo.",
        "(a) Lista de cotejo, porque es una comprobación de sí o no. (b) Rúbrica, porque gradúa el logro del criterio C. (c) Bitácora, porque registra las decisiones. Promedio: 4 + 3 + 3 + 2 = 12; 12 dividido por 4 criterios es 3.",
        ["elige un instrumento para cada pregunta", "justifica cada elección", "calcula el promedio", "cierra con una frase de evidencia"],
        ["hoja con las tres elecciones y el cálculo"],
        ["usar la rúbrica para un sí o no", "olvidar la justificación", "calcular mal el promedio"],
        "Pregunta: «¿qué tipo de evidencia entrega ese instrumento?». Si no lo sabe, pídele que relea la ficha."),
    reinforce="Inventa una lista de cotejo de tres puntos y una rúbrica de dos criterios para evaluar una presentación de tu curso.",
    extend="Explica por qué un mismo trabajo puede obtener resultados distintos con dos instrumentos y qué harías para decidir.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (decisiones de proceso de ejemplo, inventadas) del trabajo «Vuelo de papel». "
     "Decisión 1: subir el tempo de 90 a 100 pulsos por minuto; evidencia: la pieza sonaba pesada a 90; resultado: suena más ágil, con 1 desfase en 4 pasadas. "
     "Decisión 2: agregar un crescendo en los últimos 4 compases; evidencia: ninguna, fue una idea del momento; resultado: la voz se cansó al final y se revirtió la decisión. "
     "Decisión 3: ensayar con una pausa de silencio entre pasadas; evidencia: dos personas dijeron sentir la voz cansada; resultado: nadie sintió cansancio en la sesión. "
     "Condición nueva: el acto se cambia a una sala más grande, con eco.")
build(
    O6, 3, F,
    use="Aprenderé a evaluar las decisiones tomadas durante un proceso: si tuvieron evidencia, qué resultado dieron y si se revisaron, y a ensayar una evaluación que cambia cuando cambia una condición.",
    prior=["Distingo proceso y resultado.", "Sé usar instrumentos de evaluación.", "Sé revisar una decisión con una condición nueva."],
    explain=[
        "Una decisión de proceso es una elección que el grupo toma mientras trabaja: subir el tempo, cambiar un orden, agregar una pausa. Evaluarla es preguntar tres cosas. Primero, ¿tuvo evidencia? (¿se basó en un dato o en una observación?). Segundo, ¿qué resultado dio? (¿mejoró lo que se quería mejorar?). Tercero, ¿se revisó cuando hizo falta? (¿se mantuvo, se ajustó o se revirtió?). Una buena decisión se apoya en evidencia y se revisa con honestidad.",
        "Una decisión puede ser buena aunque el resultado no mejore. Por ejemplo, el grupo prueba un cambio con buena evidencia y descubre que no sirve: decidió bien, porque probó y revirtió. En cambio, una decisión sin evidencia que sale bien por casualidad no es una buena práctica: no se puede repetir. Evaluar el proceso significa valorar la calidad de las decisiones, no solo si el resultado fue favorable.",
        "Además, una evaluación depende de las condiciones. Si cambia el espacio (más grande, con eco), el público o el tiempo, una decisión que servía puede dejar de servir. Entonces se revisa: se pregunta si la evidencia sigue valiendo y qué habría que probar de nuevo. Revertir una decisión que cansa a una persona también es una decisión buena, porque cuida la salud del grupo.",
    ],
    vocab=[("decisión de proceso", "elección que el grupo toma mientras trabaja"), ("evidencia previa", "dato u observación en que se apoya una decisión"), ("revertir", "volver atrás en una decisión porque no sirvió"),
           ("calidad de una decisión", "grado en que se apoyó en evidencia y se revisó"), ("condición", "circunstancia que puede cambiar, como el espacio"), ("honestidad", "reconocer lo que funcionó y lo que no")],
    worked=[
        ("Evaluar una decisión", "Un grupo de ejemplo quita una repetición porque, al cronometrar, su pieza se pasaba 20 segundos del máximo, y ahora cabe en el tiempo. ¿Fue una buena decisión?",
         ["Se apoyó en evidencia (el cronometraje) y dio un resultado favorable (cabe en el tiempo).", "Fue una buena decisión."],
         "Sí: tuvo evidencia y resultado favorable"),
        ("Decisión buena con resultado nulo", "Un grupo prueba una pausa más larga porque una persona sentía cansancio, y descubre que el cansancio sigue. Revisa y prueba otra cosa. ¿Decidió bien?",
         ["Se apoyó en evidencia y revisó al ver que no servía.", "Decidió bien, aunque el resultado no mejorara a la primera."],
         "Sí, porque probó con evidencia y revisó"),
    ],
    mistakes=[("Evaluar una decisión solo por el resultado final.", "Una decisión sin evidencia puede salir bien por casualidad.", "Pregunta si tuvo evidencia, qué resultado dio y si se revisó."),
              ("Mantener una decisión que cansa a una persona del grupo.", "Se pone el resultado por encima de la salud.", "Revierte la decisión y busca otra que cuide a todas las personas.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una decisión de proceso?', 'Una elección que el grupo toma mientras trabaja', 'La nota final que recibe el grupo al terminar', 'La opinión del público sobre el trabajo presentado', 'La decisión de proceso es lo que el grupo elige en el camino; no es una nota ni una opinión.'),
        ('abc', '{F} ¿En qué evidencia se apoyó la decisión 1?', 'En que sonaba pesada a 90 pulsos por minuto', 'En que fue una idea que surgió en el momento del ensayo', 'En que dos personas dijeron sentir la voz cansada al final', 'La ficha dice que la pieza sonaba pesada a 90 pulsos por minuto.'),
        ('abc', '{F} ¿Qué pasó con la decisión 2?', 'Se revirtió, porque la voz se cansó al final', 'Se mantuvo, porque dio el mejor resultado del trabajo', 'Se aplicó dos veces, porque no tuvo ningún efecto', 'La ficha dice que se revirtió porque la voz se cansó.'),
        ('abc', '{F} ¿Qué decisión tuvo evidencia previa en el cansancio de las personas?', 'La decisión 3, la pausa de silencio entre pasadas', 'La decisión 2, el crescendo de los últimos compases', 'La decisión 1, subir el tempo a 100 pulsos por minuto', 'La decisión 3 se apoyó en que dos personas sentían cansancio.'),
        ('=', '{F} El tempo subió de 90 a 100 pulsos por minuto. ¿Cuántos pulsos más suenan en 3 minutos con el tempo nuevo?', '(100-90)*3', 'Se resta el tempo anterior al nuevo y se multiplica la diferencia por los 3 minutos.', ' pulsos'),
        ('abc', '{F} ¿Por qué la decisión 2 es la menos sólida?', 'Porque no tuvo evidencia y cansó la voz', 'Porque cambió la dinámica de la pieza al final', 'Porque se revirtió antes de la presentación', 'Una decisión sin evidencia que causa cansancio es la menos sólida.'),
        ('abc', '{F} ¿Qué valoración merece que el grupo revirtiera la decisión 2?', 'Es una buena práctica, porque cuidó a las personas', 'Es un error, porque revertir indica falta de decisión', 'Es irrelevante, porque el resultado final fue bueno', 'Revertir una decisión que cansa es una decisión buena para el grupo.'),
        ('=', '{F} A 100 pulsos por minuto, ¿cuántos segundos duran 10 pulsos?', '10*60//100', 'Se multiplican los pulsos por 60 y se divide por los pulsos por minuto.', ' s'),
        ('abc', '{F} Con la condición nueva (sala grande con eco), ¿qué decisión conviene revisar primero?', 'El tempo, porque el eco puede confundir 100 pulsos', 'La pausa de silencio, porque el eco la vuelve inútil del todo', 'El saludo, porque no se oye en una sala grande con eco', 'Un eco puede confundir un pulso rápido, así que conviene probar el tempo.'),
        ('abc', '{F} Un estudiante dice: «la decisión 2 fue buena, porque el crescendo suena lindo». ¿Qué respuesta es correcta?', 'No tuvo evidencia y cansó la voz, así que no fue buena', 'Tiene razón, porque lo que suena lindo siempre justifica la decisión tomada', 'No tiene razón, porque los crescendos no se pueden evaluar en un proceso', 'La calidad de una decisión incluye evidencia y cuidado, no solo cómo suena.'),
        ('abc', '{F} El grupo prueba en la sala grande y descubre que a 100 pulsos suena confuso. ¿Qué decisión de proceso es la más adecuada?', 'Probar 90 y 100 por separado en esa sala y registrar el efecto', 'Mantener 100 porque era la decisión del ensayo anterior', 'Cambiar tempo, dinámica y orden de las piezas al mismo tiempo', 'Probar por separado permite saber qué decisión sirve en la nueva condición.'),
        ('abc', 'Una estudiante dice: «una decisión sin evidencia que sale bien es una buena práctica». ¿Qué observación corresponde?', 'No se puede repetir ni explicar, así que no es buena práctica', 'Es una buena práctica, porque lo importante es el resultado final', 'Es una buena práctica, porque nadie puede evaluar la suerte de un grupo', 'Una buena práctica se puede explicar y repetir con evidencia.'),
        ('=', '{F} El grupo ensaya 4 pasadas de 3 minutos cada una, con una pausa de 1 minuto entre pasadas. ¿Cuántos minutos dura la sesión?', '4*3+3*1', 'Se suman las cuatro pasadas y las tres pausas que hay entre ellas.', ' minutos'),
    ],
    ctx=('abc', 'Después del ensayo, una persona de tu grupo dice que su voz está muy cansada, aunque el resultado mejoró. ¿Qué decisión de proceso es la mejor?', 'Dar descanso y revisar el plan, aunque el resultado mejoró', 'Seguir con el mismo plan de ensayo, porque el resultado mejoró', 'Pedirle que cante más bajo para no molestar al grupo en el ensayo', 'Cuidar la salud del grupo es parte de evaluar bien un proceso.'),
    sc=[
        ("En Interpretación musical: ¿qué es revertir una decisión?", "Volver atrás en una decisión porque no sirvió", "Revertir es parte de un proceso honesto."),
        ('abc', 'Una buena decisión de proceso:', 'Se apoya en evidencia y se revisa', 'Siempre mejora el resultado final del grupo', 'Nunca se cambia después de tomarla', 'La calidad depende de la evidencia y la revisión.'),
        ("¿Por qué se revisa una decisión si cambia el espacio?", "Porque la evidencia anterior puede dejar de valer", "Cambiar de espacio cambia cómo suena la pieza."),
    ],
    op=("Con la {F}, evalúa las tres decisiones de proceso: para cada una escribe si tuvo evidencia, qué resultado dio y si se revisó. Luego escribe qué probarías primero en la sala grande con eco, y qué registrarías.",
        "Decisión 1: tuvo evidencia (sonaba pesada a 90), resultado favorable, se mantuvo. Decisión 2: no tuvo evidencia, cansó la voz y se revirtió. Decisión 3: tuvo evidencia (dos personas con cansancio), resultado favorable, se mantuvo. En la sala grande probaría primero el tempo (90 y 100 por separado) y registraría cuál se oye más claro.",
        ["evalúa las tres decisiones con tres preguntas", "cita la evidencia de la ficha", "propone qué probar con la condición nueva", "dice qué registrará"],
        ["hoja con las tres decisiones evaluadas y el plan de prueba"],
        ["evaluar solo por el resultado", "no usar la evidencia de la ficha", "cambiar varias cosas a la vez"],
        "Pregunta: «¿en qué evidencia se apoyó esa decisión?». Si no la hay, pídele que lo anote."),
    reinforce="Escribe tres decisiones de un proceso inventado y evalúa cada una según evidencia, resultado y revisión.",
    extend="Explica un caso en que una decisión buena no mejora el resultado y por qué sigue siendo una buena decisión.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (comentarios de pares de ejemplo, inventados) sobre la presentación de «Vuelo de papel». "
     "Protocolo del curso: dos logros con evidencia y una sugerencia concreta y posible; se habla de lo que se oyó, no de la persona; quien recibe agradece y pregunta si algo no se entiende. "
     "Comentario 1: «Me gustó cómo la guitarra bajó cuando entró la voz, porque se entendió la letra; y el final fue limpio. Sugiero practicar la entrada del compás 5 con pulso contado». "
     "Comentario 2: «Estuvo bien, pero se nota que no practicaron». "
     "Comentario 3: «Tocas mal la percusión; deberías dejar eso a otra persona». "
     "Dato: en 4 pasadas hubo 1 desfase, en la entrada del compás 5.")
build(
    O6, 4, F,
    use="Aprenderé a evaluar el trabajo de pares con un protocolo (dos logros y una sugerencia con evidencia), a revisar la calidad de un comentario y a recibir una evaluación con respeto.",
    prior=["Sé evaluar con criterios y evidencia.", "Sé distinguir juicios sobre la obra y sobre la persona.", "Sé reconocer sesgos al opinar."],
    explain=[
        "Evaluar a pares es valorar el trabajo de personas de tu mismo nivel para ayudarles a mejorar. Un protocolo ayuda a hacerlo bien: dos logros con evidencia y una sugerencia concreta y posible. Un logro con evidencia dice qué funcionó y por qué («la guitarra bajó cuando entró la voz, y se entendió la letra»). Una sugerencia concreta dice qué hacer («practicar la entrada del compás 5 con pulso contado»). Sin evidencia, un elogio o una crítica queda en opinión.",
        "Un comentario de calidad se revisa con cuatro preguntas. ¿Se refiere a lo que se oyó? ¿Cita un dato comprobable? ¿Propone un cambio posible? ¿Trata con respeto a las personas? Un comentario como «se nota que no practicaron» no cita un dato y supone algo que no se vio; uno como «tocas mal» ataca a la persona. Ambos pueden reformularse con evidencia y respeto.",
        "Recibir una evaluación también es una habilidad. Se escucha sin interrumpir, se agradece, se pregunta si algo no se entiende y se decide qué se usará y qué no. Si un comentario hiere o humilla, no hay que quedarse con él: se pide apoyo a una persona adulta de confianza. Evaluar a pares exige cuidar la relación, porque se quiere ayudar a mejorar el trabajo y no dañar a nadie.",
    ],
    vocab=[("pares", "personas de tu mismo nivel que evalúan o son evaluadas"), ("protocolo", "orden acordado para dar una evaluación"), ("logro con evidencia", "algo que funcionó, apoyado en un dato"),
           ("sugerencia concreta", "cambio claro y posible que se propone"), ("reformular", "decir lo mismo con evidencia y respeto"), ("retroalimentación", "información que ayuda a mejorar un trabajo")],
    worked=[
        ("Revisar un comentario", "Un comentario de ejemplo dice: «tocaste mal, deberías dejar la guitarra». ¿Cumple el protocolo?",
         ["No cita evidencia sobre lo que se oyó y ataca a la persona.", "No cumple el protocolo."],
         "No cumple: ataca a la persona y no cita evidencia"),
        ("Reformular", "Se quiere reformular «se nota que el grupo no se escucha». Dato de ejemplo: en 2 de 4 pasadas la guitarra entró un pulso tarde. ¿Cómo queda con evidencia y sugerencia?",
         ["Se reemplaza la suposición por un dato: la guitarra entró un pulso tarde en 2 de 4 pasadas.", "Se agrega una sugerencia: contar cuatro pulsos antes de entrar."],
         "«La guitarra entró un pulso tarde en 2 de 4 pasadas; sugiero contar cuatro pulsos antes de entrar»"),
    ],
    mistakes=[("Decir «estuvo bien» como única retroalimentación.", "No dice qué funcionó ni qué mejorar.", "Cita un logro con evidencia y una sugerencia concreta."),
              ("Responder a un comentario duro con otro comentario duro.", "Se escala la situación y se daña la relación.", "Agradece, pregunta y, si hiere, pide apoyo a una persona adulta.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una sugerencia concreta?', 'Un cambio claro y posible que se propone para mejorar', 'Una opinión general sobre el trabajo de otra persona', 'Un elogio que no menciona nada de lo que se oyó', 'Una sugerencia concreta dice qué hacer; no es una opinión general ni un elogio vago.'),
        ('abc', '{F} ¿Cuántos logros con evidencia pide el protocolo?', 'Dos, con una sugerencia concreta', 'Uno, sin ninguna sugerencia para mejorar', 'Tres, junto con dos sugerencias generales', 'La ficha pide dos logros con evidencia y una sugerencia.'),
        ('abc', '{F} ¿Qué comentario cumple el protocolo?', 'El comentario 1, con logros y una sugerencia', 'El comentario 2, que dice que todo estuvo bien', 'El comentario 3, que dice cómo tocó la persona evaluada', 'Solo el comentario 1 tiene logros con evidencia y sugerencia.'),
        ('abc', '{F} ¿Qué falla en el comentario 3?', 'Ataca a la persona y no cita lo que se oyó', 'Es demasiado largo para un protocolo de evaluación', 'Menciona dos logros y ninguna sugerencia', 'El comentario 3 juzga a la persona en lugar de describir la ejecución.'),
        ('=', '{F} En 4 pasadas hubo 1 desfase, en una sola pasada. ¿Qué porcentaje de las pasadas salió sin desfase?', '3*100//4', 'Se divide el número de pasadas sin desfase por el total y se multiplica por 100.', ' %'),
        ('abc', '{F} ¿Qué dato respalda la sugerencia del comentario 1?', 'Hubo 1 desfase en la entrada del compás 5', 'El final fue limpio en todas las pasadas', 'La guitarra bajó al entrar la voz', 'El desfase del compás 5 respalda la sugerencia de practicar esa entrada.'),
        ('abc', '{F} ¿Por qué el comentario 2 no sirve para mejorar?', 'No dice qué cambiar y supone algo que no se vio', 'Es muy corto y se lee en pocos segundos', 'Es demasiado elogioso para un trabajo de un curso', 'No cita un dato ni propone un cambio posible.'),
        ('=', '{F} El grupo ensaya la entrada del compás 5 con 3 repeticiones por sesión durante 4 sesiones. ¿Cuántas repeticiones hace en total?', '3*4', 'Se multiplican las repeticiones por la cantidad de sesiones.', ' repeticiones'),
        ('abc', '{F} ¿Cómo se reformula el comentario 2 con evidencia y sugerencia?', 'Hubo 1 desfase; practiquen la entrada con pulso contado', 'No practicaron y por eso el desfase fue de todos los integrantes', 'Estuvo mal y deberían volver a empezar todo desde cero otra vez', 'Se cambia la suposición por un dato y se agrega una sugerencia posible.'),
        ('abc', '{F} La persona que tocó la percusión recibe el comentario 3. ¿Qué respuesta es la más adecuada?', 'Agradecer, pedir un dato y avisar a una persona adulta si la hirió', 'Responder con otro comentario duro para igualar la situación vivida', 'Aceptar sin preguntar que debe dejar la percusión del grupo', 'Se mantiene el respeto, se pide evidencia y se avisa si el comentario hiere.'),
        ('abc', '{F} Un estudiante dice: «mejor no dar sugerencias, porque pueden molestar». ¿Qué observación es correcta?', 'Las sugerencias concretas y respetuosas ayudan a mejorar', 'Tiene razón, porque toda sugerencia molesta a quien la recibe', 'Tiene razón, porque los pares no deben evaluar a otros', 'Una sugerencia concreta y respetuosa es parte de evaluar a pares.'),
        ('abc', '{F} Una persona del curso pide que el comentario 3 se lea en voz alta frente a todas las personas. ¿Qué decisión es adecuada?', 'No leerlo, reformularlo y hablar con una persona adulta', 'Leerlo, porque la verdad no debe ocultarse a nadie', 'Leerlo solo si la persona evaluada no está presente en la sala', 'Un comentario que humilla no se difunde; se reformula y se busca apoyo.'),
        ('=', '{F} Cada comentario completo tiene 2 logros y 1 sugerencia. Si 5 estudiantes dan un comentario completo, ¿cuántos elementos suman en total?', '5*(2+1)', 'Se suman los elementos de cada comentario y se multiplican por cinco estudiantes.', ' elementos'),
    ],
    ctx=('abc', 'Un compañero te pide una opinión sobre su ensayo y sientes que hubo muchos errores. ¿Cómo la das?', 'Con dos logros con evidencia y una sugerencia posible', 'Con una lista de todos los errores sin ningún logro que mencionar', 'Con un «estuvo bien» para evitar problemas con él o ella', 'El protocolo combina logros con evidencia y una sugerencia posible.'),
    sc=[
        ("En Interpretación musical: ¿qué es la retroalimentación?", "Información que ayuda a mejorar un trabajo", "Una buena retroalimentación cita evidencia y propone un cambio."),
        ('abc', 'Un comentario respetuoso se refiere:', 'A lo que se oyó y no a la persona', 'A la persona más que a lo que se oyó', 'A cuánto le cae bien la persona', 'Se evalúa la ejecución, no a quien la hace.'),
        ("¿Qué haces si un comentario te hiere o te humilla?", "Pido apoyo a una persona adulta de confianza", "Se busca ayuda en lugar de responder con otro ataque."),
    ],
    op=("Con la {F}, escribe un comentario para un par con el protocolo: dos logros con evidencia y una sugerencia concreta. Luego reformula el comentario 3 para que cumpla el protocolo y respete a la persona.",
        "Comentario: me gustó que la guitarra bajara cuando entró la voz, porque se entendió la letra; y el final fue limpio. Sugiero practicar la entrada del compás 5 con pulso contado. Reformulación del 3: en la percusión noté un desfase en el compás 5; sugiero ensayar esa entrada con pulso marcado, y puedo ayudar a practicarla.",
        ["escribe dos logros con evidencia", "agrega una sugerencia concreta", "reformula el comentario 3 con respeto", "no ataca a la persona"],
        ["hoja con el comentario y la reformulación"],
        ["elogios sin evidencia", "sugerencia vaga", "mantener el ataque a la persona"],
        "Pregunta: «¿qué se oyó que respalde ese logro?». Si no lo dice, pídele que lo busque en la ficha."),
    reinforce="Escribe un comentario de pares de tres frases para una pieza inventada y revísalo con las cuatro preguntas de calidad.",
    extend="Explica cómo cambiarías el protocolo si evaluaras a una persona que está muy nerviosa por presentarse.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 5 (autoevaluación de ejemplo, inventada) de Max, que toca percusión de mesa en «Vuelo de papel». "
     "Datos: en 4 pasadas hubo 1 desfase en su entrada del compás 5; el cansancio en las manos apareció en la pasada 4; ensayó 3 veces por semana durante 2 semanas, 20 minutos por vez. "
     "Logros: mantuvo el tempo de 100 pulsos por minuto; sus golpes fueron parejos. "
     "Por mejorar: la entrada del compás 5; el cansancio de las manos. "
     "Plan de mejora de ejemplo: meta, 0 desfases en 4 pasadas en 2 semanas; acciones, contar cuatro pulsos antes de entrar y calentar las manos 5 minutos; evidencia, el registro de pasadas de cada ensayo; control de salud, descansar las manos 1 minuto entre pasadas.")
build(
    O6, 5, F,
    use="Aprenderé a autoevaluar mi trabajo con datos, a formular un plan de mejora con meta, acciones y evidencia, y a cuidar mi salud (manos, voz y oído) mientras mejoro.",
    prior=["Sé evaluar con criterios y evidencia.", "Sé evaluar a pares con respeto.", "Sé que el descanso es parte del trabajo."],
    explain=[
        "La autoevaluación es evaluar el propio trabajo con la misma exigencia y el mismo respeto con que se evalúa el de otra persona. Se parte de datos (cuántos desfases, cuánto ensayó, qué sintió) y se separan los logros de lo que se puede mejorar. Una autoevaluación honesta no se castiga ni se adorna: no dice «soy malo» ni «todo está perfecto», sino «mantuve el tempo y me falta precisión en una entrada».",
        "Un plan de mejora transforma lo que se puede mejorar en una acción. Tiene cuatro partes: una meta concreta y medible con plazo («bajar de 3 a 1 desfase en 4 pasadas en 2 semanas»), acciones (qué haré: ensayar la entrada despacio, con palmas que marquen el pulso), evidencia (cómo sabré que funcionó: una tabla con los desfases de cada pasada) y control de salud (cómo cuidaré el cuerpo: calentar, descansar, bajar el volumen). Una meta que no se puede medir no se puede evaluar después.",
        "Un plan se revisa. Si la meta no se alcanza, se pregunta qué se aprendió y qué se cambia, sin culpa. Si el cuerpo avisa (dolor, cosquilleo, cansancio fuerte), se baja la exigencia y se pide orientación a una persona adulta de confianza; no se sigue «hasta lograrlo». Mejorar significa avanzar de manera sostenida y segura, no más rápido a cualquier costo.",
    ],
    vocab=[("autoevaluación", "evaluación del propio trabajo con datos"), ("meta medible", "objetivo que se puede contar o comprobar, con plazo"), ("plan de mejora", "meta, acciones, evidencia y control de salud"),
           ("evidencia de avance", "dato que muestra que la mejora ocurrió"), ("control de salud", "cuidado del cuerpo mientras se mejora"), ("sostenido", "que se mantiene en el tiempo sin exigirse en exceso")],
    worked=[
        ("Medir una meta", "Una meta de ejemplo dice: «tocar mejor». ¿Es medible? Reescríbela con un dato y un plazo.",
         ["«Tocar mejor» no se puede contar ni comprobar.", "Una versión medible: «mantener el tempo en 3 de 4 pasadas durante 1 semana»."],
         "No es medible; «mantener el tempo en 3 de 4 pasadas durante 1 semana»"),
        ("Revisar un plan", "Un plan de ejemplo propone ensayar 2 horas al día sin descanso para alcanzar la meta. ¿Qué falla?",
         ["No incluye control de salud: dos horas sin descanso exigen demasiado a manos y voz.", "Se corrige con sesiones cortas y pausas."],
         "Falta el control de salud: se corrige con sesiones cortas y pausas"),
    ],
    mistakes=[("Escribir una meta general como «ser mejor».", "No se puede medir ni revisar.", "Escribe una meta con un número y un plazo."),
              ("Seguir ensayando con dolor para cumplir la meta a tiempo.", "Se pone la meta por encima del cuerpo.", "Baja la exigencia, descansa y pide orientación a una persona adulta.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una meta medible?', 'Un objetivo que se puede contar, con plazo', 'Un deseo general de mejorar sin definir ningún plazo ni dato', 'La opinión de otra persona sobre el trabajo propio realizado', 'Una meta medible tiene un dato y un plazo.'),
        ('abc', '{F} ¿Qué logro menciona Max?', 'Mantuvo el tempo de 100 pulsos y sus golpes fueron parejos', 'No tuvo ningún desfase en las cuatro pasadas del ensayo', 'Ensayó 3 veces por semana durante todo un mes completo', 'La ficha dice que mantuvo el tempo y que sus golpes fueron parejos.'),
        ('abc', '{F} ¿Qué dato de salud menciona la autoevaluación?', 'El cansancio en las manos apareció en la pasada 4', 'La voz se cansó mucho en la pasada 2 del ensayo', 'El oído molestó durante todo el ensayo del grupo', 'La ficha dice que el cansancio en las manos apareció en la pasada 4.'),
        ('abc', '{F} ¿Cuál es la meta del plan de mejora?', '0 desfases en 4 pasadas en 2 semanas', 'Ensayar 2 horas por día sin ninguna pausa', 'Tocar más fuerte en el compás 5 de la pieza', 'La ficha define la meta con un dato y un plazo.'),
        ('=', '{F} Max ensayó 3 veces por semana durante 2 semanas, 20 minutos por vez. ¿Cuántos minutos ensayó en total?', '3*2*20', 'Se multiplican las veces por semana, las semanas y los minutos de cada vez.', ' minutos'),
        ('abc', '{F} ¿Qué acción del plan apunta a corregir la entrada del compás 5?', 'Contar cuatro pulsos antes de entrar', 'Calentar las manos 5 minutos antes de cada ensayo', 'Descansar las manos 1 minuto entre pasadas', 'Contar pulsos antes de entrar ayuda a sincronizar la entrada.'),
        ('abc', '{F} ¿Qué evidencia mostrará que el plan funcionó?', 'El registro de pasadas de cada ensayo', 'La opinión de que se siente más seguro', 'La cantidad de horas dormidas cada noche', 'La evidencia del plan es el registro de pasadas.'),
        ('=', '{F} Si el plan incluye 1 minuto de descanso entre pasadas y se hacen 4 pasadas, ¿cuántos minutos de descanso hay por sesión? (Hay un descanso entre cada par de pasadas.)', '3*1', 'Con cuatro pasadas hay tres descansos entre ellas.', ' minutos'),
        ('abc', '{F} Una meta dice «tocar mejor». ¿Qué problema tiene?', 'No se puede contar ni comprobar', 'Es demasiado exigente para el plazo', 'Es demasiado específica para un plan', 'Una meta sin dato ni plazo no se puede revisar después.'),
        ('abc', '{F} Max siente dolor en las manos en el ensayo 5. ¿Cuál es la mejor decisión?', 'Detener el ensayo, descansar y pedir orientación a una persona adulta', 'Seguir hasta cumplir la meta para no atrasarse con el plan', 'Tocar más fuerte para pasar rápido el dolor de las manos', 'Ante dolor se detiene y se pide orientación; no se fuerza.'),
        ('abc', '{F} Al cabo de 2 semanas Max logra 0 desfases en las pasadas 1 a 3, pero en la pasada 4 vuelve el cansancio de manos y hay 1 desfase. ¿Qué evaluación honesta hace?', 'Reconoce lo logrado en tres pasadas y ajusta una acción, como más descanso antes de la pasada 4', 'Fracasó por completo y no debe seguir ensayando más', 'Alcanzó la meta, porque 1 desfase es casi cero de verdad', 'Reconoce lo logrado y ajusta una cosa, sin culpa y sin adornar el dato.'),
        ('abc', 'Una estudiante escribe: «mi plan es ensayar 3 horas seguidas todos los días». ¿Qué falla?', 'No incluye control de salud y exige demasiado', 'Es demasiado corto para lograr una mejora sostenida en el tiempo', 'No menciona ningún nombre de instrumento ni de pieza', 'Un plan sostenible incluye pausas y control de salud.'),
        ('=', '{F} Si Max hace 4 pasadas por sesión y 3 sesiones por semana, ¿cuántas pasadas hace en las 2 semanas del plan?', '4*3*2', 'Se multiplican las pasadas por las sesiones semanales y por las semanas.', ' pasadas'),
    ],
    ctx=('abc', 'Tienes una presentación en 2 semanas y notas que una entrada te sale mal. ¿Qué plan de mejora es más adecuado?', 'Una meta medible, acciones, un registro y pausas', 'Ensayar sin límite hasta que salga, aunque duela mucho', 'Esperar a la presentación para ver qué pasa con la entrada', 'Un plan completo incluye meta, acciones, evidencia y salud.'),
    sc=[
        ("En Interpretación musical: ¿qué es la autoevaluación?", "La evaluación del propio trabajo con datos", "Se hace con la misma exigencia y respeto que a otra persona."),
        ('abc', 'Un plan de mejora completo tiene:', 'Meta, acciones, evidencia y control de salud', 'Solo una lista de deseos de mejora', 'Solo la opinión de un compañero del curso', 'Las cuatro partes permiten medir y cuidar.'),
        ("¿Qué haces si sientes dolor mientras ensayas?", "Detengo el ensayo, descanso y pido orientación", "La salud va primero y el dolor se atiende."),
    ],
    op=("Con la {F}, escribe tu propio plan de mejora para una entrada de un trabajo de tu curso (o para la de Max): meta medible con plazo, dos acciones, la evidencia que usarás y una medida de control de salud.",
        "Meta: 0 desfases en 4 pasadas en 2 semanas. Acciones: contar cuatro pulsos antes de entrar y practicar la entrada 3 veces por sesión. Evidencia: registrar los desfases de cada ensayo. Control de salud: calentar las manos 5 minutos y descansar 1 minuto entre pasadas; si aparece dolor, detener el ensayo.",
        ["meta con dato y plazo", "dos acciones concretas", "evidencia verificable", "medida de control de salud"],
        ["hoja con el plan de mejora completo"],
        ["meta general sin número", "olvidar el control de salud", "evidencia vaga"],
        "Pregunta: «¿cómo sabrás si la meta se cumplió?». Si no puede responder, pídele que agregue un dato medible."),
    reinforce="Escribe una autoevaluación de tres frases con un logro y algo por mejorar, usando un dato de un ensayo inventado.",
    extend="Explica por qué una meta medible puede motivar más que una meta general, y qué cuidado de salud agregarías.",
)
