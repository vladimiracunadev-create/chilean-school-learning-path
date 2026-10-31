"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 07 (territorio, visión de mundo e identidades), OA 08 (historias de pueblos en relación) y
OA 09 (diversidad lingüística y diálogo intercultural).

Criterio de autoría: las comunidades, los lugares, las personas y los relatos de práctica son INVENTADOS
(no pertenecen a ningún pueblo real) y se rotulan así. No se afirma nada de lengua, ritos, fechas de
celebraciones, arte, cosmovisión ni roles de un pueblo concreto, salvo datos generales de amplio consenso
(nombres de pueblos y lenguas, zonas generales y el saludo «mari mari»). Lo tradicional lo enseñan el
educador o la educadora tradicional y la comunidad; ningún ejercicio exige saber una lengua indígena.
Los otros módulos lc5_* importan los ayudantes de este archivo.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA7, OA8, OA9 = "LC05 OA 07", "LC05 OA 08", "LC05 OA 09"

CONSULT = " Recuerda: lo tradicional lo enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales a ellos antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement + CONSULT, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback + FEEDBACK_ADD}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


MAT = "Lápiz y hojas. Los textos y las fichas están escritos en este cuaderno. Las comunidades, los lugares y las personas son inventados."

FLV = ("Ficha situada (inventada). Comunidad: Ladera Verde (no es un pueblo real). Territorio: cerros con terrazas, una quebrada y un corral comunitario. "
       "Fuente y responsable: doña Elena, vecina de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: doña Elena autorizó usar esta ficha en la escuela. "
       "Límite: no se cuenta dónde está el lugar de respeto de la quebrada.")
FIN = ("Ficha situada (inventada). Comunidad: Isla Niebla (no es un pueblo real). Territorio: una isla con bosque, una caleta y un sendero. "
       "Fuente y responsable: don Camilo, pescador de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: don Camilo autorizó usar esta ficha en la escuela. "
       "Límite: no se cuentan las historias que la comunidad reserva.")
FPL = ("Ficha situada (inventada). Comunidad: Pampa Larga (no es un pueblo real). Territorio: una llanura seca con un pozo comunitario y caminos. "
       "Fuente y responsable: doña Marta, vecina de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: doña Marta autorizó usar esta ficha en la escuela. "
       "Límite: no se muestran las reuniones reservadas de la comunidad.")
FRH = ("Ficha situada (inventada). Comunidad: Río Hondo (no es un pueblo real). Territorio: un río, un bosque y un lago. "
       "Fuente y responsable: don Aurelio, vecino de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: don Aurelio autorizó usar esta ficha en la escuela. "
       "Límite: no se cuentan los lugares que la comunidad cuida en silencio.")

# ============================================================ OA 07 · Territorio, visión de mundo e identidades
L(
    OA7, 1, materials=MAT,
    use="Aprenderé a situar un territorio: decir de qué comunidad es, quién lo cuenta y hasta dónde puedo contar yo. Sirve para reflexionar sobre el territorio sin hablar por otros.",
    prior=["Sé que una fuente es la persona o el texto que entrega un dato.", "Sé que cada comunidad cuenta su territorio a su manera."],
    explain=[
        "El territorio no es solo un pedazo de tierra que se mide en un mapa. Es el lugar donde una comunidad vive, trabaja y recuerda, junto con las relaciones entre las personas, con los seres vivos y con la historia que ocurrió allí. Por eso se dice que el territorio y la comunidad se sostienen mutuamente.",
        "La visión de mundo es la manera en que un pueblo entiende el mundo, la naturaleza y la vida. La identidad es lo que lleva a una persona o a una comunidad a reconocerse parte de un pueblo, de su historia y de un lugar. El territorio influye en ambas, pero cada pueblo lo vive de forma distinta.",
        "Antes de reflexionar hay que situar. Una ficha situada dice la comunidad, el territorio, la fuente, el permiso y el límite. Con esos datos sabemos de quién es el relato y qué no se puede contar. Lo que dice una ficha vale para esa comunidad y no para todos los pueblos.",
    ],
    vocab=[("territorio", "lugar donde una comunidad vive, trabaja y recuerda, con sus relaciones"), ("visión de mundo", "manera en que un pueblo entiende el mundo y la vida"), ("identidad", "sentirse parte de un pueblo, de su historia y de un lugar"), ("fuente", "persona o texto que entrega el dato"), ("permiso", "autorización de la fuente para compartir lo que contó")],
    worked=[
        W("Leer una ficha situada", FLV + " ¿De quién es el relato y qué no se cuenta?", ["La comunidad es Ladera Verde y la fuente es doña Elena.", "Ella dio permiso para usar la ficha en la escuela.", "El límite dice que no se cuenta dónde está el lugar de respeto."], "El relato es de doña Elena, de Ladera Verde; no se cuenta la ubicación del lugar de respeto de la quebrada."),
        W("Territorio más allá del mapa", "Doña Elena dice: «Las terrazas las hicieron mis abuelos y las seguimos cuidando». ¿Qué muestra sobre el territorio?", ["Las terrazas son un lugar físico.", "Cuidarlas une a varias generaciones.", "Entonces el territorio guarda memoria y relaciones."], "El territorio no es solo el lugar: también guarda la memoria y el trabajo de la familia."),
    ],
    mistakes=[
        M("Pensar que el territorio es solo el dibujo de un mapa.", "Deja fuera lo que la comunidad hace y recuerda allí.", "Agrega las relaciones, el trabajo y la memoria."),
        M("Decir «todos los pueblos viven el territorio igual que Ladera Verde».", "La ficha habla de una sola comunidad.", "Escribe siempre el nombre de la comunidad de la ficha."),
    ],
    R=[
        ex("Según la ficha de Ladera Verde, ¿quién es la fuente?", "Doña Elena", "La ficha la nombra como fuente y responsable."),
        ex("¿Qué territorio tiene Ladera Verde? A) cerros con terrazas y una quebrada B) una isla con bosque y caleta", "A", "La isla con caleta es de Isla Niebla."),
        ex("La ficha de Ladera Verde dice que no se cuenta dónde está el lugar de respeto. ¿Escribes su ubicación en tu trabajo? Responde Sí o No.", "No", "El límite de la ficha lo prohíbe."),
    ],
    C=[
        ex("Verdadero o falso: el territorio es solamente la tierra que se puede medir en un mapa.", "Falso", "También incluye relaciones, trabajo y memoria."),
        ex("En Lengua y Cultura, ¿qué es la visión de mundo? A) la manera en que un pueblo entiende el mundo y la vida B) un mapa del país", "A", "Es su forma de entender la naturaleza y la vida."),
        ex("Verdadero o falso: la identidad de una persona se comprueba con una prueba de lengua indígena.", "Falso", "La identidad es sentirse parte de un pueblo y su historia; no se mide con una prueba."),
    ],
    A=[
        ex("Una ficha de Isla Niebla dice: «Fuente: don Camilo. Permiso: no consta». ¿Puedes usarla en tu trabajo? Responde Sí o No.", "No", "Sin permiso no se sabe si se puede compartir."),
        ex("Doña Elena dice: «Las terrazas las hicieron mis abuelos y las seguimos cuidando». ¿Qué idea muestra? A) el territorio guarda la memoria de la familia B) el territorio es un lugar sin historia", "A", "Las terrazas unen a quienes las hicieron con quienes las cuidan."),
        ex("Clasifica en LUGAR o RELACIÓN entre personas: a) la quebrada b) las familias que se turnan para cuidar el corral.", "a lugar, b relación", "La quebrada es un sitio; el turno entre familias es una relación."),
    ],
    Z=[
        ex("Joaquín dice: «Como Ladera Verde tiene cerros, todos los pueblos indígenas ven los cerros como Ladera Verde». ¿Qué error comete?", "Generaliza una ficha a todos los pueblos", "Una comunidad no representa a todas."),
        ex("Un compañero afirma, sin mostrar ninguna ficha: «Para una comunidad del sur el río es sagrado». ¿Por qué no es válido?", "No hay fuente que lo diga", "Sin fuente no se puede afirmar nada sobre una comunidad."),
    ],
    D=[
        ex("Hay dos fichas: Ladera Verde (cerros y terrazas) e Isla Niebla (isla, bosque y caleta). Alguien escribe «mi familia pesca en la caleta». ¿De cuál ficha viene el dato?", "De Isla Niebla", "La caleta aparece solo en la ficha de Isla Niebla."),
        ex("Una ficha trae comunidad y territorio, pero no dice quién es la fuente ni si hay permiso. ¿Qué haces primero? A) usarla igual B) pedir los datos que faltan", "B", "Sin fuente y permiso se detiene la actividad hasta completarlos."),
    ],
    context=[ex("Tu profesora te da un relato breve, pero no dice quién lo contó. Antes de usarlo, ¿qué haces? A) preguntar quién lo contó y si autorizó compartirlo B) usarlo porque parece interesante", "A", "Un relato sin fuente ni permiso no se usa.")],
    selfcheck=[
        ex("Nombra dos datos que debe tener una ficha situada.", "Dos entre: comunidad, fuente, permiso, límite", "Son los datos que permiten situar el relato."),
        ex("Verdadero o falso: el territorio incluye lo que la comunidad recuerda allí.", "Verdadero", "La memoria es parte del territorio."),
        ex("¿Qué haces ante una duda sobre una comunidad real? A) pregunto al educador tradicional o a la comunidad B) lo imagino", "A", "Ellos son la fuente."),
    ],
    task=T("Lee el relato inventado de doña Marta, de Pampa Larga: «Mi comunidad vive en una llanura seca. El pozo es de todas las familias y por turnos lo cuidamos. Mi abuelo me enseñó los caminos para llegar a él.» Haz una ficha con estos campos: comunidad, territorio, fuente, qué dice la fuente y qué límite pondrías. Escribe después una frase que empiece con «Yo pienso que…» sobre la importancia del pozo para la comunidad.",
           "Comunidad: Pampa Larga. Territorio: llanura seca con pozo y caminos. Fuente: doña Marta. Dice: el pozo es de todas las familias y se cuida por turnos. Límite: no sé cómo se organizan los turnos. Yo pienso que el pozo une a las familias porque lo cuidan entre todas.",
           ["completa la ficha con datos del relato", "separa lo que dice la fuente de lo que piensa", "pone un límite"], ["ficha completa", "frase con «Yo pienso que»"], ["agregar datos que el relato no dice", "generalizar a todos los pueblos"],
           "Pedir que muestre en qué línea del relato está cada dato; valorar que separe la fuente de su opinión."),
    reinforce="Subraya en la ficha de Ladera Verde la comunidad, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica con tus palabras por qué un territorio es más que un mapa, usando un dato de la ficha de Ladera Verde.",
)

