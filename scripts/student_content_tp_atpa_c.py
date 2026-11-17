"""Atención de Párvulos TP 3.º y 4.º medio: OAE-06 (hábitos de salud, higiene y autocuidado; manual de salud y evacuación), OAE-07 (controlar peso y talla informando a la educadora) y OAE-08 (observar síntomas y señales, accidentes menores, indicaciones de medicamentos y maltrato: solo conceptos, registro y aviso inmediato). Todo en papel: jardines, niños, niñas y familias inventados y rotulados «de ejemplo»."""
from __future__ import annotations

from tp_atpa_common import LIM, build

O6 = "TP-ATPA-3y4-OAE-06"
O7 = "TP-ATPA-3y4-OAE-07"
O8 = "TP-ATPA-3y4-OAE-08"

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (hábitos y seguridad, de ejemplo). Hábitos del jardín: lavarse las manos con agua y jabón antes de comer y después de ir al baño; cepillarse los dientes después del almuerzo con ayuda de un adulto; ventilar la sala; toser o estornudar en el pliegue del codo. "
     "Documentos: manual de salud y plan de prevención de riesgos y evacuación. Regla de ejemplo: en un simulacro o una evacuación se siguen las indicaciones de la educadora y se lleva la lista de asistencia a la zona de seguridad.")
build(
    O6, 1, F,
    use="Aprenderé qué son los hábitos de salud, la higiene y el autocuidado en niños y niñas menores de seis años y qué papel tienen el manual de salud y el plan de evacuación.",
    prior=["Conozco el rol de la técnica y de la educadora.", "Sé que los datos de los niños son confidenciales.", "Sé contar y dividir."],
    explain=[
        "En Atención de Párvulos, promover hábitos de salud es enseñar con el ejemplo y la repetición cosas que cuidan el cuerpo: lavarse las manos, cepillarse los dientes con ayuda, toser en el pliegue del codo y ventilar la sala. La higiene es la limpieza que previene enfermedades. El autocuidado es aprender a cuidar el propio cuerpo y a pedir ayuda a un adulto cuando algo molesta o no se siente bien.",
        "Las técnicas que usa el jardín están escritas en el manual de salud, y las reglas de seguridad en el plan de prevención de riesgos y evacuación. La evacuación es salir de forma ordenada hacia una zona de seguridad cuando hay una emergencia. Los simulacros son prácticas para ensayarla. Allí se siguen las instrucciones de la educadora, se mantiene la calma y se lleva la lista de asistencia.",
        "Los hábitos se aprenden jugando, con cantos y con paciencia, sin amenazas ni castigos. El adulto da el ejemplo." + LIM,
    ],
    vocab=[("hábito", "costumbre que se aprende repitiendo, como lavarse las manos"), ("higiene", "limpieza que previene enfermedades"), ("autocuidado", "cuidar el propio cuerpo y pedir ayuda a un adulto cuando hace falta"), ("manual de salud", "documento del jardín con las técnicas de salud e higiene"), ("evacuación", "salida ordenada hacia la zona de seguridad en una emergencia"), ("simulacro", "práctica de una evacuación para ensayarla")],
    worked=[
        ("Calcular un tiempo de lavado", "En otra sala de ejemplo, 12 niños se lavan las manos en grupos de 4, y cada grupo tarda 30 segundos. ¿Cuántos segundos tarda toda la sala?", ["Hay 12 ÷ 4 = 3 grupos.", "3 × 30 = 90."], "90 segundos"),
        ("Dar el ejemplo", "Un niño de ejemplo estornuda en el aire. ¿Cómo lo refuerza la técnica?", ["Le muestra la forma correcta con su propio cuerpo.", "Le recuerda estornudar en el pliegue del codo."], "Mostrando y recordando el estornudo en el codo"),
    ],
    mistakes=[("Decir «si no te lavas las manos, no juegas» como amenaza.", "El hábito se asocia al miedo y no al cuidado.", "Haz del lavado un momento agradable, con juego y con tu ejemplo."),
              ("Regresar por un objeto olvidado durante una evacuación.", "Pone en riesgo a la técnica y retrasa al grupo.", "Sigue con el grupo y avisa a la educadora.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué es el autocuidado en un niño pequeño?", "Aprender a cuidar su cuerpo y a pedir ayuda a un adulto cuando lo necesita", "Cuidarse solo sin ningún adulto cerca", "Usar solo productos de limpieza", "El autocuidado incluye pedir ayuda; no significa estar solo."),
        ("abc", "{F} ¿Cuándo se lavan las manos, según la ficha?", "Antes de comer y después de ir al baño", "Solo al llegar al jardín", "Solo después de jugar", "La ficha fija esas dos ocasiones."),
        ("abc", "{F} ¿Cómo se debe toser o estornudar?", "En el pliegue del codo", "Directo hacia los demás", "Con la mano abierta", "El pliegue del codo evita esparcir gérmenes con las manos."),
        ("abc", "{F} ¿Qué documento reúne las técnicas de salud e higiene del jardín?", "El manual de salud", "La minuta de comidas", "El inventario de juguetes", "Las técnicas están en el manual de salud."),
        ("abc", "{F} ¿Qué lleva el adulto responsable a la zona de seguridad en una evacuación?", "La lista de asistencia", "Los juguetes de la sala", "La minuta", "La lista permite comprobar que están todos los niños."),
        ("=", "{F} Los 18 niños se lavan las manos en grupos de 3 y cada grupo tarda 40 segundos. ¿Cuántos segundos tarda toda la sala?", "18//3*40", "Se calculan los grupos y se multiplican por el tiempo de cada uno.", " segundos"),
        ("abc", "{F} Un niño estornuda en su mano y luego toca los juguetes. ¿Qué hace la técnica?", "Le recuerda estornudar en el codo y lavarse las manos", "Le pide que no estornude más", "No hace nada, porque es normal", "Se refuerza el hábito con calma y se evita esparcir gérmenes."),
        ("abc", "{F} La sala lleva toda la mañana cerrada con 16 niños. ¿Qué hábito corresponde?", "Ventilar la sala según la indicación de la educadora", "Cerrar también las cortinas", "Subir la calefacción", "Ventilar renueva el aire y es uno de los hábitos de la ficha."),
        ("=", "{F} Para el cepillado hay 18 niños. Cada uno tiene un cepillo rotulado y se agregan 2 de repuesto. ¿Cuántos cepillos hay?", "18+2", "Se suman los repuestos a un cepillo por niño.", " cepillos"),
        ("abc", "Un niño no quiere lavarse las manos. ¿Cómo promueve el hábito la técnica?", "Lo invita a hacerlo juntos, con un canto, y le explica para qué sirve", "Le dice que se quedará sin juego", "Se lo hace a la fuerza", "El hábito se aprende con ejemplo y juego, no con amenazas."),
        ("abc", "{F} En un simulacro, un niño pide volver por su peluche. ¿Qué hace la técnica?", "Lo calma, le explica que siguen con el grupo y avisa a la educadora", "Lo lleva de vuelta a buscarlo", "Lo deja que vuelva solo", "En una evacuación no se regresa; se sigue con el grupo."),
        ("=", "{F} Hay 18 matriculados y hoy faltan 2. ¿Cuántos niños deben contarse en la zona de seguridad?", "18-2", "A los matriculados se les restan los ausentes.", " niños"),
        ("abc", "{F} En la zona de seguridad la técnica cuenta 15 niños, pero la lista dice 16 presentes. ¿Qué hace?", "Avisa de inmediato a la educadora y no va a buscar sola", "Entra a la sala a buscarlo", "Espera a ver si aparece", "Se avisa enseguida; no se regresa sin indicación."),
    ],
    ctx=("abc", "{F} Una familia pide por la libreta que su hijo no se cepille los dientes en el jardín porque «lo hace en casa». ¿Qué hace la técnica?", "Informa a la educadora, que conversará con la familia sobre el manual de salud", "Le dice que no se cepillará más", "Se lo cepilla igual sin avisar", "Los acuerdos con las familias los conduce la educadora y se basan en el manual."),
    sc=[
        ("En Atención de Párvulos: ¿cuándo se lavan las manos antes de comer?", "Siempre, con agua y jabón", "Así se previenen enfermedades antes de comer."),
        ("¿Qué haces si falta un niño en la zona de seguridad?", "Aviso de inmediato a la educadora", "No se vuelve a buscar por cuenta propia."),
        ("¿Cómo se enseña un hábito?", "Con ejemplo, juego y paciencia", "Las amenazas no enseñan hábitos duraderos."),
    ],
    op=("Caso de ejemplo. En una sala de nivel medio de 15 niños y niñas, antes del almuerzo se lavan las manos de a 3. Un niño dice que no quiere porque «el agua está fría». Hoy hay un simulacro de evacuación a las 11:00. "
        "Escribe: cuántos grupos de lavado se forman; qué le dirías al niño; qué documentos te guían; y qué harías en el simulacro si un niño llora.",
        "Se forman 15 ÷ 3 = 5 grupos. Al niño: «Entiendo que el agua está fría; la templamos un poco si la educadora lo permite y lo hacemos juntos». Me guían el manual de salud y el plan de prevención de riesgos y evacuación. En el simulacro: lo tomo de la mano, lo calmo y sigo con el grupo según la educadora, llevando la lista de asistencia.",
        ["calcula los grupos", "usa un lenguaje de buen trato", "nombra los documentos y la conducta ante un simulacro"],
        ["hoja con cuatro respuestas breves"],
        ["amenazar al niño", "no nombrar los documentos", "romper el orden de evacuación"],
        "Pregunta: «¿qué harías si el niño no quiere salir del simulacro?». Debe calmarlo y avisar a la educadora."),
    reinforce="Escribe tres hábitos de salud que enseñarías a niños de 4 años y cómo los harías agradables.",
    extend="Explica por qué practicar un simulacro ayuda a que los niños se sientan seguros en una emergencia real.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (plan de evacuación en palabras, de ejemplo). De la sala del nivel medio se sale al pasillo y luego por la salida norte hasta la zona de seguridad del patio. Una flecha verde en la pared marca la vía de evacuación. "
     "La lista de asistencia del grupo tiene 20 niños y niñas inscritos. El simulacro se hace el primer jueves de cada mes. Las vías de evacuación nunca se bloquean con muebles ni materiales.")
