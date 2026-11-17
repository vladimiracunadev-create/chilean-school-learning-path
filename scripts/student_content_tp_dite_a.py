"""Dibujo Técnico TP 3.º y 4.º medio: OAE-01 (leer información técnica) y OAE-02 (levantamientos y croquis a mano). Todo en papel; planos descritos por escrito; datos de ejemplo."""
from __future__ import annotations

from tp_dite_common import build

O1 = "TP-DITE-3y4-OAE-01"
O2 = "TP-DITE-3y4-OAE-02"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (documentos de ejemplo, inventados). El estudio «Taller Gráfico Ñuble» recibe de la mandante, la señora Mora, tres documentos para ampliar una bodega: "
     "(1) un plano cuyo rótulo dice «Bodega, planta, escala 1:50, revisión B»; (2) un croquis a mano alzada, sin escala, con las medidas del terreno anotadas por ella; "
     "(3) un correo que dice: «Necesito la ampliación lista el día 30; el plano es confidencial y no debe compartirse con terceros».")
build(
    O1, 1, F,
    use="Aprenderé qué documentos entregan información técnica, cómo leer su rótulo y escala, y por qué los planos son confidenciales y propiedad de quien los crea.",
    prior=["Sé multiplicar y dividir.", "Sé que 1 m son 100 cm.", "Sé que un dibujo puede representar algo más grande."],
    explain=[
        "La información técnica es todo dato escrito o dibujado que sirve para proyectar. El plano es un dibujo a escala, con medidas, que representa un objeto o una obra. El croquis es un dibujo a mano alzada, rápido, que no siempre va a escala. El manual explica las características o el uso de un producto; el informe describe una inspección o un resultado; y el mandante es la persona que encarga el trabajo y fija lo que necesita. Leer bien es identificar qué se pide, qué dato falta y qué dato parece incorrecto antes de dibujar.",
        "Todo plano tiene un rótulo: el cuadro donde aparecen el nombre del proyecto, la escala, la fecha, el autor y la revisión, que es la versión del documento (A, B, C…). Se trabaja siempre con la revisión vigente. La escala 1:50 significa que 1 unidad en el dibujo representa 50 unidades reales. Para pasar del dibujo a la realidad se multiplica por el número de la derecha, y para dibujar se divide. Recuerda que 100 cm son 1 m. Los rótulos y símbolos se escriben según la norma de dibujo vigente.",
        "Los planos son propiedad intelectual de quien los crea y confidenciales para quien los encarga: no se copian, no se muestran ni se envían a terceros sin permiso, aunque se les borre el rótulo. Y dibujar muchas horas exige ergonomía: mesa y silla a buena altura, el tablero a la vista sin torcer el cuello y pausas breves para estirar el cuerpo.",
    ],
    vocab=[("plano", "dibujo a escala con medidas que representa un objeto o una obra"), ("croquis", "dibujo a mano alzada, rápido, no siempre a escala"), ("mandante", "persona que encarga el trabajo y fija lo que necesita"), ("rótulo", "cuadro del plano con nombre, escala, fecha, autor y revisión"), ("escala", "relación entre una medida del dibujo y la medida real"), ("revisión", "versión del documento, indicada con letras"), ("propiedad intelectual", "derecho de quien crea un diseño a decidir quién lo copia o usa")],
    worked=[
        ("Pasar del dibujo a la realidad", "Un plano de ejemplo está a escala 1:20. Una pared mide 15 cm en el dibujo. ¿Cuánto mide en la realidad?", ["La escala 1:20 indica que cada 1 cm del dibujo son 20 cm reales.", "Se multiplica: 15 × 20 = 300 cm, que son 3 m."], "300 cm, es decir, 3 m"),
        ("Elegir el documento vigente", "Una empresa de ejemplo tiene dos copias del mismo plano: una dice «revisión A, 3 de mayo» y otra «revisión C, 10 de junio». ¿Cuál usas y qué haces para estar seguro?", ["La letra más avanzada y la fecha más reciente indican la versión vigente: la C.", "Antes de dibujar, confirmas con quien emitió el plano que la C sigue vigente."], "La revisión C, confirmada con quien la emitió"),
    ],
    mistakes=[("Usar un plano viejo porque «es el que tengo a mano».", "Cada revisión puede cambiar medidas; trabajar con una versión antigua produce errores.", "Revisa la letra y la fecha de la revisión y confirma que es la vigente."),
              ("Mandar el plano a un amigo para que opine, borrando antes el rótulo.", "Borrar el rótulo no quita la confidencialidad ni la autoría: seguiría siendo un documento ajeno.", "Pide permiso por escrito a la mandante antes de mostrarlo a otra persona.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es un croquis?", "Un dibujo hecho a mano alzada, rápido, que no siempre va a escala", "Un plano final con rótulo y escala exacta aprobado por el mandante", "Un manual con las instrucciones de un equipo", "El croquis se hace rápido y a mano; el plano final lleva rótulo y escala, y el manual es texto."),
        ("abc", "¿Qué indica la revisión que aparece en el rótulo de un plano?", "La versión del documento, para saber si es la vigente", "La cantidad de hojas que tiene el plano", "La escala con que se dibujó", "La revisión se anota con letras y permite distinguir versiones del mismo plano."),
        ("abc", "{F} ¿Quién es la mandante en este caso?", "La señora Mora, que encarga el trabajo y fija lo que necesita", "El Taller Gráfico Ñuble, que prepara los planos", "La bodega, que será ampliada", "El mandante es quien encarga; el taller dibuja y la bodega es el objeto del trabajo."),
        ("=", "{F} El plano (1) está a escala 1:50 y un muro mide 12 cm en el dibujo. ¿Cuántos centímetros mide en la realidad?", "12*50", "Para pasar del dibujo a la realidad se multiplica por 50.", " cm"),
        ("abc", "{F} ¿Cuál de los documentos de la ficha es un croquis?", "El documento (2), hecho a mano alzada y sin escala", "El documento (1), porque tiene rótulo y escala", "El documento (3), porque trae medidas en palabras", "El croquis es el dibujo sin escala hecho a mano; el plano tiene rótulo y escala."),
        ("abc", "{F} ¿Qué dato del rótulo del documento (1) permite convertir medidas del dibujo en medidas reales?", "La escala 1:50", "La revisión B", "El nombre del proyecto", "La escala relaciona el dibujo con la realidad; la revisión solo indica la versión."),
        ("=", "Un plano de ejemplo está a escala 1:100 y una sala mide 8 cm en el dibujo. ¿Cuántos metros mide en la realidad?", "8*100//100", "Se multiplica por 100 para obtener centímetros reales y se divide por 100 para pasar a metros.", " m"),
        ("abc", "{F} Un compañero quiere enviar el plano a un amigo «para que opine». ¿Qué corresponde?", "No enviarlo sin permiso de la mandante, porque es confidencial", "Enviarlo, porque un amigo no compite con la mandante", "Enviarlo después de borrar el rótulo para que no se sepa de quién es", "El correo (3) pide confidencialidad; borrar el rótulo no cambia que el plano es ajeno."),
        ("ab", "Una persona dibuja cuatro horas seguidas con el cuello torcido hacia el tablero. ¿Cuál es la mejor corrección?", "Ajustar la altura del tablero y la silla, y hacer pausas breves para estirarse", "Seguir sin pausas para terminar antes y descansar al final del día", "Una postura mantenida durante horas cansa y causa molestias; la corrección es ajustar el puesto y pausar."),
        ("abc", "Recibes un plano sin fecha ni revisión en el rótulo. ¿Qué haces antes de dibujar a partir de él?", "Pido a quien lo entregó que confirme su origen y su versión vigente", "Lo uso igual, porque todo plano entregado es válido", "Le anoto yo la fecha de hoy y la revisión A", "Sin fecha ni revisión no se sabe si está vigente; inventar esos datos tampoco lo valida."),
        ("abc", "{F} El croquis dice que el frente del terreno mide 12 m; el plano (1), a escala 1:50, dibuja ese frente con 20 cm. ¿Qué haces?", "Detecto una diferencia entre los dos documentos y la consulto con la mandante antes de dibujar", "Uso la medida del plano, porque tiene rótulo", "Uso el promedio de las dos medidas", "20 cm × 50 son 10 m, no 12 m: hay un posible error que solo la mandante puede aclarar."),
        ("=", "{F} Según el plano (1), un lado de la bodega se dibuja con 20 cm. El croquis (2) dice que ese lado mide 12 m. ¿Cuántos centímetros de diferencia hay entre la medida del croquis y la del plano?", "12*100-20*50", "Se pasan ambas medidas a centímetros reales y se restan.", " cm"),
        ("abc", "Un informe de ejemplo dice «la sala mide 3 m de ancho», pero su lista de medidas anota 3,5 m. ¿Cómo lo tratas?", "Lo marco como posible error y lo consulto con quien escribió el informe", "Uso la medida menor para estar más seguro", "Uso la de la lista sin avisar, porque está al final", "Dos datos distintos para lo mismo son un error posible; se consulta, no se elige a ojo."),
    ],
    ctx=("abc", "Una vecina de la mandante te pide ver el plano de la bodega «solo para curiosear». ¿Qué corresponde?", "Decirle que solo la mandante puede autorizarlo y consultarle a ella", "Mostrárselo, porque la vecina es de confianza", "Dárselo si promete no sacarle copias", "El plano es confidencial; el permiso lo da la mandante, no quien lo tiene en sus manos."),
    sc=[
        ("En Dibujo Técnico: ¿qué indica la escala 1:50?", "Que 1 unidad del dibujo representa 50 unidades reales", "Por eso se multiplica por 50 para pasar a medidas reales."),
        ("¿Para qué sirve el rótulo de un plano?", "Para identificar proyecto, escala, fecha, autor y revisión", "Con esos datos se sabe qué plano es y si es la versión vigente."),
        ("¿Qué haces si dos documentos dan medidas distintas para lo mismo?", "Lo marco como posible error y lo consulto antes de dibujar", "Nunca se elige una medida al azar ni se inventa un promedio."),
    ],
    op=("Recibes de un mandante de ejemplo un plano de una sala de reuniones a escala 1:50, revisión C, donde el ancho se dibuja con 9 cm, y un correo que dice «la sala mide 5 m de ancho». Calcula el ancho real que da el plano, compáralo con el correo y escribe una nota de tres líneas: qué diferencia hallaste, a quién se la preguntas y qué no harás mientras no te respondan.",
        "9 × 50 = 450 cm, es decir, 4,5 m. El correo dice 5 m: hay 50 cm de diferencia. Nota: «El plano rev. C da 4,5 m y el correo 5 m. Le pregunto al mandante cuál medida es la correcta. Mientras tanto no dibujo el ancho ni elijo una de las dos medidas por mi cuenta».",
        ["calcula bien el ancho real con la escala", "detecta y cuantifica la diferencia", "dice a quién consulta y no inventa una medida"],
        ["hoja con el cálculo y la nota de tres líneas"],
        ["dividir por 50 en vez de multiplicar", "promediar las dos medidas", "no indicar a quién se consulta"],
        "Pregunta: «¿por qué no puedes quedarte con la medida del plano?». Si no puede responder, pídele que repita la comparación en centímetros."),
    reinforce="Elige un objeto de tu casa, imagina un plano a escala 1:10 y calcula cuánto mediría en el dibujo uno de sus lados.",
    extend="Explica con un ejemplo inventado por qué una nota con la revisión del plano evita errores en un equipo de varias personas.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (obra de ejemplo, inventada): «Casa Los Copihues». Documentos del proyecto: la planta (vista de la casa desde arriba), la elevación (vista de frente de una fachada), "
     "el corte (vista de la casa como si se la cortara de arriba abajo), la planilla de cotas (tabla de medidas) y la memoria técnica (texto que describe materiales y criterios). "
     "Roles: la mandante encarga; la proyectista diseña y decide; el dibujante pasa lo decidido a planos; el revisor comprueba que los planos sean coherentes. "
     "Datos de la planilla (en cm): muro norte, largo 480, con una puerta de 90 y una ventana de 120 de ancho; el living es un rectángulo de 5 m de largo por 4 m de ancho.")