L(
    OA7, 2, materials=MAT,
    use="Aprenderé a leer un testimonio sobre el territorio con límites declarados: qué dice la fuente, qué interpreto yo y qué no se cuenta. Sirve para reflexionar sin inventar.",
    prior=["Sé situar una comunidad con su ficha.", "Sé que territorio e identidad se relacionan."],
    explain=[
        "Un testimonio es lo que una persona cuenta sobre lo que vive o sabe. Para leerlo con respeto separamos tres cosas. Lo primero es lo que la fuente dice, con sus propias palabras. Lo segundo es lo que yo interpreto, que es mi idea al leer. Lo tercero es lo que no se cuenta o no sé.",
        "Una interpretación puede ser razonable, pero no es un dato de la fuente. Por eso se escribe con una marca como «yo pienso que». Así nadie confunde mi idea con la voz de la comunidad. Además, hay cosas que una comunidad prefiere resguardar, y resguardar también es una forma de cuidar el territorio.",
        "Leer con límites declarados significa decir al final hasta dónde llega lo que afirmo. Si el testimonio no explica algo, escribo «el testimonio no lo dice». Si quiero saber más, pregunto al educador o educadora tradicional. Nunca relleno los vacíos con ideas inventadas.",
    ],
    vocab=[("testimonio", "relato de una persona sobre lo que vive o sabe"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("resguardar", "cuidar algo y no mostrarlo a todos"), ("límite", "lo que no se cuenta o no se sabe"), ("atribuir", "decir de quién viene un dato")],
    worked=[
        W("Separar tres cosas", "Testimonio inventado de doña Elena: «La quebrada nos da agua para las terrazas. Hay un lugar de la quebrada que solo cuidamos nosotros». Separa lo que dice, lo que interpreto y lo que no se cuenta.", ["Dice: la quebrada da agua para las terrazas.", "Interpreto: yo pienso que la quebrada es muy importante para el trabajo de la comunidad.", "No se cuenta: cuál es el lugar que cuidan solo ellos."], "Dice: la quebrada da agua. Interpreto: es importante para el trabajo. No se cuenta: el lugar que cuidan."),
        W("Marcar una interpretación", "Un niño escribe: «Doña Elena cuenta que la quebrada es lo más importante de Ladera Verde». ¿Está bien?", ["Reviso el testimonio: dice que da agua, no que sea lo más importante.", "«Lo más importante» es idea del niño.", "Debería escribir «yo pienso que»."], "No: esa frase mezcla la idea del niño con la fuente."),
    ],
    mistakes=[
        M("Escribir mi interpretación como si la hubiera dicho la fuente.", "Se atribuye a la comunidad algo que no dijo.", "Marca mis ideas con «yo pienso que»."),
        M("Rellenar con ideas lo que la comunidad decidió no contar.", "Lo resguardado se respeta; inventarlo puede ser falso e irrespetuoso.", "Escribe «el testimonio no lo dice»."),
    ],
    R=[
        ex("En el testimonio de doña Elena, ¿qué da la quebrada: agua para las terrazas o pescado?", "Agua para las terrazas", "El testimonio lo dice así."),
        ex("¿Una interpretación es una idea mía o un dato de la fuente?", "Una idea mía", "Interpretar es dar mi propia idea."),
        ex("Si el testimonio no explica algo, ¿qué escribes? A) el testimonio no lo dice B) lo invento", "A", "No se rellenan los vacíos con ideas inventadas."),
    ],
    C=[
        ex("Verdadero o falso: resguardar algo también puede ser una forma de cuidar el territorio.", "Verdadero", "Una comunidad puede cuidar un lugar sin mostrarlo."),
        ex("¿Con qué marca escribo mis ideas? A) «yo pienso que» B) «la comunidad dice que»", "A", "Así no se confunden con la fuente."),
        ex("Verdadero o falso: una interpretación razonable ya es un dato de la fuente.", "Falso", "Sigue siendo idea de quien lee."),
    ],
    A=[
        ex("Testimonio inventado de don Camilo, de Isla Niebla: «El sendero cruza el bosque hasta la caleta». Clasifica en DICE LA FUENTE o INTERPRETO: a) el sendero cruza el bosque b) el sendero debe ser muy antiguo.", "a dice la fuente, b interpreto", "La primera está escrita; la segunda es una suposición."),
        ex("Don Camilo dice: «Hay cuentos de la isla que solo contamos en la comunidad». ¿Qué puedes escribir en tu trabajo sobre esos cuentos? A) que existen y que no se cuentan B) uno inventado por ti", "A", "Solo se afirma que existen; su contenido se respeta."),
        ex("Una niña lee «La quebrada da agua» y escribe «Doña Elena dice que la quebrada es sagrada». ¿Qué dato no está en el testimonio?", "Que la quebrada es sagrada", "El testimonio habla del agua, no de lo sagrado."),
    ],
    Z=[
        ex("Rodrigo escribe, sin marcarlo: «La isla es el lugar más feliz del mundo para la gente de Isla Niebla». ¿Qué debería hacer con esa frase?", "Marcarla como su opinión o quitarla", "No está en el testimonio, así que es opinión."),
        ex("¿Por qué conviene escribir los límites al final de un trabajo? A) para mostrar hasta dónde llega lo afirmado B) para llenar la hoja", "A", "Los límites muestran lo que no se sabe ni se cuenta."),
    ],
    D=[
        ex("Dos frases sobre el mismo testimonio. Uno: «Doña Elena dice que la quebrada da agua». Otro: «Doña Elena dice que la quebrada tiene espíritus». Testimonio: «La quebrada nos da agua para las terrazas». ¿Cuál se queda en la fuente?", "La primera", "La segunda agrega algo que el testimonio no dice."),
        ex("Don Camilo no contó cómo se eligió el nombre de la caleta. ¿Qué escribes en los límites? A) no sé cómo se eligió el nombre de la caleta B) se eligió por un pez", "A", "Declarar lo que no sé evita inventar."),
    ],
    context=[ex("Para un afiche escolar, un compañero quiere dibujar el lugar de la quebrada que la comunidad cuida solo para sí. ¿Qué le dices? A) que esa parte se respeta y no se dibuja B) que lo dibuje sin detalles", "A", "El límite de la ficha dice que no se cuenta su ubicación.")],
    selfcheck=[
        ex("Nombra las tres cosas que separo al leer un testimonio.", "Lo que dice la fuente, lo que interpreto y lo que no se cuenta", "Son los tres pasos de la lectura con límites."),
        ex("Verdadero o falso: puedo completar con mi imaginación lo que la comunidad no contó.", "Falso", "Eso sería inventar."),
        ex("¿Qué escribes cuando el testimonio no explica algo? Escribe una frase corta.", "El testimonio no lo dice", "Es la manera honesta de marcar un vacío."),
    ],
    task=T("Lee este testimonio inventado de don Aurelio, de Río Hondo: «Vivimos junto al río y el bosque. De niño aprendí a reconocer el río por su sonido. Hay lugares del bosque que cuidamos en silencio y no los mostramos.» Haz tres columnas: «La fuente dice», «Yo interpreto» y «No se cuenta». Pon al menos dos datos en cada una. Cierra con una frase de límites.",
           "La fuente dice: viven junto al río y el bosque; aprendió a reconocer el río por su sonido. Yo interpreto: yo pienso que el río es parte de su recuerdo de niño. No se cuenta: qué lugares del bosque se cuidan en silencio. Límite: no sé cómo cuidan esos lugares.",
           ["separa tres columnas", "usa datos del testimonio", "marca sus ideas como interpretación"], ["tabla de tres columnas", "frase de límites"], ["escribir interpretaciones como datos", "inventar los lugares reservados"],
           "Pedir que indique en qué línea del testimonio está cada dato; valorar que deje sin completar lo no contado."),
    reinforce="Subraya con un color lo que dice la fuente y con otro lo que interpretas en el testimonio de don Aurelio.",
    extend="Explica por qué callar un lugar puede ser una manera de cuidarlo, usando el testimonio de don Aurelio.",
)

L(
    OA7, 3, materials=MAT,
    use="Aprenderé a reconocer cómo el territorio se relaciona con la visión de mundo y con la identidad en dos comunidades distintas. Sirve para ver diferencias sin decir que una es mejor.",
    prior=["Sé separar lo que dice una fuente de lo que interpreto.", "Sé qué son visión de mundo e identidad."],
    explain=[
        "Una relación cultural une dos cosas que aparecen en una fuente. Por ejemplo: un lugar y una forma de cuidarlo, o un lugar y un recuerdo. En esta clase buscamos tres tipos de relaciones: entre el territorio y la manera de entender el mundo (visión de mundo), entre el territorio y el sentirse parte de un pueblo (identidad) y entre las personas que comparten un lugar.",
        "Comparamos dos comunidades inventadas: Ladera Verde, de cerros y terrazas, e Isla Niebla, de bosque y caleta. Cada una vive su territorio a su manera. Que sean diferentes no las hace mejores ni peores: son distintas formas de relacionarse con el lugar.",
        "Para comparar bien usamos una tabla con los mismos criterios para las dos comunidades. Escribimos solo lo que dice cada fuente y marcamos con «el testimonio no lo dice» lo que falta. Si las dos comunidades tienen algo parecido, lo anotamos como semejanza, sin decir que todas las comunidades son iguales.",
    ],
    vocab=[("relación cultural", "unión entre dos cosas de una fuente, como un lugar y una forma de cuidarlo"), ("semejanza", "algo parecido entre dos comunidades"), ("diferencia", "algo distinto entre dos comunidades"), ("criterio", "punto que se usa para comparar, igual para todos"), ("jerarquizar", "decir que una cosa es mejor o más importante que otra")],
    worked=[
        W("Encontrar una relación", "Doña Elena: «Las terrazas las hicieron mis abuelos y las cuidamos cada año». Don Camilo: «El sendero lo abrieron los antiguos pescadores y lo limpiamos entre todos». ¿Qué relación hay en cada uno?", ["Doña Elena une las terrazas con el trabajo de sus abuelos.", "Don Camilo une el sendero con los antiguos pescadores.", "En ambos, el lugar se cuida entre generaciones."], "En ambas comunidades el lugar une a personas de distintas generaciones."),
        W("Comparar sin jerarquizar", "¿Es mejor vivir en cerros o en una isla?", ["La pregunta pide ordenar dos territorios.", "Las fuentes solo cuentan cómo cada comunidad vive el suyo.", "No se puede decir cuál es mejor."], "No se jerarquiza: cada comunidad vive su territorio a su manera."),
    ],
    mistakes=[
        M("Decir que el territorio de una comunidad es mejor que el de otra.", "Comparar no es ordenar de mejor a peor.", "Describe semejanzas y diferencias con los mismos criterios."),
        M("Concluir que todas las comunidades indígenas comparten lo mismo porque dos se parecen.", "Dos ejemplos no representan a todos los pueblos.", "Escribe «en estas dos comunidades» y no más."),
    ],
    R=[
        ex("En Ladera Verde, ¿quiénes hicieron las terrazas según doña Elena?", "Sus abuelos", "El testimonio dice que las hicieron sus abuelos."),
        ex("En Isla Niebla, ¿quién abrió el sendero según don Camilo? A) los antiguos pescadores B) un visitante", "A", "El testimonio lo señala."),
        ex("¿Qué territorio tiene Isla Niebla: bosque y caleta o terrazas y quebrada?", "Bosque y caleta", "Las terrazas son de Ladera Verde."),
    ],
    C=[
        ex("Verdadero o falso: comparar dos territorios significa decir cuál es mejor.", "Falso", "Comparar es buscar semejanzas y diferencias."),
        ex("¿Qué es un criterio de comparación? A) un punto igual para las dos comunidades, como «cómo se cuida el lugar» B) la opinión de quien compara", "A", "El criterio permite comparar con el mismo punto."),
        ex("Verdadero o falso: si dos comunidades se parecen en algo, todas las comunidades indígenas son iguales.", "Falso", "Dos ejemplos no representan a todos los pueblos."),
    ],
    A=[
        ex("Criterio: «quién cuida el lugar». Ladera Verde: las familias, cada año. Isla Niebla: toda la comunidad, entre todos. ¿Qué semejanza hay? A) el lugar lo cuida un grupo de personas B) el lugar no lo cuida nadie", "A", "En las dos comunidades hay un grupo que lo cuida."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) las dos comunidades cuidan su lugar entre varios b) una vive en cerros y otra en una isla.", "a semejanza, b diferencia", "La primera es algo en común; la segunda, algo distinto."),
        ex("Don Camilo dice: «El sendero nos lleva a la caleta». Completa: el sendero relaciona el bosque con…", "La caleta", "El testimonio dice que el sendero lleva a la caleta."),
    ],
    Z=[
        ex("Paula escribe: «Los cerros de Ladera Verde son más importantes que el mar de Isla Niebla». ¿Qué error comete?", "Jerarquiza dos territorios", "Cada comunidad vive el suyo a su manera."),
        ex("Pedro dice que, como las dos comunidades cuidan su lugar, todos los pueblos del país hacen lo mismo. ¿Por qué no es válido? A) dos casos no alcanzan para hablar de todos B) porque no cuidan nada", "A", "Hay muchos pueblos y cada uno cuenta su propia relación."),
    ],
    D=[
        ex("Tabla con el criterio «lo que une a las personas»: Ladera Verde, trabajar las terrazas; Isla Niebla, limpiar el sendero. ¿Cuál afirmación es correcta? A) en ambas comunidades las personas se unen en un trabajo del lugar B) solo en Ladera Verde las personas trabajan juntas", "A", "Las dos fuentes muestran un trabajo compartido."),
        ex("Quieres escribir sobre una tercera comunidad, Pampa Larga, pero no tienes ficha. ¿Qué haces? A) la dejo fuera hasta tener su ficha B) la describo por parecido a las otras", "A", "No se describe a una comunidad sin su propia fuente."),
    ],
    context=[ex("En un panel escolar dos grupos exponen Ladera Verde e Isla Niebla. Un visitante pregunta cuál es el territorio más valioso. ¿Qué respondes? A) cada comunidad lo vive a su manera y no se ordenan B) el de los cerros", "A", "Comparar no es jerarquizar.")],
    selfcheck=[
        ex("Escribe una semejanza entre Ladera Verde e Isla Niebla según este cuaderno.", "En ambas, el lugar se cuida entre varias personas", "Aparece en los dos testimonios."),
        ex("Verdadero o falso: puedo decir que un territorio es mejor que otro si me gusta más.", "Falso", "Eso es jerarquizar por gusto personal."),
        ex("¿Qué usas para comparar bien? A) los mismos criterios para las dos comunidades B) criterios distintos para cada una", "A", "Con criterios iguales la comparación es justa."),
    ],
    task=T("Lee dos relatos inventados. Ladera Verde (doña Elena): «Las terrazas las hicieron mis abuelos. Cada año las arreglamos entre las familias.» Isla Niebla (don Camilo): «El sendero lo abrieron los antiguos pescadores. Lo limpiamos entre todos para llegar a la caleta.» Haz una tabla con tres criterios: cómo se llama el lugar, quién lo cuida y qué relación hay entre las generaciones. Después escribe una semejanza y una diferencia. No digas cuál es mejor.",
           "Ladera Verde: terrazas, cuidan las familias, se unen abuelos y nietos. Isla Niebla: sendero, cuida toda la comunidad, se unen antiguos pescadores y actuales. Semejanza: ambos lugares los cuidan varias personas. Diferencia: uno es de cerro y el otro lleva a una caleta.",
           ["usa tres criterios iguales para ambas", "escribe una semejanza y una diferencia", "no jerarquiza"], ["tabla comparativa", "dos frases"], ["decir cuál es mejor", "generalizar a todos los pueblos"],
           "Pedir que muestre cada dato en el relato; valorar que no ordene de mejor a peor."),
    reinforce="Subraya con verde las semejanzas y con azul las diferencias en tu tabla.",
    extend="Escribe una pregunta que le harías a doña Elena para entender mejor cómo las terrazas se relacionan con la identidad de su comunidad.",
)

