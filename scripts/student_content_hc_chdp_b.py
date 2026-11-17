"""Comprensión histórica del presente (electivo HC, 3.º y 4.º medio): OAC-02 (perspectivas historiográficas sobre procesos de la historia reciente, conocimiento histórico y sujetos históricos), clases 1 a 5. Fuentes, personas y datos ficticios o de ejemplo."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada relato, fuente o tabla está escrito en el enunciado. "
             "Las personas, los relatos y los datos son ficticios o de ejemplo (la comuna «Lomas del Sur» no existe) y sirven para practicar el método de la historia. "
             "Las posturas se presentan con sus razones y sin tomar partido. Los temas dolorosos se tratan con sobriedad; si algo te afecta, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O2 = "HI-CHDP-3y4-OAC-02"

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (afirmaciones de ejemplo, ficticias). Afirmación 1: «Doña Rosa organizó el comedor solidario del barrio y reunió a sus vecinas para sostenerlo.» "
     "Afirmación 2: «El sindicato de la fábrica de conservas negoció mejores turnos con la empresa.» "
     "Afirmación 3: «En la región subieron las temperaturas durante el verano.» "
     "Afirmación 4: «El centro de estudiantes del liceo reunió firmas para pedir una biblioteca.»")
build(
    O2, 1, F,
    use="Aprenderé qué es la historia reciente, quiénes son los sujetos históricos y para qué sirve el conocimiento histórico en la sociedad, para reconocer a individuos y grupos como protagonistas de los procesos.",
    prior=["Sé contextualizar un hecho en tiempo, espacio y actores.", "Sé qué es una fuente y una perspectiva.", "Conozco los ejes del cambio reciente: sociedad civil, derechos, desigualdad e inclusión."],
    explain=[
        "La historia reciente es el estudio del pasado cercano, aquel del que todavía hay testigos vivos y cuyas consecuencias seguimos viviendo. Por eso se discute con más intensidad que el pasado lejano: las personas que lo vivieron pueden aportar su testimonio, pero también tienen recuerdos y puntos de vista distintos. Tiene muchas fuentes, aunque no siempre todas están abiertas o ordenadas.",
        "Un sujeto histórico es una persona o un grupo que, con sus decisiones y acciones, influye en los procesos de su sociedad. Puede ser un individuo (una dirigenta, un estudiante), un grupo organizado (un sindicato, un centro de estudiantes) o una comunidad. Un fenómeno natural, como un temporal, no es sujeto histórico, aunque sus efectos pueden obligar a otros a actuar. El protagonismo es el papel principal que un sujeto tiene en un proceso.",
        "El conocimiento histórico sirve para comprender el presente, ejercer la ciudadanía con criterio y no depender de relatos simplificados o manipulados. Una sociedad que conoce los sujetos de su historia, también los que casi no aparecen en los libros, entiende mejor cómo se construyeron sus derechos, sus instituciones y sus desigualdades.",
    ],
    vocab=[("historia reciente", "estudio del pasado cercano, con testigos vivos"), ("sujeto histórico", "persona o grupo que con sus acciones influye en un proceso"), ("protagonismo", "papel principal de un sujeto en un proceso"), ("testimonio", "relato de una persona sobre lo que vivió o supo"), ("conocimiento histórico", "saber construido con método sobre el pasado"), ("ciudadanía", "condición de personas que participan y se informan en la vida pública")],
    worked=[
        ("Reconocer un sujeto histórico", "Una asociación de pescadores artesanales de ejemplo logra que se respete una zona de pesca para sus botes. ¿Es un sujeto histórico?",
         ["Es un grupo organizado que toma decisiones y actúa con un propósito.", "Su acción influye en cómo se usa el territorio y en las normas de la zona."],
         "Sí: es un grupo que actúa con propósito e influye en su entorno"),
        ("Ubicar la historia reciente", "Una estudiante investiga cómo se fundó, hace diez años, el taller de teatro de su liceo, y entrevista a quienes lo crearon. ¿Es historia reciente?",
         ["El hecho ocurrió hace poco tiempo.", "Hay testigos vivos que pueden ser entrevistados."],
         "Sí: es pasado cercano con testigos vivos"),
    ],
    mistakes=[("Pensar que solo las autoridades son sujetos históricos.", "Se asocia la historia con cargos y no con la acción de las personas.", "Revisa quién decide y actúa: también lo hacen vecinas, estudiantes y organizaciones."),
              ("Creer que historia reciente es lo mismo que noticia de hoy.", "Se confunde lo cercano con lo inmediato.", "La historia reciente se estudia con método, fuentes y distancia crítica, aunque los hechos sean cercanos.")],
    T=[
        ("abc", "{F} ¿Cuál afirmación describe a una persona que actúa y reúne a otras?", "La afirmación 1", "La afirmación 2", "La afirmación 3", "La afirmación 1 muestra a doña Rosa organizando el comedor con sus vecinas."),
        ("abc", "{F} ¿Cuál afirmación NO describe a un sujeto histórico?", "La afirmación 3, sobre las temperaturas", "La afirmación 2, sobre el sindicato", "La afirmación 4, sobre el centro de estudiantes", "Un cambio de temperatura es un fenómeno natural, no una persona ni un grupo que decide."),
        ("abc", "En Comprensión histórica, ¿qué es la historia reciente?", "El estudio del pasado cercano, con testigos vivos", "El estudio de las noticias del día", "El estudio de la prehistoria", "Se caracteriza por la cercanía en el tiempo y por la existencia de testigos."),
        ("abc", "{F} ¿Qué tipo de sujeto histórico es el sindicato de la afirmación 2?", "Un grupo organizado", "Una persona individual", "Un fenómeno natural", "Un sindicato reúne a trabajadores que actúan colectivamente."),
        ("abc", "{F} ¿Por qué el centro de estudiantes de la afirmación 4 es un sujeto histórico?", "Porque un grupo actúa con un propósito e intenta cambiar su entorno", "Porque es famoso en todo el país", "Porque lo forman solo personas mayores de edad", "Un sujeto histórico se reconoce por su acción intencionada y su influencia, no por su fama."),
        ("ab", "¿Para qué sirve principalmente el conocimiento histórico en una sociedad?", "Para comprender el presente y ejercer la ciudadanía con criterio", "Para memorizar fechas y nombres sin relacionarlos", "El conocimiento histórico ayuda a entender el presente y a no depender de relatos simplificados."),
        ("abc", "Un temporal destruye un puente y los vecinos se organizan para reconstruirlo. ¿Quiénes son los sujetos históricos?", "Los vecinos que se organizan", "El temporal", "El puente", "El temporal es un fenómeno natural; quienes deciden y actúan son los vecinos."),
        ("abc", "Un historiador cuenta solo lo que hicieron los alcaldes de una comuna en treinta años. ¿Qué queda fuera?", "Vecinos, organizaciones y otros grupos que también actuaron", "Nada, porque los alcaldes representan a todos", "Solo los vecinos que votaron", "Una historia centrada en autoridades omite a otros sujetos que influyeron en el proceso."),
        ("abc", "¿Por qué la historia reciente suele generar más debate que la antigua?", "Porque hay testigos vivos y sus consecuencias se sienten hoy", "Porque no existen fuentes sobre ella", "Porque ocurrió en muy pocos años", "La cercanía y los distintos recuerdos de los testigos hacen que haya más discusión."),
        ("abc", "{F} Un compañero dice: «Solo el sindicato importa, porque doña Rosa no tenía ningún cargo.» ¿Qué error comete?", "Cree que solo quienes tienen cargo son sujetos históricos", "Confunde un sindicato con un fenómeno natural", "Usa una fuente del año equivocado", "Una persona sin cargo también actúa e influye, como doña Rosa."),
        ("abc", "{F} ¿Qué afirmación muestra a la vez a una persona y a un grupo que actúan juntos?", "La afirmación 1: doña Rosa y sus vecinas", "La afirmación 3: las temperaturas", "Ninguna de las cuatro", "Doña Rosa lidera y las vecinas colaboran para sostener el comedor."),
        ("abc", "Un trabajo escolar quiere mostrar cómo las mujeres de una comuna cambiaron la vida local en treinta años. ¿Qué enfoque las pone como sujetos históricas?", "Estudiar sus organizaciones, decisiones y acciones", "Contar solo las obras del municipio", "Listar las leyes nacionales del período", "Para mostrarlas como sujetos hay que centrarse en lo que ellas decidieron e hicieron."),
        ("abc", "Se dice que conocer la historia reciente sirve para la ciudadanía. ¿Cuál es un ejemplo?", "Contrastar datos y testimonios antes de creer un rumor sobre el barrio", "Aprender de memoria una lista de años", "Evitar conversar sobre el pasado", "Informarse con fuentes y contrastarlas es una forma de ejercer la ciudadanía con criterio."),
    ],
    ctx=("abc", "Una profesora propone reconstruir la historia del liceo de los últimos treinta años con testimonios de exestudiantes y no solo con documentos de la dirección. ¿Qué gana el trabajo?", "Incorpora a los estudiantes como sujetos históricos y suma fuentes orales", "Evita tener que usar fuentes", "Garantiza que no habrá desacuerdos", "Los testimonios agregan voces que los documentos oficiales suelen omitir."),
    sc=[
        ("En Comprensión histórica: ¿qué es un sujeto histórico?", "Una persona o un grupo que con sus acciones influye en un proceso", "Se reconoce por la acción intencionada y su influencia."),
        ("¿Por qué un fenómeno natural no es un sujeto histórico?", "Porque no decide ni actúa con un propósito", "Sus efectos pueden obligar a otros a actuar, pero él no actúa."),
        ("¿Qué característica distingue a la historia reciente?", "Que trata del pasado cercano y todavía hay testigos vivos", "Esa cercanía aporta testimonios, pero también más debate."),
    ],
    op=("Elige uno de estos casos de ejemplo y escribe una ficha. Caso 1: un grupo de apoderados logra que el liceo instale bebederos de agua. Caso 2: una cooperativa de recicladores de base consigue un punto de acopio en la comuna. "
        "En la ficha anota quién o quiénes son los sujetos históricos, qué hicieron, qué cambió, una fuente que permitiría comprobarlo (por ejemplo, un acta o una entrevista) y por qué es historia reciente.",
        "Caso 1. Sujetos: el grupo de apoderados. Hicieron: reunieron firmas y presentaron una petición. Cambió: se instalaron bebederos. Fuente: acta de reunión de apoderados. Es historia reciente porque hay testigos y ocurrió hace pocos años.",
        ["identifica a los sujetos históricos con una razón", "describe lo que hicieron y lo que cambió", "propone una fuente pertinente", "explica por qué es historia reciente"],
        ["ficha con sujetos, acción, cambio, fuente y justificación"],
        ["nombrar solo a la autoridad que firmó", "no indicar qué cambió", "proponer una fuente que no permite comprobar el hecho"],
        "Pregunta: «¿quién decidió y quién actuó?». Si nombra solo a una autoridad, pídele revisar si hubo otros grupos."),
    reinforce="Escribe tres ejemplos de sujetos históricos de tu entorno (un individuo, un grupo y una comunidad) y qué proceso influyen.",
    extend="Investiga con una persona adulta de tu casa un cambio de tu barrio en los últimos treinta años y anota quiénes fueron sus sujetos.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (fuentes de ejemplo, ficticias). Inauguración de un centro comunitario en Lomas del Sur, un sábado por la tarde. "
     "Testimonio (Elena, vecina, entrevistada años después): «Éramos más de cien, no cabía nadie en la sala.» "
     "Nota de prensa (diario local de ese fin de semana): «Unas 80 personas asistieron a la inauguración del centro.» "
     "Acta municipal con hoja de asistencia: 64 firmas, con la anotación «no todos firmaron».")
build(
    O2, 2, F,
    use="Aprenderé a interrogar y contrastar fuentes de la historia reciente (testimonios, prensa, documentos oficiales), reconociendo sus ventajas y límites, para sostener una afirmación sobre un proceso reciente.",
    prior=["Sé qué es una fuente primaria y una secundaria.", "Sé interrogar una fuente: quién, cuándo y para qué.", "Sé qué es un indicador y sus límites."],
    explain=[
        "La historia reciente cuenta con fuentes muy variadas: testimonios orales, notas de prensa, documentos oficiales como actas y leyes, fotografías, videos y registros digitales. Su abundancia es una ventaja, pero cada tipo tiene límites. El testimonio aporta cómo se vivió algo, pero depende de la memoria, que puede olvidar, exagerar o reordenar. La prensa informa en el momento, pero tiene una línea editorial y poco espacio. El documento oficial registra decisiones, pero calla desacuerdos y vivencias.",
        "Contrastar fuentes es compararlas para ver en qué coinciden y en qué difieren. La triangulación consiste en contrastar al menos tres fuentes de distinto tipo sobre un mismo hecho. Lo que todas confirman tiene mayor respaldo; lo que difiere debe explicarse: ¿cambia el punto de vista?, ¿el propósito?, ¿el momento en que se produjo la fuente?",
        "Cuando las cifras no coinciden, el historiador no elige la que le gusta: informa el rango o dice que la cifra exacta no se conoce, y explica por qué puede ser baja o alta cada una. También reconoce que hay fuentes que no existen o no están disponibles, y por eso sus conclusiones deben declarar sus límites.",
    ],
    vocab=[("fuente oral", "relato de una persona sobre lo que vivió o supo"), ("memoria", "recuerdo que una persona o comunidad conserva del pasado, con sus selecciones"), ("línea editorial", "punto de vista habitual de un medio de prensa"), ("contrastar fuentes", "compararlas para ver en qué coinciden y en qué difieren"), ("triangulación", "contraste de al menos tres fuentes de distinto tipo sobre un hecho"), ("documento oficial", "registro producido por una institución, como un acta o una ley")],
    worked=[
        ("Clasificar una fuente y sus límites", "Una vecina de ejemplo conserva una fotografía de una marcha escolar de hace ocho años. ¿Qué tipo de fuente es y qué límite tiene?",
         ["Es una fuente primaria visual, producida en la época del hecho.", "Muestra solo lo que quien tomó la foto decidió encuadrar; deja fuera lo que no está en el cuadro."],
         "Fuente primaria visual; muestra solo el encuadre elegido"),
        ("Contrastar dos cifras", "Un diario de ejemplo informa de 200 asistentes a un acto; el acta de los organizadores anota 150. ¿Qué hace un historiador?",
         ["Observa que difieren en 50 y piensa en el propósito de cada fuente.", "Busca una tercera fuente, como fotos o testimonios, y declara el rango si no puede precisar."],
         "Busca una tercera fuente y declara el rango de 150 a 200"),
    ],
    mistakes=[("Elegir la cifra de la fuente que más conviene a la tesis.", "Se prefiere una respuesta única a una cifra incierta.", "Informa el rango y explica por qué cada fuente puede estar alta o baja."),
              ("Creer que una fuente oficial siempre es exacta y un testimonio nunca sirve.", "Se piensa que una fuente es neutral por ser oficial.", "Todas las fuentes se interrogan: la oficial calla vivencias y el testimonio aporta lo que no se registró.")],
    T=[
        ("abc", "{F} ¿Cuál de las tres fuentes es un testimonio oral?", "El relato de Elena", "La nota de prensa", "El acta municipal", "Elena cuenta lo que vivió, años después, en una entrevista."),
        ("abc", "{F} ¿Qué fuente registra 64 firmas?", "El acta municipal", "La nota de prensa", "El testimonio de Elena", "La hoja de asistencia del acta anota esa cifra."),
        ("abc", "En Comprensión histórica, ¿qué es contrastar fuentes?", "Compararlas para ver en qué coinciden y en qué difieren", "Copiar la fuente más antigua", "Elegir la fuente más larga", "El contraste revela coincidencias y diferencias entre las fuentes."),
        ("abc", "{F} ¿Qué hecho confirman las tres fuentes?", "Que hubo una inauguración con asistencia de público", "Que asistieron exactamente 80 personas", "Que la sala era pequeña", "Las tres hablan de una inauguración con asistentes, pero difieren en las cifras."),
        ("abc", "{F} ¿Qué fuente da la cifra más alta de asistentes?", "El testimonio de Elena, con más de cien", "La nota de prensa, con unas 80", "El acta, con 64 firmas", "«Más de cien» es mayor que 80 y que 64."),
        ("=", "La nota de prensa dice «unas 80» personas y el acta registra 64 firmas. ¿Cuál es la diferencia entre ambas cifras?", "80-64", "La diferencia se calcula restando la cifra menor a la mayor."),
        ("abc", "{F} ¿Por qué la cifra del acta puede ser más baja que la real?", "Porque el acta anota que no todos firmaron", "Porque las actas siempre mienten", "Porque la prensa la corrigió", "La propia acta advierte que algunas personas no firmaron."),
        ("abc", "{F} ¿Por qué la cifra del testimonio puede ser más alta que la real?", "Porque la memoria puede ampliar lo vivido con emoción años después", "Porque Elena trabajaba en el diario", "Porque los testimonios nunca sirven", "El recuerdo cambia con el tiempo, y por eso se contrasta con otras fuentes."),
        ("abc", "{F} ¿Cuál es la conclusión más prudente sobre la asistencia?", "Las fuentes dan cifras distintas (64 firmas, unas 80, más de cien) y la cifra exacta no se conoce", "Asistieron exactamente 64 personas", "Asistieron cien personas, porque lo dice un testigo", "Cuando las fuentes difieren, lo honesto es informar el rango y reconocer la incertidumbre."),
        ("abc", "En Comprensión histórica, ¿qué es la triangulación de fuentes?", "Contrastar al menos tres fuentes de distinto tipo sobre un mismo hecho", "Dibujar un triángulo con las fechas", "Repetir la misma fuente tres veces", "Usar tipos distintos reduce el riesgo de que un sesgo domine la conclusión."),
        ("abc", "{F} Un estudiante dice: «El diario es la mejor fuente porque está impreso.» ¿Qué le respondes?", "Un diario tiene línea editorial y poco espacio: hay que contrastarlo con otras fuentes", "Tiene razón: lo impreso siempre es exacto", "Un diario nunca sirve como fuente", "Toda fuente se interroga, y ser impresa no la hace neutral."),
        ("abc", "{F} Para saber si la sala era realmente pequeña, ¿qué fuente ayudaría más?", "Un plano o las medidas de la sala junto a una fotografía del evento", "Otra entrevista a Elena sobre lo mismo", "Una nota de opinión de un columnista", "Un plano y una foto aportan evidencia independiente del recuerdo."),
        ("abc", "¿Cuál es una ventaja de la historia reciente respecto de la muy antigua?", "Se puede entrevistar a testigos que vivieron los hechos", "Existe un único relato sobre cada hecho", "Nunca hay fuentes en conflicto", "Los testigos vivos permiten recoger testimonios, aunque sus recuerdos deban contrastarse."),
    ],
    ctx=("abc", "Una estudiante investiga la creación de una plaza hace quince años. Tiene el folleto municipal que la celebra, una entrevista a la presidenta de la junta de vecinos y un acta de reunión. ¿Cómo debería usar las tres fuentes?", "Contrastarlas, preguntando quién produjo cada una y para qué", "Usar solo el folleto, porque es oficial", "Descartar la entrevista por ser subjetiva", "Cada fuente aporta algo distinto, y se corrigen entre sí cuando se contrastan."),
    sc=[
        ("En Comprensión histórica: ¿qué límite tiene un testimonio oral?", "Depende de la memoria, que puede olvidar, exagerar o reordenar", "Por eso se contrasta con otras fuentes."),
        ("¿Qué hace un historiador cuando las cifras de dos fuentes no coinciden?", "Informa el rango y explica por qué cada una puede ser alta o baja", "No elige la cifra que le conviene."),
        ("¿Qué límite tiene un documento oficial como un acta?", "Registra decisiones, pero calla desacuerdos y vivencias", "Por eso no reemplaza a los testimonios."),
    ],
    op=("Para cada una de estas tres fuentes de ejemplo sobre una feria vecinal, escribe qué tipo de fuente es, un aporte y un límite. Fuente 1: la entrevista a una feriante: «Fue la feria más grande que recuerdo.» "
        "Fuente 2: el permiso municipal de la feria, que autoriza 40 puestos. Fuente 3: una fotografía de la feria con unos 30 puestos visibles. Luego escribe una conclusión prudente sobre el tamaño de la feria.",
        "Fuente 1: testimonio; aporta cómo se vivió; límite: es impresión personal. Fuente 2: documento oficial; aporta el máximo autorizado; límite: no dice cuántos puestos hubo. Fuente 3: fotografía; aporta lo visible; límite: no muestra todo. Conclusión: tuvo hasta 40 puestos autorizados y unos 30 visibles; el tamaño exacto no se conoce.",
        ["clasifica correctamente cada fuente", "señala un aporte y un límite razonado para cada una", "redacta una conclusión que usa las tres y declara su incertidumbre"],
        ["tabla con tipo, aporte y límite, y una conclusión de dos frases"],
        ["no declarar ningún límite", "elegir una cifra única sin justificar", "tratar al permiso como prueba de cuántos puestos hubo"],
        "Pregunta: «¿qué diría otra fuente sobre esto?». Si responde que no importa, pídele probar con las tres."),
    reinforce="Con la ficha 2, escribe una oración que use las tres fuentes para describir la inauguración sin dar una cifra exacta.",
    extend="Escribe cinco preguntas que le harías a una persona adulta mayor para entrevistarla sobre un cambio en tu barrio, procurando que no induzcan la respuesta.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (relatos de ejemplo, ficticios). Cierre de una fábrica de conservas en Lomas del Sur. "
     "Relato de Marcos, trabajador: «Perdimos nuestro sustento y nadie nos avisó con tiempo.» "
     "Relato de Carolina, dueña de la fábrica: «Los costos subieron y ya no pudimos mantener la planta; intentamos reubicar a parte del personal.» "
     "Informe municipal: «El cierre dejó a 120 personas sin empleo y la comuna abrió una oficina de apoyo laboral.»")
build(
    O2, 3, F,
    use="Aprenderé a comparar las perspectivas de distintos sujetos y de distintos enfoques historiográficos (política, social y de la vida cotidiana) sobre un mismo proceso reciente, sin dar por hecho que una excluye a las otras.",
    prior=["Sé interrogar y contrastar fuentes de la historia reciente.", "Reconozco a individuos y grupos como sujetos históricos.", "Sé distinguir causas y consecuencias."],
    explain=[
        "Un mismo proceso se ve distinto según quién lo cuenta. Las personas que lo vivieron, las instituciones que decidieron y quienes lo estudian después ponen la atención en cosas diferentes: unos en las causas, otros en las consecuencias, otros en la experiencia. Comparar esas perspectivas permite reconstruir un cuadro más completo, sin que ninguna deba tomarse como la única verdad.",
        "En la historiografía hay enfoques que organizan esas miradas. La historia política estudia el poder, las instituciones y las decisiones de gobierno. La historia social estudia los grupos sociales, sus condiciones de vida y sus relaciones. La historia de la vida cotidiana estudia las experiencias diarias, como el trabajo, la familia y el barrio. Un mismo hecho puede estudiarse con los tres enfoques y entregar resultados que se complementan.",
        "Comparar bien exige separar tres planos: los hechos que todos aceptan, las explicaciones sobre sus causas y las valoraciones de lo ocurrido. Dos relatos pueden coincidir en los hechos y diferir en las causas y en cómo valoran la situación. Un relato de ejemplo puede ser verdadero en lo que cuenta sin ser completo.",
    ],
    vocab=[("historia política", "enfoque que estudia el poder, las instituciones y las decisiones de gobierno"), ("historia social", "enfoque que estudia grupos sociales y sus condiciones de vida"), ("historia de la vida cotidiana", "enfoque que estudia las experiencias diarias de las personas"), ("complementarse", "completarse entre sí aportando partes distintas"), ("valoración", "juicio sobre lo ocurrido: si fue justo, bueno o injusto"), ("hecho aceptado", "dato en el que coinciden todas las fuentes")],
    worked=[
        ("Separar hechos, explicaciones y valoraciones", "Dos vecinos de ejemplo hablan del cierre de una feria: «La feria cerró en marzo» (vecina 1) y «Cerró por culpa de la mala administración, y fue injusto» (vecino 2). ¿Qué plano corresponde a cada parte?",
         ["«Cerró en marzo» es un hecho que se puede comprobar.", "«Por culpa de la mala administración» es una explicación y «fue injusto» una valoración."],
         "Hecho; explicación; valoración"),
        ("Asignar un enfoque", "Un estudio de ejemplo analiza cómo cambió el horario de las familias y el uso del tiempo después de un cambio de turnos laborales en un barrio. ¿Qué enfoque predomina?",
         ["Estudia la rutina diaria de las familias, no el poder ni las instituciones.", "Eso corresponde a la vida cotidiana, con elementos de historia social."],
         "Historia de la vida cotidiana"),
    ],
    mistakes=[("Creer que si dos relatos difieren, uno debe estar mintiendo.", "Se confunde la diferencia de perspectiva con falsedad.", "Revisa en qué coinciden, en qué difieren y qué aspecto del proceso destaca cada relato."),
              ("Mezclar un hecho con una valoración como si fueran lo mismo.", "Se toma lo que alguien siente como dato comprobable.", "Separa lo que se puede comprobar de lo que es explicación o juicio.")],
    T=[
        ("abc", "{F} ¿Quién relata el primer testimonio de la ficha?", "Marcos, trabajador de la fábrica", "Carolina, dueña de la fábrica", "El municipio", "El primer relato es de Marcos."),
        ("abc", "{F} ¿Qué destaca Carolina en su relato?", "El aumento de los costos y los intentos de reubicar personal", "La falta de aviso a los trabajadores", "La apertura de una oficina de apoyo laboral", "Habla de costos que subieron y de reubicación de personal."),
        ("abc", "{F} ¿Qué destaca el informe municipal?", "Las consecuencias para la comuna y la respuesta institucional", "Las causas económicas del cierre", "Las vivencias personales del trabajador", "Informa cuántas personas quedaron sin empleo y la oficina creada."),
        ("abc", "En Comprensión histórica, ¿qué estudia la historia social?", "Los grupos sociales y sus condiciones de vida", "Solo las decisiones de gobierno", "Solo las batallas y los tratados", "Su objeto son los grupos y cómo viven."),
        ("abc", "En Comprensión histórica, ¿qué estudia la historia política?", "El poder, las instituciones y las decisiones de gobierno", "La rutina diaria de las familias", "Las condiciones de vida de los trabajadores", "Se centra en el poder y las instituciones."),
        ("abc", "En Comprensión histórica, ¿qué estudia la historia de la vida cotidiana?", "Las experiencias diarias, como el trabajo, la familia y el barrio", "Solo las leyes del país", "Solo los grandes líderes", "Mira cómo vivían y trabajaban las personas en su día a día."),
        ("abc", "{F} ¿Qué enfoque se parece más al relato de Marcos?", "El de la vida cotidiana y social: cómo se vivió la pérdida del trabajo", "El de la historia política de las leyes", "Ninguno, porque es un solo testimonio", "Marcos habla de su sustento y de lo que vivieron los trabajadores."),
        ("abc", "{F} ¿Se contradicen Marcos y Carolina en los hechos?", "No: ambos aceptan que la fábrica cerró; difieren en causas y vivencias", "Sí: uno dice que cerró y la otra que no", "No, porque ninguno habla del cierre", "Ambos reconocen el cierre y destacan aspectos distintos."),
        ("abc", "{F} ¿Qué diferencia hay en lo que explican Marcos y Carolina?", "Marcos destaca la falta de aviso y ella los costos que subieron", "Marcos destaca los costos y ella la falta de aviso", "Ambos destacan lo mismo", "Cada uno señala una causa o una circunstancia distinta."),
        ("=", "En la comuna de ejemplo, el cierre dejó a 120 personas sin empleo (según el informe) y la oficina de apoyo reubicó a 45. ¿Cuántas personas siguen sin reubicar?", "120-45", "Se resta a las 120 personas las 45 reubicadas."),
        ("abc", "{F} Un alumno dice: «Solo vale el informe municipal, porque es oficial.» ¿Qué le falta a esa idea?", "Las experiencias de quienes vivieron el cierre y los motivos de la empresa también ayudan a explicar el proceso", "Nada, el informe lo explica todo", "El informe no tiene ningún valor", "Una sola fuente oficial no cubre vivencias ni causas, y por eso se compara con otras."),
        ("abc", "{F} ¿Qué pregunta permite comparar mejor los tres relatos?", "¿Qué causas y consecuencias destaca cada relato y con qué evidencia?", "¿Quién tiene la razón y quién no?", "¿Cuál relato es más largo?", "Una buena pregunta pide comparar contenido y evidencia, no declarar un ganador."),
        ("abc", "{F} ¿Cuál es una conclusión equilibrada sobre el cierre?", "Fue un proceso con causas económicas y consecuencias sociales que cada actor vivió y explicó de forma distinta", "Fue culpa exclusiva de la empresa", "Fue culpa exclusiva de los trabajadores", "Reconoce las causas, las consecuencias y las perspectivas sin atribuir toda la culpa a un solo actor."),
    ],
    ctx=("abc", "Un liceo ficticio prepara un documental sobre el cierre de un cine del barrio. Hay entrevistas al dueño, a una exempleada y a un vecino que iba cada semana, además de un informe municipal sobre locales cerrados. ¿Cómo conviene organizar el documental?", "Mostrar las cuatro perspectivas y distinguir hechos, explicaciones y valoraciones", "Mostrar solo la entrevista más emotiva", "Mostrar solo el informe municipal", "Presentar perspectivas distintas y separarlas por plano permite una comprensión más completa."),
    sc=[
        ("En Comprensión histórica: ¿cuáles son los tres planos que conviene separar al comparar relatos?", "Hechos, explicaciones y valoraciones", "Así se evita tratar un juicio como si fuera un dato."),
        ("¿Pueden dos relatos distintos ser ambos verdaderos en lo que cuentan?", "Sí, porque pueden destacar aspectos diferentes del mismo proceso", "Diferir en perspectiva no equivale a mentir."),
        ("¿Qué enfoque estudia las experiencias diarias de las personas?", "La historia de la vida cotidiana", "Se ocupa del trabajo, la familia y el barrio."),
    ],
    op=("Elige un caso de ejemplo. Caso 1: la apertura de un consultorio nuevo en un barrio. Caso 2: el traslado de una feria libre a otra calle. En el caso elegido hay tres relatos: de una persona usuaria, de una funcionaria municipal y de un comerciante o de una vecina cercana. "
        "Escribe un resumen de dos líneas para cada uno (tú los inventas, marcándolos de ejemplo) y una tabla que indique hechos aceptados, causas que destaca cada uno y valoraciones. Termina con una conclusión equilibrada.",
        "Caso 2. Usuaria: «Ahora llego más rápido.» Funcionaria: «Se movió por seguridad vial.» Comerciante: «Bajaron mis ventas.» Hecho aceptado: la feria se trasladó. Causas: seguridad vial. Valoraciones: mejor llegada, peor venta. Conclusión: el traslado tuvo beneficios y costos para distintos grupos.",
        ["inventa tres relatos distintos y coherentes con el caso", "separa hechos, explicaciones y valoraciones", "redacta una conclusión equilibrada sin tomar partido"],
        ["tabla con hechos, causas y valoraciones, y una conclusión"],
        ["poner la valoración como si fuera un hecho", "hacer que los tres relatos digan lo mismo", "concluir culpando a un solo actor"],
        "Pregunta: «¿qué parte de esta frase se podría comprobar?». Si no sabe, pídele subrayarla."),
    reinforce="Elige un hecho reciente de tu liceo y escribe dos relatos breves de personas distintas; marca hecho, explicación y valoración en cada uno.",
    extend="Explica por qué un mismo hecho puede estudiarse desde la historia política, la social y la cotidiana, y qué preguntas haría cada una.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (discurso y respuesta de ejemplo, ficticios). En un acto de aniversario de Lomas del Sur, un orador dice: «Esta comuna salió adelante gracias a un solo hombre, don Aurelio, que lo hizo todo.» "
     "Un historiador local responde: «Don Aurelio fue importante, pero los registros muestran un comité de 15 vecinos, una ley que permitió el fondo para el proyecto y una crisis económica que obligó a unirse.»")
build(
    O2, 4, F,
    use="Aprenderé a explicar cómo individuos y grupos actúan dentro de condiciones que no eligieron, y cómo se usa la historia en la vida pública, reconociendo relatos simplificados y anacronismos.",
    prior=["Reconozco sujetos históricos.", "Sé comparar perspectivas de un mismo proceso.", "Distingo hecho, explicación y valoración."],
    explain=[
        "Los sujetos históricos actúan, pero no en cualquier circunstancia. Las condiciones de su época, como las leyes, la economía, los recursos y las ideas disponibles, abren posibilidades y ponen límites. Explicar un proceso exige combinar ambas cosas: qué decidieron y lograron las personas y los grupos, y qué condiciones facilitaron o dificultaron su acción. Atribuirlo todo a un individuo o todo a las condiciones deja la explicación incompleta.",
        "El uso público de la historia es la manera en que el pasado se presenta en conmemoraciones, discursos, medios y escuelas para dar sentido al presente. Puede enriquecer la memoria colectiva, pero también simplificar: convertir un proceso colectivo en la hazaña de una sola persona, ocultar tensiones o presentar un solo relato como único. Reconocer estos usos es parte del conocimiento histórico crítico.",
        "Un anacronismo es juzgar o explicar una época con ideas, conocimientos o recursos que solo existen en otra. Por ejemplo, reprochar a quienes vivieron antes no haber usado herramientas que aún no existían. Evitar el anacronismo no significa justificarlo todo: significa entender primero las condiciones de la época y luego, si corresponde, valorar con criterios explícitos.",
    ],
    vocab=[("condiciones", "circunstancias de una época que abren posibilidades o ponen límites"), ("uso público de la historia", "manera en que el pasado se presenta en discursos, conmemoraciones y medios"), ("memoria colectiva", "recuerdo compartido por una comunidad"), ("simplificación", "relato que reduce un proceso complejo a pocos elementos"), ("anacronismo", "explicar o juzgar una época con ideas o recursos de otra"), ("conocimiento histórico crítico", "saber que revisa sus fuentes, sus usos y sus límites")],
    worked=[
        ("Combinar acción y condiciones", "Un grupo de apoderados de ejemplo logra que su escuela tenga un comedor, gracias a un programa nacional de alimentación escolar. ¿Cómo se combinan acción y condiciones?",
         ["Acción: los apoderados presentaron la solicitud y se organizaron.", "Condición: existía un programa nacional que hacía posible el comedor."],
         "La acción de los apoderados y el programa nacional se combinan para explicar el comedor"),
        ("Detectar un anacronismo", "Un estudiante dice: «Los vecinos de hace cincuenta años deberían haber avisado de la reunión por mensajes al celular.» ¿Qué error comete?",
         ["Exige un recurso, el mensaje al celular, que no existía en esa época.", "Debe preguntar primero con qué medios contaban y recién después valorar."],
         "Anacronismo: exige un recurso que no existía entonces"),
    ],
    mistakes=[("Explicar un proceso colectivo como obra de una sola persona.", "Se cree que la historia necesita héroes individuales.", "Revisa qué grupos, normas y circunstancias también intervinieron."),
              ("Juzgar a las personas del pasado con los recursos y conocimientos de hoy.", "Se olvida que cada época tiene sus propios límites.", "Primero reconstruye las condiciones de la época y luego valora con criterios explícitos.")],
    T=[
        ("abc", "{F} ¿A cuántos sujetos presenta como protagonistas el orador?", "Uno: don Aurelio", "Quince vecinos", "Ninguno", "El orador atribuye todo a un solo hombre."),
        ("abc", "{F} ¿Cuántos vecinos integraban el comité según el historiador?", "15", "1", "Más de cien", "El historiador menciona un comité de 15 vecinos."),
        ("abc", "En Comprensión histórica, ¿qué es el protagonismo?", "El papel principal de un sujeto en un proceso", "Un cargo público de alto nivel", "Una ley que reconoce derechos", "El protagonismo describe el papel que juega un sujeto en el proceso."),
        ("abc", "{F} ¿Qué tres elementos menciona el historiador además de don Aurelio?", "Un comité de vecinos, una ley y una crisis económica", "Un temporal, una guerra y un tratado", "Una empresa, un banco y un diario", "Está en su respuesta: comité, ley que permitió el fondo y crisis."),
        ("abc", "{F} La ley y la crisis económica pertenecen a", "Las condiciones en que actuaron los sujetos", "Las valoraciones del orador", "Las fuentes secundarias", "Son circunstancias que facilitaron o presionaron la acción de los vecinos."),
        ("abc", "En Comprensión histórica, ¿qué es un anacronismo?", "Explicar o juzgar una época con ideas o recursos de otra", "Citar una fuente sin fecha", "Contar un hecho en orden cronológico", "El anacronismo traslada a una época lo que solo existe en otra."),
        ("abc", "{F} ¿Qué falla tiene el relato del orador?", "Simplifica un proceso colectivo atribuyéndolo a una sola persona", "Contiene un error de ortografía", "No menciona el año", "Reduce un proceso con varios sujetos y condiciones a una sola figura."),
        ("abc", "{F} ¿Qué hace el historiador con la figura de don Aurelio?", "Reconoce su importancia y la sitúa dentro de un proceso colectivo y de condiciones", "La borra por completo", "La presenta como único responsable", "Equilibra el papel del individuo con el del grupo y el contexto."),
        ("abc", "En Comprensión histórica, ¿qué es el uso público de la historia?", "La manera en que el pasado se presenta en discursos, conmemoraciones y medios para dar sentido al presente", "La lista de documentos de un archivo", "Un tipo de impuesto", "Se refiere a cómo la sociedad usa y comunica el pasado."),
        ("abc", "{F} ¿Qué conclusión es más sólida sobre la mejora de la comuna?", "Fue obra de varias personas y condiciones, entre ellas don Aurelio", "Fue obra exclusiva de don Aurelio", "Fue consecuencia exclusiva de la crisis económica", "Combina la acción de un individuo, un grupo y las condiciones."),
        ("abc", "Un estudiante critica a unos vecinos de hace cincuenta años: «¿Por qué no pidieron los certificados por internet, en vez de hacer filas?» ¿Qué error comete?", "Un anacronismo: exige medios que no existían entonces", "Un error de cálculo", "Una generalización desde un caso", "Reprocha por no usar un recurso que pertenece a otra época."),
        ("abc", "{F} Para comprobar que el comité tenía realmente 15 vecinos, ¿qué conviene buscar?", "El acta de constitución del comité u otra fuente que lo registre", "Otro discurso de aniversario", "Una opinión sobre don Aurelio", "El historiador menciona registros, y esa afirmación debe comprobarse en ellos."),
        ("abc", "¿Por qué es valioso un conocimiento histórico crítico en una sociedad democrática?", "Permite revisar relatos oficiales y evitar mitos o simplificaciones", "Sirve para que nadie discuta el pasado", "Garantiza que exista un solo relato", "La revisión crítica de fuentes y relatos fortalece la deliberación pública."),
    ],
    ctx=("abc", "Una municipalidad ficticia prepara un afiche para el aniversario de una población, con la frase «Fundada por un solo vecino, sin ayuda de nadie». Una historiadora encuentra un acta con 40 familias fundadoras. ¿Qué conviene hacer?", "Corregir la frase para reflejar a las 40 familias y su contexto", "Mantenerla porque es más breve", "Eliminar el afiche para no discutir", "Una simplificación contradicha por un registro debe corregirse, sin perder el valor de la figura mencionada."),
    sc=[
        ("En Comprensión histórica: ¿por qué hay que considerar las condiciones además de las decisiones de los sujetos?", "Porque las condiciones abren posibilidades y ponen límites a la acción", "La acción siempre ocurre dentro de circunstancias."),
        ("¿Qué es una simplificación en el uso público de la historia?", "Un relato que reduce un proceso complejo a pocos elementos", "Suele atribuir todo a una persona o a un solo factor."),
        ("¿Cómo se evita un anacronismo?", "Entendiendo primero las condiciones de la época antes de valorar", "No significa justificarlo todo, sino situar el juicio."),
    ],
    op=("Elige un discurso de ejemplo. Discurso 1: «El liceo nunca tuvo problemas hasta que llegó la nueva directora.» Discurso 2: «Gracias a una sola ley, el barrio tiene hoy agua potable.» "
        "Para el discurso elegido escribe qué sujetos o condiciones simplifica, qué otros sujetos podrían haber intervenido (inventa dos, rotulados de ejemplo), qué fuentes revisarías y una versión corregida del discurso en dos frases.",
        "Discurso 2. Simplifica: atribuye todo a una ley. Otros sujetos: un comité de vecinos y la empresa de agua. Fuentes: actas del comité y el texto de la ley. Versión corregida: «El agua potable llegó al barrio por la acción de un comité vecinal y la ley que permitió financiarla.»",
        ["identifica lo que el discurso simplifica", "propone sujetos y condiciones adicionales plausibles", "indica fuentes para comprobarlo", "reescribe el discurso de forma más completa y sobria"],
        ["ficha con simplificación, sujetos, fuentes y versión corregida"],
        ["inventar hechos como si fueran comprobados", "reemplazar una simplificación por otra", "no proponer ninguna fuente"],
        "Pregunta: «¿qué dato de tu versión corregida es de ejemplo y cuál se podría comprobar?»."),
    reinforce="Elige una frase de una conmemoración que hayas oído y escribe qué sujetos o condiciones deja fuera.",
    extend="Explica la diferencia entre entender las razones de una persona del pasado y justificar todo lo que hizo, con un ejemplo de ejemplo.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 5 (exposición de ejemplo, ficticia). El museo de Lomas del Sur prepara la exposición «Historia de nuestra comuna» con cinco paneles: Panel 1, los alcaldes del último siglo; Panel 2, las obras públicas; Panel 3, las empresas más grandes; "
     "Panel 4, el club deportivo del centro; Panel 5, una junta de vecinos del barrio alto. Ningún panel incluye testimonios de mujeres ni de personas migrantes. "
     "Propuesta A: agregar un panel con entrevistas a mujeres que dirigieron organizaciones de la comuna. Propuesta B: agregar un panel con fotos de personas migrantes que llegaron a la comuna y sus oficios. "
     "La historia de los pueblos originarios de la zona debe contarla su propia comunidad, con apoyo de educadores y educadoras tradicionales.")
build(
    O2, 5, F,
    use="Aprenderé a evaluar qué sujetos y voces incluye o deja fuera un relato histórico y a proponer, con criterios, cómo ampliarlo, para valorar la importancia del conocimiento histórico en una sociedad plural.",
    prior=["Sé reconocer sujetos históricos.", "Sé contrastar fuentes de historia reciente.", "Sé evaluar interpretaciones con criterios."],
    explain=[
        "Todo relato histórico selecciona: elige unos sujetos, hechos y fuentes y deja otros fuera. Un silencio es un sujeto, un hecho o una voz que el relato no menciona. Los silencios no siempre son intencionales: a veces faltan fuentes o nadie las recogió. Detectarlos es una tarea del conocimiento histórico, porque una sociedad se entiende mejor cuando se conocen todos los sujetos que la hicieron, no solo los más visibles.",
        "Para decidir cómo ampliar un relato conviene usar criterios: la pertinencia (si la propuesta responde a un silencio real), las fuentes disponibles (si hay evidencia para sustentarla), el respeto a las personas (consentimiento, privacidad, trato sobrio de temas dolorosos) y la viabilidad (tiempo, espacio y recursos). Ampliar un relato es sumar voces y no necesariamente reemplazar las existentes, porque lo anterior también forma parte de la historia.",
        "Cuando se trata de pueblos originarios, no se escribe en su nombre: su historia y sus conocimientos la cuentan sus propias comunidades y quienes ejercen como educadores y educadoras tradicionales. Una sociedad democrática e inclusiva reconoce a todos sus sujetos y busca formas respetuosas de incorporar sus voces.",
    ],
    vocab=[("silencio histórico", "sujeto, hecho o voz que un relato no menciona"), ("selección", "elección de qué sujetos, hechos y fuentes se incluyen en un relato"), ("pertinencia", "grado en que una propuesta responde a un problema real"), ("viabilidad", "posibilidad real de llevar algo a cabo con el tiempo y los recursos disponibles"), ("consentimiento", "autorización libre e informada de una persona para usar su testimonio"), ("voz", "perspectiva de un sujeto expresada en un relato")],
    worked=[
        ("Detectar un silencio", "Un álbum de ejemplo del aniversario de una escuela solo muestra fotos de directores y de premios deportivos. ¿Qué silencios podrían existir?",
         ["El álbum selecciona a autoridades y deportistas.", "Quedan fuera estudiantes, funcionarios y familias que vivieron la escuela en el día a día."],
         "Silencios: estudiantes, funcionarios y familias"),
        ("Aplicar criterios", "Para ampliar el álbum se proponen: (1) entrevistas a exestudiantes, con permiso de cada persona; (2) copiar las fotos de otra escuela. ¿Cuál cumple mejor con pertinencia y respeto?",
         ["La propuesta 1 responde al silencio detectado y usa consentimiento.", "La propuesta 2 no responde al silencio y no se basa en fuentes propias."],
         "La propuesta 1: es pertinente y respetuosa"),
    ],
    mistakes=[("Reemplazar un relato por otro en lugar de ampliarlo.", "Se piensa que sumar voces exige borrar lo anterior.", "Mantén lo existente y agrega las voces que faltan, indicando sus fuentes."),
              ("Contar en nombre de un pueblo originario sin consultar a su comunidad.", "Se supone que basta con leer sobre el tema.", "Invita a la comunidad y a educadores/as tradicionales a contar su propia historia.")],
    T=[
        ("abc", "{F} ¿Cuántos paneles tiene la exposición actual?", "Cinco", "Cuatro", "Siete", "La ficha enumera del Panel 1 al Panel 5."),
        ("abc", "{F} ¿En qué panel aparecen las empresas?", "En el Panel 3", "En el Panel 1", "En el Panel 5", "El Panel 3 trata de las empresas más grandes."),
        ("abc", "En Comprensión histórica, ¿qué es un silencio histórico?", "Un sujeto, hecho o voz que el relato no menciona", "Una fuente que contradice a otra fuente", "Una fuente destruida a propósito", "Se refiere a lo que el relato deja fuera."),
        ("abc", "{F} ¿Qué voces faltan en los cinco paneles según la ficha?", "Mujeres y personas migrantes", "Alcaldes y empresarios", "Dirigentes de la junta de vecinos", "La ficha dice que ningún panel incluye testimonios de mujeres ni de migrantes."),
        ("abc", "{F} ¿Qué sujeto incorpora la Propuesta A?", "Mujeres que dirigieron organizaciones", "Personas migrantes", "Alcaldes del último siglo", "Su propuesta consiste en entrevistas a mujeres dirigentes de organizaciones."),
        ("abc", "{F} ¿Qué fuente propone usar la Propuesta B?", "Fotos de personas migrantes y sus oficios", "Entrevistas a mujeres", "Actas municipales", "Se basa en fotografías de las personas migrantes."),
        ("abc", "¿Cuál es una lista adecuada de criterios para evaluar una propuesta de ampliación?", "Pertinencia, fuentes disponibles, respeto a las personas y viabilidad", "Cantidad de visitantes esperados, fama de los participantes y costo del marco", "Antigüedad de las fotos, belleza del diseño y tamaño de la sala", "Los criterios deben medir si la propuesta responde a un silencio y si puede hacerse bien."),
        ("abc", "{F} Para la Propuesta A, ¿qué cuidado ético corresponde?", "Pedir el consentimiento de cada mujer antes de usar su testimonio", "Publicar las entrevistas sin avisar", "Cambiar sus nombres sin avisarles", "El consentimiento es un deber básico al trabajar con testimonios."),
        ("abc", "{F} Una propuesta C sugiere reemplazar los paneles 1 y 3 por paneles sobre mujeres y migrantes. ¿Qué problema tiene?", "Borra sujetos y procesos que también forman parte de la historia; es mejor ampliar", "No tiene ningún problema, porque lo nuevo siempre reemplaza a lo antiguo", "Repite el panel de obras públicas", "Ampliar suma voces sin eliminar las que ya están."),
        ("abc", "{F} Respecto de la historia de los pueblos originarios de la zona, ¿qué corresponde hacer?", "Invitar a su comunidad y a educadores/as tradicionales a contarla", "Escribirla sin consultar a nadie", "Omitirla por no tener datos", "Su historia la cuentan sus propias comunidades."),
        ("abc", "{F} Si ya existen las fotos de las personas migrantes, pero las entrevistas de las mujeres exigen permisos que tardarán, ¿qué conviene?", "Incorporar primero el panel B y planificar el A para después, explicando la decisión", "Eliminar ambas propuestas", "Hacer el panel A sin entrevistas", "La viabilidad permite avanzar con lo posible y dejar claro lo pendiente."),
        ("abc", "¿Qué aporta a la sociedad conocer más sujetos de su historia?", "Comprender mejor cómo se construyeron sus derechos e instituciones", "Cerrar el debate sobre el pasado", "Elegir a un solo grupo como protagonista", "Un relato plural explica mejor los procesos y sus desigualdades."),
        ("abc", "{F} ¿Qué características tendría un relato más completo de la exposición?", "Varios sujetos y fuentes distintas, declarando sus límites", "Un solo panel más largo", "Solo testimonios, sin documentos", "La pluralidad de sujetos y fuentes, con límites declarados, hace más sólido el relato."),
    ],
    ctx=("abc", "El centro de estudiantes de un liceo ficticio quiere preparar un mural por los 50 años del establecimiento. Hasta ahora solo hay fotos de actos oficiales. ¿Cuál es una buena primera acción?", "Preguntar quiénes faltan en las fotos y buscar testimonios de exalumnos, funcionarios y familias", "Pintar los actos oficiales y no consultar a nadie", "Usar un mural de otro liceo", "Detectar silencios antes de diseñar permite incorporar voces y fuentes reales."),
    sc=[
        ("En Comprensión histórica: ¿por qué todo relato histórico selecciona?", "Porque no puede incluir todos los sujetos, hechos y fuentes", "Elegir implica dejar cosas fuera, y eso debe reconocerse."),
        ("¿Qué significa ampliar un relato en vez de reemplazarlo?", "Sumar voces nuevas sin borrar las existentes", "Lo anterior también forma parte de la historia."),
        ("¿Quiénes cuentan la historia de un pueblo originario?", "Su propia comunidad, con apoyo de educadores y educadoras tradicionales", "No se escribe en su nombre."),
    ],
    op=("Elige un relato de ejemplo. Relato 1: un libro de aniversario de un club deportivo que menciona solo a los presidentes. Relato 2: un museo escolar con objetos de profesores y de directores. "
        "Escribe qué sujetos quedan fuera, dos propuestas para ampliarlo (con la fuente de cada una), cómo aplicarías los criterios de pertinencia, fuentes, respeto y viabilidad, y cuál harías primero y por qué.",
        "Relato 1. Fuera: socias y socios, entrenadores, familias. Propuesta A: entrevistas a socias (fuente: testimonios, con permiso). Propuesta B: fotografías de las ligas juveniles (fuente: álbumes familiares). Hago primero B porque ya hay fotos y requiere menos permisos.",
        ["identifica silencios con una razón", "propone dos ampliaciones con su fuente", "aplica los cuatro criterios", "justifica el orden de ejecución"],
        ["ficha con silencios, propuestas, criterios y decisión"],
        ["proponer reemplazar el relato en vez de ampliarlo", "no considerar el consentimiento", "elegir sin aplicar criterios"],
        "Pregunta: «¿qué fuente concreta usarías para esa voz?». Si no tiene ninguna, la propuesta no es viable aún."),
    reinforce="Elige una galería de fotos o un libro de aniversario que conozcas y escribe tres voces que faltan y una fuente para cada una.",
    extend="Explica con un ejemplo de ejemplo por qué ampliar un relato puede cambiar la manera en que una comunidad se ve a sí misma.",
)
