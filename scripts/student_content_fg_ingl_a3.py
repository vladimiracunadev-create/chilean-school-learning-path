"""Cuaderno del estudiante, 4.º medio Inglés (Formación General), OA 01 (información relevante para un propósito) y OA 02 (textos claros con postura crítica y respeto).

Los títulos de clase del plan son genéricos; aquí se aplican así.
OA 01: 1 leer con un objetivo (skimming y scanning), 2 tablas, cifras y relevancia, 3 lenguaje de requisitos y condiciones, 4 fuentes, fiabilidad y perspectivas culturales.
OA 02: 1 correo formal y audiencia, 2 estructura de un ensayo breve, 3 concesión y contraste, 4 comunicar una postura con contraargumento, 5 revisar cohesión y claridad.
Textos originales, glosados, en inglés americano; los datos (precios, fechas, cifras) son de ejemplo.
"""
from __future__ import annotations

from fg_ingl_common import ADULT, MAT_L, MAT_R, arith, ex, lesson, mc, ml, mr, task

OA1 = "FG-INGL-4M-OAC-01"
OA2 = "FG-INGL-4M-OAC-02"


def sc(oa, n, rows):
    return [(f"En Inglés de 4.º medio (OA {oa}, clase {n}): {q}", a, w) for q, a, w in rows]


# ================================================================= OA 01
# ------------------------------------------------------------------ clase 1: leer con un objetivo
PROG = "«Youth Exchange Program (example). Ages: 16 to 18. Length: three weeks in July. Cost: 450 dollars for the program, plus 60 dollars for the application. Requirements: a letter of motivation, a school report and English at intermediate level. Application deadline: April 30. Scholarships: available for families with lower income; ask the school office.» (exchange = intercambio, ages = edades, length = duración, cost = costo, requirements = requisitos, letter of motivation = carta de motivación, school report = certificado de notas, intermediate = intermedio, deadline = fecha límite, scholarships = becas, income = ingresos)"

lesson(
    OA1, 1, MAT_R,
    "Aprenderé a leer con un objetivo claro: definir qué necesito saber, hacer skimming (leer rápido para la idea general) o scanning (buscar un dato puntual) y descartar lo irrelevante. Sirve para encontrar información relevante en textos reales, como programas, avisos y requisitos de otros países.",
    ["Sé encontrar la idea central de un texto.", "Conozco palabras como cost, deadline y requirements."],
    [
        "Leer con un propósito específico (specific purpose) significa partir de una pregunta o necesidad: ¿puedo postular?, ¿cuánto cuesta?, ¿qué documentos necesito?, ¿cuándo cierra el plazo? Esa pregunta decide cómo lees. Con skimming recorres el texto rápido, mirando título, primeras líneas y palabras destacadas, para saber de qué trata. Con scanning buscas un dato concreto (una fecha, un precio, un nombre) y pasas por alto el resto.",
        "La información relevante (relevant information) es la que responde a tu objetivo; el resto es información de contexto o irrelevante para esa tarea. Un mismo texto puede tener datos relevantes para una persona e irrelevantes para otra: una persona de 15 años no cumple Ages: 16 to 18, así que para ella el resto de los requisitos deja de importar. Antes de resolver, subraya palabras clave del objetivo (cost, deadline, ages, documents).",
        "Los avisos y programas usan etiquetas (labels) como Cost, Length, Requirements, Deadline, Scholarships. Reconócelas: son tu mapa. Cuando necesites combinar datos, calcula con cuidado (por ejemplo, el costo total suma el programa y la inscripción). Si falta un dato que necesitas, dilo: el texto no lo informa.",
    ],
    [("specific purpose", "propósito específico"), ("skimming", "leer rápido para la idea general"), ("scanning", "buscar un dato puntual"), ("relevant", "relevante: sirve para el objetivo"), ("deadline", "fecha límite"), ("requirements", "requisitos")],
    [
        ("Buscar un dato", PROG + " Tu objetivo: saber cuándo cierra la postulación. ¿Qué técnica usas y qué dato encuentras?", ["Busco una fecha: uso scanning.", "La etiqueta Application deadline lo indica.", "El dato es April 30."], "Scanning; el plazo cierra el 30 de abril"),
        ("Decidir si es relevante", PROG + " Tu objetivo: saber si puedes postular a los 15 años. ¿Qué dato decide?", ["Busco la etiqueta de edad.", "Ages: 16 to 18.", "A los 15 años no cumples la edad."], "Ages: 16 to 18; no puedes postular a los 15"),
    ],
    [
        ("Leer palabra por palabra todo el texto cuando solo buscas una fecha.", "Se pierde tiempo y se confunden los datos.", "Define el objetivo y usa scanning."),
        ("Sumar datos que no corresponden al objetivo.", "Se mezclan cifras de otro tema.", "Subraya solo los datos relevantes antes de calcular."),
    ],
    [
        mr(PROG, "Tu objetivo: saber cuántas semanas dura el programa. ¿Qué etiqueta buscas?", "Length", ["Cost", "Ages"], "Length indica la duración."),
        mr(PROG, "Tu objetivo: conocer los documentos que debes preparar. ¿Qué etiqueta buscas?", "Requirements", ["Scholarships", "Length"], "Los documentos aparecen en Requirements."),
        mr(PROG, "Tu objetivo: saber cuánto debes pagar por el programa sin contar la inscripción. ¿Cuál es la cifra?", "450 dólares", ["60 dólares", "510 dólares"], "El programa cuesta 450; los 60 son de la inscripción."),
    ],
    [
        mr(PROG, "Tu objetivo: saber cuándo debes enviar tu postulación. ¿Qué dato NO necesitas?", "el costo del programa", ["la fecha límite", "los requisitos de documentos"], "El costo no sirve para saber el plazo."),
        mr(PROG, "Tu objetivo: buscar ayuda económica. ¿Qué línea es la más relevante?", "Scholarships: available for families with lower income; ask the school office", ["Ages: 16 to 18; students need English at intermediate level", "Length: three weeks in July; the program costs 450 dollars"], "Habla de becas."),
        mc("Debes decidir si un artículo largo sirve para tu trabajo. ¿Qué técnica usas primero?", "skimming: leer título, primeras líneas y palabras destacadas", ["scanning de una sola palabra sin leer nada más", "traducir todo el texto"], "El skimming da la idea general rápidamente."),
    ],
    [
        arith(PROG + " Tu objetivo: calcular el pago inicial total (programa más inscripción). ¿Cuántos dólares son?", "450+60", "Se suman el costo del programa y de la inscripción.", " dólares"),
        arith(PROG + " Supón que una beca de ejemplo cubre 200 dólares del programa. ¿Cuánto queda por pagar del programa, sin contar la inscripción?", "450-200", "Se resta la beca del costo del programa.", " dólares"),
        arith(PROG + " El programa dura tres semanas. ¿Cuánto cuesta el programa por semana, sin la inscripción?", "450//3", "Se divide el costo entre las semanas.", " dólares"),
    ],
    [
        mr(PROG, "Una estudiante de 17 años quiere saber qué debe presentar y en qué nivel de inglés. ¿Qué respuesta es la mejor?", "una carta de motivación, un certificado de notas y inglés intermedio", ["ninguna carta; solo el certificado y un inglés básico", "solo los 450 dólares y la fecha de nacimiento"], "Los requisitos incluyen esos tres elementos."),
        mc("Un compañero dice que, para saber si puede viajar en julio, necesita leer todo el aviso con atención. ¿Qué le sugieres?", "buscar con scanning Length y confirmar con Ages", ["leer cada palabra del aviso sin ningún objetivo", "ignorar el aviso y preguntar a un compañero"], "El objetivo permite buscar solo los datos necesarios."),
    ],
    [
        mc("Tu objetivo es saber si hay becas. Un compañero contesta usando 'Ages: 16 to 18'. ¿Qué error cometió?", "usó un dato irrelevante para su objetivo", ["leyó demasiado rápido y se saltó el dato", "no leyó la palabra Ages del aviso"], "Ages no responde sobre becas."),
        mr(PROG, "Una familia pregunta si el texto dice cuánto dinero cubre una beca. ¿Qué debes responder?", "el texto no lo informa; hay que preguntar a la oficina del colegio", ["cubre 200 dólares del costo del programa, según el aviso", "cubre todo el costo del programa completo, según el aviso"], "Solo dice que existen becas y dónde preguntar."),
    ],
    [mc("Un aviso dice: «Free entry for students under 12. Adults pay 5 dollars.» (entry = entrada). Tu hermana tiene 10 años. ¿Cuánto paga?", "nada, la entrada es gratis", ["5 dólares, igual que los adultos", "no se sabe, porque falta la edad"], "Under 12 incluye a una niña de 10 años.")],
    sc(1, 1, [
        ("¿Qué es el scanning?", "Buscar un dato puntual en un texto", "Se usa para encontrar fechas, precios o nombres."),
        ("¿Qué es el skimming?", "Leer rápido para captar la idea general", "Usa título, primeras líneas y palabras destacadas."),
        ("¿Qué hacer si un dato necesario no está en el texto?", "Decir que el texto no lo informa", "No se debe inventar una respuesta."),
    ]),
    task("Lee este aviso de ejemplo: «Language Club (example). Meets Tuesdays at 5 p.m. Level: beginner. Cost: 20 dollars per month. Bring a notebook. Sign up before October 10.» (meets = se reúne, sign up = inscribirse). Escribe en español, para tres objetivos distintos (cuándo, cuánto y hasta cuándo inscribirse), qué técnica usas y qué dato respondes.", "Cuándo: scanning de Meets; los martes a las 5 p.m. Cuánto: scanning de Cost; 20 dólares al mes. Hasta cuándo: scanning de Sign up; antes del 10 de octubre.", ["usa la técnica adecuada", "da el dato correcto", "ignora la información que no sirve"], ["tres respuestas en español"], ["responder con un dato de otra etiqueta", "no indicar la técnica"], "Vuelve a subrayar la etiqueta que corresponde a cada objetivo."),
    "Busca en un papel de tu casa (boleta o aviso) tres datos concretos y escribe qué etiqueta usaste.",
    "Escribe tres objetivos de lectura distintos para un mismo aviso.",
)

