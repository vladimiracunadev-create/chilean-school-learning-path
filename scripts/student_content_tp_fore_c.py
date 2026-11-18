"""Forestal TP 3.º y 4.º medio: OAE-02 (instrumental, sistemas de medida, SIG y GPS para dimensionar terrenos y árboles). Todo en papel, con datos de ejemplo."""
from __future__ import annotations

from tp_fore_common import AVISO, EMER, build

O2 = "TP-FORE-3y4-OAE-02"

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La empresa ficticia «Forestal Demo» pide dimensionar el predio «Demo Norte». Datos anotados: rodal 1, 30.000 m²; rodal 2, 50.000 m². "
     "Un árbol de ejemplo de especie A mide 18 m de altura y 24 cm de diámetro a la altura del pecho. "
     "Peligros anotados para el trabajo en terreno: terreno irregular, cambios de clima, calor y posibilidad de desorientación.")
build(
    O2, 1, F,
    use="Aprenderé qué se mide en el trabajo forestal, qué unidades se usan, qué son el GPS y un sistema de información geográfica, y qué reglas generales de seguridad rigen el trabajo en terreno.",
    prior=["Sé qué es un metro, un centímetro y un metro cuadrado.", "Sé multiplicar y dividir por potencias de diez.", "Sé qué es un mapa."],
    explain=[
        "Dimensionar es medir y expresar con números el tamaño de algo. En el trabajo forestal se dimensionan terrenos (su superficie), árboles individuales (su altura y su diámetro a la altura del pecho, abreviado DAP), plantaciones (cuántos árboles hay por hectárea) y bosques nativos. La superficie se mide en metros cuadrados (m²) o en hectáreas (ha), y 1 hectárea equivale a 10.000 m²; por ejemplo, un cuadrado de 100 m de lado tiene 1 ha. La madera se mide en metros cúbicos (m³).",
        "Para ubicar y dibujar los terrenos se usan el GPS, un sistema de posicionamiento global que entrega la posición de un receptor usando señales de satélites, y el SIG, un sistema de información geográfica que reúne mapas con datos asociados. Ni el GPS ni el SIG hacen el trabajo solos: tienen un margen de error y dependen de que los datos estén al día. Un instrumento sirve si es adecuado para lo que se quiere medir y su error es pequeño.",
        f"El trabajo en terreno tiene riesgos propios, como el terreno irregular, el clima y la desorientación, y lo hace personal autorizado, en equipo, con un plan de seguridad conocido por la jefatura. {EMER} {AVISO}",
    ],
    vocab=[("dimensionar", "medir y expresar con números el tamaño de algo"), ("hectárea (ha)", "unidad de superficie equivalente a 10.000 m²"), ("DAP", "diámetro del tronco medido a la altura del pecho"), ("GPS", "sistema que entrega la posición de un receptor usando señales de satélites"), ("SIG", "sistema de información geográfica: mapas reunidos con datos asociados"), ("rodal", "porción del bosque o plantación bastante uniforme, que se maneja como una unidad")],
    worked=[
        ("De m² a hectáreas", "Un rodal de ejemplo mide 70.000 m². ¿Cuántas hectáreas son?", ["1 ha son 10.000 m².", "70.000 ÷ 10.000 = 7."], "7 ha"),
        ("Clasificar una medida", "En una ficha de ejemplo aparece «DAP: 30 cm». ¿Qué magnitud es?", ["DAP es el diámetro del tronco a la altura del pecho.", "Un diámetro es una longitud, y se mide en cm."], "Un diámetro, es decir, una longitud"),
    ],
    mistakes=[("Confundir hectárea con metro cuadrado o creer que 1 ha son 1.000 m².", "Una hectárea equivale a 10.000 m².", "Divide los m² entre 10.000 para pasar a hectáreas."),
              ("Creer que el GPS elimina los peligros del terreno.", "El GPS solo informa la posición; no cambia el clima ni el terreno.", "El trabajo en terreno exige plan de seguridad y personal autorizado.")],
    T=[
        ("abc", "En Forestal: ¿cuántos metros cuadrados tiene una hectárea?", "10.000 metros cuadrados", "1.000 metros cuadrados", "100 metros cuadrados", "Una hectárea equivale a un cuadrado de 100 m de lado, que son 10.000 m²."),
        ("abc", "En Forestal: ¿qué es el DAP de un árbol?", "El diámetro del tronco medido a la altura del pecho", "La distancia entre dos árboles vecinos", "La altura total del árbol", "El DAP es un diámetro del tronco, no una altura ni una distancia."),
        ("abc", "En Forestal: ¿qué es un SIG?", "Un sistema de información geográfica, que reúne mapas con datos asociados", "Un receptor que entrega la posición con señales de satélites", "Un instrumento para medir el diámetro del tronco", "El SIG reúne mapas y datos; el receptor de satélites corresponde al GPS."),
        ("=", "{F} ¿Cuántos metros cuadrados suman los dos rodales del predio?", "30000+50000", "Se suman las superficies de los dos rodales.", " m²"),
        ("=", "{F} ¿Cuántas hectáreas suman los dos rodales del predio?", "(30000+50000)//10000", "Se suman los metros cuadrados y se dividen entre 10.000.", " ha"),
        ("abc", "{F} ¿Qué magnitud expresan los 24 cm de la ficha?", "El diámetro del tronco a la altura del pecho, una longitud", "La altura total del árbol", "La superficie del rodal", "Los 24 cm corresponden al DAP; la altura se da en metros y la superficie en m²."),
        ("abc", "{F} Para el riesgo de desorientación, ¿qué medida se clasifica como control administrativo?", "Dejar a una persona de la oficina la ruta planificada y la hora de regreso del equipo", "Pavimentar todos los caminos del predio", "Usar una gorra durante el trabajo", "Registrar ruta y hora es una regla de trabajo; pavimentar sería ingeniería y la gorra es EPP."),
        ("=", "{F} ¿Cuántas hectáreas más tiene el rodal 2 que el rodal 1?", "(50000-30000)//10000", "Se restan las superficies y se pasa la diferencia a hectáreas.", " ha"),
        ("abc", "{F} Una persona dice: «entendí la ficha, así que puedo salir sola a medir el predio». ¿Qué respuesta es correcta?", "Es falso: el trabajo en terreno lo hace personal autorizado, en equipo y con plan de seguridad", "Es cierto, si lleva un GPS", "Es cierto, si avisa a un amigo por mensaje", "Entender la ficha no habilita para trabajar; el GPS y un aviso informal no reemplazan el plan de seguridad."),
        ("abc", "Durante una visita de ejemplo, una rama grande se desprende de un árbol y una persona queda herida bajo ella. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a levantar la rama para sacarla", "Mover a la persona rápido para llevarla a la oficina", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "En Forestal: ¿por qué un GPS no reemplaza un plan de seguridad para el trabajo en terreno?", "Porque entrega una posición, pero no elimina los peligros del terreno ni del clima", "Porque el GPS nunca funciona fuera de la oficina", "Porque la normativa prohíbe tener un GPS", "El GPS informa dónde estás; los peligros siguen y se controlan con el plan."),
        ("=", "{F} Se agrega un rodal 3 de 120.000 m² al predio de la ficha. ¿Cuántas hectáreas suma ahora el predio?", "(30000+50000+120000)//10000", "Se suman las tres superficies y se pasa el total a hectáreas.", " ha"),
        ("abc", "Un informe de ejemplo dice: «el predio mide 6 ha, es decir, 6.000 m²». ¿Qué error tiene?", "Confunde la equivalencia: 6 ha son 60.000 m²", "Ninguno, porque 1 ha son 1.000 m²", "Que las hectáreas no se usan para predios", "Una hectárea son 10.000 m², por lo que 6 ha son 60.000 m²."),
    ],
    ctx=("abc", "Un amigo te invita a «practicar con el GPS» recorriendo solo un cerro con pendiente y sin avisar a nadie. ¿Qué respondes?", "Que no, porque el trabajo en terreno exige personal autorizado, plan de seguridad y avisar a un adulto responsable", "Que sí, si lleva el celular cargado", "Que sí, si salen temprano para evitar el calor", "Un celular o un horario no reemplazan el plan de seguridad ni la autorización."),
    sc=[
        ("En Forestal: ¿cuántos m² tiene una hectárea?", "10.000 m²", "Una hectárea equivale a un cuadrado de 100 m de lado."),
        ("¿Qué entrega un GPS?", "La posición de un receptor usando señales de satélites", "El GPS informa posición, no resuelve peligros."),
        ("¿Quién hace el trabajo en terreno?", "Personal autorizado, en equipo y con plan de seguridad", "El trabajo en terreno exige autorización y plan de seguridad."),
    ],
    op=("Ficha de ejemplo: el predio «Demo Este» tiene el rodal 1 de 45.000 m², el rodal 2 de 25.000 m² y el rodal 3 de 10.000 m². Peligros anotados para el trabajo en terreno: calor y terreno irregular. Escribe (a) la superficie total en m² y en hectáreas, (b) cuántas hectáreas más tiene el rodal 1 que el rodal 2, (c) un control administrativo para el calor, (d) por qué el GPS no basta para trabajar seguro.",
        "(a) 45.000 + 25.000 + 10.000 = 80.000 m², que son 8 ha. (b) (45.000 − 25.000) ÷ 10.000 = 2 ha. (c) Un horario de trabajo con pausas y agua en las horas de más calor, informado por la jefatura. (d) Porque el GPS solo informa la posición y no elimina los peligros del terreno ni del clima. El trabajo lo hace personal autorizado.",
        ["suma y convierte bien las superficies", "calcula la diferencia en hectáreas", "propone un control administrativo", "explica el alcance del GPS"],
        ["hoja con las cuatro respuestas"],
        ["usar 1.000 m² como hectárea", "proponer solo el EPP", "creer que el GPS controla los peligros"],
        "Pregunta: «¿cuántos m² tiene una hectárea?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres rodales con superficies en m² y calcula cuántas hectáreas suman.",
    extend="Explica con un ejemplo por qué una medida con error grande puede ser inútil aunque venga de un instrumento moderno.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (mapa descrito por escrito, de ejemplo, inventado). Mapa del predio «Demo Sur», escala 1:10.000, en un SIG con cuatro capas: límite del predio, rodales, caminos y cursos de agua. "
     "El rodal A se dibuja en el mapa como un rectángulo de 4 cm por 3 cm. Tabla de atributos (datos asociados a cada rodal): rodal A, especie A, tipo plantación; rodal B, especie B, tipo bosque nativo. "
     "El receptor GPS del equipo informa su posición con un error de ejemplo de hasta 5 m.")
build(
    O2, 2, F,
    use="Aprenderé a leer un mapa descrito por escrito: escala, coordenadas, capas de un SIG, tabla de atributos y el significado del error de un GPS.",
    prior=["Sé qué es un SIG, un GPS y una hectárea.", "Sé pasar centímetros a metros.", "Sé calcular el área de un rectángulo."],
    explain=[
        "La escala de un mapa dice cuántas veces más grande es la realidad que el dibujo. En una escala 1:5.000, 1 cm del mapa equivale a 5.000 cm reales, es decir, 50 m; por eso 2 cm del mapa son 100 m. Las coordenadas son números, como la latitud y la longitud, que indican la posición de un punto sobre la Tierra. Para medir una distancia real se mide en el mapa, se multiplica por la escala y se pasa a metros.",
        "Un SIG ordena la información en capas, cada una con datos de un mismo tipo, por ejemplo caminos o cursos de agua. Cada elemento de una capa tiene una tabla de atributos con sus datos, como la especie o el tipo de bosque. Una capa desactualizada puede llevar a planificar mal, de modo que cada capa debe indicar su fecha. El GPS tiene un error: un error de 5 m significa que el punto real puede estar hasta a 5 m de la posición informada, y eso importa más si lo que se quiere ubicar es muy pequeño.",
        f"Los mapas y las capas los elabora y actualiza personal especializado en información geográfica; aquí aprendes a leerlos y a juzgarlos. {EMER} {AVISO}",
    ],
    vocab=[("escala", "relación entre una medida en el mapa y la medida real"), ("coordenadas", "números que indican la posición de un punto sobre la Tierra"), ("capa", "conjunto de datos de un mismo tipo dentro de un SIG"), ("tabla de atributos", "tabla con los datos asociados a cada elemento de una capa"), ("error del GPS", "diferencia máxima posible entre la posición real y la informada")],
    worked=[
        ("Pasar del mapa a la realidad", "En un mapa de ejemplo a escala 1:2.000, un camino mide 6 cm. ¿Cuántos metros reales mide?", ["6 × 2.000 = 12.000 cm.", "12.000 cm son 120 m."], "120 m"),
        ("Leer una tabla de atributos", "Una tabla de ejemplo dice: rodal C, especie A, bosque nativo. ¿De qué tipo es el rodal C?", ["Se busca la fila del rodal C.", "La columna de tipo dice bosque nativo."], "Bosque nativo"),
    ],
    mistakes=[("Medir en el mapa y llamar «metros» a los centímetros del dibujo.", "Los centímetros del mapa no son los de la realidad: hay que aplicar la escala.", "Multiplica por la escala y recién después pasa a metros."),
              ("Usar una capa sin mirar su fecha.", "Una capa vieja puede mostrar caminos o límites que ya cambiaron.", "Revisa la fecha de cada capa antes de usarla.")],
    T=[
        ("abc", "En Forestal: ¿qué es una capa de un SIG?", "Un conjunto de datos de un mismo tipo, como caminos o cursos de agua", "Una hoja de plástico que protege el mapa impreso", "El color de fondo del mapa", "Una capa agrupa datos de un tipo; no es una protección ni un color."),
        ("abc", "En Forestal: ¿qué indica la escala de un mapa?", "La relación entre una medida del mapa y la medida real", "La cantidad de colores que usa el dibujo", "El tamaño del papel en que se imprime", "La escala permite pasar medidas del mapa a la realidad."),
        ("abc", "En Forestal: ¿qué son las coordenadas de un punto?", "Números que indican su posición sobre la Tierra", "La distancia entre dos rodales", "El nombre de un rodal en la tabla", "Las coordenadas, como latitud y longitud, ubican un punto."),
        ("=", "{F} ¿Cuántos metros reales equivale 1 cm del mapa de la ficha?", "10000//100", "Se multiplica 1 cm por la escala y se pasa de centímetros a metros.", " m"),
        ("=", "{F} ¿Cuántos metros reales mide el lado de 4 cm del rodal A?", "4*10000//100", "Se multiplica por la escala y se pasa a metros.", " m"),
        ("abc", "{F} Según la tabla de atributos, ¿qué rodal es una plantación?", "El rodal A", "El rodal B", "Ambos rodales", "La tabla indica que A es plantación y B es bosque nativo."),
        ("=", "{F} ¿Cuántas hectáreas tiene el rodal A?", "(4*10000//100)*(3*10000//100)//10000", "Se calcula cada lado real, se multiplica para obtener m² y se pasa a hectáreas.", " ha"),
        ("abc", "{F} ¿Qué significa que el GPS tenga un error de hasta 5 m?", "Que la posición real puede estar hasta a 5 m de la posición informada", "Que siempre marca la posición 5 m al norte", "Que el GPS no sirve para ningún trabajo", "El error es un margen posible, no un desplazamiento fijo."),
        ("abc", "{F} Se necesita ubicar un límite con un error máximo de 1 m. ¿Qué conclusión corresponde con ese GPS?", "El receptor no es suficiente para ese objetivo; lo decide un especialista", "Sirve, porque 5 m es un valor cercano a 1 m", "Basta con anotar 1 m en la ficha", "Si el error del instrumento supera lo exigido, no cumple el objetivo, y anotar otro valor sería falsear el dato."),
        ("abc", "En Forestal: ¿por qué una capa de caminos desactualizada puede ser un problema para planificar?", "Porque podría llevar a planificar una ruta por un camino que ya no existe o está cerrado", "Porque los caminos cambian el color del mapa", "Porque una capa se borra sola si no se abre", "Los datos viejos pueden contradecir la realidad y llevar a malas decisiones."),
        ("abc", "{F} Dos personas miden el mismo rodal en mapas distintos y obtienen 12 ha y 6 ha. ¿Qué verificación corresponde primero?", "Revisar la escala de cada mapa", "Promediar las dos cifras", "Elegir la cifra más alta", "Una diferencia grande entre mapas suele venir de la escala usada, y debe aclararse antes de decidir."),
        ("=", "En un mapa de ejemplo a escala 1:5.000, un camino mide 12 cm. ¿Cuántos metros reales mide el camino?", "12*5000//100", "Se multiplica la medida del mapa por la escala y se pasa a metros.", " m"),
        ("abc", "{F} ¿Qué se necesita para saber si una capa del SIG está al día?", "Que la capa indique su fecha de elaboración o de última actualización", "Que tenga más colores que las otras", "Que el mapa se vea ordenado", "La fecha informa qué tan reciente es la información; el aspecto no."),
    ],
    ctx=("abc", "Una compañera te manda por mensaje las coordenadas de un punto de un predio y propone que vayas solo, por la tarde, a revisarlo. ¿Qué haces?", "Rechazar la propuesta y consultar a un adulto responsable, porque el trabajo en terreno lo hace personal autorizado con plan de seguridad", "Ir, pero llevar el celular", "Ir de todos modos, pero avisar al volver", "Unas coordenadas dicen dónde está un punto, pero no autorizan a ir ni controlan los peligros."),
    sc=[
        ("En Forestal: ¿qué es una tabla de atributos?", "Una tabla con los datos asociados a cada elemento de una capa", "La tabla guarda datos como especie y tipo de bosque."),
        ("¿Qué se hace con una medida tomada en el mapa?", "Se multiplica por la escala y se pasa a metros", "Así se obtiene la medida real."),
        ("¿Qué significa un error de 5 m del GPS?", "Que el punto real puede estar hasta a 5 m del informado", "El error es un margen posible de diferencia."),
    ],
    op=("Ficha de ejemplo: mapa del predio «Demo Oeste», escala 1:5.000. El rodal C se dibuja como un rectángulo de 6 cm por 4 cm. Tabla de atributos: rodal C, especie B, tipo plantación; rodal D, especie A, tipo bosque nativo. El GPS del equipo tiene un error de hasta 3 m. Escribe (a) las medidas reales del rodal C en metros, (b) su superficie en hectáreas, (c) el tipo del rodal D, (d) si el GPS sirve para ubicar un punto con error máximo de 1 m y por qué.",
        "(a) 6 × 5.000 ÷ 100 = 300 m y 4 × 5.000 ÷ 100 = 200 m. (b) 300 × 200 = 60.000 m², que son 6 ha. (c) Bosque nativo. (d) No sirve: su error de hasta 3 m es mayor que lo exigido; lo decide un especialista.",
        ["aplica bien la escala", "calcula la superficie y la pasa a hectáreas", "lee la tabla de atributos", "justifica sobre el error del GPS"],
        ["hoja con las cuatro respuestas"],
        ["no aplicar la escala", "olvidar pasar de m² a ha", "creer que el GPS puede corregir su error"],
        "Pregunta: «¿cuántos metros reales es 1 cm en este mapa?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un mapa a escala 1:1.000 con un rectángulo de 5 cm por 2 cm y calcula sus medidas reales en metros.",
    extend="Explica con un ejemplo por qué una capa de un SIG debe indicar su fecha.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (inventario de ejemplo, inventado). Rodal «R-5» de 12 ha, especie A. Se midieron 5 parcelas, cada una de 500 m². Árboles contados por parcela: parcela 1, 22; parcela 2, 25; parcela 3, 24; parcela 4, 29; parcela 5, 20. "
     "La densidad objetivo de ejemplo que fija el plan de manejo para este rodal es de 500 árboles por hectárea.")
build(
    O2, 3, F,
    use="Aprenderé a leer un inventario forestal: parcelas, muestra, densidad y estimación del total de árboles de un rodal.",
    prior=["Sé qué es una hectárea y cuántos m² tiene.", "Sé calcular un promedio.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Un inventario forestal es el conteo y la medición de los árboles de un lugar. Como medir todos los árboles tomaría mucho tiempo, se miden parcelas: superficies pequeñas y delimitadas que forman una muestra. De los datos de la muestra se estima el total del rodal. La densidad es el número de árboles por hectárea. Si una parcela de 250 m² tiene 20 árboles, como una hectárea contiene 40 parcelas de ese tamaño, la densidad estimada es 800 árboles por hectárea.",
        "Una estimación no es un conteo exacto: depende de cuántas parcelas se midieron y de que representen bien al rodal. Por eso se usan varias parcelas y se promedian, y no se mide solo una. Los resultados se comparan con lo que fija el plan de manejo, el documento que establece qué se hará en el predio, y las diferencias se informan. Nunca se inventa ni se ajusta el dato de una parcela que no se pudo medir.",
        f"El inventario en terreno lo hace personal autorizado; aquí practicas leer sus datos y calcular con ellos. {EMER} {AVISO}",
    ],
    vocab=[("inventario forestal", "conteo y medición de los árboles de un lugar"), ("parcela", "superficie pequeña y delimitada donde se miden los árboles"), ("muestra", "conjunto de parcelas medidas para estimar el total"), ("densidad", "número de árboles por hectárea"), ("estimación", "valor calculado a partir de una muestra, no un conteo exacto"), ("plan de manejo", "documento que establece qué se hará en un predio forestal")],
    worked=[
        ("Densidad desde una parcela", "Una parcela de ejemplo de 1.000 m² tiene 70 árboles. ¿Cuál es la densidad estimada?", ["Una hectárea tiene 10 parcelas de 1.000 m².", "70 × 10 = 700 árboles por hectárea."], "700 árboles por hectárea"),
        ("Promedio de parcelas", "Tres parcelas de ejemplo tienen 18, 20 y 22 árboles. ¿Cuál es el promedio por parcela?", ["Se suman: 18 + 20 + 22 = 60.", "Se divide entre 3: 60 ÷ 3 = 20."], "20 árboles por parcela"),
    ],
    mistakes=[("Medir una sola parcela y multiplicar por la superficie del rodal.", "Una parcela puede ser más densa o más rala que el resto del rodal.", "Usa varias parcelas y trabaja con su promedio."),
              ("Completar con un número inventado una parcela que no se pudo medir.", "Un dato inventado falsea el inventario.", "Se informa que la parcela no se midió y se deja constancia.")],
    T=[
        ("abc", "En Forestal: ¿qué es una parcela de inventario?", "Una superficie pequeña y delimitada donde se miden los árboles", "Un rodal completo con todos sus árboles", "Un camino de acceso al rodal", "La parcela es una unidad de muestra pequeña."),
        ("abc", "En Forestal: ¿qué es la densidad de una plantación?", "El número de árboles por hectárea", "La altura promedio de los árboles", "El peso de la madera de cada árbol", "La densidad relaciona cantidad de árboles con superficie."),
        ("abc", "En Forestal: ¿por qué se mide una muestra de parcelas y no todos los árboles?", "Porque medir todos toma mucho tiempo y la muestra permite estimar el total", "Porque la norma prohíbe medir todos los árboles", "Porque las parcelas son siempre más exactas que contar todos", "La muestra ahorra tiempo y permite estimar el total con cierto margen."),
        ("=", "{F} ¿Cuántos árboles se contaron en total en las 5 parcelas?", "22+25+24+29+20", "Se suman los árboles contados en cada parcela.", " árboles"),
        ("=", "{F} ¿Cuál es el promedio de árboles por parcela?", "(22+25+24+29+20)//5", "Se suma el total contado y se divide entre las 5 parcelas.", " árboles"),
        ("=", "{F} ¿Cuántas parcelas de 500 m² caben en una hectárea?", "10000//500", "Se divide la superficie de una hectárea entre la de cada parcela.", " parcelas"),
        ("=", "{F} ¿Cuál es la densidad estimada en árboles por hectárea?", "((22+25+24+29+20)//5)*(10000//500)", "Se multiplica el promedio por parcela por las parcelas que caben en una hectárea.", " árboles por hectárea"),
        ("=", "{F} ¿Cuántos árboles se estima que tiene el rodal de 12 ha?", "((22+25+24+29+20)//5)*(10000//500)*12", "Se multiplica la densidad estimada por las hectáreas del rodal.", " árboles"),
        ("abc", "{F} ¿Qué parcela se aleja más del promedio de 24 árboles?", "La parcela 4, con 29 árboles", "La parcela 3, con 24 árboles", "La parcela 1, con 22 árboles", "La parcela 4 está 5 árboles sobre el promedio, la mayor diferencia de las cinco."),
        ("abc", "{F} Un compañero propone medir solo la parcela 4 y multiplicar su conteo por todo el rodal. ¿Por qué es mala idea?", "Porque una sola parcela puede no representar al rodal entero", "Porque 29 es un número impar", "Porque siempre debe usarse la parcela con menos árboles", "Una parcela aislada puede estar más densa o más rala que el resto."),
        ("abc", "{F} Comparada con la densidad objetivo de 500 árboles por hectárea, ¿qué se concluye de la densidad estimada?", "Está 20 árboles por hectárea bajo el objetivo", "Está 20 árboles por hectárea sobre el objetivo", "Es exactamente igual al objetivo", "La densidad estimada es 480 árboles por hectárea, menor que 500."),
        ("=", "{F} ¿Cuántos árboles faltarían en total en el rodal de 12 ha para alcanzar la densidad objetivo?", "(500-((22+25+24+29+20)//5)*(10000//500))*12", "Se calcula cuántos árboles por hectárea faltan y se multiplica por las hectáreas.", " árboles"),
        ("abc", "{F} ¿Por qué el total estimado del rodal es una estimación y no un conteo exacto?", "Porque se calculó a partir de una muestra de 5 parcelas, no de todos los árboles", "Porque las hectáreas no se pueden multiplicar", "Porque el GPS siempre se equivoca", "Al usar una muestra, el resultado tiene un margen de incertidumbre."),
    ],
    ctx=("abc", "Una parcela no se pudo medir por mal tiempo. Un colega propone anotar un conteo parecido al de las otras para completar el informe. ¿Qué corresponde?", "No inventar el dato: informar que la parcela no se midió y dejar constancia", "Anotar el promedio de las demás como si fuera medido", "Anotar cualquier número, porque es solo una parcela", "Un dato inventado falsea el inventario, aunque se parezca a los demás."),
    sc=[
        ("En Forestal: ¿qué es la densidad?", "El número de árboles por hectárea", "La densidad relaciona árboles con superficie."),
        ("¿Para qué se usan varias parcelas?", "Para que la muestra represente mejor al rodal", "Una sola parcela puede no representar al rodal."),
        ("¿Qué se hace con una parcela que no se pudo medir?", "Se informa y se deja constancia, sin inventar el dato", "Un dato inventado falsea el inventario."),
    ],
    op=("Ficha de ejemplo: rodal «R-9» de 8 ha. Se midieron 4 parcelas de 500 m² con 30, 26, 34 y 30 árboles. La densidad objetivo de ejemplo del plan de manejo es 550 árboles por hectárea. Escribe (a) el promedio de árboles por parcela, (b) la densidad estimada por hectárea, (c) el total estimado de árboles del rodal, (d) si la densidad está sobre o bajo el objetivo y en cuánto.",
        "(a) 30 + 26 + 34 + 30 = 120; 120 ÷ 4 = 30 árboles por parcela. (b) 30 × 20 = 600 árboles por hectárea. (c) 600 × 8 = 4.800 árboles. (d) Sobre el objetivo en 50 árboles por hectárea.",
        ["calcula bien el promedio", "convierte a densidad por hectárea", "estima el total del rodal", "compara con el objetivo"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por las parcelas que caben en una hectárea", "olvidar multiplicar por las hectáreas", "confundir sobre y bajo el objetivo"],
        "Pregunta: «¿cuántas parcelas de 500 m² caben en una hectárea?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres parcelas con conteos de árboles y calcula su promedio.",
    extend="Explica con un ejemplo por qué es mejor medir cinco parcelas que una sola.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (tabla de volumen de ejemplo, inventada). Volumen por árbol según su clase de diámetro: clase 20 cm, 200 dm³; clase 30 cm, 500 dm³; clase 40 cm, 1.000 dm³. Se sabe que 1 m³ equivale a 1.000 dm³. "
     "Parcela de 500 m² del rodal «R-6» (6 ha): 10 árboles de clase 20, 8 de clase 30 y 3 de clase 40. El plan de manejo de ejemplo autoriza intervenir como máximo 800 m³ del rodal.")
build(
    O2, 4, F,
    use="Aprenderé a estimar el volumen de madera de una parcela y de un rodal con una tabla de volumen, y a compararlo con lo que autoriza un plan de manejo.",
    prior=["Sé qué es una parcela y la densidad.", "Sé que 1 m³ equivale a 1.000 dm³.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "El volumen de un árbol es la cantidad de madera que contiene y se mide en unidades cúbicas, como el metro cúbico (m³) o el decímetro cúbico (dm³), con 1 m³ igual a 1.000 dm³. Para no cortar el árbol se estima con una tabla de volumen, que da el volumen de un árbol típico según su clase de diámetro, es decir, el grupo de árboles cuyo diámetro cae en un intervalo y se representa con un solo valor.",
        "El volumen de una parcela es la suma de los aportes de cada clase: número de árboles por volumen de cada árbol. Para pasar de la parcela a la hectárea se multiplica por las parcelas que caben en ella, y para pasar al rodal, por las hectáreas. Por ejemplo, 5 árboles de 100 dm³ aportan 500 dm³. El resultado es una estimación, porque la tabla usa valores típicos y la muestra no mide todos los árboles.",
        f"El plan de manejo fija lo que se puede intervenir; nunca se planifica más de lo autorizado. {EMER} {AVISO}",
    ],
    vocab=[("volumen", "cantidad de madera de un árbol, medida en unidades cúbicas"), ("clase de diámetro", "grupo de árboles con diámetro dentro de un intervalo, representado por un solo valor"), ("tabla de volumen", "tabla que da el volumen de un árbol típico según su clase de diámetro"), ("m³ y dm³", "metro cúbico y decímetro cúbico; 1 m³ equivale a 1.000 dm³"), ("autorizado", "permitido por el plan de manejo y la norma vigente")],
    worked=[
        ("Aporte de una clase", "En una parcela de ejemplo hay 6 árboles de una clase cuyo volumen típico es 300 dm³. ¿Qué volumen aporta esa clase?", ["Se multiplica el número de árboles por el volumen de cada uno.", "6 × 300 = 1.800 dm³."], "1.800 dm³"),
        ("De dm³ a m³", "Una parcela de ejemplo suma 12.000 dm³. ¿Cuántos m³ son?", ["1 m³ son 1.000 dm³.", "12.000 ÷ 1.000 = 12."], "12 m³"),
    ],
    mistakes=[("Creer que la clase con más árboles siempre aporta más volumen.", "Cada árbol de clases mayores contiene mucha más madera.", "Multiplica la cantidad de árboles por el volumen de cada uno antes de comparar."),
              ("Planificar sin comparar con lo que autoriza el plan de manejo.", "Se podría intervenir más de lo permitido.", "Compara siempre el volumen estimado con el máximo autorizado.")],
    T=[
        ("abc", "En Forestal: ¿qué es una clase de diámetro?", "Un grupo de árboles con diámetro dentro de un intervalo, representado por un valor", "Un grupo de árboles de la misma especie y la misma edad", "Una sala donde se enseñan las medidas del bosque", "La clase de diámetro agrupa árboles por su diámetro."),
        ("abc", "En Forestal: ¿para qué sirve una tabla de volumen?", "Para estimar el volumen de un árbol según su clase de diámetro sin cortarlo", "Para fijar el precio de la madera en el mercado", "Para contar los árboles que hay por hectárea", "La tabla de volumen entrega volúmenes típicos por clase."),
        ("abc", "En Forestal: ¿por qué el volumen calculado con una tabla y una parcela es una estimación?", "Porque la tabla da valores típicos y la muestra no mide todos los árboles", "Porque el volumen cambia según el color de la madera", "Porque los metros cúbicos no son una medida exacta", "Se usan valores típicos y una muestra, por eso hay un margen de incertidumbre."),
        ("=", "{F} ¿Cuántos dm³ aportan los árboles de clase 20 de la parcela?", "10*200", "Se multiplica el número de árboles por el volumen de cada uno.", " dm³"),
        ("=", "{F} ¿Cuántos dm³ aportan los árboles de clase 30 de la parcela?", "8*500", "Se multiplica el número de árboles por el volumen de cada uno.", " dm³"),
        ("=", "{F} ¿Cuántos m³ tiene en total la parcela?", "(10*200+8*500+3*1000)//1000", "Se suman los aportes de cada clase y se pasa de dm³ a m³.", " m³"),
        ("=", "{F} ¿Cuántos m³ por hectárea se estiman, sabiendo que en una hectárea caben 20 parcelas de 500 m²?", "((10*200+8*500+3*1000)//1000)*20", "Se multiplica el volumen de la parcela por las parcelas que caben en una hectárea.", " m³ por hectárea"),
        ("=", "{F} ¿Cuántos m³ se estima que tiene el rodal de 6 ha?", "((10*200+8*500+3*1000)//1000)*20*6", "Se multiplica el volumen por hectárea por las hectáreas del rodal.", " m³"),
        ("abc", "{F} ¿Qué clase aporta más volumen a la parcela?", "La clase 30, con 4.000 dm³", "La clase 20, porque tiene más árboles", "La clase 40, porque cada árbol tiene más volumen", "La clase 30 aporta 4.000 dm³; la clase 20 aporta 2.000 y la clase 40, 3.000."),
        ("abc", "{F} Un compañero dice que la clase 20 aporta más volumen porque tiene más árboles. ¿Qué respuesta es correcta?", "Es falso: aporta 2.000 dm³, menos que la clase 30, porque cada árbol vale menos", "Es cierto: más árboles siempre significan más volumen", "Es cierto, si se cuentan solo árboles sanos", "El aporte es la cantidad por el volumen de cada árbol, no solo la cantidad."),
        ("abc", "{F} Comparando el volumen estimado del rodal con lo que autoriza el plan, ¿qué conclusión es correcta?", "Intervenir todo el volumen superaría lo autorizado", "El volumen estimado queda bajo lo autorizado", "El plan no fija ningún máximo", "El rodal suma 1.080 m³ y el máximo autorizado es 800 m³."),
        ("=", "{F} ¿Cuántos árboles de clase 20 equivalen en volumen a un árbol de clase 40?", "1000//200", "Se divide el volumen de un árbol de clase 40 entre el de uno de clase 20.", " árboles"),
        ("=", "{F} ¿Cuántos m³ superaría el volumen total estimado del rodal al máximo autorizado?", "((10*200+8*500+3*1000)//1000)*20*6-800", "Se resta el máximo autorizado al volumen estimado del rodal.", " m³"),
    ],
    ctx=("abc", "Un encargado te pide ajustar a mano los conteos de la parcela para que el volumen del rodal «salga» más alto y poder vender más. ¿Qué corresponde?", "No alterar los datos y avisar a un adulto responsable, porque los registros deben reflejar lo medido", "Ajustar solo un poco los conteos", "Ajustarlos si el cliente lo acepta", "Un dato alterado falsea el inventario y puede llevar a intervenir más de lo autorizado."),
    sc=[
        ("En Forestal: ¿cómo se calcula el aporte de una clase de diámetro?", "Número de árboles por el volumen de cada uno", "El aporte combina cantidad y volumen unitario."),
        ("¿Cuántos dm³ tiene un m³?", "1.000 dm³", "Un metro cúbico equivale a 1.000 decímetros cúbicos."),
        ("¿Con qué se compara el volumen estimado de un rodal?", "Con el máximo que autoriza el plan de manejo", "El plan de manejo fija lo que se puede intervenir."),
    ],
    op=("Ficha de ejemplo: tabla de volumen: clase 20 cm, 200 dm³; clase 30 cm, 500 dm³; clase 40 cm, 1.000 dm³. Una parcela de 500 m² del rodal «R-8» (4 ha) tiene 5 árboles de clase 20, 4 de clase 30 y 2 de clase 40. El plan autoriza como máximo 300 m³. Escribe (a) el volumen de la parcela en m³, (b) el volumen estimado del rodal (20 parcelas por hectárea), (c) si supera lo autorizado y en cuánto o cuánto falta, (d) por qué es una estimación.",
        "(a) 5 × 200 + 4 × 500 + 2 × 1.000 = 5.000 dm³ = 5 m³. (b) 5 × 20 × 4 = 400 m³. (c) Supera lo autorizado en 100 m³. (d) Porque la tabla usa valores típicos y la parcela es solo una muestra.",
        ["calcula el aporte de cada clase", "pasa dm³ a m³ y expande a rodal", "compara con lo autorizado", "explica el carácter de estimación"],
        ["hoja con las cuatro respuestas"],
        ["olvidar pasar de dm³ a m³", "no multiplicar por las parcelas y las hectáreas", "no comparar con lo autorizado"],
        "Pregunta: «¿cuántos dm³ tiene un m³?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una tabla de volumen de tres clases y una parcela con árboles de cada clase, y calcula su volumen.",
    extend="Explica con un ejemplo por qué comparar con el plan de manejo es parte de la planificación y no un trámite aparte.",
)
