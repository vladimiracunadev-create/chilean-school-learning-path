"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF05 (sentido de la revitalización y el fortalecimiento de la lengua, estructuras básicas gramaticales y semánticas,
nuevos contextos de uso) y OA LF06 (creaciones audiovisuales o escritas con recursos TIC para contar situaciones
personales, familiares o comunitarias).

Criterio de autoría: comunidades, personas, talleres y producciones son INVENTADOS y rotulados. No se describe la
gramática ni el vocabulario de ninguna lengua indígena: las ideas de «estructura gramatical» y «significado» se enseñan
con ejemplos en castellano y la forma en que funcionan en la lengua de cada comunidad la explica el educador o la
educadora tradicional. Las únicas palabras en lengua indígena son «mari mari», «chaltumay», «iorana» y «maururu».
Sin marcas comerciales ni enlaces. Importa los ayudantes de student_content_lc6_b.
"""
from __future__ import annotations

from student_content_lc6_b import ab, vf, L, M, T, W, MAT
from student_lessons import arith, ex

LF5, LF6 = "LC06 OA LF05", "LC06 OA LF06"

# ============================================================ OA LF05 · Revitalización, estructuras, nuevos contextos
L(
    LF5, 1, materials=MAT,
    use="Aprenderé qué significan revitalizar y fortalecer una lengua indígena y a situar una experiencia de revitalización: quién la cuenta, qué se hace y qué no se cuenta. Sirve para hablar de la lengua con respeto y sin inventar.",
    prior=["Sé que cada pueblo tiene su propia lengua.", "Sé que lo que se dice en la lengua lo enseña el educador o la educadora tradicional."],
    explain=[
        "Una lengua se mantiene viva cuando las personas la usan en la vida diaria y la transmiten a las nuevas generaciones. Cuando una lengua se habla cada vez menos, se dice que necesita ser revitalizada: devolverle usos y hablantes. Cuando una lengua se sigue hablando y se quiere hacerla más fuerte, se habla de fortalecerla. Ambas palabras comparten el deseo de que la lengua siga viva.",
        "Revitalizar y fortalecer son acciones de las comunidades, no tareas de una sola persona. Pueden incluir conversaciones con las personas mayores, talleres con educadores tradicionales, materiales de estudio, cuentos grabados con permiso y uso de la lengua en espacios nuevos. Cada comunidad decide qué hace y cómo, y el ritmo lo marca ella.",
        "Para hablar de una experiencia de revitalización, la situamos con una ficha: comunidad, qué se hace, quién lo cuenta, permiso y límite. Así sabemos de quién es el relato y qué no se cuenta. Nunca medimos la identidad de una persona por cuánto habla su lengua: pertenecer a un pueblo no depende de eso.",
    ],
    vocab=[("revitalizar", "devolver usos y hablantes a una lengua que se habla poco"), ("fortalecer", "hacer más fuerte el uso de una lengua que se sigue hablando"), ("hablante", "persona que usa una lengua"), ("transmitir", "pasar un saber o una lengua a otras personas"), ("generación", "grupo de personas de edades parecidas")],
    worked=[
        W("Leer una ficha de revitalización", "Ficha inventada. Comunidad: Quebrada Fresca (no es un pueblo real). Experiencia: un taller de conversación los sábados con personas mayores y niños. Fuente: doña Olga, vecina. Permiso: sí. Límite: no se cuentan los nombres de los niños. ¿Qué se hace y qué no se cuenta?", ["La experiencia es un taller de conversación los sábados.", "Participan personas mayores y niños.", "No se cuentan los nombres de los niños."], "Se hace un taller de conversación con mayores y niños; no se cuentan los nombres de los niños."),
        W("Distinguir revitalizar y fortalecer", "Caso 1: una lengua casi no se habla y un grupo quiere que vuelva a usarse. Caso 2: una lengua se habla bien en una comunidad y quieren que se use en la radio local. ¿Qué palabra corresponde a cada caso?", ["En el caso 1 hay que devolver usos: revitalizar.", "En el caso 2 se refuerza lo que ya existe: fortalecer.", "Ambos buscan que la lengua siga viva."], "Caso 1, revitalizar; caso 2, fortalecer."),
    ],
    mistakes=[
        M("Pensar que revitalizar es tarea de una sola persona.", "La lengua se mantiene viva entre muchas personas.", "Piensa en quiénes participan: mayores, niños, educadores y familias."),
        M("Creer que alguien es «menos» de su pueblo porque habla poco la lengua.", "La identidad no depende de eso.", "Nunca midas a una persona por su lengua."),
    ],
    R=[
        ex("Ficha: «Comunidad: Alto Manso. Experiencia: radio comunitaria con cuentos en la lengua. Fuente: don Rubén.» ¿Quién es la fuente?", "Don Rubén", "La ficha lo nombra."),
        ex("En la misma ficha, ¿qué experiencia se cuenta? A) radio comunitaria con cuentos en la lengua B) un viaje al extranjero", "A", "La ficha lo dice."),
        ex("¿Qué palabra significa devolver usos y hablantes a una lengua que se habla poco? A) revitalizar B) borrar", "A", "Esa es la definición."),
    ],
    C=[
        vf("fortalecer una lengua es hacer más fuerte el uso de una lengua que se sigue hablando.", True, "Esa es la definición."),
        vf("la identidad de una persona se mide por cuánto habla la lengua de su pueblo.", False, "La identidad no depende de eso."),
        ab("¿Quién decide qué hace una comunidad para fortalecer su lengua?", "la propia comunidad", "una persona de otro lugar", "Cada comunidad decide su camino."),
    ],
    A=[
        ex("Clasifica en REVITALIZAR o FORTALECER: a) un taller para que niños que no hablan la lengua empiecen a usarla b) una radio que usa la lengua que ya hablan los vecinos.", "a revitalizar, b fortalecer", "En a se devuelven usos; en b se refuerza lo que existe."),
        ex("Una ficha dice «Experiencia: taller de lengua». No dice fuente ni permiso. ¿Qué haces? A) pido esos datos antes de usarla B) la uso igual", "A", "Sin fuente ni permiso se detiene la actividad."),
        arith("Un taller tiene 2 sesiones al mes durante 5 meses. ¿Cuántas sesiones hay en total?", "2*5", "Se multiplican las sesiones por los meses.", " sesiones"),
    ],
    Z=[
        ex("Ana dice: «Julián no habla la lengua de su pueblo, así que no es parte del pueblo». ¿Qué error comete?", "Mide la identidad por el uso de la lengua", "La identidad no depende de cuánto se habla."),
        ex("Un grupo cuenta una experiencia de revitalización de una comunidad sin pedir permiso porque «es una buena noticia». ¿Qué falta? A) permiso de la fuente B) más fotos", "A", "Contar bien no reemplaza el permiso."),
    ],
    D=[
        ex("Dos comunidades inventadas: en una los mayores enseñan a los niños los sábados; en otra una radio transmite cuentos. ¿Cuál de las dos es la «correcta» forma de revitalizar?", "Ninguna es la única correcta", "Cada comunidad decide su camino."),
        arith("En un taller de lengua participan 8 niños y 6 personas mayores. ¿Cuántas personas hay en total?", "8+6", "Se suman niños y mayores.", " personas"),
    ],
    context=[ab("El 21 de febrero es el Día Internacional de la Lengua Materna. Tu curso quiere organizar una actividad. ¿Qué debe preguntarse primero?", "qué actividad quiere hacer la comunidad y qué autoriza", "qué es más vistoso", "La actividad se decide con la comunidad.")],
    selfcheck=[
        ex("Nombra una acción para fortalecer una lengua.", "Una entre: conversar con mayores, talleres, materiales, radio u otros usos nuevos", "Son acciones de comunidades."),
        vf("revitalizar y fortalecer buscan que la lengua siga viva.", True, "Ese es el propósito de ambas."),
        ex("¿Qué haces si no sabes cómo se usa tu lengua en un contexto? A) pregunto al educador o la educadora B) lo invento", "A", "Ellos enseñan la lengua."),
    ],
    task=T("Lee esta experiencia inventada de doña Olga, de Quebrada Fresca: «Los sábados nos juntamos en la sede. Las personas mayores conversan con los niños mientras preparamos pan. Cada semana aprendemos algo nuevo. No contamos los nombres de los niños.» Haz una ficha con comunidad, experiencia, fuente, quiénes participan y un límite. Escribe una frase que empiece con «Esta experiencia ayuda a mantener viva la lengua porque…».",
           "Comunidad: Quebrada Fresca. Experiencia: taller de conversación mientras preparan pan. Fuente: doña Olga. Participan: mayores y niños. Límite: no se cuentan los nombres de los niños. Esta experiencia ayuda a mantener viva la lengua porque los mayores y los niños la usan juntos.",
           ["completa la ficha", "respeta el límite", "explica con una razón"], ["ficha completa", "frase con razón"], ["incluir nombres de niños", "inventar lo que no dice el relato"],
           "Pedir que indique en qué línea del relato está cada dato; valorar que respete el límite."),
    reinforce="Subraya en la ficha de Quebrada Fresca los participantes, la experiencia y el límite con tres colores.",
    extend="Explica con tus palabras por qué revitalizar una lengua es una tarea de toda la comunidad.",
)

L(
    LF5, 2, materials=MAT,
    use="Aprenderé el sentido de revitalizar una lengua y cuáles son los límites al hablar de ella: qué dice la fuente, qué interpreto y qué no se cuenta. Sirve para explicar por qué importa la lengua sin exagerar ni inventar.",
    prior=["Sé qué significan revitalizar y fortalecer.", "Sé separar lo que dice una fuente de lo que interpreto."],
    explain=[
        "Las comunidades revitalizan su lengua por varias razones. Una es la identidad: la lengua lleva la historia y la manera de ver el mundo de un pueblo. Otra es la memoria: guarda nombres de lugares, relatos y saberes. Otra es la comunicación: permite hablar con las personas mayores y entre generaciones. Estas razones las explican las propias comunidades.",
        "Al explicar el sentido de revitalizar, conviene separar tres cosas: lo que dice la fuente («según don Rubén, aprender la lengua lo acercó a sus abuelos»), lo que yo interpreto («yo pienso que la lengua ayuda a la convivencia entre generaciones») y lo que no se cuenta o no sé («no sé cuántos niños participan»). Marcar esas diferencias evita atribuir ideas que la comunidad no dijo.",
        "Hay también límites éticos: no se obliga a nadie a hablar la lengua, no se critica a quien la habla poco y no se muestran grabaciones sin permiso. Revitalizar es un camino de cada persona y de cada comunidad, con sus ritmos y decisiones.",
    ],
    vocab=[("memoria", "lo que una comunidad recuerda y guarda de su historia"), ("identidad", "sentirse parte de un pueblo y de su historia"), ("convivencia", "manera de vivir juntos y cuidarse"), ("obligar", "hacer que alguien haga algo sin que lo quiera"), ("límite ético", "lo que no se debe hacer por respeto a las personas")],
    worked=[
        W("Separar tres cosas", "Testimonio inventado de don Rubén, de Alto Manso: «Cuando empecé a aprender la lengua, pude conversar mejor con mi abuela. Me gustaría que más niños vinieran, pero no puedo obligarlos». Separa lo que dice, lo que interpreto y lo que no se cuenta.", ["Dice: aprender la lengua lo ayudó a conversar con su abuela.", "Interpreto: yo pienso que la lengua acerca a las generaciones.", "No se cuenta: cuántos niños participan."], "Dice: pudo conversar con su abuela. Interpreto: acerca generaciones. No se cuenta: cuántos niños participan."),
        W("Detectar un juicio", "Un niño escribe: «Los que no hablan la lengua no quieren a su pueblo». ¿Qué error hay?", ["Se critica a un grupo de personas.", "El testimonio no dice eso.", "La identidad no depende de hablar la lengua."], "Error: critica y atribuye algo que nadie dijo; hay que quitarlo."),
    ],
    mistakes=[
        M("Atribuir a la comunidad una razón que no dijo.", "Se inventa la voz de la comunidad.", "Usa «según…» solo para lo que dijo la fuente."),
        M("Pensar que todas las personas de un pueblo deben hablar la lengua.", "No se puede obligar ni medir a nadie.", "Respeta el camino de cada persona."),
    ],
    R=[
        ex("Testimonio inventado: «Aprender la lengua me acercó a mi abuela». ¿A quién se acercó? A) a su abuela B) a un vecino", "A", "El testimonio lo dice así."),
        ex("¿Cuántas razones para revitalizar se mencionan en la explicación: identidad, memoria y comunicación? Escribe el número.", "3", "Son tres razones nombradas."),
        ex("Si el testimonio no explica algo, ¿qué escribes? A) el testimonio no lo dice B) lo invento", "A", "Se declara el límite."),
    ],
    C=[
        vf("no se obliga a una persona a hablar la lengua de su pueblo.", True, "Es un límite ético."),
        ab("¿Qué razón de revitalizar se relaciona con guardar nombres de lugares y relatos?", "la memoria", "el dinero", "La memoria guarda lo que la comunidad recuerda."),
        vf("una interpretación es lo mismo que un dato de la fuente.", False, "La interpretación es idea de quien lee."),
    ],
    A=[
        ex("Testimonio de don Rubén: «Me gustaría que más niños vinieran, pero no puedo obligarlos». Clasifica en DICE LA FUENTE o INTERPRETO: a) no puede obligar a los niños b) los niños no vienen porque no les interesa.", "a dice la fuente, b interpreto", "La segunda explica algo que la fuente no dijo."),
        ex("Clasifica la razón como IDENTIDAD, MEMORIA o COMUNICACIÓN: a) hablar con los abuelos b) guardar nombres de lugares.", "a comunicación, b memoria", "Hablar con los abuelos es comunicarse; guardar nombres es memoria."),
        ex("Tras leer «no puedo obligarlos», alguien escribe «Don Rubén cree que obligar es malo». ¿Qué problema tiene? A) atribuye una creencia más amplia que lo dicho B) lo dijo don Rubén palabra por palabra", "A", "Don Rubén solo dijo que no puede obligar."),
    ],
    Z=[
        ex("Clara escribe: «Revitalizar sirve solo para el pasado». ¿Qué le falta? A) considerar que también sirve para comunicar hoy B) usar otro color", "A", "La lengua sirve para comunicarse en el presente."),
        ex("Un compañero dice que quien habla poco la lengua «no tiene identidad». ¿Qué le respondes?", "Que la identidad no se mide por cuánto se habla la lengua", "Pertenecer no depende de eso."),
    ],
    D=[
        ex("Dos frases: Una: «Según don Rubén, aprender la lengua lo acercó a su abuela». Otra: «Según don Rubén, todos los niños deben aprender la lengua». ¿Cuál se queda en lo que dijo?", "La primera", "La segunda agrega una idea que él no dijo."),
        ex("Te piden explicar en un cartel por qué se revitaliza la lengua. ¿Qué incluyes? A) razones de la fuente con su nombre y un límite B) opiniones sin fuente", "A", "Se atribuye y se declara el límite."),
    ],
    context=[ab("Tu curso invita a una persona de la comunidad a hablar de su experiencia con la lengua. Un compañero quiere preguntar cuánto habla cada niño del curso. ¿Qué le dices?", "que esa pregunta puede incomodar y no mide a nadie", "que lo haga para saber", "No se mide a las personas por su lengua.")],
    selfcheck=[
        ex("Nombra una razón por la que una comunidad revitaliza su lengua.", "Identidad, memoria o comunicación", "Son razones de la clase."),
        vf("conviene declarar lo que no sé al explicar un testimonio.", True, "Eso evita inventar datos."),
        ex("¿Qué haces con una grabación de una persona mayor? A) pido permiso antes de compartirla B) la comparto", "A", "Sin permiso no se comparte."),
    ],
    task=T("Lee este testimonio inventado de doña Olga, de Quebrada Fresca: «Mi abuela me hablaba en la lengua y yo solo escuchaba. Hoy voy a los talleres y ya puedo decir algunas frases. Mi hijo todavía no quiere venir y no lo voy a obligar.» Haz tres columnas: «La fuente dice», «Yo interpreto» y «No se cuenta». Pon al menos dos datos en cada una y cierra con una frase de límites.",
           "La fuente dice: su abuela hablaba la lengua; hoy va a talleres; su hijo no quiere venir. Yo interpreto: yo pienso que los talleres le permiten recuperar lo que escuchaba de niña. No se cuenta: por qué el hijo no quiere venir. Límite: no sé cuántas frases dice.",
           ["separa tres columnas", "marca sus ideas como interpretación", "respeta que no obliga"], ["tabla de tres columnas", "frase de límites"], ["atribuir ideas no dichas", "juzgar al hijo"],
           "Pedir que muestre en qué línea está cada dato; valorar que no juzgue a nadie."),
    reinforce="Subraya con un color lo que dice doña Olga y con otro lo que interpretas.",
    extend="Escribe por qué no obligar a nadie a hablar la lengua puede ser una forma de respeto.",
)

L(
    LF5, 3, materials=MAT,
    use="Aprenderé qué son las estructuras básicas gramaticales y semánticas de una lengua usando ejemplos en castellano, y a preguntar cómo funcionan en la lengua de mi comunidad. Sirve para describir una lengua sin inventar cómo es.",
    prior=["Sé qué significa revitalizar una lengua.", "Sé que lo que se dice en la lengua indígena lo enseña el educador o la educadora."],
    explain=[
        "La gramática es el conjunto de reglas con que una lengua organiza las palabras para formar oraciones. Las estructuras básicas de una oración son sus partes principales: quién o qué (sustantivo), qué hace o qué ocurre (verbo) y cómo o dónde ocurre (otras palabras que complementan). En castellano decimos «Los niños recogen frutas», donde «niños» y «frutas» nombran y «recogen» dice la acción.",
        "La semántica estudia los significados. Las palabras se agrupan en campos semánticos, que son conjuntos de palabras relacionadas por el significado: «río, lluvia, vertiente, lago» pertenecen al campo del agua. Entender un campo semántico ayuda a ampliar el vocabulario y a ver qué es importante para quienes usan una lengua.",
        "Cada lengua organiza sus oraciones y sus significados a su manera, y no tiene que parecerse al castellano. Por eso, para saber cómo funciona la gramática y el significado de las palabras de una lengua indígena, no nos basamos en el castellano ni inventamos reglas: lo explica el educador o la educadora tradicional, con ejemplos de la comunidad.",
    ],
    vocab=[("gramática", "reglas con que una lengua organiza las palabras en oraciones"), ("sustantivo", "palabra que nombra personas, animales, lugares o cosas"), ("verbo", "palabra que dice una acción o un estado"), ("semántica", "estudio del significado de las palabras"), ("campo semántico", "conjunto de palabras relacionadas por el significado")],
    worked=[
        W("Reconocer partes de una oración", "Oración en castellano: «Los pescadores reparan las redes». ¿Qué palabras son sustantivos y cuál es el verbo?", ["Pregunto quién o qué: pescadores y redes (nombran).", "Pregunto qué hacen: reparan (acción).", "Las otras palabras acompañan."], "Sustantivos: pescadores y redes; verbo: reparan."),
        W("Armar un campo semántico", "Palabras: río, lluvia, lápiz, vertiente, lago. ¿Cuál no pertenece al campo del agua?", ["Veo qué tienen en común: están relacionadas con el agua.", "Río, lluvia, vertiente y lago lo están.", "Lápiz no."], "No pertenece «lápiz»."),
    ],
    mistakes=[
        M("Pensar que todas las lenguas arman las oraciones igual que el castellano.", "Cada lengua tiene su propia gramática.", "Pregunta cómo la organiza la lengua de tu comunidad."),
        M("Inventar cómo se dice una oración en lengua indígena usando el orden del castellano.", "Se crea una forma que no existe.", "Pide ejemplos al educador."),
    ],
    R=[
        ex("En «Los niños recogen frutas», ¿cuál es el verbo?", "Recogen", "Dice la acción."),
        ex("¿Cuál es un sustantivo en «El lago está tranquilo»? A) lago B) tranquilo", "A", "«Lago» nombra un lugar."),
        ex("¿Qué estudia la semántica? A) el significado de las palabras B) los números", "A", "Esa es la definición."),
    ],
    C=[
        vf("un campo semántico es un conjunto de palabras relacionadas por el significado.", True, "Esa es su definición."),
        vf("las lenguas indígenas organizan sus oraciones siempre igual que el castellano.", False, "Cada lengua tiene su gramática propia."),
        ab("¿Quién explica cómo funciona la gramática de la lengua de tu comunidad?", "el educador o la educadora tradicional", "tú, adivinando", "Ellos conocen la lengua."),
    ],
    A=[
        ex("Oración: «Las abuelas cuentan cuentos». Clasifica en SUSTANTIVO o VERBO: a) abuelas b) cuentan.", "a sustantivo, b verbo", "«Abuelas» nombra; «cuentan» dice la acción."),
        ex("¿Cuál palabra no pertenece al campo semántico de los animales de granja? gallina, oveja, vaca, martillo", "Martillo", "Es una herramienta, no un animal."),
        ex("En «Los vecinos cuidan la vertiente», ¿cuántos sustantivos hay? Escribe el número.", "2", "«Vecinos» y «vertiente» nombran."),
    ],
    Z=[
        ex("Pedro escribe una oración en una lengua indígena siguiendo el orden del castellano y dice que «está bien». ¿Qué error comete?", "Supone que la lengua se organiza como el castellano", "Cada lengua tiene su gramática."),
        ex("Dos listas de palabras relacionadas con el trabajo en la huerta: Una: «semilla, riego, surco, cosecha». Otra: «semilla, lápiz, cosecha, nube». ¿Cuál forma un campo semántico?", "La primera", "Todas se relacionan con la huerta."),
    ],
    D=[
        ex("Un compañero dice que una palabra de la lengua indígena «significa lo mismo que en castellano» porque tradujo con una aplicación. ¿Qué haces? A) pregunto al educador qué significa en su contexto B) acepto la traducción", "A", "El significado en la comunidad lo explica el educador."),
        arith("Un campo semántico tiene 4 palabras de agua dulce y 3 de agua salada. ¿Cuántas palabras tiene en total?", "4+3", "Se suman las dos listas.", " palabras"),
    ],
    context=[ab("En una clase de lengua, el educador explica una oración de la comunidad. Una compañera pregunta si «es igual que en castellano». ¿Qué conviene?", "escuchar y anotar cómo la organiza la lengua", "decir que sí para no preguntar", "Cada lengua se aprende en sus propios términos.")],
    selfcheck=[
        ex("Nombra una palabra de un campo semántico del agua.", "Río, lluvia, vertiente o lago", "Están relacionadas con el agua."),
        vf("la gramática es el conjunto de reglas con que una lengua organiza las palabras.", True, "Esa es la definición."),
        ex("¿Qué haces si quieres saber cómo se forma una oración en lengua indígena? A) pregunto al educador B) la invento", "A", "Ellos conocen la lengua."),
    ],
    task=T("Usa esta oración inventada en castellano: «Los niños recogen frutas en la huerta». 1) Marca los sustantivos y el verbo. 2) Escribe un campo semántico de cuatro palabras relacionadas con la huerta (por ejemplo, partes de una huerta que ves en tu casa o en una plaza). 3) Escribe una pregunta que le harías al educador para saber cómo se dice una oración parecida en la lengua de tu comunidad.",
           "Sustantivos: niños, frutas, huerta. Verbo: recogen. Campo semántico: huerta, semilla, riego, cosecha. Pregunta: «¿Cómo se organiza una oración sobre recoger frutas en nuestra lengua?»",
           ["identifica sustantivos y verbo", "arma un campo semántico", "formula pregunta al educador"], ["oración marcada", "lista de cuatro palabras", "pregunta"], ["inventar oraciones en lengua", "mezclar campos"],
           "Pedir que explique por qué cada palabra pertenece al campo; valorar que pregunte en vez de inventar."),
    reinforce="Marca con dos colores los sustantivos y los verbos de tres oraciones sobre tu barrio.",
    extend="Escribe dos campos semánticos distintos de cinco palabras cada uno y explica qué los une.",
)

L(
    LF5, 4, materials=MAT,
    use="Aprenderé a explicar el sentido de fortalecer una lengua con una respuesta atribuida: lo que dice la fuente, mi reflexión, un límite y una pregunta. Sirve para hablar de la lengua con respeto y con razones.",
    prior=["Sé separar lo que dice la fuente de lo que interpreto.", "Sé qué son sustantivo, verbo y campo semántico."],
    explain=[
        "Una explicación sobre el sentido de fortalecer la lengua tiene cuatro partes. Primero, lo que cuenta la fuente: «Según don Rubén…». Segundo, mi reflexión: «Yo pienso que…», con una razón. Tercero, un límite: lo que no sé. Cuarto, una pregunta que llevaré al educador o a la educadora tradicional.",
        "Podemos incorporar una idea sobre la estructura de la lengua, siempre con ejemplos en castellano y sin inventar cómo es la lengua indígena. Por ejemplo: «Yo pienso que aprender cómo se organizan las oraciones ayuda a conversar mejor; no sé cómo se organizan en la lengua de mi comunidad y lo preguntaré». Así se explica el sentido sin afirmar lo que no se sabe.",
        "La explicación puede mencionar nuevos contextos de uso, como un cartel en la escuela o un mensaje de saludo en la radio, siempre con permiso de quien los creó. Al final se hace la devolución: se muestra el texto a la fuente o al educador para que lo revisen y corrijan.",
    ],
    vocab=[("explicación atribuida", "explicación en que cada dato dice de quién viene"), ("reflexión", "pensamiento propio con razones"), ("contexto de uso", "lugar o situación donde se usa una lengua"), ("devolución", "mostrar el texto a la fuente para que lo revise"), ("pregunta pendiente", "duda anotada para consultar")],
    worked=[
        W("Armar una explicación", "Testimonio inventado de don Rubén: «En la radio de Alto Manso decimos buenos días en la lengua todas las mañanas». Escribe una explicación de cuatro partes.", ["Fuente: según don Rubén, en la radio saludan en la lengua cada mañana.", "Reflexión: yo pienso que así la lengua se escucha todos los días.", "Límite: no sé qué palabras usan. Pregunta: ¿cómo se elige el saludo?"], "Según don Rubén, en la radio saludan en la lengua cada mañana. Yo pienso que así se escucha todos los días. No sé qué palabras usan. Pregunta: ¿cómo se elige el saludo?"),
        W("Corregir una atribución", "Un niño escribe: «Alto Manso usa la radio porque es lo más importante para mantener la lengua». ¿Qué falla?", ["«Lo más importante» no lo dijo la fuente.", "No dice quién lo afirma.", "Hay que atribuir y marcar la idea propia."], "Faltó atribuir a don Rubén y marcar «yo pienso que» para lo suyo."),
    ],
    mistakes=[
        M("Explicar cómo es la gramática de la lengua indígena sin saberlo.", "Se inventa una regla.", "Escribe «no sé cómo se organiza» y pregunta."),
        M("Hablar de «los pueblos» en general desde un solo testimonio.", "Un testimonio habla de una comunidad.", "Escribe «según don Rubén, de Alto Manso…»."),
    ],
    R=[
        ex("¿Cuántas partes tiene una explicación atribuida de esta clase? Escribe el número.", "4", "Son fuente, reflexión, límite y pregunta."),
        ex("¿Qué frase atribuye un dato a don Rubén? A) «Según don Rubén…» B) «Todos creen…»", "A", "Nombra a la fuente."),
        ex("¿A quién llevas la pregunta pendiente? A) al educador o a la educadora tradicional B) a nadie", "A", "Él o ella enseña la lengua."),
    ],
    C=[
        vf("una reflexión se marca con «yo pienso que».", True, "Así no se confunde con la fuente."),
        vf("puedo afirmar cómo se organiza una oración en la lengua de mi comunidad si lo supongo.", False, "Eso sería inventar."),
        ab("¿Qué haces con un contexto de uso que creó otra persona?", "pido permiso para mencionarlo", "lo menciono sin avisar", "Se pide permiso a quien lo creó.")],
    A=[
        ex("Testimonio de don Rubén: «En la radio decimos buenos días en la lengua». Completa: «Según don Rubén, en la radio…»", "Dicen buenos días en la lengua", "Repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o REFLEXIÓN: a) don Rubén cuenta que usan la radio b) yo pienso que la radio acerca la lengua a las familias.", "a fuente, b reflexión", "La primera es un dato atribuido; la segunda, una idea propia."),
        ex("Explicación: «No sé cómo se organizan las oraciones en la lengua». ¿Qué parte es? A) el límite B) la fuente", "A", "Declara lo que no sé."),
    ],
    Z=[
        ex("Marta escribe una explicación sin pregunta final. ¿Qué mejoraría? A) agregar una pregunta para el educador B) quitar la fuente", "A", "La pregunta indica lo que se debe consultar."),
        ex("Dos explicaciones: Una dice «según doña Olga, el taller reúne a mayores y niños» y otra «los talleres siempre funcionan». ¿Cuál está mejor atribuida?", "La primera", "La segunda generaliza sin fuente."),
    ],
    D=[
        ex("Una niña quiere mencionar el cartel bilingüe que hizo otro curso. ¿Qué hace primero? A) pedir permiso a quienes lo hicieron B) copiarlo", "A", "Se respeta la autoría."),
        ex("Tu explicación mezcla una idea tuya con un dato de la fuente sin marcar. ¿Qué corriges? A) marco «yo pienso que» y «según…» B) borro todo", "A", "Se separa lo propio de lo atribuido."),
    ],
    context=[ab("En una muestra de lenguas, debes explicar en 30 segundos por qué se fortalece una lengua. ¿Cómo empiezas?", "con un dato atribuido a una fuente", "con una opinión sin fuente", "Una explicación atribuida inicia con la fuente.")],
    selfcheck=[
        ex("Nombra las cuatro partes de una explicación atribuida.", "Fuente, reflexión, límite y pregunta", "Son las partes de la clase."),
        vf("la devolución muestra el texto a la fuente para que lo revise.", True, "Esa es la devolución."),
        ex("¿Cuál de estas es una pregunta pendiente? A) ¿Cómo se organiza una oración en nuestra lengua? B) Ya sé todo", "A", "Es una duda para consultar."),
    ],
    task=T("Lee este testimonio inventado de doña Olga, de Quebrada Fresca: «En el cartel de la sede escribimos el saludo en la lengua y en castellano. Los niños lo leen al entrar. No sabemos todavía cómo se escribe cada palabra de las frases largas». Escribe una explicación de cuatro partes: fuente, reflexión con «yo pienso que», límite y pregunta para el educador. Añade una frase de devolución.",
           "Según doña Olga, en el cartel de la sede está el saludo en la lengua y en castellano. Yo pienso que así los niños ven la lengua cada día. Límite: no sé cómo se escriben las frases largas. Pregunta: ¿cómo se escribe correctamente cada frase? Devolución: le leeré el texto a doña Olga.",
           ["incluye las cuatro partes", "atribuye a doña Olga", "añade devolución"], ["explicación escrita", "frase de devolución"], ["afirmar gramática sin saberlo", "generalizar"],
           "Pedir que señale cada parte; valorar que formule la pregunta."),
    reinforce="Subraya con cuatro colores las cuatro partes de tu explicación.",
    extend="Escribe una segunda explicación sobre otro contexto de uso (una radio o un taller) con las cuatro partes.",
)

L(
    LF5, 5, materials=MAT,
    use="Aprenderé a reconocer nuevos contextos de uso de una lengua (cartel, radio, video, mensaje) y a contrastarlos con los contextos tradicionales sin decir cuál es mejor. Sirve para expresar ideas en la lengua en muchos espacios.",
    prior=["Sé explicar el sentido de fortalecer una lengua.", "Sé contrastar con los mismos criterios."],
    explain=[
        "Un contexto de uso es el lugar o la situación en que se usa una lengua. Los contextos tradicionales son aquellos en que la comunidad ha usado su lengua desde hace mucho: conversaciones en la casa, trabajo con las personas mayores y encuentros de la comunidad. Los nuevos contextos son espacios donde antes se usaba poco, como la escuela, la radio, un video o un cartel.",
        "Cada contexto sirve para algo distinto. En una conversación se intercambian ideas. En un cartel se saluda o se informa. En una grabación se guarda una voz con permiso. Contrastar es poner los contextos lado a lado con los mismos criterios: quién participa, qué se comunica y qué cuidado requiere. No decimos que uno vale más.",
        "Los nuevos contextos permiten que las personas expresen ideas en la lengua de formas nuevas, pero requieren cuidados: permiso de quien aparece o habla, respeto de lo reservado y validación del educador sobre las expresiones. Un mensaje bien cuidado en un nuevo espacio también fortalece la lengua.",
    ],
    vocab=[("contexto tradicional", "espacio donde la comunidad usa su lengua desde hace mucho"), ("nuevo contexto", "espacio donde antes se usaba poco la lengua"), ("criterio", "punto igual para comparar"), ("grabación", "registro de una voz o imagen"), ("validar", "pedir a quien sabe que confirme que está correcto")],
    worked=[
        W("Clasificar contextos", "Clasifica en TRADICIONAL o NUEVO: a) conversar con la abuela en la cocina b) un cartel bilingüe en la entrada de la escuela.", ["La conversación en la casa es antigua.", "El cartel en la escuela es un espacio nuevo.", "Ambos usan la lengua para comunicar."], "a tradicional; b nuevo."),
        W("Contrastar sin jerarquizar", "Contrasta una conversación con la abuela y un cartel bilingüe con el criterio «quién participa».", ["En la conversación participan dos personas que se hablan.", "En el cartel participan quienes lo escribieron y quienes lo leen.", "Semejanza: ambos comunican. Diferencia: uno es entre dos y otro llega a muchos."], "Ambos comunican; uno es entre dos personas y el otro llega a muchas. No se dice cuál es mejor."),
    ],
    mistakes=[
        M("Decir que los contextos nuevos son mejores porque son modernos.", "Es un juicio, no una descripción.", "Describe qué hace cada contexto."),
        M("Grabar a alguien hablando en la lengua sin pedir permiso.", "Se usa su voz sin autorización.", "Pide permiso y explica para qué."),
    ],
    R=[
        ex("¿Cuál es un contexto tradicional? A) conversar con una persona mayor en la casa B) un video en una pantalla", "A", "La conversación en la casa es antigua."),
        ex("¿Cuál es un nuevo contexto? A) un cartel bilingüe en la escuela B) una conversación en la cocina", "A", "El cartel en la escuela es un espacio nuevo."),
        ex("¿Qué se pide antes de grabar a alguien? A) permiso B) un premio", "A", "La voz de una persona se usa con su permiso."),
    ],
    C=[
        vf("un nuevo contexto puede ayudar a fortalecer la lengua si se cuida.", True, "Con permiso y validación fortalece."),
        vf("los contextos nuevos son mejores que los tradicionales.", False, "No se jerarquizan."),
        ab("¿Qué criterio sirve para contrastar dos contextos?", "quién participa y qué se comunica", "cuál es más moderno", "Son criterios iguales para ambos."),
    ],
    A=[
        ex("Clasifica en TRADICIONAL o NUEVO: a) trabajar con un mayor en la huerta b) un mensaje de saludo en una radio de la escuela.", "a tradicional, b nuevo", "El trabajo con mayores es antiguo; la radio escolar es un espacio nuevo."),
        ex("Criterio «qué cuidado requiere». Cartel: validar la escritura. Grabación: pedir permiso de la voz. ¿Qué diferencia hay? A) cada uno requiere un cuidado distinto B) ninguno requiere cuidado", "A", "Los cuidados cambian."),
        ex("Un curso pega un cartel con «mari mari». ¿Qué cuidado básico tuvo que tener? A) validar con el educador cómo se escribe B) ninguno", "A", "Se valida la escritura."),
    ],
    Z=[
        ex("Rubén dice: «La radio es mejor que la conversación porque llega a más gente». ¿Qué error comete?", "Jerarquiza dos contextos", "Llegar a más gente no los hace mejores."),
        ex("Un grupo graba una voz sin permiso porque «es para difundir la lengua». ¿Qué falta? A) permiso de la persona B) más volumen", "A", "El propósito no reemplaza el permiso."),
    ],
    D=[
        ex("Dos contextos: una conversación en la cocina y un video en la escuela. Una frase correcta es: A) «el video llega a más personas; la conversación es más cercana» B) «el video es mejor»", "A", "La A describe sin ordenar."),
        arith("Una radio emite 3 saludos al día en la lengua durante 5 días. ¿Cuántos saludos son en total?", "3*5", "Se multiplican saludos por días.", " saludos"),
    ],
    context=[ab("Tu escuela quiere agregar el saludo «mari mari» en la entrada. ¿Qué pasos sigue?", "consultar con el educador y la comunidad, validar la escritura y poner el cartel", "poner el cartel de inmediato", "Primero se consulta y se valida.")],
    selfcheck=[
        ex("Nombra un contexto tradicional y uno nuevo.", "Tradicional: conversación con mayores. Nuevo: cartel, radio o video", "Son ejemplos de la clase."),
        vf("al contrastar contextos se usan los mismos criterios para todos.", True, "Así la comparación es justa."),
        ex("¿Quién valida la escritura de un cartel en lengua? A) el educador o la educadora tradicional B) un compañero", "A", "Ellos enseñan la lengua."),
    ],
    task=T("Compara dos contextos de uso inventados de la comunidad Alto Manso: A) «los sábados conversamos en la lengua con las personas mayores mientras cocinamos»; B) «en la radio comunitaria decimos buenos días en la lengua todas las mañanas». Haz una tabla con tres criterios: quién participa, qué se comunica y qué cuidado requiere. Escribe una semejanza y una diferencia sin usar «mejor».",
           "A: participan mayores y vecinos; se comparte conversación; requiere escuchar con respeto. B: participa quien habla en la radio y quienes escuchan; se saluda; requiere permiso de la voz y validar la expresión. Semejanza: ambos usan la lengua. Diferencia: A es cercano y B llega a muchas casas.",
           ["tabla con tres criterios", "semejanza y diferencia", "no jerarquiza"], ["tabla comparativa", "dos frases"], ["decir cuál es mejor", "omitir los cuidados"],
           "Pedir que explique cada criterio; valorar que describa sin ordenar."),
    reinforce="Clasifica cinco contextos de uso (cuatro tuyos y uno del cuaderno) en tradicionales y nuevos.",
    extend="Propón un nuevo contexto de uso seguro en tu escuela y escribe los cuidados que requeriría.",
)

# ============================================================ OA LF06 · Creaciones audiovisuales o escritas con TIC
L(
    LF6, 1, materials=MAT,
    use="Aprenderé a situar una creación audiovisual o escrita con TIC: qué situación cuenta, para quién, con qué recursos y con qué permisos. Sirve para planificar con respeto.",
    prior=["Sé que lo reservado se respeta.", "Sé que las expresiones en lengua las valida el educador."],
    explain=[
        "TIC significa tecnologías de la información y la comunicación: aparatos y programas que sirven para crear y compartir mensajes, como un computador, un teléfono de la escuela, una grabadora o un programa de presentaciones. Una creación audiovisual combina imagen y sonido, por ejemplo un video corto. Una creación escrita se hace con letras, por ejemplo un cuento digital o un afiche.",
        "Antes de crear, situamos la creación con una ficha: qué situación voy a contar (personal, familiar o comunitaria), para quién, con qué recursos y con qué permisos. Si no hay computador o teléfono, podemos hacer la versión en papel: un guion con dibujos, un cartel o un cuaderno. Lo importante es el mensaje y el cuidado.",
        "Contar situaciones personales, familiares o comunitarias exige decidir qué se muestra. No se muestran datos privados, rostros de otras personas sin permiso ni lugares que la comunidad reserva. Las expresiones en lengua indígena que aparezcan las valida el educador o la educadora tradicional.",
    ],
    vocab=[("TIC", "tecnologías que sirven para crear y compartir mensajes"), ("audiovisual", "que combina imagen y sonido"), ("guion", "texto que planifica lo que se dirá y mostrará"), ("audiencia", "personas a quienes va dirigida una creación"), ("permiso", "autorización de una persona para usar su imagen, voz o relato")],
    worked=[
        W("Completar una ficha de creación", "Idea: un video de 1 minuto sobre cómo una familia inventada de Llano Verde prepara pan para una fiesta del barrio. Completa: situación, audiencia, recursos y permisos.", ["Situación: familiar y comunitaria, la preparación del pan.", "Audiencia: el curso y la comunidad escolar.", "Recursos: un teléfono de la escuela o, si no hay, dibujos en papel; permisos: de las personas que aparecen."], "Situación: preparar pan; audiencia: curso y comunidad; recursos: teléfono o dibujos; permisos: de quienes aparecen."),
        W("Elegir el formato", "No hay computador en el curso. Quieres contar una situación de tu barrio. ¿Qué formato eliges?", ["Reviso los recursos: solo papel.", "Puedo hacer un cuento escrito con dibujos.", "Lo importante es el mensaje."], "Un cuento escrito con dibujos en papel."),
    ],
    mistakes=[
        M("Pensar que sin computador no se puede crear.", "Se puede hacer una versión en papel.", "Planifica con los recursos que tienes."),
        M("Filmar a otras personas sin preguntarles.", "Se usa su imagen sin permiso.", "Pide permiso antes de mostrar a alguien."),
    ],
    R=[
        ex("¿Qué significa TIC? A) tecnologías de la información y la comunicación B) trabajo individual de clase", "A", "Esa es la sigla."),
        ex("¿Qué combina una creación audiovisual? A) imagen y sonido B) solo letras", "A", "Es su definición."),
        ex("Si no tienes teléfono ni computador, ¿qué haces? A) una versión en papel B) no hago nada", "A", "Se puede crear con papel."),
    ],
    C=[
        vf("un cuento escrito con dibujos puede ser una creación sin aparatos.", True, "Es una versión en papel."),
        vf("se puede mostrar la cara de cualquier persona porque es una escuela.", False, "Se pide permiso."),
        ab("¿Qué se hace con las expresiones en lengua indígena de una creación?", "se validan con el educador o la educadora", "se corrigen con un buscador", "Ellos enseñan la lengua."),
    ],
    A=[
        ex("Clasifica en AUDIOVISUAL o ESCRITA: a) un video de 30 segundos b) un cartel con un texto.", "a audiovisual, b escrita", "El video tiene imagen y sonido; el cartel, letras."),
        ex("Ficha: «Situación: personal. Audiencia: mi curso. Recursos: grabadora de la escuela. Permisos: de mi familia». ¿Qué dato falta para una creación sobre la comunidad? A) permiso de la comunidad B) el nombre de la grabadora", "A", "Una creación comunitaria necesita permiso de la comunidad."),
        arith("Un video tiene 4 escenas de 20 segundos cada una. ¿Cuántos segundos dura?", "4*20", "Se multiplican escenas por duración.", " segundos"),
    ],
    Z=[
        ex("Carlos graba a un vecino cantando y lo publica sin avisar porque «le gustó». ¿Qué error comete?", "Usa su voz sin permiso", "La imagen y la voz requieren autorización."),
        ex("Elena planifica un video del lugar de respeto de la comunidad porque «es muy bonito». ¿Qué falla? A) es un lugar reservado B) hay poca luz", "A", "No se muestran los lugares reservados."),
    ],
    D=[
        ex("Dos planes: Uno cuenta una fiesta de barrio con permisos de los que aparecen. Otro muestra a niños sin avisar a sus familias. ¿Cuál es adecuado?", "El primero", "Tiene los permisos necesarios."),
        ex("Tienes un teléfono de la escuela solo 30 minutos y debes grabar cuatro escenas. ¿Qué haces? A) planifico antes en papel y grabo rápido B) improviso", "A", "Planificar ahorra tiempo."),
    ],
    context=[ab("Tu curso quiere crear un video para el Día Internacional de los Pueblos Indígenas (9 de agosto). ¿Qué hacen primero?", "completar la ficha y pedir los permisos", "grabar de inmediato", "La planificación y los permisos van antes.")],
    selfcheck=[
        ex("Nombra tres datos de una ficha de creación.", "Tres entre: situación, audiencia, recursos y permisos", "Son los datos de la clase."),
        vf("el mensaje es más importante que el aparato que se use.", True, "Lo central es el mensaje y el cuidado."),
        ex("¿Qué haces si el educador corrige una expresión en tu guion? A) la cambio y agradezco B) la dejo", "A", "Él enseña la lengua."),
    ],
    task=T("Planifica una creación sobre esta situación inventada: «En Llano Verde, las familias hacen una reunión de vecinos para limpiar el arroyo y cocinar una olla común al final. Doña Berta dio permiso para contar la reunión, pero no para mostrar rostros de los niños». Completa una ficha con: formato (video, audio, cartel o cuento escrito), audiencia, recursos que tendrías (si no hay aparatos, versión en papel), permisos y un límite.",
           "Formato: cuento escrito con dibujos. Audiencia: el curso. Recursos: papel y lápices. Permisos: de doña Berta, ya dado para contar la reunión. Límite: no dibujo rostros de los niños.",
           ["completa la ficha", "elige un formato viable", "respeta el límite"], ["ficha completa"], ["incluir rostros de niños", "ignorar permisos"],
           "Pedir que explique por qué eligió el formato; valorar que respete el límite."),
    reinforce="Subraya en tu ficha el formato, la audiencia, los recursos y los permisos con cuatro colores.",
    extend="Explica cómo cambiarías tu plan si no tuvieras ningún aparato en tu casa.",
)

L(
    LF6, 2, materials=MAT,
    use="Aprenderé a decidir qué se cuenta y qué no en una creación sobre una situación personal, familiar o comunitaria, protegiendo la privacidad y lo reservado. Sirve para crear con cuidado.",
    prior=["Sé completar una ficha de creación.", "Sé que lo reservado se respeta."],
    explain=[
        "Al contar una situación, decidimos qué mostrar y qué cuidar. Los datos personales son los que identifican a alguien: nombre completo, domicilio, teléfono, rostro, lugar de estudio o trabajo. En una creación escolar, estos datos no se publican. Conviene usar dibujos, nombres de fantasía o fotos de objetos y paisajes.",
        "En las situaciones familiares, la persona decide si quiere que su historia se cuente. Se le pide permiso y se le muestra cómo quedará. En las situaciones comunitarias, además, la comunidad puede reservar ciertas partes: lugares, palabras, objetos o reuniones. Ese límite no se discute.",
        "También cuidamos el uso de la lengua: las expresiones en lengua indígena que aparezcan, como «mari mari», se escriben y pronuncian como las valida el educador o la educadora. Si hay una voz grabada, esa persona debe haber dicho que sí. Revisar la creación con una lista de cuidados antes de compartirla protege a todos.",
    ],
    vocab=[("dato personal", "dato que identifica a una persona, como domicilio o teléfono"), ("privacidad", "derecho a decidir qué se cuenta de la vida propia"), ("nombre de fantasía", "nombre inventado que reemplaza el real"), ("reservado", "que la comunidad prefiere no mostrar"), ("lista de cuidados", "preguntas para revisar antes de compartir")],
    worked=[
        W("Elegir qué se muestra", "Quieres contar cómo tu familia prepara una comida para el barrio. Tienes: foto de la olla, foto del rostro de tu hermano pequeño, dirección de tu casa, dibujo del paso a paso. ¿Qué incluyes?", ["La foto de la olla y el dibujo no identifican a nadie.", "El rostro de tu hermano y la dirección son datos personales.", "No los incluyo."], "Incluyo la foto de la olla y el dibujo; no incluyo el rostro ni la dirección."),
        W("Pedir permiso", "Escribe una frase para pedir permiso a una vecina que quieres incluir en tu video.", ["Saludo con respeto.", "Digo qué crearé y cómo aparecerá.", "Pregunto si me autoriza."], "«Mari mari, vecina. Estoy haciendo un video sobre la fiesta del barrio. ¿Me autoriza a incluir su voz?»"),
    ],
    mistakes=[
        M("Poner el nombre completo y la dirección en un afiche.", "Son datos personales y no se publican.", "Usa nombres de fantasía o solo el primer nombre con permiso."),
        M("Mostrar un lugar que la comunidad reserva porque «sale en el fondo».", "Aunque sea en el fondo, se está mostrando.", "Cambia la toma o el encuadre."),
    ],
    R=[
        ex("¿Cuál es un dato personal? A) domicilio B) el color del cielo", "A", "El domicilio identifica a una persona."),
        ex("¿Qué se hace antes de usar la voz de una persona? A) pedir permiso B) cambiarla", "A", "La voz se usa con autorización."),
        ex("¿Qué haces con un lugar que la comunidad reserva? A) no lo muestro B) lo muestro de lejos", "A", "El límite se respeta."),
    ],
    C=[
        vf("una creación escolar debe incluir el domicilio de las personas que aparecen.", False, "Es un dato personal."),
        vf("se puede usar un nombre de fantasía para proteger la privacidad.", True, "Reemplaza al real."),
        ab("¿Quién decide si una historia familiar se cuenta?", "la persona o la familia involucrada", "quien la quiere contar", "Cada persona decide sobre su historia."),
    ],
    A=[
        ex("Clasifica en SE PUEDE o NO SE PUEDE publicar: a) dibujo de una olla b) teléfono de un vecino.", "a se puede, b no se puede", "El teléfono es un dato personal."),
        ex("Eliges un nombre de fantasía para un personaje de tu cuento. ¿Cuál sirve? A) «Pancho Sol» B) el nombre y apellido de tu vecino", "A", "El nombre inventado protege a tu vecino."),
        ex("Una persona mayor dice «sí, pero no muestren mi casa». ¿Qué haces con la toma de su casa? A) la elimino B) la dejo igual", "A", "Respeto su límite."),
    ],
    Z=[
        ex("Sofía muestra en su video a unos niños jugando en el patio sin avisar a sus familias porque «son sus compañeros». ¿Qué error comete?", "Muestra rostros sin permiso", "Los rostros de otros requieren autorización."),
        ex("Un grupo muestra una reunión reservada de la comunidad porque «sale poco». ¿Qué falla? A) aunque salga poco, se muestra lo reservado B) la cámara estaba lejos", "A", "El límite aplica a toda la creación."),
    ],
    D=[
        ex("Tu cuento tiene cuatro personajes reales con nombre completo. ¿Qué haces? A) cambio los nombres por fantasía B) los dejo", "A", "Protege la privacidad."),
        arith("Una lista de cuidados tiene 6 preguntas y tu creación cumple 5. ¿Cuántas faltan por cumplir?", "6-5", "Se resta lo cumplido del total.", " pregunta"),
    ],
    context=[ab("Tu curso comparte los trabajos en una muestra para las familias. Un trabajo tiene una foto del rostro de un niño sin permiso. ¿Qué haces?", "pido que la quiten o pidan permiso", "la dejo porque ya está impresa", "Se corrige antes de mostrar.")],
    selfcheck=[
        ex("Nombra dos datos personales.", "Dos entre: nombre completo, domicilio, teléfono, rostro, lugar de estudio", "Identifican a una persona."),
        vf("se pide permiso a una persona antes de grabar su voz.", True, "Es un paso necesario."),
        ex("¿Dónde revisas la escritura de «mari mari» en tu creación? A) con el educador B) en una red social", "A", "Él valida la escritura."),
    ],
    task=T("Tienes que contar con un cuento escrito esta situación inventada: «Doña Berta, de Llano Verde, enseña a los niños a preparar pan en la sede los sábados. Ella pidió que no se publiquen rostros de niños ni su dirección». Escribe una lista de tres cosas que mostrarás y tres que no mostrarás. Agrega la frase con que pedirías permiso a doña Berta para contar su taller.",
           "Mostraré: dibujo del pan, dibujo de la sede y las manos amasando. No mostraré: rostros de niños, su dirección ni su teléfono. Permiso: «Mari mari, doña Berta. ¿Me autoriza a contar su taller de pan sin mostrar rostros de niños?»",
           ["lista de tres y tres", "respeta límites", "frase de permiso"], ["lista", "frase de permiso"], ["incluir datos personales", "omitir el permiso"],
           "Pedir que explique cada exclusión; valorar la frase de permiso."),
    reinforce="Clasifica diez datos en «se puede publicar» y «no se puede publicar».",
    extend="Explica por qué un límite de la comunidad se respeta aunque a ti te parezca poco importante.",
)

L(
    LF6, 3, materials=MAT,
    use="Aprenderé a relacionar el mensaje con el formato y la audiencia, y a planificar un guion con escenas y tiempos. Sirve para que mi creación sea clara y se pueda hacer con los recursos que tengo.",
    prior=["Sé decidir qué se muestra y qué no.", "Sé sumar, multiplicar y dividir cantidades pequeñas."],
    explain=[
        "El formato es la forma en que presentamos el mensaje: un video corto, un audio, un cartel o un cuento escrito. Para elegirlo pensamos en tres cosas: qué mensaje quiero comunicar, a quién se lo cuento y qué recursos tengo. Un mensaje sobre un sonido, como una conversación, funciona bien en audio; uno sobre un proceso, como preparar pan, en video o en dibujos paso a paso.",
        "Un guion gráfico es una tabla donde cada escena tiene un dibujo y una frase. Cada escena tiene una duración. Si el video completo debe durar 60 segundos y tengo 4 escenas del mismo largo, cada una dura 15 segundos. Planificar los tiempos evita que el mensaje quede apurado o demasiado largo.",
        "El mensaje principal debe aparecer claro: una frase corta que resuma lo que el público debe recordar. Los saludos o expresiones en lengua se ubican al inicio o al cierre, tal como los valide el educador. Antes de crear, revisamos que el guion no contenga datos personales ni lugares reservados.",
    ],
    vocab=[("formato", "forma en que se presenta un mensaje"), ("guion gráfico", "tabla con un dibujo y una frase para cada escena"), ("escena", "parte de una creación que muestra una idea"), ("duración", "tiempo que dura algo"), ("mensaje principal", "frase corta con lo que el público debe recordar")],
    worked=[
        W("Dividir el tiempo", "Un video de 60 segundos tendrá 4 escenas del mismo largo. ¿Cuánto dura cada escena?", ["Divido el total entre las escenas.", "60 dividido en 4 da 15.", "Cada escena dura 15 segundos."], "15 segundos por escena."),
        W("Elegir el formato", "Quieres que las personas escuchen la manera en que una vecina saluda a quienes llegan. ¿Qué formato es más adecuado: audio o cartel?", ["El mensaje es un sonido.", "Un audio lo conserva.", "Un cartel solo lo escribiría."], "Audio, siempre con permiso de la vecina."),
    ],
    mistakes=[
        M("Elegir el formato solo porque «se ve moderno».", "Debe servir al mensaje y a los recursos.", "Pregunta qué mensaje, a quién y con qué."),
        M("No calcular los tiempos.", "El video queda apurado o largo.", "Divide el tiempo total entre las escenas."),
    ],
    R=[
        arith("Un audio dura 90 segundos y se divide en 3 partes iguales. ¿Cuánto dura cada parte?", "90//3", "Se divide el total entre las partes.", " segundos"),
        ex("¿Qué es un guion gráfico? A) una tabla con dibujo y frase por escena B) una lista de compras", "A", "Esa es su definición."),
        ex("¿Qué debe ser el mensaje principal? A) una frase corta B) un párrafo de diez líneas", "A", "Debe ser fácil de recordar."),
    ],
    C=[
        vf("el formato debe elegirse pensando en el mensaje, la audiencia y los recursos.", True, "Son los tres criterios."),
        ab("¿Qué formato conviene si quieres mostrar los pasos para preparar pan?", "video o dibujos paso a paso", "un solo cartel con una palabra", "Muestra un proceso."),
        vf("un guion gráfico no sirve si no tengo cámara.", False, "Sirve también para versiones en papel."),
    ],
    A=[
        arith("Un video de 80 segundos tiene 4 escenas iguales. ¿Cuántos segundos dura cada una?", "80//4", "Se divide el total entre las escenas.", " segundos"),
        arith("Un guion tiene tres escenas de 20 segundos y una de 10. ¿Cuántos segundos dura el video?", "20*3+10", "Se multiplican las escenas iguales y se suma la otra.", " segundos"),
        ex("Quieres que un cuento llegue a niños que aún no leen bien. ¿Qué formato sirve más? A) video o dibujos con pocas frases B) texto largo", "A", "Las imágenes ayudan a comprender."),
    ],
    Z=[
        ex("Un guion de 60 segundos tiene 5 escenas de 15 segundos. ¿Qué error tiene? A) dura 75 segundos B) dura 60", "A", "5 escenas de 15 segundos suman 75, no 60."),
        ex("Daniel quiere usar solo un cartel para comunicar un sonido. ¿Qué dificultad tiene? A) un cartel no conserva el sonido B) un cartel es caro", "A", "Un sonido se transmite mejor en audio."),
    ],
    D=[
        arith("Tu video debe durar 2 minutos (120 segundos) y tiene 6 escenas iguales. ¿Cuántos segundos dura cada escena?", "120//6", "Se divide el total entre las escenas.", " segundos"),
        ex("Tienes 30 segundos para presentar el mensaje «los vecinos cuidan el arroyo». ¿Qué haces? A) elijo una frase corta y dos escenas B) pongo diez escenas", "A", "El tiempo limitado pide un mensaje breve."),
    ],
    context=[ab("Tu curso quiere crear un mensaje breve de bienvenida para visitas de la comunidad. ¿Qué formato elige?", "un cartel o un video corto, con el saludo validado por el educador", "un video de 20 minutos", "La bienvenida es breve y se valida.")],
    selfcheck=[
        ex("Nombra tres criterios para elegir un formato.", "Mensaje, audiencia y recursos", "Son los tres criterios."),
        vf("el mensaje principal se escribe en una frase corta.", True, "Así se recuerda."),
        arith("Un video de 45 segundos tiene 3 escenas iguales. ¿Cuántos segundos dura cada una?", "45//3", "Se divide el total entre las escenas.", " segundos"),
    ],
    task=T("Planifica un guion gráfico de 4 escenas para un video o un cuento sobre esta situación inventada: «Los vecinos de Rincón del Sol limpian la plaza y luego comparten una merienda». Cada escena debe tener un dibujo (puedes describirlo) y una frase corta. El video completo dura 60 segundos con escenas iguales. Anota la duración de cada escena y el mensaje principal. No dibujes rostros.",
           "Escena 1: vecinos llegan con escobas (15 s). Escena 2: recogen hojas (15 s). Escena 3: ponen la mesa (15 s). Escena 4: comparten la merienda (15 s). Duración: 15 segundos cada una. Mensaje: cuidar la plaza entre todos.",
           ["4 escenas con dibujo y frase", "duración correcta", "mensaje principal claro"], ["guion gráfico"], ["tiempos que no suman", "mostrar rostros"],
           "Pedir que calcule la suma; valorar el mensaje claro."),
    reinforce="Calcula la duración de cada escena de dos videos de 60 y 90 segundos con 3 escenas iguales.",
    extend="Reescribe tu guion para que dure 90 segundos con 6 escenas iguales.",
)

L(
    LF6, 4, materials=MAT,
    use="Aprenderé a escribir el guion o texto final de una creación con créditos: quién narra, quién autorizó y quién validó. Sirve para atribuir y mostrar un trabajo ordenado.",
    prior=["Sé planificar escenas con tiempos.", "Sé atribuir datos a su fuente."],
    explain=[
        "Los créditos son la parte de una creación que dice quiénes participaron. Incluyen quién escribió el guion, quién narró, de quién es el relato, quién autorizó y quién validó las expresiones en lengua. Poner créditos es una forma de reconocer el trabajo de todas las personas y de atribuir cada aporte.",
        "Un guion final tiene escenas, textos de narración y créditos. Si la creación usa una expresión en lengua indígena, aparece escrita tal como la validó el educador, con una nota: «expresión validada por el educador tradicional». También conviene agregar subtítulos o textos en castellano para que todas las personas comprendan.",
        "Antes de compartir, hacemos una devolución: mostramos la creación a la persona que contó la situación y a quien validó la lengua. Si piden cambios, los hacemos y agradecemos. Una creación que cuenta una situación de otra persona siempre le pertenece en parte a esa persona.",
    ],
    vocab=[("créditos", "parte que dice quiénes participaron en una creación"), ("narrador", "persona que cuenta lo que se muestra"), ("subtítulo", "texto breve que acompaña un video para ayudar a comprender"), ("autorizar", "dar permiso"), ("devolución", "mostrar la creación terminada a quien contó la situación")],
    worked=[
        W("Escribir créditos", "Creación: cuento sobre el taller de pan de doña Berta, narrado por Luis, con el saludo «mari mari» validado por el educador. Escribe los créditos.", ["Relato: doña Berta.", "Narración: Luis.", "Validación de la expresión en lengua: el educador tradicional."], "Créditos: Relato de doña Berta. Narra Luis. Expresión «mari mari» validada por el educador tradicional."),
        W("Agregar un subtítulo", "En el video aparece «mari mari». Escribe un subtítulo en castellano.", ["«Mari mari» es un saludo en mapuzugun.", "El subtítulo lo explica en castellano.", "Se ubica bajo la escena."], "Subtítulo: «Hola» (saludo en mapuzugun)."),
    ],
    mistakes=[
        M("Omitir los créditos de quien contó la situación.", "No se atribuye el aporte.", "Anota relato, narración y validación."),
        M("Presentar la creación sin mostrarla antes a quien la contó.", "Puede haber errores o partes que no desea compartir.", "Haz la devolución primero."),
    ],
    R=[
        ex("¿Qué dicen los créditos? A) quiénes participaron B) el precio", "A", "Reconocen a las personas."),
        ex("¿Quién valida la expresión en lengua? A) el educador o la educadora tradicional B) quien edita el video", "A", "Él o ella enseña la lengua."),
        ex("¿Para qué sirve un subtítulo? A) para ayudar a comprender B) para ocultar el texto", "A", "Acompaña con castellano."),
    ],
    C=[
        vf("los créditos incluyen a la persona que contó la situación.", True, "Es parte del reconocimiento."),
        vf("la devolución se hace después de publicar.", False, "Se hace antes de compartir."),
        ab("¿Qué incluye un guion final?", "escenas, narración y créditos", "solo una portada", "Son las partes de la clase."),
    ],
    A=[
        ex("¿Qué línea de créditos atribuye el relato? A) «Relato de doña Berta» B) «Narra Luis»", "A", "Nombra a quien contó la situación."),
        ex("Clasifica en RELATO, NARRACIÓN o VALIDACIÓN: a) doña Berta b) Luis c) el educador.", "a relato, b narración, c validación", "Cada persona aporta de manera distinta."),
        ex("En un video aparece «chaltumay». ¿Qué subtítulo en castellano corresponde? A) Gracias B) Adiós", "A", "«Chaltumay» es un agradecimiento en mapuzugun."),
    ],
    Z=[
        ex("Gonzalo publica un video sobre el taller de doña Berta sin mostrárselo antes. ¿Qué error comete?", "Omite la devolución", "Debe mostrarlo antes de compartirlo."),
        ex("Un grupo agrega el nombre del educador a los créditos sin preguntarle. ¿Qué falla? A) no pidió permiso para nombrarlo B) usó letra grande", "A", "También se pide permiso para nombrar a las personas."),
    ],
    D=[
        ex("Dos versiones de créditos. Una: «Relato de doña Berta; narra Luis; expresión validada por el educador». Otra: «Hecho por mi grupo». ¿Cuál atribuye mejor?", "La primera", "Nombra cada aporte."),
        arith("Un video tiene 5 escenas de 12 segundos y créditos de 10 segundos. ¿Cuántos segundos dura en total?", "5*12+10", "Se multiplican las escenas y se suman los créditos.", " segundos"),
    ],
    context=[ab("En la muestra de tu curso, un grupo presenta un video con una vecina que contó su historia. ¿Qué debe aparecer al final?", "los créditos con su nombre y la validación", "solo el título", "Se atribuye y se agradece.")],
    selfcheck=[
        ex("Nombra tres datos que van en los créditos.", "Tres entre: relato, narración, autorización, validación de la lengua", "Son aportes que se reconocen."),
        vf("conviene agregar subtítulos en castellano a las expresiones en lengua.", True, "Ayuda a comprender."),
        ex("¿Qué haces si la persona que contó la situación pide un cambio? A) lo hago y agradezco B) lo ignoro", "A", "La devolución incluye los cambios."),
    ],
    task=T("Con tu guion gráfico de la clase anterior (limpieza de la plaza de Rincón del Sol), escribe: 1) el texto de narración de cada escena (una frase corta), 2) los créditos (relato, narración, validación de la expresión en lengua), 3) un subtítulo en castellano para el saludo «mari mari» y 4) la frase con la que mostrarás la creación a los vecinos antes de compartirla.",
           "Narración: 1) Los vecinos llegan. 2) Recogen hojas. 3) Ponen la mesa. 4) Comparten la merienda. Créditos: Relato de los vecinos de Rincón del Sol; narra [nombre de fantasía]; «mari mari» validado por el educador. Subtítulo: «Hola». Devolución: «Les mostramos nuestro video para que nos digan si algo debe cambiar».",
           ["narración por escena", "créditos completos", "subtítulo", "frase de devolución"], ["guion final"], ["omitir créditos", "no devolver"],
           "Pedir que verifique que cada aporte esté en los créditos; valorar la devolución."),
    reinforce="Escribe los créditos de una creación tuya con tres aportes.",
    extend="Escribe un mensaje de agradecimiento para quien contó la situación de tu creación.",
)

L(
    LF6, 5, materials=MAT,
    use="Aprenderé a contrastar dos versiones de una creación (por ejemplo, video y cartel) sin decir cuál es mejor y a revisarla con una lista de cuidados. Sirve para mejorar y compartir con respeto.",
    prior=["Sé hacer un guion con créditos.", "Sé contrastar con los mismos criterios."],
    explain=[
        "Una misma situación se puede contar de más de una manera: en un video, en un cartel, en un audio o en un cuento escrito. Cada formato tiene ventajas y limitaciones. Un video muestra movimiento y voz, pero necesita aparatos y más cuidado con la privacidad. Un cartel es fácil de hacer y de compartir, pero no tiene sonido. Contrastamos con los mismos criterios, sin ordenar de mejor a peor.",
        "Los criterios útiles son: quién puede acceder (con o sin aparatos), qué datos personales se arriesgan, cómo se cuida la lengua y cuánto tiempo toma hacerlo. Con ellos describimos las diferencias y elegimos según la situación, no según gusto o moda.",
        "Antes de compartir revisamos con una lista de cuidados: ¿pedí permiso?, ¿protegí los datos personales?, ¿respeté lo reservado?, ¿validó el educador la lengua?, ¿incluí créditos? y ¿hice la devolución? Si alguna respuesta es no, corregimos y revisamos de nuevo.",
    ],
    vocab=[("ventaja", "lo que un formato hace bien"), ("limitación", "lo que un formato no puede hacer o requiere"), ("acceso", "posibilidad de usar o ver algo"), ("lista de cuidados", "preguntas para revisar antes de compartir"), ("criterio", "punto igual para comparar")],
    worked=[
        W("Contrastar dos formatos", "Contrasta un video y un cartel sobre la limpieza de una plaza con el criterio «acceso».", ["El video necesita aparatos para grabar y verlo.", "El cartel se hace con papel y se ve sin aparatos.", "Ambos cuentan la misma situación."], "Semejanza: ambos cuentan la limpieza. Diferencia: el video requiere aparatos; el cartel, no. No se dice cuál es mejor."),
        W("Usar la lista de cuidados", "Un video muestra el rostro de un niño y no tiene créditos. ¿Qué preguntas de la lista no cumple?", ["¿Protegí los datos personales? No, aparece un rostro.", "¿Incluí créditos? No.", "Debo corregir ambos."], "No cumple la protección de datos ni los créditos."),
    ],
    mistakes=[
        M("Elegir el formato más vistoso sin pensar en el acceso.", "Quizás parte de la audiencia no puede verlo.", "Piensa en quién accede."),
        M("Compartir sin revisar la lista de cuidados.", "Pueden quedar errores o datos privados.", "Revisa antes."),
    ],
    R=[
        ex("¿Qué formato se hace con papel y no necesita aparatos? A) un cartel B) un video", "A", "El cartel se hace en papel."),
        ex("¿Cuántas preguntas tiene la lista de cuidados de esta clase? Escribe el número.", "6", "Son seis preguntas en total."),
        ex("¿Qué se hace antes de compartir una creación? A) revisar la lista de cuidados B) borrar los créditos", "A", "Así se evitan errores."),
    ],
    C=[
        vf("contrastar formatos significa decir cuál es el mejor.", False, "Contrastar es describir ventajas y limitaciones."),
        ab("¿Qué criterio compara si todas las personas pueden ver la creación?", "el acceso", "el color", "El acceso dice quiénes pueden verla."),
        vf("un video puede tener más riesgos de mostrar datos personales que un cartel de dibujos.", True, "Filma a personas reales."),
    ],
    A=[
        ex("Clasifica en VENTAJA o LIMITACIÓN: a) un audio conserva una voz b) un cartel no tiene sonido.", "a ventaja, b limitación", "Cada afirmación describe lo que el formato hace o no hace."),
        ex("Criterio «cuidado de la lengua». Video: se valida cómo suena y cómo se escribe el subtítulo. Cartel: se valida cómo se escribe. ¿Qué diferencia hay? A) el video requiere validar también el sonido B) ninguna", "A", "En el video también se valida la voz."),
        ex("Un grupo cumple 5 de las 6 preguntas de la lista. ¿Qué hace? A) corrige la que falta antes de compartir B) comparte igual", "A", "Se corrige antes de compartir."),
    ],
    Z=[
        ex("Marcelo dice: «El video es mejor porque es más moderno». ¿Qué error comete?", "Jerarquiza por moda", "Cada formato sirve a una situación y a un acceso."),
        ex("Un grupo comparte un cartel sin que el educador valide la escritura de «mari mari». ¿Qué pregunta de la lista falla? A) la validación de la lengua B) los créditos", "A", "Falta validar la lengua."),
    ],
    D=[
        arith("Un curso tiene 4 grupos. Cada uno revisa su creación con las 6 preguntas de la lista. ¿Cuántas revisiones se hacen en total?", "4*6", "Se multiplican los grupos por las preguntas.", " revisiones"),
        ex("Dos planes para contar la misma situación: un video que necesita 3 aparatos o un cartel con papel. Si solo hay papel, ¿cuál es viable?", "El cartel", "Se adapta a los recursos."),
    ],
    context=[ab("Tu escuela tiene una muestra pero algunas familias no pueden ver videos. ¿Qué haces?", "ofrezco también una versión en cartel o papel", "solo muestro el video", "El acceso es un criterio.")],
    selfcheck=[
        ex("Nombra dos criterios para contrastar formatos.", "Dos entre: acceso, datos personales, cuidado de la lengua, tiempo", "Son criterios de la clase."),
        vf("después de revisar la lista, se corrige lo que falta.", True, "Así mejora el trabajo."),
        ex("¿Qué escribes si un formato requiere aparatos que no tienes? A) una limitación B) una ventaja", "A", "Es algo que dificulta hacerlo."),
    ],
    task=T("Contrasta estas dos versiones inventadas de una misma creación en Rincón del Sol sobre limpiar la plaza. A) Un video de 60 segundos con voz y música. B) Un cartel de papel con cuatro dibujos y frases. Haz una tabla con tres criterios: acceso, datos personales y cuidado de la lengua. Escribe una ventaja y una limitación de cada versión. Revisa la versión B con la lista de seis cuidados.",
           "Acceso: A necesita aparatos; B no. Datos personales: A podría mostrar rostros; B usa dibujos. Lengua: A valida voz y subtítulo; B valida escritura. Ventaja A: voz y movimiento. Limitación A: aparatos. Ventaja B: fácil de hacer. Limitación B: sin sonido. Lista de B: permisos sí, datos sí, reservado sí, lengua por validar, créditos sí, devolución por hacer.",
           ["tabla de tres criterios", "ventajas y limitaciones", "revisa con la lista"], ["tabla", "lista revisada"], ["decir cuál es mejor", "omitir la validación"],
           "Pedir que explique cada celda; valorar que no ordene de mejor a peor."),
    reinforce="Revisa una creación tuya con las seis preguntas y marca cuáles cumple.",
    extend="Escribe una séptima pregunta para la lista de cuidados y explica por qué es útil.",
)
