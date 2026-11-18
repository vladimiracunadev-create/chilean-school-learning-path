"""Muebles y Terminaciones en Madera (3.º y 4.º medio TP): OAE-05 (armar, encuadrar y prensar estructuras: riesgos, documentos, registros de escuadra y cálculo de insumos en papel) y OAE-06 (proteger, embellecer y terminar: vocabulario de acabados, riesgos de solventes, cálculo de rendimiento, control contra muestra y comparación de alternativas). Solo conceptos y planillas con datos de ejemplo."""
from __future__ import annotations

from tp_mutm_common import AVISO, EMER, build

O5 = "TP-MUTM-3y4-OAE-05"
O6 = "TP-MUTM-3y4-OAE-06"
TAIL = f"{EMER} {AVISO}"

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (sector de armado de ejemplo, inventado). En el taller ficticio «Carpintería Los Boldos» el sector de armado tiene 4 personas y 2 prensas. Hay 6 envases de adhesivo: 4 con etiqueta legible y pictogramas, y 2 sin etiqueta. "
     "Riesgos anotados: aplastamiento y atrapamiento en las prensas, vapores y contacto del adhesivo con la piel y los ojos, estructuras pesadas que se levantan entre varias personas y desorden en el piso que provoca tropiezos. "
     "Medidas anotadas: hoja de datos de seguridad disponible, ventilación, guantes y lentes indicados por esa hoja, solo personal autorizado en las prensas, pasillos libres y una etiqueta de «fuera de servicio» en la prensa 2, que tiene una falla.")
build(
    O5, 1, F,
    use="Aprenderé qué significan armar, encuadrar y prensar una estructura de mueble y qué riesgos tiene ese sector del taller, sin ningún procedimiento.",
    prior=["Sé qué es la jerarquía de controles.", "Sé restar y multiplicar.", "Sé qué es una hoja de datos de seguridad."],
    explain=[
        "Armar es unir las piezas de un mueble para formar su estructura. Encuadrar es lograr que la estructura quede a escuadra, es decir, con sus esquinas en ángulo recto, y comprobarlo. Prensar es mantener las piezas apretadas con una prensa mientras la unión se fija. Los adhesivos son productos químicos: su etiqueta trae pictogramas y su hoja de datos de seguridad (HDS) informa los peligros y la protección necesaria. Cómo se hace cada tarea lo enseña un instructor autorizado y está en las instrucciones del fabricante; este cuaderno no las contiene.",
        "Los riesgos del sector son el aplastamiento y el atrapamiento en las prensas, los vapores y el contacto de los adhesivos con la piel y los ojos, el levantamiento de estructuras pesadas y los tropiezos por desorden. Un envase sin etiqueta no se usa: se informa al responsable. Según la jerarquía de controles se organiza primero el espacio y la ventilación y solo al final se usa el EPP, que no reemplaza la autorización. Una prensa con falla se deja fuera de servicio con una etiqueta.",
        TAIL,
    ],
    vocab=[("armar", "unir las piezas de un mueble para formar su estructura"), ("encuadrar", "lograr y comprobar que la estructura quede con sus esquinas en ángulo recto"), ("prensar", "mantener las piezas apretadas con una prensa mientras la unión se fija"), ("aplastamiento", "riesgo de que una parte del cuerpo quede comprimida entre dos superficies"), ("adhesivo", "producto que une piezas entre sí"), ("fuera de servicio", "estado de un equipo con falla que no se debe usar")],
    worked=[
        ("Contar envases", "Llegan 9 envases de adhesivo y 6 tienen etiqueta. ¿Cuántos no la tienen?", ["Se restan los envases con etiqueta del total.", "9 menos 6 son 3."], "3 envases"),
        ("Reconocer el documento", "Una persona de ejemplo quiere saber qué protección necesita para un adhesivo. ¿Qué documento consulta?", ["La protección necesaria está en la hoja de datos de seguridad.", "La entrega el fabricante."], "La hoja de datos de seguridad"),
    ],
    mistakes=[("Usar una prensa con falla porque «solo es un rato».", "Una falla puede aplastar o atrapar a una persona.", "Se deja fuera de servicio con etiqueta y se avisa al responsable."),
              ("Creer que los guantes reemplazan la ventilación.", "El EPP es el último nivel de la jerarquía de controles.", "Se combinan ventilación, organización y EPP según la hoja de datos.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es encuadrar una estructura?", "Lograr y comprobar que sus esquinas queden en ángulo recto", "Unir las piezas con un adhesivo", "Apretar las piezas mientras la unión se fija", "Encuadrar es dejar la estructura a escuadra; unir y apretar son armar y prensar."),
        ("abc", "¿Qué es prensar en el armado de un mueble?", "Mantener las piezas apretadas mientras la unión se fija", "Medir el largo de las piezas", "Pintar la estructura ya armada", "Prensar es apretar; medir y pintar son otras tareas."),
        ("=", "{F} ¿Cuántos envases de adhesivo no tienen etiqueta?", "6-4", "Se restan los envases con etiqueta del total.", " envases"),
        ("abc", "{F} ¿Qué se hace con los envases sin etiqueta?", "No usarlos e informar al responsable hasta identificar el contenido", "Usarlos si el color parece igual a otros", "Mezclarlos con los etiquetados", "Sin etiqueta no se conoce el peligro, por eso no se usan ni se mezclan."),
        ("abc", "{F} ¿Dónde se consulta qué guantes y lentes corresponden?", "En la hoja de datos de seguridad", "En el plano del mueble", "En la lista de corte", "La hoja de datos indica la protección necesaria."),
        ("abc", "{F} ¿Qué equipo tiene la etiqueta de fuera de servicio?", "La prensa 2", "La prensa 1", "El sector de la bodega", "La ficha indica que la prensa 2 tiene una falla."),
        ("=", "{F} Cada una de las 4 personas recibe guantes y lentes. ¿Cuántas piezas de EPP se entregan?", "4*2", "Se multiplican las personas por las dos piezas de cada una.", " piezas"),
        ("abc", "{F} ¿Qué riesgo de la ficha se debe a dejar cosas en el piso?", "Los tropiezos", "El atrapamiento", "Los vapores", "Los objetos en el piso causan tropiezos; por eso se mantienen los pasillos libres."),
        ("abc", "{F} Una persona dice: «la prensa 2 funciona a medias, la uso solo hoy». ¿Qué corresponde?", "No usarla y avisar al responsable, porque está fuera de servicio", "Usarla con lentes puestos", "Quitar la etiqueta para trabajar más tranquila", "Una prensa con falla no se usa, aunque sea por poco tiempo."),
        ("ab", "{F} Un estudiante dice: «con guantes no hace falta ventilar». ¿Qué respuesta es correcta?", "No: el EPP es el último nivel y no reemplaza la ventilación", "Sí: los guantes eliminan todo el peligro", "La ficha incluye ventilación y guantes como medidas distintas."),
        ("abc", "{F} Una estudiante dice: «ya sé qué es prensar, puedo manejar una prensa». ¿Qué respuesta es correcta?", "No: manejar una prensa exige instructor autorizado y norma vigente", "Sí: conocer el término la habilita", "Sí, si usa lentes y guantes", "Saber un término no habilita ni el EPP reemplaza la autorización."),
        ("=", "{F} Una estructura pesada la levantan entre 3 de las 4 personas del sector. ¿Cuántas personas del sector no participan en ese levantamiento?", "4-3", "Se restan las personas que levantan del total del sector.", " persona"),
        ("abc", "{F} ¿Qué datos mínimos lleva el registro de los envases sin etiqueta?", "Cuántos son, dónde están, quién los detectó y la fecha", "Solo el color del envase", "Solo el precio del adhesivo", "Un registro útil dice cuántos, dónde, quién y cuándo."),
    ],
    ctx=("abc", "En un taller de ejemplo, la mano de una persona queda atrapada en una prensa. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Tratar de abrir la prensa sin saber hacerlo", "Esperar a que la persona se libere sola", "Se pide ayuda a quien está autorizado y a emergencias; no se improvisa."),
    sc=[
        ("En Muebles y Terminaciones en Madera: ¿qué significa armar?", "Unir las piezas de un mueble para formar su estructura", "Armar es formar la estructura uniendo las piezas."),
        ("¿Qué documento informa los peligros de un adhesivo?", "La hoja de datos de seguridad", "Esa hoja describe peligros y protección necesaria."),
        ("¿Qué se hace con una prensa con falla?", "Se deja fuera de servicio con etiqueta y se avisa", "Una prensa con falla puede causar un accidente."),
    ],
    op=("Sector de armado de ejemplo «Taller Quillay» (ficticio): 5 personas, 3 prensas y 10 envases de adhesivo, de los cuales 7 tienen etiqueta. Cada persona recibe guantes, lentes y mascarilla. Una prensa tiene falla. Escribe (a) cuántos envases no tienen etiqueta y qué haces con ellos, (b) cuántas piezas de EPP se entregan, (c) qué haces con la prensa con falla y (d) qué haces si alguien queda atrapado en una prensa.",
        "(a) 10 menos 7 son 3; no los uso e informo al responsable. (b) 5×3 son 15 piezas. (c) La dejo fuera de servicio con etiqueta y aviso. (d) No me acerco a la zona de riesgo, aviso a un adulto responsable y a emergencias.",
        ["calcula los envases sin etiqueta y no los usa", "calcula el EPP entregado", "deja la prensa fuera de servicio", "avisa sin acercarse al riesgo"],
        ["hoja con las cuatro respuestas"],
        ["usar envases sin etiqueta", "proponer abrir la prensa sin autorización", "decir que el EPP reemplaza la ventilación"],
        "Pregunta: «¿por qué una prensa con falla no se usa?». Si no responde, pídele que relea la explicación."),
    reinforce="Escribe la diferencia entre armar, encuadrar y prensar con una frase para cada término.",
    extend="Explica por qué el orden del piso es una medida de prevención en el sector de armado.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (documentos de armado de ejemplo, inventados). Producto ficticio «Adhesivo AD-ejemplo»: ficha técnica con consumo de ejemplo de 250 gramos por m² de superficie de unión; envases de 2.000 gramos; vigencia de ejemplo de 9 meses desde la fabricación; pictograma de la etiqueta: «inflamable». "
     "Plano de armado de la cómoda «C-9»: 6 uniones de esquina y 4 uniones de refuerzo. Registro de armado de ejemplo: número de estructura, fecha, responsable, lote del adhesivo y resultado del control de escuadra. "
     "Roles: armador autorizado, que ejecuta; supervisor, que revisa; controlador de calidad, que verifica la escuadra; prevencionista, que revisa los riesgos.")