build(
    O1, 2, F,
    use="Aprenderé los documentos de un proyecto de dibujo, qué muestra cada uno y qué rol hace cada persona del equipo.",
    prior=["Sé qué son un plano, un croquis y una escala.", "Sé que 1 m son 100 cm.", "Sé calcular la superficie de un rectángulo."],
    explain=[
        "Un proyecto reúne varios documentos y cada uno muestra algo distinto. La planta muestra el objeto visto desde arriba, con sus muros y puertas. La elevación muestra una fachada vista de frente. El corte muestra el interior como si se hubiera cortado el objeto, y permite leer alturas. La planilla de cotas ordena las medidas en una tabla, y la memoria técnica describe por escrito los materiales y los criterios. Para que el proyecto sea coherente, una medida no puede cambiar de un documento a otro.",
        "Cada persona cumple un rol. La mandante encarga y aprueba. La proyectista diseña y decide cualquier cambio. El dibujante representa lo decidido y no cambia el diseño por su cuenta: si cree que algo debe mejorar, lo propone por escrito. El revisor comprueba la coherencia entre documentos y avisa de los errores, pero la decisión de corregir vuelve a la proyectista.",
        "Las unidades deben ser iguales en todo el proyecto: 1 cm son 10 mm y 1 m son 100 cm. La superficie de un rectángulo es largo por ancho, y si el largo y el ancho están en metros, el resultado queda en metros cuadrados (m²).",
    ],
    vocab=[("planta", "vista del objeto desde arriba"), ("elevación", "vista de frente de una fachada"), ("corte", "vista del interior como si se cortara el objeto"), ("planilla de cotas", "tabla ordenada con las medidas del proyecto"), ("memoria técnica", "texto que describe materiales y criterios"), ("proyectista", "persona que diseña y decide el proyecto"), ("coherencia", "que los documentos no se contradigan entre sí")],
    worked=[
        ("Elegir el documento", "Una empresa de ejemplo quiere saber cuánto sube el techo de un galpón respecto del piso. ¿Qué documento usa?", ["La altura se lee en una vista lateral que corte el galpón.", "Esa vista es el corte."], "El corte"),
        ("Cambiar unidades", "En una planilla de ejemplo, una viga mide 2.400 mm. ¿Cuántos centímetros son?", ["1 cm equivale a 10 mm.", "2.400 ÷ 10 = 240 cm."], "240 cm"),
    ],
    mistakes=[("Cambiar el tamaño de una ventana porque «se vería mejor más grande».", "El dibujante no decide el diseño; ese cambio le corresponde a la proyectista.", "Propón el cambio por escrito y espera la decisión."),
              ("Creer que una planta y una elevación mostrando lo mismo deben verse iguales.", "Muestran vistas distintas del mismo objeto: arriba y de frente; lo que debe coincidir son las medidas.", "Compara medidas, no la forma de la vista.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué muestra una planta?", "El objeto visto desde arriba", "Una fachada vista de frente", "El interior cortado de arriba abajo", "La planta es la vista desde arriba; de frente es la elevación y cortada es el corte."),
        ("abc", "En Dibujo Técnico: ¿qué muestra un corte?", "El interior del objeto como si se lo hubiera cortado", "Solo la superficie exterior vista desde arriba", "Una tabla con las medidas", "El corte deja ver el interior y las alturas; la tabla es la planilla de cotas."),
        ("abc", "¿Quién decide los cambios de diseño en un proyecto?", "La proyectista", "El dibujante, por su cuenta", "El revisor, sin consultar", "El diseño lo decide la proyectista; dibujante y revisor proponen o avisan."),
        ("abc", "{F} Para ver cómo se ve de frente la fachada de la casa, ¿qué documento usas?", "La elevación", "La planta", "La planilla de cotas", "La fachada vista de frente se muestra en la elevación."),
        ("=", "{F} En el muro norte, ¿cuántos centímetros de muro quedan sin puerta ni ventana?", "480-90-120", "Se restan al largo del muro los anchos de la puerta y la ventana.", " cm"),
        ("abc", "{F} ¿Qué rol hace el dibujante?", "Pasar a planos lo que la proyectista decidió, sin cambiar el diseño por su cuenta", "Decidir el diseño final cuando le parece mejor", "Aprobar la obra en nombre de la mandante", "El dibujante representa lo decidido; decidir y aprobar corresponde a otros roles."),
        ("=", "Una puerta de ejemplo mide 2.100 mm de alto. ¿Cuántos centímetros son?", "2100//10", "Como 1 cm son 10 mm, se divide por 10.", " cm"),
        ("=", "{F} ¿Cuántos m² tiene el living?", "5*4", "La superficie de un rectángulo es largo por ancho.", " m²"),
        ("abc", "{F} El revisor ve que la planta dibuja la puerta con 90 cm y la elevación con 100 cm. ¿Qué corresponde?", "Informar la diferencia y que la proyectista decida cuál medida vale", "Que el dibujante elija la medida que se ve mejor", "Anotar 95 cm, el promedio de las dos", "El revisor avisa de las incoherencias y quien decide es la proyectista."),
        ("abc", "{F} Una pared mide 400 cm en la planta y 4 m en el corte. ¿Hay una contradicción?", "No: 4 m son 400 cm, es la misma medida en otra unidad", "Sí: el corte siempre debe mostrar medidas menores", "Sí: planta y corte no se pueden comparar", "Al convertir 4 m a centímetros se obtiene 400 cm: coinciden."),
        ("ab", "El dibujante cree que la ventana quedaría mejor más grande. ¿Qué hace?", "Lo propone por escrito a la proyectista y espera su decisión", "La agranda en el plano para ahorrar tiempo", "Un cambio de diseño solo puede decidirlo la proyectista, por eso se le propone y se espera."),
        ("abc", "El revisor recibe una planta y una elevación, pero no la memoria técnica. ¿Qué no podrá comprobar?", "Los materiales y criterios descritos por escrito", "Las medidas de la planta", "La escala de la elevación", "Los materiales y criterios están en la memoria técnica; las medidas y escalas están en los planos."),
        ("=", "El revisor de un estudio de ejemplo debe revisar 9 planos. Revisa 2 por hora durante 3 horas. ¿Cuántos planos le quedan sin revisar?", "9-2*3", "Se multiplican los planos por hora por las horas y se resta del total.", " planos"),
    ],
    ctx=("abc", "La mandante pide cambiar una puerta de lugar. El dibujante la mueve en la planta, pero olvida la elevación. ¿Qué falla?", "La coherencia: una medida cambió en un documento y no en el otro", "La escala del rótulo", "La confidencialidad del plano", "Un cambio debe reflejarse en todos los documentos que muestran ese elemento."),
    sc=[
        ("En Dibujo Técnico: ¿qué es una elevación?", "La vista de frente de una fachada", "Se usa para ver altura y aspecto exterior de un lado."),
        ("¿Qué hace el revisor cuando encuentra una incoherencia?", "La informa para que la proyectista decida", "El revisor avisa, pero no decide el diseño."),
        ("¿Por qué deben ser iguales las unidades en todos los documentos?", "Para no confundir medidas como 6 m con 6 cm", "Mezclar unidades produce errores graves al dibujar."),
    ],
    op=("Una casa de ejemplo tiene una sala rectangular de 6 m de largo por 3 m de ancho. La planilla anota el largo en metros, pero la elevación lo anota como 6.000 mm. Calcula la superficie de la sala, comprueba si las dos medidas coinciden y escribe qué documento mostraría la altura de la sala y qué rol decidiría un cambio de ancho.",
        "Superficie: 6 × 3 = 18 m². 6.000 mm ÷ 10 = 600 cm = 6 m: las medidas coinciden. La altura se lee en el corte. Un cambio de ancho lo decide la proyectista, el dibujante lo propone por escrito.",
        ["calcula la superficie", "convierte unidades y compara", "nombra el documento y el rol correctos"],
        ["hoja con cálculo, conversión y dos frases"],
        ["no convertir los milímetros", "decir que el dibujante decide el cambio", "confundir corte con planta"],
        "Pregunta: «¿cómo sabes que las dos medidas son la misma?». Si no puede responder, pídele que escriba ambas en centímetros."),
    reinforce="Dibuja a mano alzada la planta de tu pieza con sus medidas aproximadas y anota qué documento mostraría su altura.",
    extend="Explica con un ejemplo inventado qué problema produce que el dibujante cambie el diseño sin avisar.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (planilla de cotas de ejemplo, inventada) del «Taller Mora». Unidad: centímetros, salvo donde se indique. Largo total del taller: 1200. "
     "Tramos que lo forman, de izquierda a derecha: 450; 380; 3,5 m; 320. Altura de muro: 250. Puerta: ancho 90, alto 210. "
     "Ventana: ancho 150, alto 100, alféizar (altura desde el piso hasta el borde inferior de la ventana) 100. Escala del plano: 1:50.")