build(
    O6, 2, F,
    use="Aprenderé el vocabulario del autocuidado y de la evacuación: vías, zonas de seguridad, señalética, lista de asistencia y calendario de hábitos.",
    prior=["Conozco los hábitos de salud.", "Sé leer un plano en palabras.", "Sé contar y restar."],
    explain=[
        "El plan de prevención de riesgos y evacuación dice cómo salir de forma segura. La vía de evacuación es el camino marcado para salir. La zona de seguridad es el lugar abierto donde se reúne el grupo. La señalética son las señales, como una flecha verde, que indican el camino. Las vías nunca se bloquean con muebles ni materiales, y se revisan que estén despejadas.",
        "Antes de salir, la educadora o la técnica toma la lista de asistencia; al llegar a la zona de seguridad cuenta a los niños y la compara con la lista. Si falta alguien, avisa de inmediato a la persona responsable de la evacuación, que actúa según el protocolo. Los simulacros se hacen en fechas conocidas para ensayar la salida sin asustar.",
        "El autocuidado también se enseña con rutinas: un calendario de hábitos con dibujos ayuda a que los niños recuerden qué hacer cada día, como lavarse las manos o ventilar." + LIM,
    ],
    vocab=[("vía de evacuación", "camino marcado para salir del edificio"), ("zona de seguridad", "lugar abierto donde se reúne el grupo"), ("señalética", "señales o dibujos que indican un camino o una advertencia"), ("lista de asistencia", "lista de los niños presentes"), ("despejada", "libre de obstáculos"), ("calendario de hábitos", "cartel con dibujos de las rutinas de higiene")],
    worked=[
        ("Contar para comprobar", "Una lista de ejemplo tiene 14 presentes y en la zona de seguridad se cuentan 14. ¿Qué se concluye?", ["Los números coinciden.", "Están todos los niños."], "Están todos"),
        ("Revisar una vía", "La técnica ve una caja de juguetes en la vía de evacuación. ¿Qué hace?", ["Una vía bloqueada es un riesgo.", "La despeja y avisa a la educadora."], "Despejar la vía y avisar a la educadora"),
    ],
    mistakes=[("Guardar los cojines grandes en el pasillo de evacuación «mientras no se usan».", "Si hay una emergencia, el pasillo está bloqueado.", "Guarda el material en su lugar y deja la vía despejada."),
              ("Contar a los niños de memoria en la zona de seguridad sin mirar la lista.", "Se puede olvidar a alguien.", "Compara el conteo con la lista de asistencia.")],
    T=[
        ("abc", "{F} ¿Cómo se llama el lugar abierto donde se reúne el grupo en una evacuación?", "Zona de seguridad", "Vía de evacuación", "Señalética", "La zona de seguridad es el lugar de reunión; la vía es el camino."),
        ("abc", "{F} ¿Qué marca la flecha verde en la pared?", "La vía de evacuación", "El lugar de los juguetes", "El baño", "La ficha indica que la flecha verde marca la vía."),
        ("abc", "En Atención de Párvulos: ¿qué es la señalética?", "Señales o dibujos que indican un camino o una advertencia", "La lista de asistencia", "El calendario de hábitos", "La señalética guía a las personas con símbolos."),
        ("=", "{F} Hoy faltan 3 niños. ¿Cuántos deben contarse en la zona de seguridad?", "20-3", "A los inscritos se les restan los ausentes.", " niños"),
        ("abc", "{F} ¿Con qué se compara el conteo en la zona de seguridad?", "Con la lista de asistencia", "Con la minuta", "Con el inventario", "La lista de asistencia muestra quiénes están presentes."),
        ("abc", "{F} La técnica ve una caja de juguetes en el pasillo de evacuación. ¿Qué hace?", "La retira y avisa a la educadora", "La deja porque es pequeña", "Pide a un niño que la cuide", "Las vías deben estar siempre despejadas."),
        ("abc", "{F} El simulacro se hace el primer jueves de cada mes y el año escolar de ejemplo tiene 10 meses de clases. ¿Cuántos simulacros se hacen en el año escolar?", "10", "12", "9", "Se hace uno por cada mes de clases; el año escolar de ejemplo tiene 10 meses."),
        ("abc", "{F} Un niño pregunta por qué practican salir. ¿Qué responde la técnica?", "Que practicar ayuda a salir con calma si hubiera una emergencia", "Que es un juego sin importancia", "Que algo malo va a pasar hoy", "Se explica con calma y sin asustar."),
        ("abc", "{F} En la zona de seguridad cuentan 16 niños, pero hoy hay 18 presentes. ¿Qué hace la técnica?", "Avisa de inmediato a la persona responsable y no va a buscar por su cuenta", "Vuelve a la sala a buscarlos", "Espera 10 minutos", "Faltan niños: se avisa enseguida y se sigue el protocolo."),
        ("=", "{F} Hay 18 presentes y en la zona de seguridad se cuentan 16. ¿Cuántos niños faltan por ubicar?", "18-16", "Se restan los contados a los presentes.", " niños"),
        ("abc", "{F} Un calendario de hábitos muestra el dibujo de un cepillo de dientes después del almuerzo. ¿Para qué sirve?", "Para recordar visualmente la rutina", "Para anotar el peso", "Para marcar la asistencia", "Los dibujos ayudan a que los niños recuerden las rutinas."),
        ("abc", "{F} La educadora no está y el simulacro comienza. ¿Qué hace la técnica?", "Sigue las indicaciones del plan y de la persona responsable de la evacuación", "Espera a que vuelva la educadora", "Cancela el simulacro", "El plan indica quién conduce; se sigue la instrucción."),
        ("abc", "{F} La técnica cuenta a los niños, pero hay dos mesas con niños de otro grupo en la sala. ¿Qué hace?", "Cuenta solo a su grupo e informa a la persona responsable del otro", "Los cuenta a todos como suyos", "No cuenta a nadie", "Cada responsable cuenta a su grupo."),
    ],
    ctx=("abc", "{F} Durante un simulacro, un niño con silla de ruedas está en la sala. La vía tiene un escalón. ¿Qué hace la técnica?", "Sigue el plan indicado por la educadora, que prevé cómo evacuar a cada niño, y le explica con calma", "Lo deja en la sala hasta que termine", "Lo carga sin avisar", "El plan debe prever la evacuación de todos los niños; la técnica sigue las indicaciones."),
    sc=[
        ("En Atención de Párvulos: ¿qué es la zona de seguridad?", "El lugar abierto donde se reúne el grupo", "Allí se cuenta a los niños."),
        ("¿Se pueden guardar cosas en la vía de evacuación?", "No", "Debe estar libre para salir rápido."),
        ("¿Qué haces si el conteo no coincide con la lista?", "Aviso de inmediato a la persona responsable", "No se actúa por cuenta propia."),
    ],
    op=("Plan de ejemplo: la sala de transición (22 niños inscritos) sale al pasillo y por la salida este hasta el patio. Hoy hay 3 ausentes. En el simulacro se cuentan 18 niños en la zona de seguridad. Además, en la vía hay una caja de cartón. "
        "Escribe: cuántos niños deben contarse; cuántos faltan por ubicar; qué harías con la caja; y qué le dirías a la persona responsable.",
        "Deben contarse 22 − 3 = 19 niños; faltan por ubicar 19 − 18 = 1. La caja se retira de la vía y se avisa a la educadora. A la persona responsable: «Contamos 18 y deberían ser 19; falta un niño».",
        ["calcula los presentes y los que faltan", "retira el obstáculo y avisa", "informa con claridad y no sale a buscar"],
        ["hoja con dos cuentas y dos acciones"],
        ["buscar sola al niño", "dejar la caja", "no informar a la persona responsable"],
        "Pregunta: «¿qué harías si el niño que falta está llorando en la sala?». Debe avisar y esperar indicaciones del responsable."),
    reinforce="Dibuja o describe una vía de evacuación de tu casa de ejemplo con una flecha y una zona de seguridad.",
    extend="Explica por qué las vías de evacuación nunca se bloquean, aunque sea un material pequeño.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (caso de ejemplo). Sala de nivel medio con 16 niños y niñas. Hay un solo lavamanos para todo el grupo y una sola toalla de tela que se comparte. El jabón está en un estante alto. El almuerzo es a las 12:00 y cada niño se lava las manos de uno en uno, 1 minuto cada uno. "
     "La sala no se ha ventilado en toda la mañana. Jabón en dispensador sin llave y toallas de papel individuales están disponibles en la bodega.")
build(
    O6, 3, F,
    use="Aprenderé a analizar un caso de rutinas de higiene: detectar riesgos, proponer mejoras simples y avisar a la educadora.",
    prior=["Conozco los hábitos de higiene.", "Sé calcular tiempos.", "Sé que la educadora decide los cambios de rutina."],
    explain=[
        "Para analizar una rutina de higiene se observa qué se hace, cuánto tiempo toma y qué riesgos aparecen. Una toalla compartida pasa gérmenes de un niño a otro. Un jabón fuera del alcance de los niños los hace depender del adulto para lavarse. Una sala sin ventilar acumula aire usado. Estos son hechos que la técnica puede observar y registrar.",
        "Con los hechos se proponen mejoras simples: usar toallas de papel individuales, dejar el jabón al alcance de los niños en un dispensador, organizar el lavado en grupos pequeños y ventilar a horas fijas. La técnica propone, pero la educadora decide qué cambiar. Un buen análisis incluye también cuánto tiempo falta para el siguiente evento, como el almuerzo.",
        "Cada niño aprende por imitación, así que la técnica lava sus manos junto con ellos y sigue el mismo protocolo." + LIM,
    ],
    vocab=[("riesgo", "algo que puede causar daño o enfermedad"), ("mejora", "cambio simple que corrige un riesgo"), ("dispensador", "recipiente que entrega jabón sin tocarlo con las manos sucias"), ("toalla individual", "toalla de uso de una sola persona, como una toalla de papel"), ("ventilación", "renovación del aire de la sala")],
    worked=[
        ("Tiempo de lavado", "En otra sala de ejemplo, 10 niños se lavan de a uno y cada uno tarda 1 minuto. ¿Cuánto tarda la sala?", ["10 niños por 1 minuto cada uno.", "10 × 1 = 10."], "10 minutos"),
        ("Detectar un riesgo", "En una sala de ejemplo hay una taza de uso común para todos los niños. ¿Qué riesgo hay?", ["Compartir un vaso pasa gérmenes.", "Cada niño debe tener el suyo."], "Compartir el vaso pasa gérmenes de un niño a otro"),
    ],
    mistakes=[("Secar las manos de todos los niños con la misma toalla.", "La toalla compartida pasa gérmenes.", "Usa toallas de papel individuales o una toalla por niño."),
              ("Cambiar la rutina por su cuenta sin avisar.", "La educadora responde por las rutinas de la sala.", "Propón las mejoras y espera su decisión.")],
    T=[
        ("=", "{F} ¿Cuántos minutos tardan los 16 niños en lavarse de uno en uno?", "16*1", "Se multiplican los niños por el minuto de cada uno.", " minutos"),
        ("abc", "{F} ¿Qué riesgo de higiene hay en la rutina?", "La toalla de tela compartida por todos", "Que el almuerzo sea a las 12:00", "Que haya 16 niños", "La toalla compartida pasa gérmenes entre los niños."),
        ("abc", "{F} ¿Por qué el jabón en un estante alto es un problema?", "Porque los niños no pueden alcanzarlo y dependen de un adulto", "Porque ocupa mucho espacio", "Porque se gasta menos", "Dejarlo al alcance favorece la autonomía en el lavado."),
        ("abc", "{F} ¿Qué mejora corrige la toalla compartida?", "Usar toallas de papel individuales", "Usar dos toallas de tela para todos", "Dejar que se sequen con la ropa", "Una toalla individual evita el contacto entre niños."),
        ("abc", "{F} ¿Qué hace la técnica con la propuesta de usar el dispensador de jabón?", "La presenta a la educadora, que decide", "La aplica sola sin avisar", "No hace nada porque no es su tarea", "La técnica propone y la educadora decide."),
        ("abc", "{F} El lavado de los 16 niños, de uno en uno, debe terminar a las 12:00. ¿A qué hora debe comenzar como máximo?", "A las 11:44", "A las 11:46", "A las 12:16", "16 niños por 1 minuto son 16 minutos; antes de las 12:00 eso es las 11:44."),
        ("=", "{F} Si se lavan de a 4 niños a la vez (con más lavamanos) y cada grupo tarda 1 minuto, ¿cuántos minutos tardan los 16 niños?", "16//4*1", "Se calculan los grupos y se multiplican por el minuto de cada uno.", " minutos"),
        ("abc", "{F} La sala no se ha ventilado en toda la mañana. ¿Qué propone la técnica?", "Ventilar la sala a horas fijas, con aviso a la educadora", "Cerrar las ventanas para no enfriar", "Perfumar la sala", "La ventilación renueva el aire y se organiza con la educadora."),
        ("abc", "{F} Un niño se seca las manos con su ropa porque la toalla está mojada. ¿Qué hace la técnica?", "Le ofrece una toalla de papel y propone el cambio a la educadora", "Lo regaña por mojar la ropa", "Lo deja secarse con la toalla de todos", "Se ofrece una alternativa higiénica y se propone la mejora."),
        ("abc", "{F} ¿Qué falla si la técnica se lava las manos más rápido que los niños y sin jabón?", "No da el ejemplo del hábito", "Nada, los niños no la observan", "Que debería usar guantes siempre", "Los niños aprenden por imitación, por eso el adulto da el ejemplo."),
        ("=", "{F} Con 3 lavamanos, se lavan 3 niños a la vez y cada tanda tarda 1 minuto. ¿Cuántas tandas se necesitan para los 16 niños?", "(16+2)//3", "Se divide en tandas de 3 y se redondea hacia arriba porque el niño sobrante también se lava.", " tandas"),
        ("abc", "{F} El jabón del dispensador se acabó a las 11:55. ¿Qué hace la técnica?", "Avisa a la educadora y usa jabón de la bodega según la indicación", "Lava las manos solo con agua", "Cancela el lavado de manos", "El lavado con jabón es necesario; se repone con aviso."),
        ("abc", "{F} Un niño pregunta por qué usan toallas de papel ahora. ¿Qué responde la técnica?", "Que cada uno tiene la suya para no pasar los gérmenes a los demás", "Que se acabaron las toallas de tela", "Que es un castigo", "Se explica con palabras simples el porqué del cambio."),
    ],
    ctx=("abc", "{F} A las 11:50 la técnica nota que el lavado de manos con una sola fila no alcanzará a terminar antes del almuerzo. ¿Qué hace?", "Avisa a la educadora y propone lavar en grupos pequeños", "Salta el lavado de algunos niños", "Hace que los niños se laven más rápido sin jabón", "El lavado no se omite; se propone una forma más rápida."),
    sc=[
        ("En Atención de Párvulos: ¿qué riesgo tiene una toalla compartida?", "Pasa gérmenes entre los niños", "Todos usan la misma toalla y se contagian."),
        ("¿Quién decide cambiar una rutina de la sala?", "La educadora", "La técnica propone, la educadora decide."),
        ("¿Cómo aprenden los niños los hábitos?", "Imitando y repitiendo con el ejemplo del adulto", "Los niños pequeños aprenden mirando lo que hacen los adultos."),
    ],
    op=("Caso de ejemplo. En una sala de 14 niños y niñas hay un lavamanos, una toalla de tela común y el jabón está en un estante alto. Cada niño se lava solo y tarda 1 minuto. El almuerzo es a las 12:00. "
        "Escribe: cuántos minutos tarda el lavado completo; dos riesgos que ves; dos mejoras simples; y a quién se las propones.",
        "El lavado tarda 14 minutos. Riesgos: la toalla común pasa gérmenes y el jabón fuera del alcance. Mejoras: toallas de papel individuales y jabón en un dispensador a la altura de los niños. Se las propongo a la educadora.",
        ["calcula el tiempo", "identifica dos riesgos con hechos", "propone mejoras simples a la educadora"],
        ["hoja con cálculo, dos riesgos y dos mejoras"],
        ["cambiar la rutina sola", "proponer mejoras que no corrigen el riesgo", "no calcular el tiempo"],
        "Pregunta: «¿qué harías si la educadora no puede cambiar nada hoy?». Debe respetarlo y mantener las medidas de higiene posibles."),
    reinforce="Escribe tres riesgos de higiene de una sala de ejemplo y una mejora simple para cada uno.",
    extend="Explica por qué dejar el jabón al alcance de los niños favorece su autonomía.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (simulacro de ejemplo). Nivel de transición con 22 niños y niñas inscritos; hoy hay 3 ausentes. La meta del jardín para este simulacro es salir en 3 minutos (180 segundos) hasta la zona de seguridad (meta de ejemplo). "
     "Resultados del simulacro de hoy: tardó 4 minutos y 30 segundos; en la zona de seguridad se contaron 18 niños. Hay una vía de evacuación bloqueada por una caja que fue retirada durante el simulacro. Los tiempos y las cifras son de ejemplo.")
