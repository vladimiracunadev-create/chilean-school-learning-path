"""Operaciones Portuarias TP 3.º y 4.º medio: OAE-02 (estiba y desestiba como planilla). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_opor_common import AVISO, EMER, build

O2 = "TP-OPOR-3y4-OAE-02"

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Nave Demo 2», ficticia, tiene 4 bodegas y está atracada en Terminal Demo. La desestiba usa 3 cuadrillas de 8 personas, una por cada bodega en operación, en turnos de 8 horas. "
     "Rendimiento de ejemplo: 30 bultos por hora por cuadrilla. La nave trae 1.440 bultos. Peligros anotados: cargas suspendidas sobre las bodegas, escotillas abiertas (aberturas de la cubierta que dan a la bodega), "
     "piso resbaladizo por la lluvia y el borde del muelle junto al agua.")
build(
    O2, 1, F,
    use="Aprenderé qué son la estiba y la desestiba, qué peligros y riesgos tienen y por qué su ejecución exige personal autorizado y norma vigente.",
    prior=["Sé qué es un cronograma.", "Sé distinguir peligro y riesgo.", "Sé calcular horas con multiplicaciones y divisiones."],
    explain=[
        "La estiba es la ubicación ordenada de la carga a bordo de una nave, siguiendo un plan; la desestiba es sacar la carga de la nave y entregarla en el muelle, también según un plan. El plan de estiba es una planilla que indica qué carga va en cada bodega, cuánto pesa y a qué puerto va. Estiba y desestiba las ejecutan cuadrillas formadas y autorizadas, bajo la dirección de un capataz, que es el encargado de la cuadrilla.",
        "Estas faenas tienen peligros propios: cargas suspendidas, aberturas en la cubierta, pisos resbaladizos y la cercanía del agua. De ellos nacen riesgos como el aplastamiento, la caída a la bodega o al agua y el atrapamiento. Se previene con la jerarquía de controles: primero eliminar o sustituir el peligro, luego barreras físicas (ingeniería), luego permisos y capacitación (administrativos) y al final el EPP. Los permisos y las reglas de la faena los fija la norma vigente de la autoridad marítima y portuaria.",
        f"Este cuaderno solo enseña a leer planillas y a calcular en papel; no enseña cómo se mueve ni se acomoda una carga. {EMER} {AVISO}",
    ],
    vocab=[("estiba", "ubicación ordenada de la carga a bordo de una nave según un plan"), ("desestiba", "salida de la carga de la nave y entrega en el muelle según un plan"), ("plan de estiba", "planilla que indica qué carga va en cada bodega, su peso y su destino"), ("cuadrilla", "grupo de trabajadores de una faena"), ("capataz", "encargado de una cuadrilla"), ("escotilla", "abertura de la cubierta que da a la bodega de la nave"), ("aplastamiento", "daño por quedar atrapado bajo o contra una carga")],
    worked=[
        ("Clasificar la operación", "Una nave de ejemplo se prepara para zarpar y su carga se ubica en las bodegas según un plan. ¿La ubicación de esa carga a bordo es estiba o desestiba?", ["La carga se coloca a bordo de la nave.", "Colocar carga a bordo según un plan es estiba."], "Estiba"),
        ("Peligro y riesgo", "Un cable suelto cruza el piso de un pasillo de ejemplo. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el cable suelto, porque puede causar daño.", "El riesgo es que una persona tropiece con él y caiga."], "Peligro: el cable suelto; riesgo: que alguien tropiece y caiga"),
    ],
    mistakes=[("Confundir estiba con guardar la carga en la bodega del puerto.", "La estiba se hace a bordo de la nave; guardar en tierra es almacenaje.", "Pregunta siempre dónde se ubica la carga: a bordo o en tierra."),
              ("Creer que entender la planilla habilita para entrar a las bodegas de una nave.", "Las faenas a bordo exigen formación, autorización y norma vigente.", "Aprende aquí el concepto y deja la faena a personal autorizado.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es la estiba?", "La ubicación ordenada de la carga a bordo de una nave según un plan", "El traslado de la carga desde el patio a la bodega del puerto", "El conteo de bultos en la zona de control", "La estiba ocurre a bordo; el traslado en tierra y el conteo son otras actividades."),
        ("abc", "En Operaciones Portuarias: ¿qué es la desestiba?", "Sacar la carga de la nave y entregarla en el muelle según un plan", "Registrar en el manifiesto la carga que llega", "Reordenar la carga dentro de la bodega del puerto", "La desestiba es la operación inversa de la estiba, a bordo de la nave."),
        ("abc", "En Operaciones Portuarias: ¿qué es un plan de estiba?", "Una planilla que indica qué carga va en cada bodega, cuánto pesa y a qué puerto va", "Un permiso de la autoridad para que la nave zarpe", "La lista de personas que integran una cuadrilla", "El plan de estiba es la planilla de ubicación de la carga; los permisos y las listas son otros documentos."),
        ("abc", "{F} ¿Qué riesgo para las personas se asocia a las escotillas abiertas?", "Que una persona caiga por la abertura hacia la bodega", "Que la cuadrilla tenga más personas de las necesarias", "Que la lluvia moje los documentos de la nave", "Una abertura en la cubierta expone a caer; los otros problemas no son daños por la escotilla."),
        ("abc", "{F} ¿Con cuál peligro de la ficha se relaciona principalmente el riesgo de aplastamiento?", "Las cargas suspendidas sobre las bodegas", "El piso resbaladizo por la lluvia", "El borde del muelle junto al agua", "Una carga suspendida que se suelta puede aplastar; el piso mojado se relaciona con caídas y el borde con caer al agua."),
        ("abc", "{F} Una baranda fija que rodea la abertura de una escotilla, colocada por personal autorizado, es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una norma escrita", "De EPP, porque protege a la persona", "Una baranda es una barrera física y no depende de que cada persona la recuerde."),
        ("=", "{F} ¿Cuántas personas trabajan en un turno, sumando las cuadrillas en operación?", "3*8", "Se multiplican las cuadrillas en operación por las personas de cada una.", " personas"),
        ("=", "{F} Si la operación es continua las 24 horas, ¿cuántas personas en total trabajan a lo largo del día, sumando las de todos los turnos?", "24//8*3*8", "Se calculan los turnos del día y se multiplican por las personas de cada turno.", " personas"),
        ("=", "Una desestiba de ejemplo tiene 4 bodegas; cada una requiere 5 horas de trabajo de una cuadrilla. Se dispone de 2 cuadrillas que trabajan en paralelo, cada una en una bodega a la vez. ¿Cuántas horas demora desestibar las 4 bodegas?", "4//2*5", "Cada cuadrilla hace la mitad de las bodegas, una tras otra, de 5 horas cada una.", " horas"),
        ("abc", "Durante una visita de ejemplo, una persona queda atrapada por una carga que cae junto al muelle. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a ayudar a levantar la carga", "Mover a la persona para sacarla de ahí lo antes posible", "Intervenir o mover a la persona sin formación puede empeorar el daño; se avisa a quienes pueden actuar."),
        ("abc", "En Operaciones Portuarias: ¿por qué un permiso de ingreso a una zona de faena es un control administrativo y no de ingeniería?", "Porque es una regla y un documento, y no cambia físicamente el lugar", "Porque lo firma una persona de la oficina", "Porque protege solo a quien lo recibe, como el EPP", "Un permiso ordena una conducta; la ingeniería cambia el lugar con barreras físicas."),
        ("=", "{F} Con las 3 cuadrillas trabajando a la vez y el rendimiento de la ficha, ¿cuántos turnos de 8 horas se necesitan para desestibar los 1.440 bultos?", "1440//(30*3)//8", "Se calcula el rendimiento conjunto, las horas necesarias y se dividen entre las horas de cada turno.", " turnos"),
        ("abc", "{F} Un jefe propone que, para terminar en un solo turno, las cuadrillas trabajen sin relevos ni pausas. ¿Qué corresponde?", "Mantener los turnos y relevos previstos y reprogramar: la seguridad no se recorta por el plazo", "Aceptar, si la carga es urgente", "Aceptar, si todas las personas usan EPP", "Las pausas y los relevos son controles de seguridad; recortarlos aumenta el riesgo."),
    ],
    ctx=("abc", "Un familiar te propone acompañarlo a una nave atracada para «ayudar a acomodar unos bultos» porque «solo es cargar cosas». ¿Qué respondes?", "Que no, porque las faenas a bordo exigen instructor autorizado, norma vigente y elementos de protección, y que lo consultarás con un adulto responsable", "Que sí, si te presta un casco", "Que sí, pero solo en la bodega más cercana a la salida", "Un casco o la cercanía a la salida no reemplazan la formación y la autorización."),
    sc=[
        ("En Operaciones Portuarias: ¿qué es la desestiba?", "Sacar la carga de la nave y entregarla en el muelle según un plan", "La desestiba es la salida de la carga de la nave."),
        ("¿Qué es el aplastamiento?", "Daño por quedar atrapado bajo o contra una carga", "Es un riesgo propio de las cargas pesadas o suspendidas."),
        ("¿Qué indica un plan de estiba?", "Qué carga va en cada bodega, cuánto pesa y a qué puerto va", "Es la planilla que ordena la ubicación de la carga."),
    ],
    op=("Una tarea de ejemplo anota: desestibar una bodega de una nave ficticia bajo lluvia, con piso resbaladizo y cargas suspendidas sobre la bodega. Escribe (a) un peligro de la tarea y su riesgo asociado, (b) un control administrativo, (c) un control de ingeniería, (d) qué hacer si una persona cae al agua junto al muelle.",
        "(a) Peligro: las cargas suspendidas sobre la bodega; riesgo: que una caiga y aplaste a una persona. (b) Un permiso de faena y la prohibición de permanecer bajo cargas suspendidas, informada por letreros y charlas. (c) Una cubierta o barrera fija que impida el paso bajo la zona de cargas. (d) No acercarse a la zona de riesgo ni entrar al agua, avisar a un adulto responsable y a emergencias. La tarea la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "indica no intervenir y avisar"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer el EPP como único control", "sugerir entrar al agua a ayudar"],
        "Pregunta: «¿qué hace una persona sin formación ante una caída al agua?». Si no responde, pídele que relea el último párrafo de la explicación."),
    reinforce="Escribe con tus palabras la diferencia entre estiba y desestiba y da un peligro de cada una.",
    extend="Explica con un ejemplo por qué una charla de seguridad no reemplaza una barrera física.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (planilla descrita por escrito, de ejemplo, inventada). Plan de estiba de la «Nave Demo 2». Bodega 1: 60 cajones de carga general, 1.200 kg cada uno, puerto de descarga B. "
     "Bodega 2: 42 cajones de carga general, 900 kg cada uno, puerto de descarga C. Marcas de manipulación en los cajones de la bodega 2: «frágil» y «no apilar más de 3 en altura» (valor de ejemplo). "
     "Orden de descarga: primero el puerto B y después el puerto C.")
build(
    O2, 2, F,
    use="Aprenderé a leer un plan de estiba, la simbología de manipulación de los bultos, el orden de descarga y qué son los tratados internacionales del transporte marítimo.",
    prior=["Sé qué son la estiba y la desestiba.", "Sé multiplicar y dividir números enteros.", "Sé que 1 tonelada son 1.000 kilogramos."],
    explain=[
        "Un plan de estiba se lee como una planilla: cada fila indica la bodega, el tipo de carga, la cantidad de bultos, el peso, el puerto de descarga y las marcas. El orden de descarga ordena los puertos en que la nave irá dejando carga; el plan procura que la carga que se baja primero quede accesible, para no mover carga ajena sin necesidad. El peso se calcula multiplicando las unidades por el peso de cada una, y 1 tonelada equivale a 1.000 kilogramos.",
        "Los bultos traen marcas de manipulación, símbolos que avisan cómo tratarlos: «frágil» indica que se daña con facilidad, «este lado arriba» indica la posición en que debe mantenerse, «mantener seco» pide protegerlo del agua, y «no apilar más de» limita cuántos bultos pueden ir uno sobre otro. Las marcas comunican cómo evitar daños a la carga y a las personas, y el plan debe respetarlas.",
        f"Los tratados internacionales son acuerdos entre países que fijan reglas comunes, por ejemplo de seguridad en el transporte marítimo; su detalle se consulta en la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("marca de manipulación", "símbolo que avisa cómo tratar un bulto"), ("orden de descarga", "orden de los puertos en que la nave deja su carga"), ("tonelada", "unidad de peso que equivale a 1.000 kilogramos"), ("tratado internacional", "acuerdo entre países que fija reglas comunes"), ("capataz", "encargado de una cuadrilla"), ("tarjador", "persona que cuenta y registra los bultos")],
    worked=[
        ("Peso de una bodega", "Una bodega de ejemplo lleva 50 cajones de 600 kg cada uno. ¿Cuántas toneladas pesa su carga?", ["50 por 600 son 30.000 kg.", "30.000 kg son 30 toneladas."], "30 toneladas"),
        ("Leer una marca", "Un bulto de ejemplo trae la marca «mantener seco». ¿Qué comunica?", ["La marca indica una condición de manipulación.", "«Mantener seco» pide protegerlo del agua y de la humedad."], "Que debe protegerse del agua y de la humedad"),
    ],
    mistakes=[("Pensar que las marcas de manipulación son una sugerencia que se puede ignorar.", "Comunican cómo evitar daños a la carga y riesgos para las personas.", "Revisa las marcas de cada fila de la planilla antes de decidir la ubicación."),
              ("Olvidar convertir kilogramos a toneladas al sumar pesos.", "Los totales se mezclan y el resultado no tiene sentido.", "Expresa todos los pesos en la misma unidad antes de sumar.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué indica la marca de manipulación «frágil» en un bulto?", "Que se daña con facilidad y exige un trato cuidadoso", "Que el bulto pesa más que los demás", "Que el bulto debe ir siempre en la parte alta de la bodega", "«Frágil» habla de la facilidad de daño; el peso y la altura no son su significado."),
        ("abc", "En Operaciones Portuarias: ¿qué indica la marca «este lado arriba»?", "La posición en que debe mantenerse el bulto", "Que el bulto debe quedar sobre los demás", "Que el bulto se descarga primero", "La marca fija la orientación del bulto, no su lugar entre otros ni su orden de descarga."),
        ("abc", "En Operaciones Portuarias: ¿qué es un tratado internacional en el transporte marítimo?", "Un acuerdo entre países que fija reglas comunes, como las de seguridad", "Una norma interna de cada empresa naviera", "Un contrato entre un embarcador y un consignatario", "Un tratado es un acuerdo entre países; las normas internas y los contratos tienen otro alcance."),
        ("abc", "{F} ¿Qué carga debe quedar mejor ubicada en el plan para descargarse primero?", "La de la bodega 1, porque su puerto de descarga es el primero del orden", "La de la bodega 2, porque lleva la marca «frágil»", "Ninguna: el orden de descarga no influye en el plan", "El plan procura que la carga del primer puerto quede accesible."),
        ("abc", "{F} Los cajones de la bodega 2 llevan «no apilar más de 3 en altura». ¿Qué significa para la planilla?", "Que como máximo puede haber 3 cajones uno sobre otro", "Que en toda la bodega solo pueden ir 3 cajones", "Que cada cajón debe pesar menos de 3 toneladas", "La marca limita la altura de apilado, no la cantidad total ni el peso."),
        ("abc", "En Operaciones Portuarias: ¿quién es el capataz?", "El encargado de una cuadrilla", "La persona que representa a la nave ante el puerto", "La persona que recibe la carga en destino", "El capataz dirige una cuadrilla; representar a la nave es del agente y recibir la carga, del consignatario."),
        ("=", "{F} ¿Cuántos kilogramos pesa la carga de ambas bodegas?", "60*1200+42*900", "Se multiplican las unidades de cada bodega por su peso y se suman los resultados.", " kg"),
        ("=", "{F} Si cada columna de la bodega 2 apila 3 cajones, ¿cuántas columnas se forman con todos sus cajones?", "42//3", "Se dividen los cajones de la bodega 2 entre los que apila cada columna.", " columnas"),
        ("=", "Otra planilla de ejemplo lleva 25 cajones de 800 kg cada uno. ¿Cuántas toneladas pesa la carga?", "25*800//1000", "Se multiplican los cajones por su peso y se pasan los kilogramos a toneladas.", " toneladas"),
        ("abc", "{F} Un jefe propone ubicar los cajones frágiles bajo el resto de la carga «para ganar espacio». ¿Qué problema hay?", "Contradice la marca «frágil» y el límite de apilado de la planilla", "Ninguno, porque los cajones frágiles resisten más peso", "Ninguno, porque la marca solo es una sugerencia del embarcador", "Las marcas se respetan; ignorarlas daña la carga y aumenta el riesgo."),
        ("abc", "En Operaciones Portuarias: ¿por qué las marcas de manipulación deben respetarse al preparar un plan de estiba?", "Porque comunican cómo evitar daños a la carga y riesgos para las personas", "Porque reemplazan al conocimiento de embarque", "Porque solo importan si el bulto cambia de país", "Las marcas son parte de la información de seguridad de la carga."),
        ("=", "{F} El plan fija un límite de ejemplo de 120 toneladas para la carga de ambas bodegas. ¿Cuántos kilogramos de margen quedan?", "120*1000-(60*1200+42*900)", "Se pasa el límite a kilogramos y se resta el peso total de ambas bodegas.", " kg"),
        ("abc", "{F} Un cliente pide agregar 15 cajones de 900 kg a la bodega 2, con la misma marca y el mismo destino. Con el límite de 120 toneladas, ¿qué corresponde?", "No aceptarlo tal cual, porque el peso total superaría el límite de ejemplo", "Aceptarlo, porque el límite no se aplica a cajones con la misma marca", "Aceptarlo, porque el margen disponible es mayor que 15 cajones", "Los 15 cajones suman 13.500 kg, más que el margen de 10.200 kg disponible."),
    ],
    ctx=("abc", "Un amigo te muestra una foto de una carga que lleva el símbolo «frágil» y dice: «eso es solo un dibujo, se puede tratar como cualquier otro bulto». ¿Qué respondes?", "Que las marcas indican cómo tratar el bulto y deben respetarse al planificar y manipular la carga", "Que tiene razón, porque los dibujos no tienen valor", "Que solo vale si el bulto va dentro de un contenedor", "Las marcas son información de manipulación y de seguridad que debe cumplirse."),
    sc=[
        ("En Operaciones Portuarias: ¿cuántos kilogramos tiene una tonelada?", "1.000 kilogramos", "Una tonelada equivale a mil kilogramos."),
        ("¿Qué comunica la marca «mantener seco»?", "Que el bulto debe protegerse del agua y de la humedad", "La marca pide evitar el contacto con el agua."),
        ("¿Para qué sirve el orden de descarga en un plan de estiba?", "Para que la carga que se baja primero quede accesible", "Evita mover carga ajena sin necesidad."),
    ],
    op=("Planilla de ejemplo de una nave ficticia. Bodega 3: 30 cajones de 500 kg cada uno, puerto de descarga D. Bodega 4: 20 cajones de 700 kg cada uno, puerto de descarga E, con las marcas «este lado arriba» y «frágil». Orden de descarga: primero D, después E. Escribe (a) el peso de cada bodega en kilogramos, (b) el peso total en toneladas, (c) qué carga debe quedar más accesible y por qué, (d) qué significan las dos marcas de la bodega 4.",
        "(a) Bodega 3: 30 × 500 = 15.000 kg. Bodega 4: 20 × 700 = 14.000 kg. (b) 15.000 + 14.000 = 29.000 kg, que son 29 toneladas. (c) La de la bodega 3, porque su puerto D es el primero del orden de descarga. (d) «Este lado arriba» indica la posición en que debe mantenerse el bulto y «frágil» indica que se daña con facilidad y exige trato cuidadoso.",
        ["calcula el peso de cada bodega", "convierte el total a toneladas", "relaciona accesibilidad con el orden de descarga", "explica las dos marcas"],
        ["hoja con las cuatro respuestas"],
        ["no convertir kilogramos a toneladas", "ignorar el orden de descarga", "confundir «frágil» con «pesado»"],
        "Pregunta: «¿qué puerto se atiende primero?». Si no responde, pídele que relea el orden de descarga de la planilla."),
    reinforce="Inventa una fila de planilla con bodega, cantidad, peso, puerto y una marca de manipulación, y calcula su peso total.",
    extend="Explica con un ejemplo por qué el plan de estiba no puede ignorar el orden de descarga.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (planilla de ejemplo, inventada). La «Nave Demo 2» tiene 4 bodegas; las bodegas 1 y 2 son las delanteras y las 3 y 4 las traseras. Límites de peso de ejemplo: bodega 1, 150 toneladas; bodega 2, 120; bodega 3, 120; bodega 4, 150; "
     "total de la nave, 500 toneladas. Para cuidar el equilibrio, la diferencia de peso entre las delanteras y las traseras no debe pasar de 40 toneladas (valor de ejemplo). "
     "Asignación propuesta en toneladas: bodega 1, 140; bodega 2, 125; bodega 3, 100; bodega 4, 110.")
build(
    O2, 3, F,
    use="Aprenderé a revisar una planilla de estiba: límites por bodega, total, equilibrio entre delanteras y traseras y qué hacer cuando la asignación no cumple.",
    prior=["Sé leer una planilla con pesos.", "Sé sumar y restar números enteros.", "Sé qué son las marcas de manipulación y el orden de descarga."],
    explain=[
        "Al revisar una asignación se comprueban tres cosas. Primero, que cada bodega respete su límite de peso, el máximo que el plan puede asignarle. Segundo, que el peso total no supere el límite de la nave. Tercero, el equilibrio: un reparto muy desparejo entre la parte delantera y la trasera afecta la estabilidad de la nave, y por eso el plan limita la diferencia de peso entre ambas partes. Basta que una de las tres comprobaciones falle para que la planilla no se pueda aceptar.",
        "Cuando una asignación no cumple, se corrige en la planilla moviendo toneladas entre bodegas y se vuelve a comprobar todo; si la carga no cabe, el exceso se deja fuera del plan y se consulta a la jefatura y al cliente. El plan ya aprobado no lo cambia quien ejecuta la faena: lo modifica quien lo preparó o aprobó, dejando registro del cambio.",
        f"Todos los límites de esta clase son de ejemplo; los reales los fijan el fabricante y la norma vigente. Solo hacemos el cálculo de planilla en papel. {EMER} {AVISO}",
    ],
    vocab=[("límite de peso", "máximo de peso que el plan puede asignar a una bodega o a la nave"), ("equilibrio", "reparto parejo del peso entre la parte delantera y la trasera de la nave"), ("asignación", "cantidad de carga que el plan destina a una bodega"), ("delanteras y traseras", "bodegas de la parte de adelante y de la parte de atrás de la nave"), ("exceso", "cantidad que sobrepasa un límite")],
    worked=[
        ("Comparar con el límite", "Una bodega de ejemplo tiene límite de 90 toneladas y el plan le asigna 96. ¿Cumple?", ["La asignación es 96 y el límite es 90.", "96 supera 90 por 6 toneladas."], "No cumple: excede su límite por 6 toneladas"),
        ("Revisar el equilibrio", "En un plan de ejemplo las bodegas delanteras suman 130 toneladas y las traseras 105; la diferencia máxima de ejemplo es 30. ¿Cumple?", ["La diferencia es 130 menos 105, o sea 25.", "25 no supera 30."], "Sí cumple el equilibrio: la diferencia es 25 toneladas"),
    ],
    mistakes=[("Revisar solo el total de la nave y olvidar los límites de cada bodega.", "Una bodega puede pasar su límite aunque el total esté bien.", "Revisa en orden: cada bodega, el total y el equilibrio."),
              ("Resolver el exceso asignándolo igual y anotando que sobra.", "El plan no puede aprobarse con asignaciones que superan un límite.", "Mueve toneladas entre bodegas o deja el exceso fuera y consulta.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es el límite de peso de una bodega en el plan de estiba?", "El peso máximo de carga que el plan puede asignar a esa bodega", "El peso mínimo que debe llevar la bodega para que la nave zarpe", "El peso de la bodega vacía", "El límite es un máximo asignable, no un mínimo ni el peso de la estructura."),
        ("abc", "En Operaciones Portuarias: ¿por qué el plan cuida el equilibrio entre las bodegas delanteras y las traseras?", "Porque un reparto muy desparejo del peso afecta la estabilidad de la nave", "Porque así la carga se descarga más rápido", "Porque el equilibrio solo importa con carga refrigerada", "El equilibrio busca la estabilidad; no acelera la descarga ni depende del tipo de carga."),
        ("abc", "En Operaciones Portuarias: ¿qué es el peso total asignado de un plan?", "La suma de los pesos que el plan destina a todas las bodegas", "El peso de la bodega más cargada", "El promedio de peso por bodega", "El total se obtiene sumando todas las asignaciones."),
        ("abc", "{F} ¿Qué bodega supera su límite de peso en la asignación propuesta?", "La bodega 2", "La bodega 1", "La bodega 4", "La bodega 2 tiene 125 toneladas para un límite de 120; las otras quedan bajo su límite."),
        ("=", "{F} ¿Cuántas toneladas suma la asignación propuesta en total?", "140+125+100+110", "Se suman las toneladas asignadas a las cuatro bodegas.", " toneladas"),
        ("abc", "{F} ¿Cumple la asignación propuesta el límite total de la nave?", "Sí, porque el total no supera las 500 toneladas", "No, porque una bodega superó su límite y eso hace superar el total", "No, porque el total debe ser exactamente 500 toneladas", "El total es un límite aparte: 475 no supera 500, aunque otra comprobación falle."),
        ("=", "{F} ¿Cuántas toneladas se asignan a las bodegas delanteras?", "140+125", "Se suman las asignaciones de las bodegas 1 y 2.", " toneladas"),
        ("=", "{F} ¿Cuántas toneladas de diferencia hay entre las bodegas delanteras y las traseras en la asignación propuesta?", "(140+125)-(100+110)", "Se resta el peso de las traseras al de las delanteras.", " toneladas"),
        ("abc", "{F} ¿Cuál reasignación mantiene el total de 475 toneladas y cumple todos los límites y el equilibrio?", "Bodega 1: 140; bodega 2: 115; bodega 3: 110; bodega 4: 110", "Bodega 1: 140; bodega 2: 120; bodega 3: 105; bodega 4: 110", "Bodega 1: 130; bodega 2: 115; bodega 3: 125; bodega 4: 105", "La primera cumple los límites y deja una diferencia de 35; la segunda pasa de 40 toneladas y la tercera supera el límite de la bodega 3."),
        ("abc", "{F} Un compañero dice: «como el total de 475 toneladas no supera las 500, la planilla está bien». ¿Qué respuesta es correcta?", "Es falso: cada bodega debe cumplir su límite y el equilibrio, no solo el total", "Es cierto: el total es lo único que importa", "Es cierto, si el cliente firma la planilla", "Una bodega excede su límite y el equilibrio falla; el total no basta."),
        ("abc", "En Operaciones Portuarias: ¿quién puede modificar un plan de estiba ya aprobado?", "Quien lo preparó o lo aprobó, dejando registro del cambio", "Cualquier integrante de la cuadrilla, si ve que la carga no cabe", "El consignatario en el puerto de destino", "Los cambios al plan los hace su responsable y quedan registrados."),
        ("=", "{F} Se mueven 15 toneladas desde la bodega 1 hacia la bodega 4, sin otros cambios. ¿Cuántas toneladas de diferencia quedan entre las delanteras y las traseras?", "(140-15+125)-(100+110+15)", "Se recalculan las delanteras y las traseras con el movimiento y se restan.", " toneladas"),
        ("abc", "{F} Un cliente pide agregar 60 toneladas más al plan. ¿Qué corresponde?", "Dejar fuera el exceso del plan y consultar a la jefatura y al cliente", "Repartirlas igual y anotar el exceso en la planilla", "Subir el límite total de la nave en la planilla", "Con 60 más el total sería 535, sobre las 500 toneladas; no se altera un límite para que cuadre."),
    ],
    ctx=("abc", "En una práctica de ejemplo, una persona te dice: «la planilla pasa un poco el límite de una bodega, pero anota que cumple; después se acomoda en el muelle». ¿Qué respondes?", "Que no se puede anotar que cumple: hay que corregir la asignación o informar el exceso a quien corresponde", "Que lo anotas, porque la diferencia es pequeña", "Que lo anotas y después lo corriges en el muelle", "Una planilla falsa oculta un exceso real y puede causar un accidente."),
    sc=[
        ("En Operaciones Portuarias: ¿qué tres cosas se revisan en una asignación de estiba?", "El límite de cada bodega, el total y el equilibrio", "Las tres comprobaciones deben cumplirse a la vez."),
        ("¿Qué se hace con el exceso de carga que no cabe en el plan?", "Se deja fuera del plan y se consulta a la jefatura y al cliente", "No se altera un límite para que la carga quepa."),
        ("¿Qué es el equilibrio en una nave?", "Un reparto parejo del peso entre delanteras y traseras", "Cuida la estabilidad de la nave."),
    ],
    op=("Nave ficticia con 4 bodegas; las bodegas 1 y 2 son las delanteras y las 3 y 4 las traseras. Límites de ejemplo: bodegas 1 y 4, 100 toneladas cada una; bodegas 2 y 3, 80 cada una; total de la nave, 340. Diferencia máxima entre delanteras y traseras: 20 toneladas (valor de ejemplo). Asignación propuesta: bodega 1, 90; bodega 2, 85; bodega 3, 70; bodega 4, 60. Escribe (a) el total asignado, (b) qué bodega excede su límite, (c) la diferencia entre delanteras y traseras, (d) si la planilla se puede aceptar y por qué.",
        "(a) 90 + 85 + 70 + 60 = 305 toneladas. (b) La bodega 2, con 85 toneladas sobre un límite de 80. (c) Delanteras: 90 + 85 = 175; traseras: 70 + 60 = 130; diferencia: 45 toneladas. (d) No se puede aceptar: aunque el total (305) no supera 340, la bodega 2 excede su límite y la diferencia de 45 supera las 20 permitidas.",
        ["calcula el total", "identifica la bodega que excede", "calcula la diferencia entre delanteras y traseras", "concluye que no se acepta y justifica con las tres comprobaciones"],
        ["hoja con las cuatro respuestas"],
        ["revisar solo el total", "sumar mal las delanteras o las traseras", "aceptar la planilla con un exceso"],
        "Pregunta: «¿se cumplen las tres comprobaciones?». Si no responde, pídele que las revise una por una."),
    reinforce="Inventa una asignación para tres bodegas con sus límites y revisa si cumple cada límite y el total.",
    extend="Explica con un ejemplo por qué una planilla puede cumplir el límite total y aun así no ser aceptable.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (caso de ejemplo, inventado). Una bodega de la «Nave Demo 2» tiene una capacidad de volumen de 600 metros cúbicos (m³) y un límite de peso de 200 toneladas (valores de ejemplo). "
     "El factor de estiba de cada lote es el volumen que ocupa una tonelada, incluidos los espacios entre bultos. Lote X: 90 toneladas, factor 2 m³ por tonelada. Lote Y: 50 toneladas, factor 3. "
     "Lote Z: 40 toneladas, factor 4. Orden de descarga: primero el lote Z, después el lote X y al final el lote Y.")
build(
    O2, 4, F,
    use="Aprenderé a calcular el volumen de un lote con su factor de estiba y a comprobar si una carga cabe por volumen y por peso, respetando el orden de descarga.",
    prior=["Sé multiplicar y restar números enteros.", "Sé revisar límites de peso en una planilla.", "Sé qué es el orden de descarga."],
    explain=[
        "Una carga debe caber por peso y por volumen, y son dos comprobaciones distintas. El factor de estiba es el volumen que ocupa una tonelada de carga, incluidos los espacios entre bultos, y se mide en metros cúbicos por tonelada. El volumen de un lote es sus toneladas multiplicadas por el factor. La carga liviana y voluminosa tiene un factor alto porque ocupa mucho espacio por tonelada; la carga muy densa tiene un factor bajo.",
        "La capacidad de volumen de una bodega es el espacio total, en metros cúbicos, disponible para la carga. Para saber si algo cabe se suman los volúmenes de los lotes y se compara con esa capacidad; por separado se suman los pesos y se comparan con el límite de peso. Si cabe por volumen pero no por peso, o al revés, no cabe. El plan, además, ordena los lotes según el orden de descarga para que el primero en bajarse quede accesible.",
        f"Los factores, volúmenes y límites son de ejemplo para un cálculo de planilla; este cuaderno no enseña a ubicar ni sujetar la carga. {EMER} {AVISO}",
    ],
    vocab=[("factor de estiba", "volumen que ocupa una tonelada de carga, incluidos los espacios entre bultos"), ("metro cúbico (m³)", "unidad de volumen"), ("capacidad de volumen", "espacio total disponible en la bodega, en metros cúbicos"), ("lote", "conjunto de carga del mismo tipo que se planifica junto"), ("carga voluminosa", "carga que ocupa mucho espacio por cada tonelada")],
    worked=[
        ("Volumen de un lote", "Un lote de ejemplo pesa 25 toneladas y su factor de estiba es 3 m³ por tonelada. ¿Qué volumen ocupa?", ["El volumen es las toneladas por el factor.", "25 por 3 son 75."], "75 m³"),
        ("Comparar con la capacidad", "Dos lotes de ejemplo ocupan 60 m³ y 45 m³. ¿Caben en una bodega de 100 m³?", ["El volumen total es 60 más 45, o sea 105.", "105 supera 100."], "No caben: 105 m³ superan los 100 m³ de la bodega"),
    ],
    mistakes=[("Creer que si la carga cabe por volumen, entonces también cabe por peso.", "El volumen y el peso son límites distintos y se revisan por separado.", "Haz dos comprobaciones: una de volumen y otra de peso."),
              ("Usar el peso como si fuera el volumen al comparar con la capacidad.", "La capacidad de volumen está en metros cúbicos, no en toneladas.", "Multiplica las toneladas por el factor para obtener el volumen.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es el factor de estiba?", "El volumen que ocupa una tonelada de carga, incluidos los espacios entre bultos", "El peso máximo que soporta una bodega", "El porcentaje de bultos que pueden apilarse", "El factor relaciona volumen y peso de la carga; no es un límite ni un porcentaje de apilado."),
        ("abc", "En Operaciones Portuarias: ¿qué es la capacidad de volumen de una bodega?", "El espacio total, en metros cúbicos, disponible para la carga", "El peso máximo que puede llevar", "El número de personas que caben en ella", "El volumen se mide en metros cúbicos; el peso máximo es otro límite."),
        ("abc", "En Operaciones Portuarias: ¿por qué se considera el orden de descarga al armar el plan?", "Para que la carga que se baja primero quede accesible y no se mueva otra sin necesidad", "Para que la nave llegue antes a su destino", "Porque la carga más pesada siempre se baja primero", "El orden de descarga busca accesibilidad; no acelera el viaje ni depende del peso."),
        ("=", "{F} ¿Cuántos metros cúbicos ocupa el lote X?", "90*2", "Se multiplican las toneladas del lote por su factor de estiba.", " m³"),
        ("=", "{F} ¿Cuántos metros cúbicos ocupan en total los tres lotes?", "90*2+50*3+40*4", "Se calcula el volumen de cada lote y se suman.", " m³"),
        ("abc", "{F} ¿Qué lote debe quedar más accesible para descargarse primero?", "El lote Z", "El lote X", "El lote Y", "El orden de descarga indica que el lote Z se baja primero."),
        ("=", "{F} Sin agregar nada, ¿cuántos metros cúbicos libres quedan en la bodega?", "600-(90*2+50*3+40*4)", "Se resta el volumen total de los lotes a la capacidad de la bodega.", " m³"),
        ("=", "{F} Sin agregar nada, ¿cuántas toneladas de margen quedan hasta el límite de peso de la bodega?", "200-(90+50+40)", "Se resta el peso total de los lotes al límite de peso.", " toneladas"),
        ("abc", "{F} Un cliente quiere agregar 30 toneladas más del lote Y, con el mismo factor. ¿Cabe?", "No, porque el peso total (210 toneladas) superaría el límite de 200 aunque el volumen sí alcance", "Sí, porque el volumen total seguiría bajo 600 m³", "No, porque el volumen superaría los 600 m³", "Con las 30 toneladas el volumen llega a 580 m³, pero el peso llega a 210."),
        ("abc", "{F} Un compañero dice: «si la carga cabe en volumen, ya sé que cabe en peso». ¿Qué respuesta es correcta?", "Es falso: el volumen y el peso son límites distintos y se revisan por separado", "Es cierto: a más volumen siempre hay más peso", "Es cierto, si todos los lotes son del mismo tipo", "Un lote voluminoso puede ser liviano y uno denso puede pesar mucho en poco volumen."),
        ("abc", "En Operaciones Portuarias: ¿qué carga suele tener un factor de estiba mayor?", "La carga liviana y voluminosa, porque ocupa mucho espacio por tonelada", "La carga muy densa y pesada", "La carga que viaja en contenedores", "Un factor alto significa mucho volumen por cada tonelada."),
        ("=", "{F} Otra bodega de ejemplo tiene 360 m³ de capacidad. Si se carga únicamente material del lote Z, con su factor, ¿cuántas toneladas caben como máximo por volumen?", "360//4", "Se divide la capacidad de volumen entre el factor de estiba.", " toneladas"),
        ("abc", "{F} Se quiere cargar los tres lotes y, además, 15 toneladas de un lote nuevo con factor 5. ¿Cabe?", "Sí, porque el peso llega a 195 toneladas y el volumen a 565 m³, ambos bajo los límites", "No, porque el peso y el volumen no pueden sumarse", "No, porque el lote nuevo debe descargarse primero", "El peso y el volumen se suman por separado y ambos quedan dentro de los límites."),
    ],
    ctx=("abc", "En una práctica de ejemplo, un compañero calcula solo el peso de una carga y dice que «ya se sabe que cabe». ¿Qué le respondes?", "Que también hay que comprobar el volumen, porque son límites distintos", "Que tiene razón, porque el peso lo decide todo", "Que el volumen solo se revisa si la carga es frágil", "Cada límite se comprueba por separado; cumplir uno no garantiza el otro."),
    sc=[
        ("En Operaciones Portuarias: ¿cómo se calcula el volumen de un lote?", "Multiplicando sus toneladas por el factor de estiba", "El factor dice cuántos metros cúbicos ocupa cada tonelada."),
        ("¿Qué dos comprobaciones hacen falta para saber si una carga cabe?", "Una por volumen y otra por peso", "Son dos límites distintos y se revisan por separado."),
        ("¿Qué carga tiene factor de estiba alto?", "La liviana y voluminosa", "Ocupa mucho espacio por cada tonelada de carga."),
    ],
    op=("Bodega de ejemplo con 400 m³ de capacidad de volumen y 150 toneladas de límite de peso. Lote A: 40 toneladas, factor 3. Lote B: 30 toneladas, factor 5. Lote C: 50 toneladas, factor 2. Orden de descarga: primero C, después B y al final A. Escribe (a) el volumen de cada lote, (b) el volumen total y si cabe, (c) el peso total y si cumple el límite, (d) qué lote debe quedar más accesible.",
        "(a) Lote A: 40 × 3 = 120 m³. Lote B: 30 × 5 = 150 m³. Lote C: 50 × 2 = 100 m³. (b) 120 + 150 + 100 = 370 m³, que no supera 400: cabe por volumen. (c) 40 + 30 + 50 = 120 toneladas, que no supera 150: cumple. (d) El lote C, porque se descarga primero.",
        ["calcula el volumen de cada lote", "suma y compara con la capacidad", "suma y compara el peso", "usa el orden de descarga"],
        ["hoja con las cuatro respuestas"],
        ["comparar toneladas con metros cúbicos", "revisar solo el volumen o solo el peso", "ignorar el orden de descarga"],
        "Pregunta: «¿qué dos límites hay que revisar?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa dos lotes con su peso y su factor y calcula el volumen de cada uno y el total.",
    extend="Explica con un ejemplo por qué una carga voluminosa y liviana puede llenar una bodega sin acercarse a su límite de peso.",
)
