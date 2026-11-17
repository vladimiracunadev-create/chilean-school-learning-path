"""Gastronomía TP 4.º medio, mención Cocina: OAM-01 (platos de cocina básica rápidos y lentos, zonas del país, alimentación saludable), OAM-02 (cocina internacional básica) y OAM-03 (cocteles con y sin alcohol: solo conceptos, organización y costeo). Todo en papel, sin recetas ni técnicas paso a paso: datos «de ejemplo»."""
from __future__ import annotations

from tp_gaco_common import build

O1 = "TP-GACO-4-OAM-01"
O2 = "TP-GACO-4-OAM-02"
O3 = "TP-GACO-4-OAM-03"
LIM = " Este cuaderno trabaja en papel, con datos de ejemplo: la práctica en cocina requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria); no te habilita para trabajar."

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (casino de ejemplo, inventado). Para planificar, las preparaciones se clasifican por su tiempo total de producción, que incluye preparación y espera (valores de ejemplo para organizar el trabajo, no indicaciones de cocción): rápidas, hasta 30 minutos; lentas, más de 30 minutos. "
     "Preparaciones del casino: ensalada de temporada (rápida), guiso de legumbres (lenta), tortilla de verduras (rápida) y cazuela de ave (lenta). "
     "Zonas del país: la oferta de ingredientes cambia según la zona (mar, valle, cordillera, campo, sur) y también las costumbres. Guía de alimentación saludable (general): variedad de alimentos, más frutas y verduras, menos sal y azúcar añadidos.")
build(
    O1, 1, F,
    use="Aprenderé a situar la cocina básica: qué distingue las preparaciones rápidas de las lentas, cómo influye la zona del país, qué es una alimentación saludable y qué estándares de calidad se esperan.",
    prior=["Conozco la ficha técnica y las porciones.", "Sé calcular multiplicaciones y divisiones simples.", "Conozco el rótulo y el orden por riesgo."],
    explain=[
        "En Gastronomía, la cocina básica reúne preparaciones sencillas y de consumo habitual, como ensaladas, guisos, tortillas y cazuelas. Para planificar se las clasifica en rápidas y lentas según su tiempo total de producción: lo que importa a la jefa de cocina es en qué momento hay que comenzar cada una para que todo esté listo a la hora del servicio.",
        "Los platos cambian según la zona del país porque cambian los ingredientes disponibles y las costumbres: no se come igual en la costa, en el valle o en el sur. Un menú puede incorporar esa variedad. Una alimentación saludable es variada, incluye frutas y verduras y limita la sal y el azúcar añadidos; la planificación de un menú la considera.",
        "Un estándar de calidad es el nivel que se espera de un producto: la misma porción, presentación correcta y las reglas de higiene e inocuidad de la norma vigente, que fiscaliza la autoridad sanitaria. Aquí no se enseñan técnicas de cocción; solo cómo organizar y planificar." + LIM,
    ],
    vocab=[("cocina básica", "preparaciones sencillas y de consumo habitual"), ("preparación rápida", "la que tiene un tiempo total de producción corto, según la planificación"), ("preparación lenta", "la que necesita un tiempo total largo y se comienza antes"), ("alimentación saludable", "variada, con frutas y verduras y poca sal y azúcar añadidos"), ("estándar de calidad", "nivel que se espera de un producto"), ("zona del país", "región con ingredientes y costumbres propias")],
    worked=[
        ("Clasificar una preparación", "Una preparación de ejemplo tiene un tiempo total de producción de 20 minutos. Con el criterio de la ficha, ¿es rápida o lenta?", ["El límite entre rápida y lenta es de 30 minutos.", "20 es menor que 30."], "Rápida"),
        ("Planificar una hora de inicio", "Un plato lento de ejemplo necesita 60 minutos de tiempo total y debe estar listo a las 12:00. ¿A qué hora debe comenzar?", ["Se retrocede el tiempo total desde la hora del servicio.", "12:00 menos una hora es 11:00."], "A las 11:00"),
    ],
    mistakes=[("Comenzar primero las preparaciones rápidas y dejar las lentas para el final.", "Las lentas necesitan más tiempo y no estarán listas a la hora del servicio.", "Planifica hacia atrás desde la hora del servicio y comienza primero lo más lento."),
              ("Pensar que un plato regional es «mejor» que otro de otra zona.", "Cada plato responde a ingredientes y costumbres propios, no a un orden de valor.", "Valora cada preparación en su contexto y revisa que cumpla los estándares.")],
    T=[
        ("abc", "En Gastronomía: ¿qué distingue a una preparación rápida de una lenta en la planificación?", "Su tiempo total de producción", "Su precio de venta", "El número de ingredientes que lleva", "La ficha clasifica las preparaciones por el tiempo total de producción."),
        ("abc", "{F} ¿Cuál de estas preparaciones está clasificada como rápida?", "La tortilla de verduras", "El guiso de legumbres", "La cazuela de ave", "La ficha clasifica como rápidas la ensalada y la tortilla; las otras dos son lentas."),
        ("abc", "{F} ¿Por qué cambian los platos de una zona a otra del país?", "Por los ingredientes disponibles y las costumbres de cada zona", "Porque cada zona tiene una norma sanitaria distinta", "Porque el sabor lo fija la autoridad sanitaria", "La oferta de ingredientes y las costumbres explican la variedad, según la ficha."),
        ("=", "{F} El casino prepara cada día 2 preparaciones lentas y 3 rápidas, cada una de 40 porciones. ¿Cuántas porciones hay al día?", "(2+3)*40", "Se suman las preparaciones y se multiplican por las porciones de cada una.", " porciones"),
        ("abc", "{F} ¿Cuál de estas recomendaciones corresponde a una alimentación saludable según la ficha?", "Incluir más frutas y verduras", "Aumentar la sal añadida", "Reducir la variedad de alimentos", "La guía recomienda variedad, más frutas y verduras y menos sal y azúcar añadidos."),
        ("abc", "{F} Una preparación de ejemplo tiene un tiempo total de producción de 45 minutos. ¿Cómo se clasifica?", "Lenta, porque supera los 30 minutos", "Rápida, porque es menos de una hora", "Ni rápida ni lenta", "El límite de la ficha es 30 minutos; 45 lo supera."),
        ("abc", "{F} El servicio es a las 13:00 y una preparación lenta necesita 120 minutos de tiempo total. ¿A qué hora debe comenzar?", "A las 11:00", "A las 12:00", "A las 12:30", "120 minutos son dos horas, que se retroceden desde las 13:00."),
        ("abc", "{F} En la mañana, ¿qué se debe comenzar antes, la ensalada de temporada o el guiso de legumbres?", "El guiso de legumbres, que es lento", "La ensalada, que es rápida", "Ambas a la misma hora", "Lo más lento se comienza primero para llegar a tiempo."),
        ("abc", "Un compañero dice que una alimentación saludable siempre es más cara. ¿Qué respuesta corresponde?", "No necesariamente: legumbres y verduras de temporada pueden ser económicas", "Sí, siempre es más cara", "Solo es saludable si lleva carne", "El precio depende de los ingredientes elegidos y de la temporada."),
        ("abc", "Un casino de una zona costera quiere incorporar pescado local. ¿Qué debe verificar primero?", "Que haya un proveedor autorizado y se mantenga la cadena de frío", "Solo que el precio sea bajo", "Que a todos les guste el pescado", "Un producto perecible exige un proveedor autorizado y el frío continuo."),
        ("=", "{F} Una preparación lenta rinde 30 porciones por olla. Para 150 almuerzos, ¿cuántas ollas se necesitan?", "150//30", "Se dividen las porciones pedidas por las que rinde cada olla.", " ollas"),
        ("abc", "Una cocinera sirve una porción más grande a una persona conocida. ¿Qué estándar se incumple?", "La porción estandarizada, que debe ser igual para todos", "El tiempo total de producción", "La zona de origen del plato", "El estándar de calidad exige la misma porción para todos los clientes."),
        ("abc", "{F} La jefa debe tener listos a las 13:00 un guiso de legumbres, una ensalada de temporada y una tortilla de verduras. ¿Qué orden de inicio es el más adecuado?", "Comenzar el guiso primero y las preparaciones rápidas más cerca del servicio", "Comenzar la ensalada y la tortilla primero", "Comenzar todo a la vez, sin orden", "Las preparaciones rápidas se programan cerca del servicio; la lenta se adelanta."),
    ],
    ctx=("abc", "{F} Un colegio de ejemplo solicita un almuerzo con guiso, ensalada y fruta para 200 estudiantes, a las 13:00. La jefa duda sobre cuándo comenzar. ¿Qué criterio debe usar?", "Planificar hacia atrás desde las 13:00, considerando el tiempo total de la preparación más lenta", "Comenzar a la hora en que llegan los ayudantes", "Esperar a que todo el personal esté disponible", "La hora del servicio y el tiempo total de la preparación más lenta definen el inicio."),
    sc=[
        ("En Gastronomía: ¿cómo se clasifican las preparaciones para planificar?", "En rápidas y lentas según su tiempo total", "Así se sabe cuándo comenzar cada una."),
        ("¿Qué recomienda una alimentación saludable?", "Variedad, más frutas y verduras y menos sal y azúcar", "Es la guía general de la ficha."),
        ("¿Por qué varían los platos por zona?", "Por los ingredientes disponibles y las costumbres", "Cada zona tiene su propia oferta y tradiciones."),
    ],
    op=("Un casino de ejemplo servirá a las 12:30 una ensalada de temporada (tiempo total 20 minutos), un guiso de lentejas (tiempo total 90 minutos) y una fruta de postre (sin preparación). El colegio pide una opción con poca sal. "
        "Escribe: a qué hora debe comenzar cada preparación, cuál clasificarías como rápida y cuál como lenta con el criterio de 30 minutos, y dos decisiones del menú que apoyen una alimentación saludable.",
        "Guiso: comienza a las 11:00 (12:30 menos 90 minutos); lenta. Ensalada: comienza a las 12:10 (12:30 menos 20 minutos); rápida. La fruta no requiere preparación. Decisiones saludables: incluir verduras y fruta, y reducir la sal añadida.",
        ["calcula 11:00 y 12:10", "clasifica con el criterio de 30 minutos", "propone dos decisiones saludables"],
        ["hoja con horas, clasificación y dos decisiones"],
        ["retroceder mal los minutos", "clasificar el guiso como rápido", "proponer más sal"],
        "Pregunta: «¿cuántos minutos hay entre 11:00 y 12:30?». Debe responder 90."),
    reinforce="Inventa un servicio con tres preparaciones, escribe su tiempo total de ejemplo y la hora de inicio de cada una.",
    extend="Explica cómo la zona donde está un casino puede cambiar los ingredientes y el costo de su menú.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (receta estándar de ejemplo, para rendimiento y costo). «Guiso de legumbres de ejemplo»: rinde 20 porciones de 300 g. Ingredientes: legumbres secas 1.200 g, verduras 1.800 g, agua y caldo 2.800 g, aceite 100 g, sal 20 g y condimentos 80 g. "
     "Plan de producción: documento que indica qué preparaciones se hacen, cuántas porciones, quién las hace y a qué hora. Guía de alimentación saludable (general): algunos productos envasados llevan sellos de advertencia «alto en» (por ejemplo, en sodio o azúcares). "
     "Roles: la jefa de cocina planifica; el cocinero de línea elabora; el ayudante apoya; el nutricionista orienta sobre requerimientos nutricionales.")
