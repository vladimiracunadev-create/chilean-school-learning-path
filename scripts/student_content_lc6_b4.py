"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR01 (historias de eventos de otros pueblos, reflexión y uso de la lengua indígena en funciones sociales básicas) y
OA LR02 (exposición y diálogo oral de análisis sociocultural y espiritual, incorporando vocabulario pertinente).

Criterio de autoría: comunidades, personas e historias son INVENTADAS y rotuladas como tales; no describen ritos reales.
Las únicas palabras en lengua indígena son «mari mari» y «chaltumay» (mapuzugun) y «iorana» y «maururu» (rapa nui).
Las demás expresiones y el vocabulario de cada lengua los entrega el educador o la educadora tradicional; en los
ejercicios aparecen como espacio por completar y nunca se inventan. Importa los ayudantes de student_content_lc6_b.
"""
from __future__ import annotations

from student_content_lc6_b import ab, vf, L, M, T, W, MAT
from student_lessons import arith, ex

LR1, LR2 = "LC06 OA LR01", "LC06 OA LR02"

# ============================================================ OA LR01 · Historias y funciones sociales básicas
L(
    LR1, 1, materials=MAT,
    use="Aprenderé a situar la historia de un evento de otro pueblo y a reconocer funciones sociales básicas del lenguaje (saludar, agradecer, pedir permiso, despedirse). Sirve para comprender la historia y usar la lengua con respeto.",
    prior=["Sé que una fuente es la persona que cuenta una historia.", "Sé que la lengua indígena la enseña el educador o la educadora tradicional."],
    explain=[
        "Las funciones sociales básicas del lenguaje son las cosas que hacemos con las palabras para convivir: saludar al llegar, presentarnos, pedir permiso, agradecer y despedirnos. Todas las lenguas tienen formas de cumplir esas funciones, aunque cada una lo hace a su manera. Saber reconocerlas nos ayuda a comprender mejor una historia y a participar con respeto.",
        "Una historia sobre un evento, como una reunión de vecinos, muestra esas funciones en acción. Antes de leerla la situamos con una ficha: comunidad, evento, fuente, permiso y límite. Así sabemos de quién es y qué no se cuenta. Después buscamos qué funciones aparecen y quién las realiza.",
        "En esta clase solo conocemos como expresiones atestiguadas «mari mari» (saludo en mapuzugun), «chaltumay» (gracias en mapuzugun), «iorana» (saludo en rapa nui) y «maururu» (gracias en rapa nui). Para las demás funciones y para tu lengua, el educador o la educadora tradicional te enseña las expresiones. Nunca las inventamos.",
    ],
    vocab=[("función social", "lo que hacemos con las palabras para convivir, como saludar o agradecer"), ("saludar", "dar la bienvenida o reconocer a alguien al encontrarlo"), ("agradecer", "reconocer lo que otra persona hizo por nosotros"), ("pedir permiso", "preguntar si se puede hacer algo antes de hacerlo"), ("despedirse", "cerrar un encuentro con una frase amable")],
    worked=[
        W("Leer una ficha", "Ficha inventada. Comunidad: Monte Claro (no es un pueblo real). Evento: Reunión de vecinos de otoño. Fuente: doña Silvia, vecina. Permiso: sí. Límite: no se cuentan los temas privados de la reunión. ¿Qué evento es y qué no se cuenta?", ["El evento es la reunión de vecinos de otoño.", "La fuente es doña Silvia y dio permiso.", "No se cuentan los temas privados."], "Es la reunión de vecinos de otoño; no se cuentan los temas privados."),
        W("Reconocer funciones", "Historia inventada: «Al llegar, la familia saludó a todos. Antes de entrar, un niño pidió permiso a la persona mayor. Al irse, agradecieron la invitación.» ¿Qué funciones aparecen?", ["«Saludó a todos»: saludar.", "«Pidió permiso»: pedir permiso.", "«Agradecieron»: agradecer."], "Saludar, pedir permiso y agradecer."),
    ],
    mistakes=[
        M("Pensar que saludar y agradecer son iguales en todas las lenguas.", "Cada lengua tiene sus formas.", "Usa las que enseña el educador."),
        M("Inventar una expresión en lengua indígena para una función.", "Puede no existir o tener otro sentido.", "Deja el espacio y pregunta."),
    ],
    R=[
        ex("Ficha: «Comunidad: Estero Dulce. Evento: Día de los vecinos. Fuente: don Aníbal.» ¿Quién es la fuente?", "Don Aníbal", "La ficha lo nombra."),
        ex("¿Qué función cumple decir «gracias»? A) agradecer B) despedirse", "A", "Reconoce lo que otro hizo."),
        ex("¿Qué significa «mari mari» en mapuzugun?", "Saludo", "Es un saludo muy conocido."),
    ],
    C=[
        vf("«maururu» es una forma de agradecer en rapa nui.", True, "Está atestiguada como gracias."),
        vf("todas las lenguas saludan exactamente igual.", False, "Cada lengua tiene sus formas."),
        ab("¿Quién enseña las expresiones de las funciones sociales en la lengua de tu comunidad?", "el educador o la educadora tradicional", "un compañero que las busca", "Quien enseña la lengua las entrega."),
    ],
    A=[
        ex("Historia inventada: «Al llegar a la sede, la vecina dijo mari mari a todos». ¿Qué función cumple su frase? A) saludar B) pedir permiso", "A", "«Mari mari» es un saludo."),
        ex("Clasifica en SALUDAR, AGRADECER o PEDIR PERMISO: a) «¿Puedo pasar?» b) «Mari mari» c) «Chaltumay por la comida».", "a pedir permiso, b saludar, c agradecer", "Cada frase cumple una función distinta."),
        ex("Una ficha trae comunidad y evento, pero no dice la fuente ni el permiso. ¿Qué haces? A) pido esos datos antes de usarla B) la uso igual", "A", "Sin fuente ni permiso se detiene la actividad."),
    ],
    Z=[
        ex("Lucas inventa una frase para «pedir permiso» en lengua indígena porque «suena parecida». ¿Qué error comete?", "Inventa una expresión sin consultar", "La lengua la enseña el educador."),
        ex("Marta cuenta con detalle los temas privados de la reunión de Monte Claro. ¿Qué falla? A) no respeta el límite de la ficha B) usa pocas funciones", "A", "El límite pide no contarlos."),
    ],
    D=[
        ex("Dos historias: en una se saluda y se agradece; en la otra solo se saluda. ¿Cuál muestra más funciones sociales?", "La primera", "Tiene dos funciones; la otra, una."),
        ex("Escribes un cartel con «iorana» y «maururu». ¿Qué significan en ese orden? A) saludo y gracias en rapa nui B) gracias y saludo", "A", "«Iorana» saluda y «maururu» agradece."),
    ],
    context=[ab("Vas a visitar a una persona mayor de la comunidad con tu curso. ¿Qué funciones sociales usarás al llegar y al irte?", "saludar al llegar y agradecer y despedirse al irte", "no decir nada", "Esas funciones muestran respeto.")],
    selfcheck=[
        ex("Nombra tres funciones sociales básicas.", "Tres entre: saludar, presentarse, pedir permiso, agradecer, despedirse", "Son funciones de la clase."),
        vf("conviene preguntar al educador cómo se dice «gracias» en la lengua de mi comunidad.", True, "Él o ella lo enseña."),
        ex("¿Qué escribes en lugar de inventar una expresión? A) un espacio para completar con el educador B) cualquier palabra", "A", "Se evita inventar."),
    ],
    task=T("Lee esta historia inventada de doña Silvia, de Monte Claro: «Cuando llegó el invierno, los vecinos se reunieron en la sede. Una niña saludó a la persona mayor y pidió permiso para sentarse. Al terminar, todos agradecieron la invitación y se despidieron con un abrazo». Haz una ficha con comunidad, evento, fuente y límite. Después anota tres funciones sociales que aparecen y quién las realiza.",
           "Comunidad: Monte Claro. Evento: reunión de invierno. Fuente: doña Silvia. Límite: no sé qué temas se hablaron. Funciones: saludar (la niña), pedir permiso (la niña) y agradecer (todos).",
           ["completa la ficha", "identifica tres funciones", "dice quién las realiza"], ["ficha completa", "lista de funciones"], ["inventar expresiones en lengua", "contar lo privado"],
           "Pedir que señale la frase de cada función; valorar que respete el límite."),
    reinforce="Subraya en la historia las tres funciones sociales con tres colores.",
    extend="Explica por qué saludar y agradecer son maneras de mostrar respeto.",
)

L(
    LR1, 2, materials=MAT,
    use="Aprenderé a escuchar o leer una historia con límites declarados y a reflexionar sobre ella separando lo que dice, lo que interpreto y lo que no se cuenta. Sirve para comprender sin inventar.",
    prior=["Sé situar una historia con su ficha.", "Sé reconocer funciones sociales básicas."],
    explain=[
        "Reflexionar sobre una historia es pensar qué nos dice y por qué importa. Para hacerlo bien, separamos tres cosas: lo que la historia dice, lo que yo interpreto y lo que no se cuenta. Lo que dice la historia lo afirmo; lo que interpreto lo marco con «yo pienso que»; lo que no se cuenta lo dejo como pregunta.",
        "En una historia aparecen funciones sociales: alguien saluda, alguien pide permiso, alguien agradece. Preguntarse quién las hace, a quién se dirigen y qué efecto tienen ayuda a comprender cómo se cuidan las personas en esa comunidad. Por ejemplo: si una niña pide permiso a una persona mayor, interpreto que se respeta a los mayores, pero lo marco como mi idea.",
        "Los límites se declaran al final: «la historia no dice cómo se saluda en la lengua» o «no se cuenta de qué se habló». Si quiero conocer las expresiones de mi comunidad, pregunto al educador o a la educadora tradicional.",
    ],
    vocab=[("reflexionar", "pensar qué nos dice una historia y por qué importa"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("efecto", "lo que una acción produce"), ("límite", "lo que no se cuenta o no se sabe"), ("respeto", "tratar con consideración a las personas")],
    worked=[
        W("Separar tres cosas", "Historia inventada de don Aníbal, de Estero Dulce: «Cuando llega una visita, se presentan por su nombre. Luego se pregunta cómo estuvo el camino. Hay una frase de bienvenida que solo dice la comunidad». Separa lo que dice, lo que interpreto y lo que no se cuenta.", ["Dice: la visita se presenta y luego le preguntan por el camino.", "Interpreto: yo pienso que así la hacen sentir bienvenida.", "No se cuenta: la frase de bienvenida."], "Dice: se presentan y preguntan por el camino. Interpreto: la hacen sentir bienvenida. No se cuenta: la frase de bienvenida."),
        W("Efecto de una función", "Una niña pide permiso a la persona mayor antes de pasar. ¿Qué efecto puede tener?", ["Muestra consideración.", "La persona mayor se siente respetada.", "Lo escribo como interpretación."], "Yo pienso que muestra respeto por la persona mayor."),
    ],
    mistakes=[
        M("Escribir mi idea como si la hubiera dicho la historia.", "Se confunde lo propio con lo ajeno.", "Marca con «yo pienso que»."),
        M("Completar con ideas lo que la comunidad no contó.", "Se inventa.", "Escribe «la historia no lo dice»."),
    ],
    R=[
        ex("En la historia de Estero Dulce, ¿qué hace la visita al llegar? A) se presenta por su nombre B) cocina", "A", "La historia lo dice así."),
        ex("¿Qué escribes cuando la historia no explica algo? A) la historia no lo dice B) lo invento", "A", "Se declara el límite."),
        ex("¿Qué palabra marca una idea mía? A) «yo pienso que» B) «la comunidad dice que»", "A", "Marca lo propio."),
    ],
    C=[
        vf("una interpretación es una idea mía sobre lo que leí.", True, "Es lo que yo pienso."),
        vf("puedo completar con mi imaginación lo que la comunidad no contó.", False, "Eso sería inventar."),
        ab("¿Qué conviene preguntar sobre una función social en una historia?", "quién la hace y a quién se dirige", "cuántas palabras tiene", "Eso muestra cómo se cuidan las personas."),
    ],
    A=[
        ex("Historia: «Al irse, la visita agradeció y se despidió». Clasifica en DICE LA HISTORIA o INTERPRETO: a) la visita agradeció b) la visita se sintió muy querida.", "a dice la historia, b interpreto", "La segunda es una suposición."),
        ex("Una visita se presenta por su nombre en Estero Dulce. ¿Qué función social es? A) presentarse B) despedirse", "A", "Presentarse es decir quién soy."),
        ex("La historia no dice cómo se saluda en la lengua. ¿Qué escribes en los límites? A) la historia no dice cómo se saluda en la lengua B) se saluda de una forma inventada", "A", "Se declara lo que no se sabe."),
    ],
    Z=[
        ex("Rodrigo escribe sin marcar: «En Estero Dulce todos son muy simpáticos». ¿Qué debería hacer?", "Marcarlo como opinión o quitarlo", "La historia no dice eso."),
        ex("¿Por qué conviene declarar los límites al final? A) para mostrar hasta dónde llega lo afirmado B) para llenar espacio", "A", "Los límites muestran lo que no se sabe."),
    ],
    D=[
        ex("Dos frases sobre la historia de Estero Dulce. Una: «Se pregunta cómo estuvo el camino». Otra: «Se pregunta porque temen a los desconocidos». ¿Cuál se queda en la historia?", "La primera", "La segunda inventa una razón."),
        ex("La historia dice «hay una frase de bienvenida solo de la comunidad». ¿Qué haces con esa frase en tu trabajo? A) escribo que existe, sin inventarla B) la invento", "A", "Se respeta lo reservado."),
    ],
    context=[ab("Un compañero pide que le cuentes la frase de bienvenida de Estero Dulce. ¿Qué respondes?", "que la historia dice que es solo de la comunidad", "que te la inventas", "La historia reserva esa frase.")],
    selfcheck=[
        ex("Nombra las tres cosas que separo al reflexionar sobre una historia.", "Lo que dice, lo que interpreto y lo que no se cuenta", "Son los tres pasos."),
        vf("quien pide permiso a una persona mayor muestra respeto.", True, "Es una función social de respeto."),
        ex("¿Dónde consulto una duda sobre la lengua? A) con el educador o la educadora tradicional B) lo imagino", "A", "Ellos enseñan la lengua."),
    ],
    task=T("Lee esta historia inventada de doña Silvia, de Monte Claro: «Al llegar a la sede, los niños saludaron a los mayores. Una niña pidió permiso para pasar a la cocina. Al terminar, agradecieron la comida. Hay una canción de despedida que solo cantan entre vecinos.» Haz tres columnas: «La historia dice», «Yo interpreto» y «No se cuenta». Pon al menos dos datos en cada una y una frase de límites.",
           "La historia dice: los niños saludaron; una niña pidió permiso; agradecieron la comida. Yo interpreto: yo pienso que los niños aprenden a ser respetuosos. No se cuenta: la canción de despedida. Límite: la historia no dice cómo se saluda en la lengua.",
           ["separa tres columnas", "marca interpretación", "declara límites"], ["tabla de tres columnas", "frase de límites"], ["inventar la canción", "atribuir ideas propias"],
           "Pedir que indique la línea de cada dato; valorar que respete la canción reservada."),
    reinforce="Subraya con un color lo que dice la historia y con otro lo que interpretas.",
    extend="Escribe una pregunta para el educador sobre cómo se saluda en la lengua de tu comunidad.",
)

L(
    LR1, 3, materials=MAT,
    use="Aprenderé a relacionar cada función social con su situación y con las personas que participan. Sirve para elegir qué función usar y a quién dirigirla.",
    prior=["Sé reconocer funciones sociales en una historia.", "Sé separar lo que dice la historia de lo que interpreto."],
    explain=[
        "Cada función social aparece en una situación. Saludamos al llegar; pedimos permiso antes de entrar o de usar algo ajeno; agradecemos cuando alguien nos ayuda; nos despedimos al irnos. También importa a quién nos dirigimos: no hablamos igual a una persona mayor que a un compañero, ni a alguien que conocemos que a una visita.",
        "Para relacionar función, situación y persona usamos una tabla de tres columnas. En la primera va la situación («llego a la sede»), en la segunda la función («saludar») y en la tercera, la persona («una persona mayor»). Así planificamos qué decir antes de hablar.",
        "Para decir las funciones en la lengua indígena de tu comunidad, pregunta al educador o a la educadora tradicional. Entre las expresiones atestiguadas, «mari mari» y «iorana» sirven para saludar; «chaltumay» y «maururu», para agradecer. Las otras funciones las enseña el educador con ejemplos de la comunidad.",
    ],
    vocab=[("situación", "momento o lugar en que ocurre algo"), ("destinatario", "persona a quien se dirigen las palabras"), ("tabla", "cuadro de filas y columnas que ordena información"), ("visita", "persona que llega a un lugar que no es suyo"), ("trato", "manera de dirigirse a alguien")],
    worked=[
        W("Completar una tabla", "Situación: llegas a la sede y está una persona mayor. ¿Qué función y a quién?", ["La situación es llegar.", "La función es saludar.", "La persona es una persona mayor."], "Función: saludar; destinatario: una persona mayor."),
        W("Elegir la función", "Una vecina te ayudó a cargar tus útiles. ¿Qué función usas?", ["Alguien me ayudó: corresponde reconocerlo.", "La función es agradecer.", "Puedo decir chaltumay si el educador lo recomienda en mapuzugun."], "Agradecer."),
    ],
    mistakes=[
        M("Usar la misma función en todas las situaciones.", "Cada situación pide una función distinta.", "Pregúntate qué ocurrió y a quién hablas."),
        M("Hablar a todas las personas con el mismo trato.", "No es igual con un mayor que con un compañero.", "Cambia el trato según la persona."),
    ],
    R=[
        ex("¿Qué función usas al llegar a un lugar? A) saludar B) despedirse", "A", "Al llegar se saluda."),
        ex("¿Qué función usas cuando alguien te ayudó? A) agradecer B) pedir permiso", "A", "Se reconoce la ayuda."),
        ex("¿Qué función usas antes de entrar a una casa ajena? A) pedir permiso B) despedirte", "A", "Se pregunta antes de entrar."),
    ],
    C=[
        vf("la misma función sirve para todas las situaciones.", False, "Cada situación pide una función distinta."),
        vf("el destinatario es la persona a quien se dirigen las palabras.", True, "Esa es su definición."),
        ab("¿Qué expresión atestiguada sirve para saludar en rapa nui?", "iorana", "maururu", "«Iorana» es un saludo; «maururu» agradece."),
    ],
    A=[
        ex("Relaciona la situación con la función: a) te vas de la casa de un vecino b) quieres usar el teléfono de la sede. Escribe DESPEDIRSE o PEDIR PERMISO para cada una.", "a despedirse, b pedir permiso", "Al irte te despides; para usar algo ajeno, pides permiso."),
        ex("Completa la tabla: situación «llego a la sede», función ______. A) saludar B) agradecer", "A", "Al llegar se saluda."),
        ex("Un vecino te regala pan. ¿Qué expresión atestiguada en mapuzugun puedes usar para agradecer? A) chaltumay B) mari mari", "A", "«Chaltumay» agradece; «mari mari» saluda."),
    ],
    Z=[
        ex("Pía saluda con el mismo trato a una autoridad y a su compañero de banco. ¿Qué error comete?", "No adapta el trato a la persona", "El trato cambia según el destinatario."),
        ex("Un niño pide permiso después de entrar. ¿Qué falla? A) debía pedir permiso antes de entrar B) no saludó con una canción", "A", "El permiso se pide antes."),
    ],
    D=[
        ex("Tienes que planificar una visita: llegar, entrar, recibir una ayuda y irte. ¿Qué cuatro funciones usas en orden? A) saludar, pedir permiso, agradecer, despedirse B) agradecer, saludar, despedirse, pedir permiso", "A", "El orden sigue la visita."),
        arith("Una visita tiene 4 funciones sociales y repites cada una en 3 casas. ¿Cuántas veces usas funciones en total?", "4*3", "Se multiplican las funciones por las casas.", " veces"),
    ],
    context=[ab("Tu curso será recibido en la sede de la comunidad. Una compañera propone dar las gracias antes de saludar. ¿Qué le dices?", "que primero saludamos al llegar y luego agradecemos", "que está bien", "Cada función va en su momento.")],
    selfcheck=[
        ex("Nombra una función y una situación en que se usa.", "Saludar al llegar; agradecer al recibir ayuda; pedir permiso antes de entrar", "Son pares función-situación de la clase."),
        vf("«chaltumay» es una forma de agradecer en mapuzugun.", True, "Está atestiguada como agradecimiento."),
        ex("¿Quién enseña las funciones en la lengua de tu comunidad? A) el educador o la educadora tradicional B) un buscador", "A", "Ellos enseñan la lengua."),
    ],
    task=T("Completa una tabla de tres columnas («Situación», «Función», «Persona») con estas cuatro situaciones: 1) llegas a la sede y hay una persona mayor; 2) quieres sentarte junto a la ventana de la sede y alguien ya está allí; 3) una vecina te regala una fruta; 4) te vas de la sede. Para la función de saludar y la de agradecer anota la expresión atestiguada que podrías usar y deja un espacio [expresión del educador] para las otras dos.",
           "1) llegar / saludar (mari mari) / persona mayor. 2) pedir lugar / pedir permiso [expresión del educador] / la persona que ya está. 3) recibir fruta / agradecer (chaltumay) / vecina. 4) irse / despedirse [expresión del educador] / los presentes.",
           ["tabla de tres columnas completa", "usa solo expresiones atestiguadas", "deja espacio para el educador"], ["tabla completa"], ["inventar expresiones", "repetir la misma función"],
           "Pedir que explique por qué cada función corresponde; valorar que no invente."),
    reinforce="Une cada situación con su función en una lista de cuatro.",
    extend="Escribe dos situaciones nuevas de tu vida diaria y la función social que usarías en cada una.",
)

L(
    LR1, 4, materials=MAT,
    use="Aprenderé a escribir una reflexión corta sobre una historia, atribuida a su fuente, e incorporar una función social con la expresión que enseñe el educador. Sirve para opinar con respeto y usar la lengua.",
    prior=["Sé relacionar funciones con situaciones.", "Sé separar lo que dice la fuente de lo que opino."],
    explain=[
        "Una reflexión atribuida tiene cuatro partes. Primero, lo que cuenta la fuente: «Según doña Silvia…». Segundo, mi reflexión con una razón: «Yo pienso que… porque…». Tercero, un límite: lo que no sé. Cuarto, una función social con la expresión que enseña el educador, para cerrar con respeto.",
        "Por ejemplo, tras la historia de Monte Claro puedo escribir: «Según doña Silvia, los niños saludan a los mayores. Yo pienso que eso muestra respeto porque se reconocen unos a otros. No sé cómo se saluda en la lengua de la comunidad. Para cerrar, agradezco con chaltumay a quien nos contó la historia».",
        "La expresión de la función social la tomo de las que están atestiguadas o la dicta el educador. Si no la tengo, dejo un espacio [expresión del educador]. Luego muestro mi reflexión a quien me enseña para que la revise y la corrija.",
    ],
    vocab=[("reflexión atribuida", "pensamiento propio que dice la fuente y la razón"), ("razón", "dato que respalda una idea"), ("cierre", "última parte de un texto"), ("función de cierre", "frase para agradecer o despedirse al terminar"), ("revisión", "lectura de un texto para corregirlo")],
    worked=[
        W("Escribir una reflexión de cuatro partes", "Historia inventada de don Aníbal: «En Estero Dulce, la visita se presenta por su nombre». Escribe la reflexión.", ["Fuente: según don Aníbal, la visita se presenta por su nombre.", "Reflexión: yo pienso que así todos se conocen, porque cada uno dice quién es.", "Límite y cierre: no sé cómo se presenta en la lengua; agradezco con maururu si es rapa nui, o con la expresión que enseñe el educador."], "Según don Aníbal, la visita se presenta por su nombre. Yo pienso que así todos se conocen. No sé cómo se presenta en la lengua. Cierro agradeciendo con la expresión del educador."),
        W("Corregir una atribución", "Un niño escribe: «En los pueblos indígenas, al llegar se presentan por su nombre». ¿Qué falla?", ["Habla de todos los pueblos.", "La historia habla solo de Estero Dulce.", "Debe atribuir a don Aníbal."], "Falla porque generaliza: debe decir «según don Aníbal, en Estero Dulce…»."),
    ],
    mistakes=[
        M("Generalizar desde una sola historia.", "Una historia habla de una comunidad.", "Nombra la comunidad y la fuente."),
        M("Cerrar con una expresión en lengua que no me enseñaron.", "Podría estar mal.", "Usa una atestiguada o deja el espacio."),
    ],
    R=[
        ex("¿Cuántas partes tiene la reflexión atribuida de esta clase? Escribe el número.", "4", "Son fuente, reflexión, límite y cierre."),
        ex("¿Qué frase atribuye? A) «Según doña Silvia…» B) «Todos saben…»", "A", "Nombra a la fuente."),
        ex("¿Qué escribes si no tienes la expresión del educador? A) [expresión del educador] B) una inventada", "A", "Se deja el espacio."),
    ],
    C=[
        vf("la reflexión debe incluir una razón.", True, "Sin razón no tiene fundamento."),
        vf("una sola historia permite hablar de todos los pueblos.", False, "Una historia habla de una comunidad."),
        ab("¿Qué hago después de escribir mi reflexión?", "se la muestro a quien me enseña para que la revise", "la publico sin revisar", "La revisión evita errores."),
    ],
    A=[
        ex("Historia de doña Silvia: «Los niños saludan a los mayores». Completa: «Según doña Silvia, los niños…»", "Saludan a los mayores", "Repite el dato de la fuente."),
        ex("Clasifica en FUENTE, REFLEXIÓN o LÍMITE: a) según don Aníbal, la visita se presenta b) yo pienso que eso crea confianza c) no sé cómo se presenta en la lengua.", "a fuente, b reflexión, c límite", "Cada parte cumple un papel."),
        ex("Quieres cerrar tu reflexión agradeciendo en mapuzugun. ¿Qué expresión atestiguada usas? A) chaltumay B) mari mari", "A", "«Chaltumay» sirve para agradecer."),
    ],
    Z=[
        ex("Clara escribe «Yo pienso que es bonito» sin ninguna razón. ¿Qué le falta? A) una razón tomada de la historia B) más adjetivos", "A", "Una reflexión necesita razón."),
        ex("Un grupo cierra su reflexión con una frase que inventaron en lengua indígena. ¿Qué error cometen?", "Inventan una expresión", "Solo se usan expresiones atestiguadas o validadas."),
    ],
    D=[
        ex("Dos reflexiones sobre Monte Claro. Una: «Según doña Silvia, los niños saludan; yo pienso que eso muestra respeto». Otra: «Todos los niños indígenas saludan». ¿Cuál está mejor atribuida?", "La primera", "La segunda generaliza."),
        ex("No sabes cómo se dice «gracias» en tu lengua. ¿Qué haces? A) pregunto al educador B) uso cualquier palabra", "A", "Él enseña la lengua."),
    ],
    context=[ab("Para el diario mural del curso, debes escribir una reflexión sobre una historia. ¿Cómo la cierras?", "con una función social, usando una expresión validada", "con una frase inventada en lengua", "La validación evita errores.")],
    selfcheck=[
        ex("Escribe la fórmula de una reflexión atribuida con tus palabras.", "Según [fuente], …; yo pienso que… porque…; no sé…; cierro con [función]", "Une las cuatro partes."),
        vf("el educador puede corregir mi reflexión.", True, "Es parte de la revisión."),
        ex("¿Qué haces si dudas de cómo se escribe una expresión? A) pregunto al educador B) la cambio", "A", "Él valida la escritura."),
    ],
    task=T("Lee esta historia inventada de doña Silvia, de Monte Claro: «Cuando llega una familia nueva, los vecinos la saludan y le ofrecen un lugar en la mesa. Al despedirse, la familia agradece la acogida». Escribe una reflexión de cuatro partes: fuente, reflexión con «yo pienso que… porque…», límite y cierre con una función social (usa chaltumay o deja un espacio para el educador).",
           "Según doña Silvia, los vecinos saludan a la familia nueva y le ofrecen un lugar. Yo pienso que así se siente acogida porque la reciben. No sé cómo se saluda en la lengua. Cierro con: chaltumay, doña Silvia, por contarnos la historia.",
           ["incluye las cuatro partes", "atribuye a doña Silvia", "cierra con función social"], ["reflexión escrita"], ["generalizar", "inventar expresiones"],
           "Pedir que señale cada parte; valorar la atribución."),
    reinforce="Subraya con cuatro colores las cuatro partes de tu reflexión.",
    extend="Escribe una segunda reflexión sobre la historia de Estero Dulce con otra función social de cierre.",
)

L(
    LR1, 5, materials=MAT,
    use="Aprenderé a contrastar dos historias de comunidades distintas, viendo que las mismas funciones sociales se realizan de maneras diferentes, sin decir cuál es mejor. Sirve para dialogar entre culturas con respeto.",
    prior=["Sé escribir una reflexión atribuida.", "Sé contrastar con los mismos criterios."],
    explain=[
        "Las funciones sociales son universales: en todas las comunidades hay formas de saludar, agradecer, pedir permiso y despedirse. Pero las formas son distintas. En una comunidad se saluda con una frase; en otra, con un gesto; en otra, se pregunta primero por la familia. Contrastar nos ayuda a ver esa diversidad.",
        "Para contrastar dos historias usamos los mismos criterios: qué función aparece, cómo se realiza y quién la hace. Anotamos semejanzas y diferencias con expresiones como «en cambio» o «a diferencia de». Evitamos decir que una manera es más educada o más antigua, porque cada comunidad vive la suya con sentido.",
        "Además de las diferencias entre comunidades, hay diferencias dentro de una comunidad: no todas las personas hacen igual las funciones. Por eso escribimos «en esta historia» y no «siempre». Y si aparece una duda sobre cómo se hace en la lengua de tu comunidad, la anotamos para el educador o la educadora.",
    ],
    vocab=[("diversidad", "existencia de muchas formas distintas"), ("semejanza", "algo parecido entre dos cosas"), ("diferencia", "algo distinto entre dos cosas"), ("en cambio", "expresión que marca una diferencia"), ("jerarquizar", "decir que algo es mejor que otra cosa")],
    worked=[
        W("Contrastar dos historias", "Monte Claro: los niños saludan a los mayores al llegar. Estero Dulce: la visita se presenta por su nombre y le preguntan por el camino. Contrasta con el criterio «cómo se saluda o recibe».", ["En Monte Claro saludan los niños a los mayores.", "En Estero Dulce la visita se presenta y le preguntan por el camino.", "Semejanza: ambos reciben con atención. Diferencia: uno saluda y otro pregunta."], "Ambas reciben con atención; en una se saluda a los mayores y en la otra se pregunta por el camino. No se dice cuál es mejor."),
        W("Corregir un juicio", "Un compañero dice: «Preguntar por el camino es más educado que saludar». ¿Qué falla?", ["Dice «más educado», que es un orden.", "Las historias no comparan eso.", "Debe describir cada manera."], "Falla porque jerarquiza; debe describir cómo se recibe en cada comunidad."),
    ],
    mistakes=[
        M("Decir que una forma de saludar es más educada.", "Es un juicio sin fundamento.", "Describe cada forma."),
        M("Escribir «siempre» a partir de una historia.", "Una historia no cubre todos los casos.", "Escribe «en esta historia»."),
    ],
    R=[
        ex("En Monte Claro, ¿quiénes saludan a los mayores? A) los niños B) los visitantes", "A", "La historia lo dice."),
        ex("En Estero Dulce, ¿qué hace la visita al llegar? A) se presenta por su nombre B) canta", "A", "La historia lo dice."),
        ex("¿Qué expresión marca una diferencia? A) «en cambio» B) «además»", "A", "«En cambio» contrasta."),
    ],
    C=[
        vf("contrastar dos historias es decidir cuál comunidad es mejor.", False, "Contrastar es describir semejanzas y diferencias."),
        vf("las funciones sociales existen en todas las comunidades, aunque se hagan de formas distintas.", True, "Hay diversidad de formas."),
        ab("¿Qué palabra conviene usar al hablar de una historia?", "«en esta historia»", "«siempre»", "Una historia no cubre todos los casos."),
    ],
    A=[
        ex("Criterio «quién realiza la función». Monte Claro: los niños. Estero Dulce: la visita. ¿Qué diferencia hay? A) en una la hacen los niños y en la otra la visita B) no hay diferencia", "A", "Cambia quién la realiza."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) ambas comunidades reciben a las personas con atención b) una saluda y la otra pregunta por el camino.", "a semejanza, b diferencia", "La primera es común; la segunda, distinta."),
        ex("Tercera historia sin ficha. ¿Qué haces antes de compararla? A) pido la ficha con fuente y permiso B) la comparo igual", "A", "Sin ficha no se compara."),
    ],
    Z=[
        ex("Gonzalo escribe: «En todos los pueblos se saluda como en Monte Claro». ¿Qué error comete?", "Generaliza una historia a todos los pueblos", "Una historia no representa a todos."),
        ex("Valentina escribe que la forma de recibir de Estero Dulce es «más antigua». ¿Qué falla? A) no hay fuente que lo diga B) es muy corta", "A", "No se afirma lo que no está."),
    ],
    D=[
        ex("Tabla con el criterio «función que aparece»: Monte Claro, saludar y agradecer; Estero Dulce, presentarse y despedirse. ¿Qué afirmación es correcta? A) las cuatro funciones aparecen entre ambas historias B) solo aparece saludar", "A", "Entre ambas hay cuatro funciones."),
        arith("Monte Claro tiene 2 funciones y Estero Dulce, 2. ¿Cuántas funciones hay entre las dos historias?", "2+2", "Se suman las funciones de cada una.", " funciones"),
    ],
    context=[ab("En un encuentro escolar, una compañera dice que la forma de saludar de su comunidad es la única correcta. ¿Qué le dices?", "que cada comunidad saluda a su manera y todas tienen sentido", "que tiene razón", "No se jerarquizan las formas.")],
    selfcheck=[
        ex("Escribe una semejanza entre Monte Claro y Estero Dulce.", "Ambas reciben a las personas con atención", "Aparece en las dos historias."),
        vf("al contrastar usamos los mismos criterios con las dos historias.", True, "Así la comparación es justa."),
        ex("¿Qué haces con una duda sobre cómo se hace en tu lengua? A) la anoto para el educador B) la invento", "A", "Se consulta a quien sabe."),
    ],
    task=T("Contrasta estas dos historias inventadas. Monte Claro (doña Silvia): «Los niños saludan a los mayores al llegar y agradecen la comida al irse». Estero Dulce (don Aníbal): «La visita se presenta por su nombre y le preguntan por el camino; al irse, la invitan a volver». Haz una tabla con tres criterios: función que aparece, cómo se realiza y quién la hace. Escribe una semejanza y una diferencia sin «mejor» ni «más educado».",
           "Funciones: M saludar y agradecer; E presentarse y despedirse. Cómo: M saludan y agradecen; E se presentan y preguntan por el camino. Quién: M los niños; E la visita. Semejanza: en ambas se recibe y se despide con atención. Diferencia: en M saludan los niños; en E se presenta la visita.",
           ["tabla con tres criterios", "semejanza y diferencia", "no jerarquiza"], ["tabla", "dos frases"], ["usar «mejor»", "generalizar"],
           "Pedir que muestre cada dato en las historias; valorar que no ordene de mejor a peor."),
    reinforce="Subraya con verde las semejanzas y con azul las diferencias en tu tabla.",
    extend="Explica con un ejemplo por qué la misma función social puede hacerse de formas distintas.",
)

# ============================================================ OA LR02 · Exposición oral con vocabulario pertinente
L(
    LR2, 1, materials=MAT,
    use="Aprenderé a preparar una exposición oral situando el tema y a reservar un lugar para vocabulario en lengua indígena que enseñe el educador. Sirve para analizar aspectos de una cultura sin hablar por otros.",
    prior=["Sé situar un tema con una ficha.", "Sé que el vocabulario en lengua lo entrega el educador."],
    explain=[
        "Una exposición oral de análisis explica un tema separándolo en partes. Los aspectos socioculturales se refieren a la vida en comunidad: cómo se organizan las tareas, cómo se comparten los alimentos, cómo se cuida el lugar. Los aspectos espirituales se refieren a lo que la comunidad considera sagrado; de esos solo se expone lo que la comunidad autoriza.",
        "Incorporar vocabulario pertinente significa usar, en la exposición, palabras de la lengua indígena que vienen al caso: un saludo al inicio, un agradecimiento al cierre y los términos que el educador o la educadora enseñe sobre el tema. «Pertinente» quiere decir que corresponde a lo que se está hablando y que fue validado.",
        "Antes de exponer, situamos el tema con una ficha: comunidad, tema, fuente, permiso y límite. Luego hacemos una lista de vocabulario con tres columnas: palabra, significado en castellano y quién la enseñó. Las únicas palabras atestiguadas en este cuaderno son «mari mari», «chaltumay», «iorana» y «maururu».",
    ],
    vocab=[("pertinente", "que corresponde a lo que se está hablando"), ("vocabulario", "conjunto de palabras que se usan en un tema"), ("glosario", "lista de palabras con su significado"), ("aspecto sociocultural", "parte de la vida en común de una comunidad"), ("exposición oral", "presentación en que una persona explica un tema")],
    worked=[
        W("Situar un tema", "Ficha inventada. Comunidad: Campo Abierto (no es un pueblo real). Tema: cómo se organizan las tareas para la cosecha. Fuente: doña Isabel. Permiso: sí. Límite: no se exponen los nombres de las familias. ¿De qué se puede hablar?", ["El tema es la organización de tareas para la cosecha.", "La fuente es doña Isabel y dio permiso.", "No se dicen los nombres de las familias."], "Se puede exponer cómo se organizan las tareas de la cosecha, sin nombrar a las familias."),
        W("Armar un glosario", "Vas a exponer con las expresiones mari mari y chaltumay. Arma el glosario con tres columnas.", ["Palabra: mari mari; significado: saludo; quién la enseñó: el cuaderno y el educador.", "Palabra: chaltumay; significado: gracias.", "Las demás palabras las dictará el educador."], "Glosario: mari mari = saludo; chaltumay = gracias; más palabras: las dicta el educador."),
    ],
    mistakes=[
        M("Poner palabras en lengua porque «quedan bien».", "Deben ser pertinentes y validadas.", "Usa solo las que enseñe el educador."),
        M("Exponer los nombres de las familias que la ficha reserva.", "Se rompe el límite.", "Hablarás de «las familias» sin nombrarlas."),
    ],
    R=[
        ex("Ficha: «Comunidad: Pasto Alto. Tema: la esquila. Fuente: don Gaspar.» ¿Cuál es el tema?", "La esquila", "La ficha lo dice."),
        ex("¿Qué es un glosario? A) una lista de palabras con su significado B) un mapa", "A", "Es una lista con significados."),
        ex("¿Qué palabra de este cuaderno sirve para saludar en mapuzugun?", "Mari mari", "Es un saludo atestiguado."),
    ],
    C=[
        vf("«pertinente» significa que corresponde a lo que se habla y fue validado.", True, "Esa es la idea."),
        vf("en una exposición se puede usar cualquier palabra en lengua si suena bien.", False, "Deben ser palabras validadas."),
        ab("¿Quién enseña el vocabulario pertinente?", "el educador o la educadora tradicional", "un compañero que lo busca", "Quien enseña la lengua lo entrega."),
    ],
    A=[
        ex("Clasifica en SOCIOCULTURAL o ESPIRITUAL: a) cómo se reparten las tareas de la cosecha b) lo que la comunidad considera sagrado.", "a sociocultural, b espiritual", "La primera es organización; la segunda, lo sagrado."),
        ex("Glosario: ¿qué columna falta? Palabra | Significado | ______ A) quién la enseñó B) el color", "A", "Se anota la fuente de cada palabra."),
        ex("La ficha dice «Límite: no se exponen los lugares de respeto». ¿Los mencionas? Sí o No.", "No", "El límite lo prohíbe."),
    ],
    Z=[
        ex("Tomás dice: «Usaré palabras en lengua que vi en un video». ¿Qué le falta? A) validarlas con el educador B) más videos", "A", "Un video no valida las palabras."),
        ex("Sara va a exponer sobre un tema que la ficha no autoriza. ¿Qué hace? A) cambia de tema o pide permiso B) expone igual", "A", "Sin permiso no se expone."),
    ],
    D=[
        ex("Dos fichas: una con fuente y permiso; otra sin permiso. ¿Con cuál preparas ahora la exposición?", "La que tiene fuente y permiso", "La otra se detiene."),
        arith("Tu glosario tiene 4 palabras. El educador agrega 3 más. ¿Cuántas palabras tiene ahora?", "4+3", "Se suman las palabras nuevas.", " palabras"),
    ],
    context=[ab("Invitaste a un familiar para escuchar tu exposición sobre la cosecha en la comunidad. ¿Qué haces con el glosario?", "lo reviso con el educador antes", "lo reparto sin revisar", "El vocabulario se valida antes de exponer.")],
    selfcheck=[
        ex("Nombra las tres columnas de un glosario.", "Palabra, significado y quién la enseñó", "Son las columnas de la clase."),
        vf("de los aspectos espirituales solo se expone lo que la comunidad autoriza.", True, "Se respeta lo reservado."),
        ex("¿Qué saludo atestiguado hay en rapa nui? A) iorana B) chaltumay", "A", "«Iorana» saluda en rapa nui."),
    ],
    task=T("Lee esta ficha inventada: Comunidad: Campo Abierto. Tema: cómo se organizan las tareas de la cosecha. Fuente: doña Isabel, quien cuenta que cada familia lleva sus canastos, que los mayores indican el orden de la cosecha y que los jóvenes ayudan a cargar. Permiso: sí. Límite: no se exponen los nombres de las familias. Escribe el plan de una exposición de 2 minutos con tres partes y un glosario de tres filas (mari mari, chaltumay y una fila [palabra del educador]).",
           "Partes: 1) qué es la cosecha comunitaria; 2) cómo se organizan (canastos, orden de los mayores, ayuda de los jóvenes); 3) qué significa para la comunidad, según doña Isabel. Glosario: mari mari = saludo; chaltumay = gracias; [palabra del educador] = [significado que él dicte]. No digo los nombres de las familias.",
           ["tres partes del análisis", "glosario con tres filas", "respeta el límite"], ["plan escrito", "glosario"], ["inventar palabras", "nombrar familias"],
           "Pedir que señale cada parte en la ficha; valorar el glosario."),
    reinforce="Subraya en la ficha de Campo Abierto el tema, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica por qué el vocabulario en lengua debe ser validado antes de una exposición.",
)

L(
    LR2, 2, materials=MAT,
    use="Aprenderé a escuchar una exposición y anotar el vocabulario en lengua que aparece, su significado y quién lo enseñó, respetando lo reservado. Sirve para incorporar palabras con cuidado.",
    prior=["Sé armar un glosario.", "Sé tomar notas con palabras clave."],
    explain=[
        "Al escuchar una exposición, anotamos palabras clave en castellano y, si aparece una palabra en lengua indígena, la anotamos aparte en un glosario de escucha. Escribimos la palabra tal como la dice el educador o la educadora, su significado según quien expone y quién la enseñó. Si dudamos de cómo se escribe, preguntamos.",
        "Para no perder el hilo, usamos tres tipos de nota: lo que dijo la persona, lo que entendí yo y lo que no se explicó. Cuando alguien dice «esta parte es solo de la comunidad», anotamos «reservado» y no insistimos. Las preguntas se hacen al final y solo sobre lo que sí se contó.",
        "Una buena nota de escucha es breve: tres o cuatro palabras clave, el glosario de palabras en lengua y una pregunta. Con ella podemos hacer un resumen oral atribuido, por ejemplo: «Según doña Isabel, cada familia lleva sus canastos; usó la palabra chaltumay para agradecer».",
    ],
    vocab=[("glosario de escucha", "lista de palabras en lengua que aparecen en lo que escuchamos"), ("palabra clave", "palabra que sostiene la idea principal"), ("reservado", "que la comunidad prefiere no compartir"), ("resumen oral", "versión corta, dicha en voz alta, de lo que escuché"), ("atribuir", "decir de quién viene un dato")],
    worked=[
        W("Tomar notas con glosario", "Exposición inventada de doña Isabel, de Campo Abierto, leída por una persona adulta: «Mari mari. Hoy les cuento cómo se organizan las cosechas. Cada familia lleva sus canastos y los mayores indican el orden. Hay una reunión de cierre que solo es de la comunidad. Chaltumay por escuchar». Anota las palabras clave, el glosario y lo reservado.", ["Claves: familias, canastos, mayores, orden.", "Glosario: mari mari (saludo), chaltumay (gracias).", "Reservado: la reunión de cierre."], "Claves: familias, canastos, mayores, orden. Glosario: mari mari, chaltumay. Reservado: la reunión de cierre."),
        W("Hacer una pregunta adecuada", "Con esas notas, escribe una pregunta que no insista en lo reservado.", ["Elijo algo que sí se contó: el orden de la cosecha.", "Pregunto por el cómo.", "Pregunta: ¿cómo deciden los mayores el orden?"], "«¿Cómo deciden los mayores el orden de la cosecha?»"),
    ],
    mistakes=[
        M("Anotar palabras en lengua sin preguntar cómo se escriben.", "Puede haber errores.", "Pregunta al educador o a quien expone."),
        M("Insistir en la parte reservada.", "No respeta el límite.", "Pregunta por lo contado."),
    ],
    R=[
        ex("En la exposición de doña Isabel, ¿qué lleva cada familia? A) canastos B) cuadernos", "A", "La exposición lo dice."),
        ex("¿Qué indican los mayores? A) el orden de la cosecha B) el menú", "A", "La exposición lo dice."),
        ex("¿Qué palabra de la exposición significa gracias en mapuzugun?", "Chaltumay", "Es el agradecimiento atestiguado."),
    ],
    C=[
        vf("si la persona dice que una parte es reservada, se anota «reservado» y no se insiste.", True, "Se respeta el límite."),
        vf("las palabras en lengua se escriben como a uno le parece.", False, "Se escriben como indica el educador."),
        ab("¿Cuándo se hacen las preguntas?", "al final y sobre lo que sí se contó", "en medio, sobre lo reservado", "Así se respeta el turno y el límite."),
    ],
    A=[
        ex("Exposición leída: «Cada familia lleva sus canastos; los jóvenes ayudan a cargar». ¿Cuál es la idea principal? A) La cosecha se hace entre todos B) La cosecha es difícil de explicar en un día", "A", "Resume sin agregar datos."),
        ex("Clasifica en CLAVE o GLOSARIO: a) canastos b) mari mari.", "a clave, b glosario", "«Canastos» es palabra clave; «mari mari» es palabra en lengua."),
        ex("Exposición leída: «Hay una reunión de cierre solo de la comunidad». ¿Qué anotas? A) reservado: la reunión de cierre B) la hora de la reunión", "A", "La exposición no da la hora y la reserva."),
    ],
    Z=[
        ex("Pía anota «chaltumay = hola». ¿Qué error comete?", "Confunde el agradecimiento con un saludo", "«Chaltumay» significa gracias."),
        ex("Andrés pregunta tres veces qué se hace en la reunión de cierre. ¿Qué regla rompe? A) respetar los límites B) usar palabras clave", "A", "Insiste en lo reservado."),
    ],
    D=[
        ex("Tus notas dicen: claves (familias, canastos, orden), glosario (mari mari), reservado (reunión de cierre). ¿Qué pregunta es adecuada? A) ¿Cómo se turnan las familias para llevar canastos? B) ¿Qué hacen en la reunión de cierre?", "A", "La B pregunta por lo reservado."),
        arith("Anotaste 4 palabras clave, 2 palabras de glosario y 1 reservado. ¿Cuántas anotaciones tienes en total?", "4+2+1", "Se suman los tres tipos de notas.", " anotaciones"),
    ],
    context=[ab("Un familiar te cuenta una historia de su comunidad y usa una palabra en lengua. ¿Qué haces?", "pregunto cómo se escribe y qué significa, y anoto quién la enseñó", "la escribo como suene", "Se respeta cómo la escribe la fuente.")],
    selfcheck=[
        ex("Nombra los tres tipos de nota de escucha.", "Lo que dijo la persona, lo que entendí yo y lo que no se explicó", "Son las tres notas."),
        vf("el glosario de escucha anota quién enseñó cada palabra.", True, "Se atribuye la fuente."),
        ex("¿Qué escribes de una palabra en lengua si dudas del significado? A) pregunta pendiente B) un significado inventado", "A", "No se inventa."),
    ],
    task=T("Pide a una persona de tu casa que te lea este texto inventado de don Gaspar, de Pasto Alto: «Mari mari. Hoy hablaré de cómo se esquila. Cada familia trae sus tijeras de esquilar y los mayores indican qué oveja va primero. Hay una despedida que solo hacemos entre nosotros. Chaltumay por escucharme». Mientras escuchas, anota palabras clave, un glosario de escucha, lo reservado y una pregunta adecuada.",
           "Claves: familias, tijeras, mayores, oveja. Glosario: mari mari (saludo), chaltumay (gracias). Reservado: la despedida. Pregunta: ¿cómo deciden qué oveja va primero?",
           ["anota claves y glosario", "identifica lo reservado", "pregunta por lo contado"], ["notas escritas", "pregunta"], ["insistir en lo reservado", "inventar significados"],
           "Pedir que muestre dónde apareció cada dato; valorar que respete lo reservado."),
    reinforce="Vuelve a escuchar el texto y subraya con un color las palabras clave.",
    extend="Escribe un resumen oral de tres frases con «Según don Gaspar…».",
)

L(
    LR2, 3, materials=MAT,
    use="Aprenderé a relacionar cada palabra del vocabulario en lengua con la función que cumple en una exposición (abrir, nombrar, agradecer, cerrar). Sirve para incorporar palabras de manera pertinente.",
    prior=["Sé hacer un glosario.", "Sé escuchar y anotar vocabulario."],
    explain=[
        "Una palabra en lengua indígena puede cumplir distintas funciones dentro de una exposición. Un saludo abre y crea cercanía; un agradecimiento cierra y reconoce; un término propio del tema nombra algo que en castellano no tiene exactamente el mismo sentido. Para usar bien cada palabra, preguntamos: ¿en qué momento la digo y para qué?",
        "Algunas palabras tienen un significado general («mari mari» es un saludo) y otras dependen del contexto de la comunidad. Por eso, el significado de los términos del tema lo da el educador o la educadora, con ejemplos. Nunca decimos «significa exactamente lo mismo que en castellano» sin saberlo, porque el sentido puede cambiar.",
        "Para planificar, hacemos una tabla con tres columnas: palabra, función y momento de la exposición. Por ejemplo: mari mari, saludar, inicio; chaltumay, agradecer, cierre. Si hay una palabra del tema, la ponemos en el desarrollo con una breve explicación en castellano.",
    ],
    vocab=[("función de una palabra", "lo que hace una palabra dentro de una exposición"), ("momento", "parte de la exposición donde se usa algo"), ("término", "palabra propia de un tema"), ("sentido", "significado que una palabra tiene en un contexto"), ("explicación breve", "frase en castellano que aclara una palabra")],
    worked=[
        W("Completar la tabla", "Palabras: mari mari y chaltumay. Completa función y momento.", ["«Mari mari» saluda y va al inicio.", "«Chaltumay» agradece y va al cierre.", "Ambas se explican en castellano."], "Mari mari: saludar, inicio. Chaltumay: agradecer, cierre."),
        W("Explicar un término del tema", "El educador te dicta una palabra [palabra del educador] para nombrar un instrumento de cosecha. ¿Cómo la incorporas?", ["La pongo en el desarrollo.", "Escribo una explicación breve en castellano.", "Pido que el educador valide el significado."], "La incorporo en el desarrollo con una explicación breve y validada."),
    ],
    mistakes=[
        M("Decir que una palabra en lengua «es igual» a una de castellano sin consultar.", "El sentido puede cambiar.", "Pregunta qué significa en la comunidad."),
        M("Ubicar el agradecimiento al principio.", "Se pierde la función de cierre.", "Pon el agradecimiento al final."),
    ],
    R=[
        ex("¿En qué momento va «mari mari»? A) inicio B) cierre", "A", "Es un saludo."),
        ex("¿En qué momento va «chaltumay»? A) cierre B) inicio", "A", "Agradece al terminar."),
        ex("¿Qué función cumple «iorana»? A) saludar B) agradecer", "A", "Es un saludo en rapa nui."),
    ],
    C=[
        vf("una palabra en lengua puede nombrar algo que no significa exactamente lo mismo en castellano.", True, "El sentido puede cambiar."),
        vf("«chaltumay» se usa al inicio como saludo.", False, "Agradece, no saluda."),
        ab("¿Quién da el significado de un término del tema?", "el educador o la educadora", "un diccionario inventado", "Conoce el sentido en la comunidad."),
    ],
    A=[
        ex("Completa la tabla: palabra «maururu», función ______, momento cierre. A) agradecer B) saludar", "A", "«Maururu» es gracias en rapa nui."),
        ex("Une función y momento: a) saludar b) agradecer. Escribe INICIO o CIERRE para cada una.", "a inicio, b cierre", "Se saluda al comenzar y se agradece al terminar."),
        ex("Quieres usar una palabra del tema sin saber su significado. ¿Qué haces? A) pregunto al educador antes B) la uso igual", "A", "Se valida el significado."),
    ],
    Z=[
        ex("Camilo pone «maururu» al inicio de su exposición sobre rapa nui para saludar. ¿Qué error comete?", "Usa un agradecimiento como saludo", "«Maururu» es gracias."),
        ex("Marta dice que una palabra en lengua «es lo mismo que en castellano» porque tradujo con una herramienta. ¿Qué falla? A) no validó el sentido con el educador B) no la subrayó", "A", "El sentido lo explica el educador."),
    ],
    D=[
        ex("Tabla de tu exposición: inicio (mari mari), desarrollo ([palabra del educador]), cierre (chaltumay). ¿Cuántas palabras tiene la tabla?", "3", "Hay tres filas: tres palabras."),
        ex("El educador dice que una palabra tiene dos sentidos según el contexto. ¿Qué haces? A) pregunto en qué contexto uso cada uno B) elijo uno al azar", "A", "El contexto define el sentido."),
    ],
    context=[ab("Vas a presentar un cartel con tres palabras en lengua. ¿Qué agregas junto a cada palabra?", "su significado y quién la enseñó", "su color favorito", "Se atribuye y se explica.")],
    selfcheck=[
        ex("Nombra una palabra de saludo y una de agradecimiento de este cuaderno.", "Saludo: mari mari o iorana; agradecimiento: chaltumay o maururu", "Son expresiones atestiguadas del cuaderno."),
        vf("una tabla de planificación tiene palabra, función y momento.", True, "Esas son sus columnas."),
        ex("¿Quién valida el significado de un término del tema? A) el educador B) el compañero", "A", "Él conoce el sentido."),
    ],
    task=T("Planifica el vocabulario de una exposición de 2 minutos sobre «cómo se organiza una cosecha comunitaria» (tema inventado de Campo Abierto). Haz una tabla con cuatro filas: mari mari (saludo), un término del tema que dictará el educador, chaltumay (agradecimiento) y un espacio libre [palabra del educador]. Anota la función y el momento de cada una. Escribe una frase en castellano que explique el término del tema.",
           "mari mari / saludar / inicio. [término del tema] / nombrar un elemento de la cosecha / desarrollo. [palabra del educador] / según lo dicte / desarrollo. chaltumay / agradecer / cierre. Explicación: [término] es lo que usamos para nombrar un elemento de la cosecha, según el educador.",
           ["tabla con función y momento", "explicación breve", "no inventa palabras"], ["tabla", "frase explicativa"], ["inventar términos", "confundir funciones"],
           "Pedir que explique por qué cada palabra va en su momento; valorar que deje espacios."),
    reinforce="Ordena en una línea de tiempo el inicio, el desarrollo y el cierre de una exposición con sus palabras.",
    extend="Escribe una explicación breve en castellano para un término que no conozcas, pidiendo al educador que la revise.",
)

L(
    LR2, 4, materials=MAT,
    use="Aprenderé a escribir el guion de una exposición oral con vocabulario en lengua, atribuyendo cada dato y marcando énfasis y pausas. Sirve para exponer con claridad y respeto.",
    prior=["Sé relacionar palabras con su función.", "Sé distinguir inicio, desarrollo y cierre."],
    explain=[
        "El guion de una exposición contiene lo que diré en cada momento. En el inicio: saludo en lengua validado, mi nombre y el tema. En el desarrollo: dos o tres datos atribuidos («según doña Isabel…») y, si corresponde, un término del tema con su explicación. En el cierre: resumen, límites y agradecimiento en lengua validado.",
        "Marcamos el énfasis con mayúsculas en la palabra que queremos destacar y las pausas con tres puntos. El énfasis ayuda a que el público recuerde la idea más importante. También anotamos qué palabra en lengua pronunciaré y la practico con el educador o la educadora, porque la pronunciación se aprende escuchando a quien habla la lengua.",
        "Al final del guion escribimos los límites: «No sé cómo se organiza el orden de los turnos» o «no puedo contar la reunión de cierre porque es reservada». Los límites muestran lo que no se afirma y evitan que inventemos.",
    ],
    vocab=[("guion", "texto que planifica lo que se dirá"), ("énfasis", "destacar con la voz una palabra importante"), ("pausa", "silencio breve para que se entienda mejor"), ("pronunciación", "manera de decir una palabra"), ("límite", "lo que no sé o no puedo contar")],
    worked=[
        W("Armar el guion", "Datos: tema, cosecha en Campo Abierto; fuente, doña Isabel; dato, los mayores indican el orden; palabras, mari mari y chaltumay. Arma el guion de tres frases.", ["Inicio: mari mari, hoy hablaré de la cosecha en Campo Abierto.", "Desarrollo: según doña Isabel, los mayores indican el ORDEN (…) de la cosecha.", "Cierre: no sé cómo deciden el orden. Chaltumay por escucharme."], "Inicio con mari mari, desarrollo atribuido con énfasis y cierre con límites y chaltumay."),
        W("Marcar énfasis y pausa", "Frase: «Cada familia lleva sus canastos». Marca el énfasis y una pausa.", ["La idea clave es «canastos».", "La pongo en mayúsculas.", "Agrego una pausa antes."], "«Cada familia lleva sus (…) CANASTOS»."),
    ],
    mistakes=[
        M("Dar un dato sin decir de quién viene.", "No se sabe la fuente.", "Usa «según…»."),
        M("Practicar la pronunciación solo con un video.", "No se valida.", "Practica con el educador."),
    ],
    R=[
        ex("¿Dónde va el saludo en lengua? A) en el inicio B) en el cierre", "A", "Se abre saludando."),
        ex("¿Cómo marcas el énfasis en el guion? A) con mayúsculas B) con colores borrados", "A", "Así se destaca la palabra."),
        ex("¿Qué se escribe al final del guion? A) los límites B) más datos inventados", "A", "Los límites declaran lo que no se afirma."),
    ],
    C=[
        vf("el guion debe atribuir cada dato a su fuente.", True, "Así se distingue de quién viene."),
        vf("los límites sobran en un guion de exposición.", False, "Evitan que se invente."),
        ab("¿Con quién practicas la pronunciación de las palabras en lengua?", "con el educador o la educadora", "con una grabación al azar", "Quien habla la lengua puede corregirte."),
    ],
    A=[
        ex("Completa con «según»: «______ don Gaspar, los mayores indican qué oveja va primero». Escribe la palabra que falta.", "Según", "Atribuye el dato."),
        ex("Frase: «La esquila se hace en grupo». Marca el énfasis en la palabra clave. A) La esquila se hace en GRUPO B) LA esquila se hace en grupo", "A", "La idea importante es «en grupo»."),
        ex("Ordena el guion con letras: a) cierre con chaltumay b) inicio con mari mari c) dato atribuido. Escribe el orden.", "b, c, a", "Inicio, desarrollo y cierre."),
    ],
    Z=[
        ex("Pablo escribe el guion sin límites. ¿Qué podría pasar? A) afirmar cosas que no sabe B) hablar más rápido", "A", "Los límites previenen inventar."),
        ex("Una niña pronuncia «chaltumay» de una manera que escuchó en un video. ¿Qué falta? A) validar la pronunciación con el educador B) cambiar el video", "A", "El educador valida."),
    ],
    D=[
        arith("El guion dura 2 minutos. Inicio 20 segundos, desarrollo 80 segundos. ¿Cuántos segundos quedan para el cierre? (1 minuto = 60 segundos)", "2*60-20-80", "Se resta inicio y desarrollo del total.", " segundos"),
        ex("Tienes cuatro datos y solo caben tres en el tiempo. ¿Qué haces? A) elijo los más importantes B) hablo más rápido", "A", "Priorizar mantiene la claridad."),
    ],
    context=[ab("Tu curso presentará una exposición ante familias. Un compañero quiere agregar una palabra en lengua de último minuto. ¿Qué haces?", "pido que el educador la valide antes", "la agrego igual", "Toda palabra en lengua se valida antes.")],
    selfcheck=[
        ex("Nombra las tres partes del guion.", "Inicio, desarrollo y cierre", "Son las tres partes."),
        vf("el énfasis se usa en una o dos palabras clave por frase importante.", True, "Si todo se destaca, nada se destaca."),
        ex("¿Qué haces con una palabra en lengua que no sabes decir? A) la practico con el educador B) la invento", "A", "Él enseña la pronunciación."),
    ],
    task=T("Con este texto inventado de doña Isabel, de Campo Abierto: «Cada familia lleva sus canastos. Los mayores indican el orden de la cosecha. Los jóvenes ayudan a cargar». Escribe el guion de una exposición de 1 minuto con inicio (mari mari), desarrollo (dos datos con «según doña Isabel…», con una palabra en mayúsculas y una pausa (…)) y cierre (límite y chaltumay). Ensaya en voz alta con una persona de tu casa.",
           "Inicio: Mari mari, hoy hablaré de la cosecha en Campo Abierto. Desarrollo: Según doña Isabel, cada familia lleva sus CANASTOS (…) y los mayores indican el orden. Cierre: No sé cómo deciden el orden. Chaltumay por escucharme.",
           ["tiene inicio, desarrollo y cierre", "atribuye a doña Isabel", "marca énfasis, pausa y límites"], ["guion escrito", "ensayo"], ["omitir fuente", "destacar todo"],
           "Pedir que lea en voz alta; valorar la atribución."),
    reinforce="Marca con tres colores el inicio, el desarrollo y el cierre de tu guion.",
    extend="Escribe un segundo cierre distinto con otro límite.",
)

L(
    LR2, 5, materials=MAT,
    use="Aprenderé a dialogar a partir de dos exposiciones de comunidades distintas usando vocabulario pertinente, preguntando para comprender y contrastando sin jerarquizar. Sirve para conversar con respeto entre culturas.",
    prior=["Sé armar un guion con vocabulario.", "Sé contrastar con los mismos criterios."],
    explain=[
        "En un diálogo respetuoso cada persona escucha, responde y pregunta. Se pide la palabra, se espera el turno y se pregunta para comprender, no para corregir. Cuando usamos vocabulario en lengua indígena en el diálogo, lo hacemos solo con las palabras que conocemos bien, como un saludo para abrir o un agradecimiento para cerrar.",
        "Para contrastar dos exposiciones usamos criterios iguales: qué tarea se explica, quién participa y qué vocabulario se usó. Anotamos semejanzas y diferencias con frases como «a diferencia de». No decimos que una exposición es mejor que otra: cada una cuenta una comunidad distinta.",
        "Al final del diálogo resumimos con atribución: «Según doña Isabel, de Campo Abierto…; según don Gaspar, de Pasto Alto…». Las dudas que nadie puede resolver se anotan para el educador o la educadora. Cerramos con un agradecimiento en la lengua que se haya validado.",
    ],
    vocab=[("turno", "momento que le corresponde hablar a cada persona"), ("pregunta para comprender", "pregunta que busca entender, no corregir"), ("criterio", "punto igual para comparar"), ("a diferencia de", "expresión que marca diferencia sin ordenar"), ("resumen atribuido", "resumen que dice de quién viene cada dato")],
    worked=[
        W("Preguntar para comprender", "Exposición A (Campo Abierto): «Los mayores indican el orden de la cosecha». Exposición B (Pasto Alto): «Cada familia trae sus tijeras». Escribe una pregunta para comprender sobre A.", ["Elijo un dato contado: los mayores indican el orden.", "Pregunto por el cómo.", "Pregunta: ¿cómo deciden los mayores quién empieza?"], "«¿Cómo deciden los mayores quién empieza?»"),
        W("Contrastar sin jerarquizar", "Contrasta A y B con el criterio «quién participa».", ["A: familias, mayores y jóvenes.", "B: familias.", "Semejanza: participan familias. Diferencia: en A también los mayores indican."], "Ambas incluyen familias; en A, además, los mayores indican el orden. No se dice cuál es mejor."),
    ],
    mistakes=[
        M("Interrumpir para corregir una palabra.", "Rompe el turno y la confianza.", "Anota la duda y pregúntala después."),
        M("Preguntar por lo reservado.", "No respeta el límite.", "Pregunta por lo que sí se contó."),
    ],
    R=[
        ex("En un diálogo, ¿cuándo hablas? A) en tu turno B) cuando quiero", "A", "Se respeta el turno."),
        ex("¿Qué expresión marca una diferencia? A) «a diferencia de» B) «es mejor que»", "A", "Describe sin ordenar."),
        ex("¿Qué usas para abrir un diálogo con una palabra atestiguada en mapuzugun? A) mari mari B) chaltumay", "A", "«Mari mari» saluda."),
    ],
    C=[
        vf("preguntar para comprender es lo mismo que preguntar para corregir.", False, "Una busca entender; la otra, mostrar un error."),
        vf("en un diálogo se usan solo palabras en lengua que conozco bien.", True, "Se evita equivocarse."),
        ab("¿Qué haces con una duda que nadie puede resolver?", "la anoto para el educador", "la invento", "Se consulta a quien sabe."),
    ],
    A=[
        ex("Exposición C (Roca Blanca): «Los jóvenes cargan los sacos». Elige una pregunta para comprender. A) ¿Cómo se organizan los jóvenes para cargarlos? B) ¿Por qué no ayudan los mayores?", "A", "La B juzga."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) en ambas hay familias que participan b) en una los mayores indican el orden.", "a semejanza, b diferencia", "La primera es común; la segunda es particular."),
        ex("Resume con «según»: Campo Abierto, los mayores indican; Pasto Alto, cada familia trae sus tijeras. Completa: «Según don Gaspar, cada familia…»", "Trae sus tijeras", "Repite lo que dice la exposición B."),
    ],
    Z=[
        ex("Pablo dice: «Campo Abierto es más organizado que Pasto Alto». ¿Qué error comete?", "Jerarquiza sin fundamento", "Las exposiciones no comparan eso."),
        ex("Elena interrumpe para corregir cómo dijeron «mari mari». ¿Qué falla? A) rompe el turno; debía anotar la duda B) usó mal el saludo", "A", "Las dudas se consultan después."),
    ],
    D=[
        ex("Dos resúmenes: Uno: «Según doña Isabel, hay un orden; según don Gaspar, cada familia trae tijeras». Otro: «Ambas comunidades son iguales». ¿Cuál reconoce cada voz?", "El primero", "El segundo mezcla y generaliza."),
        arith("En el diálogo hablan 5 personas y cada una interviene 3 veces. ¿Cuántas intervenciones hay en total?", "5*3", "Se multiplican personas por intervenciones.", " intervenciones"),
    ],
    context=[ab("En un diálogo escolar, una compañera propone elegir cuál exposición fue mejor. ¿Qué respondes?", "que dialogamos para comprender y no para competir", "que votemos", "Dialogar no es competir.")],
    selfcheck=[
        ex("Escribe una regla del diálogo respetuoso.", "No interrumpir y esperar el turno", "Es una regla de conversación."),
        vf("el resumen final del diálogo atribuye cada voz.", True, "Reconoce a cada fuente."),
        ex("¿Con qué cierras el diálogo si tienes una expresión validada? A) con un agradecimiento en lengua B) con una crítica", "A", "El agradecimiento cierra con respeto."),
    ],
    task=T("Dialoga con una persona de tu casa a partir de estas dos mini exposiciones inventadas. A (Campo Abierto, doña Isabel): «Cada familia lleva sus canastos y los mayores indican el orden». B (Pasto Alto, don Gaspar): «Cada familia trae sus tijeras y los mayores indican qué oveja va primero». Escribe tres preguntas para comprender (dos para A, una para B), una semejanza y una diferencia con los mismos criterios, y un resumen con «Según…» que termine con chaltumay.",
           "Preguntas: ¿cómo avisan el orden?; ¿cómo saben cuándo termina?; ¿cómo deciden qué oveja va primero? Semejanza: en ambas los mayores indican. Diferencia: una es cosecha y otra, esquila. Resumen: Según doña Isabel, los mayores indican el orden; según don Gaspar, indican qué oveja va primero. Chaltumay.",
           ["formula preguntas para comprender", "compara con criterios iguales", "resume con atribución"], ["tres preguntas", "semejanza y diferencia", "resumen"], ["preguntar para corregir", "jerarquizar"],
           "Pedir que explique por qué cada pregunta busca comprender; valorar el resumen atribuido."),
    reinforce="Cambia dos preguntas que buscan corregir por preguntas que buscan comprender.",
    extend="Escribe cinco frases para pedir la palabra y esperar tu turno con respeto.",
)

L(
    LR2, 6, materials=MAT,
    use="Aprenderé a ensayar y presentar una exposición con vocabulario en lengua, con criterios claros y con validación del educador o de la comunidad. Sirve para exponer con calidad y respeto.",
    prior=["Sé armar un guion con vocabulario.", "Sé dialogar sin jerarquizar."],
    explain=[
        "Antes de presentar, ensayamos con una persona que nos escuche. Revisamos cinco criterios, cada uno de 0 a 2 puntos: claridad, volumen y ritmo, atribución, vocabulario en lengua validado y respeto de los límites. El máximo es 10 puntos. El puntaje no es una nota, sino una ayuda para saber qué mejorar.",
        "La retroalimentación se da con respeto: primero lo que estuvo bien, luego lo que se puede mejorar y un ejemplo. Después corregimos el guion y ensayamos de nuevo. Si hay una palabra en lengua que se pronunció distinto, el educador o la educadora nos muestra cómo se dice y practicamos.",
        "Antes de la presentación final, el educador valida el vocabulario y la comunidad puede revisar lo que se dice sobre su cultura. Si hay algo que no debe mostrarse, se quita. Al terminar, agradecemos a la fuente y a quienes ayudaron, y hacemos la devolución mostrando la versión final.",
    ],
    vocab=[("ensayo", "práctica previa de una presentación"), ("retroalimentación", "ayuda que dice qué estuvo bien y qué mejorar"), ("puntaje", "número que resume cuántos criterios se cumplen"), ("validación", "revisión de quien sabe para confirmar que es correcto"), ("devolución", "mostrar la versión final a la fuente")],
    worked=[
        W("Sumar puntos", "Un ensayo obtuvo: claridad 2, volumen y ritmo 1, atribución 2, vocabulario validado 2 y límites 2. ¿Cuántos puntos suma?", ["Sumo los cinco criterios.", "2 + 1 + 2 + 2 + 2.", "Comparo con el máximo de 10."], "Suma 9 de 10 puntos."),
        W("Dar retroalimentación", "Un compañero habló muy rápido y dijo «chaltumay» al inicio. Escribe la retroalimentación.", ["Digo algo que estuvo bien: se entendía el tema.", "Sugiero hablar más lento.", "Aclaro que «chaltumay» agradece y va al cierre."], "«Se entendía el tema. Habla más lento y deja ‘chaltumay’ para el cierre, porque agradece.»"),
    ],
    mistakes=[
        M("Presentar sin ensayar.", "No se detectan errores ni el tiempo.", "Ensaya al menos una vez."),
        M("Dar retroalimentación solo con «estuvo mal».", "No dice cómo mejorar.", "Di qué estuvo bien, qué mejorar y un ejemplo."),
    ],
    R=[
        ex("¿Cuántos criterios tiene el ensayo de esta clase? Escribe el número.", "5", "Son cinco criterios en total."),
        ex("¿Cuál es el máximo de puntos? A) 10 B) 5", "A", "Cinco criterios de hasta 2 puntos suman 10."),
        ex("¿Quién valida el vocabulario en lengua? A) el educador o la educadora B) un compañero", "A", "Quien enseña la lengua."),
    ],
    C=[
        vf("el puntaje del ensayo es una ayuda para mejorar.", True, "Indica qué corregir."),
        vf("si la comunidad pide quitar una parte, se deja igual por si acaso.", False, "Se quita para respetar lo pedido."),
        ab("¿Qué incluye una buena retroalimentación?", "lo que estuvo bien, lo que mejorar y un ejemplo", "solo una crítica", "Con esos elementos ayuda."),
    ],
    A=[
        arith("Un ensayo obtuvo: claridad 1, volumen y ritmo 2, atribución 2, vocabulario validado 1 y límites 2. ¿Cuántos puntos suma?", "1+2+2+1+2", "Se suman los cinco criterios.", " puntos"),
        arith("Un grupo quiere llegar a 9 puntos de 10. Ya tiene 5. ¿Cuántos puntos le faltan?", "9-5", "Se resta lo que tiene de la meta.", " puntos"),
        ex("Retroalimentación: elige la mejor. A) «Hablaste muy bajo; sube el volumen al nombrar a doña Isabel» B) «Fue malo»", "A", "Dice qué mejorar y da un ejemplo."),
    ],
    Z=[
        ex("Un grupo obtuvo 10 puntos y dice que no necesita validación del vocabulario. ¿Qué falta? A) validación del educador y de la comunidad B) más puntos", "A", "El puntaje no reemplaza la validación."),
        ex("Una niña tiene 0 en vocabulario validado. ¿Qué hace? A) pedir al educador que valide sus palabras B) hablar más fuerte", "A", "Ese criterio requiere validación."),
    ],
    D=[
        arith("Un curso tiene 6 grupos. Cada ensayo dura 2 minutos y la retroalimentación, 1 minuto. ¿Cuántos minutos se necesitan en total?", "6*(2+1)", "Cada grupo usa 3 minutos y son 6 grupos.", " minutos"),
        ex("Un grupo quita una parte que la comunidad pidió reservar y pierde 1 punto por tiempo. ¿Hizo bien? Responde Sí o No.", "Sí", "Respetar el límite vale más que un punto."),
    ],
    context=[ab("Antes de un acto escolar para las familias, tu grupo debe presentar una exposición. ¿Qué conviene?", "ensayar, pedir retroalimentación y validar el vocabulario", "improvisar", "El acto es público y se valida antes.")],
    selfcheck=[
        ex("Nombra dos de los cinco criterios del ensayo.", "Dos entre: claridad, volumen y ritmo, atribución, vocabulario validado, límites", "Son criterios de la clase."),
        vf("al terminar se agradece a la fuente y a quienes ayudaron.", True, "Es parte del cierre."),
        ex("¿Qué haces si el educador corrige tu pronunciación? A) ensayo de nuevo y agradezco B) insisto en la mía", "A", "El educador enseña la lengua."),
    ],
    task=T("Con tu guion de la clase 4 (cosecha de Campo Abierto, doña Isabel), haz un ensayo con una persona de tu casa. Que ella califique de 0 a 2 cada criterio: claridad, volumen y ritmo, atribución, vocabulario en lengua validado y respeto de límites. Suma los puntos (máximo 10), anota una cosa que estuvo bien y una por mejorar, y escribe la pregunta que le harías al educador para validar tu vocabulario.",
           "Claridad 2, volumen 1, atribución 2, vocabulario 1 (por validar), límites 2: suma 8 de 10. Estuvo bien: nombré a doña Isabel. Mejorar: hablar más fuerte. Pregunta: «¿Puede revisar si estoy diciendo bien el saludo en la lengua de mi comunidad?»",
           ["califica los cinco criterios", "suma correctamente", "anota logro y mejora", "pregunta de validación"], ["tabla de puntos", "pregunta al educador"], ["sumar mal", "omitir la validación"],
           "Pedir que muestre los puntos y la suma; valorar que pida validación."),
    reinforce="Haz una tabla con los cinco criterios y el puntaje de tu ensayo.",
    extend="Escribe una retroalimentación para un compañero con un logro, una mejora y un ejemplo.",
)