L(
    OA7, 4, materials=MAT,
    use="Aprenderé a construir una reflexión corta sobre la importancia del territorio, atribuyendo cada dato a su fuente. Sirve para opinar con respeto y sin hablar por otros.",
    prior=["Sé leer un testimonio con límites.", "Sé comparar dos comunidades sin jerarquizar."],
    explain=[
        "Una respuesta atribuida es una respuesta en que cada dato dice de quién viene. Se escribe con frases como «doña Elena cuenta que…» o «según don Camilo…». Así, quien lee puede distinguir lo que viene de la comunidad de lo que pienso yo. Es una forma de respeto y de honestidad.",
        "Para reflexionar sobre el territorio, la respuesta tiene cuatro partes. Primero, lo que cuenta la fuente. Segundo, mi reflexión, que explica qué me hace pensar eso. Tercero, un límite: lo que no sé o no se cuenta. Cuarto, una pregunta que llevaría al educador o educadora tradicional. Al terminar hacemos la devolución: mostramos lo escrito a la comunidad o al educador para que lo revisen y corrijan.",
        "Una reflexión sobre la importancia del territorio no dice que una comunidad es mejor ni que todas piensan igual. Dice, por ejemplo: «Según doña Elena, las terrazas guardan el trabajo de sus abuelos; yo pienso que el territorio ayuda a esa comunidad a recordar quiénes son».",
    ],
    vocab=[("respuesta atribuida", "respuesta en que cada dato dice de quién viene"), ("reflexión", "pensamiento propio sobre lo que se lee, con razones"), ("límite", "lo que no sé o no se cuenta"), ("devolución", "mostrar a la comunidad lo escrito para que lo revise"), ("pertenecer", "sentirse parte de un grupo o un lugar")],
    worked=[
        W("Escribir una reflexión atribuida", "Testimonio de don Aurelio, de Río Hondo (inventado): «El río es nuestro camino y nuestro sonido de cada día». Escribe una reflexión con las partes de la clase.", ["Fuente: don Aurelio dice que el río es su camino y su sonido de cada día.", "Reflexión: yo pienso que el río forma parte de la identidad de la comunidad.", "Límite: no sé qué otras cosas significa el río para ellos."], "Don Aurelio cuenta que el río es su camino y su sonido de cada día. Yo pienso que el río forma parte de su identidad. No sé qué otras cosas significa para ellos."),
        W("Corregir una atribución", "Un niño escribe: «Para Río Hondo el río es lo más sagrado». ¿Qué falta?", ["No dice quién lo afirma.", "El testimonio no habla de lo sagrado.", "Hay que atribuir y quitar lo que no está."], "Faltó atribuir a don Aurelio y quitar «lo más sagrado», que no está en el testimonio."),
    ],
    mistakes=[
        M("Escribir «los pueblos indígenas piensan que…» a partir de un solo testimonio.", "Un testimonio habla de una comunidad.", "Escribe «según don Aurelio, de Río Hondo…»."),
        M("No decir qué es opinión mía.", "El lector no puede distinguir la voz de la comunidad de la mía.", "Usa «yo pienso que…»."),
    ],
    R=[
        ex("¿Con qué frase empiezas para atribuir un dato a doña Elena? A) «Doña Elena cuenta que…» B) «Todos saben que…»", "A", "Nombra a la fuente."),
        ex("¿Cuántas partes tiene la reflexión de esta clase? Escribe el número.", "4", "Son fuente, reflexión, límite y pregunta."),
        ex("Verdadero o falso: mi reflexión es una idea mía y no del testimonio.", "Verdadero", "Por eso se rotula como mía."),
    ],
    C=[
        ex("¿Qué es una respuesta atribuida? A) una en que cada dato dice de quién viene B) una sin nombres", "A", "Atribuir es nombrar la fuente."),
        ex("Verdadero o falso: puedo escribir «los pueblos indígenas piensan lo mismo» después de leer un solo testimonio.", "Falso", "Un testimonio no representa a todos los pueblos."),
        ex("¿Para qué sirve la pregunta del final? A) para consultar al educador tradicional lo que no sé B) para terminar rápido", "A", "La pregunta señala lo que se debe consultar."),
    ],
    A=[
        ex("Testimonio de don Camilo: «El bosque nos da leña seca para el invierno». Completa la atribución: «Don Camilo cuenta que el bosque…»", "Les da leña seca para el invierno", "Repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o REFLEXIÓN: a) don Aurelio cuenta que el río es su camino b) yo pienso que el río los hace sentir en casa.", "a fuente, b reflexión", "La primera es un dato atribuido; la segunda es una idea propia."),
        ex("Una reflexión dice: «Doña Elena cuenta que cuidan las terrazas cada año; yo pienso que eso los une». ¿Qué parte es la reflexión?", "Yo pienso que eso los une", "Es la idea de quien escribe."),
    ],
    Z=[
        ex("Marta escribe una reflexión sin límite. Dice solo lo que sabe. ¿Qué mejoraría? A) agregar lo que no sé o no se cuenta B) agregar más datos inventados", "A", "El límite muestra hasta dónde llega lo afirmado."),
        ex("¿Por qué conviene mostrar tu reflexión a la comunidad o al educador? A) porque ellos pueden corregir errores sobre su territorio B) porque es obligatorio decorar", "A", "Ellos conocen su propia cultura."),
    ],
    D=[
        ex("Testimonio de doña Marta, de Pampa Larga (inventado): «El pozo es de todas las familias». Dos reflexiones: 1) «Doña Marta dice que el pozo es de todas las familias; yo pienso que eso une a la comunidad» 2) «Todos los pueblos comparten sus pozos». ¿Cuál es correcta?", "La primera", "La segunda generaliza sin fuente."),
        ex("Un compañero agrega a su reflexión una danza que, según él, hacen en Río Hondo, porque «seguro la tienen». El testimonio no la menciona. ¿Qué debe hacer?", "Quitarla porque no está en la fuente", "Lo no dicho por la fuente no se agrega."),
    ],
    context=[ex("Te piden un párrafo sobre la importancia del territorio para Ladera Verde. ¿Qué empieza mejor? A) «Doña Elena cuenta que…» B) «Todos los pueblos piensan que…»", "A", "Se atribuye el dato a la fuente.")],
    selfcheck=[
        ex("Nombra las cuatro partes de una reflexión atribuida.", "Fuente, reflexión, límite y pregunta", "Están en la explicación."),
        ex("Verdadero o falso: debo marcar qué es mi opinión.", "Verdadero", "Así no se confunde con la fuente."),
        ex("¿Qué haces al terminar? A) mostrarlo a la comunidad o al educador para que lo revise B) archivarlo sin mostrarlo", "A", "Es la devolución."),
    ],
    task=T("Usa este testimonio inventado de doña Elena: «Las terrazas las hicieron mis abuelos. Cada año las arreglamos entre las familias. Cuando camino por ellas, siento que mi familia sigue conmigo.» Escribe una reflexión de cuatro partes sobre la importancia del territorio para la identidad de Ladera Verde: 1) lo que cuenta doña Elena, 2) tu reflexión con «yo pienso que», 3) un límite y 4) una pregunta para el educador tradicional.",
           "1) Doña Elena cuenta que las terrazas las hicieron sus abuelos y que siente que su familia sigue con ella. 2) Yo pienso que las terrazas ayudan a que la comunidad recuerde quiénes son. 3) No sé qué significan las terrazas para otras familias. 4) Pregunta: ¿qué lugares son importantes para recordar la historia de nuestra comunidad?",
           ["atribuye cada dato", "reflexiona con razones", "incluye límite y pregunta"], ["texto de cuatro partes"], ["generalizar a todos los pueblos", "no marcar la opinión propia"],
           "Pedir que señale la línea del testimonio que respalda su reflexión."),
    reinforce="Enumera con 1, 2, 3 y 4 las partes de tu reflexión para comprobar que están todas.",
    extend="Reescribe tu reflexión cambiando la fuente por don Camilo, de Isla Niebla, y su sendero.",
)

# ============================================================ OA 08 · Historias de pueblos indígenas en relación
HLV = ("Historia oral inventada de Ladera Verde, contada por doña Elena: «Mis abuelos hicieron las terrazas hace muchos años. En 1950 llegó un camino a nuestros cerros. "
       "En 1975 se abrió una escuela cerca del corral. En 1990 las familias se juntaron para volver a sembrar las terrazas que estaban abandonadas.»")
HIN = ("Historia oral inventada de Isla Niebla, contada por don Camilo: «Los antiguos pescadores abrieron el sendero entre el bosque y la caleta. En 1960 llegó el primer bote con motor. "
       "En 1985 se abrió una escuela en la isla. En 2000 la comunidad se juntó para limpiar el sendero y volver a usarlo.»")

