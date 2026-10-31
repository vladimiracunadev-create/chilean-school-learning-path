"""Material del estudiante de 6.º básico, Historia, Geografía y Ciencias Sociales: OA 10 (elementos constitutivos del territorio nacional y carácter tricontinental)."""
from __future__ import annotations

from hi5_lib import build

OA10 = "HI06 OA 10"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 42 (localización de Chile, hecha para este cuaderno; datos generales). "
     "Chile está en el hemisferio sur y en el hemisferio occidental, en el extremo suroeste de América del Sur. "
     "Su territorio continental se extiende desde cerca de los 17° de latitud sur, en el norte, hasta cerca de los 56° de latitud sur, en el extremo sur. "
     "Limita al norte con Perú, al noreste con Bolivia, al este con Argentina y al oeste con el océano Pacífico. "
     "Chile es tricontinental: tiene territorio en América (Chile continental), en Oceanía (la Isla de Pascua o Rapa Nui, en la Polinesia) y en la Antártica (Territorio Chileno Antártico, entre los meridianos 53° y 90° de longitud oeste).")
build(
    OA10, 1, F,
    use="Aprenderé a ubicar a Chile en el mundo usando hemisferios, latitud, límites y su carácter tricontinental. Sirve para describir dónde está Chile y qué territorios lo forman.",
    prior=["Sé que la Tierra tiene un hemisferio norte y uno sur.", "Sé reconocer países vecinos en un mapa.", "Sé que la latitud mide la distancia al ecuador."],
    explain=[
        "La localización es el lugar donde algo se encuentra. Podemos ubicar a Chile de dos maneras. La localización absoluta usa coordenadas: latitud, que indica qué tan al norte o al sur está un lugar respecto del ecuador, y longitud, que indica qué tan al este o al oeste está respecto de un meridiano de referencia. La localización relativa lo ubica respecto de otros lugares, como países vecinos y océanos.",
        "Chile está en el hemisferio sur y occidental. Su territorio continental va desde cerca de los 17° de latitud sur hasta cerca de los 56° sur. Limita al norte con Perú, al noreste con Bolivia, al este con Argentina y al oeste con el océano Pacífico. Por eso es un país muy largo y angosto.",
        "Además, Chile es un país tricontinental: tiene territorio en tres continentes. En América está Chile continental, en Oceanía está la Isla de Pascua o Rapa Nui, y en la Antártica está el Territorio Chileno Antártico. Esta característica se llama carácter tricontinental y es un rasgo muy particular de nuestro país.",
    ],
    vocab=[("localización", "lugar donde algo se encuentra"), ("latitud", "distancia de un lugar al ecuador, medida en grados hacia el norte o el sur"), ("longitud", "distancia de un lugar a un meridiano de referencia, medida hacia el este o el oeste"), ("límite", "línea que separa dos territorios"), ("tricontinental", "con territorio en tres continentes")],
    worked=[
        ("Localización relativa", "{F} ¿Con qué país limita Chile al este?", ["Reviso los límites en la ficha.", "Al este limita con Argentina."], "Con Argentina"),
        ("Carácter tricontinental", "{F} ¿En qué continente está la Isla de Pascua?", ["La ficha dice que está en Oceanía.", "Forma parte de la Polinesia."], "En Oceanía"),
    ],
    mistakes=[("Creer que Chile está solo en América.", "Se olvidan las islas y la Antártica.", "Chile es tricontinental: América, Oceanía y Antártica."),
              ("Confundir latitud con longitud.", "Se mezclan las medidas.", "La latitud mide hacia el norte o el sur; la longitud, hacia el este o el oeste.")],
    T=[
        ("{F} ¿En qué hemisferios está Chile?", "en el hemisferio sur y en el occidental", "La ficha lo indica."),
        ("{F} ¿Con qué océano limita Chile al oeste?", "con el océano Pacífico", "La ficha lo dice."),
        ("{F} ¿Con qué país limita Chile al norte?", "con Perú", "La ficha lo indica."),
        ("{F} ¿Con qué país limita Chile al noreste?", "con Bolivia", "La ficha lo indica."),
        ("{F} ¿Qué mide la latitud?", "la distancia de un lugar al ecuador, hacia el norte o el sur", "La explicación la define."),
        ("{F} ¿Qué territorio de Chile está en la Polinesia?", "la Isla de Pascua o Rapa Nui", "La ficha lo dice."),
        ("=", "{F} Entre los 17° y los 56° de latitud sur, ¿cuántos grados de latitud abarca el territorio continental de Chile?", "56-17", "Se resta la latitud menor a la mayor.", " grados"),
        ("{F} Clasifica como localización absoluta (A) o relativa (R): a) 17° latitud sur; b) limita con Argentina; c) 56° latitud sur; d) limita con el Pacífico.", "a: A; b: R; c: A; d: R", "Las coordenadas son absolutas; los vecinos son relativos."),
        ("{F} ¿Cuáles son los tres continentes donde Chile tiene territorio?", "América, Oceanía y Antártica", "La ficha lo indica."),
        ("{F} Un compañero dice: «Chile está en el hemisferio norte». Corrígelo.", "No: está en el hemisferio sur", "La ficha lo indica."),
        ("{F} Una alumna dice: «Chile limita al oeste con Argentina». ¿Qué error comete?", "al oeste limita con el océano Pacífico; Argentina está al este", "La ficha lo indica."),
        ("{F} ¿Por qué Chile es un país largo y angosto?", "porque se extiende de norte a sur más de lo que se extiende de este a oeste", "La latitud abarca mucha distancia y limita con la cordillera y el mar."),
        ("{F} ¿Entre qué meridianos está el Territorio Chileno Antártico?", "entre los 53° y los 90° de longitud oeste", "La ficha lo dice."),
    ],
    ctx=("Un compañero describe a Chile con tres frases. Cuál es correcta: A) Está en el hemisferio sur, limita con Perú, Bolivia y Argentina. B) Está en el hemisferio norte y no tiene vecinos.", "A", "La ficha confirma la opción A."),
    sc=[("¿Qué es la latitud?", "la distancia de un lugar al ecuador", "Es la definición de la clase."),
        ("{F} ¿En qué continentes tiene territorio Chile?", "América, Oceanía y Antártica", "La ficha lo indica."),
        ("¿Qué significa tricontinental?", "con territorio en tres continentes", "Es la definición de la clase.")],
    op=("Dibuja un mapa muy simple del mundo con los continentes como manchas. Marca con un punto de color la ubicación aproximada de Chile continental, la Isla de Pascua y la Antártica. Debajo, escribe una oración que describa la localización de Chile con tres vecinos o límites. {F}",
        "Un punto en el extremo suroeste de América del Sur, otro en el océano Pacífico, al oeste, y otro en la Antártica. Oración: Chile limita con Perú, Bolivia, Argentina y el Pacífico.",
        ["tres puntos en lugares razonables", "oración con tres límites correctos", "mención de tricontinental"], ["mapa simple", "una oración"], ["poner la Isla de Pascua pegada al continente", "poner Argentina al oeste"],
        "Pide que explique por qué Chile es tricontinental."),
    reinforce="Di en voz alta los límites de Chile y sus tres continentes.",
    extend="Escribe una pregunta sobre qué ventajas puede tener ser un país tricontinental.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 43 (tipos de mapas y datos, hecha para este cuaderno). "
     "Mapa A, mapa político: muestra los límites entre países y las regiones de Chile; su leyenda usa colores para cada región. "
     "Mapa B, mapa físico: muestra el relieve con colores; en la leyenda, el verde indica poca altura y el café indica montañas altas. "
     "Mapa C, mapa de zonas marítimas: muestra el mar territorial (12 millas náuticas desde la costa), la zona contigua (24 millas) y la zona económica exclusiva (200 millas). "
     "Tabla D, datos de práctica: la Isla de Pascua está a cerca de 3.700 km de la costa chilena; la isla Robinson Crusoe, del archipiélago de Juan Fernández, está a cerca de 670 km de la costa.")
