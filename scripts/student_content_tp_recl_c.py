"""Refrigeración y Climatización TP 3.º y 4.º medio: OAE-06 (carga de fluidos y puesta en marcha: riesgos, documentos y criterios, sin procedimientos) y OAE-07 (inspección y diagnóstico de fallas en papel). Solo conceptos y planillas, con datos de ejemplo."""
from __future__ import annotations

from tp_recl_common import AVISO, EMER, build

O6 = "TP-RECL-3y4-OAE-06"
O7 = "TP-RECL-3y4-OAE-07"

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). Proyecto «Pastelería Aurora» (ficticia): un sistema nuevo para una vitrina refrigerada y un aire acondicionado. Etapas del proyecto, en lista: preparar los documentos, "
     "verificar el sistema por personal autorizado, cargar el refrigerante, poner en marcha y entregar. Riesgos que anota una ficha de seguridad de ejemplo: presión alta, congelación al contacto con la piel, "
     "desplazamiento del aire respirable en espacios cerrados, inflamabilidad en algunos tipos de fluido y daño al medio ambiente si se libera.")
build(
    O6, 1, F,
    use="Aprenderé qué significa cargar un sistema con refrigerante y ponerlo en marcha, quién puede hacerlo, qué riesgos tienen los refrigerantes y por qué nunca se liberan al ambiente.",
    prior=["Sé qué es un refrigerante.", "Sé qué es una especificación técnica.", "Sé qué es un EPP."],
    explain=[
        "Cargar un sistema es introducir el refrigerante en la cantidad que fija el fabricante, y poner en marcha es hacerlo funcionar por primera vez después de verificarlo. Ambas tareas las realiza un técnico certificado, según la norma vigente. Las presiones y fuerzas con que trabaja cada equipo las indica el fabricante en su manual; nadie las usa de memoria ni las toma de otro equipo. Este cuaderno no enseña a cargar ni a poner en marcha: solo explica los conceptos, los documentos y las reglas de seguridad.",
        "Los refrigerantes tienen riesgos: alta presión, congelación al contacto con la piel, desplazamiento del aire respirable en espacios cerrados e inflamabilidad en algunos tipos. Además dañan el medio ambiente si se liberan, y por eso la norma vigente prohíbe soltarlos al ambiente; si hay una fuga, se avisa. Las medidas se ordenan en la jerarquía de controles y el EPP es el último nivel. La ficha de datos de seguridad de cada fluido es el documento que informa de sus peligros.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("cargar", "introducir en el sistema la cantidad de refrigerante que fija el fabricante"), ("puesta en marcha", "primer funcionamiento de un sistema después de verificarlo"), ("técnico certificado", "persona evaluada y autorizada según la norma vigente para manipular refrigerantes"), ("ficha de datos de seguridad", "documento que informa los peligros, el manejo seguro y el almacenamiento de un fluido"), ("espacio cerrado", "lugar con poca ventilación donde un gas puede desplazar el aire respirable"), ("manual del fabricante", "documento que indica los valores correctos de cada equipo")],
    worked=[
        ("Horas de trabajo", "Una jornada de ejemplo tiene 8 horas. Un técnico dedica 2 horas a documentos y 3 a una verificación. ¿Cuántas horas quedan?", ["Se restan las horas ocupadas de la jornada.", "8 menos 2 menos 3 son 3."], "3 horas"),
        ("Identificar el riesgo", "Una ficha de ejemplo advierte que un fluido puede producir congelación al contacto. ¿Qué parte del cuerpo expone?", ["La congelación ocurre en el lugar de contacto.", "El contacto es con la piel."], "La piel"),
    ],
    mistakes=[("Creer que se puede cargar un sistema «a ojo» porque se vio hacerlo.", "La cantidad la fija el fabricante y un error causa fallas o riesgos.", "Esta tarea la hace solo un técnico certificado."),
              ("Soltar un poco de refrigerante al ambiente porque «es poco».", "Daña el medio ambiente y la norma vigente lo prohíbe.", "Ante una fuga o duda, avisa a un adulto responsable.")],
    T=[
        ("abc", "En Refrigeración: ¿qué significa cargar un sistema?", "Introducir en el sistema la cantidad de refrigerante que fija el fabricante", "Cambiar el aire del recinto por aire exterior", "Llenar la red con agua para verificarla", "Cargar es introducir el refrigerante en la cantidad que indica el fabricante."),
        ("abc", "¿Quién puede cargar un sistema y ponerlo en marcha?", "Un técnico certificado, según la norma vigente", "Cualquier persona con herramientas", "El cliente que compró el equipo", "Son tareas con riesgo que exigen certificación, no solo herramientas ni propiedad del equipo."),
        ("abc", "¿Por qué no se libera refrigerante al ambiente?", "Porque daña el medio ambiente y la norma vigente lo regula", "Porque es un material barato que se puede reponer", "Porque hace ruido al salir", "La liberación daña el ambiente y está regulada por la norma vigente."),
        ("abc", "{F} ¿Qué riesgo de la ficha se asocia al contacto con la piel?", "La congelación", "El desplazamiento del aire respirable", "La inflamabilidad", "Según la ficha, el contacto con la piel puede causar congelación."),
        ("abc", "{F} ¿Qué riesgo de la ficha se asocia a un espacio cerrado?", "El desplazamiento del aire respirable", "La congelación", "El daño al medio ambiente", "En un espacio cerrado el fluido puede desplazar el aire que se respira."),
        ("=", "{F} El técnico certificado cobra $35.000 por hora de ejemplo y la puesta en marcha dura 3 horas. ¿Cuánto cobra?", "35000*3", "Se multiplica el valor por hora por las horas de trabajo.", " pesos"),
        ("=", "{F} Una jornada tiene 8 horas. Si el técnico dedica 3 horas a documentos y 2 a la puesta en marcha, ¿cuántas horas quedan?", "8-3-2", "Se restan de la jornada las horas dedicadas a cada tarea.", " horas"),
        ("abc", "{F} Un ayudante propone cargar refrigerante «a ojo» porque ya vio cómo se hace. ¿Qué corresponde?", "No hacerlo: la cantidad la fija el fabricante y la tarea la hace un técnico certificado", "Hacerlo con guantes y lentes", "Hacerlo si el cliente lo autoriza", "Los EPP o la autorización del cliente no reemplazan la certificación ni el valor del fabricante."),
        ("abc", "{F} Una vecina quiere que un estudiante «ponga en marcha» su equipo nuevo. ¿Qué responde?", "Que no está autorizado y que lo haga un técnico certificado", "Que lo hará si ella no cobra a nadie", "Que lo hará si busca el manual en internet", "Poner en marcha exige certificación; haber leído un manual no habilita."),
        ("ab", "{F} Un compañero dice: «si recuerdo la presión de otro equipo, puedo usarla». ¿Es correcto?", "No: los valores de presión y fuerza los indica el fabricante para cada equipo", "Sí: todos los equipos trabajan con la misma presión", "Cada equipo tiene sus valores en su manual y no se toman de memoria ni de otro equipo."),
        ("abc", "{F} Alguien se marea en una sala cerrada donde puede haber una fuga de refrigerante. ¿Qué indican las reglas generales?", "No entrar ni tocar, avisar a un adulto responsable y llamar a emergencias", "Entrar a buscarlo sin protección porque es urgente", "Abrir una ventana y esperar sin avisar", "Entrar sin protección sumaría más afectados; se avisa de inmediato."),
        ("=", "{F} La puesta en marcha dura 3 horas y una visita de seguimiento dura 1 hora más. Con $35.000 por hora de ejemplo, ¿cuánto cuestan ambas?", "(3+1)*35000", "Se suman las horas y se multiplican por el valor por hora.", " pesos"),
        ("abc", "{F} Para abaratar, el cliente quiere usar un fluido que sobró de otra obra sin saber cuál es. ¿Qué corresponde?", "No usarlo: un fluido sin identificar no se usa; solo un técnico certificado maneja refrigerantes", "Usarlo si parece del mismo color", "Mezclarlo con el fluido nuevo", "Un fluido desconocido es un riesgo para las personas y para el equipo."),
    ],
    ctx=("abc", "Un técnico de ejemplo ve que otra persona abre una válvula de un equipo para «ver qué sale». ¿Qué corresponde?", "No acercarse ni tocar y avisar de inmediato a un adulto responsable", "Acercarse para ayudarle", "Grabar un video para mostrarlo", "Manipular refrigerante sin autorización es un riesgo; no se interviene y se avisa a quien corresponde."),
    sc=[
        ("En Refrigeración: ¿quién carga un sistema con refrigerante?", "Un técnico certificado, según la norma vigente", "Este cuaderno no habilita para trabajar ni para intervenir equipos."),
        ("¿De dónde se toman las presiones correctas de un equipo?", "Del manual del fabricante de ese equipo", "No se toman de memoria ni de otro equipo."),
        ("¿Qué se hace ante una fuga de refrigerante?", "No entrar ni tocar, avisar a un adulto responsable y a emergencias", "Nunca se libera refrigerante al ambiente."),
    ],
    op=("Proyecto de ejemplo «Panadería Lenga» (ficticia): un sistema nuevo de refrigeración. La jornada tiene 8 horas; el técnico certificado cobra $30.000 por hora de ejemplo, dedica 2 horas a documentos y 3 a la puesta en marcha. "
        "Escribe (a) quién puede poner en marcha el sistema, (b) cuántas horas quedan libres, (c) cuánto cuestan las 5 horas de trabajo, (d) qué haces si alguien se marea cerca del equipo.",
        "(a) Un técnico certificado, según la norma vigente. (b) 8 menos 2 menos 3 son 3 horas. (c) 5 por 30.000 son 150.000 pesos. (d) No entro ni toco, aviso a un adulto responsable y llamo a emergencias.",
        ["nombra al técnico certificado", "calcula las horas", "calcula el costo", "indica no entrar y avisar"],
        ["hoja con las cuatro respuestas"],
        ["decir que cualquiera puede poner en marcha", "sumar en vez de restar", "decir que entraría a ayudar"],
        "Pregunta: «¿qué haces si alguien se marea?». Si no responde, pídele que relea la regla de no entrar y avisar."),
    reinforce="Escribe tres riesgos de los refrigerantes y una regla general de seguridad para cada uno.",
    extend="Explica con un ejemplo por qué tener un manual en las manos no habilita para cargar un sistema.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (ficha de datos de seguridad de ejemplo, inventada, de un fluido ficticio «Fluido Alfa»; no corresponde a ningún producto real). Secciones: 1 identificación; 2 peligros (presión alta, congelación al contacto); "
     "3 primeros auxilios (buscar atención médica de inmediato); 4 manipulación y almacenamiento (lugar ventilado, lejos del calor); 5 protección personal (lentes y guantes); 6 información ambiental (índice de calentamiento global de ejemplo: 400); 7 inflamabilidad (no inflamable).")
build(
    O6, 2, F,
    use="Aprenderé a leer una ficha de datos de seguridad y una etiqueta, y qué significan los conceptos de carga nominal, índice de calentamiento global y acta de puesta en marcha.",
    prior=["Sé qué riesgos tienen los refrigerantes.", "Sé qué es un técnico certificado.", "Sé multiplicar."],
    explain=[
        "La ficha de datos de seguridad (FDS) es un documento ordenado en secciones: identificación del fluido, peligros, primeros auxilios, manipulación y almacenamiento, protección personal, información ambiental e inflamabilidad. Antes de que una persona certificada maneje un fluido, la lee. La etiqueta del recipiente resume lo esencial y debe estar siempre legible. La carga nominal es la cantidad de refrigerante que indica la placa del equipo; es el valor del fabricante y no se cambia por cuenta propia.",
        "El índice de calentamiento global (PCG) indica cuántas veces más calienta la atmósfera un fluido que la misma masa de dióxido de carbono; entre dos fluidos, el de menor índice daña menos al ambiente. Dato de ejemplo: un fluido con índice 250 que se fuga en 4 kg equivale a 1.000 kg de dióxido de carbono. El acta de puesta en marcha es el documento que deja constancia de lo verificado, de la cantidad cargada y de quién lo hizo. Todo lo anterior es lectura de documentos; manipular fluidos exige certificación.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("FDS", "ficha de datos de seguridad: documento que informa peligros, manejo y almacenamiento de un fluido"), ("etiqueta", "rótulo del recipiente que resume lo esencial del fluido"), ("carga nominal", "cantidad de refrigerante que indica la placa del equipo"), ("PCG", "índice de calentamiento global: cuántas veces más calienta la atmósfera que el mismo peso de dióxido de carbono"), ("acta de puesta en marcha", "documento que deja constancia de lo verificado, la cantidad cargada y quién lo hizo"), ("bitácora", "cuaderno donde se anotan las intervenciones y los datos de un equipo")],
    worked=[
        ("Ubicar la información", "Una FDS de ejemplo tiene secciones numeradas. ¿Dónde buscas qué hacer si alguien entra en contacto con el fluido?", ["Eso es información de primeros auxilios.", "Está en la sección de primeros auxilios."], "En la sección de primeros auxilios"),
        ("Equivalente en CO₂", "Un fluido de ejemplo con PCG 300 se fuga en 2 kg. ¿Cuántos kg de dióxido de carbono equivale?", ["Se multiplican los kg por el PCG.", "2 por 300 son 600."], "600 kg"),
    ],
    mistakes=[("Manejar un fluido sin haber leído su ficha de datos de seguridad.", "No se conocen sus peligros ni las medidas de protección.", "Lee la FDS antes; el manejo lo hace personal certificado."),
              ("Cambiar la carga nominal de la placa «porque el equipo es más grande».", "La carga nominal es un valor del fabricante.", "Respeta la placa y consulta al profesional encargado.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es la ficha de datos de seguridad (FDS)?", "Un documento que informa peligros, manejo y almacenamiento de un fluido", "Una factura que indica el precio de un fluido", "Un plano que muestra dónde está el equipo", "La FDS informa sobre seguridad; el precio va en la factura y la ubicación en el plano."),
        ("abc", "¿Qué es la carga nominal de un equipo?", "La cantidad de refrigerante que indica la placa del equipo", "La cantidad de refrigerante que sobró de otra obra", "La energía que consume el equipo", "La carga nominal es el valor de refrigerante que el fabricante pone en la placa."),
        ("abc", "¿Qué indica el índice de calentamiento global (PCG) de un fluido?", "Cuántas veces más calienta la atmósfera que el mismo peso de dióxido de carbono", "Qué tan caliente está el fluido dentro del equipo", "Cuánto cuesta cada kilo del fluido", "El PCG compara el efecto sobre la atmósfera; no es temperatura ni precio."),
        ("abc", "{F} ¿En qué sección de la ficha buscas cómo almacenar el fluido?", "En la sección 4, manipulación y almacenamiento", "En la sección 2, peligros", "En la sección 6, información ambiental", "El almacenamiento está en la sección 4; los peligros y el ambiente están en otras."),
        ("abc", "{F} ¿Qué peligros anota la ficha del Fluido Alfa?", "Presión alta y congelación al contacto", "Inflamabilidad y toxicidad", "Solo daño ambiental", "La sección 2 dice presión alta y congelación al contacto; la sección 7 dice que no es inflamable."),
        ("abc", "{F} ¿Es inflamable el Fluido Alfa según la ficha?", "No, según la sección 7", "Sí, según la sección 7", "La ficha no lo dice", "La sección 7 de la ficha indica que no es inflamable."),
        ("=", "{F} Si el Fluido Alfa se fuga en 3 kg, ¿cuántos kg de dióxido de carbono equivale (kg por índice)?", "3*400", "Se multiplican los kg fugados por el índice de calentamiento global de la ficha.", " kg"),
        ("=", "{F} Si el Fluido Alfa se fuga en 5 kg, ¿cuántos kg de dióxido de carbono equivale?", "5*400", "Se multiplican los kg fugados por el índice de la ficha.", " kg"),
        ("abc", "{F} Una persona quiere manipular el Fluido Alfa porque «ya leyó la ficha». ¿Qué corresponde?", "No hacerlo: leer la ficha informa, pero manipular exige certificación", "Hacerlo, porque la ficha dice que es seguro", "Hacerlo con los lentes y guantes que indica la ficha", "Leer la ficha no habilita; los lentes y guantes no reemplazan la certificación."),
        ("abc", "{F} Un compañero dice que la ficha sobra porque el fluido «no es inflamable». ¿Qué respuesta es correcta?", "No: la ficha también advierte presión alta, congelación y daño ambiental", "Sí: si no es inflamable, no tiene riesgos", "Sí: la ficha solo sirve para fluidos inflamables", "Un fluido no inflamable igual tiene presión alta y puede congelar la piel."),
        ("abc", "{F} En la placa dice una carga nominal y un compañero propone aumentarla «para que enfríe más». ¿Qué corresponde?", "Respetar la placa y consultar al profesional encargado", "Aumentarla un poco, porque más fluido enfría más", "Aumentarla solo si el cliente se queja", "La carga nominal es el valor del fabricante y no se cambia por cuenta propia."),
        ("=", "{F} Una fuga de ejemplo de 2 kg del Fluido Alfa ocurre cuatro veces en el año. ¿Cuántos kg de dióxido de carbono equivalen a las cuatro fugas?", "2*4*400", "Se multiplican los kg por fuga, el número de fugas y el índice.", " kg"),
        ("abc", "{F} El acta de puesta en marcha no indica quién hizo la verificación. ¿Qué problema tiene?", "No queda constancia de quién es responsable de lo verificado", "Ninguno, porque basta la fecha", "Que falta el precio del fluido", "El acta debe dejar constancia del responsable de lo verificado."),
    ],
    ctx=("abc", "Una bodeguera de ejemplo recibe un recipiente de fluido sin etiqueta legible. ¿Qué hace?", "No lo usa ni lo mueve y avisa al supervisor para identificarlo", "Lo usa porque parece igual a los otros", "Lo abre para ver qué contiene", "Un recipiente sin etiqueta no se maneja: se identifica por canales seguros."),
    sc=[
        ("En Refrigeración: ¿qué es la carga nominal?", "La cantidad de refrigerante que indica la placa del equipo", "Es un valor que fija el fabricante en la placa del equipo."),
        ("¿Qué compara el índice de calentamiento global?", "El efecto de un fluido sobre la atmósfera con el del dióxido de carbono", "El de menor índice daña menos al ambiente."),
        ("¿Dónde se anota quién verificó el sistema al ponerlo en marcha?", "En el acta de puesta en marcha", "El acta deja constancia del responsable."),
    ],
    op=("Ficha de datos de seguridad de ejemplo del «Fluido Beta» (ficticio): sección 2, peligros: presión alta y congelación al contacto; sección 4: almacenar en lugar ventilado y lejos del calor; sección 6: índice de calentamiento global de ejemplo 150; sección 7: no inflamable. "
        "Escribe (a) en qué sección buscas cómo almacenarlo, (b) qué peligros anota, (c) cuántos kg de dióxido de carbono equivale una fuga de 6 kg, (d) qué haces si un recipiente llega sin etiqueta.",
        "(a) En la sección 4. (b) Presión alta y congelación al contacto. (c) 6 por 150 son 900 kg. (d) No lo uso ni lo muevo y aviso al supervisor para identificarlo.",
        ["ubica la sección", "nombra los peligros", "calcula el equivalente", "no usa un recipiente sin etiqueta"],
        ["hoja con las cuatro respuestas"],
        ["confundir secciones", "sumar en vez de multiplicar", "decir que lo abriría para ver"],
        "Pregunta: «¿por qué no usas un recipiente sin etiqueta?». Si no responde, pídele que relea el papel de la etiqueta."),
    reinforce="Escribe las siete secciones de la ficha de ejemplo y qué información busca cada una.",
    extend="Explica con un ejemplo por qué dos fluidos distintos pueden tener índices de calentamiento global muy diferentes.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (acta de puesta en marcha de ejemplo, inventada, de 8 puntos). Cumplidos: 1 documentos del equipo revisados; 2 instalación aprobada por el profesional encargado; 3 certificación eléctrica archivada; 5 área despejada de personas ajenas; 6 bitácora abierta. "
     "Pendientes: 4 certificado vigente del técnico (venció hace un mes); 7 valores del fabricante disponibles en el sitio; 8 firma del profesional encargado. Puntos de detención (deben cumplirse antes de continuar): 2, 3 y 4.")
build(
    O6, 3, F,
    use="Aprenderé a leer un acta de puesta en marcha, a reconocer los puntos de detención y a decidir cuándo no se continúa.",
    prior=["Sé qué es un acta.", "Sé qué es un técnico certificado.", "Sé qué es una lista de control."],
    explain=[
        "El acta de puesta en marcha es una lista de control con puntos numerados. Cada punto está cumplido o pendiente. Un punto de detención es un punto que debe cumplirse antes de continuar: si está pendiente, la tarea se detiene hasta que se cumpla, sin importar cuántos otros puntos estén cumplidos. Los puntos de detención suelen ser requisitos de seguridad, como la aprobación de la instalación, la certificación eléctrica y la calificación vigente del técnico.",
        "Quien lee el acta no decide cumplir un punto por su cuenta. Si encuentra un punto pendiente, lo informa al supervisor o al profesional encargado, que decide. Un certificado vencido significa que la calificación no está vigente. El acta se firma solo cuando todos los puntos están cumplidos, y la firma lleva fecha. Este caso es solo de lectura: nada de lo escrito aquí enseña a ejecutar la puesta en marcha.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("punto de detención", "punto que debe cumplirse antes de continuar; si está pendiente, la tarea se detiene"), ("punto pendiente", "punto de una lista que aún no se cumple"), ("lista de control", "lista de puntos que se verifican uno por uno"), ("calificación vigente", "certificado de la persona que no ha vencido"), ("supervisor", "persona que revisa que el trabajo se haga según lo exigido y lo libera")],
    worked=[
        ("Contar pendientes", "Un acta de ejemplo tiene 6 puntos y 4 están cumplidos. ¿Cuántos están pendientes?", ["Se restan los cumplidos del total.", "6 menos 4 son 2."], "2 puntos"),
        ("Detenerse", "En un acta de ejemplo el punto de detención 2 está pendiente y el resto está cumplido. ¿Se continúa?", ["Un punto de detención pendiente detiene la tarea.", "No importa que el resto esté cumplido."], "No: la tarea se detiene"),
    ],
    mistakes=[("Continuar porque «la mayoría de los puntos está cumplida».", "Un punto de detención pendiente impide continuar.", "Revisa primero los puntos de detención."),
              ("Marcar un punto como cumplido sin tener el documento.", "Es adulterar el acta y oculta un riesgo.", "Marca solo lo que está comprobado.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es un punto de detención en un acta?", "Un punto que debe cumplirse antes de continuar", "Un punto que se revisa el último día", "Un punto que ya fue cumplido", "Detención significa que, si está pendiente, la tarea no avanza."),
        ("abc", "¿Qué significa que un certificado esté vencido?", "Que la calificación de la persona no está vigente", "Que la persona se olvidó de firmarlo", "Que el certificado es muy antiguo y por eso mejor", "Un certificado vencido ya no acredita la calificación."),
        ("abc", "¿Qué hace quien lee un acta y encuentra un punto pendiente?", "Lo informa al supervisor o al profesional encargado", "Lo marca como cumplido para avanzar", "Lo cumple por su cuenta sin avisar", "Quien lee no decide cumplir un punto; informa a quien decide."),
        ("=", "{F} ¿Cuántos puntos del acta están cumplidos?", "8-3", "Se resta del total de puntos los tres que están pendientes.", " puntos"),
        ("abc", "{F} ¿Cuál de los puntos de detención está pendiente?", "El punto 4, certificado vigente del técnico", "El punto 2, instalación aprobada", "El punto 3, certificación eléctrica", "Los puntos 2 y 3 están cumplidos; el 4 está pendiente."),
        ("abc", "{F} ¿Por qué el punto 4 está pendiente?", "Porque el certificado del técnico venció hace un mes", "Porque falta la firma del cliente", "Porque la bitácora está cerrada", "La ficha indica que el certificado venció hace un mes."),
        ("=", "{F} Los puntos pendientes son 3. Si cada punto pendiente se resuelve en 2 días, ¿cuántos días toma resolver todos?", "3*2", "Se multiplica el número de puntos pendientes por los días de cada uno.", " días"),
        ("abc", "{F} ¿Se puede continuar con la puesta en marcha?", "No: un punto de detención está pendiente", "Sí: la mayoría de los puntos está cumplida", "Sí: el cliente tiene prisa", "Un punto de detención pendiente impide continuar, sin importar los demás."),
        ("abc", "{F} Un compañero propone marcar el punto 4 como cumplido «porque el técnico es bueno». ¿Qué respuesta es correcta?", "No: marcarlo sin certificado vigente sería adulterar el acta y ocultar un riesgo", "Sí: un buen técnico no necesita certificado", "Sí, si el supervisor no se entera", "El punto exige un certificado vigente, no la opinión sobre la persona."),
        ("abc", "{F} El supervisor pide una acción para resolver el punto 4. ¿Cuál corresponde?", "Que el técnico renueve su certificado o que lo reemplace otro técnico certificado", "Que el técnico trabaje con el certificado vencido en silencio", "Que otro ayudante sin certificación lo reemplace", "El requisito es una calificación vigente; solo se cumple con un certificado vigente."),
        ("abc", "{F} El punto 7 está pendiente: no hay valores del fabricante en el sitio. ¿Qué indica eso?", "Que no se continúa hasta tener los valores, porque no se usan de memoria", "Que se pueden usar los valores de otro equipo parecido", "Que se pueden recordar y anotar sin respaldo", "Los valores correctos están en el manual del fabricante, no en la memoria."),
        ("=", "{F} Cada día de retraso de la obra cuesta $80.000 de ejemplo. Si la renovación del certificado demora 3 días y conseguir los valores del fabricante agrega 1 día más, ¿cuánto cuesta el retraso?", "(3+1)*80000", "Se suman los días de retraso y se multiplican por el costo diario.", " pesos"),
        ("abc", "{F} El acta ya tiene la firma del profesional encargado, pero el punto 4 sigue pendiente. ¿Qué problema hay?", "La firma no corresponde, porque el acta se firma solo cuando todos los puntos están cumplidos", "Ninguno, porque la firma resuelve el punto", "Que la firma debe ser del cliente", "Una firma anticipada oculta un punto de detención pendiente."),
    ],
    ctx=("abc", "Un cliente de ejemplo pide que se ponga en marcha el sistema hoy aunque el certificado del técnico venció. ¿Qué responde el supervisor?", "Que no se continúa hasta tener un técnico con certificado vigente", "Que se continúa si el cliente firma un permiso", "Que se continúa si el técnico promete renovarlo", "Un permiso del cliente no reemplaza un requisito de calificación."),
    sc=[
        ("En Refrigeración: ¿qué es un punto de detención?", "Un punto que debe cumplirse antes de continuar", "Si está pendiente, la tarea se detiene."),
        ("¿Cuándo se firma un acta de puesta en marcha?", "Cuando todos los puntos están cumplidos", "Una firma anticipada puede ocultar puntos pendientes de cumplir."),
        ("¿Qué se hace con un punto pendiente?", "Se informa al supervisor o al profesional encargado", "Quien lee no decide cumplirlo por su cuenta."),
    ],
    op=("Acta de ejemplo de la «Panadería Maqui» (ficticia), 6 puntos: 1 documentos revisados (cumplido); 2 instalación aprobada (cumplido); 3 certificación eléctrica archivada (pendiente); 4 técnico con certificado vigente (cumplido); 5 bitácora abierta (cumplido); 6 firma del profesional encargado (pendiente). Puntos de detención: 2, 3 y 4. "
        "Escribe (a) cuántos puntos están pendientes, (b) si se puede continuar y por qué, (c) qué haces con el punto 3, (d) cuándo se firma el punto 6.",
        "(a) 2 pendientes: el 3 y el 6. (b) No se puede continuar, porque el punto de detención 3 está pendiente. (c) Lo informo al supervisor o al profesional encargado, que decide; no lo marco como cumplido. (d) Cuando todos los puntos estén cumplidos.",
        ["cuenta los pendientes", "explica por qué se detiene", "informa en vez de decidir", "indica cuándo se firma"],
        ["hoja con las cuatro respuestas"],
        ["marcar el punto 3 como cumplido", "continuar por mayoría de puntos", "firmar antes de tiempo"],
        "Pregunta: «¿por qué no se continúa si solo faltan dos puntos?». Si no responde, pídele que relea la regla de los puntos de detención."),
    reinforce="Inventa un acta de seis puntos con dos puntos de detención y marca cuáles están pendientes.",
    extend="Explica con un ejemplo por qué una firma anticipada en un acta puede ocultar un riesgo.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados). Un sistema tiene una carga nominal de 20 kg según su placa. La bitácora registra reposiciones de refrigerante por fuga en el año: 1 kg en marzo y 2 kg en septiembre. "
     "El fluido «Alfa» (ficticio) tiene un índice de calentamiento global (PCG) de ejemplo de 400 y el fluido «Beta» (ficticio), de 100. Criterio de ejemplo de la empresa: si la fuga anual supera el 10 % de la carga nominal, se pide una revisión por personal autorizado. "
     "Equivalente en dióxido de carbono = kg fugados × PCG.")
build(
    O6, 4, F,
    use="Aprenderé a leer una bitácora de reposiciones, a calcular la fuga anual como porcentaje de la carga, el equivalente ambiental y a decidir cuándo pedir una revisión.",
    prior=["Sé qué es la carga nominal.", "Sé calcular porcentajes sencillos.", "Sé qué es el PCG."],
    explain=[
        "La bitácora registra las reposiciones de refrigerante: para este cálculo, cada kilo que se agrega después de la carga inicial se considera un kilo perdido por fuga. La fuga anual es la suma de las reposiciones del año. Para compararla con la carga nominal se calcula un porcentaje: la fuga dividida por la carga, multiplicada por 100. Si supera el límite que fija el criterio de la empresa o la norma vigente, se pide una revisión por personal autorizado; quien lee la bitácora no intenta repararla.",
        "El impacto ambiental de una fuga se estima multiplicando los kilos fugados por el índice de calentamiento global (PCG) del fluido. Así dos sistemas con la misma fuga pueden tener impactos muy distintos si usan fluidos con PCG distinto. Estos cálculos son de planilla con datos de ejemplo; los valores reales de carga, límites e índices los entregan el fabricante y la norma vigente.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("reposición", "refrigerante que se agrega después de la carga inicial"), ("fuga anual", "suma de las reposiciones de refrigerante de un año"), ("porcentaje de fuga", "fuga dividida por la carga nominal, multiplicada por 100"), ("equivalente en dióxido de carbono", "kilos fugados multiplicados por el índice de calentamiento global"), ("criterio de revisión", "regla que dice cuándo se pide una revisión por personal autorizado")],
    worked=[
        ("Porcentaje de fuga", "Un sistema de ejemplo tiene una carga de 40 kg y repuso 2 kg en el año. ¿Qué porcentaje de fuga es?", ["2 dividido por 40 es 0,05.", "Multiplicado por 100 es 5 %."], "5 %"),
        ("Equivalente ambiental", "Una fuga de ejemplo de 4 kg de un fluido con PCG 250. ¿Cuántos kg de dióxido de carbono equivale?", ["Se multiplican los kg por el PCG.", "4 por 250 son 1.000."], "1.000 kg"),
    ],
    mistakes=[("Contar solo la carga inicial y olvidar las reposiciones de la bitácora.", "Las reposiciones indican cuánto se perdió por fuga.", "Suma todas las reposiciones del año."),
              ("Intentar reparar el sistema al ver un porcentaje de fuga alto.", "Esa tarea la hace personal autorizado.", "Informa y pide la revisión.")],
    T=[
        ("abc", "En Refrigeración: ¿qué indica una reposición de refrigerante en la bitácora?", "Que se agregó fluido después de la carga inicial porque se había perdido", "Que se cambió el equipo completo", "Que se limpió el filtro del aire", "Una reposición significa que se repuso refrigerante perdido por fuga."),
        ("abc", "¿Qué es la fuga anual?", "La suma de las reposiciones de refrigerante de un año", "La carga nominal de la placa", "El consumo de energía del año", "La fuga anual se calcula sumando las reposiciones del año."),
        ("abc", "¿Qué hace quien lee la bitácora si el porcentaje de fuga supera el criterio?", "Pide una revisión por personal autorizado", "Intenta reparar el sistema", "Agrega refrigerante por su cuenta", "Quien lee la bitácora informa y pide revisión; no repara."),
        ("=", "{F} ¿Cuántos kg suma la fuga anual?", "1+2", "Se suman las reposiciones de marzo y de septiembre.", " kg"),
        ("=", "{F} ¿Qué porcentaje de la carga nominal es la fuga anual?", "(1+2)*100//20", "Se divide la fuga por la carga nominal y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos kg de fuga corresponden al 10 % de la carga nominal?", "20*10//100", "Se calcula el 10 % de la carga nominal.", " kg"),
        ("abc", "{F} Según el criterio de ejemplo, ¿qué corresponde hacer?", "Pedir una revisión por personal autorizado, porque la fuga supera el 10 %", "No hacer nada, porque la fuga es pequeña", "Cargar más fluido por cuenta propia", "La fuga anual supera el 10 % de la carga nominal, por lo que se pide revisión."),
        ("=", "{F} Si el sistema usa el fluido Alfa, ¿cuántos kg de dióxido de carbono equivale la fuga anual?", "(1+2)*400", "Se multiplican los kg fugados por el PCG del fluido Alfa.", " kg"),
        ("=", "{F} Si el sistema usara el fluido Beta, ¿cuántos kg de dióxido de carbono equivaldría la misma fuga anual?", "(1+2)*100", "Se multiplican los kg fugados por el PCG del fluido Beta.", " kg"),
        ("=", "{F} ¿Cuántos kg de dióxido de carbono menos se emiten con Beta que con Alfa en esa fuga anual?", "(1+2)*400-(1+2)*100", "Se resta el equivalente con Beta del equivalente con Alfa.", " kg"),
        ("abc", "{F} Un compañero dice: «como Beta tiene menos PCG, es la mejor opción en todo». ¿Qué respuesta es correcta?", "No necesariamente: el PCG es un criterio; también cuentan la seguridad, el costo y la norma vigente", "Sí: un PCG menor es siempre mejor", "Sí, porque los demás criterios no importan", "El impacto ambiental es un criterio entre varios que deben evaluarse."),
        ("=", "{F} Si la fuga del año pasara de 3 kg a 4 kg, ¿en cuántos puntos porcentuales sube respecto de la carga nominal?", "4*100//20-3*100//20", "Se calcula el porcentaje con 4 kg y se resta el de 3 kg.", " puntos"),
        ("abc", "{F} Un ayudante ve el porcentaje de fuga y propone «agregar un poco de fluido para compensar». ¿Qué corresponde?", "No hacerlo: eso lo hace un técnico certificado después de una revisión", "Hacerlo con guantes y lentes", "Hacerlo si el equipo no está funcionando", "Agregar fluido es una tarea de personal certificado que no se improvisa."),
    ],
    ctx=("abc", "Una supervisora de ejemplo recibe una bitácora con reposiciones que nadie firmó. ¿Qué hace?", "Pide que se identifique al responsable de cada reposición antes de analizar los datos", "Las da por buenas porque están escritas", "Las descarta y empieza otro registro sin avisar", "Un registro sin responsable no tiene trazabilidad y se completa antes de usarlo."),
    sc=[
        ("En Refrigeración: ¿cómo se calcula el porcentaje de fuga?", "Fuga dividida por la carga nominal, multiplicada por 100", "Así se compara la fuga con el tamaño del sistema."),
        ("¿Cómo se calcula el equivalente en dióxido de carbono?", "Multiplicando los kg fugados por el PCG", "Un PCG mayor significa más impacto por cada kg."),
        ("¿Quién repone refrigerante tras una fuga?", "Un técnico certificado, después de una revisión", "Este cuaderno no habilita para trabajar ni para intervenir equipos."),
    ],
    op=("Datos de ejemplo del «Sistema Coigüe» (ficticio): carga nominal de 25 kg; reposiciones del año: 2 kg en abril y 3 kg en octubre; fluido con PCG de ejemplo 200; criterio: se pide revisión si la fuga supera el 10 % de la carga. "
        "Escribe (a) la fuga anual, (b) el porcentaje de la carga, (c) si se pide revisión y por qué, (d) los kg de dióxido de carbono que equivale la fuga.",
        "(a) 2 más 3 son 5 kg. (b) 5 por 100 dividido por 25 son 20 %. (c) Sí, porque 20 % supera el 10 % del criterio; se pide una revisión por personal autorizado. (d) 5 por 200 son 1.000 kg.",
        ["suma las reposiciones", "calcula el porcentaje", "aplica el criterio", "calcula el equivalente ambiental"],
        ["hoja con los cálculos"],
        ["usar solo una reposición", "dividir al revés", "decidir reparar en vez de pedir revisión"],
        "Pregunta: «¿qué haces si supera el criterio?». Si no responde, pídele que relea la regla de pedir revisión."),
    reinforce="Inventa una bitácora con tres reposiciones y calcula la fuga anual y su porcentaje de una carga que elijas.",
    extend="Explica con un ejemplo por qué una misma fuga puede tener impacto ambiental distinto según el fluido.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (alternativas de ejemplo, inventadas; los tres fluidos son ficticios). Alfa: índice de calentamiento global (PCG) de ejemplo 400; no inflamable; $20.000 por kg. Beta: PCG 100; inflamable (exige medidas adicionales y técnicos capacitados); $25.000 por kg. "
     "Gamma: PCG 1.500; no inflamable; $12.000 por kg. Puntajes de 1 a 5 (5 es lo mejor), ambiente / seguridad / costo: Alfa 3 / 5 / 3; Beta 5 / 2 / 2; Gamma 1 / 5 / 5. Pesos: ambiente 3, seguridad 3, costo 1. "
     "Registro de ejemplo de una puesta en marcha: se compararon 3 valores con el rango del manual del fabricante y 2 estaban dentro del rango.")
build(
    O6, 5, F,
    use="Aprenderé a comparar fluidos refrigerantes por ambiente, seguridad y costo con una matriz, y a verificar que un registro de puesta en marcha cumple lo que indica el fabricante.",
    prior=["Sé calcular un puntaje ponderado.", "Sé qué es el PCG.", "Sé qué es un acta de puesta en marcha."],
    explain=[
        "Elegir un refrigerante es comparar criterios: el impacto ambiental, que mide el PCG; la seguridad, que incluye la inflamabilidad; y el costo. Cada fluido recibe un puntaje en cada criterio, se multiplica por el peso y se suma. El fluido de mayor puntaje es una propuesta, pero la elección la aprueba el profesional encargado, porque debe ser compatible con el equipo y con la norma vigente: no todo fluido sirve en todo equipo.",
        "Para verificar la puesta en marcha se compara cada valor registrado con el rango del manual del fabricante. Si un valor está fuera del rango, no se continúa: se detiene el trabajo, se informa al supervisor y se espera la decisión de personal autorizado. El porcentaje de valores dentro de rango resume el resultado, pero un valor fuera de rango siempre se trata. Los valores reales de presiones y fuerzas los da el fabricante.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("criterio", "característica que se usa para comparar alternativas"), ("inflamable", "que puede encenderse y quemar; exige medidas adicionales"), ("compatible", "que puede usarse en un equipo según el fabricante y la norma vigente"), ("rango del fabricante", "intervalo de valores correctos que indica el manual del equipo"), ("puntaje ponderado", "suma de cada puntaje multiplicado por el peso de su criterio")],
    worked=[
        ("Puntaje ponderado", "El fluido Mu (ficticio) tiene puntajes 4 en ambiente (peso 2) y 5 en seguridad (peso 3). ¿Cuál es su puntaje ponderado?", ["4 por 2 son 8 y 5 por 3 son 15.", "8 más 15 son 23."], "23 puntos"),
        ("Valor fuera de rango", "El manual de ejemplo da un rango de 10 a 20 para una magnitud y el registro marca 22. ¿Qué se hace?", ["22 está fuera del rango.", "Se detiene, se informa al supervisor y decide personal autorizado."], "Se detiene y se informa; decide personal autorizado"),
    ],
    mistakes=[("Elegir el fluido de menor PCG sin considerar la seguridad ni el equipo.", "Puede no ser compatible o exigir medidas adicionales.", "Compara todos los criterios y consulta al profesional encargado."),
              ("Seguir adelante cuando un valor registrado está fuera del rango.", "Puede indicar un problema de seguridad o de funcionamiento.", "Detén el trabajo e informa al supervisor.")],
    T=[
        ("abc", "En Refrigeración: ¿qué significa que un fluido sea inflamable?", "Que puede encenderse y quemar, por lo que exige medidas adicionales", "Que se congela con facilidad", "Que su precio cambia cada mes", "Inflamable se refiere a que puede encenderse; el precio o la congelación son otras propiedades."),
        ("abc", "¿Qué significa que un fluido sea compatible con un equipo?", "Que puede usarse en ese equipo según el fabricante y la norma vigente", "Que cuesta lo mismo que los demás", "Que tiene el mismo color que el anterior", "Compatible quiere decir apto para ese equipo, según el fabricante y la norma."),
        ("abc", "¿Qué es el rango del fabricante?", "El intervalo de valores correctos que indica el manual del equipo", "El rango de precios de los repuestos", "El horario en que se debe usar el equipo", "El rango del fabricante define los valores correctos de cada magnitud."),
        ("=", "{F} ¿Cuál es el puntaje ponderado del fluido Alfa?", "3*3+5*3+3*1", "Cada puntaje de Alfa se multiplica por el peso de su criterio y se suma.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje ponderado del fluido Beta?", "5*3+2*3+2*1", "Cada puntaje de Beta se multiplica por el peso de su criterio y se suma.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje ponderado del fluido Gamma?", "1*3+5*3+5*1", "Cada puntaje de Gamma se multiplica por el peso de su criterio y se suma.", " puntos"),
        ("abc", "{F} Según los puntajes ponderados, ¿qué fluido aparece primero?", "Alfa, con 27 puntos", "Beta, con 23 puntos", "Gamma, con 23 puntos", "Alfa suma 27 y Beta y Gamma suman 23 cada uno."),
        ("=", "{F} ¿Cuánto cuestan 10 kg del fluido Alfa?", "10*20000", "Se multiplica el precio por kg por los kilos.", " pesos"),
        ("=", "{F} ¿Cuánto menos cuestan 10 kg de Gamma que 10 kg de Alfa?", "10*20000-10*12000", "Se resta el costo de 10 kg de Gamma del de Alfa.", " pesos"),
        ("abc", "{F} Un compañero propone Beta porque su PCG es el menor, y descarta que es inflamable. ¿Qué respuesta es correcta?", "No se puede descartar la inflamabilidad: exige medidas adicionales y técnicos capacitados", "Beta es siempre la mejor, porque el ambiente es lo único que importa", "La inflamabilidad no importa si el técnico usa guantes", "La seguridad es un criterio con el mismo peso que el ambiente en esta matriz."),
        ("abc", "{F} Se calcula que Gamma es la más barata. ¿Por qué no aparece primera?", "Porque su PCG es muy alto y el ambiente pesa más que el costo", "Porque cuesta más que Alfa", "Porque es inflamable", "Gamma tiene el menor puntaje ambiental, y el ambiente pesa 3 contra 1 del costo."),
        ("=", "{F} Si el peso del costo subiera de 1 a 4, ¿cuál sería el nuevo puntaje ponderado de Gamma?", "1*3+5*3+5*4", "Se repite la suma de Gamma con el nuevo peso del costo.", " puntos"),
        ("abc", "{F} En el registro de la puesta en marcha, 1 de 3 valores quedó fuera del rango del manual. ¿Qué corresponde?", "Detener el trabajo, informar al supervisor y esperar la decisión de personal autorizado", "Continuar, porque 2 de 3 valores están bien", "Cambiar el valor fuera de rango para que entre", "Un valor fuera de rango se trata siempre; el porcentaje de valores buenos no lo compensa."),
    ],
    ctx=("abc", "Una técnica de ejemplo ve que una lectura de la puesta en marcha quedó fuera del rango del manual y el cliente insiste en entregar hoy. ¿Qué hace?", "Detiene la entrega, registra la lectura e informa al supervisor", "Entrega igual y avisa después", "Cambia la lectura en el registro para cumplir", "Una lectura fuera de rango se informa; el apuro del cliente no cambia el requisito."),
    sc=[
        ("En Refrigeración: ¿qué criterios se comparan al elegir un fluido?", "Ambiente, seguridad y costo, entre otros", "La elección final la aprueba el profesional encargado."),
        ("¿Qué se hace con un valor fuera del rango del fabricante?", "Se detiene el trabajo y se informa al supervisor", "El porcentaje de valores buenos no lo compensa."),
        ("¿Quién aprueba el fluido que se usará?", "El profesional encargado", "Debe ser compatible con el equipo y la norma vigente."),
    ],
    op=("Alternativas de ejemplo (fluidos ficticios) para el «Taller Radal»: fluido P, PCG 300, no inflamable, $18.000 por kg, puntajes ambiente / seguridad / costo = 3 / 5 / 3; fluido Q, PCG 80, inflamable, $24.000 por kg, puntajes 5 / 2 / 2. Pesos: ambiente 2, seguridad 3, costo 1. Se necesitan 5 kg. "
        "Escribe (a) el puntaje ponderado de cada fluido, (b) el costo de 5 kg de cada uno, (c) qué fluido propones y quién aprueba, (d) qué haces si un valor registrado queda fuera del rango del fabricante.",
        "(a) P: 3 por 2 más 5 por 3 más 3 por 1 son 24. Q: 5 por 2 más 2 por 3 más 2 por 1 son 18. (b) P: 5 por 18.000 son 90.000. Q: 5 por 24.000 son 120.000. (c) Propongo P por su mayor puntaje; lo aprueba el profesional encargado. (d) Detengo el trabajo, registro el valor e informo al supervisor.",
        ["calcula los puntajes", "calcula los costos", "propone y nombra quién aprueba", "detiene e informa ante un valor fuera de rango"],
        ["hoja con los cálculos y la propuesta"],
        ["olvidar el peso", "decidir sin el profesional encargado", "seguir con un valor fuera de rango"],
        "Pregunta: «¿quién aprueba el fluido?». Si no responde, pídele que relea la regla de compatibilidad y aprobación."),
    reinforce="Inventa dos fluidos ficticios con puntajes en tres criterios y calcula cuál tiene el mayor puntaje ponderado.",
    extend="Explica con un ejemplo por qué el fluido de mejor puntaje ambiental no siempre es el que se elige.",
)

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (orden de servicio de ejemplo, inventada). Un restaurante ficticio reporta que su aire acondicionado «no enfría bien» y que «a veces hace un ruido fuerte». "
     "Datos de la orden: equipo de 8 kW; antigüedad de 6 años; última mantención hace 14 meses; el plan del fabricante pide una mantención cada 6 meses.")
build(
    O7, 1, F,
    use="Aprenderé la diferencia entre síntoma, falla y causa, qué es inspeccionar y diagnosticar, y por qué la seguridad va primero.",
    prior=["Sé qué es un manual del fabricante.", "Sé qué es una bitácora.", "Sé restar y dividir."],
    explain=[
        "Inspeccionar es revisar un equipo con método y registrar lo que se observa. Diagnosticar es encontrar la causa de una falla comparando lo observado con las especificaciones del fabricante. El síntoma es lo que se nota, como «no enfría bien» o un ruido. La falla es lo que no funciona como debería, y la causa es la razón por la que ocurre. Una orden de servicio registra el pedido del cliente y los datos del equipo: es el punto de partida del diagnóstico.",
        "La seguridad va primero. Inspeccionar un equipo real lo hace personal autorizado, con norma vigente y EPP, porque hay energía eléctrica, presión y partes que giran. Hay señales de peligro: olor a quemado, humo, chispas, hielo grueso o ruidos muy fuertes. Ante ellas nadie se acerca ni toca: se avisa a un adulto responsable y a emergencias. Un dato como la antigüedad ayuda, pero no es una causa por sí solo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("síntoma", "lo que se nota de un equipo, como «no enfría bien» o un ruido"), ("falla", "lo que no funciona como debería"), ("causa", "razón por la que ocurre una falla"), ("inspeccionar", "revisar un equipo con método y registrar lo observado"), ("diagnosticar", "encontrar la causa de una falla comparando lo observado con las especificaciones del fabricante"), ("orden de servicio", "documento que registra el pedido del cliente y los datos del equipo")],
    worked=[
        ("Síntoma o causa", "Un cliente de ejemplo dice: «el equipo hace mucho ruido». ¿Es un síntoma o una causa?", ["Lo que el cliente nota es un síntoma.", "La causa todavía no se conoce."], "Es un síntoma"),
        ("Mantenciones atrasadas", "Un plan de ejemplo pide una mantención cada 4 meses y la última fue hace 10 meses. ¿Cuántas mantenciones completas debieron hacerse?", ["Se divide el tiempo por el intervalo.", "10 dividido por 4 son 2 completas."], "2 mantenciones"),
    ],
    mistakes=[("Dar por causa el síntoma que cuenta el cliente.", "El síntoma es lo que se nota; la causa se establece comparando con el fabricante.", "Registra el síntoma y busca la causa con datos."),
              ("Acercarse a un equipo que huele a quemado «para ver qué pasa».", "Hay riesgo de descarga o incendio.", "No te acerques; avisa a un adulto responsable.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es un síntoma de un equipo?", "Lo que se nota, como «no enfría bien»", "La pieza que debe cambiarse", "El documento que ordena la reparación", "El síntoma es lo que se percibe; la pieza o el documento son otras cosas."),
        ("abc", "¿Qué es la causa de una falla?", "La razón por la que ocurre el problema", "Lo que el cliente dice al llamar", "El precio de la reparación", "La causa explica por qué ocurre la falla; lo que se dice al llamar es el síntoma."),
        ("abc", "¿Qué registra una orden de servicio?", "El pedido del cliente y los datos del equipo", "El resultado final de la reparación", "El precio del equipo nuevo", "La orden de servicio abre el caso con el pedido y los datos del equipo."),
        ("=", "{F} ¿Cuántos meses de atraso lleva la mantención respecto del plan de 6 meses?", "14-6", "Se resta el intervalo del plan del tiempo transcurrido.", " meses"),
        ("=", "{F} ¿Cuántas mantenciones completas debieron hacerse en los últimos 14 meses?", "14//6", "Se divide el tiempo transcurrido por el intervalo del plan.", " mantenciones"),
        ("abc", "{F} ¿Cuál es el síntoma que reporta el cliente?", "El equipo no enfría bien y a veces hace un ruido fuerte", "El compresor está dañado", "El equipo tiene 6 años", "Lo que reporta el cliente es lo que nota; la antigüedad es un dato y el daño del compresor sería una causa."),
        ("abc", "{F} ¿Qué dato de la orden sugiere revisar el cumplimiento del plan de mantención?", "La última mantención fue hace 14 meses y el plan pide cada 6", "El equipo es de 8 kW", "El cliente es un restaurante", "La diferencia entre 14 y 6 meses muestra un posible incumplimiento del plan."),
        ("=", "{F} Con el plan de 2 mantenciones al año, ¿cuántas habría pedido el plan en los 6 años de antigüedad del equipo?", "6*2", "Se multiplican los años de antigüedad por las mantenciones de cada año.", " mantenciones"),
        ("abc", "{F} El cliente avisa que el equipo huele a quemado y hace chispas. ¿Qué indican las reglas generales?", "No acercarse ni tocar, avisar a un adulto responsable y llamar a emergencias", "Acercarse a mirar de dónde sale el olor", "Apagar y desarmar el equipo para revisarlo", "Con olor a quemado o chispas hay riesgo de incendio o descarga; se avisa y no se interviene."),
        ("abc", "{F} Un compañero dice: «el equipo es viejo, esa es la causa». ¿Qué respuesta es correcta?", "La antigüedad es un dato, pero la causa se establece comparando lo observado con el fabricante", "Es correcto: la antigüedad siempre es la causa", "Es correcto si el cliente está de acuerdo", "Un dato como la antigüedad no prueba la causa; esta se comprueba con observaciones."),
        ("ab", "{F} Una estudiante que leyó el manual dice que puede abrir el equipo para diagnosticar. ¿Es correcto?", "No: inspeccionar un equipo real lo hace personal autorizado", "Sí: haber leído el manual la habilita", "Leer un manual no reemplaza la autorización, la norma vigente ni la protección."),
        ("=", "{F} Cada visita de diagnóstico de ejemplo cuesta $40.000 y el informe $90.000. Con 2 visitas y un informe, ¿cuánto cuesta?", "2*40000+90000", "Se suman el costo de las dos visitas y el del informe.", " pesos"),
        ("abc", "{F} La orden dice que la última mantención fue hace 14 meses, pero la bitácora del equipo dice hace 9 meses. ¿Qué corresponde?", "Anotar la diferencia y consultar al responsable de la bitácora antes de diagnosticar", "Usar el dato que dé menos atraso", "Borrar uno de los dos datos", "Una diferencia entre documentos se anota y se aclara antes de seguir."),
    ],
    ctx=("abc", "Un cliente de ejemplo llama a un estudiante y le pide que «mire el equipo» porque saca humo. ¿Qué responde?", "Que no se acerque ni toque el equipo y avise a un adulto responsable y a emergencias", "Que lo apague desde el tablero", "Que lo abra para ver el origen", "Con humo no se interviene ni se acerca nadie sin autorización."),
    sc=[
        ("En Refrigeración: ¿qué es diagnosticar?", "Encontrar la causa de una falla comparando con las especificaciones del fabricante", "El diagnóstico se apoya en datos y no en suposiciones."),
        ("En refrigeración: ¿qué diferencia hay entre síntoma y causa?", "El síntoma es lo que se nota y la causa es la razón de la falla", "Un mismo síntoma puede tener causas distintas."),
        ("¿Quién inspecciona un equipo real?", "Personal autorizado, con norma vigente y EPP", "Este cuaderno no habilita para trabajar ni para intervenir equipos."),
    ],
    op=("Orden de servicio de ejemplo del «Café Hualle» (ficticio): el cliente reporta que el equipo «sopla aire tibio»; equipo de 6 kW; última mantención hace 18 meses; el plan del fabricante pide una cada 6 meses. "
        "Escribe (a) el síntoma, (b) cuántas mantenciones completas debieron hacerse, (c) por qué la antigüedad o el atraso no bastan para afirmar la causa, (d) qué haces si el cliente dice que el equipo huele a quemado.",
        "(a) El equipo sopla aire tibio. (b) 18 dividido por 6 son 3 mantenciones. (c) Son datos que sugieren una hipótesis, pero la causa se comprueba comparando lo observado con las especificaciones del fabricante. (d) No me acerco ni toco el equipo y aviso a un adulto responsable y a emergencias.",
        ["identifica el síntoma", "calcula las mantenciones", "distingue dato y causa", "aplica la regla de seguridad"],
        ["hoja con las cuatro respuestas"],
        ["confundir síntoma con causa", "dividir al revés", "decir que revisaría el equipo"],
        "Pregunta: «¿qué haces si huele a quemado?». Si no responde, pídele que relea la regla de las señales de peligro."),
    reinforce="Escribe tres síntomas que un cliente podría reportar y, junto a cada uno, una pregunta que ayudaría a buscar su causa.",
    extend="Explica con un ejemplo por qué dos equipos con el mismo síntoma pueden tener causas distintas.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (tabla de códigos y informe de ejemplo, inventados). Tabla de un fabricante ficticio: E1 = sensor de temperatura con lectura fuera de rango; E2 = filtro de aire con obstrucción; E3 = protección del compresor activada; E4 = comunicación entre unidades interrumpida. "
     "Informe de ejemplo: el equipo muestra E2 desde hace 3 días; el cliente dice que limpia el filtro una vez al año; el plan del fabricante pide limpiarlo cada 3 meses; el equipo consume 8 kWh extra por día por el filtro obstruido.")
build(
    O7, 2, F,
    use="Aprenderé a leer una tabla de códigos de error y un informe de inspección, a distinguir hechos de opiniones y a reconocer los roles.",
    prior=["Sé la diferencia entre síntoma y causa.", "Sé qué es un manual del fabricante.", "Sé qué es adulterar un registro."],
    explain=[
        "Un código de error es un mensaje del equipo que indica qué tipo de falla detectó. Su significado está en el manual del fabricante, en una tabla de códigos; nadie lo adivina ni lo toma de otra marca. El informe de inspección es el documento donde se anotan lo observado, quién lo observó, cuándo, las conclusiones y las recomendaciones. Un hecho es algo observable o medible, como un código en pantalla; una opinión es una creencia, como «el equipo está malo». Un buen informe separa los hechos de las opiniones.",
        "Los roles son distintos. El cliente cuenta los síntomas, el técnico autorizado inspecciona y registra, y el supervisor revisa que las conclusiones tengan respaldo. Una recomendación sin hechos que la respalden no es un diagnóstico. Cambiar un dato de un informe para que parezca más grave o más leve es adulterar un registro, una falta grave. El historial del equipo, que reúne órdenes y bitácoras anteriores, ayuda a ver si el problema se repite.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("código de error", "mensaje del equipo que indica qué tipo de falla detectó"), ("informe de inspección", "documento que anota lo observado, quién, cuándo, conclusiones y recomendaciones"), ("hecho", "algo observable o medible"), ("opinión", "creencia que no está comprobada con datos"), ("historial del equipo", "conjunto de órdenes y bitácoras anteriores de un equipo"), ("recomendación", "propuesta de acción apoyada en lo observado")],
    worked=[
        ("Hecho u opinión", "Un informe de ejemplo dice: «la pantalla muestra el código E7». ¿Es un hecho o una opinión?", ["Se puede observar en la pantalla.", "Por eso es un hecho."], "Es un hecho"),
        ("Frecuencia de limpieza", "Un plan de ejemplo pide limpiar un filtro cada 2 meses. ¿Cuántas limpiezas pide en un año?", ["Un año tiene 12 meses.", "12 dividido por 2 son 6."], "6 limpiezas"),
    ],
    mistakes=[("Tomar el significado de un código de otra marca.", "Cada fabricante tiene su propia tabla.", "Busca el código en el manual del equipo."),
              ("Mezclar opiniones con hechos en el informe.", "Un informe con opiniones sin respaldo puede llevar a decisiones equivocadas.", "Anota por separado lo observado y lo que se supone.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es un código de error?", "Un mensaje del equipo que indica qué tipo de falla detectó", "Un número de serie del equipo", "El código del técnico que lo instaló", "El código de error describe una falla detectada; no es serie ni identificador del técnico."),
        ("abc", "¿Qué debe contener un informe de inspección?", "Lo observado, quién lo hizo, cuándo y qué se recomienda", "Solo la opinión del técnico sobre el cliente", "Solo el precio de la reparación", "El informe registra observaciones, responsables, fechas y recomendaciones."),
        ("abc", "¿Dónde se busca el significado de un código de error?", "En la tabla de códigos del manual del fabricante", "En el manual de otra marca parecida", "En la memoria del técnico", "Cada fabricante define sus códigos y los publica en su manual."),
        ("abc", "{F} ¿Qué significa el código E3 de la tabla?", "La protección del compresor está activada", "El filtro de aire está obstruido", "La comunicación entre unidades se interrumpió", "La tabla asigna E3 a la protección del compresor activada."),
        ("abc", "{F} ¿Qué código muestra el equipo del informe y qué indica?", "E2, filtro de aire con obstrucción", "E1, sensor fuera de rango", "E4, comunicación interrumpida", "El informe dice E2, que la tabla asocia a un filtro obstruido."),
        ("=", "{F} ¿Cuántas limpiezas del filtro pide el plan del fabricante en un año?", "12//3", "Se divide el año en meses por el intervalo del plan.", " limpiezas"),
        ("=", "{F} El cliente limpia el filtro una vez al año. ¿Cuántas limpiezas al año le faltan?", "12//3-1", "Se resta la limpieza que sí hace de las que pide el plan.", " limpiezas"),
        ("abc", "{F} El cliente dice que el equipo «está malo». ¿Qué tipo de dato es?", "Una opinión, que debe contrastarse con hechos observados", "Un hecho medido", "Un código del fabricante", "«Está malo» es una creencia general; no es un dato observable ni un código."),
        ("=", "{F} Con 8 kWh extra por día, ¿cuántos kWh extra consumió el equipo en los 3 días con E2?", "8*3", "Se multiplica el consumo extra diario por los días.", " kWh"),
        ("abc", "{F} Un compañero cambia «E2» por «E3» en el informe porque «suena más grave». ¿Qué es eso?", "Adulterar un registro, una falta grave", "Mejorar la redacción del informe", "Una práctica aceptable si lo hace el técnico", "Cambiar un hecho observado para exagerarlo falsea el registro."),
        ("abc", "{F} Otro informe dice que el equipo muestra E4 y que «el sensor está malo». ¿Qué corresponde según la tabla?", "Registrar que E4 indica comunicación interrumpida y que la causa del sensor no está comprobada", "Registrar que E4 indica un sensor malo", "Eliminar el código del informe", "La tabla asocia E4 con la comunicación, no con un sensor."),
        ("=", "{F} Si durante 2 años se omitieron todos los años las limpiezas que le faltaban al cliente, ¿cuántas limpiezas se omitieron?", "(12//3-1)*2", "Se multiplican las limpiezas omitidas por año por los 2 años.", " limpiezas"),
        ("abc", "{F} Un informe recomienda «cambiar el compresor», pero no tiene ninguna observación que lo respalde. ¿Qué problema hay?", "Una conclusión sin hechos que la respalden no es un diagnóstico", "Ninguno, porque el técnico sabe más", "Que la recomendación debió ser más barata", "Un diagnóstico se apoya en hechos; una recomendación sin respaldo es una suposición."),
    ],
    ctx=("abc", "Un supervisor de ejemplo lee un informe que mezcla «el filtro está sucio» (observado) con «seguro que el compresor está dañado» (suposición). ¿Qué pide?", "Que separen lo observado de lo supuesto y que las conclusiones tengan respaldo", "Que el informe se entregue tal como está", "Que se borren las observaciones y quede la suposición", "Un informe confiable distingue hechos y suposiciones."),
    sc=[
        ("En Refrigeración: ¿dónde está el significado de un código de error?", "En el manual del fabricante del equipo", "Cada marca tiene su propia tabla."),
        ("En refrigeración: ¿qué diferencia hay entre un hecho y una opinión?", "El hecho se puede observar o medir y la opinión no está comprobada", "Un buen informe separa los hechos de las opiniones."),
        ("¿Qué es adulterar un registro?", "Cambiar un dato registrado para que parezca otra cosa", "Es una falta grave que oculta riesgos."),
    ],
    op=("Tabla de ejemplo de un fabricante ficticio: F1 = sensor de humedad fuera de rango; F2 = filtro obstruido; F3 = protección del ventilador activada. Informe de ejemplo del «Gimnasio Olmué»: el equipo muestra F2 desde hace 5 días; el cliente limpia el filtro cada 6 meses; el plan pide limpiarlo cada 2 meses; consumo extra de ejemplo de 6 kWh por día. El cliente dice que «el equipo está malo». "
        "Escribe (a) qué indica el código, (b) cuántas limpiezas pide el plan al año y cuántas hace el cliente, (c) los kWh extra en los 5 días, (d) un hecho y una opinión del informe.",
        "(a) F2 indica un filtro obstruido. (b) El plan pide 12 dividido por 2, o sea 6 limpiezas al año; el cliente hace 12 dividido por 6, o sea 2. (c) 6 por 5 son 30 kWh. (d) Hecho: el equipo muestra F2 desde hace 5 días; opinión: «el equipo está malo», que no está comprobada.",
        ["interpreta el código", "compara frecuencias", "calcula el consumo extra", "distingue hecho y opinión"],
        ["hoja con las cuatro respuestas"],
        ["usar la tabla de otra marca", "dividir al revés", "mezclar hechos con opiniones"],
        "Pregunta: «¿cuál de tus frases es un hecho y cuál una opinión?». Si no responde, pídele que relea la diferencia."),
    reinforce="Escribe dos hechos y dos opiniones sobre un equipo que no enfría bien, y márcalos.",
    extend="Explica con un ejemplo por qué el historial de un equipo ayuda a encontrar causas que se repiten.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado, equipo ficticio). Bitácora: mes 1, limpieza del filtro, consumo 400 kWh; mes 4, consumo 420 kWh; mes 8, consumo 480 kWh; mes 12, consumo 560 kWh y el cliente reporta que «no enfría». "
     "El informe de inspección registra una diferencia de temperatura del aire (ΔT) de 4 °C; el rango del fabricante de ejemplo es de 6 a 10 °C. El plan del fabricante pide limpiar el filtro cada 3 meses. No hay registros de otras limpiezas. Tarifa de ejemplo: $150 por kWh.")
build(
    O7, 3, F,
    use="Aprenderé a plantear hipótesis de falla, a ver cuáles tienen respaldo en la bitácora y en el informe, y a evitar afirmar una causa sin comprobarla.",
    prior=["Sé qué es el ΔT.", "Sé la diferencia entre hecho y opinión.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Una hipótesis de falla es una explicación posible que aún debe comprobarse. Un diagnóstico ordenado parte del síntoma, lista las hipótesis y revisa cuál tiene más respaldo en los datos: la bitácora, el historial, el informe de inspección y el manual del fabricante. Una hipótesis con varios datos a favor es más probable, pero no es una certeza; la causa la confirma personal autorizado con una revisión del equipo, no quien lee los papeles.",
        "Cambiar piezas sin diagnóstico puede costar más y no resolver el problema. Si no hay evidencia para una hipótesis, se anota como «sin evidencia» y se revisa solo si los síntomas persisten. Los datos de consumo ayudan: un aumento sostenido sin cambio de uso sugiere que el equipo trabaja con dificultad. El porcentaje de aumento se calcula dividiendo el aumento por el valor inicial y multiplicando por 100.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("hipótesis de falla", "explicación posible de una falla que aún debe comprobarse"), ("respaldo", "datos observados o registrados que coinciden con una hipótesis"), ("evidencia", "dato que apoya o descarta una hipótesis"), ("aumento sostenido", "alza que se mantiene o crece con el tiempo"), ("diagnóstico ordenado", "método que parte del síntoma, lista hipótesis y las descarta o confirma con datos")],
    worked=[
        ("Porcentaje de aumento", "El consumo de un equipo de ejemplo pasó de 200 a 250 kWh. ¿Qué porcentaje aumentó?", ["El aumento es 250 menos 200, o sea 50.", "50 dividido por 200 es 0,25: 25 %."], "25 %"),
        ("Hipótesis con respaldo", "Un equipo de ejemplo no enfría, tiene el filtro sin limpiar hace 10 meses y el plan pide limpiarlo cada 3. ¿Qué hipótesis tiene respaldo?", ["El dato del filtro coincide con una obstrucción.", "La hipótesis es el filtro obstruido."], "Filtro obstruido"),
    ],
    mistakes=[("Afirmar la causa solo porque una hipótesis tiene varios datos a favor.", "Un respaldo alto no es una confirmación.", "Presenta la hipótesis como probable y pide la comprobación por personal autorizado."),
              ("Cambiar piezas caras antes de comprobar las hipótesis simples.", "Puede gastarse mucho y no resolver el problema.", "Parte por las hipótesis con más respaldo y menor costo de comprobar.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es una hipótesis de falla?", "Una explicación posible que aún debe comprobarse", "La causa confirmada de la falla", "El precio de la reparación", "Una hipótesis es una explicación todavía no comprobada."),
        ("abc", "¿Qué respalda a una hipótesis de falla?", "Datos observados o registrados que coinciden con ella", "La opinión de quien habla más fuerte", "El precio de la pieza sospechosa", "El respaldo viene de datos, no de opiniones ni de precios."),
        ("abc", "¿Cómo parte un diagnóstico ordenado?", "Desde el síntoma, listando hipótesis y revisando cuáles tienen respaldo", "Cambiando la pieza más cara", "Eligiendo la causa que sugiere el cliente", "El diagnóstico ordenado parte del síntoma y usa datos para descartar o confirmar."),
        ("=", "{F} ¿Cuántos kWh subió el consumo entre el mes 1 y el mes 12?", "560-400", "Se resta el consumo inicial del consumo final.", " kWh"),
        ("=", "{F} ¿Qué porcentaje subió el consumo entre el mes 1 y el mes 12?", "(560-400)*100//400", "Se divide el aumento por el consumo inicial y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos °C le faltan al ΔT registrado para llegar al mínimo del rango del fabricante?", "6-4", "Se resta el ΔT registrado del mínimo del rango.", " °C"),
        ("=", "{F} Según el plan, entre el mes 1 y el mes 12 se debieron hacer limpiezas en los meses 4, 7 y 10. ¿Cuántas limpiezas se omitieron?", "(12-1)//3", "Se divide el tiempo transcurrido por el intervalo del plan.", " limpiezas"),
        ("abc", "{F} ¿Qué hipótesis tiene más respaldo en los datos?", "Filtro obstruido: faltan limpiezas, el consumo sube y el ΔT queda bajo el rango", "Falla del compresor, por la antigüedad del equipo", "Sensor defectuoso, porque el cliente lo sospecha", "La bitácora y el informe apoyan el filtro; los otros no tienen datos a favor."),
        ("abc", "{F} ¿Se puede afirmar con certeza que el filtro es la causa?", "No: es la hipótesis con más respaldo, pero la confirma personal autorizado", "Sí: los datos la prueban completamente", "Sí: el cliente ya lo dijo", "Un respaldo alto es una presunción; la confirmación exige revisión autorizada."),
        ("abc", "{F} El cliente propone cambiar el compresor. ¿Qué responde el técnico?", "Que antes se comprueban las hipótesis con datos; cambiar piezas sin diagnóstico puede costar más y no resolver", "Que lo cambia mañana mismo", "Que el compresor siempre es la causa", "Un cambio sin diagnóstico puede no resolver el síntoma y encarecer la solución."),
        ("=", "{F} Un compresor de ejemplo cuesta $600.000 y una mantención con limpieza $40.000. Si la causa fuera el filtro, ¿cuánto se ahorra al no cambiar el compresor?", "600000-40000", "Se resta el costo de la mantención del costo del compresor.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta, con la tarifa de ejemplo, el consumo extra del mes 12 respecto del mes 1?", "(560-400)*150", "Se multiplica el consumo extra en kWh por la tarifa.", " pesos"),
        ("abc", "{F} Otra hipótesis es una fuga de refrigerante, pero no hay reposiciones registradas. ¿Qué corresponde?", "Anotarla como hipótesis sin evidencia y revisarla si los síntomas persisten", "Afirmar que hay fuga porque el equipo no enfría", "Eliminarla del informe", "Sin datos que la apoyen, la hipótesis se anota sin evidencia y no se afirma."),
    ],
    ctx=("abc", "Un técnico de ejemplo quiere cambiar tres piezas a la vez «para asegurar». ¿Qué le responde la supervisora?", "Que primero se comprueben las hipótesis con más respaldo, una por una, con personal autorizado", "Que cambie las tres y vea qué funciona", "Que cambie solo la más cara", "Cambiar varias piezas a la vez no permite saber cuál era la causa y encarece el trabajo."),
    sc=[
        ("En Refrigeración: ¿qué es una hipótesis de falla?", "Una explicación posible que aún debe comprobarse", "Una hipótesis todavía no es una causa confirmada."),
        ("¿Quién confirma la causa de una falla?", "Personal autorizado, con una revisión del equipo", "Los papeles solo dan presunciones y no confirmaciones."),
        ("¿Cómo se calcula el porcentaje de aumento del consumo?", "Aumento dividido por el valor inicial, por 100", "Así se compara con el consumo de partida."),
    ],
    op=("Bitácora de ejemplo del «Salón Tilo» (ficticio): mes 1, limpieza del filtro, consumo 300 kWh; mes 6, consumo 345 kWh; mes 12, consumo 390 kWh y el cliente reporta que «no enfría». El plan pide limpiar el filtro cada 4 meses y no hay otras limpiezas registradas. "
        "Escribe (a) cuánto subió el consumo y qué porcentaje, (b) cuántas limpiezas se omitieron, (c) la hipótesis con más respaldo y por qué, (d) por qué no la afirmas como causa.",
        "(a) 390 menos 300 son 90 kWh; 90 por 100 dividido por 300 son 30 %. (b) Entre el mes 1 y el 12 debieron hacerse limpiezas en los meses 5 y 9: 2 omitidas. (c) Filtro obstruido, porque faltan limpiezas y el consumo sube. (d) Es una hipótesis con respaldo; la causa la confirma personal autorizado con una revisión.",
        ["calcula el aumento y el porcentaje", "cuenta las limpiezas omitidas", "elige la hipótesis con respaldo", "no la afirma sin comprobación"],
        ["hoja con las cuatro respuestas"],
        ["afirmar la causa", "dividir mal el porcentaje", "ignorar la bitácora"],
        "Pregunta: «¿por qué no afirmas el filtro como causa?». Si no responde, pídele que relea la diferencia entre respaldo y confirmación."),
    reinforce="Inventa una bitácora de cuatro registros de consumo y calcula el porcentaje de aumento entre el primero y el último.",
    extend="Explica con un ejemplo por qué cambiar varias piezas a la vez dificulta saber cuál era la causa.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (hallazgos de una inspección de ejemplo, inventados). H1: filtro de aire sucio (severidad 2, probabilidad 5). H2: ruido anormal en la unidad exterior (severidad 4, probabilidad 4). "
     "H3: señal de aceite junto a una unión de la cañería (severidad 5, probabilidad 3). H4: pintura descascarada del gabinete (severidad 1, probabilidad 4). Escalas de 1 a 5. "
     "Puntaje de riesgo = severidad × probabilidad. Criterio de ejemplo: 15 o más es prioridad alta; de 8 a 14, media; 7 o menos, baja.")
build(
    O7, 4, F,
    use="Aprenderé a ordenar los hallazgos de una inspección por riesgo, con severidad y probabilidad, y a recordar que la seguridad está por sobre cualquier puntaje.",
    prior=["Sé multiplicar.", "Sé qué es un hallazgo.", "Sé qué es una hipótesis de falla."],
    explain=[
        "Una inspección puede dejar varios hallazgos y no todos son igual de urgentes. Para ordenarlos se evalúan dos cosas. La severidad mide qué tan grave sería la consecuencia si el problema ocurre, y la probabilidad mide qué tan posible es que ocurra. Ambas se puntúan de 1 a 5 y el puntaje de riesgo es su producto. Un puntaje alto indica prioridad alta; los límites de cada nivel los fija el criterio de la empresa o del proyecto.",
        "Un hallazgo muy probable pero poco grave puede ser menos urgente que uno poco probable pero muy grave. Los puntajes ayudan a ordenar el trabajo, pero no reemplazan la seguridad: si hay olor a quemado, humo, chispas o riesgo para las personas, nadie sigue puntuando: nadie se acerca ni toca, y se avisa a un adulto responsable y a emergencias. Las acciones sobre el equipo las decide el supervisor y las ejecuta personal autorizado.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("severidad", "qué tan grave sería la consecuencia de un problema"), ("probabilidad", "qué tan posible es que un problema ocurra"), ("puntaje de riesgo", "producto de la severidad por la probabilidad"), ("prioridad", "orden de urgencia con que se atienden los hallazgos"), ("criterio de priorización", "regla que dice qué puntaje corresponde a prioridad alta, media o baja")],
    worked=[
        ("Calcular el riesgo", "Un hallazgo de ejemplo tiene severidad 3 y probabilidad 4. ¿Cuál es su puntaje de riesgo?", ["El puntaje es severidad por probabilidad.", "3 por 4 son 12."], "12 puntos"),
        ("Clasificar la prioridad", "Con el criterio de ejemplo de la ficha, ¿qué prioridad tiene un puntaje de 12?", ["12 está entre 8 y 14.", "Corresponde a prioridad media."], "Prioridad media"),
    ],
    mistakes=[("Atender primero el hallazgo que más se repite aunque sea poco grave.", "El riesgo combina severidad y probabilidad.", "Usa el puntaje de riesgo para ordenar."),
              ("Seguir puntuando mientras hay olor a quemado.", "La seguridad está por sobre cualquier puntaje.", "No te acerques ni toques; avisa a un adulto responsable y a emergencias.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es la severidad de un hallazgo?", "Qué tan grave sería la consecuencia si el problema ocurre", "Qué tan seguido se repite el problema", "Cuánto cuesta corregir el problema", "La severidad mide la gravedad de la consecuencia; la repetición es la probabilidad."),
        ("abc", "¿Qué mide la probabilidad de un hallazgo?", "Qué tan posible es que el problema ocurra", "Qué tan grave sería la consecuencia", "Cuánto tiempo toma repararlo", "La probabilidad mide qué tan posible es que ocurra, no su gravedad ni su duración."),
        ("abc", "¿Cómo se calcula el puntaje de riesgo?", "Multiplicando la severidad por la probabilidad", "Sumando la severidad y la probabilidad", "Restando la probabilidad de la severidad", "El puntaje de riesgo es un producto, según la ficha."),
        ("=", "{F} ¿Cuál es el puntaje de riesgo de H1?", "2*5", "Se multiplica su severidad por su probabilidad.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje de riesgo de H2?", "4*4", "Se multiplica su severidad por su probabilidad.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje de riesgo de H3?", "5*3", "Se multiplica su severidad por su probabilidad.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje de riesgo de H4?", "1*4", "Se multiplica su severidad por su probabilidad.", " puntos"),
        ("abc", "{F} Según el criterio de la ficha, ¿qué hallazgos son de prioridad alta?", "H2 y H3", "H1 y H4", "H1 y H2", "H2 tiene 16 y H3 tiene 15, ambos de 15 o más; H1 tiene 10 y H4 tiene 4."),
        ("abc", "{F} ¿Qué hallazgo es de prioridad baja?", "H4, con 4 puntos", "H1, con 10 puntos", "H3, con 15 puntos", "Solo H4 tiene 7 puntos o menos."),
        ("abc", "{F} Un compañero dice: «H1 se repite mucho, así que es lo más urgente». ¿Qué respuesta es correcta?", "No: tiene alta probabilidad pero baja severidad; su puntaje es menor que los de H2 y H3", "Sí: lo que más se repite siempre es lo más urgente", "Sí, porque su probabilidad es 5", "El riesgo combina severidad y probabilidad; H1 tiene 10 puntos y H2 y H3 tienen más."),
        ("=", "{F} ¿Cuántos puntos suman los puntajes de riesgo de los cuatro hallazgos?", "2*5+4*4+5*3+1*4", "Se calcula cada puntaje de riesgo y se suman los cuatro.", " puntos"),
        ("abc", "{F} Mientras se ordenan los hallazgos aparece olor a quemado cerca del equipo. ¿Qué corresponde?", "La seguridad va primero: no acercarse, avisar a un adulto responsable y a emergencias", "Terminar de puntuar antes de avisar", "Acercarse a comprobar de dónde viene", "Ante olor a quemado se interrumpe todo y se avisa; los puntajes pasan a segundo plano."),
        ("=", "{F} Si tras una corrección hecha por personal autorizado la probabilidad de H3 baja de 3 a 1, ¿cuál es su nuevo puntaje de riesgo?", "5*1", "Se multiplica su severidad, que no cambió, por la nueva probabilidad.", " puntos"),
    ],
    ctx=("abc", "Una supervisora de ejemplo recibe una lista de hallazgos sin puntajes y debe decidir qué atender primero. ¿Qué pide?", "Que cada hallazgo se evalúe con severidad y probabilidad según el criterio de priorización", "Que se atiendan en el orden en que se escribieron", "Que se atienda primero el más barato", "El orden de urgencia se apoya en el riesgo, no en el orden de escritura ni en el costo."),
    sc=[
        ("En Refrigeración: ¿cómo se calcula el puntaje de riesgo?", "Severidad por probabilidad", "Así se combina cuán grave y cuán posible es el problema."),
        ("¿Qué pasa con los puntajes si hay olor a quemado?", "La seguridad va primero y se avisa de inmediato", "Los puntajes ordenan trabajo, no reemplazan la seguridad."),
        ("¿Quién ejecuta las acciones sobre el equipo?", "Personal autorizado, por decisión del supervisor", "Este cuaderno no habilita para trabajar ni para intervenir equipos."),
    ],
    op=("Hallazgos de ejemplo del «Salón Piedra» (ficticio): J1, burbujas de agua junto a una unión (severidad 4, probabilidad 3); J2, filtro algo sucio (severidad 2, probabilidad 4); J3, cable con aislación dañada visible (severidad 5, probabilidad 4). Criterio: 15 o más es alta, de 8 a 14 media, 7 o menos baja. "
        "Escribe (a) el puntaje de cada hallazgo, (b) la prioridad de cada uno, (c) cuál se atiende primero y quién lo ejecuta, (d) qué haces si notas olor a quemado cerca de J3.",
        "(a) J1: 4 por 3 son 12; J2: 2 por 4 son 8; J3: 5 por 4 son 20. (b) J1 media, J2 media, J3 alta. (c) Se atiende primero J3, por decisión del supervisor y con personal autorizado; yo no me acerco ni toco el cable. (d) Me alejo, no toco nada y aviso a un adulto responsable y a emergencias.",
        ["calcula los puntajes", "asigna las prioridades", "ordena y nombra quién ejecuta", "aplica la regla de seguridad"],
        ["hoja con las cuatro respuestas"],
        ["sumar en vez de multiplicar", "atender por orden de escritura", "decir que revisaría el cable"],
        "Pregunta: «¿qué haces si hay olor a quemado?». Si no responde, pídele que relea la regla de que la seguridad va primero."),
    reinforce="Inventa tres hallazgos con severidad y probabilidad, calcula sus puntajes y ordénalos del más al menos urgente.",
    extend="Explica con un ejemplo por qué un hallazgo poco probable puede ser más urgente que uno muy probable.",
)
