"""Tripulación de Naves Mercantes y Especiales TP 3.º y 4.º medio: OAE-01 (leer e informar datos de instrumentos y equipos) y OAE-02 (asistir sistemas de la máquina propulsora y auxiliares). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_trnm_common import AVISO, EMER, build

O1 = "TP-TRNM-3y4-OAE-01"
O2 = "TP-TRNM-3y4-OAE-02"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Nave Demo» es una nave mercante ficticia de carga general. Su tripulación de 21 personas se reparte así: 4 en el puente, 8 en el área de cubierta, 6 en el área de máquinas y 3 en servicios. "
     "Trabaja con guardias de 4 horas. Peligros anotados: ruido en la sala de máquinas, superficies resbaladizas en cubierta, cabos tensos y partes giratorias de los equipos.")
build(
    O1, 1, F,
    use="Aprenderé qué es una nave mercante, cómo se reparten sus áreas, por qué hay que leer e informar datos de instrumentos y cómo se ordenan las medidas de prevención a bordo.",
    prior=["Sé leer una ficha escrita y una tabla simple.", "Sé sumar, restar, multiplicar y dividir números enteros.", "Sé que una nave se desplaza por el mar."],
    explain=[
        "Una nave mercante es una nave que transporta carga o pasajeros por mar con fines comerciales. A bordo el trabajo se reparte en áreas: el puente es el lugar desde donde se conduce la nave, la cubierta es la superficie exterior con sus equipos de maniobra, y el área de máquinas es donde están el motor principal y los equipos auxiliares. Un instrumento es un aparato que mide o indica un dato, como la velocidad, la profundidad o la temperatura. Leer un instrumento es anotar su valor con su unidad, y informar es comunicar ese dato, con lenguaje técnico claro, a la persona que está al mando, el oficial a cargo.",
        "En una nave hay peligros, que son fuentes de daño, y riesgos, que son la posibilidad de que ese daño ocurra. Las medidas de prevención se ordenan en la jerarquía de controles, de la más a la menos efectiva: eliminar el peligro, sustituirlo, usar controles de ingeniería (cambios físicos del lugar), usar controles administrativos (reglas, letreros y capacitación) y, al final, el equipo de protección personal (EPP), que protege solo a quien lo usa y no quita el peligro. Un ejemplo de otra nave: un piso con aceite derramado es un peligro, y que alguien resbale es el riesgo.",
        f"La guardia es el turno de vigilancia que cumple una parte de la tripulación. Los protocolos y la norma vigente de la autoridad marítima fijan cómo se trabaja en cada área. {EMER} {AVISO}",
    ],
    vocab=[("nave mercante", "nave que transporta carga o pasajeros con fines comerciales"), ("puente", "lugar de la nave desde donde se conduce"), ("cubierta", "superficie exterior de la nave, con sus equipos de maniobra"), ("área de máquinas", "zona donde están el motor principal y los equipos auxiliares"), ("instrumento", "aparato que mide o indica un dato"), ("guardia", "turno de vigilancia de una parte de la tripulación"), ("oficial a cargo", "persona que está al mando de una guardia y recibe los informes"), ("jerarquía de controles", "orden de las medidas de prevención, de la más a la menos efectiva"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Peligro y riesgo", "En una nave de ejemplo hay una escotilla abierta junto a un pasillo estrecho. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la abertura, porque puede causar daño.", "El riesgo es que alguien caiga por ella al pasar."], "Peligro: la escotilla abierta; riesgo: que una persona caiga por ella"),
        ("Clasificar un control", "Una naviera de ejemplo entrega tapones para los oídos a quienes entran a un sector ruidoso. ¿A qué nivel de la jerarquía corresponde?", ["Los tapones se llevan puestos y protegen a cada persona.", "Lo que se usa sobre el cuerpo para protegerse es un equipo de protección personal."], "Equipo de protección personal (EPP)"),
    ],
    mistakes=[("Creer que usar casco y calzado basta para estar seguro en cualquier área de la nave.", "El EPP es la última barrera: no quita el peligro y protege solo a quien lo usa.", "Primero se elimina o se controla el peligro; el EPP se suma a esas medidas."),
              ("Creer que saber leer un instrumento permite corregir el equipo por cuenta propia.", "Leer e informar es una tarea distinta de operar o ajustar un equipo, que exige autorización.", "Anota el dato, infórmalo al oficial a cargo y no intervengas el equipo.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es el área de máquinas de una nave mercante?", "La zona donde están el motor principal y los equipos auxiliares", "El lugar desde donde se conduce la nave y se ve el horizonte", "La superficie exterior donde están los equipos de maniobra", "El área de máquinas aloja motores y equipos; el puente conduce y la cubierta es la superficie exterior."),
        ("abc", "En Tripulación de Naves: ¿qué es una guardia?", "El turno de vigilancia que cumple una parte de la tripulación", "El libro donde se anotan los repuestos de la nave", "El permiso que la autoridad entrega a la nave para zarpar", "La guardia es un turno de vigilancia; los repuestos y los permisos se registran en otros documentos."),
        ("abc", "{F} Una regla escrita que prohíbe detenerse en la zona donde los cabos están tensos es un control de tipo:", "Administrativo, porque es una regla que ordena la conducta", "De ingeniería, porque cambia físicamente el lugar", "De eliminación, porque quita los cabos de la nave", "Una regla solo ordena la conducta; no cambia el lugar ni quita el peligro."),
        ("=", "{F} ¿Cuántas personas de la tripulación trabajan entre el área de cubierta y el área de máquinas?", "8+6", "Se suman las personas de cubierta y las de máquinas que indica la ficha.", " personas"),
        ("abc", "{F} ¿Cuál es el riesgo asociado al ruido en la sala de máquinas?", "Daño al oído de quien está expuesto sin protección", "Que el motor consuma más combustible del previsto", "Que las lecturas se anoten con retraso", "El riesgo es un daño para las personas; el consumo y los retrasos no lo son."),
        ("abc", "En Tripulación de Naves: ¿por qué un tripulante en formación informa un dato extraño al oficial a cargo en lugar de corregirlo él mismo?", "Porque el oficial decide con la información completa y solo personal autorizado interviene los equipos", "Porque corregirlo es más lento que informarlo", "Porque el oficial prefiere no recibir datos cuando todo parece normal", "Informar mantiene la cadena de mando; intervenir sin autorización puede causar otro problema."),
        ("=", "{F} ¿Cuántas guardias de 4 horas completan un día de 24 horas?", "24//4", "Se divide la duración del día entre la duración de cada guardia.", " guardias"),
        ("=", "En una ronda de ejemplo se leen 5 instrumentos de cubierta y 7 de máquinas cada 2 horas. ¿Cuántas lecturas se hacen en 24 horas?", "(5+7)*(24//2)", "Se suman las lecturas de una ronda y se multiplican por el número de rondas del día.", " lecturas"),
        ("abc", "{F} En cubierta hay superficies resbaladizas. ¿Cuál medida es de nivel más efectivo en la jerarquía de controles?", "Instalar una superficie antideslizante fija en la zona", "Colocar un letrero que avise «piso resbaladizo»", "Entregar calzado de seguridad a cada persona", "Cambiar la superficie quita el problema en el lugar; el letrero es administrativo y el calzado es EPP."),
        ("abc", "{F} Un compañero dice: «con casco y calzado puestos ya no necesito cumplir las reglas de cubierta». ¿Qué respuesta es correcta?", "Es falso: el EPP es la última barrera y no quita el peligro", "Es cierto, porque el EPP es la medida más efectiva", "Es cierto, si las reglas son solo letreros", "El EPP protege solo a quien lo usa y no reemplaza las otras medidas."),
        ("abc", "Durante una visita de ejemplo a una nave, una persona cae al agua desde la pasarela. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo ni entrar al agua, dar la alarma y avisar a un adulto responsable y a emergencias", "Acercarte al borde y estirar un cabo con tus manos", "Lanzarte al agua a ayudarla, porque sabes nadar", "Intervenir sin formación puede causar otro accidente; se da la alarma y se avisa."),
        ("=", "{F} Cada persona del área de cubierta de la ficha entrega 2 informes de lectura por día. ¿Cuántos informes entrega toda el área en 5 días?", "8*2*5", "Se multiplican las personas por los informes diarios y por los días.", " informes"),
        ("abc", "El oficial a cargo te pide informar cualquier lectura fuera de lo usual. Ves una lectura rara en un equipo de ejemplo. ¿Qué corresponde?", "Anotar instrumento, valor, unidad y hora, e informarlo al oficial sin intervenir el equipo", "Ajustar el equipo hasta que la lectura se vea normal", "Esperar a la siguiente guardia por si se arregla sola", "Informar con datos completos permite decidir; ajustar o esperar son conductas inseguras."),
    ],
    ctx=("abc", "Un conocido que trabaja en un buque te propone subir a la sala de máquinas para «ayudar a revisar los equipos» porque «es fácil». ¿Qué respondes?", "Que no, porque trabajar en una nave exige instructor autorizado, norma vigente y elementos de protección, y que lo consultarás con un adulto responsable", "Que sí, si te presta un casco", "Que sí, pero solo si no hay nadie más a bordo", "Un casco no reemplaza la autorización ni la formación; ir sin que nadie lo sepa es más peligroso."),
    sc=[
        ("En Tripulación de Naves: ¿qué es un riesgo?", "La posibilidad de que un peligro cause daño", "El riesgo es la posibilidad de daño; el peligro es la fuente."),
        ("A bordo: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
        ("En Tripulación de Naves: ¿a quién se informa una lectura fuera de lo usual?", "Al oficial a cargo de la guardia", "El oficial a cargo decide qué hacer con el dato informado."),
    ],
    op=("En la «Nave Demo» (caso de ejemplo) una escotilla del pasillo de máquinas queda abierta durante la guardia. Peligros anotados: la abertura y poca iluminación en el pasillo. Escribe (a) cuál es el peligro y cuál el riesgo asociado, (b) un control administrativo para ese pasillo, (c) un control de ingeniería para el mismo pasillo, (d) por qué el EPP no basta y quién realiza la tarea.",
        "(a) Peligro: la escotilla abierta en un pasillo poco iluminado; riesgo: que una persona caiga por la abertura. (b) Un letrero de aviso y una regla que obligue a mantener la escotilla cerrada cuando no se usa. (c) Una baranda o tapa fija que impida caer por la abertura. (d) Porque el EPP es la última barrera: no quita el peligro y protege solo a quien lo usa. La tarea la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer el EPP como único control", "no aclarar que la tarea la hace personal autorizado"],
        "Pregunta: «¿qué control cambia el lugar y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el nivel de ingeniería."),
    reinforce="Escribe la jerarquía de controles en orden y pon junto a cada nivel un ejemplo inventado de una nave mercante.",
    extend="Explica con un ejemplo por qué leer e informar bien un dato también ayuda a prevenir accidentes a bordo.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (tablero de ejemplo, inventado). Lecturas de la «Nave Demo»: compás, rumbo 090°; corredera (mide la velocidad), 12 nudos; ecosonda (mide la profundidad bajo la nave), 48 m; anemómetro (mide el viento), 20 nudos; "
     "termómetro del agua de enfriamiento, 70 °C; manómetro del aceite, 4 bar; tacómetro del motor, 600 rpm; indicador del tanque de combustible, 60 % de un tanque de 40 m³.")
build(
    O1, 2, F,
    use="Aprenderé qué mide cada instrumento común de cubierta y de máquinas, en qué unidad se informa y cómo se lee un dato con lenguaje técnico.",
    prior=["Sé qué es un instrumento y por qué se informa a un oficial.", "Sé calcular con enteros y porcentajes simples.", "Sé que un ángulo se mide en grados."],
    explain=[
        "Cada instrumento mide un dato y se informa con su unidad. El compás indica el rumbo, que es la dirección hacia la que apunta la proa y se mide en grados desde el norte: 000° es norte, 090° es este, 180° es sur y 270° es oeste. La corredera mide la velocidad en nudos: un nudo es una milla náutica por hora, y la milla náutica es la unidad de distancia que se usa en el mar. La ecosonda mide la profundidad bajo la nave en metros. El anemómetro mide la velocidad del viento.",
        "En el área de máquinas el termómetro mide la temperatura en grados Celsius (°C), el manómetro mide la presión (por ejemplo en bar), el tacómetro cuenta las revoluciones por minuto (rpm) de un eje y el indicador de nivel muestra cuánto contiene un tanque, a menudo en porcentaje. La distancia recorrida se calcula con distancia = velocidad × tiempo: una nave de ejemplo que navega a 8 nudos durante 3 horas recorre 24 millas náuticas.",
        f"Un dato sin unidad no sirve: «48» puede ser metros, bar o grados. Informar es decir instrumento, valor y unidad. No se toca ni se ajusta ningún equipo para leerlo. {EMER} {AVISO}",
    ],
    vocab=[("rumbo", "dirección hacia la que apunta la proa, en grados desde el norte"), ("nudo", "una milla náutica por hora"), ("milla náutica", "unidad de distancia que se usa en el mar"), ("ecosonda", "instrumento que mide la profundidad bajo la nave"), ("manómetro", "instrumento que mide la presión"), ("tacómetro", "instrumento que cuenta las revoluciones por minuto"), ("rpm", "revoluciones por minuto"), ("bar", "unidad de presión")],
    worked=[
        ("Recorrido en millas", "Una nave de ejemplo navega a 10 nudos durante 4 horas. ¿Cuántas millas náuticas recorre?", ["Se usa distancia = velocidad × tiempo.", "Se multiplican 10 nudos por 4 horas."], "40 millas náuticas"),
        ("Leer un rumbo", "En otra nave de ejemplo el compás marca 180°. ¿Hacia qué punto cardinal apunta la proa?", ["000° es norte y 180° está a la mitad de la vuelta.", "La mitad de la vuelta desde el norte apunta al sur."], "Hacia el sur"),
    ],
    mistakes=[("Informar un valor sin unidad, por ejemplo «48».", "Sin unidad no se sabe si son metros, bar o grados, y el dato puede interpretarse mal.", "Informa siempre instrumento, valor y unidad."),
              ("Confundir nudos con kilómetros por hora o con metros.", "El nudo es una milla náutica por hora y no es una unidad de profundidad ni de distancia.", "Usa nudos solo para velocidad en el mar y millas náuticas para distancia.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué mide la ecosonda de una nave?", "La profundidad bajo la nave", "La velocidad de la nave sobre el agua", "La dirección hacia la que apunta la proa", "La ecosonda mide profundidad; la velocidad la mide la corredera y el rumbo, el compás."),
        ("abc", "En Tripulación de Naves: ¿en qué unidad informa su dato un tacómetro?", "En revoluciones por minuto (rpm)", "En grados Celsius", "En nudos", "El tacómetro cuenta vueltas por minuto; los grados Celsius y los nudos miden otras cosas."),
        ("abc", "{F} ¿Qué instrumento de la ficha informa la dirección hacia la que apunta la proa?", "El compás", "La corredera", "El anemómetro", "El compás da el rumbo; la corredera da la velocidad y el anemómetro, el viento."),
        ("abc", "{F} ¿Qué instrumento informa la presión del aceite y en qué unidad lo hace?", "El manómetro, en bar", "El termómetro, en grados Celsius", "El tacómetro, en rpm", "El manómetro mide presión y en la ficha usa bar."),
        ("=", "{F} Si la nave mantiene la velocidad de la ficha durante 5 horas, ¿cuántas millas náuticas recorre?", "12*5", "Se multiplica la velocidad en nudos por las horas de navegación.", " millas"),
        ("abc", "{F} El rumbo de la ficha es 090°. ¿Hacia qué punto cardinal apunta la proa?", "Hacia el este", "Hacia el norte", "Hacia el oeste", "090° está a un cuarto de vuelta desde el norte hacia la derecha, es decir, el este."),
        ("=", "{F} ¿Cuántos metros cúbicos de combustible quedan en el tanque, según el indicador?", "40*60//100", "Se calcula el 60 % de la capacidad total del tanque.", " m³"),
        ("=", "{F} Si el eje del motor mantiene el valor del tacómetro durante 10 minutos, ¿cuántas revoluciones da?", "600*10", "Se multiplican las revoluciones por minuto por los minutos.", " revoluciones"),
        ("abc", "{F} ¿Cuál lectura está expresada con una unidad coherente con su instrumento?", "Profundidad 48 m", "Profundidad 48 nudos", "Profundidad 48 bar", "La ecosonda mide profundidad en metros; nudos es velocidad y bar es presión."),
        ("abc", "{F} Para saber cuántas millas recorre la nave en cierto tiempo, además de la velocidad de la corredera, ¿qué dato se necesita?", "El tiempo de navegación en horas", "El rumbo del compás", "La profundidad de la ecosonda", "La distancia se calcula multiplicando velocidad por tiempo; el rumbo y la profundidad no entran en esa cuenta."),
        ("abc", "Un instrumento de ejemplo marca un valor que no entiendes durante una visita guiada. ¿Qué corresponde?", "Preguntar a la persona autorizada a cargo, sin tocar ningún equipo", "Presionar los botones del equipo hasta que cambie el valor", "Anotar un valor distinto que te parezca más razonable", "Leer no autoriza a tocar ni a inventar datos; se pregunta a quien está autorizado."),
        ("=", "{F} Si el consumo de ejemplo es de 3 m³ de combustible por hora, ¿cuántas horas alcanza el combustible que hay en el tanque de la ficha?", "40*60//100//3", "Se calcula el combustible disponible y se divide por el consumo por hora.", " horas"),
        ("=", "{F} Si la nave mantiene la velocidad de la ficha durante 2 horas y media, ¿cuántas millas náuticas recorre?", "12*150//60", "Se pasan 2 horas y media a 150 minutos y se calcula la distancia proporcional a la hora.", " millas"),
    ],
    ctx=("abc", "Una persona mayor de la tripulación de ejemplo te dice: «la aguja del manómetro marca 5 bar, pero anota 4 para que no haya problemas con el oficial». ¿Qué respondes?", "Que se debe anotar el valor que marca el instrumento e informar al oficial", "Que anotas 4 porque ella tiene más experiencia", "Que anotas 4 en lápiz para borrarlo después", "Alterar un dato oculta información real; se anota lo leído y se informa."),
    sc=[
        ("En Tripulación de Naves: ¿qué mide la corredera?", "La velocidad de la nave", "La corredera indica la velocidad, que se informa en nudos."),
        ("¿Qué es un nudo?", "Una milla náutica por hora", "El nudo es la unidad de velocidad en el mar."),
        ("¿Qué tres datos componen un informe de lectura?", "Instrumento, valor y unidad", "Sin esos tres datos la lectura puede interpretarse mal."),
    ],
    op=("Tablero de ejemplo de la «Nave Ejemplo»: ecosonda 30 m; corredera 9 nudos; compás 270°; tacómetro 450 rpm; indicador de un tanque de 20 m³ en 50 %. Escribe (a) hacia qué punto cardinal apunta la proa, (b) cuántas millas náuticas recorre en 4 horas, (c) cuántos m³ hay en el tanque, (d) cómo informarías la lectura de la ecosonda con todos sus datos.",
        "(a) Hacia el oeste. (b) 9 × 4 = 36 millas náuticas. (c) 20 × 50 ÷ 100 = 10 m³. (d) «Ecosonda: profundidad bajo la nave, 30 m», agregando la hora de la lectura.",
        ["identifica el punto cardinal del rumbo", "calcula la distancia con velocidad y tiempo", "calcula el porcentaje del tanque", "informa con instrumento, valor y unidad"],
        ["hoja con cuatro respuestas"],
        ["olvidar la unidad", "confundir nudos con metros", "usar el tiempo en minutos sin convertirlo"],
        "Pregunta: «¿qué unidad corresponde a este instrumento?». Si no responde, pídele que relea la lista del vocabulario."),
    reinforce="Haz una tabla con cinco instrumentos, lo que mide cada uno y su unidad.",
    extend="Explica con un ejemplo inventado por qué una lectura sin unidad puede llevar a un error de interpretación.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (planilla de ronda de ejemplo, inventada). Rango normal de la planilla: temperatura del agua de enfriamiento de 60 a 80 °C; presión del aceite de 3 a 5 bar; velocidad del motor de 550 a 650 rpm. "
     "Ronda de las 10:00: temperatura 85 °C, presión 4 bar, velocidad 600 rpm. Ronda de las 12:00: temperatura 78 °C, presión 2 bar, velocidad 610 rpm.")
build(
    O1, 3, F,
    use="Aprenderé a comparar una lectura con el rango de una planilla, a detectar valores fuera de rango y a informarlos con todos sus datos.",
    prior=["Sé qué mide cada instrumento y en qué unidad se informa.", "Sé restar números enteros.", "Sé leer una planilla de dos columnas."],
    explain=[
        "Una planilla de ronda es una hoja donde se anotan, a horas fijas, las lecturas de varios instrumentos. Cada instrumento tiene un rango normal, que es el intervalo entre un valor mínimo y un valor máximo dentro del cual la lectura se considera esperable. Una lectura está fuera de rango si queda por debajo del mínimo o por encima del máximo. En una nave de ejemplo, si el rango de una temperatura es de 40 a 60 °C y la lectura es 65 °C, está 5 °C sobre el máximo.",
        "Estar fuera de rango no prueba que haya una falla: puede ser el equipo o puede ser el instrumento. Por eso el dato se anota tal cual y se informa de inmediato al oficial a cargo, junto con la hora, el instrumento, el valor, la unidad y el rango. También se mira la tendencia, es decir, si el valor sube, baja o se mantiene respecto de la ronda anterior.",
        f"La persona que lee no ajusta el equipo ni modifica la planilla para que «cuadre»: solo personal autorizado decide qué hacer. {EMER} {AVISO}",
    ],
    vocab=[("planilla de ronda", "hoja donde se anotan lecturas de instrumentos a horas fijas"), ("rango normal", "intervalo entre un valor mínimo y uno máximo considerados esperables"), ("fuera de rango", "lectura por debajo del mínimo o por encima del máximo del rango"), ("tendencia", "si un valor sube, baja o se mantiene entre lecturas"), ("lectura", "valor que muestra un instrumento en un momento")],
    worked=[
        ("Detectar un fuera de rango", "En una planilla de ejemplo el rango de una presión es de 2 a 6 bar y la lectura es 7 bar. ¿Está dentro del rango? ¿Cuánto se pasa?", ["El máximo del rango es 6 bar y la lectura es 7 bar.", "Se resta 7 − 6."], "Está fuera de rango, 1 bar sobre el máximo"),
        ("Tendencia", "En una planilla de ejemplo una temperatura fue 50 °C a las 08:00 y 56 °C a las 10:00. ¿Cuál es la tendencia?", ["El valor de las 10:00 es mayor que el de las 08:00.", "Un valor que aumenta entre rondas tiene tendencia a subir."], "Tendencia a subir, 6 °C en dos horas"),
    ],
    mistakes=[("Pensar que una lectura dentro del rango en un instrumento permite no informar la lectura fuera de rango de otro.", "Cada instrumento se evalúa por separado y un valor fuera de rango debe informarse aunque los demás estén normales.", "Revisa todos los instrumentos de la ronda y reporta cada valor fuera de rango."),
              ("Cambiar el valor de la planilla para que quede dentro del rango.", "Modificar una lectura oculta información real y puede ocultar una falla.", "Anota lo que marca el instrumento e informa al oficial.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es el rango normal de un instrumento?", "El intervalo entre un valor mínimo y uno máximo considerado esperable", "El valor exacto que siempre debe marcar el instrumento", "La unidad en la que se informa el dato", "El rango es un intervalo con mínimo y máximo, no un valor único ni una unidad."),
        ("abc", "{F} ¿Qué lectura de la ronda de las 10:00 está fuera de rango?", "La temperatura, 85 °C, porque supera el máximo de 80 °C", "La presión, 4 bar, porque es menor que el máximo", "La velocidad, 600 rpm, porque es menor que 650 rpm", "Solo la temperatura pasa el máximo de su rango; la presión y la velocidad están entre su mínimo y su máximo."),
        ("abc", "{F} ¿Qué lectura de la ronda de las 12:00 está fuera de rango?", "La presión, 2 bar, porque es menor que el mínimo de 3 bar", "La temperatura, 78 °C, porque es menor que 80 °C", "La velocidad, 610 rpm, porque es mayor que 600 rpm", "La presión está bajo el mínimo del rango; las otras dos lecturas están dentro de sus rangos."),
        ("=", "{F} ¿Cuántos grados Celsius sobre el máximo del rango estaba la temperatura de las 10:00?", "85-80", "Se resta el máximo del rango a la lectura de las 10:00.", " °C"),
        ("=", "{F} ¿Cuántos bar bajo el mínimo del rango estaba la presión de las 12:00?", "3-2", "Se resta la lectura al mínimo del rango de la presión.", " bar"),
        ("abc", "{F} ¿Cuál es la tendencia de la temperatura entre la ronda de las 10:00 y la de las 12:00?", "Bajó 7 °C, de 85 a 78 °C", "Subió 7 °C, de 78 a 85 °C", "Se mantuvo igual en las dos rondas", "A las 10:00 marcaba 85 °C y a las 12:00 marcó 78 °C: bajó."),
        ("abc", "{F} ¿Cuál es el informe correcto para la lectura de las 12:00 que está fuera de rango?", "«A las 12:00, presión del aceite 2 bar, bajo el rango de 3 a 5 bar»", "«Todo normal, porque la temperatura y la velocidad están en rango»", "«La presión marcó 3 bar a las 12:00 para dejarla en rango»", "El informe correcto declara hora, instrumento, valor, unidad y rango, y no oculta ni modifica el dato."),
        ("=", "{F} ¿Cuántas rpm de diferencia hay entre la lectura de velocidad de las 12:00 y la de las 10:00?", "610-600", "Se resta la lectura anterior a la lectura más reciente.", " rpm"),
        ("abc", "{F} A las 10:00 la planilla marca la temperatura fuera de rango, pero la presión y la velocidad están normales. ¿Qué corresponde?", "Informar la temperatura al oficial a cargo, aunque los otros dos instrumentos estén normales", "No informar nada, porque dos de los tres instrumentos están normales", "Esperar a la ronda de las 12:00 para ver si baja sola", "Cada lectura fuera de rango se informa, sin esperar ni promediar con las demás."),
        ("abc", "{F} ¿Cuál afirmación sobre las lecturas de las 12:00 es correcta?", "Una de las tres lecturas está fuera de rango", "Las tres lecturas están fuera de rango", "Ninguna lectura está fuera de rango", "Solo la presión de 2 bar queda fuera de su rango; la temperatura y la velocidad están dentro."),
        ("abc", "En Tripulación de Naves: ¿por qué una lectura fuera de rango no prueba por sí sola que el equipo esté fallando?", "Porque la falla podría estar en el instrumento y no en el equipo, y eso lo decide personal autorizado", "Porque los rangos de las planillas nunca son confiables", "Porque solo importan las lecturas que están dentro del rango", "Un dato fuera de rango puede deberse a un instrumento defectuoso; por eso se informa para que alguien autorizado lo evalúe."),
        ("=", "{F} Si la temperatura bajara 4 °C en cada ronda a partir del valor de las 12:00, ¿cuántos grados marcaría en la tercera ronda posterior a las 12:00?", "78-4*3", "Se restan 4 grados tres veces al valor de las 12:00.", " °C"),
        ("abc", "{F} En la ronda de las 14:00 la presión marca 4 bar y el oficial pregunta cómo evolucionó. ¿Qué respuesta es completa?", "Volvió al rango: marcó 2 bar a las 12:00 y 4 bar a las 14:00", "Sigue baja, porque a las 12:00 estaba en 2 bar", "No evolucionó, porque solo se mide a las 14:00", "Una respuesta completa compara la lectura nueva con la anterior y con el rango de 3 a 5 bar."),
    ],
    ctx=("abc", "En una visita de ejemplo, una persona de la tripulación te pide que «ajustes» la perilla de un equipo para que la lectura de temperatura vuelva a quedar en rango mientras ella va a buscar al oficial. ¿Qué respondes?", "Que no tocas el equipo y que solo anotas el valor leído mientras llega la persona autorizada", "Que sí, si lo haces despacio", "Que sí, si ella se hace responsable por escrito", "Intervenir un equipo exige autorización y formación; una promesa verbal o escrita no reemplaza eso."),
    sc=[
        ("En Tripulación de Naves: ¿cuándo una lectura está fuera de rango?", "Cuando queda bajo el mínimo o sobre el máximo del rango", "Fuera de rango significa fuera del intervalo mínimo-máximo."),
        ("¿Qué datos lleva el informe de una lectura fuera de rango?", "Hora, instrumento, valor, unidad y rango", "Con esos cinco datos el oficial puede decidir."),
        ("¿Qué es la tendencia de una lectura?", "Si el valor sube, baja o se mantiene entre rondas", "La tendencia compara una lectura con la ronda anterior."),
    ],
    op=("Planilla de ejemplo: rango del nivel del tanque de servicio, de 5 a 20 m³; rango de la velocidad del eje, de 80 a 120 rpm. Ronda de las 06:00: nivel 12 m³, velocidad 100 rpm. Ronda de las 08:00: nivel 4 m³, velocidad 118 rpm. Escribe (a) qué lectura de las 08:00 está fuera de rango y por cuánto, (b) la tendencia del nivel entre las 06:00 y las 08:00, (c) el informe completo para el oficial, (d) por qué no debes modificar la planilla.",
        "(a) El nivel de 4 m³, 1 m³ bajo el mínimo de 5 m³. (b) Bajó 8 m³ en dos horas. (c) «A las 08:00, nivel del tanque de servicio 4 m³, bajo el rango de 5 a 20 m³; a las 06:00 era 12 m³». (d) Porque modificarla oculta información real y puede tapar una falla.",
        ["detecta la lectura fuera de rango", "calcula la diferencia y la tendencia", "redacta el informe con todos los datos", "explica por qué no se altera la planilla"],
        ["hoja con las cuatro respuestas"],
        ["no indicar el rango en el informe", "informar solo la lectura rara sin hora", "proponer ajustar el equipo"],
        "Pregunta: «¿qué datos necesita el oficial para decidir?». Si no responde, pídele que relea la segunda parte de la explicación."),
    reinforce="Inventa una planilla de ejemplo con tres instrumentos y dos rondas, y marca cuál lectura está fuera de rango.",
    extend="Explica por qué mirar la tendencia ayuda más que mirar una sola lectura.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (registro de ejemplo, inventado). Nivel del tanque de servicio de una nave ficticia, en m³, leído cada 2 horas: 06:00, 20 m³; 08:00, 16 m³; 10:00, 12 m³; 12:00, 8 m³. "
     "El oficial de ejemplo pide informar cuando el nivel baje a 6 m³ o menos. El tanque no se rellena en ese período.")
build(
    O1, 4, F,
    use="Aprenderé a calcular diferencias, consumo por hora y tiempo restante con datos de un registro, y a informar según un umbral definido.",
    prior=["Sé leer un registro de lecturas con horas.", "Sé restar y dividir números enteros.", "Sé qué es un rango y una tendencia."],
    explain=[
        "Con lecturas repetidas se calculan datos nuevos. La diferencia entre dos lecturas es el valor mayor menos el menor. El consumo por hora es la diferencia de nivel dividida por las horas que pasaron entre las dos lecturas. Si el consumo se mantiene constante, se puede estimar cuánto falta para llegar a un nivel: horas restantes = nivel que falta bajar ÷ consumo por hora. Una estimación es un cálculo aproximado y no una promesa.",
        "Un umbral es un valor fijado de antemano que, al alcanzarse, obliga a informar. Un ejemplo con otro tanque: baja de 30 m³ a 24 m³ en 3 horas, es decir, 2 m³ por hora; si el umbral fuera 10 m³, faltan 14 m³ y a ese ritmo pasarían 7 horas. En una nave estos cálculos se hacen en planilla, con datos de ejemplo, y sirven para avisar con tiempo al oficial.",
        f"Calcular no autoriza a tomar decisiones por cuenta propia: el dato y la estimación se informan y el oficial a cargo decide. Los valores reales dependen de la nave y de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("diferencia", "valor mayor menos valor menor entre dos lecturas"), ("consumo por hora", "diferencia de nivel dividida por las horas transcurridas"), ("umbral", "valor fijado de antemano que obliga a informar al alcanzarse"), ("estimación", "cálculo aproximado basado en un supuesto, como que el consumo no cambia"), ("tanque de servicio", "tanque pequeño que alimenta a un equipo y se vigila con frecuencia")],
    worked=[
        ("Consumo por hora", "Un tanque de ejemplo pasa de 18 m³ a 12 m³ en 3 horas. ¿Cuánto consume por hora?", ["La diferencia es 18 − 12 = 6 m³.", "Se divide entre las 3 horas."], "2 m³ por hora"),
        ("Horas restantes", "Un tanque de ejemplo tiene 10 m³ y consume 2 m³ por hora. El umbral es 4 m³. ¿Cuántas horas faltan para alcanzarlo?", ["Faltan 10 − 4 = 6 m³ para llegar al umbral.", "Se dividen 6 m³ entre 2 m³ por hora."], "3 horas"),
    ],
    mistakes=[("Calcular el consumo dividiendo por la cantidad de lecturas en vez de por las horas transcurridas.", "El consumo por hora se mide con el tiempo que pasó, no con el número de lecturas.", "Divide la diferencia de nivel entre las horas entre las dos lecturas."),
              ("Creer que una estimación es un hecho seguro.", "Si el consumo cambia, la estimación deja de valer.", "Informa la estimación como estimación y vuelve a leer el instrumento.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es un umbral en una vigilancia de niveles?", "Un valor fijado de antemano que, al alcanzarse, obliga a informar", "El valor máximo que puede marcar cualquier instrumento", "El nombre del tanque que se vigila", "El umbral es un valor de aviso decidido antes; no es un máximo general ni el nombre de un tanque."),
        ("=", "{F} ¿Cuántos m³ bajó el nivel entre las 06:00 y las 08:00?", "20-16", "Se resta la lectura de las 08:00 a la lectura de las 06:00.", " m³"),
        ("abc", "{F} ¿Cuál es el consumo por hora del tanque entre las 06:00 y las 08:00?", "2 m³ por hora, porque bajó 4 m³ en 2 horas", "4 m³ por hora, porque bajó 4 m³", "1 m³ por hora, porque se hicieron dos lecturas", "El consumo por hora es la diferencia dividida por las horas: 4 ÷ 2."),
        ("=", "{F} ¿Cuántos m³ bajó el nivel entre las 06:00 y las 12:00?", "20-8", "Se resta la última lectura a la primera lectura del registro.", " m³"),
        ("=", "{F} ¿Cuántos m³ por hora consumió el tanque entre las 06:00 y las 12:00?", "(20-8)//6", "Se divide la diferencia total de nivel entre las 6 horas del período.", " m³ por hora"),
        ("abc", "{F} ¿El consumo fue constante en el período del registro?", "Sí, bajó 4 m³ cada 2 horas", "No, bajó más a las 08:00 que a las 12:00", "No, el nivel subió entre las 10:00 y las 12:00", "Cada intervalo de 2 horas muestra una baja de 4 m³, por lo tanto el consumo fue constante."),
        ("=", "{F} A la última lectura, ¿cuántos m³ faltan para llegar al umbral que pide el oficial?", "8-6", "Se resta el umbral al nivel de las 12:00.", " m³"),
        ("=", "{F} Si el consumo se mantiene como en el registro, ¿cuántas horas después de las 12:00 se alcanza el umbral?", "(8-6)//2", "Se divide lo que falta para el umbral entre el consumo por hora.", " horas"),
        ("abc", "{F} Si el consumo se mantiene, ¿a qué hora el nivel llega al umbral y debe informarse?", "A las 13:00", "A las 14:00", "A las 12:00", "Faltan 2 m³ y se consume 2 m³ por hora: se alcanza una hora después de las 12:00."),
        ("abc", "{F} A las 12:00 un compañero dice que no hace falta informar nada porque el tanque aún tiene 8 m³. ¿Qué respuesta es correcta?", "Se puede informar una estimación: a ese ritmo se llegará al umbral en una hora", "No se informa nada hasta que el nivel pase por debajo del umbral", "Se espera a las 14:00 para hacer una sola lectura", "Informar con anticipación una estimación permite decidir a tiempo."),
        ("abc", "En Tripulación de Naves: ¿por qué se dice que el tiempo restante calculado es una estimación?", "Porque supone que el consumo se mantiene igual y puede cambiar", "Porque la planilla no permite cálculos exactos", "Porque el tiempo no puede medirse con relojes", "La estimación depende de un supuesto: el consumo constante."),
        ("=", "{F} Si el consumo se mantuviera como en el registro desde las 06:00, ¿cuántas horas habrían bastado para vaciar por completo el tanque?", "20//2", "Se divide el nivel de las 06:00 entre el consumo por hora de la ficha.", " horas"),
        ("abc", "{F} A las 12:00 el oficial pregunta cuánto combustible gastó el tanque desde las 06:00 y a qué ritmo. ¿Qué informe es completo?", "Gastó 12 m³ en 6 horas, a 2 m³ por hora, y quedan 8 m³", "Gastó 8 m³ en total, a un ritmo constante", "Quedan 12 m³, porque se anotó la lectura de las 06:00", "Un informe completo da cuánto gastó, en cuánto tiempo, el ritmo y lo que queda."),
    ],
    ctx=("abc", "En una ronda de ejemplo, un compañero calcula el consumo y obtiene 3 m³ por hora, pero las lecturas del registro dan 2 m³ por hora. ¿Qué corresponde?", "Revisar el cálculo con las lecturas y, si hay dudas, preguntar al oficial", "Informar 3 m³ por hora, porque su cálculo es más rápido", "Cambiar las lecturas del registro para que coincidan con su cálculo", "Un cálculo se corrige revisando los datos del registro, no cambiando los datos."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se calcula el consumo por hora?", "Diferencia de nivel dividida por las horas transcurridas", "Así se obtiene cuánto baja el nivel en cada hora."),
        ("¿Qué es una estimación de horas restantes?", "Un cálculo aproximado que supone que el consumo se mantiene igual", "La estimación vale solo si el consumo no cambia."),
        ("¿A quién se informa que se alcanzará un umbral?", "Al oficial a cargo", "El oficial decide qué hacer con la información."),
    ],
    op=("Registro de ejemplo del nivel de un tanque, en m³: 14:00, 30 m³; 16:00, 24 m³; 18:00, 18 m³. El umbral de aviso es 6 m³. Escribe (a) cuántos m³ bajó entre las 14:00 y las 18:00, (b) el consumo por hora, (c) a qué hora se alcanzaría el umbral si el consumo no cambia, (d) cómo informarías esto al oficial indicando que es una estimación.",
        "(a) 30 − 18 = 12 m³. (b) 12 ÷ 4 = 3 m³ por hora. (c) A las 18:00 faltan 12 m³ para el umbral; 12 ÷ 3 = 4 horas, es decir, a las 22:00. (d) «A las 18:00 el nivel es 18 m³ y baja 3 m³ por hora; si el consumo no cambia, llegará a 6 m³ hacia las 22:00 (estimación)».",
        ["calcula la diferencia", "calcula el consumo por hora", "estima la hora del umbral", "informa señalando que es una estimación"],
        ["hoja con las cuatro respuestas"],
        ["dividir por el número de lecturas", "no sumar las horas a la hora de la última lectura", "no decir que es una estimación"],
        "Pregunta: «¿cuántas horas pasaron entre las 14:00 y las 18:00?». Si no responde, pídele que escriba la resta de horas."),
    reinforce="Inventa un registro de cuatro lecturas con un consumo constante y calcula el consumo por hora.",
    extend="Explica qué pasaría con la estimación si el consumo del tanque de ejemplo aumentara a mitad del período.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (informes de ejemplo, inventados). Una misma lectura de la «Nave Demo» se informó de tres maneras. Informe 1: «El motor está raro.» Informe 2: «A las 14:10, temperatura del agua de enfriamiento del motor principal, 88 °C, rango de la planilla de 60 a 80 °C.» "
     "Informe 3: «Temperatura 88.» Además, dos termómetros del mismo circuito marcan a las 14:10: el termómetro A, 88 °C, y el termómetro B, 70 °C.")
build(
    O1, 5, F,
    use="Aprenderé a comparar informes de una misma lectura, a elegir el más completo y a verificar un dato cruzándolo con un segundo instrumento.",
    prior=["Sé informar una lectura con instrumento, valor y unidad.", "Sé qué es un rango y una lectura fuera de rango.", "Sé restar números enteros."],
    explain=[
        "Un buen informe permite que otra persona entienda el dato sin preguntar. Tiene cinco datos: hora, equipo o instrumento, valor, unidad y rango o referencia. Un informe vago como «está raro» no dice qué se midió ni cuánto; uno sin unidad o sin hora puede mal interpretarse. Para elegir entre alternativas se compara cada informe con una lista de criterios y se escoge el que cumple más criterios, sin importar si es el más corto o el más largo.",
        "Verificar la calidad de un dato es comprobarlo con otra fuente. Si dos instrumentos miden lo mismo y sus lecturas difieren mucho, el dato no está confirmado: puede fallar uno de los instrumentos. En ese caso se informan ambas lecturas y la diferencia, sin elegir por cuenta propia cuál creer. Un ejemplo con otro circuito: un manómetro marca 3 bar y otro del mismo circuito marca 5 bar; se informan los dos valores y los 2 bar de diferencia.",
        f"Todo informe se firma o se registra con la hora y la persona que lo hizo, para saber quién lo emitió. {EMER} {AVISO}",
    ],
    vocab=[("informe completo", "informe con hora, equipo o instrumento, valor, unidad y referencia"), ("verificar", "comprobar un dato con otra fuente"), ("lectura cruzada", "comparación de dos instrumentos que miden lo mismo"), ("discrepancia", "diferencia importante entre dos lecturas que deberían parecerse"), ("criterio", "regla con la que se evalúa o se compara algo")],
    worked=[
        ("Elegir el informe más completo", "Informe X: «Temperatura alta.» Informe Y: «A las 09:30, aceite del motor auxiliar, 72 °C, rango de 50 a 70 °C.» ¿Cuál es más completo?", ["El informe Y trae hora, equipo, valor, unidad y rango.", "El informe X no trae ninguno de esos datos."], "El informe Y"),
        ("Detectar una discrepancia", "Dos manómetros del mismo circuito marcan 6 bar y 9 bar. ¿Hay discrepancia? ¿De cuánto?", ["Los dos instrumentos miden lo mismo y deberían parecerse.", "Se resta 9 − 6."], "Sí, de 3 bar"),
    ],
    mistakes=[("Elegir el informe más corto porque «ahorra tiempo».", "Un informe corto sin hora, valor o unidad obliga a preguntar y puede llevar a error.", "Elige el que trae los cinco datos."),
              ("Elegir por cuenta propia cuál de dos lecturas distintas es la verdadera.", "Con una discrepancia no se sabe cuál instrumento falla.", "Informa ambas lecturas y la diferencia, y deja que el oficial decida.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es una lectura cruzada?", "La comparación de dos instrumentos que miden lo mismo", "La lectura de un instrumento hecha por dos personas a la vez", "La lectura de un solo instrumento en dos horas distintas", "La lectura cruzada compara dos instrumentos distintos que miden lo mismo."),
        ("abc", "{F} ¿Cuál de los tres informes es el más completo?", "El informe 2, porque trae hora, equipo, valor, unidad y rango", "El informe 3, porque es el más breve", "El informe 1, porque dice cómo se ve el motor", "El informe 2 es el único que trae hora, equipo, valor, unidad y rango."),
        ("abc", "{F} ¿Qué datos faltan en el informe 3?", "La unidad, la hora y el equipo que se midió", "Solo la unidad", "Ninguno, porque ya dice el valor", "El informe 3 solo trae un número; faltan hora, equipo y unidad."),
        ("=", "{F} ¿Cuántos grados Celsius sobre el máximo del rango estaba el valor del informe 2?", "88-80", "Se resta el máximo del rango a la lectura informada.", " °C"),
        ("=", "{F} ¿Qué diferencia hay entre las lecturas de los termómetros A y B?", "88-70", "Se resta la lectura menor a la lectura mayor de los dos termómetros.", " °C"),
        ("abc", "{F} ¿Qué indica la diferencia entre los termómetros A y B?", "Una discrepancia: el dato no está confirmado y un instrumento podría fallar", "Que el termómetro B es el correcto, porque marca menos", "Que ambos están bien, porque los dos están bajo 100 °C", "Con una diferencia grande no se sabe cuál falla; el dato queda sin confirmar."),
        ("abc", "{F} ¿Cuál es el informe adecuado de la discrepancia?", "«A las 14:10, termómetro A 88 °C y termómetro B 70 °C, diferencia de 18 °C; rango de 60 a 80 °C»", "«A las 14:10, el termómetro B está bien y el A está malo»", "«A las 14:10, 88 °C»", "El informe adecuado declara ambas lecturas y la diferencia sin elegir cuál creer."),
        ("=", "{F} Si el rango máximo es 80 °C, ¿cuántos grados de margen tiene el termómetro B respecto de ese máximo?", "80-70", "Se resta la lectura del termómetro B al máximo del rango.", " °C"),
        ("abc", "{F} Un compañero propone informar solo la lectura del termómetro B, que está en rango, y dejar la del A «para no alarmar». ¿Qué corresponde?", "Informar ambas lecturas, porque callar un dato fuera de rango es inseguro", "Informar solo la del B, porque es la que está en rango", "No informar ninguna hasta tener una tercera lectura", "Omitir un dato fuera de rango oculta información que el oficial necesita."),
        ("abc", "{F} ¿Qué criterio del informe completo cumple el informe 2 y no cumple el informe 3?", "Incluir la referencia del rango de la planilla", "Estar escrito en una sola línea", "Usar la palabra «temperatura»", "El informe 3 también dice «temperatura» y es corto; solo el 2 trae el rango."),
        ("abc", "En Tripulación de Naves: ¿por qué al informar una discrepancia no se elige cuál instrumento creer?", "Porque no se sabe cuál falla y decidirlo corresponde a personal autorizado", "Porque los instrumentos siempre marcan lo mismo", "Porque el instrumento con menor valor siempre es el correcto", "No hay forma de saber cuál falla sin revisarlos; lo decide quien está autorizado."),
        ("=", "{F} Los dos termómetros se vuelven a leer media hora después y la diferencia es el doble de la de las 14:10. ¿Cuántos grados de diferencia hay ahora?", "(88-70)*2", "Se calcula la diferencia de las 14:10 y se duplica.", " °C"),
        ("abc", "{F} A las 14:40 los termómetros A y B marcan 86 °C y 84 °C. ¿Qué cambió respecto de las 14:10?", "La discrepancia bajó a 2 °C, pero ambos siguen sobre el máximo de 80 °C", "La discrepancia subió a 18 °C", "Ambos quedaron dentro del rango de la planilla", "Ahora difieren en 2 °C, aunque ambos siguen sobre 80 °C."),
    ],
    ctx=("abc", "El oficial de ejemplo te pide un informe de la presión de aceite. Tienes dos manómetros del mismo circuito: uno marca 4 bar y el otro 7 bar. ¿Qué entregas?", "Los dos valores con sus unidades, la hora y la diferencia de 3 bar", "Solo el de 4 bar, porque está más cerca del rango", "Solo el promedio, sin decir de dónde sale", "Un informe honesto muestra ambas lecturas y la discrepancia."),
    sc=[
        ("En Tripulación de Naves: ¿qué cinco datos tiene un informe completo?", "Hora, equipo, valor, unidad y referencia o rango", "Esos datos permiten entender la lectura sin preguntar."),
        ("¿Qué es una discrepancia?", "Una diferencia importante entre dos lecturas que deberían parecerse", "La discrepancia indica que el dato no está confirmado."),
        ("A bordo: ¿qué se hace con una discrepancia?", "Se informan ambas lecturas y la diferencia", "Elegir una lectura sin saber cuál falla es una conjetura."),
    ],
    op=("Informes de ejemplo sobre la presión del aceite de un motor auxiliar, rango de la planilla de 2 a 4 bar. Informe P: «Presión baja.» Informe Q: «A las 20:05, motor auxiliar, aceite, 1 bar, rango de 2 a 4 bar.» Un segundo manómetro del mismo circuito marca 3 bar a las 20:05. Escribe (a) cuál informe es mejor y por qué, (b) cuántos bar de discrepancia hay entre los dos manómetros, (c) cómo redactarías el informe final con ambos valores, (d) por qué no debes decidir cuál manómetro está bien.",
        "(a) El informe Q, porque trae hora, equipo, valor, unidad y rango. (b) 3 − 1 = 2 bar. (c) «A las 20:05, motor auxiliar, aceite: manómetro 1 marca 1 bar y manómetro 2 marca 3 bar, diferencia de 2 bar; rango de 2 a 4 bar». (d) Porque no se sabe cuál instrumento falla y lo decide personal autorizado.",
        ["elige el informe más completo", "calcula la discrepancia", "redacta el informe final con ambas lecturas", "explica por qué no se elige un manómetro"],
        ["hoja con las cuatro respuestas"],
        ["elegir el informe más corto", "informar solo una lectura", "olvidar la unidad y la hora"],
        "Pregunta: «¿qué datos tiene el informe Q que no tiene el P?». Si no responde, pídele que los liste."),
    reinforce="Escribe dos informes de una misma lectura, uno incompleto y uno completo, y marca los datos que faltan en el primero.",
    extend="Explica con un ejemplo por qué verificar un dato con un segundo instrumento mejora la calidad de la información.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La sala de máquinas de la «Nave Demo» cuenta con 1 motor principal, 2 generadores auxiliares, 1 bomba de achique (saca el agua acumulada en el fondo de la nave) y 1 compresor de aire. "
     "Las personas se reparten en guardias de 4 horas con 2 personas por guardia en la sala. Peligros anotados: ruido alto, superficies calientes, partes giratorias, aceite derramado en el piso y humo.")
build(
    O2, 1, F,
    use="Aprenderé qué es asistir la operación de una máquina, cuáles son los peligros de la sala de máquinas y qué hacer y qué no hacer como persona en formación.",
    prior=["Sé qué es el área de máquinas de una nave.", "Sé qué es la jerarquía de controles.", "Sé sumar y multiplicar números enteros."],
    explain=[
        "La máquina propulsora es el conjunto de equipos que mueve la nave: el motor principal, el eje y la hélice. Las máquinas auxiliares son los equipos que apoyan a la nave: los generadores producen electricidad, las bombas mueven líquidos y los compresores entregan aire a presión. Asistir la operación significa apoyar a quien opera, bajo la dirección del oficial de máquinas, con tareas simples de lectura, aviso y registro. No significa operar solo ni intervenir un equipo.",
        "En la sala de máquinas los peligros son el ruido, las superficies calientes, las partes giratorias, los derrames de aceite y el humo. Se previenen con la jerarquía de controles: primero eliminar o sustituir el peligro, luego usar protecciones fijas (como resguardos en las partes giratorias), reglas y letreros, y al final el equipo de protección personal, como los protectores auditivos. Un ejemplo de otra nave: un resguardo fijo sobre un eje giratorio es un control de ingeniería.",
        f"Un plan de funcionamiento indica qué equipos deben estar en marcha y con qué valores; se verifica leyendo los instrumentos, no tocando los equipos. {EMER} {AVISO}",
    ],
    vocab=[("máquina propulsora", "conjunto de equipos que mueve la nave: motor principal, eje y hélice"), ("máquinas auxiliares", "equipos que apoyan a la nave, como generadores, bombas y compresores"), ("generador", "equipo que produce electricidad"), ("asistir la operación", "apoyar a quien opera con lectura, aviso y registro, sin operar solo"), ("resguardo", "protección fija que impide tocar una parte peligrosa"), ("plan de funcionamiento", "documento que indica qué equipos funcionan y con qué valores")],
    worked=[
        ("Clasificar un equipo", "En una nave de ejemplo, un equipo produce la electricidad que usan las luces y los instrumentos. ¿Es propulsor o auxiliar?", ["Producir electricidad no mueve la nave directamente.", "Los equipos que apoyan a la nave son auxiliares."], "Máquina auxiliar (un generador)"),
        ("Clasificar un control", "En una nave de ejemplo se instala un resguardo fijo sobre un eje que gira. ¿A qué nivel de la jerarquía corresponde?", ["El resguardo cambia físicamente el lugar y no depende de que alguien lo recuerde.", "Un cambio físico del lugar es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Creer que asistir significa poder arrancar o detener los equipos.", "Asistir es apoyar con lectura, aviso y registro bajo la dirección del oficial; operar exige autorización.", "Haz solo lo que el oficial autorice y avisa antes de cualquier duda."),
              ("Creer que los protectores auditivos eliminan el ruido.", "El EPP protege solo a quien lo usa y no quita el peligro.", "Primero se controla el ruido en su origen y el EPP se suma después.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es la máquina propulsora?", "El conjunto de equipos que mueve la nave, como el motor principal, el eje y la hélice", "El conjunto de equipos que produce la electricidad para las luces", "El conjunto de bombas que saca el agua acumulada en el fondo", "La propulsora mueve la nave; los generadores y las bombas son equipos auxiliares."),
        ("abc", "En Tripulación de Naves: ¿qué hace un generador auxiliar?", "Produce electricidad para la nave", "Mueve la hélice de la nave", "Entrega aire a presión a los equipos", "El generador produce electricidad; la hélice la mueve el sistema propulsor."),
        ("abc", "En Tripulación de Naves: ¿qué significa asistir la operación de un equipo?", "Apoyar con lectura, aviso y registro bajo la dirección del oficial, sin operar solo", "Operar el equipo con libertad cuando el oficial no está", "Reparar el equipo cuando se detecta una falla", "Asistir es apoyar bajo dirección; operar solo o reparar exige autorización."),
        ("=", "{F} ¿Cuántos equipos auxiliares hay en la sala de máquinas de la ficha, contando generadores, bomba y compresor?", "2+1+1", "Se suman los dos generadores, la bomba y el compresor, sin contar el motor principal.", " equipos"),
        ("abc", "{F} Un resguardo fijo que impide tocar una parte giratoria es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla escrita", "De EPP, porque protege a quien se acerca", "El resguardo es una barrera física y no depende de que cada persona lo recuerde."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al aceite derramado en el piso?", "Que una persona resbale y se lesione", "Que el compresor entregue menos aire", "Que el plan de funcionamiento cambie de hora", "El riesgo es un daño para las personas; las otras opciones no lo son."),
        ("=", "{F} ¿Cuántos puestos de trabajo de la sala de máquinas se cubren en un día completo, sumando todas las guardias de 4 horas?", "24//4*2", "Se calculan las guardias que hay en 24 horas y se multiplican por las personas de cada guardia.", " puestos"),
        ("=", "En una ronda de ejemplo se visitan 6 equipos de la sala y en cada uno se leen 4 instrumentos. Si la ronda se repite 3 veces en una guardia, ¿cuántas lecturas se hacen?", "6*4*3", "Se multiplican los equipos, los instrumentos por equipo y las rondas.", " lecturas"),
        ("abc", "{F} Un compañero dice que, como el oficial no está, puede arrancar el compresor «para adelantar». ¿Qué respuesta es correcta?", "Es falso: asistir no autoriza a operar equipos sin la dirección del oficial", "Es cierto, si ya vio cómo se hace antes", "Es cierto, si usa protectores auditivos", "Ver una tarea o usar EPP no autoriza a operar un equipo."),
        ("abc", "{F} ¿Cuál medida es de nivel más efectivo en la jerarquía de controles para el peligro de las partes giratorias?", "Instalar un resguardo fijo que impida tocarlas", "Poner un letrero que diga «peligro, partes giratorias»", "Entregar guantes a cada persona", "El resguardo cambia el lugar; el letrero informa y los guantes son EPP."),
        ("abc", "En la sala de máquinas de ejemplo comienza un incendio. ¿Qué corresponde a una persona en formación según las reglas generales?", "No acercarte a la zona de riesgo, dar la alarma y avisar a un adulto responsable y a emergencias", "Acercarte para apagar el fuego con lo que encuentres", "Cerrar la puerta y esperar a que se apague solo", "Combatir un incendio exige formación y equipo; la conducta segura es dar la alarma y avisar."),
        ("=", "{F} Si cada equipo de la sala tiene 3 letreros de señalética, ¿cuántos letreros hay en total, contando todos los equipos de la ficha?", "(1+2+1+1)*3", "Se suman los equipos de la ficha y se multiplican por los letreros de cada uno.", " letreros"),
        ("abc", "{F} Una persona en formación nota humo en la sala de máquinas. ¿Qué es lo correcto?", "Dar la alarma y avisar de inmediato sin acercarse al origen del humo", "Acercarse para identificar el equipo y luego avisar", "Anotar la hora y avisar al terminar la guardia", "El humo puede indicar un incendio; no se investiga de cerca y se avisa de inmediato."),
    ],
    ctx=("abc", "Un conocido que trabaja en un buque te ofrece llevarte a la sala de máquinas a «mirar cómo se arranca el motor». ¿Qué respondes?", "Que no, porque entrar a una sala de máquinas exige instructor autorizado, norma vigente y elementos de protección, y que lo hablarás con un adulto responsable", "Que sí, si vas con casco y calzado", "Que sí, si entras solo cuando el motor está apagado", "El EPP y un motor apagado no reemplazan la autorización ni la formación."),
    sc=[
        ("En Tripulación de Naves: ¿qué son las máquinas auxiliares?", "Los equipos que apoyan a la nave, como generadores, bombas y compresores", "Las auxiliares apoyan; la propulsora mueve la nave."),
        ("¿Qué es un resguardo?", "Una protección fija que impide tocar una parte peligrosa", "El resguardo es un control de ingeniería."),
        ("¿Qué hace una persona en formación ante humo en la sala?", "Da la alarma y avisa sin acercarse", "Ante humo o incendio no se interviene sin formación."),
    ],
    op=("En la sala de máquinas de la «Nave Ejemplo» (caso de ejemplo) hay un compresor con una correa giratoria sin protección y un charco de aceite junto a él. Escribe (a) cuáles son los dos peligros, (b) el riesgo asociado a cada uno, (c) un control de ingeniería para la correa, (d) por qué una persona en formación no debe resolverlo por su cuenta.",
        "(a) La correa giratoria sin protección y el charco de aceite. (b) Que una mano o la ropa quede atrapada; que alguien resbale. (c) Un resguardo fijo sobre la correa. (d) Porque asistir no es operar ni reparar: la tarea la hace personal autorizado y la persona en formación avisa al oficial.",
        ["identifica los dos peligros", "señala el riesgo de cada uno", "propone un control de ingeniería", "explica por qué avisa y no interviene"],
        ["hoja con las cuatro respuestas"],
        ["confundir peligro con riesgo", "proponer solo EPP", "proponer que la persona en formación lo repare"],
        "Pregunta: «¿qué daño podría ocurrir y a quién?». Si no responde, pídele que relea los peligros de la sala."),
    reinforce="Haz una lista de los equipos de la sala de máquinas de ejemplo y marca cuáles son propulsores y cuáles auxiliares.",
    extend="Explica con un ejemplo por qué asistir es distinto de operar un equipo.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (señales de ejemplo, inventadas). En el pasillo de máquinas de la «Nave Demo» hay cuatro señales. Señal 1: círculo azul con un casco blanco dibujado. Señal 2: triángulo amarillo con un rayo negro. "
     "Señal 3: círculo rojo con una barra diagonal sobre una llama. Señal 4: rectángulo verde con una cruz blanca.")
build(
    O2, 2, F,
    use="Aprenderé a reconocer la forma y el color de las señales de seguridad y qué significan los pictogramas de prohibición, obligación, advertencia y de condición segura.",
    prior=["Sé qué es una máquina auxiliar.", "Sé qué es la jerarquía de controles.", "Sé multiplicar números enteros."],
    explain=[
        "La señalética es el conjunto de señales que comunican una regla o un aviso sin palabras, con formas, colores y pictogramas. Un pictograma es un dibujo simple que representa una idea. Las señales de seguridad se reconocen por su forma y su color. Una señal de prohibición es un círculo rojo con una barra diagonal y dice qué no se debe hacer. Una señal de obligación es un círculo azul y dice qué se debe usar o hacer. Una señal de advertencia es un triángulo amarillo con borde negro y avisa de un peligro.",
        "Una señal de condición segura, de salvamento o de ayuda es un rectángulo o cuadrado verde, y indica dónde hay una salida, un puesto de ayuda o un equipo de emergencia. Un ejemplo de otra nave: un triángulo amarillo con un símbolo de superficie caliente avisa que hay un peligro por calor; un círculo azul con un par de guantes indica que se deben usar guantes. Las señales se combinan con instrucciones del oficial.",
        f"Las señales se respetan siempre. Si una señal no se entiende, se pregunta al oficial, sin tocar nada. Los significados exactos dependen de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("señalética", "conjunto de señales que comunican reglas y avisos con formas y colores"), ("pictograma", "dibujo simple que representa una idea"), ("señal de prohibición", "círculo rojo con barra diagonal que indica lo que no se debe hacer"), ("señal de obligación", "círculo azul que indica lo que se debe usar o hacer"), ("señal de advertencia", "triángulo amarillo con borde negro que avisa de un peligro"), ("señal de condición segura", "rectángulo o cuadrado verde que indica salidas, ayuda o equipos de emergencia")],
    worked=[
        ("Leer una señal", "Una señal de ejemplo es un círculo azul con unos guantes dibujados. ¿Qué indica?", ["El círculo azul es una señal de obligación.", "El dibujo indica qué se debe usar: guantes."], "Es obligatorio usar guantes"),
        ("Clasificar por forma y color", "Una señal de ejemplo es un triángulo amarillo con una superficie caliente dibujada. ¿Qué tipo de señal es?", ["El triángulo amarillo es una señal de advertencia.", "El dibujo dice de qué peligro avisa."], "Advertencia de superficie caliente"),
    ],
    mistakes=[("Creer que el color verde significa peligro.", "El verde indica condición segura, salida o ayuda, no peligro.", "Recuerda: rojo prohíbe, azul obliga, amarillo advierte y verde indica ayuda."),
              ("Interpretar una señal solo por el dibujo, sin mirar la forma ni el color.", "El mismo dibujo puede prohibir, obligar o advertir según su forma y color.", "Mira siempre forma, color y dibujo en ese orden.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué indica una señal con forma de círculo azul?", "Una obligación: algo que se debe usar o hacer", "Una prohibición: algo que no se debe hacer", "Una advertencia de peligro", "El círculo azul indica obligación; la prohibición es un círculo rojo con barra y la advertencia es un triángulo amarillo."),
        ("abc", "En Tripulación de Naves: ¿qué indica un triángulo amarillo con borde negro?", "Una advertencia de peligro", "Una obligación de usar equipo", "Una salida de emergencia", "El triángulo amarillo advierte; la obligación es un círculo azul y la salida es verde."),
        ("abc", "{F} ¿Qué significa la señal 1?", "Es obligatorio usar casco", "Está prohibido usar casco", "Hay peligro de caída de objetos", "El círculo azul con un casco indica obligación de usarlo."),
        ("abc", "{F} ¿Qué significa la señal 2?", "Advertencia de peligro eléctrico", "Obligación de usar guantes", "Prohibido tocar los cables", "El triángulo amarillo con un rayo avisa de un peligro eléctrico."),
        ("abc", "{F} ¿Qué significa la señal 3?", "Prohibido el fuego abierto", "Obligatorio usar protección contra el fuego", "Hay ayuda contra incendios cerca", "El círculo rojo con barra sobre una llama prohíbe el fuego abierto."),
        ("abc", "{F} ¿Qué tipo de señal es la señal 4?", "De condición segura o de ayuda", "De prohibición", "De advertencia", "El rectángulo verde con una cruz blanca indica ayuda, por ejemplo un puesto de primeros auxilios."),
        ("=", "{F} En el pasillo hay 3 conjuntos iguales de las cuatro señales de la ficha. ¿Cuántas señales hay en total?", "4*3", "Se multiplica el número de señales de cada conjunto por el número de conjuntos.", " señales"),
        ("=", "En una nave de ejemplo hay 6 pasillos, cada uno con 2 señales de obligación y 3 de advertencia. ¿Cuántas señales hay en total?", "6*(2+3)", "Se suman las señales de cada pasillo y se multiplican por los pasillos.", " señales"),
        ("abc", "{F} Una persona entra a la zona de la señal 1 sin usar casco. ¿Qué incumple?", "Una obligación señalizada", "Una prohibición señalizada", "Nada, porque la señal solo informa", "Una señal de obligación exige usar el equipo; entrar sin él incumple la regla."),
        ("abc", "{F} Se quiere señalizar que no se debe fumar en la sala. ¿Qué señal es la adecuada?", "Un círculo rojo con barra diagonal sobre un cigarro", "Un círculo azul con un cigarro", "Un triángulo amarillo con un cigarro", "Lo que no se debe hacer se indica con una prohibición: círculo rojo con barra."),
        ("abc", "{F} Dos personas discuten el significado de la señal 3. Una dice que la llama sola significa «obligatorio encender fuego» y otra que el círculo rojo con barra cambia el sentido. ¿Quién tiene razón?", "La que dice que el círculo rojo con barra indica prohibición de lo dibujado", "La que dice que el dibujo de una llama siempre obliga, porque el dibujo manda", "Ninguna, porque las formas y los colores no tienen significado", "La forma y el color determinan el tipo de señal: un círculo rojo con barra prohíbe lo dibujado."),
        ("abc", "Al entrar a una sala de ejemplo ves una señal que no entiendes. ¿Qué corresponde?", "Preguntar al oficial o a la persona a cargo sin tocar nada", "Ignorarla, porque debe ser un adorno", "Quitarla para ver qué hay detrás", "Una señal que no se entiende se consulta; no se ignora ni se retira."),
        ("abc", "{F} ¿Cuántas de las cuatro señales de la ficha tienen forma circular?", "Dos: la señal 1 y la señal 3", "Tres: las señales 1, 2 y 3", "Una: solo la señal 3", "El círculo azul y el círculo rojo son las señales 1 y 3; la 2 es triángulo y la 4, rectángulo."),
    ],
    ctx=("abc", "Estás de visita en una nave de ejemplo y notas que una señal de «prohibido el fuego abierto» está tapada con una caja. ¿Qué corresponde?", "Avisar a la persona a cargo para que la señal quede visible", "Dejarla tapada, porque todos saben que no se puede encender fuego", "Retirar la señal, porque estorba", "Una señal tapada deja de cumplir su función; se avisa para corregirla."),
    sc=[
        ("En Tripulación de Naves: ¿qué indica un círculo rojo con barra diagonal?", "Una prohibición", "El círculo rojo con barra prohíbe lo que muestra el dibujo."),
        ("¿Qué indica un rectángulo verde?", "Una condición segura, una salida o una ayuda", "El verde indica seguridad o ayuda, no peligro."),
        ("¿Qué hace una persona que no entiende una señal?", "Pregunta a la persona a cargo sin tocar nada", "Consultar evita errores y mantiene la seguridad."),
    ],
    op=("Señales de ejemplo en una sala de la «Nave Ejemplo»: S1, círculo azul con unos protectores auditivos; S2, círculo rojo con barra diagonal sobre un teléfono móvil; S3, triángulo amarillo con una mano atrapada entre dos engranajes; S4, rectángulo verde con una flecha hacia una puerta. Escribe (a) qué significa cada señal y de qué tipo es, (b) cuántas señales hay si se repiten en 4 salas, (c) cuál señal exige usar un equipo de protección y en qué nivel de la jerarquía de controles está ese equipo.",
        "(a) S1: obligatorio usar protectores auditivos (obligación). S2: prohibido usar el teléfono móvil (prohibición). S3: advertencia de peligro de atrapamiento (advertencia). S4: indica una salida (condición segura). (b) 4 × 4 = 16 señales. (c) La S1; el equipo de protección personal es el último nivel de la jerarquía de controles.",
        ["identifica el tipo de cada señal", "explica el significado de cada una", "calcula la cantidad total", "relaciona la señal con el EPP"],
        ["hoja con las respuestas"],
        ["usar solo el dibujo sin forma ni color", "confundir obligación con prohibición", "olvidar multiplicar por las salas"],
        "Pregunta: «¿qué forma y qué color tiene cada señal?». Si no responde, pídele que relea la primera parte de la explicación."),
    reinforce="Dibuja las cuatro formas de señales (círculo rojo, círculo azul, triángulo amarillo, rectángulo verde) y escribe su significado.",
    extend="Explica por qué una señal clara no reemplaza a un control de ingeniería en la jerarquía de controles.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (plan y registro de ejemplo, inventados). Plan de funcionamiento de un día de la «Nave Demo»: el generador 1 funciona de 00:00 a 12:00 y el generador 2 de 12:00 a 24:00. La bomba de achique solo funciona si el nivel de agua en la sentina (fondo de la nave) supera 20 cm. "
     "Lecturas del registro: a las 06:00, el generador 1 funciona y el nivel de agua es 15 cm. A las 14:00, el generador 2 funciona, el nivel de agua es 25 cm y la bomba está detenida. A las 22:00, el generador 1 funciona.")
build(
    O2, 3, F,
    use="Aprenderé a verificar un plan de funcionamiento leyendo un registro de instrumentos y a informar las diferencias con claridad.",
    prior=["Sé qué hace un generador y una bomba.", "Sé leer un plan con horarios.", "Sé restar números enteros."],
    explain=[
        "Un plan de funcionamiento dice qué equipos deben estar en marcha en cada momento y bajo qué condiciones. Verificarlo es comparar lo que dice el plan con lo que muestran los instrumentos y el registro. Si coinciden, la lectura es conforme. Si no coinciden, hay una diferencia con el plan, que se informa sin corregirla por cuenta propia. La sentina es el fondo de la nave donde se acumula agua, y una bomba de achique es la que saca esa agua.",
        "Muchos planes usan condiciones de umbral: «la bomba funciona solo si el nivel supera 20 cm». Entonces hay que leer el nivel y compararlo con el umbral. Un ejemplo con otra nave: el plan dice que un ventilador funciona solo de noche; a las 15:00 el registro lo muestra en marcha, por lo tanto hay una diferencia que se informa.",
        f"Una persona en formación no arranca ni detiene el equipo para que el registro coincida con el plan: informa la diferencia al oficial de máquinas. {EMER} {AVISO}",
    ],
    vocab=[("verificar el plan", "comparar lo que dice el plan con lo que muestran los instrumentos y el registro"), ("conforme", "que coincide con lo que dice el plan"), ("diferencia con el plan", "caso en que el registro no coincide con lo previsto"), ("sentina", "fondo de la nave donde se acumula agua"), ("bomba de achique", "bomba que saca el agua acumulada en la sentina"), ("umbral", "valor que condiciona el funcionamiento de un equipo")],
    worked=[
        ("Verificar un horario", "Plan de ejemplo: el equipo X funciona de 08:00 a 16:00. El registro de las 10:00 dice que X funciona. ¿Es conforme?", ["Las 10:00 están dentro del horario de 08:00 a 16:00.", "El registro coincide con el plan."], "Sí, es conforme"),
        ("Verificar un umbral", "Plan de ejemplo: una bomba funciona solo si el nivel supera 30 cm. El registro marca 35 cm y la bomba está detenida. ¿Es conforme?", ["35 cm supera el umbral de 30 cm.", "El plan pide que la bomba funcione, pero está detenida."], "No, hay una diferencia con el plan"),
    ],
    mistakes=[("Poner en marcha un equipo para que el registro coincida con el plan.", "Operar un equipo exige autorización y no es parte de asistir.", "Informa la diferencia al oficial y no toques el equipo."),
              ("Confundir «conforme con el plan» con «todo está bien en la nave».", "Conforme solo dice que se cumplió el plan, que puede no cubrir otros peligros.", "Informa lo que verificaste y lo que no pudiste verificar.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué significa verificar un plan de funcionamiento?", "Comparar lo que dice el plan con lo que muestran los instrumentos y el registro", "Cambiar el plan para que coincida con lo que se ve", "Arrancar todos los equipos del plan", "Verificar es comparar el plan con los datos y no modificar ni operar."),
        ("abc", "{F} ¿Qué generador debe estar funcionando a las 06:00 según el plan?", "El generador 1", "El generador 2", "Ambos generadores", "El plan dice que el generador 1 funciona de 00:00 a 12:00."),
        ("abc", "{F} ¿Es conforme con el plan el registro de las 06:00?", "Sí, porque funciona el generador 1 y el nivel de agua está bajo el umbral", "No, porque el generador 2 debía funcionar", "No, porque la bomba debía funcionar", "A las 06:00 funciona el generador previsto y 15 cm está bajo el umbral de 20 cm."),
        ("abc", "{F} ¿Qué diferencia con el plan muestra el registro de las 14:00?", "La bomba debía funcionar porque el nivel supera 20 cm, y está detenida", "El generador 2 no debía funcionar a esa hora", "No hay ninguna diferencia con el plan", "A las 14:00 el nivel de 25 cm supera el umbral; el plan pide la bomba en marcha."),
        ("=", "{F} ¿Cuántos centímetros sobre el umbral estaba el nivel de agua a las 14:00?", "25-20", "Se resta el umbral al nivel leído.", " cm"),
        ("abc", "{F} ¿Qué diferencia con el plan muestra el registro de las 22:00?", "Debía funcionar el generador 2 y funciona el generador 1", "Debía funcionar la bomba de achique", "No hay diferencia con el plan, porque cualquier generador sirve", "A las 22:00 el plan indica el generador 2, no el 1."),
        ("=", "{F} Según el plan, ¿cuántas horas funciona cada generador en un día?", "12-0", "Se resta la hora de inicio a la hora de término de cada generador.", " horas"),
        ("=", "{F} Según el plan, ¿cuántas horas de generador hay funcionando en total en 7 días, sumando los dos generadores?", "(12+12)*7", "Se suman las horas de los dos generadores de un día y se multiplican por 7.", " horas"),
        ("abc", "{F} ¿Cómo se informa correctamente la diferencia de las 14:00?", "«A las 14:00 el nivel de la sentina es 25 cm, sobre el umbral de 20 cm, y la bomba de achique está detenida»", "«La bomba está mala»", "«Arranqué la bomba para corregirlo»", "El informe correcto da hora, valor, umbral y estado de la bomba; no opera ni opina sin datos."),
        ("abc", "{F} Una persona en formación ve que la bomba debería funcionar pero está detenida. ¿Qué corresponde?", "Informar al oficial de máquinas la diferencia, sin accionar el equipo", "Accionar la bomba para que cumpla el plan", "Anotar en el registro que la bomba funciona", "Operar exige autorización; informar permite que el oficial decida y evita registros falsos."),
        ("abc", "En Tripulación de Naves: ¿por qué un registro conforme con el plan no prueba que todo esté bien en la nave?", "Porque el plan puede no cubrir otros peligros que no se han verificado", "Porque los planes siempre tienen errores", "Porque los registros no sirven para nada", "Conforme significa que se cumplió el plan, no que se hayan descartado otros riesgos."),
        ("=", "{F} Si el nivel de agua sube 2 cm por hora desde las 14:00, ¿cuántos centímetros tendrá 3 horas después?", "25+2*3", "Se suma el aumento de tres horas al nivel de las 14:00.", " cm"),
        ("abc", "{F} Entre las 14:00 y las 22:00 hay dos diferencias con el plan distintas. ¿Cuáles son?", "La bomba detenida con el nivel sobre el umbral y el generador 1 en vez del 2", "Solo el generador 1 en vez del 2", "Solo la bomba funcionando bajo el umbral", "El registro de las 14:00 y el de las 22:00 muestran cada uno una diferencia distinta con el plan."),
    ],
    ctx=("abc", "En una visita de ejemplo, ves que un registro de las 22:00 dice «generador 2 funcionando» pero el instrumento muestra el generador 1. La persona a cargo te dice: «anota lo que dice el plan, no lo que ves». ¿Qué corresponde?", "Anotar lo que muestra el instrumento e informar la diferencia", "Anotar lo que dice el plan, porque ella manda", "No anotar nada para evitar conflictos", "El registro debe reflejar lo observado; copiar el plan oculta una diferencia real."),
    sc=[
        ("En Tripulación de Naves: ¿qué es la sentina?", "El fondo de la nave donde se acumula agua", "La sentina recoge agua que luego se saca con una bomba de achique."),
        ("¿Qué significa «conforme con el plan»?", "Que el registro coincide con lo que dice el plan", "Conforme es lo contrario de diferencia con el plan."),
        ("¿Qué se hace al ver una diferencia con el plan?", "Se informa al oficial sin operar el equipo", "Asistir es informar; operar corresponde al personal autorizado."),
    ],
    op=("Plan de ejemplo: el compresor funciona de 06:00 a 18:00; la bomba de enfriamiento funciona siempre que el compresor funciona. Registro: a las 10:00 el compresor funciona y la bomba está detenida; a las 20:00 el compresor funciona y la bomba funciona. Escribe (a) si el registro de las 10:00 es conforme y por qué, (b) si el de las 20:00 es conforme y por qué, (c) cuántas horas funciona el compresor según el plan, (d) cómo informarías la diferencia de las 10:00.",
        "(a) No, porque la bomba debía funcionar mientras funciona el compresor. (b) No, porque a las 20:00 el compresor debía estar detenido según el plan. (c) 18 − 6 = 12 horas. (d) «A las 10:00 el compresor funciona y la bomba de enfriamiento está detenida; el plan indica que debe funcionar», con hora y sin operar el equipo.",
        ["verifica cada registro contra el plan", "explica la causa de cada diferencia", "calcula las horas del plan", "redacta el informe con hora y equipos"],
        ["hoja con las cuatro respuestas"],
        ["decir que todo es conforme", "omitir la hora en el informe", "proponer accionar el equipo"],
        "Pregunta: «¿qué dice el plan para cada hora?». Si no responde, pídele que escriba el horario de cada equipo."),
    reinforce="Escribe un plan de ejemplo con dos equipos y tres horarios, y luego un registro con una diferencia.",
    extend="Explica por qué es más seguro informar una diferencia que corregirla por cuenta propia.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada). Un generador de la «Nave Demo» tiene una capacidad de 300 kW. La demanda eléctrica de ejemplo es: luces, 60 kW; bombas, 90 kW; ventilación, 70 kW; otros equipos, 50 kW. "
     "Regla de la planilla de ejemplo: la demanda no debe superar el 80 % de la capacidad de un generador; si la supera, el plan debe prever un segundo generador. (Valores de ejemplo, no reales.)")
build(
    O2, 4, F,
    use="Aprenderé a calcular una demanda eléctrica, compararla con la capacidad de un generador y aplicar una regla de planilla de ejemplo.",
    prior=["Sé qué hace un generador.", "Sé calcular un porcentaje simple.", "Sé sumar y restar números enteros."],
    explain=[
        "La potencia eléctrica es la cantidad de electricidad que un equipo necesita o entrega y se mide en kilowatts (kW). La capacidad de un generador es la potencia máxima que puede entregar. La demanda es la suma de la potencia que piden los equipos conectados. La reserva es lo que sobra: reserva = capacidad − demanda. Para no llegar al límite, una planilla de ejemplo puede fijar una regla: por ejemplo, que la demanda no supere cierto porcentaje de la capacidad.",
        "Un ejemplo con otro generador: tiene una capacidad de 200 kW y la demanda es 120 kW. La reserva es 80 kW. Si la regla de ejemplo dijera que la demanda no debe superar el 50 % de la capacidad, el límite sería 100 kW y la demanda de 120 kW lo superaría, por lo que habría que prever un segundo generador. Estas reglas dependen de la nave y de la norma vigente, y aquí los valores son solo de ejemplo.",
        f"Estos cálculos se hacen en planilla y sirven para planificar; no autorizan a poner en marcha ni a conectar equipos. {EMER} {AVISO}",
    ],
    vocab=[("kilowatt (kW)", "unidad de potencia eléctrica"), ("capacidad", "potencia máxima que puede entregar un generador"), ("demanda", "suma de la potencia que piden los equipos conectados"), ("reserva", "capacidad menos demanda"), ("porcentaje de la capacidad", "parte de la capacidad que se usa, calculada sobre 100")],
    worked=[
        ("Calcular una reserva", "Un generador de ejemplo tiene capacidad de 150 kW y la demanda es 100 kW. ¿Cuánta reserva queda?", ["Reserva = capacidad − demanda.", "Se resta 150 − 100."], "50 kW"),
        ("Aplicar una regla", "Un generador de ejemplo de 200 kW debe cumplir que la demanda no pase del 60 % de su capacidad. La demanda es 110 kW. ¿La cumple?", ["El 60 % de 200 kW es 120 kW.", "La demanda de 110 kW no supera 120 kW."], "Sí, la cumple"),
    ],
    mistakes=[("Calcular la reserva restando la demanda a la regla del 80 % en lugar de a la capacidad.", "La reserva se calcula con la capacidad completa; la regla del porcentaje es otra comparación.", "Haz dos cálculos separados: reserva y límite de la regla."),
              ("Creer que si no se cumple la regla basta conectar menos equipos sin avisar.", "Cambiar las conexiones exige autorización y debe quedar registrado.", "Informa al oficial de máquinas y deja que quien está autorizado decida.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es la demanda eléctrica de una nave?", "La suma de la potencia que piden los equipos conectados", "La potencia máxima que puede entregar un generador", "La unidad en que se mide la tensión de un cable", "La demanda es lo que piden los equipos; la capacidad es lo que puede entregar el generador."),
        ("abc", "En Tripulación de Naves: ¿qué es la reserva de un generador?", "La capacidad menos la demanda", "La suma de la capacidad y la demanda", "La demanda de un solo equipo", "La reserva es lo que sobra: capacidad menos demanda."),
        ("=", "{F} ¿Cuántos kW suma la demanda de todos los equipos de la ficha?", "60+90+70+50", "Se suman las demandas de las luces, las bombas, la ventilación y los otros equipos.", " kW"),
        ("=", "{F} ¿Cuántos kW de reserva queda en el generador de la ficha?", "300-(60+90+70+50)", "Se resta la demanda total a la capacidad del generador.", " kW"),
        ("=", "{F} ¿Cuántos kW es el 80 % de la capacidad del generador de la ficha?", "300*80//100", "Se calcula el 80 % de la capacidad, que es el límite de la regla.", " kW"),
        ("abc", "{F} ¿Cumple la demanda de la ficha con la regla de ejemplo?", "No, porque 270 kW supera el límite de 240 kW", "Sí, porque 270 kW es menor que 300 kW", "Sí, porque sobran 30 kW de reserva", "La regla compara con 240 kW, no con la capacidad completa; 270 kW lo supera."),
        ("=", "{F} ¿Cuántos kW sobre el límite de la regla está la demanda?", "270-240", "Se resta el límite de la regla a la demanda total.", " kW"),
        ("abc", "{F} Según la regla de la ficha, ¿qué debe prever el plan?", "Un segundo generador", "Apagar las luces", "Cambiar la capacidad del generador en la planilla", "La regla dice que si se supera el límite el plan debe prever un segundo generador."),
        ("=", "{F} Si se quitan de la demanda los «otros equipos», ¿cuántos kW queda la demanda?", "60+90+70", "Se suman las demandas que quedan al retirar los otros equipos.", " kW"),
        ("abc", "{F} Si se quitan los «otros equipos» de la demanda, ¿cumple la regla?", "Sí, porque 220 kW no supera el límite de 240 kW", "No, porque con menos equipos conectados la regla no se puede aplicar", "No, porque la demanda debe ser siempre igual a la capacidad", "Con 220 kW la demanda queda bajo el límite de 240 kW."),
        ("abc", "{F} Una persona propone quitar por su cuenta el equipo «otros» para cumplir la regla. ¿Qué corresponde?", "Informar al oficial de máquinas y esperar su decisión", "Desconectarlo ella misma, porque son pocos kW", "Cambiar la demanda en la planilla a 240 kW", "Desconectar o alterar datos exige autorización; se informa."),
        ("abc", "En Tripulación de Naves: ¿por qué una regla de porcentaje deja un margen entre la demanda y la capacidad?", "Para que el generador no trabaje al límite y haya espacio para aumentos de la demanda", "Para que los equipos consuman menos combustible", "Para que la planilla tenga números redondos", "El margen evita trabajar al límite y permite absorber aumentos de la demanda."),
        ("abc", "{F} Si se conecta un equipo de 40 kW a la demanda de la ficha, ¿qué ocurre con la reserva?", "Queda en negativo: la demanda de 310 kW supera la capacidad de 300 kW", "Queda en 0, porque se llena el generador", "Queda en 40 kW, porque es la potencia del equipo", "300 menos 310 da un valor negativo: el generador no alcanzaría."),
    ],
    ctx=("abc", "En una visita de ejemplo, una persona a cargo te dice: «la demanda está sobre el límite de la regla, pero conecta igual el equipo nuevo, total el generador aguanta». ¿Qué corresponde?", "Informar al oficial de máquinas que se supera la regla y no conectar nada sin su autorización", "Conectarlo, porque ella tiene más experiencia", "Conectarlo y no anotarlo", "Conectar equipos sin autorización y sin registro es inseguro."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se calcula la reserva de un generador?", "Capacidad menos demanda", "La reserva es lo que queda de la capacidad."),
        ("¿Qué mide el kilowatt?", "La potencia eléctrica", "El kW es una unidad de potencia eléctrica."),
        ("¿Por qué los valores de esta clase son solo de ejemplo?", "Porque dependen de la nave y de la norma vigente", "Los valores reales no se deducen de una planilla de ejemplo."),
    ],
    op=("Planilla de ejemplo: generador de 400 kW; demanda: luces, 80 kW; bombas, 120 kW; ventilación, 90 kW; cocina y servicios, 60 kW. Regla de ejemplo: la demanda no debe pasar del 75 % de la capacidad. Escribe (a) la demanda total, (b) la reserva, (c) el límite de la regla en kW, (d) si cumple la regla y qué informarías al oficial.",
        "(a) 80 + 120 + 90 + 60 = 350 kW. (b) 400 − 350 = 50 kW. (c) 400 × 75 ÷ 100 = 300 kW. (d) No cumple, porque 350 kW supera 300 kW; se informa «la demanda es 350 kW, 50 kW sobre el límite de 300 kW, y el plan debe prever un segundo generador».",
        ["calcula la demanda total", "calcula la reserva", "calcula el límite de la regla", "informa si cumple y qué falta"],
        ["hoja con las cuatro respuestas"],
        ["restar el límite a la capacidad", "no aplicar el porcentaje", "no avisar al oficial"],
        "Pregunta: «¿cuánto es el 75 % de 400?». Si no responde, pídele que calcule primero el 25 % y lo reste."),
    reinforce="Inventa una planilla de tres equipos con su demanda y calcula la reserva de un generador.",
    extend="Explica qué pasaría con la reserva si la demanda de la planilla aumentara por la noche.",
)

# ============================================================ OAE-02, clase 5
F = ("Ficha 5 (planes de ejemplo, inventados). Dos planes para un día de la «Nave Demo»; la demanda de ejemplo es de 270 kW. Plan A: un solo generador de 300 kW funciona las 24 horas y consume 90 litros de combustible por hora. "
     "Plan B: dos generadores de 300 kW funcionan juntos las 24 horas, cada uno con una demanda de 135 kW y un consumo de 55 litros por hora cada uno. Criterios de ejemplo: primero, la demanda no debe pasar del 80 % de la capacidad que está en uso; entre los planes que lo cumplen, se prefiere el de menor consumo de combustible.")
build(
    O2, 5, F,
    use="Aprenderé a comparar dos planes de funcionamiento con criterios fijados de antemano y a verificar que el registro cumpla el plan elegido.",
    prior=["Sé calcular demanda, capacidad y reserva.", "Sé calcular un porcentaje simple.", "Sé multiplicar números enteros."],
    explain=[
        "Comparar alternativas es evaluar cada una con los mismos criterios. Un criterio es una regla de decisión. Algunos criterios son obligatorios: si un plan no los cumple, se descarta. Otros sirven para elegir entre los planes que sí cumplen, como el menor consumo de combustible o el menor costo. Se comparan los datos en una tabla, sin mezclar criterios y sin cambiar las reglas al final.",
        "Para verificar la calidad del plan elegido se comprueba que el registro de los instrumentos coincida con él: que funcionen los equipos previstos, que los valores estén en rango y que cada dato quede escrito con su hora. Un ejemplo con otros valores: el plan X consume 40 litros por hora y el plan Y, 30; en 10 horas, X consume 400 litros e Y, 300, pero si Y no cumple el criterio obligatorio, se descarta aunque gaste menos.",
        f"Elegir un plan es una decisión del oficial a cargo; la persona en formación calcula, compara e informa. {EMER} {AVISO}",
    ],
    vocab=[("alternativa", "una de las opciones entre las que se elige"), ("criterio obligatorio", "regla que debe cumplirse; si no, la opción se descarta"), ("criterio de elección", "regla para escoger entre las opciones que cumplen los obligatorios"), ("consumo", "cantidad de combustible que gasta un equipo en un tiempo"), ("verificar la calidad", "comprobar que el registro coincide con el plan elegido")],
    worked=[
        ("Aplicar un criterio obligatorio", "Plan P de ejemplo: demanda 90 kW en un generador de 100 kW; la regla pide no pasar del 80 % de la capacidad. ¿Cumple?", ["El 80 % de 100 kW es 80 kW.", "Una demanda de 90 kW supera 80 kW."], "No cumple y se descarta"),
        ("Elegir entre dos que cumplen", "Dos planes de ejemplo cumplen la regla. El plan R consume 25 litros por hora y el plan S, 20, durante 10 horas. ¿Cuál se elige y cuántos litros gasta?", ["Se prefiere el menor consumo.", "El plan S gasta 20 × 10 litros."], "El plan S, con 200 litros"),
    ],
    mistakes=[("Elegir el plan de menor consumo sin revisar antes el criterio obligatorio.", "Un plan que no cumple la regla obligatoria se descarta aunque consuma menos.", "Aplica primero los criterios obligatorios y después los de elección."),
              ("Cambiar los criterios después de ver los resultados para que gane un plan.", "Los criterios se fijan antes de comparar para que la elección sea justa.", "Escribe los criterios antes de hacer los cálculos.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué es un criterio obligatorio al comparar planes?", "Una regla que debe cumplirse; si no, el plan se descarta", "Un dato que solo se usa para desempatar", "El nombre del plan con menor consumo", "El criterio obligatorio es una condición de entrada; no se elige entre sus incumplidores."),
        ("=", "{F} ¿Cuántos kW es el 80 % de la capacidad de un generador de la ficha?", "300*80//100", "Se calcula el 80 % de la capacidad de un generador.", " kW"),
        ("abc", "{F} ¿Cumple el plan A con el criterio obligatorio de la ficha?", "No, porque 270 kW supera el límite de 240 kW de un solo generador", "Sí, porque 270 kW es menor que 300 kW", "Sí, porque solo hay un generador en uso", "El criterio compara con el 80 % de la capacidad en uso, es decir, 240 kW."),
        ("=", "{F} ¿Cuántos kW es el 80 % de la capacidad de los dos generadores en uso del plan B?", "300*2*80//100", "Se suman las capacidades de los dos generadores y se calcula el 80 %.", " kW"),
        ("abc", "{F} ¿Cumple el plan B con el criterio obligatorio de la ficha?", "Sí, porque 270 kW no supera el límite de 480 kW", "No, porque cada generador pasa de 240 kW", "No, porque usa más de un generador", "La demanda total de 270 kW está bajo el 80 % de la capacidad en uso, que es 480 kW."),
        ("abc", "{F} ¿Cuál plan se elige según los criterios de la ficha?", "El plan B, porque es el único que cumple el criterio obligatorio", "El plan A, porque consume menos por hora", "Ninguno, porque ambos consumen combustible", "El plan A queda descartado por incumplir el criterio obligatorio."),
        ("=", "{F} ¿Cuántos litros consume el plan B en las 24 horas?", "55*2*24", "Se multiplica el consumo por hora de los dos generadores por 24 horas.", " litros"),
        ("=", "{F} ¿Cuántos litros consumiría el plan A en 24 horas?", "90*24", "Se multiplica el consumo por hora por las horas del día.", " litros"),
        ("abc", "{F} Un compañero dice: «el plan A gasta menos litros por día que el B, así que es el mejor». ¿Qué respuesta es correcta?", "Es falso: el plan A incumple el criterio obligatorio y se descarta aunque gaste menos", "Es cierto, porque el menor consumo manda siempre", "Es cierto, porque el plan B usa más equipos", "Los criterios obligatorios se aplican antes del consumo."),
        ("abc", "{F} El registro muestra que, con el plan B, un solo generador está en marcha a las 15:00. ¿Qué corresponde?", "Informar la diferencia con el plan al oficial de máquinas", "Arrancar el segundo generador para cumplir el plan", "Anotar que ambos funcionan", "La diferencia con el plan se informa; arrancar o anotar un dato falso es incorrecto."),
        ("abc", "En Tripulación de Naves: ¿por qué los criterios se fijan antes de comparar los planes?", "Para que la elección sea justa y no cambie según qué plan gane", "Para que todos los planes den el mismo resultado", "Para que los cálculos sean más rápidos", "Fijar los criterios antes evita elegir las reglas para favorecer una opción."),
        ("=", "{F} ¿Cuántos litros más que el plan A consume el plan B en 24 horas?", "55*2*24-90*24", "Se resta el consumo diario del plan A al del plan B.", " litros"),
        ("abc", "{F} Si la demanda bajara a 200 kW y los dos planes cumplieran el criterio obligatorio, ¿cuál se elige?", "El plan A, porque gasta 2.160 litros al día contra 2.640 del plan B", "El plan B, porque usa dos generadores y tiene más reserva", "Los dos por igual, porque cumplen el criterio obligatorio", "Entre planes que cumplen se elige el de menor consumo diario."),
    ],
    ctx=("abc", "En una planilla de ejemplo, un compañero te muestra dos planes y te pide que «elijas el más barato» sin mirar la regla de seguridad. ¿Qué respondes?", "Que primero se aplica el criterio obligatorio de seguridad y después se elige entre los que lo cumplen", "Que se elige el más barato aunque no cumpla la regla", "Que se elige al azar para ahorrar tiempo", "La seguridad es un criterio obligatorio; el costo solo desempata entre los que lo cumplen."),
    sc=[
        ("En Tripulación de Naves: ¿qué se hace primero al comparar planes?", "Se aplican los criterios obligatorios", "Los planes que no cumplen se descartan antes de comparar costos."),
        ("¿Por qué se fijan los criterios antes de comparar?", "Para que la elección sea justa", "Cambiar criterios al final favorece una opción."),
        ("¿Quién decide el plan que se adopta?", "El oficial a cargo", "La persona en formación calcula e informa."),
    ],
    op=("Planes de ejemplo para una demanda de 150 kW. Plan M: un generador de 200 kW, consumo 50 litros por hora. Plan N: dos generadores de 200 kW, consumo de 30 litros por hora cada uno. Criterio obligatorio: la demanda no debe pasar del 80 % de la capacidad en uso. Criterio de elección: menor consumo diario (24 horas). Escribe (a) si cada plan cumple el criterio obligatorio, (b) el consumo diario de cada plan, (c) qué plan se elige, (d) cómo informarías la elección al oficial.",
        "(a) M: el 80 % de 200 kW es 160 kW y 150 kW no lo supera, cumple. N: el 80 % de 400 kW es 320 kW, cumple. (b) M: 50 × 24 = 1.200 litros. N: 30 × 2 × 24 = 1.440 litros. (c) El plan M, porque ambos cumplen y consume menos. (d) «Ambos planes cumplen el criterio de seguridad; el plan M consume 240 litros menos al día».",
        ["aplica el criterio obligatorio a cada plan", "calcula el consumo diario", "elige según el criterio", "informa con la comparación"],
        ["hoja con las cuatro respuestas"],
        ["elegir antes de aplicar el criterio obligatorio", "olvidar multiplicar por los dos generadores", "no calcular las 24 horas"],
        "Pregunta: «¿cuál es la capacidad en uso de cada plan?». Si no responde, pídele que la escriba para cada plan."),
    reinforce="Inventa dos planes con un criterio obligatorio y uno de elección, y escribe cuál se elige.",
    extend="Explica por qué no conviene elegir un plan solo por el costo si no cumple una regla de seguridad.",
)
