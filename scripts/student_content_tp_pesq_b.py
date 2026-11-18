"""Pesquería TP 3.º y 4.º medio: OAE-03 (registro de datos pesqueros), OAE-04 (conservación y calidad) y OAE-05 (seguridad y supervivencia, solo conceptos). Todo con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_pesq_common import AVISO, EMER, build

O3 = "TP-PESQ-3y4-OAE-03"
O4 = "TP-PESQ-3y4-OAE-04"
O5 = "TP-PESQ-3y4-OAE-05"

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). En el muelle de «Caleta Demo», una encargada anota el desembarque de 12 embarcaciones ficticias en una planilla con nombre del patrón, número de identificación (dato personal), especie, kilos y hora. "
     "Peligros anotados: piso mojado, un winche de descarga en movimiento junto al lugar de anotación, carretillas que cruzan el paso, poca luz al atardecer y la presión de un comprador para «redondear» los kilos. Regla de ejemplo: cada encargado anota hasta 4 embarcaciones por turno.")
build(
    O3, 1, F,
    use="Aprenderé para qué se registran datos pesqueros, qué son la investigación pesquera y las obligaciones pesqueras, y cómo se cuidan la veracidad, la privacidad y la seguridad al anotar.",
    prior=["Sé qué son un registro y una bitácora.", "Sé qué son peligro, riesgo y jerarquía de controles.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Un dato es un hecho medido o anotado, como los kilos de una captura. La investigación pesquera es el estudio de los recursos para conocer su estado y apoyar decisiones de cuidado. Las obligaciones pesqueras son los deberes que la norma vigente establece de informar capturas y desembarques a la autoridad pesquera. Los datos que se anotan hoy sirven después para fijar medidas como cuotas, vedas y tallas mínimas.",
        "Por eso los datos deben ser veraces: un dato falso distorsiona decisiones que afectan a toda una caleta. Algunas planillas incluyen datos personales, que son información que identifica a una persona, como su nombre o su número de identificación; se comparten solo con quien corresponde y no se publican. Si alguien presiona para cambiar un dato, se anota el dato real y se avisa a un adulto responsable.",
        f"Anotar datos en un muelle también tiene peligros: piso mojado, equipos de descarga en movimiento, carretillas y poca luz. Se controlan con la jerarquía de controles: puestos fijos y barreras, reglas de turno y, al final, el EPP. {EMER} {AVISO}",
    ],
    vocab=[("dato", "hecho medido o anotado"), ("investigación pesquera", "estudio de los recursos para conocer su estado y apoyar decisiones de cuidado"), ("obligaciones pesqueras", "deberes de informar capturas y desembarques que fija la norma vigente"), ("autoridad pesquera", "institución que recibe la información y fiscaliza la actividad pesquera"), ("veracidad", "cualidad de un dato que refleja lo realmente ocurrido"), ("dato personal", "información que identifica a una persona"), ("planilla", "tabla escrita donde se anotan datos por filas y columnas")],
    worked=[
        ("Peligro y riesgo", "En un muelle de ejemplo hay una grúa de descarga que gira sobre el paso de las personas. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la grúa que gira sobre el paso.", "El riesgo es que una persona sea golpeada por el equipo o su carga."], "Peligro: la grúa que gira sobre el paso; riesgo: que alguien sea golpeado"),
        ("Distribuir turnos", "Una planilla de ejemplo tiene 8 anotaciones y se reparte por igual entre 2 encargados. ¿Cuántas anota cada uno?", ["Se divide el total entre las personas.", "8 dividido en 2 es 4."], "4 anotaciones"),
    ],
    mistakes=[("Redondear los kilos para no discutir con el comprador.", "Un dato alterado, aunque sea poco, deja de ser veraz y distorsiona las decisiones.", "Se anota el dato real y se avisa a un adulto responsable si hay presión."),
              ("Publicar la planilla completa con los números de identificación para ser «transparente».", "Los datos personales se protegen y se comparten solo con quien corresponde.", "Se publican los totales y se reservan los datos personales.")],
    T=[
        ("abc", "En Pesquería: ¿para qué sirve la investigación pesquera?", "Para conocer el estado de los recursos y apoyar decisiones de cuidado", "Para fijar el precio de venta de cada especie", "Para decidir qué embarcación sale primero", "La investigación estudia el estado de los recursos; el precio y los turnos son otros temas."),
        ("abc", "En Pesquería: ¿qué son las obligaciones pesqueras de información?", "Deberes que la norma vigente fija para informar capturas y desembarques a la autoridad pesquera", "Acuerdos privados entre compradores y vendedores", "Recomendaciones voluntarias de cada organización", "Son deberes establecidos por la norma, no acuerdos ni recomendaciones."),
        ("abc", "En Pesquería: ¿qué es un dato personal en una planilla?", "Una información que identifica a una persona, como su nombre o su número de identificación", "Cualquier cifra de kilos", "El nombre de una especie", "Los datos personales identifican a alguien; los kilos y las especies no."),
        ("=", "{F} ¿Cuántos turnos de anotación se necesitan para las 12 embarcaciones?", "12//4", "Se divide el total de embarcaciones entre las que anota cada encargado.", " turnos"),
        ("abc", "{F} ¿Qué control de ingeniería corresponde para el winche junto al lugar de anotación?", "Un puesto de anotación fijo y con barrera, fuera del paso del winche y de las carretillas", "Un cartel que diga «cuidado»", "Un chaleco reflectante para la encargada", "El puesto fijo cambia el lugar; el cartel es administrativo y el chaleco es EPP."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al winche en movimiento junto al puesto?", "Que una persona sea golpeada o atrapada por el equipo o por su carga", "El winche en movimiento mismo, que es la fuente del daño", "Que la planilla se moje y se borre", "El riesgo es la posibilidad de daño a una persona; el winche es el peligro."),
        ("abc", "{F} El comprador pide anotar 300 kg en lugar de 287 «para redondear». ¿Qué corresponde?", "Anotar el dato real y avisar a un adulto responsable si hay presión", "Anotar 300, porque la diferencia es pequeña", "Anotar 290 como punto medio", "El dato real se anota siempre; cualquier cambio lo vuelve falso."),
        ("abc", "{F} ¿Qué se hace con los números de identificación de la planilla?", "Se comparten solo con quien corresponde y no se publican", "Se publican en el muelle para dar transparencia", "Se envían a cualquier persona que los pida", "Los datos personales se protegen, aunque otros datos se informen."),
        ("abc", "En una visita de ejemplo al muelle, una carretilla atrapa a una persona contra una pared. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Empujar la carretilla para soltarla tú mismo", "Tirar de la persona para sacarla rápido", "Intervenir sin formación puede causar más daño; se avisa a quienes pueden actuar."),
        ("abc", "En Pesquería: ¿por qué un dato falso afecta a otras personas, además de a quien lo anota?", "Porque se usa para decidir cuotas y medidas de cuidado, y un dato falso las distorsiona", "Porque solo cambia la letra de la planilla", "Porque cambia el precio del combustible", "Los datos alimentan decisiones colectivas sobre el recurso."),
        ("abc", "{F} Para el peligro de la poca luz al atardecer, ¿qué medida de nivel más efectivo corresponde?", "Iluminación fija en el puesto de anotación, instalada por personal autorizado", "Otro recordatorio escrito en la pared", "Pedir a cada persona que lleve su propia linterna", "La iluminación fija es de ingeniería; el recordatorio es administrativo y la linterna es un elemento personal."),
        ("=", "{F} Si cada una de las 12 embarcaciones desembarca en promedio 85 kg, ¿cuántos kilos se esperan en total?", "12*85", "Se multiplica el número de embarcaciones por los kilos promedio.", " kg"),
        ("abc", "{F} Una estudiante dice: «leí la ficha, así que puedo ir sola al muelle a registrar desembarques». ¿Qué respuesta es correcta?", "Es falso: trabajar en un muelle exige formación, autorización y coordinación con personal autorizado", "Es cierto, si lleva la planilla", "Es cierto, si va con chaleco", "Leer una ficha no habilita para trabajar; la planilla y el chaleco tampoco."),
    ],
    ctx=("abc", "Un comprador te pide una copia de la planilla con los nombres y números de identificación de los pescadores. ¿Qué respondes?", "Que no puedes entregarla, porque contiene datos personales, y que lo consultarás con un adulto responsable", "Que sí, porque es información pública", "Que sí, pero solo si tapas los kilos", "Los datos personales se entregan solo a quien corresponde según la norma."),
    sc=[
        ("En Pesquería: ¿qué es un dato?", "Un hecho medido o anotado, como los kilos de una captura", "El dato es la unidad básica de un registro."),
        ("En Pesquería: ¿qué institución recibe la información de las obligaciones pesqueras?", "La autoridad pesquera", "La autoridad pesquera recibe y fiscaliza esa información."),
        ("En Pesquería: ¿qué haces si alguien presiona para cambiar un dato?", "Anotar el dato real y avisar a un adulto responsable", "El dato real se mantiene y se pide apoyo a un adulto."),
    ],
    op=("Caso de ejemplo: en un muelle ficticio se anotan 9 embarcaciones; cada encargado anota hasta 3 por turno. El lugar de anotación tiene piso mojado y está junto a un equipo de descarga. Una persona pide cambiar un dato para «cuadrar la cuota». Escribe (a) cuántos turnos se necesitan, (b) un peligro y su riesgo, (c) un control de ingeniería, (d) qué haces ante la petición de cambiar el dato.",
        "(a) 9 ÷ 3 = 3 turnos. (b) Peligro: el equipo de descarga junto al puesto; riesgo: que una persona sea golpeada. También sirve el piso mojado. (c) Un puesto de anotación fijo, con barrera y piso antideslizante, fuera del paso del equipo. (d) Anotar el dato real y avisar a un adulto responsable. La tarea la hace personal autorizado.",
        ["calcula los turnos", "distingue peligro y riesgo", "propone un control de ingeniería", "mantiene la veracidad del dato"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer solo el EPP", "ceder ante la petición de cambiar el dato"],
        "Pregunta: «¿qué control cambia el lugar y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el último párrafo."),
    reinforce="Escribe tres datos de una planilla inventada y marca cuál es un dato personal y cuál no.",
    extend="Explica con un ejemplo por qué un dato veraz de una caleta ayuda a cuidar el recurso de todas las caletas.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). Planilla de desembarque del día 1 en Caleta Demo: embarcación E1, especie A, 420 kg; embarcación E2, especie A, 360 kg; embarcación E3, especie B, 220 kg. "
     "La bitácora de pesca de E2 anota 380 kg. Planilla de muestreo de tallas de especie A: 6 ejemplares de 31, 34, 28, 36, 33 y 30 centímetros; talla mínima de ejemplo, 32 cm. "
     "La planilla de otro día deja vacío el campo «kilos» de una embarcación.")
build(
    O3, 2, F,
    use="Aprenderé el vocabulario de los datos pesqueros: tipos de variables, registros de captura, de desembarque y de muestreo, y los roles que los producen y los usan.",
    prior=["Sé qué es un dato y qué es una planilla.", "Sé calcular un promedio y un porcentaje con números enteros.", "Sé que los registros no se alteran."],
    explain=[
        "Los datos pesqueros se organizan en variables, que son características que se anotan en cada registro. Una variable categórica clasifica, como la especie o el arte de pesca. Una variable numérica se mide con un número y una unidad, como los kilos o los centímetros. Un promedio es la suma de los valores dividida por la cantidad de valores; por ejemplo, el promedio de 10, 20 y 30 es 20.",
        "Los documentos cumplen funciones distintas. La planilla de desembarque registra lo que llegó a puerto; la declaración de desembarque es el documento con que se informa a la autoridad, según la norma vigente; la bitácora de pesca registra la faena; la planilla de muestreo de tallas anota el tamaño de los ejemplares de una muestra. Comparar dos documentos del mismo dato es una conciliación.",
        f"Los roles también son distintos: el encargado de registro anota; el muestreador mide ejemplares de una muestra; el analista de datos revisa los datos y calcula resultados; la autoridad pesquera recibe la información. Si falta un dato, se anota «sin dato» y no se inventa. {EMER} {AVISO}",
    ],
    vocab=[("variable categórica", "característica que clasifica, como la especie"), ("variable numérica", "característica que se mide con un número y una unidad"), ("promedio", "suma de los valores dividida por la cantidad de valores"), ("planilla de desembarque", "registro de lo que llegó a puerto"), ("declaración de desembarque", "documento con que se informa lo desembarcado a la autoridad"), ("planilla de muestreo de tallas", "registro del tamaño de los ejemplares de una muestra"), ("analista de datos", "persona que revisa datos y calcula resultados"), ("muestreador", "persona que mide ejemplares de una muestra"), ("sin dato", "anotación que indica que el dato no se obtuvo")],
    worked=[
        ("Clasificar variables", "En una planilla de ejemplo se anotan «arte de pesca» y «horas de faena». ¿Cuál es categórica y cuál numérica?", ["El arte clasifica en tipos.", "Las horas se miden con un número y una unidad."], "Arte de pesca: categórica; horas de faena: numérica"),
        ("Calcular un promedio", "Una muestra de ejemplo tiene tres ejemplares de 20, 24 y 28 cm. ¿Cuál es el promedio?", ["La suma es 72.", "72 dividido en 3 es 24."], "24 cm"),
    ],
    mistakes=[("Creer que el promedio dice cuántos ejemplares están bajo la talla mínima.", "Un promedio resume, pero no indica cuántos valores quedan bajo un límite.", "Cuenta cada valor frente al límite."),
              ("Rellenar un campo vacío con el promedio de los otros datos.", "Un dato inventado deja de ser veraz.", "Se anota «sin dato» y se pide el dato real.")],
    T=[
        ("abc", "En Pesquería: ¿qué es una variable categórica?", "Una característica que clasifica, como la especie o el arte de pesca", "Una característica que siempre se mide en kilos", "Una característica que se calcula con una fórmula", "Las categóricas clasifican; las numéricas se miden con una unidad."),
        ("abc", "En Pesquería: ¿para qué sirve una planilla de muestreo de tallas?", "Para anotar el tamaño de los ejemplares de una muestra", "Para registrar el pago de la tripulación", "Para planificar una derrota", "Esa planilla registra tallas; el pago y la derrota se anotan en otros documentos."),
        ("abc", "En Pesquería: ¿qué es la declaración de desembarque?", "El documento con que se informa lo desembarcado a la autoridad, según la norma vigente", "El permiso para salir a pescar", "La lista de repuestos de una embarcación", "La declaración informa lo desembarcado; el permiso de salida es el zarpe."),
        ("=", "{F} ¿Cuántos kilos de especie A se desembarcaron el día 1 según la planilla de desembarque?", "420+360", "Se suman los kilos de las dos embarcaciones con especie A.", " kg"),
        ("=", "{F} ¿Cuántos kilos se desembarcaron en total el día 1?", "420+360+220", "Se suman los kilos de las tres embarcaciones.", " kg"),
        ("abc", "{F} ¿Qué tipo de variable es «kilos desembarcados»?", "Numérica, porque se mide con un número y una unidad", "Categórica, porque clasifica en tipos", "Ninguna, porque es solo un nombre", "Los kilos se miden con un número y una unidad."),
        ("=", "{F} ¿Qué porcentaje del total desembarcado el día 1 es especie A?", "(420+360)*100//(420+360+220)", "Se divide la especie A entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es el promedio de las tallas de la muestra, en centímetros?", "(31+34+28+36+33+30)//6", "Se suman las tallas y se divide entre el número de ejemplares.", " cm"),
        ("abc", "{F} ¿Cuántos ejemplares de la muestra están bajo la talla mínima de ejemplo?", "3 ejemplares", "2 ejemplares", "4 ejemplares", "Miden menos de 32 cm los de 31, 28 y 30 centímetros."),
        ("abc", "{F} Un compañero dice que las planillas de desembarque y de muestreo son lo mismo porque ambas tienen números. ¿Qué respuesta es correcta?", "Es falso: la de desembarque registra lo que llegó a puerto y la de muestreo registra tallas de una muestra", "Es cierto, porque ambas tienen números", "Es cierto, porque ambas las llena el patrón", "Cada documento tiene una función distinta aunque contenga números."),
        ("abc", "{F} Para E2, la planilla dice 360 kg y la bitácora de pesca dice 380 kg. ¿Qué corresponde?", "Conciliar: informar la diferencia con ambos documentos y aclararla sin cambiar los números", "Anotar 370 kg, el promedio de ambos", "Borrar la planilla y copiar la bitácora", "Una diferencia entre documentos se aclara con evidencia, no con un número inventado."),
        ("abc", "{F} Un compañero dice: «el promedio es 32 cm, igual a la talla mínima, así que ningún ejemplar está bajo talla». ¿Qué respuesta es correcta?", "Es falso: el promedio no indica cuántos están bajo la talla, y 3 de los 6 miden menos de 32 cm", "Es cierto: si el promedio iguala la talla mínima, todos cumplen", "Es cierto, porque solo importa el promedio", "El promedio resume los valores, pero no impide que algunos queden bajo el límite."),
        ("abc", "{F} Una compañera propone completar el campo «kilos» vacío con el promedio de las otras embarcaciones. ¿Qué corresponde?", "No inventar el dato: se pide el dato real y, si no existe, se anota «sin dato»", "Completarlo con el promedio para que el registro esté listo", "Dejarlo en cero", "Un dato inventado o un cero falso alteran el registro."),
    ],
    ctx=("abc", "Una persona te pide que escribas en una planilla de ejemplo kilos que no se pesaron, «para completar el día». ¿Qué respondes?", "Que no, porque no se inventan datos, y que lo consultarás con un adulto responsable", "Que sí, si los números parecen razonables", "Que sí, si después los corriges", "Inventar datos falsifica el registro, aunque parezcan razonables."),
    sc=[
        ("En Pesquería: ¿cómo se calcula un promedio?", "Se suman los valores y se divide entre la cantidad de valores", "El promedio resume un conjunto de valores."),
        ("En Pesquería: ¿qué es una variable numérica?", "Una característica que se mide con un número y una unidad", "Las variables numéricas se miden, como los kilos."),
        ("En Pesquería: ¿qué se anota si falta un dato?", "«Sin dato»", "No se inventa un dato que no se obtuvo."),
    ],
    op=("Documentos de ejemplo: planilla de desembarque: E4, especie A, 300 kg; E5, especie A, 500 kg; E6, especie B, 200 kg. Muestreo de tallas de especie A: 25, 27, 30, 28 y 30 cm, con talla mínima de ejemplo de 28 cm. Escribe (a) el total desembarcado y el porcentaje de especie A, (b) el promedio de tallas, (c) cuántos ejemplares están bajo la talla mínima, (d) una variable categórica y una numérica de la planilla.",
        "(a) 300 + 500 + 200 = 1.000 kg; la especie A es 800 kg, es decir, 80 %. (b) 25 + 27 + 30 + 28 + 30 = 140; 140 ÷ 5 = 28 cm. (c) Dos ejemplares, los de 25 y 27 cm, miden menos de 28 cm. (d) Categórica: la especie; numérica: los kilos. El promedio es igual a la talla mínima, pero hay ejemplares bajo ella.",
        ["calcula total y porcentaje", "calcula el promedio", "cuenta los ejemplares bajo la talla", "distingue variable categórica y numérica"],
        ["hoja con las cuatro respuestas"],
        ["decir que ninguno está bajo talla porque el promedio es 28", "olvidar dividir entre 5", "confundir la variable categórica con la numérica"],
        "Pregunta: «¿cuántos valores miden menos de 28?». Si no responde, pídele que revise uno por uno."),
    reinforce="Inventa una planilla de tres embarcaciones y calcula el total y el porcentaje de una especie.",
    extend="Explica con un ejemplo por qué dos muestras con el mismo promedio pueden tener distinta cantidad de ejemplares bajo la talla mínima.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (muestreo de ejemplo, inventado). Planilla de muestreo de tallas de especie A, en centímetros, 11 registros: 29, 33, 35, 32, 330, 27, 34, 30, 33, 35 y 32. "
     "Rango plausible de ejemplo para la especie A: de 10 a 60 cm. Talla mínima de ejemplo: 32 cm. Regla de ejemplo: si más de un 20 % de los ejemplares válidos está bajo la talla mínima, se informa a la organización y a la autoridad pesquera. "
     "Agrupación de ejemplo: rango 1, de 27 a 29 cm; rango 2, de 30 a 32 cm; rango 3, de 33 a 35 cm.")
build(
    O3, 3, F,
    use="Aprenderé a analizar una planilla de muestreo: detectar un valor atípico, agruparlo en una tabla de frecuencias, calcular porcentajes y decidir qué se informa.",
    prior=["Sé calcular un promedio y un porcentaje con números enteros.", "Sé qué es la talla mínima y una muestra.", "Sé que los registros no se alteran."],
    explain=[
        "Un valor atípico es un dato que se aleja mucho de los demás. Puede ser un error de digitación, es decir, una equivocación al anotar o pasar el dato, o un hecho real raro. No se decide a ojo ni se corrige por intuición: se compara con un rango plausible, que es el intervalo de valores razonables para esa especie, se marca y se verifica con la planilla original. Mientras tanto, no se usa en los cálculos.",
        "Una tabla de frecuencias agrupa los datos en rangos y cuenta cuántos hay en cada uno; esa cuenta se llama frecuencia. Con los datos válidos se calculan el promedio, la frecuencia de cada rango y el porcentaje bajo talla. Por ejemplo, si de 8 ejemplares válidos 2 están bajo la talla mínima, el porcentaje es 25 %. Si pasa del límite de la regla, se informa.",
        f"Analizar estos datos es tarea de personas formadas, con la norma vigente; aquí se practica solo en papel. Tampoco se «arregla» un dato para que la muestra se vea mejor. {EMER} {AVISO}",
    ],
    vocab=[("valor atípico", "dato que se aleja mucho de los demás"), ("error de digitación", "equivocación al anotar o pasar un dato"), ("rango plausible", "intervalo de valores razonables para una especie"), ("tabla de frecuencias", "tabla que agrupa datos en rangos y cuenta cuántos hay en cada uno"), ("frecuencia", "cantidad de datos en un rango"), ("datos válidos", "datos que están dentro del rango plausible o fueron verificados")],
    worked=[
        ("Detectar un atípico", "Una muestra de ejemplo de otra especie tiene un rango plausible de 20 a 50 cm y un registro de 5 cm. ¿Qué corresponde?", ["5 está fuera del rango plausible.", "Se marca el dato y se verifica con la planilla original antes de usarlo."], "Marcarlo y verificarlo; no usarlo ni corregirlo a ojo"),
        ("Contar frecuencias", "Una muestra de ejemplo tiene tallas 21, 22, 25, 26 y 27, y los rangos son 21–23 y 24–27. ¿Cuántos hay en cada rango?", ["En el primer rango están 21 y 22.", "En el segundo están 25, 26 y 27."], "Primer rango: 2; segundo rango: 3"),
    ],
    mistakes=[("Cambiar un valor atípico por el que «parece correcto» sin mirar la planilla original.", "Corregir por intuición puede introducir un error nuevo.", "Se marca el valor, se verifica con la fuente y se anota la verificación."),
              ("Borrar un dato atípico para que el promedio se vea mejor.", "Eliminarlo sin verificar altera la muestra.", "Se excluye de los cálculos solo mientras se verifica y se deja anotado.")],
    T=[
        ("abc", "En Pesquería: ¿qué es un valor atípico en una planilla de muestreo?", "Un dato que se aleja mucho de los demás", "El dato que más se repite", "El primer dato anotado", "Lo atípico es lo que se aleja del resto; lo más repetido y el primero no tienen esa característica."),
        ("abc", "En Pesquería: ¿qué es una tabla de frecuencias?", "Una tabla que agrupa datos en rangos y cuenta cuántos hay en cada uno", "Una lista de precios por kilo", "Un horario de turnos de anotación", "La tabla de frecuencias cuenta datos por rango."),
        ("abc", "En Pesquería: ¿qué es un error de digitación?", "Una equivocación al anotar o pasar un dato", "Una captura que supera la cuota", "Un ejemplar bajo la talla mínima", "El error de digitación es de anotación, no de captura ni de tamaño."),
        ("abc", "{F} ¿Qué registro de la planilla es sospechoso?", "El de 330 cm, porque queda fuera del rango plausible", "El de 27 cm, porque es el menor", "El de 35 cm, porque se repite", "330 está fuera del rango de 10 a 60 cm; 27 y 35 están dentro."),
        ("=", "{F} ¿Cuántos centímetros suman los 10 registros válidos de la muestra?", "27+29+30+32+32+33+33+34+35+35", "Se suman los diez valores que están dentro del rango plausible.", " cm"),
        ("=", "{F} ¿Cuál es el promedio de los 10 registros válidos, en centímetros?", "(27+29+30+32+32+33+33+34+35+35)//10", "Se divide la suma de los valores válidos entre diez.", " cm"),
        ("abc", "{F} ¿Qué rango tiene más ejemplares?", "El rango 3, de 33 a 35 cm, con 5 ejemplares", "El rango 2, de 30 a 32 cm, con 3 ejemplares", "El rango 1, de 27 a 29 cm, con 2 ejemplares", "En el rango 3 están 33, 33, 34, 35 y 35."),
        ("=", "{F} ¿Qué porcentaje de los ejemplares válidos está bajo la talla mínima?", "3*100//10", "Se multiplican por 100 los 3 ejemplares bajo talla y se divide entre los 10 válidos.", " %"),
        ("abc", "{F} ¿Qué corresponde hacer con el registro de 330 cm?", "Marcarlo, no usarlo en los cálculos y verificarlo con la planilla original", "Borrarlo de la planilla", "Cambiarlo a 33 porque es lo más probable", "El valor se verifica con la fuente; borrar o corregir a ojo altera el registro."),
        ("abc", "{F} Si se incluyera el 330 en el cálculo del promedio, ¿qué pasaría?", "El promedio subiría mucho y dejaría de representar a la muestra", "El promedio no cambiaría, porque es un solo dato", "El promedio bajaría", "Un valor muy grande aumenta el promedio y lo aleja de los demás datos."),
        ("abc", "{F} Con el porcentaje bajo talla calculado y la regla de ejemplo, ¿qué corresponde?", "Informar a la organización y a la autoridad pesquera, porque supera el 20 %", "No informar, porque el promedio es 32 cm y cumple la talla", "Esperar otra muestra antes de informar", "La regla se aplica al porcentaje bajo talla, no al promedio."),
        ("=", "{F} Si la planilla original confirma que el registro de 330 era en realidad 32, ¿cuál es el promedio de los 11 registros?", "(27+29+30+32+32+33+33+34+35+35+32)//11", "Se suman los 11 valores con la corrección verificada y se divide entre 11.", " cm"),
        ("abc", "{F} Un compañero dice que 330 cm es posible porque «algunos peces crecen mucho». ¿Qué respuesta es correcta?", "Según el rango de la ficha está fuera de lo plausible, así que se verifica con la planilla original antes de usarlo", "Es posible, así que se usa sin verificar", "Se descarta para siempre y se borra del registro", "Un dato fuera del rango plausible se verifica, no se acepta ni se borra a ciegas."),
    ],
    ctx=("abc", "Un amigo te propone «limpiar» una planilla de ejemplo borrando los datos que bajan el promedio. ¿Qué respondes?", "Que no, porque un dato solo se excluye tras verificarlo y dejando constancia, y que lo consultarás con un adulto responsable", "Que sí, si el promedio queda más bonito", "Que sí, porque son pocos datos", "Borrar datos para mejorar un promedio es falsear la muestra."),
    sc=[
        ("En Pesquería: ¿qué es un rango plausible?", "El intervalo de valores razonables para una especie", "El rango plausible permite detectar datos sospechosos."),
        ("En Pesquería: ¿qué se hace primero con un valor atípico?", "Se marca y se verifica con la planilla original", "La verificación evita errores y alteraciones."),
        ("En Pesquería: ¿qué es la frecuencia de un rango?", "La cantidad de datos que hay en ese rango", "La frecuencia cuenta cuántos datos caen en cada rango."),
    ],
    op=("Muestreo de ejemplo de especie B, en centímetros: 41, 44, 39, 450, 43, 40, 38, 43, 42, 39, 41. Rango plausible de ejemplo: 20 a 60 cm. Talla mínima de ejemplo: 40 cm. Regla de ejemplo: informar si más de un 20 % de los válidos está bajo la talla. Escribe (a) el valor sospechoso y qué haces con él, (b) el promedio de los 10 válidos, (c) el porcentaje bajo talla, (d) si corresponde informar.",
        "(a) 450 cm, fuera del rango plausible: se marca, no se usa en los cálculos y se verifica con la planilla original. (b) 41 + 44 + 39 + 43 + 40 + 38 + 43 + 42 + 39 + 41 = 410; 410 ÷ 10 = 41 cm. (c) Bajo 40 cm están 39, 38 y 39: 3 de 10, es decir, 30 %. (d) Sí, supera el 20 %: se informa a la organización y a la autoridad pesquera.",
        ["detecta el valor atípico y actúa bien", "calcula el promedio válido", "calcula el porcentaje bajo talla", "decide si se informa"],
        ["hoja con las cuatro respuestas"],
        ["incluir el 450 en el promedio", "decidir con el promedio y no con el porcentaje", "borrar el dato sospechoso"],
        "Pregunta: «¿qué valor queda fuera del rango plausible?». Si no responde, pídele que compare cada dato con 20 y 60."),
    reinforce="Inventa una muestra de diez tallas con un valor sospechoso y arma la tabla de frecuencias por rangos.",
    extend="Explica por qué un valor sospechoso se verifica en la planilla original antes de corregirlo.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (serie de ejemplo, inventada). «Lancha Demo», especie A, cuatro meses. Mes 1: 1.800 kg en 60 horas de faena. Mes 2: 2.700 kg en 60 horas. Mes 3: 2.100 kg en 70 horas. Mes 4: 1.200 kg en 40 horas. "
     "Meta de ejemplo: CPUE de al menos 35 kg por hora. La planilla de desembarque suma 2.010 kg para el mes 3.")
build(
    O3, 4, F,
    use="Aprenderé a consolidar datos mensuales, a calcular CPUE y variación porcentual, a leer una tendencia y a informar diferencias sin alterar los registros.",
    prior=["Sé calcular la CPUE y un porcentaje.", "Sé qué es una conciliación.", "Sé leer una tabla escrita."],
    explain=[
        "Consolidar datos es reunir registros de varias fechas o fuentes en una sola tabla con totales. Con los datos de varios meses se puede estudiar la tendencia, que es el comportamiento general: si los valores suben, bajan o se mantienen. La variación porcentual es el cambio entre dos valores expresado como porcentaje del valor inicial: (final − inicial) × 100 ÷ inicial.",
        "La CPUE mensual se calcula dividiendo la captura del mes entre las horas de faena de ese mes. Para explicar un cambio hay que distinguir si fue por la captura, por las horas trabajadas o por ambos. Una causa probable es una explicación posible que se debe comprobar con la bitácora de pesca, la zona, el arte y las condiciones del mar; un dato aislado no la prueba. Por ejemplo, de 400 a 500 kg la variación es de 25 %.",
        f"Si dos fuentes no coinciden, se concilian: se informa la diferencia con ambos documentos y no se cambia ninguno. Estas cifras son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("consolidar", "reunir registros en una sola tabla con totales"), ("tendencia", "comportamiento general de los datos en el tiempo"), ("variación porcentual", "cambio entre dos valores como porcentaje del valor inicial"), ("CPUE mensual", "captura del mes dividida por las horas de faena del mes"), ("causa probable", "explicación posible que hay que comprobar")],
    worked=[
        ("Calcular una variación", "Una captura de ejemplo pasa de 500 kg en el mes 1 a 600 kg en el mes 2. ¿Cuál es la variación porcentual?", ["La diferencia es 100 kg.", "100 por 100 dividido entre 500 es 20."], "20 % de aumento"),
        ("Leer una tendencia", "Las CPUE de ejemplo de cuatro meses son 30, 28, 25 y 22. ¿Cuál es la tendencia?", ["Cada valor es menor que el anterior.", "La serie baja mes a mes."], "Tendencia a la baja"),
    ],
    mistakes=[("Concluir que el recurso disminuyó porque un mes se capturó menos.", "Capturar menos puede deberse a menos horas de faena, no a menos recurso.", "Compara la CPUE y no solo los kilos."),
              ("Cambiar una cifra para que dos fuentes coincidan.", "Alterar una fuente impide saber cuál era correcta.", "Se informa la diferencia y se aclara con una nota fechada.")],
    T=[
        ("abc", "En Pesquería: ¿qué significa consolidar los datos de varios meses?", "Reunirlos en una sola tabla con totales", "Borrar los registros más antiguos", "Cambiar las unidades de kilos a litros", "Consolidar es reunir y totalizar, no borrar ni cambiar unidades."),
        ("abc", "En Pesquería: ¿qué es una variación porcentual entre dos meses?", "El cambio entre los dos valores expresado como porcentaje del valor inicial", "La diferencia entre el valor más alto y el más bajo del año", "El promedio de los dos valores", "La variación compara el cambio con el valor inicial."),
        ("abc", "En Pesquería: ¿qué es la tendencia de una serie mensual?", "El comportamiento general de los datos: si suben, bajan o se mantienen", "El valor más alto de la serie", "La suma de todos los meses", "La tendencia describe el comportamiento general en el tiempo."),
        ("=", "{F} ¿Cuál es la CPUE del mes 1?", "1800//60", "Se divide la captura del mes entre las horas de faena.", " kg por hora"),
        ("=", "{F} ¿Cuál es la CPUE del mes 2?", "2700//60", "Se divide la captura del mes entre las horas de faena.", " kg por hora"),
        ("=", "{F} ¿Cuántos kilos suman los cuatro meses?", "1800+2700+2100+1200", "Se suman las capturas mensuales.", " kg"),
        ("=", "{F} ¿Cuál es la variación porcentual de la captura del mes 1 al mes 2?", "(2700-1800)*100//1800", "Se divide el cambio entre el valor inicial y se multiplica por 100.", " %"),
        ("abc", "{F} ¿En qué mes fue mayor la CPUE?", "En el mes 2", "En el mes 1", "En el mes 3", "La CPUE del mes 2 es 45, mayor que las de los otros meses."),
        ("abc", "{F} ¿Cuántos meses quedaron bajo la meta de CPUE?", "3 meses", "1 mes", "2 meses", "Los meses 1, 3 y 4 tienen CPUE de 30, 30 y 30, bajo la meta de 35."),
        ("abc", "{F} El mes 4 capturó menos kilos que el mes 1, pero con la misma CPUE. ¿Qué conclusión es correcta?", "Capturó menos porque se trabajó menos horas: la CPUE por hora no bajó", "El recurso disminuyó, porque se capturó menos", "Hubo un error de registro seguro", "Con igual CPUE y menos horas, la captura total baja sin que el rendimiento por hora cambie."),
        ("abc", "{F} ¿Qué datos ayudarían a explicar el aumento de CPUE del mes 2?", "La zona, el arte y las condiciones anotadas en la bitácora de pesca de ese mes", "El color de la lancha", "El nombre del encargado de la planilla", "Una causa probable se comprueba con datos de la faena."),
        ("=", "{F} Si en el mes 5 se trabajan 50 horas con la CPUE del mes 3, ¿cuántos kilos se esperan?", "50*(2100//70)", "Se multiplica la CPUE del mes 3 por las horas del mes 5.", " kg"),
        ("abc", "{F} Para el mes 3, el cuadro dice 2.100 kg y la planilla de desembarque suma 2.010 kg. ¿Qué corresponde?", "Informar la diferencia de 90 kg con ambos documentos y revisar si hubo un error de digitación al anotar, sin cambiar ninguna cifra", "Anotar 2.055 kg, el promedio", "Cambiar la planilla para que diga 2.100", "Una diferencia se concilia con evidencia; no se corrige por intuición."),
    ],
    ctx=("abc", "Un dirigente te pide que escribas un aumento del 50 % en un informe aunque el dato real sea menor, «para conseguir apoyo». ¿Qué respondes?", "Que no, porque los datos deben ser veraces, y que lo consultarás con un adulto responsable", "Que sí, porque ayuda a la caleta", "Que sí, pero solo un poco", "Un informe falso daña la confianza y las decisiones sobre el recurso."),
    sc=[
        ("En Pesquería: ¿cómo se calcula la variación porcentual?", "Cambio dividido por el valor inicial, por 100", "La variación se mide respecto del valor inicial."),
        ("En Pesquería: ¿cómo se calcula la CPUE mensual?", "Captura del mes dividida por las horas de faena", "La CPUE relaciona captura y esfuerzo del mes."),
        ("En Pesquería: ¿qué se hace con dos fuentes que no coinciden?", "Se informa la diferencia y no se cambia ninguna", "La conciliación se hace con evidencia."),
    ],
    op=("Serie de ejemplo de especie B: mes 1, 1.600 kg en 50 horas; mes 2, 2.000 kg en 50 horas; mes 3, 1.800 kg en 40 horas. Meta de ejemplo de CPUE: 40 kg por hora. Escribe (a) la CPUE de cada mes, (b) cuántos meses cumplen la meta, (c) la variación porcentual de la captura del mes 1 al mes 2, (d) una causa probable del cambio y cómo la comprobarías.",
        "(a) Mes 1: 1.600 ÷ 50 = 32; mes 2: 2.000 ÷ 50 = 40; mes 3: 1.800 ÷ 40 = 45 kg por hora. (b) Dos meses cumplen la meta: el 2 y el 3. (c) (2.000 − 1.600) × 100 ÷ 1.600 = 25 %. (d) Una causa probable es un cambio de zona o de condiciones del mar; se comprueba con la bitácora de pesca de cada mes, sin darla por segura.",
        ["calcula las CPUE", "cuenta los meses que cumplen", "calcula la variación", "propone una causa probable comprobable"],
        ["hoja con las cuatro respuestas"],
        ["usar kilos totales en vez de CPUE", "tomar la causa como segura", "dividir entre el valor final"],
        "Pregunta: «¿entre qué dato divides la captura para obtener la CPUE?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa tres meses de captura y horas, y calcula la CPUE y la variación entre el primero y el último.",
    extend="Explica por qué la CPUE ayuda a distinguir entre «se capturó menos» y «hay menos recurso».",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 5 (conciliación de ejemplo, inventada). Tres embarcaciones del día 1. E1: la bitácora de pesca anota 400 kg y la planilla de desembarque 404 kg. E2: bitácora 500 kg y planilla 450 kg. E3: bitácora 200 kg y planilla 198 kg. "
     "Tolerancia de ejemplo: una diferencia de hasta 5 % de la bitácora se acepta; sobre ese valor se investiga. Alternativa de registro R1: cuaderno libre sin columnas ni firma. Alternativa R2: planilla con campos fijos, fecha, hora, responsable y firma. "
     "En la fila de E4 el campo «kilos» está vacío.")
build(
    O3, 5, F,
    use="Aprenderé a verificar la calidad de datos con criterios de completitud, exactitud y trazabilidad, a conciliar fuentes con una tolerancia y a comparar alternativas de registro.",
    prior=["Sé qué es una conciliación y un registro veraz.", "Sé calcular un porcentaje con números enteros.", "Sé qué es la bitácora y la planilla de desembarque."],
    explain=[
        "La calidad de un dato se revisa con criterios. La completitud es que estén llenos todos los campos exigidos. La exactitud es que el dato coincida con la realidad y con otras fuentes. La oportunidad es que se anote a tiempo y la legibilidad, que se pueda leer sin dudas. La trazabilidad es que se sepa quién anotó el dato y cuándo.",
        "Al conciliar dos fuentes se calcula la diferencia y se compara con una tolerancia, que es la diferencia máxima aceptada antes de investigar. Por ejemplo, con una tolerancia de 10 %, una diferencia de 5 kg sobre 100 kg se acepta, y de 20 kg se investiga. Investigar es revisar ambos documentos e informar, no cambiar un número.",
        f"Al comparar formas de registrar se prefiere la que facilita estos criterios: campos fijos, fecha, hora, responsable y firma. Estos cálculos son de ejemplo y las tareas reales las hace personal formado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("completitud", "que estén llenos todos los campos exigidos"), ("exactitud", "que el dato coincida con la realidad y con otras fuentes"), ("oportunidad", "que el dato se anote a tiempo"), ("legibilidad", "que el dato se pueda leer sin dudas"), ("trazabilidad", "que se sepa quién anotó el dato y cuándo"), ("tolerancia", "diferencia máxima aceptada antes de investigar")],
    worked=[
        ("Aplicar una tolerancia", "Una bitácora de ejemplo anota 200 kg y la planilla 190 kg. La tolerancia de ejemplo es 8 %. ¿Se investiga?", ["La diferencia es 10 kg.", "10 por 100 dividido entre 200 es 5 %, menor que 8 %."], "No: está dentro de la tolerancia"),
        ("Clasificar un defecto", "Una fila de ejemplo tiene el campo «especie» vacío. ¿Qué criterio de calidad falla?", ["Falta un dato exigido.", "Eso es la completitud."], "Completitud"),
    ],
    mistakes=[("Elegir la forma de registro más rápida aunque no tenga firma ni fecha.", "Sin responsable ni fecha se pierde la trazabilidad.", "Prefiere la forma que facilita completitud, exactitud y trazabilidad."),
              ("Considerar que una diferencia dentro de la tolerancia puede borrarse de la planilla.", "La diferencia queda registrada; solo no se investiga.", "Se anota y se deja constancia.")],
    T=[
        ("abc", "En Pesquería: ¿qué mide la completitud de un registro?", "Que estén llenos todos los campos exigidos", "Que la letra sea clara", "Que los datos se anoten rápidamente", "La completitud se refiere a campos llenos; la letra es legibilidad."),
        ("abc", "En Pesquería: ¿qué mide la exactitud de un dato?", "Que coincida con la realidad y con otras fuentes", "Que el documento sea breve", "Que tenga muchas columnas", "La exactitud compara el dato con la realidad y con otros documentos."),
        ("abc", "En Pesquería: ¿qué es la tolerancia en una conciliación?", "La diferencia máxima aceptada antes de investigar", "La diferencia mínima que permite borrar un dato", "La suma de las dos fuentes", "La tolerancia fija cuándo una diferencia obliga a investigar."),
        ("=", "{F} ¿Cuántos kilos de diferencia hay en E1 entre la bitácora y la planilla?", "404-400", "Se resta el valor menor del mayor.", " kg"),
        ("=", "{F} ¿Qué porcentaje de la bitácora es la diferencia de E2?", "(500-450)*100//500", "Se divide la diferencia entre la bitácora y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué embarcación excede la tolerancia de ejemplo?", "E2, con 10 % de diferencia", "E1, con 1 % de diferencia", "E3, con 1 % de diferencia", "Solo E2 supera el 5 % de tolerancia."),
        ("=", "{F} ¿Qué porcentaje de la bitácora es la diferencia de E3?", "(200-198)*100//200", "Se divide la diferencia entre la bitácora y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos kilos anotan en total las bitácoras de las tres embarcaciones?", "400+500+200", "Se suman los kilos de las tres bitácoras.", " kg"),
        ("=", "{F} ¿Cuántos kilos de diferencia hay entre la suma de las bitácoras y la suma de las planillas?", "(400+500+200)-(404+450+198)", "Se restan las sumas de las planillas de la suma de las bitácoras.", " kg"),
        ("abc", "{F} ¿Qué criterio de calidad falla en la fila de E4 con el campo «kilos» vacío?", "La completitud", "La legibilidad", "La oportunidad", "Falta un dato exigido, y eso afecta la completitud."),
        ("abc", "{F} ¿Qué corresponde hacer con la diferencia de E2?", "Investigar con ambos documentos e informar, sin cambiar ningún número", "Anotar 475 kg, el promedio de ambas fuentes", "Usar la bitácora porque es más antigua", "La diferencia supera la tolerancia y se investiga con evidencia."),
        ("abc", "{F} ¿Qué alternativa de registro conviene y por qué?", "R2, porque sus campos fijos, fecha, responsable y firma facilitan la completitud y la trazabilidad", "R1, porque cada persona anota lo que quiere", "Ninguna, porque no hace falta registrar", "La alternativa con estructura permite verificar y asignar responsabilidad."),
        ("abc", "{F} Una compañera propone corregir la bitácora de E2 para que coincida con la planilla y «evitar problemas». ¿Qué respondes?", "Que no: un registro no se altera; se investiga la diferencia y se informa", "Que sí, si lo hace antes de la revisión", "Que sí, si cambia solo un número", "Cambiar una fuente oculta la causa de la diferencia."),
    ],
    ctx=("abc", "Alguien te pide anotar «sin diferencias» en un informe de ejemplo aunque una embarcación superó la tolerancia. ¿Qué respondes?", "Que no, porque el informe debe ser veraz, y que lo consultarás con un adulto responsable", "Que sí, porque la diferencia es solo de una embarcación", "Que sí, si lo corriges después", "Un informe que oculta una diferencia pierde su valor."),
    sc=[
        ("En Pesquería: ¿qué es la trazabilidad de un dato?", "Que se sepa quién lo anotó y cuándo", "La trazabilidad permite seguir el origen del dato."),
        ("En Pesquería: ¿qué se hace cuando una diferencia supera la tolerancia?", "Se investiga con ambos documentos y se informa", "Sobre la tolerancia, la diferencia se investiga."),
        ("En Pesquería: ¿qué forma de registro es mejor, con firma o sin firma?", "Con firma, fecha y responsable", "Esos campos aseguran que el registro tenga trazabilidad."),
    ],
    op=("Conciliación de ejemplo, tolerancia de ejemplo 5 %: E7, bitácora 300 kg y planilla 306 kg; E8, bitácora 400 kg y planilla 360 kg. En la fila de E9 falta el responsable. Escribe (a) la diferencia porcentual de cada embarcación, (b) cuál supera la tolerancia, (c) qué criterio falla en la fila de E9, (d) qué haces con la diferencia que supera la tolerancia.",
        "(a) E7: 6 × 100 ÷ 300 = 2 %; E8: 40 × 100 ÷ 400 = 10 %. (b) E8 supera la tolerancia de 5 %. (c) La trazabilidad, porque falta saber quién anotó el dato. (d) Se investiga con ambos documentos y se informa, sin cambiar ninguna cifra. Las tareas reales las hace personal formado y autorizado.",
        ["calcula las diferencias", "identifica la que supera la tolerancia", "nombra el criterio de calidad", "describe cómo se informa"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre la planilla en vez de la bitácora", "decir que se cambia la cifra", "confundir completitud con trazabilidad"],
        "Pregunta: «¿entre qué valor divides la diferencia?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa dos fuentes para tres embarcaciones y marca cuáles superan una tolerancia de 5 %.",
    extend="Explica con un ejemplo por qué la firma y la fecha de un registro ayudan a corregir un error sin alterar el dato.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La planta de acopio ficticia «Acopio Demo», en Caleta Demo, recibe especie A en cajas de 20 kg (dato de ejemplo), 18 cajas por turno. "
     "Peligros anotados: piso mojado y frío, cajas pesadas, una cámara fría con una puerta que no se puede abrir desde dentro y exposición prolongada al frío. "
     "Reglas de ejemplo: ninguna caja de más de 18 kg se mueve a mano (valor inventado solo para planilla, no es un límite legal); el carro de ejemplo admite 120 kg por viaje.")
build(
    O4, 1, F,
    use="Aprenderé qué son la calidad, el deterioro y la cadena de frío de los recursos del mar, qué institución fiscaliza lo sanitario y cómo se previenen los peligros de una planta de acopio.",
    prior=["Sé qué son peligro, riesgo y jerarquía de controles.", "Sé qué es un recurso hidrobiológico.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "La calidad de un producto del mar es el conjunto de características que lo hacen aceptable para el consumo: frescura, aspecto, temperatura e higiene. El deterioro es la pérdida de calidad con el paso del tiempo y con el calor. La cadena de frío es mantener una temperatura baja y continua desde la captura hasta el consumidor; si se interrumpe, el deterioro se acelera aunque después se vuelva a enfriar.",
        "La higiene es la limpieza de personas, superficies y equipos que evita la contaminación. La contaminación cruzada es el paso de gérmenes u otras sustancias desde un producto, una superficie o una persona a otro producto. La autoridad sanitaria es la institución que fiscaliza las condiciones sanitarias, según la norma vigente. Este cuaderno no enseña a manipular ni a procesar productos: solo los conceptos.",
        f"En una planta de acopio hay peligros: piso mojado y frío, cajas pesadas y cámaras frías. Se controlan con la jerarquía de controles: ayudas mecánicas y puertas con apertura interior, turnos limitados en el frío y, al final, el EPP, como la ropa térmica. {EMER} {AVISO}",
    ],
    vocab=[("calidad", "conjunto de características que hacen aceptable un producto"), ("deterioro", "pérdida de calidad con el tiempo y el calor"), ("cadena de frío", "mantención de una temperatura baja y continua desde la captura hasta el consumo"), ("higiene", "limpieza de personas, superficies y equipos para evitar la contaminación"), ("contaminación cruzada", "paso de gérmenes de un producto o superficie a otro"), ("autoridad sanitaria", "institución que fiscaliza las condiciones sanitarias"), ("ayuda mecánica", "equipo como un carro que evita levantar peso a mano")],
    worked=[
        ("Peligro y riesgo", "En una cámara fría de ejemplo, el piso tiene una capa de hielo en la entrada. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el hielo en el piso de la entrada.", "El riesgo es que una persona resbale y se lastime."], "Peligro: el hielo en el piso; riesgo: resbalar y lastimarse"),
        ("Contar viajes", "Una carga de ejemplo es de 360 kg y un carro admite 90 kg por viaje. ¿Cuántos viajes hacen falta?", ["Se divide la carga entre lo que admite cada viaje.", "360 dividido en 90 es 4."], "4 viajes"),
    ],
    mistakes=[("Creer que si el producto vuelve a enfriarse, la interrupción de la cadena de frío no importa.", "El deterioro ocurrido no se revierte al volver a enfriar.", "La cadena de frío debe ser continua."),
              ("Creer que leer sobre un producto del mar habilita para manipularlo o procesarlo.", "La manipulación exige formación, higiene y norma sanitaria vigente.", "Aprende aquí el concepto y deja la tarea a personal autorizado.")],
    T=[
        ("abc", "En Pesquería: ¿qué es la cadena de frío de un producto del mar?", "Mantener una temperatura baja y continua desde la captura hasta el consumidor", "Enfriar el producto solo al final del día", "Congelar todos los productos por igual", "La cadena de frío es continua; enfriar solo al final no la mantiene."),
        ("abc", "En Pesquería: ¿qué es el deterioro de un producto del mar?", "La pérdida de calidad con el tiempo y el calor", "El aumento de su peso por el hielo", "El cambio de una especie por otra", "El deterioro es pérdida de calidad, no un cambio de peso ni de especie."),
        ("abc", "En Pesquería: ¿qué es la contaminación cruzada?", "El paso de gérmenes de un producto, una superficie o una persona a otro producto", "El enfriamiento de un producto por otro", "El mezclado de especies en una misma planilla", "La contaminación cruzada es un traspaso de gérmenes, no de temperatura ni de registros."),
        ("=", "{F} ¿Cuántos kilos de producto recibe la planta en un turno?", "18*20", "Se multiplica el número de cajas por los kilos de cada una.", " kg"),
        ("=", "{F} ¿Cuántos viajes del carro de ejemplo hacen falta para mover los kilos de un turno?", "18*20//120", "Se divide la carga del turno entre lo que admite cada viaje.", " viajes"),
        ("abc", "{F} Una caja pesa 20 kg y la regla de ejemplo limita lo que se mueve a mano a 18 kg. ¿Qué corresponde?", "No levantarla a mano: se usa una ayuda mecánica, como un carro", "Levantarla despacio para que pese menos", "Levantarla con guantes", "La regla se cumple evitando el levante a mano, no cambiando la forma de levantar."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a la puerta de la cámara fría que no se abre desde dentro?", "Que una persona quede encerrada y expuesta al frío", "La puerta misma, cuando está cerrada", "Que el producto se enfríe de más", "El riesgo es la posibilidad de daño a una persona; la puerta es el peligro."),
        ("abc", "{F} ¿Qué control de ingeniería corresponde para esa puerta?", "Una manilla de apertura interior y una alarma, instaladas por personal autorizado", "Un cartel que diga «no cerrar la puerta»", "Ropa térmica para todo el personal", "Cambiar la puerta es de ingeniería; el cartel es administrativo y la ropa es EPP."),
        ("abc", "En una visita de ejemplo, alguien golpea desde dentro de una cámara fría y no puedes abrirla. ¿Qué corresponde según las reglas generales?", "No forzar la puerta, avisar de inmediato a un adulto responsable y a emergencias", "Forzar la puerta con una herramienta", "Esperar a que la persona salga por sí misma", "Forzar una puerta sin formación puede causar más daño; se avisa a quienes pueden actuar."),
        ("abc", "En Pesquería: ¿por qué la cadena de frío debe ser continua?", "Porque cada interrupción acelera el deterioro, aunque después se vuelva a enfriar", "Porque el frío solo importa en el momento de la venta", "Porque el hielo aumenta el peso del producto", "El daño por una interrupción no se revierte al volver a enfriar."),
        ("abc", "{F} Para el piso mojado y frío, ¿qué medida de nivel más efectivo se podría sumar a una regla escrita?", "Un piso antideslizante con drenaje, instalado por personal autorizado", "Otro letrero con la misma advertencia", "Pedir a cada persona que camine despacio", "El piso antideslizante cambia el lugar; el letrero y pedir cuidado son administrativos."),
        ("=", "{F} Si otro turno recibe 24 cajas de 20 kg, ¿cuántos kilos recibe la planta entre el turno de la ficha y ese turno?", "(18+24)*20", "Se suman las cajas de los dos turnos y se multiplica por los kilos de cada caja.", " kg"),
        ("abc", "{F} Una estudiante dice: «leí la ficha, así que puedo manipular y procesar productos en la planta». ¿Qué respuesta es correcta?", "Es falso: eso exige formación, higiene, autorización y norma sanitaria vigente", "Es cierto, si usa ropa limpia", "Es cierto, si trabaja con otra persona", "Leer una ficha no habilita para trabajar; la ropa limpia sola tampoco."),
    ],
    ctx=("abc", "Un conocido te ofrece ayudar un día en una planta de acopio, entrando solo a la cámara fría con la puerta cerrada. ¿Qué respondes?", "Que no, porque esa tarea exige formación, apertura interior en la puerta y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, porque el frío no es peligroso", "Que sí, si es por poco rato", "Un rato corto en una cámara cerrada igual implica riesgo sin las medidas de seguridad."),
    sc=[
        ("En Pesquería: ¿qué institución fiscaliza las condiciones sanitarias?", "La autoridad sanitaria", "La autoridad sanitaria fiscaliza lo sanitario según la norma."),
        ("En Pesquería: ¿qué es la calidad de un producto del mar?", "El conjunto de características que lo hacen aceptable para el consumo", "La calidad reúne frescura, aspecto, temperatura e higiene."),
        ("En pesquería: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
    ],
    op=("«Acopio Demo» anota una tarea de ejemplo: mover 12 cajas de 25 kg desde la cámara fría con el piso mojado. La regla de ejemplo (valor inventado) limita lo que se mueve a mano a 18 kg y el carro admite 100 kg por viaje. Escribe (a) cuántos kilos son y cuántos viajes del carro hacen falta, (b) un peligro y su riesgo, (c) un control de ingeniería, (d) por qué el EPP no basta y quién hace la tarea.",
        "(a) 12 × 25 = 300 kg; 300 ÷ 100 = 3 viajes. (b) Peligro: piso mojado; riesgo: que alguien resbale y se lastime. También sirven las cajas pesadas (riesgo de lesión por esfuerzo). (c) Un piso antideslizante con drenaje y una ayuda mecánica, instalados por personal autorizado. (d) El EPP es la última barrera: no quita el peligro; la tarea la hace personal autorizado.",
        ["calcula kilos y viajes", "distingue peligro y riesgo", "propone un control de ingeniería", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["levantar a mano pese a la regla", "llamar riesgo a la fuente del daño", "proponer solo el EPP"],
        "Pregunta: «¿qué control cambia el lugar y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el último párrafo."),
    reinforce="Escribe tres peligros de una planta de acopio inventada y, para cada uno, un control de un nivel distinto de la jerarquía.",
    extend="Explica con un ejemplo por qué una interrupción corta de la cadena de frío puede dañar la calidad.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). Acopio Demo, día 6. Lote L-1: ingreso el día 3, 200 kg. Lote L-2: ingreso el día 1, 150 kg. Lote L-3: ingreso el día 5, 250 kg. Vida útil de ejemplo: 6 días contados desde el ingreso. "
     "Rótulo de ejemplo del lote L-2: especie A; lote L-2; fecha de ingreso, día 1; temperatura de ingreso, 3 °C; responsable, encargado de calidad.")
build(
    O4, 2, F,
    use="Aprenderé los conceptos de lote, rótulo, vida útil y rotación PEPS, qué documentos respaldan la calidad de un producto y qué roles intervienen.",
    prior=["Sé qué son la calidad y la cadena de frío.", "Sé qué es la trazabilidad.", "Sé sumar, restar y multiplicar números enteros."],
    explain=[
        "Un lote es un grupo de producto de la misma especie y fecha de ingreso que se maneja junto. El rótulo es la etiqueta que lo identifica: especie, lote, fecha de ingreso, temperatura y responsable; sin él se pierde la trazabilidad. La vida útil es el tiempo durante el cual el producto conserva su calidad; el día de vencimiento es el de ingreso más la vida útil. Por ejemplo, un producto que ingresa el día 2 con vida útil de 4 días vence el día 6.",
        "La rotación PEPS, que significa primero en entrar, primero en salir, indica que sale primero el lote que ingresó antes, para que nada se deteriore en la bodega. Los documentos son: el registro de temperatura, donde se anotan las lecturas; la hoja de control de calidad, donde se revisa cada lote; y la guía de despacho, que acompaña la salida con cantidades, destino y lote.",
        f"Los roles son el encargado de calidad, que revisa los lotes y decide su destino; el personal de acopio, que ejecuta las labores autorizadas; y la autoridad sanitaria, que fiscaliza según la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("lote", "grupo de producto de la misma especie y fecha de ingreso que se maneja junto"), ("rótulo", "etiqueta que identifica un lote"), ("vida útil", "tiempo durante el cual el producto conserva su calidad"), ("día de vencimiento", "día de ingreso más la vida útil"), ("PEPS", "primero en entrar, primero en salir"), ("registro de temperatura", "documento con las lecturas de temperatura"), ("hoja de control de calidad", "documento donde se revisa cada lote"), ("guía de despacho", "documento que acompaña la salida con cantidades, destino y lote")],
    worked=[
        ("Día de vencimiento", "Un lote de ejemplo ingresa el día 4 y tiene una vida útil de 5 días. ¿Qué día vence?", ["El vencimiento es el día de ingreso más la vida útil.", "4 más 5 es 9."], "El día 9"),
        ("Aplicar PEPS", "Dos lotes de ejemplo ingresaron los días 2 y 7. ¿Cuál sale primero?", ["PEPS saca primero lo que entró antes.", "El día 2 es anterior al día 7."], "El lote que ingresó el día 2"),
    ],
    mistakes=[("Despachar primero el lote más nuevo porque «se ve más fresco».", "El lote más antiguo es el que antes pierde calidad.", "Aplica PEPS y despacha primero el lote más antiguo."),
              ("Quitar el rótulo de una caja para reutilizarla.", "Sin rótulo se pierde el origen, la fecha y el responsable.", "El rótulo se conserva mientras el producto esté en la caja.")],
    T=[
        ("abc", "En Pesquería: ¿qué es un lote de producto?", "Un grupo de producto de la misma especie y fecha de ingreso que se maneja junto", "Un documento que acompaña la salida del producto", "La temperatura máxima que acepta una cámara", "Un lote es el grupo de producto; el documento y la temperatura son otros conceptos."),
        ("abc", "En Pesquería: ¿qué información lleva el rótulo de un lote?", "Especie, lote, fecha de ingreso, temperatura y responsable", "El nombre del comprador y el precio de venta", "El horario de los turnos del personal", "El rótulo identifica el lote y permite la trazabilidad."),
        ("abc", "En Pesquería: ¿qué indica la rotación PEPS?", "Que sale primero el lote que ingresó antes", "Que sale primero el lote más nuevo", "Que sale primero el lote más pesado", "PEPS significa primero en entrar, primero en salir."),
        ("=", "{F} ¿Qué día vence el lote L-1?", "3+6", "El vencimiento es el día de ingreso más la vida útil.", ""),
        ("=", "{F} ¿Cuántos días de vida útil le quedan hoy al lote L-2?", "1+6-6", "Se suma la vida útil al ingreso y se resta el día de hoy.", " días"),
        ("abc", "{F} Según PEPS, ¿qué lote sale primero?", "El lote L-2", "El lote L-1", "El lote L-3", "L-2 ingresó el día 1, antes que los otros dos."),
        ("=", "{F} ¿Cuántos kilos hay en total en los tres lotes?", "200+150+250", "Se suman los kilos de los tres lotes.", " kg"),
        ("abc", "{F} ¿Qué documento acompaña un despacho con las cantidades, el destino y el lote?", "La guía de despacho", "El registro de temperatura", "La hoja de control de calidad", "La guía de despacho acompaña la salida; el registro y la hoja se usan en el acopio."),
        ("=", "{F} ¿Cuántos días de vida útil le quedan hoy al lote L-3?", "5+6-6", "Se suma la vida útil al ingreso y se resta el día de hoy.", " días"),
        ("abc", "{F} El rótulo del lote L-1 dice ingreso el día 3, pero la hoja de control dice día 4. ¿Qué corresponde?", "Informar la diferencia al encargado de calidad con ambos documentos, sin cambiar ninguno", "Cambiar el rótulo para que diga día 4", "Anotar ambos días en el rótulo", "Una diferencia entre documentos se informa con evidencia; cambiarla altera la trazabilidad."),
        ("abc", "{F} Un compañero propone retirar el rótulo del lote L-2 para reutilizar la caja. ¿Qué pasa con la trazabilidad?", "Se pierde: no se sabrá el origen, la fecha ni el responsable", "No cambia, porque la caja es la misma", "Mejora, porque hay menos papeles", "Sin rótulo no se puede seguir la historia del lote."),
        ("=", "{F} Si el día 7 se despacha todo el lote L-2 y la mitad del lote L-1, ¿cuántos kilos quedan en el acopio?", "200+150+250-150-200//2", "Se suman los tres lotes y se restan los kilos despachados.", " kg"),
        ("abc", "{F} Una compañera dice que PEPS consiste en vender primero lo más nuevo para que el acopio se vea fresco. ¿Qué respuesta es correcta?", "Es falso: PEPS saca primero lo más antiguo para evitar el deterioro", "Es cierto, porque lo nuevo se vende mejor", "Es cierto si el lote nuevo es más grande", "La rotación busca que nada se deteriore en bodega."),
    ],
    ctx=("abc", "Alguien te pide cambiar la fecha de ingreso de un lote en el rótulo para que «alcance a venderse». ¿Qué respondes?", "Que no, porque un rótulo no se altera, y que lo consultarás con un adulto responsable o el encargado de calidad", "Que sí, solo un día", "Que sí, si el producto se ve bien", "Alterar una fecha oculta el deterioro y puede dañar a quien consuma el producto."),
    sc=[
        ("En Pesquería: ¿cómo se calcula el día de vencimiento de un lote?", "Día de ingreso más vida útil", "El vencimiento se obtiene sumando la vida útil al ingreso."),
        ("En Pesquería: ¿qué significa PEPS?", "Primero en entrar, primero en salir", "PEPS ordena la rotación de lotes."),
        ("En Pesquería: ¿qué rol revisa los lotes y decide su destino?", "El encargado de calidad", "El encargado de calidad responde por la revisión de cada lote."),
    ],
    op=("Lotes de ejemplo, día actual 8: lote M-1, ingreso el día 4, 180 kg; lote M-2, ingreso el día 6, 220 kg; lote M-3, ingreso el día 3, 100 kg. Vida útil de ejemplo: 5 días. Escribe (a) el día de vencimiento de cada lote, (b) cuál sale primero según PEPS, (c) cuál vence hoy, (d) qué haces si el rótulo y la hoja de control no coinciden.",
        "(a) M-1: 4 + 5 = 9; M-2: 6 + 5 = 11; M-3: 3 + 5 = 8. (b) M-3, porque ingresó antes. (c) M-3 vence el día 8, que es hoy; según la norma vigente se informa al encargado de calidad, que decide su destino. (d) Informar la diferencia con ambos documentos, sin cambiar ninguno.",
        ["calcula los vencimientos", "aplica PEPS", "identifica el lote que vence hoy", "describe cómo informar una diferencia"],
        ["hoja con las cuatro respuestas"],
        ["sacar primero el lote más nuevo", "restar en vez de sumar la vida útil", "cambiar un documento para que coincida"],
        "Pregunta: «¿qué lote ingresó antes?». Si no responde, pídele que ordene los lotes por día de ingreso."),
    reinforce="Inventa tres lotes con día de ingreso y calcula el vencimiento y el orden de salida PEPS.",
    extend="Explica con un ejemplo por qué un rótulo con responsable ayuda a corregir un error sin alterar el dato.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (registro de temperatura de ejemplo, inventado). Lote L-5, especie A, 300 kg, en una cámara de Acopio Demo. Lecturas en grados Celsius: 08:00, 2; 09:00, 3; 10:00, 4; 11:00, 7; 12:00, 8; 13:00, 3. "
     "Límite de ejemplo: 5 °C. Observación anotada: «la puerta de la cámara quedó abierta durante una descarga». "
     "Regla de ejemplo: si una lectura supera el límite, el lote se retiene y se informa al encargado de calidad, que decide su destino con la norma vigente.")
build(
    O4, 3, F,
    use="Aprenderé a analizar el registro de temperatura de un lote, detectar una interrupción de la cadena de frío y decidir qué se informa, qué se retiene y qué acción correctiva se propone.",
    prior=["Sé qué son la cadena de frío, el lote y el registro de temperatura.", "Sé comparar un dato con un límite.", "Sé restar números enteros."],
    explain=[
        "El análisis de un registro de temperatura consiste en comparar cada lectura con el límite. Una lectura sobre el límite es una desviación y significa que la cadena de frío se interrumpió. Mientras se decide qué hacer, el lote queda en retención, es decir, separado y sin venderse. La decisión sobre su destino no la toma quien lo huele o lo prueba, sino el encargado de calidad, con la norma vigente.",
        "Una causa probable es una explicación posible que se debe comprobar; por ejemplo, una puerta abierta durante una descarga. No se da por segura con una sola observación. Una acción correctiva es una medida para corregir la desviación y evitar que se repita, como una alarma de temperatura. Por ejemplo, si un registro marca 7 °C con un límite de 3 °C, la desviación es de 4 °C.",
        f"El registro no se altera: las lecturas fuera del límite se informan tal como se anotaron. La tarea de manipular producto o equipos de frío la hace personal autorizado; aquí solo se analiza en papel. {EMER} {AVISO}",
    ],
    vocab=[("desviación", "lectura o dato fuera del límite permitido"), ("retención", "separación del lote sin venderlo mientras se decide su destino"), ("causa probable", "explicación posible que hay que comprobar"), ("acción correctiva", "medida para corregir una desviación y evitar que se repita"), ("límite de temperatura", "valor máximo que acepta el plan de calidad")],
    worked=[
        ("Calcular una desviación", "Un registro de ejemplo marca 9 °C y el límite es 6 °C. ¿Cuál es la desviación?", ["La desviación es la lectura menos el límite.", "9 menos 6 es 3."], "3 °C"),
        ("Decidir una retención", "Un lote de ejemplo tiene una lectura sobre el límite. ¿Qué se hace según la regla?", ["Hay una desviación.", "Se retiene el lote y se informa al encargado de calidad."], "Retener el lote e informar al encargado de calidad"),
    ],
    mistakes=[("Decidir si un lote sirve oliéndolo o probándolo.", "El olor o el sabor no reemplazan el registro ni el análisis del encargado.", "Se retiene el lote y decide el encargado de calidad."),
              ("Creer que el problema se resolvió porque la última lectura volvió al rango.", "La interrupción ya aceleró el deterioro.", "Se informa la desviación aunque la temperatura haya vuelto a bajar.")],
    T=[
        ("abc", "En Pesquería: ¿qué es la retención de un lote?", "Dejarlo separado y sin vender hasta que se decida su destino", "Venderlo rápido antes de que se deteriore más", "Congelarlo sin revisar su registro", "La retención separa el lote mientras decide el encargado de calidad."),
        ("abc", "En Pesquería: ¿qué es una desviación en un registro de temperatura?", "Una lectura fuera del límite permitido", "La lectura más baja del día", "La hora de la primera lectura", "La desviación es un valor fuera del límite."),
        ("abc", "En Pesquería: ¿qué es una acción correctiva?", "Una medida para corregir una desviación y evitar que se repita", "Un permiso para vender un lote retenido", "La anotación de una lectura en el registro", "La acción correctiva corrige y previene, no autoriza ventas ni anota lecturas."),
        ("=", "{F} ¿Cuántos grados sobre el límite quedó la lectura más alta?", "8-5", "Se resta el límite de la lectura más alta.", " °C"),
        ("abc", "{F} ¿Qué lecturas superaron el límite?", "Las de las 11:00 y las 12:00", "Las de las 10:00 y las 11:00", "Solo la de las 12:00", "7 y 8 superan 5; la de las 10:00 es 4 y no lo supera."),
        ("=", "{F} ¿Cuántos grados subió la temperatura entre las 10:00 y las 12:00?", "8-4", "Se resta la lectura de las 10:00 de la de las 12:00.", " °C"),
        ("=", "{F} ¿Cuántos grados hay entre la lectura más alta y la más baja del día?", "8-2", "Se resta la lectura más baja de la más alta.", " °C"),
        ("abc", "{F} ¿Qué corresponde hacer con el lote L-5?", "Retenerlo e informar al encargado de calidad", "Venderlo, porque a las 13:00 volvió a 3 °C", "Oler el producto y decidir si sirve", "La regla pide retener cuando una lectura supera el límite."),
        ("abc", "{F} ¿Quién decide el destino del lote retenido?", "El encargado de calidad, con la norma vigente", "El comprador, porque es quien lo va a recibir", "Quien lo huela y lo pruebe", "El destino del lote es una decisión técnica del encargado de calidad."),
        ("abc", "{F} Un compañero dice que, como a las 13:00 la temperatura volvió a 3 °C, el problema se resolvió. ¿Qué respuesta es correcta?", "Es falso: la interrupción ya aceleró el deterioro, así que el lote se retiene y se evalúa", "Es cierto: volver al rango borra el daño", "Es cierto si el lote se vende de inmediato", "La cadena de frío interrumpida no se repara con una lectura posterior."),
        ("abc", "{F} ¿Cómo se debe tratar la observación sobre la puerta abierta?", "Como una causa probable que se comprueba, y se propone una acción correctiva", "Como la única causa demostrada", "Como un dato sin importancia que se puede borrar", "Una observación aislada plantea una causa probable, no una prueba."),
        ("abc", "{F} ¿Qué control de ingeniería ayudaría a evitar que se repita la desviación?", "Una alarma de temperatura y una puerta con cierre automático, instaladas por personal autorizado", "Un cartel que diga «cerrar la puerta»", "Ropa térmica para el personal", "La alarma y el cierre automático cambian el lugar; el cartel es administrativo y la ropa es EPP."),
        ("abc", "{F} Un compañero propone borrar las lecturas de las 11:00 y las 12:00 para que el lote se pueda vender. ¿Qué respondes?", "Que no: un registro no se altera, y las lecturas se informan tal como están", "Que sí, si el producto se ve bien", "Que sí, si solo borras una de las dos", "Borrar lecturas oculta la desviación y puede perjudicar a quien consuma el producto."),
    ],
    ctx=("abc", "Alguien te pide anotar 4 °C en las lecturas de las 11:00 y las 12:00 de un registro de ejemplo «para que el lote pase». ¿Qué respondes?", "Que no, porque un registro no se altera, y que lo consultarás con un adulto responsable o la autoridad sanitaria", "Que sí, porque la diferencia es pequeña", "Que sí, si lo corriges mañana", "Falsear una lectura oculta un riesgo sanitario real."),
    sc=[
        ("En Pesquería: ¿qué se hace con un lote cuando una lectura supera el límite?", "Se retiene y se informa al encargado de calidad", "La regla de ejemplo ordena retener y avisar."),
        ("En Pesquería: ¿cómo se calcula una desviación?", "Lectura menos límite", "La desviación mide cuánto se pasó la lectura."),
        ("En Pesquería: ¿decide el olor o el sabor el destino de un lote?", "No, decide el encargado de calidad con el registro", "El olor y el sabor no reemplazan el registro técnico."),
    ],
    op=("Registro de ejemplo del lote L-9 en grados Celsius: 08:00, 2; 09:00, 6; 10:00, 3; 11:00, 3. Límite de ejemplo: 4 °C. Observación: «falla del equipo de frío a las 08:45». Escribe (a) qué lectura supera el límite y por cuántos grados, (b) qué corresponde hacer con el lote, (c) una causa probable y cómo la comprobarías, (d) una acción correctiva.",
        "(a) La de las 09:00, que supera el límite en 6 − 4 = 2 °C. (b) Retener el lote e informar al encargado de calidad, aunque las lecturas posteriores estén dentro del límite. (c) Una causa probable es la falla del equipo de frío anotada; se comprueba con el registro de mantención del equipo, sin darla por segura. (d) Una alarma de temperatura y un plan de mantención del equipo, instalados y ejecutados por personal autorizado.",
        ["identifica la lectura y la desviación", "decide retener e informar", "plantea una causa probable comprobable", "propone una acción correctiva"],
        ["hoja con las cuatro respuestas"],
        ["decidir por el olor", "tomar la causa como segura", "olvidar informar porque luego bajó la temperatura"],
        "Pregunta: «¿qué lectura supera el límite de 4 °C?». Si no responde, pídele que compare cada lectura con el límite."),
    reinforce="Inventa un registro de cinco lecturas con un límite y marca cuáles son desviaciones.",
    extend="Explica por qué una lectura que vuelve al rango no borra la interrupción de la cadena de frío.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (control de calidad de ejemplo, inventado). Acopio Demo recibe tres lotes: L-6, 200 kg; L-7, 250 kg; L-8, 150 kg. En el control de calidad se rechazan 10 kg de L-6, 20 kg de L-7 y 0 kg de L-8. "
     "Meta de ejemplo: rechazo máximo de 6 % por lote. Proporción de ejemplo del plan de calidad: 1 kg de hielo por cada 2 kg de producto. Precio de ejemplo: 1.400 pesos por kilo.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar un criterio de calidad con datos de ejemplo: calcular rechazos, merma y pérdidas, comparar con una meta por lote y proponer mejoras sin alterar los registros.",
    prior=["Sé qué son lote, rótulo y retención.", "Sé calcular un porcentaje con números enteros.", "Sé multiplicar, dividir y restar números enteros."],
    explain=[
        "El porcentaje de rechazo es los kilos rechazados por 100, divididos por los kilos recibidos. La merma es la parte del producto que se pierde antes de llegar al consumidor, por rechazo o deterioro. El plan de calidad es el documento donde un establecimiento fija sus criterios, controles, metas y proporciones, como la cantidad de hielo por kilo de producto; sus valores reales dependen de la norma vigente y de cada establecimiento.",
        "Una meta por lote se revisa lote por lote: un porcentaje global puede ocultar un lote malo. Por ejemplo, con un lote de 200 kg con 10 kg rechazados y otro de 200 kg con 30 kg rechazados, el global es 10 %, pero el segundo lote tiene 15 %. La pérdida económica de un rechazo es los kilos rechazados por el precio.",
        f"Los cambios al plan, como reducir el hielo para ahorrar, se hacen solo con evidencia y autorización del encargado de calidad. Los números de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("porcentaje de rechazo", "kilos rechazados por 100, divididos por los kilos recibidos"), ("merma", "parte del producto que se pierde antes de llegar al consumidor"), ("plan de calidad", "documento que fija criterios, controles, metas y proporciones de un establecimiento"), ("meta por lote", "límite que se revisa para cada lote por separado"), ("pérdida económica", "kilos perdidos por su precio")],
    worked=[
        ("Calcular un rechazo", "Un lote de ejemplo de 400 kg tiene 20 kg rechazados. ¿Qué porcentaje es?", ["Se multiplica 20 por 100: 2.000.", "2.000 dividido en 400 es 5."], "5 %"),
        ("Calcular una pérdida", "Se rechazan 15 kg y el precio de ejemplo es 1.000 pesos por kilo. ¿Cuál es la pérdida?", ["La pérdida es los kilos por el precio.", "15 por 1.000 es 15.000."], "15.000 pesos"),
    ],
    mistakes=[("Concluir que todos los lotes cumplen porque el porcentaje global cumple.", "Un lote malo puede quedar oculto dentro del promedio.", "Revisa cada lote contra la meta por lote."),
              ("Reducir el hielo para ahorrar sin consultar al plan de calidad.", "Menos hielo puede romper la cadena de frío.", "Los cambios se hacen con evidencia y autorización del encargado de calidad.")],
    T=[
        ("abc", "En Pesquería: ¿qué es el porcentaje de rechazo de un lote?", "Los kilos rechazados por 100, divididos por los kilos recibidos", "Los kilos recibidos divididos por los rechazados", "El precio de los kilos rechazados", "El rechazo se calcula sobre lo recibido."),
        ("abc", "En Pesquería: ¿qué es la merma de un producto del mar?", "La parte del producto que se pierde antes de llegar al consumidor", "El aumento de peso por el hielo", "El nombre del lote que se despacha primero", "La merma es una pérdida, no un aumento ni un nombre."),
        ("abc", "En Pesquería: ¿qué es un plan de calidad?", "El documento que fija criterios, controles, metas y proporciones de un establecimiento", "La lista de turnos del personal", "El registro de lo capturado en la faena", "El plan de calidad ordena el control de calidad, no los turnos ni la captura."),
        ("=", "{F} ¿Cuántos kilos se rechazaron en total?", "10+20+0", "Se suman los kilos rechazados de los tres lotes.", " kg"),
        ("=", "{F} ¿Qué porcentaje de rechazo tiene el lote L-6?", "10*100//200", "Se multiplican los kilos rechazados por 100 y se dividen entre los recibidos.", " %"),
        ("=", "{F} ¿Qué porcentaje de rechazo tiene el lote L-7?", "20*100//250", "Se multiplican los kilos rechazados por 100 y se dividen entre los recibidos.", " %"),
        ("=", "{F} ¿Cuántos kilos de hielo corresponden al lote L-8 según la proporción del plan?", "150//2", "Se divide el producto entre dos, según la proporción de ejemplo.", " kg"),
        ("=", "{F} ¿Cuántos kilos aceptados hay entre los tres lotes?", "200+250+150-30", "Se suman los lotes y se restan los kilos rechazados.", " kg"),
        ("=", "{F} ¿Cuál es la pérdida económica por los kilos rechazados, a precio de ejemplo?", "30*1400", "Se multiplican los kilos rechazados por el precio por kilo.", " pesos"),
        ("abc", "{F} ¿Qué lote excede la meta de ejemplo de 6 % por lote?", "El lote L-7, con 8 %", "El lote L-6, con 5 %", "El lote L-8, con 0 %", "Solo L-7 supera el 6 %; los otros lotes cumplen."),
        ("abc", "{F} Un compañero dice que, como el rechazo global es 5 %, todos los lotes cumplen. ¿Qué respuesta es correcta?", "Es falso: el global resume, pero L-7 con 8 % supera el máximo por lote", "Es cierto: si el global cumple, todos cumplen", "Es cierto si el lote L-8 no tuvo rechazos", "La meta se revisa por lote; el global puede ocultar un lote que no cumple."),
        ("=", "{F} Si el lote L-7 hubiera tenido un 4 % de rechazo, ¿cuántos kilos menos se habrían rechazado?", "20-250*4//100", "Se resta al rechazo real el rechazo que habría tenido con 4 %.", " kg"),
        ("abc", "{F} Alguien propone ahorrar reduciendo el hielo a la mitad de la proporción del plan. ¿Qué respondes?", "Que no: menos hielo puede romper la cadena de frío, y la proporción solo se cambia con evidencia y autorización", "Que sí, porque el hielo no afecta la calidad", "Que sí, si el producto se vende el mismo día", "La proporción del plan protege la cadena de frío y no se cambia por ahorro."),
    ],
    ctx=("abc", "Un conocido te pide anotar 0 kg rechazados en el lote L-7 para que no se note que superó la meta. ¿Qué respondes?", "Que no, porque un registro no se altera, y que lo consultarás con un adulto responsable o el encargado de calidad", "Que sí, solo por esta vez", "Que sí, si lo informas después", "Falsear un rechazo oculta un problema de calidad real."),
    sc=[
        ("En Pesquería: ¿cómo se calcula el porcentaje de rechazo?", "Kilos rechazados por 100, divididos por los kilos recibidos", "El rechazo se mide sobre lo recibido."),
        ("En Pesquería: ¿por qué se revisa la meta lote por lote?", "Porque el promedio global puede ocultar un lote que no cumple", "Un lote malo puede quedar escondido en el global."),
        ("En Pesquería: ¿cómo se calcula una pérdida económica?", "Kilos perdidos por el precio por kilo", "La pérdida se obtiene multiplicando kilos y precio."),
    ],
    op=("Control de ejemplo: lote N-1, 300 kg con 15 kg rechazados; lote N-2, 200 kg con 20 kg rechazados. Meta de ejemplo: rechazo máximo de 6 % por lote. Precio de ejemplo: 1.000 pesos por kilo. Proporción de ejemplo: 1 kg de hielo por cada 2 kg de producto. Escribe (a) el porcentaje de rechazo de cada lote, (b) cuál supera la meta, (c) la pérdida económica total, (d) los kilos de hielo para el lote N-2.",
        "(a) N-1: 15 × 100 ÷ 300 = 5 %; N-2: 20 × 100 ÷ 200 = 10 %. (b) N-2 supera la meta de 6 %. (c) 35 kg × 1.000 = 35.000 pesos. (d) 200 ÷ 2 = 100 kg de hielo. Los cambios al plan los decide el encargado de calidad con autorización.",
        ["calcula los porcentajes", "identifica el lote que supera la meta", "calcula la pérdida", "calcula el hielo del plan"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre los kilos aceptados", "juzgar solo por el global", "olvidar sumar los kilos rechazados de los dos lotes"],
        "Pregunta: «¿entre qué valor divides los kilos rechazados?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres lotes con kilos recibidos y rechazados, y marca cuáles superan una meta de 6 %.",
    extend="Explica con un ejemplo por qué un lote con rechazo alto puede esconderse en un porcentaje global bajo.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La embarcación ficticia «Nave Demo» sale con 8 personas a bordo a una faena a 15 millas de la costa. El cuadro de obligaciones de emergencia (documento que asigna a cada persona su función) solo asigna función a 5 de las 8 personas. "
     "Peligros anotados: caída al agua, agua fría, incendio en la sala de máquinas, un equipo de comunicación de emergencia que depende de una sola persona y fatiga después de un turno largo. Meta de ejemplo de un simulacro: reunir a las 8 personas con su chaleco en 5 minutos.")
build(
    O5, 1, F,
    use="Aprenderé qué son la supervivencia en el mar, los primeros auxilios y el combate de incendio como conceptos, por qué la prevención va antes y qué hacer, como estudiante, ante una emergencia.",
    prior=["Sé qué son peligro, riesgo y jerarquía de controles.", "Sé qué es el equipo de flotación y el patrón.", "Sé restar números enteros."],
    explain=[
        "La supervivencia en el mar es el conjunto de medidas, equipos y conductas para que las personas sigan con vida después de un accidente, hasta ser rescatadas. Los primeros auxilios son la ayuda inmediata y básica a una persona herida o enferma hasta que llegue personal de salud; las dan personas formadas, y este cuaderno no enseña técnicas clínicas. El combate de incendio es el conjunto de acciones que realiza personal formado para controlar un fuego. La hipotermia es el descenso peligroso de la temperatura del cuerpo, por ejemplo por estar en agua fría.",
        "La mejor protección es la prevención, que actúa antes del accidente: evitar las fuentes de fuego, instalar detectores y alarmas (control de ingeniería), practicar simulacros y repartir funciones (controles administrativos) y usar el equipo de flotación (EPP). El plan de emergencia es el documento que dice qué hace cada persona. El simulacro es una práctica planificada y registrada para comprobar si el plan funciona. La normativa nacional e internacional vigente exige equipos, formación y simulacros.",
        f"Ninguna persona sin formación debe intentar un rescate o apagar un fuego: se aleja de la zona de riesgo y avisa. {EMER} {AVISO}",
    ],
    vocab=[("supervivencia en el mar", "conjunto de medidas y equipos para seguir con vida hasta el rescate"), ("primeros auxilios", "ayuda inmediata y básica hasta que llegue personal de salud"), ("combate de incendio", "acciones de personal formado para controlar un fuego"), ("hipotermia", "descenso peligroso de la temperatura del cuerpo"), ("plan de emergencia", "documento que dice qué hace cada persona en una emergencia"), ("cuadro de obligaciones", "documento que asigna a cada persona su función en una emergencia"), ("simulacro", "práctica planificada y registrada para comprobar el plan")],
    worked=[
        ("Peligro y riesgo", "En una nave de ejemplo hay un cable eléctrico con el aislante dañado cerca de la sala de máquinas. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el cable con el aislante dañado.", "El riesgo es que se produzca una chispa y un incendio."], "Peligro: el cable dañado; riesgo: una chispa que provoque un incendio"),
        ("Clasificar un control", "Una nave de ejemplo instala un detector de humo con alarma en la sala de máquinas. ¿A qué nivel corresponde?", ["El detector cambia físicamente el lugar.", "Los cambios físicos de ese tipo son controles de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Creer que saber nadar hace innecesario el equipo de flotación.", "El agotamiento y el agua fría pueden vencer a cualquier persona, aunque sepa nadar.", "El equipo de flotación se usa siempre que corresponda."),
              ("Creer que leer sobre una emergencia habilita para intervenir en ella.", "Un rescate, un fuego o una lesión exigen formación y personal autorizado.", "Te alejas de la zona de riesgo y avisas a un adulto responsable y a emergencias.")],
    T=[
        ("abc", "En Pesquería: ¿qué es la hipotermia?", "El descenso peligroso de la temperatura del cuerpo, por ejemplo en agua fría", "El aumento de la temperatura por trabajar al sol", "El cansancio por un turno largo", "La hipotermia es un enfriamiento del cuerpo; el cansancio es fatiga."),
        ("abc", "En Pesquería: ¿qué son los primeros auxilios?", "La ayuda inmediata y básica a una persona herida o enferma hasta que llegue personal de salud", "Un tratamiento completo que reemplaza al personal de salud", "El registro de las lesiones de la tripulación", "Los primeros auxilios son una ayuda inicial, no un tratamiento completo ni un registro."),
        ("abc", "En Pesquería: ¿qué es el plan de emergencia de una nave?", "El documento que dice qué hace cada persona en una emergencia", "El plan de las faenas del mes", "La lista de repuestos de la sala de máquinas", "El plan de emergencia asigna acciones ante un accidente, no organiza faenas ni repuestos."),
        ("=", "{F} ¿Cuántas personas quedan sin función en el cuadro de obligaciones?", "8-5", "Se resta a las personas a bordo las que tienen función asignada.", " personas"),
        ("abc", "{F} Un detector de humo con alarma en la sala de máquinas, instalado por personal autorizado, es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla escrita", "De EPP, porque protege a quien está cerca", "El detector modifica la sala y no depende de que alguien lo recuerde."),
        ("abc", "{F} La práctica periódica de simulacros es un control de tipo:", "Administrativo, porque entrena y ordena conductas", "De ingeniería, porque cambia la nave", "De EPP, porque protege el cuerpo", "Un simulacro entrena a las personas, pero no cambia la nave ni es un equipo personal."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al agua fría?", "Que una persona que cae al agua pierda calor y sufra hipotermia", "El agua misma, que está a la temperatura del mar", "Que el equipo de flotación se moje", "El riesgo es el daño posible a la persona; el agua es el peligro."),
        ("abc", "{F} Un tripulante dice: «yo sé nadar, así que no necesito el equipo de flotación». ¿Qué respuesta es correcta?", "El equipo de flotación se usa igual: el agotamiento y el agua fría pueden vencer a quien sabe nadar", "Es cierto, porque saber nadar elimina el peligro", "Es cierto si el mar está calmo", "Saber nadar no elimina el cansancio ni el frío del agua."),
        ("abc", "Durante una visita de ejemplo ves humo que sale de la sala de máquinas de una nave amarrada. ¿Qué corresponde según las reglas generales?", "Alejarte, avisar a un adulto responsable y a emergencias, sin intentar apagar el fuego", "Entrar a ver qué pasa", "Buscar un extintor y apagarlo tú", "Un fuego exige personal formado; tu acción es alejarte y avisar."),
        ("abc", "En Pesquería: ¿por qué prevenir un incendio es más efectivo que combatirlo?", "Porque al controlar la fuente se evita el accidente, mientras combatirlo supone estar ya en peligro", "Porque basta con tener extintores a bordo", "Porque combatir un incendio nunca es posible", "La prevención actúa antes, y tener extintores no reemplaza evitar el fuego."),
        ("abc", "{F} Para el peligro de un equipo de comunicación que depende de una sola persona, ¿qué medida de nivel más efectivo corresponde?", "Un equipo de comunicación de emergencia fijo, instalado y revisado por personal autorizado", "Un cartel que diga «avisar»", "Pedir a cada persona que grite fuerte", "El equipo fijo es un control de ingeniería; el cartel es administrativo y gritar no es una medida."),
        ("=", "{F} Si el simulacro de ejemplo reúne a las 8 personas con chaleco en 7 minutos, ¿cuántos minutos se pasó de la meta?", "7-5", "Se resta la meta del tiempo real.", " minutos"),
        ("abc", "{F} Una estudiante dice: «con este cuaderno ya puedo participar en un rescate en el mar». ¿Qué respuesta es correcta?", "Es falso: un rescate exige formación y personal autorizado; tu acción es alejarte y avisar", "Es cierto, si lleva chaleco", "Es cierto, si hay otra persona mirando", "El chaleco o la compañía no reemplazan la formación."),
    ],
    ctx=("abc", "Un conocido te invita a «practicar supervivencia» lanzándote al mar con chaleco un día de oleaje. ¿Qué respondes?", "Que no, porque esa práctica exige instructor autorizado, equipo adecuado y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, porque con chaleco no hay riesgo", "Que sí, si el agua está tibia", "El chaleco no elimina el peligro, y la práctica real exige instructor y condiciones controladas."),
    sc=[
        ("En Pesquería: ¿qué es un simulacro?", "Una práctica planificada y registrada para comprobar si el plan de emergencia funciona", "El simulacro verifica el plan antes de una emergencia real."),
        ("En Pesquería: ¿qué es el cuadro de obligaciones?", "El documento que asigna a cada persona su función en una emergencia", "El cuadro reparte funciones para actuar sin improvisar."),
        ("¿Qué haces tú ante un incendio a bordo?", "Alejarte de la zona de riesgo y avisar a un adulto responsable y a emergencias", "Sin formación, lo seguro es alejarte y avisar."),
    ],
    op=("Caso de ejemplo: una nave ficticia sale con 6 personas; el cuadro de obligaciones asigna función a 4 de ellas. Peligros: caída al agua en agua fría y fuego en la cocina. El simulacro de ejemplo reunió al grupo en 8 minutos con una meta de 5. Escribe (a) cuántas personas quedan sin función y cuántos minutos se pasó el simulacro, (b) un control de ingeniería para el fuego, (c) un control administrativo, (d) qué harías tú ante un incendio a bordo.",
        "(a) 6 − 4 = 2 personas sin función; 8 − 5 = 3 minutos sobre la meta. (b) Un detector de humo con alarma y una instalación revisada por personal autorizado. (c) Asignar una función a cada persona, definir reemplazos y practicar simulacros. (d) Alejarme de la zona de riesgo, avisar a un adulto responsable y a emergencias, sin intentar apagar el fuego.",
        ["calcula personas sin función y minutos", "propone un control de ingeniería", "propone un control administrativo", "responde con la regla general de emergencia"],
        ["hoja con las cuatro respuestas"],
        ["decir que se apaga el fuego sin formación", "proponer solo el chaleco", "no calcular los minutos de más"],
        "Pregunta: «¿qué hace una persona sin formación ante un incendio?». Si no responde, pídele que relea el último párrafo."),
    reinforce="Escribe la regla general ante una emergencia y un ejemplo de control de cada nivel de la jerarquía para una nave inventada.",
    extend="Explica con un ejemplo por qué un cuadro de obligaciones sin simulacros puede no servir en una emergencia.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (inventario de ejemplo, inventado). «Nave Demo»; mes actual: 5. Chalecos de flotación: 10, revisión vence en el mes 8. Aros salvavidas: 2, revisión vence en el mes 8. Balsa salvavidas: 1 de 10 plazas, revisión vence en el mes 5. "
     "Señales de socorro: 4, vencen en el mes 3. Extintores: 3, revisión vence en el mes 7. Botiquín: 1, revisión vence en el mes 6. Un equipo está vencido si su mes de vencimiento es anterior al mes actual; vence este mes si es igual.")
build(
    O5, 2, F,
    use="Aprenderé los nombres y funciones generales de los equipos de seguridad a bordo, los documentos que los controlan, como el inventario y el cuadro de obligaciones, y los roles de quienes los revisan.",
    prior=["Sé qué son el plan de emergencia y el simulacro.", "Sé qué es el EPP.", "Sé comparar un mes con otro."],
    explain=[
        "Los equipos de seguridad se describen aquí solo por su función. El chaleco de flotación mantiene a flote a una persona. El aro salvavidas es un flotador que ofrece flotación a una persona que está en el agua. La balsa salvavidas es una embarcación de emergencia con un número de plazas, que es el espacio indicado para cada persona. Las señales de socorro avisan a otros que hay una emergencia. La radiobaliza de emergencia emite una señal para ayudar a ubicar a la nave. Los extintores y el botiquín sirven al personal formado.",
        "Los documentos de control son el inventario, que lista los equipos y sus fechas de revisión; el certificado o la etiqueta de revisión, que prueba que el equipo fue revisado por personal autorizado; y el cuadro de obligaciones. Un equipo vencido no debe considerarse disponible: se informa al responsable y se repone según la norma vigente. La capacidad indicada, como las plazas de una balsa, es un límite de seguridad que no se supera.",
        f"Los roles: el patrón responde por el cumplimiento; el responsable de seguridad lleva el inventario; el personal autorizado revisa o repone los equipos; cada tripulante conoce su función. Este cuaderno no enseña a usar estos equipos. {EMER} {AVISO}",
    ],
    vocab=[("chaleco de flotación", "equipo que mantiene a flote a una persona"), ("aro salvavidas", "flotador que ofrece flotación a una persona que está en el agua"), ("balsa salvavidas", "embarcación de emergencia con un número de plazas"), ("plaza", "espacio indicado para una persona en una balsa"), ("señal de socorro", "dispositivo que avisa que hay una emergencia"), ("radiobaliza de emergencia", "equipo que emite una señal para ayudar a ubicar la nave"), ("inventario", "lista de equipos con sus fechas de revisión"), ("equipo vencido", "equipo cuyo mes de vencimiento ya pasó"), ("responsable de seguridad", "persona que lleva el inventario y vigila los equipos")],
    worked=[
        ("Equipo vencido", "En un inventario de ejemplo, en el mes 6, un extintor vence en el mes 4. ¿Está vencido?", ["Se compara el mes de vencimiento con el mes actual.", "4 es anterior a 6."], "Sí, está vencido"),
        ("Capacidad de una balsa", "Una balsa de ejemplo tiene 8 plazas y a bordo van 9 personas. ¿Alcanza?", ["Cada persona necesita una plaza.", "9 es mayor que 8: falta 1 plaza."], "No alcanza: falta 1 plaza"),
    ],
    mistakes=[("Seguir considerando disponible un equipo cuya revisión ya venció.", "Un equipo vencido no tiene garantía de funcionar.", "Se informa al responsable y se repone antes de contar con él."),
              ("Superar la capacidad de una balsa porque «se aprietan».", "La capacidad es un límite de seguridad.", "Se respeta el número de plazas indicado.")],
    T=[
        ("abc", "En Pesquería: ¿qué es una radiobaliza de emergencia?", "Un equipo que emite una señal para ayudar a ubicar la nave", "Un equipo que mide la profundidad del agua", "Una luz común de navegación", "La radiobaliza emite una señal de socorro; medir profundidad es otra función."),
        ("abc", "En Pesquería: ¿qué documento asigna a cada persona su función en una emergencia?", "El cuadro de obligaciones", "El registro de capturas", "El plan de mantención del motor", "El cuadro de obligaciones reparte funciones; la captura y el motor tienen otros documentos."),
        ("abc", "En Pesquería: ¿qué es una señal de socorro?", "Un dispositivo que avisa a otros que hay una emergencia", "Una señal que indica el rumbo de la nave", "Un instrumento que mide el viento", "La señal de socorro pide ayuda; el rumbo y el viento son otros datos."),
        ("=", "{F} ¿Cuántos meses faltan para el vencimiento del botiquín?", "6-5", "Se resta el mes actual del mes de vencimiento.", " mes"),
        ("abc", "{F} ¿Qué equipo del inventario está vencido?", "Las señales de socorro, que vencieron en el mes 3", "Los chalecos de flotación", "Los extintores", "El mes 3 es anterior al mes actual, que es el 5."),
        ("=", "{F} Si la nave sale con 9 personas, ¿cuántos chalecos sobran?", "10-9", "Se restan las personas a bordo de los chalecos del inventario.", " chaleco"),
        ("abc", "{F} ¿Qué equipo vence este mes?", "La balsa salvavidas", "El botiquín", "Los extintores", "Su vencimiento es el mes 5, igual al mes actual."),
        ("abc", "{F} ¿Qué corresponde hacer con las señales de socorro vencidas?", "Informar al responsable y reponerlas por personal autorizado antes de contar con ellas", "Usarlas igual, porque casi nunca se usan", "Cambiar el mes de vencimiento escrito en la etiqueta", "Un equipo vencido no debe considerarse disponible, y su etiqueta no se altera."),
        ("abc", "{F} La nave sale ahora con 12 personas. ¿Alcanzan los chalecos y las plazas de la balsa?", "No: faltan 2 chalecos y 2 plazas", "Sí, porque hay un chaleco más que personas", "Solo faltan 2 chalecos; la balsa alcanza si se aprietan", "Hay 10 chalecos y 10 plazas para 12 personas."),
        ("abc", "{F} Un compañero dice que el cuadro de obligaciones es solo un papel y que no hace falta que cada uno conozca su función. ¿Qué respuesta es correcta?", "Es falso: en una emergencia cada persona debe conocer su función, y por eso se difunde y se practica", "Es cierto, porque el patrón decide todo en el momento", "Es cierto si hay pocos tripulantes", "El cuadro sirve si cada persona sabe qué le corresponde."),
        ("abc", "{F} Una compañera dice que en una balsa de 10 plazas pueden ir 12 personas si se aprietan. ¿Qué respuesta es correcta?", "Es falso: la capacidad es un límite de seguridad que no se supera", "Es cierto, porque en una emergencia todo vale", "Es cierto si las personas son delgadas", "El número de plazas se respeta; superarlo pone en riesgo a todos."),
        ("=", "{F} Reponer las 4 señales de socorro cuesta 15.000 pesos de ejemplo cada una. ¿Cuál es el costo total?", "4*15000", "Se multiplica la cantidad de señales por el costo de cada una.", " pesos"),
        ("abc", "{F} Una estudiante dice: «puedo revisar y reponer un extintor porque sé leer las fechas del inventario». ¿Qué respuesta es correcta?", "Es falso: la revisión la hace personal autorizado; tu parte es leer el documento e informar", "Es cierto, si lo hace con guantes", "Es cierto, si lo hace con otra persona", "Leer el inventario no habilita para revisar equipos de seguridad."),
    ],
    ctx=("abc", "Un conocido te muestra una balsa de su bote y te propone «probarla» en el muelle por diversión. ¿Qué respondes?", "Que no, porque probar equipos de seguridad exige personal autorizado y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, porque en el muelle no hay riesgo", "Que sí, si llevas chaleco", "Los equipos de seguridad se prueban solo según la norma y con personal autorizado."),
    sc=[
        ("En Pesquería: ¿cuándo está vencido un equipo del inventario?", "Cuando su mes de vencimiento es anterior al mes actual", "Un mes anterior al actual indica revisión vencida."),
        ("En Pesquería: ¿qué es una plaza de balsa?", "El espacio indicado para una persona", "Cada persona necesita una plaza de la balsa."),
        ("En Pesquería: ¿qué rol lleva el inventario de equipos de seguridad?", "El responsable de seguridad", "El responsable de seguridad vigila las fechas y los equipos."),
    ],
    op=("Inventario de ejemplo, mes actual 4: chalecos, 12, vencen en el mes 6; balsa de 8 plazas, vence en el mes 2; señales de socorro, 3, vencen en el mes 4; botiquín, 1, vence en el mes 3. La nave sale con 10 personas. Escribe (a) qué equipos están vencidos y cuál vence este mes, (b) si alcanzan los chalecos, (c) si alcanza la balsa y qué falta, (d) qué harías con un equipo vencido.",
        "(a) Vencidos: la balsa (mes 2) y el botiquín (mes 3); las señales de socorro vencen este mes (mes 4). (b) Sí: hay 12 chalecos para 10 personas. (c) La balsa tiene 8 plazas y está vencida; para 10 personas faltan 2 plazas y la revisión. (d) Informar al responsable y reponer o revisar por personal autorizado, sin cambiar las fechas de las etiquetas.",
        ["identifica vencidos y el que vence este mes", "compara chalecos con personas", "compara plazas con personas", "describe qué hacer con un equipo vencido"],
        ["hoja con las cuatro respuestas"],
        ["considerar disponible un equipo vencido", "no comparar plazas y personas", "proponer cambiar la fecha de la etiqueta"],
        "Pregunta: «¿cuándo un equipo está vencido?». Si no responde, pídele que relea la ficha 2 y compare los meses."),
    reinforce="Inventa un inventario de cuatro equipos con meses de vencimiento y marca cuáles están vencidos para un mes actual que elijas.",
    extend="Explica por qué un inventario al día no reemplaza la revisión de los equipos por personal autorizado.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (informe de simulacro de ejemplo, inventado). «Nave Demo», 8 personas. Cuadro de obligaciones: P1, aviso por radio; P2, recuento de personas; P3, reparto de chalecos; P4, botiquín; P5 a P8, sin función asignada. "
     "Informe del simulacro: tiempo para reunir a las 8 personas, 7 minutos (meta de ejemplo, 5); personas con chaleco puesto al final, 6 de 8; la persona con la función de aviso por radio estaba fuera de turno y no tenía reemplazo; un chaleco tenía la correa cortada y estaba guardado en el cajón junto a los demás.")
build(
    O5, 3, F,
    use="Aprenderé a analizar el informe de un simulacro: leer hallazgos, calcular porcentajes y tiempos, y proponer acciones de mejora sin improvisar procedimientos.",
    prior=["Sé qué son el cuadro de obligaciones y el simulacro.", "Sé calcular un porcentaje con números enteros.", "Sé comparar un resultado con una meta."],
    explain=[
        "Un informe de simulacro registra qué se planificó, qué ocurrió y qué se debe mejorar. Un hallazgo es un hecho observado que muestra una falla o algo por mejorar, como un equipo en mal estado o una función sin reemplazo. Una acción de mejora es una medida acordada para corregir un hallazgo, con un responsable y un plazo. Un reemplazo es la persona designada para cumplir una función si la titular no está.",
        "Para analizar el informe se comparan los resultados con la meta y se calcula el cumplimiento: por ejemplo, si 3 de 4 personas cumplen, el cumplimiento es 75 %. Un resultado que no cumple la meta no se disimula: se anota tal cual y se propone una mejora. Por ejemplo, un equipo en mal estado se retira de uso, se informa al responsable y se repone por personal autorizado.",
        f"Esta clase solo analiza un informe en papel; los simulacros reales los conducen personas formadas, con instructor autorizado y la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("informe de simulacro", "registro de lo planificado, lo ocurrido y lo que se debe mejorar"), ("hallazgo", "hecho observado que muestra una falla o algo por mejorar"), ("acción de mejora", "medida acordada para corregir un hallazgo, con responsable y plazo"), ("reemplazo", "persona designada para cumplir una función si la titular no está"), ("cumplimiento", "porcentaje de lo esperado que se logró")],
    worked=[
        ("Calcular un cumplimiento", "En un simulacro de ejemplo, 8 de 10 personas llegaron con su chaleco. ¿Cuál es el cumplimiento?", ["Se multiplica 8 por 100: 800.", "800 dividido en 10 es 80."], "80 %"),
        ("Proponer una mejora", "Un informe de ejemplo muestra que una función no tiene reemplazo. ¿Qué acción de mejora corresponde?", ["El hallazgo es la falta de reemplazo.", "La mejora es designar un reemplazo en el cuadro de obligaciones."], "Designar un reemplazo con responsable y plazo"),
    ],
    mistakes=[("Anotar que se cumplió la meta aunque el tiempo fue mayor, para no preocupar.", "Un informe que oculta resultados impide mejorar.", "Se anota el resultado real y se propone una mejora."),
              ("Dejar un equipo en mal estado junto a los demás «por si falta».", "Un equipo defectuoso puede fallar justo cuando se necesita.", "Se retira de uso, se informa al responsable y se repone por personal autorizado.")],
    T=[
        ("abc", "En Pesquería: ¿qué es un simulacro de emergencia?", "Una práctica planificada y registrada para comprobar si el plan funciona", "Una emergencia real que se anota después", "Un permiso para zarpar", "El simulacro es una práctica, no una emergencia real ni un permiso."),
        ("abc", "En Pesquería: ¿qué es un hallazgo en el informe de un simulacro?", "Un hecho observado que muestra una falla o algo por mejorar", "El premio que recibe la tripulación", "La lista de todas las personas a bordo", "Un hallazgo es una observación útil para mejorar."),
        ("abc", "En Pesquería: ¿qué es una acción de mejora?", "Una medida acordada para corregir un hallazgo, con responsable y plazo", "Una anotación que borra el hallazgo del informe", "Un cambio de nombre del plan de emergencia", "La acción de mejora corrige; no borra ni renombra."),
        ("=", "{F} ¿Cuántas personas no tienen función asignada en el cuadro?", "8-4", "Se resta a las personas a bordo las que tienen función.", " personas"),
        ("=", "{F} ¿Cuántos minutos se pasó el tiempo del simulacro respecto de la meta?", "7-5", "Se resta la meta del tiempo real.", " minutos"),
        ("=", "{F} ¿Qué porcentaje de las personas tenía el chaleco puesto al final del simulacro?", "6*100//8", "Se multiplican por 100 las personas con chaleco y se dividen entre el total.", " %"),
        ("abc", "{F} ¿Qué hallazgo muestra una falla del cuadro de obligaciones?", "La función de aviso por radio no tenía reemplazo cuando la titular estaba fuera de turno", "Que haya 8 personas a bordo", "Que la meta sea de 5 minutos", "Sin reemplazo, la función se pierde si la titular no está."),
        ("abc", "{F} ¿Qué corresponde hacer con el chaleco de la correa cortada?", "Retirarlo de uso, informar al responsable y reponerlo por personal autorizado", "Dejarlo en el cajón por si faltan chalecos", "Anudar la correa y contarlo como válido", "Un equipo defectuoso no se cuenta como disponible."),
        ("abc", "{F} Se propone asignar a las cuatro personas sin función la misma tarea de aviso por radio. ¿Qué es mejor?", "Darles funciones distintas y definir reemplazos en el cuadro", "Dejarlas sin función para que no estorben", "Asignarles a todas la misma función", "Funciones distintas y reemplazos hacen más robusto el plan."),
        ("abc", "{F} Un compañero dice que, como todos llegaron, el simulacro fue bueno. ¿Qué respuesta es correcta?", "Es incompleto: tardaron más que la meta, solo 6 de 8 tenían chaleco y hay hallazgos que corregir", "Es cierto: lo único que importa es que lleguen todos", "Es cierto si el patrón estaba presente", "Un simulacro se evalúa con la meta, el cumplimiento y los hallazgos."),
        ("abc", "{F} ¿De qué tipo es el control «cuadro de obligaciones con funciones y reemplazos»?", "Administrativo, porque ordena conductas y funciones", "De ingeniería, porque cambia la nave", "De EPP, porque protege el cuerpo", "El cuadro es un documento de organización, no un cambio físico ni un equipo personal."),
        ("=", "{F} Si se asigna a cada una de las 4 funciones un reemplazo distinto, ¿cuántas personas se necesitan para cubrir titulares y reemplazos?", "4*2", "Se multiplica el número de funciones por dos personas por función.", " personas"),
        ("abc", "{F} Alguien propone anotar en el informe que el simulacro cumplió la meta «para no preocupar a nadie». ¿Qué respondes?", "Que no: el informe debe reflejar el resultado real, y se consulta con un adulto responsable", "Que sí, porque la diferencia es solo de dos minutos", "Que sí, si se corrige en el próximo simulacro", "Un informe falso impide mejorar el plan."),
    ],
    ctx=("abc", "Un conocido te pide que escribas «sin hallazgos» en el informe de un simulacro de ejemplo para quedar bien ante una fiscalización. ¿Qué respondes?", "Que no, porque un informe debe ser veraz, y que lo consultarás con un adulto responsable o con la autoridad marítima", "Que sí, porque los hallazgos son pequeños", "Que sí, si los corriges antes de la fiscalización", "Ocultar hallazgos impide corregir fallas que pueden costar vidas."),
    sc=[
        ("En Pesquería: ¿qué es un hallazgo?", "Un hecho observado que muestra una falla o algo por mejorar", "El hallazgo orienta las mejoras del plan."),
        ("En Pesquería: ¿qué es un reemplazo en el cuadro de obligaciones?", "La persona designada para cumplir una función si la titular no está", "El reemplazo evita que una función quede sin cubrir."),
        ("En Pesquería: ¿cómo se calcula un cumplimiento?", "Lo logrado por 100, dividido por lo esperado", "El cumplimiento compara lo logrado con lo esperado."),
    ],
    op=("Informe de ejemplo: nave con 10 personas; meta de reunión de 6 minutos y resultado de 9 minutos; 7 de 10 personas con chaleco puesto; una de las funciones no tiene reemplazo; un extintor con la etiqueta de revisión vencida. Escribe (a) cuántos minutos se pasó y qué porcentaje tenía chaleco, (b) dos hallazgos, (c) una acción de mejora para cada hallazgo, (d) por qué no se altera el informe.",
        "(a) 9 − 6 = 3 minutos de más; 7 × 100 ÷ 10 = 70 %. (b) Una función sin reemplazo y un extintor con la revisión vencida. (c) Designar un reemplazo en el cuadro y pedir que personal autorizado revise o reponga el extintor. (d) Porque un informe alterado oculta fallas y impide mejorar. Los simulacros reales los conducen personas formadas.",
        ["calcula minutos y porcentaje", "identifica dos hallazgos", "propone una acción por hallazgo", "explica por qué no se altera el informe"],
        ["hoja con las cuatro respuestas"],
        ["decir que el simulacro cumplió la meta", "proponer una mejora sin responsable", "ocultar un hallazgo"],
        "Pregunta: «¿qué diferencia hay entre un hallazgo y una acción de mejora?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un informe de simulacro con tres resultados y escribe un hallazgo y una acción de mejora para cada uno.",
    extend="Explica con un ejemplo por qué un reemplazo asignado hace más seguro un plan de emergencia.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (planificación de ejemplo, inventada). «Nave Demo»; mes actual: 5. Equipos: 12 chalecos de flotación (revisión vigente); una balsa de 10 plazas (revisión vence en el mes 9) y otra de 6 plazas (revisión vence en el mes 4). "
     "Regla de ejemplo: chalecos iguales a las personas más 2 de reserva, y plazas vigentes de balsa iguales o mayores que las personas. Salida A: 6 personas. Salida B: 9 personas. Salida C: 14 personas. Costo de ejemplo de reponer un chaleco: 25.000 pesos.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar una regla de seguridad con datos: calcular chalecos y plazas necesarias, detectar faltantes y costos, y distinguir lo vigente de lo vencido.",
    prior=["Sé qué es un equipo vencido y una plaza de balsa.", "Sé sumar, restar y multiplicar números enteros.", "Sé comparar cantidades con una regla."],
    explain=[
        "Aplicar una regla de seguridad es comparar lo que hay con lo que la regla exige, para cada situación. Una reserva es una cantidad adicional que se exige por si algún equipo falla; por ejemplo, con la regla de un chaleco por persona más 3 de reserva, 5 personas necesitan 8 chalecos. Las plazas de balsa que cuentan son solo las de balsas con revisión vigente: una balsa vencida no suma.",
        "Un faltante es la diferencia entre lo exigido y lo que hay. Cuando hay un faltante, la salida no cumple la regla y se informa al patrón: no se compensa con otra cosa ni se «aprieta» a las personas. Reponer o revisar equipos lo hace personal autorizado, y el costo se estima multiplicando la cantidad por el precio de cada uno.",
        f"Todos los números son de ejemplo. Una regla real la fija la norma vigente y la fiscaliza la autoridad marítima. {EMER} {AVISO}",
    ],
    vocab=[("reserva", "cantidad adicional exigida por si algún equipo falla"), ("faltante", "diferencia entre lo exigido y lo que hay"), ("plazas vigentes", "plazas de balsas con revisión vigente"), ("regla de seguridad", "condición que se debe cumplir para que una salida sea aceptable"), ("salida", "viaje o faena de la nave")],
    worked=[
        ("Calcular lo exigido", "Una regla de ejemplo pide un chaleco por persona más 3 de reserva, y salen 7 personas. ¿Cuántos chalecos se necesitan?", ["Se suman las personas y la reserva.", "7 más 3 es 10."], "10 chalecos"),
        ("Contar plazas vigentes", "Una nave de ejemplo tiene una balsa de 8 plazas vigente y otra de 4 plazas vencida. ¿Cuántas plazas cuentan?", ["La balsa vencida no suma.", "Solo cuentan las 8 plazas vigentes."], "8 plazas"),
    ],
    mistakes=[("Contar las plazas de una balsa con la revisión vencida.", "Un equipo vencido no tiene garantía de funcionar.", "Solo se cuentan las plazas de balsas con revisión vigente."),
              ("Compensar la falta de chalecos con una balsa grande.", "Cada regla se cumple por separado.", "Se cumplen los chalecos y las plazas; si falta alguno, se informa.")],
    T=[
        ("abc", "En Pesquería: ¿qué es una reserva de chalecos?", "Chalecos adicionales a las personas, exigidos por si alguno falla", "Los chalecos que usa solo el patrón", "Los chalecos que se guardan para vender", "La reserva es un respaldo sobre el número de personas."),
        ("abc", "En Pesquería: ¿qué significa que una balsa tenga la revisión vigente?", "Que su fecha de vencimiento todavía no ha pasado", "Que la balsa es nueva", "Que la balsa tiene más plazas que otras", "Vigente quiere decir que la revisión no está vencida."),
        ("abc", "En Pesquería: ¿qué es un faltante frente a una regla de seguridad?", "La diferencia entre lo exigido y lo que hay", "La suma de todos los equipos", "El costo de reponer un equipo", "El faltante mide cuánto falta para cumplir la regla."),
        ("=", "{F} ¿Cuántos chalecos exige la regla para la salida A?", "6+2", "Se suman las personas y los chalecos de reserva.", " chalecos"),
        ("=", "{F} ¿Cuántos chalecos exige la regla para la salida C?", "14+2", "Se suman las personas y los chalecos de reserva.", " chalecos"),
        ("=", "{F} ¿Cuántos chalecos faltan para la salida C?", "14+2-12", "Se restan los chalecos que hay de los exigidos.", " chalecos"),
        ("abc", "{F} ¿Cuántas plazas de balsa cuentan hoy?", "10 plazas, porque la balsa de 6 plazas tiene la revisión vencida", "16 plazas, porque se suman las dos balsas", "6 plazas, porque es la más reciente", "La balsa de 6 plazas venció en el mes 4, anterior al mes actual."),
        ("abc", "{F} ¿Qué salida no cumple la regla de seguridad?", "La salida C, porque faltan chalecos y plazas", "La salida A, porque necesita 8 chalecos", "La salida B, porque lleva 9 personas", "A y B cumplen ambas reglas; C no."),
        ("=", "{F} ¿Cuántas plazas faltan en la salida C con las balsas vigentes?", "14-10", "Se restan las plazas vigentes de las personas a bordo.", " plazas"),
        ("abc", "{F} Un compañero dice que, si se renueva la revisión de la balsa de 6 plazas, la salida C ya cumple todo. ¿Qué respuesta es correcta?", "Es falso: las plazas alcanzarían, pero seguirían faltando 4 chalecos", "Es cierto, porque las plazas son lo único que importa", "Es cierto, porque la balsa de 6 plazas reemplaza a los chalecos", "Cada regla se cumple por separado y los chalecos seguirían faltando."),
        ("abc", "{F} ¿Quién renueva la revisión de una balsa vencida?", "Personal autorizado; hasta entonces no se cuenta con esa balsa", "Un tripulante, cambiando la fecha de la etiqueta", "El comprador del producto", "La revisión la hace personal autorizado y no se altera una etiqueta."),
        ("=", "{F} ¿Cuánto cuesta reponer los chalecos que faltan para la salida C, a precio de ejemplo?", "(14+2-12)*25000", "Se multiplican los chalecos faltantes por el costo de cada uno.", " pesos"),
        ("abc", "{F} Alguien propone zarpar en la salida C igual «porque hay buen tiempo y es corto». ¿Qué respondes?", "Que no: la regla no se cumple y se informa al patrón; el buen tiempo no reemplaza los equipos", "Que sí, si el viaje dura poco", "Que sí, si todos saben nadar", "Una regla incumplida se corrige antes de salir, sin importar el tiempo."),
    ],
    ctx=("abc", "Un conocido te dice que en su bote «siempre salen 14 personas con 6 chalecos» y que no pasa nada. ¿Qué respondes?", "Que no es seguro ni cumple la regla, y que lo consultarás con un adulto responsable o con la autoridad marítima", "Que si no ha pasado nada, está bien", "Que se arregla con un buen pronóstico", "Que no haya pasado nada no prueba que sea seguro."),
    sc=[
        ("En Pesquería: ¿cuáles plazas de balsa cuentan para una regla de seguridad?", "Solo las de balsas con revisión vigente", "Un equipo vencido no se cuenta como disponible."),
        ("En Pesquería: ¿cómo se calcula un faltante?", "Lo exigido menos lo que hay", "El faltante muestra cuánto falta para cumplir."),
        ("En Pesquería: ¿puede una regla de seguridad compensarse con otra cosa?", "No, cada regla se cumple por separado", "Los chalecos y las plazas se exigen cada uno."),
    ],
    op=("Planificación de ejemplo, mes actual 6: 9 chalecos; una balsa de 8 plazas con la revisión vigente hasta el mes 10 y otra de 4 plazas vencida en el mes 5. Regla de ejemplo: un chaleco por persona más 2 de reserva y plazas vigentes iguales o mayores que las personas. Salida con 8 personas. Costo de ejemplo de un chaleco: 20.000 pesos. Escribe (a) cuántos chalecos se exigen y cuántos faltan, (b) cuántas plazas cuentan y si alcanzan, (c) el costo de los chalecos faltantes, (d) si la salida cumple y qué haces.",
        "(a) Se exigen 8 + 2 = 10 chalecos y hay 9: falta 1. (b) Cuentan 8 plazas, porque la balsa de 4 plazas está vencida; 8 es igual a las 8 personas, así que alcanzan. (c) 1 × 20.000 = 20.000 pesos. (d) No cumple, porque falta un chaleco; se informa al patrón y se repone por personal autorizado antes de salir.",
        ["calcula los chalecos exigidos y el faltante", "cuenta solo las plazas vigentes", "calcula el costo", "concluye que no cumple e informa"],
        ["hoja con las cuatro respuestas"],
        ["sumar la balsa vencida", "olvidar la reserva", "decidir que cumple porque las plazas alcanzan"],
        "Pregunta: «¿qué balsa tiene la revisión vencida?». Si no responde, pídele que compare cada mes con el mes actual."),
    reinforce="Inventa dos salidas con distinto número de personas y comprueba si cumplen una regla de chalecos y plazas.",
    extend="Explica por qué contar una balsa vencida da una falsa sensación de seguridad.",
)

# ============================================================ OAE-05, clase 5
F = ("Ficha 5 (alternativas y lista de ejemplo, inventadas). «Nave Demo», 8 personas, mes actual: 5. Plan P: funciones escritas y difundidas, simulacro mensual (12 al año), equipos accesibles. Plan Q: funciones de memoria, un simulacro al año, equipos guardados en la bodega. "
     "Plan R: funciones escritas y difundidas, simulacro trimestral (4 al año), equipos accesibles. Cada simulacro dura 1 hora con las 8 personas; costo de ejemplo de una hora-persona: 5.000 pesos. Regla de ejemplo: funciones escritas, equipos accesibles y al menos un simulacro cada 3 meses. "
     "Lista de verificación de ejemplo: línea 1, chalecos revisados, sin firma; línea 2, señales de socorro, vencimiento mes 3, anotadas como «vigentes»; línea 3, extintores, fecha de revisión ilegible.")
build(
    O5, 5, F,
    use="Aprenderé a comparar planes de emergencia con una regla y con costos, y a verificar la calidad de una lista de verificación de equipos de seguridad.",
    prior=["Sé qué son el plan de emergencia, el simulacro y el inventario.", "Sé multiplicar y restar números enteros.", "Sé que los registros no se alteran."],
    explain=[
        "Para comparar planes de emergencia se usa primero la regla de seguridad: si un plan no la cumple, se descarta aunque sea más barato. Entre los planes que sí la cumplen se compara el costo. La hora-persona es una hora de trabajo de una persona; el costo de un simulacro es las horas por las personas por el costo de la hora-persona. Por ejemplo, 2 simulacros de 1 hora con 5 personas son 10 horas-persona.",
        "Una lista de verificación es un documento con líneas que se revisan una por una. Su calidad se verifica comprobando que cada línea esté completa, legible, veraz y firmada por su responsable. Una línea ilegible o dudosa se repite con una revisión nueva; una línea falsa, como anotar vigente un equipo vencido, es un incumplimiento grave. La verificación solo la hacen personas formadas y autorizadas.",
        f"Todos los costos y reglas son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("hora-persona", "una hora de trabajo de una persona"), ("lista de verificación", "documento con líneas que se revisan una por una"), ("regla de seguridad", "condición que debe cumplir un plan para ser aceptable"), ("línea ilegible", "anotación que no se puede leer sin dudas"), ("incumplimiento", "hecho que no cumple la norma vigente")],
    worked=[
        ("Calcular un costo", "Un plan de ejemplo hace 3 simulacros de 1 hora con 6 personas, a 4.000 pesos la hora-persona. ¿Cuánto cuesta?", ["Las horas-persona son 3 por 6, es decir, 18.", "18 por 4.000 es 72.000."], "72.000 pesos"),
        ("Descartar un plan", "Una regla de ejemplo exige equipos accesibles. Un plan guarda los equipos bajo llave en la bodega. ¿Qué corresponde?", ["El plan no cumple la regla.", "Se descarta, aunque sea más barato."], "Descartarlo: no cumple la regla"),
    ],
    mistakes=[("Elegir el plan más barato sin revisar la regla.", "Un plan que no cumple la regla no es aceptable, sea barato o no.", "Aplica la regla primero y compara costos entre los que la cumplen."),
              ("Adivinar una fecha ilegible para completar la línea.", "Una fecha adivinada es un dato inventado.", "Se pide repetir la revisión y anotar el dato legible.")],
    T=[
        ("abc", "En Pesquería: al comparar planes de emergencia, ¿qué criterio va primero?", "El cumplimiento de la regla de seguridad", "El menor costo", "La mayor cantidad de simulacros posible", "Un plan que no cumple la regla se descarta aunque sea barato."),
        ("abc", "En Pesquería: ¿qué es una lista de verificación de equipos?", "Un documento con líneas que se revisan una por una", "Un registro de los kilos capturados", "Un permiso para zarpar", "La lista de verificación se revisa línea por línea."),
        ("abc", "En Pesquería: ¿qué es una hora-persona?", "Una hora de trabajo de una persona", "Una hora de viaje de la nave", "Una hora de sueño de la tripulación", "La hora-persona mide el trabajo humano invertido."),
        ("=", "{F} ¿Cuánto cuesta al año el plan P?", "12*8*5000", "Se multiplican los simulacros por las personas y por el costo de la hora-persona.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta al año el plan R?", "4*8*5000", "Se multiplican los simulacros por las personas y por el costo de la hora-persona.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta el plan P que el plan R?", "12*8*5000-4*8*5000", "Se resta el costo anual de R del costo anual de P.", " pesos"),
        ("abc", "{F} ¿Qué plan no cumple la regla de ejemplo?", "El plan Q, porque tiene funciones de memoria, equipos en la bodega y un solo simulacro al año", "El plan P, porque hace demasiados simulacros", "El plan R, porque hace simulacros trimestrales", "P y R cumplen la regla; Q no cumple ninguno de sus tres puntos."),
        ("abc", "{F} Entre los planes que cumplen la regla, ¿cuál conviene por costo?", "El plan R: cumple la regla y cuesta menos que P", "El plan P, porque tiene más simulacros", "El plan Q, porque es el más barato", "Q se descarta, y entre P y R el más barato que cumple es R."),
        ("abc", "{F} ¿Qué error hay en la línea 2 de la lista de verificación?", "Anota como vigentes unas señales cuyo vencimiento, el mes 3, ya pasó: es un dato falso", "Que el mes de vencimiento sea el 3", "Que haya señales de socorro en la lista", "Con el mes actual en 5, un vencimiento en el mes 3 es un equipo vencido."),
        ("abc", "{F} ¿Qué falta en la línea 1 de la lista de verificación?", "La firma del responsable, que da trazabilidad a la revisión", "El nombre de la nave", "El color de los chalecos", "Sin firma no se sabe quién hizo la revisión."),
        ("abc", "{F} ¿Qué corresponde con la línea 3, de fecha ilegible?", "Pedir que la revisión se repita y se anote de forma legible, sin adivinar la fecha", "Anotar la fecha que parezca más probable", "Dejarla como está porque se entiende", "Adivinar la fecha es inventar un dato."),
        ("=", "{F} Si el costo de la hora-persona subiera a 6.000 pesos, ¿cuánto costaría al año el plan R?", "4*8*6000", "Se multiplican los simulacros por las personas y por el nuevo costo.", " pesos"),
        ("abc", "{F} Alguien dice que el plan Q basta porque «nunca ha pasado nada». ¿Qué respuesta es correcta?", "Es falso: que no haya pasado nada no prueba que el plan funcione, y la regla exige simulacros y equipos accesibles", "Es cierto: si no ha pasado nada, el plan es suficiente", "Es cierto si la nave es pequeña", "La seguridad se verifica con simulacros y equipos disponibles, no con la ausencia de accidentes."),
    ],
    ctx=("abc", "Alguien te pide anotar «vigentes» en una lista de verificación de ejemplo aunque un equipo esté vencido, para evitar una multa. ¿Qué respondes?", "Que no, porque anotar un dato falso es un incumplimiento, y que lo consultarás con un adulto responsable o con la autoridad marítima", "Que sí, si lo repones después", "Que sí, porque la multa es peor", "Un registro falso pone en riesgo vidas y agrava la falta."),
    sc=[
        ("En Pesquería: ¿cómo se calcula el costo de un plan de simulacros?", "Simulacros por personas por costo de la hora-persona", "El costo es horas-persona por su precio."),
        ("En Pesquería: ¿qué se hace con una línea ilegible?", "Se pide repetir la revisión y anotar el dato legible", "Adivinar un dato lo vuelve falso."),
        ("En Pesquería: ¿qué pasa con un plan que no cumple la regla?", "Se descarta aunque sea más barato", "La seguridad pesa más que el costo."),
    ],
    op=("Alternativas de ejemplo: plan S, funciones escritas, equipos accesibles y simulacro semestral (2 al año); plan T, funciones escritas, equipos accesibles y simulacro trimestral (4 al año). Regla de ejemplo: al menos un simulacro cada 3 meses, funciones escritas y equipos accesibles. Cada simulacro dura 1 hora con 6 personas; hora-persona de ejemplo: 4.000 pesos. Escribe (a) cuál plan no cumple y por qué, (b) el costo anual de T, (c) cuál eliges, (d) qué haces con una línea falsa de una lista de verificación.",
        "(a) El plan S, porque hace un simulacro cada 6 meses y la regla exige uno cada 3. (b) 4 × 6 × 4.000 = 96.000 pesos. (c) El plan T, porque cumple la regla. (d) Informarla a un adulto responsable o a la autoridad marítima y no anotarla ni alterarla; las verificaciones reales las hace personal autorizado.",
        ["identifica el plan que no cumple", "calcula el costo anual", "elige aplicando la regla", "responde con veracidad ante una línea falsa"],
        ["hoja con las cuatro respuestas"],
        ["elegir S por ser más barato", "calcular el costo con dos simulacros", "aceptar anotar un dato falso"],
        "Pregunta: «¿cuántos meses pasan entre los simulacros del plan S?». Si no responde, pídele que divida 12 entre 2."),
    reinforce="Inventa dos planes de emergencia con distinto número de simulacros y decide cuál conviene con una regla y un costo.",
    extend="Explica por qué la ausencia de accidentes no prueba que un plan de emergencia funcione.",
)