build(
    O6, 4, F,
    use="Aprenderé a aplicar un criterio con datos en un simulacro: contar, comparar con la meta, detectar fallas y avisar a la educadora.",
    prior=["Conozco el plan de evacuación y la lista de asistencia.", "Sé convertir minutos a segundos.", "Sé restar."],
    explain=[
        "Un simulacro se evalúa con datos. Primero se cuenta cuántos niños deben estar (inscritos menos ausentes) y cuántos se cuentan en la zona de seguridad: si no coinciden, hay un niño por ubicar y se avisa de inmediato a la persona responsable. Luego se compara el tiempo que tardó el grupo con la meta del jardín. Si tardó más, se buscan las causas, por ejemplo una vía bloqueada.",
        "Para comparar se pasan los minutos a segundos (1 minuto son 60 segundos) y se restan. Con la diferencia se informa a la educadora lo ocurrido y qué se podría mejorar, como despejar las vías antes de cada jornada. En el informe se usan hechos y cifras, sin culpar a ninguna persona.",
        "En una evacuación real, la técnica sigue las indicaciones de la educadora y del plan; este cuaderno solo ensaya el análisis en papel." + LIM,
    ],
    vocab=[("meta", "tiempo o resultado que el jardín se propone alcanzar"), ("diferencia", "resultado de restar dos cantidades"), ("causa", "razón que explica por qué ocurrió un resultado"), ("informe de simulacro", "documento breve con tiempo, conteo, fallas y mejoras"), ("despejar", "retirar lo que estorba")],
    worked=[
        ("Pasar a segundos", "Un simulacro de ejemplo tardó 2 minutos y 15 segundos. ¿Cuántos segundos son?", ["2 minutos son 120 segundos.", "120 + 15 = 135."], "135 segundos"),
        ("Comparar con la meta", "La meta de ejemplo es 200 segundos y el grupo tardó 245. ¿Cuántos segundos más?", ["Se resta la meta al tiempo real.", "245 − 200 = 45."], "45 segundos más")
    ],
    mistakes=[("Decir «fue un desastre por culpa de los niños».", "Culpar no ayuda y los niños no son responsables del plan.", "Describe los hechos y propone mejoras al plan."),
              ("Informar «se tardó más» sin decir cuánto ni por qué.", "Sin cifras y causas no se puede mejorar.", "Informa el tiempo, la diferencia con la meta y la causa observada.")],
    T=[
        ("=", "{F} ¿Cuántos niños deben contarse en la zona de seguridad?", "22-3", "A los inscritos se les restan los ausentes.", " niños"),
        ("=", "{F} ¿Cuántos segundos tardó el simulacro?", "4*60+30", "Se convierten los minutos a segundos y se suman los 30 segundos.", " segundos"),
        ("=", "{F} ¿Cuántos segundos más que la meta tardó el simulacro?", "(4*60+30)-180", "Se resta la meta al tiempo del simulacro.", " segundos"),
        ("=", "{F} ¿Cuántos niños faltan por ubicar en la zona de seguridad?", "22-3-18", "Se restan ausentes y contados a los inscritos.", " niño"),
        ("abc", "{F} Faltan niños por ubicar. ¿Qué hace la técnica?", "Avisa de inmediato a la persona responsable y no va sola a buscarlos", "Entra a la sala a buscarlos", "Espera a que aparezcan", "Se avisa enseguida para que se actúe con el protocolo."),
        ("abc", "{F} ¿Qué causa pudo retrasar el simulacro?", "La caja que bloqueaba una vía", "El número de niños inscritos", "La flecha verde de la pared", "Una vía bloqueada hace que el grupo se demore al salir."),
        ("abc", "{F} ¿Qué mejora propone la técnica a la educadora?", "Revisar y despejar las vías antes de cada jornada", "Suspender los simulacros", "Pedir que los niños corran", "Despejar evita que el problema se repita."),
        ("=", "{F} Si la meta fuera 4 minutos, ¿cuántos segundos de diferencia habría con los 270 segundos del simulacro?", "270-4*60", "Se restan los segundos de la meta al tiempo real.", " segundos"),
        ("abc", "{F} Otra técnica dice que el simulacro salió mal porque «los niños no obedecen». ¿Qué observación corresponde?", "Describir los hechos y las causas del plan sin culpar a los niños", "Es verdad: los niños deben obedecer", "Agregar un castigo", "El análisis se basa en hechos y causas, no en culpas."),
        ("abc", "{F} ¿Qué datos incluye un informe de simulacro?", "Tiempo, conteo, fallas y mejoras", "Solo la opinión de la técnica", "Los nombres de los niños que lloraron", "El informe usa cifras y hechos, no etiquetas."),
        ("=", "{F} En el simulacro anterior el grupo tardó 40 segundos menos que hoy. ¿Cuántos segundos tardó antes?", "(4*60+30)-40", "Se restan los 40 segundos al tiempo de hoy.", " segundos"),
        ("abc", "{F} Un niño se asustó con el sonido del simulacro y lloró. ¿Qué hace la técnica?", "Lo acompaña, le explica con calma y lo informa a la educadora", "Lo reta por llorar", "Lo deja solo para que se calme", "Se acompaña con calma y se informa."),
        ("abc", "{F} Un informe de simulacro dice solo «salimos rápido». ¿Qué falla?", "No trae tiempo, conteo ni causas, así que no permite mejorar", "Nada, es un informe breve", "Que debería traer los nombres de los niños que lloraron", "Un informe útil lleva cifras y hechos; una frase vaga no sirve."),
    ],
    ctx=("abc", "{F} Al terminar el simulacro, un padre pregunta a la técnica cuánto tardaron y si «todo salió bien». ¿Qué responde?", "Que la educadora puede informarle del resultado y de las mejoras que se harán", "Le da los tiempos y critica a otra técnica", "Le dice que no pasó nada", "Los resultados oficiales los comunica la educadora o la dirección."),
    sc=[
        ("En Atención de Párvulos: ¿cuántos segundos tiene 1 minuto?", "60", "Se usa para pasar los tiempos del simulacro a segundos."),
        ("¿Qué haces si faltan niños en la zona de seguridad?", "Aviso de inmediato a la persona responsable", "No se va a buscar sola."),
        ("¿Cómo se informa un simulacro?", "Con tiempo, conteo, fallas y mejoras", "Así se pueden tomar decisiones a partir de datos reales."),
    ],
    op=("Datos de ejemplo: nivel medio con 20 niños y niñas inscritos y 2 ausentes. La meta del jardín es 150 segundos (de ejemplo). El simulacro tardó 3 minutos y 5 segundos y en la zona de seguridad se contaron 18 niños. Una puerta estaba cerrada con llave. "
        "Escribe: cuántos deben contarse; cuántos faltan por ubicar; cuántos segundos tardó y qué diferencia hay con la meta; qué causa observas y qué mejora propones.",
        "Deben contarse 18 y se contaron 18: no faltan. Tardó 185 segundos; la diferencia con la meta es 35 segundos. Causa: la puerta cerrada con llave. Mejora: dejar las puertas de evacuación sin llave durante la jornada y avisarlo a la educadora.",
        ["calcula presentes, tiempo y diferencia", "identifica la causa con hechos", "propone una mejora y avisa"],
        ["hoja con tres cálculos y una mejora"],
        ["no pasar los minutos a segundos", "culpar a los niños", "no proponer mejora"],
        "Pregunta: «¿qué harías si en el conteo faltara un niño?». Debe avisar de inmediato a la persona responsable."),
    reinforce="Convierte tres tiempos de simulacro de ejemplo a segundos y compáralos con una meta de 180 segundos.",
    extend="Explica por qué en un informe de simulacro se usan hechos y cifras y no culpas.",
)

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (control de ejemplo). El jardín mide el peso en gramos y la talla en centímetros una vez al mes (frecuencia de ejemplo), con la balanza y el tallímetro del jardín y con la educadora presente. Los valores se anotan con la fecha en la ficha del niño. "
     "La técnica mide según el manual de salud y entrega los valores a la educadora, que los interpreta y decide si hace falta alguna acción. Se mide en un lugar reservado, con respeto y sin comentarios sobre el cuerpo.")
build(
    O7, 1, F,
    use="Aprenderé por qué se controlan el peso y la talla, quién mide y quién interpreta, y cómo se cuida la privacidad y el respeto de cada niño.",
    prior=["Conozco el rol de la técnica y de la educadora.", "Sé que los datos de los niños son confidenciales.", "Sé multiplicar y restar."],
    explain=[
        "En Atención de Párvulos, controlar el peso y la talla es medir cuánto pesa y cuánto mide un niño o una niña, siguiendo el manual de salud del jardín. Se anota con la fecha para poder comparar con controles anteriores. Estas mediciones ayudan al equipo de salud y a la educadora a saber cómo va su crecimiento, pero no son un diagnóstico.",
        "La técnica mide y registra los valores con exactitud. No interpreta si son normales o no, porque eso lo hace la educadora con el apoyo del equipo de salud. Si hay una duda, la técnica informa los números a la educadora. Los resultados son datos personales: se anotan en la ficha, no se leen en voz alta, no se comparan entre niños y no se comentan con otras familias.",
        "El respeto también cuenta: se mide en un lugar reservado, se explica al niño lo que se hará y nunca se hacen comentarios sobre su cuerpo, como «está gordito» o «está flaquito»." + LIM,
    ],
    vocab=[("peso", "cuánto pesa un niño; en el jardín se anota en gramos"), ("talla", "cuánto mide un niño; en el jardín se anota en centímetros"), ("manual de salud", "documento del jardín con las técnicas de control"), ("control", "medición hecha en una fecha para comparar con otras"), ("interpretar", "decir si un valor es normal o no; lo hace la educadora con el equipo de salud")],
    worked=[
        ("Quién interpreta", "Un niño de ejemplo pesó 100 gramos menos que el control anterior. ¿Quién decide qué significa?", ["La técnica registra el valor.", "La educadora lo interpreta con apoyo del equipo de salud."], "La educadora"),
        ("Calcular tiempo", "Si se miden 12 niños y cada uno tarda 4 minutos, ¿cuántos minutos se necesitan?", ["12 niños por 4 minutos cada uno.", "12 × 4 = 48."], "48 minutos"),
    ],
    mistakes=[("Decir en voz alta «tienes 14 kilos, estás pesado».", "Expone al niño, hace un juicio sobre su cuerpo y publica un dato personal.", "Anota el valor en la ficha y no lo comentes."),
              ("Decirle a la madre «su hijo está muy delgado».", "La técnica no interpreta y puede preocupar sin fundamento.", "Ofrece que la educadora converse con ella sobre los controles.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué es la talla de un niño?", "Cuánto mide, que se anota en centímetros", "Cuánto pesa, en gramos", "Cuántos años tiene", "La talla es la medida de la estatura."),
        ("abc", "{F} ¿En qué unidad se anota el peso en el jardín?", "En gramos", "En centímetros", "En litros", "La ficha dice que el peso se anota en gramos."),
        ("abc", "{F} ¿Quién interpreta los valores?", "La educadora, con apoyo del equipo de salud", "La técnica", "Otra familia", "La técnica mide; la educadora interpreta."),
        ("abc", "{F} ¿Dónde se anotan los valores?", "En la ficha del niño, con la fecha", "En un papel suelto en la sala", "En el panel de todas las familias", "Los datos personales van en la ficha."),
        ("abc", "{F} Una técnica comenta en voz alta: «qué pesado estás». ¿Qué falla?", "Hace un comentario sobre el cuerpo y expone un dato personal", "Nada: es una observación amistosa", "Que no usó el nombre del niño", "Los comentarios sobre el cuerpo no respetan al niño."),
        ("abc", "¿Por qué se compara el valor de hoy con los controles anteriores?", "Porque la fecha y la secuencia muestran cómo cambia la medida", "Porque así se decide quién es el más pequeño", "Porque cada niño debe parecerse al promedio", "Comparar con controles anteriores muestra la evolución de cada niño; no se compara entre niños."),
        ("=", "{F} Si se miden 18 niños y cada uno tarda 3 minutos, ¿cuántos minutos se necesitan?", "18*3", "Se multiplican los niños por los minutos de cada uno.", " minutos"),
        ("=", "{F} Un niño de ejemplo pesó 12 kilogramos y 400 gramos. ¿Cuántos gramos son? (1 kilogramo son 1.000 gramos)", "12*1000+400", "Se convierten los kilogramos a gramos y se suman los 400 gramos.", " gramos"),
        ("abc", "{F} La madre de un niño pregunta si su hijo «está en su peso». ¿Qué responde la técnica?", "Que la educadora podrá conversar con ella sobre los controles", "Que está en su peso", "Que no sabe, pero que seguro está bien", "La interpretación la hace la educadora, no la técnica."),
        ("abc", "{F} Una técnica descubre que el valor de un niño es menor que el del control anterior. ¿Qué hace?", "Informa los valores a la educadora sin interpretar", "Lo corrige para que no haya diferencia", "Se lo cuenta a la familia", "Informar los números permite que la educadora decida."),
        ("abc", "{F} Una compañera propone comparar quién pesa más entre los niños para «motivar a comer». ¿Qué corresponde?", "No hacerlo: los datos son personales y comparar no ayuda", "Hacerlo, pues motiva", "Hacerlo solo con los más grandes", "Comparar cuerpos entre niños no respeta su privacidad ni su crecimiento."),
        ("=", "{F} El control anterior de un niño fue de 12.400 g y el de hoy es 12.700 g. ¿Cuántos gramos más pesa hoy?", "12700-12400", "Se resta el peso anterior al peso de hoy.", " gramos"),
        ("abc", "{F} Un niño no quiere subirse a la balanza porque tiene miedo. ¿Qué hace la técnica?", "Le explica con calma, se lo muestra con un peluche y avisa a la educadora si sigue sin querer", "Lo sube por la fuerza", "Le dice que es un miedoso", "Se respeta su ritmo y se informa a la educadora."),
    ],
    ctx=("abc", "{F} Antes de medir, la balanza marca 100 gramos con nada encima. ¿Qué hace la técnica?", "Avisa a la educadora, porque el instrumento no está en cero y los valores saldrían mal", "Mide igual y resta 100 gramos después", "Mide igual sin anotar el problema", "Un instrumento mal ajustado da datos incorrectos; se avisa y se corrige antes de medir."),
    sc=[
        ("En Atención de Párvulos: ¿en qué unidad se anota la talla?", "En centímetros", "Así lo indica la ficha del jardín."),
        ("¿Quién interpreta si un valor es normal?", "La educadora con el equipo de salud", "La técnica mide y registra, no interpreta."),
        ("¿Se comentan los valores con otras familias?", "No", "Son datos personales y confidenciales de cada niño y su familia."),
    ],
    op=("Caso de ejemplo. Se controla a 10 niños y niñas en un lugar reservado. La balanza marca cero. Mateo (ficticio) pesa 13.100 g y mide 94 cm. La madre de Mateo le pregunta a la técnica: «¿Está bien su peso?». "
        "Escribe: cuántos minutos necesitas si cada niño tarda 5; cómo anotarías los valores de Mateo; qué responderías a la madre; y qué informarías a la educadora.",
        "10 niños por 5 minutos: 50 minutos. Anotaría fecha, peso 13.100 g y talla 94 cm en la ficha de Mateo. A la madre: «La educadora podrá conversar con usted sobre los controles». A la educadora: los valores de hoy y, si los tengo, los del control anterior, sin interpretar.",
        ["calcula el tiempo", "anota los valores con la unidad", "deriva la interpretación a la educadora"],
        ["hoja con cálculo, anotación y dos frases"],
        ["interpretar el peso", "comentar el valor con otras personas", "olvidar las unidades"],
        "Pregunta: «¿qué harías si Mateo dice que no quiere subirse?». Debe respetar su ritmo y avisar a la educadora."),
    reinforce="Escribe tres reglas de respeto y privacidad al medir el peso y la talla de un niño.",
    extend="Explica por qué la técnica no debe decir si un valor es normal o no.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (unidades y registro, de ejemplo). 1 kilogramo (kg) son 1.000 gramos (g). 1 metro (m) son 100 centímetros (cm). Instrumentos: balanza para el peso y tallímetro para la talla de niños que pueden estar de pie; la balanza debe marcar cero antes de medir. "
     "La ficha del niño lleva fecha, edad en meses, peso en g, talla en cm, quién midió y observaciones. Edad en meses = años × 12 + meses.")
