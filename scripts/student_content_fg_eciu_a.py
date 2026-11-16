"""Educación Ciudadana 3.º medio FG: OA 01 (fundamentos, atributos y dimensiones de la democracia y la ciudadanía) y OA 02 (acceso a la justicia y sistema judicial). Casos de ejemplo inventados."""
from __future__ import annotations

from fg_eciu_common import build

O1 = "FG-ECIU-3M-OAC-01"
O2 = "FG-ECIU-3M-OAC-02"

# ============================================================ OA 01, clase 1
F = ("Ficha 1 (país ficticio de ejemplo, Laguna Azul): hay elecciones libres cada cuatro años; existen varios partidos; los tribunales son independientes del gobierno; "
     "se puede criticar al gobierno en la prensa; un decreto exige permiso previo para reunirse en cualquier plaza.")
build(
    O1, 1, F,
    use="Aprenderé a explicar qué es la democracia y la ciudadanía, cuáles son sus atributos y dimensiones, y qué libertades, deberes del Estado y responsabilidades ciudadanas implican.",
    prior=["Sé que en Chile las autoridades se eligen por votación.", "Sé que las personas tienen derechos.", "Sé distinguir una norma de una opinión."],
    explain=[
        'La democracia es una forma de gobierno en que el poder proviene del pueblo: la ciudadanía elige a sus autoridades y estas deben rendirle cuentas. Sus atributos principales son elecciones libres y periódicas, pluralismo (varias opciones políticas), separación de poderes (el poder se reparte y se controla), Estado de derecho (todos obedecen las leyes, incluidas las autoridades) y respeto de las libertades fundamentales.',
        'Las libertades fundamentales son las que protegen a toda persona frente al poder: expresarse, reunirse, asociarse y pensar según su conciencia. Por eso el Estado tiene deberes: respetarlas, protegerlas y crear condiciones para ejercerlas. Pueden limitarse solo por ley y para proteger los derechos de otras personas, no porque a la autoridad le incomode lo que se dice. Reunirse es juntarse de forma ocasional en un lugar, como en una marcha; asociarse es organizarse de forma estable, como en una junta de vecinos.',
        'La ciudadanía es la condición de ser miembro de una comunidad política, con derechos y responsabilidades. Tiene dimensiones: civil (libertades, como expresarse), política (votar, ser elegido, participar en decisiones) y social (acceso a bienes como educación y salud). La democracia también es una forma de convivir: respeto, diálogo y cuidado de lo común.',
    ],
    vocab=[("democracia", "forma de gobierno en que el poder proviene del pueblo y las autoridades rinden cuentas"), ("pluralismo", "existencia y respeto de varias ideas y opciones políticas"), ("separación de poderes", "reparto del poder en distintos órganos que se controlan entre sí"), ("libertades fundamentales", "libertades básicas de toda persona, como expresarse, reunirse y asociarse"), ("ciudadanía", "condición de miembro de una comunidad política, con derechos y responsabilidades")],
    worked=[
        ("Reconocer un atributo", "En un país de ejemplo, un jurado independiente revisa si las autoridades cumplieron las leyes y puede sancionarlas. ¿Qué atributo de la democracia se ve?", ["Hay un órgano que controla a las autoridades.", "Ese control sirve para que nadie esté por sobre la ley."], "Estado de derecho y control del poder"),
        ("Clasificar una dimensión", "Una joven de ejemplo se inscribe en un taller gratuito de salud en su comuna. ¿Qué dimensión de la ciudadanía ejerce?", ["Accede a un servicio que cubre una necesidad básica.", "Eso corresponde a bienes sociales, no a votar ni a expresarse."], "Dimensión social"),
    ],
    mistakes=[("Creer que la democracia es solo votar cada cierto tiempo.", "Se olvidan las libertades, el control del poder y la participación entre elecciones.", "Revisa cada atributo: elecciones, pluralismo, separación de poderes, Estado de derecho y libertades."),
              ("Pensar que una libertad nunca puede limitarse.", "Se confunde limitar con eliminar; algunas limitaciones protegen a otros.", "Pregunta si la limita una ley y si protege derechos de otras personas.")],
    T=[
        ('abc', '¿Cuál enunciado describe mejor la democracia?', 'Forma de gobierno en que el poder proviene del pueblo y las autoridades rinden cuentas', 'Forma de gobierno en que un solo grupo decide y el resto debe obedecer las leyes', 'Sistema en que se vota una vez y después las autoridades no responden ante nadie', 'La democracia se define por el origen popular del poder y por la rendición de cuentas; las otras opciones describen el mando de un grupo o un voto sin control posterior.'),
        ('abc', '{F} ¿Qué atributo de la democracia muestra que existan varios partidos?', 'Pluralismo', 'Separación de poderes', 'Estado de derecho', 'Pluralismo es la existencia de varias opciones políticas; la separación de poderes se refiere a órganos que se controlan y el Estado de derecho a que todos obedecen la ley.'),
        ('abc', '{F} ¿Qué libertad fundamental se ejerce al criticar al gobierno en la prensa?', 'Libertad de expresión', 'Libertad de reunión', 'Libertad de asociación', 'Criticar públicamente es expresar una opinión; reunirse es juntarse en un lugar y asociarse es organizarse de forma estable.'),
        ('abc', '¿Qué significa que en una democracia el poder provenga del pueblo?', 'Que la ciudadanía elige a sus autoridades y estas deben rendirle cuentas', 'Que las autoridades se eligen una vez y después pueden decidir sin dar explicaciones', 'Que el pueblo vota cada ley y no necesita autoridades que gobiernen', 'El poder del pueblo se ejerce eligiendo autoridades que luego responden ante él; ni se renuncia a todo control ni se elimina a las autoridades.'),
        ('abc', '¿Cuál es un deber del Estado frente a los derechos?', 'Respetarlos, protegerlos y crear condiciones para ejercerlos', 'Respetarlos solo mientras la mayoría los apoye y retirarlos si deja de hacerlo', 'Protegerlos únicamente de otros particulares, no de las propias autoridades', 'Los derechos corresponden a todas las personas y el Estado debe garantizarlos también frente a sus propios órganos, sin depender de la opinión de la mayoría.'),
        ('abc', '¿Qué diferencia hay entre un derecho y una responsabilidad ciudadana?', 'El derecho puedo exigirlo; la responsabilidad es lo que me corresponde cumplir o cuidar para convivir', 'El derecho depende de que cumpla antes mi responsabilidad; si no cumplo, lo pierdo', 'El derecho es una obligación y la responsabilidad es una opción voluntaria', 'Los derechos de una persona no desaparecen por incumplir una responsabilidad; son cosas distintas: una se exige y la otra se asume.'),
        ('abc', '{F} El decreto exige permiso previo para reunirse en cualquier plaza. ¿Qué libertad fundamental limita?', 'La libertad de reunión', 'La libertad de asociación', 'La libertad de conciencia', 'Juntarse de forma ocasional en un lugar público es reunirse; asociarse es organizarse de forma estable y la conciencia se refiere al pensamiento propio.'),
        ('abc', '{F} ¿Qué atributo cumplen los tribunales independientes del gobierno?', 'Separación de poderes', 'Pluralismo', 'Elecciones periódicas', 'Que los jueces no dependan del gobierno reparte el poder en órganos que se controlan; el pluralismo y las elecciones se refieren a las opciones políticas y al voto.'),
        ('Tener acceso a educación pública, ¿a qué dimensión de la ciudadanía corresponde?', 'Dimensión social', 'La educación es un bien social básico: no es una libertad civil (como expresarse) ni una acción política (como votar).'),
        ('{F} ¿Por qué el decreto debilita la democracia de Laguna Azul aunque haya elecciones libres?', 'Porque restringe la libertad de reunión y, sin libertades, la participación y el control del poder pierden fuerza', 'Las elecciones son un atributo de la democracia, pero no bastan si se limitan libertades fundamentales como reunirse.'),
        ('abc', 'Alguien dice: «Si voto cada cuatro años, ya cumplí con la democracia». ¿Qué respuesta es más justa?', 'La democracia incluye además libertades, participación entre elecciones y rendición de cuentas', 'El voto es el atributo más importante, por lo que las demás libertades son secundarias', 'Votar es un derecho, pero no hace falta que las autoridades den cuentas después', 'Votar es solo uno de los atributos: sin libertades ni control de las autoridades, el voto cada cuatro años no basta.'),
        ('{F} Si además los jueces fueran nombrados y destituidos a gusto del gobierno, ¿qué atributo se afectaría?', 'La separación de poderes y la independencia de los tribunales', 'Los jueces dependerían de quien deben controlar, así que el poder dejaría de estar repartido.'),
        ('abc', '¿Cuál es un criterio válido para limitar una libertad fundamental?', 'Que una ley lo establezca para proteger los derechos de otras personas', 'Que la autoridad considere injustas las críticas que recibe', 'Que la mayoría de la población esté de acuerdo en restringirla', 'Una limitación necesita base legal y un fin legítimo; ni el malestar de la autoridad ni el apoyo de la mayoría bastan, porque serían arbitrarios.'),
    ],
    ctx=('abc', 'Un grupo de vecinas se organiza en una junta de vecinos para pedir una plaza segura. ¿Qué libertad fundamental ejercen principalmente?', 'La libertad de asociación', 'La libertad de reunión', 'La libertad de conciencia', 'Organizarse de forma estable en una junta es asociarse; reunirse sería solo juntarse un día en un lugar.'),
    sc=[
        ('¿Qué es la separación de poderes?', 'Que el poder se reparte en órganos que se controlan entre sí', 'El poder se reparte (por ejemplo, entre gobierno y tribunales) para que ninguno quede por encima de la ley.'),
        ('abc', '¿Cuál es una acción de la dimensión política de la ciudadanía?', 'Votar', 'Recibir atención de salud', 'Expresar una opinión en la prensa', 'Votar y ser elegido son acciones políticas; la salud es un bien social y opinar es una libertad civil.'),
        ('En Educación Ciudadana: ¿qué es el pluralismo?', 'La existencia y respeto de varias ideas y opciones políticas', 'Es la convivencia respetuosa de ideas y opciones distintas, que permite elegir entre alternativas.'),
    ],
    op=("Usa la {F} Escribe una tabla de tres filas: (1) dos atributos de la democracia que sí se cumplen en Laguna Azul y cómo lo sabes; (2) una libertad fundamental afectada y por qué; (3) un deber del Estado que no se cumple. Cierra con una recomendación de una frase que no favorezca a ningún partido.",
        "(1) Elecciones libres cada cuatro años y pluralismo (varios partidos). (2) Libertad de reunión, porque se exige permiso previo en toda plaza. (3) Respetar y proteger las libertades. Recomendación: revisar el decreto para limitar solo lo necesario y por ley.",
        ["nombra atributos con evidencia de la ficha", "relaciona una libertad con el hecho que la afecta", "propone sin tomar partido"], ["tabla de tres filas", "recomendación de una frase"], ["listar atributos sin citar la ficha", "proponer eliminar el decreto sin razones"],
        "Pregunta qué límite sí sería razonable para una reunión y quién debería decidirlo."),
    reinforce="Explica con tus palabras tres atributos de la democracia y da un ejemplo de cada uno.",
    extend="Anota una libertad que ejerzas esta semana y qué responsabilidad hacia otros conlleva.",
)

# ============================================================ OA 01, clase 2
F = ("Ficha 2 (caso de ejemplo): la comuna de Río Claro, ficticia, rechazó el permiso para una marcha pacífica de estudiantes que pedía más buses escolares. "
     "Fuentes: (1) el oficio municipal, que dice que la calle estará en obras; (2) una nota del diario local que muestra que no hay obras ese día; (3) la ordenanza municipal, que permite marchas avisadas con 48 horas de anticipación; los estudiantes avisaron con 72.")
