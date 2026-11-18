"""Acuicultura TP 3.º y 4.º medio: OAE-06 (sistemas, equipos y maquinarias, solo conceptos y documentos), OAE-07 (registros de producción) y OAE-08 (ética, seguridad y medio ambiente). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_acui_common import AVISO, EMER, build

O6 = "TP-ACUI-3y4-OAE-06"

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El centro ficticio «Centro Demo» tiene estos equipos: una bomba de agua, un soplador de aire, un alimentador automático de alimento, una grúa en el muelle y una embarcación de apoyo. "
     "Peligros anotados: partes móviles sin protección, cables eléctricos cerca del agua, ruido, cargas suspendidas y piso resbaladizo en el muelle.")
build(
    O6, 1, F,
    use="Aprenderé qué sistemas y equipos hay en un centro de cultivo, qué es el manual del fabricante y cómo se ordenan las medidas de prevención al usar equipos.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé qué es una pauta de mantención.", "Sé sumar, restar, multiplicar y dividir números enteros."],
    explain=[
        "Un centro de cultivo usa sistemas y equipos: bombas que mueven el agua, sopladores que entregan aire, alimentadores automáticos que reparten el alimento, grúas que levantan cargas y embarcaciones de apoyo. Cada equipo tiene un manual del fabricante, el documento que dice para qué sirve, cómo debe usarse y cuidarse, y qué advertencias de seguridad tiene. El instructivo es la guía breve de uso que se basa en ese manual. Solo usa un equipo una persona autorizada, es decir, formada y habilitada para ese equipo.",
        "Los equipos tienen peligros propios: partes móviles que atrapan, electricidad cerca del agua, ruido, cargas suspendidas y gases a presión en algunos sistemas. Se previenen con la jerarquía de controles: eliminar o sustituir el peligro, controles de ingeniería como un resguardo (una protección física sobre una parte móvil), controles administrativos como reglas y señales, y al final el EPP. Un equipo que falla se marca como «fuera de servicio» con una señal y se informa; no se improvisa una reparación.",
        f"Este cuaderno no describe cómo se opera ningún equipo ni embarcación, ni cómo se maneja un gas. {EMER} {AVISO}",
    ],
    vocab=[("manual del fabricante", "documento que dice para qué sirve un equipo, cómo usarlo y cuidarlo y sus advertencias"), ("instructivo", "guía breve de uso basada en el manual"), ("persona autorizada", "persona formada y habilitada para usar un equipo"), ("resguardo", "protección física sobre una parte móvil de un equipo"), ("fuera de servicio", "estado de un equipo que no debe usarse y está señalizado"), ("alimentador automático", "equipo que reparte el alimento sin que una persona lo entregue a mano")],
    worked=[
        ("Peligro y riesgo", "En un taller de ejemplo, una correa gira sin protección junto a un pasillo. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la parte móvil sin protección.", "El riesgo es que una persona se enganche la ropa o la mano y se lesione."], "Peligro: la parte móvil sin protección; riesgo: que alguien se enganche y se lesione"),
        ("Clasificar un control", "Un centro de ejemplo instala una cubierta fija sobre una correa que gira. ¿A qué nivel de la jerarquía corresponde?", ["La cubierta cambia físicamente el equipo.", "Los cambios físicos son controles de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Creer que leer el manual del fabricante habilita para usar el equipo.", "El manual informa, pero usar un equipo exige formación y autorización.", "Aprende el concepto y deja el uso a personas autorizadas."),
              ("Quitar un resguardo porque «molesta» para trabajar.", "Sin resguardo, la parte móvil vuelve a ser un peligro.", "Se informa al técnico; el resguardo solo lo retira personal autorizado.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es el manual del fabricante de un equipo?", "El documento que dice para qué sirve, cómo usarlo y cuidarlo y sus advertencias", "La lista de precios del vendedor", "El registro de lo que comió cada animal", "El manual contiene las indicaciones del fabricante; la lista de precios y los registros son otros documentos."),
        ("abc", "En Acuicultura: ¿qué es un resguardo en un equipo?", "Una protección física sobre una parte móvil", "Un cartel que dice «peligro»", "Un guante para quien lo usa", "El resguardo cambia el equipo; el cartel y el guante son medidas de otro nivel."),
        ("abc", "En Acuicultura: ¿qué significa que un equipo esté «fuera de servicio»?", "Que no debe usarse y está señalizado", "Que está funcionando a menor velocidad", "Que se usa solo en el turno de la noche", "Fuera de servicio quiere decir que no se usa hasta que lo revise personal autorizado."),
        ("=", "De los 5 equipos de la lista, 2 tienen resguardo en todas sus partes móviles. ¿Qué porcentaje de los equipos tiene resguardo completo?", "2*100//5", "Se multiplican los equipos con resguardo por 100 y se dividen entre el total.", " %"),
        ("abc", "{F} ¿Cuál es el riesgo asociado a las partes móviles sin protección?", "Que una persona se enganche y se lesione", "El nombre del equipo", "Que el equipo haga ruido", "El riesgo es la posibilidad de daño; el ruido es otro peligro."),
        ("abc", "{F} Una cubierta fija sobre las partes móviles, instalada por personal autorizado, es un control de tipo:", "De ingeniería, porque cambia físicamente el equipo", "Administrativo, porque es una regla", "De EPP, porque protege a quien lo usa", "La cubierta modifica el equipo y no depende de que cada persona la recuerde."),
        ("abc", "{F} Un cartel que dice «no acercarse al equipo en movimiento» es un control de tipo:", "Administrativo, porque informa y ordena una conducta", "De ingeniería, porque cambia el equipo", "De eliminación, porque quita el peligro", "Un cartel solo informa; no quita ni cubre el peligro."),
        ("abc", "{F} Una estudiante dice: «leí el manual de la grúa, así que puedo usarla». ¿Qué respuesta es correcta?", "Es falso: usar una grúa exige persona autorizada, formación y norma vigente", "Es cierto, si usa casco", "Es cierto, si otra persona la mira", "Leer el manual no habilita; el casco o la compañía tampoco."),
        ("abc", "{F} Durante una visita de ejemplo, una persona queda atrapada en el soplador. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar sacarla tirando de su ropa", "Tocar el equipo para detenerlo", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("=", "El centro de ejemplo tiene 30 personas y a cada capacitación sobre equipos caben 10. ¿Cuántas capacitaciones se necesitan?", "30//10", "Se divide el total de personas entre las que caben en cada capacitación.", " capacitaciones"),
        ("abc", "{F} El alimentador automático falla. ¿Qué corresponde hacer?", "Marcarlo como fuera de servicio e informar al técnico", "Abrirlo y repararlo con las herramientas que haya", "Dejarlo funcionando mientras se avisa", "Un equipo que falla no se repara de manera improvisada."),
        ("abc", "{F} Para el riesgo de cables eléctricos cerca del agua, ¿qué medida de nivel más efectivo se podría sumar a un cartel?", "Una canalización fija de cables instalada por personal autorizado", "Otro cartel con la misma advertencia", "Pedir a cada persona que use botas", "La canalización es un control de ingeniería; el cartel es administrativo y las botas son EPP."),
        ("abc", "En Acuicultura: ¿por qué un resguardo no se retira porque «molesta» al trabajar?", "Porque sin él la parte móvil vuelve a ser un peligro", "Porque el resguardo solo sirve de adorno", "Porque retirarlo mejora la seguridad", "El resguardo es una barrera que protege a quien se acerca."),
    ],
    ctx=("abc", "Un vecino te pide ayuda para encender y mover la grúa de su muelle «solo esta vez», sin autorización. ¿Qué respondes?", "Que no, porque usar una grúa exige persona autorizada, formación y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, si hay buen tiempo", "Que sí, si vas con casco", "Haber visto el concepto no habilita para usar un equipo de levante."),
    sc=[
        ("En Acuicultura: ¿qué es un resguardo?", "Una protección física sobre una parte móvil", "El resguardo cambia el equipo para quitar el contacto."),
        ("¿Qué indica el manual del fabricante?", "Para qué sirve el equipo, cómo usarlo y cuidarlo y sus advertencias", "El manual es el documento oficial del equipo."),
        ("¿Qué se hace con un equipo que falla?", "Se marca como fuera de servicio y se informa", "Un equipo que falla no se repara de forma improvisada."),
    ],
    op=("El centro ficticio «Centro Demo» anota una situación de ejemplo: un pasillo que pasa junto a un soplador que gira sin cubierta, sobre un piso mojado. Escribe (a) el peligro y el riesgo asociado, (b) un control administrativo, (c) un control de ingeniería, (d) por qué el EPP no basta y quién hace la tarea.",
        "(a) Peligro: parte móvil sin protección y piso mojado; riesgo: que la persona se enganche o resbale y se lesione. (b) Una regla escrita que prohíba acercarse al equipo en movimiento. (c) Un resguardo fijo sobre la parte móvil instalado por personal autorizado. (d) El EPP es la última barrera y no quita el peligro; la tarea la hace una persona autorizada.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer solo el EPP", "no aclarar que la tarea la hace una persona autorizada"],
        "Pregunta: «¿qué control cambia el equipo y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres equipos de un centro de cultivo y para cada uno un peligro posible.",
    extend="Explica por qué el manual del fabricante no reemplaza la autorización para usar un equipo.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (registro de ejemplo, inventado). Centro Demo, planilla de equipos. Soplador S-1: se usa 12 horas al día; mantención primaria cada 600 horas de uso; acumula 444 horas desde la última. "
     "Bomba B-2: se usa 16 horas al día; mantención primaria cada 800 horas de uso; acumula 560 horas desde la última. Documentos: el manual del fabricante, la pauta de mantención, la hoja de vida del equipo y el registro de uso (horas por día). "
     "Para los equipos de buceo, la inspección sigue el manual del fabricante y la hace personal certificado.")
build(
    O6, 2, F,
    use="Aprenderé los documentos de un equipo, los roles de quienes lo usan y cómo se calcula cuándo corresponde su próxima mantención con horas de uso de ejemplo.",
    prior=["Sé qué es el manual del fabricante y una pauta de mantención.", "Sé multiplicar y dividir números enteros.", "Sé qué es una hoja de vida."],
    explain=[
        "Los equipos se gestionan con documentos. El manual del fabricante dice cómo usar y cuidar el equipo. La pauta de mantención fija cada cuántas horas de uso o días se revisa. La hoja de vida anota cada revisión y reparación con fecha y responsable. El registro de uso anota las horas que trabaja el equipo. Con las horas acumuladas desde la última mantención y las horas de uso diarias se puede calcular cuántos días faltan para la próxima: se resta lo acumulado al intervalo y se divide entre las horas diarias.",
        "Cada rol cumple una función. La persona autorizada usa el equipo; el técnico decide la mantención; el jefe del centro organiza los equipos; el prevencionista asesora en riesgos. Los equipos de buceo y otros de alto riesgo solo los inspecciona y usa personal certificado, según el manual y la norma vigente.",
        f"Las cifras de esta clase son de ejemplo para una planilla; los valores reales los fija el fabricante. {EMER} {AVISO}",
    ],
    vocab=[("intervalo de mantención", "horas de uso entre una mantención y la siguiente"), ("horas acumuladas", "horas de uso desde la última mantención"), ("registro de uso", "documento con las horas que trabaja un equipo"), ("persona certificada", "persona con certificación vigente para usar o inspeccionar un equipo de alto riesgo")],
    worked=[
        ("Días para la próxima mantención", "Un equipo de ejemplo se revisa cada 300 horas, acumula 180 y trabaja 10 horas al día. ¿Cuántos días faltan?", ["Faltan 300 − 180 = 120 horas.", "120 ÷ 10 = 12."], "12 días"),
        ("Elegir el documento", "El técnico de un centro de ejemplo quiere ver cuántas horas trabajó un equipo la semana pasada. ¿Qué documento consulta?", ["Las horas de trabajo diarias se anotan en un registro de uso.", "Eso está en el registro de uso."], "El registro de uso"),
    ],
    mistakes=[("Dividir el intervalo completo entre las horas diarias sin restar las horas acumuladas.", "Parte de ese tiempo ya se usó.", "Primero se restan las horas acumuladas al intervalo."),
              ("Dejar la mantención «para cuando suene raro».", "La pauta fija cuándo hacerla, no el ruido.", "Se sigue la pauta y se anota en la hoja de vida.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es el intervalo de mantención de un equipo?", "Las horas de uso entre una mantención y la siguiente", "El precio de cada mantención", "El nombre de la persona que lo usa", "El intervalo mide el uso entre una mantención y otra."),
        ("abc", "En Acuicultura: ¿qué anota el registro de uso de un equipo?", "Las horas que trabaja el equipo", "Las semillas que se captan", "El precio de venta del producto", "El registro de uso lleva la cuenta del trabajo del equipo."),
        ("abc", "En Acuicultura: ¿quién inspecciona los equipos de buceo?", "Personal certificado, según el manual del fabricante y la norma vigente", "Cualquier persona con tiempo libre", "El estudiante que leyó el manual", "Los equipos de alto riesgo los inspecciona solo personal certificado."),
        ("=", "{F} ¿Cuántas horas faltan para la próxima mantención del soplador S-1?", "600-444", "Se resta lo acumulado al intervalo de mantención.", " horas"),
        ("=", "{F} ¿Cuántos días faltan para la próxima mantención del soplador S-1?", "(600-444)//12", "Se dividen las horas que faltan entre las horas de uso diarias.", " días"),
        ("=", "{F} ¿Cuántas horas faltan para la próxima mantención de la bomba B-2?", "800-560", "Se resta lo acumulado al intervalo de mantención.", " horas"),
        ("=", "{F} ¿Cuántos días faltan para la próxima mantención de la bomba B-2?", "(800-560)//16", "Se dividen las horas que faltan entre las horas de uso diarias.", " días"),
        ("abc", "{F} ¿Qué equipo necesitará primero su mantención?", "El soplador S-1, porque le faltan 13 días y a la bomba 15 días", "La bomba B-2, porque trabaja más horas al día", "Ambos al mismo tiempo", "Al soplador le faltan 13 días y a la bomba 15, por lo que el soplador va primero."),
        ("abc", "{F} ¿Qué documento anota quién hizo cada mantención y en qué fecha?", "La hoja de vida del equipo", "El registro de uso", "El manual del fabricante", "La hoja de vida guarda el historial; el registro de uso solo cuenta horas."),
        ("=", "{F} Si el soplador S-1 trabajara 6 horas al día, ¿cuántos días faltarían para su mantención?", "(600-444)//6", "Se dividen las horas que faltan entre 6 horas de uso diarias.", " días"),
        ("abc", "Suponte que en otra planilla de ejemplo un equipo ya pasó su intervalo de mantención y nadie la hizo. ¿Qué corresponde?", "Informar al técnico y anotar el atraso en la hoja de vida", "Esperar a que falle para avisar", "Anotar que ya se hizo", "Un atraso se informa y se registra; anotar algo no hecho falsifica el registro."),
        ("abc", "{F} Un estudiante calcula los días de S-1 como 600 ÷ 12. ¿Qué error cometió?", "No restó las horas acumuladas antes de dividir", "Ninguno, el cálculo es correcto", "Dividió entre las horas de la bomba", "Hay que dividir solo las horas que faltan, no el intervalo completo."),
        ("abc", "{F} Un compañero dice: «leí el manual, así que puedo hacer la mantención de la bomba». ¿Qué respuesta es correcta?", "Es falso: la mantención la hace personal autorizado según el manual", "Es cierto, porque el manual explica todo", "Es cierto, si usa guantes", "El manual orienta, pero la labor requiere formación y autorización."),
    ],
    ctx=("abc", "Una compañera te propone anotar en la hoja de vida una mantención que no se hizo, para tener la pauta «al día». ¿Qué respondes?", "Que no, porque anotar algo que no se hizo es falsificar un registro, y que se lo contarás a un adulto responsable", "Que sí, si después la hace", "Que sí, con una fecha anterior", "Un registro falso oculta la realidad y puede esconder un riesgo."),
    sc=[
        ("En Acuicultura: ¿cómo se calculan los días hasta la próxima mantención?", "(Intervalo − horas acumuladas) ÷ horas de uso diarias", "Primero se resta lo ya usado."),
        ("¿Qué documento guarda el historial del equipo?", "La hoja de vida", "La hoja anota revisiones y reparaciones."),
        ("¿Quién inspecciona un equipo de buceo?", "Personal certificado", "Es un equipo de alto riesgo."),
    ],
    op=("Ficha de ejemplo: aireador A-3 con intervalo de 400 horas de uso, 280 horas acumuladas y 8 horas de uso al día. Escribe (a) cuántas horas faltan para la mantención, (b) cuántos días faltan, (c) en qué documento se anota la mantención cuando se haga, (d) quién la hace.",
        "(a) 400 − 280 = 120 horas. (b) 120 ÷ 8 = 15 días. (c) En la hoja de vida del equipo, con fecha y responsable. (d) Personal autorizado, según el manual del fabricante.",
        ["calcula las horas que faltan", "calcula los días", "nombra la hoja de vida", "nombra quién la hace"],
        ["hoja con las cuatro respuestas"],
        ["dividir el intervalo completo", "no restar lo acumulado", "decir que la hace cualquier persona"],
        "Pregunta: «¿qué restas al intervalo antes de dividir?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un equipo con intervalo, horas acumuladas y uso diario, y calcula los días para su próxima mantención.",
    extend="Explica por qué una mantención atrasada se informa y no se oculta.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (registro de ejemplo, inventado). Centro Demo, mes de 30 días (720 horas). Soplador S-1: potencia de 5 kW, se usa 12 horas al día; detenido por falla 36 horas en el mes. "
     "Soplador S-2: potencia de 4 kW, se usa 12 horas al día; detenido por falla 72 horas en el mes. Precio de ejemplo de la energía: $150 por kWh. Un kWh es la energía de un equipo de 1 kW que trabaja una hora.")
build(
    O6, 3, F,
    use="Aprenderé a analizar el registro de dos equipos: calcular el consumo de energía y su costo, la disponibilidad y las horas detenidas, y proponer causas probables que hay que comprobar.",
    prior=["Sé qué es un registro de uso y una hoja de vida.", "Sé calcular un porcentaje con números enteros.", "Sé multiplicar números enteros."],
    explain=[
        "El consumo de energía de un equipo en kWh se calcula multiplicando su potencia en kW por las horas que trabaja. El costo se obtiene multiplicando los kWh por el precio de cada kWh. La disponibilidad es el porcentaje del tiempo en que el equipo estuvo en condiciones de trabajar: (horas totales − horas detenidas) × 100 ÷ horas totales. Un equipo con baja disponibilidad deja al cultivo sin su servicio durante más tiempo.",
        "Analizar un caso es leer los datos, compararlos y proponer acciones. Si un equipo tiene muchas horas detenidas, hay causas probables que se deben comprobar en la hoja de vida y en las pautas de mantención: falta de mantención, desgaste o uso fuera de lo indicado. Se informa al técnico con los registros como respaldo; no se cambian cifras ni se improvisan reparaciones.",
        f"Los precios y las potencias son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("potencia", "energía por hora que consume un equipo, medida en kW"), ("kWh", "energía de un equipo de 1 kW que trabaja una hora"), ("consumo de energía", "potencia en kW multiplicada por las horas de trabajo"), ("disponibilidad", "porcentaje del tiempo en que el equipo estuvo en condiciones de trabajar"), ("horas detenidas", "horas en que el equipo no pudo trabajar por una falla")],
    worked=[
        ("Costo de energía", "Un equipo de ejemplo de 2 kW trabaja 10 horas y el kWh cuesta $100. ¿Cuánto cuesta?", ["Consumo: 2 × 10 = 20 kWh.", "Costo: 20 × 100 = 2.000."], "$2.000"),
        ("Disponibilidad", "En 100 horas de ejemplo, un equipo estuvo detenido 10. ¿Cuál es la disponibilidad?", ["Horas disponibles: 100 − 10 = 90.", "90 × 100 ÷ 100 = 90."], "90 %"),
    ],
    mistakes=[("Calcular el consumo sumando potencia y horas.", "El consumo es potencia por horas, no su suma.", "Multiplica los kW por las horas."),
              ("Concluir que el soplador S-2 falla por antiguo, sin mirar la hoja de vida.", "La antigüedad puede ser una causa, pero no está comprobada.", "Se plantea como causa probable y se comprueba con los registros.")],
    T=[
        ("abc", "En Acuicultura: ¿cómo se calcula el consumo de energía de un equipo?", "Multiplicando la potencia en kW por las horas de trabajo", "Sumando la potencia y las horas", "Dividiendo las horas entre el precio", "El consumo en kWh es potencia por horas."),
        ("abc", "En Acuicultura: ¿qué es la disponibilidad de un equipo?", "El porcentaje del tiempo en que estuvo en condiciones de trabajar", "El número de equipos del centro", "El precio de arriendo del equipo", "La disponibilidad mide el tiempo útil respecto del total."),
        ("abc", "En Acuicultura: ¿qué son las horas detenidas de un equipo?", "Las horas en que no pudo trabajar por una falla", "Las horas en que el centro estaba cerrado", "Las horas de la última mantención", "Las horas detenidas son por falla y reducen la disponibilidad."),
        ("=", "{F} ¿Cuántos kWh consume el soplador S-1 en un día?", "5*12", "Se multiplica la potencia por las horas de uso diarias.", " kWh"),
        ("=", "{F} ¿Cuánto cuesta en pesos la energía de S-1 en un día?", "5*12*150", "Se multiplican los kWh del día por el precio de cada kWh.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta la energía de S-2 en un día?", "4*12*150", "Se multiplica la potencia por las horas y por el precio del kWh.", " pesos"),
        ("=", "{F} ¿Cuál es la disponibilidad de S-1 en el mes, en %?", "(720-36)*100//720", "Se restan las horas detenidas a las totales y se calcula el porcentaje.", " %"),
        ("=", "{F} ¿Cuál es la disponibilidad de S-2 en el mes, en %?", "(720-72)*100//720", "Se restan las horas detenidas a las totales y se calcula el porcentaje.", " %"),
        ("abc", "{F} ¿Qué soplador tuvo menor disponibilidad?", "S-2", "S-1", "Ambos tuvieron la misma", "S-2 estuvo detenido 72 horas y S-1 solo 36."),
        ("=", "{F} ¿Cuántas horas más estuvo detenido S-2 que S-1?", "72-36", "Se resta la menor cantidad de horas detenidas a la mayor.", " horas"),
        ("abc", "{F} Alguien afirma que S-2 falla por ser el más antiguo. ¿Qué conclusión es adecuada?", "Es una causa probable que hay que comprobar con la hoja de vida", "Queda demostrado porque tiene más fallas", "No puede tener ninguna relación con la antigüedad", "Una causa se plantea como probable y se comprueba con los registros."),
        ("abc", "{F} ¿Qué documento se consulta primero para investigar las fallas de S-2?", "La hoja de vida de S-2", "La guía de despacho de la cosecha", "El plan de manejo de las jaulas", "La hoja de vida guarda las fallas y reparaciones del equipo."),
        ("abc", "{F} Una persona propone reparar S-2 por su cuenta «para ahorrar». ¿Qué corresponde?", "Informar al técnico, porque la reparación la hace personal autorizado", "Hacerlo de inmediato con las herramientas que haya", "Esperar a que falle de nuevo sin avisar", "Reparar un equipo sin formación es peligroso y rompe el manual."),
    ],
    ctx=("abc", "El jefe de un centro de ejemplo te pide anotar menos horas detenidas de S-2 «para que el informe quede bien». ¿Qué haces?", "No alterar el registro y avisar a un adulto responsable, como tu profesor o profesora de especialidad", "Anotar solo unas pocas horas menos", "Anotarlo y avisar después", "Alterar un registro oculta la realidad; ante la presión se consulta a un adulto responsable."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula el costo de la energía?", "Potencia × horas × precio del kWh", "Primero se calcula el consumo y luego se multiplica por el precio."),
        ("¿Cómo se calcula la disponibilidad?", "(Horas totales − horas detenidas) × 100 ÷ horas totales", "Mide el tiempo útil del equipo."),
        ("¿Qué es una causa probable?", "Una explicación posible que hay que comprobar", "Una causa probable se verifica con los registros del equipo."),
    ],
    op=("Ficha de ejemplo: aireador A-5 de 3 kW que trabaja 10 horas al día; en un mes de 720 horas estuvo detenido 144 horas; el kWh cuesta $200 (de ejemplo). Escribe (a) el consumo diario, (b) el costo diario de energía, (c) la disponibilidad del mes, (d) una causa probable de la baja disponibilidad, indicando que hay que comprobarla.",
        "(a) 3 × 10 = 30 kWh. (b) 30 × 200 = 6.000 pesos. (c) (720 − 144) × 100 ÷ 720 = 80 %. (d) Una causa probable es una mantención atrasada; hay que comprobarlo en la hoja de vida y la pauta.",
        ["calcula el consumo", "calcula el costo", "calcula la disponibilidad", "presenta la causa como probable"],
        ["hoja con las cuatro respuestas"],
        ["sumar potencia y horas", "olvidar el precio del kWh", "tomar la causa como segura"],
        "Pregunta: «¿qué documento te ayudaría a comprobar la causa?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un equipo con potencia, horas diarias y precio del kWh, y calcula su costo diario.",
    extend="Explica por qué una baja disponibilidad puede costar más que el consumo de energía.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (caso de ejemplo, inventado). Centro Demo debe asegurar la aireación de una sala con una demanda de aire de ejemplo de 240 unidades por hora. Cada soplador de ejemplo entrega 80 unidades por hora. "
     "Regla de ejemplo del centro: además de los sopladores necesarios, se mantiene 1 soplador de respaldo (reserva). Cada soplador cuesta $400.000 (de ejemplo) y su mantención anual cuesta $50.000.")
build(
    O6, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular cuántos equipos se necesitan según su capacidad, por qué se mantiene un respaldo y cuánto costaría el conjunto.",
    prior=["Sé qué es el manual del fabricante y la mantención.", "Sé multiplicar, dividir y sumar números enteros.", "Sé qué es una especificación técnica."],
    explain=[
        "La capacidad de un equipo es lo que puede entregar por hora o por día, según su especificación técnica. Para saber cuántos equipos se necesitan se divide la demanda entre la capacidad de cada uno. Un equipo de respaldo es uno adicional que queda en reserva para entrar en servicio si otro falla; así el cultivo no queda sin el servicio. Por seguridad, un equipo no se usa por encima de su capacidad indicada.",
        "El costo del conjunto es la compra de todos los equipos (los necesarios y el respaldo) más sus mantenciones. La decisión la toma la jefatura con el técnico y se basa en el manual del fabricante; el estudiante calcula en papel y entrega el resultado escrito. Los números son de ejemplo.",
        f"Cómo se instala o se pone en marcha un equipo lo indica el manual y lo hace personal autorizado; este cuaderno no lo describe. {EMER} {AVISO}",
    ],
    vocab=[("capacidad", "lo que un equipo puede entregar por hora o por día, según su especificación"), ("demanda", "cantidad que el cultivo necesita por hora o por día"), ("equipo de respaldo", "equipo adicional en reserva para entrar en servicio si otro falla"), ("costo del conjunto", "compra de todos los equipos más sus mantenciones")],
    worked=[
        ("Equipos necesarios", "Una demanda de ejemplo de 300 unidades por hora se cubre con equipos de 100 unidades. ¿Cuántos equipos se necesitan, sin respaldo?", ["Se divide la demanda entre la capacidad.", "300 ÷ 100 = 3."], "3 equipos"),
        ("Costo del conjunto", "Se compran 4 equipos de $200.000 y cada uno tiene una mantención de $20.000. ¿Cuánto cuesta el conjunto?", ["Compra: 4 × 200.000 = 800.000.", "Mantención: 4 × 20.000 = 80.000; total 880.000."], "$880.000"),
    ],
    mistakes=[("Usar un equipo por encima de su capacidad indicada «porque aguanta».", "La capacidad la fija el fabricante; exceder el límite aumenta el riesgo de falla.", "Se respeta la capacidad y se agrega otro equipo si hace falta."),
              ("Dejar el equipo de respaldo sin mantención porque «no se usa».", "Un respaldo sin mantención puede fallar justo cuando se necesita.", "El respaldo también se incluye en la pauta de mantención.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es la capacidad de un equipo?", "Lo que puede entregar por hora o por día, según su especificación", "El precio al que se compró", "El nombre de la persona que lo usa", "La capacidad es lo que el equipo puede entregar."),
        ("abc", "En Acuicultura: ¿qué es un equipo de respaldo?", "Un equipo adicional en reserva para entrar en servicio si otro falla", "Un equipo que se usa solo para medir el consumo", "El equipo que más aire entrega", "El respaldo asegura que el servicio continúe si otro falla."),
        ("abc", "En Acuicultura: ¿cómo se calcula cuántos equipos se necesitan?", "Dividiendo la demanda entre la capacidad de cada equipo", "Sumando la demanda y la capacidad", "Multiplicando el precio por los días", "Se divide la demanda entre la capacidad de cada equipo."),
        ("=", "{F} ¿Cuántos sopladores se necesitan para cubrir la demanda, sin contar el respaldo?", "240//80", "Se divide la demanda entre la capacidad de cada soplador.", " sopladores"),
        ("=", "{F} ¿Cuántos sopladores hay que tener contando el respaldo?", "240//80+1", "Se suman el soplador de respaldo a los necesarios.", " sopladores"),
        ("=", "{F} ¿Cuántos pesos cuesta comprar todos los sopladores, contando el respaldo?", "(240//80+1)*400000", "Se multiplican los sopladores por el precio de cada uno.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta la mantención anual de todos los sopladores?", "(240//80+1)*50000", "Se multiplican los sopladores por el costo de mantención de cada uno.", " pesos"),
        ("=", "{F} ¿Cuál es el costo del conjunto (compra más mantención anual)?", "(240//80+1)*400000+(240//80+1)*50000", "Se suman la compra de los sopladores y su mantención anual.", " pesos"),
        ("=", "{F} Si la demanda subiera a 320 unidades por hora, ¿cuántos sopladores se necesitarían, contando el respaldo?", "320//80+1", "Se divide la nueva demanda y se suma el respaldo.", " sopladores"),
        ("abc", "{F} Una persona propone usar solo 2 sopladores «porque aguantan más». ¿Qué corresponde?", "Respetar la capacidad indicada y usar los equipos necesarios", "Aceptarlo porque nadie lo notará", "Usarlos al máximo y sin mantención", "Exceder la capacidad indicada aumenta el riesgo de falla."),
        ("abc", "{F} El soplador de respaldo no tiene mantención porque «no se usa». ¿Qué problema tiene?", "Puede fallar justo cuando se necesite", "Ninguno, porque lo que no se usa no se gasta", "Que consume más energía parado", "Un respaldo sin mantención puede no funcionar cuando se lo necesita."),
        ("abc", "{F} Un compañero dice: «leí la especificación, así que puedo instalar los sopladores». ¿Qué respuesta es correcta?", "Es falso: la instalación la hace personal autorizado según el manual", "Es cierto, porque la especificación trae todo", "Es cierto, si usa casco", "La especificación informa, pero instalar exige formación y autorización."),
        ("abc", "{F} ¿Quién decide la compra de los equipos?", "La jefatura con el técnico", "El estudiante que hizo el cálculo", "El proveedor de los sopladores", "La decisión es de quienes tienen la responsabilidad; el estudiante entrega el cálculo."),
    ],
    ctx=("abc", "Un conocido te pide que «ajustes» el equipo de su centro para que entregue más de lo indicado por el fabricante. ¿Qué respondes?", "Que no, porque exceder la capacidad indicada es riesgoso y que consulte a un técnico autorizado", "Que sí, un poco", "Que sí, si lo hace de noche", "La capacidad la fija el fabricante; excederla aumenta el riesgo."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula el número de equipos?", "Demanda ÷ capacidad", "Cada equipo cubre una parte de la demanda."),
        ("¿Qué es un equipo de respaldo?", "Uno adicional en reserva", "Entra en servicio si otro falla."),
        ("¿Quién decide la compra?", "La jefatura con el técnico", "El estudiante solo entrega el cálculo escrito a la jefatura."),
    ],
    op=("Ficha de ejemplo: demanda de 450 unidades por hora; cada aireador entrega 150 unidades; regla de un respaldo; cada aireador cuesta $300.000 (de ejemplo). Escribe (a) cuántos aireadores se necesitan sin respaldo, (b) cuántos con respaldo, (c) el costo de compra del conjunto, (d) por qué el respaldo también necesita mantención.",
        "(a) 450 ÷ 150 = 3 aireadores. (b) 3 + 1 = 4 aireadores. (c) 4 × 300.000 = 1.200.000 pesos. (d) Porque un respaldo sin mantención puede fallar justo cuando se lo necesita.",
        ["calcula los equipos sin respaldo", "suma el respaldo", "calcula el costo", "explica la mantención del respaldo"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el respaldo", "multiplicar la demanda por la capacidad", "pensar que el respaldo no necesita mantención"],
        "Pregunta: «¿por qué se tiene un equipo extra?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una demanda y una capacidad, y calcula cuántos equipos se necesitan con un respaldo.",
    extend="Explica por qué usar un equipo por encima de su capacidad aumenta el riesgo de falla.",
)

O7 = "TP-ACUI-3y4-OAE-07"

# ============================================================ OAE-07, clase 1
F = ("Ficha 5 (caso de ejemplo, inventado). Centro Demo lleva cinco registros de producción: siembra (fecha, jaula, cantidad de alevines y peso medio), crecimiento (muestreos), mortalidad, alimentación y calidad del agua. "
     "Siembra de ejemplo en la jaula J-1: 12.000 alevines de «especie A» con un peso medio de 50 g cada uno. Un alevín es un pez joven que ya dejó de ser larva. En el centro, 50 registros de la semana se revisaron y 45 estaban completos.")
build(
    O7, 1, F,
    use="Aprenderé qué son los registros de producción, para qué se sistematizan y se informan las anomalías, y qué riesgos tiene llevar mal los registros.",
    prior=["Sé qué es un registro y la trazabilidad.", "Sé calcular un porcentaje con números enteros.", "Sé pasar de gramos a kilos."],
    explain=[
        "Un registro de producción es un documento donde se anotan datos del cultivo: la siembra (cuántos animales entran y cuánto pesan), el crecimiento, la mortalidad, la alimentación y la calidad del agua. Sistematizar es ordenar esos datos en tablas o formatos para poder compararlos y analizarlos. Una anomalía es un dato fuera de lo esperado; informar oportunamente es avisar apenas se detecta, con el registro como respaldo, y no esperar al informe mensual.",
        "Llevar mal los registros tiene riesgos: datos faltantes, errores al copiar, cifras alteradas o sin responsable, y filtración de datos personales de trabajadores. Se previenen con la jerarquía de controles: un control de ingeniería puede ser una planilla que no se guarda si falta la fecha; uno administrativo, que una segunda persona revise cada registro; y la privacidad exige compartir datos personales solo con quienes los necesitan. Trabajar muchas horas anotando también cansa: la ergonomía recomienda buena postura y pausas.",
        f"Un registro nunca se altera para que «se vea mejor». {EMER} {AVISO}",
    ],
    vocab=[("registro de producción", "documento donde se anotan datos del cultivo, como siembra, crecimiento, mortalidad y alimentación"), ("sistematizar", "ordenar los datos en tablas o formatos para compararlos y analizarlos"), ("anomalía", "dato fuera de lo esperado que hay que informar"), ("informar oportunamente", "avisar apenas se detecta un dato fuera de lo esperado"), ("alevín", "pez joven que ya dejó de ser larva"), ("datos personales", "información que identifica a una persona, como su nombre o su documento"), ("ergonomía", "cuidado de la postura y de las pausas al trabajar")],
    worked=[
        ("Biomasa de siembra", "Se siembran 2.000 alevines de ejemplo de 40 g cada uno. ¿Cuántos kilos de biomasa se siembran?", ["Gramos: 2.000 × 40 = 80.000.", "Kilos: 80.000 ÷ 1.000 = 80."], "80 kg"),
        ("Clasificar un control", "Una planilla de ejemplo no permite guardar un registro si falta la fecha. ¿A qué nivel de la jerarquía corresponde?", ["La planilla cambia la forma de registrar y no depende de que alguien lo recuerde.", "Eso es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Dejar de anotar un dato «porque es pequeño».", "Los datos pequeños pueden mostrar una tendencia importante.", "Se anota todo dato con fecha y responsable."),
              ("Compartir la lista con nombres y turnos de los trabajadores con quien la pida.", "Los datos personales solo se comparten con quienes los necesitan.", "Se consulta al responsable antes de compartirlos.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es un registro de producción?", "Un documento donde se anotan datos del cultivo, como siembra, mortalidad y alimentación", "Un plano de las jaulas del centro", "La lista de precios de los proveedores", "El registro de producción guarda datos del cultivo; el plano y los precios son otros documentos."),
        ("abc", "En Acuicultura: ¿qué significa sistematizar los datos?", "Ordenarlos en tablas o formatos para compararlos y analizarlos", "Guardarlos en un cajón para que no se pierdan", "Copiarlos a mano sin cambiarles nada", "Sistematizar es ordenar para poder analizar."),
        ("abc", "En Acuicultura: ¿qué es una anomalía en un registro?", "Un dato fuera de lo esperado que hay que informar", "Un dato anotado con lápiz azul", "El dato más repetido de la semana", "Una anomalía se define por salir de lo esperado."),
        ("=", "{F} ¿Cuántos kg de biomasa se sembraron en la jaula J-1?", "12000*50//1000", "Se multiplican los alevines por su peso en gramos y se pasa a kilos.", " kg"),
        ("=", "{F} ¿Qué porcentaje de los registros revisados de la semana estaba completo?", "45*100//50", "Se multiplican los registros completos por 100 y se dividen entre los revisados.", " %"),
        ("abc", "{F} Una planilla que no se puede guardar sin la fecha de siembra es un control de tipo:", "De ingeniería, porque cambia la forma de registrar", "Administrativo, porque es una regla escrita", "De EPP, porque protege a quien anota", "La planilla actúa sin depender de que cada persona lo recuerde."),
        ("abc", "{F} Que una segunda persona revise cada registro antes de archivarlo es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el formato", "De eliminación, porque quita el riesgo", "La revisión por otra persona es una regla de trabajo."),
        ("abc", "{F} ¿Cuál es el riesgo de anotar la siembra sin fecha ni responsable?", "Que no se pueda verificar el dato ni seguir su historia", "Que los alevines crezcan más lento", "Que el registro pese más", "Sin fecha ni responsable se pierde la trazabilidad."),
        ("abc", "{F} Una persona de otra empresa pide la lista con nombres y turnos de los trabajadores del centro. ¿Qué corresponde?", "Consultar al responsable, porque los datos personales se comparten solo con quienes los necesitan", "Entregarla porque la pidió con amabilidad", "Publicarla en un lugar visible", "Los datos personales exigen cuidado y consulta al responsable."),
        ("abc", "{F} La mortalidad de una jaula sube mucho el martes. ¿Cuándo corresponde informarlo?", "Apenas se detecta, con el registro como respaldo", "Al final del mes junto con los demás datos", "Solo si alguien lo pregunta", "Informar oportunamente permite actuar a tiempo."),
        ("=", "El centro de ejemplo anota 8 registros por jaula al día y tiene 6 jaulas. ¿Cuántos registros anota en un día?", "8*6", "Se multiplican los registros por jaula por el número de jaulas.", " registros"),
        ("abc", "{F} Una compañera propone cambiar el peso de siembra para que cuadre con la factura. ¿Qué respondes?", "Que no: se deja el dato real y se informa la diferencia al responsable", "Que sí, si lo corrige después", "Que sí, porque la factura manda", "Cambiar un dato oculta una diferencia que hay que investigar."),
        ("abc", "{F} Una persona anota registros sentada seis horas seguidas sin pausa y con dolor de espalda. ¿Qué recomienda la ergonomía?", "Hacer pausas, cuidar la postura y avisar si hay molestias", "Seguir sin pausa para terminar antes", "Cambiar solo la hora de la comida", "La ergonomía previene molestias con pausas y buena postura."),
    ],
    ctx=("abc", "Un conocido te pide que le envíes por mensaje fotos de los registros de tu centro de práctica, con nombres de trabajadores. ¿Qué respondes?", "Que no, porque los registros y los datos personales no se comparten sin autorización, y lo consultarás con un adulto responsable", "Que sí, si es solo una foto", "Que sí, si borras las fechas", "Compartir sin autorización puede dañar la privacidad de las personas."),
    sc=[
        ("En Acuicultura: ¿qué es sistematizar datos?", "Ordenarlos para compararlos y analizarlos", "Sistematizar ordena la información para poder analizarla."),
        ("¿Qué es una anomalía?", "Un dato fuera de lo esperado", "Una anomalía se informa a tiempo con el registro."),
        ("¿Cuándo se informa una anomalía?", "Apenas se detecta, con el registro como respaldo", "Un aviso tardío impide actuar a tiempo."),
    ],
    op=("El centro ficticio «Centro Demo» siembra 8.000 alevines de «especie B» de 30 g cada uno en la jaula J-3 y anota la siembra en una planilla sin fecha ni responsable. Escribe (a) la biomasa sembrada en kg, (b) qué riesgo tiene la planilla sin fecha ni responsable, (c) un control de ingeniería y uno administrativo para mejorarla, (d) qué harías con un dato raro.",
        "(a) 8.000 × 30 ÷ 1.000 = 240 kg. (b) No se puede verificar el dato ni seguir su historia, y se pierde la trazabilidad. (c) Ingeniería: una planilla que exija fecha y responsable para guardar; administrativo: una segunda persona revisa cada registro. (d) Dejarlo anotado, no cambiarlo e informar oportunamente al técnico.",
        ["calcula la biomasa", "identifica el riesgo", "propone dos controles de distinto nivel", "propone informar sin alterar"],
        ["hoja con las cuatro respuestas"],
        ["olvidar pasar de gramos a kilos", "proponer solo recordar anotar", "cambiar el dato raro"],
        "Pregunta: «¿qué dato permite saber quién anotó y cuándo?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe los cinco registros de producción de un centro de cultivo y un dato que anotarías en cada uno.",
    extend="Explica por qué una planilla que exige la fecha es mejor que un cartel que la recuerda.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 6 (registro de ejemplo, inventado). Centro Demo, jaula J-2 con 6.000 peces de «especie A» al inicio. Planilla de mortalidad diaria de seis días: 12, 8, 15, 10, 9 y 6 peces. "
     "Documentos: la planilla de mortalidad diaria (fecha, jaula, cantidad y responsable), la bitácora de alimentación y el informe semanal (resumen de la semana que se entrega a la jefatura).")
build(
    O7, 2, F,
    use="Aprenderé los formatos y documentos donde se registran los datos de producción, los conceptos de mortalidad acumulada y supervivencia, y los roles que intervienen.",
    prior=["Sé qué es un registro de producción y una anomalía.", "Sé calcular un porcentaje con números enteros.", "Sé sumar y calcular un promedio."],
    explain=[
        "Cada dato se anota en el formato que corresponde: la planilla de mortalidad diaria guarda cuántos peces mueren cada día, la bitácora de alimentación guarda lo entregado y el informe semanal resume la semana para la jefatura. La mortalidad acumulada es la suma de las mortalidades diarias hasta un día. La supervivencia es el porcentaje de animales que siguen vivos: 100 menos el porcentaje de mortalidad.",
        "El responsable de registro anota con fecha, cantidad y su nombre; el técnico revisa los datos; el jefe del centro recibe el informe; el prevencionista usa los registros de incidentes para mejorar la seguridad. Un registro correcto es legible, completo y verificable, y los datos personales se resguardan.",
        f"Si algo no cuadra, se informa; no se corrige a escondidas. {EMER} {AVISO}",
    ],
    vocab=[("planilla de mortalidad diaria", "formato donde se anota fecha, jaula, cantidad de muertos y responsable"), ("informe semanal", "resumen de la semana que se entrega a la jefatura"), ("mortalidad acumulada", "suma de las mortalidades diarias hasta un día"), ("supervivencia", "porcentaje de animales que siguen vivos"), ("responsable de registro", "persona que anota los datos con su nombre y la fecha")],
    worked=[
        ("Mortalidad acumulada", "En tres días de ejemplo mueren 5, 7 y 8 peces. ¿Cuál es la mortalidad acumulada?", ["Se suman los tres días.", "5 + 7 + 8 = 20."], "20 peces"),
        ("Supervivencia", "La mortalidad de un periodo de ejemplo fue 4 %. ¿Cuál es la supervivencia?", ["La supervivencia es lo que queda: 100 menos la mortalidad.", "100 − 4 = 96."], "96 %"),
    ],
    mistakes=[("Calcular la supervivencia como lo mismo que la mortalidad.", "Son complementos: una mide los vivos y la otra los muertos.", "La supervivencia es 100 menos la mortalidad."),
              ("Anotar los datos de la jaula sin el nombre de quien los anotó.", "Sin responsable no se puede verificar ni consultar el dato.", "Todo registro lleva fecha y responsable.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es la mortalidad acumulada?", "La suma de las mortalidades diarias hasta un día", "La mortalidad del primer día", "El peso de los peces muertos", "La acumulada suma los días; no es un dato de un solo día."),
        ("abc", "En Acuicultura: ¿qué es la supervivencia?", "El porcentaje de animales que siguen vivos", "El número de jaulas del centro", "El alimento que se entrega por día", "La supervivencia mide los vivos, no el alimento ni las jaulas."),
        ("abc", "En Acuicultura: ¿qué es el informe semanal?", "Un resumen de la semana que se entrega a la jefatura", "Una lista de personas autorizadas", "Un manual de instrucciones de un equipo", "El informe semanal resume los datos de la semana."),
        ("=", "{F} ¿Cuál es la mortalidad acumulada de los seis días?", "12+8+15+10+9+6", "Se suman las mortalidades diarias de los seis días.", " peces"),
        ("=", "{F} ¿Cuál es la mortalidad de la jaula en el periodo, en %?", "(12+8+15+10+9+6)*100//6000", "Se multiplica la mortalidad acumulada por 100 y se divide entre los peces iniciales.", " %"),
        ("=", "{F} ¿Cuál es la supervivencia de la jaula en el periodo, en %?", "100-(12+8+15+10+9+6)*100//6000", "Se resta la mortalidad al 100 %.", " %"),
        ("=", "{F} ¿Cuántos peces vivos quedan en la jaula al sexto día?", "6000-(12+8+15+10+9+6)", "Se resta la mortalidad acumulada a los peces iniciales.", " peces"),
        ("abc", "{F} ¿En qué documento se anota cuántos peces mueren cada día?", "En la planilla de mortalidad diaria", "En la bitácora de alimentación", "En el informe semanal", "La planilla diaria guarda las cifras de cada día; el informe resume y la bitácora registra alimento."),
        ("abc", "{F} ¿Qué documento resume la semana para la jefatura?", "El informe semanal", "La planilla de mortalidad diaria", "La bitácora de alimentación", "El informe semanal entrega el resumen; la planilla es el dato diario."),
        ("=", "{F} ¿En cuántos peces superó el día de mayor mortalidad al de menor mortalidad?", "15-6", "Se resta la menor cantidad de muertos a la mayor.", " peces"),
        ("abc", "{F} La planilla de ejemplo no tiene el nombre del responsable en dos días. ¿Qué corresponde?", "Informar al técnico para completar el dato con quien lo anotó, sin inventar nombres", "Poner un nombre cualquiera", "Dejarlo así sin avisar", "Un registro necesita responsable verificable; inventar nombres lo falsifica."),
        ("abc", "{F} El informe semanal dice 61 peces muertos y la planilla suma 60. ¿Qué corresponde?", "Informar la diferencia con ambos documentos, sin cambiar números", "Cambiar la planilla a 61 sin avisar", "Dejarlo así porque es solo uno", "Una diferencia se informa con evidencia; ocultarla impide corregirla."),
        ("abc", "{F} Un compañero propone no anotar los 6 peces del último día porque «ya se acabó la semana». ¿Qué respondes?", "Que no, porque cada dato se anota con su fecha", "Que sí, porque es poco", "Que sí, si lo anota la semana siguiente sin fecha", "Un dato omitido deja incompleto el registro."),
    ],
    ctx=("abc", "Una compañera te pide que anotes en la planilla su turno de mortalidad con tu nombre, porque ella no lo hizo. ¿Qué respondes?", "Que no, porque el registro debe llevar el nombre de quien realmente anotó, y que se lo contarás a un adulto responsable", "Que sí, por esta vez", "Que sí, si no se enteran", "Anotar con otro nombre falsifica la responsabilidad del registro."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula la supervivencia?", "100 menos el porcentaje de mortalidad", "Supervivencia y mortalidad son complementos entre sí."),
        ("¿Qué es la mortalidad acumulada?", "La suma de las mortalidades diarias", "La acumulada suma día a día."),
        ("¿Qué lleva todo registro correcto?", "Fecha y responsable", "Sin fecha ni responsable no se puede verificar."),
    ],
    op=("Ficha de ejemplo: jaula J-6 de «especie B» con 5.000 peces iniciales; mortalidad de cuatro días: 20, 30, 25 y 25 peces. Escribe (a) la mortalidad acumulada, (b) la mortalidad en %, (c) la supervivencia, (d) en qué documento se anotan los datos diarios y en cuál se resume la semana.",
        "(a) 20 + 30 + 25 + 25 = 100 peces. (b) 100 × 100 ÷ 5.000 = 2 %. (c) 100 − 2 = 98 %. (d) Los datos diarios en la planilla de mortalidad diaria; la semana se resume en el informe semanal.",
        ["suma la mortalidad acumulada", "calcula el porcentaje", "calcula la supervivencia", "nombra los dos documentos"],
        ["hoja con las cuatro respuestas"],
        ["usar la mortalidad como supervivencia", "dividir entre los peces vivos", "confundir los dos documentos"],
        "Pregunta: «¿cuál es el complemento de la mortalidad?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una planilla de cinco días de mortalidad y calcula la acumulada y la supervivencia de una jaula de 4.000 peces.",
    extend="Explica por qué el informe semanal no reemplaza a la planilla diaria.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 7 (registro de ejemplo, inventado). Centro Demo, jaula J-4 con 5.000 peces de «especie A» (se desprecia la mortalidad). Pesos medios al final de cada semana: semana 0, 100 g; semana 1, 130 g; semana 2, 170 g; semana 3, 200 g; semana 4, 250 g. "
     "Alimento entregado en cada semana: 300 kg, 400 kg, 450 kg y 500 kg. Meta de ejemplo: factor de conversión alimenticia (FCA) de 2 como máximo en cada semana.")
build(
    O7, 3, F,
    use="Aprenderé a analizar una serie semanal de registros de crecimiento y alimentación, calcular el FCA de cada semana y detectar una anomalía para informarla.",
    prior=["Sé calcular biomasa y FCA.", "Sé pasar de gramos a kilos.", "Sé qué es una anomalía y qué es una causa probable."],
    explain=[
        "Una serie de registros se analiza semana a semana. La biomasa de cada semana es los peces por el peso medio, pasando gramos a kilos. La ganancia semanal es la diferencia entre la biomasa de una semana y la anterior. El FCA semanal es el alimento entregado en la semana dividido por la ganancia de esa semana; un valor mayor que la meta es una anomalía y se informa.",
        "Para explicar una anomalía se plantean causas probables que hay que comprobar con más datos: alimento desperdiciado, cambios en el agua o muestreos poco representativos. No se afirma una causa sin evidencia, y nunca se cambian las cifras para que cumplan la meta. Se informa al técnico con el registro como respaldo.",
        f"Estas decisiones las toman el técnico y la jefatura; aquí analizas datos escritos. {EMER} {AVISO}",
    ],
    vocab=[("serie de registros", "datos del mismo tipo anotados semana tras semana"), ("ganancia semanal", "biomasa de una semana menos biomasa de la anterior"), ("FCA semanal", "alimento de la semana dividido entre la ganancia de la semana"), ("meta máxima", "mayor valor aceptable")],
    worked=[
        ("Ganancia semanal", "Una biomasa de ejemplo pasa de 200 kg a 260 kg en una semana. ¿Cuál es la ganancia?", ["Se resta la biomasa anterior a la nueva.", "260 − 200 = 60."], "60 kg"),
        ("FCA semanal", "En esa semana se entregan 120 kg de alimento. ¿Cuál es el FCA semanal?", ["Se divide el alimento entre la ganancia.", "120 ÷ 60 = 2."], "2"),
    ],
    mistakes=[("Calcular el FCA dividiendo la ganancia entre el alimento.", "El FCA relaciona el alimento con la ganancia, no al revés.", "Divide el alimento entre la ganancia."),
              ("Concluir que el alimento fue desperdiciado solo porque el FCA subió.", "Un FCA alto muestra que algo pasó, pero no prueba la causa.", "Se plantea como causa probable y se comprueba con datos.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es la ganancia semanal de biomasa?", "La biomasa de una semana menos la biomasa de la semana anterior", "El alimento entregado en la semana", "El número de peces vivos", "La ganancia es una diferencia de biomasa entre semanas."),
        ("abc", "En Acuicultura: ¿qué significa que el FCA de una semana supere la meta máxima?", "Que se usó más alimento por cada kilo ganado que lo esperado", "Que los peces ganaron más peso que lo esperado", "Que murieron más peces", "Un FCA más alto significa más alimento por kilo ganado."),
        ("abc", "En Acuicultura: ¿cómo se calcula la biomasa de una semana?", "Peces por peso medio, pasando gramos a kilos", "Alimento dividido entre peces", "Peso medio menos número de peces", "La biomasa es el peso total de los peces."),
        ("=", "{F} ¿Cuántos kg de biomasa tenía la jaula en la semana 0?", "5000*100//1000", "Se multiplican los peces por su peso en gramos y se pasa a kilos.", " kg"),
        ("=", "{F} ¿Cuántos kg de biomasa tenía la jaula en la semana 1?", "5000*130//1000", "Se multiplican los peces por su peso en gramos y se pasa a kilos.", " kg"),
        ("=", "{F} ¿Cuántos kg ganó la biomasa en la semana 1?", "5000*130//1000-5000*100//1000", "Se resta la biomasa de la semana 0 a la de la semana 1.", " kg"),
        ("=", "{F} ¿Cuántos kg ganó la biomasa en la semana 3?", "5000*200//1000-5000*170//1000", "Se resta la biomasa de la semana 2 a la de la semana 3.", " kg"),
        ("=", "{F} ¿Cuál es el FCA de la semana 3?", "450//(5000*200//1000-5000*170//1000)", "Se divide el alimento de la semana entre la ganancia de esa semana.", ""),
        ("=", "{F} ¿Cuál es el FCA de la semana 4?", "500//(5000*250//1000-5000*200//1000)", "Se divide el alimento de la semana entre la ganancia de esa semana.", ""),
        ("abc", "{F} ¿En qué semana el FCA superó la meta máxima?", "En la semana 3", "En la semana 2", "En la semana 4", "La semana 3 tuvo FCA de 3, mayor que 2; las semanas 1, 2 y 4 tuvieron 2."),
        ("abc", "{F} Alguien dice que el FCA de la semana 3 subió porque se desperdició alimento. ¿Qué conclusión es adecuada?", "Es una causa probable que hay que comprobar con más datos", "Queda demostrado porque el FCA subió", "No puede haber ninguna relación con el alimento", "Con un solo dato se plantea una causa probable, pero no se prueba."),
        ("abc", "{F} ¿Qué corresponde hacer con la anomalía de la semana 3?", "Informarla al técnico con el registro como respaldo", "Cambiar el alimento de la semana a 340 kg", "Dejar de anotar esa semana", "Una anomalía se informa; cambiar u ocultar el dato impide corregir."),
        ("abc", "{F} Se quiere comprobar si el muestreo de la semana 3 fue representativo. ¿Qué dato se revisa?", "Cuántos peces se midieron y cómo se eligieron", "El nombre del jefe del centro", "El precio del alimento", "La representatividad depende de la muestra medida."),
    ],
    ctx=("abc", "El jefe de un centro de ejemplo te pide corregir el alimento anotado de una semana para que el FCA «salga bien». ¿Qué haces?", "No alterar el registro y avisar a un adulto responsable, como tu profesor o profesora de especialidad", "Corregir solo un poco", "Corregirlo y avisar después", "Alterar un registro oculta la realidad; ante la presión se consulta a un adulto responsable."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula el FCA semanal?", "Alimento de la semana ÷ ganancia de la semana", "El FCA relaciona el alimento con la ganancia."),
        ("¿Qué es la ganancia semanal?", "La biomasa nueva menos la anterior", "La ganancia es una diferencia entre dos biomasas."),
        ("¿Qué se hace con un FCA sobre la meta?", "Se informa al técnico con el registro", "El dato real permite buscar causas."),
    ],
    op=("Ficha de ejemplo: jaula con 4.000 peces de «especie B»; pesos medios: semana 0, 200 g; semana 1, 250 g; semana 2, 300 g. Alimento entregado: semana 1, 400 kg; semana 2, 600 kg. Meta máxima de FCA: 2 (de ejemplo). Escribe (a) la biomasa de cada semana, (b) la ganancia de las semanas 1 y 2, (c) el FCA de ambas, (d) cuál supera la meta y qué haces.",
        "(a) Semana 0: 800 kg; semana 1: 1.000 kg; semana 2: 1.200 kg. (b) Ganancia de 200 kg en cada semana. (c) FCA semana 1: 400 ÷ 200 = 2; semana 2: 600 ÷ 200 = 3. (d) La semana 2 supera la meta; se informa al técnico con el registro como respaldo, sin cambiar el dato.",
        ["calcula las biomasas", "calcula las ganancias", "calcula los FCA", "identifica la anomalía"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "olvidar pasar a kilos", "cambiar el dato"],
        "Pregunta: «¿qué divides entre qué para el FCA?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres semanas de peso medio y alimento, y calcula el FCA de cada semana.",
    extend="Explica por qué un solo FCA alto no prueba por sí solo la causa.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 8 (registro de ejemplo, inventado). Centro Demo, registro diario de calidad del agua de una jaula durante 8 días. Temperatura en grados: 12, 13, 15, 18, 19, 16, 14 y 13. "
     "Oxígeno disuelto en unidades de planilla (de ejemplo): 9, 9, 8, 6, 5, 8, 9 y 9. Rango de ejemplo de la temperatura: de 11 a 17 grados. Mínimo de ejemplo del oxígeno disuelto: 7 unidades.")
build(
    O7, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: comparar los registros de calidad del agua con un rango, calcular promedios y porcentajes y decidir qué informar.",
    prior=["Sé qué es un registro, un rango y una anomalía.", "Sé calcular un promedio y un porcentaje con números enteros.", "Sé qué es una causa probable."],
    explain=[
        "La calidad del agua es el conjunto de condiciones del agua que importan al cultivo. Cada condición es un parámetro, como la temperatura y el oxígeno disuelto, que es la cantidad de oxígeno que hay en el agua. Para cada parámetro el plan fija un rango, es decir, un mínimo y un máximo aceptables. Una lectura fuera del rango es una anomalía y se informa de inmediato. Las lecturas las toma personal capacitado con instrumentos calibrados, que son instrumentos ajustados para que midan bien.",
        "Al analizar los datos se calcula el promedio (suma ÷ cantidad de lecturas) y el porcentaje de días fuera de rango (días fuera × 100 ÷ días registrados). En general, el agua más cálida puede contener menos oxígeno disuelto; por eso, si dos parámetros salen de su rango el mismo día, se plantea como causa probable que están relacionados, pero hay que comprobarlo con más datos antes de afirmarlo.",
        f"Los valores de esta clase son de ejemplo; los reales los fija el plan y la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("calidad del agua", "conjunto de condiciones del agua que importan al cultivo"), ("parámetro", "condición medible del agua, como la temperatura o el oxígeno disuelto"), ("rango", "mínimo y máximo aceptables de un parámetro"), ("instrumento calibrado", "instrumento ajustado para que mida bien"), ("lectura", "valor medido y anotado de un parámetro")],
    worked=[
        ("Lecturas fuera de rango", "El rango de ejemplo de un parámetro va de 10 a 14 y las lecturas de cuatro días son 12, 15, 11 y 9. ¿Cuáles están fuera de rango?", ["Se compara cada lectura con 10 y 14.", "15 supera el máximo y 9 está bajo el mínimo."], "15 y 9"),
        ("Porcentaje de días fuera", "De 10 días registrados, 2 tuvieron lecturas fuera de rango. ¿Qué porcentaje es?", ["2 × 100 = 200.", "200 ÷ 10 = 20."], "20 %"),
    ],
    mistakes=[("Dar por buena una lectura fuera de rango porque «seguro fue un error del instrumento».", "Descartar sin verificar es una conclusión sin evidencia.", "Se anota, se informa y se verifica con un instrumento calibrado."),
              ("Calcular el promedio sumando solo las lecturas buenas.", "El promedio debe incluir todas las lecturas registradas.", "Se suman todas y se dividen entre la cantidad de lecturas.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es un parámetro de la calidad del agua?", "Una condición medible del agua, como la temperatura", "El nombre del instrumento de medición", "La persona que anota los datos", "Un parámetro es una condición medible del agua."),
        ("abc", "En Acuicultura: ¿qué es el rango de un parámetro?", "El mínimo y el máximo aceptables", "El promedio de la semana", "El valor que se anotó primero", "El rango fija los límites aceptables."),
        ("abc", "En Acuicultura: ¿qué es un instrumento calibrado?", "Uno ajustado para que mida bien", "Uno que solo mide de noche", "Uno que no necesita ninguna revisión", "Calibrado quiere decir ajustado para medir correctamente."),
        ("=", "{F} ¿Cuál es el promedio de la temperatura de los 8 días, en grados?", "(12+13+15+18+19+16+14+13)//8", "Se suman las 8 lecturas y se dividen entre 8.", " grados"),
        ("=", "{F} Según el rango de ejemplo de la temperatura, ¿cuántos de los 8 días quedaron dentro del rango?", "8-2", "Se comparan las lecturas con 11 y 17: dos días (18 y 19 grados) superan el máximo; se restan a los 8 días registrados.", " días"),
        ("=", "{F} ¿Cuántos grados sobre el máximo estuvo la lectura más alta?", "19-17", "Se resta el máximo del rango a la lectura más alta.", " grados"),
        ("=", "{F} ¿Cuántas unidades bajo el mínimo estuvo la lectura más baja de oxígeno disuelto?", "7-5", "Se resta la lectura más baja al mínimo del rango.", " unidades"),
        ("abc", "{F} ¿Qué días tuvieron oxígeno disuelto bajo el mínimo?", "Los días 4 y 5", "Solo el día 5", "Los días 3 y 4", "Las lecturas de 6 y 5 son menores que 7; el día 3 marca 8, que cumple."),
        ("=", "{F} ¿Qué porcentaje de los días registrados tuvo la temperatura fuera de rango?", "2*100//8", "Se multiplican los días fuera por 100 y se dividen entre los días registrados.", " %"),
        ("abc", "{F} Los días 4 y 5 se salieron de rango en los dos parámetros. ¿Qué conclusión es adecuada?", "Es una causa probable que estén relacionados, y hay que comprobarlo con más datos", "Queda demostrado que uno causa el otro", "No puede haber ninguna relación entre ambos", "Una coincidencia permite plantear una causa probable, pero no probarla."),
        ("abc", "{F} Un compañero propone anotar 17 en lugar de 19 «porque el instrumento debe estar malo». ¿Qué corresponde?", "Anotar 19, informar y verificar con un instrumento calibrado", "Anotar 17 sin avisar", "No anotar ese día", "Descartar o corregir sin verificar oculta una posible anomalía."),
        ("abc", "{F} ¿Cuándo se informa una lectura fuera de rango?", "De inmediato, con el registro como respaldo", "Al final del mes", "Solo si alguien pregunta", "Informar oportunamente permite actuar a tiempo."),
        ("abc", "{F} Una persona propone arreglar el agua de la jaula por su cuenta añadiendo productos. ¿Qué corresponde?", "Informar al técnico, porque los productos los aplica personal autorizado", "Aplicarlos de inmediato porque ya se sabe el problema", "Esperar a que el agua cambie sola sin avisar", "Aplicar productos exige personal autorizado y norma vigente."),
    ],
    ctx=("abc", "Un conocido te pide que le digas qué producto echar a su estanque porque «el agua se ve rara». ¿Qué respondes?", "Que no puedes recomendarle productos: debe consultar a un técnico autorizado, y tú puedes avisar a un adulto responsable", "Que use cualquier producto que tenga en casa", "Que cambie toda el agua sin preguntar", "Aplicar productos exige personal autorizado y norma vigente."),
    sc=[
        ("En Acuicultura: ¿qué es un rango?", "El mínimo y el máximo aceptables", "El rango fija los límites aceptables de un parámetro."),
        ("¿Cómo se calcula el promedio?", "Se suman las lecturas y se divide por la cantidad", "El promedio incluye todas las lecturas."),
        ("¿Cuándo se informa una lectura fuera de rango?", "De inmediato, con el registro", "Un aviso tardío impide actuar a tiempo."),
    ],
    op=("Ficha de ejemplo: lecturas de temperatura de 5 días de otra jaula: 10, 12, 14, 16 y 18 grados; rango de ejemplo de 9 a 15 grados. Escribe (a) el promedio, (b) qué días están fuera de rango, (c) qué porcentaje de los días es, (d) qué harías con esos días.",
        "(a) 10 + 12 + 14 + 16 + 18 = 70; 70 ÷ 5 = 14 grados. (b) Los días de 16 y 18 grados, porque superan el máximo de 15. (c) 2 × 100 ÷ 5 = 40 %. (d) Anotarlos tal cual, informar de inmediato al técnico y verificar con un instrumento calibrado.",
        ["calcula el promedio", "identifica los días fuera de rango", "calcula el porcentaje", "propone informar sin alterar"],
        ["hoja con las cuatro respuestas"],
        ["no incluir todas las lecturas en el promedio", "cambiar los datos", "no informar"],
        "Pregunta: «¿entre qué número divides la suma?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa seis lecturas de un parámetro con un rango y cuenta los días fuera de rango.",
    extend="Explica por qué una lectura fuera de rango no se descarta sin verificar el instrumento.",
)

# ============================================================ OAE-07, clase 5
F = ("Ficha 9 (caso de ejemplo, inventado). Centro Demo, cierre del ciclo de la jaula J-8 de «especie A». Siembra: 10.000 peces. Mortalidad anotada: 300 y 200 peces en dos periodos. Cosecha enviada: 4.000 peces. Existencias anotadas por el encargado: 5.400 peces. "
     "Bodega de alimento: saldo inicial 5.000 kg, entradas 3.000 kg, consumos anotados en las jaulas 6.200 kg, saldo anotado 1.700 kg. Comparación de dos formatos: el formato A (papel con revisión) tuvo 12 errores en 200 registros revisados; el formato B (planilla con campos obligatorios) tuvo 4 errores en 200 registros revisados.")
build(
    O7, 5, F,
    use="Aprenderé a verificar la calidad de los registros con un balance de animales y de alimento y a comparar dos formatos de registro con sus tasas de error.",
    prior=["Sé qué es una anomalía y qué es informar oportunamente.", "Sé calcular un porcentaje con números enteros.", "Sé sumar y restar números enteros."],
    explain=[
        "Verificar la calidad de un registro es comprobar que está completo, tiene fecha y responsable y que sus cifras cuadran con otros registros. Un balance es una cuenta que compara lo que entró, lo que salió y lo que debe quedar. En animales: existencias que deben quedar = siembra − mortalidad − cosecha. En alimento: saldo que debe quedar = saldo inicial + entradas − consumos. Si el saldo anotado difiere del calculado, hay una diferencia que se informa y se investiga.",
        "Para comparar dos formatos de registro se calcula la tasa de error: errores × 100 ÷ registros revisados. El formato con menor tasa es mejor en ese criterio, pero se comparan también el costo y el tiempo. Una diferencia en un balance nunca se «ajusta» para que cuadre: se informa al técnico con los registros como respaldo.",
        f"La decisión final la toma la jefatura con el técnico. {EMER} {AVISO}",
    ],
    vocab=[("balance", "cuenta que compara lo que entró, lo que salió y lo que debe quedar"), ("existencias", "animales o productos que quedan en un momento dado"), ("saldo", "cantidad que queda después de sumar entradas y restar salidas"), ("tasa de error", "errores multiplicados por 100 y divididos entre los registros revisados"), ("diferencia", "valor anotado menos o más que el valor calculado")],
    worked=[
        ("Balance de animales", "Se siembran 2.000 animales de ejemplo, mueren 100 y se cosechan 500. ¿Cuántos deben quedar?", ["2.000 − 100 = 1.900.", "1.900 − 500 = 1.400."], "1.400 animales"),
        ("Tasa de error", "En 50 registros de ejemplo se encuentran 5 errores. ¿Cuál es la tasa de error?", ["5 × 100 = 500.", "500 ÷ 50 = 10."], "10 %"),
    ],
    mistakes=[("Ajustar un saldo para que el balance cuadre.", "Un ajuste oculto esconde la causa de la diferencia.", "Se informa la diferencia y se investiga."),
              ("Elegir un formato solo por su costo sin mirar su tasa de error.", "Un formato barato con muchos errores genera pérdidas por decisiones mal tomadas.", "Se comparan costo, tasa de error y tiempo.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es un balance de animales?", "Una cuenta que compara los que entraron, los que salieron y los que deben quedar", "Una lista de personas que trabajan en el centro", "Un plano de las jaulas", "El balance cuadra entradas y salidas para saber lo que debe quedar."),
        ("abc", "En Acuicultura: ¿qué es la tasa de error de un formato?", "Los errores por 100 divididos entre los registros revisados", "El precio de cada registro", "El número de personas que lo llenan", "La tasa de error mide cuántos registros tienen error."),
        ("abc", "En Acuicultura: ¿qué se hace con una diferencia en un balance?", "Se informa y se investiga con los registros como respaldo", "Se ajusta el saldo para que cuadre", "Se ignora si es pequeña", "Una diferencia es una anomalía; se investiga y no se oculta."),
        ("=", "{F} ¿Cuántos peces deben quedar en la jaula J-8 según el balance?", "10000-(300+200)-4000", "Se restan la mortalidad y la cosecha a la siembra.", " peces"),
        ("=", "{F} ¿Cuál es la diferencia entre las existencias calculadas y las anotadas?", "(10000-(300+200)-4000)-5400", "Se resta lo anotado a lo calculado.", " peces"),
        ("=", "{F} ¿Cuántos kg de alimento deben quedar en la bodega según el balance?", "5000+3000-6200", "Se suma lo que entró y se restan los consumos.", " kg"),
        ("=", "{F} ¿Cuántos kg de diferencia hay entre el saldo calculado y el anotado?", "(5000+3000-6200)-1700", "Se resta el saldo anotado al calculado.", " kg"),
        ("=", "{F} ¿Cuál es la tasa de error del formato A, en %?", "12*100//200", "Se multiplican los errores por 100 y se dividen entre los registros revisados.", " %"),
        ("=", "{F} ¿Cuál es la tasa de error del formato B, en %?", "4*100//200", "Se multiplican los errores por 100 y se dividen entre los registros revisados.", " %"),
        ("=", "{F} Si se llenaran 1.000 registros con el formato A, ¿cuántos tendrían error con esa tasa?", "1000*12//200", "Se aplica la tasa de error de A a 1.000 registros.", " registros"),
        ("abc", "{F} Según la tasa de error, ¿qué formato conviene?", "El formato B, porque tiene menos errores por registro", "El formato A, porque usa papel", "Ambos por igual", "B tiene 2 % de error y A tiene 6 %."),
        ("abc", "{F} Un compañero propone cambiar el saldo de alimento anotado a 1.800 para que cuadre. ¿Qué respondes?", "Que no: se informa la diferencia de 100 kg y se investiga", "Que sí, si lo corrige después", "Que sí, porque el balance debe cuadrar siempre", "Un ajuste oculto esconde la causa de la diferencia."),
        ("abc", "{F} El formato B es más caro. ¿Qué corresponde para decidir?", "Comparar también costo y tiempo, y que decida la jefatura con el técnico", "Elegir A porque cuesta menos", "Elegir B sin mirar el costo", "Una decisión considera varios criterios y la toma quien tiene la responsabilidad."),
    ],
    ctx=("abc", "Un compañero te pide anotar un saldo de alimento que no corresponde para que el balance «cuadre» antes de una visita. ¿Qué respondes?", "Que no, porque un registro no se altera, y que se lo contarás a un adulto responsable", "Que sí, solo por esta vez", "Que sí, si lo corrige después", "Alterar un saldo falsifica el registro y oculta una diferencia que hay que investigar."),
    sc=[
        ("En Acuicultura: ¿cómo se calculan las existencias que deben quedar?", "Siembra − mortalidad − cosecha", "El balance resta lo que salió a lo que entró."),
        ("¿Cómo se calcula la tasa de error?", "Errores × 100 ÷ registros revisados", "La tasa de error es un porcentaje."),
        ("¿Qué se hace con una diferencia en un balance?", "Se informa y se investiga", "Una diferencia no se oculta ni se ajusta."),
    ],
    op=("Ficha de ejemplo: jaula J-9: siembra de 6.000 peces, mortalidad de 150 y 100 peces, cosecha de 2.000 peces; existencias anotadas: 3.700. Dos formatos: el A tuvo 9 errores en 150 registros y el B tuvo 3 errores en 150. Escribe (a) las existencias calculadas, (b) la diferencia con lo anotado, (c) la tasa de error de A y de B, (d) qué haces con la diferencia.",
        "(a) 6.000 − (150 + 100) − 2.000 = 3.750 peces. (b) 3.750 − 3.700 = 50 peces. (c) A: 9 × 100 ÷ 150 = 6 %; B: 3 × 100 ÷ 150 = 2 %. (d) Se informa al técnico con los registros como respaldo y se investiga, sin ajustar el dato.",
        ["calcula las existencias", "calcula la diferencia", "calcula las tasas de error", "informa sin ajustar"],
        ["hoja con las cuatro respuestas"],
        ["olvidar restar la mortalidad", "ajustar el dato para que cuadre", "dividir entre el número de errores"],
        "Pregunta: «¿qué restas a la siembra?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un balance de animales con siembra, mortalidad y cosecha, y calcula cuántos deben quedar.",
    extend="Explica por qué ajustar un saldo para que cuadre es peor que informar la diferencia.",
)

O8 = "TP-ACUI-3y4-OAE-08"

# ============================================================ OAE-08, clase 1
F = ("Ficha 10 (caso de ejemplo, inventado). Matriz de riesgos de ejemplo del Centro Demo. Cada peligro tiene una probabilidad (1 = baja, 2 = media, 3 = alta) y una consecuencia (1 = leve, 2 = moderada, 3 = grave), y el puntaje es probabilidad × consecuencia. "
     "Caída al agua desde la pasarela: probabilidad 2, consecuencia 3. Ruido continuo en la sala de máquinas: probabilidad 2, consecuencia 2. Resbalón en piso mojado: probabilidad 3, consecuencia 1. Descarga eléctrica en una bomba: probabilidad 1, consecuencia 3.")
build(
    O8, 1, F,
    use="Aprenderé qué son un accidente del trabajo y una enfermedad profesional, cómo se ordenan los riesgos con una matriz de ejemplo y qué papel cumplen el manejo ético y el cuidado del ambiente.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé multiplicar números enteros.", "Sé qué es la autoridad marítima."],
    explain=[
        "Un accidente del trabajo es un hecho que ocurre por el trabajo y causa una lesión. Una enfermedad profesional es un daño a la salud que se produce poco a poco por las condiciones del trabajo, como el ruido continuo. La prevención de riesgos busca evitar ambos. Para ordenar los riesgos se puede usar una matriz de riesgos: a cada peligro se le da una probabilidad y una consecuencia (de 1 a 3 en el ejemplo) y se multiplican; el mayor puntaje se atiende primero. Los valores son siempre de ejemplo.",
        "Además de las personas se cuida a los animales y al ambiente. El manejo ético de las especies es tratar a los animales evitando sufrimiento innecesario y cumpliendo la norma vigente. El cuidado del medio ambiente y los ecosistemas es evitar que el cultivo dañe el entorno, por ejemplo con residuos o escapes de animales. En el mar rigen además las normas de la autoridad marítima. Estas faenas las hace personal autorizado.",
        f"Para controlar un peligro se aplica la jerarquía de controles: eliminar, sustituir, ingeniería, administrativos y, al final, el EPP, incluido el equipo de flotación cuando corresponde. {EMER} {AVISO}",
    ],
    vocab=[("accidente del trabajo", "hecho ocurrido por el trabajo que causa una lesión"), ("enfermedad profesional", "daño a la salud que se produce poco a poco por las condiciones del trabajo"), ("matriz de riesgos", "tabla que ordena los peligros según su probabilidad y su consecuencia"), ("probabilidad", "qué tan posible es que ocurra el daño"), ("consecuencia", "qué tan grave sería el daño"), ("puntaje de riesgo", "probabilidad multiplicada por consecuencia"), ("ecosistema", "conjunto de seres vivos y su entorno"), ("manejo ético", "trato que evita sufrimiento innecesario y cumple la norma vigente")],
    worked=[
        ("Puntaje de riesgo", "Un peligro de ejemplo tiene probabilidad 2 y consecuencia 2. ¿Cuál es su puntaje?", ["Se multiplican probabilidad y consecuencia.", "2 × 2 = 4."], "4"),
        ("Accidente o enfermedad", "Una persona pierde audición poco a poco tras años en una sala muy ruidosa de ejemplo. ¿Es un accidente del trabajo o una enfermedad profesional?", ["El daño se produjo poco a poco.", "Eso corresponde a una enfermedad profesional."], "Enfermedad profesional"),
    ],
    mistakes=[("Creer que un peligro de baja probabilidad no necesita ningún control.", "Si la consecuencia es grave, el riesgo sigue siendo importante.", "Se mira probabilidad y consecuencia juntas."),
              ("Creer que solo importa el cuidado de las personas y no el de los animales y el ambiente.", "El manejo ético y el cuidado ambiental también son obligaciones del trabajo.", "Se cuida a las personas, a los animales y al ambiente a la vez.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es una enfermedad profesional?", "Un daño a la salud que se produce poco a poco por las condiciones del trabajo", "Una lesión causada por un golpe repentino", "Una enfermedad que se contagia en la familia", "La enfermedad profesional se desarrolla gradualmente; el golpe repentino es un accidente."),
        ("abc", "En Acuicultura: ¿qué es una matriz de riesgos?", "Una tabla que ordena los peligros según su probabilidad y su consecuencia", "Un plano de las jaulas del centro", "Una lista de los proveedores de alimento", "La matriz ordena los riesgos para atender primero los más importantes."),
        ("abc", "En Acuicultura: ¿qué es el manejo ético de las especies?", "Tratar a los animales evitando sufrimiento innecesario y cumpliendo la norma vigente", "Cuidar a los animales solo si se van a vender", "Dejar que cada persona decida cómo tratarlos", "El manejo ético protege el bienestar de los animales según la norma."),
        ("=", "{F} ¿Cuál es el puntaje de la caída al agua desde la pasarela?", "2*3", "Se multiplican la probabilidad y la consecuencia.", ""),
        ("=", "{F} ¿Cuál es el puntaje del ruido continuo en la sala de máquinas?", "2*2", "Se multiplican la probabilidad y la consecuencia.", ""),
        ("=", "{F} ¿Cuántos puntos suman los puntajes de los cuatro peligros de la matriz?", "2*3+2*2+3*1+1*3", "Se calcula el puntaje de cada peligro y se suman los cuatro.", " puntos"),
        ("abc", "{F} ¿Qué peligro de la matriz tiene el mayor puntaje y se atiende primero?", "La caída al agua desde la pasarela", "El resbalón en piso mojado", "La descarga eléctrica", "La caída al agua tiene 6, el ruido 4, y el resbalón y la descarga 3 cada uno."),
        ("abc", "{F} El ruido continuo puede dañar la audición poco a poco. ¿Qué tipo de daño es?", "Una enfermedad profesional", "Un accidente del trabajo", "Un daño ambiental", "El ruido continuo causa un daño gradual a la salud."),
        ("abc", "{F} Una baranda fija en la pasarela es un control de nivel:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla escrita", "De EPP, porque protege a quien se acerca", "La baranda modifica el lugar y no depende de que cada persona la recuerde."),
        ("abc", "{F} Una persona cae al agua desde la pasarela durante una visita de ejemplo. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo ni entrar al agua, y avisar a un adulto responsable y a emergencias", "Lanzarte al agua para ayudarla de inmediato", "Esperar a ver si sale sola antes de avisar", "Entrar al agua puede producir otro accidente; se avisa a quienes pueden actuar."),
        ("=", "{F} ¿Cuántos puntos más tiene la caída al agua que el resbalón en piso mojado?", "2*3-3*1", "Se resta el puntaje del resbalón al de la caída.", " puntos"),
        ("abc", "{F} Un compañero dice que la descarga eléctrica no necesita controles porque su probabilidad es 1. ¿Qué respondes?", "Que sí necesita controles, porque su consecuencia es grave", "Que tiene razón, porque la probabilidad es la más baja", "Que solo necesita un cartel", "Una consecuencia grave exige controles aunque la probabilidad sea baja."),
        ("abc", "En Acuicultura: ¿qué es cuidar un ecosistema cuando se trabaja en un cultivo?", "Evitar que el cultivo dañe el entorno, por ejemplo con residuos o escapes de animales", "Cultivar la mayor cantidad posible de animales", "Cambiar el color de las jaulas", "Cuidar el ecosistema es evitar daños al entorno."),
    ],
    ctx=("abc", "Un conocido te ofrece trabajo ocasional en su centro de cultivo: tendrías que subir a una pasarela sin baranda y sin chaleco. ¿Qué respondes?", "Que no, porque esa tarea exige personal autorizado, equipo de flotación y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, porque la pasarela es corta", "Que sí, si solo es por un rato", "El tiempo o el largo no reemplazan las medidas de seguridad."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula el puntaje de riesgo?", "Probabilidad × consecuencia", "El puntaje combina la probabilidad y la consecuencia."),
        ("¿Qué es una enfermedad profesional?", "Un daño a la salud que se produce poco a poco por el trabajo", "Es un daño gradual causado por las condiciones del trabajo."),
        ("¿Qué haces si alguien cae al agua?", "No entrar al agua y avisar a un adulto responsable y a emergencias", "Entrar al agua puede producir otro accidente."),
    ],
    op=("Matriz de ejemplo de un centro: golpe por un cabo tenso, probabilidad 2 y consecuencia 3; frío intenso en la jornada, probabilidad 2 y consecuencia 2; piso mojado, probabilidad 3 y consecuencia 1. Escribe (a) el puntaje de cada peligro, (b) cuál se atiende primero, (c) un control de ingeniería y uno administrativo para el primero, (d) por qué el EPP no basta.",
        "(a) Golpe por cabo: 6; frío: 4; piso mojado: 3. (b) El golpe por cabo, porque tiene el mayor puntaje. (c) Ingeniería: una guía fija que mantenga los cabos ordenados; administrativo: una regla de trabajo y señales en la zona. (d) El EPP es la última barrera y no quita el peligro.",
        ["calcula los puntajes", "ordena la prioridad", "propone dos controles de distinto nivel", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["sumar probabilidad y consecuencia", "ignorar la consecuencia grave", "proponer solo el EPP"],
        "Pregunta: «¿qué se multiplica para obtener el puntaje?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres peligros con probabilidad y consecuencia, y calcula su puntaje.",
    extend="Explica por qué un peligro de baja probabilidad y consecuencia grave sigue necesitando controles.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 11 (registro de ejemplo, inventado). Centro Demo, señalética y documentos de seguridad. Señales instaladas: «uso obligatorio de chaleco de flotación», «salida de emergencia», «piso mojado» y «prohibido pasar bajo carga». "
     "Documentos: hoja de datos de seguridad de cada producto, registro de capacitación, reporte de incidentes y comité paritario (instancia donde participan representantes de los trabajadores y de la empresa). "
     "De 30 trabajadores, 24 asistieron a la capacitación de seguridad del trimestre.")
build(
    O8, 2, F,
    use="Aprenderé los colores de la señalética de seguridad, los documentos de prevención de riesgos y los roles que intervienen, y a calcular la asistencia a una capacitación.",
    prior=["Sé qué es un peligro y la jerarquía de controles.", "Sé calcular un porcentaje con números enteros.", "Sé qué es un registro."],
    explain=[
        "La señalética es el conjunto de señales que informan, advierten o prohíben. Por su color y forma se distinguen: las de prohibición son rojas, por ejemplo «prohibido fumar»; las de obligación son azules, como «uso obligatorio de casco»; las de advertencia son amarillas con forma de triángulo, como «peligro eléctrico»; y las de salvamento o emergencia son verdes. Una señal es un control administrativo: informa, pero no elimina el peligro.",
        "Los documentos de prevención son la hoja de datos de seguridad, que explica los peligros de un producto y qué medidas de seguridad corresponden; el registro de capacitación, que anota quién recibió formación; y el reporte de incidentes, donde se anota todo hecho, con o sin lesión. Un cuasi accidente es un hecho que pudo causar una lesión y no la causó; también se reporta. El comité paritario reúne a representantes de los trabajadores y de la empresa para vigilar la seguridad. El prevencionista asesora y el jefe del centro es responsable de que se cumplan las medidas.",
        f"Los números son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("señalética", "conjunto de señales que informan, advierten o prohíben"), ("hoja de datos de seguridad", "documento que explica los peligros de un producto y sus medidas de seguridad"), ("registro de capacitación", "documento que anota quién recibió formación y cuándo"), ("reporte de incidentes", "documento donde se anota todo hecho ocurrido, con o sin lesión"), ("cuasi accidente", "hecho que pudo causar una lesión y no la causó"), ("comité paritario", "instancia con representantes de los trabajadores y de la empresa para vigilar la seguridad")],
    worked=[
        ("Elegir el color", "Una señal de ejemplo indica «peligro de carga suspendida». ¿De qué color y forma debería ser?", ["Es una advertencia de un peligro.", "Las advertencias son amarillas con forma de triángulo."], "Amarilla, con forma de triángulo"),
        ("Asistencia", "De 20 trabajadores de ejemplo, 15 asistieron a una charla. ¿Qué porcentaje asistió?", ["15 × 100 = 1.500.", "1.500 ÷ 20 = 75."], "75 %"),
    ],
    mistakes=[("Creer que colgar una señal elimina el peligro.", "Una señal solo informa; el peligro sigue allí.", "Se suman controles de ingeniería cuando es posible."),
              ("No reportar un cuasi accidente porque «no pasó nada».", "Un cuasi accidente muestra un peligro real que puede repetirse con una lesión.", "Se reporta para poder prevenirlo.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es un cuasi accidente?", "Un hecho que pudo causar una lesión y no la causó", "Un accidente que causó una lesión grave", "Una capacitación a la que nadie asistió", "El cuasi accidente es un aviso de un peligro real, aunque no haya lesión."),
        ("abc", "En Acuicultura: ¿para qué sirve la hoja de datos de seguridad de un producto?", "Para explicar sus peligros y las medidas de seguridad que corresponden", "Para fijar el precio de venta del producto", "Para registrar quién lo compró", "La hoja informa los peligros y medidas de seguridad del producto."),
        ("abc", "En Acuicultura: ¿qué función cumple el comité paritario?", "Reunir a representantes de los trabajadores y de la empresa para vigilar la seguridad", "Fijar los precios de los productos del centro", "Reemplazar al supervisor de buceo", "El comité paritario vigila la seguridad con representantes de ambos lados."),
        ("abc", "{F} La señal «uso obligatorio de chaleco de flotación» tiene color:", "Azul", "Rojo", "Amarillo", "Las señales de obligación son azules."),
        ("abc", "{F} La señal «salida de emergencia» tiene color:", "Verde", "Rojo", "Azul", "Las señales de salvamento o emergencia son verdes."),
        ("abc", "{F} La señal «piso mojado» es una:", "Advertencia, de color amarillo", "Prohibición, de color rojo", "Obligación, de color azul", "El piso mojado advierte de un peligro, por lo que la señal es amarilla."),
        ("abc", "{F} La señal «prohibido pasar bajo carga» es una:", "Prohibición, de color rojo", "Advertencia, de color amarillo", "Emergencia, de color verde", "Las señales de prohibición son rojas."),
        ("=", "{F} ¿Qué porcentaje de los trabajadores asistió a la capacitación?", "24*100//30", "Se multiplican los asistentes por 100 y se dividen entre el total.", " %"),
        ("=", "{F} ¿Cuántos trabajadores no asistieron a la capacitación?", "30-24", "Se resta la asistencia al total.", " trabajadores"),
        ("abc", "{F} ¿Qué documento anota quién recibió formación y cuándo?", "El registro de capacitación", "La hoja de datos de seguridad", "El reporte de incidentes", "El registro de capacitación guarda la formación; los otros documentos tienen otra función."),
        ("abc", "{F} Una persona resbaló, no se lastimó y nadie lo anotó. ¿Qué corresponde?", "Reportarlo como cuasi accidente", "No anotarlo porque no hubo lesión", "Anotarlo como accidente grave", "Un cuasi accidente se reporta para prevenir que se repita con lesión."),
        ("abc", "{F} Un jefe propone quitar la señal «piso mojado» porque «afea el pasillo». ¿Qué corresponde?", "Dejar la señal y buscar un control de ingeniería para el piso", "Quitarla para que el pasillo se vea mejor", "Pintarla de otro color", "Una señal advierte el peligro; el piso mojado seguiría allí."),
        ("abc", "{F} ¿Qué rol del centro asesora en la prevención de riesgos?", "El prevencionista", "El comité de ventas", "Cualquier trabajador del turno", "El prevencionista asesora; el jefe del centro es responsable de que se cumplan las medidas."),
    ],
    ctx=("abc", "Un compañero te pide que firmes por él en el registro de capacitación porque faltó a la charla de seguridad. ¿Qué respondes?", "Que no, porque firmar por otro falsifica el registro, y que lo consultarás con un adulto responsable", "Que sí, si es amigo", "Que sí, solo esta vez", "Falsificar un registro de capacitación deja a la persona sin formación real."),
    sc=[
        ("En Acuicultura: ¿qué color tienen las señales de prohibición?", "Rojo", "Las prohibiciones se señalan en rojo."),
        ("¿Qué color tienen las señales de obligación?", "Azul", "Las obligaciones se señalan en azul."),
        ("¿Qué es un cuasi accidente?", "Un hecho que pudo causar una lesión y no la causó", "Se reporta para evitar que se repita."),
    ],
    op=("Ficha de ejemplo: un centro tiene 40 trabajadores; 34 asistieron a la capacitación de seguridad. Señales de ejemplo: «prohibido fumar», «uso obligatorio de casco» y «peligro eléctrico». Escribe (a) el porcentaje de asistencia, (b) cuántos faltan por capacitar, (c) el color de cada señal, (d) qué documento anota la capacitación.",
        "(a) 34 × 100 ÷ 40 = 85 %. (b) 40 − 34 = 6 trabajadores. (c) «Prohibido fumar»: rojo; «uso obligatorio de casco»: azul; «peligro eléctrico»: amarillo, con forma de triángulo. (d) El registro de capacitación.",
        ["calcula el porcentaje", "calcula los que faltan", "asigna bien los colores", "nombra el registro"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre los asistentes", "confundir los colores", "confundir el registro con la hoja de datos"],
        "Pregunta: «¿qué color tienen las señales que prohíben?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Dibuja con palabras tres señales con su color y forma, y di qué comunica cada una.",
    extend="Explica por qué una señal no reemplaza una medida de ingeniería.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 12 (registro de ejemplo, inventado). Centro Demo, reporte de incidentes del año: 20 incidentes. Por tipo: 8 caídas o resbalones, 5 golpes, 4 cortes y 3 de otro tipo. "
     "De los 20 incidentes, 6 fueron cuasi accidentes (sin lesión). Meta de ejemplo: ningún tipo de incidente debe superar el 30 % del total.")
build(
    O8, 3, F,
    use="Aprenderé a analizar un reporte de incidentes: calcular porcentajes por tipo, detectar el tipo más frecuente y proponer controles de la jerarquía.",
    prior=["Sé qué es un cuasi accidente y un reporte de incidentes.", "Sé calcular un porcentaje con números enteros.", "Sé la jerarquía de controles."],
    explain=[
        "Analizar un reporte de incidentes es contar cuántos hubo de cada tipo y calcular qué porcentaje del total es cada uno: tipo × 100 ÷ total. El tipo más frecuente es el que se atiende primero. Si un tipo supera la meta, se considera una desviación y se propone una medida. Para elegir la medida se usa la jerarquía de controles: primero eliminar o sustituir, luego ingeniería, después administrativos y al final el EPP.",
        "Una causa probable es una explicación posible que hay que comprobar con más datos, como una pasarela mojada o falta de capacitación; no se afirma sin evidencia. Después de aplicar una medida se verifica con nuevos reportes que los incidentes bajaron. Todo incidente, incluso un cuasi accidente, se reporta y los registros nunca se alteran.",
        f"Las decisiones las toman el comité paritario y la jefatura; aquí analizas datos escritos. {EMER} {AVISO}",
    ],
    vocab=[("tipo de incidente", "clase de hecho ocurrido, como caída, golpe o corte"), ("tipo más frecuente", "el que más veces se repite en el reporte"), ("desviación", "valor que supera la meta o queda fuera de lo esperado"), ("verificar una medida", "comprobar con nuevos datos que realmente redujo el problema")],
    worked=[
        ("Porcentaje por tipo", "De 50 incidentes de ejemplo, 10 fueron cortes. ¿Qué porcentaje es?", ["10 × 100 = 1.000.", "1.000 ÷ 50 = 20."], "20 %"),
        ("Comparar con la meta", "Un tipo de incidente es el 35 % del total y la meta es no superar 30 %. ¿Cumple?", ["Se compara 35 con 30.", "35 es mayor que 30."], "No cumple: supera la meta en 5 puntos"),
    ],
    mistakes=[("Atender primero el tipo de incidente más grave sin mirar cuál se repite más.", "Se necesita mirar frecuencia y gravedad juntas.", "Se usan ambos criterios para decidir la prioridad."),
              ("No reportar un cuasi accidente.", "Sin reporte no se conoce el peligro y puede repetirse con una lesión.", "Todo incidente se reporta.")],
    T=[
        ("abc", "En Acuicultura: ¿cómo se calcula el porcentaje de un tipo de incidente?", "Cantidad del tipo × 100 ÷ total de incidentes", "Total de incidentes ÷ cantidad del tipo", "Cantidad del tipo + total de incidentes", "El porcentaje compara la cantidad del tipo con el total."),
        ("abc", "En Acuicultura: ¿qué significa verificar una medida de prevención?", "Comprobar con nuevos reportes que los incidentes bajaron", "Colgar un cartel nuevo", "Anotar la fecha de instalación", "Verificar es comprobar el resultado con datos."),
        ("abc", "En Acuicultura: ¿qué es el tipo más frecuente de incidente?", "El que más veces se repite en el reporte", "El que causó la lesión más grave", "El que ocurrió primero en el año", "El más frecuente es el que más veces se repite."),
        ("=", "{F} ¿Qué porcentaje de los incidentes fueron caídas o resbalones?", "8*100//20", "Se multiplican las caídas por 100 y se dividen entre el total.", " %"),
        ("=", "{F} ¿Qué porcentaje de los incidentes fueron golpes?", "5*100//20", "Se multiplican los golpes por 100 y se dividen entre el total.", " %"),
        ("=", "{F} ¿Qué porcentaje de los incidentes fueron cortes?", "4*100//20", "Se multiplican los cortes por 100 y se dividen entre el total.", " %"),
        ("abc", "{F} ¿Qué tipo de incidente supera la meta de ejemplo del 30 %?", "Las caídas o resbalones", "Los golpes", "Los cortes", "Las caídas son 40 %, sobre 30 %; los golpes son 25 % y los cortes son 20 %."),
        ("=", "{F} ¿Qué porcentaje de los incidentes fueron cuasi accidentes?", "6*100//20", "Se multiplican los cuasi accidentes por 100 y se dividen entre el total.", " %"),
        ("=", "{F} ¿Cuántos incidentes con lesión hubo en el año?", "20-6", "Se restan los cuasi accidentes al total.", " incidentes"),
        ("abc", "{F} ¿Qué medida de nivel más efectivo conviene para reducir las caídas?", "Una superficie antideslizante y una baranda fijas, instaladas por personal autorizado", "Un cartel más grande", "Pedir a cada persona que use un calzado nuevo", "Los controles de ingeniería actúan sobre el lugar; el cartel es administrativo y el calzado es EPP."),
        ("abc", "{F} Se plantea que las caídas aumentan porque falta capacitación. ¿Qué conclusión es adecuada?", "Es una causa probable que hay que comprobar con más datos", "Queda demostrado porque son el tipo más frecuente", "No puede haber ninguna relación con la capacitación", "Una causa probable se comprueba con más datos."),
        ("abc", "{F} Alguien propone no reportar los cuasi accidentes para que el informe se vea mejor. ¿Qué respondes?", "Que no: se reportan para poder prevenirlos", "Que sí, porque no hubo lesión", "Que sí, si son pocos", "Sin reporte no se conocen los peligros que pueden repetirse."),
        ("abc", "{F} Después de instalar la medida, ¿cómo se verifica que funcionó?", "Comparando los incidentes de caída de los nuevos reportes con los de antes", "Confiando en que funciona porque costó caro", "Esperando que alguien se queje", "La verificación usa datos nuevos y no solo la intuición."),
    ],
    ctx=("abc", "El jefe de un centro de ejemplo te pide quitar del reporte tres caídas para que el informe del año «quede mejor». ¿Qué haces?", "No alterar el reporte y avisar a un adulto responsable, como tu profesor o profesora de especialidad", "Quitar solo una", "Quitarlas y avisar después", "Alterar un reporte oculta la realidad; ante la presión se consulta a un adulto responsable."),
    sc=[
        ("En Acuicultura: ¿cómo se calcula el porcentaje de un tipo de incidente?", "Cantidad × 100 ÷ total", "Se compara la cantidad con el total."),
        ("¿Qué se hace con un cuasi accidente?", "Se reporta", "Muestra un peligro real que puede repetirse."),
        ("¿Qué se hace después de aplicar una medida?", "Verificar con nuevos reportes que funcionó", "La verificación se basa en datos."),
    ],
    op=("Ficha de ejemplo: reporte de otro centro con 40 incidentes: 20 caídas, 10 golpes, 6 cortes y 4 de otro tipo; 8 fueron cuasi accidentes. Meta de ejemplo: ningún tipo sobre 30 %. Escribe (a) el porcentaje de cada tipo, (b) cuál supera la meta, (c) una medida de ingeniería y una administrativa para ese tipo, (d) cómo verificarías que funcionó.",
        "(a) Caídas: 50 %; golpes: 25 %; cortes: 15 %; otro: 10 %. (b) Las caídas, porque 50 supera 30. (c) Ingeniería: superficie antideslizante y baranda fija; administrativa: señal de piso mojado y una regla de limpieza con horario. (d) Comparando las caídas de los nuevos reportes con las de antes.",
        ["calcula los porcentajes", "identifica el tipo sobre la meta", "propone medidas de distinto nivel", "propone verificar con nuevos datos"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre la cantidad del tipo", "proponer solo EPP", "no verificar la medida"],
        "Pregunta: «¿cómo sabrías que la medida realmente sirvió?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un reporte con cuatro tipos de incidentes y calcula el porcentaje de cada uno.",
    extend="Explica por qué se reportan los cuasi accidentes aunque no haya habido lesión.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 13 (registro de ejemplo, inventado). Centro Demo, residuos del año (kg de ejemplo): plásticos de cabos y boyas, 400 kg; envases de productos, 200 kg; material orgánico (animales muertos y restos), 1.200 kg; otros, 200 kg. "
     "De los plásticos, 300 kg se entregaron a un gestor autorizado para su reciclaje. Escapes registrados en el año: dos eventos, de 150 y 50 peces. Peces en el centro al inicio del año: 10.000. Meta de ejemplo: escapes de 1 % o menos.")
build(
    O8, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo sobre el cuidado del medio ambiente: calcular proporciones de residuos y escapes, compararlas con una meta y decidir qué informar.",
    prior=["Sé qué es un ecosistema y el manejo ético.", "Sé calcular un porcentaje con números enteros.", "Sé qué es informar oportunamente."],
    explain=[
        "Un centro de cultivo genera residuos: plásticos de cabos y boyas, envases de productos, material orgánico y otros. Los residuos se clasifican, se registran y se entregan o disponen según la norma vigente, por personal autorizado y gestores autorizados; este cuaderno no describe cómo. Un escape es la salida de animales de cultivo hacia el ambiente: puede afectar a las especies nativas y a la sanidad del ecosistema, por lo que se registra y se informa a la autoridad según la norma vigente.",
        "Con los registros se calcula qué porcentaje del total es cada tipo de residuo, qué porcentaje de un residuo se recicló y qué porcentaje de los animales escapó: escapados × 100 ÷ animales iniciales. Los resultados se comparan con una meta y las desviaciones se informan. Reducir residuos y escapes es parte del manejo ético y del cuidado del ecosistema.",
        f"Todos los números son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("residuo", "material que sobra y hay que clasificar y entregar o disponer según la norma"), ("gestor autorizado", "empresa o persona autorizada para recibir y tratar residuos"), ("reciclaje", "tratamiento de un residuo para volver a usarlo como material"), ("escape", "salida de animales de cultivo hacia el ambiente"), ("especie nativa", "especie que vive de manera natural en un lugar")],
    worked=[
        ("Porcentaje de un residuo", "De 500 kg de residuos de ejemplo, 100 kg son envases. ¿Qué porcentaje es?", ["100 × 100 = 10.000.", "10.000 ÷ 500 = 20."], "20 %"),
        ("Porcentaje de escape", "De 5.000 peces de ejemplo, se escapan 50. ¿Qué porcentaje es?", ["50 × 100 = 5.000.", "5.000 ÷ 5.000 = 1."], "1 %"),
    ],
    mistakes=[("Creer que los residuos del centro pueden dejarse en cualquier lugar si son pocos.", "Los residuos se clasifican y se entregan según la norma vigente.", "Se registran y los maneja personal autorizado."),
              ("Dejar de anotar un escape pequeño.", "Un escape pequeño igual puede afectar al ecosistema y debe informarse.", "Todo escape se registra y se informa.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es un escape de animales de cultivo?", "La salida de animales de cultivo hacia el ambiente", "El traslado de animales a otra jaula del mismo centro", "La venta de animales a una planta", "El escape es la salida al ambiente; los traslados internos y las ventas son otras operaciones."),
        ("abc", "En Acuicultura: ¿por qué un escape puede dañar un ecosistema?", "Porque puede afectar a las especies nativas y a la sanidad del ambiente", "Porque los animales escapados se vuelven más caros", "Porque ocupan los espacios de las jaulas", "El daño es al entorno y a las especies nativas."),
        ("abc", "En Acuicultura: ¿qué es un gestor autorizado de residuos?", "Una empresa o persona autorizada para recibir y tratar residuos", "El jefe del centro de cultivo", "Una persona que vende alimento", "Los gestores autorizados reciben y tratan residuos según la norma."),
        ("=", "{F} ¿Cuántos kg de residuos hubo en total en el año?", "400+200+1200+200", "Se suman los kg de los cuatro tipos de residuo.", " kg"),
        ("=", "{F} ¿Qué porcentaje del total de residuos fue material orgánico?", "1200*100//2000", "Se multiplican los kg orgánicos por 100 y se dividen entre el total.", " %"),
        ("=", "{F} ¿Qué porcentaje de los plásticos se entregó a reciclaje?", "300*100//400", "Se multiplican los kg reciclados por 100 y se dividen entre los kg de plástico.", " %"),
        ("=", "{F} ¿Cuántos kg de plástico no se entregaron a reciclaje?", "400-300", "Se restan los kg reciclados al total de plástico.", " kg"),
        ("=", "{F} ¿Cuántos peces escaparon en total en el año?", "150+50", "Se suman los peces de los dos eventos.", " peces"),
        ("=", "{F} ¿Qué porcentaje de los peces iniciales escapó?", "(150+50)*100//10000", "Se multiplican los escapados por 100 y se dividen entre los peces iniciales.", " %"),
        ("abc", "{F} ¿Qué conclusión corresponde frente a la meta de escapes de 1 %?", "No cumple: el escape fue 2 %, sobre la meta", "Cumple: 2 % es menor que 1 %", "Cumple porque son solo dos eventos", "Dos por ciento supera el uno por ciento de la meta."),
        ("abc", "{F} ¿Qué se debe hacer con el dato de los escapes?", "Informarlo a quien corresponde según la norma vigente, con el registro como respaldo", "No anotarlo para no tener problemas", "Anotar 1 % para cumplir la meta", "Un escape se registra e informa; ocultarlo agrava el daño."),
        ("abc", "{F} Una persona propone botar los envases de productos al mar porque «son pocos». ¿Qué respondes?", "Que no: los residuos se clasifican y se entregan según la norma vigente a gestores autorizados", "Que sí, si son envases pequeños", "Que sí, si nadie lo ve", "Botar residuos daña el ecosistema y rompe la norma."),
        ("abc", "{F} Se plantea que los escapes se deben a redes en mal estado. ¿Qué conclusión es adecuada?", "Es una causa probable que hay que comprobar con la pauta de mantención y los registros", "Queda demostrado porque hubo escapes", "No puede tener ninguna relación con las redes", "Una causa probable se comprueba con los registros de mantención."),
    ],
    ctx=("abc", "Un conocido te propone enterrar en la orilla los animales muertos de su centro «porque es más barato». ¿Qué respondes?", "Que no, porque los residuos se manejan según la norma vigente por personal autorizado, y que lo consultarás con un adulto responsable", "Que sí, si lo entierra profundo", "Que sí, si es poco", "Un manejo incorrecto de residuos orgánicos daña el ecosistema y rompe la norma."),
    sc=[
        ("En Acuicultura: ¿qué es un escape?", "La salida de animales de cultivo hacia el ambiente", "Puede afectar a las especies nativas."),
        ("¿Cómo se calcula el porcentaje de escape?", "Escapados × 100 ÷ animales iniciales", "Se compara con los animales iniciales."),
        ("¿Quién maneja los residuos?", "Personal y gestores autorizados, según la norma vigente", "Los residuos exigen un manejo autorizado según la norma."),
    ],
    op=("Ficha de ejemplo: residuos de otro centro: plásticos 300 kg, envases 100 kg y orgánico 600 kg; se reciclaron 150 kg de plástico; escaparon 100 peces de 5.000 iniciales; meta de escapes de 1 % o menos. Escribe (a) el total de residuos, (b) el porcentaje de plástico reciclado, (c) el porcentaje de escape y si cumple la meta, (d) qué haces con el dato de escape.",
        "(a) 300 + 100 + 600 = 1.000 kg. (b) 150 × 100 ÷ 300 = 50 %. (c) 100 × 100 ÷ 5.000 = 2 %; no cumple, porque supera el 1 %. (d) Se registra e informa a quien corresponde según la norma vigente, con el registro como respaldo, sin cambiar el dato.",
        ["suma los residuos", "calcula el porcentaje reciclado", "calcula el escape y compara", "propone informar sin alterar"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre los peces escapados", "ocultar el escape", "sugerir botar residuos"],
        "Pregunta: «¿qué comparas con la meta de escapes?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa tres tipos de residuos con sus kilos y calcula el porcentaje de cada uno.",
    extend="Explica por qué un escape pequeño igual debe registrarse e informarse.",
)

# ============================================================ OAE-08, clase 5
F = ("Ficha 14 (caso de ejemplo, inventado). Centro Demo tuvo 8 caídas al año en una pasarela y compara dos medidas de prevención. Medida A, cartel y charla de seguridad: $300.000 en total, con una reducción esperada de 25 % de las caídas (dato de ejemplo). "
     "Medida B, baranda fija instalada por personal autorizado: $1.200.000 en total, con una reducción esperada de 75 % de las caídas (dato de ejemplo). Después de aplicar B, el reporte del año siguiente anotó 2 caídas.")
build(
    O8, 5, F,
    use="Aprenderé a comparar medidas de prevención con costo, efectividad y nivel de la jerarquía de controles, y a verificar con nuevos registros que una medida funcionó.",
    prior=["Sé la jerarquía de controles.", "Sé calcular un porcentaje con números enteros.", "Sé qué es verificar una medida."],
    explain=[
        "Comparar medidas es poner lado a lado el costo, cuántos incidentes evita cada una y a qué nivel de la jerarquía pertenece. Los incidentes evitados se calculan con el porcentaje de reducción: incidentes actuales × reducción ÷ 100. El costo por incidente evitado es el costo de la medida dividido entre los incidentes que evita. La jerarquía prefiere las medidas de nivel más alto, como las de ingeniería, porque actúan sobre el peligro y no dependen de la memoria de cada persona.",
        "Verificar una medida es comparar los datos de antes y después. La reducción real de un periodo se calcula como (incidentes antes − incidentes después) × 100 ÷ incidentes antes y se compara con la reducción esperada. Si la medida no funcionó como se esperaba, se revisa; los datos nunca se cambian. La decisión final la toma la jefatura con el comité paritario y el prevencionista; el estudiante entrega la comparación escrita.",
        f"Los costos y las reducciones son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("incidentes evitados", "incidentes actuales por el porcentaje de reducción, dividido entre 100"), ("costo por incidente evitado", "costo de la medida dividido entre los incidentes que evita"), ("reducción real", "porcentaje en que bajaron los incidentes entre antes y después"), ("reducción esperada", "porcentaje de baja que se calcula antes de aplicar una medida")],
    worked=[
        ("Incidentes evitados", "Hay 20 incidentes de ejemplo y una medida reduce 30 %. ¿Cuántos evita?", ["20 × 30 = 600.", "600 ÷ 100 = 6."], "6 incidentes"),
        ("Costo por incidente evitado", "Una medida de ejemplo cuesta $90.000 y evita 6 incidentes. ¿Cuánto cuesta cada incidente evitado?", ["Se divide el costo entre los incidentes evitados.", "90.000 ÷ 6 = 15.000."], "$15.000"),
    ],
    mistakes=[("Elegir la medida más barata sin mirar cuántos incidentes evita.", "Una medida barata puede evitar muy pocos incidentes.", "Se compara el costo con la efectividad."),
              ("Dar por buena una medida sin comparar los datos de antes y después.", "Sin verificar no se sabe si funcionó.", "Se comparan los registros de antes y después.")],
    T=[
        ("abc", "En Acuicultura: ¿qué es el costo por incidente evitado?", "El costo de la medida dividido entre los incidentes que evita", "El costo total del centro dividido entre sus trabajadores", "El precio de un cartel", "Relaciona lo que cuesta la medida con lo que logra."),
        ("abc", "En Acuicultura: ¿qué es la reducción real de una medida?", "El porcentaje en que bajaron los incidentes entre antes y después", "El porcentaje que se espera antes de aplicarla", "El costo de la medida", "La reducción real se calcula con datos de antes y después."),
        ("abc", "En Acuicultura: ¿por qué la jerarquía de controles prefiere las medidas de ingeniería a las administrativas?", "Porque actúan sobre el peligro y no dependen de que cada persona lo recuerde", "Porque siempre cuestan menos", "Porque no necesitan verificarse", "Las de ingeniería actúan sobre el lugar y son más estables."),
        ("=", "{F} ¿Cuántas caídas evita la medida A, según la reducción esperada?", "8*25//100", "Se multiplican las caídas por la reducción y se dividen entre 100.", " caídas"),
        ("=", "{F} ¿Cuántas caídas evita la medida B, según la reducción esperada?", "8*75//100", "Se multiplican las caídas por la reducción y se dividen entre 100.", " caídas"),
        ("=", "{F} ¿Cuánto cuesta cada caída evitada con la medida A, en pesos?", "300000//(8*25//100)", "Se divide el costo entre las caídas que evita.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta cada caída evitada con la medida B, en pesos?", "1200000//(8*75//100)", "Se divide el costo entre las caídas que evita.", " pesos"),
        ("abc", "{F} ¿Qué nivel de la jerarquía es la medida B?", "Ingeniería, porque cambia físicamente el lugar", "Administrativo, porque ordena una conducta", "EPP, porque protege a quien la usa", "Una baranda fija modifica el lugar."),
        ("abc", "{F} ¿Qué medida evita más caídas aunque cueste más por caída evitada?", "La medida B, que evita 6 caídas frente a 2 de la A", "La medida A, porque cuesta menos", "Ambas evitan lo mismo", "B evita más caídas; la elección también considera el nivel de la jerarquía."),
        ("=", "{F} ¿Cuántas caídas bajaron en la práctica tras aplicar B?", "8-2", "Se resta el número de caídas del año siguiente al de antes.", " caídas"),
        ("=", "{F} ¿Cuál fue la reducción real tras aplicar B, en %?", "(8-2)*100//8", "Se calcula la baja de caídas, se multiplica por 100 y se divide entre las caídas de antes.", " %"),
        ("abc", "{F} La reducción real fue 75 % y la esperada también. ¿Qué conclusión es adecuada?", "La medida funcionó como se esperaba", "La medida no sirvió", "No se puede comparar", "Reducción real y esperada coinciden, así que cumplió lo previsto."),
        ("abc", "{F} Una persona propone reportar solo 1 caída el año siguiente para que la medida se vea mejor. ¿Qué respondes?", "Que no: se reportan los datos reales aunque sean menos favorables", "Que sí, si lo aclara después", "Que sí, porque la medida lo merece", "Alterar un reporte falsifica la verificación de la medida."),
    ],
    ctx=("abc", "Un amigo te sugiere instalar tú mismo una baranda en la pasarela de un centro de cultivo «para ahorrar». ¿Qué respondes?", "Que no, porque esa instalación la hace personal autorizado con norma vigente y equipo de flotación, y que lo consultarás con un adulto responsable", "Que sí, si trabajan juntos", "Que sí, si hay buen clima", "Trabajar sobre una pasarela exige personal autorizado y medidas de seguridad."),
    sc=[
        ("En Acuicultura: ¿cómo se calculan los incidentes evitados?", "Incidentes actuales × reducción ÷ 100", "Se aplica el porcentaje de reducción al total."),
        ("¿Cómo se verifica una medida?", "Comparando los datos de antes y después", "La verificación se basa en nuevos datos."),
        ("¿Quién decide qué medida aplicar?", "La jefatura con el comité paritario y el prevencionista", "El estudiante entrega la comparación escrita."),
    ],
    op=("Ficha de ejemplo: un centro tiene 10 golpes al año. Medida A, regla escrita y charla: $200.000, reduce 20 %. Medida B, protección fija sobre una parte móvil: $800.000, reduce 80 %. Escribe (a) los golpes que evita cada medida, (b) el costo por golpe evitado de cada una, (c) cuál es de mayor nivel en la jerarquía, (d) cómo verificarías que funcionó.",
        "(a) A: 10 × 20 ÷ 100 = 2 golpes; B: 10 × 80 ÷ 100 = 8 golpes. (b) A: 200.000 ÷ 2 = 100.000 pesos; B: 800.000 ÷ 8 = 100.000 pesos. (c) La B, que es de ingeniería. (d) Comparando los golpes del reporte del año siguiente con los 10 de antes.",
        ["calcula los incidentes evitados", "calcula el costo por incidente evitado", "identifica el nivel de la jerarquía", "propone verificar con datos"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "elegir solo por costo", "no verificar con nuevos datos"],
        "Pregunta: «¿qué datos comparas para saber si la medida funcionó?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa dos medidas con costo y reducción, y calcula cuántos incidentes evita cada una.",
    extend="Explica con un ejemplo por qué una medida barata puede no ser la mejor.",
)
