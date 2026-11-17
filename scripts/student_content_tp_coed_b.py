"""Construcción, mención Edificación (4.º medio TP): OAM-03 (hormigón en obra: calidad, compactado y curado como conceptos y registros), OAM-04 (albañilería: documentos y cubicación) y OAM-05 (moldajes, tabiquería y techumbres: documentos, planillas y seguridad). Solo conceptos y planillas con datos de ejemplo."""
from __future__ import annotations

from tp_coed_common import AVISO, EMER, build

O3 = "TP-COED-4-OAM-03"
O4 = "TP-COED-4-OAM-04"
O5 = "TP-COED-4-OAM-05"
TAIL = f"{EMER} {AVISO}"

# ============================================================ OAM-03, clase 1
F = ("Ficha 1 (obra de ejemplo, inventada). Obra «Casa Lomas» (ficticia): se recibe hormigón para la losa de una vivienda. Cuadrilla de 9 personas, un jefe de obra y un prevencionista. "
     "Riesgos anotados: contacto del hormigón fresco con la piel y los ojos (irritación), atrapamiento por equipos en movimiento, caída desde bordes, ruido y polvo de cemento. "
     "Medidas anotadas: lentes, guantes impermeables, calzado de seguridad, zona delimitada, señalética y capacitación a toda la cuadrilla.")
