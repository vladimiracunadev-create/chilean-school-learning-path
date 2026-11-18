"""Forestal TP 3.º y 4.º medio: OAE-06 (prevención de incendios forestales: conceptos, planes y cálculos en papel). Sin procedimientos de combate, de quema ni de uso del fuego."""
from __future__ import annotations

from tp_fore_common import AVISO, EMER, build

O6 = "TP-FORE-3y4-OAE-06"

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Predio Demo: 200 ha, de las cuales 150 ha son plantación de «especie A» y 50 ha, bosque nativo. "
     "Peligros anotados para la temporada de mayor amenaza de incendios: humo, calor, cambios en el avance del fuego, caída de árboles, terreno con pendiente y trabajos que generan chispas. "
     "El plan de prevención programa 24 jornadas de trabajo con máquinas en la temporada.")
build(
    O6, 1, F,
    use="Aprenderé qué es un incendio forestal, qué factores influyen, qué es prevenir y qué es combatir, y por qué el combate lo hacen solo brigadas entrenadas y autorizadas.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé calcular porcentajes simples.", "Sé qué es una hectárea."],
    explain=[
        "Un incendio forestal es un fuego que se propaga sin control en bosques, plantaciones o matorrales. Para que exista se necesitan combustible, calor y oxígeno. El combustible forestal es el material vegetal que puede arder, como hojas secas, ramas y pastos. La temperatura, la humedad del aire, el viento y el relieve del terreno influyen en lo rápido que se propaga. La mayoría de los incendios forestales se inicia por actividades humanas, y por eso la prevención es tan importante.",
        "Prevenir es evitar que un incendio se inicie o reducir su daño: controlar las actividades que generan chispas, mantener franjas libres de vegetación combustible, vigilar y avisar a tiempo. Combatir es actuar sobre un incendio ya iniciado, y lo hacen brigadas entrenadas, con equipos, comunicaciones y un plan. No es una tarea de estudiantes ni de personas sin formación. Si ves humo o fuego, te alejas y avisas.",
        f"Este cuaderno no explica cómo se combate un incendio ni cómo se usa el fuego. {EMER} {AVISO}",
    ],
    vocab=[("incendio forestal", "fuego que se propaga sin control en bosques, plantaciones o matorrales"), ("combustible forestal", "material vegetal que puede arder, como hojas secas, ramas y pastos"), ("prevención", "acciones para evitar que un incendio se inicie o reducir su daño"), ("combate", "acciones sobre un incendio ya iniciado, que realizan brigadas entrenadas"), ("amenaza de incendio", "nivel de condiciones favorables para que un incendio se inicie y se propague"), ("franja libre de vegetación", "faja de terreno sin material que pueda arder")],
    worked=[
        ("Prevenir o combatir", "En un predio de ejemplo se mantiene una franja sin vegetación seca alrededor de un camino. ¿Es prevención o combate?", ["La franja se mantiene antes de que haya fuego.", "Evitar o reducir daños antes es prevención."], "Prevención"),
        ("Porcentaje suspendido", "En un plan de ejemplo se programan 20 jornadas con máquinas y 5 se suspenden por alta amenaza. ¿Qué porcentaje se suspende?", ["5 ÷ 20 son 25 de cada 100.", "Se suspende el 25 %."], "25 %"),
    ],
    mistakes=[("Creer que quien aprendió conceptos de incendios puede ayudar a apagar uno.", "El combate lo hacen brigadas entrenadas, con equipos y un plan.", "Si ves humo o fuego, te alejas y avisas a un adulto responsable y a emergencias."),
              ("Creer que el humo no es peligroso si el fuego está lejos.", "El humo puede intoxicar y desorientar a las personas.", "Aléjate y avisa; no te acerques a mirar.")],
    T=[
        ("abc", "En Forestal: ¿qué es un incendio forestal?", "Un fuego que se propaga sin control en bosques, plantaciones o matorrales", "Una quema planificada y autorizada por la autoridad", "Una fogata pequeña dentro de un fogón de campamento", "El incendio forestal es un fuego sin control; la quema planificada es otra cosa."),
        ("abc", "En Forestal: ¿qué es el combustible forestal?", "El material vegetal que puede arder, como hojas secas, ramas y pastos", "La gasolina que usan las máquinas", "El oxígeno del aire que alimenta el fuego", "El combustible forestal es vegetación; la gasolina es combustible de máquinas."),
        ("abc", "En Forestal: ¿qué son las medidas de prevención de incendios?", "Acciones para evitar que un incendio se inicie o reducir su daño", "Acciones para reparar el bosque después de un incendio", "Acciones para apagar un incendio ya iniciado", "La prevención actúa antes; el combate actúa sobre el fuego ya iniciado."),
        ("=", "{F} ¿Qué porcentaje del predio es plantación?", "150*100//200", "Se divide las hectáreas de plantación entre las del predio y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «humo»?", "Que las personas respiren humo, se intoxiquen o se desorienten", "El humo que se ve en el cielo", "Que cambie el color del paisaje", "El riesgo es la posibilidad de daño a las personas; el humo es la fuente del peligro."),
        ("abc", "{F} Una regla que suspende los trabajos que generan chispas en los días de alta amenaza es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el lugar", "De EPP, porque protege al personal", "Una regla de trabajo es un control administrativo."),
        ("abc", "{F} Una franja libre de vegetación combustible alrededor de un camino del predio es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla escrita", "De EPP, porque protege a las personas", "La franja cambia el terreno y dificulta la propagación sin depender de las personas."),
        ("=", "{F} Si en los días de alta amenaza se suspenden 6 de las 24 jornadas con máquinas, ¿qué porcentaje se suspende?", "6*100//24", "Se divide las jornadas suspendidas entre las programadas y se multiplica por 100.", " %"),
        ("abc", "{F} Una estudiante dice: «aprendí de incendios, así que puedo ayudar a apagar uno pequeño en el predio». ¿Qué respuesta es correcta?", "Es falso: el combate lo hacen brigadas entrenadas; ella debe alejarse y avisar", "Es cierto, si el fuego es pequeño", "Es cierto, si usa casco y guantes", "Un fuego pequeño puede crecer rápido; el combate exige entrenamiento y plan."),
        ("abc", "Durante una visita de ejemplo, ves humo en una ladera cercana. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte para comprobar qué es", "Grabar un video desde cerca para mostrarlo", "Acercarse aumenta el peligro; lo correcto es alejarse y avisar."),
        ("abc", "En Forestal: ¿por qué la prevención es más efectiva que el combate?", "Porque evita que el fuego se inicie y reduce el peligro para las personas", "Porque el combate no tiene ningún riesgo", "Porque prevenir siempre cuesta más que combatir", "Prevenir actúa antes del daño; combatir ya ocurre con el fuego encendido."),
        ("=", "{F} Una franja libre de vegetación de ejemplo mide 1.000 m de largo y 20 m de ancho. ¿Cuántas hectáreas ocupa?", "1000*20//10000", "Se calcula el área de la franja en m² y se pasa a hectáreas.", " ha"),
        ("abc", "{F} Un equipo propone hacer trabajos con chispas en un día de alta amenaza «para terminar rápido». ¿Qué corresponde?", "Suspender o reprogramar el trabajo según el plan de prevención", "Hacerlo, si se termina antes del mediodía", "Hacerlo, si se lleva más personal", "El plan de prevención restringe actividades con chispas en días de alta amenaza."),
    ],
    ctx=("abc", "Un conocido quiere quemar rastrojos en su campo en un día seco y te pide ayuda «porque sabes de incendios». ¿Qué respondes?", "Que no, porque las quemas exigen autorización y personal capacitado, y que lo consultarás con un adulto responsable", "Que sí, si el fuego es pequeño", "Que sí, si hay agua cerca", "Un fuego pequeño o agua cercana no reemplazan la autorización ni la formación."),
    sc=[
        ("En Forestal: ¿qué se necesita para que exista fuego?", "Combustible, calor y oxígeno", "Sin alguno de los tres elementos el fuego no existe."),
        ("¿Quiénes combaten los incendios forestales?", "Brigadas entrenadas, con equipos y un plan", "El combate exige entrenamiento y coordinación."),
        ("¿Qué haces si ves humo o fuego?", "Alejarme y avisar a un adulto responsable y a emergencias", "Acercarse aumenta el riesgo para las personas."),
    ],
    op=("Ficha de ejemplo: predio «Muestra», 300 ha, de las cuales 240 ha son plantación y 60 ha, bosque nativo. El plan programa 30 jornadas con máquinas y prevé suspender 9 en los días de alta amenaza. Escribe (a) qué porcentaje del predio es plantación, (b) qué porcentaje de las jornadas se suspende, (c) un control administrativo y uno de ingeniería para prevenir incendios, (d) qué haces si ves humo.",
        "(a) 240 ÷ 300 = 80 %. (b) 9 ÷ 30 = 30 %. (c) Administrativo: suspender trabajos con chispas en días de alta amenaza; ingeniería: mantener una franja libre de vegetación combustible. (d) Me alejo, no me acerco, aviso a un adulto responsable y a emergencias.",
        ["calcula los dos porcentajes", "propone controles de tipos distintos", "indica que se aleja y avisa", "distingue prevención de combate"],
        ["hoja con las cuatro respuestas"],
        ["proponer combatir el incendio", "confundir los tipos de control", "no indicar a quién se avisa"],
        "Pregunta: «¿qué es lo primero que haces si ves fuego?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres ejemplos de actividades que pueden generar chispas y una regla de prevención para cada una.",
    extend="Explica con un ejemplo por qué el humo es un peligro aunque el fuego esté lejos.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (documentos y datos de ejemplo, inventados). Plan de prevención del predio «Demo Sur»: mapa de riesgo con tres sectores. Sector A, riesgo alto, 30 ha, junto a un camino público; sector B, riesgo medio, 50 ha; sector C, riesgo bajo, 120 ha. "
     "Sistema de alerta con tres niveles de ejemplo: verde, amenaza baja; amarillo, amenaza media; rojo, amenaza alta con restricciones de trabajos que generan chispas. "
     "El plan incluye una ruta de evacuación, un punto de reunión, la cadena de mando y una lista de contactos de emergencia.")
