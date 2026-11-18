"""Agropecuaria TP 4.º medio, mención Agricultura: OAM-01 (cultivo de especies vegetales) y OAM-02 (poda, raleo y conducción de frutales). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_agag_common import AVISO, EMER, build

O1 = "TP-AGAG-4-OAM-01"
O2 = "TP-AGAG-4-OAM-02"

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Fundo Demo 2» tiene 2 hectáreas de tomates dentro de un invernadero (estructura cubierta con plástico que protege al cultivo del frío) y 10 hectáreas de maíz al aire libre. "
     "Peligros anotados: calor y humedad dentro del invernadero, una estructura y plásticos en altura, un tractor con implementos en el maíz, herramientas manuales, trabajo repetitivo agachado y radiación solar fuerte.")
build(
    O1, 1, F,
    use="Aprenderé qué es cultivar, qué grupos de especies existen, la diferencia entre cultivo al aire libre y en ambiente forzado, y cuáles son los peligros y normas del trabajo de cultivo.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Cultivar es hacer crecer plantas para obtener una cosecha. Las especies se agrupan en hortícolas (como el tomate), frutales (como el manzano), cereales (como el maíz) y cultivos industriales (como la remolacha azucarera, que se procesa en una fábrica). Se cultivan al aire libre, expuestas al clima, o en ambiente forzado, como un invernadero, donde se controla parte del clima. Cada cultivo se maneja según sus características fisiológicas, es decir, cómo funciona la planta y qué necesita para crecer.",
        "El trabajo de cultivo tiene peligros, que son fuentes de daño, y riesgos, que son la posibilidad de ese daño. El calor dentro de un invernadero puede causar un golpe de calor; el trabajo en altura puede causar caídas; el tractor, atrapamientos; y el trabajo repetitivo, dolores de espalda. La jerarquía de controles ordena las medidas: eliminar, sustituir, cambiar el lugar o el equipo (ingeniería), dar reglas y pausas (administrativo) y, al final, el equipo de protección personal (EPP).",
        f"La legislación vigente laboral, sanitaria y ambiental regula el cultivo. Las labores con tractor o en altura las hace personal capacitado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("cultivo hortícola", "cultivo de hortalizas, como el tomate"), ("cultivo frutal", "cultivo de árboles o arbustos que dan fruta, como el manzano"), ("cereal", "planta cuyo grano se cosecha, como el maíz"), ("cultivo industrial", "cultivo cuya cosecha se procesa en una industria, como la remolacha azucarera"), ("invernadero", "estructura cubierta que protege el cultivo y permite controlar parte del clima"), ("ambiente forzado", "ambiente en que se controla parte del clima del cultivo"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Clasificar una especie", "Un fundo de ejemplo cultiva trigo, cuyo grano se cosecha. ¿A qué grupo de especies pertenece?", ["El trigo da granos.", "Las plantas cuyo grano se cosecha son cereales."], "Cereal"),
        ("Clasificar un control", "Un invernadero de ejemplo instala una malla de sombra fija sobre la cubierta para bajar el calor. ¿Qué tipo de control es?", ["La malla cambia físicamente el lugar de trabajo.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que el calor del invernadero se resuelve con beber agua una vez al día.", "El calor intenso exige pausas, sombra y ventilación, no un solo cuidado.", "Se combinan controles de ingeniería, pausas y agua, según la jerarquía."),
              ("Creer que haber leído sobre el cultivo habilita para conducir el tractor del fundo.", "Las labores con maquinaria exigen formación y autorización.", "Aprende aquí el concepto y deja la labor a personal autorizado.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es un invernadero?", "Una estructura cubierta que protege el cultivo y controla parte del clima", "Un campo abierto sembrado con cereales", "Una bodega para guardar maquinaria", "El invernadero es una estructura cubierta; el campo abierto es cultivo al aire libre."),
        ("abc", "En Agropecuaria: ¿qué es un cultivo industrial?", "Un cultivo cuya cosecha se procesa en una industria", "Un cultivo que solo se hace en invernaderos", "Un cultivo de árboles que dan fruta", "El cultivo industrial se procesa en una fábrica; los frutales son otro grupo."),
        ("abc", "En Agropecuaria: ¿qué significa cultivar en ambiente forzado?", "Controlar parte del clima del cultivo, como en un invernadero", "Cultivar sin regar", "Cultivar solo de noche", "Ambiente forzado es controlar parte del clima."),
        ("=", "{F} Entre el tomate y el maíz, ¿cuántas hectáreas totales cultiva el fundo?", "2+10", "Se suman las hectáreas del invernadero y las del aire libre.", " hectáreas"),
        ("abc", "{F} Las ventanas laterales fijas que dejan salir el aire caliente del invernadero son un control de tipo:", "De ingeniería, porque cambian físicamente el lugar", "Administrativo, porque son una regla", "De EPP, porque protegen a quien trabaja", "Las ventanas modifican el invernadero y no dependen de que alguien se acuerde."),
        ("abc", "{F} Una regla que dice «pausas de 10 minutos a la sombra cada hora en el invernadero» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el invernadero", "De sustitución, porque cambia el cultivo", "Una regla de pausas es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al calor y la humedad dentro del invernadero?", "Que una persona sufra un golpe de calor", "El calor mismo dentro del invernadero", "Que el plástico se ensucie", "El riesgo es la posibilidad de daño; el calor es el peligro."),
        ("abc", "{F} Una estudiante dice: «ya aprendí del cultivo, así que puedo conducir el tractor en el maíz». ¿Qué respuesta es correcta?", "Es falso: conducir exige formación, autorización y norma vigente", "Es cierto, si va despacio", "Es cierto, si usa casco", "La velocidad o el casco no reemplazan la autorización."),
        ("abc", "{F} Durante una visita, una persona se desmaya por el calor dentro del invernadero. ¿Qué corresponde según las reglas generales?", "No quedarte, avisar a un adulto responsable y a emergencias", "Entrar a moverla sin saber qué le ocurre", "Esperar a que se despierte sola", "Se avisa a quienes pueden prestar ayuda sin riesgo."),
        ("abc", "En Agropecuaria: ¿por qué el invernadero permite adelantar una cosecha?", "Porque protege al cultivo del frío y controla parte del clima", "Porque elimina la necesidad de regar", "Porque hace crecer la planta sin luz", "La protección del frío permite sembrar antes."),
        ("abc", "{F} Se propone solo entregar sombreros para el calor del invernadero. ¿Qué medida es más efectiva?", "Mejorar la ventilación con aperturas fijas y sombra sobre la cubierta", "Entregar un segundo sombrero", "Pedir que se trabaje más rápido", "Cambiar el invernadero reduce el calor; el sombrero es EPP."),
        ("=", "{F} En el maíz se prepara un promedio de 2 hectáreas por jornada. ¿Cuántas jornadas se necesitan para las hectáreas de maíz?", "10//2", "Se dividen las hectáreas de maíz entre las que se hacen por jornada.", " jornadas"),
        ("abc", "En Agropecuaria: ¿por qué el trabajo repetitivo agachado necesita pausas y cambios de postura?", "Porque puede causar dolores de espalda y lesiones con el tiempo", "Porque el cultivo crece más lento", "Porque el tomate se cae", "El trabajo repetitivo daña la espalda si no se alterna."),
    ],
    ctx=("abc", "Un vecino te ofrece pagarte por manejar su tractor en el cultivo «porque ya sabes de cultivos». ¿Qué respondes?", "Que no, porque exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, en terreno plano", "Que sí, solo un rato", "Conocer del cultivo no habilita para conducir maquinaria."),
    sc=[
        ("En Agropecuaria: ¿qué grupo de especies es el maíz?", "Cereal", "El maíz es una planta cuyo grano se cosecha."),
        ("En el cultivo de especies: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En Agropecuaria: ¿qué es cultivar al aire libre?", "Cultivar expuesto al clima, sin estructura cubierta", "Al aire libre el cultivo queda expuesto al clima."),
    ],
    op=("El «Fundo Demo 3» anota una tarea de ejemplo: cosechar tomates dentro de un invernadero cerrado a las 15 horas de un día de calor, sin sombra ni agua cerca. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a una persona mareada en el invernadero.",
        "(a) Peligro: calor intenso en un invernadero cerrado; riesgo: que una persona sufra un golpe de calor. (b) Una regla de trabajar en las horas más frescas y pausas con agua. (c) Ventanas de ventilación fijas y sombra sobre la cubierta. (d) Aviso a un adulto responsable y a emergencias; no muevo a la persona sin saber qué le pasa.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "avisa a un adulto responsable"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al calor", "proponer solo un sombrero", "no avisar"],
        "Pregunta: «¿qué control cambia el lugar y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Clasifica en hortícola, frutal, cereal o industrial: lechuga, manzano, trigo y remolacha azucarera.",
    extend="Explica con un ejemplo por qué un invernadero puede ser un lugar más peligroso que el aire libre en verano.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (especies de ejemplo, inventada). Tomate: hortícola, una temporada, invernadero, marco de plantación 100 cm entre hileras y 50 cm entre plantas. Manzano: frutal perenne (vive muchos años), aire libre. "
     "Maíz: cereal, una temporada, aire libre, marco 80 cm entre hileras y 25 cm entre plantas. Una hectárea tiene 100.000.000 cm². Documentos: el plan de cultivo (calendario de labores), la ficha técnica de la especie y el registro de labores.")
build(
    O1, 2, F,
    use="Aprenderé la fisiología básica del cultivo (fotosíntesis, transpiración, etapas), el marco de plantación y la densidad, y los documentos y roles del cultivo.",
    prior=["Sé qué es cultivar y qué grupos de especies existen.", "Sé multiplicar y dividir enteros.", "Sé leer una ficha de datos."],
    explain=[
        "La fotosíntesis es el proceso por el que la planta usa luz, agua y dióxido de carbono para fabricar su alimento; la transpiración es la pérdida de agua por las hojas. Las etapas del cultivo son: germinación, crecimiento, floración, formación del fruto o grano y madurez. En un cultivo de una temporada, la planta cumple su ciclo y se cosecha; un frutal perenne vive muchos años y produce cada temporada.",
        "El marco de plantación es la distancia entre hileras y entre plantas. La densidad de plantación es el número de plantas por hectárea: se calcula dividiendo los 100.000.000 cm² de una hectárea por el área que ocupa cada planta, que es la distancia entre hileras por la distancia entre plantas. Una densidad muy alta hace que las plantas compitan por luz y agua; una muy baja desperdicia el terreno.",
        f"El plan de cultivo programa las labores, la ficha técnica describe lo que necesita la especie y el registro de labores anota lo realizado. El jefe de cultivo organiza, el asesor recomienda y los operarios autorizados ejecutan. {EMER} {AVISO}",
    ],
    vocab=[("fotosíntesis", "proceso por el que la planta fabrica su alimento con luz, agua y dióxido de carbono"), ("transpiración", "pérdida de agua de la planta por las hojas"), ("perenne", "planta que vive muchos años"), ("marco de plantación", "distancia entre hileras y entre plantas"), ("densidad de plantación", "número de plantas por hectárea"), ("plan de cultivo", "calendario de labores del cultivo"), ("ficha técnica", "documento que describe lo que necesita una especie")],
    worked=[
        ("Calcular la densidad", "Un marco de ejemplo es de 100 cm entre hileras y 100 cm entre plantas. ¿Cuántas plantas hay por hectárea?", ["Cada planta ocupa 100 por 100, o sea 10.000 cm².", "100.000.000 entre 10.000 es 10.000."], "10.000 plantas por hectárea"),
        ("Etapa del cultivo", "Una planta de ejemplo muestra por primera vez sus flores. ¿En qué etapa está?", ["Las flores aparecen antes de los frutos.", "Esa etapa se llama floración."], "Floración"),
    ],
    mistakes=[("Creer que mientras más plantas por hectárea, siempre mejor.", "Las plantas compiten por luz y agua.", "La densidad se fija según la especie y el asesor."),
              ("Confundir el plan de cultivo con el registro de labores.", "El plan es lo programado y el registro es lo realizado.", "Consulta cada documento para lo que fue hecho.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la fotosíntesis?", "El proceso por el que la planta fabrica su alimento con luz, agua y dióxido de carbono", "La pérdida de agua por las hojas", "El paso de la semilla a la plántula", "La fotosíntesis fabrica alimento; la pérdida de agua es transpiración."),
        ("abc", "En Agropecuaria: ¿qué es una planta perenne?", "Una planta que vive muchos años", "Una planta que vive una sola temporada", "Una planta que no necesita agua", "Perenne significa que vive muchos años."),
        ("abc", "En Agropecuaria: ¿qué es el marco de plantación?", "La distancia entre hileras y entre plantas", "El número de hectáreas del fundo", "El peso de las plantas cosechadas", "El marco describe distancias de plantación."),
        ("=", "{F} ¿Cuántas plantas de tomate hay por hectárea con su marco de plantación?", "100000000//(100*50)", "Se divide el área de una hectárea entre el área que ocupa cada planta.", " plantas"),
        ("=", "{F} ¿Cuántas plantas de maíz hay por hectárea con su marco de plantación?", "100000000//(80*25)", "Se divide el área de una hectárea entre el área que ocupa cada planta.", " plantas"),
        ("abc", "{F} ¿Qué especie de la ficha es perenne?", "El manzano", "El tomate", "El maíz", "La ficha dice que el manzano vive muchos años."),
        ("abc", "{F} ¿Qué especie de la ficha se cultiva en invernadero?", "El tomate", "El maíz", "El manzano", "La ficha asigna el invernadero al tomate."),
        ("abc", "{F} ¿Qué documento programa qué labores se hacen y cuándo?", "El plan de cultivo", "El registro de labores", "La ficha técnica", "El plan programa; el registro anota lo realizado."),
        ("abc", "{F} ¿Qué rol recomienda qué hacer en el cultivo, sin ejecutar las labores?", "El asesor", "El operario autorizado", "El comprador", "El asesor recomienda; el operario ejecuta."),
        ("=", "{F} Se duplica la distancia entre plantas de maíz, de 25 cm a 50 cm, con las hileras igual. ¿Cuántas plantas por hectárea quedan?", "100000000//(80*50)", "Se calcula el nuevo área por planta y se divide la hectárea entre ella.", " plantas"),
        ("abc", "{F} Una compañera dice: «si ponemos el doble de plantas por hectárea, cosechamos el doble». ¿Qué respuesta es correcta?", "Es incorrecto: las plantas compiten por luz y agua y puede rendir menos por planta", "Es cierto, siempre", "Es cierto, si se riega mucho", "Más densidad aumenta la competencia entre plantas por luz y agua."),
        ("abc", "{F} El jefe de cultivo quiere anotar en el registro que se hicieron labores que aún no se hacen «para adelantar». ¿Qué corresponde?", "Rechazarlo: el registro solo anota lo realizado", "Aceptarlo, si después se hacen", "Aceptarlo, si lo firma otra persona", "Anotar lo que no ocurrió falsea el registro."),
        ("abc", "En Agropecuaria: ¿por qué la transpiración importa para decidir el riego?", "Porque la planta pierde agua por las hojas y esa agua debe reponerse", "Porque la planta fabrica más alimento sin agua", "Porque el riego no depende del clima", "La pérdida de agua por las hojas define cuánta agua necesita el cultivo."),
    ],
    ctx=("abc", "Un conocido te pide que le digas, sin conocer su terreno, cuántas plantas debe poner por hectárea. ¿Qué respondes?", "Que depende de la especie y del terreno, y que lo define un asesor", "Que ponga el máximo posible", "Que ponga las que quepan", "La densidad depende de la especie y las condiciones, y la define un asesor."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula la densidad de plantación?", "Una hectárea dividida por el área de cada planta", "La densidad cuenta plantas por hectárea."),
        ("En el trabajo agrícola: ¿qué documento anota lo realizado?", "El registro de labores", "El registro guarda lo que ya se hizo."),
        ("En Agropecuaria: ¿qué es la transpiración?", "La pérdida de agua de la planta por las hojas", "La transpiración es pérdida de agua."),
    ],
    op=("Ficha de ejemplo del «Fundo Demo 4»: lechuga, hortícola de una temporada, marco de 50 cm entre hileras y 25 cm entre plantas; una hectárea tiene 100.000.000 cm². Escribe (a) el área que ocupa cada planta, (b) cuántas plantas hay por hectárea, (c) qué documento programa las labores, (d) qué rol recomienda y cuál ejecuta.",
        "(a) 50 × 25 = 1.250 cm². (b) 100.000.000 ÷ 1.250 = 80.000 plantas. (c) El plan de cultivo. (d) Recomienda el asesor y ejecuta el operario autorizado.",
        ["calcula el área por planta", "calcula la densidad", "nombra el documento", "distingue asesor y operario"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar las distancias", "confundir plan con registro"],
        "Pregunta: «¿cuántos cm² ocupa cada planta?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Calcula las plantas por hectárea de un marco inventado de 100 cm entre hileras y 20 cm entre plantas.",
    extend="Explica con un ejemplo por qué un frutal perenne se maneja distinto de un cultivo de una temporada.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). El «Fundo Demo 2» evalúa dónde producir 1 hectárea de tomate para cosechar temprano. En la zona hay 12 días de heladas (temperatura bajo 0 grados) en primavera, y el tomate no tolera las heladas. "
     "Opción A: aire libre, costo bajo; la cosecha sería normal, con riesgo de perder plantas por heladas. Opción B: invernadero, costo alto; protege de heladas y adelanta la cosecha, pero exige ventilar para evitar calor excesivo y hongos por humedad.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un caso de cultivo en papel, comparando condiciones del terreno y del clima con las necesidades de la planta, y a justificar con dos evidencias una decisión.",
    prior=["Sé qué es el ambiente forzado.", "Sé qué es la fisiología básica del cultivo.", "Sé leer una ficha con datos."],
    explain=[
        "Para analizar un caso de cultivo se leen las condiciones del lugar: clima, heladas, suelo y agua. Luego se comparan con lo que necesita la planta, que se encuentra en su ficha técnica. Una helada es una baja de temperatura bajo 0 grados que puede quemar tejidos de plantas sensibles. Un ambiente forzado puede evitarlas, pero trae nuevos riesgos: calor excesivo y humedad alta que favorecen hongos.",
        "Una buena decisión de cultivo nombra la opción, cita dos evidencias del caso y dice qué riesgos quedan y cómo se vigilan. No hay una opción mejor para todos: depende de la especie, del presupuesto y del mercado. La decisión final la toma el asesor con el jefe de cultivo; quien analiza en papel prepara la información.",
        f"Cualquier labor de implementación, como armar estructuras o aplicar productos, la hace personal capacitado. {EMER} {AVISO}",
    ],
    vocab=[("helada", "baja de temperatura bajo 0 grados que daña a plantas sensibles"), ("ficha técnica", "documento que describe lo que necesita una especie"), ("ventilar", "renovar el aire de un lugar cerrado"), ("hongo", "microorganismo que causa enfermedades de las plantas"), ("evidencia", "dato del caso que respalda una decisión"), ("riesgo residual", "riesgo que queda aunque se tome una medida")],
    worked=[
        ("Relacionar clima y planta", "Una planta de ejemplo no tolera heladas y en la zona hay muchas en primavera. ¿Qué riesgo corre al aire libre?", ["Las heladas dañan a las plantas sensibles.", "Podría perder plantas."], "Perder plantas por heladas"),
        ("Riesgo residual", "Un invernadero de ejemplo evita heladas pero se calienta mucho en verano. ¿Qué riesgo queda?", ["El invernadero protege del frío.", "Pero puede generar calor excesivo."], "Calor excesivo y humedad"),
    ],
    mistakes=[("Elegir el invernadero siempre porque «protege más».", "También trae calor, humedad y mayor costo.", "Se comparan costos, riesgos y beneficios con dos evidencias."),
              ("Dar una conclusión sin citar evidencia del caso.", "Sin dato del caso la decisión no se puede verificar.", "Cita al menos dos evidencias.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es una helada?", "Una baja de temperatura bajo 0 grados que daña a plantas sensibles", "Una lluvia muy fuerte", "Una temperatura de 40 grados", "La helada es frío intenso, bajo 0 grados."),
        ("abc", "En Agropecuaria: ¿qué es ventilar un invernadero?", "Renovar el aire del lugar cerrado", "Cubrir el invernadero con plástico", "Regar las plantas", "Ventilar renueva el aire y baja el calor y la humedad."),
        ("abc", "En Agropecuaria: ¿qué es el riesgo residual?", "El riesgo que queda aunque se tome una medida", "El riesgo que se eliminó", "El riesgo de otro predio", "El riesgo residual persiste después de aplicar la medida."),
        ("abc", "{F} ¿Qué evidencia de la ficha indica que el tomate corre riesgo al aire libre?", "Hay 12 días de heladas y el tomate no las tolera", "El costo del aire libre es bajo", "La cosecha sería normal", "Las heladas dañan al tomate, que no las tolera."),
        ("abc", "{F} ¿Qué beneficio tiene la Opción B según la ficha?", "Protege de heladas y adelanta la cosecha", "Tiene el costo más bajo", "No exige vigilar el clima", "La ficha atribuye esos beneficios al invernadero."),
        ("abc", "{F} ¿Qué riesgo trae la Opción B según la ficha?", "Calor excesivo y hongos por humedad", "Heladas", "Costo bajo", "El invernadero exige ventilar para evitar calor y hongos."),
        ("=", "{F} Si cada día de helada se pierden 5 plantas del cultivo al aire libre, ¿cuántas plantas se perderían en los 12 días?", "12*5", "Se multiplican los días de helada por las plantas que se pierden cada día.", " plantas"),
        ("abc", "{F} Si el presupuesto es muy bajo, ¿qué opción conviene analizar y con qué precaución?", "La A, con medidas para vigilar las heladas, según indique el asesor", "La B, aunque no alcance el dinero", "Ninguna, porque no se puede cultivar", "El presupuesto limita la opción B; se analiza A con vigilancia."),
        ("abc", "{F} Una compañera dice: «con el invernadero ya no hay ningún riesgo». ¿Qué respuesta es correcta?", "Es incorrecto: quedan el calor excesivo y la humedad", "Es correcto, porque el plástico lo evita todo", "Es correcto, si es nuevo", "Todo ambiente forzado deja un riesgo residual."),
        ("abc", "{F} El jefe de cultivo quiere cerrar todas las ventanas del invernadero un día de calor para «guardar el calor». ¿Qué corresponde?", "Rechazarlo: hay que ventilar para evitar calor excesivo y hongos", "Aceptarlo, porque el calor ayuda siempre", "Aceptarlo, si es de noche", "Un invernadero cerrado puede pasar de la temperatura segura."),
        ("=", "{F} Un invernadero de ejemplo tiene 20 ventanas y se abren 15. ¿Qué porcentaje de ventanas está abierto?", "15*100//20", "Se dividen las ventanas abiertas entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Quién toma la decisión final entre las opciones A y B?", "El asesor con el jefe de cultivo", "Un estudiante con la ficha", "El comprador del tomate", "La decisión final la toma quien tiene la formación y la responsabilidad."),
        ("abc", "En Agropecuaria: ¿por qué conviene citar dos evidencias al justificar una decisión?", "Porque otra persona puede verificar de dónde salió", "Porque así la decisión se hace más corta", "Porque las evidencias reemplazan al asesor", "Citar evidencias permite revisar la decisión."),
    ],
    ctx=("abc", "Un conocido te pide que decidas por él si construye un invernadero, sin darte datos de costos ni de clima. ¿Qué respondes?", "Que faltan datos y que la decisión la toma un asesor con él", "Que lo construya, porque protege", "Que no lo construya, porque cuesta", "Sin datos del clima y del presupuesto no hay decisión fundada."),
    sc=[
        ("En Agropecuaria: ¿qué riesgo evita un invernadero?", "Las heladas", "El invernadero protege del frío intenso."),
        ("En el trabajo agrícola: ¿qué riesgo trae un invernadero cerrado?", "Calor excesivo y humedad alta", "Esas condiciones favorecen hongos y golpes de calor."),
        ("En Agropecuaria: ¿qué se cita al justificar una decisión?", "Dos evidencias del caso", "Dos evidencias hacen verificable la decisión."),
    ],
    op=("Caso de ejemplo del «Fundo Demo 5»: se evalúa cultivar lechuga en 1 hectárea. Dato: hay 8 días de heladas en invierno y la lechuga tolera heladas leves pero no fuertes. Opción A: aire libre, costo bajo. Opción B: invernadero, costo alto, exige ventilar. Escribe (a) una evidencia a favor de B, (b) una evidencia a favor de A, (c) un riesgo residual de B, (d) quién decide.",
        "(a) La lechuga no tolera heladas fuertes y hay 8 días de heladas. (b) El costo de A es bajo y la lechuga tolera heladas leves. (c) Calor excesivo y humedad alta si no se ventila. (d) El asesor con el jefe de cultivo.",
        ["cita una evidencia a favor de B", "cita una evidencia a favor de A", "nombra un riesgo residual", "nombra quién decide"],
        ["hoja con las cuatro respuestas"],
        ["no citar datos del caso", "decir que B no tiene riesgos"],
        "Pregunta: «¿qué dato del caso se refiere al frío y qué dato al costo?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Escribe una planta inventada sensible al frío y una medida conceptual para protegerla, con su riesgo residual.",
    extend="Explica con un ejemplo por qué el costo no puede ser el único criterio para decidir el ambiente de cultivo.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Comparación para 1 hectárea de tomate. Aire libre: rendimiento 40.000 kg, precio de ejemplo $300 por kilo, costo $5.000.000. "
     "Invernadero: rendimiento 100.000 kg, precio de ejemplo $500 por kilo (cosecha temprana), costo $30.000.000.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular ingreso, margen y costo por kilo para comparar dos formas de cultivar la misma especie.",
    prior=["Sé qué es el rendimiento.", "Sé multiplicar y dividir enteros.", "Sé restar enteros."],
    explain=[
        "El ingreso se calcula multiplicando los kilos cosechados por el precio de cada kilo. El margen es el ingreso menos el costo. El costo por kilo se obtiene dividiendo el costo total entre los kilos cosechados. Con estos tres números se comparan dos formas de cultivar: la que tiene mayor margen deja más dinero, y la que tiene menor costo por kilo produce más barato.",
        "Un margen mayor no siempre significa mejor decisión. Una inversión alta exige tener el dinero, y un riesgo mayor puede perder todo si algo falla. Por eso los cálculos se acompañan de una lectura crítica: qué supuestos tiene el cálculo (precio, rendimiento), qué pasa si cambian y qué riesgos quedan. Todos los valores de esta clase son de ejemplo y la decisión final la toma el asesor.",
        f"El cálculo no reemplaza el criterio de seguridad ni la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("ingreso", "kilos cosechados por el precio de cada kilo"), ("margen", "ingreso menos costo"), ("costo por kilo", "costo total entre los kilos cosechados"), ("supuesto", "dato que se acepta como verdadero para hacer un cálculo"), ("inversión", "dinero que hay que poner antes de cosechar")],
    worked=[
        ("Ingreso y margen", "Un cultivo de ejemplo rinde 10.000 kg a $200 el kilo y cuesta $1.500.000. ¿Cuál es el margen?", ["Ingreso: 10.000 por 200 es 2.000.000.", "Margen: 2.000.000 menos 1.500.000."], "$500.000"),
        ("Costo por kilo", "Con el mismo cultivo, ¿cuál es el costo por kilo?", ["Se divide el costo entre los kilos.", "1.500.000 entre 10.000 es 150."], "$150 por kilo"),
    ],
    mistakes=[("Elegir la opción de mayor margen sin mirar si hay dinero para la inversión.", "Una inversión alta puede ser imposible de cubrir.", "Se compara también la inversión y el riesgo."),
              ("Olvidar que el precio de ejemplo puede cambiar.", "El margen depende del precio supuesto.", "Se prueba qué pasa si el precio baja.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es el ingreso de un cultivo?", "Los kilos cosechados por el precio de cada kilo", "El costo total del cultivo", "La superficie del terreno", "El ingreso multiplica producción y precio."),
        ("abc", "En Agropecuaria: ¿qué es el costo por kilo?", "El costo total entre los kilos cosechados", "El precio de venta de cada kilo", "El costo de una hectárea", "El costo por kilo relaciona costo y producción."),
        ("abc", "En Agropecuaria: ¿qué es un supuesto en un cálculo?", "Un dato que se acepta como verdadero para calcular", "Un resultado comprobado", "Un error del cálculo", "El supuesto es un dato aceptado, como el precio."),
        ("=", "{F} ¿Cuál es el ingreso al aire libre?", "40000*300", "Se multiplican los kilos por el precio de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuál es el ingreso en el invernadero?", "100000*500", "Se multiplican los kilos por el precio de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuál es el margen al aire libre?", "40000*300-5000000", "Se resta el costo al ingreso.", " pesos"),
        ("=", "{F} ¿Cuál es el margen en el invernadero?", "100000*500-30000000", "Se resta el costo al ingreso.", " pesos"),
        ("=", "{F} ¿Cuál es el costo por kilo al aire libre?", "5000000//40000", "Se divide el costo total entre los kilos cosechados.", " pesos"),
        ("=", "{F} ¿Cuál es el costo por kilo en el invernadero?", "30000000//100000", "Se divide el costo total entre los kilos cosechados.", " pesos"),
        ("abc", "{F} ¿Qué opción produce más barato, medido por costo por kilo?", "El aire libre", "El invernadero", "Ambas cuestan igual", "Al aire libre cuesta 125 pesos por kilo y en invernadero 300."),
        ("abc", "{F} ¿Qué opción deja más margen?", "El invernadero", "El aire libre", "Ambas dejan igual margen", "El invernadero deja 20.000.000 y el aire libre 7.000.000."),
        ("=", "{F} Si el precio del invernadero bajara a $350 por kilo, ¿cuál sería su margen?", "100000*350-30000000", "Se calcula el ingreso con el nuevo precio y se resta el costo.", " pesos"),
        ("abc", "En Agropecuaria: ¿por qué conviene probar el cálculo con otro precio?", "Porque el precio es un supuesto que puede cambiar el resultado", "Porque el costo siempre es el mismo", "Porque el rendimiento no importa", "Un cambio de precio puede cambiar la mejor opción."),
    ],
    ctx=("abc", "Un conocido te dice que construirá un invernadero «porque deja más margen» y te pide confirmar. ¿Qué respondes?", "Que además del margen hay que mirar la inversión, el riesgo y los supuestos con un asesor", "Que sí, siempre conviene", "Que no, nunca conviene", "El margen es un criterio entre varios."),
    sc=[
        ("En un cultivo de tomate: ¿cómo se calcula el margen de una hectárea?", "Ingreso menos costo", "El margen es lo que queda tras pagar el costo."),
        ("En el trabajo agrícola: ¿qué es el ingreso?", "Kilos por precio", "El ingreso multiplica producción y precio."),
        ("En Agropecuaria: ¿qué hace falta probar en un cálculo?", "Qué pasa si cambian los supuestos", "Un cálculo depende de sus supuestos."),
    ],
    op=("Datos de ejemplo del «Fundo Demo 6»: 1 hectárea de lechuga. Aire libre: 20.000 kg, precio $200 por kilo, costo $2.000.000. Invernadero: 50.000 kg, precio $300 por kilo, costo $9.000.000. Escribe (a) el margen de cada opción, (b) el costo por kilo de cada una, (c) cuál tiene mayor margen y cuál produce más barato, (d) un supuesto que habría que probar.",
        "(a) Aire libre: 20.000 × 200 − 2.000.000 = $2.000.000; invernadero: 50.000 × 300 − 9.000.000 = $6.000.000. (b) Aire libre: 2.000.000 ÷ 20.000 = $100; invernadero: 9.000.000 ÷ 50.000 = $180. (c) Mayor margen: invernadero; más barato: aire libre. (d) El precio: qué pasa si baja.",
        ["calcula los márgenes", "calcula los costos por kilo", "compara correctamente", "nombra un supuesto"],
        ["hoja con las cuatro respuestas"],
        ["no restar el costo", "confundir margen con costo por kilo"],
        "Pregunta: «¿qué se resta al ingreso para obtener el margen?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el margen de un cultivo inventado de 8.000 kg a $250 el kilo con un costo de $1.200.000.",
    extend="Explica con un ejemplo por qué un margen alto no garantiza una buena decisión.",
)

# ============================================================ OAM-01, clase 5
F = ("Ficha 5 (comparación y control de ejemplo, inventada). El «Fundo Demo 2» compara tres variedades de maíz con puntaje de ejemplo de 1 a 5 (5 es lo mejor). Variedad X: rendimiento 4, tolerancia al frío 2, costo de semilla 5. "
     "Variedad Y: rendimiento 3, tolerancia al frío 4, costo de semilla 3. Variedad Z: rendimiento 5, tolerancia al frío 3, costo de semilla 2. "
     "Control de la emergencia: plantas emergidas por metro de hilera en 5 puntos revisados: 8, 9, 7, 8 y 8. Meta de ejemplo: al menos 8 plantas por metro en promedio y ningún punto bajo 7.")
build(
    O1, 5, F,
    use="Aprenderé a comparar alternativas de cultivo con una matriz de puntajes y a verificar la calidad de la emergencia con un promedio y una meta, sin ejecutar ninguna labor.",
    prior=["Sé calcular promedios de enteros.", "Sé qué es la densidad de plantación.", "Sé sumar enteros."],
    explain=[
        "Comparar variedades exige varios criterios: rendimiento, tolerancia al clima, costo de semilla y otros. En la matriz, cada variedad recibe un puntaje por criterio y se suman los puntajes. Gana la de mayor total, pero se revisa que ningún criterio crítico, como la tolerancia al frío en una zona con heladas, quede muy bajo. Si hay empate, se prioriza el criterio más importante para el fundo.",
        "La emergencia es el nacimiento de las plántulas después de sembrar. Se verifica contando las plantas emergidas por metro de hilera en varios puntos. El promedio es la suma dividida por el número de puntos, y se compara con una meta. Un punto muy bajo señala un problema local, como mala siembra o suelo compactado, aunque el promedio cumpla. Se registra tal cual y se informa; no se corrige el dato.",
        f"El conteo en terreno y las correcciones las hace personal capacitado; aquí se interpretan datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("variedad", "grupo de plantas de una especie con características propias"), ("matriz de comparación", "tabla con criterios y puntajes para comparar alternativas"), ("emergencia", "nacimiento de las plántulas después de sembrar"), ("meta", "valor que se espera alcanzar"), ("promedio", "suma de valores dividida por la cantidad de valores"), ("punto crítico", "criterio que no puede quedar muy bajo")],
    worked=[
        ("Sumar puntajes", "Una variedad de ejemplo obtiene 3 en rendimiento, 5 en tolerancia al frío y 2 en costo. ¿Cuál es su total?", ["Se suman los tres puntajes.", "3 más 5 más 2."], "10 puntos"),
        ("Promedio de emergencia", "Se contaron 6, 10 y 8 plantas por metro en tres puntos de ejemplo. ¿Cuál es el promedio?", ["Se suman: 6 más 10 más 8 es 24.", "24 entre 3."], "8 plantas por metro"),
    ],
    mistakes=[("Elegir la variedad de mayor rendimiento aunque tolere mal el frío en una zona con heladas.", "Un punto crítico muy bajo puede perder el cultivo.", "Se revisa que ningún criterio crítico quede muy bajo."),
              ("Ignorar un punto bajo porque el promedio cumple.", "Un punto bajo señala un problema local.", "Se registra y se informa el punto bajo.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la emergencia de un cultivo?", "El nacimiento de las plántulas después de sembrar", "La cosecha de los primeros frutos", "La limpieza del terreno", "La emergencia ocurre después de sembrar."),
        ("abc", "En Agropecuaria: ¿qué es un punto crítico en una matriz de comparación?", "Un criterio que no puede quedar muy bajo", "El criterio con el puntaje más alto", "La fila con el nombre de la variedad", "El punto crítico es un criterio que no puede fallar."),
        ("abc", "En Agropecuaria: ¿qué indica un punto con muy pocas plantas emergidas?", "Un posible problema local, como mala siembra o suelo compactado", "Que todo el cultivo está perdido", "Que la variedad es la mejor", "Un punto bajo señala un problema local."),
        ("=", "{F} ¿Cuál es el total de puntaje de la variedad X?", "4+2+5", "Se suman sus puntajes de rendimiento, tolerancia al frío y costo de semilla.", " puntos"),
        ("=", "{F} ¿Cuál es el total de puntaje de la variedad Y?", "3+4+3", "Se suman sus puntajes de rendimiento, tolerancia al frío y costo de semilla.", " puntos"),
        ("=", "{F} ¿Cuál es el total de puntaje de la variedad Z?", "5+3+2", "Se suman sus puntajes de rendimiento, tolerancia al frío y costo de semilla.", " puntos"),
        ("abc", "{F} ¿Qué variedad tiene el mayor total?", "La variedad X, con 11 puntos", "La variedad Y, con 10 puntos", "La variedad Z, con 10 puntos", "X suma 11, más que Y y que Z, que suman 10 cada una."),
        ("=", "{F} ¿Cuál es el promedio de plantas emergidas por metro en los 5 puntos?", "(8+9+7+8+8)//5", "Se suman los conteos y se divide entre los 5 puntos.", " plantas por metro"),
        ("abc", "{F} ¿Se cumple la meta de ejemplo?", "Sí, porque el promedio es 8 y ningún punto baja de 7", "No, porque un punto tiene 7", "No, porque el promedio es menor que 8", "El promedio es 8 y el punto más bajo es 7, que no está bajo 7."),
        ("abc", "{F} Una compañera dice: «la variedad Z es la mejor, tiene el rendimiento más alto». ¿Qué respuesta es correcta?", "Es incompleto: hay que sumar todos los criterios y ver los críticos", "Es correcto, porque el rendimiento es lo único que cuenta", "Es correcto, si cuesta poco", "Se comparan todos los criterios, no solo uno."),
        ("abc", "{F} El jefe de cultivo quiere cambiar el conteo de 7 a 8 en un punto para que se vea mejor. ¿Qué corresponde?", "Rechazarlo: se registra el dato real", "Aceptarlo, porque el promedio ya cumple", "Aceptarlo, si lo firma otra persona", "Cambiar un dato falsea el registro."),
        ("abc", "{F} Si en la zona hay heladas fuertes, ¿qué variedad tiene la mayor tolerancia al frío?", "Y, con puntaje 4", "X, con puntaje 2", "Z, con puntaje 3", "La variedad Y tiene el puntaje más alto en tolerancia al frío."),
        ("abc", "En Agropecuaria: ¿por qué se verifica la emergencia con varios puntos y no con uno solo?", "Porque un solo punto puede no representar a todo el lote", "Porque contar uno cuesta más", "Porque el promedio no existe", "Varios puntos reflejan mejor el lote completo."),
    ],
    ctx=("abc", "Un conocido te pide que le elijas una variedad solo por su rendimiento y la siembre mañana. ¿Qué respondes?", "Que se comparan varios criterios y que la decisión final es del asesor", "Que elija la de mayor rendimiento", "Que elija la más barata", "La comparación debe considerar todos los criterios, en especial los críticos."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula el total de una variedad?", "Sumando sus puntajes", "El total suma los puntajes de cada criterio."),
        ("En el trabajo agrícola: ¿qué se hace con un punto bajo de emergencia?", "Se registra y se informa", "Informar el punto bajo permite buscar la causa del problema."),
        ("En la emergencia del maíz: ¿cómo se calcula el promedio de cinco puntos?", "Sumándolos y dividiendo entre 5", "El promedio resume los conteos en un solo número."),
    ],
    op=("Datos de ejemplo del «Fundo Demo 7»: tres variedades. P: rendimiento 5, tolerancia al frío 1, costo 3. Q: rendimiento 3, tolerancia al frío 5, costo 4. R: rendimiento 4, tolerancia al frío 3, costo 3. Emergencia en 4 puntos: 6, 8, 9 y 9 plantas por metro; meta de ejemplo: promedio de al menos 8 y ningún punto bajo 7. Escribe (a) el total de cada variedad, (b) cuál es la mayor, (c) el promedio de emergencia, (d) si se cumple la meta y qué haces con el punto bajo.",
        "(a) P: 5 + 1 + 3 = 9; Q: 3 + 5 + 4 = 12; R: 4 + 3 + 3 = 10. (b) Q. (c) (6 + 8 + 9 + 9) ÷ 4 = 8. (d) El promedio cumple, pero el punto de 6 está bajo 7: no se cumple la meta completa; se registra e informa.",
        ["suma bien los totales", "elige la mayor", "calcula el promedio", "concluye bien sobre la meta"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal", "decir que cumple porque el promedio es 8", "cambiar el dato"],
        "Pregunta: «¿qué punto está bajo 7?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Crea una matriz con dos variedades y tres criterios inventados, suma los totales y elige una.",
    extend="Explica con un ejemplo por qué un punto crítico muy bajo puede descartar una alternativa de alto total.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Huerto Demo» es un predio ficticio con 3 hectáreas de manzanos, a razón de 1.000 árboles por hectárea. "
     "Peligros anotados: escaleras y plataformas para llegar a las ramas altas (trabajo en altura), tijeras y serruchos muy afilados, ramas que caen, posturas con los brazos sobre la cabeza durante horas, picaduras de insectos y sol fuerte. Una escalera se apoya sobre suelo blando.")
build(
    O2, 1, F,
    use="Aprenderé qué son la poda, el raleo y la conducción de frutales, y cuáles son los peligros del trabajo en altura y con herramientas cortantes.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Un frutal es un árbol o arbusto que da fruta. La poda es cortar partes del árbol, como ramas, para darle forma y equilibrar el crecimiento con la producción. El raleo es quitar frutos en exceso para que los que quedan crezcan más grandes y de mejor calidad. La conducción es guiar el crecimiento del árbol con una forma y soportes, como alambres. Estas labores se hacen según la especie, el propósito productivo, el sistema de producción y el clima.",
        "Estas labores tienen peligros: el trabajo en altura puede causar caídas; las herramientas cortantes, cortes; las ramas que caen, golpes; y las posturas forzadas, dolores de cuello y hombros. La jerarquía de controles ordena las medidas: eliminar el peligro, sustituirlo, cambiar el lugar o el equipo (por ejemplo, una plataforma con barandas), dar reglas y capacitación y, al final, el equipo de protección personal (EPP), como el arnés.",
        f"Una escalera apoyada en suelo blando es peligrosa. El trabajo en altura lo hace solo personal capacitado y autorizado, bajo la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("frutal", "árbol o arbusto que da fruta"), ("poda", "corte de partes del árbol para darle forma y equilibrio"), ("raleo", "retiro de frutos en exceso para que los que quedan crezcan más"), ("conducción", "guía del crecimiento del árbol con una forma y soportes"), ("trabajo en altura", "trabajo en que existe riesgo de caer desde una altura"), ("plataforma", "superficie elevada y estable desde la que se trabaja"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Distinguir poda y raleo", "En un huerto de ejemplo se quitan frutos pequeños de un árbol para que los demás crezcan más. ¿Es poda o raleo?", ["Lo que se quita son frutos.", "Quitar frutos en exceso es raleo."], "Raleo"),
        ("Clasificar un control", "Un huerto de ejemplo nivela y afirma el suelo blando del pasillo donde se trabaja. ¿Qué tipo de control es?", ["Cambia físicamente el lugar de trabajo.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que una escalera es segura si se apoya «en cualquier lado».", "Una superficie blanda hace resbalar la escalera.", "El trabajo en altura lo hace personal capacitado, con equipos adecuados."),
              ("Creer que leer sobre poda habilita para usar un serrucho o tijeras.", "Las herramientas cortantes exigen formación y autorización.", "Aprende aquí el concepto y deja el corte a personal autorizado.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la poda de un frutal?", "El corte de partes del árbol para darle forma y equilibrio", "El retiro de frutos en exceso", "El riego del árbol en verano", "La poda corta partes del árbol; el retiro de frutos es raleo."),
        ("abc", "En Agropecuaria: ¿qué es el raleo de un frutal?", "El retiro de frutos en exceso para que los demás crezcan más", "El corte de ramas para dar forma", "La guía del árbol con alambres", "El raleo trabaja sobre los frutos, no sobre las ramas."),
        ("abc", "En Agropecuaria: ¿qué es la conducción de un frutal?", "La guía de su crecimiento con una forma y soportes", "La cosecha de la fruta", "El traslado del árbol a otro lugar", "La conducción da forma al árbol con soportes."),
        ("=", "{F} ¿Cuántos árboles tiene el huerto en total?", "3*1000", "Se multiplican las hectáreas por los árboles de cada hectárea.", " árboles"),
        ("abc", "{F} Una plataforma con barandas en vez de escaleras es un control de tipo:", "De ingeniería, porque cambia el equipo y el lugar de trabajo", "Administrativo, porque es una regla", "De EPP, porque protege a quien trabaja", "La plataforma modifica el lugar y no depende de que alguien se acuerde."),
        ("abc", "{F} Una regla que dice «no se trabaja en altura con viento fuerte» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el árbol", "De sustitución, porque cambia la herramienta", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a la escalera sobre suelo blando?", "Que resbale, la persona caiga y se lastime", "La escalera misma", "Que el árbol crezca más alto", "El riesgo es la posibilidad de daño; el suelo blando es el peligro."),
        ("abc", "{F} Una estudiante dice: «ya entendí cómo se poda, así que me subo a la escalera y poda un árbol». ¿Qué respuesta es correcta?", "Es peligroso: el trabajo en altura y con herramientas cortantes lo hace personal capacitado y autorizado", "Es correcto, si la escalera es nueva", "Es correcto, si hay alguien mirando", "Una escalera nueva o un observador no reemplazan la capacitación."),
        ("abc", "{F} En una visita, una persona cae de una escalera y no se mueve. ¿Qué corresponde según las reglas generales?", "No moverla, avisar a un adulto responsable y a emergencias", "Levantarla para que se siente", "Tirarle agua en la cara", "Moverla puede agravar una lesión; se avisa a quienes pueden ayudar."),
        ("abc", "En Agropecuaria: ¿por qué las posturas con los brazos sobre la cabeza necesitan pausas?", "Porque pueden causar dolores de cuello y hombros con el tiempo", "Porque el árbol crece más lento", "Porque las tijeras se desafilan", "El trabajo con los brazos elevados cansa y lesiona."),
        ("abc", "{F} Se propone solo entregar arneses para el trabajo en altura. ¿Qué medida es más efectiva en la jerarquía?", "Usar plataformas con barandas que evitan la caída", "Entregar un segundo arnés", "Pedir a cada persona que tenga cuidado", "Evitar la caída está más arriba que el EPP."),
        ("=", "{F} Un podador capacitado de ejemplo atiende 40 árboles por jornada. ¿Cuántas jornadas se necesitan para los árboles del huerto?", "3*1000//40", "Se dividen los árboles totales entre los árboles por jornada.", " jornadas"),
        ("abc", "En Agropecuaria: ¿por qué las herramientas cortantes de poda se guardan con funda y bajo control de personal autorizado?", "Porque así se evitan cortes y el uso por personas no autorizadas", "Porque así pesan menos", "Porque no necesitan registro", "Guardarlas con funda y bajo control previene cortes y usos indebidos."),
    ],
    ctx=("abc", "Un vecino te ofrece pagarte por podar sus manzanos desde una escalera «porque ya sabes cómo se hace». ¿Qué respondes?", "Que no, porque exige formación, equipos y autorización, y que lo consultarás con un adulto responsable", "Que sí, con una escalera firme", "Que sí, si son pocos árboles", "Conocer el concepto no habilita para trabajar en altura."),
    sc=[
        ("En Agropecuaria: ¿qué es el raleo?", "Quitar frutos en exceso para que los demás crezcan más", "El raleo mejora el tamaño de los frutos que quedan."),
        ("En la poda de frutales: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En Agropecuaria: ¿qué es el trabajo en altura?", "Un trabajo en que existe riesgo de caer", "El peligro principal es la caída."),
    ],
    op=("El «Huerto Demo 2» anota una tarea de ejemplo: podar ramas altas desde una escalera apoyada en un suelo blando, con una persona sujetándola y sin arnés. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si alguien cae y no se mueve.",
        "(a) Peligro: escalera sobre suelo blando; riesgo: que resbale, la persona caiga y se lastime. (b) Una regla de no trabajar en altura sin capacitación y con viento fuerte. (c) Una plataforma con barandas sobre una superficie firme. (d) No la muevo, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no mueve a la persona y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer solo un arnés", "mover a la persona"],
        "Pregunta: «¿qué control evita la caída aunque nadie se acuerde de la regla?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres labores de un huerto frutal y clasifícalas como poda, raleo o conducción.",
    extend="Explica con un ejemplo por qué una plataforma con barandas es mejor que una escalera.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 2 (datos de ejemplo, inventados). Cuartel 1 del «Huerto Demo»: 2 hectáreas, 1.000 árboles por hectárea, árboles de 6 años, conducción en eje central (un tronco central con ramas laterales). Cuartel 2: 1 hectárea, 800 árboles por hectárea, conducción en parrón (estructura alta de postes y alambres). "
     "Carga de ejemplo: un árbol tiene 400 frutos sin raleo y la meta de ejemplo es 250 frutos por árbol después del raleo. Documentos: el plan de poda (qué, dónde y cuándo), el registro de labores y la ficha de la variedad.")
build(
    O2, 2, F,
    use="Aprenderé los tipos de poda, los sistemas de conducción, el concepto de carga frutal y los documentos y roles de la poda, el raleo y la conducción.",
    prior=["Sé qué son poda, raleo y conducción.", "Sé multiplicar y dividir enteros.", "Sé leer una ficha de datos."],
    explain=[
        "Hay tipos de poda según el objetivo. La poda de formación se hace en árboles jóvenes para darles la forma deseada. La poda de producción se hace en árboles adultos para equilibrar el crecimiento y la fruta. La poda de renovación se hace para reemplazar ramas viejas. Los sistemas de conducción dan forma al árbol: el eje central tiene un tronco con ramas laterales, la espaldera usa alambres en hilera y el parrón usa una estructura alta de postes y alambres.",
        "La carga frutal es la cantidad de frutos que lleva un árbol. Muchos frutos dan una fruta pequeña; pocos, una fruta grande pero menos kilos. El calibre es el tamaño de la fruta. El raleo ajusta la carga para lograr un calibre adecuado. Los documentos son el plan de poda, el registro de labores y la ficha de la variedad. El jefe de huerto organiza, el capataz supervisa y los podadores capacitados ejecutan; el asesor recomienda.",
        f"Un registro anota la labor realizada y cuántos árboles se trabajaron, sin alterar los datos. {EMER} {AVISO}",
    ],
    vocab=[("poda de formación", "poda de árboles jóvenes para darles forma"), ("poda de producción", "poda de árboles adultos para equilibrar crecimiento y fruta"), ("eje central", "sistema con un tronco central y ramas laterales"), ("parrón", "sistema con estructura alta de postes y alambres"), ("carga frutal", "cantidad de frutos que lleva un árbol"), ("calibre", "tamaño de la fruta"), ("plan de poda", "documento que dice qué podar, dónde y cuándo")],
    worked=[
        ("Elegir el tipo de poda", "En un huerto de ejemplo hay árboles de 2 años que aún no tienen forma definida. ¿Qué poda corresponde?", ["Son árboles jóvenes.", "La poda para darles forma es de formación."], "Poda de formación"),
        ("Calcular la carga", "Un cuartel de ejemplo tiene 500 árboles con 300 frutos cada uno. ¿Cuántos frutos hay en total?", ["Se multiplican los árboles por los frutos de cada uno.", "500 por 300."], "150.000 frutos"),
    ],
    mistakes=[("Creer que dejar el árbol con muchos frutos da siempre más ganancia.", "Muchos frutos dan fruta pequeña de menor valor.", "El raleo busca el calibre adecuado."),
              ("Confundir el plan de poda con el registro de labores.", "El plan es lo programado y el registro es lo realizado.", "Consulta cada documento para lo que fue hecho.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la poda de formación?", "La poda de árboles jóvenes para darles la forma deseada", "La poda de árboles adultos para equilibrar la fruta", "El retiro de frutos en exceso", "La poda de formación se hace a árboles jóvenes."),
        ("abc", "En Agropecuaria: ¿qué es el calibre de la fruta?", "El tamaño de la fruta", "La cantidad de frutos por árbol", "El color de la fruta", "El calibre mide el tamaño de cada fruta cosechada."),
        ("abc", "En Agropecuaria: ¿qué es la carga frutal?", "La cantidad de frutos que lleva un árbol", "El peso del árbol", "El número de ramas del árbol", "La carga cuenta los frutos que lleva cada árbol."),
        ("=", "{F} ¿Cuántos árboles hay en el Cuartel 1?", "2*1000", "Se multiplican las hectáreas por los árboles de cada hectárea.", " árboles"),
        ("=", "{F} ¿Cuántos árboles hay en el Cuartel 2?", "1*800", "Se multiplican las hectáreas por los árboles de cada hectárea.", " árboles"),
        ("abc", "{F} ¿Qué sistema de conducción usa el Cuartel 2?", "Parrón", "Eje central", "Espaldera", "La ficha dice que el Cuartel 2 está en parrón."),
        ("abc", "{F} ¿Qué poda corresponde a los árboles de 6 años del Cuartel 1 para equilibrar crecimiento y fruta?", "Poda de producción", "Poda de formación", "Poda de renovación", "Son árboles adultos, que necesitan poda de producción."),
        ("=", "{F} ¿Cuántos frutos deben quitarse por árbol para llegar a la meta de carga?", "400-250", "Se resta la meta de frutos a la carga actual.", " frutos"),
        ("=", "{F} ¿Cuántos frutos se quitarían en total en los árboles del Cuartel 2 para llegar a la meta?", "800*(400-250)", "Se multiplican los árboles por los frutos que se quitan en cada uno.", " frutos"),
        ("abc", "{F} ¿Qué documento dice qué podar, en qué cuartel y cuándo?", "El plan de poda", "El registro de labores", "La ficha de la variedad", "El plan programa; el registro anota lo realizado."),
        ("abc", "{F} Una compañera dice: «mientras más frutos dejamos por árbol, más grande será la fruta». ¿Qué respuesta es correcta?", "Es incorrecto: con más frutos cada uno crece menos", "Es correcto, siempre", "Es correcto, si se riega mucho", "Con demasiada carga la fruta es más pequeña."),
        ("abc", "{F} El capataz pide anotar en el registro que se podó el Cuartel 2 completo, pero solo se podó la mitad. ¿Qué corresponde?", "Rechazarlo: el registro anota lo realmente trabajado", "Aceptarlo, si se termina mañana", "Aceptarlo, para cumplir el plan", "Anotar lo que no se hizo falsea el registro."),
        ("abc", "En Agropecuaria: ¿por qué conviene que el raleo lo hagan personas capacitadas?", "Porque deben decidir qué frutos quitar sin dañar el árbol", "Porque los frutos no se pueden tocar", "Porque no se necesita registro", "El raleo exige criterio y técnica para no dañar el árbol."),
    ],
    ctx=("abc", "Un conocido te pide que le «ajustes» el plan de poda de su huerto sin ver los árboles. ¿Qué respondes?", "Que el plan lo define un asesor con los árboles a la vista", "Que pode todo al mismo nivel", "Que pode lo máximo posible", "El plan depende de la edad, la variedad y el sistema."),
    sc=[
        ("En Agropecuaria: ¿qué es el parrón?", "Un sistema de conducción con estructura alta de postes y alambres", "El parrón usa una estructura alta."),
        ("En el trabajo agrícola: ¿qué es el registro de labores?", "El documento donde se anota lo realizado", "El registro guarda lo ya hecho."),
        ("En Agropecuaria: ¿qué hace el raleo con la carga?", "La ajusta para lograr un calibre adecuado", "El raleo regula la cantidad de frutos."),
    ],
    op=("Ficha de ejemplo del «Huerto Demo 3»: cuartel de 2 hectáreas, 900 árboles por hectárea, conducción en espaldera; carga de 300 frutos por árbol y meta de 200. Escribe (a) cuántos árboles tiene el cuartel, (b) cuántos frutos hay que quitar por árbol, (c) cuántos frutos se quitan en total, (d) qué documento anota lo realizado.",
        "(a) 2 × 900 = 1.800 árboles. (b) 300 − 200 = 100 frutos por árbol. (c) 1.800 × 100 = 180.000 frutos. (d) El registro de labores.",
        ["calcula los árboles", "calcula los frutos por árbol", "calcula el total", "nombra el documento"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar mal", "confundir plan con registro"],
        "Pregunta: «¿cuántos árboles hay?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Calcula los frutos totales de 600 árboles con 250 frutos cada uno.",
    extend="Explica con un ejemplo por qué el calibre cambia el valor de una fruta.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Tres cuarteles del «Huerto Demo». Cuartel A: árboles de 2 años con ramas largas que crecen en cualquier dirección, sin forma definida. "
     "Cuartel B: árboles adultos con 400 frutos pequeños cada uno y ramas sanas. Cuartel C: árboles adultos con la copa muy cerrada; en el interior casi no entra luz y los frutos de adentro salen sin color. "
     "Labores (conceptos): poda de formación, raleo y poda de aclareo (abrir la copa para que entre luz).")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso de cuarteles con síntomas distintos y a decidir con dos evidencias qué labor conceptual conviene a cada uno: formación, raleo o aclareo.",
    prior=["Sé qué son poda, raleo y conducción.", "Sé qué es la carga frutal y el calibre.", "Sé leer una ficha con datos."],
    explain=[
        "Para analizar un cuartel se observan sus señales y se relacionan con una labor. Árboles jóvenes sin forma definida necesitan poda de formación. Árboles con exceso de frutos pequeños necesitan raleo. Árboles con la copa muy cerrada, donde no entra luz, necesitan poda de aclareo, que abre la copa para que la luz y el aire lleguen al interior. La luz es necesaria porque la fruta toma color y azúcar donde la recibe, y el aire reduce la humedad que favorece hongos.",
        "La decisión se justifica con dos evidencias del caso y se registra. La labor correcta en el momento correcto cambia el resultado; una poda excesiva puede debilitar al árbol y reducir la cosecha. La decisión final la toma el asesor con el jefe de huerto, y quien ejecuta la labor es personal capacitado, porque el trabajo implica herramientas cortantes y altura.",
        f"Quien analiza el caso en papel no poda ni escala: entrega información clara. {EMER} {AVISO}",
    ],
    vocab=[("poda de aclareo", "poda que abre la copa para que entre luz y aire"), ("copa", "conjunto de ramas y hojas de un árbol"), ("síntoma", "señal visible que indica un problema"), ("evidencia", "dato del caso que respalda una decisión"), ("poda excesiva", "poda que quita demasiado y debilita al árbol")],
    worked=[
        ("Elegir la labor", "Un cuartel de ejemplo tiene árboles adultos con demasiados frutos pequeños. ¿Qué labor conviene?", ["Hay exceso de frutos pequeños.", "Quitar frutos en exceso es raleo."], "Raleo"),
        ("Relacionar síntoma y labor", "Un cuartel de ejemplo tiene copas cerradas y frutos sin color adentro. ¿Qué labor conviene?", ["Falta luz en el interior.", "Abrir la copa es poda de aclareo."], "Poda de aclareo"),
    ],
    mistakes=[("Podar mucho «para que rebrote con fuerza».", "Una poda excesiva debilita al árbol.", "La intensidad la define el asesor."),
              ("Dar una conclusión sin citar evidencia del caso.", "Sin dato del caso la decisión no se puede verificar.", "Cita dos evidencias.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la poda de aclareo?", "La poda que abre la copa para que entre luz y aire", "La poda de árboles jóvenes para darles forma", "El retiro de frutos en exceso", "El aclareo abre la copa; formar es otra poda."),
        ("abc", "En Agropecuaria: ¿por qué la luz es importante para la fruta?", "Porque la fruta toma color y azúcar donde la recibe", "Porque la luz hace caer las hojas", "Porque la luz reemplaza al riego", "La luz favorece la calidad de la fruta."),
        ("abc", "En Agropecuaria: ¿qué riesgo tiene una poda excesiva?", "Debilitar al árbol y reducir la cosecha", "Aumentar el tamaño del tronco", "Eliminar la necesidad de raleo", "Quitar demasiado deja al árbol débil."),
        ("abc", "{F} ¿Qué labor conviene al Cuartel A?", "Poda de formación, porque son árboles jóvenes sin forma", "Raleo, porque tienen muchos frutos", "Poda de aclareo, porque la copa está cerrada", "Los árboles de 2 años sin forma necesitan formación."),
        ("abc", "{F} ¿Qué evidencia respalda el raleo en el Cuartel B?", "Los árboles tienen 400 frutos pequeños cada uno", "Las ramas son sanas", "Los árboles son adultos", "El exceso de frutos pequeños es la señal que pide raleo."),
        ("abc", "{F} ¿Qué evidencia respalda la poda de aclareo en el Cuartel C?", "La copa está cerrada y los frutos de adentro salen sin color", "Los árboles tienen 2 años", "Hay 400 frutos pequeños", "La falta de luz en el interior pide abrir la copa."),
        ("=", "{F} Si el Cuartel B tiene 600 árboles con 400 frutos cada uno, ¿cuántos frutos hay en total?", "600*400", "Se multiplican los árboles por los frutos de cada uno.", " frutos"),
        ("=", "{F} Si la meta de raleo del Cuartel B es dejar 250 frutos por árbol, ¿cuántos frutos se quitan por árbol?", "400-250", "Se resta la meta de frutos a la carga actual.", " frutos"),
        ("abc", "{F} Una compañera dice: «ya sé qué labor necesita cada cuartel, así que mañana subo a podar». ¿Qué respuesta es correcta?", "Es peligroso: las labores las hace personal capacitado y autorizado", "Es correcto, si lleva guantes", "Es correcto, si alguien la ayuda", "El análisis en papel no habilita para podar ni trabajar en altura."),
        ("abc", "{F} El capataz propone podar el Cuartel A «lo máximo posible» para que rebrote. ¿Qué corresponde?", "Consultar al asesor: una poda excesiva debilita al árbol", "Aceptarlo, porque rebrota con más fuerza", "Aceptarlo, si es verano", "La intensidad de la poda la define el asesor."),
        ("abc", "{F} En el Cuartel C, un trabajador se acerca a una rama a punto de caer desde la copa. ¿Qué corresponde a quien observa?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Sujetar la rama con las manos", "Subir a cortarla", "Una rama que cae puede golpear; se avisa a quienes pueden actuar."),
        ("abc", "{F} Si el Cuartel A pasara a tener 8 años y la forma definida, ¿qué poda correspondería ahora?", "Poda de producción", "Poda de formación otra vez", "Ninguna poda nunca", "En árboles adultos se poda para equilibrar crecimiento y fruta."),
        ("abc", "En Agropecuaria: ¿por qué un cuartel con copa cerrada tiene más riesgo de hongos?", "Porque el aire no circula y la humedad se mantiene", "Porque tiene más luz", "Porque tiene menos hojas", "Sin ventilación la humedad favorece hongos."),
    ],
    ctx=("abc", "Un conocido te muestra fotos de sus manzanos con copa cerrada y te pide que le digas cuánto cortar. ¿Qué respondes?", "Que no puedes indicarlo y que un asesor debe ver los árboles", "Que corte la mitad", "Que corte todo lo que pueda", "La intensidad depende del árbol y la define un asesor."),
    sc=[
        ("En Agropecuaria: ¿qué labor conviene a un árbol joven sin forma?", "La poda de formación", "La formación da la estructura al árbol joven."),
        ("En el trabajo agrícola: ¿quién ejecuta las labores de poda?", "Personal capacitado y autorizado", "Las labores de poda exigen formación y autorización."),
        ("En Agropecuaria: ¿qué labor conviene a un árbol con exceso de frutos pequeños?", "El raleo", "El raleo ajusta la carga de frutos de cada árbol."),
    ],
    op=("Caso de ejemplo del «Huerto Demo 4»: Cuartel X, árboles de 1 año con ramas sin dirección; Cuartel Y, árboles adultos con 350 frutos pequeños cada uno y meta de 220; Cuartel Z, árboles adultos con copa cerrada y hongos en el interior. Escribe (a) la labor para X, (b) los frutos que se quitan por árbol en Y, (c) la labor para Z y una evidencia, (d) quién decide y quién ejecuta.",
        "(a) Poda de formación. (b) 350 − 220 = 130 frutos por árbol. (c) Poda de aclareo, porque la copa está cerrada y hay hongos por humedad. (d) Decide el asesor con el jefe de huerto; ejecuta personal capacitado.",
        ["elige la labor para X", "calcula los frutos de Y", "elige la labor para Z con evidencia", "distingue quién decide y quién ejecuta"],
        ["hoja con las cuatro respuestas"],
        ["elegir sin evidencia", "decidir ejecutar por cuenta propia"],
        "Pregunta: «¿qué dato del caso muestra falta de aire y luz?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Escribe dos señales inventadas de un cuartel que pidan raleo y dos que pidan aclareo.",
    extend="Explica con un ejemplo por qué una buena poda también ayuda a controlar enfermedades.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Cuartel de 1 hectárea del «Huerto Demo» con 1.000 árboles. Sin raleo: 400 frutos por árbol, peso medio de 150 gramos por fruto, precio de ejemplo $200 por kilo (fruta pequeña). "
     "Con raleo: 250 frutos por árbol, peso medio de 220 gramos por fruto, precio de ejemplo $260 por kilo (fruta de mayor calibre). Costo de ejemplo del raleo: $1.000.000 por hectárea.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular producción, ingreso y margen con y sin raleo para comparar la decisión.",
    prior=["Sé qué es el raleo y el calibre.", "Sé multiplicar y dividir enteros.", "Sé convertir gramos a kilos."],
    explain=[
        "El raleo reduce los kilos por árbol, porque quedan menos frutos, pero aumenta el tamaño de cada fruto y su precio. Para comparar se calcula la producción: frutos por árbol por peso de cada fruto, dividido entre 1.000 para pasar de gramos a kilos. Luego se multiplica por los árboles. El ingreso es kilos por precio, y el margen es el ingreso menos los costos.",
        "Un buen cálculo compara las dos opciones con los mismos supuestos: cantidad de árboles, precios y costos. El resultado indica si el raleo conviene, pero siempre con dos precauciones: los precios de ejemplo pueden cambiar y el raleo tiene un costo y una calidad (hay que quitar los frutos correctos). La decisión final la toma el asesor.",
        f"Los números de esta clase son de ejemplo y no reemplazan el criterio técnico ni la seguridad en el trabajo. {EMER} {AVISO}",
    ],
    vocab=[("producción", "kilos totales cosechados"), ("calibre", "tamaño de la fruta"), ("peso medio", "peso promedio de un fruto"), ("ingreso", "kilos por precio"), ("margen", "ingreso menos costos"), ("supuesto", "dato que se acepta como verdadero para calcular")],
    worked=[
        ("Producción por árbol", "Un árbol de ejemplo tiene 200 frutos de 100 gramos cada uno. ¿Cuántos kilos da?", ["Se multiplican los frutos por el peso de cada uno: 20.000 gramos.", "20.000 gramos son 20 kg."], "20 kg"),
        ("Margen", "Un cuartel de ejemplo produce 10.000 kg a $200 el kilo y cuesta $500.000. ¿Cuál es el margen?", ["Ingreso: 10.000 por 200.", "Margen: 2.000.000 menos 500.000."], "$1.500.000"),
    ],
    mistakes=[("Creer que menos kilos siempre significa menos dinero.", "Un mejor calibre puede subir el precio.", "Se compara el ingreso, no solo los kilos."),
              ("Olvidar el costo del raleo al comparar.", "El raleo cuesta y reduce el margen.", "Se resta el costo del raleo al ingreso con raleo.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es el peso medio de un fruto?", "El peso promedio de un fruto", "El peso total de la cosecha", "El peso del árbol", "El peso medio es el promedio por fruto."),
        ("abc", "En Agropecuaria: ¿por qué el raleo puede subir el precio por kilo?", "Porque la fruta queda más grande y de mejor calibre", "Porque la fruta pesa menos", "Porque el árbol produce más hojas", "El mayor calibre se vende mejor."),
        ("abc", "En Agropecuaria: ¿qué cuesta el raleo?", "Trabajo de personas capacitadas durante la labor", "El precio del fruto", "El agua del cultivo", "El raleo es una labor que se paga."),
        ("=", "{F} ¿Cuántos kilos da un árbol sin raleo?", "400*150//1000", "Se multiplican los frutos por el peso de cada uno y se pasa de gramos a kilos.", " kg"),
        ("=", "{F} ¿Cuántos kilos da un árbol con raleo?", "250*220//1000", "Se multiplican los frutos por el peso de cada uno y se pasa de gramos a kilos.", " kg"),
        ("=", "{F} ¿Cuántos kilos produce el cuartel sin raleo?", "400*150//1000*1000", "Se calculan los kilos por árbol y se multiplican por los árboles.", " kg"),
        ("=", "{F} ¿Cuántos kilos produce el cuartel con raleo?", "250*220//1000*1000", "Se calculan los kilos por árbol y se multiplican por los árboles.", " kg"),
        ("=", "{F} ¿Cuál es el ingreso del cuartel sin raleo?", "400*150//1000*1000*200", "Se multiplican los kilos del cuartel por el precio de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuál es el ingreso del cuartel con raleo?", "250*220//1000*1000*260", "Se multiplican los kilos del cuartel por el precio de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuál es el margen con raleo, descontando el costo del raleo?", "250*220//1000*1000*260-1000000", "Se resta el costo del raleo al ingreso con raleo.", " pesos"),
        ("abc", "{F} ¿Qué opción deja más dinero según estos datos?", "Con raleo, porque su margen es mayor que el ingreso sin raleo", "Sin raleo, porque produce más kilos", "Ambas dejan lo mismo", "Con raleo se obtienen 13.300.000 frente a 12.000.000 sin raleo."),
        ("abc", "{F} Un jefe de huerto quiere anotar que raleó el cuartel completo pero solo hizo la mitad, «para cumplir». ¿Qué corresponde?", "Rechazarlo: el registro anota lo realmente hecho", "Aceptarlo, si el resto se hace mañana", "Aceptarlo, si el asesor no está", "Falsear el registro afecta la trazabilidad."),
        ("abc", "En Agropecuaria: ¿por qué conviene revisar los supuestos antes de decidir el raleo?", "Porque el precio y el calibre pueden cambiar y modificar el resultado", "Porque los supuestos son siempre exactos", "Porque el raleo no tiene costo", "Un cambio de precio puede cambiar la mejor opción."),
    ],
    ctx=("abc", "Un conocido te pregunta si le conviene ralear, y te da solo el costo de la labor. ¿Qué respondes?", "Que faltan la carga, el calibre esperado y los precios, y que decide un asesor", "Que sí, siempre", "Que no, nunca", "Sin datos de calibre y precio no se puede comparar."),
    sc=[
        ("En Agropecuaria: ¿cómo se pasan gramos a kilos?", "Dividiendo entre 1.000", "Un kilo tiene 1.000 gramos, por eso se divide entre 1.000."),
        ("En el trabajo agrícola: ¿qué es el margen?", "El ingreso menos los costos", "El margen es lo que queda tras pagar los costos."),
        ("En Agropecuaria: ¿qué cambia el raleo en la fruta?", "Su calibre", "Quedan menos frutos, pero más grandes."),
    ],
    op=("Datos de ejemplo del «Huerto Demo 5»: 1 hectárea con 500 árboles. Sin raleo: 300 frutos de 100 gramos por árbol, precio $100 por kilo. Con raleo: 200 frutos de 160 gramos, precio $140 por kilo; costo del raleo $500.000. Escribe (a) los kilos por árbol de cada opción, (b) los kilos del cuartel, (c) el margen de cada opción, (d) cuál conviene y qué supuesto probarías.",
        "(a) Sin raleo: 300 × 100 ÷ 1.000 = 30 kg; con raleo: 200 × 160 ÷ 1.000 = 32 kg. (b) 15.000 kg sin raleo; 16.000 kg con raleo. (c) Sin raleo: 15.000 × 100 = $1.500.000; con raleo: 16.000 × 140 − 500.000 = $1.740.000. (d) Con raleo, por $240.000 más; probaría un precio menor.",
        ["calcula kilos por árbol", "calcula los kilos del cuartel", "calcula los márgenes", "elige y nombra un supuesto"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el costo del raleo", "no pasar de gramos a kilos"],
        "Pregunta: «¿cuántos gramos tiene un kilo?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula los kilos de un árbol de ejemplo con 150 frutos de 200 gramos.",
    extend="Explica con un ejemplo por qué los supuestos de un cálculo deben escribirse junto al resultado.",
)