build(
    O3, 1, F,
    use="Aprenderé qué es el hormigón, por qué su calidad depende de controles registrados y cuáles son los riesgos y los niveles de control de prevención en una obra.",
    prior=["Sé leer una ficha con datos.", "Sé sumar y multiplicar.", "Sé que en una obra cada persona tiene un rol."],
    explain=[
        "El hormigón es una mezcla de cemento, áridos (arena y grava) y agua. Al principio es una masa fresca que se puede colocar; con el tiempo se endurece y adquiere resistencia, que es la capacidad de soportar cargas sin romperse. El hormigón premezclado llega ya mezclado desde una planta; el preparado en obra se mezcla en el mismo lugar de trabajo. En ambos casos la calidad se controla con registros: documentos donde se anota qué se recibió, cuándo y qué resultados dieron las pruebas. Cómo se compacta y se cura lo fija la especificación del proyecto y lo enseña un instructor autorizado; aquí solo aprendes qué significan esos términos.",
        "Los riesgos de trabajar con hormigón fresco son la irritación de piel y ojos, el atrapamiento, las caídas y el ruido. La jerarquía de controles ordena las medidas de la más a la menos efectiva: primero eliminar el peligro, luego sustituirlo, después aplicar controles de ingeniería (barreras y protecciones colectivas), luego controles administrativos (capacitación, señalética, delimitar la zona) y, al final, los elementos de protección personal (EPP). El EPP es el último nivel porque no elimina el peligro, solo protege a quien lo usa. El prevencionista vigila las medidas y el jefe de obra decide y registra.",
        TAIL,
    ],
    vocab=[("hormigón", "mezcla de cemento, áridos y agua que se endurece"), ("hormigón premezclado", "hormigón que llega ya mezclado desde una planta"), ("resistencia", "capacidad del hormigón endurecido de soportar cargas sin romperse"), ("registro", "documento donde se anotan datos y resultados de un control"), ("jerarquía de controles", "orden de las medidas de prevención, de la más a la menos efectiva"), ("controles administrativos", "medidas como capacitación, señalética y delimitar zonas"), ("EPP", "elementos de protección personal, último nivel de control")],
    worked=[
        ("Clasificar un control", "En una obra de ejemplo se coloca una cinta y un letrero que delimitan la zona donde descarga un camión. ¿En qué nivel de la jerarquía de controles está esa medida?", ["Delimitar y señalizar son medidas de organización del trabajo.", "Corresponden a los controles administrativos."], "Controles administrativos"),
        ("Contar piezas de EPP", "Una cuadrilla de ejemplo de 5 personas recibe cada una 1 casco y 1 par de zapatos de seguridad. ¿Cuántas piezas se entregan?", ["Cada persona recibe 2 piezas.", "5 personas por 2 piezas son 10."], "10 piezas"),
    ],
    mistakes=[("Pensar que con casco y lentes ya no hace falta delimitar la zona.", "El EPP es el último nivel y no elimina el peligro.", "Combina varios niveles: delimitar, señalizar, capacitar y además usar EPP."),
              ("Creer que leer sobre el hormigón habilita para prepararlo o colocarlo.", "Esa tarea exige instructor autorizado y norma vigente.", "Usa este cuaderno para aprender conceptos y practica solo con instructor autorizado.")],
    T=[
        ("abc", "En Construcción (hormigón en obra): ¿qué materiales forman el hormigón?", "Cemento, áridos (arena y grava) y agua", "Cemento, agua y yeso", "Arena, grava y pintura", "El hormigón se compone de cemento, áridos y agua; el yeso y la pintura no son sus componentes."),
        ("abc", "Un camión trae a la obra el hormigón ya mezclado desde una planta. ¿Cómo se llama ese hormigón?", "Premezclado", "Preparado en obra", "Endurecido", "Si llega mezclado desde una planta es premezclado; el preparado en obra se mezcla en el lugar de trabajo."),
        ("abc", "En la jerarquía de controles de riesgo, ¿cuál es la primera medida que se busca?", "Eliminar el peligro", "Entregar EPP a todos", "Capacitar a la cuadrilla", "Lo más efectivo es eliminar el peligro; el EPP y la capacitación son niveles posteriores."),
        ("abc", "{F} ¿Qué medida de la ficha corresponde a controles administrativos?", "Capacitación y señalética", "Lentes y guantes impermeables", "Calzado de seguridad", "Capacitar y señalizar organizan el trabajo; lentes, guantes y calzado son EPP."),
        ("abc", "{F} ¿Qué riesgo de la ficha afecta a la piel y a los ojos?", "El contacto con el hormigón fresco", "El ruido", "La caída desde bordes", "La ficha anota irritación por contacto del hormigón fresco; el ruido y las caídas son otros riesgos."),
        ("=", "{F} Cada integrante de la cuadrilla recibe 1 par de lentes y 1 par de guantes impermeables. ¿Cuántas piezas de EPP se entregan en total?", "9*2", "Cada una de las 9 personas recibe 2 piezas de EPP.", " piezas"),
        ("=", "{F} Si cada integrante de la cuadrilla recibe 3 pares de guantes impermeables para toda la obra, ¿cuántos pares se necesitan?", "9*3", "Se multiplican las 9 personas por los 3 pares de cada una.", " pares"),
        ("abc", "{F} El prevencionista ve a una persona sin lentes cerca de la descarga. ¿Qué corresponde?", "Detener su tarea hasta que use lentes y dejar la observación registrada", "Dejarlo pasar si es solo un momento", "Anotarlo únicamente si se repite dos veces", "El EPP falta en una zona de riesgo: se corrige de inmediato y se registra la observación."),
        ("abc", "{F} Se propone entregar lentes y guantes pero no delimitar la zona. ¿Qué se responde?", "El EPP es el último nivel; además de entregarlo hay que delimitar y señalizar", "Es suficiente, porque el EPP elimina el peligro", "Es suficiente si la cuadrilla es de pocas personas", "El EPP solo protege a quien lo usa y no elimina el peligro; se combina con otros niveles."),
        ("ab", "{F} Una estudiante dice: «ya leí la ficha, así que puedo preparar y colocar hormigón en una obra». ¿Qué respuesta es correcta?", "No: leer no habilita; esa tarea exige instructor autorizado y norma vigente", "Sí: conocer los riesgos la habilita para trabajar", "La ficha solo describe riesgos y medidas; autorizarse para trabajar es un paso distinto."),
        ("abc", "¿Cuál es el orden correcto de la jerarquía de controles, de la más a la menos efectiva?", "Eliminar, sustituir, ingeniería, administrativos y EPP", "EPP, administrativos, ingeniería, sustituir y eliminar", "Administrativos, EPP, eliminar, sustituir e ingeniería", "El orden va desde eliminar el peligro hasta el EPP, que es el último nivel."),
        ("=", "{F} Para completar 1 par de lentes y 1 par de guantes por persona, la bodega tiene 6 pares de lentes y 9 pares de guantes. ¿Cuántas piezas faltan?", "9*2-(6+9)", "Se calculan las piezas necesarias y se restan las que hay en bodega.", " piezas"),
        ("abc", "{F} El jefe de obra pide registrar la falta de lentes. ¿Qué datos mínimos debe contener el registro?", "Qué faltó, dónde, quién lo detectó y la fecha", "Solo el nombre de quien lo detectó", "Solo la fecha de compra de los lentes", "Un registro útil deja constancia de qué, dónde, quién y cuándo."),
    ],
    ctx=("abc", "En una obra de ejemplo, un equipo en movimiento atrapa a un trabajador. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarse de inmediato a sacarlo por cuenta propia", "Esperar a ver si logra liberarse solo", "Acercarse sin autorización puede causar otro accidente; se avisa a quien corresponde y a emergencias."),
    sc=[
        ("En Construcción (hormigón en obra): ¿qué es la resistencia del hormigón?", "La capacidad del hormigón endurecido de soportar cargas sin romperse", "La resistencia se refiere a soportar cargas, no a la rapidez de secado."),
        ("¿En qué nivel de la jerarquía están los EPP?", "En el último nivel", "El EPP protege a la persona pero no elimina el peligro."),
        ("¿Qué se hace ante un atrapamiento o una caída en una obra?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarse sin autorización puede agravar el accidente."),
    ],
    op=("Obra de ejemplo «Taller Cumbre» (ficticia): la cuadrilla es de 7 personas y se descarga hormigón premezclado para un piso. Riesgos anotados: contacto con hormigón fresco, caída desde un borde y ruido. Medidas disponibles: lentes, guantes, barandas de protección en el borde, letreros y capacitación. Escribe (a) cuántos pares de guantes se necesitan si cada persona recibe 2 pares, (b) qué medida es de ingeniería y cuál administrativa, (c) por qué el EPP no basta y (d) qué se hace si alguien cae, sin acercarse a la zona de riesgo.",
        "(a) 7×2 son 14 pares de guantes. (b) Las barandas son controles de ingeniería; los letreros y la capacitación son administrativos. (c) El EPP es el último nivel: protege a quien lo usa pero no elimina el peligro. (d) No me acerco a la zona de riesgo, aviso a un adulto responsable y llamo a emergencias.",
        ["calcula los pares de guantes", "clasifica bien las dos medidas", "explica por qué el EPP no basta", "indica avisar sin acercarse al riesgo"],
        ["hoja con las cuatro respuestas"],
        ["decir que el EPP elimina el peligro", "confundir ingeniería con administrativo", "proponer acercarse al accidentado"],
        "Pregunta: «¿por qué el casco no reemplaza a las barandas?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe los cinco niveles de la jerarquía de controles y, junto a cada uno, un ejemplo de una obra.",
    extend="Explica con un ejemplo inventado cómo un registro de control puede evitar que una pieza de mala calidad quede escondida en una obra.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 2 (guía de despacho de ejemplo, inventada). Guía N.º 118 de la planta ficticia «Hormigones del Valle»: grado solicitado «H-ejemplo 25» (rótulo inventado); volumen 6 m³; "
     "asentamiento pedido: 10 cm (valor de ejemplo); hora de salida 09:10; hora de llegada a la obra 09:50; elemento: losa del piso 2; plazo máximo de ejemplo entre salida y llegada: 45 minutos.")
build(
    O3, 2, F,
    use="Aprenderé qué significan resistencia, trabajabilidad, probeta y registro de control y cómo se lee una guía de despacho de hormigón premezclado.",
    prior=["Sé qué es el hormigón y para qué sirven los registros.", "Sé restar horas y minutos simples.", "Sé dividir números pequeños."],
    explain=[
        "Para controlar el hormigón se usan documentos. La guía de despacho acompaña a cada camión y anota el grado solicitado, el volumen en metros cúbicos (m³), la hora de salida, la hora de llegada y el elemento que se hormigona. El grado es el rótulo que identifica la resistencia pedida. La trabajabilidad es qué tan fácil de colocar está la mezcla; el asentamiento es una medida de esa trabajabilidad, y su valor aceptable lo fija la especificación. La probeta es una muestra de hormigón fresco que se deja endurecer para probar su resistencia en un laboratorio. El resultado se anota en el registro de control.",
        "Cada persona tiene un rol: el proveedor entrega la guía, el jefe de obra la recibe y la revisa, el laboratorio informa resultados y el profesional responsable decide qué se acepta. Si algo no coincide con lo pedido, no se resuelve a criterio propio: se registra la diferencia y se informa. Nadie modifica la mezcla por su cuenta, porque eso puede cambiar la resistencia. Todos los números de este cuaderno son de ejemplo; los valores reales los fija la norma vigente y el proyecto.",
        TAIL,
    ],
    vocab=[("guía de despacho", "documento que acompaña al camión con grado, volumen y horas"), ("grado", "rótulo que identifica la resistencia pedida"), ("trabajabilidad", "qué tan fácil de colocar está la mezcla"), ("asentamiento", "medida de la trabajabilidad; su valor aceptable lo fija la especificación"), ("probeta", "muestra de hormigón fresco que se endurece para probar su resistencia en laboratorio"), ("registro de control", "documento donde se anotan los resultados de los controles")],
    worked=[
        ("Leer el volumen", "Una guía de ejemplo anota 7 m³ por camión. Llegan 2 camiones iguales. ¿Cuántos m³ llegan?", ["Se multiplica el volumen de un camión por los camiones.", "7 por 2 son 14."], "14 m³"),
        ("Interpretar un término", "Un jefe de obra de ejemplo dice: «la mezcla está muy dura de colocar». ¿Qué propiedad describe?", ["Habla de qué tan fácil o difícil es colocar la mezcla.", "Esa propiedad es la trabajabilidad."], "La trabajabilidad"),
    ],
    mistakes=[("Confundir la probeta con una pieza ya terminada de la obra.", "La probeta es una muestra pequeña hecha para probar resistencia.", "Piensa en la probeta como la muestra que representa al hormigón colocado."),
              ("Agregar agua a la mezcla para que sea más fácil de colocar.", "Cambiar la mezcla puede bajar la resistencia.", "No modifiques la mezcla: informa al responsable, que decide según la especificación.")],
    T=[
        ("abc", "En Construcción (hormigón premezclado): ¿qué es una probeta?", "Una muestra de hormigón fresco que se endurece para probar su resistencia", "El plano que dibuja los elementos de la estructura", "El camión que transporta la mezcla", "La probeta es la muestra que se prueba en laboratorio; el plano y el camión son otras cosas."),
        ("abc", "¿Qué documento acompaña a cada camión de hormigón y anota grado, volumen y horas?", "La guía de despacho", "El presupuesto de la obra", "El plano de estructura", "La guía de despacho trae los datos de cada entrega; presupuesto y plano cumplen otras funciones."),
        ("abc", "Un jefe de obra dice que la mezcla es fácil de colocar. ¿Qué propiedad describe?", "La trabajabilidad", "La resistencia", "El grado", "Qué tan fácil se coloca la mezcla es su trabajabilidad; la resistencia se mide ya endurecida."),
        ("abc", "{F} ¿Para qué elemento viene el hormigón de esta guía?", "Para la losa del piso 2", "Para la fundación", "Para un muro de contención", "La guía anota que el elemento es la losa del piso 2."),
        ("=", "{F} ¿Cuántos minutos pasaron entre la salida y la llegada del camión?", "50-10", "Se restan los minutos de la hora de salida a los de la hora de llegada.", " minutos"),
        ("abc", "{F} ¿Qué dato de la guía identifica la resistencia pedida?", "El grado «H-ejemplo 25»", "La hora de salida", "El número de guía", "El grado es el rótulo de la resistencia pedida; la hora y el número no la indican."),
        ("=", "{F} La losa necesita 24 m³ y cada camión trae el volumen de la guía. ¿Cuántos camiones se necesitan?", "24//6", "Se divide el volumen total por el volumen de cada camión.", " camiones"),
        ("ab", "{F} Se compara el tiempo entre salida y llegada con el plazo de ejemplo de la guía. ¿Qué conclusión es correcta?", "Cumple: 40 minutos no superan los 45 del plazo", "No cumple: 40 minutos superan el plazo de 45", "El tiempo transcurrido es de 40 minutos y el plazo máximo de ejemplo es de 45."),
        ("abc", "El laboratorio informa que las probetas dieron menos resistencia que la pedida. ¿A quién se informa primero?", "Al jefe de obra o al profesional responsable", "A nadie hasta que termine la obra", "Solo al proveedor de pinturas", "El resultado se comunica a quien decide qué se acepta, sin esperar al final."),
        ("abc", "Llega un camión cuya guía dice un grado distinto del pedido. ¿Qué corresponde?", "Registrar la diferencia e informar al responsable antes de recibirlo", "Recibirlo igual y avisar después", "Elegir el grado que parezca más conveniente", "Una diferencia de grado no se decide por cuenta propia: se registra e informa."),
        ("ab", "Un compañero dice: «agreguemos agua al camión para que la mezcla fluya mejor». ¿Qué respuesta es correcta?", "No: cambiar la mezcla puede bajar la resistencia y solo lo decide el responsable", "Sí: más agua siempre mejora el hormigón", "Alterar la mezcla puede cambiar su resistencia; esa decisión no es de quien descarga."),
        ("=", "{F} Si el tráfico retrasa el camión 12 minutos más, ¿cuántos minutos pasan entre salida y llegada?", "(50-10)+12", "Se suma el retraso al tiempo original entre salida y llegada.", " minutos"),
        ("abc", "{F} Con ese retraso de 12 minutos, ¿qué se hace con la guía?", "Anotar el tiempo real e informar que supera el plazo de ejemplo", "Corregir la hora de llegada para que cumpla", "Ignorar el plazo si la mezcla se ve bien", "Los tiempos se registran como ocurrieron; alterar una hora falsifica el registro."),
    ],
    ctx=("abc", "En una obra de ejemplo, un camión descarga cerca de un borde sin protección y un trabajador se acerca a mirar. ¿Qué corresponde?", "Alejarse de la zona de riesgo y avisar al prevencionista", "Acercarse más para ver mejor la descarga", "Subirse al borde para ayudar sin autorización", "La zona de descarga es de riesgo: se mantiene la distancia y se avisa a quien vigila la prevención."),
    sc=[
        ("En Construcción (hormigón premezclado): ¿qué es el grado?", "El rótulo que identifica la resistencia pedida", "El grado nombra la resistencia solicitada, no el tamaño del camión."),
        ("¿Qué se hace si una guía no coincide con lo pedido?", "Registrar la diferencia e informar al responsable", "Nadie decide por cuenta propia cuando los documentos no coinciden."),
        ("¿Quién decide qué se acepta cuando un resultado de laboratorio es bajo?", "El profesional responsable", "La decisión corresponde a quien tiene la responsabilidad técnica."),
    ],
    op=("Guía de ejemplo N.º 42: grado «H-ejemplo 20»; volumen 5 m³; salida 14:20; llegada 14:50; elemento: sobrecimiento; plazo de ejemplo: 40 minutos. El proyecto pedía grado «H-ejemplo 25». Escribe (a) cuántos minutos pasaron y si cumple el plazo de ejemplo, (b) qué diferencia hay con lo pedido, (c) a quién informas y qué registras y (d) por qué no se corrige la mezcla en el lugar.",
        "(a) 30 minutos; cumple porque no supera los 40. (b) El grado es 20 y se pidió 25. (c) Informo al jefe de obra o al profesional responsable y registro la diferencia con el número de guía y la fecha. (d) Cambiar la mezcla puede alterar la resistencia y esa decisión es del responsable.",
        ["calcula los minutos y compara con el plazo", "detecta la diferencia de grado", "informa al responsable y registra", "explica por qué no se modifica la mezcla"],
        ["hoja con las cuatro respuestas"],
        ["decidir recibir sin informar", "restar mal las horas", "proponer agregar agua"],
        "Pregunta: «¿qué datos anotarías en el registro?». Si no responde, pídele que mencione número de guía, diferencia y fecha."),
    reinforce="Escribe seis palabras de esta clase (guía, grado, trabajabilidad, asentamiento, probeta, registro) con una frase propia para cada una.",
    extend="Inventa una guía de despacho con cinco datos y escribe una pregunta que alguien podría responder leyéndola.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 3 (registro de control de ejemplo, inventado). Obra «Edificio Alameda» (ficticia): resultados de 4 probetas de un mismo elemento, en unidades de ejemplo: P1 = 27; P2 = 24; P3 = 30; P4 = 27. "
     "Resistencia especificada de ejemplo: 25. Regla de ejemplo del caso: el promedio debe ser igual o mayor que la especificada y ninguna probeta puede quedar bajo 22.")
build(
    O3, 3, F,
    use="Aprenderé a analizar en papel un registro de resultados de probetas y a decidir a quién informar según una regla de ejemplo.",
    prior=["Sé calcular un promedio de pocos datos.", "Sé comparar números.", "Sé que los resultados se informan al responsable."],
    explain=[
        "Un registro de control reúne los resultados de las probetas de un elemento. Para analizarlo se calcula el promedio, que es la suma de los resultados dividida por la cantidad de probetas, y se compara cada resultado con la regla del caso. La especificación es el valor mínimo que pide el proyecto; la regla de aceptación dice cómo se compara. En el mundo real la regla y los valores los fija la norma vigente: aquí se usa una regla de ejemplo solo para practicar el análisis en papel.",
        "El analista no decide por sí solo si una parte de la obra se acepta. Su tarea es calcular bien, anotar qué cumple y qué no, y entregar el registro al profesional responsable. Si un resultado queda fuera de la regla, se deja constancia con el número de probeta, el valor y la fecha, y se informa. Nunca se cambia un número para que el registro «cumpla».",
        TAIL,
    ],
    vocab=[("promedio", "suma de los resultados dividida por la cantidad de datos"), ("resistencia especificada", "valor mínimo pedido por el proyecto"), ("regla de aceptación", "condición con que se comparan los resultados"), ("constancia", "anotación escrita de lo observado"), ("analista", "persona que calcula y revisa los resultados del registro")],
    worked=[
        ("Calcular un promedio", "Un registro de ejemplo trae tres resultados: 31, 33 y 35. ¿Cuál es el promedio?", ["Se suman: 31 más 33 más 35 son 99.", "99 dividido en 3 es 33."], "33"),
        ("Aplicar una regla", "Regla de ejemplo: ninguna probeta bajo 20. Un registro de ejemplo trae 22, 19 y 25. ¿Cumple?", ["Se busca el resultado más bajo: 19.", "19 está bajo 20, por lo que no cumple."], "No cumple: una probeta quedó bajo 20"),
    ],
    mistakes=[("Calcular el promedio dividiendo por 3 cuando hay 4 probetas.", "Se divide por la cantidad real de datos.", "Cuenta primero las probetas del registro y luego divide."),
              ("Corregir un resultado bajo para que el registro cumpla.", "Alterar un registro oculta un problema de calidad.", "Anota el valor real y entrega el registro al responsable.")],
    T=[
        ("abc", "En Construcción (calidad del hormigón): ¿qué es la resistencia especificada?", "El valor mínimo de resistencia que pide el proyecto", "El valor más alto que se puede medir", "La cantidad de probetas del registro", "Es el mínimo pedido por el proyecto; no es un máximo ni una cantidad de muestras."),
        ("abc", "En el control de probetas: ¿cómo se calcula el promedio de varios resultados?", "Se suman los resultados y se divide por la cantidad de datos", "Se elige el resultado más alto", "Se suman los resultados sin dividir", "El promedio es la suma dividida por la cantidad de datos."),
        ("abc", "Un resultado queda fuera de la regla de aceptación. ¿Qué hace el analista?", "Dejar constancia con probeta, valor y fecha, e informar al responsable", "Cambiar el número para que el registro cumpla", "Guardar el registro sin avisar", "El analista informa lo que ve; nunca altera un dato ni lo oculta."),
        ("=", "{F} ¿Cuál es la suma de los resultados de las 4 probetas?", "27+24+30+27", "Se suman los cuatro resultados del registro.", ""),
        ("=", "{F} ¿Cuál es el promedio de las 4 probetas?", "(27+24+30+27)//4", "La suma de los cuatro resultados se divide por 4.", ""),
        ("abc", "{F} ¿Qué probeta tiene el resultado más bajo?", "P2", "P1", "P3", "P2 vale 24, menor que los 27 y 30 de las demás."),
        ("abc", "{F} Según la regla de ejemplo, ¿cumple el promedio con la resistencia especificada?", "Sí: el promedio, 27, es mayor que 25", "No: el promedio es menor que 25", "No se puede saber sin una quinta probeta", "El promedio es 27 y la especificada es 25; 27 es mayor, por lo que cumple en esa parte."),
        ("abc", "{F} ¿Cuántas probetas quedaron bajo la resistencia especificada?", "Una: P2", "Dos: P1 y P4", "Ninguna", "Solo P2, con 24, está bajo 25; P1 y P4 valen 27."),
        ("ab", "{F} Aplicando las dos condiciones de la regla de ejemplo, ¿cuál es la conclusión?", "Cumple: el promedio es suficiente y ninguna probeta bajó de 22", "No cumple: P2 está bajo 25 y eso la descarta", "La regla pide promedio suficiente y ninguna probeta bajo 22; P2 vale 24."),
        ("abc", "{F} Si P2 hubiera dado 21, ¿qué conclusión sale con la regla de ejemplo?", "No cumple, porque una probeta quedó bajo 22", "Cumple, porque el promedio sigue alto", "Se descarta P2 y se calcula con tres", "La regla exige que ninguna probeta baje de 22; un 21 la incumple aunque el promedio sea alto."),
        ("=", "{F} Si P2 hubiera dado 21 y las otras tres siguieran igual, ¿cuál sería la suma de las cuatro?", "27+21+30+27", "Se reemplaza el valor de P2 y se vuelve a sumar.", ""),
        ("abc", "{F} Un compañero propone borrar P2 del registro porque «baja el promedio». ¿Qué corresponde?", "No borrarla: todos los resultados se registran y se informan", "Borrarla si el resto cumple", "Borrarla si el jefe de obra no está", "Quitar un resultado esconde información; el registro debe ser completo."),
        ("abc", "{F} El jefe de obra pide una constancia sobre P2. ¿Qué incluye?", "Probeta P2, su valor 24, la regla usada y la fecha", "Solo la palabra «mala»", "El promedio de otra obra", "La constancia deja los datos concretos: probeta, valor, regla y fecha."),
    ],
    ctx=("abc", "En una obra de ejemplo, una persona resbala y cae cerca de un borde mientras todos miran el registro. ¿Qué corresponde?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarse a moverla de inmediato", "Seguir con el registro y avisar al final", "Ante una caída no se improvisa: se evita otro accidente y se avisa a quien corresponde y a emergencias."),
    sc=[
        ("En edificación: ¿cómo se calcula un promedio?", "Sumando los datos y dividiendo por la cantidad de datos", "El promedio reparte la suma entre la cantidad de datos."),
        ("En Construcción (calidad del hormigón): ¿se puede borrar un resultado bajo del registro?", "No, todos los resultados se registran", "Borrar datos oculta un posible problema de calidad."),
        ("¿Quién decide si una parte de la obra se acepta?", "El profesional responsable", "El analista calcula e informa; la decisión es de quien tiene la responsabilidad técnica."),
    ],
    op=("Registro de ejemplo de la obra «Bodega Norte» (ficticia): 5 probetas con resultados de ejemplo Q1 = 30; Q2 = 28; Q3 = 26; Q4 = 32; Q5 = 29. Especificada de ejemplo: 28. Regla de ejemplo: promedio igual o mayor que la especificada y ninguna probeta bajo 25. Escribe (a) la suma, (b) el promedio, (c) si cumple la regla y por qué y (d) a quién entregas el registro.",
        "(a) 30+28+26+32+29 = 145. (b) 145 dividido en 5 es 29. (c) Cumple: el promedio 29 es mayor que 28 y la probeta más baja, 26, no baja de 25. (d) Al profesional responsable, que decide si se acepta.",
        ["suma bien los cinco datos", "divide por 5", "aplica las dos condiciones", "entrega al responsable"],
        ["hoja con los cálculos y la conclusión"],
        ["dividir por otro número", "revisar solo el promedio", "decidir la aceptación sin informar"],
        "Pregunta: «¿cuál es la probeta más baja y está bajo el límite?». Si no responde, pídele que ordene los datos de menor a mayor."),
    reinforce="Inventa un registro de cuatro resultados, calcula el promedio y escribe si cumple una regla que tú definas.",
    extend="Explica por qué es peligroso que alguien cambie un número de un registro para que «cumpla».",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 4 (cubicación de ejemplo, inventada). Obra «Centro Pinar» (ficticia): una losa rectangular de 10 m de largo, 5 m de ancho y 20 cm de espesor. "
     "Se agrega una pérdida de ejemplo del 10 % sobre el volumen. Los camiones premezclados de la planta ficticia traen 6 m³ cada uno. Precio de ejemplo: $90.000 por m³ de hormigón.")
build(
    O3, 4, F,
    use="Aprenderé a calcular en papel el volumen de un elemento, a agregar una pérdida y a estimar camiones y costo con datos de ejemplo.",
    prior=["Sé multiplicar largo, ancho y alto.", "Sé pasar centímetros a metros.", "Sé calcular un porcentaje simple."],
    explain=[
        "Cubicar es calcular el volumen de un elemento para saber cuánto material se necesita. El volumen de un prisma rectangular es largo por ancho por alto, y se expresa en metros cúbicos (m³). Si una medida viene en centímetros se pasa a metros dividiendo por 100: 50 cm son 0,5 m, por eso conviene multiplicar primero y dividir por 100 al final. A la cantidad calculada se le suma una pérdida, un porcentaje de ejemplo por material que se derrama o queda en equipos.",
        "Con el volumen total se estima cuántos camiones se necesitan dividiendo por lo que trae cada uno, y se calcula el costo multiplicando por el precio por m³. Estos son cálculos de planilla con números de ejemplo: no son una dosificación ni una instrucción de trabajo. El pedido real lo hace el profesional responsable según el proyecto y la norma vigente.",
        TAIL,
    ],
    vocab=[("cubicar", "calcular el volumen de un elemento"), ("m³", "metro cúbico, unidad de volumen"), ("pérdida", "porcentaje de ejemplo que se suma por material que no llega a su destino"), ("planilla", "tabla escrita donde se ordenan cálculos y datos"), ("pedido", "solicitud de material a un proveedor")],
    worked=[
        ("Volumen de una zapata", "Una zapata de ejemplo mide 2 m de largo, 2 m de ancho y 50 cm de espesor. ¿Cuántos m³ tiene?", ["Se multiplican 2 por 2 por 50 y se divide por 100.", "2 por 2 por 50 son 200; 200 dividido en 100 es 2."], "2 m³"),
        ("Agregar la pérdida", "Un elemento de ejemplo necesita 20 m³ y se agrega una pérdida del 10 %. ¿Cuántos m³ se piden?", ["El 10 % de 20 es 2.", "20 más 2 son 22."], "22 m³"),
    ],
    mistakes=[("Multiplicar 10 × 5 × 20 y dar el resultado como m³ sin dividir por 100.", "El espesor está en centímetros y el resultado sería 100 veces mayor.", "Pasa los centímetros a metros: divide por 100."),
              ("Sumar la pérdida antes de calcular el volumen.", "La pérdida se aplica sobre el volumen ya calculado.", "Calcula el volumen y después suma el porcentaje.")],
    T=[
        ("abc", "En Construcción (cubicación): ¿qué significa cubicar un elemento?", "Calcular su volumen para saber cuánto material se necesita", "Pintarlo con tres capas", "Medir su peso en una balanza", "Cubicar es calcular volumen; no es pintar ni pesar."),
        ("abc", "¿Cómo se pasan 80 cm a metros?", "Dividiendo por 100", "Multiplicando por 100", "Sumando 100", "Un metro tiene 100 cm, por lo que se divide por 100."),
        ("abc", "¿Qué unidad se usa para el volumen de hormigón de un elemento?", "Metro cúbico (m³)", "Metro cuadrado (m²)", "Metro lineal (m)", "El volumen se mide en m³; los m² son superficies y los metros lineales, longitudes."),
        ("=", "{F} ¿Cuántos m³ tiene la losa?", "10*5*20//100", "Se multiplican largo, ancho y espesor en cm y se divide por 100.", " m³"),
        ("=", "{F} Si el volumen de la losa es 10 m³, ¿cuántos m³ son la pérdida de ejemplo del 10 %?", "10*10//100", "Se calcula el 10 % de 10 m³.", " m³"),
        ("abc", "{F} ¿Qué se suma al volumen de la losa para pedir hormigón?", "La pérdida de ejemplo del 10 %", "El precio por m³", "La capacidad del camión", "La pérdida se suma al volumen; el precio y la capacidad se usan después."),
        ("=", "{F} ¿Cuántos m³ se piden en total, con la pérdida?", "10+10*10//100", "Al volumen de la losa se suma el 10 % de pérdida.", " m³"),
        ("=", "{F} Con el pedido total, ¿cuánto cuesta el hormigón al precio de ejemplo?", "(10+10*10//100)*90000", "Se multiplica el volumen pedido por el precio por m³.", " pesos"),
        ("ab", "{F} El pedido total es 11 m³ y el proveedor despacha solo camiones completos de 6 m³. ¿Cuál es la conclusión?", "Con 2 camiones llegan 12 m³ y alcanzan; con 1 solo faltarían", "Con 1 camión de 6 m³ alcanza para los 11 m³", "Dos camiones traen 12 m³, que es más que 11; uno trae 6, que es menos."),
        ("abc", "{F} Una compañera calculó 1.000 m³ para la losa. ¿Qué error pudo cometer?", "No dividió por 100 los centímetros del espesor", "Dividió por 100 dos veces", "Sumó las medidas en lugar de multiplicar", "10 × 5 × 20 da 1.000; sin dividir por 100 el espesor queda en cm."),
        ("abc", "Un compañero dice: «este cálculo ya sirve para preparar la mezcla en obra». ¿Qué respuesta es correcta?", "No: es un cálculo de planilla de ejemplo; el pedido y la mezcla los define el responsable con la norma vigente", "Sí: con el volumen ya se puede mezclar", "Sí, si se compra cemento extra", "Este cuaderno calcula volúmenes de ejemplo; no define mezclas ni habilita para prepararlas."),
        ("=", "{F} Si la losa tuviera 30 cm de espesor, con el mismo largo y ancho, ¿cuántos m³ tendría?", "10*5*30//100", "Se reemplaza el espesor por 30 cm y se vuelve a calcular.", " m³"),
        ("=", "{F} Si el precio de ejemplo subiera a $100.000 por m³, ¿cuánto costarían los 11 m³ del pedido?", "11*100000", "Se multiplica el volumen del pedido por el nuevo precio.", " pesos"),
    ],
    ctx=("abc", "Una persona de ejemplo, calculando una planilla en la obra, se sube a un andamio sin barandas para medir un borde. ¿Qué corresponde?", "Bajar, no trabajar en altura sin autorización y avisar al prevencionista", "Seguir midiendo con cuidado", "Pedir que alguien sostenga el andamio", "El trabajo en altura exige personal autorizado y protecciones; se baja y se avisa."),
    sc=[
        ("¿Cómo se calcula el volumen de un elemento rectangular?", "Largo por ancho por alto", "El volumen de un prisma rectangular es el producto de sus tres medidas."),
        ("¿Para qué se agrega una pérdida al volumen?", "Porque parte del material no llega a su destino", "La pérdida cubre el material que se derrama o queda en equipos."),
        ("En Construcción (cubicación): ¿quién hace el pedido real a la planta?", "El profesional responsable, según el proyecto y la norma vigente", "El cálculo del cuaderno es de ejemplo y no reemplaza esa decisión."),
    ],
    op=("Elemento de ejemplo: una losa de 8 m de largo, 5 m de ancho y 25 cm de espesor, con pérdida de ejemplo del 10 %. Camiones de 6 m³; precio de ejemplo $80.000 por m³. Escribe (a) el volumen en m³, (b) la pérdida, (c) el volumen del pedido, (d) el costo del pedido y (e) por qué es un cálculo de ejemplo.",
        "(a) 8×5×25 = 1.000; 1.000 dividido en 100 son 10 m³. (b) El 10 % de 10 es 1 m³. (c) 11 m³ de pedido. (d) 11 por 80.000 son 880.000 pesos. (e) Los datos son de ejemplo; el pedido real lo define el profesional responsable con la norma vigente.",
        ["calcula el volumen con los cm bien pasados", "calcula la pérdida", "suma la pérdida al volumen", "calcula el costo", "explica que son datos de ejemplo"],
        ["hoja con cálculos y conclusión"],
        ["no dividir por 100", "aplicar la pérdida antes del volumen", "tratar el cálculo como orden de mezcla"],
        "Pregunta: «¿por qué el espesor se divide por 100?». Si no responde, pídele que relea cómo se pasan los centímetros a metros."),
    reinforce="Calcula el volumen de un elemento de 4 m, 3 m y 10 cm de espesor (datos de ejemplo) y agrégale una pérdida de 10 %.",
    extend="Explica por qué un error al pasar centímetros a metros puede multiplicar el pedido por 100.",
)

# ============================================================ OAM-04, clase 1
F = ("Ficha 5 (obra de ejemplo, inventada). Obra «Pasaje Los Aromos» (ficticia): se levanta un muro de albañilería con unidades de arcilla. Cuadrilla de 6 personas. "
     "Riesgos anotados: desplome de un muro recién levantado, caída de materiales, cortes con unidades quebradas, polvo y esfuerzo al levantar cargas. "
     "Medidas anotadas: delimitar la zona al pie del muro, no apilar materiales en los bordes, casco, guantes, lentes y mascarilla, y capacitación sobre manejo manual de cargas. "
     "Descarga del día: 12 paquetes de unidades; cada pallet de ejemplo admite 4 paquetes.")
build(
    O4, 1, F,
    use="Aprenderé qué es la albañilería estructural y no estructural, qué riesgos tiene y qué medidas de prevención y roles aparecen en una obra de muros.",
    prior=["Sé qué es la jerarquía de controles.", "Sé multiplicar y dividir números pequeños.", "Sé leer una ficha de obra."],
    explain=[
        "La albañilería es la construcción de muros con unidades, como ladrillos o bloques, unidas con mortero. El mortero es una mezcla de cemento, arena y agua que une las unidades. La albañilería estructural forma muros que soportan las cargas de la construcción; la no estructural forma cierres y divisiones que solo se sostienen a sí mismos. Saber cuál es cuál importa, porque la estructural exige más control y la define el proyecto de estructura. Las proporciones de la mezcla y la forma de colocar las unidades las fija la especificación y las enseña un instructor autorizado; este cuaderno no las incluye.",
        "Los riesgos más comunes son el desplome de un muro recién levantado, la caída de materiales, los cortes, el polvo y el esfuerzo por cargas pesadas. El manejo manual de cargas es el levantamiento y traslado de pesos con el cuerpo; su límite lo fija la norma vigente. Se previene con la jerarquía de controles: eliminar o reducir el peligro, proteger con barreras, organizar el trabajo (delimitar, señalizar, capacitar) y, al final, usar EPP. El jefe de obra organiza, el prevencionista vigila y la inspección técnica de obra revisa que se cumpla el proyecto.",
        TAIL,
    ],
    vocab=[("albañilería", "construcción de muros con unidades como ladrillos o bloques unidas con mortero"), ("mortero", "mezcla de cemento, arena y agua que une las unidades de un muro"), ("albañilería estructural", "la que forma muros que soportan cargas de la construcción"), ("albañilería no estructural", "la que forma cierres y divisiones que solo se sostienen a sí mismos"), ("manejo manual de cargas", "levantamiento y traslado de pesos con el cuerpo"), ("inspección técnica de obra", "revisión del cumplimiento del proyecto por un profesional")],
    worked=[
        ("Clasificar un muro", "Un muro de ejemplo separa dos bodegas y solo se sostiene a sí mismo. ¿Es albañilería estructural o no estructural?", ["No soporta cargas de la construcción.", "Es una división: albañilería no estructural."], "No estructural"),
        ("Contar pallets", "Se descargan 10 paquetes de unidades y cada pallet de ejemplo admite 5 paquetes. ¿Cuántos pallets se necesitan?", ["Se dividen los paquetes por los que caben en cada pallet.", "10 dividido en 5 son 2."], "2 pallets"),
    ],
    mistakes=[("Apilar unidades al borde de un muro nuevo para tenerlas a mano.", "El peso y el movimiento pueden provocar caídas o desplomes.", "Mantén los materiales a la distancia que fije el plan de prevención."),
              ("Creer que la mezcla se «mide a ojo» porque se ve fácil.", "Las proporciones afectan la resistencia y las fija la especificación.", "Este cuaderno no enseña dosificaciones: eso lo hace un instructor autorizado con la norma vigente.")],
    T=[
        ("abc", "En Construcción (albañilería): ¿qué es el mortero?", "Una mezcla de cemento, arena y agua que une las unidades de un muro", "Un tipo de ladrillo muy resistente", "El plano que dibuja la hilera de ladrillos", "El mortero es la mezcla que une las unidades; no es una unidad ni un plano."),
        ("abc", "¿Qué diferencia a la albañilería estructural de la no estructural?", "La estructural forma muros que soportan cargas de la construcción", "La estructural usa solo bloques de cemento", "La no estructural no necesita plano", "La diferencia está en si el muro soporta cargas; el material o el plano no la definen."),
        ("abc", "¿Qué es el manejo manual de cargas?", "El levantamiento y traslado de pesos con el cuerpo", "El uso de una grúa para elevar paquetes", "El conteo de paquetes recibidos", "Manejo manual significa que lo hace la persona con su cuerpo, sin máquina."),
        ("abc", "{F} ¿Qué medida de la ficha organiza el trabajo y es de tipo administrativo?", "Delimitar la zona al pie del muro y capacitar sobre cargas", "Usar casco y guantes", "Usar mascarilla y lentes", "Delimitar y capacitar organizan el trabajo; casco, guantes, mascarilla y lentes son EPP."),
        ("abc", "{F} ¿Cuál de estos es un riesgo anotado en la ficha?", "El desplome de un muro recién levantado", "El incendio de una bodega", "La falta de agua potable", "La ficha anota el desplome de un muro nuevo; las otras opciones no aparecen."),
        ("=", "{F} ¿Cuántos pallets se necesitan para los paquetes del día?", "12//4", "Se divide el total de paquetes por los paquetes de cada pallet.", " pallets"),
        ("=", "{F} Cada integrante de la cuadrilla recibe 4 piezas de EPP (casco, guantes, lentes y mascarilla). ¿Cuántas piezas se entregan?", "6*4", "Se multiplican las 6 personas por las 4 piezas de cada una.", " piezas"),
        ("abc", "{F} Una persona propone apilar unidades en el borde del muro para ahorrar tiempo. ¿Qué corresponde?", "No hacerlo: la ficha prohíbe apilar materiales en los bordes", "Hacerlo si son pocas unidades", "Hacerlo si trabaja más rápido", "La ficha anota no apilar materiales en los bordes por riesgo de caída."),
        ("abc", "{F} Un integrante del equipo siente dolor de espalda tras trasladar paquetes. ¿Qué corresponde?", "Avisar al jefe de obra o al prevencionista y repasar la capacitación sobre cargas", "Seguir cargando para no atrasar", "Cambiar de turno sin avisar a nadie", "El dolor se informa y se corrige la forma de organizar el trabajo."),
        ("ab", "{F} Un compañero dice: «con la mascarilla ya no necesito delimitar la zona del muro». ¿Qué es correcto?", "No: la mascarilla es EPP y no protege del desplome; hay que delimitar", "Sí: la mascarilla evita todo riesgo del muro", "La mascarilla protege del polvo; el desplome se previene con otras medidas."),
        ("abc", "{F} Un estudiante dice: «ya sé qué es el mortero, así que puedo preparar uno y levantar un muro». ¿Qué respuesta es correcta?", "No: esa tarea exige instructor autorizado y norma vigente", "Sí: con definir mortero basta", "Sí, si usa guantes y casco", "Conocer una definición no habilita; el EPP tampoco reemplaza la autorización."),
        ("=", "{F} Si llegaran 8 paquetes más que los del día, ¿cuántos pallets harían falta con ese total?", "(12+8)//4", "Se suman los paquetes y se dividen por los que caben en cada pallet.", " pallets"),
        ("abc", "Un muro de ejemplo comienza a inclinarse mientras trabajan 3 personas. ¿Qué corresponde según las reglas generales?", "Alejarse de la zona de riesgo, avisar a un adulto responsable y a emergencias", "Sujetar el muro con las manos hasta que llegue ayuda", "Terminar la hilada y luego avisar", "No se intenta detener un desplome: se evita la zona y se avisa."),
    ],
    ctx=("abc", "En una obra de ejemplo cae un paquete de unidades desde un apilado y golpea a un compañero. ¿Qué se hace?", "No acercarse al apilado inestable, avisar a un adulto responsable y a emergencias", "Subir al apilado para acomodarlo", "Mover al compañero sin saber si está herido", "Un apilado inestable puede caer otra vez; no se improvisa y se avisa a emergencias."),
    sc=[
        ("En Construcción (albañilería): ¿qué es la albañilería no estructural?", "La que forma cierres y divisiones que solo se sostienen a sí mismos", "No soporta cargas de la construcción, solo divide o cierra."),
        ("¿Para qué sirve delimitar la zona al pie de un muro?", "Para mantener a las personas lejos del riesgo de un desplome o de una caída de materiales", "Es una medida administrativa que reduce la exposición al riesgo."),
        ("¿Quién habilita a una persona para trabajar en albañilería?", "Un instructor autorizado, con la norma vigente", "Leer este cuaderno no reemplaza esa autorización."),
    ],
    op=("Obra de ejemplo «Condominio Sauce» (ficticia): se levanta un muro de cierre con una cuadrilla de 5 personas. Riesgos anotados: caída de materiales, cortes y polvo. Descarga: 15 paquetes de unidades y cada pallet admite 5 paquetes. Medidas disponibles: delimitar el pie del muro, guantes, lentes, mascarilla y capacitación. Escribe (a) cuántos pallets necesitas, (b) cuántas piezas de EPP entregas en total si cada persona recibe guantes, lentes y mascarilla, (c) cuál medida es administrativa y cuáles son EPP y (d) qué haces si cae un paquete y alguien queda herido.",
        "(a) 15 dividido en 5 son 3 pallets. (b) 5 personas por 3 piezas son 15 piezas. (c) Delimitar el pie del muro y la capacitación son administrativas; guantes, lentes y mascarilla son EPP. (d) No me acerco al apilado inestable, aviso a un adulto responsable y a emergencias.",
        ["calcula los pallets", "calcula las piezas de EPP", "clasifica las medidas", "indica avisar sin acercarse al riesgo"],
        ["hoja con las cuatro respuestas"],
        ["no dividir los paquetes por los del pallet", "llamar administrativo al EPP", "proponer mover al herido"],
        "Pregunta: «¿qué diferencia hay entre delimitar y usar guantes?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe tres riesgos de una obra de muros y, para cada uno, una medida administrativa y un EPP posible.",
    extend="Explica con un ejemplo inventado por qué un muro no estructural mal terminado puede igual ser un riesgo para las personas.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 6 (plano de elevación descrito por escrito, de ejemplo, inventado). Muro M1 de albañilería: 8 m de largo y 3 m de alto, escala 1:50. Leyenda: V = vano de ventana; P = vano de puerta. "
     "El plano dibuja 1 puerta (P1) y 2 ventanas (V1 y V2). Especificaciones de ejemplo: la altura de cada hilada, incluida la junta, es de 20 cm. Aparejo indicado: «trabado» (cada unidad apoya sobre la unión de las dos de la hilada de abajo).")
build(
    O4, 2, F,
    use="Aprenderé el vocabulario de la albañilería (hilada, junta, aparejo, vano) y cómo se leen un plano de elevación y las especificaciones de un muro.",
    prior=["Sé qué es el mortero y la albañilería estructural.", "Sé multiplicar y dividir.", "Sé pasar de cm a metros."],
    explain=[
        "El plano de elevación muestra un muro visto de frente, con sus medidas. La hilada es cada fila horizontal de unidades. La junta es el espacio entre unidades, que se rellena con mortero. El aparejo es la forma en que se disponen las unidades; en el aparejo trabado cada unidad apoya sobre la unión de las dos de la hilada inferior, y así no se alinean las juntas verticales. El vano es una abertura en el muro, como una puerta o una ventana. La escala relaciona el dibujo con la realidad; a escala 1:50, 1 cm del dibujo son 50 cm reales.",
        "Las especificaciones técnicas dicen por escrito qué unidad, qué mortero y qué terminación se usan, y qué muros son estructurales. Si el plano y las especificaciones no coinciden, no se elige uno por cuenta propia: se registra la diferencia y se informa a la inspección técnica de obra. Aquí solo se lee e interpreta; cómo se levanta un muro lo enseña un instructor autorizado.",
        TAIL,
    ],
    vocab=[("hilada", "cada fila horizontal de unidades de un muro"), ("junta", "espacio entre unidades que se rellena con mortero"), ("aparejo", "forma en que se disponen las unidades de un muro"), ("vano", "abertura de un muro, como una puerta o una ventana"), ("plano de elevación", "dibujo de un muro visto de frente con sus medidas"), ("escala", "razón entre la medida dibujada y la real")],
    worked=[
        ("Leer una escala", "En un plano de ejemplo a escala 1:20, un muro mide 30 cm dibujados. ¿Cuánto mide en la realidad, en cm?", ["A escala 1:20, 1 cm del dibujo son 20 cm reales.", "30 por 20 son 600 cm."], "600 cm"),
        ("Contar vanos", "Un plano de ejemplo dibuja 2 puertas y 3 ventanas. ¿Cuántos vanos tiene?", ["Cada puerta y cada ventana es un vano.", "2 más 3 son 5."], "5 vanos"),
    ],
    mistakes=[("Llamar «junta» a la fila completa de unidades.", "La fila horizontal es la hilada; la junta es el espacio entre unidades.", "Recuerda: hilada es la fila, junta es el espacio con mortero."),
              ("Medir el plano con regla en una copia reducida y confiar en eso.", "Una copia reducida cambia la escala.", "Usa las cotas y el rótulo del plano, no la regla.")],
    T=[
        ("abc", "En Construcción (albañilería): ¿qué es una hilada?", "Cada fila horizontal de unidades del muro", "El espacio vacío entre dos unidades", "La abertura de una ventana", "La hilada es la fila de unidades; el espacio entre ellas es la junta y la abertura es un vano."),
        ("abc", "¿Qué es un vano en un muro?", "Una abertura, como la de una puerta o una ventana", "Una fila de unidades", "El mortero que une las unidades", "Un vano es una abertura del muro; las otras opciones son hilada y mortero."),
        ("abc", "¿Qué muestra un plano de elevación de un muro?", "El muro visto de frente con sus medidas", "El muro visto desde arriba, como en una planta", "La lista de precios del muro", "La elevación es la vista frontal; la vista desde arriba es la planta."),
        ("=", "{F} ¿Cuántos vanos dibuja el plano?", "1+2", "Se suman la puerta y las dos ventanas.", " vanos"),
        ("=", "{F} A escala 1:50, ¿cuántos cm del dibujo representan el largo del muro de 8 m (800 cm)?", "800//50", "El largo real se divide por 50 para obtener el largo dibujado.", " cm"),
        ("abc", "{F} ¿Qué aparejo indica la ficha?", "Trabado", "Sin juntas", "Con juntas verticales alineadas", "La ficha indica un aparejo trabado; el alineado es lo contrario."),
        ("=", "{F} Con 20 cm por hilada y 3 m (300 cm) de altura, ¿cuántas hiladas tiene el muro?", "300//20", "La altura total se divide por la altura de cada hilada.", " hiladas"),
        ("=", "{F} ¿Cuántos m² mide el muro completo sin descontar vanos?", "8*3", "Se multiplica el largo por el alto en metros.", " m²"),
        ("abc", "{F} Las especificaciones dicen que el muro M1 es estructural y el plano lo rotula como tabique. ¿Qué corresponde?", "Registrar la diferencia e informar a la inspección técnica de obra", "Elegir el plano porque es un dibujo", "Elegir las especificaciones sin avisar", "Una contradicción entre documentos se informa; no se resuelve por cuenta propia."),
        ("abc", "{F} Un compañero dice que la ventana V1 debería ser más grande y la dibuja más grande en su copia. ¿Qué corresponde?", "No modificar el plano: cualquier cambio lo decide el proyectista", "Aceptarlo si la copia se ve mejor", "Cambiar también V2 para que coincida", "Los cambios de un plano los decide quien lo diseña, no quien lo copia."),
        ("ab", "{F} Un estudiante dice: «si dos juntas verticales quedan alineadas es lo mismo que el trabado». ¿Qué es correcto?", "No: en el trabado las juntas verticales no se alinean entre hiladas contiguas", "Sí: es lo mismo", "Trabado significa que la unidad se apoya sobre la unión de las dos de abajo."),
        ("=", "{F} Si el muro tuviera 9 m de largo y se mantienen los 3 m de alto, ¿cuántos m² mediría?", "9*3", "Se reemplaza el largo por 9 m y se multiplica por el alto.", " m²"),
        ("abc", "{F} En la copia reducida del plano un compañero midió 10 cm para el largo del muro y concluyó que mide 5 m. ¿Qué error cometió?", "Usó una regla en una copia cuya escala puede haber cambiado, en vez de las cotas", "Dividió por 1000 sin razón", "Confundió metros con litros", "Una copia reducida cambia la escala; por eso se confía en las cotas y el rótulo."),
    ],
    ctx=("abc", "Un colega de ejemplo te pide pararte sobre un muro recién levantado para señalar un vano. ¿Qué respondes?", "No: es una zona de riesgo; se señala desde un lugar seguro y se avisa al prevencionista", "Subes con cuidado porque es breve", "Subes si él sujeta el muro", "Un muro recién levantado puede ceder; no se sube."),
    sc=[
        ("En Construcción (albañilería): ¿qué es la junta?", "El espacio entre unidades que se rellena con mortero", "La junta es el espacio con mortero, no la fila."),
        ("¿Cómo se pasa de lo dibujado a lo real en un plano a escala 1:50?", "Multiplicando por 50", "La escala 1:50 indica que 1 cm del dibujo equivale a 50 cm reales."),
        ("¿Qué se hace si plano y especificaciones se contradicen?", "Registrar la diferencia e informar a la inspección técnica de obra", "Ningún documento se elige por cuenta propia cuando hay una contradicción."),
    ],
    op=("Plano de ejemplo (inventado) del muro M2: 6 m de largo, 2 m de alto (altura de hilada de ejemplo: 20 cm), 1 puerta y 3 ventanas. Las especificaciones indican 2 ventanas. Escribe (a) cuántos vanos dibuja el plano, (b) cuántas hiladas tiene el muro, (c) cuántos m² tiene sin descontar vanos y (d) qué haces con la diferencia entre plano y especificaciones.",
        "(a) 1 puerta más 3 ventanas son 4 vanos. (b) 200 cm dividido en 20 cm son 10 hiladas. (c) 6×2 son 12 m². (d) Registro la diferencia (3 ventanas en el plano y 2 en las especificaciones) y la informo a la inspección técnica de obra.",
        ["cuenta los vanos", "calcula las hiladas con cm", "calcula los m²", "informa la diferencia sin decidir"],
        ["hoja con las cuatro respuestas"],
        ["no pasar 2 m a 200 cm", "elegir un documento al azar", "no contar la puerta como vano"],
        "Pregunta: «¿cómo pasaste los metros a centímetros?». Si no responde, pídele que multiplique 2 por 100."),
    reinforce="Dibuja en tu cuaderno un muro con una puerta y una ventana y rotula hilada, junta y vano.",
    extend="Explica por qué en el aparejo trabado no se alinean las juntas verticales y por qué eso importa para un muro estructural.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 7 (planilla de muros de ejemplo, inventada). Obra «Casas del Parque» (ficticia). Muros: M1 estructural, 12 m²; M2 no estructural, 9 m²; M3 estructural, 15 m². "
     "Vanos: V1 de 2 m² en M1 y V2 de 3 m² en M3. Especificaciones de ejemplo: unidad tipo A para muros estructurales; unidad tipo B para muros no estructurales. "
     "El plano de arquitectura dibuja un muro M4 que la planilla no incluye.")
build(
    O4, 3, F,
    use="Aprenderé a revisar en papel una planilla de muros, a descontar vanos y a detectar diferencias entre la planilla, el plano y las especificaciones.",
    prior=["Sé qué es un vano y una hilada.", "Sé sumar y restar superficies.", "Sé que las diferencias entre documentos se informan."],
    explain=[
        "Una planilla de muros ordena los datos de cada muro: su nombre, si es estructural o no, su superficie y los vanos que lo cortan. La superficie bruta es el área del muro completo; la neta es la bruta menos los vanos. Revisar una planilla significa comparar sus datos con el plano y con las especificaciones para ver si faltan muros, si sobran o si el tipo de unidad no corresponde. El tipo de unidad que usa cada muro lo fijan las especificaciones.",
        "Cuando falta un muro en la planilla, o dos documentos dicen cosas distintas, la persona que revisa no inventa el dato: lo marca, lo registra y lo informa a la inspección técnica de obra. Todo número aquí es de ejemplo; el proyecto real y la norma vigente fijan los valores.",
        TAIL,
    ],
    vocab=[("planilla de muros", "tabla con nombre, tipo, superficie y vanos de cada muro"), ("superficie bruta", "área del muro completo, sin descontar vanos"), ("superficie neta", "superficie bruta menos los vanos"), ("muro estructural", "muro que soporta cargas de la construcción"), ("inspección técnica de obra", "revisión del cumplimiento del proyecto por un profesional")],
    worked=[
        ("Superficie neta", "Un muro de ejemplo tiene 20 m² brutos y un vano de 4 m². ¿Cuál es su superficie neta?", ["La neta es la bruta menos los vanos.", "20 menos 4 son 16."], "16 m²"),
        ("Elegir el tipo de unidad", "En un caso de ejemplo, las especificaciones piden unidad tipo X para muros estructurales. El muro MX es estructural. ¿Qué tipo se usa?", ["MX es estructural.", "Se aplica el tipo X de las especificaciones."], "Tipo X"),
    ],
    mistakes=[("Sumar los vanos a la superficie del muro.", "Un vano es una abertura donde no hay muro.", "Los vanos se restan de la superficie bruta."),
              ("Agregar a la planilla un muro dibujado en el plano, inventando sus datos.", "Un dato inventado puede llevar a pedidos y trabajos erróneos.", "Marca la falta e informa a la inspección técnica de obra.")],
    T=[
        ("abc", "En Construcción (albañilería): ¿cómo se calcula la superficie neta de un muro?", "Superficie bruta menos los vanos", "Superficie bruta más los vanos", "Superficie bruta dividida por los vanos", "Los vanos son aberturas, por lo que se restan de la superficie bruta."),
        ("abc", "¿Qué es la superficie bruta de un muro?", "El área del muro completo, sin descontar vanos", "El área solo de los vanos", "El largo del muro en metros", "La bruta incluye todo el paño; la neta resta las aberturas."),
        ("abc", "¿Qué documento dice qué tipo de unidad se usa en cada tipo de muro?", "Las especificaciones técnicas", "La lista de asistencia de la cuadrilla", "El libro de remuneraciones", "El tipo de unidad lo fijan las especificaciones técnicas."),
        ("=", "{F} ¿Cuál es la superficie neta de M1?", "12-2", "A la superficie bruta de M1 se le resta su vano V1.", " m²"),
        ("=", "{F} ¿Cuál es la superficie neta de M3?", "15-3", "A la superficie bruta de M3 se le resta su vano V2.", " m²"),
        ("abc", "{F} ¿Qué tipo de unidad corresponde a M2?", "Tipo B", "Tipo A", "Cualquiera, a elección de la cuadrilla", "M2 es no estructural y las especificaciones asignan el tipo B a esos muros."),
        ("=", "{F} ¿Cuál es la superficie bruta total de los tres muros de la planilla?", "12+9+15", "Se suman las superficies brutas de M1, M2 y M3.", " m²"),
        ("=", "{F} ¿Cuántos m² netos de muros estructurales hay entre M1 y M3?", "(12-2)+(15-3)", "Se suman las superficies netas de los dos muros estructurales.", " m²"),
        ("abc", "{F} El plano dibuja un muro M4 que la planilla no tiene. ¿Qué corresponde?", "Marcar la falta e informar a la inspección técnica de obra", "Inventar datos de M4 para completar", "Ignorar M4 porque la planilla manda", "Una falta se informa; los datos no se inventan ni se ignora un muro dibujado."),
        ("abc", "{F} Un revisor propone cambiar M2 a unidad tipo A «por si acaso». ¿Qué corresponde?", "No cambiar: la unidad la fija la especificación y cualquier cambio lo decide el proyectista", "Cambiar, porque es más segura", "Cambiar si es más barata", "El tipo de unidad no se cambia por cuenta propia; se consulta al proyectista."),
        ("ab", "{F} Un estudiante suma todos los vanos a la superficie bruta total y dice que «hay más muro». ¿Qué respuesta es correcta?", "Está equivocado: los vanos se restan porque en ellos no hay muro", "Está en lo correcto: los vanos agregan superficie", "Un vano es una abertura, de modo que no aumenta el muro."),
        ("=", "{F} Si la planilla incluyera un muro M4 estructural de 10 m² brutos sin vanos, ¿cuántos m² netos estructurales habría en total entre M1, M3 y M4?", "(12-2)+(15-3)+10", "Se suman las superficies netas de los tres muros estructurales.", " m²"),
        ("abc", "{F} Antes de pedir unidades, el supervisor pide un registro de la diferencia con M4. ¿Qué debe contener?", "Qué documento tiene M4, cuál no, quién lo detectó y la fecha", "Solo el nombre de quien lo detectó", "Un presupuesto de todos los muros", "El registro deja constancia de la diferencia, de los documentos y de quién la detectó."),
    ],
    ctx=("abc", "Mientras revisas la planilla en la obra de ejemplo, ves a un compañero subido a un muro recién levantado que se tambalea. ¿Qué haces?", "No acercarme, avisar a un adulto responsable y a emergencias", "Subir a ayudarlo a bajar", "Seguir revisando y avisar después", "Acercarse a un muro inestable puede causar otro accidente; se avisa a quien corresponde."),
    sc=[
        ("¿Qué se hace con los vanos para obtener la superficie neta?", "Se restan de la superficie bruta", "En un vano no hay muro, por lo que se descuenta."),
        ("En Construcción (albañilería): ¿qué se hace si falta un muro en la planilla?", "Marcar la falta e informar a la inspección técnica de obra", "Los datos faltantes no se inventan: se informan a quien decide."),
        ("¿Quién decide qué unidad se usa en cada muro?", "Las especificaciones y el proyectista", "El tipo de unidad no se elige por cuenta propia, lo fijan las especificaciones."),
    ],
    op=("Planilla de ejemplo (inventada) de la obra «Bodega Sur»: muros S1 estructural, 14 m², con un vano de 2 m²; S2 no estructural, 8 m², sin vanos; S3 estructural, 10 m², con un vano de 1 m². El plano dibuja además un muro S4 que no está en la planilla. Escribe (a) la superficie neta de S1, (b) la superficie neta de S3, (c) los m² netos estructurales y (d) qué haces con S4.",
        "(a) 14 menos 2 son 12 m². (b) 10 menos 1 son 9 m². (c) 12 más 9 son 21 m². (d) Marco la falta de S4 y la informo a la inspección técnica de obra sin inventar sus datos.",
        ["resta bien los vanos", "suma solo los estructurales", "informa la falta de S4"],
        ["hoja con las cuatro respuestas"],
        ["sumar los vanos", "incluir S2 en los estructurales", "inventar datos de S4"],
        "Pregunta: «¿por qué S2 no entra en el total estructural?». Si no responde, pídele que relea la planilla."),
    reinforce="Inventa una planilla de tres muros con vanos y calcula la superficie neta de cada uno.",
    extend="Explica por qué una planilla incompleta puede llevar a pedir menos unidades de las necesarias.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 8 (cubicación de ejemplo, inventada). Obra «Residencial Colina» (ficticia): muro de 10 m de largo y 3 m de alto, con vanos que suman 4 m². "
     "Datos de ejemplo: 40 unidades por m² de muro neto; pérdida de ejemplo del 5 % sobre las unidades; precio de ejemplo $250 por unidad. "
     "Control de verticalidad de ejemplo: desplome medido de 8 mm y tolerancia de ejemplo de 10 mm.")
build(
    O4, 4, F,
    use="Aprenderé a cubicar unidades de un muro en una planilla, a agregar pérdida y costo y a registrar un control de verticalidad con una tolerancia de ejemplo.",
    prior=["Sé calcular superficie bruta y neta.", "Sé calcular un porcentaje simple.", "Sé comparar un valor medido con una tolerancia."],
    explain=[
        "Para saber cuántas unidades se necesitan se calcula primero la superficie neta del muro. Luego se multiplica por la cantidad de unidades por m², un dato que entrega el catálogo o la especificación (aquí es un valor de ejemplo). A ese total se le agrega la pérdida, que es un porcentaje por unidades quebradas o sobrantes. Con las unidades pedidas se calcula el costo multiplicando por el precio de cada una.",
        "La verticalidad es qué tan derecho está el muro respecto de la vertical; el desplome es la diferencia entre la parte alta y la baja del muro. La tolerancia es la diferencia máxima aceptada, y la fija la especificación o la norma vigente (aquí, un valor de ejemplo). Quien controla anota la medida en un registro y la compara con la tolerancia, y si no cumple informa a la inspección técnica de obra. Este cuaderno no enseña cómo levantar ni corregir un muro.",
        TAIL,
    ],
    vocab=[("cubicar", "calcular cantidades de material"), ("pérdida", "porcentaje de unidades quebradas o sobrantes que se suma al pedido"), ("verticalidad", "qué tan derecho está un muro respecto de la vertical"), ("desplome", "diferencia entre la parte alta y la baja de un muro"), ("tolerancia", "diferencia máxima aceptada"), ("registro", "documento donde se anotan mediciones y conclusiones")],
    worked=[
        ("Unidades de un muro", "Un muro de ejemplo tiene 10 m² netos y se usan 30 unidades por m². ¿Cuántas unidades se necesitan sin pérdida?", ["Se multiplican los m² por las unidades de cada m².", "10 por 30 son 300."], "300 unidades"),
        ("Comparar con la tolerancia", "Un desplome de ejemplo medido es de 12 mm y la tolerancia de ejemplo es de 9 mm. ¿Cumple?", ["12 es mayor que 9.", "El desplome supera la tolerancia."], "No cumple"),
    ],
    mistakes=[("Calcular las unidades con la superficie bruta y olvidar los vanos.", "Se pedirían unidades de más para zonas sin muro.", "Calcula primero la superficie neta."),
              ("Dar por cumplida una verticalidad «porque se ve derecha».", "El control exige medir y registrar.", "Anota la medida real y compárala con la tolerancia.")],
    T=[
        ("abc", "En Construcción (albañilería): ¿qué es la tolerancia de un control?", "La diferencia máxima aceptada", "El nombre de la persona que mide", "El precio de cada unidad", "La tolerancia es el límite que se acepta; no es un nombre ni un precio."),
        ("abc", "¿Qué significa verticalidad de un muro?", "Qué tan derecho está respecto de la vertical", "Qué tan largo es el muro", "Cuántas unidades tiene la hilada", "La verticalidad se refiere a la inclinación respecto de la vertical."),
        ("abc", "¿Para qué se agrega una pérdida a las unidades?", "Para cubrir las unidades quebradas o sobrantes", "Para pagar la mano de obra", "Para aumentar la resistencia del muro", "La pérdida cubre unidades que se quiebran o sobran, no costos de mano de obra."),
        ("=", "{F} ¿Cuántos m² brutos tiene el muro?", "10*3", "Se multiplican el largo y el alto.", " m²"),
        ("=", "{F} ¿Cuántos m² netos tiene el muro, descontando los vanos?", "10*3-4", "A la superficie bruta se le restan los vanos.", " m²"),
        ("abc", "{F} ¿Con qué dato se multiplica la superficie neta para obtener las unidades?", "Con las 40 unidades por m² de ejemplo", "Con el precio de $250", "Con el desplome de 8 mm", "Las unidades por m² dan la cantidad; el precio y el desplome sirven para otras cosas."),
        ("=", "{F} ¿Cuántas unidades se necesitan sin pérdida?", "(10*3-4)*40", "Se multiplica la superficie neta por las unidades por m².", " unidades"),
        ("=", "{F} ¿Cuántas unidades equivalen a la pérdida del 5 %?", "(10*3-4)*40*5//100", "Se calcula el 5 % de las unidades sin pérdida.", " unidades"),
        ("=", "{F} ¿Cuántas unidades se piden en total, con la pérdida?", "(10*3-4)*40+(10*3-4)*40*5//100", "A las unidades sin pérdida se les suma el 5 %.", " unidades"),
        ("=", "{F} ¿Cuánto cuestan las unidades pedidas al precio de ejemplo?", "((10*3-4)*40+(10*3-4)*40*5//100)*250", "Se multiplican las unidades pedidas por el precio de cada una.", " pesos"),
        ("ab", "{F} Se compara el desplome medido con la tolerancia de ejemplo. ¿Qué conclusión es correcta?", "Cumple: 8 mm no supera los 10 mm de tolerancia", "No cumple: 8 mm superan la tolerancia", "El desplome medido es menor que la tolerancia de ejemplo."),
        ("abc", "{F} Otro control de ejemplo mide 13 mm de desplome. ¿Qué corresponde?", "Registrar el valor y avisar a la inspección técnica de obra, porque supera la tolerancia", "Registrar 10 mm para que cumpla", "No registrar nada y seguir trabajando", "Un valor fuera de tolerancia se registra tal cual y se informa."),
        ("abc", "{F} Una persona dice: «el muro se ve derecho, no hace falta medirlo». ¿Qué respuesta es correcta?", "El control exige medir y registrar la medida, aunque el muro parezca derecho", "Tiene razón, si se ve derecho basta", "Basta con que lo diga el jefe de obra sin registrar", "A simple vista no se puede comparar con una tolerancia; se mide y se anota."),
    ],
    ctx=("abc", "Para medir el desplome, un compañero de ejemplo propone subirse a una escalera apoyada sin sujeción en un muro nuevo. ¿Qué corresponde?", "No hacerlo: el trabajo en altura exige personal autorizado y protecciones; se avisa al prevencionista", "Subir rápido para terminar el control", "Subir si alguien mira desde abajo", "Subir sin protecciones puede causar una caída; que alguien mire no lo evita."),
    sc=[
        ("¿Cómo se obtiene la superficie neta de un muro?", "Restando los vanos a la superficie bruta", "En los vanos no hay muro."),
        ("En Construcción (albañilería): ¿qué se hace si un desplome supera la tolerancia?", "Registrar el valor real e informar a la inspección técnica de obra", "Un valor real no se altera para que el registro cumpla."),
        ("¿Quién enseña a levantar o corregir un muro?", "Un instructor autorizado, con la norma vigente", "Este cuaderno es solo de cálculo y conceptos, no de oficio."),
    ],
    op=("Muro de ejemplo (inventado): 8 m de largo, 3 m de alto, vanos que suman 4 m²; 40 unidades por m² netos; pérdida de ejemplo 5 %; precio de ejemplo $200 por unidad. El desplome medido es de 11 mm y la tolerancia de ejemplo es de 10 mm. Escribe (a) los m² netos, (b) las unidades sin pérdida, (c) las unidades pedidas con la pérdida, (d) si el control cumple y qué haces.",
        "(a) 8×3 son 24; 24 menos 4 son 20 m². (b) 20×40 son 800 unidades. (c) El 5 % de 800 es 40; 800 más 40 son 840 unidades. (d) 11 mm supera los 10 mm: no cumple; registro el valor real e informo a la inspección técnica de obra.",
        ["calcula los m² netos", "calcula las unidades", "suma la pérdida", "concluye con la tolerancia e informa"],
        ["hoja con cálculos y conclusión"],
        ["usar superficie bruta", "no sumar la pérdida", "registrar 10 mm en vez de 11"],
        "Pregunta: «¿por qué no se registra 10 mm?». Si no responde, pídele que relea qué se hace con un valor fuera de tolerancia."),
    reinforce="Calcula las unidades de un muro de 5 m por 2 m sin vanos, con 30 unidades por m² y una pérdida de 10 % (datos de ejemplo).",
    extend="Explica por qué una pérdida mal calculada puede dejar al equipo sin material a mitad de la obra.",
)

# ============================================================ OAM-05, clase 1
F = ("Ficha 9 (obra de ejemplo, inventada). Obra «Casa Mirador» (ficticia): vivienda de dos pisos donde se trabaja con moldajes de madera, tabiquería y techumbre. Cuadrilla de 8 personas; solo 3 de ellas están autorizadas y capacitadas para trabajo en altura. "
     "Riesgos anotados: caída desde altura, caída de herramientas y materiales, golpes y cortes con madera y clavos, atrapamiento al mover piezas pesadas, polvo de madera y contacto con líneas eléctricas cercanas. "
     "Medidas anotadas: barandas y redes (protecciones colectivas), delimitar la zona bajo los trabajos en altura, inspección diaria y charla de seguridad, casco, guantes y calzado de seguridad.")
build(
    O5, 1, F,
    use="Aprenderé qué son los moldajes, la tabiquería y la techumbre, qué riesgos tienen (sobre todo la caída desde altura) y qué reglas generales de prevención se aplican.",
    prior=["Sé qué es la jerarquía de controles.", "Sé restar números pequeños.", "Sé leer una ficha de obra."],
    explain=[
        "El moldaje es una estructura provisoria que contiene el hormigón fresco hasta que endurece y toma su forma; puede ser de madera o industrializado (paneles reutilizables). La tabiquería arma muros livianos que dividen espacios. La techumbre es la estructura del techo, que incluye las cerchas, armazones que reparten el peso de la cubierta. Todas estas obras suelen hacerse sobre el suelo o cerca de bordes y alturas, por lo que el principal peligro es la caída. Cómo se arman y se instalan lo enseña un instructor autorizado con la norma vigente; aquí solo se estudia el vocabulario y la prevención.",
        "El trabajo en altura es el que se hace donde existe riesgo de caída a distinto nivel; solo lo realiza personal autorizado, capacitado y con protecciones. Siguiendo la jerarquía de controles, primero se busca evitar la altura, luego se instalan protecciones colectivas, como barandas y redes, que cuidan a todos a la vez, después se delimita y se capacita y, al final, se usan EPP. Debajo de un trabajo en altura se delimita la zona, porque pueden caer herramientas. Si ocurre una caída, nadie se acerca a la zona de riesgo sin autorización: se avisa a un adulto responsable y a emergencias.",
        TAIL,
    ],
    vocab=[("moldaje", "estructura provisoria que contiene el hormigón fresco hasta que endurece"), ("tabiquería", "muros livianos que dividen espacios"), ("techumbre", "estructura del techo, con sus cerchas y su cubierta"), ("cercha", "armazón que reparte el peso de la cubierta"), ("trabajo en altura", "el que se hace donde existe riesgo de caída a distinto nivel"), ("protección colectiva", "medida, como una baranda o una red, que cuida a todas las personas a la vez")],
    worked=[
        ("Clasificar una medida", "En una obra de ejemplo se instala una baranda en el borde de una losa. ¿Es una protección colectiva o un EPP?", ["La baranda cuida a todas las personas que pasan por el borde.", "Es una protección colectiva."], "Protección colectiva"),
        ("Contar personal", "Una cuadrilla de ejemplo tiene 10 personas y 4 están autorizadas para trabajo en altura. ¿Cuántas no lo están?", ["Se restan las autorizadas del total.", "10 menos 4 son 6."], "6 personas"),
    ],
    mistakes=[("Pensar que con casco ya se puede trabajar en altura.", "El casco no evita la caída; el trabajo en altura exige autorización y protecciones.", "Solo personal autorizado y capacitado trabaja en altura, con protecciones colectivas."),
              ("Dejar herramientas sobre un borde porque «solo será un momento».", "Pueden caer sobre quienes están abajo.", "Se delimita la zona inferior y no se dejan objetos en los bordes.")],
    T=[
        ("abc", "En Construcción (moldajes): ¿qué es un moldaje?", "Una estructura provisoria que contiene el hormigón fresco hasta que endurece", "Una pared definitiva que no se retira nunca", "Un tipo de techo con tejas", "El moldaje es provisorio y da forma al hormigón; no es una pared ni un techo."),
        ("abc", "¿Qué es la tabiquería?", "Los muros livianos que dividen espacios", "El armazón que reparte el peso del techo", "La estructura que contiene el hormigón", "La tabiquería arma divisiones livianas; el armazón del techo es la cercha y el contenedor del hormigón es el moldaje."),
        ("abc", "¿Qué es el trabajo en altura?", "El que se hace donde existe riesgo de caída a distinto nivel", "El que se hace solo en edificios de más de diez pisos", "El que se hace con herramientas eléctricas", "Lo que define el trabajo en altura es el riesgo de caída, no la cantidad de pisos."),
        ("=", "{F} ¿Cuántas personas de la cuadrilla no están autorizadas para trabajo en altura?", "8-3", "Se restan las personas autorizadas del total de la cuadrilla.", " personas"),
        ("abc", "{F} ¿Qué medida de la ficha es una protección colectiva?", "Las barandas y las redes", "El casco", "El calzado de seguridad", "Barandas y redes cuidan a todas las personas a la vez; casco y calzado son EPP."),
        ("abc", "{F} ¿Cuál es un riesgo anotado en la ficha?", "La caída de herramientas y materiales", "La inundación de la obra", "El robo de herramientas", "La ficha nombra la caída de herramientas; las otras opciones no aparecen."),
        ("abc", "{F} Una persona no autorizada para altura se ofrece a «ayudar» en el borde del segundo piso. ¿Qué corresponde?", "No subir: el trabajo en altura lo hacen solo las personas autorizadas", "Subir si lo supervisa un compañero", "Subir con el casco puesto", "Ni la compañía ni el casco reemplazan la autorización y la capacitación."),
        ("abc", "{F} ¿Por qué se delimita la zona bajo los trabajos en altura?", "Porque pueden caer herramientas o materiales sobre quien pase", "Para que nadie vea el trabajo", "Para ahorrar cinta de seguridad", "La delimitación evita que alguien reciba un objeto caído."),
        ("=", "{F} Si las 3 personas autorizadas reciben 2 piezas de EPP cada una además de las que tienen todos, ¿cuántas piezas adicionales se entregan?", "3*2", "Se multiplican las personas autorizadas por las piezas de cada una.", " piezas"),
        ("ab", "{F} Un compañero dice: «con las barandas ya no hace falta capacitar a nadie». ¿Qué es correcto?", "No: las barandas son una medida, pero igual se capacita y se delimita", "Sí: las barandas hacen innecesario todo lo demás", "Ninguna medida aislada reemplaza a las otras en la jerarquía de controles."),
        ("abc", "{F} Una estudiante afirma: «ya leí la ficha, así que puedo armar un tabique en el segundo piso». ¿Qué respuesta es correcta?", "No: esa tarea exige instructor autorizado, norma vigente y protecciones", "Sí: leer la ficha la habilita", "Sí, si usa casco y guantes", "Conocer los riesgos no habilita; ningún EPP reemplaza la autorización."),
        ("=", "{F} Si cada una de las 8 personas necesita 1 casco, 1 par de guantes y 1 par de calzado, ¿cuántas piezas hay que tener?", "8*3", "Se multiplican las personas por las tres piezas que necesita cada una.", " piezas"),
        ("abc", "Una persona de ejemplo cae desde un borde y queda tendida. ¿Qué corresponde según las reglas generales?", "No acercarse a la zona de riesgo sin autorización, avisar a un adulto responsable y a emergencias", "Acercarse de inmediato a moverla", "Esperar a que se levante sola", "Acercarse o mover a una persona caída puede empeorar el accidente; se avisa a quien corresponde."),
    ],
    ctx=("abc", "En una obra de ejemplo, ves una herramienta apoyada en el borde de un piso alto, justo sobre donde caminan compañeros. ¿Qué haces?", "Avisar al prevencionista o al jefe de obra para que se delimite la zona y se retire con seguridad", "Subir tú mismo a tirarla al suelo", "Dejarla porque no ha caído todavía", "Un objeto en un borde es un peligro; se avisa a quien puede intervenir con seguridad."),
    sc=[
        ("En Construcción (techumbres): ¿qué es una cercha?", "Un armazón que reparte el peso de la cubierta", "La cercha es parte de la techumbre, no del moldaje."),
        ("¿Qué es una protección colectiva?", "Una medida que cuida a todas las personas a la vez, como una baranda o una red", "Se diferencia del EPP en que no protege solo a una persona."),
        ("¿Quién puede trabajar en altura?", "Solo personal autorizado y capacitado, con protecciones", "La altura exige autorización; leer este cuaderno no la reemplaza."),
    ],
    op=("Obra de ejemplo «Taller Roble» (ficticia): cuadrilla de 12 personas, de las cuales 5 están autorizadas para trabajo en altura. Riesgos anotados: caída desde altura, caída de herramientas y atrapamiento. Medidas disponibles: baranda en el borde, delimitar la zona inferior, casco, guantes y capacitación. Escribe (a) cuántas personas no están autorizadas para altura, (b) cuál medida es protección colectiva, (c) cuáles son EPP y (d) qué haces si alguien cae y queda tendido, sin acercarte a la zona de riesgo.",
        "(a) 12 menos 5 son 7 personas. (b) La baranda en el borde. (c) El casco y los guantes. (d) No me acerco a la zona de riesgo sin autorización, aviso a un adulto responsable y a emergencias.",
        ["calcula quiénes no están autorizadas", "identifica la protección colectiva", "identifica los EPP", "indica avisar sin acercarse"],
        ["hoja con las cuatro respuestas"],
        ["decir que el casco permite trabajar en altura", "confundir baranda con EPP", "proponer acercarse al caído"],
        "Pregunta: «¿por qué una baranda es colectiva y el casco no?». Si no responde, pídele que relea la definición de protección colectiva."),
    reinforce="Escribe tres riesgos de una obra de techumbre y, para cada uno, una protección colectiva o administrativa posible.",
    extend="Explica por qué delimitar la zona bajo un trabajo en altura protege a personas que no participan del trabajo.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 10 (despiece de ejemplo, inventado). Obra «Pabellón Lila» (ficticia). Tabique T1: 9 pies derechos de 3 m y 2 soleras de 4 m. Tabique T2: 5 pies derechos de 3 m y 2 soleras de 2 m. "
     "Techumbre: 4 cerchas iguales, rotuladas C1 a C4. Moldaje de un pilar de ejemplo: 4 paneles industrializados reutilizables. "
     "El despiece es la lista de piezas con sus medidas y cantidades.")
build(
    O5, 2, F,
    use="Aprenderé el vocabulario de moldajes, tabiquería y techumbres (pie derecho, solera, cercha, panel) y cómo se leen un despiece y los planos estructurales.",
    prior=["Sé qué es un moldaje, un tabique y una techumbre.", "Sé multiplicar y sumar.", "Sé leer una lista de piezas."],
    explain=[
        "El pie derecho es la pieza vertical de un tabique; la solera es la pieza horizontal en que se apoyan los pies derechos, arriba y abajo. Entre ellos forman el esqueleto del tabique. La cercha es el armazón del techo y la cubierta es la capa exterior que protege de la lluvia. El panel industrializado es una pieza de moldaje prefabricada y reutilizable, distinta de las tablas de madera que se usan una sola vez o pocas veces. El despiece es la lista de piezas, con sus medidas y cantidades, que sale de los planos.",
        "Los planos estructurales muestran dónde van moldajes, tabiques y cerchas y cuáles son sus medidas. Las especificaciones dicen la calidad de los materiales. Si una cantidad del despiece no coincide con el plano, nadie la corrige por cuenta propia: se anota la diferencia y se informa a quien diseña o inspecciona. Aquí se lee y se calcula; cómo se arman y se instalan estas piezas lo enseña un instructor autorizado.",
        TAIL,
    ],
    vocab=[("pie derecho", "pieza vertical de un tabique"), ("solera", "pieza horizontal en que se apoyan los pies derechos"), ("cercha", "armazón del techo que reparte el peso de la cubierta"), ("cubierta", "capa exterior del techo que protege de la lluvia"), ("panel industrializado", "pieza de moldaje prefabricada y reutilizable"), ("despiece", "lista de piezas con sus medidas y cantidades")],
    worked=[
        ("Piezas de un tabique", "Un tabique de ejemplo lleva 7 pies derechos y 2 soleras. ¿Cuántas piezas son?", ["Se suman los pies derechos y las soleras.", "7 más 2 son 9."], "9 piezas"),
        ("Metros lineales", "Un despiece de ejemplo anota 6 soleras de 2 m cada una. ¿Cuántos metros lineales suman?", ["Se multiplica la cantidad por el largo de cada solera.", "6 por 2 son 12."], "12 metros lineales"),
    ],
    mistakes=[("Llamar «solera» a la pieza vertical.", "La solera es horizontal y el pie derecho es vertical.", "Piensa: la solera «soporta» a los pies; el pie derecho está de pie."),
              ("Cambiar una cantidad del despiece porque «parece poca».", "Una cantidad mal cambiada altera pedidos y trabajos.", "Anota la diferencia e informa a quien diseña o inspecciona.")],
    T=[
        ("abc", "En Construcción (tabiquería): ¿qué es un pie derecho?", "La pieza vertical de un tabique", "La pieza horizontal en que se apoyan los pies", "El armazón del techo", "El pie derecho es vertical; la pieza horizontal es la solera y el armazón del techo es la cercha."),
        ("abc", "¿Qué es una solera?", "La pieza horizontal en que se apoyan los pies derechos", "La capa exterior del techo", "La pieza prefabricada de un moldaje", "La solera es horizontal; la capa exterior es la cubierta y el panel es de moldaje."),
        ("abc", "¿Qué es un despiece?", "La lista de piezas con sus medidas y cantidades", "El dibujo de la vista frontal de un muro", "El registro de accidentes de la obra", "El despiece lista piezas con medidas y cantidades; no es un dibujo ni un registro de accidentes."),
        ("=", "{F} ¿Cuántos pies derechos hay entre T1 y T2?", "9+5", "Se suman los pies derechos de los dos tabiques.", " pies derechos"),
        ("=", "{F} ¿Cuántas soleras hay entre T1 y T2?", "2+2", "Se suman las soleras de los dos tabiques.", " soleras"),
        ("abc", "{F} ¿Qué rótulos tienen las cerchas de la techumbre?", "C1 a C4", "T1 y T2", "P1 a P4", "Las cerchas son C1 a C4; T1 y T2 son tabiques."),
        ("=", "{F} ¿Cuántos metros lineales suman los pies derechos de T1?", "9*3", "Se multiplican los 9 pies derechos por 3 m cada uno.", " metros"),
        ("=", "{F} ¿Cuántos metros lineales suman todas las soleras de T1 y T2?", "2*4+2*2", "Se suman los metros de las soleras de cada tabique.", " metros"),
        ("=", "{F} ¿Cuántas piezas de madera tiene T1 entre pies derechos y soleras?", "9+2", "Se suman los pies derechos y las soleras de T1.", " piezas"),
        ("abc", "{F} El plano de T2 dibuja 6 pies derechos y el despiece anota 5. ¿Qué corresponde?", "Anotar la diferencia e informar a quien diseña o inspecciona", "Corregir el despiece a 6 sin avisar", "Pedir 5 porque el despiece es más reciente", "Una diferencia entre plano y despiece se informa; nadie la corrige por cuenta propia."),
        ("ab", "{F} Una estudiante dice: «los 4 paneles del pilar se usan una sola vez, como las tablas». ¿Qué respuesta es correcta?", "No: los paneles industrializados son reutilizables", "Sí: todo moldaje se usa una sola vez", "La ficha los describe como paneles reutilizables, a diferencia de la madera de pocos usos."),
        ("=", "{F} Si hubiera 3 pilares iguales al de la ficha, ¿cuántos paneles se necesitarían?", "3*4", "Se multiplican los pilares por los paneles de cada uno.", " paneles"),
        ("abc", "{F} Alguien propone agregar una quinta cercha «por si acaso». ¿Qué corresponde?", "No agregarla: cualquier cambio lo decide quien diseña la techumbre", "Agregarla si sobra madera", "Agregarla si el jefe de obra lo prefiere sin consultar a nadie", "El número de cerchas está definido por el diseño; los cambios los decide quien lo diseñó."),
    ],
    ctx=("abc", "Un compañero de ejemplo te pide sostener una cercha armada mientras él sube a medirla. ¿Qué respondes?", "Que no: mover piezas pesadas y subir exige personal autorizado y avisar al prevencionista", "Aceptas si es solo un momento", "Aceptas si tienes guantes", "Las piezas pesadas y la altura son riesgos serios; no se improvisa."),
    sc=[
        ("En Construcción (tabiquería): ¿qué pieza es horizontal en un tabique?", "La solera", "Los pies derechos son verticales, las soleras horizontales."),
        ("¿Qué es un panel industrializado?", "Una pieza de moldaje prefabricada y reutilizable", "Se reutiliza, a diferencia de muchas piezas de madera."),
        ("¿Qué se hace si el despiece y el plano no coinciden?", "Anotar la diferencia e informar a quien diseña o inspecciona", "Nadie corrige por cuenta propia una diferencia de documentos."),
    ],
    op=("Despiece de ejemplo (inventado): tabique T3 con 11 pies derechos de 3 m y 2 soleras de 5 m; 3 cerchas rotuladas C1 a C3; moldaje con 6 paneles. El plano de T3 dibuja 12 pies derechos. Escribe (a) cuántas piezas de madera tiene T3, (b) cuántos metros lineales suman sus soleras, (c) cuántos metros lineales suman sus pies derechos y (d) qué haces con la diferencia entre plano y despiece.",
        "(a) 11 más 2 son 13 piezas. (b) 2×5 son 10 metros. (c) 11×3 son 33 metros. (d) Anoto la diferencia (12 en el plano y 11 en el despiece) y la informo a quien diseña o inspecciona.",
        ["suma las piezas de T3", "calcula los metros de soleras", "calcula los metros de pies derechos", "informa la diferencia"],
        ["hoja con las cuatro respuestas"],
        ["incluir cerchas en las piezas de T3", "corregir el despiece sin avisar", "confundir pie derecho con solera"],
        "Pregunta: «¿qué piezas entran en T3?». Si no responde, pídele que relea el despiece de T3."),
    reinforce="Dibuja un tabique pequeño y rotula pies derechos y soleras; escribe una frase que diga cuál es horizontal y cuál vertical.",
    extend="Explica por qué un despiece correcto ayuda a pedir la cantidad justa de madera.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 11 (lista de verificación de moldaje de ejemplo, inventada). Pilar P1 de la obra «Edificio Brisa» (ficticia). Ítems: 1. Medidas del moldaje coinciden con el plano: cumple. 2. Superficies limpias y sin restos: cumple. "
     "3. Revisión de los apoyos por el responsable: no cumple. 4. Zona de trabajo delimitada y señalizada: cumple. 5. Personal autorizado presente: cumple. 6. Fecha y hora de la revisión anotadas: pendiente. "
     "Regla de ejemplo: el responsable firma solo si los seis ítems están en «cumple». Inventario de ejemplo: se necesitan 12 paneles y hay 9 en bodega.")
build(
    O5, 3, F,
    use="Aprenderé a analizar en papel una lista de verificación de moldaje y un inventario de paneles, y a decidir qué se informa antes de que el responsable firme.",
    prior=["Sé qué es un moldaje y un despiece.", "Sé restar números pequeños.", "Sé que las diferencias se informan."],
    explain=[
        "Una lista de verificación es un documento con ítems que se marcan como «cumple», «no cumple» o «pendiente». Se usa antes de una etapa importante para comprobar que todo está en orden. En un moldaje se revisan, por ejemplo, las medidas contra el plano, la limpieza, los apoyos y la seguridad de la zona. Un ítem «no cumple» no se corrige marcándolo como «cumple»: se informa y lo corrige la persona autorizada. «Pendiente» significa que aún no se ha revisado.",
        "El responsable es la persona que firma el registro y asume que todo cumple. No firma si queda algún ítem que no cumple o pendiente. Para el inventario se compara lo necesario con lo disponible: si falta material, se informa para que se pida, y no se reemplaza por otro sin autorización. Los valores y listas de este caso son inventados; cómo se arma o se revisa un moldaje en terreno lo enseña un instructor autorizado.",
        TAIL,
    ],
    vocab=[("lista de verificación", "documento con ítems que se marcan como cumple, no cumple o pendiente"), ("pendiente", "ítem que aún no se ha revisado"), ("responsable", "persona que firma el registro y asume que todo cumple"), ("inventario", "recuento de lo disponible en bodega"), ("apoyos", "elementos que sostienen provisoriamente un moldaje")],
    worked=[
        ("Contar ítems", "Una lista de ejemplo tiene 8 ítems: 5 cumplen, 2 no cumplen y el resto está pendiente. ¿Cuántos están pendientes?", ["Se suman los que cumplen y no cumplen: 7.", "8 menos 7 es 1."], "1 ítem pendiente"),
        ("Decidir la firma", "Regla de ejemplo: firma solo si todos los ítems cumplen. En un caso de ejemplo uno está pendiente. ¿Se firma?", ["Un ítem pendiente no cumple todavía la regla.", "No se firma."], "No se firma"),
    ],
    mistakes=[("Marcar «cumple» un ítem sin haberlo revisado para poder firmar.", "Un registro falso puede esconder un riesgo grave.", "Si no se revisó, queda «pendiente»; se revisa antes de firmar."),
              ("Reemplazar paneles faltantes por cualquier otro material de la bodega.", "El reemplazo altera el moldaje sin autorización.", "Informa la falta para que el responsable decida.")],
    T=[
        ("abc", "En Construcción (moldajes): ¿qué significa «pendiente» en una lista de verificación?", "Que el ítem aún no se ha revisado", "Que el ítem cumple a medias", "Que el ítem se puede marcar sin revisar", "Pendiente indica que falta revisar; no equivale a cumplir."),
        ("abc", "¿Quién firma el registro de una lista de verificación?", "El responsable, solo si todos los ítems cumplen", "Cualquier integrante de la cuadrilla", "El proveedor de los paneles", "La firma la hace quien asume la responsabilidad, y solo si todo cumple."),
        ("abc", "Un ítem «no cumple». ¿Qué corresponde?", "Informarlo para que lo corrija una persona autorizada", "Marcarlo como cumple", "Dejarlo sin mencionar", "Un ítem que no cumple se informa; no se altera la lista."),
        ("=", "{F} ¿Cuántos ítems de la lista cumplen?", "6-1-1", "De los 6 ítems, uno no cumple y otro está pendiente; los demás cumplen.", " ítems"),
        ("abc", "{F} ¿Qué ítem de la lista está en «no cumple»?", "La revisión de los apoyos por el responsable", "La limpieza de las superficies", "La zona delimitada y señalizada", "El ítem 3, revisión de apoyos, es el único marcado como no cumple."),
        ("abc", "{F} ¿Qué ítem está pendiente?", "La fecha y la hora de la revisión anotadas", "Las medidas contra el plano", "La presencia de personal autorizado", "El ítem 6 es el único marcado como pendiente."),
        ("=", "{F} ¿Cuántos paneles faltan según el inventario?", "12-9", "Se restan los paneles disponibles de los necesarios.", " paneles"),
        ("abc", "{F} Aplicando la regla de ejemplo, ¿puede firmar el responsable?", "No: hay un ítem que no cumple y uno pendiente", "Sí: cuatro de seis ítems cumplen", "Sí: basta que cumplan las medidas", "La regla pide los seis ítems en cumple; aquí hay uno que no cumple y uno pendiente."),
        ("abc", "{F} Faltan paneles. Un compañero propone usar tablas sueltas «para salir del paso». ¿Qué corresponde?", "No hacerlo: informar la falta para que el responsable decida", "Hacerlo si se ve firme", "Hacerlo si no hay nadie mirando", "Un reemplazo sin autorización altera el moldaje y puede ser riesgoso."),
        ("ab", "{F} Un estudiante dice: «marquemos los apoyos como cumple y firmemos, así no atrasamos». ¿Qué respuesta es correcta?", "No: un registro falso esconde un riesgo; los apoyos se revisan y se corrigen primero", "Sí: atrasar la obra es peor que un registro falso", "Marcar sin revisar puede ocultar un riesgo grave de colapso."),
        ("=", "{F} Si llegan 2 paneles más a la bodega, ¿cuántos paneles faltarían todavía?", "12-(9+2)", "Se suman los paneles que llegan y se restan de los necesarios.", " panel"),
        ("abc", "{F} Si se revisan los apoyos y el ítem 3 pasa a «cumple», ¿qué ítem impide todavía la firma?", "El ítem 6, que sigue pendiente hasta que se anote la fecha y la hora de la revisión", "Ninguno: ya se puede firmar", "El ítem 1, que ya cumple", "Aunque el ítem 3 se corrija, el ítem 6 sigue pendiente y la regla pide los seis ítems en cumple antes de firmar."),
        ("abc", "{F} Antes de seguir, el supervisor pide dejar constancia del ítem 3. ¿Qué incluye?", "El ítem, que no cumple, quién lo detectó y la fecha", "Solo la palabra «mal»", "El nombre del proveedor", "La constancia dice qué falló, quién lo vio y cuándo."),
    ],
    ctx=("abc", "Al revisar los apoyos de un moldaje en una obra de ejemplo, un compañero nota que una pieza se mueve y el moldaje cruje. ¿Qué corresponde?", "Alejarse de la zona de riesgo y avisar de inmediato al responsable y a un adulto responsable", "Acercarse a sujetarla con la mano", "Seguir mirando para entender qué ocurre", "Un moldaje que cruje puede ceder; nadie se acerca y se avisa a quien corresponde."),
    sc=[
        ("En Construcción (moldajes): ¿qué significa «no cumple»?", "Que el ítem no está como pide el documento y debe informarse", "Un ítem que no cumple se informa, no se esconde."),
        ("¿Cuándo firma el responsable el registro?", "Solo cuando todos los ítems están en cumple", "La firma asume que todo cumple."),
        ("¿Qué se hace si faltan paneles?", "Se informa la falta para que se pida material", "Un reemplazo sin autorización altera el moldaje y su seguridad."),
    ],
    op=("Lista de ejemplo (inventada) para un moldaje de viga: 1. Medidas coinciden con el plano: cumple. 2. Limpieza: cumple. 3. Apoyos revisados por el responsable: cumple. 4. Zona delimitada: no cumple. 5. Personal autorizado: cumple. 6. Fecha de revisión anotada: pendiente. Inventario: se necesitan 10 paneles y hay 6. Escribe (a) cuántos ítems cumplen, (b) cuántos paneles faltan, (c) si el responsable puede firmar y por qué y (d) qué informas.",
        "(a) Cumplen 4 ítems (1, 2, 3 y 5). (b) 10 menos 6 son 4 paneles. (c) No puede firmar: el ítem 4 no cumple y el 6 está pendiente. (d) Informo el ítem 4 (zona sin delimitar) y la falta de 4 paneles al responsable, con fecha.",
        ["cuenta los ítems que cumplen", "calcula los paneles faltantes", "aplica la regla de firma", "informa lo que falla"],
        ["hoja con las cuatro respuestas"],
        ["contar el pendiente como cumple", "firmar con un ítem que no cumple", "no informar la falta de paneles"],
        "Pregunta: «¿qué ítems impiden la firma?». Si no responde, pídele que relea la regla de firma."),
    reinforce="Inventa una lista de verificación de cinco ítems para un tabique y marca cuáles cumplen, cuáles no y cuáles quedan pendientes.",
    extend="Explica por qué una lista de verificación con ítems marcados sin revisar es peor que una lista con ítems pendientes.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 12 (comparación de ejemplo, inventada). Obra «Residencia Álamo» (ficticia): superficie de moldaje de 120 m². Opción A, moldaje de madera: costo de compra de $15.000 por m², con 3 usos posibles. "
     "Opción B, moldaje industrializado: arriendo de $6.000 por m² por cada uso. Se necesitan 3 usos. Tabique de ejemplo de 12 m de largo y 3 m de alto, con pies derechos cada 60 cm; precio de ejemplo de la madera: $1.500 por metro lineal.")
build(
    O5, 4, F,
    use="Aprenderé a comparar con una planilla el costo de moldaje de madera e industrializado, y a calcular cantidades de pies derechos y metros lineales con datos de ejemplo.",
    prior=["Sé multiplicar y sumar con cifras grandes.", "Sé dividir una longitud por una separación.", "Sé qué es un despiece."],
    explain=[
        "Elegir entre moldaje de madera y moldaje industrializado es una decisión de costo, plazo y calidad que toma el responsable de la obra. Con una planilla se puede comparar el costo total: en el caso de la madera, el costo de compra se reparte entre los usos posibles; en el industrializado se paga un arriendo por cada uso. El costo total de cada opción se obtiene multiplicando superficie, precio y cantidad de usos según corresponda. La comparación solo usa precios de ejemplo; no es una recomendación de compra.",
        "Para contar piezas repartidas a una distancia fija, como los pies derechos de un tabique, se divide el largo por la separación y se suma 1 por el pie del extremo final. Los metros lineales de madera se obtienen multiplicando la cantidad de piezas por el largo de cada una. Todos los datos son de ejemplo: las separaciones y medidas reales las fijan el proyecto y la norma vigente. Este cuaderno no enseña a armar ni instalar estas piezas.",
        TAIL,
    ],
    vocab=[("uso", "cada vez que se emplea el moldaje en un elemento"), ("arriendo", "pago por usar una pieza durante un período"), ("metro lineal", "un metro de longitud de una pieza"), ("separación", "distancia fija entre piezas repetidas"), ("costo total", "suma de todos los costos de una opción")],
    worked=[
        ("Costo con varios usos", "Un moldaje de ejemplo de 10 m² se arrienda a $4.000 por m² por uso y se usa 2 veces. ¿Cuál es el costo total?", ["Se multiplican m², precio y usos.", "10 por 4.000 por 2 son 80.000."], "$80.000"),
        ("Contar piezas con separación", "Un tabique de ejemplo de 4 m (400 cm) lleva pies derechos cada 100 cm. ¿Cuántos pies derechos tiene?", ["400 dividido en 100 son 4 tramos.", "Se suma 1 por el extremo final: 5."], "5 pies derechos"),
    ],
    mistakes=[("Contar solo los tramos y olvidar el pie derecho del extremo final.", "Con una separación fija siempre hay un pie más que tramos.", "Divide el largo por la separación y suma 1."),
              ("Comparar el costo de compra de la madera con el arriendo de un solo uso.", "Las opciones se comparan por la misma cantidad de usos.", "Calcula el costo total de cada opción para los 3 usos.")],
    T=[
        ("abc", "En Construcción (moldajes): ¿qué es un uso del moldaje?", "Cada vez que se emplea el moldaje en un elemento", "El color con que se pinta", "El plano que lo dibuja", "Un uso es cada empleo del moldaje en un elemento, y por eso importa para comparar costos."),
        ("abc", "¿Qué es un metro lineal de madera?", "Un metro de longitud de una pieza", "Un metro cuadrado de superficie", "Un metro cúbico de volumen", "El metro lineal mide longitud; el cuadrado mide superficie y el cúbico, volumen."),
        ("abc", "Un tabique tiene pies derechos con una separación fija. ¿Cómo se cuentan?", "Dividiendo el largo por la separación y sumando 1", "Dividiendo el largo por la separación sin sumar nada", "Multiplicando el largo por la separación", "Hay un pie más que tramos, por eso se suma 1 al dividir."),
        ("=", "{F} ¿Cuánto cuesta comprar el moldaje de madera de 120 m² (opción A)?", "120*15000", "Se multiplica la superficie por el precio de compra por m².", " pesos"),
        ("=", "{F} ¿Cuánto cuesta el arriendo del moldaje industrializado para un uso de 120 m² (opción B)?", "120*6000", "Se multiplica la superficie por el arriendo por m² de un uso.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta la opción B para los 3 usos?", "120*6000*3", "Se multiplica el arriendo de un uso por los 3 usos.", " pesos"),
        ("abc", "{F} Considerando los 3 usos, ¿cuál opción tiene menor costo total de ejemplo?", "La opción A, de madera", "La opción B, industrializada", "Cuestan lo mismo", "A cuesta 1.800.000 y B cuesta 2.160.000, por lo que A es menor en este ejemplo."),
        ("=", "{F} ¿Cuál es la diferencia de costo entre las dos opciones para los 3 usos?", "120*6000*3-120*15000", "Se resta el costo total de la opción A del costo total de la opción B.", " pesos"),
        ("=", "{F} ¿Cuántos tramos de 60 cm caben en el tabique de 12 m (1.200 cm)?", "1200//60", "El largo en centímetros se divide por la separación.", " tramos"),
        ("=", "{F} ¿Cuántos pies derechos lleva el tabique de ejemplo, sumando el del extremo final?", "1200//60+1", "A los tramos se suma el pie derecho del extremo final.", " pies derechos"),
        ("=", "{F} Si cada pie derecho mide 3 m, ¿cuántos metros lineales suman todos?", "(1200//60+1)*3", "Se multiplican los pies derechos por el largo de cada uno.", " metros"),
        ("=", "{F} ¿Cuánto cuestan esos pies derechos al precio de ejemplo por metro lineal?", "(1200//60+1)*3*1500", "Se multiplican los metros lineales por el precio de cada metro.", " pesos"),
        ("abc", "{F} Un estudiante concluye: «como A es más barata, hay que comprarla». ¿Qué respuesta es correcta?", "La decisión final la toma el responsable con costo, plazo, calidad y la norma vigente", "Es correcto, siempre se elige lo más barato", "Es correcto si el estudiante lo decide", "El cálculo es solo de ejemplo; elegir una opción es decisión de quien tiene la responsabilidad."),
    ],
    ctx=("abc", "Para contar los pies derechos de un tabique de ejemplo, un compañero propone subirse a una torre de andamio sin barandas. ¿Qué corresponde?", "No subir: el trabajo en altura exige personal autorizado y protecciones; el conteo se hace en el despiece", "Subir con cuidado", "Subir si alguien sostiene la torre", "El conteo se hace en papel; la altura sin protecciones no se improvisa."),
    sc=[
        ("¿Cómo se cuentan piezas repartidas a una separación fija?", "Dividiendo el largo por la separación y sumando 1", "Siempre hay una pieza más que tramos."),
        ("En Construcción (moldajes): ¿cómo se compara el costo de dos opciones?", "Calculando el costo total de cada una para los mismos usos", "Comparar con distinta cantidad de usos distorsiona la decisión."),
        ("¿Quién toma la decisión de qué moldaje se usa?", "El responsable de la obra, con el proyecto y la norma vigente", "El cálculo de ejemplo no reemplaza esa decisión."),
    ],
    op=("Caso de ejemplo (inventado): superficie de moldaje de 50 m²; opción A, madera, $14.000 por m² con 2 usos posibles; opción B, industrializado, $8.000 por m² por uso, con 2 usos. Tabique de 6 m (600 cm) con pies derechos cada 50 cm. Escribe (a) el costo de A, (b) el costo de B para 2 usos, (c) cuál es menor y la diferencia, (d) cuántos pies derechos lleva el tabique y (e) a quién le corresponde decidir.",
        "(a) 50×14.000 son 700.000 pesos. (b) 50×8.000×2 son 800.000 pesos. (c) A es menor y la diferencia es de 100.000 pesos. (d) 600 dividido en 50 son 12 tramos; más 1 son 13 pies derechos. (e) Al responsable de la obra, según el proyecto y la norma vigente.",
        ["calcula el costo de A", "calcula B para los usos", "compara y da la diferencia", "cuenta pies derechos con el +1", "indica quién decide"],
        ["hoja con cálculos y conclusión"],
        ["comparar B de un solo uso", "olvidar el +1", "decidir sin el responsable"],
        "Pregunta: «¿por qué B se multiplica por 2?». Si no responde, pídele que relea cómo se paga el arriendo."),
    reinforce="Calcula el costo de arrendar 30 m² a $5.000 por m² por uso durante 4 usos (datos de ejemplo).",
    extend="Explica por qué dos opciones con el mismo costo total pueden elegirse por otros motivos, como el plazo o la calidad.",
)
