"""Historia, Geografía y Ciencias Sociales EPJA Básica N2, módulo 3 (parte 2): OAD-10, caracterizar el espacio geográfico que habitaron los pueblos originarios leyendo mapas, fotografías e imágenes de pantalla. Mapas, fotos y pantallas se describen con palabras y tablas en la ficha; datos de ejemplo."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz, goma y regla. Los mapas, fotografías y pantallas de computador están descritos con palabras y tablas en la ficha de cada clase; no se necesita internet ni calculadora. Todos los datos de lugares inventados están rotulados «de ejemplo»."
build = make_build(MATERIALS)

O = "EPJA-HGCS-NB2-OAD-10"
PRIOR = ["Sé que un mapa dibuja un lugar visto desde arriba.", "Sé distinguir norte, sur, este y oeste.", "Reconozco paisajes como desierto, valle, bosque, lago y mar."]


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    build(O, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ===================================================== clase 1
F = ("Ficha 1 (mapa de ejemplo descrito con palabras; lugar inventado). Título: «Región de ejemplo». Una flecha en la esquina indica que el norte está hacia arriba del mapa. "
     "En el centro está el pueblo Villa Sol. Al norte de Villa Sol hay un río. Al sur hay un bosque. Al este se levanta una cordillera. Al oeste está el mar.")
K(1, F,
  "Hoy me ubico en un mapa de una región usando los puntos cardinales y describo dónde queda cada lugar.",
  ["Para entender dónde vivía un pueblo hay que saber ubicarse en el espacio. Un mapa es un dibujo de un lugar visto desde arriba. Casi todos los mapas tienen una flecha que marca el norte. A partir del norte se ubican los otros puntos cardinales: con el norte arriba, el sur queda abajo, el este a la derecha y el oeste a la izquierda.",
   "Para ubicar un lugar se dice dónde está en relación con otro. Si el río está al norte de Villa Sol, entonces Villa Sol está al sur del río. Esa regla se invierte siempre: si A está al norte de B, B está al sur de A. Tú ya haces esto cuando le explicas a alguien cómo llegar a un consultorio o a una feria.",
   "Chile es un país largo y angosto: el norte tiene desierto, el centro valles, el sur bosques y lluvias, y el extremo sur canales e islas. Los pueblos originarios habitaron espacios muy distintos, y el primer paso para describirlos es saber dónde están en el mapa."],
  [("mapa", "dibujo de un lugar visto desde arriba"), ("puntos cardinales", "norte, sur, este y oeste"), ("ubicación relativa", "decir dónde queda algo en relación con otra cosa"), ("región", "parte de un territorio con rasgos propios")],
  [("Ubicar con el norte", "En la ficha, ¿qué hay al oeste de Villa Sol?", ["Busco la palabra oeste en la ficha.", "Leo qué aparece junto a ella."], "El mar"),
   ("Invertir la ubicación", "El río está al norte de Villa Sol. ¿Dónde está Villa Sol respecto del río?", ["Si A está al norte de B, B está al sur de A.", "Aplico la regla al río y a Villa Sol."], "Villa Sol está al sur del río")],
  [("Creer que el norte siempre está arriba en cualquier dibujo.", "Casi todos los mapas lo ponen arriba, pero el que manda es la flecha del norte.", "Mira primero la flecha antes de ubicar."),
   ("Confundir este con oeste.", "Se intercambian la derecha y la izquierda.", "Recuerda: con el norte arriba, el este queda a la derecha.")],
  [("abc", "{F} ¿Qué hay al sur de Villa Sol?", "un bosque", "una cordillera", "el mar", "La ficha dice que al sur hay un bosque."),
   ("abc", "{F} ¿Qué hay al este de Villa Sol?", "una cordillera", "un río", "el mar", "La ficha ubica la cordillera hacia el este."),
   ("ab", "{F} ¿Hacia dónde apunta la flecha de la esquina?", "hacia el norte", "hacia el mar", "La flecha de un mapa indica el norte, que en la ficha está arriba."),
   ("abc", "{F} ¿Dónde está el bosque respecto de Villa Sol?", "al sur", "al norte", "al oeste", "La ficha dice que el bosque está al sur del pueblo."),
   ("abc", "{F} ¿Dónde está Villa Sol respecto del mar?", "al este del mar", "al oeste del mar", "al norte del mar", "El mar está al oeste de Villa Sol, así que el pueblo queda al este del mar."),
   ("ab", "{F} ¿Dónde está Villa Sol respecto de la cordillera?", "al oeste de la cordillera", "al este de la cordillera", "La cordillera está al este del pueblo, así que el pueblo queda al oeste de ella."),
   ("abc", "Una persona dice: «El río está al sur del pueblo». Según la ficha, ¿es correcto?", "no: el río está al norte de Villa Sol", "sí, es correcto", "no se puede saber", "La ficha dice claramente que el río está al norte de Villa Sol."),
   ("ab", "Un mapa es", "un dibujo de un lugar visto desde arriba", "una fotografía de una persona", "Los mapas representan lugares vistos desde arriba."),
   ("abc", "Si una ciudad está al norte de otra, la otra ciudad está", "al sur", "al este", "al oeste", "Las ubicaciones relativas se invierten: norte con sur."),
   ("ab", "Con el norte arriba del mapa, ¿qué punto cardinal queda en el lado opuesto al este?", "el oeste", "el norte", "El oeste está a la izquierda, en el lado contrario al este, que está a la derecha."),
   ("abc", "Un pueblo originario vivió junto a un río, al este de un mar. ¿Qué dato falta para ubicarlo bien en un mapa?", "el nombre y la zona del mapa donde está", "el color del río", "el tamaño de la hoja", "Con el nombre y la zona se puede ubicar el pueblo en el mapa."),
   ("abc", "{F} Si caminas de Villa Sol hacia el norte, ¿qué encuentras primero?", "el río", "el bosque", "la cordillera", "El río está al norte del pueblo."),
   ("ab", "Chile es un país", "largo y angosto, de norte a sur", "ancho y corto, de este a oeste", "Su forma se extiende mucho de norte a sur y es angosta de este a oeste.")],
  ("abc", "Una persona nueva en el barrio pregunta cómo llegar al consultorio. Tú dices: «Camina hacia el norte hasta el río y luego hacia el oeste». ¿Qué usaste?", "los puntos cardinales", "una fotografía", "una receta", "Orientarse con norte y oeste es usar puntos cardinales."),
  [("¿Cuáles son los puntos cardinales?", "Norte, sur, este y oeste", "Son las cuatro direcciones básicas para ubicarse."),
   ("Si A está al sur de B, ¿dónde está B respecto de A?", "Al norte", "La ubicación relativa se invierte siempre."),
   ("¿Qué indica la flecha de un mapa?", "Dónde está el norte", "Con ella se ubican los demás puntos cardinales.")],
  ("Con la ficha 1, escribe cuatro frases de ubicación completas, una por cada punto cardinal, para Villa Sol (por ejemplo: «Al norte de Villa Sol hay…»). Luego escribe una frase que ubique el río respecto del bosque.",
   "Al norte hay un río. Al sur hay un bosque. Al este hay una cordillera. Al oeste está el mar. El río está al norte del bosque.",
   ["usa los cuatro puntos cardinales", "los datos coinciden con la ficha", "invierte bien la ubicación"],
   ["cinco frases escritas"],
   ["cambiar este por oeste", "inventar lugares que la ficha no tiene"],
   "Pregunta: «¿Esto lo dice la ficha?»."),
  "Dibuja un mapa sencillo de tu cuadra con una flecha del norte y ubica tres lugares.",
  "Escribe cómo explicarías con puntos cardinales el camino de una plaza a una feria que tú elijas.")

# ===================================================== clase 2
F = ("Ficha 2 (mapa físico de ejemplo; lugar inventado). Título: «Valle de ejemplo». Leyenda: triángulo oscuro = montaña; línea azul = río; cuadrado = pueblo; punto verde = bosque. "
     "Escala gráfica: 1 centímetro del mapa = 10 kilómetros de terreno. En el mapa hay dos montañas en el lado este, un río que va de este a oeste, "
     "un pueblo a 4 centímetros del río y un bosque a 6 centímetros del pueblo. Fotografía de ejemplo: muestra un valle con un río estrecho, laderas secas y algunas casas de adobe.")
K(2, F,
  "Hoy aprendo las partes de un mapa y distingo qué muestra un mapa, una fotografía y una imagen en pantalla.",
  ["Un mapa tiene partes que ayudan a leerlo. El título dice qué lugar muestra. La leyenda explica qué significa cada símbolo, es decir, cada dibujo pequeño, como el triángulo de montaña. La escala dice cuánto terreno real representa cada centímetro del mapa. Y la flecha indica el norte. Sin la leyenda, un símbolo puede entenderse mal.",
   "Hay distintas representaciones del espacio. El mapa físico muestra relieve y ríos. La fotografía muestra cómo se ve un lugar en un momento y desde un punto, pero no todo el territorio. La imagen satelital es una foto tomada desde muy alto. Y los mapas en computador o celular permiten acercar, alejar y cambiar de capa, que es mostrar un tipo de información a la vez: calles, relieve o imagen satelital.",
   "Cada representación responde preguntas distintas. El mapa sirve para ubicar y medir; la fotografía, para ver detalles del paisaje; la imagen satelital, para ver el terreno desde arriba. Por eso, para estudiar el espacio de un pueblo originario conviene usar varias a la vez."],
  [("leyenda", "cuadro que explica qué significa cada símbolo del mapa"), ("escala", "relación entre una medida del mapa y la del terreno"), ("capa", "tipo de información que se muestra en un mapa de pantalla"), ("imagen satelital", "foto del terreno tomada desde muy alto")],
  [("Usar la leyenda", "En la ficha, ¿qué representa el símbolo del triángulo oscuro?", ["Busco el triángulo en la leyenda.", "Leo su significado."], "Una montaña"),
   ("Usar la escala", "El pueblo está a 4 cm del río. Con la escala de la ficha, ¿cuántos kilómetros hay?", ["Cada centímetro vale 10 km.", "Multiplico 4 por 10."], "40 kilómetros")],
  [("Interpretar un símbolo sin mirar la leyenda.", "Un mismo dibujo puede significar cosas distintas en mapas distintos.", "Lee siempre la leyenda antes de interpretar."),
   ("Creer que una fotografía muestra todo el territorio.", "Muestra solo un momento y un punto de vista.", "Úsala para detalles y combínala con un mapa.")],
  [("abc", "{F} ¿Qué representa la línea azul?", "un río", "una montaña", "un bosque", "La leyenda dice que la línea azul es un río."),
   ("abc", "{F} ¿Qué representa el punto verde?", "un bosque", "un pueblo", "un río", "La leyenda indica que el punto verde es un bosque."),
   ("ab", "La leyenda de un mapa sirve para", "entender el significado de los símbolos", "saber cuántas personas viven allí", "La leyenda explica los símbolos del mapa."),
   ("=", "{F} Si el bosque estuviera a 8 centímetros del pueblo en el mapa, ¿cuántos kilómetros serían en el terreno?", "8*10", "Cada centímetro vale 10 km; se multiplica 8 por 10.", " km"),
   ("=", "{F} ¿Cuántos centímetros del mapa representan 50 kilómetros de terreno?", "50/10", "Cada centímetro vale 10 km; se divide 50 entre 10.", " cm"),
   ("abc", "{F} ¿Qué dato muestra la fotografía y no muestra el mapa?", "cómo son las casas y el aspecto de las laderas", "la distancia en kilómetros", "la leyenda", "La fotografía entrega detalles visuales como las casas de adobe."),
   ("ab", "{F} ¿Qué dato entrega mejor el mapa que la fotografía?", "la distancia entre el pueblo y el bosque", "el color de las casas", "El mapa tiene escala y permite medir distancias; la foto no."),
   ("abc", "Una imagen satelital muestra", "el terreno visto desde muy alto", "solo el interior de una casa", "una lista de nombres", "Es una foto tomada desde muy alto que muestra el terreno."),
   ("abc", "{F} ¿Cuántas montañas hay en el lado este del mapa?", "dos", "una", "tres", "La ficha indica dos montañas en el lado este."),
   ("ab", "Una capa de un mapa de pantalla es", "un tipo de información que se muestra o se oculta", "una hoja de papel pegada", "En pantalla se puede mostrar solo calles, relieve o imagen satelital."),
   ("abc", "Una persona ve el símbolo de un triángulo en otro mapa y supone que es una montaña. ¿Qué debió hacer?", "mirar la leyenda de ese mapa", "preguntar el color de la hoja", "ignorar el símbolo", "Cada mapa tiene su propia leyenda y puede usar símbolos distintos."),
   ("abc", "{F} ¿Qué dice el título del mapa?", "Valle de ejemplo", "Región de ejemplo", "Mapa del mar", "La ficha dice que el título del mapa es «Valle de ejemplo»."),
   ("ab", "Para estudiar el espacio de un pueblo originario conviene", "usar varias representaciones: mapa, foto e imagen satelital", "usar solo una fotografía", "Cada representación aporta algo distinto y juntas dan una imagen más completa.")],
  ("abc", "En la municipalidad, una persona quiere saber qué tan lejos queda un lago de su poblado y ve un mapa con escala de 1 cm = 10 km. Mide 3 cm. ¿Qué distancia real es?", "30 km", "13 km", "3 km", "Se multiplican los 3 cm por los 10 km de cada centímetro."),
  [("En Geografía: ¿qué es la leyenda de un mapa?", "El cuadro que explica sus símbolos", "Sin la leyenda se pueden interpretar mal los símbolos."),
   ("En un mapa, ¿para qué se usa la escala?", "Para calcular distancias reales", "Relaciona la medida del mapa con la del terreno."),
   ("¿Qué muestra una fotografía de un paisaje?", "Cómo se ve ese lugar desde un punto y en un momento", "No muestra todo el territorio, solo una parte del lugar.")],
  ("Con la ficha 2, responde: (1) qué símbolo usarías para dibujar un bosque; (2) qué distancia real hay entre el pueblo y el bosque; (3) qué información da la fotografía que no da el mapa.",
   "1) Un punto verde. 2) 60 km. 3) Cómo son las casas y las laderas.",
   ["lee la leyenda", "calcula con la escala", "distingue lo que da la foto"],
   ["tres respuestas escritas"],
   ["no usar la escala", "decir que la foto muestra la distancia"],
   "Pregunta: «¿De qué parte del mapa sacaste este dato?»."),
  "Dibuja una leyenda con tres símbolos para un mapa de tu barrio.",
  "Escribe una pregunta que solo un mapa pueda responder y otra que solo una fotografía pueda responder.")

# ===================================================== clase 3
F = ("Ficha 3 (investigación de ejemplo; datos de ejemplo). Pregunta de investigación: «¿Cómo es el espacio donde vivieron los pueblos del desierto del norte?». "
     "Mapa de ejemplo: muestra una franja muy seca entre la cordillera, al este, y el mar, al oeste; hay dos oasis marcados con símbolo verde. "
     "Fotografía de ejemplo: arena y roca sin árboles; en un rincón, un grupo de árboles verdes junto a un canal de agua. "
     "Imagen satelital de ejemplo: terreno de color café con una mancha verde pequeña y angosta.")
K(3, F,
  "Hoy sigo los pasos de una investigación sencilla: formulo una pregunta, junto datos de varias representaciones y saco una conclusión.",
  ["Investigar es buscar respuestas ordenadamente. Primero se formula una pregunta clara, por ejemplo: «¿cómo es el espacio donde vivieron los pueblos del desierto del norte?». Segundo, se eligen representaciones: un mapa, una fotografía y una imagen satelital. Tercero, se leen y se anotan los datos en una tabla: relieve (la forma del terreno), clima, agua y recursos. Cuarto, se escribe una conclusión.",
   "En el desierto del norte hay muy poca agua. Por eso los lugares con agua, llamados oasis, son muy importantes: allí se concentran plantas, cultivos y personas. Los pueblos del norte aprendieron a cuidar el agua con canales y a vivir en esos espacios. Una conclusión debe apoyarse en los datos de la tabla, no en suposiciones.",
   "Cada representación aporta algo y tiene un límite. La fotografía muestra un lugar concreto; el mapa, muchos lugares a la vez; la imagen satelital, el terreno entero desde arriba. Cuando dos representaciones coinciden, la conclusión es más segura."],
  [("investigar", "buscar información de manera ordenada para responder una pregunta"), ("oasis", "lugar con agua en medio del desierto"), ("relieve", "la forma del terreno: montañas, valles, llanos"), ("conclusión", "respuesta final apoyada en los datos")],
  [("Leer una imagen satelital", "En la imagen satelital de la ficha, ¿qué indica la mancha verde?", ["Los colores muestran el terreno.", "El verde suele indicar plantas, y en el desierto, agua cerca."], "Una zona con plantas, probablemente un oasis"),
   ("Sacar una conclusión", "Con los datos de la ficha, ¿por qué hay árboles junto al canal?", ["La foto muestra un canal de agua.", "Donde hay agua hay plantas."], "Porque allí hay agua disponible")],
  [("Sacar conclusiones antes de reunir datos.", "Sin datos, la conclusión es una opinión.", "Primero llena la tabla; después concluye."),
   ("Confundir lo que se ve con lo que se supone.", "La imagen no dice cuánta gente vivía allí.", "Escribe «se ve» y «se supone» en columnas distintas.")],
  [("abc", "{F} ¿Cuál es la pregunta de investigación?", "¿Cómo es el espacio donde vivieron los pueblos del desierto del norte?", "¿Cuántos kilómetros mide Chile?", "¿Cómo se prepara una sopa?", "La ficha la formula al comienzo."),
   ("ab", "{F} En el mapa, ¿qué hay entre la cordillera y el mar?", "una franja muy seca con dos oasis", "un lago enorme", "La descripción del mapa muestra una franja seca con dos símbolos de oasis."),
   ("abc", "{F} Según la fotografía, ¿qué hay en el rincón?", "árboles verdes junto a un canal de agua", "nieve", "una playa", "La fotografía muestra un grupo de árboles junto a un canal."),
   ("abc", "{F} ¿Qué color tiene la mayor parte del terreno en la imagen satelital?", "café", "azul", "blanco", "La descripción dice que el terreno es de color café con una mancha verde pequeña."),
   ("ab", "Un oasis es", "un lugar con agua en medio del desierto", "una montaña con nieve", "Un oasis tiene agua y por eso crecen plantas."),
   ("abc", "{F} ¿Qué dato de la tabla de investigación corresponde a «agua»?", "el canal y los oasis", "la arena de la foto", "el título del mapa", "El canal y los oasis son las fuentes de agua descritas."),
   ("abc", "{F} ¿Qué se anota en la columna «relieve»?", "cordillera al este y franja seca hacia el mar", "el nombre del investigador", "el precio de los pasajes", "El relieve habla de la forma del terreno, como la cordillera."),
   ("ab", "Una investigadora escribe la conclusión antes de mirar el mapa. Su error es", "concluir sin datos", "usar lápiz", "Una conclusión sin datos es solo una opinión."),
   ("abc", "{F} ¿Qué conclusión se apoya mejor en los datos de la ficha?", "los oasis eran lugares importantes porque tenían agua", "el desierto era un lugar con mucha lluvia", "el desierto no tenía ningún lugar con plantas", "La ficha muestra agua y vegetación solo en los oasis."),
   ("ab", "{F} Una persona dice que la fotografía prueba que todo el desierto tiene un canal. Eso es", "una exageración: la foto muestra solo un lugar", "correcto", "Una foto muestra un lugar concreto, no todo el desierto."),
   ("abc", "¿Cuál es el primer paso de una investigación?", "formular una pregunta clara", "escribir la conclusión", "borrar los datos", "Sin pregunta no se sabe qué buscar."),
   ("abc", "{F} ¿Qué representación muestra mejor el terreno entero desde arriba?", "la imagen satelital", "la fotografía", "el título", "La imagen satelital se toma desde muy alto y muestra toda la zona."),
   ("ab", "Cuando el mapa y la imagen satelital coinciden en mostrar un oasis, la conclusión es", "más segura", "menos segura", "Dos fuentes que coinciden dan más seguridad.")],
  ("abc", "Una organización vecinal quiere saber por qué ciertos pueblos del norte vivían cerca de los oasis. ¿Qué datos usaría primero?", "mapa, fotografía e imagen satelital del lugar", "solo el nombre del oasis", "ningún dato", "Combinar representaciones ayuda a concluir con evidencia."),
  [("En Geografía de pueblos: ¿qué es el relieve de una zona?", "La forma del terreno", "Incluye montañas, valles y llanos de un lugar."),
   ("En un desierto, ¿qué es un oasis?", "Un lugar con agua en medio del desierto", "En él se concentran plantas y personas."),
   ("¿En qué se apoya una conclusión?", "En los datos reunidos", "Sin datos reunidos solo hay una opinión.")],
  ("Con la ficha 3, llena una tabla de cuatro filas (relieve, clima, agua, recursos) con la información que entregan las tres representaciones y escribe una conclusión de una frase.",
   "Relieve: cordillera al este y franja seca. Clima: muy seco. Agua: canal y oasis. Recursos: plantas junto al agua. Conclusión: el agua de los oasis permitía vivir en el desierto.",
   ["cuatro filas completas", "datos de la ficha", "conclusión apoyada en datos"],
   ["tabla de cuatro filas y una conclusión"],
   ["escribir datos que la ficha no entrega", "concluir sin mirar la tabla"],
   "Pregunta: «¿Qué dato apoya tu conclusión?»."),
  "Anota una pregunta de investigación sobre el espacio donde vive hoy un pueblo originario de tu región.",
  "Explica por qué conviene mirar un mapa y una imagen satelital a la vez.")

# ===================================================== clase 4
F = ("Ficha 4 (tabla de ejemplo; resumen general). Zona del país | Paisaje | Pueblos asociados. "
     "Norte | desierto, salares, oasis y altiplano | aymara y atacameño. "
     "Norte chico | valles que bajan de la cordillera al mar | diaguita. "
     "Centro y sur | valles, bosques, lagos y costa | mapuche. "
     "Extremo sur | canales, islas, viento y frío | kawésqar, yagán y selk'nam. "
     "Isla en el océano Pacífico | isla volcánica | rapanui.")
K(4, F,
  "Hoy practico con apoyo cómo relacionar zonas del país con sus paisajes y con los pueblos que las habitaron.",
  ["Chile tiene paisajes muy distintos de norte a sur. En el norte hay desierto y altiplano; en el norte chico, valles que bajan de la cordillera al mar; en el centro y sur, valles, bosques, lagos y costa; y en el extremo sur, canales e islas con viento y frío. La Isla de Pascua, en el océano Pacífico, es un territorio aparte, de origen volcánico.",
   "El paisaje condiciona los recursos disponibles. En el desierto el recurso más importante es el agua. En los valles hay suelos para cultivar. En los bosques hay madera y plantas. En el mar y los canales hay peces, mariscos y lobos marinos. Cada pueblo aprendió a aprovechar los recursos de su zona y a cuidarlos para que siguieran estando.",
   "Al leer una tabla como la de la ficha, ve primero la zona, luego el paisaje y luego el pueblo. Recuerda que la tabla es un resumen: en una misma zona pudo haber varios pueblos, y hoy muchas personas de pueblos originarios viven fuera de la zona de origen, por ejemplo en ciudades."],
  [("paisaje", "lo que se ve de un lugar: relieve, plantas, agua y construcciones"), ("altiplano", "meseta alta y fría de la cordillera en el norte"), ("canal", "paso angosto de agua entre islas o tierra firme"), ("salar", "terreno cubierto de sal, donde hubo un lago salado")],
  [("Leer la tabla", "Con la tabla de la ficha, ¿qué paisaje se asocia al pueblo diaguita?", ["Busco la fila donde aparece diaguita.", "Leo la columna Paisaje."], "Valles que bajan de la cordillera al mar"),
   ("Recurso y paisaje", "En una zona de canales e islas, ¿qué recurso es el más probable?", ["Hay mucha agua de mar.", "Entonces los peces y mariscos son abundantes."], "Los recursos del mar, como mariscos y peces")],
  [("Pensar que cada zona tuvo un solo pueblo.", "La tabla resume; en una zona pudo haber varios pueblos.", "Lee «pueblos asociados», no «únicos pueblos»."),
   ("Creer que los pueblos solo viven en la zona de la tabla.", "Hoy muchas personas viven en ciudades y en otras regiones.", "Usa la tabla como origen, no como límite.")],
  [("abc", "{F} ¿Qué paisaje corresponde a la zona del norte?", "desierto, salares, oasis y altiplano", "canales e islas", "bosques y lagos", "La fila del norte lo nombra así."),
   ("abc", "{F} ¿Qué pueblos se asocian al extremo sur?", "kawésqar, yagán y selk'nam", "aymara y atacameño", "diaguita", "La fila del extremo sur nombra a esos tres pueblos."),
   ("ab", "{F} ¿Qué pueblo se asocia a la isla en el océano Pacífico?", "rapanui", "mapuche", "La última fila lo asocia a la isla volcánica del Pacífico."),
   ("abc", "{F} ¿Qué paisaje se asocia a la zona centro y sur?", "valles, bosques, lagos y costa", "desierto y oasis", "canales y viento", "La tabla da esos elementos para el centro y sur."),
   ("abc", "En el desierto, ¿cuál es el recurso más importante?", "el agua", "la madera", "los peces", "En un lugar muy seco el agua es lo más escaso y valioso."),
   ("ab", "{F} Los valles del norte chico bajan", "de la cordillera al mar", "del mar a la cordillera", "La tabla dice que bajan de la cordillera al mar."),
   ("abc", "{F} Una persona dice que los mapuche vivían en el extremo sur de canales. Según la tabla, ¿está bien?", "no: la tabla los asocia al centro y sur", "sí, está bien", "la tabla no dice nada", "La tabla ubica a los mapuche en el centro y sur, no en los canales."),
   ("abc", "{F} ¿Qué paisaje condiciona que los kawésqar usaran canoas?", "canales e islas", "desierto", "altiplano", "En un paisaje de canales, la canoa es una forma natural de moverse."),
   ("ab", "En el centro y sur, los bosques ofrecen", "madera y plantas", "salares", "Un bosque entrega madera y plantas útiles."),
   ("abc", "{F} ¿Qué paisaje se asocia al pueblo aymara en la tabla?", "altiplano y desierto, en el norte", "canales del extremo sur", "isla volcánica", "El altiplano está en la fila del norte, donde aparece el pueblo aymara."),
   ("ab", "Si hoy una persona de un pueblo originario vive en una ciudad, la tabla", "sigue mostrando el origen, no un límite", "pierde toda validez", "La tabla resume los espacios de origen; las personas hoy viven en muchos lugares."),
   ("abc", "{F} ¿Qué dos pueblos se asocian a la zona norte en la tabla?", "aymara y atacameño", "diaguita y mapuche", "yagán y rapanui", "La fila del norte nombra a los pueblos aymara y atacameño."),
   ("ab", "{F} En la tabla, la zona del extremo sur se describe con", "viento y frío", "calor y arena", "La fila del extremo sur menciona canales, islas, viento y frío.")],
  ("abc", "Una escuela de adultos organiza una exposición con cuatro paisajes de Chile. Cada afiche irá con un pueblo. ¿Cuál emparejamiento es correcto según la tabla?", "canales e islas con kawésqar", "desierto con yagán", "altiplano con selk'nam", "El emparejamiento correcto es el que aparece en la tabla."),
  [("En Geografía: ¿qué es un paisaje?", "Lo que se ve de un lugar", "Incluye relieve, plantas, agua y construcciones."),
   ("¿Qué recurso abunda en una zona de canales?", "Los recursos del mar", "En el mar hay peces, mariscos y lobos marinos."),
   ("¿Por qué la tabla es solo un resumen?", "Porque en una zona hubo varios pueblos y hoy las personas viven en muchos lugares", "La tabla es un resumen y no marca un límite exacto.")],
  ("Con la tabla de la ficha 4, elige dos zonas y escribe, para cada una, el paisaje, el pueblo asociado y un recurso natural probable. Termina con una frase que advierta que la tabla es un resumen.",
   "Norte: desierto y altiplano; aymara y atacameño; agua de los oasis. Extremo sur: canales e islas; kawésqar; mariscos. La tabla es un resumen.",
   ["usa la tabla", "relaciona paisaje y recursos", "incluye la advertencia"],
   ["dos filas escritas y una frase final"],
   ["inventar pueblos que la tabla no tiene", "olvidar la advertencia"],
   "Pregunta: «¿La tabla dice eso o lo supuse?»."),
  "Elige una zona de la tabla y dibuja su paisaje con tres elementos.",
  "Escribe por qué el mismo paisaje no tiene los mismos recursos que otro.")

# ===================================================== clase 5
F = ("Ficha 5 (pantalla de ejemplo de un mapa en línea; lugar inventado). Botones: «+» acerca; «−» aleja. Menú «Capas»: calles, relieve, satélite. "
     "Barra de escala en la esquina: 1 centímetro de pantalla = 10 kilómetros. El punto rojo marca «Sitio de ejemplo». "
     "Con la capa «relieve» se ve una cordillera al este y una llanura al oeste; con la capa «satélite» se ve una franja verde angosta junto a un río entre dos tonos de café. "
     "La distancia en pantalla entre el sitio de ejemplo y el río mide 3 centímetros.")
K(5, F,
  "Hoy uso un mapa en pantalla y sus capas para describir el espacio donde se ubicaba un sitio de un pueblo originario.",
  ["Un mapa en línea es una representación computacional del espacio. Se puede acercar con el botón «+», alejar con «−» y cambiar de capa. La capa de calles muestra caminos y nombres; la capa de relieve muestra montañas y valles; la capa satélite muestra el terreno visto desde arriba. Cada capa responde una pregunta distinta.",
   "Para describir el espacio de un sitio, combina capas. Con relieve ves si hay cordillera o llanura. Con satélite ves dónde hay verde, que suele indicar plantas y agua. Con la escala puedes calcular distancias: si 1 centímetro vale 10 kilómetros, 3 centímetros valen 30. Anota siempre la capa que usaste, para que otra persona repita tu trabajo.",
   "Un mapa en línea no entrega todo: no dice cuánta gente vivió allí ni qué cosmovisión tenía. Eso se averigua en otras fuentes. Y si el sitio tiene un significado sagrado para una comunidad, hay que consultar a esa comunidad antes de hablar de él o de visitarlo."],
  [("mapa en línea", "mapa que se ve y se maneja en una pantalla"), ("zoom", "acercar o alejar la imagen"), ("capa satélite", "vista del terreno tomada desde muy alto"), ("sitio", "lugar donde hay huellas o recuerdos de la vida de un pueblo")],
  [("Elegir la capa", "Quiero saber si el sitio está junto a una cordillera. ¿Qué capa uso?", ["La forma del terreno se ve en relieve.", "La capa de calles no la muestra."], "La capa de relieve"),
   ("Calcular la distancia", "La barra dice 1 cm = 10 km. El sitio está a 3 cm del río. ¿Cuántos kilómetros son?", ["Multiplico 3 por 10.", "Anoto la unidad: kilómetros."], "30 kilómetros")],
  [("Usar solo la capa de calles para estudiar un paisaje.", "Las calles no muestran el relieve ni el verde.", "Elige la capa según la pregunta."),
   ("Calcular una distancia con la barra pero sin mirar su valor.", "Cada mapa tiene su propia escala.", "Lee primero cuántos kilómetros vale cada centímetro.")],
  [("abc", "{F} ¿Qué botón usarías para ver más de cerca el sitio?", "el botón «+»", "el botón «−»", "el menú de capas", "El botón «+» acerca la imagen."),
   ("abc", "{F} ¿Qué capa muestra el terreno visto desde arriba?", "satélite", "calles", "relieve", "La ficha dice que la capa satélite lo muestra."),
   ("ab", "{F} ¿Qué capas ofrece el menú «Capas»?", "calles, relieve y satélite", "solo calles y relieve", "El menú de la ficha lista tres capas: calles, relieve y satélite."),
   ("=", "{F} Con la misma barra de escala, ¿cuántos kilómetros representan 5 centímetros de pantalla?", "5*10", "Cada centímetro vale 10 km, así que se multiplica por 5.", " km"),
   ("abc", "{F} Con la capa relieve, ¿qué hay al oeste del sitio?", "una llanura", "una cordillera", "el mar", "La ficha dice que al oeste hay una llanura."),
   ("ab", "{F} La franja verde de la capa satélite junto al río suele indicar", "plantas y agua", "nieve", "El verde angosto junto a un río suele señalar vegetación y agua."),
   ("abc", "{F} ¿Qué botón sirve para ver una zona más grande?", "«−»", "«+»", "el punto rojo", "El botón «−» aleja la imagen y muestra más territorio."),
   ("abc", "Una persona quiere ver nombres de calles. ¿Qué capa usa?", "calles", "relieve", "satélite", "La capa de calles muestra caminos y nombres."),
   ("ab", "Un mapa en pantalla no te dice", "qué cosmovisión tenía el pueblo del sitio", "si hay un río cerca", "La cosmovisión se averigua en otras fuentes; el mapa solo muestra el espacio."),
   ("abc", "{F} ¿Qué se debe anotar siempre al describir un sitio con un mapa en línea?", "la capa usada", "el color del punto", "la hora del día", "Anotar la capa permite que otra persona repita el trabajo."),
   ("abc", "{F} ¿Cuántos kilómetros vale cada centímetro en la barra de escala?", "10", "100", "1", "La ficha dice que 1 centímetro de pantalla equivale a 10 kilómetros."),
   ("ab", "Si un sitio tiene significado sagrado para una comunidad, lo correcto es", "consultar a la comunidad antes de hablar de él", "publicar su ubicación exacta sin preguntar", "El respeto exige consultar a quienes lo consideran sagrado."),
   ("abc", "{F} ¿Cuál es el nombre del punto rojo?", "Sitio de ejemplo", "Villa Sol", "Valle de ejemplo", "La ficha dice que el punto rojo marca el Sitio de ejemplo.")],
  ("abc", "Un grupo de vecinos prepara una charla sobre un valle cercano y usa un mapa en línea. Quieren mostrar qué tan lejos queda el río. ¿Qué herramienta del mapa usan?", "la barra de escala", "el título", "la capa de calles", "La escala permite calcular distancias reales."),
  [("En Geografía: ¿qué es una capa de un mapa en línea?", "Un tipo de información que se muestra", "Por ejemplo, relieve, calles o satélite."),
   ("¿Qué capa muestra el relieve?", "La capa de relieve", "Muestra las montañas y las llanuras de la zona."),
   ("¿Qué hay que hacer antes de hablar de un lugar sagrado?", "Consultar a la comunidad", "Es una muestra de respeto a quienes lo cuidan.")],
  ("Con la pantalla de la ficha 5, escribe una descripción de cuatro líneas del Sitio de ejemplo: qué se ve con relieve, qué se ve con satélite, a qué distancia está del río y qué capa usaste en cada caso.",
   "Con relieve se ve una cordillera al este y una llanura al oeste. Con satélite se ve una franja verde junto al río. El río está a 30 km. Usé las capas relieve y satélite.",
   ["usa dos capas", "calcula bien la distancia", "nombra la capa en cada dato"],
   ["una descripción de cuatro líneas"],
   ["no nombrar la capa", "calcular mal la distancia"],
   "Pregunta: «¿Qué capa te mostró este dato?»."),
  "Anota tres preguntas que un mapa en línea puede responder sobre tu zona y qué capa usarías para cada una.",
  "Explica por qué conviene decir qué capa usaste.")

# ===================================================== clase 6
F = ("Ficha 6 (informe de ejemplo con errores). «Investigué el espacio de un pueblo del norte. En la fotografía no se ve a nadie, entonces nadie vivía allí. "
     "El mapa tiene un triángulo, así que seguro es un volcán. Mi mapa en línea no tenía escala, pero calculé la distancia igual: unos 100 kilómetros». "
     "Pauta de revisión: 1) La conclusión se apoya en datos. 2) Leí la leyenda. 3) Usé la escala. 4) Combiné al menos dos representaciones. 5) Cité las fuentes.")
K(6, F,
  "Hoy reviso una investigación sobre el espacio de un pueblo originario con una pauta, corrijo errores y decido qué quiero repasar.",
  ["Revisar una investigación es comprobar que cada afirmación tiene respaldo. La pauta de la ficha propone cinco preguntas: ¿la conclusión se apoya en datos?, ¿leí la leyenda?, ¿usé la escala?, ¿combiné al menos dos representaciones?, ¿cité las fuentes? Si una respuesta es no, hay que corregir antes de entregar el trabajo.",
   "Hay errores frecuentes. Deducir una cosa a partir de una foto que no la muestra: una fotografía es un instante, y si no se ve gente no significa que nadie viviera allí. Interpretar un símbolo sin leyenda. Calcular distancias sin escala. Y generalizar: lo que sirve para un paisaje del norte no explica el sur.",
   "Cuando encuentras un error, no es un fracaso: es parte del trabajo de investigar. Se corrige con los datos, se anota lo que falta y se vuelve a revisar. Si aún no puedes responder algo con las representaciones que tienes, escribe «no lo puedo afirmar» y propone dónde buscar."],
  [("pauta de revisión", "lista de preguntas para comprobar un trabajo"), ("respaldo", "dato o fuente que sostiene una afirmación"), ("deducir", "sacar una conclusión a partir de datos"), ("afirmar", "decir que algo es cierto")],
  [("Detectar un error de deducción", "Frase de la ficha: «En la fotografía no se ve a nadie, entonces nadie vivía allí». ¿Qué error hay?", ["La fotografía muestra un instante y un punto de vista.", "No muestra todo el lugar ni toda la historia."], "Deduce algo que la foto no puede probar"),
   ("Aplicar la pauta", "Una persona calculó una distancia sin escala. ¿Qué pregunta de la pauta no cumplió?", ["Busco en la pauta la que habla de la escala.", "Es la pregunta 3."], "La 3: usar la escala")],
  [("Confiar en un cálculo sin escala.", "Sin escala no hay relación entre el mapa y el terreno.", "Busca la escala o di «no puedo calcularlo»."),
   ("Revisar solo la ortografía.", "Revisar es comprobar datos, fuentes y conclusiones.", "Usa la pauta de cinco preguntas.")],
  [("abc", "{F} ¿Qué pregunta de la pauta falla en «el triángulo es seguro un volcán»?", "la 2: leer la leyenda", "la 5: citar fuentes", "la 1: nada", "Interpretó un símbolo sin leer la leyenda."),
   ("ab", "{F} ¿Qué pregunta de la pauta falla al deducir «nadie vivía allí» solo de la foto?", "la 1: la conclusión se apoya en datos", "la 3: usar la escala", "Una foto sin personas no es un dato que pruebe que nadie vivió allí."),
   ("abc", "{F} ¿Cuántas preguntas tiene la pauta de revisión?", "cinco", "tres", "diez", "La ficha lista cinco preguntas para revisar el trabajo."),
   ("abc", "{F} ¿Qué pregunta de la pauta cumple quien usa un mapa y una imagen satelital para sacar su conclusión?", "la 4: combinar al menos dos representaciones", "la 2: leer la leyenda", "la 5: citar las fuentes", "Usar dos representaciones distintas es justo lo que pide la pregunta 4."),
   ("ab", "Si no tienes escala, lo más honesto es decir", "no puedo calcular esa distancia", "calculo la distancia a ojo y no aviso", "Reconocer el límite es parte de la honestidad al investigar."),
   ("abc", "{F} Para corregir el primer error de la ficha, ¿qué frase es mejor?", "la foto muestra un lugar sin personas en ese momento, pero no prueba que nadie viviera allí", "en la foto vivían cien personas", "las fotos nunca sirven", "La corrección mantiene lo que se ve sin sacar una conclusión indebida."),
   ("ab", "Combinar al menos dos representaciones sirve para", "contrastar datos y reducir errores", "gastar más tiempo", "Si dos representaciones coinciden, la conclusión es más segura."),
   ("abc", "Una conclusión sobre el espacio de un pueblo debe apoyarse en", "datos de mapas y fotografías", "suposiciones sin fuente", "la opinión de nadie", "Las conclusiones requieren respaldo en datos."),
   ("abc", "¿Qué se hace con una pregunta que las representaciones no pueden responder?", "se anota como pendiente y se busca otra fuente", "se responde inventando", "se borra", "Anotar lo que falta es parte de investigar bien."),
   ("ab", "{F} La pregunta 5 de la pauta pide", "citar las fuentes", "dibujar un mapa", "Citar permite que otros comprueben el trabajo."),
   ("abc", "En una jornada comunitaria alguien muestra una investigación sin citar fuentes. ¿Qué es lo más respetuoso?", "pedir con amabilidad que indique de dónde sacó los datos", "burlarse de su trabajo", "aceptar todo sin preguntar", "Preguntar con respeto invita a mejorar el trabajo."),
   ("abc", "{F} ¿Qué parte de la ficha 6 es un buen ejemplo de afirmación sin respaldo?", "«seguro es un volcán»", "«investigué un pueblo del norte»", "«mi mapa en línea no tenía escala»", "«Seguro es un volcán» no se apoya en la leyenda."),
   ("ab", "Revisar un trabajo propio es", "una forma de mejorar lo que se aprende", "una señal de que se equivocó mucho", "Revisar es una parte normal y valiosa de aprender.")],
  ("abc", "Un compañero entrega una investigación con la pauta de revisión en blanco. ¿Qué le sugieres?", "responder las cinco preguntas antes de entregar", "entregar igual", "borrar los datos", "Aplicar la pauta evita errores antes de entregar."),
  [("En Geografía: ¿para qué sirve una pauta de revisión?", "Para comprobar si el trabajo cumple lo necesario", "Cada pregunta señala un punto a revisar."),
   ("¿Por qué una fotografía no prueba que nadie vivía allí?", "Porque muestra solo un instante y un punto de vista", "No muestra toda la historia del lugar."),
   ("¿Qué se hace si no hay escala?", "Se dice que no se puede calcular la distancia", "Sin escala no hay relación con el terreno.")],
  ("Reescribe en tres frases correctas los tres errores de la ficha 6 (la foto sin gente, el triángulo y la distancia sin escala) y escribe una frase final con lo que quieres repasar de la unidad.",
   "La foto muestra un instante, no prueba que nadie viviera allí. Hay que leer la leyenda antes de decir qué significa el triángulo. Sin escala no puedo calcular distancias. Quiero repasar la escala.",
   ["corrige los tres errores", "usa ideas de la unidad", "dice qué quiere repasar"],
   ["cuatro frases escritas"],
   ["repetir el error", "no mencionar la leyenda ni la escala"],
   "Pregunta: «¿Qué dato respalda tu corrección?»."),
  "Escribe tus tres preguntas de revisión favoritas para un trabajo sobre mapas.",
  "Explica con un ejemplo por qué una sola representación no basta para estudiar un espacio.")
