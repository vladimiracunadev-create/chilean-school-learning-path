"""Construcción TP, mención Obras Viales e Infraestructura, 4.º medio: OAM-01 (interpretar planos, especificaciones y ensayos) y OAM-02 (verificar partidas viales). Solo conceptos, lectura de documentos y planillas con datos de ejemplo."""
from __future__ import annotations

from tp_coov_common import AVISO, EMER, build

O1 = "TP-COOV-4-OAM-01"
O2 = "TP-COOV-4-OAM-02"

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). Proyecto «Camino Los Aromos» (ficticio): mejoramiento de un camino rural de 6 km. Documentos: planos de planta (3 láminas), perfil longitudinal (2 láminas), "
     "secciones transversales (4 láminas), especificaciones técnicas (12 páginas), informes de ensayo de laboratorio (5 informes) y libro de obra. "
     "Riesgos anotados: atropello por máquinas y camiones, vuelco de equipos, polvo en suspensión y caída de taludes.")
build(
    O1, 1, F,
    use="Aprenderé qué documentos forman un proyecto vial, qué es un estándar de calidad y qué riesgos y controles hay que reconocer antes de interpretar planos, especificaciones y ensayos.",
    prior=["Sé leer una tabla y un dibujo simple.", "Sé sumar, restar y multiplicar.", "Sé que un trabajo se encarga por escrito."],
    explain=[
        "Una obra vial es la construcción o mejora de caminos, calles y sus obras anexas, como las cunetas. Antes de trabajar existe un proyecto con documentos: los planos (planta, perfil longitudinal y secciones transversales), las especificaciones técnicas, que dicen por escrito cómo deben ser los materiales y los trabajos, y los informes de ensayo de laboratorio, que muestran si un material cumple lo exigido. Interpretar significa leer cada documento y entender qué exige. Un estándar de calidad es el nivel mínimo que debe cumplir un material o una faena.",
        "Las obras viales se rigen por la norma vigente y por el manual de carreteras del mandante, que es la institución que contrata la obra. El ITO (inspector técnico de obra) revisa que se cumpla el contrato. Los riesgos principales son el atropello, el vuelco de máquinas, el polvo y la caída de taludes. La jerarquía de controles ordena las medidas de seguridad: primero eliminar el peligro, segundo sustituirlo, tercero aislarlo con barreras y señales, cuarto organizar el trabajo y, al final, entregar elementos de protección personal (EPP).",
        f"{EMER} {AVISO}",
    ],
    vocab=[("obra vial", "construcción o mejora de caminos y calles con sus obras anexas"), ("estándar de calidad", "nivel mínimo que debe cumplir un material o una faena"), ("ITO", "inspector técnico de obra, que revisa que se cumpla el contrato"), ("mandante", "institución que contrata la obra"), ("jerarquía de controles", "orden de las medidas de seguridad, de la más a la menos efectiva"), ("EPP", "elemento de protección personal, último nivel de la jerarquía"), ("informe de ensayo", "documento del laboratorio con los resultados medidos en un material")],
    worked=[
        ("Elegir el documento", "Una jefa de calidad de ejemplo quiere saber si el material de una base cumple lo exigido. ¿Qué documento consulta?", ["Los resultados medidos en un material los entrega el laboratorio.", "Ese documento es el informe de ensayo."], "El informe de ensayo de laboratorio"),
        ("Clasificar un control", "En una obra de ejemplo se instala un cerco que separa a los peatones de la zona de camiones. ¿Qué nivel de la jerarquía es?", ["El cerco no elimina al camión, pero lo separa de las personas.", "Separar con barreras es aislar el peligro."], "Aislar el peligro (tercer nivel)"),
    ],
    mistakes=[("Usar un material porque el proveedor dice que es bueno, sin informe de ensayo.", "La calidad se demuestra con resultados medidos, no con la palabra de quien vende.", "Pide el informe de ensayo y consulta al ITO o al jefe de calidad."),
              ("Creer que leer un proyecto habilita a operar una máquina o intervenir la vía.", "Esas tareas exigen personal autorizado y norma vigente.", "Aprende los conceptos aquí y practica solo con instructor autorizado.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es una especificación técnica de un proyecto?", "Un documento escrito que dice cómo deben ser los materiales y los trabajos", "Un dibujo que muestra el camino visto desde arriba", "Un informe del laboratorio con resultados medidos", "La especificación describe por escrito materiales y trabajos; el dibujo es la planta y los resultados medidos están en el informe de ensayo."),
        ("abc", "En una obra vial de ejemplo, ¿para qué sirve un informe de ensayo de laboratorio?", "Para mostrar si un material cumple lo que se exige", "Para mostrar el recorrido del camino visto de lado, con sus alturas", "Para explicar por escrito cómo debe ejecutarse un trabajo", "El informe entrega resultados medidos; el recorrido con alturas es el perfil y las instrucciones están en las especificaciones."),
        ("abc", "Una constructora de ejemplo dice que el ITO «revisa que se cumpla el contrato». ¿Quién es el ITO?", "El inspector técnico de obra", "El proyectista que diseñó el camino", "El laboratorista que ensaya los materiales", "ITO significa inspector técnico de obra; el diseño y el ensayo corresponden a otros roles."),
        ("=", "{F} ¿Cuántas láminas de planos tiene el proyecto, sumando planta, perfil longitudinal y secciones transversales?", "3+2+4", "Se suman las láminas de los tres tipos de plano.", " láminas"),
        ("abc", "{F} ¿Cuál de estos riesgos aparece anotado en la ficha?", "Atropello por máquinas y camiones", "Intoxicación en un espacio confinado", "Descarga eléctrica en un tablero", "La ficha nombra el atropello; las otras opciones son riesgos que no están anotados."),
        ("abc", "{F} Una supervisora propone instalar una barrera que separe a los peatones de la zona de camiones. ¿A qué nivel de la jerarquía de controles corresponde?", "Aislar el peligro con una barrera", "Eliminar el peligro", "Entregar elementos de protección personal", "La barrera separa a las personas del peligro pero no lo elimina ni es un EPP."),
        ("=", "{F} El camino mide 6 km y se revisará por tramos de 500 m. ¿Cuántos tramos hay?", "6000//500", "Se pasan los 6 km a metros (6.000) y se divide por 500.", " tramos"),
        ("abc", "{F} Llega material a la obra para usarlo hoy, pero no existe informe de ensayo. ¿Qué corresponde?", "Informar al ITO o al jefe de calidad y no usarlo hasta tener el resultado", "Usarlo si el proveedor asegura que cumple", "Usarlo hoy y pedir el informe al terminar la obra", "Sin resultado medido no se sabe si cumple; se informa y se espera, no se confía en la palabra del proveedor."),
        ("ab", "{F} Una compañera dice: «leí las 12 páginas de especificaciones, así que ya puedo operar una máquina». ¿Qué respuesta es correcta?", "No: leer documentos no habilita; operar una máquina exige autorización y capacitación", "Sí: conocer las especificaciones la habilita para operar", "Conocer un documento y estar autorizada para operar una máquina son cosas distintas."),
        ("abc", "En una obra de ejemplo, un camión atropella a un trabajador. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarse de inmediato a mover a la persona", "Anotar lo ocurrido y avisar solo al terminar el turno", "Acercarse sin control puede causar otro accidente; se avisa de inmediato a un adulto responsable y a emergencias."),
        ("=", "{F} Cada informe de ensayo cuesta $45.000 (valor de ejemplo). Se piden los 5 informes de la ficha y 2 informes adicionales. ¿Cuánto cuestan en total?", "(5+2)*45000", "Se suman los informes pedidos y se multiplican por el valor de cada uno.", " pesos"),
        ("abc", "{F} Las secciones transversales muestran un talud distinto del que indican las especificaciones. ¿Qué conclusión es la más prudente?", "Hay una diferencia entre documentos: se informa al proyectista o al ITO antes de ejecutar", "Se sigue el plano porque es un dibujo", "Se sigue el texto porque está escrito", "Ningún documento manda por sí solo: la diferencia se informa a quien decide."),
        ("abc", "{F} Para el riesgo de polvo en suspensión, ¿qué orden de medidas respeta la jerarquía de controles?", "Reducir la fuente del polvo, luego organizar el trabajo y al final usar mascarilla", "Usar mascarilla, luego organizar el trabajo y al final reducir la fuente del polvo", "Organizar el trabajo, luego usar mascarilla y al final reducir la fuente del polvo", "La jerarquía parte por actuar sobre la fuente, sigue con la organización del trabajo y deja el EPP al final."),
    ],
    ctx=("abc", "Un conocido ofrece dinero a un estudiante para que «ayude a guiar camiones» en una obra vial porque «solo hay que hacer señas». ¿Qué responde?", "Agradece, explica que no está autorizado y sugiere que lo haga personal designado por la obra", "Acepta si le pagan más que a un trabajador contratado", "Acepta porque ya estudió los documentos de un proyecto vial", "Guiar camiones exige personal designado y capacitado; cobrar más o haber leído documentos no reemplaza eso."),
    sc=[
        ("En Obras Viales: ¿qué es un estándar de calidad?", "El nivel mínimo que debe cumplir un material o una faena", "El estándar fija el mínimo exigido y el informe de ensayo muestra si se alcanza."),
        ("¿Qué documento muestra si un material cumple lo exigido?", "El informe de ensayo de laboratorio", "Los resultados medidos se entregan en el informe, no en el plano."),
        ("¿Qué se hace ante un atropello o atrapamiento en la obra?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarse sin control puede aumentar el daño y las víctimas."),
    ],
    op=("Proyecto de ejemplo «Calle Los Pinos» (ficticio): planos (4 láminas), especificaciones (8 páginas) y 3 informes de ensayo. El plano de secciones muestra una cuneta, pero las especificaciones no la mencionan. Un camión descarga material sin informe de ensayo. Escribe (a) qué documento consultarías para saber si el material cumple, (b) cuántas láminas y páginas de documentos hay en total sin contar los informes, (c) qué haces con la diferencia de la cuneta y a quién informas, (d) un riesgo de la obra y una medida de la jerarquía de controles.",
        "(a) El informe de ensayo de laboratorio. (b) 4+8 son 12 entre láminas y páginas. (c) Anoto la diferencia (el plano muestra cuneta y las especificaciones no) y la informo al proyectista o al ITO; no decido por mi cuenta. (d) Atropello; aislar con una barrera que separe a las personas de los camiones.",
        ["nombra el documento correcto", "suma bien", "informa la diferencia sin decidir por su cuenta", "reconoce un riesgo y un nivel de control"],
        ["hoja con las cuatro respuestas"],
        ["usar el material sin informe", "decidir cuál documento manda", "proponer el EPP como primera medida"],
        "Pregunta: «¿qué haces si el plano y las especificaciones no coinciden?». Si no responde, pídele que relea la regla de informar la diferencia."),
    reinforce="Escribe los tres tipos de documento de un proyecto vial y, junto a cada uno, una frase que diga para qué sirve.",
    extend="Explica con un ejemplo inventado por qué un material con buen aspecto puede no cumplir el estándar de calidad.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (planos descritos por escrito, de ejemplo, inventados). Camino «Los Aromos» (ficticio). Planta a escala 1:1000. El eje del camino se mide en progresivas: «Km 0+840» significa 0 km y 840 m desde el inicio. "
     "El tramo en estudio va del Km 0+000 al Km 0+840. Perfil longitudinal: en el Km 0+000 la cota del terreno es 100 m y la del camino proyectado es 101 m; en el Km 0+200 la cota del terreno es 103 m y la del camino proyectado es 102 m. "
     "Hay una sección transversal en el Km 0+200 con calzada, bermas y cunetas.")