build(
    O1, 3, F,
    use="Aprenderé a revisar una planilla de cotas, a detectar errores de cierre, de unidades y de coherencia, y a registrarlos sin inventar datos.",
    prior=["Sé convertir metros a centímetros.", "Sé qué es una escala.", "Sé sumar y restar medidas."],
    explain=[
        "Detectar errores es comprobar antes de dibujar. Una cota es la medida anotada en un plano; la cota parcial mide un tramo y la cota total mide el largo completo. Primer control, el cierre de cotas: la suma de las cotas parciales debe ser igual a la cota total. Segundo control, las unidades: todas las medidas deben estar en la misma unidad, y 1 m son 100 cm.",
        "Tercer control, la coherencia: los elementos deben caber. Por ejemplo, la puerta no puede ser más alta que el muro, y el alféizar más el alto de la ventana no puede superar la altura del muro. Hay dos tipos de problema: el error (dos datos que se contradicen) y la omisión (falta un dato). Un dato faltante se pide a quien emitió el plano; nunca se inventa ni se mide con regla sobre el dibujo.",
        "Cada hallazgo se registra con su ubicación, el valor leído, el valor esperado y a quién se consultó. Para dibujar, la longitud en el papel es la longitud real dividida por el número de la escala; por ejemplo, 600 cm a escala 1:50 se dibujan con 12 cm.",
    ],
    vocab=[("cota", "medida anotada en un plano"), ("cota parcial", "medida de un tramo"), ("cota total", "medida del largo o alto completo"), ("cierre de cotas", "comprobar que las parciales suman la total"), ("alféizar", "altura desde el piso hasta el borde inferior de una ventana"), ("omisión", "dato necesario que falta")],
    worked=[
        ("Revisar el cierre", "Un plano de ejemplo anota una cota total de 900 cm y tres tramos de 400, 300 y 250 cm. ¿Cierran?", ["Se suman los tramos: 400 + 300 + 250 = 950 cm.", "950 es distinto de 900: no cierran, sobran 50 cm."], "No cierran: los tramos suman 50 cm más que el total"),
        ("Unificar unidades", "Una cota dice 2,4 m y otra dice 240 cm para el mismo muro. ¿Hay error?", ["2,4 m × 100 = 240 cm.", "Las dos medidas son iguales."], "No hay error: son la misma medida"),
    ],
    mistakes=[("Corregir el error del total cambiando el número por la suma de los tramos, sin consultar.", "Puede estar equivocado el total o puede estarlo un tramo; solo quien emitió la planilla lo sabe.", "Registra el hallazgo y consulta antes de modificar."),
              ("Sumar 3,5 con los demás tramos sin pasar a la misma unidad.", "Mezclar metros con centímetros da una suma sin sentido.", "Convierte todo a centímetros antes de sumar.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es la cota total?", "La medida que abarca todo el largo o el alto", "La medida de un solo tramo", "La escala del plano", "La cota total es la completa; las parciales miden cada tramo."),
        ("abc", "¿Qué significa «cierre de cotas»?", "Que la suma de las cotas parciales da la cota total", "Que se cierra el dibujo con un marco", "Que todas las cotas están en metros", "El cierre es una comprobación de suma entre parciales y total."),
        ("abc", "¿Qué haces si falta una cota necesaria?", "La pido a quien entregó el plano y no la invento", "La mido con regla sobre el dibujo y la uso como definitiva", "Dejo el espacio en blanco sin avisar", "Un dato omitido se solicita al emisor; medirlo sobre el dibujo no es una medida confiable."),
        ("=", "{F} El tercer tramo está anotado como 3,5 m. ¿Cuántos centímetros son?", "3.5*100", "Un metro son 100 centímetros.", " cm"),
        ("=", "{F} Con el tercer tramo ya en centímetros, ¿cuánto suman los cuatro tramos?", "450+380+350+320", "Se suman los cuatro tramos en la misma unidad.", " cm"),
        ("abc", "{F} ¿Qué error principal tiene la planilla?", "Los tramos suman más que el largo total", "La puerta es más alta que el muro", "La escala está escrita en metros", "Los tramos suman 1.500 cm y el total dice 1.200; la puerta de 210 cm cabe en un muro de 250 cm."),
        ("=", "{F} ¿Cuántos centímetros de diferencia hay entre la suma de los tramos y el largo total?", "450+380+350+320-1200", "Se resta el largo total a la suma de los tramos.", " cm"),
        ("abc", "{F} ¿Cabe la ventana bajo la altura del muro?", "Sí: alféizar 100 más alto 100 suman 200 cm, menos que 250 cm", "No: 100 más 150 suman 250 cm y no sobra espacio", "No se puede saber sin conocer la escala", "Se suman alféizar y alto de la ventana, no su ancho: 200 cm es menor que 250 cm."),
        ("ab", "{F} Un compañero anota: «error: la puerta mide 210 cm y el muro 250 cm, no cabe». ¿Tiene razón?", "No: 210 cm es menor que 250 cm, por lo tanto sí cabe", "Sí: la puerta es demasiado alta para el muro", "Como 210 es menor que 250, la puerta cabe y su anotación de error es equivocada."),
        ("abc", "{F} ¿Qué anotas en el registro del error de cierre?", "Dónde está, qué valor leí y cuál esperaba", "Quién tuvo la culpa del error", "El nuevo total corregido por mí", "El registro describe ubicación, valor leído y valor esperado, sin culpar ni corregir por su cuenta."),
        ("=", "{F} A escala 1:50, ¿cuántos centímetros de papel ocupa el largo total de 1200 cm?", "1200//50", "Para dibujar, la medida real se divide por el número de la escala.", " cm"),
        ("=", "{F} Supón que el largo total de 1200 y los tramos de 450, 380 y 320 fueran correctos. ¿Cuánto debería medir el tercer tramo?", "1200-450-380-320", "Se resta del total la suma de los otros tres tramos.", " cm"),
        ("abc", "{F} ¿Quién decide cuál dato es el correcto: el total o los tramos?", "Quien emitió la planilla, tras revisar el levantamiento original", "El dibujante, eligiendo el dato que le parezca", "Se elige siempre el número menor", "Solo quien emitió los datos puede confirmar cuál es el correcto."),
    ],
    ctx=("abc", "Entregas hoy un plano y descubres un error de cierre de 300 cm. Tu jefa dice «entrega igual». ¿Qué corresponde?", "Informar el error por escrito a la jefa y a quien emitió los datos, y proponer corregir antes de entregar", "Entregar igual sin comentar nada", "Corregirlo en silencio cambiando el total a 1.500", "Un error conocido se informa por escrito y se resuelve con quien emitió los datos."),
    sc=[
        ("En Dibujo Técnico: ¿qué es el cierre de cotas?", "Comprobar que las cotas parciales suman la cota total", "Es el primer control al revisar una planilla."),
        ("¿Qué datos lleva el registro de un error?", "Ubicación, valor leído, valor esperado y a quién se consultó", "Con esos datos el error se puede verificar y resolver."),
        ("¿Qué haces con un dato omitido?", "Lo pido a quien emitió el plano", "No se inventa ni se mide sobre el dibujo."),
    ],
    op=("Una planilla de ejemplo anota para una pared: cota total 700 cm; tramos 250 cm, 2,2 m y 200 cm. La altura del muro es 240 cm y una ventana tiene alféizar 110 cm y alto 150 cm. Revisa el cierre, las unidades y si la ventana cabe, y escribe el registro de cada hallazgo con ubicación, valor leído y valor esperado.",
        "Tramos en cm: 250 + 220 + 200 = 670; la total dice 700: faltan 30 cm (error de cierre). La ventana: 110 + 150 = 260 cm, mayor que 240 cm: no cabe. Registro 1: pared, leído 670, esperado 700. Registro 2: ventana, leído 260, esperado como máximo 240. Se consulta a quien emitió la planilla.",
        ["convierte 2,2 m a centímetros", "calcula el cierre y la altura de la ventana", "registra los dos hallazgos sin corregirlos por su cuenta"],
        ["hoja con los cálculos y dos registros"],
        ["sumar sin convertir 2,2 m", "sumar el ancho de la ventana en vez de su alto", "cambiar un número sin consultar"],
        "Pregunta: «¿qué dato corregirías primero y quién debe confirmarlo?». Si dice que lo corrige él, repasa la regla de consultar al emisor."),
    reinforce="Mide tres tramos de una pared de tu casa en centímetros, anota el total y comprueba si cierra.",
    extend="Explica con un ejemplo inventado la diferencia entre un error y una omisión y qué se hace en cada caso.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (pedido de ejemplo, inventado). La empresa «Muebles Cordillera» pide el plano de una mesa de oficina: largo 1800 mm, ancho 800 mm, alto 750 mm. "
     "El manual de ejemplo del fabricante dice: tablero de 25 mm de espesor; patas de 60 mm de lado. Hoja disponible: A3 en horizontal, de 420 mm de ancho por 297 mm de alto, "
     "con un margen de 10 mm por cada lado. Escalas habituales: 1:2, 1:5, 1:10, 1:20.")
