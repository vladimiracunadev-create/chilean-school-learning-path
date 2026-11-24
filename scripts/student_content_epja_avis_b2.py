"""Artes Visuales EPJA Media N1 y N2, módulo 2, OAD-06: desarrollar y evaluar ideas para murales a partir de un propósito expresivo y de la selección de procedimientos, materiales y soportes. Casos ficticios; bocetos descritos con palabras; todo en papel."""
from __future__ import annotations

from epja_avis_b_common import K

O6 = "EPJA-AVIS-NM1y2-OAD-06"

# ====================================================== OAD-06 clase 1
F = ("Ficha 1 (caso ficticio). Un grupo de vecinas y vecinos de un pasaje quiere un mural en el muro lateral de la sede social: 6 metros de largo y 2 metros de alto, de cemento liso, bajo un alero que lo protege de la lluvia. "
     "Problemática del grupo: se acumula basura en la esquina. Ideas descritas con palabras (obras de ejemplo, sin imágenes). "
     "Idea 1: un tarro de basura grande dibujado en azul y blanco, con el lema escrito «Mi esquina, mi cuidado»; se pintaría con brocha. "
     "Idea 2: un árbol hecho con tapas de botellas de colores pegadas sobre el muro; necesita un adhesivo adecuado para muros. "
     "Idea 3: un paisaje del barrio con muchas casas y mucho detalle fino.")