L(
    OA8, 1, materials=MAT,
    use="Aprenderé a situar la historia de un pueblo: quién la cuenta, de qué comunidad es y qué tipo de fuente es. Sirve para estudiar historias de otros pueblos sin mezclarlas con la del propio.",
    prior=["Sé situar un territorio con una ficha.", "Sé que cada comunidad cuenta su historia a su manera."],
    explain=[
        "La historia de un pueblo es lo que ese pueblo recuerda y cuenta sobre su pasado. Puede conservarse en la oralidad, es decir, en relatos que se cuentan de generación en generación, y también en escritos, objetos o lugares. Una historia oral es tan valiosa como una escrita, pero se cuenta desde una voz concreta.",
        "Para reflexionar sobre la historia de otros pueblos, primero hay que situar la fuente. Preguntamos quién cuenta, de qué comunidad es, de qué época habla, si dio permiso y qué parte no se cuenta. Con esos datos entendemos que el relato es una mirada y no «la historia de todos los pueblos».",
        "También hay que distinguir la historia del pueblo que corresponde, que es el que trabaja tu escuela junto al educador o educadora tradicional, de la historia de otros pueblos. No se mezclan sus datos ni se supone que una historia sea igual a otra. Las comparaciones vienen después y se hacen con respeto.",
    ],
    vocab=[("historia oral", "relato del pasado que se transmite hablando, de generación en generación"), ("hecho histórico", "algo que ocurrió en el pasado y se puede ubicar en el tiempo"), ("época", "período de tiempo, como un año o una década"), ("fuente histórica", "persona, texto u objeto que informa sobre el pasado"), ("pueblo que corresponde", "el pueblo que trabaja tu escuela junto al educador o educadora tradicional")],
    worked=[
        W("Situar una historia", HLV + " ¿Quién cuenta, de qué comunidad es y qué tipo de fuente es?", ["Cuenta doña Elena.", "La comunidad es Ladera Verde.", "Es una historia oral, contada hablando."], "La cuenta doña Elena, de Ladera Verde, como historia oral."),
        W("Ubicar hechos en el tiempo", "Con la historia de doña Elena: ¿qué ocurrió primero, el camino o la escuela?", ["El camino llegó en 1950.", "La escuela se abrió en 1975.", "1950 es antes que 1975."], "Primero llegó el camino (1950) y después la escuela (1975)."),
    ],
    mistakes=[
        M("Contar la historia de Ladera Verde como si fuera la historia de todos los pueblos.", "Cada pueblo tiene su propia historia.", "Escribe «según doña Elena, en Ladera Verde…»."),
        M("Pensar que una historia oral vale menos que una escrita.", "La oralidad es una forma válida de conservar el pasado.", "Trata ambas con la misma seriedad y atribuye cada fuente."),
    ],
    R=[
        ex("En la historia de Ladera Verde, ¿en qué año llegó el camino a los cerros?", "1950", "La historia oral lo señala."),
        ex("¿Quién cuenta la historia de Ladera Verde: don Camilo o doña Elena?", "Doña Elena", "La historia de Ladera Verde la cuenta doña Elena."),
        ex("Una historia que se cuenta hablando de generación en generación, ¿es oral o escrita?", "Oral", "La oralidad transmite relatos hablando."),
    ],
    C=[
        ex("Verdadero o falso: una historia oral vale menos que una escrita.", "Falso", "Ambas son formas válidas de conservar el pasado."),
        ex("¿Qué es el pueblo que corresponde? A) el pueblo que trabaja tu escuela junto al educador tradicional B) cualquier pueblo", "A", "Es el pueblo con el que tu escuela trabaja."),
        ex("Verdadero o falso: la historia de una comunidad se puede aplicar tal cual a todos los pueblos.", "Falso", "Cada pueblo tiene su propia historia."),
    ],
    A=[
        ex("Ordena los hechos de Isla Niebla del más antiguo al más reciente: A) escuela (1985) B) bote con motor (1960) C) limpiar el sendero (2000). Escribe las letras en orden.", "B, A, C", "Los años son 1960, 1985 y 2000."),
        arith("En Ladera Verde, el camino llegó en 1950 y la escuela se abrió en 1975. ¿Cuántos años pasaron entre ambos hechos?", "1975-1950", "Se restan los años."),
        ex("Una ficha histórica dice: «Fuente: doña Elena. Época: desde 1950. Permiso: sí». ¿Qué dato falta para situar la historia? A) la comunidad B) el color del papel", "A", "Falta decir de qué comunidad es el relato."),
    ],
    Z=[
        ex("Lucía dice: «Como en Ladera Verde llegó un camino en 1950, a todos los pueblos les llegó un camino en 1950». ¿Qué error comete?", "Generaliza un hecho de una comunidad", "Cada pueblo tiene su propia historia."),
        ex("Un compañero afirma: «La historia de Isla Niebla es la historia del pueblo que trabaja mi escuela». ¿Es válido sin consultar? A) No: hay que consultar al educador tradicional B) Sí, siempre", "A", "Solo el educador o la comunidad dicen cuál es la historia del pueblo que corresponde."),
    ],
    D=[
        arith("Isla Niebla: el primer bote con motor llegó en 1960 y la comunidad limpió el sendero en 2000. ¿Cuántos años pasaron entre ambos hechos?", "2000-1960", "Se restan los años."),
        ex("Una ficha no dice quién cuenta ni de qué época habla. ¿Qué falta para usarla? A) la fuente y la época B) más colores", "A", "Son datos para situar una historia."),
    ],
    context=[ex("Tu curso lee las historias de Ladera Verde e Isla Niebla. Una compañera quiere escribir en su trabajo cómo fue la historia de «los indígenas». ¿Qué le dices? A) que nombre la comunidad y la fuente de cada hecho B) que mezcle todo", "A", "Cada historia se atribuye a su comunidad y fuente.")],
    selfcheck=[
        ex("Nombra dos datos para situar una historia.", "Dos entre: quién cuenta, comunidad, época, permiso", "Permiten saber de quién es el relato."),
        ex("Verdadero o falso: la oralidad es una forma válida de conservar la historia.", "Verdadero", "Los relatos de generación en generación guardan el pasado."),
        ex("¿Qué haces si no sabes cuál es la historia del pueblo que corresponde? A) pregunto al educador tradicional B) la invento", "A", "Él o ella es la fuente."),
    ],
    task=T("Lee esta historia inventada de Pampa Larga, contada por doña Marta: «Las familias cavaron el pozo hace muchos años. En 1970 llegó una camioneta a la llanura. En 1995 se arregló el camino al pozo.» Haz una ficha histórica con: quién cuenta, comunidad, tipo de fuente (oral), dos hechos ordenados en el tiempo y una cosa que no sabes. Calcula cuántos años pasaron entre los dos años del relato.",
           "Cuenta: doña Marta. Comunidad: Pampa Larga. Fuente: historia oral. Hechos: 1970, llegó una camioneta; 1995, se arregló el camino al pozo. Pasaron 25 años. No sé quiénes cavaron el pozo.",
           ["situa la fuente", "ordena dos hechos", "calcula bien los años"], ["ficha histórica", "cálculo"], ["no decir quién cuenta", "agregar hechos que el relato no tiene"],
           "Pedir que indique en qué parte del relato está cada hecho."),
    reinforce="Dibuja una línea de tiempo con 1950, 1975 y 1990 para Ladera Verde y escribe un hecho en cada punto.",
    extend="Escribe dos preguntas para el educador tradicional sobre la historia del pueblo que corresponde a tu escuela.",
)

L(
    OA8, 2, materials=MAT,
    use="Aprenderé a leer una historia con límites declarados y a extraer los aspectos centrales sin completar lo que falta. Sirve para entender qué hechos marcaron a una comunidad.",
    prior=["Sé situar una historia con fuente y época.", "Sé separar lo que dice una fuente de lo que interpreto."],
    explain=[
        "Los aspectos centrales de una historia son los hechos que más cambiaron la vida de la comunidad. Para encontrarlos, buscamos qué ocurrió, cuándo y qué cambió después. Un hecho central puede ser la llegada de un camino, la apertura de una escuela o un trabajo que la comunidad retomó.",
        "Al leer una historia hay que respetar sus límites. La fuente puede decir «esto no lo cuento» o simplemente no mencionar algo. Lo que falta no se rellena. Tampoco se atribuye a la comunidad una opinión sobre un hecho si la fuente no la dio. Podemos escribir «el relato no dice qué pensaron las familias».",
        "Un buen resumen cuenta tres o cuatro hechos centrales en orden, con su fecha y con la frase «según la fuente». También separamos el cambio, es decir, lo que fue distinto después de un hecho, y la continuidad, es decir, lo que siguió igual.",
    ],
    vocab=[("hecho central", "hecho que cambió mucho la vida de una comunidad"), ("cambio", "lo que fue distinto después de un hecho"), ("continuidad", "lo que siguió igual a pesar del tiempo"), ("resumen", "texto breve con lo más importante"), ("según la fuente", "frase que muestra de quién viene el dato")],
    worked=[
        W("Elegir hechos centrales", HIN + " Elige dos hechos centrales.", ["Busco hechos que cambiaron la vida de la isla.", "El bote con motor (1960) y la escuela (1985) cambiaron cómo se trabajaba y aprendía.", "Los dos son hechos con fecha."], "Por ejemplo: la llegada del bote con motor (1960) y la apertura de la escuela (1985)."),
        W("Cambio y continuidad", "En Isla Niebla se abrió el sendero hace mucho y en 2000 la comunidad se juntó para limpiarlo. ¿Qué siguió igual?", ["El sendero seguía existiendo.", "La comunidad volvió a juntarse para cuidarlo.", "Eso es continuidad."], "El sendero y el trabajo comunitario para cuidarlo siguen."),
    ],
    mistakes=[
        M("Escribir qué sintieron las familias si el relato no lo dice.", "Es completar la historia con imaginación.", "Escribe «el relato no dice qué sintieron»."),
        M("Pensar que todo lo que pasó es un hecho central.", "Los hechos centrales son los que más cambiaron la vida de la comunidad.", "Elige los más importantes y explícalos."),
    ],
    R=[
        ex("En la historia de Isla Niebla, ¿qué llegó en 1960?", "El primer bote con motor", "El relato de don Camilo lo dice."),
        ex("En la historia de Isla Niebla, ¿en qué año se abrió la escuela?", "1985", "Don Camilo cuenta que fue en 1985."),
        ex("Si el relato no dice qué sintieron las familias, ¿qué escribes? A) el relato no lo dice B) lo inventó", "A", "No se rellenan los vacíos."),
    ],
    C=[
        ex("¿Qué es un hecho central de una historia? A) un hecho que cambió mucho la vida de la comunidad B) un detalle que nadie recuerda", "A", "Es un hecho importante para ese pueblo."),
        ex("Verdadero o falso: la continuidad es lo que siguió igual a pesar del tiempo.", "Verdadero", "Eso es lo que no cambió."),
        ex("Verdadero o falso: puedo agregar a la historia lo que «seguramente» sintieron las familias.", "Falso", "Solo se escribe lo que dice la fuente."),
    ],
    A=[
        ex("Historia de Ladera Verde: «En 1990 las familias se juntaron para volver a sembrar las terrazas». Marca el cambio y la continuidad: a) volver a sembrar b) las terrazas siguen existiendo.", "a cambio, b continuidad", "Volver a sembrar es algo distinto; las terrazas siguen."),
        ex("Resume en una frase la historia de Isla Niebla: «Según don Camilo, el sendero se abrió hace mucho y en 2000 la comunidad se juntó para…»", "Limpiarlo y volver a usarlo", "El relato lo cuenta así."),
        ex("De estos hechos de Ladera Verde, ¿cuál es el primero en el tiempo? A) la escuela en 1975 B) el camino en 1950 C) volver a sembrar en 1990", "B", "1950 es el año más antiguo."),
    ],
    Z=[
        ex("Daniel escribe: «Cuando llegó el camino, las familias de Ladera Verde estaban muy contentas». ¿Qué problema tiene la frase?", "El relato no dice cómo se sentían", "Agrega un sentimiento que no está en la fuente."),
        ex("¿Por qué no es lo mismo cambio que continuidad? A) el cambio es lo que fue distinto y la continuidad lo que siguió igual B) son sinónimos", "A", "Son ideas opuestas."),
    ],
    D=[
        ex("Don Camilo dijo que la historia del primer poblamiento de la isla no se cuenta. ¿Qué escribes en tu resumen? A) que esa parte no se cuenta B) una versión probable", "A", "Se respeta lo reservado."),
        ex("Dos resúmenes de Isla Niebla. Uno: «Según don Camilo, en 1960 llegó el bote con motor y en 1985 se abrió una escuela». Otro: «En 1960 llegó el bote y por eso desapareció la pesca antigua». ¿Cuál se queda en la fuente?", "El primero", "El segundo agrega una consecuencia que el relato no dice."),
    ],
    context=[ex("Para el diario mural de la escuela debes resumir la historia de Ladera Verde en una frase. ¿Cuál es mejor? A) «Según doña Elena, llegaron un camino y una escuela y en 1990 se volvió a sembrar» B) «Fue una historia triste»", "A", "La primera usa hechos de la fuente.")],
    selfcheck=[
        ex("Explica con tus palabras qué es la continuidad.", "Lo que siguió igual a pesar del tiempo", "Es la definición de la clase."),
        ex("Verdadero o falso: si algo no está en el relato, se escribe que el relato no lo dice.", "Verdadero", "No se rellena."),
        ex("¿Qué frase usas para atribuir un dato? A) «según la fuente…» B) «todos saben que…»", "A", "Nombra a la fuente."),
    ],
    task=T("Lee esta historia inventada de Río Hondo, contada por don Aurelio: «Las familias llegaron al río hace muchos años. En 1955 se construyó un puente de madera. En 1980 se abrió una escuela junto al bosque. En 2005 la comunidad arregló el puente para que siguiera sirviendo.» Escribe un resumen con tres hechos centrales en orden, indica un cambio y una continuidad y anota una cosa que el relato no dice. Calcula los años entre el puente y la escuela.",
           "Según don Aurelio: en 1955 se construyó un puente; en 1980 se abrió una escuela; en 2005 se arregló el puente. Cambio: llegó una escuela. Continuidad: el puente sigue sirviendo. El relato no dice quiénes construyeron el puente. Entre 1955 y 1980 pasaron 25 años.",
           ["ordena tres hechos", "distingue cambio y continuidad", "señala un vacío del relato"], ["resumen de tres hechos", "cálculo"], ["inventar sentimientos", "mezclar el orden"],
           "Pedir que muestre la línea del relato de cada hecho."),
    reinforce="Pinta de un color el cambio y de otro la continuidad en tu resumen.",
    extend="Explica por qué un cambio puede ser también una continuidad, con un ejemplo del puente.",
)