build(
    OA10, 2, F,
    use="Aprenderé a usar mapas y tablas como fuentes para conocer el territorio nacional. Sirve para saber qué muestra cada tipo de mapa y cómo leer su leyenda.",
    prior=["Sé que Chile es un país tricontinental.", "Sé reconocer países vecinos.", "Sé que una fuente tiene un propósito."],
    explain=[
        "Los mapas son fuentes geográficas. Cada tipo de mapa responde a una pregunta distinta. El mapa político muestra países, regiones y límites. El mapa físico muestra el relieve, es decir, montañas, llanuras y valles. Un mapa de zonas marítimas muestra hasta dónde llega el mar de un país.",
        "Para leer un mapa hay que mirar el título, la leyenda y, si hay, la escala. La leyenda explica el significado de los colores y los símbolos. La escala permite calcular distancias. Además hay que preguntarse quién hizo el mapa y para qué, porque un mapa muestra solo algunos datos.",
        "El territorio de Chile incluye el suelo, el subsuelo, el espacio aéreo y el mar. El mar territorial llega hasta 12 millas náuticas desde la costa, la zona contigua hasta 24 millas y la zona económica exclusiva hasta 200 millas. Una milla náutica es una unidad de medida usada en el mar. Estos datos aparecen en mapas marítimos.",
    ],
    vocab=[("leyenda", "parte del mapa que explica los colores y símbolos"), ("escala", "relación entre la distancia en el mapa y la distancia real"), ("relieve", "formas de la superficie terrestre, como montañas y llanuras"), ("mar territorial", "franja de mar de 12 millas náuticas desde la costa donde el país ejerce soberanía"), ("zona económica exclusiva", "zona de hasta 200 millas náuticas desde la costa donde el país tiene derecho a los recursos")],
    worked=[
        ("Leer una leyenda", "{F} En el mapa B, ¿qué indica el color café?", ["Miro la leyenda del mapa físico.", "El café indica montañas altas."], "Montañas altas"),
        ("Elegir el mapa adecuado", "{F} ¿Qué mapa usarías para ver los límites con países vecinos?", ["Busco un mapa que muestre límites.", "El político muestra países y límites."], "El mapa político"),
    ],
    mistakes=[("Usar un mapa físico para ver los límites de las regiones.", "Se confunde el tipo de mapa.", "El mapa político muestra límites; el físico, el relieve."),
              ("Olvidar leer la leyenda.", "Se interpretan los colores sin saber su significado.", "La leyenda explica qué significa cada color.")],
    T=[
        ("{F} ¿Qué mapa muestra el relieve?", "el mapa B", "Es el mapa físico."),
        ("{F} ¿Qué mapa muestra las zonas marítimas?", "el mapa C", "La ficha lo indica."),
        ("{F} ¿Hasta cuántas millas náuticas llega el mar territorial?", "12", "La ficha lo indica."),
        ("{F} ¿Hasta cuántas millas náuticas llega la zona económica exclusiva?", "200", "La ficha lo indica."),
        ("=", "{F} ¿Cuántas millas náuticas más allá del límite del mar territorial llega la zona contigua?", "24-12", "Se resta la medida menor a la mayor.", " millas"),
        ("=", "{F} ¿Cuántos kilómetros más lejos de la costa está la Isla de Pascua que la isla Robinson Crusoe?", "3700-670", "Se resta la distancia menor a la mayor.", " km"),
        ("{F} ¿Para qué sirve la leyenda de un mapa?", "para explicar el significado de los colores y símbolos", "La explicación lo define."),
        ("{F} ¿Qué mapa elegirías para saber qué regiones tiene Chile?", "el mapa A, el político", "Muestra las regiones."),
        ("{F} ¿Qué mapa elegirías para saber dónde están las montañas más altas?", "el mapa B, el físico", "Muestra el relieve."),
        ("{F} Una alumna dice: «El mapa B muestra las fronteras de las regiones». ¿Qué error comete?", "el mapa B muestra el relieve; las regiones las muestra el político", "Cada mapa responde a una pregunta."),
        ("{F} Un compañero dice: «La zona económica exclusiva llega a 12 millas». ¿Qué error comete?", "llega a 200 millas; 12 millas es el mar territorial", "La ficha lo indica."),
        ("{F} ¿Qué dato de la tabla D muestra que Pascua está muy lejos del continente?", "cerca de 3.700 km de la costa", "Es una distancia enorme."),
        ("{F} ¿Qué pregunta debes hacer a un mapa antes de usarlo?", "quién lo hizo, para qué y qué muestra", "Ayuda a conocer su propósito y límites."),
    ],
    ctx=("Para una exposición sobre el mar chileno, un grupo necesita saber hasta dónde llegan las 200 millas. ¿Qué mapa de la ficha deben usar y para qué sirve ese límite?", "el mapa C; marca la zona económica exclusiva donde Chile tiene derecho a los recursos", "El mapa C muestra las zonas marítimas."),
    sc=[("¿Qué es la leyenda de un mapa?", "la parte que explica los colores y símbolos", "Es la definición de la clase."),
        ("{F} ¿Hasta dónde llega la zona contigua?", "24 millas náuticas", "La ficha lo indica."),
        ("¿Qué incluye el territorio nacional?", "suelo, subsuelo, espacio aéreo y mar", "Lo explica la clase.")],
    op=("Dibuja tres rectángulos y en cada uno haz un esquema del mapa A, B o C de la ficha, según su descripción. En el mapa C dibuja la costa y tres franjas de mar con sus medidas (12, 24 y 200 millas). Debajo, escribe qué pregunta responde cada mapa. {F}",
        "A responde qué regiones y países limitan; B responde cómo es el relieve; C responde hasta dónde llega el mar de Chile. En C: tres franjas con 12, 24 y 200.",
        ["tres esquemas", "medidas del mapa C correctas", "una pregunta por mapa"], ["tres esquemas", "tres preguntas"], ["cambiar las medidas", "mezclar los tipos de mapa"],
        "Pide que explique por qué un mapa político no sirve para ver el relieve."),
    reinforce="Di en voz alta qué pregunta responde cada tipo de mapa.",
    extend="Escribe una pregunta que un mapa de zonas marítimas no puede responder.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 44 (relaciones y consecuencias del carácter tricontinental, hecha para este cuaderno). "
     "Forma de Chile: largo y angosto, con la cordillera de los Andes al este y el océano Pacífico al oeste. "
     "Consecuencias de su gran extensión de norte a sur: muchos climas distintos, desde el desierto del norte hasta zonas frías en el sur. "
     "Consecuencias del carácter tricontinental: Chile tiene una zona económica exclusiva muy grande por sus islas y su extensa costa; participa en la investigación científica de la Antártica; la Isla de Pascua aporta una cultura y un patrimonio mundial únicos (Rapa Nui). "
     "Desafíos: la conectividad con lugares lejanos, la protección del medio ambiente y la presencia del Estado en todo el territorio.")