build(
    O1, 2, F,
    use="Aprenderé a investigar un caso público: qué libertades y deberes están en juego, qué fuentes hay y qué se puede concluir de ellas.",
    prior=["Sé qué libertades fundamentales protege la democracia.", "Sé que el Estado tiene deberes frente a los derechos.", "Sé interrogar una fuente."],
    explain=[
        "Un caso público es un hecho que afecta a una comunidad y que se puede discutir con evidencia. Para investigarlo conviene partir con cuatro preguntas: qué ocurrió, quiénes participan, qué derechos o deberes están involucrados y qué fuentes lo muestran. Anotar primero los hechos, antes de opinar, evita mezclar lo comprobado con lo que uno supone.",
        "Las fuentes se comparan: un documento oficial (oficio, ordenanza) dice lo que la autoridad declara; una nota de prensa informa lo que observó un medio; un testimonio cuenta lo vivido por una persona. Cada una tiene un autor y un propósito. Si dos fuentes se contradicen, se anota la contradicción y se busca otra para resolverla, sin descartar ninguna por simpatía.",
        "Luego se conectan los hechos con los conceptos: ¿qué libertad se ejerce o se limita? ¿Qué deber tenía el Estado? ¿Se respetó el procedimiento que la propia norma exige? La conclusión debe decir hasta dónde llega la evidencia, por ejemplo «los datos sugieren que la negativa no cumplió la ordenanza», y qué falta por averiguar.",
    ],
    vocab=[("caso público", "hecho que afecta a una comunidad y puede discutirse con evidencia"), ("fuente oficial", "documento emitido por una autoridad, como un oficio o una ordenanza"), ("ordenanza", "norma municipal que regula asuntos de la comuna"), ("procedimiento", "pasos que una norma exige para tomar una decisión"), ("contradicción", "diferencia entre lo que afirman dos fuentes sobre el mismo hecho")],
    worked=[
        ("Separar hechos de opinión", "Un cartel de ejemplo dice: «La directora cerró la biblioteca, por eso odia leer». ¿Cuál es el hecho y cuál la opinión?", ["Hecho: la biblioteca fue cerrada.", "Opinión: atribuir una razón sin evidencia."], "Hecho: se cerró; opinión: «odia leer»"),
        ("Detectar contradicción", "Un oficio de ejemplo dice que el parque estaba cerrado por mantención; un video de ese día muestra el parque abierto. ¿Qué se anota?", ["Las dos fuentes se contradicen.", "No se elige una por simpatía: se busca otra fuente."], "Contradicción a resolver con otra fuente"),
    ],
    mistakes=[("Tomar una sola fuente como verdad completa.", "Cada fuente tiene un autor y un propósito que filtran lo que cuenta.", "Compara al menos dos fuentes y anota las diferencias."),
              ("Concluir culpas sin evidencia suficiente.", "Se pasa de lo que muestran los datos a lo que se supone.", "Escribe «los datos sugieren…» y lista lo que falta averiguar.")],
    T=[
        ('abc', '¿Qué conviene hacer primero al investigar un caso público?', 'Anotar los hechos antes de opinar sobre ellos', 'Buscar a quién se le puede atribuir la culpa para actuar rápido', 'Elegir la fuente que más se parezca a lo que uno piensa', 'Se parte por separar lo comprobado de lo supuesto; buscar culpables o fuentes simpáticas mezcla hechos con opiniones.'),
        ('abc', '{F} ¿Qué tipo de fuente es la ordenanza municipal?', 'Una fuente oficial', 'Una nota de prensa', 'Un testimonio personal', 'La ordenanza la emite la autoridad de la comuna; una nota de prensa informa lo que observó un medio y un testimonio cuenta lo vivido por una persona.'),
        ('abc', '{F} ¿Qué fuente informa lo que observó un medio de comunicación?', 'La nota del diario local', 'El oficio municipal', 'La ordenanza municipal', 'Una nota de prensa informa lo que un medio observó; el oficio y la ordenanza son documentos de la autoridad.'),
        ('=', '{F} Los estudiantes avisaron con 72 horas y la ordenanza exige 48. ¿Qué porcentaje más de anticipación que el mínimo tuvo el aviso?', '(72-48)*100//48', 'Se compara la diferencia con el mínimo exigido para ver cuánto lo superaron.', ' %'),
        ('abc', '{F} ¿Qué libertad protege directamente el poder juntarse en una calle para una marcha pacífica?', 'La libertad de reunión', 'La libertad de asociación', 'La libertad de conciencia', 'Una marcha es juntarse de forma ocasional en un espacio público; asociarse implica una organización estable y la conciencia es el pensamiento propio.'),
        ('abc', '{F} ¿Qué contradicción aparece entre las fuentes?', 'El oficio dice que habrá obras en la calle y la nota dice que ese día no las hay', 'La ordenanza exige 48 horas de aviso y la nota dice que hubo 72', 'El oficio rechaza el permiso y la nota informa que la marcha era pacífica', 'Una contradicción es una diferencia entre dos fuentes sobre el mismo hecho: aquí, si hay o no obras ese día.'),
        ('abc', '{F} ¿Por qué el aviso de los estudiantes cumple lo que pide la ordenanza?', 'Porque avisaron con 72 horas, más que las 48 exigidas como anticipación', 'Porque la ordenanza solo exige avisar, sin importar con cuánto tiempo', 'Porque el municipio nunca respondió al aviso', 'La ordenanza permite marchas avisadas con 48 horas de anticipación y 72 supera ese plazo.'),
        ('abc', '{F} ¿Por qué no basta el oficio para dar por comprobado que la calle estaría en obras?', 'Porque es la versión de una autoridad y otra fuente la contradice', 'Porque los oficios nunca dicen la verdad', 'Porque la nota del diario es una fuente oficial y vale más', 'Una fuente oficial también puede equivocarse o tener intereses; por eso se compara con otra, sin descartarla ni aceptarla de antemano.'),
        ('abc', '{F} ¿Qué conclusión es más ajustada a la evidencia?', 'Los datos sugieren que la negativa no se apoyó en la ordenanza ni en un hecho comprobado', 'Está probado que la autoridad actuó por motivos políticos y no por la ordenanza', 'La negativa fue legal porque la firmó una autoridad con atribuciones para hacerlo', 'Con estas fuentes solo se puede decir qué sugieren los datos; atribuir intenciones o dar por legal la decisión excede la evidencia.'),
        ('abc', '{F} ¿Qué falta averiguar para una conclusión sólida?', 'Si existía otro fundamento legal para negar el permiso', 'Cuántos estudiantes asistieron a la marcha', 'Qué opinan los estudiantes del alcalde', 'La discusión es si la negativa tuvo base; saber la asistencia o las opiniones no cambia eso.'),
        ('abc', '{F} ¿Qué deber tiene el municipio en este caso?', 'Respetar y proteger la libertad de reunión, limitándola solo por ley', 'Aceptar cualquier marcha, incluso sin ningún aviso previo', 'Decidir cada marcha según su criterio, sin ajustarse a una norma', 'El Estado debe respetar y proteger las libertades, y solo puede limitarlas por ley y con un fin legítimo.'),
        ('abc', '{F} Si dos fuentes se contradicen y no hay una tercera, ¿qué corresponde?', 'Anotar la contradicción y decir que la evidencia no alcanza', 'Quedarse con la fuente oficial porque es de una autoridad', 'Quedarse con la nota de prensa porque es independiente del municipio', 'Ninguna fuente se descarta por simpatía: sin una tercera, solo se puede reconocer que la evidencia no permite resolver.'),
        ('{F} Si la marcha se hubiera avisado con solo 24 horas, ¿qué cambiaría en el análisis?', 'Se incumpliría el aviso que menciona la ordenanza y habría que revisar si eso justifica negar el permiso', 'Con un aviso menor al exigido la negativa podría tener alguna base en el procedimiento, aunque aún habría que leer qué dice la norma para ese caso.'),
    ],
    ctx=('abc', 'Para investigar este caso, ¿cuál es la primera pregunta?', '¿Qué ocurrió y qué dicen las fuentes?', '¿Quién tiene la culpa y cómo se le sanciona?', '¿Qué opinan los vecinos de la marcha?', 'Primero se establecen los hechos con fuentes; las culpas y las opiniones vienen después.'),
    sc=[
        ('¿Qué es una ordenanza?', 'Una norma municipal que regula asuntos de la comuna', 'Es la norma de la municipalidad, como la que fija el aviso para una marcha.'),
        ('abc', '¿Cuál es una fuente oficial?', 'Un oficio municipal', 'Un rumor que circula en redes', 'Un testimonio de un vecino', 'Un oficio es un documento emitido por una autoridad; un rumor no tiene autor responsable y un testimonio cuenta lo vivido por una persona.'),
        ('¿Qué se debe hacer si dos fuentes se contradicen?', 'Anotar la contradicción y buscar otra fuente', 'No se descarta ninguna por simpatía: se anota la diferencia y se busca otra fuente para resolverla.'),
    ],
    op=("Con la {F} escribe un informe de cinco líneas: (1) qué ocurrió; (2) qué libertad y qué deber están en juego; (3) cuál fuente usarías primero y por qué; (4) una contradicción que detectas; (5) una pregunta que quedó sin responder. No culpes a nadie.",
        "(1) El municipio rechazó una marcha pacífica. (2) Libertad de reunión; deber de respetarla. (3) La ordenanza, porque fija el procedimiento. (4) El oficio dice obras y la nota dice que no hay obras. (5) ¿Existía otro motivo legal?",
        ["separa hechos de interpretación", "cita fuentes", "formula una pregunta pendiente"], ["informe de cinco líneas"], ["afirmar intenciones", "olvidar el procedimiento de la ordenanza"],
        "Pide que indique qué segunda fuente buscaría y dónde la encontraría."),
    reinforce="Escribe tres preguntas que harías a cualquier caso público antes de opinar.",
    extend="Observa una noticia local y anota qué fuentes cita y cuál propósito tiene cada una.",
)

# ============================================================ OA 01, clase 3
F = ("Ficha 3 (perspectivas de ejemplo): en el municipio ficticio de Altos del Sur se discute si prohibir carteles políticos en los postes. "
     "Perspectiva 1 (vecino): «Los carteles ensucian y son un peligro; que solo se permitan en paneles». "
     "Perspectiva 2 (organización cívica): «Los paneles son pocos y caros; prohibir los carteles reduce la libertad de expresión de quienes no tienen medios». "
     "Dato de ejemplo: la comuna tiene 8 paneles, que se arriendan por semana, y 14 organizaciones inscritas.")