build(
    O7, 2, F,
    use="Aprenderé las unidades, los instrumentos y los datos de la ficha de control, y a pasar de años a meses y de kilogramos a gramos.",
    prior=["Conozco por qué se controla peso y talla.", "Sé multiplicar y sumar.", "Sé leer una ficha."],
    explain=[
        "Los instrumentos de medición son la balanza, que mide el peso, y el tallímetro, que mide la talla. Antes de medir se comprueba que la balanza marque cero; si no, se avisa. Las unidades se anotan siempre: gramos (g) para el peso y centímetros (cm) para la talla. Un kilogramo son 1.000 gramos y un metro son 100 centímetros, por eso 12 kilogramos y 400 gramos se anotan como 12.400 g.",
        "La ficha de control del niño tiene los datos: fecha, edad en meses, peso, talla, quién midió y observaciones. Para pasar la edad a meses se multiplican los años por 12 y se suman los meses, así 2 años y 7 meses son 31 meses. Se registra sin borrar: si se comete un error, se tacha con una línea y se anota el valor correcto con la fecha.",
        "Los datos del control son personales y solo los ven las personas autorizadas. Los valores se informan a la educadora para que ella decida si corresponde alguna acción." + LIM,
    ],
    vocab=[("balanza", "instrumento para medir el peso"), ("tallímetro", "instrumento para medir la talla"), ("edad en meses", "años multiplicados por 12 más los meses"), ("unidad", "nombre de la medida, como gramos o centímetros"), ("ficha de control", "documento con los datos de cada medición"), ("poner en cero", "comprobar que la balanza marque cero antes de medir")],
    worked=[
        ("Pasar la edad a meses", "Un niño de ejemplo tiene 3 años y 2 meses. ¿Cuál es su edad en meses?", ["3 × 12 = 36.", "36 + 2 = 38."], "38 meses"),
        ("Pasar a gramos", "Un niño de ejemplo pesa 9 kilogramos y 600 gramos. ¿Cuántos gramos son?", ["9 × 1.000 = 9.000.", "9.000 + 600 = 9.600."], "9.600 gramos"),
    ],
    mistakes=[("Anotar «13» sin unidad en la ficha.", "No se sabe si son kilos, gramos o centímetros.", "Escribe siempre el número con su unidad."),
              ("Borrar con corrector un valor mal anotado.", "Se pierde el rastro de lo que se escribió.", "Tacha con una línea, anota el valor correcto y la fecha.")],
    T=[
        ("abc", "{F} ¿Con qué instrumento se mide el peso?", "La balanza", "El tallímetro", "La regla de la sala", "La ficha indica balanza para el peso y tallímetro para la talla."),
        ("abc", "{F} ¿Qué se comprueba antes de usar la balanza?", "Que marque cero", "Que esté caliente", "Que tenga pilas nuevas siempre", "Una balanza que no está en cero da un valor incorrecto."),
        ("abc", "{F} ¿Cuántos gramos tiene un kilogramo?", "1.000", "100", "10", "La ficha dice que 1 kg son 1.000 g."),
        ("=", "{F} Un niño tiene 2 años y 7 meses. ¿Cuántos meses de edad tiene?", "2*12+7", "Se multiplican los años por 12 y se suman los meses.", " meses"),
        ("=", "{F} Una niña de ejemplo pesa 11 kilogramos y 250 gramos. ¿Cuántos gramos son?", "11*1000+250", "Se convierten los kilogramos a gramos y se suman los 250 g.", " gramos"),
        ("abc", "{F} ¿Cómo se corrige un valor mal anotado en la ficha?", "Se tacha con una línea, se anota el valor correcto y la fecha", "Se borra con corrector", "Se arranca la hoja", "Con una línea se conserva el rastro de lo anotado."),
        ("=", "{F} Un niño tiene 4 años y 1 mes. ¿Cuántos meses de edad tiene?", "4*12+1", "Se multiplican los años por 12 y se suma el mes.", " meses"),
        ("abc", "{F} Una ficha dice «peso: 13». ¿Qué falla?", "No indica la unidad", "Que el número es muy alto", "Que no tiene fecha de nacimiento", "Sin unidad no se sabe qué se midió."),
        ("=", "{F} Un niño mide 1 metro y 5 centímetros. ¿Cuántos centímetros mide?", "1*100+5", "Se convierte el metro a centímetros y se suman los 5 cm.", " cm"),
        ("abc", "{F} La balanza marca 200 gramos con nada encima. ¿Qué hace la técnica?", "Avisa a la educadora y no mide hasta que esté en cero", "Mide y resta 200 gramos después", "Mide igual sin anotarlo", "Un instrumento descalibrado se avisa y se corrige antes de medir."),
        ("abc", "{F} ¿Qué datos lleva la ficha de control?", "Fecha, edad en meses, peso, talla, quién midió y observaciones", "Solo el peso y el nombre del niño", "Las opiniones de la técnica sobre el niño", "La ficha de ejemplo trae esos seis datos."),
        ("=", "{F} Un niño tiene 5 años y 9 meses. ¿Cuántos meses más le faltan para cumplir 6 años (72 meses)?", "72-(5*12+9)", "Se calcula la edad en meses y se resta de 72.", " meses"),
        ("abc", "{F} Una técnica mide a un niño con zapatos puestos y anota la talla. ¿Qué falla?", "Debe medirse según el manual del jardín, sin objetos que cambien la medida", "Nada, así se mide más rápido", "Debe sumarle 5 centímetros", "Los objetos pueden cambiar la medida; se sigue el manual."),
    ],
    ctx=("abc", "{F} Al anotar el peso de un niño, la técnica se da cuenta de que escribió 12.400 g en lugar de 12.040 g. ¿Qué hace?", "Tacha con una línea, anota el valor correcto con la fecha y lo informa a la educadora", "Lo borra con corrector", "Lo deja así", "Se corrige sin borrar y se informa, para que la ficha sea confiable."),
    sc=[
        ("En Atención de Párvulos: ¿cuántos centímetros tiene un metro?", "100", "Así se pasa de metros a centímetros."),
        ("¿Cómo se pasa la edad a meses?", "Años por 12 más los meses", "Un año tiene 12 meses, por eso se multiplica por 12."),
        ("¿Qué haces si la balanza no está en cero?", "Aviso a la educadora y no mido", "Con la balanza descompuesta, el valor saldría incorrecto."),
    ],
    op=("Datos de ejemplo. Una niña, Camila (ficticia), tiene 3 años y 8 meses; hoy pesa 14 kilogramos y 100 gramos y mide 1 metro y 2 centímetros. La balanza estaba en cero. Se equivocó al anotar el peso y escribió 14.010 g. "
        "Escribe: la edad en meses; el peso en gramos y la talla en centímetros; cómo corregirías el error; y qué informarías a la educadora.",
        "Edad: 3 × 12 + 8 = 44 meses. Peso: 14 × 1.000 + 100 = 14.100 g. Talla: 102 cm. Corrección: tachar 14.010 con una línea, anotar 14.100 g y la fecha. Aviso: valores de hoy y la corrección, sin interpretar.",
        ["convierte unidades y edad", "corrige sin borrar", "informa a la educadora sin interpretar"],
        ["hoja con tres conversiones y una corrección"],
        ["borrar el error", "olvidar las unidades", "interpretar los valores"],
        "Pregunta: «¿qué harías si la talla anotada fuera menor que la del mes anterior?». Debe avisar a la educadora."),
    reinforce="Convierte tres pesos y tres edades de ejemplo a gramos y a meses.",
    extend="Explica por qué se tacha con una línea un error en la ficha en lugar de borrarlo.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (controles de ejemplo, valores inventados). Sofía: enero, 31 meses, 12.000 g, 88 cm; febrero, 32 meses, 12.300 g, 89 cm; marzo, 33 meses, 12.250 g, 90 cm. "
     "Bruno: enero, 30 meses, 12.500 g, 90 cm; febrero, 31 meses, 12.700 g, 91 cm; marzo, 32 meses, 12.900 g, 87 cm. La educadora interpreta los valores; la técnica los registra e informa.")
build(
    O7, 3, F,
    use="Aprenderé a analizar controles ya registrados: calcular diferencias, detectar valores que parecen un error de registro o de medición y avisar a la educadora sin interpretar.",
    prior=["Conozco unidades, edad en meses y la ficha de control.", "Sé restar.", "Sé que la educadora interpreta."],
    explain=[
        "Para analizar una serie de controles se ordenan por fecha y se calcula cuánto cambió cada medida de un mes al siguiente restando el valor anterior al nuevo. Estas diferencias se informan a la educadora tal como son, sin decir si son buenas o malas. La técnica puede ayudar a detectar valores que parecen un error de registro o de medición.",
        "Un valor sospechoso es el que no es esperable, por ejemplo una talla menor que la de un control anterior en un niño que sigue creciendo. En ese caso no se corrige el dato por cuenta propia ni se supone la causa: se informa a la educadora, que decide si se repite la medición. Una disminución del peso entre dos controles también se informa sin interpretación.",
        "Los valores de cada niño se tratan por separado y con reserva. No se comparan niños entre sí." + LIM,
    ],
    vocab=[("diferencia", "resultado de restar el valor anterior al nuevo"), ("serie de controles", "mediciones de un mismo niño ordenadas por fecha"), ("valor sospechoso", "valor que no se espera, por ejemplo una talla menor que antes"), ("error de registro", "equivocación al anotar un número"), ("repetir la medición", "volver a medir cuando la educadora lo indica")],
    worked=[
        ("Calcular una diferencia", "Un niño de ejemplo midió 85 cm en un control y 87 cm en el siguiente. ¿Cuántos centímetros cambió?", ["Se resta el valor anterior al nuevo.", "87 − 85 = 2."], "2 cm"),
        ("Detectar un valor sospechoso", "Un niño de ejemplo midió 92 cm y al mes siguiente 89 cm. ¿Qué se hace?", ["No se espera que la talla baje.", "Se informa a la educadora, que decide si se repite la medición."], "Informar a la educadora"),
    ],
    mistakes=[("Corregir por su cuenta la talla de 87 cm a 92 cm «porque seguro es un error».", "Se altera un dato sin verificar.", "Informa a la educadora y deja el valor tal como se registró."),
              ("Decir a la familia «su hijo no está creciendo bien».", "La técnica no interpreta y puede causar angustia.", "Ofrece que la educadora converse sobre los controles.")],
    T=[
        ("=", "{F} ¿Cuántos gramos aumentó Sofía de enero a febrero?", "12300-12000", "Se resta el peso de enero al de febrero.", " gramos"),
        ("=", "{F} ¿Cuántos gramos menos pesó Sofía en marzo que en febrero?", "12300-12250", "Se resta el peso de marzo al de febrero.", " gramos"),
        ("=", "{F} ¿Cuántos centímetros creció Sofía de enero a marzo?", "90-88", "Se resta la talla de enero a la de marzo.", " cm"),
        ("abc", "{F} ¿Qué valor de Bruno parece un error de registro o de medición?", "La talla de marzo, 87 cm, menor que la de febrero", "El peso de enero", "La edad de febrero", "Una talla menor que la anterior no es esperable en un niño que sigue creciendo."),
        ("abc", "{F} ¿Qué hace la técnica con la talla de 87 cm de Bruno?", "Informa a la educadora y no corrige el dato por su cuenta", "La cambia a 92 cm", "Se lo dice a la familia como diagnóstico", "Se informa para que la educadora decida si se repite la medición."),
        ("abc", "{F} El peso de Sofía bajó de febrero a marzo. ¿Qué anota la técnica?", "Los dos valores con sus fechas, sin explicar la causa", "Que Sofía comió menos", "Que Sofía está enferma", "Se registran los datos; la interpretación es de la educadora."),
        ("=", "{F} ¿Cuántos gramos aumentó Bruno de enero a marzo?", "12900-12500", "Se resta el peso de enero al de marzo.", " gramos"),
        ("=", "{F} ¿Cuántos centímetros creció Bruno de enero a febrero?", "91-90", "Se resta la talla de enero a la de febrero.", " cm"),
        ("abc", "{F} La madre de Bruno pregunta por qué midieron a su hijo «tan bajito» en marzo. ¿Qué responde la técnica?", "Que la educadora conversará con ella sobre los controles", "Que el niño dejó de crecer", "Que él se encogió", "La interpretación y la conversación son de la educadora."),
        ("abc", "{F} Otra técnica dice: «Bruno pesa más que Sofía, o sea que come mejor». ¿Qué corresponde?", "Aclarar que no se comparan niños ni se saca conclusiones de los números", "Aceptarlo", "Pedirle que lo anote", "Comparar niños y sacar conclusiones no corresponde."),
        ("=", "{F} Al repetir la medición, la talla de Bruno de marzo da 92 cm. ¿Cuántos centímetros creció respecto de febrero?", "92-91", "Se resta la talla de febrero a la nueva talla de marzo.", " cm"),
        ("abc", "{F} La educadora pide repetir la medición de Bruno. ¿Qué hace la técnica?", "La repite según el manual y anota el nuevo valor con la fecha, sin borrar el anterior", "Borra el valor anterior", "Anota cualquier número", "Repetir la medición se registra con una nueva anotación, sin borrar la anterior."),
        ("abc", "{F} ¿Qué hace la técnica si no está segura de haber leído bien la balanza?", "Avisa a la educadora y repite la medición con ella presente", "Anota un valor aproximado", "Anota el valor del control anterior", "Si hay duda se verifica con la responsable, nunca se inventa un valor."),
    ],
    ctx=("abc", "{F} Al revisar la ficha de Bruno, la técnica se da cuenta de que anotó por error el peso de otro niño (13.050 g) en la fila de marzo. ¿Qué hace?", "Tacha con una línea, anota el valor correcto con la fecha y avisa a la educadora", "Borra el valor con corrector", "Lo deja así porque nadie lo notará", "Un error de registro se corrige sin borrar y se informa, para que la ficha sea confiable."),
    sc=[
        ("En Atención de Párvulos: ¿cómo se calcula una diferencia entre dos controles?", "Restando el valor anterior al nuevo", "Así se ve cuánto cambió la medida."),
        ("¿Qué haces ante una talla menor que la anterior?", "Informo a la educadora y no la corrijo", "Puede ser un error de medición o registro; ella decide."),
        ("¿Se comparan niños entre sí?", "No", "Cada niño tiene su ritmo y sus datos son personales."),
    ],
    op=("Datos de ejemplo. Noa (ficticia): mayo, 36 meses, 13.000 g, 93 cm; junio, 37 meses, 13.150 g, 94 cm; julio, 38 meses, 13.100 g, 91 cm. "
        "Escribe: cuántos gramos y centímetros cambió Noa de mayo a junio y de junio a julio; qué valor te parece sospechoso; qué harías con él; y qué responderías a la madre si pregunta si Noa «está bien».",
        "Mayo a junio: +150 g y +1 cm. Junio a julio: −50 g y −3 cm. La talla de julio (91 cm) es sospechosa porque baja. Informaría a la educadora sin corregirla. A la madre: «La educadora podrá conversar con usted sobre los controles».",
        ["calcula las diferencias", "identifica el valor sospechoso", "informa sin interpretar y deriva"],
        ["hoja con cuatro diferencias y dos acciones"],
        ["corregir el valor por su cuenta", "interpretar la salud de Noa", "responder a la madre con un juicio"],
        "Pregunta: «¿qué harías si la educadora te pide medir de nuevo?». Debe repetir con ella presente y anotar sin borrar el anterior."),
    reinforce="Calcula las diferencias de peso y talla entre tres controles de ejemplo que inventes.",
    extend="Explica por qué la técnica no corrige un valor que le parece sospechoso.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (jornada de controles, de ejemplo). 18 niños y niñas del nivel medio; cada control (peso y talla) tarda 4 minutos. La educadora presente. Sala reservada, con una balanza y un tallímetro. Los resultados se anotan en la ficha de cada niño; después se entrega a la educadora una lista con nombre, peso en gramos y talla en centímetros. "
     "Datos del día (de ejemplo): Emilia, 36 meses, 13.500 g, 95 cm; Tomás, 35 meses, 13.200 g, 94 cm; Lía, 37 meses, 12.900 g, 93 cm.")