build(
    O6, 2, F,
    use="Aprenderé los documentos de un plan de prevención de incendios, la cadena de mando, el sistema de alerta, cómo se comunica un aviso y los roles.",
    prior=["Sé qué es prevenir y combatir.", "Sé calcular porcentajes simples.", "Sé qué es un mapa y un registro."],
    explain=[
        "El plan de prevención reúne los documentos que ordenan qué hacer antes y durante una emergencia. El mapa de riesgo clasifica los sectores según su amenaza. El sistema de alerta define niveles y qué se restringe en cada uno. La ruta de evacuación y el punto de reunión indican por dónde salir y dónde juntarse en un lugar seguro. La lista de contactos dice a quién avisar. Todos deben conocer el plan, que debe estar visible y actualizado.",
        "La cadena de mando es el orden de quién da las instrucciones: en una emergencia la orden la da el jefe definido en el plan y no la primera persona que llega. Al avisar de un fuego se informa qué se ve, dónde, desde cuándo y quién avisa, con palabras claras. Los roles son el encargado de prevención, que planifica; el vigía, que observa y avisa; el jefe de emergencia, que ordena; las brigadas entrenadas, que combaten; y la autoridad forestal, que fiscaliza.",
        f"Estos conceptos permiten leer los documentos, pero no habilitan para combatir un incendio. {EMER} {AVISO}",
    ],
    vocab=[("mapa de riesgo", "mapa que clasifica los sectores según su amenaza de incendio"), ("sistema de alerta", "niveles que informan la amenaza y lo que se restringe en cada uno"), ("ruta de evacuación", "camino señalizado para salir de una zona en una emergencia"), ("punto de reunión", "lugar seguro y conocido donde se junta el personal"), ("cadena de mando", "orden de quién da las instrucciones en una emergencia"), ("vigía", "persona que observa el territorio y avisa si ve humo o fuego")],
    worked=[
        ("Elegir el documento", "Una persona de ejemplo quiere saber a quién avisar si ve humo. ¿Qué parte del plan consulta?", ["Los contactos aparecen en un documento específico.", "Es la lista de contactos de emergencia."], "La lista de contactos de emergencia"),
        ("Porcentaje de un sector", "Un predio de ejemplo tiene 300 ha y su sector de riesgo alto mide 60 ha. ¿Qué porcentaje es?", ["60 ÷ 300 son 20 de cada 100.", "El sector es el 20 % del predio."], "20 %"),
    ],
    mistakes=[("Creer que cualquier persona puede dar órdenes en una emergencia.", "Las órdenes las da el jefe definido en la cadena de mando.", "Sigue la cadena de mando y avisa a quien corresponde."),
              ("Avisar solo «hay un incendio» sin lugar ni detalles.", "Sin lugar ni hora, la ayuda no sabe adónde ir ni qué esperar.", "Informa qué ves, dónde, desde cuándo y quién eres.")],
    T=[
        ("abc", "En Forestal: ¿cuáles son los tres elementos que necesita el fuego?", "Combustible, calor y oxígeno", "Combustible, agua y viento", "Calor, humo y cenizas", "El fuego necesita combustible, calor y oxígeno; el agua y el humo no son parte de ese conjunto."),
        ("abc", "En Forestal: ¿qué es un mapa de riesgo de incendios?", "Un mapa que clasifica los sectores según su amenaza de incendio", "Un mapa que solo muestra los caminos del predio", "Una lista de las herramientas de combate", "El mapa de riesgo agrupa sectores por su amenaza."),
        ("abc", "En Forestal: ¿qué es un punto de reunión?", "Un lugar seguro y conocido al que se llega ante una evacuación", "El lugar desde donde comienza el combate", "La oficina donde se guardan las actas", "El punto de reunión permite verificar que todas las personas estén a salvo."),
        ("=", "{F} ¿Cuántas hectáreas suman los tres sectores del mapa de riesgo?", "30+50+120", "Se suman las hectáreas de los tres sectores.", " ha"),
        ("=", "{F} ¿Qué porcentaje del predio es el sector A, de riesgo alto?", "30*100//(30+50+120)", "Se divide las hectáreas del sector entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje del predio tiene riesgo alto o medio?", "(30+50)*100//(30+50+120)", "Se suman las hectáreas de ambos sectores y se compara con el total.", " %"),
        ("abc", "{F} ¿Qué sector necesita más vigilancia por su amenaza?", "El sector A, de riesgo alto", "El sector C, porque es el más grande", "El sector B, porque queda al centro", "La vigilancia se prioriza por amenaza y no por tamaño."),
        ("abc", "{F} Se anuncia el nivel rojo del sistema de alerta. ¿Qué corresponde en el predio?", "Aplicar las restricciones del plan, como suspender trabajos que generan chispas", "Seguir con las actividades como siempre", "Aumentar los trabajos con máquinas para terminar antes", "El nivel rojo activa las restricciones que fija el plan."),
        ("abc", "{F} En una emergencia, ¿quién da las instrucciones?", "El jefe definido en la cadena de mando", "La primera persona que llega al lugar", "El visitante de más edad", "La cadena de mando evita órdenes contradictorias."),
        ("abc", "{F} ¿Qué información debe darse al avisar de humo o fuego?", "Qué se ve, dónde, desde cuándo y quién avisa", "Solo la frase «hay un incendio»", "Una opinión sobre quién lo causó", "Un aviso claro permite que la ayuda llegue al lugar correcto."),
        ("abc", "En Forestal: ¿por qué el plan de prevención debe estar visible y ser conocido por todo el personal?", "Porque todas las personas deben saber qué hacer, a quién avisar y adónde ir", "Porque así nadie necesita capacitación", "Porque la autoridad lo pide solo para sancionar", "Un plan que nadie conoce no sirve en una emergencia."),
        ("=", "{F} Si hubiera un vigía por cada 40 ha de riesgo alto o medio, redondeando hacia arriba, ¿cuántos vigías se necesitarían?", "(30+50+39)//40", "Se suman las hectáreas de riesgo alto y medio, se dividen entre 40 y se redondea hacia arriba.", " vigías"),
        ("abc", "{F} El mapa de riesgo tiene una fecha antigua y desde entonces cambió el uso de varios sectores. ¿Qué corresponde?", "Actualizar el mapa antes de seguir usándolo", "Seguir usándolo, porque los mapas no caducan", "Eliminar los sectores que cambiaron", "Un mapa desactualizado puede llevar a decisiones equivocadas."),
    ],
    ctx=("abc", "Ves humo en un cerro cercano y un amigo propone ir a mirar de cerca «para saber si es peligroso». ¿Qué respondes?", "Que no, porque hay que alejarse, y avisar a un adulto responsable y a emergencias", "Que sí, pero solo un rato", "Que sí, si llevan agua", "Acercarse aumenta el riesgo; lo correcto es alejarse y avisar."),
    sc=[
        ("En Forestal: ¿qué es la cadena de mando?", "El orden de quién da las instrucciones en una emergencia", "Así se evitan órdenes contradictorias entre distintas personas."),
        ("¿Qué datos se dan al avisar de un fuego?", "Qué se ve, dónde, desde cuándo y quién avisa", "Un aviso claro permite una respuesta rápida."),
        ("¿Qué es un punto de reunión?", "Un lugar seguro y conocido donde se junta el personal", "Permite comprobar que todos estén a salvo."),
    ],
    op=("Ficha de ejemplo: plan de prevención del predio «Demo Norte». Sector X, riesgo alto, 40 ha; sector Y, riesgo medio, 60 ha; sector Z, riesgo bajo, 100 ha. Niveles de alerta: verde, amarillo y rojo. Escribe (a) el total de hectáreas y el porcentaje del sector X, (b) cuántos vigías hacen falta si hay uno por cada 50 ha de riesgo alto o medio, redondeando hacia arriba, (c) qué datos das al avisar de humo, (d) quién da las instrucciones en una emergencia.",
        "(a) 40 + 60 + 100 = 200 ha; 40 ÷ 200 = 20 %. (b) (40 + 60) ÷ 50 = 2 vigías. (c) Qué veo, dónde, desde cuándo y quién soy. (d) El jefe definido en la cadena de mando.",
        ["calcula el total y el porcentaje", "calcula los vigías", "indica los datos del aviso", "identifica quién da las órdenes"],
        ["hoja con las cuatro respuestas"],
        ["calcular mal el porcentaje", "avisar sin lugar", "creer que cualquiera da órdenes"],
        "Pregunta: «¿qué necesita saber quien recibe el aviso?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un aviso de tres líneas con qué ves, dónde y desde cuándo.",
    extend="Explica con un ejemplo por qué un plan de prevención debe actualizarse cuando cambia el uso de los sectores.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (regla y registro de ejemplo, inventados). Puntos de la amenaza del día (cada condición suma puntos): temperatura mayor que 30 grados, 2 puntos; de 25 a 30 grados, 1; menor que 25, 0. "
     "Humedad relativa del aire menor que 30 %, 2 puntos; de 30 % a 50 %, 1; mayor que 50 %, 0. Viento fuerte, 2; moderado, 1; débil, 0. Total de 0 a 2, nivel verde; de 3 a 4, amarillo; de 5 a 6, rojo. "
     "Horas de vigilancia por día de ejemplo: verde, 4; amarillo, 8; rojo, 12. "
     "Registro de cinco días: día 1, 32 grados, 25 %, viento moderado; día 2, 27 grados, 45 %, viento débil; día 3, 29 grados, 28 %, viento débil; día 4, 24 grados, 55 %, viento moderado; día 5, 26 grados, 32 %, viento fuerte.")
build(
    O6, 3, F,
    use="Aprenderé a analizar un caso: calcular el puntaje de amenaza de cada día con una regla, asignar un nivel de alerta y decidir las medidas y las horas de vigilancia.",
    prior=["Sé sumar números pequeños y comparar con rangos.", "Sé qué es el sistema de alerta.", "Sé qué es la humedad relativa y el viento."],
    explain=[
        "Un puntaje de amenaza resume varias condiciones del día en un solo número. La temperatura alta, la baja humedad relativa del aire (el porcentaje de vapor de agua que contiene respecto del máximo posible) y el viento fuerte favorecen que un incendio se inicie y se propague. Cada condición suma puntos según una regla del plan, y el total se compara con rangos que definen el nivel de alerta. La regla de esta clase es de ejemplo; la real la fija el plan y la entidad correspondiente.",
        "El nivel de alerta determina las medidas: más vigilancia, restricciones a los trabajos que generan chispas y aviso al personal. Un indicador no lo dice todo: una sola condición muy desfavorable puede bastar para sumar puntos relevantes, y por eso se miran las tres. Se aplica la regla sin inventar puntos y sin suavizar el nivel porque haya plazos que cumplir. Los resultados se registran con la fecha.",
        f"La clasificación del día y las medidas las decide el encargado de prevención. {EMER} {AVISO}",
    ],
    vocab=[("puntaje de amenaza", "número que resume las condiciones del día para clasificar la amenaza de incendio"), ("humedad relativa", "porcentaje de vapor de agua del aire respecto del máximo que podría contener"), ("nivel de alerta", "clasificación de la amenaza en verde, amarillo o rojo"), ("restricción", "limitación de una actividad en ciertos niveles de alerta")],
    worked=[
        ("Calcular un puntaje", "Con la regla de la ficha, un día de ejemplo tiene 31 grados, 40 % de humedad y viento débil. ¿Cuál es su puntaje?", ["31 grados suman 2, 40 % suma 1 y viento débil suma 0.", "2 + 1 + 0 = 3."], "3 puntos, nivel amarillo"),
        ("Pasar a horas", "Con las horas de la ficha, tres días verdes seguidos, ¿cuántas horas de vigilancia suman?", ["Cada día verde son 4 horas.", "3 × 4 = 12."], "12 horas"),
    ],
    mistakes=[("Suavizar el nivel de un día porque hay plazos que cumplir.", "El nivel lo define la regla, no la conveniencia.", "Aplica la regla tal como es y registra el resultado."),
              ("Mirar solo una condición, como la temperatura.", "El viento fuerte o la humedad baja también suman puntos.", "Suma las tres condiciones antes de clasificar.")],
    T=[
        ("abc", "En Forestal: ¿qué es la humedad relativa del aire?", "El porcentaje de vapor de agua del aire respecto del máximo posible", "La cantidad de lluvia caída durante el día", "La humedad que tiene el suelo del bosque", "La humedad relativa es una propiedad del aire, no de la lluvia ni del suelo."),
        ("abc", "En Forestal: ¿por qué el viento fuerte aumenta la amenaza de incendio?", "Porque aviva el fuego y lo propaga más rápido a otros lugares", "Porque aumenta la humedad del combustible", "Porque enfría siempre la vegetación seca", "El viento aporta oxígeno y empuja el fuego hacia nuevos combustibles."),
        ("abc", "En Forestal: ¿qué es un puntaje de amenaza?", "Un número que resume las condiciones del día para clasificar la amenaza", "El precio de las herramientas de prevención", "La cantidad de personas del equipo", "El puntaje resume condiciones; no es un costo ni un número de personal."),
        ("=", "{F} ¿Cuál es el puntaje de amenaza del día 1?", "2+2+1", "Se suman los puntos de temperatura, humedad y viento del día 1.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje de amenaza del día 3?", "1+2+0", "Se suman los puntos de temperatura, humedad y viento del día 3.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje de amenaza del día 5?", "1+1+2", "Se suman los puntos de temperatura, humedad y viento del día 5.", " puntos"),
        ("abc", "{F} ¿Qué nivel de alerta tiene el día 2?", "Verde, porque suma 2 puntos", "Amarillo, porque suma 3 puntos", "Rojo, porque suma 5 puntos", "El día 2 suma 1 + 1 + 0 = 2, que corresponde al rango verde."),
        ("=", "{F} ¿Cuántas horas de vigilancia suman los cinco días, según el nivel de cada uno?", "12+4+8+4+8", "Se suman las horas de vigilancia que corresponden al nivel de cada día.", " horas"),
        ("abc", "{F} ¿Qué corresponde el día 1?", "Aplicar las restricciones del nivel rojo y reforzar la vigilancia", "Seguir con los trabajos habituales con chispas", "Reducir la vigilancia porque es de día", "El día 1 suma 5 puntos, que es nivel rojo."),
        ("abc", "{F} De los dos días de nivel amarillo, ¿cuál tiene mayor amenaza?", "El día 5, con 4 puntos", "El día 3, porque tiene menos humedad", "Los dos igual, porque son amarillos", "El puntaje total manda: el día 5 suma 4 y el día 3 suma 3."),
        ("abc", "{F} Un compañero dice que el día 4 es peligroso porque tiene viento moderado. ¿Qué respuesta es correcta?", "No necesariamente: suma 1 punto en total y queda en nivel verde", "Sí, porque cualquier viento es peligroso", "Sí, porque el día 4 tiene más humedad", "El nivel se decide con el puntaje total de las tres condiciones."),
        ("abc", "{F} Un día de ejemplo tiene 26 grados, 55 % de humedad y viento fuerte. ¿Qué nivel tiene?", "Amarillo, porque suma 3 puntos", "Verde, porque la temperatura y la humedad son favorables", "Rojo, porque el viento fuerte basta", "Suma 1 + 0 + 2 = 3; una condición desfavorable puede mover el nivel."),
        ("=", "{F} ¿Cuántas horas más de vigilancia necesita un día rojo que uno verde?", "12-4", "Se restan las horas del día verde a las del día rojo.", " horas"),
    ],
    ctx=("abc", "Un jefe quiere seguir con trabajos que generan chispas en un día rojo porque tiene un plazo que cumplir. ¿Qué corresponde?", "Respetar las restricciones del nivel rojo y consultar a un adulto responsable si hay presión", "Seguir, pero con más vigilancia", "Seguir, si se termina antes de la tarde", "Las restricciones del nivel rojo no se levantan por plazos ni por horarios."),
    sc=[
        ("En Forestal: ¿qué condiciones suman puntos de amenaza en la ficha?", "La temperatura, la humedad relativa y el viento", "La regla suma las tres condiciones del día."),
        ("¿Qué nivel de alerta es el de 5 a 6 puntos?", "El nivel rojo", "Los rangos de la regla definen cada nivel."),
        ("¿Se puede suavizar el nivel por plazos?", "No, el nivel lo define la regla", "La conveniencia no cambia el nivel de alerta."),
    ],
    op=("Ficha de ejemplo: usa la regla y las horas de vigilancia de esta clase. Registro de cuatro días: día A, 33 grados, 20 %, viento fuerte; día B, 22 grados, 60 %, viento débil; día C, 28 grados, 35 %, viento moderado; día D, 31 grados, 45 %, viento débil. Escribe (a) el puntaje y el nivel de cada día, (b) las horas de vigilancia totales, (c) qué se restringe el día A, (d) por qué no se puede suavizar el nivel por razones de plazo.",
        "(a) A: 2 + 2 + 2 = 6, rojo; B: 0 + 0 + 0 = 0, verde; C: 1 + 1 + 1 = 3, amarillo; D: 2 + 1 + 0 = 3, amarillo. (b) 12 + 4 + 8 + 8 = 32 horas. (c) Los trabajos que generan chispas, y se refuerza la vigilancia. (d) Porque el nivel lo define la regla del plan y las restricciones protegen a las personas.",
        ["calcula los cuatro puntajes", "suma las horas", "nombra la restricción", "explica por qué no se suaviza"],
        ["hoja con las cuatro respuestas"],
        ["no sumar las tres condiciones", "confundir los rangos", "creer que el plazo cambia el nivel"],
        "Pregunta: «¿qué rango corresponde a 3 puntos?». Si no responde, pídele que relea la ficha."),
    reinforce="Inventa un día con temperatura, humedad y viento y calcula su puntaje y su nivel con la regla de la ficha.",
    extend="Explica con un ejemplo por qué una sola condición desfavorable puede cambiar el nivel de alerta.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (planificación de prevención de ejemplo, inventada; costos y valores son de ejemplo). Franja cortafuego (franja libre de vegetación combustible) del sector A: 3.000 m de largo por 10 m de ancho. Costo anual de mantención de la franja: $120.000 por hectárea. "
     "Sectores de riesgo alto y medio: 80 ha en total; una torre de vigilancia cubre 50 ha. Tiempo de respuesta (entre la alerta y la llegada de la brigada): 25 minutos; meta del plan: 20 minutos. "
     "Un incendio de ejemplo podría dañar 9 ha de plantación, con un valor de $1.200.000 por hectárea.")
build(
    O6, 4, F,
    use="Aprenderé a calcular en papel una franja cortafuego, el número de torres, el cumplimiento de un tiempo de respuesta y a comparar el costo de prevenir con el de una pérdida.",
    prior=["Sé calcular áreas de rectángulos y pasarlas a hectáreas.", "Sé calcular porcentajes simples.", "Sé dividir y redondear hacia arriba."],
    explain=[
        "Un cortafuego es una franja libre de vegetación combustible que dificulta que el fuego se propague. Su superficie se calcula como largo por ancho, y para pasar de metros cuadrados a hectáreas se divide por 10.000. La cobertura de una torre de vigilancia es la superficie que se puede observar desde ella. Si la división de hectáreas entre la cobertura no es exacta, se redondea hacia arriba, porque quedaría un sector sin cubrir.",
        "El tiempo de respuesta es el tiempo entre la alerta y la llegada de la brigada al lugar. Se compara con la meta del plan: si no se cumple, se revisan medidas, como ubicar la brigada más cerca o mejorar los caminos de acceso. También se compara el costo de prevenir con el de la pérdida posible, pero el dinero no es el único criterio: pesan la seguridad de las personas, el ambiente y la norma. Los datos de esta clase son de ejemplo.",
        f"La planificación la hace el encargado de prevención con el profesional responsable; la ejecución, personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("cortafuego", "franja libre de vegetación combustible que dificulta que el fuego se propague"), ("cobertura de una torre", "superficie que se puede observar desde una torre de vigilancia"), ("tiempo de respuesta", "tiempo entre la alerta y la llegada de la brigada al lugar"), ("meta", "valor que el plan se propone alcanzar"), ("redondear hacia arriba", "pasar al número entero siguiente cuando la división no es exacta")],
    worked=[
        ("Superficie de una franja", "Una franja de ejemplo mide 2.000 m de largo y 5 m de ancho. ¿Cuántas hectáreas ocupa?", ["2.000 × 5 = 10.000 m².", "10.000 m² es 1 ha."], "1 ha"),
        ("Redondear hacia arriba", "Un sector de ejemplo de 70 ha se vigila con torres que cubren 30 ha cada una. ¿Cuántas torres hacen falta?", ["70 ÷ 30 es 2 y sobran 10 ha.", "Para cubrir esas 10 ha hace falta otra torre: 3."], "3 torres"),
    ],
    mistakes=[("Redondear hacia abajo el número de torres.", "Quedarían hectáreas sin vigilar.", "Cuando la división no es exacta, se redondea hacia arriba."),
              ("Decidir no hacer una medida de prevención solo porque cuesta.", "El costo no es el único criterio: pesan las personas, el ambiente y la norma.", "Compara también esos criterios.")],
    T=[
        ("abc", "En Forestal: ¿qué es un cortafuego?", "Una franja libre de vegetación combustible que dificulta la propagación del fuego", "Una herramienta para apagar un incendio ya iniciado", "Un letrero de advertencia sobre la temporada", "Un cortafuego es una franja de terreno, no una herramienta ni un letrero."),
        ("abc", "En Forestal: ¿qué es la cobertura de una torre de vigilancia?", "La superficie que se puede observar desde ella", "La altura de la torre", "La cantidad de personas que trabajan en ella", "La cobertura mide la superficie observable."),
        ("abc", "En Forestal: ¿qué es el tiempo de respuesta ante un incendio?", "El tiempo entre la alerta y la llegada de la brigada al lugar", "El tiempo que tarda en apagarse el incendio", "El tiempo que toma elaborar el plan de prevención", "El tiempo de respuesta se mide desde la alerta hasta la llegada de la brigada."),
        ("=", "{F} ¿Cuántos metros cuadrados ocupa la franja cortafuego?", "3000*10", "Se multiplica el largo por el ancho de la franja.", " m²"),
        ("=", "{F} ¿Cuántas hectáreas ocupa la franja cortafuego?", "3000*10//10000", "Se calcula el área en m² y se divide entre 10.000.", " ha"),
        ("=", "{F} ¿Cuántos pesos cuesta la mantención anual de la franja?", "(3000*10//10000)*120000", "Se multiplican las hectáreas de la franja por el costo por hectárea.", " pesos"),
        ("=", "{F} ¿Cuántas torres hacen falta para cubrir los sectores de riesgo alto y medio, redondeando hacia arriba?", "(80+49)//50", "Se divide el total de hectáreas entre la cobertura de una torre y se redondea hacia arriba.", " torres"),
        ("abc", "{F} ¿Por qué se redondea hacia arriba el número de torres?", "Porque con una sola torre quedarían 30 ha sin cobertura", "Porque una torre cubre el doble de lo indicado", "Porque dos torres cuestan menos que una", "El resto de la división deja hectáreas sin vigilancia si no se agrega otra torre."),
        ("=", "{F} ¿Cuántos minutos supera el tiempo de respuesta a la meta del plan?", "25-20", "Se resta la meta al tiempo de respuesta real.", " minutos"),
        ("=", "{F} ¿Qué porcentaje de la meta representa ese exceso de tiempo?", "(25-20)*100//20", "Se divide el exceso entre la meta y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué conclusión corresponde sobre el tiempo de respuesta?", "No cumple la meta, por lo que se revisan medidas como ubicar la brigada más cerca", "Cumple la meta porque 25 es un número mayor", "La meta no es importante para el plan", "El tiempo real supera la meta de 20 minutos."),
        ("=", "{F} ¿Cuántos años de mantención de la franja equivalen al valor de la pérdida posible del incendio de ejemplo?", "9*1200000//((3000*10//10000)*120000)", "Se calcula la pérdida posible y se divide entre el costo anual de la franja.", " años"),
        ("abc", "{F} Con ese resultado, un compañero propone no hacer la franja porque «son muchos años». ¿Qué respuesta es correcta?", "No basta ese cálculo: faltan criterios como la seguridad de las personas, el ambiente y la norma", "Tiene razón, porque 30 años es mucho tiempo", "Tiene razón, si el predio es pequeño", "El cálculo solo compara dinero, y una pérdida puede incluir personas y ambiente."),
    ],
    ctx=("abc", "El jefe propone dejar de mantener la franja cortafuego este año para ahorrar y dice que «nunca pasa nada». ¿Qué respondes?", "Que la prevención no se puede recortar solo por costo, y que lo consultarás con el encargado y un adulto responsable", "Que sí, porque nunca pasa nada", "Que sí, si se reduce solo una parte", "La ausencia de incendios previos no elimina el riesgo, y la prevención se decide con más criterios que el costo."),
    sc=[
        ("En Forestal: ¿cómo se calcula la superficie de una franja?", "Largo por ancho", "El producto da los metros cuadrados."),
        ("¿Cuántos m² tiene una hectárea?", "10.000 m²", "Se divide entre 10.000 para pasar a hectáreas."),
        ("¿Qué es el tiempo de respuesta?", "El tiempo entre la alerta y la llegada de la brigada", "Se compara con la meta del plan."),
    ],
    op=("Ficha de ejemplo: franja cortafuego de 2.500 m de largo por 8 m de ancho; costo anual de mantención de $150.000 por hectárea. Sectores de riesgo alto y medio: 110 ha; una torre cubre 40 ha. Tiempo de respuesta: 30 minutos; meta: 24 minutos. Escribe (a) las hectáreas de la franja y su costo anual, (b) las torres necesarias redondeando hacia arriba, (c) cuántos minutos se supera la meta, (d) qué otros criterios además del costo considerarías antes de recortar la prevención.",
        "(a) 2.500 × 8 = 20.000 m², que son 2 ha; 2 × 150.000 = 300.000 pesos. (b) 110 ÷ 40 = 2 y sobran 30 ha; se necesitan 3 torres. (c) 30 − 24 = 6 minutos. (d) La seguridad de las personas, el ambiente y la norma vigente.",
        ["calcula la franja y su costo", "redondea las torres hacia arriba", "calcula el exceso de tiempo", "nombra criterios no económicos"],
        ["hoja con las cuatro respuestas"],
        ["no pasar de m² a hectáreas", "redondear hacia abajo", "decidir solo por costo"],
        "Pregunta: «¿qué pasa con las hectáreas que sobran en la división?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una franja con largo y ancho y calcula cuántas hectáreas ocupa.",
    extend="Explica con un ejemplo por qué comparar solo dinero no basta para decidir una medida de prevención.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (alternativas y verificación de ejemplo, inventadas). Meta del plan: tiempo de respuesta de 20 minutos o menos. Plan A, más vigilancia: costo anual $2.400.000; tiempo de respuesta de 18 minutos; protege 80 ha. "
     "Plan B, más franjas cortafuego: costo anual $3.200.000; tiempo de respuesta de 22 minutos; protege 80 ha. "
     "Simulacro de evacuación de ejemplo (ejercicio planificado y supervisado): 40 personas participaron y 36 llegaron al punto de reunión dentro del tiempo fijado; el plan exige al menos 95 de cada 100. "
     "Lista de verificación del plan: 10 ítems, 9 cumplen; el ítem crítico «mapa de evacuación actualizado» no cumple.")
build(
    O6, 5, F,
    use="Aprenderé a comparar dos planes de prevención con varios criterios y a verificar la calidad de un plan con un simulacro y una lista de verificación con ítems críticos.",
    prior=["Sé calcular costo por hectárea y porcentajes simples.", "Sé qué es un ítem crítico.", "Sé qué es el punto de reunión."],
    explain=[
        "Comparar planes de prevención exige varios criterios: el costo, el costo por hectárea protegida, el tiempo de respuesta frente a la meta y el efecto en las personas y el ambiente. El costo por hectárea protegida se calcula dividiendo el costo anual entre las hectáreas protegidas. Un plan más caro no es necesariamente mejor, y uno más barato no sirve si no cumple las metas. La decisión final la toma el profesional responsable con los datos.",
        "Para verificar un plan se hace un simulacro, un ejercicio planificado y supervisado de una emergencia, que muestra fallas antes de que ocurra una real. Sus resultados se comparan con la regla del plan, se registran tal como son y, si no se cumple, se ajusta el plan y se repite, anotando cada resultado. Además se usa una lista de verificación: si falla un ítem crítico, el plan no se da por aprobado, aunque la mayoría de los demás se cumpla.",
        f"Los simulacros los organiza personal responsable y entrenado; aquí aprendes a leer sus resultados. {EMER} {AVISO}",
    ],
    vocab=[("simulacro", "ejercicio planificado y supervisado para practicar una emergencia"), ("costo por hectárea protegida", "costo anual dividido entre las hectáreas protegidas"), ("meta del plan", "valor que el plan se propone alcanzar"), ("ítem crítico", "punto cuyo incumplimiento impide aprobar aunque los demás se cumplan"), ("verificación", "comprobación de que el plan funciona como se espera")],
    worked=[
        ("Costo por hectárea", "Un plan de ejemplo cuesta $900.000 al año y protege 60 ha. ¿Cuál es su costo por hectárea protegida?", ["Se divide el costo entre las hectáreas.", "900.000 ÷ 60 = 15.000."], "$15.000 por ha"),
        ("Cumplir una regla", "Un simulacro de ejemplo exige al menos 80 % y llegaron 18 de 20 personas. ¿Cumple?", ["18 ÷ 20 son 90 de cada 100.", "90 es mayor que 80."], "Sí, cumple"),
    ],
    mistakes=[("Repetir un simulacro sin avisar y anotar solo el mejor resultado.", "Anotar solo el mejor oculta fallas del plan.", "Se registran todos los resultados y se explican los ajustes."),
              ("Aprobar un plan porque casi todos los ítems cumplen.", "Un ítem crítico en falta impide aprobar.", "Se corrige el ítem crítico y se verifica de nuevo.")],
    T=[
        ("abc", "En Forestal: ¿qué es un simulacro de emergencia?", "Un ejercicio planificado y supervisado para practicar una emergencia", "Una emergencia real pequeña que se deja avanzar", "Una reunión para discutir los resultados financieros", "El simulacro es un ejercicio; no es una emergencia real ni una reunión de finanzas."),
        ("abc", "En Forestal: ¿para qué sirve verificar un plan con un simulacro?", "Para detectar fallas antes de una emergencia real", "Para reemplazar el plan escrito", "Para sancionar a quienes lleguen tarde", "El simulacro revela problemas del plan sin riesgo real."),
        ("abc", "En Forestal: ¿cómo se calcula el costo por hectárea protegida?", "Dividiendo el costo anual entre las hectáreas protegidas", "Multiplicando el costo anual por las hectáreas", "Restando las hectáreas al costo anual", "El costo por hectárea es una razón: costo dividido entre hectáreas."),
        ("=", "{F} ¿Cuál es el costo por hectárea protegida del plan A?", "2400000//80", "Se divide el costo anual entre las hectáreas protegidas.", " pesos por ha"),
        ("=", "{F} ¿Cuál es el costo por hectárea protegida del plan B?", "3200000//80", "Se divide el costo anual entre las hectáreas protegidas.", " pesos por ha"),
        ("=", "{F} ¿Cuántos minutos por debajo de la meta está el tiempo de respuesta del plan A?", "20-18", "Se resta el tiempo del plan A a la meta.", " minutos"),
        ("abc", "{F} ¿Qué plan cumple la meta de tiempo de respuesta?", "Solo el plan A, con 18 minutos", "Solo el plan B, con 22 minutos", "Los dos planes", "La meta es 20 minutos o menos; el plan B tarda 22."),
        ("abc", "{F} Considerando costo por hectárea y meta, ¿qué plan conviene?", "El plan A, porque cuesta menos por hectárea y cumple la meta", "El plan B, porque cuesta más y debe ser mejor", "Ninguno, porque no se pueden comparar", "El plan A es más barato por hectárea y cumple la meta; el B no la cumple."),
        ("=", "{F} ¿Qué porcentaje de las personas llegó al punto de reunión dentro del tiempo en el simulacro?", "36*100//40", "Se divide las personas que llegaron entre las que participaron y se multiplica por 100.", " %"),
        ("abc", "{F} Con ese resultado, ¿se cumple la regla del plan?", "No, porque 90 % es menor que 95 %, y se ajusta el plan y se repite el simulacro", "Sí, porque 90 % es un buen resultado", "Sí, porque el simulacro ya se hizo", "La regla exige al menos 95 %; con 90 % se ajusta y se repite."),
        ("abc", "{F} El ítem crítico «mapa de evacuación actualizado» no cumple. ¿Qué corresponde con el plan?", "No aprobarlo hasta corregir el ítem crítico", "Aprobarlo, porque 9 de 10 ítems cumplen", "Eliminar ese ítem de la lista", "Un ítem crítico en falta impide aprobar aunque los otros se cumplan."),
        ("=", "{F} ¿Cuántos pesos cuestan cinco años del plan A?", "5*2400000", "Se multiplica el costo anual por los años.", " pesos"),
        ("abc", "{F} Tras un simulacro con 36 de 40, el responsable propone repetirlo sin avisar hasta lograr 38 y anotar solo ese resultado. ¿Qué respuesta es correcta?", "No: se registra cada resultado y se repite con ajustes al plan", "Sí, porque lo que importa es el último resultado", "Sí, si los primeros intentos se borran", "Anotar solo el mejor oculta fallas que luego pueden aparecer en una emergencia."),
    ],
    ctx=("abc", "Un comité propone eliminar los simulacros del año porque «ya sabemos qué hacer». ¿Qué respondes?", "Que los simulacros verifican el plan y detectan fallas, y que lo consultarás con un adulto responsable", "Que sí, si el plan está escrito", "Que sí, si nadie ha tenido un incendio", "Un plan escrito no prueba que funcione; el simulacro muestra fallas antes de una emergencia."),
    sc=[
        ("En Forestal: ¿qué es un simulacro?", "Un ejercicio planificado y supervisado para practicar una emergencia", "Sirve para verificar el plan sin riesgo real."),
        ("¿Qué pasa si falla un ítem crítico?", "No se aprueba el plan hasta corregirlo", "Un ítem crítico impide aprobar aunque los demás cumplan."),
        ("¿Qué se hace con los resultados de un simulacro?", "Se registran todos y se ajusta el plan si hace falta", "Registrar todo permite mejorar el plan."),
    ],
    op=("Ficha de ejemplo (datos de ejemplo): plan C, costo anual $1.800.000, protege 60 ha, tiempo de respuesta 17 minutos; plan D, costo anual $2.400.000, protege 60 ha, tiempo de respuesta 21 minutos. Meta: 20 minutos o menos. Simulacro: 50 personas, 46 llegaron a tiempo; la regla exige al menos 90 de cada 100. Escribe (a) el costo por hectárea de C y de D, (b) qué plan cumple la meta y conviene, (c) el porcentaje del simulacro y si cumple, (d) qué haces si el resultado no cumple.",
        "(a) C: 1.800.000 ÷ 60 = 30.000; D: 2.400.000 ÷ 60 = 40.000. (b) Conviene C: cuesta menos por hectárea y cumple la meta; D no la cumple. (c) 46 ÷ 50 = 92 %, mayor que 90 %: cumple. (d) Si no cumpliera, se ajusta el plan, se repite el simulacro y se registran todos los resultados.",
        ["calcula los costos por hectárea", "elige con meta y costo", "calcula el porcentaje y concluye", "describe qué hacer ante un resultado que no cumple"],
        ["hoja con las cuatro respuestas"],
        ["comparar solo el costo", "no mirar la meta", "anotar solo el mejor resultado"],
        "Pregunta: «¿qué plan cumple la meta de tiempo?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos planes con costo, hectáreas protegidas y tiempo de respuesta, y calcula su costo por hectárea.",
    extend="Explica con un ejemplo por qué un simulacro puede mostrar fallas que el plan escrito no muestra.",
)
