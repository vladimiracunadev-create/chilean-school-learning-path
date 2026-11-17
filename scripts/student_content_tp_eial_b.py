"""Elaboración Industrial de Alimentos TP (3.º y 4.º medio): OAE-04 (higiene personal, de infraestructura, maquinaria y utensilios), OAE-05 (verificar el funcionamiento de máquinas, equipos e instrumentos: solo conceptos, registros y cálculos) y OAE-06 (controlar y registrar variables de proceso: BPM, POE, POES y HACCP como conceptos). Todo en papel: plantas, equipos, lotes y límites inventados y rotulados «de ejemplo»."""
from __future__ import annotations

from tp_eial_common import build

O4 = "TP-EIAL-3y4-OAE-04"
O5 = "TP-EIAL-3y4-OAE-05"
O6 = "TP-EIAL-3y4-OAE-06"
LIM = " Esto es aprendizaje conceptual en papel, con datos de ejemplo: la práctica en una planta de alimentos requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria, SEC, etc.); este cuaderno no te habilita para trabajar."
LIMX = " Las máquinas, los equipos de frío, las atmósferas peligrosas y los productos químicos de limpieza solo se estudian aquí como concepto: su uso requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria, SEC, etc.); este cuaderno no te habilita para trabajar. Ante un accidente o una intoxicación, avisa a un adulto responsable y a emergencias."

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (reglas de higiene de una planta de ejemplo, inventada). El ingreso del personal se hace por el vestidor, donde se cambia la ropa de calle por ropa de trabajo, cofia y calzado de la planta. Las manos se lavan al ingresar, después de ir al baño, después de tocar residuos o superficies sucias y cuando el supervisor lo indique. "
     "No se usan joyas ni esmalte de uñas en la zona de producción. La persona con síntomas de enfermedad digestiva o con una herida abierta avisa al supervisor y no ingresa a producción hasta que la jefatura lo indique. "
     "El flujo del personal va de la zona sucia (recepción y bodega de envases exteriores) a la zona limpia (envasado), nunca al revés. Las visitas siguen las mismas reglas. La autoridad sanitaria fiscaliza el cumplimiento de la norma sanitaria vigente.")
