"""Cuaderno del estudiante, 8.º básico Historia, Geografía y Ciencias Sociales: OA 15 (ideas ilustradas y revoluciones atlánticas)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI08 OA 15"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a situar en el tiempo y el espacio tres procesos revolucionarios: la independencia de Estados Unidos, la Revolución Francesa y las independencias hispanoamericanas, y a plantear cómo las ideas ilustradas se manifestaron en ellos.",
    ["Conozco las ideas de la Ilustración: razón, libertad, igualdad y soberanía popular.", "Sé leer una línea de tiempo y ubicar siglos."],
    [
        "Entre fines del siglo XVIII y comienzos del XIX ocurrieron varios procesos revolucionarios a ambos lados del Atlántico. En 1776, las Trece Colonias británicas de América del Norte declararon su independencia y formaron Estados Unidos. En 1789 comenzó la Revolución Francesa, que terminó con la monarquía absoluta. Desde 1808 la crisis de la monarquía española abrió el camino a las independencias de las colonias hispanoamericanas, que se extendieron hasta mediados de la década de 1820.",
        "Estos procesos tienen en común que sus protagonistas usaron ideas ilustradas: soberanía popular, constitución, separación de poderes, libertad e igualdad. Pero cada uno tuvo causas, actores y resultados propios. Por eso se habla de revoluciones atlánticas: ocurrieron en un mismo espacio y se influyeron mutuamente, a través de libros, cartas y viajeros.",
        "El problema de esta unidad es: ¿cómo se manifestaron las ideas ilustradas en estas revoluciones y qué límites tuvieron? Para responder hay que situar las fechas, los lugares y los actores, y recordar que algunas ideas, como la igualdad, no se aplicaron a todas las personas.",
    ],
    [("revolución", "cambio profundo y rápido del orden político o social"), ("Trece Colonias", "colonias británicas en la costa este de América del Norte que formaron Estados Unidos"), ("independencia", "proceso por el cual un territorio deja de depender de otro país y gobierna por sí mismo"), ("soberanía popular", "idea de que el poder político viene del pueblo"), ("revoluciones atlánticas", "procesos revolucionarios de la misma época a ambos lados del océano Atlántico")],
    [
        ("Ubicar en el tiempo", "La independencia de Estados Unidos fue declarada en 1776. ¿En qué siglo ocurrió?", ["1776 está entre 1701 y 1800.", "Es el siglo XVIII."], "En el siglo XVIII"),
        ("Ubicar en el espacio", "¿Qué colonias declararon su independencia en 1776: las colonias británicas de América del Norte o las españolas de América del Sur?", ["1776 se refiere a Estados Unidos.", "Eran colonias británicas."], "Las colonias británicas de América del Norte"),
    ],
    [
        ("Creer que las tres revoluciones fueron iguales.", "Cada una tuvo causas, actores y resultados propios, aunque compartieran ideas.", "Compara con un criterio."),
        ("Pensar que las ideas ilustradas se aplicaron a todas las personas.", "Muchas mujeres, esclavizados e indígenas quedaron fuera.", "Pregunta quién quedó excluido."),
    ],
    [
        ("¿En qué año declararon su independencia las Trece Colonias?", "En 1776", "Se dice en el primer párrafo."),
        ("¿En qué año comenzó la Revolución Francesa?", "En 1789", "Se dice en el primer párrafo."),
        ("¿Desde qué año la crisis de la monarquía española abrió camino a las independencias hispanoamericanas?", "Desde 1808", "Se dice en el primer párrafo."),
    ],
    [
        ("¿Qué ideas ilustradas usaron los protagonistas de estas revoluciones? Nombra dos.", "Soberanía popular, constitución, separación de poderes, libertad o igualdad", "Se enumeran en el segundo párrafo."),
        ("¿Por qué se llaman «revoluciones atlánticas»?", "Porque ocurrieron a ambos lados del Atlántico y se influyeron entre sí", "Está en el vocabulario."),
        ("¿Qué proceso terminó con la monarquía absoluta en Francia?", "La Revolución Francesa", "Se dice en el primer párrafo."),
    ],
    [
        arith("La independencia de Estados Unidos fue en 1776 y la Revolución Francesa comenzó en 1789. ¿Cuántos años pasaron entre ambas?", "1789-1776", "Se resta el año menor al mayor."),
        arith("Desde 1808 hasta 1824, año de la batalla final de las independencias hispanoamericanas en Ayacucho, ¿cuántos años pasaron?", "1824-1808", "Se resta el año de inicio al de término."),
        ("Una ficha de ejemplo dice: «1789: en París, representantes del pueblo se declaran Asamblea». ¿Qué proceso y qué idea ilustrada aparecen?", "La Revolución Francesa; la soberanía popular", "Los representantes del pueblo actúan en nombre de la nación."),
    ],
    [
        ("Un estudiante escribe: «Las independencias hispanoamericanas empezaron en 1776». ¿Qué error comete?", "Confunde con la independencia de Estados Unidos; las hispanoamericanas comenzaron desde 1808", "1776 corresponde a las Trece Colonias."),
        ("¿Por qué conviene mirar las tres revoluciones juntas?", "Porque ocurrieron en el mismo espacio y época y se influyeron con ideas y ejemplos", "Eso es lo que significa «atlánticas»."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A = Revolución Francesa (1789), B = independencia de Estados Unidos (1776), C = crisis de la monarquía española (1808).", "B, A, C", "Las fechas en orden son 1776, 1789 y 1808."),
        arith("Un mapa de ejemplo marca 13 colonias y 4 grandes virreinatos españoles. ¿Cuántos territorios coloniales marca?", "13+4", "Se suman los dos grupos."),
    ],
    [("Una línea de tiempo de ejemplo dice: «1776: Estados Unidos. 1789: Francia. 1808: crisis en España». ¿Cuántos procesos revolucionarios o de crisis distintos aparecen y cuál es el último?", "3; la crisis en España (1808)", "Son tres fechas y la más reciente es 1808.")],
    [("¿Qué es una revolución?", "Un cambio profundo y rápido del orden político o social", "Está en el vocabulario."), ("¿Qué ideas comparten estas revoluciones?", "Ideas ilustradas como soberanía popular y libertad", "Se explicó en el segundo párrafo."), ("¿Qué siglo ve el comienzo de estos procesos?", "El siglo XVIII", "1776 y 1789 están en ese siglo.")],
    (
        "Dibuja una línea de tiempo con cuatro hitos: 1776 (Estados Unidos), 1789 (Francia), 1808 (crisis en España) y 1824 (fin de las independencias hispanoamericanas). Bajo cada hito escribe una idea ilustrada que se relacione y una pregunta sobre quién quedó excluido.",
        "1776: libertad e igualdad; ¿quedaron fuera los esclavizados? 1789: soberanía popular; ¿y las mujeres? 1808: juntas; ¿y los indígenas? 1824: república; ¿y los esclavizados?",
        ["ubica los cuatro hitos", "relaciona una idea ilustrada con cada uno", "formula preguntas sobre exclusión"],
        ["línea de tiempo con cuatro hitos"],
        ["desordenar las fechas", "olvidar a los excluidos"],
        "Explica tu línea de tiempo a una persona de tu casa.",
    ),
    "Escribe en tres líneas qué tienen en común las tres revoluciones.",
    "Escribe una pregunta sobre cómo se enteraban las personas de lo que pasaba en otros países.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a contextualizar y seleccionar fuentes sobre las revoluciones: declaraciones, constituciones, cartas y discursos. Sirve para ver cómo las ideas ilustradas aparecen en los textos y qué silencian.",
    ["Conozco las tres revoluciones y las ideas ilustradas.", "Sé que una fuente tiene autor, fecha y propósito."],
    [
        "Cada revolución produjo textos importantes. En 1776 la Declaración de Independencia de Estados Unidos, redactada sobre todo por Thomas Jefferson, afirmó que todos los hombres son creados iguales y que tienen derechos como la vida, la libertad y la búsqueda de la felicidad. En 1787 se aprobó la Constitución de Estados Unidos, que separó el poder en tres ramas. En 1789, la Declaración de los Derechos del Hombre y del Ciudadano proclamó la libertad, la igualdad ante la ley y la soberanía de la nación.",
        "En Hispanoamérica, un texto muy conocido es la Carta de Jamaica (1815), escrita por Simón Bolívar, que analiza la situación de América y reflexiona sobre cómo organizar las nuevas naciones. Hay también juntas de gobierno, proclamas y periódicos. Estas fuentes expresan las ideas de líderes educados, sobre todo criollos.",
        "Al leer estos textos hay que preguntar: ¿quién habla?, ¿a quién se dirige?, ¿qué excluye? La Declaración de Estados Unidos dice «todos los hombres», pero en ese tiempo muchas personas estaban esclavizadas y las mujeres no votaban. Un texto expresa un ideal, pero no prueba que se cumpliera. Para saber si se aplicó hay que buscar otras fuentes, como leyes, censos o testimonios.",
    ],
    [("declaración", "texto que proclama principios, derechos o decisiones"), ("constitución", "ley fundamental que organiza el poder y protege derechos"), ("proclama", "texto o discurso dirigido al público para anunciar o convocar"), ("ideal", "meta o valor que se quiere alcanzar, aunque aún no se logre"), ("exclusión", "dejar fuera de ciertos derechos a un grupo de personas")],
    [
        ("Identificar al autor y la idea", "Una paráfrasis de ejemplo dice: «Todos los hombres nacen iguales y tienen derecho a la libertad». ¿A qué texto de la clase se parece?", ["Habla de igualdad y libertad.", "Se parece a la Declaración de Independencia de Estados Unidos."], "A la Declaración de Independencia de Estados Unidos"),
        ("Identificar una exclusión", "La declaración dice «todos los hombres», pero había personas esclavizadas. ¿Qué exclusión muestra?", ["Muchas personas no tenían los mismos derechos.", "Los esclavizados quedaban fuera."], "La exclusión de las personas esclavizadas"),
    ],
    [
        ("Creer que un texto describe lo que ocurría.", "Expresa un ideal; hay que verificarlo con otras fuentes.", "Busca leyes, censos o testimonios."),
        ("Pensar que los textos de los líderes hablan por todos.", "Eran líderes educados, sobre todo criollos o burgueses.", "Pregunta quién no aparece."),
    ],
    [
        ("¿Quién redactó sobre todo la Declaración de Independencia de Estados Unidos?", "Thomas Jefferson", "Se dice en el primer párrafo."),
        ("¿Qué proclamó la Declaración de los Derechos del Hombre y del Ciudadano de 1789?", "Libertad, igualdad ante la ley y soberanía de la nación", "Se dice en el primer párrafo."),
        ("¿Quién escribió la Carta de Jamaica?", "Simón Bolívar", "Se dice en el segundo párrafo."),
    ],
    [
        ("¿Por qué un texto es solo un ideal?", "Porque dice lo que se quiere lograr, no que se cumpliera", "Lo explica el tercer párrafo."),
        ("¿Qué separó la Constitución de Estados Unidos de 1787?", "El poder en tres ramas", "Se dice en el primer párrafo."),
        ("¿Quiénes escribían la mayoría de estos textos en Hispanoamérica?", "Líderes educados, sobre todo criollos", "Se dice en el segundo párrafo."),
    ],
    [
        arith("La Carta de Jamaica es de 1815 y la Declaración de Independencia de Estados Unidos de 1776. ¿Cuántos años pasaron?", "1815-1776", "Se resta el año menor al mayor."),
        ("Pregunta: ¿se aplicó la igualdad a las mujeres en 1789? Fuentes: 1 = Declaración de 1789; 2 = leyes de la época sobre quién votaba; 3 = poema patriótico. ¿Cuál es la más adecuada?", "La 2", "Las leyes sobre el voto muestran quién tenía derechos."),
        ("Una proclama de ejemplo dice: «¡Ciudadanos, nuestra patria será libre!». ¿A quién se dirige y qué quiere lograr?", "A los ciudadanos; convocarlos a la independencia", "Una proclama convoca al público."),
    ],
    [
        ("Un estudiante concluye: «Como la Declaración dice igualdad, todos eran iguales». ¿Qué límite tiene la conclusión?", "El texto expresa un ideal; la ley y la práctica excluían a muchos grupos", "Un ideal no prueba que se cumpliera."),
        ("¿Por qué conviene cruzar una declaración con una ley sobre el voto?", "Porque la declaración dice el ideal y la ley muestra quién tenía realmente derechos", "Cada fuente aporta algo distinto."),
    ],
    [
        ("Ordena por fecha de más antigua a más reciente: A = Constitución de EE.UU. (1787), B = Declaración de Derechos del Hombre (1789), C = Declaración de Independencia de EE.UU. (1776).", "C, A, B", "Las fechas en orden son 1776, 1787 y 1789."),
        arith("En una asamblea de ejemplo votan a favor de una declaración 85 de 100 representantes. ¿Cuántos no votaron a favor?", "100-85", "Se resta el número a favor del total."),
    ],
    [("Una carta de ejemplo de 1810 dice: «Hemos formado una junta para gobernarnos mientras el rey está preso». ¿Qué tipo de fuente es y qué puede mostrar?", "Una carta; una decisión de autogobierno de los criollos", "Informa sobre la formación de una junta.")],
    [("¿Qué es una proclama?", "Un texto o discurso dirigido al público para anunciar o convocar", "Está en el vocabulario."), ("¿Qué es una exclusión?", "Dejar fuera de ciertos derechos a un grupo", "Está en el vocabulario."), ("¿Qué pregunta ayuda a leer una declaración?", "¿Quién queda fuera de lo que dice?", "Se explicó en el tercer párrafo.")],
    (
        "Lee esta paráfrasis de ejemplo: «Los representantes del pueblo declaran que todos los ciudadanos son iguales ante la ley y que el poder viene de la nación». Escribe una tabla con cuatro filas: qué idea ilustrada aparece, qué texto de la clase se parece, quién podría quedar excluido, qué fuente adicional pedirías.",
        "Ideas: igualdad ante la ley y soberanía de la nación. Se parece a la Declaración de 1789. Podrían quedar excluidas las mujeres y esclavizados. Pediría las leyes sobre voto.",
        ["identifica ideas ilustradas", "relaciona con un texto de la clase", "señala una exclusión", "propone una fuente adicional"],
        ["tabla de cuatro filas"],
        ["tomar el ideal como realidad", "no señalar exclusión"],
        "Pregunta a una persona de tu casa qué derechos cree que faltaban en el pasado.",
    ),
    "Escribe una frase que resuma cada texto de la clase.",
    "Escribe una pregunta sobre quién no podía votar en esa época.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a relacionar cambio, continuidad y territorio en los procesos revolucionarios: qué transformaron y qué se mantuvo. Sirve para ver cuánto cambió la vida política y qué siguió igual.",
    ["Conozco las tres revoluciones y sus textos.", "Sé ubicar Estados Unidos, Francia e Hispanoamérica en un mapa."],
    [
        "Las revoluciones produjeron cambios importantes. En Estados Unidos, las colonias se independizaron y formaron una república federal con constitución. En Francia, terminó el poder absoluto del rey y la sociedad dividida en estamentos: clero, nobleza y tercer estado. En Hispanoamérica, las colonias dejaron de depender de España y se organizaron como repúblicas. En todos los casos se aceptó que el poder viene del pueblo y debe estar limitado por una constitución.",
        "También hubo continuidades. La esclavitud siguió en Estados Unidos hasta 1865. En Francia, la esclavitud se abolió en las colonias en 1794 pero fue restablecida en 1802. En Hispanoamérica, las élites criollas conservaron el poder y la tierra, y muchas desigualdades coloniales siguieron. Las mujeres no obtuvieron derecho a voto en estos países en esa época.",
        "El territorio también influyó. Estados Unidos era un conjunto de colonias que ya tenían asambleas propias; Francia era un reino con una larga tradición monárquica; Hispanoamérica era un enorme espacio con grandes distancias, regiones muy distintas y poblaciones diversas. Por eso las revoluciones fueron diferentes en forma y duración.",
    ],
    [("estamento", "grupo social con distinto honor y derechos según el nacimiento, como la nobleza"), ("república federal", "república formada por estados con gobiernos propios y un gobierno común"), ("tercer estado", "en la Francia antigua, el grupo que no era ni clero ni nobleza"), ("abolir", "terminar oficialmente con una ley o práctica, como la esclavitud"), ("élite criolla", "grupo de criollos ricos o poderosos")],
    [
        ("Reconocer un cambio", "En Francia terminó la sociedad dividida en estamentos. ¿Es un cambio o una continuidad?", ["Antes existía esa división.", "Después terminó."], "Un cambio"),
        ("Reconocer una continuidad", "La esclavitud siguió en Estados Unidos hasta 1865. ¿Es un cambio o una continuidad?", ["No terminó con la independencia.", "Se mantuvo."], "Una continuidad"),
    ],
    [
        ("Creer que la independencia terminó con las desigualdades.", "Las élites conservaron el poder y siguieron desigualdades coloniales.", "Busca continuidades."),
        ("Creer que todas las revoluciones se dieron en un mismo territorio.", "Tuvieron escenarios muy distintos.", "Relaciona el territorio con la forma de cada proceso."),
    ],
    [
        ("¿Hasta qué año siguió la esclavitud en Estados Unidos?", "Hasta 1865", "Se dice en el segundo párrafo."),
        ("¿Qué tres estamentos había en Francia antes de la Revolución?", "Clero, nobleza y tercer estado", "Se enumeran en el primer párrafo."),
        ("¿Qué forma de gobierno adoptaron las colonias hispanoamericanas?", "Repúblicas", "Se dice en el primer párrafo."),
    ],
    [
        ("¿Qué grupo conservó el poder en Hispanoamérica?", "Las élites criollas", "Se dice en el segundo párrafo."),
        ("¿Qué pasó con la esclavitud en las colonias francesas entre 1794 y 1802?", "Se abolió en 1794 y se restableció en 1802", "Se dice en el segundo párrafo."),
        ("¿Por qué las revoluciones fueron diferentes en forma y duración?", "Por las diferencias de territorio, tradición política y población", "Se explicó en el tercer párrafo."),
    ],
    [
        arith("La esclavitud se abolió en las colonias francesas en 1794 y se restableció en 1802. ¿Cuántos años estuvo abolida?", "1802-1794", "Se resta el año de la abolición al del restablecimiento."),
        arith("Un censo de ejemplo de una región hispanoamericana tiene 700 criollos, 1.200 mestizos y 1.100 indígenas. ¿Cuántas personas hay en total?", "700+1200+1100", "Se suman los tres grupos."),
        ("Un mapa de ejemplo muestra a Hispanoamérica mucho más extensa que las Trece Colonias. ¿Qué dificultad implicaba esa extensión?", "Grandes distancias y regiones muy distintas, que dificultaban coordinar la revolución", "El territorio influía en cómo se desarrollaba cada proceso."),
    ],
    [
        ("Un estudiante dice: «Con la independencia se abolió toda forma de esclavitud en América». ¿Qué error comete?", "Ignora que en Estados Unidos siguió hasta 1865 y que en otros lugares terminó después", "La esclavitud continuó en varios territorios."),
        ("¿Por qué se puede decir que hubo cambios y continuidades al mismo tiempo?", "Porque cambió quién gobernaba, pero se mantuvieron muchas desigualdades", "Cambió la forma de gobierno y siguieron exclusiones."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A = restablecimiento de la esclavitud francesa (1802), B = abolición en las colonias francesas (1794), C = fin de la esclavitud en EE.UU. (1865).", "B, A, C", "Las fechas en orden son 1794, 1802 y 1865."),
        arith("Una asamblea de ejemplo tiene 100 representantes: 65 de la élite criolla y los demás de otros grupos. ¿Cuántos son de otros grupos?", "100-65", "Se resta la élite del total."),
    ],
    [("Una tabla de ejemplo: «Francia 1789: fin de los estamentos. EE.UU. 1776: república federal. Hispanoamérica 1810: repúblicas». ¿Qué lugar adoptó una república federal?", "Estados Unidos", "La tabla lo asigna a EE.UU.")],
    [("¿Qué es un estamento?", "Un grupo social con distinto honor y derechos según el nacimiento", "Está en el vocabulario."), ("¿Qué grupo no obtuvo derecho a voto?", "Las mujeres", "Se dice en el segundo párrafo."), ("¿Qué se mantuvo en Hispanoamérica?", "El poder de las élites criollas y muchas desigualdades", "Se explicó en el segundo párrafo.")],
    (
        "Completa una tabla de tres filas (Estados Unidos, Francia, Hispanoamérica) y dos columnas (qué cambió, qué continuó), usando los datos de la clase. Escribe una frase al final que explique cómo influyó el territorio.",
        "EE.UU.: cambió el gobierno y se formó una república federal; continuó la esclavitud. Francia: terminaron los estamentos; continuó la esclavitud colonial tras 1802. Hispanoamérica: se formaron repúblicas; continuaron las élites y desigualdades. El territorio explica las diferencias.",
        ["completa las tres filas", "incluye cambio y continuidad", "explica el papel del territorio"],
        ["tabla de tres filas y una frase"],
        ["decir que todo cambió", "olvidar la esclavitud"],
        "Explica a una persona de tu casa qué cambió y qué no.",
    ),
    "Dibuja tres cajas (EE.UU., Francia, Hispanoamérica) con un cambio en cada una.",
    "Escribe una pregunta sobre cómo vivían las personas que no tenían derechos.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a contrastar actores, causas y perspectivas de las tres revoluciones. Sirve para ver quiénes las impulsaron, por qué y quiénes quedaron fuera.",
    ["Conozco el contexto de cada revolución.", "Sé que una perspectiva es un punto de vista."],
    [
        "Cada revolución tuvo causas propias. En las Trece Colonias, los colonos rechazaron los impuestos que Gran Bretaña les cobraba sin que tuvieran representantes en el Parlamento. Su lema fue «no hay impuestos sin representación». En Francia, el Estado estaba endeudado, había hambre y desigualdad, y el tercer estado, que pagaba impuestos, pedía participación. En Hispanoamérica, la crisis de la monarquía española en 1808, el descontento criollo y las ideas ilustradas llevaron a formar juntas de gobierno.",
        "Los actores también cambiaron. En Estados Unidos fueron colonos propietarios, comerciantes y abogados. En Francia, la burguesía, artesanos y campesinos; los sectores populares de París tuvieron un papel importante. En Hispanoamérica, los criollos fueron líderes, pero participaron también mestizos, indígenas y personas esclavizadas, muchas veces buscando su propia libertad. En todas partes hubo quienes se opusieron: lealistas, nobles y miembros del clero.",
        "Las perspectivas eran distintas: para los patriotas era libertad; para los lealistas, traición; para las personas esclavizadas, una posibilidad de libertad real; para las mujeres, una oportunidad que rara vez se reconoció. Contrastar perspectivas permite no repetir un relato oficial único.",
    ],
    [("lealista", "persona que permaneció fiel al rey o a la metrópoli durante la independencia"), ("patriota", "persona que apoyaba la independencia de su territorio"), ("junta de gobierno", "grupo que gobierna temporalmente en lugar de la autoridad anterior"), ("representación", "posibilidad de tener delegados que hablen y decidan en nombre de un grupo"), ("causa", "razón o hecho que explica por qué ocurre algo")],
    [
        ("Reconocer la causa", "Los colonos de Estados Unidos protestaron por los impuestos sin representación. ¿Qué tipo de causa es?", ["Se refiere a impuestos y a participación política.", "Es una causa política y económica."], "Una causa política y económica"),
        ("Contrastar perspectivas", "Un patriota dice que luchaba por la libertad y un lealista dice que traicionaba al rey. ¿Qué muestra el contraste?", ["Dos puntos de vista sobre el mismo hecho.", "Cada uno usa palabras distintas."], "Que cada grupo juzgaba el mismo hecho desde su perspectiva"),
    ],
    [
        ("Creer que todos los habitantes apoyaban la revolución.", "Hubo lealistas, nobles y clero que se opusieron.", "Distingue patriotas y lealistas."),
        ("Pensar que solo los criollos participaron en Hispanoamérica.", "Mestizos, indígenas y esclavizados también participaron.", "Incluye a todos los actores."),
    ],
    [
        ("¿Qué lema usaron los colonos de Estados Unidos?", "«No hay impuestos sin representación»", "Se dice en el primer párrafo."),
        ("¿Quiénes impulsaron principalmente las juntas hispanoamericanas?", "Los criollos", "Se explicó en el segundo párrafo."),
        ("¿Qué es un lealista?", "Una persona que permaneció fiel al rey o a la metrópoli", "Está en el vocabulario."),
    ],
    [
        ("Menciona dos causas de la Revolución Francesa.", "La deuda del Estado, el hambre o la desigualdad", "Se enumeran en el primer párrafo."),
        ("¿Por qué las personas esclavizadas podían apoyar la revolución?", "Porque veían una posibilidad real de ser libres", "Se explicó en el tercer párrafo."),
        ("¿Qué causa desencadenó las juntas en Hispanoamérica?", "La crisis de la monarquía española en 1808", "Se dice en el primer párrafo."),
    ],
    [
        arith("Una asamblea de ejemplo tiene 90 patriotas y 35 lealistas. ¿Cuántas personas son?", "90+35", "Se suman los dos grupos."),
        ("Fuente 1 (patriota): «Defendemos la libertad». Fuente 2 (lealista): «Los rebeldes destruyen el orden». ¿Qué fuente critica la revolución?", "La fuente 2", "El lealista habla de destrucción del orden."),
        ("Una mujer de ejemplo ayuda a sostener a un ejército patriota con comida y cuidados. ¿Qué actor suele quedar fuera del relato oficial?", "Las mujeres", "La clase indica que su papel rara vez se reconoció."),
    ],
    [
        ("Un estudiante dice: «La Revolución Francesa fue obra solo de los nobles». ¿Qué error comete?", "Los actores principales fueron la burguesía, artesanos y campesinos, no la nobleza", "La nobleza más bien defendía sus privilegios."),
        ("¿Por qué conviene leer fuentes de patriotas y de lealistas?", "Porque se contrastan perspectivas y no se repite un relato oficial único", "Cada lado explica los hechos de forma distinta."),
    ],
    [
        ("Ordena de causa a consecuencia: A = formación de juntas, B = crisis de la monarquía española (1808), C = declaración de independencia.", "B, A, C", "Primero la crisis, luego las juntas y después la declaración."),
        arith("En una votación de ejemplo, 55 votaron por la independencia, 30 en contra y 15 se abstuvieron. ¿Cuántas personas participaron en la votación?", "55+30+15", "Se suman los tres grupos."),
    ],
    [("Una carta de ejemplo de una mujer dice: «Coso uniformes para los patriotas; mi esposo es lealista y no lo sabe». ¿Qué muestra sobre las perspectivas dentro de una misma familia?", "Que había perspectivas distintas en una misma familia", "Marido y mujer tenían posturas opuestas.")],
    [("En Historia: ¿Qué es una causa?", "Una razón o hecho que explica por qué ocurre algo", "Está en el vocabulario."), ("¿Qué grupo de Francia pagaba impuestos y pedía participación?", "El tercer estado", "Se explicó en el primer párrafo."), ("¿Por qué contrastar perspectivas?", "Para no contar la historia desde un solo punto de vista", "Se explicó en el tercer párrafo.")],
    (
        "Escribe una tabla con cuatro actores: colono de las Trece Colonias, burgués francés, criollo hispanoamericano y persona esclavizada. Para cada uno anota qué buscaba y qué podía perder. Termina con una frase que explique por qué sus perspectivas diferían.",
        "Colono: no pagar impuestos sin representación; podía perder bienes. Burgués: participación política; podía perder su posición. Criollo: gobernar por sí mismo; podía perder privilegios. Persona esclavizada: libertad; podía perder la vida. Diferían porque tenían poder y derechos desiguales.",
        ["incluye los cuatro actores", "indica qué buscaba y qué podía perder", "explica la diferencia de perspectivas"],
        ["tabla de cuatro filas y una frase"],
        ["tratar a todos igual", "olvidar a la persona esclavizada"],
        "Comenta con una persona de tu casa qué actor tenía más que perder.",
    ),
    "Escribe un diálogo de seis líneas entre un patriota y un lealista.",
    "Escribe una pregunta sobre qué hacían los niños durante las revoluciones.",
)

# ================================================================ clase 5
lesson(
    OA, 5,
    "Aprenderé a construir un argumento con evidencia sobre cómo las ideas ilustradas se manifestaron en las revoluciones. Sirve para responder la pregunta central de la unidad.",
    ["Conozco las causas, actores y textos de las revoluciones.", "Sé que un argumento tiene afirmación, evidencia y límite."],
    [
        "Un argumento sobre este tema debe responder: ¿cómo se manifestaron las ideas ilustradas en las revoluciones? Una afirmación posible es: «Las revoluciones aplicaron ideas ilustradas como soberanía popular, constitución, separación de poderes y derechos individuales para fundar repúblicas y limitar el poder de los reyes».",
        "La evidencia puede venir de textos y hechos. En Estados Unidos, la Declaración de 1776 habló de derechos y la Constitución de 1787 separó los poderes. En Francia, la Declaración de 1789 proclamó libertad e igualdad ante la ley y la soberanía de la nación. En Hispanoamérica, las juntas de gobierno y las constituciones adoptaron la república y la soberanía popular.",
        "El límite es que las ideas no se aplicaron a todos: la esclavitud continuó en varios lugares, las mujeres no tuvieron derechos políticos y muchos indígenas y campesinos quedaron al margen. Además, otras causas influyeron: impuestos, crisis políticas y rivalidades de poder. Un buen argumento reconoce que las ideas ilustradas fueron una causa importante, pero no la única.",
    ],
    [("manifestarse", "mostrarse o hacerse visible en hechos y textos"), ("derechos individuales", "derechos que tiene cada persona, como la libertad de opinión"), ("multicausal", "con varias causas y no solo una"), ("evidencia", "dato o fuente que apoya una afirmación"), ("límite", "aquello que la evidencia no permite concluir")],
    [
        ("Separar afirmación y evidencia", "«La Declaración de 1789 proclamó la igualdad ante la ley». ¿Es una afirmación general o una evidencia concreta?", ["Cita un texto y su contenido.", "Es una evidencia concreta."], "Una evidencia concreta"),
        ("Formular un límite", "Con las declaraciones de las revoluciones, ¿qué no se puede saber sobre la vida diaria de los esclavizados?", ["Las declaraciones expresan ideales.", "No cuentan la experiencia de las personas esclavizadas."], "Cómo vivían realmente y qué derechos tenían en la práctica"),
    ],
    [
        ("Decir que las ideas ilustradas fueron la única causa.", "También influyeron impuestos, crisis políticas y rivalidades.", "Habla de varias causas."),
        ("Dar la afirmación sin evidencia.", "Sin datos es solo una opinión.", "Cita un texto o un hecho."),
    ],
    [
        ("¿Qué declaración proclamó libertad e igualdad ante la ley en 1789?", "La Declaración de los Derechos del Hombre y del Ciudadano", "Se dice en el segundo párrafo."),
        ("¿Qué separó la Constitución de 1787?", "El poder en tres ramas", "Se dice en el segundo párrafo."),
        ("¿Qué significa «multicausal»?", "Con varias causas y no solo una", "Está en el vocabulario."),
    ],
    [
        ("¿Qué ideas ilustradas se manifestaron en las revoluciones? Nombra dos.", "Soberanía popular, constitución, separación de poderes o derechos individuales", "Se nombran en el primer párrafo."),
        ("¿Qué límite tiene el argumento de la clase?", "Las ideas no se aplicaron a todos y hubo otras causas", "Se dice en el tercer párrafo."),
        ("¿Qué adoptaron las juntas y constituciones hispanoamericanas?", "La república y la soberanía popular", "Se dice en el segundo párrafo."),
    ],
    [
        arith("En una asamblea de ejemplo, 70 representantes votan una constitución con separación de poderes y 25 votan en contra. ¿Cuántos representantes hay?", "70+25", "Se suman a favor y en contra."),
        ("Elige la mejor evidencia para «las ideas ilustradas influyeron en las independencias hispanoamericanas»: 1 = una junta que adopta la soberanía popular y una constitución; 2 = una canción de moda; 3 = una receta.", "La 1", "La junta y la constitución muestran las ideas aplicadas."),
        ("Una afirmación de ejemplo dice: «La Ilustración causó todas las revoluciones». ¿Qué corrección propone la clase?", "Que fue una causa importante, pero no la única", "Hay causas políticas, económicas y sociales."),
    ],
    [
        ("Un estudiante dice: «Las revoluciones fueron perfectas porque aplicaron la igualdad». ¿Qué error comete?", "Ignora que muchas personas quedaron excluidas de la igualdad", "La clase señala esa exclusión."),
        ("¿Por qué reconocer el límite hace más fuerte el argumento?", "Porque muestra que la conclusión no exagera lo que prueban las fuentes", "Declarar límites da honestidad al argumento."),
    ],
    [
        ("Ordena las partes de un argumento: A = límite, B = afirmación, C = evidencia.", "B, C, A", "Primero se afirma, luego se prueba y al final se declara el límite."),
        arith("Un periódico de ejemplo publica 12 artículos sobre derechos y 8 sobre impuestos. ¿Cuántos artículos publica?", "12+8", "Se suman los dos grupos."),
    ],
    [("Datos de ejemplo: «Una junta de 1810 declara que el poder viene del pueblo; solo votan 200 de 5.000 habitantes». ¿Qué límite muestra el dato sobre la soberanía popular en esa junta?", "Que casi nadie podía votar: solo 200 de 5.000 habitantes", "La junta declaró que el poder viene del pueblo, pero la gran mayoría de los habitantes no participaba.")],
    [("¿Qué es una afirmación?", "La respuesta que defiendes ante una pregunta", "Es la parte central del argumento."), ("¿Qué dos textos son evidencia de las ideas ilustradas?", "La Declaración de 1776 y la de 1789", "Se nombran en la clase."), ("¿Por qué hay que incluir causas distintas?", "Porque los procesos tuvieron varias causas", "Se explicó en el tercer párrafo.")],
    (
        "Responde en cinco líneas: «¿Cómo se manifestaron las ideas ilustradas en las revoluciones?». Usa esta evidencia de ejemplo: Declaración de 1776; Constitución de 1787 con tres poderes; Declaración de 1789; juntas hispanoamericanas con soberanía popular. Incluye afirmación, dos datos y un límite.",
        "Las ideas ilustradas se manifestaron en declaraciones y constituciones que fundaron repúblicas. Datos: Declaración de 1789 con libertad e igualdad y Constitución de 1787 con tres poderes. Límite: no se aplicaron a mujeres ni esclavizados.",
        ["escribe una afirmación clara", "usa dos datos", "incluye un límite pertinente"],
        ["texto de cinco líneas"],
        ["no incluir límite", "decir que fue la única causa"],
        "Lee tu texto a una persona de tu casa y pídele que diga cuál es tu afirmación.",
    ),
    "Dibuja un esquema con tres columnas (EE.UU., Francia, Hispanoamérica) y una evidencia en cada una.",
    "Escribe una frase que explique por qué un argumento necesita evidencia.",
)

# ================================================================ clase 6
lesson(
    OA, 6,
    "Aprenderé a evaluar proyecciones y límites de las revoluciones atlánticas: qué legado dejaron y qué problemas quedaron sin resolver. Sirve para valorar su importancia sin idealizarlas.",
    ["Conozco las causas, actores y textos de las revoluciones.", "Sé construir un argumento con afirmación, evidencia y límite."],
    [
        "Las revoluciones atlánticas dejaron un legado político duradero. Extendieron la idea de que el poder viene del pueblo, que existen derechos que el Estado debe respetar y que la ley debe valer para todos. Muchas constituciones actuales recogen la separación de poderes y la protección de derechos. También dieron origen a nuevas repúblicas en América, y en la Revolución Francesa nació el lema «libertad, igualdad, fraternidad».",
        "Pero también tuvieron límites. En Francia hubo una etapa de violencia política, llamada el Terror (1793-1794), en que muchas personas fueron ejecutadas. En varios países, la esclavitud no terminó de inmediato, las mujeres no pudieron votar durante mucho tiempo y los pueblos indígenas quedaron al margen. En Hispanoamérica hubo guerras, inestabilidad y dificultades para organizar los nuevos Estados.",
        "Evaluar es separar el legado de la exageración. Se puede afirmar que las ideas ilustradas ampliaron los derechos a largo plazo. No se puede afirmar que los lograran de inmediato ni para todos. Además, hay que reconocer los límites de las fuentes: casi todas hablan de lo que decían los líderes, no de lo que vivían las personas comunes.",
    ],
    [("legado", "lo que una época deja a las siguientes"), ("Terror", "etapa de violencia política en Francia entre 1793 y 1794"), ("fraternidad", "unión y solidaridad entre las personas"), ("proyección", "continuidad de un hecho hacia épocas posteriores"), ("inestabilidad", "falta de orden y estabilidad política")],
    [
        ("Reconocer un legado", "¿Qué idea de las revoluciones sigue presente en muchas constituciones actuales?", ["La clase menciona la separación de poderes.", "Es parte del legado político."], "La separación de poderes y la protección de derechos"),
        ("Reconocer un límite", "¿Qué violencia política ocurrió en Francia entre 1793 y 1794?", ["Fue una etapa de ejecuciones.", "Se llama el Terror."], "El Terror"),
    ],
    [
        ("Idealizar las revoluciones y olvidar sus problemas.", "Hubo violencia, exclusiones y desigualdades.", "Incluye ventajas y límites."),
        ("Creer que los derechos se lograron de inmediato.", "Se ampliaron a largo plazo.", "Distingue lo propuesto y lo logrado."),
    ],
    [
        ("¿Qué lema nació en la Revolución Francesa?", "«Libertad, igualdad, fraternidad»", "Se dice en el primer párrafo."),
        ("¿Qué es un legado?", "Lo que una época deja a las siguientes", "Está en el vocabulario."),
        ("¿Entre qué años ocurrió el Terror?", "Entre 1793 y 1794", "Se dice en el segundo párrafo."),
    ],
    [
        ("Menciona dos límites de las revoluciones.", "Violencia, esclavitud que continuó, exclusión de mujeres o de indígenas", "Se enumeran en el segundo párrafo."),
        ("¿Qué se puede afirmar sobre las ideas ilustradas y los derechos?", "Que los ampliaron a largo plazo", "Se explicó en el tercer párrafo."),
        ("¿Por qué las fuentes tienen límites?", "Porque casi todas hablan de lo que decían los líderes, no de lo que vivían las personas comunes", "Lo dice el tercer párrafo."),
    ],
    [
        arith("El Terror duró de 1793 a 1794, es decir, aproximadamente un año. Si la Revolución comenzó en 1789, ¿cuántos años pasaron entre su inicio y el inicio del Terror?", "1793-1789", "Se resta el año de inicio de la Revolución al del Terror."),
        ("Una afirmación de ejemplo dice: «Las revoluciones no dejaron ningún legado». ¿Qué evidencia de la clase la contradice?", "Las constituciones actuales recogen la separación de poderes y los derechos", "Ese es un legado duradero."),
        ("Elige la mejor fuente para evaluar si las mujeres obtuvieron derecho a voto: 1 = leyes sobre el sufragio; 2 = poema patriótico; 3 = retrato de un general.", "La 1", "Las leyes indican quién podía votar."),
    ],
    [
        ("Un estudiante dice: «Las revoluciones fueron un fracaso porque hubo violencia». ¿Qué error comete?", "Juzga solo un aspecto; también dejaron un legado de derechos y repúblicas", "Hay que evaluar ventajas y límites."),
        ("¿Por qué no se puede decir que las ideas se aplicaron a todos de inmediato?", "Porque la esclavitud siguió, las mujeres no votaban y los indígenas quedaron al margen", "La clase muestra esas exclusiones."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A = Terror (1793-1794), B = Declaración de 1776, C = Carta de Jamaica (1815).", "B, A, C", "Las fechas en orden son 1776, 1793 y 1815."),
        arith("Si una constitución de ejemplo de 1811 siguió vigente hasta 1830, ¿cuántos años estuvo vigente?", "1830-1811", "Se resta el año de inicio al de término."),
    ],
    [("Un texto de ejemplo dice: «Mi bisabuela no pudo votar; mi abuela sí pudo votar en 1949». Un estudiante lo relaciona con las revoluciones. ¿Qué idea ilustrada tardó en aplicarse a las mujeres?", "La igualdad de derechos políticos", "El texto muestra que el voto femenino llegó mucho después.")],
    [("¿Qué es la inestabilidad política?", "La falta de orden y estabilidad en el gobierno", "Está en el vocabulario."), ("¿Qué grupo de personas quedó al margen en Hispanoamérica?", "Los pueblos indígenas", "Se dice en el segundo párrafo."), ("¿Qué hay que evitar al evaluar las revoluciones?", "Idealizarlas o rechazarlas por completo", "Se explicó en el tercer párrafo.")],
    (
        "Escribe un párrafo de seis líneas: «El legado y los límites de las revoluciones atlánticas». Incluye dos elementos del legado, dos límites y una pregunta que no puedes responder con las fuentes de la unidad.",
        "Legado: la soberanía popular y la separación de poderes. Límites: la esclavitud siguió y las mujeres no votaban. Pregunta: ¿cómo vivían las personas comunes durante las guerras?",
        ["incluye dos elementos del legado", "incluye dos límites", "formula una pregunta honesta"],
        ["párrafo de seis líneas"],
        ["idealizar las revoluciones", "olvidar a los excluidos"],
        "Lee el párrafo a una persona de tu casa y pídele que diga qué legado le parece más importante.",
    ),
    "Escribe tres frases con las palabras legado, límite y proyección.",
    "Escribe qué derecho de los que tienes hoy crees que se debe a estas revoluciones.",
)