L(
    OA8, 3, materials=MAT,
    use="Aprenderé a reconocer elementos comunes y diferencias entre las historias de dos comunidades, sin decir que una es mejor. Sirve para entender mejor otras historias y la del pueblo que corresponde.",
    prior=["Sé extraer hechos centrales de una historia.", "Sé comparar sin jerarquizar."],
    explain=[
        "Al comparar historias buscamos dos cosas: los elementos comunes, que son lo que se parece, y las diferencias, que son lo que cambia. Para comparar bien usamos los mismos criterios en las dos historias. Dos criterios útiles son «qué llegó al territorio» y «cómo respondió la comunidad».",
        "Comparemos Ladera Verde e Isla Niebla. En ambas llegó algo nuevo a la comunidad: un camino en una y un bote con motor en la otra. En ambas se abrió una escuela. Y en ambas hubo un momento en que la comunidad se juntó para recuperar un trabajo: sembrar las terrazas o limpiar el sendero. Esas son semejanzas.",
        "Las diferencias están en los lugares, en los años y en lo que llegó. Que las historias sean distintas no significa que una sea más importante. Tampoco podemos concluir que todos los pueblos tuvieron las mismas experiencias: eso solo lo sabremos con las fuentes de cada pueblo. Por eso, al comparar con la historia del pueblo que corresponde, se usa el relato que cuenta el educador tradicional.",
    ],
    vocab=[("elemento común", "algo que se parece en dos historias"), ("diferencia", "algo que cambia entre dos historias"), ("criterio de comparación", "punto igual para las dos historias"), ("cuadro comparativo", "tabla con los mismos criterios para dos casos"), ("jerarquizar", "decir que una historia es mejor o más importante")],
    worked=[
        W("Armar un cuadro", HLV + " " + HIN + " Compara con el criterio «qué llegó al territorio».", ["Ladera Verde: llegó un camino (1950).", "Isla Niebla: llegó un bote con motor (1960).", "En ambas llegó algo nuevo, pero distinto."], "Elemento común: llegó algo nuevo. Diferencia: un camino en Ladera Verde y un bote con motor en Isla Niebla."),
        W("Evitar la jerarquía", "Un niño dice: «La historia de Ladera Verde es más importante porque es más antigua». ¿Está bien?", ["Las fuentes no ordenan por importancia.", "Que un hecho sea más antiguo no lo hace mejor.", "Hay que comparar sin ordenar."], "No: comparar historias no es ordenarlas por importancia."),
    ],
    mistakes=[
        M("Concluir que las historias son iguales porque se parecen en un punto.", "Se parecen en un criterio, no en todo.", "Escribe también las diferencias."),
        M("Decir que una historia es más importante que otra.", "Cada pueblo valora su historia a su manera.", "Compara sin ordenar de mejor a peor."),
    ],
    R=[
        ex("¿Qué llegó a Ladera Verde en 1950?", "Un camino", "La historia oral lo dice."),
        ex("¿Qué llegó a Isla Niebla en 1960? A) un bote con motor B) un camino", "A", "Don Camilo lo cuenta así."),
        ex("En las dos comunidades se abrió algo para aprender. ¿Qué fue?", "Una escuela", "Las dos historias mencionan una escuela."),
    ],
    C=[
        ex("¿Qué es un elemento común? A) algo que se parece en dos historias B) algo que solo está en una", "A", "Lo común aparece en ambas."),
        ex("Verdadero o falso: comparar historias es decidir cuál es más importante.", "Falso", "Comparar es buscar semejanzas y diferencias."),
        ex("Verdadero o falso: un cuadro comparativo usa los mismos criterios para las dos historias.", "Verdadero", "Así la comparación es justa."),
    ],
    A=[
        ex("Criterio «cuándo se abrió la escuela»: Ladera Verde, 1975; Isla Niebla, 1985. ¿Cuál se abrió primero?", "La de Ladera Verde", "1975 es antes que 1985."),
        ex("Clasifica en ELEMENTO COMÚN o DIFERENCIA: a) en ambas la comunidad se juntó para recuperar un trabajo b) una es de cerros y otra de isla.", "a elemento común, b diferencia", "La primera se parece; la segunda cambia."),
        arith("Ladera Verde abrió su escuela en 1975 e Isla Niebla en 1985. ¿Cuántos años de diferencia hay?", "1985-1975", "Se restan los años."),
    ],
    Z=[
        ex("Camila afirma: «Como las dos comunidades recuperaron un trabajo, todos los pueblos lo hacen». ¿Qué error comete?", "Generaliza desde dos casos", "Dos casos no representan a todos los pueblos."),
        ex("Un compañero dice que la historia de Isla Niebla es peor porque tiene menos hechos en el relato. ¿Qué respondes? A) el relato es corto, pero eso no mide su valor B) tiene razón", "A", "Los relatos no se ordenan por cantidad de hechos."),
    ],
    D=[
        ex("Cuadro con el criterio «cómo respondió la comunidad»: Ladera Verde, se juntó a volver a sembrar (1990); Isla Niebla, se juntó a limpiar el sendero (2000). ¿Cuál afirmación es correcta? A) en ambas la comunidad respondió trabajando junta B) solo en una la comunidad trabajó junta", "A", "Los dos relatos muestran trabajo comunitario."),
        ex("Quieres comparar con la historia del pueblo que corresponde a tu escuela, pero no la conoces. ¿Qué haces? A) pido el relato al educador tradicional B) supongo que es igual a la de Isla Niebla", "A", "La fuente es el educador o la comunidad."),
    ],
    context=[ex("En una exposición escolar, alguien pregunta cuál de las dos historias es la mejor. ¿Qué respondes? A) que las historias se comparan, pero no se ordenan de mejor a peor B) que la de Ladera Verde", "A", "Comparar no es jerarquizar.")],
    selfcheck=[
        ex("Escribe un elemento común entre las historias de Ladera Verde e Isla Niebla.", "En ambas llegó algo nuevo y se abrió una escuela", "Aparece en las dos historias."),
        ex("Verdadero o falso: dos historias que se parecen en un punto son iguales.", "Falso", "Pueden diferir en otros puntos."),
        ex("¿Qué necesitas para comparar con la historia del pueblo que corresponde? A) su relato contado por el educador tradicional B) una suposición", "A", "Hace falta la fuente."),
    ],
    task=T("Compara estas dos historias inventadas. Pampa Larga (doña Marta): «En 1970 llegó una camioneta a la llanura. En 1995 se arregló el camino al pozo.» Río Hondo (don Aurelio): «En 1955 se construyó un puente de madera. En 2005 la comunidad arregló el puente.» Haz un cuadro con dos criterios: «qué llegó o se construyó» y «cómo respondió la comunidad». Escribe una semejanza, una diferencia y una frase que diga qué no puedes concluir.",
           "Pampa Larga: llegó una camioneta; la comunidad arregló el camino (1995). Río Hondo: se construyó un puente; la comunidad lo arregló (2005). Semejanza: en ambas arreglaron algo. Diferencia: una camioneta y un camino frente a un puente. No puedo concluir que todos los pueblos arreglen sus caminos.",
           ["usa dos criterios iguales", "escribe semejanza y diferencia", "no generaliza"], ["cuadro comparativo", "tres frases"], ["decir cuál historia es mejor", "generalizar a todos los pueblos"],
           "Pedir que indique la línea del relato de cada dato y qué no puede concluir."),
    reinforce="Marca con verde lo común y con azul lo distinto en tu cuadro.",
    extend="Escribe qué fuente necesitarías para comparar estas historias con la del pueblo que corresponde a tu escuela.",
)