# ------------------------------------------------------------------ clase 2: tablas, cifras y relevancia
COURSES = "«Course list (example): Photography, Mondays 4 p.m., 40 dollars. Cooking, Wednesdays 5 p.m., 55 dollars. Public speaking, Fridays 3 p.m., 35 dollars. Coding, Mondays 6 p.m., 60 dollars. Note: all courses last eight weeks. Students under 18 need a parent's signature.» (course = curso, public speaking = hablar en público, coding = programación, last = durar, signature = firma, under = menor de)"

lesson(
    OA1, 2, MAT_R,
    "Aprenderé a leer listas, tablas y cifras en inglés, a filtrar datos relevantes para una necesidad (horario, precio, requisito) y a detectar pistas como notas al pie. Sirve para decidir con información clara y reconocer cómo organizan los datos otras culturas.",
    ["Sé leer con un objetivo y usar scanning.", "Sé decir horas, días y precios en inglés."],
    [
        "Muchos textos presentan datos en listas o tablas: cada línea tiene el nombre, el día, la hora y el precio, separados por comas. Para extraer lo relevante, identifica primero tu criterio (day, time, price) y revisa cada línea con ese criterio. Marca las líneas que cumplen y descarta las que no. Las abreviaturas comunes son Mon, Tue, Wed, Thu, Fri, Sat, Sun; a.m. es antes del mediodía y p.m. después.",
        "Las notas (Note:) agregan condiciones que afectan a todos o a algunos: Note: all courses last eight weeks; Students under 18 need a parent's signature. Una nota puede cambiar una decisión, así que léela siempre. También hay palabras que filtran, como only, except, at least, at most y no more than. Una persona de 17 años queda incluida en under 18; una de 18 no.",
        "Al calcular con datos de una tabla, usa solo las filas pertinentes y apunta las unidades (dollars, hours, weeks). Si hay choques de horario (dos cursos al mismo tiempo) o de día, descarta uno. Siempre revisa si el texto dice algo sobre lo que te preguntan, y si no, di que no se informa.",
    ],
    [("Mon / Tue / Wed / Thu / Fri", "lun / mar / mié / jue / vie"), ("a.m. / p.m.", "antes / después del mediodía"), ("note", "nota: condición adicional"), ("under 18", "menor de 18"), ("at least / at most", "al menos / como máximo"), ("clash", "choque de horario")],
    [
        ("Filtrar por día", COURSES + " ¿Qué curso es el viernes?", ["Busco la palabra Fridays.", "Aparece en Public speaking.", "Es el único curso del viernes."], "Public speaking"),
        ("Leer una nota", COURSES + " Tienes 17 años. ¿Qué necesitas además del dinero?", ["Busco una nota que hable de edad.", "Dice Students under 18 need a parent's signature.", "A los 17 se aplica."], "La firma de uno de tus padres o tutores"),
    ],
    [
        ("Ignorar la nota final de una lista.", "Las notas pueden cambiar la decisión.", "Léelas siempre antes de decidir."),
        ("Calcular con filas que no se eligieron.", "Se suman cifras de cursos que no se tomarán.", "Marca primero las filas pertinentes."),
    ],
    [
        mr(COURSES, "¿A qué hora es Cooking?", "a las 5 p.m. los miércoles", ["a las 3 p.m. los viernes", "a las 6 p.m. los lunes"], "La línea de Cooking indica Wednesdays 5 p.m."),
        mr(COURSES, "¿Cuántas semanas dura cada curso?", "ocho", ["cuatro", "tres"], "La nota dice all courses last eight weeks."),
        mr(COURSES, "¿Cuántos cursos son los lunes?", "dos", ["uno", "tres"], "Photography y Coding son los lunes."),
    ],
    [
        mr(COURSES, "Tienes fútbol los lunes y los viernes. ¿Qué curso no choca con tus entrenamientos?", "Cooking", ["Photography", "Public speaking"], "Es el único que no es lunes ni viernes."),
        mr(COURSES, "Solo puedes empezar después de las 5:30 p.m. ¿Cuál curso cumple?", "Coding", ["Photography", "Public speaking"], "Coding empieza a las 6 p.m.; los otros, antes de las 5:30."),
        mr(COURSES, "¿Qué curso es el más barato?", "Public speaking", ["Photography", "Coding"], "Cuesta 35 dólares, menos que los demás."),
    ],
    [
        arith(COURSES + " Dos amigas toman Photography y Public speaking. ¿Cuántos dólares pagan en total?", "40+35", "Se suman los dos precios.", " dólares"),
        arith(COURSES + " Alguien se inscribe en Cooking y en Coding. ¿Cuántos dólares paga?", "55+60", "Se suman Cooking y Coding.", " dólares"),
        arith(COURSES + " Un estudiante de ejemplo tiene 100 dólares y paga Coding. ¿Cuántos dólares le quedan?", "100-60", "Se resta el precio de Coding.", " dólares"),
    ],
    [
        mc("Un estudiante dice que Cooking y Coding se pueden tomar juntos porque los dos son por la tarde. Según la lista, ¿qué respuesta es correcta?", "sí, pueden tomarse: Cooking es el miércoles y Coding el lunes", ["no, chocan porque ambos son por la tarde y empiezan temprano", "no, porque son del mismo día de la semana y a la misma hora"], "Están en días distintos, así que no chocan."),
        mr(COURSES, "Un estudiante de 18 años pregunta si necesita la firma de uno de sus padres. ¿Qué respondes?", "no, la nota se aplica a menores de 18", ["no se sabe, porque la nota no habla de edades", "sí, siempre, porque todos necesitan firma"], "Under 18 no incluye a quien ya tiene 18."),
    ],
    [
        mr(COURSES, "Quieres tomar dos cursos, sin que choquen los días, con un total de máximo 80 dólares. ¿Qué pareja sirve?", "Photography y Public speaking", ["Coding y Photography", "Cooking y Coding"], "Photography y Public speaking suman 75 y están en días distintos; Coding con Photography suma 100 y Cooking con Coding suma 115."),
        mc("Un amigo dice que el curso de Coding cuesta 60 dólares por semana. ¿Qué le respondes?", "la lista no lo dice así: da un precio por curso y que dura ocho semanas", ["tiene razón, el precio es de 60 dólares por cada semana de curso", "el precio no se puede saber con esta lista de cursos del colegio"], "El precio es por curso, no por semana."),
    ],
    [mc("En un cartel ves: «Open Mon to Fri, 9 a.m. to 5 p.m. Closed on Sat and Sun.» (closed = cerrado). ¿Puedes ir un sábado?", "no, el sábado está cerrado", ["sí, de 9 a 5 como los demás días", "no se informa si abre los sábados"], "Closed on Sat indica cierre.")],
    sc(1, 2, [
        ("¿Qué significan las abreviaturas a.m. y p.m.?", "Antes y después del mediodía", "Sirven para leer horas."),
        ("¿Qué es una nota en un listado?", "Una condición adicional que puede cambiar la decisión", "Se lee siempre."),
        ("¿Qué significa at most?", "Como máximo", "Marca un límite superior."),
    ]),
    task("Lee esta tabla de ejemplo: «Bus passes: Student, 20 dollars per month; Adult, 35 dollars per month; Senior, 15 dollars per month. Note: student passes need a school ID.» (pass = pase, senior = persona mayor, ID = carné). Responde en español cuánto paga un estudiante en tres meses, qué necesita para el pase y cuánto más paga un adulto que un estudiante por mes.", "Tres meses de pase estudiantil: 20 × 3 = 60 dólares. Necesita un carné escolar. El adulto paga 15 dólares más por mes (35 − 20).", ["calcula 60", "menciona el carné", "calcula la diferencia 15"], ["tres respuestas con cálculo"], ["usar el precio del adulto para el estudiante", "olvidar la nota"], "Subraya las filas pertinentes y la nota antes de calcular."),
    "Haz una lista de tres cursos de ejemplo con día, hora y precio, y plantea dos preguntas sobre ella.",
    "Busca un horario de tu casa (bus, tienda) y escribe una pregunta de filtro con at least o at most.",
)

# ------------------------------------------------------------------ clase 3: lenguaje de requisitos y condiciones
REQ = "«Application guidelines of a university abroad (example): Applicants must submit their documents no later than May 1. Interviews are optional unless the applicant is under 18. Students are eligible for a scholarship provided that they maintain good grades. Documents sent after the deadline will not be accepted.» (applicants = postulantes, submit = entregar, no later than = a más tardar, optional = opcional, unless = a menos que, eligible = elegible, provided that = siempre que, maintain = mantener, grades = notas, accepted = aceptados)"