build(
    O4, 1, F,
    use="Aprenderé a situar la higiene en una planta de alimentos: por qué importa la higiene personal, qué reglas generales existen, qué son las zonas limpia y sucia y qué peligros se previenen.",
    prior=["Conozco el flujo general de una planta de alimentos.", "Sé leer una ficha con reglas.", "Sé sumar y multiplicar enteros."],
    explain=[
        "La higiene en una planta de alimentos protege al consumidor y al producto. Se divide en higiene personal (cómo se presenta y se comporta quien trabaja), higiene de la infraestructura (pisos, paredes, baños y vestidores) y de las máquinas y utensilios (lo que toca el producto). La norma sanitaria vigente fija las exigencias y la autoridad sanitaria fiscaliza que se cumplan.",
        "Los peligros que se previenen son biológicos (microbios que pasan de las manos o del ambiente al producto), químicos (restos de productos de limpieza) y físicos (objetos como joyas, botones o trozos de vidrio que caen al producto). Una planta separa una zona sucia (donde llegan materias primas y envases exteriores) de una zona limpia (donde el producto queda más expuesto), y el personal circula de la sucia a la limpia, nunca al revés.",
        "Limpiar es retirar la suciedad visible; sanitizar es reducir los microbios a un nivel seguro. Las personas con síntomas de enfermedad o con heridas abiertas lo avisan al supervisor y la jefatura decide. Los productos químicos de limpieza solo los usa personal capacitado." + LIMX,
    ],
    vocab=[("higiene personal", "hábitos y presentación de quien trabaja para no contaminar el producto"), ("zona sucia", "área donde llegan materias primas y envases exteriores"), ("zona limpia", "área donde el producto está más expuesto, como el envasado"), ("limpiar", "retirar la suciedad visible"), ("sanitizar", "reducir los microbios a un nivel seguro"), ("peligro biológico", "microbios que pueden dañar la salud"), ("peligro físico", "objeto extraño, como una joya o vidrio, en el producto")],
    worked=[
        ("Clasificar un peligro", "Un botón de una camisa cae dentro de un producto sin envasar. ¿Qué tipo de peligro es?", ["Es un objeto extraño en el alimento.", "Eso corresponde a un peligro físico."], "Peligro físico"),
        ("Ubicar zonas", "En una planta de ejemplo, ¿la recepción de materias primas está en zona sucia o limpia?", ["Allí llegan materias primas y envases exteriores.", "Esa área corresponde a la zona sucia."], "Zona sucia"),
    ],
    mistakes=[("Pensar que lavarse las manos solo al ingresar es suficiente.", "Las manos se ensucian de nuevo al tocar residuos o superficies sucias.", "Lávalas cada vez que la regla lo pida: al ingresar, tras el baño, tras tocar residuos y cuando el supervisor lo indique."),
              ("Ocultar una herida abierta para no perder el turno.", "Una herida puede contaminar el producto y la jefatura debe decidir cómo proteger al producto y a la persona.", "Avisa al supervisor y sigue lo que indique la jefatura.")],
    T=[
        ("abc", "{F} ¿Qué debe hacer una persona con síntomas de enfermedad digestiva antes de entrar a producción?", "Avisar al supervisor y no ingresar hasta que la jefatura lo indique", "Trabajar solo en tareas livianas sin avisar", "Entrar usando doble guante", "La ficha pide avisar y esperar la indicación de la jefatura antes de ingresar."),
        ("abc", "{F} Según la ficha, ¿cuándo se lavan las manos?", "Al ingresar, después del baño, después de tocar residuos y cuando el supervisor lo indique", "Solo al terminar la jornada", "Solo cuando se ven sucias", "La ficha enumera esas situaciones y no condiciona el lavado a lo que se ve."),
        ("abc", "{F} ¿Qué zona es la de envasado?", "La zona limpia", "La zona sucia", "Una zona sin clasificar", "La ficha ubica el envasado en la zona limpia, donde el producto está más expuesto."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué diferencia hay entre limpiar y sanitizar?", "Limpiar retira la suciedad visible y sanitizar reduce los microbios a un nivel seguro", "Son lo mismo con distinto nombre", "Sanitizar retira la suciedad visible y limpiar reduce los microbios", "La limpieza actúa sobre la suciedad que se ve y la sanitización sobre los microbios."),
        ("abc", "{F} ¿Por qué no se permiten joyas ni esmalte de uñas en producción?", "Pueden desprenderse y caer al producto como un peligro físico", "Porque disminuyen la velocidad del trabajo", "Porque cambian el sabor del producto", "Un objeto o trozo que cae al alimento es un peligro físico."),
        ("abc", "{F} Una visita quiere entrar a la zona limpia con su ropa de calle. ¿Qué corresponde?", "Debe seguir las mismas reglas: ropa de la planta y lavado de manos", "Puede entrar si no toca nada", "Puede entrar si va acompañada por un supervisor", "La ficha establece que las visitas siguen las mismas reglas de ingreso."),
        ("=", "Una planta entrega una cofia por persona y por turno. Con 45 personas por turno y 3 turnos al día, ¿cuántas cofias se usan en un día?", "45*3", "Se multiplican las personas por turno por la cantidad de turnos.", " cofias"),
        ("abc", "{F} ¿Por qué el personal circula de la zona sucia a la limpia y no al revés?", "Para evitar llevar suciedad y microbios de la zona sucia a la limpia", "Para acortar el recorrido de la jornada", "Para que haya menos personas en la zona sucia", "El sentido del flujo evita arrastrar contaminación hacia donde el producto está expuesto."),
        ("abc", "{F} Un operario estornuda sobre un producto sin envasar. ¿Qué tipo de peligro se genera?", "Biológico, por el paso de microbios", "Físico, por un objeto extraño", "Químico, por restos de limpieza", "Los microbios de la persona pasan al producto y eso es un peligro biológico."),
        ("abc", "Un jefe dice: «si se lavan las manos al ingresar, ya no hace falta lavarlas después». ¿Qué respuesta es correcta?", "Se lavan cada vez que la regla lo pide, porque se ensucian de nuevo durante el trabajo", "Tiene razón, el lavado inicial dura todo el turno", "Solo se vuelven a lavar cuando termina el turno", "Tocar residuos o ir al baño vuelve a contaminar las manos, por eso la regla pide lavarlas otra vez."),
        ("abc", "{F} Un operario tiene una herida abierta en la mano. ¿Qué corresponde según la regla de la planta?", "Avisar al supervisor, que decide con la jefatura cómo proceder", "Cubrirla con un guante y seguir igual", "Esperar al fin del turno para avisar", "La ficha pide avisar y no ingresar a producción hasta que la jefatura lo indique."),
        ("=", "Se verifican 40 puntos de ingreso por día durante 5 días, y cada día hay 2 incumplimientos. ¿Cuántos puntos cumplieron en total?", "40*5-2*5", "Se calculan todos los puntos verificados y se restan los incumplidos.", " puntos"),
        ("abc", "{F} Un operario sale a la zona sucia a buscar cajas y vuelve directo a la línea sin lavarse las manos. ¿Cuál es la falta?", "No se lavó las manos al volver de la zona sucia, lo que puede contaminar el producto", "Salió al exterior, y eso siempre es una falta grave", "Ninguna, porque no tocó el producto", "La ficha pide lavar las manos tras tocar superficies sucias, aunque no se toque el producto de inmediato."),
    ],
    ctx=("abc", "{F} Antes de una visita de la autoridad sanitaria, un jefe pide limpiar bien solo la entrada y dejar el resto «para después». ¿Qué observación corresponde?", "La higiene se mantiene todos los días en toda la planta, no solo para las visitas", "Es correcto, porque solo se fiscaliza la entrada", "Basta con ordenar el vestidor", "La norma sanitaria exige condiciones permanentes, y no solo para una fiscalización."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué diferencia hay entre zona sucia y zona limpia?", "La sucia recibe materias primas y envases exteriores; la limpia es donde el producto está más expuesto", "Separarlas evita llevar contaminación hacia el producto."),
        ("¿Qué hace una persona con una herida abierta?", "Avisa al supervisor y espera la indicación de la jefatura", "Así se protege al producto y a la persona."),
        ("¿Quién fiscaliza la norma sanitaria vigente?", "La autoridad sanitaria", "Es la institución que controla las condiciones sanitarias de los establecimientos."),
    ],
    op=("Un día de ejemplo en una planta ocurren tres situaciones: (1) una operaria llega con una pulsera y la mantiene puesta en la línea, (2) un operario con síntomas de enfermedad digestiva no avisa y entra a producción, (3) un visitante pasa a la zona limpia sin lavarse las manos «porque solo mira». "
        "Escribe: (a) qué regla de la ficha incumple cada situación, (b) qué tipo de peligro puede generar cada una y (c) qué corresponde hacer en cada caso.",
        "(a) 1: no se usan joyas en producción. 2: debe avisar y no ingresar. 3: las visitas siguen las mismas reglas, incluido el lavado de manos. (b) 1: peligro físico; 2 y 3: peligro biológico. (c) 1: retirar la pulsera antes de ingresar. 2: avisar al supervisor y esperar su indicación. 3: lavarse las manos y seguir las reglas de ingreso.",
        ["asocia cada situación con su regla", "clasifica los peligros", "indica una acción en cada caso"],
        ["hoja con las tres respuestas"],
        ["decir que la pulsera es un peligro biológico", "permitir al visitante entrar sin reglas", "no avisar en el caso de síntomas"],
        "Pregunta: «¿qué le podría pasar al producto si la pulsera se desprende?». Debe decir que caería al producto como peligro físico."),
    reinforce="Escribe cinco reglas de higiene de una planta inventada y marca cuáles son de higiene personal y cuáles de infraestructura.",
    extend="Explica con un ejemplo inventado por qué la ropa de calle no entra a la zona limpia.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (programa de limpieza de una planta de ejemplo, inventada). Planilla: (1) piso de la zona de envasado, al final de cada turno, a cargo del operario de aseo, con registro firmado; (2) mesa de selección, al terminar cada turno, a cargo del operario de línea, con registro firmado; "
     "(3) vestidor y baños, dos veces al día, a cargo del operario de aseo; (4) equipo de envasado, limpieza profunda cada semana, a cargo de personal autorizado de mantención, con el equipo detenido y bloqueado; "
     "(5) verificación visual con pauta, a cargo del supervisor. Los productos de limpieza los usa solo personal capacitado, siguiendo la hoja de datos de seguridad.")
build(
    O4, 2, F,
    use="Aprenderé el vocabulario de la higiene: POES, programa de limpieza, verificación, registro y hoja de datos de seguridad, y qué rol responde por cada tarea.",
    prior=["Conozco la diferencia entre limpiar y sanitizar.", "Sé leer una planilla.", "Sé restar enteros."],
    explain=[
        "Un POES (Procedimiento Operativo Estandarizado de Saneamiento) es un documento que define qué se limpia o sanitiza, cuándo, quién lo hace y cómo se verifica. El programa de limpieza reúne esas tareas en una planilla con frecuencia, responsable y registro firmado. Los métodos concretos de limpieza y los productos los define el docente de la especialidad y la norma vigente.",
        "La verificación es la revisión posterior de que la tarea quedó bien hecha, por ejemplo con una pauta visual del supervisor. El registro firmado demuestra que se hizo, quién lo hizo y cuándo. Un registro rellenado de una sola vez, sin hacer la tarea en su momento, no tiene valor.",
        "La hoja de datos de seguridad es el documento del fabricante de un producto químico, que informa sus riesgos y las precauciones. Los productos de limpieza no se mezclan y solo los usa personal capacitado con la protección que corresponde. Un equipo se limpia en profundidad solo si está detenido y bloqueado por personal autorizado." + LIMX,
    ],
    vocab=[("POES", "procedimiento operativo estandarizado de saneamiento"), ("programa de limpieza", "planilla con tareas, frecuencia, responsable y registro"), ("verificación", "revisión posterior de que la tarea quedó bien hecha"), ("registro firmado", "anotación que demuestra qué se hizo, quién y cuándo"), ("hoja de datos de seguridad", "documento del fabricante con los riesgos y precauciones de un producto químico"), ("bloqueo", "dejar un equipo sin energía y señalizado antes de intervenirlo")],
    worked=[
        ("Leer una planilla", "En un programa de ejemplo, el piso se limpia al final de cada turno a cargo del operario de aseo. ¿Quién es el responsable?", ["Se busca la tarea en la planilla.", "El responsable indicado es el operario de aseo."], "El operario de aseo"),
        ("Distinguir verificación", "El supervisor revisa con una pauta si el piso quedó limpio. ¿Esa etapa es limpieza o verificación?", ["Revisa un trabajo ya hecho.", "Eso es verificación."], "Verificación"),
    ],
    mistakes=[("Firmar todo el registro del mes en una tarde.", "El registro deja de demostrar que la tarea se hizo en su momento.", "Firma cada tarea cuando se realiza."),
              ("Mezclar dos productos de limpieza «para que limpie más».", "Puede generar reacciones peligrosas y no está permitido.", "No mezcles productos; solo personal capacitado los usa según la hoja de datos de seguridad.")],
    T=[
        ("abc", "{F} ¿Con qué frecuencia se limpia la mesa de selección?", "Al terminar cada turno", "Una vez por semana", "Solo cuando se ve sucia", "La planilla fija la limpieza de la mesa al terminar cada turno."),
        ("abc", "{F} ¿Quién hace la limpieza profunda semanal del equipo de envasado?", "Personal autorizado de mantención", "Cualquier operario de línea", "El supervisor, sin detener el equipo", "La planilla asigna esa tarea a personal autorizado de mantención con el equipo detenido y bloqueado."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es un POES?", "Un documento que define qué, cuándo y quién limpia o sanitiza, y cómo se verifica", "Un producto químico de limpieza", "Un registro de ventas de la planta", "El POES ordena las tareas de saneamiento de la planta."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es la verificación en el programa de limpieza?", "La revisión posterior de que la tarea quedó bien hecha", "El pedido de los productos de limpieza", "La firma anticipada del registro", "Verificar es comprobar el resultado de una tarea ya realizada."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es una hoja de datos de seguridad?", "El documento del fabricante con los riesgos y precauciones de un producto químico", "Una receta para preparar el producto de limpieza", "Una lista de precios de proveedores", "Informa cómo manejar el producto de forma segura."),
        ("abc", "{F} ¿Para qué la planilla pide un responsable y un registro firmado en cada tarea?", "Para saber quién hizo cada tarea y poder verificarla", "Para reducir la cantidad de tareas", "Para cobrar a quien no cumpla", "El responsable y la firma permiten trazar y verificar cada tarea."),
        ("=", "Un programa de ejemplo tiene 6 tareas diarias de limpieza durante 5 días, y se firmaron 27 tareas. ¿Cuántas quedaron sin firma?", "6*5-27", "Se calculan todas las tareas de la semana y se restan las firmadas.", " tareas"),
        ("abc", "{F} Un supervisor revisa con una pauta visual el piso ya limpio. ¿Cómo se llama esa etapa?", "Verificación", "Limpieza profunda", "Registro de compra", "Revisar una tarea ya hecha es verificar."),
        ("abc", "{F} Un operario mezcla dos productos de limpieza «para que limpie más». ¿Qué respuesta corresponde?", "No se mezclan; solo personal capacitado usa los productos según la hoja de datos de seguridad", "Es correcto si se hace en un lugar ventilado", "Es correcto si el producto es de una marca conocida", "Mezclar productos puede generar riesgos y no está permitido."),
        ("abc", "Una planilla de limpieza llega con todas las firmas del mes escritas con la misma letra, en una sola tarde. ¿Qué problema hay?", "Los registros pierden valor si no se hacen cuando se realiza cada tarea", "Ninguno, porque lo importante es que esté completa", "Solo importa que la letra sea clara", "Un registro hecho a posteriori no demuestra que la tarea se realizó."),
        ("abc", "Un equipo se ve limpio, pero no se ha sanitizado. ¿Qué afirmación es correcta?", "Puede conservar microbios que no se ven, por eso limpiar no reemplaza sanitizar", "Está listo para usarse, porque se ve limpio", "Está sanitizado, porque limpiar y sanitizar son iguales", "Los microbios no se ven, por lo que se necesita sanitizar además de limpiar."),
        ("=", "En una semana de ejemplo, el vestidor se limpia 2 veces al día durante 7 días, y cada limpieza ocupa a 2 personas. ¿Cuántas asignaciones de personal hay en la semana?", "2*7*2", "Se multiplican las limpiezas por día, los días y las personas.", " asignaciones"),
        ("abc", "{F} Alguien propone limpiar el equipo de envasado en profundidad mientras sigue funcionando, para no perder producción. ¿Qué corresponde?", "No hacerlo: la limpieza profunda se hace con el equipo detenido y bloqueado por personal autorizado", "Hacerlo con cuidado y rapidez", "Hacerlo solo en el turno de noche", "La ficha indica que esa tarea la hace personal autorizado con el equipo detenido y bloqueado."),
    ],
    ctx=("abc", "{F} A mitad de turno se derrama producto en el piso de la zona de envasado, antes de la limpieza programada. ¿Qué corresponde?", "Avisar al supervisor y limpiar de inmediato según el procedimiento, sin esperar al fin del turno", "Esperar al fin del turno, porque así dice la planilla", "Cubrir el derrame con una caja", "Un derrame es un riesgo de contaminación y de resbalón, por lo que no espera la limpieza programada."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué es el programa de limpieza?", "Una planilla con tareas, frecuencia, responsable y registro", "Ordena y respalda el trabajo de saneamiento."),
        ("¿Quién usa los productos de limpieza?", "Solo personal capacitado, siguiendo la hoja de datos de seguridad", "Así se evitan accidentes y mezclas peligrosas."),
        ("¿Qué demuestra un registro firmado?", "Qué se hizo, quién lo hizo y cuándo", "Es la prueba escrita de que la tarea se realizó."),
    ],
    op=("Programa de ejemplo de una planta con 2 turnos al día: (1) piso de envasado, al final de cada turno; (2) baños, dos veces al día; (3) mesa de selección, al terminar cada turno, con registro firmado; (4) equipo, limpieza profunda semanal por personal autorizado de mantención con el equipo detenido y bloqueado. Registro de ayer: el piso figura limpiado dos veces, los baños una vez y la mesa de selección sin firma. "
        "Escribe: (a) qué tareas del registro no cumplen el programa, (b) qué problema tiene un registro sin firma, (c) quién debe verificar el trabajo y (d) por qué la limpieza profunda no la hace cualquier operario.",
        "(a) Los baños se limpiaron una vez y debían ser dos, y la mesa quedó sin firma. (b) No demuestra que la tarea se hizo, quién la hizo ni cuándo. (c) El supervisor, con una pauta de verificación. (d) Porque exige equipo detenido y bloqueado, y eso lo hace personal autorizado de mantención.",
        ["identifica las dos fallas del registro", "explica el valor de la firma", "nombra al verificador y justifica la limpieza profunda"],
        ["hoja con las cuatro respuestas"],
        ["decir que la mesa estaba bien aunque no está firmada", "creer que cualquier operario puede hacer la limpieza profunda", "no mencionar al supervisor"],
        "Pregunta: «¿cómo sabrías que la mesa se limpió si no hay firma?». Debe decir que no hay prueba."),
    reinforce="Escribe un programa de limpieza de tres filas para una planta inventada, con frecuencia, responsable y registro.",
    extend="Explica con un ejemplo inventado por qué verificar una tarea es distinto de hacerla.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (pauta de inspección de higiene de la zona de envasado, de ejemplo e inventada). Diez ítems: (1) personal con cofia y delantal limpios: cumple; (2) lavamanos con jabón y toallas: no cumple, faltan toallas; (3) sin joyas en producción: cumple; (4) piso limpio y seco: no cumple, hay charcos; "
     "(5) utensilios guardados en su lugar: cumple; (6) basureros con tapa y vaciados: no cumple, uno rebalsa; (7) registro de limpieza firmado: cumple; (8) productos de limpieza separados del producto: cumple; (9) equipos limpios al inicio del turno: cumple; (10) sin evidencia de plagas: cumple. "
     "Meta de ejemplo: al menos 90 % de ítems que cumplen. Una acción correctiva corrige lo que falló; una acción preventiva evita que vuelva a ocurrir.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un caso en papel: leer una pauta de inspección de higiene, calcular el porcentaje de cumplimiento y proponer acciones correctivas y preventivas.",
    prior=["Conozco el programa de limpieza y la verificación.", "Sé calcular porcentajes con enteros.", "Sé leer una lista de ítems."],
    explain=[
        "Una pauta de inspección es una lista de ítems que el supervisor revisa y marca como cumple o no cumple. El porcentaje de cumplimiento se calcula con los ítems que cumplen por 100, dividido por el total. Se compara con una meta, que en este cuaderno es un valor de ejemplo.",
        "Cuando un ítem no cumple se anota la causa y se define una acción correctiva, que corrige lo que falló (por ejemplo, reponer las toallas). Para que no se repita se agrega una acción preventiva, como programar una revisión periódica del stock de toallas. Las acciones llevan responsable y se verifican después.",
        "El criterio de cada ítem no cambia con el tamaño del problema: un charco pequeño igual es un incumplimiento, porque favorece los microbios y los resbalones. Todos los incumplimientos se informan, aunque bajen el puntaje." + LIM,
    ],
    vocab=[("pauta de inspección", "lista de ítems que se revisan y se marcan como cumple o no cumple"), ("porcentaje de cumplimiento", "ítems que cumplen por 100, dividido por el total"), ("acción correctiva", "medida que corrige lo que falló"), ("acción preventiva", "medida que evita que el problema vuelva a ocurrir"), ("incumplimiento", "ítem que no cumple el criterio")],
    worked=[
        ("Calcular el cumplimiento", "Una pauta de ejemplo tiene 20 ítems y 16 cumplen. ¿Cuál es el porcentaje de cumplimiento?", ["Se multiplican los ítems que cumplen por 100.", "16 × 100 ÷ 20 = 80."], "80 %"),
        ("Distinguir acciones", "Se repone el jabón que faltaba y se programa una revisión semanal de su stock. ¿Cuál es la acción correctiva y cuál la preventiva?", ["Reponer el jabón corrige lo que faltaba.", "La revisión semanal evita que vuelva a faltar."], "Correctiva: reponer; preventiva: la revisión semanal"),
    ],
    mistakes=[("Marcar «cumple» un piso con un charco «porque es pequeño».", "El criterio exige piso seco; el tamaño no cambia el incumplimiento.", "Marca «no cumple» si no se cumple el criterio y corrige."),
              ("Quedarse solo con la acción correctiva.", "El problema puede repetirse si no se evita su causa.", "Agrega una acción preventiva con responsable.")],
    T=[
        ("abc", "{F} ¿Cuántos ítems no cumplen?", "Tres", "Dos", "Cuatro", "Los ítems 2, 4 y 6 son los que no cumplen."),
        ("=", "{F} ¿Cuántos ítems cumplen?", "10-3", "Al total de ítems se le restan los que no cumplen.", " ítems"),
        ("=", "{F} ¿Cuál es el porcentaje de cumplimiento de la pauta?", "7*100//10", "Se multiplican los ítems que cumplen por 100 y se divide por el total.", " %"),
        ("abc", "{F} ¿Cumple la pauta la meta de 90 %?", "No, porque llega a 70 %", "Sí, porque la mayoría de los ítems cumple", "Sí, porque 7 es más que la mitad", "70 % es menor que la meta de 90 %."),
        ("abc", "{F} ¿Qué ítem no cumplido se relaciona con el lavado de manos?", "El lavamanos sin toallas", "El piso con charcos", "El basurero que rebalsa", "Sin toallas no se puede completar el lavado y secado de manos."),
        ("abc", "{F} ¿Qué acción correctiva corresponde para el basurero que rebalsa?", "Vaciarlo y dejar registro de la acción con responsable", "Marcarlo como cumple sin vaciarlo ni dejar registro", "Esperar la próxima inspección", "La acción correctiva soluciona lo que falló y queda registrada."),
        ("=", "{F} Si se corrigen 2 de los 3 incumplimientos, ¿qué porcentaje de cumplimiento tendría la pauta?", "(7+2)*100//10", "Se suman los ítems que pasan a cumplir y se calcula el porcentaje.", " %"),
        ("abc", "{F} Programar una revisión semanal del stock de toallas para que no vuelvan a faltar es una acción...", "Preventiva", "Correctiva", "De verificación", "Evita que el problema se repita, que es lo propio de una acción preventiva."),
        ("abc", "{F} ¿Por qué el piso con charcos es un problema de higiene y de seguridad?", "Favorece el crecimiento de microbios y puede provocar resbalones", "Solo afecta el aspecto de la planta", "Solo es un problema si hay visitas", "El agua estancada favorece microbios y aumenta el riesgo de caídas."),
        ("abc", "{F} El inspector propone marcar «cumple» el piso porque el charco es pequeño. ¿Qué corresponde?", "Marcar «no cumple», porque el tamaño no cambia el criterio, y corregirlo", "Marcar «cumple» para no bajar el puntaje", "Marcar «cumple» si el charco se seca en el turno", "El criterio exige piso seco y se evalúa siempre de la misma forma."),
        ("abc", "Dos supervisores revisan lo mismo: uno marca 8 ítems que cumplen y el otro 7. ¿Qué conviene hacer?", "Aclarar el criterio de cada ítem para que todos evalúen igual", "Promediar los dos resultados", "Usar siempre el resultado más alto", "Un criterio claro permite que distintas personas lleguen al mismo resultado."),
        ("=", "En otra pauta de ejemplo con 20 ítems, 17 cumplen. ¿Cuál es el porcentaje de cumplimiento?", "17*100//20", "Se multiplican los ítems que cumplen por 100 y se divide por el total.", " %"),
        ("abc", "{F} Antes de entregar el informe, el jefe quiere omitir los tres incumplimientos porque bajan la nota de la planta. ¿Qué corresponde?", "Informar los tres incumplimientos junto con sus acciones correctivas", "Omitirlos si ya se corrigieron", "Informarlos solo si lo pide la autoridad", "Ocultar incumplimientos impide corregir y mejorar; el informe debe reflejar lo observado."),
    ],
    ctx=("abc", "{F} El supervisor encuentra que faltan toallas por tercera vez en el mes. ¿Qué medida es la más completa?", "Reponerlas ahora y fijar una acción preventiva con responsable para revisar el stock", "Reponerlas ahora, sin más", "Pedir al personal que traiga sus propias toallas", "Reponer corrige y la revisión periódica evita la repetición."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cómo se calcula el porcentaje de cumplimiento?", "Ítems que cumplen por 100, dividido por el total", "Relaciona lo que cumple con el total de ítems."),
        ("¿Qué diferencia hay entre acción correctiva y preventiva?", "La correctiva corrige lo que falló; la preventiva evita que se repita", "Una actúa sobre el problema presente y la otra sobre su repetición."),
        ("¿Se informa un incumplimiento aunque baje el puntaje?", "Sí, todos los incumplimientos se informan", "Ocultarlos impide corregirlos y mejorar el trabajo de la planta."),
    ],
    op=("Pauta de ejemplo con 10 ítems: cumplen 8. No cumplen: (a) un basurero sin tapa y (b) un registro de limpieza sin firma. Meta de ejemplo: 90 %. "
        "Escribe: (a) el porcentaje de cumplimiento, (b) si cumple la meta, (c) una acción correctiva para cada incumplimiento y (d) una acción preventiva para evitar que se repita el registro sin firma.",
        "(a) 8 × 100 ÷ 10 = 80 %. (b) No cumple la meta de 90 %. (c) Basurero: colocar la tapa y vaciarlo; registro: firmar la tarea realizada con verificación del supervisor. (d) Revisar las firmas al cierre de cada turno.",
        ["calcula el 80 % y compara con la meta", "propone una acción correctiva por ítem", "propone una acción preventiva"],
        ["hoja con las cuatro respuestas"],
        ["no comparar con la meta", "confundir correctiva con preventiva", "proponer ocultar el incumplimiento"],
        "Pregunta: «¿qué diferencia hay entre colocar la tapa y revisar las firmas al cierre?». Debe decir que una corrige y la otra previene."),
    reinforce="Inventa una pauta de seis ítems, marca cuáles cumplen y calcula su porcentaje de cumplimiento.",
    extend="Explica con un ejemplo inventado por qué una acción correctiva sin acción preventiva puede repetirse.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (registro semanal de higiene de ejemplo, inventado). Pauta diaria de 10 ítems; ítems que cumplen cada día: lunes 9, martes 8, miércoles 9, jueves 10, viernes 7. Meta diaria de ejemplo: 90 %. "
     "Regla de la planta: si dos o más días de la semana quedan bajo la meta, se programa una capacitación al personal. "
     "Stock de cofias: 400 al inicio de la semana; consumo de 60 por día durante 5 días; se pide reposición cuando el stock queda por debajo del consumo de dos días.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar criterios con datos de ejemplo: calcular el cumplimiento diario y semanal, aplicar una regla para decidir una capacitación y calcular el stock y la reposición de elementos de protección.",
    prior=["Conozco la pauta de inspección.", "Sé calcular porcentajes con enteros.", "Sé sumar, restar y multiplicar enteros."],
    explain=[
        "Un registro semanal permite calcular el cumplimiento de cada día y el de toda la semana. El porcentaje diario se calcula con los ítems que cumplen por 100, dividido por 10 en esta pauta. El porcentaje semanal suma los ítems que cumplen de todos los días y los divide por el total de ítems de la semana. El semanal puede ocultar días críticos, por eso se mira también cada día.",
        "Una regla de decisión convierte los datos en acciones: por ejemplo, si dos o más días quedan bajo la meta, se programa una capacitación. Aplicarla es comparar el dato con la regla, sin cambiar la regla según convenga.",
        "Los elementos de protección y de higiene, como cofias, se controlan con un stock mínimo: cuando el stock queda por debajo del consumo de dos días, se pide reposición. Así no faltan en el momento en que se necesitan." + LIM,
    ],
    vocab=[("cumplimiento diario", "porcentaje de ítems que cumplen en un día"), ("cumplimiento semanal", "porcentaje de ítems que cumplen en toda la semana"), ("regla de decisión", "criterio escrito que convierte un dato en una acción"), ("stock mínimo", "cantidad que no debe faltar en bodega"), ("reposición", "nuevo pedido para recuperar el stock")],
    worked=[
        ("Cumplimiento semanal", "Una planta de ejemplo registró en tres días 8, 9 y 10 ítems que cumplen, de 10 por día. ¿Cuál es el cumplimiento de esos días?", ["Se suman los ítems que cumplen: 8 + 9 + 10 = 27.", "27 × 100 ÷ 30 = 90."], "90 %"),
        ("Aplicar una regla", "La regla de ejemplo dice: con un solo día bajo la meta no se capacita; con dos o más, sí. Hubo dos días bajo la meta. ¿Se capacita?", ["Se compara con la regla.", "Dos días cumplen la condición de dos o más."], "Sí, se capacita"),
    ],
    mistakes=[("Mirar solo el porcentaje semanal y olvidar los días críticos.", "El promedio puede ocultar un día muy bajo.", "Revisa también el cumplimiento de cada día."),
              ("Cambiar la regla de decisión para no tener que capacitar.", "La decisión deja de basarse en los datos.", "Aplica la regla tal como está escrita.")],
    T=[
        ("=", "{F} ¿Cuál fue el cumplimiento del lunes, en porcentaje?", "9*100//10", "Se multiplican los ítems que cumplen por 100 y se divide por 10.", " %"),
        ("=", "{F} ¿Cuántos ítems cumplieron en total durante la semana?", "9+8+9+10+7", "Se suman los ítems que cumplen de cada día.", " ítems"),
        ("abc", "{F} ¿Qué días quedaron bajo la meta de 90 %?", "El martes y el viernes", "Solo el viernes", "El lunes y el miércoles", "El martes tuvo 80 % y el viernes 70 %; los demás llegaron a 90 % o más."),
        ("=", "{F} ¿Cuál fue el cumplimiento semanal, en porcentaje?", "(9+8+9+10+7)*100//50", "Se divide el total de ítems que cumplen por los 50 ítems de la semana.", " %"),
        ("abc", "{F} Según la regla de la planta, ¿se programa una capacitación?", "Sí, porque dos días quedaron bajo la meta", "No, porque el cumplimiento semanal es alto", "No, porque la regla pide tres días", "La regla exige dos o más días bajo la meta y hubo dos."),
        ("=", "{F} ¿Cuántos puntos porcentuales hay entre el mejor y el peor día de la semana?", "100-70", "Se resta el cumplimiento del peor día al del mejor.", " puntos"),
        ("=", "{F} ¿Cuántas cofias quedan al terminar la semana?", "400-60*5", "Al stock inicial se le resta el consumo de los cinco días.", " cofias"),
        ("abc", "{F} Al terminar la semana quedan 100 cofias. ¿Qué corresponde según la regla de stock?", "Pedir reposición, porque 100 es menos que el consumo de dos días", "Esperar, porque aún quedan cofias", "Suspender el uso de cofias para ahorrar", "El consumo de dos días es 120 y el stock quedó por debajo."),
        ("=", "{F} ¿Cuántos pesos cuesta reponer 500 cofias a $50 cada una (precio de ejemplo)?", "500*50", "Se multiplica la cantidad de cofias por el precio de cada una.", " pesos"),
        ("abc", "{F} El viernes bajó a 70 %. Un jefe dice que fue «mala suerte». ¿Cuál es la mejor respuesta?", "Revisar qué ítems fallaron ese día y por qué, antes de concluir", "Aceptar que fue mala suerte y no hacer nada", "Borrar el registro del viernes", "Una causa se busca en los datos; atribuirla a la suerte impide corregirla."),
        ("abc", "¿Por qué sirve registrar el cumplimiento diario y no solo el semanal?", "Porque el semanal puede ocultar días críticos como un viernes muy bajo", "Porque el diario siempre es mayor que el semanal", "Porque el semanal no se puede calcular", "El detalle por día muestra los problemas que un promedio diluye."),
        ("=", "{F} Si el viernes hubieran cumplido 9 ítems en lugar de 7, ¿cuál habría sido el cumplimiento semanal?", "(9+8+9+10+9)*100//50", "Se recalcula el total de ítems que cumplen y se divide por 50.", " %"),
        ("abc", "{F} Con el viernes corregido a 9 ítems que cumplen, ¿habría que programar la capacitación?", "No, porque solo el martes quedaría bajo la meta", "Sí, porque el martes y el viernes seguirían bajo la meta", "Sí, porque el porcentaje semanal no llega a 100 %", "La regla pide dos o más días bajo la meta, y con ese cambio solo uno queda."),
    ],
    ctx=("abc", "{F} El jefe quiere cambiar la regla a «tres o más días» para no tener que capacitar esta semana. ¿Qué observación corresponde?", "Las reglas se aplican como están escritas; si se cambian, se hace con un acuerdo antes y no después de ver los datos", "Es correcto, porque la regla es del jefe", "Es correcto, si el cambio ahorra costos", "Cambiar la regla tras ver los resultados quita objetividad a la decisión."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué es una regla de decisión?", "Un criterio escrito que convierte un dato en una acción", "Evita decidir según preferencias del momento."),
        ("¿Cómo se calcula el cumplimiento semanal?", "Ítems que cumplen en la semana por 100, dividido por el total de ítems", "Usa todos los ítems revisados de la semana."),
        ("¿Cuándo se pide reposición de cofias en esta planta?", "Cuando el stock queda bajo el consumo de dos días", "Así hay tiempo de reponer antes de que se acaben."),
    ],
    op=("Registro de ejemplo de una planta, con una pauta de 10 ítems por día: lunes 10, martes 9, miércoles 8, jueves 7 y viernes 7 ítems que cumplen. Meta diaria: 90 %. Regla: con dos o más días bajo la meta se programa capacitación. Stock de guantes desechables de ejemplo: 900 al inicio; consumo de 150 por día; se repone cuando quedan menos del consumo de dos días. "
        "Escribe: (a) qué días quedaron bajo la meta, (b) el cumplimiento semanal, (c) si se programa capacitación y por qué, y (d) el stock de guantes al final de los 5 días y si se pide reposición.",
        "(a) Miércoles, jueves y viernes. (b) 41 ítems que cumplen de 50, es decir 82 %. (c) Sí, porque tres días están bajo la meta y la regla pide dos o más. (d) 900 − 150 × 5 = 150 guantes; el consumo de dos días es 300, así que se pide reposición.",
        ["identifica los tres días bajo la meta", "calcula 41 de 50 y 82 %", "aplica la regla y calcula el stock final"],
        ["hoja con las cuatro respuestas"],
        ["contar solo dos días bajo la meta", "decidir sin aplicar la regla", "olvidar el consumo de los cinco días"],
        "Pregunta: «¿por qué la regla manda capacitar con tres días bajo la meta?». Debe decir que cumple la condición de dos o más."),
    reinforce="Inventa un registro de cinco días con ítems que cumplen y calcula el cumplimiento de cada día.",
    extend="Explica con un ejemplo inventado por qué una regla de decisión debe fijarse antes de ver los datos.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 5 (línea de envasado de una planta de ejemplo, inventada). Equipos: balanza de control de peso, selladora, cinta transportadora y etiquetadora. Roles: el operador maneja un equipo solo si está autorizado y capacitado; el personal de mantención ajusta y repara; el jefe de producción coordina; el prevencionista de riesgos vela por la seguridad. "
     "Reglas generales: las guardas (protecciones que impiden el contacto con partes peligrosas) no se retiran ni se inhabilitan; ante un ruido anormal, humo, olor extraño o atasco se detiene el equipo según el procedimiento de la planta y se avisa; "
     "toda intervención en un equipo la hacen personas autorizadas, con el equipo bloqueado y señalizado. Producción de ejemplo de la línea: 120 envases por hora.")
build(
    O5, 1, F,
    use="Aprenderé a situar el trabajo con máquinas y equipos de una planta: qué equipos hay, qué riesgos tienen, qué roles intervienen y qué reglas generales de seguridad se cumplen.",
    prior=["Conozco el flujo de una planta de alimentos.", "Sé leer una ficha con reglas.", "Sé multiplicar enteros."],
    explain=[
        "En una planta se usan máquinas, equipos, instrumentos y utensilios. Una máquina o equipo transforma o mueve el producto, como una selladora o una cinta transportadora. Un instrumento mide, como una balanza. Un utensilio es una herramienta manual. Verificar su funcionamiento es comprobar que operan como se espera para asegurar la continuidad del proceso, es decir, que la producción no se detenga sin necesidad.",
        "Las máquinas tienen riesgos: partes móviles que pueden atrapar manos, ropa o cabello, superficies calientes, ruido y electricidad. Las guardas son protecciones que impiden el contacto con esas partes y nunca se retiran. El bloqueo y etiquetado es una medida que deja un equipo sin energía y señalizado para que nadie lo encienda mientras se interviene; lo hace personal capacitado. Un equipo detenido no es un equipo seguro si no está bloqueado.",
        "Cada rol tiene su tarea: el operador maneja el equipo si está autorizado, el personal de mantención ajusta y repara, el jefe de producción coordina y el prevencionista vela por la seguridad. Este cuaderno no enseña a operar ni a reparar máquinas." + LIMX,
    ],
    vocab=[("equipo", "máquina que transforma o mueve el producto"), ("instrumento", "aparato que mide, como una balanza"), ("guarda de seguridad", "protección que impide el contacto con partes peligrosas"), ("bloqueo y etiquetado", "medida que deja un equipo sin energía y señalizado antes de intervenirlo"), ("continuidad del proceso", "que la producción no se detenga sin necesidad"), ("mantención", "conjunto de acciones para que los equipos funcionen bien")],
    worked=[
        ("Clasificar un aparato", "En una planta de ejemplo hay una balanza que mide el peso de cada envase. ¿Es un equipo o un instrumento?", ["La balanza mide.", "Un aparato que mide es un instrumento."], "Instrumento"),
        ("Decidir ante una señal", "Un operador escucha un ruido anormal en la selladora. ¿Qué regla general corresponde?", ["La ficha indica detener según el procedimiento y avisar.", "No se sigue operando ni se interviene por cuenta propia."], "Detener según el procedimiento y avisar"),
    ],
    mistakes=[("Retirar una guarda porque «estorba» para trabajar más rápido.", "Sin guarda se puede atrapar una mano o la ropa en una parte móvil.", "No retires ni inhabilites guardas; si estorban, avisa para que lo evalúe personal autorizado."),
              ("Creer que un equipo detenido ya es seguro.", "Puede volver a encenderse o conservar energía mientras alguien interviene.", "Solo personal autorizado interviene, con el equipo bloqueado y señalizado.")],
    T=[
        ("abc", "{F} ¿Quién ajusta y repara los equipos?", "El personal de mantención", "El operador de la línea", "El jefe de producción", "La ficha asigna ajustes y reparaciones al personal de mantención."),
        ("abc", "{F} ¿Quién puede manejar un equipo?", "Quien está autorizado y capacitado", "Cualquier persona que haya visto cómo se hace", "Quien tenga más antigüedad", "La ficha condiciona el manejo a la autorización y la capacitación."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es una guarda de seguridad?", "Una protección que impide el contacto con partes peligrosas de la máquina", "Un registro de las horas de trabajo del equipo", "Un instrumento que mide el peso", "La guarda es una barrera física entre la persona y una parte peligrosa."),
        ("abc", "{F} Un envase se atasca en la cinta transportadora. ¿Qué corresponde según la ficha?", "No meter la mano: detener el equipo según el procedimiento y avisar a personal autorizado", "Sacarlo con la mano si la cinta va lenta", "Sacarlo con un utensilio mientras la cinta sigue en marcha", "Las partes móviles pueden atrapar manos y utensilios, por lo que el equipo debe detenerse."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es el bloqueo y etiquetado?", "Una medida que deja un equipo sin energía y señalizado antes de intervenirlo", "Pegar el rótulo del producto en el envase", "Una revisión de los precios del equipo", "Impide que alguien encienda el equipo mientras se interviene."),
        ("abc", "{F} ¿Cuál es un riesgo de la cinta transportadora?", "El atrapamiento de manos, ropa o cabello en partes móviles", "La pérdida de rótulos en la bodega", "La disminución del peso neto del producto", "Las partes móviles pueden atrapar a las personas, que es el riesgo propio de este equipo."),
        ("abc", "{F} Un operador nota un ruido anormal en un equipo. ¿Qué corresponde?", "Detener según el procedimiento y avisar al supervisor y a mantención", "Seguir trabajando hasta el fin del turno", "Abrir la protección para ver la causa", "La ficha indica detener y avisar, y no intervenir por cuenta propia."),
        ("=", "{F} La línea se detiene 2 horas por una falla. ¿Cuántos envases se dejan de producir?", "120*2", "Se multiplica la producción por hora por las horas de detención.", " envases"),
        ("=", "En una planta de ejemplo hay 5 equipos, cada uno con una revisión visual de guardas al inicio de cada turno, y trabajan 3 turnos al día. ¿Cuántas revisiones se hacen por día?", "5*3", "Se multiplican los equipos por los turnos.", " revisiones"),
        ("abc", "{F} Un operario retira una guarda porque estorba para trabajar más rápido. ¿Qué respuesta corresponde?", "Las guardas no se retiran; si estorban, se avisa para que lo evalúe personal autorizado", "Es correcto si se hace con cuidado", "Es correcto si solo se retira durante la limpieza", "La ficha prohíbe retirar o inhabilitar guardas."),
        ("abc", "Un compañero dice: «la máquina está detenida, así que no hay peligro». ¿Qué respuesta es correcta?", "Un equipo detenido puede encenderse o conservar energía; necesita bloqueo y etiquetado por personal autorizado", "Tiene razón, porque detenido significa seguro", "Solo hay peligro si el equipo es nuevo", "Detener no basta: el equipo debe quedar sin energía y señalizado."),
        ("=", "Una falla detiene la línea 3 horas. La producción es de 120 envases por hora y cada envase deja un margen de ejemplo de $200. ¿Cuántos pesos de margen se dejan de ganar?", "3*120*200", "Se multiplican las horas, los envases por hora y el margen por envase.", " pesos"),
        ("abc", "{F} Un compañero nuevo quiere enseñar a otro a manejar la etiquetadora porque «es fácil». ¿Qué corresponde?", "Solo personas autorizadas y capacitadas por el responsable manejan los equipos", "Está bien si no hay riesgo aparente", "Está bien si lo supervisa quien lleva un mes en la planta", "La capacitación y la autorización las da la planta; la facilidad aparente no las reemplaza."),
    ],
    ctx=("abc", "{F} El jefe de producción pide seguir operando una máquina con una guarda dañada para cumplir un pedido. ¿Qué respuesta corresponde?", "Detener y reportar, porque la seguridad de las personas va antes del pedido", "Seguir hasta terminar el pedido y reparar después", "Reparar la guarda con cinta adhesiva y continuar", "Una guarda dañada deja expuesta una parte peligrosa y no se opera así."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cuál es la diferencia entre un equipo y un instrumento?", "El equipo transforma o mueve el producto y el instrumento mide", "Cumplen funciones distintas dentro de la línea."),
        ("¿Quién ajusta y repara un equipo?", "El personal de mantención autorizado", "Hacerlo sin autorización arriesga accidentes y daños al equipo."),
        ("¿Se pueden retirar las guardas de seguridad?", "No, nunca se retiran ni se inhabilitan", "Protegen contra el contacto con partes peligrosas."),
    ],
    op=("Una línea de ejemplo produce 100 envases por hora. Un turno ocurre así: (1) la cinta hace un ruido anormal, (2) un operario quiere retirar una guarda para sacar un envase atascado, (3) la selladora se detiene 4 horas por una falla. "
        "Escribe: (a) qué debe hacer el operario en cada situación, (b) cuántos envases se dejan de producir en la situación 3 y (c) por qué solo personal autorizado interviene los equipos.",
        "(a) 1: detener según el procedimiento y avisar al supervisor y a mantención. 2: no retirar la guarda ni meter la mano; detener y avisar a personal autorizado. 3: avisar y esperar a mantención. (b) 4 × 100 = 400 envases. (c) Porque las máquinas tienen partes móviles y energía que pueden causar accidentes si se interviene sin capacitación ni bloqueo.",
        ["indica la acción correcta en cada situación", "calcula 400 envases", "justifica la intervención solo de personal autorizado"],
        ["hoja con las tres respuestas"],
        ["retirar la guarda para sacar el envase", "seguir operando con el ruido", "olvidar multiplicar por las horas"],
        "Pregunta: «¿qué podría pasar si se mete la mano a una cinta en marcha?». Debe decir que puede atraparla."),
    reinforce="Escribe cinco reglas de seguridad para máquinas de una planta inventada y explica el riesgo que previene cada una.",
    extend="Explica con un ejemplo inventado por qué ante un ruido anormal se detiene el equipo y no se espera al fin del turno.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 6 (hoja de vida de una balanza de ejemplo, inventada). Código B-03, ubicada en el muelle de recepción. Calibración cada 6 meses por personal autorizado; mantención preventiva cada 3 meses. "
     "Verificación diaria con un peso patrón de 1.000 g; tolerancia de ±2 g. Lecturas de hoy con el patrón: 1.001 g, 999 g, 1.000 g y 1.003 g. "
     "La bitácora es el registro cronológico del equipo y la orden de trabajo es la solicitud escrita a mantención.")
build(
    O5, 2, F,
    use="Aprenderé el vocabulario de los equipos e instrumentos: calibración, verificación, patrón, tolerancia, mantención preventiva y correctiva, hoja de vida, bitácora y orden de trabajo.",
    prior=["Conozco equipos, instrumentos y reglas de seguridad.", "Sé restar enteros.", "Sé comparar un dato con un rango."],
    explain=[
        "Un instrumento de medición, como una balanza, debe medir bien. Un peso patrón es una referencia de valor conocido con el que se compara. La verificación es comprobar con el patrón que el instrumento sigue dentro de la tolerancia (el error máximo permitido, por ejemplo ±2 g). La calibración es una comparación y ajuste más completos, que hace personal autorizado cada cierto tiempo.",
        "El error de una lectura es la diferencia entre lo que marca el instrumento y el valor del patrón. Si el error supera la tolerancia, el instrumento queda fuera de uso hasta que mantención lo revise, y se revisan los pesajes hechos desde la última verificación buena.",
        "La mantención preventiva se programa aunque el equipo funcione, para evitar fallas. La mantención correctiva repara después de que ocurre una falla. Cada equipo tiene una hoja de vida con sus datos y una bitácora donde se anota cada evento. Se pide trabajo a mantención con una orden de trabajo escrita." + LIMX,
    ],
    vocab=[("peso patrón", "referencia de valor conocido para comparar"), ("tolerancia", "error máximo permitido"), ("verificación", "comprobación con un patrón de que el instrumento mide dentro de la tolerancia"), ("calibración", "comparación y ajuste del instrumento por personal autorizado"), ("mantención preventiva", "revisión programada para evitar fallas"), ("mantención correctiva", "reparación después de una falla"), ("bitácora", "registro cronológico de un equipo"), ("orden de trabajo", "solicitud escrita a mantención")],
    worked=[
        ("Calcular un error", "Un peso patrón de 500 g se pesa en una balanza de ejemplo y marca 502 g. ¿Cuál es el error?", ["El error es la lectura menos el valor del patrón.", "502 − 500 = 2."], "2 g"),
        ("Comparar con la tolerancia", "La tolerancia de un instrumento de ejemplo es de ±3 g y el error medido es de 4 g. ¿Está dentro de la tolerancia?", ["Se compara el error con el máximo permitido.", "4 g supera los 3 g."], "No: queda fuera de la tolerancia"),
    ],
    mistakes=[("Seguir usando una balanza cuya lectura está fuera de tolerancia y «restar el error de memoria».", "Se acumulan errores y no hay respaldo de los pesajes.", "Deja el instrumento fuera de uso, registra y pide revisión."),
              ("Cambiar en el registro la lectura de 1.003 g por 1.002 g para que cumpla.", "Se altera un dato real y se oculta un problema del instrumento.", "Anota la lectura medida y avisa.")],
    T=[
        ("abc", "{F} ¿Cada cuánto se calibra la balanza?", "Cada 6 meses", "Cada 3 meses", "Todos los días", "La ficha fija la calibración cada 6 meses; cada 3 meses es la mantención preventiva."),
        ("abc", "{F} ¿Cuál es el valor del peso patrón?", "1.000 g", "1.003 g", "2 g", "El patrón de la ficha es de 1.000 g; 2 g es la tolerancia."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es calibrar un instrumento?", "Compararlo con un patrón y ajustarlo, tarea de personal autorizado", "Limpiarlo con un paño al terminar el turno", "Cambiarlo por uno nuevo cada año", "La calibración es una comparación y ajuste completos con un patrón."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es la verificación diaria con un peso patrón?", "Comprobar que el instrumento sigue midiendo dentro de la tolerancia", "Ajustar la balanza por cuenta propia", "Cambiar el peso del patrón", "Verificar es comprobar con el patrón; no es ajustar."),
        ("=", "{F} ¿Cuántos gramos se desvió la lectura de 1.003 g respecto del patrón?", "1003-1000", "El error es la lectura menos el valor del patrón.", " g"),
        ("abc", "{F} ¿La lectura de 1.003 g está dentro de la tolerancia de ±2 g?", "No, porque el error de 3 g supera los 2 g permitidos", "Sí, porque está cerca del patrón", "Sí, porque 3 g es poco", "La tolerancia máxima es 2 g y el error fue 3 g."),
        ("abc", "{F} ¿Cuántas de las cuatro lecturas de hoy están fuera de la tolerancia?", "Una, la de 1.003 g", "Dos, las de 999 g y 1.003 g", "Ninguna", "Los errores de 1 g, −1 g y 0 g están dentro de ±2 g; solo 3 g queda fuera."),
        ("abc", "Revisar la balanza cada 3 meses aunque funcione bien es una mantención...", "Preventiva", "Correctiva", "De emergencia", "Se programa para evitar fallas, lo que define la mantención preventiva."),
        ("abc", "Reparar la balanza después de que dejó de funcionar es una mantención...", "Correctiva", "Preventiva", "De calibración", "Se actúa después de la falla, lo que es la mantención correctiva."),
        ("abc", "{F} Se detecta una lectura fuera de tolerancia. ¿Qué corresponde con los pesajes hechos desde la última verificación buena?", "Revisarlos y registrar cuáles pudieron verse afectados, avisando a calidad", "Nada, porque los pesajes ya pasaron", "Repetir la verificación hasta obtener una lectura buena", "Los pesajes hechos con un instrumento dudoso pueden estar errados y deben revisarse."),
        ("abc", "¿Por qué se usa un peso patrón y no cualquier peso conocido «más o menos»?", "Porque el patrón tiene un valor de referencia confiable con el que comparar", "Porque el patrón pesa más", "Porque con cualquier peso la verificación sale igual", "Sin una referencia confiable, el error medido no tiene sentido."),
        ("=", "El patrón de otra balanza de ejemplo es de 500 g y la tolerancia es de ±2 g. La lectura de hoy es 504 g. ¿Cuántos gramos excede el límite superior?", "504-(500+2)", "Se resta el límite superior permitido a la lectura.", " g"),
        ("abc", "{F} Si la lectura del día es 1.003 g, ¿qué corresponde hacer?", "Registrar la desviación, dejar la balanza fuera de uso y pedir revisión con una orden de trabajo", "Seguir usándola y restar 3 g mentalmente en cada pesaje", "Cambiar la lectura del registro a 1.002 g", "Un instrumento fuera de tolerancia no se usa y se pide su revisión por escrito."),
    ],
    ctx=("abc", "{F} Un jefe pregunta cómo se sabrá cuándo se hizo la última mantención de la balanza B-03. ¿Dónde se busca el dato?", "En la hoja de vida y la bitácora del equipo", "En la factura de la balanza", "En la lista de precios del proveedor", "La hoja de vida y la bitácora registran las intervenciones y los eventos del equipo."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cuál es la diferencia entre verificar y calibrar?", "Verificar comprueba con un patrón; calibrar compara y ajusta por personal autorizado", "La calibración es más completa y se hace menos seguido."),
        ("En la industria de alimentos: ¿qué es la tolerancia?", "El error máximo permitido", "Fija hasta cuánto puede desviarse una medición."),
        ("¿Qué se usa para pedir trabajo a mantención?", "Una orden de trabajo escrita", "Deja constancia de qué se pidió y quién lo pidió."),
    ],
    op=("Hoja de vida de una balanza de ejemplo: patrón de 200 g, tolerancia de ±1 g, calibración cada 6 meses y mantención preventiva cada 3 meses. Lecturas de hoy: 200 g, 201 g, 199 g y 203 g. "
        "Escribe: (a) el error de cada lectura, (b) cuántas lecturas están fuera de tolerancia, (c) qué harías con la balanza y con los pesajes anteriores, y (d) qué documento usarías para pedir la revisión.",
        "(a) Errores: 0 g, 1 g, −1 g y 3 g. (b) Una, la de 203 g. (c) Dejar la balanza fuera de uso, registrar la desviación y revisar los pesajes hechos desde la última verificación buena. (d) Una orden de trabajo escrita a mantención.",
        ["calcula los cuatro errores", "identifica la lectura fuera de tolerancia", "propone acciones y nombra la orden de trabajo"],
        ["hoja con las cuatro respuestas"],
        ["contar dos lecturas fuera de rango", "seguir usando la balanza", "alterar la lectura"],
        "Pregunta: «¿qué pasa con los pesajes anteriores si la balanza estaba descalibrada?». Debe decir que podrían estar errados y se revisan."),
    reinforce="Inventa un patrón, una tolerancia y cuatro lecturas, y calcula el error de cada una.",
    extend="Explica con un ejemplo inventado por qué un instrumento fuera de tolerancia afecta el pago a un proveedor o el peso de un envase.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 7 (bitácora de una selladora de ejemplo, inventada). Capacidad diaria: 1.200 envases. Lunes: operación normal, 1.200 envases. Martes: se reporta un ruido anormal; mantención revisa y no encuentra hallazgos; 1.150 envases. "
     "Miércoles: 40 envases con sellado defectuoso; mantención cambia una pieza y el equipo se detiene 2 horas; 900 envases. Jueves: sin novedades; 1.200 envases. Viernes: se reporta de nuevo un ruido anormal; 1.100 envases. "
     "Mantención preventiva programada para el sábado.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso en papel: leer una bitácora de un equipo, calcular producción y pérdidas, ubicar patrones repetidos y decidir qué avisar.",
    prior=["Conozco la bitácora y la mantención preventiva y correctiva.", "Sé sumar y restar enteros.", "Sé calcular porcentajes sencillos."],
    explain=[
        "La bitácora anota cronológicamente los eventos de un equipo: fecha, qué ocurrió, quién lo reportó, qué se hizo y quién respondió. Leerla permite ver patrones, es decir, eventos que se repiten, como un ruido anormal que reaparece. Un patrón puede mostrar que la causa no se resolvió.",
        "Se comparan la producción y la capacidad para calcular la pérdida de cada día. Con ella se estima el costo de las fallas y se justifica una intervención. También se registra una revisión sin hallazgos, porque es información: indica qué se revisó y qué no se encontró.",
        "Quien opera el equipo no abre ni repara por su cuenta: reporta y espera a personal autorizado de mantención. Una intervención se programa o se adelanta según el riesgo, y la decisión la toma el responsable con mantención." + LIMX,
    ],
    vocab=[("patrón de eventos", "eventos que se repiten y sugieren una causa común"), ("hallazgo", "problema encontrado en una revisión"), ("capacidad diaria", "cantidad máxima que el equipo puede producir en un día"), ("pérdida de producción", "diferencia entre la capacidad y lo producido"), ("reportar", "avisar un evento a quien corresponde")],
    worked=[
        ("Calcular una pérdida", "Un equipo de ejemplo tiene capacidad de 1.000 envases por día y un día produjo 850. ¿Cuál fue la pérdida?", ["La pérdida es la capacidad menos lo producido.", "1.000 − 850 = 150."], "150 envases"),
        ("Ver un patrón", "En la bitácora de ejemplo aparece «vibración» el lunes, el miércoles y el viernes. ¿Qué indica?", ["El evento se repite.", "La causa podría no estar resuelta."], "Un patrón que conviene revisar"),
    ],
    mistakes=[("No anotar un ruido porque «ya se anotó el martes».", "La repetición es información clave para ver un patrón.", "Anota cada evento con su fecha."),
              ("Borrar una anotación porque «no se encontró nada».", "Una revisión sin hallazgos también es información.", "Conserva el registro, con lo que se revisó y el resultado.")],
    T=[
        ("=", "{F} ¿Cuántos envases se produjeron en la semana?", "1200+1150+900+1200+1100", "Se suman los envases producidos cada día.", " envases"),
        ("=", "{F} ¿Cuál es la capacidad de la selladora en los 5 días?", "1200*5", "Se multiplica la capacidad diaria por los días.", " envases"),
        ("=", "{F} ¿Cuántos envases se dejaron de producir en la semana respecto de la capacidad?", "1200*5-(1200+1150+900+1200+1100)", "A la capacidad semanal se le resta lo producido.", " envases"),
        ("abc", "{F} ¿En qué día hubo la mayor pérdida de producción?", "El miércoles", "El martes", "El viernes", "El miércoles produjo 900 de 1.200, la mayor diferencia de la semana."),
        ("=", "{F} ¿Cuántos envases se perdieron el miércoles respecto de la capacidad?", "1200-900", "A la capacidad diaria se le resta lo producido.", " envases"),
        ("abc", "{F} ¿Qué evento se repite en la bitácora?", "El ruido anormal, el martes y el viernes", "El cambio de pieza, el miércoles y el viernes", "La detención de 2 horas, el martes y el jueves", "Solo el ruido anormal aparece dos veces, los días martes y viernes."),
        ("abc", "{F} ¿Qué puede indicar que el ruido reaparezca el viernes?", "Que la causa pudo no resolverse y conviene revisarla a fondo", "Que el ruido no era un problema real", "Que el operador del viernes se equivocó", "Un evento repetido sugiere una causa pendiente, que debe investigarse."),
        ("=", "{F} ¿Qué porcentaje de la capacidad diaria alcanzó la producción del miércoles?", "900*100//1200", "Se divide lo producido por la capacidad y se multiplica por 100.", " %"),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué debe incluir cada anotación de una bitácora?", "Fecha, evento, quién lo reportó, la acción realizada y su responsable", "Solo el nombre del equipo", "Solo el precio de la reparación", "La bitácora debe permitir reconstruir qué pasó, quién actuó y cuándo."),
        ("abc", "{F} El operador del viernes no quiere anotar el ruido porque «ya se vio el martes». ¿Qué respuesta corresponde?", "Debe anotarse: la repetición es información clave para mantención", "Tiene razón, porque ya se revisó", "Basta con avisarlo de palabra", "Sin anotación no se puede ver el patrón ni respaldar la decisión."),
        ("abc", "{F} Con estos datos, ¿qué acción es más razonable?", "Pedir a mantención una revisión de la causa del ruido sin esperar al sábado, si el riesgo lo justifica", "Esperar al sábado sin avisar", "Seguir operando hasta que el equipo se detenga solo", "Un patrón de ruido merece revisión; la decisión la toma el responsable con mantención."),
        ("=", "{F} Si la mantención del sábado evita la pérdida de 300 envases por semana y cada envase deja un margen de ejemplo de $150, ¿cuántos pesos se ahorrarían en 4 semanas?", "300*150*4", "Se multiplican los envases, el margen y las semanas.", " pesos"),
        ("=", "{F} Del total producido el miércoles, 40 envases tuvieron sellado defectuoso. ¿Cuántos envases buenos hubo ese día?", "900-40", "Al total producido se le restan los defectuosos.", " envases"),
    ],
    ctx=("abc", "{F} Un compañero propone borrar la anotación del martes «porque no se encontró nada». ¿Qué respuesta corresponde?", "No se borra: una revisión sin hallazgos también es información", "Se borra para que la bitácora quede más corta", "Se borra si el supervisor lo pide de palabra", "Conservar la revisión permite saber qué se hizo y no repetir lo ya revisado."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué es la bitácora de un equipo?", "El registro cronológico de sus eventos", "Permite reconstruir lo ocurrido con cada equipo."),
        ("¿Qué indica un evento que se repite en la bitácora?", "Un patrón que conviene investigar", "La causa puede no haberse resuelto."),
        ("¿Qué hace quien opera el equipo ante una falla?", "Reporta y espera a personal autorizado", "No debe intervenir por su cuenta."),
    ],
    op=("Bitácora de ejemplo de una cinta transportadora, con capacidad de 1.000 envases por día. Lunes: 1.000. Martes: 950, se reporta vibración. Miércoles: 700, falla de un rodamiento; mantención repara y el equipo se detiene 3 horas. Jueves: 1.000. Viernes: 920, se reporta de nuevo vibración. "
        "Escribe: (a) la producción total y la pérdida de la semana, (b) el día de mayor pérdida y cuánta fue, (c) qué patrón observas y (d) qué harías.",
        "(a) La producción es 4.570 envases y la pérdida es 5.000 − 4.570 = 430 envases. (b) El miércoles, con 300 envases. (c) La vibración se repite el martes y el viernes, lo que sugiere una causa pendiente. (d) Reportar y pedir a mantención una revisión de la causa de la vibración, anotando todo en la bitácora.",
        ["calcula 4.570 y 430", "identifica el miércoles y 300", "describe el patrón y propone una acción"],
        ["hoja con las cuatro respuestas"],
        ["olvidar un día en la suma", "no ver el patrón de la vibración", "proponer reparar sin mantención"],
        "Pregunta: «¿qué día hubo evento y pérdida a la vez?». Debe decir el miércoles."),
    reinforce="Inventa una bitácora de tres días para un equipo y escribe el patrón que se observa.",
    extend="Explica con un ejemplo inventado cómo una bitácora bien llevada ayuda a decidir cuándo adelantar una mantención.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 8 (disponibilidad de un equipo de ejemplo, inventada). Tiempo programado: 8 horas por día durante 5 días. Detenciones por falla: lunes 1 hora, miércoles 2 horas y viernes 1 hora. Producción de ejemplo: 150 envases por hora de operación. "
     "Costo de ejemplo de una hora de detención: $50.000. Meta de ejemplo de disponibilidad: 92 %. La disponibilidad es el tiempo en operación dividido por el tiempo programado, expresado en porcentaje. "
     "Un repuesto debe cumplir las especificaciones del fabricante del equipo y ser autorizado por mantención.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular el tiempo programado, las detenciones y la disponibilidad de un equipo, y estimar la producción y el costo de las detenciones.",
    prior=["Conozco la bitácora de un equipo.", "Sé calcular porcentajes con enteros.", "Sé multiplicar y restar enteros."],
    explain=[
        "La disponibilidad de un equipo es la parte del tiempo programado en que está en operación. Se calcula restando las horas de detención al tiempo programado y dividiendo el resultado por el tiempo programado; se expresa en porcentaje. Sirve para comparar equipos y para ver si se cumple una meta.",
        "Las detenciones tienen un costo: la producción que se deja de obtener y el costo de la hora detenida. Con la producción por hora se calcula cuántos envases se pierden; con el costo por hora se estima el costo de las detenciones. Una mantención preventiva bien hecha reduce las detenciones por falla.",
        "Todas las detenciones se registran, también las cortas, porque sin ese registro no se pueden analizar las causas. Un repuesto debe cumplir las especificaciones del fabricante y estar autorizado por mantención; el más barato no es mejor si no cumple." + LIMX,
    ],
    vocab=[("disponibilidad", "parte del tiempo programado en que el equipo opera, en porcentaje"), ("tiempo programado", "horas que el equipo debería operar"), ("detención por falla", "tiempo que el equipo está parado por un problema"), ("repuesto", "pieza que reemplaza a otra en una reparación"), ("indicador", "dato calculado que resume cómo va un proceso")],
    worked=[
        ("Calcular la disponibilidad", "Un equipo de ejemplo tiene 40 horas programadas y 4 de detención. ¿Cuál es la disponibilidad?", ["Horas en operación: 40 − 4 = 36.", "36 × 100 ÷ 40 = 90."], "90 %"),
        ("Producción perdida", "Un equipo de ejemplo produce 100 envases por hora y se detiene 3 horas. ¿Cuántos envases se pierden?", ["Se multiplica la producción por hora por las horas detenidas.", "100 × 3 = 300."], "300 envases"),
    ],
    mistakes=[("No registrar las detenciones cortas «porque son poca cosa».", "Se pierde información para ver las causas y la disponibilidad parece mejor de lo que es.", "Registra todas las detenciones con su duración y causa."),
              ("Comprar el repuesto más barato sin revisar que cumpla las especificaciones.", "Un repuesto inadecuado puede causar nuevas fallas o riesgos.", "Usa repuestos que cumplan las especificaciones y estén autorizados por mantención.")],
    T=[
        ("=", "{F} ¿Cuántas horas programadas hay en los 5 días?", "8*5", "Se multiplican las horas por día por los días.", " horas"),
        ("=", "{F} ¿Cuántas horas de detención hubo en la semana?", "1+2+1", "Se suman las horas de detención de cada día.", " horas"),
        ("=", "{F} ¿Cuántas horas estuvo el equipo en operación?", "8*5-(1+2+1)", "Al tiempo programado se le restan las horas de detención.", " horas"),
        ("=", "{F} ¿Cuál fue la disponibilidad del equipo, en porcentaje?", "(8*5-(1+2+1))*100//(8*5)", "Se divide el tiempo en operación por el tiempo programado y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Cumple el equipo la meta de disponibilidad?", "No, porque llega a 90 % y la meta es 92 %", "Sí, porque 90 % es un valor alto", "Sí, porque hubo solo tres días con detenciones", "La disponibilidad calculada es menor que la meta."),
        ("=", "{F} ¿Cuántos envases se dejaron de producir por las detenciones?", "(1+2+1)*150", "Se multiplican las horas de detención por la producción por hora.", " envases"),
        ("=", "{F} ¿Cuántos pesos costaron las detenciones de la semana?", "(1+2+1)*50000", "Se multiplican las horas de detención por el costo por hora.", " pesos"),
        ("abc", "{F} ¿En qué día hubo más horas de detención?", "El miércoles, con 2 horas", "El lunes, con 1 hora", "El viernes, con 2 horas", "El miércoles tuvo la mayor detención, de 2 horas."),
        ("=", "Otro equipo de ejemplo tuvo 40 horas programadas y 2 horas de detención. ¿Cuál fue su disponibilidad, en porcentaje?", "(40-2)*100//40", "Se resta la detención al tiempo programado y se calcula el porcentaje.", " %"),
        ("abc", "El equipo A tuvo 90 % de disponibilidad y el equipo B, 95 %. Un jefe concluye que B es siempre mejor. ¿Qué observación es correcta?", "La disponibilidad es solo un indicador; falta ver las causas de las detenciones y la producción", "Tiene razón, porque un porcentaje mayor siempre es mejor", "No se pueden comparar equipos distintos nunca", "Un indicador no explica por sí mismo las causas ni la calidad de lo producido."),
        ("abc", "Para subir la disponibilidad, un jefe propone no registrar las detenciones cortas. ¿Qué problema hay?", "Se oculta información real y ya no se pueden analizar las causas", "Ninguno, porque lo corto no cuenta", "El registro disminuiría el costo de las detenciones", "Dejar de registrar mejora el número sin mejorar el equipo."),
        ("=", "{F} Si la mantención preventiva reduce las detenciones de la semana de 4 horas a 2 horas, ¿cuántos pesos se ahorrarían en costo de detención?", "(4-2)*50000", "Se multiplican las horas ahorradas por el costo por hora.", " pesos"),
        ("abc", "{F} Un proveedor ofrece un repuesto muy barato que no indica si cumple las especificaciones del fabricante. ¿Qué criterio corresponde?", "No usarlo hasta que mantención confirme que cumple las especificaciones", "Usarlo porque es el más barato", "Usarlo en los equipos menos importantes", "El repuesto debe cumplir las especificaciones y ser autorizado por mantención."),
    ],
    ctx=("abc", "{F} El jefe quiere alcanzar la meta de 92 % y pregunta cuántas horas de detención como máximo podría tener el equipo en 40 horas programadas. ¿Qué respuesta es correcta?", "Hasta 3 horas, porque con 37 horas de operación se supera el 92 %", "Hasta 5 horas, porque 35 horas es un 87 %", "Hasta 1 hora, porque la meta exige 100 %", "Con 3 horas de detención, la disponibilidad sería 37 × 100 ÷ 40 = 92,5 %, que cumple la meta."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cómo se calcula la disponibilidad de un equipo?", "Tiempo en operación por 100, dividido por el tiempo programado", "Relaciona el tiempo que funcionó con el que debía funcionar."),
        ("¿Qué costo tienen las detenciones?", "La producción perdida y el costo de cada hora detenida", "Ambos dejan de ganarse o se gastan igual."),
        ("¿Se registran las detenciones cortas?", "Sí, todas se registran", "Sin ellas no se pueden analizar las causas."),
    ],
    op=("Datos de ejemplo de un equipo: 8 horas programadas por día durante 5 días; detenciones de 2 horas el martes y 2 horas el jueves; producción de 200 envases por hora; costo de una hora detenida de $40.000; meta de disponibilidad de al menos 88 %. "
        "Escribe: (a) las horas en operación, (b) la disponibilidad, (c) si cumple la meta, (d) los envases perdidos y (e) el costo de las detenciones.",
        "(a) 40 − 4 = 36 horas. (b) 36 × 100 ÷ 40 = 90 %. (c) Cumple la meta de al menos 88 %. (d) 4 × 200 = 800 envases. (e) 4 × 40.000 = 160.000 pesos.",
        ["calcula las 36 horas", "calcula la disponibilidad y compara con la meta", "calcula los envases y el costo"],
        ["hoja con las cinco respuestas"],
        ["olvidar restar las detenciones", "no comparar con la meta", "multiplicar por 40 horas en lugar de por las detenidas"],
        "Pregunta: «¿cuánto costaría una hora más de detención?». Debe responder 40.000 pesos y 200 envases."),
    reinforce="Inventa un equipo con horas programadas y detenciones, y calcula su disponibilidad.",
    extend="Explica con un ejemplo inventado cómo una mantención preventiva puede costar menos que una falla.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 9 (sistema de calidad de una planta de ejemplo, inventada). Documentos: un Manual de BPM (reglas generales de higiene, instalaciones y personal); el POE-05 sobre la recepción de materias primas (define cómo se hace esa tarea de forma uniforme y quién la hace); "
     "el POES-02 sobre el saneamiento de la zona de envasado; y el Plan HACCP del producto Q (análisis de los peligros del producto y de sus puntos críticos de control). Los registros demuestran que se cumplió lo escrito. "
     "El jefe de calidad es responsable del sistema; los operarios cumplen los procedimientos y llenan los registros. La norma vigente exige estas herramientas según el tipo de establecimiento.")
build(
    O6, 1, F,
    use="Aprenderé a situar el control de las variables de proceso en una planta: qué significan BPM, POE, POES y HACCP, para qué sirven y qué rol cumplen los registros.",
    prior=["Conozco el flujo de una planta de alimentos.", "Conozco los peligros biológico, químico y físico.", "Sé leer una ficha con documentos."],
    explain=[
        "Las BPM (Buenas Prácticas de Manufactura) son las reglas generales de higiene, instalaciones, personal y orden que previenen la contaminación en toda la planta. Los POE (Procedimientos Operativos Estandarizados) son documentos que definen cómo se hace una tarea de forma uniforme y quién la hace. Los POES (Procedimientos Operativos Estandarizados de Saneamiento) hacen lo mismo con las tareas de limpieza y saneamiento.",
        "El HACCP (Análisis de Peligros y Puntos Críticos de Control) es un sistema que identifica los peligros significativos de un producto y define los puntos críticos de control donde se pueden prevenir. Las BPM son la base y el HACCP se apoya en ellas, pero no las reemplaza. Los registros son la prueba escrita de que se cumplió lo escrito y se llenan en el momento de la tarea.",
        "La norma vigente exige estas herramientas según el tipo de establecimiento. Este cuaderno solo estudia sus conceptos y registros. Los contenidos concretos de cada procedimiento los define el docente de la especialidad y la autoridad sanitaria." + LIM,
    ],
    vocab=[("BPM", "Buenas Prácticas de Manufactura: reglas generales que previenen la contaminación"), ("POE", "Procedimiento Operativo Estandarizado: define cómo se hace una tarea"), ("POES", "Procedimiento Operativo Estandarizado de Saneamiento"), ("HACCP", "Análisis de Peligros y Puntos Críticos de Control"), ("registro", "prueba escrita de que se cumplió lo escrito"), ("auditoría", "revisión planificada del cumplimiento de un sistema")],
    worked=[
        ("Reconocer un documento", "Un documento de una planta de ejemplo describe cómo se limpia y sanea una sala y quién lo hace. ¿Es un POE o un POES?", ["Trata de limpieza y saneamiento.", "Eso corresponde a un POES."], "Un POES"),
        ("Ver la relación", "¿Las BPM reemplazan al HACCP o lo apoyan?", ["Las BPM son la base de higiene y orden de toda la planta.", "El HACCP se apoya en ellas."], "Lo apoyan: son su base"),
    ],
    mistakes=[("Pensar que HACCP reemplaza a las BPM.", "El HACCP se concentra en peligros significativos y se apoya en las BPM como base.", "Aplica ambas: las BPM en toda la planta y el HACCP en los puntos críticos."),
              ("Dejar un registro «para después».", "Sin registro oportuno no hay prueba de que se cumplió lo escrito.", "Llena el registro en el momento de la tarea.")],
    T=[
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué significa BPM?", "Buenas Prácticas de Manufactura", "Buenos Procesos de Mantención", "Base de Procedimientos Mínimos", "BPM son las reglas generales que previenen la contaminación en la planta."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué significa POES?", "Procedimientos Operativos Estandarizados de Saneamiento", "Programas de Operación y Elaboración Sanitaria", "Pautas de Orden y Equipamiento Seguro", "El POES define las tareas de saneamiento de forma estandarizada."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué significa HACCP?", "Análisis de Peligros y Puntos Críticos de Control", "Análisis Higiénico de Control de Productos", "Auditoría de Higiene y Control de Calidad del Producto", "El nombre del sistema resume su función: analizar peligros y controlar puntos críticos."),
        ("abc", "{F} ¿Qué documento de la ficha trata del saneamiento de la zona de envasado?", "El POES-02", "El POE-05", "El Plan HACCP", "El POES es el procedimiento de saneamiento; el POE-05 trata de la recepción."),
        ("abc", "{F} ¿Qué documento reúne las reglas generales de higiene, instalaciones y personal?", "El Manual de BPM", "El POE-05", "El Plan HACCP", "El manual de BPM reúne las reglas generales de toda la planta."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es un POE?", "Un documento que define cómo se hace una tarea de forma uniforme y quién la hace", "Un registro de las ventas de la planta", "Un producto de limpieza", "El POE estandariza la forma de hacer una tarea."),
        ("abc", "{F} ¿Para qué sirven las BPM?", "Para establecer condiciones básicas de higiene y trabajo que previenen la contaminación", "Para calcular el costo de los lotes", "Para fijar el precio de los productos", "Las BPM son la base de higiene y orden de la planta."),
        ("abc", "{F} ¿Qué relación hay entre las BPM y el HACCP?", "Las BPM son la base y el HACCP se concentra en los peligros significativos del producto", "El HACCP reemplaza a las BPM", "Son lo mismo con distinto nombre", "El HACCP se apoya en las BPM, que cubren toda la planta."),
        ("=", "{F} Además de los 4 documentos de la ficha, la planta tiene 6 POE y 3 POES más. Cada documento debe revisarse una vez al año y ya se revisaron 5. ¿Cuántos faltan por revisar?", "4+6+3-5", "Se suman todos los documentos y se restan los ya revisados.", " documentos"),
        ("abc", "{F} Un operario sigue un método propio más rápido que el POE-05. ¿Qué respuesta corresponde?", "Sigue el POE y, si cree que puede mejorarse, lo propone para que se revise y se actualice", "Sigue su método, porque es más rápido", "Sigue su método si el supervisor no está", "El POE asegura una forma uniforme de trabajar y se cambia por una decisión formal."),
        ("abc", "{F} ¿Por qué los registros son parte del sistema y no un trámite?", "Porque demuestran que se cumplió lo escrito y permiten revisar si algo falló", "Porque se piden para cobrar a los clientes", "Porque reemplazan a los procedimientos", "Sin registros no hay forma de comprobar lo que se hizo."),
        ("=", "Un auditor de ejemplo revisa 20 registros y encuentra 3 incompletos. ¿Qué porcentaje de los registros está completo?", "(20-3)*100//20", "Se restan los incompletos del total y se calcula el porcentaje.", " %"),
        ("abc", "Un registro de limpieza de ejemplo dice «hecho» pero no tiene hora ni firma. ¿Cómo se clasifica?", "Como un registro incompleto, porque no demuestra quién lo hizo ni cuándo", "Como un registro correcto, porque dice «hecho»", "Como un registro válido si es de un día de poco trabajo", "Sin hora ni firma el registro no cumple su función de prueba."),
    ],
    ctx=("abc", "{F} Un cliente pregunta por qué la planta tiene tantos documentos y registros. ¿Qué respuesta es adecuada?", "Porque permiten hacer las tareas de forma uniforme y demostrar con registros que se cumplió lo escrito", "Porque así se evita capacitar al personal en cada tarea", "Porque los documentos reemplazan la supervisión del jefe de calidad", "Los documentos estandarizan el trabajo y los registros lo respaldan."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué diferencia hay entre POE y POES?", "El POE estandariza una tarea y el POES estandariza tareas de saneamiento", "Ambos son procedimientos, pero el POES se ocupa del saneamiento."),
        ("¿Las BPM reemplazan al HACCP?", "No, son su base", "El HACCP se apoya en las BPM de toda la planta."),
        ("¿Cuándo se llena un registro?", "En el momento de la tarea", "Así demuestra que se hizo y cuándo."),
    ],
    op=("Una planta de ejemplo tiene estos documentos: Manual de BPM, POE-12 de recepción de envases, POES-04 de saneamiento de baños y Plan HACCP del producto S. "
        "Escribe: (a) para cada documento, qué tipo es y de qué trata, (b) cómo se relacionan las BPM con el HACCP y (c) por qué un operario debe llenar el registro en el momento de la tarea.",
        "(a) Manual de BPM: reglas generales de higiene, instalaciones y personal. POE-12: procedimiento estandarizado para recibir envases. POES-04: procedimiento de saneamiento de baños. Plan HACCP: peligros y puntos críticos de control del producto S. (b) Las BPM son la base y el HACCP se apoya en ellas para controlar los peligros significativos. (c) Porque el registro oportuno demuestra que se cumplió y cuándo.",
        ["clasifica los cuatro documentos", "explica la relación BPM-HACCP", "justifica el registro oportuno"],
        ["hoja con las tres respuestas"],
        ["decir que el HACCP reemplaza a las BPM", "confundir POE y POES", "dejar el registro para el final del turno"],
        "Pregunta: «¿qué pasaría sin registros?». Debe decir que no habría prueba de lo que se hizo."),
    reinforce="Escribe una tabla con los cuatro documentos de la ficha y, para cada uno, su función en una frase.",
    extend="Explica con un ejemplo inventado por qué un procedimiento estandarizado ayuda a que dos personas hagan la misma tarea de la misma forma.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 10 (hoja de control de ejemplo, inventada). Etapa: tratamiento de conservación (PCC-1). Peligro que controla: microbios que podrían sobrevivir (biológico). Variable de proceso: nivel de tratamiento, medido en unidades de ejemplo (u.e.), una escala inventada que no corresponde a ninguna magnitud real. "
     "Límite crítico: mínimo 50 u.e. Monitoreo: en cada lote, a cargo de un operador autorizado. Acción correctiva si hay desviación: retener el lote y avisar al jefe de calidad. Verificación: el jefe de calidad revisa todos los registros cada día. "
     "Otro control de BPM: almacenamiento refrigerado con una temperatura máxima de 5 °C de ejemplo, medida en cada turno.")
build(
    O6, 2, F,
    use="Aprenderé el vocabulario del control de variables: variable de proceso, límite crítico, punto crítico de control, monitoreo, desviación, acción correctiva y verificación.",
    prior=["Conozco BPM, POE, POES y HACCP.", "Sé comparar un dato con un límite.", "Sé sumar y restar enteros."],
    explain=[
        "Una variable de proceso es una magnitud que se mide en una etapa, como una temperatura, un tiempo, un peso o un pH. Un límite crítico es el valor que separa lo aceptable de lo inaceptable en un punto crítico de control (PCC), que es la etapa donde se puede controlar un peligro significativo para evitarlo o reducirlo a un nivel aceptable. Los valores de este cuaderno son de ejemplo, en unidades inventadas, y no reemplazan los de la norma vigente.",
        "El monitoreo es la medición u observación planificada para comprobar que la variable cumple su límite; define qué se mide, cada cuánto y quién lo hace. Si el valor no cumple, hay una desviación y se aplica la acción correctiva definida: retener el lote y avisar. La verificación es una revisión posterior, por ejemplo de los registros, para comprobar que el sistema funciona.",
        "Un valor se anota como se midió. No se repite la medición hasta obtener un valor bueno ni se cambia un número para que cumpla. Un alérgeno es una sustancia que puede provocar una reacción alérgica en personas sensibles: solo se estudia como concepto y rotulado, y ante una reacción de una persona se avisa a un adulto responsable y a emergencias." + LIM,
    ],
    vocab=[("variable de proceso", "magnitud que se mide en una etapa"), ("punto crítico de control (PCC)", "etapa donde se puede controlar un peligro significativo"), ("límite crítico", "valor que separa lo aceptable de lo inaceptable en un PCC"), ("monitoreo", "medición planificada para comprobar que se cumple el límite"), ("desviación", "valor que no cumple el límite"), ("verificación", "revisión posterior de que el sistema funciona")],
    worked=[
        ("Comparar con el límite", "En un PCC de ejemplo el límite crítico es de mínimo 30 u.e. y se mide 34 u.e. ¿Hay desviación?", ["Se compara con el mínimo.", "34 es mayor que 30."], "No hay desviación"),
        ("Distinguir monitoreo y verificación", "El operador mide cada lote y el jefe de calidad revisa los registros al final del día. ¿Quién monitorea y quién verifica?", ["Medir cada lote es monitorear.", "Revisar los registros después es verificar."], "El operador monitorea y el jefe de calidad verifica"),
    ],
    mistakes=[("Repetir la medición hasta obtener un valor aceptable y anotar solo ese.", "Se oculta una desviación real y se libera un lote que podría ser peligroso.", "Anota el valor medido y aplica la acción correctiva."),
              ("Confundir monitoreo con verificación.", "El monitoreo mide en la etapa y la verificación revisa después si el sistema funciona.", "Recuerda: medir durante la etapa es monitorear; revisar después es verificar.")],
    T=[
        ("abc", "{F} ¿Cuál es el límite crítico del PCC-1?", "Un mínimo de 50 u.e.", "Un máximo de 50 u.e.", "Un mínimo de 5 u.e.", "La ficha fija el límite crítico como un mínimo de 50 u.e."),
        ("abc", "{F} ¿Cada cuánto se monitorea el PCC-1?", "En cada lote", "Una vez por semana", "Solo al final del turno", "La ficha pide el monitoreo en cada lote."),
        ("abc", "{F} ¿Quién revisa todos los registros cada día?", "El jefe de calidad, como verificación", "El operador, como monitoreo", "El proveedor, como control externo", "La ficha asigna esa revisión diaria al jefe de calidad."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es un punto crítico de control (PCC)?", "Una etapa donde se puede controlar un peligro significativo para evitarlo o reducirlo", "Cualquier etapa del flujo de proceso", "El lugar donde se guardan los registros", "Un PCC no es cualquier etapa: es donde un control es esencial."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es un límite crítico?", "El valor que separa lo aceptable de lo inaceptable en un PCC", "El valor promedio de todas las mediciones", "El costo máximo de una medición", "El límite crítico fija cuándo hay una desviación."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es el monitoreo?", "La medición u observación planificada para comprobar que se cumple el límite", "La revisión anual de un auditor externo", "La entrega del producto al cliente", "El monitoreo ocurre durante la etapa y sigue un plan."),
        ("abc", "{F} Un lote se mide en 52 u.e. en el PCC-1. ¿Qué corresponde concluir?", "Cumple el límite crítico, porque supera el mínimo de 50 u.e.", "Hay una desviación, porque no es igual a 50", "Hay una desviación, porque supera el mínimo", "El límite exige un mínimo de 50 u.e. y 52 lo cumple."),
        ("abc", "{F} Un lote se mide en 48 u.e. en el PCC-1. ¿Qué corresponde hacer?", "Retener el lote y avisar al jefe de calidad, como indica la acción correctiva", "Despacharlo si el aspecto es normal", "Repetir la medición hasta que dé 50 u.e.", "48 u.e. es una desviación y la ficha define esa acción correctiva."),
        ("=", "{F} Se monitorean 6 lotes por día durante 5 días y se registraron 28 mediciones. ¿Cuántas mediciones faltan por registrar?", "6*5-28", "Se calculan todas las mediciones esperadas y se resta lo registrado.", " mediciones"),
        ("abc", "{F} Un operador mide 48 u.e. y repite la medición hasta obtener 51 u.e. y anota solo ese valor. ¿Qué problema hay?", "Se oculta una desviación real; debe registrarse el valor medido y aplicarse la acción correctiva", "Ninguno, porque el valor final cumple", "Solo falta anotar la hora de la última medición", "Registrar solo el valor bueno oculta el problema y expone al consumidor."),
        ("abc", "{F} El jefe de calidad revisa todos los registros del día. ¿Qué etapa del control es?", "La verificación", "El monitoreo", "La acción correctiva", "Revisar los registros después de las mediciones es verificar el sistema."),
        ("abc", "{F} Seis lotes midieron 52, 55, 49, 51, 50 y 47 u.e. en el PCC-1. ¿Cuántos tienen desviación?", "Dos, los de 49 y 47 u.e.", "Uno, el de 47 u.e.", "Tres, los de 49, 50 y 47 u.e.", "Solo 49 y 47 están bajo el mínimo de 50 u.e.; 50 lo cumple."),
        ("abc", "{F} El almacenamiento refrigerado registra 7 °C de ejemplo, con un límite máximo de 5 °C. ¿Qué corresponde?", "Registrar la desviación y avisar al jefe de calidad, sin usar el producto hasta que se evalúe", "Anotar 5 °C para cumplir el registro", "Esperar al turno siguiente para medir de nuevo sin avisar", "Se anota el valor real y se avisa, porque el producto debe evaluarse."),
    ],
    ctx=("abc", "{F} Un operador nuevo pregunta por qué se mide cada lote y no una vez al día. ¿Qué respuesta es correcta?", "Porque el peligro puede variar entre lotes y el monitoreo debe cubrir cada uno", "Porque medir cada lote es más cómodo", "Porque la medición diaria no se permite", "El control frecuente permite detectar una desviación antes de que el lote avance."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué es una desviación?", "Un valor que no cumple el límite", "Indica que se debe aplicar la acción correctiva."),
        ("¿Qué diferencia hay entre monitoreo y verificación?", "El monitoreo mide en la etapa y la verificación revisa después", "Uno controla durante el proceso y el otro comprueba el sistema."),
        ("¿Cómo se anota un valor medido?", "Tal como se midió, sin cambiarlo", "Alterar un valor oculta el problema y expone al consumidor."),
    ],
    op=("Hoja de control de ejemplo: PCC-2, etapa de enfriamiento de un producto; variable: nivel de enfriamiento en u.e.; límite crítico: mínimo 40 u.e.; monitoreo en cada lote por el operador; acción correctiva: retener el lote y avisar al jefe de calidad. Registro de cinco lotes: 44, 41, 38, 40 y 45 u.e. "
        "Escribe: (a) qué lotes tienen desviación, (b) qué se hace con ellos, (c) quién monitorea y quién verifica y (d) por qué no se repite la medición hasta obtener un valor bueno.",
        "(a) Solo el lote de 38 u.e., porque 40 u.e. cumple el mínimo. (b) Retenerlo y avisar al jefe de calidad. (c) El operador monitorea cada lote y el jefe de calidad verifica los registros. (d) Porque se ocultaría una desviación real y podría liberarse un lote peligroso.",
        ["identifica el único lote con desviación", "indica la acción correctiva y los roles", "justifica no repetir la medición"],
        ["hoja con las cuatro respuestas"],
        ["decir que 40 u.e. es desviación", "no retener el lote", "confundir monitoreo con verificación"],
        "Pregunta: «¿cumple el lote de 40 u.e.?». Debe responder que sí, porque el límite es un mínimo de 40."),
    reinforce="Inventa un PCC con variable, límite crítico, monitoreo y acción correctiva, y anota tres mediciones de ejemplo.",
    extend="Explica con un ejemplo inventado por qué la acción correctiva debe estar definida antes de que ocurra la desviación.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 11 (análisis de peligros de un flujo de ejemplo, inventado). Etapa 1, recepción de materia prima: peligros, microbios (biológico) y piedras o trozos de metal (físico); control: criterios de recepción y selección (BPM). "
     "Etapa 2, almacenamiento refrigerado: crecimiento de microbios si falla el frío (biológico); control: temperatura máxima de 5 °C de ejemplo (BPM). Etapa 3, tratamiento de conservación: microbios que podrían sobrevivir (biológico); es el PCC-1, con un límite crítico de mínimo 50 u.e. "
     "Etapa 4, envasado: fragmentos de vidrio si se rompe un frasco (físico); control: inspección de envases y retiro del producto cercano (BPM). Etapa 5, rotulado: alérgeno no declarado (se clasifica como peligro químico); control: verificación del rótulo contra la ficha del producto (BPM). "
     "Registro del PCC-1 en cinco lotes, en u.e.: L-1, 52; L-2, 55; L-3, 49; L-4, 51; L-5, 53.")
build(
    O6, 3, F,
    use="Aprenderé a analizar un caso en papel: leer el análisis de peligros de un flujo, distinguir PCC de otros controles y revisar el registro de un PCC.",
    prior=["Conozco PCC, límite crítico, monitoreo y acción correctiva.", "Conozco los peligros biológico, químico y físico.", "Sé calcular un promedio con enteros."],
    explain=[
        "El análisis de peligros recorre el flujo de proceso etapa por etapa y pregunta: ¿qué peligro puede haber aquí (biológico, químico o físico)? y ¿cómo se controla? Un peligro puede controlarse con las BPM, como la selección de materias primas o el control del frío, o con un PCC cuando una etapa es esencial para evitar un peligro significativo. No todo es PCC: si todo lo fuera, se perdería el foco.",
        "Los alérgenos no declarados se clasifican como peligro químico en este cuaderno. Un alérgeno es una sustancia que puede provocar una reacción alérgica en personas sensibles y debe declararse en el rótulo. Ante una reacción alérgica de una persona se avisa a un adulto responsable y a emergencias; este cuaderno no da indicaciones médicas.",
        "Con el análisis hecho se revisa el registro del PCC: cada valor se compara con el límite crítico y las desviaciones se tratan con la acción correctiva. El promedio de los valores resume, pero no reemplaza la revisión de cada lote." + LIM,
    ],
    vocab=[("análisis de peligros", "revisión etapa por etapa de qué peligros pueden aparecer y cómo se controlan"), ("alérgeno", "sustancia que puede provocar una reacción alérgica en personas sensibles"), ("peligro significativo", "peligro con probabilidad y gravedad que justifican un control especial"), ("medida de control", "acción o regla que previene o reduce un peligro"), ("punto de control (BPM)", "control general de higiene u orden que no es un PCC")],
    worked=[
        ("Clasificar un peligro", "En un frasco de ejemplo aparece un fragmento de vidrio. ¿Qué tipo de peligro es?", ["Es un objeto extraño.", "Eso es un peligro físico."], "Físico"),
        ("Leer un registro", "El límite crítico de ejemplo es de mínimo 40 u.e. y tres lotes midieron 42, 39 y 45. ¿Cuál tiene desviación?", ["Se compara cada valor con el mínimo.", "39 es menor que 40."], "El lote de 39 u.e."),
    ],
    mistakes=[("Declarar todas las etapas como PCC «por seguridad».", "Se pierde el foco en los peligros más significativos y el sistema se vuelve inmanejable.", "Reserva los PCC para los peligros significativos y maneja el resto con BPM."),
              ("Pensar que el PCC controla todos los peligros del flujo.", "Cada etapa tiene sus propios peligros y controles.", "Revisa etapa por etapa qué control corresponde.")],
    T=[
        ("abc", "{F} ¿Qué tipo de peligro es el fragmento de vidrio de la etapa 4?", "Físico", "Biológico", "Químico", "El vidrio es un objeto extraño en el alimento."),
        ("abc", "{F} ¿Cómo se clasifica un alérgeno no declarado en el rótulo, según la ficha?", "Como peligro químico", "Como peligro biológico", "Como peligro físico", "La ficha indica que se clasifica como peligro químico."),
        ("abc", "{F} ¿Qué etapa es el PCC-1?", "El tratamiento de conservación", "El almacenamiento refrigerado", "La recepción de materia prima", "La ficha identifica el tratamiento de conservación como PCC-1."),
        ("abc", "{F} ¿Cuántos lotes del registro tienen desviación respecto del límite crítico?", "Uno, el L-3", "Dos, el L-3 y el L-4", "Ninguno", "Solo L-3 midió 49 u.e., bajo el mínimo de 50."),
        ("abc", "{F} ¿Qué se hace con el lote L-3?", "Retenerlo y avisar al jefe de calidad", "Despacharlo porque está cerca del mínimo", "Anotar 50 u.e. en el registro", "La acción correctiva es retener el lote y avisar."),
        ("=", "{F} ¿Cuántos u.e. suman los cinco lotes del registro?", "52+55+49+51+53", "Se suman los valores de los cinco lotes.", " u.e."),
        ("=", "{F} ¿Cuál es el promedio de los cinco lotes, en u.e.?", "(52+55+49+51+53)//5", "El promedio es la suma dividida por la cantidad de lotes.", " u.e."),
        ("abc", "Un lote de ejemplo midió exactamente 50 u.e. en un PCC con límite crítico de mínimo 50 u.e. ¿Qué corresponde concluir?", "Cumple el límite, porque 50 es igual al mínimo exigido", "Tiene desviación, porque no supera 50", "Tiene desviación, porque está justo en el borde", "Un mínimo de 50 u.e. acepta el valor 50."),
        ("abc", "{F} Un rótulo omite un alérgeno que el producto contiene. ¿Por qué es un peligro?", "Una persona alérgica podría consumirlo sin saberlo y sufrir una reacción", "Porque cambia el sabor del producto", "Porque aumenta el costo del rótulo", "El rótulo es la forma de advertir a las personas sensibles."),
        ("abc", "{F} Alguien dice que, como el tratamiento es un PCC, no hace falta controlar el frío del almacenamiento. ¿Qué respuesta es correcta?", "El PCC no reemplaza los otros controles; cada etapa tiene sus peligros y se controla con BPM o PCC", "Tiene razón, porque el PCC controla todo el flujo", "El frío no importa si el producto se trata después", "El almacenamiento tiene un peligro propio que se controla con la temperatura."),
        ("abc", "Una compañera propone que todas las etapas sean PCC «por seguridad». ¿Qué observación es correcta?", "Si todo es PCC se pierde el foco; los PCC se reservan para peligros significativos y el resto se maneja con BPM", "Es lo ideal porque así hay más controles", "Un PCC no necesita límite crítico", "El análisis de peligros permite concentrar el esfuerzo donde más importa."),
        ("=", "{F} Cada lote tiene 200 envases. Si el lote L-3 queda retenido, ¿cuántos envases de los cinco lotes pueden seguir su curso?", "(5-1)*200", "Se restan el lote retenido y se multiplica por los envases de cada lote.", " envases"),
        ("abc", "{F} Se rompe un frasco en el envasado. ¿Qué medida de control corresponde según la ficha?", "Inspeccionar los envases y retirar el producto cercano, avisando al supervisor", "Recoger los trozos y continuar sin avisar", "Seguir la producción si el vidrio no se ve", "La ficha define inspección y retiro del producto cercano como control."),
    ],
    ctx=("abc", "{F} El jefe de calidad se entera de que un lote salió sin declarar un alérgeno en el rótulo. ¿Qué corresponde?", "Informar de inmediato, detener la distribución según el procedimiento y revisar el lote y el rótulo", "Corregir el rótulo de los siguientes lotes sin informar", "Esperar a que haya reclamos antes de actuar", "Es un peligro para personas sensibles, por lo que se actúa de inmediato y se informa."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué es un alérgeno?", "Una sustancia que puede provocar una reacción alérgica en personas sensibles", "Por eso debe declararse en el rótulo."),
        ("¿Todas las etapas de un flujo son PCC?", "No, solo las que controlan un peligro significativo", "Si todo fuera PCC, se perdería el foco."),
        ("¿Qué se compara en el registro de un PCC?", "Cada valor con el límite crítico", "Así se detectan las desviaciones lote a lote."),
    ],
    op=("Flujo de ejemplo con tres etapas: (1) recepción de materia prima, con piedras como peligro; (2) cocción controlada, que es un PCC con límite crítico de mínimo 60 u.e.; (3) rotulado, con el riesgo de no declarar un alérgeno. Registro de la cocción en cuatro lotes: 62, 58, 64 y 60 u.e. "
        "Escribe: (a) el tipo de peligro de cada etapa, (b) qué lote tiene desviación y qué se hace con él, (c) el promedio del registro y (d) por qué no todas las etapas son PCC.",
        "(a) 1: físico; 2: biológico (microbios), controlado en el PCC; 3: químico (alérgeno no declarado). (b) El lote de 58 u.e.; se retiene y se avisa al jefe de calidad. (c) (62 + 58 + 64 + 60) ÷ 4 = 61 u.e. (d) Porque los PCC se reservan para peligros significativos y el resto se controla con BPM.",
        ["clasifica los peligros", "identifica el lote con desviación y su acción", "calcula el promedio y justifica los PCC"],
        ["hoja con las cuatro respuestas"],
        ["decir que 60 u.e. es desviación", "declarar todas las etapas PCC", "olvidar la acción correctiva"],
        "Pregunta: «¿cumple el lote de 60 u.e.?». Debe responder que sí, porque 60 es igual al mínimo."),
    reinforce="Escribe tres etapas de un flujo inventado y, para cada una, un peligro, su tipo y una medida de control.",
    extend="Explica con un ejemplo inventado por qué hacer PCC de todas las etapas haría más difícil controlar lo importante.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 12 (trazabilidad de un lote de ejemplo, inventada). Lote L-120 del producto Q: 800 envases en 40 cajas de 20 envases; se elaboró con la materia prima del lote de proveedor P-7. "
     "Al verificar los registros, el jefe de calidad ve que el PCC-1 del lote L-120 midió 46 u.e. (límite crítico: mínimo 50 u.e.), una desviación a la que no se aplicó la acción correctiva. "
     "Despachos del lote: cliente 1, 15 cajas; cliente 2, 10 cajas; en la bodega de la planta, 15 cajas. La trazabilidad hacia atrás permite saber qué materias primas y procesos tuvo el lote; hacia adelante, a quién se despachó. Costo de ejemplo de retirar una caja: $1.200.")
build(
    O6, 4, F,
    use="Aprenderé a aplicar la trazabilidad por lote con datos de ejemplo: ubicar un lote hacia atrás y hacia adelante, calcular cuánto producto está afectado y decidir un retiro.",
    prior=["Conozco el PCC, el límite crítico y la acción correctiva.", "Sé multiplicar y restar enteros.", "Sé leer una ficha con despachos."],
    explain=[
        "Un lote es un conjunto de producto elaborado en condiciones iguales, con un código que lo identifica. La trazabilidad es la capacidad de seguir un lote: hacia atrás, para saber con qué materias primas, insumos y procesos se elaboró; hacia adelante, para saber a quién se despachó. Se logra con el código de lote en cada caja y envase, y con los registros de producción y despacho.",
        "Si se detecta una desviación después del despacho, se usa la trazabilidad para ubicar el lote afectado: cuántas cajas siguen en la planta y cuántas están en clientes. Un retiro es sacar del mercado el producto afectado, avisando a los clientes. Informar es parte del deber de proteger a las personas, según la norma vigente.",
        "Lo mejor es evitar el problema: el monitoreo y la acción correctiva en el momento impiden despachar un lote con desviación. La verificación de los registros es la segunda barrera." + LIM,
    ],
    vocab=[("lote", "conjunto de producto elaborado en condiciones iguales, con un código"), ("trazabilidad", "capacidad de seguir un lote hacia atrás y hacia adelante"), ("trazabilidad hacia atrás", "saber con qué materias primas y procesos se elaboró el lote"), ("trazabilidad hacia adelante", "saber a quién se despachó el lote"), ("retiro", "sacar del mercado el producto afectado")],
    worked=[
        ("Ubicar producto", "Un lote de ejemplo tiene 30 cajas: 12 en el cliente A, 8 en el cliente B y el resto en bodega. ¿Cuántas cajas hay en bodega?", ["Cajas despachadas: 12 + 8 = 20.", "30 − 20 = 10."], "10 cajas"),
        ("Distinguir sentidos", "Para saber qué proveedor entregó la materia prima de un lote, ¿se usa la trazabilidad hacia atrás o hacia adelante?", ["Interesa el origen del lote.", "El origen se rastrea hacia atrás."], "Hacia atrás"),
    ],
    mistakes=[("No guardar el registro de a quién se despachó cada lote.", "Ante un problema no se sabe a quién avisar y hay que retirar de más.", "Registra el despacho por lote, con cliente y cantidad."),
              ("Retirar solo el producto de la bodega y no avisar a los clientes.", "El producto despachado sigue en circulación.", "Avisa a los clientes y organiza el retiro de lo despachado.")],
    T=[
        ("abc", "{F} ¿Qué significa, en este caso, la trazabilidad hacia adelante?", "Saber a qué clientes se despachó el lote L-120", "Saber qué proveedor entregó la materia prima", "Saber cuándo se limpió el equipo", "Hacia adelante se rastrea el destino del lote."),
        ("abc", "{F} ¿Qué dato permite la trazabilidad hacia atrás del lote L-120?", "El lote de proveedor P-7 de la materia prima", "El cliente 2", "Las 15 cajas en bodega", "El lote P-7 informa el origen de la materia prima."),
        ("=", "{F} ¿Cuántas cajas del lote L-120 fueron despachadas?", "15+10", "Se suman las cajas del cliente 1 y del cliente 2.", " cajas"),
        ("=", "{F} ¿Cuántas cajas del lote L-120 quedan en la bodega?", "40-15-10", "Al total de cajas se le restan las despachadas.", " cajas"),
        ("=", "{F} ¿Cuántos envases del lote L-120 fueron despachados?", "(15+10)*20", "Se multiplican las cajas despachadas por los envases de cada caja.", " envases"),
        ("abc", "{F} ¿Qué acción corresponde con las cajas que están en la bodega?", "Retenerlas e identificarlas hasta que el jefe de calidad decida", "Despacharlas rápido, antes de que el problema se conozca", "Mezclarlas con otros lotes", "El lote tiene una desviación y no debe seguir su curso sin una decisión formal."),
        ("=", "{F} ¿Cuántos envases hay en las cajas retenidas en la bodega?", "15*20", "Se multiplican las cajas retenidas por los envases de cada caja.", " envases"),
        ("abc", "En Elaboración Industrial de Alimentos: ¿para qué sirve codificar cada caja con el número de lote?", "Para identificar el lote y rastrearlo hacia atrás y hacia adelante", "Para decidir el precio de venta", "Para reemplazar el rótulo del producto", "El código de lote es la clave que conecta cada caja con sus registros."),
        ("=", "{F} Si el cliente 1 devuelve 12 de las 15 cajas recibidas, ¿cuántas cajas faltan por devolver de ese cliente?", "15-12", "A las cajas recibidas se les restan las devueltas.", " cajas"),
        ("abc", "{F} Sin registro de despachos por lote, ¿qué ocurriría en un retiro?", "No se sabría a quién avisar y habría que retirar más producto del necesario", "Se retiraría exactamente lo afectado", "No habría retiro posible ni necesario", "La falta de registro obliga a buscar el producto sin saber dónde está."),
        ("abc", "{F} La desviación se detectó en la verificación, cuando parte del lote ya estaba despachada. ¿Qué enseñanza deja?", "Que el monitoreo y la acción correctiva en el momento evitan despachar lotes con desviación", "Que la verificación es innecesaria", "Que la desviación no era importante", "El control a tiempo evita que un lote con desviación salga de la planta."),
        ("=", "{F} Si se retiran las 25 cajas despachadas, ¿cuántos pesos cuesta el retiro?", "25*1200", "Se multiplican las cajas retiradas por el costo de retirar cada una.", " pesos"),
        ("=", "{F} El cliente 2 ya vendió 4 de sus 10 cajas y devuelve las que le quedan. ¿Cuántos envases devuelve?", "(10-4)*20", "Se restan las cajas vendidas y se multiplica por los envases de cada caja.", " envases"),
    ],
    ctx=("abc", "{F} La gerencia sugiere no avisar a los clientes para evitar mala imagen. ¿Qué respuesta corresponde?", "Se informa y se organiza el retiro, porque está en juego la seguridad de las personas y la norma vigente lo exige", "No se avisa, porque el problema es pequeño", "Se avisa solo si algún cliente reclama", "La seguridad de los consumidores va antes de la imagen de la planta."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué diferencia hay entre trazabilidad hacia atrás y hacia adelante?", "Hacia atrás rastrea el origen del lote; hacia adelante, su destino", "Ambos sentidos se apoyan en el código de lote."),
        ("¿Qué es un retiro?", "Sacar del mercado el producto afectado", "Incluye avisar a quienes recibieron el producto."),
        ("¿Qué permite el código de lote?", "Conectar cada caja con sus registros", "Sin código no se puede rastrear el lote."),
    ],
    op=("Lote L-300 de ejemplo: 600 envases en 30 cajas de 20 envases. Despachos: cliente A, 12 cajas; cliente B, 8 cajas; el resto en bodega. Se detecta una desviación del PCC en ese lote. El costo de ejemplo de retirar una caja es de $1.000. "
        "Escribe: (a) cuántas cajas hay en bodega, (b) cuántos envases fueron despachados, (c) qué harías con el producto en bodega y con el despachado y (d) el costo de retirar las cajas despachadas.",
        "(a) 30 − 12 − 8 = 10 cajas. (b) (12 + 8) × 20 = 400 envases. (c) Retener e identificar las cajas de bodega, y avisar a los clientes A y B para retirar lo despachado. (d) 20 × 1.000 = 20.000 pesos.",
        ["calcula 10 cajas y 400 envases", "propone retener y avisar", "calcula el costo del retiro"],
        ["hoja con las cuatro respuestas"],
        ["olvidar avisar a los clientes", "no restar las cajas despachadas", "calcular el costo con todas las cajas"],
        "Pregunta: «¿qué pasaría si no se sabe a quién se despachó?». Debe decir que no se podría avisar a los clientes."),
    reinforce="Inventa un lote con cajas, despachos y cajas en bodega, y calcula cuántas cajas están afectadas en cada lugar.",
    extend="Explica con un ejemplo inventado por qué el código de lote debe estar en cada caja y no solo en la factura.",
)