build(
    O5, 2, F,
    use="Aprenderé qué documentos intervienen en el armado: ficha técnica, hoja de datos de seguridad, plano de armado y registro, y qué rol cumple cada persona.",
    prior=["Sé qué es armar, encuadrar y prensar.", "Sé multiplicar y dividir.", "Sé leer un registro."],
    explain=[
        "El plano de armado muestra qué piezas se unen y dónde; no explica cómo se hace la unión. La ficha técnica del adhesivo describe el producto: su consumo, su vigencia y cómo almacenarlo. La hoja de datos de seguridad informa los peligros y la protección necesaria. Son documentos distintos y se consultan para cosas distintas. El consumo de ejemplo, en gramos por m², permite calcular cuánto adhesivo se necesita en planilla; nunca se usa como guía para aplicarlo.",
        "El registro de armado deja constancia de cada estructura: número, fecha, responsable, lote del adhesivo y resultado del control de escuadra. Si más adelante aparece una falla, el registro permite rastrear qué lote y quién participó. Los roles se reparten así: el armador autorizado ejecuta, el supervisor revisa, el controlador de calidad verifica la escuadra y el prevencionista revisa los riesgos. Cada uno firma su parte. Un producto vencido no se usa y se informa.",
        TAIL,
    ],
    vocab=[("plano de armado", "documento que muestra qué piezas se unen y dónde"), ("consumo", "cantidad de producto que se necesita por unidad de superficie, dato de la ficha técnica"), ("lote", "conjunto de producto fabricado junto, identificado en el envase"), ("registro de armado", "documento que anota estructura, fecha, responsable, lote y resultado del control"), ("vigencia", "tiempo en que el producto sellado se puede usar"), ("supervisor", "persona que revisa el trabajo de otros")],
    worked=[
        ("Leer el consumo", "Un adhesivo de ejemplo consume 100 gramos por m² y se unen 8 m². ¿Cuántos gramos se necesitan?", ["Se multiplica el consumo por los m².", "100 por 8 son 800."], "800 gramos"),
        ("Revisar la vigencia", "Un adhesivo de ejemplo tiene vigencia de 6 meses y se fabricó hace 7. ¿Se puede usar?", ["Han pasado 7 meses y la vigencia es de 6.", "Se pasó de la vigencia."], "No, está vencido y se informa"),
    ],
    mistakes=[("Confundir la ficha técnica con la hoja de datos de seguridad.", "Una describe el producto y la otra cómo protegerse de él.", "Se usa la ficha para consumo y vigencia y la hoja para peligros y protección."),
              ("Armar sin anotar el lote del adhesivo.", "Sin el lote no se puede rastrear una falla posterior.", "El lote se anota en el registro de armado.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué muestra el plano de armado?", "Qué piezas se unen y dónde", "Cómo se aplica el adhesivo en cada unión", "Cuánto cuesta cada pieza", "El plano de armado indica piezas y uniones, no la forma de hacerlas."),
        ("abc", "¿Qué es el lote de un producto?", "El conjunto fabricado junto e identificado en el envase", "La cantidad de envases que compra un taller", "El nombre del armador", "El lote identifica la producción y permite rastrear fallas."),
        ("=", "{F} ¿Cuántas uniones se muestran en total en el plano de armado de la cómoda?", "6+4", "Se suman las uniones de esquina y las de refuerzo.", " uniones"),
        ("abc", "{F} ¿Qué documento informa el consumo de ejemplo del adhesivo?", "La ficha técnica", "La hoja de datos de seguridad", "El registro de armado", "El consumo es un dato del producto, que está en la ficha técnica."),
        ("abc", "{F} ¿Qué pictograma trae la etiqueta del adhesivo?", "Inflamable", "Corrosivo", "Explosivo", "La ficha señala el pictograma «inflamable»; los otros no aparecen."),
        ("=", "{F} Si se unen 12 m² de superficie, ¿cuántos gramos de adhesivo se calculan en planilla?", "12*250", "Se multiplica el consumo por los m² de superficie de unión.", " gramos"),
        ("=", "{F} ¿Cuántos envases de 2.000 gramos se necesitan para 3.000 gramos (redondeando hacia arriba)?", "(3000+1999)//2000", "Se divide 3.000 en 2.000 y se redondea hacia arriba porque sobra una parte.", " envases"),
        ("abc", "{F} ¿Qué rol verifica la escuadra de la estructura?", "El controlador de calidad", "El armador", "El prevencionista", "La verificación es función del controlador de calidad."),
        ("abc", "{F} ¿Qué datos lleva el registro de armado?", "Número de estructura, fecha, responsable, lote y resultado del control", "Solo la fecha", "Solo el nombre del supervisor", "Esos datos permiten rastrear cada estructura."),
        ("abc", "{F} Un envase tiene su vigencia vencida por 2 meses. ¿Qué corresponde?", "No usarlo e informar al responsable", "Usarlo si se ve igual", "Mezclarlo con uno vigente", "Un producto vencido no se usa, aunque se vea igual."),
        ("ab", "{F} Una persona dice: «el plano de armado me enseña cómo aplicar el adhesivo». ¿Qué respuesta es correcta?", "No: solo indica qué piezas se unen y dónde", "Sí: trae el procedimiento de aplicación", "La ficha dice que el plano muestra uniones."),
        ("abc", "{F} Una estudiante dice: «con el consumo de la ficha técnica ya sé aplicar el adhesivo». ¿Qué respuesta es correcta?", "No: la aplicación la enseña un instructor autorizado; el consumo sirve para calcular en planilla", "Sí: el consumo explica cómo aplicarlo", "Sí, si usa lentes y guantes", "El consumo es un dato de cálculo y no una guía de aplicación."),
        ("=", "{F} Si el pedido es de 5 cómodas «C-9», ¿cuántas uniones de esquina hay en total?", "5*6", "Se multiplican las cómodas por las uniones de esquina de cada una.", " uniones"),
    ],
    ctx=("abc", "En el taller de ejemplo, un adhesivo inflamable queda junto a un equipo que produce chispas. ¿Qué se hace según las reglas generales?", "Avisar al responsable para separarlos; si hay fuego, no acercarse y avisar a emergencias", "Dejarlo si no hay llamas visibles", "Taparlo con un trapo", "Un inflamable cerca de chispas es riesgo de incendio; se informa a quien corresponde."),
    sc=[
        ("¿Qué documento informa los peligros de un adhesivo?", "La hoja de datos de seguridad", "Esa hoja describe peligros y protección."),
        ("En Muebles y Terminaciones en Madera: ¿para qué sirve el lote anotado en el registro?", "Para rastrear una falla hasta su origen", "El lote identifica la producción del adhesivo."),
        ("¿Qué se hace con un adhesivo vencido?", "No se usa y se informa", "La vigencia indica hasta cuándo es utilizable."),
    ],
    op=("Documentos de ejemplo «Taller Ñire» (ficticio): adhesivo con consumo de ejemplo de 200 gramos por m², envases de 2.500 gramos y vigencia de 8 meses; se fabricó hace 9 meses. Plano de armado de una mesa: 8 uniones. Escribe (a) cuántos gramos se calculan para 10 m², (b) si el adhesivo se puede usar y por qué, (c) cuántas uniones hay en 4 mesas y (d) qué datos anotas en el registro de armado.",
        "(a) 10×200 son 2.000 gramos. (b) No: lleva 9 meses y la vigencia es de 8, está vencido. (c) 4×8 son 32 uniones. (d) Número de estructura, fecha, responsable, lote y resultado del control.",
        ["calcula los gramos", "detecta el producto vencido", "calcula las uniones", "enumera los datos del registro"],
        ["hoja con las cuatro respuestas"],
        ["confundir ficha técnica con hoja de datos", "usar el producto vencido", "olvidar el lote"],
        "Pregunta: «¿qué documento usaste para el consumo?». Si no responde, pídele que relea el vocabulario de consumo."),
    reinforce="Escribe la diferencia entre ficha técnica, hoja de datos de seguridad y plano de armado en tres frases.",
    extend="Explica cómo ayuda el registro de armado a encontrar el origen de una falla.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (registro de escuadra de ejemplo, inventado). Seis estructuras rectangulares de muebles. El controlador de calidad anota la medida de las dos diagonales de cada una, en milímetros: "
     "estructura E1: 1.000 y 1.002; E2: 1.000 y 1.005; E3: 1.001 y 1.001; E4: 998 y 1.003; E5: 1.002 y 1.000; E6: 1.000 y 1.003. "
     "Criterio de ejemplo: en una estructura rectangular a escuadra las dos diagonales son iguales; se acepta una diferencia de hasta 3 mm entre ellas. Lo que supera el criterio se separa y se registra.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un registro de escuadra: calcular la diferencia entre diagonales, aceptar o separar y calcular la tasa de rechazo.",
    prior=["Sé qué es encuadrar.", "Sé restar y calcular porcentajes sencillos.", "Sé qué es una tolerancia."],
    explain=[
        "Una forma de comprobar en papel que una estructura rectangular está a escuadra es comparar sus dos diagonales: si son iguales, las esquinas están en ángulo recto; si difieren, la estructura está deformada. En un taller el control lo hace una persona capacitada con instrumentos de medida, y anota los valores. Aquí solo se lee el registro y se aplica el criterio de ejemplo: la diferencia entre diagonales se calcula restando la menor de la mayor.",
        "Cada estructura queda aceptada o separada. Una diferencia igual al máximo permitido se acepta. Después se calcula la tasa de rechazo: las estructuras separadas, multiplicadas por 100 y divididas por el total medido. Si varias estructuras salen mal seguidas, no se corrigen una por una a ciegas: se informa al jefe de producción para revisar la causa, que puede estar en el corte, en el armado o en las instrucciones. Los valores de esta clase son inventados.",
        TAIL,
    ],
    vocab=[("diagonal", "línea que une dos esquinas opuestas de una estructura rectangular"), ("deformada", "con las esquinas fuera del ángulo recto"), ("diferencia entre diagonales", "resta de la diagonal mayor menos la menor"), ("criterio de ejemplo", "límite inventado para esta clase"), ("causa", "origen de un defecto repetido")],
    worked=[
        ("Diferencia entre diagonales", "Una estructura de ejemplo tiene diagonales de 800 mm y 806 mm. ¿Cuál es la diferencia?", ["Se resta la menor de la mayor.", "806 menos 800 son 6."], "6 mm"),
        ("Aplicar un criterio", "Con un criterio de ejemplo de diferencia máxima de 4 mm, la estructura anterior tiene 6 mm. ¿Se acepta?", ["Se compara 6 con el máximo de 4.", "6 supera el máximo."], "No, se separa y se registra"),
    ],
    mistakes=[("Restar al revés y obtener una diferencia negativa.", "La diferencia entre diagonales se calcula siempre de la mayor menos la menor.", "Se resta la menor de la mayor para obtener un número positivo."),
              ("Corregir estructuras una por una sin buscar la causa de varias fallas.", "Si el problema se repite, el origen está en otra etapa.", "Se informa al jefe de producción para revisar la causa.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es una diagonal de una estructura rectangular?", "La línea que une dos esquinas opuestas", "El borde más largo de la estructura", "La unión entre dos piezas", "La diagonal cruza la estructura de una esquina a la opuesta."),
        ("abc", "¿Qué indica que las dos diagonales sean iguales?", "Que las esquinas están en ángulo recto", "Que la estructura es pesada", "Que el adhesivo es nuevo", "Con diagonales iguales, el rectángulo está a escuadra."),
        ("=", "{F} ¿Cuántos mm de diferencia hay entre las diagonales de E2?", "1005-1000", "Se resta la diagonal menor de la mayor.", " mm"),
        ("=", "{F} ¿Cuántos mm de diferencia hay entre las diagonales de E4?", "1003-998", "Se resta la diagonal menor de la mayor.", " mm"),
        ("=", "{F} ¿Cuántos mm de diferencia hay entre las diagonales de E6?", "1003-1000", "Se resta la diagonal menor de la mayor.", " mm"),
        ("abc", "{F} ¿Qué estructura tiene las diagonales exactamente iguales?", "E3", "E1", "E5", "E3 mide 1.001 mm en ambas diagonales."),
        ("abc", "{F} ¿Qué se hace con E6, cuya diferencia es justo la máxima permitida?", "Se acepta, porque el criterio incluye el máximo", "Se separa por estar en el límite", "Se vuelve a medir hasta que dé menos", "El criterio acepta hasta 3 mm, incluyéndolos."),
        ("=", "{F} ¿Cuántas estructuras se separan según el criterio?", "1+1", "Se suman las dos estructuras que superan el máximo.", " estructuras"),
        ("=", "{F} ¿Cuántas estructuras se aceptan?", "6-2", "Se restan las separadas del total de seis.", " estructuras"),
        ("=", "{F} ¿Cuál es la tasa de rechazo en porcentaje, tomando la parte entera (2 estructuras separadas de 6 medidas)?", "2*100//6", "Se multiplican las separadas por 100 y se divide por el total, tomando la parte entera.", " %"),
        ("ab", "{F} Un compañero dice: «E5 tiene 1.002 y 1.000, que se parece a E1, así que está mal». ¿Qué respuesta es correcta?", "No: su diferencia es de 2 mm, dentro del criterio de 3 mm", "Sí: toda diferencia distinta de cero se rechaza", "La ficha admite hasta 3 mm de diferencia."),
        ("abc", "{F} Una estudiante dice: «ya sé leer el registro de escuadra, puedo corregir estructuras con las herramientas». ¿Qué respuesta es correcta?", "No: corregir exige instructor autorizado y norma vigente; leer no habilita", "Sí: leer el registro habilita para corregir", "Sí, si usa EPP completos", "Leer un registro no habilita para trabajar con herramientas."),
        ("abc", "{F} Si cinco estructuras seguidas saliesen con 5 mm de diferencia, ¿qué corresponde?", "Informar al jefe de producción para revisar la causa", "Corregirlas una por una sin avisar", "Aceptarlas por ser parejas entre sí", "Un defecto repetido tiene una causa que debe revisarse."),
    ],
    ctx=("abc", "En el taller de ejemplo, al mover una estructura pesada que parece fuera de escuadra, una persona siente un tirón fuerte en la espalda y no puede enderezarse. ¿Qué se hace según las reglas generales?", "No seguir levantando, avisar a un adulto responsable y a emergencias", "Seguir trabajando para terminar el turno", "Pedirle que cargue algo más liviano sin avisar", "Una lesión se informa a quien corresponde y se pide ayuda de emergencias."),
    sc=[
        ("¿Cómo se calcula la diferencia entre diagonales?", "Restando la diagonal menor de la mayor", "Así se obtiene un valor positivo para comparar."),
        ("En Muebles y Terminaciones en Madera: ¿qué indica una gran diferencia entre diagonales?", "Que la estructura está deformada", "Las diagonales distintas muestran esquinas fuera de ángulo recto."),
        ("¿Qué se hace si varias estructuras salen mal seguidas?", "Se informa para revisar la causa", "Un defecto repetido tiene un origen que hay que encontrar."),
    ],
    op=("Registro de ejemplo «Taller Peumo» (ficticio): criterio de ejemplo, diferencia máxima entre diagonales de 2 mm. Diagonales en mm: F1: 900 y 901; F2: 900 y 904; F3: 899 y 901; F4: 902 y 900; F5: 900 y 903. Escribe (a) la diferencia de cada estructura, (b) cuáles se separan, (c) cuántas se aceptan y (d) qué haces si las cinco estructuras salen mal otro día.",
        "(a) F1: 1; F2: 4; F3: 2; F4: 2; F5: 3. (b) Se separan F2 y F5. (c) Se aceptan 3. (d) Informo al jefe de producción para revisar la causa.",
        ["calcula las diferencias", "identifica las separadas", "cuenta las aceptadas", "propone informar para revisar la causa"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "separar las que están justo en el límite", "corregir sin informar"],
        "Pregunta: «¿por qué F3 se acepta con 2 mm?». Si no responde, pídele que relea el criterio."),
    reinforce="Calcula la diferencia entre diagonales de 750 mm y 757 mm y di si cumple un máximo de ejemplo de 5 mm.",
    extend="Explica por qué un defecto que se repite no se corrige estructura por estructura.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (planificación de armado de ejemplo, inventada). Pedido de 20 estructuras «K-3». Cada estructura necesita 2 m² de superficie de unión (dato de ejemplo). "
     "Consumo de ejemplo del adhesivo: 250 gramos por m²; envases de 2.000 gramos. El taller ficticio tiene 2 prensas y en cada tanda una prensa recibe 3 estructuras. "
     "Si hay una prensa fuera de servicio, queda 1 prensa disponible.")