lesson(
    OA1, 3, MAT_R,
    "Aprenderé el lenguaje de requisitos y condiciones (must, required, eligible, no later than, unless, provided that, as long as) y a aplicarlo a un caso concreto. Sirve para entender qué se exige en convocatorias y trámites de otras culturas y decidir qué hacer.",
    ["Sé buscar datos con scanning.", "Conozco must y if."],
    [
        "Los textos de requisitos usan verbos de obligación y de permiso: must y are required to (obligatorio), need to (necesidad), may (permitido), are not allowed to (prohibido), are eligible for (cumplen las condiciones para). Las fechas límite se expresan con no later than, by o before: no later than May 1 significa que el último día es el 1 de mayo; before May 1 deja fuera el 1 de mayo. Los plazos incumplidos suelen indicarse con will not be accepted.",
        "Las condiciones se marcan con unless (a menos que), provided that, as long as (siempre que), if y otherwise (de lo contrario). Unless es negativa: Interviews are optional unless the applicant is under 18 significa que la entrevista es obligatoria si es menor de 18. Provided that y as long as exigen que se cumpla algo para obtener el beneficio: eligible for a scholarship provided that they maintain good grades.",
        "Para aplicar los requisitos a un caso, haz una lista: ¿qué debo entregar?, ¿hasta cuándo?, ¿qué condiciones debo cumplir?, ¿qué pasa si no las cumplo? Evita asumir lo que el texto no dice. Si una frase tiene dos condiciones (por ejemplo edad y notas), comprueba cada una por separado antes de concluir.",
    ],
    [("must / required", "obligatorio"), ("no later than", "a más tardar"), ("unless", "a menos que"), ("provided that / as long as", "siempre que"), ("eligible", "elegible: cumple las condiciones"), ("otherwise", "de lo contrario")],
    [
        ("Aplicar una condición con unless", REQ + " Tienes 17 años. ¿La entrevista es obligatoria u opcional para ti?", ["La frase dice optional unless the applicant is under 18.", "Tienes 17, así que eres menor de 18.", "Se aplica el unless: es obligatoria."], "Obligatoria, porque eres menor de 18"),
        ("Aplicar un plazo", REQ + " Envías tus documentos el 2 de mayo. ¿Se aceptan?", ["El límite es no later than May 1.", "El 2 de mayo es después del 1.", "Documents sent after the deadline will not be accepted."], "No se aceptan, porque llegaron después de la fecha límite"),
    ],
    [
        ("Entender unless como si fuera because.", "Unless introduce una excepción, no una causa.", "Traduce unless como a menos que."),
        ("Pensar que before May 1 y no later than May 1 son lo mismo.", "Before deja fuera el 1 de mayo; no later than lo incluye.", "Lee con atención la preposición."),
    ],
    [
        mr(REQ, "¿Hasta cuándo se pueden entregar los documentos?", "hasta el 1 de mayo inclusive", ["hasta el 2 de mayo", "solo antes del 1 de mayo"], "No later than May 1 incluye el 1 de mayo."),
        mr(REQ, "¿Qué ocurre con los documentos enviados después de la fecha límite?", "no se aceptan", ["se aceptan con multa", "se aceptan solo si hay entrevista"], "El texto dice will not be accepted."),
        mc("¿Qué significa unless?", "a menos que", ["siempre que", "por lo tanto"], "Unless introduce una excepción."),
    ],
    [
        mr(REQ, "¿Cuándo es opcional la entrevista?", "cuando la persona tiene 18 años o más", ["cuando la persona es menor de 18", "cuando no entrega documentos"], "Optional unless under 18 significa que solo los menores deben ir."),
        mr(REQ, "¿Qué condición se exige para obtener una beca?", "mantener buenas notas", ["ser mayor de edad", "entregar los documentos antes del 1 de abril"], "Provided that they maintain good grades."),
        mc("¿Qué frase significa 'siempre que'?", "as long as", ["even though", "in spite of"], "As long as es equivalente a provided that."),
    ],
    [
        mr(REQ, "Una estudiante de 18 años con buenas notas entrega todo el 30 de abril. ¿Qué es cierto?", "está a tiempo, la entrevista es opcional y es elegible para beca", ["debe ir a una entrevista obligatoria y está a tiempo", "llegó tarde, pero la entrevista es opcional"], "Cumple el plazo, no es menor de 18 y mantiene buenas notas."),
        mr(REQ, "Un estudiante de 16 años con buenas notas entrega todo el 1 de mayo. ¿Qué es cierto?", "está a tiempo, debe ir a entrevista y es elegible para beca", ["no está a tiempo, pero sí debe ir a entrevista", "está a tiempo, y la entrevista es opcional"], "El 1 de mayo está permitido; como es menor de 18, la entrevista es obligatoria."),
        mc("Completa (fee = tarifa, process = tramitar): 'You must pay the fee; ___, we cannot process your form.'", "otherwise", ["unless", "provided that"], "Otherwise indica la consecuencia de no cumplir."),
    ],
    [
        mr(REQ, "Un compañero dice que las notas no importan porque cualquier estudiante tiene beca. ¿Qué respondes?", "falso: la beca exige mantener buenas notas", ["verdadero: nada se exige para una beca", "no se puede saber, el texto no habla de becas"], "Provided that exige una condición."),
        mc("Dos reglas: 'You may use a dictionary.' y 'You must not use your phone.' ¿Qué diferencia hay?", "may permite y must not prohíbe", ["las dos reglas obligan a hacer algo", "las dos reglas permiten hacer algo"], "May es permiso; must not es prohibición."),
    ],
    [
        mr(REQ, "Una estudiante entrega un documento el 30 de abril, pero le falta uno. Entrega el faltante el 3 de mayo. ¿Qué ocurre con el faltante?", "no se acepta, porque llegó después de la fecha límite", ["se acepta si hay una entrevista después", "se acepta por tener buenas notas"], "Los documentos después del plazo no se aceptan."),
        mc("¿Qué reformulación mantiene el significado de 'Interviews are optional unless the applicant is under 18'?", "Only applicants under 18 must attend an interview", ["All applicants must attend an interview", "No applicant has an interview"], "Solo los menores de 18 deben asistir."),
    ],
    [mc("En un aviso lees: «You may enter only if you have a ticket.» (enter = entrar). Si no tienes un ticket, ¿puedes entrar?", "no", ["sí", "solo los fines de semana"], "Only if exige tener ticket.")],
    sc(1, 3, [
        ("¿Qué significa no later than?", "A más tardar, incluyendo ese día", "Marca el último día permitido."),
        ("¿Cómo se dice siempre que en inglés (condición)?", "Provided that o as long as", "Ambas expresan condición."),
        ("¿Qué significa otherwise?", "De lo contrario", "Anuncia la consecuencia de no cumplir."),
    ]),
    task("Lee estos requisitos de ejemplo: «To join the volunteer program, applicants must be at least 16 and bring a signed permission form. Meetings are on Saturdays unless there is a public holiday. Volunteers are eligible for a certificate provided that they attend six meetings.» (volunteer = voluntario, permission form = autorización firmada, certificate = certificado, attend = asistir). Escribe en español tres frases con condiciones que apliquen a una persona de 15 años y a otra de 17 que asiste a cinco reuniones.", "Con 15 años no puede postular, pues se pide tener al menos 16. Con 17 y una autorización firmada sí puede unirse, pero con cinco reuniones aún no es elegible para el certificado, porque se exigen seis.", ["aplica la condición de edad", "aplica la condición de asistencia", "no inventa datos"], ["tres frases"], ["no usar la condición de seis reuniones", "confundir at least con at most"], "Subraya los números y compara cada caso con ellos."),
    "Escribe cuatro requisitos de ejemplo para un club de tu elección usando must, unless y provided that.",
    "Busca una norma de tu casa o colegio y reescríbela en inglés con unless.",
)

# ------------------------------------------------------------------ clase 4: fuentes, fiabilidad y perspectivas culturales
GAP = "«In some countries, many students take a year off between school and university to work or travel. In others, most students go directly to university. Studies suggest that a gap year can help some students decide what to study, but it is not clear that it benefits everybody.» (take a year off = tomarse un año libre, gap year = año sabático, studies suggest = los estudios sugieren, benefit = beneficiar; texto de ejemplo)"
SRC1 = "«Source 1: a personal blog by a student who took a gap year. Title: 'My best decision ever'. No data. Written for entertainment.» (source = fuente, blog = blog, entertainment = entretención)"
SRC2 = "«Source 2: a report by an education research center that surveyed 2,000 students and lists its methods. Title: 'Gap year outcomes'. Written to inform schools.» (report = informe, surveyed = encuestó, methods = métodos, outcomes = resultados; ejemplo)"