build(
    O1, 2, F,
    use="Aprenderé a leer una receta estándar y un plan de producción, a reconocer los roles de la brigada y a considerar la alimentación saludable al planificar.",
    prior=["Conozco preparaciones rápidas y lentas.", "Sé dividir y calcular porcentajes.", "Conozco la ficha técnica."],
    explain=[
        "La receta estándar es el documento que fija los ingredientes, las cantidades, el rendimiento y la porción de una preparación, para que salga igual cada vez. El peso total se obtiene sumando los ingredientes; el peso de la porción, dividiéndolo por las porciones. El plan de producción dice qué preparaciones se hacen, cuántas porciones, quién las hace y a qué hora.",
        "La brigada es el equipo de cocina: la jefa planifica y supervisa, el cocinero de línea elabora, el ayudante apoya y, cuando existe, el nutricionista orienta sobre los requerimientos nutricionales de las personas. Una alimentación saludable se considera al diseñar la receta y el menú, por ejemplo moderando la sal y revisando los sellos de advertencia «alto en» de los productos envasados que se compran.",
        "Cambiar una receta estándar exige autorización y registro. Las cantidades de esta ficha son de ejemplo y solo sirven para calcular rendimiento y costo; este cuaderno no describe cómo preparar el plato." + LIM,
    ],
    vocab=[("receta estándar", "documento con ingredientes, cantidades, rendimiento y porción de una preparación"), ("plan de producción", "documento que dice qué se hace, cuántas porciones, quién y cuándo"), ("brigada", "equipo de personas de la cocina con roles definidos"), ("nutricionista", "profesional que orienta sobre los requerimientos nutricionales"), ("sello «alto en»", "advertencia en un producto envasado sobre un exceso de un componente")],
    worked=[
        ("Calcular el peso de una porción", "Una receta de ejemplo pesa 4.800 g en total y rinde 16 porciones. ¿Cuánto pesa cada porción?", ["Se divide el peso total por las porciones.", "4.800 ÷ 16 = 300."], "300 g"),
        ("Calcular un porcentaje", "En una receta de ejemplo de 2.000 g, un ingrediente pesa 500 g. ¿Qué porcentaje del peso total es?", ["Se multiplica por 100 y se divide por el total.", "500 × 100 ÷ 2.000 = 25."], "25 %"),
    ],
    mistakes=[("Cambiar la cantidad de sal «a gusto» en cada turno.", "El producto cambia de un día a otro y no se controla el contenido de sal.", "Propón el cambio a la jefa; si lo autoriza, se registra en la receta estándar."),
              ("No leer los sellos de advertencia de un producto envasado antes de comprarlo.", "Se puede incorporar un exceso de sal, azúcar o grasa sin darse cuenta.", "Revisa el rotulado y compara con la guía de alimentación saludable.")],
    T=[
        ("abc", "En Gastronomía: ¿para qué sirve una receta estándar?", "Para que una preparación salga igual cada vez, con cantidades y rendimiento definidos", "Para decidir quién trabaja cada turno", "Para registrar la limpieza de la cocina", "La receta estándar fija cantidades y rendimiento y asegura un producto constante."),
        ("=", "{F} ¿Cuántos gramos suman todos los ingredientes de la receta?", "1200+1800+2800+100+20+80", "Se suman las cantidades de los seis ingredientes.", " g"),
        ("=", "{F} ¿Cuántos gramos pesa cada porción según el rendimiento?", "6000//20", "Se divide el peso total por las porciones que rinde.", " g"),
        ("abc", "{F} ¿Qué indica el plan de producción?", "Qué preparaciones se hacen, cuántas porciones, quién y a qué hora", "Los ingredientes de una sola receta", "Los sellos de advertencia de los productos", "El plan organiza la producción; los ingredientes están en la receta."),
        ("abc", "{F} ¿Quién orienta sobre los requerimientos nutricionales?", "El nutricionista", "El ayudante", "El cocinero de línea", "La ficha asigna esa orientación al nutricionista."),
        ("=", "{F} ¿Qué porcentaje del peso total representan las verduras?", "1800*100//6000", "Se multiplica el peso de las verduras por 100 y se divide por el peso total.", " %"),
        ("abc", "{F} Una cocinera propone aumentar la sal de la receta porque «a la gente le gusta más salado». ¿Qué corresponde?", "Proponerlo a la jefa, que decide y registra el cambio; la guía recomienda limitar la sal", "Cambiarlo por su cuenta, porque conoce el gusto del público", "Cambiarlo solo en el turno de la tarde", "Los cambios se autorizan y registran, y la guía saludable limita la sal añadida."),
        ("abc", "{F} Un producto envasado que se quiere comprar lleva un sello «alto en» sodio. ¿Qué corresponde?", "Considerarlo al decidir si comprarlo y cuánto usar, porque aporta mucho sodio", "Ignorar el sello, porque es solo publicidad", "Comprarlo en mayor cantidad", "El sello es una advertencia sobre un exceso y debe considerarse en la planificación."),
        ("=", "{F} Si se produce el doble de la receta, ¿cuántos gramos de legumbres se necesitan?", "1200*2", "Se multiplica la cantidad de legumbres de la receta por 2.", " g"),
        ("abc", "{F} El plan de producción asigna a un ayudante nuevo elaborar solo, la preparación completa, sin supervisión. ¿Qué observación corresponde?", "El ayudante apoya bajo supervisión; la elaboración la hace quien tiene el rol de cocinero", "Está bien, porque el plan lo asigna", "Está bien, si se lo pide un compañero", "El rol de ayudante es de apoyo; una tarea completa requiere a quien corresponde."),
        ("abc", "Dos cocineros hacen el mismo plato con cantidades distintas porque cada uno usa su propia anotación. ¿Qué falla ocurre?", "No usan una receta estándar común, por lo que el plato sale distinto", "Falta un nutricionista", "El plato se clasifica como lento", "Sin una receta estándar compartida se pierde la constancia del producto."),
        ("=", "{F} Si cada porción se vende a $2.000 (precio de ejemplo), ¿cuánto se obtiene por las 20 porciones?", "2000*20", "Se multiplica el precio de una porción por las porciones del rendimiento.", " pesos"),
        ("=", "{F} La receta usa 20 g de sal para 20 porciones. ¿Cuántos gramos de sal hay por porción?", "20//20", "Se divide la sal total por las porciones.", " g"),
    ],
    ctx=("abc", "{F} Un colegio de ejemplo pide reducir la sal en sus almuerzos. La jefa debe decidir cómo proceder con la receta estándar. ¿Qué corresponde?", "Proponer el ajuste a quien autoriza, consultar al nutricionista y registrar la nueva versión de la receta", "Disminuir la sal en cada turno según el criterio de quien cocina", "Eliminar la receta estándar", "Un cambio de este tipo se coordina, se autoriza y se registra para mantenerlo constante."),
    sc=[
        ("En Gastronomía: ¿qué contiene una receta estándar?", "Ingredientes, cantidades, rendimiento y porción", "Permite repetir el mismo producto en cada turno."),
        ("¿Cómo se obtiene el peso de una porción?", "Peso total dividido por las porciones", "Reparte el peso total entre las porciones que rinde."),
        ("¿Qué advierte un sello «alto en»?", "Un exceso de un componente del producto", "Informa para decidir con criterio al comprar."),
    ],
    op=("Receta estándar de ejemplo «Tortilla de verduras de ejemplo», rinde 10 porciones: huevos 600 g, verduras 900 g, harina 100 g, aceite 50 g, sal 10 g. Plan de producción: 40 porciones para las 13:00. "
        "Calcula el peso total y el peso de cada porción, por cuánto hay que multiplicar la receta y cuántos gramos de verduras se necesitan; indica además qué rol decide un cambio de sal y qué documento muestra cuántas porciones hacer.",
        "Peso total: 600 + 900 + 100 + 50 + 10 = 1.660 g; por porción: 1.660 ÷ 10 = 166 g. Factor: 40 ÷ 10 = 4. Verduras: 900 × 4 = 3.600 g. Un cambio de sal lo autoriza la jefa de cocina; las porciones están en el plan de producción.",
        ["calcula 1.660 g y 166 g", "calcula el factor 4 y 3.600 g", "nombra el rol y el documento"],
        ["hoja con cálculos y dos respuestas"],
        ["usar 40 como factor", "cambiar la sal sin autorización", "confundir receta con plan"],
        "Pregunta: «¿por cuánto se multiplica la receta?». Si responde 40, repasa el factor."),
    reinforce="Escribe una receta estándar inventada de cuatro ingredientes con su rendimiento y calcula el peso de una porción.",
    extend="Explica por qué una receta estándar compartida protege la calidad del servicio aunque cambie el personal.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (caso de producción de ejemplo, inventado). Pedido: 120 almuerzos para las 13:00 de un colegio de ejemplo. Preparaciones: guiso de legumbres (lenta; tiempo total de ejemplo 150 minutos), tortilla de verduras (rápida; 30 minutos) y ensalada de temporada (rápida; 20 minutos). "
     "Capacidad de ejemplo: cada olla grande rinde 40 porciones del guiso y hay 2 ollas. Personal: 1 cocinera y 2 ayudantes. El colegio informa que 10 estudiantes tienen indicación de dieta sin gluten y que 6 son vegetarianos (según la lista entregada por el colegio; ningún estudiante está en los dos grupos).")
