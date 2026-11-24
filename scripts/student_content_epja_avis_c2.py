"""Artes Visuales EPJA Media N1 y N2, módulo 3, OAD-10: analizar una obra cinematográfica e interpretar su propósito expresivo (2 clases). Obras inventadas descritas por escrito."""
from __future__ import annotations

from epja_avis_c_common import K

O = "EPJA-AVIS-NM1y2-OAD-10"

# ====================================================== clase 1
F = ("Ficha 1 (obra de ejemplo inventada; no es una película real). «La última micro», cortometraje ficticio de 12 minutos. "
     "Rosa, una trabajadora de aseo, espera cada noche la última micro para volver a casa. "
     "Escena 1 (3 min): plano general de un paradero vacío, luz azul y fría de un poste, se oye el viento; Rosa se ve pequeña en el cuadro. "
     "Escena 2 (2 min): primer plano de Rosa mirando el reloj; solo se oye el segundero; nadie habla. "
     "Escena 3 (4 min): la micro llega con luz cálida adentro, suena música suave y Rosa se sienta junto a la ventana. "
     "Cierre: corte directo a una casa con una ventana iluminada, sin mostrar el viaje.")
K(O, 1, F,
  "Hoy aprenderé a distinguir describir de interpretar una obra cinematográfica y a reconocer los criterios con que se analiza su propósito expresivo.",
  ["Analizar una obra es mirarla con atención y con criterios, no solo decir si gustó. Primero se describe: qué se ve y qué se oye, sin opinar. Después se interpreta: qué idea, sensación o emoción propone la obra y para qué. La interpretación debe apoyarse en evidencia, es decir, en algo concreto de la obra.",
   "Los criterios estéticos de esta clase son cinco: las sensaciones y emociones que genera, las ideas, el tema, los elementos contextuales (lugar, época, trabajo, modo de vida que se muestra) y el lenguaje audiovisual (planos, luz, sonido, montaje). El propósito expresivo es lo que la obra quiere comunicar o provocar con esos recursos.",
   "Una elipsis omite un tramo y el público lo deduce, como el viaje en micro de la obra de ejemplo. Una metáfora visual presenta una imagen que representa otra idea. Dos personas pueden interpretar distinto y ambas tener razón si muestran evidencia. Analizar también implica estar dispuesto a cambiar de opinión."],
  [("propósito expresivo", "lo que una obra quiere comunicar o provocar con sus recursos"), ("describir", "decir lo que se ve y se oye, sin opinar"), ("interpretar", "proponer qué idea o emoción comunica la obra, con evidencia"), ("elipsis", "tramo de la acción que no se muestra y se deduce")],
  [("Describir o interpretar", "Con la ficha 1: «Rosa aparece pequeña en un paradero vacío». ¿Es descripción o interpretación?", ["Dice lo que se ve en la escena 1.", "No agrega ninguna idea ni opinión."], "Descripción"),
   ("Interpretar con evidencia", "Una persona dice: «la escena 1 transmite soledad». ¿Qué evidencia de la ficha la apoya?", ["Se ve un paradero vacío y a Rosa pequeña.", "La luz es azul y fría, y solo se oye el viento."], "Paradero vacío, Rosa pequeña, luz fría y viento")],
  [("Interpretar es opinar lo que a mí me gusta.", "Se confunde interpretar con decir «me gustó».", "Interpretar es proponer un sentido y probarlo con algo concreto de la obra."),
   ("Solo hay una interpretación correcta.", "Se cree que existe una respuesta única.", "Varias interpretaciones pueden valer si cada una muestra evidencia.")],
  [("abc", "En Artes Visuales: ¿qué es interpretar una obra?", "Proponer qué idea o emoción comunica, apoyándose en evidencia", "Contar la historia en el mismo orden", "Decir si el actor es conocido", "Interpretar da sentido a lo que se ve y se oye con razones."),
   ("abc", "{F} «Rosa mira el reloj y se oye el segundero» es una", "descripción de lo que se ve y se oye", "interpretación sin evidencia", "opinión sobre el director", "Solo informa lo que muestra la escena 2."),
   ("abc", "{F} «La escena 2 transmite la tensión de la espera» es una", "interpretación apoyada en el primer plano y el segundero", "descripción sin ninguna idea", "opinión sin relación con la ficha", "Propone una emoción y la ficha ofrece evidencia."),
   ("abc", "{F} ¿Qué sensación puede generar la luz cálida del interior de la micro en la escena 3?", "Calidez y alivio", "Frío y abandono", "Peligro y miedo", "La luz cálida y la música suave se asocian con acogida."),
   ("ab", "{F} ¿Cuál es un elemento contextual de la ficha?", "El trabajo de aseo y el viaje nocturno en transporte público", "El ángulo de la cámara", "El contexto es el modo de vida del personaje; el ángulo es lenguaje audiovisual."),
   ("abc", "{F} El tema de la obra se describe mejor como", "la espera de una trabajadora para volver a casa de noche", "la rivalidad entre dos vecinas", "un viaje de vacaciones", "La ficha trata de Rosa esperando volver a casa tras su trabajo."),
   ("=", "{F} Las escenas 1, 2 y 3 duran 3, 2 y 4 minutos. La obra dura 12. ¿Cuántos minutos queda para el cierre?", "12-3-2-4", "Se restan las tres escenas de los 12 minutos: 12 − 9 = 3 minutos.", " minutos"),
   ("abc", "{F} ¿Qué cambia entre la luz de la escena 1 y la de la escena 3?", "Pasa de luz fría a luz cálida", "Pasa de luz cálida a luz fría", "Se mantiene igual en las dos", "Una es azul y fría; la otra, cálida dentro de la micro."),
   ("abc", "{F} El cierre salta del interior de la micro a la casa sin mostrar el viaje. Eso es una", "elipsis", "metáfora", "ángulo picado", "Se omite un tramo y el público lo deduce."),
   ("abc", "¿Cuál comentario usa evidencia de la obra?", "«Rosa se ve pequeña en el plano general, y por eso parece sola»", "«Esa película no me gustó porque sí»", "«Seguro la hizo alguien famoso»", "Cita un recurso concreto y explica qué efecto produce."),
   ("ab", "{F} Una persona pensaba que la obra era solo triste, pero nota la luz cálida de la escena 3 y la ventana iluminada de la casa. ¿Qué actitud muestra flexibilidad?", "Reformula: la obra mezcla cansancio y esperanza", "Mantiene su idea y ignora esas escenas", "Al ver nueva evidencia, ajusta su interpretación en vez de defenderla a toda costa."),
   ("abc", "{F} ¿Qué interpretación del cierre en la casa está mejor respaldada?", "Que Rosa llegó a un lugar cálido y de descanso, por la ventana iluminada", "Que Rosa se perdió, por el viento de la escena 1", "Que la micro chocó, porque no se muestra el viaje", "La ventana iluminada se relaciona con calidez y hogar."),
   ("abc", "Dos personas interpretan distinto un final, y ambas citan escenas. ¿Qué es lo más razonable?", "Aceptar que ambas pueden tener argumentos válidos", "Decidir que una es ignorante", "Prohibir hablar del tema", "El análisis se basa en razones, no en una única respuesta.")],
  ("abc", "Una persona ve en una sede vecinal un cortometraje inventado donde una vecina cuida cada tarde una huerta común y al final los vecinos comparten las verduras. ¿Cuál comentario mezcla descripción e interpretación bien?",
   "«Se ve a la vecina cuidando la huerta (descripción); propone que cuidar lo común une al barrio (interpretación)»", "«Me aburrió y punto»", "«Es una película real de un director conocido»", "Distingue lo que se ve de la idea que propone y las vincula."),
  [("En Artes Visuales: ¿qué es el propósito expresivo?", "Lo que la obra quiere comunicar o provocar", "Se analiza con los recursos que usa."),
   ("Al ver una obra audiovisual: ¿qué diferencia hay entre describir e interpretar?", "Describir informa lo que hay; interpretar propone un sentido con evidencia", "Interpretar necesita razones de la obra."),
   ("¿Qué es una elipsis?", "Omitir un tramo para que el público lo deduzca", "El viaje en micro no se muestra.")],
  ("{F} Escribe un comentario de cinco líneas sobre la escena 2 de la ficha: dos líneas de descripción, dos de interpretación con evidencia y una que diga qué sensación te produce.",
   "Descripción: primer plano de Rosa que mira el reloj; solo se oye el segundero. Interpretación: transmite espera tensa porque el rostro cerca y el sonido repetido llenan el silencio. Sensación: me hace sentir su cansancio.",
   ["separa descripción e interpretación", "usa evidencia de la ficha", "nombra una sensación", "no copia la ficha entera"],
   ["comentario de cinco líneas con descripción, interpretación y sensación"],
   ["opinar sin evidencia", "mezclar lo que se ve con lo que se supone"],
   "Revisa que la interpretación cite un recurso (plano, luz, sonido). Si solo dice «me gustó», pide un dato de la ficha."),
  "Subraya en la ficha tres datos que puedan servir de evidencia para la sensación de espera.",
  "Escribe una interpretación distinta de la elipsis del cierre y cítala con evidencia.")

