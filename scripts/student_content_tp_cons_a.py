"""Construcción TP 3.º medio: OAE-01 (leer planos, esquemas y especificaciones), OAE-02 (mediciones y controles) y OAE-03 (trazados). Solo conceptos, documentos y planillas, con datos de ejemplo."""
from __future__ import annotations

from tp_cons_common import AVISO, EMER, build

O1 = "TP-CONS-3-OAE-01"
O2 = "TP-CONS-3-OAE-02"
O3 = "TP-CONS-3-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). Proyecto «Casa Pino» (ficticio): vivienda de un piso de 60 m². Láminas: A-1 planta de arquitectura, A-2 elevaciones, E-1 fundaciones, "
     "E-2 estructura de muros y techumbre, T-1 terminaciones. Además trae un manual de especificaciones técnicas de 12 páginas. Riesgos anotados para la obra: caída de personas, golpe por objetos y atrapamiento.")
build(
    O1, 1, F,
    use="Aprenderé qué documentos forman un proyecto de construcción, qué tipos de plano existen y qué riesgos hay que reconocer antes de leer cualquier lámina.",
    prior=["Sé leer una tabla y un dibujo simple.", "Sé sumar y multiplicar.", "Sé que un trabajo se encarga por escrito."],
    explain=[
        "Una obra de construcción reúne los trabajos que levantan una edificación o una vía. Antes de ejecutarla existe un proyecto: un conjunto de documentos. El plano es un dibujo a escala. El de arquitectura muestra la distribución y las medidas; el de fundación, lo que apoya en el suelo; el de estructura, los elementos que sostienen; el de terminaciones, los acabados; el de obras viales, caminos y calles. El esquema es un dibujo simplificado que explica una idea. El manual de especificaciones técnicas dice por escrito qué materiales y qué calidad se piden.",
        "La obra gruesa es la parte que sostiene la construcción (fundaciones, muros, vigas, techumbre); las terminaciones son los acabados que se ven y se usan. Cada plano lleva una revisión, que es su versión. Los roles se reparten: el proyectista diseña, el jefe de obra organiza, el supervisor revisa y los trabajadores ejecutan. Lo que se debe cumplir lo fija la norma vigente, y una entidad fiscalizadora la hace cumplir. Si dos documentos se contradicen, nadie elige uno por su cuenta: se anota la diferencia y se informa a quien decide.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("plano", "dibujo a escala de una obra"), ("esquema", "dibujo simplificado que explica una idea"), ("especificaciones técnicas", "texto que dice qué materiales y qué calidad se piden"), ("obra gruesa", "parte que sostiene la construcción"), ("terminaciones", "acabados de una obra"), ("revisión", "versión de un plano"), ("proyectista", "persona que diseña el proyecto")],
    worked=[
        ("Elegir el documento", "Un encargado de ejemplo necesita saber qué calidad debe tener la pintura de una sala. ¿Qué documento consulta?", ["La calidad de los materiales se escribe, no se dibuja.", "Ese texto está en el manual de especificaciones técnicas."], "Las especificaciones técnicas"),
        ("Contar hojas", "Un proyecto de ejemplo tiene 4 láminas y un manual de 8 páginas. Se imprime 1 copia de todo. ¿Cuántas hojas se imprimen?", ["Se suman las láminas y las páginas del manual.", "4 más 8 son 12."], "12 hojas"),
    ],
    mistakes=[("Elegir entre dos documentos que se contradicen y seguir sin avisar.", "Un documento puede estar equivocado y llevar a ejecutar algo riesgoso.", "Anota la diferencia e informa al proyectista o al supervisor."),
              ("Creer que saber leer planos habilita para dirigir trabajos de riesgo.", "Esas tareas exigen personal autorizado y norma vigente.", "Aprende los conceptos aquí y practica solo con instructor autorizado.")],
    T=[
        ("abc", "En Construcción: ¿qué es un esquema dentro de los documentos de una obra?", "Un dibujo simplificado que explica una idea", "Un texto con el precio de cada material", "Un plano a escala de toda la obra con todas sus medidas", "El esquema simplifica una idea; el texto de calidad son las especificaciones y el plano completo lleva escala y medidas."),
        ("abc", "Un jefe de obra de ejemplo quiere ver cómo se distribuyen las piezas de una vivienda. ¿Qué plano mira?", "El de arquitectura", "El de fundación", "El de obras viales", "La distribución de recintos está en arquitectura; fundación muestra el apoyo y viales se refiere a caminos."),
        ("abc", "En Construcción: ¿qué se llama obra gruesa?", "La parte que sostiene la construcción", "Los acabados de pintura y revestimientos", "El conjunto de herramientas de la obra", "La obra gruesa es la estructura; los acabados son las terminaciones y las herramientas son otro asunto."),
        ("=", "{F} Se imprime 2 copias de cada lámina y 3 copias del manual. ¿Cuántas hojas se imprimen en total?", "5*2+12*3", "Cinco láminas por 2 copias más 12 páginas por 3 copias.", " hojas"),
        ("abc", "{F} Se quiere saber cómo se apoya la vivienda en el suelo. ¿Qué lámina corresponde?", "E-1, de fundaciones", "T-1, de terminaciones", "A-2, de elevaciones", "La fundación es lo que apoya en el suelo; las otras láminas muestran acabados o fachadas."),
        ("abc", "{F} ¿Qué riesgos anota la ficha para esta obra?", "Caída de personas, golpe por objetos y atrapamiento", "Solo el atraso de los materiales", "Caída de personas y contaminación de un río cercano", "La ficha nombra exactamente caída, golpe y atrapamiento; las otras opciones agregan cosas que no nombra."),
        ("=", "{F} Una empresa de ejemplo cobra $1.200 por m² por el aseo final. ¿Cuánto cobra por la vivienda?", "60*1200", "Se multiplica el valor por m² por la superficie de la vivienda.", " pesos"),
        ("abc", "{F} Un trabajador sin autorización quiere subir al techo «solo a mirar». ¿Qué corresponde?", "No hacerlo: los trabajos en altura los hace personal autorizado con protección según la norma vigente", "Hacerlo si avisa a un compañero", "Hacerlo si el día está despejado", "Avisar a un compañero o que haga buen tiempo no reemplaza la autorización ni la protección exigida."),
        ("abc", "{F} Las especificaciones indican un material distinto del que señala la lámina T-1. ¿Qué se hace?", "Anotar la diferencia e informar al proyectista o al supervisor", "Seguir la lámina porque es un dibujo", "Seguir las especificaciones porque son texto", "Cuando dos documentos se contradicen no se elige uno por cuenta propia: decide quien diseña o supervisa."),
        ("ab", "{F} Una estudiante dice: «ya sé leer las láminas, así que puedo dirigir los trabajos de la obra». ¿Qué respuesta es correcta?", "No: leer documentos no habilita para dirigir ni ejecutar trabajos de riesgo", "Sí: leer láminas es lo único que se necesita", "Leer láminas es una habilidad distinta de estar autorizado y de conocer la norma vigente."),
        ("abc", "En una obra de ejemplo se desploma parte de un talud y alguien queda atrapado. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar de inmediato a sacar a la persona sin avisar", "Esperar a ver si el terreno se mueve de nuevo antes de llamar", "Entrar o esperar pone a más personas en peligro; se mantiene la distancia y se avisa de inmediato."),
        ("=", "{F} El proyectista agrega 2 láminas de terminaciones. Se imprimen 2 copias de cada lámina y 3 del manual. ¿Cuántas hojas se imprimen ahora?", "(5+2)*2+12*3", "Siete láminas por 2 copias más 12 páginas por 3 copias.", " hojas"),
        ("abc", "{F} Una copia de E-2 dice revisión B y otra dice revisión C. El supervisor confirma que C es la más nueva. ¿Cuál se usa?", "La revisión C y se retira la B", "Las dos, para comparar", "La B, porque llegó primero a la obra", "La revisión más nueva confirmada por el supervisor es la vigente; mantener versiones viejas en obra causa errores."),
    ],
    ctx=("abc", "Un vecino ofrece dinero a un estudiante para que «dirija» la ampliación de su casa porque ya sabe leer planos. ¿Qué responde?", "Agradece, explica que no está autorizado y sugiere contratar a un profesional o empresa responsable", "Acepta si cobra menos que una empresa", "Acepta, porque ya estudió los documentos de un proyecto", "Dirigir trabajos exige autorización y norma vigente; cobrar menos o haber estudiado no lo reemplazan."),
    sc=[
        ("En Construcción: ¿qué muestra un plano de estructura?", "Los elementos que sostienen la construcción", "La estructura es lo que sostiene; los acabados están en terminaciones."),
        ("¿Qué se hace si el plano y las especificaciones se contradicen?", "Anotar la diferencia e informar al proyectista o al supervisor", "No se elige un documento al azar porque podría ser el equivocado."),
        ("¿Quién dirige trabajos de riesgo en una obra?", "Personal autorizado, con norma vigente y protección", "Este cuaderno no habilita para trabajar ni intervenir obras."),
    ],
    op=("Proyecto de ejemplo «Bodega Coigüe»: 3 láminas (A-1 arquitectura, E-1 fundaciones, T-1 terminaciones) y un manual de especificaciones de 6 páginas. El manual pide un revestimiento distinto del que dibuja T-1. Escribe (a) qué documento consultarías para saber qué calidad de material se pide, (b) cuántas hojas se imprimen si se hacen 2 copias de todo, (c) qué haces con la diferencia del revestimiento y a quién informas, (d) un riesgo de la obra y quién debe ejecutar trabajos de riesgo.",
        "(a) Las especificaciones técnicas. (b) 3+6 son 9 hojas y por 2 copias son 18 hojas. (c) Anoto la diferencia y la informo al proyectista o al supervisor; no elijo por mi cuenta. (d) Caída o golpe; los ejecuta personal autorizado según la norma vigente.",
        ["nombra el documento correcto", "calcula bien las hojas", "informa la diferencia sin decidir por su cuenta", "reconoce un riesgo y quién ejecuta"],
        ["hoja con las cuatro respuestas"],
        ["elegir un documento sin avisar", "olvidar multiplicar por las copias", "decir que puede ejecutar el trabajo"],
        "Pregunta: «¿qué haces si dos documentos se contradicen?». Si no responde, pídele que relea la regla de informar la diferencia."),
    reinforce="Escribe los cinco tipos de plano de la explicación y, junto a cada uno, una frase que diga qué muestra.",
    extend="Explica con un ejemplo inventado por qué una obra bien dibujada puede ser riesgosa si la ejecuta personal sin autorización.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (plano descrito por escrito, de ejemplo, inventado). Planta de la «Bodega Roble», a escala 1:100. Leyenda: P = puerta, V = ventana, M = muro, C = corte. "
     "Elementos: 1 puerta (P1), 2 ventanas (V1 y V2) y un corte A-A. Cota de altura de los muros en el corte A-A: 3 m. Rótulo: revisión C. "
     "En el plano, el lado largo de la bodega mide 8 cm y el lado corto mide 5 cm.")
build(
    O1, 2, F,
    use="Aprenderé a leer la planta, el corte, la leyenda, las cotas, la escala y el rótulo de un plano de construcción descrito por escrito.",
    prior=["Sé qué documentos forman un proyecto.", "Sé multiplicar y dividir por 50 y 100.", "Sé pasar de centímetros a metros."],
    explain=[
        "La planta es la vista de la construcción desde arriba, como si se le quitara el techo. El corte es una vista que parte la construcción por una línea y muestra alturas y espesores. La elevación es la vista de una fachada. El detalle es una ampliación de un punto con más medidas. La leyenda explica el significado de cada símbolo; sin ella un plano no se puede leer. La cota es un número que indica una medida. El rótulo reúne el nombre del proyecto, la escala, la fecha y la revisión.",
        "El plano se dibuja a escala: una razón fija entre lo dibujado y lo real. A escala 1:100, 1 cm del plano son 100 cm reales, es decir, 1 m. A escala 1:50, 1 cm del plano son 50 cm reales. Para pasar de lo dibujado a lo real se multiplica por el número de la escala. Una fotocopia reducida o ampliada cambia el tamaño del dibujo, por eso se confía en las cotas y el rótulo, no en una regla.",
        f"Nadie agrega símbolos ni cambia medidas por su cuenta: lo decide el proyectista. {EMER} {AVISO}",
    ],
    vocab=[("planta", "vista desde arriba"), ("corte", "vista que parte la construcción por una línea y muestra alturas"), ("elevación", "vista de una fachada"), ("detalle", "ampliación de un punto con más medidas"), ("leyenda", "tabla que explica los símbolos"), ("cota", "número que indica una medida"), ("escala", "razón fija entre lo dibujado y lo real")],
    worked=[
        ("Pasar de plano a realidad", "En un plano de ejemplo a escala 1:50, un pasillo mide 10 cm. ¿Cuánto mide en la realidad, en metros?", ["Se multiplica por 50: 10 por 50 son 500 cm.", "500 cm son 5 m."], "5 m"),
        ("Leyenda faltante", "A un plano de ejemplo le falta la leyenda. Un ayudante dice que el símbolo de un círculo es un pilar. ¿Puede afirmarlo?", ["Sin leyenda el significado de un símbolo no está confirmado.", "Debe pedir la leyenda o consultar al proyectista."], "No: debe pedir la leyenda"),
    ],
    mistakes=[("Medir con regla una fotocopia reducida para saber una dimensión.", "La copia cambió el tamaño del dibujo y la escala ya no coincide.", "Usa las cotas escritas y revisa el rótulo."),
              ("Cambiar la ubicación de una ventana porque «se ve mejor».", "Solo el proyectista decide cambios al diseño.", "Anota la duda e infórmala al proyectista o al supervisor.")],
    T=[
        ("abc", "En Construcción: ¿qué muestra un corte en un plano?", "Alturas y espesores al partir la construcción por una línea", "Solo el precio de cada elemento", "La fachada completa vista de frente", "El corte parte la construcción y muestra alturas; la fachada es la elevación y los precios van en el presupuesto."),
        ("abc", "En un plano, ¿qué es una cota?", "Un número que indica una medida", "El nombre del dibujante", "El color con que se pinta un muro", "La cota indica una medida; el nombre del autor y el color no son cotas."),
        ("abc", "¿Qué indica la revisión escrita en el rótulo de un plano?", "La versión del plano", "La cantidad de personas que lo leyeron", "El número de hojas de la obra", "La revisión identifica la versión; no cuenta lectores ni hojas."),
        ("=", "{F} ¿Cuántos centímetros reales mide el lado corto de la bodega?", "5*100", "A escala 1:100 se multiplica por 100 los 5 cm dibujados.", " cm"),
        ("=", "{F} ¿Cuántas aberturas (puertas y ventanas) dibuja la planta en total?", "1+2", "Se suman una puerta y dos ventanas.", " aberturas"),
        ("abc", "{F} ¿Qué significa C en la leyenda?", "Corte", "Cota", "Cielo", "La leyenda de la ficha dice C = corte; las otras opciones usan la misma letra pero no están en ella."),
        ("=", "{F} ¿Cuántos m² tiene la planta de la bodega?", "8*5", "Los lados reales miden 8 m y 5 m; el área es su producto.", " m²"),
        ("abc", "{F} Una copia del plano parece reducida a la mitad. ¿Cómo se obtiene la medida confiable?", "Leyendo las cotas y el rótulo, no con una regla", "Midiendo con regla y suponiendo la misma escala", "Pidiendo la opinión de un compañero", "La regla sobre una copia cambiada engaña; las cotas escritas no cambian al copiar."),
        ("abc", "{F} Hay dos copias, una con revisión B y otra con revisión C. El supervisor dice que la C es la vigente. ¿Cuál se usa?", "La revisión C", "La revisión B", "La que esté más limpia", "La revisión vigente indicada por el supervisor es la que manda."),
        ("ab", "{F} Un ayudante dice: «la puerta parece angosta, la haré más ancha». ¿Qué respuesta es correcta?", "No: solo el proyectista decide cambios; se informa la duda", "Sí: quien ve la obra puede cambiar las medidas", "Las medidas de un plano no las cambia quien ejecuta."),
        ("abc", "{F} El jefe de obra pregunta quién puede autorizar un cambio en la ubicación de V2. ¿Quién es?", "El proyectista, con conocimiento del supervisor", "Cualquier trabajador que lo vea necesario", "El que llegue primero a la obra", "El diseño lo decide el proyectista; ni la necesidad percibida ni llegar primero dan autoridad."),
        ("=", "{F} Si cada metro cuadrado de un muro lleva un recubrimiento de ejemplo, y un muro largo mide 8 m con la altura de la cota, ¿cuántos m² tiene?", "8*3", "Largo del muro por la altura dada por la cota.", " m²"),
        ("abc", "{F} Otro dibujante muestra el lado largo de 8 m con 16 cm. ¿A qué escala lo dibujó?", "1:50", "1:100", "1:25", "Si 16 cm son 800 cm reales, cada centímetro vale 50 cm reales, es decir, escala 1:50."),
    ],
    ctx=("abc", "En una obra de ejemplo llega una lámina sin leyenda ni rótulo. ¿Qué corresponde hacer?", "Pedir la lámina completa y no usarla hasta tenerla", "Usarla porque los dibujos se entienden solos", "Completar la leyenda con lo que parece lógico", "Sin leyenda ni rótulo no se sabe qué significa ni qué versión es; se pide la lámina completa."),
    sc=[
        ("En Construcción: ¿qué es la leyenda de un plano?", "La tabla que explica qué es cada símbolo", "Sin leyenda no se pueden interpretar los símbolos con seguridad."),
        ("A escala 1:50, ¿cuántos centímetros reales son 3 cm del plano?", "150 cm", "Se multiplica 3 por 50 porque cada centímetro representa 50."),
        ("¿Quién cambia las medidas de un plano?", "El proyectista, no quien ejecuta", "Los cambios de diseño tienen un responsable y quedan registrados."),
    ],
    op=("Plano de ejemplo «Bodega Haya»: planta a escala 1:50. Leyenda: P = puerta, V = ventana. Elementos: 2 puertas y 3 ventanas. En el plano, el lado largo mide 12 cm y el corto 8 cm. Rótulo: revisión A. Escribe (a) cuántos metros reales mide cada lado, (b) cuántas aberturas dibuja, (c) qué haces si ves que una ventana está en la pared equivocada y a quién avisas, (d) qué indica la revisión.",
        "(a) 12 por 50 son 600 cm, es decir, 6 m; 8 por 50 son 400 cm, es decir, 4 m. (b) 2+3 son 5 aberturas. (c) Anoto la duda y aviso al proyectista o al supervisor; no la cambio yo. (d) La versión del plano.",
        ["convierte bien con la escala", "cuenta las aberturas", "informa sin cambiar el diseño", "explica la revisión"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar por 100 en vez de 50", "cambiar la ventana por su cuenta", "confundir revisión con fecha"],
        "Pregunta: «¿por qué multiplicas por 50?». Si no responde, pídele que relea la regla de la escala."),
    reinforce="Dibuja una tabla con tres columnas (medida en el plano, escala, medida real) y completa tres filas con números inventados.",
    extend="Explica por qué dos personas pueden obtener medidas distintas si una usa la cota y la otra una fotocopia reducida.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Taller «Alerce». Planta A-1 (revisión B): 4 ventanas; muro del eje B de 600 cm; muro del eje C de 400 cm. "
     "Planilla de ventanas de las especificaciones (revisión B): 5 ventanas. Plano de estructura E-2 (revisión B): muro del eje B de 600 cm y muro del eje C de 400 cm. "
     "Cada ventana lleva 2 m² de vidrio (dato de ejemplo).")
build(
    O1, 3, F,
    use="Aprenderé a cruzar planos y especificaciones para detectar diferencias y a dejarlas registradas sin decidir por mi cuenta.",
    prior=["Sé qué es una revisión y una cota.", "Sé sumar y multiplicar.", "Sé convertir centímetros a metros."],
    explain=[
        "Un caso de lectura cruzada consiste en comparar el mismo dato en varios documentos. Si coincide, se dice que los documentos son consistentes. Si no coincide, hay una discrepancia: una diferencia entre documentos. Una planilla es una tabla de elementos con sus cantidades. Un registro de diferencias deja escrito qué documentos se contradicen, qué dice cada uno, quién lo detectó y la fecha.",
        "Una discrepancia no se resuelve eligiendo el documento que parece más lógico. Se informa al proyectista o al supervisor, que decide qué documento se corrige. Mientras no haya decisión, no se compra ni se ejecuta lo dudoso. Que dos documentos tengan la misma revisión indica que la diferencia no se explica por versiones distintas, y por eso hay que consultarla igual.",
        f"Esta tarea es de lectura y registro; no se corrige nada por cuenta propia. {EMER} {AVISO}",
    ],
    vocab=[("consistente", "que coincide en los distintos documentos"), ("discrepancia", "diferencia entre dos documentos sobre un mismo dato"), ("planilla", "tabla de elementos con sus cantidades"), ("registro de diferencias", "escrito que anota qué se contradice, quién lo vio y cuándo"), ("eje", "línea de referencia sobre la que se ubican muros")],
    worked=[
        ("Detectar una discrepancia", "En un caso de ejemplo, la planta dice 3 puertas y la planilla dice 4. ¿Hay discrepancia? ¿De cuánto?", ["Se comparan los dos datos del mismo elemento.", "No coinciden: 4 menos 3 es 1."], "Sí, de 1 puerta"),
        ("Registrar", "La planta dice 3 puertas y la planilla dice 4. ¿Qué se anota primero en el registro de diferencias?", ["Se anotan los documentos que se contradicen.", "Luego lo que dice cada uno, quién lo detectó y la fecha."], "Los documentos que se contradicen y lo que dice cada uno"),
    ],
    mistakes=[("Comprar 5 ventanas «por si acaso» sin consultar.", "Si el error está en la planilla se gasta de más; si está en el plano, se compra distinto.", "Informa la discrepancia y espera la decisión."),
              ("Decir «los ejes coinciden, entonces todo está bien».", "Una coincidencia no cancela otra discrepancia.", "Revisa cada dato por separado.")],
    T=[
        ("abc", "En Construcción: ¿qué es una discrepancia entre documentos?", "Una diferencia sobre un mismo dato entre dos documentos", "Una coincidencia total entre todos los planos", "Un error de ortografía en el rótulo", "La discrepancia es una diferencia sobre un mismo dato; la coincidencia total es lo contrario."),
        ("abc", "{F} ¿Entre qué documentos hay una discrepancia?", "Entre la planta A-1 y la planilla de ventanas", "Entre A-1 y E-2", "Entre E-2 y el rótulo", "Solo el número de ventanas difiere, entre la planta y la planilla; los muros coinciden."),
        ("abc", "{F} ¿Qué datos son consistentes entre A-1 y E-2?", "Los muros de los ejes B y C", "El número de ventanas", "La cantidad de vidrio", "Las longitudes de ambos ejes coinciden en los dos planos; las ventanas no están en E-2."),
        ("=", "{F} ¿Cuántas ventanas de diferencia hay entre la planilla y la planta?", "5-4", "Se resta el menor del mayor para ver la diferencia.", " ventana"),
        ("=", "{F} ¿Cuántos centímetros suman los muros de los ejes B y C?", "600+400", "Se suman las dos longitudes dadas en centímetros.", " cm"),
        ("abc", "{F} ¿Qué debe contener el registro de esta discrepancia como mínimo?", "Los documentos, lo que dice cada uno, quién la detectó y la fecha", "Solo el nombre de quien la detectó", "La decisión final, aunque no se haya consultado a nadie", "Un registro útil deja constancia de qué, dónde, quién y cuándo."),
        ("=", "{F} ¿Cuántos m² de diferencia de vidrio hay entre lo que pide la planilla y lo que dibuja la planta?", "(5-4)*2", "La diferencia de ventanas por 2 m² de vidrio cada una.", " m²"),
        ("abc", "{F} El encargado de compras propone pedir 5 ventanas «por si acaso». ¿Qué corresponde?", "Esperar la decisión del proyectista o supervisor antes de comprar", "Pedir 5 porque sobra antes que falta", "Pedir 4 porque el plano manda siempre", "Ningún documento manda por sí solo; hasta que se decida no se compra lo dudoso."),
        ("abc", "{F} ¿Qué plano se consulta para ubicar las ventanas en un recinto?", "La planta A-1", "El plano de estructura E-2", "El manual del fabricante", "La ubicación de aberturas se lee en la planta de arquitectura."),
        ("ab", "{F} Un estudiante dice: «los ejes B y C coinciden, así que no hay nada que informar». ¿Qué respuesta es correcta?", "No: aún hay una discrepancia en las ventanas", "Sí: si algo coincide no hay discrepancias", "Una coincidencia en los ejes no corrige la diferencia de ventanas."),
        ("abc", "{F} Los tres documentos tienen revisión B. ¿Qué indica eso sobre la discrepancia?", "Que no se explica por versiones distintas y hay que consultarla igual", "Que no es importante", "Que la planilla está equivocada", "Con la misma revisión no hay versión vieja que explique la diferencia, por lo que se consulta."),
        ("=", "{F} Si los ejes B y C fueran los lados de un recinto rectangular, ¿cuántos metros mide su perímetro?", "2*(600+400)//100", "El perímetro es dos veces la suma de los lados, convertido de centímetros a metros.", " m"),
        ("abc", "{F} Alguien propone avisar de la diferencia solo de palabra en el pasillo. ¿Qué es mejor?", "Dejarla en un registro escrito con fecha y firmarla", "Avisar de palabra, que es más rápido", "No avisar si es una diferencia pequeña", "El registro escrito deja constancia; una palabra dicha en el pasillo se puede olvidar."),
    ],
    ctx=("abc", "Un proveedor de ejemplo pregunta cuántas ventanas debe fabricar y los documentos dicen 4 y 5. ¿Qué responde el encargado de la obra?", "Que se aclarará con el proyectista antes de confirmar la cantidad", "Que fabrique 5 y se verá después", "Que fabrique 4 porque es menos costoso", "Confirmar sin aclarar puede significar fabricar de más o de menos; se resuelve antes."),
    sc=[
        ("En Construcción: ¿qué significa que dos documentos son consistentes?", "Que coinciden en los datos que comparten", "Si coinciden no hay discrepancia en esos datos."),
        ("¿A quién se informa una discrepancia entre documentos?", "Al proyectista o al supervisor", "Ellos deciden qué documento se corrige."),
        ("¿Se compra lo dudoso mientras no haya decisión?", "No, se espera la decisión", "Comprar lo dudoso puede significar gastar en algo equivocado."),
    ],
    op=("Caso de ejemplo «Galpón Lingue»: la planta dice 6 pilares; la planilla de estructura dice 8 pilares; ambos son revisión A. Cada pilar cuesta $30.000 (de ejemplo). Escribe (a) la diferencia de pilares, (b) la diferencia de costo, (c) qué datos anotarías en el registro, (d) qué harías con la compra.",
        "(a) 8-6 son 2 pilares. (b) 2 por $30.000 son $60.000. (c) Los dos documentos, lo que dice cada uno (6 y 8), quién lo detectó y la fecha. (d) No compro lo dudoso hasta que el proyectista o el supervisor decidan.",
        ["calcula la diferencia", "calcula el costo", "registra documentos, valores, autor y fecha", "no compra antes de la decisión"],
        ["hoja con las cuatro respuestas"],
        ["comprar sin consultar", "olvidar la fecha", "elegir un documento por su cuenta"],
        "Pregunta: «¿qué dato falta en tu registro?». Si no responde, pídele que relea qué debe contener."),
    reinforce="Inventa dos documentos que digan cantidades distintas de un mismo elemento y escribe el registro de la diferencia.",
    extend="Explica por qué una diferencia pequeña también debe informarse.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (especificación y recepción de ejemplo, inventadas). Especificación de la viga V1: largo 400 cm; sección 10 cm de ancho por 20 cm de alto; "
     "una pieza cumple el largo si su diferencia con 400 cm es de 1 cm o menos. Recepción en bodega de cuatro piezas: pieza 1 mide 399 cm; pieza 2 mide 402 cm; pieza 3 mide 398 cm; pieza 4 mide 401 cm.")
build(
    O1, 4, F,
    use="Aprenderé a comparar una especificación técnica con datos de ejemplo y a decidir si una pieza cumple, usando tolerancia, sección y volumen.",
    prior=["Sé leer especificaciones.", "Sé multiplicar tres números.", "Sé restar para hallar una diferencia."],
    explain=[
        "Una especificación técnica pide características concretas. La sección es la forma y las medidas de la cara cortada de una pieza; por ejemplo, ancho por alto. El área de la sección rectangular se calcula multiplicando ancho por alto. La tolerancia es la diferencia máxima que la especificación acepta entre la medida pedida y la real. Si una pieza está dentro de la tolerancia, cumple; si no, no cumple.",
        "Para decidir se compara cada medida con lo pedido y se calcula la diferencia sin importar el signo. Una pieza que no cumple no se usa por decisión propia: se registra y se informa al supervisor, que decide si se rechaza o se consulta al proyectista. El volumen de una pieza recta es largo por ancho por alto, y se expresa en centímetros cúbicos (cm³) si las medidas están en centímetros.",
        f"Aquí solo se leen y se comparan datos escritos. {EMER} {AVISO}",
    ],
    vocab=[("sección", "forma y medidas de la cara cortada de una pieza"), ("tolerancia", "diferencia máxima aceptada respecto de la medida pedida"), ("volumen", "espacio que ocupa una pieza; largo por ancho por alto"), ("cumple", "está dentro de lo que pide la especificación"), ("recepción", "revisión de lo que llega a la bodega frente a lo pedido")],
    worked=[
        ("Revisar una pieza", "Una especificación de ejemplo pide un listón de 250 cm con diferencia máxima de 2 cm. Llega uno de 252 cm. ¿Cumple?", ["La diferencia es 252 menos 250, igual a 2 cm.", "2 cm es el máximo permitido, así que está dentro."], "Sí, cumple"),
        ("Área de una sección", "Un listón de ejemplo tiene sección de 5 cm por 15 cm. ¿Cuál es su área de sección?", ["Se multiplica ancho por alto.", "5 por 15 son 75."], "75 cm²"),
    ],
    mistakes=[("Aceptar una pieza fuera de tolerancia porque «son solo unos centímetros».", "La tolerancia es el límite escrito; pasarlo no cumple la especificación.", "Registra la medida e informa al supervisor."),
              ("Comparar solo el largo y olvidar la sección.", "La sección también es parte de la especificación.", "Revisa cada característica que la especificación pide.")],
    T=[
        ("abc", "En Construcción: ¿qué es la tolerancia de una especificación?", "La diferencia máxima aceptada respecto de la medida pedida", "La cantidad de piezas que se puede perder", "El plazo para entregar el material", "La tolerancia limita la diferencia de medida; no habla de mermas ni de plazos."),
        ("abc", "¿Qué es la sección de una viga de ejemplo?", "La forma y medidas de su cara cortada", "El lugar de la obra donde se instala", "La cantidad de piezas del pedido", "La sección describe la cara cortada; el lugar y la cantidad son otros datos."),
        ("=", "{F} ¿Cuál es el área de la sección de la viga V1 en cm²?", "10*20", "Se multiplica ancho por alto.", " cm²"),
        ("abc", "{F} La pieza 1 mide 399 cm. ¿Cumple?", "Sí: la diferencia con 400 cm es 1 cm", "No: no mide 400 cm exactos", "No se puede saber sin medirla otra vez", "La tolerancia admite hasta 1 cm de diferencia, y 399 está a 1 cm de 400."),
        ("abc", "{F} La pieza 2 mide 402 cm. ¿Qué corresponde?", "No cumple: se registra e informa al supervisor", "Cumple porque sobra largo", "Cumple si se corta a mano", "La diferencia de 2 cm supera la tolerancia de 1 cm y la decisión corresponde al supervisor."),
        ("=", "{F} ¿Cuántos centímetros se aleja la pieza 3 de la medida pedida?", "400-398", "Se resta la medida real de la pedida.", " cm"),
        ("=", "{F} ¿Cuál es el volumen, en cm³, de una pieza que mide exactamente lo especificado?", "400*10*20", "Largo por ancho por alto.", " cm³"),
        ("abc", "{F} ¿Entre qué medidas de largo, en centímetros, cumple una pieza?", "Entre 399 y 401, ambas incluidas", "Entre 398 y 402, ambas incluidas", "Solo si mide exactamente 400", "La tolerancia de 1 cm da el rango de 399 a 401 y los extremos cumplen."),
        ("abc", "{F} La pieza 4 mide 401 cm. ¿Cumple?", "Sí: está a 1 cm, que es el límite aceptado", "No: pasa de 400", "Solo si se rebaja", "La ficha dice que 1 cm o menos de diferencia cumple, y 401 está exactamente a 1 cm."),
        ("ab", "{F} Un ayudante dice: «la pieza 2 sirve igual porque son solo 2 cm de más». ¿Qué respuesta es correcta?", "No: supera la tolerancia; se registra y se consulta", "Sí: unos centímetros nunca importan", "Una pieza que supera la tolerancia no cumple la especificación."),
        ("abc", "{F} ¿Qué datos debe anotar el registro de recepción de cada pieza?", "Número de pieza, medida, resultado y fecha", "Solo la fecha", "Solo el resultado, sin medida", "Para que otro pueda verificar, el registro incluye qué se midió, el valor y el resultado."),
        ("=", "{F} Se pidieron 12 vigas y se espera que 1 de cada 3 llegue fuera de tolerancia. ¿Cuántas llegarían fuera?", "12//3", "Una de cada tres de 12 son 12 divididas en 3.", " vigas"),
        ("abc", "{F} Un proveedor envía vigas de 10 cm por 18 cm de sección, de 400 cm de largo. ¿Cumplen?", "No: la sección también está especificada y el área es 180 cm² en vez de 200", "Sí: tienen el largo correcto", "Sí: son más económicas", "La especificación pide una sección de 10 por 20; el largo correcto no compensa una sección menor."),
    ],
    ctx=("abc", "Una pieza llega con el largo correcto pero sin que nadie haya registrado la recepción. ¿Qué corresponde?", "Registrar la recepción con medida, resultado y fecha antes de usarla", "Usarla porque el largo es correcto", "Registrarla después si hay tiempo", "El registro hace verificable la recepción y debe hacerse antes de usar la pieza."),
    sc=[
        ("En Construcción: ¿qué significa que una pieza cumple?", "Que está dentro de lo que pide la especificación", "Cumplir es estar dentro de la medida y tolerancia pedidas."),
        ("¿Cuál es el área de una sección de 6 cm por 12 cm?", "72 cm²", "Se multiplica ancho por alto, 6 por 12."),
        ("¿Qué se hace con una pieza fuera de tolerancia?", "Se registra e informa al supervisor", "El supervisor decide si se rechaza o se consulta."),
    ],
    op=("Especificación de ejemplo: viga V2 de 300 cm de largo, sección de 8 cm por 18 cm, diferencia máxima de 2 cm. Llegan tres piezas: 301 cm, 304 cm y 298 cm. Escribe (a) el área de la sección, (b) qué piezas cumplen, (c) qué haces con las que no cumplen, (d) qué anotas en el registro.",
        "(a) 8 por 18 son 144 cm². (b) 301 (1 cm) y 298 (2 cm) cumplen; 304 (4 cm) no. (c) La registro e informo al supervisor. (d) Número de pieza, medida, resultado y fecha.",
        ["calcula el área", "decide bien cada pieza", "no usa la pieza que no cumple", "registra los datos mínimos"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el límite incluido", "usar la pieza que no cumple", "no registrar la fecha"],
        "Pregunta: «¿cuánto se aleja la de 298?». Si no responde, pídele que reste."),
    reinforce="Inventa una especificación con largo y tolerancia y decide si cuatro medidas inventadas cumplen.",
    extend="Explica por qué una tolerancia pequeña no autoriza a usar piezas que la superan.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (comparación de ejemplo, inventada). Plano E-2 del «Galpón Cedro». Revisión B: 8 pilares y 6 vigas. Revisión C: 10 pilares y 6 vigas, con la nota «ver detalle D-3». "
     "La planilla de materiales se armó con la revisión B. Precios de ejemplo: pilar $40.000 cada uno; viga $55.000 cada una.")
build(
    O1, 5, F,
    use="Aprenderé a comparar dos revisiones de un plano, a actualizar una planilla y a verificar la calidad de mi lectura con una lista de control.",
    prior=["Sé qué es una revisión y un detalle.", "Sé calcular costos con precios unitarios.", "Sé registrar diferencias."],
    explain=[
        "Un plano cambia durante el proyecto y cada versión es una revisión. Comparar dos revisiones es buscar qué se agregó, qué se quitó y qué cambió. Una planilla armada con una revisión antigua queda desactualizada y hay que corregirla con la vigente. La nota que dice «ver detalle» obliga a consultar esa lámina antes de calcular.",
        "Para verificar la calidad de una lectura se usa una lista de control: ¿es la revisión vigente?, ¿leí la escala?, ¿leí la leyenda?, ¿revisé las cotas?, ¿consulté los detalles citados? Si la lista queda incompleta, la lectura no está terminada. Dos personas que obtienen cantidades distintas leen otra vez juntas la misma revisión y consultan al supervisor.",
        f"Todo se hace en papel, con documentos y precios de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("revisión vigente", "versión de un plano que está en uso"), ("desactualizada", "armada con una versión antigua"), ("detalle", "lámina que amplía un punto con más medidas"), ("lista de control", "lista de preguntas que se marcan antes de dar por buena una lectura"), ("costo unitario", "precio de una unidad")],
    worked=[
        ("Comparar revisiones", "Una revisión A de ejemplo trae 4 vigas y la revisión B trae 5. ¿Qué cambió?", ["Se comparan las cantidades de la misma pieza.", "En la B hay una viga más."], "Se agregó una viga"),
        ("Costo adicional", "Una pieza de ejemplo cuesta $20.000 y se agregan 3. ¿Cuánto cuesta el aumento?", ["Se multiplica la cantidad agregada por el precio.", "3 por 20.000 son 60.000."], "$60.000"),
    ],
    mistakes=[("Seguir calculando con la planilla antigua porque «ya estaba hecha».", "Una planilla desactualizada da cantidades y costos equivocados.", "Corrígela con la revisión vigente e informa el cambio."),
              ("Ignorar la nota «ver detalle».", "El detalle puede cambiar medidas o cantidades.", "Consulta el detalle antes de calcular.")],
    T=[
        ("abc", "En Construcción: ¿qué es una lista de control de lectura?", "Una lista de preguntas que se marcan antes de dar por buena la lectura", "Una lista con el nombre de los trabajadores de la obra", "Una lista de precios de los materiales", "La lista de control verifica la lectura; no es un listado de personas ni de precios."),
        ("abc", "{F} ¿Qué cambió de la revisión B a la C?", "Hay 2 pilares más y una nota que remite al detalle D-3", "Hay 2 vigas más", "Se quitaron 2 pilares", "La C trae 10 pilares frente a 8 y mantiene 6 vigas."),
        ("abc", "{F} ¿Por qué la planilla de materiales está desactualizada?", "Se armó con la revisión B y la vigente es la C", "Porque no incluye vigas", "Porque tiene precios de ejemplo", "Se armó con una revisión anterior a la vigente."),
        ("=", "{F} ¿Cuántos pilares se agregan en la revisión C?", "10-8", "Se resta la cantidad de la revisión B de la de la C.", " pilares"),
        ("=", "{F} ¿Cuánto cuesta en total la estructura de la revisión C (pilares y vigas)?", "10*40000+6*55000", "Pilares por su precio más vigas por el suyo.", " pesos"),
        ("=", "{F} ¿Cuántas piezas (pilares y vigas) hay en total en la revisión C?", "10+6", "Se suman pilares y vigas.", " piezas"),
        ("abc", "{F} La nota dice «ver detalle D-3». ¿Qué corresponde?", "Consultar el detalle D-3 antes de calcular", "Ignorarla porque es solo una nota", "Calcular y consultar después", "Un detalle citado puede cambiar los datos; se consulta antes de calcular."),
        ("abc", "{F} ¿Qué corresponde hacer con la planilla armada con la revisión B?", "Actualizarla con la revisión C e informar el cambio", "Dejarla como está porque ya está aprobada", "Borrarla sin avisar", "La planilla debe corresponder a la revisión vigente y el cambio se informa."),
        ("ab", "{F} Un ayudante dice: «la revisión C es más nueva, no hace falta revisar la planilla». ¿Qué respuesta es correcta?", "No: la planilla debe actualizarse con la revisión C", "Sí: la planilla se actualiza sola", "La planilla no cambia por sí sola cuando cambia el plano."),
        ("abc", "{F} Dos personas leen la misma lámina y obtienen cantidades distintas. ¿Qué hacen?", "Releer juntas la misma revisión y consultar al supervisor", "Quedarse con la cantidad menor", "Promediar las dos cantidades", "Se aclara la diferencia con la misma revisión y la decisión es del supervisor."),
        ("abc", "¿Cuál NO es una pregunta de una lista de control de lectura?", "¿Cuánto dinero tiene el cliente?", "¿Es la revisión vigente?", "¿Leí la leyenda?", "Las otras preguntas verifican la lectura; la capacidad de pago del cliente no."),
        ("=", "{F} Se aprueban además 2 pilares y 1 viga más que los de la revisión C. ¿Cuánto cuesta ese aumento?", "2*40000+55000", "Dos pilares y una viga con sus precios unitarios.", " pesos"),
        ("abc", "{F} Una lectura quedó con la escala sin revisar y la lista de control incompleta. ¿Qué corresponde?", "Completar la lista antes de dar por terminada la lectura", "Entregar la lectura porque lo importante son las cantidades", "Marcar la lista como completa", "Una lista incompleta indica una lectura sin terminar; no se marca por cumplir."),
    ],
    ctx=("abc", "Llega a la obra una orden de compra armada con la revisión B. Hoy la vigente es la C. ¿Qué hace el encargado?", "Detener la compra y actualizarla con la revisión C", "Comprar de todos modos para ganar tiempo", "Comprar la mitad con cada revisión", "Comprar con una revisión antigua genera piezas que no sirven o faltan."),
    sc=[
        ("En Construcción: ¿qué es la revisión vigente?", "La versión del plano que está en uso", "Es la que debe usarse para calcular y ejecutar."),
        ("Una pieza vale $25.000 y se agregan 4. ¿Cuánto cuesta el aumento?", "$100.000", "Se multiplica la cantidad por el precio unitario."),
        ("¿Qué se hace con una nota «ver detalle»?", "Consultar el detalle antes de calcular", "El detalle puede cambiar medidas o cantidades."),
    ],
    op=("Plano de ejemplo «Taller Roble»: revisión A con 5 pilares y 4 vigas; revisión B con 6 pilares y 4 vigas y una nota «ver detalle D-1». Pilar $35.000, viga $48.000 (de ejemplo). La planilla se hizo con la A. Escribe (a) qué cambió, (b) cuánto cuesta el aumento, (c) qué haces con la planilla, (d) qué haces con la nota.",
        "(a) Se agregó un pilar y hay una nota. (b) 1 por $35.000 son $35.000. (c) La actualizo con la revisión B e informo el cambio. (d) Consulto el detalle D-1 antes de calcular.",
        ["detecta el cambio", "calcula el aumento", "actualiza la planilla", "consulta el detalle"],
        ["hoja con las cuatro respuestas"],
        ["seguir con la planilla antigua", "ignorar el detalle", "olvidar informar el cambio"],
        "Pregunta: «¿qué revisión vale?». Si no responde, pídele que relea el concepto de revisión vigente."),
    reinforce="Escribe tu propia lista de control de cinco preguntas para dar por buena una lectura.",
    extend="Explica qué riesgos trae a una obra tener copias de distintas revisiones circulando a la vez.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 6 (obra de ejemplo, inventada). Obra «Bodega Lenga»: cuatro tareas de medición y control. Largo de un muro (instrumento: huincha de medir); horizontalidad de un piso (instrumento: nivel); "
     "verticalidad de un pilar (instrumento: plomada); ángulo de una esquina (instrumento: escuadra). El registro tiene seis columnas: magnitud, valor, unidad, instrumento, fecha y responsable.")
build(
    O2, 1, F,
    use="Aprenderé qué es medir y controlar en una obra, qué magnitudes se miden, qué instrumentos corresponden y qué riesgos hay alrededor.",
    prior=["Sé las unidades metro y centímetro.", "Sé multiplicar y dividir.", "Sé leer una tabla."],
    explain=[
        "Medir es comparar algo con una unidad, como el metro o el centímetro. Controlar es verificar si una medida cumple lo que pide el proyecto. Una magnitud es una característica que se puede medir: la longitud, el ángulo, la horizontalidad (qué tan plana está una superficie respecto del nivel) y la verticalidad (qué tan alineada está una pieza con la vertical). Cada magnitud tiene un instrumento apropiado: la huincha de medir para longitudes, el nivel para la horizontalidad, la plomada para la verticalidad y la escuadra para los ángulos rectos.",
        "Un instrumento debe estar en buen estado y verificado por quien corresponda; si está dañado, se informa y no se usa. Todo valor medido se anota con su unidad, la fecha y quién lo midió, porque sin eso nadie puede revisarlo. Medir en una obra tiene riesgos: zonas con desnivel o sin protección, tránsito de maquinaria, objetos que caen. Las condiciones de seguridad las fija la norma vigente y las verifica personal autorizado.",
        f"En este cuaderno solo aprendes el vocabulario y a leer registros. {EMER} {AVISO}",
    ],
    vocab=[("magnitud", "característica que se puede medir"), ("instrumento", "aparato con el que se mide"), ("horizontalidad", "qué tan plana está una superficie respecto del nivel"), ("verticalidad", "qué tan alineada está una pieza con la vertical"), ("registro", "tabla donde se anotan las mediciones"), ("controlar", "verificar si una medida cumple lo pedido")],
    worked=[
        ("Elegir el instrumento", "Una cuadrilla de ejemplo quiere saber el largo de una pared. ¿Qué instrumento corresponde?", ["El largo es una longitud.", "Las longitudes se miden con huincha."], "Huincha de medir"),
        ("Convertir unidades", "Un registro de ejemplo anota 2 m 50 cm. ¿Cuántos centímetros son?", ["2 m son 200 cm.", "200 más 50 son 250."], "250 cm"),
    ],
    mistakes=[("Anotar un valor sin su unidad porque «se entiende».", "Un número sin unidad puede leerse como metros, centímetros o milímetros.", "Anota siempre valor y unidad."),
              ("Usar un instrumento dañado «porque casi se ve igual».", "Una medida con instrumento dañado no es confiable.", "Informa y espera su revisión o reemplazo.")],
    T=[
        ("abc", "En Construcción: ¿qué instrumento sirve como referencia de la verticalidad de un pilar?", "La plomada", "La huincha de medir", "La escuadra", "La plomada da la referencia vertical; la huincha mide largos y la escuadra ángulos rectos."),
        ("abc", "¿Cuál es una magnitud que se mide en metros?", "La longitud", "La verticalidad", "El número de revisión", "La longitud se mide en metros; la verticalidad no se expresa así y la revisión no es una magnitud."),
        ("abc", "En Construcción: ¿qué significa controlar una medida?", "Verificar si cumple lo que pide el proyecto", "Medirla de memoria", "Anotarla sin compararla", "Controlar es comparar con lo pedido; medir de memoria o solo anotar no verifica nada."),
        ("=", "{F} Un largo se anotó como 3 m 20 cm. ¿Cuántos centímetros son?", "3*100+20", "Tres metros son 300 cm y se suman 20 cm.", " cm"),
        ("abc", "{F} ¿Qué instrumento corresponde para la horizontalidad del piso?", "El nivel", "La plomada", "La huincha de medir", "La horizontalidad se verifica con nivel; la plomada es para la vertical y la huincha para largos."),
        ("abc", "{F} ¿Qué columna del registro dice quién midió?", "Responsable", "Magnitud", "Instrumento", "La columna Responsable identifica a la persona; las otras describen qué y con qué se midió."),
        ("=", "{F} Cada una de las cuatro tareas de la ficha se mide 3 veces. ¿Cuántas mediciones hay en total?", "4*3", "Cuatro tareas por tres mediciones cada una.", " mediciones"),
        ("abc", "{F} La huincha tiene la punta doblada. ¿Qué corresponde?", "Informar y no usarla hasta que la revisen o reemplacen", "Usarla y restar mentalmente lo doblado", "Usarla porque casi no se nota", "Un instrumento dañado da medidas poco confiables y se informa."),
        ("abc", "{F} Para medir hay que acercarse al borde de una losa sin protección. ¿Qué corresponde?", "No hacerlo: avisar al supervisor y esperar protección según la norma vigente", "Hacerlo con cuidado", "Hacerlo rápido", "Trabajar al borde sin protección es riesgo de caída; se avisa y se espera protección."),
        ("ab", "{F} Un ayudante anota «300» sin unidad en la columna valor. ¿Qué respuesta es correcta?", "Está incompleto: falta la unidad", "Está completo: se entiende", "La unidad forma parte del dato; sin ella 300 puede ser cm, mm o m."),
        ("abc", "{F} Al medir cerca de un camino interno circulan camiones. ¿Qué corresponde?", "Pedir que la zona esté señalizada y protegida y avisar al supervisor", "Medir rápido entre un camión y otro", "Pedir al conductor que se detenga a la fuerza", "Trabajar en vías con tráfico exige señalización y protección según la norma vigente."),
        ("=", "{F} Un tramo de 12 m se divide en partes de 150 cm. ¿Cuántas partes salen?", "1200//150", "Se pasan 12 m a 1200 cm y se divide por 150.", " partes"),
        ("abc", "{F} Un registro no tiene fecha ni responsable. ¿Cuál es el problema?", "Nadie puede saber quién midió ni cuándo", "Se gasta más papel", "No se puede sumar", "Sin fecha y responsable el registro no se puede revisar ni verificar."),
    ],
    ctx=("abc", "Una medida del muro parece extraña y un compañero propone «ajustarla» en el registro. ¿Qué corresponde?", "Anotar lo medido y avisar al supervisor", "Cambiar el valor para que cumpla", "Borrar la fila", "Un registro refleja lo medido; alterarlo oculta el problema."),
    sc=[
        ("En Construcción: ¿para qué sirve la plomada?", "Para dar la referencia de la vertical", "La plomada es la referencia con la que se verifica la verticalidad."),
        ("¿Cuántos centímetros son 4 m 30 cm?", "430 cm", "4 m son 400 cm y se suman 30."),
        ("¿Qué se hace con un instrumento dañado?", "Informar y no usarlo", "Una medida con un instrumento dañado no es confiable."),
    ],
    op=("Obra de ejemplo «Taller Quillay»: se quiere registrar el largo de un muro (5 m 40 cm), la horizontalidad de un piso y la verticalidad de un pilar. Escribe (a) qué instrumento corresponde a cada magnitud, (b) el largo del muro en centímetros, (c) las seis columnas de un registro, (d) qué haces si el instrumento de la horizontalidad está dañado.",
        "(a) Huincha para el largo, nivel para la horizontalidad y plomada para la verticalidad. (b) 540 cm. (c) Magnitud, valor, unidad, instrumento, fecha y responsable. (d) Informo y no lo uso hasta que lo revisen o reemplacen.",
        ["asocia magnitud e instrumento", "convierte la unidad", "nombra las seis columnas", "no usa el instrumento dañado"],
        ["hoja con las cuatro respuestas"],
        ["confundir plomada y nivel", "olvidar la unidad", "usar el instrumento dañado"],
        "Pregunta: «¿qué columna dice quién midió?». Si no responde, pídele que relea el registro de la ficha."),
    reinforce="Haz una tabla con cuatro magnitudes y escribe el instrumento y la unidad de cada una.",
    extend="Explica con un ejemplo inventado qué problema causa un valor sin unidad en un registro.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 7 (registro de ejemplo, inventado). Control del largo de un muro; largo esperado 300 cm; tolerancia ±2 cm. Mediciones registradas: M1 = 299 cm; M2 = 301 cm; M3 = 300 cm; "
     "M4 = 303 cm; M5 = 298 cm. El instrumento tiene su menor división en 1 cm.")
build(
    O2, 2, F,
    use="Aprenderé los conceptos de error, tolerancia, precisión y verificación de instrumentos para leer un registro de mediciones.",
    prior=["Sé qué es una magnitud y una unidad.", "Sé restar y hallar diferencias.", "Sé leer un registro."],
    explain=[
        "El valor esperado es la medida que pide el proyecto. El error de medición es la diferencia entre el valor medido y el esperado: se calcula restando el esperado al medido, y puede ser positivo o negativo. La tolerancia es el error máximo que el proyecto acepta, escrito como ±2 cm, que significa hasta 2 cm de más o de menos. Una medición cumple cuando su error está dentro de la tolerancia.",
        "La precisión es qué tan pequeña es la división del instrumento: con divisiones de 1 cm no se pueden afirmar diferencias de 1 mm. La calibración es la comprobación de un instrumento contra una referencia, y la hace personal autorizado. Un registro muestra todos los valores medidos, aunque algunos no cumplan; nadie debe modificarlos. Quien detecta una medida fuera de tolerancia la informa al supervisor.",
        f"Todo es lectura de datos; no se interviene ningún elemento de la obra. {EMER} {AVISO}",
    ],
    vocab=[("valor esperado", "medida que pide el proyecto"), ("error de medición", "diferencia entre el valor medido y el esperado"), ("tolerancia", "error máximo que se acepta"), ("precisión", "qué tan pequeña es la división del instrumento"), ("calibración", "comprobación de un instrumento contra una referencia")],
    worked=[
        ("Calcular un error", "El valor esperado de un tramo de ejemplo es 500 cm y se midieron 497 cm. ¿Cuál es el error?", ["Se resta el esperado al medido: 497 menos 500.", "El resultado es −3 cm."], "−3 cm"),
        ("Decidir si cumple", "Una tolerancia de ejemplo es ±4 cm y el error medido es +5 cm. ¿Cumple?", ["Se compara el tamaño del error con la tolerancia.", "5 cm supera 4 cm."], "No cumple"),
    ],
    mistakes=[("Cambiar un valor del registro para que «cumpla».", "Alterar un registro oculta el problema y puede causar un defecto en la obra.", "Conserva el valor medido e informa al supervisor."),
              ("Afirmar diferencias menores que la división del instrumento.", "El instrumento no puede distinguirlas.", "Indica la limitación o pide un instrumento más preciso autorizado por la obra.")],
    T=[
        ("abc", "En Construcción: ¿qué es el error de una medición?", "La diferencia entre el valor medido y el esperado", "Un descuido de la persona que mide", "El instrumento que se usó", "El error es una diferencia numérica; no mide la intención de quien midió ni nombra el instrumento."),
        ("abc", "¿Qué es la calibración de un instrumento?", "Su comprobación contra una referencia, hecha por personal autorizado", "Anotar la fecha en el registro", "Lavarlo después de usarlo", "La calibración compara el instrumento con una referencia, no es un registro ni una limpieza."),
        ("abc", "¿Qué significa una tolerancia de ±3 cm?", "Hasta 3 cm de más o de menos", "Exactamente 3 cm de más", "Que siempre se corta 3 cm", "El signo ± indica diferencia en ambos sentidos hasta 3 cm."),
        ("=", "{F} ¿Cuál es el error de la medición M4, en cm?", "303-300", "Se resta el esperado al medido.", " cm"),
        ("abc", "{F} La medición M5 (298 cm) ¿cumple?", "Sí: su error es −2 cm, dentro de la tolerancia", "No: es menor que 300", "No: se debió medir de nuevo", "El error es 2 cm hacia abajo y la tolerancia es ±2 cm, así que está en el límite permitido."),
        ("abc", "{F} ¿Cuántas mediciones están fuera de tolerancia?", "Una: M4", "Dos: M1 y M5", "Ninguna", "Solo M4 se aleja 3 cm; las demás están a 2 cm o menos."),
        ("=", "{F} ¿Cuál es la diferencia entre la medición mayor y la menor?", "303-298", "Se resta la menor de la mayor.", " cm"),
        ("abc", "{F} ¿Qué se hace con la medición M4?", "Se mantiene en el registro y se informa al supervisor", "Se borra porque no cumple", "Se cambia por 302", "Un registro conserva lo medido; el supervisor decide qué hacer."),
        ("abc", "{F} Una persona afirma que una pieza mide 3 mm más que lo esperado. ¿Se puede afirmar con este instrumento?", "No: su menor división es 1 cm y no distingue 3 mm", "Sí: se estima a ojo", "Sí: se multiplica por 10", "La división mínima de 1 cm limita la precisión; 3 mm es menos que eso."),
        ("ab", "{F} Un ayudante propone anotar 300 en lugar de 303 en M4 «para que no haya problemas». ¿Qué respuesta es correcta?", "No: se anota lo medido y se informa", "Sí: así se evita un reclamo", "Falsear un registro oculta un posible defecto."),
        ("abc", "{F} ¿Quién verifica la calibración del instrumento?", "Personal autorizado según la norma vigente y la empresa", "Cualquier ayudante que quiera", "Cada trabajador con su propio criterio", "La calibración la hace personal autorizado para que la referencia sea confiable."),
        ("=", "{F} Si el valor esperado fuera 450 cm con la misma tolerancia, ¿cuál es el valor máximo que cumple?", "450+2", "Se suma la tolerancia al valor esperado.", " cm"),
        ("abc", "{F} La medición M2 es 301 cm. ¿Cómo se escribe en metros y centímetros?", "3 m 1 cm", "30 m 1 cm", "3 m 10 cm", "301 cm son 3 m y 1 cm porque 3 m son 300 cm."),
    ],
    ctx=("abc", "En una obra de ejemplo dos mediciones de un mismo tramo dan 500 y 506 cm con tolerancia ±2 cm. ¿Qué corresponde?", "Registrar ambas e informar al supervisor", "Elegir la que cumple y borrar la otra", "Promediarlas y anotar un solo valor", "Ambas mediciones son datos; se registran y se informa la diferencia."),
    sc=[
        ("En Construcción: ¿qué es la tolerancia?", "El error máximo aceptado", "La tolerancia fija el límite de lo aceptable."),
        ("Un esperado es 200 cm y se midió 198 cm. ¿Cuál es el error?", "−2 cm", "Se resta el esperado al medido."),
        ("¿Se cambia un valor del registro para que cumpla?", "No, se anota lo medido", "Alterar el registro oculta un problema."),
    ],
    op=("Registro de ejemplo: largo esperado 250 cm; tolerancia ±3 cm; mediciones 251, 254, 247 y 250 cm. Escribe (a) el error de cada medición, (b) cuáles cumplen, (c) qué haces con las que no cumplen, (d) por qué no se corrige el registro.",
        "(a) +1, +4, −3 y 0 cm. (b) 251, 247 y 250 cm cumplen. (c) Las dejo en el registro e informo al supervisor. (d) Porque el registro debe reflejar lo medido y alterarlo oculta un problema.",
        ["calcula bien los errores", "decide con la tolerancia", "informa en vez de corregir", "explica la razón"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "olvidar el límite incluido", "borrar la medición"],
        "Pregunta: «¿cuál es el límite incluido?». Si no responde, pídele que relea la tolerancia."),
    reinforce="Inventa un registro de cinco mediciones con su tolerancia y escribe el error de cada una.",
    extend="Explica la diferencia entre precisión del instrumento y tolerancia del proyecto.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 8 (caso de ejemplo, inventado). Verificación de un piso en seis puntos de control. Altura de referencia 1000 mm; tolerancia ±3 mm. Alturas registradas: P1 = 1000 mm; "
     "P2 = 1002 mm; P3 = 1001 mm; P4 = 1005 mm; P5 = 999 mm; P6 = 1000 mm. Registro firmado por el ayudante A en una fecha de ejemplo. Falta anotar dónde está cada punto sobre el plano.")
build(
    O2, 3, F,
    use="Aprenderé a leer un caso de verificación de piso con puntos de control, a calcular desniveles y a decidir qué se informa.",
    prior=["Sé qué es error y tolerancia.", "Sé restar.", "Sé leer un registro."],
    explain=[
        "El desnivel es la diferencia de altura entre dos puntos. Un punto de control es un lugar elegido para medir y se identifica con un nombre, como P1. Para verificar la horizontalidad de un piso se compara la altura de cada punto con una altura de referencia, y cada punto debe cumplir por separado: que la mayoría cumpla no basta. La desviación de un punto es su diferencia con la referencia, sin importar el signo.",
        "El registro debe decir dónde está cada punto sobre el plano, porque sin esa ubicación nadie puede repetir la verificación en el mismo lugar. Si un punto no cumple, se deja en el registro y se informa; el registro no se corrige para que se vea mejor. Las medidas de este caso son de ejemplo y no son límites reales.",
        f"El caso se resuelve leyendo números en papel. {EMER} {AVISO}",
    ],
    vocab=[("desnivel", "diferencia de altura entre dos puntos"), ("punto de control", "lugar elegido para medir, con un nombre"), ("altura de referencia", "altura con la que se compara cada punto"), ("desviación", "diferencia de un punto con la referencia, sin signo"), ("milímetro (mm)", "milésima parte de un metro")],
    worked=[
        ("Calcular un desnivel", "En un caso de ejemplo, un punto está a 2010 mm y otro a 2004 mm. ¿Cuál es el desnivel?", ["Se resta la altura menor de la mayor.", "2010 menos 2004 es 6."], "6 mm"),
        ("Desviación de un punto", "La referencia de ejemplo es 500 mm y un punto marca 497 mm. ¿Cuál es su desviación?", ["Se calcula la diferencia con la referencia sin signo.", "500 menos 497 es 3."], "3 mm"),
    ],
    mistakes=[("Decir «la mayoría de los puntos cumple, entonces el piso cumple».", "Cada punto debe cumplir por separado.", "Revisa punto por punto."),
              ("Borrar un punto que no cumple para que el registro «se vea limpio».", "Borrar oculta un problema y deja de ser un registro confiable.", "Déjalo e informa al supervisor.")],
    T=[
        ("abc", "En Construcción: ¿qué es un desnivel?", "La diferencia de altura entre dos puntos", "La suma de las alturas de un piso", "El instrumento que mide la altura", "El desnivel compara dos alturas; no es una suma ni un instrumento."),
        ("abc", "¿Qué es un punto de control en la verificación de un piso?", "Un lugar elegido para medir, con un nombre", "El lugar donde se guardan los instrumentos", "Un punto de la hoja donde se firma", "El punto de control es un lugar de medición identificado por nombre."),
        ("abc", "¿Qué compara la desviación de un punto de un piso?", "Su altura con la altura de referencia", "Su nombre con el de otro punto", "La fecha con la hora", "La desviación es la diferencia de altura con la referencia."),
        ("=", "{F} ¿Cuál es el desnivel entre P4 y P5, en mm?", "1005-999", "Se resta la altura menor de la mayor.", " mm"),
        ("abc", "{F} ¿Qué punto supera la tolerancia de ±3 mm?", "P4", "P2", "P5", "P4 se desvía 5 mm; P2 se desvía 2 y P5 se desvía 1."),
        ("=", "{F} ¿Cuál es la desviación del punto P2, en mm?", "1002-1000", "Se resta la referencia a la altura de P2.", " mm"),
        ("=", "{F} Suma de las desviaciones de los seis puntos, en mm.", "0+2+1+5+1+0", "Se suman las desviaciones sin signo de P1 a P6.", " mm"),
        ("abc", "{F} El punto P5 mide 999 mm. ¿Cumple?", "Sí: se desvía 1 mm", "No: es menor que 1000", "No: se debe medir tres veces", "La desviación de 1 mm es menor que la tolerancia de 3 mm."),
        ("abc", "{F} ¿Qué se hace con P4?", "Dejarlo en el registro e informar al supervisor", "Borrarlo para que el registro quede limpio", "Cambiar su valor a 1003", "Un registro conserva lo medido y el supervisor decide."),
        ("ab", "{F} Un estudiante dice: «cinco de seis puntos cumplen, así que el piso cumple». ¿Qué respuesta es correcta?", "No: P4 no cumple y cada punto debe cumplir", "Sí: la mayoría decide", "Cada punto debe cumplir; un punto fuera de tolerancia basta para informar."),
        ("abc", "{F} ¿Qué dato falta para poder repetir la verificación en los mismos lugares?", "La ubicación de cada punto sobre el plano", "El color del piso", "El nombre del cliente", "Sin ubicación nadie sabe dónde estaba cada punto de control."),
        ("=", "{F} ¿Cuántos mm de ancho tiene el rango aceptado de alturas?", "1003-997", "Se resta el límite inferior del superior.", " mm"),
        ("abc", "{F} Alguien propone quitar P4 del registro para que parezca que todo cumple. ¿Qué corresponde?", "Rechazarlo: alterar un registro oculta un problema", "Aceptarlo si el supervisor no mira", "Aceptarlo si son pocos milímetros", "Un registro no se altera; ocultar un dato fuera de tolerancia es una falta."),
    ],
    ctx=("abc", "El ayudante A entrega el registro sin firmar. ¿Qué corresponde?", "Pedir que lo firme con su fecha antes de archivarlo", "Archivarlo igual", "Firmarlo otra persona por él", "La firma y la fecha hacen verificable quién midió y cuándo."),
    sc=[
        ("En Construcción: ¿qué es la desviación de un punto?", "Su diferencia con la altura de referencia", "Se calcula como diferencia con la referencia, sin considerar el signo."),
        ("¿Una altura de 1006 mm cumple con referencia 1000 y ±3?", "No", "Su desviación de 6 mm supera la tolerancia de 3 mm."),
        ("¿Cuántos puntos deben cumplir para que el piso cumpla?", "Todos", "Cada punto se verifica por separado."),
    ],
    op=("Caso de ejemplo: piso de un taller con referencia 2000 mm, tolerancia ±2 mm y cuatro puntos: Q1 = 2001, Q2 = 2003, Q3 = 1999, Q4 = 2000. Escribe (a) la desviación de cada punto, (b) qué puntos cumplen, (c) el desnivel entre Q2 y Q3, (d) qué haces con el punto que no cumple.",
        "(a) 1, 3, 1 y 0 mm. (b) Q1, Q3 y Q4 cumplen. (c) 2003 menos 1999 son 4 mm. (d) Lo dejo en el registro e informo al supervisor.",
        ["calcula las desviaciones", "decide con la tolerancia", "calcula el desnivel", "informa sin borrar"],
        ["hoja con las cuatro respuestas"],
        ["usar la mayoría como criterio", "borrar el punto", "restar mal"],
        "Pregunta: «¿cuántos puntos deben cumplir?». Si no responde, pídele que relea la regla."),
    reinforce="Inventa cinco alturas con su referencia y escribe la desviación de cada una.",
    extend="Explica por qué el registro debe indicar dónde está cada punto de control.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 9 (control de ejemplo, inventado). Recinto rectangular con lados esperados de 600 cm y 800 cm. Diagonal esperada: 1000 cm. Tolerancia de ±2 cm para lados y diagonales. "
     "Valores registrados: lados 600, 801, 799 y 600 cm; diagonales D1 = 1000 cm y D2 = 1004 cm.")
build(
    O2, 4, F,
    use="Aprenderé el criterio de las diagonales para saber si una esquina es recta y a leer un control con datos de ejemplo.",
    prior=["Sé qué es tolerancia y error.", "Sé multiplicar.", "Sé sumar los lados de un rectángulo."],
    explain=[
        "En un rectángulo, las dos diagonales miden lo mismo. Si al medirlas dan valores distintos, el recinto no es un rectángulo perfecto y alguna esquina no es recta. Las diagonales sirven para controlar, no para corregir. Existe una relación entre los lados y la diagonal de un rectángulo: con lados de 3 y 4 unidades, la diagonal mide 5. Los múltiplos funcionan igual: lados de 6 y 8 dan diagonal de 10; lados de 9 y 12 dan diagonal de 15. Esta es la regla 3-4-5.",
        "Para decidir, se compara cada valor con el esperado dentro de la tolerancia y también las dos diagonales entre sí. Si una diagonal queda fuera de tolerancia, se registra y se informa al supervisor; quien decide qué se corrige y quién lo hace es el responsable de la obra. Este cuaderno no enseña cómo medir ni cómo corregir una esquina.",
        f"Todos los valores son de ejemplo para practicar la lectura. {EMER} {AVISO}",
    ],
    vocab=[("diagonal", "línea que une dos esquinas opuestas"), ("regla 3-4-5", "lados 3 y 4 dan diagonal 5; sus múltiplos también"), ("rectángulo", "figura de cuatro lados con esquinas rectas"), ("esquina recta", "esquina de 90 grados")],
    worked=[
        ("Aplicar la regla", "Un recinto de ejemplo tiene lados de 300 y 400 cm. ¿Cuánto debe medir su diagonal?", ["300 y 400 son 3 y 4 multiplicados por 100.", "La diagonal es 5 por 100."], "500 cm"),
        ("Comparar diagonales", "En un control de ejemplo, las diagonales miden 700 y 701 cm con tolerancia ±2. ¿Se pueden aceptar?", ["La diferencia entre las diagonales es 1 cm.", "1 es menor que la tolerancia."], "Sí, están dentro de la tolerancia"),
    ],
    mistakes=[("Pensar que si una diagonal está bien, la otra también.", "Cada diagonal se compara por separado y entre sí.", "Revisa las dos."),
              ("Intentar corregir una esquina sin autorización.", "Esa decisión es del responsable de la obra.", "Registra e informa al supervisor.")],
    T=[
        ("abc", "En Construcción: ¿qué se cumple en las diagonales de un rectángulo?", "Miden lo mismo", "Una mide el doble de la otra", "Son siempre iguales a un lado", "En un rectángulo las dos diagonales son iguales; las otras opciones no ocurren."),
        ("abc", "¿Qué indica que las dos diagonales midan distinto?", "Que alguna esquina no es recta", "Que el plano está bien", "Que el instrumento mide más", "Una diferencia entre diagonales señala que el recinto no es un rectángulo perfecto."),
        ("abc", "Según la regla 3-4-5, con lados de 3 y 4 unidades, ¿cuánto mide la diagonal?", "5 unidades", "7 unidades", "12 unidades", "La regla dice que la diagonal es 5; 7 es la suma de los lados y 12 su producto."),
        ("=", "{F} ¿Cuál es la diferencia entre D2 y D1, en cm?", "1004-1000", "Se resta la menor de la mayor.", " cm"),
        ("abc", "{F} D2 mide 1004 cm. ¿Cumple?", "No: se aleja 4 cm de 1000", "Sí: se aleja 4 cm", "Sí: cumple si D1 cumple", "La tolerancia es ±2 cm y 4 cm la supera."),
        ("=", "{F} ¿Cuál es el perímetro registrado, en cm?", "600+801+799+600", "Se suman los cuatro lados registrados.", " cm"),
        ("=", "{F} ¿Cuántos m² tiene el recinto con los lados esperados?", "6*8", "Los lados esperados son 6 m y 8 m.", " m²"),
        ("abc", "{F} ¿Entre qué valores cumple una diagonal?", "Entre 998 y 1002 cm", "Entre 1000 y 1004 cm", "Solo en 1000 cm", "Con ±2 cm de tolerancia el rango va de 998 a 1002."),
        ("abc", "{F} Los lados registrados son 801 y 799 cm. ¿Cumplen?", "Sí: se desvían 1 cm cada uno", "No: no miden 800", "Solo uno cumple", "Ambos están a 1 cm del valor esperado, dentro de ±2 cm."),
        ("ab", "{F} Un ayudante dice: «D1 está bien, así que no importa D2». ¿Qué respuesta es correcta?", "No: D2 también se revisa y no cumple", "Sí: basta con una diagonal", "Las dos diagonales deben revisarse porque se comparan entre sí."),
        ("abc", "{F} ¿Qué se hace con la diferencia detectada en D2?", "Registrarla e informarla al supervisor", "Corregir la esquina por cuenta propia", "Ignorarla por ser de 4 cm", "El supervisor decide qué se corrige y quién lo hace."),
        ("=", "{F} Con la regla 3-4-5, un recinto de 900 cm por 1200 cm, ¿cuánto mide su diagonal?", "5*300", "Los lados son 3 y 4 por 300; la diagonal es 5 por 300.", " cm"),
        ("abc", "{F} ¿Por qué una diferencia de 4 cm entre diagonales es una señal importante?", "Porque indica que alguna esquina no es recta", "Porque el recinto cambió de tamaño", "Porque el instrumento se dañó siempre", "Una diferencia de diagonales apunta a una esquina fuera de escuadra y debe informarse."),
    ],
    ctx=("abc", "En una obra de ejemplo las diagonales de un recinto miden 500 y 508 cm con tolerancia ±2 cm. ¿Qué corresponde?", "Registrar e informar al supervisor", "Promediar y anotar 504", "Medir hasta que den igual", "La diferencia de 8 cm supera la tolerancia; se registra e informa."),
    sc=[
        ("En Construcción: ¿cómo son las diagonales de un rectángulo?", "Iguales", "Las dos diagonales de un rectángulo miden lo mismo."),
        ("Con lados de 6 y 8, ¿cuánto mide la diagonal?", "10", "Es el doble de 3, 4 y 5, por la regla de los múltiplos."),
        ("¿Quién decide qué corregir si una esquina no es recta?", "El responsable de la obra, informado por el supervisor", "No decide el trabajador por su cuenta."),
    ],
    op=("Control de ejemplo: recinto de 1200 cm por 1600 cm, diagonal esperada de 2000 cm, tolerancia ±3 cm. Registrado: diagonales 2001 y 2005 cm. Escribe (a) cuántos cm de diferencia hay entre las diagonales, (b) qué diagonales cumplen, (c) qué indica la diferencia, (d) qué haces.",
        "(a) 2005 menos 2001 son 4 cm. (b) 2001 cumple (1 cm) y 2005 no (5 cm). (c) Que alguna esquina no es recta. (d) Registro e informo al supervisor.",
        ["calcula la diferencia", "decide con la tolerancia", "interpreta la señal", "informa sin corregir"],
        ["hoja con las cuatro respuestas"],
        ["revisar una sola diagonal", "corregir por su cuenta", "restar mal"],
        "Pregunta: «¿cuál está fuera del límite?». Si no responde, pídele que relea la tolerancia."),
    reinforce="Escribe la diagonal de tres recintos de lados múltiplos de 3 y 4 que inventes.",
    extend="Explica por qué las diagonales sirven para controlar y no para decidir una corrección.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 10 (obra de ejemplo, inventada). Obra «Escuela Rural Mañío» (ficticia): un edificio de un piso de 20 m por 10 m en un terreno de 40 m de frente por 30 m de fondo. "
     "Documentos: plano de emplazamiento, plano de fundaciones, planilla de ejes y cuaderno de topografía. Riesgos anotados en el terreno: caída a un desnivel o a una excavación, atropello por maquinaria y golpe por objetos.")
build(
    O3, 1, F,
    use="Aprenderé qué es un trazado, para qué sirven los puntos de referencia y los niveles, y qué riesgos tiene un terreno antes de leer cualquier medida.",
    prior=["Sé leer planos y registros de medición.", "Sé calcular áreas de rectángulos.", "Sé qué es una tolerancia."],
    explain=[
        "El trazado es la marcación sobre el terreno de dónde irá cada parte de una obra, siguiendo los planos. El replanteo es pasar las medidas del plano al terreno. El emplazamiento es la ubicación de la obra dentro del terreno. Un punto de referencia es un punto fijo y conocido desde el cual se miden distancias y alturas. El nivel es la altura de un punto respecto de una referencia. Hay trazados de edificación, de obras viales, de fundaciones, de estructuras y de elementos como moldajes y enfierraduras, siempre según planos estructurales o de terminaciones.",
        "Los documentos del trazado son el plano de emplazamiento, el de fundaciones, la planilla de ejes y el cuaderno de topografía, que es el registro de lo medido en terreno. Cada medida se lee de los planos y se compara con lo registrado; nadie cambia una referencia por su cuenta. El terreno tiene riesgos: caídas a desniveles o excavaciones, atropello por maquinaria y golpes por objetos. Las reglas de seguridad las fija la norma vigente y las exige la entidad fiscalizadora.",
        f"Aquí solo se aprenden conceptos y lectura de documentos; no se ejecuta ningún trazado. {EMER} {AVISO}",
    ],
    vocab=[("trazado", "marcación en el terreno de dónde irá cada parte de la obra"), ("replanteo", "paso de las medidas del plano al terreno"), ("emplazamiento", "ubicación de la obra dentro del terreno"), ("punto de referencia", "punto fijo y conocido desde el cual se miden distancias y alturas"), ("nivel", "altura de un punto respecto de una referencia"), ("cuaderno de topografía", "registro de lo medido en el terreno")],
    worked=[
        ("Elegir el documento", "Un jefe de obra de ejemplo quiere saber en qué lugar del terreno queda el edificio. ¿Qué plano consulta?", ["La ubicación dentro del terreno se llama emplazamiento.", "Está en el plano de emplazamiento."], "El plano de emplazamiento"),
        ("Calcular un área", "Un terreno de ejemplo mide 25 m por 18 m. ¿Cuántos m² tiene?", ["Se multiplica el largo por el ancho del terreno.", "25 por 18 son 450."], "450 m²"),
    ],
    mistakes=[("Mover o reemplazar un punto de referencia «porque estorba».", "Todas las medidas dependen de él; moverlo cambia la obra.", "Informa al supervisor y espera su decisión."),
              ("Acercarse al borde de una excavación para mirar mejor.", "El borde puede ceder y hay riesgo de caída.", "Mantente fuera de la zona señalizada y avisa si ves algo extraño.")],
    T=[
        ("abc", "En Construcción: ¿qué es el trazado de una obra?", "La marcación sobre el terreno de dónde irá cada parte, según los planos", "El dibujo de los planos de arquitectura", "La compra de los materiales de la obra", "El trazado pasa lo dibujado al terreno; el dibujo y la compra son otras etapas."),
        ("abc", "En Construcción: ¿qué significa emplazamiento?", "La ubicación de la obra dentro del terreno", "El tipo de hormigón de la fundación", "El nombre del dueño del terreno", "El emplazamiento se refiere a dónde queda la obra; no a materiales ni dueños."),
        ("abc", "¿Para qué sirve un punto de referencia?", "Para medir distancias y alturas desde un punto fijo y conocido", "Para marcar dónde se guardan los materiales", "Para indicar quién firmó el plano", "El punto de referencia es la base de las medidas; no ubica bodegas ni firmas."),
        ("=", "{F} ¿Cuántos m² tiene el terreno?", "40*30", "Se multiplica el frente por el fondo.", " m²"),
        ("abc", "{F} ¿Qué plano muestra dónde queda el edificio dentro del terreno?", "El plano de emplazamiento", "El plano de fundaciones", "La planilla de ejes", "El emplazamiento ubica la obra en el terreno; las otras piezas tratan de apoyos o distancias entre ejes."),
        ("abc", "{F} ¿Qué riesgos anota la ficha para el terreno?", "Caída a desnivel o excavación, atropello por maquinaria y golpe por objetos", "Solo el calor del verano", "Caída a desnivel y falta de agua potable", "La ficha nombra tres riesgos concretos; las otras opciones agregan algo que no nombra."),
        ("=", "{F} ¿Cuántos m² del terreno quedan sin edificio?", "40*30-20*10", "Se resta el área del edificio del área del terreno.", " m²"),
        ("abc", "{F} Una persona quiere acercarse al borde de una excavación abierta «solo para mirar». ¿Qué corresponde?", "No hacerlo: mantenerse fuera de la zona señalizada y avisar al supervisor", "Hacerlo si lleva casco", "Hacerlo si es rápido", "El borde puede ceder; el casco no evita la caída ni reemplaza la zona señalizada."),
        ("abc", "{F} Una máquina movió el punto de referencia. ¿Qué corresponde?", "Informar al supervisor y no trazar hasta aclararlo", "Ponerlo de nuevo donde parecía estar", "Seguir sin él", "Una referencia movida invalida las medidas; la repone solo quien corresponde."),
        ("ab", "{F} Un estudiante dice: «sé leer el plano de fundaciones, así que puedo trazar solo». ¿Qué respuesta es correcta?", "No: leer planos no habilita; el trazado lo hace personal autorizado", "Sí: leer planos basta para trazar", "El trazado exige personal autorizado, norma vigente y equipos adecuados."),
        ("abc", "En una obra de ejemplo se desmorona la pared de una excavación y alguien queda atrapado. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Bajar de inmediato a sacarlo", "Esperar a que la pared se asiente antes de avisar", "Entrar o esperar pone a más personas en peligro; se mantiene la distancia y se avisa de inmediato."),
        ("=", "{F} Se cerca todo el terreno. ¿Cuántos metros mide el cerco?", "2*(40+30)", "El perímetro es dos veces la suma del frente y el fondo.", " m"),
        ("abc", "{F} ¿Qué documento da las distancias entre ejes?", "La planilla de ejes", "El plano de emplazamiento", "El cuaderno de topografía", "La planilla de ejes lista las distancias; el cuaderno solo registra lo medido en terreno."),
    ],
    ctx=("abc", "Un conductor de ejemplo estaciona un camión sobre un punto de referencia marcado. ¿Qué corresponde?", "Pedir que se retire y avisar al supervisor para verificar el punto", "Dejarlo y seguir midiendo desde ese punto", "Mover el punto unos centímetros", "Un punto aplastado o movido pierde validez y debe verificarse."),
    sc=[
        ("En Construcción: ¿qué es el replanteo?", "Pasar las medidas del plano al terreno", "El replanteo traslada lo dibujado al terreno."),
        ("Un terreno de 10 m por 12 m, ¿cuántos m² tiene?", "120 m²", "Se multiplica el largo por el ancho del terreno."),
        ("¿Quién mueve un punto de referencia?", "Nadie por su cuenta: lo decide el supervisor", "Todas las medidas dependen de ese punto."),
    ],
    op=("Obra de ejemplo «Taller Boldo»: terreno de 20 m por 15 m; edificio de 10 m por 6 m. Riesgos anotados: caída a una zanja y atropello por maquinaria. Escribe (a) cuántos m² tiene el terreno, (b) cuántos m² quedan libres, (c) qué documento te dice dónde queda el edificio en el terreno, (d) qué haces si ves que se movió el punto de referencia.",
        "(a) 20 por 15 son 300 m². (b) 300 menos 60 son 240 m². (c) El plano de emplazamiento. (d) No sigo; aviso al supervisor para verificarlo.",
        ["calcula el área del terreno", "calcula el área libre", "nombra el documento correcto", "informa sin mover la referencia"],
        ["hoja con las cuatro respuestas"],
        ["olvidar restar el edificio", "confundir plano con planilla", "mover la referencia"],
        "Pregunta: «¿qué documento ubica el edificio?». Si no responde, pídele que relea el emplazamiento."),
    reinforce="Escribe tres frases sobre qué es el trazado, el replanteo y el punto de referencia.",
    extend="Explica por qué un error de 5 cm en un punto de referencia puede repetirse en toda la obra.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 11 (planilla de ejemplo, inventada). Planilla de ejes de un edificio de ejemplo. Ejes de la dirección larga: A, B, C y D; distancias entre ejes consecutivos: A-B = 400 cm; B-C = 500 cm; C-D = 400 cm. "
     "Ejes de la dirección corta: 1 y 2; distancia 1-2 = 600 cm. Punto de referencia PR-1 con cota 1000 cm. Nivel de piso terminado (NPT) = 1020 cm.")
build(
    O3, 2, F,
    use="Aprenderé el vocabulario del trazado (ejes, planilla, cota, nivel de piso terminado, moldaje y enfierradura) y a leer una planilla de ejes.",
    prior=["Sé qué es un trazado y un punto de referencia.", "Sé sumar longitudes.", "Sé leer tablas."],
    explain=[
        "Un eje es una línea de referencia del plano sobre la que se ubican muros, pilares o fundaciones. Los ejes se nombran con letras en una dirección y con números en la otra. La planilla de ejes anota la distancia entre ejes consecutivos. Para saber la distancia entre dos ejes no vecinos se suman las distancias intermedias. La cota es la altura de un punto respecto de una referencia. El nivel de piso terminado, o NPT, es la altura que tendrá el piso al terminar la obra.",
        "El moldaje es el molde provisorio que da forma al hormigón fresco. La enfierradura es el conjunto de barras de acero que van dentro del hormigón. Ambos se ubican con el trazado, pero este cuaderno no enseña cómo se arman ni se instalan: es trabajo de personal autorizado con norma vigente. Ningún valor de una planilla se cambia por cuenta propia; si algo no coincide, se informa al proyectista o al supervisor.",
        f"Todas las cifras son de ejemplo y sirven para sumar en papel. {EMER} {AVISO}",
    ],
    vocab=[("eje", "línea de referencia del plano donde se ubican muros, pilares o fundaciones"), ("planilla de ejes", "tabla con las distancias entre ejes"), ("cota", "altura de un punto respecto de una referencia"), ("NPT", "nivel de piso terminado: altura del piso al terminar la obra"), ("moldaje", "molde provisorio que da forma al hormigón fresco"), ("enfierradura", "conjunto de barras de acero que van dentro del hormigón")],
    worked=[
        ("Sumar distancias", "En una planilla de ejemplo, A-B = 300 cm y B-C = 450 cm. ¿Cuál es la distancia A-C?", ["Se suman las distancias intermedias.", "300 más 450 son 750."], "750 cm"),
        ("Diferencia de cotas", "Un punto de ejemplo tiene cota 2000 cm y la referencia vale 1985 cm. ¿Cuántos cm la supera?", ["Se resta la referencia a la cota.", "2000 menos 1985 es 15."], "15 cm"),
    ],
    mistakes=[("Medir la distancia entre ejes no vecinos como si fuera una sola cifra de la planilla.", "La planilla anota solo ejes consecutivos.", "Suma las distancias intermedias."),
              ("Elegir un punto de referencia propio para «ahorrar tiempo».", "Distintos puntos dan medidas distintas y mezclan niveles.", "Usa solo el punto de referencia del proyecto.")],
    T=[
        ("abc", "En Construcción: ¿qué es un eje en un plano de trazado?", "Una línea de referencia donde se ubican muros, pilares o fundaciones", "Una pieza de acero de la estructura", "La escala del plano", "El eje es una línea del plano; no es una pieza ni la escala."),
        ("abc", "En Construcción: ¿qué es un moldaje?", "Un molde provisorio que da forma al hormigón fresco", "Un revestimiento permanente de un muro", "Una herramienta para medir", "El moldaje da forma al hormigón fresco y luego se retira; no es revestimiento ni instrumento."),
        ("abc", "En Construcción: ¿qué es la enfierradura?", "El conjunto de barras de acero que van dentro del hormigón", "El conjunto de tablas que sostienen la techumbre", "La pintura de los fierros visibles", "La enfierradura es el acero interior del hormigón; no son tablas ni pintura."),
        ("=", "{F} ¿Cuál es la distancia entre los ejes A y D, en cm?", "400+500+400", "Se suman las tres distancias consecutivas.", " cm"),
        ("=", "{F} ¿Cuál es la distancia entre los ejes A y C, en cm?", "400+500", "Se suman las distancias A-B y B-C.", " cm"),
        ("abc", "{F} ¿Qué es PR-1 en la ficha?", "El punto fijo desde el que se miden los niveles", "Un eje del edificio", "El nivel de piso terminado", "PR-1 es el punto de referencia; los ejes llevan letras o números."),
        ("=", "{F} ¿Cuántos cm sobre PR-1 está el nivel de piso terminado?", "1020-1000", "Se resta la cota del punto de referencia a la del NPT.", " cm"),
        ("=", "{F} ¿Cuántos m² encierran los ejes A a D y 1 a 2? Pasa antes cada distancia a metros (100 cm son 1 m).", "(4+5+4)*6", "1300 cm son 13 m y 600 cm son 6 m; se multiplican el largo y el ancho.", " m²"),
        ("abc", "{F} PR-1 se mueve por un golpe de maquinaria. ¿Qué corresponde?", "Avisar al supervisor y verificar la referencia antes de seguir", "Seguir con las medidas porque casi no se movió", "Reemplazarlo por un punto elegido a ojo", "Si la referencia cambia, todas las medidas dejan de ser válidas."),
        ("ab", "{F} Un ayudante propone usar su propio punto de referencia cercano «para caminar menos». ¿Qué respuesta es correcta?", "No: se usa solo el punto de referencia del proyecto", "Sí: da lo mismo cualquier punto", "Distintos puntos dan medidas y niveles distintos que no se pueden mezclar."),
        ("abc", "{F} ¿Quién autoriza un cambio en la distancia entre los ejes B y C?", "El proyectista, con conocimiento del supervisor", "El ayudante que hace el trazado", "El primero que se dé cuenta", "Las distancias entre ejes son parte del diseño y las cambia solo quien diseña."),
        ("=", "{F} Si se agregara un eje E a 400 cm del D, ¿cuál sería la distancia entre A y E, en cm?", "400+500+400+400", "Se suman las cuatro distancias consecutivas.", " cm"),
        ("abc", "{F} La planilla dice B-C = 500 cm y otro plano dice 450 cm. ¿Qué se hace?", "Anotar la discrepancia e informar al proyectista o al supervisor", "Usar la menor", "Usar la que sale más cómoda", "Ante una discrepancia no se elige un valor: se informa para que decida quien diseña."),
    ],
    ctx=("abc", "Un estudiante en práctica ve una estaca con cinta en un terreno y piensa que es una basura. ¿Qué corresponde?", "No tocarla y preguntar al supervisor qué es", "Retirarla para despejar", "Moverla a un costado", "Las marcas del terreno pueden ser referencias; no se tocan sin preguntar."),
    sc=[
        ("En Construcción: ¿qué es el NPT?", "El nivel de piso terminado", "Es la altura que tendrá el piso al terminar la obra."),
        ("Con A-B = 200 cm y B-C = 300 cm, ¿cuánto mide A-C?", "500 cm", "Se suman las distancias intermedias entre los ejes."),
        ("¿Quién cambia una distancia entre ejes?", "El proyectista", "Las distancias son parte del diseño."),
    ],
    op=("Planilla de ejemplo: ejes A, B, C; A-B = 350 cm; B-C = 450 cm. Eje 1 y 2 a 500 cm. PR-1 cota 800 cm; NPT = 815 cm. Escribe (a) la distancia A-C, (b) el área encerrada por A-C y 1-2 en m², (c) cuántos cm sobre PR-1 está el NPT, (d) qué haces si el plano de fundaciones dice B-C = 400 cm.",
        "(a) 350 más 450 son 800 cm. (b) 800 por 500 son 400.000 cm², es decir, 40 m². (c) 815 menos 800 son 15 cm. (d) Anoto la discrepancia e informo al proyectista o al supervisor.",
        ["suma las distancias", "calcula el área", "calcula la diferencia de cota", "informa la discrepancia"],
        ["hoja con las cuatro respuestas"],
        ["no sumar distancias intermedias", "olvidar pasar a m²", "elegir un valor por su cuenta"],
        "Pregunta: «¿cómo sacaste A-C?». Si no responde, pídele que relea el vocabulario de planilla de ejes."),
    reinforce="Inventa una planilla con cuatro ejes y calcula la distancia entre el primero y el último.",
    extend="Explica por qué mezclar dos puntos de referencia puede desplazar una obra completa.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 12 (caso de ejemplo, inventado). Obra «Escuela Rural Mañío». Planilla de ejes: A-B = 400 cm; B-C = 500 cm. Plano de fundaciones: A-B = 400 cm; B-C = 450 cm. "
     "Plano de emplazamiento: el edificio queda a 300 cm del deslinde sur, y el mínimo de ejemplo es 250 cm. Cuaderno de topografía: PR-1 = 1000 cm y PR-2 = 1004 cm; según la planilla ambos deberían tener la misma cota.")
build(
    O3, 3, F,
    use="Aprenderé a leer un caso de trabajo en papel con datos que no coinciden y a decidir qué se registra y a quién se informa antes de trazar.",
    prior=["Sé qué es una discrepancia.", "Sé leer una planilla de ejes.", "Sé qué es un punto de referencia."],
    explain=[
        "El deslinde es el límite del terreno. El plano de emplazamiento indica a qué distancia queda el edificio del deslinde y la norma vigente fija una distancia mínima; en este cuaderno el mínimo es solo de ejemplo. Antes de ubicar cualquier eje, se cruzan los documentos: planilla de ejes, plano de fundaciones, emplazamiento y cuaderno de topografía. Si un dato no coincide, hay una discrepancia que se registra y se informa.",
        "Dos puntos de referencia que según el proyecto tienen la misma cota deben dar lo mismo al compararlos. Si no coinciden, no se sigue hasta aclarar cuál es el correcto: lo decide el supervisor o el profesional responsable. El registro de la discrepancia incluye los documentos, los valores, quién la detectó y la fecha. Esta lectura se hace en papel y no autoriza a trazar.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("deslinde", "límite del terreno"), ("distancia mínima", "menor distancia permitida; el valor real lo fija la norma vigente"), ("discrepancia", "diferencia entre documentos sobre un mismo dato"), ("cruzar documentos", "comparar un mismo dato en varios documentos")],
    worked=[
        ("Cruzar datos", "La planilla de ejemplo dice 300 cm y el plano dice 320 cm para una misma distancia. ¿Cuál es la diferencia?", ["Se restan los dos valores.", "320 menos 300 es 20."], "20 cm"),
        ("Verificar una distancia mínima", "Un edificio de ejemplo queda a 400 cm del deslinde y el mínimo de ejemplo es 350 cm. ¿Cumple?", ["Se compara la distancia real con el mínimo.", "400 es mayor que 350."], "Sí, cumple"),
    ],
    mistakes=[("Elegir la distancia menor «para estar seguros».", "La decisión no es de quien traza; elegir mal puede cambiar la ubicación de la obra.", "Informa la discrepancia y espera la decisión."),
              ("Trazar con dos puntos de referencia que no coinciden.", "Los niveles quedarían desplazados.", "Detén y consulta cuál es el punto válido.")],
    T=[
        ("abc", "En Construcción: ¿qué es el deslinde de un terreno?", "Su límite", "El punto más alto del terreno", "La pendiente del terreno", "El deslinde es el límite; la altura y la pendiente son otras características."),
        ("abc", "En Construcción: ¿qué significa cruzar documentos?", "Comparar un mismo dato en varios documentos", "Firmar varios documentos a la vez", "Archivar los planos en cruz", "Cruzar es comparar un dato entre documentos para detectar diferencias."),
        ("abc", "{F} ¿Entre qué documentos hay una discrepancia de distancia?", "Entre la planilla de ejes y el plano de fundaciones", "Entre el emplazamiento y la planilla", "Entre el cuaderno y el emplazamiento", "La distancia B-C difiere entre planilla y fundaciones; los otros datos no se contradicen entre sí."),
        ("=", "{F} ¿Cuántos cm de diferencia hay en B-C entre la planilla y el plano de fundaciones?", "500-450", "Se resta el valor menor del mayor.", " cm"),
        ("=", "{F} ¿Cuál sería la diferencia en la distancia A-C según una y otra fuente?", "(400+500)-(400+450)", "Se calcula A-C con cada valor de B-C y se restan.", " cm"),
        ("abc", "{F} El edificio queda a 300 cm del deslinde sur y el mínimo de ejemplo es 250. ¿Cumple?", "Sí: sobran 50 cm", "No: debe estar a 300 exactos", "No: debe estar a más de 400", "La distancia real supera el mínimo en 50 cm."),
        ("=", "{F} ¿Cuántos cm sobran sobre el mínimo?", "300-250", "Se resta el mínimo a la distancia real.", " cm"),
        ("=", "{F} ¿Cuántos cm de diferencia hay entre PR-2 y PR-1?", "1004-1000", "Se resta la menor de la mayor.", " cm"),
        ("abc", "{F} Según la planilla PR-1 y PR-2 deben tener la misma cota. ¿Qué corresponde?", "Informar al supervisor y no trazar hasta aclarar cuál es válido", "Usar el promedio de los dos", "Elegir PR-2 porque es mayor", "Con dos referencias que no coinciden las medidas no son confiables; decide el supervisor."),
        ("ab", "{F} Un ayudante propone usar B-C = 450 cm «por ser el menor y evitar problemas». ¿Qué respuesta es correcta?", "No: la discrepancia se informa y decide quien diseña", "Sí: lo menor es lo más seguro", "Elegir por criterio propio no es una decisión de quien traza."),
        ("abc", "{F} ¿Qué debe incluir el registro de la discrepancia de B-C?", "Los documentos, los dos valores, quién la detectó y la fecha", "Solo la distancia menor", "El nombre del dueño del terreno", "Un registro útil deja constancia de qué, dónde, quién y cuándo."),
        ("=", "{F} Si A-C según la planilla fuera lado de un recinto y el otro lado midiera 600 cm, ¿cuántos metros mediría el perímetro?", "2*(900+600)//100", "El perímetro es el doble de la suma de los lados, pasado a metros.", " m"),
        ("abc", "{F} ¿Qué documento se consulta para saber la distancia mínima al deslinde de este caso?", "El plano de emplazamiento", "La planilla de ejes", "El cuaderno de topografía", "La distancia al deslinde está en el emplazamiento; la planilla trata de ejes."),
    ],
    ctx=("abc", "El dueño del terreno de ejemplo pide a un estudiante «mover un poco» los ejes para conservar un árbol. ¿Qué responde?", "Que cualquier cambio lo decide el proyectista y se informa al supervisor", "Que lo hará si el dueño firma una hoja", "Que lo hará pero en secreto", "Los ejes son parte del diseño; un cambio informal puede romper el proyecto."),
    sc=[
        ("En Construcción: ¿qué es el deslinde?", "El límite del terreno", "El deslinde marca el borde del terreno."),
        ("Con valores 250 y 260 para una misma distancia, ¿cuál es la diferencia?", "10", "Se resta el menor del mayor."),
        ("¿Quién decide qué documento se corrige?", "El proyectista o el supervisor", "La decisión no corresponde a quien traza la obra."),
    ],
    op=("Caso de ejemplo: planilla de ejes A-B = 600 cm; plano de fundaciones A-B = 620 cm; distancia al deslinde 280 cm con mínimo de ejemplo 250 cm. Escribe (a) la diferencia de A-B, (b) si la distancia al deslinde cumple, (c) qué datos anotas en el registro, (d) a quién informas.",
        "(a) 620 menos 600 son 20 cm. (b) Sí, sobran 30 cm. (c) Los dos documentos, 600 y 620, quién la detectó y la fecha. (d) Al proyectista o al supervisor.",
        ["calcula la diferencia", "compara con el mínimo", "registra completo", "informa a quien decide"],
        ["hoja con las cuatro respuestas"],
        ["elegir un valor", "no anotar la fecha", "olvidar informar"],
        "Pregunta: «¿qué falta en tu registro?». Si no responde, pídele que relea qué contiene."),
    reinforce="Inventa dos documentos que dicen distancias distintas y escribe el registro de la discrepancia.",
    extend="Explica por qué dos puntos de referencia que no coinciden detienen un trazado.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 13 (niveles de ejemplo, inventados). Punto de referencia PR-1 con cota 1000 cm. Terreno natural en el sitio: cota 960 cm. Nivel de piso terminado (NPT) del edificio: 1020 cm. "
     "Parte baja de la fundación: 100 cm más abajo que el terreno natural.")
build(
    O3, 4, F,
    use="Aprenderé a comparar cotas y niveles con datos de ejemplo, a calcular diferencias de altura y a decidir qué se informa.",
    prior=["Sé qué es una cota y el NPT.", "Sé restar.", "Sé leer un plano de fundaciones descrito por escrito."],
    explain=[
        "Los niveles se comparan siempre con la misma referencia. La diferencia de nivel entre dos puntos se calcula restando la cota menor de la mayor. Un punto que está más abajo que otro tiene una cota menor. El terreno natural es el terreno antes de intervenirlo. La parte baja de una fundación es la altura más profunda donde esta apoya. Con las cotas se obtiene, por ejemplo, cuánto sobresale el piso terminado sobre el terreno natural.",
        "Si el proyecto cambia un nivel, el cambio lo decide el proyectista y se registra. Quien lee las cotas no las modifica. En el cuaderno de topografía se anotan los niveles medidos y se comparan con los del plano. Una diferencia fuera de tolerancia se informa. Este cuaderno no enseña cómo se miden niveles en terreno.",
        f"Todas las cotas son de ejemplo y sirven solo para practicar la resta. {EMER} {AVISO}",
    ],
    vocab=[("terreno natural", "terreno antes de intervenirlo"), ("parte baja de la fundación", "altura más profunda donde apoya la fundación"), ("diferencia de nivel", "resta entre la cota mayor y la menor"), ("cota", "altura de un punto respecto de una referencia")],
    worked=[
        ("Diferencia de nivel", "Un punto de ejemplo está en cota 1500 cm y otro en 1430 cm. ¿Cuál es la diferencia de nivel?", ["Se resta la cota menor de la mayor.", "1500 menos 1430 es 70."], "70 cm"),
        ("Cota más baja", "Si una fundación de ejemplo apoya 80 cm bajo un terreno de cota 1200 cm, ¿cuál es su cota baja?", ["Se resta la profundidad a la cota del terreno.", "1200 menos 80 es 1120."], "1120 cm"),
    ],
    mistakes=[("Restar con referencias distintas.", "Si cada dato usa otra referencia, la diferencia no tiene sentido.", "Verifica que todas las cotas usen la misma referencia."),
              ("Cambiar el NPT «porque conviene».", "El nivel de piso es parte del diseño.", "Informa la duda al proyectista o al supervisor.")],
    T=[
        ("abc", "En Construcción: ¿qué es el terreno natural?", "El terreno antes de intervenirlo", "El terreno ya nivelado para construir", "El terreno con la obra terminada", "El terreno natural es el original; nivelado o terminado son estados posteriores."),
        ("abc", "¿Qué indica una cota menor entre dos puntos?", "Que el punto está más abajo", "Que el punto está más lejos", "Que el punto es más antiguo", "La cota es la altura; una cota menor es una posición más baja."),
        ("abc", "¿Cómo se calcula la diferencia de nivel entre dos puntos?", "Restando la cota menor de la mayor", "Sumando las dos cotas", "Multiplicando las cotas", "La diferencia entre alturas es una resta; sumar o multiplicar no tiene sentido."),
        ("=", "{F} ¿Cuántos cm sobre el terreno natural queda el NPT?", "1020-960", "Se resta la cota del terreno a la del NPT.", " cm"),
        ("=", "{F} ¿Cuál es la cota de la parte baja de la fundación, en cm?", "960-100", "Se resta la profundidad a la cota del terreno natural.", " cm"),
        ("=", "{F} ¿Cuántos cm hay entre el NPT y la parte baja de la fundación?", "1020-(960-100)", "Se calcula la cota baja y se resta del NPT.", " cm"),
        ("abc", "{F} El terreno natural tiene cota 960 y PR-1 vale 1000. ¿Dónde está el terreno?", "40 cm bajo PR-1", "40 cm sobre PR-1", "A la misma altura que PR-1", "960 es menor que 1000 en 40, por lo que está más abajo."),
        ("abc", "{F} ¿Cuál es la cota más alta de la ficha?", "El NPT, con 1020 cm", "PR-1, con 1000 cm", "El terreno natural, con 960 cm", "1020 es la cifra mayor entre las cotas de la ficha."),
        ("=", "{F} ¿Cuántos cm bajo PR-1 queda la parte baja de la fundación?", "1000-860", "La parte baja está en 860 y PR-1 vale 1000.", " cm"),
        ("ab", "{F} Un ayudante dice: «subo el NPT 5 cm porque así queda más lindo». ¿Qué respuesta es correcta?", "No: el NPT lo define el proyectista y se informa la propuesta", "Sí: 5 cm no afectan nada", "El nivel de piso terminado es parte del diseño y no lo cambia quien ejecuta."),
        ("abc", "{F} ¿Qué se anota en el cuaderno de topografía para cada nivel?", "La cota, la referencia usada, quién midió y la fecha", "Solo la cota", "Solo el nombre del dueño", "Un registro útil dice qué, con qué referencia, quién y cuándo."),
        ("=", "{F} Si el NPT subiera 15 cm, ¿cuántos cm sobre el terreno natural quedaría?", "(1020+15)-960", "Se suma el cambio al NPT y se resta la cota del terreno.", " cm"),
        ("abc", "{F} Dos personas obtienen 160 y 140 cm entre NPT y la parte baja. ¿Qué es lo primero que se revisa?", "Que ambas usen las mismas cotas y la misma referencia", "Quién tiene más experiencia", "Cuál resultado es mayor", "Una diferencia entre resultados suele venir de datos o referencias distintas."),
    ],
    ctx=("abc", "En una obra de ejemplo, el cuaderno dice que el terreno está en cota 955 y el plano dice 960. ¿Qué corresponde?", "Registrar la diferencia de 5 cm e informar al supervisor", "Corregir el plano a mano", "Anotar 960 en el cuaderno", "Los datos no se alteran; la diferencia se registra e informa."),
    sc=[
        ("En Construcción: ¿qué es la diferencia de nivel?", "La resta entre la cota mayor y la menor", "Compara dos alturas con la misma referencia."),
        ("Con cotas 1200 y 1150, ¿cuál es la diferencia?", "50 cm", "Se resta la menor de la mayor."),
        ("¿Quién cambia el NPT?", "El proyectista", "El nivel de piso es parte del diseño."),
    ],
    op=("Caso de ejemplo: PR-1 = 2000 cm; terreno natural = 1980 cm; NPT = 2010 cm; fundación 120 cm bajo el terreno. Escribe (a) cuántos cm sobre el terreno queda el NPT, (b) la cota baja de la fundación, (c) la distancia entre NPT y la parte baja, (d) qué haces si el cuaderno anota un terreno de 1985 cm.",
        "(a) 2010 menos 1980 son 30 cm. (b) 1980 menos 120 son 1860 cm. (c) 2010 menos 1860 son 150 cm. (d) Registro la diferencia de 5 cm e informo al supervisor.",
        ["calcula el NPT sobre el terreno", "calcula la cota baja", "calcula la distancia total", "informa la diferencia"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "olvidar la profundidad", "corregir por su cuenta"],
        "Pregunta: «¿qué cota resta a cuál?». Si no responde, pídele que relea cómo se calcula la diferencia de nivel."),
    reinforce="Inventa cuatro cotas y calcula la diferencia de nivel entre cada par consecutivo.",
    extend="Explica por qué todas las cotas de un proyecto deben usar la misma referencia.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 14 (comparación de ejemplo, inventada). Ubicar un cobertizo en el terreno de la «Escuela Rural Mañío». Alternativa 1: queda a 500 cm del deslinde y necesita 12 m de camino de acceso. "
     "Alternativa 2: queda a 200 cm del deslinde y necesita 4 m de camino. El plano de emplazamiento exige un mínimo de 300 cm al deslinde (valor de ejemplo). Costo de ejemplo del camino: $15.000 por metro.")
build(
    O3, 5, F,
    use="Aprenderé a comparar alternativas de ubicación con criterios del plano y a verificar un trazado con una lista de control en papel.",
    prior=["Sé qué es emplazamiento y deslinde.", "Sé calcular costos.", "Sé comparar un dato con un mínimo."],
    explain=[
        "Para comparar alternativas se usan criterios: si cumple lo que exige el plano, cuánto cuesta y qué riesgos trae. Primero se eliminan las alternativas que no cumplen un mínimo exigido, porque un menor costo no compensa un incumplimiento. Después, entre las que cumplen, se comparan costos y otros factores. La decisión final no la toma quien compara, sino el proyectista o el supervisor.",
        "La verificación de calidad de un trazado en papel usa una lista de control: ¿están vigentes los planos?, ¿está verificado el punto de referencia?, ¿coinciden las distancias entre documentos?, ¿están los registros con fecha y responsable?, ¿se informaron las discrepancias? Si falta alguna respuesta, la verificación no está terminada. Todo es lectura y comparación de datos de ejemplo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("criterio", "condición con la que se juzga una alternativa"), ("alternativa", "una de varias opciones posibles"), ("mínimo exigido", "valor menor permitido; el real lo fija la norma vigente"), ("lista de control", "lista de preguntas que se marcan antes de dar algo por verificado")],
    worked=[
        ("Eliminar por mínimo", "Dos alternativas de ejemplo dejan 180 y 260 cm al deslinde y el mínimo de ejemplo es 200 cm. ¿Cuál queda eliminada?", ["Se compara cada distancia con el mínimo.", "180 es menor que 200."], "La que deja 180 cm"),
        ("Comparar costos", "Una alternativa de ejemplo necesita 5 m de camino a $12.000 por metro. ¿Cuánto cuesta?", ["Se multiplican los metros por el precio.", "5 por 12.000 son 60.000."], "$60.000"),
    ],
    mistakes=[("Elegir la alternativa más barata aunque no cumpla el mínimo.", "Incumplir lo exigido invalida la alternativa, sin importar el costo.", "Descarta primero las que no cumplen."),
              ("Dar por verificado un trazado con la lista de control incompleta.", "Las preguntas sin responder son riesgos sin revisar.", "Completa la lista antes de cerrar.")],
    T=[
        ("abc", "En Construcción: ¿qué es un criterio de comparación?", "Una condición con la que se juzga una alternativa", "El nombre de la persona que decide", "El resultado final de la obra", "El criterio es la condición de juicio; no es una persona ni un resultado."),
        ("abc", "{F} ¿Qué alternativa cumple el mínimo al deslinde?", "La alternativa 1", "La alternativa 2", "Ambas", "La 1 deja 500 cm, más que 300; la 2 deja 200, menos que el mínimo."),
        ("abc", "¿Qué se hace primero al comparar alternativas?", "Descartar las que no cumplen un mínimo exigido", "Elegir la más barata", "Elegir la más grande", "Un incumplimiento invalida la alternativa, así que se descarta antes de comparar costos."),
        ("=", "{F} ¿Cuánto cuesta el camino de la alternativa 1?", "12*15000", "Se multiplican los metros por el precio por metro.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta el camino de la alternativa 2?", "4*15000", "Se multiplican los metros por el precio por metro.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta el camino de la alternativa 1 que el de la 2?", "12*15000-4*15000", "Se restan los costos de los dos caminos.", " pesos"),
        ("abc", "{F} La alternativa 2 es más barata. ¿Por qué no se elige?", "Porque no cumple el mínimo de 300 cm al deslinde", "Porque tiene menos camino", "Porque es más corta", "Quedó a 200 cm y el plano exige 300; incumplir invalida la alternativa."),
        ("=", "{F} ¿Cuántos cm sobran sobre el mínimo en la alternativa 1?", "500-300", "Se resta el mínimo a la distancia de la alternativa.", " cm"),
        ("abc", "{F} ¿Quién toma la decisión final de ubicación?", "El proyectista o el supervisor", "Quien hizo la comparación", "El primero que llegue a la obra", "La decisión es de quien tiene la responsabilidad del diseño y la obra."),
        ("ab", "{F} Un estudiante dice: «elijo la 2 porque ahorra $120.000». ¿Qué respuesta es correcta?", "No: la 2 incumple el mínimo del plano", "Sí: el ahorro es lo más importante", "Un menor costo no compensa incumplir una exigencia del plano."),
        ("abc", "¿Cuál es una pregunta de la lista de control de un trazado en papel?", "¿Está verificado el punto de referencia?", "¿Cuántos años tiene el dueño?", "¿Qué color tiene el cobertizo?", "Las preguntas de la lista verifican la calidad del trazado; las otras no tienen relación."),
        ("=", "{F} Si la alternativa 1 necesitara 3 m más de camino, ¿cuánto costaría el camino completo?", "(12+3)*15000", "Se suman los metros y se multiplican por el precio.", " pesos"),
        ("abc", "La lista de control del trazado tiene 5 preguntas y solo 4 están respondidas. ¿Qué corresponde?", "Responder la que falta antes de dar por verificado el trazado", "Darlo por verificado igual", "Marcar la quinta sin revisar", "Una pregunta sin responder deja un riesgo sin revisar."),
    ],
    ctx=("abc", "Un contratista de ejemplo quiere ubicar un cobertizo a 250 cm del deslinde para ahorrar camino, con un mínimo de 300 cm. ¿Qué responde el supervisor?", "No es posible porque incumple el mínimo del plano", "Se acepta si firma un compromiso", "Se acepta porque es solo un cobertizo", "Un mínimo exigido no se negocia con un compromiso; incumplirlo invalida la alternativa."),
    sc=[
        ("En Construcción: ¿qué es una alternativa?", "Una de varias opciones posibles", "Se compara con otras opciones según los criterios."),
        ("¿Qué se descarta primero al comparar?", "Las que no cumplen un mínimo exigido", "Un incumplimiento invalida la alternativa sin importar su costo."),
        ("¿Quién decide la ubicación final?", "El proyectista o el supervisor", "La decisión no corresponde a quien compara las opciones."),
    ],
    op=("Comparación de ejemplo: alternativa A deja 400 cm al deslinde y requiere 8 m de camino; alternativa B deja 150 cm y requiere 3 m. Mínimo de ejemplo 200 cm; camino $10.000 por metro. Escribe (a) qué alternativa cumple el mínimo, (b) el costo del camino de A, (c) por qué no se elige B aunque cueste menos, (d) quién decide.",
        "(a) La A. (b) 8 por $10.000 son $80.000. (c) Porque B queda a 150 cm y el mínimo es 200: incumple. (d) El proyectista o el supervisor.",
        ["compara con el mínimo", "calcula el costo", "explica el descarte", "nombra quién decide"],
        ["hoja con las cuatro respuestas"],
        ["elegir por precio", "olvidar el mínimo", "decidir por su cuenta"],
        "Pregunta: «¿qué se compara primero?». Si no responde, pídele que relea el orden de los criterios."),
    reinforce="Escribe cinco preguntas para una lista de control de trazado.",
    extend="Explica por qué la alternativa más barata no siempre es la mejor.",
)