lesson(
    OA1, 4, MAT_R,
    "Aprenderé a evaluar la relevancia y fiabilidad de una fuente (autor, propósito, evidencia) y a comparar cómo distintas culturas abordan un tema para tomar una postura informada. Sirve para comprender información relevante con sentido crítico.",
    ["Sé extraer datos relevantes para un objetivo.", "Sé distinguir hechos de opiniones."],
    [
        "Una fuente (source) es el origen de la información. Para decidir si es fiable (reliable) pregunta quién la escribió, para qué (propósito), qué evidencia da y cuándo se escribió. Un blog personal sin datos expresa una experiencia; un informe que explica sus métodos y cuántas personas encuestó entrega más evidencia, aunque también debes preguntarte quién lo financió y a quién representan los datos.",
        "Una fuente puede ser relevante pero poco fiable, o fiable pero poco relevante para tu objetivo. Si necesitas decidir si tomarte un año libre, el informe sobre resultados es más útil que un blog con anécdotas. Verbos como suggest, may, can y not clear indican prudencia: no afirman que algo ocurre siempre. Distingue entre lo que el texto asegura (is) y lo que sugiere (may).",
        "Los textos de otras culturas muestran formas distintas de resolver un mismo asunto: en algunos lugares es común tomarse un año antes de la universidad y en otros no. Describir esas diferencias sin juzgarlas es parte de entender una cultura. Una postura crítica combina evidencia, matiz y respeto: puedes decir I would consider a gap year if it has a clear plan, without saying it is right for everybody.",
    ],
    [("source", "fuente"), ("reliable", "fiable"), ("evidence", "evidencia"), ("survey", "encuesta"), ("suggest / may", "sugerir / puede"), ("gap year", "año sabático")],
    [
        ("Comparar fuentes", SRC1 + " " + SRC2 + " ¿Cuál fuente aporta más evidencia y por qué?", ["Busco datos y métodos.", "La fuente 2 encuestó a 2.000 estudiantes y muestra sus métodos.", "La fuente 1 no tiene datos."], "La fuente 2, porque tiene datos y explica sus métodos"),
        ("Distinguir prudencia", GAP + " ¿Qué indica la frase it is not clear that it benefits everybody?", ["Es una frase prudente.", "Indica que no se asegura que sea beneficioso para todos.", "Hay matiz, no certeza."], "Que no se puede afirmar que beneficie a todos"),
    ],
    [
        ("Creer que lo más emocionante es lo más fiable.", "Un título entusiasta no es evidencia.", "Mira datos, métodos y propósito."),
        ("Presentar 'puede ayudar' como si fuera 'ayuda siempre'.", "Se pierde el matiz que el texto escribió.", "Conserva may, can y suggest en tu resumen."),
    ],
    [
        mr(SRC1, "¿Con qué propósito se escribió la fuente 1?", "entretener", ["informar a los colegios con datos", "vender cursos"], "El texto dice Written for entertainment."),
        mr(SRC2, "¿Cuántos estudiantes encuestó la fuente 2?", "dos mil", ["doscientos", "veinte"], "El texto dice 2,000 students."),
        mr(GAP, "¿Qué hacen algunos estudiantes de ciertos países?", "se toman un año libre antes de la universidad", ["no estudian nunca después del colegio", "trabajan solo mientras están en la universidad"], "Dice many students take a year off between school and university."),
    ],
    [
        mc(SRC1 + " " + SRC2 + " Tu objetivo es decidir si tomarte un año libre. ¿Qué fuente es más útil?", "el informe de resultados con datos", ["el blog con anécdotas personales", "ninguna de las dos fuentes sirve"], "Aporta evidencia sobre resultados."),
        mr(GAP, "¿Qué sugieren los estudios del texto?", "que un año libre puede ayudar a algunos a decidir qué estudiar", ["que todos deben tomarse un año libre antes de la universidad", "que un año libre es perjudicial para todos los estudiantes"], "Dice can help some students decide."),
        mc("¿Cuál palabra expresa prudencia?", "may", ["always", "everyone"], "May indica posibilidad."),
    ],
    [
        mc(GAP + " Un compañero resume el texto así: 'Taking a gap year helps everybody.' ¿Qué problema tiene?", "pierde el matiz: el texto dice que puede ayudar a algunos", ["no habla de la universidad en ninguna parte", "es demasiado corto para ser un resumen"], "No se afirma para todos."),
        mc(GAP + " ¿Cuál resumen respeta las dos formas de abordar el tema?", "In some places, many students take a year off; in others, most go directly to university", ["Everybody takes a year off before university, because it is the best choice for all", "Nobody takes a year off before university, because it is a waste of time for all"], "Muestra ambas prácticas sin generalizar."),
        mc("Una fuente anónima dice 'Experts agree' pero no nombra a ningún experto. ¿Qué haces?", "pedir fuentes verificables antes de confiar", ["ignorar el tema porque nadie lo sabe", "confiar porque dice que son expertos"], "Las afirmaciones sin evidencia son poco fiables."),
    ],
    [
        mc(GAP + " Debes escribir una recomendación para una amiga que duda. Usando este texto, ¿cuál es la mejor postura?", "I would consider a gap year if it has a clear plan, but it may not be right for everybody", ["Everybody must take a gap year before university, because it helps all students", "A gap year is a waste of time for every student who wants to study later"], "Es una postura con matiz y condición."),
        mc("¿Qué criterio NO mejora la fiabilidad de una fuente?", "que tenga muchas imágenes", ["que explique sus métodos", "que indique quién la escribió"], "Las imágenes no son evidencia."),
    ],
    [
        mc("Dos textos tratan el mismo tema desde culturas distintas: uno dice que es común vivir con la familia durante los estudios y el otro que es común independizarse al terminar el colegio. ¿Qué es lo más respetuoso?", "describir ambas formas sin decir cuál es la correcta", ["decir que una de las dos formas está equivocada", "ignorar el tema para no ofender a nadie"], "Se comprenden las diferencias sin jerarquizarlas."),
        mc("Lees en un informe: 'Most students surveyed (62%) said they felt more focused after a gap year.' Un compañero dice que eso vale para todos los estudiantes del mundo. ¿Qué respondes?", "no: los datos son de los estudiantes encuestados, no de todos", ["sí, el 62% es una cifra mundial", "no importa, porque una cifra siempre es válida"], "Una muestra no representa a todos."),
    ],
    [mc("Quieres decidir si confías en una fuente. ¿Qué pregunta no te ayuda?", "¿cuántas veces la han compartido en redes?", ["¿quién la escribió y para qué", "¿qué evidencia da y de dónde viene"], "Ser compartida no prueba que sea fiable.")],
    sc(1, 4, [
        ("¿Qué criterios sirven para evaluar una fuente?", "Autor, propósito, evidencia y fecha", "Permiten juzgar su fiabilidad."),
        ("¿Qué indica la palabra may?", "Posibilidad, no certeza", "Es una palabra prudente."),
        ("¿Por qué una muestra no representa a todos?", "Porque solo incluye a quienes respondieron", "Se debe indicar quiénes fueron."),
    ]),
    task("Lee estas dos fuentes de ejemplo sobre estudiar con música. F1: «A friend told me music helps her focus. It works for everybody.» F2: «A study of 400 students suggests that quiet music may help some students focus, but loud music can make concentration harder.» (focus = concentrarse, study = estudio, loud = fuerte). Escribe en español cuál es más fiable, por qué, y una postura propia de una oración con cautela.", "F2 es más fiable: tiene una muestra de 400 estudiantes y usa palabras prudentes (suggests, may, can). F1 es una opinión sin evidencia. Postura: Yo probaría música suave al estudiar, pero no creo que sirva para todos.", ["compara las dos fuentes", "usa evidencia para justificar", "plantea una postura con matiz"], ["tres respuestas en español"], ["decir que F1 es más fiable porque dice everybody", "no usar prudencia"], "Vuelve a buscar datos y palabras de cautela en cada fuente."),
    "Elige un artículo de una revista en inglés o español y anota tres criterios para evaluar su fiabilidad.",
    "Escribe dos frases sobre un tema usando may y suggest.",
)

# ================================================================= OA 02
# ------------------------------------------------------------------ clase 1: correo formal y audiencia
MAIL = "«Subject: Request for information about the debate club. Dear Mr. Vera, I am writing to ask whether students in fourth year can join the debate club. I am interested because I would like to improve my public speaking. Could you please tell me the meeting times? Thank you for your time. Sincerely, Camila Soto» (subject = asunto, debate club = club de debate, fourth year = cuarto medio, improve = mejorar, public speaking = hablar en público, meeting times = horarios de reunión, sincerely = atentamente)"