build(
    O1, 2, F,
    use="Aprenderé a leer la planta, el perfil longitudinal y las secciones transversales de un camino descrito por escrito, y qué rol cumple cada persona de la obra.",
    prior=["Sé qué documentos forman un proyecto vial.", "Sé restar y multiplicar.", "Sé pasar de centímetros a metros."],
    explain=[
        "La planta es la vista del camino desde arriba; en ella se dibuja el eje, que es la línea central del camino. A lo largo del eje se miden las progresivas: distancias acumuladas desde el inicio, escritas como Km 1+250, que significa 1 km más 250 m, es decir 1.250 m. El perfil longitudinal es un corte vertical a lo largo del eje y muestra las cotas, que son las alturas, del terreno y del camino proyectado. Si el camino queda más bajo que el terreno hay un corte; si queda más alto hay un terraplén.",
        "La sección transversal es un corte perpendicular al eje. Muestra la calzada (parte por donde circulan los vehículos), las bermas (franjas laterales junto a la calzada) y las cunetas (canales laterales que recogen el agua). La escala es la razón entre la medida dibujada y la real: a escala 1:1000, 1 cm del plano son 1.000 cm, o sea 10 m reales. Los roles: el proyectista diseña, el ITO revisa por el mandante, el jefe de obra dirige a la constructora y el laboratorista ensaya los materiales.",
        f"Nadie cambia cotas ni medidas por su cuenta: lo decide el proyectista. {EMER} {AVISO}",
    ],
    vocab=[("eje", "línea central del camino"), ("progresiva", "distancia acumulada desde el inicio, escrita como Km 1+250"), ("cota", "número que indica la altura de un punto"), ("corte", "tramo donde el camino queda más bajo que el terreno"), ("terraplén", "tramo donde el camino queda más alto que el terreno"), ("calzada", "parte del camino por donde circulan los vehículos"), ("berma", "franja lateral junto a la calzada"), ("cuneta", "canal lateral que recoge el agua")],
    worked=[
        ("Distancia entre progresivas", "En otro camino de ejemplo hay una señal en el Km 1+250 y otra en el Km 1+700. ¿Qué distancia hay entre ellas?", ["Km 1+250 son 1.250 m y Km 1+700 son 1.700 m.", "1.700 menos 1.250 son 450."], "450 m"),
        ("Corte o terraplén", "En un punto de otro camino de ejemplo el terreno tiene cota 52 m y el camino proyectado, 50 m. ¿Hay corte o terraplén?", ["Se compara la cota del camino con la del terreno.", "El camino queda más bajo que el terreno."], "Corte"),
    ],
    mistakes=[("Leer Km 0+840 como 0,84 metros o como 840 km.", "La notación suma kilómetros y metros: 0 km más 840 m.", "Lee primero los kilómetros, luego los metros y pasa todo a metros."),
              ("Confundir el perfil longitudinal con la planta.", "La planta se ve desde arriba; el perfil longitudinal es un corte vertical con alturas.", "Si el dibujo muestra cotas, es perfil; si muestra el trazado visto desde arriba, es planta.")],
    T=[
        ("abc", "En Obras Viales: ¿qué muestra el perfil longitudinal de un camino?", "Las alturas del terreno y del camino a lo largo del eje", "El ancho de la calzada y de las bermas en un punto", "El trazado del camino visto desde arriba", "El perfil entrega cotas a lo largo del eje; el ancho está en la sección transversal y el trazado en la planta."),
        ("abc", "¿Qué es una progresiva en un plano vial?", "La distancia acumulada medida a lo largo del eje desde el inicio", "La altura de un punto sobre un nivel de referencia", "La razón entre la medida dibujada y la real", "La progresiva mide distancia a lo largo del eje; la altura es la cota y la razón es la escala."),
        ("abc", "En una sección transversal, ¿qué es la cuneta?", "Un canal lateral que recoge y conduce el agua", "La parte por donde circulan los vehículos", "Una franja lateral junto a la calzada", "La cuneta es el canal del agua; por la calzada circulan los vehículos y la berma es otra franja."),
        ("=", "{F} ¿Cuántos metros hay entre el Km 0+200 y el final del tramo en estudio, Km 0+840?", "840-200", "Se restan las dos progresivas expresadas en metros.", " m"),
        ("abc", "{F} En el Km 0+200, ¿qué hay según el perfil longitudinal?", "Un corte, porque el camino (102 m) queda más bajo que el terreno (103 m)", "Un terraplén, porque el terreno (103 m) queda más alto que el camino (102 m)", "Ni corte ni terraplén, porque la diferencia es de solo 1 m", "Si el camino queda bajo el terreno se llama corte; el terraplén es lo contrario y una diferencia pequeña igual se clasifica."),
        ("abc", "{F} ¿Qué significa que la planta esté a escala 1:1000?", "Que 1 cm del plano representa 1.000 cm reales", "Que el plano mide 1.000 cm de largo", "Que el camino tiene 1.000 progresivas", "La escala es una razón fija entre lo dibujado y lo real; no es el tamaño del plano ni un conteo."),
        ("=", "{F} En la planta, un segmento del eje mide 4 cm. ¿Cuántos metros reales representa?", "4*1000//100", "Se multiplican los 4 cm por 1.000 y se pasan los centímetros a metros dividiendo por 100.", " m"),
        ("abc", "{F} Un dibujante necesita mostrar el ancho de la calzada y de las cunetas en el Km 0+200. ¿Qué plano usa?", "La sección transversal en ese punto", "El perfil longitudinal", "La planta completa del tramo", "El ancho en un punto se ve en un corte perpendicular al eje, que es la sección transversal."),
        ("abc", "Una constructora de ejemplo termina un tramo y quiere saber quién revisa, en nombre del mandante, que cumpla el contrato. ¿Quién es?", "El ITO", "El proyectista", "El laboratorista", "El ITO inspecciona por el mandante; el proyectista diseña y el laboratorista ensaya."),
        ("ab", "{F} Un compañero dice: «en el Km 0+000 hay un corte porque el camino está más bajo». ¿Qué respuesta es correcta?", "No: la cota del camino (101 m) es mayor que la del terreno (100 m), así que hay un terraplén", "Sí: el camino queda más bajo que el terreno y por eso hay corte", "Al comparar las cotas del Km 0+000 el camino queda más alto que el terreno."),
        ("abc", "{F} Un informe de ensayo dice que la muestra se tomó en el Km 0+950, pero el tramo en estudio termina en el Km 0+840. ¿Qué conclusión es más prudente?", "La muestra está fuera del tramo: se consulta al ITO o al laboratorio por un posible error de registro", "La muestra sirve igual y se promedia con las demás", "Se corrige el informe cambiando 950 por 840", "Un dato fuera del tramo puede ser un error; se consulta y no se corrige el documento por cuenta propia."),
        ("=", "{F} El tramo entre el Km 0+200 y el Km 0+840 se divide en partes de 80 m para revisarlo. ¿Cuántas partes resultan?", "(840-200)//80", "Se calcula la longitud del tramo restando progresivas y se divide por 80.", " partes"),
        ("abc", "{F} Una estudiante lee «Km 0+200» y escribe en su cuaderno «200 km desde el inicio». ¿Qué corrección corresponde?", "Son 0 km más 200 m, es decir 200 m desde el inicio", "Son 2 km desde el inicio", "Son 20 m desde el inicio", "La notación suma kilómetros y metros: 0 km más 200 m equivalen a 200 m."),
    ],
    ctx=("abc", "Un amigo de un estudiante dice que ya sabe leer planos viales y propone ir a una obra a «medir y marcar el eje» por su cuenta. ¿Qué responde?", "Que leer planos en papel no lo autoriza a intervenir una obra y que el trabajo lo hace personal designado", "Que acepta si lleva su propio chaleco reflectante", "Que acepta si avisa por mensaje a un compañero", "Un chaleco o un aviso por mensaje no reemplazan la autorización ni la norma vigente de la obra."),
    sc=[
        ("En Obras Viales: ¿qué es un terraplén?", "Un tramo donde el camino queda más alto que el terreno", "Se compara la cota del camino con la del terreno: si es mayor, hay terraplén."),
        ("¿Qué distancia es Km 1+250?", "1.250 m desde el inicio", "La notación suma 1 km (1.000 m) y 250 m."),
        ("¿Qué plano muestra las alturas a lo largo del eje?", "El perfil longitudinal", "El perfil es el corte vertical a lo largo del eje y contiene las cotas."),
    ],
    op=("Camino de ejemplo «Las Vertientes» (ficticio). Planta a escala 1:2000. Perfil longitudinal: en el Km 0+100 la cota del terreno es 80 m y la del camino proyectado, 79 m; en el Km 0+500 el terreno es 76 m y el camino, 78 m. Escribe (a) cuántos metros hay entre el Km 0+100 y el Km 0+500, (b) si en cada progresiva hay corte o terraplén y por qué, (c) cuántos metros reales representan 3 cm de la planta, (d) qué documento mostraría el ancho de la calzada.",
        "(a) 500-100 son 400 m. (b) En el Km 0+100 hay corte porque el camino (79 m) queda más bajo que el terreno (80 m); en el Km 0+500 hay terraplén porque el camino (78 m) queda más alto que el terreno (76 m). (c) 3 cm por 2.000 son 6.000 cm, o sea 60 m. (d) La sección transversal.",
        ["resta bien las progresivas", "compara las cotas y nombra corte o terraplén", "usa la escala correctamente", "elige la sección transversal"],
        ["hoja con las cuatro respuestas"],
        ["leer Km 0+100 como 100 km", "invertir corte y terraplén", "olvidar pasar centímetros a metros"],
        "Pregunta: «¿cómo decidiste si era corte o terraplén?». Si no responde, pídele que compare la cota del camino con la del terreno."),
    reinforce="Dibuja en tu cuaderno una tabla con las palabras eje, progresiva, cota, corte y terraplén y escribe una frase de ejemplo para cada una.",
    extend="Explica por qué en un tramo largo pueden alternarse cortes y terraplenes aunque el camino sea casi plano.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (informe de ensayo de ejemplo, inventado). Laboratorio de ejemplo. Material de base del camino «Los Aromos» (ficticio), Km 0+000 al Km 0+840. "
     "Valor exigido en las especificaciones: índice de calidad mínimo de 80 puntos (valor de ejemplo, no normativo). Muestras: M1 (Km 0+100) 84 puntos; M2 (Km 0+300) 79 puntos; M3 (Km 0+500) 91 puntos; M4 (Km 0+700) 80 puntos.")