build(
    O7, 4, F,
    use="Aprenderé a aplicar un criterio con datos: organizar una jornada de controles, registrar con exactitud y comunicar los resultados a la educadora con respeto y reserva.",
    prior=["Conozco unidades, ficha y serie de controles.", "Sé calcular tiempos.", "Sé que no se comparan niños."],
    explain=[
        "Organizar una jornada de controles es calcular cuánto tiempo se necesita (niños por minutos de cada control) y preparar el lugar: una sala reservada, la balanza en cero, el tallímetro listo y las fichas a mano. Se llama a los niños de uno en uno, se les explica lo que se hará y se les agradece. La educadora está presente durante la jornada.",
        "Después se entrega a la educadora una lista con nombre, peso en gramos y talla en centímetros, tal como se midió. Esa lista es confidencial: no se deja a la vista, no se muestra a otras familias y no se publica. La técnica puede agregar una observación objetiva, como «no quiso subirse la primera vez», pero no escribe interpretaciones sobre el cuerpo del niño.",
        "Si el niño está en una etapa de cambio, como cuando está incómodo con un control, se respeta y se pide apoyo a la educadora." + LIM,
    ],
    vocab=[("jornada de controles", "día en que se miden peso y talla a todo el grupo"), ("lista de resultados", "documento con nombre, peso y talla que se entrega a la educadora"), ("observación objetiva", "hecho anotado, sin interpretación"), ("reservada", "que no tiene público y protege la privacidad"), ("agradecer", "reconocer al niño su colaboración")],
    worked=[
        ("Tiempo de la jornada", "Se controlan 15 niños de ejemplo y cada control tarda 4 minutos. ¿Cuántos minutos dura la jornada?", ["15 niños por 4 minutos cada uno.", "15 × 4 = 60."], "60 minutos"),
        ("Dónde guardar la lista", "La lista de resultados queda sobre la mesa de la sala. ¿Qué corresponde?", ["Es información confidencial que no se muestra a otras personas.", "Se entrega a la educadora y se guarda fuera de la vista."], "Entregarla a la educadora y guardarla fuera de la vista"),
    ],
    mistakes=[("Colgar la lista de pesos en el panel «para que las familias vean».", "Expone datos personales de todos los niños.", "Entrega la lista solo a la educadora."),
              ("Medir con el resto del grupo mirando.", "No respeta la privacidad del niño.", "Mide en una sala reservada y de uno en uno.")],
    T=[
        ("=", "{F} ¿Cuántos minutos dura la jornada de controles?", "18*4", "Se multiplican los niños por los minutos de cada control.", " minutos"),
        ("=", "{F} Cada control usa 1 hoja de registro. Se preparan hojas para los niños más 3 de repuesto. ¿Cuántas hojas se preparan?", "18+3", "Se suman las hojas de repuesto a una por niño.", " hojas"),
        ("abc", "{F} ¿Dónde se miden los niños?", "En una sala reservada, de uno en uno", "En el patio, frente a todos", "En la sala común con las familias", "La privacidad exige un lugar reservado."),
        ("abc", "{F} ¿A quién se entrega la lista de resultados?", "A la educadora", "A todas las familias del jardín", "A las niñas y niños del grupo", "La educadora interpreta y decide qué hacer."),
        ("abc", "{F} ¿Qué unidades se escriben en la lista?", "Gramos para el peso y centímetros para la talla", "Kilos para ambos", "Metros para el peso", "La ficha del jardín usa gramos y centímetros."),
        ("=", "{F} ¿Cuántos gramos pesa más Emilia que Lía?", "13500-12900", "Se resta el peso de Lía al de Emilia.", " gramos"),
        ("abc", "{F} ¿Cómo se anota la talla de Tomás?", "94 cm", "94", "94 kg", "Se anota con su unidad: centímetros."),
        ("abc", "{F} Una técnica propone anotar al lado de Lía «seguro come poco». ¿Qué corresponde?", "No anotar interpretaciones; anotar solo los valores y observaciones objetivas", "Anotarlo para que la educadora lo sepa", "Decírselo a la madre", "La técnica no interpreta; registra hechos."),
        ("abc", "{F} Emilia llora porque no quiere subirse a la balanza. ¿Qué hace la técnica?", "La tranquiliza, le explica con calma y avisa a la educadora si sigue sin querer", "La sube a la fuerza", "La deja sin control sin avisar", "Se respeta su ritmo y se informa."),
        ("=", "{F} Si se pierden 12 minutos por un retraso, ¿cuántos minutos suma la jornada ahora?", "18*4+12", "A los minutos de los controles se suman los del retraso.", " minutos"),
        ("abc", "{F} Una familia llega y pide ver la lista de pesos de todos los niños. ¿Qué responde la técnica?", "Que la lista es confidencial y que la educadora puede informarle sobre su hijo", "Se la muestra rápido", "Le muestra solo los de los niños más pequeños", "Los datos de otros niños son confidenciales."),
        ("=", "{F} ¿Cuántos gramos más pesa Emilia que Tomás?", "13500-13200", "Se resta el peso de Tomás al de Emilia.", " gramos"),
        ("abc", "{F} Después de la jornada, la técnica nota que olvidó anotar la talla de uno de los niños. ¿Qué hace?", "Avisa a la educadora y vuelve a medir a ese niño en otro momento", "Anota una talla parecida a la del control anterior", "Lo deja en blanco sin avisar", "Nunca se inventa un valor; se vuelve a medir."),
    ],
    ctx=("abc", "{F} Un niño dice en voz alta, al ver el resultado de otro: «¡él pesa más que yo!». ¿Qué hace la técnica?", "Explica con calma que cada niño crece a su ritmo y que los números son de cada uno", "Calla al niño con severidad", "Lee todos los pesos en voz alta", "Se educa en el respeto a la diversidad de cuerpos sin comparar."),
    sc=[
        ("En Atención de Párvulos: ¿cuántos minutos dura un grupo si cada niño tarda 4 y son 10?", "40 minutos", "Se multiplican los niños por los minutos de cada uno."),
        ("¿Dónde se miden los niños?", "En un lugar reservado", "Así se protege la privacidad de cada niño al medirlo."),
        ("¿Dónde se guarda la lista de resultados?", "Con la educadora, fuera de la vista", "Es información confidencial que no se muestra a otras personas."),
    ],
    op=("Datos de ejemplo. Jornada de controles de 12 niños y niñas, 5 minutos cada uno, en una sala reservada. Resultados: Amaru, 14.000 g y 96 cm; Camila, 13.400 g y 95 cm. Una niña se asusta con la balanza. "
        "Escribe: cuántos minutos dura la jornada; cómo anotarías los datos de Amaru y Camila; qué harías con la niña asustada; y qué harías con la lista al final.",
        "Dura 12 × 5 = 60 minutos. Amaru: 14.000 g y 96 cm; Camila: 13.400 g y 95 cm, con fecha. A la niña le explico con calma, se lo muestro con un peluche y aviso a la educadora si sigue sin querer. La lista se entrega a la educadora y se guarda fuera de la vista.",
        ["calcula el tiempo", "anota con unidades", "cuida a la niña y la privacidad"],
        ["hoja con cálculo, dos anotaciones y dos acciones"],
        ["olvidar las unidades", "publicar la lista", "forzar a la niña"],
        "Pregunta: «¿qué harías si una familia te pide ver la lista completa?». Debe decir que es confidencial y derivar a la educadora."),
    reinforce="Calcula cuánto dura una jornada de controles de 16 niños si cada uno tarda 5 minutos.",
    extend="Explica por qué la lista de resultados se entrega solo a la educadora.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (regla del jardín, de ejemplo). La técnica observa y registra lo que ve: no diagnostica, no da medicamentos por su cuenta y no decide qué hacer. Ante un malestar, un accidente o la sospecha de maltrato, avisa de inmediato a la educadora o al adulto responsable. "
     "Ante una emergencia, también se avisa a emergencias. El manual de salud y los protocolos del establecimiento dicen qué hace cada persona. Practicar con niños exige supervisión de la educadora.")