build(
    OA10, 3, F,
    use="Aprenderé a relacionar la forma y la localización de Chile con sus consecuencias. Sirve para explicar por qué Chile tiene climas distintos, recursos marinos y desafíos particulares.",
    prior=["Sé ubicar a Chile y su carácter tricontinental.", "Sé leer mapas.", "Sé distinguir causa y consecuencia."],
    explain=[
        "La forma y la localización de un país tienen consecuencias. Chile es largo y angosto: va de norte a sur por más de 4.000 kilómetros, con la cordillera al este y el océano al oeste. Una consecuencia de esa extensión es que hay muchos climas diferentes, desde el desierto del norte hasta zonas frías en el sur.",
        "El carácter tricontinental también tiene consecuencias. Chile tiene una zona económica exclusiva muy grande, gracias a su extensa costa y a sus islas. Participa en la investigación científica en la Antártica. Y la Isla de Pascua aporta una cultura única, la del pueblo rapa nui, y un patrimonio reconocido en el mundo.",
        "También hay desafíos. Es difícil conectar lugares muy lejanos, proteger el medio ambiente y asegurar la presencia del Estado en todo el territorio. Los actores que participan son el Estado, las comunidades locales, los científicos y las empresas. Explicar bien implica decir quiénes ganan y quiénes enfrentan las dificultades.",
    ],
    vocab=[("clima", "conjunto de condiciones del tiempo atmosférico que se repiten en un lugar"), ("patrimonio", "bienes y tradiciones que se cuidan porque tienen un valor especial"), ("conectividad", "posibilidad de comunicarse o llegar a un lugar"), ("medio ambiente", "conjunto de seres vivos y elementos de la naturaleza que nos rodean"), ("recurso natural", "elemento de la naturaleza que las personas usan, como el agua o los peces")],
    worked=[
        ("Relacionar forma y clima", "{F} ¿Por qué Chile tiene climas muy distintos?", ["Chile es muy largo de norte a sur.", "Eso da climas diferentes, desde desierto hasta zonas frías."], "Porque se extiende mucho de norte a sur"),
        ("Identificar un desafío", "{F} Nombra un desafío del territorio de Chile.", ["Reviso los desafíos de la ficha.", "Uno es la conectividad con lugares lejanos."], "La conectividad con lugares lejanos"),
    ],
    mistakes=[("Pensar que Chile tiene un solo clima.", "Se olvida su gran extensión.", "Tiene muchos climas por su extensión de norte a sur."),
              ("Creer que el carácter tricontinental solo trae ventajas.", "Se olvidan los desafíos.", "También hay desafíos de conectividad y de medio ambiente.")],
    T=[
        ("{F} ¿Qué hay al este de Chile según la ficha?", "la cordillera de los Andes", "La ficha lo indica."),
        ("{F} ¿Qué hay al oeste?", "el océano Pacífico", "La ficha lo indica."),
        ("{F} ¿Qué consecuencia tiene que Chile sea largo de norte a sur?", "tiene muchos climas distintos", "La ficha lo indica."),
        ("{F} ¿A qué pueblo pertenece la cultura de la Isla de Pascua que menciona la clase?", "al pueblo rapa nui", "La ficha escribe Rapa Nui y la explicación habla del pueblo rapa nui."),
        ("{F} Clasifica como ventaja (V) o desafío (D): a) zona económica exclusiva grande; b) conectividad con lugares lejanos; c) investigación en la Antártica; d) proteger el medio ambiente.", "a: V; b: D; c: V; d: D", "La ficha las clasifica así."),
        ("=", "{F} Si usamos 4.000 km como largo de Chile de norte a sur, ¿cuántos tramos de 500 km caben en esa longitud?", "4000//500", "Se divide el largo total por el tramo.", " tramos"),
        ("{F} ¿Quiénes participan en el cuidado del territorio según la explicación?", "el Estado, las comunidades locales, los científicos y las empresas", "La explicación los enumera."),
        ("{F} ¿Qué consecuencia tiene la costa extensa de Chile?", "una zona económica exclusiva muy grande", "La ficha lo indica."),
        ("{F} Un compañero dice: «Chile tiene un solo clima». Corrígelo.", "no: por su extensión tiene muchos climas", "La ficha lo indica."),
        ("{F} Una alumna dice: «La Isla de Pascua no es importante para Chile». ¿Qué dato de la ficha lo contradice?", "que aporta una cultura y un patrimonio únicos", "La ficha lo señala."),
        ("{F} ¿Por qué la conectividad es un desafío?", "porque hay lugares muy lejanos entre sí", "La ficha lo indica."),
        ("{F} ¿Qué dos tipos de lugares tiene Chile además del continental?", "una isla de Oceanía y un territorio antártico", "La ficha los menciona."),
        ("{F} Elige la mejor explicación. A) El carácter tricontinental trae ventajas y desafíos. B) Solo trae problemas.", "A", "La ficha describe ambos."),
    ],
    ctx=("Un grupo debate si conviene proteger el mar de Chile. Escribe una razón basada en la ficha.", "porque la zona económica exclusiva es muy grande y tiene recursos marinos y medio ambiente que cuidar", "La ficha presenta ese territorio y el desafío ambiental."),
    sc=[("¿Qué es el clima?", "el conjunto de condiciones del tiempo que se repiten en un lugar", "Es la definición de la clase."),
        ("{F} ¿Qué es la conectividad?", "la posibilidad de comunicarse o llegar a un lugar", "Es la definición de la clase."),
        ("¿Qué consecuencia tiene la gran extensión de Chile?", "muchos climas distintos", "La ficha lo indica.")],
    op=("Dibuja un esquema de causa y consecuencia con flechas: escribe en el centro «Chile es largo y angosto» y dibuja tres flechas hacia tres consecuencias de la ficha. Después escribe dos desafíos y una ventaja del carácter tricontinental. {F}",
        "Consecuencias: muchos climas, zona económica exclusiva grande, cultura rapa nui. Desafíos: conectividad y medio ambiente. Ventaja: investigación en la Antártica.",
        ["tres consecuencias", "dos desafíos", "una ventaja"], ["esquema con flechas", "lista de desafíos y ventaja"], ["poner un desafío como ventaja", "no incluir flechas"],
        "Pide que explique una flecha con sus palabras."),
    reinforce="Di en voz alta tres consecuencias de la forma de Chile.",
    extend="Escribe una pregunta sobre cómo se podría mejorar la conectividad con las islas.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 45 (comparación de los tres territorios, hecha para este cuaderno; datos generales). "
     "Chile continental (América): territorio extenso, de desierto a zonas frías; la mayor parte de la población del país vive aquí; actividades como minería, agricultura, pesca y servicios. "
     "Isla de Pascua (Oceanía): isla en el océano Pacífico, de clima subtropical; hogar del pueblo rapa nui; su patrimonio atrae turismo; está a cerca de 3.700 km de la costa. "
     "Territorio Chileno Antártico (Antártica): territorio helado, sin población permanente en grandes ciudades; allí hay bases científicas y sus habitantes son científicos, personal militar y algunas familias; el Tratado Antártico, firmado en 1959, regula su uso pacífico y la investigación científica.")
