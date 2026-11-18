"""Mecánica Automotriz TP (3.º y 4.º medio) módulo A: OAE-01 (inspeccionar y diagnosticar averías), OAE-02 (manuales, planos, diagramas y normas de emisiones) y OAE-03 (mantenimiento básico según pautas). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_meau_common import AVISO, EMER, build

O1 = "TP-MEAU-3y4-OAE-01"
O2 = "TP-MEAU-3y4-OAE-02"
O3 = "TP-MEAU-3y4-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Taller Autoservicio Demo» atiende vehículos livianos. Su matriz de peligros anota: un vehículo elevado sobre un elevador, aceite derramado en el piso, una batería de 12 V sobre un carro, "
     "gases de escape en un recinto con poca ventilación, el ruido de una herramienta neumática y piezas calientes del motor. Dotación del turno: 15 personas; el taller tiene 3 puestos de trabajo.")
build(
    O1, 1, F,
    use="Aprenderé qué trabajos reúne la mecánica automotriz, qué peligros típicos tiene un taller de vehículos y cómo se ordenan las medidas de prevención.",
    prior=["Sé leer una tabla sencilla.", "Sé multiplicar y dividir números enteros.", "Sé que un taller sigue reglas escritas."],
    explain=[
        "La mecánica automotriz reúne la inspección, el mantenimiento, el diagnóstico y la reparación de vehículos livianos, semipesados y pesados y de sus sistemas mecánicos, eléctricos y electrónicos. Se trabaja en talleres del sector metalmecánico, guiados por manuales y especificaciones del fabricante. Un taller anota sus peligros en una matriz de peligros, una tabla que los lista junto a sus medidas de control.",
        "Un peligro es una fuente que puede causar daño y el riesgo es la posibilidad de que ese daño ocurra. La matriz de ejemplo puede puntuar el riesgo multiplicando la probabilidad (de 1 a 5) por la gravedad (de 1 a 5). Las medidas se ordenan en la jerarquía de controles, de la más a la menos efectiva: eliminar, sustituir, controles de ingeniería (como extraer los gases hacia el exterior), controles administrativos (reglas, señales, permisos) y, al final, el equipo de protección personal (EPP). El monóxido de carbono, un gas del escape, no se ve ni se huele y es tóxico.",
        f"La Dirección del Trabajo fiscaliza que se cumpla la normativa laboral. Trabajar bajo un vehículo elevado, con baterías o con gases de escape es tarea de personal autorizado y capacitado. {EMER} {AVISO}",
    ],
    vocab=[("mecánica automotriz", "inspección, mantenimiento, diagnóstico y reparación de vehículos y sus sistemas"), ("vehículo liviano", "vehículo de carga y tamaño menores, como un automóvil"), ("matriz de peligros", "tabla que lista los peligros de un lugar y sus medidas de control"), ("control de ingeniería", "medida que cambia el lugar o el equipo para reducir el peligro"), ("jerarquía de controles", "orden de las medidas de prevención, de la más a la menos efectiva"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Peligro y riesgo", "En un taller de ejemplo hay un cable de alimentación tendido a lo ancho de un pasillo. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el cable tendido, que puede causar daño.", "El riesgo es que alguien tropiece y se lesione."], "Peligro: el cable tendido; riesgo: que alguien tropiece y se lesione"),
        ("Tipo de control", "Un taller de ejemplo pega un cartel «Piso mojado» y marca con cinta la zona que no se debe pisar. ¿Qué tipo de control es?", ["Un cartel y una zona marcada ordenan la conducta de las personas.", "Las reglas, las señales y los permisos son controles administrativos."], "Control administrativo"),
    ],
    mistakes=[("Creer que con casco y guantes basta para operar cualquier equipo del taller.", "El EPP es la última barrera y no reemplaza la formación ni la autorización.", "Primero se controla el peligro; el equipo lo maneja personal autorizado."),
              ("Llamar «riesgo» al objeto que puede dañar.", "El objeto es el peligro; el riesgo es la posibilidad de daño.", "Nombra primero el peligro y luego cuál es el daño posible.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué trabajos reúne esta especialidad?", "Inspeccionar, mantener y reparar vehículos y sus sistemas", "Solo fabricar vehículos nuevos en una línea de montaje", "Solo atender al público y cobrar los trabajos", "La especialidad abarca inspección, mantenimiento y reparación; las otras opciones recortan el oficio."),
        ("abc", "En Mecánica Automotriz: ¿qué diferencia hay entre peligro y riesgo?", "El peligro es la fuente que puede dañar y el riesgo es la posibilidad de que el daño ocurra", "El peligro es el daño ya ocurrido y el riesgo es la fuente", "Son sinónimos y se anotan en una sola columna", "El peligro es la fuente y el riesgo es la posibilidad del daño; no son lo mismo."),
        ("abc", "En Mecánica Automotriz: ¿cuál es el orden de la jerarquía de controles, de la más a la menos efectiva?", "Eliminar, sustituir, controles de ingeniería, controles administrativos y EPP", "EPP, controles administrativos, controles de ingeniería, sustituir y eliminar", "Controles administrativos, EPP, eliminar, sustituir y controles de ingeniería", "La jerarquía empieza por quitar el peligro y termina en el EPP, que solo protege a quien lo usa."),
        ("abc", "{F} ¿Qué peligro de la matriz puede causar una intoxicación por inhalación?", "Los gases de escape en un recinto con poca ventilación", "El ruido de una herramienta neumática", "Las piezas calientes del motor", "Los gases tóxicos se inhalan; el ruido daña la audición y las piezas calientes causan quemaduras."),
        ("abc", "{F} El taller encierra la herramienta neumática en una cabina que baja el ruido que llega al resto del recinto. ¿En qué nivel de la jerarquía de controles está esa medida?", "En los controles de ingeniería", "En el EPP, el último nivel", "En los controles administrativos", "La cabina cambia el equipo y el lugar; no depende de una regla ni de un equipo personal."),
        ("abc", "{F} Una regla escrita dice que nadie se ubica bajo el vehículo elevado sin autorización. ¿Qué tipo de control es?", "Un control administrativo", "Un control de ingeniería", "El equipo de protección personal", "Una regla ordena la conducta de las personas, y por eso es administrativa."),
        ("=", "{F} El taller asigna 1 monitor de seguridad por cada 5 personas de la dotación del turno. ¿Cuántos monitores corresponden?", "15//5", "Se divide la dotación entre las personas que cubre cada monitor.", " monitores"),
        ("=", "Un peligro de ejemplo tiene probabilidad 5 y gravedad 4. Con una medida de control la probabilidad baja a 2 y la gravedad se mantiene. ¿Cuántos puntos baja el puntaje?", "5*4-2*4", "Se calcula el puntaje antes y después, y se restan.", " puntos"),
        ("=", "{F} Cada uno de los 3 puestos de trabajo debe tener 2 extintores y el taller guarda 1 más de repuesto. ¿Cuántos extintores necesita?", "3*2+1", "Se multiplican los puestos por los extintores de cada uno y se suma el de repuesto.", " extintores"),
        ("abc", "{F} Un aprendiz dice: «ya tengo casco y guantes, así que puedo subir y bajar el vehículo del elevador». ¿Qué respuesta es correcta?", "Es falso: operar un elevador exige formación, autorización y norma vigente, y el EPP no lo reemplaza", "Es cierto, porque el EPP lo protege de cualquier peligro", "Es cierto, si lo hace despacio y otra persona lo mira", "Usar EPP no habilita para operar equipos; la autorización y la formación son aparte."),
        ("abc", "En una visita a un taller de ejemplo, un vehículo elevado se inclina y empieza a caer. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte para sostenerlo hasta que llegue ayuda", "Empujar el vehículo desde un lado para enderezarlo", "Acercarse a una carga que cae puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("=", "{F} El peligro A de una matriz de ejemplo tiene probabilidad 3 y gravedad 5; el peligro B tiene probabilidad 4 y gravedad 3. ¿Cuántos puntos más tiene A que B?", "3*5-4*3", "Se calculan los dos puntajes y se restan.", " puntos"),
        ("abc", "{F} Un compañero dice: «el riesgo de los gases de escape es bajo porque a veces se abre la puerta». ¿Qué observación es correcta?", "El riesgo se evalúa con probabilidad y gravedad y necesita un control estable, no depender de que la puerta esté abierta", "Tiene razón, porque abrir una puerta es un control de ingeniería", "Tiene razón, porque la gravedad de un gas que no se ve es baja", "Un control que depende de un descuido ocasional no es estable; el gas sin olor puede ser muy grave."),
    ],
    ctx=("abc", "El jefe de un taller de ejemplo te dice: «ponte unos guantes y ayúdame a subir ese vehículo al elevador, tú ya sabes de motores». ¿Qué respondes?", "Que no, porque operar un elevador exige instructor autorizado y norma vigente, y que consultarás a un adulto responsable", "Que sí, porque con guantes basta", "Que sí, pero solo si el vehículo es liviano", "Saber de motores y usar guantes no habilitan para operar equipos de elevación."),
    sc=[
        ("En Mecánica Automotriz: ¿qué gas del escape no se ve ni se huele y es tóxico?", "El monóxido de carbono", "Por ser invisible e inodoro no se detecta con los sentidos."),
        ("En Mecánica Automotriz: ¿cuál es el último nivel de la jerarquía de controles?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("¿Qué institución fiscaliza que el taller cumpla la normativa laboral?", "La Dirección del Trabajo", "Esa institución fiscaliza lo laboral, como las condiciones de trabajo."),
    ],
    op=("Un taller de ejemplo anota dos tareas: (1) pedir a un aprendiz que «ayude» con un vehículo elevado en el elevador; (2) hacer funcionar un motor en un recinto cerrado. Escribe (a) el peligro y el riesgo de cada tarea, (b) un control de ingeniería para una de ellas, (c) un control administrativo, (d) por qué el EPP no basta y quién hace estas tareas. No describas cómo se hacen.",
        "(a) Tarea 1: peligro, el vehículo elevado; riesgo, que caiga o aplaste a alguien. Tarea 2: peligro, los gases de escape; riesgo, intoxicarse al respirarlos. (b) Extraer los gases hacia el exterior con un sistema de ventilación. (c) Una regla escrita y una señal de que solo personal autorizado interviene en el elevador. (d) El EPP es la última barrera: no quita el peligro. Las tareas las hace personal autorizado con norma vigente.",
        ["distingue peligro y riesgo", "propone un control de ingeniería", "propone un control administrativo", "explica por qué el EPP no basta y quién hace la tarea"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al vehículo elevado", "proponer solo el EPP", "describir cómo se hace la tarea"],
        "Pregunta: «¿qué medida quitaría o alejaría el peligro?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe los cinco niveles de la jerarquía de controles en orden y pon junto a cada uno un ejemplo inventado de taller automotriz.",
    extend="Explica con un ejemplo por qué un cartel de advertencia no reemplaza a un control de ingeniería.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (orden de trabajo de ejemplo, inventada). Orden OT-A-210 del «Taller Autoservicio Demo». Vehículo liviano «Modelo Demo 1», 62.000 km. Queja escrita por la persona propietaria: «el motor se calienta más de lo normal y el ventilador a veces no gira». "
     "Asignada a «Técnico Demo». Horas estimadas: 3. Tarifa de mano de obra de ejemplo: $12.000 por hora.")
build(
    O1, 2, F,
    use="Aprenderé a distinguir síntoma, falla y avería, sistema y componente, qué documentos usa un taller para diagnosticar y qué hace cada rol.",
    prior=["Sé leer una orden con datos.", "Sé multiplicar números enteros.", "Sé que un vehículo tiene varios sistemas."],
    explain=[
        "El síntoma es lo que se observa o se reporta, como un ruido o una luz de aviso. La falla es el funcionamiento incorrecto de un componente o de un sistema, y la avería es el daño o defecto que impide el funcionamiento normal. La causa es el origen de la falla. Un sistema es un conjunto de componentes que cumplen una función, como refrigeración o lubricación; un componente es una pieza individual, como un termostato o un fusible.",
        "El síntoma no dice cuál pieza falla: la causa se establece con inspección, datos y especificaciones. El taller usa la hoja de recepción, la orden de trabajo (que registra el vehículo, la queja, las horas estimadas y el costo), el historial del vehículo y el manual del fabricante. El costo de mano de obra se calcula multiplicando las horas por la tarifa por hora.",
        f"El asesor de servicio recibe y registra la queja; el jefe de taller asigna y supervisa; el técnico autorizado ejecuta; el control de calidad verifica antes de entregar. {EMER} {AVISO}",
    ],
    vocab=[("síntoma", "lo que se observa o se reporta"), ("falla", "funcionamiento incorrecto de un componente o sistema"), ("avería", "daño o defecto que impide el funcionamiento normal"), ("sistema", "conjunto de componentes que cumplen una función"), ("componente", "pieza individual de un sistema"), ("orden de trabajo", "documento que registra el vehículo, la queja, las horas y el costo"), ("historial del vehículo", "registro de sus revisiones y trabajos anteriores")],
    worked=[
        ("Síntoma o causa", "En una orden de ejemplo se anota: «al encender las luces se escucha un zumbido». ¿Es un síntoma o una causa?", ["Lo escrito describe lo que se escucha.", "No dice qué pieza falla: es un síntoma."], "Es un síntoma"),
        ("Mano de obra", "Una orden de ejemplo estima 5 horas con tarifa de $10.000 por hora. ¿Cuánto es la mano de obra?", ["Se multiplican las horas por la tarifa.", "5 por 10.000 son 50.000."], "$50.000"),
    ],
    mistakes=[("Escribir en la orden la pieza que «seguro» está mala sin haber inspeccionado.", "Eso es un diagnóstico sin evidencia; el síntoma no dice cuál es la causa.", "Anota el síntoma con lo que informa la persona y deja el diagnóstico para la inspección."),
              ("Usar «síntoma», «falla» y «avería» como si fueran lo mismo.", "El síntoma se observa; la falla es el funcionamiento incorrecto y la avería es el daño.", "Pregunta si es algo que se observa, un mal funcionamiento o un daño.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué es un síntoma?", "Lo que se observa o se reporta, como un ruido o una luz de aviso", "La pieza exacta que está dañada", "La reparación que se debe hacer", "El síntoma es lo observado; la pieza dañada y la reparación son otra etapa."),
        ("abc", "En Mecánica Automotriz: ¿qué diferencia hay entre sistema y componente?", "El sistema es un conjunto que cumple una función y el componente es una pieza individual del sistema", "El componente es el conjunto y el sistema es una pieza individual", "Son lo mismo y solo cambia el nombre según el taller", "Un sistema agrupa componentes; un fusible o un termostato son componentes."),
        ("abc", "En Mecánica Automotriz: ¿qué documento pide una tarea al taller y registra el vehículo, la queja y las horas estimadas?", "La orden de trabajo", "El manual del fabricante", "El certificado de calibración de un instrumento", "La orden de trabajo organiza la tarea; el manual y el certificado cumplen otras funciones."),
        ("abc", "{F} Según la queja escrita en la orden, ¿cuál de estas afirmaciones es un síntoma y no un diagnóstico?", "El motor se calienta más de lo normal", "El termostato está pegado", "El motor eléctrico del ventilador está quemado", "Lo que la persona observa es el síntoma; las otras afirmaciones nombran una causa sin comprobarla."),
        ("abc", "{F} ¿Con qué sistema se relaciona de forma directa el síntoma principal de la orden?", "Con el sistema de refrigeración", "Con el sistema de lubricación", "Con el sistema de alumbrado", "El calentamiento del motor se vincula con la refrigeración; los otros sistemas tienen otra función."),
        ("abc", "{F} El técnico asignado quiere saber si este vehículo ya tuvo trabajos anteriores en el sistema. ¿Qué documento consulta?", "El historial del vehículo", "El plano de conjunto de la carrocería", "La tarifa de mano de obra", "El historial registra las revisiones y trabajos anteriores del vehículo."),
        ("=", "{F} ¿Cuántos pesos cuesta la mano de obra estimada de la orden?", "3*12000", "Se multiplican las horas estimadas por la tarifa por hora.", " pesos"),
        ("=", "Otra orden de ejemplo estima 4 horas de mano de obra a $15.000 la hora y $28.000 en repuestos. ¿Cuántos pesos suma la orden?", "4*15000+28000", "Se suma la mano de obra, horas por tarifa, con los repuestos.", " pesos"),
        ("=", "{F} El historial anota que el vehículo tenía 47.000 km en su última revisión. ¿Cuántos km recorrió desde entonces hasta esta orden?", "62000-47000", "Se resta el kilometraje de la revisión al kilometraje actual.", " km"),
        ("abc", "{F} Un compañero dice: «el ventilador a veces no gira, así que hay que cambiar el ventilador». ¿Qué observación es correcta?", "La queja es un síntoma; el ventilador es solo un componente posible y la causa se establece con inspección y datos", "Es correcta, porque el síntoma siempre señala la pieza dañada", "Es correcta, si el ventilador es la pieza más barata de reemplazar", "El síntoma no identifica la pieza: otras causas pueden explicar que un ventilador no gire."),
        ("abc", "Un asesor de servicio anota en la orden «falla en el módulo electrónico» sin haber inspeccionado el vehículo. ¿Qué problema tiene esa anotación?", "Registra un diagnóstico sin evidencia en lugar del síntoma que informó la persona", "Ninguno, porque el asesor debe anotar la causa al recibir", "Que es muy corta y basta con agregar más palabras", "El asesor registra lo que se informa; la causa se establece después con datos."),
        ("=", "{F} Se agrega un trabajo adicional de 2 horas a la misma tarifa y el taller descuenta $6.000 de la mano de obra total por una garantía de ejemplo. ¿Cuántos pesos quedan por mano de obra?", "(3+2)*12000-6000", "Se suman las horas, se multiplican por la tarifa y se resta el descuento.", " pesos"),
        ("abc", "Una orden de ejemplo se cierra con la firma de control de calidad antes de que el asesor entregue el vehículo. ¿Qué función cumple esa firma?", "Dejar constancia de que otra persona verificó que el trabajo cumple lo pedido", "Reemplazar la firma de quien ejecutó el trabajo", "Autorizar al técnico a elegir un repuesto de menor calidad", "La firma de control de calidad da constancia de una verificación independiente."),
    ],
    ctx=("abc", "Una persona propietaria te cuenta en la recepción de un taller de ejemplo: «mi auto hace un ruido raro». ¿Qué corresponde anotar en la orden?", "El ruido como síntoma, con lo que la persona informe de cuándo ocurre, sin afirmar la causa", "«Falla de rodamiento», para ahorrar tiempo", "Nada, hasta que el técnico desarme el vehículo", "La recepción registra el síntoma; la causa se establece con inspección autorizada."),
    sc=[
        ("En Mecánica Automotriz: ¿qué es una avería?", "Un daño o defecto que impide el funcionamiento normal", "La avería es el daño; el síntoma es lo que se nota."),
        ("¿Qué rol verifica el trabajo antes de la entrega?", "El control de calidad", "Verifica que lo hecho cumpla lo pedido."),
        ("¿Cómo se calcula la mano de obra estimada de una orden?", "Se multiplican las horas por la tarifa por hora", "Horas por tarifa da el costo de la mano de obra."),
    ],
    op=("Ficha de ejemplo: orden OT-A-305. Queja escrita: «al girar la llave el tablero se apaga unos segundos». Horas estimadas: 2. Tarifa: $14.000 por hora. Repuestos de ejemplo: $40.000. Escribe (a) cuál es el síntoma, (b) dos sistemas que podrían relacionarse, como candidatos y no como confirmados, (c) por qué todavía no se anota una pieza dañada, (d) el costo total de la orden.",
        "(a) El tablero se apaga unos segundos al girar la llave. (b) El sistema eléctrico y el sistema de arranque, como candidatos. (c) Porque falta inspección con datos y especificaciones; la queja no identifica la pieza. (d) 2 × 14.000 + 40.000 = 68.000 pesos.",
        ["identifica el síntoma", "propone sistemas como candidatos", "explica por qué no hay pieza confirmada", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["anotar una pieza como confirmada", "confundir síntoma con causa", "calcular mal el costo"],
        "Pregunta: «¿la queja dice qué pieza falla o solo lo que se observa?». Si duda, pídele que relea la definición de síntoma."),
    reinforce="Inventa dos quejas de personas propietarias y subraya en cada una el síntoma; luego nombra un sistema candidato para cada una.",
    extend="Explica con un ejemplo por qué una misma queja puede tener más de una causa posible.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado; los datos los registró personal autorizado). Vehículo liviano «Modelo Demo 3». Síntoma escrito: «al intentar arrancar, el motor gira muy lento y luego solo se oye un chasquido». "
     "Registro: tensión de la batería en reposo, 12 V (mínimo de la especificación de ejemplo: 12 V); tensión durante el intento de arranque, 8 V (mínimo de la especificación de ejemplo: 10 V); luces del tablero: se atenúan al intentar arrancar; nivel de combustible: normal.")
build(
    O1, 3, F,
    use="Aprenderé a razonar un caso de falla en papel: partir del síntoma, proponer sistemas candidatos, usar datos para confirmar o descartar y escribir una conclusión que no se pase de lo que los datos permiten.",
    prior=["Sé qué es un síntoma.", "Sé comparar números enteros.", "Sé que una especificación es un valor de referencia."],
    explain=[
        "Un análisis de falla en papel sigue un orden: primero el síntoma, después los sistemas candidatos, luego los datos que confirman o descartan cada candidato y al final la conclusión. Un dato descarta una causa cuando muestra que esa causa no explica el síntoma; un dato confirma cuando coincide con lo que esa causa produciría. Una especificación técnica del fabricante es un valor o rango de referencia con el que se compara una medición.",
        "Un dato fuera de especificación señala el sistema sospechoso, pero no siempre prueba qué componente falla. Por ejemplo, una tensión baja durante el arranque apunta al suministro de energía, que incluye la batería, las conexiones y el consumo del motor de arranque. Cambiar piezas «por si acaso» gasta repuestos, tapa la causa real y deja el registro sin evidencia. La conclusión debe decir qué se sabe y qué falta verificar.",
        f"Las mediciones las toma personal autorizado y capacitado; aquí solo se interpreta un registro escrito. {EMER} {AVISO}",
    ],
    vocab=[("sistema candidato", "sistema que podría explicar el síntoma y que aún no está confirmado"), ("confirmar", "mostrar con un dato que una causa explica el síntoma"), ("descartar", "mostrar con un dato que una causa no explica el síntoma"), ("especificación técnica", "valor o rango de referencia del fabricante"), ("conclusión apresurada", "afirmar una causa con menos datos de los necesarios"), ("fusible abierto", "fusible que se cortó por exceso de corriente y ya no deja pasar corriente")],
    worked=[
        ("Descartar con un dato", "Caso de ejemplo: una luz de aviso del tablero no enciende al girar la llave. Un registro de personal autorizado anota que la lámpara de esa luz está en buen estado. ¿Qué descarta ese dato?", ["Una lámpara en buen estado no explica que la luz no encienda.", "Descarta que la lámpara sea la causa."], "Descarta la lámpara como causa"),
        ("Comparar con la especificación", "Una lectura de ejemplo marca 9 V y el mínimo de la especificación es 10 V. ¿Cuántos V faltan?", ["Se resta la lectura al mínimo.", "10 menos 9 son 1."], "Faltan 1 V"),
    ],
    mistakes=[("Concluir que una pieza está mala porque un dato está fuera de especificación.", "El dato señala el sistema sospechoso; varias piezas pueden producir el mismo dato.", "Escribe qué sistema apunta el dato y qué verificación falta."),
              ("Cambiar varias piezas a la vez «por si acaso».", "No se sabe cuál era la causa y el registro queda sin evidencia.", "Cada decisión se apoya en un dato que confirma o descarta.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿cuál es el orden lógico de un análisis de falla en papel?", "Síntoma, sistemas candidatos, datos que confirman o descartan y conclusión", "Conclusión, cambio de piezas y luego el síntoma", "Sistema candidato, cambio de pieza y datos al final", "El análisis parte de lo observado y llega a una conclusión apoyada en datos."),
        ("abc", "En Mecánica Automotriz: ¿qué significa que un dato descarta una causa posible?", "Muestra que esa causa no explica el síntoma", "Confirma que esa causa es la correcta", "Obliga a repetir toda la inspección desde cero", "Descartar es mostrar que una causa no explica lo observado."),
        ("abc", "En Mecánica Automotriz: ¿qué es una especificación técnica del fabricante?", "Un valor o rango de referencia con el que se compara una medición", "La opinión del técnico más experimentado", "El precio de la reparación acordado con la persona propietaria", "La especificación es la referencia del fabricante; no depende de opiniones ni de precios."),
        ("abc", "{F} ¿Qué dato de la ficha muestra que algo no cumple lo esperado?", "La tensión durante el intento de arranque, 8 V, está bajo el mínimo de 10 V", "La tensión en reposo, 12 V, está fuera de especificación", "El nivel de combustible normal, que debería ser mayor", "En reposo la tensión es igual al mínimo, así que cumple; solo la lectura en arranque queda bajo su mínimo."),
        ("abc", "{F} ¿Qué sistema queda como principal candidato según los datos?", "El de arranque y su suministro de energía", "El de combustible", "El de refrigeración", "La tensión baja y el giro lento apuntan al suministro de energía del arranque."),
        ("abc", "{F} ¿Qué relación hay entre la lectura de 8 V y el síntoma de giro lento?", "Una tensión baja durante el arranque es coherente con un giro lento", "El giro lento hace que la tensión suba", "No hay relación, porque la tensión solo importa en reposo", "El dato coincide con lo que produciría un suministro de energía insuficiente."),
        ("=", "{F} ¿Cuántos V bajó la tensión desde el reposo hasta el intento de arranque?", "12-8", "Se resta la tensión del intento de arranque a la tensión en reposo.", " V"),
        ("=", "Otro caso de ejemplo: el mínimo durante el arranque es 10 V y tres vehículos registran 9 V, 11 V y 7 V. ¿Cuántos V suman las diferencias bajo el mínimo de los vehículos que no cumplen?", "(10-9)+(10-7)", "Solo se suman las diferencias de los vehículos bajo 10 V, que son el primero y el tercero.", " V"),
        ("abc", "{F} ¿Qué falta para señalar la pieza responsable en este caso?", "Una verificación adicional del suministro de energía y del motor de arranque, hecha por personal autorizado", "Nada: con 8 V ya se sabe que hay que cambiar la batería", "Nada: el giro lento prueba que el motor de arranque está dañado", "El dato apunta al sistema, pero varias piezas pueden producirlo y falta verificar cuál."),
        ("abc", "{F} Un compañero dice: «8 V es menor que 10 V, así que la batería está mala y hay que cambiarla». ¿Qué respuesta es correcta?", "Es una conclusión apresurada: el dato señala el suministro de energía, que incluye batería, conexiones y consumo del motor de arranque", "Es correcta, porque la batería es la única fuente de tensión", "Es incorrecta, porque una tensión baja solo afecta el alumbrado y no el arranque", "El dato no distingue entre las piezas del suministro de energía."),
        ("abc", "Un técnico cambia tres piezas a la vez «por si acaso» y el síntoma desaparece. ¿Qué problema tiene esa forma de trabajar?", "No se sabe cuál era la causa, se gastó en repuestos innecesarios y el registro queda sin evidencia", "Ninguno: lo importante es que el síntoma desapareció", "Que cambiar piezas siempre empeora el síntoma", "Sin datos que confirmen una causa no hay trazabilidad ni se sabe qué falló."),
        ("=", "Otro vehículo de ejemplo registra 10 V en reposo y 6 V durante el arranque. Las especificaciones de ejemplo son 12 V en reposo y 10 V en arranque. ¿Cuántos V suman las diferencias bajo el mínimo de las dos lecturas?", "(12-10)+(10-6)", "Se calcula cuánto falta en reposo y cuánto falta en arranque, y se suman.", " V"),
        ("abc", "{F} Se compara el caso con un registro de ejemplo de otro vehículo igual, de arranque normal, que marca 11 V durante el arranque. ¿Qué aporta esa comparación?", "Muestra que 8 V es un valor anormal para ese modelo, pero no identifica la pieza responsable", "Confirma que la batería está dañada", "Confirma que el motor de arranque está dañado", "Comparar con un vehículo normal confirma que el dato es anormal, y la pieza se sigue estableciendo con verificación."),
    ],
    ctx=("abc", "Una persona propietaria te pregunta en un taller de ejemplo si «con ese 8 V ya se sabe qué pieza cambiar». Como estudiante, ¿qué respondes?", "Que el dato señala el sistema, pero la causa la confirma personal autorizado con más verificación y la especificación del fabricante", "Que sí, porque la batería siempre es la causa", "Que un dato de tensión no sirve para nada", "El dato orienta, pero no identifica una sola pieza."),
    sc=[
        ("En Mecánica Automotriz: ¿qué hace un dato que confirma una causa?", "Muestra que esa causa explica el síntoma", "Confirmar es coincidir con lo que la causa produciría."),
        ("¿Qué debe decir una buena conclusión?", "Qué se sabe y qué falta verificar", "La conclusión no debe pasarse de los datos."),
        ("¿Por qué no se cambian piezas «por si acaso»?", "Porque no se sabe cuál era la causa y el registro queda sin evidencia", "Cada decisión debe apoyarse en un dato."),
    ],
    op=("Ficha de ejemplo: síntoma escrito, «las luces de posición traseras no encienden». Registro de personal autorizado: la lámpara izquierda no enciende; la lámpara derecha no enciende; el fusible de ese circuito está abierto; las luces delanteras funcionan. Escribe (a) qué sistema se ve comprometido, (b) dos hechos del registro que lo apoyan, (c) qué no se puede concluir todavía, (d) quién debe verificar la causa.",
        "(a) El sistema de alumbrado y señalización, en su circuito de luces traseras. (b) Fallan las dos lámparas traseras a la vez y el fusible del circuito está abierto, mientras las delanteras funcionan. (c) No se puede concluir que baste reemplazar el fusible, porque un fusible se abre por una causa, como un consumo excesivo. (d) Personal autorizado, con el manual del fabricante.",
        ["nombra el sistema", "cita dos datos del registro", "indica el límite de la conclusión", "señala quién verifica"],
        ["hoja con las cuatro respuestas"],
        ["afirmar que el fusible es la causa", "no usar datos del registro", "proponer cambiar piezas al azar"],
        "Pregunta: «¿por qué se abriría el fusible?». Si no responde, pídele que relea que un dato señala el sistema y no siempre la pieza."),
    reinforce="Escribe en tres líneas un síntoma inventado, dos sistemas candidatos y un dato que descartaría a uno de ellos.",
    extend="Explica con un ejemplo por qué una conclusión puede decir «hay que verificar más» y aun así ser una buena conclusión.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (planilla de verificación de ejemplo, inventada; las lecturas las tomó personal autorizado). Especificaciones y lecturas del «Modelo Demo 2». "
     "(1) Tensión de batería en reposo: mínimo 12 V; lectura 12 V. (2) Presión de aceite en funcionamiento normal: rango de 150 a 300 kPa; lectura 120 kPa. (3) Temperatura del líquido refrigerante en funcionamiento normal: rango de 80 a 100 °C; lectura 105 °C. "
     "(4) Resistencia de un sensor de temperatura: rango de 200 a 300 Ω; lectura 250 Ω. (5) Corriente de carga del alternador: mínimo 20 A; lectura 14 A.")
build(
    O1, 4, F,
    use="Aprenderé a comparar lecturas con las especificaciones del fabricante, a decidir si cumplen, a tratar las lecturas dudosas por la resolución del instrumento y a registrar bien cada valor.",
    prior=["Sé comparar y restar números enteros.", "Sé qué es una especificación.", "Sé leer una planilla con filas y columnas."],
    explain=[
        "Una especificación puede ser un mínimo, un máximo o un rango de dos límites. Una lectura cumple si queda dentro de lo especificado, y los límites se incluyen: una lectura igual al mínimo cumple. Fuera de rango es una no conformidad y se registra aunque esté cerca del límite; no existe una tolerancia inventada por el taller. Se anota siempre el valor, la unidad, el instrumento, la fecha y quién lo tomó.",
        "Un instrumento análogo muestra la medida sobre una escala; uno digital la muestra como número. La resolución es la menor variación que el instrumento puede mostrar. En la planilla de ejemplo de esta clase se usa esta regla: si una lectura supera un límite por menos de una resolución, queda en duda y se informa para repetirla con un instrumento más fino; si lo supera por más de una resolución, es no conforme. Las unidades van junto al número: V, A, Ω, kPa y °C.",
        f"Una planilla corregida se tacha con una línea y se firma; no se borra. {EMER} {AVISO}",
    ],
    vocab=[("rango", "valores mínimo y máximo entre los que una lectura es conforme"), ("no conformidad", "lectura fuera de lo que pide la especificación"), ("resolución", "menor variación que un instrumento puede mostrar"), ("kPa", "kilopascal, unidad de presión"), ("Ω", "ohm, unidad de resistencia eléctrica"), ("A", "ampere, unidad de corriente")],
    worked=[
        ("Rango de dos límites", "Una especificación de ejemplo pide de 40 a 60 unidades y se lee 62. ¿Cumple?", ["El máximo es 60 y 62 lo supera.", "Una lectura fuera de rango no cumple."], "No cumple"),
        ("Lectura en duda", "El máximo de ejemplo es 50 y un instrumento de resolución 4 marca 51. ¿Cómo se informa?", ["51 supera el máximo por 1, menos que una resolución de 4.", "Queda en duda y se repite con un instrumento más fino."], "En duda, para repetirla"),
    ],
    mistakes=[("Aceptar una lectura fuera de rango porque está «cerca».", "No existe una tolerancia inventada: fuera de rango es no conformidad.", "Registra el valor y la diferencia con el límite."),
              ("Anotar solo el número y dejar la unidad «sobreentendida».", "Sin unidad no se sabe qué se midió ni si la comparación es válida.", "Escribe siempre la unidad junto al valor.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué es un rango de especificación?", "Los valores mínimo y máximo entre los que la lectura es conforme", "El promedio de las lecturas anteriores del vehículo", "El valor exacto que siempre debe leerse", "El rango fija dos límites; la lectura no tiene que ser un único valor."),
        ("abc", "En Mecánica Automotriz: ¿qué diferencia a un instrumento análogo de uno digital?", "El análogo muestra la medida sobre una escala y el digital la muestra como número", "El digital siempre mide sin error y el análogo no", "El análogo sirve solo para temperatura y el digital solo para tensión", "La diferencia es la forma de mostrar la medida; ambos tienen resolución limitada."),
        ("abc", "En Mecánica Automotriz: ¿qué se registra junto con cada valor medido?", "La unidad, el instrumento, la fecha y quién tomó la lectura", "Solo el número, porque la unidad se supone", "Solo el nombre del vehículo", "El registro completo permite revisar y repetir la lectura."),
        ("abc", "{F} ¿Cuál de las lecturas supera el máximo de su rango?", "La temperatura del líquido refrigerante", "La presión de aceite", "La resistencia del sensor", "105 °C supera el máximo de 100 °C; la presión está bajo su mínimo y la resistencia está dentro del rango."),
        ("abc", "{F} La tensión de batería en reposo es 12 V y su mínimo es 12 V. ¿Cumple?", "Sí, porque el límite mínimo se incluye en lo conforme", "No, porque debe superar al mínimo", "No, porque falta un máximo", "Los límites se incluyen: una lectura igual al mínimo cumple."),
        ("abc", "{F} ¿Cuál de estas lecturas se compara contra un rango de dos límites?", "La presión de aceite", "La corriente de carga del alternador", "La tensión de batería en reposo", "La presión tiene mínimo y máximo; la corriente y la tensión de reposo solo tienen mínimo."),
        ("=", "{F} ¿Cuántos kPa le faltan a la presión de aceite para llegar al mínimo de su rango?", "150-120", "Se resta la lectura al mínimo del rango.", " kPa"),
        ("=", "{F} ¿Cuántos Ω de ancho tiene el rango de la resistencia del sensor?", "300-200", "El ancho del rango es el máximo menos el mínimo.", " Ω"),
        ("abc", "{F} Otra lectura de temperatura se tomó con un instrumento análogo de resolución 2 °C y marcó 101 °C, con el mismo máximo de 100 °C. ¿Cómo se informa?", "En duda, porque supera el máximo por menos de una resolución y se repite con un instrumento más fino", "Como conforme, porque 101 está muy cerca de 100", "Como no conforme definitiva, porque supera el máximo", "La diferencia de 1 °C es menor que la resolución de 2 °C, por eso la lectura queda en duda."),
        ("abc", "{F} Un compañero dice: «las lecturas fuera de rango están cerca del límite, así que el vehículo queda conforme». ¿Qué respuesta es correcta?", "Una lectura fuera de rango es no conforme aunque esté cerca, y se registra y se informa", "Tiene razón: hasta un 10 % fuera del límite se acepta", "Tiene razón, si la persona propietaria está de acuerdo", "La tolerancia la fija el fabricante, no el taller; un 10 % inventado no existe."),
        ("abc", "En una planilla alguien anotó «temperatura: 105» y borró la unidad con corrector. ¿Qué corresponde?", "Tachar con una línea, escribir el dato correcto con su unidad y dejar firma y fecha", "Dejarlo así, porque el contexto indica °C", "Borrar toda la fila y escribir una lectura que cumpla", "Una corrección se hace visible y firmada; borrar o inventar un dato falsea el registro."),
        ("=", "{F} Para cada lectura no conforme la orden de ejemplo cobra 1 hora de revisión a $11.000 la hora. ¿Cuántos pesos cobra por las lecturas no conformes de la planilla?", "3*11000", "Hay tres lecturas no conformes: presión de aceite, temperatura y corriente de carga.", " pesos"),
        ("abc", "{F} Hay que redactar un informe breve de la planilla. ¿Qué redacción corresponde?", "Tres lecturas no conformes: presión de aceite 120 kPa (mín. 150), temperatura 105 °C (máx. 100) y corriente de carga 14 A (mín. 20); se deriva a personal autorizado", "El vehículo está dañado y hay que reparar el motor", "Todas las lecturas están bien salvo una", "El informe cita cada lectura no conforme con su valor, su límite y su unidad, y no inventa una causa."),
    ],
    ctx=("abc", "Una persona propietaria te pregunta en un taller de ejemplo por qué su vehículo «no pasa» si una lectura solo se pasó un poco del límite. ¿Qué respondes?", "Que el límite lo fija el fabricante y una lectura fuera de rango es no conforme, aunque se registra con exactitud para decidir con personal autorizado", "Que el taller puede aceptar un poco más si el trabajo fue rápido", "Que el límite solo vale para vehículos nuevos", "El rango es una referencia técnica y el taller no lo corrige por conveniencia."),
    sc=[
        ("En Mecánica Automotriz: ¿una lectura igual al mínimo cumple?", "Sí, el límite se incluye", "Los límites forman parte de lo conforme."),
        ("¿Qué es la resolución de un instrumento?", "La menor variación que puede mostrar", "Por eso una lectura cercana a un límite puede quedar en duda."),
        ("En una planilla automotriz: ¿cómo se corrige un dato mal anotado?", "Se tacha con una línea y se firma, sin borrar", "Así el registro conserva el dato original."),
    ],
    op=("Ficha de ejemplo: planilla de otro vehículo. (1) Tensión de carga con el motor funcionando: rango de 13 a 15 V; lectura 12 V. (2) Resistencia de un sensor: rango de 100 a 150 Ω; lectura 150 Ω. (3) Temperatura: máximo 90 °C; lectura 91 °C con un instrumento de resolución 2 °C. Escribe (a) si cada lectura cumple, está en duda o no cumple, (b) cuánto se aparta cada una del límite, (c) una línea de informe, (d) por qué no se nombra una pieza dañada.",
        "(a) (1) No cumple; (2) cumple, porque el límite se incluye; (3) en duda, porque supera el máximo por menos de una resolución. (b) (1) 1 V bajo el mínimo; (2) 0 Ω; (3) 1 °C sobre el máximo. (c) «Tensión de carga 12 V, bajo el mínimo de 13 V; temperatura 91 °C en duda por resolución; se derivan a personal autorizado.» (d) Porque las lecturas señalan sistemas, no una pieza confirmada.",
        ["clasifica cada lectura", "calcula las diferencias", "redacta el informe con valores y unidades", "explica el límite de la conclusión"],
        ["hoja con las clasificaciones, las diferencias y el informe"],
        ["aceptar una lectura fuera de rango", "olvidar las unidades", "nombrar una pieza como dañada"],
        "Pregunta: «¿el límite incluye su propio valor?». Si no responde, pídele que relea la regla de los límites."),
    reinforce="Inventa una especificación de ejemplo con rango y tres lecturas: una conforme, una en duda y una no conforme.",
    extend="Explica con un ejemplo por qué no se puede promediar una lectura fuera de rango con otra dentro del rango para aprobarla.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (cotizaciones y control final de ejemplo, inventadas). Para un mismo vehículo liviano el taller presenta dos alternativas sobre un conjunto del sistema de refrigeración. "
     "Alternativa A: reemplazar solo el componente sospechoso; repuesto $45.000, mano de obra 2 horas, garantía 3 meses. Alternativa B: reemplazar el conjunto completo; repuesto $90.000, mano de obra 3 horas, garantía 12 meses. Tarifa: $12.000 por hora. "
     "Lista de control final (6 puntos): 1 orden firmada; 2 repuestos con referencia correcta; 3 lecturas dentro de rango; 4 niveles de fluidos registrados; 5 residuos entregados al gestor; 6 firma de control de calidad. Estado: puntos 1 a 5 cumplidos; el 6, pendiente.")
build(
    O1, 5, F,
    use="Aprenderé a comparar dos alternativas de trabajo con costo, garantía y seguridad, y a verificar la calidad con una lista de control final y la trazabilidad de los repuestos.",
    prior=["Sé calcular un costo con horas y tarifa.", "Sé dividir números enteros.", "Sé qué es una orden de trabajo."],
    explain=[
        "Comparar alternativas no es elegir la más barata. Se mira el costo total, que suma repuestos y mano de obra, la garantía, el cumplimiento de las especificaciones del fabricante y la seguridad. Para comparar de forma justa se puede calcular el costo por mes de garantía, que es el costo total dividido por los meses de garantía. La decisión final la toma la persona propietaria con la información que entrega el taller.",
        "La garantía es el compromiso escrito de responder por el trabajo y los repuestos durante un plazo. La trazabilidad de un repuesto es poder seguir su origen y su uso mediante una referencia o lote registrados. La lista de control final verifica por escrito cada punto antes de entregar el vehículo, y se entrega solo cuando todos los puntos están cumplidos. Los residuos del trabajo se entregan a un gestor autorizado.",
        f"Esta clase compara números y documentos; el trabajo real lo hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("costo total", "suma de repuestos y mano de obra"), ("garantía", "compromiso escrito de responder por el trabajo durante un plazo"), ("trazabilidad", "poder seguir el origen y el uso de un repuesto con su referencia o lote"), ("lista de control final", "verificación escrita de cada punto antes de entregar"), ("gestor autorizado", "empresa autorizada para retirar y tratar residuos")],
    worked=[
        ("Costo por mes de garantía", "Una alternativa de ejemplo cuesta $60.000 en total y tiene garantía de 6 meses. ¿Cuánto cuesta por mes de garantía?", ["Se divide el costo total entre los meses.", "60.000 entre 6 son 10.000."], "$10.000 por mes"),
        ("Lista de control", "Una lista de ejemplo tiene 4 puntos y 3 están cumplidos. ¿Se puede entregar el vehículo?", ["Se entrega solo si todos los puntos están cumplidos.", "Falta 1 punto."], "No, hasta cumplir el punto pendiente"),
    ],
    mistakes=[("Elegir la alternativa solo por el menor precio.", "El precio no muestra la garantía, el cumplimiento de la especificación ni la seguridad.", "Compara costo total, garantía y cumplimiento de especificaciones."),
              ("Entregar el vehículo con un punto de la lista de control pendiente porque «era solo una firma».", "La verificación forma parte del trabajo y protege a la persona propietaria.", "Se completa toda la lista antes de entregar.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué es la garantía de un trabajo?", "El compromiso escrito de responder por el trabajo y los repuestos durante un plazo", "Un descuento que se aplica al precio final", "El plazo que tiene el técnico para devolver sus herramientas", "La garantía es un compromiso por un plazo; un descuento es otra cosa."),
        ("abc", "En Mecánica Automotriz: ¿para qué sirve una lista de control final?", "Para verificar por escrito que se cumplió cada punto antes de entregar el vehículo", "Para listar los repuestos que se queda el taller", "Para fijar la tarifa por hora del próximo trabajo", "La lista deja constancia de que cada verificación se hizo."),
        ("abc", "En Mecánica Automotriz: ¿qué es la trazabilidad de un repuesto?", "Poder seguir su origen y su uso mediante una referencia o lote registrados", "La rapidez con que llega a la bodega", "El precio que pagó el taller por él", "La trazabilidad permite saber de dónde viene y dónde se usó."),
        ("abc", "{F} ¿Qué punto de la lista de control final está pendiente?", "La firma de control de calidad", "La entrega de residuos al gestor", "La referencia correcta de los repuestos", "El estado indica que cumplieron los puntos 1 a 5 y que falta el 6."),
        ("abc", "{F} Según la lista, ¿se puede entregar ya el vehículo?", "No, porque falta el punto 6 y se entrega cuando todos estén cumplidos", "Sí, porque 5 de 6 puntos son una mayoría suficiente", "Sí, porque el punto pendiente es solo una firma", "La regla pide todos los puntos cumplidos, no una mayoría."),
        ("abc", "{F} ¿Qué punto de la lista muestra el cuidado ambiental del taller?", "La entrega de residuos al gestor", "Las lecturas dentro de rango", "La orden firmada", "Entregar residuos a un gestor autorizado es una práctica ambiental."),
        ("=", "{F} ¿Cuántos pesos cuesta en total la alternativa A, entre repuesto y mano de obra?", "45000+2*12000", "Se suma el repuesto con las horas multiplicadas por la tarifa.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta en total la alternativa B que la A?", "(90000+3*12000)-(45000+2*12000)", "Se calcula el costo total de cada una y se restan.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta por mes de garantía la alternativa B?", "(90000+3*12000)//12", "Se divide el costo total de B entre sus 12 meses de garantía.", " pesos"),
        ("abc", "{F} Un compañero dice: «la alternativa A es mejor porque es más barata». ¿Qué observación es correcta?", "No necesariamente: por mes de garantía A cuesta más que B, y la decisión depende también de la especificación y la seguridad", "Tiene razón: lo más barato siempre es lo mejor", "Se equivoca: lo más caro siempre es lo mejor", "Por mes de garantía A cuesta 23.000 y B 10.500; ni lo barato ni lo caro es siempre mejor."),
        ("abc", "El jefe de un taller de ejemplo pide entregar hoy un vehículo con el control de calidad pendiente porque la persona propietaria tiene apuro. ¿Qué corresponde?", "Completar el control antes de entregar y explicar el motivo", "Entregar y completar la firma mañana", "Firmar el control sin verificar para cumplir el plazo", "La verificación es parte del trabajo y no se salta por apuro."),
        ("=", "{F} Si se elige B y el taller descuenta $6.000 de la mano de obra, ¿cuánto es cada cuota si se paga en 3 cuotas iguales?", "(90000+3*12000-6000)//3", "Se calcula el total con descuento y se divide entre 3.", " pesos"),
        ("abc", "{F} Una persona propone elegir la alternativa solo por el menor tiempo de entrega. ¿Qué criterio falta considerar?", "El costo total, la garantía, el cumplimiento de las especificaciones y la seguridad", "Ninguno, porque el tiempo es el único criterio técnico", "Solo la marca del repuesto", "Una decisión técnica considera varios criterios, no solo la rapidez."),
    ],
    ctx=("abc", "Una persona propietaria te pide en un taller de ejemplo que le entregues el vehículo «sin anotar nada, para ahorrar papeleo». ¿Qué respondes?", "Que el registro de lo hecho, las lecturas y la garantía son parte del trabajo y protegen a ambas partes, así que se anotan", "Que sí, si paga al contado", "Que sí, siempre que el trabajo haya sido pequeño", "Sin registro no hay trazabilidad ni garantía."),
    sc=[
        ("En Mecánica Automotriz: ¿cómo se calcula el costo por mes de garantía?", "Se divide el costo total entre los meses de garantía", "Permite comparar alternativas con plazos distintos."),
        ("¿Cuándo se entrega el vehículo según la lista de control final?", "Cuando todos los puntos están cumplidos", "Un punto pendiente impide la entrega."),
        ("¿Qué es un gestor autorizado?", "Una empresa autorizada para retirar y tratar residuos", "El taller entrega los residuos a quien está autorizado."),
    ],
    op=("Ficha de ejemplo: para otro vehículo liviano, la alternativa X cuesta en repuestos $30.000, lleva 1 hora de mano de obra y tiene garantía de 2 meses; la alternativa Y cuesta en repuestos $50.000, lleva 2 horas y tiene garantía de 10 meses. Tarifa: $10.000 por hora. Escribe (a) el costo total de cada una, (b) el costo por mes de garantía de cada una, (c) un criterio no numérico que también deba mirarse, (d) cuál es el último punto antes de entregar el vehículo.",
        "(a) X: 30.000 + 1 × 10.000 = 40.000; Y: 50.000 + 2 × 10.000 = 70.000. (b) X: 40.000 ÷ 2 = 20.000 por mes; Y: 70.000 ÷ 10 = 7.000 por mes. (c) El cumplimiento de la especificación del fabricante o la seguridad. (d) La verificación final: la lista de control completa con la firma de control de calidad.",
        ["calcula los costos totales", "calcula el costo por mes", "nombra un criterio no numérico", "indica el último punto de entrega"],
        ["hoja con los cálculos y las dos respuestas escritas"],
        ["elegir solo por precio", "calcular mal el costo por mes", "omitir la verificación final"],
        "Pregunta: «¿cuántos meses cubre cada garantía?». Si no responde, pídele que relea cómo se calcula el costo por mes."),
    reinforce="Inventa dos alternativas con costo y garantía, y calcula cuál tiene el menor costo por mes de garantía.",
    extend="Explica con un ejemplo por qué la alternativa con menor costo por mes de garantía puede no ser la que conviene a una persona.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (índice de un manual de servicio de ejemplo, inventado). Manual de servicio del «Modelo Demo 4», edición 2. Secciones: Generalidades, páginas 1 a 20; Motor, 21 a 140; Refrigeración y lubricación, 141 a 190; Sistema eléctrico, 191 a 300; Transmisión, 301 a 380; Carrocería, 381 a 430. "
     "Aparte existe el boletín técnico BT-07, posterior a la edición 2, que corrige una especificación del sistema eléctrico.")
build(
    O2, 1, F,
    use="Aprenderé qué documentos usa un taller automotriz, para qué sirve cada uno, qué riesgo hay en usar el equivocado y qué son las normas de emisiones.",
    prior=["Sé leer un índice con páginas.", "Sé sumar y restar números enteros.", "Sé que un vehículo tiene un fabricante y un modelo."],
    explain=[
        "El manual de usuario orienta a la persona propietaria. El manual de servicio, o de taller, entrega al personal técnico las especificaciones, los diagramas y las instrucciones del fabricante. Un boletín técnico es un documento posterior que corrige o complementa un manual. Los planos y diagramas muestran circuitos o conjuntos con símbolos. Los manuales reales tienen derechos de autor: aquí solo se usan índices y tablas inventados.",
        "Cada manual corresponde a un modelo, una edición, un motor y un rango de años. Usar el manual de otro modelo o una edición superada lleva a leer especificaciones que no corresponden al vehículo. La referencia vigente es la edición más reciente más sus boletines; si un boletín y el manual difieren, manda el boletín. Las normas de emisiones, nacionales e internacionales, fijan los límites de gases y partículas que puede emitir un vehículo, y cambian según el país, el tipo de motor y la fecha de fabricación.",
        f"Las autoridades de transporte y de medio ambiente fijan y fiscalizan esos límites según la norma vigente. El jefe de taller controla qué ediciones hay a la vista. {EMER} {AVISO}",
    ],
    vocab=[("manual de usuario", "documento que orienta a la persona propietaria"), ("manual de servicio", "documento técnico del fabricante para el taller"), ("boletín técnico", "documento posterior que corrige o complementa un manual"), ("edición", "versión de un manual"), ("norma de emisiones", "regla que fija los límites de gases y partículas de un vehículo"), ("diagrama", "dibujo con símbolos que muestra un circuito o un conjunto")],
    worked=[
        ("Contar páginas", "Un índice de ejemplo dice: Climatización, páginas 55 a 90. ¿Cuántas páginas tiene la sección, contando la primera y la última?", ["Se resta la primera página a la última: 90 menos 55 son 35.", "Se suma 1 para incluir la primera página: 36."], "36 páginas"),
        ("Rango de años", "Un manual de ejemplo dice: «Modelo Z, años 3 a 5». Un vehículo es un Modelo Z del año 7. ¿El manual le corresponde?", ["Se compara el año 7 con el rango de 3 a 5.", "El año 7 está fuera del rango: el manual no le corresponde."], "No le corresponde"),
    ],
    mistakes=[("Usar el manual de otro modelo porque «son parecidos».", "Las especificaciones cambian según modelo, motor y año.", "Confirma modelo, edición y motor antes de leer una cifra."),
              ("Dar por válido el manual y olvidar los boletines.", "Un boletín posterior puede corregir una especificación.", "La referencia vigente es la edición más reciente más sus boletines.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué diferencia hay entre el manual de usuario y el manual de servicio?", "El de usuario orienta a la persona propietaria y el de servicio entrega datos técnicos al personal del taller", "El de usuario trae las especificaciones técnicas completas y el de servicio es una guía de uso diario", "Son el mismo documento con distinta portada", "El manual de servicio es técnico y es el de uso del taller; el de usuario es para quien conduce o es propietario."),
        ("abc", "En Mecánica Automotriz: ¿qué es un boletín técnico?", "Un documento del fabricante que corrige o complementa un manual después de su edición", "Una lista de precios de repuestos", "Un aviso del taller sobre sus horarios de atención", "El boletín actualiza la información técnica; no es una lista de precios ni un aviso interno."),
        ("abc", "En Mecánica Automotriz: ¿qué fija una norma de emisiones?", "Los límites de gases y partículas que puede emitir un vehículo", "El consumo máximo de combustible que debe declarar el taller", "La cantidad de repuestos que debe tener una bodega", "Una norma de emisiones regula lo que sale por el escape, no el consumo declarado ni las bodegas."),
        ("abc", "{F} Una persona busca información sobre un fusible. ¿En qué sección del manual la encuentra?", "En Sistema eléctrico", "En Generalidades", "En Transmisión", "Un fusible forma parte del sistema eléctrico; Generalidades es introductoria y Transmisión es otro sistema."),
        ("abc", "{F} El boletín BT-07 es posterior a la edición 2 y corrige una especificación eléctrica. ¿Qué valor se usa para esa especificación?", "El del boletín, porque es posterior y corrige el manual", "El del manual, porque es el documento más completo", "El promedio entre ambos valores", "Un boletín posterior corrige el manual y no se promedian dos valores."),
        ("ab", "{F} Una persona del taller consulta el manual de otro modelo en lugar del «Modelo Demo 4». ¿Qué riesgo tiene?", "Leer especificaciones que no corresponden al vehículo", "Ninguno, porque todos los modelos de una marca comparten las mismas especificaciones", "Las especificaciones cambian según modelo, motor y año; usar otro manual lleva a valores equivocados."),
        ("=", "{F} ¿Cuántas páginas tiene la sección Motor, contando la primera y la última?", "140-21+1", "Se resta la primera página a la última y se suma 1 para incluir la primera.", " páginas"),
        ("=", "{F} Una persona imprime solo las secciones Refrigeración y lubricación y Sistema eléctrico. ¿Cuántas páginas imprime?", "(190-141+1)+(300-191+1)", "Se cuentan las páginas de cada sección, con la primera incluida, y se suman.", " páginas"),
        ("=", "{F} Un técnico lee las secciones Generalidades y Transmisión completas a un ritmo de 10 páginas por hora. ¿Cuántas horas necesita?", "((20-1+1)+(380-301+1))//10", "Se suman las páginas de las dos secciones y se divide entre las páginas por hora.", " horas"),
        ("abc", "{F} Un técnico dice: «ese manual es la edición 2, ya no sirve, me guío por lo que recuerdo del modelo anterior». ¿Qué respuesta es correcta?", "No corresponde: la edición vigente más sus boletines es la referencia y la memoria de otro modelo no la reemplaza", "Corresponde, porque la experiencia vale más que el documento", "Corresponde, porque una edición con boletín queda anulada por completo", "Un boletín corrige una especificación, no anula todo el manual, y la memoria no es un documento."),
        ("abc", "En un taller de ejemplo hay dos copias del mismo manual con ediciones distintas. ¿Qué hace el jefe de taller?", "Retira la edición superada y deja a la vista la vigente con sus boletines", "Deja las dos para que cada técnico elija la que prefiera", "Guarda solo la más antigua porque es la original", "El control de ediciones evita que se usen valores superados."),
        ("=", "{F} Se agrega al manual un anexo de 25 páginas después de la última página de Carrocería. ¿Cuántas páginas tiene ahora el manual?", "430+25", "El manual llega hasta la página 430 y se suman las 25 del anexo.", " páginas"),
        ("abc", "Un taller de ejemplo debe elegir qué norma de emisiones aplica a un vehículo. ¿Qué datos del vehículo necesita?", "El año o la fecha de fabricación, el tipo de motor y combustible, y la norma vigente del país", "Solo el color y el nombre del modelo", "Solo el kilometraje recorrido", "La norma depende de la fecha, el motor, el combustible y el país; el color o el kilometraje no la definen."),
    ],
    ctx=("abc", "Una persona propietaria te muestra una página de internet con un valor de especificación distinto al del manual de servicio de un taller de ejemplo. ¿Qué respondes?", "Que la fuente es el manual vigente del fabricante con sus boletines, y que el valor de la página no se usa sin verificar su origen", "Que se usa el valor de la página, porque es más nuevo", "Que se usa el promedio de ambos valores", "Una fuente sin origen verificable no reemplaza el documento del fabricante."),
    sc=[
        ("En Mecánica Automotriz: ¿qué manual usa el taller para consultar especificaciones técnicas?", "El manual de servicio del fabricante", "Ese manual trae los datos técnicos para el personal del taller."),
        ("¿Qué manda si un boletín posterior y el manual difieren?", "El boletín", "El boletín corrige lo que el manual dice."),
        ("¿De qué depende la norma de emisiones aplicable a un vehículo?", "Del país, el tipo de motor y la fecha de fabricación", "Esos datos definen qué límites corresponden."),
    ],
    op=("Ficha de ejemplo: índice de otro manual de servicio. Generalidades, páginas 1 a 15; Motor, 16 a 110; Sistema eléctrico, 111 a 200. El boletín BT-02, posterior a la edición, corrige una especificación del motor. Escribe (a) en qué sección buscas la especificación del motor y cuántas páginas tiene, (b) qué documento manda si difiere del manual, (c) un riesgo de usar el manual de otro modelo, (d) quién controla qué ediciones están a la vista.",
        "(a) En la sección Motor, que tiene 110 − 16 + 1 = 95 páginas. (b) El boletín BT-02, porque es posterior y corrige. (c) Leer especificaciones que no corresponden al vehículo. (d) El jefe de taller.",
        ["ubica la sección y cuenta las páginas", "indica qué documento manda", "nombra un riesgo", "identifica el rol"],
        ["hoja con las cuatro respuestas"],
        ["contar mal las páginas por no incluir la primera", "preferir el manual al boletín", "decir que cada técnico elige la edición"],
        "Pregunta: «¿qué documento es posterior?». Si no responde, pídele que relea qué es un boletín técnico."),
    reinforce="Inventa un índice de tres secciones con sus páginas y calcula cuántas páginas tiene cada una.",
    extend="Explica con un ejemplo por qué un manual correcto puede dar un valor equivocado para un vehículo.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (leyenda y diagrama de ejemplo, inventados, del «Modelo Demo 4»). Símbolos: BAT = batería; FUS = fusible; INT = interruptor; LAM = lámpara; MASA = retorno a la carrocería. Colores de cable de ejemplo: R = rojo, alimentación; N = negro, masa; A = amarillo, señal. "
     "Abreviaturas de ejemplo: ECU = unidad de control electrónica; MT = transmisión manual; AT = transmisión automática. Circuito de una luz: BAT, FUS (10 A), INT, LAM y MASA, en ese orden. La lámpara es de 60 W y el sistema es de 12 V.")
build(
    O2, 2, F,
    use="Aprenderé a leer la leyenda de un diagrama eléctrico, a seguir el camino de la corriente y a calcular la corriente normal de una lámpara para juzgar si el fusible es adecuado.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé qué es una batería y un interruptor.", "Sé leer una lista ordenada."],
    explain=[
        "Un diagrama eléctrico usa símbolos, colores de cable y abreviaturas que se explican en su leyenda. Los colores y las abreviaturas los define cada fabricante: se lee siempre la leyenda del mismo manual. El diagrama se lee siguiendo el camino de la corriente, desde la alimentación (la batería) pasando por el fusible, el interruptor y la carga (la lámpara) hasta el retorno a la masa.",
        "El fusible es un componente que se abre y corta el circuito si pasa más corriente de la prevista; protege al circuito. El relé es un interruptor accionado eléctricamente que permite gobernar una corriente grande con una corriente pequeña. La potencia en watts (W) es la tensión en volts (V) por la corriente en amperes (A), por lo que la corriente es la potencia dividida por la tensión. Si un fusible es mayor que la corriente normal, deja margen; si es mucho mayor, ya no protege bien.",
        f"Los diagramas se leen en papel; intervenir un circuito real es tarea de personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("leyenda", "explicación de los símbolos, colores y abreviaturas de un diagrama"), ("fusible", "componente que se abre si pasa más corriente de la prevista"), ("relé", "interruptor accionado eléctricamente"), ("carga", "componente que consume energía, como una lámpara"), ("masa", "retorno de la corriente a la carrocería"), ("potencia", "tensión por corriente, en watts (W)")],
    worked=[
        ("Leer una leyenda", "Una leyenda de ejemplo dice: SEN = sensor; ACT = actuador. Un diagrama anota «SEN, ECU, ACT». ¿Qué componente recibe la señal del sensor?", ["El orden indica que el sensor envía su señal al siguiente componente.", "Después de SEN viene ECU."], "La ECU"),
        ("Interruptor abierto", "Un diagrama de ejemplo muestra BAT, INT, LAM y MASA. Con INT abierto, ¿qué ocurre con LAM?", ["El interruptor abierto interrumpe el camino de la corriente.", "Sin corriente, la lámpara no enciende."], "LAM queda sin corriente"),
    ],
    mistakes=[("Suponer que el amarillo significa lo mismo en todos los diagramas.", "Los colores los define cada fabricante en su leyenda.", "Lee la leyenda del mismo manual antes de interpretar colores."),
              ("Cambiar un fusible por uno mucho mayor «para que no se abra».", "Un fusible mucho mayor deja de proteger el circuito.", "El fusible lo define el fabricante según la corriente del circuito.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿para qué sirve la leyenda de un diagrama eléctrico?", "Explica los símbolos, colores y abreviaturas que usa ese diagrama", "Indica el precio de cada componente del circuito", "Reemplaza a la orden de trabajo", "La leyenda es la clave de lectura del diagrama; no trae precios ni órdenes."),
        ("abc", "En Mecánica Automotriz: ¿qué función cumple un fusible en un circuito?", "Se abre y corta el circuito cuando pasa más corriente de la prevista", "Aumenta la tensión para que el circuito funcione mejor", "Guarda energía para cuando se apague el motor", "El fusible protege al circuito abriéndose; no eleva la tensión ni guarda energía."),
        ("abc", "En Mecánica Automotriz: ¿qué es un relé?", "Un interruptor accionado eléctricamente que gobierna una corriente grande con una pequeña", "Un sensor que mide la temperatura", "Un cable de color rojo que alimenta todo el circuito", "El relé es un interruptor accionado eléctricamente; no mide ni es un cable."),
        ("abc", "{F} En el circuito de luz de la ficha, ¿qué componente está inmediatamente después del fusible?", "El interruptor", "La lámpara", "La masa", "El orden de la ficha es BAT, FUS, INT, LAM y MASA."),
        ("abc", "{F} ¿Para qué sirve el fusible de 10 A de ese circuito?", "Para proteger el circuito de una corriente mayor a la prevista", "Para encender la lámpara", "Para conectar el circuito a la carrocería", "El fusible protege y no enciende cargas; la conexión a la carrocería es la masa."),
        ("abc", "{F} ¿Cuál es el camino de la corriente del circuito, desde la alimentación hasta el retorno?", "BAT, FUS, INT, LAM y MASA", "BAT, INT, FUS, MASA y LAM", "MASA, LAM, INT, FUS y BAT", "La corriente sale de la batería, pasa por el fusible, el interruptor y la lámpara y vuelve por la masa."),
        ("=", "{F} ¿Cuántos A consume normalmente la lámpara del circuito?", "60//12", "La corriente es la potencia dividida por la tensión.", " A"),
        ("=", "Otra lámpara de ejemplo consume 36 W a 12 V y se protege con un fusible de 10 A. ¿Cuántos A de margen hay entre el fusible y su corriente normal?", "10-36//12", "Se calcula la corriente normal y se resta al valor del fusible.", " A"),
        ("=", "Un circuito de ejemplo lleva dos lámparas de 48 W cada una, conectadas directamente a la alimentación de 12 V, de modo que sus corrientes se suman. ¿Cuántos A normales pasan por el fusible?", "(48+48)//12", "Se suman las potencias y se divide entre la tensión.", " A"),
        ("abc", "{F} Si el fusible del circuito de la ficha se abre por exceso de corriente, ¿qué ocurre con la lámpara?", "Queda sin corriente, porque el fusible abierto interrumpe el camino", "Enciende más fuerte, porque la corriente busca otro camino", "Enciende igual, mientras el interruptor siga cerrado", "Un fusible abierto corta el circuito entero, aunque el interruptor esté cerrado."),
        ("abc", "Un técnico lee un diagrama de otro fabricante y asume que la abreviatura «MT» significa lo mismo que en la ficha. ¿Qué observación es correcta?", "Debe consultar la leyenda de ese diagrama, porque las abreviaturas y los colores varían según el fabricante", "Es correcta: las abreviaturas son iguales en todos los manuales", "Es correcta, si la abreviatura tiene dos letras", "Cada fabricante define su leyenda; asumir un significado puede llevar a un error."),
        ("=", "Un circuito de ejemplo tiene tres lámparas de 24 W cada una, conectadas directamente a la alimentación de 12 V y protegidas por un fusible de 10 A. ¿Cuántos A de margen hay respecto a la corriente normal?", "10-(3*24)//12", "Se calcula la corriente normal sumando las potencias y se resta al fusible.", " A"),
        ("abc", "{F} Se agrega una segunda lámpara de 36 W, conectada directamente a la alimentación de 12 V, al circuito de la ficha. ¿Qué conclusión es correcta?", "El fusible de 10 A sigue siendo adecuado, porque la corriente normal de 8 A no lo supera", "El fusible se abrirá siempre, porque se sumó una lámpara", "Hay que subir el fusible a 30 A para tener más margen", "Las corrientes de 5 A y 3 A suman 8 A, que está bajo los 10 A; un fusible mucho mayor ya no protegería bien."),
    ],
    ctx=("abc", "Un compañero de curso te muestra un diagrama sin leyenda y dice: «el cable amarillo es de alimentación, eso es igual en todos». ¿Qué respondes?", "Que sin leyenda no se puede asegurar, porque cada fabricante define sus colores, y que se pide el documento completo", "Que sí, porque el amarillo siempre es de alimentación", "Que se adivina por el grosor del cable", "Los colores y las abreviaturas están definidos en la leyenda de cada manual."),
    sc=[
        ("En Mecánica Automotriz: ¿cómo se calcula la corriente normal de una lámpara?", "Se divide la potencia entre la tensión", "Potencia, tensión y corriente se relacionan en P = V × I."),
        ("¿Qué hace un interruptor abierto en un circuito?", "Interrumpe el camino de la corriente", "Sin camino cerrado no hay corriente."),
        ("¿Dónde se explica el significado de un color de cable?", "En la leyenda del mismo manual", "Cada fabricante define sus propios colores y símbolos."),
    ],
    op=("Ficha de ejemplo: leyenda: BOC = bocina; REL = relé; INT = interruptor. Circuito de la bocina: BAT, FUS (10 A), INT, REL, BOC y MASA, en ese orden. La bocina consume 48 W con 12 V. Escribe (a) qué significa BOC, (b) qué componente va inmediatamente después del interruptor, (c) la corriente normal de la bocina y el margen respecto al fusible, (d) qué haces si una abreviatura no está en la leyenda.",
        "(a) Bocina. (b) El relé. (c) 48 ÷ 12 = 4 A; el margen es 10 − 4 = 6 A. (d) Consultar la leyenda del mismo manual o pedir el documento completo, sin suponer su significado.",
        ["traduce la abreviatura con la leyenda", "indica el componente que sigue en el circuito", "calcula la corriente y el margen", "no supone significados"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "olvidar la unidad", "suponer el significado de una abreviatura"],
        "Pregunta: «¿potencia entre tensión o tensión entre potencia?». Si duda, pídele que relea la relación entre watts, volts y amperes."),
    reinforce="Inventa un circuito de cinco componentes en orden y escribe el camino de la corriente de la alimentación a la masa.",
    extend="Explica con un ejemplo por qué un fusible mucho mayor que la corriente normal no protege bien el circuito.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Vehículo «Modelo Demo 5». Personal autorizado informa que la unidad de control guardó el código de ejemplo Z-205. Tabla del manual de ejemplo: Z-101, señal del sensor de temperatura fuera de rango; Z-205, señal del sensor de oxígeno sin variación; Z-310, circuito de la bomba de combustible abierto. "
     "Nota del manual: «un código indica el circuito o la señal afectados; no identifica por sí solo la pieza defectuosa». Registro de gases de ejemplo: CO = 5 unidades (límite de ejemplo: 2); hidrocarburos = 150 unidades (límite de ejemplo: 200).")
build(
    O2, 3, F,
    use="Aprenderé a interpretar un código de falla con la tabla del manual, a comparar un registro de gases con los límites de ejemplo y a escribir una conclusión que no se pase de los datos.",
    prior=["Sé qué es un síntoma.", "Sé comparar y restar números enteros.", "Sé que una norma fija límites."],
    explain=[
        "La unidad de control electrónica (ECU) vigila sensores y actuadores y guarda un código de falla (DTC) cuando una señal sale de lo esperado. La tabla del manual traduce el código a una descripción. El sensor de oxígeno informa sobre los gases del escape para controlar la mezcla de aire y combustible que entra al motor, y con ella las emisiones. Un código indica el circuito o la señal afectados, pero por sí solo no identifica la pieza defectuosa.",
        "Un registro de gases se compara con los límites de la norma vigente: el valor medido no debe superar el límite, y un valor igual al límite cumple. Se informa cada gas con su valor, su límite y su diferencia. Las normas de emisiones se aplican al vehículo según su país, motor y fecha; no se elige la de otro país por conveniencia.",
        f"Los gases se miden solo con equipos autorizados, en lugares ventilados y por personal capacitado; aquí solo se leen registros. {EMER} {AVISO}",
    ],
    vocab=[("unidad de control (ECU)", "computador del vehículo que vigila sensores y actuadores"), ("código de falla (DTC)", "código que guarda la unidad de control cuando una señal sale de lo esperado"), ("sensor de oxígeno", "sensor que informa sobre los gases del escape"), ("límite de emisiones", "valor máximo de un gas que la norma permite"), ("hidrocarburos", "restos de combustible sin quemar que salen por el escape")],
    worked=[
        ("Leer un código", "Una tabla de ejemplo dice: Z-410, circuito del ventilador abierto. Un vehículo guarda Z-410. ¿Qué indica?", ["La tabla traduce el código a una descripción.", "Indica un problema en el circuito del ventilador, sin decir qué pieza falla."], "Un circuito del ventilador abierto, sin pieza identificada"),
        ("Comparar con un límite", "El límite de ejemplo de un gas es 6 unidades y el registro dice 8. ¿Cuántas unidades lo supera?", ["Se resta el límite al registro.", "8 menos 6 son 2."], "Lo supera en 2 unidades"),
    ],
    mistakes=[("Decir que el código «nombra» la pieza que hay que cambiar.", "El código señala la señal o el circuito afectados, no la pieza.", "Escribe qué circuito indica y qué verificación falta."),
              ("Buscar la norma de emisiones de otro país por tener límites más fáciles.", "La norma se aplica según el país, el motor y la fecha del vehículo.", "Usa la norma vigente que corresponde al vehículo.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué es un código de falla (DTC)?", "Un código que guarda la unidad de control e indica el circuito o la señal afectados", "El número de serie de la pieza dañada", "La orden de reparación impresa por el taller", "El código lo genera la unidad de control; no es un número de serie ni una orden."),
        ("abc", "En Mecánica Automotriz: ¿un código de falla identifica por sí solo la pieza defectuosa?", "No, indica el circuito o la señal afectados y hay que verificar más", "Sí, siempre señala la pieza que se debe cambiar", "Sí, pero solo en vehículos nuevos", "El código orienta hacia un circuito; la pieza se establece con verificación."),
        ("abc", "En Mecánica Automotriz: ¿qué es un límite de emisiones?", "El valor máximo de un gas que la norma permite que emita el vehículo", "La cantidad mínima de combustible que debe consumir", "El kilometraje máximo que puede recorrer el vehículo", "El límite acota lo que sale por el escape y no el combustible ni el kilometraje."),
        ("abc", "{F} ¿Qué indica el código Z-205 según la tabla del manual?", "Que la señal del sensor de oxígeno no varía", "Que el circuito de la bomba de combustible está abierto", "Que la señal del sensor de temperatura está fuera de rango", "La tabla asocia Z-205 a la señal del sensor de oxígeno sin variación."),
        ("abc", "{F} ¿Con qué función se relaciona el código Z-205?", "Con el control de la mezcla y de las emisiones", "Con el alumbrado del vehículo", "Con la refrigeración del motor", "El sensor de oxígeno informa sobre los gases del escape para controlar mezcla y emisiones."),
        ("abc", "{F} ¿Cuál de los dos gases del registro supera su límite?", "El CO", "Los hidrocarburos", "Ambos gases", "El CO marca 5 sobre un límite de 2; los hidrocarburos marcan 150 bajo un límite de 200."),
        ("=", "{F} ¿Cuántas unidades supera el CO a su límite?", "5-2", "Se resta el límite al valor registrado.", " unidades"),
        ("=", "{F} ¿Cuántas unidades le faltan a los hidrocarburos para llegar a su límite?", "200-150", "Se resta el valor registrado al límite.", " unidades"),
        ("abc", "{F} ¿Cómo se informa el registro de gases?", "El CO no cumple su límite y los hidrocarburos sí cumplen", "Ambos cumplen porque los hidrocarburos cumplen", "Ninguno cumple porque uno no cumple", "Cada gas se compara con su propio límite y se informa por separado."),
        ("abc", "{F} Un compañero dice: «el código Z-205 dice sensor de oxígeno, así que hay que cambiar el sensor de oxígeno». ¿Qué respuesta es correcta?", "El código indica la señal afectada; la causa puede estar en el sensor, su cableado u otra condición, y se verifica antes de decidir", "Es correcto, porque el código nombra la pieza", "Es incorrecto, porque los códigos no sirven", "La nota del manual aclara que el código no identifica por sí solo la pieza."),
        ("abc", "Un taller de ejemplo quiere decidir si un vehículo cumple la norma de emisiones usando la tabla de límites de otro país. ¿Qué corresponde?", "Usar la norma vigente que corresponde al vehículo y a su país", "Usar la más exigente de cualquier país", "Usar la de otro país si sus límites son más fáciles de cumplir", "La norma aplicable depende del país, el motor y la fecha del vehículo, y no se elige por conveniencia."),
        ("=", "{F} Un segundo vehículo de ejemplo registra CO = 5 e hidrocarburos = 250 con los mismos límites. ¿Cuántas unidades suman las diferencias sobre los límites?", "(5-2)+(250-200)", "Se calcula cuánto supera cada gas su límite y se suman.", " unidades"),
        ("abc", "{F} Tras una verificación de personal autorizado, el registro del vehículo de la ficha cambia a CO = 2 e hidrocarburos = 150. ¿Qué informe corresponde?", "Ambos gases cumplen sus límites de ejemplo, porque 2 no supera 2 y 150 no supera 200", "El CO no cumple, porque debe ser menor que 2", "No se puede informar sin cambiar el sensor de oxígeno", "Un valor igual al límite cumple, y los hidrocarburos están bajo su límite."),
    ],
    ctx=("abc", "Una persona propietaria de un taller de ejemplo pide que se «borre el código» de la unidad de control para que se apague la luz de aviso. ¿Qué respondes?", "Que borrar el código no resuelve la causa y puede ocultar información; se registra y se informa a personal autorizado", "Que sí, porque con la luz apagada el vehículo cumple", "Que sí, siempre que lo haga una persona conocida", "Borrar el código oculta información y no corrige la causa del problema."),
    sc=[
        ("En Mecánica Automotriz: ¿qué guarda la unidad de control cuando una señal sale de lo esperado?", "Un código de falla", "El código registra la señal o el circuito afectados."),
        ("¿Un valor igual al límite de emisiones cumple?", "Sí", "El límite se incluye en lo conforme."),
        ("¿Qué informa el sensor de oxígeno?", "Los gases del escape, para controlar mezcla y emisiones", "Por eso se relaciona con las emisiones."),
    ],
    op=("Ficha de ejemplo: tabla del manual: Z-440, señal del sensor de posición del pedal fuera de rango. Registro de gases de ejemplo: CO = 1 unidad (límite 2); hidrocarburos = 210 unidades (límite 200). Escribe (a) qué indica el código Z-440, (b) qué no dice el código, (c) si cada gas cumple y cuánto se aparta del límite, (d) quién verifica la causa.",
        "(a) Que la señal del sensor de posición del pedal sale de rango. (b) No dice cuál es la pieza defectuosa. (c) El CO cumple (1 no supera 2, queda 1 unidad bajo el límite); los hidrocarburos no cumplen (210 supera 200 por 10 unidades). (d) Personal autorizado, con el manual del fabricante.",
        ["traduce el código con la tabla", "indica lo que el código no dice", "compara cada gas con su límite", "señala quién verifica"],
        ["hoja con las cuatro respuestas"],
        ["afirmar que el sensor está dañado", "no comparar cada gas por separado", "calcular mal la diferencia"],
        "Pregunta: «¿el código dice qué pieza falla?». Si responde que sí, pídele que relea la nota del manual de la ficha."),
    reinforce="Inventa una tabla de tres códigos con su descripción y escribe qué dice y qué no dice uno de ellos.",
    extend="Explica con un ejemplo por qué es peligroso borrar un código de falla sin investigar su causa.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (tabla de especificaciones de ejemplo, inventada). Manual del «Modelo Demo 6», edición 3. Capacidad de aceite del motor y límite de CO según motor y años (el año 1 es el primero de fabricación del modelo; unidades de ejemplo). "
     "Motor M1, años 1 a 3: aceite 4 L, límite de CO 4. Motor M1, años 4 a 6: aceite 4 L, límite de CO 2. Motor M2, años 1 a 3: aceite 5 L, límite de CO 3. Motor M2, años 4 a 6: aceite 5 L, límite de CO 1. "
     "Vehículos del taller: V1, motor M1, año 5, CO medido 2; V2, motor M2, año 2, CO medido 4; V3, motor M2, año 5, CO medido 1.")
build(
    O2, 4, F,
    use="Aprenderé a elegir la fila correcta de una tabla con dos datos de entrada, a aplicar el límite de emisiones que corresponde y a escribir un informe con el valor, el límite y la diferencia.",
    prior=["Sé leer una tabla de doble entrada.", "Sé comparar y restar números enteros.", "Sé que 1 L son 1.000 mL."],
    explain=[
        "Una tabla de especificaciones puede depender de dos datos, por ejemplo el motor y el rango de años del vehículo. Para elegir la fila se hacen coincidir ambos datos: no se toma la primera fila ni la de valores más altos. Una norma más reciente suele traer límites más bajos, porque exige menos contaminación a los vehículos fabricados después de cierta fecha.",
        "El informe de una lectura de emisiones anota el valor medido, el límite aplicado, la diferencia y la fila o norma usada. Una lectura igual al límite cumple. La reducción porcentual entre dos límites es la diferencia por 100 dividida por el valor anterior. Las capacidades de aceite se expresan en litros (L); 1 L equivale a 1.000 mililitros (mL).",
        f"Esta clase lee tablas y calcula; no enseña a intervenir un motor ni a medir gases. {EMER} {AVISO}",
    ],
    vocab=[("tabla de doble entrada", "tabla donde la fila depende de dos datos"), ("capacidad de aceite", "volumen de aceite que lleva un motor según su especificación"), ("reducción porcentual", "diferencia por 100 dividida por el valor anterior"), ("informe de lectura", "texto que anota valor, límite, diferencia y fila usada"), ("litro (L)", "unidad de volumen; 1 L son 1.000 mL")],
    worked=[
        ("Elegir la fila", "Tabla de ejemplo: motor Q, años 1 y 2, límite 6; motor Q, años 3 a 5, límite 4. Un vehículo con motor Q y año 3 tiene que cumplir ¿qué límite?", ["Se busca el motor Q y el rango de años que contiene el año 3.", "Es la fila de años 3 a 5."], "Límite 4"),
        ("Aceite de una flota", "Tres vehículos de ejemplo llevan 6 L de aceite cada uno. ¿Cuántos L suman?", ["Se multiplica la capacidad por el número de vehículos.", "3 por 6 son 18."], "18 L"),
    ],
    mistakes=[("Usar la fila de los años más nuevos porque «es la más actual».", "La fila depende del año del vehículo, no del año más reciente de la tabla.", "Haz coincidir motor y rango de años del vehículo."),
              ("Informar solo «rechazado» sin el valor ni el límite.", "El informe debe permitir revisar la decisión.", "Anota valor, límite, diferencia y fila usada.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿cómo se elige la fila correcta de una tabla con dos datos de entrada?", "Se hacen coincidir el motor y el rango de años del vehículo con la fila", "Se elige la fila con el valor más alto", "Se elige la primera fila de la tabla", "La fila depende de ambos datos del vehículo, no de su posición ni de su valor."),
        ("abc", "En Mecánica Automotriz: ¿por qué una norma de emisiones más reciente suele traer límites más bajos?", "Porque exige menos contaminación a los vehículos fabricados después de cierta fecha", "Porque los vehículos nuevos contaminan más", "Porque los límites solo suben con la edad del vehículo", "Las normas se vuelven más exigentes con el tiempo para reducir la contaminación."),
        ("abc", "En Mecánica Automotriz: ¿qué se anota en el informe cuando una lectura de emisiones supera el límite?", "El valor medido, el límite aplicado, la diferencia y la fila o norma usada", "Solo la palabra «rechazado»", "Solo el límite, sin el valor medido", "El informe debe permitir revisar la decisión con todos sus datos."),
        ("abc", "{F} ¿Qué límite de CO se aplica al vehículo V1?", "2 unidades", "4 unidades", "1 unidad", "V1 tiene motor M1 y año 5, que cae en la fila de años 4 a 6 con límite 2."),
        ("abc", "{F} ¿Qué capacidad de aceite indica el manual para el vehículo V2?", "5 L", "4 L", "3 L", "V2 tiene motor M2, cuya capacidad de aceite es 5 L en sus dos filas."),
        ("abc", "{F} ¿Qué cambia en las filas del motor M2 entre los años 1 a 3 y los años 4 a 6?", "El límite de CO baja de 3 a 1 y la capacidad de aceite se mantiene", "La capacidad de aceite sube y el límite de CO se mantiene", "Ambos valores bajan", "La tabla muestra 5 L en ambas filas y un límite de CO que baja."),
        ("=", "{F} ¿Cuántos mL de aceite lleva el motor M1?", "4*1000", "Se multiplican los litros por 1.000 para pasar a mililitros.", " mL"),
        ("=", "{F} ¿Cuántos L de aceite necesitan en total los vehículos V1, V2 y V3?", "4+5+5", "V1 usa 4 L por su motor M1 y V2 y V3 usan 5 L cada uno por su motor M2.", " L"),
        ("abc", "{F} ¿Cuál de los tres vehículos no cumple su límite de CO?", "V2", "V1", "V3", "V2 mide 4 sobre un límite de 3; V1 y V3 miden un valor igual a su límite y cumplen."),
        ("=", "{F} ¿Qué reducción porcentual tiene el límite de CO del motor M1 al pasar de los años 1 a 3 a los años 4 a 6?", "(4-2)*100//4", "La diferencia por 100 dividida por el valor anterior es la reducción porcentual.", " %"),
        ("abc", "{F} Un técnico aplica a V2 el límite de la fila de años 4 a 6 «porque es la más nueva». ¿Qué observación es correcta?", "Es un error: V2 es del año 2 y le corresponde la fila de años 1 a 3, con límite 3", "Es correcto, porque siempre se usa la norma más nueva", "Es correcto, porque con ese límite V2 pasaría", "La fila se elige por el año del vehículo; cambiarla para que pase falsea el resultado."),
        ("=", "{F} El taller recibe 10 vehículos con motor M2 y compra el aceite en bidones de 25 L. ¿Cuántos bidones cubren el pedido?", "(10*5)//25", "Se calculan los litros totales y se dividen entre los litros de cada bidón.", " bidones"),
        ("abc", "{F} Un vehículo de ejemplo con motor M1 y año 6 registra CO medido 3. ¿Qué informe es correcto?", "No cumple: supera por 1 el límite de 2 de la fila de años 4 a 6", "Cumple, porque 3 no supera el límite de 4", "Cumple, porque el año 6 es el más nuevo", "El año 6 usa la fila de límite 2, y 3 lo supera por 1."),
    ],
    ctx=("abc", "Una persona propietaria te cuenta que su vecino aprobó con CO 3 y pide que aprueben el suyo, también con CO 3, pero de otro motor y año. ¿Qué respondes?", "Que el límite depende del motor y del año de cada vehículo, así que se compara con la fila que le corresponde", "Que sí, porque la misma lectura siempre da el mismo resultado", "Que se aplica el promedio de los dos vehículos", "Cada vehículo se compara con su propia fila de la tabla."),
    sc=[
        ("En Mecánica Automotriz: ¿qué dos datos definen la fila en la tabla de la ficha?", "El motor y el rango de años", "La fila se elige con ambos datos."),
        ("En el taller automotriz: ¿cuántos mL tiene 1 L de aceite?", "1.000 mL", "Un litro equivale a mil mililitros."),
        ("¿Qué debe llevar un informe de lectura?", "Valor, límite, diferencia y fila usada", "Así se puede revisar la decisión."),
    ],
    op=("Ficha de ejemplo: tabla de otro manual. Motor K, años 1 y 2: límite de CO 5; motor K, años 3 y 4: límite de CO 3. Vehículo A: motor K, año 4, CO medido 3. Vehículo B: motor K, año 2, CO medido 6. Escribe (a) el límite que corresponde a cada vehículo, (b) si cada uno cumple, (c) la diferencia de cada uno con su límite, (d) una línea de informe para B.",
        "(a) A: 3; B: 5. (b) A cumple, porque 3 no supera 3; B no cumple. (c) A: 0 unidades; B: supera por 1 unidad. (d) «Vehículo B, motor K, año 2: CO 6, límite 5 de la fila de años 1 y 2; supera por 1; no cumple.»",
        ["elige la fila de cada vehículo", "decide si cumple", "calcula las diferencias", "redacta el informe con los cuatro datos"],
        ["hoja con las cuatro respuestas"],
        ["usar la misma fila para ambos", "decir que A no cumple por ser igual al límite", "informar sin el límite"],
        "Pregunta: «¿en qué rango de años cae el año de cada vehículo?». Si duda, pídele que relea cómo se elige la fila."),
    reinforce="Inventa una tabla de doble entrada con dos motores y dos rangos de años, y elige la fila para un vehículo que tú inventes.",
    extend="Explica con un ejemplo por qué usar la fila equivocada puede aprobar un vehículo que no cumple.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (flota de ejemplo, inventada). La empresa «Transportes Demo» tiene 12 vehículos livianos, 8 semipesados y 5 pesados. Clasificación de ejemplo según el peso bruto: liviano, hasta 3 toneladas; semipesado, más de 3 y hasta 10 toneladas; pesado, más de 10 toneladas (la norma vigente fija los valores reales). "
     "La matriz de peligros de su taller anota: vehículo elevado, fluidos calientes, aire comprimido, ruido y neumáticos de gran tamaño a presión.")
build(
    O3, 1, F,
    use="Aprenderé los tipos de mantenimiento, cómo se clasifican los vehículos livianos, semipesados y pesados y por qué el mantenimiento sigue la pauta del fabricante y las reglas de seguridad.",
    prior=["Sé sumar y multiplicar números enteros.", "Sé qué es un peligro y qué es un riesgo.", "Sé que un manual trae especificaciones."],
    explain=[
        "El mantenimiento preventivo se hace a intervalos fijados por el fabricante para evitar fallas; el mantenimiento correctivo se hace para corregir una falla que ya ocurrió. Las tareas y los intervalos del preventivo están en la pauta de mantenimiento del fabricante. Los vehículos se clasifican por su peso bruto en livianos, semipesados y pesados, y cada clase tiene pautas, repuestos y riesgos distintos.",
        "Un vehículo más pesado y con más sistemas de presión, como el aire comprimido, tiene mayor riesgo en el taller: piezas de gran masa, fluidos calientes y neumáticos a presión. Por eso las tareas las hace personal autorizado, con la norma vigente. Omitir una tarea de la pauta, aunque el vehículo parezca funcionar bien, quita la protección que el fabricante previó y puede afectar la seguridad y la garantía.",
        f"La autoridad de transporte exige revisiones técnicas periódicas según la norma vigente, y la Dirección del Trabajo fiscaliza las condiciones de trabajo del taller. {EMER} {AVISO}",
    ],
    vocab=[("mantenimiento preventivo", "el que se hace por intervalos para evitar fallas"), ("mantenimiento correctivo", "el que se hace para corregir una falla ya ocurrida"), ("pauta de mantenimiento", "lista de tareas e intervalos fijados por el fabricante"), ("peso bruto", "peso del vehículo más su carga máxima"), ("vehículo semipesado", "vehículo de peso intermedio entre el liviano y el pesado"), ("revisión técnica", "control periódico que exige la autoridad de transporte")],
    worked=[
        ("Clasificar un vehículo", "Con la clasificación de ejemplo de la explicación, un vehículo tiene un peso bruto de 6 toneladas. ¿Cómo se clasifica?", ["Se compara 6 con los límites de 3 y 10 toneladas.", "Está sobre 3 y no supera 10: es semipesado."], "Semipesado"),
        ("Tipo de mantenimiento", "Un taller de ejemplo cambia una pieza después de que dejó de funcionar. ¿Qué tipo de mantenimiento es?", ["La pieza ya falló antes de la intervención.", "Corregir una falla ocurrida es mantenimiento correctivo."], "Mantenimiento correctivo"),
    ],
    mistakes=[("Saltarse una tarea de la pauta porque «el vehículo anda bien».", "La tarea preventiva existe para evitar fallas antes de que se noten.", "Cumple la pauta aunque no haya síntomas."),
              ("Pensar que un vehículo pesado lo atiende cualquiera «con ayuda».", "Mayor masa y presión elevan el riesgo; lo atiende personal autorizado.", "Las tareas con riesgo las hace personal autorizado.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué es el mantenimiento preventivo?", "El que se hace a intervalos fijados por el fabricante para evitar fallas", "El que se hace después de que el vehículo falla", "El que se hace solo cuando la persona propietaria lo pide", "El preventivo se adelanta a la falla; el correctivo la repara."),
        ("abc", "En Mecánica Automotriz: ¿qué es el mantenimiento correctivo?", "El que se hace para corregir una falla ya ocurrida", "El que se hace por calendario aunque no haya fallas", "El que consiste solo en lavar el vehículo", "El correctivo actúa sobre una falla que ya existe."),
        ("abc", "En Mecánica Automotriz: ¿qué fija las tareas y los intervalos del mantenimiento preventivo?", "La pauta de mantenimiento del fabricante", "La preferencia del taller", "El precio de los repuestos", "El fabricante conoce el vehículo y fija la pauta; no depende de preferencias ni de precios."),
        ("abc", "{F} Con la clasificación de la ficha, ¿cómo se clasifica un vehículo de 8 toneladas de peso bruto?", "Semipesado", "Liviano", "Pesado", "8 está sobre 3 y no supera 10, que es el rango de los semipesados."),
        ("abc", "{F} ¿Qué clase de vehículo es la más numerosa de la flota?", "Los livianos", "Los semipesados", "Los pesados", "Hay 12 livianos, 8 semipesados y 5 pesados."),
        ("abc", "{F} De los peligros de la matriz, ¿cuál tiene como daño típico las quemaduras?", "Los fluidos calientes", "El ruido", "Los neumáticos de gran tamaño a presión", "Un fluido caliente puede quemar; el ruido daña la audición y los neumáticos a presión pueden liberar energía."),
        ("=", "{F} ¿Cuántos vehículos tiene la flota en total?", "12+8+5", "Se suman los livianos, los semipesados y los pesados.", " vehículos"),
        ("=", "{F} La empresa planifica 2 intervenciones preventivas al año por cada vehículo. ¿Cuántas intervenciones planifica en total?", "(12+8+5)*2", "Se calcula el total de vehículos y se multiplica por las intervenciones de cada uno.", " intervenciones"),
        ("=", "{F} Una intervención de un semipesado dura 4 horas y la de un pesado, 6 horas. Si cada semipesado y cada pesado se atiende una vez, ¿cuántas horas suman?", "8*4+5*6", "Se multiplican los vehículos de cada clase por sus horas y se suman.", " horas"),
        ("abc", "{F} Un jefe dice: «como los vehículos pesados son más grandes, los atiende cualquiera con ayuda». ¿Qué respuesta es correcta?", "No corresponde: mayor masa y presión elevan el riesgo y la tarea es de personal autorizado, con norma vigente", "Corresponde, porque cualquier persona puede ayudar si usa guantes", "Corresponde, porque los vehículos pesados son más resistentes", "A más masa y más sistemas a presión, más riesgo; los guantes no autorizan a nadie."),
        ("abc", "Un técnico decide omitir una tarea de la pauta del fabricante porque «el vehículo anda bien». ¿Qué problema tiene esa decisión?", "Se omite una tarea preventiva pensada para evitar fallas antes de que se noten, y puede afectar la seguridad y la garantía", "Ninguno, porque si no hay síntomas no hay falla", "Que ahorra tiempo pero no cambia nada", "La tarea preventiva actúa antes de que aparezcan síntomas."),
        ("=", "{F} La flota agrega 3 livianos y 2 pesados y cada vehículo recibe 2 intervenciones preventivas al año. ¿Cuántas intervenciones suma la flota ampliada?", "(12+8+5+3+2)*2", "Se suma el total de vehículos con los nuevos y se multiplica por 2.", " intervenciones"),
        ("abc", "En una visita a un taller de ejemplo, un fluido caliente salpica a una persona. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte rápido para ayudar con tus manos", "Limpiar el fluido antes de que llegue ayuda", "Acercarse sin formación puede sumar otro daño; se avisa a quienes pueden actuar."),
    ],
    ctx=("abc", "El conductor de un camión de ejemplo te dice: «mi camión nunca falla, no necesita pauta». ¿Qué respondes?", "Que la pauta es preventiva, evita fallas, protege la seguridad y se sigue aunque no haya síntomas", "Que es verdad, la pauta solo sirve para vehículos con problemas", "Que la pauta se hace solo si el cliente la paga", "La pauta preventiva se cumple aunque el vehículo parezca estar bien."),
    sc=[
        ("En Mecánica Automotriz: ¿qué tipo de mantenimiento se hace después de una falla?", "El correctivo", "Corrige una falla que ya ocurrió."),
        ("¿Dónde están los intervalos del mantenimiento preventivo?", "En la pauta de mantenimiento del fabricante", "El fabricante fija tareas e intervalos."),
        ("¿Qué institución fiscaliza las condiciones de trabajo del taller?", "La Dirección del Trabajo", "Fiscaliza lo laboral, como la seguridad del puesto."),
    ],
    op=("Ficha de ejemplo: una empresa tiene 4 vehículos livianos, 3 semipesados y 2 pesados, y planifica 3 intervenciones preventivas al año por vehículo. Escribe (a) cuántos vehículos y cuántas intervenciones al año tiene, (b) qué tipo de mantenimiento es el de una pieza cambiada después de una falla, (c) un peligro propio de los vehículos pesados con un control administrativo, (d) quién realiza la tarea.",
        "(a) 4 + 3 + 2 = 9 vehículos; 9 × 3 = 27 intervenciones al año. (b) Mantenimiento correctivo. (c) Peligro: neumáticos a presión o piezas de gran masa; control administrativo: una regla escrita de que solo personal autorizado interviene. (d) Personal autorizado, con la norma vigente.",
        ["calcula vehículos e intervenciones", "clasifica el tipo de mantenimiento", "relaciona peligro y control", "indica quién realiza la tarea"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar mal las intervenciones", "llamar preventivo a un mantenimiento tras una falla", "decir que cualquiera interviene"],
        "Pregunta: «¿la pieza se cambió antes o después de la falla?». Si duda, pídele que relea las definiciones de preventivo y correctivo."),
    reinforce="Escribe tres tareas de ejemplo y marca si cada una es preventiva o correctiva.",
    extend="Explica con un ejemplo por qué el mantenimiento preventivo puede ser más barato que el correctivo.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (pauta de mantenimiento y hoja de vida de ejemplo, inventadas, del «Modelo Demo 7»). Cada fila indica el intervalo en km y en meses, y se cumple lo que ocurra primero. "
     "Inspección general de niveles de fluidos: cada 10.000 km o 6 meses. Reemplazo de aceite del motor y de su filtro: cada 10.000 km o 12 meses. Reemplazo del filtro de aire: cada 20.000 km o 24 meses. Reemplazo de la correa de distribución: cada 100.000 km o 60 meses. "
     "Hoja de vida: el último reemplazo de aceite se hizo a los 38.000 km, hace 7 meses; el kilometraje actual es 44.000 km.")
build(
    O3, 2, F,
    use="Aprenderé a leer una pauta de mantenimiento con intervalos en km y en meses, a calcular vencimientos y a usar la hoja de vida del vehículo.",
    prior=["Sé sumar y restar números enteros.", "Sé qué es el mantenimiento preventivo.", "Sé leer una tabla con filas."],
    explain=[
        "Una pauta de mantenimiento lista las tareas y su intervalo en kilómetros y en meses. La regla «lo que ocurra primero» significa que la tarea vence cuando se alcanza cualquiera de los dos límites. El kilometraje de vencimiento es el kilometraje de la última vez que se hizo la tarea más el intervalo. Los fluidos y las piezas también se degradan con el tiempo, por eso la pauta fija un plazo en meses además de los km.",
        "La hoja de vida del vehículo registra las fechas, los kilometrajes, las tareas hechas y quién las hizo. Solo se anota lo que tiene un registro o comprobante verificable; no se completa de memoria ni se falsea para conservar una garantía. El asesor de servicio informa a la persona propietaria el próximo vencimiento, el técnico autorizado ejecuta y el jefe de taller supervisa que la pauta se cumpla.",
        f"Esta clase trabaja con números y documentos escritos; las tareas reales las hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("intervalo", "cada cuántos km o meses se repite una tarea"), ("lo que ocurra primero", "regla según la cual vence el primer límite que se alcance"), ("vencimiento", "kilometraje o fecha en que una tarea debe hacerse"), ("hoja de vida", "registro de las tareas hechas a un vehículo"), ("comprobante", "documento que respalda que una tarea se hizo")],
    worked=[
        ("Próximo vencimiento", "Una tarea de ejemplo se hizo a los 25.000 km y su intervalo es 15.000 km. ¿A qué kilometraje vence?", ["Se suma el intervalo al kilometraje de la última vez.", "25.000 más 15.000 son 40.000."], "A los 40.000 km"),
        ("Lo que ocurra primero", "Una pauta de ejemplo dice 8.000 km o 6 meses. Han pasado 7 meses y 5.000 km desde la última vez. ¿Está vencida?", ["Se compara cada dato con su límite.", "Los 7 meses superan los 6 meses, aunque los km no lleguen a 8.000."], "Sí, vencida por tiempo"),
    ],
    mistakes=[("Esperar a que se cumplan ambos límites para hacer la tarea.", "La regla es lo que ocurra primero: basta con alcanzar uno.", "Compara cada dato con su límite y actúa con el primero que se alcance."),
              ("Anotar en la hoja de vida una tarea que no tiene comprobante.", "Eso falsea el registro y puede ocultar un mantenimiento omitido.", "Solo se anota lo respaldado por un registro verificable.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿qué significa «cada 10.000 km o 6 meses, lo que ocurra primero»?", "Que la tarea vence cuando se alcance cualquiera de los dos límites", "Que hay que esperar a que se cumplan ambos límites", "Que el taller elige el límite que le convenga", "La regla toma el primer límite alcanzado, no ambos."),
        ("abc", "En Mecánica Automotriz: ¿qué registra la hoja de vida de un vehículo?", "Las fechas, los kilometrajes, las tareas hechas y quién las hizo", "Solo el precio de compra del vehículo", "Solo los datos de contacto de la persona propietaria", "La hoja de vida es el historial de mantenimiento, no un registro comercial."),
        ("abc", "En Mecánica Automotriz: ¿cómo se calcula el kilometraje del próximo vencimiento de una tarea?", "Se suma el intervalo al kilometraje de la última vez que se hizo", "Se resta el intervalo al kilometraje actual", "Se multiplica el kilometraje actual por el intervalo", "El vencimiento se cuenta hacia adelante desde la última vez."),
        ("abc", "{F} ¿Qué tarea de la pauta tiene el mismo intervalo en km que el reemplazo de aceite pero un plazo en meses menor?", "La inspección general de niveles de fluidos", "El reemplazo del filtro de aire", "El reemplazo de la correa de distribución", "Inspección y aceite tienen 10.000 km, pero la inspección vence a los 6 meses y el aceite a los 12."),
        ("abc", "{F} ¿En qué documento se anota que el aceite se reemplazó a los 38.000 km?", "En la hoja de vida del vehículo", "En la pauta de mantenimiento", "En el manual de usuario", "La hoja de vida guarda lo ya hecho; la pauta solo fija intervalos."),
        ("abc", "{F} ¿Cuál es la tarea de la pauta con el plazo más largo en meses?", "El reemplazo de la correa de distribución", "El reemplazo del filtro de aire", "El reemplazo de aceite", "La correa tiene 60 meses; el filtro de aire 24 y el aceite 12."),
        ("=", "{F} ¿A qué kilometraje vence el próximo reemplazo de aceite?", "38000+10000", "Se suma el intervalo al kilometraje del último reemplazo.", " km"),
        ("=", "{F} ¿Cuántos km faltan, desde el kilometraje actual, para el próximo reemplazo de aceite?", "(38000+10000)-44000", "Se calcula el vencimiento y se resta el kilometraje actual.", " km"),
        ("=", "{F} El vehículo recorrió 24.000 km desde el último reemplazo de la correa de distribución. ¿Cuántos km le faltan para completar el intervalo?", "100000-24000", "Se resta lo recorrido al intervalo en km de la correa.", " km"),
        ("abc", "{F} Han pasado 13 meses desde el último reemplazo de aceite de otro vehículo y recorrió solo 7.000 km. ¿Está vencido el reemplazo?", "Sí, porque se superaron los 12 meses aunque no se llegó a los 10.000 km", "No, porque no se llegó a los 10.000 km", "No, porque deben cumplirse ambos límites a la vez", "Con la regla de lo que ocurra primero, superar un solo límite vence la tarea."),
        ("abc", "Una persona dice: «mi vehículo casi no se usa, así que puedo ignorar el plazo en meses». ¿Qué respuesta es correcta?", "No: los fluidos y las piezas también se degradan con el tiempo, por eso la pauta fija un plazo en meses", "Sí, porque solo importan los km", "Sí, si el vehículo está guardado en un lugar techado", "El plazo en meses cubre el deterioro por tiempo aunque se recorran pocos km."),
        ("=", "Una tarea de ejemplo tiene un intervalo de 15.000 km o 12 meses y se hizo a los 52.000 km. Hoy el vehículo tiene 61.000 km. ¿Cuántos km faltan para el vencimiento por kilometraje?", "(52000+15000)-61000", "Se calcula el kilometraje de vencimiento y se resta el actual.", " km"),
        ("abc", "{F} En la hoja de vida falta la fecha del último reemplazo de aceite. ¿Qué consecuencia tiene?", "No se puede calcular con certeza el vencimiento por tiempo y hay que informar y completar el dato con un comprobante", "Ninguna, porque basta el kilometraje", "Se asume que se hizo hoy", "Sin la fecha, el límite en meses no se puede comprobar; suponerla falsea el registro."),
    ],
    ctx=("abc", "Una persona propietaria te pide que anotes como «hecho» un mantenimiento que le hizo un conocido, sin comprobante. ¿Qué respondes?", "Que solo se anota lo que tiene un comprobante o registro verificable, para no falsear la hoja de vida", "Que sí, para que no pierda la garantía", "Que se anota con lápiz para poder borrarlo después", "Una hoja de vida solo es útil si sus datos son verificables."),
    sc=[
        ("En Mecánica Automotriz: ¿cuándo vence una tarea con intervalo en km y en meses?", "Cuando se alcanza el primero de los dos límites", "Esa es la regla de lo que ocurra primero."),
        ("¿Cómo se calcula un vencimiento en km?", "Sumando el intervalo al kilometraje de la última vez", "Se cuenta desde la última vez que se hizo."),
        ("En Mecánica Automotriz: ¿qué se anota en la hoja de vida de un vehículo?", "Solo lo que tiene un registro verificable", "Un dato sin respaldo falsea el historial."),
    ],
    op=("Ficha de ejemplo: pauta: reemplazo de filtro de aire cada 15.000 km o 12 meses. Hoja de vida: el último reemplazo se hizo a los 31.000 km, hace 9 meses; el kilometraje actual es 38.000 km. Escribe (a) el kilometraje de vencimiento, (b) cuántos km faltan, (c) si está vencido por tiempo, (d) qué se registra cuando se haga la tarea.",
        "(a) 31.000 + 15.000 = 46.000 km. (b) 46.000 − 38.000 = 8.000 km. (c) No: han pasado 9 meses y el plazo es de 12. (d) La fecha, el kilometraje, la tarea hecha y quién la hizo, con su comprobante.",
        ["calcula el vencimiento", "calcula los km que faltan", "compara con el plazo en meses", "indica qué se registra"],
        ["hoja con las cuatro respuestas"],
        ["restar el intervalo en vez de sumarlo", "olvidar el límite en meses", "no registrar quién hizo la tarea"],
        "Pregunta: «¿se cuenta hacia adelante o hacia atrás desde la última vez?». Si duda, pídele que relea cómo se calcula el vencimiento."),
    reinforce="Inventa una tarea con intervalo en km y meses, el dato de la última vez y el kilometraje actual, y calcula cuánto falta.",
    extend="Explica con un ejemplo por qué una tarea puede vencer por tiempo aunque el vehículo casi no se haya usado.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (registro de flota de ejemplo, inventado). Pauta de ejemplo para vehículos semipesados: reemplazo de aceite y filtro cada 15.000 km o 9 meses, lo que ocurra primero. "
     "S1: último reemplazo a los 120.000 km, hace 8 meses; kilometraje actual 131.000 km. S2: último reemplazo a los 98.000 km, hace 10 meses; kilometraje actual 104.000 km. S3: último reemplazo a los 75.000 km, hace 5 meses; kilometraje actual 91.000 km.")
build(
    O3, 3, F,
    use="Aprenderé a revisar el registro de una flota, a decidir qué vehículos tienen el mantenimiento al día o vencido y a informar al jefe de taller con datos.",
    prior=["Sé calcular vencimientos de una pauta.", "Sé restar números enteros.", "Sé que la regla es lo que ocurra primero."],
    explain=[
        "Para revisar un registro se calcula, para cada vehículo, cuántos km recorrió y cuánto tiempo pasó desde la última intervención, y se compara con los dos límites de la pauta. Si no se alcanzó ninguno, la tarea está al día; si se alcanzó o superó alguno, está vencida. Un vehículo que recorrió más km no es necesariamente el más urgente: importa si superó algún límite.",
        "Las tareas vencidas se atienden antes que las que están al día, porque una tarea preventiva vencida deja al vehículo sin la protección prevista por el fabricante. El informe al jefe de taller lleva, por vehículo, el recorrido, el tiempo, los límites y el estado. Posponer un mantenimiento vencido por conveniencia no corresponde: se registra, se informa el riesgo y decide el jefe de taller según la pauta y la norma vigente.",
        f"Esta clase revisa registros; las tareas las hace personal autorizado y capacitado. {EMER} {AVISO}",
    ],
    vocab=[("al día", "sin ningún límite de la pauta alcanzado"), ("vencida", "con al menos un límite de la pauta superado"), ("recorrido", "km avanzados desde la última intervención"), ("prioridad", "orden en que se atienden las tareas"), ("informe", "texto con los datos y el estado de cada vehículo")],
    worked=[
        ("Al día", "Una pauta de ejemplo dice 10.000 km o 6 meses. Un vehículo recorrió 7.000 km en 4 meses. ¿Cuál es su estado?", ["7.000 es menor que 10.000 y 4 es menor que 6.", "Ningún límite se alcanzó."], "Al día"),
        ("Vencida por km", "Una pauta de ejemplo dice 12.000 km o 8 meses. Un vehículo recorrió 13.000 km en 5 meses. ¿Cuál es su estado?", ["13.000 supera los 12.000 km.", "Con un límite superado, la tarea está vencida."], "Vencida por kilometraje"),
    ],
    mistakes=[("Atender primero al vehículo que más km recorrió.", "El criterio es si superó un límite de la pauta, no solo los km.", "Calcula el estado de cada vehículo y atiende primero los vencidos."),
              ("Posponer un mantenimiento vencido sin registrarlo.", "Se pierde la trazabilidad y el riesgo queda oculto.", "Registra el vencimiento, informa el riesgo y espera la decisión del jefe de taller.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿cómo se calcula cuántos km recorrió un vehículo desde su última intervención?", "Se resta el kilometraje de la última intervención al kilometraje actual", "Se suma el intervalo al kilometraje actual", "Se divide el kilometraje actual entre los meses", "El recorrido es la diferencia entre el kilometraje actual y el de la última vez."),
        ("abc", "En Mecánica Automotriz: ¿qué estado tiene una tarea cuando no se alcanzó ninguno de sus dos límites?", "Al día", "Vencida", "En espera de un repuesto", "Sin ningún límite alcanzado, la tarea está al día."),
        ("abc", "En Mecánica Automotriz: ¿por qué se atiende primero una tarea vencida que una al día?", "Porque una tarea preventiva vencida deja al vehículo sin la protección prevista por el fabricante", "Porque las tareas al día no se registran", "Porque las tareas vencidas son más baratas", "El preventivo vencido es un riesgo acumulado; el costo no define la prioridad."),
        ("abc", "{F} ¿Qué vehículo supera el límite de tiempo de la pauta?", "S2", "S1", "S3", "S2 lleva 10 meses y el límite es 9; S1 lleva 8 y S3 lleva 5."),
        ("abc", "{F} ¿Qué vehículo supera el límite de kilometraje de la pauta?", "S3", "S1", "S2", "S3 recorrió 16.000 km desde el último reemplazo y el límite es 15.000; S1 recorrió 11.000 y S2 6.000."),
        ("abc", "{F} ¿Qué vehículo está al día en ambos límites?", "S1", "S2", "S3", "S1 recorrió 11.000 km en 8 meses y no alcanzó ninguno de los dos límites."),
        ("=", "{F} ¿Cuántos km le faltan a S1 para el límite de kilometraje de la pauta?", "15000-(131000-120000)", "Se calcula el recorrido y se resta al intervalo.", " km"),
        ("=", "{F} ¿Cuántos km superó S3 el límite de kilometraje de la pauta?", "(91000-75000)-15000", "Se calcula el recorrido y se resta el intervalo.", " km"),
        ("=", "{F} Cada reemplazo toma 3 horas de mano de obra y el taller atiende solo los vehículos vencidos. ¿Cuántas horas necesita?", "2*3", "Los vehículos vencidos son S2 y S3, y cada uno toma 3 horas.", " horas"),
        ("abc", "{F} El jefe quiere atender primero a S1 porque recorrió más km que S2. ¿Qué respuesta es correcta?", "Corresponde priorizar a los vencidos, S2 y S3; S1 sigue al día en ambos límites aunque haya recorrido más km", "Corresponde, porque el que más recorrió siempre es el más urgente", "Corresponde, porque S2 y S3 pueden esperar un año", "La prioridad la fija el estado según la pauta y no solo los km recorridos."),
        ("abc", "{F} Alguien dice que S2 no necesita el reemplazo porque recorrió solo 6.000 km. ¿Qué respuesta es correcta?", "Sí lo necesita: venció por tiempo, con 10 meses sobre un límite de 9, y basta con alcanzar un límite", "No lo necesita, porque solo importa el kilometraje", "No lo necesita, si el conductor asegura que no hay síntomas", "La regla es lo que ocurra primero; el tiempo también vence la tarea."),
        ("=", "{F} Pasan 2 meses y S1 recorre 5.000 km más. ¿Cuántos km por encima del límite de kilometraje de la pauta quedará S1?", "(131000-120000+5000)-15000", "Se suma el recorrido nuevo al anterior y se resta el límite de kilometraje.", " km"),
        ("abc", "{F} ¿Qué debe contener el informe al jefe de taller?", "Por vehículo, el recorrido, el tiempo, los límites y el estado: S1 al día, S2 vencido por tiempo y S3 vencido por kilometraje", "Solo la lista de vehículos vencidos, sin los datos", "Solo la recomendación de atender a todos sin indicar estados", "El informe da los datos y el estado para que el jefe decida con evidencia."),
    ],
    ctx=("abc", "El jefe de una empresa de ejemplo pide postergar por 3 meses el mantenimiento vencido de un camión de reparto porque «no hay tiempo». ¿Qué corresponde?", "Registrar el vencimiento, informar el riesgo al jefe de taller y esperar su decisión según la pauta y la norma", "Posponer sin registrar para no complicar la entrega", "Hacer el mantenimiento tú mismo en la noche", "Una decisión de posponer la toma quien corresponde y queda registrada; no se oculta ni se improvisa."),
    sc=[
        ("En Mecánica Automotriz: ¿qué estado tiene una tarea con un límite superado?", "Vencida", "Basta un límite superado para vencerla."),
        ("¿Qué se atiende primero: una tarea vencida o una al día?", "La vencida", "La vencida deja sin protección al vehículo."),
        ("¿Qué lleva el informe al jefe de taller por cada vehículo?", "El recorrido, el tiempo, los límites y el estado", "Con esos datos el jefe puede decidir con evidencia."),
    ],
    op=("Ficha de ejemplo: pauta para camiones pesados: reemplazo de aceite y filtro cada 20.000 km o 12 meses. P1: último reemplazo a los 200.000 km, hace 10 meses; kilometraje actual 215.000 km. P2: último reemplazo a los 150.000 km, hace 13 meses; kilometraje actual 158.000 km. P3: último reemplazo a los 90.000 km, hace 6 meses; kilometraje actual 112.000 km. Escribe (a) el estado de cada camión, (b) cuáles prioriza, (c) cuántos km le faltan a P1 para su límite, (d) qué dato mínimo anotas por camión en el informe.",
        "(a) P1: al día (15.000 km y 10 meses); P2: vencido por tiempo (13 meses sobre 12); P3: vencido por kilometraje (22.000 km sobre 20.000). (b) P2 y P3. (c) 20.000 − 15.000 = 5.000 km. (d) El recorrido, el tiempo, los límites y el estado.",
        ["calcula el estado de cada camión", "prioriza los vencidos", "calcula los km restantes", "indica los datos del informe"],
        ["hoja con las cuatro respuestas"],
        ["priorizar por km recorridos", "olvidar el límite en meses", "informar sin datos"],
        "Pregunta: «¿superó algún límite?». Si duda, pídele que relea la regla de lo que ocurra primero."),
    reinforce="Inventa un vehículo con su último reemplazo, su kilometraje actual y el tiempo transcurrido, y decide su estado con una pauta que tú escribas.",
    extend="Explica con un ejemplo por qué un informe con datos ayuda más al jefe de taller que una frase como «hay que atender todo».",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (presupuesto de mantenimiento de ejemplo, inventado). Flota de 6 vehículos livianos. Intervención de aceite por vehículo: aceite 4 L a $5.000 el litro; filtro de aceite $8.000; mano de obra 2 horas a $11.000 la hora. "
     "Además, una vez al año cada vehículo recibe un filtro de aire de $12.000. Cada vehículo recorre 15.000 km al año y el intervalo de aceite es de 5.000 km. Presupuesto anual disponible: $900.000.")
build(
    O3, 4, F,
    use="Aprenderé a planificar el mantenimiento de una flota con números: cuántas intervenciones al año, cuánto cuestan, si alcanza el presupuesto y cuánto aceite usado queda como residuo.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé qué es un intervalo de la pauta.", "Sé calcular un costo con horas y tarifa."],
    explain=[
        "Para planificar se calcula primero la frecuencia: las intervenciones al año de un vehículo son los km anuales divididos por el intervalo en km. El costo de una intervención suma los insumos y repuestos más la mano de obra, que son las horas por la tarifa. El costo anual de un vehículo suma todas sus intervenciones y gastos anuales, y el de la flota se obtiene multiplicando por el número de vehículos.",
        "El resultado se compara con el presupuesto. Si el presupuesto no alcanza, no se recorta la pauta del fabricante por cuenta propia: se informa el déficit y decide quien corresponde. Cada cambio de aceite deja aceite usado, que es un residuo que se entrega a un gestor autorizado según la norma vigente; nunca se vierte en desagües ni en el suelo. Cambiar un intervalo exige respaldo técnico del fabricante.",
        f"Esta clase planifica con números; el trabajo real lo hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("frecuencia", "veces al año que se repite una tarea"), ("insumo", "material que se consume en una tarea, como el aceite"), ("mano de obra", "horas de trabajo por su tarifa"), ("presupuesto", "dinero disponible para un fin"), ("déficit", "falta de dinero respecto de lo necesario"), ("aceite usado", "residuo que se entrega a un gestor autorizado")],
    worked=[
        ("Frecuencia", "Un vehículo de ejemplo recorre 12.000 km al año y su intervalo es 4.000 km. ¿Cuántas intervenciones al año necesita?", ["Se dividen los km anuales entre el intervalo.", "12.000 entre 4.000 son 3."], "3 intervenciones"),
        ("Costo de una intervención", "Una intervención de ejemplo usa 3 L de aceite a $4.000 el litro y 1 hora de mano de obra a $9.000. ¿Cuánto cuesta?", ["El aceite cuesta 3 por 4.000, es decir 12.000.", "Se suman 12.000 y 9.000."], "$21.000"),
    ],
    mistakes=[("Recortar tareas de la pauta para que «cuadre» el presupuesto.", "La pauta del fabricante no se ajusta al dinero disponible.", "Informa el déficit y deja que decida quien corresponde."),
              ("Olvidar el aceite usado en el plan.", "Cada cambio de aceite genera un residuo que hay que gestionar.", "Calcula también los litros de aceite usado y su entrega a un gestor autorizado.")],
    T=[
        ("abc", "En Mecánica Automotriz: ¿cómo se calcula cuántas intervenciones al año necesita un vehículo?", "Se dividen los km anuales entre el intervalo en km", "Se multiplican los km anuales por el intervalo", "Se restan los km anuales al intervalo", "La frecuencia es cuántas veces cabe el intervalo en los km del año."),
        ("abc", "En Mecánica Automotriz: ¿qué incluye el costo de una intervención preventiva?", "Los insumos y repuestos más la mano de obra", "Solo la mano de obra", "Solo el precio del vehículo", "El costo suma materiales y trabajo; el precio del vehículo no interviene."),
        ("abc", "En Mecánica Automotriz: ¿qué se hace con el aceite usado que deja una intervención?", "Se entrega a un gestor autorizado, según la norma vigente", "Se vierte en el desagüe del taller", "Se deja en el patio hasta que se evapore", "El aceite usado es un residuo que no puede ir a desagües ni al suelo."),
        ("abc", "{F} ¿Qué datos de la ficha permiten calcular cuántas intervenciones de aceite hay al año por vehículo?", "Los km anuales y el intervalo de aceite", "El precio por litro y las horas de mano de obra", "El presupuesto anual y el filtro de aire", "La frecuencia sale de dividir los km anuales entre el intervalo."),
        ("abc", "{F} ¿Cuál de los gastos de la ficha depende del número de horas?", "La mano de obra", "El aceite", "El filtro de aire", "La mano de obra es horas por tarifa; los otros gastos son materiales."),
        ("abc", "{F} ¿Qué gasto se repite una sola vez al año por vehículo?", "El filtro de aire", "El filtro de aceite", "La mano de obra", "La ficha indica que el filtro de aire se cambia una vez al año; lo demás va con cada intervención de aceite."),
        ("=", "{F} ¿Cuántos pesos cuesta una intervención de aceite, entre aceite, filtro de aceite y mano de obra?", "4*5000+8000+2*11000", "Se suman el aceite, el filtro y la mano de obra.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta el año de un vehículo, con sus intervenciones de aceite y su filtro de aire?", "(15000//5000)*(4*5000+8000+2*11000)+12000", "Se multiplican las intervenciones por su costo y se suma el filtro de aire.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta el año de toda la flota?", "6*((15000//5000)*(4*5000+8000+2*11000)+12000)", "Se multiplica el costo anual de un vehículo por los 6 vehículos.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más que el presupuesto cuesta el plan anual de la flota?", "6*((15000//5000)*(4*5000+8000+2*11000)+12000)-900000", "Se calcula el costo anual de la flota y se resta el presupuesto.", " pesos"),
        ("abc", "{F} Para ajustar el presupuesto, un jefe propone dejar de cambiar el filtro de aire. ¿Qué observación es correcta?", "No corresponde recortar la pauta sin respaldo técnico; hay que informar el déficit y buscar financiamiento", "Corresponde, porque los filtros de aire no influyen en el motor", "Corresponde, si el vehículo se ve limpio", "La pauta la fija el fabricante y no se recorta para cuadrar un presupuesto."),
        ("=", "{F} Cada intervención de aceite deja 4 L de aceite usado. ¿Cuántos litros de aceite usado genera la flota en el año?", "6*(15000//5000)*4", "Se multiplican los vehículos, las intervenciones por vehículo y los litros de cada una.", " L"),
        ("=", "{F} El taller consigue el aceite a $4.000 el litro. ¿Cuánto cuesta ahora el plan anual de la flota?", "6*((15000//5000)*(4*4000+8000+2*11000)+12000)", "Se recalcula la intervención con el nuevo precio por litro y se vuelve a calcular el año de la flota.", " pesos"),
    ],
    ctx=("abc", "El dueño de una flota de ejemplo pregunta si puede alargar el intervalo del aceite de 5.000 a 10.000 km «para gastar la mitad». ¿Qué respondes?", "Que el intervalo lo fija el fabricante y cambiarlo sin respaldo técnico arriesga el motor y la garantía; se consulta el manual y al jefe de taller", "Que sí, porque gastará la mitad y no cambia nada", "Que sí, si el aceite se ve limpio", "El intervalo se respalda con el manual del fabricante, no con el aspecto del aceite."),
    sc=[
        ("En Mecánica Automotriz: ¿cómo se calcula la frecuencia anual de una tarea?", "Dividiendo los km anuales entre el intervalo", "Muestra cuántas veces cabe el intervalo en el año."),
        ("¿Qué pasa con el aceite usado?", "Se entrega a un gestor autorizado", "Es un residuo que no se vierte en desagües ni en el suelo."),
        ("En el mantenimiento de una flota: ¿qué se hace si el presupuesto no alcanza?", "Se informa el déficit y decide quien corresponde", "La pauta no se recorta por cuenta propia."),
    ],
    op=("Ficha de ejemplo: una flota de 4 vehículos recorre 12.000 km al año por vehículo; el intervalo de aceite es 6.000 km. Una intervención usa 5 L de aceite a $4.000 el litro y 1 hora de mano de obra a $10.000. Presupuesto anual: $300.000. Escribe (a) cuántas intervenciones por vehículo al año, (b) cuánto cuesta una intervención, (c) el costo anual de la flota, (d) si alcanza el presupuesto y cuántos litros de aceite usado se generan.",
        "(a) 12.000 ÷ 6.000 = 2. (b) 5 × 4.000 + 10.000 = 30.000 pesos. (c) 4 × 2 × 30.000 = 240.000 pesos. (d) Alcanza y sobran 60.000 pesos; el aceite usado es 4 × 2 × 5 = 40 L, que se entregan a un gestor autorizado.",
        ["calcula la frecuencia", "calcula el costo de una intervención", "calcula el costo de la flota", "compara con el presupuesto y calcula el residuo"],
        ["hoja con los cálculos y las respuestas"],
        ["multiplicar los km por el intervalo", "olvidar la mano de obra", "olvidar el residuo"],
        "Pregunta: «¿cuántas veces cabe el intervalo en los km del año?». Si duda, pídele que relea cómo se calcula la frecuencia."),
    reinforce="Inventa una flota de tres vehículos, un intervalo y un costo por intervención, y calcula el costo anual.",
    extend="Explica con un ejemplo por qué alargar un intervalo puede salir más caro a largo plazo.",
)