build(
    O8, 1, F,
    use="Aprenderé el contexto de la observación del bienestar de niños y niñas: qué se observa, qué no se hace y a quién se avisa ante un malestar, un accidente o una sospecha de maltrato.",
    prior=["Conozco el rol de la técnica y de la educadora.", "Distingo un hecho de una interpretación.", "Sé que los datos de los niños son confidenciales."],
    explain=[
        "En Atención de Párvulos, la técnica pasa muchas horas con los niños y puede notar cambios: un niño más callado, que no quiere jugar, que llora de forma distinta, que rechaza la comida o se queja de un dolor. Estos cambios se observan y se anotan con hechos: qué se vio, a qué hora y qué dijo el niño. No son un diagnóstico. Decir qué tiene el niño corresponde a los profesionales de salud.",
        "La regla central es avisar de inmediato a la educadora o al adulto responsable, y a emergencias si la situación es grave. La técnica acompaña con calma al niño y no lo deja solo. No da medicamentos ni remedios por su cuenta: un medicamento solo se entrega siguiendo el protocolo del establecimiento, con documentos de la familia y de un médico. Este cuaderno no enseña dosis ni tratamientos.",
        "Lo mismo ocurre ante un accidente menor, como un golpe en el patio, o ante la sospecha de maltrato: se avisa, se registra y se deja actuar a quien corresponde. En ningún caso la técnica investiga o confronta." + LIM,
    ],
    vocab=[("observar", "mirar con atención y anotar lo que se ve u oye"), ("diagnóstico", "decir qué enfermedad o problema tiene alguien; lo hacen los profesionales de salud"), ("adulto responsable", "persona del jardín que está a cargo cuando no está la educadora"), ("accidente menor", "situación inesperada, como un golpe o una caída, que se avisa a la educadora para que decida"), ("protocolo", "pasos acordados por el establecimiento"), ("emergencias", "servicio de ayuda al que se llama cuando la situación es grave")],
    worked=[
        ("Hecho o diagnóstico", "¿Qué frase es un hecho: «Tomás se frota los ojos» o «Tomás tiene una infección»?", ["Un hecho se ve y se puede contar.", "Decir qué tiene es un diagnóstico."], "«Tomás se frota los ojos»"),
        ("A quién se avisa", "Un niño de ejemplo dice «me duele la guatita» y la educadora está en la sala. ¿Qué hace la técnica?", ["No le da nada por su cuenta.", "Lo acompaña y avisa de inmediato a la educadora."], "Acompañarlo y avisar a la educadora"),
    ],
    mistakes=[("Dar una cucharada de un jarabe de la mochila porque «a mi hijo le sirve».", "No sabe si corresponde y podría dañar al niño.", "No des nada y avisa de inmediato a la educadora."),
              ("Decirle a la familia «su hijo tiene fiebre» sin que lo haya evaluado nadie.", "Es un diagnóstico que no le corresponde.", "Avisa a la educadora, que decide a quién contactar.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué hace la técnica si observa que un niño está decaído y sin ganas de jugar?", "Lo acompaña, registra lo que ve y avisa a la educadora", "Le da un remedio de su bolso", "Le dice a la familia qué enfermedad tiene", "La técnica observa, registra y avisa; no da remedios ni diagnostica."),
        ("abc", "{F} ¿Quién decide qué hacer ante un malestar?", "La educadora o el adulto responsable", "La técnica según su experiencia", "Otro niño del grupo", "Según la regla del jardín, la técnica avisa y decide quien está a cargo."),
        ("abc", "{F} ¿A quién se avisa de inmediato ante un accidente, un malestar o una sospecha de maltrato?", "A la educadora o al adulto responsable", "Solo a la familia", "A ningún adulto hasta tener certeza", "La regla pide avisar de inmediato a quien está a cargo."),
        ("abc", "{F} ¿Cuál de estas frases es un hecho observable?", "Tomás se frota los ojos y tiene las mejillas rojas", "Tomás tiene una infección", "Tomás está haciéndose el enfermo", "Frotarse los ojos y mejillas rojas se ven; las otras frases interpretan."),
        ("abc", "Un niño se cae en el patio y llora. ¿Qué hace primero la técnica?", "Se acerca con calma, no lo deja solo y avisa de inmediato a la educadora", "Lo levanta rápido y lo manda a jugar", "Espera a ver si deja de llorar", "Se acompaña y se avisa de inmediato, sin improvisar."),
        ("abc", "Una madre deja en la mochila de su hijo un frasco con jarabe y una nota. ¿Qué hace la técnica?", "No lo da ni lo guarda por su cuenta, y entrega la nota y el frasco a la educadora o dirección para seguir el protocolo", "Lo da según la nota", "Le pide al niño que se lo tome solo", "Los medicamentos solo se manejan según el protocolo y con documentos."),
        ("=", "{F} En una jornada la técnica registra 6 observaciones en la mañana y 4 en la tarde; 3 de ellas requirieron aviso inmediato. ¿Cuántas no requirieron aviso inmediato?", "6+4-3", "Se suman todas las observaciones y se restan las de aviso inmediato.", " observaciones"),
        ("abc", "¿Qué anotación está bien escrita?", "«A las 10:30 Mateo dijo: me duele la cabeza, y se frotó los ojos»", "«Mateo tiene fiebre»", "«Mateo se hace el enfermo»", "Se anota lo que dijo e hizo, con la hora, sin interpretar."),
        ("abc", "Una familia le pide a la técnica en la puerta que su hijo, resfriado, «no salga al patio». ¿Qué hace?", "Le dice que la educadora podrá conversarlo y le avisa", "Acepta y no lo avisa a nadie", "Le dice que no se preocupe", "Los acuerdos de salud con las familias pasan por la educadora."),
        ("abc", "¿Por qué la técnica no hace diagnósticos?", "Porque no tiene la formación de un profesional de salud y podría equivocarse", "Porque no tiene tiempo", "Porque nadie le ha pedido su opinión", "Un diagnóstico equivocado puede causar daño o retrasar la ayuda."),
        ("abc", "Una compañera propone dar «un remedio casero» a un niño con dolor. ¿Qué corresponde?", "No dar nada y avisar a la educadora", "Dárselo en poca cantidad", "Dárselo si el niño lo pide", "No se da nada por cuenta propia."),
        ("=", "{F} Un niño dijo que le dolía la cabeza a las 10:30 y la técnica avisó a las 10:32. ¿Cuántos minutos pasaron hasta el aviso?", "(10*60+32)-(10*60+30)", "Se restan las dos horas, en minutos.", " minutos"),
        ("abc", "Un niño dice que se siente mal, pero la educadora está en otra sala. ¿Qué hace la técnica?", "Lo acompaña, pide ayuda de inmediato a otro adulto responsable y no le da nada", "Espera a que vuelva la educadora", "Le da agua con azúcar", "Si falta la educadora, se avisa a otro adulto responsable sin dejar al niño solo."),
    ],
    ctx=("abc", "{F} A mitad de la mañana, un niño llora, se queja de dolor en una pierna y no quiere apoyarla. La educadora está en la sala. ¿Qué hace la técnica?", "Se acerca, lo acompaña con calma sin dejarlo solo y avisa de inmediato a la educadora", "Lo obliga a caminar para ver si le duele", "Le dice que no es nada", "Se avisa enseguida y quien está a cargo decide si se llama a emergencias."),
    sc=[
        ("En Atención de Párvulos: ¿qué haces ante un malestar de un niño?", "Lo acompaño y aviso de inmediato a la educadora", "La técnica no diagnostica ni da remedios."),
        ("¿Das un medicamento a un niño porque la familia lo pide en una nota?", "No, sigo el protocolo con la educadora o dirección", "Los medicamentos tienen documentos y personas autorizadas."),
        ("¿Qué anotas en un registro?", "Hechos observados con la hora", "Los hechos se pueden comprobar y las opiniones no."),
    ],
    op=("Caso de ejemplo. Durante la siesta, una niña, Lía, se queja de dolor de cabeza y llora. La educadora está en la sala. Su madre dejó en la mochila un frasco de jarabe con una nota. "
        "Escribe: qué hace la técnica en el momento; qué anota con hechos; qué hace con el frasco y la nota; y qué no hace.",
        "La técnica acompaña a Lía con calma, no la deja sola y avisa de inmediato a la educadora. Anota: «A las 14:10 Lía lloró y dijo que le dolía la cabeza». El frasco y la nota se entregan a la educadora o dirección para seguir el protocolo; no se da nada. No hace diagnósticos, no da el jarabe y no le dice a la madre qué tiene.",
        ["acompaña y avisa de inmediato", "anota hechos con la hora", "no da medicamentos ni diagnostica"],
        ["hoja con cuatro respuestas breves"],
        ["dar el jarabe", "interpretar la causa", "no avisar a la educadora"],
        "Pregunta: «¿qué harías si Lía empeora?». Debe avisar de inmediato a la educadora y, si hay una emergencia, a emergencias."),
    reinforce="Escribe tres hechos observables que podrías anotar sobre un niño que está decaído.",
    extend="Explica por qué avisar de inmediato es más importante que tratar de entender qué le pasa al niño.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (vocabulario y documentos, de ejemplo). Hecho observable: algo que se ve u oye («llora», «se frota los ojos»). Interpretación: explicación de por qué ocurre («está resfriado»). "
     "Registro de accidente: fecha, hora, lugar, qué ocurrió, quién estaba presente, a quién se avisó y a qué hora. Autorización escrita: documento de la familia que el establecimiento exige, junto con la indicación escrita de un médico, para cualquier medicamento; lo maneja solo la persona autorizada por el protocolo. "
     "Buen trato: trato respetuoso y tierno, con límites claros. Maltrato: cualquier acción u omisión que daña a un niño o lo pone en riesgo.")
build(
    O8, 2, F,
    use="Aprenderé el vocabulario y los documentos para registrar y avisar: hechos, interpretaciones, registro de accidente, autorización escrita, buen trato y maltrato.",
    prior=["Sé que la técnica no diagnostica.", "Sé que se avisa de inmediato a la educadora.", "Sé leer una ficha."],
    explain=[
        "Para avisar bien hay que distinguir un hecho observable, como «lloró y se frotó los ojos», de una interpretación, como «está resfriado». En el registro solo van hechos. Un registro de accidente tiene: fecha, hora, lugar, qué ocurrió, quiénes estaban presentes y a quién se avisó y a qué hora. Se escribe con claridad, sin culpar a nadie.",
        "Un medicamento solo se entrega si la familia presenta una autorización escrita y la indicación escrita de un médico, y lo maneja únicamente la persona que el protocolo autoriza. La técnica no decide ni administra por cuenta propia. Este cuaderno no trata dosis ni procedimientos de tratamiento.",
        "El buen trato es tratar con respeto, ternura y límites claros. El maltrato es cualquier acción u omisión que daña o pone en riesgo a un niño, y los adultos tienen el deber de protegerlos. Si hay una sospecha, no se investiga ni se confronta: se avisa de inmediato a la educadora o a la dirección, que activan las redes de protección según el protocolo del establecimiento. El Fono Niños 147 es una línea de ayuda." + LIM,
    ],
    vocab=[("hecho observable", "algo que se ve u oye y se puede contar"), ("interpretación", "explicación personal de por qué ocurre algo"), ("registro de accidente", "documento con fecha, hora, lugar, qué ocurrió, presentes y a quién se avisó"), ("autorización escrita", "documento de la familia que exige el establecimiento para un medicamento"), ("buen trato", "trato respetuoso, tierno y con límites claros"), ("maltrato", "acción u omisión que daña a un niño o lo pone en riesgo")],
    worked=[
        ("Completar un registro", "Un registro de ejemplo tiene fecha, hora, lugar, qué ocurrió y quiénes estaban presentes, pero falta algo importante. ¿Qué falta?", ["El registro debe decir a quién se avisó y cuándo.", "Falta esa parte."], "A quién se avisó y a qué hora"),
        ("Hecho o interpretación", "¿Qué frase es una interpretación: «Noa llora» o «Noa llora porque está celosa»?", ["Llorar se ve.", "La causa es una interpretación."], "«Noa llora porque está celosa»"),
    ],
    mistakes=[("Escribir «se cayó por culpa del auxiliar».", "Culpa a una persona sin certeza y el registro no es para eso.", "Escribe qué ocurrió y quiénes estaban."),
              ("Aceptar un frasco con una nota escrita a mano como autorización.", "El protocolo exige documentos y una persona autorizada.", "Deriva a la educadora o dirección para seguir el protocolo.")],
    T=[
        ("abc", "{F} ¿Cuál de estas es un hecho observable?", "Camila llora y se agarra el codo", "Camila tiene un dolor fuerte", "Camila se lastimó el hueso", "Llorar y agarrarse el codo se ven; las otras frases interpretan."),
        ("abc", "{F} ¿Cuál es una interpretación?", "«Amaru está resfriado»", "«Amaru estornuda»", "«Amaru se frota la nariz»", "Decir que está resfriado explica la causa, y no se puede comprobar."),
        ("abc", "{F} ¿Qué datos lleva un registro de accidente?", "Fecha, hora, lugar, qué ocurrió, presentes, a quién se avisó y a qué hora", "Solo el nombre del niño", "La opinión de la técnica sobre qué pasó", "La ficha trae esos siete datos."),
        ("abc", "{F} ¿Qué documentos exige el establecimiento para un medicamento?", "Autorización escrita de la familia e indicación escrita de un médico", "Una nota del niño", "Una llamada de un vecino", "Ambos documentos son necesarios y los maneja la persona autorizada."),
        ("abc", "En Atención de Párvulos: ¿qué es el maltrato infantil?", "Cualquier acción u omisión que daña a un niño o lo pone en riesgo", "Cualquier regaño suave que no daña", "Un juego brusco entre niños", "El maltrato daña o pone en riesgo al niño; los otros ejemplos no lo son."),
        ("abc", "{F} Un registro dice: «Lunes, 11:00, patio. Mateo se cayó. No se avisó a nadie». ¿Qué falla?", "No dice a quién se avisó y hay que avisar de inmediato", "Nada: el registro es suficiente", "Que dice la hora", "Un accidente se avisa de inmediato y se registra a quién."),
        ("=", "{F} En un día, el jardín anotó 4 registros de accidente por la mañana y 2 por la tarde. ¿Cuántos registros hay en total?", "4+2", "Se suman los registros de las dos partes del día.", " registros"),
        ("abc", "{F} ¿Cuál de estas es una muestra de buen trato?", "Poner un límite con voz calmada y explicar la razón", "Burlarse de un niño que llora", "Dejarlo en una sala solo como castigo", "El buen trato combina respeto y límites sin humillar."),
        ("abc", "{F} Una técnica escribe: «Bruno es agresivo y se pegó él mismo». ¿Qué falla?", "Interpreta y etiqueta en vez de contar los hechos", "Nada", "Que usó el nombre del niño", "El registro solo lleva hechos y no opiniones ni etiquetas."),
        ("abc", "{F} Una familia deja un frasco sin documentos. ¿Qué hace la técnica?", "Lo entrega a la educadora o dirección y no lo da", "Lo da con cuidado", "Lo guarda en su bolso", "Sin documentos y sin persona autorizada no se maneja un medicamento."),
        ("=", "{F} Un accidente ocurrió a las 10:40 y se avisó a las 10:45. ¿Cuántos minutos pasaron?", "(10*60+45)-(10*60+40)", "Se restan las dos horas, en minutos.", " minutos"),
        ("abc", "{F} ¿Qué debe hacer un adulto ante una sospecha de maltrato?", "Avisar de inmediato a la educadora o dirección, sin investigar ni confrontar", "Preguntar a la familia qué pasó", "Esperar hasta tener pruebas", "Los adultos protegen avisando y dejando actuar a quien corresponde."),
        ("abc", "{F} ¿Qué es el Fono Niños 147?", "Una línea de ayuda para niños, niñas y adolescentes", "El teléfono de la sala", "El número del jardín", "Es la línea de ayuda que se nombra en este cuaderno."),
    ],
    ctx=("abc", "{F} Un niño se golpea la cabeza con una mesa en la sala. La técnica lo acompaña y avisa a la educadora. ¿Qué anota después?", "Fecha, hora, lugar, qué ocurrió, presentes y a quién y cuándo avisó", "Su opinión sobre qué le pasó al niño", "Solo que fue un accidente", "El registro lleva hechos y a quién se avisó."),
    sc=[
        ("En Atención de Párvulos: ¿qué documentos exige el establecimiento para un medicamento?", "Autorización de la familia e indicación escrita de un médico", "Con ambos documentos se sigue el protocolo."),
        ("¿Qué escribes en un registro de accidente?", "Hechos con fecha, hora y a quién avisé", "Así queda un registro claro y útil para la educadora."),
        ("¿Qué es el buen trato?", "Trato respetuoso, tierno y con límites claros", "Pone límites con calma y respeto, sin humillar al niño."),
    ],
    op=("Caso de ejemplo. El martes a las 10:20, en el patio, un niño de ejemplo se cayó de un banco bajo y se pegó en la barbilla. Estaban presentes la técnica y 5 niños. La técnica avisó a la educadora a las 10:21. "
        "Escribe: un registro de accidente con los siete datos; una frase que sea un hecho y otra que sea una interpretación sobre el niño; y a quién avisarías si el niño empeora.",
        "Registro: Martes (ficticio), 10:20, patio, el niño se cayó de un banco bajo y se pegó en la barbilla; presentes: la técnica y 5 niños; se avisó a la educadora a las 10:21. Hecho: «Lloró y se agarró la barbilla». Interpretación: «Está muy asustado». Si empeora: aviso de inmediato a la educadora o adulto responsable y a emergencias.",
        ["el registro tiene los siete datos", "distingue hecho e interpretación", "avisa a la educadora y a emergencias si empeora"],
        ["hoja con registro y dos frases"],
        ["omitir a quién se avisó", "escribir un diagnóstico", "no avisar a emergencias si empeora"],
        "Pregunta: «¿qué dato falta si no anotas la hora del aviso?». Debe ver que no se sabe cuánto se tardó."),
    reinforce="Escribe un registro de accidente de ejemplo con los siete datos.",
    extend="Explica por qué en un registro de accidente no se escribe quién tuvo la culpa.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (caso de ejemplo, ficticio). Tomás, de 3 años, llegó hoy más callado de lo habitual. A las 8:30 no quiso comer su desayuno y se frotaba los ojos. A las 10:30 dijo «me duele la cabeza» y tenía las mejillas rojas. "
     "La educadora está en la sala. Registro a completar: hora, hecho y a quién se avisó.")
