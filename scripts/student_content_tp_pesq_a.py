"""Pesquería TP 3.º y 4.º medio: OAE-01 (navegación, conceptos y planificación en papel) y OAE-02 (faenas extractivas, solo conceptos y registros). Todo con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_pesq_common import AVISO, EMER, build

O1 = "TP-PESQ-3y4-OAE-01"
O2 = "TP-PESQ-3y4-OAE-02"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La embarcación ficticia «Nave Demo» sale de una caleta ficticia con 7 personas a bordo, incluido el patrón. "
     "Peligros anotados: cubierta mojada y resbaladiza, bordas bajas, oleaje, niebla que reduce la visibilidad y un cajón cerrado con llave que guarda 4 chalecos de flotación (dato de ejemplo).")
build(
    O1, 1, F,
    use="Aprenderé qué son la navegación, el patrón y la autoridad marítima, cómo se distinguen peligro y riesgo a bordo y cómo se ordenan las medidas de prevención.",
    prior=["Sé leer una ficha escrita y una lista de datos.", "Sé sumar, restar, multiplicar y dividir números enteros.", "Sé que el mar y el tiempo cambian y que eso trae peligros."],
    explain=[
        "Navegar es conducir una embarcación de un punto a otro por el agua. La tripulación es el grupo de personas que trabaja a bordo, y el patrón es la persona responsable de la embarcación y de su tripulación. La autoridad marítima es la institución del Estado que fiscaliza la seguridad de la navegación y de la vida humana en el mar, según la norma vigente. El zarpe es la autorización de salida de una embarcación.",
        "Todo trabajo a bordo tiene peligros, que son fuentes de daño, y riesgos, que son la posibilidad de que ese daño ocurra. La jerarquía de controles ordena la prevención de la más a la menos efectiva: eliminar el peligro, sustituirlo, aplicar controles de ingeniería (cambios físicos de la nave), controles administrativos (reglas, listas de verificación, capacitación) y, al final, el equipo de protección personal (EPP), que incluye el equipo de flotación. El EPP protege a quien lo usa, pero no elimina el peligro.",
        f"También se debe cuidar el ambiente: no se arrojan residuos ni combustible al agua, según la normativa nacional e internacional. {EMER} {AVISO}",
    ],
    vocab=[("embarcación", "construcción flotante usada para navegar"), ("tripulación", "grupo de personas que trabaja a bordo"), ("patrón", "persona responsable de la embarcación y de su tripulación"), ("autoridad marítima", "institución del Estado que fiscaliza la seguridad de la navegación"), ("zarpe", "autorización de salida de una embarcación"), ("peligro", "fuente con capacidad de causar daño"), ("riesgo", "posibilidad de que un peligro cause daño"), ("jerarquía de controles", "orden de las medidas de prevención, de la más a la menos efectiva"), ("EPP", "equipo de protección personal, la última barrera"), ("equipo de flotación", "chaleco u otro elemento que mantiene a flote a una persona")],
    worked=[
        ("Peligro y riesgo", "En una nave de ejemplo hay una abertura en el piso de la cubierta sin tapa. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la abertura sin tapa, porque puede causar daño.", "El riesgo es que una persona caiga por ella y se lastime."], "Peligro: la abertura sin tapa; riesgo: que alguien caiga y se lastime"),
        ("Clasificar un control", "Una nave de ejemplo entrega guantes de trabajo a la tripulación porque un cabo es áspero. ¿A qué nivel de la jerarquía corresponde?", ["Los guantes protegen a quien los usa, pero el cabo sigue siendo áspero.", "Un elemento que lleva puesta la persona es equipo de protección personal."], "Equipo de protección personal (EPP), el último nivel"),
    ],
    mistakes=[("Creer que usar chaleco y botas basta para trabajar seguro en cualquier tarea de a bordo.", "El EPP es la última barrera: no quita el peligro y protege solo a quien lo usa.", "Primero se elimina o se controla el peligro; el EPP se suma a esas medidas."),
              ("Creer que leer una ficha de navegación habilita para conducir una embarcación.", "Navegar exige formación, instructor autorizado y la autorización de la autoridad marítima.", "Aprende aquí el concepto y deja la tarea a personal autorizado.")],
    T=[
        ("abc", "En Pesquería: ¿qué responsabilidad tiene el patrón de una embarcación?", "Es la persona responsable de la embarcación y de su tripulación", "Es el documento que autoriza la salida de la nave", "Es el instrumento que mide la profundidad bajo la nave", "El patrón es una persona con responsabilidad; la autorización es el zarpe y la profundidad se mide con un instrumento."),
        ("abc", "En Pesquería: ¿qué es la autoridad marítima?", "La institución del Estado que fiscaliza la seguridad de la navegación y de la vida humana en el mar", "La organización de pescadores que reparte los turnos de trabajo de una caleta", "La empresa que vende combustible y repuestos a las naves", "La autoridad marítima fiscaliza la seguridad; los turnos y la venta de repuestos son asuntos distintos."),
        ("abc", "En Pesquería: ¿qué es el zarpe?", "La autorización de salida de una embarcación", "El registro de lo capturado durante un viaje", "El plan que fija cuándo se revisa el motor", "El zarpe autoriza salir; la captura y la mantención se anotan en otros documentos."),
        ("=", "{F} Cada persona a bordo debe tener su propio chaleco de flotación. ¿Cuántos chalecos faltan en la nave de ejemplo?", "7-4", "Se resta a las personas a bordo la cantidad de chalecos que hay.", " chalecos"),
        ("abc", "{F} Una pintura antideslizante fija sobre la cubierta, aplicada por personal autorizado, es un control de tipo:", "De ingeniería, porque cambia físicamente la nave", "Administrativo, porque ordena una conducta", "De EPP, porque protege a quien camina", "La superficie modifica la cubierta y no depende de que cada persona lo recuerde."),
        ("abc", "{F} Un cartel que dice «prohibido correr en cubierta» es un control de tipo:", "Administrativo, porque informa y ordena una conducta", "De ingeniería, porque queda fijo en la nave", "De EPP, porque protege a las personas", "Un cartel informa y ordena, pero no cambia la cubierta ni protege el cuerpo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a la niebla?", "Que la visibilidad reducida lleve a un choque con otra nave o un obstáculo", "La niebla misma, que reduce la visibilidad", "Que el oleaje sea siempre más alto cuando hay niebla", "El riesgo es la posibilidad de daño; la niebla es el peligro y el oleaje es otro peligro distinto."),
        ("abc", "{F} Un tripulante propone dejar los chalecos en el cajón cerrado con llave «para que no se pierdan». ¿Qué falla de prevención hay?", "El equipo de flotación debe estar accesible para todas las personas a bordo", "Los chalecos solo los necesita el patrón", "Los chalecos deben guardarse siempre en un lugar cerrado", "Un chaleco guardado bajo llave no puede usarse a tiempo; es un equipo de protección que debe estar disponible."),
        ("abc", "En una visita de ejemplo a un muelle ves que una persona cae al agua. ¿Qué corresponde según las reglas generales?", "No acercarte al borde ni entrar al agua, avisar a un adulto responsable y a emergencias", "Entrar al agua para sacarla lo antes posible", "Tirarle un objeto y alejarte para no estorbar sin avisar a nadie", "Entrar al agua pone en riesgo a otra persona; se avisa de inmediato a quienes pueden actuar."),
        ("abc", "En Pesquería: ¿por qué una lista de verificación antes de salir es un control administrativo y no de ingeniería?", "Porque depende de que las personas la usen y la cumplan, y no cambia físicamente la nave", "Porque solo la puede revisar el patrón", "Porque se escribe en papel y el papel no puede ser un control físico", "Un control administrativo se apoya en conductas y reglas; el de ingeniería modifica el lugar."),
        ("abc", "{F} Para el peligro de la cubierta mojada, ¿qué medida de nivel más efectivo se podría sumar a una regla escrita?", "Una superficie antideslizante fija instalada por personal autorizado", "Otro cartel con la misma advertencia", "Pedir a cada persona que use botas", "La superficie es un control de ingeniería; el cartel es administrativo y las botas son EPP."),
        ("=", "{F} Una regla de ejemplo exige un chaleco por persona más 2 de reserva. ¿Cuántos chalecos debe haber a bordo?", "7+2", "Se suman las personas a bordo y los chalecos de reserva que exige la regla.", " chalecos"),
        ("abc", "{F} Un compañero dice que el chaleco elimina el peligro de caer al agua. ¿Qué corrección es adecuada?", "No evita la caída: reduce el daño si ocurre, y por eso es la última barrera de la jerarquía", "Es cierto, y por eso se omiten los demás controles", "Es cierto solo para el patrón", "El EPP no quita el peligro; se suma a los controles de los niveles anteriores."),
    ],
    ctx=("abc", "Un vecino te invita a salir en su bote un fin de semana, sin chalecos y sin permiso de salida. ¿Qué respondes?", "Que no, porque navegar exige autorización, equipo de flotación y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, porque con buen tiempo basta", "Que sí, siempre que vayas sentado y sin moverte", "El buen tiempo no reemplaza la autorización ni el equipo de flotación."),
    sc=[
        ("En Pesquería: ¿qué diferencia hay entre peligro y riesgo?", "El peligro es la fuente de daño; el riesgo es la posibilidad de que ocurra", "El peligro es la causa; el riesgo mide la posibilidad de daño."),
        ("En pesquería: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
        ("En Pesquería: ¿quién es la persona responsable de la embarcación y su tripulación?", "El patrón", "El patrón responde por la nave y por quienes trabajan a bordo."),
    ],
    op=("La nave ficticia «Nave Demo» anota una tarea de ejemplo: cruzar la cubierta mojada, con la nave en el muelle, para revisar un compartimento. Peligros anotados: piso resbaladizo y bordas bajas. Escribe (a) cuál es el peligro del piso y cuál el riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) por qué el equipo de flotación no basta y quién hace la tarea.",
        "(a) Peligro: piso mojado y resbaladizo; riesgo: que la persona resbale, caiga al agua o al piso y se lastime. (b) Una regla escrita que solo permita el paso con el piso seco y en compañía. (c) Una superficie antideslizante y una baranda fijas instaladas por personal autorizado. (d) El equipo de flotación es la última barrera: reduce el daño, pero no evita la caída; la tarea la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué el equipo de flotación no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer el EPP como único control", "no aclarar que la tarea la hace personal autorizado"],
        "Pregunta: «¿qué control cambia la cubierta y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el nivel de ingeniería."),
    reinforce="Escribe la jerarquía de controles en orden y pon junto a cada nivel un ejemplo inventado de una nave.",
    extend="Explica con un ejemplo por qué una capacitación es un control administrativo y no reemplaza una medida de ingeniería.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (carta de ejemplo, inventada, descrita por escrito). Bahía ficticia: Caleta Demo (punto A); Faro Demo (punto B), a 12 millas náuticas de A, al rumbo 90°; Isla Demo (punto C), a 18 millas náuticas de B, al rumbo 180° medido desde B. "
     "Entre A y B, a 4 millas de A, la carta marca un banco de arena con 2 metros de profundidad. Velocidad de crucero de la nave de ejemplo: 6 nudos. Documentos de ejemplo: la carta náutica, el boletín meteorológico y la bitácora de navegación.")
build(
    O1, 2, F,
    use="Aprenderé a leer una carta náutica descrita por escrito, a usar rumbos, millas y nudos, y a distinguir la carta, el boletín meteorológico y la bitácora de navegación.",
    prior=["Sé qué es el patrón y qué es el zarpe.", "Sé multiplicar y dividir números enteros.", "Sé leer una tabla o una ficha escrita."],
    explain=[
        "La carta náutica es la representación del mar y de la costa que muestra profundidades, peligros como los bancos de arena y ayudas a la navegación como faros y boyas. El rumbo es la dirección de avance, medida en grados desde el norte: 0° es el norte, 90° el este, 180° el sur y 270° el oeste. La derrota es la ruta planificada entre puntos de la carta.",
        "Las distancias en el mar se miden en millas náuticas. El nudo es una unidad de velocidad: una milla náutica recorrida en una hora. Por ejemplo, una nave a 5 nudos recorre 20 millas en 4 horas. El tiempo de un tramo se calcula dividiendo la distancia entre la velocidad. La sonda es la medida de la profundidad del agua.",
        f"Los documentos se usan cada uno para lo suyo. La carta muestra el lugar; el boletín meteorológico entrega el pronóstico del tiempo en el mar; la bitácora de navegación registra horas, rumbos y observaciones del viaje. El patrón decide con esa información. {EMER} {AVISO}",
    ],
    vocab=[("carta náutica", "representación del mar y la costa con profundidades, peligros y ayudas"), ("rumbo", "dirección de avance medida en grados desde el norte"), ("derrota", "ruta planificada entre puntos de la carta"), ("milla náutica", "unidad de distancia usada en el mar"), ("nudo", "velocidad de una milla náutica por hora"), ("sonda", "medida de la profundidad del agua"), ("banco de arena", "zona de poca profundidad marcada en la carta"), ("boletín meteorológico", "documento con el pronóstico del tiempo en el mar"), ("bitácora de navegación", "registro de horas, rumbos y observaciones del viaje")],
    worked=[
        ("Calcular un tiempo", "Una derrota de ejemplo mide 24 millas náuticas y la nave avanza a 8 nudos. ¿Cuánto demora?", ["El tiempo se calcula dividiendo la distancia entre la velocidad.", "24 dividido en 8 es 3."], "3 horas"),
        ("Elegir el documento", "El patrón de una nave de ejemplo quiere saber si mañana habrá viento fuerte en el mar. ¿Qué documento consulta?", ["El viento es un dato del tiempo, no del lugar.", "El pronóstico está en el boletín meteorológico."], "El boletín meteorológico"),
    ],
    mistakes=[("Creer que un nudo es un kilómetro por hora.", "El nudo se mide en millas náuticas por hora, no en kilómetros.", "Usa millas náuticas con nudos."),
              ("Creer que la carta náutica entrega el pronóstico del tiempo.", "La carta muestra el lugar; el tiempo está en el boletín meteorológico.", "Consulta cada documento para lo que fue hecho.")],
    T=[
        ("abc", "En Pesquería: ¿qué muestra una carta náutica?", "Profundidades, peligros y ayudas a la navegación de una zona del mar", "Las horas y los rumbos anotados en cada viaje", "El pronóstico de viento y de oleaje de la semana", "La carta representa el lugar; la bitácora registra el viaje y el boletín da el pronóstico."),
        ("abc", "En Pesquería: ¿qué es un nudo, como unidad de velocidad?", "Una milla náutica recorrida por hora", "Un kilómetro recorrido por hora", "Una vuelta de la hélice por minuto", "El nudo se define con millas náuticas por hora; el kilómetro por hora es otra unidad."),
        ("abc", "En Pesquería: ¿hacia qué punto cardinal apunta el rumbo 270°?", "Oeste", "Este", "Sur", "Con el norte en 0°, el este está en 90°, el sur en 180° y el oeste en 270°."),
        ("=", "{F} ¿Cuántas horas demora la nave en ir de A a B a la velocidad de crucero?", "12//6", "Se divide la distancia entre la velocidad de la nave.", " horas"),
        ("abc", "{F} ¿Qué rumbo tiene la derrota de B a C?", "180°", "90°", "270°", "La ficha indica que C está al rumbo 180° desde B; el 90° es el rumbo de A a B."),
        ("abc", "{F} ¿Qué documento sirve para anotar horas, rumbos y observaciones del viaje?", "La bitácora de navegación", "El boletín meteorológico", "La carta náutica", "La bitácora registra el viaje; el boletín da el pronóstico y la carta muestra el lugar."),
        ("=", "{F} ¿Cuántas millas náuticas tiene la derrota completa de A a B y de B a C?", "12+18", "Se suman las distancias de los dos tramos.", " millas náuticas"),
        ("=", "{F} ¿Cuántas horas demora el tramo de B a C a la velocidad de crucero?", "18//6", "Se divide la distancia del tramo entre la velocidad de crucero.", " horas"),
        ("abc", "{F} ¿Qué indica la carta sobre el tramo de A a B, a 4 millas de A?", "Que hay poca profundidad y la derrota debe revisarse antes de usarla", "Que ahí la profundidad es mayor que en el resto de la bahía", "Que ahí está el faro de la ficha", "Un banco de arena con 2 metros de profundidad es una zona de poca profundidad."),
        ("abc", "{F} Un compañero dice que, para saber si el mar estará tranquilo, basta con mirar la carta náutica. ¿Qué respuesta es correcta?", "Es falso: la carta muestra el lugar, y el pronóstico está en el boletín meteorológico", "Es cierto, porque la carta incluye el pronóstico", "Es cierto si el viaje dura menos de un día", "Cada documento sirve para lo suyo; el tiempo se consulta en el boletín."),
        ("abc", "{F} La bitácora de ejemplo dice: «salida de A a las 9:00; llegada a B a las 12:00». ¿Es coherente con la carta y la velocidad?", "No coincide: a 6 nudos el tramo demora 2 horas; hay que revisar la causa y anotarla sin borrar el registro", "Sí, porque el tramo demora 3 horas", "Sí, porque la bitácora siempre tiene la razón sobre la carta", "A 6 nudos, 12 millas demoran 2 horas; una diferencia se investiga y se informa, no se oculta."),
        ("=", "{F} La nave sale de A a las 8 de la mañana y navega hasta C sin paradas a la velocidad de crucero. ¿A qué hora, en formato de 24 horas, llega a C?", "8+(12+18)//6", "Se suman las distancias, se divide entre la velocidad y se suma a la hora de salida.", " horas"),
        ("abc", "{F} Una estudiante dice: «con la carta de ejemplo ya puedo conducir una nave real». ¿Qué respuesta es correcta?", "Es falso: conducir una nave exige formación, instructor autorizado y autorización de la autoridad marítima", "Es cierto, porque la carta trae toda la información", "Es cierto si la nave es pequeña", "Una carta de ejemplo en papel no habilita para navegar."),
    ],
    ctx=("abc", "En una visita a una caleta, un pescador te ofrece conducir su bote a motor «un ratito», sin chaleco. ¿Qué respondes?", "Que no, porque conducir una embarcación exige formación, autorización y equipo de flotación, y que lo consultarás con un adulto responsable", "Que sí, porque un ratito corto no es peligroso", "Que sí, pero solo si él va a tu lado", "La cercanía de otra persona no reemplaza la formación ni el equipo de flotación."),
    sc=[
        ("En Pesquería: ¿qué es la derrota?", "La ruta planificada entre puntos de la carta", "La derrota es el plan de la ruta antes de navegarla."),
        ("En Pesquería: ¿cómo se calcula el tiempo de un tramo?", "Dividiendo la distancia entre la velocidad", "Con la distancia y la velocidad se obtiene el tiempo."),
        ("¿Qué documento entrega el pronóstico del tiempo en el mar?", "El boletín meteorológico", "El boletín informa sobre el tiempo; la carta muestra el lugar."),
    ],
    op=("Carta de ejemplo: Punto P (puerto ficticio), Punto Q a 20 millas náuticas de P, al rumbo 270°; Punto R a 12 millas náuticas de Q, al rumbo 0°. Velocidad de crucero de ejemplo: 4 nudos. Escribe (a) hacia qué punto cardinal va el primer tramo, (b) cuántas horas demora el tramo de P a Q, (c) cuántas millas tiene la derrota completa, (d) qué documento consultarías para el pronóstico y por qué ese.",
        "(a) Hacia el oeste, porque 270° es el oeste. (b) 20 ÷ 4 = 5 horas. (c) 20 + 12 = 32 millas náuticas. (d) El boletín meteorológico, porque entrega el pronóstico del tiempo en el mar; la carta solo muestra el lugar. La decisión de navegar la toma el patrón con personal autorizado.",
        ["interpreta el rumbo en grados", "calcula el tiempo del tramo", "suma las distancias", "elige el documento correcto con una razón"],
        ["hoja con las cuatro respuestas"],
        ["confundir 270° con el este", "multiplicar en vez de dividir", "decir que la carta trae el pronóstico"],
        "Pregunta: «¿qué documento te dice cómo estará el tiempo?». Si no responde, pídele que relea el tercer párrafo."),
    reinforce="Dibuja un esquema inventado con tres puntos, rumbos y millas, y calcula el tiempo de cada tramo con una velocidad que elijas.",
    extend="Explica con un ejemplo por qué una diferencia entre la bitácora y la carta no se borra, sino que se informa.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (plan de viaje de ejemplo, inventado). Nave Demo: viaje de ida y vuelta entre Caleta Demo y una zona de trabajo a 15 millas náuticas, a 5 nudos. En la zona se anotan 3 horas con el motor a baja potencia. "
     "Consumo de combustible de ejemplo: 8 litros por hora navegando y 4 litros por hora en la zona. Combustible disponible: 100 litros; la regla de ejemplo del armador exige volver con al menos 25 % sin usar. "
     "Boletín de ejemplo: viento de 18 nudos en la tarde; el límite de ejemplo de la nave es 20 nudos. El plan no anota cuántas personas van a bordo.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un plan de viaje escrito: calcular tiempos y consumos, comparar con una reserva y con un límite del tiempo, y detectar datos que faltan.",
    prior=["Sé calcular el tiempo con distancia y velocidad.", "Sé calcular un porcentaje con números enteros.", "Sé qué es la bitácora y el boletín meteorológico."],
    explain=[
        "El plan de viaje es el documento donde se anotan la ruta, los tiempos, las personas a bordo, el combustible estimado, el pronóstico y el plan de emergencia. Analizarlo en papel significa leer los datos, compararlos con lo exigido y decidir si el plan es aceptable. La autonomía es el tiempo o la distancia que la nave puede cumplir con su combustible; la reserva es la parte que no se usa a propósito, por seguridad.",
        "Un margen es la diferencia entre un valor y su límite: si el límite de viento es 25 nudos y el pronóstico es 21, el margen es 4 nudos. Un margen pequeño obliga a vigilar y a informar al patrón. El consumo se calcula multiplicando las horas por los litros por hora. El combustible lo manejan solo personas autorizadas; aquí solo se hacen cuentas en papel.",
        f"Si un dato falta, el plan está incompleto y se corrige antes de salir, no después. Con el pronóstico sobre el límite, la decisión es no salir hasta que el patrón y la norma vigente lo permitan. {EMER} {AVISO}",
    ],
    vocab=[("plan de viaje", "documento con ruta, tiempos, personas a bordo, combustible y plan de emergencia"), ("autonomía", "tiempo o distancia que la nave puede cumplir con su combustible"), ("reserva", "parte del combustible que se deja sin usar por seguridad"), ("margen", "diferencia entre un valor y su límite"), ("consumo", "cantidad de combustible usada en un tiempo"), ("límite de ejemplo", "valor máximo que acepta la nave según la regla de la ficha")],
    worked=[
        ("Calcular un consumo", "Una nave de ejemplo navega 5 horas y consume 6 litros por hora. ¿Cuántos litros usa?", ["El consumo se calcula multiplicando las horas por los litros por hora.", "5 por 6 es 30."], "30 litros"),
        ("Calcular un margen", "El límite de viento de una nave de ejemplo es 30 nudos y el pronóstico dice 22. ¿Cuál es el margen?", ["El margen es la diferencia entre el límite y el valor.", "30 menos 22 es 8."], "8 nudos"),
    ],
    mistakes=[("Completar los datos que faltan en el plan con números inventados para que se vea listo.", "Un plan con datos inventados oculta que falta información importante.", "Se informa lo que falta y se completa con datos reales antes de salir."),
              ("Creer que si el pronóstico queda bajo el límite no hay nada que vigilar.", "Con un margen pequeño, un pequeño cambio del tiempo supera el límite.", "Se informa el margen al patrón y se sigue el pronóstico.")],
    T=[
        ("abc", "En Pesquería: ¿qué es el plan de viaje de una nave?", "El documento con ruta, tiempos, personas a bordo, combustible y plan de emergencia", "El registro de lo capturado después del viaje", "La lista de repuestos que hay en el taller", "El plan de viaje se prepara antes de salir; la captura y los repuestos se registran en otros documentos."),
        ("abc", "En Pesquería: ¿qué es la autonomía de una nave?", "El tiempo o la distancia que puede cumplir con su combustible", "La velocidad máxima del motor", "El número de personas que caben a bordo", "La autonomía depende del combustible disponible, no de la velocidad máxima ni de la capacidad."),
        ("abc", "En Pesquería: ¿qué es un margen frente a un límite del tiempo?", "La diferencia entre el límite y el valor pronosticado", "La suma de todos los valores pronosticados", "El valor más alto registrado en la bitácora", "El margen mide cuánto falta para llegar al límite."),
        ("=", "{F} ¿Cuántas horas navega la nave en total, ida y vuelta, sin contar el tiempo en la zona?", "2*15//5", "Se duplica la distancia, por la ida y la vuelta, y se divide entre la velocidad.", " horas"),
        ("=", "{F} ¿Cuántos litros consume navegando, ida y vuelta, sin contar la zona?", "2*15//5*8", "Se multiplican las horas de navegación por los litros por hora.", " litros"),
        ("=", "{F} ¿Cuántos litros consume en las horas de trabajo en la zona?", "3*4", "Se multiplican las horas en la zona por su consumo por hora.", " litros"),
        ("=", "{F} ¿Cuántos litros puede usar como máximo la nave para respetar la regla de la reserva?", "100-100*25//100", "Se resta del combustible disponible el 25 % que debe quedar sin usar.", " litros"),
        ("=", "{F} ¿Cuántos litros de margen quedan entre el consumo total y el máximo que permite la regla?", "(100-100*25//100)-(2*15//5*8+3*4)", "Se resta el consumo total de los litros máximos permitidos.", " litros"),
        ("abc", "{F} ¿Qué conclusión sobre el viento es adecuada?", "Cumple el límite de ejemplo, pero con un margen de solo 2 nudos: se informa al patrón y se vigila el pronóstico", "No cumple, porque 18 es muy cercano a 20 y por eso se prohíbe", "Cumple con amplio margen, así que no hay que revisar nada más", "18 es menor que 20, pero la diferencia es pequeña y un cambio del tiempo la anularía."),
        ("abc", "{F} El plan no anota cuántas personas van a bordo. ¿Qué corresponde?", "Completarlo antes de salir, porque ese dato sirve para el equipo de flotación y el plan de emergencia", "Nada, porque ese dato solo sirve para pagar a los tripulantes", "Anotarlo después del viaje junto con la captura", "El número de personas determina cuántos chalecos y qué roles de emergencia hacen falta."),
        ("abc", "{F} Por un cambio del tiempo el regreso se retrasa y la nave navega 2 horas más a 8 litros por hora. ¿Se mantiene la regla de la reserva?", "No: usaría 76 litros, más de los 75 que permite la regla", "Sí, porque 76 litros es menos que los 100 disponibles", "Sí, porque la reserva solo se exige al salir", "El consumo total pasa de 60 a 76 litros y supera los 75 permitidos."),
        ("abc", "{F} El boletín cambia y anuncia viento de 24 nudos sobre el límite de ejemplo. ¿Qué corresponde?", "No salir hasta que el patrón y la norma vigente lo permitan", "Salir igual si el viaje es corto", "Salir y volver apenas empeore", "Con el pronóstico sobre el límite, la decisión se toma con datos, no con apuro."),
        ("abc", "{F} Un compañero propone anotar 4 personas a bordo para que el plan «esté completo», sin saber el número real. ¿Qué respondes?", "Que no se inventan datos: se consulta la cantidad real al patrón y se anota", "Que sí, si después se corrige", "Que sí, porque 4 es un número común", "Inventar un dato falsifica el plan y puede dejar a alguien sin chaleco."),
    ],
    ctx=("abc", "Una compañera te propone «ajustar» el consumo anotado en el plan de ejemplo para que no se note que supera la regla. ¿Qué respondes?", "Que no, porque un registro no se altera y que cualquier duda se consulta con el patrón o un adulto responsable", "Que sí, pero solo unos litros", "Que sí, si lo corrigen en el siguiente viaje", "Alterar un dato oculta la realidad, aunque sea poco o temporal."),
    sc=[
        ("En Pesquería: ¿cómo se calcula el consumo de un viaje?", "Multiplicando las horas por los litros por hora", "El consumo depende del tiempo y de cuánto gasta cada hora."),
        ("¿Qué es una reserva de combustible?", "La parte que se deja sin usar por seguridad", "La reserva es un resguardo que no se gasta."),
        ("¿Qué se hace con un dato que falta en el plan?", "Se informa y se completa con el dato real antes de salir", "Un dato inventado oculta el problema."),
    ],
    op=("Plan de ejemplo: nave con ida y vuelta de 24 millas náuticas en total, a 6 nudos, consumo de 7 litros por hora, combustible de 60 litros y reserva exigida de 25 %. El pronóstico anuncia viento de 14 nudos y el límite de ejemplo es 16. Escribe (a) las horas de navegación, (b) los litros consumidos, (c) si cumple la regla de la reserva, (d) el margen de viento y qué harías con él.",
        "(a) 24 ÷ 6 = 4 horas. (b) 4 × 7 = 28 litros. (c) La reserva de 25 % de 60 es 15, así que se pueden usar 45 litros; 28 es menor, por lo que cumple. (d) 16 − 14 = 2 nudos de margen; es pequeño, así que se informa al patrón y se vigila el pronóstico. La decisión final la toma el patrón con la norma vigente.",
        ["calcula las horas", "calcula el consumo", "compara con la reserva", "calcula el margen y propone una acción"],
        ["hoja con las cuatro respuestas"],
        ["olvidar descontar la reserva", "calcular mal el margen", "decidir sin informar al patrón"],
        "Pregunta: «¿cuántos litros se pueden usar y cuántos se usan?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un plan de viaje con distancia, velocidad, consumo y combustible, y calcula si cumple una reserva de 25 %.",
    extend="Explica por qué un margen pequeño de viento obliga a informar al patrón aunque el plan cumpla el límite.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (derrota de ejemplo, inventada). Nave Demo, salida a las 9 de la mañana. Tramo 1: 8 millas náuticas, rumbo 45°, a 4 nudos. Tramo 2: 15 millas, rumbo 135°, a 5 nudos. Tramo 3: 12 millas, rumbo 200°, a 6 nudos. "
     "Hora límite de ejemplo para llegar a puerto: las 18 horas. El tramo 2 cruza una zona donde el boletín de ejemplo anuncia corriente en contra.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar un criterio de planificación: calcular tiempos por tramo, hora de llegada, margen y rumbo inverso con los datos de una derrota de ejemplo.",
    prior=["Sé calcular el tiempo de un tramo con distancia y velocidad.", "Sé que el rumbo se mide en grados desde el norte.", "Sé calcular un margen."],
    explain=[
        "Una derrota se divide en tramos, y cada tramo tiene una distancia, un rumbo y una velocidad. El tiempo de cada tramo es la distancia dividida por la velocidad, y el tiempo total es la suma de los tiempos de los tramos. La hora de llegada es la hora de salida más el tiempo total. El margen frente a una hora límite es la diferencia entre esa hora límite y la hora de llegada.",
        "El rumbo inverso es el rumbo contrario, el que se usaría para volver por el mismo tramo. Se obtiene sumando 180° al rumbo, o restándolos cuando la suma pasa de 360°. Por ejemplo, el rumbo inverso de 60° es 240°. La velocidad media de un viaje es la distancia total dividida por el tiempo total.",
        f"Una corriente en contra reduce la velocidad real de un tramo, así que el plan debe revisarse con ese dato. Cuando el margen es cero o negativo, el plan no es aceptable y se informa al patrón. {EMER} {AVISO}",
    ],
    vocab=[("tramo", "parte de la derrota con un rumbo y una velocidad propios"), ("rumbo inverso", "rumbo contrario, que se obtiene sumando o restando 180°"), ("hora de llegada", "hora de salida más el tiempo total"), ("hora límite", "hora máxima para llegar, fijada por el plan"), ("velocidad media", "distancia total dividida por el tiempo total"), ("corriente", "movimiento del agua que puede ayudar o frenar el avance")],
    worked=[
        ("Tiempo de un tramo", "Un tramo de ejemplo mide 18 millas náuticas y se navega a 6 nudos. ¿Cuánto demora?", ["Se divide la distancia entre la velocidad.", "18 dividido en 6 es 3."], "3 horas"),
        ("Rumbo inverso", "Un tramo de ejemplo tiene rumbo 100°. ¿Cuál es su rumbo inverso?", ["Se suma 180° al rumbo.", "100 más 180 es 280."], "280°"),
    ],
    mistakes=[("Calcular el tiempo de un tramo multiplicando la distancia por la velocidad.", "Multiplicar da un número sin sentido: la unidad no es la hora.", "Se divide la distancia entre la velocidad."),
              ("Obtener el rumbo inverso sumando 90° en vez de 180°.", "El rumbo contrario forma media vuelta, es decir, 180°.", "Suma o resta 180° y deja el resultado entre 0° y 360°.")],
    T=[
        ("abc", "En Pesquería: ¿qué es el rumbo inverso de un tramo?", "El rumbo contrario, que se obtiene sumando o restando 180°", "El rumbo que se obtiene sumando 90°", "La velocidad con la que se regresa", "El rumbo inverso es media vuelta; sumar 90° da un giro de un cuarto."),
        ("abc", "En Pesquería: ¿cómo se obtiene el tiempo de un tramo?", "Dividiendo la distancia entre la velocidad", "Multiplicando la distancia por la velocidad", "Restando la velocidad de la distancia", "Con millas y nudos, el tiempo en horas sale de dividir."),
        ("abc", "En Pesquería: ¿qué es un tramo de una derrota?", "Una parte de la ruta con un rumbo y una velocidad propios", "El tiempo total del viaje", "La hora máxima para llegar", "La derrota se divide en tramos; el tiempo total y la hora límite son otros datos."),
        ("=", "{F} ¿Cuántas millas náuticas tiene la derrota completa?", "8+15+12", "Se suman las distancias de los tres tramos.", " millas náuticas"),
        ("abc", "{F} ¿Cuál es el rumbo inverso del tramo 2?", "315°", "45°", "225°", "135 más 180 es 315; el 45° y el 225° corresponden a otros tramos."),
        ("=", "{F} ¿Cuántas horas demora el viaje completo sumando los tres tramos?", "8//4+15//5+12//6", "Se calcula el tiempo de cada tramo y se suman.", " horas"),
        ("=", "{F} ¿A qué hora, en formato de 24 horas, llega la nave a puerto?", "9+(8//4+15//5+12//6)", "Se suma el tiempo total a la hora de salida.", " horas"),
        ("=", "{F} ¿Cuál es el rumbo inverso del tramo 3, en grados?", "200-180", "Como 200 más 180 pasa de 360, se resta 180.", "°"),
        ("abc", "{F} Un compañero calcula el rumbo inverso del tramo 1 sumando 90° y anota 135°. ¿Qué error cometió?", "Debe sumar 180°, no 90°: el resultado correcto es 225°", "Ninguno: 135° es el rumbo contrario", "Debe restar 180° y anotar −135°", "El rumbo contrario se obtiene con 180°; 45 más 180 es 225."),
        ("abc", "{F} La corriente en contra reduce la velocidad del tramo 2 a 3 nudos. ¿Qué conclusión es correcta?", "Ese tramo demora 5 horas, el viaje llega a las 18 horas y el margen es cero", "Ese tramo demora 3 horas, igual que antes, y llega a las 16 horas", "Ese tramo demora 1 hora, porque la corriente lo acelera", "15 millas a 3 nudos son 5 horas; el viaje dura 2 más 5 más 2, es decir, 9 horas."),
        ("=", "{F} ¿Cuál es el margen, en horas, frente a la hora límite con los datos originales de la ficha?", "18-(9+(8//4+15//5+12//6))", "Se resta la hora de llegada de la hora límite.", " horas"),
        ("=", "{F} ¿Cuál es la velocidad media del viaje completo, en nudos, con los datos originales?", "(8+15+12)//(8//4+15//5+12//6)", "Se divide la distancia total entre el tiempo total.", " nudos"),
        ("abc", "{F} Un compañero propone ahorrar tiempo acortando el tramo 2 por una zona que la carta de ejemplo marca con poca profundidad. ¿Qué corresponde?", "Mantener la derrota y consultar al patrón, porque un atajo por poca profundidad puede ser peligroso", "Tomar el atajo, porque llegar antes mejora el margen", "Tomar el atajo si es de día", "Ahorrar horas no justifica pasar por una zona de poca profundidad."),
    ],
    ctx=("abc", "Alguien te dice que, para recuperar tiempo, una nave de ejemplo podría salir sin revisar el pronóstico. ¿Qué respondes?", "Que no, porque revisar el pronóstico es parte del plan y cualquier duda se consulta con el patrón o un adulto responsable", "Que sí, porque el pronóstico casi nunca cambia", "Que sí, si el viaje es corto", "Saltarse el pronóstico elimina información necesaria para la seguridad."),
    sc=[
        ("En Pesquería: ¿cómo se obtiene la hora de llegada de un viaje?", "Sumando el tiempo total a la hora de salida", "La llegada es la salida más lo que dura el viaje."),
        ("¿Cuál es el rumbo inverso de 90°?", "270°", "El rumbo contrario se obtiene sumando 180 grados: da 270."),
        ("¿Qué significa un margen igual a cero?", "Que se llega justo a la hora límite y el plan debe informarse al patrón", "Sin margen, cualquier retraso incumple el plan."),
    ],
    op=("Derrota de ejemplo: salida a las 7 de la mañana. Tramo 1: 10 millas náuticas, rumbo 30°, a 5 nudos. Tramo 2: 18 millas, rumbo 250°, a 6 nudos. Hora límite de ejemplo: las 16 horas. Escribe (a) el tiempo de cada tramo, (b) la hora de llegada, (c) el margen, (d) el rumbo inverso de cada tramo.",
        "(a) Tramo 1: 10 ÷ 5 = 2 horas; tramo 2: 18 ÷ 6 = 3 horas. (b) 7 + 5 = 12 horas. (c) 16 − 12 = 4 horas de margen. (d) Tramo 1: 30 + 180 = 210°; tramo 2: 250 − 180 = 70°. La decisión de navegar la toma el patrón con personal autorizado.",
        ["calcula los tiempos", "calcula la hora de llegada", "calcula el margen", "obtiene los rumbos inversos"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar en vez de dividir", "sumar 90° para el rumbo inverso", "olvidar la hora de salida"],
        "Pregunta: «¿qué número debes sumar al rumbo para invertirlo?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una derrota de dos tramos y calcula la hora de llegada y los rumbos inversos.",
    extend="Explica por qué una corriente en contra puede dejar un margen en cero aunque la distancia no cambie.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (alternativas y bitácora de ejemplo, inventadas). Derrota A: 28 millas náuticas a 7 nudos, consumo de 10 litros por hora; pasa junto a un banco de arena y por una zona de resguardo ambiental (área marcada donde la norma restringe actividades para proteger el ambiente). "
     "Derrota B: 36 millas a 6 nudos, consumo de 7 litros por hora, por aguas profundas y fuera de toda zona de resguardo. Precio de ejemplo del combustible: 1.000 pesos por litro. "
     "Bitácora de ejemplo: anotación 1, 08:00 salida de Caleta Demo, rumbo 90°, 6 nudos; anotación 2, 10:00 cambio a rumbo 180°; anotación 3, 09:30 pronóstico revisado, viento de 15 nudos. Sin nota aclaratoria y sin firma del patrón.")
build(
    O1, 5, F,
    use="Aprenderé a comparar dos derrotas con criterios de seguridad, norma, ambiente, tiempo y costo, y a verificar la calidad de una bitácora de navegación.",
    prior=["Sé calcular tiempos, consumos y márgenes.", "Sé qué es la bitácora de navegación.", "Sé que no se alteran los registros."],
    explain=[
        "Comparar alternativas es ponerlas lado a lado con los mismos criterios y decidir con ellos. Para dos derrotas los criterios son: la seguridad de las personas y de la nave, el cumplimiento de la norma vigente, el cuidado del ambiente, el tiempo y el costo. La seguridad y la norma van primero: una derrota más barata no se elige si cruza un peligro o una zona de resguardo ambiental.",
        "Verificar la calidad de una bitácora es revisar que esté completa, legible, en orden cronológico, coherente con la carta y las velocidades y firmada por quien corresponde. Un error se corrige con una nota fechada que explique el motivo, y no se borra, no se reescribe ni se arranca la hoja. Una verificación de calidad es la revisión que comprueba que un documento cumple lo exigido.",
        f"Todos los valores de esta clase son de ejemplo para una planilla: los reales dependen de la norma vigente. Quien decide la derrota es el patrón, con la información de la autoridad marítima. {EMER} {AVISO}",
    ],
    vocab=[("criterio", "regla con la que se compara y se decide"), ("zona de resguardo ambiental", "área marcada donde la norma restringe actividades para proteger el ambiente"), ("verificación de calidad", "revisión que comprueba que un documento cumple lo exigido"), ("orden cronológico", "orden según la hora en que ocurrió cada hecho"), ("nota aclaratoria", "anotación fechada que explica un error sin borrarlo"), ("firma del patrón", "constancia de que el patrón revisó y se hace responsable del registro")],
    worked=[
        ("Costo de una alternativa", "Una derrota de ejemplo dura 3 horas y consume 9 litros por hora; el litro cuesta 800 pesos de ejemplo. ¿Cuánto cuesta el combustible?", ["Los litros son 3 por 9, es decir, 27.", "27 por 800 es 21.600."], "21.600 pesos de ejemplo"),
        ("Corregir una anotación", "Una bitácora de ejemplo tiene una hora mal anotada. ¿Qué se hace?", ["No se borra ni se reescribe.", "Se agrega una nota fechada que explica el error."], "Una nota aclaratoria fechada, sin borrar"),
    ],
    mistakes=[("Elegir siempre la derrota más corta y barata.", "El costo y el tiempo son criterios menores frente a la seguridad y la norma.", "Compara primero seguridad y norma; usa costo y tiempo para decidir entre las opciones seguras."),
              ("Borrar una anotación equivocada de la bitácora y escribir encima.", "Un registro alterado pierde su valor como evidencia.", "Deja la anotación y agrega una nota aclaratoria fechada.")],
    T=[
        ("abc", "En Pesquería: al comparar dos derrotas, ¿qué criterio va primero?", "La seguridad de las personas y de la nave", "El menor costo de combustible", "La menor cantidad de horas de viaje", "La seguridad prima sobre el ahorro y el tiempo."),
        ("abc", "En Pesquería: ¿qué es una zona de resguardo ambiental en la carta?", "Un área marcada donde la norma restringe actividades para proteger el ambiente", "Un lugar donde siempre hay boyas de pesca", "El sector de mayor tráfico de naves", "La zona de resguardo protege el ambiente; las boyas y el tráfico son otros datos de la carta."),
        ("abc", "En Pesquería: ¿qué revisa la verificación de calidad de una bitácora?", "Que esté completa, legible, en orden y sin alteraciones", "Que tenga la letra más bonita posible", "Que repita los datos de la bitácora de otra nave", "La calidad se mide por completitud, orden y fidelidad, no por estética ni por copia."),
        ("=", "{F} ¿Cuántas horas demora la derrota A?", "28//7", "Se divide la distancia entre la velocidad.", " horas"),
        ("=", "{F} ¿Cuántas horas demora la derrota B?", "36//6", "Se divide la distancia entre la velocidad.", " horas"),
        ("=", "{F} ¿Cuántos litros consume la derrota A?", "28//7*10", "Se multiplican las horas de la derrota por los litros por hora.", " litros"),
        ("=", "{F} ¿Cuántos litros consume la derrota B?", "36//6*7", "Se multiplican las horas de la derrota por los litros por hora.", " litros"),
        ("=", "{F} ¿Cuántos pesos de ejemplo más cuesta el combustible de la derrota B que el de la A?", "36//6*7*1000-28//7*10*1000", "Se calcula el costo de cada derrota y se restan.", " pesos"),
        ("abc", "{F} ¿Qué derrota conviene y por qué?", "La B: cuesta 2.000 pesos más, pero evita el banco de arena y la zona de resguardo; la seguridad y la norma pesan más que el ahorro", "La A: es más corta y más barata, y eso decide", "La A, porque 4 horas son menos que 6 y el tiempo es el criterio principal", "Una diferencia de costo pequeña no justifica un peligro ni una zona de resguardo."),
        ("abc", "{F} ¿Qué anotación de la bitácora rompe el orden cronológico?", "La anotación 3, porque es de las 09:30 y aparece después de la de las 10:00 sin explicación", "La anotación 1, porque no indica el rumbo de regreso", "La anotación 2, porque cambia de rumbo", "Una hora anterior escrita después de una posterior, sin nota aclaratoria, rompe el orden."),
        ("abc", "{F} ¿Qué corresponde hacer con la anotación fuera de orden?", "Dejarla y agregar una nota fechada que aclare el motivo, sin borrar ni reescribir", "Borrarla y reescribirla en su lugar", "Arrancar la hoja y empezar una nueva", "Un error se explica en una nota; borrar o arrancar altera el registro."),
        ("abc", "{F} Falta la firma del patrón en la hoja. ¿Qué es lo correcto?", "Pedirle al patrón que firme y anotar la omisión; nadie firma por él", "Firmar con su nombre para completar el registro", "Dejarla así, porque la firma no importa si los datos están completos", "La firma es la constancia de responsabilidad del patrón y no se suple."),
        ("abc", "{F} Un compañero propone usar la derrota A y solo «anotar en la bitácora» que no pasó por la zona de resguardo. ¿Qué respondes?", "Que no: falsear un registro es grave y la derrota debe cumplir la norma vigente", "Que sí, porque nadie lo verá", "Que sí, si la nave solo toca el borde de la zona", "Un registro falso oculta un incumplimiento y no cambia la ruta real."),
    ],
    ctx=("abc", "Un conocido te pide que le «arregles» la bitácora de su bote para que las horas calcen con la carta. ¿Qué respondes?", "Que no, porque un registro no se altera, y que cualquier duda se consulta con un adulto responsable o con la autoridad marítima", "Que sí, pero solo las horas más raras", "Que sí, si te paga", "Alterar un registro lo vuelve inservible y puede ser una falta."),
    sc=[
        ("En Pesquería: ¿qué se hace al comparar dos derrotas con costos parecidos?", "Se elige la que cumple mejor la seguridad, la norma y el ambiente", "Con costos parecidos pesan más los criterios de seguridad y norma."),
        ("¿Qué es una nota aclaratoria en una bitácora?", "Una anotación fechada que explica un error sin borrarlo", "La nota conserva el registro original y explica el motivo."),
        ("En Pesquería: ¿quién firma la bitácora de navegación?", "El patrón", "La firma del patrón deja constancia de su responsabilidad."),
    ],
    op=("Alternativas de ejemplo: derrota C, 30 millas náuticas a 5 nudos, consumo de 9 litros por hora, por un tramo con un banco de arena; derrota D, 35 millas a 7 nudos, consumo de 8 litros por hora, por aguas profundas. Precio de ejemplo: 1.000 pesos por litro. Escribe (a) horas y litros de cada derrota, (b) la diferencia de costo, (c) cuál eliges y con qué criterio principal, (d) qué verificarías en la bitácora al llegar.",
        "(a) C: 30 ÷ 5 = 6 horas y 6 × 9 = 54 litros; D: 35 ÷ 7 = 5 horas y 5 × 8 = 40 litros. (b) C cuesta 54.000 pesos y D, 40.000: D cuesta 14.000 pesos menos. (c) D, porque es más barata, más rápida y evita el banco de arena; el criterio principal es la seguridad. (d) Que esté completa, legible, en orden cronológico, sin alteraciones y con la firma del patrón.",
        ["calcula horas y litros", "calcula la diferencia de costo", "elige con la seguridad como criterio", "nombra una verificación de bitácora"],
        ["hoja con las cuatro respuestas"],
        ["elegir solo por costo", "olvidar el banco de arena", "no mencionar la firma ni el orden de la bitácora"],
        "Pregunta: «¿qué derrota evita un peligro y además es más barata?». Si no responde, pídele que compare los dos pesos de la ficha."),
    reinforce="Inventa dos derrotas con distancia, velocidad y consumo, y decide con una tabla de cinco criterios.",
    extend="Explica por qué la firma del patrón en la bitácora no puede hacerla otra persona.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La lancha ficticia «Lancha Demo» sale de «Caleta Demo» con 4 tripulantes a una faena de 12 horas. Regla de ejemplo de descanso: 1 hora de descanso por cada 4 horas de trabajo. "
     "Regla de ejemplo de hidratación: 1 botella de agua potable por persona cada 6 horas. Peligros anotados: cubierta mojada, cabos tensados, un equipo de cubierta con partes en movimiento, poca luz en la madrugada y cansancio por turnos largos.")
build(
    O2, 1, F,
    use="Aprenderé qué es una faena de pesca artesanal o industrial, qué son una veda, una cuota y un área de manejo, y cómo se aplica la jerarquía de controles a los peligros de una faena.",
    prior=["Sé qué son peligro, riesgo y jerarquía de controles.", "Sé qué es el patrón y la autoridad marítima.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Un recurso hidrobiológico es un ser vivo del agua que se puede aprovechar, como un pez, un molusco o un alga. La faena es el conjunto de labores de una jornada de captura, desde la salida hasta el regreso. En términos generales, la pesca artesanal la hacen personas y organizaciones con embarcaciones pequeñas, y la industrial, empresas con naves mayores; las definiciones exactas las fija la norma vigente. El sistema extractivo es el conjunto de arte, embarcación y método con que se captura.",
        "Para cuidar los recursos, la norma vigente usa herramientas como la veda, que es un período o una zona en que se prohíbe capturar un recurso para protegerlo; la cuota, que es la cantidad máxima de captura autorizada; y el área de manejo, que es una zona asignada a una organización de pescadores para que administre un recurso. Respetarlas es parte del trabajo, igual que cuidar el ambiente.",
        f"Una faena tiene peligros: cubierta mojada, equipos con partes en movimiento, cabos tensados, poca luz y fatiga, que es un cansancio que reduce la atención. Se controlan con la jerarquía de controles: protecciones fijas, reglas de descanso y, al final, el EPP, incluido el equipo de flotación. {EMER} {AVISO}",
    ],
    vocab=[("recurso hidrobiológico", "ser vivo del agua que se puede aprovechar"), ("faena", "conjunto de labores de una jornada de captura"), ("sistema extractivo", "conjunto de arte, embarcación y método con que se captura"), ("veda", "período o zona en que se prohíbe capturar un recurso para protegerlo"), ("cuota", "cantidad máxima de captura autorizada"), ("área de manejo", "zona asignada a una organización de pescadores para administrar un recurso"), ("fatiga", "cansancio que reduce la atención"), ("guarda", "protección fija que cubre partes peligrosas de un equipo")],
    worked=[
        ("Peligro y riesgo", "En una faena de ejemplo hay una escalera metálica de acceso a la bodega, mojada y sin pasamanos. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la escalera mojada y sin pasamanos.", "El riesgo es que una persona resbale al bajar y se lastime."], "Peligro: escalera mojada sin pasamanos; riesgo: resbalar y lastimarse"),
        ("Clasificar un control", "Una faena de ejemplo reemplaza un producto de limpieza irritante por otro inofensivo. ¿A qué nivel de la jerarquía corresponde?", ["No se elimina la limpieza, pero se cambia el producto por uno menos dañino.", "Cambiar un peligro por otro menor es sustitución, el segundo nivel."], "Sustitución"),
    ],
    mistakes=[("Creer que quien tiene buenos guantes y chaleco puede acercarse a un equipo con partes en movimiento.", "El EPP no elimina el atrapamiento: solo quien está autorizado y formado trabaja cerca.", "Primero van las guardas y la formación; el EPP se suma."),
              ("Creer que la veda o la cuota son sugerencias que cada pescador decide.", "Son normas vigentes que protegen el recurso y se fiscalizan.", "Se respetan y se consultan con la organización o la autoridad pesquera.")],
    T=[
        ("abc", "En Pesquería: ¿qué es un recurso hidrobiológico?", "Un ser vivo del agua que se puede aprovechar, como un pez, un molusco o un alga", "Una embarcación usada para pescar", "El permiso que autoriza capturar una especie", "El recurso es el organismo; la embarcación y el permiso son otros elementos."),
        ("abc", "En Pesquería: ¿qué es una faena de pesca?", "El conjunto de labores de una jornada de captura, desde la salida hasta el regreso", "El documento que autoriza pescar", "El lugar donde se guardan los equipos en la caleta", "La faena es la jornada de trabajo; el permiso y la bodega son otras cosas."),
        ("abc", "En Pesquería: ¿qué es una veda?", "Un período o una zona en que la norma prohíbe capturar un recurso para protegerlo", "Un permiso para capturar más de lo normal", "El horario en que la pesca rinde más", "La veda protege el recurso prohibiendo capturarlo, no lo promueve."),
        ("=", "{F} ¿Cuántas horas de descanso corresponden en la faena de 12 horas?", "12//4", "Se divide el total de horas entre las horas de trabajo por cada descanso.", " horas"),
        ("abc", "{F} Una guarda fija que cubre las partes en movimiento del equipo de cubierta, instalada por personal autorizado, es un control de tipo:", "De ingeniería, porque cambia físicamente el equipo", "Administrativo, porque ordena una conducta", "De EPP, porque protege a quien se acerca", "La guarda modifica el equipo y no depende de que alguien recuerde una regla."),
        ("abc", "{F} La regla de descanso por cada cuatro horas de trabajo es un control de tipo:", "Administrativo, porque ordena los turnos", "De ingeniería, porque cambia la nave", "De sustitución, porque cambia el equipo", "Una regla de turnos ordena una conducta y no modifica la nave ni el equipo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a los cabos tensados en la cubierta?", "Que un cabo se suelte o se rompa y golpee a una persona", "El cabo tensado mismo, que es la fuente del daño", "Que el cabo se moje y pese más", "El riesgo es la posibilidad de daño; el cabo tensado es el peligro y el peso extra es un problema menor."),
        ("abc", "{F} Un compañero dice: «con un buen chaleco y guantes puedo acercarme al equipo con partes en movimiento». ¿Qué respuesta es correcta?", "Es falso: el EPP no elimina el atrapamiento y solo personal autorizado trabaja cerca del equipo", "Es cierto, si el equipo se mueve despacio", "Es cierto, si otra persona lo mira", "Ni el chaleco ni los guantes quitan el peligro de atrapamiento."),
        ("abc", "En una visita de ejemplo al muelle ves que un tripulante queda atrapado por un equipo de cubierta. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a apagar el equipo tú mismo", "Tirar de la persona para sacarla rápido", "Intervenir sin formación puede causar más daño; se avisa a quienes pueden actuar."),
        ("abc", "En Pesquería: ¿por qué la fatiga es un peligro durante una faena?", "Porque el cansancio reduce la atención y aumenta la posibilidad de errores y accidentes", "Porque el cansancio solo disminuye la captura, no la seguridad", "Porque la fatiga se elimina por completo con un chaleco", "La fatiga afecta la seguridad y no se corrige con un EPP."),
        ("abc", "{F} Para el peligro de la poca luz en la madrugada, ¿qué medida de nivel más efectivo se podría sumar a una regla escrita?", "Iluminación fija en la cubierta instalada por personal autorizado", "Otro recordatorio escrito en el plan de viaje", "Pedir a cada tripulante que se acostumbre a la oscuridad", "La iluminación fija es un control de ingeniería; el recordatorio es administrativo y acostumbrarse no es una medida."),
        ("=", "{F} ¿Cuántas botellas de agua potable deben llevarse para los 4 tripulantes en toda la faena de 12 horas?", "4*12//6", "Se multiplica el número de personas por las veces que se necesita una botella.", " botellas"),
        ("abc", "{F} Una estudiante dice: «leí la ficha, así que puedo salir con mi tío a una faena». ¿Qué respuesta es correcta?", "Es falso: una faena exige formación, autorización y norma vigente, y este cuaderno no habilita para trabajar", "Es cierto, si lleva chaleco", "Es cierto, si va solo de acompañante", "Leer una ficha no habilita para trabajar; el chaleco tampoco reemplaza la autorización."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por «ayudar con la red» en su lancha un sábado, sin capacitación ni chaleco. ¿Qué respondes?", "Que no, porque esa tarea exige instructor autorizado, equipo de flotación y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, porque un sábado no es peligroso", "Que sí, si él te enseña en el momento", "Una enseñanza improvisada no reemplaza la formación ni el equipo de flotación."),
    sc=[
        ("En Pesquería: ¿qué es una cuota de captura?", "La cantidad máxima de captura autorizada", "La cuota fija un límite para proteger el recurso."),
        ("En Pesquería: ¿qué es un área de manejo?", "Una zona asignada a una organización de pescadores para administrar un recurso", "El área de manejo se asigna a una organización según la norma."),
        ("En pesquería: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
    ],
    op=("«Lancha Demo» anota una tarea de ejemplo: trabajar en la cubierta al amanecer, con piso mojado y un equipo con partes en movimiento, después de 10 horas seguidas sin descanso. Escribe (a) un peligro y su riesgo, (b) un control de ingeniería, (c) un control administrativo, (d) por qué el EPP no basta y quién hace la tarea.",
        "(a) Peligro: equipo con partes en movimiento; riesgo: atrapamiento. También sirve el piso mojado (riesgo de resbalar) o la fatiga (riesgo de error). (b) Una guarda fija sobre el equipo o una superficie antideslizante, instaladas por personal autorizado. (c) Una regla de descanso por turnos y un horario de trabajo con luz suficiente. (d) El EPP es la última barrera y no quita el peligro; la tarea la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control de ingeniería", "propone un control administrativo", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer solo el EPP", "no aclarar que la tarea la hace personal autorizado"],
        "Pregunta: «¿qué control cambia el equipo y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el último párrafo."),
    reinforce="Escribe tres peligros de una faena inventada y, para cada uno, un control de un nivel distinto de la jerarquía.",
    extend="Explica con un ejemplo por qué una veda protege al recurso y también a quienes viven de él.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (tabla de ejemplo, inventada). Tres sistemas de captura de ejemplo, con la captura de una faena cada uno. Arte X: 900 kg de la especie buscada (especie A) y 100 kg de otras especies. "
     "Arte Y: 700 kg de especie A y 300 kg de otras especies. Arte Z (una trampa): 380 kg de especie A y 20 kg de otras especies. Documento de ejemplo: la bitácora de pesca.")
build(
    O2, 2, F,
    use="Aprenderé el vocabulario de los sistemas extractivos y de las artes de pesca, qué es la selectividad y la captura incidental, y qué documentos y roles intervienen en una faena.",
    prior=["Sé qué es una faena, una veda y una cuota.", "Sé calcular un porcentaje con números enteros.", "Sé leer una tabla escrita."],
    explain=[
        "Un arte de pesca es el dispositivo con que se captura un recurso. Algunos tipos, descritos solo por su idea general, son: la red de cerco, que rodea un grupo de peces; la red de arrastre, que se desplaza por el agua; la red de enmalle, que queda extendida y retiene peces por su tamaño; el espinel, una línea larga con muchos anzuelos; y la trampa, una estructura que atrae y retiene organismos. También existe la recolección manual de algunos recursos.",
        "La selectividad es la capacidad de un arte de capturar principalmente la especie y las tallas buscadas. La captura incidental es la captura de especies o tallas que no se buscaban. El porcentaje de selectividad se calcula como la captura de la especie buscada por 100, dividida por la captura total. Por ejemplo, un arte que captura 160 kg de la especie buscada y 40 kg de otras tiene 80 % de selectividad.",
        f"En la faena se usa la bitácora de pesca, el registro de cada faena con el arte, la zona, las horas y lo capturado. Intervienen el patrón de pesca, que dirige la faena; los tripulantes, que cumplen funciones asignadas; y el encargado del registro, que anota los datos. {EMER} {AVISO}",
    ],
    vocab=[("arte de pesca", "dispositivo con que se captura un recurso"), ("red de cerco", "red que rodea un grupo de peces"), ("red de enmalle", "red que queda extendida y retiene peces por su tamaño"), ("espinel", "línea larga con muchos anzuelos"), ("trampa", "estructura que atrae y retiene organismos"), ("selectividad", "capacidad de capturar principalmente lo buscado"), ("captura incidental", "captura de especies o tallas no buscadas"), ("bitácora de pesca", "registro de cada faena con arte, zona, horas y captura"), ("patrón de pesca", "persona que dirige la faena")],
    worked=[
        ("Calcular selectividad", "Un arte de ejemplo capturó 340 kg de la especie buscada y 60 kg de otras especies. ¿Qué porcentaje es la especie buscada?", ["La captura total es 340 más 60, es decir, 400 kg.", "340 por 100 dividido entre 400 es 85."], "85 %"),
        ("Elegir el documento", "Una organización de ejemplo quiere saber qué arte se usó y cuántas horas duró una faena. ¿Qué documento consulta?", ["Esos datos son propios de cada faena.", "Se anotan en la bitácora de pesca."], "La bitácora de pesca"),
    ],
    mistakes=[("Creer que el arte que captura más kilos es siempre el más selectivo.", "La selectividad mide qué parte de la captura es la buscada, no los kilos totales.", "Calcula el porcentaje de la especie buscada sobre la captura total."),
              ("Creer que conocer los tipos de arte en este cuaderno permite usarlos.", "Usar un arte exige formación, instructor autorizado y la norma vigente.", "Aprende aquí el vocabulario y deja el uso a personal autorizado.")],
    T=[
        ("abc", "En Pesquería: ¿qué es un arte de pesca?", "Un dispositivo con que se captura un recurso, como una red, un espinel o una trampa", "El permiso para pescar una especie", "La zona donde está permitido pescar", "El arte es el dispositivo de captura; el permiso y la zona son otras cosas."),
        ("abc", "En Pesquería: ¿qué es la selectividad de un arte?", "La capacidad de capturar principalmente la especie y las tallas buscadas", "La cantidad de kilos que captura en total", "La velocidad con que se usa el arte", "La selectividad se refiere a qué se captura, no a cuánto ni a qué rapidez."),
        ("abc", "En Pesquería: ¿qué es la captura incidental?", "La captura de especies o tallas que no se buscaban", "La captura que supera la cuota de ejemplo", "La captura anotada sin firma", "Lo incidental es lo no buscado; superar la cuota o faltar la firma son otros problemas."),
        ("=", "{F} ¿Qué porcentaje de la captura del arte X es especie A?", "900*100//(900+100)", "Se multiplica la especie buscada por 100 y se divide entre la captura total.", " %"),
        ("=", "{F} ¿Qué porcentaje de la captura del arte Y es especie A?", "700*100//(700+300)", "Se multiplica la especie buscada por 100 y se divide entre la captura total.", " %"),
        ("abc", "{F} ¿Qué arte de la ficha es el más selectivo?", "El arte Z, con 95 % de especie A", "El arte X, con 90 % de especie A", "El arte Y, con 70 % de especie A", "Z tiene el mayor porcentaje de la especie buscada, aunque capture menos kilos."),
        ("=", "{F} ¿Cuántos kilos de captura incidental sumaron el arte X y el arte Y?", "100+300", "Se suman los kilos de otras especies de ambos artes.", " kg"),
        ("abc", "{F} ¿Qué conclusión es correcta sobre el arte Y?", "El 30 % de su captura no es la especie buscada: es menos selectivo que X y que Z", "Es el más selectivo, porque capturó muchos kilos de otras especies", "Es igual de selectivo que X, porque ambos capturaron más de 600 kg", "Un 30 % de captura incidental es mayor que el de los otros dos."),
        ("abc", "{F} ¿Qué documento registra, faena por faena, qué arte se usó, cuánto se capturó y de qué especies?", "La bitácora de pesca", "La carta náutica", "El plan de viaje", "La bitácora de pesca anota la faena; la carta muestra el lugar y el plan organiza el viaje."),
        ("abc", "{F} Un compañero dice que la trampa Z es peor que el arte X porque captura menos kilos. ¿Qué respuesta es correcta?", "Los kilos no miden la selectividad: Z tiene mayor porcentaje de especie A, aunque haya que mirar también otros criterios", "Es cierto, porque capturar menos siempre es peor", "Es cierto, porque la trampa no es un arte de pesca", "La comparación de selectividad se hace con porcentajes, no con kilos totales."),
        ("abc", "{F} ¿Por qué el arte con más captura incidental puede ser un problema para los recursos?", "Porque captura individuos de otras especies o tallas que no se buscaban y afecta su conservación", "Porque llena la bodega y deja menos espacio", "Porque el arte siempre pesa más que los demás", "La captura incidental puede dañar poblaciones que no se pretendía extraer."),
        ("=", "{F} Si el arte X hubiera capturado 1.500 kg de especie A y 500 kg de otras, ¿qué porcentaje habría sido especie A?", "1500*100//(1500+500)", "Se divide la especie buscada entre la captura total y se multiplica por 100.", " %"),
        ("abc", "{F} Un compañero propone anotar la captura incidental del arte Y como «especie A» para mejorar su selectividad en el registro. ¿Qué respondes?", "Que no: el registro debe reflejar lo realmente capturado, sin alterarlo", "Que sí, si el total no cambia", "Que sí, porque son peces de todos modos", "Alterar la especie falsea los datos que se usan para cuidar el recurso."),
    ],
    ctx=("abc", "En una caleta, alguien te ofrece mostrarte «cómo se maneja» una red de enmalle en un bote, sin chaleco. ¿Qué respondes?", "Que no, porque usar un arte exige formación, equipo de flotación y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, porque solo mirarás", "Que sí, si el bote está atracado", "Estar cerca de un equipo en uso ya implica riesgo sin formación ni equipo de flotación."),
    sc=[
        ("En Pesquería: ¿cómo se calcula el porcentaje de selectividad?", "Captura de la especie buscada por 100, dividida por la captura total", "La selectividad compara lo buscado con el total capturado."),
        ("En Pesquería: ¿qué es un espinel?", "Una línea larga con muchos anzuelos", "El espinel es un arte basado en una línea con anzuelos."),
        ("En Pesquería: ¿qué rol dirige la faena de pesca?", "El patrón de pesca", "El patrón de pesca conduce la faena y responde por ella."),
    ],
    op=("Tabla de ejemplo: arte P, 450 kg de especie A y 50 kg de otras especies; arte Q, 240 kg de especie A y 160 kg de otras; arte R, 570 kg de especie A y 30 kg de otras. Escribe (a) el porcentaje de especie A de cada arte, (b) cuál es el más selectivo y cuál el menos, (c) en qué documento se anota cada faena, (d) por qué no se altera lo anotado.",
        "(a) P: 450 × 100 ÷ 500 = 90 %; Q: 240 × 100 ÷ 400 = 60 %; R: 570 × 100 ÷ 600 = 95 %. (b) El más selectivo es R y el menos selectivo es Q. (c) En la bitácora de pesca. (d) Porque un registro alterado falsea los datos con que se cuida el recurso y se pierde la trazabilidad. Usar los artes lo hace personal autorizado.",
        ["calcula tres porcentajes", "identifica el más y el menos selectivo", "nombra la bitácora de pesca", "explica por qué no se altera el registro"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre la captura buscada y no entre la total", "elegir el arte con más kilos", "decir que el registro se puede ajustar"],
        "Pregunta: «¿entre qué número divides para obtener el porcentaje?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa tres artes con captura de la especie buscada y de otras, y calcula cuál es el más selectivo.",
    extend="Explica con un ejemplo por qué un arte muy selectivo puede capturar pocos kilos y seguir siendo una buena opción.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (seguimiento de ejemplo, inventado). La organización ficticia «Organización Demo» tiene un área de manejo para la especie A con una cuota de ejemplo de 14.000 kg para la temporada. "
     "Capturas del mes 1 al mes 4: 2.500 kg, 3.100 kg, 2.900 kg y 2.700 kg. La veda de ejemplo comienza en el mes 6. Muestra de tallas de ejemplo: de 50 ejemplares medidos, 8 están bajo la talla mínima de ejemplo. "
     "Regla de ejemplo: si más de un 20 % de la muestra está bajo la talla mínima, se informa a la organización y a la autoridad pesquera.")
build(
    O2, 3, F,
    use="Aprenderé a analizar el seguimiento de una cuota: acumulado, saldo y porcentaje de uso, y a revisar una muestra de tallas contra la talla mínima, con datos de ejemplo.",
    prior=["Sé qué son la veda, la cuota y el área de manejo.", "Sé calcular un porcentaje con números enteros.", "Sé sumar y restar números enteros."],
    explain=[
        "El seguimiento de una cuota se hace con el acumulado, que es la suma de lo capturado hasta hoy, y el saldo, que es la cuota menos el acumulado, es decir, lo que todavía se puede capturar. El porcentaje de uso es el acumulado por 100 dividido por la cuota. Capturar más que la cuota es un incumplimiento de la norma vigente, y una veda no amplía la cuota ni la reemplaza.",
        "La talla mínima es el tamaño bajo el cual la norma no permite retener un ejemplar. Para revisarla se mide una muestra, que es un grupo pequeño de ejemplares que representa al total. El porcentaje bajo talla es la cantidad de ejemplares bajo la talla mínima por 100, dividida por el tamaño de la muestra. Si pasa de un límite fijado, se informa a la organización y a la autoridad pesquera.",
        f"Estos datos los anotan personas autorizadas y formadas, con registros que no se alteran. Por ejemplo, con una cuota de 5.000 kg y 1.000 kg capturados, el saldo es 4.000 kg y el porcentaje de uso es 20 %. {EMER} {AVISO}",
    ],
    vocab=[("acumulado", "suma de lo capturado hasta hoy"), ("saldo", "cuota menos acumulado: lo que todavía se puede capturar"), ("porcentaje de uso", "acumulado por 100 dividido por la cuota"), ("talla mínima", "tamaño bajo el cual no se permite retener un ejemplar"), ("muestra", "grupo pequeño de ejemplares que representa al total"), ("porcentaje bajo talla", "ejemplares bajo la talla mínima por 100, dividido por la muestra")],
    worked=[
        ("Calcular un saldo", "Una cuota de ejemplo es de 8.000 kg y el acumulado es de 6.000 kg. ¿Cuál es el saldo?", ["El saldo es la cuota menos el acumulado.", "8.000 menos 6.000 es 2.000."], "2.000 kg"),
        ("Porcentaje bajo talla", "En una muestra de ejemplo de 40 ejemplares, 6 están bajo la talla mínima. ¿Qué porcentaje es?", ["Se multiplica 6 por 100: 600.", "600 dividido en 40 es 15."], "15 %"),
    ],
    mistakes=[("Creer que cuando empieza una veda se puede capturar lo que falte de la cuota antes de que termine.", "La cuota es un máximo y la veda no la amplía.", "Se respeta el saldo; lo que sobra no se compensa con más captura."),
              ("Redondear hacia abajo un porcentaje bajo talla para no pasar el límite.", "Alterar un dato oculta el problema.", "Se anota el dato real y se informa según la regla.")],
    T=[
        ("abc", "En Pesquería: ¿qué es el saldo de una cuota?", "Lo que todavía se puede capturar: la cuota menos el acumulado", "Lo capturado hasta hoy", "El precio de lo capturado", "El saldo mide lo que queda; lo ya capturado es el acumulado."),
        ("abc", "En Pesquería: ¿qué es la talla mínima?", "El tamaño bajo el cual la norma no permite retener un ejemplar", "El tamaño medio de todos los ejemplares capturados", "El peso que debe tener la captura de un día", "La talla mínima es un límite de tamaño por ejemplar."),
        ("abc", "En Pesquería: ¿para qué sirve una muestra de tallas?", "Para revisar, con un grupo pequeño, cómo es el tamaño de las capturas", "Para reemplazar el registro de las capturas de otra faena", "Para fijar el precio de venta", "La muestra representa al total sin medir cada ejemplar."),
        ("=", "{F} ¿Cuántos kilos acumulados hay entre el mes 1 y el mes 4?", "2500+3100+2900+2700", "Se suman las capturas de los cuatro meses.", " kg"),
        ("=", "{F} ¿Cuál es el saldo de la cuota después del mes 4?", "14000-(2500+3100+2900+2700)", "Se resta de la cuota la suma de las capturas.", " kg"),
        ("=", "{F} ¿Qué porcentaje de la cuota se ha usado después del mes 4?", "(2500+3100+2900+2700)*100//14000", "Se multiplica el acumulado por 100 y se divide entre la cuota.", " %"),
        ("=", "{F} ¿Qué porcentaje de la muestra de tallas está bajo la talla mínima?", "8*100//50", "Se multiplican los ejemplares bajo talla por 100 y se dividen entre la muestra.", " %"),
        ("abc", "{F} Con el porcentaje bajo talla de la muestra, ¿qué corresponde según la regla de ejemplo?", "No supera el 20 %, así que se registra y se sigue vigilando", "Informar a la autoridad, porque 16 está cerca de 20", "No registrar nada, porque la muestra es pequeña", "La regla pide informar solo si el porcentaje pasa de 20; igual se registra."),
        ("=", "{F} ¿Cuántos kilos se capturaron en promedio por mes entre los meses 1 y 4?", "(2500+3100+2900+2700)//4", "Se divide el acumulado entre el número de meses.", " kg"),
        ("abc", "{F} Si en el mes 5 se captura lo mismo que el promedio mensual, ¿qué pasa con el saldo?", "Se agota exactamente: no queda margen para ningún error y hay que informar al patrón y a la organización", "Sobra la mitad del saldo", "Se excede la cuota en 200 kg", "El promedio de 2.800 kg es igual al saldo de 2.800 kg."),
        ("abc", "{F} Un compañero propone capturar 3.000 kg en el mes 5 «porque la veda empieza en el mes 6». ¿Qué respondes?", "Que no: excedería la cuota en 200 kg, y la veda no amplía la cuota", "Que sí, porque la veda compensa el exceso", "Que sí, si lo anotan como captura del mes 6", "El saldo es de 2.800 kg, así que 3.000 kg lo superan."),
        ("=", "{F} Si en el mes 5 se capturan 2.400 kg, ¿cuántos kilos del saldo quedan sin usar?", "14000-(2500+3100+2900+2700)-2400", "Se resta al saldo lo capturado en el mes 5.", " kg"),
        ("abc", "{F} Un ejemplar medido está bajo la talla mínima. ¿Qué dice la regla general?", "No se retiene, según la norma vigente, y se registra como captura bajo talla", "Se retiene si es el último del día", "Se retiene si nadie fiscaliza", "La talla mínima protege a los ejemplares jóvenes y se respeta siempre."),
    ],
    ctx=("abc", "Un dirigente de ejemplo te pide anotar 2.800 kg en vez de 3.000 kg en el mes 5 para «no pasarse» de la cuota. ¿Qué respondes?", "Que no, porque un registro no se altera, y que cualquier duda se consulta con un adulto responsable o con la autoridad pesquera", "Que sí, solo por esta vez", "Que sí, si se compensa el mes siguiente", "Falsear un dato oculta un incumplimiento y daña al recurso."),
    sc=[
        ("En Pesquería: ¿cómo se calcula el saldo de una cuota?", "Cuota menos acumulado", "El saldo es lo que queda de la cuota."),
        ("En Pesquería: ¿una veda amplía la cuota?", "No, la veda no amplía la cuota", "La veda es una protección distinta de la cuota."),
        ("En Pesquería: ¿qué es un porcentaje bajo talla?", "Los ejemplares bajo la talla mínima por 100, dividido por la muestra", "Mide qué parte de la muestra está bajo la talla."),
    ],
    op=("Seguimiento de ejemplo: cuota de la especie B de 9.000 kg; capturas de 2.000, 2.500 y 1.500 kg en tres meses; en una muestra de 40 ejemplares, 12 están bajo la talla mínima de ejemplo. La regla de ejemplo pide informar si pasa de 20 %. Escribe (a) el acumulado y el saldo, (b) si el acumulado está por encima o por debajo de la mitad de la cuota y por cuántos kilos, (c) el porcentaje bajo talla y qué corresponde hacer, (d) por qué no se altera el registro.",
        "(a) Acumulado: 2.000 + 2.500 + 1.500 = 6.000 kg; saldo: 9.000 − 6.000 = 3.000 kg. (b) La mitad de la cuota son 4.500 kg y ya se capturaron 6.000 kg, así que se superó la mitad por 1.500 kg. (c) 12 × 100 ÷ 40 = 30 %, que pasa de 20 %, así que se informa a la organización y a la autoridad pesquera. (d) Porque un registro alterado oculta el problema y se pierde la trazabilidad.",
        ["calcula acumulado y saldo", "compara con la mitad de la cuota", "calcula el porcentaje bajo talla y decide", "explica por qué no se altera el registro"],
        ["hoja con las cuatro respuestas"],
        ["olvidar restar el acumulado", "dividir entre la cuota para el bajo talla", "no informar al pasar el límite"],
        "Pregunta: «¿entre qué número divides para obtener el porcentaje bajo talla?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una cuota con cuatro capturas mensuales y calcula el acumulado, el saldo y el porcentaje de uso.",
    extend="Explica por qué medir una muestra permite decidir sin medir cada ejemplar capturado.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (registro de ejemplo, inventado). «Lancha Demo», especie A, tres faenas. Faena 1: 6 horas y 900 kg. Faena 2: 8 horas y 960 kg. Faena 3: 5 horas y 800 kg. "
     "Precio de ejemplo: 1.200 pesos por kilo. Costo variable de ejemplo: 25.000 pesos por hora de faena. Regla de ejemplo: ninguna faena puede pasar de 6 horas, por la fatiga.")
build(
    O2, 4, F,
    use="Aprenderé a calcular la captura por unidad de esfuerzo, el ingreso, el costo y el margen de una faena con datos de ejemplo, y a considerar también la seguridad.",
    prior=["Sé qué es una faena y la fatiga.", "Sé multiplicar, dividir, sumar y restar números enteros.", "Sé leer una tabla escrita."],
    explain=[
        "El esfuerzo de pesca es la medida del trabajo dedicado a capturar, por ejemplo las horas de faena. La captura por unidad de esfuerzo, o CPUE, es la captura dividida por el esfuerzo; con kilos y horas se mide en kilos por hora. Una CPUE alta indica que se captura más por cada hora de trabajo. Los científicos la usan junto con otros datos para seguir el estado de un recurso.",
        "El ingreso es lo que se obtiene por vender: kilos por precio. El costo es lo que se gasta. El margen económico es el ingreso menos el costo. El margen por hora es el margen dividido por las horas. Por ejemplo, una faena de 4 horas con ingreso de 500.000 pesos y costo de 320.000 pesos deja un margen de 180.000 pesos.",
        f"Un buen número económico no basta para decidir: la regla de seguridad, como el límite de horas por fatiga, va primero. Todos los precios y costos de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("esfuerzo de pesca", "medida del trabajo dedicado a capturar, como las horas de faena"), ("CPUE", "captura por unidad de esfuerzo: captura dividida por esfuerzo"), ("ingreso", "kilos vendidos por precio"), ("costo variable", "gasto que depende de las horas de faena"), ("margen económico", "ingreso menos costo"), ("margen por hora", "margen dividido por las horas de faena")],
    worked=[
        ("Calcular una CPUE", "Una faena de ejemplo captura 480 kg en 4 horas. ¿Cuál es la CPUE?", ["La CPUE es la captura dividida por las horas.", "480 dividido en 4 es 120."], "120 kg por hora"),
        ("Calcular un margen", "Una faena de ejemplo tiene un ingreso de 640.000 pesos y un costo de 410.000 pesos. ¿Cuál es el margen?", ["El margen es el ingreso menos el costo.", "640.000 menos 410.000 es 230.000."], "230.000 pesos"),
    ],
    mistakes=[("Elegir siempre la faena con el mayor margen total sin mirar las horas.", "Un margen alto con muchas horas puede romper la regla de seguridad y cansar a la tripulación.", "Compara también el margen por hora, la CPUE y el límite de horas."),
              ("Creer que la CPUE sube cuando se capturan más kilos en más horas.", "Si crecen los kilos y las horas en la misma proporción, la CPUE no mejora.", "Divide siempre la captura entre el esfuerzo.")],
    T=[
        ("abc", "En Pesquería: ¿qué es la CPUE?", "La captura dividida por el esfuerzo de pesca, por ejemplo kilos por hora", "El precio de venta por kilo", "El costo total de una faena", "La CPUE mide la captura por esfuerzo; el precio y el costo son otros datos."),
        ("abc", "En Pesquería: ¿qué es el esfuerzo de pesca?", "La medida del trabajo dedicado a capturar, como las horas de faena", "El peso total de la captura", "El número de especies capturadas", "El esfuerzo mide el trabajo, no el resultado."),
        ("abc", "En Pesquería: ¿qué es el margen económico de una faena?", "El ingreso menos el costo", "El ingreso más el costo", "El costo dividido por las horas", "El margen es lo que queda después de restar los costos."),
        ("=", "{F} ¿Cuál es la CPUE de la faena 1?", "900//6", "Se divide la captura entre las horas de la faena.", " kg por hora"),
        ("=", "{F} ¿Cuál es la CPUE de la faena 2?", "960//8", "Se divide la captura entre las horas de la faena.", " kg por hora"),
        ("=", "{F} ¿Cuál es el ingreso de la faena 3?", "800*1200", "Se multiplican los kilos por el precio de ejemplo.", " pesos"),
        ("=", "{F} ¿Cuál es el costo de la faena 2?", "8*25000", "Se multiplican las horas por el costo por hora.", " pesos"),
        ("=", "{F} ¿Cuál es el margen de la faena 2?", "960*1200-8*25000", "Se resta el costo del ingreso de la faena.", " pesos"),
        ("=", "{F} ¿Cuál es el margen por hora de la faena 3?", "(800*1200-5*25000)//5", "Se calcula el margen y se divide entre las horas.", " pesos"),
        ("abc", "{F} ¿Qué faena tiene el mayor margen total?", "La faena 2, con 952.000 pesos", "La faena 1, con 930.000 pesos", "La faena 3, con 835.000 pesos", "El margen total de la faena 2 supera al de las otras dos."),
        ("abc", "{F} Un compañero dice que la faena 2 es la mejor porque tiene el mayor margen total. ¿Qué observación es adecuada?", "Tiene el menor margen por hora y la menor CPUE, y además pasa del límite de horas por fatiga", "Es la mejor, porque el margen total es el único criterio", "Es la peor, porque tiene más horas y por eso pierde dinero", "Pierde en eficiencia por hora y no cumple la regla de seguridad, aunque su margen total sea alto."),
        ("=", "{F} Si el precio de ejemplo bajara a 1.000 pesos por kilo, ¿cuál sería el margen de la faena 1?", "900*1000-6*25000", "Se calcula el ingreso con el precio nuevo y se resta el costo.", " pesos"),
        ("abc", "{F} Según la regla de ejemplo del límite de horas, ¿qué faena no cumple?", "La faena 2, porque dura 8 horas", "La faena 1, porque dura exactamente 6 horas", "La faena 3, porque tiene menos horas que las demás", "Solo la faena 2 supera las 6 horas; 6 horas cumple el límite."),
    ],
    ctx=("abc", "Un armador de ejemplo te dice que, como la faena de 8 horas deja más plata, hay que alargar todas las faenas aunque la tripulación esté cansada. ¿Qué respondes?", "Que la seguridad va primero: el límite de horas por fatiga se respeta, y cualquier duda se consulta con un adulto responsable o la autoridad marítima", "Que sí, porque la plata decide", "Que sí, si el equipo toma más café", "La fatiga aumenta el riesgo de accidentes, y el ahorro económico no lo compensa."),
    sc=[
        ("En Pesquería: ¿cómo se calcula la CPUE con kilos y horas?", "Kilos divididos por horas", "La CPUE relaciona lo capturado con el trabajo dedicado."),
        ("En Pesquería: ¿cómo se calcula el margen económico?", "Ingreso menos costo", "El margen es lo que queda tras pagar los costos."),
        ("¿Qué criterio va primero al elegir una faena?", "La seguridad y la norma", "La seguridad y la norma pesan más que el margen."),
    ],
    op=("Registro de ejemplo: faena P, 5 horas y 700 kg; faena Q, 6 horas y 720 kg. Precio de ejemplo: 1.500 pesos por kilo; costo de ejemplo: 30.000 pesos por hora; límite de ejemplo: 6 horas. Escribe (a) la CPUE de cada faena, (b) el margen de cada una, (c) cuál tiene mejor margen por hora, (d) si ambas cumplen el límite de horas.",
        "(a) P: 700 ÷ 5 = 140 kg por hora; Q: 720 ÷ 6 = 120 kg por hora. (b) P: 700 × 1.500 − 5 × 30.000 = 900.000 pesos; Q: 720 × 1.500 − 6 × 30.000 = 900.000 pesos. (c) P: 900.000 ÷ 5 = 180.000; Q: 900.000 ÷ 6 = 150.000; mejor la P. (d) Sí: ambas están dentro de las 6 horas.",
        ["calcula la CPUE", "calcula los márgenes", "compara márgenes por hora", "verifica el límite de horas"],
        ["hoja con las cuatro respuestas"],
        ["no restar el costo", "dividir las horas entre la captura", "no verificar el límite de horas"],
        "Pregunta: «¿qué debes restar al ingreso para obtener el margen?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa dos faenas con horas y kilos, y calcula la CPUE y el margen por hora de cada una.",
    extend="Explica con un ejemplo por qué dos faenas con el mismo margen total pueden tener márgenes por hora distintos.",
)

# ============================================================ OAE-02, clase 5
F = ("Ficha 5 (alternativas y registro de ejemplo, inventados). Alternativa 1, una red de enmalle: 540 kg de especie A y 60 kg de otras especies, costo de la faena de 108.000 pesos de ejemplo, 6 horas. "
     "Alternativa 2, un espinel: 490 kg de especie A y 10 kg de otras especies, costo de 147.000 pesos de ejemplo, 9 horas. Regla de ejemplo: ninguna faena pasa de 8 horas. "
     "Registro de la alternativa 1: especie A 540 kg, otras especies 60 kg, total anotado 580 kg, área anotada «sector norte» (el área de manejo autorizada de ejemplo es «sector sur»), sin firma del patrón.")
build(
    O2, 5, F,
    use="Aprenderé a comparar dos sistemas extractivos con criterios de selectividad, costo, horas y norma, y a verificar la calidad de un registro de captura.",
    prior=["Sé calcular selectividad, CPUE y margen.", "Sé qué es un área de manejo y una cuota.", "Sé que los registros no se alteran."],
    explain=[
        "Para comparar dos sistemas extractivos se usan los mismos criterios: el cumplimiento de la norma y de las reglas de seguridad, la selectividad, el costo por kilo de la especie buscada, las horas de faena y el impacto en el ambiente. El costo por kilo es el costo de la faena dividido por los kilos de la especie buscada. Una alternativa que no cumple la norma o la regla de seguridad se descarta aunque sea más barata.",
        "Verificar un registro de captura es comprobar que esté completo, que los números cuadren, que el área sea la autorizada y que lleve la firma del responsable. La conciliación es comparar dos fuentes de un mismo dato, por ejemplo la suma por especie y el total anotado. Si hay diferencias, se informan con evidencia, sin cambiar los números, y se aclaran con una nota fechada.",
        f"Estos cálculos son de ejemplo. Elegir un sistema extractivo en la práctica corresponde a personas autorizadas, con la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("costo por kilo", "costo de la faena dividido por los kilos de la especie buscada"), ("conciliación", "comparación de dos fuentes de un mismo dato para ver si cuadran"), ("verificación de un registro", "comprobación de que está completo, cuadra y cumple lo exigido"), ("área autorizada", "zona donde la norma permite capturar"), ("incumplimiento", "hecho que no cumple la norma vigente")],
    worked=[
        ("Costo por kilo", "Una faena de ejemplo costó 90.000 pesos y capturó 300 kg de la especie buscada. ¿Cuál es el costo por kilo?", ["Se divide el costo entre los kilos de la especie buscada.", "90.000 dividido en 300 es 300."], "300 pesos por kilo"),
        ("Conciliar un total", "Un registro de ejemplo anota 200 kg de especie A y 30 kg de especie B, con un total de 230 kg. ¿Cuadra?", ["La suma por especie es 200 más 30, que es 230.", "El total anotado es 230, igual a la suma."], "Sí, cuadra"),
    ],
    mistakes=[("Elegir la alternativa más barata sin revisar las horas ni el área.", "Una alternativa que rompe una regla de seguridad o de la norma se descarta primero.", "Aplica primero las reglas y luego compara costos."),
              ("Cambiar el total anotado para que coincida con la suma.", "Alterar un número oculta el error original.", "Se informa la diferencia y se agrega una nota aclaratoria fechada.")],
    T=[
        ("abc", "En Pesquería: al comparar dos sistemas extractivos, ¿qué criterio va primero?", "El cumplimiento de la norma y de las reglas de seguridad", "El menor costo por kilo", "La mayor captura total", "Una alternativa que no cumple la norma se descarta aunque sea barata."),
        ("abc", "En Pesquería: ¿qué es el costo por kilo de una faena?", "El costo de la faena dividido por los kilos de la especie buscada", "El precio al que se vende cada kilo", "El costo de la faena multiplicado por las horas", "El costo por kilo relaciona el gasto con lo obtenido."),
        ("abc", "En Pesquería: ¿qué es la conciliación de un registro de captura?", "Comparar dos fuentes de un mismo dato para ver si cuadran", "Borrar las anotaciones repetidas", "Cambiar los totales para que se parezcan", "La conciliación detecta diferencias; no las corrige alterando datos."),
        ("=", "{F} ¿Cuál es el costo por kilo de especie A de la alternativa 1?", "108000//540", "Se divide el costo de la faena entre los kilos de especie A.", " pesos por kilo"),
        ("=", "{F} ¿Cuál es el costo por kilo de especie A de la alternativa 2?", "147000//490", "Se divide el costo de la faena entre los kilos de especie A.", " pesos por kilo"),
        ("=", "{F} ¿Qué porcentaje de la captura de la alternativa 1 es especie A?", "540*100//(540+60)", "Se divide la especie A entre la captura total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje de la captura de la alternativa 2 es especie A?", "490*100//(490+10)", "Se divide la especie A entre la captura total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué alternativa conviene según la regla de ejemplo de horas y el costo por kilo?", "La alternativa 1: cuesta menos por kilo y cumple el límite de 8 horas", "La alternativa 2, porque es más selectiva y eso decide aunque dure 9 horas", "Ninguna, porque las dos tienen captura incidental", "La alternativa 2 dura 9 horas y no cumple la regla; la 1 cumple y es más barata por kilo."),
        ("=", "{F} ¿Cuántos kilos de diferencia hay entre la suma de las especies y el total anotado en el registro de la alternativa 1?", "540+60-580", "Se resta el total anotado de la suma real por especie.", " kg"),
        ("abc", "{F} ¿Qué corresponde hacer con esa diferencia entre la suma y el total anotado?", "Informarla con el registro como evidencia y aclararla con una nota fechada, sin cambiar los números", "Cambiar el total anotado a 600 sin avisar", "Esperar a que el patrón la corrija solo en otra faena", "Una diferencia se informa y se aclara; cambiarla en silencio altera el registro."),
        ("abc", "{F} El área anotada es «sector norte» y la autorizada de ejemplo es «sector sur». ¿Qué corresponde?", "Informar de inmediato la diferencia sin modificar el registro, porque podría ser un incumplimiento que decide la autoridad", "Anotar «sector sur» para que coincida", "Dejarlo así, porque el nombre del sector no importa", "Cambiar el área oculta un posible incumplimiento y no lo corrige."),
        ("=", "{F} ¿Cuántos pesos de ejemplo más habría costado obtener los 540 kg de especie A con el costo por kilo de la alternativa 2?", "(147000//490-108000//540)*540", "Se multiplica la diferencia de costo por kilo por los kilos de especie A.", " pesos"),
        ("abc", "{F} Falta la firma del patrón en el registro. ¿Qué es lo correcto?", "Pedirle al patrón que revise y firme, y anotar la omisión; nadie firma por él", "Firmar con su nombre para completar el registro", "Dejar el registro sin firma porque los datos están completos", "La firma es la constancia de responsabilidad del patrón y no se suple."),
    ],
    ctx=("abc", "Un conocido te pide «arreglar» un registro de captura para que el área y el total calcen antes de una fiscalización. ¿Qué respondes?", "Que no, porque un registro no se altera, y que cualquier duda se consulta con un adulto responsable o con la autoridad pesquera", "Que sí, pero solo el total", "Que sí, si lo corrige después", "Alterar un registro es una falta y oculta el problema real."),
    sc=[
        ("En Pesquería: ¿cómo se calcula el costo por kilo?", "Costo de la faena dividido por los kilos de la especie buscada", "El costo por kilo relaciona el gasto con lo obtenido."),
        ("En Pesquería: ¿qué se hace cuando un registro no cuadra?", "Se informa la diferencia con evidencia y se aclara con una nota fechada", "Un registro que no cuadra se aclara sin alterar los datos."),
        ("En Pesquería: ¿qué pasa con una alternativa que no cumple la norma?", "Se descarta aunque sea más barata", "La norma pesa más que el costo."),
    ],
    op=("Alternativas de ejemplo: alternativa M, 300 kg de especie A y 20 kg de otras, costo de 90.000 pesos, 7 horas; alternativa N, 250 kg de especie A y 10 kg de otras, costo de 100.000 pesos, 9 horas. Límite de ejemplo: 8 horas. Registro de M: especie A 300 kg, otras 20 kg, total anotado 330 kg, con firma del patrón. Escribe (a) el costo por kilo de cada una, (b) cuál elegirías y por qué, (c) si el registro de M cuadra, (d) qué haces con una diferencia.",
        "(a) M: 90.000 ÷ 300 = 300 pesos por kilo; N: 100.000 ÷ 250 = 400 pesos por kilo. (b) M, porque es más barata por kilo y cumple el límite de 8 horas; N dura 9 horas y no lo cumple. (c) No cuadra: 300 + 20 = 320 kg, y el total anotado es 330 kg, 10 kg de diferencia. (d) Se informa con el registro como evidencia y se aclara con una nota fechada, sin cambiar los números.",
        ["calcula el costo por kilo", "elige aplicando la regla de horas", "detecta la diferencia del registro", "describe cómo se informa"],
        ["hoja con las cuatro respuestas"],
        ["elegir solo por selectividad", "no descartar la alternativa de 9 horas", "corregir el total sin avisar"],
        "Pregunta: «¿qué alternativa pasa el límite de horas?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos alternativas con costo, kilos y horas, descarta la que rompe una regla y compara las que quedan.",
    extend="Explica por qué la conciliación entre la suma por especie y el total ayuda a cuidar el recurso.",
)