build(
    O1, 4, F,
    use="Aprenderé a relevar los datos necesarios de un pedido y un manual, y a elegir la escala para que un dibujo quepa en la hoja.",
    prior=["Sé qué es una escala.", "Sé que 1 cm son 10 mm.", "Sé restar medidas."],
    explain=[
        "Relevar datos es seleccionar y anotar, de los documentos recibidos, solo lo que se necesita para dibujar: medidas con su unidad, materiales, cantidades, hoja y fecha de entrega. Lo que falta se pide al mandante; lo que no sirve no se copia. Después de dibujar se vuelve al pedido y se marca cada dato usado para comprobar que no quedó ninguno afuera.",
        "El formato de papel define el espacio disponible. Una hoja A4 mide 210 mm por 297 mm y una A3 mide 297 mm por 420 mm. El área útil es la parte que queda dentro de los márgenes: se resta el margen dos veces, una por cada lado. Si además hay un rótulo, también se descuenta su espacio.",
        "Para elegir la escala se busca la mayor escala habitual en que el dibujo cabe en el área útil. Una escala mayor tiene el número de la derecha más pequeño: 1:2 es mayor que 1:5. En el papel, la medida es la medida real dividida por el número de la escala. Si el pedido cambia, se anota una nueva revisión y no se modifica el dibujo sin dejar registro.",
    ],
    vocab=[("relevar datos", "seleccionar y anotar los datos necesarios de un documento"), ("área útil", "parte de la hoja que queda dentro de los márgenes"), ("margen", "espacio libre en los bordes de la hoja"), ("formato", "tamaño de la hoja, como A3 o A4"), ("escala mayor", "la que tiene el número de la derecha más pequeño"), ("espesor", "grosor de una pieza")],
    worked=[
        ("Ver si cabe", "Una pieza de ejemplo mide 600 mm de largo. La hoja es A4 horizontal (297 mm de ancho), con margen de 10 mm por lado, y se usa la escala 1:5. ¿Cabe?", ["Ancho útil: 297 − 10 − 10 = 277 mm.", "En el papel: 600 ÷ 5 = 120 mm, que es menor que 277 mm."], "Sí, cabe"),
        ("Relevar datos", "Un pedido de ejemplo dice: «necesito una repisa de madera de 900 mm de largo y 200 mm de fondo, con espesor de 18 mm; entrega el viernes». ¿Qué datos relevas?", ["Medidas: largo 900 mm, fondo 200 mm, espesor 18 mm.", "Material: madera; fecha de entrega: viernes."], "Largo 900 mm, fondo 200 mm, espesor 18 mm, madera, entrega el viernes"),
    ],
    mistakes=[("Elegir la escala más pequeña para estar seguro de que quepa.", "El dibujo queda diminuto y se pierden detalles; se busca la mayor escala que quepa.", "Prueba de la mayor a la menor y detente en la primera que cabe."),
              ("Olvidar descontar los márgenes al calcular el espacio de la hoja.", "El dibujo podría pasar sobre los márgenes y quedar cortado al imprimir.", "Resta el margen dos veces: uno por cada lado.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es el área útil de una hoja?", "La parte de la hoja que queda dentro de los márgenes", "Toda la hoja, incluido el borde", "Solo el espacio donde va el rótulo", "El área útil es la que queda libre una vez descontados los márgenes."),
        ("abc", "¿Cuál es el criterio para elegir la escala?", "La mayor escala habitual en que el dibujo cabe en el área útil", "La menor escala posible, para que siempre quepa", "Cualquiera, porque la escala no cambia el tamaño del dibujo", "La escala cambia el tamaño en el papel; se busca la mayor que quepa para ver bien los detalles."),
        ("abc", "En Dibujo Técnico: ¿qué es relevar datos?", "Seleccionar y anotar los datos del pedido que se necesitan para dibujar", "Copiar todo el pedido, incluso lo que no sirve", "Inventar los datos que no están", "Se anota lo necesario; lo faltante se pide y no se inventa."),
        ("=", "{F} ¿Cuántos milímetros de ancho útil tiene la hoja A3 con el margen de 10 mm por lado?", "420-2*10", "Se resta el margen dos veces al ancho de la hoja.", " mm"),
        ("=", "{F} ¿Cuántos milímetros de alto útil tiene la hoja con el margen de 10 mm por lado?", "297-2*10", "Se resta el margen dos veces al alto de la hoja.", " mm"),
        ("=", "{F} Con escala 1:5, ¿cuántos milímetros de papel ocupa el largo de la mesa?", "1800//5", "La medida real se divide por 5.", " mm"),
        ("abc", "{F} ¿Cabe el largo de la mesa en el ancho útil con la escala 1:5?", "Sí: 360 mm es menor que 400 mm", "No: 360 mm es mayor que 277 mm", "No: 1800 mm es mayor que 400 mm", "Se compara 360 mm con el ancho útil de 400 mm; olvidar la escala o usar el alto lleva a errores."),
        ("ab", "{F} ¿Es correcto elegir la escala 1:2 para el largo?", "No: 1800 ÷ 2 son 900 mm y superan los 400 mm útiles", "Sí: 1:2 es la escala más grande y siempre sirve", "A escala 1:2 el largo ocuparía 900 mm, que no cabe en un ancho útil de 400 mm."),
        ("abc", "{F} ¿Qué dato necesitas para dibujar el borde del tablero visto de lado?", "El espesor de 25 mm", "El lado de las patas, 60 mm", "El alto de la mesa, 750 mm", "El borde del tablero se dibuja con su espesor; el lado de las patas es otra medida."),
        ("=", "{F} Con escala 1:5, ¿cuántos milímetros de papel representan el espesor del tablero?", "25//5", "El espesor real se divide por 5.", " mm"),
        ("abc", "{F} El pedido no dice el color del tablero. ¿Qué haces?", "Lo pido a Muebles Cordillera antes de cerrar el plano", "Elijo yo un color que me parezca bonito", "Lo dejo sin color sin avisar a nadie", "Un dato faltante se pide a quien encarga el trabajo."),
        ("=", "{F} Con escala 1:5, la mesa vista de lado tiene un alto de 750 mm. ¿Cuántos milímetros sobran del alto útil de 277 mm?", "277-750//5", "Se resta al alto útil el alto del dibujo en el papel.", " mm"),
        ("abc", "{F} ¿Cuál es la mejor lista de datos relevados?", "Largo 1800, ancho 800, alto 750 mm; tablero 25 mm; patas 60 mm; hoja A3", "Una mesa grande de oficina con patas", "Las medidas de la mesa, sin unidades", "Una buena lista tiene cifras con unidad, componentes y formato de hoja."),
    ],
    ctx=("abc", "Después de aprobar el plano, Muebles Cordillera cambia por teléfono el largo a 2000 mm. ¿Qué haces?", "Pido que lo confirme por escrito y registro la nueva revisión", "Cambio el largo sin anotar nada, es solo una cifra", "Ignoro el cambio porque el pedido original ya estaba aprobado", "Un cambio de medidas se confirma por escrito y se registra como nueva revisión."),
    sc=[
        ("¿Cómo se calcula el ancho útil de una hoja?", "Se resta el margen dos veces al ancho de la hoja", "Hay un margen en cada lado."),
        ("¿Qué escala se elige para un dibujo?", "La mayor escala habitual en que el dibujo cabe", "Así el dibujo queda lo más grande y legible posible."),
        ("¿Qué haces cuando el pedido cambia?", "Pido confirmación por escrito y anoto una nueva revisión", "Así se sabe qué versión del plano es la vigente."),
    ],
    op=("Un taller de ejemplo pide el plano de un estante de 1200 mm de largo, 300 mm de fondo y 1800 mm de alto, con tableros de 18 mm de espesor, en una hoja A3 vertical (297 mm de ancho por 420 mm de alto) con margen de 10 mm por lado. Releva los datos, calcula el alto útil y decide si el alto del estante cabe a escala 1:5 y a escala 1:10.",
        "Datos: 1200 × 300 × 1800 mm, tableros de 18 mm, hoja A3 vertical. Alto útil: 420 − 20 = 400 mm. A 1:5: 1800 ÷ 5 = 360 mm, cabe. A 1:10: 180 mm, cabe pero más pequeño. Se elige 1:5, la mayor que cabe.",
        ["relevan todos los datos con unidad", "calculan el alto útil", "eligen la escala con el criterio de la mayor que cabe"],
        ["hoja con la lista de datos, los cálculos y la decisión"],
        ["no descontar los márgenes", "elegir 1:10 sin probar 1:5", "olvidar escribir las unidades"],
        "Pregunta: «¿por qué no eliges 1:10 si también cabe?». Si no responde, repasa el criterio de la mayor escala."),
    reinforce="Elige un libro, mide su largo en milímetros y calcula cuánto ocuparía en una hoja si lo dibujaras a escala 1:2.",
    extend="Explica con un ejemplo inventado qué problema produce relevar un dato sin su unidad.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (encargo de ejemplo, inventado). La junta de vecinos «Villa Los Aromos» pide el levantamiento de su sede, un salón rectangular. "
     "El equipo debe medir el interior con huincha (cinta métrica) desde el piso, sin subirse a muebles ni escaleras y con una persona adulta responsable presente. "
     "Croquis con las medidas anotadas: largo 9 m; ancho 6 m; altura del salón: sin medir. La sede tiene 1 puerta de 1 m de ancho y 2 ventanas de 2 m de ancho cada una.")
