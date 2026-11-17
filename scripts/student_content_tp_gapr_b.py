"""Gastronomía TP 4.º medio, mención Pastelería y Repostería: OAM-04 (máquinas, equipos e instrumental: solo conceptos, clasificación, seguridad general, bitácoras y planificación) y OAM-05 (variaciones de recetas y de la forma de servir). Todo en papel, sin operar equipos ni describir técnicas: datos «de ejemplo»."""
from __future__ import annotations

from tp_gapr_common import build

O4 = "TP-GAPR-4-OAM-04"
O5 = "TP-GAPR-4-OAM-05"
LIM = " Este cuaderno trabaja en papel, con datos de ejemplo: la práctica en obrador requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria); no te habilita para operar equipos ni para trabajar."

# ============================================================ OAM-04, clase 1
F = ("Ficha 1 (obrador de ejemplo, inventado). Equipos: batidora eléctrica de mesa, amasadora, horno, cámara de refrigeración, balanza y laminadora. Instrumental: espátulas, moldes, mangas pasteleras, termómetro y tamiz. "
     "Peligros generales: atrapamiento (partes en movimiento), quemaduras (superficies calientes), cortes, descargas eléctricas y resbalones. Reglas generales: usar un equipo solo con capacitación y autorización; no usarlo con las protecciones retiradas; no usar ropa suelta ni joyas colgantes cerca de partes en movimiento; "
     "apagar y desconectar antes de limpiar o revisar, tarea que hace personal autorizado; informar de inmediato cualquier falla y no repararla por cuenta propia.")
build(
    O4, 1, F,
    use="Aprenderé a situar el uso de máquinas, equipos e instrumental de un obrador: qué son, qué peligros tienen y qué reglas generales de seguridad se aplican.",
    prior=["Conozco la higiene del obrador.", "Sé restar cantidades.", "Conozco los roles de un obrador."],
    explain=[
        "En Pastelería y Repostería, un equipo es un aparato o una máquina, como una batidora, una amasadora o un horno; el instrumental es el conjunto de herramientas manuales, como espátulas, moldes o un tamiz. Cada equipo tiene un uso previsto, una capacidad y riesgos propios, que figuran en las instrucciones del fabricante y en la ficha del equipo.",
        "Los peligros más frecuentes son el atrapamiento por partes en movimiento, las quemaduras por superficies calientes, los cortes, las descargas eléctricas y los resbalones. Las reglas generales son usar un equipo solo con capacitación y autorización, mantener las protecciones puestas, evitar ropa suelta y joyas cerca de partes en movimiento, apagar y desconectar antes de limpiar o revisar, e informar cualquier falla sin repararla por cuenta propia.",
        "Estas reglas no sustituyen la capacitación práctica con instructor ni la norma vigente. Ante un accidente, se avisa de inmediato a un adulto responsable y a los servicios de emergencia." + LIM,
    ],
    vocab=[("equipo", "aparato o máquina, como una batidora o un horno"), ("instrumental", "herramientas manuales, como espátulas o moldes"), ("atrapamiento", "lesión por quedar una parte del cuerpo o la ropa en una pieza en movimiento"), ("protección", "pieza que cubre una parte peligrosa de un equipo"), ("capacitación", "formación práctica que habilita a usar un equipo con seguridad")],
    worked=[
        ("Clasificar un elemento", "En un obrador de ejemplo hay una espátula y un horno. ¿Cuál es equipo y cuál instrumental?", ["El horno es un aparato.", "La espátula es una herramienta manual."], "El horno es un equipo y la espátula, instrumental"),
        ("Contar autorizaciones", "En un obrador de ejemplo trabajan 10 personas y 4 están autorizadas para usar la amasadora. ¿Cuántas no lo están?", ["Se restan las autorizadas del total.", "10 − 4 = 6."], "6 personas"),
    ],
    mistakes=[("Usar un equipo «porque parece fácil» sin capacitación.", "Un uso incorrecto puede causar atrapamientos, cortes o quemaduras.", "Úsalo solo con capacitación y autorización."),
              ("Retirar una protección «porque estorba».", "Deja expuesta una parte peligrosa del equipo.", "No uses el equipo sin su protección e informa la situación.")],
    T=[
        ("abc", "En Pastelería y Repostería: ¿qué es un equipo?", "Un aparato o máquina, como una batidora o un horno", "Una herramienta manual, como una espátula", "Una receta con cantidades", "El equipo es un aparato; las herramientas manuales son instrumental."),
        ("abc", "{F} ¿Cuál de estos elementos es instrumental?", "El tamiz", "La amasadora", "La laminadora", "El tamiz es una herramienta manual."),
        ("abc", "{F} ¿Qué peligro se asocia a las partes en movimiento?", "El atrapamiento", "El resbalón", "La descarga eléctrica", "La ficha asocia el atrapamiento a las partes en movimiento."),
        ("abc", "{F} ¿Qué peligro se asocia a las superficies calientes?", "Las quemaduras", "Los cortes", "El atrapamiento", "Una superficie caliente puede quemar la piel."),
        ("=", "En un obrador de ejemplo trabajan 12 personas y 5 tienen capacitación y autorización para usar la amasadora. ¿Cuántas no la tienen?", "12-5", "Del total de personas se restan las autorizadas.", " personas"),
        ("abc", "{F} Un ayudante quiere limpiar la batidora mientras está conectada, «solo un momento». ¿Qué corresponde?", "Apagar y desconectar antes, y dejar que lo haga personal autorizado", "Limpiarla rápido con cuidado", "Limpiarla con la mano seca", "La regla exige apagar y desconectar antes de limpiar o revisar."),
        ("abc", "{F} La amasadora tiene la protección retirada «porque estorba». ¿Qué corresponde?", "No usarla e informar de inmediato", "Usarla con cuidado", "Usarla solo con poca masa", "Un equipo sin su protección deja expuestas partes peligrosas."),
        ("abc", "{F} Una ayudante trabaja cerca de la amasadora con una manga ancha y suelta. ¿Qué observación corresponde?", "La ropa suelta puede quedar atrapada; debe usar ropa ajustada", "Está bien si se arremanga una vez", "Está bien si la amasadora está lenta", "La regla evita que la ropa quede atrapada por partes en movimiento."),
        ("abc", "{F} El horno hace un ruido extraño al usarse. ¿Qué corresponde?", "Dejar de usarlo, informar de inmediato y no repararlo por cuenta propia", "Seguir usándolo hasta que termine el turno", "Repararlo con ayuda de un compañero", "Una falla se informa a quien corresponde y no se repara sin autorización."),
        ("abc", "Un compañero dice que, como una batidora es de uso común, no necesita capacitación. ¿Qué respuesta es correcta?", "Todo equipo con partes en movimiento o calor se usa solo con capacitación y autorización", "Tiene razón, es de uso común", "Solo el horno requiere capacitación", "El uso común no elimina el riesgo."),
        ("abc", "En un obrador, una persona sufre un accidente con un equipo. ¿Qué corresponde?", "Avisar de inmediato a un adulto responsable y a los servicios de emergencia", "Intentar sacarla con una maniobra improvisada", "Esperar a ver si se recupera", "Ante un accidente se pide ayuda de personal capacitado."),
        ("=", "Un obrador de ejemplo tiene 3 amasadoras y 2 batidoras, y cada equipo requiere 2 personas autorizadas por turno. Hay 3 turnos. ¿Cuántas autorizaciones se necesitan en total?", "(3+2)*2*3", "Se suman los equipos y se multiplican por las personas y los turnos.", " autorizaciones"),
        ("abc", "{F} ¿Para qué sirven las instrucciones de operación del fabricante?", "Para conocer el uso previsto, los límites y los riesgos del equipo", "Para decidir el precio de los productos", "Para reemplazar la capacitación práctica", "Las instrucciones complementan la capacitación, pero no la reemplazan."),
    ],
    ctx=("abc", "{F} Un practicante comenta que vio en un video cómo se usa una amasadora y que «ya está listo» para usarla solo. ¿Qué debe responder el encargado?", "Que ver un video no reemplaza la capacitación práctica con instructor y la autorización", "Que puede usarla si ve otro video", "Que puede usarla si trabaja despacio", "El uso de un equipo requiere formación práctica y autorización."),
    sc=[
        ("En Pastelería y Repostería: ¿qué es el instrumental?", "Las herramientas manuales, como espátulas y moldes", "Se distingue de los equipos, que son aparatos."),
        ("¿Qué se hace antes de limpiar un equipo?", "Apagarlo y desconectarlo", "Evita que parta mientras se limpia."),
        ("¿Quién repara un equipo con falla?", "Personal autorizado, no cualquier persona", "Una reparación improvisada puede causar accidentes."),
    ],
    op=("Un obrador de ejemplo tiene: batidora, espátulas, horno, moldes, balanza, tamiz. Un ayudante nuevo quiere probar la batidora y comenta que la protección «le molesta». "
        "Escribe: (a) qué elementos son equipos y cuáles instrumental, (b) tres reglas generales de seguridad que aplicarías a la batidora, y (c) qué harías con la protección que molesta.",
        "(a) Equipos: batidora, horno y balanza. Instrumental: espátulas, moldes y tamiz. (b) Usarla solo con capacitación y autorización; apagar y desconectar antes de limpiar; evitar ropa suelta y joyas cerca. (c) No retirar la protección ni usar el equipo así; informar al encargado.",
        ["clasifica los seis elementos", "nombra tres reglas de seguridad", "indica no retirar la protección e informar"],
        ["hoja con tres respuestas"],
        ["llamar equipo a las espátulas", "retirar la protección", "describir cómo operar la batidora"],
        "Pregunta: «¿qué haces si la protección molesta?». Debe responder informar y no usar el equipo así."),
    reinforce="Haz una tabla con ocho elementos de un obrador inventado y clasifícalos como equipo o instrumental.",
    extend="Explica por qué una regla de seguridad se aplica siempre, aunque quien trabaje tenga experiencia.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 2 (clasificación y documentos de equipos de ejemplo). Clasificación por función: pesaje y medición (balanza, termómetro); mezclado y amasado (batidora, amasadora); calor (horno); frío y conservación (cámara de refrigeración); formado y corte (laminadora, cortadores). "
     "Ficha de equipo: nombre, función, capacidad, uso previsto, riesgos y mantención. Mantención preventiva: revisiones programadas para evitar fallas. Mantención correctiva: reparación después de una falla. Bitácora: registro de usos, fallas y mantenciones. "
     "Roles: el operador autorizado usa el equipo; el encargado de mantención lo revisa y repara; la jefa de producción planifica su uso.")