lesson(
    OA2, 1, MAT_R,
    "Aprenderé a escribir un correo formal claro: asunto, saludo, propósito en la primera frase, una petición cortés y cierre. Sirve para producir textos adecuados a su audiencia y propósito, expresando también una postura personal con respeto.",
    ["Sé planificar propósito, audiencia y postura.", "Sé usar Could you y I would like to."],
    [
        "Un correo formal (formal email) se escribe a una persona que no es tu par: un profesor, una directora, una empresa. Tiene seis partes: asunto (subject) que resume el tema, saludo (Dear Mr. Vera), propósito en la primera frase (I am writing to ask / to request / to complain / to apply), desarrollo con las razones, petición cortés (Could you please...?) y cierre (Thank you for your time. Sincerely, o Best regards, + nombre).",
        "El registro formal usa frases completas, evita abreviaciones y contracciones (do not en lugar de don't), no usa emojis ni jerga y prefiere palabras como request, regarding, I would appreciate. El tono es cortés incluso al criticar: I am concerned that..., I would like to suggest... en vez de This is terrible. Una postura personal se expone con razones: I believe that... because...",
        "Antes de enviar, revisa la audiencia (¿le escribo a una persona que no conozco?), el propósito (¿pido, informo, me quejo?), la claridad (¿se entiende en la primera línea?) y la brevedad: un correo debe ser corto. Los correos informales (a un amigo) pueden usar Hi, contracciones y frases más cortas.",
    ],
    [("subject", "asunto"), ("Dear Mr. / Ms.", "estimado/a señor/a"), ("I am writing to", "le escribo para"), ("Could you please", "¿podría, por favor"), ("Thank you for your time", "gracias por su tiempo"), ("Sincerely", "atentamente")],
    [
        ("Reconocer el propósito", MAIL + " ¿Cuál es el propósito del correo?", ["Busco I am writing to.", "Dice I am writing to ask whether students in fourth year can join.", "El propósito es consultar si pueden unirse y pedir horarios."], "Consultar si estudiantes de cuarto medio pueden unirse y pedir los horarios"),
        ("Formal o informal", "¿Cuál inicio es más formal? A) Hey Mr. Vera, wanna chat? B) Dear Mr. Vera, I am writing to request information.", ["Dear y I am writing to request son formales.", "Hey y wanna son informales.", "La opción B es formal."], "B) Dear Mr. Vera, I am writing to request information."),
    ],
    [
        ("Empezar el correo con una larga historia antes del propósito.", "El lector no entiende qué se pide.", "Escribe el propósito en la primera frase."),
        ("Usar emojis y jerga en un correo formal.", "Resta formalidad.", "Usa frases completas y cortesía."),
    ],
    [
        mr(MAIL, "¿Cuál es el asunto del correo?", "Request for information about the debate club", ["Dear Mr. Vera, about the debate club", "Sincerely, Camila Soto from fourth year"], "El asunto está después de Subject."),
        mr(MAIL, "¿Qué pide Camila?", "los horarios de reunión", ["una nota", "un permiso para salir"], "Dice Could you please tell me the meeting times?"),
        mr(MAIL, "¿Cómo cierra Camila el correo?", "con una frase de cortesía y su nombre", ["con un chiste sobre el club de debate", "con una queja sobre los horarios"], "Cierra con Thank you for your time y Sincerely, Camila Soto."),
    ],
    [
        mr(MAIL, "¿Qué razón da Camila?", "quiere mejorar su manera de hablar en público", ["quiere ganar una competencia de debate", "quiere cambiarse de curso este año"], "Dice I would like to improve my public speaking."),
        mc("¿Qué saludo es adecuado para una directora que no conoces bien?", "Dear Ms. Rojas,", ["Hi Rojas!", "Hey!"], "Dear + título y apellido es formal."),
        mc("¿Cuál frase es una petición cortés?", "Could you please send me the schedule?", ["I want the schedule right now", "Send me the schedule today"], "Could you please es cortés."),
    ],
    [
        mc("Debes escribir a un profesor para pedir una prórroga. ¿Qué asunto es mejor?", "Request for a deadline extension", ["Help, I need more time!!!", "Hello, a question for you"], "Resume el tema con claridad."),
        mc("Completa con una frase formal: 'I ___ writing to complain about the broken heater.'", "am", ["are", "is"], "I am writing."),
        mc("¿Cuál reescritura convierte 'I don't have the book' en formal?", "I do not have the book", ["I don't have book", "I not have the book"], "Sin contracción y con ortografía completa."),
    ],
    [
        mc("Un compañero escribe a la directora: 'This is terrible. Fix the heater now.' ¿Qué cambio mantiene su queja y la hace formal?", "I am concerned that the heater is broken; I would appreciate it if it could be repaired", ["Fix the heater now or else I will complain to the whole school about it", "The heater is bad, sorry about that, but please fix it as soon as you can"], "Expresa la crítica con respeto."),
        mc("Escribes a un amigo y a tu profesora con el mismo mensaje. ¿Qué es lo mejor?", "adaptar el registro a cada audiencia", ["usar el mismo registro para ambos", "usar solo emojis"], "La audiencia cambia el registro."),
    ],
    [
        mr(MAIL, "Un compañero dice que el correo es demasiado largo para su propósito. ¿Cuál es la mejor respuesta?", "es breve y cada parte cumple una función", ["tiene razón: debe ser más largo", "no hay propósito"], "Contiene asunto, propósito, razón, petición y cierre."),
        mc("¿Qué frase aporta una postura personal con razón en un correo formal?", "I believe that older students can help younger ones because they have experience", ["Older students are great and everybody in the school really likes them", "That's what I think about older students and younger students at school"], "Incluye una postura y su razón."),
    ],
    [mc("Quieres cerrar un correo formal con una fórmula neutra y cortés. ¿Qué cierre usas?", "Best regards,", ["See ya!", "XOXO"], "Es cortés y neutro.")],
    sc(2, 1, [
        ("¿Qué partes tiene un correo formal?", "Asunto, saludo, propósito, desarrollo, petición y cierre", "Cada parte cumple una función."),
        ("¿Dónde va el propósito en un correo formal?", "En la primera frase", "Así el lector entiende rápido."),
        ("¿Cómo se pide con cortesía?", "Could you please...?", "Es una petición formal."),
    ]),
    task("Escribe en inglés un correo formal de cuatro a seis oraciones a una profesora para pedir una reunión sobre tu trabajo final. Incluye asunto, saludo, I am writing to..., una razón y un cierre. (meeting = reunión, final project = trabajo final)", "Subject: Request for a meeting about the final project. Dear Ms. Pérez, I am writing to ask for a short meeting. I would like to check my topic because I want to make it clearer. Could you please tell me when you are available? Thank you for your time. Sincerely, Luis", ["asunto y saludo formales", "propósito en la primera frase", "petición cortés y cierre"], ["correo en inglés"], ["usar Hey o contracciones", "no incluir el cierre"], "Marca cada parte y reemplaza lo informal."),
    "Reescribe un mensaje informal tuyo en forma de correo formal.",
    "Escribe tres asuntos de correo formal distintos.",
)

# ------------------------------------------------------------------ clase 2: estructura de un ensayo breve
ESS = "«Title: Should schools start later? Introduction: Many teenagers feel tired in class. This essay argues that schools should start later. Body 1: Sleep research suggests that teenagers need more sleep than children. Body 2: A later start could improve attention in the first lessons. Counterargument: Some families need early schedules for work. However, buses and after-school programs can be adjusted. Conclusion: Later starts would help students, so schools should consider them.» (schedules = horarios, buses = buses, after-school programs = actividades después de clases, adjusted = ajustados, attention = atención; texto de ejemplo)"