build(
    O2, 1, F,
    use="Aprenderé qué es un levantamiento, qué datos debe llevar un croquis de medidas y qué cuidados y límites tiene el trabajo de medición.",
    prior=["Sé calcular la superficie de un rectángulo.", "Sé usar metros y centímetros.", "Sé qué es un croquis."],
    explain=[
        "Un levantamiento consiste en medir y registrar cómo es algo que ya existe, para después dibujarlo. Puede ser una obra civil (una casa, un salón, un camino) o un conjunto mecánico, que es una máquina o un mecanismo formado por varias piezas unidas. El mandante fija qué se debe levantar y con qué detalle, y esas especificaciones se leen antes de medir.",
        "Primero se hace un croquis a mano alzada, con proporciones aproximadas y todas las medidas con su unidad: sin unidades, 6 m y 6 cm se confunden. Después, con el croquis, se dibuja el plano de levantamiento. El perímetro es la suma de los lados de una figura, la superficie de un rectángulo es largo por ancho y la superficie de muros es el perímetro por la altura.",
        "Este cuaderno es conceptual: no te habilita para medir en terreno. En un trabajo real se mide desde el piso, sin subir a escaleras, techos ni muebles, con una persona adulta responsable y con autorización de quien es dueño del lugar. Los planos de un tercero son confidenciales, y fotografiar a personas requiere su permiso.",
    ],
    vocab=[("levantamiento", "medir y registrar cómo es algo que ya existe"), ("especificaciones", "indicaciones del mandante sobre lo que necesita"), ("conjunto mecánico", "máquina o mecanismo formado por varias piezas"), ("perímetro", "suma de los lados de una figura"), ("huincha", "cinta métrica"), ("unidad", "medida que acompaña a un número, como m o cm")],
    worked=[
        ("Calcular perímetro y superficie", "Una sala de ejemplo mide 5 m de largo y 4 m de ancho. ¿Cuál es su perímetro y su superficie?", ["Perímetro: 5 + 4 + 5 + 4 = 18 m.", "Superficie: 5 × 4 = 20 m²."], "18 m de perímetro y 20 m² de superficie"),
        ("Detectar un dato faltante", "El mandante pide un corte de la sala, pero el croquis solo trae largo y ancho. ¿Qué falta?", ["El corte muestra alturas.", "Hay que medir la altura de la sala."], "La altura"),
    ],
    mistakes=[("Subirse a una silla para medir arriba cuando no hay escalera.", "Es un riesgo de caída; medir en altura exige personal autorizado y equipo adecuado.", "Mide solo desde el piso y anota lo que no se alcanzó para pedir ayuda."),
              ("Anotar «9» sin unidad en el croquis.", "Quien dibuje no sabrá si son metros, centímetros o milímetros.", "Escribe siempre la unidad junto al número.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es un levantamiento?", "Medir y registrar cómo es algo que ya existe, para dibujarlo", "Diseñar algo nuevo que todavía no existe", "Imprimir copias de un plano ya hecho", "Un levantamiento parte de lo existente; diseñar algo nuevo es otro trabajo."),
        ("abc", "¿Por qué el croquis de levantamiento lleva escritas las unidades?", "Para que nadie confunda 6 m con 6 cm al dibujar", "Para que el croquis quede a escala", "Porque la norma pide que las unidades sean pequeñas", "La unidad define el valor de la medida; no tiene que ver con la escala."),
        ("abc", "{F} Si el mandante pide también cortes, ¿qué medida falta en el croquis?", "La altura del salón", "El largo del salón", "El ancho de la puerta", "Los cortes muestran alturas y el croquis no trae la altura del salón."),
        ("=", "{F} ¿Cuántos m² de superficie tiene el salón?", "9*6", "La superficie de un rectángulo es largo por ancho.", " m²"),
        ("=", "{F} ¿Cuántos metros mide el perímetro del salón?", "2*(9+6)", "El perímetro suma los cuatro lados: dos largos y dos anchos.", " m"),
        ("abc", "{F} ¿Cuál es la conducta correcta para medir?", "Medir desde el piso con una persona adulta responsable presente", "Subirse a una silla para medir arriba si no hay escalera", "Medir solo y rápido para no molestar", "Medir desde el piso y acompañado reduce el riesgo; subirse a una silla es un riesgo de caída."),
        ("=", "{F} Las 2 ventanas miden 2 m de ancho cada una y la puerta 1 m. ¿Cuántos metros de ancho suman las ventanas y la puerta juntas?", "2*2+1", "Se suman los anchos de las dos ventanas y el de la puerta.", " m"),
        ("abc", "{F} Al llegar, el equipo ve una columna que no estaba en el pedido. ¿Qué hace?", "La anota en el croquis y avisa a la junta de vecinos", "La omite porque no estaba en el pedido", "La dibuja pero sin medirla", "Un elemento existente se registra, y se informa porque el pedido no lo mencionaba."),
        ("ab", "Una integrante quiere sacar fotos de las personas que usan el salón para «dar contexto al plano». ¿Qué corresponde?", "Fotografiar solo el espacio y pedir permiso si salen personas", "Sacar las fotos igual, porque es solo para el plano", "Las personas tienen derecho a su imagen; se pide permiso o se evita que aparezcan."),
        ("abc", "{F} Alguien propone dibujar además cómo quedaría el salón si se ampliara. ¿Qué es eso?", "Un proyecto de ampliación, que es otro encargo distinto del levantamiento", "Parte del levantamiento, porque también es un plano", "Un error de medición", "El levantamiento representa lo existente; una ampliación es un diseño nuevo."),
        ("=", "{F} Supón que después se mide una altura de 3 m. ¿Cuántos m² de muros tiene el salón, sin descontar puerta ni ventanas (perímetro por altura)?", "30*3", "La superficie de muros es el perímetro por la altura.", " m²"),
        ("=", "{F} Con la altura de 3 m, la puerta de 2 m de alto y las ventanas de 1 m de alto, ¿cuántos m² de muro quedan al descontar la puerta (1 m de ancho) y las 2 ventanas (2 m de ancho cada una)?", "90-1*2-2*(2*1)", "A los 90 m² de muros se restan la puerta y las dos ventanas.", " m²"),
        ("abc", "{F} Dos integrantes midieron el largo: uno anotó 9 m y otro 9,5 m. ¿Qué corresponde?", "Volver a medir juntos y registrar la medida acordada y quién la tomó", "Anotar el promedio, 9,25 m", "Anotar la mayor para estar seguros", "Una diferencia entre dos mediciones se aclara volviendo a medir, no promediando."),
    ],
    ctx=("abc", "La junta de vecinos encargó el levantamiento. Un integrante quiere llevarse el croquis para mostrarlo a otra empresa. ¿Qué corresponde?", "Pedir autorización a la junta, que es la mandante", "Mostrarlo, porque lo hizo el equipo", "Mostrarlo sin los nombres de la junta", "El trabajo es del mandante y confidencial hasta que él autorice compartirlo."),
    sc=[
        ("En Dibujo Técnico: ¿qué es un levantamiento?", "Medir y registrar cómo es algo que ya existe", "Sirve de base para dibujar el plano de lo existente."),
        ("¿Qué debe llevar cada medida de un croquis?", "Su unidad", "Sin unidad se pueden confundir metros y centímetros."),
        ("¿Desde dónde se mide en un trabajo escolar de ejemplo?", "Desde el piso, con una persona adulta responsable presente", "Medir en altura exige personal autorizado."),
    ],
    op=("Una escuela de ejemplo pide el levantamiento de una sala rectangular de 8 m de largo y 5 m de ancho, con una puerta de 1 m y una ventana de 3 m de ancho. Escribe lista de datos que anotarías en el croquis, calcula la superficie y el perímetro, indica qué medida falta si piden cortes y describe dos cuidados al medir.",
        "Datos: largo 8 m, ancho 5 m, puerta 1 m, ventana 3 m. Superficie: 8 × 5 = 40 m². Perímetro: 2 × (8 + 5) = 26 m. Falta la altura. Cuidados: medir desde el piso y con una persona adulta responsable; pedir autorización para fotografiar o compartir el croquis.",
        ["anota todas las medidas con unidad", "calcula superficie y perímetro", "indica la altura y dos cuidados"],
        ["croquis a mano alzada con medidas y los cálculos"],
        ["omitir las unidades", "confundir perímetro con superficie", "proponer medir en altura"],
        "Pregunta: «¿qué le falta al croquis para hacer un corte?». Si no responde, repasa para qué sirve el corte."),
    reinforce="Haz un croquis de tu pieza con el largo y el ancho en metros, y calcula su perímetro y su superficie.",
    extend="Explica con un ejemplo inventado por qué un levantamiento y un proyecto nuevo son encargos distintos.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (pieza de ejemplo, inventada). Una abrazadera es una pieza plana de 80 mm de largo, 30 mm de ancho y 5 mm de espesor, con 2 agujeros redondos de 10 mm de diámetro. "
     "El centro de cada agujero está a 15 mm del extremo más cercano, sobre la línea central. Conjunto de ejemplo: la abrazadera, un perno y una tuerca. "
     "Tipos de línea: continua gruesa para los contornos visibles; discontinua para los contornos ocultos; de trazo y punto para ejes y centros. En el cuaderno cuadriculado, 1 cuadrito representa 10 mm.")