# ====================================================== clase 2
F = ("Ficha 2 (obra de ejemplo inventada; no es una película real). «El pasaje», cortometraje ficticio de 8 minutos, exhibido en el cine comunitario de una sede vecinal inventada. "
     "Don Aurelio, vecino mayor, barre cada mañana su pasaje. "
     "Escena 1: plano medio de don Aurelio barriendo; se oye la escoba; luz de amanecer. "
     "Escena 2: plano detalle de una flor que crece en una grieta del pavimento; música suave de piano. "
     "Escena 3: plano general del pasaje limpio, con vecinos que abren ventanas y lo saludan; se oyen voces y una radio. "
     "Entre la escena 2 y la 3 no se muestra cómo se limpió el pasaje. "
     "Pauta del comentario: 1) descripción; 2) interpretación; 3) evidencia; 4) contexto.")
K(O, 2, F,
  "Hoy aprenderé a redactar un análisis con postura razonada de una obra y a revisar mis ideas si aparece nueva evidencia.",
  ["Un buen análisis tiene cuatro partes: describir lo que se ve y se oye, interpretar qué propone, mostrar la evidencia y relacionarlo con el contexto, es decir, con la vida y el lugar que la obra muestra. Así una postura deja de ser una simple opinión y pasa a ser una postura razonada.",
   "Una metáfora visual es una imagen que representa otra idea. En la obra de ejemplo, una flor que crece en una grieta puede representar algo bello que nace en un lugar duro. Una elipsis omite un tramo del tiempo: aquí no se muestra cómo se limpió el pasaje, y el público lo imagina. Ambos recursos dejan espacio para que cada persona interprete.",
   "En tu comunidad también hay obras audiovisuales: videos de una junta de vecinos, un documental local, un cine en la sede. Analizarlas es una conversación entre personas. Escucha otras lecturas, compáralas con tu evidencia y reelabora tu idea si hay buenas razones."],
  [("postura razonada", "opinión apoyada en razones y evidencia de la obra"), ("metáfora visual", "imagen que representa otra idea"), ("elipsis", "tramo omitido que el público deduce"), ("contexto", "lugar, trabajo y modo de vida que la obra muestra")],
  [("Armar una interpretación", "Con la ficha 2, interpreta la flor en la grieta: ¿qué puede representar y qué evidencia lo apoya?", ["Idea: algo vivo y bello crece en un lugar duro.", "Evidencia: plano detalle de la flor en el pavimento y música suave."], "Esperanza que nace en un lugar duro; plano detalle, grieta y piano"),
   ("Reelaborar una idea", "Alguien pensaba que «El pasaje» trata solo de limpieza. Al notar la escena 3, ¿cómo reformula?", ["La escena 3 muestra a los vecinos saludando.", "Reformula: la obra trata de cuidar el espacio común y de cómo eso une a las personas."], "Trata del cuidado del espacio común y de la unión del barrio")],
  [("Una postura razonada es la más fuerte o la más repetida.", "Se confunde razonar con insistir.", "Se razona mostrando evidencia, no gritando ni repitiendo."),
   ("Cambiar de interpretación es perder.", "Se asocia cambiar con equivocarse.", "Reelaborar con nueva evidencia es parte de analizar bien.")],
  [("abc", "En Artes Visuales: ¿qué es una postura razonada?", "Una opinión apoyada en razones y evidencia de la obra", "Una opinión repetida en voz alta", "Una opinión copiada de otra persona", "Se justifica con algo concreto de lo visto y oído."),
   ("abc", "{F} ¿Cuál es el elemento sonoro de la escena 1?", "El ruido de la escoba", "La música de piano", "Las voces de los vecinos", "La ficha indica que en la escena 1 se oye la escoba."),
   ("ab", "{F} ¿Qué plano se usa en la escena 2?", "Plano detalle", "Plano general", "La flor en la grieta se muestra en un plano detalle."),
   ("abc", "{F} Una metáfora visual es", "una imagen que representa otra idea", "un movimiento de cámara", "el tiempo que dura una escena", "La flor puede representar algo más que una flor."),
   ("abc", "{F} ¿Qué tramo se omite entre la escena 2 y la 3?", "Cómo se limpió el pasaje", "La llegada de don Aurelio", "El saludo de los vecinos", "El público ve la flor y luego el pasaje limpio sin el proceso."),
   ("=", "{F} Suponte que las escenas 1, 2 y 3 duran 3, 1 y 3 minutos y el corto dura 8. ¿Cuántos minutos faltan por asignar?", "8-3-1-3", "Se restan 3, 1 y 3 de 8: 8 − 7 = 1 minuto.", " minutos"),
   ("abc", "{F} ¿Qué interpretación de la escena 1 está mejor respaldada?", "Don Aurelio cuida su pasaje con constancia cada mañana", "Don Aurelio está enojado con sus vecinos", "Don Aurelio está por mudarse del pasaje", "La escoba, el plano medio y la luz de amanecer muestran un trabajo diario y tranquilo."),
   ("abc", "{F} ¿Qué contexto muestra la obra?", "La vida cotidiana de un pasaje de barrio y un vecino mayor que lo cuida", "Un viaje en tren de lujo", "Un laboratorio de ciencias", "Ese es el entorno y modo de vida que la ficha describe."),
   ("abc", "{F} ¿Cuál comentario separa bien la descripción de la interpretación?", "«Hay un plano detalle de una flor (descripción); sugiere esperanza (interpretación)»", "«La flor me gustó y ya»", "«Es mejor que cualquier otra obra»", "Lo que se ve queda aparte de la idea que se propone."),
   ("abc", "Una persona ve evidencia nueva que contradice su idea. ¿Qué hace alguien flexible?", "Revisa su idea y la ajusta si las razones lo piden", "Evita volver a mirar la obra", "Descalifica a quien opina distinto", "Analizar bien incluye reelaborar cuando aparecen buenas razones."),
   ("ab", "{F} ¿Qué parte de la pauta pide citar la escena que respalda la idea?", "Evidencia", "Descripción", "La evidencia es el dato concreto que sostiene la interpretación."),
   ("abc", "{F} Una vecina interpreta la flor como símbolo de esperanza y otra como «fragilidad de lo bello». ¿Qué es lo más razonable?", "Comparar las razones de ambas y ver si pueden complementarse", "Elegir la de quien habla más fuerte", "Anular las dos y no opinar", "Ambas pueden tener argumentos válidos con la misma evidencia."),
   ("abc", "En un cine comunitario se comenta una obra después de verla. ¿Qué actitud ayuda más a analizarla?", "Escuchar otras lecturas y citar evidencia propia", "Interrumpir para imponer la mía", "Opinar sin haber mirado la obra", "Una conversación respetuosa con evidencia enriquece el análisis.")],
  ("abc", "En la sede vecinal se exhibe un cortometraje inventado sobre una feria de barrio. Una persona escribe: «Me gustó el final porque el último plano muestra a todos juntos bajo una luz cálida; creo que dice que la comunidad se sostiene entre todos». ¿Qué le falta a su comentario para ser completo según la pauta?",
   "Mencionar el contexto, es decir, qué muestra la obra de la vida del barrio", "Nada, porque ya opinó", "Decir quién la dirigió", "La pauta pide descripción, interpretación, evidencia y contexto; falta ligarla con el entorno."),
  [("En Artes Visuales: ¿qué es una metáfora visual?", "Una imagen que representa otra idea", "La flor en la grieta puede ser un ejemplo."),
   ("¿Cuáles son las cuatro partes de la pauta?", "Descripción, interpretación, evidencia y contexto", "Ordenan un análisis completo y bien fundamentado."),
   ("¿Por qué conviene reelaborar una idea?", "Porque aparece evidencia nueva o otra lectura razonable", "Así el análisis se vuelve más justo y completo.")],
  ("{F} Escribe un comentario de 8 a 10 líneas sobre «El pasaje» con las cuatro partes de la pauta, y termina con una frase que diga si tu idea cambió al considerar otra interpretación posible, que escribes en una línea.",
   "Descripción: plano detalle de una flor en una grieta; música de piano. Interpretación: esperanza en un lugar duro. Evidencia: el plano cercano y la música suave. Contexto: pasaje de barrio y su cuidado. Cambié mi idea: ahora veo también el trabajo diario de don Aurelio.",
   ["incluye descripción e interpretación separadas", "cita evidencia de la ficha", "relaciona con el contexto", "muestra flexibilidad ante otra lectura"],
   ["comentario de 8 a 10 líneas con las cuatro partes y una frase de revisión"],
   ["omitir el contexto", "no citar ninguna evidencia"],
   "Revisa que estén las cuatro partes y que la evidencia salga de la ficha. Reconoce la flexibilidad cuando la persona ajusta su idea con razones."),
  "Completa una tabla con cuatro filas (descripción, interpretación, evidencia y contexto) para la escena 3.",
  "Escribe una interpretación opuesta a la tuya sobre la flor y evalúa cuál tiene más evidencia.")