build(
    O1, 3, F,
    use="Aprenderé a contrastar perspectivas sobre una libertad y a decir qué evidencia sostiene a cada una sin tomar partido.",
    prior=["Sé investigar un caso con fuentes.", "Sé que las libertades pueden limitarse solo por ley y para proteger a otros.", "Sé separar hechos de opiniones."],
    explain=[
        "Una perspectiva es la mirada de una persona o grupo según su situación e intereses. En una democracia es normal que dos perspectivas legítimas choquen: una valora el orden y la limpieza; otra, la libertad de expresión. Contrastar no es decidir quién gana, sino entender qué valor defiende cada una y con qué evidencia.",
        "Para contrastar se arma una tabla: qué afirma cada perspectiva, qué valor defiende, qué evidencia presenta y qué no responde. La evidencia puede ser un dato (cantidad de paneles), una norma o un testimonio. Un argumento es más fuerte cuando su evidencia se puede verificar y cuando reconoce el costo de lo que propone.",
        "También se busca el punto de acuerdo: ambos quieren una comuna ordenada y con voz para todos. A partir de ahí aparecen soluciones intermedias, por ejemplo más paneles o espacios gratuitos. Comparar con cuidado evita la falacia del «todo o nada», que presenta solo dos salidas cuando hay más.",
    ],
    vocab=[("perspectiva", "mirada de una persona o grupo según su situación y sus intereses"), ("valor", "idea de lo que se considera importante proteger, como el orden o la libertad"), ("evidencia", "dato, norma o testimonio que sostiene una afirmación"), ("punto de acuerdo", "idea que comparten posturas distintas"), ("falacia del todo o nada", "error de presentar solo dos salidas cuando existen más")],
    worked=[
        ("Valor y evidencia", "En un liceo de ejemplo, A dice «prohibamos los celulares porque distraen» y B dice «dejémoslos porque sirven para estudiar». ¿Qué valor defiende cada uno?", ["A defiende la concentración.", "B defiende el uso de recursos para aprender."], "A, concentración; B, acceso a recursos"),
        ("Buscar un acuerdo", "Dos vecinos de ejemplo discuten por una feria: uno quiere silencio, otro quiere trabajo. ¿Qué punto de acuerdo hay?", ["Ambos quieren que el barrio funcione bien.", "Se puede acordar horarios de la feria."], "Convivencia: horarios acordados"),
    ],
    mistakes=[("Elegir una perspectiva por simpatía antes de revisar su evidencia.", "La simpatía no sustituye los datos.", "Anota evidencia de ambas antes de decidir."),
              ("Creer que solo hay dos soluciones posibles.", "Se cae en el todo o nada.", "Busca opciones intermedias o combinadas.")],
    T=[
        ('abc', '¿Para qué sirve contrastar perspectivas?', 'Para entender qué valor defiende cada una y con qué evidencia, antes de decidir', 'Para elegir la perspectiva que cuente con más apoyo entre quienes participan en el debate', 'Para demostrar que una de las dos perspectivas está equivocada y debe descartarse', 'Contrastar es comparar valores y evidencias; no es contar apoyos ni buscar quién pierde.'),
        ('abc', '{F} ¿Qué valor defiende principalmente el vecino?', 'El orden, la limpieza y la seguridad del espacio público', 'La libertad de expresión de las organizaciones', 'El ahorro de recursos del municipio', 'El vecino habla de suciedad y peligro, es decir, de orden y seguridad.'),
        ('=', '{F} Si cada organización necesitara su propio panel, ¿cuántos paneles faltarían?', '14-8', 'Se compara el número de organizaciones con el de paneles existentes.', ' paneles'),
        ('abc', '{F} ¿Qué dato respalda la preocupación de la organización cívica?', 'Hay menos paneles (8) que organizaciones inscritas (14)', 'Hay 8 paneles en toda la comuna', 'El vecino considera peligrosos los carteles', 'Comparar paneles con organizaciones muestra que no alcanza para todas; la opinión del vecino no es un dato de la organización.'),
        ('abc', '{F} ¿Qué punto de acuerdo hay entre ambas posturas?', 'Que el espacio público esté ordenado y todas las voces puedan expresarse', 'Que se prohíba todo cartel político en la comuna', 'Que solo las organizaciones inscritas puedan expresarse', 'Un punto de acuerdo es lo que comparten posturas distintas: ambos quieren una comuna ordenada y con voz para todos.'),
        ('abc', '{F} ¿Qué no responde la perspectiva 1?', 'Cómo se expresarían quienes no pueden pagar un panel', 'Si los carteles pueden ser un peligro', 'Si los paneles son una alternativa a los postes', 'La perspectiva 1 ya habla del peligro y de los paneles; deja sin respuesta qué pasa con quienes no tienen recursos.'),
        ('abc', '{F} ¿Qué solución intermedia respeta ambas posturas?', 'Aumentar los paneles y reservar algunos gratuitos para organizaciones pequeñas', 'Permitir carteles en cualquier lugar, sin reglas', 'Prohibir los carteles en postes y mantener solo los 8 paneles actuales', 'Combina el orden que pide el vecino con el acceso a la expresión que pide la organización; las otras dejan de lado a una de las dos.'),
        ('abc', '{F} La cifra de 8 paneles frente a 14 organizaciones, ¿qué tipo de evidencia es?', 'Un dato verificable que puede contarse', 'Una opinión sobre lo que conviene hacer', 'Una norma que obliga a la comuna', 'Se puede contar y comprobar, a diferencia de una opinión; tampoco es una norma.'),
        ('abc', '{F} Alguien dice: «O se prohíben todos los carteles o se deja todo como está». ¿Qué error comete?', 'Falacia del todo o nada', 'Contrastar valores con evidencia', 'Buscar un punto de acuerdo', 'Presenta solo dos salidas cuando existen opciones intermedias, como más paneles.'),
        ('abc', '{F} ¿Cuál argumento es más fuerte para decidir?', 'Uno cuya evidencia se puede verificar y que reconoce el costo de lo que propone', 'Uno que repite su postura varias veces con mucha seguridad y sin cambiar de argumento', 'Uno que reúne más firmas que el otro, sin presentar otros datos que lo respalden', 'La fuerza de un argumento está en su evidencia verificable y en admitir costos, no en la insistencia ni en el número de firmas.'),
        ('abc', '{F} ¿Qué pregunta ayudaría a decidir mejor?', '¿Cuántos carteles dañan realmente los postes y cuánto cuesta arrendar un panel por semana?', '¿Qué postura tiene más seguidores en redes sociales y mayor cantidad de comentarios?', '¿Qué postura se presentó primero en la reunión de la junta y quién habló más tiempo?', 'Pide datos verificables sobre el daño y el costo; los seguidores o el orden de llegada no son evidencia.'),
        ('=', '{F} Si se agregan 10 paneles y se reserva 1 de cada 3 paneles para organizaciones sin recursos, ¿cuántos paneles quedarían reservados?', '(8+10)//3', 'Se suman los paneles existentes y los nuevos, y luego se toma un tercio.', ' paneles'),
        ('abc', '{F} ¿Qué riesgo tiene dejar solo paneles pagados para la expresión política?', 'Que quienes tienen menos recursos queden con menos posibilidades de expresarse', 'Que los carteles dejen de ensuciar los postes y que los vecinos reclamen menos', 'Que se prohíba la libertad de reunión en los espacios públicos de la comuna', 'El costo es una barrera para organizaciones con menos medios, lo que afecta su libertad de expresión.'),
    ],
    ctx=('abc', 'Una compañera dice: «Contrastar es elegir al que más me gusta». ¿Qué le respondes?', 'Contrastar es comparar valores y evidencias antes de decidir', 'Tiene razón: la simpatía es el mejor criterio cuando hay dos posturas', 'Contrastar es buscar cuál postura tiene más seguidores', 'Elegir por simpatía no es contrastar; se comparan valor y evidencia de cada postura.'),
    sc=[
        ('En Educación Ciudadana: ¿Qué es una perspectiva?', 'La mirada de una persona o grupo según su situación e intereses', 'Cada perspectiva nace de una situación e intereses distintos, por eso puede chocar con otra legítima.'),
        ('abc', '¿Qué es un punto de acuerdo?', 'Una idea que comparten posturas distintas', 'La postura que gana en una votación', 'La conclusión de la persona que habla primero', 'A partir de lo que ambos comparten se buscan soluciones intermedias.'),
        ('En la tabla de contraste, ¿qué se anota en la fila «qué no responde»?', 'Lo que esa postura deja sin explicar o sin resolver', 'Ayuda a ver los vacíos de cada argumento, por ejemplo, quién queda fuera de su propuesta.'),
    ],
    op=("Con la {F} arma una tabla con dos columnas (perspectiva 1 y 2) y cuatro filas: qué afirma, qué valor defiende, qué evidencia presenta, qué no responde. Termina con un punto de acuerdo y una solución intermedia.",
        "Perspectiva 1: afirma que los carteles ensucian; valor, orden; evidencia, un comentario sobre peligro; no responde cómo se expresan quienes no pagan paneles. Perspectiva 2: afirma que prohibir reduce la expresión; valor, libertad; evidencia, 8 paneles para 14 organizaciones; no responde por la limpieza. Acuerdo: ambos quieren una comuna ordenada. Solución: más paneles gratuitos.",
        ["identifica valores", "separa evidencia de opinión", "propone una salida intermedia"], ["tabla completa", "acuerdo y solución"], ["describir solo una postura", "repetir argumentos sin evidencia"],
        "Pregunta qué dato nuevo cambiaría su decisión."),
    reinforce="Elige un tema escolar y escribe dos perspectivas con su valor y su evidencia.",
    extend="Busca dos opiniones distintas sobre un tema de tu barrio y anota qué valor defiende cada una.",
)

# ============================================================ OA 01, clase 4
F = ("Ficha 4 (debate de ejemplo en un centro de estudiantes ficticio): se propone cerrar el patio a las 17:00 para evitar ruidos. "
     "Argumento A: «Hay que cerrar porque los vecinos reclaman; hay 12 reclamos este mes». "
     "Argumento B: «No hay que cerrar porque siempre se ha usado hasta más tarde». "
     "Argumento C: «Quienes ensayan teatro no tendrían espacio; podría cerrarse a las 19:00 y reservar un sector para ensayos».")
build(
    O1, 4, F,
    use="Aprenderé a deliberar con razones: afirmar una tesis, sostenerla con evidencia, escuchar objeciones y buscar una decisión compartida.",
    prior=["Sé contrastar perspectivas.", "Sé distinguir un hecho de una opinión.", "Sé qué libertades fundamentales existen."],
    explain=[
        "Deliberar es discutir con razones para tomar una decisión que afecta a un grupo. A diferencia de pelear o imponer, exige escuchar y estar dispuesto a cambiar de idea si aparecen mejores argumentos. Un argumento tiene una tesis (lo que sostengo), razones (por qué) y evidencia (datos o normas que lo respaldan).",
        "Hay argumentos débiles. «Siempre se ha hecho así» apela a la costumbre, no a una razón. «Tú no sabes de esto» ataca a la persona en vez de la idea. «Todos lo piensan» apela a la mayoría sin evidencia. Un buen argumento responde a las objeciones: reconoce lo valioso de la postura contraria y propone ajustes.",
        "Una buena deliberación sigue reglas: pedir la palabra, hablar sobre ideas y no sobre personas, citar evidencia y resumir el acuerdo al final. Si no hay consenso total, se puede votar, pero la votación sigue a la discusión y no la reemplaza. Así la decisión es legítima y la minoría se sabe escuchada.",
    ],
    vocab=[("deliberar", "discutir con razones para tomar una decisión que afecta a un grupo"), ("tesis", "idea central que una persona sostiene"), ("objeción", "razón que cuestiona una postura"), ("consenso", "acuerdo al que llegan todas las partes"), ("argumento ad hominem", "ataque a la persona en vez de a su idea")],
    worked=[
        ("Reconocer una tesis", "Una alumna de ejemplo dice: «Debemos tener un reciclaje en el liceo porque cada día se botan muchas botellas». ¿Cuál es su tesis y cuál su razón?", ["Tesis: debe haber reciclaje.", "Razón: cada día se botan muchas botellas."], "Tesis: reciclaje; razón: muchas botellas"),
        ("Responder una objeción", "Alguien responde: «El reciclaje cuesta». ¿Qué ajuste propondrías?", ["Reconoce el costo.", "Propone comenzar con un solo contenedor de prueba."], "Proponer una prueba pequeña"),
    ],
    mistakes=[("Usar «siempre se ha hecho así» como razón.", "La costumbre no explica por qué es conveniente.", "Agrega una razón que sirva hoy."),
              ("Atacar a quien habla en vez de a su idea.", "Se desvía la discusión.", "Responde al argumento y deja a la persona fuera.")],
    T=[
        ('abc', '¿Qué partes tiene un argumento?', 'Tesis, razones y evidencia', 'Opinión, rumor y consenso', 'Objeción, votación y acuerdo', 'Un argumento afirma una tesis, da razones y las respalda con evidencia; la objeción, la votación y el acuerdo son parte del debate, no del argumento.'),
        ('abc', '{F} ¿Qué argumento ofrece un dato verificable?', 'El argumento A, con sus 12 reclamos', 'El argumento B, con su referencia al uso del patio', 'El argumento C, con su mención del teatro', 'Solo A entrega una cifra que puede comprobarse; B apela a la costumbre y C describe una necesidad sin cifras.'),
        ('abc', '{F} El argumento B, ¿qué tipo de razón usa?', 'Apela a la costumbre', 'Aporta un dato verificable', 'Responde una objeción', '«Siempre se ha usado» no explica por qué conviene mantenerlo hoy.'),
        ('abc', '{F} ¿Qué hace el argumento C?', 'Reconoce el problema del ruido y propone otro horario y un espacio para ensayos', 'Defiende mantener todo igual porque así ha sido siempre y no hay que cambiar nada', 'Exige cerrar el patio antes de las 17:00 y sin ninguna excepción para nadie', 'C acepta el problema de los vecinos y ofrece un ajuste (19:00 y un sector), en vez de rechazar o endurecer.'),
        ('abc', '{F} ¿Qué es una objeción?', 'Una razón que cuestiona una postura y obliga a responderla', 'La conclusión con la que termina una discusión', 'El dato que apoya la tesis propia', 'Una objeción cuestiona; no cierra la discusión ni apoya la tesis propia.'),
        ('abc', '{F} Un estudiante dice: «El que propuso cerrar ni siquiera ensaya, así que no entiende». ¿Qué error comete?', 'Ataca a la persona en lugar de responder a su argumento', 'Presenta una objeción con evidencia sobre el horario del patio', 'Apela a la costumbre del patio, porque siempre se ha usado', 'No discute si cerrar el patio conviene, sino a quien lo propuso.'),
        ('abc', '{F} ¿Qué propone el argumento C además de cambiar la hora?', 'Reservar un sector para los ensayos', 'Cerrar el patio durante todo el día', 'Pedir a los vecinos que dejen de reclamar', 'Ofrece espacio a quienes ensayan, que es el grupo que perjudicaría el cierre a las 17:00.'),
        ('=', '{F} Con el cierre a las 19:00 en lugar de las 17:00, ¿cuántas horas más a la semana (5 días) queda abierto el patio?', '(19-17)*5', 'Se calcula cuántas horas más al día y se multiplica por los días.', ' horas'),
        ('=', '{F} Supón que de los 12 reclamos, 9 ocurrieron después de las 19:00. ¿Qué porcentaje es?', '9*100//12', 'Se compara la parte con el total de reclamos.', ' %'),
        ('abc', '{F} Con ese dato supuesto (9 de los 12 reclamos después de las 19:00), ¿qué postura queda mejor apoyada?', 'C: cerrar a las 19:00 evita la mayoría de los reclamos y protege los ensayos', 'B: la costumbre explica que haya pocos reclamos', 'A: cerrar a las 17:00 es la única forma de reducir los reclamos', 'Si el 75 % de los reclamos es posterior a las 19:00, cerrar a esa hora los evita en su mayoría y deja tiempo de ensayo.'),
        ('abc', '{F} Un estudiante pide: «Votemos ya, sin discutir». ¿Qué falla?', 'Se vota sin haber escuchado razones, y la votación debe seguir a la discusión', 'Votar nunca es válido en una deliberación', 'Hay que esperar a que todos estén de acuerdo antes de votar', 'La votación puede cerrar una deliberación, pero no reemplazarla; tampoco hay que esperar unanimidad.'),
        ('abc', '{F} ¿Qué pregunta pide más evidencia al argumento A?', '¿A qué horas ocurrieron los reclamos?', '¿Quién redactó el reclamo más largo?', '¿Cuántos años lleva el patio en uso?', 'Saber en qué horarios hubo ruido ayuda a decidir qué horas limitar.'),
        ('abc', '{F} ¿Qué hace legítima la decisión si no hay consenso?', 'Votar después de escuchar las razones y resumir el acuerdo', 'Que decida el grupo que habló primero, sin escuchar al resto del curso', 'Que la minoría acepte sin dar sus razones y sin quedar en el registro', 'La legitimidad viene de una discusión con razones y de una votación posterior; la minoría debe sentirse escuchada.'),
    ],
    ctx=('abc', 'En una asamblea alguien dice: «Todos piensan igual que yo». ¿Qué corresponde?', 'Pedir evidencia de que realmente muchos lo piensan', 'Aceptarlo, porque si son todos tiene que ser verdad', 'Responder que quien lo dice no sabe del tema', '«Todos lo piensan» no es evidencia; y descalificar a la persona sería otro error.'),
    sc=[
        ('¿Qué es deliberar?', 'Discutir con razones para tomar una decisión que afecta a un grupo', 'Deliberar exige escuchar y estar dispuesto a cambiar de idea con mejores argumentos.'),
        ('abc', '¿Cuál es un argumento débil?', '«Siempre se ha hecho así»', '«Hay 12 reclamos este mes»', '«Podemos cerrar a las 19:00 y reservar un sector»', 'La costumbre no explica por qué es conveniente hoy; los otros usan un dato y una propuesta.'),
        ('En Educación Ciudadana: ¿Qué es una tesis?', 'La idea central que alguien sostiene', 'Es lo que se defiende y para lo cual se dan razones y evidencia.'),
    ],
    op=("Con la {F} escribe un argumento de cuatro oraciones a favor de una de las tres posturas: tesis, una razón, evidencia o dato de la ficha, y una respuesta a una objeción. Luego escribe cómo cerrarías la discusión con una votación respetuosa.",
        "Tesis: conviene la propuesta C. Razón: da una solución a los vecinos y a quienes ensayan. Evidencia: hay 12 reclamos y existen ensayos de teatro. Objeción: «cuesta organizar el sector»; respuesta: se puede probar un mes. Cierre: leer las tres posturas, votar y resumir el acuerdo.",
        ["incluye tesis, razón y evidencia", "responde a una objeción", "propone un cierre respetuoso"], ["argumento de cuatro oraciones", "cierre de la discusión"], ["usar la costumbre como única razón", "olvidar la objeción"],
        "Pregunta qué parte de la postura contraria sí le parece valiosa."),
    reinforce="Escribe un argumento breve sobre un tema escolar con tesis, razón y evidencia.",
    extend="Observa una discusión en tu entorno y anota si se usaron razones, ataques a personas o apelaciones a la costumbre.",
)