build(
    O2, 2, F,
    use="Aprenderé a hacer un croquis de una pieza y de un conjunto, con los tipos de línea, las proporciones y las cotas.",
    prior=["Sé qué es un croquis.", "Sé qué es una cota.", "Sé calcular volumen de una caja (largo por ancho por alto)."],
    explain=[
        "El croquis de una pieza se hace a mano alzada, pero con orden y proporciones correctas. Primero se dibuja un rectángulo que encierra la pieza, con la proporción entre su largo y su ancho; en papel cuadriculado se cuentan cuadritos. Luego se dibujan los contornos, después los ejes y por último las cotas. Una pieza es un elemento de una sola parte; un conjunto está formado por varias piezas ensambladas.",
        "Cada tipo de línea tiene un significado según la norma de dibujo vigente. La línea continua gruesa marca los contornos que se ven; la línea discontinua marca contornos ocultos, que no se ven desde donde se mira; y la línea de trazo y punto marca ejes de simetría y centros. Las cotas se escriben con su unidad, una sola vez, y cerca de lo que miden.",
        "Para acotar un agujero se da su diámetro y la posición de su centro. La distancia entre dos centros se calcula restando de la medida total las distancias a los extremos. Un croquis no se mide con regla para obtener datos: sus datos son las cotas anotadas.",
    ],
    vocab=[("pieza", "elemento de una sola parte"), ("conjunto", "varias piezas ensambladas"), ("contorno oculto", "borde que no se ve desde la vista dibujada"), ("eje", "línea central o de simetría"), ("diámetro", "medida que cruza un círculo por su centro"), ("proporción", "relación entre dos medidas de un dibujo")],
    worked=[
        ("Contar cuadritos", "Un croquis de ejemplo representa una placa de 60 mm × 20 mm en papel cuadriculado donde 1 cuadrito son 10 mm. ¿Cuántos cuadritos de largo y de ancho usas?", ["Largo: 60 ÷ 10 = 6 cuadritos.", "Ancho: 20 ÷ 10 = 2 cuadritos."], "6 cuadritos de largo y 2 de ancho"),
        ("Elegir el tipo de línea", "En una pieza de ejemplo hay un agujero interior que no se ve desde arriba. ¿Con qué línea se dibuja?", ["Es un contorno que existe, pero oculto desde esa vista.", "Los contornos ocultos se dibujan con línea discontinua."], "Línea discontinua"),
    ],
    mistakes=[("Dibujar el agujero que no se ve con línea continua gruesa.", "Esa línea significa que el contorno es visible; el oculto se dibuja discontinuo.", "Usa discontinua para lo que queda oculto en esa vista."),
              ("Repetir la misma cota tres veces en el croquis «para que se entienda».", "Una medida repetida puede quedar contradictoria si se corrige solo una vez.", "Escribe cada cota una sola vez, donde mejor se lea.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es un conjunto?", "Varias piezas ensambladas", "Una sola pieza con muchos agujeros", "Una pieza dibujada a escala natural", "El conjunto reúne piezas; la abrazadera con perno y tuerca forma uno."),
        ("abc", "¿Qué tipo de línea se usa para los contornos visibles?", "Continua gruesa", "Discontinua", "De trazo y punto", "La continua gruesa marca lo visible; la discontinua lo oculto."),
        ("abc", "¿Qué tipo de línea se usa para un eje de simetría?", "De trazo y punto", "Continua gruesa", "Discontinua", "La línea de trazo y punto se reserva para ejes y centros."),
        ("=", "{F} Con 1 cuadrito igual a 10 mm, ¿cuántos cuadritos de largo usa la abrazadera?", "80//10", "El largo en milímetros se divide por lo que vale cada cuadrito.", " cuadritos"),
        ("=", "{F} ¿Cuántos cuadritos de ancho usa la abrazadera?", "30//10", "El ancho se divide por 10 mm por cuadrito.", " cuadritos"),
        ("abc", "{F} ¿Qué datos se anotan para acotar un agujero?", "Su diámetro y la posición de su centro", "Solo su color", "La escala del cuaderno", "Un agujero se acota con su diámetro y la posición del centro."),
        ("=", "{F} ¿Cuántos milímetros hay entre los centros de los dos agujeros?", "80-15-15", "A la medida total se restan las distancias del centro a cada extremo.", " mm"),
        ("abc", "{F} Si la abrazadera se mira desde arriba, ¿cómo se dibuja la tuerca que queda tapada por la pieza?", "Con línea discontinua, porque está oculta", "Con línea continua gruesa, como si se viera", "No se dibuja nunca", "Lo que no se ve en esa vista se dibuja discontinuo."),
        ("=", "{F} ¿Cuál es el volumen de la abrazadera sin descontar los agujeros (largo por ancho por espesor)?", "80*30*5", "El volumen de una pieza en forma de caja es largo por ancho por espesor.", " mm³"),
        ("abc", "{F} En un croquis de la abrazadera, el dibujante escribe «80» sin unidad. ¿Cuál es el problema?", "No se sabe si son milímetros, centímetros u otra unidad", "Que 80 es una cifra demasiado grande", "Que las cotas no se pueden escribir en croquis", "Una cota sin unidad es ambigua y puede producir una pieza de tamaño equivocado."),
        ("abc", "{F} Un croquis trae una cota repetida en dos lugares: 80 mm y 82 mm para el largo. ¿Qué corresponde?", "Consultar cuál es la medida correcta y dejar una sola cota", "Dejar las dos, así quien fabrique elige", "Promediar y escribir 81 mm", "Dos cotas distintas del mismo largo son un error; se aclara y se deja una."),
        ("=", "{F} Se dibuja un croquis de la abrazadera con cuadritos. ¿Cuántos cuadritos de largo mide la distancia entre los centros de los dos agujeros?", "(80-15-15)//10", "La distancia entre centros se divide por 10 mm por cuadrito.", " cuadritos"),
        ("abc", "{F} ¿Por qué no conviene medir con regla el croquis para saber el largo de la pieza?", "Porque el croquis es a mano alzada y sus datos son las cotas anotadas", "Porque la regla estropea el papel cuadriculado", "Porque la regla solo mide en centímetros", "El croquis no está a escala exacta; solo sus cotas son datos confiables."),
    ],
    ctx=("abc", "Un compañero dibuja el eje de un agujero con línea continua gruesa, igual que el contorno. ¿Qué le dices?", "Que el eje se dibuja con línea de trazo y punto para distinguirlo del contorno", "Que está bien, mientras se entienda", "Que borre el eje porque nunca se dibuja", "Cada tipo de línea tiene un significado, y mezclarlos confunde a quien lee."),
    sc=[
        ("En Dibujo Técnico: ¿para qué sirve la línea discontinua?", "Para dibujar contornos ocultos", "Muestra lo que existe, pero no se ve desde esa vista."),
        ("¿Qué diferencia hay entre pieza y conjunto?", "La pieza es de una sola parte y el conjunto reúne varias piezas", "El conjunto se forma al ensamblar piezas."),
        ("¿Qué se debe hacer con una cota?", "Escribirla una sola vez y con su unidad", "Así no hay contradicciones ni dudas."),
    ],
    op=("Una placa de ejemplo mide 100 mm de largo, 40 mm de ancho y 6 mm de espesor, con un agujero redondo de 12 mm de diámetro cuyo centro está a 20 mm de un extremo, sobre la línea central. En un cuaderno cuadriculado donde 1 cuadrito son 10 mm, calcula cuántos cuadritos usa de largo y de ancho, la distancia del centro al otro extremo y escribe qué tipo de línea usarías para el contorno, el eje del agujero y un agujero oculto.",
        "Largo: 100 ÷ 10 = 10 cuadritos; ancho: 40 ÷ 10 = 4 cuadritos. Distancia al otro extremo: 100 − 20 = 80 mm. Contorno: línea continua gruesa; eje: línea de trazo y punto; agujero oculto: línea discontinua.",
        ["calcula cuadritos y distancia", "asigna el tipo de línea correcto a los tres elementos", "acota con unidad y sin repetir"],
        ["croquis a mano alzada con cotas y las tres respuestas"],
        ["usar línea continua para lo oculto", "olvidar las unidades", "repetir cotas"],
        "Pregunta: «¿qué línea usarías si el agujero no se viera?». Si no responde, repasa los tipos de línea."),
    reinforce="Dibuja a mano alzada, en cuaderno cuadriculado, un rectángulo de 6 por 3 cuadritos con un agujero en el centro y acótalo.",
    extend="Explica con un ejemplo inventado cómo un croquis con cotas repetidas puede producir una pieza mal hecha.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (levantamiento de ejemplo, inventado) de una sala que parece rectangular. Lados medidos: norte 800 cm; sur 800 cm; este 600 cm; oeste 604 cm. "
     "Diagonales medidas: 1000 cm y 1006 cm. En un rectángulo, los lados opuestos son iguales y las dos diagonales también. "
     "Criterio de ejemplo del equipo: una diferencia de hasta 2 cm se acepta como error de medición; una mayor obliga a repetir la medición.")
