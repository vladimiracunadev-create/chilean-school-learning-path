"""Mecánica de Mantenimiento de Aeronaves TP (3.º y 4.º medio) módulo B: OAE-03 (elementos estructurales), OAE-04 (controles de vuelo) y OAE-05 (documentos técnicos en inglés). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_meae_common import AVISO, EMER, build

O3 = "TP-MEAE-3y4-OAE-03"
O4 = "TP-MEAE-3y4-OAE-04"
O5 = "TP-MEAE-3y4-OAE-05"

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (matriz de peligros de ejemplo, inventada). El «Hangar Demo de Estructuras» anota: una persona sobre una plataforma elevada junto al empenaje, una aeronave elevada sobre gatas, polvo fino de un material compuesto, "
     "un solvente de limpieza en un recipiente abierto, el borde cortante de una chapa metálica y el ruido de una herramienta neumática. Dotación del turno: 16 personas; el hangar tiene 4 puestos de trabajo.")
build(
    O3, 1, F,
    use="Aprenderé qué partes forman la estructura de una aeronave, qué peligros tiene el trabajo estructural y cómo se ordenan las medidas de prevención.",
    prior=["Sé leer una matriz de peligros.", "Sé multiplicar y dividir enteros.", "Sé que el trabajo sigue manuales del fabricante."],
    explain=[
        "La estructura de una aeronave se divide en partes: el fuselaje, que es el cuerpo central; las alas; el empenaje, que es la cola con sus estabilizadores; el tren de aterrizaje, con sus ruedas y soportes; y el interior, con la cabina, los pisos, los asientos y los paneles. Se fabrican con aleaciones metálicas y con materiales compuestos, que son capas de fibras unidas con resina. El mantenimiento estructural sigue el manual de mantenimiento y el manual de reparaciones estructurales del fabricante.",
        "Los peligros típicos del trabajo estructural son las caídas desde altura, las cargas elevadas, el polvo fino, los solventes, los bordes cortantes y el ruido. Un control de ingeniería puede ser una plataforma con barandas; uno administrativo, un permiso de trabajo y una regla escrita; y el equipo de protección personal (EPP) es la última barrera. El trabajo en altura y el uso de gatas para elevar una aeronave son tareas de personal capacitado y autorizado.",
        f"En este cuaderno solo se estudian los conceptos. {EMER} {AVISO}",
    ],
    vocab=[("fuselaje", "cuerpo central de la aeronave"), ("empenaje", "cola de la aeronave, con sus estabilizadores"), ("tren de aterrizaje", "ruedas y soportes que sostienen la aeronave en tierra"), ("material compuesto", "material de capas de fibras unidas con resina"), ("manual de reparaciones estructurales", "documento del fabricante con límites de daño y reparaciones"), ("control de ingeniería", "medida que cambia el equipo o el lugar para reducir el peligro")],
    worked=[
        ("Parte de la estructura", "En una aeronave de ejemplo, ¿en qué parte están los estabilizadores de la cola?", ["Los estabilizadores forman parte de la cola.", "La cola se llama empenaje."], "En el empenaje"),
        ("Tipo de control", "Un hangar de ejemplo instala barandas en una plataforma de trabajo. ¿Qué tipo de control es?", ["Las barandas cambian el lugar de trabajo.", "Es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Creer que un arnés o un casco bastan para trabajar en altura.", "El EPP es la última barrera y no reemplaza la formación ni el permiso.", "Primero se controla el peligro; la tarea la hace personal autorizado."),
              ("Llamar «riesgo» a la plataforma elevada.", "La plataforma es el peligro; el riesgo es la posibilidad de caer.", "Nombra el peligro y luego el daño posible.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué parte de la aeronave es el empenaje?", "La cola, con sus estabilizadores", "El cuerpo central", "Las ruedas y sus soportes", "El empenaje es la cola; el cuerpo central es el fuselaje."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es un material compuesto?", "Un material de capas de fibras unidas con resina", "Una aleación metálica de una sola capa", "Un solvente de limpieza", "Los compuestos combinan fibras y resina; no son un metal ni un líquido."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué documento fija los límites de daño y las reparaciones estructurales?", "El manual de reparaciones estructurales del fabricante", "La orden de trabajo de la aeronave", "La matriz de peligros del hangar", "Ese manual trae los límites de daño y las reparaciones permitidas."),
        ("abc", "{F} ¿Qué peligro de la matriz puede causar una caída?", "La persona sobre una plataforma elevada junto al empenaje", "El ruido de la herramienta neumática", "El polvo fino del material compuesto", "La altura expone a caídas; el ruido y el polvo dañan de otra manera."),
        ("abc", "{F} Un permiso de trabajo y una regla escrita para trabajar en altura son:", "Controles administrativos", "Controles de ingeniería", "El equipo de protección personal", "Un permiso y una regla ordenan la conducta de las personas."),
        ("abc", "{F} ¿Qué peligro de la matriz se asocia al daño de las vías respiratorias por partículas?", "El polvo fino de un material compuesto", "El borde cortante de una chapa", "La aeronave elevada sobre gatas", "Las partículas finas se respiran; el borde corta y la gata sostiene una carga."),
        ("=", "{F} El hangar asigna 1 persona a cargo de seguridad por cada 4 personas del turno. ¿Cuántas personas se necesitan?", "16//4", "Se divide la dotación entre las personas que cubre cada responsable.", " personas"),
        ("=", "{F} Cada uno de los 4 puestos debe tener 2 extintores y el hangar guarda 3 de repuesto. ¿Cuántos extintores necesita?", "4*2+3", "Se multiplican los puestos por los extintores de cada uno y se suma el repuesto.", " extintores"),
        ("=", "Un peligro de ejemplo tiene probabilidad 4 y gravedad 5. Con un control la probabilidad baja a 2. ¿Cuántos puntos baja el puntaje (probabilidad por gravedad)?", "4*5-2*5", "Se calcula el puntaje antes y después, y se restan.", " puntos"),
        ("abc", "{F} Una persona en práctica dice: «con el arnés puesto, puedo subir a la plataforma sin permiso». ¿Qué respuesta es correcta?", "Es falso: el trabajo en altura exige formación, permiso y autorización, y el EPP es solo la última barrera", "Es cierto, porque el arnés elimina el peligro", "Es cierto, si va con un compañero", "El EPP no reemplaza la formación ni el permiso."),
        ("abc", "En una visita a un hangar de ejemplo, una plataforma elevada se inclina y una persona empieza a caer. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Subir a la plataforma a ayudar", "Intentar sostener a la persona con las manos", "Acercarse puede provocar otro accidente; se avisa a quienes pueden actuar."),
        ("=", "{F} El peligro de la aeronave elevada tiene probabilidad 2 y gravedad 5; el del solvente abierto tiene probabilidad 4 y gravedad 3. ¿Cuántos puntos más de puntaje (probabilidad por gravedad) tiene el segundo?", "4*3-2*5", "Se calculan los dos puntajes y se restan.", " puntos"),
        ("abc", "{F} Un compañero dice: «el riesgo del borde cortante es bajo porque la chapa es delgada». ¿Qué observación es correcta?", "Una chapa delgada puede cortar con gravedad; el riesgo se evalúa con probabilidad y gravedad", "Tiene razón, porque lo delgado nunca corta", "Tiene razón, porque los bordes no se evalúan", "El grosor no define el riesgo; se evalúa la posibilidad y la gravedad del daño."),
    ],
    ctx=("abc", "Un jefe de turno de ejemplo te dice: «sube a la plataforma y mira la cola, que tú ya sabes de estructuras». ¿Qué respondes?", "Que no, porque trabajar en altura exige instructor autorizado y norma vigente, y que consultarás a un adulto responsable", "Que sí, porque saber de estructuras basta", "Que sí, si vas muy despacio", "Saber del tema no habilita para trabajar en altura."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué es el fuselaje?", "El cuerpo central de la aeronave", "Es la parte central que une las demás."),
        ("¿Cuál es la última barrera de la jerarquía de controles?", "El equipo de protección personal", "El EPP protege a la persona pero no quita el peligro."),
        ("¿Quién hace trabajo en altura?", "Personal capacitado y autorizado", "Esta tarea no es para quien no tiene autorización."),
    ],
    op=("Un hangar de ejemplo anota dos tareas: (1) pedir a una persona en práctica que revise el borde de un ala desde una escalera sin permiso; (2) dejar un solvente de limpieza en un recipiente abierto junto a un puesto de trabajo. Escribe (a) el peligro y el riesgo de cada tarea, (b) un control de ingeniería para una de ellas, (c) un control administrativo, (d) por qué el EPP no basta y quién hace estas tareas. No describas cómo se hacen.",
        "(a) Tarea 1: peligro, la altura; riesgo, caer. Tarea 2: peligro, el solvente abierto; riesgo, inhalarlo o que se encienda. (b) Guardar el solvente en un recipiente cerrado. (c) Un permiso de trabajo y una regla escrita. (d) El EPP es la última barrera y no quita el peligro; lo hace personal autorizado con norma vigente.",
        ["distingue peligro y riesgo", "propone un control de ingeniería", "propone un control administrativo", "explica por qué el EPP no basta y quién hace la tarea"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la escalera", "proponer solo el EPP", "describir cómo se hace la tarea"],
        "Pregunta: «¿qué medida quitaría o alejaría el peligro?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe las cinco partes de la estructura de una aeronave y una función de cada una.",
    extend="Explica con un ejemplo por qué el arnés no reemplaza al permiso de trabajo en altura.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (tarjeta de inspección de ejemplo, inventada). Cinco hallazgos descritos por una persona inspectora en una aeronave de ejemplo. H1: manchas de óxido blanquecino sobre un panel de aluminio. H2: una línea fina que cruza un remache. "
     "H3: hundimiento localizado de la chapa del fuselaje. H4: capas separadas en el borde de un panel de material compuesto. H5: pérdida de material en un tope por roce repetido. Horas estimadas de evaluación: 2 por hallazgo; tarifa de ejemplo $16.000 por hora.")
build(
    O3, 2, F,
    use="Aprenderé los tipos de daño estructural, la diferencia entre estructura primaria y secundaria y qué documentos y roles intervienen en la inspección.",
    prior=["Sé nombrar las partes de la estructura.", "Sé multiplicar enteros.", "Sé que los manuales fijan límites."],
    explain=[
        "Los daños estructurales más comunes son la corrosión, que es el deterioro de un metal por reacción con el ambiente; la grieta, una separación fina del material; la abolladura, un hundimiento localizado; la delaminación, la separación de capas de un material compuesto; y el desgaste, la pérdida de material por roce. La fatiga es el deterioro por cargas repetidas y puede originar grietas. La estructura primaria es la que soporta las cargas principales del vuelo; la secundaria, la que no.",
        "Cada hallazgo se compara con los límites del manual de reparaciones estructurales: un daño dentro del límite permitido se registra; uno fuera del límite se informa a personal certificado, que decide con el manual. Una reparación mayor, según la norma vigente, afecta la resistencia de la estructura y se aprueba con requisitos especiales. La tarjeta de inspección registra hallazgos, ubicación, fecha y firmas.",
        f"Esta clase solo estudia conceptos y documentos. {EMER} {AVISO}",
    ],
    vocab=[("corrosión", "deterioro de un metal por reacción con el ambiente"), ("grieta", "separación fina del material"), ("abolladura", "hundimiento localizado de una chapa"), ("delaminación", "separación de las capas de un material compuesto"), ("fatiga", "deterioro por cargas repetidas"), ("estructura primaria", "estructura que soporta las cargas principales del vuelo"), ("reparación mayor", "reparación que afecta la resistencia de la estructura")],
    worked=[
        ("Tipo de daño", "Una persona inspectora de ejemplo describe «hundimiento en una chapa tras un golpe». ¿Qué tipo de daño es?", ["Un hundimiento localizado es una abolladura.", "No hay separación de capas ni óxido."], "Abolladura"),
        ("Costo de evaluación", "Una evaluación de ejemplo toma 3 horas a $10.000 la hora. ¿Cuánto cuesta?", ["Se multiplican las horas por la tarifa.", "3 por 10.000 son 30.000."], "$30.000"),
    ],
    mistakes=[("Llamar «grieta» a cualquier marca en la superficie.", "La grieta es una separación del material; una mancha o un rayón son otra cosa.", "Describe lo que ves y compara con la definición de cada daño."),
              ("Decidir por cuenta propia que un daño es menor y no informarlo.", "La clasificación del daño la decide personal certificado según el manual.", "Registra el hallazgo y los datos e informa.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es la corrosión?", "El deterioro de un metal por reacción con el ambiente", "La separación de capas de un material compuesto", "La pérdida de material por roce", "La corrosión es un proceso químico del metal; las otras son delaminación y desgaste."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es una delaminación?", "La separación de las capas de un material compuesto", "Un hundimiento localizado de una chapa", "Una línea fina que cruza una pieza metálica", "Solo los materiales compuestos tienen capas que se separan."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué diferencia hay entre estructura primaria y secundaria?", "La primaria soporta las cargas principales del vuelo y la secundaria no", "La primaria es la interior y la secundaria la exterior", "Son lo mismo y solo cambia el nombre", "La clasificación depende de si la estructura soporta las cargas principales."),
        ("abc", "{F} ¿Qué hallazgo describe una corrosión?", "H1, las manchas de óxido blanquecino sobre un panel de aluminio", "H3, el hundimiento localizado de la chapa", "H5, la pérdida de material en un tope", "El óxido sobre un metal es el signo de corrosión."),
        ("abc", "{F} ¿Qué hallazgo describe una delaminación?", "H4, las capas separadas en el borde de un panel de material compuesto", "H2, la línea fina que cruza un remache", "H1, las manchas de óxido", "Capas separadas en un compuesto es delaminación."),
        ("abc", "{F} ¿Qué hallazgo describe una grieta?", "H2, la línea fina que cruza un remache", "H3, el hundimiento de la chapa", "H5, la pérdida de material por roce", "Una línea fina de separación es una grieta; el hundimiento es otro daño."),
        ("=", "{F} ¿Cuántas horas de evaluación suman los 5 hallazgos?", "5*2", "Se multiplican los hallazgos por las horas de cada uno.", " horas"),
        ("=", "{F} ¿Cuántos pesos cuesta la evaluación de un solo hallazgo?", "2*16000", "Se multiplican las horas estimadas por la tarifa por hora.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta la evaluación de los 5 hallazgos?", "5*2*16000", "Se multiplican los hallazgos, las horas de cada uno y la tarifa.", " pesos"),
        ("abc", "{F} Una persona dice: «H5 es desgaste porque algo se hundió». ¿Qué observación es correcta?", "Es falso: el desgaste es pérdida de material por roce y lo que se hundió sería una abolladura", "Es correcto, porque desgaste y hundimiento son lo mismo", "Es correcto, si el tope es metálico", "El desgaste pierde material; el hundimiento es una abolladura."),
        ("abc", "{F} Una persona en práctica dice: «H2 es una línea chica, la clasifico como menor y no la informo». ¿Qué corresponde?", "Registrar el hallazgo e informar a personal certificado, que clasifica según el manual", "Dejarlo sin registro, porque es chico", "Pulir la zona para borrar la línea", "La clasificación del daño la decide personal certificado; borrar el signo oculta información."),
        ("=", "{F} Si cada hallazgo debe llevar 3 datos en la tarjeta (ubicación, fecha y firma), ¿cuántos datos hay en total?", "5*3", "Se multiplican los hallazgos por los datos de cada uno.", " datos"),
        ("abc", "Un compañero dice: «la fatiga es un daño que aparece por un solo golpe fuerte». ¿Qué observación es correcta?", "Es falso: la fatiga se debe a cargas repetidas a lo largo del tiempo", "Es correcto, porque la fatiga es un golpe", "Es correcto, si el golpe es en el ala", "La fatiga es un deterioro por cargas que se repiten."),
    ],
    ctx=("abc", "Una persona de un hangar de ejemplo te dice: «tapa con pintura esa mancha blanca del panel para que el inspector no la vea». ¿Qué respondes?", "Que no, porque ocultar un hallazgo falsea el registro, y avisarás a un adulto responsable", "Que sí, porque una mancha es solo estética", "Que sí, si la pintura es resistente", "Ocultar un hallazgo es una falta grave de honestidad."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué es una abolladura?", "Un hundimiento localizado de una chapa", "Se trata de una deformación local, no de una separación."),
        ("¿Quién clasifica un daño fuera de límites?", "Personal certificado según el manual", "La clasificación no es del técnico."),
        ("¿Qué se hace con un daño dentro del límite permitido?", "Se registra", "Todo hallazgo se registra aunque esté dentro del límite."),
    ],
    op=("Ficha de ejemplo: una persona inspectora anota: A) manchas de óxido en un soporte metálico; B) capas separadas en el borde de un panel de compuesto; C) una línea fina que sale del borde de un agujero de una puerta de acceso. Cada evaluación toma 3 horas a $12.000 la hora. Escribe (a) el tipo de daño de cada uno, (b) el costo de evaluar los tres, (c) qué documento fija el límite permitido, (d) por qué no clasificas tú el daño.",
        "(a) A: corrosión; B: delaminación; C: grieta. (b) 3 hallazgos × 3 horas × 12.000 = 108.000 pesos. (c) El manual de reparaciones estructurales del fabricante. (d) La clasificación la decide personal certificado según el manual; yo registro e informo.",
        ["identifica los tipos de daño", "calcula el costo", "nombra el documento", "explica quién clasifica"],
        ["hoja con las cuatro respuestas"],
        ["confundir delaminación con grieta o abolladura", "calcular mal el costo", "clasificar por cuenta propia"],
        "Pregunta: «¿qué dice la definición del daño?». Si duda, pídele que relea el vocabulario."),
    reinforce="Escribe los cinco tipos de daño estructural con su definición en tus palabras.",
    extend="Explica con un ejemplo por qué una grieta puede ser más grave que una mancha de óxido leve.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (informe de ubicación de ejemplo, inventado). Referencia: la «estación» de fuselaje es la distancia en centímetros desde un punto de referencia de la nariz (valores de ejemplo). Hallazgos en una aeronave de ejemplo: H1 (corrosión) en la estación 120, lado izquierdo; "
     "H2 (abolladura) en la estación 340, lado derecho; H3 (delaminación) en la estación 345, lado derecho; H4 (grieta) en la estación 610, lado izquierdo. Regla de ejemplo del informe: hallazgos del mismo lado a menos de 20 cm entre sí se informan como una sola zona.")
build(
    O3, 3, F,
    use="Aprenderé a ubicar hallazgos con estaciones y lados, a calcular distancias y a escribir un informe estructural en papel.",
    prior=["Sé restar números enteros.", "Sé leer una tabla.", "Sé nombrar los daños estructurales."],
    explain=[
        "Para decir dónde está un hallazgo se usa un sistema de referencia. En el fuselaje, la estación es la distancia desde un punto de referencia fijo, cerca de la nariz. Además se indica el lado: izquierdo o derecho, mirando desde atrás hacia la nariz. La ubicación con estación y lado permite que otra persona encuentre el mismo hallazgo y verifique el informe sin confundirse.",
        "La distancia entre dos hallazgos del mismo lado se calcula restando sus estaciones. Si el informe dice que hallazgos cercanos se agrupan, se escriben como una zona con sus estaciones de inicio y término. El informe incluye: tipo de daño, ubicación, medidas, fecha y firma. No incluye una decisión de reparar: esa la toma personal certificado según el manual.",
        f"Este análisis es solo en papel. {EMER} {AVISO}",
    ],
    vocab=[("estación", "distancia en centímetros desde un punto de referencia del fuselaje (en estos ejemplos)"), ("lado izquierdo y derecho", "lados de la aeronave, mirando desde atrás hacia la nariz"), ("zona", "grupo de hallazgos cercanos que se informan juntos"), ("informe estructural", "documento con tipo de daño, ubicación, medidas, fecha y firma"), ("punto de referencia", "lugar fijo desde el cual se miden las ubicaciones")],
    worked=[
        ("Distancia", "Dos hallazgos de ejemplo del mismo lado están en las estaciones 80 y 130. ¿Cuántos cm los separan?", ["Se resta la estación menor a la mayor.", "130 menos 80 son 50."], "50 cm"),
        ("Zona", "Con la regla de ejemplo de menos de 20 cm, dos hallazgos del mismo lado están a 12 cm. ¿Se informan juntos?", ["12 es menor que 20.", "Sí forman una zona."], "Sí, como una zona"),
    ],
    mistakes=[("Informar la ubicación sin indicar el lado.", "Sin el lado, otra persona puede buscar en la mitad equivocada.", "Escribe siempre estación y lado."),
              ("Agrupar hallazgos de lados distintos solo porque tienen estaciones parecidas.", "Un lado no es el otro: están en lugares diferentes.", "Agrupa solo los del mismo lado.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué indica la estación de un hallazgo en el fuselaje?", "La distancia desde un punto de referencia fijo", "La temperatura del metal", "El número de horas de vuelo", "La estación ubica el hallazgo con una distancia medida desde un punto fijo."),
        ("abc", "En Mantenimiento de Aeronaves: ¿por qué se anota el lado de un hallazgo?", "Para que otra persona lo encuentre sin confundirse", "Para saber quién lo vio primero", "Para calcular su costo", "Sin el lado el hallazgo podría buscarse en la mitad equivocada."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué incluye un informe estructural?", "Tipo de daño, ubicación, medidas, fecha y firma", "La decisión final de reparar o no", "Solo el nombre de la persona inspectora", "El informe describe lo observado; la decisión es de personal certificado."),
        ("abc", "{F} ¿Qué hallazgos están en el lado derecho?", "H2 y H3", "H1 y H4", "H1 y H2", "La ficha anota derecho para H2 y H3 e izquierdo para H1 y H4."),
        ("abc", "{F} Según la regla de ejemplo, ¿qué hallazgos se informan como una sola zona?", "H2 y H3, por estar en el mismo lado y a 5 cm", "H1 y H4, por estar en el mismo lado", "H1 y H2, por estar a menos de 400 cm", "Solo H2 y H3 son del mismo lado y están a menos de 20 cm."),
        ("abc", "{F} ¿Qué hallazgo está más cerca de la nariz?", "H1, en la estación 120", "H4, en la estación 610", "H3, en la estación 345", "Una estación menor está más cerca del punto de referencia."),
        ("=", "{F} ¿Cuántos cm separan a H2 de H3?", "345-340", "Se resta la estación menor a la mayor.", " cm"),
        ("=", "{F} ¿Cuántos cm separan a H1 de H4, ambos del lado izquierdo?", "610-120", "Se resta la estación menor a la mayor.", " cm"),
        ("=", "{F} ¿Cuántos cm hay entre H1 y H2?", "340-120", "Se resta la estación de H1 a la de H2.", " cm"),
        ("abc", "{F} Una persona dice: «H1 y H2 están cerca porque ambos tienen estaciones bajas». ¿Qué observación es correcta?", "Es falso: están en lados distintos y a 220 cm, así que no forman una zona", "Es correcto, porque 120 y 340 son bajos", "Es correcto, porque los dos son del mismo lado", "Para agrupar deben estar en el mismo lado y a menos de 20 cm."),
        ("abc", "{F} En el informe, ¿qué frase está bien escrita?", "«H3: delaminación en la estación 345, lado derecho»", "«H3: en la parte de atrás»", "«H3: daño grave, se repara hoy»", "Un informe bien escrito da tipo, estación y lado, sin decidir una reparación."),
        ("=", "{F} Si un quinto hallazgo del lado izquierdo apareciera a 15 cm de H4 hacia la nariz, ¿en qué estación estaría?", "610-15", "Hacia la nariz las estaciones son menores, así que se resta.", " cm"),
        ("abc", "Una persona en práctica anota «H5: lado izquierdo» sin estación. ¿Qué problema tiene el registro?", "Falta la estación: otra persona no podría ubicar el hallazgo con precisión", "Ninguno, porque basta con el lado", "Que el lado no se debe anotar", "El lado solo ubica la mitad; la estación completa la posición."),
    ],
    ctx=("abc", "Una persona de práctica de ejemplo te dice: «anota «cerca de la puerta» en vez de la estación, que es más corto». ¿Qué respondes?", "Que no, porque una ubicación vaga no permite a otra persona verificar el hallazgo", "Que sí, porque la puerta es una buena referencia", "Que sí, si la puerta tiene un número", "Una ubicación precisa permite la verificación independiente."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿cómo se calcula la distancia entre dos hallazgos del mismo lado?", "Restando sus estaciones", "La diferencia entre estaciones da la distancia."),
        ("¿Qué dos datos ubican un hallazgo en el fuselaje?", "La estación y el lado", "Con ambos otra persona lo encuentra."),
        ("¿Quién decide reparar según el informe?", "Personal certificado", "El informe describe y no decide."),
    ],
    op=("Informe de ejemplo: H1 en la estación 200, lado derecho, corrosión; H2 en la estación 214, lado derecho, corrosión; H3 en la estación 480, lado izquierdo, abolladura. Regla de ejemplo: del mismo lado y a menos de 20 cm se informan como una zona. Escribe (a) la distancia entre H1 y H2, (b) si forman una zona y por qué, (c) cuántos cm separan H2 de H3 en estaciones y si forman zona, (d) una línea del informe para H3 sin decidir reparación.",
        "(a) 214 - 200 = 14 cm. (b) Sí: mismo lado y 14 es menor que 20. (c) 480 - 214 = 266 cm; no forman zona porque están en lados distintos y lejos. (d) «H3: abolladura en la estación 480, lado izquierdo».",
        ["calcula la distancia", "aplica la regla de zona", "distingue lados", "escribe una línea de informe sin decidir"],
        ["hoja con las cuatro respuestas"],
        ["agrupar lados distintos", "restar mal las estaciones", "agregar una decisión de reparar"],
        "Pregunta: «¿mismo lado y menos de 20 cm?». Si duda, pídele que relea la regla de zona."),
    reinforce="Inventa tres hallazgos con estación y lado y escribe cuáles forman una zona según la regla de 20 cm.",
    extend="Explica por qué una buena ubicación permite la verificación independiente.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (tabla de límites de daño de ejemplo, inventada). Límites de ejemplo: profundidad máxima de corrosión permitida 5 (centésimas de milímetro, valor de ejemplo); profundidad máxima de abolladura permitida 30; cualquier grieta: ningún valor permitido, siempre se informa. Pérdida máxima de espesor permitida: 10 %. "
     "Hallazgos medidos: corrosión C1: profundidad 4; corrosión C2: profundidad 6; abolladura A1: profundidad 30; abolladura A2: profundidad 35; grieta G1: longitud 2. Pieza P: espesor original 20, pérdida medida 3.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar una tabla de límites de daño a medidas de ejemplo y a escribir una conclusión «dentro del límite» o «informar a personal certificado».",
    prior=["Sé comparar enteros.", "Sé calcular un porcentaje exacto.", "Sé distinguir los tipos de daño."],
    explain=[
        "La tabla de límites de daño del manual de reparaciones estructurales dice cuánto daño se permite sin reparación. Un daño está dentro del límite si su medida es igual o menor que el máximo. Si lo supera, se informa a personal certificado. Algunos daños, como una grieta, no tienen valor permitido: siempre se informan, sin importar su tamaño.",
        "La pérdida de espesor se expresa en porcentaje. El porcentaje se calcula como la pérdida por 100 dividido entre el espesor original. Por ejemplo, una pieza de espesor 50 que perdió 5 tiene una pérdida de 5 por 100 dividido entre 50, es decir, 10 %. Los valores de este cuaderno son de ejemplo; los reales los fija el fabricante.",
        f"El registro de cada medida lleva la conclusión, la fecha y la firma. Medir y evaluar daños reales exige instrumentos calibrados, formación y autorización. {EMER} {AVISO}",
    ],
    vocab=[("límite de daño", "medida máxima de daño que el manual permite sin reparación"), ("dentro del límite", "daño cuya medida no supera el máximo permitido"), ("pérdida de espesor", "material perdido, expresado en porcentaje del espesor original"), ("sin valor permitido", "tipo de daño que siempre se informa"), ("porcentaje", "cantidad por cada 100")],
    worked=[
        ("Dentro del límite", "Una tabla de ejemplo permite una profundidad máxima de 8 y se mide 7. ¿Está dentro del límite?", ["Siete no supera 8.", "Está dentro del límite."], "Dentro del límite"),
        ("Porcentaje de pérdida", "Una pieza de ejemplo de espesor 40 perdió 2. ¿Qué porcentaje perdió?", ["Se calcula 2 por 100 dividido entre 40.", "200 dividido entre 40 es 5."], "5 %"),
    ],
    mistakes=[("Medir con un límite que no corresponde al tipo de daño.", "Cada tipo de daño tiene su propio límite en la tabla.", "Busca primero el tipo de daño y luego su límite."),
              ("Decir que una grieta pequeña está dentro del límite.", "Para una grieta no hay valor permitido.", "Informa siempre la grieta, por pequeña que sea.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿cuándo un daño está dentro del límite?", "Cuando su medida es igual o menor que el máximo permitido", "Cuando su medida es mayor que el máximo", "Cuando nadie lo vio", "Dentro del límite significa que la medida no supera el máximo."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué se hace con una grieta de cualquier tamaño?", "Se informa siempre", "Se mide y, si es pequeña, no se registra", "Se pule para que no se vea", "Para una grieta la tabla no da ningún valor permitido."),
        ("abc", "En Mantenimiento de Aeronaves: ¿cómo se calcula el porcentaje de pérdida de espesor?", "Pérdida por 100 dividido entre el espesor original", "Espesor original por 100 dividido entre la pérdida", "Pérdida más espesor original", "El porcentaje compara la pérdida con el espesor original."),
        ("abc", "{F} ¿Qué corrosión está dentro del límite?", "C1, con profundidad 4", "C2, con profundidad 6", "Las dos, porque son valores bajos", "El máximo es 5; C1 lo cumple y C2 lo supera."),
        ("abc", "{F} ¿Qué abolladura está dentro del límite?", "A1, con profundidad 30, porque es igual al máximo", "A2, con profundidad 35", "Ninguna, porque 30 es muy alto", "Un valor igual al máximo cumple el límite; 35 lo supera."),
        ("abc", "{F} ¿Qué conclusión corresponde a la grieta G1, de longitud 2?", "Informar a personal certificado, porque no tiene valor permitido", "Dentro del límite, porque 2 es menor que 5", "Dentro del límite, porque es muy corta", "Una grieta siempre se informa, aunque la medida sea baja."),
        ("=", "{F} ¿Cuántas centésimas de milímetro de margen tiene C1 bajo su máximo?", "5-4", "Se resta la profundidad medida al máximo.", " centésimas"),
        ("=", "{F} ¿Cuántas centésimas de milímetro supera A2 el máximo de las abolladuras?", "35-30", "Se resta el máximo a la profundidad medida.", " centésimas"),
        ("=", "{F} ¿Qué porcentaje de espesor perdió la pieza P?", "3*100//20", "Se multiplica la pérdida por 100 y se divide entre el espesor original.", " %"),
        ("abc", "{F} ¿La pérdida de espesor de la pieza P está dentro del límite de 10 %?", "No, porque perdió 15 % y supera el 10 %", "Sí, porque 3 es menor que 10", "Sí, porque 15 % es menor que 20", "El porcentaje de pérdida es 15, y el máximo permitido es 10."),
        ("abc", "{F} Una persona dice: «C2 solo pasó 1 del máximo, así que lo consideramos dentro del límite». ¿Qué observación es correcta?", "Es falso: superar el máximo, aunque sea por poco, lo deja fuera del límite", "Es correcto, porque 1 es muy poco", "Es correcto, si hay otro daño peor", "El límite es un valor: lo que lo supera queda fuera."),
        ("=", "{F} Si la corrosión C1 aumentara 3 centésimas de milímetro, ¿qué profundidad tendría?", "4+3", "Se suma el aumento a la profundidad medida.", " centésimas"),
        ("abc", "{F} ¿Cuál es la lista de hallazgos que se informan a personal certificado?", "C2, A2, G1 y la pieza P", "C1 y A1", "Solo G1", "C2, A2 y P superan el máximo, y G1 es una grieta."),
    ],
    ctx=("abc", "Una compañera de práctica te muestra una medida de corrosión de 7 con límite máximo 5 y dice «lo anoto como dentro del límite, no hay problema». ¿Qué haces?", "Le explicas que 7 supera 5 y que debe registrarse fuera del límite e informarse", "La dejas, porque es su registro", "Cambias el 7 por 5", "Un registro con una conclusión falsa se corrige informando, no ocultando."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué pasa con una grieta en la tabla de límites?", "No tiene valor permitido y siempre se informa", "No hay máximo aceptable para una grieta."),
        ("¿Cómo se calcula 3 de pérdida sobre un espesor de 30, en porcentaje?", "3 por 100 dividido entre 30, que da 10 %", "Se compara la pérdida con el espesor original."),
        ("¿Quién decide qué hacer con un daño fuera del límite?", "Personal certificado, según el manual", "Quien mide no decide la reparación."),
    ],
    op=("Tabla de ejemplo: corrosión máx. 6; abolladura máx. 20; grieta sin valor permitido; pérdida de espesor máx. 8 %. Medidas: corrosión Q1: 5; corrosión Q2: 7; abolladura R1: 22; grieta S1: longitud 1; pieza T de espesor original 25 con pérdida 3. Escribe (a) la conclusión de cada hallazgo, (b) el porcentaje de pérdida de T y su conclusión, (c) cuántos hallazgos se informan, (d) a quién.",
        "(a) Q1: dentro; Q2: fuera; R1: fuera; S1: informar siempre. (b) 3 × 100 / 25 = 12 %, que supera 8 %: se informa. (c) Cinco hallazgos de los cuales se informan Q2, R1, S1 y T: cuatro. (d) A personal certificado.",
        ["aplica cada límite", "calcula el porcentaje", "cuenta los hallazgos a informar", "nombra a quién informa"],
        ["hoja con las cuatro respuestas"],
        ["decir que la grieta está dentro", "calcular mal el porcentaje", "decidir la reparación"],
        "Pregunta: «¿cuál es el máximo de ese tipo de daño?». Si duda, pídele que relea la ficha de límites."),
    reinforce="Inventa una tabla con dos máximos y una pérdida porcentual y evalúa tres medidas.",
    extend="Explica por qué una grieta no tiene un valor permitido en la tabla.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 5 (comparación de dos planes de inspección de ejemplo, inventados). Un hallazgo de corrosión superó el límite en un panel de una aeronave de ejemplo. Plan A: inspeccionar solo la zona del hallazgo, 2 horas. "
     "Plan B: ampliar la inspección a las zonas vecinas del mismo lado, 6 horas. El manual de ejemplo dice: «si un hallazgo supera el límite, ampliar la inspección a zonas vecinas». Tarifa de ejemplo $15.000 por hora. Lista de comprobación de cierre: 10 ítems.")
build(
    O3, 5, F,
    use="Aprenderé a comparar planes de inspección con el criterio del manual y el costo, y a verificar la calidad con una lista y una revisión independiente.",
    prior=["Sé calcular costos con horas y tarifas.", "Sé que el manual manda sobre el costo.", "Sé qué es una revisión independiente."],
    explain=[
        "Al comparar planes de inspección se miran el criterio del manual, el costo y el riesgo de dejar pasar un daño. El manual puede exigir ampliar la inspección: cuando un hallazgo supera el límite, se revisan las zonas vecinas, porque un daño suele no estar solo. Si el manual exige una acción, el plan que la cumple es el que corresponde, aunque cueste más. El costo se usa para comparar solo entre planes que cumplen el manual.",
        "Verificar la calidad de una inspección es comprobar que se hizo completa y que los registros son correctos. Se usa una lista de comprobación, con cada ítem marcado como cumplido, y una revisión independiente: una persona distinta de quien inspeccionó revisa y firma aparte. El resultado se informa a personal certificado, que decide.",
        f"Estos planes se comparan en papel; ejecutarlos exige personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("plan de inspección", "descripción de qué zonas se revisan y con cuánto tiempo"), ("ampliar la inspección", "revisar también las zonas vecinas a un hallazgo"), ("criterio del manual", "regla del manual que debe cumplir el plan elegido"), ("lista de comprobación", "lista de ítems que se marcan como cumplidos"), ("revisión independiente", "verificación hecha por una persona distinta de quien inspeccionó")],
    worked=[
        ("Costo de un plan", "Un plan de ejemplo toma 4 horas a $9.000 la hora. ¿Cuánto cuesta?", ["Se multiplican las horas por la tarifa.", "4 por 9.000 son 36.000."], "$36.000"),
        ("Plan que cumple", "El manual de ejemplo exige revisar 3 zonas y un plan solo revisa 2. ¿Cumple el manual?", ["El manual pide 3 zonas.", "El plan revisa solo 2: no cumple."], "No cumple"),
    ],
    mistakes=[("Elegir el plan más barato aunque no cumpla lo que pide el manual.", "El costo solo compara planes que cumplen el manual.", "Primero mira el criterio del manual y luego el costo."),
              ("Cerrar la inspección con un ítem de la lista sin marcar.", "Un ítem sin marcar es una verificación pendiente.", "Completa y comprueba todos los ítems antes de cerrar.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué significa ampliar la inspección?", "Revisar también las zonas vecinas a un hallazgo", "Repetir la misma zona dos veces", "Revisar solo el hallazgo, pero con más herramientas", "Se amplía a zonas vecinas porque los daños suelen no estar solos."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué manda al elegir entre planes de inspección?", "El criterio del manual, y el costo solo compara los que lo cumplen", "El plan más barato siempre", "El plan que dura menos", "El manual fija lo mínimo; el costo se compara entre planes que lo cumplen."),
        ("abc", "En Mantenimiento de Aeronaves: ¿para qué sirve la revisión independiente?", "Para que otra persona compruebe el resultado y detecte errores", "Para ahorrar horas de trabajo", "Para que quien inspeccionó no firme", "La mirada de otra persona detecta lo que el autor pasó por alto."),
        ("abc", "{F} ¿Qué plan cumple el criterio del manual?", "El plan B, que amplía a las zonas vecinas", "El plan A, que solo revisa la zona del hallazgo", "Ninguno de los dos", "El manual de ejemplo pide ampliar, y solo B lo hace."),
        ("abc", "{F} Una persona dice: «el plan A es mejor porque cuesta menos». ¿Qué observación es correcta?", "A no cumple el criterio del manual, así que no se elige solo por costo", "Tiene razón, porque el costo es lo único que importa", "Tiene razón, porque 2 horas es menos que 6", "El costo se usa entre planes que cumplen el manual."),
        ("abc", "{F} ¿Qué riesgo tiene el plan A?", "Dejar sin revisar daños en las zonas vecinas", "Gastar demasiado en horas", "Revisar zonas que no corresponden", "Un plan limitado puede dejar pasar un daño cercano."),
        ("=", "{F} ¿Cuántos pesos cuesta el plan A?", "2*15000", "Se multiplican las horas por la tarifa.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta el plan B?", "6*15000", "Se multiplican las horas por la tarifa.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta B que A?", "6*15000-2*15000", "Se restan los costos de los dos planes.", " pesos"),
        ("abc", "{F} Al cierre, la lista tiene 10 ítems y 9 marcados. ¿Qué corresponde?", "No cerrar hasta comprobar y marcar el ítem faltante", "Cerrar, porque 9 de 10 basta", "Marcar el décimo sin comprobar", "Un ítem pendiente deja la inspección sin verificar."),
        ("abc", "{F} Una persona de práctica dice: «yo inspeccioné, así que yo hago también la revisión independiente». ¿Qué observación es correcta?", "Es falso: la revisión independiente la hace otra persona", "Es correcto, porque conoce mejor el trabajo", "Es correcto, si firma dos veces", "La independencia exige que revise alguien distinto."),
        ("=", "{F} Si 8 de los 10 ítems de la lista están marcados, ¿qué porcentaje está completo?", "8*100//10", "Se divide lo marcado entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿A quién se informa el resultado de la inspección ampliada?", "A personal certificado, que decide según el manual", "A la persona propietaria, para que elija", "A nadie, hasta la próxima inspección", "El resultado se informa a quien decide con el manual."),
    ],
    ctx=("abc", "Una persona a cargo de un hangar de ejemplo te dice: «hagamos solo el plan corto, el largo cuesta mucho». El manual pide ampliar. ¿Qué respondes?", "Que el plan debe cumplir el manual y que consultarás a un adulto responsable", "Que sí, porque el costo manda", "Que sí, si el hallazgo es pequeño", "El manual manda sobre el costo."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué se compara solo entre planes que cumplen el manual?", "El costo", "Un plan que no cumple no se considera."),
        ("¿Quién hace la revisión independiente?", "Una persona distinta de quien inspeccionó", "Así se detectan errores que quien inspeccionó no ve."),
        ("¿Se cierra una lista con un ítem sin marcar?", "No", "El ítem pendiente es una verificación sin hacer."),
    ],
    op=("Caso de ejemplo: un hallazgo de grieta en otro panel. Plan C: revisar solo la zona, 1 hora. Plan D: revisar la zona y las dos zonas vecinas, 4 horas. El manual de ejemplo pide revisar las zonas vecinas. Tarifa $18.000 por hora. Escribe (a) el costo de cada plan, (b) qué plan cumple el manual, (c) la diferencia de costo, (d) cómo verificas la calidad del plan elegido.",
        "(a) C: 1 × 18.000 = 18.000; D: 4 × 18.000 = 72.000. (b) D, porque revisa las zonas vecinas. (c) 54.000 pesos más. (d) Con una lista de comprobación completa y una revisión independiente de otra persona; el resultado se informa a personal certificado.",
        ["calcula los costos", "elige el plan que cumple", "calcula la diferencia", "describe la verificación"],
        ["hoja con las cuatro respuestas"],
        ["elegir el barato", "calcular mal la diferencia", "olvidar la revisión independiente"],
        "Pregunta: «¿qué pide el manual?». Si duda, pídele que relea el criterio del manual."),
    reinforce="Inventa dos planes con horas y tarifa, indica cuál cumple un criterio del manual y calcula su costo.",
    extend="Explica por qué el costo no debe mandar sobre el criterio del manual.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 6 (matriz de peligros de ejemplo, inventada). El «Hangar Demo de Controles» anota: una superficie de control que se mueve cuando se energiza el sistema, una persona sobre una plataforma elevada junto a la cola, "
     "cables de control tensados, una aeronave elevada sobre gatas y el ruido de una herramienta neumática. Dotación del turno: 14 personas; 2 puestos de trabajo.")
build(
    O4, 1, F,
    use="Aprenderé qué son los controles de vuelo, qué superficies tiene una aeronave y qué peligros generales tiene su mantenimiento.",
    prior=["Sé leer una matriz de peligros.", "Sé multiplicar y dividir enteros.", "Sé que el mantenimiento sigue manuales."],
    explain=[
        "Los controles de vuelo son los sistemas que permiten a la persona piloto dirigir la aeronave. Sus superficies se agrupan: las superficies primarias son los alerones, el timón de profundidad y el timón de dirección, que controlan los movimientos principales. Las superficies secundarias y auxiliares, como los flaps, los spoilers y los compensadores, complementan a las primarias; el manual del fabricante indica cómo se clasifica cada una en cada aeronave. El mantenimiento sigue el manual de mantenimiento y respeta las normas de seguridad.",
        "Una superficie de control puede moverse sin aviso si un sistema se energiza. Los cables de control pueden estar tensados y guardar energía. Por eso se usa un permiso de trabajo, y un sistema de bloqueo y etiquetado a cargo de personas autorizadas. El trabajo cerca de la cola puede ser en altura. La jerarquía de controles sigue siendo: eliminar, sustituir, ingeniería, administrativo y EPP.",
        f"Este cuaderno no te enseña a mover ni a ajustar una superficie. {EMER} {AVISO}",
    ],
    vocab=[("controles de vuelo", "sistemas con que la persona piloto dirige la aeronave"), ("superficie primaria", "superficie que controla los movimientos principales: alerón, timón de profundidad y timón de dirección"), ("superficie secundaria", "superficie que complementa a las primarias, como un flap o un compensador"), ("bloqueo y etiquetado", "sistema que impide activar un equipo que se está trabajando"), ("cable de control", "cable que transmite el movimiento a una superficie")],
    worked=[
        ("Primaria o no", "En una aeronave de ejemplo, ¿un alerón es una superficie primaria?", ["Los alerones controlan un movimiento principal.", "Sí es primaria."], "Sí, es primaria"),
        ("Energía guardada", "Un cable de control de ejemplo está tensado. ¿Puede conservar energía aunque nadie lo mueva?", ["Un cable tensado guarda energía.", "Si se suelta de golpe, puede liberarla."], "Sí, puede conservar energía"),
    ],
    mistakes=[("Creer que una superficie de control apagada no puede moverse.", "Puede moverse si un sistema se energiza.", "Trata la superficie como si pudiera moverse hasta que personal autorizado confirme el bloqueo."),
              ("Pensar que cualquier persona puede quitar una etiqueta de bloqueo.", "Solo quien la puso o quien la norma autoriza.", "Respeta la etiqueta y avisa a un adulto responsable.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿para qué sirven los controles de vuelo?", "Para que la persona piloto dirija la aeronave", "Para controlar la temperatura de la cabina", "Para medir el combustible disponible", "Los controles de vuelo dirigen el movimiento de la aeronave."),
        ("abc", "En Mantenimiento de Aeronaves: ¿cuáles son superficies primarias?", "Los alerones, el timón de profundidad y el timón de dirección", "Los flaps, los spoilers y los compensadores", "El tren de aterrizaje y las puertas", "Las primarias controlan los movimientos principales."),
        ("abc", "En Mantenimiento de Aeronaves: ¿para qué sirve el bloqueo y etiquetado?", "Para impedir que alguien active un sistema que se está trabajando", "Para medir el recorrido de las superficies", "Para calcular el costo de la tarea", "Evita una activación accidental mientras hay personas trabajando."),
        ("abc", "{F} ¿Qué peligro de la matriz puede liberar energía guardada de golpe?", "Los cables de control tensados", "El ruido de la herramienta", "La plataforma elevada", "Un cable tensado guarda energía mecánica."),
        ("abc", "{F} ¿Qué peligro de la matriz se asocia al movimiento inesperado?", "La superficie de control que se mueve al energizar el sistema", "La aeronave elevada sobre gatas", "El ruido de la herramienta neumática", "Una superficie puede moverse sin aviso al energizar."),
        ("abc", "{F} Un permiso de trabajo con bloqueo y etiquetado es un control:", "Administrativo", "De ingeniería", "El equipo de protección personal", "Es una regla de trabajo que ordena la conducta de las personas."),
        ("=", "{F} El hangar asigna 1 persona a cargo de seguridad por cada 7 personas del turno. ¿Cuántas personas se necesitan?", "14//7", "Se divide la dotación entre las personas que cubre cada responsable.", " personas"),
        ("=", "{F} Cada uno de los 2 puestos debe tener 3 etiquetas de bloqueo y el hangar guarda 5 de repuesto. ¿Cuántas etiquetas necesita?", "2*3+5", "Se multiplican los puestos por las etiquetas de cada uno y se suma el repuesto.", " etiquetas"),
        ("=", "Un peligro de ejemplo tiene probabilidad 3 y gravedad 4. Con un control, la probabilidad baja a 1. ¿Cuántos puntos baja el puntaje (probabilidad por gravedad)?", "3*4-1*4", "Se calcula el puntaje antes y después, y se restan.", " puntos"),
        ("abc", "{F} Una persona en práctica dice: «la superficie está quieta, así que puedo apoyar la mano en su borde». ¿Qué respuesta es correcta?", "Es falso: puede moverse al energizar el sistema, y la tarea es de personal autorizado", "Es cierto, si no hay nadie en la cabina", "Es cierto, porque está quieta", "Quieta no significa bloqueada; solo personal autorizado interviene."),
        ("abc", "En una visita a un hangar de ejemplo, una superficie de control comienza a moverse sola con una persona al lado. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a sujetar la superficie", "Tocar el cable para detenerla", "Acercarse puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("=", "{F} El peligro del cable tensado tiene probabilidad 2 y gravedad 4; el de la superficie que se mueve tiene probabilidad 3 y gravedad 5. ¿Cuántos puntos más de puntaje (probabilidad por gravedad) tiene el segundo?", "3*5-2*4", "Se calculan los dos puntajes y se restan.", " puntos"),
        ("abc", "{F} Un compañero dice: «el riesgo del cable es bajo porque está firme». ¿Qué observación es correcta?", "Un cable firme está tensado y puede liberar energía; el riesgo se evalúa con probabilidad y gravedad", "Tiene razón, porque lo firme no se mueve", "Tiene razón, porque los cables no guardan energía", "Estar firme no significa estar sin energía."),
    ],
    ctx=("abc", "Una persona de un hangar de ejemplo te dice: «sostén ese cable mientras muevo la superficie, tú solo mira». ¿Qué respondes?", "Que no, porque tocar cables tensados exige instructor autorizado y norma vigente, y que avisarás a un adulto responsable", "Que sí, si solo lo sostienes", "Que sí, con guantes", "Mover superficies y sostener cables son tareas de personal autorizado."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿cuáles son los tres controles primarios?", "Alerones, timón de profundidad y timón de dirección", "Las primarias controlan los movimientos principales de la aeronave."),
        ("¿Qué puede guardar un cable de control tensado?", "Energía", "Un cable tensado guarda energía mecánica."),
        ("¿Quién interviene las superficies de control?", "Personal capacitado y autorizado", "Esta tarea no es para quien no tiene autorización."),
    ],
    op=("Un hangar de ejemplo anota dos situaciones: (1) un sistema de control energizado con una persona de práctica cerca de la superficie; (2) cables de control tensados sobre un carro. Escribe (a) el peligro y el riesgo de cada una, (b) un control administrativo, (c) la conducta ante un movimiento inesperado de la superficie, (d) por qué el EPP no basta. No describas cómo se interviene.",
        "(a) 1: peligro, la superficie que puede moverse; riesgo, que golpee a alguien. 2: peligro, los cables tensados; riesgo, que liberen energía y lastimen. (b) Un permiso de trabajo con bloqueo y etiquetado. (c) No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias. (d) El EPP es la última barrera y no quita el peligro.",
        ["distingue peligro y riesgo", "propone un control administrativo", "responde con conducta de emergencia", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["decir que sujeta la superficie", "proponer solo el EPP", "describir cómo se interviene"],
        "Pregunta: «¿quién puede actuar y qué debo hacer yo?». Si duda, pídele que relea la conducta de emergencia."),
    reinforce="Escribe las tres superficies primarias y una superficie secundaria, usando solo lo que aprendiste.",
    extend="Explica con un ejemplo por qué una superficie quieta no está necesariamente bloqueada.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 7 (tabla de ejes y superficies de ejemplo, inventada). Eje longitudinal: movimiento de alabeo, superficie primaria: alerones. Eje lateral: movimiento de cabeceo, superficie primaria: timón de profundidad. "
     "Eje vertical: movimiento de guiñada, superficie primaria: timón de dirección. Cuatro fuerzas: sustentación (hacia arriba), peso (hacia abajo), empuje (hacia adelante), resistencia (hacia atrás). Registro de ajustes: la tarjeta guarda 3 valores por superficie.")
build(
    O4, 2, F,
    use="Aprenderé los principios básicos de aerodinámica que explican los controles de vuelo: las cuatro fuerzas, los tres ejes y la relación entre superficies y movimientos.",
    prior=["Sé leer una tabla.", "Sé qué es una superficie de control.", "Sé calcular con enteros."],
    explain=[
        "Sobre una aeronave en vuelo actúan cuatro fuerzas: la sustentación, que la sostiene en el aire hacia arriba; el peso, que la atrae hacia abajo; el empuje, que la impulsa hacia adelante; y la resistencia, que se opone al avance. En vuelo nivelado y constante, las fuerzas opuestas se equilibran. Las superficies de control cambian la forma en que el aire fluye sobre la aeronave y producen movimientos alrededor de tres ejes.",
        "El eje longitudinal va de la nariz a la cola y el movimiento alrededor de él se llama alabeo, que producen los alerones. El eje lateral va de ala a ala y el movimiento se llama cabeceo, que produce el timón de profundidad. El eje vertical atraviesa la aeronave de arriba abajo y el movimiento se llama guiñada, que produce el timón de dirección. El manual de mantenimiento describe cada superficie y sus ajustes.",
        f"Estos principios explican por qué una superficie mal ajustada afecta el vuelo. {EMER} {AVISO}",
    ],
    vocab=[("sustentación", "fuerza que sostiene la aeronave en el aire, hacia arriba"), ("resistencia", "fuerza que se opone al avance de la aeronave"), ("alabeo", "movimiento alrededor del eje longitudinal"), ("cabeceo", "movimiento alrededor del eje lateral"), ("guiñada", "movimiento alrededor del eje vertical"), ("eje", "línea imaginaria alrededor de la cual gira la aeronave")],
    worked=[
        ("Fuerza opuesta", "En vuelo nivelado de ejemplo, ¿qué fuerza se opone al peso?", ["El peso va hacia abajo.", "La que va hacia arriba es la sustentación."], "La sustentación"),
        ("Eje y superficie", "Una aeronave de ejemplo debe girar alrededor del eje vertical. ¿Qué superficie primaria se usa?", ["El eje vertical corresponde a la guiñada.", "La guiñada la produce el timón de dirección."], "El timón de dirección"),
    ],
    mistakes=[("Confundir sustentación con empuje.", "La sustentación sostiene hacia arriba; el empuje impulsa hacia adelante.", "Piensa en la dirección de cada fuerza."),
              ("Asociar el timón de profundidad al alabeo.", "El timón de profundidad produce el cabeceo.", "Relaciona cada eje con su movimiento y su superficie en la tabla.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es la sustentación?", "La fuerza que sostiene la aeronave en el aire, hacia arriba", "La fuerza que la impulsa hacia adelante", "La fuerza que la atrae hacia abajo", "La sustentación actúa hacia arriba; el empuje va adelante y el peso hacia abajo."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es el cabeceo?", "El movimiento alrededor del eje lateral", "El movimiento alrededor del eje vertical", "El movimiento alrededor del eje longitudinal", "El cabeceo sube o baja la nariz; es el giro alrededor del eje lateral."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué superficie primaria produce la guiñada?", "El timón de dirección", "Los alerones", "El timón de profundidad", "El timón de dirección mueve la nariz a izquierda o derecha."),
        ("abc", "{F} ¿Qué fuerza se opone al empuje?", "La resistencia", "La sustentación", "El peso", "La resistencia va hacia atrás, en contra del empuje."),
        ("abc", "{F} ¿Qué superficie primaria produce el alabeo?", "Los alerones", "El timón de profundidad", "El timón de dirección", "La tabla indica que el alabeo lo producen los alerones."),
        ("abc", "{F} ¿Con qué movimiento se relaciona el eje lateral?", "Con el cabeceo", "Con el alabeo", "Con la guiñada", "La tabla asocia el eje lateral al cabeceo."),
        ("=", "{F} La tarjeta guarda 3 valores por cada una de las 3 superficies primarias. ¿Cuántos valores guarda?", "3*3", "Se multiplican las superficies por los valores de cada una.", " valores"),
        ("=", "{F} Si cada una de las cuatro fuerzas se anota con 2 datos en una planilla de ejemplo, ¿cuántos datos hay en total?", "4*2", "Se multiplican las fuerzas por los datos de cada una.", " datos"),
        ("=", "Una aeronave de ejemplo pesa 5.000 unidades y su sustentación es de 4.200 unidades. ¿Cuántas unidades le faltan a la sustentación para equilibrar el peso?", "5000-4200", "Se resta la sustentación al peso para ver lo que falta.", " unidades"),
        ("abc", "{F} Una persona dice: «los alerones producen el cabeceo». ¿Qué observación es correcta?", "Es falso: los alerones producen el alabeo, y el cabeceo lo produce el timón de profundidad", "Es correcto, porque los alerones son los más grandes", "Es correcto, porque el cabeceo es un giro", "La tabla asigna cada superficie a un movimiento distinto."),
        ("abc", "{F} ¿Qué se necesita para que la aeronave cambie de movimiento alrededor de un eje?", "Que una superficie de control cambie el flujo de aire", "Que aumente el empuje del motor", "Que cambie el peso de la aeronave", "Las superficies cambian el flujo de aire y generan el movimiento."),
        ("=", "{F} Una planilla de ejemplo anota una línea por cada fuerza y una línea por cada eje de la ficha. ¿Cuántas líneas necesita?", "4+3", "Se suman las fuerzas y los ejes listados en la ficha.", " líneas"),
        ("abc", "Un técnico de ejemplo dice: «la resistencia no importa en el mantenimiento». ¿Qué observación es correcta?", "Es falsa: una superficie dañada o mal ajustada puede cambiar la resistencia y el comportamiento", "Es correcta, porque solo importa la sustentación", "Es correcta, si la superficie es pequeña", "El estado de las superficies afecta las fuerzas del vuelo."),
    ],
    ctx=("abc", "Una compañera te dice: «ajusta tú el timón de dirección, que una guiñada no se nota». ¿Qué respondes?", "Que no, porque ajustar una superficie exige instructor autorizado y el manual vigente, y que consultarás a un adulto responsable", "Que sí, porque se ve poco", "Que sí, si es un ajuste pequeño", "Cualquier ajuste de una superficie de control es una tarea autorizada."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué movimiento produce el timón de profundidad?", "El cabeceo", "El timón de profundidad sube o baja la nariz."),
        ("¿Qué fuerza se opone a la sustentación?", "El peso", "Una va hacia arriba y la otra hacia abajo."),
        ("¿Qué superficie produce el alabeo?", "Los alerones", "Giran la aeronave alrededor del eje longitudinal."),
    ],
    op=("Planilla de ejemplo: movimientos que se desean en una aeronave de ejemplo: (1) subir la nariz; (2) inclinar un ala hacia abajo; (3) mover la nariz hacia la derecha. Escribe (a) el movimiento de cada caso (alabeo, cabeceo o guiñada), (b) la superficie primaria de cada uno, (c) el eje de cada uno, (d) por qué no ajustas tú ninguna superficie.",
        "(a) 1: cabeceo; 2: alabeo; 3: guiñada. (b) 1: timón de profundidad; 2: alerones; 3: timón de dirección. (c) 1: lateral; 2: longitudinal; 3: vertical. (d) Ajustar superficies exige instructor autorizado, manual vigente y norma; este cuaderno no lo habilita.",
        ["identifica el movimiento", "relaciona con la superficie", "relaciona con el eje", "explica que no ajusta"],
        ["hoja con las respuestas"],
        ["confundir alabeo y cabeceo", "relacionar mal superficie y eje", "proponer un ajuste"],
        "Pregunta: «¿qué dice la tabla de ejes?». Si duda, pídele que relea la ficha."),
    reinforce="Haz un cuadro con tres columnas: eje, movimiento y superficie primaria, y complétalo de memoria.",
    extend="Explica con un ejemplo por qué una superficie dañada puede cambiar la resistencia.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 8 (informe de vuelo de ejemplo, inventado). La persona piloto de una aeronave de ejemplo anota: «con las manos libres de los mandos, la aeronave tiende a inclinarse siempre hacia la derecha». "
     "Tabla de candidatos de ejemplo (no confirmados): alerón izquierdo, alerón derecho, compensador del alerón, cables de control de alerones. Tarjeta de ejemplo: 4 candidatos; cada revisión de papel toma 2 horas; tarifa $14.000 por hora.")
build(
    O4, 3, F,
    use="Aprenderé a analizar en papel un informe de vuelo, a relacionarlo con un eje y a escribir candidatos sin afirmar una causa.",
    prior=["Sé relacionar ejes y superficies.", "Sé distinguir síntoma y causa.", "Sé multiplicar enteros."],
    explain=[
        "Un informe de vuelo anota lo que la persona piloto percibe, como una tendencia a inclinarse hacia un lado. Es un síntoma. Para analizarlo, se identifica el movimiento: inclinarse hacia un lado es alabeo, es decir, un giro alrededor del eje longitudinal. De ahí se listan las superficies y los componentes relacionados, como candidatos a causa, sin confirmar ninguno.",
        "Una causa se confirma con inspección y verificación autorizadas, según el manual. En el informe se escribe el síntoma, el movimiento, los candidatos, lo que no se sabe y a quién se informa. El cálculo de costos y horas de revisión en papel ayuda a planificar. Nunca se afirma «la causa es» sin comprobación.",
        f"Ajustar o reparar una superficie de control es tarea de personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("informe de vuelo", "anotación de lo que percibe la persona piloto en vuelo"), ("tendencia", "inclinación a moverse de una forma sin intervención"), ("candidato a causa", "componente que podría explicar el síntoma y aún no está confirmado"), ("compensador", "pequeña superficie que ayuda a ajustar la tendencia de una superficie mayor"), ("causa confirmada", "causa establecida con inspección y verificación autorizadas")],
    worked=[
        ("Movimiento", "Una persona piloto de ejemplo informa que la nariz tiende a subir sola. ¿Qué movimiento es?", ["La nariz sube y baja en el cabeceo.", "Es un cabeceo."], "Cabeceo"),
        ("Candidatos", "Para un cabeceo no deseado de ejemplo, ¿es el timón de dirección un candidato obvio?", ["El cabeceo lo produce el timón de profundidad.", "El timón de dirección produce guiñada, no es el candidato obvio."], "No; el candidato obvio es el timón de profundidad"),
    ],
    mistakes=[("Escribir «la causa es el alerón derecho» sin comprobación.", "Un candidato no es una causa confirmada.", "Escribe «es un candidato»; la causa la confirma personal autorizado."),
              ("Confundir el síntoma con el movimiento y no identificar el eje.", "El síntoma es lo que se percibe; el movimiento se relaciona con un eje.", "Primero escribe el síntoma, luego el movimiento y el eje.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué anota un informe de vuelo?", "Lo que la persona piloto percibe, como un síntoma", "La causa confirmada de una falla", "El costo de la reparación", "El informe de vuelo registra percepciones, no causas."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es un compensador?", "Una pequeña superficie que ayuda a ajustar la tendencia de una superficie mayor", "Una pieza del tren de aterrizaje", "Un instrumento de la cabina", "El compensador es una superficie pequeña de ajuste."),
        ("abc", "En Mantenimiento de Aeronaves: ¿a qué movimiento corresponde inclinarse hacia un lado?", "Al alabeo", "Al cabeceo", "A la guiñada", "Inclinar un ala hacia abajo es alabeo."),
        ("abc", "{F} ¿Cuál es el síntoma del caso?", "La aeronave tiende a inclinarse hacia la derecha con las manos libres", "El alerón derecho está dañado", "Los cables de control están mal ajustados", "El síntoma es lo percibido; las otras opciones afirman causas."),
        ("abc", "{F} ¿Qué movimiento describe el síntoma?", "Un alabeo, alrededor del eje longitudinal", "Un cabeceo, alrededor del eje lateral", "Una guiñada, alrededor del eje vertical", "Inclinarse hacia un lado es un giro alrededor del eje longitudinal."),
        ("abc", "{F} ¿Qué superficie primaria se relaciona con ese movimiento?", "Los alerones", "El timón de profundidad", "El timón de dirección", "El alabeo lo producen los alerones."),
        ("=", "{F} ¿Cuántas horas suma revisar en papel los 4 candidatos, a 2 horas cada uno?", "4*2", "Se multiplican los candidatos por las horas de cada revisión.", " horas"),
        ("=", "{F} ¿Cuántos pesos cuesta la revisión de un candidato?", "2*14000", "Se multiplican las horas por la tarifa.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta la revisión de los 4 candidatos?", "4*2*14000", "Se multiplican los candidatos, las horas y la tarifa.", " pesos"),
        ("abc", "{F} Un compañero dice: «la causa es el alerón derecho». ¿Qué observación es correcta?", "Es un candidato, no una causa confirmada, y lo confirma personal autorizado", "Es correcto, porque la tendencia es hacia la derecha", "Es correcto, porque solo hay un alerón derecho", "Un candidato no es una causa confirmada."),
        ("abc", "{F} Una persona en práctica propone mover los cables de control «para ver si cambia». ¿Qué corresponde?", "No hacerlo: informar el síntoma y los candidatos al personal certificado", "Hacerlo, si lo hace con cuidado", "Hacerlo, porque es un candidato", "Analizar el informe no autoriza a intervenir."),
        ("=", "{F} Si 2 de los 4 candidatos se descartan con evidencia, ¿cuántos quedan?", "4-2", "Se resta lo descartado al total de candidatos.", " candidatos"),
        ("abc", "{F} ¿Qué frase es correcta en el informe?", "«Tendencia a inclinarse a la derecha; candidatos: alerones, compensador y cables; causa no confirmada»", "«El alerón derecho está malo»", "«Hay que cambiar los cables»", "El informe nombra síntoma y candidatos sin afirmar una causa."),
    ],
    ctx=("abc", "Una persona piloto de ejemplo te dice con certeza «es el compensador, ajústalo». ¿Qué respondes?", "Que lo anotarás como candidato y que la causa y el ajuste los decide personal autorizado", "Que lo ajustas ahora mismo", "Que no hace falta registrar nada", "La certeza no reemplaza la confirmación autorizada."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿un candidato a causa es lo mismo que una causa confirmada?", "No", "El candidato aún no está comprobado."),
        ("¿Qué movimiento es inclinarse hacia un lado?", "Alabeo", "Alabeo es el giro alrededor del eje longitudinal."),
        ("¿Quién confirma una causa?", "Personal autorizado, con inspección y verificación", "El informe solo describe y orienta."),
    ],
    op=("Informe de ejemplo: «la nariz de la aeronave tiende a girar sola hacia la izquierda con los mandos libres». Tabla: candidatos: timón de dirección, compensador del timón de dirección, cables del timón de dirección. Cada revisión de papel toma 3 horas a $13.000 la hora. Escribe (a) el síntoma, (b) el movimiento y el eje, (c) el costo de revisar los tres candidatos, (d) una frase de informe que no afirme una causa.",
        "(a) La nariz tiende a girar sola hacia la izquierda. (b) Guiñada, eje vertical. (c) 3 candidatos × 3 horas × 13.000 = 117.000 pesos. (d) «Tendencia a girar la nariz hacia la izquierda; candidatos: timón de dirección, compensador y cables; causa no confirmada»; se informa a personal certificado.",
        ["identifica síntoma", "relaciona movimiento y eje", "calcula el costo", "no afirma una causa"],
        ["hoja con las cuatro respuestas"],
        ["confundir guiñada con alabeo", "afirmar una causa", "calcular mal"],
        "Pregunta: «¿qué se percibió y qué eje corresponde?». Si duda, pídele que relea la tabla de ejes."),
    reinforce="Inventa un informe de vuelo con una tendencia y escribe el movimiento, el eje y los candidatos.",
    extend="Explica por qué se registran candidatos y no causas cuando falta confirmación.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 9 (tabla de recorridos de ejemplo, inventada). Valores en grados, de ejemplo. Alerón izquierdo: recorrido hacia arriba permitido de 20 a 24; alerón derecho: recorrido hacia arriba permitido de 20 a 24. "
     "Timón de profundidad: recorrido hacia arriba permitido de 25 a 29. Regla de simetría de ejemplo: la diferencia entre los dos alerones no debe pasar de 2 grados. Valores registrados: alerón izquierdo 22; alerón derecho 25; timón de profundidad 27.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar una tabla de recorridos con rangos y una regla de simetría a valores de ejemplo y a escribir una conclusión sin ajustar nada.",
    prior=["Sé comparar enteros con un rango.", "Sé restar enteros.", "Sé que los valores los fija el manual."],
    explain=[
        "El manual de mantenimiento trae una tabla de recorridos: el rango de movimiento que puede tener cada superficie, medido en grados. Un valor está dentro de tolerancia si queda entre el mínimo y el máximo, incluidos ambos. Si queda fuera del rango, se informa. La regla de simetría compara dos superficies a ambos lados, como los alerones: la diferencia entre ellos no debe pasar de un valor máximo.",
        "Para evaluar un valor se identifica la superficie, se busca su rango, se compara y se escribe la conclusión. Para la simetría se resta el menor al mayor. Los valores de este cuaderno son de ejemplo en grados; los reales los fija el fabricante. El registro lleva superficie, valor, rango, conclusión, fecha y firma.",
        f"Medir recorridos reales exige instrumentos calibrados, formación y autorización; ajustar una superficie, también. {EMER} {AVISO}",
    ],
    vocab=[("recorrido", "ángulo que una superficie se mueve desde su posición neutra"), ("rango", "intervalo entre un valor mínimo y uno máximo"), ("dentro de tolerancia", "valor que queda en el rango permitido, incluidos los extremos"), ("simetría", "igualdad dentro de un margen entre dos superficies opuestas"), ("posición neutra", "posición de una superficie cuando no está desviada")],
    worked=[
        ("Dentro del rango", "Un recorrido de ejemplo permitido es de 10 a 14 grados y se mide 12. ¿Está dentro de tolerancia?", ["12 está entre 10 y 14.", "Sí cumple."], "Dentro de tolerancia"),
        ("Simetría", "Dos superficies de ejemplo miden 15 y 18 grados y la regla permite hasta 4 de diferencia. ¿Cumple?", ["La diferencia es 18 menos 15, o sea 3.", "3 no pasa de 4."], "Sí cumple"),
    ],
    mistakes=[("Olvidar que los extremos del rango están incluidos.", "Un valor igual al mínimo o al máximo también cumple.", "Usa «entre» con los dos extremos incluidos."),
              ("Comparar un valor con el rango de otra superficie.", "Cada superficie tiene su rango propio.", "Busca primero la superficie en la tabla.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es un recorrido?", "El ángulo que una superficie se mueve desde su posición neutra", "La distancia entre dos aeronaves", "El tiempo de un vuelo", "El recorrido de una superficie se mide en grados."),
        ("abc", "En Mantenimiento de Aeronaves: ¿cuándo un valor está dentro de tolerancia?", "Cuando queda entre el mínimo y el máximo, incluidos ambos", "Cuando es mayor que el máximo", "Cuando es exactamente el promedio de dos superficies", "La tolerancia es el rango permitido con sus extremos."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué compara una regla de simetría?", "Dos superficies opuestas, con una diferencia máxima permitida", "Una superficie con la hora del día", "Dos aeronaves distintas", "La simetría compara superficies de ambos lados."),
        ("abc", "{F} ¿Qué alerón tiene un recorrido dentro de su rango?", "El izquierdo, con 22", "El derecho, con 25", "Los dos, porque ambos están cerca de 24", "El rango es 20 a 24; 22 cumple y 25 queda fuera."),
        ("abc", "{F} ¿Qué conclusión corresponde al timón de profundidad con 27?", "Dentro de tolerancia, porque 27 está entre 25 y 29", "Fuera de tolerancia, porque 27 es menor que 29", "Fuera de tolerancia, porque es impar", "27 está dentro del rango de 25 a 29."),
        ("abc", "{F} ¿Qué conclusión corresponde al alerón derecho con 25?", "Fuera de tolerancia, porque supera el máximo de 24", "Dentro de tolerancia, porque 25 es cercano a 24", "Dentro de tolerancia, porque está en la tabla", "El máximo es 24 y 25 lo supera."),
        ("=", "{F} ¿Cuántos grados de diferencia hay entre los dos alerones?", "25-22", "Se resta el valor menor al mayor.", " grados"),
        ("=", "{F} ¿Cuántos grados le faltan al alerón izquierdo para llegar al máximo de su rango?", "24-22", "Se resta el valor registrado al máximo.", " grados"),
        ("=", "{F} ¿Cuántos grados sobre el máximo está el alerón derecho?", "25-24", "Se resta el máximo al valor registrado.", " grados"),
        ("abc", "{F} ¿Cumple la regla de simetría de los alerones, con máximo 2 grados de diferencia?", "No, porque la diferencia es 3, mayor que 2", "Sí, porque 3 es menor que 24", "Sí, porque los dos están dentro del rango", "La diferencia entre alerones es 3 y supera el máximo de 2."),
        ("abc", "{F} Una persona en práctica dice: «yo muevo el alerón derecho hasta que cuadre». ¿Qué corresponde?", "No: informar los valores a personal certificado, porque ajustar es tarea autorizada", "Hacerlo, porque es un ajuste pequeño", "Hacerlo, si lo mide dos veces", "Evaluar la tabla no habilita para ajustar."),
        ("=", "{F} Si el alerón izquierdo subiera 2 grados, ¿qué recorrido tendría?", "22+2", "Se suma el aumento al valor registrado.", " grados"),
        ("abc", "{F} ¿Cuál es el resumen correcto de la planilla?", "Fuera: el alerón derecho y la simetría; dentro: el alerón izquierdo y el timón de profundidad", "Todo está dentro de tolerancia", "Solo el timón de profundidad está fuera", "El derecho supera su rango y la diferencia entre alerones supera 2."),
    ],
    ctx=("abc", "En una planilla de ejemplo de otra práctica, un recorrido de 31 en un rango de 25 a 29 está anotado como «dentro». ¿Qué haces?", "Avisas al responsable del registro porque 31 supera el máximo", "Lo dejas, porque ya está firmado", "Cambias el 31 por 29", "Una conclusión errónea se informa; no se altera el dato."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué es la posición neutra?", "La posición de una superficie cuando no está desviada", "Desde esa posición se mide el recorrido."),
        ("¿Se incluyen los extremos de un rango en la tolerancia?", "Sí", "Un valor igual al mínimo o al máximo cumple."),
        ("¿Quién ajusta una superficie fuera de tolerancia?", "Personal autorizado, no quien mide", "Quien mide solo registra e informa, y no ajusta."),
    ],
    op=("Tabla de ejemplo (grados): alerón izquierdo 18 a 22; alerón derecho 18 a 22; simetría máxima 1 grado. Valores: izquierdo 21; derecho 19. Escribe (a) si cada alerón está dentro de su rango, (b) la diferencia entre los dos, (c) si cumple la simetría y por qué, (d) qué haces con la planilla y a quién informas.",
        "(a) Izquierdo 21: dentro; derecho 19: dentro. (b) 21 - 19 = 2 grados. (c) No cumple: 2 es mayor que 1. (d) Registro los valores y la conclusión e informo a personal certificado; no ajusto.",
        ["evalúa el rango", "calcula la diferencia", "aplica la simetría", "informa sin ajustar"],
        ["hoja con las cuatro respuestas"],
        ["decir que cumple la simetría", "calcular mal la diferencia", "proponer un ajuste"],
        "Pregunta: «¿el valor está entre el mínimo y el máximo?». Si duda, pídele que relea la ficha."),
    reinforce="Inventa un rango para una superficie y tres valores, y escribe cuáles están dentro de tolerancia.",
    extend="Explica por qué la simetría de los alerones es importante para el comportamiento de la aeronave.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 10 (extracto en inglés de una tarjeta de ejemplo, inventado). «WARNING: Do not move the control surface without authorization. CAUTION: Use only approved parts. NOTE: Record the date and the work card number.» "
     "Glosario de la tarjeta: do not, no hagas; without, sin; authorization, autorización; use only, usa solo; approved, aprobado; parts, piezas; record, anotar; date, fecha; work card, tarjeta de trabajo; number, número.")
build(
    O5, 1, F,
    use="Aprenderé por qué el inglés técnico es parte del mantenimiento de aeronaves y a reconocer el significado de WARNING, CAUTION y NOTE en un documento.",
    prior=["Sé leer una frase breve con ayuda de un glosario.", "Sé contar elementos de una lista.", "Sé que los manuales traen avisos de seguridad."],
    explain=[
        "Muchos manuales y publicaciones técnicas de aeronaves están escritos en inglés, porque la aviación es internacional. Por eso quien hace mantenimiento debe comprender la información técnica en inglés y usarla con exactitud. Un error al leer un aviso puede causar un accidente. Cuando una palabra no se entiende, no se adivina: se consulta el glosario o a una persona responsable.",
        "Los documentos usan tres tipos de aviso. WARNING advierte de un peligro que puede lesionar a una persona. CAUTION advierte de un peligro que puede dañar equipo o piezas. NOTE entrega información útil que no es un peligro. «Do not» significa «no hagas» y es una prohibición. «Use only» significa «usa solo» y limita una opción. «Record» significa «anotar» en el registro.",
        f"Leer un aviso no te habilita para ejecutar la tarea. {EMER} {AVISO}",
    ],
    vocab=[("WARNING", "aviso de peligro que puede lesionar a una persona"), ("CAUTION", "aviso de peligro que puede dañar equipo o piezas"), ("NOTE", "información útil que no es un peligro"), ("do not", "expresión inglesa que significa «no hagas»"), ("use only", "expresión inglesa que significa «usa solo»"), ("record", "anotar en un registro")],
    worked=[
        ("Aviso de lesión", "Un documento de ejemplo dice: «WARNING: Keep clear of the area». ¿Qué tipo de peligro anuncia?", ["WARNING advierte de peligro para las personas.", "Anuncia riesgo de lesión."], "Peligro para las personas"),
        ("Prohibición", "Un documento de ejemplo dice: «Do not open the panel». ¿Qué significa?", ["«Do not» es una prohibición.", "Significa que no se debe abrir el panel."], "No abras el panel"),
    ],
    mistakes=[("Adivinar el significado de una palabra técnica sin consultar.", "Un error de lectura puede causar un accidente.", "Consulta el glosario o a una persona responsable."),
              ("Tratar un WARNING como si fuera una NOTE.", "WARNING advierte de lesión; NOTE solo informa.", "Lee primero la palabra de encabezado del aviso.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿por qué se estudia inglés técnico?", "Porque muchos manuales y publicaciones técnicas están escritos en inglés", "Porque está prohibido usar manuales en español", "Porque el inglés solo se usa para hablar con la persona piloto", "La aviación es internacional y gran parte de la documentación está en inglés."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué anuncia un aviso WARNING?", "Un peligro que puede lesionar a una persona", "Un peligro que solo puede dañar una pieza", "Una información útil que no es un peligro", "WARNING se refiere a lesiones a personas."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué anuncia un aviso CAUTION?", "Un peligro que puede dañar equipo o piezas", "Un peligro que puede lesionar a una persona", "Una información útil que no es un peligro", "CAUTION se refiere a daños a equipo o piezas."),
        ("abc", "{F} ¿Qué dice el primer aviso del extracto?", "No muevas la superficie de control sin autorización", "Mueve la superficie de control con autorización", "Anota la fecha de la tarjeta", "«Do not move ... without authorization» es una prohibición."),
        ("abc", "{F} ¿Qué significa «Use only approved parts»?", "Usa solo piezas aprobadas", "Usa todas las piezas disponibles", "Usa piezas sin aprobar", "«Use only» limita la opción a lo aprobado."),
        ("abc", "{F} ¿Qué pide la nota (NOTE) del extracto?", "Anotar la fecha y el número de la tarjeta de trabajo", "No mover nada", "Cambiar piezas", "«Record the date and the work card number» pide registrar esos datos."),
        ("=", "{F} El extracto tiene 3 avisos. Una persona los copia en 4 listas de vocabulario distintas. ¿Cuántos avisos copió en total?", "3*4", "Se multiplican los avisos por las listas.", " avisos"),
        ("=", "Un manual de ejemplo tiene 240 páginas y 3 de cada 4 están en inglés. ¿Cuántas páginas están en inglés?", "240*3//4", "Se divide entre 4 y se multiplica por 3 las partes en inglés.", " páginas"),
        ("=", "Una persona en práctica quiere aprender 35 palabras de glosario a razón de 5 por día. ¿Cuántos días necesita?", "35//5", "Se divide el total de palabras entre las que aprende cada día.", " días"),
        ("abc", "{F} Una persona dice: «CAUTION anuncia lesión a las personas, igual que WARNING». ¿Qué observación es correcta?", "Es falsa: CAUTION se refiere a dañar equipo o piezas, y WARNING a lesionar personas", "Es correcta, porque los dos avisos son iguales", "Es correcta, si el texto está en mayúsculas", "Los avisos distinguen el tipo de daño."),
        ("abc", "{F} Una persona de práctica no entiende la palabra «approved» y la supone. ¿Qué corresponde?", "Consultar el glosario o a una persona responsable antes de seguir", "Seguir con la palabra que más se parece", "Saltarse la frase", "Un error de lectura puede causar un accidente; no se adivina."),
        ("=", "{F} Si el glosario traduce 9 palabras y una persona ya conoce 4, ¿cuántas palabras le faltan por aprender?", "9-4", "Se resta lo conocido al total del glosario.", " palabras"),
        ("abc", "{F} ¿Qué aviso debe leerse antes de tocar una superficie de control?", "El WARNING que prohíbe moverla sin autorización", "La NOTE sobre la fecha", "El CAUTION sobre las piezas", "El aviso de peligro y de prohibición va antes de cualquier acción."),
    ],
    ctx=("abc", "Una tarjeta de ejemplo dice «WARNING: Do not touch the cable without authorization» (touch, tocar; cable, cable) y una persona te dice «seguro dice que se puede tocar». ¿Qué haces?", "Le explicas que dice lo contrario y consultas el glosario o a un adulto responsable", "La crees, porque habla con seguridad", "Tocas el cable para comprobarlo", "Leer mal un aviso puede causar un accidente."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué significa «do not»?", "No hagas", "«Do not» expresa una prohibición y no una sugerencia."),
        ("¿Qué tipo de peligro anuncia WARNING?", "Un peligro para las personas", "WARNING se refiere a lesionar personas."),
        ("¿Qué se hace con una palabra que no se entiende?", "Se consulta el glosario o a una persona responsable", "No se adivina el significado de las palabras técnicas."),
    ],
    op=("Extracto de ejemplo: «CAUTION: Use only approved fasteners. WARNING: Do not use the equipment without authorization. NOTE: Record the task number.» Glosario: fasteners, sujetadores; equipment, equipo; task, tarea. Escribe (a) qué dice cada aviso en español, (b) qué aviso se refiere a peligro para las personas, (c) qué hace una persona de práctica con un término que no entiende, (d) por qué leer el aviso no la habilita para ejecutar la tarea.",
        "(a) «Usa solo sujetadores aprobados»; «No uses el equipo sin autorización»; «Anota el número de la tarea». (b) El WARNING. (c) Consulta el glosario o a una persona responsable. (d) Ejecutar la tarea exige instructor autorizado y norma vigente.",
        ["traduce los avisos", "identifica el WARNING", "no adivina palabras", "reconoce que necesita autorización"],
        ["hoja con las cuatro respuestas"],
        ["confundir WARNING con CAUTION", "adivinar una palabra", "ejecutar la tarea"],
        "Pregunta: «¿qué dice el glosario?». Si duda, pídele que relea el significado de cada aviso."),
    reinforce="Haz una tarjeta con WARNING, CAUTION y NOTE, su significado en español y un ejemplo inventado en inglés sencillo.",
    extend="Explica por qué un error de lectura en un aviso puede ser grave.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 11 (tarjeta de pieza en inglés, de ejemplo, inventada). «Part: control cable. P/N: DEM-0042 (example). S/N: 00317 (example). Status: unserviceable. Reference: AMM, flight controls chapter (example).» "
     "Glosario: P/N, part number, número de parte; S/N, serial number, número de serie; serviceable, en condición de uso; unserviceable, fuera de condición de uso; AMM, Aircraft Maintenance Manual, manual de mantenimiento de la aeronave.")
build(
    O5, 2, F,
    use="Aprenderé siglas y términos de los documentos de mantenimiento en inglés y los roles de las personas que los usan.",
    prior=["Sé usar un glosario.", "Sé qué es un manual de mantenimiento.", "Sé restar enteros."],
    explain=[
        "Los documentos en inglés usan siglas. AMM es el Aircraft Maintenance Manual, el manual de mantenimiento de la aeronave. SB es Service Bulletin, boletín de servicio. AD es Airworthiness Directive, directiva de aeronavegabilidad. IPC es Illustrated Parts Catalog, catálogo ilustrado de piezas. WO es work order, orden de trabajo. P/N es part number, el número que identifica el tipo de pieza, y S/N es serial number, el número que identifica una pieza en particular.",
        "Una pieza serviceable está en condición de uso; una unserviceable no lo está y no debe instalarse. Los roles en inglés son: technician, quien ejecuta; inspector, quien verifica de forma independiente; y certifying staff, el personal certificado que libera la aeronave a servicio con un certificado de release to service. Un logbook es el libro de registro de la aeronave y de sus trabajos.",
        f"Una pieza se identifica con P/N y S/N juntos, para no confundirla. {EMER} {AVISO}",
    ],
    vocab=[("AMM", "Aircraft Maintenance Manual: manual de mantenimiento de la aeronave"), ("SB", "Service Bulletin: boletín de servicio"), ("AD", "Airworthiness Directive: directiva de aeronavegabilidad"), ("P/N", "part number: número que identifica el tipo de pieza"), ("S/N", "serial number: número que identifica una pieza en particular"), ("serviceable", "en condición de uso"), ("certifying staff", "personal certificado que libera la aeronave a servicio")],
    worked=[
        ("Sigla", "Un documento de ejemplo menciona «IPC». ¿Qué es?", ["IPC es Illustrated Parts Catalog.", "Es el catálogo ilustrado de piezas."], "El catálogo ilustrado de piezas"),
        ("P/N y S/N", "Dos piezas de ejemplo tienen el mismo P/N y distinto S/N. ¿Son del mismo tipo?", ["El mismo P/N indica el mismo tipo de pieza.", "El S/N distinto identifica unidades diferentes."], "Sí, mismo tipo y unidades distintas"),
    ],
    mistakes=[("Confundir P/N con S/N.", "El P/N identifica el tipo de pieza; el S/N identifica una unidad.", "Lee la sigla completa antes de anotar."),
              ("Considerar una pieza unserviceable como lista para instalar.", "Unserviceable significa fuera de condición de uso.", "Solo piezas serviceable con su documentación completa se usan.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es un AD (Airworthiness Directive)?", "Una disposición obligatoria de la autoridad aeronáutica", "Una recomendación opcional del fabricante", "Una lista de precios de piezas", "AD es la directiva obligatoria; la recomendación es el SB."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué identifica el S/N?", "Una pieza en particular", "El tipo de pieza", "La fecha de compra", "El número de serie identifica una unidad concreta."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué significa «serviceable»?", "En condición de uso", "Fuera de condición de uso", "Pendiente de pago", "Serviceable indica que la pieza puede usarse."),
        ("abc", "{F} ¿Qué número identifica el tipo de pieza en la tarjeta?", "El P/N DEM-0042", "El S/N 00317", "El número del AMM", "El P/N identifica el tipo; el S/N una unidad."),
        ("abc", "{F} ¿Cuál es el estado de la pieza según la tarjeta?", "Unserviceable, fuera de condición de uso", "Serviceable, en condición de uso", "No tiene estado", "La tarjeta dice «unserviceable» en su campo de estado."),
        ("abc", "{F} ¿Qué documento aparece como referencia?", "El AMM, el manual de mantenimiento", "El IPC, el catálogo de piezas", "El AD, la directiva", "La tarjeta dice «Reference: AMM» en su campo de referencia."),
        ("=", "{F} Un lote de ejemplo tiene piezas con S/N desde 00310 hasta 00317, ambos incluidos. ¿Cuántas piezas son?", "317-310+1", "Se restan los extremos y se suma 1 porque ambos se incluyen.", " piezas"),
        ("=", "Un catálogo de ejemplo tiene 120 páginas y una pieza aparece en 1 de cada 6. ¿En cuántas páginas aparece?", "120//6", "Se divide el total de páginas entre 6.", " páginas"),
        ("=", "Una orden de ejemplo (WO) tiene 7 tareas y 3 están terminadas. ¿Cuántas faltan?", "7-3", "Se resta lo terminado al total de tareas.", " tareas"),
        ("abc", "{F} Una persona dice: «el S/N 00317 es el mismo para todas las piezas de ese tipo». ¿Qué observación es correcta?", "Es falsa: el S/N identifica una unidad; el tipo lo identifica el P/N", "Es correcta, porque el S/N es el número de tipo", "Es correcta, si las piezas son nuevas", "El S/N es único para cada unidad."),
        ("abc", "{F} Una persona de práctica dice: «la pieza está unserviceable, pero la instalo igual». ¿Qué corresponde?", "No hacerlo: informar a personal certificado, porque no está en condición de uso", "Hacerlo, si el P/N coincide", "Hacerlo, si tiene un S/N", "Una pieza fuera de condición de uso no debe instalarse."),
        ("abc", "Un técnico de ejemplo ejecuta una tarea y un inspector la verifica. ¿Qué rol libera a servicio la aeronave?", "El certifying staff", "El technician", "El inspector", "La liberación la firma el personal certificado."),
        ("abc", "¿Qué es un logbook en un hangar de ejemplo?", "El libro de registro de la aeronave y de sus trabajos", "Una herramienta de medición", "Una lista de precios", "Es el libro donde se anotan los trabajos."),
    ],
    ctx=("abc", "En un taller de ejemplo, una persona anota solo el S/N de una pieza en el registro. ¿Qué haces?", "Le pides anotar también el P/N, para identificar el tipo de pieza", "Lo aceptas, porque el S/N basta", "Borras el S/N", "La pieza se identifica con P/N y S/N juntos."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué es un SB?", "Un boletín de servicio del fabricante", "Service Bulletin es una recomendación del fabricante."),
        ("¿Qué significa P/N?", "Part number, número que identifica el tipo de pieza", "P/N es la sigla de part number, número de parte."),
        ("¿Quién firma la liberación a servicio?", "El certifying staff", "El certifying staff es el personal certificado de la organización."),
    ],
    op=("Tarjeta de ejemplo: «Part: hose (example). P/N: DEM-0100. S/N: 00850. Status: serviceable. Reference: IPC.» Glosario: hose, manguera. Escribe (a) qué significan P/N, S/N e IPC, (b) el estado de la pieza, (c) qué rol libera la aeronave a servicio, (d) por qué una pieza se identifica con P/N y S/N juntos.",
        "(a) P/N: número de parte; S/N: número de serie; IPC: catálogo ilustrado de piezas. (b) Serviceable, en condición de uso. (c) El certifying staff. (d) El P/N da el tipo y el S/N la unidad; juntos evitan confundir piezas.",
        ["interpreta las siglas", "lee el estado", "nombra el rol", "explica P/N y S/N"],
        ["hoja con las cuatro respuestas"],
        ["confundir P/N y S/N", "decir que el técnico libera", "no usar el glosario"],
        "Pregunta: «¿qué dice el glosario de cada sigla?». Si duda, pídele que relea el vocabulario."),
    reinforce="Haz una tabla con siete siglas inglesas del mantenimiento y su significado en español.",
    extend="Explica por qué un número de serie y un número de parte no son lo mismo.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 12 (tarjeta de tarea en inglés, de ejemplo, inventada). «Task card 07. Title: Inspect the left aileron hinge area. Zone: left wing, trailing edge. Interval: 200 flight hours. Estimated time: 3 hours. "
     "WARNING: Do not move the flight controls without authorization. NOTE: Report any corrosion, cracks or loose parts to the inspector. Sign-off: technician and inspector.» "
     "Glosario: inspect, inspeccionar; left, izquierdo; aileron, alerón; hinge, bisagra; area, zona; wing, ala; inspector, inspector; trailing edge, borde de fuga; flight hours, horas de vuelo; report, informar; cracks, grietas; loose parts, piezas sueltas; sign-off, firma de cierre.")
build(
    O5, 3, F,
    use="Aprenderé a leer una tarjeta de tarea en inglés y a extraer qué se hace, dónde, cada cuánto, qué advertencias hay y quién firma, sin ejecutar la tarea.",
    prior=["Sé usar un glosario.", "Sé qué es una tarjeta de tarea.", "Sé sumar y multiplicar enteros."],
    explain=[
        "Una tarjeta de tarea en inglés se lee por campos. Title dice qué tarea es. Zone dice dónde. Interval dice cada cuánto se repite. Estimated time dice cuánto se estima que tarda. WARNING, CAUTION y NOTE son los avisos. Sign-off dice quiénes firman el cierre. Las palabras de dirección más comunes son left y right, upper y lower, forward y aft (hacia atrás), y inboard y outboard (más cerca o más lejos del fuselaje).",
        "Para comprender la tarjeta: primero se lee el título, luego la zona y los avisos, y recién después el resto. Si aparece una palabra desconocida, se busca en el glosario. Lo que la tarjeta pide informar, como grietas o corrosión, se informa al inspector; no se decide qué hacer. Nunca se salta un WARNING.",
        f"Este ejercicio es de lectura; ejecutar la tarea exige autorización. {EMER} {AVISO}",
    ],
    vocab=[("title", "campo que dice qué tarea es"), ("zone", "campo que dice dónde se hace la tarea"), ("interval", "campo que dice cada cuánto se repite"), ("sign-off", "firma de cierre de la tarea"), ("forward", "hacia adelante"), ("aft", "hacia atrás"), ("inboard", "más cerca del fuselaje")],
    worked=[
        ("Leer el título", "Una tarjeta de ejemplo dice «Title: Inspect the right flap». ¿Qué tarea es?", ["«Inspect» es inspeccionar.", "«Right flap» es el flap derecho."], "Inspeccionar el flap derecho"),
        ("Leer el intervalo", "Una tarjeta de ejemplo dice «Interval: 150 flight hours». ¿Cada cuánto se repite?", ["Interval es el intervalo.", "Se repite cada 150 horas de vuelo."], "Cada 150 horas de vuelo"),
    ],
    mistakes=[("Saltarse el WARNING para ir a la tarea.", "El aviso informa del peligro y la prohibición.", "Lee título, zona y avisos antes que el resto."),
              ("Confundir «left» con «right».", "Cambia la zona de la tarea.", "Confirma el lado con el glosario.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué dice el campo «Zone» de una tarjeta de tarea?", "Dónde se hace la tarea", "Cada cuánto se repite", "Quién firma", "Zone indica la zona de la aeronave."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué significa «aft»?", "Hacia atrás", "Hacia adelante", "Hacia arriba", "Aft es la dirección hacia la cola."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué se hace con un WARNING en una tarjeta?", "Se lee antes de la tarea y se respeta", "Se salta si se tiene experiencia", "Se anota solo al final", "Un aviso de seguridad se lee primero."),
        ("abc", "{F} ¿Qué tarea pide la tarjeta?", "Inspeccionar la zona de las bisagras del alerón izquierdo", "Cambiar el alerón derecho", "Mover los mandos de vuelo", "«Inspect the left aileron hinge area» es esa tarea."),
        ("abc", "{F} ¿Dónde se hace la tarea?", "En el ala izquierda, borde de fuga", "En el ala derecha, borde de ataque", "En el fuselaje, cerca de la puerta", "La zona es «left wing, trailing edge»."),
        ("abc", "{F} ¿Qué debe informarse al inspector?", "Corrosión, grietas o piezas sueltas", "Solo el costo de la tarea", "Solo la hora de término de la tarea", "La nota pide informar corrosión, grietas o piezas sueltas."),
        ("=", "{F} Si la tarea se hizo a las 1.040 horas de vuelo de la aeronave de ejemplo, ¿a qué hora de vuelo corresponde la próxima?", "1040+200", "Se suma el intervalo a la hora de la última ejecución.", " horas de vuelo"),
        ("=", "{F} ¿Cuántos pesos cuesta la mano de obra estimada si la tarifa de ejemplo es $15.000 por hora?", "3*15000", "Se multiplican las horas estimadas por la tarifa.", " pesos"),
        ("=", "{F} La aeronave de ejemplo tiene 1.180 horas de vuelo y la tarea se hizo a las 1.040. ¿Cuántas horas han pasado?", "1180-1040", "Se resta la hora de la última ejecución a la hora actual.", " horas"),
        ("abc", "{F} Una persona dice: «el WARNING me deja mover los mandos si ya terminé». ¿Qué observación es correcta?", "Es falsa: el WARNING prohíbe mover los mandos sin autorización", "Es correcta, si terminó la tarea", "Es correcta, porque el WARNING es una sugerencia", "«Do not move ... without authorization» es una prohibición."),
        ("abc", "{F} Una persona de práctica dice: «veo corrosión en la bisagra, la limpio yo». ¿Qué corresponde según la tarjeta?", "Informar al inspector; no decidir qué hacer", "Limpiarla, para ahorrar tiempo", "Ignorarla, porque está en una bisagra", "La nota pide informar al inspector."),
        ("=", "{F} Si se hacen 2 inspecciones como esta en una misma semana de ejemplo, ¿cuántas horas estimadas suman?", "2*3", "Se multiplican las inspecciones por las horas de cada una.", " horas"),
        ("abc", "{F} ¿Quiénes firman el cierre de la tarjeta?", "El técnico y el inspector", "Solo la persona propietaria", "Nadie, porque es de lectura", "La tarjeta dice «Sign-off: technician and inspector»."),
    ],
    ctx=("abc", "En una tarjeta de ejemplo no entiendes el campo «Zone: aft cargo area». ¿Qué haces?", "Consultas el glosario o a una persona responsable, y no supones la zona", "Supones que es la zona delantera", "Omites el campo y sigues", "No se adivina la zona de una tarea."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué es «Sign-off»?", "La firma de cierre de la tarea", "Deja constancia de quién cerró la tarea."),
        ("¿Qué significa «inboard»?", "Más cerca del fuselaje", "Outboard significa lo contrario de inboard."),
        ("¿A quién se informa una grieta que pide informar la tarjeta?", "Al inspector", "La nota de la tarjeta lo indica así."),
    ],
    op=("Tarjeta de ejemplo: «Title: Inspect the right flap track area. Zone: right wing, trailing edge. Interval: 300 flight hours. Estimated time: 4 hours. WARNING: Do not move the flaps without authorization. NOTE: Report any damage to the inspector.» Glosario: right, derecho; wing, ala; flap, flap; track, riel; damage, daño; inspector, inspector. Escribe (a) qué tarea es y dónde, (b) cada cuánto se repite, (c) qué se informa y a quién, (d) si la tarea se hizo a las 600 horas de vuelo, cuándo corresponde la siguiente.",
        "(a) Inspeccionar la zona del riel del flap derecho, en el ala derecha, borde de fuga. (b) Cada 300 horas de vuelo. (c) Cualquier daño, al inspector. (d) 600 + 300 = 900 horas de vuelo.",
        ["interpreta título y zona", "lee el intervalo", "identifica qué y a quién informa", "calcula la próxima ejecución"],
        ["hoja con las cuatro respuestas"],
        ["confundir lados", "decidir qué hacer con el daño", "calcular mal el intervalo"],
        "Pregunta: «¿qué dicen los campos Title, Zone e Interval?». Si duda, pídele que relea el glosario."),
    reinforce="Inventa una tarjeta en inglés sencillo con cuatro campos y tradúcela.",
    extend="Explica por qué es importante leer el WARNING antes que el resto de la tarjeta.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 13 (tabla en inglés, de ejemplo, inventada). Current aircraft flight hours (FH): 1,450. Task A: last done 1,300 FH; interval 100 FH. Task B: last done 1,400 FH; interval 100 FH. Task C: last done 1,350 FH; interval 200 FH. Task D: last done 1,250 FH; interval 200 FH. "
     "Glosario: current, actual; last done, última ejecución; next due, próximo vencimiento; due, vence hoy; overdue, vencida; not due, aún no vence. En inglés, la coma separa miles (1,450 es mil cuatrocientos cincuenta).")
build(
    O5, 4, F,
    use="Aprenderé a leer números y tablas en inglés y a decidir el estado de una tarea: not due, due u overdue.",
    prior=["Sé sumar y restar enteros.", "Sé qué es un intervalo.", "Sé usar un glosario."],
    explain=[
        "En inglés, la coma separa los miles y el punto separa los decimales: 1,450 se lee «mil cuatrocientos cincuenta» y no «uno coma cuatro cinco cero». Esto es distinto del español de Chile, donde el punto separa los miles. Confundirlos puede cambiar el valor por mil. Por eso se lee con cuidado cada número de un documento en inglés y se confirma con el contexto.",
        "En una tabla de tareas, next due es la hora en que la tarea vence: la última ejecución más el intervalo. Si la hora actual es menor que el next due, la tarea está not due. Si es igual, está due, es decir, vence hoy. Si es mayor, está overdue, vencida. Una tarea overdue se informa a personal certificado, que decide con la norma vigente.",
        f"Calcular estados en papel no autoriza a liberar la aeronave. {EMER} {AVISO}",
    ],
    vocab=[("next due", "hora en que la tarea vence"), ("not due", "tarea que aún no vence"), ("due", "tarea que vence hoy"), ("overdue", "tarea vencida"), ("flight hours (FH)", "horas de vuelo"), ("last done", "última ejecución")],
    worked=[
        ("Leer un número", "Un documento de ejemplo en inglés dice «2,300 FH». ¿Cuántas horas de vuelo son?", ["En inglés la coma separa los miles.", "Son 2.300 horas."], "2.300 horas de vuelo"),
        ("Estado", "Una tarea de ejemplo tiene last done 500 FH, interval 100 FH y la hora actual es 560 FH. ¿Qué estado tiene?", ["El next due es 500 más 100, o sea 600.", "560 es menor que 600: not due."], "Not due"),
    ],
    mistakes=[("Leer «1,450» como un número con decimales.", "En inglés la coma separa miles.", "Lee la coma como separador de miles."),
              ("Calcular el next due restando el intervalo.", "El next due es la última ejecución más el intervalo.", "Suma el intervalo a la hora de la última ejecución.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué significa «1,450 FH» en un documento en inglés?", "Mil cuatrocientos cincuenta horas de vuelo", "Uno coma cuatro cinco cero horas de vuelo", "Catorce horas con cincuenta minutos", "En inglés la coma separa los miles."),
        ("abc", "En Mantenimiento de Aeronaves: ¿cómo se calcula el next due?", "Última ejecución más intervalo", "Última ejecución menos intervalo", "Hora actual más intervalo", "El next due es la hora en que la tarea vence."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué significa «overdue»?", "Tarea vencida", "Tarea que aún no vence", "Tarea terminada", "Overdue indica que el vencimiento ya pasó."),
        ("abc", "{F} ¿Cuál es el next due de la tarea A?", "1,400 FH", "1,300 FH", "1,500 FH", "Se suma el intervalo 100 a la última ejecución 1,300 y da 1,400."),
        ("abc", "{F} ¿Qué estado tiene la tarea A con la hora actual de 1,450 FH?", "Overdue", "Due", "Not due", "El next due 1,400 es menor que 1,450."),
        ("abc", "{F} ¿Qué estado tiene la tarea D?", "Due, porque su next due es 1,450 FH", "Overdue, porque 1,450 es alto", "Not due, porque faltan 200", "1,250 más 200 es 1,450, igual a la hora actual."),
        ("=", "{F} ¿Cuántas FH faltan para que venza la tarea B?", "1500-1450", "Su next due es 1,500; se resta la hora actual.", " FH"),
        ("=", "{F} ¿Cuántas FH faltan para que venza la tarea C?", "1350+200-1450", "Se suma el intervalo a la última ejecución y se resta la hora actual.", " FH"),
        ("=", "{F} ¿Cuántas FH pasó la tarea A de su vencimiento?", "1450-1400", "Se resta el next due a la hora actual.", " FH"),
        ("abc", "{F} Una persona lee «1,300 FH» como «uno coma tres horas». ¿Qué observación es correcta?", "Es falsa: en inglés la coma separa miles, y son mil trescientas horas", "Es correcta, porque la coma es decimal", "Es correcta, si el documento es antiguo", "Confundir el separador cambia el valor por mil."),
        ("abc", "{F} ¿Qué lista contiene solo tareas not due?", "B y C", "A y D", "A, B y C", "B vence a 1,500 y C vence a 1,550; ambas son mayores que 1,450."),
        ("abc", "{F} Una persona dice: «la tarea A está overdue, así que libero la aeronave igual». ¿Qué corresponde?", "No: informar a personal certificado, que decide con la norma vigente", "Liberarla, si la tarea es corta", "Liberarla, si firma el técnico", "La liberación es siempre de personal certificado."),
        ("=", "Una tarea de ejemplo tiene last done 2,100 FH, interval 250 FH y la hora actual es 2,300 FH. ¿Cuántas FH faltan?", "2100+250-2300", "Se suma el intervalo y se resta la hora actual.", " FH"),
    ],
    ctx=("abc", "Una persona a cargo de un hangar de ejemplo te dice: «la tarea overdue puede esperar al próximo viaje, es solo una tarea». ¿Qué respondes?", "Que una tarea overdue se informa a personal certificado, que decide con la norma vigente", "Que sí, porque la tarea es corta", "Que sí, si hay buen clima", "La decisión sobre una tarea vencida es de personal certificado."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué significa «due»?", "Que la tarea vence hoy", "La hora actual es igual al next due."),
        ("¿Qué separa la coma en un número en inglés?", "Los miles", "En inglés 1,450 se lee mil cuatrocientos cincuenta, con coma de miles."),
        ("¿Quién decide qué hacer con una tarea overdue?", "Personal certificado, según la norma vigente", "El técnico no libera la aeronave."),
    ],
    op=("Tabla de ejemplo: current 3,200 FH. Task E: last done 3,000 FH, interval 200 FH. Task F: last done 2,900 FH, interval 250 FH. Task G: last done 3,100 FH, interval 300 FH. Escribe (a) el next due de cada tarea, (b) el estado de cada una (not due, due u overdue), (c) cuántas FH faltan a la que no ha vencido, (d) qué haces con las vencidas.",
        "(a) E: 3,200; F: 3,150; G: 3,400. (b) E: due; F: overdue; G: not due. (c) A G le faltan 3,400 - 3,200 = 200 FH. (d) Las informo a personal certificado, que decide con la norma vigente.",
        ["calcula el next due", "clasifica el estado", "calcula lo que falta", "informa a personal certificado"],
        ["hoja con las cuatro respuestas"],
        ["leer mal la coma", "restar el intervalo", "liberar la aeronave"],
        "Pregunta: «¿cuál es la última ejecución más el intervalo?». Si duda, pídele que relea cómo se calcula el next due."),
    reinforce="Escribe en palabras tres números en inglés con coma, como 1,200 y 3,450, y su valor en horas.",
    extend="Explica por qué confundir la coma con el punto puede cambiar el valor de una hora por mil.",
)