# ============================================================ OA 01, clase 5
F = ("Ficha 5 (diagnóstico de ejemplo en el liceo ficticio Los Aromos): 40 estudiantes encuestados; 28 dicen conocer sus derechos como estudiantes y 12 no; "
     "10 de los 12 no los conocen porque nunca se les explicaron. Recursos del curso: 3 semanas, un diario mural, 15 estudiantes voluntarios.")
build(
    O1, 5, F,
    use="Aprenderé a diseñar una acción democrática pequeña: objetivo, participantes, pasos, recursos y una forma de saber si funcionó.",
    prior=["Sé deliberar con razones.", "Sé qué derechos y responsabilidades tiene la ciudadanía.", "Sé leer una cifra simple."],
    explain=[
        "Una acción democrática es una iniciativa en que personas se organizan para mejorar algo común usando medios pacíficos y respetuosos de los derechos de otros. Puede ser informar, proponer una norma o pedir una reunión a una autoridad. Parte de un diagnóstico: qué problema hay, a quiénes afecta y qué datos lo muestran.",
        "Un buen diseño tiene un objetivo claro y medible («que 30 de 40 estudiantes conozcan sus derechos»), participantes con roles, pasos con plazos, recursos disponibles y un indicador para saber si resultó. Además considera riesgos, por ejemplo que el mensaje no llegue a todos, y define cómo se corregirá.",
        "La acción debe respetar las libertades y el bien común: no usar la fuerza, no presionar ni humillar, y dar voz a quienes piensan distinto. Al terminar se evalúa con el indicador, se reconoce lo logrado y se decide si repetirla, ajustarla o cerrarla. Así se ejerce la ciudadanía de forma responsable.",
    ],
    vocab=[("acción democrática", "iniciativa pacífica y organizada para mejorar algo común"), ("diagnóstico", "descripción del problema con datos"), ("objetivo medible", "meta que se puede verificar con un número o hecho"), ("indicador", "dato que muestra si se logró el objetivo"), ("rol", "tarea que asume cada participante")],
    worked=[
        ("Plantear un objetivo medible", "En un liceo de ejemplo, 20 de 50 estudiantes saben dónde pedir ayuda y se quiere llegar a 35. ¿Qué objetivo medible se plantea?", ["Se parte de 20 y se quiere llegar a 35.", "Se expresa con un número comprobable."], "Que 35 de 50 sepan dónde pedir ayuda"),
        ("Elegir un indicador", "Si el objetivo es que más personas lean el diario mural, ¿qué indicador sirve?", ["Debe ser algo que se pueda contar.", "Por ejemplo, cuántos responden bien una breve encuesta."], "Número de estudiantes que contestan bien la encuesta"),
    ],
    mistakes=[("Proponer un objetivo vago como «que todos participen mejor».", "No se puede comprobar si se logró.", "Escríbelo con un número o un hecho observable."),
              ("Olvidar el riesgo de no llegar a todos.", "Se asume que el mensaje será recibido.", "Piensa quién podría quedar fuera y cómo incluirlo.")],
    T=[
        ('abc', '¿Para qué sirve el diagnóstico en una acción democrática?', 'Para describir el problema con datos antes de actuar', 'Para decidir quién dirigirá la acción y quiénes serán los voluntarios', 'Para evaluar el resultado al final y decidir si se repite', 'El diagnóstico muestra qué problema hay, a quiénes afecta y qué datos lo muestran.'),
        ('=', '{F} ¿Qué porcentaje de los 40 encuestados dice conocer sus derechos?', '28*100//40', 'Se compara la cantidad que los conoce con el total de encuestados.', ' %'),
        ('abc', '{F} ¿Qué problema muestran los datos?', 'De quienes no conocen sus derechos, casi todos dicen que nunca se los explicaron', 'La mayoría del liceo no conoce sus derechos, por lo que hay que informar a todos', 'Faltan voluntarios para informar y por eso los estudiantes no conocen sus derechos', '10 de los 12 que no los conocen señalan que nunca se los explicaron; en cambio, 28 de 40 sí los conocen.'),
        ('abc', '{F} ¿Cuál es un objetivo medible?', 'Que, al terminar las 3 semanas, al menos 36 de los 40 conozcan sus derechos', 'Que los estudiantes sean más participativos en el liceo durante todo el año escolar', 'Que se pegue la mayor cantidad posible de afiches en todos los pasillos del liceo', 'Un número y un plazo permiten comprobar si se logró.'),
        ('=', '{F} Si la meta es que 36 de los 40 conozcan sus derechos, ¿cuántos de los 12 que hoy no los conocen deben aprenderlos?', '36-28', 'Se resta lo que ya se cumple a la meta.', ' estudiantes'),
        ('abc', '{F} Con los recursos del curso, ¿qué canal es posible?', 'Diario mural más conversaciones breves en cada curso a cargo de los voluntarios', 'Una campaña de televisión durante tres meses con presencia en medios nacionales', 'Un seminario externo con expertos pagados y transmisión en vivo a todo el país', 'Solo la primera usa recursos que la ficha entrega.'),
        ('abc', '{F} ¿Qué indicador mide si funcionó?', 'Número de estudiantes que contestan bien una breve encuesta final', 'Cantidad de afiches pegados en el diario mural durante las tres semanas', 'Número de voluntarios que se inscribieron para participar en la campaña', 'Los afiches y los inscritos miden la actividad; la encuesta mide el resultado.'),
        ('abc', '{F} ¿Cuál de estas medidas respeta la libertad de las personas?', 'Invitar a conversaciones voluntarias y aceptar que alguien no participe', 'Hacer que cada curso firme que está de acuerdo con la campaña', 'Exigir asistencia a los cursos con menos conocimiento', 'Una acción democrática es voluntaria y no presiona.'),
        ('abc', '{F} ¿Por qué conviene asignar roles?', 'Para que cada voluntario sepa qué tarea le toca y se evite duplicar esfuerzos', 'Para que algunos voluntarios decidan por los demás sin consultarlos', 'Para que todos los voluntarios hagan exactamente lo mismo', 'Los roles reparten el trabajo de forma clara; no buscan jerarquía ni uniformidad.'),
        ('abc', '{F} Un riesgo posible es que el mensaje no llegue a todos. ¿Qué medida lo reduce?', 'Combinar el diario mural con conversaciones breves en cada curso', 'Pegar el mensaje una sola vez y confiar en que será leído', 'Pedir a los estudiantes que informen a los demás por su cuenta', 'Usar más de un canal alcanza a personas que no pasan por el diario mural.'),
        ('=', '{F} Si cada voluntario logra explicar los derechos a 2 de los 12 estudiantes que aún no los conocen, ¿cuántos voluntarios se necesitan para alcanzar a los 12?', '12//2', 'Se reparte el total de estudiantes entre los que alcanza cada voluntario.', ' voluntarios'),
        ('abc', '{F} Si no se logra la meta, ¿qué corresponde?', 'Revisar con el indicador qué falló y ajustar la acción', 'Repetir exactamente lo mismo con más afiches', 'Cerrar la acción sin decir nada para evitar críticas', 'La evaluación sirve para aprender y decidir si repetir, ajustar o cerrar.'),
        ('abc', '{F} Si al final 31 de los 40 conocen sus derechos y la meta era 36, ¿qué conclusión es correcta?', 'La acción mejoró la situación (de 28 a 31) pero no alcanzó la meta', 'La acción fracasó porque no hubo ningún cambio', 'La meta se cumplió porque más de la mitad conoce sus derechos', 'Pasar de 28 a 31 es una mejora, y 31 es menor que 36, por lo que la meta no se alcanzó.'),
    ],
    ctx=('abc', 'Un grupo de ejemplo quiere que la municipalidad repare un paso peatonal. ¿Cuál es un primer paso democrático?', 'Reunir datos del problema y pedir una reunión por escrito', 'Cortar la calle sin aviso hasta que respondan', 'Esperar a que otra persona haga el reclamo', 'Se actúa de forma pacífica y con evidencia.'),
    sc=[
        ('En Educación Ciudadana: ¿Qué es un indicador?', 'Un dato que muestra si se logró el objetivo', 'Es lo que se mide al final, como cuántas personas responden bien la encuesta.'),
        ('abc', '¿Cuál es un objetivo medible?', 'Que 30 personas firmen la petición', 'Que haya mejor convivencia en el liceo', 'Que todos estén más motivados', 'Solo el primero se puede comprobar con un número.'),
        ('¿Por qué evaluar al final?', 'Para decidir si repetir, ajustar o cerrar la acción', 'Con el indicador se sabe si resultó y qué corregir.'),
    ],
    op=("Con la {F} diseña una acción en una tabla: objetivo medible, participantes y roles, tres pasos con semana, recurso, un riesgo y un indicador. Escribe una frase que explique cómo respeta las libertades de las demás personas.",
        "Objetivo: que 36 de 40 conozcan sus derechos. Roles: 5 voluntarios en el diario mural, 10 en las conversaciones por curso. Pasos: semana 1, redactar el mural; semana 2, conversaciones; semana 3, encuesta final. Riesgo: que no llegue a todos. Indicador: respuestas correctas en la encuesta. Es voluntaria y respeta opiniones.",
        ["objetivo medible", "pasos con plazo", "indicador claro"], ["tabla de diseño", "frase de respeto a libertades"], ["objetivo sin número", "actividad sin indicador"],
        "Pregunta cómo se enteraría si alguien quedó fuera."),
    reinforce="Escribe un objetivo medible para mejorar algo en tu curso.",
    extend="Elige un problema de tu comunidad y anota qué dato lo muestra y quién podría ayudar.",
)

# ============================================================ OA 02, clase 1
F = ("Ficha 6 (caso de ejemplo): Camila, vecina de una comuna ficticia, quiere reclamar porque una empresa le cobra una deuda ya pagada. "
     "Hay un juzgado civil a 40 kilómetros de su casa, una corporación de asistencia jurídica gratuita en el centro de la comuna y una mediación municipal para reclamos pequeños. "
     "Camila trabaja de lunes a viernes.")