build(
    O1, 3, F,
    use="Aprenderé a analizar un caso de producción en papel: calcular capacidad, planificar los horarios hacia atrás y considerar requerimientos alimentarios especiales.",
    prior=["Conozco el plan de producción.", "Sé restar horas y calcular divisiones.", "Conozco alérgenos y contaminación cruzada."],
    explain=[
        "Un caso de producción se analiza en pasos: primero se lee el pedido (cuántas porciones y para cuándo), luego se compara con la capacidad de los equipos y del personal, después se planifican los horarios hacia atrás desde la hora del servicio y por último se revisan los requerimientos especiales de los comensales.",
        "La capacidad es la cantidad máxima de porciones que se puede producir con los equipos disponibles. Si la capacidad no alcanza, se calcula cuánto falta y se decide: otra tanda, otro equipo o ajustar el pedido. Un requerimiento especial es una necesidad alimentaria distinta, como una dieta vegetariana o sin gluten; se registra, se rotula y se evita la contaminación cruzada con otros alimentos.",
        "El gluten es una proteína de algunos cereales, como el trigo; las personas con indicación de dieta sin gluten no deben consumirlo. Ante una duda sobre ingredientes o ante una reacción de una persona, no se improvisa: se consulta a la jefatura y, si hay una reacción, se avisa a un adulto responsable y a emergencias." + LIM,
    ],
    vocab=[("capacidad", "cantidad máxima de porciones que se pueden producir con los equipos"), ("tanda", "cada vez que se elabora una preparación completa"), ("requerimiento especial", "necesidad alimentaria distinta, como dieta vegetariana o sin gluten"), ("gluten", "proteína presente en algunos cereales, como el trigo"), ("planificar hacia atrás", "calcular las horas de inicio retrocediendo desde la hora del servicio")],
    worked=[
        ("Calcular la capacidad", "Una cocina de ejemplo tiene 3 ollas que rinden 25 porciones cada una. ¿Qué capacidad tiene?", ["Se multiplican las ollas por sus porciones.", "3 × 25 = 75."], "75 porciones"),
        ("Planificar hacia atrás", "Una preparación de ejemplo necesita 45 minutos y el servicio es a las 12:30. ¿A qué hora comienza?", ["Se retroceden 45 minutos desde 12:30.", "12:30 menos 30 es 12:00; menos 15 más, 11:45."], "A las 11:45"),
    ],
    mistakes=[("Asumir que alcanza la capacidad sin calcularla.", "Se descubre el faltante cuando ya es tarde para resolverlo.", "Calcula la capacidad antes de comenzar y compara con el pedido."),
              ("Dar a una persona con dieta sin gluten una preparación sin confirmar sus ingredientes.", "Puede contener gluten y causar una reacción.", "Verifica los ingredientes, rotula y consulta a la jefatura.")],
    T=[
        ("=", "{F} ¿Cuántas porciones del guiso se pueden producir con las 2 ollas en una tanda?", "2*40", "Se multiplican las ollas por las porciones de cada una.", " porciones"),
        ("=", "{F} ¿Cuántas porciones del guiso faltan para completar el pedido en esa tanda?", "120-2*40", "Al pedido se le restan las porciones que rinden las dos ollas.", " porciones"),
        ("abc", "{F} Si el guiso se hiciera en 2 tandas seguidas de 150 minutos cada una, ¿a qué hora debe comenzar la primera para servir a las 13:00?", "A las 08:00", "A las 10:30", "A las 09:30", "Dos tandas suman 300 minutos, es decir, 5 horas hacia atrás desde las 13:00."),
        ("abc", "{F} Si la cocina consiguiera una tercera olla igual y elaborara las 120 porciones del guiso en una sola tanda de 150 minutos, ¿a qué hora debe comenzar para servir a las 13:00?", "A las 10:30", "A las 11:00", "A las 12:30", "150 minutos son dos horas y media, que se retroceden desde las 13:00."),
        ("abc", "{F} ¿A qué hora debe comenzar la tortilla de verduras para estar lista a las 13:00?", "A las 12:30", "A las 12:00", "A las 12:40", "30 minutos retroceden desde las 13:00 hasta las 12:30."),
        ("abc", "{F} ¿A qué hora debe comenzar la ensalada de temporada para estar lista a las 13:00?", "A las 12:40", "A las 12:20", "A las 12:30", "20 minutos retroceden desde las 13:00 hasta las 12:40."),
        ("abc", "{F} ¿Qué requerimiento especial tienen 10 estudiantes?", "Indicación de dieta sin gluten", "Dieta vegetariana", "Alergia a los frutos secos", "La ficha informa 10 estudiantes con dieta sin gluten y 6 vegetarianos."),
        ("=", "{F} ¿Cuántos estudiantes tienen una dieta especial entre los sin gluten y los vegetarianos?", "10+6", "Se suman los estudiantes de ambos requerimientos.", " estudiantes"),
        ("abc", "{F} Una ayudante propone servir a los estudiantes sin gluten el mismo guiso sin revisar los ingredientes. ¿Qué corresponde?", "Verificar los ingredientes, rotular y consultar a la jefatura antes de servir", "Servir el mismo guiso, porque son legumbres", "Servir igual y preguntar después si alguien se siente mal", "Sin verificación puede haber gluten en algún ingrediente y causar una reacción."),
        ("=", "{F} De los 120 almuerzos, ¿cuántos quedan para estudiantes sin requerimientos especiales de los dos grupos indicados?", "120-10-6", "Al total se le restan los estudiantes con requerimientos especiales.", " almuerzos"),
        ("abc", "{F} Un estudiante con dieta sin gluten presenta malestar después de comer. ¿Qué corresponde?", "Avisar de inmediato a un adulto responsable y a los servicios de emergencia", "Darle una infusión que se recomienda", "Pedirle que descanse y esperar", "No se improvisan remedios; se pide ayuda de personal capacitado."),
        ("abc", "{F} Con 1 cocinera y 2 ayudantes, una persona propone que los ayudantes decidan solos cuántas porciones hacer. ¿Qué observación corresponde?", "El plan lo define la jefa o la cocinera responsable; los ayudantes apoyan", "Es correcto, porque son mayoría", "Es correcto si se ponen de acuerdo", "El plan de producción responde a una responsabilidad asignada, no a la mayoría."),
        ("=", "{F} Si el guiso necesita 1.200 g de legumbres secas para 20 porciones (de ejemplo), ¿cuántos gramos se necesitan para 120 porciones?", "1200*(120//20)", "Se calcula el factor de escala y se multiplica la cantidad de legumbres.", " g"),
    ],
    ctx=("abc", "{F} Faltando una hora, la cocinera descubre que una de las 2 ollas está en mantención y no podrá usarse. ¿Qué decisión es la más razonable?", "Avisar a la jefatura, recalcular la capacidad y ajustar el plan, por ejemplo con otra tanda o apoyo adicional", "Producir igual y esperar que alcance", "Reducir la porción a los estudiantes sin avisar", "Se recalcula la capacidad y se decide con la jefatura, sin reducir porciones a escondidas."),
    sc=[
        ("En Gastronomía: ¿qué es la capacidad de producción?", "La cantidad máxima de porciones con los equipos disponibles", "Se compara con el pedido para saber si alcanza."),
        ("¿Cómo se planifica la hora de inicio?", "Retrocediendo el tiempo total desde la hora del servicio", "Así la preparación queda lista a tiempo."),
        ("¿Qué se hace antes de servir a una persona con dieta sin gluten?", "Verificar ingredientes, rotular y consultar", "Evita servir un alimento que contenga gluten."),
    ],
    op=("Caso de ejemplo. Pedido: 90 almuerzos para las 12:30. Preparación principal: cazuela, con tiempo total de ejemplo de 120 minutos; cada olla rinde 30 porciones y hay 2 ollas. Ensalada: tiempo total de 20 minutos. 8 estudiantes son vegetarianos y 4 tienen dieta sin gluten. "
        "Calcula la capacidad de las ollas y cuánto falta, la hora de inicio de la cazuela (supón que se presta una tercera olla de 30 porciones y todo se hace en una sola tanda) y la de la ensalada, y escribe tres decisiones para atender a los estudiantes con dieta especial.",
        "Capacidad: 2 × 30 = 60 porciones; faltan 90 − 60 = 30. Cazuela: comienza a las 10:30 (12:30 menos 120 minutos). Ensalada: a las 12:10. Decisiones: verificar los ingredientes de las opciones vegetariana y sin gluten, rotularlas y evitar la contaminación cruzada, y consultar a la jefatura ante dudas.",
        ["calcula 60 porciones y 30 faltantes", "calcula 10:30 y 12:10", "propone tres decisiones para dietas especiales"],
        ["hoja con cálculos y tres decisiones"],
        ["olvidar el faltante", "servir sin verificar ingredientes", "dar consejos médicos"],
        "Pregunta: «¿cuántas porciones faltan con las dos ollas?». Si responde 0, repasa la capacidad."),
    reinforce="Inventa un pedido de 100 porciones con dos preparaciones, calcula capacidad y horas de inicio.",
    extend="Explica por qué la capacidad de los equipos puede limitar cuántas porciones se pueden ofrecer.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (costeo de ejemplo, inventado). «Guiso de legumbres de ejemplo», rinde 20 porciones. Precios de ejemplo por kilo: legumbres $2.500; verduras $1.200; aceite $3.000; sal $1.000; condimentos $10.000. "
     "Cantidades de la receta: legumbres 1.200 g, verduras 1.800 g, aceite 100 g, sal 20 g y condimentos 80 g (el agua y el caldo se consideran sin costo). Costo objetivo: el costo de ingredientes debe ser el 40 % del precio de venta.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: costear una receta estándar, calcular el costo por porción y el precio de venta según un costo objetivo.",
    prior=["Conozco la receta estándar y el rendimiento.", "Sé convertir gramos a kilos.", "Sé calcular porcentajes."],
    explain=[
        "Costear una receta es calcular cuánto cuestan sus ingredientes. Para cada ingrediente se multiplica la cantidad, expresada en kilos, por el precio por kilo; como 1 kilo son 1.000 gramos, se puede multiplicar los gramos por el precio y dividir por 1.000. La suma de todos los costos es el costo total de la receta.",
        "El costo por porción es el costo total dividido por las porciones que rinde la receta. El costo objetivo es el porcentaje del precio de venta que se destina a los ingredientes. Si el costo objetivo es del 40 %, el precio de venta se calcula multiplicando el costo por porción por 100 y dividiendo por 40.",
        "Con estos cálculos se compara una receta con otra, se evalúan cambios de ingredientes y se fija el precio. Las cifras de esta clase son de ejemplo; en la práctica se usan los precios reales vigentes del proveedor." + LIM,
    ],
    vocab=[("costeo", "cálculo del costo de los ingredientes de una receta"), ("costo por porción", "costo total dividido por las porciones"), ("costo objetivo", "porcentaje del precio de venta destinado a ingredientes"), ("precio de venta", "valor al que se ofrece una porción al cliente"), ("margen", "parte del precio que queda después de pagar los ingredientes")],
    worked=[
        ("Costear un ingrediente", "Una receta de ejemplo usa 500 g de un ingrediente que cuesta $4.000 el kilo. ¿Cuánto cuesta?", ["Se multiplican los gramos por el precio y se divide por 1.000.", "500 × 4.000 ÷ 1.000 = 2.000."], "$2.000"),
        ("Calcular el precio de venta", "El costo por porción de ejemplo es $300 y el costo objetivo es del 50 %. ¿Cuál es el precio de venta?", ["Se multiplica el costo por 100 y se divide por el porcentaje.", "300 × 100 ÷ 50 = 600."], "$600"),
    ],
    mistakes=[("Olvidar convertir los gramos a kilos antes de multiplicar por el precio.", "El costo sale mil veces mayor o menor que el real.", "Divide los gramos por 1.000 para obtener los kilos."),
              ("Fijar el precio de venta igual al costo por porción.", "No queda margen para cubrir otros gastos ni ganancia.", "Usa el costo objetivo para calcular un precio con margen.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es el costo objetivo?", "El porcentaje del precio de venta que se destina a los ingredientes", "El precio al que compra el proveedor", "El número de porciones que rinde una receta", "El costo objetivo fija qué parte del precio cubre los ingredientes."),
        ("=", "{F} ¿Cuánto cuestan las legumbres de la receta?", "1200*2500//1000", "Se multiplican los gramos por el precio y se divide por 1.000.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan las verduras de la receta?", "1800*1200//1000", "Se multiplican los gramos por el precio y se divide por 1.000.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan el aceite, la sal y los condimentos juntos?", "100*3000//1000+20*1000//1000+80*10000//1000", "Se calcula el costo de cada ingrediente y se suman.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de ingredientes de la receta?", "1200*2500//1000+1800*1200//1000+100*3000//1000+20*1000//1000+80*10000//1000", "Se suman los costos de los cinco ingredientes.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta cada porción en ingredientes?", "6280//20", "Se divide el costo total por las porciones.", " pesos"),
        ("=", "{F} ¿Cuál es el precio de venta de una porción, con el costo objetivo de 40 %?", "314*100//40", "Se multiplica el costo por porción por 100 y se divide por el costo objetivo.", " pesos"),
        ("abc", "{F} Si el precio de venta fuera igual al costo por porción, ¿qué ocurriría?", "No quedaría margen para otros gastos ni ganancia", "Se ganaría más de lo planeado", "Los ingredientes pasarían a ser solo el 40 % del precio", "Sin margen, el negocio no cubre los demás gastos."),
        ("=", "{F} Si el precio de las legumbres sube a $3.000 el kilo, ¿cuánto cuestan las legumbres de la receta?", "1200*3000//1000", "Se recalcula el costo con el nuevo precio por kilo.", " pesos"),
        ("abc", "{F} Un compañero dice que, como el agua no cuesta, la receta no tiene costos fijos de gas, luz ni personal. ¿Qué respuesta es correcta?", "El costo objetivo se refiere a ingredientes; el precio de venta también debe cubrir los otros gastos", "Tiene razón, porque solo cuentan los ingredientes", "Los otros gastos se pagan con el costo de los ingredientes", "El margen del precio de venta cubre los gastos que no son ingredientes."),
        ("=", "{F} Si cada porción se vende a $785 y se venden las 20 porciones, ¿cuánto se obtiene en total?", "785*20", "Se multiplica el precio de una porción por las porciones vendidas.", " pesos"),
        ("=", "{F} Con las ventas de $15.700 y el costo total de ingredientes, ¿cuánto queda de margen antes de otros gastos?", "15700-6280", "A los ingresos se les resta el costo de los ingredientes.", " pesos"),
        ("abc", "{F} Se propone cambiar los condimentos por otros más baratos. ¿Qué debe hacerse antes de aplicar el cambio?", "Recalcular el costo y pedir autorización a la jefa, que registra la nueva versión de la receta", "Aplicarlo de inmediato, porque ahorra dinero", "Aplicarlo solo en el turno de la tarde", "Un cambio de ingrediente altera el producto y debe autorizarse y registrarse."),
    ],
    ctx=("abc", "{F} Un casino de ejemplo debe decidir si vende el guiso a $600 la porción. La jefa quiere respetar el costo objetivo de 40 %. ¿Qué conclusión corresponde?", "A $600 el costo por porción sería más del 40 % del precio, por lo que conviene subir el precio o rebajar el costo", "Conviene mantener los $600, porque el precio redondo es mejor", "Conviene bajar el precio para vender más", "El costo por porción de $314 supera el 40 % de $600, que serían $240."),
    sc=[
        ("En Gastronomía: ¿cómo se calcula el costo de un ingrediente?", "Gramos por precio por kilo, dividido por 1.000", "Convierte los gramos a kilos para usar el precio."),
        ("¿Cómo se calcula el costo por porción?", "Costo total dividido por las porciones", "Reparte el costo entre las porciones."),
        ("¿Para qué sirve el costo objetivo?", "Para fijar un precio de venta con margen", "Indica qué parte del precio cubre los ingredientes."),
    ],
    op=("Receta de ejemplo «Ensalada de legumbres», rinde 10 porciones: legumbres 600 g a $2.500 el kilo, verduras 900 g a $1.200 el kilo, aceite 50 g a $3.000 el kilo. Costo objetivo: 30 % del precio de venta. "
        "Calcula el costo de cada ingrediente, el costo total, el costo por porción y el precio de venta de una porción, y explica por qué no conviene vender a un precio igual al costo.",
        "Legumbres: 600 × 2.500 ÷ 1.000 = 1.500. Verduras: 900 × 1.200 ÷ 1.000 = 1.080. Aceite: 50 × 3.000 ÷ 1.000 = 150. Total: 2.730 pesos. Por porción: 273. Precio: 273 × 100 ÷ 30 = 910 pesos. No conviene vender al costo porque no queda margen para otros gastos ni ganancia.",
        ["calcula los tres costos y el total de 2.730", "calcula 273 por porción y 910 de precio", "explica la falta de margen"],
        ["hoja con cálculos y explicación"],
        ["olvidar dividir por 1.000", "usar el costo total como precio", "no explicar el margen"],
        "Pregunta: «¿cuántos kilos son 600 g?». Si no responde 0,6, ayúdale con la conversión usando 600 × precio ÷ 1.000."),
    reinforce="Inventa una receta de tres ingredientes con precios y calcula su costo total y por porción.",
    extend="Explica por qué subir el precio de un ingrediente obliga a revisar el precio de venta.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 1 (carta internacional de un restaurante de ejemplo, inventado). Preparaciones básicas de ejemplo: Perú, ají de gallina; México, tacos; China, arroz frito; Francia, quiche; Italia, pasta con salsa de tomate. "
     "Cada una tiene una especificación: nombre, país de origen, ingredientes principales, alérgenos declarados y porción. Alérgenos declarados (de ejemplo; en la práctica se declaran los de la receta real): ají de gallina, leche y frutos secos; tacos, soya; arroz frito, huevo y soya; quiche, huevo, leche y gluten; pasta con salsa de tomate, gluten. "
     "La autoridad sanitaria fiscaliza el rotulado y la higiene según la norma vigente.")