L(
    OA8, 4, materials=MAT,
    use="Aprenderé a escribir una comparación de historias donde cada dato diga de quién viene. Sirve para reflexionar sobre la historia de otros pueblos con respeto y sin generalizar.",
    prior=["Sé comparar historias con criterios iguales.", "Sé atribuir cada dato a su fuente."],
    explain=[
        "Una comparación atribuida tiene cuatro partes. Primero, lo que cuenta cada fuente, con su nombre. Segundo, los elementos comunes. Tercero, las diferencias. Cuarto, los límites: lo que no sé, lo que las fuentes no cuentan y lo que debo preguntar al educador o educadora tradicional.",
        "Cada afirmación lleva una marca de dónde viene. Por ejemplo: «Según doña Elena, en 1950 llegó un camino a Ladera Verde. Según don Camilo, en 1960 llegó un bote con motor a Isla Niebla. En las dos comunidades llegó algo nuevo». La última frase es mi comparación, y se apoya en dos fuentes.",
        "En el texto no aparecen frases como «los pueblos indígenas siempre…» ni «la mejor historia es…». Se habla de estas dos comunidades. Si vamos a compartir la comparación, pedimos que el educador o la comunidad la revisen: es la validación. Al final se agrega una frase sobre el pueblo que corresponde a tu escuela: «Para compararlo necesito conocer su relato, que me contará el educador tradicional».",
    ],
    vocab=[("comparación atribuida", "comparación en que cada dato dice de quién viene"), ("límite", "lo que no sé o no se cuenta"), ("generalizar", "decir que algo vale para todos a partir de unos pocos casos"), ("relato", "historia que se cuenta"), ("validación", "revisión del trabajo por la comunidad o el educador tradicional")],
    worked=[
        W("Armar una comparación", "Doña Elena: «En 1975 se abrió una escuela cerca del corral». Don Camilo: «En 1985 se abrió una escuela en la isla». Escribe una comparación atribuida.", ["Atribuyo cada dato a su fuente.", "Busco lo común: en las dos se abrió una escuela.", "Busco la diferencia: los años, 1975 y 1985."], "Según doña Elena, en Ladera Verde se abrió una escuela en 1975. Según don Camilo, en Isla Niebla se abrió en 1985. En ambas comunidades se abrió una escuela, pero con diez años de diferencia."),
        W("Revisar la generalización", "Alguien escribe: «Todos los pueblos recibieron escuelas entre 1975 y 1985». ¿Qué corriges?", ["Solo hay dos fuentes.", "No sabemos de los demás pueblos.", "Hay que hablar solo de estas dos comunidades."], "Corrijo: «En estas dos comunidades, según sus fuentes, la escuela llegó en 1975 y 1985»."),
    ],
    mistakes=[
        M("Generalizar a todos los pueblos a partir de dos comunidades.", "No hay fuentes de los demás pueblos.", "Escribe «en estas dos comunidades»."),
        M("No marcar de quién viene cada dato.", "Se confunden las voces de las fuentes con la mía.", "Usa «según doña Elena…» o «según don Camilo…»."),
    ],
    R=[
        ex("¿Con qué frase de inicio atribuyes un dato a doña Elena? Escribe las tres primeras palabras.", "Según doña Elena", "Es la forma de atribuir."),
        ex("¿Cuántas partes tiene la comparación atribuida? Escribe el número.", "4", "Son fuentes, comunes, diferencias y límites."),
        ex("En 1985 se abrió una escuela según don Camilo. ¿En qué comunidad?", "Isla Niebla", "Don Camilo es de Isla Niebla."),
    ],
    C=[
        ex("¿Qué es generalizar? A) decir que algo vale para todos a partir de unos pocos casos B) contar un solo caso", "A", "Es salir de los casos conocidos a todos."),
        ex("Verdadero o falso: en una comparación atribuida se puede escribir «los pueblos indígenas siempre hicieron lo mismo».", "Falso", "Es una generalización sin fuente."),
        ex("Verdadero o falso: al final se muestra el trabajo al educador tradicional para que lo revise.", "Verdadero", "Es la validación."),
    ],
    A=[
        ex("Completa la atribución con los datos: «Según don Aurelio, en Río Hondo se construyó en 1955 un…»", "Puente de madera", "El relato de Río Hondo lo dice."),
        ex("Clasifica en DATO DE UNA FUENTE o MI COMPARACIÓN: a) según doña Marta, en 1970 llegó una camioneta a Pampa Larga b) en ambas comunidades hubo trabajo compartido.", "a dato de una fuente, b mi comparación", "La primera es un dato; la segunda une dos fuentes."),
        ex("Una comparación dice: «En ambas llegó algo nuevo, pero no sé cómo lo vivieron las familias». ¿Qué parte es el límite?", "No sé cómo lo vivieron las familias", "Es lo que la fuente no cuenta."),
    ],
    Z=[
        ex("Ignacio escribe una comparación sin nombrar fuentes. ¿Qué problema tiene? A) no se sabe de quién viene cada dato B) tiene muchos datos", "A", "Falta la atribución."),
        ex("¿Por qué la comparación termina diciendo qué no se sabe del pueblo que corresponde? A) porque su relato se obtiene del educador tradicional B) porque no importa", "A", "Esa historia la cuenta su propia fuente."),
    ],
    D=[
        ex("Tres frases sobre Pampa Larga y Río Hondo. 1) «Según doña Marta, en 1970 llegó una camioneta.» 2) «Según don Aurelio, en 1955 se construyó un puente.» 3) «Todos los pueblos reciben cosas nuevas.» ¿Cuál no debería estar en una comparación atribuida?", "La tercera", "Generaliza sin fuente."),
        ex("Dos comparaciones. A: «En ambas comunidades la comunidad arregló algo; no sé por qué». B: «En ambas comunidades arreglaron algo porque estaban tristes». ¿Cuál respeta la fuente?", "A", "B inventa el motivo."),
    ],
    context=[ex("Para el acto de fin de unidad, un grupo comparará dos historias. ¿Qué frase del cartel es mejor? A) «Según sus fuentes, en dos comunidades se abrió una escuela» B) «Todos los pueblos tuvieron escuela»", "A", "La primera se queda en las fuentes.")],
    selfcheck=[
        ex("Nombra las cuatro partes de una comparación atribuida.", "Lo que cuenta cada fuente, elementos comunes, diferencias y límites", "Están en la explicación."),
        ex("Verdadero o falso: puedo escribir «todos los pueblos» si comparé solo dos.", "Falso", "Eso sería generalizar."),
        ex("¿Qué frase usas para marcar un límite? A) «No sé…» B) «Seguro que…»", "A", "Reconoce lo que falta."),
    ],
    task=T("Usa estas dos historias inventadas. Ladera Verde (doña Elena): «En 1950 llegó un camino. En 1990 las familias volvieron a sembrar las terrazas.» Isla Niebla (don Camilo): «En 1960 llegó un bote con motor. En 2000 la comunidad limpió el sendero.» Escribe una comparación atribuida con las cuatro partes: fuentes, elementos comunes, diferencias y límites. Agrega una frase sobre lo que necesitas para compararlas con la historia del pueblo que corresponde a tu escuela.",
           "Según doña Elena, en 1950 llegó un camino y en 1990 volvieron a sembrar. Según don Camilo, en 1960 llegó un bote y en 2000 limpiaron el sendero. Común: llegó algo nuevo y la comunidad retomó un trabajo. Diferencia: los lugares y los años. Límite: no sé qué pensaron las familias. Para compararlas con el pueblo que corresponde necesito el relato que cuente el educador tradicional.",
           ["atribuye las fuentes", "no generaliza", "incluye límites y el pueblo que corresponde"], ["comparación de cuatro partes"], ["generalizar a todos los pueblos", "inventar pensamientos de las familias"],
           "Pedir que señale la fuente de cada dato; valorar que reconozca lo que falta."),
    reinforce="Pon un número del 1 al 4 en cada parte de tu comparación.",
    extend="Escribe una pregunta para el educador tradicional sobre un hecho central de la historia del pueblo que corresponde.",
)

# ============================================================ OA 09 · Diversidad lingüística y diálogo intercultural
L(
    OA9, 1, materials=MAT + " Esta clase usa solo nombres de pueblos y lenguas de amplio conocimiento.",
    use="Aprenderé a situar la diversidad de pueblos indígenas y lenguas que hay en Chile y a valorarla. Sirve para dialogar con respeto con personas de otros pueblos.",
    prior=["Sé que cada pueblo tiene su historia y su territorio.", "Sé que lo tradicional lo enseña el educador o la educadora tradicional."],
    explain=[
        "En el territorio chileno viven muchos pueblos indígenas. Algunos de ellos son el mapuche, el aymara, el rapa nui, el quechua, el kawésqar y el yagán. Cada pueblo tiene su propia historia, su territorio y su lengua. La lengua del pueblo mapuche es el mapuzugun; la del pueblo aymara, el aymara; la del pueblo rapa nui, el rapa nui; y los pueblos quechua, kawésqar y yagán tienen la suya, que lleva el mismo nombre. Por eso se habla de diversidad: no existe un solo pueblo indígena ni una sola lengua.",
        "Los pueblos viven en distintas zonas. Por ejemplo, el pueblo aymara está en el norte del país, el pueblo mapuche en la zona centro-sur, el pueblo rapa nui en Rapa Nui (isla de Pascua), en el océano Pacífico, y los pueblos kawésqar y yagán en el extremo sur, entre canales y fiordos. Estas son ubicaciones generales y cada pueblo las explica mejor que nosotros.",
        "Algunas lenguas se hablan hoy en muchos lugares y otras tienen pocas personas que las hablan, y por eso se trabaja para fortalecerlas, es decir, revitalizarlas. Valorar la diversidad significa reconocerla y respetar que cada pueblo y cada lengua tiene su lugar. No se ordenan de mejor a peor.",
    ],
    vocab=[("diversidad", "existencia de muchas formas distintas"), ("pueblo indígena", "pueblo que habita un territorio desde antes de la formación del Estado"), ("lengua", "sistema de palabras y reglas con que un pueblo se comunica"), ("revitalización", "trabajo para que una lengua vuelva a usarse más"), ("intercultural", "entre personas de culturas distintas que dialogan con respeto")],
    worked=[
        W("Ubicar pueblos en zonas generales", "¿En qué zona general de Chile está el pueblo aymara?", ["Recuerdo la lista de zonas.", "El pueblo aymara está en el norte.", "Es una ubicación general."], "En el norte de Chile (ubicación general)."),
        W("Evitar ordenar lenguas", "Un niño dice: «El mapuzugun es más importante que el aymara». ¿Está bien?", ["Las lenguas no se ordenan por importancia.", "Cada una pertenece a un pueblo.", "Hay que valorar la diversidad."], "No: todas las lenguas son valiosas y no se ordenan."),
    ],
    mistakes=[
        M("Pensar que hay una sola lengua indígena en Chile.", "Cada pueblo tiene su propia lengua.", "Nombra la lengua de cada pueblo."),
        M("Decir que algunas lenguas son «mejores» que otras.", "Todas tienen igual valor.", "Valora la diversidad sin ordenar."),
    ],
    R=[
        ex("¿En qué zona general de Chile está el pueblo aymara? A) el norte B) el extremo sur", "A", "El pueblo aymara está en el norte."),
        ex("¿Dónde está el pueblo rapa nui? A) en Rapa Nui (isla de Pascua), en el Pacífico B) en los canales del sur", "A", "Rapa Nui es una isla en el océano Pacífico."),
        ex("¿Cuál es un pueblo indígena real de Chile: el pueblo mapuche o la comunidad Ladera Verde de este cuaderno?", "El pueblo mapuche", "Ladera Verde es una comunidad inventada de este cuaderno."),
    ],
    C=[
        ex("Verdadero o falso: en Chile hay un solo pueblo indígena.", "Falso", "Hay varios pueblos, cada uno con su historia."),
        ex("¿Qué significa revitalizar una lengua? A) trabajar para que se use más B) dejar de usarla", "A", "Es fortalecer su uso."),
        ex("Verdadero o falso: la diversidad es una riqueza y no una razón para ordenar pueblos de mejor a peor.", "Verdadero", "Valorar es reconocer sin ordenar."),
    ],
    A=[
        ex("Une pueblo y zona general: 1) aymara 2) kawésqar a) norte b) extremo sur", "1-a, 2-b", "Los aymara están en el norte y los kawésqar en el extremo sur."),
        ex("¿Qué pueblo está en la zona centro-sur? A) mapuche B) rapa nui", "A", "El pueblo rapa nui está en una isla del Pacífico."),
        ex("De estas lenguas, ¿cuál es del pueblo aymara? A) el aymara B) el mapuzugun", "A", "El mapuzugun es la lengua del pueblo mapuche."),
    ],
    Z=[
        ex("Tomás dice: «Si conozco el mapuzugun, conozco las lenguas indígenas de Chile». ¿Qué error comete?", "Cada pueblo tiene su propia lengua", "El mapuzugun es una lengua entre varias."),
        ex("¿Por qué se dice que la ubicación de los pueblos que aprendimos es solo general? A) porque cada pueblo explica mejor su territorio B) porque no existen", "A", "El territorio lo cuenta su propia comunidad."),
    ],
    D=[
        ex("Rosa afirma: «Si una lengua tiene pocas personas que la hablan, vale menos». ¿Qué respondes? A) el valor de una lengua no depende de cuántos la hablan B) tiene razón", "A", "Todas las lenguas tienen igual valor."),
        ex("Un compañero cuenta que su vecino «habla otra lengua». Tú no sabes cuál. ¿Qué haces? A) le preguntas con respeto cuál es B) supones una", "A", "Se pregunta, no se supone."),
    ],
    context=[ex("En un mural escolar quieren poner el nombre de un pueblo y su lengua. ¿Qué dupla es correcta? A) pueblo aymara y lengua aymara B) pueblo mapuche y lengua aymara", "A", "La lengua del pueblo mapuche es el mapuzugun.")],
    selfcheck=[
        ex("Nombra tres pueblos indígenas de Chile.", "Tres entre: mapuche, aymara, rapa nui, quechua, kawésqar, yagán", "Están en la explicación."),
        ex("Verdadero o falso: valorar la diversidad es ordenar los pueblos de mejor a peor.", "Falso", "Valorar es reconocer y respetar."),
        ex("¿A quién preguntas por la lengua de un pueblo? A) al educador tradicional o a la comunidad B) a nadie", "A", "Ellos son la fuente."),
    ],
    task=T("Haz un afiche con tres pueblos indígenas de Chile que estén en la explicación: escribe el pueblo, su lengua (solo el nombre) y su zona general. Al final escribe una frase que valore la diversidad sin comparar pueblos. No agregues palabras de ninguna lengua indígena, salvo que el educador tradicional te las indique.",
           "Pueblo aymara, lengua aymara, norte. Pueblo mapuche, lengua mapuzugun, centro-sur. Pueblo rapa nui, lengua rapa nui, isla del Pacífico. En Chile hay muchos pueblos y lenguas, y todos merecen respeto.",
           ["nombra tres pueblos y sus lenguas", "ubica la zona general", "valora sin comparar"], ["afiche con tres filas", "frase final"], ["agregar palabras inventadas", "decir que un pueblo es mejor"],
           "Pedir que explique de dónde sacó cada dato; valorar que no agregue palabras que no conoce."),
    reinforce="Une con flechas cada pueblo de tu afiche con su zona general en un dibujo simple del país.",
    extend="Escribe una pregunta que le harías al educador tradicional sobre la lengua del pueblo que corresponde a tu escuela.",
)

