"""Mecánica de Mantenimiento de Aeronaves TP (3.º y 4.º medio) módulo A: OAE-01 (motores recíprocos y a reacción: conceptos, documentos y límites en planilla) y OAE-02 (sistemas de la aeronave, diagramas y esquemas). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_meae_common import AVISO, EMER, build

O1 = "TP-MEAE-3y4-OAE-01"
O2 = "TP-MEAE-3y4-OAE-02"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Organización Demo de Mantenimiento» atiende aeronaves pequeñas con motor recíproco y aeronaves medianas con motor a reacción. Su matriz de peligros anota: una hélice en giro durante una prueba, "
     "la entrada de aire de una turbina en funcionamiento, ruido intenso, superficies muy calientes tras el funcionamiento y una herramienta olvidada dentro de la zona de un motor. Dotación del turno: 18 personas; el hangar tiene 3 puestos de trabajo.")
build(
    O1, 1, F,
    use="Aprenderé qué es el mantenimiento de aeronaves, qué diferencia a un motor recíproco de uno a reacción, qué peligros tiene un hangar y cómo se ordenan las medidas de prevención.",
    prior=["Sé leer una tabla sencilla.", "Sé multiplicar y dividir números enteros.", "Sé que un lugar de trabajo sigue reglas escritas."],
    explain=[
        "El mantenimiento de aeronaves reúne las tareas que mantienen una aeronave en condición segura de volar: inspecciones, cambios de componentes, reparaciones y registros. Lo hace una organización de mantenimiento reconocida por la autoridad aeronáutica, con personal capacitado, siempre según el manual de mantenimiento del fabricante y las publicaciones técnicas aplicables. Un motor recíproco tiene pistones que suben y bajan dentro de cilindros. Un motor a reacción tiene una turbina que aspira aire por la admisión, lo comprime, lo quema con combustible y expulsa los gases por la tobera.",
        "Un peligro es una fuente que puede causar daño y el riesgo es la posibilidad de que ese daño ocurra. Las medidas se ordenan en la jerarquía de controles, de la más a la menos efectiva: eliminar, sustituir, controles de ingeniería (cambiar el equipo o el lugar), controles administrativos (reglas, señales, recuentos, permisos) y, al final, el equipo de protección personal (EPP). El objeto extraño (FOD, por sus siglas en inglés) es cualquier cosa olvidada o suelta que puede dañar un motor. Los factores humanos son las condiciones que favorecen el error: apuro, cansancio, mala comunicación o falta de información.",
        f"Desarmar, armar y probar un motor es trabajo de personal capacitado, con instructor y autorización. La liberación de una aeronave a servicio la firma siempre personal certificado. {EMER} {AVISO}",
    ],
    vocab=[("mantenimiento de aeronaves", "tareas que mantienen una aeronave en condición segura de volar"), ("motor recíproco", "motor con pistones que se mueven dentro de cilindros"), ("motor a reacción", "motor con turbina que aspira, comprime y expulsa aire y gases"), ("objeto extraño (FOD)", "objeto olvidado o suelto que puede dañar un motor"), ("factores humanos", "condiciones que favorecen el error de las personas"), ("personal certificado", "personas autorizadas por la autoridad para liberar una aeronave a servicio")],
    worked=[
        ("Peligro y riesgo", "En un hangar de ejemplo hay un charco de aceite en el pasillo. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el charco, que puede causar daño.", "El riesgo es que alguien resbale y se lesione."], "Peligro: el charco de aceite; riesgo: que alguien resbale y se lesione"),
        ("Factor humano", "Una persona de ejemplo, apurada por el fin del turno, no revisa si falta alguna de sus piezas pequeñas antes de cerrar un panel. ¿Qué factor humano aparece?", ["Hay apuro por el tiempo.", "El apuro favorece omitir una revisión: es un factor humano."], "El apuro por el tiempo"),
    ],
    mistakes=[("Creer que con casco y guantes basta para trabajar cerca de un motor.", "El EPP es la última barrera y no reemplaza la formación ni la autorización.", "Primero se controla el peligro; el motor lo trabaja personal autorizado."),
              ("Llamar «riesgo» a la herramienta olvidada.", "La herramienta es el peligro; el riesgo es el daño que puede causar.", "Nombra primero el peligro y luego el daño posible.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué diferencia a un motor recíproco de uno a reacción?", "El recíproco mueve pistones en cilindros; el a reacción aspira y comprime aire con una turbina", "El recíproco usa turbina y el a reacción usa pistones", "El recíproco no necesita aire y el a reacción sí", "El recíproco trabaja con pistones y cilindros; la turbina caracteriza al motor a reacción."),
        ("abc", "En Mantenimiento de Aeronaves: ¿quién firma la liberación a servicio de una aeronave tras el mantenimiento?", "El personal certificado", "Cualquier técnico que haya trabajado en la aeronave", "La persona propietaria de la aeronave", "La liberación es una responsabilidad reservada a personal certificado por la autoridad."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué medida es la más efectiva de la jerarquía de controles?", "Eliminar el peligro", "Poner un cartel de advertencia", "Usar equipo de protección personal", "Eliminar quita el peligro; el cartel y el EPP lo dejan presente."),
        ("abc", "{F} ¿Qué peligro de la matriz puede aspirar objetos sueltos hacia el motor?", "La entrada de aire de una turbina en funcionamiento", "El ruido intenso", "Las superficies calientes tras el funcionamiento", "La admisión de una turbina aspira aire con fuerza; el ruido y el calor dañan de otra manera."),
        ("abc", "{F} La herramienta olvidada dentro de la zona de un motor es un ejemplo de:", "Objeto extraño (FOD)", "Desgaste normal de una pieza", "Control de ingeniería", "Un objeto suelto que puede dañar el motor se llama objeto extraño."),
        ("abc", "{F} La organización cuenta sus herramientas al comenzar y al terminar cada trabajo. ¿Qué tipo de control es?", "Un control administrativo", "Un control de ingeniería", "El equipo de protección personal", "Un recuento es una regla de trabajo que ordena la conducta de las personas."),
        ("=", "{F} La organización asigna 1 monitor de seguridad por cada 6 personas de la dotación del turno. ¿Cuántos monitores corresponden?", "18//6", "Se divide la dotación entre las personas que cubre cada monitor.", " monitores"),
        ("=", "Un peligro de ejemplo tiene probabilidad 4 y gravedad 5. Con una medida de control la probabilidad baja a 1 y la gravedad se mantiene. ¿Cuántos puntos baja el puntaje (probabilidad por gravedad)?", "4*5-1*5", "Se calcula el puntaje antes y después, y se restan.", " puntos"),
        ("=", "{F} Cada uno de los 3 puestos de trabajo debe tener 2 señales de zona demarcada y la organización guarda 4 señales más de repuesto. ¿Cuántas señales necesita?", "3*2+4", "Se multiplican los puestos por las señales de cada uno y se suma el repuesto.", " señales"),
        ("abc", "{F} Un aprendiz dice: «terminé de armar la unidad, así que libero la aeronave a servicio». ¿Qué respuesta es correcta?", "Es falso: la liberación a servicio la firma personal certificado", "Es cierto, si el trabajo quedó bien hecho", "Es cierto, si otra persona del turno lo mira", "Hacer el trabajo no habilita para liberar la aeronave; esa firma es de personal certificado."),
        ("abc", "En una visita a un hangar de ejemplo, de un motor sale humo y se oye un golpe fuerte. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte con cuidado para ver de dónde sale el humo", "Esperar junto a la entrada a que se apague solo", "Acercarse puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("=", "{F} El peligro A de una matriz de ejemplo tiene probabilidad 3 y gravedad 5; el peligro B tiene probabilidad 2 y gravedad 4. ¿Cuántos puntos más de puntaje (probabilidad por gravedad) tiene A que B?", "3*5-2*4", "Se calculan los dos puntajes y se restan.", " puntos"),
        ("abc", "{F} Un compañero dice: «el riesgo de la herramienta olvidada es bajo porque es pequeña». ¿Qué observación es correcta?", "El tamaño no define el riesgo: un objeto pequeño dentro de un motor puede causar un daño grave", "Tiene razón, porque el daño depende solo del tamaño del objeto", "Tiene razón, porque el motor tritura cualquier objeto sin consecuencias", "El riesgo se evalúa con la probabilidad y la gravedad del daño, no con el tamaño del objeto."),
    ],
    ctx=("abc", "Un jefe de turno de ejemplo te dice: «ven a ayudarme a hacer funcionar ese motor, tú ya conoces el manual». ¿Qué respondes?", "Que no, porque probar un motor exige instructor autorizado y norma vigente, y que consultarás a un adulto responsable", "Que sí, porque conocer el manual es suficiente", "Que sí, pero solo si el motor es pequeño", "Conocer el manual no habilita para probar un motor; hace falta autorización."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué es un objeto extraño (FOD)?", "Un objeto olvidado o suelto que puede dañar un motor", "FOD nombra a los objetos que no deberían estar en la zona de un motor."),
        ("En Mantenimiento de Aeronaves: ¿cuál es el último nivel de la jerarquía de controles?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("¿Quién firma la liberación de una aeronave a servicio?", "El personal certificado", "Solo personal certificado puede firmar esa liberación."),
    ],
    op=("Un hangar de ejemplo anota dos tareas: (1) pedir a una persona en práctica que «ayude» a hacer funcionar un motor mientras otras personas pasan por el pasillo; (2) un compañero que lleva muchas horas seguidas sin descanso y no recibió la información escrita del turno anterior. Escribe (a) el peligro y el riesgo de la tarea 1, (b) un control administrativo para esa tarea, (c) un factor humano de la tarea 2 y una medida que lo reduzca, (d) por qué el EPP no basta y quién hace estas tareas. No describas cómo se hacen.",
        "(a) Peligro: el motor en funcionamiento; riesgo: que alguien sea alcanzado por una pieza o por los gases. (b) Una regla escrita y una señal de que solo personal autorizado entra a la zona. (c) El cansancio o la falta de información; una medida: descansos y un traspaso escrito entre turnos. (d) El EPP es la última barrera: no quita el peligro. Las tareas las hace personal autorizado con norma vigente.",
        ["distingue peligro y riesgo", "propone un control administrativo", "nombra un factor humano y una medida", "explica por qué el EPP no basta y quién hace la tarea"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al motor", "proponer solo el EPP", "describir cómo se hace la tarea"],
        "Pregunta: «¿qué medida quitaría o alejaría el peligro?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe los cinco niveles de la jerarquía de controles en orden y pon junto a cada uno un ejemplo inventado de un hangar de mantenimiento.",
    extend="Explica con un ejemplo por qué un cartel de advertencia no reemplaza a un control de ingeniería.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (tarjeta de tarea de ejemplo, inventada). Tarjeta TT-114 de la «Organización Demo de Mantenimiento»: «Inspección periódica de un motor recíproco», aeronave de ejemplo matrícula «XX-DEM», motor «Motor Demo R-4» de 4 cilindros. "
     "Horas del motor: 1.185 h. Última inspección: a las 1.080 h. Intervalo de la tarea: cada 100 h. Horas estimadas: 6. Tarifa de mano de obra de ejemplo: $15.000 por hora.")
build(
    O1, 2, F,
    use="Aprenderé las partes principales de los motores recíprocos y a reacción, qué documentos guían su mantenimiento y qué hace cada rol.",
    prior=["Sé leer una tarjeta o ficha con datos.", "Sé restar y multiplicar números enteros.", "Sé que un manual fija reglas del trabajo."],
    explain=[
        "Un motor recíproco tiene cilindros, pistones, un cigüeñal que convierte el vaivén en giro y válvulas que abren y cierran. Su ciclo de cuatro tiempos es: admisión, compresión, combustión y escape. Un motor a reacción sigue este orden: admisión de aire, compresor, cámara de combustión, turbina y tobera. La turbina mueve al compresor con parte de la energía de los gases.",
        "El manual de mantenimiento del fabricante fija las tareas, los límites y los intervalos. Las publicaciones técnicas incluyen los boletines de servicio, que son recomendaciones del fabricante, y las directivas de aeronavegabilidad, que son disposiciones obligatorias de la autoridad aeronáutica. La tarjeta de tarea baja una tarea del manual a una hoja con espacios para anotar y firmar. La orden de trabajo registra la aeronave, la tarea, las horas y el costo, y el registro del motor guarda su historia.",
        f"El técnico ejecuta, el inspector verifica de forma independiente, y el personal certificado libera la aeronave a servicio. Las horas que faltan para una tarea se calculan con el intervalo menos las horas transcurridas desde la última vez. {EMER} {AVISO}",
    ],
    vocab=[("cilindro", "tubo donde se mueve un pistón en un motor recíproco"), ("compresor", "parte del motor a reacción que comprime el aire"), ("tobera", "salida por donde se expulsan los gases de un motor a reacción"), ("boletín de servicio", "recomendación del fabricante sobre una modificación o inspección"), ("directiva de aeronavegabilidad", "disposición obligatoria de la autoridad aeronáutica"), ("tarjeta de tarea", "hoja que baja una tarea del manual con espacios para anotar y firmar"), ("inspector", "persona que verifica un trabajo de forma independiente")],
    worked=[
        ("Ciclo de cuatro tiempos", "En un motor recíproco de ejemplo, ¿qué tiempo viene justo después de la compresión?", ["El orden es admisión, compresión, combustión y escape.", "Tras comprimir, sigue la combustión."], "La combustión"),
        ("Horas que faltan", "Un motor de ejemplo lleva 2.060 h, su última revisión fue a las 1.990 h y el intervalo es de 100 h. ¿Cuántas horas faltan?", ["Han pasado 2.060 menos 1.990, o sea 70 h.", "Faltan 100 menos 70, o sea 30 h."], "30 horas"),
    ],
    mistakes=[("Creer que un boletín de servicio es siempre obligatorio.", "Es una recomendación del fabricante; se vuelve obligatorio si la autoridad lo emite como directiva.", "Pregunta quién emite el documento y si es una disposición obligatoria."),
              ("Dejar que quien ejecutó la tarea sea la única persona que la verifica.", "La verificación debe ser independiente para detectar errores.", "Un inspector distinto revisa el resultado y firma aparte.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿cuál es el orden de las etapas de un motor a reacción?", "Admisión, compresor, cámara de combustión, turbina y tobera", "Cámara de combustión, compresor, admisión, tobera y turbina", "Turbina, admisión, cámara de combustión, compresor y tobera", "El aire entra, se comprime, se quema con combustible, mueve la turbina y sale por la tobera."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es una tarjeta de tarea?", "Una hoja que baja una tarea del manual con espacios para anotar y firmar", "Una licencia personal para trabajar en cualquier aeronave", "Una factura de repuestos del hangar", "La tarjeta organiza la tarea y deja constancia; no es una licencia ni una factura."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es una directiva de aeronavegabilidad?", "Una disposición obligatoria emitida por la autoridad aeronáutica", "Una sugerencia opcional del fabricante", "Una lista de precios de repuestos", "La directiva obliga; la sugerencia opcional corresponde al boletín de servicio."),
        ("abc", "{F} ¿Qué componente propio de un motor recíproco aparece nombrado en la ficha?", "Los cilindros", "El compresor", "La tobera", "El compresor y la tobera son partes de un motor a reacción, no de uno recíproco."),
        ("abc", "{F} ¿Qué rol verifica que la tarea cumpla lo que pide la tarjeta, de forma distinta a quien la ejecutó?", "El inspector", "El jefe de bodega", "La persona propietaria de la aeronave", "El inspector da una verificación independiente de quien hizo el trabajo."),
        ("abc", "{F} ¿Qué documento fija los límites y los intervalos de la tarea de la ficha?", "El manual de mantenimiento del fabricante", "La orden de trabajo", "El registro del motor", "El manual fija límites e intervalos; la orden y el registro solo dejan constancia."),
        ("=", "{F} ¿Cuántas horas han pasado desde la última inspección?", "1185-1080", "Se resta la hora de la última inspección a las horas actuales del motor.", " horas"),
        ("=", "{F} ¿Cuántos pesos cuesta la mano de obra estimada de la tarea?", "6*15000", "Se multiplican las horas estimadas por la tarifa por hora.", " pesos"),
        ("=", "Otro motor de ejemplo lleva 2.340 h, su última inspección fue a las 2.290 h y el intervalo es de 100 h. ¿Cuántas horas faltan para la próxima?", "100-(2340-2290)", "Se resta del intervalo lo que ya transcurrió desde la última inspección.", " horas"),
        ("abc", "{F} ¿Está vencida la tarea de la ficha?", "Sí, porque lo transcurrido desde la última inspección supera el intervalo", "No, porque aún no llega a las 1.200 h del motor", "No, porque el intervalo se cuenta desde las 0 h del motor", "Si lo transcurrido supera el intervalo, la tarea está vencida."),
        ("abc", "Un compañero dice: «el boletín de servicio del fabricante siempre es obligatorio». ¿Qué observación es correcta?", "No siempre: es una recomendación y se vuelve obligatoria si la autoridad la emite como directiva", "Es correcta, porque todo documento del fabricante obliga por ley", "Es correcta, porque el boletín reemplaza al manual", "El boletín recomienda; la obligación la fija una directiva de la autoridad."),
        ("=", "{F} Si la tarea se repite cada 100 h y la última inspección fue a las 1.080 h, ¿a qué hora del motor correspondía la siguiente?", "1080+100", "Se suma el intervalo a la hora de la última inspección.", " horas"),
        ("abc", "Una tarjeta de tarea de ejemplo tiene todos sus pasos marcados, pero sin firma ni fecha. ¿Qué corresponde pensar?", "Está incompleta: falta dejar constancia de quién la hizo y cuándo", "Está completa si el trabajo salió bien", "Basta con que alguien la firme el mes siguiente sin saber quién la hizo", "El registro necesita quién, cuándo y qué; sin firma ni fecha no hay trazabilidad."),
    ],
    ctx=("abc", "Una persona en práctica te ofrece una tarjeta de tarea ya firmada «para ahorrar tiempo» y no sabe quién la llenó. ¿Qué haces?", "No la usas como registro y avisas a un adulto responsable, porque una firma sin autor verificable no sirve", "La usas, porque una firma ya vale como registro", "La usas si la fecha es de hoy", "Un registro firmado sin autor identificable no es confiable."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué parte de un motor a reacción comprime el aire?", "El compresor", "El compresor comprime el aire antes de la cámara de combustión."),
        ("¿Qué tiempo del motor recíproco sigue a la combustión?", "El escape", "El orden es admisión, compresión, combustión y escape."),
        ("¿Quién emite una directiva de aeronavegabilidad?", "La autoridad aeronáutica", "Es una disposición de la autoridad, no del fabricante."),
    ],
    op=("Ficha de ejemplo: orden OT-B-52 de un motor a reacción de ejemplo con 3.420 h. Última revisión de una tarea: 3.340 h. Intervalo: 100 h. Horas estimadas: 4. Tarifa: $18.000 por hora. Escribe (a) cuántas horas faltan para la tarea, (b) el costo de la mano de obra, (c) qué documento fija el intervalo y qué documento deja constancia del trabajo, (d) qué rol verifica y qué rol libera a servicio.",
        "(a) Han pasado 3.420 - 3.340 = 80 h; faltan 100 - 80 = 20 h. (b) 4 × 18.000 = 72.000 pesos. (c) El manual de mantenimiento fija el intervalo; la tarjeta de tarea y la orden de trabajo dejan constancia. (d) El inspector verifica y el personal certificado libera a servicio.",
        ["calcula las horas que faltan", "calcula el costo", "distingue manual y registro", "distingue inspector y personal certificado"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "confundir manual con orden de trabajo", "decir que el técnico libera a servicio"],
        "Pregunta: «¿cuántas horas han pasado y cuánto dice el intervalo?». Si duda, pídele que relea cómo se calculan las horas que faltan."),
    reinforce="Dibuja en tu cuaderno las cinco etapas de un motor a reacción en orden y los cuatro tiempos de un motor recíproco, con una flecha entre cada una.",
    extend="Explica con un ejemplo por qué un boletín de servicio puede volverse obligatorio.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (registro de funcionamiento de ejemplo, inventado). Motor a reacción «Motor Demo T-2». Límites de ejemplo: temperatura de gases 650 unidades; vibración 40 unidades. "
     "Lecturas por vuelo (de ejemplo): vuelo 1: temperatura 610, vibración 21; vuelo 2: temperatura 614, vibración 22; vuelo 3: temperatura 621, vibración 25; vuelo 4: temperatura 633, vibración 31.")
build(
    O1, 3, F,
    use="Aprenderé a analizar en papel un registro de funcionamiento: comparar lecturas con un límite, ver una tendencia y decidir a quién informar.",
    prior=["Sé restar números enteros.", "Sé leer una tabla de varias columnas.", "Sé que los límites los fija el manual del fabricante."],
    explain=[
        "Un registro de funcionamiento anota lecturas del motor después de cada vuelo: temperatura, vibración, consumo de aceite y otras. Cada lectura se compara con un límite del manual. Si la lectura supera el límite, hay una discrepancia que se informa. Una tendencia es la forma en que cambia una lectura a lo largo del tiempo: si sube vuelo tras vuelo, aunque siga bajo el límite, conviene avisar antes de que lo alcance.",
        "Para estudiar una tendencia se calcula la diferencia entre lecturas consecutivas y se compara con el margen que queda hasta el límite. El margen es el límite menos la lectura actual. Quien analiza el registro no repara ni prueba el motor: anota la observación y la informa al personal certificado, que decide el paso siguiente según el manual.",
        f"Decir «el motor está mal» sin datos no sirve. Un buen análisis nombra la lectura, el límite, el margen y la tendencia. {EMER} {AVISO}",
    ],
    vocab=[("registro de funcionamiento", "planilla con las lecturas del motor después de cada vuelo"), ("lectura", "valor medido y anotado de una magnitud"), ("límite", "valor máximo o mínimo permitido por el manual"), ("margen", "diferencia entre el límite y la lectura actual"), ("tendencia", "forma en que cambia una lectura a lo largo del tiempo"), ("discrepancia", "diferencia entre lo observado y lo que el manual permite")],
    worked=[
        ("Margen", "Un motor de ejemplo tiene límite de consumo de aceite de 8 unidades por vuelo y una lectura de 5. ¿Cuál es el margen?", ["El margen es el límite menos la lectura.", "8 menos 5 son 3."], "3 unidades"),
        ("Tendencia", "Lecturas de ejemplo de presión de aceite: 52, 50, 47. ¿Sube o baja la tendencia y cuánto cambió entre la primera y la última?", ["Los valores van disminuyendo vuelo tras vuelo.", "Entre 52 y 47 bajó 5 unidades."], "Baja; cambió 5 unidades"),
    ],
    mistakes=[("Pensar que mientras la lectura esté bajo el límite no hay nada que informar.", "Una tendencia que sube sostenidamente puede llegar al límite pronto.", "Calcula el margen y la diferencia entre lecturas antes de concluir."),
              ("Intentar «arreglar» el motor al ver una discrepancia en el registro.", "Analizar el registro no habilita a intervenir el motor.", "Anota la lectura, el límite y la tendencia e informa a personal certificado.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es una tendencia en un registro de funcionamiento?", "La forma en que cambia una lectura a lo largo del tiempo", "El valor máximo que permite el manual", "La firma de quien tomó la lectura", "La tendencia mira el cambio en el tiempo; el valor máximo es el límite."),
        ("abc", "En Mantenimiento de Aeronaves: ¿cómo se calcula el margen de una lectura?", "Límite menos lectura actual", "Lectura actual menos la lectura del primer vuelo", "Límite más lectura actual", "El margen mide cuánto falta para llegar al límite."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué se hace ante una discrepancia en el registro?", "Se anota con sus datos y se informa al personal certificado", "Se borra la lectura y se vuelve a tomar hasta que salga bien", "Se espera a que el motor falle para actuar", "Se informa con datos; borrar lecturas oculta información necesaria."),
        ("abc", "{F} ¿En cuál vuelo hubo la mayor lectura de vibración?", "En el vuelo 4", "En el vuelo 1", "En el vuelo 2", "Las lecturas de vibración suben de 21 a 31, y la mayor es la del vuelo 4."),
        ("abc", "{F} ¿Alguna lectura de temperatura supera el límite de 650?", "No, todas son menores que 650", "Sí, la del vuelo 4", "Sí, la del vuelo 3", "La mayor temperatura es 633, que aún es menor que el límite de 650."),
        ("abc", "{F} ¿Cómo describe la tendencia de la temperatura?", "Sube en cada vuelo", "Baja en cada vuelo", "Se mantiene igual en los cuatro vuelos", "Las lecturas 610, 614, 621 y 633 aumentan de un vuelo al siguiente."),
        ("=", "{F} ¿Cuántas unidades de margen quedan en la temperatura del vuelo 4?", "650-633", "Se resta la lectura actual al límite.", " unidades"),
        ("=", "{F} ¿Cuántas unidades subió la vibración entre el vuelo 1 y el vuelo 4?", "31-21", "Se resta la primera lectura a la última.", " unidades"),
        ("=", "{F} ¿Cuántas unidades subió la temperatura entre el vuelo 3 y el vuelo 4?", "633-621", "Se resta la lectura del vuelo 3 a la del vuelo 4.", " unidades"),
        ("abc", "{F} Un compañero dice: «la vibración está bajo 40, así que no hay nada que informar». ¿Qué observación es correcta?", "Aunque esté bajo el límite, sube vuelo tras vuelo y conviene informarlo con sus datos", "Tiene razón, porque solo se informa cuando se supera el límite", "Tiene razón, porque la vibración nunca importa si la temperatura está bajo su límite", "Una tendencia creciente es una señal que se informa antes de llegar al límite."),
        ("abc", "{F} Al ver la tabla, una persona en práctica propone «abrir el motor para ver qué pasa». ¿Qué corresponde?", "No hacerlo: informar los datos al personal certificado, que decide según el manual", "Hacerlo, porque la tendencia lo exige", "Hacerlo, si lo hace con guantes", "El análisis del registro no autoriza a intervenir el motor."),
        ("=", "{F} Si la vibración siguiera subiendo 6 unidades por vuelo, ¿cuántas unidades tendría en el vuelo 6, tomando como base el vuelo 4?", "31+6*2", "Del vuelo 4 al 6 hay 2 vuelos, cada uno suma 6 unidades.", " unidades"),
        ("abc", "{F} ¿Qué dato debe incluir un informe claro sobre el vuelo 4?", "Las lecturas, los límites, el margen y la tendencia", "Solo la frase «el motor se ve raro»", "Solo la temperatura del primer vuelo", "Un informe con datos permite decidir; una opinión sin números no."),
    ],
    ctx=("abc", "Al repasar un registro de ejemplo, ves que la temperatura de gases de otro motor subió tres vuelos seguidos, pero sigue bajo el límite máximo. ¿Qué haces?", "Anotas la tendencia con sus datos y la informas al personal certificado", "No haces nada porque aún está sobre el límite", "Cambias tú la lectura para que se vea estable", "Una tendencia que empeora se informa aunque no haya superado el límite."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué es el margen?", "La diferencia entre el límite y la lectura actual", "El margen dice cuánto falta para llegar al límite."),
        ("¿A quién se informa una discrepancia del registro?", "Al personal certificado", "Esa persona decide el paso siguiente según el manual."),
        ("¿Qué muestra una lectura que sube vuelo tras vuelo?", "Una tendencia creciente", "La tendencia describe el cambio a lo largo de los vuelos."),
    ],
    op=("Registro de ejemplo de otro motor a reacción: límite de temperatura 705 unidades. Lecturas por vuelo: vuelo 1: 655; vuelo 2: 662; vuelo 3: 671; vuelo 4: 683. Escribe (a) el margen del vuelo 4, (b) cuánto subió la temperatura entre el vuelo 1 y el vuelo 4, (c) si hay discrepancia y por qué, (d) qué informas y a quién, sin proponer cómo reparar nada.",
        "(a) 705 - 683 = 22 unidades. (b) 683 - 655 = 28 unidades. (c) No supera el límite, pero la tendencia sube en cada vuelo y el margen es pequeño. (d) Informo las cuatro lecturas, el límite, el margen y la tendencia al personal certificado, que decide según el manual.",
        ["calcula el margen", "calcula el cambio", "distingue límite superado de tendencia", "informa con datos y a la persona correcta"],
        ["hoja con las cuatro respuestas"],
        ["restar mal el margen", "decir que no hay nada que informar", "proponer una reparación"],
        "Pregunta: «¿cuántas unidades faltan para el límite y cómo han cambiado las lecturas?». Si duda, pídele que relea qué es el margen."),
    reinforce="Inventa cuatro lecturas de una magnitud de un motor y un límite, calcula el margen del último dato y escribe si la tendencia sube o baja.",
    extend="Explica por qué una lectura bajo el límite también puede merecer un aviso.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (tabla de límites de ejemplo, inventada). Medidas en centésimas de milímetro, valores de ejemplo. Holgura máxima permitida entre un pistón y su cilindro: 45. Espesor mínimo permitido de una pieza de ejemplo: 120. Medidas registradas: cilindro 1: holgura 38; cilindro 2: holgura 45; "
     "cilindro 3: holgura 47; pieza X: espesor 125; pieza Y: espesor 119.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar en papel un límite máximo o mínimo a medidas de ejemplo y a escribir un registro correcto de «dentro» o «fuera de límites».",
    prior=["Sé comparar números enteros.", "Sé leer una tabla de límites.", "Sé que las medidas de ejemplo no son valores reales."],
    explain=[
        "En el manual de mantenimiento hay tablas de límites. Un límite máximo dice hasta dónde puede llegar una medida; un límite mínimo dice desde dónde puede bajar. Una medida está dentro de límites si cumple el límite: igual o menor que el máximo, o igual o mayor que el mínimo. Si no lo cumple, está fuera de límites. Una tolerancia es el rango permitido alrededor de un valor nominal, que es el valor de diseño.",
        "El registro de una medida lleva: la pieza, el valor medido, el límite de la tabla, la comparación y la conclusión «dentro» o «fuera de límites», con fecha y firma. Quien tiene medidas fuera de límites no decide por su cuenta si la pieza se repara o se cambia: informa a personal certificado, según el manual. Las medidas de este cuaderno son números de ejemplo escritos en centésimas de milímetro; las reales las fija el fabricante.",
        f"Medir piezas de un motor real exige instrumentos calibrados, formación y autorización. {EMER} {AVISO}",
    ],
    vocab=[("límite máximo", "valor que una medida no debe superar"), ("límite mínimo", "valor bajo el cual una medida no debe quedar"), ("dentro de límites", "medida que cumple el límite de la tabla"), ("fuera de límites", "medida que no cumple el límite de la tabla"), ("valor nominal", "valor de diseño de una medida"), ("tolerancia", "rango permitido alrededor del valor nominal"), ("holgura", "espacio libre entre dos piezas que encajan")],
    worked=[
        ("Límite máximo", "Una tabla de ejemplo fija una holgura máxima de 30 y una medida registrada es 28. ¿Está dentro de límites?", ["El límite es máximo: la medida no debe pasar de 30.", "28 es menor que 30: está dentro."], "Dentro de límites"),
        ("Límite mínimo", "Una tabla de ejemplo fija un espesor mínimo de 80 y la medida es 79. ¿Está dentro de límites?", ["El límite es mínimo: la medida debe ser 80 o más.", "79 queda bajo 80: está fuera."], "Fuera de límites"),
    ],
    mistakes=[("Aplicar un límite mínimo como si fuera máximo.", "Con un mínimo, una medida mayor es aceptable y una menor no.", "Antes de comparar, lee si la tabla dice máximo o mínimo."),
              ("Decidir por cuenta propia cambiar o reparar la pieza que quedó fuera de límites.", "Esa decisión corresponde a personal certificado según el manual.", "Registra la medida, el límite y la conclusión, e informa.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿cuándo una medida cumple un límite máximo?", "Cuando es igual o menor que el límite", "Cuando es mayor que el límite", "Cuando es exactamente la mitad del límite", "Un máximo es el tope: la medida puede llegar a él pero no pasarlo."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es el valor nominal?", "El valor de diseño de una medida", "El valor medido en la última revisión", "El límite más alto de la tabla", "El nominal es el valor de diseño; la tolerancia es el rango alrededor de él."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué lleva un registro de medida bien hecho?", "Pieza, valor medido, límite, conclusión, fecha y firma", "Solo la palabra «bien» y la fecha", "Solo el valor medido, sin la pieza", "Un registro debe permitir a otra persona reconstruir qué se midió, contra qué y con qué resultado."),
        ("abc", "{F} ¿Cuál cilindro tiene una holgura fuera de límites?", "El cilindro 3, con 47", "El cilindro 1, con 38", "El cilindro 2, con 45", "El máximo es 45 y solo el 47 lo supera; el 45 queda en el límite y es aceptable."),
        ("abc", "{F} ¿Qué conclusión se anota para la pieza Y, con espesor 119?", "Fuera de límites, porque está bajo el mínimo de 120", "Dentro de límites, porque 119 es un número alto", "Dentro de límites, porque está cerca de 120", "Con un mínimo de 120, un espesor de 119 queda por debajo."),
        ("abc", "{F} ¿Qué conclusión se anota para el cilindro 2, con holgura 45?", "Dentro de límites, porque 45 es igual al máximo permitido", "Fuera de límites, porque 45 no es menor que 45", "Fuera de límites, porque está justo en el borde", "Igual al máximo cumple el límite; el borde no se considera fuera."),
        ("=", "{F} ¿Cuántas centésimas de milímetro de margen tiene el cilindro 1 respecto de la holgura máxima?", "45-38", "Se resta la holgura medida al máximo permitido.", " centésimas"),
        ("=", "{F} ¿Cuántas centésimas de milímetro pasa el cilindro 3 el máximo permitido?", "47-45", "Se resta el máximo a la holgura medida.", " centésimas"),
        ("=", "{F} ¿Cuántas centésimas de milímetro de margen tiene la pieza X sobre el espesor mínimo?", "125-120", "Se resta el mínimo al espesor medido.", " centésimas"),
        ("abc", "{F} Una persona de práctica dice: «el cilindro 3 está fuera de límites, así que lo cambio yo ahora». ¿Qué observación es correcta?", "Debe registrar la medida y el límite e informar, porque la decisión es de personal certificado según el manual", "Tiene razón, porque fuera de límites siempre se cambia de inmediato", "Tiene razón, si primero pide permiso a un compañero", "Estar fuera de límites no autoriza a intervenir; hay que informar."),
        ("abc", "{F} ¿Cuál es la lista correcta de piezas fuera de límites?", "Cilindro 3 y pieza Y", "Cilindro 2 y pieza X", "Cilindro 1 y cilindro 2", "Solo el cilindro 3 supera el máximo y solo la pieza Y queda bajo el mínimo."),
        ("=", "{F} Si la holgura del cilindro 1 aumentara 9 centésimas, ¿qué medida tendría?", "38+9", "Se suma el aumento a la holgura medida.", " centésimas"),
        ("abc", "Una tabla de ejemplo dice «espesor mínimo 90» y una medida es 90. ¿Qué conclusión corresponde?", "Dentro de límites, porque 90 cumple el mínimo", "Fuera de límites, porque no es mayor que 90", "No se puede concluir sin medir otra vez", "Un mínimo de 90 admite 90 o más."),
    ],
    ctx=("abc", "En una planilla de ejemplo de otra práctica ves que el límite de una pieza es «mínimo 60» y la medida anotada es 58, con la conclusión «dentro de límites». ¿Qué haces?", "Avisas al responsable del registro: la conclusión es incorrecta porque 58 está bajo el mínimo", "Lo dejas, porque el registro ya está firmado", "Cambias el 58 por 60 para que cuadre", "Un error de conclusión se informa; no se altera el dato."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué significa «fuera de límites»?", "Que la medida no cumple el límite de la tabla", "Fuera de límites es no cumplir el máximo o el mínimo."),
        ("¿Quién decide qué hacer con una pieza fuera de límites?", "Personal certificado, según el manual", "La decisión no es de quien tomó la medida."),
        ("Con un límite máximo de 50, ¿está dentro de límites una medida de 50?", "Sí, porque es igual al máximo", "El máximo incluye su propio valor."),
    ],
    op=("Tabla de ejemplo (centésimas de milímetro): holgura máxima 60; espesor mínimo 200. Medidas: cilindro A: 58; cilindro B: 61; pieza M: 205; pieza N: 198. Escribe (a) la conclusión «dentro» o «fuera» de cada medida con su razón, (b) el margen o el exceso de cada una, (c) qué escribes en el registro y a quién informas, sin decir cómo se repara.",
        "(a) A: dentro (58 ≤ 60); B: fuera (61 > 60); M: dentro (205 ≥ 200); N: fuera (198 < 200). (b) A: margen 2; B: exceso 1; M: margen 5; N: falta 2. (c) Pieza, medida, límite, conclusión, fecha y firma; informo a personal certificado, que decide según el manual.",
        ["aplica máximo y mínimo correctamente", "calcula margen o exceso", "escribe un registro completo", "informa sin proponer reparación"],
        ["hoja con las respuestas"],
        ["aplicar el máximo como mínimo", "calcular mal el exceso", "decidir la reparación"],
        "Pregunta: «¿es un máximo o un mínimo?». Si duda, pídele que relea cómo se aplica cada límite."),
    reinforce="Inventa una tabla con un límite máximo y uno mínimo y cuatro medidas; escribe la conclusión de cada una.",
    extend="Explica con un ejemplo por qué una medida igual al límite máximo sigue dentro de límites.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (comparación de opciones de ejemplo, inventada). Una unidad de ejemplo de un motor, fuera de límites, tiene dos alternativas que el manual permite y que decide personal certificado. "
     "Opción A, reparar: $360.000 y 600 h de vida restante después de la reparación. Opción B, reemplazar por una unidad nueva: $1.000.000 y 2.000 h de vida. Plazo de A: 3 días; plazo de B: 5 días. La aeronave de ejemplo cuesta $90.000 por día detenida.")
build(
    O1, 5, F,
    use="Aprenderé a comparar alternativas con datos, a calcular un costo por hora de vida y a verificar la calidad con una lista de comprobación y una revisión independiente.",
    prior=["Sé dividir números enteros.", "Sé comparar costos.", "Sé que las decisiones técnicas las toma personal certificado."],
    explain=[
        "Cuando el manual permite más de una opción, se comparan con datos. El costo por hora de vida es el costo total dividido entre las horas de vida que quedan. El costo por detención es el costo por día de la aeronave detenida por los días de plazo. El costo total de una opción suma su precio y el costo de la detención. Pero el costo no manda solo: manda lo que permite el manual y lo que decide el personal certificado.",
        "La verificación de calidad usa una lista de comprobación (cada ítem se marca como cumplido o no) y una revisión independiente: otra persona distinta de quien ejecutó el trabajo revisa los resultados y firma aparte. Si un ítem de la lista falta, el trabajo no se da por terminado.",
        f"Comparar en papel no habilita para elegir ni ejecutar una reparación o un reemplazo reales. {EMER} {AVISO}",
    ],
    vocab=[("costo por hora de vida", "costo total dividido entre las horas de vida restantes"), ("costo por detención", "costo diario de la aeronave detenida por los días de plazo"), ("lista de comprobación", "lista de ítems que se marcan como cumplidos o no"), ("revisión independiente", "revisión hecha por una persona distinta de quien ejecutó"), ("alternativa", "una de las opciones que el manual permite")],
    worked=[
        ("Costo por hora de vida", "Una opción de ejemplo cuesta $240.000 y deja 400 h de vida. ¿Cuánto es el costo por hora de vida?", ["Se divide el costo entre las horas de vida.", "240.000 dividido en 400 es 600."], "$600 por hora"),
        ("Costo por detención", "Una aeronave de ejemplo cuesta $50.000 por día detenida y una opción tarda 4 días. ¿Cuánto cuesta la detención?", ["Se multiplican los días por el costo diario.", "4 por 50.000 es 200.000."], "$200.000"),
    ],
    mistakes=[("Elegir la opción más barata sin mirar la vida restante.", "Una opción barata con poca vida puede salir cara por hora.", "Calcula el costo por hora de vida de cada opción."),
              ("Dar por terminado un trabajo con un ítem de la lista sin marcar.", "Un ítem sin marcar significa que no se comprobó.", "El trabajo no se cierra hasta completar y verificar todos los ítems.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es una revisión independiente?", "La revisión hecha por una persona distinta de quien ejecutó el trabajo", "La revisión que hace la misma persona dos veces", "La revisión que se hace sin lista ni registro", "Independiente significa que verifica alguien que no hizo el trabajo."),
        ("abc", "En Mantenimiento de Aeronaves: ¿cómo se calcula el costo por hora de vida?", "Costo total dividido entre las horas de vida restantes", "Horas de vida restantes dividido entre el costo total", "Costo total más las horas de vida restantes", "Mide cuánto cuesta cada hora de uso que se obtiene."),
        ("abc", "En Mantenimiento de Aeronaves: ¿quién decide entre reparar o reemplazar una unidad?", "Personal certificado, según lo que permite el manual", "Quien tenga la opción más barata", "La persona en práctica más experta del turno", "La decisión técnica es de personal certificado; el costo es solo un dato."),
        ("abc", "{F} ¿Qué opción tiene el menor costo por hora de vida?", "La opción B, reemplazar", "La opción A, reparar", "Las dos tienen el mismo costo por hora", "Se divide cada costo entre sus horas de vida y se comparan los resultados."),
        ("abc", "{F} Una persona dice: «A es la mejor, porque tiene el precio más bajo». ¿Qué observación es correcta?", "El precio no basta: A deja menos horas de vida y su costo por hora es mayor", "Tiene razón, porque el precio más bajo siempre gana", "Tiene razón, porque la vida restante no importa", "Se compara el costo por hora de vida y no solo el precio."),
        ("abc", "{F} ¿Qué opción tiene el mayor plazo?", "La opción B, con 5 días", "La opción A, con 3 días", "Las dos tienen el mismo plazo", "El plazo de B es mayor que el de A."),
        ("=", "{F} ¿Cuántos pesos por hora de vida cuesta la opción A?", "360000//600", "Se divide el costo entre las horas de vida restantes.", " pesos por hora"),
        ("=", "{F} ¿Cuántos pesos por hora de vida cuesta la opción B?", "1000000//2000", "Se divide el costo entre las horas de vida restantes.", " pesos por hora"),
        ("=", "{F} ¿Cuántos pesos cuesta la detención de la aeronave con la opción A?", "3*90000", "Se multiplican los días de plazo por el costo diario.", " pesos"),
        ("=", "{F} ¿Cuántos pesos suma el costo total de la opción B, con su precio y su detención?", "1000000+5*90000", "Se suma el precio al costo de los 5 días de detención.", " pesos"),
        ("abc", "{F} ¿Qué opción tiene el menor costo total, sumando precio y detención?", "La opción A", "La opción B", "Las dos suman lo mismo", "Se suma a cada precio el costo de sus días de detención y se comparan los totales."),
        ("abc", "Al cerrar un trabajo de ejemplo, la lista de comprobación tiene 12 ítems y uno quedó sin marcar. ¿Qué corresponde?", "No darlo por terminado hasta comprobar y marcar ese ítem", "Darlo por terminado porque 11 de 12 es suficiente", "Marcarlo sin comprobar para cerrar la lista", "Un ítem sin marcar es una verificación pendiente."),
        ("=", "En una lista de comprobación de ejemplo hay 20 ítems y se marcaron 15. ¿Qué porcentaje está completo?", "15*100//20", "Se divide lo marcado entre el total y se multiplica por 100.", " %"),
    ],
    ctx=("abc", "Un jefe de turno de ejemplo te propone: «marca tú los ítems de la lista que me faltan, así cerramos antes». ¿Qué respondes?", "Que no, porque cada ítem lo marca quien lo comprobó y otra persona revisa de forma independiente", "Que sí, porque cerrar antes es más importante", "Que sí, si son pocos ítems", "Marcar ítems no comprobados falsea el registro."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué es una lista de comprobación?", "Una lista de ítems que se marcan como cumplidos o no", "Permite verificar que no se omitió ningún paso del trabajo."),
        ("¿Quién hace una revisión independiente?", "Una persona distinta de quien ejecutó el trabajo", "Esa independencia permite detectar errores que el autor no ve."),
        ("¿Se cierra un trabajo con un ítem sin comprobar?", "No", "Un ítem sin comprobar deja el trabajo sin verificar."),
    ],
    op=("Ficha de ejemplo: unidad de otro motor con dos opciones permitidas. Opción 1: $450.000 y 900 h de vida, plazo de 2 días. Opción 2: $1.200.000 y 3.000 h de vida, plazo de 4 días. Costo por día detenida: $70.000. Escribe (a) el costo por hora de vida de cada opción, (b) el costo total de cada opción con la detención, (c) qué opción conviene por costo por hora y cuál por costo total, (d) quién decide y qué verificación se hace al cerrar. No digas cómo se hace el trabajo.",
        "(a) Opción 1: 450.000 / 900 = 500 por hora; opción 2: 1.200.000 / 3.000 = 400 por hora. (b) Opción 1: 450.000 + 2 × 70.000 = 590.000; opción 2: 1.200.000 + 4 × 70.000 = 1.480.000. (c) Por costo por hora conviene la 2; por costo total, la 1. (d) Decide personal certificado según el manual; al cerrar se usa una lista de comprobación y una revisión independiente.",
        ["calcula el costo por hora", "calcula el costo total", "distingue los dos criterios", "nombra quién decide y la verificación"],
        ["hoja con las cuatro respuestas"],
        ["usar solo el precio", "olvidar la detención", "decir que decide quien ejecuta"],
        "Pregunta: «¿qué criterio estás usando para comparar?». Si duda, pídele que relea las fórmulas de la explicación."),
    reinforce="Inventa dos opciones con precio, horas de vida y plazo, y calcula el costo por hora de vida de cada una.",
    extend="Explica por qué la opción más barata hoy no siempre es la que más conviene.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 6 (matriz de peligros de ejemplo, inventada). El «Hangar Demo de Sistemas» trabaja con aeronaves de ejemplo en un turno de 20 personas y 4 puestos. Su matriz anota: una línea con fluido a presión con una fuga visible, una batería conectada a un tablero, vapores de combustible en el ambiente, "
     "un panel abierto con cables a la vista, una aeronave con energía eléctrica externa conectada y ruido intenso.")
build(
    O2, 1, F,
    use="Aprenderé qué sistemas tiene una aeronave, qué peligros generales tiene trabajar con sistemas con energía y qué reglas generales los controlan.",
    prior=["Sé leer una matriz de peligros.", "Sé multiplicar enteros.", "Sé que los manuales fijan cómo se trabaja."],
    explain=[
        "Una aeronave está formada por sistemas, conjuntos de componentes que cumplen una función: el sistema de combustible, el hidráulico, el eléctrico, el de aire y presurización, el de tren de aterrizaje, los de instrumentos y comunicaciones, entre otros. El mantenimiento de los sistemas se hace según los diagramas y esquemas del manual del fabricante y las publicaciones técnicas, con respeto de las normas ambientales, de higiene, seguridad y de actuación humana.",
        "Los sistemas guardan energía aunque la aeronave esté parada: presión, tensión eléctrica o fluidos. Por eso un sistema puede ser peligroso aunque parezca apagado. Las organizaciones usan un permiso de trabajo y un sistema de bloqueo y etiquetado, que impide que alguien active un sistema que otra persona está trabajando, y solo lo manejan personas autorizadas. Los residuos y fluidos se manejan según las normas ambientales y la hoja de datos de seguridad.",
        f"Este cuaderno solo trabaja los conceptos. Tocar, abrir o probar sistemas reales exige instructor autorizado y norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("sistema de la aeronave", "conjunto de componentes que cumplen una función"), ("energía almacenada", "energía que un sistema conserva aunque esté detenido"), ("permiso de trabajo", "autorización escrita para realizar una tarea con riesgo"), ("bloqueo y etiquetado", "sistema que impide activar un equipo que se está trabajando"), ("hoja de datos de seguridad", "documento que informa los peligros de una sustancia"), ("residuo", "material que sobra de un trabajo y debe manejarse según norma")],
    worked=[
        ("Energía almacenada", "Una aeronave de ejemplo lleva horas detenida. ¿Puede conservar energía en sus sistemas?", ["Los sistemas pueden guardar presión o tensión.", "Parada no significa sin energía."], "Sí, puede conservar energía almacenada"),
        ("Sistema o componente", "En una aeronave de ejemplo, ¿«sistema de tren de aterrizaje» es un sistema o un componente?", ["Agrupa varios componentes con una función.", "Es un sistema."], "Es un sistema"),
    ],
    mistakes=[("Creer que un sistema detenido no tiene peligro.", "Puede guardar presión, tensión o fluidos.", "Trata todo sistema como si tuviera energía hasta que personal autorizado confirme lo contrario."),
              ("Pensar que el bloqueo y etiquetado lo puede quitar cualquier persona.", "Solo lo retira quien lo puso o quien la norma autorice.", "Respeta las etiquetas y avisa a un adulto responsable.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es un sistema de la aeronave?", "Un conjunto de componentes que cumplen una función", "Una pieza individual", "Un documento del hangar", "Un sistema agrupa componentes; una pieza individual es un componente."),
        ("abc", "En Mantenimiento de Aeronaves: ¿para qué sirve el bloqueo y etiquetado?", "Para impedir que alguien active un sistema que se está trabajando", "Para registrar las horas de vuelo de la aeronave", "Para pintar los componentes", "Evita una activación accidental mientras hay personas trabajando."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es la energía almacenada?", "La energía que un sistema conserva aunque esté detenido", "La energía que consume la aeronave al volar", "La batería de repuesto del hangar", "Un sistema detenido puede conservar presión o tensión."),
        ("abc", "{F} ¿Qué peligro de la matriz está relacionado con una fuga en un sistema que guarda energía?", "La línea con fluido a presión con una fuga visible", "El ruido intenso", "El panel abierto con cables a la vista", "Un fluido a presión guarda energía y la fuga puede liberarla."),
        ("abc", "{F} ¿Qué medida pertenece a los controles administrativos?", "Un permiso de trabajo y bloqueo y etiquetado, manejados por personas autorizadas", "Cambiar un equipo por otro que no use presión", "Usar protección auditiva y guantes", "Un permiso y un bloqueo son reglas y procedimientos de la organización."),
        ("abc", "{F} ¿Con qué documento se informa el peligro de los vapores de combustible del ambiente?", "Con la hoja de datos de seguridad de la sustancia", "Con la orden de trabajo del vuelo anterior", "Con el registro de horas del motor", "La hoja de datos de seguridad describe los peligros de una sustancia."),
        ("=", "{F} Se asigna 1 persona a cargo de seguridad por cada 5 personas del turno. ¿Cuántas personas se necesitan?", "20//5", "Se divide la dotación entre las personas que cubre cada responsable.", " personas"),
        ("=", "{F} Cada uno de los 4 puestos debe tener 3 etiquetas de bloqueo y el hangar guarda 6 más de repuesto. ¿Cuántas etiquetas necesita?", "4*3+6", "Se multiplican los puestos por las etiquetas de cada uno y se suma el repuesto.", " etiquetas"),
        ("=", "Un peligro de ejemplo tiene probabilidad 5 y gravedad 3. Con un control la probabilidad baja a 2. ¿Cuántos puntos baja el puntaje (probabilidad por gravedad)?", "5*3-2*3", "Se calcula el puntaje antes y después, y se restan.", " puntos"),
        ("abc", "{F} Un aprendiz dice: «la aeronave tiene conectada la energía externa, pero como está parada puedo tocar los cables del panel abierto». ¿Qué respuesta es correcta?", "Es falso: puede haber energía, y solo personal autorizado interviene", "Es cierto, si no hay nadie más cerca", "Es cierto, porque una aeronave parada no tiene energía", "Parada no significa sin energía; tocar cables lo decide personal autorizado."),
        ("abc", "En una visita a un hangar de ejemplo, ves una chispa y una fuga cerca de un tablero. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte para cerrar la fuga con las manos", "Tocar el tablero para desconectarlo", "Acercarse a una fuga con chispas puede causar un accidente mayor."),
        ("=", "{F} El peligro de los vapores de combustible tiene probabilidad 2 y gravedad 5; el de la batería conectada tiene probabilidad 3 y gravedad 4. ¿Cuántos puntos más de puntaje (probabilidad por gravedad) tiene el segundo?", "3*4-2*5", "Se calculan los dos puntajes y se restan.", " puntos"),
        ("abc", "{F} Un compañero dice: «el riesgo de la fuga es bajo porque gotea poco». ¿Qué observación es correcta?", "El riesgo depende de la energía y de la gravedad posible, no solo de cuánto gotea", "Tiene razón, porque lo pequeño no preocupa", "Tiene razón, porque un goteo siempre es inofensivo", "Un goteo pequeño en un sistema con energía puede escalar a un accidente grave."),
    ],
    ctx=("abc", "Una persona de un hangar de ejemplo te dice: «ayúdame a abrir ese panel y toca los cables, que yo te guío». ¿Qué respondes?", "Que no, porque tocar sistemas con energía exige instructor autorizado y norma vigente, y que avisarás a un adulto responsable", "Que sí, si ella te guía paso a paso", "Que sí, pero con guantes", "Un guía informal no reemplaza la autorización ni el permiso de trabajo."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué puede conservar un sistema detenido?", "Energía almacenada", "Un sistema detenido puede conservar presión o tensión."),
        ("¿Qué documento informa los peligros de una sustancia?", "La hoja de datos de seguridad", "Describe los peligros y el manejo de una sustancia."),
        ("¿Quién interviene los sistemas de una aeronave?", "Personal autorizado y capacitado", "Esta tarea no es para quien no tiene autorización."),
    ],
    op=("Un hangar de ejemplo anota dos situaciones: (1) un sistema de aire de ejemplo con presión en sus líneas, detenido y con un cartel de bloqueo; (2) un charco de un fluido de ejemplo cerca de un tablero eléctrico. Escribe (a) el peligro y el riesgo de cada situación, (b) un control administrativo para una de ellas, (c) qué hace una persona de práctica ante la situación 2, (d) por qué el EPP no basta. No describas cómo se interviene.",
        "(a) 1: peligro, la presión guardada; riesgo, que se libere de golpe y cause daño. 2: peligro, el fluido cerca de un tablero; riesgo, incendio o descarga. (b) Un permiso de trabajo y un bloqueo con etiqueta. (c) No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias. (d) El EPP es la última barrera y no quita el peligro.",
        ["distingue peligro y riesgo", "propone un control administrativo", "responde con conducta de emergencia", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["decir que lo arregla por su cuenta", "proponer solo el EPP", "describir cómo se interviene"],
        "Pregunta: «¿quién puede actuar y qué debo hacer yo?». Si duda, pídele que relea la conducta de emergencia."),
    reinforce="Escribe cuatro sistemas de una aeronave y una función de cada uno, usando solo lo que aprendiste.",
    extend="Explica con un ejemplo por qué «detenido» no significa «sin energía».",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 7 (esquema de bloques de ejemplo, inventado). Sistema de fluido de ejemplo: [Depósito D] → [Bomba B] → [Filtro F] → [Válvula V] → [Actuador A] → regreso al [Depósito D]. "
     "Leyenda: D depósito, B bomba, F filtro, V válvula, A actuador. Una flecha indica el sentido del flujo. El esquema trae 5 bloques y 5 flechas.")
build(
    O2, 2, F,
    use="Aprenderé a leer esquemas y diagramas de un sistema: bloques, flechas, leyenda y símbolos, y qué documentos y roles usa el mantenimiento de sistemas.",
    prior=["Sé seguir una secuencia con flechas.", "Sé contar elementos de un dibujo.", "Sé que un manual trae documentos con instrucciones."],
    explain=[
        "Un esquema de bloques muestra un sistema con cuadros que representan componentes y flechas que indican el sentido del flujo. Un diagrama funcional explica cómo trabaja un sistema; un diagrama de ubicación muestra dónde está cada componente en la aeronave; un diagrama eléctrico o de cableado muestra cómo se conectan los componentes con cables. Toda figura trae una leyenda, que explica el significado de los símbolos y las siglas.",
        "En un sistema de fluido, el depósito guarda el fluido, la bomba lo impulsa, el filtro lo limpia, la válvula lo deja pasar o lo detiene y el actuador usa el fluido para producir un movimiento. Leer un esquema es seguir las flechas desde una fuente hasta un destino. Aguas arriba son los componentes que están antes de uno dado; aguas abajo, los que están después. Un componente puede tener un código de referencia, una identificación única que se usa en el manual y en los registros para no confundir piezas parecidas. Los esquemas del manual pueden cambiar con las revisiones: se usa siempre la versión vigente.",
        f"El técnico lee e informa, el inspector verifica y el personal certificado libera a servicio. {EMER} {AVISO}",
    ],
    vocab=[("esquema de bloques", "dibujo con cuadros y flechas que muestra un sistema"), ("leyenda", "lista que explica los símbolos y siglas de una figura"), ("aguas arriba", "componentes que están antes de uno dado en el flujo"), ("aguas abajo", "componentes que están después de uno dado en el flujo"), ("código de referencia", "identificación única de un componente en el manual"), ("diagrama eléctrico", "diagrama que muestra cómo se conectan los componentes con cables")],
    worked=[
        ("Aguas arriba y abajo", "En un esquema de ejemplo el flujo va de P a Q y luego a R. ¿Qué componente está aguas abajo de Q?", ["Aguas abajo es lo que viene después en el flujo.", "Después de Q viene R."], "R"),
        ("Contar flechas", "Un esquema de ejemplo en línea tiene 4 bloques conectados uno tras otro, sin regreso. ¿Cuántas flechas tiene?", ["Entre 4 bloques en línea hay 3 uniones.", "Cada unión es una flecha."], "3 flechas"),
    ],
    mistakes=[("Leer un esquema sin mirar la leyenda.", "Los símbolos y siglas cambian de un manual a otro.", "Primero lee la leyenda y luego sigue las flechas."),
              ("Usar un esquema de una revisión antigua del manual.", "Puede estar desactualizado.", "Usa siempre la versión vigente indicada en el manual.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué muestra un esquema de bloques?", "Los componentes de un sistema y el sentido del flujo entre ellos", "El precio de cada componente", "El nombre de las personas que hacen el trabajo", "Cuadros y flechas representan componentes y el sentido del flujo."),
        ("abc", "En Mantenimiento de Aeronaves: ¿para qué sirve la leyenda de un diagrama?", "Para explicar el significado de los símbolos y las siglas", "Para fijar los intervalos de mantenimiento", "Para firmar el diagrama", "Sin la leyenda un símbolo puede interpretarse mal."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es el código de referencia de un componente?", "Una identificación única usada en el manual y en los registros", "Una frase que describe cómo funciona el componente", "El precio del componente", "El código evita confundir piezas parecidas."),
        ("abc", "{F} ¿Qué componente está justo después de la bomba B en el esquema?", "El filtro F", "El actuador A", "El depósito D", "Las flechas van B → F; el actuador está más adelante."),
        ("abc", "{F} ¿Cuántos componentes están aguas abajo de la válvula V antes del regreso al depósito?", "Uno, el actuador A", "Dos, el actuador A y el filtro F", "Ninguno, porque V es el último bloque", "Tras V solo sigue A antes de volver al depósito D."),
        ("abc", "{F} ¿Qué símbolo de la leyenda representa a la bomba?", "B", "F", "V", "La leyenda dice que B es la bomba; F es el filtro y V la válvula."),
        ("=", "{F} Cada flecha del esquema se rotula con 2 etiquetas de ejemplo. ¿Cuántas etiquetas se necesitan?", "5*2", "Cada una de las flechas lleva una etiqueta.", " etiquetas"),
        ("=", "{F} Un taller de ejemplo revisa en planilla 3 veces cada bloque. ¿Cuántas revisiones hace?", "5*3", "Se multiplican los bloques por las revisiones de cada uno.", " revisiones"),
        ("=", "Un esquema de ejemplo en línea tiene 7 bloques conectados uno tras otro, sin regreso. ¿Cuántas flechas tiene?", "7-1", "Entre n bloques en línea hay n menos 1 uniones.", " flechas"),
        ("abc", "{F} Una persona dice: «el filtro F está aguas arriba de la bomba B». ¿Qué observación es correcta?", "Es falsa: F está después de B, aguas abajo", "Es cierta, porque F va escrito más abajo en la leyenda", "Es cierta, porque los filtros siempre van antes de las bombas", "El orden lo da el sentido de las flechas, no el orden de la leyenda."),
        ("abc", "Una persona en práctica encuentra dos esquemas del mismo sistema con distinta fecha de revisión. ¿Cuál usa?", "El de la versión vigente según el manual", "El que esté más a mano", "El más antiguo, porque ya se probó", "Un esquema desactualizado puede ser incorrecto; se usa la versión vigente."),
        ("=", "{F} Un registro de ejemplo guarda 4 datos por cada bloque. ¿Cuántos datos guarda en total?", "5*4", "Se multiplican los bloques por los datos de cada uno.", " datos"),
        ("abc", "{F} Una persona dice: «el esquema no tiene regreso, porque el flujo termina en el actuador A». ¿Qué observación es correcta?", "Es falsa: hay una flecha de regreso desde A hasta el depósito D", "Es cierta, porque A es el último bloque de la leyenda", "Es cierta, porque todos los esquemas terminan en un actuador", "La ficha indica un regreso al depósito D, así que el flujo vuelve a su inicio."),
    ],
    ctx=("abc", "En un taller de ejemplo, una persona te pide seguir un esquema «de memoria» para ahorrar tiempo. ¿Qué respondes?", "Que no, porque el trabajo se hace con el esquema vigente del manual a la vista", "Que sí, porque la memoria basta", "Que sí, si lo recuerda un compañero", "Los esquemas cambian; el manual vigente es la fuente."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué indica una flecha de un esquema de bloques?", "El sentido del flujo", "La flecha muestra por dónde avanza el flujo."),
        ("¿Qué significa «aguas abajo»?", "Los componentes que están después de uno dado en el flujo", "Se refiere al sentido en que avanza el flujo."),
        ("¿Qué versión de un esquema se usa?", "La vigente según el manual", "Las versiones antiguas pueden estar desactualizadas."),
    ],
    op=("Esquema de ejemplo: [Fuente S] → [Regulador R] → [Válvula W] → [Equipo E] → [Salida X]. Leyenda: S fuente, R regulador, W válvula, E equipo, X salida. Escribe (a) cuántos bloques y cuántas flechas hay, (b) qué componentes están aguas arriba de E, (c) qué componente está aguas abajo de R, (d) qué haces si tu esquema no trae leyenda.",
        "(a) 5 bloques y 4 flechas. (b) S, R y W. (c) W, E y X están aguas abajo de R. (d) Pido el documento completo con leyenda, porque sin ella no interpreto los símbolos; informo a un adulto responsable.",
        ["cuenta bloques y flechas", "identifica aguas arriba", "identifica aguas abajo", "explica por qué necesita la leyenda"],
        ["hoja con las cuatro respuestas"],
        ["contar mal las flechas", "invertir arriba y abajo", "interpretar símbolos sin leyenda"],
        "Pregunta: «¿hacia dónde apunta la flecha?». Si duda, pídele que relea aguas arriba y aguas abajo."),
    reinforce="Dibuja un esquema inventado de 4 bloques con leyenda y escribe qué está aguas arriba y qué aguas abajo del segundo bloque.",
    extend="Explica por qué una leyenda es indispensable para leer un diagrama.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 8 (caso de ejemplo, inventado). Esquema de un sistema de aire de ejemplo: [Fuente F] → [Regulador R] → [Válvula V1] → [Rama 1: Equipo E1] y también [Válvula V1] → [Válvula V2] → [Rama 2: Equipo E2]. "
     "Registro del vuelo de ejemplo: «el equipo E1 funcionó con normalidad; el equipo E2 no recibió flujo». No hay diagnóstico confirmado.")
build(
    O2, 3, F,
    use="Aprenderé a analizar en papel un caso: seguir un esquema, ordenar candidatos a causa y escribir un informe de hallazgos sin afirmar lo que no se comprobó.",
    prior=["Sé leer un esquema de bloques.", "Sé distinguir síntoma y causa.", "Sé que solo se informa lo comprobado."],
    explain=[
        "Un caso de mantenimiento parte de un síntoma, como «el equipo E2 no recibió flujo». Con el esquema se hace una lista de componentes candidatos a causa: los que están aguas arriba del equipo afectado, porque lo que falla antes puede dejar sin flujo a lo que viene después. Un candidato no es una causa confirmada: la causa se establece con inspección y pruebas autorizadas, según el manual.",
        "Si un equipo funciona bien, los componentes que están aguas arriba de él quedan menos sospechosos, porque ese flujo sí llegó. Es una pista, no una prueba. El informe de hallazgos escribe: el síntoma, los candidatos con su razón, lo que no se sabe y a quién se informa. Nunca escribe «la causa es» sin una comprobación hecha por personal autorizado.",
        f"Este análisis es solo en papel. {EMER} {AVISO}",
    ],
    vocab=[("candidato a causa", "componente que podría explicar un síntoma y aún no está confirmado"), ("causa confirmada", "causa establecida con inspección y pruebas autorizadas"), ("pista", "dato que orienta, pero no prueba"), ("informe de hallazgos", "documento que describe síntoma, candidatos y lo que no se sabe"), ("rama", "camino del esquema que sale de un punto y va a un equipo")],
    worked=[
        ("Candidatos", "En un esquema de ejemplo, [P] → [Q] → [R] → [Equipo T]. El equipo T no recibe flujo. ¿Qué componentes son candidatos?", ["Los candidatos están aguas arriba de T.", "P, Q y R."], "P, Q y R"),
        ("Pista", "En otro esquema de ejemplo, el equipo U funciona y está después de [M] y [N]. ¿Qué dice esto de M y N?", ["Si U funciona, el flujo pasó por M y N.", "Son menos sospechosos, pero no se descartan del todo."], "Son menos sospechosos como causa del síntoma de otro equipo después de ellos"),
    ],
    mistakes=[("Escribir «la causa es la válvula V2» sin comprobación.", "Un candidato no es una causa confirmada.", "Escribe «V2 es un candidato»; la causa la confirma personal autorizado."),
              ("Descartar un componente solo porque otro equipo funciona.", "Es una pista, no una prueba.", "Registra la pista y deja la decisión al personal certificado.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es un candidato a causa?", "Un componente que podría explicar el síntoma y aún no está confirmado", "La pieza que ya se comprobó que falla", "El equipo que funciona bien", "Candidato significa posible; la confirmación llega después."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué contiene un informe de hallazgos?", "Síntoma, candidatos con su razón, lo que no se sabe y a quién se informa", "Solo el nombre de la pieza que parece fallar", "Solo la fecha del vuelo", "Un informe completo diferencia lo comprobado de lo supuesto."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué componentes son candidatos cuando un equipo no recibe flujo?", "Los que están aguas arriba de ese equipo", "Los que están aguas abajo del equipo", "Todos los equipos que sí funcionan", "Lo que falla antes puede dejar sin flujo a lo que viene después."),
        ("abc", "{F} ¿Cuál es el síntoma del caso?", "El equipo E2 no recibió flujo", "La válvula V2 está dañada", "El regulador R no funciona", "El síntoma es lo observado; las otras opciones nombran una causa sin comprobar."),
        ("abc", "{F} ¿Qué componente es candidato para el síntoma de E2 y NO lo es para el de E1?", "La válvula V2", "La fuente F", "El regulador R", "V2 está solo en el camino de E2; F, R y V1 están antes de ambos equipos."),
        ("abc", "{F} E1 funcionó. ¿Qué se puede decir de F, R y V1?", "Son menos sospechosos, porque el flujo pasó por ellos, pero no están descartados del todo", "Están confirmados como causa", "Están descartados para siempre", "Que E1 funcione es una pista, no una prueba definitiva."),
        ("=", "{F} Revisar cada componente candidato en la planilla toma 2 horas de ejemplo. Para E2 los candidatos son F, R, V1 y V2. ¿Cuántas horas suma la revisión?", "4*2", "Se multiplican los candidatos por las horas de cada revisión.", " horas"),
        ("=", "{F} El esquema tiene 6 componentes entre fuente, regulador, válvulas y equipos. Si 4 están aguas arriba de E2, ¿cuántos no están aguas arriba de E2?", "6-4", "Se resta al total la cantidad de componentes aguas arriba.", " componentes"),
        ("=", "{F} Cada candidato exige 3 anotaciones en el informe y hay 4 candidatos para E2. ¿Cuántas anotaciones hay en total?", "4*3", "Se multiplican los candidatos por las anotaciones de cada uno.", " anotaciones"),
        ("abc", "{F} Un compañero dice: «la causa es V2, porque está en la rama 2». ¿Qué observación es correcta?", "V2 es un candidato, no una causa confirmada, y lo confirma personal autorizado", "Es correcta, porque estar en la rama basta", "Es correcta, porque V2 es la única pieza de la rama", "Un candidato no es una causa confirmada."),
        ("abc", "{F} Un aprendiz propone abrir y probar V2 para «ver si es esa». ¿Qué corresponde?", "No hacerlo: informar el síntoma y los candidatos al personal certificado", "Hacerlo, si trae guantes", "Hacerlo, porque el esquema lo permite", "Analizar el esquema no autoriza a intervenir sistemas."),
        ("=", "{F} Si el informe describe 5 hallazgos y cada uno ocupa 2 líneas, ¿cuántas líneas ocupa en total?", "5*2", "Se multiplican los hallazgos por las líneas de cada uno.", " líneas"),
        ("abc", "{F} ¿Qué frase es correcta en un informe de hallazgos?", "«E2 no recibió flujo; son candidatos V1, V2, R y F; no se ha confirmado la causa»", "«La causa del problema es V2 y hay que cambiarla»", "«E2 está malo»", "El informe nombra síntoma y candidatos sin afirmar una causa no comprobada."),
    ],
    ctx=("abc", "Una compañera de práctica dice con seguridad «seguro es la bomba» sin haber visto datos. ¿Qué haces?", "Le pides los datos y propones registrar «bomba» como candidato, no como causa", "La crees y escribes «causa: bomba» en el registro", "Cambias la bomba tú en el hangar", "La seguridad no reemplaza la evidencia."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿un candidato a causa es lo mismo que una causa confirmada?", "No", "El candidato aún no está comprobado."),
        ("¿Qué componentes se revisan primero como candidatos para un equipo sin flujo?", "Los que están aguas arriba", "Lo que falla antes afecta a lo que viene después."),
        ("¿Cómo se llama el dato que orienta pero no prueba?", "Una pista", "Una pista no es una prueba."),
    ],
    op=("Caso de ejemplo: esquema [Fuente S] → [Regulador R] → [Válvula W1] y luego [W1] → [Equipo P] y [W1] → [Válvula W2] → [Equipo Q]. Síntoma: P funcionó; Q no recibió flujo. Escribe (a) el síntoma, (b) los candidatos para Q con la razón, (c) cuál es candidato solo para Q, (d) una frase de informe que no afirme una causa y a quién se informa.",
        "(a) Q no recibió flujo. (b) S, R, W1 y W2, porque están aguas arriba de Q. (c) W2, porque está solo en el camino de Q. (d) «Q no recibió flujo; son candidatos S, R, W1 y W2; no se ha confirmado la causa»; se informa al personal certificado.",
        ["identifica el síntoma", "lista candidatos con razón", "distingue el candidato exclusivo", "no afirma una causa e informa"],
        ["hoja con las cuatro respuestas"],
        ["afirmar una causa", "incluir a P como candidato", "proponer intervenir"],
        "Pregunta: «¿qué está aguas arriba de Q?». Si duda, pídele que relea los candidatos."),
    reinforce="Inventa un esquema de 5 componentes con un equipo sin flujo y escribe los candidatos y la frase de informe.",
    extend="Explica por qué un candidato no debe escribirse como causa en un registro.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 9 (programa de mantenimiento de ejemplo, inventado). Aeronave de ejemplo «XX-DEM». Tarea T1: intervalo 500 horas de vuelo (HV); desde su última ejecución van 520 HV. Tarea T2: intervalo 400 ciclos; van 380 ciclos. Tarea T3: intervalo 12 meses; van 13 meses. "
     "Tarea T4: intervalo «300 HV o 9 meses, lo que ocurra primero»; van 90 HV y 8 meses. Un ciclo de ejemplo es un despegue con su aterrizaje.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar un criterio de programa de mantenimiento a datos de ejemplo: intervalos por horas, ciclos y meses, y a decidir qué tarea está vencida o por vencer.",
    prior=["Sé restar y comparar enteros.", "Sé leer una tabla de intervalos.", "Sé que las tareas se repiten según el manual."],
    explain=[
        "El programa de mantenimiento de una aeronave lista tareas con su intervalo, que puede darse en horas de vuelo (HV), en ciclos o en tiempo calendario. Una tarea vence cuando lo transcurrido desde su última ejecución alcanza o supera el intervalo. Cuando el intervalo dice «lo que ocurra primero», se revisan todas las unidades: basta con que una se cumpla para que la tarea venza.",
        "Los márgenes se calculan con el intervalo menos lo transcurrido. Si un margen es positivo, falta ese valor para vencer; si es cero, vence ahora; si es negativo, la tarea está vencida y la aeronave no se libera a servicio sin la decisión del personal certificado según la norma vigente. Los intervalos de este cuaderno son números de ejemplo; los reales los fija el fabricante y la autoridad aeronáutica.",
        f"Calcular en papel no autoriza a decidir si una aeronave vuela o no. {EMER} {AVISO}",
    ],
    vocab=[("programa de mantenimiento", "lista de tareas con sus intervalos para una aeronave"), ("hora de vuelo (HV)", "hora que la aeronave pasa en vuelo, medida para el mantenimiento"), ("ciclo", "un despegue con su aterrizaje, en estos ejemplos"), ("intervalo", "cada cuánto se repite una tarea"), ("vencida", "tarea cuyo intervalo se alcanzó o se superó"), ("lo que ocurra primero", "criterio que obliga a revisar todas las unidades del intervalo")],
    worked=[
        ("Margen en horas", "Una tarea de ejemplo tiene intervalo de 250 HV y van 200 HV. ¿Cuántas HV faltan?", ["Se resta lo transcurrido al intervalo.", "250 menos 200 son 50."], "50 HV"),
        ("Dos unidades", "Una tarea de ejemplo vence a las 100 HV o a los 6 meses, lo que ocurra primero. Van 40 HV y 6 meses. ¿Está vencida?", ["Con meses ya se llegó al intervalo de 6.", "Basta una unidad para vencer."], "Sí, por los 6 meses"),
    ],
    mistakes=[("Sumar horas y meses como si fueran la misma unidad.", "Cada unidad se compara solo con su propio intervalo.", "Compara HV con HV, ciclos con ciclos y meses con meses."),
              ("Ignorar el «lo que ocurra primero».", "Basta que una unidad se cumpla.", "Revisa todas las unidades del intervalo.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿cuándo vence una tarea con intervalo de 500 HV?", "Cuando lo transcurrido desde su última ejecución alcanza o supera 500 HV", "Cuando la aeronave cumple 500 HV en total desde que se fabricó", "Cuando pasan 500 días", "El intervalo se cuenta desde la última ejecución de esa tarea."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué significa «lo que ocurra primero» en un intervalo?", "Que basta con que se cumpla una de las unidades para que la tarea venza", "Que deben cumplirse todas las unidades a la vez", "Que solo cuentan los meses", "Se revisa cada unidad y vence con la primera que llegue."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es un ciclo en estos ejemplos?", "Un despegue con su aterrizaje", "Una hora de vuelo", "Un mes de calendario", "El ciclo cuenta despegues y aterrizajes, no tiempo."),
        ("abc", "{F} ¿Cuál tarea está vencida por horas de vuelo?", "T1, porque van 520 HV con intervalo de 500", "T2, porque van 380 ciclos", "T4, porque van 90 HV", "Solo T1 supera su intervalo en horas de vuelo."),
        ("abc", "{F} ¿Cuál tarea está vencida por tiempo calendario?", "T3, porque van 13 meses con intervalo de 12", "T4, porque van 8 meses con 9 de intervalo", "T2, porque van 380 ciclos", "T3 superó sus 12 meses; T4 aún no llega a 9."),
        ("abc", "{F} ¿Está vencida la tarea T4?", "No, porque ni sus HV ni sus meses alcanzaron el intervalo", "Sí, porque van 8 meses", "Sí, porque van 90 HV", "Con 90 de 300 HV y 8 de 9 meses, ninguna unidad se cumplió."),
        ("=", "{F} ¿Cuántas HV pasó T1 de su intervalo?", "520-500", "Se resta el intervalo a lo transcurrido.", " HV"),
        ("=", "{F} ¿Cuántos ciclos faltan para que venza T2?", "400-380", "Se resta lo transcurrido al intervalo.", " ciclos"),
        ("=", "{F} ¿Cuántos meses faltan para que venza T4 por tiempo calendario?", "9-8", "Se resta lo transcurrido al intervalo en meses.", " meses"),
        ("=", "{F} ¿Cuántas HV faltan para que venza T4 por horas?", "300-90", "Se resta lo transcurrido al intervalo en HV.", " HV"),
        ("abc", "{F} Una persona dice: «T2 ya venció porque van 380 ciclos y es casi 400». ¿Qué observación es correcta?", "Aún no venció: faltan 20 ciclos y solo vence al alcanzar el intervalo", "Tiene razón, porque casi 400 equivale a 400", "Tiene razón, porque los ciclos cuentan doble", "Una tarea vence al alcanzar o superar el intervalo, no antes."),
        ("abc", "{F} Una aeronave tiene T1 y T3 vencidas. Un técnico dice: «la libero yo, total son solo dos tareas». ¿Qué corresponde?", "No: la liberación a servicio es de personal certificado según la norma vigente", "Sí, porque son pocas tareas", "Sí, si T1 se ejecuta mañana", "Con tareas vencidas decide personal certificado; el técnico no libera."),
        ("=", "Una tarea de ejemplo tiene intervalo de 150 HV y van 128 HV. La aeronave vuela 25 HV más sin ejecutar la tarea. ¿Cuántas HV pasó del intervalo?", "128+25-150", "Se suma el uso a lo transcurrido y se resta el intervalo.", " HV"),
    ],
    ctx=("abc", "Una tarea de ejemplo vence a las 200 HV o a los 4 meses, lo que ocurra primero, y la persona a cargo dice «no importa el calendario, solo las HV». ¿Qué haces?", "Le recuerdas que basta con que una unidad se cumpla y revisas también los meses", "Le das la razón, porque las HV son más importantes", "Ignoras los meses, para ir más rápido", "El criterio «lo que ocurra primero» exige revisar ambas unidades."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué pasa con una tarea cuando lo transcurrido iguala al intervalo?", "Vence", "La tarea vence al alcanzar el intervalo, no después."),
        ("¿Se pueden sumar horas de vuelo y meses?", "No, cada unidad se compara con su propio intervalo", "Son unidades distintas y cada una tiene su propio intervalo."),
        ("¿Quién libera a servicio una aeronave con tareas vencidas?", "Solo personal certificado según la norma vigente", "El técnico no tiene esa facultad."),
    ],
    op=("Programa de ejemplo: tarea A: intervalo 300 HV, van 310 HV. Tarea B: intervalo 250 ciclos, van 240. Tarea C: «150 HV o 6 meses, lo que ocurra primero», van 160 HV y 4 meses. Escribe (a) qué tareas están vencidas y por qué, (b) cuánto falta a la que no está vencida, (c) quién decide sobre la aeronave con tareas vencidas, (d) un error común al leer «lo que ocurra primero».",
        "(a) A está vencida: 310 es mayor que 300; C está vencida por horas de vuelo (160 es mayor que 150), aunque sus meses (4 de 6) aún no se cumplan. (b) A B le faltan 250 - 240 = 10 ciclos. (c) El personal certificado, según la norma vigente. (d) Revisar solo una unidad e ignorar la otra.",
        ["identifica las tareas vencidas", "calcula lo que falta", "nombra quién decide", "explica el criterio de dos unidades"],
        ["hoja con las cuatro respuestas"],
        ["sumar horas y meses", "decidir como técnico", "ignorar las HV de C porque los meses no se cumplen"],
        "Pregunta: «¿cuál unidad llegó primero?». Si duda, pídele que relea cómo vence una tarea con dos unidades."),
    reinforce="Inventa tres tareas con intervalos en HV, ciclos y meses y escribe cuál está vencida y cuánto falta a las demás.",
    extend="Explica por qué se necesita más de una unidad en algunos intervalos.",
)

# ============================================================ OAE-02, clase 5
F = ("Ficha 10 (dos órdenes de trabajo cerradas de ejemplo, inventadas). Orden OT-C-10: 20 ítems de verificación, 18 marcados; tiene fecha y firma del técnico, pero la firma de la revisión independiente está vacía. "
     "Orden OT-C-11: 20 ítems, 20 marcados; fecha y firma del técnico, firma de la revisión independiente de otra persona, referencia al manual con la revisión vigente. Costo de revisión por ítem de ejemplo: $2.000.")
build(
    O2, 5, F,
    use="Aprenderé a comparar dos registros de trabajo cerrados, a detectar lo que falta y a ver cómo se informa un pendiente sin decidir por cuenta propia.",
    prior=["Sé calcular porcentajes sencillos.", "Sé que un registro lleva fecha y firma.", "Sé que la revisión independiente la hace otra persona."],
    explain=[
        "Cerrar una orden de trabajo exige que todos los ítems estén comprobados, que lleve fecha y firma de quien ejecutó, la firma de una revisión independiente y la referencia a la versión vigente del manual. Si falta alguno, la orden queda con pendientes. Un pendiente es un ítem no cumplido o no verificado. Se informa por escrito, con su motivo y su responsable.",
        "Un defecto que no se puede resolver en el momento puede diferirse, es decir, postergarse con autorización. La decisión de diferir la toma personal certificado según la norma vigente y se registra con sus condiciones y su plazo; el técnico no la toma por su cuenta. Comparar dos órdenes permite ver cuál está completa y qué le falta a la otra: el porcentaje completo se calcula como ítems marcados por 100 dividido entre el total.",
        f"La honestidad del registro es parte de la seguridad: un registro falso puede esconder un defecto. {EMER} {AVISO}",
    ],
    vocab=[("orden cerrada", "orden con todos sus ítems comprobados y las firmas requeridas"), ("pendiente", "ítem no cumplido o no verificado"), ("diferir", "postergar un defecto con autorización de personal certificado"), ("revisión independiente", "verificación hecha por una persona distinta de quien ejecutó"), ("trazabilidad", "posibilidad de reconstruir qué se hizo, quién y cuándo")],
    worked=[
        ("Ítems completos", "Una orden de ejemplo tiene 10 ítems y 7 marcados. ¿Cuántos son pendientes?", ["Los pendientes son los no marcados.", "10 menos 7 son 3."], "3 pendientes"),
        ("Quién difiere", "Un técnico de ejemplo encuentra un defecto que no puede resolver en el turno. ¿Quién decide diferirlo?", ["Diferir es una decisión con autorización.", "La toma personal certificado según la norma vigente."], "Personal certificado"),
    ],
    mistakes=[("Marcar un ítem pendiente como cumplido para cerrar la orden.", "Un registro falso puede esconder un defecto.", "Deja el ítem como pendiente e infórmalo con su motivo."),
              ("Diferir un defecto por decisión propia.", "Diferir exige autorización de personal certificado.", "Informa el defecto y espera la decisión autorizada.")],
    T=[
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es un pendiente en una orden de trabajo?", "Un ítem no cumplido o no verificado", "Un ítem que ya tiene firma", "El costo total de la orden", "Un pendiente es lo que falta para cerrar la orden."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué significa diferir un defecto?", "Postergarlo con autorización de personal certificado", "Borrarlo del registro", "Ignorarlo hasta que falle", "Diferir es una postergación autorizada y registrada con plazo."),
        ("abc", "En Mantenimiento de Aeronaves: ¿qué es la trazabilidad de un registro?", "Poder reconstruir qué se hizo, quién y cuándo", "Poder borrar un dato sin dejar rastro", "Que el registro sea breve", "Con trazabilidad se puede verificar el trabajo después."),
        ("abc", "{F} ¿Qué orden está completa?", "La OT-C-11, con todos sus ítems y firmas", "La OT-C-10, porque tiene firma del técnico", "Las dos, porque ambas tienen fecha", "La OT-C-10 carece de revisión independiente y tiene 2 ítems sin marcar."),
        ("abc", "{F} ¿Qué le falta a la OT-C-10 además de dos ítems?", "La firma de la revisión independiente", "La fecha", "La firma del técnico", "La ficha dice que esa firma está vacía."),
        ("abc", "{F} ¿Qué dato de la OT-C-11 da más seguridad de usar el manual correcto?", "La referencia a la revisión vigente del manual", "La fecha del trabajo", "El costo por ítem", "La referencia a la versión vigente permite comprobar contra qué se trabajó."),
        ("=", "{F} ¿Cuántos ítems pendientes tiene la OT-C-10?", "20-18", "Se resta lo marcado al total de ítems.", " ítems"),
        ("=", "{F} ¿Qué porcentaje de ítems tiene marcado la OT-C-10?", "18*100//20", "Se divide lo marcado entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos pesos cuesta la revisión de los 20 ítems de la OT-C-11?", "20*2000", "Se multiplican los ítems por el costo de revisión de cada uno.", " pesos"),
        ("abc", "{F} Una persona dice: «a la OT-C-10 le marco los 2 ítems que faltan y la cierro». ¿Qué observación es correcta?", "No: marcar sin comprobar falsea el registro; debe quedar pendiente e informarse", "Es correcta, porque solo son 2 ítems", "Es correcta, si lo hace en la misma fecha", "Un registro falso puede esconder un defecto."),
        ("abc", "{F} Para la OT-C-10, ¿qué corresponde informar?", "Los 2 ítems pendientes y la firma independiente faltante, con responsable y motivo", "Solo que la orden está casi lista", "Nada, porque el técnico ya firmó", "Un pendiente se informa por escrito con su motivo y su responsable."),
        ("=", "En una orden de ejemplo hay 40 ítems y 34 están marcados. ¿Cuántos son pendientes?", "40-34", "Se resta lo marcado al total.", " ítems"),
        ("abc", "Un defecto de ejemplo no se puede resolver en el turno y la persona a cargo dice «lo dejo escrito y sigo». ¿Qué falta para diferirlo?", "La autorización de personal certificado, con condiciones y plazo registrados", "Nada, porque dejarlo escrito basta", "Solo la fecha", "Diferir exige una decisión autorizada, no solo una anotación."),
    ],
    ctx=("abc", "Una persona de un hangar de ejemplo te dice: «firma tú la revisión independiente de mi trabajo, así cerramos hoy». ¿Qué respondes?", "Que no, porque la revisión independiente la hace otra persona que sí comprobó el trabajo", "Que sí, porque firmar es solo un trámite", "Que sí, si la fecha es de hoy", "Firmar sin comprobar anula el valor de la verificación."),
    sc=[
        ("En Mantenimiento de Aeronaves: ¿qué es un ítem pendiente?", "Un ítem no cumplido o no verificado", "Es lo que falta para cerrar la orden."),
        ("¿Quién autoriza diferir un defecto?", "Personal certificado", "Esa decisión no le corresponde al técnico."),
        ("¿Por qué no se marca un ítem sin comprobar?", "Porque el registro quedaría falso", "Un registro falso puede esconder un defecto."),
    ],
    op=("Dos órdenes de ejemplo: OT-D-1 tiene 25 ítems, 20 marcados, firma del técnico, sin revisión independiente. OT-D-2 tiene 25 ítems, 25 marcados, firma del técnico y revisión independiente. Escribe (a) cuántos pendientes tiene OT-D-1, (b) qué porcentaje de ítems está marcado en OT-D-1, (c) qué orden está lista para cerrarse y por qué, (d) qué haces con los pendientes de OT-D-1 sin marcarlos como cumplidos.",
        "(a) 25 - 20 = 5 pendientes. (b) 20 × 100 / 25 = 80 %. (c) OT-D-2, porque tiene todos los ítems y las dos firmas. (d) Los dejo como pendientes, los informo por escrito con su motivo y su responsable; si hay que diferir, decide personal certificado.",
        ["calcula los pendientes", "calcula el porcentaje", "elige la orden completa con razón", "informa los pendientes sin falsear"],
        ["hoja con las cuatro respuestas"],
        ["marcar ítems sin comprobar", "decidir diferir por cuenta propia", "olvidar la firma independiente"],
        "Pregunta: «¿qué falta para que la orden esté cerrada?». Si duda, pídele que relea las condiciones de cierre."),
    reinforce="Inventa una orden con 16 ítems y 12 marcados, calcula los pendientes y el porcentaje y escribe qué informarías.",
    extend="Explica con un ejemplo por qué la honestidad del registro es parte de la seguridad.",
)