build(
    O5, 4, F,
    use="Aprenderé a calcular en papel el adhesivo necesario y el número de tandas de prensa para un pedido, y a ver cómo una prensa fuera de servicio cambia la planificación.",
    prior=["Sé multiplicar y dividir con resto.", "Sé qué es el consumo.", "Sé qué es una tanda."],
    explain=[
        "Planificar el armado de un pedido en papel requiere dos cálculos. El primero es el insumo: se multiplica la superficie de unión por el consumo de la ficha técnica y se pasa a envases dividiendo por el contenido de cada uno, redondeando hacia arriba. El segundo es la capacidad de las prensas: una tanda es un grupo de estructuras que se prensa a la vez; dividiendo las estructuras por las que caben en una tanda, también hacia arriba, se obtiene el número de tandas.",
        "Si hay varias prensas disponibles, las tandas se reparten entre ellas; cuando una queda fuera de servicio, la capacidad baja y el plazo se alarga. Esa diferencia se informa con anticipación y no se resuelve usando una prensa con falla ni acelerando el trabajo. Todos los números de esta clase son de ejemplo y sirven para calcular en planilla; el uso real del adhesivo y de las prensas lo enseña un instructor autorizado y lo fija el fabricante.",
        TAIL,
    ],
    vocab=[("tanda", "grupo de estructuras que se prensa a la vez"), ("capacidad", "cantidad de trabajo que se puede hacer en un tiempo con los equipos disponibles"), ("superficie de unión", "área de contacto entre piezas que se unen, en m²"), ("insumo", "material que se consume al fabricar, como el adhesivo"), ("planificación", "cálculo anticipado de cantidades y turnos")],
    worked=[
        ("Contar tandas", "Un pedido de ejemplo tiene 14 estructuras y cada tanda recibe 4. ¿Cuántas tandas hay?", ["14 dividido en 4 da 3 y sobran 2.", "Las 2 restantes necesitan otra tanda: se redondea hacia arriba."], "4 tandas"),
        ("Envases necesarios", "Un trabajo de ejemplo necesita 5.000 gramos y cada envase trae 2.000. ¿Cuántos envases se compran?", ["5.000 dividido en 2.000 da 2 y sobran 1.000.", "Se compra un envase más."], "3 envases"),
    ],
    mistakes=[("Redondear hacia abajo el número de envases.", "Faltaría adhesivo para terminar.", "Si la división deja resto, se compra un envase más."),
              ("Usar la prensa fuera de servicio para cumplir el plazo.", "Una prensa con falla puede causar un accidente.", "Se informa que la capacidad bajó y se renegocia el plazo.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es una tanda de prensado?", "Un grupo de estructuras que se prensa a la vez", "Un tipo de adhesivo", "La suma de los envases de un lote", "La tanda agrupa estructuras que se prensan juntas."),
        ("abc", "¿Qué pasa con la capacidad de armado si una prensa queda fuera de servicio?", "Baja y el plazo puede alargarse", "Sube porque quedan menos prensas", "No cambia", "Con menos prensas disponibles se prensa menos por vez."),
        ("=", "{F} ¿Cuántos m² de superficie de unión necesita todo el pedido?", "20*2", "Se multiplican las estructuras por los m² de cada una.", " m²"),
        ("=", "{F} ¿Cuántos gramos de adhesivo se calculan para 40 m²?", "40*250", "Se multiplica el consumo por los m² de unión.", " gramos"),
        ("=", "{F} ¿Cuántos envases de 2.000 gramos se necesitan para 10.000 gramos?", "10000//2000", "Se divide el total entre el contenido de cada envase.", " envases"),
        ("=", "{F} ¿Cuántas estructuras caben en una tanda de las 2 prensas juntas?", "2*3", "Se multiplican las prensas por las estructuras de cada una.", " estructuras"),
        ("=", "{F} ¿Cuántas tandas de las dos prensas juntas (6 estructuras por tanda) se necesitan para 20 estructuras, redondeando hacia arriba?", "(20+5)//6", "Se divide 20 en 6 y se redondea hacia arriba.", " tandas"),
        ("=", "{F} Con una sola prensa disponible (3 estructuras por tanda), ¿cuántas tandas se necesitan para 20 estructuras, redondeando hacia arriba?", "(20+2)//3", "Se divide 20 en 3 y se redondea hacia arriba.", " tandas"),
        ("abc", "{F} ¿Qué conviene hacer si una prensa está fuera de servicio y el plazo es justo?", "Informar la menor capacidad y renegociar el plazo", "Usar la prensa con falla para ir más rápido", "Saltarse el control de escuadra", "Se informa y se renegocia, sin riesgos."),
        ("abc", "{F} Una persona compra solo 4 envases de 2.000 gramos para el pedido de la ficha. ¿Alcanza?", "No: 4 envases dan 8.000 gramos y faltan 2.000", "Sí: 4 envases son más que 10.000", "Sí, porque sobra", "Con 4 envases hay 8.000 gramos, menos que los 10.000 necesarios."),
        ("ab", "{F} Un estudiante dice: «el consumo de la ficha me enseña a aplicar el adhesivo». ¿Qué respuesta es correcta?", "No: solo permite calcular cantidades en planilla", "Sí: es una guía de aplicación", "La ficha rotula el consumo como dato de ejemplo."),
        ("abc", "{F} Otra estudiante dice: «ya planifico las tandas, puedo manejar las prensas». ¿Qué respuesta es correcta?", "No: manejar prensas exige instructor autorizado y norma vigente", "Sí: planificar habilita para manejarlas", "Sí, si hay supervisor", "Planificar es un cálculo en papel y no habilita para operar equipos."),
        ("=", "{F} Si el pedido aumentara a 24 estructuras y se prensan de 6 en 6 con las dos prensas, ¿cuántas tandas son?", "24//6", "Se divide el pedido entre las estructuras por tanda.", " tandas"),
    ],
    ctx=("abc", "En una planificación de ejemplo, el jefe pide terminar antes y sugiere cargar la prensa con más estructuras de las que indica el fabricante. ¿Qué respuesta es correcta?", "No: se respetan las indicaciones del fabricante y se renegocia el plazo", "Sí: más carga es más rápido y seguro", "Sí, si todos usan lentes", "Exceder la capacidad indicada es un riesgo de accidente; se informa."),
    sc=[
        ("¿Qué se hace con el resto de una división de envases?", "Se compra un envase más", "Un envase incompleto igual se compra entero."),
        ("En Muebles y Terminaciones en Madera: ¿qué cálculo da el número de tandas?", "Estructuras dividido en estructuras por tanda, hacia arriba", "Las estructuras restantes necesitan una tanda más."),
        ("¿Qué cambia si una prensa está fuera de servicio?", "La capacidad baja y el plazo se alarga", "Con menos prensas hay menos estructuras por cada tanda."),
    ],
    op=("Planificación de ejemplo «Taller Quillay» (ficticio): 18 estructuras; 3 m² de unión cada una; consumo de ejemplo de 200 gramos por m²; envases de 3.000 gramos; 2 prensas, cada una con 4 estructuras por tanda. Escribe (a) los m² de unión, (b) los gramos de adhesivo y los envases necesarios, (c) las tandas con ambas prensas y (d) las tandas si solo hay una prensa.",
        "(a) 18×3 son 54 m². (b) 54×200 son 10.800 gramos; 10.800÷3.000 da 3 y sobran 1.800, así que 4 envases. (c) Con las dos prensas caben 8 por tanda; 18÷8 da 2 y sobran 2, así que 3 tandas. (d) Con una prensa caben 4; 18÷4 da 4 y sobran 2, así que 5 tandas.",
        ["calcula los m²", "calcula gramos y envases con redondeo", "calcula las tandas con dos prensas", "calcula las tandas con una prensa"],
        ["hoja con las cuatro respuestas"],
        ["redondear hacia abajo", "multiplicar por prensas en vez de por estructuras", "olvidar la superficie por estructura"],
        "Pregunta: «¿por qué se redondea hacia arriba?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula cuántas tandas de 5 estructuras se necesitan para 32 estructuras.",
    extend="Explica por qué respetar la capacidad indicada por el fabricante es una medida de seguridad y no solo de calidad.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 5 (taller de terminaciones de ejemplo, inventado). El taller ficticio «Carpintería Los Boldos» tiene una zona de terminaciones con 3 personas. Se reciben 12 envases de productos de acabado: 9 con etiqueta legible y pictogramas, y 3 sin etiqueta. "
     "Riesgos anotados: vapores de solventes, productos inflamables cerca de fuentes de calor, contacto con piel y ojos, polvo fino de madera y trapos con restos de producto que pueden incendiarse. "
     "Medidas anotadas: hoja de datos de seguridad disponible, ventilación, productos inflamables guardados lejos del calor, mascarilla indicada por la hoja, guantes y lentes, retiro programado de residuos y personal capacitado.")
build(
    O6, 1, F,
    use="Aprenderé qué son los acabados de un mueble y qué riesgos tienen los productos de terminación, sin ningún procedimiento de aplicación.",
    prior=["Sé qué es una hoja de datos de seguridad.", "Sé restar y multiplicar.", "Sé qué es la jerarquía de controles."],
    explain=[
        "Las terminaciones protegen la madera, mejoran su aspecto y le dan el acabado que pidió el diseño. Se usan productos como barnices, lacas, tintes y selladores, que son químicos: traen pictogramas en la etiqueta y una hoja de datos de seguridad (HDS) con peligros, protección y qué hacer ante un derrame o contacto. Los solventes liberan vapores que pueden irritar, intoxicar o inflamarse. Cómo se aplican esos productos lo enseña un instructor autorizado y está en las instrucciones del fabricante; este cuaderno no las contiene.",
        "Los riesgos principales son los vapores, el fuego, el contacto con piel y ojos, el polvo fino y los residuos: un trapo con restos de producto puede incendiarse y se retira según la HDS. Un envase sin etiqueta no se usa. Según la jerarquía de controles se prefieren productos menos peligrosos, ventilación y orden, y el EPP respiratorio y de protección se usa al final y según lo que indique la HDS. Ante una intoxicación o un incendio, nadie entra a rescatar sin autorización.",
        TAIL,
    ],
    vocab=[("terminación", "etapa que protege la madera y define el aspecto final del mueble"), ("solvente", "líquido que disuelve otros productos y libera vapores"), ("inflamable", "que se incendia con facilidad"), ("pictograma", "símbolo de la etiqueta que advierte un peligro"), ("residuo", "material descartado, como trapos con restos de producto"), ("ventilación", "renovación del aire de un recinto")],
    worked=[
        ("Contar envases", "Llegan 15 envases de producto y 11 tienen etiqueta. ¿Cuántos no la tienen?", ["Se restan los envases con etiqueta del total.", "15 menos 11 son 4."], "4 envases"),
        ("Reconocer el documento", "Una persona de ejemplo quiere saber qué mascarilla usar con un producto. ¿Qué documento consulta?", ["La protección necesaria figura en la hoja de datos de seguridad.", "La entrega el fabricante."], "La hoja de datos de seguridad"),
    ],
    mistakes=[("Guardar un trapo con restos de producto en un cajón cerrado.", "Puede incendiarse y nadie lo ve.", "Se retira según la hoja de datos y el plan de residuos."),
              ("Usar mascarilla como único control de los vapores.", "El EPP es el último nivel de la jerarquía de controles.", "Se combina con ventilación y productos menos peligrosos.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿para qué sirve una terminación en un mueble?", "Para proteger la madera y definir su aspecto final", "Para unir las piezas de la estructura", "Para medir las piezas con precisión", "Las terminaciones protegen y dan el acabado; unir y medir son otras etapas."),
        ("abc", "¿Qué es un solvente?", "Un líquido que disuelve otros productos y libera vapores", "Un tablero para chapas", "Un tipo de tela para tapizado", "El solvente es un líquido químico y sus vapores son un riesgo."),
        ("=", "{F} ¿Cuántos envases no tienen etiqueta?", "12-9", "Se restan los envases con etiqueta del total recibido.", " envases"),
        ("abc", "{F} ¿Qué se hace con los envases sin etiqueta?", "No usarlos e informar al responsable hasta identificar su contenido", "Usarlos si el olor se parece al de otros", "Mezclarlos con productos etiquetados", "El olor no identifica un producto; sin etiqueta no se usa."),
        ("abc", "{F} ¿Dónde se consulta qué mascarilla corresponde?", "En la hoja de datos de seguridad", "En el plano del mueble", "En la lista de corte", "La HDS indica la protección necesaria."),
        ("=", "{F} Cada una de las 3 personas recibe mascarilla, guantes y lentes. ¿Cuántas piezas de EPP se entregan?", "3*3", "Se multiplican las personas por las tres piezas de cada una.", " piezas"),
        ("abc", "{F} ¿Qué riesgo de la ficha se debe a los trapos con restos de producto?", "Que pueden incendiarse", "Que producen ruido", "Que atrapan la ropa", "La ficha advierte que esos trapos pueden incendiarse."),
        ("abc", "{F} ¿Qué medida de la ficha reduce la acumulación de vapores?", "La ventilación", "La zona demarcada de aprendices", "La etiqueta de fuera de servicio", "Ventilar renueva el aire y reduce los vapores."),
        ("abc", "{F} Se ve un envase inflamable junto a una fuente de calor. ¿Qué corresponde?", "Avisar al responsable para separarlo de la fuente de calor", "Dejarlo si no hay llamas", "Taparlo con un trapo", "Un inflamable cerca del calor es riesgo de incendio; se informa."),
        ("ab", "{F} Una persona dice: «con la mascarilla no hace falta ventilar». ¿Qué respuesta es correcta?", "No: el EPP es el último nivel y no reemplaza la ventilación", "Sí: la mascarilla elimina todo el peligro", "La ficha incluye ventilación y mascarilla como medidas distintas."),
        ("abc", "{F} Una estudiante dice: «sé qué es una terminación, puedo aplicar un barniz». ¿Qué respuesta es correcta?", "No: la aplicación exige instructor autorizado y norma vigente", "Sí: conocer el término la habilita", "Sí, si usa lentes y guantes", "Saber un término no habilita ni el EPP reemplaza la autorización."),
        ("=", "{F} Si cada una de las 9 etiquetas legibles tiene 2 pictogramas (dato de ejemplo), ¿cuántos pictogramas hay en total?", "9*2", "Se multiplican los envases etiquetados por los pictogramas de cada uno.", " pictogramas"),
        ("abc", "{F} El prevencionista pide registrar los envases sin etiqueta. ¿Qué datos mínimos lleva el registro?", "Cuántos son, dónde están, quién los detectó y la fecha", "Solo el nombre del proveedor", "Solo su precio", "Un registro útil dice cuántos, dónde, quién y cuándo."),
    ],
    ctx=("abc", "En un taller de ejemplo, una persona respira vapores de un solvente y se desploma dentro de un cuarto cerrado. ¿Qué se hace según las reglas generales?", "No entrar a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar de inmediato sin protección a sacarla", "Esperar a ver si se recupera sola", "Entrar sin protección puede intoxicar también a quien ayuda; se avisa a quien corresponde y a emergencias."),
    sc=[
        ("En Muebles y Terminaciones en Madera: ¿qué es una terminación?", "La etapa que protege la madera y define el aspecto final", "Protege y da el aspecto final del mueble."),
        ("¿Qué se hace con un trapo con restos de producto?", "Se retira según la hoja de datos y el plan de residuos", "Puede incendiarse si se guarda sin control."),
        ("¿Qué medida va antes que el EPP en la jerarquía de controles?", "La ventilación y el uso de productos menos peligrosos", "El EPP es el último nivel."),
    ],
    op=("Zona de terminaciones de ejemplo «Taller Ñire» (ficticio): 4 personas y 14 envases de productos, de los cuales 10 tienen etiqueta. Cada persona recibe mascarilla y lentes. Riesgos: vapores, inflamables y trapos con restos de producto. Escribe (a) cuántos envases no tienen etiqueta y qué haces con ellos, (b) cuántas piezas de EPP se entregan, (c) qué haces con los trapos con restos de producto y (d) qué haces si alguien se intoxica con vapores.",
        "(a) 14 menos 10 son 4; no los uso e informo al responsable. (b) 4×2 son 8 piezas. (c) Los retiro según la hoja de datos y el plan de residuos. (d) No entro a la zona de riesgo, aviso a un adulto responsable y a emergencias.",
        ["calcula los envases sin etiqueta y no los usa", "calcula el EPP entregado", "retira los trapos según el plan", "avisa sin acercarse al riesgo"],
        ["hoja con las cuatro respuestas"],
        ["usar envases sin etiqueta", "guardar los trapos en un cajón cerrado", "entrar a rescatar sin protección"],
        "Pregunta: «¿por qué los trapos con restos pueden ser un riesgo?». Si no responde, pídele que relea la explicación."),
    reinforce="Escribe la diferencia entre ventilación y mascarilla dentro de la jerarquía de controles.",
    extend="Explica por qué se prefiere sustituir un producto muy peligroso por otro menos peligroso cuando es posible.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 6 (cuadro de acabados de ejemplo, inventado). Mueble ficticio «Aparador A-5»: tapa, acabado barnizado transparente; cuerpo, acabado lacado de color blanco; asiento de un banquito acompañante, acabado tapizado en tela; "
     "puertas con un adorno tallado. Documentos: la ficha técnica del producto de acabado (rendimiento, vigencia, almacenamiento), la hoja de datos de seguridad (peligros y protección) y una muestra aprobada, que es una pieza pequeña de referencia firmada por el cliente.")
build(
    O6, 2, F,
    use="Aprenderé el vocabulario de los acabados de muebles y qué documentos se usan para especificar y controlar la terminación.",
    prior=["Sé qué es una terminación.", "Sé qué es la ficha técnica y la hoja de datos de seguridad.", "Sé leer un cuadro de datos."],
    explain=[
        "Los acabados tienen nombres propios. El tallado es una decoración que se obtiene quitando material de la madera. La impregnación superficial es un tratamiento con un producto que penetra en la superficie para protegerla. El sellado forma una capa que cierra los poros. El pulido deja la superficie lisa o con brillo. El teñido cambia el color con un tinte. El barnizado es una capa protectora transparente y el lacado, una capa de laca, que puede ser de color. El tapizado es revestir con tela y relleno. Aquí solo se aprenden los nombres y los documentos, no cómo se hacen.",
        "Para especificar un acabado se usa el cuadro de acabados, que dice qué acabado lleva cada parte del mueble. La ficha técnica dice cuánto rinde el producto y cuánto dura; la hoja de datos de seguridad, cómo protegerse. La muestra aprobada es una pieza de referencia firmada por el cliente: el mueble terminado se compara con ella. Quien decide si el acabado cumple es el controlador de calidad, no quien lo aplicó.",
        TAIL,
    ],
    vocab=[("tallado", "decoración que se obtiene quitando material de la madera"), ("impregnación superficial", "tratamiento con un producto que penetra en la superficie para protegerla"), ("sellado", "capa que cierra los poros de la madera"), ("barnizado", "capa protectora transparente sobre la madera"), ("lacado", "capa de laca, que puede ser de color"), ("tapizado", "revestimiento con tela y relleno"), ("muestra aprobada", "pieza de referencia firmada por el cliente")],
    worked=[
        ("Reconocer el acabado", "Una persona de ejemplo quiere revestir un asiento con tela y relleno. ¿Cómo se llama ese acabado?", ["Revestir con tela y relleno es tapizar.", "El resultado es un asiento tapizado."], "Tapizado"),
        ("Leer el cuadro", "Un cuadro de ejemplo indica: puerta, lacado azul; borde, barnizado. ¿Cuántas partes del mueble aparecen?", ["Se cuentan las filas del cuadro.", "Hay dos: puerta y borde."], "2 partes"),
    ],
    mistakes=[("Confundir barnizado con lacado.", "El barniz es una capa transparente y la laca puede ser de color.", "Se lee el nombre del acabado en el cuadro y se consulta la ficha técnica."),
              ("Controlar el acabado comparándolo con el recuerdo del color.", "La memoria cambia; la referencia es la muestra aprobada.", "Se compara con la muestra aprobada firmada por el cliente.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es el tallado?", "Una decoración que se obtiene quitando material de la madera", "Una capa de color sobre la madera", "El revestimiento de un asiento con tela", "El tallado quita material; el color y la tela son otros acabados."),
        ("abc", "¿Qué es el tapizado?", "El revestimiento de un asiento con tela y relleno", "Una capa transparente protectora", "Un tratamiento que cierra los poros", "El tapizado reviste con tela; la capa transparente es el barnizado."),
        ("abc", "¿Qué es el sellado?", "Una capa que cierra los poros de la madera", "Una decoración tallada", "Un cambio de color con un tinte", "El sellado cierra poros; el tinte es otro tratamiento."),
        ("abc", "{F} ¿Qué acabado lleva la tapa?", "Barnizado transparente", "Lacado blanco", "Tapizado en tela", "La ficha indica que la tapa lleva barnizado transparente."),
        ("abc", "{F} ¿Qué acabado lleva el cuerpo del aparador?", "Lacado de color blanco", "Barnizado transparente", "Tallado", "El cuerpo se especifica con lacado blanco."),
        ("abc", "{F} ¿Qué parte del mueble lleva un adorno tallado?", "Las puertas", "La tapa", "El cuerpo", "La ficha indica que las puertas llevan un adorno tallado."),
        ("abc", "{F} ¿Qué documento dice cuánto rinde el producto de acabado?", "La ficha técnica", "La hoja de datos de seguridad", "La muestra aprobada", "El rendimiento es un dato de la ficha técnica."),
        ("abc", "{F} ¿Qué documento dice qué protección usar con el producto?", "La hoja de datos de seguridad", "La ficha técnica", "El cuadro de acabados", "La protección necesaria se informa en la HDS."),
        ("abc", "{F} ¿Con qué se compara el mueble terminado para controlar su aspecto?", "Con la muestra aprobada", "Con el recuerdo del color", "Con otro mueble del taller", "La muestra aprobada es la referencia firmada por el cliente."),
        ("abc", "{F} El color del cuerpo se ve algo más claro que la muestra aprobada. ¿Qué corresponde?", "Registrar la diferencia y avisar al controlador de calidad", "Aceptarlo porque se parece", "Cambiar la muestra para que coincida", "La referencia es la muestra; las diferencias se registran y se informan."),
        ("ab", "{F} Un compañero dice: «barnizado y lacado son lo mismo». ¿Qué respuesta es correcta?", "No: el barnizado es transparente y el lacado puede ser de color", "Sí: son sinónimos", "El cuadro de la ficha los lista como acabados distintos."),
        ("abc", "{F} Una estudiante dice: «ya sé los nombres de los acabados, puedo aplicar una laca». ¿Qué respuesta es correcta?", "No: aplicar exige instructor autorizado, norma vigente y EPP", "Sí: conocer los nombres la habilita", "Sí, si hay ventilación", "Conocer nombres no habilita para trabajar con productos."),
        ("=", "{F} Si cada aparador tiene 2 puertas con adorno tallado (dato de ejemplo), ¿cuántas puertas talladas hay en 4 aparadores?", "4*2", "Se multiplican los aparadores por las puertas talladas de cada uno.", " puertas"),
    ],
    ctx=("abc", "En el taller de ejemplo, un envase de laca vuelca y el piso queda mojado cerca de una estufa. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Secar el piso con un trapo cerca de la estufa", "Encender la estufa para que se seque", "Un derrame inflamable cerca del calor es riesgo de incendio; se avisa a quien corresponde."),
    sc=[
        ("¿Qué diferencia hay entre barnizado y lacado?", "El barniz es transparente y la laca puede ser de color", "Se distinguen por su aspecto final."),
        ("En Muebles y Terminaciones en Madera: ¿qué es una muestra aprobada?", "Una pieza de referencia firmada por el cliente", "Sirve de referencia para controlar el acabado."),
        ("¿Quién decide si un acabado cumple?", "El controlador de calidad", "La verificación no la hace quien aplicó el acabado."),
    ],
    op=("Cuadro de acabados de ejemplo «Taller Peumo» (ficticio): mueble «Repisa R-2»: frente, lacado verde; tapa, barnizado transparente; costados, impregnación superficial; adorno, tallado. Escribe (a) cuántas partes aparecen en el cuadro, (b) qué acabado lleva la tapa, (c) con qué comparas el mueble terminado y (d) qué documento dice cómo protegerte del producto.",
        "(a) Cuatro partes: frente, tapa, costados y adorno. (b) Barnizado transparente. (c) Con la muestra aprobada. (d) La hoja de datos de seguridad.",
        ["cuenta las partes", "lee el acabado de la tapa", "nombra la muestra aprobada", "nombra la hoja de datos"],
        ["hoja con las cuatro respuestas"],
        ["confundir barnizado y lacado", "comparar con el recuerdo", "confundir ficha técnica con hoja de datos"],
        "Pregunta: «¿qué diferencia hay entre barnizado y lacado?». Si no responde, pídele que relea el vocabulario."),
    reinforce="Escribe tres nombres de acabados y una frase que diga qué es cada uno, sin explicar cómo se aplica.",
    extend="Explica por qué la muestra aprobada evita discusiones con el cliente.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 7 (cálculo de rendimiento de ejemplo, inventado). Pedido de 7 muebles. Superficie a cubrir con el producto de acabado: 2 m² por mueble (dato de ejemplo). "
     "Ficha técnica de ejemplo: rendimiento de 7 m² por litro y por capa; capas indicadas por el fabricante: 2; envases de 1 litro. Merma de ejemplo: 25 % sobre los litros calculados.")
build(
    O6, 3, F,
    use="Aprenderé a calcular en papel cuánto producto de acabado se necesita a partir de la superficie, el rendimiento y las capas indicadas por el fabricante.",
    prior=["Sé qué es el rendimiento.", "Sé calcular un porcentaje sencillo.", "Sé multiplicar y dividir."],
    explain=[
        "El rendimiento es la superficie que cubre una cantidad de producto en una capa; por ejemplo, 12 m² por litro significaría que un litro alcanza para 12 m² en una capa. Para calcular el producto necesario se multiplica la superficie por el número de capas que indica el fabricante y se divide por el rendimiento. Después se suma la merma y se pasa a envases, redondeando hacia arriba. Este es un cálculo de planilla con datos de ejemplo.",
        "El número de capas y el rendimiento los fija el fabricante en la ficha técnica y no se cambian por cuenta propia. Un producto mal calculado puede faltar o sobrar: el faltante presiona a improvisar y el sobrante queda almacenado, con su riesgo si es inflamable. Los envases sobrantes se guardan según la hoja de datos de seguridad, lejos del calor, y los residuos se retiran según el plan. Todo número de esta clase es inventado.",
        TAIL,
    ],
    vocab=[("rendimiento", "superficie que cubre una cantidad de producto en una capa"), ("capa", "cada pasada de producto sobre una superficie, según indica el fabricante"), ("litro", "unidad de volumen para productos líquidos"), ("sobrante almacenado", "envase que queda sin usar y se guarda según la hoja de datos"), ("superficie a cubrir", "área total que recibirá el producto, en m²")],
    worked=[
        ("Litros necesarios", "Un trabajo de ejemplo cubre 12 m² con una capa y el rendimiento es de 6 m² por litro. ¿Cuántos litros se necesitan?", ["Se divide la superficie por el rendimiento.", "12 dividido en 6 son 2."], "2 litros"),
        ("Dos capas", "El mismo trabajo lleva 2 capas. ¿Cuántos litros se necesitan?", ["Se multiplica la superficie por las 2 capas: 24 m².", "24 dividido en 6 son 4."], "4 litros"),
    ],
    mistakes=[("Olvidar multiplicar por el número de capas.", "El producto alcanzaría solo para una capa.", "Se multiplica la superficie por las capas indicadas por el fabricante."),
              ("Guardar los envases sobrantes cerca de una fuente de calor.", "Un producto inflamable puede incendiarse.", "Se guardan según la hoja de datos, lejos del calor.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué indica el rendimiento de un producto de acabado?", "La superficie que cubre una cantidad de producto en una capa", "El tiempo que dura el producto sin usar", "El precio por litro", "El rendimiento relaciona producto y superficie cubierta."),
        ("abc", "¿Quién fija el número de capas de un producto de acabado?", "El fabricante, en la ficha técnica", "Cada persona según su experiencia", "El cliente al recibir el mueble", "El número de capas lo indica el fabricante."),
        ("=", "{F} ¿Cuántos m² suman los 7 muebles?", "7*2", "Se multiplican los muebles por los m² de cada uno.", " m²"),
        ("=", "{F} ¿Cuántos m² hay que cubrir en total considerando las 2 capas (14 m² por capa)?", "14*2", "Se multiplica la superficie por las capas.", " m²"),
        ("=", "{F} ¿Cuántos litros se necesitan para cubrir 28 m² con un rendimiento de 7 m² por litro?", "28//7", "Se divide la superficie entre el rendimiento.", " litros"),
        ("=", "{F} ¿Cuántos litros son la merma de 25 % sobre 4 litros?", "4*25//100", "El 25 % de los litros calculados es la merma.", " litros"),
        ("=", "{F} ¿Cuántos litros hay que comprar en total (4 litros más la merma de 1 litro)?", "4+1", "Se suman los litros calculados y la merma.", " litros"),
        ("abc", "{F} ¿Cuántos envases de 1 litro se compran?", "5 envases", "4 envases", "6 envases", "Con 5 litros se necesitan 5 envases de 1 litro."),
        ("abc", "{F} Una persona calcula solo 1 capa y obtiene 2 litros. ¿Qué error cometió?", "Olvidó multiplicar por las 2 capas del fabricante", "Dividió mal por el rendimiento", "Sumó dos veces la merma", "Con 2 capas el cálculo se duplica; con 1 capa quedó corto."),
        ("ab", "{F} Un compañero dice: «con 3 capas queda mejor, no importa lo que diga la ficha». ¿Qué respuesta es correcta?", "No: las capas las fija el fabricante en la ficha técnica", "Sí: más capas siempre es mejor", "La ficha indica 2 capas, que son las del fabricante."),
        ("abc", "{F} Una estudiante dice: «ya sé calcular el producto, puedo aplicar el acabado». ¿Qué respuesta es correcta?", "No: aplicar exige instructor autorizado, norma vigente y EPP", "Sí: calcular habilita para aplicar", "Sí, si usa ventilación", "El cálculo en papel no habilita para trabajar con productos."),
        ("=", "{F} Si el pedido fuera de 10 muebles de 2 m² cada uno, ¿cuántos m² habría que cubrir en una capa?", "10*2", "Se multiplican los muebles por los m² de cada uno.", " m²"),
        ("abc", "{F} Sobra 1 envase inflamable. ¿Qué corresponde?", "Guardarlo según la hoja de datos, lejos del calor", "Dejarlo en el piso del taller", "Ponerlo junto a la estufa para que no se congele", "El almacenamiento seguro está en la HDS y evita incendios."),
    ],
    ctx=("abc", "En el taller de ejemplo, un envase de producto con vapores se calienta al sol y empieza a hincharse. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Abrirlo para que salgan los vapores", "Golpearlo para comprobar si está duro", "Un envase que se hincha es un riesgo; se avisa a quien corresponde."),
    sc=[
        ("En Muebles y Terminaciones en Madera: ¿Cómo se calculan los litros necesarios?", "Superficie por capas, dividido por el rendimiento", "El rendimiento relaciona superficie y litros."),
        ("En Muebles y Terminaciones en Madera: ¿por qué se redondea hacia arriba el número de envases?", "Porque un envase incompleto igual se compra entero", "No se puede comprar una fracción de envase."),
        ("¿Dónde se guardan los envases sobrantes?", "Según la hoja de datos, lejos del calor", "Un almacenamiento seguro evita incendios y derrames en el taller."),
    ],
    op=("Cálculo de ejemplo «Taller Quillay» (ficticio): 6 muebles de 3 m² cada uno; rendimiento de ejemplo de 9 m² por litro y por capa; 2 capas; merma de ejemplo de 50 % sobre los litros calculados; envases de 1 litro. Escribe (a) los m² a cubrir en una capa, (b) los m² con las 2 capas, (c) los litros calculados y los litros con la merma y (d) cuántos envases compras.",
        "(a) 6×3 son 18 m². (b) 18×2 son 36 m². (c) 36÷9 son 4 litros; la merma de 50 % es 2 litros; en total 6 litros. (d) 6 envases de 1 litro.",
        ["calcula la superficie", "multiplica por las capas", "calcula litros y merma", "calcula los envases"],
        ["hoja con las cuatro respuestas"],
        ["olvidar las capas", "olvidar la merma", "dividir al revés"],
        "Pregunta: «¿por qué se multiplica por las capas?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula los litros para 20 m² con un rendimiento de 5 m² por litro y 2 capas.",
    extend="Explica por qué un sobrante de producto inflamable es también un riesgo de seguridad.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 8 (control del acabado contra la muestra aprobada, ejemplo inventado). Lista de verificación de ejemplo con tres criterios: color igual a la muestra, superficie lisa y uniforme, y ausencia de gotas o burbujas. "
     "Resultados de seis piezas (C = cumple, N = no cumple): pieza 1: C, C, C; pieza 2: N, C, C; pieza 3: C, C, C; pieza 4: C, N, N; pieza 5: C, C, C; pieza 6: C, C, N. "
     "Regla de ejemplo: una pieza se aprueba solo si cumple los tres criterios. Las piezas no aprobadas se separan y se registran.")
build(
    O6, 4, F,
    use="Aprenderé a aplicar una lista de verificación de acabado contra la muestra aprobada y a calcular cuántas piezas se aprueban.",
    prior=["Sé qué es la muestra aprobada.", "Sé calcular un porcentaje sencillo.", "Sé leer una tabla."],
    explain=[
        "Una lista de verificación enumera criterios observables que el acabado debe cumplir, como el color, la textura o la presencia de defectos visibles. Para cada pieza se marca si cumple o no cada criterio. Una pieza se aprueba solo si cumple todos; basta un criterio incumplido para que no se apruebe. El controlador de calidad anota el resultado de cada criterio para que el registro permita saber en qué falló cada pieza.",
        "Las piezas no aprobadas se separan y se registra qué criterio falló. Si el mismo criterio falla en muchas piezas, hay un problema común, que se informa al jefe de producción sin intentar corregirlo en el momento. No se retoca una pieza por cuenta propia ni se exponen más personas a los productos: cualquier trabajo de corrección lo decide el responsable y lo ejecuta personal autorizado. En esta clase todo se calcula en papel con datos inventados.",
        TAIL,
    ],
    vocab=[("lista de verificación", "tabla de criterios observables que se marcan como cumple o no cumple"), ("criterio observable", "característica que se puede comprobar mirando la pieza"), ("aprobada", "pieza que cumple todos los criterios"), ("problema común", "falla que se repite en varias piezas"), ("registro de calidad", "documento donde se anotan los resultados de cada criterio")],
    worked=[
        ("Aprobar una pieza", "Una pieza de ejemplo cumple dos de tres criterios. ¿Se aprueba?", ["Se aprueba solo si cumple los tres criterios.", "Cumple solo dos."], "No se aprueba"),
        ("Contar aprobadas", "En una revisión de ejemplo se revisan 10 piezas y 7 se aprueban. ¿Cuántas no se aprueban?", ["Se restan las aprobadas del total.", "10 menos 7 son 3."], "3 piezas"),
    ],
    mistakes=[("Aprobar una pieza porque «cumple casi todo».", "La regla pide cumplir todos los criterios.", "Se separa la pieza y se registra qué criterio falló."),
              ("Retocar la pieza por cuenta propia para aprobarla.", "No se sabe el riesgo ni se registra el problema.", "Se informa al responsable y decide quién interviene.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es una lista de verificación de acabado?", "Una tabla de criterios observables que se marcan como cumple o no cumple", "Una lista de precios de los productos", "El plano con las cotas del mueble", "La lista de verificación ordena criterios del control."),
        ("abc", "¿Cuándo se aprueba una pieza según la regla de ejemplo?", "Cuando cumple los tres criterios", "Cuando cumple al menos uno", "Cuando cumple la mayoría", "Basta un criterio incumplido para que no se apruebe."),
        ("abc", "{F} ¿Qué pieza falla solo en el color?", "La pieza 2", "La pieza 4", "La pieza 6", "La pieza 2 marca N solo en el color."),
        ("abc", "{F} ¿Qué pieza falla en superficie y en gotas o burbujas?", "La pieza 4", "La pieza 2", "La pieza 6", "La pieza 4 marca N en superficie y en gotas o burbujas."),
        ("=", "{F} ¿Cuántas piezas cumplen los tres criterios?", "1+1+1", "Se cuenta cada pieza que marca C en los tres criterios.", " piezas"),
        ("=", "{F} ¿Cuántas piezas no se aprueban?", "6-3", "Se restan las aprobadas del total revisado.", " piezas"),
        ("=", "{F} ¿Qué porcentaje de las 6 piezas se aprueba (parte entera)?", "3*100//6", "Se multiplican las aprobadas por 100 y se divide por el total.", " %"),
        ("=", "{F} ¿Cuántas marcas N hay en total en toda la tabla?", "1+2+1", "Se suman las N de las piezas 2, 4 y 6.", " marcas"),
        ("abc", "{F} ¿Qué criterio incumple la pieza 6?", "Ausencia de gotas o burbujas", "Color igual a la muestra", "Superficie lisa y uniforme", "La pieza 6 marca N solo en el tercer criterio."),
        ("abc", "{F} La pieza 2 solo falla en el color. Una persona propone aprobarla porque «es lo menos grave». ¿Qué respuesta es correcta?", "No: la regla pide cumplir los tres criterios", "Sí: un solo fallo no cuenta", "Sí, si el cliente no está", "La regla de ejemplo exige todos los criterios."),
        ("ab", "{F} Un estudiante dice: «puedo retocar la pieza 4 con un poco de producto para aprobarla». ¿Qué respuesta es correcta?", "No: se informa al responsable y decide quién interviene", "Sí: retocar es parte del control", "La ficha indica que las no aprobadas se separan y se registran."),
        ("abc", "{F} Otra estudiante dice: «ya sé evaluar un acabado, puedo corregirlo con el producto». ¿Qué respuesta es correcta?", "No: corregir exige instructor autorizado, norma vigente y EPP", "Sí: evaluar habilita para corregir", "Sí, si hay ventilación", "Evaluar en papel no habilita para trabajar con productos."),
        ("abc", "{F} Si la mitad de las piezas fallara en el mismo criterio, ¿qué corresponde?", "Informar al jefe de producción un problema común", "Corregir cada pieza sin avisar", "Aprobarlas para no atrasar", "Una falla repetida se informa para encontrar su origen."),
    ],
    ctx=("abc", "En la zona de terminaciones de ejemplo, una persona se salpica los ojos con un producto y siente ardor intenso. ¿Qué se hace según las reglas generales?", "Avisar de inmediato a un adulto responsable y a emergencias, sin manipular el producto", "Frotarse los ojos con la manga", "Seguir trabajando hasta terminar la pieza", "Una salpicadura en los ojos se informa a quien corresponde y a emergencias."),
    sc=[
        ("¿Cuántos criterios debe cumplir una pieza para aprobarse en la regla de ejemplo?", "Los tres", "La regla exige cumplir todos los criterios."),
        ("En Muebles y Terminaciones en Madera: ¿con qué se compara el color de la pieza?", "Con la muestra aprobada", "La muestra es la referencia del acabado."),
        ("¿Qué se hace con las piezas no aprobadas?", "Se separan y se registra qué criterio falló", "El registro permite encontrar el origen del problema."),
    ],
    op=("Control de ejemplo «Taller Ñire» (ficticio): criterios: color igual a la muestra, superficie lisa y ausencia de gotas. Cinco piezas (C = cumple, N = no cumple): pieza A: C, C, C; pieza B: C, N, C; pieza C: N, N, C; pieza D: C, C, C; pieza E: C, C, N. Escribe (a) cuántas piezas se aprueban, (b) qué criterio incumple B, (c) qué porcentaje se aprueba y (d) qué haces con las no aprobadas.",
        "(a) Se aprueban A y D: 2 piezas. (b) La superficie. (c) 2×100÷5 son 40 %. (d) Las separo y registro qué criterio falló, y aviso al responsable.",
        ["cuenta las aprobadas", "identifica el criterio incumplido", "calcula el porcentaje", "separa y registra"],
        ["hoja con las cuatro respuestas"],
        ["aprobar piezas que cumplen casi todo", "retocar por cuenta propia", "no registrar el criterio que falló"],
        "Pregunta: «¿por qué una pieza con solo un fallo no se aprueba?». Si no responde, pídele que relea la regla."),
    reinforce="Escribe tres criterios observables de ejemplo para controlar el acabado de una tapa.",
    extend="Explica qué ventaja tiene registrar qué criterio falló y no solo que la pieza no se aprobó.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 9 (comparación de alternativas de acabado, ejemplo inventado). Tres sistemas de acabado ficticios para una mesa. Puntajes de conveniencia de 1 a 5, donde un puntaje mayor es mejor en todos los criterios (incluida la seguridad, donde 5 significa menos peligro): "
     "sistema X: costo 4, durabilidad 3, seguridad 5; sistema Y: costo 3, durabilidad 5, seguridad 2; sistema Z: costo 5, durabilidad 2, seguridad 4. "
     "Pesos de ejemplo de cada criterio: costo 2, durabilidad 3, seguridad 3. El puntaje total de un sistema es la suma de cada puntaje multiplicado por su peso.")
build(
    O6, 5, F,
    use="Aprenderé a comparar alternativas de acabado con una matriz de criterios y pesos, a incluir la seguridad como criterio y a dejar registrada la decisión.",
    prior=["Sé qué es un criterio.", "Sé multiplicar y sumar.", "Sé qué es sustituir un producto peligroso."],
    explain=[
        "Comparar alternativas es elegir entre varias opciones con criterios claros. Una matriz de decisión es una tabla donde cada opción recibe un puntaje por criterio; cada criterio tiene un peso que indica su importancia. El puntaje total de una opción es la suma de cada puntaje multiplicado por su peso. La opción con mayor puntaje total es la más conveniente según esos criterios y esos pesos, que son de ejemplo y se pueden discutir.",
        "La seguridad es un criterio, no un detalle: según la jerarquía de controles, sustituir un producto muy peligroso por otro menos peligroso es una medida de prevención. Verificar la calidad es comprobar que lo elegido cumple lo pedido, por ejemplo comparando con la muestra aprobada y usando la lista de verificación. La decisión se registra con las opciones, los criterios, los pesos y quién decidió. Cambiar de producto lo aprueba el responsable; nadie lo cambia por cuenta propia.",
        TAIL,
    ],
    vocab=[("matriz de decisión", "tabla que compara opciones con criterios y pesos"), ("peso", "importancia de un criterio, expresada en un número"), ("puntaje total", "suma de cada puntaje multiplicado por su peso"), ("sustitución", "cambiar un producto peligroso por otro menos peligroso"), ("verificar", "comprobar que lo elegido cumple lo pedido")],
    worked=[
        ("Puntaje ponderado", "Una opción de ejemplo tiene puntaje 3 en un criterio de peso 2 y puntaje 4 en otro de peso 1. ¿Cuál es su total?", ["Se multiplica cada puntaje por su peso: 6 y 4.", "Se suman los dos resultados."], "10 puntos"),
        ("Elegir la opción", "Dos opciones de ejemplo suman 18 y 21 puntos. ¿Cuál es más conveniente según esa matriz?", ["Se compara el total de cada una.", "21 es mayor que 18."], "La de 21 puntos"),
    ],
    mistakes=[("Elegir la opción más barata sin mirar la seguridad.", "Un producto barato puede ser muy peligroso para las personas.", "La seguridad es un criterio con peso dentro de la matriz."),
              ("Cambiar de producto por cuenta propia a mitad del trabajo.", "El nuevo producto puede tener otros peligros y otra ficha.", "El cambio lo aprueba el responsable y se registra.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es una matriz de decisión?", "Una tabla que compara opciones con criterios y pesos", "Un plano con las medidas del mueble", "Una lista de envases sin etiqueta", "La matriz ordena la comparación entre opciones."),
        ("abc", "¿Qué es sustituir un producto en prevención de riesgos?", "Cambiar un producto peligroso por otro menos peligroso", "Comprar el doble del mismo producto", "Guardar el producto en un lugar oculto", "La sustitución reduce el peligro desde el origen."),
        ("=", "{F} ¿Cuál es el puntaje total del sistema X?", "4*2+3*3+5*3", "Se multiplica cada puntaje por su peso y se suman los resultados.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total del sistema Y?", "3*2+5*3+2*3", "Se multiplica cada puntaje por su peso y se suman los resultados.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total del sistema Z?", "5*2+2*3+4*3", "Se multiplica cada puntaje por su peso y se suman los resultados.", " puntos"),
        ("abc", "{F} ¿Qué sistema tiene el mayor puntaje total?", "El sistema X", "El sistema Y", "El sistema Z", "X suma 32, más que Y con 27 y Z con 28."),
        ("abc", "{F} ¿Qué sistema es el más barato según los puntajes?", "El sistema Z", "El sistema Y", "El sistema X", "Z tiene el puntaje más alto en costo, 5."),
        ("abc", "{F} ¿Qué sistema es el más peligroso según los puntajes?", "El sistema Y", "El sistema X", "El sistema Z", "Y tiene el puntaje más bajo en seguridad, 2."),
        ("abc", "{F} Una persona propone elegir Y por ser el más durable. ¿Qué respuesta es correcta?", "No: con los pesos de la ficha, el total de Y es menor que el de X", "Sí: la durabilidad decide siempre", "Sí, porque la seguridad no importa", "La matriz considera todos los criterios con sus pesos."),
        ("ab", "{F} Un compañero dice: «si el peso de la seguridad subiera a 5, el sistema Y pasaría a ser el mejor». ¿Qué respuesta es correcta?", "No: al recalcular, X sigue con el mayor total", "Sí: Y es el más durable y por eso ganaría", "Con peso 5 en seguridad, X suma 42, Y suma 31 y Z suma 36."),
        ("abc", "{F} Una estudiante dice: «ya elegí el sistema X, puedo cambiar el producto en el taller por mi cuenta». ¿Qué respuesta es correcta?", "No: el cambio lo aprueba el responsable y lo ejecuta personal autorizado", "Sí: elegir habilita para cambiar", "Sí, si cuesta menos", "Elegir en una matriz no habilita para cambiar productos."),
        ("=", "{F} Si el peso de la seguridad pasara de 3 a 4, ¿cuál sería el nuevo puntaje total de X (4 por 2, 3 por 3 y 5 por 4)?", "4*2+3*3+5*4", "Se recalcula con el nuevo peso de seguridad.", " puntos"),
        ("abc", "{F} ¿Qué se registra al decidir entre los sistemas?", "Las opciones, los criterios, los pesos y quién decidió", "Solo el nombre del sistema elegido", "Solo el precio", "El registro permite revisar la decisión después."),
    ],
    ctx=("abc", "En el taller de ejemplo, al probar un producto nuevo una persona siente mareo y náuseas por los vapores. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Seguir trabajando con mascarilla hasta terminar", "Pedirle que beba agua y regrese a la zona", "Los síntomas por vapores se informan a quien corresponde y a emergencias."),
    sc=[
        ("¿Cómo se obtiene el puntaje total de una opción?", "Sumando cada puntaje multiplicado por su peso", "Los pesos reflejan la importancia de cada criterio."),
        ("En Muebles y Terminaciones en Madera: ¿por qué la seguridad es un criterio de la matriz?", "Porque un producto peligroso afecta a las personas", "La seguridad pesa en la decisión."),
        ("¿Quién aprueba cambiar de producto?", "El responsable", "Cambiar de producto altera peligros y fichas."),
    ],
    op=("Matriz de ejemplo «Taller Peumo» (ficticio): dos acabados para un banco. Acabado P: costo 5, durabilidad 3, seguridad 2. Acabado Q: costo 3, durabilidad 4, seguridad 5. Pesos: costo 1, durabilidad 2, seguridad 3. Escribe (a) el total de P, (b) el total de Q, (c) cuál conviene y (d) qué registras al decidir.",
        "(a) 5×1+3×2+2×3 son 17. (b) 3×1+4×2+5×3 son 26. (c) Conviene Q. (d) Las opciones, los criterios, los pesos y quién decidió.",
        ["calcula el total de P", "calcula el total de Q", "elige la opción", "describe el registro"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por los pesos", "elegir por el costo solo", "no registrar la decisión"],
        "Pregunta: «¿por qué la seguridad es parte de la decisión?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula el total de una opción con puntajes 2, 4 y 5 y pesos 1, 2 y 3.",
    extend="Explica cómo cambiaría la decisión si el peso de la seguridad fuese mayor.",
)