build(
    O2, 1, F,
    use="Aprenderé qué significa acceder a la justicia, cuáles son las principales características del sistema judicial y qué mecanismos existen para resguardar mis derechos.",
    prior=["Sé que las personas tienen derechos.", "Sé que existen tribunales.", "Sé qué es una ley."],
    explain=[
        'Acceder a la justicia es poder acudir a una instancia imparcial para que se resuelva un conflicto o se proteja un derecho, de forma real y no solo teórica. Existen barreras: la distancia, el costo, la falta de información y el lenguaje complejo. Un sistema judicial democrático busca reducirlas con asistencia gratuita, atención cercana y explicaciones claras. También pesa el tiempo: muchos trámites se hacen en horario laboral.',
        'El sistema judicial se caracteriza por jueces independientes e imparciales, debido proceso (reglas justas para juzgar), derecho a defensa, publicidad de los juicios, presunción de inocencia en materia penal y posibilidad de apelar. Hay distintos tribunales según el asunto: civiles, de familia, laborales y penales. La Corte Suprema es el tribunal de mayor jerarquía.',
        'Hay mecanismos de acceso: asistencia jurídica gratuita para quien no puede pagar un abogado, defensa penal pública, mediación para llegar a acuerdos sin juicio y acciones constitucionales para proteger derechos fundamentales cuando una autoridad o un particular los afecta de forma ilegal o arbitraria. Conocerlos permite elegir el camino adecuado.',
    ],
    vocab=[("acceso a la justicia", "posibilidad real de acudir a una instancia imparcial para resolver un conflicto o proteger un derecho"), ("debido proceso", "conjunto de reglas justas con que se debe juzgar"), ("imparcial", "que no favorece a ninguna de las partes"), ("mediación", "proceso en que un tercero ayuda a llegar a un acuerdo sin juicio"), ("apelar", "pedir que un tribunal superior revise una decisión")],
    worked=[
        ("Reconocer una barrera", "Don Mario, de una comuna de ejemplo, no reclama por una multa porque cree que no entenderá los trámites. ¿Qué barrera aparece?", ["No sabe cómo hacerlo ni entiende el lenguaje.", "Esa es una barrera de información y lenguaje."], "Falta de información y lenguaje complejo"),
        ("Elegir un mecanismo", "Una familia de ejemplo no puede pagar abogado y necesita orientación para un reclamo. ¿Qué mecanismo sirve?", ["Hay asistencia jurídica gratuita.", "Su fin es ayudar a quien no puede pagar."], "Asistencia jurídica gratuita"),
    ],
    mistakes=[("Pensar que acceder a la justicia es solo existir un tribunal.", "Se ignora que las barreras impiden usarlo.", "Revisa distancia, costo, información y lenguaje."),
              ("Creer que todo conflicto debe ir a juicio.", "Hay mediación y otras vías que pueden resolverlo.", "Pregunta si puede resolverse con un acuerdo.")],
    T=[
        ('abc', '¿Qué significa acceder a la justicia?', 'Poder acudir en la práctica a una instancia imparcial para resolver un conflicto', 'Que existan tribunales en alguna parte del país, aunque sea difícil llegar a ellos', 'Ganar siempre el caso que se presenta, porque la ley favorece a quien reclama', 'Acceder es poder usar el sistema de verdad; que exista un tribunal o ganar no define el acceso.'),
        ('abc', '¿Qué es el debido proceso?', 'Reglas justas con que se debe juzgar, como ser oído y poder defenderse', 'El tiempo máximo que puede durar un juicio, que fija cada tribunal', 'La posibilidad de elegir al juez que se prefiera para el caso', 'Garantiza que las partes sean escuchadas con reglas conocidas; no fija plazos ni permite elegir juez.'),
        ('abc', '¿Qué significa que un juez sea imparcial?', 'No favorece a ninguna de las partes', 'Siempre da la razón a quien reclama primero', 'Resuelve según lo que prefiere la mayoría', 'La imparcialidad exige no inclinarse ni por una parte ni por la opinión mayoritaria.'),
        ('abc', '{F} El juzgado civil está a 40 kilómetros de la casa de Camila. ¿Qué barrera de acceso refleja?', 'La distancia, que encarece y alarga el trámite', 'La falta de información sobre sus derechos', 'El lenguaje técnico de los tribunales', '40 kilómetros implican gasto y tiempo de traslado.'),
        ('abc', '{F} Camila trabaja de lunes a viernes. ¿Qué barrera práctica puede enfrentar?', 'Falta de tiempo para hacer trámites que suelen ser en horario laboral', 'El lenguaje complejo de los documentos que debe firmar en el trámite', 'El costo de contratar un abogado particular para presentar el reclamo', 'El dato de la ficha es su horario de trabajo, lo que se relaciona con el tiempo disponible.'),
        ('abc', '¿Para qué sirve la mediación?', 'Para llegar a un acuerdo con ayuda de un tercero, sin llegar a juicio', 'Para obtener una sentencia que obligue a la otra parte', 'Para que un juez castigue a quien incumplió', 'La mediación facilita acuerdos entre las partes; la sentencia y el castigo son propios de los tribunales.'),
        ('abc', '{F} Si el monto de la deuda es pequeño, ¿qué vía puede probar Camila antes del juzgado?', 'La mediación municipal', 'La defensa penal pública', 'Una apelación ante un tribunal superior', 'Para reclamos pequeños la ficha menciona la mediación; la defensa penal es para asuntos penales y apelar supone una decisión previa.'),
        ('abc', '{F} Camila no puede pagar un abogado y necesita orientación para reclamar. ¿Qué mecanismo le sirve?', 'La asistencia jurídica gratuita', 'La defensa penal pública', 'La mediación municipal', 'La asistencia jurídica gratuita orienta a quien no puede pagar; la defensa penal es para acusados y la mediación busca acuerdos.'),
        ('abc', '{F} ¿Por qué un juzgado más cercano mejora el acceso?', 'Reduce costos y tiempos de traslado', 'Garantiza que el juez falle a favor de quien reclama', 'Elimina la necesidad de presentar pruebas', 'La cercanía disminuye una barrera; no cambia el resultado ni los requisitos.'),
        ('abc', 'Una autoridad afecta de forma ilegal o arbitraria un derecho fundamental. ¿Qué mecanismo existe?', 'Una acción constitucional', 'Una mediación obligatoria entre la autoridad y la persona', 'La asistencia jurídica gratuita, que reemplaza al tribunal', 'Las acciones constitucionales protegen derechos fundamentales; la asistencia gratuita orienta pero no reemplaza al tribunal.'),
        ('abc', '{F} Camila no sabe cuál de los tres servicios sirve para su caso. ¿Qué medida reduce esa barrera?', 'Información en lenguaje claro sobre cada servicio y cómo llegar', 'Un juzgado nuevo en su misma calle que atienda solo a los vecinos', 'Un abogado particular para cada vecino que quiera reclamar por una deuda', 'La barrera es de información; las otras medidas son costosas y no la resuelven.'),
        ('abc', '¿Para qué sirve apelar?', 'Para pedir que un tribunal superior revise una decisión', 'Para pedir que otro abogado reemplace al defensor', 'Para pedir que el juicio se haga en otra comuna', 'La apelación permite revisar lo decidido por un tribunal.'),
        ('abc', 'Una persona acusada de un delito debe ser considerada inocente mientras no se demuestre lo contrario. ¿Qué rasgo del sistema judicial es?', 'Presunción de inocencia', 'Mediación entre las partes del conflicto', 'Apelación ante un tribunal superior', 'Es la garantía penal de inocencia hasta que se pruebe la culpa.'),
    ],
    ctx=('abc', 'Una persona mayor no lee bien y debe hacer un trámite judicial. ¿Qué medida facilita su acceso?', 'Explicarle en lenguaje claro y orientarla en cada paso', 'Entregarle un formulario más largo para que lo lea en casa', 'Pedirle que vuelva con un familiar que sepa', 'El lenguaje claro reduce la barrera; las otras trasladan el problema a la persona.'),
    sc=[
        ('abc', '¿Cuál de estas es una barrera de acceso a la justicia?', 'El costo de contratar un abogado', 'Que exista la apelación', 'Que los juicios sean públicos', 'El costo puede impedir reclamar; la apelación y la publicidad son garantías.'),
        ('abc', '¿Cuál es un rasgo del sistema judicial democrático?', 'Jueces independientes e imparciales', 'Juicios secretos en todos los casos', 'Jueces nombrados por una de las partes', 'La independencia y la imparcialidad aseguran que nadie juzgue en su propio favor.'),
        ('En Educación Ciudadana: ¿Qué es mediar?', 'Ayudar a las partes a llegar a un acuerdo sin juicio', 'El mediador no impone una decisión: facilita el acuerdo.'),
    ],
    op=("Con la {F} escribe en cinco líneas: (1) dos barreras que enfrenta Camila; (2) qué servicio usarías primero y por qué; (3) qué debería haber si su reclamo no se resuelve; (4) una duda que tendrías que aclarar con un abogado o abogada.",
        "(1) Distancia al juzgado y falta de tiempo. (2) Asistencia jurídica gratuita, porque orienta sin costo. (3) Un camino judicial con derecho a apelar. (4) ¿Qué documentos necesito para probar que pagué?",
        ["nombra barreras reales", "elige un mecanismo con razón", "reconoce que algo debe consultarse a un abogado"], ["cinco líneas"], ["decidir sin considerar el costo", "afirmar plazos legales sin saberlos"],
        "Pregunta qué barrera sería más difícil de superar y cómo podría ayudarla su comunidad."),
    reinforce="Escribe tres barreras de acceso a la justicia y una medida para reducir cada una.",
    extend="Averigua con una persona adulta si en tu comuna hay servicios de asistencia jurídica gratuita.",
)

# ============================================================ OA 02, clase 2
F = ("Ficha 7 (caso de ejemplo): un trabajador ficticio, Sergio, recibió una carta de despido con fecha del 5 de junio, pero sostiene que dejó de trabajar el 20 de mayo y que no se le pagó el sueldo de mayo. "
     "Documentos: (1) carta de despido; (2) liquidación de sueldo de abril; (3) mensajes con su jefa del 20 de mayo. Primera instancia: reclamar ante la inspección del trabajo; si no hay acuerdo, tribunales laborales.")
build(
    O2, 2, F,
    use="Aprenderé a investigar un caso de interés público sobre justicia: ubicar la institución adecuada, reunir pruebas y entender el recorrido de un reclamo.",
    prior=["Sé qué es acceder a la justicia.", "Sé que hay tribunales según el tipo de asunto.", "Sé qué es una fuente."],
    explain=[
        "Un conflicto puede seguir un recorrido: primero se intenta una vía simple, como un reclamo ante la institución encargada o una mediación, y si no basta se acude a un tribunal. Cada vía tiene una institución, y elegir la correcta ahorra tiempo. Por eso se investiga quién es competente, es decir, a quién le corresponde resolver ese asunto.",
        "Una prueba es cualquier elemento que ayuda a demostrar un hecho: un contrato, una liquidación, un mensaje, un testigo. Para reunirlas se ordena una línea de tiempo con fechas y se verifica cuál documento respalda cada afirmación. Una afirmación sin prueba sigue siendo una versión; la ley exige presentar pruebas ante un tribunal.",
        "Para investigar el caso se anota qué derecho está en juego, qué dice cada documento y qué falta. Se debe cuidar la privacidad de las personas y no sacar conclusiones sobre culpas antes de que un tribunal decida. El tribunal decide con la ley y las pruebas; las instituciones administrativas pueden ayudar a conciliar.",
    ],
    vocab=[("competente", "autoridad o tribunal a quien le corresponde resolver un asunto"), ("prueba", "elemento que ayuda a demostrar un hecho"), ("conciliación", "acuerdo entre las partes con ayuda de una institución"), ("línea de tiempo", "orden de hechos según su fecha"), ("versión", "relato de una persona sin respaldo todavía")],
    worked=[
        ("Ordenar fechas", "En un caso de ejemplo, un arriendo se firmó el 1 de marzo, se pagó hasta junio y se reclamó el 4 de agosto. ¿Qué dato falta para probar el pago?", ["Hay contrato y reclamo.", "Falta un comprobante del pago de julio."], "Comprobante de pago de julio"),
        ("Elegir institución", "Una consumidora de ejemplo reclama por un producto defectuoso. ¿A quién corresponde primero?", ["Hay instituciones para reclamos de consumo.", "Se intenta primero un reclamo ante ellas."], "Una institución de consumo"),
    ],
    mistakes=[("Acusar a alguien sin pruebas.", "Una versión no basta en un tribunal.", "Reúne documentos y escribe «según el documento…»."),
              ("Ir a cualquier institución sin averiguar si es competente.", "Se pierde tiempo.", "Averigua cuál resuelve ese tipo de asunto.")],
    T=[
        ('abc', '¿Qué distingue a una prueba de una simple versión?', 'La prueba es un elemento que respalda el hecho; la versión es solo un relato', 'La versión se presenta ante el tribunal y la prueba no, porque es solo un relato', 'La prueba siempre es un testigo que declara ante el tribunal laboral', 'Una afirmación sin respaldo sigue siendo versión; los documentos o testigos pueden ser pruebas.'),
        ('abc', '¿Qué significa que un tribunal sea competente?', 'Le corresponde resolver ese tipo de asunto', 'Sabe mucho de leyes', 'Es el que queda más cerca del domicilio', 'Competente se refiere a quién le corresponde resolver; no es cercanía ni conocimiento.'),
        ('abc', '{F} ¿Qué documento muestra la fecha formal del despido?', 'La carta de despido', 'La liquidación de abril', 'Los mensajes con su jefa', 'La carta es la que tiene fecha del 5 de junio.'),
        ('=', '{F} ¿Cuántos días pasaron desde el 20 de mayo hasta el 5 de junio? (Mayo tiene 31 días.)', '31-20+5', 'Se cuentan los días que quedan de mayo y se suman los de junio.', ' días'),
        ('abc', '{F} ¿Qué documento respalda mejor que dejó de trabajar el 20 de mayo?', 'Los mensajes con su jefa de esa fecha', 'La liquidación de abril', 'La carta de despido del 5 de junio', 'Los mensajes son de la fecha en discusión; los otros son de abril y de junio.'),
        ('abc', '{F} ¿Qué muestra la liquidación de abril?', 'El pago de abril, pero no dice nada del sueldo de mayo', 'Que el despido fue injusto', 'Que el sueldo de mayo se pagó incompleto', 'Corresponde a otro mes, por lo que no prueba nada sobre mayo.'),
        ('abc', '{F} ¿Qué prueba falta para demostrar lo ocurrido con el sueldo de mayo?', 'Un documento o registro que muestre si se pagó el sueldo de mayo', 'Otra copia de la liquidación de abril', 'Un comentario de un compañero sobre el carácter de la jefa', 'Se necesita respaldo del pago de ese mes.'),
        ('abc', '{F} ¿Qué vía menciona la ficha como primera instancia?', 'Reclamar ante la inspección del trabajo', 'Presentarse directamente ante la Corte Suprema', 'Pedir una mediación municipal vecinal', 'La ficha indica la inspección y después los tribunales laborales.'),
        ('abc', '{F} Los mensajes son del 20 de mayo y la carta del 5 de junio. ¿Qué podrían sugerir las fechas?', 'Que hubo un período entre su salida y el despido formal que habría que explicar', 'Que el despido ocurrió antes de que dejara de trabajar, por lo que carece de valor', 'Que la carta es falsa porque tiene otra fecha que los mensajes con su jefa', 'Las fechas distintas piden explicación, no demuestran falsedad.'),
        ('abc', '{F} ¿Qué conclusión NO se puede sacar todavía?', 'Que la jefa actuó de mala fe', 'Que hay una diferencia entre dos fechas', 'Que falta prueba del pago de mayo', 'No hay prueba de intenciones; las otras dos se desprenden de los documentos.'),
        ('abc', '{F} Si no hay acuerdo en la inspección del trabajo, ¿a qué tribunales corresponde acudir según la ficha?', 'A los tribunales laborales', 'A los tribunales de familia', 'A los tribunales penales', 'El asunto es laboral, por lo que lo resuelven tribunales laborales.'),
        ('abc', '{F} ¿Qué cuidado debe tener quien investiga el caso?', 'Proteger la privacidad y no decidir quién tiene la culpa', 'Publicar los datos de Sergio para conseguir apoyo', 'Concluir culpas si los documentos parecen claros', 'Decidir culpas corresponde al tribunal, y los datos personales se protegen.'),
        ('abc', '{F} ¿Cuál es el orden cronológico correcto de los hechos del caso?', 'Liquidación de abril, mensajes del 20 de mayo, carta del 5 de junio', 'Mensajes del 20 de mayo, liquidación de abril, carta del 5 de junio', 'Carta del 5 de junio, mensajes del 20 de mayo, liquidación de abril', 'Abril va antes que mayo y mayo antes que junio.'),
    ],
    ctx=('abc', 'Una familia tiene un conflicto por una herencia. ¿Qué paso inicial conviene?', 'Averiguar qué tribunal es competente y reunir los documentos del caso', 'Acudir al tribunal más cercano sin averiguar nada más', 'Esperar a que el conflicto se resuelva solo', 'Primero se identifica a quién le corresponde y se reúnen pruebas.'),
    sc=[
        ('En Educación Ciudadana: ¿Qué es una prueba?', 'Un elemento que ayuda a demostrar un hecho', 'Un contrato o una liquidación respaldan un hecho; la sospecha no.'),
        ('abc', '¿Cuál es un ejemplo de prueba?', 'Un contrato firmado', 'Una sospecha sobre la intención del jefe', 'Un rumor de pasillo', 'El contrato es un documento que respalda un hecho.'),
        ('En Educación Ciudadana: ¿Qué es una línea de tiempo?', 'Un orden de hechos según su fecha', 'Ayuda a ver la secuencia y a detectar qué falta.'),
    ],
    op=("Con la {F} construye una línea de tiempo de tres fechas y escribe una tabla con tres filas: documento, qué demuestra, qué no demuestra. Termina con la institución a la que acudirías primero y una pregunta que harías a un abogado o abogada.",
        "Línea: 20 de mayo, deja de trabajar; 5 de junio, carta de despido; abril, última liquidación. Tabla: carta, demuestra el despido formal, no demuestra el pago; mensajes, demuestran fecha de salida, no el sueldo; liquidación de abril, muestra el pago de abril, no el de mayo. Institución: la inspección del trabajo. Pregunta: ¿qué plazo tengo?",
        ["ordena fechas", "separa lo que demuestra cada documento", "formula una pregunta a un especialista"], ["línea de tiempo", "tabla de tres filas"], ["atribuir culpa", "olvidar lo que no demuestra un documento"],
        "Pregunta qué otra prueba buscaría."),
    reinforce="Explica con tus palabras la diferencia entre competente y no competente.",
    extend="Anota un conflicto cotidiano y dos pruebas que ayudarían a resolverlo.",
)

