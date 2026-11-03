"""Cuaderno del estudiante, 8.º básico Historia, Geografía y Ciencias Sociales: OA 16 (independencias hispanoamericanas y de Chile)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI08 OA 16"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a situar en el tiempo y el espacio la independencia hispanoamericana y la de Chile, y a plantear el problema: por qué un proceso continental tomó caminos propios en cada lugar.",
    ["Conozco la Ilustración y las revoluciones atlánticas.", "Sé ubicar los Andes y los principales países de Sudamérica en un mapa."],
    [
        "La independencia de las colonias hispanoamericanas fue un proceso continental: ocurrió en casi toda América hispana entre 1808 y la década de 1820. Tuvo un detonante común: en 1808, Napoleón invadió España y obligó a abdicar al rey Fernando VII. Sin rey legítimo, muchos criollos se preguntaron quién debía gobernar y formaron juntas de gobierno en nombre del monarca preso. Con el tiempo, pasaron de gobernar en su nombre a proclamar la independencia.",
        "En Chile, el proceso comenzó el 18 de septiembre de 1810, con la formación de la Primera Junta Nacional de Gobierno. Se suele dividir en etapas: la Patria Vieja (1810-1814), la Reconquista española (1814-1817) y la Patria Nueva (1817-1823). El 12 de febrero de 1817 el Ejército de los Andes, dirigido por José de San Martín, venció en Chacabuco. La independencia fue proclamada el 12 de febrero de 1818 y consolidada en la batalla de Maipú, el 5 de abril de 1818.",
        "El problema de esta unidad es: ¿por qué la independencia fue un proceso continental pero con rasgos propios en cada región, y cómo se vivió en Chile? Para responder hay que ubicar las fechas, los lugares y los actores, y recordar que no todos los habitantes apoyaban la independencia ni participaban en igual forma.",
    ],
    [("criollo", "hijo de españoles nacido en América"), ("junta de gobierno", "grupo que gobierna temporalmente en lugar de la autoridad anterior"), ("Patria Vieja", "primera etapa de la independencia de Chile, entre 1810 y 1814"), ("Reconquista", "período entre 1814 y 1817 en que los españoles recuperaron el control de Chile"), ("Patria Nueva", "etapa entre 1817 y 1823 en que Chile se declaró independiente")],
    [
        ("Ubicar en el tiempo", "La Primera Junta de Gobierno de Chile se formó el 18 de septiembre de 1810. ¿En qué etapa se ubica?", ["La clase fija etapas por años.", "1810 pertenece a la Patria Vieja."], "En la Patria Vieja"),
        ("Reconocer el detonante común", "¿Qué ocurrió en 1808 en España que abrió camino a las juntas?", ["Napoleón invadió España.", "El rey Fernando VII quedó preso."], "Napoleón invadió España y el rey Fernando VII quedó impedido de gobernar"),
    ],
    [
        ("Creer que la independencia comenzó con una declaración en 1810.", "En 1810 se formó una junta que gobernaba en nombre del rey; la independencia se proclamó en 1818.", "Distingue junta e independencia."),
        ("Pensar que todos los habitantes apoyaban la independencia.", "Hubo realistas y patriotas, y muchos indiferentes.", "Revisa los distintos bandos."),
    ],
    [
        ("¿Qué etapa va de 1810 a 1814?", "La Patria Vieja", "Está en el vocabulario."),
        ("¿En qué año se proclamó la independencia de Chile?", "En 1818", "Se dice en el segundo párrafo."),
        ("¿Quién dirigía el Ejército de los Andes?", "José de San Martín", "Se dice en el segundo párrafo."),
    ],
    [
        ("¿Por qué se formaron juntas de gobierno en América en 1808 y 1810?", "Porque el rey estaba preso y los criollos se preguntaron quién debía gobernar", "Lo explica el primer párrafo."),
        ("¿Qué batalla consolidó la independencia de Chile en abril de 1818?", "Maipú", "Se dice en el segundo párrafo."),
        ("¿Qué período va de 1814 a 1817?", "La Reconquista española", "Está en el vocabulario."),
    ],
    [
        arith("La Primera Junta se formó en 1810 y la independencia se proclamó en 1818. ¿Cuántos años pasaron entre ambos hechos?", "1818-1810", "Se resta el año menor al mayor."),
        arith("La Patria Nueva duró de 1817 a 1823. ¿Cuántos años abarca?", "1823-1817", "Se resta el año de inicio al de término."),
        ("Una ficha de ejemplo dice: «12 de febrero de 1817: el ejército cruza los Andes y vence en Chacabuco». ¿Qué batalla es y qué etapa comienza poco después?", "Chacabuco; la Patria Nueva", "Chacabuco inició la Patria Nueva."),
    ],
    [
        ("Un estudiante dice: «Chile fue independiente desde 1810». ¿Qué error comete?", "En 1810 se formó una junta que gobernaba en nombre del rey; la independencia se proclamó en 1818", "No hay que confundir autogobierno con independencia."),
        ("¿Por qué se dice que la independencia fue un proceso continental?", "Porque ocurrió en casi toda América hispana, con causas comunes y ritmos distintos", "Las colonias reaccionaron a la misma crisis."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A = Maipú (1818), B = Primera Junta (1810), C = Chacabuco (1817).", "B, C, A", "Las fechas en orden son 1810, 1817 y 1818."),
        arith("Un ejército de ejemplo tiene 3.000 soldados de infantería y 1.500 de caballería. ¿Cuántos soldados tiene?", "3000+1500", "Se suman los dos grupos."),
    ],
    [("Una línea de tiempo de ejemplo dice: «1808 Napoleón invade España; 1810 Primera Junta; 1814 Reconquista; 1818 independencia». ¿Cuántos años duró la Reconquista, de 1814 a 1817?", "3 años", "1817 menos 1814 es 3.")],
    [("¿Qué es una junta de gobierno?", "Un grupo que gobierna temporalmente en lugar de la autoridad anterior", "Está en el vocabulario."), ("¿Qué pasó el 5 de abril de 1818?", "La batalla de Maipú", "Se explicó en el segundo párrafo."), ("¿Qué rey había quedado impedido de gobernar?", "Fernando VII", "Se explicó en el primer párrafo.")],
    (
        "Dibuja una línea de tiempo con seis hitos de Chile: 1810 (Primera Junta), 1814 (Reconquista), 1817 (Chacabuco), 1818 (independencia proclamada), 1818 (Maipú) y 1823 (fin de la Patria Nueva). Bajo cada hito escribe en qué etapa está y una pregunta sobre quién participó.",
        "1810 Primera Junta: Patria Vieja. 1814 Reconquista. 1817 Chacabuco: Patria Nueva. 1818 independencia. 1818 Maipú. 1823 fin de la Patria Nueva. Pregunta: ¿qué hicieron las mujeres?",
        ["ubica los hitos en orden", "relaciona cada hito con su etapa", "formula una pregunta"],
        ["línea de tiempo con seis hitos"],
        ["desordenar las fechas", "confundir junta e independencia"],
        "Explica tu línea de tiempo a una persona de tu casa.",
    ),
    "Escribe una frase con cada etapa de la independencia de Chile.",
    "Escribe una pregunta sobre cómo vivían los habitantes de las ciudades durante la Reconquista.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a contextualizar y seleccionar fuentes de la independencia: actas, proclamas, periódicos y constituciones. Sirve para leer textos de la época sabiendo quién habla y a quién habla.",
    ["Conozco las etapas de la independencia de Chile.", "Sé que una fuente tiene autor, fecha y propósito."],
    [
        "Para estudiar la independencia se usan fuentes de varios tipos. El acta de instalación de la Primera Junta (1810) muestra que, al comienzo, los criollos gobernaban en nombre del rey Fernando VII. El periódico Aurora de Chile (1812), editado por Camilo Henríquez, difundió ideas de libertad y de república. El Reglamento Constitucional de 1812 fue un primer ensayo de constitución. La Declaración de Independencia de 1818 proclamó que Chile era un Estado libre e independiente. También hay cartas, proclamas de generales y diarios de soldados.",
        "Cada fuente tiene su contexto. Un acta oficial muestra lo que las autoridades quisieron dejar por escrito. Un periódico patriota defiende una causa y puede omitir lo que no le conviene. Las proclamas buscan convencer o animar. Las fuentes realistas, es decir, de quienes defendían al rey, muestran la mirada contraria. Al comparar todas se obtiene una imagen más completa.",
        "También hay silencios. Hay pocas fuentes escritas por mujeres, por indígenas, por personas esclavizadas o por soldados comunes. Eso no significa que no participaran, sino que sus voces se registraron menos. Elegir fuentes variadas y reconocer los silencios es parte del trabajo del historiador.",
    ],
    [("acta", "documento que registra lo que se decidió en una reunión"), ("proclama", "texto o discurso para convocar o anunciar algo al público"), ("realista", "persona o grupo que defendía al rey de España durante la independencia"), ("patriota", "persona o grupo que defendía la independencia o el autogobierno"), ("silencio de las fuentes", "grupos o temas de los que casi no hay registros")],
    [
        ("Identificar la fuente", "Un texto de ejemplo dice: «Se instala la Junta; se jura lealtad al rey Fernando VII». ¿Qué tipo de fuente es y qué muestra?", ["Registra una decisión oficial.", "Es un acta y muestra lealtad al rey."], "Un acta; que la Junta gobernaba en nombre del rey"),
        ("Elegir la fuente", "Pregunta: ¿qué ideas se difundían en 1812? Opciones: periódico Aurora de Chile o lista de impuestos. ¿Cuál conviene?", ["El periódico difunde ideas.", "La lista de impuestos no."], "El periódico Aurora de Chile"),
    ],
    [
        ("Creer que una proclama muestra lo que pensaba todo el pueblo.", "Es un texto con propósito de convencer.", "Pregunta quién la escribió y para qué."),
        ("Creer que no participaron las personas de las que no hay registro.", "Participaron, pero hay pocas fuentes que lo muestren.", "Reconoce los silencios."),
    ],
    [
        ("¿Quién editó el periódico Aurora de Chile?", "Camilo Henríquez", "Se dice en el primer párrafo."),
        ("¿Qué proclamó la Declaración de 1818?", "Que Chile era un Estado libre e independiente", "Se dice en el primer párrafo."),
        ("¿Qué es una proclama?", "Un texto o discurso para convocar o anunciar algo al público", "Está en el vocabulario."),
    ],
    [
        ("¿Qué mostraba el acta de 1810?", "Que los criollos gobernaban en nombre del rey", "Se explicó en el primer párrafo."),
        ("¿Por qué un periódico patriota tiene límites como fuente?", "Porque defiende una causa y puede omitir lo que no le conviene", "Lo dice el segundo párrafo."),
        ("¿Qué grupos tienen pocas fuentes escritas?", "Mujeres, indígenas, personas esclavizadas y soldados comunes", "Se enumeran en el tercer párrafo."),
    ],
    [
        arith("El Reglamento Constitucional es de 1812 y la Declaración de Independencia se proclamó en 1818. ¿Cuántos años pasaron?", "1818-1812", "Se resta el año menor al mayor."),
        ("Pregunta: ¿cómo veían la independencia los realistas? Fuentes: 1 = carta de un oficial realista; 2 = periódico patriota; 3 = Declaración de 1818. ¿Cuál es la más adecuada?", "La 1", "La carta del oficial realista expresa esa mirada."),
        ("Una proclama de ejemplo dice: «¡Soldados, la patria os espera!». ¿Qué busca lograr?", "Animar y convocar a los soldados", "Una proclama convoca y motiva."),
    ],
    [
        ("Un estudiante concluye: «Como no hay textos de mujeres, ellas no participaron». ¿Qué error comete?", "Confunde silencio de las fuentes con ausencia; las mujeres participaron pero hay menos registros", "La ausencia de registro no prueba ausencia de participación."),
        ("¿Por qué conviene comparar una fuente patriota con una realista?", "Porque cada una da una versión distinta y se obtiene una imagen más completa", "Cada bando cuenta la historia a su manera."),
    ],
    [
        ("Ordena por fecha de más antigua a más reciente: A = Declaración de 1818, B = acta de la Primera Junta (1810), C = Aurora de Chile (1812).", "B, C, A", "Las fechas en orden son 1810, 1812 y 1818."),
        arith("Una biblioteca de ejemplo guarda 12 actas, 30 cartas y 8 periódicos de la época. ¿Cuántos documentos tiene?", "12+30+8", "Se suman los tres tipos."),
    ],
    [("Una carta de ejemplo de una vecina de Santiago en 1814 dice: «Mi hijo se fue con el ejército patriota y yo cuido la casa». ¿Qué grupo, con pocas fuentes, aparece en este texto?", "Las mujeres", "La autora es una mujer que cuenta su experiencia.")],
    [("¿Qué es un acta?", "Un documento que registra lo que se decidió en una reunión", "Está en el vocabulario."), ("¿Qué es el silencio de las fuentes?", "Que hay grupos de los que casi no hay registros", "Está en el vocabulario."), ("¿Qué primer ensayo de constitución hubo en 1812?", "El Reglamento Constitucional", "Se dice en el primer párrafo.")],
    (
        "Lee esta fuente de ejemplo: «Proclama del general, 1817: Soldados, cruzamos los Andes para liberar Chile». Escribe una tabla con cuatro filas: quién habla, a quién se dirige, qué quiere lograr, qué voz falta. Cierra con una frase sobre qué fuente adicional pedirías.",
        "Habla un general patriota a sus soldados. Quiere animarlos. Falta la voz de los soldados comunes y de los realistas. Pediría un diario de un soldado.",
        ["identifica autor y destinatario", "señala el propósito", "indica una voz que falta", "propone una fuente adicional"],
        ["tabla de cuatro filas y una frase"],
        ["tomar la proclama como relato neutro", "no pedir otra fuente"],
        "Pide a una persona de tu casa que lea la proclama y diga qué sintió.",
    ),
    "Escribe tres preguntas sobre la independencia y qué fuente usarías para cada una.",
    "Escribe en tres líneas por qué es importante buscar las voces que faltan.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a relacionar cambio, continuidad y territorio en la independencia: la crisis del sistema colonial, la opción republicana y cómo se desarrollaron las campañas en el espacio. Sirve para ver qué se transformó y qué siguió igual.",
    ["Conozco las etapas y las fuentes de la independencia.", "Sé ubicar los Andes, Santiago, Chacabuco y Maipú."],
    [
        "La independencia fue consecuencia de una crisis del sistema colonial. Desde el siglo XVIII, las reformas de los Borbones, como mayores impuestos y más control, molestaron a los criollos, que tenían pocos cargos importantes. A esto se sumaron las ideas ilustradas y los ejemplos de Estados Unidos y Francia. En 1808 la caída del rey de España desató la crisis. Tras la independencia, las colonias adoptaron mayoritariamente el modelo republicano y no la monarquía.",
        "Hubo cambios: se terminó el dominio político de España, se abolieron títulos de nobleza, se declaró la soberanía popular y, en Chile, se abolió la esclavitud en 1823. Y hubo continuidades: las élites criollas conservaron la tierra y el poder, los pueblos indígenas siguieron con pocos derechos y muchas desigualdades coloniales persistieron.",
        "El territorio fue clave. Para liberar Chile, San Martín organizó el Ejército de los Andes en Cuyo, cruzó la cordillera en 1817 y venció en Chacabuco. Después se formó una Escuadra Libertadora en Valparaíso, que permitió luego la expedición al Perú en 1820. En el norte de Sudamérica, Simón Bolívar lideró otros ejércitos. La geografía, con montañas, ríos y grandes distancias, condicionó las campañas.",
    ],
    [("crisis del sistema colonial", "pérdida de legitimidad y eficacia del dominio español en América"), ("modelo republicano", "organización del Estado sin rey, con cargos de plazo limitado y soberanía popular"), ("Escuadra Libertadora", "flota organizada por Chile en 1818 para apoyar la independencia en el Pacífico"), ("campaña", "serie de operaciones militares en un territorio"), ("reformas borbónicas", "cambios del siglo XVIII para controlar mejor las colonias y cobrar más impuestos")],
    [
        ("Reconocer un cambio", "Chile abolió la esclavitud en 1823. ¿Es un cambio o una continuidad respecto de la Colonia?", ["Antes existía la esclavitud.", "Se abolió."], "Un cambio"),
        ("Reconocer una continuidad", "Las élites criollas conservaron la tierra y el poder. ¿Es un cambio o una continuidad?", ["Ya tenían tierra y poder.", "Se mantuvo."], "Una continuidad"),
    ],
    [
        ("Pensar que la independencia cambió todo de inmediato.", "Hubo cambios políticos, pero muchas desigualdades siguieron.", "Busca cambios y continuidades."),
        ("Olvidar el territorio al explicar las campañas.", "Los Andes y las distancias condicionaron los ejércitos.", "Relaciona el relieve con las decisiones militares."),
    ],
    [
        ("¿Qué modelo de gobierno adoptaron mayoritariamente las colonias?", "El republicano", "Se dice en el primer párrafo."),
        ("¿En qué año se abolió la esclavitud en Chile?", "En 1823", "Se dice en el segundo párrafo."),
        ("¿Dónde organizó San Martín el Ejército de los Andes?", "En Cuyo", "Se dice en el tercer párrafo."),
    ],
    [
        ("¿Por qué las reformas borbónicas molestaron a los criollos?", "Por los mayores impuestos y el mayor control, con pocos cargos para ellos", "Lo explica el primer párrafo."),
        ("¿Qué permitió la Escuadra Libertadora?", "La expedición al Perú en 1820", "Se dice en el tercer párrafo."),
        ("¿Qué obstáculo natural tuvo que cruzar el Ejército de los Andes?", "La cordillera de los Andes", "Se dice en el tercer párrafo."),
    ],
    [
        arith("Un ejército de ejemplo sale de Cuyo con 4.000 soldados y 500 quedan en el camino. ¿Cuántos soldados llegan a Chile?", "4000-500", "Se restan los que quedan del total."),
        ("La esclavitud se abolió en Chile en 1823, cinco años después de la independencia proclamada. ¿En qué año se proclamó la independencia?", "En 1818", "1823 menos 5 años da 1818."),
        ("Un mapa de ejemplo marca las rutas del Ejército de los Andes desde Cuyo hasta Chacabuco. ¿Qué factor del territorio muestran las rutas?", "La necesidad de cruzar la cordillera", "Las rutas siguen pasos de la cordillera."),
    ],
    [
        ("Un estudiante dice: «Después de la independencia, los pueblos indígenas ganaron todos los derechos». ¿Qué continuidad ignora?", "Que siguieron con pocos derechos", "La clase señala esa continuidad."),
        ("¿Por qué las ideas ilustradas ayudaron a la independencia?", "Porque ofrecieron argumentos de soberanía popular, libertad y republicanismo", "Esas ideas justificaron el cambio."),
    ],
    [
        ("Ordena de causa a consecuencia: A = formación de juntas, B = crisis de 1808, C = proclamación de la independencia.", "B, A, C", "Primero la crisis, luego las juntas y después la independencia."),
        arith("Una escuadra de ejemplo tiene 6 barcos y se suman 4. ¿Cuántos barcos tiene?", "6+4", "Se suman los dos grupos."),
    ],
    [("Un mapa de ejemplo marca: «Cuyo → cordillera → Chacabuco → Santiago». ¿Qué orden de lugares siguió el Ejército de los Andes antes de llegar a Santiago?", "Cuyo, cordillera y Chacabuco", "Es el orden del mapa.")],
    [("¿Qué son las reformas borbónicas?", "Cambios del siglo XVIII para controlar mejor las colonias y cobrar más impuestos", "Está en el vocabulario."), ("¿Qué se abolió en Chile en 1823?", "La esclavitud", "Se explicó en el segundo párrafo."), ("¿Qué se mantuvo de la Colonia?", "El poder de las élites y las desigualdades", "Se explicó en el segundo párrafo.")],
    (
        "Completa una tabla con dos columnas, cambio y continuidad, y tres filas. En «cambio» escribe tres hechos de la clase. En «continuidad» escribe tres hechos. Termina con una frase que explique el papel del territorio en las campañas.",
        "Cambio: fin del dominio español; república; abolición de la esclavitud en Chile. Continuidad: poder de las élites; pocos derechos indígenas; desigualdades coloniales. El relieve de los Andes condicionó las campañas.",
        ["completa las dos columnas con hechos de la clase", "explica el papel del territorio"],
        ["tabla de tres filas y una frase"],
        ["decir que todo cambió", "olvidar el territorio"],
        "Explica a una persona de tu casa qué cambió y qué continuó.",
    ),
    "Dibuja un mapa con la ruta del Ejército de los Andes y rotula tres lugares.",
    "Escribe una pregunta sobre cómo vivieron el cambio los campesinos.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a contrastar actores, causas y perspectivas de la independencia de Chile: patriotas, realistas, mujeres, grupos populares y comunidades indígenas. Sirve para entender que el proceso tuvo conflictos internos.",
    ["Conozco las etapas y el territorio de la independencia.", "Sé que cada grupo tiene una perspectiva."],
    [
        "En Chile hubo dos grandes bandos: los patriotas, que querían autogobierno o independencia, y los realistas, que defendían al rey y la unidad con España. Entre los patriotas había también diferencias. José Miguel Carrera y Bernardo O'Higgins fueron figuras importantes, pero rivales: sus seguidores se llamaron carrerinos y o'higginistas. Esas disputas debilitaron al bando patriota, sobre todo antes de la derrota de Rancagua en 1814.",
        "Participaron muchos otros actores. Mujeres como Javiera Carrera apoyaron la causa patriota. Los grupos populares, como campesinos y artesanos, integraron los ejércitos de ambos bandos, a veces por obligación. Algunas comunidades mapuches se alinearon con uno u otro bando según sus intereses. Las personas esclavizadas fueron reclutadas o buscaron su libertad, y la abolición de la esclavitud en 1823 fue un paso importante.",
        "Cada actor tuvo causas distintas. Los criollos querían participación política y comercio libre. Los realistas defendían el orden, su fidelidad al rey y sus intereses. Los grupos populares buscaban sobrevivir, tierra o libertad. Contrastar sus perspectivas muestra que la independencia no fue un bloque único: fue un proceso con conflictos, intereses y decisiones diversas.",
    ],
    [("carrerino", "seguidor de José Miguel Carrera durante la independencia de Chile"), ("o'higginista", "seguidor de Bernardo O'Higgins"), ("reclutamiento", "incorporación de personas a un ejército, a veces por obligación"), ("rivalidad", "competencia entre dos personas o grupos que buscan el liderazgo"), ("alineación", "decisión de un grupo de apoyar a uno de los bandos")],
    [
        ("Distinguir bandos", "Una persona de ejemplo defiende al rey y la unidad con España. ¿Es patriota o realista?", ["Defiende al rey.", "Eso es realista."], "Realista"),
        ("Contrastar causas", "Un criollo quiere comercio libre y participación política; un oficial realista defiende al rey. ¿Qué muestra el contraste?", ["Cada uno defiende un interés distinto.", "Por eso apoyan bandos opuestos."], "Que cada grupo tenía intereses y causas distintas"),
    ],
    [
        ("Creer que los patriotas eran un solo grupo unido.", "Había rivalidades, como la de Carrera y O'Higgins.", "Muestra las disputas internas."),
        ("Pensar que todos los grupos populares apoyaban a los patriotas.", "Muchos estaban en ambos ejércitos, a veces por reclutamiento.", "Distingue obligación y convicción."),
    ],
    [
        ("¿Qué querían los patriotas?", "Autogobierno o independencia", "Se dice en el primer párrafo."),
        ("¿Qué defendían los realistas?", "Al rey y la unidad con España", "Se dice en el primer párrafo."),
        ("¿Qué rivalidad debilitó a los patriotas?", "La de Carrera y O'Higgins", "Se dice en el primer párrafo."),
    ],
    [
        ("¿Quiénes son los carrerinos?", "Los seguidores de José Miguel Carrera", "Está en el vocabulario."),
        ("¿Qué papel tuvieron los grupos populares?", "Integraron los ejércitos de ambos bandos, a veces por obligación", "Se explicó en el segundo párrafo."),
        ("¿Por qué algunas comunidades mapuches se alinearon con un bando?", "Según sus propios intereses", "Se dice en el segundo párrafo."),
    ],
    [
        arith("Un regimiento de ejemplo tiene 300 soldados; 120 fueron reclutados a la fuerza. ¿Cuántos eran voluntarios?", "300-120", "Se restan los reclutados del total."),
        ("Fuente 1 (patriota): «Luchamos por la libertad». Fuente 2 (realista): «Defendemos al rey legítimo». ¿Qué tienen en común ambos textos?", "Que cada uno justifica su causa con un valor", "Ambos defienden su bando con argumentos."),
        ("Una mujer de ejemplo organiza ayuda para soldados patriotas desde su casa. ¿Qué actor representa?", "Las mujeres que apoyaron la causa patriota", "La clase menciona a mujeres como Javiera Carrera."),
    ],
    [
        ("Un estudiante dice: «La derrota de Rancagua se debió solo a la fuerza realista». ¿Qué otra causa de la clase omite?", "Las disputas internas entre los patriotas", "La rivalidad Carrera-O'Higgins debilitó al bando patriota."),
        ("¿Por qué conviene leer fuentes patriotas y realistas?", "Porque se contrastan versiones y no se repite un relato único", "Cada bando cuenta los hechos a su manera."),
    ],
    [
        ("Ordena por fecha de más antigua a más reciente: A = abolición de la esclavitud en Chile (1823), B = derrota de Rancagua (1814), C = Primera Junta (1810).", "C, B, A", "Las fechas en orden son 1810, 1814 y 1823."),
        arith("En una votación de ejemplo, 45 votan por O'Higgins y 35 por Carrera. ¿Cuántas personas votaron?", "45+35", "Se suman los dos grupos."),
    ],
    [("Una carta de ejemplo de un soldado de 1815 dice: «Me reclutaron sin preguntarme; no sé por qué peleamos». ¿Qué grupo y qué perspectiva muestra?", "Un soldado reclutado; la perspectiva de quien no eligió", "Habla de reclutamiento obligatorio.")],
    [("¿Qué es la rivalidad?", "La competencia entre dos personas o grupos que buscan el liderazgo", "Está en el vocabulario."), ("¿Quién fue Javiera Carrera según la clase?", "Una mujer que apoyó la causa patriota", "Se explicó en el segundo párrafo."), ("¿Qué paso importante ocurrió en 1823?", "La abolición de la esclavitud", "Se dice en la clase 3.")],
    (
        "Escribe una tabla con cuatro actores: criollo patriota, oficial realista, campesino reclutado y mujer que apoya a los patriotas. Para cada uno anota qué buscaba y qué podía perder. Termina con una frase que diga por qué sus perspectivas diferían.",
        "Criollo patriota: participación y comercio libre; podía perder bienes. Oficial realista: defender al rey; podía perder cargos. Campesino reclutado: sobrevivir; podía perder la vida. Mujer: apoyar la causa; podía perder seguridad. Diferían por sus intereses.",
        ["incluye los cuatro actores", "indica qué buscaba y qué podía perder", "explica la diferencia de perspectivas"],
        ["tabla de cuatro filas y una frase"],
        ["tratar a todos igual", "olvidar a los reclutados"],
        "Conversa con una persona de tu casa sobre qué bando habrías apoyado y por qué.",
    ),
    "Escribe un diálogo de seis líneas entre un patriota y un realista.",
    "Escribe una pregunta sobre cómo vivían los niños durante las guerras de independencia.",
)

# ================================================================ clase 5
lesson(
    OA, 5,
    "Aprenderé a construir un argumento con evidencia sobre la independencia como proceso continental, con la crisis colonial, las ideas ilustradas y la opción republicana. Sirve para responder la pregunta central de la unidad.",
    ["Conozco las causas, actores y el territorio de la independencia.", "Sé que un argumento tiene afirmación, evidencia y límite."],
    [
        "Un argumento posible es: «La independencia hispanoamericana fue un proceso continental causado por la crisis del sistema colonial, que adoptó ideas ilustradas y optó por el modelo republicano». La evidencia puede ser el hecho de que en 1808 cayó el rey, de que se formaron juntas casi en todas partes entre 1809 y 1811, y de que las nuevas naciones adoptaron constituciones y repúblicas.",
        "Para Chile, la evidencia incluye la Primera Junta (1810), el Reglamento Constitucional de 1812, la batalla de Chacabuco (1817), la Declaración de Independencia de 1818 y la abolición de la esclavitud en 1823. Para el continente, se puede mencionar la acción de Simón Bolívar en el norte y de San Martín en el sur, que se coordinó en parte en la campaña del Perú.",
        "El límite es que el argumento no explica toda la diversidad de experiencias. No todos los grupos apoyaron la independencia, muchos indígenas y esclavizados no recibieron beneficios inmediatos, y las élites criollas conservaron el poder. También hay que declarar si se usó solo documentos oficiales. Un buen argumento incluye evidencia y límites.",
    ],
    [("proceso continental", "proceso que ocurre en gran parte de un continente, con rasgos comunes y diferencias locales"), ("opción republicana", "decisión de organizar el Estado como república y no como monarquía"), ("campaña del Perú", "operación militar de 1820 para liberar el Perú, apoyada por una escuadra chilena"), ("afirmación", "respuesta que se defiende ante una pregunta"), ("límite", "aquello que la evidencia no permite concluir")],
    [
        ("Separar afirmación y evidencia", "«En 1808 cayó el rey de España». ¿Es una afirmación general o una evidencia concreta?", ["Es un hecho con fecha.", "Es una evidencia."], "Una evidencia concreta"),
        ("Formular un límite", "Con los documentos oficiales de una junta, ¿qué no se puede saber?", ["Son documentos de autoridades.", "No muestran lo que pensaban los grupos populares."], "Qué pensaban y vivían los grupos populares"),
    ],
    [
        ("Dar solo la afirmación sin evidencia.", "Sin datos es solo opinión.", "Cita fechas, textos o hechos."),
        ("Decir que todos se beneficiaron con la independencia.", "Muchos grupos no recibieron beneficios inmediatos.", "Incluye el límite."),
    ],
    [
        ("¿Qué es una opción republicana?", "La decisión de organizar el Estado como república y no como monarquía", "Está en el vocabulario."),
        ("¿Qué hecho de 1808 fue evidencia de la crisis colonial?", "La caída del rey de España", "Se dice en el primer párrafo."),
        ("¿Quién lideró la acción en el norte de Sudamérica?", "Simón Bolívar", "Se dice en el segundo párrafo."),
    ],
    [
        ("Nombra dos evidencias chilenas de la independencia.", "La Primera Junta, Chacabuco, la Declaración de 1818 o la abolición de la esclavitud", "Se enumeran en el segundo párrafo."),
        ("¿Qué límite tiene el argumento de la clase?", "No explica toda la diversidad de experiencias y no todos los grupos se beneficiaron", "Se dice en el tercer párrafo."),
        ("¿Por qué se dice «proceso continental»?", "Porque ocurrió en casi toda América hispana", "Está en el vocabulario."),
    ],
    [
        ("Se formaron juntas en 1809 en Quito y en 1810 en Caracas, Buenos Aires, Bogotá y Santiago. ¿Qué ciudad formó su junta antes que las demás?", "Quito", "Su junta es de 1809, un año antes que las otras."),
        ("Elige la mejor evidencia para «la independencia adoptó el modelo republicano»: 1 = constituciones de las nuevas naciones; 2 = un cuadro de paisaje; 3 = una carta de amor.", "La 1", "Las constituciones muestran la forma de gobierno."),
        ("Una afirmación de ejemplo dice: «La independencia benefició a todos por igual». ¿Qué evidencia de la clase la contradice?", "Que los pueblos indígenas y esclavizados no recibieron beneficios inmediatos", "La clase lo señala."),
    ],
    [
        ("Un estudiante concluye: «Como San Martín cruzó los Andes, Chile se liberó solo con ayuda externa». ¿Qué error comete?", "Ignora que hubo también patriotas chilenos, O'Higgins y la Escuadra Libertadora organizada en Chile", "El proceso involucró a chilenos y extranjeros."),
        ("¿Por qué conviene incluir el límite en el argumento?", "Porque muestra qué no prueba la evidencia y evita exagerar", "Un límite aporta honestidad."),
    ],
    [
        ("Ordena las partes de un argumento: A = límite, B = afirmación, C = evidencia.", "B, C, A", "Primero se afirma, luego se prueba y al final se declara el límite."),
        arith("Un registro de ejemplo anota 50 documentos oficiales y 20 cartas privadas sobre la independencia. ¿Cuántos documentos hay?", "50+20", "Se suman los dos grupos."),
    ],
    [("Datos de ejemplo: «Entre 1810 y 1818 se escribieron 3 actas de junta, 2 proclamas de generales y 5 cartas de soldados». ¿Cuántas fuentes escribieron autoridades y cuántas soldados?", "5 de autoridades (actas y proclamas) y 5 de soldados", "3 actas + 2 proclamas = 5 de autoridades; las cartas de soldados son 5. Los datos muestran cantidad, no representatividad.")],
    [("¿Qué es una afirmación?", "La respuesta que se defiende ante una pregunta", "Está en el vocabulario."), ("¿Qué año fue clave para la crisis colonial?", "1808", "Se explicó en la clase."), ("¿Qué modelo adoptaron las nuevas naciones?", "El republicano", "Se explicó en la clase 3.")],
    (
        "Responde en cinco líneas: «¿Por qué la independencia de Chile fue parte de un proceso continental?». Usa esta evidencia de ejemplo: caída del rey en 1808; juntas en varias ciudades; ideas ilustradas; Primera Junta (1810) y Declaración (1818). Incluye afirmación, dos datos y un límite.",
        "La independencia de Chile fue parte de un proceso continental porque nació de la crisis de 1808 y de las ideas ilustradas. Datos: juntas en varias ciudades y la Primera Junta (1810). Límite: no explica la experiencia de todos los grupos.",
        ["escribe una afirmación clara", "usa dos datos", "incluye un límite"],
        ["texto de cinco líneas"],
        ["no incluir límite", "decir que la independencia fue solo chilena"],
        "Lee tu texto a una persona de tu casa y pídele que diga cuál es tu afirmación.",
    ),
    "Dibuja un mapa de Sudamérica con San Martín y Bolívar y sus rutas.",
    "Escribe una frase que explique qué significa «proceso continental».",
)

# ================================================================ clase 6
lesson(
    OA, 6,
    "Aprenderé a evaluar proyecciones y límites de la independencia: la organización de la república en Chile, los problemas de la época y el legado. Sirve para valorar el proceso sin idealizarlo.",
    ["Conozco las causas, actores y evidencias de la independencia.", "Sé construir un argumento con afirmación, evidencia y límite."],
    [
        "Después de la independencia vino el difícil desafío de organizar la república. En Chile, Bernardo O'Higgins gobernó como Director Supremo hasta 1823, cuando abdicó por la presión de distintos grupos. Siguió un período de ensayos constitucionales, con varias constituciones y cambios de gobierno. En 1830 una guerra civil terminó con la victoria de los conservadores en Lircay, y en 1833 se aprobó una constitución que dio estabilidad por casi un siglo.",
        "El proceso dejó legados: un Estado independiente, instituciones republicanas, la abolición de la esclavitud en 1823 y una identidad nacional en formación. Pero también tuvo límites. Los pueblos indígenas quedaron con pocos derechos; en el sur, la llamada Guerra a Muerte, iniciada en 1819, fue un conflicto muy violento entre realistas y patriotas, con participación de población local. Las élites siguieron concentrando el poder y la tierra.",
        "Evaluar es separar el legado de la idealización. Se puede afirmar que la independencia cambió quién gobernaba. No se puede afirmar que mejorara de inmediato la vida de todos. Además, las fuentes oficiales muestran sobre todo el punto de vista de los líderes. Declarar esos límites hace más fuerte la conclusión.",
    ],
    [("Director Supremo", "título del jefe del gobierno de Chile entre 1817 y 1823"), ("abdicar", "renunciar al cargo de gobierno"), ("ensayos constitucionales", "intentos de organizar la república con distintas constituciones"), ("legado", "lo que una época deja a las siguientes"), ("identidad nacional", "sentimiento de pertenecer a una misma nación")],
    [
        ("Reconocer un legado", "¿Qué institución se abolió en Chile en 1823?", ["Fue un cambio social importante.", "Fue la esclavitud."], "La esclavitud"),
        ("Reconocer un límite", "¿Quiénes quedaron con pocos derechos después de la independencia, según la clase?", ["Un grupo con muchos años de exclusión.", "Los pueblos indígenas."], "Los pueblos indígenas"),
    ],
    [
        ("Pensar que la república se organizó de inmediato.", "Hubo años de ensayos, guerras y cambios hasta 1833.", "Revisa la secuencia."),
        ("Idealizar la independencia.", "Hubo violencia, exclusiones y desigualdades.", "Incluye legado y límites."),
    ],
    [
        ("¿Qué título tuvo O'Higgins en el gobierno?", "Director Supremo", "Está en el vocabulario."),
        ("¿En qué año abdicó O'Higgins?", "En 1823", "Se dice en el primer párrafo."),
        ("¿En qué año se aprobó la constitución que dio estabilidad por casi un siglo?", "En 1833", "Se dice en el primer párrafo."),
    ],
    [
        ("¿Qué fue la Guerra a Muerte?", "Un conflicto muy violento en el sur entre realistas y patriotas", "Se explicó en el segundo párrafo."),
        ("Nombra dos legados de la independencia.", "Un Estado independiente, instituciones republicanas, abolición de la esclavitud o identidad nacional", "Se enumeran en el segundo párrafo."),
        ("¿Por qué no se puede afirmar que mejoró la vida de todos?", "Porque muchos grupos siguieron con pocos derechos y desigualdades", "Lo dice el tercer párrafo."),
    ],
    [
        arith("O'Higgins fue Director Supremo desde 1817 hasta 1823. ¿Cuántos años gobernó?", "1823-1817", "Se resta el año de inicio al de término."),
        arith("Entre la abdicación de O'Higgins (1823) y la constitución de 1833, ¿cuántos años pasaron?", "1833-1823", "Se resta el año menor al mayor."),
        ("Una afirmación de ejemplo dice: «La independencia terminó con toda desigualdad». ¿Qué evidencia de la clase la contradice?", "Que las élites siguieron concentrando el poder y la tierra y los indígenas tenían pocos derechos", "La clase muestra continuidades."),
    ],
    [
        ("Un estudiante dice: «La Guerra a Muerte fue un episodio menor». ¿Qué corrige la clase?", "Fue un conflicto muy violento en el sur con participación de población local", "La clase subraya su violencia."),
        ("¿Por qué las fuentes oficiales tienen límites?", "Porque muestran sobre todo el punto de vista de los líderes", "Lo dice el tercer párrafo."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A = Constitución de 1833, B = abdicación de O'Higgins (1823), C = batalla de Lircay (1830).", "B, C, A", "Las fechas en orden son 1823, 1830 y 1833."),
        arith("Un presupuesto de ejemplo tiene 5.000 pesos para escuelas y 3.000 para el ejército. ¿Cuántos pesos son en total?", "5000+3000", "Se suman las dos partidas."),
    ],
    [("Un texto de ejemplo dice: «Mi tatarabuelo luchó por la libertad, pero siguió trabajando para un patrón». ¿Qué continuidad de la independencia ilustra?", "Que las desigualdades coloniales persistieron", "El trabajador seguía sometido a un patrón.")],
    [("¿Qué es el legado?", "Lo que una época deja a las siguientes", "Está en el vocabulario."), ("¿Qué son los ensayos constitucionales?", "Intentos de organizar la república con distintas constituciones", "Está en el vocabulario."), ("¿Qué hay que evitar al evaluar la independencia?", "Idealizarla o rechazarla por completo", "Se explicó en el tercer párrafo.")],
    (
        "Escribe un párrafo de seis líneas: «Qué cambió y qué no con la independencia de Chile». Incluye dos legados, dos límites y una pregunta que no puedes responder con las fuentes de la unidad.",
        "Legados: Estado independiente y abolición de la esclavitud en 1823. Límites: pueblos indígenas con pocos derechos y élites con el poder. Pregunta: ¿cómo vivían los campesinos después de 1818?",
        ["incluye dos legados", "incluye dos límites", "formula una pregunta honesta"],
        ["párrafo de seis líneas"],
        ["idealizar la independencia", "olvidar a los excluidos"],
        "Lee el párrafo a una persona de tu casa y pídele que diga qué legado le parece más importante.",
    ),
    "Escribe tres frases con las palabras legado, límite y proyección.",
    "Escribe qué símbolo patrio conoces y qué pregunta tendrías sobre su origen.",
)