build(
    O4, 2, F,
    use="Aprenderé el vocabulario y los documentos de los equipos de un obrador: clasificación por función, ficha de equipo, mantención y bitácora, y quién responde por cada cosa.",
    prior=["Distingo equipo e instrumental.", "Conozco las reglas generales de seguridad.", "Sé calcular divisiones."],
    explain=[
        "Los equipos de un obrador se clasifican por función: pesaje y medición (balanza, termómetro), mezclado y amasado (batidora, amasadora), calor (horno), frío y conservación (cámara de refrigeración) y formado y corte (laminadora). Conocer la función ayuda a elegir el equipo adecuado y a entender sus riesgos.",
        "Cada equipo tiene una ficha con su capacidad, su uso previsto, sus riesgos y su mantención. La mantención preventiva son revisiones programadas para evitar fallas; la correctiva es la reparación después de que el equipo falla. La bitácora es el registro de usos, fallas y mantenciones, y permite saber qué pasó y cuándo.",
        "El operador autorizado usa el equipo, el encargado de mantención lo revisa y repara, y la jefa de producción planifica su uso según su capacidad. La capacidad es la cantidad máxima que el equipo puede procesar en cada uso; superarla es un riesgo." + LIM,
    ],
    vocab=[("capacidad", "cantidad máxima que un equipo puede procesar en cada uso"), ("mantención preventiva", "revisiones programadas para evitar fallas"), ("mantención correctiva", "reparación después de una falla"), ("bitácora", "registro de usos, fallas y mantenciones de un equipo"), ("operador autorizado", "persona capacitada y autorizada para usar un equipo")],
    worked=[
        ("Calcular tandas", "Una batidora de ejemplo procesa hasta 4 kg por uso y se necesitan 12 kg de masa. ¿Cuántos usos se necesitan?", ["Se divide el total por la capacidad.", "12 ÷ 4 = 3."], "3 usos"),
        ("Distinguir mantenciones", "Un equipo de ejemplo se revisa cada mes aunque funcione bien. ¿Qué tipo de mantención es?", ["Se hace en forma programada.", "No espera una falla."], "Mantención preventiva"),
    ],
    mistakes=[("Superar la capacidad del equipo «para ahorrar tiempo».", "Se sobrecarga el equipo y aumentan los riesgos de falla y de accidente.", "Respeta la capacidad indicada en la ficha del equipo."),
              ("No anotar una falla en la bitácora porque «ya se arregló».", "Se pierde la historia del equipo y se repiten las fallas.", "Registra todas las fallas y mantenciones en la bitácora.")],
    T=[
        ("abc", "{F} ¿En qué grupo se clasifica la balanza?", "Pesaje y medición", "Mezclado y amasado", "Formado y corte", "La ficha ubica la balanza y el termómetro en pesaje y medición."),
        ("abc", "{F} ¿En qué grupo se clasifica la amasadora?", "Mezclado y amasado", "Calor", "Frío y conservación", "La ficha ubica la batidora y la amasadora en mezclado y amasado."),
        ("abc", "{F} ¿Qué es la mantención preventiva?", "Revisiones programadas para evitar fallas", "Reparación después de una falla", "Compra de un equipo nuevo", "La ficha define la preventiva como revisiones programadas."),
        ("=", "{F} Una batidora de ejemplo procesa hasta 5 kg por uso y se necesitan 25 kg de masa. ¿Cuántos usos se necesitan?", "25//5", "Se divide la masa total por la capacidad de cada uso.", " usos"),
        ("abc", "{F} ¿Qué registra la bitácora?", "Usos, fallas y mantenciones", "Solo los precios de los productos", "Solo los alérgenos", "La ficha define la bitácora con esos tres registros."),
        ("abc", "{F} ¿Quién revisa y repara los equipos?", "El encargado de mantención", "El operador autorizado", "La jefa de producción", "La ficha asigna la revisión y reparación al encargado de mantención."),
        ("abc", "{F} ¿Quién planifica el uso de los equipos según su capacidad?", "La jefa de producción", "El encargado de mantención", "El operador autorizado", "La ficha asigna la planificación a la jefa."),
        ("=", "Un horno de ejemplo tiene 6 bandejas y cada bandeja recibe 20 piezas. ¿Cuántas piezas caben en cada hornada?", "6*20", "Se multiplican las bandejas por las piezas de cada una.", " piezas"),
        ("=", "Con ese horno de ejemplo de 6 bandejas de 20 piezas, ¿cuántas hornadas se necesitan para 480 piezas?", "480//(6*20)", "Se divide el total de piezas por las que caben en cada hornada.", " hornadas"),
        ("abc", "{F} Un operador agrega 7 kg de masa a una batidora de capacidad 5 kg «porque es poco más». ¿Qué observación corresponde?", "Supera la capacidad y sobrecarga el equipo; debe dividir la masa en usos", "Está bien, porque la batidora es potente", "Está bien si trabaja despacio", "Superar la capacidad aumenta el riesgo de falla y accidente."),
        ("abc", "{F} Un equipo falló y se reparó el mismo día. ¿Qué debe hacerse con el registro?", "Anotar la falla y la reparación en la bitácora", "No anotar nada, porque ya funciona", "Anotar solo la fecha", "La bitácora conserva la historia del equipo."),
        ("=", "{F} Un obrador de ejemplo revisa su cámara de refrigeración cada 30 días como mantención preventiva. ¿Cuántas revisiones hace en 360 días?", "360//30", "Se divide el período por el intervalo entre revisiones.", " revisiones"),
        ("abc", "{F} ¿Qué diferencia hay entre una mantención preventiva y una correctiva?", "La preventiva se programa antes de que falle; la correctiva se hace después de una falla", "La preventiva se hace solo en equipos nuevos", "La correctiva se hace antes de usar el equipo", "Una busca evitar fallas y la otra repararlas."),
    ],
    ctx=("abc", "{F} El encargado de mantención nota que la bitácora de la amasadora no tiene registros de los últimos meses. ¿Qué debe hacer?", "Pedir a los operadores que registren los usos y fallas, e informar a la jefa de producción", "Ignorarlo, porque la amasadora funciona", "Inventar los registros de los últimos meses", "Una bitácora sin registro no permite planificar la mantención."),
    sc=[
        ("En Pastelería y Repostería: ¿qué es la capacidad de un equipo?", "La cantidad máxima que procesa en cada uso", "Superarla aumenta el riesgo de falla."),
        ("¿Qué es la mantención correctiva?", "La reparación después de una falla", "Se distingue de la preventiva, que es programada."),
        ("¿Qué registra la bitácora?", "Usos, fallas y mantenciones", "Permite conocer la historia del equipo."),
    ],
    op=("Ficha de ejemplo: batidora con capacidad de 4 kg por uso; horno con 5 bandejas de 24 piezas; mantención preventiva de la batidora cada 150 horas de uso. Se necesitan 20 kg de masa y 480 piezas. "
        "Calcula los usos de la batidora, las piezas por hornada y las hornadas necesarias; indica quién planifica el uso, quién repara si hay una falla y qué se anota en la bitácora.",
        "Usos de la batidora: 20 ÷ 4 = 5. Piezas por hornada: 5 × 24 = 120. Hornadas: 480 ÷ 120 = 4. Planifica la jefa de producción; repara el encargado de mantención; se anotan los usos, las fallas y las mantenciones.",
        ["calcula 5 usos y 4 hornadas", "nombra planificación y reparación", "indica el contenido de la bitácora"],
        ["hoja con cálculos y tres respuestas"],
        ["olvidar la capacidad", "confundir quien repara con quien planifica", "no mencionar la bitácora"],
        "Pregunta: «¿cuántas piezas caben por hornada?». Debe responder 120."),
    reinforce="Inventa una ficha de equipo con capacidad y mantención, y calcula cuántos usos requiere una producción inventada.",
    extend="Explica por qué la mantención preventiva suele ser mejor que esperar a que un equipo falle.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 3 (bitácora y pedido de ejemplo, inventados). Equipos: 2 batidoras de ejemplo (capacidad de masa de 5 kg por uso, cada uso ocupa 30 minutos de ejemplo) y 1 horno (6 bandejas de 20 piezas por hornada). Pedido: 600 piezas, con 30 kg de masa. "
     "Bitácora: el día 3 la batidora 1 hizo un ruido anormal durante el uso; el operador la apagó y avisó. Reglas: un equipo con falla se deja fuera de servicio, rotulado «no usar», y se avisa al encargado de mantención; no se repara por cuenta propia.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un caso con equipos en papel: calcular usos y tiempos según su capacidad y actuar correctamente ante una falla registrada en la bitácora.",
    prior=["Conozco la capacidad y la bitácora.", "Sé dividir y multiplicar.", "Conozco las reglas de seguridad."],
    explain=[
        "Para planificar una producción con equipos se calcula cuántos usos requiere: la cantidad total dividida por la capacidad de cada uso. Si hay varios equipos iguales, los usos se reparten entre ellos, y el tiempo total depende de cuántos usos hace cada equipo y de cuánto dura cada uno.",
        "Si un equipo falla, se detiene su uso, se deja fuera de servicio con un rótulo «no usar», se avisa al encargado de mantención y se anota en la bitácora. La producción se replanifica con los equipos disponibles. Nadie repara el equipo por cuenta propia ni lo vuelve a usar hasta que lo autorice personal calificado.",
        "Un buen análisis anota los datos, calcula, replanifica y registra. Todos los datos son de ejemplo y se calculan en papel." + LIM,
    ],
    vocab=[("fuera de servicio", "equipo que no se debe usar hasta que se repare"), ("rótulo «no usar»", "aviso que impide que otra persona use un equipo con falla"), ("replanificar", "volver a organizar la producción con los recursos disponibles"), ("personal calificado", "personas con la formación para revisar y reparar un equipo")],
    worked=[
        ("Calcular usos por equipo", "Se necesitan 24 kg de masa, la capacidad es de 4 kg por uso y hay 2 equipos iguales. ¿Cuántos usos hace cada equipo?", ["Usos totales: 24 ÷ 4 = 6.", "Entre 2 equipos: 6 ÷ 2 = 3."], "3 usos por equipo"),
        ("Calcular un tiempo", "Un equipo de ejemplo hace 3 usos de 20 minutos cada uno. ¿Cuántos minutos trabaja?", ["Se multiplican los usos por la duración.", "3 × 20 = 60."], "60 minutos"),
    ],
    mistakes=[("Volver a usar un equipo con falla porque «funcionó después de apagarlo y prenderlo».", "La falla puede seguir y causar un accidente.", "Déjalo fuera de servicio hasta que lo autorice personal calificado."),
              ("Planificar sin considerar que un equipo está fuera de servicio.", "La producción se atrasa y se corren riesgos por apuro.", "Replanifica con los equipos que sí están disponibles.")],
    T=[
        ("=", "{F} ¿Cuántos usos de batidora se necesitan para los 30 kg de masa?", "30//5", "Se divide la masa total por la capacidad de cada uso.", " usos"),
        ("=", "{F} Si ambas batidoras estuvieran funcionando, ¿cuántos usos haría cada una?", "30//5//2", "Se divide el total de usos entre las dos batidoras.", " usos"),
        ("=", "{F} Si cada uso dura 30 minutos, ¿cuántos minutos trabajaría cada batidora?", "3*30", "Se multiplican los usos de cada batidora por su duración.", " minutos"),
        ("=", "{F} ¿Cuántas piezas caben en cada hornada?", "6*20", "Se multiplican las bandejas por las piezas de cada una.", " piezas"),
        ("=", "{F} ¿Cuántas hornadas se necesitan para las 600 piezas?", "600//(6*20)", "Se divide el pedido por las piezas de cada hornada.", " hornadas"),
        ("abc", "{F} ¿Qué debe hacerse con la batidora 1, que hizo un ruido anormal?", "Dejarla fuera de servicio, rotularla «no usar» y avisar al encargado de mantención", "Seguir usándola con cuidado", "Repararla con el apoyo de un compañero", "La regla de la ficha exige sacarla de servicio y avisar."),
        ("abc", "{F} ¿Qué rótulo debe llevar la batidora 1 mientras está con falla?", "«No usar»", "«Listo para usar»", "«Revisión terminada»", "El rótulo impide que otra persona use el equipo sin saber que tiene una falla."),
        ("=", "{F} Con solo la batidora 2 disponible, ¿cuántos usos hará en total para los 30 kg?", "30//5", "Se divide la masa por la capacidad de cada uso.", " usos"),
        ("=", "{F} Con solo la batidora 2, ¿cuántos minutos necesitaría en total?", "6*30", "Se multiplican los usos por la duración de cada uno.", " minutos"),
        ("abc", "{F} Con la batidora 1 fuera de servicio, ¿qué decisión es razonable?", "Replanificar la producción con la batidora 2, que toma más tiempo", "Usar igual la batidora 1 para ahorrar tiempo", "Reducir los kilos de masa de cada uso", "Se replanifica con los equipos disponibles sin comprometer la seguridad."),
        ("abc", "{F} Un operador propone volver a usar la batidora 1 porque «ya no suena». ¿Qué corresponde?", "No usarla hasta que personal calificado la revise y la autorice", "Usarla, porque ya no hace ruido", "Usarla solo con poca masa", "Una falla puede persistir aunque no se note."),
        ("=", "{F} Si los usos de la batidora 2 empiezan a las 08:00 y duran 30 minutos cada uno de 6 usos seguidos, ¿cuántas horas dura el trabajo?", "6*30//60", "Se calculan los minutos totales y se pasan a horas.", " horas"),
        ("abc", "{F} ¿Qué debe anotarse en la bitácora?", "La falla de la batidora 1, la acción tomada y el aviso al encargado", "Solo que el pedido se atrasó", "Nada, porque el equipo quedó fuera de servicio", "La bitácora registra fallas y acciones para tener historia del equipo."),
    ],
    ctx=("abc", "{F} El cliente exige el pedido a la hora acordada. La jefa de producción duda entre usar la batidora 1 o atrasarse. ¿Qué es lo más razonable?", "Informar al cliente del atraso posible y replanificar sin usar el equipo con falla", "Usar la batidora 1 para cumplir", "Pedir al operador que la use con cuidado", "La seguridad prevalece sobre el plazo; se informa y se replanifica."),
    sc=[
        ("En Pastelería y Repostería: ¿qué se hace con un equipo con falla?", "Se deja fuera de servicio, rotulado, y se avisa", "Evita que otra persona lo use y se accidente."),
        ("¿Cómo se calculan los usos de un equipo?", "Cantidad total dividida por la capacidad de cada uso", "Muestra cuántas veces debe usarse el equipo."),
        ("¿Quién autoriza volver a usar un equipo reparado?", "Personal calificado", "Verifica que el equipo quedó seguro para usarse."),
    ],
    op=("Caso de ejemplo. Dos amasadoras de capacidad de 6 kg por uso (cada uso ocupa 20 minutos); un horno de 4 bandejas de 25 piezas por hornada. Pedido: 400 piezas con 36 kg de masa. La amasadora 2 queda fuera de servicio por una falla. "
        "Calcula los usos necesarios, el tiempo con una sola amasadora, las piezas por hornada y las hornadas, y escribe tres acciones frente a la falla.",
        "Usos: 36 ÷ 6 = 6. Tiempo con una amasadora: 6 × 20 = 120 minutos. Piezas por hornada: 4 × 25 = 100. Hornadas: 400 ÷ 100 = 4. Acciones: dejar la amasadora 2 fuera de servicio y rotulada «no usar», avisar al encargado de mantención y anotar la falla en la bitácora.",
        ["calcula 6 usos y 120 minutos", "calcula 100 piezas y 4 hornadas", "nombra tres acciones frente a la falla"],
        ["hoja con cálculos y tres acciones"],
        ["usar la amasadora con falla", "olvidar anotar en la bitácora", "dividir mal"],
        "Pregunta: «¿cuántos usos hacen falta?». Debe responder 6."),
    reinforce="Inventa un caso con dos equipos, un pedido y una falla, y calcula usos y tiempos con un solo equipo.",
    extend="Explica por qué se prefiere atrasar un pedido antes que usar un equipo con falla.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 4 (plan de uso y mantención de ejemplo, inventado). Batidora de ejemplo: 25 horas de uso por semana; mantención preventiva cada 200 horas de uso; horas acumuladas desde la última mantención: 150. "
     "Costo de ejemplo de una mantención preventiva: $60.000; costo de ejemplo de una reparación correctiva por falla: $180.000. El obrador trabaja 52 semanas al año.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: calcular cuándo corresponde la mantención de un equipo y comparar el costo de la mantención preventiva con el de las reparaciones.",
    prior=["Conozco la mantención preventiva y correctiva.", "Sé dividir y multiplicar.", "Conozco la bitácora."],
    explain=[
        "La mantención preventiva se programa según horas de uso o tiempo. Para saber cuándo toca la próxima, se calculan las horas que faltan (intervalo menos horas acumuladas) y se dividen por las horas de uso semanales. El resultado es el número de semanas hasta la próxima mantención.",
        "Comparar costos ayuda a decidir: una mantención preventiva suele costar menos que una reparación correctiva y evita detener la producción. El costo anual de la mantención preventiva se obtiene multiplicando el número de mantenciones al año por su costo.",
        "Los valores de esta clase son de ejemplo. Toda mantención la realiza personal calificado y se registra en la bitácora." + LIM,
    ],
    vocab=[("intervalo", "horas o tiempo entre dos mantenciones"), ("horas acumuladas", "horas de uso desde la última mantención"), ("horas de uso al año", "horas semanales por las semanas de trabajo"), ("costo anual", "costo de todas las mantenciones en un año")],
    worked=[
        ("Calcular horas restantes", "Una mantención de ejemplo corresponde cada 100 horas y el equipo lleva 70. ¿Cuántas horas faltan?", ["Se resta lo acumulado al intervalo.", "100 − 70 = 30."], "30 horas"),
        ("Calcular semanas", "Faltan 30 horas y el equipo se usa 10 horas por semana. ¿En cuántas semanas toca la mantención?", ["Se dividen las horas restantes por las horas semanales.", "30 ÷ 10 = 3."], "3 semanas"),
    ],
    mistakes=[("Postergar una mantención preventiva «hasta que el equipo falle».", "Una falla detiene la producción y suele costar más.", "Respeta el programa de mantención preventiva."),
              ("Calcular las semanas con el intervalo completo y no con las horas restantes.", "El resultado no corresponde al momento real de la próxima mantención.", "Resta primero las horas acumuladas.")],
    T=[
        ("=", "{F} ¿Cuántas horas faltan para la próxima mantención preventiva de la batidora?", "200-150", "Al intervalo se le restan las horas acumuladas.", " horas"),
        ("=", "{F} ¿En cuántas semanas toca la próxima mantención?", "(200-150)//25", "Se dividen las horas que faltan por las horas de uso por semana.", " semanas"),
        ("=", "{F} ¿Cuántas horas se usa la batidora en un año?", "25*52", "Se multiplican las horas semanales por las semanas del año.", " horas"),
        ("=", "{F} ¿Cuántas mantenciones preventivas completas corresponden en un año?", "1300//200", "Se dividen las horas anuales por el intervalo entre mantenciones.", " mantenciones"),
        ("=", "{F} ¿Cuánto cuestan esas mantenciones preventivas al año?", "6*60000", "Se multiplican las mantenciones por el costo de cada una.", " pesos"),
        ("=", "{F} Si sin mantención preventiva hubiera 3 fallas al año, ¿cuánto costarían las reparaciones?", "3*180000", "Se multiplican las fallas por el costo de cada reparación.", " pesos"),
        ("abc", "{F} Con los datos de ejemplo, ¿qué resulta más económico al año?", "La mantención preventiva, con $360.000, frente a $540.000 de reparaciones", "Las reparaciones, con $360.000", "Cuestan lo mismo", "La preventiva cuesta menos que las fallas de la hipótesis y evita detener la producción."),
        ("=", "{F} ¿Cuántos pesos se ahorran al año con la mantención preventiva, según esos datos?", "3*180000-6*60000", "A los costos de las reparaciones se les restan los de la mantención preventiva.", " pesos"),
        ("abc", "{F} Un jefe propone no hacer la mantención porque el equipo «funciona bien». ¿Qué observación corresponde?", "La mantención preventiva busca evitar fallas antes de que ocurran", "Tiene razón, no hace falta si funciona", "Solo se hace cuando el equipo falla", "Funcionar hoy no garantiza que no falle mañana."),
        ("=", "{F} Si el uso semanal subiera a 50 horas, ¿en cuántas semanas tocaría la próxima mantención?", "(200-150)//50", "Se dividen las horas que faltan por las nuevas horas semanales.", " semana"),
        ("abc", "{F} ¿Dónde se registra cada mantención realizada?", "En la bitácora del equipo", "En la ficha técnica de un producto", "En el rótulo de un alimento", "La bitácora conserva la historia de usos, fallas y mantenciones."),
        ("abc", "{F} Un operador intenta hacer la mantención de la batidora «para ahorrar». ¿Qué corresponde?", "La realiza personal calificado y queda registrada", "Es válido si ve un tutorial", "Es válido si desconecta el equipo", "La mantención requiere personal con formación y autorización."),
        ("=", "{F} En 2 semanas de uso, ¿cuántas horas acumularía la batidora desde las 150 horas actuales?", "150+25*2", "Se suman las horas acumuladas y las que se agregan en 2 semanas.", " horas"),
    ],
    ctx=("abc", "{F} La jefa de producción debe decidir si adelanta la mantención de la batidora porque se acerca una semana de mucha producción. ¿Qué es lo más razonable?", "Hacerla antes de la semana de alta producción para evitar una falla en un momento crítico", "Esperar a que llegue a las 200 horas aunque pueda fallar", "Cancelarla definitivamente", "Anticipar la mantención reduce el riesgo en la semana de mayor demanda."),
    sc=[
        ("En Pastelería y Repostería: ¿cómo se calculan las horas que faltan para la mantención?", "Intervalo menos horas acumuladas", "Muestra cuánto uso queda antes de la mantención."),
        ("¿Cómo se calculan las semanas hasta la mantención?", "Horas restantes divididas por horas semanales", "Convierte horas de uso en semanas."),
        ("¿Quién realiza la mantención?", "Personal calificado", "Requiere formación y autorización de personal calificado."),
    ],
    op=("Plan de ejemplo de una amasadora: 20 horas de uso por semana; mantención preventiva cada 120 horas; horas acumuladas: 80. Costo de una mantención preventiva: $50.000; costo de una reparación correctiva: $150.000. El obrador trabaja 48 semanas al año. "
        "Calcula las horas que faltan, en cuántas semanas toca la mantención, las horas de uso al año, cuántas mantenciones corresponden al año y su costo anual.",
        "Faltan 120 − 80 = 40 horas. Semanas: 40 ÷ 20 = 2. Horas al año: 20 × 48 = 960. Mantenciones: 960 ÷ 120 = 8. Costo anual: 8 × 50.000 = 400.000 pesos.",
        ["calcula 40 horas y 2 semanas", "calcula 960 horas y 8 mantenciones", "calcula 400.000 pesos"],
        ["hoja con cálculos"],
        ["usar el intervalo completo", "olvidar las semanas", "confundir preventiva y correctiva"],
        "Pregunta: «¿cuántas horas de uso al año tiene la amasadora?». Debe responder 960."),
    reinforce="Inventa un equipo con horas de uso semanales y un intervalo de mantención, y calcula cuándo toca la próxima.",
    extend="Explica por qué conviene registrar cada mantención en la bitácora y no solo realizarla.",
)

