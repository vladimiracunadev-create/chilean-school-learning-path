"""Refrigeración y Climatización TP 3.º y 4.º medio: OAE-01 (leer planos de cañerías y ductos), OAE-02 (cubicar elementos y materiales) y OAE-03 (mediciones y controles de verificación). Solo conceptos, documentos y planillas, con datos de ejemplo."""
from __future__ import annotations

from tp_recl_common import AVISO, EMER, build

O1 = "TP-RECL-3y4-OAE-01"
O2 = "TP-RECL-3y4-OAE-02"
O3 = "TP-RECL-3y4-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). Proyecto «Tienda Brisa» (ficticio): un local comercial de 90 m² con climatización por ductos y una vitrina refrigerada. "
     "Documentos: planos de planta de ductos (2 láminas), esquema de cañerías (1 lámina), especificaciones técnicas (8 páginas), lista de materiales (3 páginas) y presupuesto (2 páginas). "
     "Riesgos anotados para la ejecución: alta presión en tuberías, descarga eléctrica, quemadura y caída desde altura.")
build(
    O1, 1, F,
    use="Aprenderé qué documentos forman un proyecto de climatización y refrigeración, qué riesgos hay en la obra y por qué un plano no basta para intervenir una red.",
    prior=["Sé leer una tabla y un dibujo simple.", "Sé sumar y multiplicar.", "Sé que un trabajo se encarga por escrito."],
    explain=[
        "Un sistema de refrigeración y climatización mueve calor de un lugar a otro: enfría o calienta un recinto usando un fluido llamado refrigerante, que circula por cañerías, y aire, que circula por ductos. Antes de ejecutar una obra existe un proyecto, formado por documentos. Un plano de redes es un dibujo a escala que muestra por dónde van las cañerías y los ductos. La simbología es el conjunto de símbolos del dibujo y la leyenda explica cada uno. Las especificaciones técnicas dicen por escrito cómo deben ser los materiales y el trabajo.",
        "Leer un plano exige compararlo con la obra real. Las condiciones reales de la obra son lo que existe en el recinto: vigas, muros, otras instalaciones y la altura libre. Si el dibujo pasa por un lugar ocupado, eso es una interferencia: se anota y se informa al proyectista; nadie rompe un muro ni cambia la ruta por su cuenta. Los riesgos del oficio son la alta presión del refrigerante, la descarga eléctrica, la quemadura y la caída. Se reducen con personal autorizado, norma vigente y elementos de protección personal (EPP).",
        f"{EMER} {AVISO}",
    ],
    vocab=[("refrigerante", "fluido que circula por las cañerías y transporta calor"), ("red de cañerías", "conjunto de tuberías por donde circulan el refrigerante o el agua del sistema"), ("red de ductos", "conjunto de conductos por donde circula el aire"), ("simbología", "conjunto de símbolos con que se dibuja un plano"), ("leyenda", "tabla que explica qué significa cada símbolo"), ("especificaciones técnicas", "documento escrito que dice cómo deben ser los materiales y el trabajo"), ("interferencia", "lugar donde el recorrido dibujado choca con algo que existe en la obra"), ("EPP", "elementos de protección personal, como casco, lentes y guantes")],
    worked=[
        ("Elegir el documento", "Un jefe de obra de ejemplo necesita saber de qué material deben ser los conductos de aire de una oficina. ¿Qué documento consulta primero?", ["Las características de los materiales se escriben en un documento específico.", "Ese documento son las especificaciones técnicas."], "Las especificaciones técnicas"),
        ("Reconocer una interferencia", "En un plano de ejemplo, un ducto atraviesa el lugar donde hay un muro de hormigón. ¿Qué se anota y a quién se informa?", ["El recorrido dibujado choca con algo real: eso es una interferencia.", "No se rompe el muro; se informa al proyectista."], "Una interferencia, que se informa al proyectista"),
    ],
    mistakes=[("Cambiar la ruta de un ducto en la obra porque hay una viga, sin avisar.", "Puede afectar el flujo de aire o la estructura, y nadie lo revisó.", "Anota la interferencia e informa al proyectista."),
              ("Creer que leer planos habilita para intervenir cañerías con refrigerante.", "Esa tarea exige personal autorizado, norma vigente y protección.", "Aprende los conceptos aquí y practica solo con instructor autorizado.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es una red de cañerías de un sistema de climatización?", "El conjunto de tuberías por donde circulan el refrigerante o el agua del sistema", "El conjunto de conductos por donde circula el aire del recinto", "La tabla con los costos de los materiales del sistema", "Las cañerías llevan fluidos; el aire va por ductos y los costos van en el presupuesto."),
        ("abc", "En Refrigeración: ¿para qué sirve la leyenda de un plano de redes?", "Para explicar qué significa cada símbolo del dibujo", "Para indicar cuánto cuesta cada tramo de cañería", "Para fijar cómo deben ser los materiales y el trabajo", "La leyenda explica símbolos; los costos van al presupuesto y los materiales a las especificaciones."),
        ("abc", "En una obra de ejemplo, ¿qué es una interferencia en un plano de ductos?", "Un lugar donde el recorrido dibujado choca con algo que existe, como una viga", "Un ducto que transporta más aire que el pedido en el proyecto", "Un error de ortografía en la leyenda del plano", "Una interferencia es un choque con algo real; el exceso de aire o la ortografía son otras cosas."),
        ("=", "{F} Entre los documentos escritos (especificaciones, lista de materiales y presupuesto), ¿cuántas páginas hay en total?", "8+3+2", "Se suman las páginas de los tres documentos escritos.", " páginas"),
        ("abc", "{F} El jefe de obra quiere saber cuánto costará el proyecto. ¿Qué documento debe consultar?", "El presupuesto", "La lista de materiales", "El esquema de cañerías", "Los costos se reúnen en el presupuesto; la lista indica qué piezas se necesitan y el esquema dibuja la red."),
        ("abc", "{F} ¿Cuál de estos riesgos está anotado en la ficha para la ejecución?", "Caída desde altura", "Inundación por rotura de la red de agua potable", "Intoxicación por polvo de cemento", "La ficha nombra alta presión, descarga eléctrica, quemadura y caída; los otros dos no figuran."),
        ("=", "{F} La empresa de ejemplo cobra $1.800 por m² por climatizar el local. ¿Cuánto cobra por el local?", "90*1800", "El valor por m² se multiplica por los metros cuadrados del local.", " pesos"),
        ("abc", "{F} Un ayudante sin autorización quiere abrir una cañería con refrigerante «para ver cómo es por dentro». ¿Qué corresponde?", "No hacerlo: esa tarea la realiza personal autorizado con norma vigente y protección", "Hacerlo si usa guantes y lentes", "Hacerlo si el cliente se lo permite por escrito", "Los guantes o el permiso del cliente no reemplazan la autorización ni la norma vigente."),
        ("abc", "{F} El plano pasa un ducto por el lugar donde el local tiene una viga. ¿Qué se anota y qué se hace?", "Se anota una interferencia y se informa al proyectista", "Se corta la viga para que pase el ducto", "Se cambia la ruta del ducto en la obra sin avisar", "Una interferencia se informa; ni se daña la estructura ni se cambia la ruta por cuenta propia."),
        ("ab", "{F} Una estudiante dice: «ya leí los planos, así que puedo intervenir la red de cañerías del local». ¿Es correcto?", "No: leer planos no habilita; intervenir la red lo hace personal autorizado", "Sí: leer los planos la habilita para trabajar en la red", "Entender documentos es distinto de estar autorizada para trabajar con refrigerante a presión."),
        ("abc", "{F} Las especificaciones piden ductos de un material y la lista de materiales trae otro. ¿Qué conclusión es la más prudente?", "Hay una diferencia entre documentos: se informa para aclararla antes de comprar", "Manda la lista de materiales, porque es la que se compra", "Manda la especificación y se borra la lista sin avisar", "Cuando dos documentos se contradicen no se elige uno por cuenta propia: se consulta al proyectista."),
        ("=", "{F} Si el presupuesto tuviera 4 páginas más y la lista de materiales 2 páginas menos, ¿cuántas páginas escritas tendría el proyecto (especificaciones, lista y presupuesto)?", "8+(3-2)+(2+4)", "Se ajustan la lista y el presupuesto y se suman con las especificaciones.", " páginas"),
        ("abc", "En una obra de ejemplo hay una fuga de refrigerante y una trabajadora está mareada. ¿Qué indican las reglas generales?", "No entrar ni tocar, avisar a un adulto responsable y llamar a emergencias", "Entrar rápido a cerrar la fuga para evitar daños", "Esperar a ver si la fuga se detiene sola antes de avisar", "Ante una fuga o intoxicación no se entra ni se improvisa: se avisa a un adulto responsable y a emergencias."),
    ],
    ctx=("abc", "Un vecino ofrece pagar a un estudiante para que «arregle rápido» el aire acondicionado de su casa abriendo las cañerías. ¿Qué responde?", "Agradece, explica que no está autorizado y sugiere contratar a un técnico autorizado", "Acepta si cobra menos que un técnico", "Acepta porque ya estudió los planos de un proyecto", "Intervenir cañerías con refrigerante exige autorización y norma vigente; cobrar menos o haber estudiado no la reemplazan."),
    sc=[
        ("En Refrigeración: ¿qué muestra un plano de redes de ductos?", "Por dónde va el aire, dibujado a escala con símbolos", "El plano es un dibujo a escala; los costos van al presupuesto y los materiales a las especificaciones."),
        ("¿Qué se hace si el recorrido dibujado choca con una viga real?", "Anotar la interferencia e informar al proyectista", "No se cambia la ruta ni se daña la estructura por cuenta propia."),
        ("¿Quién interviene una red con refrigerante?", "Personal autorizado, con norma vigente y protección", "Este cuaderno no habilita para trabajar ni para intervenir equipos."),
    ],
    op=("Proyecto de ejemplo «Panadería Costa» (ficticia): planos de ductos (3 láminas), especificaciones (6 páginas), lista de materiales (2 páginas) y presupuesto (2 páginas). El plano pasa un ducto por el lugar de una viga. "
        "Escribe (a) qué documento consultarías para conocer el material de los ductos, (b) cuántas páginas escritas hay en total, (c) qué haces con la viga y a quién informas, (d) un riesgo de la obra y quién debe ejecutarla.",
        "(a) Las especificaciones técnicas. (b) 6+2+2 son 10 páginas escritas. (c) Anoto una interferencia y la informo al proyectista; no corto ni cambio nada por mi cuenta. (d) Alta presión o caída desde altura; lo ejecuta personal autorizado según la norma vigente.",
        ["nombra el documento correcto", "suma bien las páginas escritas", "informa la interferencia sin decidir por su cuenta", "reconoce un riesgo y quién ejecuta"],
        ["hoja con las cuatro respuestas"],
        ["sumar las láminas como páginas escritas", "decir que cortaría la viga", "decir que puede ejecutar el trabajo"],
        "Pregunta: «¿qué haces si el plano choca con la viga?». Si no responde, pídele que relea la regla de informar la interferencia."),
    reinforce="Escribe los cinco documentos de un proyecto y, junto a cada uno, una frase que diga para qué sirve.",
    extend="Explica con un ejemplo inventado por qué un plano bien dibujado puede ser riesgoso si se ejecuta sin personal autorizado.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (esquema descrito por escrito, de ejemplo, inventado). Esquema de una sala de ventas de 10 m por 6 m, escala 1:50. Leyenda de ejemplo: R = rejilla de retorno de aire; D = difusor de impulsión; "
     "flecha continua = sentido del aire por el ducto; línea con trazos = cañería de refrigerante; V = válvula de corte. Elementos: 4 difusores (D1 a D4), 2 rejillas (R1 y R2), 6 válvulas (V1 a V6), "
     "un ducto principal de 8 m y una cañería de 12 m. En el esquema, la pared larga mide 20 cm.")