# ============================================================ OA 02, clase 3
F = ("Ficha 8 (perspectivas de ejemplo sobre un reclamo de vecinos contra una tienda por ruido nocturno). "
     "Perspectiva 1 (vecina): «Queremos mediación: es rápida y puede terminar en un acuerdo». "
     "Perspectiva 2 (abogado de los vecinos): «Prefiero el tribunal: una sentencia obliga al local». "
     "Perspectiva 3 (dueño de la tienda): «Cumplo la norma; que se pruebe con una medición». "
     "Dato de ejemplo: una mediación similar demoró 2 semanas y un juicio similar demoró 20.")
build(
    O2, 3, F,
    use="Aprenderé a comparar vías de justicia, sus ventajas y límites, usando evidencia y distintas perspectivas.",
    prior=["Sé qué es mediación y qué es un juicio.", "Sé comparar perspectivas.", "Sé calcular diferencias simples."],
    explain=[
        "Elegir una vía para resolver un conflicto implica comparar ventajas y límites. La mediación suele ser más rápida, barata y conserva la relación entre las partes, pero solo funciona si ambas quieren llegar a un acuerdo y el acuerdo no siempre se puede imponer. El juicio entrega una decisión obligatoria, pero es más lento, más formal y exige pruebas.",
        "Cada perspectiva responde a un interés: quien reclama quiere que el problema termine; quien es reclamado quiere defender su actividad; el abogado busca asegurar efectos legales. Entender intereses ayuda a ver qué vía los respeta mejor. Una comparación justa usa criterios: tiempo, costo, obligatoriedad, relación entre las partes y posibilidad de probar.",
        "También conviene distinguir entre lo que dice una fuente y lo que cada actor quisiera. Un dato como «dos semanas frente a veinte» es un ejemplo y no una regla general. Antes de decidir se pregunta qué evidencia falta, por ejemplo una medición de ruido. Los derechos de ambas partes deben respetarse: el descanso de los vecinos y el trabajo del local.",
    ],
    vocab=[("sentencia", "decisión final de un tribunal que obliga a las partes"), ("criterio", "aspecto con el que se compara, como tiempo o costo"), ("interés", "lo que una persona quiere lograr o proteger"), ("obligatoriedad", "carácter de lo que debe cumplirse"), ("medición", "registro de un dato con un instrumento")],
    worked=[
        ("Comparar con criterios", "Dos vías de ejemplo: la A demora 1 semana y no obliga; la B demora 10 y obliga. ¿Qué criterio favorece a cada una?", ["A gana en tiempo.", "B gana en obligatoriedad."], "A, tiempo; B, obligatoriedad"),
        ("Identificar un interés", "Un panadero de ejemplo dice: «Sólo quiero poder trabajar sin multas injustas». ¿Qué interés expresa?", ["Quiere continuar su actividad.", "Y evitar sanciones sin respaldo."], "Defender su actividad y evitar multas injustas"),
    ],
    mistakes=[("Elegir la vía por rapidez sin mirar si obliga a cumplir.", "Un acuerdo sin cumplimiento deja el conflicto abierto.", "Compara más de un criterio."),
              ("Pensar que una vía es buena para todos los conflictos.", "Cada caso tiene sus condiciones.", "Revisa la naturaleza del conflicto y las ganas de acuerdo.")],
    T=[
        ('abc', '¿Qué ventaja tiene la mediación frente al juicio, según la clase?', 'Suele ser más rápida y barata y conserva la relación entre las partes', 'Entrega una decisión que obliga aunque una parte no quiera', 'Permite apelar a un tribunal superior', 'La obligatoriedad es ventaja del juicio; la mediación destaca por rapidez, costo y relación entre las partes.'),
        ('=', '{F} ¿Cuántas veces más tiempo demoró el juicio que la mediación en el dato de ejemplo?', '20//2', 'Se divide el tiempo del juicio entre el de la mediación.', ' veces'),
        ('abc', '{F} ¿Qué evidencia pide el dueño para aceptar el reclamo?', 'Una medición que pruebe el nivel de ruido', 'Una declaración firmada por los vecinos', 'Un informe de la municipalidad sobre su patente', 'Él afirma que cumple la norma y pide que se pruebe con una medición.'),
        ('abc', '{F} ¿Qué criterio favorece a la mediación según el dato de ejemplo?', 'Tiempo: fue más rápida', 'Obligatoriedad: el acuerdo siempre se impone', 'Formalidad: exige pruebas ordenadas', 'El dato compara 2 semanas con 20; la obligatoriedad y la formalidad favorecen al juicio.'),
        ('abc', '{F} ¿Qué criterio favorece al tribunal según el abogado?', 'Obligatoriedad', 'Rapidez', 'Conservar la relación', 'Una sentencia obliga al local; en cambio rapidez y relación son fortalezas de la mediación.'),
        ('abc', '{F} ¿Qué interés expresa el dueño?', 'Defender su actividad comercial sin aceptar cambios sin pruebas', 'Cerrar el local para evitar reclamos de los vecinos y ahorrar costos', 'Que los vecinos se vayan del barrio para poder seguir funcionando de noche', 'Dice que cumple la norma y pide una medición.'),
        ('abc', '{F} ¿Qué dato falta para decidir con evidencia?', 'Una medición del nivel de ruido en horario nocturno', 'El nombre del abogado de los vecinos y los años que lleva ejerciendo', 'El año en que se abrió la tienda y quién fue su primer dueño', 'Es el hecho que ambas partes discuten.'),
        ('abc', '{F} ¿Qué límite tiene la mediación?', 'Solo funciona si ambas partes quieren llegar a un acuerdo', 'Siempre es más lenta que un juicio, porque exige muchas audiencias', 'Exige que un juez la apruebe antes de que las partes puedan reunirse', 'Si una parte no quiere acordar, no hay mediación.'),
        ('abc', '{F} ¿Qué límite tiene el juicio?', 'Es más lento y formal, y exige pruebas', 'No permite obtener una decisión obligatoria', 'No sirve cuando existe una norma', 'El juicio es obligatorio pero lento; la norma es justamente lo que se aplica.'),
        ('abc', '{F} Un asistente dice: «El dato prueba que la mediación siempre demora 2 semanas». ¿Qué error comete?', 'Generaliza un dato de ejemplo como si fuera una regla', 'Cita una fuente que no existe para respaldar lo que afirma', 'Confunde una mediación con una sentencia que obliga a las partes', 'Un caso similar no permite asegurar lo que pasará siempre.'),
        ('abc', '{F} ¿Qué punto de acuerdo hay entre las tres perspectivas?', 'Que el problema se resuelva respetando el descanso de los vecinos y el trabajo del local', 'Que la tienda debe cerrar de noche para que los vecinos puedan descansar', 'Que el juicio es la única vía válida para resolver conflictos entre vecinos', 'Todos quieren una solución que no vulnere derechos de ninguna parte.'),
        ('=', '{F} Supón (dato de ejemplo) que de 50 mediaciones similares, 35 terminaron en acuerdo. ¿Qué porcentaje terminó en acuerdo?', '35*100//50', 'Se compara la parte que terminó en acuerdo con el total.', ' %'),
        ('abc', '{F} ¿Qué combinación de vías puede satisfacer a más actores?', 'Mediar primero y, si no hay acuerdo, ir a tribunal con la medición', 'Ir directo a tribunal sin intentar un acuerdo', 'Mediar y obligar al local a aceptar lo acordado sin pruebas', 'Combina rapidez con un respaldo obligatorio y la prueba que pide el dueño.'),
    ],
    ctx=('abc', 'Dos hermanos discuten por el uso de una pieza de la casa y no quieren perder su relación. ¿Qué vía conviene?', 'Mediación, porque busca un acuerdo y conserva la relación', 'Juicio inmediato, porque una sentencia termina el conflicto', 'No hacer nada para no perder la relación', 'La mediación cuida el vínculo y busca un acuerdo.'),
    sc=[
        ('¿Qué es una sentencia?', 'Una decisión final de un tribunal que obliga a las partes', 'Obliga a las partes, a diferencia de un acuerdo que depende de su voluntad.'),
        ('abc', '¿Qué criterios sirven para comparar vías de solución?', 'Tiempo, costo, obligatoriedad y relación entre las partes', 'Cantidad de testigos, simpatía por una parte y hora del trámite', 'Solo la rapidez, porque los demás criterios no se pueden comparar', 'Los criterios se refieren a cómo funciona cada vía, no a preferencias.'),
        ('En Educación Ciudadana: ¿Qué es un interés?', 'Lo que una persona quiere lograr o proteger', 'Ayuda a entender qué postura toma cada actor y por qué.'),
    ],
    op=("Con la {F} arma una tabla que compare mediación y tribunal con cuatro criterios (tiempo, costo, obligatoriedad, relación entre las partes) y escribe qué recomendarías y qué evidencia falta. Mantén un tono respetuoso con las tres perspectivas.",
        "Mediación: rápida, barata, conserva la relación, no siempre obliga. Tribunal: lento, más caro, obliga, puede tensar la relación. Recomendación: mediar primero, con una medición de ruido como base. Evidencia que falta: la medición y si el local cumple la norma.",
        ["compara con criterios", "reconoce los intereses de los tres actores", "señala evidencia faltante"], ["tabla de cuatro criterios", "recomendación"], ["comparar con un solo criterio", "desconocer al dueño"],
        "Pregunta cómo cambiaría su recomendación si la medición muestra ruido sobre la norma."),
    reinforce="Elige un conflicto de tu entorno y compara dos vías posibles con dos criterios.",
    extend="Anota un caso donde un acuerdo sin obligatoriedad podría no cumplirse.",
)

# ============================================================ OA 02, clase 4
F = ("Ficha 9 (tema de deliberación de ejemplo): una comuna ficticia debate si todos los reclamos de consumo pequeños (de poco monto) deben pasar por una mediación obligatoria antes de llegar al tribunal. "
     "Razón a favor: descongestiona los tribunales. Razón en contra: puede retrasar a quien necesita una decisión inmediata. "
     "Dato de ejemplo: de 100 reclamos pequeños, 60 se resolvieron en mediación y 40 llegaron a tribunal.")
