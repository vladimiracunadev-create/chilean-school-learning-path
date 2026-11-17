"""Estética (electivo HC, 3.º y 4.º medio): OAC-03 (fenómenos que han influido en la historia de la estética) y OAC-04 (relaciones entre arte, moral y política), clases 1 a 5 de cada OA. Sociedades, obras y casos ficticios."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada texto, caso o ficha está escrito en el enunciado. "
             "Los textos filosóficos son resúmenes originales de posturas y las obras de arte son casos ficticios descritos con palabras: no se reproducen obras con derechos ni se usan imágenes o audio. "
             "Las posturas se presentan con sus razones y sin tomar partido: tu tarea es analizar y evaluar. Si tu docente propone mirar o escuchar una obra real, hazlo en sala y con las pautas que él o ella indique. "
             "En los temas de moral, política o bienestar emocional se usan casos ficticios; si algo te afecta, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O3 = "FI-ESTE-3y4-OAC-03"

# ============================================================ OAC-03, clase 1
F = ("Ficha 11 (caso ficticio: la sociedad imaginaria de Valle Alto). Momento 1: las máscaras se usaban en las ceremonias de la cosecha; nadie las llamaba «arte» y se guardaban en el templo. "
     "Momento 2: un taller empezó a fabricar copias de las máscaras con moldes para venderlas en la feria. "
     "Momento 3: un museo expone las máscaras originales en vitrinas, con buena luz, para que la gente las contemple. "
     "Pregunta de la clase: ¿qué cambió en la manera de percibir las máscaras?")
build(
    O3, 1, F,
    use="Aprenderé a plantear un problema de historia de la estética a partir de un caso: cómo las creencias religiosas, la tecnología y los procesos históricos cambian lo que una sociedad considera arte y cómo lo percibe.",
    prior=["Distingo juicio estético de juicio de hecho.", "Sé que las ideas sobre el arte pueden cambiar.", "Reconozco causas y consecuencias en un relato."],
    explain=[
        "La historia de la estética estudia cómo han cambiado, en distintas épocas y sociedades, las ideas sobre la belleza y el arte, y también las prácticas de crear, mostrar y mirar obras. Un mismo objeto puede pasar de tener una función ritual, ligada a una creencia, a ser contemplado como obra en un museo.",
        "Tres tipos de fenómenos influyen en esos cambios. Las creencias religiosas pueden encargar, regular o prohibir ciertas imágenes. Los cambios tecnológicos, como nuevas técnicas para copiar, cambian quién produce y quién ve obras. Los procesos históricos, como el crecimiento de las ciudades o los cambios de poder, modifican quién financia el arte y para qué.",
        "Explicar un fenómeno es decir qué pasó, por qué pasó y qué efectos tuvo. Evaluar su impacto es preguntar a quién afectó, cuánto cambió y cuánto duró. En esta clase solo plantearemos el problema con un caso ficticio; no aprenderemos fechas, porque lo importante es el método para explicar.",
    ],
    vocab=[("historia de la estética", "estudio de cómo cambian las ideas y prácticas sobre belleza y arte"), ("función ritual", "uso de un objeto en una ceremonia ligada a una creencia"), ("función contemplativa", "uso de un objeto para ser mirado por sí mismo"), ("fenómeno histórico", "hecho o proceso que influye en un cambio social"), ("impacto", "efecto de un fenómeno en las personas y las prácticas")],
    worked=[
        ("Identificar una función", "En el Momento 1 de una ficha parecida, las máscaras se guardan en el templo y se usan en ceremonias. ¿Qué función tienen?",
         ["Mira para qué se usan: para una ceremonia de cosecha.", "Eso es una función ritual."],
         "Función ritual"),
        ("Nombrar el tipo de fenómeno", "Un taller ficticio empieza a copiar máscaras con moldes. ¿Qué tipo de fenómeno es?",
         ["Observa qué cambió: una técnica para producir copias.", "Eso corresponde a un cambio tecnológico."],
         "Un cambio tecnológico"),
    ],
    mistakes=[("Creer que las ideas sobre el arte son las mismas en todas las épocas.", "Se proyecta el presente sobre el pasado.", "Pregunta qué función y qué creencias tenía el objeto en su sociedad."),
              ("Explicar un cambio con una sola causa.", "Se simplifica un proceso complejo.", "Busca si influyeron creencias, tecnología y procesos históricos al mismo tiempo.")],
    T=[
        ("abc", "{F} ¿Qué dato de la ficha muestra que, en el Momento 1, las máscaras no se miraban como obras de museo?", "Que se guardaban en el templo y nadie las llamaba «arte»", "Que se vendían en la feria", "Que se exponían con buena luz en vitrinas", "En el Momento 1 eran objetos de ceremonia, guardados en el templo y sin el nombre de «arte»."),
        ("abc", "{F} ¿Qué cambio introduce el Momento 2?", "Se fabrican copias con moldes para venderlas", "Se exhiben en vitrinas", "Las máscaras se usan en la cosecha", "El taller copia con moldes: un cambio técnico que permite producir varias."),
        ("abc", "{F} ¿Qué función se destaca en el Momento 3?", "Contemplativa, porque se expone para ser mirada", "Ritual, porque se usa en cosecha", "Comercial, porque se vende", "El museo las exhibe para que se contemplen."),
        ("abc", "En Estética: ¿qué estudia la historia de la estética?", "Cómo cambian las ideas y las prácticas sobre belleza y arte", "Solo la fecha de nacimiento de los artistas", "Únicamente la técnica de las pinturas", "Su objeto es el cambio de ideas y prácticas en el tiempo."),
        ("abc", "{F} ¿Qué dato del Momento 3 muestra un cambio en la manera de percibir las máscaras?", "Se exponen en vitrinas con buena luz para que la gente las contemple", "Se guardan en el templo", "Se fabrican copias con moldes", "Contemplar las máscaras con buena luz es mirarlas por sí mismas, a diferencia del uso ritual."),
        ("ab", "{F} ¿Qué fenómeno ayudó a que las máscaras llegaran a un público más amplio?", "Las copias vendidas en la feria", "El silencio del templo", "Las copias circulaban por la feria, mientras el templo las mantenía reservadas."),
        ("abc", "Una comunidad ficticia prohíbe pintar rostros humanos por una creencia religiosa. ¿Qué tipo de fenómeno influye en el arte?", "Una creencia religiosa", "Un cambio tecnológico", "Un fenómeno natural", "La prohibición proviene de una creencia, que regula las imágenes."),
        ("abc", "Una ciudad ficticia crece y aparecen comerciantes que compran cuadros para sus casas. ¿Qué tipo de fenómeno influye en el arte?", "Un proceso histórico, el crecimiento de la ciudad y de nuevos compradores", "Una creencia religiosa", "Un cambio tecnológico", "El crecimiento urbano y los nuevos compradores son procesos históricos."),
        ("abc", "{F} Un estudiante dice: «Las máscaras siempre fueron arte, igual que ahora». ¿Qué corrección es mejor?", "En el Momento 1 nadie las llamaba arte: tenían función ritual", "Siempre fueron objetos de museo", "Eran un producto comercial desde el Momento 1", "Los hechos del caso muestran que el sentido de las máscaras cambió."),
        ("abc", "{F} Otro estudiante dice: «En el Momento 3 las máscaras ya no son ceremoniales y por eso valen menos». ¿Qué se puede observar?", "Que cambió su función y su manera de ser percibidas, no necesariamente su valor", "Que su valor aumentó porque están en un museo", "Que perdieron todo su sentido", "Cambiar de función no implica automáticamente que valgan menos."),
        ("abc", "{F} ¿Cuál de estas descripciones del público es correcta según la ficha?", "En el Momento 3 la gente contempla las máscaras originales en un museo", "En el Momento 1 las máscaras se vendían en la feria", "En el Momento 2 las máscaras estaban solo dentro del templo", "El museo las expone para que el público las contemple; las otras opciones cambian los momentos."),
        ("abc", "{F} Para explicar el paso del Momento 1 al Momento 3, ¿qué conviene hacer?", "Buscar cómo influyeron creencias, tecnología y procesos históricos", "Elegir la causa más reciente", "Explicarlas solo por su belleza actual", "Los cambios suelen tener varias causas que interactúan."),
        ("abc", "Evalúa: «Como las copias se vendían, las máscaras perdieron todo sentido para la comunidad». ¿Qué falla?", "Supone un efecto sin evidencia, pues el caso no dice que haya perdido sentido para todos", "Que las copias no se vendían", "Que el templo cerró", "Un efecto debe apoyarse en evidencia del caso."),
    ],
    ctx=("abc", "Un centro cultural ficticio de Valle Alto prepara una sala sobre las máscaras. Una persona quiere que digan solo «obra maestra». Otra propone contar también su uso en la cosecha. ¿Qué enfoque histórico es más completo?", "Presentar su función ritual original y su función actual de contemplación", "Mostrarlas sin ningún texto", "Presentar solo su valor de venta", "Un enfoque histórico explica los cambios de función y de percepción."),
    sc=[
        ("En Estética: ¿qué es la función ritual de un objeto?", "Su uso en una ceremonia ligada a una creencia", "No se limita a ser mirado por sí mismo."),
        ("¿Cuáles son los tres tipos de fenómenos que influyen en la historia de la estética?", "Creencias religiosas, cambios tecnológicos y procesos históricos", "Son los tres tipos que se trabajan en esta clase."),
        ("¿Por qué no basta una sola causa para explicar un cambio?", "Porque los cambios suelen tener varias causas que interactúan", "Reducirlo a una sola causa simplifica demasiado."),
    ],
    op=("Elige uno de estos objetos ficticios: (1) una flauta usada en fiestas del pueblo y hoy tocada en conciertos, (2) un tejido usado como manta que hoy cuelga de un muro de museo, (3) una canción de cuna que hoy se graba y se escucha en plataformas. "
        "Escribe su función en un momento anterior, su función actual, qué tipo de fenómeno pudo influir (creencia, tecnología o proceso histórico) y una pregunta de investigación sobre el cambio.",
        "Objeto 2. Antes: manta de uso cotidiano. Ahora: obra para ser contemplada en un muro. Fenómeno: un proceso histórico, el surgimiento de museos. Pregunta: ¿qué cambió en la mirada de quienes lo ven ahora?",
        ["indica la función anterior y la actual", "nombra un tipo de fenómeno posible", "formula una pregunta de investigación", "evita presentar el pasado con ideas de hoy"],
        ["ficha con función anterior, actual, fenómeno y pregunta"],
        ["suponer que la función siempre fue la actual", "dar una causa única", "formular una pregunta que se responde con sí o no"],
        "Pregunta: «¿para qué lo usaba la gente antes y para qué ahora?». Pídele que la escriba con dos verbos."),
    reinforce="Elige un objeto de tu casa que haya cambiado de uso con los años y describe la función antes y ahora.",
    extend="Explica por qué un objeto puede ser valioso para una comunidad aunque no se lo llame «arte».",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 12 (casos ficticios y glosario). Caso A: un monasterio imaginario encarga manuscritos decorados con motivos religiosos y los usa en sus ceremonias. "
     "Caso B: un taller imaginario imprime láminas con una prensa, de manera que muchas casas pueden tener una imagen. "
     "Caso C: una república imaginaria crea una academia que decide qué obras se enseñan y se premian. "
     "Glosario: mecenazgo = apoyo económico de una persona o institución poderosa a quien crea; reproducción técnica = hacer varias copias de una obra con un procedimiento; institución = organización estable que regula una práctica (museo, academia); canon = conjunto de obras que una sociedad considera ejemplares; secularización = pérdida de influencia de la religión en la vida pública.")
build(
    O3, 2, F,
    use="Aprenderé a definir mecenazgo, reproducción técnica, institución, canon y secularización, y a usarlos para explicar fenómenos que han influido en la historia de la estética.",
    prior=["Reconozco función ritual y función contemplativa.", "Distingo creencias, tecnología y procesos históricos.", "Sé explicar causas y efectos."],
    explain=[
        "Los conceptos de esta clase ayudan a nombrar fenómenos. El mecenazgo es el apoyo económico de alguien poderoso a quien crea; influye en qué obras se hacen y con qué temas. La reproducción técnica es la posibilidad de hacer muchas copias de una obra, lo que cambia quién tiene acceso a ella.",
        "Una institución es una organización estable que regula una práctica, como un museo, que decide qué exhibir, o una academia, que decide qué se enseña. El canon es el conjunto de obras que una sociedad considera ejemplares y que se estudian o se imitan. Quienes forman parte de las instituciones influyen en cómo se arma el canon.",
        "La secularización es la pérdida de influencia de la religión en la vida pública. Cuando ocurre, el arte puede dejar de depender de encargos religiosos y volcarse a otros temas y compradores. Estos conceptos no explican por sí solos un cambio: sirven para describirlo con precisión y preguntarse por sus causas.",
    ],
    vocab=[("mecenazgo", "apoyo económico de una persona o institución poderosa a quien crea"), ("reproducción técnica", "hacer varias copias de una obra con un procedimiento"), ("institución", "organización estable que regula una práctica, como un museo o una academia"), ("canon", "conjunto de obras que una sociedad considera ejemplares"), ("secularización", "pérdida de influencia de la religión en la vida pública")],
    worked=[
        ("Aplicar el concepto de mecenazgo", "Un comerciante ficticio paga a una pintora para que decore el salón del gremio con escenas de su historia. ¿Qué concepto describe esa relación?",
         ["Mira quién paga: una persona con recursos.", "Mira qué recibe: obras para un fin determinado. Eso es mecenazgo."],
         "Mecenazgo"),
        ("Aplicar el concepto de canon", "Una academia ficticia publica una lista de obras que todo estudiante debe estudiar. ¿Qué concepto describe esa lista?",
         ["Observa qué es la lista: obras consideradas ejemplares por una institución.", "Eso es un canon."],
         "Canon"),
    ],
    mistakes=[("Creer que un canon es natural y siempre fue el mismo.", "Se olvida que lo arman instituciones y personas en cada época.", "Pregunta quién lo definió y con qué criterios."),
              ("Confundir reproducción técnica con falsificación.", "Se mezclan copias autorizadas y engaños.", "Una reproducción técnica es una copia hecha con un procedimiento; la falsificación se hace para engañar.")],
    T=[
        ("abc", "{F} ¿Qué concepto describe la relación del monasterio con quienes hacen manuscritos?", "Mecenazgo", "Canon", "Secularización", "El monasterio encarga y financia obras para su uso."),
        ("abc", "{F} ¿Qué concepto describe lo que hace el taller del Caso B?", "Reproducción técnica", "Mecenazgo", "Canon", "Imprime muchas láminas con una prensa."),
        ("abc", "{F} ¿Qué es la academia del Caso C?", "Una institución que regula una práctica artística", "Un tipo de reproducción técnica", "Un mecenas", "Decide qué se enseña y premia, es decir, regula una práctica."),
        ("En Estética: ¿cómo se llama la pérdida de influencia de la religión en la vida pública?", "Secularización", "Es el término que designa ese fenómeno."),
        ("abc", "{F} ¿Qué efecto de la reproducción técnica se ve en el Caso B?", "Muchas casas pueden tener una imagen", "Solo el monasterio tiene imágenes", "Se prohíben las imágenes", "Con copias, más gente accede a las imágenes."),
        ("ab", "{F} ¿Qué relación hay entre la academia del Caso C y el canon?", "Al decidir qué se enseña y se premia, la academia influye en cómo se arma el canon", "El canon se arma solo, sin que ninguna institución participe", "Una institución que decide qué obras se enseñan y premian participa en formar el canon."),
        ("abc", "Un estudio ficticio dice que, cuando la ciudad se volvió menos dependiente de la religión, los pintores empezaron a pintar escenas del mercado. ¿Qué concepto se usa?", "Secularización", "Mecenazgo", "Canon", "Describe la menor influencia religiosa y un cambio de temas."),
        ("abc", "Una empresa ficticia compra cuadros y financia a jóvenes pintores sin pedir temas. ¿Qué concepto describe esa relación?", "Mecenazgo", "Reproducción técnica", "Canon", "Describe el apoyo económico a quienes crean obras."),
        ("abc", "{F} Un estudiante dice: «El canon del Caso C es la lista natural de las mejores obras». ¿Qué le falta considerar?", "Que una institución, en un momento, decidió qué incluir y qué dejar fuera", "Que el canon es una lista de obras de un solo autor", "Que el canon no puede cambiar nunca", "Un canon lo arman personas e instituciones con criterios."),
        ("abc", "{F} Otro estudiante dice: «Las láminas del Caso B son falsificaciones». ¿Qué corrección es mejor?", "Son reproducciones técnicas; no hay engaño en el caso", "Son mecenazgo", "Son un canon", "El caso describe copias hechas con una prensa, no engaños."),
        ("abc", "{F} Si un monasterio como el del Caso A dejara de encargar manuscritos, ¿qué podría pasar con quienes los hacían?", "Podrían buscar otros compradores o mecenas, como talleres o comerciantes", "Seguirían trabajando igual que antes con los mismos temas", "Dejarían de crear obras de inmediato", "Sin ese encargo, tendrían que depender de otras fuentes de apoyo."),
        ("abc", "{F} ¿Cuál de estas afirmaciones es sólida?", "Para explicar cambios del arte conviene combinar mecenazgo, reproducción técnica e instituciones", "Un solo concepto basta para explicar todo", "Los conceptos solo sirven para nombrar épocas", "Los conceptos describen distintos aspectos que se combinan."),
        ("abc", "Una museóloga ficticia dice: «Con las reproducciones técnicas se amplía el acceso, pero también puede cambiar lo que se aprecia de una obra». ¿Cuál es el sentido de «puede cambiar»?", "Que las copias podrían alterar cómo se percibe el original", "Que el original pierde todo su valor", "Que las copias son siempre falsificaciones", "Es una hipótesis sobre el efecto de la reproducción en la percepción."),
    ],
    ctx=("abc", "Un museo comunitario ficticio quiere explicar por qué hay tantas obras religiosas en su sala y pocas de la vida diaria. ¿Qué concepto le ayuda a explicarlo mejor?", "Mecenazgo, porque quienes encargaban y pagaban obras eran instituciones religiosas", "Reproducción técnica, porque había una prensa", "Secularización, porque ya no había religión", "El tipo de encargo que financiaba las obras explica su temática."),
    sc=[
        ("En Estética: ¿qué es el mecenazgo?", "El apoyo económico de una persona o institución poderosa a quien crea", "Influye en qué obras se hacen."),
        ("En Estética: ¿Qué es un canon?", "Un conjunto de obras que una sociedad considera ejemplares", "Se arma por decisiones de personas e instituciones."),
        ("¿Qué es la reproducción técnica?", "Hacer varias copias de una obra con un procedimiento", "Cambia quién tiene acceso a las obras."),
    ],
    op=("Elige una de estas situaciones ficticias: (1) un empresario financia un teatro en un pueblo, (2) una escuela de música decide qué piezas deben estudiar los alumnos, (3) una imprenta barata produce afiches de pintura. "
        "Indica qué concepto de la clase la describe, qué efecto podría tener en los artistas o en el público y una pregunta que te harías para comprobar ese efecto.",
        "Situación 2. Concepto: canon. Efecto: las piezas incluidas se aprenden más y otras quedan fuera. Pregunta: ¿quién decidió la lista y con qué criterios?",
        ["usa el concepto correcto", "describe un efecto plausible", "formula una pregunta que se puede investigar", "no generaliza sin evidencia"],
        ["ficha con concepto, efecto y pregunta"],
        ["usar un concepto que no corresponde", "afirmar un efecto sin justificarlo", "formular una pregunta de sí o no"],
        "Pregunta: «¿qué palabra de la ficha muestra que este concepto es el correcto?». Pídele que la cite."),
    reinforce="Describe un caso de tu entorno (un concurso, una lista de lecturas, un museo local) y di qué concepto de la clase le corresponde.",
    extend="Explica por qué un canon puede cambiar con el tiempo y qué fenómenos podrían cambiarlo.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 13 (línea de tiempo ficticia de Valle Alto). Período 1: el templo encarga las imágenes y fija reglas estrictas: los personajes se pintan de frente y con tamaño según su importancia. "
     "Período 2: llega una máquina de grabar y se producen láminas baratas; muchas casas tienen imágenes. "
     "Período 3: la ciudad se vuelve menos dependiente del templo; los pintores trabajan para ferias y coleccionistas y eligen temas libres, como paisajes y escenas del mercado. "
     "Tabla de reconstrucción: período / quién financia / qué técnica / qué temas / quién mira.")
build(
    O3, 3, F,
    use="Aprenderé a reconstruir una secuencia histórica ordenando períodos, causas y efectos, y a explicar cómo un cambio influye en otro sin atribuirle una causa única.",
    prior=["Defino mecenazgo, reproducción técnica y secularización.", "Ordeno hechos en una secuencia.", "Distingo causa y efecto."],
    explain=[
        "Reconstruir una secuencia histórica es ordenar períodos y señalar qué cambió de uno a otro. Una tabla ayuda a comparar con las mismas preguntas: quién financia, qué técnica se usa, qué temas aparecen y quién mira. Así se ve qué factores cambian juntos.",
        "Una causa es un hecho que contribuye a que ocurra otro, el efecto. Los cambios históricos tienen causas múltiples: una creencia, una técnica nueva y un cambio en quién compra pueden actuar al mismo tiempo. Decir que algo es «causa» exige mostrar cómo contribuye, no solo que ocurrió antes.",
        "También hay que distinguir lo que cambió de lo que permaneció. En un período puede cambiar la técnica y mantenerse el tema, o cambiar el público y mantenerse la técnica. Una buena reconstrucción informa ambas cosas y usa palabras prudentes como «contribuyó», «favoreció» o «permitió», en vez de afirmar que una sola causa lo explica todo.",
    ],
    vocab=[("secuencia histórica", "serie ordenada de períodos con sus cambios"), ("causa", "hecho que contribuye a que ocurra otro"), ("efecto", "resultado de una causa"), ("causas múltiples", "varios factores que actúan juntos"), ("permanencia", "lo que se mantiene a pesar de los cambios")],
    worked=[
        ("Completar una fila de la tabla", "Para el Período 2 de una ficha parecida (máquina de grabar y láminas baratas), ¿qué técnica se usa y quién mira?",
         ["Busca la técnica: grabado con máquina.", "Busca quién mira: muchas casas tienen imágenes, es decir, un público más amplio."],
         "Técnica: grabado con máquina; mira un público más amplio"),
        ("Redactar con prudencia", "Redacta con verbo prudente la relación entre la máquina de grabar y los nuevos compradores.",
         ["Observa que ocurrieron en el mismo período, pero eso no prueba que una cause a la otra.", "Redacta: la máquina de grabar favoreció que más personas accedieran a imágenes."],
         "La máquina de grabar favoreció que más personas accedieran a imágenes"),
    ],
    mistakes=[("Decir que algo es causa solo porque ocurrió antes.", "Se confunde orden en el tiempo con causalidad.", "Muestra cómo ese hecho contribuyó al otro, no solo que fue anterior."),
              ("Omitir lo que permaneció entre períodos.", "Se cuenta solo el cambio.", "Anota también lo que se mantuvo.")],
    T=[
        ("abc", "{F} Según la tabla, ¿quién financia en el Período 1?", "El templo", "Los coleccionistas", "Las ferias", "El templo encarga y fija reglas de las imágenes."),
        ("abc", "{F} ¿Qué regla de composición fija el templo en el Período 1?", "Los personajes se pintan de frente y con tamaño según su importancia", "Los pintores eligen temas libres", "Las láminas deben ser baratas", "Es la regla que la ficha atribuye al Período 1."),
        ("abc", "{F} ¿Qué temas aparecen en el Período 3?", "Temas libres, como paisajes y escenas del mercado", "Solo retratos de personas importantes", "Solo escenas de la ceremonia de cosecha", "La ficha dice que los pintores eligen temas libres."),
        ("abc", "{F} ¿Para quiénes trabajan los pintores en el Período 3?", "Para ferias y coleccionistas", "Para el templo", "Para una academia", "La ficha dice que los pintores trabajan para ferias y coleccionistas."),
        ("abc", "En Estética: ¿qué es una secuencia histórica?", "Una serie ordenada de períodos con sus cambios", "Una lista de obras ejemplares", "Un tipo de encargo de obras", "Se ordena el tiempo y se anotan los cambios."),
        ("ab", "{F} ¿Qué relación entre la máquina de grabar y los compradores nuevos permite afirmar la ficha?", "Que aparecen en períodos consecutivos, pero la ficha no prueba que una cause a la otra", "Que la máquina causó que existieran los compradores", "Aparecer en períodos consecutivos no prueba por sí solo una relación de causa y efecto."),
        ("abc", "{F} Una estudiante escribe: «La máquina de grabar causó los temas libres». ¿Qué hay que revisar?", "Si hay evidencia de que la máquina contribuyó a ese cambio, además de otras causas", "Que la máquina apareció antes que los nuevos temas", "Que los temas libres son pocos", "Una causa se afirma mostrando cómo contribuye, no solo que ocurrió antes."),
        ("abc", "{F} ¿Cuál es una formulación prudente sobre el Período 3?", "El menor peso del templo favoreció que los pintores eligieran temas libres", "La máquina de grabar causó por sí sola los temas libres", "El templo dejó de importar y por eso nacieron los temas libres", "El verbo «favoreció» indica contribución sin afirmar una causa única."),
        ("abc", "{F} Si el Período 3 hubiera mantenido la regla de pintar de frente y con tamaño según importancia, ¿qué habría permanecido?", "Una convención del Período 1", "La máquina de grabar", "La feria", "Esa regla era del Período 1."),
        ("abc", "{F} Un estudiante dice: «Solo cambió la técnica entre los períodos 1 y 3». ¿Qué corrección es mejor?", "También cambiaron quién financia, qué temas aparecen y quién mira", "Solo cambió quién financia", "Solo cambió quién mira", "La tabla muestra cambios en varias dimensiones."),
        ("abc", "{F} ¿Qué factores podrían haber actuado juntos para producir los temas libres del Período 3?", "Menor peso del templo, nuevos compradores y láminas baratas", "Solo el mecenazgo del templo", "Solo la técnica de grabado", "Los cambios históricos suelen tener causas múltiples."),
        ("abc", "{F} ¿Cuál de estos rasgos aparece por primera vez en el Período 3?", "Los pintores eligen temas libres, como paisajes y escenas del mercado", "El templo encarga las imágenes", "Llega una máquina de grabar", "Los temas libres se mencionan solo en el Período 3; las otras opciones son de los períodos 1 y 2."),
        ("abc", "{F} Un historiador ficticio afirma que la máquina de grabar fue la única causa del cambio de temas. ¿Qué objeción es la más razonable?", "Que también cambiaron el financiamiento y los compradores, por lo que hubo otras causas", "Que la máquina produjo demasiadas láminas", "Que nadie compraba láminas", "Una explicación monocausal ignora otros cambios."),
    ],
    ctx=("abc", "Un museo ficticio de Valle Alto prepara un panel que explique el paso del Período 1 al 3. Un guía propone: «La máquina cambió todo». Otra: «Cambiaron quién pagaba, la técnica y quién miraba». ¿Qué enunciado reconstruye mejor la secuencia?", "El de la segunda persona, porque indica varios cambios que actuaron juntos", "El del guía, porque es más claro y corto", "Ambos por igual", "La reconstrucción debe mostrar causas múltiples."),
    sc=[
        ("En Estética: ¿qué son las causas múltiples?", "Varios factores que actúan juntos para producir un cambio", "Evitan explicar un cambio con una sola razón."),
        ("¿Por qué «ocurrió antes» no basta para afirmar que algo es causa?", "Porque hay que mostrar cómo contribuyó al efecto", "Que algo ocurra antes no prueba que sea causa."),
        ("¿Qué es la permanencia?", "Lo que se mantiene a pesar de los cambios", "Se anota junto a los cambios."),
    ],
    op=("Reconstruye en una tabla los tres períodos de la ficha con las cinco columnas (período, quién financia, qué técnica, qué temas, quién mira). Después escribe tres frases prudentes (con «favoreció», «contribuyó» o «permitió») que relacionen cambios entre períodos, y una cosa que haya permanecido.",
        "Frase: el menor peso del templo favoreció que los pintores trabajaran para ferias y coleccionistas. La máquina de grabar permitió que más casas tuvieran imágenes. Permaneció: la existencia de imágenes en la vida cotidiana.",
        ["la tabla está completa y es fiel a la ficha", "usa verbos prudentes", "las frases relacionan al menos dos factores", "indica algo que permaneció"],
        ["tabla de tres filas y cinco columnas, tres frases y una permanencia"],
        ["usar verbos como «causó» sin evidencia", "dejar celdas vacías", "olvidar anotar permanencias"],
        "Pregunta: «¿qué palabra muestra que no afirmas una causa única?». Pídele que subraye el verbo prudente."),
    reinforce="Haz una línea de tiempo de tres momentos sobre cómo ha cambiado la música que oyes tú y tu familia, y rotula qué cambió y qué permaneció.",
    extend="Explica por qué un cambio tecnológico puede favorecer cambios en el arte sin ser su única causa.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 14 (argumentos originales sobre Valle Alto). Argumento A: «Después de que llegó la máquina de grabar, aparecieron nuevos temas; por lo tanto, la máquina causó los nuevos temas.» "
     "Argumento B: «Los nuevos temas se deben solo a la tecnología.» "
     "Argumento C: «Talleres que no tenían máquina también cambiaron sus temas, así que la máquina no fue la única causa; probablemente influyó el cambio de compradores.» "
     "Criterios de impacto: alcance (a cuántas personas afectó), profundidad (cuánto cambió) y duración (cuánto tiempo se mantuvo el efecto).")
build(
    O3, 4, F,
    use="Aprenderé a formular y evaluar argumentos sobre el impacto de un fenómeno en la historia de la estética con criterios de alcance, profundidad y duración, y a evitar falacias causales.",
    prior=["Reconstruyo secuencias históricas.", "Distingo causas múltiples y permanencias.", "Sé qué es una premisa y una conclusión."],
    explain=[
        "Evaluar el impacto de un fenómeno es preguntar cuánto cambió las cosas. Tres criterios ayudan: el alcance, es decir, a cuántas personas afectó; la profundidad, o sea, cuánto cambió la práctica; y la duración, cuánto se mantuvo el efecto. Un fenómeno puede tener gran alcance y poca profundidad, o al revés.",
        "Los argumentos causales tienen errores típicos. La falacia post hoc concluye que A causó B solo porque A ocurrió antes que B. La explicación monocausal atribuye un cambio a una única causa cuando hubo varias. Para evitarlas, se busca evidencia de cómo actuó la causa, se compara con casos en que no estuvo presente y se consideran otras causas posibles.",
        "Un buen argumento sobre impacto indica qué fenómeno se evalúa, qué criterio usa, qué evidencia da y qué otras causas descarta o admite. También reconoce los límites de lo que se sabe. No se trata de decidir si algo fue «bueno» o «malo», sino de mostrar con razones cuánto cambió y para quién.",
    ],
    vocab=[("alcance", "a cuántas personas afectó un fenómeno"), ("profundidad", "cuánto cambió la práctica a causa de un fenómeno"), ("duración", "cuánto tiempo se mantuvo el efecto"), ("falacia post hoc", "concluir que A causó B solo porque A ocurrió antes"), ("explicación monocausal", "atribuir un cambio a una única causa")],
    worked=[
        ("Detectar post hoc", "«Se instaló una biblioteca ficticia en el pueblo y, después, se pintaron más murales; la biblioteca causó los murales». ¿Qué falacia es?",
         ["Mira la base: un hecho ocurrió antes que otro.", "No hay evidencia de cómo la biblioteca contribuyó; es post hoc."],
         "Falacia post hoc"),
        ("Aplicar un criterio de impacto", "Una técnica ficticia de impresión permitió que 1.000 familias tuvieran láminas, pero las familias pronto dejaron de comprarlas. ¿Cómo fue su alcance y cómo su duración?",
         ["El alcance fue amplio: llegó a 1.000 familias.", "La duración fue breve: se dejaron de comprar pronto."],
         "Alcance amplio y duración breve"),
    ],
    mistakes=[("Medir el impacto solo por el número de obras producidas.", "Se olvida la profundidad y la duración.", "Evalúa alcance, profundidad y duración por separado."),
              ("Descartar toda causa tecnológica por ser insuficiente.", "Se pasa de «no única» a «irrelevante».", "Reconoce que una causa puede contribuir sin ser la única.")],
    T=[
        ("abc", "{F} ¿Qué falacia comete el Argumento A?", "Post hoc: concluye causa solo por haber ocurrido antes", "Ataque a la persona", "Apelación a la mayoría", "Pasa de «después de» a «a causa de» sin evidencia."),
        ("abc", "{F} ¿Qué error comete el Argumento B?", "Es una explicación monocausal", "Es una falacia post hoc", "Es una apelación a la mayoría", "Atribuye los temas solo a la tecnología."),
        ("abc", "{F} ¿Qué hace de mejor el Argumento C?", "Compara con talleres sin máquina y admite otras causas", "Repite que la máquina fue la causa", "Ataca a quienes defienden la máquina", "Usa un caso comparativo y reconoce causas múltiples."),
        ("En Estética: ¿cómo se llama el criterio de impacto que mide a cuántas personas afectó un fenómeno?", "Alcance", "Es el criterio que se refiere al número de personas afectadas."),
        ("abc", "{F} ¿Qué criterio de impacto evalúa cuánto cambió la práctica?", "Profundidad", "Alcance", "Duración", "La profundidad mide el grado de cambio en la práctica."),
        ("ab", "Una moda ficticia de decorar con un dibujo duró solo una temporada. ¿Qué criterio de impacto fue débil?", "La duración", "El alcance", "El dato dice que el efecto duró poco, lo cual pesa sobre la duración."),
        ("abc", "Un cambio ficticio hizo que los pintores de una ciudad cambiaran por completo cómo trabajaban, pero solo en un taller pequeño. ¿Qué se puede decir?", "Tuvo gran profundidad y poco alcance", "Tuvo gran alcance y poca profundidad", "No tuvo ningún impacto", "El cambio fue grande en la práctica, pero afectó a pocos."),
        ("abc", "{F} Un estudiante dice: «Como los talleres sin máquina también cambiaron, la tecnología no tuvo ningún papel». ¿Qué falla?", "Pasa de «no única» a «ningún papel», sin mostrar que no contribuyó", "Usa un caso de talleres", "Confunde alcance con profundidad", "Que haya otras causas no implica que una de ellas no contribuyera."),
        ("abc", "{F} ¿Qué evidencia reforzaría el Argumento C?", "Mostrar que en los talleres sin máquina se dieron cambios de compradores antes de los temas", "Mostrar que hubo muchas láminas en el Período 3", "Citar la opinión de un historiador sin datos", "Un orden temporal y un mecanismo plausible dan más fuerza a la causa."),
        ("abc", "{F} Evalúa el Argumento B con tu criterio: ¿es sólido?", "No: usa «solo» sin descartar otras causas posibles", "Sí: la tecnología fue lo primero que ocurrió", "Sí: porque es más simple", "La palabra «solo» exige descartar otras causas."),
        ("abc", "Una investigadora ficticia dice: «La televisión redujo la asistencia a conciertos. Lo sé porque primero vino la televisión y después bajó la asistencia». ¿Cómo mejorar su argumento?", "Compararía con localidades sin televisión y consideraría otras causas", "Concluiría que la televisión no tuvo efecto alguno", "Agregaría más años de datos sin comparar", "Comparar y considerar otras causas reduce el riesgo de post hoc."),
        ("abc", "Un panel sobre Valle Alto dice: «La máquina de grabar tuvo un impacto de gran alcance». Un dato de ejemplo de la sociedad ficticia es que muchas casas tuvieron láminas baratas. ¿Qué criterio apoya ese dato?", "El alcance, porque llegó a muchas personas", "La duración, porque el efecto se mantuvo", "La profundidad, porque cambió por completo la práctica", "El número de casas que recibieron láminas mide a cuántas personas afectó, es decir, el alcance."),
        ("abc", "Dos estudiantes evalúan una misma innovación ficticia: una dice que su impacto fue profundo y la otra que fue superficial. ¿Cuál es la mejor manera de resolver el desacuerdo?", "Pedir la evidencia de cómo cambió la práctica y comparar según el criterio de profundidad", "Votar sin más", "Descartar a una de las dos", "Se resuelve contrastando evidencia según criterios compartidos."),
    ],
    ctx=("abc", "Un diario escolar ficticio titula: «Desde que llegaron los videojuegos de arte, se visitan menos museos». Un lector responde que no hay evidencia de que lo uno cause lo otro. ¿Qué falacia señala?", "Post hoc: concluir causa solo por la secuencia temporal", "Ataque a la persona", "Apelación a la mayoría", "Pasar de la secuencia a la causa sin evidencia es post hoc."),
    sc=[
        ("En Estética: ¿qué es la falacia post hoc?", "Concluir que A causó B solo porque A ocurrió antes", "Ordena en el tiempo, pero no prueba causa."),
        ("¿Cuáles son los tres criterios de impacto de la clase?", "Alcance, profundidad y duración", "Permiten evaluar cuánto cambió un fenómeno."),
        ("¿Por qué es débil una explicación monocausal?", "Porque ignora otros factores que pudieron actuar juntos", "Los cambios históricos suelen tener varias causas."),
    ],
    op=("Elige uno de estos fenómenos ficticios: (1) las radios llegan a un valle y las canciones locales se vuelven populares, (2) una nueva ley obliga a que cada escuela tenga un taller de arte, (3) una plaza renovada incorpora un escenario abierto. "
        "Escribe un argumento breve sobre su impacto con: criterio de impacto usado, evidencia de ejemplo (rotulada como ficticia), otra causa posible y una frase que evite la falacia post hoc.",
        "Fenómeno 2. Criterio: alcance. Evidencia de ejemplo (ficticia): 12 escuelas abrieron talleres. Otra causa: interés previo de las familias. Frase prudente: la ley favoreció que más estudiantes accedieran a talleres, aunque el interés previo también influyó.",
        ["usa al menos un criterio de impacto", "la evidencia está rotulada como ficticia", "señala otra causa posible", "usa un verbo prudente"],
        ["argumento breve con criterio, evidencia, otra causa y frase prudente"],
        ["afirmar causa por orden temporal", "presentar la evidencia como real", "no señalar ninguna otra causa"],
        "Pregunta: «¿qué otro factor pudo producir lo mismo?». Pídele que lo agregue como otra causa."),
    reinforce="Elige un cambio reciente en tu escuela y escribe una frase que lo vincule con una causa, usando un verbo prudente.",
    extend="Explica con un ejemplo por qué un fenómeno puede tener gran alcance y poca duración.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 15 (tesis y objeciones originales). Tesis T: «La tecnología explica los cambios del arte: cada vez que aparece una técnica nueva, cambia lo que se considera arte.» "
     "Objeción 1: «Hay cambios en el arte sin cambio técnico: un nuevo grupo de compradores puede cambiar los temas con las mismas técnicas.» "
     "Objeción 2: «Decir que las máscaras de Valle Alto ya eran arte en el Período 1 porque hoy nos parecen bellas es mirar el pasado con ojos de hoy.» "
     "Réplica sugerida a la Objeción 1: «Reconozco que la tecnología no es la única causa; sostengo que suele ser una condición que favorece cambios, junto con otros factores.»")
build(
    O3, 5, F,
    use="Aprenderé a responder objeciones comunes al explicar fenómenos históricos de la estética, como el determinismo tecnológico y el anacronismo, y a evaluar el impacto con más prudencia.",
    prior=["Evalúo impacto con alcance, profundidad y duración.", "Evito post hoc y monocausalidad.", "Sé formular una réplica."],
    explain=[
        "El determinismo tecnológico es la idea de que la tecnología determina por sí sola los cambios sociales y artísticos. Es una tesis fuerte que suele enfrentar contraejemplos: cambios que ocurren sin nueva técnica, y nuevas técnicas que no producen cambios. Una versión más moderada sostiene que la tecnología favorece o condiciona, pero no decide sola.",
        "El anacronismo consiste en juzgar o describir el pasado con ideas, valores o conceptos del presente, como llamar «arte» a un objeto que su sociedad no consideraba así. Para evitarlo, se pregunta qué sentido tenía el objeto para quienes lo usaban y se distinguen los conceptos de la época de los nuestros.",
        "Responder a estas objeciones mejora una explicación. Puede ser necesario matizar la tesis, admitir un límite o aclarar qué se afirma exactamente. Una explicación histórica sólida no promete certezas absolutas: ofrece razones, indica su alcance y reconoce lo que podría revisarse con nueva evidencia.",
    ],
    vocab=[("determinismo tecnológico", "idea de que la tecnología determina por sí sola los cambios"), ("anacronismo", "juzgar el pasado con ideas o conceptos del presente"), ("matizar", "precisar una tesis para que no afirme más de lo que puede sostener"), ("condición favorecedora", "factor que facilita un cambio sin decidirlo por sí solo")],
    worked=[
        ("Reconocer el anacronismo", "«Los antiguos pintores de Valle Alto hacían arte abstracto, igual que hoy». ¿Cuál es el problema?",
         ["Busca qué se proyecta: un concepto de hoy, arte abstracto, sobre el pasado.", "No hay evidencia de que ese concepto existiera; es anacronismo."],
         "Anacronismo"),
        ("Matizar una tesis", "Matiza la tesis «Las imprentas cambiaron el arte» para que sea más prudente.",
         ["Identifica el exceso: afirma que la imprenta fue la causa del cambio del arte.", "Matiza: las imprentas favorecieron cambios en cómo el arte circulaba y quién lo veía, junto con otros factores."],
         "Las imprentas favorecieron cambios en cómo circulaba el arte, junto con otros factores"),
    ],
    mistakes=[("Defender una tesis fuerte ignorando los contraejemplos.", "Se confunde firmeza con rigidez.", "Si hay contraejemplos, matiza la tesis."),
              ("Describir una práctica antigua con palabras que su época no usaba, sin avisarlo.", "Se proyecta el presente en el pasado.", "Indica qué sentido tenía para quienes la practicaban.")],
    T=[
        ("abc", "{F} ¿Qué sostiene la Tesis T?", "Que la tecnología explica los cambios del arte", "Que la tecnología nunca influye", "Que el arte no cambia", "T dice que cada técnica nueva cambia lo que se considera arte."),
        ("abc", "{F} ¿Qué muestra la Objeción 1?", "Que hay cambios en el arte sin cambio técnico", "Que no existen técnicas nuevas", "Que los compradores no importan", "Un grupo de compradores puede cambiar los temas con las mismas técnicas."),
        ("abc", "{F} ¿De qué problema advierte la Objeción 2?", "Del anacronismo", "Del determinismo tecnológico", "De la falacia post hoc", "Advierte contra mirar el pasado con ojos de hoy."),
        ("En Estética: ¿cómo se llama la idea de que la tecnología determina por sí sola los cambios?", "Determinismo tecnológico", "Es el nombre de esa tesis fuerte sobre la tecnología."),
        ("abc", "{F} ¿Qué hace la réplica sugerida a la Objeción 1?", "Acepta el límite y modera la tesis: la tecnología favorece, junto con otros factores", "Niega todo lo dicho", "Ataca a quien objeta", "Reconoce un límite de la tesis y la hace más prudente."),
        ("ab", "¿Qué es matizar una tesis?", "Precisarla para que no afirme más de lo que puede sostener", "Repetirla con más fuerza", "Es hacerla más prudente y precisa, no más rotunda."),
        ("abc", "Alguien dice: «En la prehistoria, las personas ya hacían arte contemporáneo». ¿Qué problema tiene?", "Anacronismo", "Determinismo tecnológico", "Post hoc", "Proyecta un concepto de hoy sobre otra época."),
        ("abc", "Un grupo ficticio dice: «Como se inventó una tinta nueva, cambiaron todos los estilos». ¿Qué objeción aplicarías?", "Que es determinismo tecnológico: hay que considerar otros factores", "Que es una falacia post hoc", "Que es un ataque a la persona", "Atribuye todo el cambio a una técnica."),
        ("abc", "{F} Un estudiante propone responder a la Objeción 2 diciendo: «Estudiaremos las máscaras según el sentido que les daba la comunidad del Período 1». ¿Qué evita con esto?", "El anacronismo", "El determinismo tecnológico", "La monocausalidad", "Se atiende al sentido que tenía el objeto en su época."),
        ("abc", "{F} Un estudiante dice: «Si hay contraejemplos, la Tesis T es falsa y nada de ella sirve». ¿Qué corrección es mejor?", "Se puede conservar una versión moderada, como condición favorecedora", "Se debe repetir T sin cambios", "Se debe eliminar la tecnología de la explicación", "Una tesis moderada puede resistir objeciones que una fuerte no resiste."),
        ("abc", "{F} Escribe la versión más prudente de la Tesis T.", "La tecnología suele favorecer cambios en el arte, junto con otros factores", "La tecnología explica todo en el arte", "La tecnología no influye en el arte", "La versión prudente reconoce la influencia sin atribuirle todo el cambio."),
        ("abc", "{F} Una investigadora usa en su informe «arte» para hablar del Período 1 y advierte: «aquí usamos esa palabra solo para nosotros». ¿Qué hace?", "Reconoce y limita el anacronismo", "Cae en el determinismo", "Comete post hoc", "Aclara que el concepto es de hoy y no de la comunidad."),
        ("abc", "{F} ¿Qué principio guía mejor las respuestas a las dos objeciones de la ficha?", "Ajustar la explicación a la evidencia y a la época estudiada", "Defender siempre la tesis original", "Evitar las objeciones", "Se responde matizando, con atención a la evidencia y al contexto."),
    ],
    ctx=("abc", "Un documental escolar ficticio dice: «Gracias a la cámara portátil, el arte pasó a ser lo que cualquiera puede hacer». Una estudiante comenta que también influyó el cambio de ideas sobre quién puede ser artista. ¿Qué hace su comentario?", "Matiza una explicación demasiado tecnológica con otro factor", "Repite el determinismo", "Comete anacronismo", "Agrega una causa no tecnológica que complementa la explicación."),
    sc=[
        ("En Estética: ¿qué es el anacronismo?", "Juzgar o describir el pasado con ideas del presente", "Proyecta conceptos actuales sobre otra época."),
        ("¿Qué es el determinismo tecnológico?", "La idea de que la tecnología determina por sí sola los cambios", "Es una tesis fuerte que enfrenta contraejemplos."),
        ("¿Por qué conviene matizar una tesis ante una buena objeción?", "Para que no afirme más de lo que puede sostener", "Una tesis matizada resiste mejor la evidencia."),
    ],
    op=("Toma esta tesis ficticia: «Cada nuevo medio de comunicación hace que el arte cambie por completo». Escribe una objeción (que muestre exceso o anacronismo), una réplica que acepte parte de la objeción y una versión matizada de la tesis. "
        "Si te sirve, usa este contraejemplo: un grupo de bailarines cambió sus rutinas por una nueva idea de grupo, sin usar nuevos medios.",
        "Objeción: los bailarines cambiaron sin nuevos medios. Réplica: acepto que no es la única causa. Tesis matizada: los nuevos medios suelen favorecer cambios en el arte, junto con otros factores como nuevas ideas.",
        ["la objeción es pertinente", "la réplica acepta parte de la objeción", "la tesis matizada es más prudente", "no cambia de tema"],
        ["objeción, réplica y tesis matizada"],
        ["repetir la tesis sin cambios", "no aceptar nada de la objeción", "hacer una tesis tan débil que no afirme nada"],
        "Pregunta: «¿qué palabra de tu nueva tesis la hace más prudente?». Pídele que la marque."),
    reinforce="Busca una frase de un video o noticia que atribuya un cambio cultural a una sola causa y reescríbela más prudente.",
    extend="Explica la diferencia entre determinismo tecnológico y la idea de que la tecnología favorece cambios, y por qué la segunda resiste mejor las objeciones.",
)

O4 = "FI-ESTE-3y4-OAC-04"

# ============================================================ OAC-04, clase 1
F = ("Ficha 16 (caso ficticio). En el pueblo imaginario de Cerro Claro, la compañía de teatro del liceo estrena «La plaza vacía», una obra que muestra con crudeza cómo un alcalde ficticio ignora a sus vecinos. "
     "El concejo debate. Concejala Marta: «Una obra que ridiculiza a una autoridad daña la convivencia; hay que retirarla.» "
     "Concejal Iván: «Una obra vale por lo que hace sentir y pensar; no es tarea del concejo decidir qué se puede mostrar.» "
     "Profesora Elisa: «Quizá la obra ayude a conversar sobre lo que nos pasa; veamos qué efectos tiene antes de decidir.»")
build(
    O4, 1, F,
    use="Aprenderé a plantear el problema de las relaciones entre arte, moral y política con un caso ficticio, a distinguir valores estéticos, morales y políticos y a formular preguntas de investigación.",
    prior=["Reconstruyo posiciones con tesis y razones.", "Distingo juicio de hecho y juicio estético.", "Sé qué es una pregunta de investigación."],
    explain=[
        "La moral es el conjunto de ideas sobre lo bueno y lo malo, lo correcto y lo incorrecto en la conducta. La política es la actividad en que una comunidad toma decisiones colectivas y distribuye poder. El arte se relaciona con ambas porque las obras pueden mostrar conductas, criticar autoridades, proponer valores o ser usadas con fines políticos.",
        "Para estudiar esta relación hay que separar tres tipos de juicio sobre una obra. El juicio estético valora cómo se presenta a los sentidos. El juicio moral valora si lo que muestra o promueve es bueno o malo. El juicio político valora su efecto en el poder o en la convivencia. Una obra puede recibir juicios distintos en cada plano, y mezclarlos sin darse cuenta lleva a confusiones.",
        "Investigar es formular una pregunta precisa, buscar fuentes de distinto tipo, como textos filosóficos y obras, y contrastarlas. Una buena pregunta evita el «sí o no» y se concentra en una relación: por ejemplo, ¿en qué casos una obra que critica a una autoridad contribuye al debate público y en cuáles se considera dañina, y con qué razones?",
    ],
    vocab=[("moral", "ideas sobre lo bueno y lo malo en la conducta"), ("política", "actividad de decisiones colectivas y de distribución del poder"), ("juicio moral", "valoración de si algo es bueno o malo"), ("juicio político", "valoración del efecto de algo en el poder o la convivencia"), ("pregunta de investigación", "pregunta precisa que guía la búsqueda de fuentes")],
    worked=[
        ("Clasificar un juicio", "Un vecino ficticio dice: «El mural es injusto con los pescadores». ¿Qué tipo de juicio es?",
         ["Mira qué valora: una relación de justicia con personas.", "Eso es un juicio moral."],
         "Un juicio moral"),
        ("Mejorar una pregunta", "Mejora la pregunta «¿Es buena la censura?» para convertirla en una pregunta de investigación.",
         ["Nota que se responde con sí o no y no indica qué relación se estudia.", "Reformula: ¿qué razones se han dado a favor y en contra de limitar obras que critican autoridades?"],
         "¿Qué razones se han dado a favor y en contra de limitar obras que critican autoridades?"),
    ],
    mistakes=[("Mezclar el juicio estético con el juicio moral sin darse cuenta.", "Se piensa que una obra bella no puede ser moralmente discutible, o al revés.", "Separa el plano estético, el moral y el político, y evalúa cada uno."),
              ("Formular una pregunta de investigación que se responde con sí o no.", "No guía qué buscar.", "Pregunta por razones, condiciones o relaciones.")],
    T=[
        ("abc", "{F} ¿Qué razón da la concejala Marta para retirar la obra?", "Que ridiculizar a una autoridad daña la convivencia", "Que la obra es mala artísticamente", "Que no tiene público", "Su razón es el daño a la convivencia."),
        ("abc", "{F} ¿Qué sostiene el concejal Iván?", "Que no corresponde al concejo decidir qué se puede mostrar", "Que la obra debe retirarse para cuidar la convivencia", "Que la obra es injusta con el alcalde", "Iván defiende que el concejo no decida qué mostrar."),
        ("abc", "{F} ¿Qué propone la profesora Elisa?", "Mirar los efectos de la obra antes de decidir", "Retirar la obra mientras se discute", "Aprobar la obra sin mirar sus efectos", "Ella pide evaluar efectos antes de decidir."),
        ("En Arte y política: ¿cómo se llama la valoración de si algo es bueno o malo en la conducta?", "Juicio moral", "Es el nombre del juicio que valora lo bueno y lo malo."),
        ("abc", "{F} Marta dice que la obra «daña la convivencia». ¿Qué tipo de juicio es?", "Un juicio político o de convivencia", "Un juicio estético", "Un juicio de hecho sobre medidas", "Valora el efecto de la obra en la convivencia y el poder."),
        ("ab", "Una espectadora ficticia dice: «La escena final es luminosa y armónica». ¿Qué tipo de juicio es?", "Estético", "Moral", "Valora cómo se presenta lo percibido, no si es bueno o malo."),
        ("abc", "Un alumno dice: «Esta obra enseña a tratar con respeto a las personas mayores». ¿Qué tipo de juicio es?", "Un juicio moral", "Un juicio estético", "Un juicio de hecho", "Valora si lo que promueve la obra es bueno, es decir, un juicio moral."),
        ("abc", "{F} ¿Cuál es una buena pregunta de investigación sobre el caso?", "¿En qué condiciones una obra que critica a una autoridad aporta a la convivencia del pueblo y en cuáles se la considera dañina?", "¿Fue buena la actuación?", "¿Cuánto duró la obra?", "Pregunta por razones, no se responde con un sí o un no."),
        ("abc", "{F} Una estudiante dice: «Como la obra es teatral, no tiene relación con la política». ¿Qué corrección es mejor?", "Una obra puede mostrar decisiones colectivas y criticar a una autoridad, por lo que tiene relación con la política", "Tiene razón: el teatro nunca se relaciona con la política", "El teatro solo se relaciona con la moral", "El caso muestra que una obra puede abordar la autoridad y el poder."),
        ("abc", "{F} Un estudiante dice: «Si la obra es de calidad estética, entonces nadie puede criticarla moralmente». ¿Qué falla?", "Mezcla los planos: una obra puede ser valiosa estéticamente y discutible moralmente", "Confunde la moral con la política", "No distingue la obra de su autor", "Un juicio estético no anula el juicio moral."),
        ("abc", "{F} ¿Qué fuentes ayudarían a investigar la pregunta del caso?", "Textos filosóficos sobre arte y moral, y obras que aborden el tema", "Solo la opinión del alcalde", "Solo cuánto costó producir la obra", "Textos filosóficos y obras permiten contrastar razones con ejemplos."),
        ("abc", "{F} ¿Cuál de estas preguntas conviene mejorar porque se responde con sí o no?", "¿Debe el concejo retirar la obra?", "¿Qué razones se dan a favor y en contra de que un concejo limite una obra?", "¿En qué casos una obra que critica a una autoridad aporta al debate?", "Una pregunta de sí o no no guía qué buscar; las otras piden razones o condiciones."),
        ("abc", "{F} Si la profesora Elisa tiene razón en que hay que ver los efectos, ¿qué dato investigaría primero?", "Cómo reaccionó el público y qué conversaciones generó la obra", "Cuánto costó producir la obra", "Quién actuó en cada papel", "Los efectos en el público son lo relevante para su propuesta."),
    ],
    ctx=("abc", "Un periódico escolar ficticio quiere escribir sobre la obra «La plaza vacía». Un redactor propone titular: «Obra bella pero dañina». Otro dice que mezcla planos. ¿Qué mejora el titular?", "Separar el juicio estético del juicio político y explicar cada uno", "Eliminar el juicio estético", "Repetir el titular", "Los planos distintos deben identificarse para no confundir al lector."),
    sc=[
        ("En Arte y política: ¿qué es la política?", "La actividad de decisiones colectivas y de distribución del poder", "El arte puede abordarla, criticarla o ser usado por ella."),
        ("¿Qué diferencia hay entre juicio estético y juicio moral?", "El estético valora cómo se presenta algo; el moral, si es bueno o malo", "Cada uno evalúa un plano distinto de la obra."),
        ("¿Cómo es una buena pregunta de investigación?", "Precisa, no se responde con sí o no y guía la búsqueda de fuentes", "Pregunta por razones, condiciones o relaciones."),
    ],
    op=("Elige uno de estos casos ficticios: (1) un mural en una plaza muestra de forma crítica el trabajo en una mina, (2) una canción de una banda escolar usa palabras fuertes contra la contaminación, (3) un cortometraje muestra una discusión violenta para criticar la violencia. "
        "Escribe un juicio estético, uno moral y uno político posibles sobre el caso y una pregunta de investigación.",
        "Caso 1. Estético: los colores fríos dan sensación de encierro. Moral: muestra con respeto a las personas trabajadoras. Político: pone en discusión las condiciones del trabajo. Pregunta: ¿qué razones se han dado para valorar o limitar murales que critican a una empresa?",
        ["los tres juicios son de planos distintos", "cada juicio es plausible", "la pregunta no se responde con sí o no", "se mantiene neutral frente a posturas partidistas"],
        ["tres juicios y una pregunta de investigación"],
        ["usar el mismo tipo de juicio tres veces", "tomar partido político sin argumento", "formular una pregunta de sí o no"],
        "Pregunta: «¿esta frase valora cómo se ve, si es bueno o el efecto en la comunidad?». Pídele que rotule cada juicio."),
    reinforce="Elige una canción o serie que conozcas (sin copiar letras) y escribe un juicio de cada plano: estético, moral y político.",
    extend="Explica por qué una persona puede admirar una obra estéticamente y, a la vez, discrepar de lo que muestra.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 17 (glosario y casos ficticios). Glosario: moralismo = postura que juzga las obras sobre todo por su efecto moral; autonomismo = postura que sostiene que el valor del arte es independiente de la moral y la política («el arte por el arte»); arte comprometido = arte que busca intervenir en un problema social o político; propaganda = mensaje difundido para persuadir y que busca ganar apoyo más que abrir un debate; censura = prohibir o limitar una obra por su contenido. "
     "Caso A: un cartel ficticio exagera los logros de una autoridad y esconde sus fallas. "
     "Caso B: un cuento ficticio muestra con detalle la vida de una familia migrante, sin dar un mensaje explícito. "
     "Caso C: un teatro ficticio decide prohibir una obra por su contenido, después de la presión de un grupo.")
build(
    O4, 2, F,
    use="Aprenderé a definir moralismo, autonomismo, arte comprometido, propaganda y censura, y a usarlos para analizar casos de relación entre arte, moral y política.",
    prior=["Distingo juicio estético, moral y político.", "Sé formular una pregunta de investigación.", "Reconstruyo posiciones."],
    explain=[
        "Los conceptos de esta clase permiten hablar con precisión. El moralismo juzga las obras sobre todo por su efecto moral. El autonomismo sostiene que el valor del arte es independiente de la moral y la política. El arte comprometido busca intervenir en un problema social o político. Son posturas que dan respuestas distintas a qué debe importar al valorar una obra.",
        "La propaganda es un mensaje difundido para persuadir y ganar apoyo, más que para abrir un debate. A veces usa recursos artísticos, y no siempre es fácil distinguirla del arte comprometido: la diferencia suele estar en si la obra deja espacio a la duda y a la pluralidad, o solo busca imponer un mensaje. La censura es prohibir o limitar una obra por su contenido.",
        "Estos conceptos no se aplican de manera automática. Una obra puede ser comprometida y tener valor estético; otra puede ser propaganda y tener una forma muy cuidada. Por eso se estudian casos, se piden razones y se evita descalificar con etiquetas. Aquí no tomamos partido político: practicamos el análisis.",
    ],
    vocab=[("moralismo", "postura que juzga las obras sobre todo por su efecto moral"), ("autonomismo", "postura que sostiene que el valor del arte es independiente de la moral y la política"), ("arte comprometido", "arte que busca intervenir en un problema social o político"), ("propaganda", "mensaje difundido para persuadir y ganar apoyo más que para abrir un debate"), ("censura", "prohibir o limitar una obra por su contenido")],
    worked=[
        ("Aplicar propaganda", "Un afiche ficticio muestra a una autoridad siempre sonriente y oculta toda crítica. ¿Qué concepto lo describe mejor?",
         ["Mira qué busca: ganar apoyo sin permitir duda.", "Eso corresponde a propaganda."],
         "Propaganda"),
        ("Aplicar autonomismo", "Una crítica ficticia dice: «Esta pieza de cámara debe juzgarse solo por su música, no por quién la encargó». ¿Qué postura supone?",
         ["Mira qué separa: el valor de la obra y lo político.", "Es una postura autonomista."],
         "Autonomismo"),
    ],
    mistakes=[("Usar «propaganda» como insulto para cualquier obra con mensaje.", "Se confunde mensaje con manipulación.", "Pregunta si la obra deja espacio a la duda o solo busca persuadir."),
              ("Creer que censura es lo mismo que cualquier crítica.", "Se mezcla criticar con prohibir o limitar.", "La censura limita o prohíbe; la crítica opina y deja circular la obra.")],
    T=[
        ("abc", "{F} ¿Qué rasgo del Caso A lo acerca a la propaganda?", "Exagera logros y esconde fallas para ganar apoyo", "Muestra con detalle la vida de una familia", "Prohíbe una obra por su contenido", "Busca persuadir y ganar apoyo en lugar de abrir un debate."),
        ("abc", "{F} ¿Qué concepto describe mejor la decisión del Caso C?", "Censura", "Autonomismo", "Propaganda", "Prohibir una obra por su contenido es censura, según el glosario."),
        ("En Arte y política: ¿cómo se llama la postura que dice que el valor del arte es independiente de la moral y la política?", "Autonomismo", "Es el nombre de la postura del «arte por el arte»."),
        ("abc", "{F} ¿Qué rasgo del Caso B lo distingue de una propaganda?", "No impone un mensaje explícito y muestra una vida con detalle", "Exagera logros", "Esconde fallas", "El cuento no busca persuadir con un mensaje cerrado."),
        ("abc", "¿Qué distingue al arte comprometido de la propaganda según la explicación?", "Que deja espacio a la duda y a la pluralidad, mientras la propaganda busca imponer un mensaje", "Que siempre tiene un eslogan", "Que es más corta", "La diferencia está en la apertura al debate."),
        ("ab", "Un crítico ficticio dice: «Una obra es buena solo si enseña buenos valores». ¿Qué postura expresa?", "Moralismo", "Autonomismo", "Juzga la obra principalmente por su efecto moral."),
        ("abc", "Un mural ficticio denuncia la falta de agua en una localidad y propone una asamblea. ¿Qué concepto le conviene?", "Arte comprometido", "Autonomismo", "Censura", "Busca intervenir en un problema social."),
        ("abc", "{F} Si la comunidad del Caso C pidiera presentar la obra y conversar después, ¿qué cambiaría?", "Pasaría de limitar a abrir un debate sobre la obra", "Se convertiría en propaganda", "Se volvería autonomismo", "Presentar y conversar evita la censura y favorece la discusión."),
        ("abc", "{F} Un estudiante dice: «El Caso B no puede ser arte comprometido porque no dice qué pensar». ¿Qué se puede responder?", "Que una obra puede intervenir en un problema mostrando una realidad sin un mensaje cerrado", "Que el compromiso exige un eslogan", "Que no es arte", "El compromiso no exige un mensaje explícito."),
        ("abc", "{F} Otro estudiante dice: «El Caso A tiene una forma muy cuidada, así que no puede ser propaganda». ¿Qué falla?", "Una obra con forma cuidada puede ser propaganda; la forma no la define", "Que el cartel debe ser arte comprometido", "Que la propaganda siempre es descuidada", "La propaganda se define por su finalidad persuasiva, no por la calidad formal."),
        ("abc", "Una escuela ficticia decide retirar un libro por tratar un tema incómodo. ¿Qué concepto se aplica?", "Censura", "Propaganda", "Autonomismo", "Limita una obra por su contenido."),
        ("abc", "Una periodista ficticia escribe: «Esta novela me parece floja, pero debe poder leerse». ¿Qué distingue?", "Crítica (opinión) de censura (limitar)", "Autonomismo de propaganda", "Moralismo de arte comprometido", "Opinar sobre la calidad no equivale a pedir que se prohíba."),
        ("abc", "{F} Un estudiante dice: «Toda obra con un mensaje es propaganda». ¿Qué corrección es mejor?", "Una obra con mensaje puede dejar espacio a la duda y al debate; entonces no es solo propaganda", "Toda propaganda es arte comprometido", "Solo las obras sin ningún mensaje son arte", "La diferencia está en si la obra deja espacio a la duda o solo busca imponer un mensaje."),
    ],
    ctx=("abc", "En un liceo ficticio, un afiche para una campaña de reciclaje muestra solo imágenes alegres y no deja ver ningún problema. ¿Cómo podría hacerse menos propagandístico y más abierto al debate?", "Incluir datos de ejemplo rotulados y una pregunta para conversar", "Quitar el afiche", "Aumentar las imágenes alegres", "Dar información y preguntas deja espacio a la duda."),
    sc=[
        ("En Arte y política: ¿qué es el arte comprometido?", "Arte que busca intervenir en un problema social o político", "No siempre tiene un mensaje explícito."),
        ("En Estética: ¿Qué es la censura?", "Prohibir o limitar una obra por su contenido", "Se distingue de la crítica, que solo opina."),
        ("¿Qué distingue a la propaganda?", "Busca persuadir y ganar apoyo más que abrir un debate", "Su finalidad principal es persuadir y ganar apoyo."),
    ],
    op=("Elige dos de estos casos ficticios y clasifícalos con un concepto de la clase, explicando con una razón: (1) un cartel que muestra solo ventajas de un proyecto, (2) una obra que muestra una injusticia y deja preguntas abiertas, (3) un colegio que decide no exhibir un mural por un tema delicado, (4) una melodía instrumental que se valora solo por su forma. "
        "Después escribe una pregunta que le harías a cada caso.",
        "Caso 1: propaganda, porque busca apoyo sin mostrar problemas. Pregunta: ¿qué desventajas no se muestran? Caso 4: autonomismo, porque se valora por su forma. Pregunta: ¿puede ignorarse el contexto de quien la compuso?",
        ["clasifica con el concepto correcto", "da una razón basada en el caso", "formula una pregunta pertinente por caso", "evita tomar partido político"],
        ["dos casos clasificados con razón y pregunta"],
        ["usar etiquetas sin razón", "tomar partido político", "dar preguntas que se responden con sí o no"],
        "Pregunta: «¿qué rasgo del caso muestra que es propaganda y no arte comprometido?». Pídele que lo cite."),
    reinforce="Elige un anuncio o afiche que veas esta semana y analízalo con los conceptos de la clase.",
    extend="Explica con un ejemplo por qué una obra puede ser a la vez arte comprometido y de gran valor estético.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 18 (posturas de la tradición filosófica, resumidas por el cuaderno, sin citas). Postura P (en la tradición antigua, una postura que desconfía de ciertas obras): las historias y los cantos forman el carácter de la juventud, así que quienes gobiernan deben vigilar qué obras se les ofrecen. "
     "Postura A (otra postura de esa tradición): la tragedia permite sentir piedad y temor ante lo que ocurre a otros y, al hacerlo, depura esas emociones (catarsis); por eso el teatro puede ser provechoso para la comunidad. "
     "Postura M (autonomista moderna, resumen): el valor de una obra no se mide por su utilidad moral o política; mezclar los planos empobrece la mirada. "
     "Postura C (compromiso, resumen): el arte forma parte de la vida social y no puede ser neutral; elegir qué mostrar ya es tomar posición. "
     "Recordatorio del caso de Cerro Claro: «La plaza vacía» es una obra ficticia del liceo que muestra con crudeza cómo un alcalde ficticio ignora a sus vecinos, y el concejo debate si limitarla.")
build(
    O4, 3, F,
    use="Aprenderé a reconstruir cuatro posturas sobre la relación entre arte, moral y política y a compararlas por sus razones, sus supuestos y lo que implicarían para el caso de Cerro Claro.",
    prior=["Distingo moralismo, autonomismo y arte comprometido.", "Reconstruyo tesis y razones.", "Sé qué es una implicancia."],
    explain=[
        "En la tradición filosófica antigua aparecen dos posturas influyentes sobre el arte y la comunidad. Una, que suele asociarse a Platón, desconfía de ciertas obras porque pueden formar el carácter, y propone que quienes gobiernan vigilen lo que se ofrece a la juventud. Otra, que suele asociarse a Aristóteles, sostiene que la tragedia produce una catarsis, una depuración de la piedad y el temor, y por eso puede ser provechosa.",
        "En tiempos modernos, el autonomismo defiende que el valor del arte no depende de su utilidad moral o política, y que mezclar los planos empobrece la mirada. La postura del compromiso sostiene lo contrario: que el arte forma parte de la vida social y que hasta lo que se decide mostrar o callar toma posición. Estas posturas se oponen en qué debe importar al valorar una obra.",
        "Para reconstruirlas, se pregunta de cada una: qué tesis sostiene, qué razones ofrece y qué supone. Después se compara qué haría cada una con el caso de Cerro Claro. Reconstruir no es adherir: es entender cada postura en su versión más fuerte antes de evaluarla. No se necesita elegir hoy una de ellas.",
    ],
    vocab=[("catarsis", "depuración de emociones, como la piedad y el temor, al presenciar una tragedia"), ("formación del carácter", "proceso por el cual las experiencias moldean la manera de ser de una persona"), ("neutralidad", "no tomar posición"), ("versión más fuerte", "la formulación más razonable y cuidadosa de una postura")],
    worked=[
        ("Reconstruir la Postura A", "Reconstruye la Postura A de la ficha con tesis y razón.",
         ["Tesis: el teatro puede ser provechoso para la comunidad.", "Razón: la tragedia depura la piedad y el temor, es decir, produce catarsis."],
         "Tesis: el teatro puede ser provechoso; razón: produce catarsis"),
        ("Comparar dos posturas", "Compara la Postura M y la C en qué debe importar al valorar una obra.",
         ["M: importa la obra misma, no su utilidad moral o política.", "C: importa también lo que la obra decide mostrar o callar, porque el arte no es neutral."],
         "M: la obra misma; C: también lo que muestra o calla"),
    ],
    mistakes=[("Atribuir a una postura filosófica más de lo que dice el resumen.", "Se cree saber toda la teoría de un autor.", "Atente a lo que el resumen presenta y di cuando algo excede lo estudiado."),
              ("Reducir las posturas a una caricatura, como «P quiere prohibir todo».", "Se pierde la razón central.", "Reconstruye la razón de cada postura antes de evaluarla.")],
    T=[
        ("abc", "{F} ¿Qué razón principal ofrece la Postura P para vigilar las obras?", "Que forman el carácter de la juventud", "Que son difíciles de entender", "Que no tienen público", "P sostiene que las historias y los cantos moldean el carácter."),
        ("abc", "{F} ¿Qué es la catarsis según la Postura A?", "La depuración de la piedad y el temor al presenciar una tragedia", "Una forma de aplauso", "La censura de las obras", "Es la depuración de emociones que describe la ficha."),
        ("abc", "{F} ¿Qué sostiene la Postura M?", "Que el valor de una obra no se mide por su utilidad moral o política", "Que toda obra debe educar", "Que el arte no tiene valor", "M separa el valor artístico de la utilidad moral o política."),
        ("abc", "{F} ¿Qué sostiene la Postura C?", "Que el arte no puede ser neutral porque elegir qué mostrar es tomar posición", "Que el arte es neutral", "Que el arte debe ser prohibido", "C liga el arte con la vida social."),
        ("En Arte y política: ¿cómo se llama la depuración de emociones como la piedad y el temor al presenciar una tragedia?", "Catarsis", "Es el término que la tradición antigua usa para ese efecto."),
        ("abc", "{F} ¿Con qué postura coincidiría más un concejal que quiera revisar «La plaza vacía» porque cree que puede formar actitudes en la juventud?", "Con la Postura P", "Con la Postura M", "Con la Postura A", "Coincide en el interés por el efecto formativo de las obras."),
        ("ab", "{F} ¿Con qué postura coincidiría más una profesora que dice: «La obra permite sentir lo que viven otros y sacar emociones guardadas»?", "Con la Postura A", "Con la Postura M", "Habla de piedad, temor y depuración, que es la idea de catarsis."),
        ("abc", "{F} ¿Qué supuesto parece tener la Postura P?", "Que las obras influyen en la forma de ser de quienes las reciben", "Que el arte no influye en nada", "Que las obras solo sirven para entretener", "La vigilancia que propone se justifica porque se supone que las obras influyen."),
        ("abc", "{F} ¿Qué supuesto parece tener la Postura M?", "Que se puede separar el valor estético de lo moral y lo político", "Que el arte siempre tiene un mensaje político", "Que lo moral depende del gusto", "Quien sostiene que el valor no depende de la utilidad moral supone esa separación."),
        ("abc", "{F} ¿En qué se oponen más claramente M y C?", "En si el arte puede o no separarse de la vida social y política", "En si el arte debe ser bello", "En si el arte se aprende", "M separa los planos y C los une."),
        ("abc", "{F} Un estudiante resume: «P quiere prohibir todo». ¿Qué falla?", "Caricaturiza: P propone vigilar lo que se ofrece a la juventud, no prohibir todo", "Es la mejor reconstrucción", "Habla de la catarsis", "Reconstruir exige usar la razón de la postura y no exagerarla."),
        ("abc", "{F} ¿Qué haría la Postura A ante «La plaza vacía»?", "Considerar que la obra puede ayudar a la comunidad a sentir y pensar lo que ocurre", "Retirarla inmediatamente", "Ignorarla", "A valora el efecto positivo de las obras que mueven emociones."),
        ("abc", "{F} Una estudiante dice: «Con estas cuatro posturas ya sé cuál es la correcta». ¿Qué corrección es mejor?", "Reconstruir no es elegir: falta evaluar con criterios y casos", "Tiene razón: la más antigua es la correcta", "No hay nada que reconstruir", "Reconstruir es solo el primer paso."),
    ],
    ctx=("abc", "El concejo de Cerro Claro ficticio decide escuchar una exposición de las cuatro posturas antes de votar. ¿Cuál es la mejor manera de preparar a los concejales?", "Presentar cada postura con sus razones y supuestos, sin caricaturizarlas", "Presentar solo la postura de moda", "Pedir que voten sin leer", "Una comparación justa se apoya en reconstruir cada postura bien."),
    sc=[
        ("En Arte y política: ¿qué sostiene en general la Postura C?", "Que el arte no puede ser neutral porque elegir qué mostrar toma posición", "Liga el arte con la vida social."),
        ("¿Por qué es importante reconstruir la versión más fuerte de una postura?", "Porque así se evalúa la postura en su formulación más razonable", "Una crítica a una caricatura no vale como crítica."),
        ("¿Qué opone a la Postura M y a la Postura C?", "Que M separa el arte de lo moral y político y C los une", "Es una oposición en la relación entre planos."),
    ],
    op=("Elige dos de las cuatro posturas de la ficha (P, A, M, C). Reconstruye cada una con tesis, razón y supuesto, y escribe qué haría cada una con el caso «La plaza vacía». "
        "Termina con una frase que diga en qué se oponen y una pregunta que quedó abierta.",
        "Posturas M y C. M: tesis, el valor de la obra no depende de su utilidad moral o política; razón, mezclar planos empobrece la mirada; supuesto, se pueden separar los planos. Con la obra: valorar su forma. C: tesis, el arte no es neutral; razón, elegir qué mostrar toma posición; supuesto, el arte forma parte de la vida social. Con la obra: ver qué posición toma. Se oponen en separar o unir los planos. Pregunta: ¿se puede valorar la forma sin considerar el contexto?",
        ["reconstruye tesis, razón y supuesto de ambas posturas", "indica qué haría cada una con el caso", "señala una oposición", "deja una pregunta abierta"],
        ["dos reconstrucciones, una oposición y una pregunta"],
        ["caricaturizar una postura", "mezclar su opinión con el resumen", "no indicar supuestos"],
        "Pregunta: «¿esta frase es lo que dice la postura o lo que piensas tú?». Pídele que marque cada una."),
    reinforce="Escribe en cinco líneas qué diría cada una de las cuatro posturas sobre un videojuego que muestra violencia.",
    extend="Explica por qué las posturas P y A, en la lectura general de la clase, dan valoraciones distintas a la influencia del arte en la comunidad.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 19 (argumento y plan de investigación originales). Argumento V: «Si una obra muestra violencia, entonces promueve la violencia. La película ficticia «Marea baja» muestra violencia en varias escenas. Por lo tanto, «Marea baja» promueve la violencia.» "
     "Información adicional: «Marea baja» muestra las consecuencias dolorosas de la violencia y su final invita a pensar. "
     "Plan de investigación (borrador): Pregunta: ¿cuándo una obra que muestra violencia contribuye al debate sobre ella y cuándo se la considera dañina, y con qué razones? "
     "Fuentes posibles: (1) un texto filosófico breve (resumen), (2) una obra descrita en palabras, (3) la opinión de dos personas del barrio. Criterios para valorar fuentes: pertinencia, claridad, diversidad de miradas.")
build(
    O4, 4, F,
    use="Aprenderé a evaluar un argumento sobre arte y moral, distinguiendo mostrar de promover, y a diseñar una investigación breve con pregunta, fuentes de distinto tipo y criterios para valorarlas.",
    prior=["Distingo juicio estético, moral y político.", "Reconozco posturas sobre arte y moral.", "Sé evaluar un argumento."],
    explain=[
        "Un argumento común es: «Si una obra muestra X, entonces promueve X». Su premisa mezcla mostrar con promover. Una obra puede mostrar una conducta para criticarla, para comprenderla o para advertir sobre sus consecuencias. Para evaluar si promueve algo hay que mirar cómo lo presenta: si lo celebra, si lo critica o si deja abierta la reflexión.",
        "Diseñar una investigación breve implica una pregunta, fuentes variadas y criterios para valorarlas. Las fuentes pueden ser textos filosóficos, obras y testimonios. Los criterios son: pertinencia (¿responde a mi pregunta?), claridad (¿se entiende lo que dice?) y diversidad de miradas (¿incluyo más de una postura?). Un buen plan indica también qué haré con la información y cómo evitaré sacar conclusiones apresuradas.",
        "Al investigar, se registran las razones de cada fuente y se comparan. Si todas las fuentes dicen lo mismo, conviene preguntarse qué miradas faltan. La investigación no busca confirmar lo que ya pensábamos: busca entender mejor un problema. Tampoco toma partido político: se analiza con respeto a las distintas posiciones.",
    ],
    vocab=[("mostrar", "presentar algo en una obra, sin que eso implique aprobarlo"), ("promover", "impulsar o hacer atractiva una conducta"), ("fuente pertinente", "fuente que responde a la pregunta de investigación"), ("diversidad de miradas", "inclusión de más de una postura en la investigación"), ("conclusión apresurada", "conclusión sacada sin suficiente evidencia")],
    worked=[
        ("Evaluar la premisa de V", "Evalúa la premisa «si una obra muestra violencia, entonces la promueve».",
         ["Piensa en casos: una película puede mostrar violencia para mostrar su dolor.", "Concluye que mostrar no es promover; la premisa es débil."],
         "La premisa es débil porque mostrar no equivale a promover"),
        ("Valorar una fuente", "Una fuente ficticia es un afiche de una campaña que solo repite un eslogan. Para la pregunta del plan, ¿es una fuente pertinente?",
         ["Pregunta si ayuda a responder cuándo una obra contribuye al debate: no ofrece razones.", "Concluye que es poco pertinente."],
         "Es poco pertinente porque no ofrece razones"),
    ],
    mistakes=[("Tratar «mostrar» y «promover» como si fueran lo mismo.", "Se ignora cómo presenta la obra lo que muestra.", "Mira si la obra celebra, critica o deja abierta la reflexión."),
              ("Elegir solo fuentes que confirmen lo que uno ya piensa.", "Se pierde diversidad de miradas.", "Incluye al menos una fuente que piense distinto.")],
    T=[
        ("abc", "{F} ¿Cuál es la conclusión del Argumento V?", "«Marea baja» promueve la violencia", "Que «Marea baja» muestra violencia en varias escenas", "Que toda película con violencia es dañina", "La conclusión es lo que se quiere justificar."),
        ("abc", "{F} Si la primera premisa del Argumento V fuera verdadera, ¿se seguiría la conclusión?", "Sí: el argumento sería válido, y lo discutible es la primera premisa", "No: faltarían más escenas de violencia", "No: «Marea baja» tendría que ser una película real", "La forma es válida; la debilidad está en que la premisa mezcla mostrar con promover."),
        ("abc", "{F} ¿Qué información adicional pone en duda el Argumento V?", "Que la película muestra las consecuencias dolorosas de la violencia", "Que la película muestra violencia en varias escenas", "Que la película es de ficción", "Mostrar el dolor sugiere que no la presenta como deseable."),
        ("abc", "En Arte y política: ¿qué significa promover una conducta?", "Impulsarla o hacerla atractiva", "Mostrarla sin más", "Criticarla", "Promover es impulsar o hacer atractiva una conducta."),
        ("abc", "{F} ¿Cuál es una fuente pertinente para la pregunta del plan?", "Un resumen de una postura filosófica sobre el efecto de las obras", "Un afiche con un eslogan", "Una noticia sobre un estreno", "Debe ofrecer razones sobre cuándo una obra contribuye o daña."),
        ("ab", "{F} ¿Qué criterio de valoración de fuentes busca que no investigues con una sola postura?", "Diversidad de miradas", "Pertinencia", "La diversidad pide incluir más de una postura, no solo la que ya compartes."),
        ("abc", "{F} Una estudiante propone usar como únicas fuentes a tres amigos que piensan igual que ella. ¿Qué criterio se incumple?", "La diversidad de miradas", "La claridad", "La pertinencia en todos los casos", "El plan no incluye otras posturas distintas de la suya."),
        ("abc", "{F} ¿Cómo debería ajustarse el Argumento V para ser más prudente?", "«Una obra que muestra violencia puede promoverla, criticarla o invitar a pensar según cómo la presente»", "«Toda obra violenta es dañina»", "«Ninguna obra puede ser dañina»", "Una versión prudente depende de cómo se presenta lo que se muestra."),
        ("abc", "{F} Una investigadora pretende concluir tras mirar una sola obra que «las obras violentas siempre contribuyen al debate». ¿Qué falla?", "Saca una conclusión apresurada con una sola obra", "Usa demasiadas fuentes", "Escribe una pregunta de sí o no", "Una sola obra no basta para afirmar un «siempre»."),
        ("abc", "{F} Si una fuente defiende que hay que limitar las obras violentas y otra defiende que no, ¿qué conviene hacer con ellas?", "Comparar sus razones y supuestos en una tabla", "Quedarse solo con la que gusta", "Descartar ambas", "La comparación permite entender el problema."),
        ("abc", "{F} ¿Qué puede decirse de un cortometraje ficticio que presenta la violencia como algo admirable y sin consecuencias?", "Es más plausible decir que la promueve, según cómo la presenta", "Es imposible decir algo", "No muestra nada", "El modo de presentar importa para decidir si promueve."),
        ("abc", "{F} Elige el mejor paso para cerrar la investigación del plan.", "Resumir las razones de cada fuente y responder a la pregunta con prudencia", "Elegir la fuente más famosa y citarla", "Esconder las fuentes que no encajan", "Cerrar es sintetizar razones y responder con matices."),
        ("abc", "{F} Una estudiante dice: «Mi investigación está bien porque confirma lo que ya pensaba». ¿Qué corrección es mejor?", "Una investigación no busca confirmar sino entender mejor un problema", "Tiene toda la razón", "No hay que investigar", "Si solo confirma lo previo, pudo faltar diversidad."),
    ],
    ctx=("abc", "Un centro escolar ficticio debe decidir si deja que sus estudiantes presenten un cortometraje sobre acoso escolar que muestra escenas duras. Una apoderada dice: «Mostrar acoso es promoverlo». ¿Qué conviene hacer antes de decidir?", "Revisar cómo presenta el cortometraje lo que muestra y conversar con la comunidad", "Prohibirlo sin ver", "Presentarlo sin ninguna conversación", "El modo de presentar importa y el diálogo ayuda a decidir."),
    sc=[
        ("En Arte y política: ¿por qué «mostrar» no es lo mismo que «promover»?", "Porque una obra puede mostrar algo para criticarlo, comprenderlo o advertir sobre sus consecuencias", "Depende de cómo la obra presenta lo que muestra."),
        ("¿Cuáles son tres criterios para valorar fuentes?", "Pertinencia, claridad y diversidad de miradas", "Son los tres criterios que da la ficha."),
        ("¿Qué es una conclusión apresurada?", "Una conclusión sacada sin suficiente evidencia", "Por ejemplo, generalizar desde una sola obra."),
    ],
    op=("Diseña un plan de investigación breve. Elige una pregunta: (1) ¿cuándo se justifica limitar la difusión de una obra?, (2) ¿qué efectos pueden tener los murales que critican a una autoridad?, (3) ¿cómo se distingue una obra comprometida de propaganda? "
        "Indica: tu pregunta, tres fuentes de distinto tipo (describe cada una en una línea, usando fuentes ficticias o de ejemplo), los criterios con que las valorarás y cómo evitarás una conclusión apresurada.",
        "Pregunta 3. Fuentes: (a) resumen de una postura sobre arte comprometido (ficticio); (b) un cartel descrito en palabras; (c) opinión de una vecina. Criterios: pertinencia, claridad y diversidad. Evitaré concluir con una sola fuente y compararé razones en una tabla.",
        ["la pregunta es precisa y no se responde con sí o no", "las tres fuentes son de distinto tipo", "indica criterios de valoración", "señala cómo evitará conclusiones apresuradas"],
        ["plan con pregunta, tres fuentes, criterios y precauciones"],
        ["elegir fuentes que piensan igual", "no indicar criterios", "formular una pregunta de sí o no"],
        "Pregunta: «¿qué fuente de tu plan piensa distinto que tú?». Pídele que la marque."),
    reinforce="Escribe una pregunta de investigación sobre el cine, la música o los videojuegos y nombra dos fuentes posibles de tipos distintos.",
    extend="Explica por qué «lo que muestra una obra» no basta para saber cuáles son sus efectos en las personas.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 20 (objeciones originales). Tesis X: «Una comunidad tiene derecho a limitar la difusión de una obra cuando puede dañar a sus habitantes.» "
     "Objeción 1: «¿Quién decide qué obra daña? Si lo decide una sola autoridad, podría limitar obras solo porque la critican.» "
     "Objeción 2: «Si se prohíben las obras que incomodan, se pierde la posibilidad de que una comunidad se mire a sí misma y discuta.» "
     "Tesis Y: «Ninguna obra debería ser limitada jamás.» "
     "Objeción a Y: «Hay casos extremos, como una obra que revele datos privados de una persona y la ponga en riesgo, donde limitar parece razonable.»")
build(
    O4, 5, F,
    use="Aprenderé a responder objeciones a tesis sobre limitar o proteger obras, a buscar posiciones intermedias y a cerrar una investigación con una conclusión matizada sobre arte, moral y política.",
    prior=["Reconstruyo posturas sobre arte y política.", "Distingo mostrar de promover.", "Sé formular réplicas."],
    explain=[
        "Dos tesis extremas sobre este tema son: «una comunidad puede limitar obras que dañan» y «ninguna obra debería limitarse nunca». Cada una enfrenta objeciones fuertes. La primera, el riesgo de que quien decide use el poder para silenciar críticas. La segunda, los casos extremos en que una obra pone en riesgo a una persona.",
        "Ante objeciones sólidas, una salida frecuente es buscar posiciones intermedias que distingan casos. Por ejemplo, separar el desacuerdo con el contenido, que se resuelve con crítica y debate, del daño concreto a personas, que puede justificar medidas. Una posición intermedia debe indicar con claridad qué criterio usa para distinguir y quién lo aplica.",
        "Cerrar una investigación es escribir una conclusión matizada: responde a la pregunta con razones, reconoce los límites de la evidencia y deja abierto lo que falta saber. Una conclusión matizada no es una evasión: afirma lo que puede sostener y dice por qué. Aquí no se toma partido político; se muestran razones y se invita a discutir con respeto.",
    ],
    vocab=[("posición intermedia", "postura que distingue casos en lugar de aceptar o rechazar todo"), ("criterio de distinción", "regla que permite separar los casos que se tratan distinto"), ("conclusión matizada", "respuesta con razones que reconoce los límites de la evidencia"), ("daño concreto", "perjuicio específico a personas determinadas")],
    worked=[
        ("Clasificar una objeción", "La Objeción 1 pregunta quién decide qué obra daña. ¿A qué riesgo apunta?",
         ["Mira qué cuestiona: el poder de quien decide.", "Apunta al riesgo de que se silencien críticas."],
         "Al riesgo de que quien decide use el poder para silenciar críticas"),
        ("Proponer una posición intermedia", "Propón una posición intermedia ante las tesis X e Y.",
         ["Distingue: discrepar del contenido se responde con crítica y debate.", "Distingue: daño concreto a personas determinadas puede justificar medidas, con un procedimiento claro."],
         "Responder con crítica y debate al desacuerdo; admitir medidas solo ante daño concreto, con procedimiento claro"),
    ],
    mistakes=[("Creer que una posición intermedia es una evasión.", "Se confunde matizar con no decidir.", "Una posición intermedia indica criterios y quién los aplica."),
              ("Responder a una objeción repitiendo la tesis.", "No se hace cargo de la dificultad.", "Reconoce qué parte de la objeción tiene fuerza y ajusta la tesis.")],
    T=[
        ("abc", "{F} ¿Qué sostiene la Tesis X?", "Que una comunidad puede limitar obras que puedan dañar a sus habitantes", "Que no hay que limitar nada", "Que las obras no dañan", "X defiende un derecho de limitar por daño."),
        ("abc", "{F} ¿Qué riesgo señala la Objeción 1?", "Que una autoridad limite obras solo porque la critican", "Que las obras no tengan público", "Que no haya procedimiento para publicarlas", "Apunta al uso del poder para silenciar críticas."),
        ("abc", "{F} ¿Qué valor defiende la Objeción 2?", "Que una comunidad pueda mirarse a sí misma y discutir", "Que solo se muestren obras que gusten a todos", "Que la autoridad decida qué se muestra", "Defiende la posibilidad de autocrítica y debate."),
        ("abc", "{F} ¿Qué sostiene la Tesis Y?", "Que ninguna obra debería ser limitada jamás", "Que solo deben limitarse las obras que dañan", "Que toda obra debe ser aprobada por una autoridad", "La tesis Y rechaza toda limitación de obras."),
        ("abc", "{F} ¿Qué caso usa la objeción a Y?", "Una obra que revela datos privados de una persona y la pone en riesgo", "Una obra que critica a una autoridad", "Una obra que incomoda a parte del público", "Es un caso extremo de daño concreto."),
        ("En Arte y política: ¿cómo se llama la postura que distingue casos en lugar de aceptar o rechazar todo?", "Posición intermedia", "Es el nombre que se usa en la clase."),
        ("ab", "{F} ¿Cuál es una réplica razonable a la Objeción 1 desde la Tesis X?", "Precisar un procedimiento claro y no limitar obras solo por criticar", "Insistir en que la autoridad nunca se equivoca", "Reconoce el riesgo y ajusta la tesis; no basta con confiar en la autoridad."),
        ("abc", "{F} ¿Qué debe indicar una posición intermedia para no ser una evasión?", "Qué criterio usa para distinguir los casos y quién lo aplica", "Cuál obra le gusta más a quien decide", "Que ninguna obra se limite jamás", "Sin criterio explícito y sin saber quién decide, distinguir casos no responde a la Objeción 1."),
        ("abc", "{F} Una posición intermedia distingue el desacuerdo con el contenido (se responde con crítica y debate) del daño concreto a personas determinadas (puede justificar medidas con un procedimiento claro). ¿Qué respondería ante una obra ficticia que ridiculiza con ironía a una autoridad?", "Es un desacuerdo con el contenido: se responde con crítica y debate", "Hay que limitarla porque molesta", "Hay que limitarla porque critica a una autoridad", "Una ironía sobre una autoridad no causa daño concreto a personas determinadas."),
        ("abc", "{F} Una posición intermedia distingue el desacuerdo con el contenido (se responde con crítica y debate) del daño concreto a personas determinadas (puede justificar medidas con un procedimiento claro). ¿Qué respondería ante una obra que publica la dirección y los horarios de una persona ficticia con intención de acosarla?", "Hay daño concreto: puede justificar medidas con procedimiento claro", "Es solo una crítica", "Es un desacuerdo con el contenido que se responde con debate", "Exponer a una persona determinada a un riesgo concreto es daño, no un simple desacuerdo."),
        ("abc", "{F} Un estudiante dice: «Una posición intermedia no se decide por nada». ¿Qué responder?", "Que se decide por un criterio y por un procedimiento que debe explicitar", "Que tiene razón", "Que no necesita razones", "Una posición intermedia es una posición con criterios."),
        ("abc", "Sobre un cartel ficticio que ironiza a una autoridad, tres estudiantes concluyen algo distinto. ¿Cuál conclusión es matizada?", "Por ahora no se ve daño concreto a personas; conviene responder con crítica y debate y revisar si aparecen nuevos antecedentes", "El cartel debe retirarse, porque toda ironía es dañina", "El cartel no puede discutirse, porque toda crítica es válida", "Da razones, distingue el caso y reconoce que la evidencia puede cambiar."),
        ("abc", "{F} Para ser honesta, una conclusión matizada debe además…", "Reconocer los límites de la evidencia reunida", "Ocultar las objeciones", "Cambiar de tema", "La honestidad intelectual incluye decir qué no se sabe."),
    ],
    ctx=("abc", "Un liceo ficticio recibe reclamos por un mural que critica con ironía a la dirección. Un grupo pide borrarlo y otro, mantenerlo sin conversar. ¿Qué actitud sigue la posición intermedia?", "Distinguir si hay daño concreto a personas, conversar sobre la crítica y decidir con un procedimiento claro", "Borrarlo de inmediato", "Mantenerlo sin escuchar a nadie", "Distingue casos y deja claro el procedimiento."),
    sc=[
        ("En Arte y política: ¿qué es una posición intermedia?", "Una postura que distingue casos y explicita su criterio", "No evade el problema: propone un criterio explícito."),
        ("¿Qué riesgo señala la objeción a limitar obras por daño?", "Que quien decide use el poder para silenciar críticas", "Pregunta quién y con qué procedimiento decide."),
        ("¿Qué debe incluir una conclusión matizada?", "Razones, límites de la evidencia y lo que queda abierto", "Responde con razones sin pretender una certeza absoluta."),
    ],
    op=("Cierra tu investigación sobre la pregunta «¿cuándo se justifica limitar la difusión de una obra?». Escribe: la tesis X o Y con la que más simpatizas, la objeción más fuerte contra ella, tu réplica o ajuste, y una conclusión matizada de cuatro a seis líneas. "
        "Usa casos ficticios y mantén un tono neutral: se trata de razones, no de partidos.",
        "Simpatizo con X. Objeción: ¿quién decide? Ajuste: un procedimiento abierto y revisable. Conclusión: el desacuerdo con el contenido se responde con crítica y debate; el daño concreto a personas determinadas puede justificar medidas con un procedimiento claro. Falta saber qué procedimientos funcionan mejor.",
        ["presenta una tesis y la objeción más fuerte", "ajusta la tesis o la defiende con razones", "la conclusión distingue casos", "reconoce lo que queda abierto"],
        ["tesis, objeción, réplica y conclusión matizada"],
        ["elegir una tesis sin considerar objeciones", "conclusión sin razones", "no reconocer límites de evidencia"],
        "Pregunta: «¿qué caso extremo pondría a prueba tu conclusión?». Pídele que lo escriba y diga cómo respondería."),
    reinforce="Imagina una regla de convivencia de tu curso sobre qué publicar en un panel y escribe una objeción y una réplica.",
    extend="Explica por qué la crítica y el debate son una forma de respuesta a una obra distinta de la censura.",
)
