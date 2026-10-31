"""Cuaderno del estudiante, 7.º básico Historia, Geografía y Ciencias Sociales: OA 17 (límites al poder en Atenas y Roma)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI07 OA 17"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a identificar las instituciones y las normas con que Atenas y Roma limitaron el poder. Sirve para entender cómo se evitó que una sola persona mandara sin control.",
    ["Sé que Atenas y Roma fueron ciudades de la Antigüedad.", "Sé que una ley es una norma para todos."],
    [
        "Atenas, ciudad griega, desarrolló la democracia, palabra que significa «poder del pueblo». Sus instituciones principales fueron la Asamblea, donde los ciudadanos varones discutían y votaban las leyes; el Consejo de los Quinientos, que preparaba los temas; los tribunales populares, formados por ciudadanos elegidos por sorteo; y los estrategos, que dirigían el ejército y eran elegidos. Hacia el 508 a.C., Clístenes hizo reformas que ampliaron la participación.",
        "Roma, según la tradición, se convirtió en república en el 509 a.C., cuando expulsó a su último rey. Una república es un sistema en que los cargos no son hereditarios sino elegidos y temporales. Sus instituciones principales fueron los cónsules (dos magistrados que gobernaban durante un año), el Senado (consejo de personas con experiencia), las asambleas del pueblo y los tribunos de la plebe, que defendían a los ciudadanos comunes.",
        "En ambas ciudades las normas ayudaban a limitar el poder. En Roma, la Ley de las Doce Tablas, escrita hacia el 450 a.C., puso por escrito normas para que todos las conocieran. La ley escrita permite que una autoridad no pueda castigar a su gusto. Estas instituciones no eran perfectas ni incluían a todos, pero fueron intentos de repartir y controlar el poder.",
    ],
    [("democracia", "gobierno en que el pueblo decide, del griego «poder del pueblo»"), ("república", "sistema en que los cargos son elegidos y temporales"), ("cónsul", "magistrado romano que gobernaba por un año, junto a otro"), ("Senado", "consejo romano de personas con experiencia política"), ("Asamblea", "reunión de ciudadanos atenienses que votaban las leyes"), ("magistrado", "persona que ejercía un cargo público en Roma")],
    [
        ("Reconocer una institución", "Una ficha de ejemplo dice: «Reunión de ciudadanos varones que discuten y votan las leyes». ¿Es de Atenas o de Roma, y cómo se llama?", ["Los ciudadanos votan las leyes.", "Eso es la Asamblea ateniense."], "Atenas; la Asamblea"),
        ("Reconocer un cargo", "En Roma, dos personas gobiernan por un año. ¿Cómo se llaman?", ["Son magistrados.", "Gobernaban por un año.", "Son cónsules."], "Cónsules"),
    ],
    [
        ("Creer que Atenas y Roma tenían las mismas instituciones.", "Atenas tenía Asamblea y tribunales populares; Roma, cónsules, Senado y tribunos.", "Nombra la ciudad antes de nombrar la institución."),
        ("Pensar que la ley escrita ya existía en todas partes.", "En Roma fue un avance: las Doce Tablas pusieron las normas por escrito, hacia el 450 a.C.", "Pregunta cuándo y por qué se escribió la ley."),
    ],
    [
        ("¿Qué significa «democracia»?", "Poder del pueblo", "Es la definición del vocabulario."),
        ("¿Cuántos cónsules había en Roma?", "Dos", "Gobernaban juntos por un año."),
        ("¿Cuál era el consejo romano de personas con experiencia?", "El Senado", "Está en el vocabulario."),
    ],
    [
        ("¿Quién defendía a los ciudadanos comunes en la República romana?", "Los tribunos de la plebe", "Esa era su función."),
        ("¿Cuántos años duraba el cargo de cónsul?", "Un año", "Los cargos eran temporales."),
        ("¿Qué institución ateniense preparaba los temas para la Asamblea?", "El Consejo de los Quinientos", "Preparaba los asuntos que se votaban."),
    ],
    [
        arith("La Ley de las Doce Tablas se escribió hacia el 450 a.C. y la República romana comenzó, según la tradición, en el 509 a.C. ¿Cuántos años pasaron entre ambos hechos?", "509-450", "Antes de Cristo los años se cuentan hacia atrás: se resta el menor al mayor."),
        ("En una ciudad de ejemplo, los jueces son 200 ciudadanos elegidos por sorteo. ¿Cuál de las dos ciudades usaba tribunales así?", "Atenas", "Los tribunales populares ciudadanos eran atenienses."),
        ("Un cargo de ejemplo es hereditario y vitalicio. ¿Es compatible con una república, según la clase?", "No", "En una república los cargos son elegidos y temporales."),
    ],
    [
        ("Pedro dice: «El Senado romano era una asamblea que votaba todas las leyes». ¿Qué corrección haces?", "Era un consejo de personas con experiencia; las asambleas del pueblo votaban", "El Senado y las asambleas eran instituciones distintas."),
        ("¿Por qué la ley escrita limita el poder?", "Porque todos conocen las normas y una autoridad no puede castigar a su gusto", "Las reglas públicas ponen un límite."),
    ],
    [
        ("Ordena de más antigua a más reciente según la clase: A) inicio de la República romana, B) reformas de Clístenes, C) Ley de las Doce Tablas.", "A, B, C", "La República (509 a.C.) es anterior a las reformas de Clístenes (hacia 508 a.C.) y a las Doce Tablas (hacia 450 a.C.); los años antes de Cristo se cuentan hacia atrás."),
        ("Una afirmación dice: «En Atenas y Roma el poder se concentraba en una sola persona». Corrígela con dos instituciones.", "Había instituciones como la Asamblea, el Consejo, los cónsules y el Senado que repartían el poder", "El poder estaba repartido."),
    ],
    [("Un estudiante lee: «Dos magistrados elegidos por un año, un consejo de experiencia y asambleas del pueblo». ¿A qué ciudad corresponde?", "A Roma", "Cónsules, Senado y asambleas son romanos.")],
    [("En la unidad de Atenas y Roma, ¿qué es una república?", "Un sistema en que los cargos son elegidos y temporales", "Es la definición del vocabulario."), ("¿Cuándo se escribió la Ley de las Doce Tablas?", "Hacia el 450 a.C.", "La explicación lo dice."), ("¿Por qué se dice que la ley escrita es un límite al poder?", "Porque todos conocen las normas", "Ninguna autoridad puede inventarlas.")],
    (
        "Completa una tabla de dos columnas (Atenas y Roma) con tres filas: instituciones principales, duración de los cargos, norma importante. Usa solo datos de la clase. Después escribe tres líneas explicando cómo cada ciudad intentó que nadie mandara sin control.",
        "Atenas: Asamblea, Consejo, tribunales; Roma: cónsules, Senado, tribunos; norma: Doce Tablas.",
        ["completa seis casillas", "usa datos correctos", "explica el control del poder", "no mezcla ciudades"],
        ["tabla de seis casillas y tres líneas de explicación"],
        ["poner cónsules en Atenas", "confundir Senado con Asamblea"],
        "Muestra tu tabla a una persona de tu casa y pídele que cierre los ojos y repita una institución de cada ciudad.",
    ),
    "Dibuja un esquema simple de las instituciones de Roma y señala quién elige a quién.",
    "Averigua quién fue Clístenes y qué reformas hizo.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a examinar cómo se distribuía y se controlaba el poder en Atenas y Roma. Sirve para ver los mecanismos concretos: sorteo, elección, temporalidad, veto y rendición de cuentas.",
    ["Sé qué instituciones tenían Atenas y Roma.", "Sé que limitar el poder es evitar abusos."],
    [
        "Para limitar el poder, Atenas y Roma usaron mecanismos que todavía nos sirven. La temporalidad significa que los cargos duran poco: los cónsules, un año; muchos cargos atenienses, también un año. La elegibilidad significa que ciertos cargos se eligen por voto. El sorteo, usado en Atenas para muchos cargos, daba a cualquier ciudadano la oportunidad de participar. La colegialidad significa que el cargo lo ejercen varios: en Roma, dos cónsules.",
        "Otros mecanismos fueron el veto, la rendición de cuentas y el ostracismo. En Roma, los tribunos de la plebe podían vetar, es decir, detener una decisión, y cada cónsul podía vetar a su colega. En Atenas, los magistrados debían rendir cuentas al terminar su cargo. El ostracismo era una votación en la que los ciudadanos podían desterrar por diez años a alguien considerado peligroso para la ciudad.",
        "Estos mecanismos evitaban que el poder se concentrara. Un historiador antiguo, Polibio, describió a Roma como un gobierno mixto con tres elementos: cónsules (una autoridad), Senado (un grupo de experiencia) y pueblo (las asambleas). Cada uno equilibraba a los otros. Sin embargo, el sistema tuvo crisis y no incluía a toda la población.",
    ],
    [("temporalidad", "carácter limitado en el tiempo de un cargo"), ("elegibilidad", "principio por el cual ciertos cargos se eligen por voto"), ("sorteo", "elección al azar de una persona para un cargo"), ("veto", "derecho de detener una decisión de otra autoridad"), ("rendición de cuentas", "explicación que da una autoridad sobre lo que hizo en su cargo"), ("ostracismo", "votación ateniense para desterrar por diez años a alguien considerado peligroso")],
    [
        ("Identificar el mecanismo", "En Roma, un cónsul detiene una decisión de su colega. ¿Qué mecanismo usa?", ["Detiene una decisión.", "Es el veto."], "El veto"),
        ("Identificar otro mecanismo", "Un magistrado ateniense explica al final de su año todo lo que hizo con el dinero público. ¿Qué mecanismo es?", ["Explica lo que hizo en su cargo.", "Es rendición de cuentas."], "Rendición de cuentas"),
    ],
    [
        ("Pensar que el sorteo era injusto.", "Daba a cualquier ciudadano la posibilidad de participar y evitaba compras de votos.", "Pregunta qué problema resolvía."),
        ("Creer que el ostracismo era pena de muerte.", "Era un destierro de diez años, sin quitar los bienes.", "Distingue destierro de muerte."),
    ],
    [
        ("¿Cuántos años dura un cargo de cónsul?", "Un año", "La temporalidad limitaba su poder."),
        ("¿Qué derecho tenían los tribunos de la plebe para detener decisiones?", "El veto", "Es el mecanismo del vocabulario."),
        ("¿Cuántos años duraba el destierro por ostracismo?", "Diez", "La explicación lo dice."),
    ],
    [
        ("¿Qué quiere decir «colegialidad»?", "Que un cargo lo ejercen varios, como los dos cónsules", "Es el reparto del cargo entre más de una persona."),
        ("¿Por qué el sorteo daba oportunidad a cualquier ciudadano?", "Porque no dependía de la riqueza ni de la fama", "El azar trata a todos igual."),
        ("¿Quién describió a Roma como un gobierno mixto?", "Polibio", "La clase lo nombra."),
    ],
    [
        arith("En una votación de ejemplo participan 600 ciudadanos y 250 votan por desterrar a una persona. ¿Cuántos no votan por desterrar?", "600-250", "Se restan los votos a favor del total."),
        ("En una ciudad de ejemplo un gobernante dura 20 años en su cargo y nadie puede detenerlo. ¿Qué dos mecanismos de la clase le faltan?", "Temporalidad y veto", "No hay límite de tiempo ni forma de detenerlo."),
        ("Observa: «Un cónsul quiere declarar una guerra, pero su colega lo impide». ¿Qué mecanismo se usa?", "Colegialidad con veto", "Dos cónsules se equilibran con la posibilidad de vetar."),
    ],
    [
        ("Luis dice: «Si los cargos duraran toda la vida, el poder estaría mejor repartido». ¿Qué error comete?", "La temporalidad evita que una persona concentre el poder durante mucho tiempo", "Los cargos largos concentran el poder."),
        ("¿Por qué el ostracismo podía usarse injustamente?", "Porque dependía de la votación y podía dañar a alguien por rivalidad política", "Ningún mecanismo era perfecto."),
    ],
    [
        ("¿Cuál cargo tiene más temporalidad? A) un cargo de un año B) un cargo de por vida.", "A", "Un cargo de un año termina pronto y limita el tiempo de mando."),
        ("Relaciona cada mecanismo con su ciudad: sorteo, veto de los tribunos. Responde en ese orden.", "Atenas, Roma", "El sorteo fue usado en Atenas y el veto de los tribunos en Roma."),
    ],
    [("En una ciudad de ejemplo existen tres cargos: uno dura cinco años, otro es hereditario y el tercero dura un año y debe rendir cuentas. ¿Cuál se parece más a los mecanismos de Atenas y Roma?", "El que dura un año y rinde cuentas", "Combina temporalidad y rendición de cuentas.")],
    [("En la unidad de Atenas y Roma, ¿qué es el veto?", "El derecho de detener una decisión de otra autoridad", "Es la definición del vocabulario."), ("En la unidad de Atenas y Roma, ¿qué es la rendición de cuentas?", "Explicar lo que se hizo en un cargo", "Es la definición del vocabulario."), ("¿Para qué sirve la temporalidad?", "Para evitar que una persona concentre el poder mucho tiempo", "Limita la duración del mando.")],
    (
        "Elige dos mecanismos de la clase y explica en cuatro líneas, con un ejemplo inventado en un curso, cómo evitarías que el delegado de curso concentrara demasiado poder. Usa al menos un mecanismo ateniense y uno romano. Datos útiles: sorteo, elección, un año de duración, dos delegados, veto, rendición de cuentas.",
        "Elegiría dos delegados por un año; uno podría vetar al otro; al final rendirían cuentas ante el curso.",
        ["usa un mecanismo ateniense", "usa un mecanismo romano", "explica cómo limita el poder", "es posible en un curso"],
        ["texto de cuatro líneas con dos mecanismos"],
        ["usar mecanismos que no existieron", "no explicar la limitación"],
        "Presenta tu idea a una persona de tu casa y pídele que diga qué mecanismo le parece más justo.",
    ),
    "Escribe una ventaja y un problema del sorteo para elegir cargos.",
    "Averigua qué es el ostracismo hoy y en qué se parece o diferencia del antiguo.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a reconocer quiénes eran ciudadanos en Atenas y Roma y quiénes quedaban excluidos. Sirve para evaluar los límites de estas instituciones.",
    ["Sé que Atenas y Roma limitaron el poder con instituciones.", "Sé que una norma puede incluir a unos y excluir a otros."],
    [
        "Un ciudadano era alguien con derechos políticos: podía votar, participar en asambleas y ocupar cargos. En Atenas, la ciudadanía era para varones adultos nacidos de padres atenienses. Quedaban excluidos las mujeres, los esclavos y los metecos, extranjeros que vivían en la ciudad. Por eso la democracia ateniense era una democracia de una minoría de la población.",
        "En Roma, el ciudadano (cives) tenía derechos legales y políticos, pero no todos eran iguales. Había patricios, familias aristocráticas, y plebeyos, el resto de los ciudadanos libres. Los plebeyos lograron con luchas, como la creación de los tribunos de la plebe en el 494 a.C., más derechos. Las mujeres no votaban, aunque tenían ciertos derechos civiles. Los esclavos no eran ciudadanos. Con el tiempo, Roma extendió la ciudadanía: tras la Guerra Social (91–88 a.C.) se dio a los aliados italianos y en el 212 d.C. a casi todos los habitantes libres del Imperio.",
        "Estas exclusiones muestran los límites de la época. Hoy consideramos que los derechos políticos deben incluir a todas las personas adultas. Pero al estudiar el pasado, hay que explicar quiénes participaban y evitar suponer que la palabra «ciudadano» significaba lo mismo que hoy.",
    ],
    [("ciudadano", "persona con derechos políticos en su ciudad"), ("meteco", "extranjero que vivía en Atenas sin ser ciudadano"), ("patricio", "miembro de las familias aristocráticas de Roma"), ("plebeyo", "ciudadano romano que no era patricio"), ("exclusión", "dejar fuera a alguien de un derecho"), ("aliados", "pueblos unidos a Roma por acuerdos")],
    [
        ("Clasificar personas", "Una mujer libre vivía en Atenas, hija de padre ateniense. ¿Era ciudadana con derecho a voto?", ["Las mujeres estaban excluidas.", "No tenía derecho a voto."], "No"),
        ("Clasificar a otra persona", "Un comerciante extranjero vive en Atenas hace veinte años. ¿Cómo se le llamaba?", ["Es un extranjero residente.", "Se le llama meteco."], "Meteco"),
    ],
    [
        ("Creer que en Atenas votaba toda la población.", "Votaban solo los varones adultos nacidos de padres atenienses.", "Pregunta quién estaba incluido."),
        ("Pensar que la ciudadanía romana no cambió.", "Se extendió con el tiempo, por ejemplo a los aliados italianos y después a casi todos los habitantes libres del Imperio.", "Fecha cada ampliación."),
    ],
    [
        ("¿Cómo se llamaba el extranjero residente en Atenas?", "Meteco", "Está en el vocabulario."),
        ("¿En qué año aproximado se crearon los tribunos de la plebe?", "494 a.C.", "La explicación da esa fecha."),
        ("¿Podían votar los esclavos en Roma?", "No", "No eran ciudadanos."),
    ],
    [
        ("¿Quiénes eran los patricios?", "Miembros de las familias aristocráticas de Roma", "Es la definición del vocabulario."),
        ("¿Quiénes estaban excluidos de la ciudadanía ateniense?", "Mujeres, esclavos y metecos", "La explicación los nombra."),
        ("¿Qué ocurrió en el 212 d.C. con la ciudadanía romana?", "Se extendió a casi todos los habitantes libres del Imperio", "La clase lo menciona."),
    ],
    [
        arith("La Guerra Social romana duró de 91 a 88 a.C. ¿Cuántos años pasaron entre su inicio y su fin?", "91-88", "Se resta el año menor al mayor (los años a.C. se cuentan hacia atrás)."),
        ("En Atenas, de 100 personas de ejemplo, 20 eran ciudadanos varones. ¿Cuántas personas quedaban excluidas?", "80", "Se restan los ciudadanos del total."),
        ("Una ficha de ejemplo dice: «En una votación en Atenas solo participan varones adultos de padres atenienses». ¿Qué grupos no votan?", "Mujeres, esclavos y metecos", "Son los grupos excluidos."),
    ],
    [
        ("Julia dice: «La democracia de Atenas era igual a la de hoy». Da una diferencia de la clase.", "En Atenas solo votaba una minoría de varones adultos", "La participación era mucho más limitada."),
        ("¿Por qué los plebeyos lucharon por tener tribunos?", "Para proteger sus derechos frente a los patricios", "El tribunado fue un logro de la plebe."),
    ],
    [
        ("Ordena de la ciudadanía más restringida a la más amplia: A) Atenas clásica, B) Roma tras el 212 d.C.", "A, B", "En Atenas votaba una minoría; en Roma imperial casi todos los habitantes libres eran ciudadanos."),
        ("Un estudiante escribe: «Como excluían a muchas personas, no sirve estudiarlas». ¿Qué responderías?", "Sirve para ver cómo se limitó el poder y también sus límites", "El pasado se analiza con sus logros y exclusiones."),
    ],
    [("Un joven de ejemplo nace en Roma de una familia libre, pero no patricia. ¿Cómo se llama su grupo y qué lograron los de su grupo en el 494 a.C.?", "Plebeyo; consiguieron los tribunos de la plebe", "Es el grupo de ciudadanos que no eran patricios.")],
    [("En la unidad de Atenas y Roma, ¿qué es un ciudadano?", "Una persona con derechos políticos en su ciudad", "Es la definición del vocabulario."), ("¿Qué significa exclusión?", "Dejar fuera a alguien de un derecho", "Es la definición del vocabulario."), ("¿Por qué es importante conocer las exclusiones?", "Para entender los límites de esas instituciones", "Permiten evaluar con justicia el pasado.")],
    (
        "Escribe un texto de cinco líneas que responda: «¿Quién participaba y quién no en la democracia ateniense y en la república romana?». Incluye al menos tres grupos excluidos o con menos derechos y una ampliación de la ciudadanía con su fecha. Termina con una frase que no juzgue con ideas de hoy sin explicarlas.",
        "En Atenas votaban varones adultos de padres atenienses; no votaban mujeres, esclavos ni metecos. En Roma, en el 212 d.C. se extendió la ciudadanía a casi todos los libres.",
        ["menciona tres grupos con menos derechos", "incluye una ampliación con fecha", "distingue Atenas de Roma", "no proyecta ideas de hoy sin explicarlas"],
        ["texto de cinco líneas con cuatro elementos"],
        ["decir que todos votaban", "olvidar fechas"],
        "Lee tu texto a una persona de tu casa y pídele que diga quién quedó fuera.",
    ),
    "Anota qué derechos políticos tienen hoy las personas de tu edad y cuáles no.",
    "Averigua cuándo pudieron votar las mujeres por primera vez en Chile.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a comparar los mecanismos de control del poder de Atenas y Roma. Sirve para ver semejanzas y diferencias sin decir que una ciudad fue mejor.",
    ["Sé qué mecanismos usaban Atenas y Roma.", "Sé comparar con criterios."],
    [
        "Para comparar se eligen criterios. Primero, la forma de participación: en Atenas el pueblo decidía directamente en la Asamblea; en Roma había asambleas, pero el Senado y los magistrados tenían mucho peso. Segundo, la forma de elegir cargos: en Atenas, sorteo y elección; en Roma, elección. Tercero, la duración: en ambas, cargos temporales, de un año.",
        "Cuarto, el control del poder. En Atenas, la rendición de cuentas y el ostracismo; en Roma, el veto de los tribunos y la colegialidad de los cónsules. Quinto, la ley: ambas usaron leyes escritas, aunque en Roma las Doce Tablas fueron un hito. Sexto, la ciudadanía: en ambas excluyó a mujeres y esclavos.",
        "Los resultados de una comparación dependen de los criterios. Si el criterio es la participación directa del pueblo, Atenas destaca. Si es la estabilidad por siglos o el reparto entre varias instituciones, Roma destaca. Por eso se evita decir «una fue mejor» y se prefiere decir «cada una resolvió de manera distinta el problema de controlar el poder».",
    ],
    [("criterio", "aspecto que se usa para comparar"), ("participación directa", "forma en que el pueblo decide por sí mismo, sin representantes"), ("colegialidad", "ejercicio de un cargo por varias personas"), ("hito", "hecho importante que marca un antes y un después"), ("estabilidad", "capacidad de mantenerse sin grandes cambios"), ("gobierno mixto", "mezcla de elementos de una sola autoridad, un grupo y el pueblo")],
    [
        ("Elegir el criterio", "Se compara «cuántos años duran los cargos». ¿Qué criterio es: duración, ciudadanía o ley?", ["Habla de años.", "Es la duración."], "Duración"),
        ("Aplicar el criterio", "Criterio: ¿hay veto para detener decisiones? ¿Cuál ciudad lo tenía en la clase?", ["Los tribunos y los cónsules.", "Eso es Roma."], "Roma"),
    ],
    [
        ("Comparar sin criterios.", "Sin criterios, la comparación queda en opiniones.", "Nombra el criterio antes de comparar."),
        ("Decir que una ciudad fue mejor.", "Cada una resolvió de manera distinta; el resultado depende del criterio.", "Usa «en cuanto a…» al comparar."),
    ],
    [
        ("¿En cuál ciudad el pueblo decidía directamente en la Asamblea?", "Atenas", "Así lo dice la explicación."),
        ("¿En cuál ciudad existía el veto de los tribunos?", "Roma", "Es un mecanismo romano."),
        ("¿Cuánto duraban los cargos en ambas ciudades?", "Generalmente un año", "La temporalidad era común."),
    ],
    [
        ("En la unidad de Atenas y Roma, ¿qué es un criterio?", "Un aspecto que se usa para comparar", "Es la definición del vocabulario."),
        ("¿Qué grupos estaban excluidos en ambas ciudades?", "Mujeres y esclavos", "Ambas los excluían."),
        ("¿Qué mecanismo de Atenas desterraba por diez años?", "El ostracismo", "Es el mecanismo ateniense."),
    ],
    [
        ("Criterio: «participación directa del pueblo». ¿Qué ciudad destaca más?", "Atenas", "Allí la Asamblea decidía directamente."),
        ("Criterio: «reparto del poder entre tres elementos». ¿Qué ciudad destaca más?", "Roma", "El gobierno mixto reparte entre cónsules, Senado y pueblo."),
        arith("Una ciudad de ejemplo elige 10 magistrados cada año y cada uno dura 1 año. En 8 años, ¿cuántos magistrados distintos se necesitan, como mínimo, si ninguno repite?", "10*8", "Cada año se renuevan los 10 cargos."),
    ],
    [
        ("Ana dice: «Roma fue mejor porque duró más». ¿Qué problema tiene su criterio?", "Elige solo la duración y no considera la participación ni la inclusión", "Un solo criterio no basta."),
        ("Pedro dice: «Atenas era perfecta porque el pueblo decidía». ¿Qué dato de la clase lo contradice?", "Excluía a mujeres, esclavos y metecos", "La participación era limitada."),
    ],
    [
        ("Relaciona criterio y ciudad destacada: participación directa, reparto entre varios organismos. Responde en ese orden.", "Atenas, Roma", "Es la lectura de la comparación."),
        ("Un estudiante escribe: «En cuanto a la ley escrita, ambas ciudades la usaron; en cuanto a la participación, Atenas destaca». ¿Usó criterios correctamente?", "Sí", "Nombra el criterio antes de comparar."),
    ],
    [("Una tabla de ejemplo compara Atenas y Roma en tres criterios: forma de participación, duración y ciudadanía. ¿Cuál criterio muestra una semejanza clara?", "La duración o la ciudadanía excluyente", "En ambas los cargos eran de un año y se excluía a mujeres y esclavos.")],
    [("En la unidad de Atenas y Roma, ¿qué es la participación directa?", "La forma en que el pueblo decide por sí mismo", "Es la definición del vocabulario."), ("¿Qué mecanismo romano evitaba el abuso de un solo cónsul?", "La colegialidad y el veto", "Dos cónsules podían detenerse."), ("¿Por qué evitar «una fue mejor»?", "Porque depende del criterio", "La comparación debe ser justa.")],
    (
        "Haz una tabla comparativa con cuatro criterios (participación, elección de cargos, duración, control del poder) y dos columnas (Atenas y Roma). Escribe una frase en cada casilla con datos de la clase. Después escribe dos líneas explicando por qué evitas decir «una fue mejor».",
        "Participación: Atenas, Asamblea directa; Roma, asambleas, Senado y magistrados. Duración: ambas, un año.",
        ["ocho casillas completas", "datos correctos", "dos líneas de justificación", "usa criterios claros"],
        ["tabla de ocho casillas y dos líneas"],
        ["mezclar ciudades", "dar opiniones sin criterio"],
        "Muestra tu tabla a una persona de tu casa y pídele que elija un criterio y diga qué ciudad destaca.",
    ),
    "Escribe un criterio nuevo para comparar Atenas y Roma y explica por qué sirve.",
    "Averigua qué diferencia hay entre democracia directa y representativa.",
)

# ================================================================ clase 5
lesson(
    OA, 5,
    "Aprenderé a evaluar el alcance de las instituciones de Atenas y Roma sin proyectar las instituciones actuales. Sirve para reconocer continuidades y cambios con el presente.",
    ["Sé comparar mecanismos y ciudadanía.", "Sé qué es un anacronismo."],
    [
        "Hay continuidades entre el mundo antiguo y el actual. Seguimos usando la idea de que los cargos deben ser temporales, de que la ley debe ser pública y de que el poder se debe repartir entre varias instituciones. También usamos palabras como democracia, república y senado. Pero hay cambios importantes: hoy la mayoría de las democracias son representativas, es decir, el pueblo elige representantes; el voto se extiende a todas las personas adultas; y los derechos humanos protegen a todos, incluyendo la prohibición de la esclavitud.",
        "Para evaluar los alcances de las instituciones antiguas hay que preguntar qué lograban en su tiempo, a quién incluían y qué límites tenían. Evitamos el anacronismo: no hay que decir que Atenas «era una democracia como la nuestra» ni juzgar a sus habitantes solo con valores actuales sin explicar el contexto.",
        "Un buen razonamiento sigue tres pasos. Primero, describir el mecanismo antiguo. Segundo, compararlo con uno actual, nombrando la semejanza y la diferencia. Tercero, concluir con cuidado: «se parece en…, pero cambió en…». Así se reconoce el aporte sin idealizar el pasado.",
    ],
    [("continuidad", "algo que se mantiene a lo largo del tiempo"), ("cambio", "algo que se transforma con el tiempo"), ("democracia representativa", "sistema en que el pueblo elige representantes para decidir"), ("sufragio universal", "derecho de voto de todas las personas adultas"), ("derechos humanos", "derechos que protegen a toda persona por ser persona"), ("idealizar", "ver el pasado mejor de lo que fue")],
    [
        ("Clasificar", "«Los cargos de alcalde duran cuatro años». ¿Se parece más a la temporalidad antigua o a la monarquía hereditaria?", ["El cargo es temporal.", "Se parece a la temporalidad."], "A la temporalidad"),
        ("Clasificar otro rasgo", "Hoy se prohíbe la esclavitud. ¿Es continuidad o cambio respecto de Atenas y Roma?", ["En Atenas y Roma existía esclavitud.", "Hoy se prohíbe.", "Es cambio."], "Cambio"),
    ],
    [
        ("Decir que Atenas era una democracia como la actual.", "Era directa, para una minoría y con esclavitud; la actual es representativa y con sufragio universal.", "Nombra la semejanza y la diferencia."),
        ("Idealizar el pasado.", "Las instituciones antiguas tenían logros y exclusiones.", "Evalúa a quién incluían."),
    ],
    [
        ("¿Qué democracia es la que elige representantes?", "La representativa", "Es la definición del vocabulario."),
        ("¿Qué derecho tienen hoy todas las personas adultas para elegir?", "El voto (sufragio universal)", "Es la definición del vocabulario."),
        ("¿Una continuidad es algo que se mantiene o que se transforma?", "Que se mantiene", "Es la definición del vocabulario."),
    ],
    [
        ("Nombra una continuidad entre el mundo antiguo y el actual.", "Cargos temporales, ley pública, reparto del poder o palabras como democracia", "Son las continuidades de la clase."),
        ("Nombra un cambio importante.", "Democracia representativa, sufragio universal o prohibición de la esclavitud", "Son los cambios de la clase."),
        ("En la unidad de Atenas y Roma, ¿qué es idealizar el pasado?", "Verlo mejor de lo que fue", "Es la definición del vocabulario."),
    ],
    [
        ("Hoy el presidente de Chile dura cuatro años en el cargo. ¿Qué continuidad con la temporalidad antigua muestra?", "Que el cargo es temporal", "El poder tiene límite de tiempo."),
        ("Una ley chilena de ejemplo se publica para que todos la conozcan. ¿Qué continuidad con las Doce Tablas muestra?", "La ley pública", "Todos pueden conocer la norma."),
        ("Una asamblea de curso de ejemplo elige delegados para decidir. ¿Es más parecida a la democracia directa o a la representativa?", "A la representativa", "Se eligen representantes."),
    ],
    [
        ("Luis dice: «La democracia ateniense era mejor que la actual porque era directa». ¿Qué error comete?", "Idealiza el pasado y olvida que excluía a mujeres, esclavos y metecos", "Se debe evaluar a quién incluía."),
        ("Marta dice: «Como los romanos tenían esclavos, no sirve estudiarlos». ¿Qué responderías?", "Sirve estudiar sus mecanismos y también sus exclusiones para evaluarlos con justicia", "El pasado se estudia con matices."),
    ],
    [
        ("Ordena el razonamiento: A) comparar con uno actual, B) concluir con cuidado, C) describir el mecanismo antiguo.", "C, A, B", "Es el orden de los tres pasos."),
        ("Un estudiante concluye: «El veto de los tribunos es idéntico al veto que usa hoy un presidente». ¿Qué le falta a su conclusión?", "Nombrar también las diferencias entre ambos", "Un buen razonamiento dice en qué se parece y en qué cambió."),
    ],
    [("Un estudiante escribe: «El Senado romano era igual al Senado de Chile». ¿Qué dos diferencias puedes dar con lo estudiado?", "Roma no tenía sufragio universal y el Senado era un consejo de experiencia, no elegido por todos", "Hoy los senadores son elegidos por voto.")],
    [("En la unidad de Atenas y Roma, ¿qué es una continuidad?", "Algo que se mantiene a lo largo del tiempo", "Es la definición del vocabulario."), ("En la unidad de Atenas y Roma, ¿qué es el sufragio universal?", "El derecho de voto de todas las personas adultas", "Es la definición del vocabulario."), ("¿Cuáles son los tres pasos del razonamiento de la clase?", "Describir, comparar y concluir con cuidado", "Es la estructura de la explicación.")],
    (
        "Escribe un texto de siete líneas con el título «Lo que seguimos usando y lo que cambió». Debe incluir dos continuidades, dos cambios y una frase que evite el anacronismo. Usa solo datos de la unidad.",
        "Continuidades: cargos temporales y ley pública. Cambios: democracia representativa y fin de la esclavitud. No debemos decir que Atenas era como la actual.",
        ["dos continuidades", "dos cambios", "una frase que evita el anacronismo", "datos correctos"],
        ["texto de siete líneas con tres partes"],
        ["idealizar el pasado", "confundir continuidad con cambio"],
        "Pide a una persona de tu casa que subraye las continuidades y los cambios que encontró en tu texto.",
    ),
    "Escribe una pregunta que un historiador podría hacer sobre los alcances de la república romana.",
    "Averigua qué instituciones actuales de Chile controlan el poder (por ejemplo, los tribunales y el Congreso).",
)