build(
    O2, 4, F,
    use="Aprenderé a deliberar sobre un diseño del sistema de justicia, con razones, evidencia y propuestas que resguarden los derechos.",
    prior=["Sé qué es una tesis, una razón y una objeción.", "Sé comparar vías de justicia.", "Sé interpretar un dato simple."],
    explain=[
        "Deliberar sobre justicia exige pensar en todas las personas que usan el sistema. Una medida puede tener buenos efectos para la mayoría y perjudicar a un grupo, por ejemplo a quien necesita una decisión urgente. Por eso se examinan efectos esperados, efectos no deseados y condiciones que podrían corregirlos.",
        "Un argumento sólido incluye tres partes: la afirmación, la razón y la evidencia, y además la respuesta a una objeción. Si alguien propone la mediación obligatoria, debe explicar cómo protegerá a quien tiene urgencia. Quien se opone debe decir qué alternativa propone para descongestionar tribunales.",
        "Un dato como «60 de 100» muestra una proporción; no dice por qué esos casos se resolvieron. Hay que evitar sobreinterpretar. Una deliberación seria termina con una propuesta que combina razones: por ejemplo, mediación previa salvo casos urgentes. Así se resguardan las libertades y los derechos de la comunidad.",
    ],
    vocab=[("efecto no deseado", "consecuencia no buscada de una medida"), ("proporción", "parte de un total, como 60 de 100"), ("urgencia", "necesidad de una solución inmediata"), ("propuesta combinada", "solución que une razones de varias posturas"), ("sobreinterpretar", "sacar de un dato más de lo que realmente muestra")],
    worked=[
        ("Efecto no deseado", "Una comuna de ejemplo hace obligatoria una etapa de conversación antes de cualquier reclamo. ¿Qué efecto no deseado podría aparecer?", ["Alguien con urgencia debe esperar.", "Se necesita una excepción para casos urgentes."], "Retraso en casos urgentes"),
        ("Leer una proporción", "De 50 reclamos de ejemplo, 30 se resolvieron por acuerdo. ¿Qué proporción es?", ["30 de 50 es más de la mitad.", "No dice por qué se resolvieron."], "30 de 50, sin explicar la causa"),
    ],
    mistakes=[("Defender una medida sin explicar sus efectos en quienes tienen urgencia.", "Se piensa solo en la mayoría.", "Pregunta quién podría perjudicarse y cómo se compensa."),
              ("Decir que un dato prueba la causa de un resultado.", "Una proporción no explica el porqué.", "Escribe «el dato muestra que… pero no explica por qué».")],
    T=[
        ('abc', '¿Qué es un efecto no deseado?', 'Una consecuencia no buscada de una medida, que puede perjudicar a alguien', 'Un objetivo de la medida que no se cumplió, porque nadie la aplicó bien', 'Una objeción sin evidencia que presenta un participante del debate', 'Es una consecuencia no buscada, como el retraso para quien tiene urgencia.'),
        ('abc', '{F} ¿Qué persigue la mediación previa obligatoria según la razón a favor?', 'Descongestionar los tribunales', 'Impedir que las personas reclamen', 'Acelerar las decisiones urgentes', 'La razón a favor dice que descongestiona; acelerar urgencias es la preocupación de la razón en contra.'),
        ('abc', '¿Qué debe incluir un argumento sólido, además de afirmación, razón y evidencia?', 'La respuesta a una objeción', 'Una advertencia de que la medida no funcionará', 'La opinión de la mayoría', 'Un argumento sólido reconoce y responde objeciones.'),
        ('abc', '{F} ¿Qué medida corrige el efecto no deseado de la mediación obligatoria?', 'Una excepción para los casos urgentes', 'Eliminar el tribunal para reclamos pequeños', 'Hacer obligatoria la mediación incluso en casos urgentes', 'La excepción protege a quien necesita una decisión inmediata sin eliminar la mediación.'),
        ('abc', '{F} Un asistente dice: «El dato prueba que la mediación funciona en todos los casos». ¿Qué corresponde?', 'Señalar que el dato muestra solo 60 de 100 y no permite generalizar', 'Aceptarlo, porque más de la mitad se resolvió', 'Pedir que se ignoren los 40 casos que llegaron a tribunal', '60 de 100 no es el total, y ocultar los 40 sesga la lectura.'),
        ('abc', '{F} ¿Qué dato adicional ayudaría a decidir?', 'Cuántos de los reclamos que llegaron a tribunal eran urgentes', 'Cuántos abogados trabajan en la comuna y cuántos atienden reclamos pequeños', 'El nombre de cada persona que reclamó y la comuna en que vive', 'Muestra si la excepción es necesaria; los nombres, además, afectan la privacidad.'),
        ('abc', '{F} ¿Qué propuesta combina ambas razones?', 'Mediación previa, salvo en casos urgentes', 'Mediación obligatoria siempre, sin excepciones', 'Ir siempre al tribunal, sin mediación', 'Une descongestión con protección ante la urgencia.'),
        ('abc', '{F} Un participante grita que «los jueces son flojos». ¿Qué error comete?', 'Ataca a las personas en lugar de responder al argumento', 'Usa un dato sin citar la fuente de donde proviene la cifra', 'Propone una excepción sin evidencia que la respalde para casos urgentes', 'No discute la medida, sino a quienes trabajan en los tribunales.'),
        ('=', '{F} Si la misma proporción se aplicara a 250 reclamos, ¿cuántos se resolverían en mediación (estimación de ejemplo)?', '250*60//100', 'Se aplica 60 de cada 100 al nuevo total.', ' reclamos'),
        ('abc', '{F} ¿Qué condición haría más justa la medida?', 'Que la mediación sea gratuita y cercana a los hogares', 'Que la mediación tenga un costo que cubra el servicio', 'Que se realice solo en la capital regional', 'Un costo o una distancia mayor serían nuevas barreras.'),
        ('abc', '{F} ¿Qué haría fuerte a un argumento final?', 'Incluir evidencia y responder a la objeción de la postura contraria', 'Repetir la tesis con más fuerza y sin responder ninguna objeción', 'Citar a quienes ya están de acuerdo con la postura que se defiende', 'La fuerza viene de la evidencia y de hacerse cargo de las objeciones.'),
        ('abc', '{F} ¿Cuál afirmación sobre el dato 60 de 100 es válida?', 'Cerca de seis de cada diez reclamos de este ejemplo se resolvieron en mediación', 'La mediación resuelve seis de cada diez reclamos en cualquier comuna del país', 'Los cuarenta reclamos que llegaron a tribunal eran todos casos urgentes', 'El dato describe un ejemplo; no permite generalizar ni explicar por qué llegaron a tribunal.'),
        ('abc', '{F} ¿Cuál es una objeción a la mediación previa obligatoria?', 'Puede retrasar a quien necesita una decisión inmediata', 'Descongestiona los tribunales y reduce el número de juicios pendientes', 'Resuelve 60 de cada 100 reclamos pequeños que se presentan', 'Una objeción cuestiona la postura; las otras opciones son a favor.'),
    ],
    ctx=('abc', 'Un grupo propone mediación obligatoria para todos los conflictos vecinales, incluso si hay violencia. ¿Qué advertencia es razonable?', 'Debe haber excepciones cuando existe riesgo para una persona', 'La mediación es siempre la mejor vía, incluso con violencia', 'Basta con que el mediador pida a las partes que se respeten', 'Cuando hay riesgo para una persona se necesitan otras vías de protección.'),
    sc=[
        ('abc', '¿Qué es una propuesta combinada?', 'Una que une razones de posturas distintas, como mediar salvo urgencias', 'La que apoya la mayor parte del grupo', 'La que repite la tesis de la persona que habló primero', 'Combina razones de ambos lados en vez de elegir uno.'),
        ('abc', '¿Qué es una proporción?', 'Una relación entre una parte y el total, como 60 de 100', 'El total de casos de una comuna', 'Una opinión sobre cuántos casos son urgentes', 'Compara una parte con el todo.'),
        ('abc', '¿Qué es sobreinterpretar un dato?', 'Sacar de él más de lo que muestra', 'Citar la fuente del dato', 'Comparar el dato con otro', 'Sobreinterpretar sería concluir causas que el dato no muestra.'),
    ],
    op=("Con la {F} escribe un texto de seis líneas con tu postura: afirmación, una razón con el dato, una objeción posible, tu respuesta y una propuesta final. Cuida los derechos de quienes tienen urgencia.",
        "Afirmo que conviene mediación previa con excepciones. Razón: 60 de 100 reclamos se resolvieron así. Objeción: retrasa casos urgentes. Respuesta: se exceptúan urgencias. Propuesta: mediación gratuita, cercana y con excepciones por urgencia.",
        ["usa el dato sin sobreinterpretarlo", "responde la objeción", "protege derechos"], ["texto de seis líneas"], ["afirmar que el dato prueba la causa", "ignorar la urgencia"],
        "Pregunta qué cambiaría su postura."),
    reinforce="Explica por qué una medida buena para la mayoría puede perjudicar a un grupo.",
    extend="Busca un reglamento de tu liceo y anota un posible efecto no deseado.",
)

# ============================================================ OA 02, clase 5
F = ("Ficha 10 (diagnóstico de ejemplo en el barrio ficticio El Mirador): se encuestó a 50 vecinos; 35 no saben dónde pedir ayuda jurídica gratuita, 10 lo saben y 5 no responden. "
     "Recursos: un panel informativo en la sede vecinal, 12 jóvenes voluntarios, 2 semanas. Un profesional abogado o abogada de la asistencia gratuita puede revisar la información antes de publicarla.")
