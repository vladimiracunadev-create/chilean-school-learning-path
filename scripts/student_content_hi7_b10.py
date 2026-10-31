"""Cuaderno del estudiante, 7.º básico Historia, Geografía y Ciencias Sociales: OA 20 (convivencia y conflicto entre culturas)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI07 OA 20"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a reconocer las formas de contacto entre culturas en las civilizaciones estudiadas. Sirve para ver que los encuentros pueden ser pacíficos, violentos o ambas cosas.",
    ["Conozco las civilizaciones mesoamericanas, andinas, grecorromanas, medievales e islámicas.", "Sé que un hecho puede tener varias causas."],
    [
        "Cuando dos culturas entran en contacto pueden relacionarse de muchas formas. El comercio es el intercambio de productos. La alianza es un pacto entre pueblos, a veces sellado con matrimonios entre familias de gobernantes, como entre ciudades mayas. La migración es el desplazamiento de personas a otro lugar, como los pueblos germanos que se instalaron dentro del Imperio romano. La guerra y la conquista son enfrentamientos armados para dominar. La conversión religiosa es el cambio de creencias, a veces voluntario y a veces forzado.",
        "Estas formas pueden mezclarse. Roma comerció con pueblos germanos, los empleó como soldados y también los combatió. Los incas combinaron negociación, alianzas y ejército para integrar pueblos. Los mexicas recibían tributo de pueblos conquistados y mantenían alianzas, como la Triple Alianza. En Al-Ándalus hubo comercio, tratados y guerras entre reinos cristianos y musulmanes.",
        "Para clasificar un caso se pregunta qué hacen los grupos: ¿intercambian, se unen, se desplazan, se enfrentan o imponen creencias? Un mismo caso puede mostrar más de una forma. No se debe reducir todo contacto a conflicto ni todo a convivencia pacífica.",
    ],
    [("contacto", "relación entre grupos de culturas distintas"), ("alianza", "pacto entre pueblos para actuar juntos"), ("migración", "desplazamiento de personas a otro territorio"), ("conquista", "dominio de un territorio por la fuerza"), ("conversión", "cambio de creencias religiosas"), ("tributo", "pago exigido a un pueblo dominado")],
    [
        ("Clasificar un caso", "Dos ciudades mayas de ejemplo sellan un pacto con el matrimonio de dos jóvenes de familias gobernantes. ¿Qué forma de contacto es?", ["Es un pacto entre pueblos.", "Es una alianza."], "Alianza"),
        ("Clasificar otro caso", "Familias de un pueblo germano se instalan dentro del Imperio romano. ¿Qué forma de contacto es?", ["Se desplazan de lugar.", "Es migración."], "Migración"),
    ],
    [
        ("Creer que contacto significa siempre conflicto.", "El comercio, la alianza y la migración son formas de contacto pacíficas.", "Clasifica con las cinco formas."),
        ("Creer que cada caso muestra una sola forma.", "Roma comerció con los germanos, los empleó como soldados y los combatió.", "Revisa si hay más de una forma."),
    ],
    [
        ("¿Cómo se llama el pago exigido a un pueblo dominado?", "Tributo", "Es la definición del vocabulario."),
        ("¿Cómo se llama el desplazamiento de personas a otro territorio?", "Migración", "Es la definición del vocabulario."),
        ("¿Cómo se llama el cambio de creencias religiosas?", "Conversión", "Es la definición del vocabulario."),
    ],
    [
        ("Nombra dos formas pacíficas de contacto de la clase.", "Dos de estas: comercio, alianza, migración", "No implican enfrentamiento armado."),
        ("¿Qué forma de contacto implica dominar por la fuerza?", "La conquista", "Es la definición del vocabulario."),
        ("¿Qué alianza de la clase unió a Tenochtitlan, Texcoco y Tlacopan?", "La Triple Alianza", "Se menciona en la explicación."),
    ],
    [
        ("Una ficha de ejemplo dice: «Mercaderes de dos ciudades intercambian telas y cerámica cada año». ¿Qué forma de contacto es?", "Comercio", "Intercambian productos entre sí."),
        ("Otra ficha dice: «Un ejército entra a un valle y obliga a pagar tributo». ¿Qué forma de contacto es?", "Conquista", "Domina por la fuerza."),
        ("Un caso de ejemplo muestra comercio, alianza y una guerra con un mismo pueblo. ¿Cuántas formas de contacto aparecen?", "Tres", "Comercio, alianza y guerra son tres."),
    ],
    [
        ("Julia dice: «Roma y los pueblos germanos solo tuvieron guerras». ¿Qué dato de la clase la corrige?", "También comerciaron y los germanos fueron empleados como soldados", "Hubo varias formas de contacto."),
        ("Pedro dice: «Cuando los incas integraron pueblos nunca usaron la negociación». ¿Qué corrección haces?", "Combinaron negociación, alianzas y ejército", "La clase menciona las tres."),
    ],
    [
        ("¿Cuál de estas formas de contacto es la más violenta: comercio, alianza o conquista?", "La conquista", "Implica dominar por la fuerza, mientras las otras son pactos o intercambios."),
        ("Un pueblo de ejemplo comercia con una ciudad, la ayuda a defenderse y luego le exige tributo por la fuerza. ¿Qué tres formas de contacto aparecen?", "Comercio, alianza y conquista", "Intercambia, coopera y domina."),
    ],
    [("Un estudiante lee: «En Al-Ándalus hubo comercio, tratados y guerras entre reinos cristianos y musulmanes». ¿Qué conclusión limitada puede escribir?", "Que el contacto incluyó formas pacíficas y violentas", "No reduce todo a conflicto ni a paz.")],
    [("En la unidad de convivencia y conflicto, ¿qué es una alianza?", "Un pacto entre pueblos para actuar juntos", "Es la definición del vocabulario."), ("En la unidad de convivencia y conflicto, ¿qué es una conquista?", "El dominio de un territorio por la fuerza", "Es la definición del vocabulario."), ("¿Por qué un caso puede mostrar varias formas?", "Porque los grupos se relacionan de muchas maneras a la vez o en distintas épocas", "Roma y los incas son ejemplos.")],
    (
        "Describe estos tres casos de la unidad: Roma y los germanos, los incas y otros pueblos, y Al-Ándalus. Para cada uno, escribe una línea con las formas de contacto que reconoces y un dato de la clase que lo muestra. Termina con una frase sobre por qué no conviene decir «solo conflicto».",
        "Roma y germanos: comercio, migración y guerra; los germanos fueron soldados romanos. No conviene decir solo conflicto porque hubo comercio.",
        ["tres casos", "formas de contacto correctas", "un dato por caso", "frase de cierre"],
        ["tres líneas y una frase final"],
        ["reducir todo a conflicto", "no usar datos"],
        "Léele tus tres líneas a una persona de tu casa y pídele que repita una forma de contacto.",
    ),
    "Anota un ejemplo de contacto entre culturas que conozcas hoy en Chile.",
    "Averigua qué pueblos germanos se instalaron en el Imperio romano y cuándo.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a comparar casos de cooperación, intercambio y conflicto. Sirve para ver cómo cambia la relación entre culturas con el tiempo y con los intereses.",
    ["Conozco las formas de contacto.", "Sé que una fuente tiene perspectiva."],
    [
        "La cooperación es trabajar juntos con un objetivo común, como una alianza militar o un taller de traducción. El intercambio es el paso de productos, ideas o personas entre grupos, como el comercio de cacao entre mayas y aztecas. El conflicto es un enfrentamiento por recursos, poder o creencias. Una relación puede cambiar de una a otra: un pueblo aliado puede volverse rival.",
        "Algunos casos: los tlaxcaltecas fueron enemigos de los mexicas y luego se aliaron con los españoles en 1519. Los reinos cristianos y musulmanes de la península ibérica comerciaron, pagaron parias y también guerrearon. Los incas integraron a algunos pueblos mediante alianzas y regalos, y sometieron por la fuerza a otros. Roma y las ciudades griegas cooperaron en el comercio y compitieron por el poder.",
        "Al comparar casos se usan criterios: quiénes participan, qué buscan, qué ganan o pierden, y cuánto dura la relación. Es importante no tratar a una cultura como un bloque: dentro de un mismo pueblo puede haber grupos que cooperan y otros que se oponen.",
    ],
    [("cooperación", "trabajo conjunto con un objetivo común"), ("intercambio", "paso de productos, ideas o personas entre grupos"), ("conflicto", "enfrentamiento por recursos, poder o creencias"), ("rival", "grupo que compite con otro"), ("criterio", "aspecto que se usa para comparar"), ("interés", "aquello que un grupo quiere conseguir o proteger")],
    [
        ("Clasificar", "Traductores de dos culturas trabajan juntos en un mismo taller. ¿Es cooperación, intercambio o conflicto?", ["Trabajan con un objetivo común.", "Es cooperación."], "Cooperación"),
        ("Clasificar otro caso", "Dos pueblos pelean por el control de una fuente de agua. ¿Es cooperación, intercambio o conflicto?", ["Hay enfrentamiento por un recurso.", "Es conflicto."], "Conflicto"),
    ],
    [
        ("Tratar a una cultura como un bloque.", "Dentro de un pueblo hay grupos con intereses distintos.", "Pregunta qué grupo coopera y cuál se opone."),
        ("Creer que una relación nunca cambia.", "Un aliado puede volverse rival y un rival, aliado.", "Fecha cada etapa."),
    ],
    [
        ("¿Cómo se llama el trabajo conjunto con un objetivo común?", "Cooperación", "Es la definición del vocabulario."),
        ("¿Cómo se llama el paso de productos, ideas o personas entre grupos?", "Intercambio", "Es la definición del vocabulario."),
        ("¿Quiénes se aliaron con los españoles en 1519 tras ser enemigos de los mexicas?", "Los tlaxcaltecas", "Así lo dice la explicación."),
    ],
    [
        ("¿Qué pagaban a veces los reinos musulmanes a los reinos cristianos a cambio de paz?", "Parias", "Eran tributos a cambio de no ser atacados."),
        ("Nombra dos criterios para comparar casos.", "Dos de estos: quiénes participan, qué buscan, qué ganan o pierden, cuánto dura", "Son los criterios de la explicación."),
        ("¿Por qué no se debe tratar a una cultura como un bloque?", "Porque dentro de ella hay grupos con intereses distintos", "Hay diversidad interna."),
    ],
    [
        ("Un caso de ejemplo: dos ciudades comercian durante 50 años y luego se enfrentan por una ruta. ¿Qué cambió en la relación?", "Pasó de intercambio a conflicto", "El interés por la ruta cambió el vínculo."),
        ("Un pueblo A, de ejemplo, se alía con B para defenderse de C. ¿Qué forma de contacto muestra entre A y B, y qué entre A y C?", "Cooperación con B y conflicto con C", "Se une a unos y se enfrenta a otros."),
        arith("Un caso de ejemplo: la alianza duró de 1519 a 1521. ¿Cuántos años duró?", "1521-1519", "Se resta el año de inicio al de término.", " años"),
    ],
    [
        ("Ana dice: «Los tlaxcaltecas traicionaron a los mexicas». ¿Qué precisión de la clase haces?", "Eran enemigos de los mexicas desde antes, así que su alianza respondía a sus propios intereses", "No hay traición si ya eran rivales."),
        ("Pedro dice: «Cada cultura actuó como un bloque». ¿Qué dato lo contradice?", "Dentro de un mismo pueblo hubo grupos que cooperaron y otros que se opusieron", "Hubo diversidad interna."),
    ],
    [
        ("Da un ejemplo de la clase de un mismo par de grupos que tuvo intercambio y conflicto.", "Los reinos cristianos y musulmanes de la península ibérica", "Comerciaron, pagaron parias y guerrearon."),
        ("Una tabla de ejemplo tiene tres casos y tres criterios. ¿Cuántas casillas debe completar?", "9", "3 por 3 son 9."),
    ],
    [("Un estudiante lee: «Los reinos de la península ibérica comerciaron, pagaron parias y guerrearon». ¿Qué dos formas de relación de la clase (cooperación, intercambio o conflicto) aparecen en esa frase?", "Intercambio (comercio) y conflicto (guerras)", "Comerciar es intercambio y guerrear es conflicto.")],
    [("En la unidad de convivencia y conflicto, ¿qué es la cooperación?", "El trabajo conjunto con un objetivo común", "Es la definición del vocabulario."), ("En la unidad de convivencia y conflicto, ¿qué es un conflicto?", "Un enfrentamiento por recursos, poder o creencias", "Es la definición del vocabulario."), ("¿Qué criterios sirven para comparar?", "Quiénes participan, qué buscan, qué ganan y cuánto dura", "Son los criterios de la clase.")],
    (
        "Completa una tabla con tres casos (tlaxcaltecas y mexicas, reinos de la península ibérica, incas y otros pueblos) y los criterios: quiénes participan, qué buscan, qué forma de relación hay. Escribe luego tres líneas con una semejanza y una diferencia entre dos casos.",
        "Tlaxcaltecas: rivales de los mexicas, buscan autonomía, conflicto y luego alianza con otros. Semejanza: ambos casos cambian con el tiempo.",
        ["completa nueve casillas", "datos correctos", "una semejanza", "una diferencia"],
        ["tabla de nueve casillas y tres líneas"],
        ["tratar a una cultura como un bloque", "inventar datos"],
        "Muestra tu tabla a una persona de tu casa y pídele que elija el caso que más cambió.",
    ),
    "Anota un ejemplo actual de cooperación y uno de conflicto entre grupos de tu entorno.",
    "Averigua qué pueblos aliados ayudaron a los españoles en la toma de Tenochtitlan.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a examinar el poder, la resistencia y la negociación entre culturas. Sirve para ver quién tenía más fuerza y cómo respondieron los demás.",
    ["Conozco formas de contacto, cooperación y conflicto.", "Sé que un pueblo dominado puede actuar."],
    [
        "El poder es la capacidad de un grupo para imponer decisiones o conseguir lo que quiere. En un contacto entre culturas, el poder puede ser desigual: un grupo puede tener más ejército, más recursos o más organización. La resistencia es la oposición del grupo con menos poder, ya sea con armas o manteniendo su lengua y costumbres. La negociación es el diálogo para llegar a un acuerdo que ambos acepten.",
        "Ejemplos de la historia: en el año 9 d.C., guerreros germanos liderados por Arminio derrotaron a tres legiones romanas en el bosque de Teutoburgo y frenaron la expansión de Roma hacia el río Elba. Los chachapoyas resistieron a los incas, y los mapuche detuvieron su avance al sur del Maule. En cambio, otros pueblos negociaron: algunos curacas aceptaron integrarse al Tawantinsuyu a cambio de conservar parte de su poder.",
        "Las fuentes de estos casos suelen venir del grupo con más poder. Por eso conviene buscar también la voz del grupo que resistió o negoció, por ejemplo a través de la arqueología o de comunidades actuales. Y hay que evitar el error de pensar que quien resistió «perdió su tiempo» o que quien negoció «traicionó». Cada decisión respondió a un contexto.",
    ],
    [("poder", "capacidad de un grupo para imponer decisiones o conseguir lo que quiere"), ("resistencia", "oposición de un grupo con menos poder"), ("negociación", "diálogo para llegar a un acuerdo"), ("legión", "unidad del ejército romano"), ("avance", "expansión de un grupo sobre un territorio"), ("contexto", "circunstancias de tiempo y lugar de un hecho")],
    [
        ("Clasificar", "Un curaca acepta integrarse al Tawantinsuyu a cambio de conservar parte de su poder local. ¿Es resistencia o negociación?", ["Llega a un acuerdo.", "Es negociación."], "Negociación"),
        ("Clasificar otro caso", "Los germanos de Arminio derrotan a tres legiones romanas en el año 9 d.C. ¿Es resistencia o negociación?", ["Se oponen con armas.", "Es resistencia."], "Resistencia"),
    ],
    [
        ("Pensar que quien negoció traicionó a su pueblo.", "Muchos buscaron proteger a su gente en un contexto de desigualdad de poder.", "Pregunta qué opciones tenía."),
        ("Creer que toda resistencia fue armada.", "También se resiste manteniendo la lengua y las costumbres.", "Piensa en prácticas cotidianas."),
    ],
    [
        ("¿En qué año ocurrió la batalla del bosque de Teutoburgo?", "9 d.C.", "La explicación da ese año."),
        ("¿Cómo se llama la oposición del grupo con menos poder?", "Resistencia", "Es la definición del vocabulario."),
        ("¿Cómo se llama el diálogo para llegar a un acuerdo?", "Negociación", "Es la definición del vocabulario."),
    ],
    [
        ("¿Qué frenó la expansión de Roma hacia el Elba según la clase?", "La derrota de tres legiones en Teutoburgo", "Fue el hecho que la detuvo."),
        ("¿Qué pueblos detuvieron el avance inca al sur del Maule?", "Los mapuche", "La clase lo señala."),
        ("¿Por qué las fuentes suelen favorecer al grupo con más poder?", "Porque ese grupo escribía y conservaba sus relatos", "Los vencidos dejaron menos registros."),
    ],
    [
        arith("Una legión de ejemplo tiene 5.000 soldados. ¿Cuántos soldados tienen tres legiones?", "3*5000", "Se multiplica la cantidad de soldados de una legión por tres."),
        ("Un pueblo de ejemplo mantiene su idioma aunque se lo prohíben. ¿Qué forma de resistencia es?", "Resistencia cultural", "Defiende su lengua."),
        ("Un jefe de ejemplo pide a cambio de su alianza que se respeten sus tierras. ¿Qué mecanismo usa?", "Negociación", "Busca un acuerdo con condiciones."),
    ],
    [
        ("Luis dice: «Los germanos eran bárbaros que atacaban sin razón». ¿Qué corrección haces?", "Defendían su territorio frente a la expansión de Roma", "Tenían sus propias razones."),
        ("Marta dice: «Quien negoció fue débil». ¿Qué respuesta de la clase puedes dar?", "Cada decisión respondió a un contexto y buscaba proteger a su gente", "No se juzga sin contexto."),
    ],
    [
        ("¿Cuál es una forma de resistencia sin armas? A) mantener la lengua y las costumbres propias B) enfrentar al ejército con armas.", "A", "Defender la lengua y las costumbres es resistencia cultural sin armas."),
        ("Una afirmación dice: «Los romanos siempre ganaban». ¿Qué hecho de la clase la contradice?", "La derrota de tres legiones en Teutoburgo", "Fue una derrota romana."),
    ],
    [("Un historiador de ejemplo dice: «Los incas lograron integrar a todos los pueblos». ¿Qué dos casos de la clase lo contradicen?", "La resistencia de los chachapoyas y de los mapuche al sur del Maule", "Hubo pueblos que resistieron.")],
    [("En la unidad de convivencia y conflicto, ¿qué es el poder?", "La capacidad de imponer decisiones o conseguir lo que se quiere", "Es la definición del vocabulario."), ("En la unidad de convivencia y conflicto, ¿qué es una legión?", "Una unidad del ejército romano", "Es la definición del vocabulario."), ("¿Por qué buscar la voz del grupo que resistió?", "Porque las fuentes suelen venir del grupo con más poder", "Así se completa la historia.")],
    (
        "Elige un caso de resistencia (germanos y Roma, chachapoyas o mapuche) y un caso de negociación (curacas incas). Para cada uno escribe: quién tenía más poder, qué hizo el otro grupo, qué consiguió y qué fuente conocemos. Termina con una frase que evite juzgar solo con ideas de hoy.",
        "Germanos y Roma: Roma tenía más poder; Arminio derrotó a tres legiones; frenaron el avance; la fuente es romana. No juzgamos sin contexto.",
        ["un caso de resistencia", "un caso de negociación", "una fuente", "frase sin anacronismo"],
        ["dos fichas y una frase"],
        ["juzgar con valores de hoy sin explicar", "olvidar la fuente"],
        "Lee tus fichas a una persona de tu casa y pídele que diga qué diferencia hay entre resistir y negociar.",
    ),
    "Escribe una pregunta que le harías a una comunidad indígena sobre la resistencia de su pueblo.",
    "Averigua cuántos años duró la conquista de Galia por Roma y quién la dirigió.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a debatir sobre los principios que ayudan a la convivencia entre pueblos y culturas hoy. Sirve para usar los casos del pasado y fundamentar una postura con respeto.",
    ["Conozco casos de convivencia y conflicto.", "Sé argumentar con casos."],
    [
        "El respeto es reconocer el valor de otra persona o cultura y tratarla con dignidad. La tolerancia es aceptar que otros piensen, hablen o vivan distinto, siempre que no dañen a nadie. La resolución pacífica de conflictos es buscar acuerdos sin violencia, por medio del diálogo, la mediación (un tercero ayuda a conversar) o el arbitraje (un tercero decide según reglas). Estos principios sirven en el curso, en la comuna y entre países.",
        "En un debate se presenta una postura, se argumenta con casos y se escucha a los demás. Reglas básicas: hablar por turnos, no interrumpir, no insultar, criticar ideas y no a las personas, y cambiar de postura si hay buenas razones. Para fundamentar con historia, se usan casos del pasado: por ejemplo, la colaboración de traductores en Toledo apoya la idea de que el diálogo enriquece; las guerras de conquista muestran los daños de la violencia.",
        "Un debate no busca «ganar», sino entender mejor. Si en tu curso hay un conflicto, se recomienda hablar con calma, pedir ayuda a una persona adulta de confianza como un profesor o la persona que orienta, y no resolverlo con violencia ni exponiendo a alguien en redes sociales.",
    ],
    [("respeto", "reconocer el valor de otras personas y culturas y tratarlas con dignidad"), ("tolerancia", "aceptar que otros piensen o vivan distinto sin dañar a nadie"), ("mediación", "ayuda de un tercero para que las partes conversen y lleguen a un acuerdo"), ("arbitraje", "decisión de un tercero según reglas acordadas"), ("diálogo", "conversación en que las personas se escuchan y se responden"), ("postura", "opinión que se defiende con argumentos")],
    [
        ("Identificar un principio", "Dos compañeros discuten por un trabajo y piden a una profesora que los ayude a conversar. ¿Qué mecanismo usan?", ["Un tercero ayuda a conversar.", "Es mediación."], "Mediación"),
        ("Identificar otro principio", "Una persona escucha con atención una opinión distinta a la suya y no la insulta. ¿Qué principio muestra?", ["Acepta que otros piensen distinto.", "Es tolerancia (y respeto)."], "Tolerancia y respeto"),
    ],
    [
        ("Pensar que tolerar es aceptar cualquier daño.", "La tolerancia aplica mientras no se dañe a nadie.", "Distingue diferencia de daño."),
        ("Creer que un debate se gana gritando.", "Se busca entender mejor con argumentos y escucha.", "Habla por turnos y critica ideas."),
    ],
    [
        ("¿Cómo se llama el reconocer el valor de otras personas y culturas?", "Respeto", "Es la definición del vocabulario."),
        ("¿Cómo se llama la decisión de un tercero según reglas acordadas?", "Arbitraje", "Es la definición del vocabulario."),
        ("¿A quién conviene acudir si hay un conflicto en el curso?", "A una persona adulta de confianza, como un profesor", "Así lo recomienda la clase."),
    ],
    [
        ("Nombra dos reglas básicas de un debate.", "Dos de estas: hablar por turnos, no interrumpir, no insultar, criticar ideas y no personas", "Son las reglas de la explicación."),
        ("¿Qué caso histórico apoya la idea de que el diálogo enriquece?", "La colaboración de traductores en Toledo", "La clase lo cita."),
        ("¿Qué muestran las guerras de conquista, según la clase?", "Los daños de la violencia", "Se cita como contraejemplo."),
    ],
    [
        ("Un curso de ejemplo debate si cambiar las reglas de uso del patio. Un estudiante dice: «Tu idea es tonta». ¿Qué regla rompe?", "No criticar a las personas, sino a las ideas", "Insultó en vez de criticar la idea."),
        ("Un estudiante cambia de postura tras escuchar un buen argumento. ¿Es una debilidad o un rasgo de buen debate?", "Un rasgo de buen debate", "Se puede cambiar si hay buenas razones."),
        ("Un compañero publica una foto de otro en redes para burlarse de él. ¿Qué dice la clase que no se debe hacer?", "Exponer a alguien en redes sociales", "Se debe hablar con calma y pedir ayuda adulta."),
    ],
    [
        ("Ana dice: «Para resolver un conflicto lo mejor es ganarle al otro». ¿Qué respuesta dan los principios de la clase?", "Se busca un acuerdo con diálogo o mediación, no ganar", "Los principios apuntan a resolver sin violencia."),
        ("Pedro dice: «El respeto significa estar siempre de acuerdo». ¿Qué error comete?", "Se puede respetar a una persona aunque se piense distinto", "Respeto no es acuerdo."),
    ],
    [
        ("Ordena los pasos de un turno de debate: A) responder con respeto a lo que dijeron, B) presentar la postura, C) escuchar a los demás.", "B, C, A", "Se presenta la postura, se escucha y luego se responde."),
        ("Elige la frase que fundamenta mejor: A) «La colaboración en Toledo muestra que dialogar enriquece.» B) «Yo creo que dialogar es mejor porque sí.»", "A", "Usa un caso histórico verificable."),
    ],
    [("Una escuela de ejemplo debate si resolver un conflicto con insultos o con mediación. Un estudiante defiende la mediación citando que los traductores de Toledo colaboraron y la violencia solo causó daños. ¿Qué dos recursos de la clase usó?", "Un caso histórico y un principio de resolución pacífica", "Usó evidencia y un principio.")],
    [("En la unidad de convivencia y conflicto, ¿qué es la tolerancia?", "Aceptar que otros piensen o vivan distinto sin dañar a nadie", "Es la definición del vocabulario."), ("En la unidad de convivencia y conflicto, ¿qué es la mediación?", "La ayuda de un tercero para que las partes lleguen a un acuerdo", "Es la definición del vocabulario."), ("¿Para qué sirve un debate?", "Para entender mejor y fundamentar posturas", "No busca ganar.")],
    (
        "Prepara una intervención de seis líneas para este debate: «¿Qué principio es más importante para la convivencia entre culturas: el respeto, la tolerancia o la resolución pacífica de conflictos?». Elige uno, di tu postura, da un caso histórico de la unidad, responde una posible objeción y cierra con una idea para el curso.",
        "Postura: el respeto. Caso: en Toledo trabajaron juntos traductores de distintas religiones. Objeción: respetar no resuelve conflictos, pero abre el diálogo. Idea: escuchar sin interrumpir.",
        ["elige un principio", "da un caso de la unidad", "responde una objeción", "propone una idea concreta"],
        ["intervención de seis líneas con cuatro elementos"],
        ["no dar caso histórico", "insultar o descalificar"],
        "Practica tu intervención ante una persona de tu casa y pídele que diga si fue respetuosa.",
    ),
    "Escribe dos reglas que propondrías para que los debates de tu curso sean respetuosos.",
    "Averigua qué hace un mediador escolar o una persona que orienta en tu establecimiento.",
)

# ================================================================ clase 5
lesson(
    OA, 5,
    "Aprenderé a fundamentar una conclusión sobre convivencia y conflicto sin juzgar el pasado solo desde el presente. Sirve para cerrar la unidad con una explicación responsable.",
    ["Conozco casos de contacto, poder y resistencia.", "Sé qué es un anacronismo."],
    [
        "Juzgar el pasado solo desde el presente se llama presentismo. Consiste en medir a las personas de otras épocas solo con los valores de hoy, sin considerar sus condiciones. Por ejemplo, decir «los romanos eran malos porque tenían esclavos» sin explicar el contexto ni lo que sabemos hoy. Esto no significa justificar todo: hoy sabemos que la esclavitud, la conquista violenta y la persecución dañaron a muchas personas, y podemos decirlo.",
        "La clave es distinguir tres acciones. Comprender es explicar por qué ocurrió algo con las ideas, los intereses y los recursos de su época. Evaluar es decir qué consecuencias tuvo y para quiénes, con evidencia. Juzgar es expresar un valor actual sobre el hecho. Un buen historiador comprende primero, evalúa con evidencia y, si juzga, lo declara como tal.",
        "Para fundamentar una conclusión se necesita una afirmación, un caso con lugar y fecha, una razón y un límite. Se debe incluir la perspectiva de distintos grupos, no solo la del vencedor. Y se cierra con una pregunta para seguir investigando, porque la historia siempre puede ampliarse con nuevas fuentes.",
    ],
    [("presentismo", "juzgar el pasado solo con los valores de hoy, sin considerar su contexto"), ("comprender", "explicar por qué ocurrió un hecho en su época"), ("evaluar", "analizar consecuencias con evidencia"), ("juzgar", "expresar un valor sobre un hecho"), ("perspectiva", "punto de vista de un grupo"), ("conclusión", "idea final apoyada en evidencia")],
    [
        ("Reconocer el presentismo", "«Los mexicas fueron malos porque no respetaban los derechos humanos actuales.» ¿Qué error cometió?", ["Aplica valores de hoy sin contexto.", "Es presentismo."], "Presentismo"),
        ("Distinguir acciones", "«Explico por qué la conquista ocurrió con las ideas de su época.» ¿Es comprender, evaluar o juzgar?", ["Explica el porqué.", "Es comprender."], "Comprender"),
    ],
    [
        ("Pensar que comprender es justificar.", "Comprender explica; no significa aprobar.", "Distingue comprender, evaluar y juzgar."),
        ("Pensar que nunca se puede juzgar el pasado.", "Se puede juzgar si se declara que es un juicio y se apoya en evidencia.", "Aclara qué es hecho y qué es juicio."),
    ],
    [
        ("¿Cómo se llama juzgar el pasado solo con valores de hoy?", "Presentismo", "Es la definición del vocabulario."),
        ("¿Qué acción consiste en explicar por qué ocurrió algo en su época?", "Comprender", "Es la definición del vocabulario."),
        ("¿Qué partes necesita una conclusión fundamentada?", "Afirmación, caso, razón y límite", "Son las partes de la explicación."),
    ],
    [
        ("En la unidad de convivencia y conflicto, ¿qué es evaluar?", "Analizar consecuencias con evidencia", "Es la definición del vocabulario."),
        ("¿Por qué incluir la perspectiva de distintos grupos?", "Para no mostrar solo la visión del vencedor", "La clase lo recomienda."),
        ("¿Con qué se debe cerrar una conclusión, según la clase?", "Con una pregunta para seguir investigando", "La historia puede ampliarse."),
    ],
    [
        ("Un estudiante escribe: «Los incas fueron crueles porque obligaban a hacer trabajos». ¿Qué debería agregar para comprender?", "El contexto: la mita era un sistema de trabajo por turnos con beneficios y obligaciones", "Comprender incluye el contexto."),
        ("Otro escribe: «La conquista dañó a muchos pueblos y hoy lo reconocemos». ¿Es presentismo o una evaluación con evidencia?", "Una evaluación con evidencia declarada", "Reconoce los daños y lo dice como juicio actual."),
        ("«La esclavitud existió en Roma y dañó a millones de personas; hoy se considera una violación de derechos humanos.» ¿Qué frase es el juicio actual?", "«Hoy se considera una violación de derechos humanos»", "Expresa un valor actual."),
    ],
    [
        ("Luis dice: «Si explico por qué pasó, estoy justificándolo». ¿Qué respuesta le das?", "Explicar no es justificar: comprender y juzgar son acciones distintas", "La clase las diferencia."),
        ("Marta dice: «No debo opinar nunca sobre el pasado». ¿Qué matiz agregas?", "Se puede opinar si se declara que es un juicio y se apoya en evidencia", "No se prohíbe juzgar."),
    ],
    [
        ("Ordena de la acción más descriptiva a la más valorativa: A) juzgar, B) comprender, C) evaluar.", "B, C, A", "Comprender describe el porqué, evaluar analiza consecuencias y juzgar expresa un valor."),
        ("Una conclusión dice: «Los mapuche resistieron a los incas al sur del Maule; según crónicas y arqueología, el avance se detuvo. Queda abierta la pregunta de cómo vivieron esa frontera». ¿Qué parte es la última frase?", "La pregunta para seguir investigando", "Cierra con una pregunta abierta."),
    ],
    [("Un estudiante lee dos conclusiones: A) «Los romanos fueron perversos.» B) «Roma conquistó pueblos, y la conquista dañó a muchos; hoy la condenamos, aunque en su época se la veía como un deber». ¿Cuál evita mejor el presentismo?", "B", "Esa conclusión explica el contexto y declara el juicio actual.")],
    [("En la unidad de convivencia y conflicto, ¿qué es el presentismo?", "Juzgar el pasado solo con los valores de hoy", "Es la definición del vocabulario."), ("¿Qué diferencia hay entre comprender y juzgar?", "Comprender explica el porqué; juzgar expresa un valor", "Son acciones distintas."), ("¿Se puede juzgar el pasado?", "Sí, declarando que es un juicio y con evidencia", "No se prohíbe, pero se aclara.")],
    (
        "Escribe una conclusión final de siete líneas sobre la unidad: «¿Cómo fueron la convivencia y el conflicto entre culturas en las civilizaciones estudiadas?». Debe tener afirmación, un caso con lugar y fecha, una razón, un límite, una frase que distinga comprender de juzgar y una pregunta final. Usa solo datos de la unidad.",
        "Afirmación: hubo convivencia y conflicto. Caso: Toledo, siglo XII; razón: el diálogo enriqueció; límite: no todos tenían los mismos derechos; hoy condenamos la violencia; pregunta: ¿qué otras fuentes faltan?",
        ["afirmación", "caso con lugar y fecha", "límite", "pregunta final"],
        ["conclusión de siete líneas con seis elementos"],
        ["presentismo sin contexto", "olvidar la pregunta"],
        "Lee tu conclusión a una persona de tu casa y pídele que señale dónde distingues comprender de juzgar.",
    ),
    "Escribe una pregunta histórica de esta unidad que te gustaría investigar.",
    "Averigua cómo se llama el área de la historia que estudia la memoria de los pueblos originarios y qué fuentes usa.",
)