build(
    O2, 3, F,
    use="Aprenderé a comprobar un levantamiento con medidas de control, a decidir cuándo repetir una medición y a registrar la información que lo respalda.",
    prior=["Sé qué es un perímetro y una superficie.", "Sé qué es un levantamiento.", "Sé comparar medidas."],
    explain=[
        "Un levantamiento no termina al anotar las medidas: se comprueba. Una medida de control es una medida extra que sirve para verificar las demás. En una sala que parece rectangular, los lados opuestos deben ser iguales y las dos diagonales también. Una diagonal es la línea que une dos esquinas opuestas. Si las diagonales difieren, la sala no tiene sus esquinas a escuadra, es decir, en ángulo recto.",
        "Todo instrumento y toda persona cometen pequeños errores. Por eso el equipo fija un criterio de aceptación, o tolerancia: una diferencia máxima aceptable. Si la diferencia es igual o menor, se acepta y se anota; si es mayor, se repite la medición antes de dibujar. Quien dibuja con medidas dudosas traspasa el error al plano.",
        "El registro debe permitir que otra persona repita el trabajo: qué se midió, con qué instrumento, quién midió, qué día y qué diferencia se halló. Si la sala no es rectangular, el plano debe dibujar su forma real, no una forma idealizada, y se informa al mandante.",
    ],
    vocab=[("medida de control", "medida extra que sirve para verificar otras"), ("diagonal", "línea que une dos esquinas opuestas"), ("a escuadra", "con esquinas en ángulo recto"), ("tolerancia", "diferencia máxima aceptable"), ("registro", "anotación de lo que se hizo y se halló")],
    worked=[
        ("Comparar lados opuestos", "En una pieza de ejemplo, los lados opuestos miden 300 cm y 303 cm. Con una tolerancia de 2 cm, ¿se acepta?", ["La diferencia es 303 − 300 = 3 cm.", "3 cm es mayor que 2 cm: no se acepta y se repite la medición."], "No se acepta: se repite la medición"),
        ("Comparar diagonales", "Las diagonales de una sala de ejemplo miden 500 cm y 501 cm. Con tolerancia de 2 cm, ¿qué se concluye?", ["La diferencia es 1 cm.", "1 cm es menor que 2 cm: es aceptable."], "Es aceptable: la sala se considera a escuadra"),
    ],
    mistakes=[("Dibujar un rectángulo perfecto aunque las diagonales no coinciden.", "El plano mostraría una forma que no es la real y los datos serían falsos.", "Si la diferencia excede la tolerancia, repite la medición y dibuja la forma real."),
              ("Aceptar cualquier diferencia diciendo que «las huinchas siempre fallan».", "Sin un criterio, no hay forma de saber si un error es normal o grave.", "Define y registra la tolerancia antes de medir.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es una diagonal?", "La línea que une dos esquinas opuestas", "El lado más largo de una figura", "La línea central de una pieza", "La diagonal cruza la figura entre esquinas opuestas."),
        ("abc", "¿Para qué sirve una medida de control?", "Para verificar otras medidas", "Para dibujar con mayor grosor", "Para cambiar la escala", "La medida de control no define la forma: la comprueba."),
        ("abc", "¿Qué es una tolerancia?", "La diferencia máxima aceptable", "La medida más grande de un plano", "La escala de la hoja", "La tolerancia es el límite de diferencia que se acepta."),
        ("=", "{F} ¿Cuántos centímetros de diferencia hay entre los lados este y oeste?", "604-600", "Se resta la medida menor a la mayor.", " cm"),
        ("=", "{F} ¿Cuántos centímetros de diferencia hay entre las dos diagonales?", "1006-1000", "Se restan las dos diagonales.", " cm"),
        ("abc", "{F} Con la tolerancia del equipo, ¿se acepta la diferencia de los lados este y oeste?", "No: 4 cm supera los 2 cm aceptados", "Sí: 4 cm es menor que 2 cm", "Sí: los lados norte y sur son iguales", "La diferencia de 4 cm es mayor que 2 cm, por eso hay que repetir la medición."),
        ("abc", "{F} ¿Qué conclusión se saca de las diagonales de la ficha?", "Difieren más que la tolerancia, así que la sala puede no estar a escuadra", "Son iguales, así que la sala es rectángulo perfecto", "No sirven, porque las diagonales no se miden", "6 cm es más que 2 cm: puede haber esquinas que no sean rectas."),
        ("=", "Otra sala de ejemplo: lados norte 750 cm y sur 752 cm. ¿Cuántos centímetros de diferencia hay?", "752-750", "Se resta el lado menor al mayor.", " cm"),
        ("ab", "En otra sala de ejemplo, dos lados opuestos difieren en 2 cm y la tolerancia del equipo es de 2 cm. ¿Qué corresponde?", "Aceptar la medida y anotarla en el registro", "Repetir la medición, porque hay diferencia", "La tolerancia dice hasta 2 cm; esa diferencia no la supera, por lo tanto se acepta."),
        ("abc", "{F} Después de repetir la medición, el lado oeste sigue en 604 cm. ¿Qué haces al dibujar?", "Dibujo la forma real y lo informo al mandante", "Dibujo un rectángulo perfecto de 600 cm", "No dibujo el lado oeste", "Si la medida se repite, se dibuja lo que existe y se informa."),
        ("abc", "{F} ¿Qué dato falta en un buen registro de la medición de la ficha?", "Quién midió, con qué instrumento y qué día", "El color de la huincha", "El nombre del mandante de otra obra", "El registro debe permitir repetir y verificar el trabajo."),
        ("=", "{F} Si las diagonales de la ficha se midieran con una huincha cuya lectura tiene un error máximo de 3 cm por medición, ¿cuántos centímetros de error máximo puede tener la diferencia entre las dos diagonales (suma de ambos errores)?", "3+3", "Los errores máximos de las dos mediciones se pueden sumar.", " cm"),
        ("abc", "{F} Con ese error de 3 cm por medición, la diferencia de 6 cm entre diagonales, ¿se puede explicar solo por el instrumento?", "Sí, porque 6 cm no supera el error máximo posible de 6 cm", "No: 6 cm es mayor que el error de 3 cm de una sola medición", "No se puede, porque las diagonales no se ven", "El error máximo combinado es 6 cm; la diferencia observada coincide con él y no lo supera."),
    ],
    ctx=("abc", "El equipo tiene prisa y el jefe dice: «dibujen la sala como rectángulo de 800 por 600 y listo». ¿Qué corresponde?", "Informar que hay diferencias sobre la tolerancia y proponer repetir la medición", "Dibujarla así sin avisar, para entregar a tiempo", "Cambiar las medidas del registro para que cuadren", "El plano debe mostrar lo real; si hay dudas se repite la medición y se informa."),
    sc=[
        ("En Dibujo Técnico: ¿qué es una medida de control?", "Una medida extra para verificar otras", "Por ejemplo, las diagonales de una sala."),
        ("¿Qué haces si la diferencia supera la tolerancia?", "Repito la medición antes de dibujar", "No se traspasa un error dudoso al plano."),
        ("¿Qué anotas en el registro de una medición?", "Qué se midió, con qué instrumento, quién y qué día", "Así otra persona puede repetir y verificar."),
    ],
    op=("Una sala de ejemplo se mide con estos datos: norte 500 cm; sur 503 cm; este 400 cm; oeste 400 cm; diagonales 640 cm y 641 cm. La tolerancia del equipo es 2 cm. Calcula las diferencias entre lados opuestos y entre diagonales, decide qué se acepta y qué se repite, y escribe tres datos del registro.",
        "Norte y sur: 503 − 500 = 3 cm, supera la tolerancia: se repite. Este y oeste: 0 cm, se acepta. Diagonales: 641 − 640 = 1 cm, se acepta. Registro: qué se midió (lados y diagonales), con qué instrumento y quién midió; día de la medición.",
        ["calcula las tres diferencias", "decide qué se acepta y qué se repite con la tolerancia", "escribe tres datos del registro"],
        ["hoja con las diferencias, decisiones y registro"],
        ["aceptar 3 cm con tolerancia 2 cm", "no repetir la medición", "olvidar el instrumento en el registro"],
        "Pregunta: «¿por qué se repite la medición del norte y sur?». Si no responde, repasa la regla de la tolerancia."),
    reinforce="Mide dos lados opuestos de una mesa de tu casa y compáralos con una tolerancia de 2 cm.",
    extend="Explica con un ejemplo inventado por qué las diagonales ayudan a saber si una sala está a escuadra.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (levantamiento de ejemplo, inventado). Sala rectangular de 800 cm de largo por 600 cm de ancho. Puerta de 90 cm de ancho en el muro sur, con su borde a 100 cm de la esquina oeste. "
     "Hoja A3 horizontal (420 mm de ancho por 297 mm de alto), margen de 10 mm por lado y un rótulo de 40 mm de alto en la parte inferior. "
     "Escalas habituales: 1:20, 1:50, 1:100.")