K(O6, 1, F,
  "Hoy aprenderé a pensar un mural: elegir su propósito expresivo, su tema a partir de una problemática propia, el soporte, los materiales y los procedimientos, y a evaluar las ideas con criterios.",
  ["Un mural es una obra de gran formato hecha sobre un muro u otro soporte fijo, pensada para un lugar que se comparte. Antes de pintar, se desarrolla la idea: ¿qué queremos expresar? Ese es el propósito expresivo. El tema puede salir de una problemática propia, como la basura en una esquina, un pasaje oscuro o la memoria del barrio. Así el mural habla de algo que la comunidad conoce.",
   "Luego se decide con qué y sobre qué. El soporte es la superficie donde se hace la obra: un muro de cemento, un panel de madera o una tela grande. Los materiales son lo que se usa: pintura, tapas, papeles. El procedimiento es cómo se trabaja: pintura con brocha, plantilla recortada para repetir una forma, collage con piezas pegadas. Conviene elegir materiales cotidianos, seguros y fáciles de conseguir.",
   "Evaluar una idea es compararla con criterios antes de gastar tiempo y materiales. Se pregunta si el propósito es claro, si se entiende a distancia, si el soporte y los materiales calzan, si se puede hacer con el tiempo y los recursos disponibles, y si la comunidad está de acuerdo. También se pide autorización a quien administra el muro. Un boceto, que es un dibujo previo y simple de la idea, permite probar antes de pintar."],
  [("mural", "obra de gran formato hecha sobre un muro u otro soporte fijo para un lugar compartido"), ("soporte", "superficie sobre la que se hace la obra"), ("boceto", "dibujo previo y simple para probar una idea antes de hacerla"), ("evaluar una idea", "compararla con criterios antes de decidir si se hace")],
  [("Distinguir soporte y material", "En la idea 2 de ejemplo, un árbol de tapas pegadas sobre un muro de cemento. ¿Cuál es el soporte y cuál el material?",
    ["El soporte es la superficie donde se hace la obra: el muro de cemento.", "El material es lo que se pega: las tapas de botellas."], "Soporte: muro de cemento. Material: tapas de botellas."),
   ("Evaluar a distancia", "La idea 3 tiene muchas casas con detalle fino y el muro se verá desde unos metros. ¿Qué se anota al evaluarla?",
    ["Los detalles finos son pequeños.", "Desde lejos no se alcanzarán a ver: se anota que su legibilidad a distancia es baja."], "Baja legibilidad a distancia")],
  [("Elegir la idea que más gusta sin evaluarla.", "Se confunde preferencia con evaluación.", "Compara las ideas con los mismos criterios antes de decidir."),
   ("Empezar a pintar sin boceto.", "Se cree que el boceto es una pérdida de tiempo.", "Un boceto permite corregir tamaño, colores y texto antes de pintar el muro.")],
  [("abc", "En Artes Visuales: ¿qué es un mural?", "Una obra de gran formato hecha sobre un muro u otro soporte fijo, pensada para un lugar compartido", "Una fotografía pequeña guardada en un álbum", "Un dibujo hecho solo para guardar en un cajón", "Un mural se hace sobre un soporte fijo y se comparte con quienes pasan por el lugar."),
   ("abc", "{F} ¿Cuáles son las medidas del muro de la ficha?", "6 metros de largo y 2 metros de alto", "2 metros de largo y 6 metros de alto", "6 metros de largo y 6 metros de alto", "La ficha indica un muro de 6 metros de largo por 2 metros de alto."),
   ("ab", "Para que un mural tenga sentido para una comunidad, su tema debería", "relacionarse con una problemática o historia propia del lugar", "ser igual al de cualquier otro mural de otro barrio", "Un tema propio hace que las personas se reconozcan en la obra."),
   ("abc", "El propósito expresivo de un mural es", "la idea o sensación que quiere comunicar a quienes lo miran", "el tipo de brocha que se usa", "el nombre de quien lo pinta", "El propósito responde a qué se quiere expresar con la obra."),
   ("abc", "{F} ¿Cuál es el soporte del mural de la ficha?", "El muro lateral de cemento liso de la sede", "Las tapas de botellas de colores", "La brocha con que se pintaría", "El soporte es la superficie donde se hace la obra, aquí el muro."),
   ("abc", "{F} En la idea 2, las tapas de botellas son", "el material", "el soporte", "el tema", "Son lo que se usa para hacer el árbol; el soporte es el muro."),
   ("=", "{F} ¿Cuántos metros cuadrados de superficie tiene el muro?", "6*2", "La superficie se calcula multiplicando el largo por el alto del muro.", " m²"),
   ("=", "Una pintura de ejemplo indica en su etiqueta que rinde 4 metros cuadrados por tarro. ¿Cuántos tarros hacen falta para cubrir 12 metros cuadrados?", "12//4", "Se divide la superficie por lo que rinde cada tarro de ejemplo.", " tarros"),
   ("abc", "{F} ¿Qué idea incluye un mensaje escrito que llama directamente a cuidar la esquina?", "La idea 1, con el lema «Mi esquina, mi cuidado»", "La idea 2, el árbol de tapas", "La idea 3, el paisaje del barrio", "Solo la idea 1 incluye un lema escrito sobre el cuidado de la esquina."),
   ("abc", "{F} Entre las ideas 1 y 3, ¿cuál es más fácil de leer desde varios metros de distancia?", "La idea 1, porque es una imagen grande y simple con un lema", "La idea 3, porque tiene más detalle fino", "Ambas por igual, porque el muro tiene el mismo tamaño", "Una imagen grande y simple se entiende a distancia; el detalle fino se pierde."),
   ("ab", "{F} Si el muro no tuviera alero y recibiera lluvia, ¿qué habría que evaluar además?", "Si los materiales y la pintura resisten la humedad", "Nada, porque la lluvia no afecta a un mural", "Un muro expuesto necesita materiales que aguanten el agua."),
   ("abc", "{F} La idea 2 pega tapas sobre un muro liso. ¿Qué conviene evaluar antes de elegirla?", "Si hay un adhesivo adecuado para muros y si las tapas se mantendrán firmes con el tiempo", "Solo si a todos les gustan los colores", "Nada, porque las tapas son livianas", "La durabilidad del pegado sobre un muro liso es parte de la factibilidad."),
   ("abc", "Un vecino dice: «el muro es de la sede, pero el mural lo veremos todos». ¿Qué paso conviene incluir antes de pintar?", "Acordar con quien administra el muro y con la comunidad qué se hará", "Empezar a pintar y pedir permiso si alguien reclama", "Elegir la idea sin conversar con el resto del grupo", "Un acuerdo previo cuida el espacio compartido y evita conflictos.")],
  ("abc", "Un taller de ejemplo evalúa un boceto de mural: letras amarillas sobre un fondo blanco, en un muro que se verá desde 10 metros. ¿Qué observación es más útil?", "El contraste entre letra y fondo es bajo, así que costará leerlo a distancia", "Las letras amarillas se ven alegres, así que no hay nada que corregir", "Nada que observar, porque todo boceto sirve", "Un contraste bajo dificulta leer el texto desde lejos y conviene corregirlo."),
  [("En Artes Visuales: ¿qué es el soporte de una obra?", "La superficie sobre la que se hace", "Elegirlo bien evita problemas de pintura o de pegado."),
   ("En Artes Visuales: ¿para qué sirve un boceto de mural?", "Para probar la idea antes de hacerla en el muro", "Corregir en papel es más fácil y barato que en el muro."),
   ("¿Qué se pregunta al evaluar una idea de mural?", "Si el propósito es claro, si se ve a distancia y si es factible", "Los mismos criterios permiten comparar ideas con justicia.")],
  ("{F} Elige una de las tres ideas y evalúala: escribe su propósito, el soporte y el material, una fortaleza y un problema, y una decisión (seguirla, ajustarla o descartarla) con una razón.",
   "Idea 1. Propósito: invitar a cuidar la esquina. Soporte: muro de cemento. Material: pintura azul y blanca. Fortaleza: el lema se lee a distancia. Problema: el tarro solo puede parecer aburrido. Decisión: ajustarla, sumando un dibujo de vecinos cuidando la esquina, porque eso conecta con la comunidad.",
   ["nombra propósito, soporte y material", "indica una fortaleza y un problema", "toma una decisión con razón", "usa solo datos de la ficha"],
   ["lista breve de seis líneas más una frase de decisión"],
   ["decidir solo por gusto", "olvidar la legibilidad a distancia"],
   "Revisa que la decisión tenga una razón apoyada en un criterio. Si la persona escribe solo «me gusta», pregunta qué criterio se cumple. Reconoce las decisiones de ajustar bien fundamentadas."),
  "Escribe tres criterios para evaluar una idea de mural y una pregunta para cada uno.",
  "Describe con palabras un boceto simple de un mural para un pasaje o un lugar de trabajo, con un máximo de tres colores, sin dar datos personales.")

