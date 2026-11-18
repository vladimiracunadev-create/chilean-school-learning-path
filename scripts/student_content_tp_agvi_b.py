"""Agropecuaria TP 4.º medio, mención Vitivinícola: OAM-04 (envasado, etiquetado y sellado), OAM-05 (bodegaje del vino envasado) y OAM-06 (verificación de maquinaria, equipos, instrumentos y utensilios). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_agvi_common import AVISO, EMER, build

O4 = "TP-AGVI-4-OAM-04"
O5 = "TP-AGVI-4-OAM-05"
O6 = "TP-AGVI-4-OAM-06"

# ============================================================ OAM-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La línea de envasado de la «Bodega Demo» llena botellas de vidrio de 750 mL, las sella con una tapa, les pega una etiqueta y las ordena en cajas de 12 botellas. "
     "Peligros anotados: botellas que se rompen y cortan, partes móviles de la llenadora y de la cinta transportadora, ruido, piso mojado, cajas pesadas que se levantan a mano, productos de limpieza y personal que trabaja muchas horas seguidas.")
build(
    O4, 1, F,
    use="Aprenderé qué son el envasado, el etiquetado y el sellado del vino, por qué las normas de higiene y calidad son importantes y cuáles son los peligros de una línea de envasado.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Envasar es poner el vino en envases, como botellas de vidrio, para conservarlo y venderlo. El sellado es cerrar la botella con una tapa o un corcho para que no entre aire ni salga líquido. El etiquetado es pegar una etiqueta con los datos del producto que exige la norma vigente: qué es, cuánto contiene, su lote y su origen. Todo se hace según las normas de higiene y calidad, es decir, con equipos limpios, personal que cumple reglas de higiene y registros de cada lote.",
        "La línea de envasado tiene peligros. El vidrio roto corta; las partes móviles atrapan; el ruido daña el oído; el piso mojado resbala; las cajas pesadas dañan la espalda; y los productos de limpieza irritan. La jerarquía de controles ordena las medidas: eliminar, sustituir, cambiar el lugar o el equipo, reglas y capacitación y, al final, el equipo de protección personal (EPP).",
        f"Una protección fija sobre las partes móviles es un control de ingeniería; una regla de pausas y rotación de tareas es administrativa. La línea la opera personal capacitado y autorizado; este cuaderno no habilita para hacerlo. {EMER} {AVISO}",
    ],
    vocab=[("envasado", "colocar el vino en envases para conservarlo y venderlo"), ("sellado", "cierre de la botella con una tapa o un corcho"), ("etiquetado", "colocación de la etiqueta con los datos que exige la norma vigente"), ("lote de envasado", "grupo de botellas envasadas juntas con las mismas condiciones"), ("normas de higiene", "reglas de limpieza que evitan la contaminación del producto"), ("cinta transportadora", "equipo que mueve las botellas por la línea"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Distinguir sellado y etiquetado", "En una línea de ejemplo se coloca el corcho en la botella. ¿Es sellado o etiquetado?", ["El corcho cierra la botella.", "Es sellado."], "Sellado"),
        ("Clasificar un control", "Una línea de ejemplo instala un botón de parada de emergencia al alcance de quien trabaja junto a la cinta. ¿Qué tipo de control es?", ["El botón actúa sin depender de que alguien recuerde una regla.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que recoger vidrio roto con las manos es seguro si se hace con cuidado.", "El vidrio corta aunque haya cuidado.", "Se avisa y lo retira personal con equipo adecuado."),
              ("Creer que leer sobre la línea habilita para operarla.", "Operar la línea exige formación y autorización.", "Aprende aquí el concepto y deja la operación a personal capacitado.")],
    T=[
        ("abc", "En el envasado del vino: ¿qué es el sellado?", "El cierre de la botella con una tapa o un corcho", "La colocación de la etiqueta", "El llenado de la botella", "El sellado cierra la botella; el etiquetado pone la etiqueta."),
        ("abc", "En el envasado del vino: ¿qué es el etiquetado?", "La colocación de la etiqueta con los datos exigidos por la norma", "El cierre de la botella", "El lavado de la botella", "El etiquetado pone la etiqueta con los datos exigidos."),
        ("abc", "En el envasado del vino: ¿qué es un lote de envasado?", "Un grupo de botellas envasadas juntas con las mismas condiciones", "Una botella rota", "Un camión con cajas", "El lote agrupa botellas con las mismas condiciones."),
        ("=", "{F} Una caja lleva 12 botellas de 750 mL. ¿Cuántas botellas hay en 25 cajas?", "12*25", "Se multiplican las botellas de cada caja por las cajas.", " botellas"),
        ("abc", "{F} Una cubierta fija sobre la cadena de la cinta transportadora es un control de tipo:", "De ingeniería, porque cambia físicamente el equipo", "Administrativo, porque es una regla", "De EPP, porque protege a quien trabaja", "La cubierta es una parte del equipo y funciona siempre."),
        ("abc", "{F} Una regla que dice «rotación de tareas cada 2 horas en las cajas pesadas» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el equipo", "De sustitución, porque cambia la caja", "Una regla de rotación es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al vidrio roto en el piso de la línea?", "Que una persona se corte o resbale", "El vidrio mismo", "Que falten botellas", "El riesgo es la posibilidad de daño; el vidrio roto es el peligro."),
        ("abc", "{F} Una estudiante dice: «ya aprendí cómo funciona la llenadora, así que la opero yo». ¿Qué respuesta es correcta?", "Es peligroso: la línea la opera personal capacitado y autorizado", "Es correcto, si usa guantes", "Es correcto, si va despacio", "Los guantes o la lentitud no reemplazan la formación."),
        ("abc", "{F} Durante una visita, una persona se corta con vidrio y sangra mucho. ¿Qué corresponde según las reglas generales?", "No tocar el vidrio ni la herida, avisar a un adulto responsable y a emergencias", "Sacar los vidrios con las manos", "Esperar a que deje de sangrar", "Se avisa a quienes pueden prestar ayuda."),
        ("abc", "En el envasado del vino: ¿por qué los equipos de la línea deben estar limpios?", "Porque evitan contaminar el vino", "Porque así hacen menos ruido", "Porque pesan menos", "Las normas de higiene protegen la calidad del producto."),
        ("abc", "{F} Se propone solo entregar guantes por el peligro del vidrio. ¿Qué medida es más efectiva?", "Retirar el vidrio roto con equipos y mantener la línea ordenada", "Entregar guantes más gruesos", "Pedir mayor cuidado", "Actuar sobre el origen del peligro está más arriba que el EPP."),
        ("=", "{F} Una línea de ejemplo llena 1.200 botellas por hora. ¿Cuántas botellas llena en 6 horas?", "1200*6", "Se multiplican las botellas por hora por las horas de trabajo.", " botellas"),
        ("abc", "En el envasado del vino: ¿por qué la etiqueta debe tener el lote?", "Porque permite seguir el origen de cada botella", "Porque aumenta el volumen", "Porque reemplaza al corcho", "El lote da trazabilidad a cada botella envasada."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por operar su línea de envasado «porque ya viste cómo funciona». ¿Qué respondes?", "Que no, porque exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, a poca velocidad", "Que sí, con guantes", "Haber visto el concepto no habilita para operar maquinaria."),
    sc=[
        ("En el envasado del vino: ¿qué es envasar?", "Poner el vino en envases para conservarlo y venderlo", "El envasado prepara el vino para su venta."),
        ("En la línea de envasado: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En el envasado del vino: ¿qué dato permite seguir el origen de una botella?", "El lote", "El lote da trazabilidad a cada botella envasada."),
    ],
    op=("La «Bodega Demo 2» anota una tarea de ejemplo: limpiar el vidrio roto de la línea con las manos mientras la cinta está en marcha y el piso está mojado. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a alguien con un corte grande.",
        "(a) Peligro: vidrio roto junto a una cinta en marcha; riesgo: que la persona se corte o quede atrapada. (b) Una regla de detener la línea y avisar antes de limpiar. (c) Un sistema de parada de emergencia y una cubierta fija sobre la cinta. (d) No toco la herida ni los vidrios, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "avisa a un adulto responsable"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer recoger el vidrio con las manos", "no avisar"],
        "Pregunta: «¿qué control detiene la línea aunque alguien se olvide de la regla?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres peligros de una línea de envasado y el riesgo de cada uno.",
    extend="Explica con un ejemplo por qué el etiquetado con lote ayuda a retirar botellas con problemas.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 2 (etiqueta y registros de ejemplo, inventados). Etiqueta de ejemplo del «Vino Demo»: contenido 750 mL; grado alcohólico 13 % (dato de ejemplo); lote L-45; origen «valle de ejemplo». Estanque de 9.000 litros listo para envasar. "
     "Control de llenado de cuatro botellas del lote: 750, 752, 748 y 750 mL. Tolerancia de ejemplo: 5 mL de diferencia con los 750 mL. Documentos: la orden de envasado, el registro de control de llenado, el registro de lote y la hoja de limpieza de la línea. Roles: jefe de envasado, operador de línea, controlador de calidad y bodeguero.")
build(
    O4, 2, F,
    use="Aprenderé qué datos lleva una etiqueta, cómo se controla el llenado de las botellas y cuáles son los documentos y roles de una línea de envasado.",
    prior=["Sé qué son el envasado, el sellado y el etiquetado.", "Sé calcular promedios y diferencias.", "Sé dividir enteros."],
    explain=[
        "La etiqueta de una botella debe tener los datos que exige la norma vigente, entre ellos qué producto es, su contenido, su grado alcohólico, el lote y el origen. El control de llenado comprueba que cada botella tenga la cantidad indicada en la etiqueta: se mide el contenido de una muestra y se compara con el valor nominal (el escrito en la etiqueta) y con una tolerancia, que es la diferencia máxima aceptable.",
        "Los documentos de la línea dan evidencia: la orden de envasado dice qué se envasa y cuánto; el registro de control de llenado anota las mediciones; el registro de lote identifica las botellas; la hoja de limpieza dice cuándo se limpió la línea y quién lo hizo. El jefe de envasado organiza, el operador ejecuta con capacitación, el controlador de calidad mide y el bodeguero recibe las cajas. Nadie anota una medición que no hizo.",
        f"Una botella fuera de tolerancia se aparta y se informa; no se corrige el registro. {EMER} {AVISO}",
    ],
    vocab=[("valor nominal", "cantidad escrita en la etiqueta"), ("tolerancia", "diferencia máxima aceptable respecto del valor nominal"), ("control de llenado", "medición del contenido de una muestra de botellas"), ("orden de envasado", "documento que dice qué se envasa y cuánto"), ("hoja de limpieza", "documento que dice cuándo se limpió la línea y quién lo hizo"), ("grado alcohólico", "porcentaje de alcohol del vino, escrito en la etiqueta")],
    worked=[
        ("Botellas por estanque", "Un estanque de ejemplo tiene 1.500 litros y cada botella contiene 750 mL. ¿Cuántas botellas se llenan? (1 litro son 1.000 mL)", ["1.500 litros son 1.500.000 mL.", "1.500.000 dividido entre 750 es 2.000."], "2.000 botellas"),
        ("Comparar con la tolerancia", "Una botella de ejemplo tiene 744 mL y la tolerancia es 5 mL sobre 750. ¿Cumple?", ["La diferencia es 750 menos 744, o sea 6.", "6 es mayor que 5."], "No cumple"),
    ],
    mistakes=[("Anotar el valor nominal en el registro en vez del medido.", "El registro debe mostrar lo realmente medido.", "Se anota la medición real."),
              ("Creer que la etiqueta puede llevar cualquier dato.", "La norma vigente exige ciertos datos.", "Se respetan los datos obligatorios.")],
    T=[
        ("abc", "En el envasado del vino: ¿qué es el valor nominal de una botella?", "La cantidad escrita en la etiqueta", "La cantidad que se midió", "La diferencia máxima aceptable", "El valor nominal es el de la etiqueta."),
        ("abc", "En el envasado del vino: ¿qué es la tolerancia de llenado?", "La diferencia máxima aceptable respecto del valor nominal", "El precio de la botella", "El número de botellas por caja", "La tolerancia limita la diferencia aceptable."),
        ("abc", "En el envasado del vino: ¿para qué sirve la hoja de limpieza de la línea?", "Para anotar cuándo se limpió y quién lo hizo", "Para fijar el precio del vino", "Para medir el contenido", "La hoja de limpieza deja evidencia de la higiene."),
        ("=", "{F} ¿Cuántas botellas de 750 mL se llenan con el estanque de 9.000 litros? (1 litro son 1.000 mL)", "9000*1000//750", "Se pasan los litros a mL y se divide entre el contenido de cada botella.", " botellas"),
        ("=", "{F} ¿Cuántas cajas de 12 botellas se arman con ese estanque?", "9000*1000//750//12", "Se dividen las botellas totales entre las botellas de cada caja.", " cajas"),
        ("=", "{F} ¿Cuál es el promedio de las cuatro botellas controladas?", "(750+752+748+750)//4", "Se suman las cuatro mediciones y se divide entre 4.", " mL"),
        ("abc", "{F} ¿Cumple la botella de 752 mL la tolerancia de ejemplo?", "Sí, porque la diferencia es 2 mL, menor que 5 mL", "No, porque es mayor que 750", "No se puede saber", "Una diferencia de 2 mL está dentro de la tolerancia."),
        ("abc", "{F} ¿Qué documento dice qué se envasa y cuánto?", "La orden de envasado", "La hoja de limpieza", "El registro de lote", "La orden de envasado indica el trabajo."),
        ("abc", "{F} ¿Qué rol mide el contenido de las botellas de la muestra?", "El controlador de calidad", "El bodeguero", "El comprador", "El controlador de calidad mide el contenido de la muestra."),
        ("abc", "{F} Un operador dice: «si una botella tiene 744 mL, la anoto como 750 para que cumpla». ¿Qué respuesta es correcta?", "Es incorrecto: se anota la medición real, se aparta la botella e informa", "Es correcto, porque cumple", "Es correcto, si es solo una", "Alterar una medición falsea el registro."),
        ("abc", "{F} El jefe de envasado quiere anotar que la línea se limpió, aunque no se limpió, «para el control». ¿Qué corresponde?", "Rechazarlo: no se anota lo que no se hizo", "Aceptarlo, si se limpia mañana", "Aceptarlo, para cumplir", "Anotar una limpieza que no ocurrió falsea el registro."),
        ("abc", "{F} Una botella se rompe y el vidrio salta cerca de una persona que está sin protección. ¿Qué corresponde a quien lo ve?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Recoger el vidrio con las manos", "Acercarse a limpiar", "El vidrio corta; se avisa a quienes tienen el equipo."),
        ("abc", "En el envasado del vino: ¿por qué se controla el llenado con varias botellas?", "Porque una sola botella no representa a todo el lote", "Porque cuesta menos", "Porque cada botella tiene otra tolerancia", "Varias mediciones describen mejor el lote."),
    ],
    ctx=("abc", "Un conocido te pide que firmes el control de llenado de un lote que no mediste. ¿Qué respondes?", "Que no, porque firmar sin medir lo falsea, y que lo consultarás con un adulto responsable", "Que sí, si confías", "Que sí, solo una vez", "Una firma certifica una medición que debe haberse hecho."),
    sc=[
        ("En el envasado del vino: ¿cómo se calcula el promedio de cuatro mediciones?", "Se suman y se dividen entre 4", "El promedio resume las mediciones en un solo número."),
        ("En el envasado del vino: ¿qué se hace con una botella fuera de tolerancia?", "Se aparta y se informa", "No se corrige el registro para que parezca bueno."),
        ("En el envasado del vino: ¿qué rol organiza la línea de envasado?", "El jefe de envasado", "El jefe de envasado organiza el trabajo de la línea."),
    ],
    op=("Control de ejemplo de la «Bodega Demo 3»: estanque de 4.500 litros; botellas de 750 mL; cajas de 12; mediciones de 749, 751, 750 y 746 mL con tolerancia de 5 mL. Escribe (a) cuántas botellas se llenan, (b) cuántas cajas se arman, (c) qué mediciones cumplen la tolerancia, (d) qué haces con una medición que no cumple.",
        "(a) 4.500 × 1.000 ÷ 750 = 6.000 botellas. (b) 6.000 ÷ 12 = 500 cajas. (c) Las cuatro cumplen, porque la mayor diferencia es 4 mL. (d) Se aparta la botella, se anota el valor real y se informa.",
        ["calcula las botellas", "calcula las cajas completas", "compara con la tolerancia", "no altera el registro"],
        ["hoja con las cuatro respuestas"],
        ["no pasar a mL", "alterar una medición"],
        "Pregunta: «¿cuántos mL hay en 4.500 litros?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula las botellas de 750 mL que se llenan con 3.000 litros.",
    extend="Explica con un ejemplo por qué el valor nominal y la tolerancia protegen al comprador.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Control de calidad del lote L-52 en la «Bodega Demo». Observaciones: Z1, una botella tiene 744 mL con tolerancia de ejemplo de 5 mL sobre 750; Z2, el 3 % de las etiquetas está torcido pero es legible; "
     "Z3, el lote impreso en las etiquetas de una caja es ilegible; Z4, un corcho llegó deteriorado y la botella gotea; Z5, la línea funciona normal, con todas las mediciones dentro de la tolerancia. Categorías: A, detener la línea y avisar; B, retener el lote y revisar; C, sin acción.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un caso de control de calidad en papel, a clasificar cada observación por su urgencia y a decidir quién actúa, sin operar la línea.",
    prior=["Sé qué son valor nominal y tolerancia.", "Sé qué datos lleva una etiqueta.", "Sé leer una lista de observaciones."],
    explain=[
        "Para analizar un lote se clasifica cada observación según su gravedad. Una botella que gotea o tiene un sello deteriorado puede ser un problema de inocuidad y de calidad: se retira ese producto y se informa. Un lote ilegible en la etiqueta quita la trazabilidad: se retienen las cajas hasta resolverlo. Una medición fuera de tolerancia se aparta y se registra. Un detalle estético menor, como una etiqueta torcida pero legible, se anota y se corrige después.",
        "Un buen análisis nombra la observación, la categoría, la evidencia y quién actúa. El operador avisa, el controlador de calidad decide qué lote se retiene, el jefe de envasado decide parar la línea y el personal autorizado hace los ajustes. Nadie sigue envasando con un problema que puede lastimar o contaminar, ni cambia un dato del registro.",
        f"Si hay vidrio roto o una máquina que atrapa, las personas se alejan y piden ayuda. {EMER} {AVISO}",
    ],
    vocab=[("retener", "dejar un lote aparte hasta resolver el problema"), ("inocuidad", "que el producto no dañe la salud"), ("trazabilidad", "posibilidad de seguir el origen de cada botella"), ("defecto estético", "detalle de apariencia que no afecta la seguridad ni el contenido"), ("evidencia", "dato del caso que respalda una categoría")],
    worked=[
        ("Clasificar un defecto", "Una botella de ejemplo sale de la línea con un trozo de vidrio dentro. ¿A qué categoría corresponde?", ["Un cuerpo extraño en la botella puede dañar la salud.", "Se detiene y se avisa: categoría A."], "A"),
        ("Defecto estético", "Una etiqueta de ejemplo está levemente torcida pero legible. ¿A qué categoría corresponde?", ["No afecta la seguridad.", "Se corrige después: categoría C."], "C"),
    ],
    mistakes=[("Seguir envasando con un corcho deteriorado «hasta terminar el estanque».", "Todo el lote podría salir defectuoso.", "Se detiene y se avisa."),
              ("Reetiquetar a mano el lote ilegible sin avisar.", "Puede mezclarse con otro lote.", "Se retiene y lo resuelve el jefe de envasado.")],
    T=[
        ("abc", "En el envasado del vino: ¿qué es la inocuidad?", "Que el producto no dañe la salud", "Que el producto cueste poco", "Que la botella sea bonita", "La inocuidad es no dañar la salud."),
        ("abc", "En el envasado del vino: ¿qué es un defecto estético?", "Un detalle de apariencia que no afecta la seguridad ni el contenido", "Un defecto que contamina el vino", "Una botella rota", "Lo estético no afecta la seguridad."),
        ("abc", "En el envasado del vino: ¿qué pasa si el lote es ilegible en la etiqueta?", "Se pierde la trazabilidad", "El vino aumenta de volumen", "La botella se rompe", "Sin lote no se puede seguir el origen."),
        ("abc", "{F} ¿A qué categoría corresponde Z4, el corcho deteriorado y la botella que gotea?", "A, detener la línea y avisar", "B, retener y revisar", "C, sin acción", "El goteo puede afectar la calidad y la inocuidad."),
        ("abc", "{F} ¿A qué categoría corresponde Z3, el lote ilegible en una caja?", "B, retener el lote y revisar", "A, detener la línea", "C, sin acción", "La falta de trazabilidad exige retener las cajas."),
        ("abc", "{F} ¿A qué categoría corresponde Z1, la botella de 744 mL?", "B, retener el lote y revisar", "A, detener la línea siempre", "C, sin acción", "La botella está fuera de la tolerancia de ejemplo."),
        ("abc", "{F} ¿A qué categoría corresponde Z2, etiquetas torcidas pero legibles?", "C, sin acción por ahora, y se anota", "A, detener la línea", "B, retener el lote", "Es un defecto estético menor que no afecta la seguridad."),
        ("abc", "{F} ¿A qué categoría corresponde Z5, la línea normal?", "C, sin acción", "A, detener la línea", "B, retener el lote", "Todas las mediciones cumplen la tolerancia de ejemplo."),
        ("=", "{F} ¿Cuántos mL de diferencia hay entre los 750 mL nominales y la botella de Z1?", "750-744", "Se resta la medición al valor nominal.", " mL"),
        ("=", "{F} Si de 400 etiquetas el 3 % está torcido, ¿cuántas etiquetas son?", "400*3//100", "Se calcula el porcentaje sobre el total de etiquetas.", " etiquetas"),
        ("abc", "{F} Una compañera dice: «seguimos envasando y corregimos el corcho al final». ¿Qué respuesta es correcta?", "Es incorrecto: se detiene la línea y se avisa", "Es correcto, para no perder tiempo", "Es correcto, si son pocas", "Seguir con un corcho dañado puede dañar todo el lote."),
        ("abc", "{F} Una botella explota por presión y varios vidrios salen disparados hacia las personas. ¿Qué corresponde a quien lo ve?", "Alejarse de la zona de riesgo y avisar a un adulto responsable y a emergencias", "Acercarse a recoger el vidrio", "Seguir con el trabajo", "El vidrio disparado puede herir; se pide ayuda."),
        ("abc", "En el envasado del vino: ¿por qué la categoría A tiene prioridad?", "Porque hay riesgo para la salud o la seguridad", "Porque es más barata", "Porque no necesita registro", "El riesgo para personas se atiende primero."),
    ],
    ctx=("abc", "Un conocido te cuenta que algunas de sus botellas gotean por el corcho y te pregunta si puede venderlas igual. ¿Qué respondes?", "Que no, porque pueden afectar la calidad y la inocuidad, y que consulte a un enólogo o al controlador de calidad", "Que sí, si son pocas", "Que sí, con un descuento", "Una botella que gotea puede tener un problema de calidad."),
    sc=[
        ("En el envasado del vino: ¿qué se hace con una botella que gotea?", "Se aparta y se avisa", "Puede ser un problema de calidad."),
        ("En el envasado del vino: ¿qué categoría tiene una etiqueta torcida pero legible?", "C, sin acción por ahora, y se anota", "Es un defecto estético menor que no afecta la seguridad."),
        ("En el envasado del vino: ¿quién decide qué lote se retiene?", "El controlador de calidad", "El controlador revisa la calidad de cada lote envasado."),
    ],
    op=("Observaciones de ejemplo de la «Bodega Demo 4»: W1, una botella gotea por el corcho; W2, 20 etiquetas de un total de 500 están torcidas pero legibles; W3, una caja no tiene lote visible; W4, todas las mediciones de llenado cumplen. Categorías: A, detener y avisar; B, retener y revisar; C, sin acción. Escribe (a) la categoría de W1 a W4, (b) qué porcentaje de etiquetas está torcido, (c) quién decide qué lote se retiene, (d) qué haces si ves vidrio roto en la línea.",
        "(a) W1: A; W2: C; W3: B; W4: C. (b) 20 × 100 ÷ 500 = 4 %. (c) El controlador de calidad. (d) No me acerco, aviso a un adulto responsable.",
        ["clasifica bien las cuatro observaciones", "calcula el porcentaje", "nombra al controlador", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["clasificar el goteo como normal", "proponer recoger el vidrio"],
        "Pregunta: «¿qué observación puede afectar la salud?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Clasifica en A, B o C tres observaciones inventadas: botella que gotea, etiqueta torcida y lote ilegible.",
    extend="Explica con un ejemplo por qué la trazabilidad por lote permite retirar solo las botellas con problemas.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). La «Bodega Demo» envasa un estanque de 9.000 litros en botellas de 750 mL, con una línea que llena 1.200 botellas por hora. Se rechazan 2 % de las botellas por defectos. "
     "Costo de ejemplo por botella (vidrio, corcho y etiqueta): $600. Costo de la línea: $90.000 por hora. Precio de venta de ejemplo: $4.000 por botella.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular botellas, horas de línea, rechazos y margen de un envasado.",
    prior=["Sé calcular botellas por estanque.", "Sé calcular porcentajes enteros.", "Sé multiplicar y dividir enteros."],
    explain=[
        "El número de botellas de un estanque es sus litros multiplicados por 1.000 y divididos entre los mL de cada botella. Las horas de línea son las botellas divididas entre las que se llenan por hora. Las botellas rechazadas son un porcentaje de las envasadas y no se venden. El ingreso es las botellas buenas por el precio, y el margen es el ingreso menos los costos del material y de la línea.",
        "El rechazo es una pérdida: cada botella rechazada ya gastó vidrio, corcho, etiqueta y tiempo de línea. Por eso reducir los defectos mejora el margen. Pero nunca se baja el nivel de control ni se saltan las normas de higiene para ahorrar. Los valores son de ejemplo y las decisiones las toman el jefe de envasado y el enólogo.",
        f"Los cálculos no reemplazan las BPM ni la seguridad en la línea. {EMER} {AVISO}",
    ],
    vocab=[("horas de línea", "botellas totales divididas entre las que se llenan por hora"), ("botellas rechazadas", "botellas con defectos que no se venden"), ("botellas buenas", "botellas envasadas menos las rechazadas"), ("costo de material", "gasto por botella en vidrio, corcho y etiqueta"), ("margen", "ingreso menos costos")],
    worked=[
        ("Horas de línea", "Una línea de ejemplo llena 500 botellas por hora y hay 3.000 botellas. ¿Cuántas horas necesita?", ["Se divide el total entre las botellas por hora.", "3.000 entre 500."], "6 horas"),
        ("Botellas buenas", "De 3.000 botellas de ejemplo se rechaza el 5 %. ¿Cuántas quedan buenas?", ["El 5 % de 3.000 es 150.", "3.000 menos 150."], "2.850 botellas"),
    ],
    mistakes=[("Calcular el ingreso con todas las botellas, incluidas las rechazadas.", "Las rechazadas no se venden.", "Se usan solo las botellas buenas."),
              ("Bajar el control de calidad para ahorrar tiempo.", "Aumenta el riesgo de reclamos y daños.", "El control no se negocia.")],
    T=[
        ("abc", "En el envasado del vino: ¿qué son las botellas buenas?", "Las botellas envasadas menos las rechazadas", "Todas las botellas del estanque", "Solo las botellas vacías", "Las buenas son las que se pueden vender."),
        ("abc", "En el envasado del vino: ¿por qué un rechazo es una pérdida?", "Porque ya gastó material y tiempo de línea sin poder venderse", "Porque aumenta el volumen", "Porque no se registra", "Cada rechazo ya costó material y tiempo."),
        ("abc", "En el envasado del vino: ¿qué es el margen?", "El ingreso menos los costos", "Los costos más el ingreso", "El número de botellas", "El margen resta los costos del ingreso."),
        ("=", "{F} ¿Cuántas botellas se llenan con el estanque?", "9000*1000//750", "Se pasan los litros a mL y se divide entre el contenido de cada botella.", " botellas"),
        ("=", "{F} ¿Cuántas horas de línea se necesitan?", "9000*1000//750//1200", "Se dividen las botellas totales entre las que se llenan por hora.", " horas"),
        ("=", "{F} ¿Cuántas botellas se rechazan?", "9000*1000//750*2//100", "Se calcula el 2 % de las botellas envasadas.", " botellas"),
        ("=", "{F} ¿Cuántas botellas buenas quedan?", "9000*1000//750-9000*1000//750*2//100", "Se resta el rechazo a las botellas envasadas.", " botellas"),
        ("=", "{F} ¿Cuál es el ingreso por las botellas buenas?", "(9000*1000//750-9000*1000//750*2//100)*4000", "Se multiplican las botellas buenas por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuál es el costo del material de todas las botellas envasadas?", "9000*1000//750*600", "Se multiplican las botellas envasadas por el costo de cada una.", " pesos"),
        ("=", "{F} ¿Cuál es el costo de la línea por todas las horas de envasado?", "9000*1000//750//1200*90000", "Se multiplican las horas de línea por el costo de cada hora.", " pesos"),
        ("abc", "{F} Un jefe propone no revisar el llenado para ahorrar tiempo de línea. ¿Qué corresponde?", "Rechazarlo: el control de calidad no se negocia", "Aceptarlo, para ahorrar", "Aceptarlo, si las botellas se ven llenas", "Sin control pueden salir botellas fuera de tolerancia."),
        ("abc", "{F} Una estudiante quiere operar la línea porque ya calculó el margen. ¿Qué corresponde?", "Rechazarlo: la línea la opera personal capacitado y autorizado", "Aceptarlo, si va despacio", "Aceptarlo, si usa guantes", "Calcular no habilita para operar maquinaria."),
        ("abc", "En el envasado del vino: ¿por qué reducir los rechazos mejora el margen?", "Porque se pierde menos material y se venden más botellas", "Porque se llenan menos botellas", "Porque baja el precio", "Menos rechazos significan más botellas vendibles."),
    ],
    ctx=("abc", "Un conocido te pregunta si le conviene envasar más rápido y te da solo las botellas por hora. ¿Qué respondes?", "Que también hay que mirar los rechazos, la seguridad y el control de calidad con su jefe de envasado", "Que sí, siempre", "Que no, nunca", "La velocidad influye en los defectos y la seguridad."),
    sc=[
        ("En el envasado del vino: ¿cómo se calcula el número de botellas de un estanque?", "Litros por 1.000 entre mL por botella", "Se convierten los litros a mL y se divide."),
        ("En el envasado del vino: ¿cómo se calculan las horas de línea?", "Botellas entre botellas por hora", "Las horas resultan de una división."),
        ("En el envasado del vino: ¿cómo se calcula el margen?", "Ingreso menos costos", "El margen es lo que queda tras pagar costos."),
    ],
    op=("Datos de ejemplo de la «Bodega Demo 5»: 6.000 litros en botellas de 750 mL; línea de 800 botellas por hora; 3 % de rechazo; precio $3.500 por botella; costo de material $500 por botella. Escribe (a) las botellas envasadas, (b) las horas de línea, (c) las botellas buenas, (d) el ingreso menos el costo del material.",
        "(a) 6.000 × 1.000 ÷ 750 = 8.000 botellas. (b) 8.000 ÷ 800 = 10 horas. (c) 8.000 − 240 = 7.760 botellas. (d) 7.760 × 3.500 − 8.000 × 500 = 27.160.000 − 4.000.000 = $23.160.000.",
        ["calcula las botellas", "calcula las horas", "calcula las botellas buenas", "calcula el ingreso menos el material"],
        ["hoja con las cuatro respuestas"],
        ["usar todas las botellas para el ingreso", "no restar el material"],
        "Pregunta: «¿cuántas botellas se rechazan del total?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula las horas de línea de 4.800 botellas con 600 botellas por hora.",
    extend="Explica con un ejemplo por qué un rechazo es más caro que la botella que se pierde.",
)

# ============================================================ OAM-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La bodega de producto terminado de la «Bodega Demo» guarda cajas de 12 botellas en pallets de 60 cajas, apilados hasta 4 niveles en estanterías. Un operador autorizado mueve los pallets con una grúa horquilla. "
     "Peligros anotados: pallets altos que pueden caer, la grúa horquilla que puede atropellar o volcar, botellas que se rompen y dejan vidrio y vino en el piso, estanterías sobrecargadas, cajas de cartón y madera que pueden arder, y variaciones de temperatura.")
build(
    O5, 1, F,
    use="Aprenderé qué son el bodegaje y el almacenamiento del vino envasado, qué condiciones ambientales requiere y cuáles son los peligros de una bodega de producto terminado.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "El bodegaje es guardar y cuidar el producto terminado hasta su despacho. El vino envasado se almacena en condiciones ambientales requeridas: temperatura estable y moderada, humedad adecuada, poca luz y sin vibraciones fuertes. Las variaciones bruscas de temperatura y el calor dañan el vino. Los productos se ordenan por lote y se rotan según la regla FIFO, que despacha primero lo que primero entró.",
        "La bodega tiene peligros: los pallets altos pueden caer; la grúa horquilla puede atropellar o volcar; las botellas rotas dejan vidrio y piso resbaloso; las estanterías sobrecargadas pueden colapsar; y las cajas de cartón y madera pueden arder. La jerarquía de controles ordena las medidas: eliminar, sustituir, cambiar el lugar o el equipo, reglas y capacitación y, al final, el equipo de protección personal (EPP).",
        f"Un sistema de rociadores contra incendio es un control de ingeniería; una regla de altura máxima de apilado es administrativa. La grúa la opera solo personal capacitado y autorizado, bajo la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("bodegaje", "guardar y cuidar el producto terminado hasta su despacho"), ("producto terminado", "vino ya envasado y etiquetado, listo para vender"), ("condiciones ambientales", "temperatura, humedad y luz del lugar de guarda"), ("FIFO", "regla que despacha primero lo que primero entró"), ("estantería", "estructura con niveles para guardar pallets"), ("grúa horquilla", "vehículo con horquillas para levantar y mover pallets"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Aplicar FIFO", "Un lote A entró el día 2 y un lote B entró el día 8. ¿Cuál se despacha primero según FIFO?", ["FIFO despacha primero lo más antiguo.", "El lote A entró antes."], "El lote A"),
        ("Clasificar un control", "Una bodega de ejemplo coloca topes y rieles fijos en las estanterías para que los pallets no se deslicen. ¿Qué tipo de control es?", ["Los topes cambian físicamente la estantería.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que apilar más pallets «cabe» si la estantería aguanta.", "Cada estantería tiene una carga y una altura máximas.", "Se respeta el máximo indicado."),
              ("Creer que leer sobre la grúa horquilla habilita para conducirla.", "Conducirla exige formación y autorización.", "Aprende aquí el concepto y deja la operación a personal autorizado.")],
    T=[
        ("abc", "En la bodega de producto terminado: ¿qué es el bodegaje?", "Guardar y cuidar el producto terminado hasta su despacho", "Cosechar la uva", "Fermentar el mosto", "El bodegaje cuida el producto ya terminado."),
        ("abc", "En la bodega de producto terminado: ¿qué significa FIFO?", "Primero entra, primero sale", "Primero entra, último sale", "Solo sale lo más caro", "FIFO despacha primero lo más antiguo."),
        ("abc", "En la bodega de producto terminado: ¿qué condición ambiental cuida el vino?", "Una temperatura estable y moderada", "Una luz fuerte todo el día", "Un piso mojado", "El calor y las variaciones de temperatura dañan el vino."),
        ("=", "{F} Un pallet lleva 60 cajas de 12 botellas. ¿Cuántas botellas lleva un pallet?", "60*12", "Se multiplican las cajas por las botellas de cada caja.", " botellas"),
        ("abc", "{F} Instalar rociadores automáticos contra incendio es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla", "De EPP, porque protege a quien trabaja", "Los rociadores actúan sin depender de las personas."),
        ("abc", "{F} Una regla que dice «altura máxima de apilado: 4 niveles» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia la estantería", "De sustitución, porque cambia el pallet", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a los pallets apilados en altura?", "Que caigan y aplasten a una persona", "El pallet mismo", "Que ocupen poco espacio", "El riesgo es la posibilidad de daño; el pallet en altura es el peligro."),
        ("abc", "{F} Una estudiante dice: «ya aprendí cómo se mueve un pallet, así que conduzco la grúa». ¿Qué respuesta es correcta?", "Es peligroso: la grúa la opera personal capacitado y autorizado", "Es correcto, si va lento", "Es correcto, si usa casco", "Conducir la grúa exige formación y autorización."),
        ("abc", "{F} Un pallet se inclina y se ve a punto de caer sobre un pasillo con personas. ¿Qué corresponde según las reglas generales?", "Alejarte de la zona de riesgo y avisar a un adulto responsable y a emergencias", "Sujetar el pallet con las manos", "Pasar por debajo rápidamente", "Un pallet que cae puede aplastar; se avisa a quienes pueden actuar."),
        ("abc", "En la bodega de producto terminado: ¿por qué se ordena el producto por lote?", "Porque permite seguir el origen y despachar con FIFO", "Porque las botellas pesan menos", "Porque no necesita registro", "El orden por lote facilita la trazabilidad."),
        ("abc", "{F} Se propone solo entregar cascos para el peligro de los pallets altos. ¿Qué medida es más efectiva?", "Respetar la altura máxima y usar estanterías en buen estado", "Entregar cascos más resistentes", "Pedir mayor cuidado", "Limitar la altura actúa sobre el peligro."),
        ("=", "{F} Una estantería de ejemplo tiene 10 posiciones por nivel y 4 niveles. ¿Cuántos pallets caben?", "10*4", "Se multiplican las posiciones por los niveles.", " pallets"),
        ("abc", "En la bodega de producto terminado: ¿por qué el vidrio roto y el vino derramado son un peligro?", "Porque cortan y hacen resbalar", "Porque aumentan el calor", "Porque llenan la estantería", "El vidrio corta y el líquido hace resbalar."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por conducir la grúa horquilla de su bodega «porque ya viste cómo se hace». ¿Qué respondes?", "Que no, porque exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, a poca velocidad", "Que sí, solo un rato", "Haber visto el concepto no habilita para operar vehículos."),
    sc=[
        ("En la bodega de producto terminado: ¿qué es el producto terminado?", "El vino ya envasado y etiquetado, listo para vender", "Es el producto final del proceso."),
        ("En la bodega de producto terminado: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En la bodega de producto terminado: ¿qué hace FIFO?", "Despacha primero lo más antiguo", "FIFO evita que el producto envejezca en la bodega."),
    ],
    op=("La «Bodega Demo 2» anota una tarea de ejemplo: apilar pallets a 6 niveles en una estantería de 4, con la grúa operada por una persona sin autorización, en un pasillo con gente. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves un pallet a punto de caer.",
        "(a) Peligro: pallets apilados sobre el máximo; riesgo: que caigan y aplasten a una persona. (b) Una regla de altura máxima y de que solo personal autorizado opera la grúa. (c) Estanterías con topes y pasillos señalizados y separados. (d) Me alejo, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "se aleja y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer sujetar el pallet", "proponer solo casco"],
        "Pregunta: «¿qué control limita la altura aunque alguien se olvide de la regla?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres peligros de una bodega de vino envasado y el riesgo de cada uno.",
    extend="Explica con un ejemplo por qué el calor dañaría un vino ya envasado.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 2 (parámetros y registros de ejemplo, inventados). Bodega de producto terminado de la «Bodega Demo». Parámetros de ejemplo: temperatura de 12 a 16 grados; humedad del aire de 60 a 75 %. Lecturas del día: mañana, 14 grados y 70 %; tarde, 18 grados y 72 %. "
     "Inventario: el sistema dice 1.200 cajas; el conteo físico encontró 1.176 cajas. Lotes: L-45 entró el día 3 con 600 cajas y L-52 entró el día 10 con 600 cajas. Documentos: el kárdex (ingresos y salidas), el registro de condiciones y la guía de despacho. Roles: jefe de bodega, bodeguero, operador de grúa autorizado y controlador.")
build(
    O5, 2, F,
    use="Aprenderé a leer parámetros ambientales e inventarios de una bodega, a calcular diferencias de inventario y a conocer los documentos y roles del bodegaje.",
    prior=["Sé qué es el bodegaje y FIFO.", "Sé comparar valores con rangos.", "Sé calcular porcentajes enteros."],
    explain=[
        "El registro de condiciones anota la temperatura y la humedad de la bodega con fecha y hora. Si una lectura sale del rango, no está conforme y se informa tal cual. El kárdex anota cada ingreso y cada salida de cajas por lote. El inventario es el conteo de lo que hay: el inventario del sistema es lo que dicen los registros y el inventario físico es lo que se cuenta en la bodega. La diferencia entre ambos es una merma o un error de registro y debe explicarse.",
        "La guía de despacho acompaña a las cajas cuando salen de la bodega. El jefe de bodega organiza, el bodeguero cuenta y ordena, el operador autorizado mueve los pallets con la grúa y el controlador verifica el inventario. Un inventario no se ajusta para que «cuadre»: se investiga la diferencia y se registra la causa.",
        f"Una lectura fuera de rango o una diferencia sin explicar se informa el mismo día. {EMER} {AVISO}",
    ],
    vocab=[("kárdex", "registro de cada ingreso y salida de cajas por lote"), ("inventario del sistema", "cantidad que dicen los registros"), ("inventario físico", "cantidad que se cuenta en la bodega"), ("merma", "producto que se pierde por rotura, error o robo"), ("guía de despacho", "documento que acompaña las cajas al salir de la bodega"), ("registro de condiciones", "documento con temperatura y humedad de la bodega")],
    worked=[
        ("Diferencia de inventario", "El sistema dice 500 cajas y el conteo encontró 485. ¿Cuántas cajas faltan?", ["Se resta el conteo físico al del sistema.", "500 menos 485."], "15 cajas"),
        ("Comparar con el rango", "El rango de ejemplo es de 12 a 16 grados y la lectura es 19. ¿Está conforme?", ["19 es mayor que 16.", "Está fuera de rango."], "No, está fuera de rango"),
    ],
    mistakes=[("Ajustar el inventario del sistema al físico sin buscar la causa.", "Se oculta la diferencia.", "Se investiga y se registra la causa."),
              ("Anotar una temperatura dentro del rango sin haberla medido.", "Se falsea el registro.", "Se anota solo lo medido.")],
    T=[
        ("abc", "En la bodega de producto terminado: ¿qué es el inventario físico?", "La cantidad que se cuenta en la bodega", "La cantidad que dicen los registros", "El precio de las cajas", "El físico es lo que se cuenta."),
        ("abc", "En la bodega de producto terminado: ¿qué es la merma?", "El producto que se pierde por rotura, error o robo", "El producto que se vende", "El producto que entra", "La merma es una pérdida de producto que debe explicarse."),
        ("abc", "En la bodega de producto terminado: ¿para qué sirve la guía de despacho?", "Para acompañar las cajas cuando salen de la bodega", "Para anotar la humedad", "Para fijar el precio", "La guía acompaña el despacho de las cajas fuera de la bodega."),
        ("=", "{F} ¿Cuántas cajas de diferencia hay entre el sistema y el conteo físico?", "1200-1176", "Se resta el conteo físico al inventario del sistema.", " cajas"),
        ("=", "{F} ¿Qué porcentaje del inventario del sistema representa esa diferencia?", "(1200-1176)*100//1200", "Se divide la diferencia entre el inventario del sistema y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué lectura de la ficha está fuera del rango de temperatura?", "La de la tarde, 18 grados", "La de la mañana, 14 grados", "Ninguna", "18 supera el máximo de 16."),
        ("abc", "{F} ¿Cuál lote se despacha primero según FIFO?", "L-45, porque entró el día 3", "L-52, porque entró el día 10", "Ambos a la vez", "L-45 entró antes, así que sale primero con FIFO."),
        ("abc", "{F} ¿Qué documento anota los ingresos y salidas de cajas por lote?", "El kárdex", "El registro de condiciones", "La guía de despacho", "El kárdex registra los movimientos de entrada y de salida."),
        ("abc", "{F} ¿Qué rol mueve los pallets con la grúa?", "El operador de grúa autorizado", "El bodeguero sin autorización", "El comprador", "Solo el personal autorizado conduce la grúa."),
        ("abc", "{F} Un bodeguero dice: «faltan 24 cajas, ajusto el sistema a 1.176 y listo». ¿Qué respuesta es correcta?", "Es incorrecto: se investiga la causa y se registra antes de ajustar", "Es correcto, porque cuadra", "Es correcto, si son pocas", "Ajustar sin investigar oculta el problema."),
        ("abc", "{F} El jefe quiere anotar 16 grados en la lectura de la tarde, aunque fue 18. ¿Qué corresponde?", "Rechazarlo: se anota la lectura real e informa", "Aceptarlo, para cumplir el rango", "Aceptarlo, si nadie revisa", "Alterar una lectura falsea el registro."),
        ("abc", "{F} Una caja cae de un pallet alto y varias botellas se rompen junto a una persona. ¿Qué corresponde a quien lo ve?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Recoger los vidrios con las manos", "Acercarse a mirar", "El vidrio corta; se avisa a quienes tienen el equipo."),
        ("abc", "En la bodega de producto terminado: ¿por qué conviene hacer inventarios periódicos?", "Para detectar diferencias y corregir a tiempo", "Para ocultar la merma", "Para evitar registrar", "Los inventarios muestran diferencias a tiempo."),
    ],
    ctx=("abc", "Un conocido te pide que anotes en el kárdex salidas de cajas que no ocurrieron para que el inventario cuadre. ¿Qué respondes?", "Que no, porque se registra solo lo ocurrido, y que lo consultarás con un adulto responsable", "Que sí, si cuadra", "Que sí, solo algunas", "Registrar lo que no ocurrió falsea el inventario."),
    sc=[
        ("En la bodega de producto terminado: ¿cómo se calcula la diferencia de inventario?", "Sistema menos conteo físico", "La diferencia compara lo registrado con lo contado."),
        ("En la bodega de producto terminado: ¿qué se hace con una lectura fuera de rango?", "Se anota tal cual y se informa", "Un registro veraz permite actuar a tiempo ante un problema."),
        ("En la bodega de producto terminado: ¿qué lote sale primero con FIFO?", "El más antiguo", "FIFO despacha lo más antiguo para que no envejezca."),
    ],
    op=("Datos de ejemplo de la «Bodega Demo 3»: rango de 12 a 16 grados; lecturas de 15 y 17 grados; el sistema dice 800 cajas y el conteo físico encontró 784; lote M-10 entró el día 4 y lote M-12 entró el día 9. Escribe (a) la diferencia de inventario, (b) el porcentaje de la diferencia, (c) qué lectura está fuera de rango, (d) qué lote sale primero.",
        "(a) 800 − 784 = 16 cajas. (b) 16 × 100 ÷ 800 = 2 %. (c) La de 17 grados. (d) El lote M-10.",
        ["calcula la diferencia", "calcula el porcentaje", "identifica la lectura fuera de rango", "aplica FIFO"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "ajustar sin investigar"],
        "Pregunta: «¿qué dos cantidades comparas para la diferencia?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula la diferencia entre 600 cajas del sistema y 588 del conteo físico.",
    extend="Explica con un ejemplo por qué una diferencia de inventario debe tener una causa registrada.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Observaciones en la bodega de producto terminado de la «Bodega Demo». V1, la temperatura marca 22 grados desde hace tres días (rango de ejemplo 12 a 16). V2, cajas de cartón de la fila inferior con manchas de humedad y etiquetas despegadas. "
     "V3, un pallet está apilado a 6 niveles y la estantería permite 4. V4, el conteo físico coincide con el sistema y las condiciones son normales. V5, hay humo saliendo de un tablero eléctrico del pasillo. Categorías: A, alejarse y avisar de inmediato; B, informar y corregir; C, sin acción.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso de bodegaje en papel, a clasificar cada observación por su urgencia y a decidir quién actúa, sin intervenir equipos ni pallets.",
    prior=["Sé qué son las condiciones ambientales de una bodega.", "Sé leer un inventario.", "Sé leer una lista de observaciones."],
    explain=[
        "Para analizar una bodega se clasifica cada observación según su gravedad. Humo en un tablero eléctrico, un pallet a punto de caer o un derrame con gente cerca son emergencias: las personas se alejan y piden ayuda. Una temperatura fuera de rango sostenida, cajas con humedad o un apilado sobre el máximo no son emergencias inmediatas, pero se informan y se corrigen. Una bodega normal no necesita acción, aunque se sigue vigilando.",
        "Un buen análisis nombra la observación, la categoría, la evidencia y quién actúa. El bodeguero informa, el jefe de bodega decide, el personal de mantención autorizado revisa la temperatura y el tablero, y el operador autorizado reordena los pallets. Un pallet sobre el máximo no se baja por cuenta propia ni se revisa un tablero con humo.",
        f"El calor sostenido puede dañar el vino ya envasado, y la humedad puede estropear cajas y etiquetas. {EMER} {AVISO}",
    ],
    vocab=[("temperatura sostenida", "temperatura que se mantiene fuera de rango varios días"), ("humedad", "agua en el aire o en las cajas"), ("urgencia", "qué tan rápido hay que actuar"), ("corregir", "arreglar una causa con quien corresponde"), ("evidencia", "dato del caso que respalda una categoría")],
    worked=[
        ("Clasificar la urgencia", "Un pallet de ejemplo se ve inclinado y a punto de caer sobre un pasillo con personas. ¿A qué categoría corresponde?", ["Un pallet que cae puede aplastar a una persona.", "Es riesgo inmediato: categoría A, alejarse y avisar."], "A"),
        ("Clasificar un desvío", "Una bodega de ejemplo está 3 grados sobre su rango desde hace dos días. ¿A qué categoría corresponde?", ["No es una emergencia inmediata.", "Se informa y se corrige: categoría B."], "B")
    ],
    mistakes=[("Revisar un tablero con humo «para ver qué pasa».", "Hay riesgo de descarga y de incendio.", "Se aleja y se avisa a emergencias."),
              ("Bajar un pallet sobre el máximo con la grúa sin estar autorizado.", "Operar la grúa exige formación y autorización.", "Se informa y lo reordena personal autorizado.")],
    T=[
        ("abc", "En la bodega de producto terminado: ¿qué es una temperatura sostenida fuera de rango?", "La que se mantiene fuera de rango varios días", "La que cambia una vez al año", "La que siempre está en rango", "Sostenida significa que se mantiene en el tiempo."),
        ("abc", "En la bodega de producto terminado: ¿qué es corregir una causa?", "Arreglarla con quien corresponde", "Ocultarla", "Esperar a que desaparezca", "Corregir es resolver el problema con quien corresponde."),
        ("abc", "En la bodega de producto terminado: ¿qué efecto puede tener la humedad en las cajas?", "Estropear el cartón y despegar las etiquetas", "Aumentar el volumen del vino", "Hacer más duro el vidrio", "La humedad daña cartón y etiquetas."),
        ("abc", "{F} ¿A qué categoría corresponde V5, el humo en el tablero eléctrico?", "A, alejarse y avisar de inmediato", "B, informar y corregir", "C, sin acción", "El humo indica riesgo de incendio o descarga."),
        ("abc", "{F} ¿A qué categoría corresponde V1, 22 grados sostenidos?", "B, informar y corregir", "A, alejarse y avisar", "C, sin acción", "Es un desvío del parámetro sin emergencia inmediata."),
        ("abc", "{F} ¿A qué categoría corresponde V3, el pallet apilado a 6 niveles?", "B, informar y corregir con personal autorizado", "A, alejarse y avisar siempre", "C, sin acción", "Supera el máximo; se informa y se reordena."),
        ("abc", "{F} ¿A qué categoría corresponde V2, las cajas con humedad?", "B, informar y corregir la causa", "A, alejarse y avisar", "C, sin acción", "La humedad daña las cajas y debe corregirse."),
        ("abc", "{F} ¿A qué categoría corresponde V4, el conteo coincide y las condiciones son normales?", "C, sin acción", "A, alejarse y avisar", "B, informar y corregir", "No hay ninguna anomalía que informar ni corregir."),
        ("=", "{F} ¿Cuántos grados sobre el máximo está la bodega en V1?", "22-16", "Se resta el máximo del rango a la lectura.", " grados"),
        ("=", "{F} ¿Cuántos niveles sobre el máximo está el pallet de V3?", "6-4", "Se resta el máximo permitido a los niveles apilados.", " niveles"),
        ("abc", "{F} Una compañera dice: «voy a abrir el tablero con humo para ver qué pasa». ¿Qué respuesta es correcta?", "Es peligroso: se aleja y se avisa a emergencias", "Es correcto, si apaga la luz", "Es correcto, si usa guantes", "Un tablero con humo puede dar una descarga o incendiarse."),
        ("abc", "{F} Una persona intenta bajar con las manos un pallet apilado a 6 niveles y el pallet se inclina. ¿Qué corresponde a quien lo ve?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Ayudar a sostenerlo", "Pasar por debajo", "Un pallet que cae puede aplastar."),
        ("abc", "En la bodega de producto terminado: ¿por qué se informa el desvío de temperatura aunque no sea una emergencia?", "Porque el calor sostenido puede dañar el vino", "Porque se corrige solo", "Porque no afecta el producto", "El calor sostenido deteriora el vino."),
    ],
    ctx=("abc", "Un conocido te cuenta que su bodega está a 25 grados todo el verano y te pregunta si el vino «se aguanta». ¿Qué respondes?", "Que el calor sostenido puede dañar el vino y que debe consultar a su enólogo", "Que sí, que se aguanta", "Que lo cubra con una manta", "El calor sostenido deteriora el vino envasado."),
    sc=[
        ("En la bodega de producto terminado: ¿qué se hace ante humo en un tablero eléctrico?", "Se aleja y se avisa a emergencias", "Hay riesgo de incendio o de descarga."),
        ("En la bodega de producto terminado: ¿qué categoría tiene una temperatura fuera de rango sostenida?", "B, informar y corregir", "No es emergencia, pero daña el vino."),
        ("En la bodega de producto terminado: ¿quién reordena un pallet sobre el máximo?", "Personal autorizado", "Operar la grúa exige formación y autorización."),
    ],
    op=("Observaciones de ejemplo de la «Bodega Demo 4»: U1, humo saliendo de la grúa horquilla estacionada; U2, 21 grados sostenidos con rango de ejemplo de 12 a 16; U3, un pallet a 5 niveles con máximo de 4; U4, todo normal. Categorías: A, alejarse y avisar; B, informar y corregir; C, sin acción. Escribe (a) la categoría de U1 a U4, (b) cuántos grados sobre el máximo está U2, (c) quién reordena el pallet de U3, (d) qué haces si ves humo.",
        "(a) U1: A; U2: B; U3: B; U4: C. (b) 21 − 16 = 5 grados. (c) Personal autorizado. (d) Me alejo, aviso a un adulto responsable y a emergencias.",
        ["clasifica bien las cuatro observaciones", "calcula el exceso", "nombra quién reordena", "se aleja y avisa"],
        ["hoja con las cuatro respuestas"],
        ["clasificar el humo como normal", "proponer revisar el humo"],
        "Pregunta: «¿qué observación tiene riesgo inmediato?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Clasifica en A, B o C tres observaciones inventadas: humo, temperatura alta sostenida y bodega normal.",
    extend="Explica con un ejemplo por qué un desvío sostenido es un problema aunque no sea una emergencia.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). La bodega de producto terminado de la «Bodega Demo» tiene 10 posiciones por nivel y 4 niveles. Cada pallet lleva 60 cajas de 12 botellas. Ventas de ejemplo: 4.800 cajas por mes (30 días). "
     "Stock actual: 2.400 cajas (la estantería está llena). Costo de guarda de ejemplo: $50 por caja por mes. Merma de ejemplo por mal almacenamiento: 1 caja por cada 100 almacenadas al mes.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular capacidad, días de inventario, costo de guarda y mermas de una bodega de vino envasado.",
    prior=["Sé qué es el bodegaje y el inventario.", "Sé multiplicar y dividir enteros.", "Sé calcular porcentajes sencillos."],
    explain=[
        "La capacidad de una estantería en pallets es las posiciones por nivel por los niveles. Las cajas que caben son los pallets por las cajas de cada uno. Los días de inventario son el stock dividido entre las ventas diarias; indican cuántos días alcanza lo guardado. El costo de guarda es las cajas por el costo por caja por mes. La merma es el producto que se pierde por mal almacenamiento.",
        "Con estos cálculos se decide si hay espacio, si conviene guardar más tiempo o si hay que despachar más rápido. Un inventario muy grande cuesta más y envejece el vino; uno muy pequeño puede dejar sin producto a los clientes. Los valores son de ejemplo y las decisiones las toman el jefe de bodega y el enólogo.",
        f"La capacidad máxima y la altura de apilado nunca se superan para guardar más. {EMER} {AVISO}",
    ],
    vocab=[("capacidad de la estantería", "pallets que caben según posiciones y niveles"), ("días de inventario", "stock dividido entre las ventas diarias"), ("stock", "cantidad de cajas que hay guardadas"), ("costo de guarda", "gasto de guardar cada caja por mes"), ("merma", "producto que se pierde por mal almacenamiento")],
    worked=[
        ("Capacidad en pallets", "Una estantería de ejemplo tiene 8 posiciones por nivel y 3 niveles. ¿Cuántos pallets caben?", ["Se multiplican las posiciones por los niveles.", "8 por 3."], "24 pallets"),
        ("Días de inventario", "El stock de ejemplo es 600 cajas y se venden 20 por día. ¿Cuántos días alcanza?", ["Se divide el stock entre las ventas diarias.", "600 entre 20."], "30 días"),
    ],
    mistakes=[("Guardar más pallets que la capacidad «porque entran apretados».", "Se supera el máximo de altura o de carga.", "Se respeta la capacidad y se usa otro lugar."),
              ("Calcular los días de inventario con las ventas mensuales en vez de diarias.", "La división mezcla unidades.", "Se divide el stock entre las ventas diarias.")],
    T=[
        ("abc", "En la bodega de producto terminado: ¿qué son los días de inventario?", "El stock dividido entre las ventas diarias", "El número de pallets", "Las ventas del mes", "Los días de inventario indican cuánto alcanza el stock."),
        ("abc", "En la bodega de producto terminado: ¿qué es el stock?", "La cantidad de cajas que hay guardadas", "El precio de las cajas", "El costo por mes", "El stock es la cantidad de cajas que está guardada."),
        ("abc", "En la bodega de producto terminado: ¿qué pasa si el inventario es muy grande?", "Cuesta más guardarlo y el vino envejece más tiempo", "Se vende más", "Se rompe menos", "Un inventario grande aumenta costos y tiempo de guarda."),
        ("=", "{F} ¿Cuántos pallets caben en la estantería?", "10*4", "Se multiplican las posiciones por nivel por los niveles.", " pallets"),
        ("=", "{F} ¿Cuántas cajas caben en la estantería llena?", "10*4*60", "Se multiplican los pallets por las cajas de cada pallet.", " cajas"),
        ("=", "{F} ¿Cuántas botellas hay en la estantería llena?", "10*4*60*12", "Se multiplican las cajas por las botellas de cada caja.", " botellas"),
        ("=", "{F} ¿Cuántas cajas se venden por día?", "4800//30", "Se dividen las ventas del mes entre los días del mes.", " cajas"),
        ("=", "{F} ¿Cuántos días de inventario hay con el stock actual?", "2400//(4800//30)", "Se divide el stock entre las ventas diarias.", " días"),
        ("=", "{F} ¿Cuánto cuesta guardar el stock actual por un mes?", "2400*50", "Se multiplican las cajas por el costo de guarda mensual.", " pesos"),
        ("=", "{F} ¿Cuántas cajas se pierden por mal almacenamiento al mes, a razón de 1 por cada 100 almacenadas?", "2400//100*1", "Se calcula cuántos grupos de 100 cajas hay y se multiplica por 1.", " cajas"),
        ("abc", "{F} Un bodeguero propone apilar a 6 niveles para guardar más cajas. ¿Qué corresponde?", "Rechazarlo: se respeta la altura máxima y se usa otro lugar", "Aceptarlo, para guardar más", "Aceptarlo, si la estantería parece firme", "Superar la altura máxima aumenta el riesgo de caída."),
        ("abc", "{F} Una estudiante quiere mover los pallets con la grúa porque ya calculó la capacidad. ¿Qué corresponde?", "Rechazarlo: la grúa la opera personal capacitado y autorizado", "Aceptarlo, si va despacio", "Aceptarlo, si hay otro adulto", "Calcular no habilita para operar la grúa."),
        ("abc", "En la bodega de producto terminado: ¿por qué conviene vigilar los días de inventario?", "Para equilibrar el costo de guardar y no quedarse sin producto", "Para ocultar las ventas", "Para evitar contar", "Los días de inventario guían el nivel de stock."),
    ],
    ctx=("abc", "Un conocido te pregunta si le conviene guardar el doble de vino y te da solo el costo de la bodega. ¿Qué respondes?", "Que faltan las ventas y la capacidad, y que lo decide con su enólogo y jefe de bodega", "Que sí, siempre", "Que no, nunca", "Sin ventas ni capacidad no se puede decidir."),
    sc=[
        ("En la bodega de producto terminado: ¿cómo se calcula la capacidad en pallets?", "Posiciones por nivel por niveles", "La capacidad multiplica posiciones y niveles."),
        ("En la bodega de producto terminado: ¿cómo se calculan los días de inventario?", "Stock entre ventas diarias", "El resultado indica cuántos días alcanza el stock."),
        ("En la bodega de producto terminado: ¿cómo se calcula el costo de guarda?", "Cajas por costo por caja por mes", "El costo se multiplica por las cajas."),
    ],
    op=("Datos de ejemplo de la «Bodega Demo 5»: estantería con 6 posiciones por nivel y 5 niveles; 50 cajas por pallet; ventas de 3.000 cajas por mes de 30 días; stock de 1.200 cajas; costo de guarda de $40 por caja por mes. Escribe (a) los pallets que caben, (b) las cajas que caben, (c) los días de inventario, (d) el costo mensual de guardar el stock.",
        "(a) 6 × 5 = 30 pallets. (b) 30 × 50 = 1.500 cajas. (c) Ventas diarias: 3.000 ÷ 30 = 100; 1.200 ÷ 100 = 12 días. (d) 1.200 × 40 = $48.000.",
        ["calcula los pallets", "calcula las cajas", "calcula los días de inventario", "calcula el costo mensual"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por los niveles", "dividir entre las ventas mensuales"],
        "Pregunta: «¿cuántas cajas se venden por día?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula los días de inventario de un stock inventado de 1.800 cajas con ventas diarias de 60.",
    extend="Explica con un ejemplo por qué un inventario muy grande puede ser un problema para el vino.",
)

# ============================================================ OAM-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Antes de la vendimia, la «Bodega Demo» revisa sus máquinas y equipos (moledora-despalilladora, prensa, bombas, filtro y llenadora), sus instrumentos (refractómetro, termómetro, medidor de pH) y sus utensilios (mangueras, baldes y tamices). "
     "Peligros anotados: partes móviles, energía almacenada en la prensa, electricidad cerca del agua, agua caliente y productos de limpieza y sanitización, ruido y dióxido de carbono en la sala de estanques.")
build(
    O6, 1, F,
    use="Aprenderé qué significa verificar el funcionamiento de la maquinaria, los equipos, los instrumentos y los utensilios de una bodega, y cuáles son los peligros de ese trabajo, sin operar ni reparar nada.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Verificar el funcionamiento es comprobar que una máquina, un equipo, un instrumento o un utensilio está listo y funciona como se espera antes de usarlo. Una máquina hace un trabajo, como la prensa o la bomba; un instrumento mide, como el refractómetro; y un utensilio es una herramienta de apoyo, como una manguera o un balde. Verificar asegura la disponibilidad, es decir, que todo esté listo para que el proceso no se detenga en plena vendimia. Además se verifica la higiene: lo que toca el vino debe estar limpio.",
        "El trabajo de verificación tiene peligros: las partes móviles atrapan; la prensa puede soltar energía almacenada; la electricidad con agua causa descargas; el agua caliente quema; los productos de limpieza irritan; y el dióxido de carbono puede quitar el aire. La jerarquía de controles aplica. Antes de intervenir una máquina, personal autorizado la deja sin energía y la señaliza, lo que se llama bloqueo y etiquetado.",
        f"El operador observa y reporta; el mecánico autorizado interviene. Nadie repara ni abre un equipo por cuenta propia. {EMER} {AVISO}",
    ],
    vocab=[("verificar", "comprobar que algo funciona como se espera antes de usarlo"), ("disponibilidad", "que los equipos estén listos para que el proceso no se detenga"), ("utensilio", "herramienta de apoyo, como una manguera o un balde"), ("instrumento", "aparato que mide algo, como un refractómetro"), ("bloqueo y etiquetado", "dejar un equipo sin energía y señalizar que no se debe encender"), ("energía almacenada", "energía que un equipo conserva aunque esté apagado"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Equipo o instrumento", "En una bodega de ejemplo se usa un aparato que mide el azúcar del jugo de la uva. ¿Es una máquina o un instrumento?", ["Su función es medir.", "Es un instrumento."], "Instrumento"),
        ("Clasificar un control", "Una bodega de ejemplo instala una cubierta fija sobre el tablero eléctrico de la sala de bombas. ¿Qué tipo de control es?", ["La cubierta cambia físicamente el equipo.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que una máquina apagada no tiene peligros.", "Puede conservar energía almacenada.", "Solo personal autorizado la deja sin energía y la señaliza."),
              ("Creer que verificar es lo mismo que reparar.", "Verificar es comprobar; reparar es intervenir.", "Si algo falla, se reporta a personal autorizado.")],
    T=[
        ("abc", "En la bodega de vinificación: ¿qué significa verificar el funcionamiento de un equipo?", "Comprobar que funciona como se espera antes de usarlo", "Repararlo cuando se rompe", "Comprarlo nuevo", "Verificar es comprobar; reparar es otra tarea."),
        ("abc", "En la bodega de vinificación: ¿qué es un utensilio?", "Una herramienta de apoyo, como una manguera o un balde", "Una máquina que mueve líquidos", "Un instrumento que mide el azúcar", "El utensilio es una herramienta de apoyo."),
        ("abc", "En la bodega de vinificación: ¿qué es la disponibilidad de los equipos?", "Que estén listos para que el proceso no se detenga", "Que sean nuevos", "Que sean baratos", "La disponibilidad asegura la continuidad del proceso."),
        ("=", "{F} La bodega tiene 5 máquinas y equipos, 3 instrumentos y 4 utensilios por verificar. ¿Cuántos elementos son en total?", "5+3+4", "Se suman las máquinas, los instrumentos y los utensilios.", " elementos"),
        ("abc", "{F} Una protección fija sobre las cadenas de la bomba es un control de tipo:", "De ingeniería, porque cambia físicamente el equipo", "Administrativo, porque es una regla", "De EPP, porque protege a quien trabaja", "La protección es una parte del equipo y funciona siempre."),
        ("abc", "{F} Una regla que dice «el bloqueo y etiquetado lo hace solo personal autorizado» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia la prensa", "De sustitución, porque cambia al personal", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a la energía almacenada de la prensa?", "Que se libere de golpe y cause una lesión grave", "La prensa misma en la bodega", "Que esté apagada", "El riesgo es la posibilidad de daño; la energía almacenada es el peligro."),
        ("abc", "{F} Una estudiante dice: «ya aprendí a verificar la prensa, así que la abro y reviso por dentro». ¿Qué respuesta es correcta?", "Es peligroso: abrir o reparar lo hace personal autorizado", "Es correcto, si apaga el interruptor", "Es correcto, si usa guantes", "Un equipo apagado puede conservar energía."),
        ("abc", "{F} Una persona queda con la mano atrapada en una máquina de la bodega. ¿Qué corresponde según las reglas generales?", "No acercarte, avisar a un adulto responsable y a emergencias", "Tirar de ella para liberarla", "Encender la máquina para soltarla", "Mover la máquina puede agravar la lesión."),
        ("abc", "En la bodega de vinificación: ¿por qué se verifica la higiene de lo que toca el vino?", "Porque la suciedad puede contaminar el vino", "Porque el vino pesa más", "Porque las mangueras se encogen", "Lo que toca el vino debe estar limpio."),
        ("abc", "{F} Se propone solo entregar guantes por las partes móviles de los equipos. ¿Qué medida es más efectiva?", "Cubrir las partes móviles con protecciones fijas", "Entregar guantes más gruesos", "Pedir mayor cuidado", "Cubrir el peligro actúa más arriba que el EPP."),
        ("=", "{F} Si cada elemento tiene 4 puntos de verificación, ¿cuántos puntos se verifican en los 12 elementos de la bodega?", "(5+3+4)*4", "Se multiplican los elementos por los puntos de cada uno.", " puntos"),
        ("abc", "En la bodega de vinificación: ¿qué hace el operador si nota un ruido anormal en una bomba?", "Avisa de inmediato a su jefe, sin abrirla ni repararla", "La abre para revisarla", "La sigue usando", "El operador reporta; la revisión la hace personal autorizado."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por revisar y arreglar su prensa «porque ya sabes cómo funciona». ¿Qué respondes?", "Que no, porque exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, si está apagada", "Que sí, con guantes", "Haber visto el concepto no habilita para intervenir una prensa."),
    sc=[
        ("En la bodega de vinificación: ¿qué es un instrumento?", "Un aparato que mide algo", "El instrumento mide, como el refractómetro."),
        ("En la bodega de vinificación: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En la bodega de vinificación: ¿quién interviene una máquina con falla?", "Personal capacitado y autorizado", "La intervención exige formación y norma vigente."),
    ],
    op=("La «Bodega Demo 2» anota una tarea de ejemplo: abrir la tapa de la prensa para revisar su interior con la máquina recién apagada, sin bloqueo ni etiqueta, mientras otra persona limpia el piso mojado junto al tablero. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a alguien atrapado.",
        "(a) Peligro: energía almacenada y partes móviles de la prensa; riesgo: que la máquina se mueva y atrape a la persona. (b) Una regla de bloquear y etiquetar antes de cualquier intervención. (c) Una protección fija y un sistema de parada de emergencia. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer abrir la tapa", "no avisar"],
        "Pregunta: «¿qué control cubre la parte móvil aunque alguien se olvide de la regla?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Clasifica como máquina, instrumento o utensilio: refractómetro, prensa, manguera y medidor de pH.",
    extend="Explica con un ejemplo por qué una máquina apagada puede seguir siendo peligrosa.",
)

# ============================================================ OAM-06, clase 2
F = ("Ficha 2 (verificación de ejemplo, inventada). Refractómetro de la «Bodega Demo»: al medir agua pura (patrón de 0 °Brix) marcó 1 °Brix; tolerancia de ejemplo: 0 de diferencia. Termómetro: patrón de 20 grados, marcó 22; tolerancia de 1 grado. "
     "Plan de mantención de ejemplo: la prensa se revisa cada 150 horas de uso; lleva 130 horas desde la última revisión. Documentos: la hoja de verificación, el registro de verificaciones, la hoja de vida de cada equipo y el manual del fabricante. Roles: operador, mecánico autorizado, jefe de bodega y enólogo.")
build(
    O6, 2, F,
    use="Aprenderé los conceptos de patrón, error, tolerancia y plan de mantención, y los documentos y roles de la verificación de equipos e instrumentos de una bodega.",
    prior=["Sé qué significa verificar un equipo.", "Sé restar enteros.", "Sé leer una ficha con datos."],
    explain=[
        "Un instrumento se verifica comparándolo con un patrón, que es un valor conocido. El refractómetro debe marcar 0 °Brix con agua pura; si marca otro valor, tiene un error, que es la diferencia entre lo que marca y el patrón. La tolerancia es el error máximo aceptable. Un instrumento con error mayor que la tolerancia está fuera de tolerancia y no se debe usar hasta que personal autorizado lo calibre, es decir, lo ajuste.",
        "Las máquinas se verifican con un plan de mantención, que indica cada cuántas horas de uso se revisan. Para saber cuántas horas faltan se resta lo usado al intervalo. Los documentos son la hoja de verificación, que guía qué revisar; el registro de verificaciones, que anota fecha, equipo, resultado y responsable; la hoja de vida, que resume la historia del equipo; y el manual del fabricante. El operador reporta, el mecánico autorizado repara y el jefe de bodega decide si un equipo se retira.",
        f"Un resultado de verificación no se altera para que «cumpla». {EMER} {AVISO}",
    ],
    vocab=[("patrón", "valor conocido con el que se compara un instrumento"), ("error", "diferencia entre lo que marca el instrumento y el patrón"), ("tolerancia", "error máximo aceptable"), ("calibrar", "ajustar un instrumento para que marque el valor correcto"), ("plan de mantención", "documento que indica cada cuántas horas se revisa un equipo"), ("hoja de vida", "documento que resume la historia de un equipo")],
    worked=[
        ("Calcular el error", "Un termómetro de ejemplo marca 26 con un patrón de 25. ¿Cuál es el error?", ["Se resta el patrón a la lectura.", "26 menos 25."], "1 grado"),
        ("Horas que faltan", "Una bomba de ejemplo se revisa cada 200 horas y lleva 170. ¿Cuántas horas faltan?", ["Se resta lo usado al intervalo.", "200 menos 170."], "30 horas"),
    ],
    mistakes=[("Usar un instrumento fuera de tolerancia «porque se acerca».", "Sus mediciones llevarán a decisiones equivocadas.", "Se retira hasta que lo calibre personal autorizado."),
              ("Postergar la revisión de una máquina porque «todavía funciona».", "Una falla durante la vendimia detiene el proceso.", "Se respeta el plan de mantención.")],
    T=[
        ("abc", "En la bodega de vinificación: ¿qué es un patrón?", "Un valor conocido con el que se compara un instrumento", "El nombre del instrumento", "El precio del instrumento", "El patrón es el valor de referencia."),
        ("abc", "En la bodega de vinificación: ¿qué es la tolerancia?", "El error máximo aceptable", "El error mínimo", "El promedio de las lecturas", "La tolerancia fija el límite del error."),
        ("abc", "En la bodega de vinificación: ¿qué es calibrar un instrumento?", "Ajustarlo para que marque el valor correcto", "Cambiarle el color", "Guardarlo en una caja", "Calibrar corrige la lectura del instrumento."),
        ("=", "{F} ¿Cuál es el error del refractómetro, en °Brix?", "1-0", "Se resta el patrón a la lectura del refractómetro.", " °Brix"),
        ("abc", "{F} ¿Está el refractómetro dentro de la tolerancia de ejemplo?", "No, porque el error de 1 supera la tolerancia de 0", "Sí, porque el error es pequeño", "Sí, porque marca más que el patrón", "La tolerancia es 0 y el error es 1."),
        ("=", "{F} ¿Cuál es el error del termómetro, en grados?", "22-20", "Se resta el patrón a la lectura del termómetro.", " grados"),
        ("abc", "{F} ¿Está el termómetro dentro de la tolerancia de ejemplo?", "No, porque el error de 2 supera la tolerancia de 1", "Sí, porque el error es pequeño", "Sí, porque marca más que el patrón", "El error de 2 grados es mayor que 1."),
        ("=", "{F} ¿Cuántas horas faltan para la próxima revisión de la prensa?", "150-130", "Se resta lo usado al intervalo del plan.", " horas"),
        ("abc", "{F} ¿Qué documento anota fecha, equipo, resultado y responsable de cada verificación?", "El registro de verificaciones", "La hoja de vida", "El manual del fabricante", "El registro guarda lo ya verificado."),
        ("abc", "{F} ¿Qué rol repara y calibra los equipos?", "El mecánico autorizado", "El operador", "El comprador", "El mecánico autorizado interviene los equipos con falla."),
        ("abc", "{F} El jefe de bodega quiere anotar «conforme» para el refractómetro, aunque el error es 1. ¿Qué corresponde?", "Rechazarlo: se anota el resultado real e informa", "Aceptarlo, para cumplir", "Aceptarlo, si nadie lo revisa", "Anotar conforme algo que no lo es falsea el registro."),
        ("abc", "{F} Una estudiante quiere calibrar el termómetro con agua de la llave. ¿Qué corresponde?", "Rechazarlo: la calibración la hace personal autorizado con un patrón adecuado", "Aceptarlo, si el agua está fría", "Aceptarlo, si lo hace rápido", "Un patrón inadecuado deja el instrumento más desajustado."),
        ("abc", "En la bodega de vinificación: ¿por qué un error de medición puede ser grave durante la vendimia?", "Porque lleva a decisiones equivocadas sobre la uva o el vino", "Porque la uva pesa más", "Porque los instrumentos se cansan", "Un dato falso afecta las decisiones de calidad."),
    ],
    ctx=("abc", "Un conocido te pide que firmes que su refractómetro está calibrado sin haberlo comparado con un patrón. ¿Qué respondes?", "Que no, porque firmar sin comprobar lo falsea, y que lo consultarás con un adulto responsable", "Que sí, si se ve bien", "Que sí, solo una vez", "La calibración se comprueba con un patrón."),
    sc=[
        ("En la bodega de vinificación: ¿cómo se calcula el error de un instrumento?", "Lectura menos patrón", "El error es la diferencia con el patrón."),
        ("En la bodega de vinificación: ¿qué se hace con un instrumento fuera de tolerancia?", "Se retira hasta que lo calibre personal autorizado", "Un instrumento fuera de tolerancia entrega datos falsos."),
        ("En la bodega de vinificación: ¿cuántas horas faltan para una revisión de 150 horas con 130 usadas?", "20 horas", "Se resta lo usado al intervalo."),
    ],
    op=("Datos de ejemplo de la «Bodega Demo 3»: medidor de pH que marca 4 al medir un patrón de 3, con tolerancia de 0; bomba revisada cada 250 horas que lleva 220 horas de uso. Escribe (a) el error del medidor y si está dentro de la tolerancia, (b) las horas que faltan para la revisión de la bomba, (c) en qué documento anotas el resultado, (d) quién calibra el medidor.",
        "(a) 4 − 3 = 1; no está dentro de la tolerancia de 0. (b) 250 − 220 = 30 horas. (c) En el registro de verificaciones. (d) El mecánico autorizado.",
        ["calcula el error y concluye", "calcula las horas", "nombra el documento", "nombra quién calibra"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "usar un instrumento fuera de tolerancia"],
        "Pregunta: «¿qué valor se resta a la lectura para obtener el error?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el error de un termómetro que marca 11 al medir un patrón de 10 y compáralo con una tolerancia de 1.",
    extend="Explica con un ejemplo por qué un plan de mantención evita fallas durante la vendimia.",
)

# ============================================================ OAM-06, clase 3
F = ("Ficha 3 (hoja de verificación de ejemplo, inventada). Resultados previos a la vendimia en la «Bodega Demo»: Q1, la despalilladora hace un ruido metálico fuerte y vibra; Q2, el refractómetro marca 1 °Brix con agua pura (tolerancia de ejemplo 0); "
     "Q3, la bomba de trasiego funciona normal, con mangueras limpias; Q4, la prensa tiene una fuga de aceite hidráulico; Q5, las mangueras tienen restos de vino de la vendimia anterior sin limpiar. "
     "Categorías: A, no usar y avisar de inmediato; B, retirar o programar calibración, mantención o limpieza; C, conforme.")
build(
    O6, 3, F,
    use="Aprenderé a analizar los resultados de una verificación previa a la vendimia, a clasificar cada equipo según su urgencia y a decidir quién actúa, sin operar ni reparar.",
    prior=["Sé qué son error, tolerancia y calibración.", "Sé qué es una hoja de verificación.", "Sé leer una lista de resultados."],
    explain=[
        "Para analizar una verificación se clasifica cada equipo según su resultado. Un ruido metálico fuerte con vibración o una fuga de aceite hidráulico en una prensa indican riesgo de falla grave o de accidente: no se usa el equipo y se avisa de inmediato. Un instrumento fuera de tolerancia o un utensilio sucio no es una emergencia, pero no se usa hasta calibrarlo o limpiarlo. Un equipo normal está conforme.",
        "Un buen análisis nombra el equipo, la categoría, la evidencia y quién actúa. El operador reporta, el jefe de bodega decide si el equipo se retira, el mecánico autorizado repara o calibra, y el personal de limpieza capacitado limpia y sanitiza los utensilios. Nadie usa un equipo en categoría A ni cambia un dato para que pase la verificación.",
        f"La higiene también se verifica: lo que toca el vino debe estar limpio antes de la vendimia. {EMER} {AVISO}",
    ],
    vocab=[("fuga", "salida de líquido por donde no debería"), ("vibración", "temblor fuerte de una máquina que indica una posible falla"), ("sanitizar", "aplicar un tratamiento que reduce los microbios en una superficie"), ("categoría", "grupo según la urgencia"), ("evidencia", "dato del resultado que respalda una categoría")],
    worked=[
        ("Clasificar un equipo", "Un cable eléctrico de ejemplo de la sala de bombas está pelado y toca el piso mojado. ¿A qué categoría corresponde?", ["Hay riesgo inmediato de descarga eléctrica.", "Categoría A: no usar y avisar."], "A"),
        ("Clasificar un utensilio", "Una manguera de ejemplo tiene restos del año pasado, sin limpiar. ¿A qué categoría corresponde?", ["No es una emergencia, pero no se debe usar.", "Categoría B: limpiar antes de usar."], "B"),
    ],
    mistakes=[("Seguir usando una máquina que vibra «hasta terminar la vendimia».", "Puede romperse y causar un accidente.", "Se detiene si es seguro y se avisa."),
              ("Usar mangueras sin limpiar porque «el vino las limpia».", "Pueden contaminar el vino.", "Se limpian y sanitizan antes de usar.")],
    T=[
        ("abc", "En la bodega de vinificación: ¿qué es una fuga?", "Una salida de líquido por donde no debería", "Una medición correcta", "Un instrumento nuevo", "La fuga es líquido que sale donde no debe."),
        ("abc", "En la bodega de vinificación: ¿qué significa sanitizar un utensilio?", "Aplicar un tratamiento que reduce los microbios en su superficie", "Pintarlo de otro color", "Guardarlo en una caja", "Sanitizar reduce los microbios que pueden contaminar el vino."),
        ("abc", "En la bodega de vinificación: ¿qué puede indicar una vibración fuerte en una máquina?", "Una posible falla", "Que funciona mejor", "Que está limpia", "La vibración fuerte señala una posible falla."),
        ("abc", "{F} ¿A qué categoría corresponde Q1, la despalilladora con ruido metálico y vibración?", "A, no usar y avisar de inmediato", "B, retirar o programar", "C, conforme", "El ruido metálico indica riesgo de falla grave."),
        ("abc", "{F} ¿A qué categoría corresponde Q2, el refractómetro con error de 1 °Brix?", "B, retirar hasta calibrar", "A, no usar y avisar de inmediato", "C, conforme", "Está fuera de tolerancia, pero no hay emergencia."),
        ("abc", "{F} ¿A qué categoría corresponde Q3, la bomba normal con mangueras limpias?", "C, conforme", "A, no usar", "B, retirar", "Funciona como se espera, sin ruidos ni fallas visibles."),
        ("abc", "{F} ¿A qué categoría corresponde Q4, la prensa con fuga de aceite hidráulico?", "A, no usar y avisar de inmediato", "B, programar limpieza", "C, conforme", "La fuga puede indicar una falla grave."),
        ("abc", "{F} ¿A qué categoría corresponde Q5, las mangueras con restos sin limpiar?", "B, limpiar y sanitizar antes de usar", "A, no usar y avisar de inmediato", "C, conforme", "Es un problema de higiene que se corrige antes de usar."),
        ("=", "{F} Si la bodega verifica 5 equipos y 2 quedan en categoría A, ¿cuántos quedan sin categoría A?", "5-2", "Se restan los equipos de categoría A al total.", " equipos"),
        ("abc", "{F} Un operario dice: «la prensa gotea poco aceite, la uso igual esta vendimia». ¿Qué respuesta es correcta?", "Es peligroso: se detiene y se avisa, y lo revisa personal autorizado", "Es correcto, si gotea poco", "Es correcto, si limpia el aceite", "Una fuga puede crecer y causar un accidente."),
        ("abc", "{F} El jefe de bodega quiere anotar «conforme» para Q5, sin que se limpien las mangueras, «para cumplir la verificación». ¿Qué corresponde?", "Rechazarlo: no se anota lo que no se hizo", "Aceptarlo, para ganar tiempo", "Aceptarlo, si el vino las limpia", "Anotar conforme algo sin limpiar falsea el registro."),
        ("abc", "{F} La despalilladora vibra fuerte y de pronto suelta una pieza hacia las personas. ¿Qué corresponde a quien lo ve?", "Alejarse de la zona de riesgo y avisar a un adulto responsable y a emergencias", "Acercarse a apagarla", "Recoger la pieza", "Una pieza proyectada puede lesionar; se avisa a quienes pueden actuar."),
        ("abc", "En la bodega de vinificación: ¿por qué la categoría A tiene prioridad sobre la B?", "Porque hay riesgo inmediato de falla grave o accidente", "Porque es más barata de resolver", "Porque no necesita registro", "El riesgo inmediato se atiende primero."),
    ],
    ctx=("abc", "Un conocido te describe un ruido metálico en su despalilladora y te pregunta si puede usarla en la vendimia. ¿Qué respondes?", "Que deje de usarla y llame a un mecánico autorizado", "Que la use con cuidado", "Que la abra para mirar", "Una máquina con ruido metálico puede romperse y causar un accidente."),
    sc=[
        ("En la bodega de vinificación: ¿qué categoría tiene una fuga de aceite en la prensa?", "A, no usar y avisar de inmediato", "La fuga puede indicar una falla grave."),
        ("En la bodega de vinificación: ¿qué se hace con un utensilio sucio?", "Se limpia y sanitiza antes de usarlo", "Lo que toca el vino debe estar limpio."),
        ("En la bodega de vinificación: ¿quién repara o calibra?", "El mecánico autorizado", "Reparar y calibrar exige formación y autorización."),
    ],
    op=("Resultados de ejemplo de la «Bodega Demo 4»: R1, la bomba hace chispas y huele a quemado; R2, el termómetro marca 2 grados sobre el patrón con tolerancia de 1; R3, la filtradora funciona normal y limpia; R4, los baldes tienen restos de vino del año anterior. Categorías: A, no usar y avisar; B, retirar o limpiar; C, conforme. Escribe (a) la categoría de R1 a R4, (b) cuánto excede R2 la tolerancia, (c) quién calibra el termómetro, (d) qué haces si ves chispas.",
        "(a) R1: A; R2: B; R3: C; R4: B. (b) 2 − 1 = 1 grado. (c) El mecánico autorizado. (d) Me alejo, aviso a un adulto responsable y a emergencias.",
        ["clasifica bien los cuatro resultados", "calcula el exceso", "nombra quién calibra", "se aleja y avisa"],
        ["hoja con las cuatro respuestas"],
        ["clasificar las chispas como normales", "proponer reparar por cuenta propia"],
        "Pregunta: «¿qué resultado tiene riesgo inmediato?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Clasifica en A, B o C tres resultados inventados: humo en un motor, utensilio sucio y equipo normal.",
    extend="Explica con un ejemplo por qué una máquina que vibra no se sigue usando.",
)

# ============================================================ OAM-06, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Vendimia de la «Bodega Demo»: 300 horas de trabajo programadas. Sin verificación previa se esperan 40 horas de detención por fallas; con verificación previa se esperan 15. "
     "Cada hora detenida cuesta $80.000 en pérdidas de ejemplo. La verificación previa de todos los equipos cuesta $400.000. Un instrumento marca 2 grados sobre un patrón de 20.")
build(
    O6, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular la disponibilidad de los equipos, las pérdidas por detención y el ahorro de verificar antes de la vendimia.",
    prior=["Sé qué es verificar y calibrar.", "Sé calcular porcentajes enteros.", "Sé multiplicar y restar enteros."],
    explain=[
        "La disponibilidad es el porcentaje de las horas programadas en que los equipos están listos para trabajar: se calcula con las horas disponibles divididas por las programadas, por 100. Las horas disponibles son las programadas menos las horas de detención. Cada hora de detención durante la vendimia tiene un costo, porque la uva espera y se deteriora. La pérdida por detención es las horas detenidas por el costo de cada hora.",
        "Verificar antes de la vendimia tiene un costo, pero evita detenciones. El ahorro de verificar es la pérdida sin verificación, menos la pérdida con verificación, menos el costo de verificar. El error porcentual de un instrumento es el error dividido por el patrón, por 100. Los valores son de ejemplo y las decisiones las toman el jefe de bodega y el enólogo; calcular no reemplaza la verificación hecha por personal capacitado.",
        f"Ningún ahorro justifica usar un equipo con falla ni saltarse una verificación. {EMER} {AVISO}",
    ],
    vocab=[("disponibilidad", "porcentaje de las horas programadas en que los equipos están listos"), ("horas disponibles", "horas programadas menos horas de detención"), ("pérdida por detención", "horas detenidas por el costo de cada hora"), ("ahorro de verificar", "pérdida sin verificación menos pérdida con verificación, menos costo de verificar"), ("error porcentual", "error dividido por el patrón, por 100")],
    worked=[
        ("Disponibilidad", "En 200 horas programadas de ejemplo hubo 10 horas detenidas. ¿Cuál fue la disponibilidad?", ["Horas disponibles: 200 menos 10, o sea 190.", "190 de 200 es 95 por ciento."], "95 %"),
        ("Pérdida por detención", "Esas 10 horas de ejemplo cuestan $50.000 cada una. ¿Cuál es la pérdida?", ["Se multiplican las horas por el costo de cada una.", "10 por 50.000."], "$500.000"),
    ],
    mistakes=[("Calcular la disponibilidad dividiendo entre las horas detenidas.", "Debe dividirse entre las horas programadas.", "Disponibilidad es horas disponibles entre horas programadas."),
              ("Saltarse la verificación para ahorrar su costo.", "Las detenciones suelen costar más.", "Se compara el costo con la pérdida que evita.")],
    T=[
        ("abc", "En la bodega de vinificación: ¿qué es la disponibilidad de los equipos?", "El porcentaje de las horas programadas en que están listos", "El número de equipos que tiene la bodega", "El precio de los equipos", "La disponibilidad relaciona horas disponibles y programadas."),
        ("abc", "En la bodega de vinificación: ¿por qué una detención en plena vendimia es costosa?", "Porque la uva espera y se deteriora mientras el proceso está detenido", "Porque la uva pesa más", "Porque los equipos se enfrían", "La espera deteriora la uva que ya fue cosechada."),
        ("abc", "En la bodega de vinificación: ¿qué es el error porcentual de un instrumento?", "El error dividido por el patrón, por 100", "El patrón dividido por el error", "La tolerancia por 100", "El error porcentual compara el error con el patrón."),
        ("=", "{F} ¿Cuántas horas disponibles hay en la vendimia sin verificación previa?", "300-40", "Se restan las horas de detención a las horas programadas.", " horas"),
        ("=", "{F} ¿Cuántas horas disponibles hay con verificación previa?", "300-15", "Se restan las horas de detención a las horas programadas.", " horas"),
        ("=", "{F} ¿Cuál es la pérdida por detención sin verificación previa?", "40*80000", "Se multiplican las horas detenidas por el costo de cada hora.", " pesos"),
        ("=", "{F} ¿Cuál es la pérdida por detención con verificación previa?", "15*80000", "Se multiplican las horas detenidas por el costo de cada hora.", " pesos"),
        ("=", "{F} ¿Cuánto se ahorra al verificar, descontando el costo de la verificación?", "40*80000-15*80000-400000", "Se resta la pérdida con verificación y el costo de verificar a la pérdida sin verificación.", " pesos"),
        ("=", "{F} ¿Cuál es el error porcentual del instrumento?", "2*100//20", "Se divide el error entre el patrón y se multiplica por 100.", " %"),
        ("abc", "{F} Un jefe propone saltarse la verificación previa para ahorrar $400.000. ¿Qué corresponde?", "Rechazarlo: la detención sin verificar cuesta más y puede ser peligrosa", "Aceptarlo, para ahorrar", "Aceptarlo, si los equipos son nuevos", "Con estos números, verificar ahorra más de lo que cuesta."),
        ("abc", "{F} Una estudiante quiere calibrar el instrumento porque ya calculó su error. ¿Qué corresponde?", "Rechazarlo: la calibración la hace personal autorizado", "Aceptarlo, si usa un patrón", "Aceptarlo, si el error es pequeño", "Calcular el error no habilita para calibrar."),
        ("=", "{F} ¿Cuál es la disponibilidad con verificación previa, en porcentaje de las 300 horas?", "(300-15)*100//300", "Se dividen las horas disponibles entre las programadas y se multiplica por 100.", " %"),
        ("abc", "En la bodega de vinificación: ¿por qué conviene verificar los equipos antes de la vendimia y no durante?", "Porque durante la vendimia una falla detiene el proceso con la uva esperando", "Porque durante la vendimia no hay equipos", "Porque verificar es más barato en la vendimia", "Anticiparse evita detenciones críticas durante la vendimia."),
    ],
    ctx=("abc", "Un conocido te pregunta si vale la pena verificar sus equipos antes de la vendimia y te da solo el costo de la verificación. ¿Qué respondes?", "Que faltan las pérdidas esperadas por detención, y que decide con su jefe de bodega y su mecánico", "Que sí, siempre", "Que no, nunca", "Sin pérdidas esperadas no se puede comparar."),
    sc=[
        ("En la bodega de vinificación: ¿cómo se calcula la disponibilidad?", "Horas disponibles entre horas programadas, por 100", "La disponibilidad es un porcentaje de las horas programadas."),
        ("En la bodega de vinificación: ¿cómo se calcula la pérdida por detención?", "Horas detenidas por el costo de cada hora", "El costo se multiplica por las horas detenidas."),
        ("En la bodega de vinificación: ¿qué compara el ahorro de verificar?", "La pérdida evitada y el costo de verificar", "Si lo evitado supera el costo, conviene."),
    ],
    op=("Datos de ejemplo de la «Bodega Demo 5»: 200 horas programadas; sin verificación se esperan 24 horas detenidas y con verificación 6; cada hora detenida cuesta $60.000; verificar cuesta $300.000; un termómetro marca 12 con un patrón de 10. Escribe (a) la pérdida sin verificación, (b) la pérdida con verificación, (c) el ahorro de verificar, (d) el error porcentual del termómetro.",
        "(a) 24 × 60.000 = $1.440.000. (b) 6 × 60.000 = $360.000. (c) 1.440.000 − 360.000 − 300.000 = $780.000. (d) 2 × 100 ÷ 10 = 20 %.",
        ["calcula la pérdida sin verificación", "calcula la pérdida con verificación", "calcula el ahorro", "calcula el error porcentual"],
        ["hoja con las cuatro respuestas"],
        ["no restar el costo de verificar", "dividir entre el error"],
        "Pregunta: «¿qué se multiplica por el costo de cada hora?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula la disponibilidad de 400 horas programadas con 20 horas detenidas.",
    extend="Explica con un ejemplo por qué una detención en plena vendimia cuesta más que una en otro momento.",
)