build(
    O2, 4, F,
    use="Aprenderé a pasar un croquis de medidas a un plano a escala: elegir la escala, calcular las medidas en el papel y ubicar los elementos.",
    prior=["Sé elegir una escala para que un dibujo quepa.", "Sé convertir cm a mm.", "Sé dividir por el número de la escala."],
    explain=[
        "Para pasar de un croquis a un plano a escala se siguen cuatro pasos: calcular el área útil de la hoja (hoja menos márgenes y menos rótulo); elegir la mayor escala habitual en que el dibujo cabe; calcular cada medida en el papel dividiendo la medida real por el número de la escala; y dibujar con regla y escuadra a partir de una esquina de referencia.",
        "Al convertir, se cuida la unidad. Si la medida real está en centímetros y el papel se mide en milímetros, se multiplica por 10 después de dividir por la escala: 800 cm a escala 1:50 son 16 cm en el papel, es decir, 160 mm. La puerta y las ventanas se ubican midiendo desde la esquina de referencia, con la misma escala.",
        "Antes de entregar se verifica el plano: la escala escrita en el rótulo, las cotas con unidad, los elementos del croquis y la coincidencia de las medidas con el registro de la medición. Si algo no cabe o no coincide, se corrige antes de entregar.",
    ],
    vocab=[("área útil", "parte de la hoja disponible para dibujar"), ("esquina de referencia", "esquina desde donde se miden las posiciones"), ("escala gráfica", "regla dibujada que muestra la escala"), ("verificación", "comprobación final antes de entregar")],
    worked=[
        ("Calcular el papel", "Un muro de ejemplo mide 500 cm y el plano está a escala 1:50. ¿Cuántos milímetros ocupa en el papel?", ["500 ÷ 50 = 10 cm en el papel.", "10 cm son 100 mm."], "100 mm"),
        ("Comprobar el área útil", "Una hoja A4 horizontal (297 mm por 210 mm), con margen de 10 mm por lado y rótulo de 30 mm abajo. ¿Cuál es el alto útil?", ["Alto: 210 − 10 − 10 = 190 mm.", "Se descuenta también el rótulo: 190 − 30 = 160 mm."], "160 mm"),
    ],
    mistakes=[("Descontar los márgenes pero olvidar el rótulo al calcular el alto útil.", "El dibujo podría tapar el rótulo o quedar cortado.", "Resta márgenes y rótulo al alto de la hoja."),
              ("Medir la posición de la puerta desde una esquina distinta a la del croquis.", "La puerta quedaría en el lugar equivocado del plano.", "Usa la misma esquina de referencia del croquis.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es la esquina de referencia?", "La esquina desde donde se miden las posiciones", "La esquina más lejana del rótulo", "La esquina donde se firma el plano", "La referencia común evita ubicar mal los elementos."),
        ("abc", "¿Cómo se obtiene una medida en el papel?", "Se divide la medida real por el número de la escala", "Se multiplica la medida real por el número de la escala", "Se suma el número de la escala a la medida real", "En papel el dibujo es más pequeño; por eso se divide."),
        ("abc", "¿Qué se verifica antes de entregar el plano?", "Escala, cotas con unidad y coincidencia con el registro de medición", "Solo el color del papel", "Solo que el rótulo esté centrado", "La verificación asegura que el plano sea fiel al levantamiento."),
        ("=", "{F} ¿Cuántos milímetros de ancho útil tiene la hoja con sus márgenes de 10 mm por lado?", "420-2*10", "Se resta el margen dos veces al ancho.", " mm"),
        ("=", "{F} ¿Cuántos milímetros de alto útil quedan si se descuentan los márgenes y el rótulo?", "297-2*10-40", "Se restan al alto los márgenes y el rótulo.", " mm"),
        ("=", "{F} A escala 1:50, ¿cuántos milímetros ocupa el largo de la sala en el papel?", "800//50*10", "Se divide por 50 para obtener centímetros y se multiplica por 10 para pasar a milímetros.", " mm"),
        ("=", "{F} A escala 1:50, ¿cuántos milímetros ocupa el ancho de la sala en el papel?", "600//50*10", "Se divide por 50 y se pasa a milímetros multiplicando por 10.", " mm"),
        ("abc", "{F} ¿Cabe el ancho de la sala a escala 1:20 en el alto útil?", "No: 600 ÷ 20 son 30 cm, es decir, 300 mm y superan el alto útil de 237 mm", "Sí: 600 ÷ 20 son 30 cm y caben en 420 mm", "Sí: la escala 1:20 siempre cabe", "El alto útil es 237 mm y a esa escala el ancho ocuparía 300 mm."),
        ("abc", "{F} ¿Qué escala se elige?", "1:50, la mayor habitual en que la sala cabe", "1:20, porque es la más grande", "1:100, porque es la más segura", "1:20 no cabe en el alto útil; 1:50 sí cabe y es la mayor que cabe."),
        ("=", "{F} A escala 1:50, la puerta mide 90 cm. ¿Cuántos milímetros ocupa en el papel?", "90*10//50", "Se pasa a milímetros y se divide por 50.", " mm"),
        ("=", "{F} A escala 1:50, ¿a cuántos milímetros de la esquina oeste empieza la puerta en el papel?", "100*10//50", "La posición de 100 cm se pasa a milímetros y se divide por 50.", " mm"),
        ("abc", "{F} Un compañero dibuja la puerta en el muro norte. ¿Qué error comete?", "No respeta la ubicación del levantamiento, que la sitúa en el muro sur", "Usa la escala equivocada", "Olvida el rótulo", "La ficha ubica la puerta en el muro sur; ponerla en el norte contradice el levantamiento."),
        ("abc", "{F} En el rótulo escribes «escala 1:20», pero dibujaste a 1:50. ¿Qué pasa?", "Quien lea el plano calculará medidas reales equivocadas", "Nada, porque la escala del rótulo no se usa", "El plano se verá más pequeño, pero será correcto", "Una escala mal escrita lleva a leer medidas reales equivocadas."),
    ],
    ctx=("abc", "Al terminar el plano descubres que el largo en el papel no coincide con tu cálculo. ¿Qué haces?", "Reviso el cálculo y la regla antes de entregar y corrijo lo que esté mal", "Entrego igual, porque es una diferencia pequeña", "Cambio la escala del rótulo para que coincida", "Se verifica antes de entregar; cambiar el rótulo oculta el error sin corregirlo."),
    sc=[
        ("¿Cómo se calcula una medida en el papel?", "Se divide la medida real por el número de la escala", "El dibujo es más pequeño que la realidad."),
        ("¿Qué se descuenta del alto de la hoja para el área útil?", "Los márgenes y el rótulo", "Ambos ocupan espacio de la hoja."),
        ("¿Por qué se usa una esquina de referencia?", "Para ubicar bien puertas y ventanas", "Todas las posiciones se miden desde el mismo punto."),
    ],
    op=("Una bodega de ejemplo mide 1000 cm de largo por 400 cm de ancho. La hoja es A3 horizontal (420 mm por 297 mm), con márgenes de 10 mm por lado y rótulo de 40 mm de alto. Calcula el ancho y el alto útiles, decide entre las escalas 1:20, 1:50 y 1:100 y calcula cuántos milímetros ocupan el largo y el ancho de la bodega con la escala elegida.",
        "Ancho útil: 420 − 20 = 400 mm. Alto útil: 297 − 20 − 40 = 237 mm. A 1:20 el largo sería 500 mm, no cabe. A 1:50: largo 200 mm y ancho 80 mm, caben. Se elige 1:50, la mayor que cabe.",
        ["calcula el área útil", "prueba las escalas y elige la mayor que cabe", "calcula las medidas en el papel con unidades"],
        ["hoja con cálculos y la elección"],
        ["no descontar el rótulo", "elegir 1:100 sin probar 1:50", "dividir por la escala sin pasar a milímetros"],
        "Pregunta: «¿por qué 1:20 no sirve?». Si no responde, pídele que calcule 1000 ÷ 20 en milímetros."),
    reinforce="Mide el largo de tu cuaderno y calcula cuánto ocuparía un muro de 4 m dibujado a escala 1:50.",
    extend="Explica con un ejemplo inventado qué problema produce que la escala del rótulo no coincida con el dibujo.",
)