# ====================================================== OAD-06 clase 2
F = ("Ficha 2 (caso ficticio; ideas descritas con palabras, obras de ejemplo). El centro comunitario de un barrio quiere un mural en el muro del acceso: 8 metros de largo y 2 de alto, de ladrillo pintado de blanco, sin alero, expuesto a la lluvia. "
     "Problemática: el pasaje de acceso es oscuro de noche y poco acogedor. "
     "Idea A, «Ventanas con luz»: filas de ventanas amarillas pintadas, cada una distinta, para dar sensación de pasaje habitado y claro; pintura para exteriores en cuatro colores y plantillas de cartón para repetir las ventanas. "
     "Idea B, «Retratos del barrio»: doce rostros realistas de vecinos; exige mucha técnica de dibujo y el permiso de cada persona retratada. "
     "Idea C, «Frase gigante»: letras negras sobre fondo blanco que dicen «Pasaje con luz, pasaje seguro»; muy legible, con pintura simple y casi sin imagen. "
     "Pauta de ejemplo: cinco criterios puntuados de 0 a 2 (propósito y tema, legible a distancia, factible con materiales y tiempo, resiste el exterior, participación de la comunidad). "
     "Puntajes del grupo: A = 2, 2, 2, 1, 2; B = 2, 1, 0, 1, 1; C = 1, 2, 2, 2, 0.")
