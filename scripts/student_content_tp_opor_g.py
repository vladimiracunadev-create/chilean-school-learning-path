"""Operaciones Portuarias TP 3.º y 4.º medio: OAE-07 (prevención de accidentes, emergencias, principios básicos de primeros auxilios y medio ambiente). Solo conceptos y reglas generales; todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_opor_common import AVISO, EMER, build

O7 = "TP-OPOR-3y4-OAE-07"

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (registro mensual de ejemplo, inventado). «Terminal Demo» tiene 200 trabajadores. En el mes hubo 3 accidentes con tiempo perdido y 5 sin tiempo perdido, y 14 incidentes sin daño. Los accidentes con tiempo perdido sumaron 18 días perdidos. "
     "Condiciones anotadas: iluminación insuficiente en un pasillo, un piso con aceite derramado y una señal de prohibición borrada. Conductas anotadas: una persona cruzó una ruta de camiones sin mirar y otra caminó mirando su teléfono.")
build(
    O7, 1, F,
    use="Aprenderé qué es un accidente y qué es un incidente, qué son las condiciones y los actos inseguros, cómo se calcula una tasa de accidentabilidad de ejemplo y qué normas generales rigen la seguridad en una faena portuaria.",
    prior=["Sé distinguir peligro y riesgo.", "Sé calcular un porcentaje sencillo.", "Sé ordenar la jerarquía de controles."],
    explain=[
        "Un accidente es un suceso no deseado que causa daño a una persona o a un bien. Un incidente es un suceso que pudo causar daño pero no lo causó: es una advertencia. Los accidentes pueden tener tiempo perdido, si la persona debe dejar de trabajar, o no tenerlo. Los sucesos se explican por condiciones inseguras, situaciones del lugar o del equipo que pueden causar daño, como un piso con aceite, y por actos inseguros, conductas que pueden causar daño, como caminar mirando el teléfono entre vehículos.",
        "Para medir la seguridad se usan índices. La tasa de accidentabilidad de ejemplo es el número de accidentes dividido entre el número de trabajadores, multiplicado por 100. Los accidentes y los incidentes se registran siempre, con honestidad, y se investigan para evitar que se repitan. Se previene con la jerarquía de controles: eliminar el peligro, sustituirlo, usar barreras físicas, reglas y capacitación, y, al final, el EPP.",
        f"Las faenas portuarias se rigen por la norma vigente y las fiscalizan las entidades competentes. Todos los datos de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("accidente", "suceso no deseado que causa daño a una persona o a un bien"), ("incidente", "suceso que pudo causar daño pero no lo causó"), ("accidente con tiempo perdido", "accidente tras el cual la persona debe dejar de trabajar"), ("condición insegura", "situación del lugar o del equipo que puede causar daño"), ("acto inseguro", "conducta de una persona que puede causar daño"), ("tasa de accidentabilidad", "accidentes divididos entre trabajadores, por 100")],
    worked=[
        ("Clasificar un suceso", "Un trabajador de ejemplo tropieza con un cable suelto, pero no se lastima. ¿Es accidente o incidente?", ["No hubo daño a la persona.", "Un suceso que pudo causar daño y no lo causó es un incidente."], "Incidente"),
        ("Calcular una tasa", "Una empresa de ejemplo tiene 100 trabajadores y 3 accidentes en el mes. ¿Cuál es la tasa de accidentabilidad de ejemplo?", ["Se divide 3 entre 100.", "3 dividido en 100 por 100 es 3."], "3"),
    ],
    mistakes=[("Creer que si nadie se lastimó, no hay nada que registrar.", "Un incidente es una advertencia de que puede ocurrir un accidente.", "Registra e investiga también los incidentes."),
              ("Buscar solo a la persona culpable de un accidente.", "También hay condiciones inseguras y causas de fondo que deben corregirse.", "Revisa las condiciones, los actos y las causas de fondo.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es un accidente?", "Un suceso no deseado que causa daño a una persona o a un bien", "Un suceso que pudo causar daño pero no lo causó", "Un documento donde se anotan los turnos", "El accidente produce daño; si no lo hay, es un incidente."),
        ("abc", "En Operaciones Portuarias: ¿qué es un incidente?", "Un suceso que pudo causar daño pero no lo causó", "Un accidente grave con varios días perdidos", "Una falta administrativa de un documento", "El incidente es una advertencia sin daño."),
        ("abc", "En Operaciones Portuarias: ¿qué es una condición insegura?", "Una situación del lugar o del equipo que puede causar daño", "Una conducta de una persona que puede causar daño", "Un permiso de trabajo vencido", "La condición se refiere al lugar o al equipo; la conducta es un acto inseguro."),
        ("abc", "{F} ¿Cuál de las observaciones es una condición insegura?", "La iluminación insuficiente en un pasillo", "Caminar mirando el teléfono", "Cruzar una ruta de camiones sin mirar", "La iluminación pertenece al lugar; las otras dos son conductas."),
        ("abc", "{F} ¿Cuál de las observaciones es un acto inseguro?", "Caminar mirando el teléfono entre vehículos", "El piso con aceite derramado", "La señal de prohibición borrada", "Mirar el teléfono es una conducta; el piso y la señal son condiciones."),
        ("=", "{F} ¿Cuántos accidentes hubo en el mes, con y sin tiempo perdido?", "3+5", "Se suman los accidentes con tiempo perdido y los que no lo tuvieron.", " accidentes"),
        ("=", "{F} ¿Cuál es la tasa de accidentabilidad de ejemplo del mes?", "(3+5)*100//200", "Se divide el total de accidentes entre los trabajadores y se multiplica por 100.", ""),
        ("=", "{F} ¿Cuántos días perdidos hubo en promedio por cada accidente con tiempo perdido?", "18//3", "Se dividen los días perdidos entre los accidentes con tiempo perdido.", " días"),
        ("=", "Una empresa de ejemplo tiene 250 trabajadores y 5 accidentes en el año. ¿Cuál es su tasa de accidentabilidad de ejemplo?", "5*100//250", "Se divide los accidentes entre los trabajadores y se multiplica por 100.", ""),
        ("abc", "{F} Hubo 14 incidentes sin daño. ¿Qué corresponde hacer con ellos?", "Registrarlos e investigarlos, porque advierten de posibles accidentes", "Ignorarlos, porque nadie se lastimó", "Anotarlos solo si alguien lo reclama", "Un incidente muestra una falla que puede causar un accidente."),
        ("abc", "Durante una visita de ejemplo, una persona queda aplastada junto a un equipo. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a mover el equipo para sacarla", "Tirar de la persona para sacarla de ahí", "Mover el equipo o a la persona sin formación puede empeorar el daño."),
        ("=", "{F} Si con medidas de prevención los accidentes del mes bajaran a la mitad, ¿cuál sería la tasa de accidentabilidad de ejemplo?", "((3+5)//2)*100//200", "Se calcula la mitad de los accidentes y se aplica la fórmula de la tasa.", ""),
        ("abc", "{F} Para corregir el piso con aceite derramado, ¿cuál medida es de nivel más efectivo?", "Eliminar la fuga de aceite en su origen", "Poner un letrero de piso resbaladizo", "Entregar calzado antideslizante a todo el personal", "Quitar la fuente actúa sobre el peligro; el letrero es administrativo y el calzado es EPP."),
    ],
    ctx=("abc", "Un compañero de práctica dice: «casi me pasa algo, pero como no me lastimé, no lo anoto». ¿Qué le respondes?", "Que lo anote como incidente, porque advierte de un posible accidente", "Que tiene razón, porque no hubo daño", "Que lo anote solo si fue grave", "Un incidente se registra para prevenir un accidente futuro."),
    sc=[
        ("En Operaciones Portuarias: ¿qué es un incidente?", "Un suceso que pudo causar daño pero no lo causó", "Es una advertencia de falla que no causó daño."),
        ("¿Cómo se calcula la tasa de accidentabilidad de ejemplo?", "Accidentes entre trabajadores, por 100", "Es un porcentaje respecto de los trabajadores."),
        ("¿Qué se hace con los incidentes?", "Se registran y se investigan", "Los incidentes pueden anticipar un accidente futuro."),
    ],
    op=("Registro de ejemplo de un terminal ficticio con 150 trabajadores: 2 accidentes con tiempo perdido, 4 sin tiempo perdido y 9 incidentes sin daño. Condiciones anotadas: un pasillo sin luz y un extintor sin señal. Conductas anotadas: una persona sin casco en una zona con cargas suspendidas. Escribe (a) cuántos accidentes hubo en total, (b) la tasa de accidentabilidad de ejemplo, (c) una condición insegura y un acto inseguro del caso, (d) por qué se registran también los incidentes.",
        "(a) 2 + 4 = 6 accidentes. (b) 6 × 100 ÷ 150 = 4. (c) Condición: el pasillo sin luz; acto: estar sin casco en la zona de cargas suspendidas. (d) Porque advierten de fallas que pueden causar un accidente y permiten corregirlas antes.",
        ["suma los accidentes", "calcula la tasa", "distingue condición y acto", "explica el valor del incidente"],
        ["hoja con las cuatro respuestas"],
        ["no sumar los accidentes sin tiempo perdido", "confundir condición con acto", "decir que los incidentes no importan"],
        "Pregunta: «¿qué pasó con los incidentes?». Si no responde, pídele que relea la definición de incidente."),
    reinforce="Escribe dos ejemplos inventados de condición insegura y dos de acto inseguro en un recinto portuario.",
    extend="Explica con un ejemplo por qué conviene corregir una condición insegura antes de que ocurra un accidente.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (plan de seguridad de ejemplo, inventado). Zona de muelle de «Terminal Demo». Letreros: un círculo rojo con una diagonal sobre una persona bajo una carga; un triángulo amarillo con un rayo; un círculo azul con un casco; un cuadrado verde con una cruz blanca. "
     "Trabajadores de la zona: 40. EPP disponible: 40 cascos, 40 pares de calzado de seguridad y 30 chalecos reflectantes. En el registro de entrega de EPP constan 38 cascos entregados.")
build(
    O7, 2, F,
    use="Aprenderé a reconocer la señalética de seguridad, los equipos de protección personal, los documentos y los roles de la prevención, y a leer un registro de entrega de EPP.",
    prior=["Sé qué es la jerarquía de controles y el EPP.", "Sé restar y calcular porcentajes sencillos.", "Sé qué es un accidente y un incidente."],
    explain=[
        "La señalética de seguridad usa formas y colores para que se entienda rápido. Una señal de prohibición es un círculo rojo con una diagonal; una de advertencia es un triángulo amarillo; una de obligación es un círculo azul, como la que exige usar casco; y una de salvamento o información es un cuadrado o rectángulo verde, como la que indica primeros auxilios. Las señales borradas o dañadas dejan de cumplir su función y se reponen.",
        "El equipo de protección personal (EPP) incluye casco, calzado de seguridad, chaleco reflectante, guantes, protección auditiva, protección respiratoria y chaleco salvavidas para trabajar cerca del agua. Se entrega a cada persona según su tarea, y su entrega queda en un registro de entrega que dice qué equipo recibió cada persona. El EPP es la última barrera y no reemplaza otros controles. Entre los roles están el prevencionista, que asesora en seguridad, y el comité paritario de higiene y seguridad, integrado por representantes de la empresa y de los trabajadores.",
        f"La matriz de riesgos es una tabla que lista los peligros, sus riesgos y sus controles. Los datos de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("señal de prohibición", "círculo rojo con una diagonal que indica lo que no se debe hacer"), ("señal de advertencia", "triángulo amarillo que avisa de un peligro"), ("señal de obligación", "círculo azul que exige hacer algo, como usar casco"), ("señal de salvamento", "cuadrado o rectángulo verde que indica seguridad, salida o primeros auxilios"), ("registro de entrega de EPP", "documento que dice qué equipo recibió cada persona"), ("prevencionista", "persona que asesora en seguridad"), ("comité paritario", "grupo de representantes de la empresa y de los trabajadores para la seguridad")],
    worked=[
        ("Leer una señal", "Un letrero de ejemplo es un triángulo amarillo con una llama. ¿Qué tipo de señal es?", ["El triángulo amarillo es la forma de las señales de advertencia.", "La llama indica el peligro."], "De advertencia, sobre un peligro de fuego"),
        ("EPP pendiente", "Se necesitan 25 cascos y el registro dice que se entregaron 21. ¿Cuántos faltan por entregar?", ["Se resta lo entregado a lo necesario.", "25 menos 21 son 4."], "4 cascos"),
    ],
    mistakes=[("Creer que una señal de advertencia prohíbe hacer algo.", "La advertencia avisa de un peligro; la prohibición está en el círculo rojo.", "Mira la forma y el color de la señal."),
              ("Creer que entregar EPP sin dejar registro es suficiente.", "Sin registro no se puede demostrar quién lo recibió.", "Anota siempre la entrega en el registro.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué indica un círculo rojo con una diagonal sobre un dibujo?", "Una prohibición", "Una obligación", "Una advertencia de peligro", "El círculo rojo con diagonal es la forma de la prohibición."),
        ("abc", "En Operaciones Portuarias: ¿qué indica un círculo azul con un casco?", "Que es obligatorio usar casco", "Que está prohibido usar casco", "Que hay un peligro de caída de casco", "El círculo azul es una señal de obligación."),
        ("abc", "En Operaciones Portuarias: ¿qué es el comité paritario de higiene y seguridad?", "Un grupo de representantes de la empresa y de los trabajadores para temas de seguridad", "Un grupo de inspectores de la aduana", "El equipo que opera los equipos de carga", "El comité paritario reúne a representantes de ambas partes."),
        ("abc", "{F} ¿Qué indica el triángulo amarillo con un rayo?", "Una advertencia de peligro, aquí asociado a la electricidad", "Una obligación de usar equipo eléctrico", "Una salida de emergencia", "El triángulo amarillo es una advertencia y el rayo indica el tipo de peligro."),
        ("abc", "{F} ¿Qué señal de la ficha indica un lugar de seguridad o de primeros auxilios?", "El cuadrado verde con una cruz blanca", "El círculo azul con un casco", "El círculo rojo con una diagonal", "El verde se usa para salvamento y primeros auxilios."),
        ("=", "{F} ¿Cuántos chalecos reflectantes faltan para que cada trabajador de la zona tenga uno?", "40-30", "Se resta los chalecos disponibles a los trabajadores.", " chalecos"),
        ("=", "{F} ¿Cuántos cascos faltan por registrar como entregados?", "40-38", "Se resta lo registrado a los cascos disponibles.", " cascos"),
        ("abc", "{F} ¿Para qué sirve el registro de entrega de EPP?", "Para demostrar qué equipo recibió cada persona", "Para reemplazar la señalética de la zona", "Para evitar que se use el equipo", "El registro deja constancia de la entrega a cada persona."),
        ("=", "{F} Un chaleco reflectante cuesta $5.000 (valor de ejemplo). ¿Cuántos pesos cuesta completar los chalecos que faltan?", "(40-30)*5000", "Se multiplican los chalecos faltantes por su precio.", " pesos"),
        ("abc", "{F} Un trabajador dice: «tengo casco, así que puedo pasar bajo la carga suspendida». ¿Qué respuesta es correcta?", "Es falso: la señal de prohibición manda y el casco no elimina el peligro", "Es cierto: el casco lo protege de cualquier carga", "Es cierto, si pasa rápido", "El EPP es la última barrera y no autoriza a ignorar una prohibición."),
        ("abc", "En Operaciones Portuarias: ¿por qué la señalética usa formas y colores distintos?", "Para que se entienda rápido el tipo de mensaje, aunque no se lea el texto", "Para que el recinto se vea más ordenado", "Porque los colores reemplazan a las normas", "La forma y el color permiten reconocer el mensaje a primera vista."),
        ("=", "{F} ¿Qué porcentaje de los cascos disponibles figura como entregado en el registro?", "38*100//40", "Se divide lo entregado entre lo disponible y se multiplica por 100.", " %"),
        ("abc", "{F} Una señal de prohibición de la zona está borrada. ¿Qué corresponde?", "Avisar a la jefatura para reponerla, porque una señal borrada no cumple su función", "Dejarla, porque todos ya la conocen", "Pintarla a mano con otro color", "Una señal dañada debe reponerse para que cumpla su mensaje."),
    ],
    ctx=("abc", "Un amigo te muestra una foto de un puerto y dice: «esas señales amarillas son prohibiciones». ¿Qué le respondes?", "Que los triángulos amarillos advierten de un peligro y que la prohibición es un círculo rojo con una diagonal", "Que tiene razón, porque todo lo amarillo prohíbe", "Que las señales no tienen significado fijo", "Cada forma y color de señal tiene un significado distinto."),
    sc=[
        ("En Operaciones Portuarias: ¿qué forma tiene una señal de advertencia?", "Un triángulo amarillo", "El triángulo amarillo avisa de un peligro."),
        ("¿Qué es el EPP en la jerarquía de controles?", "La última barrera", "Protege a una persona pero no quita el peligro."),
        ("¿Qué documento dice qué equipo recibió cada persona?", "El registro de entrega de EPP", "Deja constancia por escrito de cada entrega realizada."),
    ],
    op=("Plan de seguridad de ejemplo de un terminal ficticio. Zona de patio con 25 trabajadores. EPP disponible: 25 cascos, 20 chalecos reflectantes y 25 pares de calzado. El registro de entrega muestra 22 cascos entregados. Letreros: un círculo rojo con una diagonal sobre una persona frente a un camión y un cuadrado verde con una flecha. Escribe (a) cuántos chalecos faltan, (b) cuántos cascos faltan por entregar, (c) qué indica cada letrero, (d) por qué el EPP no reemplaza a los letreros ni a otras medidas.",
        "(a) 25 − 20 = 5 chalecos. (b) 25 − 22 = 3 cascos. (c) El círculo rojo con diagonal indica una prohibición; el cuadrado verde con una flecha indica una salida o un lugar de seguridad. (d) Porque el EPP es la última barrera: no quita el peligro y protege solo a quien lo usa.",
        ["calcula los chalecos faltantes", "calcula los cascos pendientes", "interpreta ambos letreros", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["confundir advertencia con prohibición", "olvidar restar lo entregado", "decir que el EPP basta"],
        "Pregunta: «¿qué forma y color tiene una prohibición?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Dibuja con palabras una señal de cada tipo (prohibición, advertencia, obligación y salvamento) y escribe qué significa.",
    extend="Explica con un ejemplo por qué una señal borrada es una condición insegura.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (informe de ejemplo, inventado). En «Terminal Demo», una persona resbaló en un pasillo del patio y se lastimó una pierna (lesión menor). Antecedentes: el piso tenía aceite derramado desde hacía 2 días, sin señal de aviso; la persona caminaba mirando su teléfono; "
     "la limpieza del pasillo se hace cada 3 días; y se había registrado una queja de seguridad sobre el aceite que no fue atendida, porque no existe una persona asignada para atender las quejas de seguridad. "
     "El accidente causó 6 días perdidos (valor de ejemplo) y cada día perdido cuesta $30.000 (valor de ejemplo).")
build(
    O7, 3, F,
    use="Aprenderé a analizar un accidente en papel: separar causas inmediatas y causas de fondo, proponer medidas correctivas ordenadas por jerarquía y calcular su costo de ejemplo.",
    prior=["Sé distinguir condición insegura y acto inseguro.", "Sé ordenar la jerarquía de controles.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Investigar un accidente sirve para evitar que se repita, no para castigar. Se separan las causas inmediatas, lo que ocurrió justo antes del daño, como un piso con aceite o una conducta distraída, de la causa de fondo o causa raíz, la razón de origen que permitió que ocurriera, como una falla de organización. Una pregunta útil es «¿por qué ocurrió esto?», repetida hasta llegar al origen.",
        "Las medidas correctivas atacan las causas y se ordenan por la jerarquía de controles: eliminar la fuente del peligro es más efectivo que poner un letrero o entregar EPP. Corregir solo la causa inmediata, por ejemplo limpiar el piso una vez, no basta si la causa raíz sigue: el problema volverá. Todo accidente se registra y se investiga con honestidad, aunque la lesión sea menor.",
        f"El costo de un accidente se calcula en días perdidos por su costo diario, y es solo una parte de su costo real. Los datos de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("causa inmediata", "lo que ocurrió justo antes del daño"), ("causa raíz", "razón de fondo que permitió que el accidente ocurriera"), ("medida correctiva", "acción para eliminar o reducir una causa"), ("investigación de accidente", "análisis para evitar que se repita"), ("días perdidos", "días de trabajo que se pierden por un accidente")],
    worked=[
        ("Causa inmediata y causa raíz", "Un trabajador de ejemplo se golpea con una puerta mal sujeta; el mantenimiento de las puertas no tiene calendario. ¿Cuál es la causa inmediata y cuál la raíz?", ["La causa inmediata es la puerta mal sujeta, que ocurrió justo antes del golpe.", "La causa raíz es que el mantenimiento no tiene calendario."], "Inmediata: la puerta mal sujeta; raíz: falta de un calendario de mantenimiento"),
        ("Costo de un accidente", "Un accidente de ejemplo causa 4 días perdidos a $20.000 por día. ¿Cuánto cuestan los días perdidos?", ["Se multiplican los días por el costo diario.", "4 por 20.000 son 80.000."], "$80.000"),
    ],
    mistakes=[("Quedarse con la causa inmediata y culpar a la persona.", "No se corrige la causa de fondo y el accidente puede repetirse.", "Pregunta «¿por qué?» hasta llegar a la causa raíz."),
              ("Creer que un accidente con lesión menor no se investiga.", "Puede repetirse con consecuencias mayores.", "Registra e investiga todos los accidentes.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es la causa inmediata de un accidente?", "Lo que ocurrió justo antes del daño", "La razón de fondo que permitió que ocurriera", "La sanción que se aplica a una persona", "La causa inmediata está junto al daño; la de fondo es la raíz."),
        ("abc", "En Operaciones Portuarias: ¿qué es la causa raíz de un accidente?", "La razón de fondo que permitió que el accidente ocurriera", "Lo que ocurrió justo antes del daño", "El nombre de la persona lesionada", "La causa raíz es el origen organizativo o técnico del problema."),
        ("abc", "En Operaciones Portuarias: ¿para qué se investiga un accidente?", "Para evitar que se repita", "Para encontrar a quién castigar", "Para cumplir un trámite sin consecuencias", "La investigación busca prevenir, no castigar."),
        ("abc", "{F} ¿Cuál es el acto inseguro del caso?", "Caminar mirando el teléfono", "El aceite derramado en el piso", "La limpieza cada 3 días", "Mirar el teléfono es una conducta; el aceite y la limpieza son condiciones."),
        ("abc", "{F} ¿Cuál es la condición insegura del caso?", "El piso con aceite derramado y sin señal", "La persona lesionada", "La queja registrada", "El aceite en el piso es una condición del lugar."),
        ("abc", "{F} ¿Cuál es la causa raíz que explica por qué el aceite no se atendió a tiempo?", "No existe una persona asignada para atender las quejas de seguridad", "La persona caminaba distraída", "El piso estaba mojado", "La queja no se atendió por falta de un responsable; lo demás son causas inmediatas."),
        ("=", "{F} ¿Cuántas limpiezas del pasillo se hacen en 30 días, con la frecuencia de la ficha?", "30//3", "Se divide el período entre los días que pasan entre limpiezas.", " limpiezas"),
        ("=", "{F} Si la limpieza se hiciera todos los días, ¿cuántas limpiezas más habría en 30 días?", "30-30//3", "Se resta las limpiezas actuales a las 30 limpiezas diarias.", " limpiezas"),
        ("=", "{F} ¿Cuántos pesos cuestan los días perdidos del accidente?", "6*30000", "Se multiplican los días perdidos por el costo diario.", " pesos"),
        ("abc", "{F} ¿Basta con sancionar a la persona que miraba el teléfono?", "No: hay causas de fondo, como la falta de un responsable de quejas, que también deben corregirse", "Sí, porque la causa única es el acto inseguro", "Sí, porque el aceite no es un peligro", "Corregir solo la conducta deja sin resolver las causas de fondo."),
        ("abc", "En Operaciones Portuarias: ¿por qué corregir solo la causa inmediata no basta?", "Porque si la causa raíz sigue, el problema puede repetirse", "Porque la causa inmediata nunca importa", "Porque la causa raíz siempre es una persona", "Sin corregir el origen, el problema vuelve."),
        ("=", "{F} Si en un año ocurrieran 4 accidentes iguales a este, ¿cuántos pesos costarían en total los días perdidos?", "4*6*30000", "Se multiplican los accidentes por los días perdidos y por el costo diario.", " pesos"),
        ("abc", "{F} Un jefe propone cerrar el informe sin investigar «porque la lesión fue menor». ¿Qué respuesta es correcta?", "Es falso: se investiga igual para evitar que se repita con consecuencias mayores", "Es cierto: las lesiones menores no se investigan", "Es cierto, si la persona no reclama", "Un accidente menor puede ser una advertencia de uno grave."),
    ],
    ctx=("abc", "Un compañero dice: «la culpa fue de quien se distrajo; con eso el informe queda cerrado». ¿Qué respondes?", "Que también hay condiciones y causas de fondo que deben corregirse, no solo la conducta", "Que tiene razón, porque la culpa es de una sola persona", "Que el informe se cierra si la persona pide disculpas", "Un informe útil identifica y corrige también las causas de fondo."),
    sc=[
        ("En Operaciones Portuarias: ¿qué es la causa raíz?", "La razón de fondo que permitió el accidente", "Corregirla evita que el problema se repita."),
        ("¿Qué medida es de nivel más efectivo?", "Eliminar la fuente del peligro", "La eliminación actúa en el origen del problema."),
        ("¿Para qué se investiga un accidente?", "Para evitar que se repita", "La investigación busca prevenir futuros accidentes."),
    ],
    op=("Informe de ejemplo: en un terminal ficticio, una persona se golpeó la cabeza con una carga que se balanceaba sobre una zona de paso; la zona no tenía barrera ni señal, y no hay una persona encargada de revisar las zonas de paso. El accidente causó 3 días perdidos a $25.000 por día. Escribe (a) la causa inmediata, (b) la causa raíz, (c) una medida correctiva de nivel alto, (d) el costo de los días perdidos.",
        "(a) La carga que se balanceaba sobre una zona de paso sin barrera ni señal. (b) La falta de una persona encargada de revisar las zonas de paso. (c) Una barrera fija que impida el paso bajo la zona de cargas. (d) 3 × 25.000 = $75.000.",
        ["identifica la causa inmediata", "identifica la causa raíz", "propone una medida de nivel alto", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["culpar solo a la persona lesionada", "proponer solo un letrero", "olvidar multiplicar por los días"],
        "Pregunta: «¿por qué no había quien revisara la zona?». Si no responde, pídele que relea la definición de causa raíz."),
    reinforce="Inventa un accidente breve y escribe una causa inmediata y una causa raíz.",
    extend="Explica con un ejemplo por qué «tener más cuidado» no es una medida correctiva suficiente.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (plan de emergencia de ejemplo, inventado). En las oficinas y la bodega de «Terminal Demo» hay 90 personas y 3 salidas de emergencia señalizadas. Cada salida permite pasar 15 personas por minuto (valor de ejemplo). "
     "En un simulacro de evacuación anterior se tardaron 4 minutos en llegar al punto de encuentro. Capacitación de seguridad: cada curso tiene cupo para 18 personas y dura 4 horas; deben capacitarse las 90 personas. "
     "Las vías de evacuación y el punto de encuentro están señalizados.")
build(
    O7, 4, F,
    use="Aprenderé los conceptos básicos de una emergencia de fuego y de evacuación, qué hace una persona sin capacitación y cómo se calculan tiempos de evacuación y capacitaciones en papel.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé qué es una señal de salvamento.", "Sé qué es el EPP y la jerarquía de controles."],
    explain=[
        "El fuego necesita tres cosas, que forman el triángulo del fuego: calor, combustible y oxígeno. Sin una de ellas, el fuego no se mantiene. Un plan de emergencia define las vías de evacuación, caminos señalizados que llevan de forma segura al exterior, y el punto de encuentro, el lugar seguro donde se reúne el personal tras evacuar para ser contado. Las vías y las salidas deben mantenerse siempre despejadas, aunque sea por poco tiempo.",
        "Combatir un fuego es una tarea de personal capacitado y autorizado, con los equipos que corresponden. Una persona sin esa capacitación no intenta apagarlo: da la alarma, evacúa por la vía señalizada hacia el punto de encuentro y avisa a un adulto responsable y a emergencias. Para planificar se calcula el tiempo teórico de evacuación, que es el número de personas dividido entre las personas que pasan por minuto por todas las salidas, y se compara con el de los simulacros.",
        f"Todos los números de esta clase son de ejemplo. La norma vigente fija las exigencias reales. {EMER} {AVISO}",
    ],
    vocab=[("triángulo del fuego", "calor, combustible y oxígeno, los tres elementos del fuego"), ("vía de evacuación", "camino señalizado que lleva de forma segura al exterior"), ("punto de encuentro", "lugar seguro donde se reúne el personal tras evacuar"), ("simulacro", "ejercicio que practica un plan de emergencia"), ("tiempo teórico de evacuación", "personas divididas entre las que pasan por minuto por las salidas"), ("emergencia", "situación grave e inesperada que exige actuar rápido")],
    worked=[
        ("Tiempo teórico", "En un plan de ejemplo hay 60 personas y 2 salidas por las que pasan 10 personas por minuto cada una. ¿Cuántos minutos de evacuación teóricos hay?", ["Entre las dos salidas pasan 2 por 10, o sea 20 personas por minuto.", "60 dividido en 20 son 3."], "3 minutos"),
        ("Cursos necesarios", "Hay que capacitar a 40 personas y cada curso tiene cupo para 10. ¿Cuántos cursos hacen falta?", ["Se divide el total de personas entre el cupo.", "40 dividido en 10 son 4."], "4 cursos"),
    ],
    mistakes=[("Intentar apagar un fuego sin capacitación para «ayudar».", "Se expone a un riesgo grave y puede retrasar la alarma y la evacuación.", "Da la alarma, evacúa y avisa."),
              ("Dejar cajas frente a una salida «solo un rato».", "En una emergencia, un obstáculo puede impedir la salida.", "Mantén despejadas las vías y las salidas siempre.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué tres elementos forman el triángulo del fuego?", "Calor, combustible y oxígeno", "Humo, llama y ceniza", "Agua, aire y calor", "El fuego necesita calor, combustible y oxígeno para mantenerse."),
        ("abc", "En Operaciones Portuarias: ¿qué es una vía de evacuación?", "Un camino señalizado que lleva de forma segura al exterior", "Una ruta por donde entran los camiones al recinto", "Un pasillo donde se guardan los extintores", "La vía de evacuación sirve para salir de forma segura."),
        ("abc", "En Operaciones Portuarias: ¿qué es el punto de encuentro?", "El lugar seguro donde se reúne el personal tras evacuar para ser contado", "La oficina donde se entregan los permisos", "El lugar donde se guarda el EPP", "El punto de encuentro permite saber que todos evacuaron."),
        ("=", "{F} ¿Cuántas personas por minuto pueden pasar entre las 3 salidas?", "3*15", "Se multiplican las salidas por las personas que pasan por cada una.", " personas por minuto"),
        ("=", "{F} ¿Cuántos minutos teóricos tomaría evacuar a las 90 personas?", "90//(3*15)", "Se divide el total de personas entre las que pasan por minuto.", " minutos"),
        ("abc", "{F} Una persona sin capacitación ve un inicio de fuego en la bodega. ¿Qué corresponde?", "Dar la alarma, evacuar por la vía señalizada al punto de encuentro y avisar a un adulto responsable y a emergencias", "Intentar apagarlo con lo que encuentre", "Quedarse a observar que no avance", "Combatir el fuego es tarea de personal capacitado; las demás personas evacúan."),
        ("=", "{F} ¿Cuántos cursos de seguridad se necesitan para capacitar a las 90 personas?", "90//18", "Se divide el total de personas entre el cupo de cada curso.", " cursos"),
        ("=", "{F} ¿Cuántas horas de curso se necesitan en total?", "90//18*4", "Se calcula el número de cursos y se multiplica por las horas de cada uno.", " horas"),
        ("=", "En un simulacro de ejemplo hay 120 personas y 4 salidas por las que pasan 10 personas por minuto cada una. ¿Cuántos minutos teóricos de evacuación hay?", "120//(4*10)", "Se divide el total entre las personas que pasan por minuto por todas las salidas.", " minutos"),
        ("abc", "{F} El simulacro anterior tardó 4 minutos y el tiempo teórico es menor. ¿Qué indica?", "Que hay demoras reales, como obstáculos o poca señalización, que deben investigarse y corregirse", "Que todo está bien, porque ningún simulacro tarda menos", "Que el cálculo teórico está equivocado", "Una diferencia entre el tiempo real y el teórico señala problemas por revisar."),
        ("abc", "En Operaciones Portuarias: ¿por qué las vías y las salidas de evacuación deben mantenerse despejadas?", "Porque un obstáculo puede impedir o retrasar la salida en una emergencia", "Porque se ven más ordenadas", "Porque así se pueden guardar más cosas en la bodega", "En una emergencia cada minuto cuenta y un obstáculo puede bloquear la salida."),
        ("=", "{F} Si una de las salidas quedara bloqueada, ¿cuántos minutos teóricos tomaría evacuar a las 90 personas?", "90//(2*15)", "Quedan 2 salidas; se divide el total entre las personas por minuto de ambas.", " minutos"),
        ("abc", "{F} Un jefe propone guardar unas cajas frente a una de las salidas «solo por hoy». ¿Qué respuesta es correcta?", "Es falso: las salidas no se bloquean ni por poco tiempo", "Es cierto: por un día no hay problema", "Es cierto, si hay otras dos salidas", "Una emergencia puede ocurrir en cualquier momento."),
    ],
    ctx=("abc", "Un compañero de práctica dice: «si veo fuego en la bodega, voy a intentar apagarlo antes de avisar, para que no se pierda la carga». ¿Qué respondes?", "Que primero se da la alarma y se evacúa, porque combatir el fuego es tarea de personal capacitado", "Que tiene razón, porque la carga vale más", "Que lo intente solo si el fuego es pequeño", "Las personas valen más que la carga y el fuego puede crecer rápido."),
    sc=[
        ("En Operaciones Portuarias: ¿qué forman el calor, el combustible y el oxígeno?", "El triángulo del fuego", "Sin uno de los tres, el fuego no se mantiene."),
        ("¿Qué hace una persona sin capacitación ante un fuego?", "Da la alarma, evacúa y avisa", "Combatir fuego es tarea de personal capacitado."),
        ("¿Para qué sirve el punto de encuentro?", "Para reunir y contar al personal tras evacuar", "Permite saber si falta alguien por evacuar."),
    ],
    op=("Plan de emergencia de ejemplo: 75 personas, 3 salidas por las que pasan 5 personas por minuto cada una, y cursos de seguridad de 4 horas con cupo para 15 personas. Escribe (a) cuántas personas pasan por minuto entre las tres salidas, (b) los minutos teóricos de evacuación, (c) cuántos cursos y cuántas horas de curso hacen falta para capacitar a las 75 personas, (d) qué hace una persona sin capacitación ante un inicio de fuego.",
        "(a) 3 × 5 = 15 personas por minuto. (b) 75 ÷ 15 = 5 minutos. (c) 75 ÷ 15 = 5 cursos; 5 × 4 = 20 horas. (d) Da la alarma, evacúa por la vía señalizada hacia el punto de encuentro y avisa a un adulto responsable y a emergencias, sin intentar apagar el fuego.",
        ["calcula las personas por minuto", "calcula el tiempo teórico", "calcula cursos y horas", "indica dar la alarma, evacuar y avisar"],
        ["hoja con las cuatro respuestas"],
        ["olvidar multiplicar por las salidas", "sugerir apagar el fuego sin capacitación", "no calcular las horas totales"],
        "Pregunta: «¿quién combate un fuego?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Escribe los tres elementos del triángulo del fuego y explica por qué quitar uno apaga el fuego.",
    extend="Explica con un ejemplo por qué un simulacro puede mostrar problemas que el cálculo teórico no muestra.",
)

# ============================================================ OAE-07, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). En «Terminal Demo» hay una zona donde se carga un líquido de ejemplo, con riesgo de derrame al ambiente. Se esperan 10 derrames por año si no se hace nada. "
     "Alternativa 1 (control administrativo): charlas y letreros; cuesta $400.000 y reduce los derrames esperados de 10 a 6 por año. Alternativa 2 (control de ingeniería): una bandeja de contención fija que retiene lo derramado; cuesta $1.200.000 y reduce los derrames esperados de 10 a 1 por año. "
     "Cada derrame cuesta $250.000 (limpieza y sanciones, valor de ejemplo). Lista de inspección de la zona (10 puntos): en la revisión de ejemplo, 9 puntos están en orden.")
build(
    O7, 5, F,
    use="Aprenderé a comparar medidas de prevención por costo y efectividad, a cuidar el medio ambiente ante derrames y residuos, a recordar los principios básicos de primeros auxilios (proteger, avisar y socorrer) y a verificar con una lista de inspección.",
    prior=["Sé ordenar la jerarquía de controles.", "Sé calcular costos y porcentajes sencillos.", "Sé qué es una lista de verificación y el principio de cero faltas."],
    explain=[
        "La protección del medio ambiente en un puerto es cuidar el agua, el aire y el suelo: evitar derrames, emisiones y residuos mal manejados. Un derrame de un producto al suelo o al agua daña el ambiente y trae costos de limpieza y sanciones según la norma vigente. Al comparar medidas de prevención se suma el costo de la medida y el costo esperado de los derrames que quedan: es el costo de la medida más los derrames esperados por el costo de cada uno. Conviene la medida de menor costo total que, además, sea de un nivel alto en la jerarquía de controles.",
        "Los principios básicos de primeros auxilios se resumen en tres palabras: proteger, avisar y socorrer. Proteger es no exponerse ni acercarse a la zona de riesgo; avisar es llamar a un adulto responsable y a emergencias; socorrer lo hacen solo las personas con formación en primeros auxilios o el personal de emergencia. Ante un derrame o un herido, quien no tiene formación se mantiene a distancia y avisa.",
        f"La lista de inspección se revisa punto por punto y, bajo el principio de cero faltas, se corrige cualquier punto pendiente antes de dar la inspección por buena. Los costos son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("medio ambiente", "el agua, el aire y el suelo que rodean al puerto"), ("derrame", "escape de un líquido o producto fuera de su envase"), ("costo esperado", "costo de los derrames que se espera que ocurran"), ("proteger, avisar y socorrer", "principios básicos de primeros auxilios: no exponerse, llamar y socorrer solo quien tiene formación"), ("lista de inspección", "lista de puntos que se revisan en una zona")],
    worked=[
        ("Costo de una medida", "Una medida de ejemplo cuesta $100.000 y deja 2 derrames esperados por año de $50.000 cada uno. ¿Cuál es el costo total?", ["Los derrames cuestan 2 por 50.000, o sea 100.000.", "100.000 de la medida más 100.000 de derrames son 200.000."], "$200.000"),
        ("Aplicar PAS", "Una persona de ejemplo sin formación ve a alguien caído cerca de una zona de maniobras. ¿Qué hace según proteger, avisar y socorrer?", ["Protege: no se acerca a la zona de riesgo.", "Avisa a un adulto responsable y a emergencias; socorrer lo hace quien tiene formación."], "No se acerca, avisa y deja el socorro a quien tiene formación"),
    ],
    mistakes=[("Creer que la medida más barata siempre es la mejor.", "Puede dejar más derrames esperados y costar más en total.", "Suma el costo de la medida y el de los derrames esperados."),
              ("Acercarse a un herido en una zona de riesgo para ayudar.", "Puede sufrir otro accidente y no tiene formación para socorrer.", "Protege, avisa y deja el socorro a quien tiene formación.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es la protección del medio ambiente?", "Cuidar el agua, el aire y el suelo evitando derrames, emisiones y residuos mal manejados", "Cuidar solo que los documentos estén ordenados", "Limitar el ingreso de camiones en el recinto", "La protección ambiental se refiere al entorno, no a la documentación ni al tránsito."),
        ("abc", "En Operaciones Portuarias: ¿qué significa proteger, avisar y socorrer?", "No exponerse, llamar a un adulto responsable y a emergencias, y que socorra quien tiene formación", "Prevenir, atender y sanar a cualquier persona presente", "Parar el trabajo, alejar a todos y guardar silencio", "Es el principio básico de primeros auxilios: proteger, avisar y socorrer."),
        ("abc", "En Operaciones Portuarias: ¿quién puede socorrer a una persona herida?", "Una persona con formación en primeros auxilios o el personal de emergencia", "Cualquier persona que esté presente", "Solo quien lleve más tiempo trabajando en el puerto", "El socorro lo hace quien tiene formación."),
        ("=", "{F} ¿Cuántos pesos cuestan los derrames esperados si no se hace nada?", "10*250000", "Se multiplican los derrames esperados por el costo de cada uno.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la alternativa 1, sumando la medida y los derrames que quedan?", "400000+6*250000", "Se suman el costo de la medida y el de los 6 derrames esperados.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la alternativa 2?", "1200000+1*250000", "Se suman el costo de la medida y el del derrame esperado.", " pesos"),
        ("abc", "{F} ¿Qué alternativa conviene por costo total?", "La alternativa 2, porque su costo total es menor", "La alternativa 1, porque la medida cuesta menos", "Ninguna, porque no hacer nada cuesta lo mismo", "El costo total de la alternativa 2 es menor, aunque su medida cueste más."),
        ("=", "{F} ¿Cuántos pesos menos cuesta en total la alternativa 2 que la 1?", "(400000+6*250000)-(1200000+1*250000)", "Se resta el costo total de la alternativa 2 al de la alternativa 1.", " pesos"),
        ("=", "{F} ¿Qué porcentaje de cumplimiento tiene la lista de inspección?", "9*100//10", "Se divide los puntos en orden entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} Con 9 de los 10 puntos en orden, ¿se da por buena la inspección?", "No: bajo cero faltas se corrige el punto pendiente antes de darla por buena", "Sí, porque 90 % es suficiente", "Sí, si el punto pendiente parece poco importante", "Cero faltas exige que todos los puntos estén en orden."),
        ("abc", "{F} ¿Por qué la alternativa 2 es de un nivel más alto en la jerarquía de controles?", "Porque cambia físicamente el lugar y no depende de que las personas recuerden las charlas", "Porque es más cara", "Porque la usan las personas con más experiencia", "La ingeniería actúa sobre el lugar; lo administrativo depende de la conducta."),
        ("=", "{F} Si cada derrame costara $500.000 en lugar de $250.000, ¿cuántos pesos más costaría en total la alternativa 1 que la 2?", "(400000+6*500000)-(1200000+1*500000)", "Se recalculan los costos con el nuevo costo por derrame y se restan.", " pesos"),
        ("abc", "Durante una visita de ejemplo, ves que un envase se rompe y un líquido desconocido se derrama en el suelo cerca de una zanja que da al agua. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo ni entrar al agua, avisar a un adulto responsable y a emergencias", "Acercarte con arena o trapos para contener el líquido", "Echar agua para diluirlo", "Un líquido desconocido puede ser peligroso; se mantiene la distancia y se avisa."),
    ],
    ctx=("abc", "Un compañero dice: «si hay un derrame, lo limpio yo con lo que tenga a mano, así no se entera nadie». ¿Qué respondes?", "Que no, porque se avisa a un adulto responsable y a emergencias y la limpieza la hace personal capacitado", "Que sí, si es poco líquido", "Que sí, pero solo con guantes", "Un derrame desconocido puede ser peligroso y debe informarse."),
    sc=[
        ("En Operaciones Portuarias: ¿cómo se calcula el costo total de una medida?", "Sumando el costo de la medida y el de los derrames que quedan", "Ambos costos forman el costo total."),
        ("¿Qué significa proteger, avisar y socorrer?", "No exponerse, avisar y que socorra quien tiene formación", "Es el principio básico de los primeros auxilios."),
        ("¿Qué exige cero faltas en una inspección?", "Que todos los puntos estén en orden", "Un punto pendiente se corrige antes de aprobar."),
    ],
    op=("Alternativa A (control administrativo, letreros y charlas): cuesta $300.000 y reduce los derrames esperados de 8 a 5 por año. Alternativa B (control de ingeniería, una bandeja de contención fija): cuesta $900.000 y reduce los derrames esperados de 8 a 1 por año. Cada derrame cuesta $200.000 (valor de ejemplo). Escribe (a) el costo esperado de los derrames si no se hace nada, (b) el costo total de A, (c) el costo total de B, (d) qué alternativa conviene y qué hace una persona sin formación ante un derrame.",
        "(a) 8 × 200.000 = $1.600.000. (b) 300.000 + 5 × 200.000 = $1.300.000. (c) 900.000 + 1 × 200.000 = $1.100.000. (d) Conviene B, porque tiene el menor costo total y es de nivel más alto en la jerarquía. La persona sin formación no se acerca a la zona de riesgo, avisa a un adulto responsable y a emergencias.",
        ["calcula el costo sin medidas", "calcula el costo total de A", "calcula el costo total de B", "elige y explica qué hacer ante un derrame"],
        ["hoja con las cuatro respuestas"],
        ["olvidar sumar el costo de la medida", "elegir solo por el costo de la medida", "sugerir acercarse a limpiar el derrame"],
        "Pregunta: «¿qué hace una persona sin formación ante un derrame?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Escribe con tus palabras qué significa proteger, avisar y socorrer y da un ejemplo inventado en un puerto.",
    extend="Explica con un ejemplo por qué una barrera física puede costar más al comienzo y menos en total que unas charlas.",
)