build(
    O2, 5, F,
    use="Aprenderé a diseñar una acción comunitaria para que más personas conozcan y usen mecanismos de acceso a la justicia, resguardando sus derechos y los de su comunidad.",
    prior=["Sé qué son las barreras de acceso a la justicia.", "Sé diseñar una acción con objetivo e indicador.", "Sé leer una encuesta."],
    explain=[
        "Una forma de fortalecer el acceso a la justicia es informar a la comunidad. Una guía comunitaria indica dónde pedir ayuda, qué documentos reunir y a quién acudir en cada tipo de problema. Debe estar en lenguaje claro y ser revisada por una persona experta, porque la información jurídica inexacta puede perjudicar.",
        "El diseño parte de un diagnóstico: cuántas personas no saben dónde acudir. Se fija un objetivo medible, se asignan roles, se eligen medios (panel, conversación, volantes) y se define un indicador, como cuántas personas responden bien una pregunta de control. También se piensa en quienes podrían quedar fuera: personas mayores, quienes no leen bien o no pueden asistir.",
        "La acción no reemplaza a un abogado: orienta y deriva. Se evita dar consejos legales concretos sobre casos individuales. Se cuida la privacidad: no se anotan nombres ni casos reales en el panel. Al final se evalúa con el indicador y se corrige lo que no funcionó.",
    ],
    vocab=[("guía comunitaria", "material que orienta sobre dónde y cómo pedir ayuda"), ("derivar", "indicar a una persona a qué institución acudir"), ("lenguaje claro", "forma de escribir sencilla y directa"), ("revisión experta", "control de la información por alguien que domina el tema"), ("inclusión", "tomar medidas para que nadie quede fuera")],
    worked=[
        ("Medir el alcance", "En un barrio de ejemplo, 20 de 40 vecinos no sabían dónde acudir; tras la guía, 10 siguen sin saberlo. ¿Cuántos mejoraron?", ["Antes, 20 no sabían.", "Después, 10; mejoraron 20 menos 10."], "10 vecinos mejoraron"),
        ("Pensar en quien queda fuera", "Una guía de ejemplo se publica solo en internet. ¿A quién podría dejar fuera?", ["A quien no tiene internet.", "Se agrega un panel físico."], "A quien no tiene internet"),
    ],
    mistakes=[("Dar consejos sobre casos individuales en la guía.", "Eso exige un profesional que conozca los hechos.", "Orienta y deriva, no resuelve casos."),
              ("Publicar nombres o casos reales para dar ejemplos.", "Se vulnera la privacidad.", "Usa ejemplos ficticios.")],
    T=[
        ('abc', '¿Qué es una guía comunitaria?', 'Un texto en lenguaje claro que indica dónde pedir ayuda y qué documentos reunir', 'Un documento que reemplaza la asesoría de un abogado en el caso de cada persona', 'Un reclamo formal presentado ante un tribunal por un grupo de vecinos', 'Orienta y deriva; no reemplaza a un abogado ni es un reclamo.'),
        ('=', '{F} ¿Qué porcentaje de los 50 vecinos encuestados no sabe dónde pedir ayuda jurídica?', '35*100//50', 'Se compara la cantidad que no sabe con el total encuestado.', ' %'),
        ('abc', '{F} ¿Qué objetivo medible es adecuado?', 'Que al menos 30 de los 50 vecinos sepan dónde pedir ayuda al cabo de 2 semanas', 'Que todo el barrio entienda mejor la ley y se sienta más seguro', 'Que los 12 voluntarios repartan muchos volantes en las calles del barrio', 'Un número y un plazo permiten comprobarlo.'),
        ('abc', '{F} ¿Qué medio permite llegar a quien no usa internet?', 'El panel impreso en la sede vecinal, junto con conversaciones', 'Una publicación en redes sociales del barrio que lean los vecinos conectados', 'Un correo a la lista de vecinos que tengan dirección electrónica', 'Solo el panel físico no depende de conexión.'),
        ('abc', '{F} ¿Por qué debe revisar la guía una persona experta?', 'Para evitar información jurídica inexacta que perjudique a quien la use', 'Para que la guía parezca más oficial y los vecinos confíen en ella', 'Para que incluya consejos sobre cada caso individual de los vecinos', 'Un error jurídico podría dañar a quien confíe en la guía.'),
        ('=', '{F} Para llegar a 30 vecinos que sepan dónde ir, ¿cuántos más que los 10 que hoy lo saben deben aprenderlo?', '30-10', 'Se resta los actuales a la meta.', ' vecinos'),
        ('abc', '{F} ¿Qué indicador sirve para medir el alcance?', 'Número de vecinos que responden bien una pregunta de control', 'Cantidad de volantes entregados durante las dos semanas de campaña', 'Cantidad de voluntarios inscritos en el equipo de difusión', 'Mide el resultado, no la actividad.'),
        ('abc', '{F} ¿Qué debe evitar la guía?', 'Dar consejos legales sobre el caso de una persona', 'Indicar a qué institución acudir en cada tipo de problema', 'Explicar con lenguaje sencillo qué documentos reunir', 'Orientar y derivar es lo que corresponde; aconsejar sobre casos individuales es tarea de especialistas.'),
        ('abc', '{F} ¿Cómo se cuida la privacidad de las personas?', 'Usando ejemplos sin nombres ni casos reales', 'Anotando solo el primer nombre de cada afectado', 'Pidiendo permiso verbal y pegando el caso completo', 'Un primer nombre o un caso completo siguen exponiendo a la persona.'),
        ('abc', '{F} ¿Qué medida incluye a una persona mayor que no lee bien?', 'Explicarle de forma oral con apoyo de un voluntario', 'Entregarle el panel en letra pequeña para que lo lea con calma', 'Pedirle que lea la guía en su casa con ayuda de un familiar', 'La conversación elimina la barrera de la lectura.'),
        ('=', '{F} Si cada voluntario conversa con 5 de los 35 vecinos que no saben dónde pedir ayuda, ¿cuántos voluntarios se necesitan para alcanzar a los 35?', '35//5', 'Se reparte el total de vecinos entre los que alcanza cada voluntario.', ' voluntarios'),
        ('abc', '{F} Si al final solo 18 de 50 saben dónde ir y la meta era 30, ¿qué corresponde?', 'Revisar qué falló (alcance, medio, lenguaje) y ajustar la guía', 'Declarar cumplida la meta porque mejoró respecto de los 10 iniciales', 'Cerrar la acción para no repetir el error en el futuro', '18 es mayor que 10 pero menor que 30: hay que corregir.'),
        ('abc', '{F} ¿Por qué conviene un panel y también conversaciones?', 'Porque llegan a personas distintas: quienes pasan por la sede y quienes prefieren hablar', 'Porque así se reparte el costo entre los voluntarios y se gasta menos dinero', 'Porque la ley exige que toda guía comunitaria use ambos medios a la vez', 'Varios canales incluyen a más personas.'),
    ],
    ctx=('abc', 'Un grupo quiere ayudar a un vecino con un problema legal propio. ¿Qué es lo más adecuado?', 'Orientarlo hacia un servicio de asistencia jurídica', 'Darle un consejo legal detallado', 'Pedirle que publique su caso en el panel', 'Orientar y derivar es lo prudente.'),
    sc=[
        ('abc', '¿Qué es derivar?', 'Indicar a qué servicio o persona acudir', 'Resolver el caso por cuenta propia con ayuda de voluntarios', 'Archivar el caso en una carpeta del panel', 'Derivar no es resolver, sino orientar hacia quien corresponde.'),
        ('abc', '¿Qué es lenguaje claro?', 'Escribir de forma sencilla y directa, sin términos innecesarios', 'Usar términos jurídicos para dar seriedad a la guía ante los vecinos', 'Escribir lo mismo en textos más largos para explicar con detalle', 'El lenguaje claro permite que más personas entiendan la guía y puedan usarla.'),
        ('abc', '¿Cuál es una medida de inclusión en esta acción?', 'Explicar la información de forma oral a quien no lee bien', 'Publicarla solo en un panel alto que se vea desde lejos', 'Dar la información solo a quienes la pidan en la sede vecinal', 'Incluir es pensar en quién podría quedar fuera.'),
    ],
    op=("Con la {F} diseña una guía comunitaria: objetivo medible, tres pasos con semana, un reparto de roles para los voluntarios, un medio para incluir a quienes no leen bien, un indicador y la revisión experta.",
        "Objetivo: 30 de 50 sepan dónde acudir. Pasos: semana 1, redactar y revisar con un profesional; semana 2, panel y conversaciones. Roles: 4 en redacción, 4 en panel, 4 en conversaciones. Inclusión: conversaciones orales. Indicador: pregunta de control. Revisión: abogada o abogado de la asistencia gratuita.",
        ["objetivo medible", "inclusión", "revisión experta"], ["diseño de guía"], ["dar consejos legales", "olvidar la privacidad"],
        "Pregunta qué hará si alguien pide consejo sobre su caso."),
    reinforce="Escribe una guía de tres líneas sobre dónde pedir ayuda jurídica con tus propias palabras.",
    extend="Averigua qué servicios gratuitos hay en tu comuna.",
)

# ============================================================ OA 02, clase 6
F = ("Ficha 11 (evaluación de ejemplo): el programa ficticio «Justicia Cerca» instaló 3 oficinas de orientación gratuita. En un año atendió 600 personas; "
     "de ellas, 420 lograron un acuerdo o iniciaron un trámite y 180 no continuaron. Motivos de no continuar (de ejemplo): 90 por falta de tiempo, 60 por falta de documentos y 30 por desconfianza. Costo anual de ejemplo: 30 millones de pesos.")
build(
    O2, 6, F,
    use="Aprenderé a evaluar los efectos y límites de una medida de acceso a la justicia con criterios claros, sin exagerar lo logrado.",
    prior=["Sé qué barreras hay para acceder a la justicia.", "Sé leer proporciones.", "Sé diseñar un indicador."],
    explain=[
        "Evaluar es juzgar con criterios y evidencia si algo logró su objetivo, a qué costo y con qué límites. Los criterios habituales son cobertura (a cuántos llegó), efectividad (si ayudó a resolver), equidad (si llegó a quienes más lo necesitaban), costo y sostenibilidad (si puede mantenerse). Una evaluación seria dice qué logró y qué no.",
        "Los límites aparecen al ver quién queda fuera y por qué. En el caso de ejemplo, quienes no continuaron mencionan falta de tiempo, falta de documentos y desconfianza. Cada motivo sugiere una mejora distinta: horarios flexibles, ayuda para reunir documentos y actividades para generar confianza. Un límite no es un fracaso: es una pista para mejorar.",
        "También hay que cuidar la interpretación. Una cifra de atendidos no prueba que se hizo justicia; solo muestra alcance. Para afirmar efectos se necesitan datos de resultados y, si es posible, comparación con una situación sin el programa. Se comunica con honestidad: logros, límites y qué se hará.",
    ],
    vocab=[("cobertura", "cantidad de personas a las que llega una medida"), ("efectividad", "grado en que una medida logra su objetivo"), ("equidad", "trato justo que considera las necesidades distintas"), ("sostenibilidad", "posibilidad de mantener algo en el tiempo"), ("límite", "aspecto que restringe lo que una medida logra")],
    worked=[
        ("Calcular una proporción", "Un programa de ejemplo atendió 200 personas y 50 no continuaron. ¿Qué parte no continuó?", ["50 de 200 es la cuarta parte.", "Es una proporción de abandono."], "Una cuarta parte"),
        ("Distinguir alcance y resultado", "Un informe de ejemplo dice: «Atendimos 500 personas». ¿Prueba que se resolvieron sus problemas?", ["Muestra alcance.", "No muestra resultados."], "No; solo muestra alcance"),
    ],
    mistakes=[("Medir el éxito solo por cuántas personas fueron atendidas.", "Atender no es lo mismo que resolver.", "Agrega indicadores de resultados."),
              ("Ocultar los límites para que el programa se vea mejor.", "Se pierde la oportunidad de mejorar.", "Comunica logros y límites.")],
    T=[
        ('abc', '¿Qué mide la efectividad de un programa?', 'Si ayudó a resolver los problemas de las personas', 'A cuántas personas llegó el programa durante el año', 'Si puede mantenerse en el tiempo con los recursos de la comuna', 'Efectividad es resolver; cobertura es llegar y sostenibilidad es mantenerse.'),
        ('=', '{F} ¿Qué porcentaje de las 600 personas logró un acuerdo o inició un trámite?', '420*100//600', 'Se compara la parte que logró avanzar con el total.', ' %'),
        ('=', '{F} De las personas que no continuaron, ¿qué porcentaje lo hizo por falta de tiempo?', '90*100//180', 'Se compara el grupo que mencionó el tiempo con el total que no continuó.', ' %'),
        ('abc', '{F} Se atendió a 600 personas en 3 oficinas. ¿Qué criterio describe esta cifra?', 'Cobertura, porque dice a cuántas personas llegó', 'Efectividad, porque dice cuántos problemas se resolvieron', 'Sostenibilidad, porque dice cuánto durará', 'La cantidad de atendidos muestra alcance, no resultados.'),
        ('abc', '{F} ¿Cuál es el motivo más frecuente de no continuar?', 'Falta de tiempo, con 90 de las 180 personas', 'Falta de documentos, con la mitad de quienes no continuaron', 'Desconfianza, con casi la mitad de quienes no continuaron', '90 es el mayor de los tres valores (90, 60 y 30).'),
        ('abc', '{F} ¿Qué mejora responde a la falta de tiempo?', 'Horarios flexibles o atención fuera del horario de oficina', 'Cerrar oficinas para concentrar la atención', 'Pedir más documentos desde la primera visita', 'Responde directamente a la barrera mencionada.'),
        ('abc', '{F} ¿Qué mejora responde a la falta de documentos?', 'Un servicio que ayude a reunir y ordenar los documentos', 'Aceptar solo casos que lleguen con todo listo', 'Recomendar que busquen un abogado privado', 'Ayudar a reunirlos reduce la barrera sin excluir a nadie.'),
        ('abc', '{F} ¿Qué mejora responde a la desconfianza?', 'Actividades que expliquen el servicio y muestren sus resultados', 'Reducir la información que se entrega sobre el servicio y sus resultados', 'Atender solo a quienes ya confían en el programa y lo recomiendan', 'La confianza se construye con información y transparencia.'),
        ('abc', '{F} Un funcionario dice: «Atendimos 600 personas, así que hicimos justicia a todas». ¿Qué error comete?', 'Confunde alcance con resultados: atender no prueba que se resolvió', 'Usa un porcentaje mal calculado al comparar con los datos del año', 'Compara con un barrio que no corresponde al de la evaluación', '180 personas no continuaron, así que no todas obtuvieron un resultado.'),
        ('abc', '{F} ¿Qué criterio falta para saber si el programa llegó a quienes más lo necesitaban?', 'Equidad', 'Costo', 'Sostenibilidad', 'Equidad pregunta quién quedó fuera y quién más lo necesita.'),
        ('=', '{F} Con un costo de 30 millones de pesos y 600 personas atendidas, ¿cuánto costó cada persona atendida?', '30000000//600', 'Se divide el costo total entre las personas atendidas.', ' pesos'),
        ('abc', '{F} Para saber si el programa causó una mejora, ¿qué dato ayudaría?', 'Comparar con un barrio parecido sin el programa', 'Contar cuántos afiches se repartieron', 'Preguntar solo a quienes quedaron conformes', 'La comparación permite atribuir efectos; las otras opciones miden actividad o sesgan.'),
        ('abc', '{F} ¿Qué es un límite del programa?', 'Una condición que restringe lo que logra y orienta mejoras', 'Un fracaso que obliga a cerrarlo, porque el programa no cumplió', 'Un error en el cálculo de los costos que debe corregirse', 'No es un fracaso, sino una pista para mejorar.'),
    ],
    ctx=('abc', 'Una comuna quiere saber si podrá financiar el programa durante diez años. ¿Qué criterio revisa?', 'Sostenibilidad, porque pregunta si puede mantenerse', 'Cobertura, porque dice a cuántas personas llega', 'Equidad, porque dice quién queda fuera', 'Pregunta si el programa puede mantenerse en el tiempo.'),
    sc=[
        ('¿Qué es la cobertura?', 'La cantidad de personas a las que llega una medida', 'Mide alcance, no si se resolvieron los problemas.'),
        ('¿Qué es la equidad?', 'Un trato justo que considera necesidades distintas', 'Mira quién queda fuera y a quién se debe dar más apoyo.'),
        ('abc', '¿Por qué una evaluación debe decir también lo que no se logró?', 'Para mejorar el programa y comunicar con honestidad', 'Para decidir quién tuvo la culpa de lo que salió mal', 'Para impedir que el programa continúe si hubo fallas', 'Los límites son pistas para mejorar.'),
    ],
    op=("Con la {F} redacta una evaluación breve: dos logros con datos, dos límites con datos, una mejora para cada límite y una frase honesta para informar a la comunidad.",
        "Logros: atendió a 600 personas; 420 lograron acuerdo o trámite. Límites: 90 por falta de tiempo; 30 por desconfianza. Mejoras: horarios flexibles; actividades de confianza. Mensaje: logramos orientar a 420 de 600; seguiremos mejorando horarios y confianza.",
        ["usa datos", "no exagera", "propone mejoras"], ["evaluación breve"], ["confundir alcance con justicia", "ocultar límites"],
        "Pregunta qué dato adicional pediría."),
    reinforce="Explica por qué atender personas no equivale a resolver sus problemas.",
    extend="Elige un servicio público que conozcas y anota un logro y un límite posibles.",
)