build(
    O8, 3, F,
    use="Aprenderé a analizar un caso de cambios en un niño: qué hechos anotar, cuándo avisar, qué no hacer y qué decir a la familia.",
    prior=["Distingo hechos e interpretaciones.", "Conozco el registro y el aviso.", "Sé calcular minutos."],
    explain=[
        "Para analizar un caso de cambios en un niño se hace una lista de hechos con la hora: qué se vio, qué dijo el niño y qué hizo. Si los cambios aparecen en distintos momentos del día, se anotan todos, porque juntos ayudan a la educadora a decidir. Cada hecho se avisa de inmediato a la educadora o al adulto responsable, sin esperar a tener todos.",
        "La técnica acompaña al niño con calma y no lo deja solo. No le da medicamentos ni remedios, no le pregunta cosas que lo asusten y no le dice a la familia qué cree que tiene. Si la educadora decide contactar a la familia o a servicios de salud, ella lo hace. En una emergencia se avisa también a emergencias.",
        "Los registros del caso son confidenciales y no se comentan con otras familias." + LIM,
    ],
    vocab=[("cambio de conducta", "algo distinto en lo que el niño hace habitualmente"), ("lista de hechos", "anotaciones con la hora de lo observado"), ("aviso inmediato", "avisar apenas se nota algo, sin esperar"), ("acompañar", "estar cerca del niño con calma, sin dejarlo solo"), ("confidencial", "que no se comenta con personas ajenas")],
    worked=[
        ("Armar una lista de hechos", "Un niño de ejemplo llegó callado a las 8:00 y a las 9:30 dijo «tengo frío». ¿Cuáles son los dos hechos?", ["Cada uno con su hora.", "8:00 llegó callado; 9:30 dijo «tengo frío»."], "8:00 llegó callado; 9:30 dijo «tengo frío»"),
        ("Qué no hacer", "Una compañera dice «tócale la frente y dile a la mamá que tiene fiebre». ¿Qué corresponde?", ["Es un diagnóstico.", "La técnica avisa a la educadora, que decide."], "Avisar a la educadora y no decir que tiene fiebre"),
    ],
    mistakes=[("Esperar a la hora de salida para contarle a la educadora lo que pasó en la mañana.", "La educadora no pudo decidir a tiempo.", "Avisa apenas lo notes."),
              ("Decirle a la madre «su hijo anda con una infección».", "No es su rol diagnosticar.", "Dile que la educadora podrá conversar con ella.")],
    T=[
        ("abc", "{F} ¿Qué hecho se observó a las 8:30?", "Tomás no quiso comer su desayuno y se frotaba los ojos", "Tomás tenía las mejillas rojas", "Tomás dijo que le dolía la cabeza", "A las 8:30 se anotó el rechazo del desayuno y los ojos."),
        ("abc", "{F} ¿Qué dijo Tomás a las 10:30?", "«Me duele la cabeza»", "«Quiero comer»", "«Tengo frío»", "La ficha registra esa frase dicha por el niño a esa hora."),
        ("=", "{F} ¿Cuántos minutos pasaron entre los dos primeros hechos (8:30 y 10:30)?", "(10*60+30)-(8*60+30)", "Se restan las horas, convertidas a minutos.", " minutos"),
        ("abc", "{F} ¿A quién avisa la técnica y cuándo?", "A la educadora, de inmediato", "A la familia, al final del día", "A nadie, hasta estar segura", "Se avisa de inmediato a quien está a cargo."),
        ("abc", "{F} ¿Cuál es el registro correcto?", "«8:30: no quiso comer y se frotaba los ojos. 10:30: dijo me duele la cabeza y tenía las mejillas rojas. Avisé a la educadora»", "«Tomás está enfermo»", "«Tomás tiene fiebre y debe irse»", "El registro correcto cuenta hechos, horas y a quién se avisó."),
        ("abc", "{F} Una compañera propone darle un jarabe «para que se sienta mejor». ¿Qué corresponde?", "No dar nada y esperar la indicación de la educadora", "Dárselo en poca cantidad", "Darle agua con azúcar", "La técnica no da medicamentos ni remedios."),
        ("abc", "{F} La madre llega y pregunta qué tiene su hijo. ¿Qué responde la técnica?", "Que la educadora podrá informarle de lo observado", "Que tiene fiebre", "Que no sabe, pero que seguro es poca cosa", "Los diagnósticos no corresponden y la educadora conversa con la familia."),
        ("abc", "{F} La técnica nota que Tomás está más decaído y se queja de dolor intenso. La educadora no está en la sala. ¿Qué hace?", "Lo acompaña, pide ayuda de inmediato a otro adulto responsable y no le da nada", "Espera a que vuelva la educadora", "Le pide que se mueva para distraerse", "Se pide ayuda de inmediato y se acompaña."),
        ("=", "{F} Si se avisó a la educadora a las 10:31, ¿cuántos minutos pasaron desde que Tomás dijo que le dolía la cabeza (10:30)?", "(10*60+31)-(10*60+30)", "Se restan las dos horas, en minutos.", " minutos"),
        ("abc", "{F} Otro niño pregunta qué le pasa a Tomás. ¿Qué responde la técnica?", "Que Tomás no se siente bien y que lo están cuidando", "Que Tomás está enfermo y se contagiará", "Que no moleste a Tomás y se calle", "Se responde con calma y sin dar detalles que asusten."),
        ("abc", "{F} Una técnica anota: «Tomás se hace el enfermo para no comer». ¿Qué falla?", "Interpreta una intención que no se puede comprobar", "Nada", "Que usó el nombre del niño", "El registro no incluye intenciones que nadie puede comprobar."),
        ("=", "{F} Si hay 15 niños en la sala y la técnica debe seguir a cargo de los 14 restantes mientras acompaña a Tomás, ¿cuántos niños son los otros?", "15-1", "Al total se le resta Tomás.", " niños"),
        ("abc", "{F} Mientras acompaña a Tomás, la técnica no puede ver bien a los otros niños. ¿Qué hace?", "Pide a otro adulto responsable que supervise al resto", "Los deja solos un momento", "Pide a un niño que los cuide", "Los niños no se dejan solos; se coordina el cuidado."),
    ],
    ctx=("abc", "{F} A las 11:00 Tomás vomita y se pone muy pálido. La educadora se acerca. ¿Qué hace la técnica?", "Sigue las indicaciones de la educadora, cuida al resto del grupo y anota hechos con la hora", "Le da un medicamento del botiquín", "Llama a la familia para decir qué tiene", "La educadora decide; la técnica colabora, cuida al grupo y registra."),
    sc=[
        ("En Atención de Párvulos: ¿qué anotas en la lista de hechos?", "Lo que vi y escuché con la hora", "Así la educadora puede decidir con información completa y a tiempo."),
        ("¿Cuándo avisas a la educadora?", "De inmediato", "No hay que esperar a tener todos los hechos."),
        ("¿Dices a la familia qué cree la técnica que tiene el niño?", "No", "Los diagnósticos no corresponden a la técnica."),
    ],
    op=("Caso de ejemplo. Camila (ficticia), de 4 años, llega a las 8:00 muy cansada; a las 9:15 se acuesta en un rincón; a las 10:00 no quiere jugar y dice «me duele la guatita». La educadora está en la sala. "
        "Escribe: una lista de hechos con horas; qué haces y a quién avisas; qué no haces; y cómo respondes a la madre que llega a las 12:00 y pregunta por Camila.",
        "Hechos: 8:00 llegó muy cansada; 9:15 se acostó en un rincón; 10:00 no quiso jugar y dijo «me duele la guatita». Acompaño a Camila y aviso de inmediato a la educadora. No le doy nada, no diagnostico y no la dejo sola. A la madre: «La educadora podrá conversar con usted sobre lo que observamos».",
        ["lista de hechos con horas", "acompaña y avisa de inmediato", "no da medicamentos ni diagnostica y deriva"],
        ["hoja con lista de hechos y tres acciones"],
        ["dar algo a la niña", "diagnosticar", "dejar a la niña sola"],
        "Pregunta: «¿qué pasaría si Camila empeora?». Debe avisar de inmediato a la educadora y, si hay una emergencia, a emergencias."),
    reinforce="Escribe una lista de cuatro hechos con hora sobre un niño que está decaído.",
    extend="Explica por qué avisar apenas aparece el primer cambio ayuda más que esperar a ver cómo sigue.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (conducta ante una sospecha, de ejemplo). Si un niño o niña dice o hace algo que hace sospechar maltrato: escuchar con calma; no hacer preguntas insistentes ni investigar; no confrontar a ningún adulto; no prometer guardar el secreto; anotar las palabras exactas y la hora; "
     "avisar de inmediato a la educadora o a la dirección, que actúan con las redes de protección según el protocolo del establecimiento. Fono Niños 147: línea de ayuda. Buen trato: respeto, ternura y límites claros.")
