"""Material del estudiante de 7.º básico, Historia, Geografía y Ciencias Sociales: OA 07 (civilización romana y legado mediterráneo)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI07 OA 07"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (cronología resumida, hecha para este cuaderno). "
     "753 a. C.: fecha tradicional de la fundación de Roma, que mezcla leyenda e historia. "
     "509 a. C.: comienza la República, con cargos elegidos por un año, como dos cónsules, y un Senado. "
     "264 a. C. a 146 a. C.: guerras de Roma contra Cartago; en 146 a. C. Cartago es destruida. "
     "27 a. C.: Augusto se convierte en el primer emperador. "
     "395 d. C.: el Imperio se divide en una parte de Occidente y otra de Oriente. "
     "476 d. C.: termina el Imperio romano de Occidente; el de Oriente continúa. "
     "Factores de la expansión: un ejército organizado, alianzas con otras ciudades de Italia, ofrecer derechos de ciudadanía a algunos pueblos, fundar colonias y el comercio.")
build(
    OA, 1, F,
    use="Aprenderé a distinguir república, expansión e imperio en la historia de Roma. Sirve para ubicar cada etapa y no mezclar sus rasgos.",
    prior=["Sé comparar años a. C.", "Sé qué es una ciudad-Estado.", "Sé qué es un Estado."],
    explain=[
        "Roma comenzó como una ciudad en Italia y, con el tiempo, dominó todo el Mediterráneo. Su historia se suele dividir en etapas. En la República, desde 509 a. C., los cargos eran elegidos por un año, como los dos cónsules, y había un Senado. En el Imperio, desde 27 a. C., un emperador concentraba el poder.",
        "Durante la República ocurrió gran parte de la expansión: Roma se extendió por Italia y luego por el Mediterráneo, y el Imperio llegó a ser aún más extenso. Las guerras contra Cartago, entre 264 y 146 a. C., fueron una de las más importantes. La expansión no se explica solo por el ejército: también influyeron las alianzas con otras ciudades, los derechos de ciudadanía que se ofrecían, las colonias y el comercio.",
        "El Imperio cambió con el tiempo. En 395 d. C. se dividió en Occidente y Oriente, y en 476 d. C. terminó el de Occidente, mientras el de Oriente siguió existiendo. Por eso no es correcto hablar de «el fin de Roma» como si todo hubiera desaparecido. Los años a. C. se cuentan hacia atrás y los d. C. hacia adelante.",
    ],
    vocab=[("república", "gobierno con cargos elegidos por tiempo limitado y un Senado"), ("cónsul", "magistrado romano elegido por un año; había dos"), ("emperador", "gobernante con gran poder en el Imperio romano"), ("expansión", "crecimiento del territorio controlado por un Estado"), ("Senado", "asamblea de ciudadanos importantes que aconsejaba y controlaba a los magistrados")],
    worked=[
        ("Calcular una duración", "{F} ¿Cuántos años duró la República, de 509 a 27 a. C.?", ["Los años a. C. se restan: 509 − 27.", "El resultado es 482."], "482 años"),
        ("Identificar una etapa", "Un gobernante con gran poder, que se llama emperador, ¿corresponde a la República o al Imperio?", ["La República tenía cónsules elegidos por un año.", "El emperador es propio del Imperio."], "Al Imperio"),
    ],
    mistakes=[("Decir que Roma fue siempre un imperio.", "Se mira solo la etapa más conocida.", "Antes del Imperio hubo una República de casi cinco siglos."),
              ("Explicar la expansión solo por la fuerza del ejército.", "Se ignoran las alianzas, la ciudadanía y el comercio.", "Nombra varios factores combinados.")],
    T=[
        ("{F} ¿Cuántos cónsules había en la República?", "2", "La ficha dice que había dos cónsules."),
        ("{F} ¿Cuánto duraba el cargo de cónsul?", "Un año", "La ficha lo indica."),
        ("{F} ¿Quién fue el primer emperador?", "Augusto", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años separan el comienzo de las guerras contra Cartago (264 a. C.) de la destrucción de Cartago (146 a. C.)?", "264-146", "Se restan los años a. C.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la división del Imperio y el fin del Imperio de Occidente?", "476-395", "Se restan los años d. C.", " años"),
        ("{F} Ordena de más antiguo a más reciente: fin del Imperio de Occidente, comienzo de la República, destrucción de Cartago.", "Comienzo de la República, destrucción de Cartago, fin del Imperio de Occidente", "Las fechas son 509 a. C., 146 a. C. y 476 d. C."),
        ("{F} Clasifica como propio de la República (R) o del Imperio (I): 1) dos cónsules elegidos por un año; 2) un emperador con gran poder; 3) un Senado que controlaba a los magistrados.", "1 R, 2 I, 3 R", "Cónsules y Senado son de la República; el emperador del Imperio."),
        ("=", "{F} ¿Cuántos años pasaron entre la fundación tradicional de Roma, en 753 a. C., y el comienzo de la República, en 509 a. C.?", "753-509", "Se restan los años a. C.", " años"),
        ("{F} ¿Qué parte del Imperio continuó existiendo después de 476 d. C.?", "El Imperio de Oriente", "La ficha lo indica."),
        ("{F} Pedro dice: «Roma fue siempre un imperio». Corrígelo con dos fechas de la ficha.", "Primero fue república desde 509 a. C. y solo en 27 a. C. se convirtió en imperio con Augusto", "Hubo una República antes del Imperio."),
        ("{F} Ana afirma que Roma se expandió solo por su ejército. Nombra dos factores de la ficha que muestren que no.", "Por ejemplo: alianzas con ciudades de Italia y derechos de ciudadanía para algunos pueblos", "La ficha nombra varios factores."),
        ("{F} ¿Por qué no es exacto decir que Roma «desapareció» en 476 d. C.?", "Porque terminó el Imperio de Occidente, pero el de Oriente continuó", "Fue el fin de una parte."),
        ("{F} ¿Qué fecha de la ficha es más reciente: 509 a. C. o 395 d. C.? Explica.", "395 d. C., porque es después de Cristo", "Los años d. C. son posteriores a los a. C."),
    ],
    ctx=("Un afiche de un museo muestra una línea de tiempo de Roma que empieza con un emperador. ¿Qué etapa anterior omite y desde qué año? {F}", "La República, desde 509 a. C.", "Antes de Augusto hubo cinco siglos de república."),
    sc=[("¿Qué era un cónsul?", "Un magistrado romano elegido por un año; había dos", "Es un cargo propio de la República."),
        ("¿En qué año comenzó el Imperio, según la ficha?", "En 27 a. C.", "Comenzó con Augusto como primer emperador."),
        ("=", "{F} ¿Cuántos años duró la fase final del Imperio de Occidente entre 395 d. C. y 476 d. C.?", "476-395", "Se restan los años d. C.", " años")],
    op=("Dibuja una línea de tiempo de Roma con las seis fechas de la ficha. Pinta la República y el Imperio de colores distintos, marca con una barra las guerras contra Cartago y escribe una frase que explique la expansión con dos factores. {F}",
        "Líneas con 753 a. C., 509 a. C., 264–146 a. C., 27 a. C., 395 d. C. y 476 d. C., con colores para República e Imperio, la barra de las guerras contra Cartago y la frase de dos factores.",
        ["respeta el orden de las fechas", "distingue República e Imperio por color y marca las guerras contra Cartago", "la frase usa dos factores"], ["línea de tiempo dibujada", "frase escrita"], ["ordenar mal los años a. C.", "explicar la expansión con un solo factor"],
        "Pide que explique qué etapa le parece más larga y por qué."),
    reinforce="Nombra en voz alta tres etapas de Roma y un rasgo de cada una.",
    extend="Escribe una pregunta sobre cómo cambió la vida de las personas al pasar de república a imperio.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (resumen hecho para este cuaderno; las cifras de la provincia son de ejemplo). "
     "Las Doce Tablas, de hacia 450 a. C., fueron las primeras leyes escritas de Roma y se exhibieron en el Foro para que todos pudieran conocerlas. "
     "El derecho romano se ocupó, entre otras cosas, de las personas, la propiedad y los contratos (acuerdos entre personas). "
     "Roma gobernó los territorios que conquistó dividiéndolos en provincias. Cada provincia tenía un gobernador que cobraba impuestos y resolvía juicios. Muchas ciudades locales mantenían sus propios consejos. "
     "Provincia de ejemplo: 20 ciudades, cada una paga 100 monedas de impuesto al año. "
     "El Código Civil de Chile, escrito por Andrés Bello y promulgado en 1855, se inspira en parte en el derecho romano.")
build(
    OA, 2, F,
    use="Aprenderé a relacionar el derecho romano con la administración de las provincias. Sirve para entender cómo Roma gobernaba un territorio tan grande.",
    prior=["Sé qué es un Estado y qué es el tributo.", "Sé qué fue la República y el Imperio.", "Sé multiplicar con números pequeños."],
    explain=[
        "Un territorio tan grande necesitaba reglas y organización. El derecho romano comenzó con las Doce Tablas, hacia 450 a. C., primeras leyes escritas, que se exhibieron en el Foro para que todos las conocieran. Una ley escrita y pública limita la arbitrariedad: todos saben qué se puede hacer y qué no.",
        "Con el tiempo, el derecho romano reguló la propiedad, los contratos y las personas. También cambió: se agregaron normas y se adaptaron a nuevas situaciones. Para administrar lo conquistado, Roma lo dividió en provincias, con un gobernador que cobraba impuestos y resolvía juicios. Muchas ciudades locales conservaban sus propios consejos.",
        "El legado del derecho romano llegó hasta hoy, pero no como una copia intacta. El Código Civil de Chile, escrito por Andrés Bello y promulgado en 1855, se inspira en parte en esa tradición, y también en otras fuentes. Un legado es lo que una sociedad recibe de otra y adapta a su propia época.",
    ],
    vocab=[("provincia", "territorio conquistado por Roma, gobernado por un funcionario"), ("gobernador", "funcionario que mandaba una provincia"), ("contrato", "acuerdo entre personas con obligaciones para ambas"), ("ley escrita", "norma puesta por escrito para que todos la conozcan"), ("legado", "lo que una sociedad recibe de otra y adapta")],
    worked=[
        ("Calcular impuestos", "{F} ¿Cuánto recibe Roma en un año de las 20 ciudades?", ["Cada ciudad paga 100 monedas.", "Multiplico: 20 × 100 = 2.000."], "2.000 monedas"),
        ("Explicar un propósito", "{F} ¿Para qué sirve exhibir las leyes en el Foro?", ["El Foro era un lugar público.", "Así todos podían conocerlas."], "Para que todos conocieran las leyes"),
    ],
    mistakes=[("Creer que el derecho romano nunca cambió.", "Se piensa en las Doce Tablas como el único derecho romano.", "Cambió durante siglos, con nuevas normas."),
              ("Decir que el Código Civil chileno es una copia del derecho romano.", "Se confunde inspiración con copia.", "Se inspira en parte en esa tradición y en otras fuentes.")],
    T=[
        ("{F} ¿Dónde se exhibieron las Doce Tablas?", "En el Foro", "La ficha lo indica."),
        ("{F} ¿Hacia qué año son las Doce Tablas?", "Hacia 450 a. C.", "La ficha lo indica."),
        ("{F} ¿Qué cobraba el gobernador de una provincia?", "Impuestos", "La ficha lo indica."),
        ("=", "{F} ¿Cuántas monedas recibiría Roma de 8 ciudades de la provincia?", "8*100", "Se multiplican las ciudades por el impuesto de cada una.", " monedas"),
        ("{F} ¿Quién mantenía consejos propios en las provincias?", "Muchas ciudades locales", "La ficha lo indica."),
        ("{F} Clasifica como derecho (D) o administración (A): 1) ley escrita; 2) cobro de impuestos; 3) contrato; 4) gobernador de provincia.", "1 D, 2 A, 3 D, 4 A", "Las normas son derecho; cobrar y gobernar son administración."),
        ("=", "{F} Si cada ciudad envía 100 monedas y Roma recibe 1.500 de una provincia, ¿cuántas ciudades hay en esa provincia?", "1500//100", "Se divide el total por lo que paga cada ciudad.", " ciudades"),
        ("{F} ¿Por qué es importante que una ley sea escrita y pública?", "Porque todos saben qué se permite y qué no, y se limita la arbitrariedad", "La ley conocida limita decisiones caprichosas."),
        ("{F} ¿Qué gana Roma al permitir que las ciudades mantengan sus consejos locales?", "Menos conflictos y menos gasto, porque los asuntos locales los resuelven los locales", "Se gobierna un territorio grande con ayuda local."),
        ("{F} Un compañero dice: «El derecho romano nunca cambió desde las Doce Tablas». Corrígelo.", "Cambió durante siglos: se agregaron normas y se adaptaron a nuevas situaciones", "El derecho evoluciona."),
        ("{F} Ana dice: «El Código Civil de Chile es una copia del derecho romano». Corrígela.", "Se inspira en parte en esa tradición, pero fue escrito por Andrés Bello con otras fuentes", "Una inspiración no es una copia."),
        ("{F} ¿Cómo se relacionan el derecho y la administración en una provincia?", "El gobernador aplica las leyes al resolver juicios y cobrar impuestos", "La administración usa las normas para ordenar el territorio."),
        ("{F} Un joven dice: «Como Roma tenía leyes escritas, todos eran tratados igual». ¿Qué falta en su razonamiento?", "Que había diferencias entre ciudadanos y no ciudadanos y entre personas libres y esclavizadas", "Las leyes no implicaban igualdad para todos."),
    ],
    ctx=("Un colegio expone en el patio las normas de convivencia para que todos las lean antes de que comience el año. ¿Con qué idea romana se parece y por qué? {F}", "Con las Doce Tablas en el Foro: normas escritas y públicas", "Que todos las conozcan limita la arbitrariedad."),
    sc=[("¿Qué era una provincia?", "Un territorio conquistado por Roma, gobernado por un funcionario", "Se administraba aparte."),
        ("¿Para qué sirve un contrato?", "Para fijar un acuerdo con obligaciones entre personas", "Es parte del derecho."),
        ("=", "{F} ¿Cuántas monedas pagan 15 ciudades?", "15*100", "Se multiplican las ciudades por 100.", " monedas")],
    op=("Elige una regla de tu curso y escríbela como una «tabla» con tres líneas: qué se debe hacer, qué pasa si no se cumple y dónde se exhibe. Explica en dos líneas por qué ayuda que sea escrita y pública. {F}",
        "Regla: levantar la mano para hablar; si no se cumple, se recuerda la norma; se exhibe en la pizarra.",
        ["la regla está bien redactada", "incluye consecuencia y lugar de exhibición", "explica por qué ayuda que sea pública"], ["regla escrita", "explicación escrita"], ["reglas ambiguas", "no explicar el beneficio"],
        "Pide que explique en qué se parece su regla a una ley romana y en qué no."),
    reinforce="Explica con tus palabras qué es una provincia y qué hacía un gobernador.",
    extend="Escribe una pregunta sobre cómo se resolvían los juicios en una provincia lejana.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (resumen hecho para este cuaderno; algunas cifras son de ejemplo). "
     "Una legión romana tenía unos 5.000 soldados. Un soldado marchaba unos 30 km por día. Los soldados también construían caminos y fuertes. "
     "La Vía Apia, una de las primeras calzadas (caminos de piedra) importantes, se empezó a construir en 312 a. C. Junto a los caminos había columnas llamadas miliarios que indicaban distancias. "
     "Los acueductos llevaban agua a las ciudades con una pendiente suave para que el agua corriera sola; en un acueducto de ejemplo, el agua baja 1 m por cada 1.000 m de largo. "
     "Otras obras: puentes, puertos, termas (baños públicos) y anfiteatros.")
build(
    OA, 3, F,
    use="Aprenderé a examinar el papel del ejército, los caminos y la infraestructura en el Imperio romano. Sirve para explicar cómo se mantenía unido un territorio grande.",
    prior=["Sé qué es una provincia.", "Sé cómo se relacionan ley y administración.", "Sé multiplicar y dividir con números pequeños."],
    explain=[
        "El ejército romano estaba organizado en legiones, de unos 5.000 soldados. Los soldados marchaban unos 30 km por día y, además de combatir, construían caminos, puentes y fuertes. Un ejército organizado ayudó a defender y controlar un territorio grande.",
        "Los caminos romanos o calzadas, como la Vía Apia (desde 312 a. C.), eran de piedra, con columnas llamadas miliarios que indicaban distancias. Servían al ejército, pero también al comercio, al correo y a los funcionarios. Con ellos, las noticias y los productos viajaban más rápido entre ciudades y provincias.",
        "La infraestructura incluía acueductos que llevaban agua a las ciudades con una pendiente suave, puertos, puentes, termas y anfiteatros. Estas obras muestran la capacidad técnica y la organización de Roma, pero no la explican sola: la expansión se debió a muchas causas, y los caminos y las obras se financiaban con impuestos y trabajo de muchas personas, incluidas las esclavizadas.",
    ],
    vocab=[("legión", "unidad del ejército romano de unos 5.000 soldados"), ("calzada", "camino de piedra construido por los romanos"), ("miliario", "columna junto al camino que indica distancias"), ("acueducto", "obra que lleva agua a una ciudad con una pendiente suave"), ("termas", "baños públicos romanos")],
    worked=[
        ("Calcular días de marcha", "{F} Una calzada de 150 km, ¿cuántos días de marcha necesita un ejército?", ["Avanza 30 km por día.", "Divido: 150 ÷ 30 = 5."], "5 días"),
        ("Calcular una pendiente", "{F} En un acueducto de 5.000 m de largo, ¿cuántos metros baja el agua?", ["Baja 1 m cada 1.000 m.", "Divido: 5.000 ÷ 1.000 = 5."], "5 m"),
    ],
    mistakes=[("Atribuir la expansión de Roma solo a la superioridad militar.", "Se ignoran los caminos, las alianzas y la administración.", "El ejército fue uno de varios factores."),
              ("Pensar que las obras romanas las hicieron solo ingenieros famosos.", "Se olvida el trabajo de muchas personas.", "Las obras se hicieron con soldados, trabajadores y personas esclavizadas.")],
    T=[
        ("{F} ¿Cuántos soldados tenía una legión?", "Unos 5.000", "La ficha lo indica."),
        ("{F} ¿Cuántos km marchaba un soldado por día?", "30 km", "La ficha lo indica."),
        ("{F} ¿Qué indicaban los miliarios?", "Las distancias", "La ficha lo indica."),
        ("=", "{F} Una calzada de 120 km, ¿cuántos días de marcha necesita un ejército?", "120//30", "Se divide la distancia por los km de cada día.", " días"),
        ("=", "{F} ¿Cuántos soldados hay en 5 legiones?", "5*5000", "Se multiplican las legiones por los soldados de cada una.", " soldados"),
        ("{F} ¿Desde cuándo se construyó la Vía Apia?", "Desde 312 a. C.", "La ficha lo indica."),
        ("=", "{F} En un acueducto de 20.000 m, ¿cuántos metros baja el agua?", "20000//1000", "Se divide el largo por los metros por cada metro de bajada.", " m"),
        ("=", "{F} Un ejército marcha 15 días a 30 km por día. ¿Cuántos kilómetros recorre?", "15*30", "Se multiplican los días por los km diarios.", " km"),
        ("{F} ¿Por qué un acueducto necesita una pendiente suave?", "Para que el agua corra sola sin desbordarse ni detenerse", "Una pendiente muy fuerte la haría correr demasiado."),
        ("{F} Pedro dice: «Roma controló su territorio solo con el ejército». Nombra dos cosas de la ficha, además de los soldados, que ayudaban a controlarlo.", "Los caminos con miliarios, que permitían mover tropas, noticias y comercio, y obras como puertos, puentes o acueductos", "El ejército se apoyaba en caminos y obras."),
        ("{F} ¿Por qué los caminos refuerzan al ejército?", "Porque permiten mover tropas y noticias con rapidez", "Con calzadas, las legiones llegan antes."),
        ("{F} ¿Qué evidencia arqueológica conservada permite saber cuánto distaban dos ciudades?", "Los miliarios, columnas con distancias junto a los caminos", "La ficha los describe."),
        ("{F} Un compañero dice: «Las obras romanas muestran que todos vivían bien». ¿Qué falta en su razonamiento?", "Que las obras se hicieron con trabajo de muchas personas, incluidas esclavizadas, y se pagaron con impuestos", "Las obras no prueban igualdad."),
    ],
    ctx=("Una constructora mide un camino de 90 km y quiere saber cuántos días tardaría un grupo de soldados a pie, como en la ficha. ¿Qué respondes? {F}", "3 días", "90 ÷ 30 = 3 días."),
    sc=[("¿Qué es una calzada?", "Un camino de piedra construido por los romanos", "La Vía Apia es una."),
        ("¿Para qué servía un acueducto?", "Para llevar agua a una ciudad", "Usaba una pendiente suave."),
        ("=", "{F} ¿Cuántos km recorre un ejército en 4 días de marcha?", "4*30", "Se multiplican los días por 30 km.", " km")],
    op=("Dibuja un mapa esquemático de una provincia con una ciudad, un fuerte, una calzada con dos miliarios, un acueducto y un puerto. Escribe una frase para cada obra que explique para qué servía y quién la usaba. {F}",
        "Calzada con miliarios que muestran distancias para soldados, comerciantes y funcionarios; acueducto que lleva agua a la ciudad; puerto para el comercio.",
        ["incluye las cinco obras", "explica el uso de cada una", "menciona quiénes la usaban"], ["mapa dibujado", "frases escritas"], ["omitir el uso de alguna obra", "decir que las obras fueron solo para el ejército"],
        "Pide que explique cómo se financiaban las obras y quién trabajaba en ellas."),
    reinforce="Nombra tres obras romanas y para qué servía cada una.",
    extend="Escribe una pregunta sobre cómo se mantenían los caminos después de construidos.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (resumen hecho para este cuaderno). "
     "Lengua: el latín dio origen a lenguas romances como el español, el italiano, el francés, el portugués y el rumano. Palabras latinas: aqua (agua), terra (tierra), lingua (lengua), pater (padre). En la parte oriental del Imperio se hablaba sobre todo griego, y había muchas lenguas locales. "
     "Ciudadanía: al principio la tenían pocas personas. En 212 d. C., el edicto de Caracalla concedió la ciudadanía a casi todos los habitantes libres del Imperio. Las personas esclavizadas no eran ciudadanas. "
     "Religión: los romanos honraban a muchos dioses (Júpiter, Juno, Minerva) y al emperador; también llegaron cultos de Oriente. El cristianismo creció y sufrió persecuciones. En 313 d. C., el edicto de Milán permitió su libre práctica y en 380 d. C. fue declarado religión oficial.")
build(
    OA, 4, F,
    use="Aprenderé a analizar la lengua, la ciudadanía y la religión en el Imperio romano. Sirve para ver que era una sociedad diversa y que su legado es variado.",
    prior=["Sé qué fue la República y el Imperio.", "Sé qué es una provincia.", "Sé comparar años d. C."],
    explain=[
        "El Imperio romano unía a pueblos muy distintos. El latín se difundió, y de él nacieron lenguas romances como el español, el italiano, el francés, el portugués y el rumano. Los pueblos conquistados adoptaron en distinto grado la lengua, las leyes y las costumbres de Roma: a este proceso se le llama romanización. No fue igual en todas partes, y no todos hablaban latín: en el Oriente se hablaba sobre todo griego, y había muchas lenguas locales.",
        "La ciudadanía romana fue ampliándose. Al principio la tenían pocas personas; en 212 d. C. el edicto de Caracalla la concedió a casi todos los habitantes libres del Imperio. Las personas esclavizadas no eran ciudadanas. Ser ciudadano daba derechos ante la ley, aunque seguía habiendo desigualdad entre grupos.",
        "En religión, los romanos honraban a muchos dioses y al emperador, y aceptaron cultos de otros lugares. El cristianismo creció, sufrió persecuciones y luego fue permitido en 313 d. C. y declarado religión oficial en 380 d. C. Roma no fue una sociedad uniforme: tenía lenguas, derechos y creencias diversos que cambiaron con el tiempo.",
    ],
    vocab=[("lengua romance", "lengua que nació del latín"), ("romanización", "proceso por el que pueblos conquistados adoptaron lengua, leyes y costumbres de Roma"), ("ciudadanía", "condición de quien tiene derechos y deberes políticos y legales"), ("edicto", "orden dictada por una autoridad"), ("politeísta", "que cree en muchos dioses"), ("religión oficial", "religión reconocida por el Estado")],
    worked=[
        ("Relacionar palabras", "{F} ¿Qué palabra española viene de la latina terra?", ["Busco terra en la ficha.", "La ficha dice que significa tierra."], "Tierra"),
        ("Calcular una distancia en el tiempo", "{F} ¿Cuántos años pasaron entre el edicto de Milán y el edicto que declaró religión oficial al cristianismo?", ["Fechas: 313 d. C. y 380 d. C.", "Resto: 380 − 313 = 67."], "67 años"),
    ],
    mistakes=[("Decir que todos los habitantes del Imperio hablaban latín.", "Se supone una sociedad uniforme.", "En Oriente se hablaba griego y había muchas lenguas locales."),
              ("Creer que la ciudadanía incluía a todas las personas del Imperio.", "Se ignora a las personas esclavizadas.", "El edicto de Caracalla alcanzó a los habitantes libres, no a las personas esclavizadas.")],
    T=[
        ("{F} ¿Qué significa en español la palabra latina aqua?", "Agua", "La ficha lo indica."),
        ("{F} ¿Cuántas lenguas romances nombra la ficha?", "5", "Español, italiano, francés, portugués y rumano."),
        ("{F} ¿Qué otorgó el edicto de Caracalla?", "La ciudadanía a casi todos los habitantes libres del Imperio", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre el edicto de Caracalla (212 d. C.) y el edicto de Milán (313 d. C.)?", "313-212", "Se restan los años d. C.", " años"),
        ("{F} ¿Qué lengua se hablaba sobre todo en el Oriente del Imperio?", "Griego", "La ficha lo indica."),
        ("En Historia: ¿qué es la romanización y fue igual en todas partes?", "Es la adopción de la lengua, las leyes y las costumbres de Roma por pueblos conquistados; no fue igual en todas partes", "Cada región adoptó lo romano en distinto grado."),
        ("=", "{F} ¿Cuántos años pasaron entre el edicto de Milán y la declaración de religión oficial?", "380-313", "Se restan los años d. C.", " años"),
        ("{F} Relaciona cada palabra latina con su significado: terra, lingua, pater.", "Terra: tierra; lingua: lengua; pater: padre", "La ficha da los significados."),
        ("{F} ¿Por qué se dice que los romanos eran politeístas?", "Porque honraban a muchos dioses", "La ficha nombra varios."),
        ("{F} Ana dice: «Todos los habitantes del Imperio hablaban latín». Corrígela.", "En el Oriente se hablaba sobre todo griego y había muchas lenguas locales", "La ficha lo indica."),
        ("{F} Un compañero dice: «Después del edicto de Caracalla todos eran ciudadanos». ¿Qué personas quedaban fuera?", "Las personas esclavizadas", "La ficha lo dice."),
        ("{F} ¿Por qué el edicto de Milán cambió la situación de los cristianos?", "Porque permitió su libre práctica y dejaron de ser perseguidos por ese motivo", "La ficha dice que permitió su práctica."),
        ("{F} Elige la frase más precisa: A) El Imperio romano tenía lenguas, derechos y creencias diversos que cambiaron con el tiempo; B) El Imperio romano era una sociedad uniforme.", "A) Tenía lenguas, derechos y creencias diversos que cambiaron con el tiempo", "La ficha muestra diversidad."),
    ],
    ctx=("En Chile hablamos español y en Italia, italiano. ¿Qué relación histórica explica que las dos lenguas tengan palabras parecidas, como «lengua» y «lingua»? {F}", "Que ambas son lenguas romances nacidas del latín", "El latín se difundió en el Imperio y dio origen a ambas."),
    sc=[("¿Qué es una lengua romance?", "Una lengua que nació del latín", "El español es una."),
        ("¿Qué significa politeísta?", "Que cree en muchos dioses", "Los romanos honraban a varios."),
        ("=", "{F} ¿Cuántos años pasaron entre 313 d. C. y 380 d. C.?", "380-313", "Se restan los años d. C.", " años")],
    op=("Escribe una ficha de 6 líneas: dos palabras del español que vengan del latín (usa las de la ficha), una frase sobre quién era ciudadano antes y después de 212 d. C. y una frase sobre cómo cambió la situación del cristianismo. {F}",
        "Agua (aqua) y tierra (terra); antes pocos eran ciudadanos y en 212 d. C. casi todos los libres; en 313 d. C. se permitió el cristianismo.",
        ["dos palabras con su origen latino", "explica el cambio de ciudadanía", "explica el cambio del cristianismo"], ["ficha escrita"], ["decir que todos hablaban latín", "olvidar a las personas esclavizadas"],
        "Pide que explique qué grupos seguían sin derechos después de 212 d. C."),
    reinforce="Escribe tres palabras latinas de la ficha con su significado en español.",
    extend="Escribe una pregunta sobre qué lenguas locales se hablaban en una provincia del Imperio.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (resumen hecho para este cuaderno). "
     "Continuidades en Chile: el español viene del latín; usamos el alfabeto latino; los nombres de los meses julio y agosto vienen de Julio César y de Augusto; el Código Civil de 1855 se inspira en parte en el derecho romano; el Palacio de La Moneda, proyectado por el arquitecto italiano Joaquín Toesca y terminado en 1805, es de estilo neoclásico, inspirado en la arquitectura clásica de Grecia y Roma. "
     "Cambios: el latín se transformó en nuevas lenguas; el derecho fue adaptado a nuevas leyes y a las necesidades de cada país; Roma tenía esclavitud y emperadores, algo que hoy no existe en Chile.")
build(
    OA, 5, F,
    use="Aprenderé a evaluar qué continuó, qué cambió y cómo se apropió el legado romano en épocas posteriores, como la nuestra. Sirve para decir qué recibimos de Roma sin idealizarla.",
    prior=["Sé qué fue la República y el Imperio.", "Sé qué aportaron el derecho y las lenguas romances.", "Sé distinguir continuidad y cambio."],
    explain=[
        "Un legado es lo que una sociedad recibe de otra. De Roma recibimos el alfabeto latino, la base del español, nombres de meses, ideas de derecho y formas de construir. Esa continuidad no es una copia: cada época toma lo que le sirve y lo cambia, y a eso se le llama apropiación.",
        "Por ejemplo, el español viene del latín, pero cambió mucho. El Código Civil chileno de 1855 se inspira en parte en el derecho romano, pero fue escrito por Andrés Bello para Chile y mezcla otras fuentes. El Palacio de La Moneda, terminado en 1805, es de estilo neoclásico, inspirado en la arquitectura clásica de Grecia y Roma, pero fue proyectado por un arquitecto italiano para Chile.",
        "También hay cambios y rupturas: Roma tenía esclavitud y emperadores con gran poder, y hoy la esclavitud está prohibida en Chile y no tenemos emperadores. Para evaluar el legado conviene preguntar qué se conservó, qué se transformó y qué se dejó atrás, y evitar la idea de que lo romano fue siempre mejor o peor que lo actual.",
    ],
    vocab=[("legado", "lo que una sociedad recibe de otra"), ("continuidad", "aquello que se mantiene a lo largo del tiempo"), ("cambio", "aquello que se transforma con el tiempo"), ("apropiación", "tomar algo de otra época o cultura y adaptarlo a las propias necesidades"), ("neoclásico", "estilo del siglo XVIII y XIX inspirado en el arte de Grecia y Roma")],
    worked=[
        ("Clasificar continuidad y cambio", "{F} El español viene del latín, pero hoy es distinto. ¿Es continuidad, cambio o ambas?", ["El español viene del latín: continuidad.", "Pero se transformó: cambio."], "Ambas"),
        ("Contar elementos", "En una lista de 5 legados de Roma, 3 son continuidades. ¿Cuántos son cambios?", ["Total: 5 legados.", "Resto: 5 − 3 = 2."], "2 cambios"),
    ],
    mistakes=[("Pensar que el legado romano llegó intacto hasta hoy.", "Se confunde legado con copia.", "Cada época adaptó lo recibido a sus necesidades."),
              ("Decir que Roma fue mejor o peor que hoy.", "Se evalúa sin considerar el contexto.", "Compara qué continuó y qué cambió, explicando la época.")],
    T=[
        ("{F} ¿De qué lengua viene el español?", "Del latín", "La ficha lo indica."),
        ("{F} ¿De quién viene el nombre del mes de julio?", "De Julio César", "La ficha lo indica."),
        ("{F} ¿Qué alfabeto usamos?", "El latino", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre 1805 y 1855?", "1855-1805", "Se restan los años.", " años"),
        ("{F} ¿Qué estilo tiene el Palacio de La Moneda según la ficha?", "Neoclásico, inspirado en la arquitectura clásica", "La ficha lo indica."),
        ("{F} Clasifica como continuidad (C) o cambio (A): 1) usamos el alfabeto latino; 2) hoy está prohibida la esclavitud en Chile; 3) el español viene del latín; 4) ya no hay emperadores en Chile.", "1 C, 2 A, 3 C, 4 A", "Lo que se mantiene es continuidad; lo que cambió, cambio."),
        ("{F} ¿Quién escribió el Código Civil de Chile?", "Andrés Bello", "La ficha lo indica."),
        ("{F} ¿Por qué el Código Civil chileno es una apropiación y no una copia del derecho romano?", "Porque fue escrito para Chile, se inspira en parte en el derecho romano y mezcla otras fuentes", "Se adaptó a las necesidades del país."),
        ("=", "{F} Si se nombran 4 legados y 3 cambios de la ficha, ¿cuántos hechos hay en total?", "4+3", "Se suman ambas cantidades.", " hechos"),
        ("{F} Pedro dice: «El legado romano llegó intacto hasta hoy». Corrígelo con un ejemplo de la ficha.", "El español viene del latín, pero cambió mucho", "La lengua es un ejemplo de transformación."),
        ("{F} Ana dice: «Roma fue mejor que Chile hoy porque tenía acueductos». ¿Qué error de método hay?", "Evalúa sin comparar los criterios ni considerar el contexto; Roma tenía además esclavitud, que hoy está prohibida", "Un buen juicio considera ventajas y problemas."),
        ("{F} ¿Qué podría decir un guía del Palacio de La Moneda sobre su relación con Roma?", "Que su estilo neoclásico se inspira en la arquitectura clásica, pero fue construido en Chile en 1805", "Es un ejemplo de apropiación."),
        ("{F} Propón un legado romano que no esté en la ficha y que tú reconozcas hoy.", "Por ejemplo: el calendario de doce meses, o las ideas de ciudadanía, o las carreteras que siguen rutas antiguas", "Hay más legados."),
    ],
    ctx=("Un guía de turismo dice: «En La Moneda, Roma sigue viva». ¿Cómo lo corriges para ser más preciso? {F}", "Es un edificio neoclásico inspirado en la arquitectura clásica, no un edificio romano", "Hay inspiración y adaptación, no continuidad exacta."),
    sc=[("¿Qué es la apropiación de un legado?", "Tomar algo de otra época y adaptarlo a las propias necesidades", "No es copiar."),
        ("¿Qué es una continuidad? Da un ejemplo.", "Algo que se mantiene en el tiempo, como el alfabeto latino", "Se conserva aunque cambie."),
        ("{F} ¿De quién viene el nombre del mes de agosto?", "De Augusto", "La ficha lo indica.")],
    op=("Elige tres legados de Roma que veas hoy en tu vida (por ejemplo, el idioma, un mes, un edificio). Para cada uno escribe qué se mantuvo, qué cambió y una pregunta que quedaría abierta. {F}",
        "Idioma: se mantiene la raíz latina; cambió la pronunciación y el vocabulario; ¿qué palabras indígenas se agregaron?",
        ["tres legados distintos", "distingue lo que se mantuvo y lo que cambió", "una pregunta abierta por legado"], ["tres fichas escritas"], ["decir que se copió igual", "no mencionar ningún cambio"],
        "Pide que explique por qué un legado puede ser una apropiación y no una copia."),
    reinforce="Menciona dos continuidades y dos cambios entre Roma y Chile hoy.",
    extend="Escribe una pregunta sobre qué legados de otros pueblos, además de Roma, vemos en Chile.",
)