build(
    O1, 2, F,
    use="Aprenderé a leer la simbología, la leyenda, las flechas de flujo y la escala de un esquema de ductos y cañerías descrito por escrito.",
    prior=["Sé qué documentos forman un proyecto.", "Sé multiplicar y dividir por números pequeños.", "Sé pasar de centímetros a metros."],
    explain=[
        "En un esquema de climatización cada elemento se dibuja con un símbolo y la leyenda dice qué es. El ducto de impulsión lleva aire tratado desde el equipo hasta el recinto y termina en difusores, que reparten el aire. El aire vuelve al equipo por rejillas de retorno. La flecha de flujo indica el sentido en que circula el aire o el fluido. Una válvula de corte permite aislar un tramo de cañería; solo personal autorizado las opera. Un codo cambia la dirección del recorrido y una unión es el punto donde se juntan dos piezas.",
        "El esquema se dibuja a escala: una razón fija entre la medida dibujada y la real. A escala 1:20, 1 cm del dibujo son 20 cm reales. Para pasar de lo dibujado a lo real se multiplica por 20 y para pasar de lo real a lo dibujado se divide por 20. Una copia reducida o ampliada sin avisar cambia la escala; por eso se confía en las cotas, que son números que indican medidas, y en el rótulo, no en la regla.",
        f"Ninguna persona agrega símbolos nuevos ni cambia medidas por su cuenta: eso lo decide el proyectista. {EMER} {AVISO}",
    ],
    vocab=[("difusor", "pieza que reparte el aire tratado dentro del recinto"), ("rejilla de retorno", "abertura por donde el aire del recinto vuelve al equipo"), ("flecha de flujo", "flecha que indica el sentido en que circula el aire o el fluido"), ("válvula de corte", "pieza que permite aislar un tramo de cañería"), ("codo", "pieza que cambia la dirección de un ducto o cañería"), ("unión", "punto donde se juntan dos piezas"), ("escala", "razón fija entre la medida dibujada y la real"), ("cota", "número que indica una medida del dibujo")],
    worked=[
        ("Pasar a medida real", "Un esquema de ejemplo está a escala 1:25. Un ducto mide 12 cm en el dibujo. ¿Cuánto mide en la realidad?", ["Cada centímetro dibujado son 25 centímetros reales.", "12 por 25 son 300 centímetros, que son 3 metros."], "300 cm (3 m)"),
        ("Contar símbolos", "Una leyenda de ejemplo dice: C = codo; T = unión en te. Un esquema trae 5 C y 2 T. ¿Cuántos codos hay?", ["La leyenda dice que C significa codo.", "Se cuentan solo los símbolos C."], "5 codos"),
    ],
    mistakes=[("Medir con regla una copia reducida y usar la escala del rótulo.", "La copia ya no está a la escala indicada y la medida sale falsa.", "Usa las cotas o pide una copia a escala."),
              ("Contar una válvula como si fuera una rejilla porque ambas son símbolos.", "Cada símbolo significa algo distinto según la leyenda.", "Cuenta solo los símbolos que la leyenda asigna a lo que buscas.")],
    T=[
        ("abc", "En Refrigeración: ¿qué indica la flecha de flujo sobre un ducto en un esquema?", "El sentido en que circula el aire", "El diámetro del ducto", "La posición de la válvula de corte", "La flecha de flujo muestra el sentido de circulación; el diámetro se indica con cotas."),
        ("abc", "En Refrigeración: ¿para qué sirve una rejilla de retorno?", "Para que el aire del recinto vuelva hacia el equipo", "Para repartir el aire tratado dentro del recinto", "Para aislar un tramo de cañería del resto de la red", "La rejilla devuelve el aire al equipo; repartirlo es función del difusor y aislar tramos, de la válvula."),
        ("abc", "Un esquema llega a la obra sin leyenda. ¿Qué corresponde?", "Pedir la leyenda al proyectista antes de interpretar los símbolos", "Suponer que los símbolos son los de otro proyecto parecido", "Interpretar cada símbolo por su forma", "Sin leyenda un símbolo puede entenderse mal; se consulta a quien lo diseñó."),
        ("=", "{F} ¿Cuántos símbolos de difusor y de rejilla dibuja el esquema en total?", "4+2", "Se suman los 4 difusores y las 2 rejillas de la ficha.", " símbolos"),
        ("=", "{F} ¿Cuántos centímetros mide en el esquema la pared corta de la sala (6 m reales)?", "600//50", "La medida real de 600 cm se divide por la escala 1:50.", " cm"),
        ("abc", "{F} ¿Qué representa el símbolo D3 y qué hace?", "Un difusor, que reparte aire tratado en el recinto", "Una rejilla de retorno, que devuelve el aire al equipo", "Una válvula de corte, que aísla un tramo de cañería", "La leyenda asigna la letra D a los difusores, que reparten el aire."),
        ("=", "{F} Un tramo de ducto dibujado mide 14 cm en el esquema. ¿Cuántos metros reales representa?", "14*50//100", "Se multiplica por 50 para pasar a centímetros reales y se divide por 100 para pasar a metros.", " m"),
        ("abc", "{F} El esquema trae un símbolo Z1 que no está en la leyenda. ¿Qué corresponde?", "Pedir al proyectista su significado antes de usarlo", "Suponer que es otra rejilla porque se parece", "Ignorarlo y seguir con el resto del esquema", "Un símbolo sin leyenda no se interpreta por parecido: se consulta a quien diseñó."),
        ("=", "{F} Se quiere dibujar la misma sala a escala 1:100. ¿Cuántos centímetros medirá la pared larga?", "1000//100", "Los 1000 cm reales de la pared larga se dividen por la nueva escala.", " cm"),
        ("abc", "{F} Un compañero cuenta 3 rejillas porque suma R1, R2 y la válvula V1. ¿Cuál es el error?", "V1 es una válvula, no una rejilla; las rejillas son 2", "Falta sumar un difusor como si fuera rejilla", "Las rejillas no se cuentan en un esquema", "Según la leyenda, V es una válvula de corte; solo se cuentan los símbolos R."),
        ("abc", "{F} Alguien mide la pared larga con regla en una copia reducida a la mitad y obtiene 10 cm. ¿Qué conclusión es correcta?", "No debe usar esa medida: la copia está reducida; debe usar las cotas o pedir una copia a escala", "La pared mide 500 cm reales porque 10 por 50 son 500", "La pared mide 10 cm reales porque la regla siempre da lo real", "En una copia reducida la escala del rótulo ya no vale; se usan las cotas."),
        ("=", "{F} La cañería de 12 m se arma con barras de 3 m unidas entre sí. ¿Cuántas uniones entre barras tendrá la cañería?", "12//3-1", "Hay 4 barras y entre ellas queda una unión menos que barras.", " uniones"),
        ("abc", "{F} La lista de materiales pide 5 válvulas de corte y el esquema dibuja las de la ficha. ¿Qué diferencia hay y qué corresponde?", "Falta una válvula en la lista; se informa para corregir antes de comprar", "Sobra una válvula en la lista; se devuelve la compra", "No hay diferencia, porque siempre se compra una menos", "El esquema dibuja 6 válvulas y la lista pide 5: es una diferencia que se informa, no una regla de compra."),
    ],
    ctx=("abc", "Una instaladora de ejemplo recibe un esquema con la escala borrada por una mancha. ¿Qué corresponde?", "Pedir una copia legible o la escala al proyectista antes de medir", "Deducir la escala midiendo un objeto cualquiera del dibujo", "Usar la escala de otro esquema del mismo proyecto", "Sin escala legible las medidas pueden salir falsas; se pide el dato a quien diseñó."),
    sc=[
        ("En Refrigeración: ¿cómo se pasa una medida dibujada a la medida real?", "Multiplicándola por el número de la escala", "A escala 1:50, cada centímetro dibujado equivale a 50 centímetros reales."),
        ("¿Para qué sirve la leyenda de un esquema?", "Para saber qué significa cada símbolo", "Sin leyenda, un símbolo puede interpretarse mal."),
        ("En Refrigeración: ¿qué lleva el aire tratado desde el equipo hasta el recinto?", "El ducto de impulsión, que termina en difusores", "El retorno lleva el aire de vuelta; la impulsión lo entrega al recinto."),
    ],
    op=("Esquema de ejemplo de una oficina de 8 m por 5 m, escala 1:50. Leyenda: D = difusor; R = rejilla de retorno; V = válvula de corte. Elementos: 3 D, 2 R, 4 V y un símbolo X2 que no está en la leyenda. "
        "Escribe (a) cuántos centímetros mide en el esquema la pared de 8 m, (b) cuántos difusores y cuántas válvulas hay, (c) qué haces con el símbolo X2 y por qué, (d) qué medida usarías si la copia estuviera ampliada.",
        "(a) 800 dividido por 50 son 16 cm. (b) 3 difusores y 4 válvulas. (c) Pido al proyectista el significado de X2 antes de usarlo, porque no está en la leyenda y no se interpreta por parecido. (d) Usaría las cotas del esquema o pediría una copia a escala.",
        ["calcula bien la medida en el dibujo", "cuenta los símbolos según la leyenda", "no interpreta X2 por su cuenta", "reconoce que una copia ampliada no sirve para medir"],
        ["hoja con las cuatro respuestas y el cálculo"],
        ["multiplicar en vez de dividir", "contar X2 como válvula", "medir con regla una copia ampliada"],
        "Pregunta: «¿por qué no puedes suponer qué es X2?». Si no responde, pídele que relea el papel de la leyenda."),
    reinforce="Dibuja a mano alzada un croquis de una sala con dos difusores, una rejilla y una flecha de flujo, y escribe su leyenda.",
    extend="Explica con un ejemplo por qué una cota es más confiable que medir con regla un plano impreso.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Proyecto «Oficinas Los Alerces» (ficticio). Red de ductos de impulsión descrita por tramos: T1 de 6 m, T2 de 4 m y T3 de 2 m, unidos por 2 codos. "
     "El plano dibuja además 1 reducción (pieza que cambia la sección del ducto) al final de T3. Una viga cruza el tramo T2. La lista de materiales pide 12 m de ducto, 3 codos y 1 reducción. "
     "Las especificaciones piden registrar toda diferencia en un formulario de consulta con fecha.")