L(
    OA9, 2, materials=MAT,
    use="Aprenderé a escuchar a una persona que habla otra lengua o variante, con límites declarados: qué entiendo, qué no y qué debo preguntar. Sirve para dialogar con respeto.",
    prior=["Sé que hay muchos pueblos y lenguas en Chile.", "Sé que no se inventan palabras de otras lenguas."],
    explain=[
        "El diálogo intercultural es una conversación entre personas de culturas distintas en la que todas son escuchadas y respetadas. Para que funcione, escuchamos sin interrumpir, preguntamos cuando no entendemos y no juzgamos lo que nos parece distinto.",
        "Cuando una persona usa palabras de su lengua, no las repetimos de memoria ni adivinamos su significado. Preguntamos cómo se dicen, cómo se escriben y qué significan, y anotamos quién nos lo enseñó. Una misma lengua puede tener variantes, es decir, formas distintas de hablar según el lugar. Ninguna variante es «más correcta» que otra.",
        "Un ejemplo ampliamente conocido es el saludo «mari mari» del mapuzugun, la lengua del pueblo mapuche. Podemos mencionarlo, pero la pronunciación y los usos los enseña el educador o la educadora tradicional. Si no estamos seguros de algo, decimos «no lo sé, ¿me lo enseñas?».",
    ],
    vocab=[("diálogo intercultural", "conversación respetuosa entre personas de culturas distintas"), ("variante", "forma distinta de hablar una misma lengua según el lugar"), ("escuchar activamente", "atender sin interrumpir y preguntar si no entiendo"), ("autorización", "permiso de una persona para compartir lo que enseñó"), ("pronunciación", "manera de decir una palabra")],
    worked=[
        W("Escuchar con respeto", "Una vecina de un pueblo indígena te saluda en su lengua. Tú no conoces esa lengua. ¿Qué haces?", ["No imito sin saber cómo se dice.", "Agradezco el saludo.", "Pregunto cómo se pronuncia y qué significa."], "Agradezco, pregunto cómo se dice y qué significa, y anoto quién me lo enseñó."),
        W("Variantes", "Dos personas dicen una palabra de su lengua de manera algo distinta, porque viven en lugares diferentes. ¿Cuál está equivocada?", ["Una lengua puede tener variantes.", "Cada variante se usa en un lugar.", "Ninguna es más correcta."], "Ninguna: son variantes de la misma lengua."),
    ],
    mistakes=[
        M("Inventar una palabra o su significado para sonar «indígena».", "Es irrespetuoso y puede ser falso.", "Pregunta al educador tradicional."),
        M("Corregir a alguien porque lo dice distinto.", "Puede ser una variante.", "Pregunta de dónde es su forma de hablar."),
    ],
    R=[
        ex("¿Qué haces si no entiendes lo que dijo una persona en su lengua? A) pregunto con respeto B) me río", "A", "Preguntar es una forma de respeto."),
        ex("¿El saludo «mari mari» pertenece a la lengua mapuzugun o al aymara?", "Mapuzugun", "Es un saludo del mapuzugun."),
        ex("¿Quién enseña la pronunciación de una palabra de un pueblo? A) el educador tradicional o la comunidad B) cualquiera", "A", "Ellos son la fuente."),
    ],
    C=[
        ex("Verdadero o falso: una variante es una forma distinta de hablar una misma lengua.", "Verdadero", "Cambia según el lugar."),
        ex("Verdadero o falso: puedo inventar el significado de una palabra si suena parecido a otra.", "Falso", "Sería inventar lengua."),
        ex("¿Qué es el diálogo intercultural? A) una conversación respetuosa entre culturas distintas B) una pelea entre culturas", "A", "Todas las personas son escuchadas."),
    ],
    A=[
        ex("Alguien te enseña una palabra de su lengua. ¿Qué haces al final, después de agradecer y preguntar cómo se pronuncia? A) anoto quién me la enseñó B) la cuento como si fuera mía", "A", "Anotar la fuente reconoce a quien enseñó."),
        ex("Una compañera cuenta: «Dos personas que viven en lugares distintos dicen una palabra de su lengua un poco diferente». Según lo aprendido, ¿qué es probable? A) que sean variantes B) que una de las dos se equivoque", "A", "Puede haber variantes por lugar."),
        ex("Clasifica en RESPETUOSO o NO RESPETUOSO: a) interrumpir y reírse de la pronunciación b) preguntar con calma cómo se dice.", "a no respetuoso, b respetuoso", "La primera ofende; la segunda muestra interés."),
    ],
    Z=[
        ex("Ana dice «mari mari» como broma para molestar a un compañero. ¿Qué error comete? ", "Usa un saludo como burla", "Los saludos y palabras de una lengua se respetan."),
        ex("¿Por qué anotar quién te enseñó una palabra? A) para reconocer la fuente y devolver el crédito B) para ocupar más espacio", "A", "La fuente merece reconocimiento."),
    ],
    D=[
        ex("Un visitante dice: «Esa forma de decir no es correcta». Tú piensas en lo aprendido. ¿Qué respondes? A) puede ser una variante, ¿me explicas? B) tiene razón", "A", "Las variantes no se corrigen."),
        ex("Quieres escribir una palabra de una lengua indígena en tu cartel, pero no sabes cómo se escribe. ¿Qué haces? A) pregunto al educador tradicional B) la escribo como creo", "A", "La escritura la valida quien enseña."),
    ],
    context=[ex("En el patio una niña te enseña un saludo de su familia. Una compañera lo repite para burlarse. ¿Qué haces? A) pido respeto y agradezco a la niña por enseñarlo B) me río", "A", "Se cuida el diálogo y la autorización de quien enseñó.")],
    selfcheck=[
        ex("Escribe dos acciones de un diálogo intercultural respetuoso.", "Dos entre: escuchar sin interrumpir, preguntar, no juzgar, agradecer", "Son parte de la explicación."),
        ex("Verdadero o falso: puedo adivinar el significado de una palabra que no conozco.", "Falso", "Se pregunta siempre."),
        ex("¿Qué es una variante? Escribe una frase corta.", "Una forma distinta de hablar la misma lengua según el lugar", "Es la definición de la clase."),
    ],
    task=T("Escribe un diálogo corto, de cuatro intervenciones, entre dos estudiantes: Lía, que llegó de otra región, y Sami, que conoce un saludo en mapuzugun («mari mari»). Lía no conoce la palabra. Muestra cómo Sami explica con respeto, qué pregunta Lía y cómo ambos dicen que la pronunciación la enseñará el educador tradicional. No inventes otras palabras de ninguna lengua.",
           "Lía: Escuché que dices «mari mari», ¿qué es? Sami: Es un saludo del mapuzugun, la lengua del pueblo mapuche. Lía: ¿Cómo se pronuncia bien? Sami: No estoy seguro; le preguntaremos al educador tradicional.",
           ["cuatro intervenciones", "usa solo «mari mari»", "escucha y pregunta con respeto"], ["diálogo de cuatro intervenciones"], ["inventar palabras", "burlarse o corregir sin preguntar"],
           "Pedir que lea el diálogo en voz alta y que explique qué hace cada personaje para respetar al otro."),
    reinforce="Subraya en tu diálogo las frases que muestran respeto.",
    extend="Escribe dos frases que podrías decir cuando no entiendes algo de otra cultura.",
)