lesson(
    OA2, 2, MAT_R,
    "Aprenderé a organizar un ensayo breve de postura: introducción con tesis, párrafos de desarrollo con oración temática y evidencia, contraargumento con refutación y conclusión. Sirve para producir textos claros que expresen una postura crítica respetando otras posturas.",
    ["Sé escribir un párrafo con postura y razones.", "Sé usar conectores de contraste."],
    [
        "Un ensayo argumentativo breve (short argumentative essay) tiene cuatro partes. 1) Introducción: presenta el tema y la tesis (thesis), que es la postura en una oración: This essay argues that schools should start later. 2) Desarrollo (body): uno o dos párrafos, cada uno con una oración temática (topic sentence), una razón y una evidencia. 3) Contraargumento (counterargument) y refutación (rebuttal): presentas una objeción y respondes con una razón. 4) Conclusión: repite la tesis con otras palabras y propone una acción.",
        "La tesis debe ser clara, defendible y específica. Los párrafos deben tratar una sola idea. La evidencia puede ser un dato, un ejemplo o una explicación; si usas un estudio, di si es de ejemplo. Incluir un contraargumento muestra respeto hacia otras posturas y fortalece tu texto: Some families need early schedules. However, ... Evita ataques personales y palabras absolutas.",
        "Para que sea claro, usa conectores entre párrafos (First, In addition, However, In conclusion), mantén oraciones de largo moderado y evita repeticiones. Una conclusión no debe traer ideas nuevas. Un buen ensayo breve puede tener 150 a 200 palabras.",
    ],
    [("thesis", "tesis: postura en una oración"), ("body paragraph", "párrafo de desarrollo"), ("topic sentence", "oración temática"), ("counterargument", "contraargumento"), ("rebuttal", "refutación"), ("conclusion", "conclusión")],
    [
        ("Reconocer la tesis", ESS + " ¿Cuál es la tesis?", ["La tesis aparece en la introducción.", "This essay argues que schools should start later.", "Es la postura en una oración."], "This essay argues that schools should start later."),
        ("Reconocer la refutación", ESS + " ¿Qué respuesta da el texto al contraargumento de las familias?", ["Busco However después del contraargumento.", "Dice buses and after-school programs can be adjusted.", "Esa es la refutación."], "Que los buses y las actividades después de clases se pueden ajustar"),
    ],
    [
        ("Poner ideas nuevas en la conclusión.", "La conclusión debe cerrar, no abrir.", "Repite la tesis con otras palabras."),
        ("Ignorar toda postura contraria.", "El texto parece poco justo o incompleto.", "Incluye un contraargumento y respóndele."),
    ],
    [
        mr(ESS, "¿Qué parte del ensayo dice Some families need early schedules?", "el contraargumento", ["la tesis", "la conclusión"], "Presenta una objeción a la tesis."),
        mr(ESS, "¿Qué idea desarrolla Body 1?", "los adolescentes necesitan dormir más que los niños", ["los buses escolares son caros para las familias", "los horarios de las familias no pueden cambiar"], "Habla de las necesidades de sueño."),
        mr(ESS, "¿Qué hace la conclusión?", "retoma la tesis y propone considerar el cambio", ["introduce un tema nuevo sobre los buses", "presenta un contraargumento sobre las familias"], "Dice schools should consider them."),
    ],
    [
        mr(ESS, "¿Qué idea desarrolla Body 2?", "un inicio más tarde podría mejorar la atención", ["los profesores prefieren empezar temprano", "los buses son de colores"], "A later start could improve attention."),
        mc("Ordena con letras las partes de un ensayo: a) conclusión b) tesis c) contraargumento y refutación d) desarrollo. Escribe el orden más usual.", "b, d, c, a", ["a, b, c, d", "d, b, a, c"], "Tesis, desarrollo, contraargumento y conclusión."),
        mc("¿Qué es una oración temática?", "la oración que presenta la idea del párrafo", ["la última oración del ensayo completo", "una cita de un libro o un estudio"], "Anuncia la idea de un párrafo."),
    ],
    [
        mc("Tesis posible para un ensayo sobre bicicletas: ¿cuál es mejor?", "This essay argues that cities should build more bike lanes to improve safety", ["Some people use bicycles to go to work in the morning in many cities", "Bikes are good for the city and also good for the health of people"], "Es específica y defendible."),
        mc("Contraargumento posible para 'Phones should be allowed in class'. ¿Cuál es adecuado?", "Some teachers worry that phones may distract students", ["Phones are expensive for many families", "Students like to play games on phones"], "Es una objeción relevante."),
        mc("Refutación para esa objeción: ¿cuál es adecuada?", "However, clear rules can limit phones to learning tasks", ["Teachers are wrong about phones in class", "Phones are small and easy to hide"], "Responde a la objeción con una razón."),
    ],
    [
        mc("Un compañero escribe una introducción que cuenta cinco anécdotas y no dice su postura. ¿Qué falta?", "una tesis clara", ["más anécdotas", "una conclusión"], "La introducción debe incluir la tesis."),
        mc("Un párrafo de desarrollo mezcla tres ideas distintas. ¿Qué es lo mejor?", "dividirlo en párrafos con una idea cada uno", ["añadir más conectores a cada oración", "borrar la oración temática de cada uno"], "Un párrafo debe tratar una sola idea."),
    ],
    [
        mc("Debes decidir si incluir un contraargumento en un ensayo sobre uniformes. ¿Qué es lo mejor?", "sí, uno razonable seguido de una refutación", ["no, mostraría debilidad ante los lectores", "sí, pero sin responderlo después"], "Muestra respeto y fortalece la postura."),
        mc("¿Qué conclusión es mejor para el ensayo de bicicletas?", "In conclusion, building more bike lanes would make cities safer, so councils should plan them", ["Another idea is that buses are very slow and councils should buy more of them", "Bikes have two wheels, so cities should paint more lines on every street"], "Retoma la tesis y propone una acción."),
    ],
    [mc("Cuentas las palabras de tu ensayo y tienes 120. El objetivo es entre 150 y 200. ¿Qué haces?", "agregar un ejemplo o una explicación en el desarrollo", ["añadir una conclusión nueva con otro tema", "repetir la tesis tres veces"], "El desarrollo es el lugar para ampliar con evidencia.")],
    sc(2, 2, [
        ("¿Qué es la tesis de un ensayo?", "La postura del autor en una oración", "Se presenta en la introducción."),
        ("¿Qué es una refutación?", "La respuesta a un contraargumento", "Muestra por qué la objeción no cambia la postura."),
        ("¿Qué no debe haber en la conclusión?", "Ideas nuevas", "La conclusión cierra el texto."),
    ]),
    task("Escribe en inglés un esquema de ensayo con estos cinco elementos para uno de estos temas: A) libraries should stay open at night, o B) schools should teach financial skills. Thesis, Body 1, Body 2, Counterargument + rebuttal y Conclusion, cada uno en una oración (la refutación puede ir en una segunda oración). (financial skills = habilidades financieras)", "Thesis: This essay argues that libraries should stay open at night. Body 1: Students need a quiet place to study. Body 2: Night hours help people who work in the day. Counterargument: Opening at night costs money. However, one extra evening shift is a small cost. Conclusion: Longer hours would help the community, so councils should consider them.", ["tiene los cinco elementos", "cada uno cumple su función", "la tesis es clara"], ["esquema de cinco oraciones"], ["omitir el contraargumento", "tesis vaga"], "Marca cada elemento y reescribe el que no cumple su función."),
    "Desarrolla en una oración el Body 1 de tu esquema con una razón y un ejemplo.",
    "Escribe tres tesis distintas sobre temas de tu colegio.",
)

# ------------------------------------------------------------------ clase 3: concesión y contraste
lesson(
    OA2, 3, MAT_R,
    "Aprenderé a usar although, even though, despite, in spite of, whereas, nevertheless y on the other hand para reconocer otras posturas y contrastar ideas en un texto formal. Sirve para expresar una postura crítica que respeta otras posturas.",
    ["Sé usar however y but.", "Sé estructurar un ensayo breve."],
    [
        "La concesión (concession) reconoce un punto de la otra postura antes de mantener la propia. Se hace con although y even though + sujeto y verbo: Although some families need early schedules, buses can be adjusted. Con despite o in spite of va un sustantivo o un verbo con -ing: Despite the cost, libraries are worth it; In spite of being tired, she finished. No se usa sujeto y verbo después de despite: Despite of the rain es incorrecto, y Despite the rain, we played es correcto.",
        "Para contrastar dos ideas separadas se usan whereas y while (en medio de la oración): Cities have many buses, whereas small towns often have none. Nevertheless, however y on the other hand van al inicio de una oración con coma: Nevertheless, many students prefer to walk. On the one hand... on the other hand... presenta dos lados de un tema. But es más informal y va en el medio de la oración.",
        "No uses although y but juntos: Although it is expensive, but it is useful es incorrecto. Elige uno: Although it is expensive, it is useful, o It is expensive, but it is useful. Estos recursos hacen tu texto más respetuoso porque muestran que consideras la otra postura antes de responder.",
    ],
    [("although / even though", "aunque + oración"), ("despite / in spite of", "a pesar de + sustantivo o -ing"), ("whereas / while", "mientras que"), ("nevertheless", "sin embargo, aun así"), ("on the other hand", "por otro lado"), ("concession", "concesión: reconocer otro punto")],
    [
        ("Elegir although o despite", "Completa: '___ the heavy rain, the match continued.' A) Despite B) Although", ["Después del espacio viene un sustantivo, the heavy rain.", "Despite va con sustantivos.", "Although necesita sujeto y verbo."], "A) Despite"),
        ("Evitar although y but juntos", "¿Cuál oración es correcta? A) Although it is cheap, it is good. B) Although it is cheap, but it is good.", ["Although y but no se usan juntos.", "La A usa solo although.", "La B repite el contraste."], "A) Although it is cheap, it is good."),
    ],
    [
        ("Escribir Despite of the rain.", "Despite no lleva of; in spite of sí lleva of.", "Usa despite o in spite of."),
        ("Usar although con un sustantivo: Although the rain.", "Although necesita sujeto y verbo.", "Usa despite the rain o although it rained."),
    ],
    [
        mc("Completa: '___ some students dislike uniforms, many accept them.'", "Although", ["Despite", "Nevertheless"], "Some students dislike es una oración con sujeto y verbo."),
        mc("Completa: '___ being tired, she finished the project.'", "In spite of", ["Whereas", "Nevertheless"], "In spite of va con -ing o sustantivo."),
        mc("Completa: 'Big cities have many buses, ___ small towns often have none.'", "whereas", ["despite", "unless"], "Whereas une dos hechos contrastantes."),
    ],
    [
        mc("¿Qué oración es correcta?", "Even though it was late, they kept talking", ["Even though was late, they kept talking", "Even though it was late, but they kept talking"], "Even though necesita sujeto y verbo y no se combina con but."),
        mc("¿Qué oración es correcta?", "Despite the noise, I could study", ["Despite of the noise, I could study", "Despite it was noisy, I could study"], "Despite va con sustantivo y sin of."),
        mc("¿Qué conector va al inicio de la oración con coma? '___, many students prefer to walk.'", "Nevertheless", ["Although", "Whereas"], "Nevertheless se usa con coma entre oraciones."),
    ],
    [
        mc("Une las ideas con una concesión: 'Some families need early schedules. Later starts help students.' Elige.", "Although some families need early schedules, later starts help students", ["Despite some families need early schedules, later starts help students", "Some families need early schedules but although later starts help students"], "Although + sujeto y verbo funciona; las otras tienen errores."),
        mc("Reescribe con despite: 'Although the cost is high, libraries are worth it.'", "Despite the high cost, libraries are worth it", ["Despite the cost is high, libraries are worth it", "Despite of the high cost, libraries are worth it"], "Despite lleva un sustantivo."),
        mc("¿Qué opción presenta dos lados de un tema?", "On the one hand, cars are fast; on the other hand, they pollute", ["Cars are fast; although, on the other hand, pollute", "On the one hand cars; despite on the other hand fast"], "Sigue la estructura de dos lados."),
    ],
    [
        mc("Un alumno dice que although y but pueden ir juntos para dar más fuerza. ¿Qué respuesta es correcta?", "no: se elige uno u otro en la misma oración", ["sí: juntos dan más fuerza al contraste", "sí: siempre se usan juntos en textos formales"], "Usarlos juntos duplica el contraste y es incorrecto."),
        mc("¿Cuál frase reconoce la otra postura con más respeto?", "Although I understand the concern about cost, I believe that libraries are valuable", ["Everybody who disagrees with libraries is simply wrong about what they need", "Cost is not a problem for libraries, period, and there is no more to discuss"], "Reconoce el punto del otro y mantiene la postura."),
    ],
    [
        mc("Debes escribir una concesión para el tema 'uniformes'. ¿Cuál es adecuada?", "Although uniforms can limit self-expression, they may reduce pressure about clothes", ["Uniforms are great, and nobody disagrees with them in this school at all", "Despite uniforms, but they reduce pressure about the clothes in the school"], "Reconoce una objeción y da una razón."),
        mc("Corrige: 'In spite the rain, we played.'", "In spite of the rain, we played", ["In spite of the rain we plays", "In spite of that rain, we play"], "In spite of necesita of."),
    ],
    [mc("Completa: 'Despite ___ tired, he went to the gym.'", "being", ["he was", "is"], "Despite se une con -ing.")],
    sc(2, 3, [
        ("¿Qué sigue a although?", "Un sujeto y un verbo", "Although introduce una oración."),
        ("¿Qué sigue a despite?", "Un sustantivo o un verbo con -ing", "No lleva sujeto ni verbo conjugado."),
        ("¿Para qué sirve una concesión?", "Para reconocer otro punto antes de mantener la postura", "Muestra respeto por otras posturas."),
    ]),
    task("Escribe en inglés cuatro oraciones sobre el tema 'los celulares en clases': una con although, una con despite, una con whereas y una con nevertheless. Mantén una postura clara. (celular = phone)", "Although phones can distract students, they can help with research. Despite the risk of distraction, a clear rule can solve the problem. Some students use phones to learn, whereas others only play. Nevertheless, I believe that rules are better than a total ban.", ["usa los cuatro conectores correctamente", "mantiene una postura", "reconoce otra postura"], ["cuatro oraciones"], ["usar despite con sujeto y verbo", "combinar although y but"], "Corrige cada conector con la regla de la clase."),
    "Convierte tres oraciones con but en oraciones con although.",
    "Escribe dos oraciones con on the one hand y on the other hand sobre el transporte público.",
)