# ============================================================ OAM-05, clase 1
F = ("Ficha 1 (variaciones de productos de pastelería, de ejemplo). Producto base: «Bizcocho de ejemplo». Variaciones posibles (de ejemplo): menos azúcar añadida, formato mini (porciones pequeñas), relleno alternativo, versión sin frutos secos en la decoración y versión sin gluten (solo si el obrador puede asegurar que no hay contaminación cruzada). "
     "Reglas: cada variación es una versión nueva con su ficha, aprobada por la jefa de producción, probada con una evaluación sensorial y registrada; en pastelería, cambiar un ingrediente puede alterar la textura, el volumen y la vida útil; "
     "una versión sin un alérgeno exige utensilios, superficies y almacenamiento separados; si no se puede asegurar, se declara «puede contener trazas».")
build(
    O5, 1, F,
    use="Aprenderé a situar las variaciones de productos de pastelería: por qué se hacen, qué efectos pueden tener los cambios y qué cuidados exigen los alérgenos.",
    prior=["Conozco la formulación y los alérgenos.", "Conozco la vida útil.", "Sé multiplicar."],
    explain=[
        "En Pastelería y Repostería, una variación es un cambio planificado en un producto o en su forma de servirlo, para mejorar su sabor o su textura o para atender a una clientela diversa: menos azúcar añadida, un formato mini, un relleno alternativo o una versión sin un alérgeno. Cada variación es una versión nueva, con su propia ficha, aprobación y registro.",
        "En pastelería los ingredientes cumplen funciones y están en equilibrio: cambiar uno puede alterar la textura, el volumen o la vida útil del producto. Por eso toda variación se prueba con una evaluación sensorial, que revisa aspecto, color, olor, sabor y textura, antes de ofrecerse.",
        "Una versión sin un alérgeno, como los frutos secos o el gluten, exige evitar la contaminación cruzada con utensilios, superficies y almacenamiento separados. Si el obrador no puede asegurarlo, se declara «puede contener trazas», es decir, restos muy pequeños del alérgeno. Este cuaderno no enseña a elaborar los productos. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("variación", "cambio planificado de un producto o de su forma de servirlo"), ("formato mini", "porciones pequeñas del mismo producto"), ("evaluación sensorial", "revisión de aspecto, color, olor, sabor y textura"), ("trazas", "restos muy pequeños de un ingrediente"), ("«puede contener»", "advertencia de que pudo haber contacto con un alérgeno")],
    worked=[
        ("Contar versiones", "Un producto de ejemplo se ofrece en 2 formatos y con 2 rellenos. ¿Cuántas versiones distintas hay?", ["Se multiplican los formatos por los rellenos.", "2 × 2 = 4."], "4 versiones"),
        ("Decidir un rotulado", "Un obrador de ejemplo prepara una versión sin frutos secos en la misma mesa que las demás, sin separación. ¿Qué advertencia corresponde?", ["No puede asegurar la ausencia del alérgeno.", "Se declara que puede contener trazas."], "«Puede contener trazas de frutos secos»"),
    ],
    mistakes=[("Llamar «sin gluten» a un producto solo por cambiar la harina.", "El gluten puede llegar por contacto con utensilios, superficies u otros ingredientes.", "Declara «sin gluten» solo si se puede asegurar la separación; si no, declara las trazas."),
              ("Reducir el azúcar sin evaluar el efecto en la textura y la vida útil.", "El producto puede cambiar mucho y durar menos.", "Prueba la versión y registra sus resultados.")],
    T=[
        ("abc", "En Pastelería y Repostería: ¿qué es una variación de un producto?", "Un cambio planificado del producto o de su forma de servirlo", "Un error al seguir la formulación", "El reemplazo definitivo del producto sin registro", "La variación es un cambio deliberado, aprobado y registrado."),
        ("abc", "{F} ¿Cuál de estas es una variación de formato?", "El formato mini", "El relleno alternativo", "Menos azúcar añadida", "El formato mini cambia el tamaño de la porción."),
        ("abc", "{F} ¿Por qué se prueba y se aprueba una variación antes de ofrecerla?", "Porque cambiar un ingrediente puede alterar la textura, el volumen y la vida útil", "Porque la norma pide siempre nuevos colores", "Porque así aumenta el precio", "En pastelería los ingredientes están en equilibrio y un cambio afecta el resultado."),
        ("abc", "{F} ¿Qué exige una versión sin un alérgeno?", "Utensilios, superficies y almacenamiento separados", "Solo cambiar el nombre del producto", "Solo una decoración distinta", "La ficha exige separación para evitar la contaminación cruzada."),
        ("=", "Un producto de ejemplo se ofrece en 2 formatos (normal y mini) y con 3 rellenos distintos. ¿Cuántas versiones distintas hay?", "2*3", "Se multiplican los formatos por los rellenos.", " versiones"),
        ("abc", "{F} Una versión sin frutos secos se prepara en la misma mesa que las demás, sin separación. ¿Qué corresponde informar?", "Que puede contener trazas de frutos secos", "Que es completamente libre de frutos secos", "Nada, porque la decoración es distinta", "Sin separación no se puede asegurar la ausencia del alérgeno."),
        ("abc", "{F} ¿Por qué no basta cambiar la harina para ofrecer una versión sin gluten?", "Porque el gluten puede llegar por contaminación cruzada de utensilios, superficies u otros ingredientes", "Porque la harina nunca contiene gluten", "Porque el azúcar contiene gluten", "La ausencia de gluten depende de todo el proceso, no solo de un ingrediente."),
        ("=", "Un obrador produce 200 unidades por día y el 15 % son del formato mini. ¿Cuántas unidades mini produce?", "200*15//100", "Se calcula el 15 % del total de unidades.", " unidades"),
        ("abc", "{F} Se reduce el azúcar para una versión «menos dulce». ¿Qué debe evaluarse?", "El sabor, la textura, el volumen y la vida útil de la nueva versión", "Solo el nombre del producto", "Solo el precio del azúcar", "El azúcar influye en varios aspectos del producto."),
        ("abc", "{F} Un pastelero ofrece de inmediato un relleno alternativo porque «cree que gustará más». ¿Qué corresponde?", "Presentarlo como propuesta, probarlo, registrarlo y obtener la aprobación", "Ofrecerlo y registrarlo después", "Ofrecerlo solo si nadie reclama", "Una variación se aprueba, se prueba y se registra antes de ofrecerse."),
        ("=", "El obrador ofrece 3 variaciones, cada una con 24 unidades por lote. ¿Cuántas unidades de variaciones produce por lote en total?", "3*24", "Se multiplican las variaciones por las unidades de cada una.", " unidades"),
        ("abc", "{F} Una clienta alérgica a los frutos secos pide la versión sin ellos. ¿Qué debe hacer la persona que atiende?", "Informar según el rotulado y consultar a la jefatura si se produjo con separación o puede contener trazas", "Decirle que es seguro sin revisar", "Ofrecerle la versión normal", "La respuesta debe basarse en el rotulado y la información de producción."),
        ("abc", "{F} Un compañero dice que no hace falta registrar la variación porque «es la misma formulación con un cambio pequeño». ¿Qué respuesta es correcta?", "Todo cambio se registra para poder repetirlo y controlar alérgenos y costos", "Tiene razón, solo se registran cambios grandes", "El registro es opcional", "Un cambio sin registro se pierde y puede alterar alérgenos o costos."),
    ],
    ctx=("abc", "{F} Una escuela de ejemplo pide una versión de un bizcocho con menos azúcar para sus estudiantes. ¿Qué pasos de gestión corresponde seguir?", "Definir la versión con su ficha, evaluar el efecto en la textura y la vida útil, probarla, registrarla y rotular", "Quitar azúcar sin registrar y entregar", "Rechazar el pedido por ser una variación", "La variación se define, se prueba, se registra y se rotula antes de ofrecerse."),
    sc=[
        ("En Pastelería y Repostería: ¿qué exige una versión sin un alérgeno?", "Separación de utensilios, superficies y almacenamiento", "Evita la contaminación cruzada con el alérgeno."),
        ("¿Qué significa «puede contener trazas»?", "Que pudo haber contacto con el alérgeno", "Se usa cuando no se puede asegurar la separación."),
        ("¿Por qué se prueba una variación?", "Porque un cambio puede alterar el producto", "La prueba evalúa los efectos antes de ofrecerla."),
    ],
    op=("Producto base de ejemplo: «Galleta de ejemplo». El obrador estudia tres variaciones: una con menos azúcar, una en formato mini y una versión sin frutos secos (que se produciría en la misma mesa que las demás, sin separación). "
        "Escribe: (a) qué debe probarse en la versión con menos azúcar, (b) qué documentos tendría cada variación, (c) qué advertencia llevaría la versión sin frutos secos y por qué.",
        "(a) El sabor, la textura, el volumen y la vida útil. (b) Cada variación tendría su ficha, aprobación de la jefa de producción, número de versión y registro de la prueba sensorial. (c) «Puede contener trazas de frutos secos», porque sin separación no se puede asegurar la ausencia del alérgeno.",
        ["nombra los efectos del azúcar a evaluar", "indica ficha, aprobación y registro", "declara la advertencia con su razón"],
        ["hoja con tres respuestas"],
        ["decir que la versión es libre de frutos secos", "omitir la aprobación", "no probar la versión"],
        "Pregunta: «¿por qué no puedes asegurar la ausencia de frutos secos?». Debe responder que no hay separación."),
    reinforce="Inventa un producto base y tres variaciones, y escribe qué cambia y qué debe probarse en cada una.",
    extend="Explica por qué las versiones sin alérgenos son más delicadas en pastelería que en otros alimentos.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 2 (registro de versiones de ejemplo). «Bizcocho de ejemplo». Versión 1 (base): harina 500 g, azúcar 200 g, huevo 250 g, mantequilla 150 g; vida útil de ejemplo, 4 días. Versión 2 (menos azúcar): azúcar 150 g; vida útil de ejemplo, 3 días. "
     "Versión 3 (formato mini): misma formulación que la versión 1, en porciones de 25 g. Evaluación sensorial de 8 personas (escala de 1 a 5; máximo 40): versión 1, 32; versión 2, 30; versión 3, 38. Aprueba la jefa de producción.")
build(
    O5, 2, F,
    use="Aprenderé a leer un registro de versiones de un producto de pastelería y a usar porcentajes, pesos y evaluaciones para entender el efecto de cada variación.",
    prior=["Conozco la variación y la versión.", "Sé calcular porcentajes.", "Sé calcular el peso total de una formulación."],
    explain=[
        "El registro de versiones anota cada variación: qué ingredientes cambian, las cantidades, la vida útil, el resultado de la evaluación y quién la aprobó. Con él se compara cada versión con la base. La reducción de un ingrediente se calcula restando la cantidad nueva a la anterior, y su porcentaje, multiplicando por 100 y dividiendo por la cantidad anterior.",
        "El peso total de una formulación es la suma de sus ingredientes. Para un formato mini se calcula el número de unidades dividiendo el peso total por el peso de cada unidad. La evaluación sensorial se compara por el porcentaje del máximo: la suma de puntajes por 100, dividida por el máximo posible, que es el número de personas por 5.",
        "Una variación puede mejorar un aspecto y empeorar otro, por ejemplo reducir el azúcar y acortar la vida útil. Por eso se decide mirando varios datos juntos. Los valores de esta ficha son de ejemplo." + LIM,
    ],
    vocab=[("reducción", "disminución de la cantidad de un ingrediente"), ("peso total", "suma de los ingredientes de una formulación"), ("unidad mini", "porción pequeña del mismo producto"), ("máximo posible", "personas por 5 puntos"), ("vida útil", "plazo durante el cual el producto puede usarse")],
    worked=[
        ("Calcular una reducción", "Una formulación de ejemplo pasa de 300 g a 240 g de un ingrediente. ¿Qué porcentaje se redujo?", ["Reducción: 300 − 240 = 60 g.", "60 × 100 ÷ 300 = 20."], "20 %"),
        ("Calcular unidades", "Una masa de ejemplo de 900 g se divide en porciones de 30 g. ¿Cuántas unidades salen?", ["Se divide el peso total por el peso de cada unidad.", "900 ÷ 30 = 30."], "30 unidades"),
    ],
    mistakes=[("Calcular el porcentaje de reducción dividiendo por la cantidad nueva.", "El porcentaje debe medirse respecto de la cantidad original.", "Divide la reducción por la cantidad anterior."),
              ("Elegir una versión solo porque obtuvo el puntaje más alto, sin mirar la vida útil.", "Una versión puede gustar y durar muy poco para el servicio.", "Compara puntaje, vida útil, costo y alérgenos.")],
    T=[
        ("=", "{F} ¿Cuántos gramos suman los ingredientes de la versión 1?", "500+200+250+150", "Se suman las cantidades de los cuatro ingredientes.", " g"),
        ("=", "{F} ¿Cuántos gramos suman los ingredientes de la versión 2?", "500+150+250+150", "Se suman las cantidades de los cuatro ingredientes de la versión 2.", " g"),
        ("=", "{F} ¿Cuántos gramos de azúcar se redujeron en la versión 2 respecto de la versión 1?", "200-150", "A la cantidad de azúcar de la versión 1 se le resta la de la versión 2.", " g"),
        ("=", "{F} ¿Qué porcentaje de reducción de azúcar tiene la versión 2?", "(200-150)*100//200", "Se multiplica la reducción por 100 y se divide por la cantidad original.", " %"),
        ("=", "{F} ¿Cuántas unidades mini de 25 g salen de la masa de la versión 3?", "1100//25", "Se divide el peso total de la formulación por el de cada unidad.", " unidades"),
        ("=", "{F} ¿Cuál es el puntaje máximo posible de la evaluación?", "8*5", "Se multiplican las personas por el puntaje más alto.", " puntos"),
        ("=", "{F} ¿Qué porcentaje del máximo obtuvo la versión 1?", "32*100//40", "Se multiplica la suma por 100 y se divide por el máximo posible.", " %"),
        ("=", "{F} ¿Qué porcentaje del máximo obtuvo la versión 3?", "38*100//40", "Se multiplica la suma por 100 y se divide por el máximo posible.", " %"),
        ("abc", "{F} ¿Qué versión obtuvo el menor puntaje en la evaluación?", "La versión 2", "La versión 1", "La versión 3", "La versión 2 sumó 30, menos que las otras dos."),
        ("abc", "{F} ¿Qué desventaja tiene la versión 2 en cuanto a su vida útil?", "Dura un día menos que la versión base", "Dura un día más que la versión base", "Dura lo mismo", "La ficha indica 3 días frente a los 4 de la versión base."),
        ("abc", "{F} Una compañera dice que la versión 2 es la mejor porque tiene menos azúcar, sin mirar más datos. ¿Qué respuesta es correcta?", "Debe compararse también el puntaje, la vida útil, el costo y los alérgenos", "Tiene razón, el azúcar es lo único importante", "No importa el azúcar", "Una decisión considera varios datos a la vez."),
        ("=", "{F} Si se produce el doble de la formulación de la versión 3, ¿cuántas unidades mini salen?", "2*1100//25", "Se duplica el peso total y se divide por el peso de cada unidad.", " unidades"),
        ("abc", "{F} ¿Quién aprueba las versiones?", "La jefa de producción", "El decorador", "El proveedor", "La ficha asigna la aprobación a la jefa de producción."),
    ],
    ctx=("abc", "{F} Una cliente quiere la versión 2, pero quiere recogerla cinco días después de su elaboración. ¿Qué debe informar la persona que atiende?", "Que la vida útil de ejemplo de esa versión es de 3 días, por lo que debe ajustarse la fecha de elaboración o de retiro", "Que no hay problema, porque dura una semana", "Que dura 4 días, como la base", "El plazo de cada versión se informa por separado."),
    sc=[
        ("En Pastelería y Repostería: ¿cómo se calcula el porcentaje de reducción?", "Reducción por 100, dividida por la cantidad original", "Se mide respecto de la cantidad anterior."),
        ("¿Cómo se calcula el número de unidades mini?", "Peso total dividido por el peso de cada unidad", "Reparte el peso total en porciones iguales."),
        ("¿Qué se compara además del puntaje?", "Vida útil, costo y alérgenos", "Una decisión usa varios datos a la vez."),
    ],
    op=("Registro de ejemplo. Versión 1 de un «Queque de ejemplo»: harina 600 g, azúcar 300 g, huevo 300 g, mantequilla 200 g; vida útil 5 días. Versión 2: azúcar 240 g; vida útil 4 días. Evaluación de 8 personas: versión 1, suma 34; versión 2, suma 32. "
        "Calcula la reducción de azúcar y su porcentaje, el peso total de cada versión, el porcentaje del máximo de cada una y la diferencia de vida útil.",
        "Reducción de azúcar: 300 − 240 = 60 g, es decir, 60 × 100 ÷ 300 = 20 %. Peso total: versión 1, 1.400 g; versión 2, 1.340 g. Máximo: 8 × 5 = 40. Versión 1: 34 × 100 ÷ 40 = 85 %. Versión 2: 32 × 100 ÷ 40 = 80 %. La versión 2 dura 1 día menos.",
        ["calcula 60 g y 20 %", "calcula 1.400 g, 1.340 g, 85 % y 80 %", "indica 1 día menos de vida útil"],
        ["hoja con cálculos"],
        ["dividir por la cantidad nueva", "olvidar el máximo", "no comparar la vida útil"],
        "Pregunta: «¿cuántos gramos suman los ingredientes de la versión 2?». Debe responder 1.340."),
    reinforce="Inventa dos versiones de un producto con cuatro ingredientes y calcula la reducción de un ingrediente y su porcentaje.",
    extend="Explica por qué una versión con menos azúcar puede tener una vida útil distinta.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 3 (costeo del formato mini, de ejemplo, inventado). Masa de 1.100 g con un costo de ingredientes de $4.400. Formato normal: porciones de 100 g (11 porciones) y empaque de $100 por porción. Formato mini: porciones de 25 g (44 unidades) y empaque de $50 por unidad. "
     "Costo objetivo: 40 % del precio de venta. Se entiende por costo de una porción la parte de la masa más su empaque.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso de variación de formato: calcular el costo por porción con empaque, fijar precios y comparar el formato normal con el mini.",
    prior=["Conozco el formato mini y el costo objetivo.", "Sé dividir y calcular precios.", "Conozco el registro de versiones."],
    explain=[
        "Cuando un producto cambia de formato, cambia el número de porciones y su costo. El costo de la masa por porción se obtiene dividiendo el costo de los ingredientes por las porciones; a ese costo se suma el empaque de cada porción. El costo total de una porción es la suma de ambos.",
        "El precio de venta de cada porción se calcula con el costo objetivo: se multiplica el costo de la porción por 100 y se divide por el porcentaje. Para comparar formatos con justicia se usa la misma cantidad de producto, por ejemplo 100 g: se calcula cuánto cuesta y cuánto se cobra por esa cantidad en cada formato.",
        "Un formato mini suele costar más por gramo porque lleva más empaque y trabajo, y se cobra por unidad, por lo que conviene que el cliente conozca el precio por cantidad. Los datos son de ejemplo y se calculan en papel." + LIM,
    ],
    vocab=[("empaque", "envoltorio o caja de cada porción"), ("costo de la porción", "parte de la masa más su empaque"), ("precio por cantidad", "precio de la misma cantidad de producto"), ("formato normal", "porción de tamaño habitual"), ("formato mini", "porción pequeña del mismo producto")],
    worked=[
        ("Calcular el costo de una porción", "Una masa de ejemplo cuesta $3.000 y rinde 10 porciones, con empaque de $80 cada una. ¿Cuánto cuesta cada porción?", ["Masa por porción: 3.000 ÷ 10 = 300.", "Con empaque: 300 + 80 = 380."], "$380"),
        ("Calcular el precio de venta", "El costo de una porción es $380 y el costo objetivo es 40 %. ¿Cuál es el precio de venta?", ["Se multiplica por 100 y se divide por 40.", "380 × 100 ÷ 40 = 950."], "$950"),
    ],
    mistakes=[("Olvidar el empaque al calcular el costo de la porción.", "El costo queda subestimado, sobre todo en el formato mini.", "Suma el empaque de cada porción al costo de la masa."),
              ("Comparar el precio de una unidad mini con el de una porción normal sin ajustar la cantidad.", "Se compara una cantidad distinta de producto.", "Compara los dos formatos con la misma cantidad, por ejemplo 100 g.")],
    T=[
        ("=", "{F} ¿Cuánto cuesta la masa de cada porción del formato normal?", "4400//11", "Se divide el costo de los ingredientes por las porciones.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta cada porción normal con su empaque?", "4400//11+100", "Se suman el costo de la masa por porción y el empaque.", " pesos"),
        ("=", "{F} ¿Cuál es el precio de venta de una porción normal?", "500*100//40", "Se multiplica el costo por 100 y se divide por el costo objetivo.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta la masa de cada unidad mini?", "4400//44", "Se divide el costo de los ingredientes por las unidades.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta cada unidad mini con su empaque?", "4400//44+50", "Se suman el costo de la masa por unidad y el empaque.", " pesos"),
        ("=", "{F} ¿Cuál es el precio de venta de una unidad mini?", "150*100//40", "Se multiplica el costo por 100 y se divide por el costo objetivo.", " pesos"),
        ("=", "{F} ¿Cuántas unidades mini equivalen a 100 g de producto?", "100//25", "Se divide la cantidad de 100 g por el peso de cada unidad mini.", " unidades"),
        ("=", "{F} ¿Cuánto cuesta comprar 100 g en formato mini?", "4*375", "Se multiplica el precio de una unidad mini por las unidades de 100 g.", " pesos"),
        ("abc", "{F} Comparando 100 g de cada formato, ¿cuál es más caro para el cliente?", "El formato mini, porque lleva más empaque por gramo", "El formato normal, porque pesa más", "Cuestan lo mismo", "Con 100 g, el mini cuesta $1.500 y el normal $1.250."),
        ("=", "{F} ¿Cuántos pesos más caro es el formato mini que el normal por cada 100 g?", "1500-1250", "Al precio de 100 g en mini se le resta el precio de 100 g en normal.", " pesos"),
        ("abc", "{F} Un cliente pregunta por qué el mini sale más caro por gramo. ¿Qué respuesta es adecuada?", "Porque cada unidad lleva su empaque y requiere más trabajo", "Porque el mini lleva menos ingredientes de calidad", "Porque hay un error de cobro", "La explicación se basa en los costos de empaque y trabajo, sin engaños."),
        ("=", "{F} Si se venden las 44 unidades mini al precio calculado, ¿cuánto se obtiene?", "375*44", "Se multiplica el precio de una unidad por las unidades vendidas.", " pesos"),
        ("abc", "{F} Una compañera propone cobrar el mini al mismo precio por unidad que la porción normal. ¿Qué observación corresponde?", "El mini pesa una cuarta parte y no se justificaría cobrar lo mismo; debe aplicarse el costo objetivo", "Es lo más justo", "Es lo más económico para el cliente", "El precio debe reflejar el costo real de cada formato."),
    ],
    ctx=("abc", "{F} La jefa debe decidir si ofrece el formato mini para un evento de 50 personas, con 4 minis por persona. ¿Qué datos de la ficha le ayudan a decidir?", "El costo y el precio de cada unidad mini, y la cantidad total de unidades necesaria", "Solo el costo de la masa", "El precio del formato normal", "El costo por unidad y el total de unidades permiten calcular el pedido."),
    sc=[
        ("En Pastelería y Repostería: ¿cómo se calcula el costo de una porción con empaque?", "Costo de la masa por porción más el empaque", "Suma los dos componentes del costo."),
        ("¿Por qué el mini suele costar más por gramo?", "Porque lleva más empaque y trabajo", "Cada unidad pequeña lleva su empaque."),
        ("¿Con qué se comparan dos formatos?", "Con la misma cantidad de producto", "Así la comparación entre formatos es justa."),
    ],
    op=("Masa de ejemplo de 900 g con un costo de $3.600. Formato normal: porciones de 90 g con empaque de $60. Formato mini: porciones de 30 g con empaque de $30. Costo objetivo: 40 %. "
        "Calcula las porciones de cada formato, el costo con empaque de cada porción, el precio de venta, y compara cuánto cuesta 90 g en cada formato.",
        "Normal: 900 ÷ 90 = 10 porciones; masa $360 + empaque $60 = $420; precio 420 × 100 ÷ 40 = $1.050. Mini: 900 ÷ 30 = 30 unidades; masa $120 + empaque $30 = $150; precio 150 × 100 ÷ 40 = $375. 90 g en mini son 3 unidades: 3 × 375 = $1.125, más que los $1.050 del formato normal.",
        ["calcula porciones y costos con empaque", "calcula los precios de venta", "compara 90 g en cada formato"],
        ["hoja con cálculos y comparación"],
        ["olvidar el empaque", "comparar cantidades distintas", "no aplicar el costo objetivo"],
        "Pregunta: «¿cuántas unidades mini hay en 90 g?». Debe responder 3."),
    reinforce="Inventa una masa con su costo y dos formatos, y calcula el precio de cada unidad.",
    extend="Explica por qué dos formatos del mismo producto tienen precios por gramo distintos.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 4 (comparación de variaciones, de ejemplo, inventada). Tres variaciones de un queque, evaluadas por 8 personas con escala de 1 a 5 (máximo 40). Variación A (menos azúcar): suma 28; vida útil 3 días; costo por porción $380. Variación B (relleno alternativo): suma 34; vida útil 2 días; costo por porción $420. "
     "Variación C (formato mini): suma 36; vida útil 4 días; costo por unidad $150. Criterio de ejemplo para adoptar una variación: al menos 80 % del máximo, vida útil de al menos 3 días y costo por unidad de hasta $450; si más de una cumple, se elige la de mayor porcentaje.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: comparar variaciones por varias condiciones a la vez y decidir cuál se adopta.",
    prior=["Conozco el registro de versiones.", "Sé calcular el porcentaje del máximo.", "Sé comparar valores con un criterio."],
    explain=[
        "Un criterio de adopción reúne varias condiciones medibles que una variación debe cumplir a la vez. En este caso son tres: un porcentaje mínimo del máximo en la evaluación sensorial, una vida útil mínima y un costo máximo por unidad. Basta que falle una condición para que la variación no se adopte.",
        "Se calcula el porcentaje del máximo con la suma de puntajes multiplicada por 100 y dividida por el máximo posible, que es el número de personas por 5. Luego se compara cada dato con su condición. Si más de una variación cumple, se elige la de mayor porcentaje. Si ninguna cumple, se mejora la receta o se mantiene la versión base.",
        "La decisión la aprueba la jefa de producción y se registra con los datos y el criterio aplicado, que se fija antes de revisar los resultados. Todo es un ejercicio en papel con datos de ejemplo." + LIM,
    ],
    vocab=[("criterio de adopción", "conjunto de condiciones que debe cumplir una variación"), ("condición", "requisito medible del criterio"), ("porcentaje del máximo", "suma por 100, dividida por el máximo posible"), ("desempate", "regla para elegir cuando más de una variación cumple")],
    worked=[
        ("Aplicar un criterio", "Una variación de ejemplo obtiene 85 % del máximo, vida útil de 2 días y costo de $300. El criterio exige al menos 80 %, vida útil de 3 días y costo hasta $450. ¿Se adopta?", ["Cumple el porcentaje y el costo.", "No cumple la vida útil."], "No se adopta"),
        ("Calcular el porcentaje", "Con 5 personas (máximo 25), una variación suma 21. ¿Qué porcentaje del máximo obtiene?", ["Se multiplica por 100 y se divide por 25.", "21 × 100 ÷ 25 = 84."], "84 %"),
    ],
    mistakes=[("Adoptar una variación porque cumple dos de las tres condiciones.", "El criterio exige cumplir todas a la vez.", "Verifica cada condición y adopta solo si cumple todas."),
              ("Cambiar el criterio después de ver los resultados.", "La decisión pierde objetividad.", "Define el criterio antes de la evaluación.")],
    T=[
        ("=", "{F} ¿Cuál es el puntaje máximo posible?", "8*5", "Se multiplican las personas por el puntaje más alto.", " puntos"),
        ("=", "{F} ¿Qué porcentaje del máximo obtuvo la variación A?", "28*100//40", "Se multiplica la suma por 100 y se divide por el máximo posible.", " %"),
        ("=", "{F} ¿Qué porcentaje del máximo obtuvo la variación B?", "34*100//40", "Se multiplica la suma por 100 y se divide por el máximo posible.", " %"),
        ("=", "{F} ¿Qué porcentaje del máximo obtuvo la variación C?", "36*100//40", "Se multiplica la suma por 100 y se divide por el máximo posible.", " %"),
        ("abc", "{F} ¿Por qué no se adopta la variación A?", "Porque no alcanza el 80 % del máximo", "Porque su costo supera $450", "Porque su vida útil es de menos de 3 días", "Obtiene 70 %, inferior al mínimo de 80 %."),
        ("abc", "{F} ¿Por qué no se adopta la variación B?", "Porque su vida útil es menor que 3 días", "Porque no alcanza el 80 % del máximo", "Porque su costo supera $450", "Cumple el porcentaje y el costo, pero dura solo 2 días."),
        ("abc", "{F} ¿Cumple la variación C todas las condiciones?", "Sí: 90 %, vida útil de 4 días y costo de $150", "No: su vida útil es menor que 3 días", "No: su costo supera $450", "Cumple las tres condiciones del criterio."),
        ("abc", "{F} Con el criterio de la ficha, ¿qué variación se adopta?", "La variación C", "La variación A", "La variación B", "Solo C cumple las tres condiciones."),
        ("=", "{F} ¿Cuántos días más de vida útil tiene la variación C que la variación B?", "4-2", "A la vida útil de C se le resta la de B.", " días"),
        ("=", "{F} Si la variación C se vendiera con un costo de $480 por unidad, ¿cuántos pesos superaría el máximo de $450?", "480-450", "Al costo se le resta el máximo permitido.", " pesos"),
        ("abc", "{F} Un compañero propone adoptar la variación B porque «gusta más que A». ¿Qué observación corresponde?", "No cumple la vida útil mínima; debe cumplirse todo el criterio", "Es válido, porque su porcentaje es alto", "Es válido si se reduce el costo", "El criterio exige cumplir todas las condiciones a la vez."),
        ("=", "{F} Si 50 personas piden 4 unidades de la variación C cada una, ¿cuántas unidades se necesitan?", "50*4", "Se multiplican las personas por las unidades de cada una.", " unidades"),
        ("abc", "{F} Si ninguna variación hubiera cumplido el criterio, ¿qué corresponde?", "Mejorar la receta o mantener la versión base", "Adoptar la que más se acerque", "Ofrecer todas sin registro", "Sin cumplir el criterio, no se adopta una variación."),
    ],
    ctx=("abc", "{F} La jefa debe registrar la decisión de adoptar la variación C. ¿Qué datos debe incluir?", "Las sumas, los porcentajes, las vidas útiles y los costos, el criterio aplicado y su aprobación", "Solo el nombre de la variación", "Solo el costo de la variación", "Un registro completo permite justificar y repetir la decisión."),
    sc=[
        ("En Pastelería y Repostería: ¿cuántas condiciones deben cumplirse para adoptar una variación?", "Todas las del criterio", "Basta que falle una para no adoptarla."),
        ("¿Cómo se calcula el porcentaje del máximo?", "Suma por 100, dividida por el máximo", "Permite comparar evaluaciones con distinto número de personas."),
        ("¿Cuándo se fija el criterio?", "Antes de revisar los resultados", "Así la decisión de adoptar es objetiva."),
    ],
    op=("Variaciones D y E de un bizcocho, evaluadas por 10 personas (máximo 50). D: suma 44; vida útil 4 días; costo por unidad $400. E: suma 46; vida útil 2 días; costo por unidad $350. Criterio: al menos 80 % del máximo, vida útil de al menos 3 días y costo de hasta $450. "
        "Calcula el máximo y el porcentaje de cada una, verifica las tres condiciones y decide cuál se adopta, indicando qué registrarías.",
        "Máximo: 10 × 5 = 50. D: 44 × 100 ÷ 50 = 88 %. E: 46 × 100 ÷ 50 = 92 %. D cumple porcentaje, vida útil (4) y costo (400). E cumple porcentaje y costo, pero su vida útil es de 2 días. Se adopta D. Se registran los puntajes, las vidas útiles, los costos, el criterio y la aprobación.",
        ["calcula 50, 88 % y 92 %", "verifica las tres condiciones de cada una", "decide D y señala los datos a registrar"],
        ["hoja con cálculos, decisión y registro"],
        ["elegir E por su porcentaje", "olvidar la vida útil", "no registrar la decisión"],
        "Pregunta: «¿cuántos días dura E?». Debe responder 2, menos que el mínimo."),
    reinforce="Inventa dos variaciones con puntaje, vida útil y costo, y decide cuál se adopta con un criterio de tres condiciones.",
    extend="Explica por qué un criterio con varias condiciones protege mejor al cliente que uno con una sola.",
)