K(O6, 2, F,
  "Hoy aplicaré la evaluación de ideas de mural a un caso de comunidad: compararé tres ideas con una pauta, decidiré con razones y describiré un boceto con palabras.",
  ["En una comunidad real casi nunca hay una sola buena idea. Por eso se comparan varias. Una pauta con criterios y puntajes sirve para que todas las ideas se midan igual. Los puntajes se suman, pero no deciden solos: se mira también el lugar, el tiempo y las personas que participarán.",
   "Cuando una idea tiene un punto débil, se puede ajustar en vez de descartarla. Una idea con mucho detalle puede simplificarse. Una idea sin participación puede abrirse a que los vecinos pinten junto con el grupo. También se pueden combinar dos ideas si hay espacio, tiempo y materiales para ambas, y si el mensaje sigue claro.",
   "El resultado de la evaluación es un boceto descrito: qué va arriba, abajo y al centro, qué colores se usan, qué texto lleva y desde qué distancia se leerá. En esta clase todo se hace con palabras y cifras de ejemplo; la realización del mural viene después. Si tienes dudas sobre permisos, consulta a quien administra el muro."],
  [("pauta de evaluación", "tabla de criterios con puntajes para comparar ideas"), ("factible", "que se puede hacer con el tiempo, los materiales y las personas disponibles"), ("ajustar una idea", "cambiarla para corregir un punto débil sin perder su propósito"), ("participación", "que la comunidad tome parte en elegir o hacer el mural")],
  [("Sumar una pauta", "La idea A de ejemplo obtuvo 2, 2, 2, 1 y 2 en los cinco criterios. ¿Cuánto suma, de un máximo de 10?",
    ["Se suman los cinco puntajes: 2 + 2 = 4.", "4 + 2 = 6, 6 + 1 = 7 y 7 + 2 = 9."], "9 de 10 puntos"),
   ("Ajustar una idea", "La idea C de ejemplo tiene 0 en participación. ¿Cómo ajustarla sin cambiar su propósito?",
    ["Su problema es que los vecinos no participan.", "Se puede invitar a pintar las letras juntos y a elegir la frase entre varias."], "Invitar a vecinos a pintar y a elegir la frase")],
  [("Elegir sin comparar con los mismos criterios.", "Se evalúa cada idea con una vara distinta.", "Aplica la misma pauta a todas las ideas y compara los puntajes."),
   ("Creer que una idea con puntaje bajo no sirve para nada.", "Se confunde puntaje con valor.", "Un punto débil se puede ajustar; revisa cuál criterio bajó el puntaje.")],
  [("abc", "{F} ¿Cuál es la problemática que motiva el mural?", "Un pasaje de acceso oscuro de noche y poco acogedor", "La falta de pintura en el centro", "El precio del ladrillo", "La ficha declara esa problemática como motivo del mural."),
   ("abc", "{F} ¿Qué soporte tiene el mural?", "Un muro de ladrillo pintado de blanco", "Una tela colgada", "Un panel de madera", "La ficha describe un muro de ladrillo pintado de blanco, de 8 por 2 metros."),
   ("abc", "{F} ¿Qué idea usa plantillas de cartón para repetir las ventanas?", "La idea A, «Ventanas con luz»", "La idea B, «Retratos del barrio»", "La idea C, «Frase gigante»", "Las plantillas de cartón están en la descripción de la idea A."),
   ("=", "{F} ¿Cuántos puntos suma la idea B?", "2+1+0+1+1", "Se suman los cinco puntajes de la idea B en la pauta de la ficha.", " puntos"),
   ("abc", "{F} ¿Qué diferencia principal hay entre la idea A y la idea C?", "La A se apoya en una imagen repetida de ventanas y la C en una frase escrita", "La A usa solo texto y la C solo imágenes", "No hay diferencia: son la misma idea", "A usa imágenes y C usa texto como elemento central, según la ficha."),
   ("ab", "{F} ¿Por qué la idea B obtuvo 0 en factibilidad?", "Exige rostros realistas con mucha técnica y el permiso de cada persona retratada", "Porque el muro es de ladrillo y todo lo demás sería igual de difícil", "La ficha indica la técnica avanzada y los permisos como las dificultades de B."),
   ("=", "{F} ¿Cuántos puntos más tiene la idea A que la idea C?", "(2+2+2+1+2)-(1+2+2+2+0)", "Se restan los totales de C y de A calculados con los puntajes de la ficha.", " puntos"),
   ("=", "{F} ¿Cuántos metros cuadrados hay que cubrir en el muro?", "8*2", "La superficie se calcula multiplicando el largo por el alto del muro.", " m²"),
   ("abc", "{F} Sin alero, el muro queda expuesto a la lluvia. ¿Qué criterio de la pauta se relaciona directamente?", "Que resista el exterior", "La participación de la comunidad", "El propósito y el tema", "La lluvia pone a prueba la resistencia de la pintura y los materiales."),
   ("abc", "{F} Con la pauta, ¿qué postura razonada es más sólida?", "Elegir la idea A, porque suma más puntos y cumple en propósito, legibilidad y factibilidad", "Elegir la B, porque tiene la técnica más detallada", "Elegir la C, porque tiene el texto más corto", "A suma 9 puntos, el total más alto, con buen puntaje en propósito y legibilidad."),
   ("abc", "{F} La idea B obtuvo 1 en «legible a distancia». ¿Qué dato de la ficha lo explica mejor?", "Son doce rostros realistas repartidos en un muro de 8 por 2 metros, con mucho detalle en cada uno", "El muro es de ladrillo pintado de blanco", "Cada persona retratada debe dar su permiso", "Muchos rostros con detalle fino en poco espacio se pierden desde lejos; el ladrillo y el permiso son otros criterios."),
   ("abc", "{F} Una vecina propone combinar A y C: ventanas amarillas con la frase abajo. ¿Qué debe revisar el grupo antes de decidir?", "Si hay espacio, tiempo y materiales para ambas y si la frase sigue legible", "Nada, porque combinar siempre mejora el resultado", "Que sea más difícil para que se vea mejor", "Combinar exige comprobar que el mensaje no se sobrecargue ni exceda los recursos."),
   ("abc", "{F} Evaluar una idea es distinto de elegir la que más gusta. ¿Qué muestra mejor esa diferencia?", "Aplicar los mismos criterios a las tres ideas y comparar los puntajes antes de opinar", "Votar sin explicar el voto", "Elegir la idea de quien propuso primero", "Los criterios comunes permiten explicar y comparar, y no solo preferir.")],
  ("abc", "Una persona describe su boceto: «arriba, nubes celestes; al centro, la frase en letras rojas grandes sobre fondo blanco; abajo, una franja verde con macetas». ¿Qué falta para que sea un boceto bien descrito?", "Indicar desde qué distancia se leerá y cuántos colores se usarán", "Nada, porque todo boceto está completo", "Agregar el precio de cada pincel", "Un boceto útil describe ubicación, colores, texto y distancia de lectura."),
  [("En Artes Visuales: ¿qué es una pauta de evaluación?", "Una tabla de criterios con puntajes para comparar ideas", "Permite comparar todas las ideas con la misma vara."),
   ("¿Qué se puede hacer con una idea que tiene un punto débil?", "Ajustarla sin perder su propósito", "Corregir el punto débil es mejor que descartar sin pensar."),
   ("¿Qué debe incluir un boceto descrito?", "Ubicación, colores, texto y distancia de lectura", "Esos datos permiten probar la idea antes de pintar.")],
  ("{F} Elige la idea que seguirías (A, B, C o una combinación). Escribe tu decisión con dos razones apoyadas en los puntajes y en el lugar, un ajuste que harías y un boceto descrito con palabras: qué va arriba, al centro y abajo, colores (máximo cuatro), texto si lleva y distancia de lectura.",
   "Elijo la idea A. Razones: suma 9 puntos y el pasaje oscuro se ilumina con ventanas amarillas. Ajuste: pedir a vecinos que pinten una ventana cada uno. Boceto: arriba, cielo azul oscuro; al centro, tres filas de ventanas amarillas distintas; abajo, una franja gris. Cuatro colores. Se lee desde 10 metros.",
   ["elige una idea y da dos razones", "usa los puntajes y el lugar", "propone un ajuste", "describe un boceto con ubicación, colores y distancia"],
   ["decisión con razones más un boceto escrito de cuatro o cinco líneas"],
   ["elegir sin usar los puntajes", "describir un boceto sin indicar colores ni distancia"],
   "Comprueba que se mencione al menos un puntaje de la ficha. Si el boceto no dice colores, pide que los nombre. Valora que el ajuste cuide la participación y la factibilidad."),
  "Suma otra vez los puntos de cada idea y ordénalas de mayor a menor.",
  "Escribe una pauta de cinco criterios, de 0 a 2, para evaluar una idea de letrero o cartel para una sede social.")
