"""Instalaciones Sanitarias TP 3.º y 4.º medio: OAE-05 (mantener y reparar artefactos y redes de gas y agua potable: mantenimiento como planificación y documentación) y OAE-06 (redes de agua potable, riego y evacuación: solo conceptos y cálculos en papel)."""
from __future__ import annotations

from tp_insa_common import AVISO, EMER, build

O5 = "TP-INSA-3y4-OAE-05"
O6 = "TP-INSA-3y4-OAE-06"

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El condominio ficticio «Parque Alto», de 12 casas, contrata un servicio de mantención de los artefactos de gas y de la red de agua potable. "
     "Cada casa tiene 2 artefactos de gas (cocina y calentador de agua). Documentos entregados: manuales de los fabricantes, una pauta de mantención y una bitácora. "
     "Riesgos anotados: gas, agua caliente, electricidad en algunos artefactos, resbalones y productos de limpieza.")
build(
    O5, 1, F,
    use="Aprenderé la diferencia entre mantener y reparar, qué documentos guían el trabajo, qué institución vigila el gas y qué riesgos tiene la mantención.",
    prior=["Sé que el gas es de riesgo alto.", "Sé leer una ficha con documentos.", "Sé multiplicar."],
    explain=[
        "Mantener es cuidar un artefacto o una red para que no falle: es la mantención preventiva, que se planifica con anticipación. Reparar es corregir una falla que ya ocurrió: es la mantención correctiva. Ambas siguen las especificaciones del fabricante, que están en el manual, y las normas vigentes: en gas, las de la Superintendencia de Electricidad y Combustibles (SEC); en agua potable, las normas sanitarias. Un empalme es la conexión entre la red de una propiedad y la red pública del servicio, y solo personal autorizado lo interviene.",
        "Los riesgos de la mantención son el gas (fuga, incendio, explosión, monóxido de carbono), el agua caliente (quemaduras), la electricidad de algunos artefactos, los resbalones en pisos mojados y los productos químicos de limpieza. Si un artefacto presenta una falla, se deja sin uso, se señaliza como «fuera de servicio» y se avisa a personal autorizado. Nadie improvisa una reparación de gas.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("mantención preventiva", "cuidado planificado de un artefacto o una red para que no falle"), ("mantención correctiva", "reparación de una falla que ya ocurrió"), ("manual del fabricante", "documento con las especificaciones y cuidados de un artefacto"), ("pauta de mantención", "lista de tareas periódicas con su frecuencia"), ("bitácora", "cuaderno donde se anotan los hechos del trabajo"), ("empalme", "conexión entre la red de una propiedad y la red pública"), ("fuera de servicio", "señal de que un artefacto no debe usarse")],
    worked=[
        ("Clasificar la mantención", "Cada seis meses un técnico de ejemplo revisa un artefacto, aunque funcione bien. ¿Qué tipo de mantención es?", ["Se hace antes de que falle y con un calendario.", "Es mantención preventiva."], "Preventiva"),
        ("Contar tareas", "Un condominio de ejemplo tiene 8 casas con 3 artefactos cada una. ¿Cuántos artefactos hay que incluir en la pauta?", ["Se multiplican las casas por los artefactos.", "8 por 3 son 24."], "24 artefactos"),
    ],
    mistakes=[("Seguir usando un artefacto con falla «mientras llega el técnico».", "La falla puede empeorar y causar un accidente.", "Deja el artefacto fuera de servicio, señalízalo y avisa a personal autorizado."),
              ("Pensar que repasar un manual habilita para reparar un artefacto de gas.", "Reparar gas exige personal autorizado.", "Aprende los conceptos y deja la reparación a quien corresponde.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es la mantención preventiva?", "El cuidado planificado de un artefacto o una red para que no falle", "La reparación de una falla ya ocurrida", "La compra de un artefacto nuevo", "La mantención preventiva se anticipa a la falla."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es la mantención correctiva?", "La reparación de una falla que ya ocurrió", "La revisión periódica de un artefacto que funciona bien", "El cambio de la pauta de mantención", "La correctiva actúa después de que apareció la falla."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es un empalme?", "La conexión entre la red de una propiedad y la red pública", "Una unión entre dos tubos dentro de una pared", "Un tipo de artefacto de gas", "El empalme une la propiedad con la red pública y se interviene solo por personal autorizado."),
        ("=", "{F} ¿Cuántos artefactos de gas hay en el condominio de la ficha?", "12*2", "Se multiplican las casas por los dos artefactos de cada una.", " artefactos"),
        ("abc", "{F} ¿Qué documento de la ficha lista las tareas periódicas con su frecuencia?", "La pauta de mantención", "El manual del fabricante", "La bitácora", "La pauta ordena las tareas periódicas; el manual da las especificaciones y la bitácora registra hechos."),
        ("abc", "{F} ¿Qué riesgo de la ficha se asocia al agua caliente de los artefactos?", "Quemaduras", "Intoxicación por monóxido de carbono", "Caída desde altura", "El agua caliente puede producir quemaduras; el monóxido viene de mala combustión."),
        ("=", "{F} La pauta de ejemplo exige 3 revisiones al año por cada artefacto de gas. ¿Cuántas revisiones suman al año los artefactos del condominio?", "12*2*3", "Se multiplican los artefactos por las revisiones anuales de cada uno.", " revisiones"),
        ("abc", "Una persona de ejemplo detecta que un calentador de agua presenta una falla. ¿Qué corresponde?", "Dejarlo fuera de servicio, señalizarlo y avisar a personal autorizado", "Seguir usándolo hasta que el técnico llegue", "Abrirlo para ver qué falla", "Un artefacto con falla puede causar un accidente; se deja sin uso hasta que lo revise personal autorizado."),
        ("ab", "Un estudiante de ejemplo quiere reparar la llave de un artefacto de gas del condominio porque «el manual es fácil». ¿Qué corresponde?", "No hacerlo: la reparación de gas la hace personal autorizado", "Hacerlo con el manual en la mano", "Entender el manual no habilita para reparar gas, que es una tarea de riesgo alto."),
        ("abc", "En una visita de ejemplo, una persona percibe olor a gas dentro de un recinto cerrado. ¿Qué corresponde según las reglas generales?", "No entrar ni accionar interruptores o llamas, avisar a un adulto responsable y a emergencias", "Entrar a buscar la fuga", "Abrir los artefactos para revisar", "Entrar o encender algo puede provocar intoxicación, incendio o explosión."),
        ("abc", "{F} Un compañero dice: «si la pauta ya existe, no hace falta anotar nada en la bitácora». ¿Qué respuesta es correcta?", "Es falso: la bitácora deja registro de lo que se hizo y se encontró", "Es cierto: la pauta reemplaza a la bitácora", "Es cierto si todo está bien", "La pauta planifica y la bitácora registra lo que realmente ocurrió."),
        ("=", "{F} Cada casa tiene 2 artefactos de gas y la pauta dice que cada uno recibe 2 horas de revisión al año. ¿Cuántas horas de revisión suma el condominio?", "12*2*2", "Se multiplican los artefactos por las horas de cada uno.", " horas"),
        ("abc", "¿Qué tipo de mantención es reparar un calentador que dejó de funcionar?", "Correctiva", "Preventiva", "Ninguna: reparar no es mantención", "Reparar una falla ya ocurrida es mantención correctiva."),
    ],
    ctx=("abc", "Un vecino del condominio de ejemplo te dice: «el calentador hace un ruido raro; ábrelo, que tú estudiaste esto». ¿Qué respondes?", "Que lo deje fuera de servicio y llame a personal autorizado; tú no lo abrirás", "Que lo abres, pero con el manual", "Que lo sigas usando mientras anotas el ruido", "Un ruido anormal puede ser señal de falla; la revisión de gas es de personal autorizado."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué es la mantención preventiva?", "El cuidado planificado para que el artefacto no falle", "Se hace antes de que ocurra la falla."),
        ("¿Qué se hace con un artefacto con falla?", "Se deja fuera de servicio y se avisa a personal autorizado", "Seguir usándolo puede causar un accidente."),
        ("¿Quién repara artefactos de gas?", "Personal autorizado", "La reparación del gas es de riesgo alto."),
    ],
    op=("Ficha de ejemplo: el edificio «Los Cedros» tiene 10 departamentos con 3 artefactos de gas cada uno. La pauta de ejemplo exige 2 revisiones al año por artefacto. Escribe (a) cuántos artefactos hay, (b) cuántas revisiones al año suman, (c) cómo se llama la mantención de reparar un artefacto que falló, (d) qué harías si un artefacto presentara una falla.",
        "(a) 10 × 3 = 30 artefactos. (b) 30 × 2 = 60 revisiones. (c) Correctiva. (d) Dejarlo fuera de servicio, señalizarlo y avisar a personal autorizado, sin repararlo.",
        ["calcula los artefactos", "calcula las revisiones", "clasifica la mantención", "propone la conducta correcta"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar mal", "confundir preventiva con correctiva", "proponer reparar el artefacto"],
        "Pregunta: «¿qué diferencia hay entre mantener y reparar?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Escribe tres ejemplos de mantención preventiva y tres de mantención correctiva en una vivienda, sin describir cómo se hacen.",
    extend="Explica con un ejemplo por qué la mantención preventiva suele costar menos que esperar a que algo falle.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (pauta de mantención de ejemplo, inventada). Tareas y frecuencias: inspección visual por técnico autorizado, cada 6 meses; revisión completa de un artefacto de gas por técnico autorizado, cada 12 meses; "
     "revisión de la documentación (manuales y certificados), cada 12 meses; cambio de una pieza por desgaste, según la vida útil indicada en el manual (en este ejemplo, 5 años). "
     "Hoja de vida del artefacto de ejemplo: instalado en el mes 0; última inspección visual en el mes 6.")
build(
    O5, 2, F,
    use="Aprenderé los documentos de la mantención (pauta, hoja de vida, orden de trabajo, informe), el calendario de frecuencias y el rol de cada persona.",
    prior=["Sé qué es mantención preventiva y correctiva.", "Sé sumar meses.", "Sé qué es una bitácora."],
    explain=[
        "La pauta de mantención dice qué tarea se hace y cada cuánto tiempo. La hoja de vida del artefacto es su historia por escrito: fecha de instalación, revisiones, fallas y cambios de piezas. La orden de trabajo (OT) es el documento que encarga una tarea concreta: dice qué se hace, dónde, quién lo hace y para cuándo. El informe técnico resume lo que se encontró y lo que se recomienda. Un repuesto es una pieza que reemplaza a otra desgastada. La vida útil es el tiempo durante el cual el fabricante indica que una pieza funciona bien.",
        "Para planificar se suman meses al último hecho: si la última inspección fue en el mes 6 y se repite cada 6 meses, la próxima es en el mes 12. Los roles son: el técnico autorizado ejecuta; el supervisor planifica y revisa; el usuario avisa de las fallas y no interviene; el encargado de repuestos controla las piezas.",
        f"Planificar y registrar es parte de la seguridad: sin registro nadie sabe qué se hizo. {EMER} {AVISO}",
    ],
    vocab=[("hoja de vida", "historia escrita de un artefacto: instalación, revisiones, fallas y cambios"), ("orden de trabajo (OT)", "documento que encarga una tarea concreta"), ("informe técnico", "resumen de lo encontrado y lo recomendado"), ("repuesto", "pieza que reemplaza a otra desgastada"), ("vida útil", "tiempo en que el fabricante indica que una pieza funciona bien"), ("frecuencia", "cada cuánto tiempo se repite una tarea")],
    worked=[
        ("Próxima fecha", "Un artefacto de ejemplo tuvo su última revisión en el mes 4 y se revisa cada 3 meses. ¿En qué mes es la próxima?", ["Se suma la frecuencia al mes de la última revisión.", "4 más 3 son 7."], "En el mes 7"),
        ("Fin de vida útil", "Una pieza de ejemplo se instaló en el año 2 y tiene una vida útil de 4 años. ¿En qué año termina su vida útil?", ["Se suma la vida útil al año de instalación.", "2 más 4 son 6."], "En el año 6"),
    ],
    mistakes=[("Confundir la hoja de vida con la orden de trabajo.", "La hoja de vida es la historia del artefacto y la orden de trabajo encarga una tarea concreta.", "Usa cada documento para su función."),
              ("Guardar los registros solo en la memoria de quien trabajó.", "Cuando esa persona falta, nadie sabe qué se hizo.", "Anota todo en la bitácora y en la hoja de vida.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es la hoja de vida de un artefacto?", "La historia escrita del artefacto: instalación, revisiones, fallas y cambios", "Su manual de uso", "La factura de compra", "La hoja de vida acumula los hechos que le ocurren al artefacto."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es una orden de trabajo?", "El documento que encarga una tarea concreta", "La lista de todos los artefactos", "El certificado del instalador", "La OT dice qué se hace, dónde, quién y para cuándo."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es la vida útil de una pieza?", "El tiempo en que el fabricante indica que funciona bien", "El tiempo que tarda en llegar al taller", "El precio de reemplazarla", "La vida útil fija un horizonte para planificar el cambio."),
        ("=", "{F} Si la última inspección visual fue en el mes 6 y se repite cada 6 meses, ¿en qué mes es la próxima?", "6+6", "Se suma la frecuencia al mes de la última inspección.", ""),
        ("=", "{F} ¿En qué mes se cumple el primer año desde la instalación, que es cuando toca la revisión completa?", "0+12", "Se suma la frecuencia de 12 meses al mes de instalación.", ""),
        ("abc", "{F} ¿Quién ejecuta la revisión completa de un artefacto de gas según la pauta?", "Un técnico autorizado", "El usuario del artefacto", "Cualquier persona del condominio", "La pauta indica que la revisión de gas la hace un técnico autorizado."),
        ("=", "{F} ¿Cuántos años faltan para el cambio de la pieza por desgaste, si el artefacto lleva 2 años instalado?", "5-2", "Se resta el tiempo transcurrido a la vida útil de 5 años.", " años"),
        ("=", "{F} En un período de 24 meses desde la instalación, ¿cuántas inspecciones visuales contempla la pauta de cada 6 meses?", "24//6", "Se divide el período entre la frecuencia.", " inspecciones"),
        ("abc", "{F} El usuario nota que sale olor a gas de la cocina. ¿Qué corresponde hacer a quien está presente?", "No entrar ni accionar interruptores o llamas, avisar a un adulto responsable y a emergencias", "Abrir el artefacto para ver el problema", "Esperar a la próxima inspección programada", "Una fuga no espera la fecha de la pauta; se avisa de inmediato a emergencias."),
        ("abc", "{F} Un compañero propone no anotar la inspección porque «todo estaba bien». ¿Qué respuesta es correcta?", "Es mejor anotarla: el registro muestra que se hizo y cuándo", "Tiene razón: solo se anotan las fallas", "Se anota solo si el cliente lo pide", "Sin registro no se puede demostrar ni planificar la siguiente revisión."),
        ("=", "Un edificio de ejemplo tiene 9 artefactos y la pauta pide una revisión completa anual de cada uno. Si cada revisión toma 2 horas, ¿cuántas horas son al año?", "9*2", "Se multiplican los artefactos por las horas de cada revisión.", " horas"),
        ("abc", "¿Cuál es el rol del supervisor en la mantención?", "Planificar y revisar el trabajo", "Usar los artefactos sin intervenirlos", "Fabricar los repuestos", "El supervisor planifica y revisa; el técnico autorizado ejecuta."),
        ("abc", "¿Qué debe hacer el usuario de un artefacto que nota una falla?", "Avisar y no intervenir", "Repararlo con ayuda de un manual", "Pedir prestadas herramientas a un vecino", "El usuario informa; la intervención corresponde a personal autorizado."),
    ],
    ctx=("abc", "La administradora de un edificio de ejemplo pregunta si puede ahorrar suspendiendo las revisiones anuales «porque los artefactos funcionan». ¿Qué respondes?", "Que la mantención preventiva evita fallas graves y que la pauta se cumple con técnicos autorizados", "Que sí, mientras no haya fallas", "Que las haga un vecino para ahorrar", "Funcionar hoy no garantiza seguridad mañana; la pauta existe para prevenir."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué dice una pauta de mantención?", "Qué tarea se hace y cada cuánto tiempo", "Ordena las tareas periódicas con sus frecuencias."),
        ("¿Cómo se calcula la próxima fecha de una tarea periódica?", "Sumando la frecuencia a la fecha de la última", "La frecuencia indica cada cuánto se repite."),
        ("¿Dónde queda la historia escrita de un artefacto?", "En su hoja de vida", "La hoja de vida registra instalación, revisiones y fallas."),
    ],
    op=("Ficha de ejemplo: pauta de un artefacto de gas: inspección visual por técnico autorizado cada 4 meses; revisión completa por técnico autorizado cada 12 meses; pieza con vida útil de 6 años. El artefacto se instaló en el mes 0 y la última inspección visual fue en el mes 8. Escribe (a) en qué mes toca la próxima inspección visual, (b) cuántas inspecciones visuales caben en los primeros 24 meses, (c) cuántos años faltan para el cambio de la pieza si lleva 2 años instalado, (d) quién ejecuta la revisión completa.",
        "(a) 8 + 4 = mes 12. (b) 24 ÷ 4 = 6 inspecciones. (c) 6 − 2 = 4 años. (d) Un técnico autorizado.",
        ["calcula la próxima inspección", "calcula las inspecciones del período", "calcula los años que faltan", "indica quién ejecuta la revisión"],
        ["hoja con los cuatro resultados"],
        ["sumar mal los meses", "dividir al revés", "decir que el usuario hace la revisión completa"],
        "Pregunta: «¿qué documento anotarías la inspección?». Si no responde, pídele que relea la hoja de vida y la bitácora."),
    reinforce="Arma una pauta de ejemplo con tres tareas, su frecuencia y quién las ejecuta, sin describir cómo se hacen.",
    extend="Explica con un ejemplo cómo una hoja de vida ayuda a decidir si reparar o reemplazar un artefacto.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (caso en papel, de ejemplo, inventado). Una familia de 4 personas dice que su cuenta de agua subió, sin haber cambiado sus hábitos ni sus visitas. "
     "Lecturas del medidor al final de cada mes, en m³: enero 120; febrero 132; marzo 144; abril 156; mayo 198; junio 240. Precio del agua de ejemplo: $1.200 por m³. Cada mes tiene 30 días. 1 m³ equivale a 1.000 litros.")
build(
    O5, 3, F,
    use="Aprenderé a analizar una serie de lecturas de un medidor en papel, a detectar un consumo anormal y a proponer una conducta segura sin intervenir la red.",
    prior=["Sé restar lecturas.", "Sé convertir m³ a litros.", "Sé qué es un medidor."],
    explain=[
        "El medidor de agua acumula el consumo: cada lectura es mayor que la anterior. El consumo de un mes se obtiene restando la lectura del mes anterior a la lectura del mes. Si el consumo de varios meses es parecido y de pronto sube mucho sin explicación, se habla de un consumo anormal. Una causa posible es una fuga: pérdida de agua por un lugar donde no debería salir. Otras causas posibles son más personas, riego o un cambio de hábitos, por eso la lectura de la tabla no basta para asegurarlo.",
        "El análisis termina con una conclusión prudente: se dice qué muestran los datos, qué causas son posibles y qué se recomienda. La recomendación es avisar a personal autorizado o a la empresa de servicio para que revise; el análisis en papel no reemplaza esa revisión. Una pérdida pequeña y constante cuesta dinero y desperdicia agua, que es un bien escaso.",
        f"Los números son de ejemplo y no se interviene ninguna tubería. {EMER} {AVISO}",
    ],
    vocab=[("lectura del medidor", "número que acumula el consumo de agua hasta una fecha"), ("consumo mensual", "diferencia entre la lectura de un mes y la del mes anterior"), ("consumo anormal", "consumo que sube mucho sin una causa conocida"), ("fuga", "pérdida de agua por un lugar donde no debería salir"), ("conclusión prudente", "afirmación que dice lo que muestran los datos sin exagerar")],
    worked=[
        ("Calcular un consumo", "Un medidor de ejemplo marcó 300 m³ en agosto y 311 m³ en septiembre. ¿Cuál fue el consumo de septiembre?", ["Se resta la lectura de agosto a la de septiembre.", "311 menos 300 son 11 m³."], "11 m³"),
        ("Pasar a litros por día", "Un consumo extra de ejemplo de 6 m³ en un mes de 30 días, ¿cuántos litros por día es?", ["6 m³ son 6.000 litros.", "6.000 dividido en 30 son 200 litros por día."], "200 litros por día"),
    ],
    mistakes=[("Decir con seguridad que hay una fuga solo por la tabla.", "Otras causas, como más personas o riego, producen datos parecidos.", "Di que es una causa posible y pide una revisión de personal autorizado."),
              ("Sumar las lecturas en vez de restarlas para obtener el consumo.", "La lectura ya acumula el consumo anterior.", "Resta la lectura anterior a la lectura del mes.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿cómo se obtiene el consumo de un mes con un medidor?", "Restando la lectura del mes anterior a la lectura del mes", "Sumando todas las lecturas", "Multiplicando la lectura por 30", "El medidor acumula, por eso se resta la lectura anterior."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es un consumo anormal?", "Un consumo que sube mucho sin una causa conocida", "El consumo más bajo del año", "Un consumo igual todos los meses", "Un salto sin explicación es una señal para investigar."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es una fuga de agua?", "Una pérdida de agua por un lugar donde no debería salir", "El uso normal de una llave", "El cobro del servicio", "La fuga pierde agua sin que nadie la use."),
        ("=", "{F} ¿Cuál fue el consumo de febrero?", "132-120", "Se resta la lectura de enero a la de febrero.", " m³"),
        ("=", "{F} ¿Cuál fue el consumo de abril?", "156-144", "Se resta la lectura de marzo a la de abril.", " m³"),
        ("=", "{F} ¿Cuál fue el consumo de mayo?", "198-156", "Se resta la lectura de abril a la de mayo.", " m³"),
        ("abc", "{F} ¿Desde qué mes aparece el consumo anormal?", "Desde mayo, que sube a 42 m³ frente a los 12 m³ de los meses anteriores", "Desde febrero", "Desde abril", "Hasta abril el consumo fue de 12 m³ por mes y en mayo subió a 42 m³."),
        ("=", "{F} ¿Cuántos m³ por sobre el consumo normal se registran en un mes anormal?", "42-12", "Se resta el consumo normal al consumo del mes anormal.", " m³"),
        ("=", "{F} ¿Cuántos litros por día representa ese consumo extra en un mes de 30 días?", "30*1000//30", "30 m³ son 30.000 litros y se dividen entre los 30 días.", " litros"),
        ("=", "{F} ¿Cuánto cuesta por mes el consumo extra?", "30*1200", "Se multiplican los m³ extra por el precio de cada m³.", " pesos"),
        ("abc", "{F} Un técnico novato dice: «seguro hay una fuga en la cocina». ¿Qué conclusión es más prudente?", "Los datos muestran un consumo anormal desde mayo; una fuga es una causa posible y debe revisarla personal autorizado", "Es seguro que es una fuga y hay que romper el piso", "No es nada, porque la familia gasta mucho", "Los datos no prueban la causa; la conclusión prudente pide revisión."),
        ("abc", "{F} ¿Qué otra causa posible, distinta de una fuga, podría explicar un aumento?", "Más personas usando agua o riego", "Un cambio en el color de las tuberías", "Que el medidor suma las lecturas", "Un mayor uso de agua también eleva el consumo."),
        ("abc", "¿Qué corresponde recomendar a la familia de la ficha?", "Avisar a personal autorizado o a la empresa de servicio para que revise, sin abrir paredes ni intervenir tuberías", "Romper el piso para buscar la fuga", "Probar con herramientas hasta encontrarla", "El análisis no reemplaza la revisión de personal autorizado."),
    ],
    ctx=("abc", "El dueño de una casa de ejemplo te pide: «mira mi tabla y dime exactamente dónde está la fuga». ¿Qué respondes?", "Que la tabla muestra solo un consumo anormal, no dónde está la causa, y que debe llamar a personal autorizado", "Que está en la cocina, sin dudar", "Que rompa el muro para ver", "Una tabla de lecturas no ubica una fuga; la revisión en terreno la hace personal autorizado."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se calcula el consumo mensual?", "Lectura del mes menos lectura del mes anterior", "El medidor acumula el consumo, por eso se restan lecturas."),
        ("¿Cuántos litros tiene un metro cúbico?", "1.000 litros", "Esa equivalencia sirve para pasar de m³ a litros."),
        ("¿Qué hace una conclusión prudente?", "Dice lo que muestran los datos y las causas posibles", "No afirma una causa que los datos no prueban."),
    ],
    op=("Ficha de ejemplo: lecturas del medidor al final de cada mes, en m³: julio 400; agosto 410; septiembre 420; octubre 460; noviembre 500. Precio de ejemplo: $1.000 por m³; meses de 30 días. Escribe (a) el consumo de cada mes de agosto a noviembre, (b) desde qué mes es anormal, (c) cuántos litros por día son los m³ de más de un mes anormal, (d) una conclusión prudente y qué recomendarías.",
        "(a) Agosto 10, septiembre 10, octubre 40, noviembre 40 m³. (b) Desde octubre. (c) 30 m³ de más son 30.000 litros y, entre 30 días, 1.000 litros por día. (d) «El consumo es anormal desde octubre; una fuga es una causa posible y debe revisarla personal autorizado»; sin intervenir tuberías.",
        ["calcula los consumos mensuales", "identifica el mes desde el que es anormal", "calcula los litros por día", "redacta una conclusión prudente"],
        ["hoja con la tabla de consumos y la conclusión"],
        ["sumar las lecturas", "afirmar con seguridad que hay una fuga", "proponer romper una pared"],
        "Pregunta: «¿qué otra causa podría explicar el aumento?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa cinco lecturas de un medidor con un salto en la cuarta y calcula los consumos de cada mes.",
    extend="Explica con un ejemplo por qué una conclusión prudente es más útil que una afirmación sin prueba.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (matriz de riesgo y órdenes de trabajo de ejemplo, inventadas). Probabilidad de que ocurra el problema (1 = baja, 3 = alta) y gravedad de sus consecuencias (1 = leve, 3 = grave). Puntaje = probabilidad × gravedad. "
     "Prioridad: alta con 6 o más puntos, media con 3 a 5 puntos, baja con 1 o 2 puntos; con igual puntaje se atiende primero la de mayor gravedad. "
     "OT-1: llave de un lavamanos que gotea (probabilidad 3, gravedad 1). OT-2: revisión pendiente de un artefacto de gas fuera del plazo de la pauta (probabilidad 2, gravedad 3). "
     "OT-3: calentador de agua con temperatura variable (probabilidad 3, gravedad 2). OT-4: cambio de un sello menor en una llave de bodega (probabilidad 2, gravedad 1). Regla aparte: ante olor a gas o riesgo inmediato no se usa la matriz; se actúa como emergencia.")
build(
    O5, 4, F,
    use="Aprenderé a priorizar órdenes de trabajo con una matriz de riesgo, a distinguir un caso de emergencia y a justificar el orden por escrito.",
    prior=["Sé multiplicar números pequeños.", "Sé ordenar de mayor a menor.", "Sé qué es una orden de trabajo."],
    explain=[
        "No todas las órdenes de trabajo son igual de urgentes. Una matriz de riesgo ayuda a decidir el orden: para cada problema se estima la probabilidad de que ocurra y la gravedad de sus consecuencias, y se multiplican para obtener un puntaje. A mayor puntaje, mayor prioridad. Si dos órdenes empatan, se atiende primero la de mayor gravedad, porque sus consecuencias son peores.",
        "La matriz es una herramienta de planificación, no sustituye al juicio. Hay situaciones de emergencia, como el olor a gas, un atrapamiento o una caída, que no esperan en una fila: se actúa de inmediato avisando a un adulto responsable y a emergencias, sin entrar al lugar. Las estimaciones de probabilidad y gravedad las hacen personas capacitadas, y el orden decidido se anota con su justificación.",
        f"Los puntajes de esta ficha son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("matriz de riesgo", "tabla que combina probabilidad y gravedad para priorizar"), ("probabilidad", "qué tan posible es que ocurra un problema"), ("gravedad", "qué tan graves serían sus consecuencias"), ("prioridad", "orden de atención de las tareas"), ("emergencia", "situación que exige actuar de inmediato avisando a quienes pueden intervenir")],
    worked=[
        ("Calcular el puntaje", "Una orden de ejemplo tiene probabilidad 2 y gravedad 3. ¿Qué puntaje y prioridad tiene si en la regla de ejemplo la prioridad es alta con 6 o más puntos?", ["Se multiplican: 2 por 3 son 6.", "6 puntos corresponde a prioridad alta."], "6 puntos: prioridad alta"),
        ("Desempate", "Dos órdenes de ejemplo empatan con 6 puntos: una con gravedad 3 y otra con gravedad 2. ¿Cuál se atiende primero?", ["Con igual puntaje se atiende primero la de mayor gravedad.", "La de gravedad 3 va primero."], "La de gravedad 3"),
    ],
    mistakes=[("Atender primero la tarea más fácil.", "La urgencia depende del riesgo, no de la facilidad.", "Ordena por puntaje y gravedad."),
              ("Poner en la fila de la matriz una emergencia como el olor a gas.", "Una emergencia no espera su turno.", "Actúa de inmediato: avisa a un adulto responsable y a emergencias, sin entrar.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué mide la gravedad en una matriz de riesgo?", "Qué tan graves serían las consecuencias del problema", "Qué tan probable es que ocurra", "Cuánto cuesta la reparación", "La gravedad evalúa las consecuencias, no la probabilidad."),
        ("abc", "En Instalaciones Sanitarias: ¿cómo se obtiene el puntaje de una orden de trabajo?", "Multiplicando probabilidad por gravedad", "Sumando probabilidad y gravedad", "Dividiendo la gravedad entre la probabilidad", "La ficha define el puntaje como probabilidad por gravedad."),
        ("abc", "En Instalaciones Sanitarias: ¿qué se hace cuando dos órdenes empatan en puntaje?", "Se atiende primero la de mayor gravedad", "Se atiende primero la más barata", "Se atiende primero la más fácil", "Con igual puntaje la gravedad desempata, porque sus consecuencias son peores."),
        ("=", "{F} ¿Qué puntaje tiene la OT-1, la llave que gotea?", "3*1", "Se multiplican la probabilidad y la gravedad de la OT-1.", " puntos"),
        ("=", "{F} ¿Qué puntaje tiene la OT-2, la revisión pendiente de un artefacto de gas?", "2*3", "Se multiplican la probabilidad y la gravedad de la OT-2.", " puntos"),
        ("=", "{F} ¿Qué puntaje tiene la OT-3, el calentador con temperatura variable?", "3*2", "Se multiplican la probabilidad y la gravedad de la OT-3.", " puntos"),
        ("=", "{F} ¿Qué puntaje tiene la OT-4, el sello menor de la bodega?", "2*1", "Se multiplican la probabilidad y la gravedad de la OT-4.", " puntos"),
        ("abc", "{F} ¿Qué órdenes tienen prioridad alta?", "La OT-2 y la OT-3", "La OT-1 y la OT-4", "Solo la OT-3", "La OT-2 y la OT-3 suman 6 puntos, el mínimo para prioridad alta."),
        ("abc", "{F} ¿Cuál es el orden de atención correcto?", "OT-2, OT-3, OT-1 y OT-4", "OT-3, OT-2, OT-1 y OT-4", "OT-1, OT-2, OT-3 y OT-4", "La OT-2 y la OT-3 empatan en 6 y gana la de gravedad 3; luego sigue la de 3 y la de 2."),
        ("abc", "{F} Una persona avisa que hay olor a gas en un departamento. ¿Cómo se trata?", "Como emergencia: no entrar, avisar a un adulto responsable y a emergencias, sin usar la matriz", "Como una OT más, con prioridad alta", "Se agrega a la fila después de la OT-3", "Una fuga posible es una emergencia y no espera su turno."),
        ("abc", "{F} Un compañero propone atender primero la OT-4 porque es la más rápida. ¿Qué respuesta es correcta?", "No: se ordena por riesgo, y la OT-4 tiene el menor puntaje", "Sí: lo rápido siempre va primero", "Sí, si la OT-4 es barata", "La prioridad se decide por riesgo y no por rapidez."),
        ("=", "{F} ¿Cuántos puntos más tiene la OT-2 que la OT-1?", "2*3-3*1", "Se resta el puntaje de la OT-1 al de la OT-2.", " puntos"),
        ("abc", "¿Cuál es la mejor justificación escrita del orden?", "Puntaje de cada orden, desempate por gravedad y excepción de emergencias", "Se hizo lo más urgente", "El jefe lo decidió", "Una justificación completa muestra los cálculos y las reglas aplicadas."),
    ],
    ctx=("abc", "Una administradora de ejemplo te pregunta por qué la revisión del artefacto de gas se atiende antes que la llave que gotea, si la llave molesta más. ¿Qué respondes?", "Que la revisión de gas tiene mayor puntaje por su gravedad, aunque la llave sea más molesta", "Que fue una decisión al azar", "Que el gas siempre se atiende primero sin cálculo", "La matriz prioriza por riesgo y no por molestia."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué se multiplica en la matriz de riesgo?", "Probabilidad por gravedad", "El producto resume qué tan urgente es la orden."),
        ("¿Cómo se trata el olor a gas?", "Como emergencia, sin esperar turno", "No entra a la fila de la matriz."),
        ("¿Qué se hace con un empate en puntaje?", "Se atiende primero la de mayor gravedad", "Sus consecuencias serían peores, por eso se atiende primero."),
    ],
    op=("Ficha de ejemplo. Regla de ejemplo: puntaje = probabilidad × gravedad; prioridad alta con 6 o más puntos, media con 3 a 5 y baja con 1 o 2; con igual puntaje va primero la de mayor gravedad, y si empatan en todo, por orden de llegada. OT-A: ducha con goteo (probabilidad 3, gravedad 1). OT-B: revisión de un artefacto de gas fuera de plazo (probabilidad 2, gravedad 3). OT-C: calentador con temperatura variable (probabilidad 2, gravedad 3). OT-D: cambio de un sello en una llave exterior (probabilidad 1, gravedad 1). Escribe (a) el puntaje de cada orden, (b) la prioridad de cada una, (c) el orden de atención con la regla de desempate, (d) qué harías si alguien avisara de un olor a gas.",
        "(a) A: 3; B: 6; C: 6; D: 1. (b) A media; B alta; C alta; D baja. (c) B y C empatan en 6 y tienen la misma gravedad, por lo que van en el orden de llegada B, C; luego A y D. (d) Emergencia: no entrar, avisar a un adulto responsable y a emergencias.",
        ["calcula los puntajes", "asigna prioridades", "ordena con el desempate", "trata el olor a gas como emergencia"],
        ["hoja con los puntajes, el orden y la conducta ante la emergencia"],
        ["sumar en lugar de multiplicar", "ordenar por facilidad", "meter la emergencia en la fila"],
        "Pregunta: «¿qué haces si dos órdenes empatan y tienen la misma gravedad?». Si no responde, pídele que proponga un criterio, como el orden de llegada."),
    reinforce="Escribe cuatro problemas de mantención, con su probabilidad y gravedad, calcula los puntajes y ordénalos.",
    extend="Explica con un ejemplo por qué una matriz de riesgo ayuda a decidir pero no reemplaza el juicio de una persona capacitada.",
)

# ============================================================ OAE-05, clase 5
F = ("Ficha 5 (decisión de ejemplo, inventada). Un artefacto de agua caliente de ejemplo presenta una falla. Alternativa A, reparar: costo $60.000; vida útil restante estimada, 2 años. "
     "Alternativa B, reemplazar: costo $180.000; vida útil estimada, 8 años. El repuesto de la alternativa A se consigue. Cualquiera que sea la alternativa, la intervención la hace personal autorizado. "
     "Lista de control de cierre de la orden de trabajo (10 puntos): cumplen 9; falta firmar la bitácora.")
build(
    O5, 5, F,
    use="Aprenderé a comparar reparar y reemplazar con un costo por año y condiciones de seguridad, y a verificar la calidad del cierre de una orden de trabajo.",
    prior=["Sé dividir un costo entre años.", "Sé calcular un porcentaje.", "Sé qué es una orden de trabajo."],
    explain=[
        "Para decidir entre reparar y reemplazar se compara el costo por año de uso: el costo de la alternativa dividido en los años de vida útil que se espera obtener. Pero el costo no es lo único: también cuentan la disponibilidad de repuestos, el riesgo si el artefacto vuelve a fallar y lo que recomienda el fabricante. En artefactos de agua caliente o de gas, cualquiera sea la alternativa, la intervención la hace personal autorizado.",
        "El cierre de una orden de trabajo se verifica con una lista de control: se revisa que estén la descripción de lo hecho, los repuestos usados, la fecha, la firma y el aviso al usuario. Los puntos que faltan se completan antes de cerrar. Un cierre sin firma ni registro no demuestra que el trabajo se hizo ni quién fue responsable.",
        f"Los precios son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("costo por año", "costo de una alternativa dividido en los años de vida útil esperados"), ("reemplazar", "cambiar el artefacto por otro nuevo"), ("repuesto disponible", "pieza que realmente se puede conseguir"), ("cierre de la orden", "momento en que se da por terminada una orden de trabajo, con registro"), ("lista de control", "pauta de puntos a revisar con «cumple» o «no cumple»")],
    worked=[
        ("Costo por año", "Una alternativa de ejemplo cuesta $90.000 y se espera que dure 3 años. ¿Cuánto cuesta por año?", ["Se divide el costo entre los años.", "90.000 dividido en 3 son 30.000."], "$30.000 por año"),
        ("Porcentaje de la lista", "Una lista de control de ejemplo tiene 8 puntos y cumplen 6. ¿Qué porcentaje cumple?", ["Se divide lo que cumple entre el total.", "6 por 100 dividido en 8 son 75 %."], "75 %"),
    ],
    mistakes=[("Elegir siempre la alternativa de menor costo inmediato.", "Una reparación barata que dura poco puede costar más por año.", "Compara el costo por año y las condiciones de seguridad."),
              ("Cerrar la orden sin firma porque «el trabajo ya está hecho».", "Sin registro no hay constancia ni responsable.", "Completa los puntos pendientes antes de cerrar.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es el costo por año de una alternativa?", "Su costo dividido en los años de vida útil esperados", "Su costo multiplicado por los años", "El costo de la última cuenta", "El costo por año reparte el gasto en el tiempo que se espera que dure."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es un repuesto disponible?", "Una pieza que realmente se puede conseguir", "Una pieza que existe en teoría", "Un artefacto completo", "Si el repuesto no se consigue, reparar no es posible."),
        ("abc", "En Instalaciones Sanitarias: ¿para qué sirve la lista de control de cierre de una orden?", "Para verificar que el trabajo quede completo y registrado", "Para calcular el costo por año", "Para elegir al técnico", "La lista asegura que no falten registros ni firmas."),
        ("=", "{F} ¿Cuánto cuesta por año la alternativa A, reparar?", "60000//2", "Se divide el costo de reparar entre los 2 años de vida útil.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta por año la alternativa B, reemplazar?", "180000//8", "Se divide el costo de reemplazar entre los 8 años de vida útil.", " pesos"),
        ("abc", "{F} Según el costo por año, ¿qué alternativa conviene?", "La alternativa B, porque su costo por año es menor", "La alternativa A, porque su costo inicial es menor", "Ninguna, porque cuestan lo mismo por año", "B cuesta 22.500 por año y A cuesta 30.000 por año."),
        ("=", "{F} ¿Cuántos pesos por año ahorra la alternativa B respecto de la A?", "60000//2-180000//8", "Se resta el costo por año de B al de A.", " pesos"),
        ("=", "{F} ¿Qué porcentaje de los puntos de la lista de control cumple?", "9*100//10", "Se divide lo que cumple entre el total y se pasa a porcentaje.", " %"),
        ("abc", "{F} ¿Qué corresponde con el punto que falta, la firma de la bitácora?", "Completarlo antes de cerrar la orden", "Cerrar igual, porque cumple el 90 %", "Firmar a nombre de otra persona", "Un cierre incompleto no deja responsable ni constancia."),
        ("abc", "{F} Un compañero propone que la reparación la haga el dueño para ahorrar. ¿Qué respuesta es correcta?", "No: en artefactos de agua caliente o gas la intervención la hace personal autorizado", "Sí: reparar es fácil si hay un repuesto", "Sí, con la ayuda del manual", "La seguridad exige personal autorizado, sea reparar o reemplazar."),
        ("abc", "{F} Si el repuesto de la alternativa A no se consiguiera, ¿qué ocurriría?", "Reparar dejaría de ser posible y quedaría reemplazar", "Reparar sería igualmente posible con otra pieza cualquiera", "Habría que usar un repuesto improvisado", "Sin repuesto adecuado no se repara; improvisar es peligroso."),
        ("=", "Otra alternativa de ejemplo cuesta $150.000 y se espera que dure 5 años. ¿Cuánto cuesta por año?", "150000//5", "Se divide el costo entre los años de vida útil.", " pesos"),
        ("abc", "¿Cuál es el mejor registro de la decisión?", "Costo por año de cada alternativa, disponibilidad de repuestos, riesgo y quién decide y ejecuta", "Se eligió reemplazar", "Es mejor lo más barato", "Un buen registro permite revisar la decisión."),
    ],
    ctx=("abc", "Un cliente de ejemplo te dice: «repara el calentador tú, que sale más barato que llamar a la empresa». ¿Qué respondes?", "Que no puedes: la reparación la hace personal autorizado, y puedes ayudarlo a comparar costos por escrito", "Que sí, pero solo si lo supervisa un vecino", "Que sí, si compra el repuesto más barato", "Un estudiante no repara artefactos de agua caliente ni de gas; sí puede comparar costos en papel."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se calcula el costo por año?", "Costo dividido en los años de vida útil", "Reparte el gasto en el tiempo esperado de uso."),
        ("¿Quién interviene un artefacto de agua caliente o de gas?", "Personal autorizado", "La intervención es de riesgo alto."),
        ("¿Qué se hace con un punto pendiente de la lista de control?", "Se completa antes de cerrar la orden", "Un cierre incompleto no deja constancia."),
    ],
    op=("Ficha de ejemplo: alternativa A, reparar un artefacto: $80.000 y vida útil restante de 2 años; alternativa B, reemplazarlo: $240.000 y vida útil de 8 años. La lista de control de cierre tiene 8 puntos y cumplen 6. Escribe (a) el costo por año de cada alternativa, (b) cuál conviene por costo, (c) el porcentaje de la lista que cumple, (d) quién interviene el artefacto.",
        "(a) A: 80.000 ÷ 2 = 40.000 pesos por año. B: 240.000 ÷ 8 = 30.000 pesos por año. (b) La B. (c) 6 de 8 son 75 %. (d) Personal autorizado.",
        ["calcula ambos costos por año", "elige con el criterio de costo por año", "calcula el porcentaje", "indica quién interviene"],
        ["hoja con los cálculos y la conclusión"],
        ["comparar solo el costo inicial", "dividir al revés", "proponer que el dueño repare"],
        "Pregunta: «¿qué otra condición, además del costo, importa?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula en papel el costo por año de tres alternativas de ejemplo con costos de $50.000, $120.000 y $200.000 y vidas útiles de 2, 4 y 8 años.",
    extend="Explica con un ejemplo por qué una reparación barata puede salir más cara a largo plazo.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). En la parcela ficticia «Los Quillayes» viven 5 personas en una casa y hay un huerto. El proyecto de ejemplo tiene 6 láminas e incluye: la red de agua potable de la casa (18 m), "
     "la red de riego del huerto, en 3 sectores (27 m), y la red de evacuación de las aguas servidas de la casa hacia un sistema de ejemplo. "
     "Riesgos anotados: zanjas, una bomba de agua que funciona con electricidad, aguas servidas y caídas.")
build(
    O6, 1, F,
    use="Aprenderé qué redes tiene una vivienda con huerto, por qué el agua potable y el agua de riego se mantienen separadas y qué riesgos y cuidados ambientales hay en estas redes.",
    prior=["Sé qué es una red sanitaria.", "Sé leer una ficha con documentos.", "Sé que las zanjas y las cámaras son de riesgo alto."],
    explain=[
        "El agua potable es agua apta para beber y cocinar, que cumple la norma sanitaria vigente. La red de riego lleva agua a las plantas, y esa agua puede tener una calidad distinta. Por eso las dos redes se mantienen separadas e identificadas: si el agua de riego llegara a una llave de la casa, podría causar enfermedades. La red de evacuación retira las aguas servidas de los artefactos, y esas aguas contienen microbios (riesgo biológico). La autoridad sanitaria vigila el agua potable y la salud de las personas.",
        "Los riesgos de estas redes son el derrumbe y la caída en zanjas, el contacto con aguas servidas, y la mezcla de agua con electricidad en equipos como la bomba, que impulsa el agua. Solo personal autorizado interviene la electricidad y las bombas. El cuidado ambiental exige usar el agua con responsabilidad, evitar pérdidas y manejar los residuos de la obra según el plan.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("agua potable", "agua apta para beber y cocinar, que cumple la norma sanitaria vigente"), ("red de riego", "red que lleva agua a las plantas"), ("bomba", "equipo que impulsa el agua"), ("aguas servidas", "aguas usadas de los artefactos, que contienen microbios"), ("riesgo biológico", "posibilidad de contagio por microbios"), ("autoridad sanitaria", "institución que vigila el agua potable y la salud de las personas")],
    worked=[
        ("Reconocer la red", "En un plano de ejemplo, una tubería lleva agua a las hileras de un huerto. ¿Qué red es?", ["La red que lleva agua a las plantas es la de riego.", "No debe unirse con la red de agua potable."], "La red de riego"),
        ("Sumar metros", "Una parcela de ejemplo tiene una red potable de 20 m y una de riego de 35 m. ¿Cuántos metros suman?", ["Se suman los metros de las dos redes.", "20 más 35 son 55."], "55 m"),
    ],
    mistakes=[("Conectar la red de riego con la de agua potable «para ahorrar tubería».", "El agua de riego puede contaminar el agua que se bebe.", "Mantén las redes separadas e identificadas, según el proyecto."),
              ("Pensar que, por saber leer los planos, ya se puede manipular una bomba conectada a la electricidad.", "Mezclar agua y electricidad es de riesgo alto.", "Deja las bombas a personal autorizado.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es el agua potable?", "Agua apta para beber y cocinar que cumple la norma sanitaria vigente", "Cualquier agua que se vea transparente", "Agua de riego pasada por una tela", "El agua potable no se define por cómo se ve, sino por cumplir la norma sanitaria."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es una red de riego?", "Una red que lleva agua a las plantas", "Una red que lleva agua para beber a la casa", "Una red que retira las aguas servidas", "La red de riego abastece cultivos, no la casa."),
        ("abc", "¿Por qué se mantienen separadas e identificadas las redes de riego y de agua potable?", "Para evitar que agua de calidad distinta llegue a donde se bebe", "Para que el riego tenga más presión", "Para ahorrar tubería", "Una mezcla podría contaminar el agua potable y causar enfermedades."),
        ("abc", "{F} ¿Qué elemento de la ficha reúne agua y electricidad?", "La bomba de agua", "La red de evacuación", "La lámina del proyecto", "La bomba impulsa el agua con electricidad, y esa mezcla es de riesgo alto."),
        ("abc", "{F} ¿Qué red retira las aguas usadas de la casa?", "La red de evacuación", "La red de riego", "La red de agua potable", "La evacuación retira las aguas servidas de los artefactos."),
        ("=", "{F} ¿Cuántos metros suman las redes de agua potable y de riego?", "18+27", "Se suman los metros de las dos redes de la ficha.", " m"),
        ("=", "{F} Se imprimen 4 copias de todas las láminas del proyecto. ¿Cuántas láminas son en total?", "6*4", "Se multiplican las láminas por el número de copias.", " láminas"),
        ("abc", "En una obra de ejemplo, una persona observa que una zanja se derrumbó y alguien quedó atrapado. ¿Qué corresponde según las reglas generales?", "No entrar a la zanja, avisar a un adulto responsable y a emergencias", "Entrar a sacarlo de inmediato", "Esperar a ver si se libera solo", "Entrar a una zanja derrumbada puede producir otro atrapamiento; se avisa a quienes pueden rescatar."),
        ("abc", "{F} Un constructor propone conectar un punto de riego a la red de agua potable «para que haya más presión». ¿Qué respuesta es correcta?", "No: las redes se mantienen separadas, y cualquier cambio lo decide el proyectista", "Sí: más presión es siempre mejor", "Sí, si se anota en la bitácora", "Unir las redes puede contaminar el agua potable."),
        ("ab", "Un estudiante de ejemplo ve que la bomba de la parcela hace ruido y quiere abrirla para revisarla. ¿Qué corresponde?", "No hacerlo: avisar a personal autorizado", "Abrirla con cuidado, porque ya estudió sanitarias", "Una bomba conectada a la electricidad es de riesgo alto; este cuaderno no habilita para abrirla."),
        ("abc", "Una persona de ejemplo ve un derrame de aguas servidas en un sector de la obra. ¿Qué corresponde?", "Alejarse, impedir que otros se acerquen y avisar al responsable de la obra", "Limpiarlo de inmediato con las manos desnudas", "Taparlo con tierra sin avisar", "Las aguas servidas tienen riesgo biológico; se avisa a quien corresponde."),
        ("=", "{F} La lectura detallada del proyecto toma 2 horas por lámina. ¿Cuántas horas toma leer las 6 láminas?", "6*2", "Se multiplican las láminas por las horas de cada una.", " horas"),
        ("abc", "Antes de leer los planos, ¿qué documento conviene revisar para saber qué materiales y reglas rigen la obra?", "Las especificaciones técnicas", "La lista de precios del proveedor", "El calendario de vacaciones", "Las especificaciones fijan materiales y reglas del proyecto."),
    ],
    ctx=("abc", "El dueño de una parcela de ejemplo te dice: «arreglé el riego conectándolo a la llave de la cocina; así tengo agua rápida». ¿Qué le respondes?", "Que debe separar las redes y consultar a un instalador autorizado, porque el agua de riego puede contaminar el agua potable", "Que está bien si el agua se ve limpia", "Que lo deje así y lo revise el próximo año", "Unir ambas redes es un riesgo sanitario que debe corregir personal autorizado."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué red lleva agua para beber?", "La red de agua potable", "Es la que cumple la norma sanitaria."),
        ("¿Por qué se separan las redes de riego y de agua potable?", "Para evitar contaminar el agua que se bebe", "El agua de riego puede tener otra calidad."),
        ("¿Quién interviene una bomba conectada a la electricidad?", "Personal autorizado", "Mezclar agua y electricidad es de riesgo alto."),
    ],
    op=("Ficha de ejemplo: una parcela tiene una casa y un huerto. La red de agua potable mide 22 m, la de riego 30 m y el proyecto tiene 5 láminas. Escribe (a) cuántos metros suman las dos redes, (b) cuántas láminas hay que imprimir si se piden 3 copias, (c) por qué las redes se mantienen separadas, (d) qué tarea de la parcela no te corresponde y quién la hace.",
        "(a) 22 + 30 = 52 m. (b) 5 × 3 = 15 láminas. (c) Para que el agua de riego no contamine el agua que se bebe. (d) Intervenir la bomba o la electricidad: lo hace personal autorizado.",
        ["suma los metros", "calcula las láminas", "explica la separación de las redes", "reconoce una tarea que no le corresponde"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal", "proponer unir las redes", "decir que puede intervenir la bomba"],
        "Pregunta: «¿qué pasaría si el agua de riego llegara a la llave de la cocina?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Escribe una lista de cuatro riesgos de una parcela con casa y huerto y, junto a cada uno, una medida general de prevención.",
    extend="Explica con un ejemplo por qué el agua es un recurso que conviene cuidar en una instalación sanitaria.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (datos de ejemplo, inventados). Casa de 5 personas; dotación de ejemplo: 150 litros por persona por día. Riego del huerto en 3 sectores: sector 1, 20 litros por minuto (L/min); sector 2, 30 L/min; sector 3, 10 L/min. "
     "Caudal disponible de la fuente de ejemplo: 40 L/min. Regla de planilla: los sectores que riegan a la vez no pueden pedir más caudal que el disponible.")
build(
    O6, 2, F,
    use="Aprenderé los conceptos de caudal, dotación y sector de riego, y a hacer cálculos simples en una planilla de papel.",
    prior=["Sé multiplicar y sumar.", "Sé qué es una red de riego.", "Sé convertir horas a minutos."],
    explain=[
        "El caudal es el volumen de agua que pasa por un punto en cierto tiempo; se expresa, por ejemplo, en litros por minuto (L/min). La dotación es la cantidad de agua que se calcula para cada persona por día. El consumo diario de una vivienda es la dotación multiplicada por el número de personas. Con 3 personas y una dotación de 100 litros por persona por día, el consumo es 300 litros por día.",
        "En el riego, el huerto se divide en sectores: partes que se riegan por separado. Cada sector pide un caudal. El aspersor reparte el agua como una lluvia; el goteo la entrega gota a gota cerca de la planta. Un temporizador es el equipo que abre y cierra el riego según un horario. Un estanque almacena agua. Los datos del cálculo vienen del proyecto, y los valores reales los fijan el proyectista y la norma vigente.",
        f"Todos los números de este cuaderno son de ejemplo para calcular en papel. {EMER} {AVISO}",
    ],
    vocab=[("caudal", "volumen de agua que pasa por un punto en cierto tiempo, por ejemplo en litros por minuto"), ("dotación", "cantidad de agua calculada por persona por día"), ("consumo diario", "dotación multiplicada por el número de personas"), ("sector de riego", "parte del huerto que se riega por separado"), ("aspersor", "dispositivo que reparte el agua como lluvia"), ("goteo", "forma de riego que entrega el agua gota a gota cerca de la planta"), ("estanque", "depósito que almacena agua")],
    worked=[
        ("Consumo diario", "Una familia de ejemplo de 4 personas tiene una dotación de 120 litros por persona por día. ¿Cuántos litros usa por día?", ["Se multiplica la dotación por las personas.", "120 por 4 son 480."], "480 litros por día"),
        ("Volumen de riego", "Un sector de ejemplo con un caudal de 15 L/min riega durante 20 minutos. ¿Cuántos litros entrega?", ["Se multiplica el caudal por los minutos.", "15 por 20 son 300."], "300 litros")
    ],
    mistakes=[("Confundir caudal con volumen.", "El caudal es volumen por unidad de tiempo; el volumen es la cantidad total.", "Multiplica el caudal por el tiempo para obtener el volumen."),
              ("Sumar solo dos de los tres sectores al revisar si cumplen con el caudal disponible.", "Los sectores que riegan a la vez deben sumarse todos.", "Suma los caudales de todos los sectores que riegan juntos.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es el caudal?", "El volumen de agua que pasa por un punto en cierto tiempo", "La cantidad total de agua de un estanque", "La altura a que sube el agua", "El caudal mide volumen por unidad de tiempo, por ejemplo litros por minuto."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es la dotación?", "La cantidad de agua calculada por persona por día", "El caudal de una bomba", "El largo de una tubería", "La dotación es el agua prevista por persona y por día."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es un sector de riego?", "Una parte del huerto que se riega por separado", "Un tipo de aspersor", "Una tubería de evacuación", "Los sectores permiten regar por partes y repartir el caudal."),
        ("=", "{F} ¿Cuántos litros usa la casa por día?", "5*150", "Se multiplica la dotación por las personas.", " litros"),
        ("=", "{F} ¿Cuántos litros usa la casa en una semana de 7 días?", "5*150*7", "Se multiplica el consumo diario por 7 días.", " litros"),
        ("=", "{F} ¿Cuántos L/min piden juntos los sectores 1 y 3?", "20+10", "Se suman los caudales de los dos sectores.", " L/min"),
        ("abc", "{F} ¿Pueden regar a la vez los sectores 1 y 3?", "Sí, porque piden 30 L/min y hay 40 L/min disponibles", "No, porque piden más de 40 L/min", "No se puede saber", "30 L/min no supera el caudal disponible de 40 L/min."),
        ("abc", "{F} ¿Pueden regar a la vez los sectores 1 y 2?", "No, porque piden 50 L/min y hay 40 L/min disponibles", "Sí, porque cada sector pide menos de 40 L/min", "Sí, si se abre más la llave", "50 L/min supera el caudal disponible de 40 L/min."),
        ("=", "{F} ¿Cuántos litros entrega el sector 2 si riega durante 30 minutos?", "30*30", "Se multiplica el caudal por los minutos de riego.", " litros"),
        ("=", "{F} ¿Cuántos litros entrega el sector 3 en 1 hora?", "10*60", "Una hora son 60 minutos y se multiplica por el caudal.", " litros"),
        ("abc", "{F} Un compañero propone regar los tres sectores a la vez «y ver qué pasa». ¿Qué respuesta es correcta?", "No: los tres piden 60 L/min, más que los 40 disponibles, y la regla de planilla no se cumple", "Sí: la regla de planilla es solo una sugerencia", "Sí, si se riega poco tiempo", "La suma de los tres sectores supera el caudal disponible."),
        ("=", "{F} ¿Cuántos L/min piden los tres sectores si riegan a la vez?", "20+30+10", "Se suman los caudales de los tres sectores.", " L/min"),
        ("abc", "¿Qué equipo abre y cierra el riego según un horario?", "El temporizador", "El aspersor", "El estanque", "El temporizador programa cuándo se riega."),
    ],
    ctx=("abc", "Un vecino de ejemplo quiere alargar el riego «porque el huerto se ve seco» y pide que alguien manipule la bomba. ¿Qué respondes?", "Que consulte al proyectista o a personal autorizado; la bomba y la electricidad no se manipulan sin autorización", "Que manipules tú la bomba, porque estudiaste sanitarias", "Que la abra y la deje funcionando de noche", "Cambiar el riego o la bomba exige personal autorizado y respetar el diseño."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se calcula el consumo diario de una vivienda?", "Dotación por número de personas", "El consumo diario multiplica la dotación por las personas."),
        ("¿Cómo se obtiene el volumen que entrega un sector?", "Multiplicando el caudal por el tiempo", "Un caudal por minutos da litros."),
        ("¿Qué se compara con el caudal disponible?", "La suma de los caudales de los sectores que riegan a la vez", "No pueden pedir más de lo que hay."),
    ],
    op=("Ficha de ejemplo: casa de 4 personas con dotación de ejemplo de 120 litros por persona por día. Riego en 3 sectores de 15, 25 y 10 L/min; caudal disponible de ejemplo: 40 L/min. Escribe (a) el consumo diario de la casa, (b) cuántos litros entrega el sector de 25 L/min en 20 minutos, (c) si riegan a la vez el sector de 15 y el de 25, y por qué, (d) qué persona interviene la bomba.",
        "(a) 4 × 120 = 480 litros por día. (b) 25 × 20 = 500 litros. (c) Sí, porque piden 15 + 25 = 40 L/min, que no supera 40 L/min disponibles. (d) Personal autorizado.",
        ["calcula el consumo diario", "calcula el volumen del sector", "compara con el caudal disponible", "indica quién interviene la bomba"],
        ["hoja con los cuatro resultados"],
        ["multiplicar mal", "no sumar los sectores que riegan a la vez", "decir que el dueño interviene la bomba"],
        "Pregunta: «¿qué pasaría si se agrega el sector de 10 L/min?». Si no responde, pídele que repita la suma con tres sectores."),
    reinforce="Calcula en papel el consumo diario de una casa de 6 personas con una dotación de ejemplo de 110 litros por persona.",
    extend="Explica con un ejemplo por qué el caudal disponible limita cuántos sectores pueden regar al mismo tiempo.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (caso en papel, de ejemplo, inventado). Edificio de 12 departamentos con 4 personas cada uno; dotación de ejemplo: 140 litros por persona por día. Se quiere un estanque que guarde la demanda de 2 días. "
     "Estanque E1: base de 3 m por 2 m y altura útil de 2 m. Estanque E2: base de 3 m por 3 m y altura útil de 2 m. 1 m³ equivale a 1.000 litros.")
build(
    O6, 3, F,
    use="Aprenderé a calcular la demanda de agua de un edificio, a convertir el volumen de un estanque a litros y a decidir cuál alcanza para una reserva de días.",
    prior=["Sé calcular el consumo diario.", "Sé el volumen de un bloque rectangular.", "Sé convertir m³ a litros."],
    explain=[
        "La demanda diaria de un edificio es la dotación multiplicada por el número total de personas. Para cuidar la continuidad del servicio se calcula una reserva: la demanda de varios días, que se guarda en un estanque. Si el edificio usa 5.000 litros por día y se quiere una reserva de 3 días, el estanque debe guardar 15.000 litros.",
        "El volumen de un estanque rectangular es largo por ancho por altura útil, en m³, y se pasa a litros multiplicando por 1.000. La altura útil es la altura que realmente se llena de agua. Para saber si alcanza se compara la capacidad con la reserva necesaria; la autonomía es la cantidad de días completos que el estanque cubre, y se obtiene dividiendo la capacidad entre la demanda diaria.",
        f"Los valores reales de dotación y de reserva los fija el proyecto con la norma vigente; aquí son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("demanda diaria", "dotación multiplicada por el total de personas"), ("reserva", "agua guardada para cubrir la demanda de varios días"), ("altura útil", "altura que realmente se llena de agua en el estanque"), ("capacidad", "volumen de agua que cabe en un estanque"), ("autonomía", "días completos que un estanque cubre la demanda")],
    worked=[
        ("Reserva necesaria", "Un edificio de ejemplo usa 5.000 litros por día y se quiere una reserva de 2 días. ¿Cuántos litros debe guardar el estanque?", ["Se multiplica la demanda diaria por los días de reserva.", "5.000 por 2 son 10.000."], "10.000 litros"),
        ("Autonomía", "Un estanque de ejemplo de 20.000 litros abastece un edificio que usa 6.000 litros por día. ¿Cuántos días completos cubre?", ["Se divide la capacidad entre la demanda diaria.", "20.000 entre 6.000 da 3 días completos."], "3 días completos"),
    ],
    mistakes=[("Olvidar convertir de m³ a litros antes de comparar.", "Comparar m³ con litros da un resultado absurdo.", "Multiplica los m³ por 1.000."),
              ("Usar la altura total del estanque en vez de la altura útil.", "No toda la altura se llena de agua.", "Usa la altura útil.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es la reserva de agua de un edificio?", "El agua guardada para cubrir la demanda de varios días", "El agua que se pierde por fugas", "El agua que sale por el desagüe", "La reserva asegura el servicio ante una interrupción."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es la altura útil de un estanque?", "La altura que realmente se llena de agua", "La altura total de las paredes", "La altura del edificio", "El volumen se calcula con la altura útil, no con la total."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es la autonomía de un estanque?", "Los días completos que cubre la demanda", "Su peso cuando está lleno", "Su precio en pesos", "La autonomía relaciona la capacidad con la demanda diaria."),
        ("=", "{F} ¿Cuántas personas viven en el edificio?", "12*4", "Se multiplican los departamentos por las personas de cada uno.", " personas"),
        ("=", "{F} ¿Cuántos litros usa el edificio por día?", "12*4*140", "Se multiplican las personas por la dotación.", " litros"),
        ("=", "{F} ¿Cuántos litros debe guardar el estanque para la reserva de 2 días?", "12*4*140*2", "Se multiplica la demanda diaria por los 2 días de reserva.", " litros"),
        ("=", "{F} ¿Cuántos metros cúbicos tiene el estanque E1?", "3*2*2", "El volumen es largo por ancho por altura útil.", " m³"),
        ("=", "{F} ¿Cuántos litros caben en el estanque E1?", "3*2*2*1000", "Se multiplican los m³ por 1.000.", " litros"),
        ("=", "{F} ¿Cuántos litros caben en el estanque E2?", "3*3*2*1000", "Se multiplican los m³ por 1.000.", " litros"),
        ("abc", "{F} ¿Qué estanque alcanza para la reserva de 2 días?", "Solo el E2, porque guarda 18.000 litros y se necesitan 13.440", "Solo el E1", "Ambos", "E1 guarda 12.000 litros, menos de los 13.440 necesarios."),
        ("=", "{F} ¿Cuántos días completos de autonomía da el estanque E2?", "18000//6720", "Se divide la capacidad entre la demanda diaria y se toman días completos.", " días"),
        ("=", "{F} ¿Cuántos litros sobran en el estanque E2 después de cubrir la reserva de 2 días?", "18000-13440", "Se resta la reserva necesaria a la capacidad.", " litros"),
        ("abc", "{F} Un compañero propone elegir E1 «porque es más barato». ¿Qué respuesta es correcta?", "No: E1 no cubre la reserva exigida; antes del costo debe cumplirse la reserva", "Sí: el costo es lo único que importa", "Sí, si se llena dos veces al día", "Una alternativa que no cumple la reserva no se considera."),
    ],
    ctx=("abc", "La administradora de un edificio de ejemplo pregunta si puede ampliar la cantidad de departamentos sin revisar el estanque. ¿Qué respondes?", "Que primero se recalcula la demanda y la reserva, y que cualquier cambio lo decide el proyectista", "Que sí, porque el estanque siempre alcanza", "Que sí, mientras el agua se vea limpia", "Más personas aumentan la demanda y pueden dejar la reserva corta."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se calcula la demanda diaria?", "Dotación por total de personas", "La demanda diaria multiplica la dotación por las personas."),
        ("¿Cómo se pasa un volumen de m³ a litros?", "Multiplicando por 1.000", "Cada metro cúbico equivale a 1.000 litros."),
        ("¿Cómo se obtiene la autonomía?", "Dividiendo la capacidad entre la demanda diaria", "Se cuentan los días completos que alcanza."),
    ],
    op=("Ficha de ejemplo: edificio de 10 departamentos con 3 personas cada uno; dotación de ejemplo de 120 litros por persona por día; reserva de 2 días. Estanque K1: base de 2 m por 3 m y altura útil de 2 m. Estanque K2: base de 3 m por 3 m y altura útil de 2 m. Escribe (a) la demanda diaria, (b) la reserva necesaria, (c) la capacidad en litros de cada estanque, (d) cuáles estanques alcanzan y cuántos litros sobran en cada uno.",
        "(a) 10 × 3 × 120 = 3.600 litros por día. (b) 3.600 × 2 = 7.200 litros. (c) K1: 2 × 3 × 2 × 1.000 = 12.000 litros. K2: 3 × 3 × 2 × 1.000 = 18.000 litros. (d) Ambos alcanzan; sobran 4.800 litros en K1 y 10.800 litros en K2.",
        ["calcula la demanda diaria", "calcula la reserva", "calcula las capacidades", "compara y calcula los sobrantes"],
        ["hoja con la planilla de cálculo y la conclusión"],
        ["olvidar convertir a litros", "usar una altura que no es la útil", "no calcular los sobrantes"],
        "Pregunta: «¿cuántos días completos de autonomía da cada estanque?». Si no responde, pídele que divida la capacidad entre la demanda diaria."),
    reinforce="Calcula en papel la capacidad en litros de un estanque de 2 m por 2 m de base y 1 m de altura útil.",
    extend="Explica con un ejemplo por qué conviene tener una reserva de agua en un edificio.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (plan de riego de ejemplo, inventado). Caudal disponible de la fuente: 50 L/min. Sectores del huerto y caudales: A, 25 L/min; B, 15 L/min; C, 30 L/min; D, 10 L/min. "
     "Cada sector riega 40 minutos por turno. Regla de planilla: en un mismo turno los sectores no pueden pedir más caudal que el disponible. Plan propuesto: turno 1 con A, B y D; turno 2 con C.")
build(
    O6, 4, F,
    use="Aprenderé a organizar turnos de riego con una regla de caudal, a calcular el volumen y el tiempo total y a decidir si un plan cumple.",
    prior=["Sé sumar caudales.", "Sé multiplicar caudal por tiempo.", "Sé qué es un sector de riego."],
    explain=[
        "Un plan de riego reparte los sectores en turnos. En cada turno, la suma de los caudales de los sectores que riegan a la vez no puede superar el caudal disponible. Si lo supera, los sectores no reciben el agua prevista. Después se calcula el volumen de cada sector (caudal por minutos) y el tiempo total, que es el número de turnos por la duración de cada turno.",
        "Un plan cumple solo si todos sus turnos cumplen. Si un turno no cumple, se rediseña el reparto, por ejemplo moviendo un sector a otro turno. Los cambios de diseño los decide el proyectista y se anotan en el registro. El uso eficiente del agua también importa: un riego innecesariamente largo desperdicia agua.",
        f"El plan de esta ficha es de ejemplo y no es una receta de riego. {EMER} {AVISO}",
    ],
    vocab=[("turno", "grupo de sectores que riegan a la vez"), ("volumen de riego", "caudal multiplicado por los minutos de riego"), ("tiempo total", "número de turnos por la duración de cada turno"), ("plan de riego", "reparto de los sectores en turnos"), ("uso eficiente", "uso del agua sin desperdicio")],
    worked=[
        ("Cumplir un turno", "Con un caudal disponible de 40 L/min, dos sectores de ejemplo piden 18 y 20 L/min. ¿Pueden regar juntos?", ["Se suman: 18 más 20 son 38 L/min.", "38 no supera 40: pueden."], "Sí, pueden regar juntos"),
        ("Tiempo total", "Un plan de ejemplo tiene 3 turnos de 25 minutos cada uno. ¿Cuánto dura el riego completo?", ["Se multiplican los turnos por la duración.", "3 por 25 son 75 minutos."], "75 minutos"),
    ],
    mistakes=[("Aprobar un plan porque «casi» cumple el caudal.", "Un turno que supera el caudal disponible no cumple la regla.", "Revisa que cada turno esté dentro del límite."),
              ("Calcular el tiempo total sumando solo los minutos de un turno.", "El tiempo total incluye todos los turnos.", "Multiplica los turnos por la duración de cada uno.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es un turno de riego?", "Un grupo de sectores que riegan a la vez", "Un sector que nunca se riega", "Una tubería de evacuación", "El turno agrupa los sectores que riegan juntos."),
        ("abc", "En Instalaciones Sanitarias: ¿cómo se obtiene el volumen de riego de un sector?", "Caudal por minutos de riego", "Caudal más minutos", "Minutos divididos en el caudal", "El caudal por el tiempo da el volumen."),
        ("abc", "En Instalaciones Sanitarias: ¿cuándo cumple un plan de riego?", "Cuando todos sus turnos están dentro del caudal disponible", "Cuando tiene un solo turno", "Cuando riega siempre de noche", "Un plan cumple solo si cada turno respeta el límite de caudal."),
        ("=", "{F} ¿Cuántos L/min piden juntos los sectores A, B y D en el turno 1?", "25+15+10", "Se suman los caudales de los tres sectores.", " L/min"),
        ("abc", "{F} ¿Cumple el turno 1 la regla de planilla?", "Sí, porque pide 50 L/min y hay 50 L/min disponibles", "No, porque pide más de 50 L/min", "No se puede saber", "50 no supera 50, por lo tanto el turno cumple."),
        ("abc", "{F} ¿Cumple el turno 2, con solo el sector C?", "Sí, porque pide 30 L/min y hay 50 L/min disponibles", "No, porque un turno necesita dos sectores", "No, porque 30 es mayor que 25", "30 L/min es menos que los 50 L/min disponibles."),
        ("=", "{F} ¿Cuántos litros entrega el sector A en su turno?", "25*40", "Se multiplica el caudal por los minutos de riego.", " litros"),
        ("=", "{F} ¿Cuántos litros entrega el sector C en su turno?", "30*40", "Se multiplica el caudal por los minutos de riego.", " litros"),
        ("=", "{F} ¿Cuántos litros entregan en total los cuatro sectores en un ciclo completo?", "(25+15+30+10)*40", "Se suman los caudales y se multiplica por 40 minutos.", " litros"),
        ("=", "{F} ¿Cuántos minutos dura el ciclo completo de riego con los dos turnos?", "2*40", "Se multiplican los turnos por la duración de cada uno.", " minutos"),
        ("abc", "{F} Alguien propone poner A y C juntos en un turno para ahorrar tiempo. ¿Qué respuesta es correcta?", "No: pedirían 55 L/min, más que los 50 disponibles", "Sí: 55 L/min es casi 50", "Sí, si se riega menos tiempo", "El turno superaría el caudal disponible y no cumpliría la regla."),
        ("abc", "{F} Otro propone C y B en un mismo turno. ¿Cumple?", "Sí, porque piden 45 L/min, menos que los 50 disponibles", "No, porque C es el sector más grande", "No, porque dos sectores nunca pueden regar juntos", "30 más 15 son 45 L/min, dentro del caudal disponible."),
        ("abc", "¿Cuál es el mejor registro del plan de riego?", "Turnos, caudal de cada uno, volúmenes por sector, tiempo total y quién aprobó", "Se riega por la tarde", "El huerto queda bien regado", "Un buen registro permite revisar y repetir el plan."),
    ],
    ctx=("abc", "El dueño del huerto de ejemplo quiere regar los cuatro sectores a la vez «para terminar rápido». ¿Qué propones?", "Explicar que los cuatro piden 80 L/min y la fuente da 50, por lo que se necesitan turnos", "Aceptar, porque el dueño decide", "Abrir más la bomba para que alcance", "La fuente entrega un caudal limitado; el reparto en turnos lo respeta."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué se compara con el caudal disponible en un turno?", "La suma de los caudales de los sectores del turno", "No pueden pedir más de lo disponible."),
        ("¿Cómo se calcula el tiempo total del riego?", "Turnos por duración de cada turno", "El tiempo se acumula turno tras turno."),
        ("¿Quién decide los cambios de diseño de un plan de riego?", "El proyectista", "Los cambios se anotan en el registro."),
    ],
    op=("Ficha de ejemplo: caudal disponible de 60 L/min; sectores P, 30 L/min; Q, 20 L/min; R, 25 L/min; S, 10 L/min; cada sector riega 30 minutos por turno. Plan: turno 1 con P y R; turno 2 con Q y S. Escribe (a) el caudal que pide cada turno y si cumple, (b) los litros que entrega el sector R, (c) el tiempo total, (d) qué harías si el turno 1 no cumpliera.",
        "(a) Turno 1: 30 + 25 = 55 L/min, cumple. Turno 2: 20 + 10 = 30 L/min, cumple. (b) 25 × 30 = 750 litros. (c) 2 × 30 = 60 minutos. (d) Avisar al proyectista para rediseñar el reparto de los sectores y anotar el cambio.",
        ["calcula el caudal de cada turno y compara", "calcula los litros del sector", "calcula el tiempo total", "propone avisar al proyectista"],
        ["hoja con los cálculos y la conclusión"],
        ["no sumar todos los sectores del turno", "calcular mal los litros", "cambiar el caudal disponible"],
        "Pregunta: «¿qué pasaría si P y Q regaran juntos?». Si no responde, pídele que sume sus caudales."),
    reinforce="Arma en papel un plan de riego con tres sectores de 10, 20 y 30 L/min y un caudal disponible de 40 L/min, con los turnos que necesites.",
    extend="Explica con un ejemplo por qué un riego más largo de lo necesario desperdicia agua.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (alternativas y control de calidad de ejemplo, inventados). Huerto de 200 m². Riego por aspersión: usa 4 litros por m² por día; costo de instalación $150.000. "
     "Riego por goteo: usa 3 litros por m² por día; costo de instalación $240.000. Precio del agua de ejemplo: $1.000 por m³; 1 m³ equivale a 1.000 litros; mes de 30 días. "
     "Lista de control documental de entrega (10 puntos): cumplen 8; faltan el registro de una prueba hecha por personal autorizado y la firma de recepción.")
build(
    O6, 5, F,
    use="Aprenderé a comparar dos sistemas de riego por consumo de agua y costo, a calcular en cuántos meses se recupera una inversión y a verificar la documentación de entrega.",
    prior=["Sé calcular consumos diarios y mensuales.", "Sé convertir litros a m³.", "Sé calcular un porcentaje."],
    explain=[
        "Comparar sistemas de riego implica calcular cuánta agua usan y cuánto cuestan. El consumo diario es los litros por m² multiplicados por los m² del huerto. El consumo mensual se obtiene multiplicando por 30 días y el costo mensual, pasando los litros a m³ y multiplicando por el precio del agua. Un sistema más caro de instalar puede ahorrar agua. El tiempo de recuperación es la cantidad de meses que tarda el ahorro mensual en igualar la diferencia de costo de instalación.",
        "La calidad de la entrega se verifica con una lista de control documental: se revisan los planos finales, los registros de las pruebas hechas por personal autorizado, los certificados de los materiales y la firma de recepción. Un punto que falta se completa antes de recibir la obra. La seguridad y la separación entre el agua de riego y el agua potable no se negocian por ahorrar costos.",
        f"Los consumos y los precios de esta ficha son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("aspersión", "riego que reparte el agua como lluvia"), ("goteo", "riego que entrega el agua gota a gota cerca de la planta"), ("tiempo de recuperación", "meses que tarda el ahorro mensual en igualar la diferencia de costo de instalación"), ("ahorro mensual", "diferencia entre el costo mensual de dos alternativas"), ("registro de prueba", "documento donde personal autorizado deja constancia de una prueba y su resultado")],
    worked=[
        ("Consumo diario", "Un jardín de ejemplo de 50 m² usa 2 litros por m² por día. ¿Cuántos litros usa por día?", ["Se multiplican los m² por los litros por m².", "50 por 2 son 100."], "100 litros por día"),
        ("Recuperación", "Un sistema de ejemplo cuesta $60.000 más y ahorra $5.000 al mes. ¿En cuántos meses recupera la diferencia?", ["Se divide la diferencia entre el ahorro mensual.", "60.000 entre 5.000 son 12."], "12 meses"),
    ],
    mistakes=[("Elegir el sistema más barato de instalar sin calcular el consumo de agua.", "Un sistema barato puede gastar más agua y salir más caro con el tiempo.", "Compara también el costo de uso."),
              ("Marcar «cumple» en un registro de prueba que no existe.", "Sin el documento no hay evidencia.", "Marca «cumple» solo con respaldo escrito.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es el riego por goteo?", "El que entrega el agua gota a gota cerca de la planta", "El que reparte el agua como lluvia", "El que usa solo agua potable", "El goteo aplica el agua directamente cerca de la planta."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es el tiempo de recuperación de una inversión?", "Los meses que tarda el ahorro en igualar la diferencia de costo de instalación", "Los meses que dura la garantía", "Los días de una obra", "El tiempo de recuperación compara la inversión extra con el ahorro."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es un registro de prueba?", "El documento donde personal autorizado deja constancia de una prueba y su resultado", "Un plano del sistema de riego", "La lista de precios del agua", "El registro respalda por escrito que una prueba se hizo y qué resultó."),
        ("=", "{F} ¿Cuántos litros usa por día el riego por aspersión?", "200*4", "Se multiplican los m² por los litros por m².", " litros"),
        ("=", "{F} ¿Cuántos litros usa por día el riego por goteo?", "200*3", "Se multiplican los m² por los litros por m².", " litros"),
        ("=", "{F} ¿Cuántos m³ usa el riego por aspersión en un mes?", "200*4*30//1000", "Se multiplica el consumo diario por 30 y se pasa a m³.", " m³"),
        ("=", "{F} ¿Cuántos m³ usa el riego por goteo en un mes?", "200*3*30//1000", "Se multiplica el consumo diario por 30 y se pasa a m³.", " m³"),
        ("=", "{F} ¿Cuánto ahorra por mes el goteo frente a la aspersión?", "(200*4*30//1000-200*3*30//1000)*1000", "Se resta el consumo en m³ y se multiplica por el precio de cada m³.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta instalar el goteo?", "240000-150000", "Se resta el costo de la aspersión al del goteo.", " pesos"),
        ("=", "{F} ¿En cuántos meses el ahorro mensual iguala la diferencia de costo de instalación?", "(240000-150000)//6000", "Se divide la diferencia de instalación entre el ahorro mensual de 6.000 pesos.", " meses"),
        ("abc", "{F} Si el huerto se usará muchos años, ¿qué alternativa conviene por costo y agua?", "El goteo, porque recupera su costo extra y ahorra agua", "La aspersión, porque su instalación cuesta menos", "Ninguna", "Tras recuperar la inversión, el goteo ahorra agua y dinero."),
        ("=", "{F} ¿Qué porcentaje de los puntos de la lista de control cumple?", "8*100//10", "Se divide lo que cumple entre el total y se pasa a porcentaje.", " %"),
        ("abc", "{F} Faltan el registro de una prueba y la firma de recepción. ¿Qué corresponde?", "Completarlos antes de recibir la obra", "Recibir igual, porque cumple el 80 %", "Firmar la recepción y buscar el registro después", "Sin evidencia ni responsable la recepción no es confiable."),
    ],
    ctx=("abc", "El dueño de un huerto de ejemplo te pide que le digas «cuál sistema instalar» y que lo instales tú. ¿Qué respondes?", "Que puedes mostrar la comparación en papel, pero que la instalación y las pruebas las hace personal autorizado", "Que instalas el más barato mañana mismo", "Que lo instale él con un manual", "Instalar y probar redes exige personal autorizado; este cuaderno no habilita para hacerlo."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se calcula el consumo diario del riego?", "Litros por m² por la cantidad de m²", "Se multiplica el uso por la superficie."),
        ("¿Cómo se calcula el tiempo de recuperación?", "Diferencia de instalación dividida en el ahorro mensual", "Compara la inversión extra con lo que se ahorra cada mes."),
        ("¿Qué se hace con un punto de la lista sin evidencia?", "Se completa antes de recibir la obra", "Sin respaldo escrito no se marca como cumplido."),
    ],
    op=("Ficha de ejemplo: huerto de 100 m²; aspersión usa 4 litros por m² por día e instalación de $100.000; goteo usa 2 litros por m² por día e instalación de $160.000; precio del agua de $1.000 por m³; mes de 30 días. Escribe (a) el consumo mensual en m³ de cada sistema, (b) el ahorro mensual en pesos del goteo, (c) en cuántos meses se recupera la diferencia de instalación, (d) quién instala y prueba el sistema.",
        "(a) Aspersión: 100 × 4 × 30 ÷ 1.000 = 12 m³. Goteo: 100 × 2 × 30 ÷ 1.000 = 6 m³. (b) (12 − 6) × 1.000 = 6.000 pesos. (c) (160.000 − 100.000) ÷ 6.000 = 10 meses. (d) Personal autorizado.",
        ["calcula los consumos mensuales", "calcula el ahorro", "calcula el tiempo de recuperación", "indica quién instala y prueba"],
        ["hoja con la comparación completa"],
        ["no pasar los litros a m³", "dividir al revés", "decir que el estudiante instala"],
        "Pregunta: «¿qué pasa después de recuperar la inversión?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula en papel el consumo mensual en m³ de un jardín de 50 m² que usa 3 litros por m² por día.",
    extend="Explica con un ejemplo por qué ahorrar agua importa tanto en la instalación como en el uso.",
)