build(
    O8, 4, F,
    use="Aprenderé el buen trato, los derechos de niños y niñas y la única conducta de la técnica ante una sospecha de maltrato: escuchar, registrar y avisar de inmediato.",
    prior=["Conozco el buen trato.", "Sé que los registros llevan hechos.", "Sé que el protocolo del establecimiento guía las acciones."],
    explain=[
        "Los niños y niñas tienen derecho a ser respetados, escuchados, cuidados y protegidos. El buen trato cumple esos derechos: se pone un límite con calma, sin gritos, burlas, comparaciones ni castigos humillantes. El maltrato daña o pone en riesgo al niño. Este cuaderno no enseña a reconocer casos reales: eso exige formación y el protocolo del establecimiento.",
        "Si un niño o niña dice o hace algo que preocupa, la técnica nunca investiga ni confronta. Lo escucha con calma, sin presionar ni hacer preguntas insistentes, no promete guardar el secreto, anota sus palabras exactas con la hora y avisa de inmediato a la educadora o a la dirección. Ellas activan las redes de protección según el protocolo. La técnica guarda reserva con el resto.",
        "El Fono Niños 147 es una línea de ayuda para niños, niñas y adolescentes. La técnica no habla con la familia ni con el adulto involucrado sobre la sospecha." + LIM,
    ],
    vocab=[("derecho del niño", "algo que todo niño o niña merece, como ser protegido y escuchado"), ("buen trato", "trato respetuoso, tierno y con límites claros"), ("maltrato", "acción u omisión que daña a un niño o lo pone en riesgo"), ("red de protección", "instituciones que protegen a niños y niñas, a las que acude el establecimiento según su protocolo"), ("confrontar", "enfrentar a un adulto para pedirle explicaciones"), ("palabras exactas", "lo que el niño dijo, tal cual")],
    worked=[
        ("Elegir la conducta", "Un niño de ejemplo dice una frase que preocupa. ¿Qué hace la técnica primero?", ["Escucha con calma, sin presionar.", "Anota sus palabras y avisa de inmediato a la educadora."], "Escucharlo, anotar sus palabras y avisar de inmediato"),
        ("Qué no hacer", "Una compañera propone preguntar al niño varias veces «¿quién fue?». ¿Qué corresponde?", ["Las preguntas insistentes presionan al niño.", "No se investiga: se avisa."], "No hacerlo; avisar a la educadora o dirección"),
    ],
    mistakes=[("Prometer «no se lo cuento a nadie» a un niño que cuenta algo que preocupa.", "No se puede guardar un secreto si el niño puede estar en riesgo.", "Dile con calidez que vas a pedir ayuda a un adulto que sabe cómo cuidarlo."),
              ("Hablar con el adulto involucrado para «aclarar las cosas».", "Es confrontar y puede poner al niño en mayor riesgo.", "Avisa de inmediato a la educadora o dirección, que activan las redes.")],
    T=[
        ("abc", "En Atención de Párvulos: ¿qué es el buen trato?", "Trato respetuoso, tierno y con límites claros", "Complacer siempre al niño", "Evitar poner límites", "El buen trato combina cariño y límites sin humillar."),
        ("abc", "{F} Si un niño dice algo que preocupa, ¿qué hace la técnica primero?", "Lo escucha con calma, sin preguntas insistentes", "Le hace muchas preguntas para entender", "Le dice que no se preocupe y cambia de tema", "Se escucha sin presionar ni cambiar de tema."),
        ("abc", "{F} ¿Qué anota la técnica?", "Las palabras exactas del niño y la hora", "Su opinión sobre quién tiene la culpa", "Una conclusión sobre lo que pasó", "Se anotan palabras exactas, no conclusiones."),
        ("abc", "{F} ¿A quién avisa de inmediato?", "A la educadora o a la dirección", "A la familia", "Al adulto involucrado", "Quienes activan las redes de protección según el protocolo son la educadora y la dirección."),
        ("abc", "{F} Un niño pide a la técnica que no se lo cuente a nadie. ¿Qué responde?", "Que no puede guardar secretos si él puede estar en riesgo y que pedirá ayuda a un adulto que sabe cuidarlo", "Que prometido, no se lo contará a nadie", "Que no diga nada a otros niños", "No se promete guardar el secreto; se explica con calidez que se pedirá ayuda."),
        ("abc", "{F} Una técnica quiere hablar con el adulto señalado «para aclarar». ¿Qué corresponde?", "No hacerlo: confrontar puede aumentar el riesgo; se avisa a la educadora o dirección", "Hacerlo con respeto", "Hacerlo si el niño está de acuerdo", "Confrontar queda fuera del rol de la técnica."),
        ("abc", "{F} ¿Qué es el Fono Niños 147?", "Una línea de ayuda para niños, niñas y adolescentes", "El teléfono del jardín", "Un número para pedir materiales", "Es la línea de ayuda que nombra este cuaderno."),
        ("=", "{F} En un taller de buen trato de ejemplo participan 24 niños en grupos de 6. ¿Cuántos grupos se forman?", "24//6", "Se divide el total entre los niños por grupo.", " grupos"),
        ("abc", "{F} Una técnica comenta a otra familia «creo que a ese niño lo tratan mal en su casa». ¿Qué falla?", "Comparte una sospecha con quien no debe y puede dañar a la familia y al niño", "Nada, es información útil", "Que no lo dijo a la educadora", "La reserva es parte de la protección; solo se informa a quien corresponde."),
        ("abc", "¿Qué derecho se cumple al poner un límite con calma y explicando la razón?", "El derecho a ser respetado y cuidado", "El derecho a no tener límites", "El derecho a no ser escuchado", "El buen trato cumple el derecho a ser respetado."),
        ("abc", "Un adulto del jardín grita y humilla a un niño por derramar su vaso. ¿Qué hace la técnica?", "Acompaña al niño con calma y avisa de inmediato a la educadora o dirección", "Grita también para apoyar", "Calla por temor a quedar mal", "Se cuida al niño y se avisa a quien puede activar el protocolo."),
        ("=", "{F} La técnica escucha al niño a las 11:00 y avisa a las 11:03. ¿Cuántos minutos pasaron antes del aviso?", "(11*60+3)-(11*60)", "Se restan las dos horas, en minutos.", " minutos"),
        ("abc", "{F} ¿Qué se hace con las notas escritas sobre este tipo de situaciones?", "Se entregan a la educadora o dirección y se guardan con reserva", "Se dejan en la sala para que todos las lean", "Se comentan en el recreo", "Son datos sensibles y se manejan con confidencialidad."),
    ],
    ctx=("abc", "{F} Una niña le cuenta a la técnica algo que le preocupa sobre cómo la trata un adulto y agrega «no le digas a nadie». La técnica la escucha con calma. ¿Qué hace?", "Le dice con cariño que pedirá ayuda a un adulto que sabe cuidarla, anota sus palabras exactas y avisa de inmediato a la educadora o dirección", "Le promete guardar el secreto", "Le hace varias preguntas para comprobar su relato", "Se escucha, se anota y se avisa de inmediato sin prometer secreto ni investigar."),
    sc=[
        ("En Atención de Párvulos: ¿qué haces ante una sospecha de maltrato?", "Escucho con calma, anoto y aviso de inmediato a la educadora o dirección", "No se investiga ni se confronta."),
        ("¿Prometes guardar el secreto?", "No", "Si el niño puede estar en riesgo, hay que pedir ayuda."),
        ("¿Qué línea de ayuda nombra este cuaderno?", "El Fono Niños 147", "Es la única línea de ayuda que se menciona."),
    ],
    op=("Situación de ejemplo, sin detalles: durante el juego libre, un niño de 4 años dice una frase que a la técnica le preocupa sobre cómo lo trata un adulto, y agrega «no le digas a nadie». Nadie más escuchó. "
        "Escribe: qué le dices al niño; qué anotas; a quién avisas y cuándo; y tres cosas que no haces.",
        "Al niño: «Gracias por contármelo; voy a pedir ayuda a un adulto que sabe cuidarte». Anoto sus palabras exactas y la hora. Aviso de inmediato a la educadora o dirección, que activan las redes de protección según el protocolo. No hago preguntas insistentes, no confronto al adulto y no prometo guardar el secreto ni lo comento con otros.",
        ["escucha con calma y explica con cariño", "anota palabras exactas y avisa de inmediato", "evita investigar, confrontar y prometer secreto"],
        ["hoja con una frase, una anotación, un aviso y tres «no»"],
        ["prometer el secreto", "hacer preguntas insistentes", "hablar con el adulto señalado"],
        "Pregunta: «¿qué harías si la educadora no está?». Debe avisar de inmediato a la dirección o a otro adulto responsable."),
    reinforce="Escribe tres frases de buen trato para poner un límite a un niño que tira los juguetes.",
    extend="Explica por qué la técnica no investiga ni confronta, aunque quiera ayudar.",
)

# ============================================================ OAE-08, clase 5
F = ("Ficha 5 (tres registros de ejemplo de una caída en el patio). Pauta de calidad (1 punto por criterio): P1 fecha y hora; P2 qué ocurrió, con hechos; P3 a quién se avisó y cuándo; P4 sin diagnóstico ni acción por cuenta propia; P5 sin juicios. "
     "Registro A: «Lunes, 10:40, patio. Amaru se cayó al correr y se golpeó la rodilla; lloró. La técnica lo acompañó y avisó a la educadora a las 10:41». Cumple P1 a P5 (5 puntos). "
     "Registro B: «Amaru se cayó y se hizo una herida seria; le puse una crema». Cumple solo P2 (1 punto). Registro C: «Amaru se cayó. Todo bien». Cumple P4 y P5 (2 puntos).")
build(
    O8, 5, F,
    use="Aprenderé a comparar registros y respuestas de la técnica ante un accidente menor, con una pauta de calidad, y a verificar que se avise a tiempo y sin improvisar.",
    prior=["Conozco el registro de accidente.", "Sé que no se da nada por cuenta propia.", "Sé sumar puntos de una pauta."],
    explain=[
        "Para comparar registros se usa una pauta de calidad con cinco criterios: tiene fecha y hora, cuenta con hechos qué ocurrió, dice a quién y cuándo se avisó, no incluye diagnóstico ni acciones por cuenta propia, y no tiene juicios. Se suma un punto por criterio cumplido. El mejor registro es el que cumple todos, porque la educadora y la familia pueden confiar en él.",
        "Verificar la calidad también incluye revisar la conducta de la técnica: acompañar al niño, no dejarlo solo, avisar de inmediato a la educadora o al adulto responsable y, si es grave, a emergencias. No se aplican cremas ni remedios, porque eso podría empeorar la situación y no corresponde a su rol.",
        "Si un registro tiene puntaje bajo, se mejora reescribiéndolo con hechos y los datos que faltan, con la ayuda de la educadora." + LIM,
    ],
    vocab=[("pauta de calidad", "lista de criterios para comparar registros"), ("criterio", "aspecto que se revisa en cada registro"), ("acción por cuenta propia", "hacer algo sin que la educadora lo indique, como aplicar una crema"), ("juicio", "opinión sobre un niño o una situación que no se puede comprobar"), ("reescribir", "volver a escribir un registro con los datos que faltan")],
    worked=[
        ("Calcular el puntaje", "Un registro de ejemplo cumple P1, P2, P3 y P5, pero no P4. ¿Cuántos puntos tiene?", ["Se cuenta un punto por criterio cumplido.", "Son 4."], "4 puntos"),
        ("Mejorar un registro", "Un registro dice: «Se cayó y estaba mal». ¿Qué datos faltan?", ["Faltan la hora, los hechos y a quién se avisó.", "«Estaba mal» es un juicio."], "Hora, hechos y a quién se avisó"),
    ],
    mistakes=[("Escribir «le puse una crema porque no era grave».", "La técnica no aplica productos por cuenta propia y juzga la gravedad.", "Avisa a la educadora y anota solo lo que hizo."),
              ("Escribir «todo bien» como único registro.", "No sirve para saber qué ocurrió ni a quién se avisó.", "Anota los hechos con la hora y el aviso.")],
    T=[
        ("abc", "{F} ¿Qué registro cumple todos los criterios?", "El A", "El B", "El C", "El registro A cumple P1 a P5."),
        ("=", "{F} ¿Cuántos puntos suman los registros B y C juntos?", "1+2", "Se suman los puntos de ambos registros.", " puntos"),
        ("abc", "{F} ¿Qué criterio cumple solo el registro B?", "P2: dice qué ocurrió", "P3: a quién se avisó", "P5: sin juicios", "El registro B cuenta la caída, pero falla en los demás criterios."),
        ("abc", "{F} ¿Por qué el registro B no cumple P4?", "Porque la técnica aplicó una crema por cuenta propia y escribió un juicio sobre la herida", "Porque no tiene fecha", "Porque es muy largo", "Aplicar una crema es una acción por cuenta propia que la técnica no hace."),
        ("abc", "{F} ¿Qué le falta al registro C?", "Fecha y hora, hechos y a quién se avisó", "Un diagnóstico", "Un nombre más largo", "Solo dice que se cayó y que está bien: no cuenta nada concreto."),
        ("=", "{F} ¿Cuántos minutos pasaron entre la caída (10:40) y el aviso a la educadora (10:41) en el registro A?", "(10*60+41)-(10*60+40)", "Se restan las horas del aviso y de la caída, en minutos.", " minuto"),
        ("abc", "{F} Un niño se cae y se golpea la cabeza; la técnica lo acompaña. ¿Qué hace de inmediato?", "Avisa a la educadora o adulto responsable y, si hay una emergencia, a emergencias", "Lo manda a la sala para descansar", "Espera 10 minutos para ver cómo está", "Se avisa de inmediato y no se deja al niño solo."),
        ("abc", "{F} Una compañera propone reescribir B como: «Amaru se cayó. Le sangra la rodilla. Avisé a la educadora a las 10:42». ¿Qué observación corresponde?", "Mejora, pero falta la fecha y el lugar", "Está perfecto", "Es peor que antes", "El nuevo registro cuenta hechos y el aviso, pero aún le falta la fecha y el lugar."),
        ("=", "{F} Si el registro C se reescribe cumpliendo P1, P2 y P3, además de los que ya cumple, ¿cuántos puntos tendría?", "2+3", "Se suman los puntos que ya tiene y los tres nuevos.", " puntos"),
        ("abc", "{F} La educadora le pide a la técnica reescribir el registro B. ¿Qué hace?", "Lo reescribe con hechos, hora y aviso, y le entrega ambas versiones", "Rompe el registro B", "Reescribe sin avisar", "Se conserva el registro original y se agrega la versión corregida."),
        ("abc", "{F} Un niño tiene un golpe y la técnica no sabe si es grave. ¿Qué hace?", "Avisa de inmediato a la educadora o adulto responsable y a emergencias si corresponde", "Decide que no es grave", "Le pone hielo y espera", "La técnica no decide la gravedad; avisa."),
        ("abc", "{F} Otra técnica quiere comentar el accidente en la puerta con otras familias para «prevenir». ¿Qué corresponde?", "No hacerlo: la información la entrega la educadora a la familia del niño", "Hacerlo en voz baja", "Hacerlo con los apoderados más cercanos", "La información de un niño es confidencial."),
        ("=", "{F} El jardín quiere que cada registro sea de 5 puntos. Si hay 12 registros y 9 ya lo son, ¿cuántos faltan por reescribir?", "12-9", "A los registros totales se les restan los que ya cumplen.", " registros"),
    ],
    ctx=("abc", "{F} Al leer el registro A, la educadora pregunta qué hizo la técnica entre la caída y el aviso. ¿Qué responde la técnica?", "Que lo acompañó con calma, no lo dejó solo y avisó a la educadora", "Que lo curó con su botiquín", "Que no recuerda", "Se informa lo que se hizo, sin acciones por cuenta propia."),
    sc=[
        ("En Atención de Párvulos: ¿cuántos puntos da la pauta por criterio?", "Un punto", "Cada criterio cumplido suma un punto."),
        ("¿Aplicas cremas o remedios a un niño?", "No, aviso a la educadora", "La técnica no actúa por cuenta propia."),
        ("¿Qué debe decir un registro de accidente?", "Qué ocurrió, la hora y a quién se avisó", "Así el registro es claro y se puede verificar después."),
    ],
    op=("Dos registros de ejemplo de una caída. Registro X: «Martes, 11:10, sala. Mateo se tropezó con una silla y se golpeó el codo; lloró. La técnica lo acompañó y avisó a la educadora a las 11:11». Registro Y: «Mateo se cayó, se hizo una herida seria. Le di agua con azúcar». Pauta: P1 fecha y hora; P2 hechos; P3 a quién se avisó y cuándo; P4 sin acción por cuenta propia; P5 sin juicios. "
        "Escribe: el puntaje de cada registro con la razón de cada criterio no cumplido; cómo reescribirías Y; y qué harías en el momento si Mateo no deja de llorar.",
        "X cumple P1 a P5: 5 puntos. Y cumple P2 solamente: falta fecha y hora (P1), a quién se avisó (P3), hizo una acción por cuenta propia (P4) y dijo «herida seria», un juicio (P5): 1 punto. Reescritura: «Martes, 11:10, sala. Mateo se cayó y se golpeó el codo; lloró. Avisé a la educadora a las 11:11». Si no deja de llorar: lo acompaño, no lo dejo solo y aviso a la educadora; si es una emergencia, a emergencias.",
        ["asigna bien los puntajes", "explica los criterios no cumplidos", "reescribe con hechos y avisa de inmediato"],
        ["hoja con dos puntajes, un registro reescrito y una acción"],
        ["dar agua con azúcar", "no incluir la hora del aviso", "decir la gravedad"],
        "Pregunta: «¿qué falta en tu reescritura para que sea de 5 puntos?». Debe revisar fecha, hechos, aviso, ninguna acción por cuenta propia y ausencia de juicios."),
    reinforce="Aplica la pauta de cinco criterios a un registro de accidente de ejemplo que inventes.",
    extend="Explica por qué un registro con hechos y hora es útil para la educadora y para la familia.",
)