build(
    O1, 3, F,
    use="Aprenderé a recorrer una red de ductos tramo por tramo, a contar accesorios, a comparar el plano con la lista de materiales y a registrar una consulta.",
    prior=["Sé leer la simbología de un esquema.", "Sé sumar longitudes.", "Sé qué es una interferencia."],
    explain=[
        "Una red de ductos se lee siguiendo el recorrido del aire desde el equipo hasta el recinto. Un tramo es una parte recta entre dos cambios de dirección o de sección. Un accesorio es una pieza que no es un tramo recto: por ejemplo un codo, que cambia la dirección, o una reducción, que cambia la sección. La longitud total de la red es la suma de sus tramos, y los accesorios se cuentan aparte.",
        "La revisión cruzada compara un documento con otro: el plano con la lista de materiales. Si los datos no coinciden aparece un hallazgo, que es una diferencia o falta que se anota para corregirla. El revisor no corrige por su cuenta: llena un formulario de consulta que dice qué documentos se contradicen, qué dice cada uno, quién lo detectó y la fecha, y lo envía al proyectista. Su respuesta escrita se archiva junto a los planos. Un cambio de ruta modifica el plano, la lista y, a veces, los cálculos.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("tramo", "parte recta de una red entre dos cambios de dirección o de sección"), ("accesorio", "pieza que no es un tramo recto, como un codo o una reducción"), ("reducción", "pieza que cambia la sección de un ducto"), ("revisión cruzada", "comparación de un documento con otro para encontrar diferencias"), ("hallazgo", "diferencia o falta que se anota para corregirla"), ("formulario de consulta", "hoja donde se registra una duda o diferencia y su respuesta"), ("profesional responsable", "persona que firma y responde por una parte del proyecto, como la estructura")],
    worked=[
        ("Sumar tramos", "Una red de ejemplo tiene tramos de 5 m, 3 m y 7 m. ¿Cuánto mide en total?", ["Se suman las longitudes de los tres tramos.", "5 más 3 más 7 son 15."], "15 m"),
        ("Detectar un hallazgo", "El plano de un proyecto de ejemplo dibuja 4 codos y la lista de materiales pide 5. ¿Qué se anota?", ["Los dos documentos deben coincidir.", "Hay una diferencia de 1 codo, que se informa en el formulario."], "Un hallazgo: el plano dice 4 codos y la lista 5; se informa al proyectista"),
    ],
    mistakes=[("Corregir la lista de materiales para que calce con el plano sin avisar a nadie.", "No se sabe cuál de los dos documentos es el equivocado.", "Informa el hallazgo; el proyectista decide qué se corrige."),
              ("Dejar la respuesta del proyectista en una conversación verbal.", "Sin registro escrito nadie puede comprobar qué se decidió ni cuándo.", "Archiva la respuesta escrita con fecha junto a los planos.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es un tramo de una red de ductos?", "Una parte recta del recorrido entre dos cambios de dirección o de sección", "El conjunto completo de la red de ductos y cañerías", "La hoja donde se anotan las diferencias entre documentos", "El tramo es una parte recta; la red completa es mayor y la hoja de diferencias es el formulario."),
        ("abc", "En Refrigeración: ¿para qué sirve un codo en una red de ductos?", "Para cambiar la dirección del recorrido", "Para cambiar la sección del ducto", "Para aislar un tramo del resto de la red", "El codo cambia la dirección; cambiar la sección es función de la reducción."),
        ("abc", "¿Qué es un hallazgo en una revisión cruzada de documentos?", "Una diferencia o falta que se anota para corregirla", "Un material nuevo que se agrega a la obra", "Una medida tomada con una regla sobre el plano", "Un hallazgo es una diferencia detectada al comparar documentos, no un material ni una medida."),
        ("=", "{F} ¿Cuántos metros suman los tres tramos de ducto?", "6+4+2", "Se suman las longitudes de T1, T2 y T3.", " m"),
        ("abc", "{F} ¿Qué diferencia hay entre el plano y la lista de materiales?", "El plano dibuja 2 codos y la lista pide 3", "El plano dibuja 12 m de ducto y la lista pide 10 m", "El plano dibuja 1 reducción y la lista no la pide", "Los metros y la reducción coinciden en ambos documentos; solo los codos difieren."),
        ("abc", "{F} ¿Qué problema plantea la viga que cruza el tramo T2?", "Es una interferencia que se informa al proyectista", "Es un material que debe retirarse de la obra", "No plantea problema, porque el ducto es liviano", "Una viga cruzando el recorrido es una interferencia real; no se retira ni se ignora."),
        ("=", "{F} La empresa instaladora cobra $4.500 por cada metro de ducto instalado. ¿Cuánto cobra por la red de la ficha?", "12*4500", "Se multiplica el valor por metro por los 12 metros de ducto.", " pesos"),
        ("=", "{F} Si cada codo cuesta $6.000 y se compran los que pide la lista de materiales, ¿cuánto cuestan los codos?", "3*6000", "Se multiplica el precio de un codo por los 3 codos de la lista.", " pesos"),
        ("abc", "{F} ¿Qué debe contener el formulario de consulta por la diferencia de codos?", "Qué documentos se contradicen, qué dice cada uno, quién lo detectó y la fecha", "Solo el nombre de quien lo detectó", "La solución elegida, aunque nadie la haya aprobado", "Un registro útil deja constancia de qué, dónde, quién y cuándo."),
        ("abc", "{F} Un compañero dice: «como la lista pide 3 codos, el plano está mal y lo corrijo». ¿Qué respuesta es correcta?", "No: no se sabe cuál documento se equivoca; se informa la diferencia al proyectista", "Sí: la lista de materiales siempre manda sobre el plano", "Sí, pero solo si lo anota después de corregirlo", "Ningún documento manda por sí solo; decide quien diseñó el proyecto."),
        ("abc", "{F} Para evitar la viga se propone bajar el tramo T2, lo que agrega 2 codos. ¿Qué debe hacerse antes de ejecutar ese cambio?", "Consultar al proyectista, porque cambia el plano, la lista y quizá los cálculos", "Ejecutarlo y actualizar los documentos al final", "Pedir al cliente que lo apruebe de palabra", "Un cambio de ruta afecta varios documentos y lo autoriza el proyectista por escrito."),
        ("=", "{F} Si se baja el tramo T2, la red necesitaría 1 m más de ducto que lo dibujado en el plano. ¿Cuántos metros de ducto tendría la red?", "12+1", "Al total dibujado de 12 m se le suma el metro adicional.", " m"),
        ("abc", "{F} ¿Qué registro deja constancia correcta de la decisión final sobre la viga?", "Una respuesta escrita del proyectista con fecha, archivada con los planos", "Un mensaje verbal de un compañero de obra", "Una nota personal del instalador", "La constancia debe ser escrita, fechada y emitida por quien decide."),
    ],
    ctx=("abc", "Una instaladora de ejemplo ve en obra un ducto dibujado que atraviesa una viga. Su jefe dice: «pasa igual, rompe un poco la viga». ¿Qué responde?", "Que la estructura no se modifica sin la autorización del profesional responsable", "Que lo hace, pero con casco y guantes", "Que lo hace de noche, cuando no hay nadie", "El casco o el horario no hacen segura una modificación estructural; la autoriza el profesional responsable."),
    sc=[
        ("En Refrigeración: ¿qué es la longitud total de una red de ductos?", "La suma de la longitud de sus tramos", "Los accesorios se cuentan aparte; la longitud suma los tramos."),
        ("En refrigeración: ¿qué se hace con una diferencia entre el plano y la lista de materiales?", "Se registra en un formulario y se informa al proyectista", "El revisor no corrige por su cuenta, porque no sabe cuál documento falla."),
        ("¿Cómo se deja constancia de la respuesta del proyectista?", "Por escrito, con fecha, archivada junto a los planos", "Un registro verbal no permite comprobar después qué se decidió."),
    ],
    op=("Caso de ejemplo «Bodega Pinares» (ficticia): red de ductos con tramos de 8 m, 5 m y 3 m unidos por 2 codos. La lista de materiales pide 16 m de ducto y 2 codos. Una cañería de agua cruza el tramo de 5 m. "
        "Escribe (a) la longitud total del plano, (b) la diferencia con la lista y qué documentos se contradicen, (c) qué haces con la cañería de agua, (d) qué datos escribirías en el formulario de consulta.",
        "(a) 8+5+3 son 16 m. (b) No hay diferencia en metros ni en codos: 16 m y 2 codos coinciden en el plano y la lista. (c) Es una interferencia; la informo al proyectista y no muevo la cañería por mi cuenta. (d) Qué elementos chocan (ducto y cañería), qué se observó, quién lo detectó y la fecha.",
        ["suma bien los tramos", "compara correctamente plano y lista", "informa la interferencia sin decidir por su cuenta", "completa los datos del formulario"],
        ["hoja con los cálculos y el borrador del formulario"],
        ["inventar una diferencia donde no la hay", "mover la cañería de agua sin consultar", "dejar el formulario sin fecha"],
        "Pregunta: «¿dónde queda registrada la respuesta del proyectista?». Si no responde, pídele que relea la regla del registro escrito."),
    reinforce="Inventa una red de tres tramos con sus longitudes y una lista de materiales con una diferencia, y escribe el hallazgo.",
    extend="Explica con un ejemplo por qué es mejor consultar por escrito que resolver una duda de planos con una conversación en la obra.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados). Sobre el cielo falso de una sala hay 60 cm de altura libre entre la losa y el cielo. Un ducto rectangular de ejemplo mide 40 cm de alto. "
     "El proyecto exige 5 cm de holgura sobre el ducto y 5 cm bajo él, y el soporte colgante ocupa 3 cm. En un cruce, una viga de 30 cm de alto cuelga bajo la losa. "
     "Los datos del relevamiento de la sala vienen en un informe de ejemplo hecho por personal autorizado.")
build(
    O1, 4, F,
    use="Aprenderé a comparar el espacio que necesita un ducto con el que existe en la obra y a decidir qué informar cuando no cabe.",
    prior=["Sé sumar y restar medidas en centímetros.", "Sé qué es una interferencia.", "Sé que los cambios los decide el proyectista."],
    explain=[
        "Un plano se dibuja en un papel, pero la obra tiene condiciones reales que pueden facilitar u obstaculizar el proyecto. Una de ellas es la altura libre: el espacio vertical disponible entre la losa y el cielo falso para pasar ductos. Para saber si un ducto cabe se calcula el espacio necesario y se compara con el disponible. El espacio necesario suma el alto del ducto, la holgura, que es el espacio libre mínimo que el proyecto exige alrededor, y el soporte que lo cuelga.",
        "Si el espacio necesario es menor o igual que el disponible, el ducto cabe. Si es mayor, hay una interferencia y se informa, con los datos, al proyectista. El relevamiento es la toma de datos del lugar y la hace personal autorizado; este cuaderno no enseña a medir en altura ni en techos. Nadie reduce una holgura, baja un cielo falso o corta un ducto por su cuenta: son cambios que decide y firma el proyectista.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("altura libre", "espacio vertical disponible entre la losa y el cielo falso"), ("holgura", "espacio libre mínimo que el proyecto exige alrededor de un ducto"), ("soporte", "pieza que sostiene un ducto o una cañería"), ("relevamiento", "toma de datos de las condiciones reales del lugar, hecha por personal autorizado"), ("cielo falso", "techo interior liviano que deja un espacio sobre él"), ("espacio necesario", "suma del alto del ducto, sus holguras y su soporte")],
    worked=[
        ("Espacio necesario", "Un ducto de ejemplo mide 25 cm de alto, necesita 4 cm de holgura arriba, 4 cm abajo y un soporte de 2 cm. ¿Cuánto espacio necesita?", ["Se suman el alto, las dos holguras y el soporte.", "25 más 4 más 4 más 2 son 35."], "35 cm"),
        ("Comparar con lo disponible", "Una altura libre de ejemplo es de 50 cm y el espacio necesario es de 35 cm. ¿Cabe y cuánto sobra?", ["Se compara lo necesario con lo disponible.", "35 es menor que 50, y 50 menos 35 son 15."], "Cabe y sobran 15 cm"),
    ],
    mistakes=[("Comparar solo el alto del ducto con la altura libre y olvidar holguras y soporte.", "El ducto necesita más espacio que su propio alto.", "Suma alto, holguras y soporte antes de comparar."),
              ("Reducir una holgura para que el ducto «quepa justo».", "La holgura la fija el proyecto y puede afectar la seguridad o el funcionamiento.", "Informa el problema; solo el proyectista cambia una holgura.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es la altura libre sobre un cielo falso?", "El espacio vertical disponible entre la losa y el cielo para pasar ductos", "La altura total del edificio", "El alto del ducto más grande de la red", "La altura libre es el espacio disponible para instalar; no es la altura del edificio ni del ducto."),
        ("abc", "En Refrigeración: ¿qué es la holgura de un ducto?", "El espacio libre mínimo que el proyecto exige alrededor del ducto", "El ancho de la sección del ducto", "El sobrante de material después de cortar", "La holgura es un espacio exigido por el proyecto, no una medida del ducto ni un sobrante."),
        ("abc", "¿Qué es un relevamiento de obra?", "La toma de datos de las condiciones reales del lugar, hecha por personal autorizado", "El dibujo de un plano nuevo para el cliente", "El conteo de los materiales comprados", "El relevamiento recoge datos reales del lugar; no dibuja planos ni cuenta compras."),
        ("=", "{F} ¿Cuántos centímetros de espacio necesita el ducto con sus holguras y su soporte?", "40+5+5+3", "Se suman el alto del ducto, las dos holguras y el soporte.", " cm"),
        ("=", "{F} En una zona sin viga, ¿cuántos centímetros sobran de la altura libre después de ubicar el ducto con sus holguras y su soporte?", "60-(40+5+5+3)", "Se resta el espacio necesario de la altura libre disponible.", " cm"),
        ("abc", "{F} ¿Cabe el ducto en el cruce con la viga?", "No: bajo la viga quedan 30 cm y el ducto necesita 53 cm", "Sí: la altura libre total es 60 cm y el ducto necesita 53 cm", "Sí, porque la viga se puede picar un poco", "Bajo la viga la altura libre baja a 30 cm, menos que los 53 cm necesarios."),
        ("=", "{F} Bajo la viga, ¿cuántos centímetros faltan para que quepa el ducto con sus holguras y su soporte?", "53-(60-30)", "Se resta el espacio disponible bajo la viga del espacio necesario.", " cm"),
        ("=", "{F} El proyectista cambia el ducto a uno de 30 cm de alto, con las mismas holguras y el mismo soporte. ¿Cuántos centímetros de espacio necesita ahora?", "30+5+5+3", "Se suman el nuevo alto, las dos holguras y el soporte.", " cm"),
        ("abc", "{F} Al comprobar que el ducto no cabe bajo la viga, ¿qué se hace?", "Anotar la interferencia con los datos y consultar al proyectista", "Bajar el cielo falso de toda la sala sin consultar", "Cortar el ducto en dos y dejarlo suelto bajo la viga", "Una interferencia se informa con datos; no se improvisan cambios de cielo ni de ducto."),
        ("abc", "{F} Un compañero propone reducir las holguras de 5 cm a 0 cm «para que quepa». ¿Qué respuesta es correcta?", "No: la holgura la fija el proyecto y solo el proyectista puede cambiarla", "Sí, si el ducto queda bien ajustado", "Sí, porque las holguras casi nunca se miden en la obra", "Cambiar una holgura altera lo que el proyecto exige y no lo decide quien ejecuta."),
        ("=", "{F} El soporte colgante pasa a ocupar 8 cm en lugar de 3 cm. En la zona sin viga, ¿cuántos centímetros sobran de los 60 cm de altura libre?", "60-(40+5+5+8)", "Se suma el nuevo soporte al espacio necesario y se resta de la altura libre.", " cm"),
        ("abc", "{F} Con el soporte de 8 cm sobran 2 cm, y el informe de relevamiento declara un posible error de 3 cm. ¿Qué conclusión es la más prudente?", "Hay riesgo de que no quepa: se informa y se verifica el dato antes de ejecutar", "Cabe, porque 2 cm son suficientes", "No importa, porque el error siempre favorece", "Si el posible error es mayor que lo que sobra, el resultado es incierto y se verifica."),
        ("=", "{F} Se estudia otro ducto de 48 cm de alto con las mismas holguras de 5 cm y un soporte de 3 cm. ¿Cuántos centímetros faltan para que quepa en la zona sin viga?", "(48+5+5+3)-60", "Se calcula el espacio necesario y se resta la altura libre de 60 cm.", " cm"),
    ],
    ctx=("abc", "Una jefa de obra de ejemplo descubre que el cielo falso quedó 6 cm más bajo que lo dibujado en el plano. ¿Qué hace?", "Registra la medida real y consulta al proyectista si el ducto sigue cabiendo", "Instala el ducto igual y espera que alcance", "Sube el cielo falso a golpes para recuperar los 6 cm", "Una diferencia entre plano y obra se registra con la medida real y se consulta antes de ejecutar."),
    sc=[
        ("En Refrigeración: ¿qué se suma para obtener el espacio necesario de un ducto?", "El alto del ducto, sus holguras y su soporte", "Con solo el alto no se sabe si el ducto cabe."),
        ("¿Qué se hace si el espacio necesario es mayor que el disponible?", "Se informa la interferencia con datos al proyectista", "Nadie reduce holguras ni corta ductos por su cuenta."),
        ("¿Quién realiza el relevamiento de las condiciones reales?", "Personal autorizado, que entrega un informe", "Medir en altura o en techos exige autorización y protección."),
    ],
    op=("Datos de ejemplo de la «Sala Andes» (ficticia): altura libre de 55 cm; ducto de 35 cm de alto; holguras de 4 cm arriba y 4 cm abajo; soporte de 2 cm; una viga de 25 cm de alto cuelga bajo la losa en un cruce. "
        "Escribe (a) el espacio necesario del ducto, (b) si cabe en la zona sin viga y cuánto sobra o falta, (c) cuánta altura libre queda bajo la viga y si el ducto cabe allí, (d) qué haces si no cabe y a quién informas.",
        "(a) 35+4+4+2 son 45 cm. (b) 55 menos 45: cabe y sobran 10 cm. (c) Bajo la viga quedan 55 menos 25, o sea 30 cm; como 45 es mayor que 30, no cabe y faltan 15 cm. (d) Anoto la interferencia con los datos y la informo al proyectista, que decide el cambio.",
        ["suma bien el espacio necesario", "compara con la altura libre", "calcula el espacio bajo la viga", "informa sin decidir por su cuenta"],
        ["hoja con los cálculos y la nota de interferencia"],
        ["olvidar las holguras o el soporte", "decir que reduciría una holgura", "no informar la interferencia"],
        "Pregunta: «¿qué datos incluyes al informar?». Si no responde, pídele que relea la parte de informar con datos."),
    reinforce="Inventa un ducto con su alto, holguras y soporte, y calcula si cabe en una altura libre que elijas.",
    extend="Explica con un ejemplo por qué una diferencia de pocos centímetros entre plano y obra puede cambiar la decisión sobre un ducto.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (alternativas de ejemplo, inventadas). Para llevar un ducto a una sala hay dos rutas. Ruta A: 14 m de ducto y 4 codos; cruza una viga, lo que exige una autorización estructural de $90.000. "
     "Ruta B: 19 m de ducto y 6 codos; sin cruces. Costos de ejemplo: ducto $4.500 por metro; codo $6.000 cada uno. Matriz de decisión de ejemplo, puntajes de 1 a 5 (5 es lo mejor): "
     "costo: A 2 y B 5; facilidad de mantención: A 3 y B 4; bajo riesgo en obra: A 2 y B 4. Pesos de los criterios: costo 3, mantención 1, riesgo 2.")
build(
    O1, 5, F,
    use="Aprenderé a comparar alternativas de ruta con costos y una matriz de decisión, y a verificar la calidad de un plano antes de usarlo.",
    prior=["Sé multiplicar y sumar costos.", "Sé qué es una interferencia.", "Sé que las decisiones se registran por escrito."],
    explain=[
        "Cuando hay dos o más rutas posibles se comparan con criterios, que son las características que importan: costo, facilidad de mantención, riesgo en obra. La matriz de decisión es una tabla que da un puntaje a cada alternativa en cada criterio. El peso de un criterio indica cuánto importa: el puntaje se multiplica por el peso y se suma. Gana la alternativa con mayor puntaje total, pero el costo real también se calcula aparte, con la longitud de ducto, la cantidad de accesorios y los extras.",
        "Antes de usar un plano se verifica su calidad con una lista de control: que tenga leyenda, escala, rótulo, firma del proyectista y la revisión vigente. La revisión es la versión del plano; usar una revisión antigua puede llevar a ejecutar algo que ya fue cambiado. La elección final la aprueba por escrito el proyectista; quien ejecuta no cambia de ruta por cuenta propia.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("criterio", "característica que se usa para comparar alternativas"), ("matriz de decisión", "tabla que da un puntaje a cada alternativa en cada criterio"), ("peso", "número que indica cuánto importa un criterio"), ("puntaje ponderado", "suma de cada puntaje multiplicado por el peso de su criterio"), ("revisión vigente", "versión más reciente y aprobada de un plano"), ("lista de control", "lista de puntos que se verifican uno por uno")],
    worked=[
        ("Puntaje ponderado", "En una matriz de ejemplo, la ruta M tiene puntaje 4 en costo (peso 2) y 3 en riesgo (peso 1). ¿Cuál es su puntaje ponderado?", ["Cada puntaje se multiplica por su peso: 4 por 2 y 3 por 1.", "8 más 3 son 11."], "11 puntos"),
        ("Costo de una ruta", "Una ruta de ejemplo usa 10 m de ducto a $3.000 el metro y 2 codos a $5.000 cada uno. ¿Cuánto cuesta?", ["El ducto cuesta 10 por 3.000 y los codos 2 por 5.000.", "30.000 más 10.000 son 40.000."], "$40.000"),
    ],
    mistakes=[("Elegir la ruta más corta sin mirar costos de accesorios ni riesgos.", "La longitud es solo un criterio; el costo y el riesgo también cuentan.", "Compara todos los criterios con su peso y calcula el costo total."),
              ("Usar un plano de una revisión antigua porque ya estaba impreso.", "La versión puede haber cambiado y llevar a ejecutar algo equivocado.", "Confirma con el proyectista cuál es la revisión vigente.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es una matriz de decisión?", "Una tabla que da un puntaje a cada alternativa en cada criterio", "Una tabla con los precios de los materiales de la obra", "Un plano con los símbolos de una red de ductos", "La matriz compara alternativas con puntajes; los precios van en el presupuesto y los símbolos en el plano."),
        ("abc", "En Refrigeración: ¿qué significa que un criterio tenga más peso que otro?", "Que influye más en el puntaje total de cada alternativa", "Que el material de ese criterio es más pesado", "Que se evalúa primero en la obra", "El peso mide la importancia del criterio en el puntaje, no la masa ni el orden."),
        ("abc", "¿Para qué sirve la revisión vigente indicada en el rótulo de un plano?", "Para saber que se trabaja con la versión más reciente aprobada", "Para saber cuánto cuesta el plano", "Para indicar la escala del dibujo", "La revisión identifica la versión del plano; el costo y la escala se indican en otros lugares."),
        ("=", "{F} ¿Cuánto cuesta el ducto de la ruta A (sin codos ni autorización)?", "14*4500", "Se multiplican los 14 metros por el valor de cada metro.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la ruta B, con ducto y codos?", "19*4500+6*6000", "Se suman el costo del ducto y el de los 6 codos.", " pesos"),
        ("=", "{F} ¿Cuál es el puntaje ponderado de la ruta A?", "2*3+3*1+2*2", "Cada puntaje de A se multiplica por el peso de su criterio y se suma.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje ponderado de la ruta B?", "5*3+4*1+4*2", "Cada puntaje de B se multiplica por el peso de su criterio y se suma.", " puntos"),
        ("=", "{F} ¿Cuál es el costo total de la ruta A, con ducto, codos y autorización estructural?", "14*4500+4*6000+90000", "Se suman el ducto, los 4 codos y la autorización estructural.", " pesos"),
        ("abc", "{F} Según los puntajes ponderados y los costos de la ficha, ¿qué ruta aparece mejor?", "La ruta B, con mayor puntaje y menor costo total", "La ruta A, porque es más corta", "Ninguna, porque hay empate", "B suma 27 puntos contra 13 de A y además cuesta menos."),
        ("abc", "{F} Un instalador dice: «la ruta A es más corta, así que es la mejor». ¿Qué respuesta es correcta?", "No necesariamente: la longitud es un criterio; también cuentan el costo total y el riesgo", "Sí: lo más corto siempre es lo mejor", "Sí, porque la matriz solo mide la longitud", "La matriz incluye varios criterios y el costo total muestra otra realidad."),
        ("=", "{F} ¿Cuánto ahorra la ruta B respecto de la ruta A en costo total?", "(14*4500+4*6000+90000)-(19*4500+6*6000)", "Se resta el costo total de B del costo total de A.", " pesos"),
        ("=", "{F} Si el proyectista cambia el peso del riesgo de 2 a 4, ¿cuál es el nuevo puntaje ponderado de la ruta A?", "2*3+3*1+2*4", "Se repite la suma de A con el peso del riesgo cambiado a 4.", " puntos"),
        ("abc", "El plano de una ruta tiene la revisión C impresa, pero existe una revisión D. ¿Qué corresponde antes de ejecutar?", "Confirmar con el proyectista cuál revisión está vigente y usar solo esa", "Usar la revisión C porque ya está impresa", "Mezclar datos de la revisión C con los de la D", "Se trabaja con la versión vigente; mezclar versiones lleva a errores."),
    ],
    ctx=("abc", "El dueño de un local de ejemplo quiere la ruta más barata aunque el plano muestre otra. ¿Qué responde el instalador?", "Que el cambio de ruta lo decide y lo aprueba por escrito el proyectista", "Que la cambia de inmediato porque el dueño paga", "Que la cambia y avisa cuando termine", "El que paga no reemplaza al proyectista: un cambio de ruta se aprueba por escrito."),
    sc=[
        ("En Refrigeración: ¿cómo se calcula un puntaje ponderado?", "Multiplicando cada puntaje por el peso de su criterio y sumando", "Así los criterios más importantes pesan más en el total."),
        ("¿Quién aprueba la ruta final de una red?", "El proyectista, por escrito", "Quien ejecuta no cambia de ruta por su cuenta."),
        ("¿Qué se verifica en un plano antes de usarlo?", "Leyenda, escala, rótulo, firma y revisión vigente", "Una lista de control evita usar planos incompletos o antiguos."),
    ],
    op=("Alternativas de ejemplo para el «Taller Lomas» (ficticio): ruta M con 10 m de ducto y 3 codos, ruta N con 13 m de ducto y 5 codos. Ducto a $3.000 el metro y codo a $5.000. Puntajes (1 a 5): costo M 4 y N 3; riesgo M 2 y N 5. Pesos: costo 2 y riesgo 3. "
        "Escribe (a) el costo total de cada ruta, (b) el puntaje ponderado de cada ruta, (c) qué ruta propondrías y por qué, (d) quién aprueba la elección y qué versión del plano usas.",
        "(a) M: 10 por 3.000 más 3 por 5.000 son 45.000. N: 13 por 3.000 más 5 por 5.000 son 64.000. (b) M: 4 por 2 más 2 por 3 son 14. N: 3 por 2 más 5 por 3 son 21. (c) Propondría N por su mayor puntaje, aunque cuesta más; lo informo con ambos datos. (d) Lo aprueba por escrito el proyectista y uso la revisión vigente.",
        ["calcula bien los costos", "calcula bien los puntajes ponderados", "justifica la propuesta con ambos datos", "indica quién aprueba y la revisión vigente"],
        ["hoja con los cálculos y la propuesta"],
        ["olvidar multiplicar por el peso", "elegir solo por costo", "decidir sin aprobación del proyectista"],
        "Pregunta: «¿quién decide la ruta final?». Si no responde, pídele que relea el papel del proyectista."),
    reinforce="Inventa dos rutas con sus metros y codos, ponles un costo y calcula cuál es más barata.",
    extend="Explica con un ejemplo por qué la ruta de menor costo no siempre es la que se recomienda.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Proyecto «Gimnasio Aurora» (ficticio): una sala de 12 m por 8 m con 3 m de altura, con ductos de aire y cañerías. El cómputo de materiales de ejemplo lista ducto, aislante, abrazaderas (piezas que sujetan) y rejillas. "
     "Una planilla de cálculo (programa que hace cuentas con los datos que se escriben) calcula las cantidades.")
build(
    O2, 1, F,
    use="Aprenderé qué es cubicar, para qué sirve, qué errores comete una planilla cuando los datos están mal y qué cuidados hay al manipular materiales.",
    prior=["Sé multiplicar medidas.", "Sé que un presupuesto reúne costos.", "Sé qué es un cómputo o lista de materiales."],
    explain=[
        "Cubicar es calcular cuántos elementos y materiales necesita una obra a partir de longitudes, superficies y volúmenes. El resultado se anota en un cómputo de materiales: una lista de partidas. Una partida es cada ítem de trabajo o de material, con su unidad y su cantidad. El cómputo sirve para presupuestar, comprar y programar la obra. Si la cantidad queda corta hay un faltante y la obra puede detenerse; si queda larga hay un sobrante y se gasta de más.",
        "Hoy las cantidades se calculan en una planilla de cálculo o en un programa de dibujo que las entrega solas. Pero el programa solo calcula lo que se le escribe: si un largo se anota con un cero de más, la cantidad sale mal igual. Por eso la persona revisa el orden de magnitud de cada resultado con una cuenta rápida a mano. Cada cantidad sale de un plano con su revisión vigente; si el plano cambia, la cubicación se rehace.",
        f"Los materiales de una obra pueden ser pesados o tener bordes filosos. Moverlos exige personal capacitado, EPP y las reglas de manipulación de cargas de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("cubicar", "calcular cuántos elementos y materiales necesita una obra a partir de longitudes, superficies y volúmenes"), ("cómputo de materiales", "lista de partidas con su unidad y su cantidad"), ("partida", "ítem de trabajo o de material dentro de un cómputo"), ("faltante", "cantidad que falta para completar lo que la obra necesita"), ("sobrante", "cantidad comprada que no se usa"), ("planilla de cálculo", "programa que hace cuentas con los datos que se escriben en sus celdas"), ("orden de magnitud", "tamaño aproximado de un resultado: decenas, cientos, miles")],
    worked=[
        ("Superficie de un piso", "Una bodega de ejemplo mide 7 m por 5 m. ¿Cuántos m² tiene su piso?", ["La superficie de un rectángulo es largo por ancho.", "7 por 5 son 35."], "35 m²"),
        ("Detectar un dato mal escrito", "Una planilla de ejemplo entrega 3.500 m² de piso para la bodega de 7 m por 5 m. ¿Qué se sospecha?", ["Se compara con la cuenta rápida: 7 por 5 son 35.", "3.500 es cien veces mayor: se sospecha un dato escrito con ceros de más."], "Un error en los datos de entrada, que debe revisarse"),
    ],
    mistakes=[("Comprar lo que dice la planilla sin revisar el orden de magnitud.", "El programa no detecta un dato escrito con un cero de más.", "Haz una cuenta rápida a mano y compara."),
              ("Mover planchas con bordes filosos sin EPP para ahorrar tiempo.", "Hay riesgo de cortes y de lesiones por carga.", "Pide que lo haga personal capacitado, con EPP y según las reglas de manipulación.")],
    T=[
        ("abc", "En Refrigeración: ¿qué significa cubicar los materiales de una obra?", "Calcular cuántos elementos y materiales se necesitan a partir de longitudes, superficies y volúmenes", "Dibujar el plano de las redes de la obra", "Comprar los materiales al precio más bajo posible", "Cubicar es calcular cantidades; dibujar planos y comparar precios son otras tareas."),
        ("abc", "¿Qué es una partida en un cómputo de materiales?", "Un ítem de trabajo o de material con su unidad y su cantidad", "La fecha en que parte la obra", "El total de dinero del presupuesto", "La partida es cada fila del cómputo, no una fecha ni el total de dinero."),
        ("abc", "¿Qué problema causa un faltante de materiales en una obra?", "La obra puede detenerse hasta comprar lo que falta", "Se gasta dinero en materiales que no se usan", "El plano pierde su escala", "El faltante detiene el trabajo; el gasto de más es efecto del sobrante."),
        ("=", "{F} ¿Cuántos m² tiene el piso de la sala?", "12*8", "La superficie de un rectángulo es largo por ancho.", " m²"),
        ("=", "{F} ¿Cuántos m³ de aire contiene la sala?", "12*8*3", "El volumen de un prisma es largo por ancho por alto.", " m³"),
        ("abc", "{F} El programa entrega 960 m² de piso porque se escribió el largo como 120 m en vez de 12 m. ¿Qué debe concluir la persona?", "El dato de largo se escribió mal: hay que revisarlo antes de comprar", "El piso mide 960 m² porque el programa lo calculó", "El programa nunca se equivoca, así que se compra lo que dice", "Un resultado diez veces mayor que la cuenta rápida de 96 m² indica un dato de entrada mal escrito."),
        ("=", "{F} La empresa cobra $2.300 por m² de piso por instalar la climatización. ¿Cuánto cobra por la sala?", "12*8*2300", "Se multiplica la superficie del piso por el valor de cada m².", " pesos"),
        ("abc", "{F} Un bodeguero mueve sin protección unas planchas de metal con bordes filosos «para ahorrar tiempo». ¿Qué corresponde?", "Que lo haga personal capacitado, con EPP y según las reglas de manipulación", "Seguir sin EPP si son pocas planchas", "Pedir a un cliente que ayude a cargarlas", "Los bordes filosos y el peso exigen EPP y personal capacitado, sin importar la cantidad."),
        ("=", "{F} Se pierde 1 día de trabajo por cada 8 abrazaderas que faltan, y faltan 24. Si un día de trabajo cuesta $120.000, ¿cuánto cuesta el retraso?", "24//8*120000", "Se calculan los días perdidos y se multiplican por el costo de cada día.", " pesos"),
        ("ab", "{F} Un compañero dice: «como usamos una planilla de cálculo, no hace falta revisar los resultados». ¿Es correcto?", "No: la planilla solo calcula lo escrito; hay que revisar el orden de magnitud", "Sí: una planilla de cálculo no se equivoca nunca", "El programa no detecta datos mal escritos; la persona sigue siendo responsable de revisar."),
        ("abc", "{F} El cómputo dice 300 m² de piso para esta sala y la persona sospecha un error. ¿Qué comprobación rápida le sirve?", "Multiplicar largo por ancho: 12 por 8 da cerca de 100 m², no 300", "Sumar el largo y el ancho de la sala", "Multiplicar largo, ancho y alto de la sala", "El piso es una superficie: largo por ancho; el alto da el volumen y la suma no corresponde."),
        ("=", "{F} El cielo de la sala se cubre con planchas de aislante de 2 m² cada una, sin considerar sobrantes. ¿Cuántas planchas se necesitan?", "12*8//2", "La superficie del cielo es igual a la del piso y se divide por lo que cubre cada plancha.", " planchas"),
        ("abc", "Una cubicación se hizo con el plano de la revisión B, pero el proyectista ya emitió la revisión C. ¿Qué corresponde?", "Verificar o rehacer la cubicación con la revisión vigente antes de comprar", "Comprar igual y corregir después si sobra", "Sumar un 50 % de material para cubrir cualquier cambio", "Una cubicación vale para la revisión con que se hizo; otra revisión puede cambiar las cantidades."),
    ],
    ctx=("abc", "Una jefa de obra de ejemplo recibe una planilla con una cantidad que le parece exagerada para una sala pequeña. ¿Qué hace?", "Pide verificar los datos de entrada antes de comprar", "Compra todo porque la planilla viene de la oficina", "Compra la mitad, por si acaso", "Un resultado dudoso se verifica en sus datos; comprar a ciegas o recortar sin calcular no corrige el error."),
    sc=[
        ("En Refrigeración: ¿para qué sirve un cómputo de materiales?", "Para presupuestar, comprar y programar la obra con cantidades calculadas", "El cómputo reúne las cantidades que la obra necesita."),
        ("¿Qué hace la persona con el resultado de una planilla?", "Revisa su orden de magnitud con una cuenta rápida a mano", "La planilla solo calcula los datos que se le escriben."),
        ("¿Quién mueve materiales pesados o con bordes filosos?", "Personal capacitado, con EPP y según las reglas de manipulación", "Este cuaderno no habilita para trabajar ni para intervenir equipos."),
    ],
    op=("Datos de ejemplo del «Salón Maitén» (ficticio): sala de 9 m por 6 m y 3 m de alto. Una planilla entrega 5.400 m² de piso. Cada rejilla cuesta $8.000 y se piden 5. "
        "Escribe (a) la superficie del piso calculada a mano, (b) si el resultado de la planilla es razonable y qué sospechas, (c) cuánto cuestan las rejillas, (d) quién debe mover las rejillas si son pesadas y con qué protección.",
        "(a) 9 por 6 son 54 m². (b) 5.400 es cien veces mayor que 54: sospecho un dato de entrada con ceros de más y lo reviso antes de comprar. (c) 5 por 8.000 son 40.000 pesos. (d) Personal capacitado, con EPP y según las reglas de manipulación de cargas.",
        ["calcula la superficie", "detecta el resultado no razonable", "calcula el costo", "indica quién mueve la carga y con qué protección"],
        ["hoja con las cuatro respuestas y los cálculos"],
        ["confiar en la planilla sin revisar", "sumar en vez de multiplicar", "decir que cualquiera mueve cargas pesadas"],
        "Pregunta: «¿cómo sabes que 5.400 m² no es razonable?». Si no responde, pídele que relea la cuenta rápida a mano."),
    reinforce="Inventa una sala con largo y ancho, calcula su superficie a mano y escribe qué resultado de planilla te haría sospechar un error.",
    extend="Explica con un ejemplo por qué un faltante puede costar más que un sobrante pequeño.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (datos de ejemplo, inventados). Un ducto rectangular tiene una sección de 50 cm por 30 cm y un largo de 25 m. El aislante se vende en planchas de 2 m² y se agrega una merma de 10 %. "
     "Un recinto mide 6 m por 5 m y 3 m de alto. Fórmulas: perímetro de un rectángulo = 2 × (largo + ancho); superficie = largo × ancho; volumen de un prisma = largo × ancho × alto.")
build(
    O2, 2, F,
    use="Aprenderé a calcular perímetros, superficies y volúmenes con sus unidades, a convertir centímetros en metros y a agregar la merma.",
    prior=["Sé multiplicar y dividir.", "Sé que 100 cm son 1 m.", "Sé qué es cubicar."],
    explain=[
        "Para cubicar se usan tres medidas. El perímetro es el largo del contorno de una figura y se mide en metros (m). La superficie es el espacio que cubre una cara y se mide en metros cuadrados (m²). El volumen es el espacio que ocupa un cuerpo y se mide en metros cúbicos (m³). El aislante que envuelve un ducto cubre su superficie lateral: perímetro de la sección por largo del ducto. Antes de multiplicar, todas las medidas deben estar en la misma unidad: para pasar de centímetros a metros se divide por 100.",
        "La merma es la cantidad extra que se agrega por cortes y pérdidas, y se expresa como porcentaje. Si una obra necesita 50 m² y la merma es de 20 %, se agrega el 20 % de 50, que es 10 m², y se compran 60 m². El volumen de aire de un recinto sirve para estimar un caudal: el caudal se mide en metros cúbicos por hora (m³/h) y se obtiene multiplicando el volumen por las renovaciones por hora, que son las veces que se cambia todo el aire en una hora.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("perímetro", "largo del contorno de una figura; se mide en metros"), ("superficie", "espacio que cubre una cara; se mide en metros cuadrados (m²)"), ("volumen", "espacio que ocupa un cuerpo; se mide en metros cúbicos (m³)"), ("merma", "cantidad extra que se agrega por cortes y pérdidas, expresada como porcentaje"), ("sección", "forma que se ve al cortar un ducto de punta"), ("caudal", "volumen de aire que se mueve en una hora; se mide en m³/h"), ("renovaciones por hora", "veces que se cambia todo el aire de un recinto en una hora")],
    worked=[
        ("Perímetro y superficie", "Un panel de ejemplo mide 4 m por 3 m. ¿Cuál es su perímetro y su superficie?", ["Perímetro: 2 por (4 más 3), que son 14 m.", "Superficie: 4 por 3, que son 12 m²."], "Perímetro 14 m y superficie 12 m²"),
        ("Agregar merma", "Una obra de ejemplo necesita 50 m² de un material y la merma es de 20 %. ¿Cuántos m² se compran?", ["El 20 % de 50 es 10.", "50 más 10 son 60."], "60 m²"),
    ],
    mistakes=[("Multiplicar centímetros por metros sin convertir.", "La unidad queda mezclada y la cantidad sale mal.", "Convierte todo a metros antes de multiplicar."),
              ("Calcular el aislante de un ducto con el área de su sección en vez de su perímetro.", "El aislante envuelve el contorno a lo largo del ducto, no cubre la sección.", "Multiplica el perímetro de la sección por el largo del ducto.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es la merma de un material?", "La cantidad extra que se agrega por cortes y pérdidas", "El precio que se descuenta por comprar en cantidad", "El material que sobra siempre y se devuelve al proveedor", "La merma se agrega a lo calculado para cubrir cortes y pérdidas; no es descuento ni devolución."),
        ("abc", "¿En qué unidad se expresa el volumen de aire de un recinto?", "En metros cúbicos (m³)", "En metros cuadrados (m²)", "En metros (m)", "El volumen mide espacio ocupado y se expresa en metros cúbicos."),
        ("abc", "¿Qué fórmula da el perímetro de un rectángulo?", "2 × (largo + ancho)", "largo × ancho", "largo × ancho × alto", "El perímetro es el contorno; largo por ancho es la superficie y con el alto se obtiene el volumen."),
        ("=", "{F} ¿Cuántos centímetros mide el perímetro de la sección del ducto?", "2*(50+30)", "Se suman el largo y el ancho de la sección y se multiplica por 2.", " cm"),
        ("=", "{F} ¿Cuántos m² de aislante cubren el exterior del ducto (perímetro de la sección por el largo)?", "160*25//100", "Se multiplica el perímetro de 160 cm por 25 m y se divide por 100 para pasar los centímetros a metros.", " m²"),
        ("=", "{F} ¿Cuántos m² tiene el piso del recinto de 6 m por 5 m?", "6*5", "La superficie de un rectángulo es largo por ancho.", " m²"),
        ("=", "{F} ¿Cuántos m³ de aire contiene el recinto?", "6*5*3", "El volumen es largo por ancho por alto.", " m³"),
        ("=", "{F} Sin considerar la merma, ¿cuántas planchas de 2 m² se necesitan para los 40 m² del ducto?", "40//2", "Se divide la superficie por lo que cubre cada plancha.", " planchas"),
        ("=", "{F} Con la merma de 10 % sobre los 40 m² del ducto, ¿cuántos m² de aislante se deben comprar?", "40+40*10//100", "Se calcula el 10 % de 40 y se suma a los 40 m².", " m²"),
        ("abc", "{F} Un compañero calcula el aislante del ducto multiplicando solo 50 por 30. ¿Cuál es su error?", "Debe usar el perímetro de la sección por el largo del ducto", "Debe sumar 50 y 30 sin multiplicar", "Debe multiplicar por la altura del recinto", "Multiplicar 50 por 30 da el área de la sección, que no es la superficie que se envuelve."),
        ("=", "{F} El recinto necesita 4 renovaciones por hora (valor de ejemplo). ¿Cuántos m³ de aire por hora debe mover el sistema?", "6*5*3*4", "Se multiplica el volumen del recinto por las renovaciones por hora.", " m³/h"),
        ("=", "{F} Con la merma de 10 %, ¿cuántas planchas de 2 m² se deben comprar para el ducto?", "(40+40*10//100)//2", "Se calculan los m² con merma y se dividen por lo que cubre cada plancha.", " planchas"),
        ("abc", "{F} El proyectista cambia el largo del ducto de 25 m a 30 m. ¿Qué debe hacerse con la cubicación?", "Recalcular la superficie y las planchas con el largo nuevo", "Mantenerla, porque la merma cubre la diferencia", "Agregar 5 planchas sin calcular", "Un cambio de largo cambia la superficie; la cantidad se recalcula y no se estima."),
    ],
    ctx=("abc", "Una bodeguera de ejemplo recibe una medida en centímetros y la planilla pide metros. ¿Qué hace?", "Convierte la medida a metros antes de calcular", "Escribe el número tal cual, porque da igual", "Redondea la medida a la decena más cercana", "La planilla supone la unidad pedida; escribir centímetros donde van metros deja la cantidad cien veces mayor."),
    sc=[
        ("En Refrigeración: ¿cómo se obtiene la superficie lateral de un ducto?", "Perímetro de la sección por largo del ducto", "El aislante envuelve el contorno del ducto a lo largo."),
        ("¿Cómo se pasa de centímetros a metros?", "Dividiendo por 100", "Un metro tiene 100 centímetros, por eso se divide por 100."),
        ("En Refrigeración: ¿qué es la merma?", "La cantidad extra que se agrega por cortes y pérdidas", "Se expresa como porcentaje de lo calculado."),
    ],
    op=("Datos de ejemplo de la «Sala Boldo» (ficticia): ducto de sección 40 cm por 30 cm y largo de 20 m; aislante en planchas de 2 m²; merma de 25 %. Recinto de 8 m por 4 m y 3 m de alto con 5 renovaciones por hora. "
        "Escribe (a) el perímetro de la sección en cm, (b) los m² de aislante sin merma, (c) las planchas que se compran con merma, (d) el caudal de aire en m³/h.",
        "(a) 2 por (40+30) son 140 cm. (b) 140 por 20 son 2.800 y, dividido por 100, son 28 m². (c) El 25 % de 28 son 7; 28 más 7 son 35 m²; 35 dividido por 2 da 17 y sobra 1, por lo que se compran 18 planchas. (d) 8 por 4 por 3 son 96 m³, por 5 renovaciones: 480 m³/h.",
        ["calcula el perímetro", "calcula la superficie con unidades", "agrega la merma y redondea hacia arriba", "calcula el caudal"],
        ["hoja con los cálculos"],
        ["no convertir centímetros a metros", "usar el área de la sección", "redondear hacia abajo las planchas"],
        "Pregunta: «¿por qué se compran 18 y no 17 planchas?». Si no responde, pídele que relea cómo se redondea una cantidad de compra."),
    reinforce="Inventa un ducto con sección y largo, y calcula los m² de aislante con una merma de 10 %.",
    extend="Explica con un ejemplo por qué hay que convertir las unidades antes de multiplicar dos medidas.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Una cañería se compone de tres tramos: A de 15 m, B de 10 m y C de 8 m. Se vende en barras de 6 m a $9.000 cada una. "
     "Regla de la obra de ejemplo: el sobrante de una barra no se reutiliza en otro tramo. El aislante de la cañería se vende en tiras de 2 m a $2.500 cada una y también se cubica por tramo. "
     "Además se necesitan 5 codos a $1.200 cada uno.")
build(
    O2, 3, F,
    use="Aprenderé a cubicar barras, tiras y accesorios de una cañería, redondeando hacia arriba y aplicando la regla de sobrantes de la obra.",
    prior=["Sé calcular superficies y la merma.", "Sé dividir con resto.", "Sé qué es un tramo."],
    explain=[
        "Los materiales lineales, como las cañerías y sus tiras de aislante, se compran en piezas de largo fijo. Para saber cuántas piezas se necesitan se divide el largo del tramo por el largo de la pieza y el resultado se redondea hacia arriba, porque no se compran fracciones de pieza. Un truco de cálculo: se suma al largo el largo de la pieza menos 1 y se hace la división entera. Por ejemplo, 7 m con piezas de 3 m: (7 + 2) ÷ 3 = 3 piezas.",
        "La regla de sobrantes decide si el resto de una pieza se puede usar en otro tramo. Si la obra no lo permite, cada tramo se calcula por separado y las piezas se suman; si lo permite, se divide el largo total. La regla se escribe en las especificaciones y la cubicación la respeta, aunque sea más cara. Los accesorios, como los codos, se cuentan uno a uno. El costo total suma piezas lineales y accesorios.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("pieza", "elemento de largo fijo que se compra completo, como una barra o una tira"), ("barra", "pieza recta de cañería de largo fijo"), ("tira de aislante", "pieza de aislante de largo fijo que cubre una cañería"), ("regla de sobrantes", "regla que dice si el resto de una pieza puede usarse en otro tramo"), ("redondear hacia arriba", "pasar a la cantidad entera siguiente cuando hay resto"), ("división entera", "división que entrega solo la parte entera del resultado")],
    worked=[
        ("Piezas de un tramo", "Un tramo de ejemplo mide 11 m y las barras miden 4 m. ¿Cuántas barras se necesitan?", ["11 dividido por 4 da 2 y sobran 3 metros.", "Se redondea hacia arriba: 3 barras."], "3 barras"),
        ("Costo de piezas", "Una obra de ejemplo compra 5 barras a $7.000 y 3 codos a $900. ¿Cuánto cuesta?", ["Las barras cuestan 5 por 7.000, que son 35.000.", "Los codos cuestan 3 por 900, que son 2.700; el total es 37.700."], "$37.700"),
    ],
    mistakes=[("Redondear hacia abajo el número de barras.", "Quedaría un trozo de tramo sin cañería.", "Redondea hacia arriba cuando hay resto."),
              ("Dividir el largo total ignorando la regla de sobrantes.", "La obra puede no permitir reutilizar el resto de una barra.", "Aplica la regla de las especificaciones tramo por tramo.")],
    T=[
        ("abc", "En Refrigeración: ¿por qué el número de barras se redondea hacia arriba?", "Porque no se compran fracciones de barra y hay que cubrir todo el largo", "Porque la merma siempre es de 10 %", "Porque redondear hacia abajo dejaría barras de más", "Si hay resto, la cantidad entera menor no alcanza para cubrir el tramo."),
        ("abc", "¿Qué dice la regla de sobrantes de una obra?", "Si el resto de una pieza puede usarse o no en otro tramo", "Cuánto cuesta cada barra de cañería", "Qué día termina la obra", "La regla fija si el resto se reutiliza; no habla de precios ni de plazos."),
        ("abc", "¿Qué es una tira de aislante en una cubicación?", "Una pieza de aislante de largo fijo que cubre una cañería", "Un tramo de cañería sin aislar", "Una abrazadera que sujeta la cañería", "La tira es una pieza de aislante; la abrazadera es un soporte y el tramo sin aislar es lo contrario."),
        ("=", "{F} ¿Cuántos metros de cañería suman los tres tramos?", "15+10+8", "Se suman las longitudes de los tres tramos.", " m"),
        ("=", "{F} ¿Cuántas barras de 6 m se necesitan para el tramo A?", "(15+5)//6", "Se suma 5 al largo y se divide por 6 para redondear hacia arriba.", " barras"),
        ("=", "{F} Aplicando la regla de la obra (sin reutilizar sobrantes), ¿cuántas barras se necesitan para los tres tramos?", "(15+5)//6+(10+5)//6+(8+5)//6", "Se calcula cada tramo por separado y se suman las barras.", " barras"),
        ("=", "{F} ¿Cuánto cuestan las barras de la regla de la obra?", "7*9000", "Se multiplican las 7 barras por su precio unitario.", " pesos"),
        ("=", "{F} Si el sobrante se pudiera reutilizar entre tramos, ¿cuántas barras de 6 m cubrirían los 33 m?", "(33+5)//6", "Se divide el largo total, sumando 5, por el largo de la barra.", " barras"),
        ("=", "{F} Aplicando la regla de la obra, ¿cuántas tiras de aislante de 2 m se necesitan para los tres tramos?", "(15+1)//2+(10+1)//2+(8+1)//2", "Se calcula cada tramo por separado y se redondea hacia arriba con tiras de 2 m.", " tiras"),
        ("abc", "{F} Un compañero dice que bastan 6 barras «porque 33 dividido en 6 da 5,5 y se redondea». ¿Qué responde según la regla de la obra?", "Que con la regla de no reutilizar sobrantes se necesitan 7 barras", "Que se necesitan 5 barras", "Que se necesitan 8 barras", "Con la regla de la obra, cada tramo usa barras completas: 3, 2 y 2."),
        ("=", "{F} ¿Cuál es el costo total de barras, tiras de aislante y codos?", "7*9000+17*2500+5*1200", "Se suman el costo de las 7 barras, de las 17 tiras y de los 5 codos.", " pesos"),
        ("=", "{F} Otro proveedor ofrece barras de 5 m a $7.500. Con la misma regla, ¿cuánto costarían las barras de los tres tramos?", "((15+4)//5+(10+4)//5+(8+4)//5)*7500", "Se calculan las barras de 5 m por tramo, se suman y se multiplican por el precio.", " pesos"),
        ("abc", "{F} La planilla muestra 70 barras para esta cañería. ¿Qué corresponde?", "Revisar los datos de entrada: para 33 m, 70 barras es un resultado desproporcionado", "Comprar las 70 barras porque lo dice la planilla", "Dividir 70 por 2 y comprar esas barras", "Un resultado diez veces mayor que lo esperable indica un dato mal escrito, no una compra."),
    ],
    ctx=("abc", "Una compradora de ejemplo ve que una barra sobrante del tramo B sirve para completar el tramo C, pero la regla de la obra lo prohíbe. ¿Qué hace?", "Respeta la regla y consulta al proyectista si cree que conviene cambiarla", "Usa el sobrante igual, para ahorrar", "Usa el sobrante y lo oculta en la cubicación", "La regla está en las especificaciones; solo el proyectista puede cambiarla."),
    sc=[
        ("En Refrigeración: ¿cómo se calcula el número de barras de un tramo?", "Dividiendo el largo por el de la barra y redondeando hacia arriba", "No se compran fracciones de barra."),
        ("¿Qué se hace con los accesorios en una cubicación?", "Se cuentan uno a uno", "Los accesorios no se miden en metros."),
        ("¿Quién cambia la regla de sobrantes de una obra?", "El proyectista, por escrito", "Quien cubica solo aplica la regla escrita en las especificaciones."),
    ],
    op=("Datos de ejemplo de la «Bodega Roble» (ficticia): tramos de cañería de 14 m y 9 m; barras de 6 m a $8.000; regla: no se reutilizan sobrantes; 3 codos a $1.500. "
        "Escribe (a) las barras de cada tramo, (b) el total de barras y su costo, (c) el costo de los codos y el costo total, (d) qué harías si la planilla entregara 40 barras.",
        "(a) 14: (14+5)//6 son 3 barras; 9: (9+5)//6 son 2 barras. (b) 5 barras, que cuestan 40.000. (c) Los codos cuestan 4.500; el total es 44.500. (d) Revisaría los datos de entrada, porque 40 barras es desproporcionado para 23 m.",
        ["calcula las barras por tramo", "suma y calcula costos", "respeta la regla de sobrantes", "detecta el resultado desproporcionado"],
        ["hoja con los cálculos"],
        ["redondear hacia abajo", "dividir el total ignorando la regla", "comprar sin revisar un resultado desproporcionado"],
        "Pregunta: «¿por qué cada tramo se calcula por separado?». Si no responde, pídele que relea la regla de sobrantes."),
    reinforce="Inventa dos tramos de cañería y calcula las barras que necesitas con barras de 3 m y regla de no reutilizar sobrantes.",
    extend="Explica con un ejemplo cuándo una regla de sobrantes más estricta aumenta el costo de una cubicación.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada, escrita en papel). Partida / unidad / cantidad / precio unitario: ducto / m / 25 / $4.500; aislante / m² / 40 / $3.000; codo / un / 6 / $6.000; rejilla / un / 4 / $8.000; abrazadera / un / 30 / $500. "
     "La fila de total de la planilla dice $300.500. Se acordó reservar un 5 % de imprevistos sobre el total correcto. «un» significa unidad.")
build(
    O2, 4, F,
    use="Aprenderé a leer una planilla de cubicación con subtotales y total, a detectar errores de fórmula o de unidad y a agregar imprevistos.",
    prior=["Sé multiplicar cantidades por precios.", "Sé sumar columnas.", "Sé calcular porcentajes simples."],
    explain=[
        "Una planilla de cubicación tiene una fila por partida, con su unidad, su cantidad y su precio unitario. El subtotal de una fila es la cantidad por el precio unitario, y el total es la suma de todos los subtotales. Los programas calculan esas cuentas con fórmulas, pero una fórmula puede estar mal escrita: por ejemplo, un total que no incluye todas las filas sale menor que el real. También pueden mezclarse unidades, como sumar metros con metros cuadrados.",
        "Para verificar una planilla se recalcula a mano un subtotal y el total, se comparan las unidades y se revisa que cada precio coincida con la lista de precios vigente. Los imprevistos son un porcentaje del total que se reserva para gastos que no se pueden prever; el porcentaje lo acuerda quien aprueba el presupuesto y se calcula sobre el total correcto. Cuando existen dos versiones con totales distintos, se identifica la vigente por su fecha y su revisión.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("subtotal", "cantidad por precio unitario de una fila"), ("total", "suma de todos los subtotales"), ("fórmula", "regla que una planilla usa para calcular un valor a partir de otros"), ("precio unitario", "precio de una unidad de una partida"), ("imprevistos", "porcentaje del total que se reserva para gastos que no se pueden prever"), ("versión vigente", "versión más reciente y aprobada de un documento")],
    worked=[
        ("Subtotal y total", "Una planilla de ejemplo tiene 10 m de ducto a $2.000 y 4 rejillas a $5.000. ¿Cuál es el total?", ["Ducto: 10 por 2.000, que son 20.000. Rejillas: 4 por 5.000, que son 20.000.", "El total suma ambos subtotales: 40.000."], "$40.000"),
        ("Detectar una omisión", "Una planilla de ejemplo tiene 10 m de ducto a $2.000 y 4 rejillas a $5.000, pero su fila de total muestra $20.000. ¿Qué pasó?", ["El total correcto es 40.000.", "El total mostrado coincide con un solo subtotal: la fórmula omitió una fila."], "La fórmula del total omitió una fila"),
    ],
    mistakes=[("Confiar en el total de la planilla sin recalcular ningún subtotal.", "Una fórmula incompleta no avisa y el total sale menor que el real.", "Recalcula a mano un subtotal y el total antes de usarlos."),
              ("Calcular los imprevistos sobre un total con error.", "El error se arrastra al presupuesto.", "Corrige primero el total y luego aplica el porcentaje.")],
    T=[
        ("abc", "En Refrigeración: ¿cómo se obtiene el subtotal de una fila de un cómputo?", "Multiplicando la cantidad por el precio unitario", "Sumando la cantidad y el precio unitario", "Dividiendo el precio unitario por la cantidad", "El subtotal es cantidad por precio; sumarlos o dividirlos no da el costo de la partida."),
        ("abc", "¿Qué ocurre si la fórmula del total no incluye todas las filas?", "El total sale menor que la suma real", "El total sale mayor que la suma real", "Cambian los precios unitarios", "Al omitir filas se suman menos subtotales, por lo que el total queda corto."),
        ("abc", "¿Para qué se reserva un porcentaje de imprevistos?", "Para cubrir gastos que no se pueden prever, según un criterio acordado", "Para dar un descuento al cliente", "Para compensar errores de cálculo sin corregirlos", "Los imprevistos cubren lo no previsible; no reemplazan la corrección de errores."),
        ("=", "{F} ¿Cuál es el subtotal de la fila de aislante?", "40*3000", "Se multiplica la cantidad por el precio unitario.", " pesos"),
        ("=", "{F} ¿Cuál es el subtotal de la fila de ducto?", "25*4500", "Se multiplica la cantidad por el precio unitario.", " pesos"),
        ("=", "{F} ¿Cuál es el total correcto de la planilla?", "25*4500+40*3000+6*6000+4*8000+30*500", "Se suman los cinco subtotales de las filas.", " pesos"),
        ("=", "{F} El total de la planilla dice $300.500. ¿Cuántos pesos faltan respecto del total correcto?", "(25*4500+40*3000+6*6000+4*8000+30*500)-300500", "Se resta el total mostrado del total correcto.", " pesos"),
        ("abc", "{F} ¿Qué fila omitió la fórmula del total de $300.500?", "La de abrazaderas, cuyo subtotal es $15.000", "La de rejillas, cuyo subtotal es $32.000", "La de codos, cuyo subtotal es $36.000", "La diferencia entre el total correcto y el mostrado es 15.000, igual al subtotal de las abrazaderas."),
        ("=", "{F} ¿Cuánto son los imprevistos del 5 % sobre el total correcto?", "(25*4500+40*3000+6*6000+4*8000+30*500)*5//100", "Se calcula el 5 % del total correcto.", " pesos"),
        ("abc", "{F} Un compañero cambia el precio del codo de $6.000 a $600 por un cero de menos. ¿Cómo se detecta?", "Comparando el precio con la lista vigente y recalculando el subtotal", "No se puede detectar sin comprar los codos", "Sumando los precios sin multiplicar por las cantidades", "Un precio fuera de la lista vigente aparece al verificarlo y al recalcular el subtotal."),
        ("abc", "{F} La planilla suma en una misma columna los metros del ducto con los m² del aislante. ¿Cuál es el problema?", "Mezcla unidades distintas, que no deben sumarse", "Ninguno, porque ambas unidades llevan la letra m", "Falta una fila de totales", "Metros y metros cuadrados miden cosas diferentes y no se suman entre sí."),
        ("=", "{F} Si el precio del aislante sube de $3.000 a $3.400 por m², ¿cuánto sube el total?", "40*(3400-3000)", "Se multiplica el alza por m² por los 40 m² de aislante.", " pesos"),
        ("abc", "{F} Dos versiones de la planilla tienen totales distintos y nadie sabe cuál es la última. ¿Qué corresponde?", "Identificar la versión vigente por fecha y revisión y verificar los subtotales antes de comprar", "Comprar según la versión que dé el total más bajo", "Promediar los dos totales y usar ese valor", "Una compra se hace con la versión vigente y verificada, no con un valor inventado."),
    ],
    ctx=("abc", "Una asistente de ejemplo recibe de un programa de dibujo una cantidad de 4.000 m de ducto para una sala de 90 m². ¿Qué hace?", "Desconfía del orden de magnitud y revisa unidades y datos antes de comprar", "Compra 4.000 m porque el programa lo calculó", "Divide la cantidad por 2 para quedar más tranquila", "Un resultado desproporcionado se revisa en sus datos; recortarlo a ojo no corrige el error."),
    sc=[
        ("En Refrigeración: ¿cómo se calcula el total de una planilla de cubicación?", "Sumando los subtotales de todas las filas", "Cada subtotal es cantidad por precio unitario."),
        ("¿Qué se verifica a mano en una planilla?", "Un subtotal, el total y las unidades", "Una fórmula incompleta no avisa del error."),
        ("¿Cómo se identifica la versión vigente de un cómputo?", "Por su fecha y su revisión", "Así no se compra con una versión antigua."),
    ],
    op=("Planilla de ejemplo del «Local Quillay» (ficticio): ducto 18 m a $4.500; aislante 30 m² a $3.000; rejilla 3 un a $8.000. La fila de total dice $145.000. Se reserva un 10 % de imprevistos. "
        "Escribe (a) el subtotal de cada partida, (b) el total correcto, (c) qué error tiene el total mostrado y cuánto falta, (d) los imprevistos sobre el total correcto.",
        "(a) Ducto: 18 por 4.500 son 81.000; aislante: 30 por 3.000 son 90.000; rejillas: 3 por 8.000 son 24.000. (b) 195.000. (c) El total mostrado es 145.000: faltan 50.000, y no coincide con ninguna fila; hay un error de fórmula o de dato que se revisa. (d) El 10 % de 195.000 son 19.500.",
        ["calcula los subtotales", "suma el total", "detecta y cuantifica el error", "calcula los imprevistos sobre el total correcto"],
        ["hoja con los cálculos y el hallazgo"],
        ["usar el total mostrado para los imprevistos", "mezclar unidades", "no cuantificar la diferencia"],
        "Pregunta: «¿sobre qué total calculas los imprevistos?». Si no responde, pídele que relea la regla de corregir primero el total."),
    reinforce="Inventa una planilla de tres partidas con cantidades y precios, y calcula subtotales y total.",
    extend="Explica con un ejemplo qué le pasa a un presupuesto cuando la fórmula del total omite una fila.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (tabla de magnitudes, de ejemplo). Magnitud / unidad / instrumento: temperatura / °C / termómetro; presión / kPa / manómetro; humedad relativa / % / higrómetro; caudal de aire / m³/h / medidor de caudal; "
     "tensión eléctrica / V / voltímetro; corriente eléctrica / A / amperímetro; energía / kWh / medidor de energía. Datos de ejemplo: un equipo de 3 kW funciona 5 horas al día; la tarifa de ejemplo es de $150 por kWh.")
build(
    O3, 1, F,
    use="Aprenderé qué magnitudes se miden en un sistema de climatización, con qué unidades e instrumentos, por qué se verifican y por qué medir en equipos reales exige autorización.",
    prior=["Sé multiplicar.", "Sé que una unidad acompaña a cada medida.", "Sé qué es una especificación técnica."],
    explain=[
        "Medir es comparar una magnitud con una unidad usando un instrumento. En climatización y refrigeración se miden la temperatura (°C), la presión (kPa), la humedad relativa (%), el caudal de aire (m³/h), la tensión eléctrica (V), la corriente eléctrica (A) y la energía (kWh). Un kilovatio-hora (kWh) es la energía que usa un equipo de 1 kW funcionando 1 hora. Un control de verificación compara una lectura con el valor que fija la especificación técnica o el fabricante, para saber si el sistema cumple.",
        "Las mediciones sirven para la seguridad, para que el sistema funcione como se diseñó, para controlar el consumo de energía y para proteger el medio ambiente. Medir en un equipo real tiene riesgos: energía eléctrica, presión, piezas que giran y, a veces, altura. Por eso lo hace solo personal autorizado, con norma vigente y EPP. Este cuaderno no enseña a medir ni a conectar instrumentos: trabaja con lecturas ya registradas, de ejemplo. Nunca se libera refrigerante al ambiente: ante una fuga se avisa.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("magnitud", "propiedad que se puede medir, como la temperatura o la presión"), ("unidad", "patrón con que se expresa una medida, como °C o kPa"), ("presión", "fuerza que ejerce un fluido sobre una superficie; se mide en kPa"), ("humedad relativa", "porcentaje de vapor de agua que tiene el aire respecto del máximo que podría tener a esa temperatura"), ("caudal", "volumen de aire que se mueve en una hora; se mide en m³/h"), ("kWh", "energía que usa un equipo de 1 kW funcionando 1 hora"), ("verificación", "comparación de una lectura con el valor que fija la especificación o el fabricante")],
    worked=[
        ("Aire movido", "Un caudal de ejemplo de 600 m³/h funciona 3 horas. ¿Cuántos m³ de aire mueve?", ["El caudal se multiplica por las horas.", "600 por 3 son 1.800."], "1.800 m³"),
        ("Energía en kWh", "Un equipo de ejemplo de 2 kW funciona 4 horas. ¿Cuántos kWh usa?", ["La energía es potencia por horas.", "2 por 4 son 8."], "8 kWh"),
    ],
    mistakes=[("Medir en un equipo real porque se conoce el nombre del instrumento.", "Conocer el instrumento no habilita a trabajar con energía ni con presión.", "Practica solo con instructor autorizado y norma vigente."),
              ("Cambiar una unidad por otra sin convertir, como kW por kWh.", "El kW es potencia y el kWh es energía en un tiempo.", "Revisa qué magnitud es cada unidad antes de calcular.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es una verificación?", "Comparar una lectura con el valor que fija la especificación o el fabricante", "Dibujar de nuevo el plano de la instalación", "Comprar un instrumento más preciso", "Verificar es comparar lo medido con lo exigido; dibujar planos o comprar instrumentos son otras tareas."),
        ("abc", "¿Qué magnitud mide un higrómetro?", "La humedad relativa del aire", "La temperatura del aire", "El caudal de aire", "El higrómetro mide humedad relativa; la temperatura y el caudal tienen otros instrumentos."),
        ("abc", "¿En qué unidad se expresa el caudal de aire?", "En m³/h", "En kPa", "En kWh", "El caudal es volumen por hora; kPa mide presión y kWh energía."),
        ("=", "{F} ¿Cuántos kWh consume el equipo de 3 kW en un día de 5 horas?", "3*5", "La energía es la potencia por las horas de funcionamiento.", " kWh"),
        ("=", "{F} ¿Cuánto cuesta la energía del equipo en un día, a la tarifa de ejemplo?", "3*5*150", "Se multiplican los kWh del día por el precio de cada kWh.", " pesos"),
        ("abc", "{F} ¿Qué instrumento corresponde a la corriente eléctrica?", "El amperímetro", "El voltímetro", "El manómetro", "La corriente se mide en amperes con un amperímetro; el voltímetro mide tensión y el manómetro presión."),
        ("=", "{F} En un mes de 20 días de trabajo, ¿cuántos kWh consume el equipo?", "3*5*20", "Se multiplican los kWh diarios por los días del mes.", " kWh"),
        ("abc", "{F} Un ayudante sin autorización quiere conectar un voltímetro a un equipo en marcha «solo para practicar». ¿Qué corresponde?", "No hacerlo: medir en equipos reales lo hace personal autorizado, con norma vigente y EPP", "Hacerlo si usa guantes", "Hacerlo si el supervisor está en otra sala", "Los guantes o la ausencia del supervisor no reemplazan la autorización ni la norma vigente."),
        ("=", "{F} Un caudal de ejemplo de 800 m³/h funciona 6 horas. ¿Cuántos m³ de aire mueve?", "800*6", "Se multiplica el caudal por las horas de funcionamiento.", " m³"),
        ("abc", "{F} Un compañero dice: «si la lectura está lejos del valor de la especificación, ajusto el equipo yo mismo». ¿Qué respuesta es correcta?", "Debe registrar la lectura e informar al supervisor; ajustar equipos lo hace personal autorizado", "Puede ajustarlo si tiene herramientas", "Debe ignorar la lectura y seguir midiendo", "Registrar e informar permite decidir con respaldo; ajustar sin autorización es riesgoso."),
        ("abc", "Durante una revisión se percibe un olor extraño y se sospecha una fuga de refrigerante. ¿Qué indican las reglas generales?", "No acercarse ni tocar, avisar a un adulto responsable y a emergencias", "Acercarse para ver de dónde sale", "Seguir con las mediciones y avisar al terminar", "Ante una fuga no se entra ni se improvisa: se avisa de inmediato."),
        ("=", "{F} Si la tarifa de ejemplo sube de $150 a $180 por kWh, ¿cuánto sube el costo de un mes de 20 días de funcionamiento del equipo?", "3*5*20*(180-150)", "Se multiplica el consumo mensual en kWh por el alza de cada kWh.", " pesos"),
        ("abc", "{F} El equipo consume 15 kWh al día y la especificación de ejemplo fija un máximo de 12 kWh al día. ¿Qué corresponde registrar?", "Que el consumo supera el máximo en 3 kWh al día y se informa al supervisor", "Que el consumo es correcto porque el equipo funciona", "Que debe cambiarse la tarifa", "Una lectura sobre el máximo es una diferencia que se registra e informa."),
    ],
    ctx=("abc", "Un técnico de ejemplo anota una potencia «3 kWh» donde el instrumento mostraba 3 kW. ¿Qué error cometió?", "Confundió potencia (kW) con energía (kWh)", "Escribió bien, porque son la misma unidad", "Confundió la temperatura con la presión", "El kW mide potencia y el kWh energía en un tiempo; no son equivalentes."),
    sc=[
        ("En Refrigeración: ¿qué es medir?", "Comparar una magnitud con una unidad usando un instrumento", "La medida expresa cuánto vale la magnitud en esa unidad."),
        ("¿Quién mide en un equipo real?", "Personal autorizado, con norma vigente y EPP", "Este cuaderno no enseña a medir ni a conectar instrumentos."),
        ("¿Qué se hace ante una fuga de refrigerante?", "No acercarse ni tocar, y avisar a un adulto responsable y a emergencias", "Nunca se improvisa ante una fuga."),
    ],
    op=("Datos de ejemplo de la «Sala Copihue» (ficticia): un equipo de 4 kW funciona 6 horas al día; tarifa de ejemplo de $140 por kWh; la especificación fija un máximo de 20 kWh al día. "
        "Escribe (a) los kWh diarios, (b) el costo diario, (c) si cumple el máximo y cuántos kWh se pasa o le sobran, (d) quién mide el consumo en el equipo real.",
        "(a) 4 por 6 son 24 kWh. (b) 24 por 140 son 3.360 pesos. (c) No cumple: se pasa por 4 kWh, lo registro e informo al supervisor. (d) Personal autorizado, con norma vigente y EPP.",
        ["calcula los kWh", "calcula el costo", "compara con el máximo y registra la diferencia", "indica quién mide"],
        ["hoja con los cálculos y el registro"],
        ["confundir kW con kWh", "no informar la diferencia", "decir que mediría el equipo real"],
        "Pregunta: «¿qué haces con la diferencia de 4 kWh?». Si no responde, pídele que relea la parte de registrar e informar."),
    reinforce="Escribe tres magnitudes, la unidad de cada una y el instrumento con que se mide.",
    extend="Explica con un ejemplo por qué una lectura sin unidad no sirve para verificar un sistema.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (certificados de ejemplo, inventados). Termómetro T1: rango de −30 a 50 °C, resolución 1 °C, calibración vigente. Termómetro T2: rango de 0 a 100 °C, resolución 2 °C, calibración vigente. "
     "Termómetro T3: rango de −30 a 50 °C, resolución 1 °C, calibración vencida. Una verificación de ejemplo pide medir una temperatura esperada de 22 °C con una tolerancia de ±1 °C.")
build(
    O3, 2, F,
    use="Aprenderé a elegir un instrumento según su rango, su resolución y su calibración, y a leer una tolerancia y un certificado.",
    prior=["Sé qué es una verificación.", "Sé restar y sumar números enteros.", "Sé que una medida lleva unidad."],
    explain=[
        "Un instrumento se describe con tres datos. El rango es el intervalo de valores que puede medir, de un mínimo a un máximo. La resolución es el menor cambio que el instrumento distingue; una resolución de 2 °C solo diferencia saltos de 2 en 2. La calibración es la comparación del instrumento con un patrón de referencia, y su certificado dice el error del instrumento y hasta cuándo es vigente. Con la calibración vencida, la lectura no tiene respaldo y no se usa para decidir.",
        "La tolerancia es la diferencia máxima aceptada entre la lectura y el valor esperado; se escribe, por ejemplo, ±3 °C alrededor de un valor. Para verificar con seguridad, el rango del instrumento debe incluir el valor esperado, su resolución debe ser más fina que la tolerancia y su calibración debe estar vigente. El error de un instrumento es la diferencia entre lo que marca y el valor del patrón. Toda lectura queda registrada con el instrumento que se usó.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("rango", "intervalo de valores que un instrumento puede medir"), ("resolución", "menor cambio que un instrumento distingue"), ("calibración", "comparación del instrumento con un patrón de referencia"), ("certificado de calibración", "documento que dice el error del instrumento y hasta cuándo es vigente"), ("tolerancia", "diferencia máxima aceptada entre la lectura y el valor esperado"), ("error del instrumento", "diferencia entre lo que marca y el valor del patrón"), ("patrón de referencia", "instrumento muy confiable con que se compara otro")],
    worked=[
        ("Valor mínimo y máximo", "Un valor esperado de ejemplo es 15 °C con una tolerancia de ±3 °C. ¿Entre qué valores se acepta la lectura?", ["El mínimo es 15 menos 3, que son 12.", "El máximo es 15 más 3, que son 18."], "Entre 12 °C y 18 °C"),
        ("Elegir por rango", "Un instrumento de ejemplo mide de 0 a 40 °C. ¿Sirve para un valor esperado de 55 °C?", ["El valor esperado debe estar dentro del rango.", "55 es mayor que 40: queda fuera."], "No sirve: 55 °C queda fuera de su rango"),
    ],
    mistakes=[("Usar un instrumento con calibración vencida porque «se ve bien».", "Sin calibración vigente no se sabe cuánto se equivoca.", "Revisa la fecha del certificado y usa uno vigente."),
              ("Elegir un instrumento cuya resolución es mayor que la tolerancia.", "No puede distinguir diferencias tan pequeñas como las que se necesita comprobar.", "Elige una resolución más fina que la tolerancia.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es el rango de un instrumento de medición?", "El intervalo de valores que puede medir, de un mínimo a un máximo", "El menor cambio que el instrumento distingue", "La fecha hasta la que está calibrado", "El rango es el intervalo medible; el menor cambio es la resolución y la fecha pertenece al certificado."),
        ("abc", "¿Qué es la calibración de un instrumento?", "Compararlo con un patrón de referencia y registrar su error", "Cambiarle las pilas antes de usarlo", "Limpiarlo después de cada medición", "Calibrar es comparar con un patrón; la limpieza o las pilas no determinan su error."),
        ("abc", "¿Qué es la tolerancia en una verificación?", "La diferencia máxima aceptada entre la lectura y el valor esperado", "El tiempo máximo que puede durar la medición", "La cantidad de lecturas que deben tomarse", "La tolerancia fija cuánto puede alejarse la lectura del valor esperado."),
        ("abc", "{F} ¿Qué termómetro corresponde usar para la verificación?", "T1: su rango incluye 22 °C, su resolución es 1 °C y su calibración está vigente", "T2: su rango incluye 22 °C y su calibración está vigente", "T3: su rango incluye 22 °C y su resolución es 1 °C", "T2 tiene resolución mayor que la tolerancia y T3 tiene la calibración vencida."),
        ("abc", "{F} ¿Por qué no sirve T2 para esta verificación?", "Su resolución de 2 °C es mayor que la tolerancia de 1 °C", "Su rango no incluye 22 °C", "Su calibración está vencida", "T2 solo distingue saltos de 2 °C, por lo que no puede comprobar ±1 °C."),
        ("abc", "{F} ¿Por qué no se usa T3 para esta verificación?", "Su calibración está vencida, así que la lectura no tiene respaldo", "Su rango es demasiado pequeño", "Su resolución es de 2 °C", "T3 tiene rango y resolución adecuados, pero un certificado vencido invalida su lectura."),
        ("=", "{F} ¿Cuál es el valor mínimo aceptado en la verificación?", "22-1", "Se resta la tolerancia del valor esperado.", " °C"),
        ("=", "{F} ¿Cuál es el valor máximo aceptado en la verificación?", "22+1", "Se suma la tolerancia al valor esperado.", " °C"),
        ("=", "{F} El termómetro T1 lee 24 °C. ¿Cuántos °C excede el máximo aceptado?", "24-(22+1)", "Se resta el máximo aceptado de la lectura.", " °C"),
        ("abc", "{F} Un compañero dice: «T3 se ve bien, así que sirve para medir». ¿Qué respuesta es correcta?", "No: sin calibración vigente, la lectura no tiene respaldo", "Sí: si se ve bien, mide correctamente", "Sí, pero solo si el supervisor no pregunta", "La apariencia no prueba que mida bien; lo prueba un certificado vigente."),
        ("=", "En una comparación de ejemplo, el patrón de referencia marca 20 °C y el instrumento marca 22 °C. ¿Cuál es el error del instrumento?", "22-20", "El error es lo que marca el instrumento menos el valor del patrón.", " °C"),
        ("=", "{F} Si un instrumento tiene un error de 3 °C y la tolerancia de la verificación es de ±1 °C, ¿cuántos °C supera el error a la tolerancia?", "3-1", "Se resta la tolerancia del error del instrumento.", " °C"),
        ("abc", "{F} Un registro de lecturas no indica qué instrumento se usó. ¿Qué problema tiene?", "No se puede comprobar si el instrumento tenía calibración vigente", "Ninguno, porque las lecturas bastan", "Que se midió en una hora equivocada", "Sin saber qué instrumento se usó no se puede confiar en la lectura."),
    ],
    ctx=("abc", "Una supervisora de ejemplo recibe lecturas hechas con un instrumento cuyo certificado venció la semana pasada. ¿Qué hace?", "No usa esas lecturas para decidir y pide repetirlas con un instrumento calibrado", "Las usa porque el vencimiento fue reciente", "Las usa, pero baja la tolerancia para compensar", "Una calibración vencida invalida la lectura, aunque haya vencido hace poco."),
    sc=[
        ("En Refrigeración: ¿qué dice el certificado de calibración?", "El error del instrumento y hasta cuándo es vigente", "Sin certificado vigente, la lectura no tiene respaldo."),
        ("¿Qué debe cumplir la resolución respecto de la tolerancia?", "Ser más fina que la tolerancia", "Así el instrumento puede distinguir diferencias pequeñas."),
        ("¿Qué se escribe junto a cada lectura registrada?", "El instrumento que se usó", "Así se puede comprobar su calibración."),
    ],
    op=("Instrumentos de ejemplo de la «Planta Cipreses» (ficticia): P1, rango 0 a 60 °C, resolución 1 °C, calibración vigente; P2, rango 0 a 60 °C, resolución 5 °C, calibración vigente; P3, rango 0 a 30 °C, resolución 1 °C, calibración vigente. Valor esperado de 40 °C, tolerancia ±2 °C. "
        "Escribe (a) el rango de lecturas aceptadas, (b) qué instrumento usarías y por qué, (c) por qué descartas los otros dos, (d) qué haces si el certificado del instrumento elegido estuviera vencido.",
        "(a) De 38 °C a 42 °C. (b) P1: su rango incluye 40 °C, su resolución de 1 °C es más fina que ±2 °C y su calibración está vigente. (c) P2 tiene resolución de 5 °C, mayor que la tolerancia; P3 llega solo hasta 30 °C y no incluye 40 °C. (d) No uso sus lecturas y pido uno con calibración vigente.",
        ["calcula el rango aceptado", "elige P1 con las tres razones", "descarta P2 y P3 con su motivo", "no usa lecturas con calibración vencida"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el rango", "ignorar la resolución", "usar un instrumento vencido"],
        "Pregunta: «¿por qué no sirve P2?». Si no responde, pídele que relea la regla de resolución y tolerancia."),
    reinforce="Escribe con tus palabras qué es el rango, la resolución y la calibración de un instrumento.",
    extend="Explica con un ejemplo por qué un instrumento con buena resolución puede no servir si su calibración está vencida.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (planilla de lecturas, de ejemplo, inventada). Temperatura del aire de una sala; valor esperado de ejemplo 22 °C con tolerancia ±2 °C. Lecturas: 08:00 21 °C; 10:00 23 °C; 12:00 25 °C; 14:00 22 °C; 16:00 20 °C; 18:00 21 °C. "
     "Instrumento: termómetro con calibración vigente. Criterio de ejemplo: la verificación se aprueba si todas las lecturas están dentro de la tolerancia.")
build(
    O3, 3, F,
    use="Aprenderé a leer una planilla de lecturas, a detectar lecturas fuera de tolerancia, a calcular promedio y extremos, y a registrar sin adulterar datos.",
    prior=["Sé qué es una tolerancia.", "Sé sumar y dividir con números enteros.", "Sé qué es una verificación."],
    explain=[
        "Una planilla de lecturas registra la hora, la lectura, el valor esperado y el estado de cada medición. Una lectura es conforme si está dentro de la tolerancia y no conforme si queda fuera; la no conformidad es el incumplimiento de un requisito. Para resumir se calculan el promedio, que es la suma de las lecturas dividida por su cantidad, el máximo y el mínimo, y la diferencia entre ellos, que muestra cuánto varió la magnitud.",
        "El criterio de aprobación se define antes de medir y está en la especificación. Cuando una lectura no conforme aparece, quien registra no la corrige ni ajusta el equipo: la anota tal como es e informa al supervisor, que decide si se repite la verificación. Cambiar un número para que la planilla apruebe es adulterar un registro, una falta grave que puede ocultar un riesgo. Un promedio dentro de la tolerancia no compensa una lectura fuera de ella.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("planilla de lecturas", "tabla donde se anotan hora, lectura, valor esperado y estado de cada medición"), ("conforme", "lectura que está dentro de la tolerancia"), ("no conformidad", "incumplimiento de un requisito, como una lectura fuera de tolerancia"), ("promedio", "suma de las lecturas dividida por su cantidad"), ("adulterar un registro", "cambiar un dato registrado para que parezca que se cumple"), ("criterio de aprobación", "regla que dice cuándo una verificación se considera aprobada")],
    worked=[
        ("Contar lecturas conformes", "Con valor esperado 20 °C y tolerancia ±1 °C, un registro de ejemplo trae 19, 21 y 22 °C. ¿Cuántas lecturas son conformes?", ["Se aceptan valores entre 19 y 21 °C.", "19 y 21 son conformes; 22 queda fuera."], "2 lecturas conformes"),
        ("Calcular un promedio", "Tres lecturas de ejemplo son 18, 20 y 22 °C. ¿Cuál es el promedio?", ["Se suman las lecturas: 60.", "60 dividido por 3 son 20."], "20 °C"),
    ],
    mistakes=[("Corregir una lectura fuera de tolerancia para que la planilla apruebe.", "Adulterar un registro oculta un posible riesgo y es una falta grave.", "Anótala tal como está e informa al supervisor."),
              ("Aprobar porque el promedio está dentro de la tolerancia.", "Una lectura fuera de tolerancia es una no conformidad aunque el promedio sea bueno.", "Aplica el criterio de aprobación a cada lectura.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es una no conformidad en una verificación?", "Un incumplimiento de un requisito, como una lectura fuera de la tolerancia", "Una lectura exactamente igual al valor esperado", "Un instrumento con certificado vigente", "La no conformidad es incumplir un requisito; una lectura igual al esperado o un certificado vigente son conformes."),
        ("abc", "¿Qué hace quien detecta una lectura fuera de tolerancia?", "La registra tal como es e informa al supervisor", "La corrige para que la planilla apruebe", "La borra y mide de nuevo sin avisar", "Registrar e informar permite decidir con respaldo; corregir o borrar es adulterar."),
        ("abc", "¿Qué es adulterar un registro?", "Cambiar un dato registrado para que parezca que se cumple", "Anotar una lectura con su unidad", "Archivar la planilla con su fecha", "Adulterar es falsear un dato registrado; anotar con unidad o archivar es buena práctica."),
        ("=", "{F} ¿Cuál es el valor mínimo aceptado de la sala?", "22-2", "Se resta la tolerancia del valor esperado.", " °C"),
        ("=", "{F} ¿Cuál es el valor máximo aceptado de la sala?", "22+2", "Se suma la tolerancia al valor esperado.", " °C"),
        ("abc", "{F} ¿Qué lectura queda fuera de la tolerancia?", "La de las 12:00, con 25 °C", "La de las 10:00, con 23 °C", "La de las 16:00, con 20 °C", "El máximo aceptado es 24 °C; 20 °C está justo en el límite inferior y es conforme."),
        ("=", "{F} ¿Cuál es el promedio de las seis lecturas?", "(21+23+25+22+20+21)//6", "Se suman las seis lecturas y se dividen por 6.", " °C"),
        ("=", "{F} ¿Cuál es la diferencia entre la lectura máxima y la mínima?", "25-20", "Se resta la lectura mínima de la máxima.", " °C"),
        ("=", "{F} ¿Cuántos °C sobrepasa el máximo aceptado la lectura de las 12:00?", "25-(22+2)", "Se resta el máximo aceptado de la lectura de las 12:00.", " °C"),
        ("abc", "{F} Según el criterio de ejemplo, ¿se aprueba la verificación?", "No: una lectura quedó fuera de tolerancia", "Sí: el promedio es igual al valor esperado", "Sí: cinco de seis lecturas son conformes", "El criterio exige que todas las lecturas estén dentro de la tolerancia."),
        ("abc", "{F} Un compañero cambia el 25 por un 24 en la planilla «para que apruebe». ¿Qué es eso?", "Adulterar un registro, una falta grave que debe informarse", "Corregir un error de ortografía", "Una práctica aceptable si el supervisor no se entera", "Cambiar un dato real para aprobar es falsear el registro y oculta un posible riesgo."),
        ("=", "{F} Las lecturas conformes son todas menos una. ¿Cuántos °C suman esas lecturas conformes?", "132-25", "Se resta de la suma de todas las lecturas la que está fuera de tolerancia.", " °C"),
        ("abc", "{F} Antes de repetir la verificación, el supervisor pide confirmar el instrumento. ¿Qué dato del certificado debe revisar?", "Que su calibración esté vigente", "Que su color coincida con el de otros instrumentos", "Que haya sido comprado recientemente", "La vigencia de la calibración respalda las lecturas; el color o la fecha de compra no."),
    ],
    ctx=("abc", "Una asistente de ejemplo ve que la última lectura de una planilla está fuera de tolerancia y el equipo parece funcionar normal. ¿Qué hace?", "Registra la lectura real e informa al supervisor", "La omite porque el equipo parece normal", "La cambia por el valor esperado", "Aunque el equipo parezca normal, la lectura real se registra e informa."),
    sc=[
        ("En Refrigeración: ¿cómo se calcula el promedio de las lecturas?", "Sumándolas y dividiendo por su cantidad", "El promedio resume las lecturas en un solo valor."),
        ("¿Qué se hace con una lectura no conforme?", "Se registra tal cual y se informa al supervisor", "No se corrige ni se ajusta el equipo por cuenta propia."),
        ("¿Basta con que el promedio esté en tolerancia para aprobar?", "No: el criterio se aplica a cada lectura", "Un promedio bueno no compensa una lectura fuera de tolerancia."),
    ],
    op=("Planilla de ejemplo de la «Sala de ensayo Peumo» (ficticia, solo un cuadro en papel): valor esperado 10 °C, tolerancia ±2 °C; lecturas a las 09:00, 11:00, 13:00 y 15:00: 9, 12, 13 y 10 °C. Criterio de ejemplo: se aprueba si todas las lecturas son conformes. "
        "Escribe (a) el rango aceptado, (b) qué lecturas son conformes y cuál no, (c) el promedio, (d) si se aprueba la verificación y qué haces con la lectura no conforme.",
        "(a) De 8 °C a 12 °C. (b) 9, 12 y 10 son conformes; 13 está fuera. (c) 9+12+13+10 son 44, y 44 dividido por 4 son 11 °C. (d) No se aprueba, porque una lectura queda fuera; la registro tal como es e informo al supervisor, sin cambiarla.",
        ["calcula el rango aceptado", "identifica la lectura no conforme", "calcula el promedio", "aplica el criterio y no adultera el registro"],
        ["hoja con las cuatro respuestas"],
        ["aprobar por el promedio", "cambiar la lectura fuera de tolerancia", "equivocar el límite del rango"],
        "Pregunta: «¿por qué no aprueba aunque el promedio sea 11 °C?». Si no responde, pídele que relea el criterio de aprobación."),
    reinforce="Inventa cuatro lecturas con un valor esperado y una tolerancia, y marca cuáles son conformes.",
    extend="Explica con un ejemplo por qué adulterar un registro puede ocultar un riesgo para las personas.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (hoja de verificación de ejemplo, inventada). El manual de ejemplo de un fabricante ficticio indica que la diferencia de temperatura del aire (ΔT = temperatura del aire de retorno menos la del aire de impulsión) debe estar entre 6 y 10 °C. "
     "Registros: equipo E1, retorno 27 °C e impulsión 19 °C; equipo E2, retorno 26 °C e impulsión 23 °C; equipo E3, retorno 28 °C e impulsión 17 °C. E1 funciona con 2 kW durante 8 horas al día por 25 días; tarifa de ejemplo de $150 por kWh. "
     "El certificado del instrumento usado en E2 está vencido. Equivalencia: 1 kPa son 1000 Pa.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio de verificación con datos de ejemplo: calcular un ΔT, compararlo con el rango del fabricante, estimar el consumo y decidir qué informar.",
    prior=["Sé qué es una tolerancia y un rango.", "Sé calcular kWh.", "Sé que una lectura necesita un instrumento calibrado."],
    explain=[
        "La diferencia de temperatura del aire, o ΔT, es la resta entre la temperatura del aire de retorno, que es el que vuelve al equipo, y la del aire de impulsión, que es el que sale hacia el recinto. Es una forma de ver si el equipo está enfriando como se espera. Cada fabricante indica en su manual el rango correcto de ΔT para su equipo, y ese es el único valor válido: no se usa el de memoria ni el de otro equipo.",
        "Para decidir se calcula el ΔT, se compara con el rango y se revisa la calidad del dato: si el instrumento tiene la calibración vencida, la lectura no sirve. Un ΔT fuera de rango no se interpreta por cuenta propia: se informa al supervisor, que decide con personal autorizado. El consumo se estima con kWh, que es potencia por horas, y su costo con la tarifa. Las presiones se registran en la unidad que pide la hoja: 1 kPa son 1000 pascales (Pa). Si hay olor, humo o ruido anormal, primero la seguridad.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("ΔT", "diferencia de temperatura: retorno menos impulsión"), ("aire de retorno", "aire que vuelve del recinto hacia el equipo"), ("aire de impulsión", "aire que sale del equipo hacia el recinto"), ("manual del fabricante", "documento que indica los valores correctos de cada equipo"), ("pascal (Pa)", "unidad de presión; 1 kPa equivale a 1000 Pa"), ("lectura confiable", "lectura hecha con un instrumento de calibración vigente")],
    worked=[
        ("Calcular un ΔT", "Un equipo de ejemplo tiene retorno a 25 °C e impulsión a 18 °C. ¿Cuál es su ΔT?", ["El ΔT es retorno menos impulsión.", "25 menos 18 son 7."], "7 °C"),
        ("Comparar con el rango", "El manual de ejemplo de otro equipo pide un ΔT entre 5 y 9 °C y el equipo tiene 7 °C. ¿Cumple?", ["Se compara con el rango del manual.", "7 está entre 5 y 9."], "Sí, cumple"),
    ],
    mistakes=[("Usar un rango de ΔT recordado de otro equipo.", "Cada equipo tiene sus propios valores en su manual.", "Usa el rango del manual del equipo que se verifica."),
              ("Usar una lectura hecha con un instrumento sin calibración vigente.", "No se sabe cuánto error tiene.", "Pide repetir la lectura con un instrumento calibrado.")],
    T=[
        ("abc", "En Refrigeración: ¿qué es el ΔT del aire de un equipo?", "La resta entre la temperatura del aire de retorno y la del aire de impulsión", "La suma de las temperaturas de entrada y de salida", "La potencia que consume el equipo", "El ΔT es una diferencia de temperaturas; no es una suma ni una potencia."),
        ("abc", "¿Qué hace una persona si el certificado del instrumento está vencido?", "No usa esa lectura para decidir e informa para repetirla con un instrumento calibrado", "La usa igual si el equipo parece normal", "La corrige restándole un valor estimado", "Sin calibración vigente la lectura no tiene respaldo y se repite."),
        ("abc", "¿Por qué se usa el rango del manual del fabricante y no uno recordado de otro equipo?", "Porque cada equipo tiene sus propios valores en su manual", "Porque los manuales son más baratos que los instrumentos", "Porque todos los equipos tienen siempre el mismo rango", "Los valores correctos dependen del diseño de cada equipo."),
        ("=", "{F} ¿Cuántos °C vale el ΔT del equipo E1?", "27-19", "Se resta la temperatura de impulsión de la de retorno.", " °C"),
        ("=", "{F} ¿Cuántos °C vale el ΔT del equipo E3?", "28-17", "Se resta la temperatura de impulsión de la de retorno.", " °C"),
        ("abc", "{F} ¿Qué equipo tiene un ΔT dentro del rango del manual?", "E1, con un ΔT de 8 °C", "E2, con un ΔT de 3 °C", "E3, con un ΔT de 11 °C", "Solo E1 queda entre 6 y 10 °C; E2 queda debajo y E3 encima."),
        ("=", "{F} ¿Cuántos °C le faltan al ΔT de E2 para llegar al mínimo del rango?", "6-(26-23)", "Se resta el ΔT de E2 del mínimo del rango.", " °C"),
        ("=", "{F} ¿Cuántos kWh consume E1 en los 25 días?", "2*8*25", "Se multiplican los kW, las horas diarias y los días.", " kWh"),
        ("=", "{F} ¿Cuánto cuesta la energía de E1 en esos 25 días, a la tarifa de ejemplo?", "2*8*25*150", "Se multiplican los kWh del período por la tarifa de cada kWh.", " pesos"),
        ("abc", "{F} E2 tiene un ΔT bajo y además el certificado de su instrumento está vencido. ¿Qué conclusión corresponde?", "La lectura no es confiable: se informa y se repite con un instrumento calibrado, por personal autorizado", "El equipo está averiado y debe desarmarse", "El ΔT es correcto porque está cerca del rango", "Con un certificado vencido no se puede concluir nada; se repite con respaldo."),
        ("abc", "{F} Un compañero dice que E3 está «mejor» porque su ΔT de 11 °C enfría más. ¿Qué respuesta es correcta?", "Está fuera del rango del fabricante y se informa, aunque parezca enfriar más", "Está mejor, porque un ΔT mayor siempre es bueno", "Está igual que E1, porque ambos enfrían", "El criterio es el rango del manual, no cuánto parece enfriar."),
        ("=", "{F} Una presión de ejemplo de 250 kPa debe registrarse en una hoja que pide pascales. ¿Cuántos Pa son?", "250*1000", "Se multiplica por 1000, porque 1 kPa equivale a 1000 Pa.", " Pa"),
        ("abc", "{F} Mientras se revisa la hoja de E3, alguien nota olor extraño y humo cerca del equipo. ¿Qué corresponde?", "Primero la seguridad: no acercarse ni tocar, avisar a un adulto responsable y a emergencias", "Terminar de anotar la hoja de verificación antes de avisar", "Acercarse a comprobar de dónde viene el humo", "Con humo u olor extraño no se entra ni se improvisa: se avisa de inmediato."),
    ],
    ctx=("abc", "Una supervisora de ejemplo recibe una hoja con lecturas de ΔT fuera de rango en dos equipos. ¿Qué hace?", "Revisa la calibración de los instrumentos y decide con personal autorizado cómo seguir", "Archiva la hoja sin hacer nada", "Pide a los usuarios que ajusten los equipos ellos mismos", "Un resultado fuera de rango exige verificar el dato y decidir con personal autorizado."),
    sc=[
        ("En Refrigeración: ¿cómo se calcula el ΔT del aire?", "Retorno menos impulsión", "Es la diferencia entre el aire que vuelve y el que sale."),
        ("¿De dónde se toma el rango correcto de ΔT?", "Del manual del fabricante del equipo", "Cada equipo tiene sus propios valores."),
        ("¿Cuántos Pa son 3 kPa?", "3000 Pa", "Un kPa equivale a 1000 Pa, así que 3 kPa son 3000 Pa."),
    ],
    op=("Hoja de ejemplo (equipos ficticios): el manual pide un ΔT entre 7 y 11 °C. Equipo F1: retorno 29 °C, impulsión 20 °C. Equipo F2: retorno 25 °C, impulsión 20 °C. F1 funciona con 3 kW durante 6 horas al día por 20 días; tarifa de ejemplo $140 por kWh. "
        "Escribe (a) el ΔT de cada equipo, (b) cuál cumple el manual, (c) los kWh y el costo de F1, (d) qué haces con el equipo que no cumple y quién decide los pasos siguientes.",
        "(a) F1: 29−20 son 9 °C; F2: 25−20 son 5 °C. (b) F1 cumple, porque 9 está entre 7 y 11; F2 queda por debajo. (c) 3 por 6 por 20 son 360 kWh; 360 por 140 son 50.400 pesos. (d) Registro el valor tal cual, verifico la calibración del instrumento e informo al supervisor, que decide con personal autorizado.",
        ["calcula los ΔT", "compara con el rango", "calcula consumo y costo", "informa sin intervenir el equipo"],
        ["hoja con los cálculos y el informe"],
        ["restar al revés", "usar un rango de otro equipo", "decir que ajustaría el equipo"],
        "Pregunta: «¿quién decide qué hacer con F2?». Si no responde, pídele que relea la regla de informar al supervisor."),
    reinforce="Inventa un equipo con temperaturas de retorno e impulsión, calcula su ΔT y compáralo con un rango que escribas.",
    extend="Explica con un ejemplo por qué una lectura con instrumento vencido puede llevar a una decisión equivocada.",
)
