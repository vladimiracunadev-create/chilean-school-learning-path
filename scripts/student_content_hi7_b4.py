"""Cuaderno del estudiante, 7.º básico Historia, Geografía y Ciencias Sociales: OA 14 (Tawantinsuyu)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI07 OA 14"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a ubicar la expansión del Tawantinsuyu y sus cuatro regiones. Sirve para entender cuánto territorio abarcó y qué pueblos quedaron dentro.",
    ["Sé que los incas vivieron en los Andes.", "Sé leer un mapa con norte, sur, este y oeste."],
    [
        "El Tawantinsuyu fue el Estado de los incas. En quechua, «tawa» significa cuatro y «suyu» significa región: «las cuatro regiones unidas». Su capital era Cusco, en los Andes del actual Perú. Las cuatro regiones eran: Chinchaysuyo, al noroeste; Antisuyo, al este, hacia la selva; Collasuyo, al sur, que incluía el altiplano y parte del norte de Chile; y Contisuyo, al suroeste, hacia la costa.",
        "Los incas eran al comienzo un pueblo pequeño en el valle de Cusco. Su expansión creció con rapidez desde mediados del siglo XV, con gobernantes como Pachacútec, y siguió hasta que en 1532 los españoles capturaron al Sapa Inca (el gobernante) Atahualpa en Cajamarca. En su mayor extensión, el Tawantinsuyu iba desde el sur de Colombia hasta el centro de Chile, en torno al río Maule, e incluía territorios de Ecuador, Perú, Bolivia y el noroeste de Argentina.",
        "En lo que hoy es Chile, el Tawantinsuyu llegó al norte y a la zona central. Allí vivían pueblos como los atacameños y los diaguitas, que quedaron integrados al Estado inca. Más al sur, los pueblos mapuche resistieron. Para entender esta expansión es útil ubicar cada región en el mapa y fechar cada avance.",
    ],
    [("Tawantinsuyu", "Estado de los incas, «las cuatro regiones unidas» en quechua"), ("Cusco", "capital del Tawantinsuyu"), ("suyu", "región, en quechua"), ("Sapa Inca", "gobernante supremo del Tawantinsuyu"), ("expansión", "crecimiento de un Estado sobre nuevos territorios"), ("Collasuyo", "región sur del Tawantinsuyu, que incluía el norte de Chile")],
    [
        ("Ubicar una región", "Una ficha de ejemplo dice: «Región al sur, con altiplano y parte del actual norte de Chile». ¿Qué región es?", ["Al sur: Collasuyo.", "Incluye el norte de Chile."], "Collasuyo"),
        ("Calcular una fecha", "Una expansión inca empezó hacia 1450 y los españoles capturaron a Atahualpa en 1532. ¿Cuántos años pasaron?", ["Se resta 1450 de 1532.", "1532 − 1450 = 82."], "82 años"),
    ],
    [
        ("Pensar que el Tawantinsuyu siempre fue grande.", "Empezó como un pueblo pequeño en el valle de Cusco y se expandió desde el siglo XV.", "Fecha cada etapa."),
        ("Creer que los incas llegaron a todo Chile.", "Llegaron hasta el centro, en torno al río Maule; los mapuche resistieron más al sur.", "Ubica el límite sur en el mapa."),
    ],
    [
        ("¿Cuál era la capital del Tawantinsuyu?", "Cusco", "Estaba en los Andes del actual Perú."),
        ("¿Cuántas regiones tenía el Tawantinsuyu?", "Cuatro", "El nombre «tawa» significa cuatro."),
        ("¿Qué región incluía parte del norte de Chile?", "Collasuyo", "Es la región sur."),
    ],
    [
        ("¿Qué significa «suyu» en quechua?", "Región", "Está en el vocabulario."),
        ("¿En qué año capturaron los españoles a Atahualpa en Cajamarca?", "1532", "La explicación da esa fecha."),
        ("¿Qué pueblos de lo que hoy es Chile quedaron integrados al Tawantinsuyu?", "Atacameños y diaguitas", "La clase los menciona."),
    ],
    [
        arith("Un mapa de ejemplo muestra la distancia entre Cusco y el río Maule como 4.000 kilómetros en una ruta. Si un viajero recorre 25 kilómetros por día, ¿cuántos días tarda?", "4000//25", "Se divide la distancia por los kilómetros diarios.", " días"),
        ("Ana dice que el Tawantinsuyu llegó hasta Punta Arenas. Según la clase, ¿es correcto?", "No, llegó hasta el centro de Chile, en torno al río Maule", "El límite sur fue el Maule."),
        ("Una ficha de ejemplo dice: «Región al este, hacia la selva». ¿Qué región es?", "Antisuyo", "Es la región oriental."),
    ],
    [
        ("Pedro dice: «Los incas siempre vivieron como un gran Estado». ¿Qué dato de la clase lo corrige?", "Empezaron como un pueblo pequeño en el valle de Cusco y se expandieron desde el siglo XV", "Hubo un proceso de crecimiento."),
        ("¿Por qué conviene decir «hasta el río Maule» y no «hasta cierta ciudad»?", "Porque las fronteras eran zonas y no líneas exactas, y el río es una referencia geográfica", "Ubica el límite en un accidente geográfico."),
    ],
    [
        ("¿Qué región queda más al norte: Chinchaysuyo (noroeste) o Collasuyo (sur)?", "Chinchaysuyo", "La clase la ubica al noroeste, mientras Collasuyo está al sur."),
        ("Una afirmación dice: «El Tawantinsuyu incluía parte del actual Chile, Bolivia y Perú». ¿Qué dato de la clase la respalda?", "Collasuyo incluía altiplano y parte del norte de Chile, y la capital estaba en el actual Perú", "Son datos de la explicación."),
    ],
    [("Un estudiante lee una ficha: «Pueblo atacameño, norte de Chile, siglo XV». ¿A qué región inca pertenecía?", "Collasuyo", "Esa región incluía el norte de Chile.")],
    [("¿Qué significa Tawantinsuyu?", "Las cuatro regiones unidas", "Es la definición del vocabulario."), ("¿Cuál era el límite sur del Tawantinsuyu?", "El centro de Chile, en torno al río Maule", "Así lo dice la explicación."), ("¿Quién era el Sapa Inca?", "El gobernante supremo", "Está en el vocabulario.")],
    (
        "Dibuja un mapa muy simple de América del Sur y marca con flechas las cuatro regiones del Tawantinsuyu, con su nombre y su orientación. Marca también el límite sur en Chile. Escribe después una frase que diga qué pueblos de Chile quedaron dentro del Tawantinsuyu.",
        "Chinchaysuyo (noroeste), Antisuyo (este), Collasuyo (sur), Contisuyo (suroeste); atacameños y diaguitas quedaron integrados.",
        ["marca las cuatro regiones", "ubica Cusco", "marca el límite sur", "nombra al menos un pueblo de Chile"],
        ["mapa simple con cuatro regiones, Cusco y límite sur más una frase"],
        ["confundir Antisuyo con Collasuyo", "poner el límite sur en la Patagonia"],
        "Muestra tu mapa a una persona de tu casa y pídele que señale la región que incluía el norte de Chile.",
    ),
    "Escribe qué diferencia hay entre un Estado grande y un Estado que se expande poco a poco.",
    "Averigua cómo se dice «cuatro» y «región» en quechua y qué otras palabras quechuas usamos en Chile.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a analizar los caminos, la administración y la reciprocidad del Tawantinsuyu. Sirve para entender cómo un Estado sin escritura alfabética pudo organizar un territorio tan grande.",
    ["Sé que los incas gobernaron un territorio extenso.", "Sé que un Estado necesita comunicarse y recoger recursos."],
    [
        "El Qhapaq Ñan o camino inca fue una red de caminos de más de 30.000 kilómetros que unía las regiones del Tawantinsuyu. Tenía tramos empedrados, escaleras, puentes colgantes de fibras y tambos, que eran posadas y depósitos a lo largo del camino. Servía para mover ejércitos, productos y mensajes. Los chasquis eran corredores que llevaban mensajes por relevos de tambo en tambo.",
        "Los incas no tenían escritura como la nuestra, pero usaron el quipu, un conjunto de cuerdas con nudos para registrar cantidades. La administración estaba organizada: el Sapa Inca gobernaba desde Cusco, con gobernadores de las regiones y con jefes locales llamados curacas. Había depósitos estatales (collcas) para guardar alimentos y telas. Para producir esos alimentos se cultivaba en las laderas con andenes, terrazas de piedra y tierra que sostenían la pendiente, y se sembraba maíz, papa y quinua.",
        "La economía se apoyaba en la reciprocidad, el intercambio de trabajo y ayuda entre personas de una comunidad llamada ayllu, y en la redistribución, en la que el Estado repartía bienes que recogía. Las comunidades daban trabajo al Estado en turnos (mita) y recibían alimentos y chicha en las fiestas. Así se unían obligaciones y beneficios.",
    ],
    [("Qhapaq Ñan", "red de caminos del Tawantinsuyu"), ("tambo", "posada y depósito junto al camino inca"), ("chasqui", "corredor que llevaba mensajes por relevos"), ("quipu", "conjunto de cuerdas con nudos para registrar cantidades"), ("curaca", "jefe local de un grupo andino"), ("reciprocidad", "intercambio de ayuda y trabajo entre personas o comunidades")],
    [
        ("Seguir un mensaje", "Un mensaje debe llegar a un tambo a 15 km. El chasqui corre un tramo y entrega el aviso al siguiente chasqui. ¿Cómo se llama este sistema?", ["Cada corredor cubre un tramo.", "Lo entrega al siguiente.", "Se llama relevos."], "Relevos"),
        ("Explicar la reciprocidad", "Una comunidad trabaja un campo del Estado y recibe alimentos y chicha en una fiesta. ¿Qué principio muestra?", ["Da trabajo y recibe algo a cambio.", "Es reciprocidad."], "Reciprocidad"),
    ],
    [
        ("Pensar que sin escritura no había administración.", "Usaron quipus, funcionarios, depósitos y caminos para administrar.", "Pregunta qué medio usaban para registrar y mandar."),
        ("Creer que el camino inca era una sola ruta recta.", "Era una red con muchos ramales entre regiones.", "Piensa en red, no en una línea."),
    ],
    [
        ("¿Cómo se llamaba el camino inca?", "Qhapaq Ñan", "Está en el vocabulario."),
        ("¿Quiénes llevaban mensajes por relevos?", "Los chasquis", "Está en el vocabulario."),
        ("¿Qué se guardaba en las collcas?", "Alimentos y telas", "Eran depósitos estatales."),
    ],
    [
        ("¿Para qué servía un quipu?", "Para registrar cantidades", "Es la definición del vocabulario."),
        ("¿Qué era un ayllu?", "Una comunidad andina cuyos miembros se ayudaban entre sí", "La explicación lo presenta como comunidad con reciprocidad."),
        ("¿Por qué los tambos eran útiles para los viajeros y los ejércitos?", "Porque ofrecían descanso y depósitos de alimentos a lo largo del camino", "Eran posadas y depósitos."),
    ],
    [
        arith("Un tramo del camino inca tiene 12 tambos y cada tambo guarda 300 raciones de alimento. ¿Cuántas raciones hay en total?", "12*300", "Se multiplica el número de tambos por las raciones de cada uno."),
        ("Un chasqui de ejemplo lleva un quipu con un registro de cantidades. ¿Qué dos medios de la administración inca usa?", "El chasqui y el quipu", "Combina mensajero y registro."),
        ("Un curaca de ejemplo recibe una orden del Sapa Inca y la comunica a su comunidad. ¿Qué nivel de la administración representa el curaca?", "Un jefe local", "Los curacas eran jefes locales."),
    ],
    [
        ("Marta dice: «El camino inca servía solo para el comercio». ¿Qué otros usos de la clase puedes dar?", "Mover ejércitos y mensajes, además de productos", "La clase menciona varios usos."),
        ("Un historiador de ejemplo dice: «La reciprocidad era una obligación y a la vez una forma de ayuda». ¿Qué muestra la mita en ese sentido?", "Que la comunidad daba trabajo al Estado y recibía alimentos y chicha", "Había obligación con beneficio."),
    ],
    [
        ("Ordena de lo más local a lo más central: A) Sapa Inca, B) ayllu, C) curaca.", "B, C, A", "El ayllu es la comunidad, el curaca su jefe y el Sapa Inca el gobernante supremo."),
        ("Un pueblo andino vive en una ladera con poca tierra plana y quiere sembrar maíz y papa. ¿Qué sistema de cultivo de la clase le sirve?", "Los andenes, terrazas en la ladera", "Los andenes sostienen la pendiente y crean campos de cultivo."),
    ],
    [("Un viaje de ejemplo parte de Cusco hacia el norte de Chile por el Qhapaq Ñan. ¿Qué apoyo del camino le sirve para descansar y cuál para cruzar un río?", "Los tambos para descansar y los puentes colgantes para cruzar el río", "Los tambos eran posadas y los puentes cruzaban ríos.")],
    [("En la unidad del Tawantinsuyu, ¿qué es un tambo?", "Una posada y depósito a lo largo del camino", "Es la definición del vocabulario."), ("En la unidad del Tawantinsuyu, ¿qué es un curaca?", "Un jefe local", "Es la definición del vocabulario."), ("En la unidad del Tawantinsuyu, ¿qué es la reciprocidad?", "Un intercambio de ayuda y trabajo", "Es la definición del vocabulario.")],
    (
        "Escribe una explicación de seis líneas titulada «Cómo un mensaje llegaba de Cusco a una región lejana». Incluye: el camino, los tambos, los chasquis, el quipu y un curaca que recibe el mensaje. Al final, escribe un límite: qué no sabemos con certeza.",
        "El mensaje salía de Cusco por el Qhapaq Ñan, un chasqui lo llevaba hasta un tambo y otro seguía; llegaba al curaca. No sabemos exactamente cuánto tardaba.",
        ["incluye los cinco elementos", "sigue un orden lógico", "explica el relevo", "incluye un límite"],
        ["texto de seis líneas con los cinco elementos y un límite"],
        ["olvidar el quipu", "decir que los chasquis corrían todo el camino sin relevos"],
        "Lee tu texto a una persona de tu casa y pídele que cuente cuántos relevos imaginó.",
    ),
    "Dibuja un tambo con depósito, descanso y camino, y rotula cada parte.",
    "Averigua qué tramos del Qhapaq Ñan se conservan hoy en Chile.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a examinar las estrategias con que los incas integraron y dominaron a otros pueblos. Sirve para entender que combinaron fuerza, negociación y organización.",
    ["Sé que el Tawantinsuyu tenía caminos y administración.", "Sé que dominar a otro pueblo tiene consecuencias."],
    [
        "Los incas usaron varias estrategias para unir pueblos tan diversos. Una fue el ejército, que sometía a quienes se resistían. Otra fue la negociación: ofrecían regalos y alianzas a los jefes que aceptaban. A los curacas que se integraban se les permitía conservar parte de su poder local. A veces los hijos de curacas vivían en Cusco, donde aprendían quechua y costumbres incas.",
        "Una estrategia importante fue el traslado de población. Los mitimaes eran familias trasladadas a otras regiones para cultivar, vigilar o enseñar costumbres. También se impuso el quechua como lengua oficial para comunicarse con todos los pueblos y se promovió el culto al Sol, aunque los pueblos conservaron sus propios dioses.",
        "Para los pueblos dominados había obligaciones: trabajo por turnos (mita), entrega de tejidos y alimentos, y servicio militar. Existía además el yanaconaje: los yanaconas eran personas que servían de manera permanente a nobles o al Inca, separadas de su comunidad. Para los incas estas medidas fortalecían la unidad. Para algunos pueblos significaron pérdida de autonomía.",
    ],
    [("mitimae", "familia trasladada a otra región por orden del Estado inca"), ("quechua", "lengua oficial del Tawantinsuyu"), ("yanacona", "persona que servía de manera permanente a un noble o al Inca"), ("mita", "trabajo por turnos para el Estado"), ("autonomía", "capacidad de un pueblo de decidir por sí mismo"), ("integración", "unión de un pueblo a un Estado mayor")],
    [
        ("Identificar la estrategia", "Una familia de ejemplo es trasladada desde el valle de Cusco a una región recién conquistada para cultivar y enseñar costumbres. ¿Qué estrategia muestra?", ["La familia es trasladada.", "Se llama mitimae."], "El traslado de población (mitimaes)"),
        ("Relacionar una obligación", "Una comunidad entrega trabajo por turnos al Estado cada año. ¿Qué institución es?", ["Trabajo por turnos para el Estado.", "Se llama mita."], "La mita"),
    ],
    [
        ("Creer que los incas solo dominaron por la guerra.", "También usaron negociación, regalos, traslados y lengua común.", "Nombra al menos dos estrategias."),
        ("Pensar que los pueblos perdían todo y se volvían iguales.", "Muchos conservaron dioses, lengua y jefes locales con límites.", "Pregunta qué se conservó y qué se perdió."),
    ],
    [
        ("¿Qué lengua fue oficial en el Tawantinsuyu?", "El quechua", "Está en el vocabulario."),
        ("¿Cómo se llamaban las familias trasladadas a otras regiones?", "Mitimaes", "Está en el vocabulario."),
        ("¿Qué eran los yanaconas?", "Personas que servían de manera permanente a nobles o al Inca", "Es la definición del vocabulario."),
    ],
    [
        ("¿Para qué vivían los hijos de curacas en Cusco?", "Para aprender quechua y costumbres incas", "Así se integraban a los incas."),
        ("¿Por qué el quechua ayudaba a gobernar?", "Porque permitía comunicarse con pueblos de lenguas distintas", "Una lengua común facilita la administración."),
        ("¿Qué conservaban los curacas que se integraban sin resistir?", "Parte de su poder local", "La clase lo indica."),
    ],
    [
        arith("Un grupo de 14 familias mitimaes se traslada y cada familia tiene 5 personas. ¿Cuántas personas se trasladan?", "14*5", "Se multiplica el número de familias por las personas de cada una."),
        ("Una ficha de ejemplo dice: «Un jefe local recibe regalos y acepta unirse al Estado». ¿Qué estrategia muestra?", "Negociación", "Se logra integración sin guerra."),
        ("Un pueblo mantiene su dios y también reconoce al Sol. ¿Qué dato de la clase explica esto?", "El culto al Sol se promovió, pero los pueblos conservaron sus propios dioses", "Hubo integración con conservación."),
    ],
    [
        ("Pedro dice: «Todos los pueblos aceptaron al Inca porque les convenía». ¿Qué dato de la clase lo contradice?", "Algunos resistieron y fueron sometidos por el ejército", "La clase menciona sometimiento."),
        ("¿Desde qué punto de vista la mita fortalecía el Estado y desde cuál significaba pérdida de autonomía?", "Fortalecía al Estado inca; significaba pérdida de autonomía para los pueblos que debían trabajar", "Hay dos perspectivas."),
    ],
    [
        ("Entre estas dos estrategias, ¿cuál no usa la fuerza? A) regalos y alianzas B) ataque del ejército.", "A", "Los regalos y las alianzas se ofrecen; el ataque es violento."),
        ("Una afirmación dice: «El imperio inca unió a los pueblos solo con respeto». Corrige la afirmación con dos estrategias de la clase.", "Combinó negociación con ejército y traslados forzados", "Hubo coerción además de alianza."),
    ],
    [("Un estudiante lee que un pueblo de ejemplo fue integrado con regalos, los hijos de su curaca vivieron en Cusco, parte de su población fue trasladada y todos adoptaron el quechua. ¿Cuántas estrategias distintas se mencionan en el relato?", "Cuatro", "Regalos, hijos del curaca en Cusco, traslado y quechua son cuatro.")],
    [("¿Qué son los mitimaes?", "Familias trasladadas a otra región por orden del Estado", "Es la definición del vocabulario."), ("¿Por qué se impuso el quechua?", "Para comunicarse con todos los pueblos", "Era la lengua oficial."), ("¿Qué perdían algunos pueblos?", "Autonomía", "Dependían del Estado.")],
    (
        "Elige un pueblo de ejemplo que debe integrarse al Tawantinsuyu: A) un pueblo con muchos guerreros y un curaca que desconfía; B) un pueblo pequeño que necesita alimentos. Describe qué estrategias de la clase usarían los incas, cómo reaccionaría el pueblo y qué ganaría y perdería cada lado.",
        "Pueblo B: los incas ofrecen alimentos de las collcas y alianza; el curaca acepta; el pueblo gana seguridad y pierde autonomía.",
        ["usa al menos dos estrategias", "describe una reacción posible", "nombra una ganancia y una pérdida", "evita juicios sin evidencia"],
        ["texto de seis líneas con cuatro elementos"],
        ["decir que todos aceptaban sin problemas", "no mencionar pérdidas"],
        "Cuéntale tu caso a una persona de tu casa y pídele que diga si habría aceptado.",
    ),
    "Escribe una diferencia entre mita y yanaconaje con tus palabras.",
    "Averigua qué pueblos de Chile quedaron dentro del Tawantinsuyu y qué evidencia arqueológica se conserva.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a reconocer pueblos, resistencias y negociaciones dentro del Tawantinsuyu. Sirve para ver que los pueblos no fueron solo «dominados», sino que actuaron.",
    ["Sé cómo el Tawantinsuyu integró pueblos.", "Sé que una fuente tiene autor y fecha."],
    [
        "El Tawantinsuyu reunió pueblos con lenguas y costumbres distintas, como los chancas, los chachapoyas, los atacameños y los diaguitas. No todos se integraron de la misma manera. Algunos se aliaron pronto, otros resistieron y fueron sometidos, y otros negociaron condiciones.",
        "Los chancas fueron rivales de los incas antes de la gran expansión y, según los relatos, los incas los vencieron en el siglo XV. Los chachapoyas, en el nororiente de Perú, resistieron y luego fueron sometidos. En Chile, los atacameños y diaguitas fueron incorporados, mientras que los pueblos mapuche, según crónicas y arqueología, resistieron al sur del Maule.",
        "Muchas de estas historias nos llegan por cronistas españoles que escribieron después de 1532, a veces usando relatos de nobles incas. Por eso hay que contrastar con la arqueología y con los testimonios de comunidades actuales. En vez de preguntar solo «¿quién ganó?», conviene preguntar también cómo actuaron los pueblos para defender intereses, cambiar acuerdos o adaptarse.",
    ],
    [("resistencia", "oposición de un pueblo a ser dominado"), ("negociación", "diálogo para llegar a un acuerdo"), ("sometimiento", "dominio de un pueblo por la fuerza"), ("cronista", "persona que escribe la historia de su tiempo"), ("incorporar", "unir un pueblo a un Estado"), ("interés", "aquello que un grupo quiere conseguir o proteger")],
    [
        ("Distinguir reacciones", "Un pueblo de ejemplo rechazó al ejército inca y fue vencido. ¿Qué reacción tuvo?", ["Se opuso a la dominación.", "Fue vencido.", "Resistió y fue sometido."], "Resistió y fue sometido"),
        ("Ubicar en Chile", "Un pueblo de ejemplo del norte de Chile fue incorporado al Tawantinsuyu. ¿Cuál puede ser?", ["Norte de Chile: atacameños.", "También diaguitas más al sur."], "Atacameños o diaguitas"),
    ],
    [
        ("Pensar que los pueblos andinos eran todos iguales.", "Tenían lenguas y respuestas diferentes: unos se aliaron, otros resistieron.", "Nombra el pueblo y qué hizo."),
        ("Preguntar solo quién ganó.", "También importa cómo actuaron los pueblos para defender intereses.", "Pregunta qué quería cada actor."),
    ],
    [
        ("¿Cómo se llama la oposición de un pueblo a ser dominado?", "Resistencia", "Está en el vocabulario."),
        ("¿Qué pueblos fueron rivales de los incas antes de la gran expansión?", "Los chancas", "La clase los menciona."),
        ("¿Dónde resistieron los pueblos mapuche, según la clase?", "Al sur del río Maule", "Es el límite sur de los incas."),
    ],
    [
        ("¿Por qué conviene contrastar los relatos de los cronistas con la arqueología?", "Porque los cronistas escribieron después y desde su mirada", "La arqueología aporta otra evidencia."),
        ("¿Qué hicieron algunos pueblos en lugar de resistir o someterse?", "Negociaron condiciones", "La clase indica que algunos negociaron."),
        ("¿Qué significa «incorporar» un pueblo al Estado?", "Unirlo a un Estado mayor", "Es la definición del vocabulario."),
    ],
    [
        ("Una crónica de ejemplo dice: «Los chachapoyas resistieron con fuerza». ¿Qué debes preguntar sobre el cronista?", "Quién era, cuándo escribió y desde qué mirada", "Se contrasta la fuente."),
        ("Una fuente arqueológica de ejemplo muestra fortalezas incas en la zona del Maule, límite sur del Estado. ¿Qué sugiere?", "Que hubo una frontera militar entre incas y pueblos que resistieron", "Las fortificaciones indican conflicto."),
        ("Un pueblo de ejemplo negoció que su curaca conservara sus tierras a cambio de mita. ¿Qué ganó y qué cedió?", "Ganó conservar tierras; cedió trabajo", "Cada parte logró algo y cedió algo."),
    ],
    [
        ("Luis dice: «Los pueblos sometidos no hicieron nada». Da un ejemplo de la clase que lo contradiga.", "Los chachapoyas resistieron; algunos pueblos negociaron condiciones", "Hubo acciones de los pueblos."),
        ("¿Por qué no es lo mismo «resistir» que «ser derrotado»?", "Porque resistir es una acción y ser derrotado es el resultado", "Un pueblo puede resistir y aun así perder."),
    ],
    [
        ("¿Cuál de estas relaciones usó la fuerza: A) alianza con regalos B) sometimiento por el ejército?", "B", "El sometimiento implica vencer por las armas; la alianza se pacta."),
        ("Una afirmación dice: «Los atacameños y diaguitas fueron incorporados sin ninguna negociación». ¿Qué advertencia haces?", "Las fuentes no permiten asegurarlo; puede haber habido negociación o resistencia", "Los datos son limitados."),
    ],
    [("Un historiador de ejemplo dice: «Los chancas, los chachapoyas y los mapuche muestran que los pueblos actuaron de distinto modo ante los incas». ¿Qué ejemplo da la clase de cada una de las tres respuestas: rivalidad previa, resistencia luego sometida y resistencia que detuvo la expansión?", "Chancas: rivalidad previa; chachapoyas: resistencia luego sometida; mapuche: resistencia al sur del Maule", "Cada pueblo ilustra una respuesta distinta.")],
    [("En la unidad del Tawantinsuyu, ¿qué es la resistencia?", "La oposición de un pueblo a ser dominado", "Es la definición del vocabulario."), ("¿Qué pueblos de Chile fueron incorporados?", "Atacameños y diaguitas", "La clase lo dice."), ("¿Por qué preguntar cómo actuaron los pueblos?", "Para ver que defendieron intereses y no fueron solo dominados", "Los pueblos tuvieron iniciativa.")],
    (
        "Elige uno de estos tres pueblos: chancas, chachapoyas o mapuche. Escribe seis líneas con: dónde vivían, qué hicieron ante los incas, qué fuente cuenta su historia y qué límite tiene esa fuente. Usa solo datos de la clase y escribe «no sé» donde falte información.",
        "Chachapoyas: nororiente de Perú; resistieron y fueron sometidos; la crónica española cuenta su historia; límite: escribió después de 1532.",
        ["incluye ubicación", "incluye acción ante los incas", "incluye fuente y su límite", "admite lo que no sabe"],
        ["texto de seis líneas con los cuatro elementos"],
        ["inventar fechas o hechos", "no mencionar el límite de la fuente"],
        "Léele tu texto a una persona de tu casa y pídele que diga qué pregunta le quedó.",
    ),
    "Escribe dos preguntas que harías a una comunidad actual sobre la historia de su pueblo con los incas.",
    "Averigua qué fortalezas incas existen en el norte de Chile, como el Pukará de Quitor, y qué se sabe de ellas.",
)

# ================================================================ clase 5
lesson(
    OA, 5,
    "Aprenderé a explicar la unidad y la diversidad del Tawantinsuyu con varias fuentes. Sirve para ver que un Estado puede unir y a la vez dejar espacio a las diferencias.",
    ["Sé que los incas usaron caminos, administración y estrategias de integración.", "Sé contrastar fuentes."],
    [
        "Para explicar el Tawantinsuyu hay que mirar dos cosas a la vez. La unidad incluye el camino inca, el quechua como lengua oficial, la administración, la mita y el culto al Sol. La diversidad incluye las lenguas locales, los dioses propios, los curacas y las costumbres de cada pueblo. Ambas existieron al mismo tiempo.",
        "Las fuentes ayudan a ver esa mezcla. Los quipus y los restos de caminos y collcas muestran organización común. Las cerámicas, textiles y tumbas locales muestran estilos propios. Los cronistas españoles aportan relatos, pero desde su mirada. Hoy, las comunidades andinas conservan lenguas y tradiciones que también son fuentes.",
        "Una explicación equilibrada combina varias fuentes y evita dos errores: decir que todo era uniforme o decir que cada pueblo vivía aislado. También avisa qué no se puede afirmar. Por ejemplo, no sabemos con exactitud cuánta gente vivía en el Tawantinsuyu, porque las cifras de los cronistas se contradicen.",
    ],
    [("unidad", "aquello que une a varios grupos bajo un mismo Estado"), ("diversidad", "diferencia de lenguas, creencias y costumbres"), ("uniforme", "igual en todas partes"), ("evidencia material", "objetos y restos que se conservan, como caminos, textiles o tumbas"), ("equilibrada", "que considera varios puntos de vista"), ("contradecirse", "decir cosas incompatibles")],
    [
        ("Clasificar un rasgo", "El quechua como lengua oficial, ¿es un rasgo de unidad o de diversidad?", ["Une a todos para comunicarse.", "Es unidad."], "Unidad"),
        ("Clasificar otro rasgo", "Un pueblo conserva a su propio dios y su estilo de cerámica. ¿Es unidad o diversidad?", ["Son rasgos propios del pueblo.", "Es diversidad."], "Diversidad"),
    ],
    [
        ("Pensar que unidad significa que todos eran iguales.", "Podía haber un camino y una lengua oficial y a la vez lenguas y dioses locales.", "Busca rasgos comunes y rasgos propios."),
        ("Usar una sola fuente para explicar todo.", "Cada fuente muestra una parte; se combinan para ver el conjunto.", "Cita al menos dos tipos de fuentes."),
    ],
    [
        ("¿Qué rasgo de unidad usa un quipu?", "La administración común", "Servía para registrar cantidades del Estado."),
        ("¿Qué fuente local muestra estilos propios de cada pueblo?", "Las cerámicas, los textiles o las tumbas locales", "Muestran diferencias entre pueblos."),
        ("¿Qué fuente de la clase cuenta relatos desde la mirada española?", "Los cronistas", "Escribieron después de 1532."),
    ],
    [
        ("¿Por qué las cifras de población del Tawantinsuyu son inciertas?", "Porque las cifras de los cronistas se contradicen", "No hay un censo seguro."),
        ("¿Qué evita una explicación equilibrada?", "Decir que todo era uniforme o que cada pueblo vivía aislado", "Son los dos errores de la clase."),
        ("¿Qué fuentes actuales ayudan a entender la diversidad andina?", "Las comunidades andinas con sus lenguas y tradiciones", "La clase las incluye como fuentes."),
    ],
    [
        ("Una ficha de ejemplo dice: «Se encontró un tambo con collca y un camino empedrado». ¿Qué rasgo de unidad apoya?", "La organización común del Estado inca", "Tambo, collca y camino son obras del Estado."),
        ("Una ficha de ejemplo dice: «Se encontró cerámica de estilo local en una tumba de la época inca». ¿Qué muestra?", "Que se conservaron costumbres locales en tiempos incas", "Los estilos locales muestran diversidad."),
        arith("Un cronista de ejemplo dice que había 6 millones de habitantes y otro dice 14 millones. ¿Cuánta es la diferencia entre ambas cifras, en millones?", "14-6", "Se resta la cifra menor a la mayor.", " millones"),
    ],
    [
        ("Julia dice: «Si había quechua, no existían otras lenguas». Da un argumento de la clase en contra.", "Las lenguas locales siguieron existiendo", "El quechua era oficial, pero no la única lengua."),
        ("¿Por qué una explicación debe decir «no sabemos con exactitud»?", "Porque las fuentes tienen límites y se contradicen en algunos datos", "Es honestidad sobre la evidencia."),
    ],
    [
        ("Ordena una buena explicación que empieza por un rasgo de unidad y termina con el límite: A) límite, B) rasgo de unidad, C) rasgo de diversidad, D) conclusión.", "B, C, D, A", "Se presentan unidad y diversidad, se concluye y se cierra con el límite."),
        ("Una afirmación dice: «El Tawantinsuyu fue un Estado uniforme». ¿Qué dos evidencias de la clase la contradicen?", "Lenguas locales y dioses propios o estilos de cerámica locales", "Ambos rasgos muestran diversidad."),
    ],
    [("Un estudiante lee dos relatos: uno dice que el Tawantinsuyu estaba muy unido y otro que cada pueblo mantenía su cultura. ¿Qué conclusión equilibrada puedes escribir?", "Que había elementos comunes y diferencias locales al mismo tiempo", "Ambas ideas son compatibles.")],
    [("En la unidad del Tawantinsuyu, ¿qué es unidad en esta clase?", "Aquello que une a varios grupos bajo un mismo Estado", "Es la definición del vocabulario."), ("En la unidad del Tawantinsuyu, ¿qué es diversidad?", "La diferencia de lenguas, creencias y costumbres", "Es la definición del vocabulario."), ("¿Qué error evita una explicación equilibrada?", "Decir que todo era uniforme", "Es uno de los errores de la clase.")],
    (
        "Escribe una tabla con dos columnas: «unidad» y «diversidad», y tres filas. En cada fila escribe un rasgo y la fuente que lo muestra (por ejemplo, un camino, una cerámica local, una crónica). Después redacta una conclusión de tres líneas que empiece con «según las fuentes…».",
        "Unidad: quechua oficial, fuente: crónicas; diversidad: cerámica local, fuente: tumbas. Según las fuentes, el Tawantinsuyu combinó unidad y diversidad.",
        ["completa seis casillas", "usa una fuente distinta en cada fila", "redacta una conclusión limitada", "no usa palabras que jerarquicen"],
        ["tabla de seis casillas y conclusión de tres líneas"],
        ["decir que fue uniforme", "no citar fuentes"],
        "Muestra tu tabla a una persona de tu casa y pídele que diga qué fila le pareció más clara.",
    ),
    "Escribe dos preguntas que una tercera fuente podría ayudar a responder.",
    "Averigua qué instrumentos o productos andinos conservan hoy elementos de la época inca.",
)

# ================================================================ clase 6
lesson(
    OA, 6,
    "Aprenderé a revisar el concepto de imperio y a decidir si sirve para describir al Tawantinsuyu. Sirve para usar las palabras históricas con cuidado.",
    ["Sé que los incas dominaron a muchos pueblos.", "Sé que una palabra puede venir de otra época o lengua."],
    [
        "Un imperio es un Estado que domina a otros pueblos o territorios y los gobierna desde un centro. La palabra viene de Roma. Los cronistas españoles llamaron «imperio» al Tawantinsuyu porque se parecía a lo que conocían: un Estado extenso, con un gobernante supremo, ejército y tributos.",
        "Algunos rasgos encajan: dominio sobre muchos pueblos, un ejército, caminos y tributos. Otros rasgos matizan: los incas se pensaban como «cuatro regiones unidas», no como un imperio, y los curacas locales conservaron poder. La mita y la reciprocidad también eran formas de relación distintas de las europeas. Por eso algunos historiadores usan imperio y otros prefieren hablar de Estado, aclarando sus rasgos.",
        "La conclusión depende de la definición que se use. Una buena práctica es explicar qué se entiende por la palabra y qué rasgos de la sociedad estudiada coinciden o no. Así se evita proyectar ideas de otra época y se respeta la forma en que ese pueblo se entendía a sí mismo.",
    ],
    [("imperio", "Estado que domina a otros pueblos o territorios desde un centro"), ("concepto", "idea general con la que se nombra algo"), ("matizar", "agregar precisiones para no generalizar"), ("anacronismo", "juzgar o describir el pasado con ideas de hoy"), ("definición", "explicación de lo que significa una palabra"), ("rasgo", "característica de algo")],
    [
        ("Probar un rasgo", "Rasgo: «dominó a muchos pueblos y cobró tributos». ¿Encaja con la definición de imperio de la clase?", ["Un imperio domina a otros pueblos.", "Cobrar tributos es una forma de dominio."], "Sí, encaja"),
        ("Probar otro rasgo", "Rasgo: «se pensaba a sí mismo como cuatro regiones unidas». ¿Encaja del todo con el término imperio?", ["Es la forma en que el Estado se nombraba.", "No es el término «imperio»."], "No del todo; matiza el concepto"),
    ],
    [
        ("Usar «imperio» sin explicar qué se entiende.", "Cada persona puede pensar en un modelo distinto, como el romano.", "Define el término antes de usarlo."),
        ("Decir que el Tawantinsuyu era igual a Roma.", "Tuvo semejanzas, pero también reciprocidad, mita y estructuras propias.", "Compara con criterios claros."),
    ],
    [
        ("¿De qué civilización viene la palabra «imperio»?", "De Roma", "La clase lo dice."),
        ("¿Qué nombre se daba el Estado inca a sí mismo?", "Tawantinsuyu", "Significa cuatro regiones unidas."),
        ("¿Qué rasgo ayuda a decir que fue un imperio: dominar a muchos pueblos o ser una aldea pequeña?", "Dominar a muchos pueblos", "Es el rasgo de la definición."),
    ],
    [
        ("¿Por qué los cronistas usaron la palabra «imperio»?", "Porque se parecía a Estados extensos que ellos conocían", "Compararon con su experiencia."),
        ("¿Qué rasgo matiza la idea de un imperio muy centralizado?", "Que los curacas locales conservaron poder", "No todo estaba controlado desde Cusco."),
        ("En la unidad del Tawantinsuyu, ¿qué es un anacronismo?", "Describir el pasado con ideas de hoy", "Es la definición del vocabulario."),
    ],
    [
        ("Un estudiante escribe: «El Tawantinsuyu fue un imperio perfecto». ¿Qué problema tiene la frase?", "Califica con «perfecto» en vez de describir rasgos", "No es un hecho comprobable."),
        ("Un estudiante escribe: «Fue un imperio porque dominó pueblos, cobró tributos y tuvo ejército, aunque los curacas conservaron poder local». ¿Qué hace bien?", "Define con rasgos y agrega un matiz", "Usa evidencia y matiza."),
        ("¿Qué pregunta debes hacer antes de usar la palabra imperio?", "¿Qué entiendo por imperio y qué rasgos tiene este Estado?", "Se define y se compara."),
    ],
    [
        ("Julia afirma: «Como los incas no usaron la palabra imperio, no pudo haber un imperio». ¿Qué objeción tiene su razonamiento?", "Que un concepto puede describir algo aunque la sociedad no lo usara, siempre que se explique", "El historiador define sus términos."),
        ("Pedro afirma: «Imperio es una palabra mala». ¿Qué error comete?", "Confunde un concepto descriptivo con un juicio moral", "Imperio describe un tipo de Estado."),
    ],
    [
        ("Ordena los pasos de un buen análisis: A) comparar con rasgos, B) definir el concepto, C) concluir con matices.", "B, A, C", "Primero se define, luego se compara y al final se concluye."),
        ("Una afirmación dice: «El Tawantinsuyu fue un imperio como el romano». ¿Qué dos diferencias de la clase puedes agregar?", "Se nombraba como cuatro regiones unidas y tenía reciprocidad y mita", "Son rasgos propios."),
    ],
    [("Una ficha de ejemplo dice: «Estado andino, cuatro regiones, caminos, curacas con poder local, tributo en trabajo». Con la definición de la clase, ¿diría que es un imperio, un Estado o puede usarse ambos términos?", "Pueden usarse ambos, explicando los rasgos", "Tiene rasgos de imperio y matices propios.")],
    [("En la unidad del Tawantinsuyu, ¿qué es un imperio?", "Un Estado que domina a otros pueblos desde un centro", "Es la definición del vocabulario."), ("¿Qué rasgo matiza el concepto de imperio en el Tawantinsuyu?", "Los curacas conservaron poder local", "Es uno de los matices."), ("¿Por qué hay que definir las palabras?", "Para evitar confusión y anacronismos", "Dos personas pueden entenderlas distinto.")],
    (
        "Escribe un texto de siete líneas con el título «¿Fue el Tawantinsuyu un imperio?». Debe contener: una definición propia de imperio, dos rasgos que encajan, un rasgo que matiza, una conclusión y un límite. Datos que puedes usar: dominio de pueblos, ejército, tributos, caminos, curacas con poder local, nombre «cuatro regiones unidas».",
        "Imperio: Estado que domina pueblos. Encajan: dominio y tributos. Matiza: curacas con poder local. Conclusión: puede llamarse imperio con matices. Límite: dependemos de crónicas.",
        ["define el concepto", "usa dos rasgos que encajan", "usa un matiz", "incluye conclusión y límite"],
        ["texto de siete líneas con cinco partes"],
        ["no definir imperio", "juzgar con palabras morales"],
        "Lee tu texto a una persona de tu casa y pídele que diga si usó la palabra imperio con cuidado.",
    ),
    "Escribe una frase que use «Estado» en lugar de «imperio» para describir al Tawantinsuyu y compárala con una que use imperio.",
    "Averigua cómo se llama hoy el Qhapaq Ñan en la lista del Patrimonio Mundial y qué países participan.",
)
