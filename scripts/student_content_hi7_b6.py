"""Cuaderno del estudiante, 7.º básico Historia, Geografía y Ciencias Sociales: OA 16 (confluencia de legados en América Latina)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI07 OA 16"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a reconocer las raíces indígenas, griegas, romanas y europeas que se mezclan en la cultura latinoamericana de hoy. Sirve para ver que una misma costumbre puede tener varias fuentes.",
    ["Sé que mayas, aztecas e incas dejaron legados.", "Sé que Grecia y Roma influyeron en Europa."],
    [
        "La cultura latinoamericana actual es el resultado de un encuentro de tradiciones. Las civilizaciones maya, azteca e inca dejaron lenguas, alimentos, técnicas agrícolas y creencias. Grecia aportó ideas como democracia y filosofía, y muchas palabras científicas. Roma dejó el latín, de donde viene el español, además de ideas de derecho y república. Desde 1492 llegaron además la lengua, la religión y las instituciones de España y Portugal, y, forzadamente, personas africanas que también aportaron música, comidas y lenguas.",
        "Un ejemplo claro es el idioma. El español viene del latín, pero incorpora palabras indígenas como tomate, cóndor y papa, y palabras griegas como democracia. Otro es la comida: el maíz y la papa son americanos; el trigo y el aceite de oliva son del Mediterráneo. En la plaza de una ciudad se combinan la plaza romana y española con ferias y mercados de origen indígena.",
        "Al identificar una raíz hay que ser cuidadoso. Una costumbre puede tener varios orígenes y puede haber cambiado con el tiempo. Además, no todas las raíces llegaron en condiciones iguales: algunas se impusieron, otras se mezclaron y otras sobrevivieron resistiendo. Por eso se habla de confluencia, no de una simple suma.",
    ],
    [("confluencia", "unión de varias corrientes o tradiciones en un mismo lugar"), ("legado", "herencia cultural que dejó un pueblo"), ("raíz cultural", "origen histórico de una costumbre o expresión"), ("latín", "lengua de los romanos, base del español"), ("filosofía", "reflexión sobre el ser humano, el conocimiento y el mundo, desarrollada en Grecia"), ("mestizaje cultural", "mezcla de tradiciones de distintos orígenes")],
    [
        ("Rastrear una palabra", "La palabra «democracia» viene del griego. ¿Qué raíz cultural muestra: griega, romana o indígena americana?", ["Se dice que viene del griego.", "La raíz es griega."], "Griega"),
        ("Rastrear un alimento", "El maíz y la papa fueron cultivados antes de 1492 en América. ¿De qué raíz son: indígena americana o mediterránea?", ["Antes de 1492 en América.", "Son indígenas americanos."], "Indígena americana"),
    ],
    [
        ("Pensar que la cultura latinoamericana tiene un solo origen.", "Es una confluencia de raíces indígenas, europeas, africanas, griegas y romanas.", "Pregunta qué parte viene de cada tradición."),
        ("Creer que todas las mezclas fueron pacíficas.", "Algunas se impusieron, otras se mezclaron y otras sobrevivieron resistiendo.", "Pregunta cómo llegó cada elemento."),
    ],
    [
        ("¿De qué lengua viene el español?", "Del latín", "El latín es la lengua de los romanos."),
        ("¿De qué raíz es la palabra «tomate»?", "Indígena americana", "Viene del náhuatl."),
        ("¿Qué idea política griega usamos hoy?", "La democracia", "La palabra y la idea vienen de Grecia."),
    ],
    [
        ("En la unidad de legados latinoamericanos, ¿qué es una raíz cultural?", "El origen histórico de una costumbre o expresión", "Es la definición del vocabulario."),
        ("Nombra un alimento de origen mediterráneo y uno de origen americano.", "Mediterráneo: trigo o aceite de oliva; americano: maíz o papa", "Están en la explicación."),
        ("¿Por qué se habla de «confluencia» y no de «suma»?", "Porque las tradiciones se mezclaron, se impusieron o resistieron y no solo se juntaron", "Hubo procesos desiguales."),
    ],
    [
        ("Una ficha de ejemplo dice: «En una plaza se venden choclos y se levanta una iglesia con columnas». ¿Qué dos raíces muestra?", "Una americana (choclo) y una europea o romana (iglesia con columnas)", "Combina alimento americano con arquitectura europea."),
        ("La palabra «república» viene del latín. ¿Qué civilización antigua la usó primero?", "Roma", "Es una palabra romana."),
        ("Un abuelo de ejemplo cocina pan de trigo con pebre de ají. ¿Cuál ingrediente es de origen mediterráneo y cuál americano?", "Trigo mediterráneo; ají americano", "El trigo llegó con los europeos; el ají es americano."),
    ],
    [
        ("Lucía dice: «El español es una lengua exclusivamente romana». ¿Qué corrección haces?", "Viene del latín, pero tiene palabras indígenas, árabes y de otras lenguas", "Una lengua incorpora aportes de otros pueblos."),
        ("¿Por qué no basta decir «todas las raíces son iguales de importantes»?", "Porque algunas se impusieron y otras fueron relegadas aunque hoy se reconozcan", "Hubo desigualdad en el encuentro."),
    ],
    [
        ("Ordena por antigüedad aproximada de su origen: A) democracia griega, B) lengua castellana en América, C) cultivo de maíz en Mesoamérica.", "C, A, B", "El cultivo del maíz es muy antiguo, la democracia griega es anterior a Roma y el castellano llegó en el siglo XV."),
        arith("El español llegó a América en 1492. ¿Cuántos años han pasado hasta 2026?", "2026-1492", "Se resta el año de llegada al año actual."),
    ],
    [("Una lista de ejemplo de palabras: tomate, república, cóndor, democracia, papa. ¿Cuántas son de origen americano?", "Tres: tomate, cóndor y papa", "Las otras dos son de raíz grecolatina.")],
    [("En la unidad de legados latinoamericanos, ¿qué es un legado?", "Una herencia cultural que dejó un pueblo", "Es la definición del vocabulario."), ("¿Qué raíz tiene la palabra «democracia»?", "Griega", "Viene del griego."), ("¿Por qué se habla de confluencia?", "Porque varias tradiciones se mezclaron con desigualdad", "No fue una simple suma.")],
    (
        "Elige tres elementos de esta lista y escribe sus raíces: pan de trigo, palta (aguacate), plaza central, la palabra «senado», una canción con quena, el tomate. Para cada uno indica raíz principal, cómo llegó o se mezcló, y una duda.",
        "Palta: raíz americana; los pueblos andinos la cultivaban; duda: cómo cambió su cultivo con el tiempo.",
        ["elige tres elementos", "identifica una raíz razonable", "explica cómo llegó o se mezcló", "formula una duda"],
        ["tres fichas con raíz, cómo llegó y duda"],
        ["asignar un único origen", "olvidar la duda"],
        "Muestra tus fichas a una persona de tu casa y pídele que agregue otra raíz posible.",
    ),
    "Anota tres palabras que uses y averigua si vienen del latín, del griego o de una lengua indígena.",
    "Investiga qué aportes africanos hay en la música o en las comidas de América Latina.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a rastrear una expresión cultural latinoamericana usando fuentes. Sirve para pasar de «creo que viene de…» a «lo muestra tal fuente».",
    ["Sé reconocer raíces culturales.", "Sé que una fuente tiene límites."],
    [
        "Rastrear una expresión cultural significa seguir su historia: qué es hoy, qué rasgos tiene y de dónde pueden venir. Seguimos cinco pasos. Primero, describir la expresión: qué se hace, quién participa, cuándo. Segundo, identificar rasgos que parecen de una tradición (por ejemplo, un instrumento andino, un ritual cristiano). Tercero, buscar fuentes que lo confirmen: crónicas, objetos, testimonios de comunidades. Cuarto, contrastar. Quinto, escribir un límite.",
        "Un ejemplo: la fiesta de La Tirana, en el norte de Chile, se celebra en julio, con bailes religiosos y devoción a la Virgen del Carmen. Tiene rasgos católicos, como la procesión y la devoción, y rasgos andinos, como la música de bronces y quenas y los bailes de comparsa, que vienen de tradiciones anteriores. Otro ejemplo es el Día de Muertos en México, que reúne ofrendas y flores con fechas del calendario católico: el 1 y 2 de noviembre.",
        "Las fuentes son varias: relatos de los participantes, imágenes, documentos de la Iglesia, estudios arqueológicos y entrevistas. Cada una responde preguntas distintas. Un buen rastreo no afirma más de lo que prueban las fuentes, y reconoce que una misma expresión puede haber cambiado desde su origen.",
    ],
    [("expresión cultural", "forma en que un grupo comparte sus tradiciones, como una fiesta, una danza o una comida"), ("devoción", "respeto y cariño hacia una figura religiosa"), ("procesión", "desfile religioso por las calles"), ("comparsa", "grupo de bailarines que actúa en una fiesta"), ("ofrenda", "objetos y alimentos que se ponen en recuerdo de los difuntos o de un dios"), ("testimonio", "relato de una persona sobre algo que vivió")],
    [
        ("Describir primero", "Una ficha de ejemplo dice: «En julio miles de personas bailan en procesión hacia una iglesia con música de bronces». ¿Qué paso del rastreo es leer esta descripción?", ["Es el primer paso.", "Es describir la expresión."], "Describir la expresión"),
        ("Identificar un rasgo", "Si el baile usa una quena (flauta andina), ¿qué raíz sugiere ese rasgo?", ["La quena es un instrumento andino.", "Un instrumento andino sugiere una raíz andina o indígena."], "Una raíz andina o indígena"),
    ],
    [
        ("Afirmar el origen sin fuente.", "Un origen se prueba con fuentes, no con una sensación.", "Escribe qué fuente lo apoya."),
        ("Creer que una expresión no cambia.", "Las expresiones se transforman con el tiempo y con quienes participan.", "Compara épocas."),
    ],
    [
        ("¿Cuántos pasos tiene el rastreo de la clase?", "Cinco", "Son describir, identificar rasgos, buscar fuentes, contrastar y escribir un límite."),
        ("¿En qué mes se celebra la fiesta de La Tirana, según la clase?", "Julio", "La explicación lo indica."),
        ("¿En qué fechas se celebra el Día de Muertos que menciona la clase?", "El 1 y 2 de noviembre", "La explicación lo indica."),
    ],
    [
        ("En la unidad de legados latinoamericanos, ¿qué es una comparsa?", "Un grupo de bailarines que actúa en una fiesta", "Es la definición del vocabulario."),
        ("¿Qué rasgos católicos tiene La Tirana según la clase?", "La procesión y la devoción a la Virgen del Carmen", "La clase los menciona."),
        ("¿Qué tipo de fuente es el relato de una persona que participa en una fiesta?", "Un testimonio", "Es la definición del vocabulario."),
    ],
    [
        ("Una ficha de ejemplo dice: «Se colocan flores, comida y fotos en una mesa el 2 de noviembre». ¿Qué paso del rastreo es nombrar las fechas del calendario católico?", "Identificar rasgos de una tradición", "Las fechas muestran un rasgo cristiano."),
        ("Un historiador de ejemplo afirma: «Esa fiesta es solo católica». Cita un rasgo de la clase que lo matiza.", "La música de bronces y quenas y los bailes de comparsa tienen raíz andina", "Hay raíces mezcladas."),
        ("Un estudiante quiere confirmar el origen de un baile. ¿Qué fuente de la clase puede usar además de libros: un testimonio de participantes o una lista de precios de entradas?", "Un testimonio de participantes", "Es evidencia directa de quien participa."),
    ],
    [
        ("Pedro dice: «Como es una fiesta católica, no tiene raíces indígenas». ¿Qué error comete?", "Piensa que una fiesta solo puede tener un origen", "Las expresiones pueden mezclar raíces."),
        ("Ana escribe: «Esta danza viene de los incas». ¿Qué límite deberías agregar?", "Que se necesitan fuentes que lo confirmen y que la danza ha cambiado", "No se puede afirmar un origen exacto sin evidencia."),
    ],
    [
        ("Ordena los pasos del rastreo: A) buscar fuentes, B) escribir un límite, C) describir la expresión, D) identificar rasgos, E) contrastar.", "C, D, A, E, B", "Es el orden de los cinco pasos."),
        ("Un estudiante concluye: «La fiesta tiene raíces cristianas y andinas». ¿Qué dos rasgos de la clase apoyan esa conclusión?", "Procesión y devoción a la Virgen del Carmen; quenas y bailes de comparsa", "Un rasgo por cada raíz."),
    ],
    [("Un vecino de ejemplo cuenta: «En mi pueblo ponemos una mesa con fruta y pan el 2 de noviembre para recordar a los que murieron». ¿Qué tipo de fuente es y qué falta para estar seguros del origen?", "Un testimonio; faltan otras fuentes que confirmen el origen", "Un solo relato no basta.")],
    [("¿Cuál es el primer paso para rastrear una expresión?", "Describirla", "Se parte por observar qué es."), ("En la unidad de legados latinoamericanos, ¿qué es un testimonio?", "El relato de una persona sobre algo que vivió", "Es la definición del vocabulario."), ("¿Por qué hay que escribir un límite?", "Para no afirmar más de lo que prueban las fuentes", "Así se evitan las exageraciones.")],
    (
        "Elige una de estas expresiones y rastréala con los cinco pasos: A) fiesta de La Tirana; B) Día de Muertos en México. Escribe una ficha con descripción, dos rasgos y su posible raíz, una fuente que usarías, una comparación con otra fuente y un límite.",
        "B: se ponen ofrendas y flores; rasgos: ofrendas (raíz mesoamericana) y fechas (calendario católico); fuente: testimonios; límite: la fiesta cambió.",
        ["describe la expresión", "señala dos rasgos con raíces distintas", "propone una fuente", "incluye un límite"],
        ["ficha con cinco partes"],
        ["asignar una sola raíz", "no proponer fuente"],
        "Muestra tu ficha a una persona de tu casa y pídele que diga qué testimonio agregaría.",
    ),
    "Escribe una pregunta que le harías a una comunidad sobre una fiesta tradicional.",
    "Averigua qué fiestas religiosas con baile existen en tu región.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a examinar cambios, apropiaciones y resistencias en la cultura latinoamericana. Sirve para entender que el patrimonio se transforma, se usa o se defiende.",
    ["Sé rastrear una expresión cultural.", "Sé que las mezclas no siempre son entre iguales."],
    [
        "Una tradición cambia cuando se mezcla con otras. Este proceso se llama sincretismo: por ejemplo, ceremonias indígenas que se mantienen junto a fiestas cristianas. Otras veces hay apropiación, cuando alguien usa elementos de una cultura sin reconocerla o sin su permiso, por ejemplo una empresa que copia un diseño textil de una comunidad. También hay resistencia, cuando un pueblo mantiene su lengua o sus ceremonias aunque se las prohíban o las desprecien.",
        "En América Latina hubo presiones para abandonar lenguas y costumbres indígenas, pero muchas comunidades las defendieron. Por eso hoy se hablan el quechua, el aimara, el mapudungun y las lenguas mayas, y se enseñan en algunas escuelas. Al mismo tiempo, algunos símbolos indígenas se usan en el comercio o el turismo, a veces sin beneficiar a las comunidades.",
        "Para analizar un caso se pregunta: quién crea o usa la expresión, quién se beneficia, si hay permiso y cuál es la mirada de la comunidad. No se trata de juzgar toda mezcla como mala. Muchas son creativas y valoradas. La clave es el respeto y la participación de quienes son parte de la tradición.",
    ],
    [("sincretismo", "mezcla de creencias o prácticas de distintas tradiciones"), ("apropiación cultural", "uso de elementos de una cultura sin reconocerla o sin su permiso"), ("resistencia cultural", "defensa de la lengua y las costumbres propias"), ("comunidad", "grupo de personas que comparten territorio, historia o tradiciones"), ("patrimonio", "bienes y tradiciones que un grupo quiere conservar"), ("beneficio", "ganancia o ventaja que alguien obtiene")],
    [
        ("Clasificar un caso", "Una comunidad mantiene su lengua en la escuela aunque durante años se le dijo que no la usara. ¿Es sincretismo, apropiación o resistencia?", ["Mantiene su lengua pese a presiones.", "Es resistencia."], "Resistencia cultural"),
        ("Clasificar otro caso", "Una empresa copia el diseño de un tejido de una comunidad y lo vende sin pedir permiso. ¿Qué es?", ["Usa un elemento de otra cultura.", "No hay permiso.", "Es apropiación."], "Apropiación cultural"),
    ],
    [
        ("Pensar que toda mezcla es apropiación.", "Hay mezclas creativas y respetuosas con participación de la comunidad.", "Pregunta si hay permiso y quién se beneficia."),
        ("Creer que la resistencia solo ocurre con armas.", "También se resiste manteniendo la lengua, la música y las ceremonias.", "Piensa en prácticas cotidianas."),
    ],
    [
        ("¿Cómo se llama la mezcla de creencias de distintas tradiciones?", "Sincretismo", "Es la definición del vocabulario."),
        ("¿Cómo se llama la defensa de la lengua y las costumbres propias?", "Resistencia cultural", "Es la definición del vocabulario."),
        ("¿Cuál de estas lenguas no es indígena americana: mapudungun, quechua o latín?", "Latín", "El latín es la lengua de los romanos; las otras dos son indígenas."),
    ],
    [
        ("¿Qué pregunta ayuda a evaluar una apropiación?", "Si hay permiso y quién se beneficia", "La clase lo propone."),
        ("¿Por qué la participación de la comunidad es clave?", "Porque ella es parte de la tradición y puede decidir cómo se usa", "Evita que otros la usen sin respeto."),
        ("¿Qué ejemplo de sincretismo menciona la clase?", "Ceremonias indígenas que se mantienen junto a fiestas cristianas", "Está en la explicación."),
    ],
    [
        ("Un diseñador de ejemplo trabaja con tejedoras de una comunidad, les paga y escribe su nombre en la etiqueta. ¿Es apropiación o colaboración?", "Colaboración", "Hay permiso, pago y reconocimiento."),
        ("Una escuela de ejemplo enseña quechua a los estudiantes de la zona. ¿Qué proceso favorece?", "La resistencia o conservación cultural", "Fortalece la lengua."),
        ("Una fiesta de ejemplo tiene misa y también bailes con música andina. ¿Qué proceso muestra?", "Sincretismo", "Mezcla elementos de dos tradiciones."),
    ],
    [
        ("Luis dice: «Toda mezcla cultural es mala». Da un argumento en contra.", "Hay mezclas creativas y respetuosas hechas con la participación de la comunidad", "La clase advierte que no se trata de juzgar toda mezcla."),
        ("Marta dice: «Si un símbolo es bonito, cualquiera puede usarlo». ¿Qué le responderías?", "Hay que preguntar a la comunidad, reconocerla y compartir beneficios", "El respeto y el permiso importan."),
    ],
    [
        ("Ordena de menos a más respetuoso: A) copiar sin permiso, B) usar con permiso y pagar, C) usar con permiso y dar reconocimiento y pago.", "A, B, C", "A no pide permiso, B paga y C además reconoce."),
        ("Un caso de ejemplo: «Una comunidad recibe un pago justo, aprueba el diseño y se la nombra como autora». ¿Cuántas condiciones de respeto de la clase cumple: permiso, beneficio y reconocimiento?", "Tres", "Cumple las tres."),
    ],
    [("Una marca de ropa de ejemplo usa dibujos de un pueblo sin avisarle. La marca gana dinero y el pueblo no. ¿Qué dos preguntas de la clase muestran el problema?", "¿Hay permiso? y ¿quién se beneficia?", "No hubo permiso y el beneficio fue solo de la marca.")],
    [("En la unidad de legados latinoamericanos, ¿qué es apropiación cultural?", "Usar elementos de una cultura sin reconocerla o sin su permiso", "Es la definición del vocabulario."), ("En la unidad de legados latinoamericanos, ¿qué es resistencia cultural?", "Defender la lengua y las costumbres propias", "Es la definición del vocabulario."), ("En la unidad de legados latinoamericanos, ¿qué es sincretismo?", "La mezcla de creencias o prácticas de distintas tradiciones", "Es la definición del vocabulario.")],
    (
        "Lee estos tres casos de ejemplo: A) una radio comunitaria transmite en una lengua indígena; B) una tienda vende ropa con diseños tradicionales sin avisar a la comunidad; C) una fiesta mezcla misa con danzas andinas. Para cada uno escribe si es resistencia, apropiación o sincretismo, y una pregunta que harías a la comunidad.",
        "A: resistencia; pregunta: ¿qué programas quieren transmitir? B: apropiación; ¿les gustaría participar? C: sincretismo; ¿cómo viven la fiesta?",
        ["clasifica los tres casos", "formula una pregunta para cada uno", "usa un tono respetuoso", "evita juzgar a las personas"],
        ["tres clasificaciones con tres preguntas"],
        ["llamar apropiación a todo", "no formular preguntas"],
        "Léele tus preguntas a una persona de tu casa y pídele que diga si suenan respetuosas.",
    ),
    "Escribe dos formas de reconocer a una comunidad cuando se usa una expresión suya.",
    "Averigua si en tu comuna se enseña una lengua indígena y dónde.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a relacionar el patrimonio con la vida presente de América Latina. Sirve para entender qué se cuida hoy, quién lo cuida y por qué.",
    ["Sé que hay legados indígenas, grecorromanos y europeos.", "Sé que las comunidades pueden defender su cultura."],
    [
        "El patrimonio es el conjunto de bienes y tradiciones que un grupo quiere cuidar y transmitir. Puede ser material, como un edificio, un camino o un sitio arqueológico, o inmaterial, como una lengua, una fiesta o una forma de tejer. Cada país y comunidad decide qué cuidar; también existen listas internacionales, como el Patrimonio Mundial de la UNESCO.",
        "Hay ejemplos que combinan legados. El Qhapaq Ñan, el camino inca, fue declarado Patrimonio Mundial en 2014 con seis países, entre ellos Chile. Las iglesias de madera de Chiloé, declaradas en 2000, muestran la mezcla de arquitectura europea y trabajo local en madera. En muchas ciudades latinoamericanas el trazado en cuadrícula con una plaza central tiene raíces romanas y españolas, y los mercados y las ferias conservan formas indígenas de intercambio.",
        "Cuidar el patrimonio hoy implica decisiones: quién lo mantiene, con qué recursos, para qué público y con qué voz de la comunidad. Hay beneficios, como el turismo, y riesgos, como la masificación o el olvido. Un buen proyecto de patrimonio escucha a la comunidad y se pregunta qué quiere conservar y cómo.",
    ],
    [("patrimonio material", "bienes que se pueden tocar, como edificios o caminos"), ("patrimonio inmaterial", "tradiciones vivas, como lenguas, fiestas o técnicas"), ("UNESCO", "organización internacional que declara sitios Patrimonio Mundial"), ("conservar", "cuidar para que algo no se pierda"), ("turismo", "viaje de personas para conocer lugares"), ("masificación", "llegada de demasiada gente a un lugar")],
    [
        ("Clasificar patrimonio", "Una técnica de tejido que se enseña de abuelas a nietas, ¿es patrimonio material o inmaterial?", ["No es un objeto fijo.", "Es una tradición viva."], "Inmaterial"),
        ("Clasificar otro bien", "Un camino empedrado inca, ¿es patrimonio material o inmaterial?", ["Se puede tocar.", "Es material."], "Material"),
    ],
    [
        ("Pensar que patrimonio es solo lo antiguo y de piedra.", "También incluye lenguas, fiestas y técnicas vivas.", "Pregunta si es material o inmaterial."),
        ("Creer que declarar un sitio lo protege solo.", "Se necesitan recursos, planes y participación de la comunidad.", "Pregunta quién lo cuida."),
    ],
    [
        ("¿En qué año fue declarado Patrimonio Mundial el Qhapaq Ñan?", "2014", "La explicación da ese año."),
        ("¿Qué iglesias de madera de Chile fueron declaradas en 2000?", "Las de Chiloé", "La explicación las menciona."),
        ("¿Qué organización declara Patrimonio Mundial?", "La UNESCO", "Está en el vocabulario."),
    ],
    [
        ("¿Qué mezcla muestran las iglesias de Chiloé?", "Arquitectura europea y trabajo local en madera", "La clase lo explica."),
        ("En la unidad de legados latinoamericanos, ¿qué es patrimonio inmaterial?", "Tradiciones vivas como lenguas, fiestas o técnicas", "Es la definición del vocabulario."),
        ("Nombra un beneficio y un riesgo del turismo en un sitio patrimonial.", "Beneficio: ingresos; riesgo: masificación", "Están en la explicación."),
    ],
    [
        arith("El Qhapaq Ñan fue declarado Patrimonio Mundial en 2014. ¿Cuántos años pasaron hasta 2026?", "2026-2014", "Se resta el año de declaración al año actual."),
        ("Un pueblo de ejemplo tiene una fiesta de 300 años que mezcla bailes indígenas con una procesión católica. ¿Qué tipo de patrimonio es y qué mezcla muestra?", "Inmaterial; mezcla de tradiciones indígenas y cristianas", "Es una tradición viva con raíces distintas."),
        ("Un sitio de ejemplo recibe 5.000 visitantes diarios y su suelo se desgasta. ¿Qué riesgo de la clase se presenta?", "La masificación", "Demasiada gente daña el lugar."),
    ],
    [
        ("Julia dice: «El patrimonio pertenece solo al Estado». ¿Qué le falta considerar?", "La voz y la participación de la comunidad", "La comunidad cuida y vive el patrimonio."),
        ("¿Por qué un sitio puede ser a la vez beneficio y riesgo?", "Porque el turismo da ingresos, pero puede dañar el lugar si hay demasiada gente", "Ambos efectos pueden coexistir."),
    ],
    [
        ("Ordena el proceso de un proyecto patrimonial: A) ejecutar, B) escuchar a la comunidad, C) evaluar resultados.", "B, A, C", "Primero se escucha, luego se ejecuta y al final se evalúa."),
        ("Una lista de ejemplo: lengua mapuche, camino inca, fiesta de La Tirana, iglesia de madera. ¿Cuántos son patrimonio inmaterial?", "Dos: lengua mapuche y fiesta de La Tirana", "Camino e iglesia son materiales."),
    ],
    [("Una comunidad de ejemplo quiere cuidar un camino antiguo y también la fiesta que se hace allí. ¿Qué dos tipos de patrimonio incluye?", "Material (camino) e inmaterial (fiesta)", "Combina un bien físico y una tradición viva.")],
    [("En la unidad de legados latinoamericanos, ¿qué es el patrimonio?", "Los bienes y tradiciones que un grupo quiere cuidar y transmitir", "Es la definición de la explicación."), ("¿Cuál es un ejemplo de patrimonio inmaterial?", "Una lengua, una fiesta o una forma de tejer", "Son tradiciones vivas."), ("¿Por qué escuchar a la comunidad?", "Porque ella vive y cuida el patrimonio", "Su voz es clave.")],
    (
        "Elige un patrimonio de esta lista: la lengua mapuche, el camino inca o las iglesias de Chiloé. Escribe un plan de seis líneas con: tipo de patrimonio, qué legados muestra, un beneficio, un riesgo y una acción concreta para cuidarlo con la comunidad.",
        "Iglesias de Chiloé: patrimonio material; muestra arquitectura europea y madera local; beneficio: turismo; riesgo: desgaste; acción: planificar visitas con la comunidad.",
        ["clasifica el tipo", "señala legados", "menciona un beneficio y un riesgo", "propone una acción con la comunidad"],
        ["plan de seis líneas con cinco partes"],
        ["no incluir a la comunidad", "decir que declarar basta"],
        "Cuéntale tu plan a una persona de tu casa y pídele que diga qué acción agregaría.",
    ),
    "Anota un patrimonio de tu región y si es material o inmaterial.",
    "Averigua qué sitios de Chile son Patrimonio Mundial y a qué tipo pertenecen.",
)