build(
    OA10, 4, F,
    use="Aprenderé a comparar los tres territorios que forman Chile: el continental, la Isla de Pascua y el antártico. Sirve para ver sus semejanzas y diferencias.",
    prior=["Sé que Chile es tricontinental.", "Sé leer mapas.", "Sé comparar con criterios."],
    explain=[
        "Comparar los tres territorios de Chile permite entender su diversidad. Podemos usar criterios como el clima, la población y las actividades. Así vemos qué tienen en común y en qué se diferencian.",
        "Chile continental es extenso, tiene muchos climas y la mayor parte de la población. La Isla de Pascua está en Oceanía, tiene clima subtropical, es el hogar del pueblo rapa nui y recibe turismo por su patrimonio. El Territorio Chileno Antártico es helado, casi sin población permanente y se usa para la investigación científica, según el Tratado Antártico de 1959.",
        "Aunque son muy distintos, los tres territorios forman parte del territorio nacional y requieren la presencia del Estado. Comparar permite valorar esa diversidad y entender por qué cada territorio tiene necesidades y desafíos distintos, por ejemplo en salud, transporte o protección ambiental.",
    ],
    vocab=[("subtropical", "clima cálido y húmedo sin inviernos muy fríos"), ("base científica", "lugar donde trabajan científicos en zonas lejanas"), ("Tratado Antártico", "acuerdo entre países de 1959 que regula el uso pacífico de la Antártica"), ("población permanente", "personas que viven todo el año en un lugar"), ("diversidad", "gran variedad de características")],
    worked=[
        ("Comparar la población", "{F} ¿Dónde vive la mayor parte de la población de Chile?", ["Reviso los tres territorios.", "La ficha dice que en Chile continental."], "En Chile continental"),
        ("Comparar el clima", "{F} ¿Qué diferencia de clima hay entre la Isla de Pascua y el territorio antártico?", ["Pascua tiene clima subtropical.", "La Antártica es helada."], "Pascua es subtropical y la Antártica es helada"),
    ],
    mistakes=[("Pensar que en la Antártica viven miles de personas permanentemente.", "Se confunde con las bases.", "Allí hay bases científicas y pocas personas."),
              ("Creer que la Isla de Pascua es parte de América.", "Se confunde la localización.", "Está en Oceanía, en la Polinesia.")],
    T=[
        ("{F} ¿En qué océano está la Isla de Pascua?", "en el Pacífico", "La ficha lo indica."),
        ("{F} ¿Qué tratado regula el uso pacífico de la Antártica?", "el Tratado Antártico", "La ficha lo indica."),
        ("{F} ¿En qué año se firmó el Tratado Antártico?", "1959", "La ficha lo dice."),
        ("{F} ¿Qué pueblo vive en la Isla de Pascua?", "el pueblo rapa nui", "La ficha lo dice."),
        ("{F} ¿Qué atrae turistas a la Isla de Pascua según la ficha?", "su patrimonio", "La ficha lo indica."),
        ("{F} ¿Quiénes habitan el territorio antártico?", "científicos, personal militar y algunas familias", "La ficha lo indica."),
        ("=", "{F} Un avión recorre 925 km por hora. ¿Cuántas horas tarda en volar los 3.700 km que separan la costa chilena de la Isla de Pascua?", "3700//925", "Se divide la distancia por la rapidez.", " horas"),
        ("{F} Clasifica cada rasgo como continental (C), Pascua (P) o antártico (A): a) bases científicas; b) minería; c) pueblo rapa nui.", "a: A; b: C; c: P", "La ficha asigna cada rasgo a un territorio."),
        ("{F} ¿Qué tienen en común los tres territorios?", "forman parte del territorio nacional y requieren la presencia del Estado", "La explicación lo señala."),
        ("{F} Un compañero dice: «El territorio antártico tiene ciudades grandes». Corrígelo.", "no: tiene pocas personas, en bases científicas", "La ficha lo indica."),
        ("{F} Una alumna dice: «Pascua y la Antártica tienen el mismo clima». ¿Qué error comete?", "Pascua es subtropical y la Antártica es helada", "La ficha lo dice."),
        ("{F} ¿Qué criterio permite comparar quién vive en cada territorio?", "la población", "Es un criterio de la explicación."),
        ("{F} ¿Por qué cada territorio tiene necesidades distintas?", "porque son muy diferentes en clima, población y actividades", "La diversidad crea necesidades distintas."),
    ],
    ctx=("Un afiche dice: «Los tres territorios de Chile son iguales». Usa la ficha para responder con dos diferencias.", "tienen climas distintos y poblaciones muy diferentes", "La ficha muestra diferencias claras."),
    sc=[("¿Qué es el Tratado Antártico?", "un acuerdo de 1959 que regula el uso pacífico de la Antártica", "Es la definición de la clase."),
        ("{F} ¿Qué clima tiene la Isla de Pascua?", "subtropical", "La ficha lo dice."),
        ("¿Por qué es útil comparar los tres territorios?", "para valorar su diversidad y entender sus necesidades", "Cada uno es distinto.")],
    op=("Dibuja una tabla con tres columnas (Chile continental, Isla de Pascua, Territorio Antártico) y tres filas (clima, población, actividades). Completa con la ficha. Debajo escribe una semejanza y una diferencia. {F}",
        "Continental: muchos climas, mayoría de población, minería. Pascua: subtropical, rapa nui, turismo. Antártico: helado, científicos, investigación. Semejanza: forman parte del territorio nacional.",
        ["tres columnas y tres filas", "datos de la ficha", "semejanza y diferencia"], ["tabla comparativa", "dos oraciones"], ["poner minería en la Antártica", "decir que son iguales"],
        "Pide que explique cuál fila fue más difícil."),
    reinforce="Di en voz alta una característica de cada territorio.",
    extend="Escribe una pregunta sobre cómo se cuida el medio ambiente en la Antártica.",
)