# ------------------------------------------------------------------ clase 4: comunicar una postura con contraargumento
OPED = "«Some people argue that tablets in class make students lazy. I disagree. In my school, students use tablets to read, practice vocabulary and write in groups. Admittedly, a tablet can distract a student, but a clear rule solves that. If we want students to learn how to use technology well, we should teach them, not ban it. For these reasons, schools should keep tablets, with limits.» (tablets = tabletas, lazy = flojos, admittedly = es cierto que, distract = distraer, ban = prohibir, limits = límites; texto de ejemplo)"

lesson(
    OA2, 4, MAT_L,
    "Aprenderé a comunicar una postura crítica, por escrito o en una intervención oral, con contraargumento, refutación y llamado a la acción respetuosos. Sirve para producir textos y discursos claros que consideren otras posturas.",
    ["Sé estructurar un ensayo breve.", "Sé usar although y despite."],
    [
        "Un texto de opinión (opinion piece) y una intervención oral usan una estructura parecida: abrir con la postura de otros (Some people argue that...), expresar la propia (I disagree. / I believe that...), dar razones y ejemplos, reconocer una objeción válida (Admittedly, ..., It is true that...), refutarla (but a clear rule solves that), y cerrar con un llamado a la acción (schools should keep tablets, with limits). Esto muestra respeto sin perder la postura.",
        "Los marcadores guían al oyente: For these reasons..., In my experience..., Let me explain why..., To sum up... En voz alta usa pausas, énfasis en palabras clave y frases cortas. Evita palabras absolutas y ataques: critica la idea, no a la persona. Si usas un ejemplo propio, dilo; si usas un dato, indica de dónde viene o rotúlalo como ejemplo.",
        "Un llamado a la acción (call to action) debe ser realista y respetuoso: schools should keep tablets, with limits; Let us consider a trial period. No es una orden: es una propuesta basada en lo dicho. Antes de entregar o presentar tu texto, comprueba que tiene postura, razones, concesión, refutación y cierre.",
    ],
    [("opinion piece", "texto de opinión"), ("admittedly / it is true that", "es cierto que: concesión"), ("to sum up", "para resumir"), ("call to action", "llamado a la acción"), ("I disagree", "no estoy de acuerdo"), ("limits", "límites")],
    [
        ("Reconocer la concesión", OPED + " ¿Qué frase reconoce una objeción válida?", ["Busco una palabra como Admittedly.", "Dice Admittedly, a tablet can distract a student.", "Esa es la concesión."], "Admittedly, a tablet can distract a student."),
        ("Reconocer el llamado a la acción", OPED + " ¿Qué propone el autor al final?", ["Busco la última oración.", "Dice schools should keep tablets, with limits.", "Esa es la propuesta."], "Mantener las tabletas en el colegio, con límites"),
    ],
    [
        ("Presentar la postura contraria de forma burlesca.", "Se pierde el respeto y no se argumenta.", "Describe la otra postura con justicia."),
        ("Cerrar con una orden.", "Resulta poco respetuoso.", "Haz una propuesta basada en tus razones."),
    ],
    [
        mr(OPED, "¿Cuál es la postura del autor?", "las tabletas deben mantenerse en el colegio con límites", ["las tabletas deben prohibirse en todas las clases", "las tabletas son siempre una herramienta perfecta"], "Dice I disagree y propone keep tablets, with limits."),
        mr(OPED, "¿Cuál es la postura que presenta Some people?", "que las tabletas hacen flojos a los estudiantes", ["que las tabletas son baratas para los colegios", "que los estudiantes no deben leer en clases"], "Dice tablets in class make students lazy."),
        mr(OPED, "¿Qué ejemplo da el autor sobre el uso de tabletas?", "leer, practicar vocabulario y escribir en grupos", ["mirar videos de entretención en clases", "jugar videojuegos durante los recreos"], "Dice students use tablets to read, practice vocabulary and write in groups."),
    ],
    [
        mr(OPED, "¿Cómo responde el autor al riesgo de distracción?", "con una regla clara", ["prohibiendo las tabletas", "ignorando el problema"], "Dice a clear rule solves that."),
        mr(OPED, "¿Qué frase introduce la conclusión?", "For these reasons", ["Some people argue", "In my school"], "Es un marcador de cierre."),
        mc("¿Qué marcador usarías para resumir al final de una intervención oral?", "To sum up", ["To begin with", "Let me give an example"], "To sum up resume."),
    ],
    [
        mc("Debes presentar la postura contraria con justicia. ¿Qué frase sirve?", "Some people argue that cities have too many cars", ["People who think that cities have cars are silly", "Nobody believes that cities have too many cars"], "Describe la otra postura sin burlarse."),
        mc("Completa una concesión: '___, a school uniform can limit self-expression, but it reduces pressure.'", "It is true that", ["Despite", "Although of"], "It is true that reconoce el punto."),
        mc("¿Qué llamado a la acción es adecuado?", "Let us try a one-month trial period", ["Do it now or I won't speak to you", "That is all"], "Es una propuesta respetuosa."),
    ],
    [
        mc("Un compañero dice que no debemos reconocer la postura contraria, porque debilita el texto. ¿Qué respuesta es correcta?", "reconocerla con respeto muestra criterio y fortalece el texto", ["solo sirve en la conversación, no en el texto", "tiene razón: la postura contraria lo debilita"], "La concesión muestra que se pensó en otras posturas."),
        mc("Debes hablar 90 segundos. ¿Qué te ayuda a sonar claro?", "frases cortas, pausas y énfasis en palabras clave", ["hablar muy rápido para terminar a tiempo", "leer el texto sin mirar nunca al público"], "La claridad es lo central."),
    ],
    [
        mc("Escribes una opinión sobre el reciclaje. ¿Cuál es la mejor secuencia?", "postura contraria, tu postura, razones, concesión, refutación, llamado a la acción", ["llamado a la acción, razones, postura contraria, saludo, concesión, refutación", "concesión, ejemplo, saludo, postura contraria, tu postura, razones, cierre"], "Es la estructura del texto de opinión."),
        mc("Lees tu texto en voz alta y notas una frase muy larga. ¿Qué haces?", "dividirla en dos frases con un conector", ["dejarla igual", "borrar la mitad de las ideas"], "Las frases breves son más claras para escuchar."),
    ],
    [mc("Quieres usar un dato en tu intervención: «Seven out of ten students said they like group work» (de ejemplo). ¿Qué haces con el dato?", "rotularlo como ejemplo o indicar de dónde viene", ["presentarlo como un hecho de todo el mundo", "esconder su origen para que parezca más fuerte"], "Un dato necesita su fuente o su rótulo.")],
    sc(2, 4, [
        ("¿Qué es un llamado a la acción?", "Una propuesta para actuar basada en las razones", "Cierra el texto de opinión."),
        ("¿Para qué sirve Admittedly,...?", "Para reconocer un punto válido de la otra postura", "Es una concesión."),
        ("¿Cómo se critica con respeto?", "La idea, no a la persona", "Se argumenta sin atacar."),
    ]),
    task("Prepara un texto de opinión de cinco a seis oraciones en inglés sobre uno de estos temas: A) cell phones at school, B) homework on weekends. Incluye la postura contraria con Some people argue that..., tu postura, una razón, una concesión con Admittedly o It is true that, una refutación y un llamado a la acción. Léelo en voz alta a una persona de tu casa.", "Some people argue that homework on weekends is necessary. I disagree. Students need time to rest and see family. Admittedly, some projects take time, but they can be planned during the week. For these reasons, teachers should avoid weekend homework.", ["incluye las seis partes", "tono respetuoso", "oraciones breves"], ["texto de cinco o seis oraciones", "lectura en voz alta"], ["omitir la concesión", "cerrar con una orden"], "Marca las seis partes, completa la que falta y acorta las oraciones largas."),
    "Escribe una concesión y una refutación para tu tema favorito.",
    "Practica dos veces en voz alta tu texto con pausas.",
)

