"""Lectura y escritura especializadas (electivo 3.º y 4.º medio HC): OAC-03 (registrar y procesar información, clases 1 a 5) y OAC-04 (construir y transformar el conocimiento por escrito, clases 1 a 5)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno (o un procesador de texto, si lo tienes). Todos los textos, fichas, tablas y fuentes de los ejercicios están escritos en el enunciado y son originales y de ejemplo: no necesitas internet ni libros. "
             "En la actividad abierta trabajas con los insumos que la propia actividad entrega. Si ocupas un computador o un celular, no compartas datos personales ni subas textos ajenos sin permiso.")
build = make_build(MATERIALS)

O3 = "LL-LEES-3y4-OAC-03"
O4 = "LL-LEES-3y4-OAC-04"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (tareas y estrategias de ejemplo). Tarea P: memorizar definiciones clave de un capítulo para una prueba. "
     "Tarea Q: comparar tres estudios sobre un mismo tema según su método y sus resultados. "
     "Tarea R: reunir citas textuales y datos con su fuente para un ensayo. "
     "Tarea S: comprender cómo se relacionan cinco conceptos de una lectura. "
     "Estrategias: glosario con tarjetas (E1), cuadro comparativo (E2), ficha de contenido con datos de la fuente (E3) y mapa conceptual (E4).")
build(
    O3, 1, F,
    use="Aprenderé a elegir una estrategia para registrar información (apuntes, fichas, cuadros, mapas, glosarios) según el propósito y el tipo de texto. Sirve para no perder datos y para usarlos después al escribir.",
    prior=["Sé subrayar y tomar apuntes.", "Sé qué es una fuente y por qué se atribuye.", "Conozco el propósito y la audiencia de un texto."],
    explain=[
        "Registrar información es dejar por escrito lo que se lee o se observa de modo que se pueda usar después. No existe una estrategia única: depende del propósito. Para memorizar términos sirve un glosario con tarjetas. Para comparar fuentes sirve un cuadro comparativo. Para reunir citas y datos con su origen sirve la ficha de contenido. Para ver cómo se relacionan conceptos sirve un mapa conceptual.",
        "Las estrategias se eligen según tres preguntas: para qué usaré esta información, qué tipo de texto estoy leyendo y qué parte necesito conservar. En un texto impreso se anotan las páginas; en un texto digital se anotan la dirección y la fecha de consulta. En ambos se separa con claridad lo que dice la fuente de lo que yo pienso, para no confundir ideas ajenas con propias.",
        "Una buena anotación es breve, precisa y recuperable: se entiende semanas después y permite volver a la fuente. Anotar todo, sin criterio, produce montones de apuntes inútiles; anotar demasiado poco obliga a releer. Decidir qué registrar según el tema, el propósito de escritura y las convenciones del género es parte del trabajo especializado.",
    ],
    vocab=[("registrar", "dejar por escrito información para usarla después"), ("ficha de contenido", "tarjeta con una idea o dato, su fuente y su tipo (cita, paráfrasis o comentario)"), ("cuadro comparativo", "tabla que compara fuentes o ideas según criterios"), ("mapa conceptual", "esquema que une conceptos con palabras de enlace"), ("glosario", "lista de términos con su definición")],
    worked=[
        ("Elegir según el propósito", "Debes comparar dos informes sobre el uso de bicicletas según su muestra y su resultado. ¿Qué estrategia eliges?",
         ["El propósito es comparar dos fuentes según criterios.", "El cuadro comparativo ordena las fuentes en columnas y los criterios en filas."],
         "Cuadro comparativo"),
        ("Elegir y justificar", "Debes recordar el significado de siete términos nuevos de una lectura. ¿Qué estrategia eliges y por qué?",
         ["El propósito es memorizar definiciones.", "Un glosario con tarjetas permite repasar término y definición."],
         "Glosario con tarjetas"),
    ],
    mistakes=[("Copiar el texto completo «por si acaso».", "Se registra demasiado, sin criterio, y no se distingue lo importante.", "Decide primero el propósito y anota solo lo que sirve para él, con su fuente."),
              ("Anotar un dato sin escribir de dónde sale.", "Después no se puede citar ni verificar.", "Agrega siempre autor, año, título y página o dirección con fecha de consulta.")],
    T=[
        ("abc", "{F} ¿Qué estrategia conviene para la tarea P?", "Glosario con tarjetas (E1)", "Mapa conceptual (E4)", "Cuadro comparativo (E2)", "Memorizar definiciones se apoya en tarjetas con término y definición."),
        ("abc", "{F} ¿Qué estrategia conviene para la tarea Q?", "Cuadro comparativo (E2)", "Glosario con tarjetas (E1)", "Mapa conceptual (E4)", "Comparar estudios según método y resultados se ordena en filas y columnas."),
        ("ab", "En Lengua: ¿qué es una ficha de contenido?", "Una tarjeta con una idea o dato, su fuente y si es cita, paráfrasis o comentario", "Una lista de palabras con su significado", "La ficha de contenido conserva el dato con su origen; la lista de palabras es un glosario."),
        ("abc", "{F} ¿Qué estrategia conviene para la tarea R?", "Ficha de contenido con datos de la fuente (E3)", "Glosario con tarjetas (E1)", "Mapa conceptual (E4)", "Las citas y datos para un ensayo requieren conservar la fuente de cada uno."),
        ("abc", "{F} ¿Qué estrategia conviene para la tarea S?", "Mapa conceptual (E4)", "Ficha de contenido (E3)", "Cuadro comparativo (E2)", "Mostrar relaciones entre conceptos es lo que hace un mapa conceptual."),
        ("ab", "Un estudiante anota una cifra y escribe solo «según la lectura». ¿Qué le falta?", "Los datos de la fuente: autor, año, título y página o dirección", "Un subrayado más grueso", "Sin datos de la fuente no puede citarla ni volver a verificarla."),
        ("abc", "Un texto digital se registra con dirección y fecha de consulta; uno impreso, con número de página. ¿Por qué se anota la fecha de consulta en lo digital?", "Porque la página puede cambiar o desaparecer", "Para saber cuándo se escribió el trabajo del estudiante", "Porque sin fecha no se puede anotar el autor", "Un sitio digital se modifica, y la fecha indica qué versión se leyó."),
        ("abc", "{F} Para la tarea Q, ¿cómo conviene organizar el cuadro comparativo de los tres estudios?", "Una columna por estudio y una fila por criterio, como el método y los resultados", "Una sola columna con los tres estudios mezclados", "Una fila por estudio y ningún criterio rotulado", "El cuadro ordena las fuentes en columnas y los criterios en filas, para leer cada criterio de lado a lado."),
        ("ab", "Una compañera dice que siempre conviene la misma estrategia, el subrayado. ¿Es correcto?", "No: la estrategia depende del propósito de uso", "Sí: subrayar sirve para todo", "Distintos propósitos (memorizar, comparar, citar) piden distintas estrategias."),
        ("abc", "{F} Para la tarea R, ¿cuál de estas fichas está bien hecha?", "Dato: «40 % de los estudiantes llega en bicicleta». Fuente: Muestra (2022), Informe escolar, p. 4. Tipo: cita textual", "Dato: «mucha gente llega en bicicleta»", "Fuente: informe escolar. Dato: sin anotar", "La primera tiene dato preciso, fuente completa y tipo de nota."),
        ("abc", "Un estudiante anota todo un capítulo, copiando cada oración, para escribir un informe de una página. ¿Qué problema tiene?", "Registra demasiado sin criterio y no distingue lo útil", "Registra muy poco", "No cita a nadie", "Registrar según el propósito evita acumular apuntes que no se usarán."),
        ("abc", "{F} Una estudiante resuelve la tarea P con un cuadro comparativo de tres columnas. ¿Qué problema tiene esa elección?", "El cuadro sirve para comparar fuentes, pero P pide memorizar términos y definiciones", "Tiene demasiadas columnas para una prueba", "Debió usar una ficha de contenido, porque P pide reunir citas", "Cada propósito pide su estrategia: memorizar términos se apoya en un glosario con tarjetas."),
        ("abc", "{F} Un estudiante debe, a la vez, comparar tres estudios (Q) y reunir citas para su ensayo (R). ¿Qué plan es más razonable?", "Usar un cuadro comparativo para Q y fichas de contenido para R", "Usar un único mapa para ambos", "Anotar todo sin estrategia", "Cada propósito pide su estrategia; no hay una sola herramienta para ambos."),
    ],
    ctx=("abc", "Una estudiante prepara un informe sobre el sueño y debe guardar tres datos de un artículo en línea para citarlos. ¿Qué anotación conviene?", "Cada dato con autor, título, dirección y fecha de consulta", "Solo los datos sin su origen", "Solo el título del sitio", "Los datos sin fuente no se pueden citar; la fecha indica qué versión leyó."),
    sc=[
        ("En Lengua: ¿de qué depende la estrategia de registro?", "Del propósito de uso de la información", "Para qué se usará la información decide cómo se registra."),
        ("¿Qué estrategia ordena la comparación de varias fuentes?", "El cuadro comparativo", "Filas y columnas permiten comparar por criterios."),
        ("¿Qué dato no debe faltar al anotar información?", "La fuente de donde viene", "Sin la fuente no se puede citar ni verificar."),
    ],
    op=("Elige una de estas situaciones: A) memorizar siete términos de una lectura sobre el ahorro de agua, B) comparar dos informes sobre horarios de sueño, C) reunir citas para un ensayo sobre el uso del celular en clases. Escribe: (1) la estrategia que elegiste, (2) por qué, (3) una muestra de dos anotaciones con sus datos de fuente (puedes inventar la fuente, rotulada «de ejemplo»).",
        "Situación B. Estrategia: cuadro comparativo. Razón: debo comparar dos informes según criterios. Muestra: Informe 1 (Pérez, 2022, de ejemplo): 30 estudiantes, duermen 7 horas. Informe 2 (Soto, 2021, de ejemplo): 45 estudiantes, duermen 8 horas.",
        ["la estrategia coincide con el propósito", "justifica con una razón", "las anotaciones incluyen datos de fuente"],
        ["mini cuadro o ficha con dos anotaciones"],
        ["anotar sin fuente", "elegir una estrategia que no corresponde al propósito", "no justificar"],
        "Pregunta: «¿cómo usarás esta anotación al escribir?»."),
    reinforce="Elige una estrategia para cada propósito: memorizar términos, comparar tres fuentes y reunir citas con su fuente, y justifica cada elección en una línea.",
    extend="Explica qué ventajas y qué riesgos tiene registrar información solo en el computador respecto del papel.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (fuente y notas de ejemplo). Fuente: Rojas, M. (2021). El uso del agua en los barrios. Editorial Ejemplo. Informe de ejemplo, p. 12. "
     "Texto de la p. 12: «De las 80 casas encuestadas, 50 contaban con medidor propio; el consumo promedio fue de 15 metros cúbicos por mes». "
     "Nota 1: «De 80 casas, 50 tenían medidor propio (Rojas, 2021, p. 12)». "
     "Nota 2: «“De las 80 casas encuestadas, 50 contaban con medidor propio” (Rojas, 2021, p. 12)». "
     "Nota 3: «Parece poco, quizás habría que investigar por qué (idea mía)».")
build(
    O3, 2, F,
    use="Aprenderé a hacer fichas bibliográficas y de contenido: datos de la fuente, cita textual, paráfrasis y comentario propio. Sirve para registrar sin confundir ideas ajenas y propias.",
    prior=["Sé elegir una estrategia de registro.", "Sé qué es una cita y una paráfrasis.", "Sé por qué se atribuye una idea."],
    explain=[
        "Una ficha bibliográfica registra los datos de la fuente: autor, año, título, tipo de fuente, editorial o sitio, y, si es digital, la dirección y la fecha de consulta. Esos datos permiten volver a la fuente y citarla. Una ficha de contenido registra una idea o un dato de esa fuente y conviene indicar de qué tipo es: cita textual, paráfrasis o comentario propio.",
        "La cita textual copia palabras exactas entre comillas, con autor, año y página. La paráfrasis reescribe la idea con palabras propias, conserva los datos y también lleva la fuente. El comentario propio es una idea de quien escribe y se marca como tal («idea mía») para no confundirla con la fuente. Separar los tres tipos evita el plagio involuntario cuando después se redacta el texto.",
        "Una buena ficha de contenido tiene un solo dato o idea, está rotulada con una palabra clave del tema y remite a la ficha bibliográfica. Así se puede reordenar y reutilizar en distintos textos. Una ficha que mezcla varias ideas, o que no distingue lo ajeno de lo propio, es poco útil.",
    ],
    vocab=[("ficha bibliográfica", "tarjeta con los datos para identificar una fuente"), ("cita textual", "copia exacta entre comillas, con fuente y página"), ("paráfrasis", "idea ajena con palabras propias y fuente"), ("comentario propio", "idea de quien escribe, marcada como tal"), ("fecha de consulta", "día en que se leyó una fuente digital")],
    worked=[
        ("Completar una ficha bibliográfica", "Fuente impresa de ejemplo: autor Soto, año 2020, título «Huertos escolares», editorial Ejemplo. ¿Qué datos hay y cuál falta para citar una afirmación concreta?",
         ["Hay autor, año, título y editorial.", "Falta la página de donde se tomó la afirmación."],
         "Falta la página"),
        ("Clasificar una nota", "Nota: «Soto (2020, p. 8) señala que 20 de 30 cursos tenían huerto». ¿Es cita, paráfrasis o comentario?",
         ["No usa comillas, así que no es cita textual.", "Reescribe la idea con la fuente y la página."],
         "Paráfrasis"),
    ],
    mistakes=[("Poner en la misma ficha una cita y una opinión sin separarlas.", "Después no se sabe qué es de la fuente y qué es propio.", "Haz fichas distintas o marca «idea mía» en el comentario."),
              ("Citar sin página porque «es de un sitio web».", "Aunque no tenga página, se anotan dirección y fecha de consulta.", "Registra dirección y fecha de consulta en fuentes digitales y página en impresas.")],
    T=[
        ("abc", "{F} ¿Cuál de las notas es una cita textual?", "La nota 2", "La nota 1", "La nota 3", "La nota 2 copia las palabras exactas entre comillas y con página."),
        ("abc", "{F} ¿Cuál de las notas es una paráfrasis?", "La nota 1", "La nota 2", "La nota 3", "La nota 1 reescribe la idea con otras palabras y mantiene los datos y la fuente."),
        ("abc", "{F} ¿Cuál de las notas es un comentario propio?", "La nota 3", "La nota 1", "La nota 2", "La nota 3 incluye «idea mía» y no atribuye nada a la fuente."),
        ("=", "{F} Según la fuente, ¿qué porcentaje de las 80 casas encuestadas tenía medidor propio? Divide 50 entre 80 y multiplica por 100.", "50/80*100", "50 de 80 equivale a 62,5 de cada 100 casas.", " %"),
        ("ab", "En Lengua: ¿qué datos lleva una ficha bibliográfica?", "Autor, año, título, tipo de fuente y editorial o sitio", "Solo el tema del texto", "La ficha bibliográfica identifica la fuente para poder encontrarla y citarla."),
        ("abc", "{F} ¿Qué dato le falta a la ficha bibliográfica para fuente impresa si solo se anotó autor, año y editorial?", "El título", "La página de la que se tomó la idea", "El resumen del libro", "Sin título la fuente no queda identificada con claridad."),
        ("ab", "{F} Un estudiante cambió «50» por «casi la mitad» en la nota 1. ¿Qué problema hay?", "Cambió el dato exacto y ahora la paráfrasis es inexacta", "Está bien: parafrasear permite cambiar datos", "Una paráfrasis debe conservar el sentido y la cifra; 50 de 80 es más que la mitad."),
        ("abc", "Una fuente digital de ejemplo no tiene número de página. ¿Qué datos de ubicación se anotan?", "La dirección del sitio y la fecha de consulta", "Ninguno, porque no se puede citar", "Solo el nombre del buscador", "En lo digital la dirección y la fecha cumplen el papel de la página."),
        ("abc", "{F} Se debe hacer una ficha que contenga a la vez la cita de la nota 2 y la opinión de la nota 3. ¿Qué es lo más adecuado?", "Hacer dos fichas separadas o rotular claramente cada parte", "Unir ambas en una oración sin marcas", "Quitar la fuente de la cita", "Separar lo ajeno de lo propio evita plagio involuntario."),
        ("abc", "{F} ¿Qué rasgo hace de la nota 2 una cita textual y no una paráfrasis?", "Copia palabras exactas entre comillas", "Menciona el año", "Usa un número", "La paráfrasis también tiene año y números; lo propio de la cita son las comillas con palabras exactas."),
        ("abc", "Un estudiante hace una ficha con tres ideas de la fuente y una opinión propia. ¿Qué problema tiene?", "Es difícil de reordenar y mezcla ideas ajenas y propias", "Es demasiado corta", "Tiene demasiadas fuentes", "Una ficha útil lleva una sola idea y distingue su origen."),
        ("abc", "{F} Se parafrasea la fuente así: «Según Rojas (2021, p. 12), casi todas las casas tenían medidor propio». ¿Qué error hay?", "Distorsiona el dato: eran 50 de 80, no casi todas", "No lleva fuente", "Es una cita textual mal hecha", "La paráfrasis debe conservar el dato, y 50 de 80 no es «casi todas»."),
        ("abc", "{F} ¿Cuál de estas fichas bibliográficas está completa para un libro impreso?", "Rojas, M. (2021). El uso del agua en los barrios. Editorial Ejemplo", "Rojas, M. El uso del agua en los barrios. Editorial Ejemplo", "Rojas, M. (2021). Editorial Ejemplo", "La primera tiene autor, año, título y editorial; las otras omiten el año o el título."),
    ],
    ctx=("abc", "Una estudiante leyó en línea un artículo de ejemplo del autor Díaz (2023). Quiere guardar el dato «el 30 % del grupo estudia con música» para citarlo. ¿Qué ficha conviene?", "Dato, autor, año, título, dirección y fecha de consulta, rotulada como paráfrasis", "Solo el dato", "Solo el nombre del autor", "Para citar un dato digital se necesita su origen completo y el tipo de nota."),
    sc=[
        ("En Lengua: ¿qué tres tipos de nota hay en una ficha de contenido?", "Cita textual, paráfrasis y comentario propio", "Los tres tipos permiten separar lo ajeno de lo propio."),
        ("¿Qué lleva una cita textual?", "Comillas, palabras exactas, fuente y página", "La cita conserva las palabras de la fuente."),
        ("¿Qué debe conservar una paráfrasis?", "El sentido y los datos de la fuente", "Cambiar palabras no autoriza a cambiar el sentido."),
    ],
    op=("Con esta fuente de ejemplo: Torres, L. (2022). Estudiar con música. Editorial Ejemplo, p. 5: «De los 60 estudiantes consultados, 24 prefieren estudiar con música; los demás, en silencio». Haz tres fichas de contenido: una cita textual, una paráfrasis y un comentario propio, y una ficha bibliográfica completa.",
        "Bibliográfica: Torres, L. (2022). Estudiar con música. Editorial Ejemplo. Cita: «De los 60 estudiantes consultados, 24 prefieren estudiar con música» (Torres, 2022, p. 5). Paráfrasis: según Torres (2022, p. 5), 24 de 60 prefieren estudiar con música. Comentario: parece una minoría; revisar si hay datos por curso (idea mía).",
        ["ficha bibliográfica con autor, año, título y editorial", "cita con comillas, año y página", "paráfrasis con el dato exacto y comentario marcado como propio"],
        ["cuatro fichas"],
        ["cita sin comillas", "paráfrasis con el dato cambiado", "comentario sin marcar como propio"],
        "Pregunta: «¿qué parte de esta ficha es de la fuente y cuál es tuya?»."),
    reinforce="Convierte en paráfrasis, sin cambiar el dato, esta cita de ejemplo: «El 70 % de las familias encuestadas separa el papel» (Vega, 2020, p. 3).",
    extend="Explica por qué las fichas de una sola idea permiten reutilizar la información en textos distintos.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (dos fuentes de ejemplo sobre huertos escolares). Fuente A: «En un liceo con 400 estudiantes, 30 participaron durante tres meses en un huerto escolar; al final, 24 dijeron haber aprendido a cuidar plantas». "
     "Fuente B: «En otro liceo con 600 estudiantes, 90 participaron durante seis meses en un huerto; 63 dijeron haberse sentido más motivados con la asignatura de Ciencias». "
     "Criterios de comparación: tamaño del liceo, participantes, duración y resultado declarado.")
build(
    O3, 3, F,
    use="Aprenderé a procesar la información que registré: resumir, sintetizar y comparar fuentes en un cuadro. Sirve para pasar de datos sueltos a ideas organizadas que se pueden usar en un texto.",
    prior=["Sé hacer fichas de contenido.", "Sé parafrasear con la fuente.", "Sé calcular un porcentaje simple."],
    explain=[
        "Procesar la información es trabajar con lo registrado para entenderlo y usarlo. Tres operaciones frecuentes: resumir una fuente, que es condensar sus ideas principales conservando el sentido; sintetizar varias fuentes, que es integrar lo común y lo distinto en una idea nueva; y comparar, que es poner las fuentes frente a frente según criterios definidos antes.",
        "El cuadro comparativo ordena la comparación: en las filas se ponen los criterios (tamaño, duración, resultado) y en las columnas las fuentes. Se completa con datos exactos y su fuente; luego se leen las filas para ver coincidencias y diferencias. Una diferencia no es un error: a veces se explica por el contexto, como un liceo más grande o un período más largo.",
        "Una síntesis no es la suma de dos resúmenes: relaciona lo que dicen las fuentes y señala qué se concluye y qué no. Si una fuente mide motivación y otra aprendizaje, no se pueden igualar sin cautela. Al comparar porcentajes, hay que verificar que se calculan sobre el mismo total, para no comparar números que no son comparables.",
    ],
    vocab=[("resumen", "versión breve de una fuente con sus ideas principales"), ("síntesis", "integración de varias fuentes en una idea nueva"), ("criterio de comparación", "aspecto según el cual se comparan las fuentes"), ("coincidencia", "rasgo que las fuentes comparten"), ("diferencia", "rasgo en que las fuentes se distinguen")],
    worked=[
        ("Calcular un porcentaje para comparar", "En la fuente A participaron 30 de 400 estudiantes. ¿Qué porcentaje es?",
         ["Se divide 30 entre 400: 0,075.", "Se multiplica por 100: 7,5 %."],
         "7,5 %"),
        ("Distinguir resumen y síntesis", "Un estudiante escribe dos resúmenes seguidos, uno por fuente. Otro escribe: «Ambas experiencias tuvieron resultado positivo, aunque miden aspectos distintos». ¿Quién sintetizó?",
         ["El primero solo suma resúmenes.", "El segundo integra lo común (resultado positivo) y señala una diferencia (qué miden)."],
         "El segundo estudiante"),
    ],
    mistakes=[("Comparar porcentajes calculados sobre totales distintos como si fueran iguales.", "Los porcentajes dependen del total; no son comparables sin verificarlo.", "Calcula todos los porcentajes sobre el mismo criterio antes de compararlos."),
              ("Armar una síntesis que repite cada fuente por separado.", "No relaciona lo común ni lo distinto.", "Une las fuentes con una idea nueva y señala qué se puede y qué no se puede concluir.")],
    T=[
        ("abc", "{F} ¿Cuántos estudiantes participaron en el huerto en la fuente B?", "90", "600", "63", "La fuente B dice que participaron 90; 600 es el total del liceo y 63 los motivados."),
        ("ab", "En Lengua: ¿qué es una síntesis?", "Integrar varias fuentes en una idea nueva", "Copiar la primera fuente", "La síntesis relaciona lo común y lo distinto de varias fuentes."),
        ("abc", "{F} ¿Cuál de estas filas NO forma parte de los criterios de comparación de la ficha?", "Costo del huerto", "Duración", "Participantes", "Los criterios son tamaño del liceo, participantes, duración y resultado declarado; el costo no está."),
        ("abc", "{F} ¿Qué criterio de comparación indica que A y B difieren en 3 meses?", "Duración", "Tamaño del liceo", "Resultado declarado", "A duró tres meses y B seis; la diferencia está en la duración."),
        ("=", "{F} En la fuente B, ¿qué porcentaje de los participantes dijo sentirse más motivado? Calcula 63 dividido por 90 y multiplicado por 100.", "63/90*100", "Se divide la cantidad de motivados entre los participantes y se multiplica por 100.", " %"),
        ("abc", "{F} En la fuente A, ¿qué porcentaje de los participantes dijo haber aprendido a cuidar plantas? Usa 24 de 30.", "80 %", "24 %", "30 %", "24 dividido por 30 da 0,8, es decir, 80 %."),
        ("ab", "{F} Un estudiante afirma que A y B coinciden en que el huerto fue positivo. ¿Qué cuidado debe tener?", "Aclarar que miden resultados distintos: aprendizaje en A y motivación en B", "Ninguno, porque ambos resultados son iguales", "Las fuentes miden aspectos distintos, así que no pueden igualarse sin cautela."),
        ("abc", "{F} ¿Cuál es una síntesis adecuada?", "En dos liceos, una minoría participó en un huerto y declaró resultados favorables, aunque se midieron aspectos distintos", "La fuente A habla de 30 estudiantes y la B de 90", "El huerto es siempre bueno para todos", "La primera integra lo común y marca la diferencia; las otras repiten datos o generalizan."),
        ("abc", "{F} Si se quiere comparar la participación en A y B, ¿qué dato se necesita de cada fuente?", "El porcentaje de participantes sobre el total del liceo", "El resultado declarado por los participantes", "Solo la cantidad de participantes de cada fuente", "Compara bien un porcentaje sobre el mismo criterio, no números absolutos de liceos de distinto tamaño."),
        ("=", "{F} ¿Qué porcentaje del liceo participó en B? Calcula 90 dividido por 600 y multiplicado por 100.", "90/600*100", "Se divide la cantidad de participantes entre el total del liceo y se multiplica por 100.", " %"),
        ("abc", "{F} La participación fue de 7,5 % en A y de 15 % en B. ¿Qué liceo tuvo mayor participación en proporción?", "El de la fuente B", "El de la fuente A", "Tuvieron la misma", "B tuvo 15 % y A 7,5 %, así que en proporción B tuvo mayor participación."),
        ("abc", "{F} ¿Qué conclusión no se puede sacar de las dos fuentes?", "Que el huerto causa el aprendizaje en todos los liceos", "Que los liceos son de distinto tamaño", "Que la duración fue distinta", "Dos fuentes con resultados declarados no demuestran causa general."),
        ("abc", "{F} Un estudiante anota «Resultado: A, 24; B, 63» y concluye que B tuvo mejor resultado. ¿Qué error hay?", "Compara conteos de resultados distintos y sobre totales distintos (30 y 90 participantes)", "No hay error: 63 es mayor que 24", "Debió comparar la duración en lugar del resultado", "24 de 30 y 63 de 90 miden cosas distintas sobre grupos de distinto tamaño; no se pueden comparar así."),
    ],
    ctx=("abc", "Una estudiante compara dos encuestas de ejemplo: una a 50 estudiantes donde 20 estudian con música, y otra a 200 donde 60 lo hacen. ¿Qué debe hacer antes de comparar?", "Calcular los porcentajes: 40 % y 30 %", "Comparar 20 con 60", "Elegir la encuesta más grande sin comparar", "Los números absolutos no son comparables cuando los totales difieren; los porcentajes sí."),
    sc=[
        ("En Lengua: ¿qué diferencia hay entre resumir y sintetizar?", "Resumir condensa una fuente; sintetizar integra varias", "La síntesis relaciona fuentes para una idea nueva."),
        ("¿Qué se pone en las filas de un cuadro comparativo?", "Los criterios de comparación", "Las filas contienen los criterios y las columnas las fuentes."),
        ("=", "Si 18 de 60 estudiantes prefieren estudiar de mañana, ¿qué porcentaje es?", "18/60*100", "Se divide 18 entre 60 y se multiplica por 100."),
    ],
    op=("Compara estas dos fuentes de ejemplo. Fuente 1: «En un liceo de 500 estudiantes, 100 asistieron a talleres de lectura; 70 dijeron leer más». Fuente 2: «En un liceo de 300 estudiantes, 90 asistieron; 54 dijeron leer más». Arma un cuadro con cuatro criterios (tamaño, asistentes, porcentaje de asistentes, resultado) y escribe una síntesis de dos oraciones con una cautela.",
        "Cuadro: tamaño 500 y 300; asistentes 100 y 90; porcentaje 20 % y 30 %; resultado 70 de 100 (70 %) y 54 de 90 (60 %). Síntesis: En ambos liceos una parte de los estudiantes asistió y más de la mitad de los asistentes dijo leer más. Esto no prueba que los talleres sean la causa.",
        ["cuadro con los cuatro criterios y datos correctos", "porcentajes calculados sobre el total correcto", "síntesis que integra y agrega una cautela"],
        ["cuadro de dos columnas y cuatro filas más síntesis"],
        ["comparar números absolutos", "error en los porcentajes", "afirmar causa"],
        "Pregunta: «¿sobre qué total calculaste cada porcentaje?»."),
    reinforce="Calcula los porcentajes de 12 de 80 y de 30 de 150 y di cuál es mayor.",
    extend="Explica por qué una síntesis debe señalar lo que las fuentes no permiten concluir.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (tabla de ejemplo sobre lectura). Fuente: «Informe de ejemplo sobre hábitos de lectura», Torres (2023), p. 9, publicado en línea (dirección de ejemplo, consultado el 5 de mayo de 2025). "
     "Horas semanales promedio de lectura por gusto, según curso: primero medio, 3 horas; segundo medio, 4 horas; tercero medio, 6 horas; cuarto medio, 5 horas. Muestra: 120 estudiantes por curso. "
     "Notas de un estudiante: N1 «Tercero lee más»; N2 «3.º medio: 6 horas semanales de lectura por gusto (Torres, 2023, p. 9)»; N3 «Los de cuarto leen menos porque tienen más pruebas».")
build(
    O3, 4, F,
    use="Aprenderé a registrar datos de tablas y fuentes digitales o impresas con su unidad, su fuente y su alcance, y a organizar mis notas para recuperarlas. Sirve para usar datos sin distorsionarlos.",
    prior=["Sé leer una tabla.", "Sé hacer fichas de contenido.", "Sé citar con autor, año y página."],
    explain=[
        "Los datos de una tabla se registran completos: cifra, unidad (horas semanales), grupo (qué curso), muestra (cuántas personas) y fuente (autor, año, página o dirección y fecha de consulta). Una nota como «tercero lee más» pierde la cifra, la unidad y el alcance, y no se puede verificar. Una nota como la N2 conserva todo lo necesario.",
        "Registrar un dato no es interpretarlo. Una tabla muestra un hecho observado; la causa («leen menos porque tienen más pruebas») es una hipótesis del lector y debe rotularse como tal, porque la fuente no la afirma. Distinguir lo que dice la tabla de lo que uno supone evita atribuirle a la fuente ideas que no tiene.",
        "En soportes digitales hay riesgos especiales: las páginas cambian, un dato puede estar sin autor o sin fecha, y copiar y pegar puede mezclar textos. Por eso se registra la dirección y la fecha de consulta, se guarda una copia con el dato y su fuente y se ordenan los archivos con nombres claros. En soportes impresos se anota la página. En ambos, las notas deben poder encontrarse semanas después.",
    ],
    vocab=[("unidad", "medida en que se expresa un dato, como horas semanales"), ("muestra", "grupo de personas del que se obtuvo el dato"), ("alcance", "a qué grupo y período se aplica el dato"), ("hipótesis", "explicación posible que aún no se ha comprobado"), ("soporte", "medio donde está la fuente: impreso o digital")],
    worked=[
        ("Registrar completo un dato de tabla", "De la tabla: segundo medio, 4 horas semanales de lectura por gusto. Escribe una nota completa.",
         ["Se escribe la cifra con unidad y grupo.", "Se agrega la fuente con año y página."],
         "«2.º medio: 4 horas semanales de lectura por gusto (Torres, 2023, p. 9)»"),
        ("Separar dato e hipótesis", "Nota: «Los de cuarto leen menos porque tienen más pruebas». ¿Qué parte es dato y qué parte es hipótesis?",
         ["Dato: cuarto medio lee menos que tercero.", "Hipótesis: la causa son las pruebas, que la tabla no menciona."],
         "El dato es la diferencia de horas; la causa es una hipótesis"),
    ],
    mistakes=[("Anotar «tercero lee más» sin cifra.", "No se puede comparar ni citar y se pierde la unidad.", "Registra la cifra con su unidad, el grupo y la fuente."),
              ("Copiar la causa que uno supone como si fuera de la fuente.", "Se le atribuye a la fuente algo que no dice.", "Marca como hipótesis propia lo que la fuente no afirma.")],
    T=[
        ("abc", "{F} ¿Cuántas horas semanales de lectura por gusto registra tercero medio?", "6 horas", "4 horas", "5 horas", "La tabla indica 6 horas para tercero medio; 5 es cuarto y 4 es segundo."),
        ("ab", "En Lengua: ¿qué es la unidad de un dato?", "La medida en que se expresa, como horas semanales", "El número de personas encuestadas", "La unidad aclara cómo se mide la cifra; las personas encuestadas son la muestra."),
        ("=", "{F} ¿Cuántas horas semanales más lee tercero medio que primero medio?", "6-3", "Se resta la cifra de primero medio de la de tercero medio.", " horas"),
        ("abc", "{F} ¿Cuál de las notas del estudiante conserva dato, grupo, unidad y fuente?", "N2", "N1", "N3", "N2 trae la cifra, el curso, la unidad y la fuente con página; N1 y N3 no."),
        ("ab", "{F} ¿Qué parte de la nota N3 no está en la tabla?", "La causa: «porque tienen más pruebas»", "La comparación entre cursos", "La tabla muestra cuántas horas leen; la causa es una suposición del lector."),
        ("abc", "{F} ¿Qué dato falta en N1 para poder citarla?", "La cifra, la unidad y la fuente", "El color del texto", "El nombre del estudiante", "«Tercero lee más» no dice cuánto, en qué unidad ni de dónde sale."),
        ("abc", "{F} Un compañero concluye: «Todos los estudiantes de tercero medio leen 6 horas semanales». ¿Qué error hay?", "Un promedio no dice cuánto lee cada estudiante: unos leen más y otros menos", "Falta la unidad de horas", "Tercero medio no es el curso con más horas", "La tabla da horas semanales promedio por curso, no el valor de cada persona."),
        ("abc", "{F} Un estudiante escribe: «Cuarto medio lee 5 horas, así que los de 4.º son menos aplicados». ¿Qué error tiene?", "Convierte un dato en una conclusión sobre las personas que la fuente no permite", "Cita mal la página", "Usa números", "La tabla mide horas de lectura por gusto; no mide aplicación ni ofrece causa."),
        ("abc", "{F} Para citar la fuente digital, ¿qué debe anotarse además del autor, el año y el título?", "La dirección y la fecha de consulta", "Solo la fecha de consulta", "Ninguno", "Una fuente digital se identifica por su dirección y la fecha en que se leyó."),
        ("abc", "{F} Si el dato se cita como válido para «todos los estudiantes de Chile», ¿qué problema hay?", "Excede el alcance: la muestra es de 120 estudiantes por curso", "Falta la unidad", "Usa un gráfico", "La tabla solo representa a la muestra; hay que limitar el alcance."),
        ("abc", "Un estudiante guarda un dato digital sin fecha ni dirección. Semanas después la página cambió. ¿Qué problema tiene?", "No puede comprobar qué versión leyó ni volver a la fuente", "Puede citarla igual sin riesgo", "Debe borrar todas sus notas", "Sin dirección y fecha de consulta no se verifica el dato en la fuente."),
        ("abc", "{F} Dos estudiantes registran el mismo dato: uno dice «tercero: 6» y otro «3.º medio: 6 horas semanales de lectura por gusto (Torres, 2023, p. 9)». ¿Por qué el segundo es mejor?", "Porque se entiende y se puede citar sin volver a la tabla", "Porque es más largo", "Porque tiene más números", "Una nota útil se entiende sola y remite a su fuente."),
        ("abc", "{F} ¿Qué afirmación sí respalda la tabla?", "Tercero medio tiene el promedio más alto de horas de lectura por gusto de los cuatro cursos", "Los estudiantes de cuarto medio leen menos porque tienen más pruebas", "A medida que sube el curso, el promedio de lectura siempre aumenta", "Tercero medio tiene 6 horas, la cifra más alta; la causa no la entrega la tabla y de tercero a cuarto el promedio baja."),
    ],
    ctx=("abc", "Un grupo de ejemplo encuentra en línea un gráfico sin autor ni fecha que dice que «el 80 % de los jóvenes duerme mal». ¿Qué conviene hacer antes de registrarlo?", "Buscar su origen y, si no se puede, anotarlo como dato sin fuente verificada", "Citar el gráfico como evidencia principal", "Pegar el gráfico sin comentarios", "Un dato sin autor ni fecha no se puede verificar; no debe ser evidencia principal."),
    sc=[
        ("En Lengua: ¿qué debe tener la nota de un dato de tabla?", "Cifra, unidad, grupo y fuente", "Con esos elementos el dato se entiende y se puede citar."),
        ("¿Qué se anota de una fuente digital para ubicarla?", "La dirección y la fecha de consulta", "Reemplazan a la página de lo impreso."),
        ("¿Una causa que uno supone es dato o hipótesis?", "Hipótesis", "La tabla no la afirma; es una suposición del lector."),
    ],
    op=("Con esta tabla de ejemplo: «Horas semanales promedio de deporte por gusto; fuente: Pérez (2022), p. 14; muestra de 100 estudiantes por curso: primero medio, 5 horas; segundo medio, 4 horas; tercero medio, 3 horas». Escribe tres notas: (1) un dato completo con su fuente, (2) una comparación entre dos cursos con la diferencia en horas, (3) una hipótesis propia rotulada como tal.",
        "(1) 1.º medio: 5 horas semanales de deporte por gusto (Pérez, 2022, p. 14). (2) Primero medio hace 2 horas semanales más que tercero medio (5 − 3) (Pérez, 2022, p. 14). (3) Hipótesis propia: podría deberse a que cursos mayores tienen más trabajo escolar; la fuente no lo afirma.",
        ["dato con cifra, unidad, grupo y fuente", "comparación con la diferencia calculada bien", "hipótesis rotulada y separada del dato"],
        ["tres notas escritas"],
        ["dato sin unidad o sin fuente", "diferencia mal calculada", "hipótesis presentada como dato"],
        "Pregunta: «¿esta nota dice qué muestra la fuente y qué piensas tú?»."),
    reinforce="Escribe una nota completa con este dato de ejemplo: «Segundo medio duerme 7 horas diarias; fuente Soto (2021), p. 6; muestra de 90 estudiantes».",
    extend="Explica por qué guardar una copia del dato con su fuente puede ser útil aunque la página en línea siga disponible.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (notas y plan de ejemplo). Texto por escribir: informe breve para el consejo del liceo sobre el uso de la biblioteca. Secciones: Problema, Método, Resultados, Conclusión. "
     "N1: «Pregunta: ¿cuántas veces por semana usa la biblioteca un segundo medio?». "
     "N2: «Se encuestó a 60 estudiantes durante una semana de ejemplo». "
     "N3: «Resultado: 36 de 60 usan la biblioteca al menos dos veces por semana». "
     "N4: «La bibliotecaria es muy simpática» (opinión sin relación con el problema). "
     "N5: «Conclusión posible: la mayoría usa la biblioteca, pero hay que ver el horario». "
     "N6: «Los resultados fueron lindos».")
build(
    O3, 5, F,
    use="Aprenderé a ajustar mis notas al tema, al propósito y a las convenciones del género que voy a escribir: ubicarlas en las secciones, descartar lo que no sirve y reescribir lo impreciso. Sirve para pasar de apuntes a un texto coherente.",
    prior=["Sé registrar datos con su fuente.", "Conozco las secciones de un informe.", "Sé distinguir un dato de una opinión."],
    explain=[
        "Las notas valen según su utilidad para el texto que se va a escribir. Antes de usarlas se contrastan con el tema, el propósito y las convenciones del género. Si el género es un informe, las notas deben calzar en sus secciones: problema, método, resultados y conclusión. Una nota que no calza en ninguna sección, o que no tiene relación con el problema, se descarta o se guarda aparte.",
        "También se revisa el registro. Un informe usa un lenguaje preciso y cauteloso; una nota como «los resultados fueron lindos» es vaga y coloquial: hay que reemplazarla por un dato («36 de 60 usan la biblioteca al menos dos veces por semana»). Las notas con cifras deben conservar la unidad, el total y la fuente; las impresiones se reescriben o se descartan.",
        "Procesar las notas para un texto es un trabajo de decisión: qué se queda, qué se reformula, qué se descarta y dónde va cada cosa. Un buen cierre de esta etapa es un esquema con notas asignadas a cada sección, listo para redactar. Si falta información en alguna sección, se detecta ahora y se busca en otra fuente.",
    ],
    vocab=[("convención del género", "forma de organizar y decir propia de un tipo de texto"), ("sección", "parte del texto con función propia"), ("descartar", "dejar fuera una nota que no sirve al propósito"), ("reformular", "volver a decir una nota con precisión y registro adecuados"), ("registro", "modo de decir según la situación, formal o coloquial")],
    worked=[
        ("Ubicar una nota en una sección", "Nota: «Se encuestó a 60 estudiantes durante una semana de ejemplo». ¿En qué sección de un informe va?",
         ["Describe cómo se obtuvo la información.", "Eso corresponde al método."],
         "Método"),
        ("Reformular una nota vaga", "Nota: «Las cifras fueron buenas». Reformúlala con un dato de ejemplo.",
         ["La nota es vaga y valorativa.", "Se reemplaza por un dato con total y unidad."],
         "«Aprobaron 40 de 50 estudiantes (de ejemplo)»"),
    ],
    mistakes=[("Poner todas las notas en el texto «para no perder nada».", "Las notas irrelevantes distraen y rompen la coherencia.", "Descarta o guarda aparte lo que no responde al problema."),
              ("Dejar en el informe notas coloquiales como «lindos».", "No cumple el registro del género y no aporta información verificable.", "Reemplázalas por datos con unidad, total y fuente.")],
    T=[
        ("abc", "{F} ¿En qué sección va la nota N1?", "Problema", "Método", "Resultados", "N1 formula la pregunta que guía el estudio, es decir, el problema."),
        ("abc", "{F} ¿En qué sección va la nota N2?", "Método", "Problema", "Conclusión", "N2 describe cómo se obtuvieron los datos, que es el método."),
        ("abc", "{F} ¿En qué sección va la nota N3?", "Resultados", "Método", "Conclusión", "N3 entrega el resultado numérico del estudio."),
        ("ab", "{F} ¿Qué se debe hacer con N4, «La bibliotecaria es muy simpática»?", "Descartarla o guardarla aparte, porque no responde al problema", "Ponerla en resultados como dato clave", "La nota no se relaciona con el uso de la biblioteca ni con el propósito del informe."),
        ("abc", "{F} ¿En qué sección va la nota N5?", "Conclusión", "Método", "Problema", "N5 interpreta los resultados y señala un límite, lo propio de una conclusión."),
        ("ab", "{F} ¿Qué problema tiene la nota N6, «Los resultados fueron lindos»?", "Es vaga y coloquial, sin dato verificable", "Es demasiado precisa", "«Lindos» no informa nada medible ni cumple el registro de un informe."),
        ("=", "{F} Según N3, ¿qué porcentaje de los 60 estudiantes usa la biblioteca al menos dos veces por semana? Divide 36 entre 60 y multiplica por 100.", "36/60*100", "36 de 60 equivale a 60 de cada 100, es decir, más de la mitad.", " %"),
        ("abc", "{F} ¿Cuál es una reformulación de N6 que cumple el registro del informe?", "«36 de 60 estudiantes usan la biblioteca al menos dos veces por semana»", "«Estuvo bien»", "«Qué buenos resultados»", "La primera entrega un dato concreto y un registro formal."),
        ("abc", "{F} Un estudiante propone poner N5 en la sección Método. ¿Qué problema hay?", "N5 interpreta resultados y pertenece a la conclusión", "N5 es demasiado larga", "El método no lleva notas", "El método explica cómo se obtuvieron los datos, no qué se concluye."),
        ("abc", "{F} Un informe necesita las secciones Problema, Método, Resultados y Conclusión. Con N1, N2, N3 y N5 ubicadas, ¿qué sección tiene más de una nota?", "Ninguna: cada una tiene una nota", "Método", "Resultados", "N1 va en problema, N2 en método, N3 en resultados y N5 en conclusión."),
        ("abc", "{F} Se pide que la conclusión mencione una limitación. ¿Qué nota ya la aporta?", "N5, porque dice que hay que ver el horario", "N2", "N4", "N5 reconoce que falta analizar el horario, lo que es un límite."),
        ("abc", "{F} Si se cambia el género a un artículo de divulgación para el diario mural, ¿qué ajuste de las notas es razonable?", "Explicar términos y presentar los datos de forma más cercana, conservando las cifras", "Quitar las cifras", "Agregar N4 como dato central", "La divulgación mantiene la información esencial con lenguaje accesible."),
        ("{F} ¿Cuántas de las seis notas quedan fuera del informe por no cumplir su propósito o su registro, sin reformular?", "2", "N4 no tiene relación con el problema y N6 es vaga; las otras cuatro sirven."),
    ],
    ctx=("abc", "Un grupo tiene estas notas para un informe sobre bicicletas: «se encuestó a 40 estudiantes», «14 llegan en bicicleta», «la bici es lo máximo». ¿Qué hace con la tercera?", "La reformula como dato o la descarta, porque es una opinión coloquial", "La usa como resultado principal", "La pone en el método", "Una opinión coloquial no cumple el registro del informe ni aporta dato."),
    sc=[
        ("En Lengua: ¿qué se contrasta con las notas antes de usarlas en un texto?", "El tema, el propósito y las convenciones del género", "Esos tres elementos deciden qué se usa y dónde."),
        ("¿Qué se hace con una nota que no sirve al propósito?", "Se descarta o se guarda aparte", "Dejarla en el texto rompe la coherencia."),
        ("¿En qué sección de un informe va el resultado numérico?", "En Resultados", "Los resultados presentan lo que se obtuvo."),
    ],
    op=("Estas son las notas de ejemplo para un informe sobre el uso de patio en recreos: N1 «¿Cuántos estudiantes de primero medio salen al patio en el recreo largo?», N2 «Se contó a los estudiantes en cinco recreos de ejemplo», N3 «El patio es lindo», N4 «En promedio salieron 45 de 60», N5 «Habría que probar con otros días». Asigna cada nota a una sección (Problema, Método, Resultados, Conclusión), descarta o reformula las que no sirven y escribe la reformulación.",
        "N1 Problema. N2 Método. N3 se descarta o se reformula con un dato (por ejemplo, «el patio tiene 3 mesas de ejemplo»), porque «lindo» no aporta. N4 Resultados. N5 Conclusión (limitación).",
        ["asigna bien las notas a las secciones", "descarta o reformula la nota vaga", "justifica en una línea cada decisión"],
        ["cuadro con cinco notas y su decisión"],
        ["ubicar resultados en el método", "dejar la nota vaga como dato", "no justificar"],
        "Pregunta: «¿qué parte del informe depende de esta nota?»."),
    reinforce="Ubica estas notas en las secciones de un informe: «se midió el tiempo de traslado», «llegaron en promedio 20 minutos», «¿cuánto tarda un estudiante en llegar?».",
    extend="Explica cómo cambiaría la ubicación de las notas si el género fuera un ensayo con tesis y argumentos.",
)

# ============================================================ OAC-04, clase 1
F = ("Ficha 6 (lectura y dos notas de ejemplo). Texto leído: «Un huerto escolar necesita riego regular. Si se riega con agua de lluvia recolectada, disminuye el consumo de agua de la red». "
     "Nota A: «Un huerto escolar necesita riego regular. Si se riega con agua de lluvia recolectada, disminuye el consumo de agua de la red». "
     "Nota B: «Si el liceo recolectara agua de lluvia, podría regar sin gastar agua potable. No sé cuánta agua haría falta ni si llueve lo suficiente. Debo averiguar el tamaño del huerto y cuánto se gasta hoy».")
build(
    O4, 1, F,
    use="Aprenderé a escribir para pensar: usar la escritura como herramienta para entender, relacionar y cuestionar lo que leo. Sirve para construir conocimiento propio y no solo repetir lo leído.",
    prior=["Sé tomar notas de una lectura.", "Sé formular preguntas.", "Sé distinguir qué sé y qué no sé."],
    explain=[
        "Escribir sirve para comunicar un conocimiento ya armado, pero también para construirlo. Cuando se escribe para pensar, se ponen en palabras propias las ideas, se relacionan con lo que ya se sabe, se descubren vacíos y se formulan preguntas. A esto se le llama transformar el conocimiento: no se copia lo leído, se lo reorganiza y se lo hace propio.",
        "Algunas estrategias para pensar por escrito: la escritura libre, que consiste en escribir sin detenerse durante unos minutos sobre un tema; el cuadro «qué sé, qué no sé, qué necesito averiguar»; la pregunta al texto («¿qué pasaría si…?»); y la explicación con palabras propias a una persona que no conoce el tema. Estos borradores no son para entregar: pueden ser desordenados.",
        "Copiar el texto no transforma nada: la nota A repite lo leído. La nota B, en cambio, relaciona la lectura con el liceo, reconoce lo que no se sabe y plantea qué averiguar. La diferencia no es de largo, sino de actividad intelectual: B aplica, cuestiona y proyecta. Después, ese material se puede ordenar y pulir para comunicarlo a otros.",
    ],
    vocab=[("escribir para pensar", "usar la escritura para entender, relacionar y cuestionar"), ("escritura libre", "escribir sin detenerse sobre un tema, sin corregir"), ("transformar el conocimiento", "reorganizar lo leído para hacerlo propio"), ("vacío de información", "lo que aún no se sabe y se necesita averiguar"), ("palabras propias", "forma personal de decir una idea sin copiarla")],
    worked=[
        ("Reconocer una nota que transforma", "Nota: «El agua de lluvia podría servir para el huerto del liceo, pero no sé cuánta se necesita». ¿Transforma el conocimiento?",
         ["Relaciona la lectura con una situación propia (el liceo).", "Reconoce un vacío (cuánta agua se necesita)."],
         "Sí: relaciona, aplica y reconoce un vacío"),
        ("Usar el cuadro qué sé, qué no sé", "Tema: las redes sociales y el estudio. Completa el cuadro con una línea cada una.",
         ["Qué sé: muchos estudiantes las usan a diario.", "Qué no sé: cuánto tiempo dedican durante el estudio.", "Qué necesito averiguar: una encuesta o estudio sobre el tiempo de uso al estudiar."],
         "Cuadro completo con las tres columnas"),
    ],
    mistakes=[("Creer que copiar el texto con letra más ordenada es estudiar.", "Copiar no obliga a entender ni a relacionar.", "Reescribe con tus palabras y agrega una pregunta propia."),
              ("No escribir el borrador porque «aún no sé nada».", "Escribir ayuda a descubrir lo que se sabe y lo que falta.", "Empieza con escritura libre y marca vacíos.")],
    T=[
        ("abc", "{F} ¿Qué nota copia el texto leído?", "La nota A", "La nota B", "Ninguna", "La nota A repite el texto sin cambiar nada."),
        ("ab", "En Lengua: ¿qué es la escritura libre?", "Escribir sin detenerse sobre un tema, sin corregir", "Escribir solo con la letra más bonita", "Se escribe sin parar para descubrir ideas; no se pule."),
        ("abc", "{F} ¿Qué hace la nota B que no hace la A?", "Relaciona la lectura con el liceo y reconoce lo que no sabe", "Usa más palabras", "Cita al autor", "La diferencia está en la actividad intelectual: aplicar y cuestionar."),
        ("abc", "{F} ¿Qué vacío de información reconoce la nota B?", "Cuánta agua haría falta y si llueve lo suficiente", "Quién escribió el texto", "Cuándo se escribió la nota", "La nota lo dice: no sabe cuánta agua haría falta ni si llueve lo suficiente."),
        ("abc", "¿Cuál es un ejemplo de pregunta al texto que ayuda a pensar?", "«¿Qué pasaría si el liceo no recolectara agua de lluvia?»", "«¿Cuántas oraciones tiene el texto?»", "«¿Quién lo escribió y en qué año?»", "La primera obliga a relacionar y explorar consecuencias."),
        ("ab", "Un compañero dice que los borradores de escritura para pensar deben estar perfectos. ¿Es correcto?", "No: pueden ser desordenados porque sirven para descubrir ideas", "Sí: todo lo que se escribe debe estar pulido", "Escribir para pensar es una etapa previa y no se entrega."),
        ("abc", "{F} En el cuadro «qué sé, qué no sé, qué necesito averiguar», ¿dónde va «el tamaño del huerto»?", "Qué necesito averiguar", "Qué sé", "No va en ninguna", "Es un dato que la nota B dice que debe averiguar."),
        ("abc", "{F} ¿Cuál es una pregunta nueva que podría surgir de la nota B?", "¿Cuántos litros usa el huerto por semana?", "¿Cuántas palabras tiene el texto?", "¿Qué letra usa el autor?", "Pide un dato que sirve para completar el vacío de información."),
        ("abc", "Una estudiante explica con sus palabras a un compañero de otro curso, que no conoce el tema, cómo se riega un huerto con agua de lluvia recolectada. ¿Qué estrategia usa?", "Explicar con palabras propias a otra persona", "Copiar de un libro", "Subrayar sin leer", "Explicar a alguien que no sabe obliga a reorganizar lo entendido."),
        ("abc", "{F} Se debe pasar de la nota B a un texto para el consejo del liceo. ¿Qué paso sigue?", "Averiguar los datos que faltan y ordenar las ideas para comunicarlas", "Copiar la nota B tal cual", "Borrar los vacíos de información", "Después de pensar, se completa la información y se organiza para comunicar."),
        ("abc", "Dos estudiantes escriben la misma cantidad de palabras: uno copia, el otro relaciona y pregunta. ¿Quién transforma mejor el conocimiento?", "El que relaciona y pregunta", "El que copia más rápido", "Ambos por igual", "Transformar no depende del largo, sino de relacionar y cuestionar."),
        ("abc", "{F} Si el estudiante agrega a B «además, otros liceos ya lo hicieron», ¿qué debería hacer antes de usarlo en un texto?", "Buscar una fuente que lo confirme", "Afirmarlo como cierto", "Quitar la nota", "Una idea nueva sin respaldo necesita verificarse antes de comunicarse."),
        ("abc", "{F} ¿Qué dos datos dice la nota B que debe averiguar con la expresión «Debo averiguar»?", "El tamaño del huerto y cuánto se gasta hoy", "Cuánta agua haría falta y si llueve lo suficiente", "El autor del texto y la fecha", "La nota usa «Debo averiguar» para el tamaño del huerto y el gasto actual; los otros son cosas que dice no saber."),
    ],
    ctx=("abc", "Una estudiante leyó un artículo de ejemplo sobre la importancia del desayuno. Quiere usar la escritura para entender mejor. ¿Qué es lo más útil?", "Escribir qué sabe, qué no sabe y qué necesita averiguar sobre el desayuno de su curso", "Copiar los párrafos del artículo", "Subrayar todo el artículo", "El cuadro con tres columnas la obliga a relacionar y reconocer vacíos."),
    sc=[
        ("En Lengua: ¿para qué sirve escribir para pensar?", "Para entender, relacionar y cuestionar lo leído", "La escritura es herramienta de construcción del conocimiento."),
        ("¿Copiar un texto transforma el conocimiento?", "No: repite sin relacionar ni cuestionar", "Transformar exige reorganizar con palabras propias."),
        ("¿Qué tres columnas tiene el cuadro de apoyo?", "Qué sé, qué no sé y qué necesito averiguar", "Ordena el pensamiento y los vacíos."),
    ],
    op=("Lee este texto original de ejemplo: «En muchos liceos se organiza un recreo con juegos organizados para que más estudiantes se muevan. Cuando hay juegos organizados, suele participar más gente que cuando el patio queda libre». Haz tres cosas: (1) una escritura libre de cuatro líneas sin detenerte, (2) un cuadro «qué sé, qué no sé, qué necesito averiguar» y (3) una pregunta propia al texto.",
        "(1) Si hubiera juegos en nuestro recreo, quizás saldría más gente al patio, aunque algunos prefieren conversar. (2) Qué sé: hay juegos organizados en algunos liceos. Qué no sé: si a mi curso le gustaría. Qué necesito averiguar: encuesta de preferencias. (3) ¿Qué pasaría si los juegos fueran voluntarios?",
        ["la escritura libre relaciona el texto con su contexto", "el cuadro tiene las tres columnas completas", "la pregunta cuestiona o proyecta"],
        ["escritura de cuatro líneas, cuadro y una pregunta"],
        ["copiar el texto", "dejar vacío el cuadro", "pregunta que se responde con sí o no sin sentido"],
        "Pregunta: «¿qué entendiste que no estaba escrito en el texto?»."),
    reinforce="Haz un cuadro de tres columnas sobre el tema «dormir y rendir en clases» con una línea en cada una.",
    extend="Explica por qué un borrador de escritura para pensar puede ser desordenado y aun así útil.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 7 (esquema por armar, de ejemplo). Tesis: «El liceo debería instalar un sistema de recolección de agua de lluvia para regar el huerto». "
     "I1: «El riego con agua de lluvia disminuye el gasto de agua potable». I2: «Un liceo de ejemplo redujo su consumo en un tercio al regar con agua de lluvia». "
     "I3: «La instalación tiene un costo inicial que se recupera con el ahorro». I4: «El huerto sirve para aprender Ciencias». "
     "I5: «El color de las paredes del patio es celeste». I6: «Una cuenta de ejemplo muestra que el ahorro anual cubre el costo en tres años».")
build(
    O4, 2, F,
    use="Aprenderé a planificar un texto con un esquema jerárquico: tesis, argumentos, evidencias y conclusión. Sirve para organizar lo pensado antes de escribir y detectar lo que falta o sobra.",
    prior=["Sé qué es una tesis y qué es evidencia.", "Sé escribir para pensar.", "Sé distinguir lo relevante de lo irrelevante."],
    explain=[
        "Un esquema es un plano del texto. En un texto argumentativo tiene niveles: arriba, la tesis; debajo, los argumentos o razones que la apoyan; y bajo cada argumento, la evidencia que lo sostiene (un dato, un ejemplo, una cita). Esta jerarquía muestra qué idea depende de cuál y permite ver si un argumento no tiene evidencia.",
        "Para esquematizar se hace una lista de ideas, se descartan las que no se relacionan con la tesis y se agrupan las demás. Un argumento es una razón general («reduce el gasto de agua»); la evidencia es lo que la respalda («un liceo de ejemplo redujo su consumo en un tercio»). Un mismo dato no es argumento y evidencia a la vez: cada uno tiene un nivel.",
        "Un esquema también incluye la apertura y el cierre: la introducción presenta el problema y la tesis, y la conclusión retoma la tesis y su alcance. Un esquema flexible se puede ajustar mientras se escribe, pero sin esquema es fácil perder el hilo, repetir ideas o dejar argumentos sin respaldo.",
    ],
    vocab=[("esquema", "plano jerárquico de las ideas de un texto"), ("argumento", "razón que apoya la tesis"), ("evidencia", "dato, ejemplo o cita que respalda un argumento"), ("jerarquía", "orden por niveles entre ideas"), ("irrelevante", "que no se relaciona con la tesis")],
    worked=[
        ("Distinguir argumento y evidencia", "«Mejora la concentración de los estudiantes» y «en una encuesta de ejemplo, 36 de 50 dijeron concentrarse mejor tras un recreo activo». ¿Cuál es argumento y cuál evidencia?",
         ["La primera es una razón general que apoya una tesis.", "La segunda es un dato concreto que respalda esa razón."],
         "Argumento y evidencia, respectivamente"),
        ("Detectar una idea irrelevante", "En un esquema sobre reciclaje aparece: «los contenedores son azules». ¿Sirve a la tesis «el liceo debe reciclar más papel»?",
         ["Se compara con la tesis.", "El color no apoya la tesis."],
         "Es irrelevante y se descarta"),
    ],
    mistakes=[("Poner en el mismo nivel la tesis, los argumentos y los datos.", "Se pierde la jerarquía y no se ve qué apoya a qué.", "Ordena por niveles: tesis, argumentos y evidencias bajo cada argumento."),
              ("Dejar en el esquema ideas que no se relacionan con la tesis.", "Distraen y alargan el texto sin aportar.", "Contrasta cada idea con la tesis y descarta las que no la apoyan.")],
    T=[
        ("abc", "{F} ¿Cuál de las ideas es una evidencia?", "I2", "I1", "I4", "I2 es un dato concreto de otro liceo que respalda un argumento."),
        ("abc", "{F} ¿Qué idea es irrelevante para la tesis?", "I5", "I3", "I6", "El color de las paredes no se relaciona con el riego con agua de lluvia."),
        ("ab", "En Lengua: ¿qué es un argumento en un esquema?", "Una razón que apoya la tesis", "Un dato suelto sin relación", "El argumento es la razón general; el dato que la respalda es la evidencia."),
        ("abc", "{F} ¿Qué idea es un argumento que apoya la tesis?", "I1", "I2", "I6", "I1 es una razón general; I2 y I6 son datos que respaldan razones."),
        ("abc", "{F} ¿Qué evidencia respalda el argumento I3 (el costo se recupera)?", "I6", "I2", "I4", "I6 es la cuenta que muestra que el ahorro cubre el costo en tres años."),
        ("abc", "{F} ¿Qué evidencia respalda el argumento I1 (disminuye el gasto de agua potable)?", "I2", "I6", "I5", "I2 muestra un caso en que el consumo bajó un tercio."),
        ("ab", "{F} ¿Dónde debe ir la tesis dentro del esquema?", "En la introducción y retomada en la conclusión", "Solo al final", "La tesis se presenta al comienzo para guiar al lector y se retoma al cerrar."),
        ("abc", "{F} Si se agrega el argumento I4 (el huerto sirve para aprender Ciencias), ¿qué le falta para quedar bien apoyado?", "Una evidencia, como un ejemplo de actividad", "Más adjetivos", "Quitar la tesis", "Un argumento sin evidencia queda como afirmación sin respaldo."),
        ("abc", "{F} Un estudiante propone usar I2 como argumento principal y descartar I1. ¿Qué problema hay?", "I2 es un dato de un caso: sin la razón general I1 no queda claro qué apoya", "I2 es irrelevante para la tesis", "I1 es una evidencia más fuerte que I2", "Un dato necesita un argumento que explique qué sostiene; I2 respalda a I1."),
        ("abc", "Un estudiante pone en un esquema solo tesis y datos, sin argumentos. ¿Qué problema tiene?", "Falta la razón que une los datos con la tesis", "Tiene demasiados datos", "Falta la ortografía", "Los datos necesitan un argumento que explique por qué apoyan la tesis."),
        ("abc", "{F} Dos estudiantes discuten si I3 es evidencia o argumento. ¿Quién tiene razón?", "I3 es argumento, porque es una razón general que luego se respalda con I6", "I3 es evidencia, porque tiene un número", "I3 no se relaciona con la tesis", "I3 se respalda con la cuenta de I6, así que está en el nivel de argumento."),
        ("abc", "{F} ¿Cuál es una conclusión coherente con el esquema?", "El liceo debería instalar el sistema porque reduce el gasto y su costo se recupera", "El huerto es bonito", "El color de las paredes mejora el riego", "Retoma la tesis con sus principales razones."),
        ("abc", "{F} ¿Cuál sería una evidencia adecuada para el argumento I4 (el huerto sirve para aprender Ciencias)?", "En un huerto de ejemplo, un curso midió el crecimiento de las plantas durante una unidad de Ciencias", "El huerto es bonito y tiene muchas flores", "El liceo debería instalar el sistema de recolección", "Una evidencia es un dato o ejemplo concreto que respalda el argumento; las otras son una descripción y la tesis."),
    ],
    ctx=("abc", "Un grupo quiere defender que el liceo abra la biblioteca en la tarde. Tiene tres ideas: «más estudiantes podrían estudiar», «una encuesta de ejemplo mostró que 45 de 60 quieren ese horario» y «la biblioteca tiene sillas azules». ¿Cuál es la evidencia y cuál se descarta?", "Evidencia: la encuesta; se descarta: las sillas azules", "Evidencia: las sillas; se descarta: la encuesta", "Todas son evidencia", "La encuesta respalda el argumento; el color de las sillas no se relaciona con la tesis."),
    sc=[
        ("En Lengua: ¿cuáles son los niveles de un esquema argumentativo?", "Tesis, argumentos y evidencias", "Muestran la jerarquía de las ideas."),
        ("¿Qué se hace con una idea que no se relaciona con la tesis?", "Se descarta", "Una idea irrelevante distrae al lector y alarga el texto."),
        ("¿Para qué sirve la evidencia?", "Para respaldar un argumento", "Sin evidencia el argumento queda sin respaldo."),
    ],
    op=("Elige una tesis: A) el liceo debería tener un horario de estudio en la tarde, B) el curso debería organizar una colecta de útiles. Arma un esquema con la tesis, dos argumentos, una evidencia (de ejemplo) para cada argumento y una conclusión. Agrega una idea irrelevante y táchala con la razón.",
        "Tesis A. Argumento 1: ayuda a quienes no tienen lugar para estudiar en casa. Evidencia: 20 de 50 encuestados (de ejemplo) no tienen lugar. Argumento 2: aprovecha la biblioteca. Evidencia: hoy cierra a las 14:00. Conclusión: conviene abrir la biblioteca en la tarde. Idea irrelevante: el color de las mesas.",
        ["tesis clara", "dos argumentos con evidencia cada uno", "conclusión que retoma la tesis y una idea descartada con razón"],
        ["esquema por niveles"],
        ["argumentos sin evidencia", "confundir evidencia con argumento", "conclusión que no retoma la tesis"],
        "Pregunta: «¿qué argumento no tiene evidencia?»."),
    reinforce="Con la tesis «los recreos deberían tener juegos organizados», escribe dos argumentos y una evidencia de ejemplo para cada uno.",
    extend="Explica por qué un esquema ayuda a descubrir qué información falta antes de empezar a escribir.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 8 (párrafo y conectores, de ejemplo). Párrafo: «Conviene abrir la biblioteca en la tarde (afirmación). En una encuesta de ejemplo, 45 de 60 estudiantes dijeron que estudiarían allí después de clases (evidencia). Esto muestra que existe una demanda real de un lugar tranquilo para estudiar (explicación)». "
     "Conectores: porque, además, sin embargo, por lo tanto, en cambio.")
build(
    O4, 3, F,
    use="Aprenderé a escribir un párrafo argumentativo con afirmación, evidencia y explicación, y a usar conectores que muestren la relación entre las ideas. Sirve para convertir el esquema en texto claro.",
    prior=["Sé armar un esquema con tesis, argumentos y evidencia.", "Sé qué es un conector.", "Sé citar la fuente de un dato."],
    explain=[
        "Un párrafo argumentativo tiene tres movimientos: la afirmación (la idea que se sostiene), la evidencia (el dato, ejemplo o cita que la respalda) y la explicación (por qué esa evidencia apoya la afirmación). Muchos textos débiles tienen afirmación y evidencia pero omiten la explicación: el lector debe adivinar la conexión. La explicación es lo que hace visible el razonamiento.",
        "Los conectores muestran la relación lógica entre ideas. «Porque» introduce una causa; «además» suma una razón; «sin embargo» marca un contraste u objeción; «por lo tanto» introduce una consecuencia o conclusión; «en cambio» opone dos casos. Elegir un conector equivocado cambia el sentido: usar «por lo tanto» donde corresponde «sin embargo» confunde al lector.",
        "Un párrafo también tiene unidad: trata una sola idea principal. Si aparecen dos afirmaciones distintas, conviene dividirlo. Al terminar, se puede comprobar con tres preguntas: ¿qué afirmo?, ¿con qué lo respaldo? y ¿por qué ese respaldo apoya mi afirmación? Si falta alguna respuesta, el párrafo no está completo.",
    ],
    vocab=[("párrafo argumentativo", "unidad de texto con afirmación, evidencia y explicación"), ("afirmación", "idea que se sostiene"), ("explicación", "razonamiento que une evidencia y afirmación"), ("conector", "palabra que marca la relación lógica entre ideas"), ("unidad", "que el párrafo trate una sola idea principal")],
    worked=[
        ("Identificar las partes", "Párrafo: «El curso debería hacer una colecta. En su liceo, 30 de 40 estudiantes necesitan útiles (de ejemplo). Esto muestra que hay una necesidad amplia». ¿Qué parte es la evidencia?",
         ["La afirmación es la primera oración.", "El dato «30 de 40» es la evidencia.", "La tercera oración explica."],
         "«30 de 40 estudiantes necesitan útiles»"),
        ("Elegir un conector", "«La biblioteca abre hasta las 14:00; ___ los estudiantes no pueden usarla en la tarde». ¿Cuál conector va?",
         ["La segunda parte es una consecuencia de la primera.", "El conector de consecuencia es «por lo tanto»."],
         "por lo tanto"),
    ],
    mistakes=[("Poner afirmación y dato, sin explicar por qué el dato apoya la idea.", "El lector no ve la conexión.", "Agrega una oración que explique la relación."),
              ("Usar «por lo tanto» para marcar contraste.", "Ese conector indica consecuencia, no oposición.", "Usa «sin embargo» para contrastar y «por lo tanto» para concluir.")],
    T=[
        ("abc", "{F} ¿Cuál es la afirmación del párrafo?", "Conviene abrir la biblioteca en la tarde", "45 de 60 estudiantes dijeron que estudiarían allí", "Existe una demanda real de un lugar tranquilo", "La primera oración es la idea que se sostiene."),
        ("abc", "{F} ¿Cuál es la evidencia del párrafo?", "La encuesta en que 45 de 60 dijeron que estudiarían allí", "Conviene abrir la biblioteca", "Hay demanda real", "El dato de la encuesta respalda la afirmación."),
        ("ab", "En Lengua: ¿qué es la explicación en un párrafo argumentativo?", "El razonamiento que une la evidencia con la afirmación", "Una repetición de la afirmación", "La explicación muestra por qué la evidencia apoya la afirmación."),
        ("abc", "{F} ¿Qué cumple la tercera oración del párrafo?", "Explica por qué la encuesta apoya la afirmación", "Presenta una nueva afirmación", "Repite el dato", "Dice que la encuesta muestra una demanda real."),
        ("abc", "«Los estudiantes estudian poco en casa; ___ conviene abrir la biblioteca en la tarde». ¿Qué conector va?", "por lo tanto", "sin embargo", "en cambio", "La segunda parte es una consecuencia de la primera."),
        ("abc", "«Algunos prefieren estudiar en silencio; ___ otros estudian mejor conversando». ¿Qué conector va?", "en cambio", "porque", "por lo tanto", "La segunda parte opone un caso distinto al de la primera."),
        ("abc", "«Conviene el horario de tarde ___ así más estudiantes pueden estudiar». ¿Qué conector va?", "porque", "sin embargo", "en cambio", "La segunda parte da la razón, es decir, la causa."),
        ("abc", "«Se pensó que nadie usaría el horario de tarde; ___ 45 de 60 estudiantes dijeron que sí lo usarían». ¿Qué conector va?", "sin embargo", "además", "por lo tanto", "La segunda parte contradice lo que se pensaba, así que marca un contraste."),
        ("abc", "{F} Se elimina la tercera oración del párrafo. ¿Qué pasa con el razonamiento?", "Falta la explicación que conecta el dato con la afirmación", "Queda mejor", "Se pierde la evidencia", "Sin explicación el lector debe adivinar la conexión."),
        ("ab", "Un estudiante escribe dos afirmaciones diferentes en un mismo párrafo. ¿Qué conviene hacer?", "Dividirlo en dos párrafos, uno por idea", "Dejarlo igual porque es más corto", "Cada párrafo debe tratar una sola idea principal."),
        ("abc", "{F} Se agrega una oración: «Además, la biblioteca tiene 30 puestos libres cada tarde (de ejemplo)». ¿Qué función cumple «además»?", "Suma otra razón o evidencia", "Marca un contraste", "Introduce una conclusión", "«Además» agrega una razón más en la misma línea."),
        ("abc", "{F} ¿Cuál reescritura mejora la explicación del párrafo?", "Esto muestra que hay estudiantes que no tienen dónde estudiar por la tarde y que la biblioteca podría cubrir esa necesidad", "Esto es todo lo que se puede decir sobre el tema", "Por eso, la biblioteca es un lugar bonito", "La primera detalla por qué el dato apoya la afirmación."),
        ("abc", "Un párrafo dice: «El recreo es corto. Por lo tanto, algunos prefieren un recreo más largo. Sin embargo, el recreo es corto». ¿Qué problema tiene?", "Los conectores no corresponden a las relaciones lógicas entre las ideas", "Está bien", "Le falta una cita", "Se usa «por lo tanto» y «sin embargo» sin sentido lógico."),
    ],
    ctx=("abc", "Una estudiante escribe: «Conviene un horario de estudio en la tarde. En una encuesta de ejemplo, 30 de 50 piden más tiempo para estudiar». ¿Qué le falta para ser un párrafo argumentativo completo?", "Una oración que explique por qué la encuesta apoya la afirmación", "Más adjetivos", "Un título más largo", "Tiene afirmación y evidencia, pero falta la explicación."),
    sc=[
        ("En Lengua: ¿qué tres partes tiene un párrafo argumentativo?", "Afirmación, evidencia y explicación", "Las tres hacen visible el razonamiento."),
        ("¿Qué conector introduce una consecuencia?", "Por lo tanto", "Marca lo que se sigue de lo anterior."),
        ("¿Cuántas ideas principales debe tener un párrafo?", "Una", "La unidad del párrafo exige una sola idea principal."),
    ],
    op=("Elige una afirmación: A) conviene reciclar papel en el liceo, B) conviene un recreo más largo. Escribe un párrafo de cuatro a cinco oraciones con afirmación, una evidencia de ejemplo rotulada, una explicación y al menos dos conectores distintos. Subraya las tres partes.",
        "A. Conviene reciclar papel en el liceo. En un conteo de ejemplo, cada curso desecha 4 kilos de papel al mes. Esto muestra que hay mucho papel que podría reutilizarse. Además, un contenedor por piso facilita la tarea. Por lo tanto, instalar contenedores es una medida simple.",
        ["incluye afirmación, evidencia de ejemplo y explicación", "usa al menos dos conectores distintos con sentido lógico", "trata una sola idea principal"],
        ["párrafo de cuatro a cinco oraciones"],
        ["omitir la explicación", "conectores mal usados", "mezclar dos ideas"],
        "Pregunta: «¿qué conecta tu dato con tu afirmación?»."),
    reinforce="Escribe tres oraciones con los conectores «porque», «sin embargo» y «por lo tanto», cada una con su sentido correcto.",
    extend="Explica por qué «además» y «sin embargo» no pueden intercambiarse sin cambiar el sentido.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 9 (texto base y tres versiones, de ejemplo). Texto base: «En un estudio de ejemplo, 40 estudiantes de un liceo registraron su sueño durante dos semanas. El promedio fue de 7 horas por noche. Quienes durmieron menos de 7 horas reportaron más cansancio en clases». "
     "Versión 1: «En un estudio de ejemplo, 40 estudiantes registraron su sueño durante dos semanas; el promedio fue de 7 horas. Quienes durmieron menos de 7 horas reportaron más cansancio». "
     "Versión 2: «Varios estudiantes que duermen mal están siempre cansados en clases». "
     "Versión 3 (divulgación): «Durante dos semanas, 40 estudiantes anotaron cuántas horas dormían. En promedio dormían 7 horas, y quienes dormían menos contaban sentirse más cansados en clases».")
build(
    O4, 4, F,
    use="Aprenderé a reformular un texto: parafrasear, condensar y expandir, y a transformarlo de un registro o género a otro sin cambiar su sentido. Sirve para adaptar lo que sé a distintos lectores.",
    prior=["Sé parafrasear con la fuente.", "Sé distinguir registro formal y coloquial.", "Sé qué es una audiencia."],
    explain=[
        "Reformular es decir una misma idea de otra manera. La paráfrasis cambia las palabras y la estructura, pero conserva el sentido y los datos. La condensación reduce el texto a lo esencial. La expansión agrega explicaciones, ejemplos o definiciones para quien lee. En todos los casos se debe conservar lo que la fuente afirma: las cifras, las condiciones y los límites.",
        "Transformar un texto es adaptarlo a otra audiencia o a otro género. Una nota de estudio puede convertirse en un párrafo de informe; un informe, en un texto de divulgación. Al hacerlo cambian el registro, los términos y el orden, pero no los datos ni las conclusiones. Un buen control es preguntarse: ¿un lector que solo conoce mi versión entendería lo mismo que uno que leyó el original?",
        "Los errores frecuentes son tres: distorsionar el sentido («más cansados» se vuelve «siempre cansados»), perder datos (omitir el promedio o la cantidad de estudiantes) y agregar afirmaciones que el original no hace. Reformular no es embellecer ni exagerar: es comunicar lo mismo con otras palabras, para otro lector.",
    ],
    vocab=[("parafrasear", "decir una idea con palabras y estructura propias, conservando el sentido"), ("condensar", "reducir un texto a lo esencial"), ("expandir", "agregar explicaciones o ejemplos para quien lee"), ("distorsionar", "cambiar el sentido de lo que dice la fuente"), ("adaptar", "ajustar un texto a otra audiencia o género")],
    worked=[
        ("Detectar una distorsión", "Original: «algunos estudiantes dormían menos de 7 horas». Versión: «todos los estudiantes dormían poco». ¿Qué ocurre?",
         ["«Algunos» se convirtió en «todos».", "Cambia la extensión de la afirmación."],
         "Distorsiona: pasa de algunos a todos"),
        ("Condensar", "Condensa en una oración: «40 estudiantes anotaron su sueño dos semanas; el promedio fue 7 horas; los que durmieron menos se sintieron más cansados».",
         ["Se conservan los datos esenciales: 40 estudiantes, dos semanas, 7 horas.", "Se conserva el resultado."],
         "«En dos semanas, 40 estudiantes promediaron 7 horas de sueño, y quienes durmieron menos reportaron más cansancio»"),
    ],
    mistakes=[("Exagerar al reformular: «siempre cansados» en vez de «más cansados».", "Cambia el alcance de la afirmación.", "Mantén la intensidad y los límites de la fuente."),
              ("Quitar las cifras para que «suene mejor».", "Se pierde información verificable.", "Conserva los datos esenciales aunque cambies las palabras.")],
    T=[
        ("abc", "{F} ¿Qué versión es una condensación fiel del texto base?", "La versión 1", "La versión 2", "Ninguna", "La versión 1 conserva los datos y los resultados con menos palabras."),
        ("abc", "{F} ¿Qué versión distorsiona el sentido del texto base?", "La versión 2", "La versión 1", "La versión 3", "La 2 cambia «más cansancio» por «siempre cansados» y pierde los datos."),
        ("ab", "En Lengua: ¿qué es parafrasear?", "Decir la idea con palabras y estructura propias, conservando el sentido", "Cambiar los datos para que suene mejor", "La paráfrasis no cambia el sentido ni los datos."),
        ("abc", "{F} ¿Qué cambio hace la versión 3 respecto del texto base?", "Lo adapta a un público general con un lenguaje más cercano", "Agrega datos nuevos", "Elimina el resultado", "Mantiene datos y resultado y cambia el registro."),
        ("abc", "{F} Alguien condensa la versión 1 como «los 40 estudiantes dormían 7 horas cada uno». ¿Qué problema hay?", "7 horas es el promedio, no lo que durmió cada estudiante", "Está bien: el promedio y lo que durmió cada uno es lo mismo", "Convirtió una cifra en un porcentaje", "Un promedio resume al grupo; pasarlo a «cada uno» cambia el sentido."),
        ("abc", "{F} La versión 2 omite el dato «40 estudiantes». ¿Qué problema genera?", "No se sabe el tamaño de la muestra y la afirmación parece general", "Mejora la claridad", "Hace el texto más formal", "Sin la muestra no se puede evaluar cuánto respalda la afirmación."),
        ("abc", "Un estudiante expande así «40 estudiantes anotaron su sueño»: «40 estudiantes, es decir, un grupo de un liceo, anotaron cada noche cuántas horas durmieron». ¿Qué agregó?", "Una explicación que aclara cómo se registró el dato", "Una opinión propia", "Un dato nuevo no presente en el original", "La explicación detalla el registro sin cambiar el sentido."),
        ("abc", "{F} Se quiere escribir una versión para especialistas. ¿Qué rasgo conviene?", "Registro formal, términos exactos y cautela", "Expresiones coloquiales", "Omitir las cifras", "Un público especialista espera precisión y cautela."),
        ("ab", "Una compañera dice que, al adaptar un texto a otra audiencia, puede cambiar el resultado para que sea más interesante. ¿Es correcto?", "No: cambian el registro y el orden, no los datos ni las conclusiones", "Sí: lo importante es que atraiga", "Adaptar no autoriza a alterar el contenido."),
        ("abc", "{F} Se expande la versión 3 con una definición. ¿Cuál es adecuada?", "«El promedio es la suma de las horas dividida por la cantidad de estudiantes»", "«El promedio es el número más grande»", "«El promedio es el número más repetido»", "La primera define correctamente el promedio como media aritmética."),
        ("abc", "{F} Una versión dice «dormían 7 horas, es decir, nadie dormía menos». ¿Qué error hay?", "Agrega una afirmación que el original contradice: algunos sí dormían menos de 7 horas", "Está bien", "Es una condensación", "El texto base dice que algunos durmieron menos de 7 horas."),
        ("abc", "{F} ¿Cuál es el mejor control para saber si una reformulación es fiel?", "Preguntarse si quien solo lee la versión entiende lo mismo que quien leyó el original", "Contar las palabras", "Comprobar que suene bonito", "La fidelidad se mide en el sentido y los datos conservados."),
        ("abc", "{F} La versión 3 dice que quienes dormían menos «contaban sentirse más cansados». ¿Cambió el sentido respecto del texto base?", "No: cambia las palabras, pero conserva el resultado y su alcance", "Sí: pasó de lo que reportaron a una certeza", "Sí: agregó un dato nuevo", "«Reportaron más cansancio» y «contaban sentirse más cansados» dicen lo mismo con otras palabras."),
    ],
    ctx=("abc", "Una estudiante debe explicar a niños de básica, sin cambiar el contenido, esta frase: «El 60 % de los estudiantes encuestados prefiere estudiar por la tarde». ¿Qué versión es mejor?", "«De cada 10 estudiantes consultados, 6 prefieren estudiar por la tarde»", "«A casi todos les gusta la tarde»", "«Estudiar de tarde es lo mejor»", "La primera expresa el mismo dato con lenguaje cercano; las otras lo distorsionan."),
    sc=[
        ("En Lengua: ¿qué debe conservar una reformulación?", "El sentido y los datos del original", "Cambia la forma, no el contenido."),
        ("¿Qué es condensar?", "Reducir un texto a lo esencial", "Se eliminan detalles pero se mantienen las ideas principales."),
        ("¿Qué es adaptar un texto?", "Ajustarlo a otra audiencia o género sin cambiar sus datos", "Cambia el registro, no la información."),
    ],
    op=("Texto base de ejemplo: «En una encuesta de ejemplo a 50 estudiantes de un liceo, 30 dijeron usar el celular para estudiar al menos una hora al día. Quienes lo usan más de dos horas reportaron distraerse más». Escribe tres versiones: (1) una condensación de una oración, (2) una versión de divulgación para las familias y (3) una frase que distorsione el texto a propósito, marcando qué se distorsionó.",
        "(1) En una encuesta a 50 estudiantes, 30 usan el celular al menos una hora al día para estudiar, y quienes lo usan más de dos horas reportan más distracción. (2) Se preguntó a 50 estudiantes: 30 usan el celular al menos una hora diaria para estudiar; los que lo usan más de dos horas cuentan distraerse más. (3) Todos los estudiantes se distraen con el celular. Se distorsionó: pasó de algunos a todos.",
        ["la condensación conserva los datos y el resultado", "la versión de divulgación mantiene datos y cambia el registro", "identifica correctamente qué se distorsionó"],
        ["tres versiones y una marca de distorsión"],
        ["perder las cifras", "cambiar el alcance", "agregar datos nuevos"],
        "Pregunta: «¿entendería lo mismo quien solo lee tu versión?»."),
    reinforce="Reformula con otras palabras y conserva el dato: «El 40 % del curso llega en bicicleta».",
    extend="Explica qué riesgos tiene exagerar un resultado al adaptarlo para un público general.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 10 (párrafo con problemas, de ejemplo). «Los estudiantes duermen mal por el celular. Para mejorar el sueño, deberían apagar el celular antes de dormir. Se midió el sueño en un curso, 30 estudiantes (de ejemplo), y 12 dijeron dormir menos de 7 horas. Estos datos prueban que el celular es la causa. Todos los jovenes se duermen tarde, y por ello, el liceo debe prohibir los celulares. Los jovenes y las jovenes necesitan dormir bien. Dormir bien es importante, dormir bien ayuda»."
     )
build(
    O4, 5, F,
    use="Aprenderé a revisar y editar mi texto en tres niveles: contenido, organización y forma. Sirve para mejorar el texto de verdad y no solo corregir lo superficial.",
    prior=["Sé armar un párrafo argumentativo.", "Sé reformular sin cambiar el sentido.", "Sé dar y recibir comentarios."],
    explain=[
        "Revisar es releer con ojos críticos para mejorar el texto. Conviene hacerlo en tres niveles y en este orden. Primero el contenido: ¿la tesis es clara?, ¿la evidencia respalda lo que se afirma?, ¿hay afirmaciones exageradas, como decir que un dato prueba una causa cuando solo muestra una asociación? Luego la organización: ¿las ideas siguen un orden lógico?, ¿cada párrafo trata una sola idea?, ¿hay repeticiones? Por último la forma: ortografía, puntuación, acentos, repeticiones de palabras y estilo.",
        "El orden importa. Corregir tildes en un párrafo que luego se va a reescribir es trabajo perdido. Corregir solo la superficie sin revisar el contenido deja intactos los problemas importantes. Una lista de cotejo ayuda: preguntas cortas para cada nivel que se marcan una a una. Otras técnicas útiles son dejar reposar el texto, leerlo en voz alta y pedir la lectura de otra persona.",
        "Editar es aplicar las decisiones de la revisión: reescribir, reordenar, agregar evidencia, quitar lo sobrante y corregir la forma. Cada cambio debe acercar el texto a su propósito y su audiencia. Un texto no mejora solo porque tenga menos errores de ortografía: mejora cuando lo que dice es verdadero, está bien respaldado y se entiende.",
    ],
    vocab=[("revisión", "relectura crítica para decidir qué mejorar"), ("edición", "aplicación de los cambios decididos"), ("lista de cotejo", "lista de preguntas que se marcan al revisar"), ("causa", "razón por la cual ocurre algo"), ("asociación", "relación entre dos datos que no prueba que uno cause al otro")],
    worked=[
        ("Clasificar un problema de contenido", "Frase: «Estos datos prueban que el celular es la causa». ¿En qué nivel está el problema?",
         ["La frase afirma una causa que los datos no demuestran.", "Eso afecta el contenido."],
         "Contenido"),
        ("Ordenar la revisión", "Hay un error de acentos, una conclusión al comienzo y una afirmación exagerada. ¿Qué se revisa primero?",
         ["La afirmación exagerada es de contenido.", "El orden de la conclusión es de organización y los acentos son de forma."],
         "Primero la afirmación exagerada (contenido)"),
    ],
    mistakes=[("Revisar solo la ortografía y dar el texto por listo.", "El contenido y la organización siguen con problemas.", "Revisa en orden: contenido, organización y forma."),
              ("Corregir tildes antes de reescribir los párrafos.", "Se pierde tiempo en partes que pueden cambiar.", "Deja la forma para el final.")],
    T=[
        ("abc", "{F} ¿Qué problema de contenido tiene la frase «Estos datos prueban que el celular es la causa»?", "Afirma una causa que 12 de 30 con poco sueño no demuestran", "Tiene mala ortografía", "Es muy corta", "Un dato de asociación no prueba causa, y menos con una muestra pequeña."),
        ("ab", "En Lengua: ¿qué es una lista de cotejo?", "Una lista de preguntas que se marcan una a una al revisar", "Un resumen del texto", "Ayuda a no olvidar aspectos al revisar."),
        ("abc", "{F} ¿Qué problema de organización tiene el párrafo?", "Mezcla varias ideas: sueño, celular, prohibición y bienestar", "Falta una coma", "Tiene muchas palabras", "El párrafo no trata una sola idea principal."),
        ("abc", "{F} ¿Qué error de forma aparece en el párrafo?", "«jovenes» sin tilde", "Una cifra mal calculada", "Una tesis ausente", "Debe escribirse «jóvenes» con tilde; es un error de ortografía."),
        ("abc", "{F} ¿Qué afirmación exagerada aparece en el párrafo?", "«Todos los jóvenes se duermen tarde»", "«Se midió el sueño en un curso»", "«12 dijeron dormir menos de 7 horas»", "«Todos» generaliza sin respaldo; los datos son de 30 estudiantes."),
        ("abc", "{F} ¿Qué repetición innecesaria hay en el final del párrafo?", "«Dormir bien es importante, dormir bien ayuda»", "«Se midió el sueño»", "«El liceo debe prohibir»", "Repite la misma idea con casi las mismas palabras sin aportar."),
        ("ab", "¿Qué debe revisarse primero?", "El contenido y la organización", "La ortografía", "Los problemas de fondo pueden obligar a reescribir y vuelven inútil la corrección de forma."),
        ("=", "{F} En la muestra, 12 de 30 estudiantes durmieron menos de 7 horas. ¿Qué porcentaje es?", "12/30*100", "Se divide 12 entre 30 y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Cuál es una reescritura más cuidadosa de «Estos datos prueban que el celular es la causa»?", "Estos datos sugieren una posible relación, pero no permiten concluir que el celular sea la causa", "Los datos son ciertos", "El celular es la causa de todo", "La primera ajusta la afirmación a la evidencia con cautela."),
        ("abc", "Un estudiante corrige todas las tildes y entrega su texto sin revisar la tesis ni las pruebas. ¿Qué error comete?", "Corrige solo la superficie sin atender el contenido", "Revisa demasiado", "Cumple con la revisión completa", "La revisión debe incluir contenido y organización."),
        ("abc", "{F} ¿Cuál técnica ayuda a detectar frases que no suenan bien?", "Leer el texto en voz alta", "Subrayarlo en color", "Contar las palabras", "Al leer en voz alta se perciben repeticiones y frases confusas."),
        ("abc", "{F} ¿Cuál oración del párrafo es la única que entrega un dato verificable?", "«Se midió el sueño en un curso, 30 estudiantes (de ejemplo), y 12 dijeron dormir menos de 7 horas»", "«Los jóvenes y las jóvenes necesitan dormir bien»", "«Dormir bien es importante»", "Solo la primera trae cifras de una muestra concreta; las otras son afirmaciones generales."),
        ("abc", "{F} Si el texto fuera un informe para especialistas, ¿qué cambiaría en la expresión «Todos los jóvenes»?", "Se reemplaza por los datos de la muestra y se limita el alcance", "Se mantiene para dar fuerza", "Se agrega otra generalización", "Un informe exige precisión y alcance acorde con los datos."),
    ],
    ctx=("abc", "Un grupo revisa su informe y encuentra: una cifra sin fuente, dos faltas de ortografía y una conclusión que no se relaciona con la tesis. ¿Qué hace primero?", "Corrige la conclusión y agrega la fuente de la cifra", "Corrige las faltas de ortografía", "Entrega sin cambios", "Los problemas de contenido y organización van antes que los de forma."),
    sc=[
        ("En Lengua: ¿en qué orden se revisa un texto?", "Contenido, organización y forma", "Los problemas de fondo se resuelven antes de la forma."),
        ("¿Qué técnica ayuda a detectar frases confusas?", "Leer en voz alta", "Al leer en voz alta se oyen los tropiezos."),
        ("¿Un dato de asociación prueba una causa?", "No", "Una asociación muestra relación, no que una cosa cause la otra."),
    ],
    op=("Revisa este texto de ejemplo: «El deporte es lo mejor, todos mejoran notas. Se midió en 40 estudiantes y 25 hacen deporte. Esto prueba que el deporte sube las notas. Los estudiantes que hacen deporte son mas felices». Haz una lista de cotejo con tres preguntas (contenido, organización y forma) y reescribe el texto en versión mejorada.",
        "Contenido: ¿afirma más de lo que muestran los datos? Sí («prueba»). Organización: ¿trata una sola idea? No, mezcla notas y felicidad. Forma: «mas» lleva tilde. Versión: En una muestra de 40 estudiantes, 25 hacen deporte. Los datos sugieren una posible relación con las notas, pero no permiten concluir una causa.",
        ["lista con preguntas de los tres niveles", "versión que corrige el contenido y la forma", "mantiene la cautela"],
        ["lista de cotejo y versión mejorada"],
        ["corregir solo ortografía", "mantener «prueba»", "no ajustar el alcance"],
        "Pregunta: «¿qué cambiaste del contenido y qué de la forma?»."),
    reinforce="Revisa esta oración y reescríbela: «Todos los estudiantes duermen mal; esto prueba que el colegio los cansa».",
    extend="Explica por qué dejar reposar un texto uno o dos días ayuda a revisarlo mejor.",
)
