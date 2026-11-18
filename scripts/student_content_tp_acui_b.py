"""Acuicultura TP 3.º y 4.º medio: OAE-03 (cosecha, solo conceptos y registros), OAE-04 (captación de semillas) y OAE-05 (tareas subacuáticas, solo conceptos de seguridad y documentos). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_acui_common import AVISO, EMER, build

O3 = "TP-ACUI-3y4-OAE-03"

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La planta ficticia «Planta Demo» recibe peces cosechados de «especie A» para clasificarlos y empacarlos en cajas de 20 kg. "
     "Peligros anotados: carga suspendida de una grúa en el muelle, piso con agua y hielo, herramientas cortantes en la sala de proceso, ruido y frío intenso en la cámara de frío.")
build(
    O3, 1, F,
    use="Aprenderé qué es la cosecha, qué son la calidad, la inocuidad y la cadena de frío, y cómo se ordenan las medidas de prevención en una planta de proceso.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé qué es la trazabilidad.", "Sé sumar, restar, multiplicar y dividir números enteros."],
    explain=[
        "La cosecha es la extracción de los animales de un cultivo cuando alcanzaron el tamaño comercial, es decir, el tamaño en que se venden. Después los productos pasan a una planta de proceso, donde se clasifican, se empacan y se guardan. Los estándares de calidad del sector fijan qué se espera de un producto, como su tamaño, su aspecto y su frescura. La inocuidad es que un alimento no cause daño a quien lo consume.",
        "Para conservar la calidad y la inocuidad se mantiene la cadena de frío: mantener el producto frío de manera continua desde la cosecha hasta el consumidor, por ejemplo en una cámara de frío, una sala refrigerada. La trazabilidad permite saber de qué lote y de qué jaula viene cada caja. El manejo ético exige tratar a los animales evitando sufrimiento innecesario, según la norma vigente y por personal autorizado.",
        f"Los peligros de la cosecha y de la planta se previenen con la jerarquía de controles: eliminar, sustituir, ingeniería (barreras físicas), administrativos (reglas y señales) y, al final, el EPP. Nunca hay que pararse bajo una carga suspendida. Este cuaderno no describe cómo se cosecha ni cómo se procesa. {EMER} {AVISO}",
    ],
    vocab=[("cosecha", "extracción de los animales de un cultivo cuando alcanzan el tamaño comercial"), ("tamaño comercial", "tamaño en que un producto se vende"), ("planta de proceso", "lugar donde los productos se clasifican, se empacan y se guardan"), ("estándar de calidad", "característica esperada de un producto, como tamaño, aspecto o frescura"), ("inocuidad", "característica de un alimento que no causa daño a quien lo consume"), ("cadena de frío", "mantención continua del frío desde la cosecha hasta el consumidor"), ("cámara de frío", "sala refrigerada donde se guardan los productos"), ("carga suspendida", "carga levantada por un equipo y que cuelga sobre el piso")],
    worked=[
        ("Peligro y riesgo", "En una sala de ejemplo hay un charco de agua y hielo frente a la puerta de la cámara. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el charco con hielo, que puede causar daño.", "El riesgo es que alguien resbale, caiga y se lastime."], "Peligro: el charco con hielo; riesgo: que alguien resbale, caiga y se lastime"),
        ("Clasificar un control", "Una planta de ejemplo instala una barrera fija que impide el paso a la zona donde se mueven las cargas. ¿A qué nivel de la jerarquía corresponde?", ["La barrera cambia físicamente el lugar.", "Los cambios físicos del lugar son controles de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Creer que usar casco y guantes permite estar bajo una carga suspendida.", "El EPP no quita el peligro; una carga que cae puede causar un daño grave.", "Nunca hay que pararse bajo una carga suspendida; se respetan las barreras y las reglas."),
              ("Creer que la inocuidad se asegura solo con el aspecto del producto.", "Un producto puede verse bien y no ser inocuo; la inocuidad depende de la cadena de frío y de la norma.", "Se siguen los registros y las reglas de la planta.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es la cosecha?", "La extracción de los animales de un cultivo cuando alcanzaron el tamaño comercial", "La entrega diaria de alimento a los animales", "La compra de animales jóvenes para iniciar un cultivo", "La cosecha ocurre al final del cultivo; alimentar y comprar son labores de otras etapas."),
        ("abc", "En Acuicultura: ¿qué es la inocuidad de un alimento?", "Que no cause daño a quien lo consume", "Que tenga un color atractivo", "Que sea el más barato del mercado", "La inocuidad se refiere a no dañar al consumidor, no al color ni al precio."),
        ("abc", "En Acuicultura: ¿qué es la cadena de frío?", "Mantener el producto frío de manera continua desde la cosecha hasta el consumidor", "Congelar el producto una sola vez al final del proceso", "Guardar el producto a temperatura ambiente durante el día", "La cadena de frío es continua; una interrupción puede afectar la calidad y la inocuidad."),
        ("=", "En la cámara de frío de ejemplo cada estante admite 8 cajas y hay 40 cajas para guardar. ¿Cuántos estantes se necesitan?", "40//8", "Se divide el total de cajas entre las que admite cada estante.", " estantes"),
        ("abc", "{F} ¿Cuál es el riesgo asociado a la carga suspendida de la grúa?", "Que la carga caiga sobre una persona y la golpee", "La grúa guardada en su lugar", "Que las cajas se enfríen demasiado rápido", "El riesgo es la posibilidad de daño; la grúa guardada es el equipo y el frío es otro tema."),
        ("abc", "{F} Una barrera fija que impide el paso bajo la zona de carga, instalada por personal autorizado, es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una norma escrita", "De EPP, porque protege a quien se acerca", "La barrera modifica el lugar y no depende de que cada persona la recuerde."),
        ("abc", "{F} Que el personal use calzado antideslizante para el piso con agua y hielo es un control de tipo:", "EPP, porque protege solo a quien lo usa", "De ingeniería, porque cambia el piso", "De eliminación, porque quita el hielo", "El calzado no cambia el piso: protege a quien lo lleva."),
        ("abc", "{F} Un compañero dice: «leí la ficha, así que puedo manejar la grúa». ¿Qué respuesta es correcta?", "Es falso: usar equipos de levante exige personal autorizado y norma vigente", "Es cierto, si usa casco", "Es cierto, si otra persona la mira", "Leer una ficha no habilita para operar equipos; el casco o la compañía tampoco."),
        ("abc", "{F} Durante una visita de ejemplo, una persona queda atrapada bajo una caja que cayó de la carga. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Meterte bajo la carga a levantar la caja", "Tirar de la persona sin avisar a nadie", "Acercarse bajo una carga puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("=", "La planta de ejemplo procesa 6.000 kg por día en 4 turnos iguales. ¿Cuántos kg procesa cada turno?", "6000//4", "Se divide el total diario entre el número de turnos.", " kg"),
        ("abc", "En Acuicultura: ¿por qué se mantiene la cadena de frío hasta el consumidor?", "Para conservar la calidad y la inocuidad del producto", "Para que los animales crezcan más rápido", "Para reducir el peso de las cajas", "El frío continuo cuida la calidad y la inocuidad."),
        ("abc", "{F} ¿Qué medida de nivel más efectivo se podría sumar a un letrero que advierte «no pasar bajo la carga»?", "Una barrera física fija instalada por personal autorizado", "Otro letrero con letras más grandes", "Pedir a cada persona que use casco", "La barrera es un control de ingeniería; el letrero es administrativo y el casco es EPP."),
        ("abc", "En Acuicultura: ¿qué exige el manejo ético durante la cosecha?", "Evitar sufrimiento innecesario, cumplir la norma vigente y que lo haga personal autorizado", "Terminar lo antes posible aunque no se cumpla la norma", "Que lo haga cualquier persona con buena voluntad", "El manejo ético se apoya en la norma y en personal autorizado."),
    ],
    ctx=("abc", "Una conocida te ofrece pagarte por ayudar en la cosecha de su centro de cultivo el fin de semana, en el muelle con una grúa. ¿Qué respondes?", "Que no, porque esa tarea exige personal autorizado, norma vigente y elementos de protección, y que lo consultarás con un adulto responsable", "Que sí, porque verás cómo lo hacen otros", "Que sí, si usas casco", "Haber visto el concepto en clases no habilita para trabajar en un muelle con equipos de levante."),
    sc=[
        ("En Acuicultura: ¿qué es la cosecha?", "La extracción de los animales cuando alcanzan el tamaño comercial", "Es la etapa final del cultivo."),
        ("¿Qué es la cadena de frío?", "Mantener el frío de manera continua hasta el consumidor", "La cadena de frío cuida la calidad y la inocuidad."),
        ("¿Qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
    ],
    op=("La planta ficticia «Planta Demo» anota una tarea de ejemplo: pasar con cajas por un pasillo con agua y hielo, junto a una zona donde cuelga una carga. Escribe (a) el peligro del pasillo y el riesgo asociado, (b) un control administrativo, (c) un control de ingeniería, (d) por qué el EPP no basta y quién hace la tarea.",
        "(a) Peligro: pasillo con agua y hielo; riesgo: que la persona resbale, caiga y se lastime. (b) Una regla escrita y señales que prohíban el paso bajo la carga y exijan avisar al cruzar. (c) Una barrera fija y un piso antideslizante instalados por personal autorizado. (d) El EPP es la última barrera: no quita el peligro y protege solo a quien lo usa; la tarea la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer solo el EPP", "no aclarar que la tarea la hace personal autorizado"],
        "Pregunta: «¿qué control cambia el lugar y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el último párrafo."),
    reinforce="Escribe en tus palabras qué es la cadena de frío y por qué importa para la inocuidad.",
    extend="Explica con un ejemplo por qué una barrera fija es mejor que un letrero solo.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (registro de ejemplo, inventado). Planta Demo, lote de cosecha C-12 de «especie A», proveniente de la jaula J-5: 4.000 peces con un peso vivo total de 16.000 kg. Después de clasificar y procesar quedan 12.000 kg de producto, empacados en cajas de 20 kg. "
     "Documentos: el registro de cosecha (lote, jaula, cantidad y fecha), la guía de despacho (qué se envía, cuánto, desde dónde y hacia dónde) y la ficha de calidad (tamaño, aspecto y frescura según el estándar).")
build(
    O3, 2, F,
    use="Aprenderé los conceptos de rendimiento, merma y lote de cosecha, los documentos de la cosecha y los roles de quienes participan.",
    prior=["Sé qué es la cosecha y la trazabilidad.", "Sé calcular un porcentaje con números enteros.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "El rendimiento de un proceso es el porcentaje de producto útil que se obtiene respecto de lo que entró: se calcula producto obtenido × 100 ÷ producto de entrada. La merma es la parte que se pierde o se descarta, es decir, la diferencia entre lo que entra y lo que se obtiene. Un lote de cosecha es el grupo de animales cosechados juntos, de una misma jaula y fecha, lo que permite la trazabilidad.",
        "Los documentos de la cosecha son tres. El registro de cosecha anota lote, jaula, cantidad y fecha. La guía de despacho acompaña el envío y dice qué se envía, cuánto, desde dónde y hacia dónde. La ficha de calidad anota tamaño, aspecto y frescura según el estándar. Todos se completan con datos reales, sin borrar ni cambiar cifras.",
        f"Los roles se reparten así: el jefe de cosecha organiza la jornada, el encargado de calidad revisa los estándares, el prevencionista asesora en riesgos y el personal autorizado ejecuta las labores. {EMER} {AVISO}",
    ],
    vocab=[("rendimiento", "porcentaje de producto útil obtenido respecto del producto de entrada"), ("merma", "parte que se pierde o se descarta en un proceso"), ("lote de cosecha", "grupo de animales cosechados juntos, de una misma jaula y fecha"), ("registro de cosecha", "documento con lote, jaula, cantidad y fecha"), ("guía de despacho", "documento que acompaña un envío: qué, cuánto, desde dónde y hacia dónde"), ("ficha de calidad", "documento con tamaño, aspecto y frescura según el estándar"), ("peso vivo", "peso de los animales antes del proceso")],
    worked=[
        ("Calcular rendimiento", "Entran 500 kg de producto y se obtienen 350 kg útiles. ¿Cuál es el rendimiento?", ["350 × 100 = 35.000.", "35.000 ÷ 500 = 70."], "70 %"),
        ("Elegir el documento", "El encargado de una planta de ejemplo quiere saber a qué destino se envió una carga y cuántos kilos llevaba. ¿Qué documento consulta?", ["Destino y cantidad del envío son datos de un documento de traslado.", "Eso se anota en la guía de despacho."], "La guía de despacho"),
    ],
    mistakes=[("Calcular el rendimiento dividiendo el producto obtenido entre el producto obtenido.", "El rendimiento compara lo obtenido con lo que entró, no consigo mismo.", "Divide el producto obtenido entre el producto de entrada."),
              ("Anotar una cantidad en la guía distinta de la del registro para que «cuadre».", "Las cifras deben ser reales y coincidir entre documentos; una diferencia se investiga.", "Si no coinciden, se informa al encargado con ambos documentos.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es el rendimiento de un proceso?", "El porcentaje de producto útil obtenido respecto del que entró", "El tiempo que demora el proceso", "El costo de cada kilo de producto", "El rendimiento compara lo obtenido con lo que entró."),
        ("abc", "En Acuicultura: ¿qué es la merma?", "La parte que se pierde o se descarta en un proceso", "El producto que se vende primero", "El peso de las cajas vacías", "La merma es la diferencia entre lo que entra y lo que se obtiene."),
        ("abc", "En Acuicultura: ¿para qué sirve la guía de despacho?", "Para acompañar un envío e indicar qué se envía, cuánto, desde dónde y hacia dónde", "Para registrar los pesos del muestreo de una jaula", "Para fijar la densidad máxima de cultivo", "La guía acompaña el envío; el muestreo y la densidad son otros documentos."),
        ("=", "{F} ¿Cuántas cajas de 20 kg se llenan con el producto obtenido?", "12000//20", "Se divide el producto obtenido entre los kilos de cada caja.", " cajas"),
        ("=", "{F} ¿Cuántos kg de merma tuvo el lote?", "16000-12000", "Se resta el producto obtenido al peso vivo.", " kg"),
        ("=", "{F} ¿Cuál es el rendimiento del lote, en %?", "12000*100//16000", "Se multiplica el producto obtenido por 100 y se divide entre el peso vivo.", " %"),
        ("=", "{F} ¿Cuál es el peso medio de un pez del lote, en kg?", "16000//4000", "Se divide el peso vivo total entre el número de peces.", " kg"),
        ("abc", "{F} ¿Qué documento anota el lote, la jaula, la cantidad y la fecha de la cosecha?", "El registro de cosecha", "La ficha de calidad", "La guía de despacho", "El registro de cosecha identifica el lote; la ficha mide calidad y la guía acompaña el envío."),
        ("abc", "{F} ¿Qué documento anota el tamaño, el aspecto y la frescura del producto?", "La ficha de calidad", "El registro de cosecha", "La guía de despacho", "La ficha de calidad registra los estándares del producto."),
        ("abc", "{F} ¿Qué rol revisa los estándares de calidad?", "El encargado de calidad", "El prevencionista", "El jefe de cosecha", "El encargado de calidad revisa estándares; el prevencionista asesora en riesgos y el jefe organiza."),
        ("=", "{F} Si 500 kg del producto se descartan en la revisión de calidad, ¿cuántos kg quedan para empacar?", "12000-500", "Se resta lo descartado al producto obtenido.", " kg"),
        ("abc", "{F} La guía de despacho dice 12.000 kg y el registro anota 11.500 kg. ¿Qué corresponde?", "Informar la diferencia al encargado con ambos documentos, sin cambiar cifras", "Cambiar la guía a 11.500 sin avisar", "Esperar a que nadie lo note", "Una diferencia se informa con evidencia; ocultarla impide corregirla."),
        ("abc", "{F} Un compañero propone cambiar el origen de las cajas a otra jaula porque «se vende mejor». ¿Qué respondes?", "Que no, porque el origen real debe quedar anotado para la trazabilidad", "Que sí, si lo corrige después", "Que sí, porque el cliente no lo revisa", "Alterar el origen rompe la trazabilidad y puede ocultar un problema."),
    ],
    ctx=("abc", "Una compañera te propone anotar en la ficha de calidad que el lote «cumple todo» sin haber revisado nada, para terminar antes. ¿Qué respondes?", "Que no, porque anotar datos que no se revisaron falsifica un registro, y que se lo contarás a un adulto responsable", "Que sí, pero solo en las filas más fáciles", "Que sí, si después revisa en la bodega", "Un registro falso oculta la realidad y puede afectar a quien consume el producto."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula el rendimiento?", "Producto obtenido × 100 ÷ producto de entrada", "El rendimiento compara lo obtenido con lo que entró."),
        ("¿Qué es la merma?", "La parte que se pierde o se descarta", "Es la diferencia entre lo que entra y lo que se obtiene."),
        ("¿Qué se hace con una diferencia entre dos documentos?", "Se informa con ambos documentos, sin cambiar cifras", "Una diferencia se investiga y no se oculta."),
    ],
    op=("Ficha de ejemplo: lote de cosecha C-20 de «especie B»: peso vivo de 9.000 kg y producto obtenido de 6.300 kg, empacado en cajas de 30 kg. Escribe (a) el rendimiento, (b) la merma, (c) cuántas cajas se llenan, (d) qué documento acompaña el envío y qué dice.",
        "(a) 6.300 × 100 ÷ 9.000 = 70 %. (b) 9.000 − 6.300 = 2.700 kg. (c) 6.300 ÷ 30 = 210 cajas. (d) La guía de despacho: qué se envía, cuánto, desde dónde y hacia dónde.",
        ["calcula el rendimiento", "calcula la merma", "calcula las cajas", "nombra el documento"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre el producto obtenido", "confundir la merma con el rendimiento", "confundir la guía con el registro"],
        "Pregunta: «¿entre qué cantidad divides para el rendimiento?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un lote con peso vivo y producto obtenido, y calcula su rendimiento y su merma.",
    extend="Explica por qué la guía de despacho y el registro de cosecha deben coincidir.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (registro de ejemplo, inventado). Planta Demo, revisión de calidad de tres lotes de cosecha. Lote 1: ingresan 10.000 kg y se aprueban 9.500 kg. Lote 2: ingresan 8.000 kg y se aprueban 6.400 kg. "
     "Lote 3: ingresan 6.000 kg y se aprueban 5.400 kg. Meta mínima de ejemplo: 90 % del producto aprobado. Precio de ejemplo del producto: $2.000 por kg.")
build(
    O3, 3, F,
    use="Aprenderé a analizar el registro de calidad de varios lotes de cosecha: calcular el porcentaje aprobado, compararlo con la meta y proponer causas probables que hay que comprobar.",
    prior=["Sé calcular un porcentaje con números enteros.", "Sé qué es la trazabilidad y la merma.", "Sé qué es una causa probable."],
    explain=[
        "Analizar un caso en papel significa leer los datos, compararlos con lo esperado, decidir qué significan y proponer acciones. El porcentaje aprobado de un lote es lo aprobado × 100 ÷ lo que ingresó. La meta mínima es el menor valor aceptable: un lote cumple si su porcentaje es igual o mayor que la meta. El producto no aprobado se llama desvío de calidad y representa una pérdida de dinero, que se calcula multiplicando los kilos desviados por el precio.",
        "Si un lote queda bajo la meta, la trazabilidad permite volver a su jaula y su fecha de cosecha para buscar causas probables, que son explicaciones posibles que hay que comprobar con más registros, sin darlas por ciertas. Se informa al encargado de calidad con los registros como respaldo; las cifras nunca se cambian para que cumplan la meta.",
        f"Estas decisiones las toman el encargado de calidad y la jefatura; aquí razonas con datos escritos. {EMER} {AVISO}",
    ],
    vocab=[("porcentaje aprobado", "lo aprobado por 100 dividido entre lo que ingresó"), ("meta mínima", "menor valor aceptable"), ("desvío de calidad", "producto que no cumple el estándar y se aparta"), ("trazabilidad", "posibilidad de volver al origen de un lote"), ("causa probable", "explicación posible que todavía hay que comprobar")],
    worked=[
        ("Porcentaje aprobado", "Ingresan 2.000 kg y se aprueban 1.800 kg. ¿Cuál es el porcentaje aprobado?", ["1.800 × 100 = 180.000.", "180.000 ÷ 2.000 = 90."], "90 %"),
        ("Desvío en dinero", "Se desvían 100 kg de producto de precio $3.000 por kg. ¿Cuánto dinero se pierde?", ["Se multiplican los kilos desviados por el precio.", "100 × 3.000 = 300.000."], "$300.000"),
    ],
    mistakes=[("Concluir que la causa de un lote bajo es el cansancio del personal solo porque coincidió con ese día.", "Que dos hechos coincidan no prueba que uno cause el otro.", "Anótala como causa probable y compruébala con más datos."),
              ("Subir los kilos aprobados para que el lote cumpla.", "El dato real es la base de la decisión.", "Se deja el dato y se informa al encargado.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es el porcentaje aprobado de un lote?", "Lo aprobado por 100 dividido entre lo que ingresó", "El precio de cada kilo de producto", "El peso de las cajas aprobadas", "El porcentaje aprobado compara lo aprobado con lo que ingresó."),
        ("abc", "En Acuicultura: ¿qué es un desvío de calidad?", "Producto que no cumple el estándar y se aparta", "Un cambio de ruta en el transporte", "El nombre de la jaula de origen", "El desvío es el producto no aprobado."),
        ("abc", "En Acuicultura: ¿para qué sirve la trazabilidad cuando un lote queda bajo la meta?", "Para volver a su jaula y fecha de cosecha y buscar causas probables", "Para calcular el precio de venta de cada caja", "Para reemplazar la ficha de calidad del lote", "La trazabilidad permite investigar el origen del problema."),
        ("=", "{F} ¿Cuál es el porcentaje aprobado del lote 2? (en %)", "6400*100//8000", "Se multiplican los kilos aprobados por 100 y se dividen entre los que ingresaron.", " %"),
        ("=", "{F} ¿Cuál es el porcentaje aprobado del lote 3? (en %)", "5400*100//6000", "Se multiplican los kilos aprobados por 100 y se dividen entre los que ingresaron.", " %"),
        ("abc", "{F} ¿Qué lote quedó bajo la meta mínima?", "El lote 2", "El lote 1", "El lote 3", "El lote 2 tiene 80 %, menor que 90 %; el lote 1 tiene 95 % y el lote 3 tiene 90 %, que cumple."),
        ("=", "{F} ¿Cuántos kg se desviaron en el lote 2?", "8000-6400", "Se resta lo aprobado a lo que ingresó.", " kg"),
        ("=", "{F} ¿Cuántos pesos representan los kilos desviados del lote 2, con el precio de ejemplo?", "(8000-6400)*2000", "Se multiplican los kilos desviados por el precio de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuántos kg se desviaron en total entre los tres lotes?", "(10000-9500)+(8000-6400)+(6000-5400)", "Se suman los kilos desviados de cada lote.", " kg"),
        ("abc", "{F} Un compañero afirma: «el lote 2 bajó porque el personal estaba cansado». ¿Qué conclusión es adecuada?", "Es una causa probable que hay que comprobar con más registros", "Queda demostrado porque el lote bajó ese día", "No puede tener ninguna relación con el personal", "Con un solo dato se plantea una causa probable, pero no se prueba."),
        ("abc", "{F} ¿Qué corresponde hacer primero con el dato del lote 2?", "Informarlo al encargado de calidad con los registros como respaldo", "Subir los kilos aprobados para que llegue a 90 %", "No anotar el lote en el registro", "Un dato bajo la meta se informa; cambiarlo u ocultarlo impide mejorar."),
        ("=", "{F} ¿Cuántos kg tendría que haber aprobado como mínimo el lote 2 para cumplir la meta?", "8000*90//100", "Se calcula el 90 % de lo que ingresó.", " kg"),
        ("abc", "{F} Una persona propone anotar 7.200 kg aprobados en el lote 2 para cumplir la meta. ¿Qué respondes?", "Que no: los datos reales no se cambian y se informa el resultado", "Que sí, si lo corrige en el próximo lote", "Que sí, porque la meta es lo importante", "Cambiar un dato oculta el problema y rompe la trazabilidad."),
    ],
    ctx=("abc", "El jefe de una planta de ejemplo te pide quitar de la planilla un lote que salió bajo la meta, antes de una visita. ¿Qué haces?", "No alterar el registro y avisar a un adulto responsable, como tu profesor o profesora de especialidad", "Quitar solo ese lote", "Quitarlo y avisar después", "Alterar un registro oculta la realidad; ante la presión se consulta a un adulto responsable."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula el porcentaje aprobado?", "Aprobado × 100 ÷ ingresado", "El porcentaje compara lo aprobado con lo que ingresó."),
        ("¿Qué es un desvío de calidad?", "Producto que no cumple el estándar", "El desvío es el producto no aprobado."),
        ("¿Qué se hace con un lote bajo la meta?", "Se informa al encargado con los registros", "El dato real permite buscar causas."),
    ],
    op=("Ficha de ejemplo: tres lotes de «especie B». Lote A: ingresan 5.000 kg y se aprueban 4.600 kg. Lote B: ingresan 4.000 kg y se aprueban 3.200 kg. Meta mínima de ejemplo: 85 %. Precio de ejemplo: $2.500 por kg. Escribe (a) el porcentaje aprobado de cada lote, (b) cuál queda bajo la meta, (c) cuántos pesos representan los kg desviados de ese lote, (d) una causa probable que habría que comprobar.",
        "(a) Lote A: 4.600 × 100 ÷ 5.000 = 92 %; lote B: 3.200 × 100 ÷ 4.000 = 80 %. (b) El lote B, porque 80 es menor que 85. (c) 4.000 − 3.200 = 800 kg; 800 × 2.500 = 2.000.000 pesos. (d) Una causa probable es una demora o una interrupción de la cadena de frío antes de la revisión; hay que comprobarla con los registros.",
        ["calcula los porcentajes", "identifica el lote bajo la meta", "calcula el valor de los desvíos", "presenta la causa como probable"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre lo aprobado", "tomar la causa como segura", "olvidar multiplicar por el precio"],
        "Pregunta: «¿cómo sabrías si la causa es la correcta?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa dos lotes con kilos ingresados y aprobados, y calcula el porcentaje aprobado de cada uno.",
    extend="Explica por qué la trazabilidad ayuda a investigar un lote bajo la meta.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (caso de ejemplo, inventado). Planta Demo despacha 15.000 kg de producto aprobado de «especie A». Precio de venta de ejemplo: $2.800 por kg. Costo de proceso de ejemplo: $1.200 por kg. "
     "Costo de transporte de ejemplo: $3.000.000 en total. Cada camión refrigerado de ejemplo transporta 5.000 kg.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio económico con datos de ejemplo: calcular ingresos, costos, margen y camiones necesarios de un despacho, y a registrar el resultado.",
    prior=["Sé calcular rendimiento y porcentaje aprobado.", "Sé multiplicar, sumar, restar y dividir números enteros.", "Sé qué es la guía de despacho."],
    explain=[
        "El ingreso por venta es los kilos vendidos multiplicados por el precio de cada kilo. El costo total es la suma de los costos: los que dependen de los kilos, como el costo de proceso por kilo, y los que no dependen de ellos, como el transporte de un envío. El margen es el ingreso menos el costo total; si es positivo hay ganancia y si es negativo hay pérdida. El margen por kilo es el margen dividido entre los kilos.",
        "Un envío requiere camiones refrigerados para mantener la cadena de frío. La cantidad de camiones se calcula dividiendo los kilos entre la capacidad de cada uno, y el resultado debe cubrir toda la carga. Los resultados se anotan en un registro y se informan a la jefatura; las cifras de esta clase son de ejemplo y los valores reales dependen del mercado.",
        f"Cómo se carga, se estiba y se transporta cada envío lo hace personal autorizado y no se describe aquí. {EMER} {AVISO}",
    ],
    vocab=[("ingreso por venta", "kilos vendidos multiplicados por el precio de cada kilo"), ("costo total", "suma de todos los costos de una operación"), ("margen", "ingreso menos costo total"), ("margen por kilo", "margen dividido entre los kilos vendidos"), ("camión refrigerado", "vehículo que mantiene el frío durante el traslado")],
    worked=[
        ("Calcular margen", "Se venden 1.000 kg a $3.000 por kg y el costo total es $2.000.000. ¿Cuál es el margen?", ["Ingreso: 1.000 × 3.000 = 3.000.000.", "Margen: 3.000.000 − 2.000.000 = 1.000.000."], "$1.000.000"),
        ("Camiones necesarios", "Hay 9.000 kg para enviar y cada camión lleva 3.000 kg. ¿Cuántos camiones se necesitan?", ["Se divide la carga entre la capacidad.", "9.000 ÷ 3.000 = 3."], "3 camiones"),
    ],
    mistakes=[("Calcular el margen sumando ingreso y costo.", "El margen es lo que queda después de pagar los costos.", "Resta el costo total al ingreso."),
              ("Contar el transporte por kilo cuando el dato es un total del envío.", "Un costo total no se multiplica por los kilos.", "Súmalo una sola vez al costo total.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es el ingreso por venta?", "Los kilos vendidos multiplicados por el precio de cada kilo", "Lo que cuesta transportar la carga", "La merma del proceso", "El ingreso es lo que se recibe por vender."),
        ("abc", "En Acuicultura: ¿qué es el margen de un despacho?", "El ingreso menos el costo total", "El ingreso más el costo total", "El costo de cada camión", "El margen es lo que queda después de pagar los costos."),
        ("abc", "En Acuicultura: ¿por qué se usan camiones refrigerados para transportar producto?", "Para mantener la cadena de frío durante el traslado", "Para que la carga pese más", "Para evitar completar la guía de despacho", "El camión refrigerado mantiene el frío; la guía sigue siendo necesaria."),
        ("=", "{F} ¿Cuántos pesos de ingreso por venta tiene el despacho?", "15000*2800", "Se multiplican los kilos por el precio de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta el proceso de todos los kilos?", "15000*1200", "Se multiplican los kilos por el costo de proceso de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total del despacho (proceso más transporte)?", "15000*1200+3000000", "Se suma el costo de proceso y el de transporte.", " pesos"),
        ("=", "{F} ¿Cuál es el margen del despacho?", "15000*2800-(15000*1200+3000000)", "Se resta el costo total al ingreso.", " pesos"),
        ("=", "{F} ¿Cuál es el margen por kilo?", "(15000*2800-(15000*1200+3000000))//15000", "Se divide el margen entre los kilos vendidos.", " pesos"),
        ("=", "{F} ¿Cuántos camiones refrigerados se necesitan?", "15000//5000", "Se divide la carga entre la capacidad de cada camión.", " camiones"),
        ("abc", "{F} Un compañero propone usar menos camiones sobrecargándolos «para ahorrar». ¿Qué corresponde?", "Respetar la capacidad indicada y consultar al encargado", "Cargar más porque nadie lo notará", "Dejar parte de la carga sin camión", "Sobrecargar es inseguro y rompe las reglas; las decisiones de transporte son del encargado."),
        ("abc", "{F} El costo de transporte sube a $4.000.000. ¿Qué ocurre con el margen?", "Baja en $1.000.000", "Sube en $1.000.000", "No cambia porque es un costo fijo", "Un costo mayor reduce el margen en la misma cantidad."),
        ("abc", "{F} La guía de despacho dice 15.000 kg y el registro de calidad aprobó 14.500 kg. ¿Qué es lo más adecuado?", "Informar la diferencia al encargado con ambos documentos, sin cambiar cifras", "Cambiar el registro a 15.000 sin avisar", "Despachar de todas formas sin comentarlo", "Una diferencia entre documentos se informa antes de despachar."),
        ("abc", "{F} Una persona propone cargar los camiones sin completar la guía de despacho «para ir más rápido». ¿Qué respondes?", "Que no, porque la guía respalda el envío y la trazabilidad", "Que sí, si el chofer conoce el destino", "Que sí, si se completa la semana siguiente", "Sin guía no hay respaldo de lo que se envió ni de su origen."),
    ],
    ctx=("abc", "Un vendedor te ofrece comprarte producto «sin guía ni factura» a un precio más conveniente para tu proyecto escolar. ¿Qué haces?", "Rechazo la oferta y lo consulto con mi profesor o profesora, porque sin documentos no hay trazabilidad ni respaldo", "Lo compro si es bastante barato", "Lo compro si es poca cantidad", "Sin documentos no se puede asegurar el origen ni la inocuidad."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula el margen?", "Ingreso menos costo total", "El margen es lo que queda después de pagar los costos."),
        ("¿Cómo se calculan los camiones necesarios?", "Se divide la carga entre la capacidad de cada camión", "La división indica cuántos viajes cubren la carga."),
        ("¿Qué documento acompaña el envío?", "La guía de despacho", "La guía respalda lo que se envía."),
    ],
    op=("Ficha de ejemplo: despacho de 12.000 kg de «especie B» a $3.000 por kg; costo de proceso de ejemplo $1.500 por kg; transporte $2.000.000 en total; cada camión lleva 4.000 kg. Escribe (a) el ingreso, (b) el costo total, (c) el margen, (d) cuántos camiones se necesitan y qué documento acompaña el envío.",
        "(a) 12.000 × 3.000 = 36.000.000 pesos. (b) 12.000 × 1.500 + 2.000.000 = 20.000.000 pesos. (c) 36.000.000 − 20.000.000 = 16.000.000 pesos. (d) 12.000 ÷ 4.000 = 3 camiones; la guía de despacho acompaña el envío.",
        ["calcula el ingreso", "calcula el costo total", "calcula el margen", "calcula camiones y nombra el documento"],
        ["hoja con las cuatro respuestas"],
        ["sumar ingreso y costo", "multiplicar el transporte por los kilos", "olvidar la guía de despacho"],
        "Pregunta: «¿qué restas al ingreso para obtener el margen?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un despacho con kilos, precio y costos, y calcula el margen.",
    extend="Explica por qué un costo total de transporte se suma una sola vez y no por cada kilo.",
)

O4 = "TP-ACUI-3y4-OAE-04"

# ============================================================ OAE-04, clase 1
F = ("Ficha 5 (caso de ejemplo, inventado). El centro ficticio «Captación Demo» tiene una línea de cultivo con colectores y flotadores, sostenida por fondeos, para captar semillas de «especie A» (un molusco de ejemplo). "
     "Peligros anotados: trabajo desde una embarcación, cabos y cadenas con tensión, colectores y flotadores pesados, oleaje y niebla, y frío durante la jornada.")
build(
    O4, 1, F,
    use="Aprenderé qué es la captación de semillas, qué elementos tiene una línea de cultivo y cómo se ordenan las medidas de prevención en esas labores.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé qué es un registro y la trazabilidad.", "Sé calcular un porcentaje con números enteros."],
    explain=[
        "En algunas especies, como ciertos moluscos, las crías se obtienen del ambiente natural. A esas crías pequeñas se les llama semillas. La captación es la obtención de semillas usando colectores, que son dispositivos donde las larvas se fijan y crecen. Los colectores cuelgan de una línea de cultivo, una cuerda larga que se mantiene en su lugar con flotadores, que la sostienen en la superficie, y con fondeos, que son los sistemas de anclaje que la fijan al fondo.",
        "Instalar y mantener estos equipos son labores de riesgo: se hacen desde una embarcación, con cabos y cadenas tensos, piezas pesadas, oleaje y frío. Se prevén con la jerarquía de controles: eliminar el peligro o sustituirlo, controles de ingeniería (por ejemplo, ayudas mecánicas), controles administrativos (planes de trabajo, reglas y horarios) y, al final, el EPP, que incluye el equipo de flotación. El mantenimiento primario son las labores simples y periódicas de cuidado, que hace personal autorizado según el manual del fabricante.",
        f"Este cuaderno no describe cómo se instala una línea ni cómo se trabaja desde una embarcación. {EMER} {AVISO}",
    ],
    vocab=[("semilla", "cría pequeña de un molusco que se obtiene para cultivarla"), ("captación", "obtención de semillas del ambiente natural usando colectores"), ("colector", "dispositivo donde las larvas se fijan y crecen"), ("línea de cultivo", "cuerda larga de la que cuelgan los colectores"), ("flotador", "pieza que mantiene la línea en la superficie"), ("fondeo", "sistema de anclaje que fija la línea al fondo"), ("mantenimiento primario", "labores simples y periódicas de cuidado de un equipo"), ("embarcación", "nave en que se llega al lugar de trabajo en el mar")],
    worked=[
        ("Peligro y riesgo", "En un muelle de ejemplo hay un cabo suelto, tirante y sin señal, junto al borde. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el cabo tirante, que puede causar daño.", "El riesgo es que alguien se enrede o se golpee y caiga al agua."], "Peligro: el cabo tirante; riesgo: que alguien se enrede o se golpee y caiga al agua"),
        ("Clasificar un control", "Un centro de ejemplo exige un plan de trabajo escrito y firmado antes de cada salida a la línea. ¿A qué nivel de la jerarquía corresponde?", ["El plan ordena cómo se trabaja, pero no cambia el lugar.", "Las reglas y los planes de trabajo son controles administrativos."], "Control administrativo"),
    ],
    mistakes=[("Creer que quien vio una línea de cultivo desde la costa puede ayudar a instalar o mantener una.", "Esas labores exigen formación, autorización, equipo de flotación y norma vigente.", "Aprende el concepto y deja la labor a personal autorizado."),
              ("Creer que un chaleco de flotación elimina el peligro de caer al agua.", "El equipo de flotación es EPP: reduce el daño, pero el peligro sigue.", "Se suman controles de ingeniería y reglas de trabajo.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es la captación de semillas?", "La obtención de semillas del ambiente natural usando colectores", "La compra de alimento para los animales jóvenes", "La venta de animales adultos a una planta", "La captación obtiene semillas del medio con colectores; comprar alimento o vender son otras etapas."),
        ("abc", "En Acuicultura: ¿qué es un colector?", "Un dispositivo donde las larvas se fijan y crecen", "Un documento que registra pesos", "Una embarcación pequeña para la línea", "El colector es el dispositivo físico donde se fijan las larvas."),
        ("abc", "En Acuicultura: ¿qué es un fondeo en una línea de cultivo?", "Un sistema de anclaje que fija la línea al fondo", "Una pieza que mantiene la línea en la superficie", "Un registro de las semillas captadas", "El fondeo ancla; la pieza que sostiene en la superficie es el flotador."),
        ("=", "Una línea de ejemplo tiene 6 tramos iguales y 18 colectores en total. ¿Cuántos colectores hay en cada tramo?", "18//6", "Se divide el total de colectores entre el número de tramos.", " colectores"),
        ("abc", "{F} ¿Cuál es el riesgo asociado a los cabos y cadenas con tensión?", "Que un golpe o un enredo lesione a una persona o la haga caer al agua", "El cabo mismo, guardado en su lugar", "Que las semillas se fijen más lento", "El riesgo es la posibilidad de daño; el cabo guardado es el peligro."),
        ("abc", "{F} Una ayuda mecánica instalada por personal autorizado para evitar levantar a mano piezas pesadas es un control de tipo:", "De ingeniería, porque cambia físicamente la forma de trabajar", "Administrativo, porque es una regla escrita", "De EPP, porque protege el cuerpo", "La ayuda mecánica modifica el trabajo y no depende de que cada persona la recuerde."),
        ("abc", "{F} Un horario que evita salir a la línea con niebla es un control de tipo:", "Administrativo, porque ordena cuándo se trabaja", "De ingeniería, porque cambia la línea", "De EPP, porque protege a quien lo usa", "Los horarios y las reglas son controles administrativos."),
        ("abc", "{F} Una estudiante dice: «ya sé qué es un fondeo, así que puedo ayudar a instalar uno». ¿Qué respuesta es correcta?", "Es falso: instalar fondeos exige personal autorizado, equipo de flotación y norma vigente", "Es cierto, si se sube a la embarcación con chaleco", "Es cierto, si hay buen clima", "Conocer el concepto no habilita para trabajar; el chaleco o el clima no reemplazan la autorización."),
        ("abc", "{F} Durante una visita de ejemplo, una persona cae al agua desde la embarcación. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo ni entrar al agua, y avisar a un adulto responsable y a emergencias", "Lanzarte al agua para ayudarla de inmediato", "Esperar un rato a ver si logra salir sola", "Entrar al agua puede producir otro accidente; se avisa a quienes pueden actuar."),
        ("=", "De 24 salidas planificadas al año a la línea de ejemplo, 6 se suspenden por mal tiempo. ¿Qué porcentaje de las salidas se suspende?", "6*100//24", "Se multiplican las salidas suspendidas por 100 y se dividen entre las planificadas.", " %"),
        ("abc", "En Acuicultura: ¿por qué los fondeos y flotadores se revisan con una pauta escrita y no «cuando alguien se acuerda»?", "Porque una pauta fija qué se revisa y cada cuánto, y deja registro", "Porque así se evita usar el manual del fabricante", "Porque el fondeo se puede dejar sin revisión", "La pauta ordena y deja evidencia de lo revisado."),
        ("abc", "En Acuicultura: ¿qué significa que el mantenimiento primario se haga según el manual del fabricante?", "Que se siguen las indicaciones del fabricante para ese equipo", "Que cada persona decide cómo cuidar el equipo", "Que no se lleva ningún registro", "El manual del fabricante dice cómo cuidar el equipo; los registros dejan evidencia."),
        ("abc", "{F} ¿Qué medida de nivel más efectivo se podría sumar a una regla escrita sobre piezas pesadas?", "Una ayuda mecánica instalada por personal autorizado", "Un nuevo cartel con la misma regla", "Pedir a cada persona que use guantes", "La ayuda mecánica es un control de ingeniería; el cartel es administrativo y los guantes son EPP."),
    ],
    ctx=("abc", "Un conocido te invita a su embarcación para «echar una mano» con una línea de cultivo, sin chaleco ni permiso. ¿Qué respondes?", "Que no, porque esa tarea exige personal autorizado, equipo de flotación y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, si el mar está calmo", "Que sí, si vas junto a él", "El mar calmo o la compañía no reemplazan la autorización ni el equipo de flotación."),
    sc=[
        ("En Acuicultura: ¿qué es una semilla?", "Una cría pequeña de un molusco que se obtiene para cultivarla", "La semilla es la cría que se capta con colectores."),
        ("¿Qué es un flotador de la línea?", "Una pieza que mantiene la línea en la superficie", "El flotador sostiene la línea cerca de la superficie."),
        ("¿Qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
    ],
    op=("El centro ficticio «Captación Demo» anota una tarea de ejemplo: salir a revisar una línea de cultivo en una embarcación con oleaje y poca visibilidad. Escribe (a) el peligro y el riesgo asociado, (b) un control administrativo, (c) un control de ingeniería, (d) qué EPP se suma y por qué no basta como único control.",
        "(a) Peligro: oleaje y poca visibilidad en una embarcación; riesgo: que una persona pierda el equilibrio y caiga al agua. (b) Un plan de trabajo escrito y una regla que suspenda la salida con condiciones adversas. (c) Barandas y pasarelas fijas instaladas por personal autorizado. (d) El equipo de flotación; no basta porque es la última barrera y no quita el peligro.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer solo el EPP", "no mencionar el equipo de flotación"],
        "Pregunta: «¿qué control cambia el lugar y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Dibuja con palabras una línea de cultivo: nombra sus cuatro elementos y para qué sirve cada uno.",
    extend="Explica por qué un plan de trabajo escrito no reemplaza una barandilla fija.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 6 (registro de ejemplo, inventado). Captación Demo, línea L-1 con 200 colectores. Documentos del centro: la ficha técnica del colector (especificaciones del fabricante: material, largo y capacidad), "
     "la pauta de mantención (qué se revisa y cada cuánto), la hoja de vida del equipo (historial de revisiones y reparaciones) y el registro de captación (fecha, línea, número de colectores y semillas contadas en una muestra). "
     "Muestra de ejemplo: 10 colectores con 120, 140, 160, 150, 130, 170, 150, 140, 160 y 180 semillas.")
build(
    O4, 2, F,
    use="Aprenderé los documentos de un equipo de captación, qué son las especificaciones técnicas y la hoja de vida, y cómo se estima el total de semillas con una muestra.",
    prior=["Sé qué es un colector, una línea de cultivo y un fondeo.", "Sé calcular un promedio.", "Sé multiplicar números enteros."],
    explain=[
        "Un equipo de captación se maneja con documentos. Las especificaciones técnicas son las características que fija el fabricante: material, tamaño y capacidad de cada pieza; están en la ficha técnica y en el manual. La pauta de mantención indica qué se revisa y cada cuánto tiempo. La hoja de vida es el registro del equipo: cada revisión, reparación y cambio de piezas, con fecha y responsable. El registro de captación anota cuántas semillas se captaron.",
        "Para estimar las semillas de una línea no se cuentan todos los colectores: se cuenta una muestra, se calcula el promedio por colector (suma de los conteos dividida por la cantidad de colectores contados) y se multiplica por el número total de colectores. Es una estimación y no un conteo exacto. Un registro útil dice qué, cuánto, cuándo y quién, y no se altera.",
        f"Los roles: el jefe del centro organiza, el técnico decide las labores, el prevencionista asesora en riesgos y el personal autorizado ejecuta. {EMER} {AVISO}",
    ],
    vocab=[("especificación técnica", "característica que fija el fabricante de un equipo, como material, tamaño o capacidad"), ("ficha técnica", "documento con las especificaciones de un equipo"), ("pauta de mantención", "documento que indica qué se revisa y cada cuánto tiempo"), ("hoja de vida del equipo", "registro de revisiones, reparaciones y cambios de piezas con fecha y responsable"), ("registro de captación", "documento con fecha, línea, colectores y semillas contadas"), ("estimación", "valor aproximado calculado con una muestra")],
    worked=[
        ("Estimar semillas", "En una muestra de ejemplo, 5 colectores tienen 80, 90, 100, 110 y 120 semillas, y la línea tiene 50 colectores. ¿Cuántas semillas se estiman?", ["Promedio: 500 ÷ 5 = 100.", "Total estimado: 100 × 50 = 5.000."], "5.000 semillas"),
        ("Elegir el documento", "El técnico de un centro de ejemplo quiere saber cuándo se reparó un fondeo por última vez. ¿Qué documento consulta?", ["La fecha de una reparación se anota en el historial del equipo.", "Eso está en la hoja de vida del equipo."], "La hoja de vida del equipo"),
    ],
    mistakes=[("Estimar el total de semillas multiplicando solo el conteo del mejor colector por el número de colectores.", "Un solo colector no representa a la línea.", "Se usa el promedio de la muestra."),
              ("Dejar sin anotar una reparación porque «fue algo pequeño».", "Sin registro, la hoja de vida pierde su historial y no se puede planificar.", "Toda revisión y reparación se anota con fecha y responsable.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es una especificación técnica de un equipo?", "Una característica que fija el fabricante, como material, tamaño o capacidad", "La opinión del vendedor sobre el equipo", "El nombre del lote de semillas captadas", "Las especificaciones las fija el fabricante en la ficha técnica."),
        ("abc", "En Acuicultura: ¿para qué sirve la hoja de vida de un equipo?", "Para registrar sus revisiones, reparaciones y cambios de piezas", "Para fijar el precio de venta de las semillas", "Para anotar el número de personas de un turno", "La hoja de vida guarda el historial del equipo."),
        ("abc", "En Acuicultura: ¿qué es una estimación de semillas?", "Un valor aproximado calculado con una muestra", "El conteo exacto de cada semilla de la línea", "El peso de los colectores", "La estimación usa una muestra y no cuenta todas las semillas."),
        ("=", "{F} ¿Cuántas semillas se contaron en total en la muestra?", "120+140+160+150+130+170+150+140+160+180", "Se suman los conteos de los diez colectores.", " semillas"),
        ("=", "{F} ¿Cuál es el promedio de semillas por colector de la muestra?", "(120+140+160+150+130+170+150+140+160+180)//10", "Se divide la suma de los conteos entre los 10 colectores.", " semillas"),
        ("=", "{F} Con ese promedio, ¿cuántas semillas se estiman en la línea L-1?", "(120+140+160+150+130+170+150+140+160+180)//10*200", "Se multiplica el promedio de la muestra por los 200 colectores.", " semillas"),
        ("abc", "{F} ¿Qué documento indica qué se revisa y cada cuánto tiempo?", "La pauta de mantención", "El registro de captación", "La ficha técnica del colector", "La pauta fija qué se revisa y cuándo; el registro de captación anota semillas y la ficha técnica da especificaciones."),
        ("abc", "{F} ¿Qué documento tiene las características del fabricante, como el material del colector?", "La ficha técnica del colector", "La hoja de vida del equipo", "La pauta de mantención", "Las especificaciones del fabricante están en la ficha técnica."),
        ("abc", "{F} Un compañero propone contar solo el colector con más semillas y multiplicar por 200. ¿Qué problema tiene?", "Un solo colector no representa a la línea y la estimación sale demasiado alta", "Ninguno, porque cualquier colector sirve", "Que contar semillas no está permitido", "La estimación debe usar el promedio de una muestra."),
        ("abc", "{F} ¿Qué rol del centro asesora en la prevención de riesgos del trabajo?", "El prevencionista", "El jefe del centro", "El personal autorizado que ejecuta las labores", "El prevencionista asesora en riesgos; el jefe organiza y el personal ejecuta."),
        ("=", "{F} Si la línea tuviera 300 colectores con el mismo promedio, ¿cuántas semillas se estimarían?", "(120+140+160+150+130+170+150+140+160+180)//10*300", "Se multiplica el promedio por los 300 colectores.", " semillas"),
        ("abc", "{F} Se reparó un fondeo y nadie lo anotó en la hoja de vida. ¿Qué problema tiene?", "Se pierde el historial y no se puede planificar la próxima revisión", "Ninguno, porque lo importante es que quedó reparado", "Que el fondeo ya no se podrá usar", "Sin registro no se sabe qué se hizo ni cuándo corresponde revisar."),
        ("abc", "{F} Un compañero dice: «leí la ficha técnica, así que puedo reparar un fondeo yo solo». ¿Qué respuesta es correcta?", "Es falso: las reparaciones las hace personal autorizado según el manual del fabricante", "Es cierto, porque la ficha trae toda la información", "Es cierto, si lleva guantes", "Una ficha informa, pero no reemplaza la formación ni la autorización."),
    ],
    ctx=("abc", "Una compañera te propone anotar en la hoja de vida que se hizo una revisión que no se hizo, para tener la pauta «al día». ¿Qué respondes?", "Que no, porque anotar algo que no se hizo es falsificar un registro, y que se lo contarás a un adulto responsable", "Que sí, si después hace la revisión", "Que sí, pero con fecha de la semana anterior", "Un registro falso oculta la realidad y puede esconder un riesgo."),
    sc=[
        ("En Acuicultura: ¿qué es la hoja de vida de un equipo?", "El registro de sus revisiones, reparaciones y cambios de piezas", "La hoja guarda el historial del equipo."),
        ("¿Cómo se estima el total de semillas de una línea?", "Promedio de la muestra por el número de colectores", "El promedio de la muestra representa a la línea."),
        ("¿Qué indica la pauta de mantención?", "Qué se revisa y cada cuánto tiempo", "La pauta ordena qué revisiones se hacen y cuándo."),
    ],
    op=("Ficha de ejemplo: línea L-4 con 120 colectores. Muestra de 5 colectores con 100, 110, 90, 120 y 130 semillas. Escribe (a) el promedio de la muestra, (b) las semillas estimadas en la línea, (c) en qué documento se anota la estimación, (d) qué documento consultarías para saber cuándo se revisó por última vez un fondeo.",
        "(a) 100 + 110 + 90 + 120 + 130 = 550; 550 ÷ 5 = 110 semillas. (b) 110 × 120 = 13.200 semillas. (c) En el registro de captación. (d) En la hoja de vida del equipo.",
        ["calcula el promedio", "estima el total", "nombra el documento de captación", "nombra la hoja de vida"],
        ["hoja con las cuatro respuestas"],
        ["usar la suma como promedio", "multiplicar por los colectores de la muestra", "confundir la hoja de vida con la pauta"],
        "Pregunta: «¿por qué se usa el promedio y no el mejor colector?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una muestra de cinco colectores, calcula su promedio y estima el total de una línea de 80 colectores.",
    extend="Explica por qué una estimación con muestra no es un conteo exacto.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 7 (registro de ejemplo, inventado). Captación Demo, resultados de la temporada para tres líneas. Línea L-1: 120 colectores y 18.000 semillas captadas. Línea L-2: 100 colectores y 8.000 semillas. "
     "Línea L-3: 80 colectores y 12.000 semillas. Meta de ejemplo: al menos 100 semillas por colector. Datos anotados: la línea L-2 está más cerca de la desembocadura de un río.")
build(
    O4, 3, F,
    use="Aprenderé a analizar el registro de captación de varias líneas: calcular las semillas por colector, compararlas con una meta y proponer causas probables que hay que comprobar.",
    prior=["Sé qué es la captación y un colector.", "Sé calcular un promedio con números enteros.", "Sé qué es una causa probable."],
    explain=[
        "Analizar un caso en papel significa leer los datos, compararlos con lo esperado, decidir qué significan y proponer acciones. Las semillas por colector de una línea se calculan dividiendo las semillas captadas entre el número de colectores. La meta de ejemplo es el valor mínimo que se espera. Una línea que queda bajo la meta tiene una desviación y se informa al técnico con los registros como respaldo.",
        "Para explicar una desviación se piensa en causas probables: por ejemplo, la ubicación de la línea, la época de instalación de los colectores o el estado de los equipos. Cada una es solo una hipótesis hasta comprobarla con más registros: que dos hechos coincidan no prueba que uno cause el otro. Los datos reales nunca se cambian para que cumplan la meta.",
        f"Las decisiones de mover o reemplazar equipos las toman el técnico y la jefatura con personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("semillas por colector", "semillas captadas divididas entre el número de colectores"), ("meta", "valor mínimo que se espera alcanzar"), ("desviación", "valor que queda fuera de la meta"), ("hipótesis", "explicación posible que todavía hay que comprobar")],
    worked=[
        ("Semillas por colector", "Una línea de ejemplo con 50 colectores captó 6.000 semillas. ¿Cuántas semillas hay por colector?", ["Se divide las semillas entre los colectores.", "6.000 ÷ 50 = 120."], "120 semillas por colector"),
        ("Comparar con la meta", "Una línea de ejemplo tiene 90 semillas por colector y la meta es 100. ¿Cumple?", ["Se compara 90 con 100.", "90 es menor que 100."], "No cumple: queda 10 semillas bajo la meta"),
    ],
    mistakes=[("Concluir que una línea captó poco por su ubicación solo porque está cerca de un río.", "La cercanía al río es un dato que coincide, pero no prueba la causa.", "Anótala como hipótesis y compruébala con más temporadas."),
              ("Subir el número de semillas de una línea para que cumpla la meta.", "El dato real es la base de cualquier decisión.", "Se deja el dato y se informa al técnico.")],
    T=[
        ("abc", "En Acuicultura: ¿cómo se calculan las semillas por colector de una línea?", "Dividiendo las semillas captadas entre el número de colectores", "Multiplicando los colectores por los metros de línea", "Sumando todas las semillas de todas las líneas", "El promedio por colector divide las semillas entre los colectores."),
        ("abc", "En Acuicultura: ¿qué es una hipótesis sobre la causa de un resultado bajo?", "Una explicación posible que todavía hay que comprobar", "Una causa que ya está demostrada", "El nombre de la línea afectada", "La hipótesis se comprueba con más datos."),
        ("abc", "En Acuicultura: ¿qué significa que una línea quede bajo la meta?", "Que su resultado es menor que el mínimo esperado", "Que su resultado supera el máximo", "Que no se registró ningún dato", "Bajo la meta es menor que el mínimo esperado."),
        ("=", "{F} ¿Cuántas semillas por colector tuvo la línea L-1?", "18000//120", "Se dividen las semillas entre los colectores.", " semillas"),
        ("=", "{F} ¿Cuántas semillas por colector tuvo la línea L-2?", "8000//100", "Se dividen las semillas entre los colectores.", " semillas"),
        ("=", "{F} ¿Cuántas semillas por colector tuvo la línea L-3?", "12000//80", "Se dividen las semillas entre los colectores.", " semillas"),
        ("abc", "{F} ¿Qué línea quedó bajo la meta de ejemplo?", "La línea L-2", "La línea L-1", "La línea L-3", "La línea L-2 tuvo 80 por colector, menos que 100; las otras tuvieron 150."),
        ("=", "{F} ¿Cuántas semillas habría tenido la línea L-2 si hubiera cumplido justo la meta?", "100*100", "Se multiplican los colectores por la meta de semillas por colector.", " semillas"),
        ("=", "{F} ¿Cuántas semillas se captaron entre las tres líneas?", "18000+8000+12000", "Se suman las semillas de las tres líneas.", " semillas"),
        ("abc", "{F} Un técnico dice que L-2 captó menos por estar cerca de la desembocadura del río. ¿Qué conclusión es adecuada?", "Es una hipótesis que hay que comprobar con más temporadas y más datos", "Queda demostrado porque ese dato coincide", "No puede haber ninguna relación entre ambos datos", "Un solo dato permite plantear una hipótesis, pero no probarla."),
        ("abc", "{F} ¿Qué corresponde hacer con el dato de la línea L-2?", "Informarlo al técnico con el registro como respaldo", "Subir las semillas a 10.000 para que cumpla", "No anotar la línea en el registro", "Una desviación se informa; cambiar u ocultar el dato impide corregir."),
        ("abc", "{F} Una persona propone mover la línea L-2 de lugar por cuenta propia. ¿Qué corresponde?", "Anotar la propuesta e informar al técnico, porque mover equipos es labor de personal autorizado", "Hacerlo de inmediato porque el dato ya muestra el problema", "Esperar a que otra persona lo haga sin comentarlo", "Mover líneas es una labor de riesgo y la decide el técnico."),
        ("abc", "{F} Se quiere comprobar si el estado de los equipos influyó en L-2. ¿Qué documento se consulta?", "La hoja de vida del equipo de esa línea", "La guía de despacho de otra línea", "El precio de venta de la temporada anterior", "La hoja de vida muestra revisiones y reparaciones del equipo."),
    ],
    ctx=("abc", "El jefe de un centro de ejemplo te pide sumar semillas a la línea más baja del registro «para que no se note». ¿Qué haces?", "No alterar el registro y avisar a un adulto responsable, como tu profesor o profesora de especialidad", "Sumar solo unas pocas semillas", "Sumarlas y avisar después", "Alterar un registro oculta la realidad; ante la presión se consulta a un adulto responsable."),
    sc=[
        ("En Acuicultura: ¿cómo se calculan las semillas por colector?", "Semillas captadas ÷ número de colectores", "Es un promedio de semillas por cada colector."),
        ("En acuicultura: ¿qué es una hipótesis?", "Una explicación posible que hay que comprobar", "Una hipótesis se verifica con más datos."),
        ("¿Qué se hace con un dato bajo la meta?", "Se informa al técnico sin cambiarlo", "El dato real permite tomar decisiones."),
    ],
    op=("Ficha de ejemplo: temporada de «especie B». Línea A: 60 colectores y 7.200 semillas. Línea B: 90 colectores y 7.200 semillas. Meta de ejemplo: al menos 100 semillas por colector. Escribe (a) las semillas por colector de cada línea, (b) cuál queda bajo la meta y por cuánto, (c) una hipótesis que explique la diferencia, indicando que hay que comprobarla, (d) qué documento consultarías para revisar los equipos de esa línea.",
        "(a) Línea A: 7.200 ÷ 60 = 120; línea B: 7.200 ÷ 90 = 80. (b) La línea B queda 20 semillas por colector bajo la meta. (c) Una hipótesis es que la ubicación o la época de instalación de B no favoreció la captación; hay que comprobarlo con más datos. (d) La hoja de vida del equipo.",
        ["calcula las semillas por colector", "identifica la línea bajo la meta", "presenta la causa como hipótesis", "nombra la hoja de vida"],
        ["hoja con las cuatro respuestas"],
        ["dividir las semillas entre las líneas", "tomar la causa como segura", "olvidar comparar con la meta"],
        "Pregunta: «¿cómo sabrías si la hipótesis es correcta?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa dos líneas con colectores y semillas, y calcula las semillas por colector de cada una.",
    extend="Explica por qué una buena ubicación aparente no prueba por sí sola que una línea captó más.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 8 (caso de ejemplo, inventado). Pauta de mantención de ejemplo de Captación Demo: revisar los flotadores cada 15 días, los fondeos cada 90 días y reemplazar los colectores con más de 24 meses de uso. "
     "Equipo de la línea L-5 (de ejemplo): 20 flotadores, 4 fondeos y 200 colectores, de los cuales 30 tienen más de 24 meses. Precio de ejemplo de un colector nuevo: $2.500. Plazo de planificación: 360 días.")
build(
    O4, 4, F,
    use="Aprenderé a planificar en papel el mantenimiento primario con una pauta escrita: calcular cuántas revisiones corresponden, qué piezas reemplazar y cuánto costaría, y a registrar el plan.",
    prior=["Sé qué es una pauta de mantención y una hoja de vida.", "Sé multiplicar y dividir números enteros.", "Sé calcular un porcentaje con números enteros."],
    explain=[
        "El mantenimiento primario es el conjunto de labores simples y periódicas de cuidado de un equipo. Se planifica con una pauta de mantención: cada pieza tiene una frecuencia de revisión y un criterio de reemplazo, por ejemplo, un máximo de meses de uso. Las revisiones que corresponden en un plazo se calculan dividiendo los días del plazo entre la frecuencia en días. Los reemplazos se calculan contando cuántas piezas superan el criterio, y su costo se obtiene multiplicando esas piezas por el precio de cada una.",
        "Cada revisión y cada reemplazo se anota en la hoja de vida con fecha y responsable. Si una pieza falla antes de lo previsto se informa al técnico: la pauta puede ajustarla él, no cada persona por su cuenta. Los precios y plazos son de ejemplo.",
        f"Cómo se revisa o se reemplaza cada pieza lo indica el manual del fabricante y lo hace personal autorizado; este cuaderno no lo describe. {EMER} {AVISO}",
    ],
    vocab=[("frecuencia de revisión", "cada cuánto tiempo se revisa una pieza"), ("criterio de reemplazo", "regla que indica cuándo cambiar una pieza, como un máximo de meses de uso"), ("plazo de planificación", "tiempo para el que se prepara un plan"), ("reemplazo", "cambio de una pieza gastada por otra nueva")],
    worked=[
        ("Revisiones en un plazo", "Una pieza de ejemplo se revisa cada 30 días. ¿Cuántas revisiones corresponden en 360 días?", ["Se divide el plazo entre la frecuencia.", "360 ÷ 30 = 12."], "12 revisiones"),
        ("Costo de reemplazo", "Hay que reemplazar 10 piezas de ejemplo y cada una cuesta $4.000. ¿Cuánto cuesta?", ["Se multiplican las piezas por el precio.", "10 × 4.000 = 40.000."], "$40.000"),
    ],
    mistakes=[("Calcular las revisiones dividiendo los días entre el número de piezas.", "Las revisiones dependen de la frecuencia, no de cuántas piezas hay.", "Divide el plazo entre la frecuencia de revisión."),
              ("Cambiar la frecuencia de revisión por cuenta propia porque «la pieza se ve bien».", "La frecuencia la fija la pauta, que el técnico puede ajustar.", "Se informa al técnico y se anota en la hoja de vida.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es la frecuencia de revisión de una pieza?", "Cada cuánto tiempo se revisa", "El precio de cada revisión", "El nombre de quien la revisa", "La frecuencia indica cada cuánto se revisa."),
        ("abc", "En Acuicultura: ¿qué es un criterio de reemplazo?", "Una regla que indica cuándo cambiar una pieza, como un máximo de meses de uso", "El lugar donde se compran las piezas", "El peso máximo de cada pieza", "El criterio dice cuándo corresponde cambiar la pieza."),
        ("abc", "En Acuicultura: ¿qué es el mantenimiento primario?", "Labores simples y periódicas de cuidado de un equipo, hechas según el manual del fabricante", "Reparaciones grandes que cambian el equipo completo", "La compra de equipos nuevos cada año", "El mantenimiento primario son cuidados simples y periódicos."),
        ("=", "{F} ¿Cuántas revisiones de flotadores corresponden en el plazo de planificación?", "360//15", "Se divide el plazo entre la frecuencia de revisión.", " revisiones"),
        ("=", "{F} ¿Cuántas revisiones de fondeos corresponden en el plazo de planificación?", "360//90", "Se divide el plazo entre la frecuencia de revisión.", " revisiones"),
        ("=", "{F} Si el precio de un colector nuevo subiera a $3.000, ¿cuánto costaría reemplazar los colectores que cumplen el criterio?", "30*3000", "Se multiplican los 30 colectores por el nuevo precio.", " pesos"),
        ("=", "{F} ¿Cuánto costaría, en pesos, reemplazar esos colectores?", "30*2500", "Se multiplican los colectores por el precio de cada uno.", " pesos"),
        ("=", "{F} ¿Qué porcentaje de los colectores de la línea cumple el criterio de reemplazo?", "30*100//200", "Se multiplican los colectores por 100 y se dividen entre el total.", " %"),
        ("=", "{F} ¿Cuántos colectores quedan sin necesidad de reemplazo?", "200-30", "Se restan los colectores a reemplazar al total.", " colectores"),
        ("abc", "{F} Un flotador falla antes de su próxima revisión. ¿Qué corresponde?", "Informar al técnico y anotarlo en la hoja de vida", "Esperar a la próxima revisión para no cambiar la pauta", "Cambiar la frecuencia por cuenta propia", "Una falla se informa y se registra; el técnico decide si ajusta la pauta."),
        ("abc", "{F} Una compañera propone no registrar el reemplazo de colectores porque «ya están cambiados». ¿Qué corresponde?", "Registrarlo con fecha y responsable en la hoja de vida", "No registrarlo para ahorrar tiempo", "Registrarlo con una fecha anterior", "Sin registro no hay evidencia ni historial del equipo."),
        ("abc", "{F} Un estudiante calcula las revisiones de fondeos como 360 ÷ 4. ¿Qué error cometió?", "Dividió entre el número de fondeos y no entre la frecuencia de revisión", "Ninguno, el cálculo es correcto", "Dividió entre los flotadores", "Las revisiones dependen de la frecuencia de 90 días, no del número de piezas."),
        ("abc", "{F} Un compañero dice: «con la pauta ya puedo reemplazar los colectores». ¿Qué respuesta es correcta?", "Es falso: la pauta orienta, pero el reemplazo lo hace personal autorizado según el manual", "Es cierto, porque la pauta incluye todo", "Es cierto, si va con un chaleco puesto", "La pauta planifica; la labor es de personal autorizado."),
    ],
    ctx=("abc", "Un conocido te pide que le anotes en papel «cada cuántos días» debe revisar su línea de cultivo y que lo haga solo. ¿Qué respondes?", "Que no puedes fijarlo por él: la frecuencia la define el manual y un técnico autorizado, y que consulte a una persona autorizada", "Que la revise cuando se acuerde", "Que la revise cada 15 días siempre", "La frecuencia depende del equipo y la fija el manual y el técnico."),
    sc=[
        ("En Acuicultura: ¿cómo se calculan las revisiones de un plazo?", "Días del plazo ÷ frecuencia de revisión", "La frecuencia fija cada cuánto se revisa."),
        ("¿Dónde se anota cada revisión o reemplazo?", "En la hoja de vida del equipo", "La hoja guarda el historial completo del equipo."),
        ("¿Quién ajusta una pauta de mantención?", "El técnico", "La pauta se ajusta con decisión técnica."),
    ],
    op=("Ficha de ejemplo: pauta de ejemplo de otro centro: revisar los fondeos cada 60 días y reemplazar los colectores con más de 18 meses; la línea tiene 150 colectores, 45 con más de 18 meses; el colector nuevo cuesta $3.000 (de ejemplo); plazo de 360 días. Escribe (a) cuántas revisiones de fondeos corresponden, (b) cuántos colectores se reemplazan y qué porcentaje es, (c) el costo del reemplazo, (d) dónde se anota todo lo que se haga.",
        "(a) 360 ÷ 60 = 6 revisiones. (b) 45 colectores; 45 × 100 ÷ 150 = 30 %. (c) 45 × 3.000 = 135.000 pesos. (d) En la hoja de vida del equipo, con fecha y responsable.",
        ["calcula las revisiones", "calcula colectores y porcentaje", "calcula el costo", "nombra la hoja de vida"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre el número de piezas", "olvidar el porcentaje", "no mencionar la hoja de vida"],
        "Pregunta: «¿entre qué número divides los días del plazo?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una pauta con una frecuencia de revisión y calcula las revisiones de un año de 360 días.",
    extend="Explica por qué cambiar la frecuencia de una pauta es decisión del técnico y no de cualquier persona.",
)

O5 = "TP-ACUI-3y4-OAE-05"
AV5 = " Este cuaderno no contiene instrucciones de buceo, ni profundidades, tiempos o equipos reales: todo número es de ejemplo para una planilla."

# ============================================================ OAE-05, clase 1
F = ("Ficha 9 (caso de ejemplo, inventado). El centro ficticio «Centro Demo» contrata a una empresa de buceo de ejemplo para tareas subacuáticas: retirar peces muertos de una jaula, revisar una red y revisar una estructura. "
     "Peligros anotados: ahogamiento, hipotermia, falla del equipo de respiración, enredo en la red, corriente, poca visibilidad y tráfico de embarcaciones.")
build(
    O5, 1, F,
    use="Aprenderé qué son las tareas subacuáticas, por qué son de alto riesgo, quiénes intervienen y cómo se ordenan las medidas de prevención, solo como conceptos.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé qué es una balsa jaula y una red de cultivo.", "Sé calcular un porcentaje con números enteros."],
    explain=[
        "Una tarea subacuática es un trabajo que se hace bajo el agua en un centro de cultivo, como revisar redes o estructuras o retirar animales muertos de una jaula. Es una de las labores de más alto riesgo del sector. Solo la realiza un buzo con certificación vigente y aptitud médica vigente, es decir, con documentos que acreditan su formación y su estado de salud, bajo la dirección de un supervisor de buceo, que es la persona responsable de dirigir la tarea y vigilar su seguridad.",
        "Las normas de estas actividades las fija y fiscaliza la autoridad marítima. Entre los peligros están el ahogamiento (falta de aire por estar sumergido), la hipotermia (bajada peligrosa de la temperatura del cuerpo), la falla de un equipo, el enredo en redes, la corriente y la poca visibilidad. La jerarquía de controles pide primero eliminar o sustituir la tarea (por ejemplo, observar con una cámara operada desde la superficie cuando sirve), luego aplicar controles de ingeniería, administrativos (plan de trabajo, supervisor, registros) y, al final, el EPP.",
        f"Nadie debe meterse al agua por su cuenta: ni para ayudar. {EMER}{AV5} {AVISO}",
    ],
    vocab=[("tarea subacuática", "trabajo que se hace bajo el agua en un centro de cultivo"), ("buzo", "persona con certificación vigente para trabajar bajo el agua"), ("supervisor de buceo", "persona responsable de dirigir la tarea de buceo y vigilar su seguridad"), ("autoridad marítima", "institución que fija y fiscaliza las normas de las actividades en el mar"), ("aptitud médica", "documento que acredita que una persona está apta para una tarea según su salud"), ("ahogamiento", "falta de aire por estar sumergido"), ("hipotermia", "bajada peligrosa de la temperatura del cuerpo")],
    worked=[
        ("Peligro y riesgo", "En una jaula de ejemplo la red tiene un tramo suelto y rasgado. ¿Cuál es el peligro y cuál el riesgo para una persona que trabaja allí?", ["El peligro es el tramo suelto, que puede atrapar.", "El riesgo es que la persona se enrede y no pueda salir."], "Peligro: el tramo suelto; riesgo: que la persona se enrede y no pueda salir"),
        ("Clasificar un control", "Un centro de ejemplo exige un supervisor designado y un plan de trabajo escrito antes de cada tarea. ¿A qué nivel de la jerarquía corresponde?", ["Exigir roles y documentos ordena cómo se trabaja.", "Las reglas, los planes y los roles son controles administrativos."], "Control administrativo"),
    ],
    mistakes=[("Creer que saber nadar o tener un chaleco permite ayudar en una tarea subacuática.", "Esas tareas exigen formación, certificación, aptitud médica, supervisor y norma de la autoridad marítima.", "Aprende el concepto y deja la tarea a personal autorizado."),
              ("Creer que si una persona cae al agua hay que entrar a sacarla de inmediato.", "Entrar al agua puede producir otro accidente.", "No te acerques a la zona de riesgo ni entres al agua: avisa a un adulto responsable y a emergencias.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es una tarea subacuática?", "Un trabajo que se hace bajo el agua en un centro de cultivo, como revisar redes o estructuras", "Un trabajo de oficina en el que se llenan planillas del centro", "Un trabajo de limpieza de la sala de proceso", "La tarea subacuática se hace bajo el agua; las planillas y la limpieza se hacen en otros lugares."),
        ("abc", "En Acuicultura: ¿qué es un supervisor de buceo?", "La persona responsable de dirigir la tarea de buceo y vigilar su seguridad", "La persona que compra los equipos del centro", "El buzo que lleva más tiempo en el agua", "El supervisor dirige y vigila; la experiencia por sí sola no basta."),
        ("abc", "En Acuicultura: ¿qué es la hipotermia?", "Una bajada peligrosa de la temperatura del cuerpo", "La pérdida de la vista por poca luz", "La sed intensa durante la jornada", "La hipotermia es el enfriamiento peligroso del cuerpo, un riesgo de trabajar en agua fría."),
        ("=", "En un centro de ejemplo trabajan 24 personas en tareas de superficie y 6 en tareas subacuáticas. ¿Qué porcentaje del personal hace tareas subacuáticas?", "6*100//30", "Se divide el personal subacuático entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Cuál es el riesgo para una persona asociado al peligro «enredo en la red»?", "Que quede atrapada y no pueda salir", "Que la red necesite pintura nueva", "Que la jaula tenga menos peces", "El riesgo es el posible daño a la persona; la pintura y los peces son otros asuntos."),
        ("abc", "{F} Observar la red con una cámara operada desde la superficie, cuando la tarea solo exige mirar, en lugar de enviar a una persona bajo el agua, es una medida de nivel:", "De sustitución, porque cambia la forma de hacer la tarea y reduce el peligro", "De EPP, porque protege el cuerpo", "Administrativo, porque ordena un horario", "Reemplazar la tarea por una menos peligrosa es sustituir."),
        ("abc", "{F} Exigir un supervisor de buceo y un plan escrito antes de cada tarea es una medida de nivel:", "Administrativo, porque ordena cómo se trabaja", "De ingeniería, porque cambia físicamente la red", "De EPP, porque protege el cuerpo", "Los roles, planes y reglas son controles administrativos."),
        ("abc", "{F} Una estudiante dice: «ya sé qué es un buzo, así que puedo ayudar a revisar la red bajo el agua». ¿Qué respuesta es correcta?", "Es falso: solo personal certificado, con supervisor y norma de la autoridad marítima puede hacerlo", "Es cierto, si sabe nadar bien", "Es cierto, si usa chaleco", "Saber nadar o llevar chaleco no habilita para tareas subacuáticas."),
        ("abc", "Durante una visita de ejemplo, ves que una persona cae al agua cerca de una jaula. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo ni entrar al agua, y avisar a un adulto responsable y a emergencias", "Lanzarte al agua para ayudarla de inmediato", "Esperar un rato a ver si logra salir sola", "Entrar al agua puede producir otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "En Acuicultura: ¿para qué sirve exigir una aptitud médica vigente a quien hace tareas subacuáticas?", "Para acreditar que su salud es compatible con una tarea de alto riesgo", "Para reemplazar al supervisor de buceo", "Para fijar el precio de la tarea", "La aptitud médica verifica la salud para la tarea; no reemplaza roles ni fija precios."),
        ("abc", "En Acuicultura: ¿qué es la autoridad marítima?", "La institución que fija y fiscaliza las normas de las actividades en el mar", "La empresa que vende los equipos de buceo", "La persona que dirige el centro de cultivo", "La autoridad marítima fija y fiscaliza las normas; no vende equipos ni dirige el centro."),
        ("abc", "{F} ¿Qué medida de nivel más efectivo se podría sumar a un plan escrito para tareas subacuáticas?", "Sustituir la tarea bajo el agua por una inspección con cámara cuando solo hay que mirar", "Colocar otro cartel con la misma advertencia", "Pedir a cada persona que lleve ropa de abrigo", "La sustitución actúa sobre el peligro; el cartel es administrativo y la ropa es EPP."),
        ("=", "En un año de ejemplo se planifican 36 tareas subacuáticas y 9 se pueden sustituir por inspección con cámara desde la superficie. ¿Qué porcentaje se puede sustituir?", "9*100//36", "Se multiplican las tareas sustituibles por 100 y se dividen entre las planificadas.", " %"),
    ],
    ctx=("abc", "Un conocido te ofrece «bucear a escondidas» para revisar la red de su jaula sin supervisor, porque «es rápido». ¿Qué respondes?", "Que no, porque esa tarea exige personal certificado, supervisor y norma de la autoridad marítima, y que lo consultarás con un adulto responsable", "Que sí, si el agua está tranquila", "Que sí, si vas con un compañero", "La tranquilidad del agua o la compañía no reemplazan la certificación ni el supervisor."),
    sc=[
        ("En Acuicultura: ¿qué es la hipotermia?", "Una bajada peligrosa de la temperatura del cuerpo", "Es un riesgo del trabajo en agua fría."),
        ("¿Quién dirige una tarea de buceo?", "El supervisor de buceo", "El supervisor dirige y vigila la seguridad."),
        ("¿Qué haces si alguien cae al agua?", "No entrar al agua y avisar a un adulto responsable y a emergencias", "Entrar al agua puede producir otro accidente."),
    ],
    op=("El centro ficticio «Centro Demo» planifica una tarea de ejemplo: revisar una red bajo el agua con poca visibilidad y corriente. Escribe (a) el peligro y un riesgo asociado, (b) una medida de sustitución, (c) una medida administrativa, (d) por qué ninguna persona sin certificación debe participar, aunque quiera ayudar.",
        "(a) Peligro: red con poca visibilidad y corriente; riesgo: que la persona se enrede o pierda la orientación. (b) Revisar la red con una cámara operada desde la superficie cuando solo hay que mirar. (c) Exigir un supervisor, un plan de trabajo escrito y un registro de la tarea. (d) Porque la tarea exige formación, certificación, aptitud médica y supervisor, y entrar al agua sin ellos puede causar otro accidente.",
        ["distingue peligro y riesgo", "propone una sustitución", "propone una medida administrativa", "explica por qué no debe participar quien no está certificado"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer solo el EPP", "sugerir que alguien sin certificación entre al agua"],
        "Pregunta: «¿qué medida elimina o reduce el peligro y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe la jerarquía de controles en orden y pon junto a cada nivel un ejemplo inventado para una tarea subacuática.",
    extend="Explica con un ejemplo por qué sustituir una tarea es más efectivo que entregar un equipo de protección.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 10 (registro de ejemplo, inventado). Centro Demo, jornada de tareas subacuáticas. Documentos: certificado del buzo (vigente o vencido), aptitud médica (vigente o vencida), plan de trabajo subacuático, análisis de riesgos de la tarea, "
     "bitácora de buceo (fecha, buzo, supervisor, tarea, inicio y término de cada inmersión) y registro de mortalidad extraída (jaula y cantidad). Bitácora de ejemplo: inmersión 1, 40 minutos; inmersión 2, 35 minutos; inmersión 3, 45 minutos. "
     "Los tiempos son de ejemplo para una planilla y no son valores de trabajo.")
build(
    O5, 2, F,
    use="Aprenderé los documentos y los roles de una tarea subacuática, qué anota una bitácora de buceo y cómo se revisa que un registro cuadre.",
    prior=["Sé qué es una tarea subacuática y un supervisor de buceo.", "Sé sumar y comparar números enteros.", "Sé qué es la trazabilidad."],
    explain=[
        "Una tarea subacuática se respalda con documentos. El certificado del buzo y su aptitud médica deben estar vigentes: un documento vencido es un documento que no cuenta. El plan de trabajo subacuático dice qué se hará, quién participa y qué medidas de seguridad hay. El análisis de riesgos lista los peligros de la tarea y sus controles. La bitácora de buceo anota fecha, buzo, supervisor, tarea y el inicio y término de cada inmersión. El registro de mortalidad extraída anota de qué jaula y cuántos peces muertos se retiraron.",
        "Los roles son distintos. El supervisor de buceo dirige la tarea y vigila la seguridad. El buzo realiza la tarea bajo sus órdenes. El encargado de superficie apoya desde la superficie y mantiene la comunicación. El jefe del centro organiza la producción y el prevencionista asesora en riesgos. Un registro útil dice qué, cuánto, cuándo y quién, y nunca se altera.",
        f"Si algo no cuadra en un registro, se informa al supervisor; no se corrige a escondidas.{AV5} {EMER} {AVISO}",
    ],
    vocab=[("certificado del buzo", "documento que acredita la formación de un buzo"), ("vigente", "que todavía tiene validez"), ("plan de trabajo subacuático", "documento que dice qué se hará, quién participa y qué medidas de seguridad hay"), ("análisis de riesgos", "lista de los peligros de una tarea y sus controles"), ("bitácora de buceo", "registro de cada inmersión con fecha, buzo, supervisor, tarea e inicio y término"), ("encargado de superficie", "persona que apoya desde la superficie y mantiene la comunicación"), ("inmersión", "cada vez que una persona se sumerge para hacer una tarea"), ("registro de mortalidad extraída", "documento con la jaula y la cantidad de peces muertos retirados")],
    worked=[
        ("Sumar tiempos", "Una bitácora de ejemplo anota dos inmersiones de 20 y 30 minutos. ¿Cuántos minutos suman?", ["Se suman las duraciones.", "20 + 30 = 50."], "50 minutos"),
        ("Elegir el documento", "El prevencionista de un centro de ejemplo quiere ver qué peligros se identificaron para una tarea y cómo se controlan. ¿Qué documento consulta?", ["Peligros y controles de una tarea se listan en un documento de riesgos.", "Eso está en el análisis de riesgos."], "El análisis de riesgos"),
    ],
    mistakes=[("Aceptar un certificado vencido «porque el buzo tiene mucha experiencia».", "Un documento vencido no acredita nada; la experiencia no lo reemplaza.", "La tarea no se autoriza hasta que el documento esté vigente."),
              ("Corregir a escondidas una hora de la bitácora que no cuadra.", "Una corrección oculta impide saber qué pasó realmente.", "Se informa al supervisor con el registro como respaldo.")],
    T=[
        ("abc", "En Acuicultura: ¿qué anota una bitácora de buceo?", "Fecha, buzo, supervisor, tarea y el inicio y término de cada inmersión", "El precio de venta de los peces cosechados", "La temperatura de la sala de proceso", "La bitácora registra las inmersiones; el precio y la sala de proceso son otros asuntos."),
        ("abc", "En Acuicultura: ¿qué es el análisis de riesgos de una tarea subacuática?", "Una lista de los peligros de la tarea y sus controles", "Un registro de las semillas captadas", "La fecha en que vence el certificado", "El análisis lista peligros y controles; las semillas y las fechas son otros documentos."),
        ("abc", "En Acuicultura: ¿qué significa que un certificado esté vigente?", "Que todavía tiene validez", "Que fue emitido hace mucho tiempo", "Que lo firmó el jefe del centro", "Vigente quiere decir que aún vale; uno vencido no cuenta."),
        ("=", "{F} ¿Cuántos minutos suman las tres inmersiones de la bitácora?", "40+35+45", "Se suman las duraciones de las tres inmersiones.", " minutos"),
        ("=", "{F} ¿Cuántos minutos más duró la inmersión 3 que la inmersión 2?", "45-35", "Se resta la duración menor a la mayor.", " minutos"),
        ("abc", "{F} ¿Qué documento anota cuántos peces muertos se retiraron y de qué jaula?", "El registro de mortalidad extraída", "El certificado del buzo", "El plan de trabajo subacuático", "El registro de mortalidad anota jaula y cantidad; el certificado y el plan son otros documentos."),
        ("abc", "{F} ¿Qué rol dirige la tarea y vigila la seguridad?", "El supervisor de buceo", "El jefe del centro", "El encargado de superficie", "El supervisor dirige y vigila; el encargado de superficie apoya y el jefe organiza."),
        ("abc", "{F} ¿Qué rol apoya desde la superficie y mantiene la comunicación?", "El encargado de superficie", "El buzo", "El prevencionista", "El encargado de superficie apoya y comunica; el buzo realiza la tarea y el prevencionista asesora."),
        ("=", "{F} El encargado de superficie anotó 90 minutos de trabajo en total. ¿Cuántos minutos faltan o sobran respecto de la suma de la bitácora? (diferencia)", "(40+35+45)-90", "Se resta lo anotado a la suma de la bitácora.", " minutos"),
        ("abc", "{F} La suma de la bitácora y el total anotado por el encargado no coinciden. ¿Qué corresponde?", "Informar la diferencia al supervisor con ambos registros, sin cambiar números", "Cambiar la bitácora para que coincida", "Esperar a que nadie lo note", "Una diferencia entre registros se informa con evidencia y no se corrige a escondidas."),
        ("abc", "{F} El certificado del buzo figura vencido, pero tiene «mucha experiencia». ¿Qué corresponde?", "No autorizar la tarea hasta que el documento esté vigente", "Autorizar la tarea porque la experiencia reemplaza el documento", "Autorizar la tarea si es breve", "Un documento vencido no acredita la formación; la tarea no se autoriza."),
        ("abc", "{F} Un compañero dice: «leí la ficha, así que puedo ser el encargado de superficie en una tarea real». ¿Qué respuesta es correcta?", "Es falso: los roles de una tarea subacuática los ocupa personal capacitado y autorizado", "Es cierto, porque el encargado solo mira", "Es cierto, si lleva chaleco", "Leer una ficha no habilita para ocupar un rol de una tarea de alto riesgo."),
        ("abc", "{F} ¿Qué rol del centro asesora en la prevención de riesgos del trabajo?", "El prevencionista", "El buzo", "El supervisor de buceo", "El prevencionista asesora en riesgos; el buzo realiza la tarea y el supervisor la dirige."),
    ],
    ctx=("abc", "Una compañera te propone anotar en la bitácora inmersiones que no se hicieron, para que el registro de la semana esté «completo». ¿Qué respondes?", "Que no, porque anotar algo que no se hizo es falsificar un registro, y que se lo contarás a un adulto responsable", "Que sí, pero con tiempos cortos", "Que sí, si después hace las inmersiones", "Un registro falso oculta la realidad y puede esconder un riesgo."),
    sc=[
        ("En Acuicultura: ¿qué es un certificado vigente?", "Uno que todavía tiene validez", "Un documento vencido no acredita nada."),
        ("¿Qué rol dirige la tarea subacuática?", "El supervisor de buceo", "El supervisor dirige y vigila la seguridad."),
        ("¿Qué se hace con una diferencia entre dos registros?", "Se informa al supervisor sin cambiar números", "Una diferencia se informa con evidencia."),
    ],
    op=("Ficha de ejemplo: bitácora de una jornada con tres inmersiones de 30, 25 y 20 minutos. El encargado de superficie anotó 80 minutos en total. Escribe (a) la suma de la bitácora, (b) la diferencia con lo anotado por el encargado, (c) qué haces con esa diferencia, (d) qué rol dirige la tarea y qué rol apoya desde la superficie.",
        "(a) 30 + 25 + 20 = 75 minutos. (b) 80 − 75 = 5 minutos de diferencia. (c) Se informa al supervisor con ambos registros como respaldo, sin cambiar números. (d) El supervisor de buceo dirige; el encargado de superficie apoya y mantiene la comunicación.",
        ["suma los tiempos", "calcula la diferencia", "informa sin alterar", "distingue los dos roles"],
        ["hoja con las cuatro respuestas"],
        ["restar en vez de sumar", "corregir a escondidas la diferencia", "confundir al supervisor con el encargado de superficie"],
        "Pregunta: «¿qué haces si dos registros no coinciden?». Si no responde, pídele que relea el último párrafo."),
    reinforce="Escribe tres datos que debe llevar una bitácora de buceo y para qué sirve cada uno.",
    extend="Explica por qué un certificado vencido no se reemplaza por la experiencia de quien lo tiene.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 11 (caso de ejemplo, inventado). El supervisor de un centro de ejemplo revisa en papel una lista de verificación de 10 documentos antes de autorizar una tarea subacuática. "
     "Resultado: 1 certificado del buzo, vigente. 2 aptitud médica, vencida. 3 supervisor designado, sí. 4 plan de trabajo firmado, sí. 5 análisis de riesgos, no existe. 6 encargado de superficie designado, sí. "
     "7 plan de comunicación, sí. 8 plan de emergencia con aviso a emergencias, sí. 9 autorización o aviso a la autoridad marítima según la norma vigente, no existe. 10 registro de mortalidad previsto, sí.")
build(
    O5, 3, F,
    use="Aprenderé a analizar una lista de verificación de documentos antes de una tarea subacuática, a decidir si se puede autorizar y a informar lo que falta.",
    prior=["Sé qué documentos respaldan una tarea subacuática.", "Sé calcular un porcentaje con números enteros.", "Sé qué es una causa probable."],
    explain=[
        "Una lista de verificación es un documento con los elementos que deben estar listos antes de una tarea; cada uno se marca como cumplido o no cumplido. El porcentaje de cumplimiento es los elementos cumplidos × 100 ÷ el total. La regla de este caso es que una tarea de alto riesgo no se autoriza hasta que todos los elementos estén cumplidos, es decir, hasta que el cumplimiento sea 100 %.",
        "Si faltan elementos, la decisión es no autorizar y informar al supervisor y al prevencionista qué falta. Nadie «completa» a escondidas un documento: un análisis de riesgos o una autorización se elaboran de verdad y los firma quien corresponde. Una causa probable de que falten documentos puede ser la falta de planificación; hay que comprobarlo y proponer una mejora, como una lista que se revise con anticipación.",
        f"Esta clase trabaja solo con la revisión de papeles; no incluye ninguna tarea bajo el agua.{AV5} {EMER} {AVISO}",
    ],
    vocab=[("lista de verificación", "documento con los elementos que deben estar listos antes de una tarea"), ("cumplimiento", "porcentaje de elementos que están listos"), ("autorizar", "dar permiso para realizar una tarea cuando todo lo exigido está en regla"), ("elemento faltante", "documento o condición exigida que todavía no está")],
    worked=[
        ("Calcular cumplimiento", "Una lista de ejemplo tiene 20 elementos y 15 están cumplidos. ¿Cuál es el cumplimiento?", ["15 × 100 = 1.500.", "1.500 ÷ 20 = 75."], "75 %"),
        ("Decidir", "Una lista de ejemplo tiene un elemento obligatorio sin cumplir. ¿Se autoriza la tarea de alto riesgo?", ["La regla exige que todos los elementos estén cumplidos.", "Falta uno, por lo que no se autoriza."], "No se autoriza hasta que se cumpla"),
    ],
    mistakes=[("Autorizar la tarea porque «ya casi está todo».", "Una tarea de alto riesgo exige todos los elementos cumplidos.", "No se autoriza hasta completar la lista."),
              ("Completar un documento faltante a escondidas solo para marcarlo como cumplido.", "Un documento hecho sin análisis real no protege a nadie y falsifica la lista.", "Se elabora de verdad con quien corresponde y se informa.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es una lista de verificación previa a una tarea?", "Un documento con los elementos que deben estar listos antes de la tarea", "Un registro de las ventas del mes", "Un plano del fondo del mar", "La lista de verificación comprueba que todo esté listo antes de actuar."),
        ("abc", "En Acuicultura: ¿qué es el cumplimiento de una lista de verificación?", "El porcentaje de elementos que están listos", "El número de personas que firmaron", "La duración de la tarea", "El cumplimiento mide cuántos elementos están listos respecto del total."),
        ("abc", "En Acuicultura: ¿cuándo se autoriza una tarea subacuática, según la regla de este caso?", "Cuando todos los elementos de la lista están cumplidos", "Cuando la mayoría de los elementos está cumplida", "Cuando el buzo asegura que está listo", "La regla exige cumplimiento total para una tarea de alto riesgo."),
        ("=", "{F} ¿Cuántos elementos de la lista están cumplidos?", "10-3", "Se restan los elementos faltantes al total de 10.", " elementos"),
        ("=", "{F} ¿Cuál es el porcentaje de cumplimiento de la lista?", "7*100//10", "Se multiplican los elementos cumplidos por 100 y se dividen entre el total.", " %"),
        ("abc", "{F} ¿Cuáles son los elementos que faltan o no están en regla?", "La aptitud médica vencida, el análisis de riesgos y la autorización o aviso", "Solo el análisis de riesgos", "El certificado del buzo y el plan de comunicación", "Los elementos 2, 5 y 9 no están cumplidos; los demás sí."),
        ("abc", "{F} ¿Qué decisión corresponde con ese resultado?", "No autorizar la tarea e informar al supervisor y al prevencionista qué falta", "Autorizar la tarea porque el cumplimiento es mayor que la mitad", "Autorizar la tarea si es muy breve", "Con elementos faltantes la tarea de alto riesgo no se autoriza."),
        ("=", "{F} ¿Cuántos puntos porcentuales faltan para llegar al cumplimiento total?", "100-7*100//10", "Se resta el cumplimiento al 100 % exigido.", " puntos"),
        ("abc", "{F} Un compañero propone marcar «cumplido» el análisis de riesgos sin elaborarlo para llegar a 80 %. ¿Qué respondes?", "Que no: no se marca un documento que no existe y se informa lo que falta", "Que sí, si después lo elabora", "Que sí, porque nadie lo revisa", "Marcar algo no cumplido falsifica la lista y deja la tarea sin protección."),
        ("abc", "{F} La aptitud médica está vencida y el buzo dice que se siente bien. ¿Qué corresponde?", "No autorizar hasta que la aptitud médica esté vigente", "Autorizar porque el buzo se siente bien", "Autorizar si la tarea es corta", "La sensación personal no reemplaza un documento vigente."),
        ("abc", "{F} Una posible causa de que falten tres documentos es la falta de planificación. ¿Qué conclusión es adecuada?", "Es una causa probable que hay que comprobar y proponer una mejora, como revisar la lista con anticipación", "Queda demostrado y no hay nada que hacer", "No puede haber relación con la planificación", "Una causa probable se verifica y se corrige con una medida."),
        ("abc", "{F} Una persona propone que el propio buzo firme los tres documentos faltantes para avanzar. ¿Qué corresponde?", "Que cada documento lo elabore y firme quien corresponde según la norma", "Que el buzo los firme porque conoce la tarea", "Que se firmen sin leerlos", "Los documentos los firma quien tiene esa responsabilidad."),
        ("abc", "{F} ¿Qué es lo primero que debe hacer un estudiante que ve la lista con tres elementos faltantes?", "Contarlo a un adulto responsable, como su profesor o profesora de especialidad", "Entrar al agua a revisar por su cuenta", "Guardar silencio para no meterse en problemas", "Un estudiante no autoriza tareas de riesgo; informa a un adulto responsable."),
    ],
    ctx=("abc", "Un jefe de un centro de ejemplo te dice: «marca todo como cumplido, que el buzo ya está en el agua». ¿Qué haces?", "No marcar nada que no esté cumplido y avisar a un adulto responsable, como tu profesor o profesora de especialidad", "Marcar solo lo que faltaba", "Marcar todo y avisar después", "Falsificar una lista de verificación deja la tarea sin protección."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula el cumplimiento?", "Cumplidos × 100 ÷ total", "El cumplimiento compara lo listo con el total."),
        ("¿Se autoriza una tarea de alto riesgo con elementos faltantes?", "No, se autoriza solo con todo cumplido", "La regla exige cumplimiento total en tareas de alto riesgo."),
        ("¿Qué se hace con un documento que falta?", "Se elabora de verdad con quien corresponde y se informa", "No se marca algo que no existe."),
    ],
    op=("Ficha de ejemplo: lista de verificación de 8 elementos de otra tarea subacuática; 6 están cumplidos; faltan el plan de emergencia y el análisis de riesgos. Escribe (a) el porcentaje de cumplimiento, (b) si se autoriza la tarea y por qué, (c) qué haces con los elementos que faltan, (d) a quién informarías.",
        "(a) 6 × 100 ÷ 8 = 75 %. (b) No se autoriza, porque una tarea de alto riesgo exige todos los elementos cumplidos. (c) Se elaboran de verdad con quien corresponde y no se marcan como cumplidos antes. (d) Al supervisor y al prevencionista; un estudiante lo cuenta a un adulto responsable.",
        ["calcula el porcentaje", "decide con la regla", "no marca lo que falta", "nombra a quién informar"],
        ["hoja con las cuatro respuestas"],
        ["autorizar con un cumplimiento incompleto", "marcar como cumplido lo que no existe", "no informar a nadie"],
        "Pregunta: «¿qué dice la regla sobre los elementos de una tarea de alto riesgo?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una lista de verificación de seis elementos, marca dos como faltantes y calcula el porcentaje de cumplimiento.",
    extend="Explica por qué un cumplimiento de 90 % no basta para autorizar una tarea de alto riesgo.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 12 (registro de ejemplo, inventado). Centro Demo, registro de mortalidad extraída del periodo (peces muertos retirados de cada jaula por personal certificado). Jaula J-1: 10.000 peces al inicio y 200 retirados. "
     "Jaula J-2: 8.000 al inicio y 320 retirados. Jaula J-3: 5.000 al inicio y 250 retirados. Jaula J-4: 4.000 al inicio y 40 retirados. Mortalidad máxima de ejemplo: 3 %. Peso medio de ejemplo de un pez: 2 kg.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular la mortalidad por jaula a partir de un registro de mortalidad extraída, compararla con el máximo e informar anomalías a tiempo.",
    prior=["Sé qué es la mortalidad y cómo se calcula.", "Sé calcular un porcentaje con números enteros.", "Sé qué documentos respaldan una tarea subacuática."],
    explain=[
        "Retirar los peces muertos de una jaula es una tarea subacuática que hacen buzos certificados; este cuaderno solo enseña a leer su registro. La mortalidad de una jaula en un periodo es el porcentaje de peces que murieron: retirados × 100 ÷ peces iniciales. Una desviación es una jaula que supera la mortalidad máxima del plan. La biomasa perdida es los peces muertos multiplicados por su peso medio.",
        "Informar de anomalías de manera oportuna significa avisar apenas se detecta un dato fuera de lo esperado, con el registro como respaldo, y no esperar al fin de mes ni esconderlo. Una alta mortalidad en una sola jaula puede tener causas probables que hay que comprobar, como cambios en el agua o en la sanidad; no se afirma una causa sin datos. La decisión la toman el técnico y la jefatura.",
        f"Las cifras de esta clase son de ejemplo para una planilla.{AV5} {EMER} {AVISO}",
    ],
    vocab=[("mortalidad extraída", "peces muertos retirados de una jaula en un periodo"), ("mortalidad máxima", "máximo de mortalidad aceptable según el plan"), ("biomasa perdida", "peso de los peces muertos"), ("anomalía", "dato fuera de lo esperado"), ("informar oportunamente", "avisar apenas se detecta un dato fuera de lo esperado")],
    worked=[
        ("Calcular mortalidad", "En una jaula de ejemplo con 2.000 peces se retiran 60 muertos. ¿Cuál es la mortalidad?", ["60 × 100 = 6.000.", "6.000 ÷ 2.000 = 3."], "3 %"),
        ("Biomasa perdida", "Se retiran 50 peces muertos de 4 kg cada uno. ¿Cuántos kilos de biomasa se perdieron?", ["Se multiplican los peces por su peso.", "50 × 4 = 200."], "200 kg"),
    ],
    mistakes=[("Calcular la mortalidad dividiendo entre los peces que quedan vivos.", "La mortalidad se calcula sobre los peces iniciales.", "Divide los retirados entre los peces iniciales."),
              ("Esperar al fin de mes para avisar de una mortalidad alta.", "Un aviso tardío impide actuar a tiempo.", "Se informa apenas se detecta el dato, con el registro como respaldo.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es la mortalidad extraída de una jaula?", "Los peces muertos retirados de la jaula en un periodo", "El número de peces que se cosecharon", "El peso del alimento que no se consumió", "La mortalidad extraída son los muertos retirados."),
        ("abc", "En Acuicultura: ¿qué significa informar oportunamente una anomalía?", "Avisar apenas se detecta el dato, con el registro como respaldo", "Esperar a fin de mes para avisar todas juntas", "Corregir el dato antes de avisar", "Oportuno es avisar a tiempo y con evidencia."),
        ("abc", "En Acuicultura: ¿qué es la biomasa perdida por mortalidad?", "El peso de los peces muertos", "El peso del alimento entregado", "El número de jaulas del centro", "La biomasa perdida es el peso de los muertos."),
        ("=", "{F} ¿Cuál es la mortalidad de la jaula J-1, en %?", "200*100//10000", "Se multiplican los retirados por 100 y se dividen entre los peces iniciales.", " %"),
        ("=", "{F} ¿Cuál es la mortalidad de la jaula J-2, en %?", "320*100//8000", "Se multiplican los retirados por 100 y se dividen entre los peces iniciales.", " %"),
        ("=", "{F} ¿Cuál es la mortalidad de la jaula J-3, en %?", "250*100//5000", "Se multiplican los retirados por 100 y se dividen entre los peces iniciales.", " %"),
        ("abc", "{F} ¿Qué jaulas superan la mortalidad máxima de ejemplo?", "J-2 y J-3", "Solo J-2", "J-1 y J-4", "J-2 tiene 4 % y J-3 tiene 5 %, ambas sobre 3 %; J-1 tiene 2 % y J-4 tiene 1 %."),
        ("=", "{F} ¿Cuántos peces se retiraron en total entre las cuatro jaulas?", "200+320+250+40", "Se suman los peces retirados de las cuatro jaulas.", " peces"),
        ("=", "{F} ¿Cuál es la mortalidad del conjunto de las cuatro jaulas, en %?", "(200+320+250+40)*100//(10000+8000+5000+4000)", "Se divide el total de retirados entre el total de peces iniciales y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos kg de biomasa se perdieron en la jaula J-3?", "250*2", "Se multiplican los peces retirados por el peso medio.", " kg"),
        ("abc", "{F} La jaula J-3 superó el máximo. ¿Qué corresponde hacer?", "Informarlo apenas se detecta, con el registro como respaldo", "Esperar al fin de mes para ver si baja", "Cambiar el dato a 3 % para que cumpla", "Una anomalía se informa a tiempo y no se oculta."),
        ("abc", "{F} Alguien afirma que la mortalidad de J-3 se debe al cambio de turno. ¿Qué conclusión es adecuada?", "Es una causa probable que hay que comprobar con más datos", "Queda demostrado porque coincidió con el cambio de turno", "No puede tener ninguna relación con el turno", "Una causa se plantea como probable y se comprueba con datos."),
        ("abc", "{F} Un estudiante propone ir a retirar los peces muertos de J-3 «para ayudar». ¿Qué respondes?", "Que no, porque es una tarea subacuática que hacen buzos certificados con supervisor", "Que sí, si lleva chaleco", "Que sí, si el agua está calma", "Esa tarea de alto riesgo la hace personal certificado, no estudiantes."),
    ],
    ctx=("abc", "Una compañera quiere borrar de la planilla la jaula con mortalidad más alta para que el informe de la semana «se vea mejor». ¿Qué respondes?", "Que no, porque un registro no se altera, y que lo informarás a un adulto responsable", "Que sí, si lo corrige después", "Que sí, solo por esta semana", "Borrar un dato oculta la anomalía e impide actuar a tiempo."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula la mortalidad de una jaula?", "Retirados × 100 ÷ peces iniciales", "La mortalidad se calcula sobre los peces iniciales."),
        ("¿Qué es informar oportunamente?", "Avisar apenas se detecta el dato, con el registro", "Un aviso tardío impide actuar a tiempo."),
        ("¿Quién retira los peces muertos bajo el agua?", "Personal certificado, con supervisor", "Es una tarea de alto riesgo."),
    ],
    op=("Ficha de ejemplo: jaula J-9 de «especie B»: 6.000 peces iniciales y 300 retirados; jaula J-10: 2.000 peces iniciales y 120 retirados. Mortalidad máxima de ejemplo: 5 %. Escribe (a) la mortalidad de cada jaula, (b) cuál supera el máximo, (c) cómo informarías la anomalía, (d) quién retira los peces muertos bajo el agua.",
        "(a) J-9: 300 × 100 ÷ 6.000 = 5 %; J-10: 120 × 100 ÷ 2.000 = 6 %. (b) J-10, porque 6 es mayor que 5; J-9 queda justo en el máximo. (c) Apenas se detecta, con el registro de mortalidad como respaldo, al técnico, sin cambiar el dato. (d) Personal certificado con supervisor de buceo.",
        ["calcula las mortalidades", "identifica la jaula sobre el máximo", "describe cómo informar", "nombra quién hace la tarea"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre los peces vivos", "esperar al fin de mes", "sugerir que un estudiante retire los peces"],
        "Pregunta: «¿entre qué cantidad divides los retirados?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos jaulas con peces iniciales y retirados, y calcula la mortalidad de cada una.",
    extend="Explica por qué avisar a tiempo de una mortalidad alta es mejor que esperar al informe mensual.",
)

# ============================================================ OAE-05, clase 5
F = ("Ficha 13 (caso de ejemplo, inventado). Centro Demo necesita revisar el estado de la red de una jaula y compara dos alternativas. Alternativa A: tarea subacuática con buzo certificado, supervisor y encargado de superficie: 3 personas a $120.000 cada una por jornada, más $180.000 de embarcación. "
     "Alternativa B: inspección con una cámara operada desde la superficie: $250.000 de arriendo de la cámara más $100.000 de una persona que la opera. La cámara solo permite mirar; no repara. Los costos son de ejemplo.")
build(
    O5, 5, F,
    use="Aprenderé a comparar dos alternativas para una tarea con costo, riesgo y alcance, y a verificar la calidad de los registros antes de decidir.",
    prior=["Sé qué es la sustitución en la jerarquía de controles.", "Sé multiplicar, sumar y restar números enteros.", "Sé qué es la bitácora de buceo."],
    explain=[
        "Comparar alternativas es poner las opciones lado a lado con los mismos criterios: costo, riesgo y alcance. El alcance es lo que la alternativa permite hacer; por ejemplo, una cámara permite observar, pero no reparar. El costo total es la suma de todos los gastos de una opción. En cuanto al riesgo, la jerarquía de controles prefiere la alternativa que reduce el peligro desde el origen, es decir, la que sustituye la tarea más peligrosa por una menos peligrosa cuando eso es posible.",
        "Verificar la calidad es comprobar que los datos de la comparación están completos, con fecha y responsable, y que las cifras cuadran. Una alternativa más barata no siempre sirve: si se necesita reparar, la cámara no alcanza. La decisión final la toma la jefatura con el supervisor y el prevencionista; el estudiante entrega la comparación escrita.",
        f"Esta clase trabaja solo con papeles y números de ejemplo.{AV5} {EMER} {AVISO}",
    ],
    vocab=[("alternativa", "una de las opciones entre las que hay que elegir"), ("alcance", "lo que una alternativa permite hacer"), ("costo total", "suma de todos los gastos de una opción"), ("criterio", "aspecto con que se comparan las opciones"), ("sustituir", "reemplazar una tarea peligrosa por una menos peligrosa")],
    worked=[
        ("Costo de una alternativa", "Una alternativa de ejemplo usa 2 personas a $50.000 cada una y $30.000 de equipo. ¿Cuál es su costo total?", ["Personas: 2 × 50.000 = 100.000.", "Se suma el equipo: 100.000 + 30.000 = 130.000."], "$130.000"),
        ("Elegir con alcance", "La alternativa X cuesta menos pero no permite reparar, y se necesita reparar. ¿Alcanza X?", ["Se compara lo que se necesita con el alcance de X.", "X no permite reparar."], "No alcanza, aunque cueste menos"),
    ],
    mistakes=[("Elegir la alternativa más barata sin revisar su alcance.", "Si no permite hacer lo que se necesita, el ahorro no sirve.", "Compara costo, riesgo y alcance."),
              ("Dar por seguras las cifras de un registro sin verificarlas.", "Un registro incompleto o descuadrado puede llevar a una mala decisión.", "Se verifica que esté completo, con fecha y responsable, y que cuadre.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es el alcance de una alternativa?", "Lo que la alternativa permite hacer", "El lugar donde se compra", "El tiempo que dura el contrato", "El alcance dice qué se puede lograr con la alternativa."),
        ("abc", "En Acuicultura: ¿qué significa sustituir una tarea peligrosa?", "Reemplazarla por una menos peligrosa cuando es posible", "Hacerla más rápido para exponerse menos", "Entregar más equipo de protección", "Sustituir es cambiar la tarea; el equipo de protección actúa después."),
        ("abc", "En Acuicultura: ¿qué significa verificar la calidad de los datos de una comparación?", "Comprobar que están completos, tienen fecha y responsable y cuadran", "Copiarlos a mano con otra letra", "Guardarlos sin leerlos", "Verificar es comprobar; copiar o guardar no comprueba nada."),
        ("=", "{F} ¿Cuál es el costo total de la alternativa A?", "3*120000+180000", "Se multiplican las tres personas por su costo y se suma la embarcación.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la alternativa B?", "250000+100000", "Se suman el arriendo de la cámara y la persona que la opera.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta A que B?", "(3*120000+180000)-(250000+100000)", "Se resta el costo de B al de A.", " pesos"),
        ("abc", "{F} Solo se necesita ver el estado de la red. ¿Qué alternativa conviene según costo, riesgo y alcance?", "La B, porque alcanza para mirar, cuesta menos y evita exponer a una persona bajo el agua", "La A, porque siempre es mejor enviar a una persona", "Ninguna, porque no se puede mirar una red", "Si basta con mirar, la B tiene menor costo y menor riesgo."),
        ("abc", "{F} Se descubre que hay que reparar la red. ¿Qué alternativa alcanza?", "La A, porque la tarea de reparación requiere personal certificado", "La B, porque la cámara también repara", "Ninguna, porque nadie repara redes", "La cámara solo permite mirar; reparar exige una tarea subacuática autorizada."),
        ("=", "{F} Si se hicieran 12 inspecciones al año con la alternativa A, ¿cuántos pesos costarían?", "12*(3*120000+180000)", "Se multiplica el costo de una jornada por 12.", " pesos"),
        ("=", "{F} Con 12 inspecciones al año, ¿cuántos pesos se ahorrarían usando B en vez de A?", "12*((3*120000+180000)-(250000+100000))", "Se multiplica por 12 la diferencia de costo entre A y B.", " pesos"),
        ("abc", "{F} El registro del costo de A dice $540.000 y la factura de ejemplo dice $560.000. ¿Qué corresponde?", "Informar la diferencia con ambos documentos, sin cambiar cifras", "Cambiar el registro a $560.000 sin avisar", "Dejarlo así sin comentarlo", "Una diferencia se informa con evidencia y no se corrige a escondidas."),
        ("abc", "{F} ¿Quién toma la decisión final de qué alternativa usar?", "La jefatura con el supervisor y el prevencionista", "El estudiante que hizo la comparación", "El proveedor de la cámara", "La decisión es de quienes tienen la responsabilidad; el estudiante aporta la comparación."),
        ("abc", "{F} Una persona propone quitar al supervisor de la alternativa A «para ahorrar». ¿Qué respondes?", "Que no, porque el supervisor es obligatorio en una tarea subacuática", "Que sí, porque baja el costo", "Que sí, si el buzo tiene experiencia", "Quitar al supervisor deja la tarea sin dirección ni vigilancia de seguridad."),
    ],
    ctx=("abc", "Un conocido te ofrece «hacerlo más barato» bajando a revisar la red de su jaula sin certificación ni supervisor. ¿Qué respondes?", "Que no, porque esa tarea exige personal certificado y supervisor, y que lo consultarás con un adulto responsable", "Que sí, porque ahorra dinero", "Que sí, si hace buen tiempo", "El ahorro no justifica una tarea de alto riesgo sin certificación ni supervisor."),
    sc=[
        ("En Acuicultura: ¿qué es el alcance de una alternativa?", "Lo que permite hacer", "El alcance dice qué se puede lograr con la alternativa."),
        ("¿Qué criterios se comparan entre alternativas?", "Costo, riesgo y alcance", "Comparar con los mismos criterios permite decidir."),
        ("¿Quién decide la alternativa final?", "La jefatura con el supervisor y el prevencionista", "El estudiante entrega la comparación escrita."),
    ],
    op=("Ficha de ejemplo: alternativa A, tarea con buzo: 3 personas a $100.000 y $150.000 de embarcación. Alternativa B, cámara desde la superficie: $200.000 en total; solo permite mirar. Escribe (a) el costo total de A y de B, (b) la diferencia, (c) cuál conviene si solo hay que mirar y por qué, (d) cuál alcanza si hay que reparar y quién decide.",
        "(a) A: 3 × 100.000 + 150.000 = 450.000 pesos; B: 200.000 pesos. (b) 450.000 − 200.000 = 250.000 pesos. (c) B, porque basta para mirar, cuesta menos y evita exponer a una persona bajo el agua. (d) A, porque reparar exige una tarea subacuática autorizada; decide la jefatura con el supervisor y el prevencionista.",
        ["calcula los costos", "calcula la diferencia", "elige según el alcance y el riesgo", "indica quién decide"],
        ["hoja con las cuatro respuestas"],
        ["comparar solo el costo", "olvidar el alcance", "decidir sin la jefatura"],
        "Pregunta: «¿qué puede hacer la cámara y qué no?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos alternativas para una tarea con costos y alcance distintos, y compara su costo total.",
    extend="Explica con un ejemplo cuándo una alternativa más barata no es la mejor.",
)
