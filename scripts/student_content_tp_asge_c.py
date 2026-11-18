"""Asistencia en Geología TP 3.º y 4.º medio: OAE-07 (mapas digitales de terreno) y OAE-08 (información geológica desde puntos remotos). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_asge_common import AVISO, EMER, build

O7 = "TP-ASGE-3y4-OAE-07"
O8 = "TP-ASGE-3y4-OAE-08"

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La oficina de cartografía de la empresa ficticia «Minera Demo» prepara el mapa digital del «Proyecto Mesa Demo», con 5 capas: relieve (curvas de nivel), caminos, zonas de exclusión, puntos de muestreo y unidades de roca. "
     "Peligros anotados: imprimir el mapa sin la capa de zonas de exclusión, usar una versión antigua, escribir mal una coordenada, perder el archivo sin copia, mostrar a personas ajenas los puntos de muestreo (información reservada de la empresa) y trabajar horas seguidas frente a la pantalla con mala postura. "
     "Valores de ejemplo (la norma vigente indica lo que corresponde): una pausa de 10 minutos por cada 60 minutos frente a la pantalla; copia de seguridad diaria de 3 archivos.")
build(
    O7, 1, F,
    use="Aprenderé qué es un mapa digital y una capa, qué peligros tiene un mapa con errores u omisiones, por qué la información de terreno es reservada y qué controles y pausas se usan al trabajar con mapas en computador.",
    prior=["Sé leer un plano con escala y coordenadas.", "Sé distinguir peligro y riesgo.", "Sé la jerarquía de controles."],
    explain=[
        "Un mapa digital es un mapa creado y guardado en un computador. Está formado por capas: cada capa reúne elementos de un mismo tipo, como los caminos o las zonas de exclusión, y se puede mostrar u ocultar. Con un mapa digital se registra y se clasifica información topográfica y geológica del terreno, siguiendo los requerimientos de información que pide el proyecto. Un mapa debe tener su escala, su leyenda y su fecha de versión.",
        "Un error u omisión en un mapa puede ser un riesgo para las personas: si falta la capa de zonas de exclusión, alguien puede dirigirse a un lugar peligroso. Por eso hay controles: la revisión por una segunda persona (administrativo), la edición del archivo oficial solo con clave de acceso (ingeniería) y el uso de la versión vigente. La información de ubicación de muestras y hallazgos es reservada: solo se comparte con personas autorizadas por la empresa. También se cuida a quien trabaja frente a la pantalla, con pausas y buena postura, y se guardan copias de seguridad, es decir, copias aparte para recuperar el trabajo si se pierde.",
        f"Los mapas oficiales los prepara y aprueba personal autorizado; este cuaderno no te habilita para aprobar un mapa que usen otras personas en terreno. {EMER} {AVISO}",
    ],
    vocab=[("mapa digital", "mapa creado y guardado en un computador, formado por capas"), ("capa", "conjunto de elementos del mismo tipo que se puede mostrar u ocultar"), ("versión vigente", "versión actual y aprobada de un documento"), ("información reservada", "información que solo pueden ver personas autorizadas por la empresa"), ("copia de seguridad", "copia de los datos guardada aparte para recuperarlos si se pierden"), ("requerimientos de información", "lo que el proyecto pide que el mapa muestre")],
    worked=[
        ("Peligro y riesgo", "Un mapa de ejemplo se imprime con una versión antigua que no muestra un camino cerrado por un deslizamiento. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la información desactualizada del mapa.", "El riesgo es que un vehículo siga por un camino cerrado y sufra un accidente."], "Peligro: mapa desactualizado; riesgo: que un vehículo tome un camino cerrado y sufra un accidente"),
        ("Clasificar un control", "Se establece que cada mapa lo revise una segunda persona antes de ser aprobado. ¿A qué nivel de la jerarquía corresponde?", ["La revisión es una regla de trabajo.", "No cambia el sistema ni equipa a nadie: es un control administrativo."], "Control administrativo"),
    ],
    mistakes=[("Imprimir un mapa «casi igual» al de la semana pasada sin revisar su versión.", "Pequeñas diferencias pueden ser una zona de exclusión nueva o un camino cerrado.", "Se usa solo la versión vigente, con su fecha, y se verifica antes de imprimir."),
              ("Compartir una captura de pantalla del mapa con los puntos de muestreo en una red social.", "Esa información es reservada de la empresa.", "Solo se comparte por los canales de la empresa y con personas autorizadas.")],
    T=[
        ("abc", "En Geología: ¿qué es un mapa digital?", "Un mapa creado y guardado en un computador, formado por capas", "Un plano dibujado a mano en una libreta de terreno", "Una fotografía tomada desde un vehículo en movimiento", "El mapa digital está en un computador y se organiza en capas; el plano a mano y la fotografía son otra cosa."),
        ("abc", "En Geología: ¿qué es una capa de un mapa digital?", "Un conjunto de elementos del mismo tipo que se puede mostrar u ocultar", "La hoja de papel sobre la que se imprime el mapa", "El color de fondo del mapa", "Una capa agrupa elementos de un mismo tipo, como los caminos."),
        ("abc", "En Geología: ¿qué es la información reservada de un proyecto?", "Información que solo pueden ver personas autorizadas por la empresa", "Información que se publica en el mapa para todos", "Información que ya no sirve y se borra", "La información reservada se comparte solo con personas autorizadas."),
        ("abc", "{F} ¿Cuál es el riesgo de imprimir el mapa sin la capa de zonas de exclusión?", "Que alguien no vea el peligro y se dirija a una zona prohibida", "Que el mapa quede con menos colores", "Que el archivo pese menos", "El riesgo es la posibilidad de daño a una persona; los colores o el peso del archivo no lo son."),
        ("abc", "{F} Pedir que otra persona revise el mapa antes de aprobarlo es un control de tipo:", "Administrativo, porque ordena un paso de revisión", "De ingeniería, porque cambia el terreno", "De EPP, porque protege el cuerpo", "La revisión es una regla de trabajo; no cambia el sistema ni equipa a nadie."),
        ("abc", "{F} Bloquear la edición del archivo oficial con claves de acceso, de modo que solo el personal autorizado pueda cambiarlo, es un control de tipo:", "De ingeniería, porque actúa sobre el sistema y no depende de que alguien lo recuerde", "Administrativo, porque es una regla escrita", "De EPP, porque protege a la persona", "El bloqueo técnico del archivo actúa sobre el sistema, no sobre la conducta."),
        ("=", "{F} En una jornada de 6 horas frente a la pantalla, ¿cuántas pausas de ejemplo corresponden, una por cada 60 minutos?", "(6*60)//60", "Se pasan las horas a minutos y se divide entre los minutos de cada tramo.", " pausas"),
        ("abc", "{F} Una estudiante dice: «ya sé cómo se ordenan las capas, así que puedo aprobar el mapa oficial para que lo use otro equipo en terreno». ¿Qué respuesta es correcta?", "Es falso: aprobar un mapa exige personal autorizado, revisión y norma vigente", "Es cierto, si el mapa se ve ordenado", "Es cierto, si lo imprime a color", "Un mapa oficial exige autorización y revisión; el orden o el color no la reemplazan."),
        ("abc", "Durante una visita de ejemplo, ves en un mapa que falta una zona de exclusión y un equipo está por salir hacia ese sector. ¿Qué corresponde según las reglas generales?", "No acompañar al equipo ni acercarte a la zona, y avisar de inmediato a un adulto responsable", "Acompañar al equipo para advertirles en el camino", "Corregir el mapa tú mismo y dejar que salgan", "No es seguro acercarse a la zona de riesgo; se avisa a quienes pueden detener la salida."),
        ("abc", "En Geología: ¿por qué conviene guardar copias de seguridad de un mapa digital?", "Porque si el archivo se daña o se borra, se pierde el trabajo y la información", "Porque así el archivo se vuelve más liviano", "Porque las copias reemplazan la revisión del mapa", "La copia aparte permite recuperar el trabajo; no hace más liviano el archivo ni reemplaza la revisión."),
        ("abc", "{F} Un compañero comparte en una red social una captura con los puntos de muestreo, «porque se ve bonito». ¿Qué corresponde responder?", "Que no: esa información es reservada y solo se comparte por canales de la empresa con personas autorizadas", "Que sí, si borra el título", "Que sí, si la captura es pequeña", "La ubicación de muestras es reservada, aunque la captura sea pequeña o sin título."),
        ("=", "{F} Con la copia de seguridad diaria de 3 archivos, ¿cuántas copias se guardan durante 5 días?", "3*5", "Se multiplican los archivos copiados cada día por los días.", " copias"),
        ("abc", "{F} Un compañero imprime el mapa de la semana pasada porque «es casi igual». ¿Cuál es la mejor respuesta?", "Que se usa solo la versión vigente, verificando su fecha, antes de imprimir", "Que está bien, si la mayoría de las capas coincide", "Que está bien, si se avisa después que era una versión antigua", "Una diferencia pequeña puede ser una zona de exclusión o un camino cerrado."),
    ],
    ctx=("abc", "Un conocido te pide que le «hagas un mapa» de un terreno minero real con puntos de muestreo, para publicarlo en internet. ¿Qué respondes?", "Que no, porque esa información es reservada y la preparan personas autorizadas, y que lo consultarás con un adulto responsable", "Que sí, si solo muestras algunos puntos", "Que sí, si no pones el nombre del proyecto", "La ubicación de muestras y hallazgos es información reservada de la empresa."),
    sc=[
        ("En Geología: ¿qué es una capa de un mapa digital?", "Un conjunto de elementos del mismo tipo que se puede mostrar u ocultar", "Las capas permiten ordenar la información del mapa."),
        ("En el trabajo con mapas digitales: ¿qué versión se usa para el trabajo en terreno?", "La versión vigente y aprobada", "Una versión antigua puede no mostrar un peligro."),
        ("¿Para qué sirve una copia de seguridad?", "Para recuperar los datos si el archivo se pierde o se daña", "La copia se guarda aparte del archivo original."),
    ],
    op=("Mapa digital de ejemplo del «Proyecto Cuenca Demo», con 4 capas: relieve, caminos, zonas de exclusión y puntos de muestreo. Una persona prepara el mapa durante una jornada de 5 horas frente a la pantalla, con una pausa de ejemplo por cada 60 minutos. Escribe (a) cuántas pausas de ejemplo corresponden, (b) un peligro del mapa y su riesgo, (c) un control administrativo y uno de ingeniería, (d) por qué no se comparte el mapa con personas ajenas, (e) qué haces si ves que un equipo va a salir con un mapa que no muestra una zona de exclusión.",
        "(a) 5 × 60 ÷ 60 = 5 pausas. (b) Peligro: la omisión de la capa de zonas de exclusión; riesgo: que alguien se dirija a una zona prohibida. (c) Administrativo: la revisión por una segunda persona; ingeniería: el bloqueo de edición con claves de acceso. (d) Porque la ubicación de las muestras es información reservada de la empresa. (e) No acercarme a la zona ni acompañar al equipo, y avisar de inmediato a un adulto responsable.",
        ["calcula bien las pausas", "distingue peligro y riesgo", "propone un control administrativo y uno de ingeniería", "explica que la información es reservada", "indica avisar de inmediato"],
        ["hoja con las cinco respuestas"],
        ["llamar riesgo a la omisión misma", "proponer solo EPP", "responder que se acerca a corregir"],
        "Pregunta: «¿quién puede ver y quién puede editar el archivo oficial?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un mapa de cuatro capas y escribe, para cada capa, un peligro que habría si se omitiera.",
    extend="Explica con un ejemplo por qué la revisión por una segunda persona es un control administrativo.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (mapa de ejemplo, inventado). Mapa digital del «Sector Colina Demo» con elementos vectoriales: 12 muestras, 3 caminos y 4 unidades de roca. Cada elemento tiene una tabla de atributos (datos asociados). "
     "El mapa lleva además una imagen ráster de fondo de 400 por 300 píxeles, en que cada píxel representa 5 metros; todo el mapa está georreferenciado. "
     "La ficha de metadatos (datos sobre el archivo) dice: autor R1, fecha de versión de ejemplo 12 de mayo, fuente de los datos, sistema de coordenadas y escala. Roles: geólogo jefe (pide el mapa), técnico de dibujo (lo elabora) y asistente de geología (aporta y revisa datos).")
build(
    O7, 2, F,
    use="Aprenderé los conceptos de dato vectorial, ráster, georreferenciación, tabla de atributos y metadatos, qué elementos debe tener un mapa y qué rol cumple cada persona, para leer un mapa digital en papel.",
    prior=["Sé qué es un mapa digital y una capa.", "Sé calcular distancias con una escala.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "En un mapa digital hay dos grandes tipos de datos. Los vectoriales son elementos dibujados como puntos (por ejemplo, una muestra), líneas (un camino) o polígonos (una unidad de roca), y cada uno tiene una tabla de atributos con sus datos. Los ráster son imágenes formadas por píxeles, cuadritos con un valor o color; la resolución dice cuántos metros reales representa cada píxel. Georreferenciar es asignar coordenadas reales a un mapa o imagen para ubicarlo en el terreno.",
        "Un mapa completo lleva título, norte, escala, leyenda, sistema de coordenadas y fecha de versión. Los metadatos son los datos sobre el archivo: quién lo hizo, cuándo, con qué fuente y en qué sistema de coordenadas; sirven para saber si es la versión vigente y nunca se cambian para «mejorar» un mapa. Para pasar de píxeles a superficie, se multiplican los píxeles por los metros de cada uno, y se recuerda que una hectárea son 10.000 metros cuadrados.",
        f"El geólogo jefe pide la información que necesita; el técnico de dibujo elabora el mapa; el asistente de geología aporta y revisa datos. {EMER} {AVISO}",
    ],
    vocab=[("dato vectorial", "elemento dibujado como punto, línea o polígono, con datos asociados"), ("ráster", "imagen formada por píxeles, cada uno con un valor o color"), ("resolución", "metros reales que representa cada píxel de una imagen"), ("georreferenciar", "asignar coordenadas reales a un mapa o imagen"), ("tabla de atributos", "tabla con los datos asociados a cada elemento del mapa"), ("metadatos", "datos sobre el archivo: autor, fecha, fuente y sistema de coordenadas"), ("hectárea", "unidad de superficie que equivale a 10.000 metros cuadrados")],
    worked=[
        ("Tipo de elemento", "En un mapa de ejemplo, un pozo de agua se representa con un símbolo en un único lugar, y una quebrada con una línea. ¿Qué tipo vectorial es cada uno?", ["Un lugar único es un punto.", "Un recorrido alargado es una línea."], "El pozo es un punto y la quebrada es una línea"),
        ("Superficie de una imagen", "Una imagen ráster de ejemplo mide 200 por 100 píxeles y cada píxel representa 10 metros. ¿Qué superficie cubre en hectáreas?", ["Mide 2.000 por 1.000 metros, es decir, 2.000.000 metros cuadrados.", "Dividido por 10.000 da 200 hectáreas."], "200 hectáreas"),
    ],
    mistakes=[("Creer que la imagen de fondo de un mapa y sus puntos son el mismo tipo de dato.", "La imagen es ráster, formada por píxeles; los puntos son vectoriales, con datos asociados.", "Se distingue cada tipo para saber qué se puede medir o consultar."),
              ("Cambiar la fecha de los metadatos para que el mapa parezca más reciente.", "Se falsea la versión y se puede usar un mapa desactualizado.", "Los metadatos reflejan la realidad y se actualizan solo con una nueva versión.")],
    T=[
        ("abc", "En Geología: ¿qué es un dato vectorial en un mapa digital?", "Un elemento dibujado como punto, línea o polígono, con datos asociados", "Una imagen formada por píxeles", "El papel donde se imprime el mapa", "Los datos vectoriales son puntos, líneas o polígonos; la imagen de píxeles es ráster."),
        ("abc", "En Geología: ¿qué es una imagen ráster?", "Una imagen formada por píxeles, cada uno con un valor o color", "Una línea que une dos puntos del mapa", "Una tabla con datos de cada muestra", "El ráster está hecho de píxeles; la línea es vectorial y la tabla es de atributos."),
        ("abc", "En Geología: ¿qué es georreferenciar un mapa?", "Asignarle coordenadas reales para ubicarlo en el terreno", "Colorear sus capas con símbolos distintos", "Imprimirlo a una escala mayor", "Georreferenciar vincula el mapa con coordenadas reales."),
        ("abc", "{F} ¿Qué tipo de elemento vectorial representa a las 12 muestras?", "Puntos", "Líneas", "Polígonos", "Cada muestra está en un lugar único, así que se dibuja como punto."),
        ("abc", "{F} ¿Qué tipo de elemento vectorial representa a los caminos?", "Líneas", "Puntos", "Polígonos", "Un camino es un recorrido alargado, dibujado como línea."),
        ("abc", "{F} ¿Qué tipo de elemento vectorial representa a las unidades de roca?", "Polígonos", "Líneas", "Puntos", "Una unidad de roca ocupa una superficie, que se dibuja como polígono."),
        ("=", "{F} ¿Cuántos elementos vectoriales hay en total en el mapa?", "12+3+4", "Se suman los puntos, las líneas y los polígonos.", " elementos"),
        ("=", "{F} ¿Cuántos metros de ancho cubre la imagen ráster?", "400*5", "Se multiplican los píxeles de ancho por los metros de cada píxel.", " metros"),
        ("=", "{F} ¿Qué superficie cubre la imagen ráster, en hectáreas?", "(400*5*300*5)//10000", "Se multiplican ancho y alto en metros y se divide entre 10.000.", " hectáreas"),
        ("abc", "{F} ¿Qué parte de la ficha de metadatos permite saber si el mapa es la versión vigente?", "La fecha de versión", "El sistema de coordenadas", "El nombre del geólogo jefe", "La fecha de versión indica si el mapa es el actual."),
        ("abc", "{F} Un mapa se entrega sin escala ni norte. ¿Cuál es el problema?", "No permite medir distancias reales ni orientarse, por lo que es un mapa incompleto", "Ninguno, porque el norte siempre está arriba", "Que el mapa ocupa más espacio en la pantalla", "Sin escala y norte no se pueden medir distancias ni orientar."),
        ("=", "{F} Para la misma superficie, si la resolución mejora a 2 metros por píxel, ¿cuántos píxeles de ancho necesita la imagen?", "(400*5)//2", "Se divide el ancho en metros entre los metros de cada píxel.", " píxeles"),
        ("abc", "{F} Un compañero cambia la fecha de los metadatos para que el mapa parezca más reciente. ¿Qué respuesta es correcta?", "Es falso: los metadatos reflejan la realidad y solo cambian con una nueva versión", "Es cierto, porque la fecha no afecta el mapa", "Es cierto, si el mapa se ve igual", "Cambiar la fecha puede hacer usar un mapa desactualizado."),
    ],
    ctx=("abc", "Una compañera te sugiere borrar los metadatos de un mapa de práctica antes de entregarlo «porque nadie los mira». ¿Qué respondes?", "Que los metadatos no se borran y que lo consultarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, porque ocupan espacio", "Que sí, si el mapa está terminado", "Sin metadatos no se sabe quién hizo el mapa ni si es vigente."),
    sc=[
        ("En Geología: ¿qué son los metadatos de un mapa?", "Datos sobre el archivo, como autor, fecha, fuente y sistema de coordenadas", "Los metadatos dicen de dónde viene el mapa y si está vigente."),
        ("En un mapa digital: ¿qué tipo de dato es una imagen de píxeles?", "Ráster", "El ráster está formado por píxeles."),
        ("¿Qué equivale una hectárea?", "10.000 metros cuadrados", "La hectárea es una unidad de superficie."),
    ],
    op=("Mapa de ejemplo del «Sector Altiplano Demo»: 20 puntos (muestras), 5 líneas (caminos) y 3 polígonos (unidades de roca); imagen ráster de 300 por 200 píxeles, con 10 metros por píxel. Escribe (a) cuántos elementos vectoriales hay, (b) qué superficie cubre la imagen en hectáreas, (c) qué dato de los metadatos permite saber si el mapa es vigente, (d) qué haces si un compañero quiere cambiar ese dato para que parezca más reciente.",
        "(a) 20 + 5 + 3 = 28 elementos. (b) 3.000 × 2.000 = 6.000.000 metros cuadrados; ÷ 10.000 = 600 hectáreas. (c) La fecha de versión. (d) No se cambia: los metadatos reflejan la realidad; se consulta con un adulto responsable.",
        ["suma bien los elementos", "calcula bien la superficie", "nombra la fecha de versión", "no acepta alterar los metadatos"],
        ["hoja con las cuatro respuestas"],
        ["olvidar dividir entre 10.000", "confundir ráster con vectorial", "alterar la fecha"],
        "Pregunta: «¿cuántos metros reales mide cada lado de la imagen?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un mapa con tres tipos de elementos y di si cada uno es punto, línea o polígono.",
    extend="Explica con un ejemplo por qué los metadatos importan para no usar un mapa desactualizado.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (mapa de ejemplo, inventado). Mapa digital del «Sector Meseta Demo», escala 1:2.000 (1 centímetro equivale a 20 metros). Área de estudio: de E 900 a E 1.200 y de N 1.900 a N 2.200. "
     "Zona de exclusión: rectángulo de E 1.040 a E 1.080 y de N 2.040 a N 2.080. Capa de puntos de muestreo: P1 (E 1.000, N 2.000); P2 (E 1.100, N 2.000); P3 (E 1.100, N 2.100); P4 (E 1.000, N 2.100); P5 (E 5.000, N 2.050); P6 (E 1.050, N 2.060). "
     "La ficha de metadatos del mapa dice «fecha de versión: sin dato». El mapa se prepara para que un equipo lo use en terreno.")
build(
    O7, 3, F,
    use="Aprenderé a analizar en papel un mapa digital: detectar valores atípicos, comprobar que los puntos no caen en zonas de exclusión, calcular distancias y superficies con la escala, y decidir qué hacer con los errores sin acomodar los datos.",
    prior=["Sé qué es una capa y qué son los metadatos.", "Sé usar la escala de un plano.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Analizar un mapa digital significa revisar si sus datos son consistentes entre sí. El área de estudio es la región que cubre el proyecto: fuera de ella no debería haber datos del mapa. Un valor atípico es un dato que queda muy lejos del resto y que puede ser un error de digitación, como un dígito de más o de menos. Una verificación de consistencia comprueba que los datos no se contradicen: por ejemplo, que ningún punto de muestreo quede dentro de una zona de exclusión.",
        "Con la escala se pasan medidas del mapa a medidas reales y al revés, y con las coordenadas se calculan superficies. Cuando se encuentra un error no se acomoda el dato para que pase la revisión: se revisa la libreta de terreno, se informa y se corrige con firma. Un mapa sin fecha de versión no se usa en terreno hasta saber de qué versión se trata, porque podría ser desactualizado.",
        f"Esta revisión la hace personal autorizado antes de aprobar un mapa. Aquí practicas el razonamiento. {EMER} {AVISO}",
    ],
    vocab=[("área de estudio", "región que cubre el proyecto y fuera de la cual no debe haber datos"), ("valor atípico", "dato que queda muy lejos del resto y puede ser un error"), ("error de digitación", "falla al escribir un dato, como un dígito cambiado"), ("verificación de consistencia", "comprobación de que los datos no se contradicen entre sí"), ("versión vigente", "versión actual y aprobada de un documento")],
    worked=[
        ("Valor atípico", "En un mapa de ejemplo, cuatro puntos están entre E 300 y E 400 y un quinto está en E 3.500. ¿Qué observación corresponde?", ["Cuatro puntos están agrupados y uno está muy lejos.", "E 3.500 es un valor atípico, posible error de digitación de E 350."], "E 3.500 es un valor atípico que debe revisarse"),
        ("Punto dentro de una zona", "Una zona de exclusión de ejemplo va de E 200 a E 260 y de N 500 a N 560. Un punto está en E 230 y N 520. ¿Qué corresponde?", ["230 está entre 200 y 260, y 520 está entre 500 y 560.", "El punto cae dentro de la zona: se informa y se revisa."], "El punto está dentro de la zona y debe revisarse e informarse"),
    ],
    mistakes=[("Mover un punto fuera de la zona de exclusión para que el mapa «pase la revisión».", "El punto quedaría mal ubicado y se oculta un problema real.", "Se revisa la libreta, se informa y se corrige con firma si hay un error."),
              ("Usar un mapa sin fecha de versión porque «se ve completo».", "Podría ser una versión antigua sin un peligro nuevo.", "No se usa hasta identificar su versión.")],
    T=[
        ("abc", "En Geología: ¿qué es un valor atípico en una capa de puntos de un mapa?", "Un dato que queda muy lejos del resto y que puede ser un error de digitación", "El punto más cercano al camino", "El primer punto digitado en el mapa", "El valor atípico se aleja del conjunto, no es ni el primero ni el más cercano al camino."),
        ("abc", "En Geología: ¿qué es el área de estudio de un mapa?", "La región que cubre el proyecto, fuera de la cual no debe haber datos", "El espacio de la hoja que queda en blanco", "La parte del mapa donde está la leyenda", "El área de estudio delimita la región del proyecto."),
        ("abc", "En Geología: ¿qué es una verificación de consistencia?", "Comprobar que los datos del mapa no se contradicen entre sí", "Imprimir el mapa en varios tamaños", "Contar cuántas capas tiene el archivo", "La verificación de consistencia busca contradicciones."),
        ("abc", "{F} ¿Qué punto de la capa de muestreo es un valor atípico?", "P5, porque está en E 5.000, muy fuera del área de estudio", "P1, porque es el primero", "P3, porque está al Norte de P2", "P5 queda muy lejos del área de estudio, que llega hasta E 1.200."),
        ("abc", "{F} ¿Qué punto cae dentro de la zona de exclusión?", "P6, porque E 1.050 y N 2.060 están dentro del rectángulo", "P4, porque N 2.100 es mayor que 2.080", "P2, porque E 1.100 es mayor que 1.080", "P6 cumple ambos rangos: E entre 1.040 y 1.080, y N entre 2.040 y 2.080."),
        ("=", "{F} ¿Cuántos centímetros ocupa en el mapa el ancho del área de estudio, de 300 metros?", "(300*100)//2000", "Se pasan los metros a centímetros y se divide entre la escala.", " centímetros"),
        ("=", "{F} ¿Cuántos centímetros separan en el mapa a los puntos P1 y P2, que están a 100 metros?", "(100*100)//2000", "Se pasan los metros a centímetros y se divide entre la escala.", " centímetros"),
        ("=", "{F} ¿Cuántas hectáreas tiene el área de estudio, de 300 por 300 metros?", "(300*300)//10000", "Se multiplica ancho por alto en metros y se divide entre 10.000.", " hectáreas"),
        ("abc", "{F} ¿Cuál es la causa probable del valor de E 5.000 en P5?", "Un error de digitación, que se confirma con la libreta de terreno", "Que P5 es un punto correcto que nadie había movido", "Un error de dibujo que se arregla moviendo P5 sobre el mapa", "Un valor atípico se verifica en la fuente original; no se mueve a ojo ni se da por bueno."),
        ("abc", "{F} ¿Qué corresponde hacer con P6, que cae dentro de la zona de exclusión?", "No moverlo para que calce: revisar la libreta, informar y decidir con personal autorizado", "Moverlo fuera de la zona para que el mapa pase la revisión", "Borrarlo del mapa sin avisar", "Mover o borrar el punto oculta un problema; se revisa y se informa."),
        ("abc", "{F} La ficha dice «fecha de versión: sin dato». ¿Qué corresponde?", "No usar el mapa en terreno hasta identificar su versión", "Usarlo, porque se ve completo", "Escribir la fecha de hoy para completar el dato", "Sin fecha de versión no se sabe si está vigente, y poner una fecha inventada falsea el registro."),
        ("abc", "{F} ¿Qué orden de revisión del mapa es el adecuado?", "Revisar el área de estudio, buscar valores atípicos, comprobar las zonas de exclusión, revisar la versión, informar y corregir con firma", "Corregir primero los puntos a ojo y revisar después qué cambió", "Revisar solo el primer punto, porque los otros son iguales", "La revisión recorre todos los controles y termina informando y corrigiendo con evidencia."),
        ("abc", "{F} Un compañero borra P5 y P6 para que el mapa «pase la revisión». ¿Qué respuesta es correcta?", "Es falso: borrar los puntos oculta los errores en vez de corregirlos", "Es cierto, porque así el mapa queda sin errores", "Es cierto, si después se vuelven a agregar", "Los puntos erróneos se investigan y se corrigen con evidencia, no se borran para esconder el problema."),
    ],
    ctx=("abc", "Una compañera te sugiere mover un punto de un mapa de práctica fuera de la zona de exclusión «para que no se note el error». ¿Qué respondes?", "Que no se mueven puntos para esconder errores y que lo consultarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, si el movimiento es pequeño", "Que sí, y se corrige después de la revisión", "Mover un punto para esconder un error pone en riesgo a quien use el mapa."),
    sc=[
        ("En Geología: ¿qué es un valor atípico?", "Un dato que queda muy lejos del resto y puede ser un error", "El valor atípico se revisa en la fuente original."),
        ("En la revisión de un mapa: ¿qué se verifica sobre las zonas de exclusión?", "Que ningún punto de muestreo quede dentro de ellas", "Un punto dentro de una zona de exclusión debe revisarse."),
        ("¿Qué se hace con un mapa sin fecha de versión?", "No se usa en terreno hasta identificar su versión", "Sin versión no se sabe si está vigente."),
    ],
    op=("Mapa de ejemplo del «Sector Cresta Demo», escala 1:5.000 (1 centímetro equivale a 50 metros). Área de estudio: de E 2.000 a E 2.500 y de N 3.000 a N 3.400. Zona de exclusión: de E 2.200 a E 2.260 y de N 3.100 a N 3.160. Puntos: Q1 (E 2.100, N 3.050), Q2 (E 2.230, N 3.130), Q3 (E 9.000, N 3.200). Escribe (a) qué punto cae dentro de la zona de exclusión, (b) qué punto es un valor atípico, (c) cuántos centímetros ocupa en el mapa el ancho del área de estudio, (d) qué haces con los puntos con problema.",
        "(a) Q2, porque E 2.230 está entre 2.200 y 2.260 y N 3.130 está entre 3.100 y 3.160. (b) Q3, porque E 9.000 queda muy fuera del área de estudio. (c) 500 metros ÷ 50 = 10 centímetros. (d) No los muevo ni los borro: reviso la libreta de terreno, informo y se corrigen con firma por personal autorizado.",
        ["detecta el punto dentro de la zona", "detecta el valor atípico", "calcula bien la escala", "no esconde ni mueve los puntos con problema"],
        ["hoja con las cuatro respuestas"],
        ["comparar solo una coordenada", "mover el punto para que calce", "dividir mal la escala"],
        "Pregunta: «¿entre qué dos valores de E y de N está la zona?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres puntos y una zona de exclusión en coordenadas, y di cuál punto cae dentro.",
    extend="Explica con un ejemplo por qué un error se corrige con evidencia y no a ojo.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (pedido de ejemplo, inventado). El geólogo jefe del «Proyecto Cresta Demo» pide un mapa de un área de 4.000 metros hacia el Este por 3.000 metros hacia el Norte, a escala 1:5.000, con las capas de puntos de muestreo, caminos, zonas de exclusión y curvas de nivel cada 10 metros; "
     "el desnivel del área va de la cota 2.000 a la 2.120. La imagen de fondo tiene un píxel cada 5 metros. Hay que digitar 24 puntos de muestreo, a 3 minutos por punto, y cada punto lo revisa una segunda persona en 1 minuto (datos de ejemplo). "
     "El área de estudio va de E 5.000 a E 9.000 y de N 1.000 a N 4.000. Las hojas de impresión de ejemplo miden 100 por 70 centímetros.")
build(
    O7, 4, F,
    use="Aprenderé a planificar en papel un mapa digital con datos de ejemplo: calcular el tamaño en papel, las curvas de nivel, los píxeles de la imagen y los tiempos de digitación y revisión, y a comprobar que los datos caen dentro del área de estudio.",
    prior=["Sé usar la escala de un mapa.", "Sé qué son las curvas de nivel y la equidistancia.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Para planificar un mapa se parte del pedido de información: qué área cubre, a qué escala y con qué capas. Con la escala se calcula el tamaño en papel: se pasan los metros a centímetros y se divide entre el denominador de la escala. La cantidad de curvas de nivel se obtiene dividiendo el desnivel entre la equidistancia y sumando 1 para incluir ambas curvas de los extremos. La cantidad de píxeles de una imagen se calcula dividiendo cada lado, en metros, entre los metros por píxel.",
        "Digitar es escribir o marcar los datos en el mapa a partir de los registros de terreno. El tiempo de trabajo se calcula multiplicando la cantidad de puntos por el tiempo de cada uno, y la revisión por una segunda persona agrega su propio tiempo: es un control que detecta errores de digitación, aunque cueste minutos. Cada punto se comprueba contra el área de estudio. Los tiempos y las medidas de este cuaderno son de ejemplo.",
        f"Los tiempos y el formato reales los fija el equipo de cartografía. Aquí aprendes el razonamiento. {EMER} {AVISO}",
    ],
    vocab=[("pedido de información", "documento que dice qué debe mostrar el mapa"), ("digitar", "escribir o marcar datos en un mapa digital a partir de registros"), ("equidistancia", "diferencia de cota entre curvas de nivel consecutivas"), ("píxel", "cuadrito mínimo de una imagen ráster"), ("revisión por una segunda persona", "control en que otra persona comprueba lo digitado antes de aprobarlo")],
    worked=[
        ("Tamaño en papel", "Un área de ejemplo de 2.000 metros de ancho se dibuja a escala 1:10.000. ¿Cuántos centímetros ocupa de ancho?", ["Se pasan 2.000 metros a 200.000 centímetros.", "200.000 dividido por 10.000 da 20 centímetros."], "20 centímetros"),
        ("Curvas de nivel", "Un desnivel de ejemplo de 60 metros se dibuja con curvas cada 20 metros. ¿Cuántas curvas hay, incluyendo ambas de los extremos?", ["60 dividido por 20 da 3.", "Se suma 1 por la curva inicial: 4 curvas."], "4 curvas"),
    ],
    mistakes=[("Olvidar sumar 1 al contar las curvas entre dos cotas.", "Con 3 intervalos hay 4 curvas, porque se cuentan ambos extremos.", "Se divide el desnivel entre la equidistancia y se suma 1."),
              ("Omitir la revisión por segunda persona para ahorrar tiempo.", "La revisión detecta errores que pueden ubicar mal un punto.", "Se incluye el tiempo de revisión en el plan.")],
    T=[
        ("abc", "En Geología: ¿qué es un pedido de información de un mapa?", "El documento que dice qué debe mostrar el mapa, con qué escala y con qué capas", "La lista de los materiales de un campamento", "El informe con los resultados del laboratorio", "El pedido define el contenido del mapa; los otros documentos son de otra tarea."),
        ("abc", "En Geología: ¿qué significa digitar un punto en un mapa digital?", "Escribir o marcar sus coordenadas en el mapa a partir de un registro", "Imprimir el punto en la hoja", "Calcular su distancia al camino con una regla", "Digitar es ingresar el dato al mapa digital."),
        ("abc", "En Geología: ¿para qué sirve la revisión por una segunda persona?", "Para detectar errores de digitación antes de aprobar el mapa", "Para repartir el trabajo entre más personas", "Para reemplazar la revisión de la versión vigente", "La segunda revisión busca errores; no es un reparto de tareas."),
        ("=", "{F} ¿Cuántos centímetros de ancho ocupa el área en el mapa a escala 1:5.000?", "(4000*100)//5000", "Se pasan los metros a centímetros y se divide entre la escala.", " centímetros"),
        ("=", "{F} ¿Cuántos centímetros de alto ocupa el área en el mapa?", "(3000*100)//5000", "Se pasan los metros a centímetros y se divide entre la escala.", " centímetros"),
        ("=", "{F} ¿Cuántas curvas de nivel hay entre las cotas 2.000 y 2.120, incluyendo ambas?", "(2120-2000)//10+1", "Se divide el desnivel entre la equidistancia y se suma 1.", " curvas"),
        ("=", "{F} ¿Cuántos píxeles en total tiene la imagen de fondo del área?", "(4000//5)*(3000//5)", "Se calculan los píxeles de ancho y de alto y se multiplican.", " píxeles"),
        ("=", "{F} ¿Cuántos minutos toma digitar los 24 puntos?", "24*3", "Se multiplica la cantidad de puntos por los minutos de cada uno.", " minutos"),
        ("=", "{F} ¿Cuántos minutos toma en total digitar y revisar los 24 puntos?", "24*3+24*1", "Se suman los tiempos de digitación y de revisión.", " minutos"),
        ("abc", "{F} Un punto de muestreo tiene E 6.200 y N 4.500. ¿Qué corresponde concluir?", "Está fuera del área de estudio porque N supera 4.000, y debe revisarse", "Está dentro del área de estudio porque E está entre 5.000 y 9.000", "Está dentro, porque ninguna coordenada es cero", "Ambas coordenadas deben estar dentro del rango; N 4.500 supera el máximo de 4.000."),
        ("=", "{F} Si el pedido cambia la equidistancia a 20 metros, ¿cuántas curvas de nivel hay entre las cotas 2.000 y 2.120, incluyendo ambas?", "(2120-2000)//20+1", "Se divide el desnivel entre la nueva equidistancia y se suma 1.", " curvas"),
        ("abc", "{F} ¿Cabe el mapa completo en una hoja de impresión de 100 por 70 centímetros?", "Sí, porque 80 por 60 centímetros no superan 100 por 70", "No, porque 80 es mayor que 70", "No, porque la escala 1:5.000 no se puede imprimir", "El mapa mide 80 por 60 centímetros, y ambos lados caben en la hoja."),
        ("abc", "{F} Un compañero propone omitir la revisión por una segunda persona para ahorrar 24 minutos. ¿Cuál es la mejor respuesta?", "Que no: la revisión detecta errores de digitación que podrían ubicar mal un punto, aunque cueste tiempo", "Que sí, porque 24 minutos son demasiado", "Que sí, si el primero digitó con cuidado", "La revisión es un control de calidad; el cuidado no reemplaza una segunda mirada."),
    ],
    ctx=("abc", "Un conocido te pide que le calcules cuánto tiempo tomará digitar un mapa de su faena real «para ofrecérselo a otra empresa» con los datos de clase. ¿Qué respondes?", "Que los números del cuaderno son de ejemplo, que los tiempos reales los fija el equipo de cartografía y que lo consultarás con un adulto responsable", "Que sí, porque los cálculos están bien", "Que sí, si cobras por hora", "Los valores son de ejemplo y la información de una faena real es reservada."),
    sc=[
        ("En Geología: ¿cómo se cuentan las curvas de nivel entre dos cotas?", "Se divide el desnivel entre la equidistancia y se suma 1", "Se suma 1 para incluir ambas curvas de los extremos."),
        ("En la planificación de un mapa: ¿qué se calcula con la escala?", "El tamaño que ocupa el área en el papel", "La escala relaciona medidas del mapa con medidas reales."),
        ("¿Para qué sirve la revisión por una segunda persona?", "Para detectar errores de digitación", "La segunda mirada encuentra errores que el digitador no ve."),
    ],
    op=("Pedido de ejemplo del «Proyecto Estero Demo»: área de 3.000 metros hacia el Este por 2.000 hacia el Norte, a escala 1:5.000; desnivel de la cota 500 a la 580 con curvas cada 20 metros; 18 puntos a digitar, a 2 minutos por punto, y 1 minuto de revisión por punto; hojas de impresión de 70 por 50 centímetros. Escribe (a) las medidas del mapa en centímetros, (b) si cabe en la hoja, (c) cuántas curvas de nivel hay incluyendo los extremos, (d) cuántos minutos toma digitar y revisar los puntos.",
        "(a) 60 por 40 centímetros. (b) Sí, porque 60 no supera 70 y 40 no supera 50. (c) 80 ÷ 20 + 1 = 5 curvas. (d) 18 × 2 + 18 × 1 = 54 minutos. Los valores reales los fija el equipo de cartografía.",
        ["calcula bien las medidas del mapa", "compara con la hoja", "cuenta bien las curvas", "suma digitación y revisión"],
        ["hoja con las cuatro respuestas"],
        ["olvidar sumar 1 a las curvas", "omitir el tiempo de revisión", "pasar mal los metros a centímetros"],
        "Pregunta: «¿cuántos centímetros son 3.000 metros en la escala dada?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula los centímetros que ocupa un lado de 2.500 metros a escala 1:5.000.",
    extend="Explica con un ejemplo por qué conviene incluir el tiempo de revisión en el plan de un mapa.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Proyecto Cordón Demo» de la empresa ficticia «Minera Demo» tiene un punto remoto de trabajo, sin señal de telefonía celular. Plan de comunicaciones de ejemplo: radio como medio principal, teléfono satelital como medio alternativo, "
     "un reporte cada 2 horas durante una jornada de 8 horas, y una persona responsable del plan en el campamento base. El receptor de posicionamiento tiene una batería para 10 horas y el trabajo dura 5 jornadas sin recarga. "
     "Peligros anotados: depender de un único medio de comunicación, batería agotada, coordenadas mal transmitidas, señal débil cerca de paredes altas, un reporte que no llega y nadie reacciona, y filtración de información reservada.")
build(
    O8, 1, F,
    use="Aprenderé qué es un sistema de posicionamiento global, qué es el plan de comunicaciones de un punto remoto, qué peligros tiene la falta de comunicación o un error de coordenadas y qué controles ordenan la jerarquía de prevención.",
    prior=["Sé qué son las coordenadas Este y Norte.", "Sé distinguir peligro y riesgo.", "Sé la jerarquía de controles."],
    explain=[
        "Un sistema de posicionamiento global es un conjunto de satélites cuyas señales permiten a un receptor calcular su posición. Un punto remoto es un lugar alejado, con poca o ninguna cobertura de telefonía. Las tecnologías de información y comunicación, como radios, teléfonos satelitales y computadores, sirven para leer, transmitir y registrar la información geológica desde allí, siguiendo los requerimientos de información del proyecto.",
        "En un punto remoto, un problema de comunicación puede volverse grave. El plan de comunicaciones es el documento que fija los medios, las horas de reporte y lo que se hace si un reporte no llega. Los controles siguen la jerarquía: un segundo medio de comunicación independiente (ingeniería), horas fijas de reporte y lectura de vuelta de las coordenadas (administrativo) y baterías de repuesto. La lectura de vuelta consiste en repetir lo recibido para que quien lo envió confirme que es correcto. Las coordenadas de hallazgos son información reservada: solo se transmiten por canales de la empresa.",
        f"Estas tareas las hace personal autorizado, con instrucción y norma vigente de la autoridad minera. {EMER} {AVISO}",
    ],
    vocab=[("sistema de posicionamiento global", "conjunto de satélites que permite a un receptor calcular su posición"), ("punto remoto", "lugar alejado, con poca o ninguna cobertura de telefonía"), ("plan de comunicaciones", "documento que fija medios, horas de reporte y qué hacer si un reporte no llega"), ("medio alternativo", "segundo medio de comunicación que se usa si el principal falla"), ("lectura de vuelta", "repetir lo recibido para que quien lo envió confirme que es correcto"), ("reporte", "mensaje periódico con la posición y el estado de una persona o equipo")],
    worked=[
        ("Peligro y riesgo", "Un equipo de ejemplo recibe por radio las coordenadas de un hallazgo y las anota sin repetirlas a quien las envió. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es anotar coordenadas sin confirmarlas.", "El riesgo es que un dígito mal entendido ubique el hallazgo, o a una persona, en un lugar equivocado."], "Peligro: coordenadas sin confirmar; riesgo: ubicar un hallazgo o a una persona en un lugar equivocado"),
        ("Clasificar un control", "Se escribe una regla que obliga a probar la comunicación y a anotar el resultado antes de salir a un punto remoto de ejemplo. ¿A qué nivel de la jerarquía corresponde?", ["Una regla escrita ordena la conducta.", "No cambia el sistema ni equipa a nadie: es un control administrativo."], "Control administrativo"),
    ],
    mistakes=[("Creer que si el receptor muestra una posición, esa posición es exacta.", "La señal puede ser débil o tener error, por ejemplo cerca de paredes altas.", "Se anota la precisión y se repite la lectura en mejores condiciones, informando la duda."),
              ("Creer que quien leyó este cuaderno puede trabajar solo en un punto remoto.", "Trabajar en puntos remotos exige personal autorizado, plan de comunicaciones y norma vigente.", "Aprende aquí el concepto y deja el trabajo remoto a personal autorizado.")],
    T=[
        ("abc", "En Geología: ¿qué es un sistema de posicionamiento global?", "Un conjunto de satélites cuyas señales permiten a un receptor calcular su posición", "Una red de caminos que une los campamentos", "Un mapa digital con las zonas de exclusión", "Es un sistema de satélites que da posición; los caminos y los mapas son otra cosa."),
        ("abc", "En Geología: ¿qué es un plan de comunicaciones?", "Un documento que fija medios, horas de reporte y qué hacer si un reporte no llega", "Una lista de las muestras que se envían al laboratorio", "El horario de las comidas del campamento", "El plan de comunicaciones organiza cómo se mantiene el contacto."),
        ("abc", "En Geología: ¿qué es un medio alternativo de comunicación?", "Un segundo medio que se usa si el principal falla", "Un medio que se usa solo para entretenimiento", "El mismo medio principal con otro nombre", "El medio alternativo es un respaldo independiente del principal."),
        ("abc", "{F} ¿Cuál es el riesgo de depender de un único medio de comunicación en el punto remoto?", "Quedar incomunicado si falla y no poder pedir ayuda", "Gastar más batería en la jornada", "Tener que repetir el reporte más veces", "El riesgo es la posibilidad de daño: sin comunicación no se puede pedir ayuda."),
        ("abc", "{F} Las horas fijas de reporte y la lectura de vuelta de coordenadas son controles de tipo:", "Administrativo, porque ordenan cómo y cuándo se comunica", "De ingeniería, porque cambian el terreno", "De EPP, porque protegen a la persona", "Son reglas de trabajo; no cambian el sistema ni equipan a nadie."),
        ("abc", "{F} Un segundo medio de comunicación independiente, como un teléfono satelital, es un control de tipo:", "De ingeniería, porque agrega un respaldo físico al sistema", "Administrativo, porque es una regla escrita", "De EPP, porque protege a quien lo lleva", "Un respaldo físico independiente actúa sobre el sistema y no depende de que alguien lo recuerde."),
        ("=", "{F} Con un reporte cada 2 horas, sin contar el de salida, ¿cuántos reportes se esperan en una jornada de 8 horas?", "8//2", "Se divide la duración de la jornada entre las horas entre reportes.", " reportes"),
        ("abc", "{F} Una estudiante dice: «ya sé leer coordenadas, así que puedo ir sola a un punto remoto a obtener datos». ¿Qué respuesta es correcta?", "Es falso: trabajar en un punto remoto exige personal autorizado, plan de comunicaciones y norma vigente", "Es cierto, si lleva el receptor cargado", "Es cierto, si avisa por mensaje a una amiga", "Un cuaderno no habilita para trabajar en un punto remoto; la batería o un aviso informal tampoco."),
        ("abc", "{F} Una persona de ejemplo no envía su reporte a la hora fijada. ¿Qué corresponde según el plan?", "Avisar a la persona responsable del plan, que activa a personal autorizado y a emergencias; no salir a buscarla por cuenta propia", "Esperar al día siguiente por si se comunica", "Ir de inmediato a su punto de trabajo sin avisar", "Un reporte ausente activa el plan; ir sola a un lugar remoto añade otra persona en riesgo."),
        ("abc", "En Geología: ¿por qué conviene hacer una lectura de vuelta de las coordenadas transmitidas por radio?", "Porque un dígito mal escuchado puede ubicar mal el punto", "Porque así el mensaje se transmite más rápido", "Porque la radio solo acepta números repetidos", "La lectura de vuelta detecta errores de escucha o de dictado."),
        ("abc", "{F} El receptor muestra baja precisión porque está junto a una pared alta. ¿Qué corresponde?", "Anotar la baja precisión y repetir la lectura en mejores condiciones, informando la duda", "Anotar la posición como exacta, porque el receptor la mostró", "No anotar nada, porque la lectura no sirve", "La precisión se registra junto con la posición; ocultarla engaña a quien usa el dato."),
        ("=", "{F} Si cada batería dura 10 horas y el trabajo requiere 8 horas por jornada durante 5 jornadas sin recarga, ¿cuántas baterías hacen falta, subiendo al entero?", "(8*5+9)//10", "Se calculan las horas totales y se divide entre la autonomía de cada batería subiendo al entero.", " baterías"),
        ("abc", "{F} Un compañero pide enviar las coordenadas de un hallazgo por una aplicación de mensajería personal, «porque es más rápido». ¿Cuál es la mejor respuesta?", "Que no: esas coordenadas son información reservada y se transmiten solo por los canales de la empresa", "Que sí, si el mensaje se borra después", "Que sí, si solo se envía una coordenada", "La información reservada solo se transmite por canales autorizados, aunque se borre después."),
    ],
    ctx=("abc", "Un conocido te ofrece que lo acompañes a un lugar remoto «porque ya sabes usar un receptor de posición», sin avisar a nadie. ¿Qué respondes?", "Que no, porque ir a un lugar remoto sin plan de comunicaciones es peligroso, y que lo consultarás con un adulto responsable", "Que sí, si llevas el receptor cargado", "Que sí, si vuelven antes de que oscurezca", "Sin plan de comunicaciones nadie sabría pedir ayuda si hay un problema."),
    sc=[
        ("En Geología: ¿qué es un punto remoto?", "Un lugar alejado, con poca o ninguna cobertura de telefonía", "En un punto remoto la comunicación necesita un plan."),
        ("En la comunicación de terreno: ¿qué es la lectura de vuelta?", "Repetir lo recibido para que quien lo envió confirme que es correcto", "La lectura de vuelta evita errores de dictado."),
        ("¿Qué se hace si un reporte no llega a la hora fijada?", "Se avisa a la persona responsable del plan, sin salir a buscar por cuenta propia", "El plan define quién actúa si un reporte falta."),
    ],
    op=("Plan de ejemplo del «Proyecto Pampa Demo»: radio como medio principal, teléfono satelital como medio alternativo, reporte cada 3 horas durante una jornada de 9 horas, batería del receptor de 12 horas y 4 jornadas sin recarga. Escribe (a) cuántos reportes se esperan en una jornada, (b) cuántas baterías hacen falta, subiendo al entero, (c) un control administrativo y uno de ingeniería, (d) qué debe hacer una persona si un reporte no llega.",
        "(a) 9 ÷ 3 = 3 reportes. (b) 9 × 4 = 36 horas; 36 ÷ 12 = 3 baterías. (c) Administrativo: horas fijas de reporte y lectura de vuelta; ingeniería: un segundo medio de comunicación independiente. (d) Avisar a la persona responsable del plan, que activa a personal autorizado y a emergencias; no salir a buscar por cuenta propia.",
        ["calcula bien los reportes", "calcula bien las baterías", "propone un control administrativo y uno de ingeniería", "indica avisar al responsable del plan"],
        ["hoja con las cuatro respuestas"],
        ["olvidar las jornadas al calcular las baterías", "proponer salir a buscar a la persona", "proponer solo EPP"],
        "Pregunta: «¿qué pasa si el único medio de comunicación falla?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres controles de comunicación para un punto remoto y clasifica cada uno como administrativo o de ingeniería.",
    extend="Explica con un ejemplo por qué la lectura de vuelta reduce el riesgo de ubicar mal un punto.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (datos de ejemplo, inventados). Registro de un receptor de posicionamiento del «Proyecto Cordón Demo». Waypoints (puntos guardados con nombre): W-01 en E 6.000, N 4.000, cota 2.100; W-02 en E 6.300, N 4.400, cota 2.150. "
     "El receptor recorrió de W-01 a W-02 en 10 minutos y guardó el track (la serie de posiciones del recorrido). Precisión de ejemplo del receptor: más o menos 5 metros. Los dos receptores del proyecto deben usar el mismo datum (modelo de referencia con que se calculan las coordenadas). "
     "Formato de mensaje de ejemplo: punto; E; N; cota; hora; responsable, por ejemplo «P-014; E 6.200; N 4.300; cota 2.050; 14:30; R2». Documentos: planilla de campo (datos medidos) y bitácora de comunicaciones (mensajes enviados y recibidos).")
build(
    O8, 2, F,
    use="Aprenderé los conceptos de waypoint, track, datum y precisión, el formato de un mensaje de posición y los documentos de registro, para leer y registrar en papel la información que viene de un punto remoto.",
    prior=["Sé qué es un plan de comunicaciones.", "Sé calcular distancias con coordenadas.", "Sé restar y dividir números enteros."],
    explain=[
        "Un receptor de posicionamiento guarda información de dos tipos. Un waypoint es un punto guardado con un nombre y sus coordenadas; un track es la serie de posiciones que el receptor registra mientras se desplaza. La precisión es el desvío máximo esperado entre la posición medida y la real. El datum es el modelo de referencia con que se calculan las coordenadas: si dos receptores usan datum distintos, la misma posición puede mostrar coordenadas desplazadas, así que se comprueba que coincidan antes de comparar datos.",
        "Un mensaje de posición sigue un formato fijo para que no falte nada: punto, coordenadas Este y Norte, cota, hora y responsable. No se redondean ni se recortan los dígitos para ahorrar caracteres, porque se pierde precisión. Los datos se registran en la planilla de campo, y los mensajes enviados y recibidos, en la bitácora de comunicaciones, con hora y responsable. Para calcular la distancia horizontal entre dos puntos se usan las diferencias de coordenadas, como en el teorema de Pitágoras.",
        f"El responsable de recepción en la base anota el mensaje; el asistente de geología ayuda a ordenar y revisar los datos; el geólogo jefe decide qué se necesita. {EMER} {AVISO}",
    ],
    vocab=[("waypoint", "punto guardado en el receptor con un nombre y sus coordenadas"), ("track", "serie de posiciones que el receptor guarda mientras se desplaza"), ("datum", "modelo de referencia con que se calculan las coordenadas"), ("precisión", "desvío máximo esperado entre la posición medida y la real"), ("formato de mensaje", "orden fijo de los datos que se transmiten"), ("bitácora de comunicaciones", "registro de los mensajes enviados y recibidos")],
    worked=[
        ("Diferencia de coordenadas", "Dos waypoints de ejemplo están en E 1.200 y E 1.450. ¿Cuántos metros hay entre ellos en la dirección Este?", ["Se resta la coordenada menor a la mayor.", "1.450 menos 1.200 son 250 metros."], "250 metros"),
        ("Velocidad media", "Un recorrido de ejemplo de 600 metros se hizo en 20 minutos. ¿Cuántos metros por minuto avanzó en promedio?", ["Se divide la distancia entre el tiempo.", "600 dividido por 20 da 30 metros por minuto."], "30 metros por minuto"),
    ],
    mistakes=[("Redondear una coordenada de 6.200 a 6.000 para acortar el mensaje.", "Se pierden 200 metros de precisión y el punto queda mal ubicado.", "Se transmiten todos los dígitos del formato."),
              ("Comparar posiciones de dos receptores sin revisar su datum.", "Con datum distintos, el mismo punto puede mostrar coordenadas desplazadas.", "Se comprueba que ambos usen el mismo datum antes de comparar.")],
    T=[
        ("abc", "En Geología: ¿qué es un waypoint?", "Un punto guardado en el receptor con un nombre y sus coordenadas", "Una línea que une todas las posiciones de un recorrido", "El modelo de referencia con que se calculan las coordenadas", "El waypoint es un punto guardado; la línea del recorrido es el track y el modelo es el datum."),
        ("abc", "En Geología: ¿qué es un track de un receptor de posicionamiento?", "La serie de posiciones que el receptor guarda mientras se desplaza", "Un punto con nombre en el mapa", "La batería del receptor", "El track es el registro del recorrido; el punto con nombre es el waypoint."),
        ("abc", "En Geología: ¿qué es el datum de un sistema de coordenadas?", "El modelo de referencia con que se calculan las coordenadas", "La hora a la que se toma cada lectura", "La unidad de medida de la cota", "El datum fija el modelo de referencia; no es una hora ni una unidad."),
        ("abc", "{F} ¿Qué dato del mensaje de ejemplo indica la altura del punto sobre el nivel de referencia?", "La cota", "La hora", "El responsable", "La cota es la altura; la hora y el responsable son otros datos del mensaje."),
        ("abc", "{F} ¿Qué documento guarda los mensajes enviados y recibidos, con hora y responsable?", "La bitácora de comunicaciones", "La planilla de campo", "El mapa digital", "La bitácora registra mensajes; la planilla guarda los datos medidos."),
        ("=", "{F} ¿Cuántos metros al Este está W-02 respecto de W-01?", "6300-6000", "Se resta la coordenada Este de W-01 a la de W-02.", " metros"),
        ("=", "{F} ¿Cuántos metros al Norte está W-02 respecto de W-01?", "4400-4000", "Se resta la coordenada Norte de W-01 a la de W-02.", " metros"),
        ("abc", "{F} ¿Qué distancia horizontal hay entre W-01 y W-02?", "500 metros", "700 metros", "100 metros", "Con 300 al Este y 400 al Norte, la distancia es 500; 700 sumaría las diferencias y 100 las restaría."),
        ("=", "{F} Si el recorrido de W-01 a W-02 se hizo en línea recta y en 10 minutos, ¿cuántos metros por minuto avanzó?", "500//10", "Se divide la distancia de 500 metros entre los minutos del recorrido.", " metros por minuto"),
        ("abc", "{F} Dos receptores muestran coordenadas que difieren en 80 metros para el mismo punto, y uno usa otro datum. ¿Qué conviene hacer?", "Verificar que ambos usen el mismo datum antes de comparar los datos", "Promediar las dos posiciones y anotarlas como exactas", "Elegir la del receptor más nuevo sin revisar nada", "Un datum distinto puede desplazar coordenadas; se unifica antes de comparar."),
        ("abc", "{F} Llega el mensaje «P-014; E 6.200; N 4.30; cota 2.050; 14:30; R2». ¿Qué corresponde hacer?", "Notar que falta un dígito en N, pedir la repetición y no completarlo de memoria", "Completar N con un cero para que quede de cuatro dígitos", "Anotarlo tal cual y no avisar", "Un dato incompleto se confirma con quien lo envió, no se supone."),
        ("abc", "{F} Dos lecturas del mismo punto difieren en 3 metros al Este y 2 al Norte, y la precisión del receptor es de más o menos 5 metros. ¿Qué conclusión corresponde?", "Es una diferencia compatible con la precisión; se anotan la lectura y su precisión", "Una de las dos está mal y se descarta al azar", "Es un error grave que invalida todo el recorrido", "Una diferencia menor que la precisión es esperable; no es un error."),
        ("abc", "{F} Un compañero propone redondear las coordenadas de 6.200 a 6.000 para ahorrar caracteres en el mensaje. ¿Qué respuesta es correcta?", "Es falso: se perderían 200 metros de precisión; el formato exige todos los dígitos", "Es cierto, porque la diferencia es pequeña", "Es cierto, si se avisa después", "Redondear a la centena puede mover un punto cientos de metros."),
    ],
    ctx=("abc", "Un compañero te propone anotar en la bitácora de comunicaciones los mensajes «de memoria» al final del día, para no interrumpir el trabajo. ¿Qué respondes?", "Que los mensajes se anotan en el momento, con hora y responsable, y que lo consultarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, si se acuerdan bien", "Que sí, y se corrige si falta algo", "Un registro hecho de memoria puede fallar y no deja evidencia confiable."),
    sc=[
        ("En Geología: ¿qué es un waypoint?", "Un punto guardado en el receptor con un nombre y sus coordenadas", "El waypoint guarda un lugar con su nombre."),
        ("En el uso de receptores: ¿qué es el datum?", "El modelo de referencia con que se calculan las coordenadas", "Con datum distintos las coordenadas pueden diferir."),
        ("¿Qué se hace si un mensaje llega con un dato incompleto?", "Se pide la repetición y no se completa de memoria", "Un dato incompleto se confirma con quien lo envió."),
    ],
    op=("Ficha de ejemplo del «Proyecto Cresta Demo»: waypoint X-01 en E 3.000, N 5.000, cota 1.800; waypoint X-02 en E 3.600, N 5.800, cota 1.850; recorrido en línea recta de X-01 a X-02 en 25 minutos; precisión del receptor de ejemplo de 5 metros. Escribe (a) cuántos metros al Este y cuántos al Norte está X-02 de X-01, (b) la distancia horizontal entre ambos (diferencias de 600 y 800 metros), (c) cuántos metros por minuto se avanzó, (d) qué haces si llega un mensaje con una coordenada Norte de solo tres dígitos.",
        "(a) 600 metros al Este y 800 al Norte. (b) 1.000 metros, porque 600 y 800 forman un triángulo de lados 3, 4 y 5 multiplicados por 200. (c) 1.000 ÷ 25 = 40 metros por minuto. (d) Pido la repetición a quien envió el mensaje y no completo el dato de memoria. Todo se registra en la bitácora con hora y responsable.",
        ["calcula bien las diferencias", "obtiene la distancia horizontal", "calcula la velocidad media", "pide repetir el dato incompleto"],
        ["hoja con las cuatro respuestas"],
        ["sumar las diferencias en vez de calcular la distancia", "completar el dato de memoria", "olvidar la unidad"],
        "Pregunta: «¿qué dos diferencias de coordenadas necesitas para la distancia horizontal?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa dos waypoints con coordenadas y calcula cuántos metros al Este y al Norte está uno del otro.",
    extend="Explica con un ejemplo por qué dos receptores con distinto datum pueden mostrar coordenadas distintas para el mismo lugar.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (bitácora de ejemplo, inventada). «Proyecto Cordón Demo». Área de estudio: de E 6.000 a E 7.000 y de N 4.000 a N 5.000; las cotas del área van de 2.000 a 2.200 metros. Los reportes se esperan cada hora, de las 10:00 a las 16:00. "
     "Mensajes recibidos en la base: M1, 10:00, E 6.150, N 4.200, cota 2.040; M2, 11:00, E 6.250, N 4.200, cota 2.045; M3, 12:00, E 6.250, N 4.300, cota 2.052; M4, 14:00, E 6.050, N 4.300, cota 2.020; "
     "M5, 15:00, E 8.350, N 4.350, cota 2.060; M6, 16:00, E 6.350, N 4.350, cota 20.500. El reporte de las 13:00 no está en la bitácora.")
build(
    O8, 3, F,
    use="Aprenderé a analizar en papel una bitácora de mensajes de posición: detectar datos fuera de rango, reportes faltantes y lecturas dudosas, calcular distancias de un recorrido y actuar sin suponer ni acomodar los datos.",
    prior=["Sé el formato de un mensaje de posición.", "Sé qué es un área de estudio y un valor atípico.", "Sé sumar y restar números enteros."],
    explain=[
        "Analizar una bitácora de mensajes significa revisar cada mensaje con los mismos controles. Un dato fuera de rango es el que queda fuera del área de estudio o de los valores posibles, como una cota mayor que las del área. Un reporte faltante es el que debía llegar a una hora fijada y no está. Una lectura dudosa se confirma con la lectura de vuelta: se pide al emisor repetir el dato y se compara con lo recibido.",
        "Cuando falta un reporte no se supone que todo está bien ni se rellena con una posición estimada: se registra el hecho, se pregunta al responsable y se aplica el plan de comunicaciones si no hay respuesta. Un error probable de digitación, como un dígito cambiado, no se corrige en la bitácora hasta confirmarlo con el emisor, y la corrección se hace con firma y sin borrar. La distancia de un recorrido se obtiene sumando los tramos entre posiciones consecutivas.",
        f"Estos análisis los hace el responsable de recepción con el asistente de geología, bajo el plan de comunicaciones. {EMER} {AVISO}",
    ],
    vocab=[("dato fuera de rango", "dato que queda fuera del área de estudio o de los valores posibles"), ("reporte faltante", "reporte que debía llegar a una hora fijada y no está registrado"), ("lectura dudosa", "dato que parece un error y se confirma con el emisor"), ("tramo", "recorrido entre dos posiciones consecutivas"), ("registro consecutivo", "registro ordenado por hora, sin saltos")],
    worked=[
        ("Dato fuera de rango", "Una bitácora de ejemplo con área de estudio de E 100 a E 400 recibe un mensaje con E 750. ¿Qué observación corresponde?", ["750 es mayor que 400, el máximo del área.", "Es un dato fuera de rango y debe confirmarse con el emisor."], "Dato fuera de rango, por confirmar con el emisor"),
        ("Reportes esperados", "Con reportes cada 2 horas de las 8:00 a las 14:00, ¿cuántos reportes se esperan, incluyendo ambos extremos?", ["De 8 a 14 hay 6 horas, que son 3 intervalos de 2 horas.", "Se suma 1 por el reporte inicial: 4 reportes."], "4 reportes"),
    ],
    mistakes=[("Rellenar un reporte faltante con una posición estimada para que la bitácora quede completa.", "Una posición supuesta puede ser falsa y hace creer que todo está bien.", "Se registra que falta, se pregunta al responsable y se aplica el plan si no hay respuesta."),
              ("Corregir en la bitácora un dato dudoso sin consultar al emisor.", "La corrección podría estar equivocada y se pierde el registro original.", "Se confirma con una lectura de vuelta y se corrige con firma, sin borrar.")],
    T=[
        ("abc", "En Geología: ¿qué es un dato fuera de rango en una bitácora de posición?", "Un dato que queda fuera del área de estudio o de los valores posibles", "Un dato que llegó a la hora esperada", "Un dato escrito con letra clara", "Un dato fuera de rango no calza con el área ni con los valores posibles."),
        ("abc", "En Geología: ¿qué es un reporte faltante?", "Un reporte que debía llegar a una hora fijada y no está registrado", "Un reporte que se envió dos veces", "Un reporte con más de seis datos", "El reporte faltante es el que no llegó cuando debía."),
        ("abc", "En Geología: ¿qué es una lectura dudosa?", "Un dato que parece un error y se confirma con el emisor", "Un dato que no se necesita guardar", "Un dato que ya fue corregido con firma", "Una lectura dudosa se confirma antes de usarla."),
        ("abc", "{F} ¿Qué mensaje tiene una coordenada Este fuera del área de estudio?", "M5, con E 8.350", "M1, con E 6.150", "M4, con E 6.050", "El área llega hasta E 7.000; solo E 8.350 queda fuera."),
        ("abc", "{F} ¿Qué mensaje tiene una cota imposible para el área?", "M6, con cota 20.500", "M3, con cota 2.052", "M4, con cota 2.020", "Las cotas del área van de 2.000 a 2.200; 20.500 queda muy fuera."),
        ("abc", "{F} ¿Qué reporte falta en la bitácora?", "El de las 13:00", "El de las 12:00", "El de las 16:00", "Los mensajes saltan de las 12:00 a las 14:00."),
        ("=", "{F} Con un reporte cada hora de las 10:00 a las 16:00, incluyendo ambos extremos, ¿cuántos reportes se esperan?", "(16-10)+1", "Se restan las horas y se suma 1 por el reporte inicial.", " reportes"),
        ("=", "{F} ¿Cuántos reportes faltan, si se recibieron 6?", "7-6", "Se restan los reportes recibidos a los esperados.", " reporte"),
        ("=", "{F} ¿Cuántos metros recorrió la persona entre M1 y M3, sumando los dos tramos?", "(6250-6150)+(4300-4200)", "Se suman la diferencia Este de M1 a M2 y la diferencia Norte de M2 a M3.", " metros"),
        ("abc", "{F} ¿Cuál es la explicación probable de E 8.350 en M5?", "Un error de digitación, que se confirma con una lectura de vuelta", "Que el punto es correcto porque nadie lo cuestionó", "Un cambio de datum que ya se resolvió", "Un valor atípico se confirma con el emisor; no se supone que sea correcto."),
        ("abc", "{F} ¿Qué corresponde hacer con la cota 20.500 de M6?", "No corregirla en la bitácora hasta confirmarla con el emisor, y luego corregir con firma", "Cambiarla a 2.050 de inmediato, porque parece un dígito de más", "Borrar el mensaje M6 de la bitácora", "Un dígito de más es probable, pero se confirma antes de corregir."),
        ("abc", "{F} Falta el reporte de las 13:00. ¿Qué corresponde?", "Registrar que falta, preguntar al responsable y aplicar el plan de comunicaciones si no hay respuesta", "Rellenar el reporte con una posición estimada", "Suponer que todo estaba bien y seguir", "Un reporte faltante activa el plan; suponer o rellenar oculta un posible problema."),
        ("abc", "{F} Un compañero rellena el reporte de las 13:00 con un promedio de las posiciones de M3 y M4, «para que quede completo». ¿Qué respuesta es correcta?", "Es falso: una posición estimada no es un dato real y puede ocultar un problema", "Es cierto, porque el promedio es muy parecido a lo que ocurrió", "Es cierto, si se anota con otra letra", "Un dato inventado en la bitácora engaña a quien la use."),
    ],
    ctx=("abc", "Una compañera te propone «arreglar» la bitácora de práctica cambiando los datos fuera de rango para que todos calcen antes de una visita. ¿Qué respondes?", "Que no se alteran los datos y que lo consultarás con un adulto responsable, como tu profesor o profesora de especialidad", "Que sí, solo los más llamativos", "Que sí, y se corrige después de la visita", "Alterar los datos oculta errores reales; ante la duda se consulta a un adulto responsable."),
    sc=[
        ("En Geología: ¿qué es un dato fuera de rango?", "Un dato que queda fuera del área de estudio o de los valores posibles", "Un dato fuera de rango se revisa con el emisor."),
        ("En la bitácora de un punto remoto: ¿qué se hace si falta un reporte?", "Se registra, se pregunta al responsable y se aplica el plan si no hay respuesta", "Un reporte faltante activa el plan de comunicaciones."),
        ("En una bitácora de posición geológica: ¿cómo se corrige un dato dudoso?", "Se confirma con el emisor y se corrige con firma, sin borrar", "La corrección se hace con evidencia y con firma."),
    ],
    op=("Bitácora de ejemplo del «Proyecto Estero Demo». Área de estudio: de E 1.000 a E 1.500 y de N 2.000 a N 2.400; cotas de 800 a 900. Reportes cada hora de las 9:00 a las 12:00. Mensajes: 9:00, E 1.100, N 2.100, cota 850; 10:00, E 1.200, N 2.100, cota 855; 12:00, E 1.200, N 5.200, cota 860. Escribe (a) cuántos reportes se esperan, (b) cuál falta, (c) qué dato está fuera de rango, (d) cuántos metros se recorrieron entre los dos primeros mensajes, (e) qué haces con el dato fuera de rango y con el reporte faltante.",
        "(a) De 9 a 12 con reporte cada hora: 12 − 9 + 1 = 4 reportes. (b) Falta el de las 11:00. (c) N 5.200, porque el área llega solo hasta N 2.400. (d) 100 metros hacia el Este. (e) El dato fuera de rango se confirma con el emisor con lectura de vuelta y se corrige con firma, sin borrar; del reporte faltante se informa al responsable y, si no hay respuesta, se aplica el plan de comunicaciones. No se rellena ni se supone.",
        ["calcula bien los reportes esperados", "detecta el faltante", "detecta el dato fuera de rango", "calcula bien el tramo", "no acomoda ni supone datos"],
        ["hoja con las cinco respuestas"],
        ["olvidar sumar 1 a los reportes", "corregir el dato sin confirmar", "rellenar el reporte faltante"],
        "Pregunta: «¿qué mensajes deberían existir y cuáles hay?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una bitácora de cuatro mensajes con una hora faltante y un dato fuera de rango, y escribe qué errores tiene.",
    extend="Explica con un ejemplo por qué una posición estimada no debe rellenar un reporte faltante.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados). «Proyecto Cordón Demo». El receptor tiene batería para 12 horas; la jornada es de 9 horas y el trabajo dura 3 días sin recarga. "
     "Cada mensaje de posición tiene 40 caracteres y el medio de comunicación transmite 10 caracteres por segundo. Se envían 6 mensajes por día. Precisión requerida de ejemplo: más o menos 10 metros; el receptor informa más o menos 4 metros. "
     "Al final de cada día se guarda un respaldo de la planilla de campo en un medio aparte del receptor.")
build(
    O8, 4, F,
    use="Aprenderé a calcular en papel horas de batería, tiempos de transmisión, cantidad de datos y márgenes de precisión de un trabajo remoto, y a decidir con un criterio, un respaldo y datos reales.",
    prior=["Sé el formato de un mensaje de posición.", "Sé multiplicar y dividir números enteros.", "Sé redondear hacia arriba cuando no se puede usar una fracción."],
    explain=[
        "Para planificar un trabajo remoto se calcula cuánta energía y cuánto tiempo de comunicación hacen falta. Las horas totales se obtienen multiplicando la jornada por los días; las baterías, dividiendo las horas totales entre la autonomía de cada una y subiendo al entero. El tiempo de un mensaje se calcula dividiendo sus caracteres entre la velocidad de transmisión, que es cuántos caracteres se envían por segundo.",
        "Un criterio de precisión dice cuánto desvío se acepta: si la precisión del receptor es menor o igual que la requerida, cumple, y la diferencia es el margen. Un respaldo es una copia de los datos guardada aparte del equipo original, porque si el equipo se pierde o se daña no se pierden los datos. Si un día los mensajes o las horas reales cambian, se recalcula con el dato real y se informa al responsable.",
        f"Estos cálculos los revisa el responsable del plan. Aquí aprendes el razonamiento con números de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("velocidad de transmisión", "cantidad de caracteres que se envían por segundo"), ("margen", "diferencia entre lo exigido y lo que se tiene"), ("respaldo", "copia de los datos guardada aparte del equipo original"), ("criterio de precisión", "valor máximo de desvío que se acepta en una posición"), ("recalcular", "volver a calcular con un dato real cuando algo cambia")],
    worked=[
        ("Horas y baterías", "Un equipo de ejemplo trabaja 7 horas al día durante 4 días, con baterías de 14 horas. ¿Cuántas baterías necesita?", ["Horas totales: 7 × 4 = 28.", "28 dividido por 14 da 2 baterías exactas."], "2 baterías"),
        ("Tiempo de transmisión", "Un mensaje de ejemplo de 50 caracteres se transmite a 5 caracteres por segundo. ¿Cuántos segundos demora?", ["Se divide la cantidad de caracteres entre la velocidad.", "50 dividido por 5 son 10 segundos."], "10 segundos"),
    ],
    mistakes=[("Guardar el respaldo en el mismo equipo que contiene los datos originales.", "Si el equipo se pierde o se daña, se pierden ambos.", "El respaldo se guarda aparte del equipo original."),
              ("Mantener el cálculo inicial cuando un día se envían más mensajes de lo previsto.", "Los tiempos y la batería cambian con el uso real.", "Se recalcula con el dato real y se informa.")],
    T=[
        ("abc", "En Geología: ¿qué es la precisión de un receptor de posicionamiento?", "El desvío máximo esperado entre la posición medida y la real", "La cantidad de horas que dura su batería", "El número de mensajes que puede enviar por día", "La precisión se refiere al desvío de la posición, no a la batería ni a los mensajes."),
        ("abc", "En Geología: ¿qué es un respaldo de la planilla de campo?", "Una copia de los datos guardada aparte del equipo original", "La planilla original, pero escrita con otra letra", "Un cuaderno donde se anotan los reportes del día", "El respaldo es una copia aparte para recuperar los datos si el equipo se pierde."),
        ("abc", "En Geología: ¿qué es la velocidad de transmisión de un medio de comunicación?", "La cantidad de caracteres que se envían por segundo", "El tiempo que dura la batería del receptor", "La distancia máxima que cubre la señal", "La velocidad de transmisión mide caracteres por segundo."),
        ("=", "{F} ¿Cuántas horas de funcionamiento necesita el receptor durante todo el trabajo?", "9*3", "Se multiplican las horas de cada jornada por los días.", " horas"),
        ("=", "{F} ¿Cuántas baterías de 12 horas hacen falta, subiendo al entero?", "(9*3+11)//12", "Se suman 11 antes de dividir entre 12 para subir al siguiente entero.", " baterías"),
        ("=", "{F} ¿Cuántos segundos demora la transmisión de un mensaje de posición?", "40//10", "Se divide la cantidad de caracteres entre los que se envían por segundo.", " segundos"),
        ("=", "{F} ¿Cuántos mensajes de posición se envían en todo el trabajo?", "6*3", "Se multiplican los mensajes por día por los días.", " mensajes"),
        ("=", "{F} ¿Cuántos segundos de transmisión se usan en total en todo el trabajo?", "(6*3*40)//10", "Se calculan los caracteres totales y se dividen entre los que se envían por segundo.", " segundos"),
        ("=", "{F} ¿Cuántos metros de margen tiene el receptor respecto de la precisión requerida?", "10-4", "Se resta la precisión del receptor a la precisión requerida.", " metros"),
        ("abc", "{F} Un día se envían 9 mensajes en lugar de 6. ¿Qué corresponde?", "Recalcular el tiempo de transmisión con el dato real e informar al responsable", "Mantener el cálculo inicial para no modificar el plan", "Anotar 6 mensajes para que coincida con lo previsto", "Los cálculos se actualizan con datos reales; anotar lo previsto falsea el registro."),
        ("abc", "{F} El respaldo se guarda en el mismo receptor que tiene la planilla de campo. ¿Cuál es el problema?", "Si el equipo se pierde o se daña, se pierden la planilla y su respaldo", "Ninguno, porque ocupa menos espacio", "Que el respaldo se vuelve más lento", "Un respaldo útil se guarda aparte del equipo original."),
        ("=", "{F} ¿Cuántos caracteres se envían en total en todo el trabajo, con los mensajes de la ficha?", "6*3*40", "Se multiplican los mensajes totales por los caracteres de cada uno.", " caracteres"),
        ("abc", "{F} Un compañero omite el respaldo del segundo día porque «ya está en la planilla». ¿Qué respuesta es correcta?", "Es falso: el respaldo protege los datos si el equipo falla, y debe hacerse cada día", "Es cierto, porque la planilla es suficiente", "Es cierto, si el día fue corto", "La planilla y el respaldo cumplen funciones distintas; sin respaldo, un fallo del equipo pierde el día."),
    ],
    ctx=("abc", "Un conocido te pide que calcules las baterías y el tiempo de transmisión de un trabajo remoto real, «con los números de la clase». ¿Qué respondes?", "Que los números del cuaderno son de ejemplo, que los valores reales los fija el plan del proyecto y que lo consultarás con un adulto responsable", "Que sí, porque el método está bien", "Que sí, si agregas una batería más por si acaso", "Los valores son de ejemplo; los reales dependen del equipo, del plan y de la norma vigente."),
    sc=[
        ("En Geología: ¿cómo se calcula el tiempo de transmisión de un mensaje?", "Se divide sus caracteres entre la velocidad de transmisión", "La velocidad se mide en caracteres por segundo."),
        ("En el trabajo remoto: ¿dónde se guarda el respaldo de los datos?", "Aparte del equipo original", "Así los datos sobreviven si el equipo falla."),
        ("¿Cuándo se cumple un criterio de precisión?", "Cuando la precisión del receptor es menor o igual que la requerida", "Un desvío menor significa que la medida es más precisa."),
    ],
    op=("Ficha de ejemplo: «Proyecto Humedal Demo». Batería del receptor para 10 horas; jornada de 8 horas durante 5 días sin recarga; mensajes de 30 caracteres a 5 caracteres por segundo; 4 mensajes por día; precisión requerida de más o menos 8 metros y precisión del receptor de más o menos 3 metros. Escribe (a) las horas totales y cuántas baterías hacen falta, (b) cuántos segundos demora un mensaje, (c) el margen de precisión, (d) dónde guardarías el respaldo y por qué.",
        "(a) 8 × 5 = 40 horas; 40 ÷ 10 = 4 baterías. (b) 30 ÷ 5 = 6 segundos. (c) 8 − 3 = 5 metros de margen, así que cumple. (d) Aparte del receptor, porque si el equipo se pierde o se daña no se pierden los datos. Los valores reales los fija el plan del proyecto.",
        ["calcula bien horas y baterías", "calcula bien el tiempo del mensaje", "calcula el margen de precisión", "guarda el respaldo aparte y lo explica"],
        ["hoja con las cuatro respuestas"],
        ["olvidar los días al calcular las baterías", "dividir al revés el tiempo de transmisión", "guardar el respaldo en el mismo equipo"],
        "Pregunta: «¿qué pasa con los datos si el receptor se pierde y no hay respaldo?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Calcula las baterías de un trabajo inventado de 6 horas al día durante 5 días, con baterías de 10 horas.",
    extend="Explica con un ejemplo por qué un respaldo guardado en el mismo equipo no protege los datos.",
)