build(
    O1, 3, F,
    use="Aprenderé a leer un informe de ensayo de ejemplo, compararlo con lo exigido en las especificaciones y registrar un incumplimiento sin alterar resultados.",
    prior=["Sé qué documentos forman un proyecto vial.", "Sé leer progresivas.", "Sé comparar números."],
    explain=[
        "Un informe de ensayo identifica el material, el lugar donde se tomó la muestra (con su progresiva), la fecha, el valor medido y la conclusión. Las especificaciones fijan el valor exigido. Si la especificación pide un mínimo, el resultado cumple cuando es igual o mayor que ese mínimo; si pide un máximo, cumple cuando es igual o menor. Un resultado que justo iguala el límite cumple; uno que queda bajo un mínimo no cumple, aunque sea por muy poco.",
        "Cuando una muestra no cumple, nadie cambia el número, repite el ensayo hasta que salga bien ni promedia con otras muestras para esconder el resultado. Se informa al ITO y al jefe de calidad, se deja un registro con el punto, el valor medido, el valor exigido, la fecha y quién lo detectó, y la decisión (por ejemplo, repetir un ensayo o revisar el tramo) la toman el ITO y el proyectista. Un informe sin progresiva, sin fecha o sin valores se devuelve al laboratorio para aclararlo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("valor medido", "resultado que entrega el laboratorio para una muestra"), ("valor exigido", "límite que fijan las especificaciones"), ("mínimo", "límite que el resultado debe igualar o superar"), ("máximo", "límite que el resultado debe igualar o no superar"), ("muestra", "porción de material tomada en un punto identificado para ensayarla"), ("registro", "anotación escrita de lo detectado, con fecha y responsable")],
    worked=[
        ("Comparar con un mínimo", "Otro informe de ejemplo exige un mínimo de 60 puntos y una muestra mide 62. ¿Cumple?", ["El mínimo se iguala o se supera.", "62 es mayor que 60."], "Cumple"),
        ("Comparar con un máximo", "Una especificación de ejemplo exige humedad máxima de 12 y el informe mide 15. ¿Cumple?", ["Con un máximo, el valor medido debe ser igual o menor.", "15 es mayor que 12."], "No cumple"),
    ],
    mistakes=[("Decir que 79 cumple un mínimo de 80 porque «está muy cerca».", "Un mínimo se alcanza o no se alcanza; la cercanía no cuenta.", "Compara el número medido con el límite y registra si está bajo él."),
              ("Repetir el ensayo hasta que dé un buen resultado y borrar el primero.", "Eso oculta información; todos los resultados deben quedar registrados.", "Informa al ITO, que decide si corresponde repetir el ensayo y cómo se registra.")],
    T=[
        ("abc", "En Obras Viales: ¿qué significa que una especificación fije un valor mínimo?", "Que el resultado medido debe ser igual o mayor que ese valor", "Que el resultado medido debe ser igual o menor que ese valor", "Que el resultado medido debe ser exactamente igual a ese valor", "Un mínimo se alcanza o se supera; igual o menor corresponde a un máximo."),
        ("abc", "¿Qué datos debe traer un informe de ensayo para poder usarlo?", "Material, lugar de la muestra, fecha, valor medido y valor exigido", "Solo el nombre del laboratorio y la firma", "Solo la palabra «cumple»", "Sin lugar, fecha y valores no se puede verificar nada; una conclusión sola no es evidencia."),
        ("abc", "Una muestra de ejemplo no cumple el mínimo exigido. ¿Qué corresponde?", "Informar al ITO y al jefe de calidad y dejar un registro", "Repetir el ensayo hasta que dé un resultado mayor", "Promediar con las otras muestras para que cumpla", "El incumplimiento se informa y registra; repetir hasta aprobar o promediar lo esconde."),
        ("=", "{F} ¿Cuántos puntos sobre el mínimo exigido tiene la muestra M3?", "91-80", "Se resta el mínimo exigido al valor medido de M3.", " puntos"),
        ("abc", "{F} ¿Qué muestras cumplen el mínimo exigido?", "M1, M3 y M4", "M1 y M3", "M1, M2 y M3", "M4 iguala el mínimo y cumple; M2 está un punto bajo el mínimo y no cumple."),
        ("abc", "{F} La muestra M2 mide 79 puntos. ¿Qué conclusión corresponde?", "No cumple, porque queda un punto bajo el mínimo", "Cumple, porque la diferencia es mínima", "Cumple si se redondea 79 a 80", "El mínimo no admite redondeos ni cercanías: 79 está bajo 80."),
        ("=", "{F} ¿Qué porcentaje de las 4 muestras cumple el mínimo?", "3*100//4", "Cumplen 3 de 4 muestras: se divide entre 4 y se multiplica por 100.", " %"),
        ("abc", "Un informe de ejemplo mide humedad 14 y la especificación exige un máximo de 12. ¿Qué corresponde concluir?", "No cumple, porque supera el máximo", "Cumple, porque 14 es mayor que 12", "Cumple si hay otras muestras con menos humedad", "Con un máximo, el valor debe ser igual o menor; 14 lo supera."),
        ("ab", "{F} El jefe de obra pide cambiar el 79 de M2 por un 80 «para no atrasar la obra». ¿Qué respuesta es correcta?", "No se modifica el informe: la diferencia se informa al ITO y se registra", "Se acepta, porque el jefe de obra manda sobre el laboratorio", "Un informe del laboratorio no lo corrige quien tiene interés en el resultado."),
        ("abc", "{F} Un compañero propone ensayar M2 otra vez en otro punto, hasta que dé 80 o más, y usar solo ese resultado. ¿Por qué es incorrecto?", "Porque oculta el resultado original: todos los resultados se registran y el ITO decide si se repite", "Porque repetir un ensayo siempre está prohibido", "Porque 79 y 80 son valores iguales", "Descartar el primer resultado esconde información; repetir solo lo decide el ITO y se registran ambos."),
        ("abc", "Un informe de ejemplo no indica la progresiva donde se tomó la muestra. ¿Qué corresponde?", "Pedir al laboratorio que lo aclare antes de usar el informe", "Asumir que fue la progresiva más cercana", "Usar el informe igual, porque el valor es lo importante", "Sin ubicación no se sabe qué tramo representa el resultado; se aclara antes de usarlo."),
        ("=", "{F} Si el mínimo exigido fuera 85 puntos, ¿cuántos puntos faltan en total sumando las muestras que no lo alcanzarían?", "(85-84)+(85-79)+(85-80)", "Las muestras M1, M2 y M4 quedarían bajo 85; se suma lo que falta a cada una.", " puntos"),
        ("abc", "{F} El jefe de obra dice: «M2 no cumple, pero las otras tres sí, así que seguimos». ¿Qué respuesta es correcta?", "El tramo que representa M2 queda observado hasta que el ITO decida", "Se sigue sin cambios porque la mayoría cumple", "Se detiene toda la obra y se descarta el material de todos los tramos", "Cada muestra representa un lugar: el incumplimiento se trata en ese tramo, sin ignorarlo ni extenderlo a todo."),
    ],
    ctx=("abc", "En una obra de ejemplo, un trabajador le pide a una estudiante en práctica que firme como conforme un informe de ensayo «para no atrasar». ¿Qué responde?", "Que no firma documentos que no le corresponden y que lo derive al ITO o al jefe de calidad", "Que firma si vio la muestra", "Que firma si el valor está cerca del mínimo", "Firmar un informe corresponde a quien tiene la responsabilidad; ver la muestra o la cercanía no reemplazan eso."),
    sc=[
        ("En Obras Viales: ¿cuándo cumple un resultado frente a un mínimo?", "Cuando es igual o mayor que el mínimo", "El mínimo se alcanza o se supera; un valor menor no cumple."),
        ("¿Qué se hace con un resultado que no cumple?", "Informar al ITO y al jefe de calidad y dejar un registro", "El incumplimiento no se oculta ni se corrige por cuenta propia."),
        ("¿Qué datos lleva un registro de incumplimiento?", "Punto, valor medido, valor exigido, fecha y quién lo detectó", "Esos datos permiten ubicar y revisar el problema después."),
    ],
    op=("Informe de ejemplo de un laboratorio ficticio: el material de una subbase exige un mínimo de 70 puntos (de ejemplo). Muestras: S1 (Km 0+050) 75; S2 (Km 0+250) 68; S3 (Km 0+450) 70; S4 (Km 0+650) 66. Escribe (a) qué muestras cumplen, (b) qué porcentaje de las 4 cumple, (c) qué datos pondrías en el registro del incumplimiento de S2 y a quién informas, (d) por qué no se debe promediar para que cumplan.",
        "(a) S1 y S3 (S3 iguala el mínimo). (b) 2 de 4 son 50 %. (c) Punto S2 en Km 0+250, valor medido 68, valor exigido 70, fecha y quién lo detectó; informo al ITO y al jefe de calidad. (d) El promedio esconde que S2 y S4 están bajo el mínimo y cada muestra representa un lugar distinto.",
        ["identifica bien las muestras que cumplen", "calcula el porcentaje", "completa el registro con datos y destinatarios", "explica por qué no se promedia"],
        ["hoja con las cuatro respuestas"],
        ["decir que S3 no cumple por igualar el mínimo", "calcular mal el porcentaje", "proponer repetir hasta que cumpla"],
        "Pregunta: «¿cumple un resultado que justo iguala el mínimo?». Si dice que no, pídele que relea cómo se define un mínimo."),
    reinforce="Escribe tres frases: una con un mínimo que se cumple, otra con un mínimo que no se cumple y otra con un máximo que no se cumple, usando números inventados.",
    extend="Explica por qué dos muestras de lugares distintos no se pueden reemplazar una por otra en el informe.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (planilla de control de ejemplo, inventada). Control de espesor de una capa de base del camino «Los Aromos» (ficticio); los valores son de ejemplo, no normativos. "
     "Exigencia de las especificaciones: espesor mínimo de 20 cm en cada punto de control. Puntos, uno cada 200 m desde el Km 0+000: P1 (Km 0+000) 22 cm; P2 (Km 0+200) 20 cm; P3 (Km 0+400) 18 cm; P4 (Km 0+600) 25 cm; P5 (Km 0+800) 20 cm. "
     "Ancho de la capa: 6 m.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: comparar valores con lo exigido, calcular promedios, porcentajes y volúmenes en una planilla.",
    prior=["Sé comparar un valor con un mínimo.", "Sé leer progresivas.", "Sé multiplicar y dividir."],
    explain=[
        "Un criterio técnico es la regla con que se decide si algo cumple. Primero hay que leer cómo lo fija la especificación. Si exige un mínimo «en cada punto», ningún punto puede quedar bajo ese valor, y un punto alto no compensa a uno bajo. Si exige un «promedio mínimo», se calcula el promedio, que es la suma de los valores dividida por la cantidad de valores, y se compara con el mínimo.",
        "En una planilla también se calculan porcentajes (partes que cumplen dividido por el total, por 100) y volúmenes. El volumen de una capa es largo por ancho por espesor, con todas las medidas en metros; para pasar centímetros a metros se divide por 100. Todos estos números son de ejemplo y sirven para calcular, no para ejecutar trabajos. La decisión sobre qué hacer con un incumplimiento la toma el ITO con el proyectista.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("criterio técnico", "regla con que se decide si algo cumple lo exigido"), ("promedio", "suma de los valores dividida por la cantidad de valores"), ("espesor", "medida del grosor de una capa"), ("volumen", "cantidad de espacio que ocupa un material, en metros cúbicos (m³)"), ("planilla", "tabla de cálculo con datos y resultados"), ("punto de control", "lugar identificado donde se mide un valor")],
    worked=[
        ("Calcular un promedio", "Otro control de ejemplo mide espesores de 15, 17 y 19 cm. ¿Cuál es el promedio?", ["Se suman: 15+17+19 son 51.", "Se divide por 3 valores: 17."], "17 cm"),
        ("Calcular un volumen", "Una capa de ejemplo mide 50 m de largo, 4 m de ancho y 10 cm de espesor. ¿Cuántos m³ son?", ["Los 10 cm son 10 dividido por 100 metros.", "50 por 4 por 10 son 2.000; dividido por 100 es 20."], "20 m³"),
    ],
    mistakes=[("Compensar un punto bajo con uno alto cuando se exige el mínimo en cada punto.", "La exigencia es por punto, no por promedio.", "Revisa cada punto contra el mínimo y registra los que quedan bajo él."),
              ("Multiplicar el espesor en centímetros directamente por largo y ancho en metros.", "Las tres medidas deben estar en la misma unidad.", "Pasa los centímetros a metros dividiendo por 100 antes de multiplicar.")],
    T=[
        ("abc", "En Obras Viales: una especificación de ejemplo exige un espesor mínimo «en cada punto». ¿Qué significa?", "Que ningún punto controlado puede quedar bajo el mínimo", "Que el promedio de los puntos debe alcanzar el mínimo", "Que basta con que el primer punto lo cumpla", "La exigencia por punto se verifica punto a punto; el promedio es otra forma de exigir."),
        ("abc", "¿Cómo se calcula el promedio de varios valores?", "Se suman los valores y se divide por la cantidad de valores", "Se suman el mayor y el menor y se divide por dos", "Se resta el menor al mayor", "El promedio usa todos los valores; las otras opciones usan solo dos o calculan otra cosa."),
        ("abc", "Para pasar un espesor de centímetros a metros antes de calcular un volumen, ¿qué se hace?", "Se divide por 100", "Se multiplica por 100", "Se divide por 10", "Un metro tiene 100 cm; por eso se divide por 100."),
        ("=", "{F} ¿Cuántos centímetros le faltan al punto P3 para alcanzar el espesor mínimo?", "20-18", "Se resta el espesor medido al mínimo exigido.", " cm"),
        ("abc", "{F} ¿Qué puntos quedan bajo el espesor mínimo exigido?", "Solo P3", "P2 y P3", "P1 y P4", "P2 y P5 igualan el mínimo y cumplen; solo P3 queda bajo 20 cm."),
        ("=", "{F} ¿Cuál es el promedio de los espesores de los cinco puntos?", "(22+20+18+25+20)//5", "Se suman los cinco espesores y se divide por 5.", " cm"),
        ("=", "{F} ¿Cuántos metros cuadrados de superficie tiene la capa entre el Km 0+000 y el Km 0+800?", "800*6", "La superficie es el largo del tramo por el ancho de la capa.", " m²"),
        ("=", "{F} ¿Qué porcentaje de los puntos de control cumple el espesor mínimo?", "4*100//5", "Cumplen 4 de 5 puntos: se divide entre 5 y se multiplica por 100.", " %"),
        ("abc", "{F} El ITO pide el registro del incumplimiento. ¿Qué debe incluir como mínimo?", "El punto (P3, Km 0+400), el espesor medido, el exigido, la fecha y quién lo detectó", "Solo la frase «P3 no cumple»", "Solo el nombre de quien lo detectó", "Un registro útil dice dónde, cuánto, contra qué exigencia, cuándo y quién."),
        ("ab", "{F} Un compañero afirma que la capa cumple porque el promedio de los puntos supera el mínimo. ¿Qué respuesta es correcta?", "No: la exigencia es en cada punto, así que P3 bajo el mínimo no se compensa con otros", "Sí: si el promedio supera el mínimo toda la capa cumple", "Cuando se exige en cada punto, un valor alto no puede tapar uno bajo."),
        ("abc", "{F} Un compañero dice que P2 no cumple porque «apenas iguala el mínimo y no lo supera». ¿Qué corresponde?", "P2 cumple, porque la especificación exige mínimo 20 cm y mide 20 cm", "P2 no cumple, porque debe superar el mínimo", "P2 cumple solo si se mide otra vez", "Un mínimo se cumple al igualarlo o superarlo; medir de nuevo no es necesario."),
        ("=", "{F} Si el tramo completo tuviera exactamente el espesor mínimo exigido, ¿cuántos m³ de material tendría la capa?", "800*6*20//100", "Volumen = largo por ancho por espesor, con el espesor pasado de cm a metros.", " m³"),
        ("abc", "{F} La constructora propone que se apruebe la capa usando el promedio medido en vez del mínimo en cada punto. ¿Qué consideración es correcta?", "El criterio lo fija el contrato con las especificaciones y lo aplica el ITO; no se cambia por conveniencia", "Siempre corresponde usar el promedio", "Siempre corresponde usar el valor más bajo de todos", "Cómo se evalúa lo define el contrato; nadie elige el criterio que más le conviene."),
    ],
    ctx=("abc", "Un estudiante de ejemplo debe resumir una planilla para el ITO. Los cinco puntos cumplen salvo uno. ¿Cómo la resume?", "Indica que cuatro puntos cumplen, señala cuál no cumple con su valor y su progresiva, y entrega los datos", "Escribe solo que «en general cumple»", "Omite el punto que no cumple para no alarmar", "El resumen debe ser fiel: incluye el punto que no cumple, con valor y ubicación."),
    sc=[
        ("En Obras Viales: ¿cómo se calcula el promedio?", "Sumando los valores y dividiendo por la cantidad de valores", "Se usan todos los valores, no solo el mayor y el menor."),
        ("¿Cómo se calcula el volumen de una capa?", "Largo por ancho por espesor, con todas las medidas en metros", "Las tres medidas deben estar en la misma unidad."),
        ("¿Se compensa un punto bajo con uno alto cuando se exige el mínimo en cada punto?", "No, cada punto se compara con el mínimo", "La exigencia es por punto y no por promedio."),
    ],
    op=("Planilla de ejemplo de una capa de un camino ficticio (valores de ejemplo, no normativos). Exigencia: espesor mínimo de 15 cm en cada punto. Puntos cada 100 m desde el Km 0+000: Q1 16 cm; Q2 15 cm; Q3 13 cm; Q4 18 cm. Ancho: 5 m. Escribe (a) qué puntos no cumplen y cuánto les falta, (b) qué porcentaje de los puntos cumple, (c) cuántos m³ tendría la capa entre el Km 0+000 y el Km 0+300 con el espesor mínimo exigido, (d) qué datos irían en el registro del incumplimiento.",
        "(a) Q3, le faltan 2 cm. (b) 3 de 4 son 75 %. (c) 300 m por 5 m por 15 cm: 300*5*15 son 22.500, dividido por 100 son 225 m³. (d) Punto Q3 (Km 0+200), 13 cm medidos, 15 cm exigidos, fecha y quién lo detectó.",
        ["identifica el punto que no cumple", "calcula el porcentaje", "calcula el volumen pasando cm a m", "completa el registro"],
        ["hoja con las cuatro respuestas"],
        ["compensar con otro punto", "no pasar cm a m", "omitir la progresiva en el registro"],
        "Pregunta: «¿por qué no usaste el promedio?». Si no responde, pídele que relea qué significa «en cada punto»."),
    reinforce="Inventa una planilla de tres puntos con un mínimo y marca cuál cumple, cuál no y cuánto falta.",
    extend="Explica la diferencia entre exigir un mínimo en cada punto y exigir un promedio mínimo, con un ejemplo de números.",
)

# ============================================================ OAM-01, clase 5
F = ("Ficha 5 (ofertas de ejemplo, inventadas). Para una subbase del camino «Los Aromos» (ficticio) se necesitan 400 m³ de material. El mínimo exigido en las especificaciones es 80 puntos (valor de ejemplo). "
     "Oferta A: $9.000 por m³, con informe de ensayo (resultado 82 puntos), plazo de 5 días. Oferta B: $7.500 por m³, sin informe de ensayo, plazo de 3 días. "
     "Oferta C: $8.000 por m³, con informe de ensayo (resultado 76 puntos), plazo de 4 días.")
build(
    O1, 5, F,
    use="Aprenderé a comparar alternativas con un requisito de calidad primero y el costo y el plazo después, y a verificar la calidad con una lista de verificación.",
    prior=["Sé comparar un resultado con un mínimo.", "Sé calcular un costo total.", "Sé qué es un informe de ensayo."],
    explain=[
        "Para comparar alternativas se separan los requisitos excluyentes de los criterios de comparación. Un requisito excluyente es una condición que, si no se cumple, deja fuera la alternativa aunque sea más barata: por ejemplo, tener informe de ensayo y alcanzar el valor mínimo exigido. Solo las alternativas que pasan ese filtro se comparan por costo total y plazo. El costo total es el precio unitario por la cantidad, más los costos extra de ejemplo, como un atraso.",
        "La calidad se verifica con una lista de verificación: preguntas que se marcan como cumple o no cumple, cada una con su evidencia, como el informe, la fecha y la progresiva. Una lista con un punto en blanco no está completa y no se aprueba hasta aclararlo. El precio más bajo no justifica aprobar algo que no se puede verificar.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("requisito excluyente", "condición que, si no se cumple, deja fuera una alternativa"), ("costo total", "precio unitario por cantidad, más costos extra"), ("lista de verificación", "conjunto de preguntas que se marcan como cumple o no cumple, con evidencia"), ("alternativa", "una de las opciones que se comparan"), ("plazo", "tiempo en días para entregar"), ("evidencia", "documento o dato que respalda una respuesta")],
    worked=[
        ("Filtrar y comparar", "Dos ofertas de arena de ejemplo: X cuesta $6.000 por m³ y su informe cumple; Y cuesta $5.000 por m³ y su informe no cumple. ¿Cuál se compara?", ["Primero se aplica el requisito excluyente.", "Y no cumple y queda fuera aunque sea más barata."], "Solo X"),
        ("Costo total", "La oferta X de ejemplo cuesta $6.000 por m³ y se necesitan 150 m³. ¿Cuál es el costo total?", ["Se multiplica el precio por la cantidad.", "6.000 por 150 son 900.000."], "$900.000"),
    ],
    mistakes=[("Elegir la oferta más barata antes de revisar si cumple.", "La calidad es un requisito excluyente; el precio solo compara las que cumplen.", "Aplica primero el filtro de cumplimiento y después compara costo y plazo."),
              ("Aprobar una lista de verificación con una casilla en blanco.", "Una casilla en blanco significa que falta evidencia.", "Aclara el punto con el laboratorio o el ITO antes de aprobar.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es un requisito excluyente al comparar ofertas?", "Una condición que deja fuera la oferta si no se cumple, aunque sea más barata", "Una condición que se prefiere pero que puede no cumplirse", "El precio más bajo entre todas las ofertas", "Un requisito excluyente funciona como filtro previo; el precio solo compara las ofertas que lo cumplen."),
        ("abc", "¿Para qué sirve una lista de verificación de calidad?", "Para marcar cumple o no cumple en cada punto, con su evidencia", "Para decidir quién cobra más en la obra", "Para reemplazar al informe de ensayo", "La lista ordena la revisión y exige evidencia; no reemplaza el informe."),
        ("abc", "¿Cómo se calcula el costo total de comprar un material?", "Precio unitario por cantidad, más costos extra si los hay", "Solo el precio unitario", "La cantidad dividida por el precio", "El costo total combina precio y cantidad; el precio unitario solo indica el valor de cada unidad."),
        ("=", "{F} ¿Cuánto cuesta en total la oferta A para los 400 m³?", "9000*400", "El costo total es el precio por m³ multiplicado por la cantidad.", " pesos"),
        ("abc", "{F} ¿Qué oferta queda fuera porque no presenta informe de ensayo?", "Oferta B", "Oferta A", "Oferta C", "Solo la oferta B no trae informe; A y C sí lo presentan."),
        ("abc", "{F} ¿Por qué la oferta C no cumple los requisitos?", "Porque su resultado (76) queda bajo el mínimo exigido de 80", "Porque es la más cara de las tres", "Porque tiene el plazo más largo de las tres", "C es más barata que A y más rápida; su problema es que 76 está bajo 80."),
        ("=", "{F} Si se comprara a la oferta B en vez de a la A, ¿cuántos pesos menos costaría el total de los 400 m³?", "(9000-7500)*400", "Se multiplica la diferencia de precio por m³ por la cantidad.", " pesos"),
        ("abc", "{F} ¿Qué oferta cumple a la vez el requisito de tener informe y el de alcanzar el mínimo?", "Oferta A", "Oferta B", "Oferta C", "A trae informe con 82, sobre el mínimo; B no trae informe y C queda bajo el mínimo."),
        ("abc", "{F} El jefe de obra quiere elegir la oferta B «porque es la más barata». ¿Qué respuesta es correcta?", "Sin informe no se puede verificar la calidad, así que el ahorro no justifica aprobarla", "B es válida porque llega antes", "B es válida si el proveedor la recomienda", "Un plazo corto o una recomendación no reemplazan la evidencia de calidad."),
        ("ab", "{F} Si la oferta B presentara antes de comprar un informe con resultado 81, ¿qué cambiaría?", "Pasaría el filtro de cumplimiento y recién entonces se compararía con A por costo y plazo", "Ganaría de inmediato por ser la más barata, sin comparar nada más", "Con un informe que cumple, B entra a la comparación; no gana automáticamente."),
        ("abc", "Una lista de verificación marca «cumple» en «informe presente» y en «resultado sobre el mínimo», pero «fecha del informe» está en blanco. ¿Qué corresponde?", "Pedir la fecha al laboratorio antes de aprobar", "Aprobar porque los dos puntos principales cumplen", "Escribir la fecha de hoy en la casilla", "Una casilla en blanco es evidencia faltante; no se completa por suposición."),
        ("=", "{F} La obra pierde $120.000 de ejemplo por cada día después del tercer día. ¿Cuánto suma el atraso de la oferta A?", "(5-3)*120000", "Se multiplican los días de atraso (5 menos 3) por el valor de cada día.", " pesos"),
        ("abc", "{F} Una oferta D de ejemplo cumple los requisitos, cuesta $9.500 por m³ y entrega en 3 días. La obra pierde $120.000 por cada día después del tercero. Para 400 m³, ¿qué oferta tiene menor costo total, A o D?", "La oferta D", "La oferta A", "Cuestan exactamente lo mismo", "A cuesta 3.600.000 más 240.000 de atraso; D cuesta 3.800.000 sin atraso, que es menos."),
    ],
    ctx=("abc", "Un proveedor de ejemplo le regala una cena a un estudiante en práctica para que «ayude» a que su oferta pase el filtro. ¿Qué responde?", "Rechaza el regalo e informa a su supervisor, porque las ofertas se evalúan solo con los requisitos", "Acepta si no cambia ningún número", "Acepta y no cuenta nada para no causar problemas", "Aceptar regalos compromete la imparcialidad; se rechaza y se informa."),
    sc=[
        ("En Obras Viales: ¿qué es un requisito excluyente?", "Una condición que deja fuera la oferta si no se cumple", "El requisito excluyente se aplica antes de comparar precios."),
        ("¿Se aprueba una lista de verificación con una casilla en blanco?", "No, primero se aclara y se obtiene la evidencia", "Una casilla en blanco significa que falta evidencia."),
        ("¿Cómo se calcula el costo total de una compra?", "Precio unitario por cantidad, más costos extra", "El total combina precio, cantidad y costos adicionales."),
    ],
    op=("Ofertas de ejemplo para 200 m³ de material. Mínimo exigido: 60 puntos (de ejemplo). Oferta P: $7.000 por m³, informe con 65 puntos, plazo de 4 días. Oferta Q: $6.000 por m³, sin informe, plazo de 2 días. Oferta R: $6.500 por m³, informe con 58 puntos, plazo de 3 días. Escribe (a) qué ofertas pasan el filtro de calidad y por qué las otras no, (b) el costo total de la oferta que pasa, (c) qué dirías si el jefe de obra pide elegir Q por su precio, (d) qué casilla de una lista de verificación quedaría en blanco para Q.",
        "(a) Solo P: Q no tiene informe y R mide 58, bajo el mínimo de 60. (b) 7.000 por 200 son 1.400.000 pesos. (c) Que sin informe no se puede verificar la calidad y el ahorro no justifica aprobarla. (d) La de «informe de ensayo presente» y la del resultado.",
        ["aplica primero el filtro de calidad", "calcula el costo total", "argumenta contra elegir por precio", "identifica la evidencia faltante"],
        ["hoja con las cuatro respuestas"],
        ["comparar precios antes del filtro", "equivocar el cálculo del total", "aceptar la oferta sin informe"],
        "Pregunta: «¿qué haces primero, comparar precios o revisar si cumple?». Si no responde, pídele que relea el requisito excluyente."),
    reinforce="Escribe dos requisitos excluyentes y dos criterios de comparación para elegir un material, con tus palabras.",
    extend="Explica con un ejemplo inventado cuándo una oferta más cara puede ser más conveniente que una más barata.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 6 (itemizado de ejemplo, inventado). Obra «Calle Los Quillayes» (ficticia), de mediana envergadura. Partidas del contrato: P1 despeje de la franja, 4.000 m²; P2 movimiento de tierra, 1.800 m³; P3 base, 1.200 m³; P4 señalización, 12 unidades. "
     "Documentos: itemizado (1 hoja), planos (6 láminas), especificaciones técnicas (10 páginas) y libro de obra. Riesgos anotados: atropello, vuelco de máquinas, polvo y caída de talud.")
build(
    O2, 1, F,
    use="Aprenderé qué es una partida de una obra vial, qué significa verificarla, quién participa y qué riesgos y reglas de seguridad rodean esa verificación.",
    prior=["Sé qué documentos forman un proyecto vial.", "Sé multiplicar.", "Sé qué hace el ITO."],
    explain=[
        "Una partida es cada parte del trabajo que el contrato mide y paga por separado. Cada partida tiene un nombre, una unidad de medida (metros cuadrados, metros cúbicos, metros lineales o unidades), una cantidad y un precio. El itemizado es la lista de las partidas de la obra. Una obra de mediana envergadura es una obra de tamaño intermedio, con varias partidas y varios roles participando. Verificar una partida es comprobar, con documentos y registros, que lo ejecutado corresponde a lo que piden los planos y las especificaciones y a la cantidad que se declara.",
        "Quien verifica compara tres cosas: lo declarado por la constructora, lo registrado en el libro de obra y lo exigido por planos y especificaciones. Si algo no coincide, se informa al ITO y no se da por verificado. Una visita a terreno la hacen personas autorizadas, con elementos de protección personal (EPP) y acompañadas, porque en una obra vial hay atropello, vuelco de máquinas, polvo y caída de taludes. La jerarquía de controles pone primero eliminar o aislar el peligro y deja el EPP al final.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("partida", "parte del trabajo que el contrato mide y paga por separado"), ("itemizado", "lista de las partidas de la obra con unidad, cantidad y precio"), ("unidad de medida", "magnitud con que se mide una partida, como m², m³ o unidades"), ("verificar", "comprobar con documentos y registros que lo ejecutado cumple lo pedido"), ("libro de obra", "registro escrito de los hechos de la obra"), ("mediana envergadura", "obra de tamaño intermedio, con varias partidas y roles")],
    worked=[
        ("Elegir la unidad", "Una partida de ejemplo «cuneta revestida» se mide por la longitud que tiene la cuneta. ¿Qué unidad usa?", ["La longitud se mide en metros lineales.", "Es una partida medida en metros (m)."], "Metros lineales"),
        ("Monto de una partida", "Una partida de ejemplo de 20 unidades se paga a $5.000 por unidad. ¿Cuál es su monto?", ["Se multiplica la cantidad por el precio.", "20 por 5.000 son 100.000."], "$100.000"),
    ],
    mistakes=[("Creer que una partida está verificada porque aparece en el itemizado.", "El itemizado solo dice qué se contrató, no qué se ejecutó.", "Verifica contra el libro de obra, las especificaciones y los informes."),
              ("Entrar a la zona de máquinas a «mirar» una partida sin autorización.", "Hay riesgo de atropello y vuelco, y se necesita autorización y EPP.", "Pide que la visita la haga personal autorizado y acompañado.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es una partida de un contrato?", "Una parte del trabajo que se mide y se paga por separado", "Una lámina del plano de planta", "Un resultado de laboratorio", "La partida es una unidad del contrato con cantidad y precio; la lámina y el resultado son otros documentos."),
        ("abc", "¿Qué muestra el itemizado de una obra?", "La lista de partidas con su unidad, cantidad y precio", "El detalle de los riesgos de cada persona", "Los resultados medidos de cada muestra", "El itemizado lista lo contratado; los resultados medidos están en los informes de ensayo."),
        ("abc", "En una obra vial de ejemplo, ¿qué significa verificar una partida?", "Comprobar con documentos y registros que lo ejecutado cumple lo pedido y lo declarado", "Ejecutar otra vez la partida para comprobarla", "Pagar la partida apenas se declara", "Verificar es comprobar con evidencia, no repetir el trabajo ni pagar sin revisar."),
        ("=", "{F} Entre movimiento de tierra y base, ¿cuántos m³ suman las dos partidas?", "1800+1200", "Ambas partidas se miden en m³, así que se suman sus cantidades.", " m³"),
        ("abc", "{F} ¿Con qué unidad se mide la partida P1, despeje de la franja?", "Metros cuadrados (m²)", "Metros cúbicos (m³)", "Unidades", "La ficha indica que P1 tiene 4.000 m², una medida de superficie."),
        ("abc", "{F} ¿Cuál de estos riesgos aparece anotado en la ficha?", "Caída de talud", "Intoxicación en un espacio confinado", "Descarga eléctrica en un tablero", "La ficha nombra la caída de talud; los otros riesgos no están anotados."),
        ("=", "{F} La partida P4 se paga a $85.000 por unidad (valor de ejemplo). ¿Cuál es el monto total de P4?", "12*85000", "El monto es la cantidad de unidades por el precio de cada una.", " pesos"),
        ("abc", "{F} Un visitante sin autorización quiere «verificar» P2 entrando a la zona de las máquinas. ¿Qué corresponde?", "No entrar: la visita a terreno la hace personal autorizado, con EPP y acompañado", "Entrar si usa un chaleco reflectante", "Entrar si en ese momento hay poco movimiento", "El chaleco o la poca actividad no reemplazan la autorización ni el acompañamiento."),
        ("ab", "{F} Una compañera dice: «P3 aparece en el itemizado, así que ya está verificada». ¿Qué respuesta es correcta?", "No: estar en el itemizado solo indica que está contratada; se verifica con registros y especificaciones", "Sí: toda partida del itemizado está verificada", "El itemizado dice lo que se contrató, no lo que ya se ejecutó."),
        ("abc", "{F} El jefe de obra declara terminada P2, pero el libro de obra no registra su ejecución. ¿Qué corresponde?", "Informar al ITO y pedir los registros antes de darla por verificada", "Darla por verificada porque el jefe de obra lo declara", "Anotar en el libro que se ejecutó, sin consultar", "Sin registro no hay evidencia; se informa y se solicita, no se completa por suposición."),
        ("abc", "{F} Los planos muestran 11 señales, pero el itemizado de P4 pide 12 unidades. ¿Qué conclusión es la más prudente?", "Hay una diferencia entre documentos: se informa al proyectista o al ITO antes de verificar", "Se sigue el itemizado porque tiene precio", "Se sigue el plano porque es un dibujo", "Ningún documento manda por sí solo: la diferencia se informa a quien decide."),
        ("=", "{F} Se declara ejecutada la mitad de P1. Con un precio de ejemplo de $900 por m², ¿qué monto corresponde a esa mitad?", "(4000//2)*900", "Se calcula la mitad de la cantidad y se multiplica por el precio.", " pesos"),
        ("abc", "{F} Para el riesgo de atropello, ¿qué medida es de nivel más alto en la jerarquía de controles?", "Separar con barreras y señales la circulación de peatones y de máquinas", "Entregar un chaleco reflectante a cada persona", "Dar una charla breve de seguridad", "Aislar el peligro está sobre organizar el trabajo (charla) y sobre el EPP, que va al final."),
    ],
    ctx=("abc", "Un conocido ofrece pagarle a un estudiante por «medir a ojo» una partida en una obra para ahorrar la visita del ITO. ¿Qué responde?", "Agradece y explica que verificar corresponde al ITO y a personal autorizado, con registros", "Acepta si cobra menos que el ITO", "Acepta si no hay máquinas trabajando ese día", "La verificación exige autorización y evidencia; cobrar menos o la ausencia de máquinas no la reemplazan."),
    sc=[
        ("En Obras Viales: ¿qué es una partida?", "Una parte del trabajo que se mide y se paga por separado", "La partida tiene unidad, cantidad y precio en el contrato."),
        ("¿Qué tres cosas compara quien verifica una partida?", "Lo declarado, lo registrado y lo exigido", "Solo comparando las tres se detectan las diferencias."),
        ("¿Quién hace la visita a terreno de una obra vial?", "Personal autorizado, con EPP y acompañado", "Este cuaderno no habilita para intervenir obras."),
    ],
    op=("Itemizado de ejemplo de «Calle Las Acacias» (ficticia): P1 despeje, 2.000 m²; P2 base, 600 m³; P3 señalización, 8 unidades. Precios de ejemplo: P2 $19.000 por m³ y P3 $70.000 por unidad. El jefe de obra declara terminada P2, pero el libro de obra no la registra. Escribe (a) cuántos m³ suman las partidas medidas en m³, (b) el monto de P3, (c) qué haces con la declaración de P2 y a quién informas, (d) un riesgo de la obra y una medida de la jerarquía de controles.",
        "(a) Solo P2 se mide en m³: 600 m³. (b) 8 por 70.000 son 560.000 pesos. (c) No la doy por verificada; informo al ITO y pido el registro. (d) Atropello; aislar con barreras la circulación de peatones y máquinas.",
        ["distingue las unidades", "calcula el monto", "no verifica sin registro e informa al ITO", "nombra un riesgo y un nivel de control"],
        ["hoja con las cuatro respuestas"],
        ["sumar partidas con unidades distintas", "dar por verificada una partida sin registro", "proponer el EPP como primera medida"],
        "Pregunta: «¿qué evidencia falta para verificar P2?». Si no responde, pídele que relea qué compara quien verifica."),
    reinforce="Escribe tres partidas de una obra vial inventada con su unidad de medida.",
    extend="Explica por qué una partida declarada como terminada puede no estar verificada y qué documento falta.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 7 (documentos de obra de ejemplo, inventados). Obra «Calle Los Quillayes» (ficticia). Estado de pago N.º 2: antes de este período no hay avance en ninguna partida. "
     "P1 despeje: contratado 4.000 m², precio $900 por m², ejecutado en el período 1.500 m². P3 base: contratado 1.200 m³, precio $18.000 por m³, ejecutado en el período 300 m³. "
     "Libro de obra, anotación del día 12: «se ejecutan 300 m³ de base entre el Km 0+000 y el Km 0+500».")
build(
    O2, 2, F,
    use="Aprenderé el vocabulario y los documentos que se usan para verificar partidas: estado de pago, libro de obra, cantidades, precios y roles.",
    prior=["Sé qué es una partida.", "Sé multiplicar y restar.", "Sé qué hace el ITO."],
    explain=[
        "El estado de pago es el documento en que la constructora declara, para un período, qué cantidad ejecutó de cada partida y el monto que corresponde. El ITO lo revisa en nombre del mandante antes de aprobarlo. El monto de una partida se calcula como cantidad ejecutada por precio unitario. El libro de obra es el registro diario de lo que ocurre en la obra: avances, instrucciones, incidentes y decisiones, con fecha y firma.",
        "Los roles son: el jefe de obra dirige a la constructora y declara lo ejecutado; el ITO verifica y aprueba por el mandante; el proyectista aclara dudas del diseño; el laboratorista entrega los resultados de ensayo; el prevencionista de riesgos vigila la seguridad. Cada dato se respalda con un documento. Un libro de obra no se corrige borrando: una anotación nueva se hace con la fecha real.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("estado de pago", "documento en que la constructora declara lo ejecutado en un período y su monto"), ("precio unitario", "precio de cada unidad de medida de una partida"), ("cantidad ejecutada", "cantidad de una partida que ya se hizo en el período"), ("prevencionista de riesgos", "persona que vigila la seguridad de la obra"), ("jefe de obra", "persona que dirige a la constructora en la obra"), ("período", "intervalo de tiempo que cubre un estado de pago")],
    worked=[
        ("Monto del período", "En un estado de pago de ejemplo se ejecutan 80 m² de una partida cuyo precio es $2.500 por m². ¿Cuál es el monto del período?", ["Se multiplica la cantidad por el precio.", "80 por 2.500 son 200.000."], "$200.000"),
        ("Elegir el rol", "Un estado de pago de ejemplo está listo y alguien debe revisarlo por el mandante. ¿Quién lo revisa?", ["El que verifica por el mandante es el ITO.", "No es el jefe de obra, que lo prepara."], "El ITO"),
    ],
    mistakes=[("Borrar una anotación del libro de obra que estaba equivocada.", "El libro es un registro: borrar elimina evidencia.", "Haz una anotación nueva con la fecha real que aclare el error."),
              ("Pensar que el jefe de obra aprueba su propio estado de pago.", "La aprobación la hace el ITO por el mandante.", "El jefe de obra declara y el ITO verifica y aprueba.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es un estado de pago?", "El documento donde la constructora declara lo ejecutado en un período y su monto", "Un plano que muestra el camino visto desde arriba", "Un informe de laboratorio con resultados de muestras", "El estado de pago declara avance y monto; el plano y el informe cumplen otras funciones."),
        ("abc", "¿Qué es el libro de obra?", "El registro diario escrito de lo que ocurre en la obra", "La lista de precios de los materiales", "El archivo con todos los planos", "El libro registra hechos con fecha y firma; la lista de precios y los planos son otros documentos."),
        ("abc", "¿Quién revisa en nombre del mandante que lo declarado en el estado de pago coincida con lo ejecutado?", "El ITO", "El proyectista", "El laboratorista", "El ITO verifica por el mandante; el proyectista diseña y el laboratorista ensaya."),
        ("=", "{F} ¿Cuántos m² de la partida P1 quedan pendientes después de lo ejecutado en este período?", "4000-1500", "Se resta lo ejecutado a la cantidad contratada.", " m²"),
        ("abc", "{F} ¿Qué documento respalda que se ejecutaron 300 m³ de base el día 12?", "La anotación del libro de obra", "El itemizado de la obra", "El plano de planta", "El libro de obra registra lo ocurrido ese día; el itemizado solo dice lo contratado."),
        ("abc", "{F} ¿En qué unidad se mide la partida P3?", "Metros cúbicos (m³)", "Metros cuadrados (m²)", "Unidades", "La ficha da la cantidad de la base en m³, una medida de volumen."),
        ("=", "{F} ¿Cuál es el monto de la partida P1 en este estado de pago?", "1500*900", "El monto es la cantidad ejecutada por el precio unitario.", " pesos"),
        ("=", "{F} ¿Cuál es el monto total del estado de pago, sumando P1 y P3?", "1500*900+300*18000", "Se calcula el monto de cada partida y se suman.", " pesos"),
        ("ab", "{F} Un revisor dice: «P3 debe medirse en m² porque la base es una superficie». ¿Qué respuesta es correcta?", "No: el contrato mide P3 en m³, la unidad que fija el itemizado", "Sí: toda base se mide en m²", "La unidad de una partida la fija el contrato, no la forma de la obra."),
        ("abc", "{F} El estado de pago declara 350 m³ de base, pero el libro de obra registra 300 m³. ¿Qué corresponde?", "Informar la diferencia y dar por verificado solo lo que tiene respaldo", "Aprobar los 350 m³ porque los declara la constructora", "Aprobar el promedio entre 300 y 350", "Lo declarado sin respaldo no se verifica; la diferencia se informa al ITO."),
        ("ab", "{F} El jefe de obra pide agregar hoy, con la fecha del día 12, una anotación que no se hizo entonces. ¿Qué corresponde?", "No: se anota hoy con la fecha de hoy, indicando a qué día se refiere", "Sí: así el libro cuadra con el estado de pago", "Una fecha cambiada altera el registro; lo correcto es anotar con la fecha real."),
        ("=", "{F} ¿Qué porcentaje del contrato de la partida P3 se ejecutó en este período?", "300*100//1200", "Se divide lo ejecutado por lo contratado y se multiplica por 100.", " %"),
        ("abc", "{F} Para verificar P3 de punta a punta, ¿qué conjunto de documentos corresponde?", "Itemizado, especificaciones, libro de obra e informe de ensayo del material", "Solo el itemizado", "Solo el estado de pago y la firma del jefe de obra", "Se necesita lo contratado, lo exigido, lo registrado y la calidad medida, no solo lo que declara la constructora."),
    ],
    ctx=("abc", "Una estudiante de ejemplo ve en el libro de obra una anotación del día 12 con un error de cantidad. Un compañero propone borrarla con corrector. ¿Qué responde?", "Que no se borra: se hace una anotación nueva con la fecha real que aclare el error", "Que se borra si nadie lo ve", "Que se borra si el error es pequeño", "Borrar elimina evidencia; el error se corrige con una anotación nueva y fechada."),
    sc=[
        ("En Obras Viales: ¿cómo se calcula el monto de una partida?", "Cantidad ejecutada por precio unitario", "El monto combina cuánto se hizo con cuánto vale cada unidad."),
        ("¿Quién verifica por el mandante lo declarado en un estado de pago?", "El ITO", "El jefe de obra declara y el ITO verifica y aprueba."),
        ("¿Se borra una anotación errónea del libro de obra?", "No: se hace una anotación nueva con la fecha real", "El libro es un registro y borrar elimina evidencia."),
    ],
    op=("Estado de pago de ejemplo de «Calle Las Acacias» (ficticia): sin avance anterior. P2 base: contratado 600 m³, precio $19.000 por m³, ejecutado en el período 150 m³. P3 señalización: contratado 8 unidades, precio $70.000 por unidad, ejecutado 2 unidades. El libro de obra registra 120 m³ de base. Escribe (a) el monto de P2 declarado, (b) el monto de P3, (c) qué diferencia hay entre lo declarado y lo registrado en P2 y qué haces, (d) qué rol aprueba el estado de pago.",
        "(a) 150 por 19.000 son 2.850.000 pesos. (b) 2 por 70.000 son 140.000 pesos. (c) Se declaran 150 m³ y el libro registra 120: hay 30 m³ sin respaldo; informo al ITO y solo doy por verificado lo respaldado. (d) El ITO, por el mandante.",
        ["calcula el monto de P2", "calcula el monto de P3", "detecta y informa la diferencia", "nombra al ITO"],
        ["hoja con las cuatro respuestas"],
        ["aprobar lo declarado sin respaldo", "confundir cantidad con monto", "decir que el jefe de obra aprueba"],
        "Pregunta: «¿qué haces con los m³ que el libro no registra?». Si no responde, pídele que relea la regla de verificar solo lo respaldado."),
    reinforce="Escribe una frase que diga para qué sirve cada uno de estos documentos: estado de pago, libro de obra e itemizado.",
    extend="Explica por qué el jefe de obra no debería aprobar su propio estado de pago.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 8 (lista de chequeo de ejemplo, inventada). Obra «Calle Los Quillayes» (ficticia), verificación del día 20. P1 despeje: declarado 1.500 m²; libro de obra registra 1.500 m²; informe fotográfico presente. "
     "P2 movimiento de tierra: declarado 600 m³; libro de obra registra 450 m³; sin otros respaldos. P3 base: declarado 300 m³; libro de obra registra 300 m³; informe de ensayo del material presente y cumple el mínimo. "
     "P4 señalización: declarado 4 unidades; el libro de obra no tiene anotación; el itemizado fija 12 unidades en total. Precios de ejemplo: P2 $2.200 por m³ y P4 $85.000 por unidad.")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso de verificación de partidas en papel con una lista de chequeo: detectar diferencias, registrarlas e informarlas.",
    prior=["Sé qué es una partida.", "Sé qué documentos respaldan una partida.", "Sé calcular montos."],
    explain=[
        "Una lista de chequeo es una tabla con las partidas y los respaldos que cada una debe tener. Para cada partida se compara lo declarado por la constructora con lo registrado en el libro de obra y con los demás respaldos exigidos, como informes de ensayo o fotos. Si coinciden, la partida queda conforme. Si no coinciden o falta un respaldo, se anota un hallazgo, que es una diferencia o una falta detectada.",
        "Los hallazgos se registran con el nombre de la partida, lo declarado, lo respaldado, la diferencia, la fecha y quién los detectó, y se informan al ITO. Mientras no haya respaldo, esa cantidad queda observada: no se da por verificada ni se corrige el libro de obra a la medida. Si una partida requiere revisar el terreno, lo hace personal autorizado, con EPP y acompañado; este cuaderno solo trabaja los documentos.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("lista de chequeo", "tabla con las partidas y los respaldos que cada una debe tener"), ("hallazgo", "diferencia o falta detectada en la verificación"), ("conforme", "partida cuyo respaldo coincide con lo declarado"), ("observada", "cantidad que queda sin verificar hasta que haya respaldo"), ("respaldo", "documento o registro que prueba lo declarado"), ("declarado", "cantidad que informa la constructora")],
    worked=[
        ("Detectar una diferencia", "En una lista de chequeo de ejemplo se declaran 90 m² y el libro registra 70 m². ¿Cuánta cantidad queda observada?", ["Se resta lo registrado a lo declarado.", "90 menos 70 son 20."], "20 m²"),
        ("Clasificar una partida", "Otra partida de ejemplo declara 50 unidades, el libro registra 50 y hay informe de ensayo que cumple. ¿Cómo se clasifica?", ["Todo coincide y hay respaldo.", "No hay diferencia ni falta."], "Conforme"),
    ],
    mistakes=[("Dar por conforme una partida porque «seguro está hecha».", "Sin respaldo no hay verificación.", "Anota el hallazgo y deja la cantidad observada hasta que haya respaldo."),
              ("Promediar lo declarado con lo registrado.", "El promedio no corresponde a ninguna evidencia.", "Verifica solo lo registrado y deja la diferencia observada.")],
    T=[
        ("abc", "En Obras Viales: ¿qué es un hallazgo en una verificación de partidas?", "Una diferencia o una falta de respaldo detectada", "Un resultado de laboratorio que cumple", "El precio unitario de una partida", "El hallazgo es una diferencia o falta; el resultado que cumple y el precio no lo son."),
        ("abc", "¿Qué se compara en una lista de chequeo de partidas?", "Lo declarado, lo registrado y los respaldos exigidos", "Solo lo declarado por la constructora", "Solo el precio de cada partida", "Con una sola fuente no se detectan diferencias; se contrastan declarado, registro y respaldos."),
        ("abc", "Una partida declara más cantidad que la registrada. ¿Qué corresponde?", "Informar al ITO y dar por verificado solo lo respaldado", "Verificar todo lo declarado", "Corregir el libro de obra para que coincida", "La diferencia se informa; el libro no se modifica para que cuadre."),
        ("=", "{F} ¿Cuántos m³ de diferencia hay en P2 entre lo declarado y lo registrado en el libro?", "600-450", "Se resta lo registrado a lo declarado.", " m³"),
        ("abc", "{F} ¿Qué partidas coinciden entre lo declarado y lo registrado y tienen su respaldo?", "P1 y P3", "P1 y P2", "P3 y P4", "P2 tiene diferencia y P4 no tiene registro; solo P1 y P3 coinciden."),
        ("abc", "{F} ¿Qué hallazgo corresponde anotar para P4?", "No hay anotación en el libro que respalde las 4 unidades declaradas", "Hay una diferencia de 8 unidades entre lo declarado y lo registrado", "No hay hallazgo porque 4 es menor que 12", "El libro no registra nada de P4; 12 es el total del contrato y no lo registrado."),
        ("=", "{F} ¿Cuánto vale la diferencia de P2 con el precio de ejemplo?", "(600-450)*2200", "Se calcula la diferencia en m³ y se multiplica por el precio por m³.", " pesos"),
        ("=", "{F} ¿Qué porcentaje de las 4 partidas coincide con su respaldo?", "2*100//4", "Coinciden 2 de 4 partidas: se divide entre 4 y se multiplica por 100.", " %"),
        ("abc", "{F} El jefe de obra asegura que las 4 unidades de P4 «ya están instaladas, solo falta anotarlas». ¿Qué corresponde?", "Dejar las 4 unidades observadas hasta que exista el registro y que el ITO decida", "Verificarlas porque el jefe de obra lo asegura", "Anotarlas el ITO en el libro con la fecha de ayer", "La verificación exige respaldo; no se completa el libro con fechas distintas de las reales."),
        ("ab", "{F} Un compañero propone verificar P2 por el promedio entre lo declarado y lo registrado. ¿Qué respuesta es correcta?", "No: se verifica solo lo registrado y la diferencia queda observada", "Sí: el promedio reparte la diferencia de forma justa", "El promedio no corresponde a ninguna evidencia; solo vale lo que tiene respaldo."),
        ("abc", "{F} El informe fotográfico de P1 no tiene fecha. ¿Qué corresponde?", "Pedir la fecha al responsable del informe antes de darlo por válido", "Escribir la fecha de hoy en el informe", "Usarlo igual, porque las fotos son claras", "Un respaldo sin fecha no se puede ubicar en el tiempo; se aclara con quien lo preparó."),
        ("=", "{F} ¿Cuánto suman, en pesos, las cantidades sin respaldo de P2 y de P4?", "150*2200+4*85000", "Se calcula el monto sin respaldo de P2 y el de P4 y se suman.", " pesos"),
        ("abc", "{F} Terminada la lista, ¿qué orden de acciones es correcto?", "Registrar los hallazgos, informarlos al ITO y esperar su decisión", "Pagar todo lo declarado y revisar después", "Corregir el libro de obra y luego informar", "Primero se registra y se informa; la decisión la toma el ITO y los registros no se modifican."),
    ],
    ctx=("abc", "Una estudiante de ejemplo ayuda a completar una lista de chequeo y nota que una partida no tiene respaldo. El jefe de obra le dice que «lo deje pasar esta vez». ¿Qué hace?", "Anota el hallazgo y lo informa al ITO", "Lo deja pasar si es solo esta vez", "Lo deja pasar si el jefe de obra lo firma", "Un hallazgo no se omite por pedido de quien declara; se registra e informa."),
    sc=[
        ("En Obras Viales: ¿qué es una lista de chequeo?", "Una tabla con las partidas y los respaldos que cada una debe tener", "La lista ordena la revisión partida por partida."),
        ("¿Qué se hace con una cantidad declarada sin respaldo?", "Queda observada y se informa al ITO", "No se verifica ni se oculta; se informa."),
        ("¿Se corrige el libro de obra para que cuadre con lo declarado?", "No, el libro se mantiene y la diferencia se informa", "Modificar el registro elimina la evidencia que sirve para verificar."),
    ],
    op=("Lista de chequeo de ejemplo de «Calle Las Acacias» (ficticia). P1 despeje: declarado 800 m², libro 800 m², fotos presentes. P2 base: declarado 200 m³, libro 150 m³, sin informe de ensayo. P3 señalización: declarado 3 unidades, libro sin anotación. Precio de ejemplo de P2: $19.000 por m³. Escribe (a) qué partida queda conforme, (b) la diferencia de P2 en m³ y su valor, (c) qué hallazgos registras y a quién los informas, (d) qué respaldo falta en P2 además de la diferencia.",
        "(a) P1. (b) 200-150 son 50 m³, y 50 por 19.000 son 950.000 pesos. (c) P2: 50 m³ sin registro y sin informe de ensayo; P3: sin anotación en el libro; los informo al ITO. (d) El informe de ensayo del material.",
        ["identifica la partida conforme", "calcula la diferencia y su valor", "registra los hallazgos e informa al ITO", "nombra el respaldo que falta"],
        ["hoja con las cuatro respuestas"],
        ["verificar lo declarado sin respaldo", "no informar los hallazgos", "olvidar el informe de ensayo"],
        "Pregunta: «¿qué haces con lo que no tiene registro?». Si no responde, pídele que relea qué significa que una cantidad quede observada."),
    reinforce="Inventa una lista de chequeo de tres partidas, con una conforme y dos con hallazgo, y escribe qué informarías.",
    extend="Explica por qué es importante registrar los hallazgos con fecha y con el nombre de quien los detectó.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 9 (planilla de avance de ejemplo, inventada). Obra «Calle Los Naranjos» (ficticia). P1 despeje: contratado 6.000 m², acumulado anterior 1.000 m², ejecutado en el período 1.500 m², precio $800 por m². "
     "P3 base: contratado 1.200 m³, acumulado anterior 400 m³, ejecutado en el período 200 m³, precio $20.000 por m³; rendimiento de ejemplo 40 m³ por día. "
     "P4 señalización: contratado 10 unidades, acumulado anterior 0, ejecutado en el período 4, precio $90.000 por unidad.")
build(
    O2, 4, F,
    use="Aprenderé a calcular avance físico, saldos, montos y días de trabajo con datos de ejemplo para verificar las partidas de una obra.",
    prior=["Sé qué es una partida.", "Sé calcular montos.", "Sé calcular porcentajes."],
    explain=[
        "El acumulado de una partida es la suma de lo ejecutado en los períodos anteriores y en el período actual. El avance físico es el porcentaje que representa el acumulado respecto de lo contratado: acumulado dividido por contratado, por 100. El saldo es lo que falta por ejecutar: contratado menos acumulado. El monto del período es la cantidad del período por el precio unitario.",
        "El rendimiento es la cantidad que se ejecuta por unidad de tiempo; en este cuaderno es un dato de ejemplo para programar y no un valor real. Con él se estima el tiempo: días = cantidad dividida por rendimiento. Estos cálculos permiten detectar declaraciones que no cuadran, pero la decisión la toma el ITO con los registros. Todo se calcula en papel con números de ejemplo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("acumulado", "suma de lo ejecutado en períodos anteriores y en el actual"), ("avance físico", "porcentaje del contrato ya ejecutado"), ("saldo", "cantidad que falta por ejecutar"), ("rendimiento", "cantidad que se ejecuta por día u hora, dato de ejemplo para programar"), ("monto del período", "cantidad del período por el precio unitario"), ("contratado", "cantidad total fijada en el contrato")],
    worked=[
        ("Avance físico", "Una partida de ejemplo contratada en 400 m² lleva un acumulado de 100 m². ¿Qué avance físico tiene?", ["Se divide el acumulado por lo contratado.", "100 entre 400 es una cuarta parte: 25 por ciento."], "25 %"),
        ("Días de trabajo", "A una partida de ejemplo le faltan 90 m² y su rendimiento es de 30 m² por día. ¿Cuántos días se estiman?", ["Se divide el saldo por el rendimiento.", "90 entre 30 son 3."], "3 días"),
    ],
    mistakes=[("Calcular el avance físico con lo del período en vez de con el acumulado.", "El avance físico cuenta todo lo ejecutado hasta la fecha.", "Suma el acumulado anterior y el período antes de dividir."),
              ("Dividir el contratado por lo ejecutado.", "Eso da cuántas veces cabe lo ejecutado, no el porcentaje de avance.", "Divide lo ejecutado por lo contratado y multiplica por 100.")],
    T=[
        ("abc", "En Obras Viales: ¿cómo se calcula el avance físico de una partida?", "Acumulado dividido por contratado, por 100", "Cantidad del período multiplicada por el precio", "Contratado dividido por acumulado", "El avance es un porcentaje del contrato ejecutado; multiplicar por el precio da un monto."),
        ("abc", "¿Qué es el acumulado de una partida?", "Lo ejecutado en períodos anteriores más lo del período actual", "Solo lo ejecutado en el período actual", "La cantidad contratada", "El acumulado reúne todo lo ejecutado hasta la fecha."),
        ("abc", "En una planilla de ejemplo, ¿qué es el rendimiento?", "La cantidad que se ejecuta por día u hora", "El precio de cada unidad", "La cantidad total contratada", "El rendimiento relaciona cantidad con tiempo y sirve para estimar días."),
        ("=", "{F} ¿Cuál es el acumulado de la partida P1 después de este período?", "1000+1500", "Se suman el acumulado anterior y lo ejecutado en el período.", " m²"),
        ("=", "{F} ¿Cuántos m² de P1 faltan por ejecutar después de este período?", "6000-(1000+1500)", "El saldo es lo contratado menos el acumulado.", " m²"),
        ("=", "{F} ¿Cuál es el monto del período de la partida P4?", "4*90000", "El monto se calcula con la cantidad del período por el precio unitario.", " pesos"),
        ("=", "{F} ¿Qué avance físico, en porcentaje, tiene la partida P3 después de este período?", "(400+200)*100//1200", "Se suma el acumulado anterior y el período, se divide por lo contratado y se multiplica por 100.", " %"),
        ("=", "{F} Con el rendimiento de ejemplo, ¿cuántos días se estiman para ejecutar el saldo de P3?", "(1200-400-200)//40", "Se calcula el saldo y se divide por el rendimiento diario.", " días"),
        ("=", "{F} ¿Qué avance físico, en porcentaje, tiene P4 después de este período?", "4*100//10", "Se divide lo ejecutado por lo contratado y se multiplica por 100.", " %"),
        ("ab", "{F} Un compañero calcula el avance de P3 con solo los 200 m³ del período (200 de 1.200). ¿Qué respuesta es correcta?", "No: el avance físico usa el acumulado, es decir, lo anterior más el período", "Sí: el avance físico se calcula solo con el período", "El avance físico cuenta todo lo ejecutado hasta la fecha, no únicamente un período."),
        ("abc", "{F} Si el rendimiento de ejemplo de P3 bajara a 30 m³ por día, ¿qué pasaría con los días para el saldo?", "Aumentarían, porque se ejecutaría menos por día para el mismo saldo", "Disminuirían, porque el rendimiento es un número menor", "No cambiarían, porque el saldo es el mismo", "Con el mismo saldo y menos cantidad por día se necesitan más días."),
        ("=", "{F} ¿Cuál es el monto acumulado de P3 hasta la fecha, con el precio de ejemplo?", "(400+200)*20000", "Se suma el acumulado y se multiplica por el precio unitario.", " pesos"),
        ("abc", "{F} La constructora declara los 1.500 m² de P1 como ejecutados en 5 días de trabajo, y se sabe que el rendimiento de ejemplo de P1 es de 200 m² por día. ¿Qué corresponde?", "Aclarar la diferencia con el jefe de obra y los registros, porque lo declarado supera lo estimado para 5 días", "Aceptarlo, porque siempre se puede trabajar más rápido", "Reducir la cantidad en el estado de pago sin avisar", "Con 5 días y 200 m² por día se estiman 1.000 m²; la diferencia con 1.500 se revisa con evidencia."),
    ],
    ctx=("abc", "Un estudiante de ejemplo prepara una planilla para el ITO y nota que un avance físico le da 105 % en una partida. ¿Qué hace?", "Revisa los datos y los cálculos, y si el resultado se mantiene informa al ITO", "Lo deja en 100 % sin avisar", "Lo borra de la planilla", "Un avance sobre 100 % indica un error o una declaración excesiva; se revisa e informa, no se oculta."),
    sc=[
        ("En Obras Viales: ¿cómo se calcula el saldo de una partida?", "Contratado menos acumulado", "El saldo es lo que falta para llegar a lo contratado."),
        ("¿Cómo se calcula el avance físico?", "Acumulado dividido por contratado, por 100", "Se compara todo lo ejecutado con lo contratado."),
        ("¿Cómo se estiman los días de un trabajo con un rendimiento de ejemplo?", "Cantidad dividida por rendimiento", "El rendimiento relaciona cantidad por día."),
    ],
    op=("Planilla de ejemplo de «Calle Las Acacias» (ficticia). P2 base: contratado 600 m³, acumulado anterior 100 m³, período 200 m³, precio $19.000 por m³, rendimiento de ejemplo 50 m³ por día. P3 señalización: contratado 8 unidades, acumulado anterior 2, período 2, precio $70.000 por unidad. Escribe (a) el avance físico de P2, (b) el saldo de P2 y los días estimados para ejecutarlo, (c) el monto del período de P3, (d) qué haces si una partida da más de 100 % de avance.",
        "(a) Acumulado 300 m³ de 600: 50 %. (b) Saldo 300 m³; 300 entre 50 son 6 días. (c) 2 por 70.000 son 140.000 pesos. (d) Reviso datos y cálculos y, si se mantiene, informo al ITO.",
        ["calcula el avance con el acumulado", "calcula saldo y días", "calcula el monto del período", "informa una inconsistencia"],
        ["hoja con las cuatro respuestas"],
        ["usar solo el período para el avance", "no restar el acumulado en el saldo", "ocultar un avance mayor que 100 %"],
        "Pregunta: «¿qué cantidad usaste para el avance, la del período o el acumulado?». Si no responde, pídele que relea la definición de avance físico."),
    reinforce="Inventa una partida con contratado, acumulado y período, y calcula su avance físico y su saldo.",
    extend="Explica por qué el rendimiento de ejemplo sirve para detectar declaraciones dudosas, pero no para decidir solo.",
)