build(
    O2, 1, F,
    use="Aprenderé a situar la cocina internacional básica en un servicio: qué es una especificación, cómo se declaran los alérgenos y qué significa adaptar una preparación respetando su origen.",
    prior=["Conozco la receta estándar y el rótulo.", "Conozco los alérgenos.", "Sé multiplicar porciones."],
    explain=[
        "La cocina internacional básica reúne preparaciones de otros países que un servicio ofrece a su público, como las de Perú, México, China, Francia o Italia. Cada una se maneja con una especificación: un documento que describe el producto y el nivel de calidad esperado, con su nombre, país de origen, ingredientes principales, alérgenos declarados y porción.",
        "Adaptar una preparación significa ajustarla a los ingredientes disponibles y a los gustos del público, manteniendo su identidad o declarando que es una variante. Si un ingrediente cambia, la jefa lo autoriza, se actualiza la especificación y se revisan los alérgenos. Un alérgeno es una sustancia que en algunas personas causa una reacción; por eso se declara en la carta y se informa con seguridad.",
        "Se respeta la cultura de cada país: se nombra bien el plato, no se hacen burlas y se explica su origen con rigor. La autoridad sanitaria fiscaliza el rotulado y la higiene según la norma vigente. Este cuaderno no enseña a elaborar los platos, solo a gestionarlos en papel. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("especificación", "documento que describe un producto y el nivel de calidad que debe cumplir"), ("país de origen", "país donde nace la preparación"), ("alérgeno declarado", "alérgeno que figura en la especificación del producto"), ("adaptar", "ajustar una preparación a los ingredientes y al público disponibles"), ("variante", "versión de una preparación con cambios declarados")],
    worked=[
        ("Leer una especificación", "Una especificación de ejemplo dice: «País de origen: Italia». ¿Qué dato da?", ["Indica de dónde proviene la preparación.", "No describe ingredientes ni porción."], "El país de origen"),
        ("Contar porciones", "Un restaurante de ejemplo ofrece 3 preparaciones con 20 porciones cada una. ¿Cuántas porciones son?", ["Se multiplican las preparaciones por las porciones.", "3 × 20 = 60."], "60 porciones"),
    ],
    mistakes=[("Cambiar un ingrediente principal porque falta y no avisar.", "La especificación deja de ser verdadera y los alérgenos declarados pueden ser falsos.", "Informa a la jefa, decide si se mantiene o se declara una variante y actualiza la especificación."),
              ("Decirle a un cliente alérgico que un plato «no debería tener» un alérgeno.", "Una suposición puede causar una reacción.", "Responde con la especificación vigente y consulta a la jefatura si hay dudas.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es una especificación de un producto?", "Un documento que lo describe: nombre, origen, ingredientes, alérgenos y porción", "El precio al que lo vende el proveedor", "El orden en que se sirve en la mesa", "La especificación define el producto y su calidad esperada."),
        ("abc", "{F} ¿Qué preparación de la ficha corresponde a Italia?", "Pasta con salsa de tomate", "Quiche", "Tacos", "La ficha asocia la pasta con salsa de tomate a Italia; el quiche es de Francia."),
        ("abc", "{F} ¿Qué alérgenos declara el quiche?", "Huevo, leche y gluten", "Soya y huevo", "Leche y frutos secos", "La ficha declara huevo, leche y gluten para el quiche."),
        ("=", "Un restaurante de ejemplo ofrece 5 preparaciones internacionales, cada una con 24 porciones al día, y abre 6 días a la semana. ¿Cuántas porciones prepara por semana?", "5*24*6", "Se multiplican las preparaciones, las porciones diarias y los días.", " porciones"),
        ("abc", "{F} Una clienta alérgica al huevo pregunta por el arroz frito. ¿Qué corresponde?", "Informar que, según la especificación, contiene huevo y soya", "Decir que no tiene huevo, para tranquilizarla", "Decir que se averiguará al terminar el servicio", "La respuesta se basa en la especificación, sin suposiciones ni demoras."),
        ("abc", "{F} ¿Cuál de estas preparaciones declara gluten?", "Pasta con salsa de tomate", "Tacos", "Arroz frito", "La ficha declara gluten en la pasta; los tacos y el arroz declaran soya, y el arroz además huevo."),
        ("abc", "Un cocinero cambia un ingrediente principal por otro porque falta en bodega. ¿Qué corresponde?", "Informar a la jefa, evaluar si se mantiene la especificación y actualizar los alérgenos si cambian", "Cambiarlo sin avisar para no atrasar el servicio", "Dejar de servir el plato sin avisar", "Un cambio sin informar vuelve falsa la especificación y puede poner en riesgo a los clientes."),
        ("abc", "En Gastronomía: ¿qué significa adaptar una preparación internacional?", "Ajustarla a los ingredientes y al público, manteniendo la especificación o declarando la variante", "Cambiar solo el nombre del país", "Copiarla igual sin considerar la disponibilidad", "La adaptación es un ajuste declarado, no un cambio oculto."),
        ("=", "Una porción de pasta con salsa pesa 350 g y se sirven 40 porciones. ¿Cuántos kilos de producto terminado son?", "350*40//1000", "Se multiplican los gramos por las porciones y se pasan a kilos.", " kg"),
        ("abc", "Un compañero se burla de la forma en que se come un plato de otro país. ¿Qué corresponde?", "Pedirle respeto por las costumbres de cada país y por las personas", "Reírse, porque es una broma inocente", "Ignorarlo mientras no haya clientes", "La cocina internacional requiere respeto hacia las culturas que la crearon."),
        ("abc", "¿Por qué se declaran los alérgenos en la carta?", "Para que las personas con alergias puedan decidir con información", "Para que el plato parezca más complejo", "Para vender más porciones", "El rotulado protege a quienes pueden reaccionar a ciertos alimentos."),
        ("abc", "{F} ¿Cuántas de las cinco preparaciones declaran leche o gluten?", "Tres: ají de gallina, quiche y pasta", "Dos: quiche y pasta", "Cuatro: todas menos los tacos", "El ají declara leche, el quiche leche y gluten y la pasta gluten."),
        ("abc", "{F} ¿Quién fiscaliza el rotulado y la higiene de los productos de la carta?", "La autoridad sanitaria", "El país de origen del plato", "La jefa de cocina de otro local", "La ficha asigna la fiscalización a la autoridad sanitaria."),
    ],
    ctx=("abc", "{F} Un grupo de turistas incluye a dos personas que informan alergia a los frutos secos y a la soya. ¿Qué debe hacer la persona que atiende?", "Revisar la especificación de cada preparación, ofrecer solo las que no declaran esos alérgenos y confirmar con la jefatura", "Servir cualquier plato y pedirles que avisen si se sienten mal", "Preguntarles qué creen que lleva cada plato", "La decisión se basa en la especificación vigente, no en suposiciones ni en esperar una reacción."),
    sc=[
        ("En Gastronomía: ¿qué datos tiene una especificación?", "Nombre, país de origen, ingredientes, alérgenos y porción", "Describe el producto y su calidad."),
        ("¿Qué se hace si cambia un ingrediente principal?", "Se informa a la jefa y se actualiza la especificación", "Así los alérgenos declarados siguen siendo verdaderos."),
        ("¿Quién fiscaliza el rotulado?", "La autoridad sanitaria", "Controla el cumplimiento de la norma vigente."),
    ],
    op=("Especificación de ejemplo de un «Pan relleno de ejemplo» (preparación básica de ejemplo de Francia): porción de 120 g; ingredientes principales de ejemplo: masa de trigo, queso y jamón; alérgenos declarados de ejemplo: gluten y leche. La cocina se queda sin jamón y quiere usar champiñones. "
        "Escribe: (a) quién autoriza el cambio, (b) qué documento se actualiza, (c) si cambia algún alérgeno declarado y por qué, y (d) cómo informarías a una persona alérgica a la leche.",
        "(a) La jefa de cocina autoriza el cambio. (b) Se actualiza la especificación. (c) Los alérgenos declarados (gluten y leche) siguen igual, porque el cambio de jamón por champiñones no los modifica, pero se revisan los ingredientes del nuevo producto. (d) Se le informa, según la especificación, que contiene leche, y no se le sirve.",
        ["nombra a la jefa como quien autoriza", "indica la especificación como documento a actualizar", "informa el alérgeno de leche con la especificación"],
        ["hoja con cuatro respuestas"],
        ["cambiar sin autorizar", "decir que no contiene leche", "olvidar actualizar el documento"],
        "Pregunta: «¿qué documento dice los alérgenos del pan?». Debe nombrar la especificación."),
    reinforce="Inventa la especificación de una preparación de otro país con cinco datos y dos alérgenos declarados.",
    extend="Explica por qué respetar el origen de una preparación y declarar sus variantes es un deber profesional.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 2 (especificación y glosario de ejemplo). Producto: «Tacos de ejemplo»; origen: México; porción: 3 unidades de 80 g; ingredientes principales de ejemplo: tortilla de maíz, relleno de carne, verduras y salsa; alérgeno declarado de ejemplo: soya. "
     "Glosario de ejemplo: mise en place (Francia), organización previa de ingredientes y utensilios; al dente (Italia), término que describe la textura firme de la pasta; wok (China), sartén ancha de origen chino; ají (Perú), tipo de pimiento picante usado en la cocina peruana. "
     "Roles: la jefa de cocina aprueba la especificación; el cocinero la aplica; el encargado de calidad verifica que lo servido coincida con ella.")
build(
    O2, 2, F,
    use="Aprenderé el vocabulario básico de la cocina internacional, a leer una especificación y a reconocer quién aprueba, aplica y verifica cada documento.",
    prior=["Conozco la especificación y los alérgenos.", "Sé multiplicar porciones y gramos.", "Conozco los roles de la brigada."],
    explain=[
        "Cada cocina tiene su vocabulario, y muchos términos se usan en el idioma de origen: mise en place viene del francés y significa organización previa; al dente, del italiano, describe una textura firme; wok es una sartén de origen chino; ají es un pimiento picante de uso frecuente en Perú. Conocer el vocabulario permite entender especificaciones, cartas y proveedores.",
        "Una especificación se lee por partes: nombre y origen, porción, ingredientes principales y alérgenos declarados. La porción indica cuánto se sirve; en la ficha son 3 unidades de 80 g cada una. Para verificar, el encargado de calidad compara el producto servido con esa especificación, por ejemplo el peso de la porción y los ingredientes.",
        "La jefa aprueba la especificación, el cocinero la aplica y el encargado de calidad verifica. Si una persona cambia algo sin aprobación, deja de haber un documento verdadero. Los términos de esta ficha son de ejemplo y no sustituyen a una especificación real. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("mise en place", "organización previa de ingredientes y utensilios (francés)"), ("al dente", "textura firme de la pasta (italiano)"), ("wok", "sartén ancha de origen chino"), ("ají", "pimiento picante usado en la cocina peruana"), ("encargado de calidad", "persona que verifica que lo servido cumple la especificación")],
    worked=[
        ("Calcular el peso de una porción", "Una porción de ejemplo son 4 unidades de 60 g. ¿Cuánto pesa la porción?", ["Se multiplican las unidades por el peso de cada una.", "4 × 60 = 240."], "240 g"),
        ("Asociar un término", "¿A qué país corresponde el término «al dente»?", ["Es un término que describe la pasta.", "Proviene del idioma italiano."], "Italia"),
    ],
    mistakes=[("Usar un término extranjero sin conocer su significado.", "Se puede confundir una indicación de la especificación o un pedido a un proveedor.", "Consulta el glosario y confirma el significado antes de usarlo."),
              ("Verificar solo la apariencia del plato y no el peso de la porción.", "La especificación incluye la porción y el producto puede no cumplirla.", "Compara lo servido con todos los datos de la especificación.")],
    T=[
        ("abc", "{F} ¿Qué significa «mise en place» según el glosario?", "Organización previa de ingredientes y utensilios", "Una textura firme de la pasta", "Una sartén ancha", "El glosario lo define como la organización previa del trabajo."),
        ("abc", "{F} ¿A qué país corresponde el término «wok»?", "China", "Italia", "Perú", "El glosario asocia el wok a China."),
        ("=", "{F} ¿Cuántos gramos pesa una porción de tacos?", "3*80", "Se multiplican las unidades de la porción por su peso.", " g"),
        ("abc", "{F} ¿Qué alérgeno declara la especificación de los tacos?", "Soya", "Leche", "Gluten", "La especificación de ejemplo declara solo soya."),
        ("abc", "{F} ¿Quién verifica que lo servido coincida con la especificación?", "El encargado de calidad", "El cocinero", "El proveedor", "La ficha asigna esa verificación al encargado de calidad."),
        ("=", "{F} Para un evento se piden 50 porciones de tacos. ¿Cuántas unidades de taco se necesitan?", "50*3", "Se multiplican las porciones por las unidades de cada porción.", " unidades"),
        ("=", "{F} ¿Cuántos kilos de producto terminado son las 50 porciones de tacos?", "50*3*80//1000", "Se calculan los gramos totales y se pasan a kilos.", " kg"),
        ("abc", "{F} ¿Quién aprueba la especificación?", "La jefa de cocina", "El encargado de calidad", "El cocinero que la aplica", "La ficha asigna la aprobación a la jefa."),
        ("abc", "En Gastronomía: un pedido dice «ají amarillo» (de ejemplo) y la bodega no tiene idea de qué es. ¿Qué corresponde?", "Consultar el glosario o a la jefatura antes de reemplazarlo", "Reemplazarlo por cualquier pimiento", "Anular el pedido sin avisar", "Un término desconocido se aclara antes de actuar para mantener la especificación."),
        ("abc", "{F} El encargado de calidad pesa una porción de tacos y obtiene 200 g. ¿Qué conclusión corresponde?", "No cumple: la especificación fija 240 g por porción", "Cumple, porque se acerca a la porción", "Cumple, si el cliente no reclama", "El peso debe coincidir con el de la especificación, y hay 40 g de diferencia."),
        ("=", "{F} Si una porción debía pesar 240 g y salieron 200 g, ¿cuántos gramos faltan por porción?", "240-200", "A la porción especificada se le resta la porción real.", " g"),
        ("abc", "Un cocinero cambia el relleno de los tacos sin avisar porque «se ve igual». ¿Qué observación corresponde?", "El cambio debe aprobarlo la jefa y reflejarse en la especificación, sobre todo por los alérgenos", "Está bien, porque la apariencia es igual", "Solo importa si un cliente reclama", "La apariencia no garantiza que los ingredientes o los alérgenos sean los mismos."),
        ("abc", "{F} ¿Cuál de estos términos describe una textura de la pasta?", "Al dente", "Mise en place", "Wok", "Según el glosario, al dente describe la textura firme de la pasta."),
    ],
    ctx=("abc", "{F} Un proveedor entrega tortillas con un envase que declara soya y gluten, y la especificación solo declara soya. ¿Qué debe hacer la jefa?", "Verificar el nuevo ingrediente, actualizar la especificación y los alérgenos antes de servir", "Servir igual, porque la especificación ya existe", "Quitar la mención del gluten de la carta", "Si cambia lo que se declara en el envase, la información al cliente debe actualizarse antes de servir."),
    sc=[
        ("En Gastronomía: ¿quién aprueba la especificación?", "La jefa de cocina", "Es quien responde por el producto y su calidad."),
        ("¿Qué compara el encargado de calidad?", "Lo servido con la especificación", "Asegura que el producto cumpla lo declarado."),
        ("¿Qué significa «al dente»?", "Textura firme de la pasta", "Es un término italiano de textura."),
    ],
    op=("Especificación de ejemplo «Arroz frito de ejemplo» (preparación de ejemplo de China): porción de 250 g; alérgenos declarados de ejemplo: huevo y soya. Se pide una producción de 30 porciones. Una porción servida en el control pesó 230 g. "
        "Calcula los kilos totales de la producción, di si la porción servida cumple la especificación y cuántos gramos faltan, y escribe quién la aprobó, quién la verifica y qué alérgenos informarías a un cliente.",
        "Producción: 30 × 250 = 7.500 g, es decir, 7,5 kg. La porción de 230 g no cumple; faltan 20 g. La aprueba la jefa de cocina y la verifica el encargado de calidad. Se informaría que contiene huevo y soya.",
        ["calcula 7.500 g (7,5 kg)", "detecta los 20 g de diferencia", "nombra roles y alérgenos"],
        ["hoja con cálculos y respuestas"],
        ["decir que 230 g cumple", "confundir aprobar con verificar", "olvidar un alérgeno"],
        "Pregunta: «¿quién compara la porción con la especificación?». Debe responder el encargado de calidad."),
    reinforce="Escribe un glosario de cuatro términos de cocina internacional con su país y su significado.",
    extend="Explica por qué conocer el vocabulario de otras cocinas ayuda a evitar errores con proveedores y clientes.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 3 (caso de producción de ejemplo, inventado). «Pasta con salsa de tomate de ejemplo», porción de 350 g. Ingredientes para 10 porciones: pasta seca 1.000 g, tomate 1.500 g, aceite 60 g, ajo 30 g y queso 100 g. "
     "Pedido de un evento: 60 porciones. Existencias en bodega: pasta 5.000 g, tomate 8.000 g, aceite 400 g, ajo 200 g y queso 0 g (se agotó). Alérgenos declarados de ejemplo: gluten y leche (por el queso).")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso: escalar una especificación, detectar faltantes y decidir con la jefatura si se pide más o se declara una variante.",
    prior=["Conozco el factor de escala.", "Conozco la especificación y los alérgenos.", "Sé restar cantidades."],
    explain=[
        "Para un evento se calcula el factor de escala dividiendo las porciones pedidas por las porciones de la ficha. Cada ingrediente de la ficha se multiplica por ese factor y se compara con las existencias de bodega. Si algo no alcanza, se calcula el faltante restando lo que hay a lo que se necesita.",
        "Ante un faltante hay tres caminos: pedirlo al proveedor si el plazo lo permite, producir menos porciones o ofrecer una variante declarada. Una variante cambia la especificación: por ejemplo, una versión sin queso elimina el alérgeno de la leche, pero lo decide la jefa y se rotula en la carta.",
        "En todos los casos se mantiene la información veraz para el cliente. Si una persona alérgica pregunta, se responde con la especificación vigente; ante una reacción, se avisa a un adulto responsable y a emergencias." + LIM,
    ],
    vocab=[("factor de escala", "número por el que se multiplica cada ingrediente de la ficha"), ("faltante", "cantidad que falta para cubrir lo necesario"), ("variante", "versión de la preparación con un cambio declarado"), ("existencias", "cantidad disponible en bodega")],
    worked=[
        ("Calcular el factor", "Una ficha de ejemplo rinde 8 porciones y se piden 48. ¿Cuál es el factor de escala?", ["Se dividen las porciones pedidas por las de la ficha.", "48 ÷ 8 = 6."], "6"),
        ("Detectar un faltante", "Se necesitan 750 g de un ingrediente y hay 500 g. ¿Cuánto falta?", ["Se resta lo disponible de lo necesario.", "750 − 500 = 250."], "250 g"),
    ],
    mistakes=[("Servir una variante sin queso sin declararlo en la carta.", "Los clientes creen que sigue siendo la preparación original y pueden decidir mal.", "Declara la variante y actualiza los alérgenos informados."),
              ("Decidir el cambio de un ingrediente sin consultar.", "La jefa es quien aprueba cambios a la especificación.", "Consulta y registra la decisión.")],
    T=[
        ("=", "{F} ¿Cuál es el factor de escala para 60 porciones?", "60//10", "Se dividen las porciones pedidas por las que rinde la ficha.", ""),
        ("=", "{F} ¿Cuántos gramos de pasta seca se necesitan?", "1000*6", "Se multiplica la pasta de la ficha por el factor 6.", " g"),
        ("=", "{F} ¿Cuántos gramos de pasta seca faltan?", "1000*6-5000", "A la pasta necesaria se le restan las existencias.", " g"),
        ("=", "{F} ¿Cuántos gramos de tomate se necesitan?", "1500*6", "Se multiplica el tomate de la ficha por el factor 6.", " g"),
        ("=", "{F} ¿Cuántos gramos de tomate faltan?", "1500*6-8000", "Al tomate necesario se le restan las existencias.", " g"),
        ("abc", "{F} ¿Alcanza el aceite de bodega para las 60 porciones?", "Sí: se necesitan 360 g y hay 400 g", "No: se necesitan 600 g", "No: se necesitan 460 g", "60 g por 6 dan 360 g, que son menos que los 400 g existentes."),
        ("abc", "{F} ¿Alcanza el ajo de bodega para las 60 porciones?", "Sí: se necesitan 180 g y hay 200 g", "No: se necesitan 300 g", "No: se necesitan 210 g", "30 g por 6 dan 180 g, menos que los 200 g existentes."),
        ("=", "{F} ¿Cuántos gramos de queso se necesitan, aunque no haya existencias?", "100*6", "Se multiplica el queso de la ficha por el factor 6.", " g"),
        ("abc", "{F} Si no se puede conseguir queso, ¿qué opción es válida?", "Ofrecer una variante sin queso, declarada y aprobada por la jefa", "Servir la pasta sin queso igual y no informar", "Reemplazar el queso por otro producto sin revisar sus alérgenos", "Una variante se declara y aprueba; ocultarla confunde al cliente."),
        ("abc", "{F} ¿Qué alérgeno desaparece si se ofrece la variante sin queso, manteniendo los demás ingredientes?", "La leche", "El gluten", "Ninguno", "La ficha asocia la leche al queso; el gluten proviene de la pasta."),
        ("abc", "{F} Un cliente alérgico a la leche pregunta si puede comer la versión original. ¿Qué corresponde?", "Informar que contiene leche por el queso y ofrecerle la variante declarada", "Decir que no tiene leche", "Decir que lo pruebe en poca cantidad", "La respuesta debe ser veraz y basada en la especificación."),
        ("=", "{F} Si cada porción pesa 350 g, ¿cuántos kilos de producto terminado son 60 porciones?", "60*350//1000", "Se multiplican las porciones por el peso y se pasan a kilos.", " kg"),
        ("abc", "{F} Una persona del evento muestra dificultad para respirar luego de comer. ¿Qué corresponde?", "Avisar de inmediato a un adulto responsable y a los servicios de emergencia", "Ofrecerle agua y esperar", "Darle un medicamento que alguien lleve", "Se pide ayuda de personal capacitado y no se improvisan remedios."),
    ],
    ctx=("abc", "{F} Faltando poco, el proveedor avisa que no podrá entregar pasta seca ni tomate hoy. ¿Qué es lo más razonable?", "Informar a la jefa y al cliente, y evaluar reducir porciones o cambiar la preparación con aprobación", "Servir menos pasta por plato sin avisar", "Mezclar con otras pastas sin declararlo", "Hay que informar y decidir con aprobación, no ocultar el cambio."),
    sc=[
        ("En Gastronomía: ¿cómo se calcula el factor de escala?", "Porciones pedidas dividido por porciones de la ficha", "Indica cuántas veces se multiplica la ficha."),
        ("¿Qué se hace si falta un ingrediente?", "Se calcula el faltante y se decide con la jefa", "Se pide más, se reduce la producción o se declara una variante."),
        ("¿Qué alérgeno aporta el queso en esta ficha?", "Leche", "La ficha lo declara por el queso."),
    ],
    op=("Ficha de ejemplo «Arroz frito de ejemplo», 8 porciones: arroz 800 g, verduras 600 g, huevo 240 g, salsa de soya 40 g. Pedido: 40 porciones. Existencias: arroz 3.500 g, verduras 3.000 g, huevo 1.000 g, salsa 200 g. Alérgenos declarados de ejemplo: huevo y soya. "
        "Calcula el factor y las cantidades necesarias, qué ingredientes no alcanzan y cuánto falta, y propón una decisión con la jefa sin ocultar el cambio al cliente.",
        "Factor: 40 ÷ 8 = 5. Arroz: 4.000 g (hay 3.500, faltan 500). Verduras: 3.000 g (alcanzan justo). Huevo: 1.200 g (hay 1.000, faltan 200). Salsa: 200 g (alcanza justo). Decisión: pedir el arroz y el huevo faltantes o producir menos porciones, informando a la jefa; si cambia un ingrediente, se declara.",
        ["calcula el factor 5", "detecta los faltantes de arroz y huevo", "propone una decisión veraz con la jefa"],
        ["hoja con cálculos y decisión"],
        ["usar 40 como factor", "no detectar el faltante de huevo", "ocultar un cambio"],
        "Pregunta: «¿cuántos gramos de huevo necesitas?». Si no responde 1.200, repasa el factor."),
    reinforce="Inventa una ficha de 10 porciones con tres ingredientes, escala a 50 porciones y detecta un faltante.",
    extend="Explica por qué una variante declarada es mejor que un cambio oculto, aunque el cliente no note la diferencia.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 4 (conversión y costeo de ejemplo, inventados). Equivalencias de ejemplo: 1 kg = 1.000 g; 1 litro = 1.000 ml; 1 taza de ejemplo = 250 ml; 1 libra de ejemplo = 450 g (aproximado). "
     "Receta extranjera de ejemplo (escrita en unidades de su país), rinde 10 porciones: harina 2 libras; leche 4 tazas; huevos 6 unidades. Precios de ejemplo: harina $1.800 por kg; leche $1.000 por litro; huevo $180 por unidad. Costo objetivo: 40 % del precio de venta.")
build(
    O2, 4, F,
    use="Aprenderé a convertir unidades de una receta extranjera y a calcular su costo, el costo por porción y el precio de venta con un costo objetivo.",
    prior=["Sé convertir gramos a kilos.", "Conozco el costeo y el costo objetivo.", "Sé multiplicar y dividir."],
    explain=[
        "Las especificaciones de otros países pueden venir con otras unidades, como libras o tazas. Para trabajarlas se convierten a las unidades que usamos: gramos, kilos, mililitros y litros. Se usa una tabla de equivalencias y se multiplica la cantidad por el valor de la equivalencia. Los valores de esta ficha son de ejemplo y aproximados.",
        "Una vez convertidas las cantidades, se calcula el costo de cada ingrediente. Para los sólidos, los gramos multiplicados por el precio por kilo y divididos por 1.000; para los líquidos, los mililitros multiplicados por el precio por litro y divididos por 1.000; para unidades sueltas, las unidades por el precio de cada una.",
        "El costo total dividido por las porciones es el costo por porción, y el precio de venta se obtiene al multiplicarlo por 100 y dividirlo por el costo objetivo. Todo es un ejercicio en papel; en la práctica se usan equivalencias oficiales y precios reales." + LIM,
    ],
    vocab=[("conversión", "cambio de una unidad a otra, como libras a gramos"), ("equivalencia", "relación entre dos unidades, como 1 litro = 1.000 ml"), ("costo por porción", "costo total dividido por las porciones"), ("precio de venta", "valor al que se ofrece una porción"), ("aproximado", "cercano al valor real, no exacto")],
    worked=[
        ("Convertir una unidad", "Con la equivalencia de ejemplo de 1 libra = 450 g, ¿cuántos gramos son 3 libras?", ["Se multiplican las libras por 450.", "3 × 450 = 1.350."], "1.350 g"),
        ("Costear un líquido", "Se usan 500 ml de un líquido que cuesta $1.200 el litro. ¿Cuánto cuesta?", ["Se multiplican los ml por el precio y se divide por 1.000.", "500 × 1.200 ÷ 1.000 = 600."], "$600"),
    ],
    mistakes=[("Costear sin convertir antes las libras a gramos.", "El resultado no corresponde a las unidades del precio por kilo.", "Convierte todas las cantidades a la unidad del precio antes de calcular."),
              ("Creer que una equivalencia aproximada sirve para cualquier receta.", "Una diferencia pequeña puede ser relevante en producciones grandes.", "Usa la equivalencia vigente y revisa el margen de error.")],
    T=[
        ("=", "{F} ¿Cuántos gramos son las 2 libras de harina?", "2*450", "Se multiplican las libras por la equivalencia de 450 g.", " g"),
        ("=", "{F} ¿Cuántos mililitros son las 4 tazas de leche?", "4*250", "Se multiplican las tazas por 250 ml.", " ml"),
        ("=", "{F} ¿Cuánto cuesta la harina de la receta?", "2*450*1800//1000", "Se convierten las libras a gramos y se multiplican por el precio por kilo, dividiendo por 1.000.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta la leche de la receta?", "4*250*1000//1000", "Se convierten las tazas a mililitros y se multiplican por el precio por litro, dividiendo por 1.000.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan los huevos de la receta?", "6*180", "Se multiplican las unidades por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la receta?", "2*450*1800//1000+4*250*1000//1000+6*180", "Se suman los costos de la harina, la leche y los huevos.", " pesos"),
        ("=", "{F} ¿Cuál es el costo por porción?", "3700//10", "Se divide el costo total por las porciones.", " pesos"),
        ("=", "{F} ¿Cuál es el precio de venta de una porción con el costo objetivo?", "370*100//40", "Se multiplica el costo por porción por 100 y se divide por el costo objetivo.", " pesos"),
        ("abc", "{F} ¿Por qué se convierten las libras a gramos antes de costear?", "Porque el precio de la harina está en pesos por kilo", "Porque las libras no se pueden pagar", "Porque la receta cambia de país", "El precio y la cantidad deben estar en la misma unidad."),
        ("=", "{F} Si el precio de la harina sube a $2.000 el kilo, ¿cuánto cuesta la harina de la receta?", "2*450*2000//1000", "Se recalcula el costo con el nuevo precio por kilo.", " pesos"),
        ("abc", "{F} Un cocinero dice que 1 taza es siempre 250 ml. ¿Qué observación corresponde?", "Es un valor de ejemplo; en la práctica se usa la equivalencia vigente indicada por la jefatura", "Tiene razón, es una ley universal", "Debe usarse 200 ml, porque es la medida habitual en todas las cocinas", "La ficha rotula la equivalencia como de ejemplo; en la práctica se verifica."),
        ("=", "{F} Si se produce el doble de la receta, ¿cuántos mililitros de leche se necesitan?", "4*250*2", "Se convierten las tazas y se multiplican por el doble.", " ml"),
        ("abc", "{F} Si el costo de los ingredientes pasara de $3.700 a $4.000, ¿qué ocurre con el precio de venta si se mantiene el costo objetivo?", "Debe subir, para que los ingredientes sigan siendo el 40 % del precio", "Debe bajar", "Se mantiene igual", "Con un costo mayor, el precio necesario para mantener el porcentaje también es mayor."),
    ],
    ctx=("abc", "{F} Una cocinera propone vender cada porción a $600 porque «es un precio redondo». ¿Qué debe revisar la jefa?", "Si el costo por porción respeta el costo objetivo de 40 % con ese precio", "Solo que el precio sea redondo", "Que la receta sea extranjera", "Con $600, el 40 % son $240, y el costo por porción es de $370, por lo que no se cumple."),
    sc=[
        ("En Gastronomía: ¿para qué se convierten las unidades de una receta extranjera?", "Para trabajar con las unidades de los precios y los equipos", "Hace posible el costeo y la comparación."),
        ("¿Cómo se calcula el precio de venta con el costo objetivo?", "Costo por porción por 100, dividido por el porcentaje", "Relaciona el costo con el precio."),
        ("¿Por qué las equivalencias de la ficha se rotulan como de ejemplo?", "Porque en la práctica se usan las vigentes", "Evita tomar un valor aproximado como regla."),
    ],
    op=("Receta extranjera de ejemplo, rinde 12 porciones: azúcar 1 libra; leche 3 tazas; aceite 250 ml. Equivalencias de ejemplo: 1 libra = 450 g; 1 taza = 250 ml. Precios de ejemplo: azúcar $1.400 el kg; leche $1.000 el litro; aceite $3.600 el litro. Costo objetivo: 40 %. "
        "Calcula la cantidad en gramos y mililitros de cada ingrediente, el costo total, el costo por porción y el precio de venta.",
        "Azúcar: 450 g, costo 450 × 1.400 ÷ 1.000 = 630. Leche: 3 × 250 = 750 ml, costo 750. Aceite: 250 ml, costo 250 × 3.600 ÷ 1.000 = 900. Total: 2.280 pesos. Costo por porción: 2.280 ÷ 12 = 190. Precio de venta: 190 × 100 ÷ 40 = 475 pesos.",
        ["convierte las unidades", "calcula el costo total", "calcula costo por porción y precio de venta"],
        ["hoja con conversiones y cálculos"],
        ["olvidar dividir por 1.000", "no convertir tazas a mililitros", "usar el costo total como precio"],
        "Pregunta: «¿cuántos mililitros son 3 tazas?». Si no responde 750, repasa la equivalencia."),
    reinforce="Inventa una receta extranjera con libras y tazas, conviértela a gramos y mililitros y calcula su costo.",
    extend="Explica por qué una pequeña diferencia en una equivalencia puede ser importante en una producción grande.",
)

# ============================================================ OAM-03, clase 1
F = ("Ficha 1 (bar de un restaurante de ejemplo, inventado). Carta de bebidas: 3 con alcohol y 4 sin alcohol. Reglas generales (según la norma vigente, que fiscaliza la autoridad competente): las personas menores de edad no consumen bebidas alcohólicas ni son atendidas con ellas; no se atiende con alcohol a personas en estado de ebriedad; "
     "se ofrece siempre una alternativa sin alcohol; el estudiante en formación trabaja solo con versiones sin alcohol y bajo supervisión del docente. Riesgos del consumo de alcohol: accidentes, daño a la salud y conducir bajo su efecto.")
build(
    O3, 1, F,
    use="Aprenderé a situar el trabajo del bar: qué es un coctel, qué diferencia hay entre bebidas con y sin alcohol y qué responsabilidades y límites impone la norma.",
    prior=["Conozco la ficha técnica y las porciones.", "Sé calcular porcentajes.", "Conozco la norma sanitaria como marco general."],
    explain=[
        "En Gastronomía, un coctel es una bebida preparada con varios ingredientes, que puede llevar alcohol o no. Las bebidas alcohólicas contienen alcohol; las analcohólicas o sin alcohol no lo contienen. El bar es el área del servicio donde se preparan y se sirven las bebidas, y funciona con fichas, inventarios y reglas de servicio responsable.",
        "El alcohol tiene riesgos importantes: accidentes, daño a la salud y peligro al conducir. Por eso la norma vigente, que fiscaliza la autoridad competente, establece límites: las personas menores de edad no consumen alcohol ni son atendidas con él, y tampoco se atiende con alcohol a quien está en estado de ebriedad. Un buen bar ofrece siempre una alternativa sin alcohol.",
        "En la formación, el estudiante trabaja solo con versiones sin alcohol y bajo supervisión del docente. Este cuaderno no enseña a preparar bebidas con alcohol: solo estudia conceptos, normas, fichas y costos en papel. Ante un malestar de una persona, se avisa a un adulto responsable y a los servicios de emergencia." + LIM,
    ],
    vocab=[("coctel", "bebida preparada con varios ingredientes, con o sin alcohol"), ("bebida alcohólica", "bebida que contiene alcohol"), ("bebida analcohólica", "bebida sin alcohol"), ("servicio responsable", "atender cumpliendo los límites de la norma y cuidando a las personas"), ("estado de ebriedad", "estado de una persona afectada por el alcohol")],
    worked=[
        ("Clasificar una bebida", "Un jugo de frutas con agua con gas, sin otros ingredientes. ¿Es alcohólica o analcohólica?", ["No contiene alcohol.", "Eso es una bebida analcohólica."], "Analcohólica"),
        ("Responder a una petición", "Un joven que aparenta ser menor de edad pide una bebida con alcohol. ¿Qué se hace?", ["Las personas menores de edad no son atendidas con alcohol.", "Se ofrece una opción sin alcohol."], "No se le atiende con alcohol y se ofrece una alternativa sin alcohol"),
    ],
    mistakes=[("Pensar que una persona mayor de edad puede probar bebidas con alcohol durante las prácticas de formación.", "En formación se trabaja solo con versiones sin alcohol y bajo supervisión.", "Usa solo versiones sin alcohol y sigue las indicaciones del docente."),
              ("Atender con alcohol a una persona con signos de ebriedad «porque es cliente habitual».", "Se la pone en riesgo y se incumple la norma.", "No la atiendes con alcohol, ofreces una alternativa y avisas al encargado.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es un coctel?", "Una bebida preparada con varios ingredientes, con alcohol o sin alcohol", "Una bebida que siempre contiene alcohol", "Un plato frío de entrada", "El coctel se define por la mezcla de ingredientes, no por llevar alcohol."),
        ("=", "{F} ¿Cuántas bebidas hay en la carta en total?", "3+4", "Se suman las bebidas con alcohol y sin alcohol.", " bebidas"),
        ("abc", "{F} Un joven de 16 años pide una bebida con alcohol. ¿Qué corresponde?", "No atenderlo con alcohol y ofrecerle una opción sin alcohol", "Atenderlo si insiste", "Atenderlo si dice que es para otra persona", "La norma impide atender con alcohol a menores de edad, sin importar el pedido."),
        ("abc", "{F} Una persona con signos de ebriedad pide otra bebida con alcohol. ¿Qué corresponde?", "No atenderla con alcohol, ofrecerle agua o una bebida sin alcohol y avisar al encargado", "Servirla, porque es cliente habitual", "Servirla con menos alcohol", "La ficha impide atender con alcohol a quien está en estado de ebriedad."),
        ("=", "Un bar de ejemplo ofrece 10 bebidas, de las cuales 6 son sin alcohol. ¿Qué porcentaje de la carta es sin alcohol?", "6*100//10", "Se multiplican las bebidas sin alcohol por 100 y se dividen por el total.", " %"),
        ("abc", "{F} ¿Con qué tipo de bebidas trabaja un estudiante en formación?", "Solo con versiones sin alcohol y bajo supervisión del docente", "Con y sin alcohol, bajo supervisión", "Con alcohol, si ya tiene 18 años", "La ficha limita el trabajo de formación a versiones sin alcohol."),
        ("abc", "{F} ¿Qué relación hay entre el alcohol y conducir?", "Conducir bajo el efecto del alcohol es un riesgo de accidentes", "Una pequeña cantidad mejora la concentración al conducir", "Solo es riesgoso conducir de noche", "La ficha incluye conducir bajo su efecto entre los riesgos del alcohol."),
        ("abc", "{F} ¿Qué debe ofrecer siempre el bar, según la ficha?", "Una alternativa sin alcohol", "Una bebida con alcohol destacada", "Un descuento por cantidad", "La ficha dice que se ofrece siempre una alternativa sin alcohol."),
        ("=", "Un bar de ejemplo atiende 8 horas con 25 bebidas por hora, y la mitad son sin alcohol. ¿Cuántas bebidas sin alcohol se sirven al día?", "8*25//2", "Se calculan las bebidas del día y se toma la mitad.", " bebidas"),
        ("abc", "{F} Un compañero propone probar una mezcla con alcohol «para saber cómo queda» durante la práctica. ¿Qué respuesta corresponde?", "No: en formación se trabaja solo con versiones sin alcohol y bajo supervisión", "Sí, si prueba muy poco", "Sí, si es mayor de edad", "La ficha excluye el alcohol de la práctica de formación."),
        ("abc", "{F} Un local anuncia consumo de alcohol «sin límite» por un precio fijo. ¿Qué observación corresponde?", "Contradice el principio de servicio responsable, que cuida los límites y a las personas", "Es una buena estrategia comercial", "Es obligatorio por norma", "El servicio responsable incluye evitar incentivos al consumo excesivo."),
        ("abc", "Una persona del público dice sentirse mal después de beber en el local. ¿Qué corresponde?", "Avisar de inmediato a un adulto responsable y a los servicios de emergencia", "Darle un remedio casero", "Pedirle que descanse y esperar", "Ante un malestar se pide ayuda de personal capacitado."),
        ("abc", "En Gastronomía: ¿para qué sirve ofrecer siempre una alternativa sin alcohol?", "Para que todas las personas, incluidas las que no pueden o no quieren beber alcohol, tengan una opción", "Para vender solo bebidas más baratas", "Para reemplazar las fichas de bebida", "La alternativa permite incluir a todos los clientes y cuidar su seguridad."),
    ],
    ctx=("abc", "{F} Un grupo de jóvenes llega a una mesa y uno de ellos aparenta ser menor de edad y pide una bebida con alcohol. ¿Qué debe hacer el garzón?", "Verificar la edad según el procedimiento del local y, si es menor o no puede acreditarla, atenderlo solo con opciones sin alcohol", "Atender a todos sin preguntar", "Servir el alcohol y avisar después a la jefa", "La norma impide atender con alcohol a menores; se verifica y se ofrece una alternativa."),
    sc=[
        ("En Gastronomía: ¿qué es una bebida analcohólica?", "Una bebida sin alcohol", "No contiene alcohol, a diferencia de una bebida alcohólica."),
        ("¿A quién no se atiende con alcohol?", "A menores de edad y a personas en estado de ebriedad", "Así lo establecen las reglas generales de la ficha."),
        ("¿Qué bebidas usa un estudiante en formación?", "Solo versiones sin alcohol y bajo supervisión", "Es una regla de seguridad de la formación."),
    ],
    op=("Un bar de ejemplo recibe a cuatro clientes: una persona adulta que pide un coctel con alcohol, un estudiante de 17 años que pide lo mismo, una persona con signos de ebriedad que pide otra bebida con alcohol y una familia que quiere una bebida para niños. "
        "Escribe qué harías con cada cliente (sin describir cómo se prepara ninguna bebida con alcohol) y por qué es importante que el bar ofrezca siempre una alternativa sin alcohol.",
        "Persona adulta: se le atiende según las reglas del local y la norma vigente. Estudiante de 17 años: no se le atiende con alcohol y se le ofrece una opción sin alcohol. Persona con ebriedad: no se le atiende con alcohol, se le ofrece agua o una bebida sin alcohol y se avisa al encargado. Familia: se ofrece una bebida sin alcohol. La alternativa sin alcohol permite que todos tengan una opción segura.",
        ["aplica la norma a los cuatro clientes", "ofrece alternativas sin alcohol cuando corresponde", "explica la importancia de la alternativa sin alcohol"],
        ["hoja con cuatro respuestas y una explicación"],
        ["servir alcohol al menor", "describir cómo preparar una bebida con alcohol", "no ofrecer una alternativa"],
        "Pregunta: «¿qué opción le ofreces al estudiante de 17 años?». Debe nombrar una alternativa sin alcohol."),
    reinforce="Escribe cinco reglas de servicio responsable de un bar y explica una con tus palabras.",
    extend="Explica por qué la formación en bar usa solo versiones sin alcohol aunque el oficio incluya bebidas alcohólicas.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 2 (ficha de bebida y documentos del bar, de ejemplo). «Refresco de frutas de ejemplo» (sin alcohol): jugo 90 ml; agua con gas 60 ml; endulzante líquido 10 ml; hielo según la ficha; vaso de 300 ml; decoración, 1 rodaja de limón. "
     "Documentos: ficha de bebida (ingredientes y medidas), inventario de bar (stock) y registro de mermas (lo que se pierde por derrames o roturas). Roles: la encargada de bar organiza; el bartender (persona que elabora las bebidas) las prepara; el garzón las sirve. Esta ficha sirve solo para calcular medidas y costos.")
build(
    O3, 2, F,
    use="Aprenderé a leer una ficha de bebida, a distinguir los documentos del bar y a reconocer el rol de cada persona del servicio.",
    prior=["Distingo bebidas con y sin alcohol.", "Sé sumar y multiplicar medidas.", "Conozco el inventario y la merma."],
    explain=[
        "Una ficha de bebida indica los ingredientes de una bebida con sus medidas, el tipo de vaso y la decoración. Las medidas se expresan en mililitros (ml): 1.000 ml son 1 litro. Sumar los líquidos permite saber cuánto volumen ocupan en el vaso, y multiplicarlos por el número de bebidas permite calcular lo que se necesita para una producción.",
        "El bar usa tres documentos: la ficha de bebida, el inventario de bar, que registra el stock de cada producto, y el registro de mermas, que anota lo que se pierde por derrames o roturas. La merma se expresa como porcentaje de lo preparado, calculado como lo perdido por 100 dividido por el total.",
        "Los roles son: la encargada de bar organiza y controla, el bartender elabora las bebidas y el garzón las sirve. Las medidas deben respetarse para que el producto sea siempre igual y el costo no se descontrole; se cambian solo con autorización." + LIM,
    ],
    vocab=[("ficha de bebida", "documento con ingredientes, medidas, vaso y decoración de una bebida"), ("mililitro (ml)", "milésima parte de un litro"), ("inventario de bar", "registro del stock de los productos del bar"), ("registro de mermas", "anotación de lo que se pierde por derrames o roturas"), ("bartender", "persona que elabora las bebidas en el bar")],
    worked=[
        ("Sumar volúmenes", "Una bebida de ejemplo lleva 100 ml de un líquido y 50 ml de otro. ¿Cuántos ml de líquido tiene?", ["Se suman los dos volúmenes.", "100 + 50 = 150."], "150 ml"),
        ("Calcular una merma", "Se prepararon 40 bebidas de ejemplo y se derramaron 2. ¿Qué porcentaje de merma hubo?", ["Se multiplican las perdidas por 100 y se dividen por el total.", "2 × 100 ÷ 40 = 5."], "5 %"),
    ],
    mistakes=[("Medir «a ojo» para ir más rápido.", "Las bebidas salen distintas y el costo de cada una cambia.", "Usa las medidas de la ficha de bebida."),
              ("No anotar un derrame porque fue pequeño.", "El registro de mermas deja de reflejar lo ocurrido y el inventario no cuadra.", "Anota todas las mermas, también las pequeñas.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es una ficha de bebida?", "Un documento con ingredientes, medidas, vaso y decoración de una bebida", "Una lista de clientes frecuentes", "El registro de ventas del día", "La ficha define cómo debe ser la bebida para que salga igual cada vez."),
        ("=", "{F} ¿Cuántos mililitros de líquido lleva el refresco de frutas (jugo, agua con gas y endulzante)?", "90+60+10", "Se suman los tres volúmenes de la ficha.", " ml"),
        ("=", "{F} Si el vaso es de 300 ml, ¿cuántos mililitros quedan libres después de los líquidos, para hielo y decoración?", "300-(90+60+10)", "Al volumen del vaso se le resta el volumen de los líquidos.", " ml"),
        ("=", "{F} Para 40 refrescos, ¿cuántos mililitros de jugo se necesitan?", "90*40", "Se multiplican los mililitros de jugo por el número de refrescos.", " ml"),
        ("abc", "{F} Si cada caja de jugo trae 1.000 ml, ¿cuántas cajas completas se necesitan para esos 40 refrescos?", "4 cajas", "3 cajas", "5 cajas", "Se necesitan 3.600 ml, que superan las 3 cajas y requieren una cuarta."),
        ("abc", "{F} ¿Qué documento registra lo que se pierde por derrames o roturas?", "El registro de mermas", "El inventario de bar", "La ficha de bebida", "La ficha lo asigna al registro de mermas."),
        ("abc", "{F} ¿Quién elabora las bebidas?", "El bartender", "El garzón", "La encargada de bar", "La ficha asigna la preparación al bartender y el servicio al garzón."),
        ("abc", "{F} ¿Quién sirve las bebidas a las personas?", "El garzón", "El bartender", "La encargada de bar", "La ficha asigna el servicio al garzón."),
        ("=", "En un día se prepararon 50 bebidas de ejemplo y se derramaron 3. ¿Qué porcentaje de merma hubo?", "3*100//50", "Se multiplican las bebidas perdidas por 100 y se dividen por el total.", " %"),
        ("abc", "En Gastronomía: ¿qué significa que una bebida sea analcohólica?", "Que no contiene alcohol", "Que se sirve sin hielo", "Que no lleva decoración", "Analcohólica significa sin alcohol, sin importar los otros ingredientes."),
        ("abc", "{F} Un bartender mide el jugo «a ojo» y a veces pone más de 90 ml. ¿Qué consecuencia tiene?", "La bebida cambia y el costo y el stock se descontrolan", "Ninguna, porque más jugo mejora la bebida", "Solo cambia el vaso", "Las medidas aseguran el producto y el control del costo."),
        ("=", "{F} Un bar prepara 120 refrescos en un día. ¿Cuántos mililitros de agua con gas se usan?", "60*120", "Se multiplican los mililitros de agua con gas por el número de refrescos.", " ml"),
        ("abc", "Los vasos y utensilios del bar deben tomarse por su base o exterior, con las manos limpias. ¿Cuál es la razón principal?", "Evitar contaminar las partes que tocan la bebida o la boca", "Que se vea más ordenado", "Que dure más el vaso", "La regla busca proteger las superficies que contactan con la bebida y las personas."),
    ],
    ctx=("abc", "{F} Una bartender nueva nota que el inventario dice 20 cajas de jugo, pero en la bodega hay 18. ¿Qué debe hacer?", "Revisar el registro de mermas y las salidas, y avisar a la encargada de bar de la diferencia", "Cambiar el inventario a 18 en silencio", "No hacer nada, porque 2 cajas es poco", "Una diferencia de inventario se investiga y se informa, no se oculta."),
    sc=[
        ("En Gastronomía: ¿en qué unidad se expresan las medidas de líquidos de la ficha?", "En mililitros (ml)", "Son la unidad usada en las fichas de bebida."),
        ("¿Quién prepara las bebidas del bar?", "El bartender", "Es el rol que las elabora."),
        ("¿Qué se anota en el registro de mermas?", "Lo que se pierde por derrames o roturas", "Permite controlar el inventario real del bar."),
    ],
    op=("Ficha de ejemplo «Refresco de piña de ejemplo» (sin alcohol): jugo 120 ml, agua con gas 80 ml, endulzante 20 ml; vaso de 400 ml. Se preparan 60 refrescos y se derraman 3. "
        "Calcula el volumen de líquido de un refresco, el espacio libre del vaso, los mililitros de jugo para 60 refrescos y el porcentaje de merma; indica además qué documento registra el derrame.",
        "Líquidos: 120 + 80 + 20 = 220 ml. Espacio libre: 400 − 220 = 180 ml. Jugo para 60: 120 × 60 = 7.200 ml. Merma: 3 × 100 ÷ 60 = 5 %. El derrame se anota en el registro de mermas.",
        ["calcula 220 ml y 180 ml", "calcula 7.200 ml y 5 %", "nombra el registro de mermas"],
        ["hoja con cálculos y documento"],
        ["olvidar sumar el endulzante", "calcular la merma sobre un total equivocado", "no nombrar el documento"],
        "Pregunta: «¿cuántos ml son 7.200 en litros?». Debe responder 7,2 litros."),
    reinforce="Inventa una ficha de bebida sin alcohol con tres líquidos y calcula el volumen para 25 bebidas.",
    extend="Explica por qué anotar las mermas ayuda a que el inventario coincida con lo que hay en el bar.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 3 (costeo de bar de ejemplo, inventado). Botella de concentrado de frutas de ejemplo (sin alcohol): 750 ml, precio $9.000; porción de ejemplo de 30 ml; merma de ejemplo de 30 ml por botella (derrames y restos). "
     "Caja de jugo: 1.000 ml, $1.500; porción de 100 ml. Botella de agua con gas: 500 ml, $900; porción de 100 ml. Costo objetivo de ejemplo: 25 % del precio de venta. "
     "Estos datos se usan solo para calcular porciones y costos en papel: este cuaderno no enseña a preparar bebidas con alcohol, y el estudiante en formación trabaja solo con versiones sin alcohol bajo supervisión.")
build(
    O3, 3, F,
    use="Aprenderé a analizar un caso de bar en papel: calcular cuántas porciones rinde un envase, el costo por porción y el precio de venta de una bebida.",
    prior=["Conozco la merma.", "Conozco el costo objetivo.", "Sé dividir y calcular porcentajes."],
    explain=[
        "Un envase rinde porciones: se calculan dividiendo el contenido útil por el tamaño de la porción. El contenido útil es el contenido total menos la merma, que es lo que se pierde por derrames y restos. El costo por porción es el precio del envase dividido por las porciones que rinde.",
        "Una bebida mezcla varios ingredientes, por lo que su costo es la suma de los costos por porción de cada ingrediente. Con el costo objetivo se calcula el precio de venta: el costo se multiplica por 100 y se divide por el porcentaje objetivo. Así se compara una bebida con otra y se decide qué ofrecer.",
        "En formación se trabaja solo con versiones sin alcohol, por eso todos los envases de este ejemplo son sin alcohol. Los valores de esta clase son de ejemplo; solo se hacen cálculos en papel." + LIM,
    ],
    vocab=[("contenido útil", "contenido total menos la merma"), ("porción", "cantidad de un ingrediente que se usa en una bebida"), ("rendimiento de un envase", "cantidad de porciones que da"), ("costo por porción", "precio del envase dividido por las porciones"), ("precio de venta", "valor al que se ofrece la bebida")],
    worked=[
        ("Calcular porciones de un envase", "Una botella de ejemplo de 500 ml tiene una merma de 20 ml y se usan porciones de 40 ml. ¿Cuántas porciones rinde?", ["Contenido útil: 500 − 20 = 480 ml.", "480 ÷ 40 = 12."], "12 porciones"),
        ("Calcular el costo por porción", "Un envase de ejemplo cuesta $3.000 y rinde 15 porciones. ¿Cuánto cuesta cada porción?", ["Se divide el precio por las porciones.", "3.000 ÷ 15 = 200."], "$200"),
    ],
    mistakes=[("Calcular las porciones sin descontar la merma.", "El rendimiento queda sobrestimado y el costo por porción sale menor al real.", "Resta primero la merma al contenido total."),
              ("Fijar el precio igual al costo de la bebida.", "No queda margen para cubrir otros gastos.", "Usa el costo objetivo para calcular un precio con margen.")],
    T=[
        ("=", "{F} ¿Cuántos mililitros útiles tiene la botella de concentrado, después de la merma?", "750-30", "Al contenido total se le resta la merma.", " ml"),
        ("=", "{F} ¿Cuántas porciones rinde la botella de concentrado?", "(750-30)//30", "Se divide el contenido útil por el tamaño de la porción.", " porciones"),
        ("=", "{F} ¿Cuánto cuesta cada porción del concentrado?", "9000//24", "Se divide el precio de la botella por las porciones que rinde.", " pesos"),
        ("=", "{F} ¿Cuántas porciones de 100 ml rinde la caja de jugo?", "1000//100", "Se divide el contenido de la caja por el tamaño de la porción.", " porciones"),
        ("=", "{F} ¿Cuánto cuesta cada porción de jugo?", "1500//10", "Se divide el precio de la caja por las porciones que rinde.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta cada porción de agua con gas?", "900//5", "Se divide el precio de la botella por las 5 porciones de 100 ml que rinde.", " pesos"),
        ("=", "{F} Una bebida sin alcohol lleva una porción de jugo y una de agua con gas. ¿Cuál es su costo?", "150+180", "Se suman los costos por porción de los dos ingredientes.", " pesos"),
        ("=", "{F} ¿Cuál es el precio de venta de esa bebida sin alcohol con el costo objetivo?", "330*100//25", "Se multiplica el costo por 100 y se divide por el porcentaje objetivo.", " pesos"),
        ("abc", "{F} ¿Por qué se resta la merma antes de calcular las porciones de la botella?", "Porque el contenido que se pierde no se puede servir", "Porque la merma baja el precio de la botella", "Porque la merma aumenta el número de porciones", "Lo que se pierde no forma parte de las porciones servibles."),
        ("=", "{F} Si la merma de la botella fuera de 0 ml, ¿cuántas porciones rendiría?", "750//30", "Se divide el contenido total por el tamaño de la porción.", " porciones"),
        ("abc", "{F} Un bar de formación decide qué ofrecer a sus estudiantes. ¿Qué opción corresponde según la ficha?", "La bebida sin alcohol, bajo supervisión del docente", "La bebida con alcohol, para practicar con el costo real", "Ambas, según el interés del estudiante", "La ficha limita la formación a versiones sin alcohol."),
        ("=", "{F} Si se venden 60 bebidas sin alcohol al precio calculado de $1.320, ¿cuánto se obtiene?", "1320*60", "Se multiplica el precio de una bebida por el número de bebidas vendidas.", " pesos"),
        ("abc", "{F} Si el precio de la caja de jugo sube a $2.000, ¿qué le ocurre al costo de la bebida sin alcohol?", "Sube, porque el jugo cuesta más por porción", "Baja, porque el jugo es más caro", "Se mantiene, porque la porción es igual", "El costo por porción del jugo aumenta y arrastra al costo de la bebida."),
    ],
    ctx=("abc", "{F} El encargado calcula el rendimiento de la botella de concentrado sin descontar la merma de 30 ml. ¿Qué error comete?", "Sobrestima las porciones y subestima el costo por porción", "Subestima las porciones y sobrestima el costo", "No comete ningún error", "Sin restar la merma, el rendimiento parece mayor y el costo por porción menor."),
    sc=[
        ("En Gastronomía: ¿cómo se calcula el contenido útil de un envase?", "Contenido total menos la merma", "Lo que se pierde no se puede servir."),
        ("¿Cómo se calcula el costo por porción?", "Precio del envase dividido por las porciones", "Reparte el costo entre las porciones."),
        ("¿Qué bebidas se trabajan en formación?", "Solo versiones sin alcohol", "Es una regla de seguridad de la formación."),
    ],
    op=("Datos de ejemplo: caja de jugo de 1.000 ml, $1.200, porción de 125 ml; botella de bebida con gas sin alcohol de 1.000 ml, $1.000, porción de 125 ml; costo objetivo del 25 %. Una bebida sin alcohol lleva una porción de cada una. "
        "Calcula las porciones que rinde cada envase, el costo de cada porción, el costo de la bebida y su precio de venta.",
        "Porciones de jugo: 1.000 ÷ 125 = 8; costo por porción: 1.200 ÷ 8 = 150. Porciones de bebida con gas: 8; costo por porción: 1.000 ÷ 8 = 125. Costo de la bebida: 150 + 125 = 275. Precio de venta: 275 × 100 ÷ 25 = 1.100 pesos.",
        ["calcula 8 porciones por envase", "calcula 150, 125 y 275", "calcula 1.100 de precio"],
        ["hoja con cálculos"],
        ["no dividir por la porción", "sumar mal los costos", "fijar el precio igual al costo"],
        "Pregunta: «¿cuántas porciones de 125 ml hay en 1.000 ml?». Debe responder 8."),
    reinforce="Inventa dos ingredientes sin alcohol con envase, precio y porción, y calcula el costo y precio de una bebida.",
    extend="Explica por qué un bar debe calcular su merma real y no suponer que no hay pérdidas.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 4 (carta e inventario de bar de ejemplo, inventados). Carta sin alcohol: bebida A, costo $350; bebida B, costo $500; costo objetivo del 25 % del precio de venta. Ventas de un día: 40 bebidas A y 30 bebidas B. "
     "Inventario de cajas de jugo: stock inicial 20; entradas 30; salidas de 12, 15 y 9; stock mínimo 10; stock objetivo 40. Criterio de servicio responsable: la carta destaca las opciones sin alcohol e informa los ingredientes y alérgenos de cada bebida.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: fijar precios con un costo objetivo, calcular ventas y margen, y controlar el inventario de un bar.",
    prior=["Conozco el costo objetivo y el precio de venta.", "Conozco el inventario y el stock mínimo.", "Sé multiplicar y restar."],
    explain=[
        "Con el costo de cada bebida y el costo objetivo se calcula el precio de venta. Las ventas del día son el precio por las unidades vendidas; el costo del día es el costo por las unidades vendidas; y el margen es la diferencia entre ambos, que debe cubrir otros gastos y dejar una ganancia.",
        "El inventario del bar se controla con el stock: el stock final es el inicial más las entradas menos las salidas. Si el stock queda bajo el mínimo, se pide para llegar al stock objetivo. Un buen control evita quedarse sin producto y también acumular de más.",
        "La carta debe informar los ingredientes y los alérgenos de cada bebida y destacar las opciones sin alcohol, como parte del servicio responsable. Todas las cifras son de ejemplo y solo se calcula en papel. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("ventas", "dinero que se obtiene al vender: precio por unidades"), ("costo del día", "costo por las unidades vendidas"), ("margen", "diferencia entre las ventas y el costo"), ("stock objetivo", "nivel al que se quiere llegar al reponer"), ("carta", "lista de productos que ofrece un servicio, con sus precios")],
    worked=[
        ("Calcular un margen", "Un producto de ejemplo se vende a $800 y cuesta $200. Se venden 10 unidades. ¿Cuál es el margen?", ["Ventas: 800 × 10 = 8.000. Costo: 200 × 10 = 2.000.", "Margen: 8.000 − 2.000 = 6.000."], "$6.000"),
        ("Calcular una cantidad a pedir", "Un producto de ejemplo tiene stock de 12 y el objetivo es 30. ¿Cuánto se pide?", ["Se resta el stock actual al objetivo.", "30 − 12 = 18."], "18 unidades"),
    ],
    mistakes=[("Calcular el margen sin restar el costo de las bebidas vendidas.", "Se confunde la venta con la ganancia.", "Resta el costo del día a las ventas del día."),
              ("Esperar a que el stock llegue a cero para pedir.", "Se queda sin producto antes de que llegue el pedido.", "Pide cuando llegue al stock mínimo.")],
    T=[
        ("=", "{F} ¿Cuál es el precio de venta de la bebida A?", "350*100//25", "Se multiplica el costo por 100 y se divide por el costo objetivo.", " pesos"),
        ("=", "{F} ¿Cuál es el precio de venta de la bebida B?", "500*100//25", "Se multiplica el costo por 100 y se divide por el costo objetivo.", " pesos"),
        ("=", "{F} ¿Cuánto se vendió en el día de la bebida A?", "1400*40", "Se multiplica el precio por las unidades vendidas.", " pesos"),
        ("=", "{F} ¿Cuánto se vendió en el día de la bebida B?", "2000*30", "Se multiplica el precio por las unidades vendidas.", " pesos"),
        ("=", "{F} ¿Cuál fue el costo del día de las dos bebidas?", "350*40+500*30", "Se suman los costos de las unidades vendidas de A y de B.", " pesos"),
        ("=", "{F} ¿Cuál fue el margen del día?", "1400*40+2000*30-(350*40+500*30)", "A las ventas del día se les resta el costo del día.", " pesos"),
        ("=", "{F} ¿Cuántas cajas de jugo hay en stock?", "20+30-(12+15+9)", "Al stock inicial se suman las entradas y se restan las salidas.", " cajas"),
        ("abc", "{F} Con ese stock, ¿hay que pedir jugo?", "No, porque el stock supera el mínimo de 10", "Sí, porque no llega al objetivo de 40", "Sí, porque hubo salidas", "El stock actual de 14 está sobre el mínimo, que es el aviso de pedido."),
        ("=", "{F} ¿Cuántas cajas habría que pedir para llegar al stock objetivo?", "40-14", "Al stock objetivo se le resta el stock actual.", " cajas"),
        ("abc", "{F} ¿Qué debe informar la carta, además de los precios, según el criterio de servicio responsable?", "Los ingredientes y alérgenos de cada bebida, y destacar las opciones sin alcohol", "Solo el nombre de la bebida", "Solo las bebidas más vendidas", "La ficha incluye información de ingredientes y alérgenos como criterio de servicio."),
        ("abc", "{F} Una compañera propone fijar la bebida B en $1.000 porque «es un precio redondo». ¿Qué debe revisarse?", "Que $1.000 respete el costo objetivo: el costo de $500 sería el 50 % del precio", "Nada, porque un precio redondo siempre es mejor", "Que el precio sea el doble del precio de A", "Con $1.000 los ingredientes serían el 50 % del precio, superando el 25 % objetivo."),
        ("=", "{F} Si la bebida A se vendiera a $1.800 en lugar de $1.400, ¿cuánto sería la venta de las 40 unidades?", "1800*40", "Se multiplica el nuevo precio por las unidades vendidas.", " pesos"),
        ("abc", "{F} Una jefa quiere destacar una bebida con alcohol en la carta del colegio. ¿Qué corresponde?", "Destacar las opciones sin alcohol, y respetar la norma vigente sobre la venta a menores", "Destacar la bebida con alcohol para vender más", "Eliminar toda opción sin alcohol", "La ficha pide destacar las opciones sin alcohol como parte del servicio responsable."),
    ],
    ctx=("abc", "{F} Al cerrar el día, el margen parece alto, pero el stock de jugo bajó cerca del mínimo. ¿Qué decisión es más razonable?", "Calcular la cantidad a pedir para llegar al stock objetivo y anticiparse a la falta", "Esperar a que se acabe el jugo", "Subir los precios sin revisar el inventario", "El margen no reemplaza el control de stock; se pide antes de quedarse sin producto."),
    sc=[
        ("En Gastronomía: ¿cómo se calcula el margen del día?", "Ventas del día menos costo del día", "Muestra lo que queda después de pagar los ingredientes."),
        ("¿Cuándo se pide un producto?", "Cuando el stock llega al mínimo", "Así se evita quedarse sin producto."),
        ("¿Qué debe informar la carta?", "Ingredientes, alérgenos y opciones sin alcohol", "Es parte del servicio responsable del bar."),
    ],
    op=("Carta sin alcohol de ejemplo: bebida C, costo $420; bebida D, costo $600; costo objetivo del 40 %. Ventas del día: 25 bebidas C y 20 bebidas D. Inventario de cajas de jugo: stock inicial 18; entrada 22; salidas de 10 y 14; stock mínimo 8 y stock objetivo 30. "
        "Calcula los precios de venta, las ventas y el costo del día, el margen y el stock final; indica si hay que pedir y cuánto, y qué información agregarías a la carta.",
        "Precios: C, 420 × 100 ÷ 40 = 1.050; D, 600 × 100 ÷ 40 = 1.500. Ventas: 1.050 × 25 + 1.500 × 20 = 26.250 + 30.000 = 56.250. Costo: 420 × 25 + 600 × 20 = 10.500 + 12.000 = 22.500. Margen: 33.750. Stock final: 18 + 22 − (10 + 14) = 16. No hay que pedir, porque supera el mínimo de 8; para llegar al objetivo faltarían 14. En la carta: ingredientes, alérgenos y destacar las opciones sin alcohol.",
        ["calcula precios de 1.050 y 1.500", "calcula ventas, costo y margen", "calcula el stock de 16 y decide sobre el pedido"],
        ["hoja con cálculos y una mejora de la carta"],
        ["usar el 30 %", "no restar el costo", "pedir aunque supere el mínimo"],
        "Pregunta: «¿qué costo objetivo se usa?». Debe responder 40 %."),
    reinforce="Inventa dos bebidas sin alcohol con su costo, calcula el precio de venta con un costo objetivo y el margen de un día.",
    extend="Explica por qué un bar puede ganar bien aunque ofrezca opciones sin alcohol destacadas.",
)