# ------------------------------------------------------------------ clase 5: revisar cohesión y claridad
DRAFT2 = "«In my opinion the school should have a recycling program. The program is good for the environment. The program is cheap. Actually, many students are interested and it would be easy to start. It would make the school better and we should do it.» (recycling program = programa de reciclaje, environment = medio ambiente, cheap = barato, easy to start = fácil de empezar)"

lesson(
    OA2, 5, MAT_R,
    "Aprenderé a revisar un texto para mejorar su cohesión (conectores, referencias), reducir repeticiones, corregir puntuación y falsos amigos, y dar y recibir comentarios respetuosos. Sirve para que mis textos claros expresen una postura crítica que se entienda y respete a otras personas.",
    ["Sé escribir un ensayo breve.", "Sé usar conectores de contraste."],
    [
        "Revisar es mejorar el texto en varias pasadas. 1) Sentido: ¿se entiende la tesis y cada razón apoya la tesis? 2) Cohesión: ¿las ideas se unen con conectores (because, however, in addition, therefore) y referencias claras (it, they, this)? 3) Concisión: ¿hay repeticiones como the program... the program... the program? Usa pronombres y sinónimos. 4) Puntuación y ortografía: coma después de palabras introductorias (However, In addition,), punto al final, mayúscula inicial.",
        "Errores frecuentes: la oración sin conectar (comma splice): The program is good, it is cheap se corrige con and o con un punto y coma; las palabras vagas (thing, good, better) se reemplazan por palabras precisas; los falsos amigos: actually (en realidad, no actualmente), sensible (sensato), eventually (finalmente, no eventualmente), library (biblioteca). Revisa también las colocaciones: do research, make a decision.",
        "Para dar un comentario a un compañero, usa tres pasos: una fortaleza (One strength is...), una sugerencia (You could add... / It would be clearer if...) y una pregunta (What do you think about...?). Recibir comentarios es una oportunidad: no cambia tu postura, pero puede mejorarla. Agradece con Thank you for the feedback.",
    ],
    [("cohesion", "cohesión: ideas bien unidas"), ("repetition", "repetición"), ("comma splice", "dos oraciones unidas solo con coma"), ("feedback", "comentarios sobre un trabajo"), ("One strength is", "una fortaleza es"), ("You could add", "podrías agregar")],
    [
        ("Eliminar repeticiones", DRAFT2 + " ¿Qué problema de cohesión tienen las tres primeras oraciones?", ["Veo la palabra program repetida.", "The program aparece al inicio de dos oraciones.", "Se resuelve con it o con un conector."], "Repiten the program; conviene usar it y conectores"),
        ("Falso amigo", DRAFT2 + " En Actually, many students are interested, el autor quiso decir actualmente. ¿Qué palabra corresponde?", ["Actually significa en realidad.", "Actualmente se dice currently.", "La palabra correcta es Currently."], "Currently"),
    ],
    [
        ("Unir dos oraciones con una coma sola.", "Es un comma splice: falta un conector o un punto.", "Usa and, but o un punto."),
        ("Reemplazar mal los comentarios con críticas personales.", "Un comentario sobre la persona no mejora el texto.", "Comenta el texto con fortaleza, sugerencia y pregunta."),
    ],
    [
        mc("¿Cuál reemplaza mejor 'The program is good. The program is cheap.'?", "The program is good, and it is cheap", ["The program is good, the program is cheap", "Good program, cheap program"], "Une las ideas y evita repetir."),
        mc("¿Cuál oración corrige el comma splice 'The park is clean, it is safe'?", "The park is clean, and it is safe", ["The park is clean it is safe", "The park is clean, because it is safe"], "And une dos ideas correctamente."),
        mc("¿Qué palabra se usa para 'actualmente'?", "currently", ["actually", "eventually"], "Actually significa en realidad."),
    ],
    [
        mc("¿Qué palabra precisa reemplaza a good en 'a good idea for the environment'?", "beneficial", ["nice", "thing"], "Beneficial es más precisa."),
        mc("¿Qué conector sirve entre 'The program is cheap' y 'It is easy to start'?", "In addition,", ["Despite,", "Unless,"], "Suma una razón."),
        mc("¿Qué comentario sigue el formato fortaleza + sugerencia?", "One strength is your clear thesis; you could add an example in the second paragraph", ["This is bad and boring, so you should rewrite all of it from the beginning", "Your text is wrong and I do not like the way you write about this topic"], "Contiene una fortaleza y una sugerencia."),
    ],
    [
        mc("Texto: " + DRAFT2 + " ¿Cuál es la mejor revisión de 'It would make the school better and we should do it'?", "It would improve the school, so we should start it this year", ["Better school and we do it", "It would make the school better and we should do it, do it"], "Es más precisa y conectada."),
        mc("Texto: " + DRAFT2 + " Agrega una frase de concesión respetuosa. ¿Cuál sirve?", "Admittedly, the program needs volunteers, but students can share the work", ["Anyone against the program is simply wrong and does not understand students", "The program is perfect and has no problems at all for anybody in the school"], "Reconoce una objeción y responde."),
        mc("Un compañero te dice 'Your text is bad'. ¿Cómo le pides un comentario útil?", "Could you tell me one strength and one thing I could improve?", ["You are wrong, so tell me everything you dislike", "I do not care what you think about my text"], "Pide un comentario concreto con cortesía."),
    ],
    [
        mc("Un compañero dice que repetir the program tres veces da énfasis. ¿Qué le respondes?", "puede hacer que el texto suene repetitivo; un pronombre o sinónimo es mejor", ["tiene razón: repetir una palabra siempre da más énfasis al texto", "nunca se debe repetir ninguna palabra en un texto, ni siquiera un pronombre"], "La repetición excesiva resta claridad."),
        mc("Una amiga escribe 'I eventually will study abroad' pensando en 'eventualmente'. ¿Qué significa eventually?", "finalmente, con el tiempo", ["a veces, de vez en cuando", "quizás, tal vez más adelante"], "Eventually es falso amigo de eventualmente."),
    ],
    [
        mc("Texto: " + DRAFT2 + " Reescribe la frase con 'In my opinion the school should have' para que la tesis sea más específica.", "In my opinion, the school should start a recycling program for paper and plastic", ["The school has a program for some students who like to recycle at home", "In my opinion the school should have something good for all the students"], "Es específica y defendible."),
        mc("Pides un comentario sobre tu texto y recibes: 'It would be clearer if you gave an example.' ¿Cuál es una buena respuesta?", "Thank you for the feedback; I will add an example from my school", ["That's wrong; I will not change my text because I like it as it is", "I won't change anything because it is fine and I do not need advice"], "Agradece y toma el comentario."),
    ],
    [mc("Cuando revisas, ¿qué conviene hacer primero?", "revisar el sentido y la tesis", ["revisar solo las comas", "cambiar todas las palabras"], "El sentido va antes que la forma.")],
    sc(2, 5, [
        ("¿Qué es la cohesión?", "La unión clara entre ideas mediante conectores y referencias", "Hace el texto fluido."),
        ("¿Qué es un comma splice?", "Unir dos oraciones completas solo con una coma", "Se corrige con and, but o un punto."),
        ("¿Qué contiene un comentario útil?", "Una fortaleza, una sugerencia y una pregunta", "Respeta y ayuda a mejorar."),
    ]),
    task("Revisa este borrador y reescríbelo en inglés en cinco oraciones claras: «I think that the school need a garden. The garden is nice. The garden can teach students. Actually the school has no space for it, but many students want it, it is easy.» (need = necesita, nice = agradable, garden = huerto). Debes corregir la concordancia, eliminar repeticiones, arreglar el comma splice y reemplazar el falso amigo (en Actually el autor quiere decir actualmente).", "I think that the school needs a garden. It is useful because it can teach students about plants. In addition, many students want it. Currently, there is no space, but a small area would be easy to use. For these reasons, the school should start one.", ["corrige la concordancia", "evita repeticiones", "corrige el comma splice y el falso amigo"], ["texto reescrito"], ["no corregir el verbo", "mantener actually con sentido de actualmente"], "Revisa en este orden: sentido, cohesión, concisión y forma."),
    "Pide a alguien de tu casa que lea tu texto y te diga una fortaleza y una sugerencia.",
    "Escribe tres comentarios para el texto de un compañero con el formato fortaleza, sugerencia y pregunta.",
)
