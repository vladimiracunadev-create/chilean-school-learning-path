"""Ciencias Naturales EPJA Básica N2, módulo 1, desempeño OAD-03: investigar enfermedades de los sistemas digestivo, respiratorio y circulatorio, con medidas de prevención y autocuidado. Todo en papel; datos y textos de ejemplo; sin consejo clínico."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz y goma. Todo se resuelve con los textos y datos de ejemplo escritos en la ficha. Este cuaderno es ciencia general, no un consejo médico: ante síntomas o dudas de salud, se consulta a una persona profesional del centro de salud."
build = make_build(MATERIALS)

O3 = "EPJA-CNAT-NB2-OAD-03"
PRIOR = ["Conozco los niveles de organización y los sistemas digestivo y respiratorio.", "Sé formular una pregunta investigable y registrar datos con su unidad."]


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_):
    if len(op) == 5:  # (enunciado, ejemplo, criterios, evidencia, retroalimentación): los errores son los frecuentes de la clase
        op = (*op[:4], [m[0] for m in mistakes], op[4])
    build(O3, n, F, use=use, prior=PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ====================================================== OAD-03 clase 1
F = ("Ficha 1 (mensajes de ejemplo). Mensaje A, recibido en una cadena sin firma: «Este jugo cura todas las enfermedades del estómago y del corazón». "
     "Mensaje B, de un afiche de un centro de salud (ejemplo): «Lávate las manos con agua y jabón antes de comer y después de ir al baño». "
     "Mensaje C, dicho en la feria: «A mi vecino le dio gripe y a mí me contagió».")
K(1, F,
  "Hoy aprenderé a partir de la vida diaria: qué es una enfermedad, qué la puede causar y cómo reconocer información confiable para investigarla.",
  ["La salud es un estado de bienestar del cuerpo y de la mente. Una enfermedad es una alteración que impide que un órgano o un sistema funcione de manera normal. Muchas se conocen por la vida diaria: el resfrío, el dolor de estómago, la presión alta.",
   "Algunas enfermedades las causan agentes que se pasan de una persona a otra, como los virus y las bacterias: son enfermedades infecciosas o contagiosas. Otras no se contagian y se relacionan con hábitos y otros factores, como el tabaco o una alimentación desequilibrada.",
   "Para investigar una enfermedad hay que usar fuentes confiables: instituciones de salud, centros de atención y publicaciones con autoría y fecha. Un mensaje de cadena sin firma o una promesa de «cura milagrosa» no es evidencia. Este cuaderno da ciencia general; la salud de cada persona la evalúa un profesional."],
  [("enfermedad", "alteración que impide que un órgano o sistema funcione con normalidad"), ("contagioso", "que se pasa de una persona a otra"), ("prevención", "medidas que se toman para evitar una enfermedad"), ("fuente confiable", "origen de información con autoría, fecha y respaldo de una institución")],
  [("Clasificar una enfermedad", "El resfrío lo causa un virus que pasa de una persona a otra. ¿Es contagiosa o no contagiosa?",
    ["Se pasa de una persona a otra por un agente, el virus.", "Es una enfermedad contagiosa."], "Contagiosa"),
   ("Evaluar una fuente", "Un mensaje de cadena sin firma promete curar todo con un jugo. ¿Es una fuente confiable?",
    ["No tiene autoría, fecha ni respaldo.", "Promete curas milagrosas sin evidencia."], "No, no es una fuente confiable")],
  [("Creer que toda enfermedad se contagia.", "Se piensa que todas las enfermedades las causan virus o bacterias.", "Algunas no se contagian y se relacionan con hábitos o factores de riesgo."),
   ("Fiarse de un mensaje por haber sido reenviado muchas veces.", "Que muchos lo compartan no lo vuelve verdadero.", "Busca autoría, fecha e institución que lo respalde.")],
  [("abc", "¿Qué es una enfermedad?", "una alteración que impide el funcionamiento normal de un órgano o sistema", "un hábito de vida", "una persona", "Las enfermedades alteran el funcionamiento normal del cuerpo."),
   ("abc", "¿Qué tipo de agentes causa muchas enfermedades contagiosas?", "virus y bacterias", "el frío y la humedad", "el cansancio y el sueño", "Los virus y las bacterias son agentes que pasan de una persona a otra."),
   ("abc", "{F} ¿Cuál de los mensajes viene de una fuente identificable, un centro de salud?", "el mensaje B", "el mensaje A", "el mensaje C", "El mensaje B indica su origen, un afiche de un centro de salud."),
   ("abc", "{F} ¿Por qué el mensaje A no es una fuente confiable?", "No tiene autoría y promete una cura para todo", "Porque habla del estómago", "Porque es corto", "Prometer curar todas las enfermedades sin respaldo no es información confiable."),
   ("abc", "{F} El mensaje B recomienda lavarse las manos con agua y jabón. ¿Qué tipo de medida es?", "prevención", "tratamiento de una enfermedad ya grave", "un diagnóstico", "Se hace antes de enfermar, para evitar contagios."),
   ("abc", "{F} En el mensaje C, ¿qué dice que hizo la gripe del vecino?", "contagió a la persona que habla", "la curó", "la volvió fuerte", "El mensaje dice que a quien habla le dio gripe porque su vecino la tenía."),
   ("abc", "¿Cuál de estas es una enfermedad que no se contagia?", "una enfermedad relacionada con fumar por mucho tiempo", "el resfrío común", "la gripe", "Los daños por el tabaco se deben a un hábito, no a un agente que pase de una persona a otra."),
   ("abc", "Se quiere investigar la gastroenteritis. ¿Qué fuente conviene usar?", "un folleto de un centro de salud con fecha y autoría", "un mensaje de cadena sin firma", "un comentario sin nombre en una red social", "Una institución de salud con fecha y autoría respalda lo que dice."),
   ("abc", "Alguien dice «si algo se comparte mucho, es verdad». ¿Qué corresponde responder?", "Compartir mucho no demuestra que sea cierto", "Tiene razón", "Lo que se comparte siempre es oficial", "La veracidad se comprueba con la fuente y la evidencia, no con la cantidad de reenvíos."),
   ("abc", "Alguien piensa que todas las enfermedades se contagian. ¿Cuál es el error?", "Algunas se relacionan con hábitos y no pasan de una persona a otra", "Ninguna se contagia", "Solo las del corazón se contagian", "Hay enfermedades no contagiosas, como las ligadas a ciertos hábitos de vida."),
   ("abc", "Si una persona tiene síntomas, ¿qué conviene hacer?", "consultar a una persona profesional de un centro de salud", "tomar lo que dice una cadena", "esperar a que otra persona opine", "El diagnóstico y el tratamiento los define un profesional de salud."),
   ("abc", "Se compara «lavar las manos» con «tomar un jugo milagroso». ¿Cuál tiene respaldo en información de salud confiable?", "lavar las manos con agua y jabón", "el jugo milagroso", "ninguna de las dos", "El lavado de manos es una medida de prevención recomendada por instituciones de salud."),
   ("abc", "¿Qué dato no ayuda a evaluar si una fuente de salud es confiable?", "la cantidad de reenvíos", "la autoría", "la fecha", "Los reenvíos no muestran respaldo; la autoría y la fecha sí aportan.")],
  ("abc", "En una junta de vecinos se comparten dos textos sobre cómo evitar enfermedades del estómago. El primero es un folleto de un centro de salud con fecha; el segundo, una cadena sin firma. ¿Cuál conviene usar para la investigación?", "el folleto del centro de salud", "la cadena sin firma", "los dos por igual", "El folleto tiene autoría y respaldo de una institución de salud."),
  [("En Ciencias: ¿qué es la prevención de una enfermedad?", "Medidas que se toman antes para evitarla", "Por ejemplo, lavarse las manos para evitar contagios."),
   ("En información de salud: ¿qué es una fuente confiable?", "Un origen de información con autoría, fecha y respaldo", "Eso permite comprobar lo que dice."),
   ("¿Todas las enfermedades son contagiosas?", "No", "Algunas se relacionan con hábitos y factores de riesgo.")],
  ("Con los tres mensajes de la ficha 1, escribe para cada uno si es o no es una fuente confiable y por qué, y señala cuál contiene una medida de prevención.",
   "A: no confiable, sin autoría ni evidencia. B: confiable, de un centro de salud, y contiene una medida de prevención (lavarse las manos). C: es un comentario de feria; no sirve como fuente para investigar.",
   ["evalúa los tres mensajes", "usa autoría y respaldo como criterio", "identifica la medida de prevención"],
   ["Distingue una fuente institucional de una cadena.", "Justifica con un criterio.", "Reconoce la prevención del mensaje B."],
   "Si dice que A es confiable por ser popular, pregunta quién lo firma. Si no identifica la prevención, pregunta qué se hace antes de enfermar."),
  "Escribe dos enfermedades contagiosas y dos que no se contagian que ya conozcas.",
  "Escribe tres criterios que usarías para decidir si un folleto de salud es confiable.")

# ====================================================== OAD-03 clase 2
F = ("Ficha 2 (esquema del sistema circulatorio, de ejemplo). Corazón: músculo con cuatro cavidades (dos aurículas y dos ventrículos) que bombea la sangre. "
     "Arterias: vasos que sacan la sangre del corazón. Venas: vasos que devuelven la sangre al corazón. Capilares: vasos muy finos donde la sangre intercambia sustancias con las células. "
     "Sangre: líquido que lleva oxígeno, nutrientes y desechos.")
K(2, F,
  "Hoy reconoceré las estructuras del sistema circulatorio y su función, para entender después qué enfermedades lo afectan.",
  ["El sistema circulatorio reparte la sangre por todo el cuerpo. Está formado por el corazón, los vasos sanguíneos y la sangre. El corazón es un músculo que bombea sin descanso: tiene cuatro cavidades, dos aurículas arriba y dos ventrículos abajo.",
   "Los vasos sanguíneos son tubos por donde corre la sangre. Las arterias sacan la sangre del corazón. Las venas la devuelven. Los capilares son vasos muy finos que llegan a todos los rincones y allí la sangre entrega oxígeno y nutrientes y recoge desechos.",
   "El sistema circulatorio trabaja con otros dos que ya conoces: el respiratorio le entrega oxígeno y el digestivo le entrega nutrientes. El pulso es el golpe que se siente en una arteria cuando el corazón empuja la sangre."],
  [("corazón", "órgano muscular que bombea la sangre"), ("arteria", "vaso que saca la sangre del corazón"), ("vena", "vaso que devuelve la sangre al corazón"), ("capilar", "vaso muy fino donde la sangre intercambia sustancias con las células")],
  [("Identificar un vaso", "¿Cómo se llama el vaso que devuelve la sangre al corazón?",
    ["Las arterias sacan la sangre; el otro tipo la devuelve.", "Esos vasos son las venas."], "Las venas"),
   ("Entender una función", "¿Para qué sirven los capilares?",
    ["Son los vasos más finos y llegan hasta las células.", "Ahí se intercambian oxígeno, nutrientes y desechos."], "Para el intercambio de sustancias con las células")],
  [("Decir que las arterias son las que llevan la sangre al corazón.", "Se confunden los sentidos: las arterias la sacan del corazón.", "Recuerda: arterias salen, venas vuelven."),
   ("Pensar que el corazón es solo un tubo.", "Se olvida que es un músculo con cavidades que bombea.", "El corazón es un músculo con cuatro cavidades.")],
  [("abc", "{F} ¿Cuántas cavidades tiene el corazón?", "cuatro", "dos", "seis", "El corazón tiene dos aurículas y dos ventrículos."),
   ("abc", "{F} ¿Qué vasos sacan la sangre del corazón?", "las arterias", "las venas", "los capilares", "Las arterias salen del corazón y reparten la sangre."),
   ("ab", "{F} ¿Qué vasos devuelven la sangre al corazón?", "las venas", "las arterias", "Las venas llevan la sangre de vuelta hacia el corazón."),
   ("abc", "{F} ¿En qué vasos ocurre el intercambio de sustancias con las células?", "los capilares", "las arterias grandes", "las venas grandes", "Los capilares son tan finos que dejan pasar las sustancias."),
   ("abc", "¿Qué lleva la sangre a las células?", "oxígeno y nutrientes", "solo aire", "solo agua", "La sangre reparte lo que el cuerpo necesita y recoge desechos."),
   ("abc", "¿Qué órgano bombea la sangre?", "el corazón", "el estómago", "el pulmón", "El corazón es el músculo que impulsa la sangre por el cuerpo."),
   ("abc", "El corazón tiene dos aurículas y dos ventrículos. ¿Cuántas cavidades suma eso?", "4", "2", "6", "Dos aurículas más dos ventrículos son cuatro cavidades."),
   ("abc", "¿Qué sistema le entrega oxígeno al circulatorio?", "el respiratorio", "el digestivo", "el esquelético", "En los alvéolos el oxígeno pasa a la sangre."),
   ("abc", "¿Qué sistema le entrega nutrientes al circulatorio?", "el digestivo", "el respiratorio", "el reproductor", "En el intestino delgado los nutrientes pasan a la sangre."),
   ("abc", "Alguien dice «las arterias llevan la sangre al corazón». ¿Cuál es el error?", "Las arterias sacan la sangre del corazón", "Las arterias no existen", "Son las venas las que lo bombean", "El sentido de las arterias es desde el corazón hacia el cuerpo."),
   ("abc", "Alguien dice que el corazón es un tubo. ¿Qué corresponde responder?", "Es un músculo con cuatro cavidades que bombea", "Tiene razón", "Es una célula", "El corazón es un órgano muscular que se contrae y bombea la sangre."),
   ("abc", "¿Qué recorrido sigue la sangre desde el corazón hasta una célula y de vuelta?", "arterias, capilares, venas", "venas, capilares, arterias", "capilares, arterias, venas", "Sale por arterias, intercambia en capilares y regresa por venas."),
   ("abc", "Una persona nota su pulso en la muñeca. ¿Qué siente?", "el empuje de la sangre en una arteria", "el aire en la tráquea", "el alimento en el esófago", "El pulso es el golpe de la sangre impulsada por el corazón al pasar por una arteria.")],
  ("abc", "En una charla del consultorio, una persona escucha «el corazón es la bomba del sistema circulatorio». ¿Qué significa eso?", "que el corazón impulsa la sangre por todo el cuerpo", "que el corazón guarda aire", "que el corazón digiere alimentos", "Como una bomba, el corazón mueve la sangre a través de los vasos."),
  [("En Ciencias: ¿qué es una arteria?", "Un vaso que saca la sangre del corazón", "Reparte la sangre por el cuerpo."),
   ("¿Qué hace una vena?", "Devuelve la sangre al corazón", "Su sentido es hacia el corazón."),
   ("¿Qué son los capilares?", "Vasos muy finos donde ocurre el intercambio", "Allí la sangre entrega oxígeno y nutrientes.")],
  ("Dibuja un esquema del sistema circulatorio: un corazón con sus cuatro cavidades y tres tipos de vasos con flechas que muestren por dónde sale y por dónde vuelve la sangre. Rotula arterias, venas y capilares.",
   "Corazón con cuatro cavidades. Flecha de salida por arterias, flecha de intercambio en capilares y flecha de regreso por venas.",
   ["rotula el corazón y los tres tipos de vasos", "las flechas muestran el sentido correcto", "indica qué lleva la sangre"],
   ["Arterias salen, venas vuelven.", "Los capilares están entre ambas.", "Menciona oxígeno y nutrientes."],
   "Si invierte arterias y venas, pregunta hacia dónde va cada una. Si olvida los capilares, pregunta dónde se entregan las sustancias a las células."),
  "Escribe con tus palabras qué hace cada parte del sistema circulatorio.",
  "Explica por qué sin el sistema circulatorio el oxígeno y los nutrientes no llegarían a las células.")

# ====================================================== OAD-03 clase 3
F = ("Ficha 3 (cuadro de ejemplo). Enfermedad: gastroenteritis. Qué es: infección del estómago y el intestino, causada por virus o bacterias, con vómitos y diarrea. "
     "Problema posible: deshidratación, que es perder mucha agua del cuerpo. Cómo se pasa: alimentos o agua contaminados, o manos sucias. "
     "Prevención: lavar las manos con agua y jabón, usar agua segura, cocer bien los alimentos, mantener la comida fría refrigerada y separar crudo de cocido.")
K(3, F,
  "Hoy investigaré enfermedades del sistema digestivo, cómo se producen y qué medidas generales de prevención y autocuidado existen.",
  ["Algunas enfermedades del sistema digestivo se deben a alimentos o agua contaminados. La gastroenteritis es una infección del estómago y el intestino, causada por virus o bacterias, que produce vómitos y diarrea. La intoxicación por alimentos ocurre cuando se come algo contaminado.",
   "Un riesgo de la diarrea y los vómitos es la deshidratación: el cuerpo pierde mucha agua. Por eso, ante síntomas intensos o que duran, se consulta a un profesional del centro de salud. Este cuaderno solo entrega ciencia general, no indica tratamientos.",
   "La prevención se apoya en hábitos de higiene: lavarse las manos con agua y jabón, usar agua segura, cocer bien los alimentos, guardar la comida fría en refrigerador y no mezclar alimentos crudos con cocidos. La gastritis, en cambio, es una inflamación del estómago que puede tener varias causas."],
  [("gastroenteritis", "infección del estómago y el intestino con vómitos y diarrea"), ("deshidratación", "pérdida de mucha agua del cuerpo"), ("contaminado", "que tiene gérmenes u otras sustancias dañinas"), ("higiene", "hábitos de limpieza que cuidan la salud")],
  [("Relacionar causa y prevención", "Un alimento cocido se dejó muchas horas fuera del refrigerador. ¿Qué medida de prevención no se respetó?",
    ["La ficha dice que la comida fría debe refrigerarse.", "Guardar en frío evita que crezcan gérmenes."], "Refrigerar la comida que lo necesita"),
   ("Distinguir causa de síntoma", "En la gastroenteritis, ¿la diarrea es causa o síntoma?",
    ["La causa es la infección por virus o bacterias.", "La diarrea es lo que se nota: el síntoma."], "Es un síntoma")],
  [("Pensar que la gastroenteritis se evita solo tomando algo después de comer.", "No se ve que la prevención se hace antes, con higiene y cuidado de los alimentos.", "La prevención incluye lavar manos, agua segura y buen almacenamiento."),
   ("Mezclar un cuchillo usado con carne cruda y luego con verduras sin lavarlo.", "Se pasan gérmenes de un alimento a otro.", "Separa lo crudo de lo cocido y lava los utensilios.")],
  [("abc", "{F} ¿Cuál es la causa de la gastroenteritis según la ficha?", "virus o bacterias", "el frío", "comer mucho pan", "La ficha dice que es una infección causada por virus o bacterias."),
   ("abc", "{F} ¿Qué es la deshidratación?", "perder mucha agua del cuerpo", "ganar peso", "tener hambre", "La ficha la define como pérdida de mucha agua del cuerpo."),
   ("abc", "{F} ¿Cuál de estas es una medida de prevención de la ficha?", "lavar las manos con agua y jabón", "dejar la comida fuera del refrigerador", "mezclar crudo con cocido", "Lavar las manos reduce el paso de gérmenes a la boca."),
   ("abc", "{F} ¿Cómo se puede pasar la gastroenteritis?", "por alimentos o agua contaminados o por manos sucias", "por el frío o por el viento", "por la picadura de un insecto", "La ficha indica estas vías de contagio."),
   ("abc", "¿Qué síntomas típicos tiene la gastroenteritis?", "vómitos y diarrea", "tos y mocos", "dolor de huesos", "Son los síntomas de la ficha para esta infección."),
   ("abc", "¿Por qué es importante guardar la comida fría en refrigerador?", "Porque el frío frena el crecimiento de gérmenes", "Porque le da más sabor", "Porque la hace dura", "En frío los gérmenes crecen más lento, y eso reduce riesgos."),
   ("=", "{F} Una familia de ejemplo compra 12 huevos y usa 5 en una preparación bien cocida. ¿Cuántos huevos quedan para guardar en refrigerador?", "12-5", "Se restan los huevos usados de los que había.", " huevos"),
   ("abc", "Alguien guarda carne cruda y verduras lavadas juntas, en contacto. ¿Qué medida de prevención falla?", "separar crudo de cocido o de alimentos que se comen sin cocción", "usar agua segura", "lavarse las manos", "Los jugos de la carne cruda pueden pasar gérmenes a otros alimentos."),
   ("abc", "Una persona dice «si lavo mis manos solo cuando se ven sucias, está bien». ¿Qué corresponde responder?", "Los gérmenes no se ven, y conviene lavarse antes de comer y después de ir al baño", "Tiene razón", "Lavarse no sirve", "La ficha recomienda lavar con agua y jabón en momentos clave, aunque las manos parezcan limpias."),
   ("abc", "Alguien afirma «con vómitos y diarrea nunca hay que preocuparse por la deshidratación». ¿Cuál es el error?", "Perder mucha agua es un riesgo, y si los síntomas son intensos o duran se consulta a un profesional", "La deshidratación solo afecta a los pulmones", "No hay error", "La ficha advierte que la pérdida de mucha agua es un riesgo posible de esta infección."),
   ("abc", "Un grupo comunitario quiere reducir casos de gastroenteritis en un comedor de ejemplo. ¿Qué medida es más relevante?", "agua segura, higiene de manos y alimentos bien guardados", "cambiar el color de las paredes", "poner música", "Son las medidas que reducen el paso de gérmenes."),
   ("abc", "¿Cuál de estas es una enfermedad del sistema digestivo?", "la gastroenteritis", "el asma", "la hipertensión", "La gastroenteritis afecta el estómago y el intestino."),
   ("abc", "Se anota «hay diarrea desde ayer, así que usaré lo que me dijo un amigo». ¿Qué conviene en lugar de eso?", "consultar a un profesional de salud si los síntomas son intensos o duran", "seguir la recomendación del amigo", "no consultar", "Un amigo no puede evaluar la situación; el profesional sí.")],
  ("abc", "En un puesto de comida de una feria (ejemplo), una persona observa que la cocinera lava sus manos con agua y jabón, guarda la comida fría en un frigorífico y separa los alimentos crudos de los cocidos. ¿Qué cumple?", "medidas de prevención de enfermedades digestivas", "medidas contra el asma", "medidas contra la hipertensión", "Cada acción reduce el paso de gérmenes a los alimentos."),
  [("En Ciencias: ¿qué es la gastroenteritis?", "Una infección del estómago y el intestino con vómitos y diarrea", "Las causan virus o bacterias que pasan de una persona a otra."),
   ("¿Qué es la deshidratación?", "Perder mucha agua del cuerpo", "Puede ocurrir con vómitos y diarrea intensos."),
   ("¿Cuál es una medida de prevención?", "Lavarse las manos con agua y jabón", "Reduce el paso de gérmenes a la boca y a los alimentos.")],
  ("Con la ficha 3, arma un cuadro de tres filas con: enfermedad, causa y dos medidas de prevención. Luego explica con tus palabras por qué la prevención es mejor que esperar a enfermar.",
   "Gastroenteritis: causa virus o bacterias. Prevención: lavar manos y guardar la comida fría. Prevenir evita pasar por la enfermedad y sus riesgos.",
   ["completa el cuadro", "usa información de la ficha", "explica la prevención con sus palabras"],
   ["Nombra la causa de la ficha.", "Incluye dos medidas de prevención.", "La explicación es clara."],
   "Si propone un tratamiento, recuerda que eso lo define un profesional. Si repite solo una medida, pide otra de la ficha."),
  "Escribe tres hábitos de higiene que ayudan a prevenir enfermedades del sistema digestivo.",
  "Investiga con tus palabras la diferencia entre una infección y una intoxicación por alimentos.")

# ====================================================== OAD-03 clase 4
F = ("Ficha 4 (cuadro de ejemplo). Resfrío común: causado por virus, se pasa por gotitas al toser o por contacto. Influenza: causada por virus, se pasa igual. Neumonía: infección de los pulmones, puede ser causada por virus o bacterias. "
     "Asma: enfermedad en que las vías de los pulmones se inflaman y se estrechan; no se contagia. Prevención general: lavarse las manos, ventilar los espacios, cubrirse al toser, vacunarse según el calendario de salud y evitar el humo de tabaco.")
K(4, F,
  "Hoy investigaré enfermedades del sistema respiratorio: cuáles se contagian, cuáles no y qué medidas generales de prevención y autocuidado existen.",
  ["Muchas enfermedades respiratorias las causan virus o bacterias que pasan de persona a persona por gotitas al toser y estornudar. Ejemplos son el resfrío común, la influenza y la neumonía, que es una infección de los pulmones.",
   "El asma es distinta: las vías de los pulmones se inflaman y se estrechan, y no se contagia. El humo de tabaco irrita las vías respiratorias y daña los pulmones. Un diagnóstico y un tratamiento los define siempre un profesional de salud.",
   "Hay medidas de prevención general: lavarse las manos, ventilar los espacios cerrados, cubrirse la boca al toser, vacunarse según indica el calendario de salud y evitar el humo de tabaco. Los síntomas intensos o que duran se consultan en un centro de salud."],
  [("neumonía", "infección de los pulmones"), ("asma", "enfermedad en que las vías de los pulmones se inflaman y estrechan"), ("gotitas", "pequeñas gotas que salen al toser, estornudar o hablar"), ("ventilar", "renovar el aire de un espacio abriendo ventanas o puertas")],
  [("Distinguir contagiosa de no contagiosa", "El asma, ¿se contagia?", ["La ficha dice que las vías se inflaman y estrechan.", "No es causada por un agente que pase de una persona a otra."], "No se contagia"),
   ("Relacionar medida y enfermedad", "¿Qué medida ayuda a reducir el paso de virus respiratorios en una sala cerrada?", ["Los virus se pasan por gotitas en el aire.", "Renovar el aire reduce la concentración de gotitas."], "Ventilar el espacio")],
  [("Creer que el asma se contagia al estar cerca.", "Se confunde una enfermedad crónica de las vías respiratorias con una infección.", "El asma no se contagia."),
   ("Toser en la mano y luego saludar sin lavarla.", "Los gérmenes quedan en la mano y se pasan al tocar.", "Cúbrete con el pliegue del codo o lávate las manos después.")],
  [("abc", "{F} ¿Cuál de estas enfermedades es una infección de los pulmones?", "la neumonía", "el asma", "la gastroenteritis", "La ficha define la neumonía como infección de los pulmones."),
   ("abc", "{F} ¿Cuál de estas enfermedades no se contagia?", "el asma", "el resfrío común", "la influenza", "El asma no es causada por un agente que pase de persona a persona."),
   ("abc", "{F} ¿Cómo se pasan el resfrío y la influenza?", "por gotitas al toser o por contacto", "por la comida cocida", "por los alimentos fríos", "La ficha indica que se transmiten por gotitas y contacto."),
   ("abc", "¿Qué medida ayuda a reducir el paso de virus respiratorios?", "cubrirse al toser y lavarse las manos", "compartir los vasos", "cerrar todas las ventanas", "Cubrir la tos y lavarse las manos reduce el paso de gotitas y gérmenes."),
   ("abc", "¿Qué efecto tiene el humo de tabaco sobre las vías respiratorias?", "las irrita y daña los pulmones", "las protege", "las limpia", "El humo de tabaco contiene sustancias que irritan y dañan."),
   ("abc", "{F} ¿Cuál de estas medidas figura en la ficha como prevención general?", "vacunarse según el calendario de salud", "tomar remedios sin consulta", "no ventilar", "La ficha menciona la vacunación según el calendario de salud."),
   ("=", "Un centro de salud de ejemplo atendió 18 consultas por enfermedades respiratorias el lunes y 25 el martes. ¿Cuántas consultas fueron en total entre ambos días?", "18+25", "Se suman las consultas de los dos días.", " consultas"),
   ("abc", "Una sala con muchas personas tiene todas las ventanas cerradas. ¿Qué medida de prevención respiratoria conviene?", "ventilar abriendo ventanas", "cerrar la puerta para que no salga el aire", "calentar más la sala", "Renovar el aire reduce la acumulación de gotitas."),
   ("abc", "Alguien dice «el asma se pasa al compartir el vaso». ¿Qué corresponde responder?", "El asma no se contagia", "Tiene razón", "Solo se contagia a los niños", "El asma es una enfermedad de las vías respiratorias que no se transmite."),
   ("abc", "Una persona con tos cubre su boca con el pliegue del codo. ¿Qué medida aplica?", "evitar que las gotitas lleguen a otras personas", "curarse sola", "evitar el asma", "El codo frena las gotitas y es una medida de prevención."),
   ("abc", "Se dice «como la neumonía es infección, siempre se cura con lo mismo». ¿Qué falla?", "La causa puede ser un virus o una bacteria y el tratamiento lo define un profesional", "Nada, es verdad", "La neumonía no es infección", "La ficha dice que puede tener causas distintas, y eso importa para el tratamiento."),
   ("abc", "En un cuadro de ejemplo se anota «tos, estornudos, mocos» para el resfrío. ¿Cuál de estas es una frase prudente?", "Los síntomas intensos o que duran se consultan en un centro de salud", "No hace falta consultar nunca", "Hay que decidir solo", "Una frase prudente deriva a un profesional cuando los síntomas son intensos."),
   ("abc", "¿Cuál es el sistema afectado por el asma?", "el respiratorio", "el digestivo", "el circulatorio", "Las vías respiratorias se inflaman y se estrechan, y eso dificulta respirar.")],
  ("abc", "En un lugar de trabajo de ejemplo, un afiche dice «Si tienes tos, cúbrete con el codo, lávate las manos y ventila la sala». ¿Qué tipo de medidas son?", "prevención de enfermedades respiratorias contagiosas", "tratamientos del asma", "tratamientos de la gastroenteritis", "Son medidas generales para reducir el paso de gérmenes respiratorios."),
  [("En Ciencias: ¿qué es la neumonía?", "Una infección de los pulmones", "Puede ser causada por virus o bacterias."),
   ("¿Qué es el asma?", "Una enfermedad en que las vías respiratorias se inflaman y estrechan", "No se contagia porque no la causa un agente que pase entre personas."),
   ("¿Para qué se ventila un espacio?", "Para renovar el aire y reducir las gotitas", "Así se reduce el paso de virus.")],
  ("Usando la ficha 4, arma un cuadro con cuatro enfermedades respiratorias, si se contagian o no, y dos medidas de prevención general. Escribe una frase que invite a consultar a un profesional de salud ante síntomas intensos.",
   "Resfrío: se contagia. Influenza: se contagia. Neumonía: se contagia si es infecciosa. Asma: no se contagia. Prevención: cubrirse al toser y ventilar. Ante síntomas intensos, consultar en un centro de salud.",
   ["incluye cuatro enfermedades", "indica si se contagian", "incluye una frase prudente"],
   ["Usa los datos de la ficha.", "Distingue contagiosas y no contagiosas.", "No da indicaciones de tratamiento."],
   "Si indica remedios, recuerda que el tratamiento lo define un profesional. Si dice que el asma se contagia, vuelve a la ficha."),
  "Escribe tres medidas de prevención respiratoria para una sala con mucha gente.",
  "Explica por qué el humo de tabaco no es una enfermedad contagiosa pero sí un riesgo para el sistema respiratorio.")

# ====================================================== OAD-03 clase 5
F = ("Ficha 5 (cuadro de ejemplo). Hipertensión arterial: la presión de la sangre sobre las paredes de las arterias se mantiene alta. Aterosclerosis: se acumulan depósitos en las paredes de las arterias y las estrechan. "
     "Infarto: una arteria que lleva sangre al corazón se tapa y parte del músculo cardíaco deja de recibir sangre. Factores de riesgo: fumar, sedentarismo, alimentación con mucha sal y grasas, antecedentes familiares. "
     "Prevención general: actividad física, alimentación variada, no fumar y controles de salud. Estas enfermedades no se contagian.")
K(5, F,
  "Hoy aplicaré lo aprendido a enfermedades del sistema circulatorio: qué son, qué factores de riesgo tienen y cómo se leen datos de ejemplo sobre ellas.",
  ["Las enfermedades del sistema circulatorio afectan al corazón y a los vasos sanguíneos. La hipertensión arterial ocurre cuando la presión de la sangre sobre las arterias se mantiene alta. La aterosclerosis estrecha las arterias por depósitos en sus paredes. En un infarto, una arteria del corazón se obstruye.",
   "Estas enfermedades no se contagian. Se relacionan con factores de riesgo, que son condiciones que aumentan la probabilidad de enfermar: fumar, el sedentarismo, una alimentación con mucha sal y grasas, y los antecedentes familiares. Tener un factor de riesgo no significa que la persona enfermará, ni que se pueda saber sin un control.",
   "La prevención es general: actividad física, alimentación variada, no fumar y controles de salud periódicos. Leer una tabla de datos ayuda a comparar. Aquí usaremos datos de ejemplo escritos en la ficha, sin hacer diagnósticos."],
  [("hipertensión arterial", "presión de la sangre alta de manera sostenida"), ("aterosclerosis", "estrechamiento de las arterias por depósitos en sus paredes"), ("factor de riesgo", "condición que aumenta la probabilidad de enfermar"), ("sedentarismo", "poca actividad física en la vida diaria")],
  [("Identificar un factor de riesgo", "¿Es el sedentarismo un factor de riesgo del sistema circulatorio?", ["La ficha lo lista entre los factores de riesgo.", "La poca actividad física aumenta la probabilidad de enfermar."], "Sí, es un factor de riesgo"),
   ("Interpretar un dato de ejemplo", "En una tabla de ejemplo, de 50 personas, 20 hacen actividad física regular. ¿Cuántas no la hacen?", ["Se parte del total de 50.", "Se restan las 20 que sí la hacen."], "30 personas")],
  [("Pensar que quien tiene un factor de riesgo enfermará seguro.", "Se confunde riesgo con certeza.", "Un factor de riesgo aumenta la probabilidad, no la asegura."),
   ("Creer que las enfermedades del corazón se contagian.", "Se confunden con las infecciosas.", "No las causa un agente que pase de una persona a otra.")],
  [("abc", "{F} ¿Qué es la hipertensión arterial?", "presión de la sangre sobre las arterias que se mantiene alta", "falta de aire", "dolor de estómago", "La ficha la define así, y afecta a las arterias."),
   ("abc", "{F} ¿Qué ocurre en la aterosclerosis?", "se acumulan depósitos que estrechan las arterias", "se infectan los pulmones", "se rompe un hueso", "Los depósitos estrechan el espacio por donde pasa la sangre."),
   ("abc", "{F} ¿Cuál de estos es un factor de riesgo de la ficha?", "fumar", "tomar agua", "dormir", "La ficha nombra fumar entre los factores de riesgo."),
   ("abc", "{F} ¿Cuál de estas es una medida de prevención de la ficha?", "hacer actividad física", "fumar más", "comer con mucha sal", "La actividad física ayuda a cuidar el corazón y los vasos."),
   ("abc", "{F} ¿Estas enfermedades se contagian?", "no", "sí, por gotitas", "sí, por el agua", "La ficha indica que no se contagian."),
   ("abc", "¿Qué es un factor de riesgo?", "una condición que aumenta la probabilidad de enfermar", "una enfermedad segura", "un tratamiento", "El riesgo es una probabilidad, no una certeza."),
   ("=", "Una encuesta de ejemplo en un barrio registra 80 personas; 30 caminan a diario. ¿Cuántas no caminan a diario?", "80-30", "Se restan las personas que caminan del total.", " personas"),
   ("=", "En esa misma encuesta de ejemplo, 12 de las 80 personas fuman. ¿Cuántas no fuman?", "80-12", "Se restan las que fuman del total.", " personas"),
   ("abc", "Una persona tiene antecedentes familiares de hipertensión. ¿Qué es correcto afirmar?", "Tiene un factor de riesgo, pero no es seguro que enferme", "Enfermará seguro", "No tiene riesgo", "El antecedente aumenta la probabilidad sin asegurarla."),
   ("abc", "Alguien dice «los controles de salud solo sirven si ya hay síntomas». ¿Qué corresponde responder?", "Los controles ayudan a detectar a tiempo, también sin síntomas", "Tiene razón", "No sirven", "Detectar a tiempo permite orientación profesional antes de que haya complicaciones."),
   ("abc", "Una tabla de ejemplo muestra que de 80 personas, 30 caminan a diario. ¿Cuál es una conclusión prudente?", "En este grupo, 30 de 80 caminan a diario", "Todos caminan", "Nadie camina", "Se limita a lo que la tabla dice."),
   ("abc", "Se afirma «si fumas, tendrás un infarto». ¿Qué falla?", "Fumar aumenta el riesgo, pero no asegura el infarto", "Nada", "Fumar protege", "Un factor de riesgo es una probabilidad, no un destino."),
   ("abc", "Un cuadro de ejemplo ordena: hipertensión, aterosclerosis, infarto. ¿Qué tienen en común?", "afectan al sistema circulatorio", "se contagian por gotitas", "afectan al sistema digestivo", "Las tres afectan al corazón o a los vasos sanguíneos.")],
  ("abc", "En una charla de una junta de vecinos, una persona escucha: «caminar a diario, comer con menos sal y no fumar ayudan a prevenir enfermedades del corazón». ¿Qué tipo de recomendación es?", "una medida general de prevención", "un diagnóstico personal", "un tratamiento", "Son hábitos generales, no un diagnóstico ni un tratamiento."),
  [("En Ciencias: ¿qué es un factor de riesgo?", "Una condición que aumenta la probabilidad de enfermar", "Solo aumenta la probabilidad, y no asegura que alguien enferme."),
   ("¿Qué es el sedentarismo?", "Poca actividad física en la vida diaria", "Es un factor de riesgo para el corazón y los vasos sanguíneos."),
   ("¿Las enfermedades del corazón se contagian?", "No", "No las causa un agente que pase entre personas.")],
  ("Con los datos de ejemplo: 100 personas, 40 hacen actividad física regular y 15 fuman, escribe un texto de cuatro líneas que diga cuántas personas no hacen actividad física, cuántas no fuman y una conclusión prudente. Agrega una frase que invite a consultar con un centro de salud.",
   "60 personas no hacen actividad física regular y 85 no fuman. En este grupo de ejemplo, más de la mitad no hace actividad física. Conviene consultar con un centro de salud para recibir orientación.",
   ["calcula 60 y 85", "formula una conclusión prudente", "incluye la frase de consulta"],
   ["Los dos cálculos son correctos.", "La conclusión se limita a los datos.", "Invita a consultar a un profesional."],
   "Si generaliza a toda la población, pregunta cuántas personas fueron. Si olvida la frase de consulta, pídele agregarla."),
  "Escribe dos hábitos que sirvan para cuidar el sistema circulatorio.",
  "Explica con tus palabras la diferencia entre un factor de riesgo y una causa segura.")

# ====================================================== OAD-03 clase 6
F = ("Ficha 6 (tres fuentes de ejemplo). Fuente A: folleto de un centro de salud, con autoría y fecha, que explica hábitos de prevención de la gastroenteritis. "
     "Fuente B: cadena anónima que promete «curar el corazón con un jugo». Fuente C: afiche de un centro de salud, con fecha, que recomienda ventilar los espacios y cubrirse al toser. "
     "Tabla de ejemplo: Gastroenteritis, sistema digestivo, higiene de manos. Neumonía, sistema respiratorio, vacunas según calendario. Hipertensión, sistema circulatorio, controles y actividad física.")
K(6, F,
  "Hoy revisaré lo logrado: comparar fuentes, ordenar la información de las enfermedades de tres sistemas en un cuadro y decidir qué sigo repasando.",
  ["Una investigación sobre enfermedades parte con una pregunta, busca fuentes confiables, anota qué dicen y compara. Un cuadro resumen ayuda: enfermedad, sistema afectado, causa y medidas de prevención. Con él se ven las diferencias entre las enfermedades infecciosas y las que se relacionan con hábitos.",
   "Al revisar cada fuente se pregunta: ¿quién la escribió?, ¿tiene fecha?, ¿la respalda una institución de salud?, ¿dice cómo lo sabe? Una cadena anónima que promete curas no cumple con ninguna de esas preguntas. La información de salud se usa para entender y prevenir, no para diagnosticarse.",
   "Terminada la investigación se hace una autoevaluación: qué aprendí, qué me falta y qué haré para repasar. Si algo de salud te preocupa, la persona indicada es un profesional del centro de salud más cercano."],
  [("cuadro resumen", "tabla que ordena la información por columnas"), ("comparar", "buscar semejanzas y diferencias"), ("sistema afectado", "sistema del cuerpo que la enfermedad perjudica"), ("autoevaluación", "revisión que hace la propia persona de su aprendizaje")],
  [("Evaluar una fuente", "¿Cuál de las fuentes de la ficha es más confiable para investigar la gastroenteritis?", ["Debe tener autoría y fecha.", "El folleto del centro de salud la tiene."], "La fuente A"),
   ("Completar un cuadro", "La neumonía es una infección de los pulmones. ¿Qué sistema afecta?", ["Los pulmones son parte del sistema respiratorio.", "Por eso se ubica en ese sistema."], "El sistema respiratorio")],
  [("Usar solo una fuente sin compararla.", "No se sabe si coincide con otras.", "Compara al menos dos fuentes confiables."),
   ("Copiar información de salud sin entenderla.", "No se puede explicar ni usar.", "Escribe con tus palabras lo que entendiste.")],
  [("abc", "{F} ¿Cuál de las fuentes de la ficha 6 es la más confiable sobre la prevención de la gastroenteritis?", "la fuente A", "la fuente B", "la fuente C", "La fuente A tiene autoría, fecha y respaldo institucional, y trata ese tema."),
   ("abc", "{F} ¿Por qué la fuente B no es confiable?", "Es anónima y promete curar con un jugo", "Tiene fecha", "Está firmada", "Una cadena anónima con promesas no tiene respaldo."),
   ("abc", "{F} ¿Qué medida de prevención recomienda la fuente C?", "ventilar los espacios y cubrirse al toser", "dejar la comida fuera del refrigerador", "fumar menos", "La fuente C recomienda ventilar y cubrirse al toser."),
   ("abc", "{F} Según la tabla, ¿qué sistema afecta la hipertensión?", "el sistema circulatorio", "el sistema digestivo", "el sistema respiratorio", "La tabla ubica la hipertensión en el sistema circulatorio."),
   ("abc", "{F} Según la tabla, ¿qué medida se asocia con la gastroenteritis?", "higiene de manos", "vacunas según calendario", "controles y actividad física", "La tabla asocia la gastroenteritis con la higiene de manos."),
   ("abc", "{F} Según la tabla, ¿qué medida se asocia con la neumonía?", "vacunas según calendario", "higiene de manos", "controles y actividad física", "La tabla asocia la neumonía con vacunas según calendario."),
   ("abc", "¿Qué enfermedad de la tabla es probable que no sea contagiosa?", "la hipertensión", "la gastroenteritis", "la neumonía", "La hipertensión se relaciona con factores de riesgo y no con un agente que se contagie."),
   ("abc", "¿Qué pregunta ayuda a evaluar una fuente de salud?", "¿Quién la escribió y tiene fecha y respaldo?", "¿Cuántos la compartieron?", "¿Es más larga?", "La autoría, la fecha y el respaldo muestran confiabilidad."),
   ("abc", "Alguien dice «con esta tabla ya sé qué enfermedad tengo». ¿Qué corresponde responder?", "La información sirve para entender y prevenir; el diagnóstico lo hace un profesional", "Tiene razón", "La tabla es un diagnóstico", "Un cuadro general no reemplaza la evaluación de un profesional."),
   ("abc", "Se piensa que basta una fuente para decidir. ¿Cuál es el error?", "No se compara con otras fuentes confiables", "Una fuente siempre alcanza", "Las fuentes no importan", "Comparar fuentes permite saber si coinciden."),
   ("abc", "En un cuadro resumen se organizan filas de enfermedad, sistema, causa y prevención. ¿Para qué sirve?", "Para comparar de un vistazo la información", "Para decorar", "Para diagnosticar", "Ordenar en columnas facilita ver semejanzas y diferencias."),
   ("abc", "Una persona termina su investigación con «aprendí a evaluar fuentes; me falta repasar el sistema circulatorio». ¿Qué hizo?", "una autoevaluación", "un diagnóstico", "una receta", "Reconoció lo logrado y lo que falta."),
   ("abc", "Se compara una enfermedad infecciosa con una relacionada con hábitos. ¿Cuál es una diferencia?", "La infecciosa la causa un agente que se contagia; la otra se relaciona con factores de riesgo", "Todas se contagian", "Ninguna tiene prevención", "La causa y la forma de prevenirlas son distintas.")],
  ("abc", "En el consultorio, una persona recibe un folleto sobre cómo prevenir enfermedades respiratorias. ¿Cuál es una buena práctica al usarlo?", "leer, comprender y consultar al equipo de salud ante dudas", "usarlo para diagnosticarse", "ignorarlo", "El folleto orienta, pero las dudas personales se resuelven con un profesional."),
  [("En Ciencias: ¿qué es un cuadro resumen?", "Una tabla que ordena la información en columnas", "Permite comparar la información de varias enfermedades de un vistazo."),
   ("¿Qué se revisa en una fuente de salud?", "Autoría, fecha y respaldo", "Con eso se decide si es confiable."),
   ("¿Para qué sirve la información de salud de un cuaderno?", "Para entender y prevenir, no para diagnosticar", "El diagnóstico lo realiza un profesional.")],
  ("Arma tu propio cuadro resumen con tres enfermedades (una digestiva, una respiratoria y una circulatoria) y estas columnas: sistema afectado, causa y una medida de prevención. Después escribe cuál fuente de la ficha 6 usarías y por qué.",
   "Gastroenteritis, digestivo, virus o bacterias, higiene de manos. Neumonía, respiratorio, virus o bacterias, vacunas según el calendario. Hipertensión, circulatorio, factores de riesgo, actividad física. Usaría las fuentes A y C porque tienen autoría y fecha.",
   ["incluye tres enfermedades de tres sistemas", "completa las tres columnas", "elige fuentes con una razón"],
   ["Los sistemas están bien ubicados.", "La causa y la prevención coinciden con lo estudiado.", "La razón usa autoría o fecha."],
   "Si repite el sistema, pregunta qué órgano se afecta. Si elige la cadena anónima, pregunta quién la firma."),
  "Escribe tres preguntas que seguirías investigando sobre una enfermedad de tu elección.",
  "Explica cómo le explicarías a una persona cercana qué fuente de salud es confiable.")