L(
    OA9, 3, materials=MAT,
    use="Aprenderé a reconocer relaciones entre lenguas, territorios y pueblos, y a ver que la diversidad es una riqueza. Sirve para dialogar sin comparar de mejor a peor.",
    prior=["Sé nombrar algunos pueblos y lenguas de Chile.", "Sé que no se ordenan lenguas ni pueblos."],
    explain=[
        "Cada lengua tiene una relación con un territorio y con un pueblo. En la lengua de un pueblo hay palabras que nombran sus lugares, sus alimentos, sus historias y sus formas de organizarse. Por eso, cuando una lengua se debilita, también se debilita parte del conocimiento del pueblo.",
        "Hoy muchos pueblos trabajan para recuperar sus lenguas: las enseñan en escuelas, las usan en programas, y las conversan en la familia. Ese trabajo se llama revitalización. También se hace con ayuda de personas mayores y educadores tradicionales que saben la lengua; a quienes la hablan los llamamos hablantes.",
        "Para dialogar, es útil saber que hay relaciones entre lenguas y también diferencias. No es correcto decir que una lengua indígena es «solo un dialecto» ni que es «más primitiva». Cada una es un sistema completo. En un diálogo intercultural, quien conversa reconoce esas diferencias y pregunta a quien sabe.",
    ],
    vocab=[("revitalización", "trabajo para que una lengua vuelva a usarse más"), ("territorio lingüístico", "zona donde se habla una lengua"), ("hablante", "persona que habla una lengua"), ("conocimiento ancestral", "saberes que un pueblo ha transmitido por generaciones"), ("programa de lengua", "actividad organizada para enseñar una lengua")],
    worked=[
        W("Relacionar lengua y saber", "Una comunidad inventada tiene muchos nombres propios para los vientos de su llanura. ¿Qué relación hay entre la lengua y su territorio?", ["La lengua tiene palabras para el territorio.", "Esas palabras guardan saberes sobre el viento.", "Perder la lengua perdería parte de esos saberes."], "La lengua guarda saberes sobre el territorio."),
        W("Ver la revitalización", "Una escuela invita a una persona mayor de la comunidad a enseñar su lengua. ¿Qué tipo de trabajo es?", ["Se enseña a quienes no la hablan.", "Se hace con una persona mayor que la sabe.", "Es una forma de revitalización."], "Es revitalización: se fortalece el uso de la lengua."),
    ],
    mistakes=[
        M("Decir que una lengua indígena es solo un dialecto.", "Cada lengua es un sistema completo.", "Habla de lengua, no de dialecto menor."),
        M("Pensar que revitalizar una lengua es inventar palabras nuevas.", "Es fortalecer el uso de las existentes con quienes la saben.", "Trabaja con hablantes y educadores tradicionales."),
    ],
    R=[
        ex("Una persona que habla una lengua se llama… A) hablante B) lector", "A", "Es el nombre de quien habla una lengua."),
        ex("Si una lengua deja de usarse, ¿qué se debilita también? A) los saberes de ese pueblo B) el clima", "A", "Los saberes se guardan en la lengua."),
        ex("¿Cómo se llama el trabajo para que una lengua vuelva a usarse más?", "Revitalización", "Es la definición de la clase."),
    ],
    C=[
        ex("Verdadero o falso: cada lengua es un sistema completo y tiene valor propio.", "Verdadero", "Ninguna es menos que otra."),
        ex("Verdadero o falso: revitalizar una lengua consiste en inventar palabras nuevas.", "Falso", "Consiste en fortalecer su uso con quienes la saben."),
        ex("¿Dónde se guardan los nombres de lugares y alimentos de un pueblo? A) en su lengua B) solo en los mapas", "A", "La lengua guarda esas palabras."),
    ],
    A=[
        ex("Clasifica en ACCIÓN DE REVITALIZACIÓN o NO: a) una persona mayor enseña su lengua en la escuela b) se prohíbe hablar la lengua en clase.", "a revitalización, b no", "La primera fortalece el uso; la segunda lo impide."),
        ex("Una comunidad inventada tiene muchas palabras para cada tipo de viento de su llanura. ¿Qué saber guarda esa lengua? A) saberes sobre el viento B) saberes sobre el mar", "A", "Los nombres del viento guardan saberes del territorio."),
        ex("Una escuela propone tres acciones: 1) invitar a una persona mayor que habla la lengua; 2) usar palabras sacadas de un video sin preguntar; 3) practicar con una hablante que lo autoriza. ¿Cuáles apoyan la revitalización con respeto? A) 1 y 3 B) 2 y 3 C) 1 y 2", "A", "La 2 usa palabras sin fuente autorizada."),
    ],
    Z=[
        ex("Pedro dice: «La lengua de un pueblo pequeño es menos importante». ¿Qué error comete?", "Ordena lenguas por tamaño", "Todas las lenguas tienen igual valor."),
        ex("¿Por qué una escuela invita a una persona mayor a enseñar su lengua? A) porque ella la sabe y puede transmitirla B) porque es más divertido", "A", "La persona mayor es una fuente de la lengua."),
    ],
    D=[
        ex("Una niña de Pampa Larga (inventada) aprende palabras de su lengua con una persona mayor de su comunidad. Su amigo dice que es «una pérdida de tiempo». ¿Qué le respondes? A) es una forma de mantener viva la lengua B) tiene razón", "A", "Aprenderla con quienes la saben es revitalizar."),
        ex("En una feria hay carteles de tres pueblos con sus lenguas. Alguien pregunta cuál es «la mejor». ¿Qué respondes? A) todas valen y no se ordenan B) la que tiene más hablantes", "A", "La diversidad se valora sin ordenar."),
    ],
    context=[ex("Tu curso quiere organizar un día de las lenguas con invitados de comunidades. ¿Qué debe hacer primero? A) invitar al educador tradicional o a personas de la comunidad que lo autoricen B) imitar palabras en internet", "A", "La fuente y su autorización van primero.")],
    selfcheck=[
        ex("Escribe una relación entre lengua y territorio.", "La lengua guarda nombres de lugares y saberes del territorio", "Es una idea central de la clase."),
        ex("Verdadero o falso: revitalizar es trabajar para que la lengua se use más.", "Verdadero", "Es la definición."),
        ex("¿Qué haces ante la lengua de otro pueblo? A) respeto y pregunto B) la comparo con la mía", "A", "No se ordenan lenguas."),
    ],
    task=T("Lee: «La comunidad inventada de Pampa Larga quiere que sus niños aprendan su lengua. Doña Marta, que la habla, ofrece enseñarla los sábados.» Haz una lista de tres cosas que la escuela puede hacer para apoyar esa revitalización (por ejemplo, invitar, prestar un espacio, escuchar) y una cosa que NO debe hacer. Cierra con una frase que valore la diversidad.",
           "La escuela puede invitar a doña Marta, prestar una sala y organizar horarios. No debe inventar palabras ni prohibir que se hable. Cierra: cada lengua es una riqueza de nuestro país.",
           ["lista de tres apoyos", "una cosa a evitar", "valora la diversidad"], ["lista de tres acciones", "frase final"], ["inventar palabras de la lengua", "decir que una lengua vale más que otra"],
           "Pedir que explique cómo cada acción respeta a doña Marta como fuente."),
    reinforce="Escribe tres palabras en español que nombren cosas de tu barrio y compáralas con las de un compañero, sin ordenarlas.",
    extend="Explica con un ejemplo por qué perder una lengua también es perder saberes.",
)

L(
    OA9, 4, materials=MAT,
    use="Aprenderé a construir una invitación o mensaje de diálogo intercultural respetuoso, con cada dato atribuido. Sirve para favorecer el diálogo entre personas de pueblos distintos.",
    prior=["Sé nombrar pueblos y lenguas de Chile.", "Sé dialogar respetando y preguntando."],
    explain=[
        "Una respuesta atribuida en esta clase es un mensaje de diálogo. Dice qué aprendimos, de quién lo aprendimos y qué queremos preguntar. Por ejemplo: «Aprendí del educador tradicional que mi comunidad escolar trabaja con la lengua de su pueblo. Quiero preguntarte cómo puedo ayudar».",
        "Un buen mensaje de diálogo tiene cuatro partes. Primero, saludar y presentarse. Segundo, decir lo que aprendimos y de qué fuente. Tercero, decir lo que no sabemos y hacer una pregunta respetuosa. Cuarto, agradecer y pedir que revisen el mensaje si lo vamos a compartir.",
        "En el mensaje no usamos palabras de una lengua indígena que no hayamos aprendido de una fuente autorizada. Tampoco decimos que un pueblo es mejor que otro. Al final guardamos una copia con el nombre de quien nos ayudó y le damos las gracias.",
    ],
    vocab=[("mensaje de diálogo", "texto breve que busca conversar con respeto"), ("saludar", "decir hola de manera cordial"), ("agradecer", "decir gracias por lo recibido"), ("fuente autorizada", "persona que permitió compartir lo que enseñó"), ("revisión", "lectura de un trabajo para corregirlo")],
    worked=[
        W("Armar un mensaje", "Escribe un mensaje de diálogo a un educador tradicional, con las cuatro partes.", ["Saludo y me presento.", "Cuento lo que aprendí y de quién.", "Digo lo que no sé, pregunto y agradezco."], "Hola, soy estudiante de 5.º. Aprendí de mi curso que hay varios pueblos y lenguas en Chile. No sé cómo se enseña la lengua del pueblo de mi escuela. ¿Podría explicarnos? Gracias."),
        W("Corregir un mensaje", "Un mensaje dice: «Todos los indígenas hablan igual». ¿Qué corriges?", ["Hay muchos pueblos y lenguas.", "Cada lengua es distinta.", "Cambia a una frase respetuosa."], "«En Chile hay varios pueblos indígenas y cada uno tiene su propia lengua»."),
    ],
    mistakes=[
        M("Usar palabras de una lengua indígena que no aprendí de una fuente autorizada.", "Puedo equivocarme y ofender.", "Pregunta antes de usarlas."),
        M("Terminar sin agradecer ni pedir revisión.", "El diálogo queda incompleto.", "Agradece y pide que revisen lo que vas a compartir."),
    ],
    R=[
        ex("¿Cuántas partes tiene un buen mensaje de diálogo en esta clase? Escribe el número.", "4", "Son saludar, contar lo aprendido, preguntar y agradecer."),
        ex("¿Qué se hace primero en un mensaje de diálogo? A) saludar y presentarse B) pedir algo", "A", "Se empieza con un saludo cordial."),
        ex("¿Qué se dice al final del mensaje? A) gracias B) una orden", "A", "Se agradece la ayuda."),
    ],
    C=[
        ex("Verdadero o falso: puedo escribir palabras de una lengua indígena sin saber de dónde las aprendí.", "Falso", "Hay que tener una fuente autorizada."),
        ex("¿Para qué sirve decir lo que no sabemos? A) para hacer una pregunta respetuosa B) para parecer ignorantes", "A", "Reconocer lo que falta abre el diálogo."),
        ex("Verdadero o falso: un mensaje de diálogo puede decir que un pueblo es mejor que otro.", "Falso", "El diálogo no jerarquiza."),
    ],
    A=[
        ex("Ordena las partes del mensaje: A) agradecer B) saludar C) preguntar D) contar lo aprendido. Escribe las letras en orden.", "B, D, C, A", "Primero se saluda, luego se cuenta, se pregunta y se agradece."),
        ex("Completa el saludo con el dato correcto: «Hola, soy estudiante de 5.º de la escuela…» ¿Qué sigue? A) y quiero preguntarte algo B) y no me interesa", "A", "Se presenta la intención con respeto."),
        ex("Clasifica en RESPETUOSA o NO: a) «¿Podría explicarnos cómo se enseña la lengua de su pueblo?» b) «Seguro que su lengua es fácil».", "a respetuosa, b no", "La primera pregunta con interés; la segunda supone y minimiza."),
    ],
    Z=[
        ex("Camila quiere agregar una palabra que escuchó en un video, sin saber si es correcta. ¿Qué es mejor? A) preguntar al educador B) agregarla igual", "A", "No se usa lengua sin fuente autorizada."),
        ex("¿Por qué se pide que revisen el mensaje antes de compartirlo? A) porque la comunidad puede corregir lo que quedó mal B) porque es un trámite", "A", "Ellos conocen su cultura."),
    ],
    D=[
        ex("Dos mensajes. A: «Soy Tomás, aprendí de la profesora que hay varios pueblos. No sé la lengua de mi comunidad: ¿me ayudan? Gracias». B: «Sé todo de su pueblo». ¿Cuál es un mensaje de diálogo respetuoso?", "A", "B afirma saber todo y no pregunta."),
        ex("Un mensaje usa tres palabras de una lengua que su autor no aprendió de nadie. ¿Qué debería hacer antes de enviarlo? A) quitarlas o consultar al educador B) dejarlas", "A", "Sin fuente autorizada no se usan."),
    ],
    context=[ex("Tu escuela invitará a una familia de otro pueblo a una charla. Te piden escribir la invitación. ¿Qué incluye? A) saludo, lo que aprendiste, una pregunta y gracias B) solo la fecha", "A", "Son las cuatro partes del mensaje.")],
    selfcheck=[
        ex("Nombra las cuatro partes de un mensaje de diálogo.", "Saludar, contar lo aprendido, preguntar y agradecer", "Están en la explicación."),
        ex("Verdadero o falso: debo guardar el nombre de quien me ayudó.", "Verdadero", "Es una forma de reconocer la fuente."),
        ex("¿Qué haces antes de compartir tu mensaje? A) pedir que lo revisen B) enviarlo sin mirar", "A", "La revisión evita errores."),
    ],
    task=T("Escribe un mensaje de diálogo de cuatro partes dirigido a una persona de una comunidad indígena que visita tu escuela (puedes llamarla «invitada»). Debes: saludar, contar dos cosas que aprendiste sobre la diversidad de pueblos y lenguas de Chile, hacer una pregunta respetuosa y agradecer. No uses palabras de lenguas indígenas, salvo que alguien autorizado te las enseñe.",
           "Hola, soy estudiante de 5.º. Aprendí que en Chile hay varios pueblos indígenas y que cada uno tiene su propia lengua. También aprendí que las lenguas no se ordenan de mejor a peor. ¿Cómo podemos apoyar el uso de la lengua de su pueblo? Muchas gracias por visitarnos.",
           ["incluye las cuatro partes", "usa dos datos aprendidos", "no usa lengua inventada"], ["mensaje de cuatro partes"], ["inventar palabras", "comparar pueblos de mejor a peor"],
           "Pedir que lea el mensaje y señale cada parte."),
    reinforce="Numera las cuatro partes de tu mensaje con 1, 2, 3 y 4.",
    extend="Escribe una versión de tu mensaje para presentarlo en un panel, con una sola pregunta.",
)
