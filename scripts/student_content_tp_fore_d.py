"""Forestal TP 3.º y 4.º medio: OAE-03 (manejos culturales de bosque nativo y plantaciones, productivos y de preservación). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_fore_common import AVISO, EMER, build

O3 = "TP-FORE-3y4-OAE-03"

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Predio Alfa: 40 ha de plantación de «especie A», propósito productivo, densidad inicial de ejemplo de 600 árboles por hectárea. "
     "Predio Beta: 25 ha de bosque nativo, propósito de preservación; 5 ha de ese predio son una franja que protege un curso de agua. "
     "Peligros anotados para el trabajo en ambos predios: caída de ramas y de árboles, terreno con pendiente, cambios de clima y herramientas de corte.")
build(
    O3, 1, F,
    use="Aprenderé la diferencia entre bosque nativo y plantación, entre propósito productivo y de preservación, qué es un manejo cultural del bosque y cuáles son las reglas generales de seguridad y de cuidado del ambiente.",
    prior=["Sé qué es una hectárea y un plan de manejo.", "Sé qué es un peligro y un riesgo.", "Sé la jerarquía de controles."],
    explain=[
        "Un bosque nativo es un bosque formado por especies originarias del país que crecen de forma natural. Una plantación forestal es un bosque creado por personas, que plantan árboles, generalmente de una o pocas especies. Según el propósito, el manejo puede ser productivo, cuando el objetivo es obtener madera u otros productos, o de preservación, cuando se busca mantener el bosque protegido, su biodiversidad y su suelo.",
        "Los manejos culturales del bosque son intervenciones planificadas para ayudar a los árboles y proteger el suelo; entre ellos se nombran el raleo, que es reducir el número de árboles para que los restantes tengan más espacio, y la poda, que es quitar ramas bajas para mejorar la calidad de la madera. También importa la regeneración, que es el nacimiento de árboles nuevos, y el cuidado del suelo, porque el suelo sin cubierta se erosiona, es decir, el agua o el viento lo van desgastando.",
        f"Todo manejo exige un plan de manejo aprobado por la autoridad forestal y personal autorizado. Los peligros del trabajo, como la caída de ramas o árboles, el terreno con pendiente y el clima, se controlan con la jerarquía de controles. {EMER} {AVISO}",
    ],
    vocab=[("bosque nativo", "bosque de especies originarias del país que crece de forma natural"), ("plantación forestal", "bosque creado por personas que plantan árboles"), ("propósito productivo", "manejo orientado a obtener madera u otros productos"), ("propósito de preservación", "manejo orientado a mantener protegido el bosque, su biodiversidad y su suelo"), ("raleo", "reducir el número de árboles para que los restantes tengan más espacio"), ("regeneración", "nacimiento de árboles nuevos"), ("erosión", "desgaste del suelo por agua o viento")],
    worked=[
        ("Clasificar un predio", "Un predio de ejemplo es un bosque de especies originarias del país, protegido para cuidar su biodiversidad. ¿Qué tipo de bosque y qué propósito tiene?", ["Las especies originarias que crecen solas indican bosque nativo.", "Protegerlo y cuidar su biodiversidad indica un propósito de preservación."], "Bosque nativo con propósito de preservación"),
        ("Calcular árboles de una plantación", "Una plantación de ejemplo tiene 15 ha con 800 árboles por hectárea. ¿Cuántos árboles tiene?", ["Se multiplica la densidad por las hectáreas.", "800 × 15 = 12.000."], "12.000 árboles"),
    ],
    mistakes=[("Creer que un bosque nativo no tiene dueño ni reglas y que cualquiera puede intervenirlo.", "Toda intervención exige plan de manejo aprobado y personal autorizado.", "Consulta siempre el plan de manejo y a la autoridad forestal."),
              ("Creer que el propósito de preservación significa abandono sin ningún registro.", "La preservación también se planifica y se vigila.", "Registra y revisa el estado del bosque según el plan.")],
    T=[
        ("abc", "En Forestal: ¿qué es un bosque nativo?", "Un bosque de especies originarias del país que crece de forma natural", "Un bosque creado por personas en filas de una sola especie", "Un bosque formado solo por especies traídas de otros países", "El bosque nativo se origina de forma natural; la plantación la crean las personas."),
        ("abc", "En Forestal: ¿qué es una plantación forestal?", "Un bosque creado por personas que plantan árboles", "Un bosque que se regenera solo desde hace siglos", "Un bosque que se usa solo para actividades recreativas", "La plantación es un bosque creado por plantación."),
        ("abc", "En Forestal: ¿qué significa que un bosque tenga propósito de preservación?", "Que se busca mantenerlo protegido, con su biodiversidad y su suelo", "Que se cortan todos sus árboles para venderlos", "Que se deja sin ningún plan ni registro", "La preservación apunta a proteger el bosque y su suelo, no a cosechar todo."),
        ("=", "{F} ¿Cuántas hectáreas suman los dos predios de la ficha?", "40+25", "Se suman las hectáreas de los dos predios.", " ha"),
        ("abc", "{F} ¿Qué propósito tiene el predio Beta?", "Preservación", "Productivo", "Ninguno", "La ficha dice que el predio Beta es de preservación."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «caída de ramas»?", "Que una persona sea golpeada por una rama y se lesione", "La rama que se desprende del árbol", "Que el bosque se vea desordenado", "El riesgo es la posibilidad de daño; la rama es la fuente de peligro."),
        ("abc", "{F} Un letrero «zona con riesgo de caída de ramas, no ingrese sin autorización» es un control de tipo:", "Administrativo, porque informa y ordena una conducta", "De ingeniería, porque cambia el lugar", "De EPP, porque protege a la persona", "El letrero solo informa; no cambia el lugar ni protege el cuerpo."),
        ("=", "{F} ¿Qué porcentaje del predio Beta es la franja que protege el curso de agua?", "5*100//25", "Se divide la franja entre la superficie del predio y se multiplica por 100.", " %"),
        ("abc", "{F} Una estudiante dice: «el bosque nativo no es de nadie, así que puedo intervenirlo». ¿Qué respuesta es correcta?", "Es falso: toda intervención exige plan de manejo aprobado y personal autorizado", "Es cierto, si usa herramientas de mano", "Es cierto, si interviene pocos árboles", "Las herramientas o la cantidad de árboles no reemplazan el plan ni la autorización."),
        ("abc", "Durante una visita de ejemplo, un árbol cae y una persona queda atrapada bajo sus ramas. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a cortar las ramas para liberarla", "Mover el tronco con ayuda de otras personas", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "En Forestal: ¿por qué se protege el suelo cuando se trabaja en un bosque?", "Porque el suelo sin cubierta se erosiona y se pierde la base para que el bosque se regenere", "Porque el suelo es solo el piso por donde camina el personal", "Porque el suelo no cambia con el trabajo ni con la lluvia", "El suelo protegido sostiene la regeneración; sin cubierta se erosiona."),
        ("=", "{F} ¿Cuántos árboles tiene el predio Alfa con la densidad inicial anotada?", "40*600", "Se multiplica la densidad por las hectáreas del predio.", " árboles"),
        ("abc", "{F} Si el predio Alfa pasara a un propósito de preservación, ¿qué documento debería modificarse y aprobarse?", "El plan de manejo", "La ficha de un lote de plantas de vivero", "El registro de temperatura de un vivero", "El propósito de un predio se fija en su plan de manejo, aprobado por la autoridad."),
    ],
    ctx=("abc", "Un propietario te pide marcar «unos pocos» árboles de bosque nativo para sacarlos sin plan de manejo, porque «nadie se va a dar cuenta». ¿Qué respondes?", "Que no, porque toda intervención exige plan de manejo aprobado, y que lo consultarás con un adulto responsable", "Que sí, si son pocos", "Que sí, si lo hace un familiar con experiencia", "El número de árboles o la experiencia no sustituyen el plan ni la autorización."),
    sc=[
        ("En Forestal: ¿qué es la erosión del suelo?", "El desgaste del suelo por agua o viento", "La erosión desgasta el suelo cuando no está protegido."),
        ("¿Qué es un propósito productivo?", "Un manejo orientado a obtener madera u otros productos", "El propósito productivo busca obtener productos del bosque."),
        ("¿Qué documento fija lo que se hará en un predio?", "El plan de manejo", "El plan de manejo define propósito, superficie e intervenciones."),
    ],
    op=("Ficha de ejemplo: predio «Gamma»: 18 ha de plantación de «especie B», propósito productivo, 700 árboles por hectárea. Predio «Delta»: 30 ha de bosque nativo, propósito de preservación, con 6 ha de franja de protección de un curso de agua. Peligros anotados: caída de ramas y terreno con pendiente. Escribe (a) cuántos árboles tiene Gamma, (b) qué porcentaje de Delta es franja de protección, (c) un control administrativo para la caída de ramas, (d) por qué no basta con haber leído esta ficha para intervenir el bosque.",
        "(a) 18 × 700 = 12.600 árboles. (b) 6 ÷ 30 = 20 %. (c) Un letrero de advertencia y una regla de no ingresar sin autorización durante el manejo. (d) Porque toda intervención exige plan de manejo aprobado, personal autorizado y la norma vigente; este cuaderno no habilita para trabajar.",
        ["calcula los árboles de la plantación", "calcula el porcentaje de la franja", "propone un control administrativo", "explica por qué hace falta autorización"],
        ["hoja con las cuatro respuestas"],
        ["confundir bosque nativo con plantación", "olvidar la autorización", "proponer solo el EPP"],
        "Pregunta: «¿qué documento aprueba lo que se hará en un predio?». Si no responde, pídele que relea el tercer párrafo."),
    reinforce="Escribe una oración que distinga bosque nativo de plantación y otra que distinga propósito productivo de preservación.",
    extend="Explica con un ejemplo por qué el cuidado del suelo es importante tanto en una plantación como en un bosque nativo.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (extracto de plan de manejo, de ejemplo, inventado). Predio Gamma, rodal 3: 20 ha de plantación de «especie A», propósito productivo. Densidad actual de ejemplo: 1.000 árboles por hectárea. "
     "Densidad objetivo que fija el plan tras la intervención: 500 árboles por hectárea. Medida ambiental del plan: la franja de protección de un curso de agua no se interviene. "
     "El plan fue elaborado por un profesional forestal responsable y revisado por la autoridad forestal.")
build(
    O3, 2, F,
    use="Aprenderé los conceptos de plan de manejo, densidad, espaciamiento, regeneración y cobertura, y los roles que participan en el manejo de un rodal.",
    prior=["Sé qué es la densidad y una hectárea.", "Sé qué es un rodal y un plan de manejo.", "Sé dividir números enteros."],
    explain=[
        "El plan de manejo es el documento que establece los objetivos, la superficie, las especies, las intervenciones, los plazos y las medidas ambientales de un predio forestal. Lo elabora un profesional forestal responsable, lo revisa la autoridad forestal y todo el personal debe cumplirlo. Si hay que cambiar algo, se modifica el plan y se aprueba el cambio; no se cambia de palabra en terreno.",
        "La densidad es el número de árboles por hectárea y el espaciamiento es la superficie que le corresponde a cada árbol: una hectárea mide 10.000 m², así que con 250 árboles por hectárea a cada uno le tocan 40 m². La regeneración es el nacimiento de árboles nuevos, ya sea natural o por plantación. La cobertura es la parte del suelo protegida por vegetación o por restos vegetales. Cuando la densidad baja, los árboles que quedan reciben más luz y espacio.",
        f"Cada rol cumple su función: el profesional forestal planifica, el jefe de faena organiza el trabajo, el prevencionista asesora en riesgos, el personal autorizado ejecuta y la autoridad forestal fiscaliza. {EMER} {AVISO}",
    ],
    vocab=[("plan de manejo", "documento con objetivos, superficie, intervenciones, plazos y medidas ambientales"), ("espaciamiento", "superficie que le corresponde a cada árbol"), ("cobertura", "parte del suelo protegida por vegetación o restos vegetales"), ("profesional forestal responsable", "persona que elabora el plan de manejo y responde por él"), ("autoridad forestal", "institución que revisa y fiscaliza los planes de manejo")],
    worked=[
        ("Espaciamiento", "Una plantación de ejemplo tiene 400 árboles por hectárea. ¿Qué superficie le corresponde a cada árbol?", ["Una hectárea son 10.000 m².", "10.000 ÷ 400 = 25 m²."], "25 m² por árbol"),
        ("Elegir el documento", "En una faena de ejemplo se discute cuántos árboles deben quedar después de la intervención. ¿Dónde se busca el dato?", ["La densidad objetivo la fija el plan.", "Se consulta el plan de manejo, no la opinión de cada trabajador."], "En el plan de manejo"),
    ],
    mistakes=[("Cambiar de palabra en terreno la densidad que fija el plan.", "Solo se puede modificar el plan con el profesional responsable y la aprobación de la autoridad.", "Si hay una diferencia, se informa y se consulta antes de actuar."),
              ("Creer que la autoridad forestal ejecuta las labores del plan.", "Fiscaliza; las labores las hace personal autorizado.", "Distingue quién planifica, quién ejecuta y quién fiscaliza.")],
    T=[
        ("abc", "En Forestal: ¿qué es un plan de manejo?", "Un documento con objetivos, superficie, intervenciones, plazos y medidas ambientales", "Una lista de herramientas que tiene la empresa", "Un registro de ventas de un predio", "El plan de manejo ordena qué se hará en el predio y cómo se cuidará el ambiente."),
        ("abc", "En Forestal: ¿qué es el espaciamiento de una plantación?", "La superficie que le corresponde a cada árbol", "La cantidad de agua que recibe cada árbol", "La edad promedio de los árboles", "El espaciamiento relaciona la superficie con el número de árboles."),
        ("abc", "En Forestal: ¿qué es la regeneración de un bosque?", "El nacimiento de árboles nuevos", "La cosecha de los árboles más viejos", "El registro de los árboles que se cortaron", "Regeneración significa que aparecen nuevos árboles, de forma natural o por plantación."),
        ("=", "{F} ¿Qué superficie le corresponde a cada árbol con la densidad actual?", "10000//1000", "Se divide la superficie de una hectárea entre el número de árboles.", " m²"),
        ("=", "{F} ¿Qué superficie le corresponde a cada árbol con la densidad objetivo?", "10000//500", "Se divide la superficie de una hectárea entre el número de árboles que quedan.", " m²"),
        ("=", "{F} ¿Cuántos árboles tiene el rodal 3 con la densidad actual?", "1000*20", "Se multiplica la densidad por las hectáreas del rodal.", " árboles"),
        ("=", "{F} ¿Cuántos árboles deben quedar en el rodal 3 según el plan?", "500*20", "Se multiplica la densidad objetivo por las hectáreas del rodal.", " árboles"),
        ("abc", "{F} ¿Quién elaboró el plan de manejo del ejemplo?", "Un profesional forestal responsable", "El personal que ejecuta las labores de campo", "El jefe de la bodega de herramientas", "El plan lo elabora un profesional forestal responsable, no quien lo ejecuta."),
        ("abc", "{F} El jefe de faena propone empezar «y arreglar el plan después». ¿Qué respuesta es correcta?", "No se interviene sin el plan aprobado; si algo cambia, se modifica el plan antes", "Se puede empezar, porque el plan es solo una formalidad", "Se puede empezar, si el trabajo es rápido", "Intervenir sin plan aprobado incumple la norma y puede dañar el bosque."),
        ("abc", "{F} ¿Por qué el plan establece que la franja de protección de un curso de agua no se interviene?", "Porque protege el agua y el suelo de esa zona", "Porque en esa zona no hay árboles", "Porque nadie puede entrar a esa zona nunca", "La franja evita que el suelo se erosione y que el agua se contamine."),
        ("=", "{F} ¿Qué porcentaje de los árboles actuales debe retirarse para alcanzar la densidad objetivo?", "(1000-500)*100//1000", "Se calcula cuántos árboles por hectárea sobran y se compara con la densidad actual.", " %"),
        ("abc", "{F} Un inventario posterior mide 520 árboles por hectárea y el plan dice 500. ¿Qué corresponde?", "Registrar el dato real e informar al profesional responsable para que decida", "Modificar el plan por cuenta propia a 520", "Ocultar el dato para no retrasar el trabajo", "Las diferencias se informan con el dato real, y el plan solo lo cambia quien corresponde."),
        ("abc", "{F} ¿Qué rol fiscaliza que el manejo cumpla el plan aprobado?", "La autoridad forestal", "El personal autorizado que ejecuta las labores", "El proveedor de las herramientas", "La autoridad fiscaliza; el personal ejecuta y el proveedor solo entrega equipos."),
    ],
    ctx=("abc", "Un conocido te propone usar «el plan de otro predio parecido» para empezar un trabajo en el tuyo, porque «es casi lo mismo». ¿Qué respondes?", "Que no, porque cada predio tiene su propio plan elaborado y aprobado, y que lo consultarás con un adulto responsable", "Que sí, si los árboles son de la misma especie", "Que sí, si cambias el nombre del predio", "Un plan describe un predio concreto; copiarlo no lo reemplaza."),
    sc=[
        ("En Forestal: ¿qué es la cobertura del suelo?", "La parte del suelo protegida por vegetación o restos vegetales", "La cobertura protege el suelo de la erosión."),
        ("¿Quién fiscaliza los planes de manejo?", "La autoridad forestal", "La autoridad revisa y fiscaliza los planes."),
        ("¿Se puede cambiar el plan de palabra en terreno?", "No, se modifica el plan y se aprueba el cambio", "El plan solo se cambia con la aprobación correspondiente."),
    ],
    op=("Ficha de ejemplo: plan de manejo del rodal 8 del predio «Épsilon»: 12 ha de plantación de «especie B», densidad actual de ejemplo de 400 árboles por hectárea y densidad objetivo de 200. Escribe (a) la superficie por árbol actual y la objetivo, (b) cuántos árboles tiene el rodal hoy y cuántos deben quedar, (c) quién elabora el plan y quién lo fiscaliza, (d) qué haces si el inventario muestra una densidad distinta de la anotada.",
        "(a) Hoy 10.000 ÷ 400 = 25 m² por árbol y objetivo 10.000 ÷ 200 = 50 m² por árbol. (b) 400 × 12 = 4.800 árboles hoy y 200 × 12 = 2.400 deben quedar. (c) Lo elabora un profesional forestal responsable y lo fiscaliza la autoridad forestal. (d) Se registra el dato real y se informa al profesional responsable.",
        ["calcula los árboles actuales y los objetivo", "distingue quién elabora y quién fiscaliza", "propone registrar e informar", "relaciona espaciamiento con densidad"],
        ["hoja con las cuatro respuestas"],
        ["no distinguir los roles", "modificar el plan por cuenta propia", "calcular mal los árboles del rodal"],
        "Pregunta: «¿quién puede cambiar el plan?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una densidad por hectárea y calcula qué superficie le toca a cada árbol.",
    extend="Explica con un ejemplo por qué es importante que el plan fije la densidad objetivo y no cada persona en terreno.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (inventario de ejemplo, inventado). Predio Delta, rodal 7: 15 ha de bosque nativo, propósito de preservación con uso productivo limitado. "
     "Árboles adultos contados en 4 parcelas de 500 m²: 14, 18, 16 y 12. Plántulas (árboles nuevos, muy pequeños) contadas en 5 subparcelas de 10 m²: 3, 5, 4, 6 y 2. "
     "Cobertura del suelo: en 10 puntos revisados, 3 tenían suelo desnudo. Criterios de ejemplo del plan: regeneración suficiente si hay al menos 3.000 plántulas por hectárea; alerta de suelo si más del 25 % de los puntos tiene suelo desnudo.")
build(
    O3, 3, F,
    use="Aprenderé a analizar un caso de bosque nativo con datos de inventario: densidad de adultos, regeneración y cobertura del suelo, y a decidir qué informar.",
    prior=["Sé calcular un promedio y una densidad por hectárea.", "Sé qué es regeneración y cobertura.", "Sé calcular un porcentaje simple."],
    explain=[
        "Un indicador es un dato que permite saber si algo va bien o mal, como las plántulas por hectárea o el porcentaje de suelo desnudo. Para analizar un caso se calcula cada indicador y se compara con el criterio del plan. Una plántula es un árbol recién nacido, todavía muy pequeño. Si se cuenta en una subparcela de 1 m² y hay 2 plántulas, se estima que hay 20.000 por hectárea, porque una hectárea tiene 10.000 m².",
        "Un indicador bueno no compensa uno malo: puede haber mucha regeneración y, al mismo tiempo, un suelo mal protegido, y las plántulas se pierden si el suelo se erosiona. Por eso se miran todos los indicadores juntos y se decide con el profesional responsable. Los puntos con suelo desnudo se anotan como porcentaje de los puntos revisados. Las conclusiones se redactan con los números, la fecha y quién midió.",
        f"El análisis y la decisión corresponden al profesional forestal responsable; el trabajo en terreno lo hace personal autorizado, con plan de seguridad. {EMER} {AVISO}",
    ],
    vocab=[("plántula", "árbol recién nacido, todavía muy pequeño"), ("indicador", "dato que permite saber si algo va bien o mal"), ("criterio del plan", "valor de referencia que fija el plan para comparar un indicador"), ("suelo desnudo", "suelo sin vegetación ni restos que lo cubran"), ("subparcela", "parcela pequeña dentro del rodal usada para contar plántulas")],
    worked=[
        ("Plántulas por hectárea", "En 4 subparcelas de ejemplo de 10 m² hay en total 12 plántulas. ¿Cuántas hay por hectárea, estimadas?", ["El promedio por subparcela es 12 ÷ 4 = 3.", "Una hectárea tiene 1.000 subparcelas de 10 m²: 3 × 1.000 = 3.000."], "3.000 plántulas por hectárea"),
        ("Comparar con el criterio", "Un criterio de ejemplo pide menos de 30 % de suelo desnudo y un rodal tiene 20 %. ¿Se cumple?", ["20 es menor que 30.", "El indicador está dentro del criterio."], "Sí, se cumple"),
    ],
    mistakes=[("Concluir que todo va bien porque un solo indicador es bueno.", "Un buen indicador no compensa uno que está en alerta.", "Revisa todos los indicadores juntos."),
              ("Estimar plántulas por hectárea sin pasar de la subparcela a la hectárea.", "Una subparcela es una fracción muy pequeña de la hectárea.", "Multiplica por las subparcelas que caben en una hectárea.")],
    T=[
        ("abc", "En Forestal: ¿qué es una plántula?", "Un árbol recién nacido, todavía muy pequeño", "Un árbol adulto listo para ser intervenido", "Una semilla guardada en la bodega", "La plántula es el árbol joven que nace en el bosque."),
        ("abc", "En Forestal: ¿qué es un indicador del estado de un bosque?", "Un dato que permite saber si algo va bien o mal, como las plántulas por hectárea", "Una opinión personal del jefe de faena", "Un permiso para entrar al predio", "El indicador es un dato medible que se compara con un criterio."),
        ("abc", "En Forestal: ¿qué es el suelo desnudo?", "Suelo sin vegetación ni restos que lo cubran", "Suelo ya cubierto por plantas y restos", "Suelo que no ha recibido lluvia", "El suelo desnudo no tiene cobertura y se erosiona con más facilidad."),
        ("=", "{F} ¿Cuál es el promedio de árboles adultos por parcela?", "(14+18+16+12)//4", "Se suman los conteos de las 4 parcelas y se dividen entre 4.", " árboles"),
        ("=", "{F} ¿Cuántos árboles adultos por hectárea se estiman, sabiendo que caben 20 parcelas de 500 m² en una hectárea?", "((14+18+16+12)//4)*20", "Se multiplica el promedio por parcela por las parcelas que caben en una hectárea.", " árboles por hectárea"),
        ("=", "{F} ¿Cuántas plántulas se estiman por hectárea, sabiendo que caben 1.000 subparcelas de 10 m² en una hectárea?", "((3+5+4+6+2)//5)*1000", "Se calcula el promedio de las 5 subparcelas y se multiplica por las 1.000 que caben en una hectárea.", " plántulas por hectárea"),
        ("abc", "{F} ¿Cumple el rodal el criterio de regeneración?", "Sí, porque tiene más plántulas por hectárea que las 3.000 exigidas", "No, porque tiene menos de 3.000 plántulas por hectárea", "No se puede saber, porque faltan los árboles adultos", "Las plántulas estimadas son 4.000 por hectárea, más que el mínimo de 3.000."),
        ("=", "{F} ¿Qué porcentaje de los puntos revisados tenía suelo desnudo?", "3*100//10", "Se divide la cantidad de puntos con suelo desnudo entre los revisados y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué conclusión corresponde respecto del suelo?", "Hay alerta, porque 30 % supera el 25 % del criterio, y se informa al profesional responsable", "No hay problema, porque 30 % es menor que 25 %", "No se puede concluir nada con un porcentaje", "El criterio dice alerta si más del 25 % está desnudo, y el rodal tiene 30 %."),
        ("abc", "{F} Un compañero dice: «hay muchas plántulas, así que el suelo desnudo no importa». ¿Por qué es un error?", "Porque sin suelo protegido las plántulas pueden perderse por erosión", "Porque las plántulas no necesitan suelo", "Porque el suelo desnudo ayuda a que las plántulas crezcan", "El suelo desnudo se erosiona y pone en riesgo a las plántulas."),
        ("abc", "{F} El rodal tiene buena regeneración y una alerta de suelo. ¿Qué recomendación es coherente con su propósito de preservación?", "Posponer intervenciones productivas hasta mejorar la cobertura, consultando al profesional responsable", "Cosechar todos los adultos porque la regeneración es suficiente", "Eliminar las plántulas de los sectores con suelo desnudo", "El propósito es preservar; proteger el suelo y consultar es lo coherente."),
        ("=", "{F} ¿Cuántos árboles adultos se estiman en todo el rodal de 15 ha?", "((14+18+16+12)//4)*20*15", "Se multiplica la densidad estimada por las hectáreas del rodal.", " árboles"),
        ("abc", "{F} Si el plan fija ahora un máximo de 20 % de suelo desnudo, ¿cómo cambia la conclusión?", "Sigue en alerta, y con más razón, porque 30 % supera 20 %", "Deja de haber alerta, porque 30 % es menor que 20 %", "La conclusión no depende del criterio", "El criterio es más exigente y el valor de 30 % lo supera aún más."),
    ],
    ctx=("abc", "Dos subparcelas no se pudieron contar por una tormenta, y un colega propone escribir los mismos valores que las otras para completar el informe. ¿Qué corresponde?", "Informar que no se contaron y dejar constancia, sin inventar datos", "Copiar los valores de las otras subparcelas", "Anotar cero plántulas para no equivocarse", "Un dato inventado o copiado falsea el análisis; lo correcto es informar la falta."),
    sc=[
        ("En Forestal: ¿qué es una plántula?", "Un árbol recién nacido, todavía muy pequeño", "La plántula es el árbol más joven del bosque."),
        ("¿Cómo se compara un indicador con el plan?", "Se calcula el indicador y se compara con el criterio del plan", "El criterio es el valor de referencia fijado por el plan."),
        ("¿Quién decide qué hacer según el análisis?", "El profesional forestal responsable", "La decisión técnica corresponde al profesional responsable."),
    ],
    op=("Ficha de ejemplo: rodal «R-3» de 10 ha de bosque nativo con propósito de preservación. Árboles adultos en 4 parcelas de 500 m²: 10, 12, 14 y 12. Plántulas en 4 subparcelas de 10 m²: 4, 2, 6 y 4. Suelo desnudo en 2 de 10 puntos revisados. Criterios de ejemplo: al menos 5.000 plántulas por hectárea; alerta si más del 25 % de los puntos tiene suelo desnudo. Escribe (a) la densidad estimada de adultos por hectárea, (b) las plántulas estimadas por hectárea y si cumple, (c) el porcentaje de suelo desnudo y si hay alerta, (d) qué informarías y a quién.",
        "(a) 10 + 12 + 14 + 12 = 48; 48 ÷ 4 = 12 por parcela; 12 × 20 = 240 árboles por hectárea. (b) 4 + 2 + 6 + 4 = 16; 16 ÷ 4 = 4 por subparcela; 4 × 1.000 = 4.000 por hectárea: no cumple, porque son menos de 5.000. (c) 2 ÷ 10 = 20 %: no hay alerta. (d) Se informa al profesional forestal responsable que la regeneración está bajo el criterio, con los datos y la fecha.",
        ["calcula los promedios y los expande", "compara con los criterios", "no confunde los umbrales", "informa a quien corresponde"],
        ["hoja con las cuatro respuestas"],
        ["olvidar pasar de subparcela a hectárea", "confundir qué indicador cumple y cuál no", "no informar al profesional responsable"],
        "Pregunta: «¿qué indicador está en alerta y cuál no?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa tres conteos de plántulas por subparcela de 10 m² y calcula las plántulas por hectárea estimadas.",
    extend="Explica con un ejemplo por qué un buen indicador no compensa a uno en alerta.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (planificación de ejemplo, inventada; todos los costos y rendimientos son de ejemplo). Rodal 4: 24 ha de plantación de «especie B», propósito productivo. Densidad actual: 800 árboles por hectárea. "
     "Densidad objetivo del plan: 600 árboles por hectárea. Rendimiento de una cuadrilla (grupo de trabajadores autorizados bajo un responsable): 2 ha por jornada. Costo de una cuadrilla: $150.000 por jornada. "
     "El plan autoriza realizar la intervención en una ventana de 8 jornadas.")
build(
    O3, 4, F,
    use="Aprenderé a planificar en papel una intervención de manejo: porcentaje de árboles a retirar, jornadas, cuadrillas, costo y plazo, comparados con lo que autoriza el plan.",
    prior=["Sé qué es densidad y espaciamiento.", "Sé calcular porcentajes simples.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Planificar una intervención en papel es calcular cuánto trabajo hay, cuántos recursos se necesitan y cuánto tiempo toma, antes de empezar. El rendimiento es la cantidad de trabajo que hace una cuadrilla en una jornada, por ejemplo hectáreas por jornada. Una jornada es un día de trabajo. Con el rendimiento se calcula el número de jornadas y, con el costo diario de la cuadrilla, el costo total. Un rodal de 10 ha con un rendimiento de 1 ha por jornada necesita 10 jornadas de una cuadrilla, o 5 jornadas de dos cuadrillas.",
        "El plan fija el resultado que se debe alcanzar y la ventana de tiempo permitida. Un cálculo es correcto si cuadra con el plan: la densidad final es la objetivo y el plazo no supera la ventana. Si un dato real difiere del de la ficha, se recalcula y se informa. Usar más cuadrillas acorta el plazo pero no cambia el trabajo total, y por eso el costo total puede ser el mismo.",
        f"La planificación la hace el profesional forestal con la jefatura; las labores las ejecuta personal autorizado, con plan de seguridad. Aquí solo practicas los cálculos. {EMER} {AVISO}",
    ],
    vocab=[("rendimiento", "cantidad de trabajo que hace una cuadrilla en una jornada"), ("jornada", "un día de trabajo"), ("cuadrilla", "grupo de trabajadores autorizados que realiza una labor bajo un responsable"), ("ventana de tiempo", "plazo máximo que fija el plan para hacer una intervención"), ("costo total", "suma de todos los gastos de una intervención")],
    worked=[
        ("Jornadas necesarias", "Un rodal de ejemplo tiene 18 ha y una cuadrilla rinde 3 ha por jornada. ¿Cuántas jornadas necesita una cuadrilla?", ["Se divide la superficie entre el rendimiento.", "18 ÷ 3 = 6."], "6 jornadas"),
        ("Costo de una intervención", "Una cuadrilla de ejemplo trabaja 5 jornadas a $100.000 por jornada. ¿Cuál es el costo?", ["Se multiplican las jornadas por el costo diario.", "5 × 100.000 = 500.000."], "$500.000"),
    ],
    mistakes=[("Creer que usar el doble de cuadrillas cuesta el doble.", "El trabajo total es el mismo: se termina antes, pero se pagan las mismas jornadas.", "Compara jornadas por cuadrillas, no solo jornadas calendario."),
              ("Ignorar la ventana de tiempo del plan al planificar.", "Una intervención que no cabe en la ventana incumple el plan.", "Compara siempre el plazo calculado con la ventana autorizada.")],
    T=[
        ("abc", "En Forestal: ¿qué es el rendimiento de una cuadrilla?", "La cantidad de trabajo que hace en una jornada, como hectáreas por jornada", "El pago que recibe cada trabajador al mes", "La cantidad de árboles que sobreviven después", "El rendimiento mide trabajo por jornada."),
        ("abc", "En Forestal: ¿qué es una cuadrilla?", "Un grupo de trabajadores autorizados que realiza una labor bajo un responsable", "Una herramienta que se usa en grupos", "Un documento que aprueba el plan", "La cuadrilla es un grupo de personas, no una herramienta ni un documento."),
        ("abc", "En Forestal: ¿por qué se planifica en papel antes de intervenir un rodal?", "Para calcular recursos, plazos y costos y compararlos con el plan antes de empezar", "Para evitar tener que aprobar el plan de manejo", "Para que el trabajo se haga con personal sin capacitación", "La planificación previa ordena el trabajo y verifica que cumpla el plan."),
        ("=", "{F} ¿Cuántos árboles por hectárea deben retirarse para llegar a la densidad objetivo?", "800-600", "Se resta la densidad objetivo a la densidad actual.", " árboles por hectárea"),
        ("=", "{F} ¿Qué porcentaje de los árboles actuales representa lo que debe retirarse?", "(800-600)*100//800", "Se divide lo que se retira entre la densidad actual y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos árboles deben retirarse en todo el rodal 4?", "(800-600)*24", "Se multiplica lo que se retira por hectárea por las hectáreas del rodal.", " árboles"),
        ("=", "{F} ¿Cuántas jornadas necesita una sola cuadrilla para todo el rodal?", "24//2", "Se divide la superficie entre el rendimiento por jornada.", " jornadas"),
        ("=", "{F} ¿Cuántas jornadas necesitan dos cuadrillas que trabajan al mismo tiempo?", "24//(2*2)", "Se divide la superficie entre el rendimiento conjunto de las dos cuadrillas.", " jornadas"),
        ("=", "{F} ¿Cuántos pesos cuesta la intervención con dos cuadrillas?", "(24//(2*2))*2*150000", "Se multiplican las jornadas por las cuadrillas y por el costo de cada una por jornada.", " pesos"),
        ("abc", "{F} Considerando la ventana de 8 jornadas, ¿qué alternativa cumple el plan?", "Dos cuadrillas, que terminan en 6 jornadas", "Una cuadrilla, que termina en 8 jornadas", "Ninguna de las dos alternativas", "Una cuadrilla necesita 12 jornadas y supera la ventana; dos necesitan 6."),
        ("abc", "{F} ¿Qué diferencia hay entre usar una o dos cuadrillas en el costo y el plazo?", "El costo total es igual, pero con dos cuadrillas el plazo se reduce a la mitad", "Con dos cuadrillas el costo se duplica y el plazo es igual", "Con una cuadrilla el costo es la mitad y el plazo también", "El trabajo total es el mismo: 12 jornadas de cuadrilla en cualquier caso."),
        ("=", "{F} ¿Cuántos pesos cuesta la intervención por cada hectárea?", "((24//(2*2))*2*150000)//24", "Se divide el costo total entre las hectáreas del rodal.", " pesos"),
        ("=", "{F} Si el inventario real midiera 760 árboles por hectárea en lugar de 800, ¿cuántos árboles habría que retirar en el rodal para llegar al objetivo?", "(760-600)*24", "Se recalcula con el dato real y se multiplica por las hectáreas del rodal.", " árboles"),
    ],
    ctx=("abc", "El jefe te propone sumar a dos personas sin formación para «ganar tiempo» en la intervención. ¿Qué respondes?", "Que no, porque solo el personal autorizado y capacitado ejecuta las labores, y que lo consultarás con un adulto responsable", "Que sí, si trabajan lejos del resto", "Que sí, si usan guantes y casco", "La capacitación y la autorización no se reemplazan con EPP ni con distancia."),
    sc=[
        ("En Forestal: ¿cómo se calculan las jornadas de una cuadrilla?", "Se divide la superficie entre el rendimiento por jornada", "Así se obtiene cuántos días de trabajo hay que programar."),
        ("¿Qué ocurre con el costo total si se usan más cuadrillas?", "El costo total puede ser el mismo, pero se termina antes", "El trabajo total es el mismo, solo cambia el plazo."),
        ("¿Con qué se compara el plazo calculado?", "Con la ventana de tiempo que autoriza el plan", "El plazo debe caber en la ventana del plan."),
    ],
    op=("Ficha de ejemplo (todos los datos son de ejemplo): rodal 9 de 30 ha de plantación de «especie A». Densidad actual: 500 árboles por hectárea; objetivo del plan: 400. Rendimiento de una cuadrilla: 3 ha por jornada, a $120.000 por jornada. Ventana autorizada: 6 jornadas. Escribe (a) cuántos árboles se retiran en el rodal y qué porcentaje de los actuales son, (b) cuántas jornadas necesita una cuadrilla, (c) cuántas cuadrillas se necesitan para cumplir la ventana, (d) el costo total.",
        "(a) (500 − 400) × 30 = 3.000 árboles, que son 100 ÷ 500 = 20 % de los actuales. (b) 30 ÷ 3 = 10 jornadas. (c) 2 cuadrillas, porque 10 ÷ 2 = 5 jornadas, dentro de las 6 autorizadas. (d) 10 × 120.000 = 1.200.000 pesos.",
        ["calcula los árboles a retirar", "calcula jornadas con una y con dos cuadrillas", "compara con la ventana", "calcula el costo total"],
        ["hoja con los cálculos y respuestas"],
        ["no dividir por el rendimiento", "duplicar el costo por usar dos cuadrillas", "ignorar la ventana del plan"],
        "Pregunta: «¿cuánto trabajo total hay, en jornadas de cuadrilla?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un rodal de 20 ha con un rendimiento por jornada y calcula las jornadas de una cuadrilla y de dos.",
    extend="Explica con un ejemplo por qué usar más cuadrillas no siempre cambia el costo total.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 5 (alternativas de ejemplo, inventadas; ingresos, costos y porcentajes son de ejemplo). Se evalúan dos formas de manejar el mismo rodal. "
     "Alternativa A: una sola etapa de intervención; ingreso $5.000.000, costo $2.000.000, cobertura del suelo que queda 55 %, 10 jornadas de trabajo. "
     "Alternativa B: dos etapas de intervención; ingreso $5.000.000, costo $2.600.000, cobertura del suelo que queda 75 %, 12 jornadas de trabajo. "
     "El plan exige una cobertura mínima de 70 %. Lista de verificación de calidad de ejemplo para la intervención elegida: 8 ítems, de los cuales 6 se cumplen; el ítem crítico «la franja de protección del curso de agua está señalizada» se marca como no cumple.")
build(
    O3, 5, F,
    use="Aprenderé a comparar alternativas de manejo con criterios de utilidad, cobertura del suelo y exposición, y a verificar la calidad con una lista de verificación que tiene ítems críticos.",
    prior=["Sé calcular ingreso menos costo.", "Sé calcular un porcentaje simple.", "Sé qué es cobertura del suelo."],
    explain=[
        "Al comparar alternativas se calcula la utilidad, que es el ingreso menos el costo, pero la mayor utilidad no decide sola: antes hay que revisar los criterios mínimos del plan, como la cobertura del suelo que debe quedar, y también la exposición, que es el tiempo de trabajo durante el cual el personal está expuesto a los peligros. Una alternativa que no cumple un mínimo del plan no es aceptable, aunque deje más utilidad.",
        "La verificación de calidad se hace con una lista de verificación: un documento con puntos que se marcan como cumple o no cumple. Algunos ítems son críticos: si uno no se cumple, la intervención no se aprueba, aunque el resto se cumpla. Por ejemplo, con 9 de 10 ítems cumplidos y un ítem crítico en falta, igual se detiene. Los resultados se registran tal como son y se informan al responsable.",
        f"La elección final la hace el profesional forestal responsable con la jefatura. {EMER} {AVISO}",
    ],
    vocab=[("utilidad", "ingreso menos costo"), ("exposición", "tiempo durante el cual el personal está expuesto a un peligro"), ("lista de verificación", "documento con puntos que se marcan como cumple o no cumple"), ("ítem crítico", "punto cuyo incumplimiento impide aprobar aunque los demás se cumplan"), ("criterio mínimo", "valor que el plan exige como mínimo")],
    worked=[
        ("Utilidad de una alternativa", "Una alternativa de ejemplo tiene ingreso de $900.000 y costo de $350.000. ¿Cuál es su utilidad?", ["La utilidad es ingreso menos costo.", "900.000 − 350.000 = 550.000."], "$550.000"),
        ("Revisar un mínimo", "Un plan de ejemplo exige al menos 60 % de cobertura y una alternativa deja 58 %. ¿Es aceptable?", ["58 es menor que 60.", "No cumple el mínimo."], "No es aceptable"),
    ],
    mistakes=[("Elegir la alternativa con mayor utilidad sin revisar los mínimos del plan.", "Una alternativa que incumple el plan no es aceptable.", "Primero verifica los criterios mínimos y después compara la utilidad."),
              ("Aprobar una intervención por tener un alto porcentaje de ítems cumplidos, aunque un ítem crítico falle.", "Un ítem crítico en falta impide aprobar.", "Corrige el ítem crítico y verifica de nuevo.")],
    T=[
        ("abc", "En Forestal: ¿qué es una lista de verificación?", "Un documento con puntos a revisar que se marcan como cumple o no cumple", "Una lista de las herramientas que tiene una empresa", "Un mapa de las parcelas de un predio", "La lista de verificación sirve para comprobar el cumplimiento punto por punto."),
        ("abc", "En Forestal: ¿qué es un ítem crítico en una lista de verificación?", "Un punto cuyo incumplimiento impide aprobar aunque los demás se cumplan", "El punto que más cuesta cumplir", "El último punto de la lista", "Lo crítico no es el costo ni el lugar en la lista, sino el efecto en la aprobación."),
        ("abc", "En Forestal: ¿cómo se calcula la utilidad de una alternativa de manejo?", "Ingreso menos costo", "Ingreso más costo", "Costo menos ingreso", "La utilidad es lo que queda después de pagar los costos."),
        ("=", "{F} ¿Cuál es la utilidad de la alternativa A?", "5000000-2000000", "Se resta el costo al ingreso de la alternativa.", " pesos"),
        ("=", "{F} ¿Cuál es la utilidad de la alternativa B?", "5000000-2600000", "Se resta el costo al ingreso de la alternativa.", " pesos"),
        ("=", "{F} ¿Cuántas jornadas más de exposición tiene la alternativa B que la A?", "12-10", "Se restan las jornadas de A a las de B.", " jornadas"),
        ("abc", "{F} ¿Qué alternativa cumple la cobertura mínima del plan?", "Solo la alternativa B, con 75 %", "Solo la alternativa A, con 55 %", "Las dos alternativas", "El plan exige 70 %; B deja 75 % y A deja 55 %."),
        ("=", "{F} ¿Qué porcentaje de los ítems de la lista de verificación se cumple?", "6*100//8", "Se divide la cantidad de ítems que cumplen entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} El ítem crítico de la franja del curso de agua no se cumple. ¿Qué corresponde?", "No aprobar hasta corregirlo, aunque el 75 % de los ítems se cumpla", "Aprobar, porque 75 % supera la mitad", "Eliminar ese ítem de la lista", "Un ítem crítico en falta impide aprobar sin importar el porcentaje."),
        ("abc", "{F} Considerando utilidad y cobertura mínima, ¿qué alternativa conviene?", "La B, porque cumple el mínimo de cobertura aunque tenga menos utilidad", "La A, porque tiene la mayor utilidad", "Ninguna, porque no existen criterios", "La alternativa A no cumple el mínimo del plan, así que no es aceptable."),
        ("abc", "{F} La alternativa B tiene más jornadas de trabajo. ¿Qué implica para la seguridad?", "Hay más tiempo de exposición del personal, que debe controlarse con medidas", "El riesgo desaparece porque el trabajo se divide en etapas", "El riesgo no depende del tiempo de exposición", "Más jornadas significan más tiempo expuesto a los peligros, que se controlan con la jerarquía."),
        ("=", "{F} ¿Cuántos pesos de utilidad por jornada tiene la alternativa B?", "(5000000-2600000)//12", "Se divide la utilidad de B entre sus jornadas.", " pesos por jornada"),
        ("=", "{F} Si el costo de B bajara un 10 % (dato de ejemplo), ¿cuál sería su utilidad?", "5000000-(2600000*90//100)", "Se calcula el nuevo costo, que es el 90 % del anterior, y se resta al ingreso.", " pesos"),
    ],
    ctx=("abc", "Un cliente de ejemplo quiere aprobar la alternativa A porque es más rentable y dice que la cobertura mínima «es burocracia». ¿Qué corresponde?", "No aprobar una alternativa que incumple el mínimo del plan, y consultar al profesional responsable", "Aprobarla si el cliente asume la responsabilidad", "Aprobarla y corregir la cobertura después", "El mínimo del plan protege el suelo y no se puede saltar por conveniencia."),
    sc=[
        ("En Forestal: ¿qué es la utilidad?", "El ingreso menos el costo", "La utilidad mide lo que queda después de pagar los costos."),
        ("¿Qué pasa si falla un ítem crítico?", "No se aprueba hasta corregirlo", "Un ítem crítico impide aprobar aunque los demás se cumplan."),
        ("¿Qué se revisa antes de comparar la utilidad?", "Los criterios mínimos del plan", "Una alternativa que no cumple el plan no es aceptable."),
    ],
    op=("Ficha de ejemplo (todos los datos son de ejemplo): dos alternativas para un rodal. Alternativa C: ingreso $4.000.000, costo $1.500.000, cobertura que queda 60 %, 8 jornadas. Alternativa D: ingreso $4.000.000, costo $1.900.000, cobertura que queda 80 %, 10 jornadas. El plan exige una cobertura mínima de 75 %. Lista de verificación: 10 ítems, 9 cumplen y el ítem crítico «la franja de protección está señalizada» cumple. Escribe (a) la utilidad de C y de D, (b) cuál cumple la cobertura mínima, (c) cuál conviene y por qué, (d) si la lista permite aprobar y por qué.",
        "(a) C: 4.000.000 − 1.500.000 = 2.500.000; D: 4.000.000 − 1.900.000 = 2.100.000. (b) Solo D, con 80 %. (c) D, porque C no cumple el mínimo del plan aunque tenga más utilidad. (d) Sí permite aprobar, porque 9 de 10 ítems cumplen, incluido el ítem crítico.",
        ["calcula bien las utilidades", "revisa el mínimo del plan", "justifica la elección", "interpreta la lista con el ítem crítico"],
        ["hoja con las cuatro respuestas"],
        ["elegir solo por utilidad", "ignorar el mínimo del plan", "no mirar si el ítem crítico se cumple"],
        "Pregunta: «¿cuál alternativa cumple el mínimo del plan?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos alternativas con ingreso y costo y calcula la utilidad de cada una.",
    extend="Explica con un ejemplo por qué un ítem crítico es distinto de los otros ítems de una lista de verificación.",
)
