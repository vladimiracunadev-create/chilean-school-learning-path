"""Mecánica Industrial, mención Matricería, 4.º medio: OAM-01 (matrices: partes, documentos, compatibilidad con la prensa y cálculo), OAM-02 (moldes de inyección: partes, fichas, compatibilidad con la inyectora y cálculo) y OAM-03 (detección de fallas y control de calidad en papel). Todo en papel, con datos de ejemplo; sin procedimientos de montaje, desmontaje ni operación."""
from __future__ import annotations

from tp_mema_common import AVISO, EMER, build

O1 = "TP-MEMA-4-OAM-01"
O2 = "TP-MEMA-4-OAM-02"
O3 = "TP-MEMA-4-OAM-03"

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Taller Demo de Matricería» fabrica matrices, que son herramientas que dan forma a una chapa metálica en una prensa, una máquina que aplica una gran fuerza. Matriz M-01 de ejemplo: corta un disco de una chapa. "
     "Partes: punzón (pieza superior que empuja), matriz hembra (pieza inferior con el hueco), placa guía, columnas guía, resortes y extractor (pieza que suelta la chapa). Peligros anotados: aplastamiento al cerrarse la prensa, piezas muy pesadas, bordes filosos, energía almacenada en resortes y en el sistema hidráulico, ruido y aceite en el piso.")
build(
    O1, 1, F,
    use="Aprenderé qué es una matriz y una prensa, sus partes principales, sus peligros y los controles generales que protegen a las personas, sin montar ni operar nada.",
    prior=["Sé qué es una máquina-herramienta.", "Sé qué es un resguardo y la jerarquía de controles.", "Sé qué es la energía almacenada."],
    explain=[
        "Una matriz es una herramienta que da forma a una chapa o a otro material cuando una prensa la cierra con fuerza. Hay matrices de corte, que separan una pieza; de doblado, que doblan la chapa, y de embutición, que forman piezas huecas. Sus partes básicas son el punzón, que empuja desde arriba; la matriz hembra, con el hueco; las columnas y la placa guía, que alinean las piezas; los resortes y el extractor, que sueltan la chapa.",
        "El peligro principal es el aplastamiento cuando la prensa cierra, además de las cargas pesadas, los bordes filosos y la energía almacenada en resortes e hidráulica. Los controles incluyen resguardos o cortinas de luz que detienen la prensa si se invade la zona, mandos que obligan a usar ambas manos fuera de la zona de peligro, bloqueo y etiquetado, y orden y limpieza. El EPP es la última barrera.",
        f"Montar, ajustar y operar una matriz exige personal autorizado e instructor; este cuaderno no enseña a hacerlo. {EMER} {AVISO}",
    ],
    vocab=[("matriz", "herramienta que da forma a una chapa cuando una prensa la cierra"), ("prensa", "máquina que aplica una gran fuerza para cerrar una matriz"), ("punzón", "pieza superior de la matriz que empuja la chapa"), ("matriz hembra", "pieza inferior de la matriz con el hueco"), ("extractor", "pieza que suelta la chapa de la matriz"), ("cortina de luz", "dispositivo que detiene la prensa si algo invade la zona de peligro")],
    worked=[
        ("Nombrar la parte", "En una matriz de ejemplo, la pieza superior empuja la chapa hacia el hueco. ¿Cómo se llama?", ["Es la pieza que empuja desde arriba.", "Se llama punzón."], "El punzón"),
        ("Clasificar un control", "Una prensa de ejemplo se detiene sola si una mano invade la zona de peligro. ¿Qué tipo de control es?", ["Es un dispositivo que actúa sin depender de la conducta.", "Es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Creer que una prensa detenida ya no tiene peligro.", "Pueden quedar resortes o presión hidráulica con energía almacenada.", "Considera siempre las energías almacenadas y el bloqueo y etiquetado de la empresa."),
              ("Pensar que leer sobre matrices habilita para montarlas.", "El montaje exige personal autorizado e instructor.", "Aprende el concepto y deja la tarea a quien está autorizado.")],
    T=[
        ("abc", "En Matricería: ¿qué es una matriz?", "Una herramienta que da forma a una chapa cuando una prensa la cierra", "Una máquina que aplica una gran fuerza", "Un instrumento que mide el espesor de la chapa", "La matriz es la herramienta; la prensa es la máquina."),
        ("abc", "En Matricería: ¿qué hace el punzón de una matriz?", "Empuja la chapa desde arriba hacia el hueco", "Sostiene la chapa por debajo", "Suelta la chapa después del corte", "El punzón es la pieza superior que empuja."),
        ("abc", "En Matricería: ¿qué es una cortina de luz?", "Un dispositivo que detiene la prensa si algo invade la zona de peligro", "Una cubierta que tapa la matriz", "Una luz que ilumina el piso", "La cortina de luz protege sin depender de la conducta."),
        ("abc", "{F} ¿Qué parte de la matriz M-01 suelta la chapa?", "El extractor", "El punzón", "La placa guía", "El extractor retira la chapa de la matriz."),
        ("abc", "{F} ¿Cuál es el peligro principal de la prensa de la ficha?", "El aplastamiento al cerrarse", "El ruido de la oficina", "El color de la chapa", "Al cerrar, la prensa puede aplastar cualquier cosa en la zona."),
        ("abc", "{F} Los resortes de la matriz representan un peligro de:", "Energía almacenada", "Radiación", "Humos", "Un resorte comprimido guarda energía que puede liberarse."),
        ("=", "{F} El taller tiene 3 prensas y cada una requiere 2 personas durante la prueba de una matriz. ¿Cuántas personas se necesitan?", "3*2", "Se multiplican las prensas por las personas de cada una.", " personas"),
        ("=", "{F} Cada prensa retira 20 kg de recortes de chapa al día. ¿Cuántos kg retiran las 3 prensas en 5 días?", "3*20*5", "Se multiplican las prensas, los kg por día y los días.", " kg"),
        ("abc", "{F} Una barrera que impide acercar las manos a la zona de cierre es un control:", "De ingeniería", "Administrativo", "De EPP", "La barrera cambia físicamente el lugar."),
        ("abc", "{F} Un aprendiz dice: «la prensa está apagada, así que puedo meter la mano a ajustar la chapa». ¿Qué respuesta es correcta?", "Es falso: puede quedar energía almacenada, y solo personal autorizado, con bloqueo y etiquetado, interviene", "Es cierto, porque apagada no se mueve", "Es cierto, si usa guantes", "En este caso, apagada no significa sin energía."),
        ("abc", "En una visita a un taller de ejemplo, una mano queda atrapada al cerrarse una prensa. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar abrir la matriz tú mismo", "Jalar el brazo de la persona", "Intervenir sin formación puede causar otra lesión."),
        ("=", "{F} Si la matriz M-01 tiene 2 columnas guía y 4 resortes, ¿cuántas de estas piezas lleva en total?", "2+4", "Se suman las columnas y los resortes.", " piezas"),
        ("abc", "En Matricería: ¿qué se hace con el aceite usado y los trapos con aceite?", "Se almacenan en recipientes rotulados y se gestionan según la norma vigente", "Se botan a la basura común", "Se vierten al desagüe", "En este caso, son residuos que requieren gestión."),
    ],
    ctx=("abc", "Un amigo de ejemplo te dice: «el taller del colegio tiene una prensa, probemos con una chapa». ¿Qué respondes?", "Que no, porque usar una prensa exige instructor autorizado y norma vigente, y que consultarás a un adulto responsable", "Que sí, con guantes", "Que sí, si lo hacemos despacio", "Este cuaderno no habilita para operar prensas."),
    sc=[
        ("En Matricería: ¿qué es una prensa?", "Una máquina que aplica una gran fuerza para cerrar una matriz", "La prensa mueve la matriz y le da la fuerza."),
        ("En Matricería: ¿cuál es el peligro principal de cerrar una prensa?", "El aplastamiento", "Cualquier parte del cuerpo en la zona puede ser aplastada."),
        ("En Matricería: ¿quién puede intervenir una matriz?", "Personal autorizado con instructor", "El trabajo exige formación y norma vigente."),
    ],
    op=("Ficha de ejemplo: una matriz de doblado ficticia en una prensa con resguardo y cortina de luz. Partes: punzón, matriz hembra, columnas, resortes. Peligros: aplastamiento, bordes filosos y energía almacenada. Escribe (a) qué parte empuja la chapa, (b) un control de ingeniería, (c) un control administrativo, (d) por qué una prensa detenida puede seguir teniendo energía. No describas cómo se monta.",
        "(a) El punzón. (b) La cortina de luz o el resguardo. (c) El bloqueo y etiquetado y la regla de que solo personal autorizado interviene. (d) Porque pueden quedar resortes comprimidos o presión hidráulica con energía almacenada.",
        ["nombra el punzón", "propone un control de ingeniería", "propone un control administrativo", "explica la energía almacenada"],
        ["hoja con las cuatro respuestas"],
        ["decir que detenida es sin energía", "proponer solo EPP", "describir cómo se monta"],
        "Pregunta: «¿qué pieza empuja la chapa?». Si duda, pídele que relea las partes de la matriz."),
    reinforce="Escribe cuatro partes de una matriz con una frase de lo que hace cada una.",
    extend="Explica con un ejemplo por qué una cortina de luz protege mejor que un cartel de advertencia.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (plano y datos de ejemplo, descritos por escrito, inventados). Matriz de corte M-02 para un disco de 50 mm de diámetro en chapa de 2 mm de espesor. Lista de piezas: 1 punzón, 1 matriz hembra, 1 placa guía, 2 columnas, 4 resortes, 1 extractor. "
     "Altura cerrada de la matriz (cuando está cerrada): 180 mm. Fuerza de corte de ejemplo: perímetro de corte × espesor × resistencia al corte de ejemplo (300 N por mm²); en N. Perímetro del disco de 50 mm de diámetro, para el ejemplo: 150 mm. "
     "Prensas del taller (datos de ejemplo): prensa P1, fuerza máxima 100 kN, altura de cierre admitida 150 a 200 mm; prensa P2, fuerza máxima 200 kN, altura de cierre admitida 220 a 300 mm. 1 kN son 1.000 N. Ficha de la matriz: historial de golpes y mantenciones.")
build(
    O1, 2, F,
    use="Aprenderé a leer una lista de piezas y una ficha de matriz, a calcular una fuerza de corte de ejemplo y a comprobar si una matriz es compatible con una prensa, solo en papel.",
    prior=["Sé qué es una matriz y una prensa.", "Sé multiplicar enteros.", "Sé comparar números."],
    explain=[
        "El plano de conjunto de una matriz incluye su lista de piezas, con las cantidades, y datos como la altura cerrada, que es la altura de la matriz cuando está cerrada. La ficha de la matriz guarda su historial: cuántos golpes ha dado y qué mantenciones tuvo. Una prensa tiene una fuerza máxima y una altura de cierre admitida, el rango de alturas de matriz que puede recibir.",
        "Para que una matriz sea compatible con una prensa, la fuerza máxima de la prensa debe ser mayor que la fuerza necesaria, con un margen, y la altura cerrada de la matriz debe quedar dentro de la altura de cierre admitida. En el ejemplo, la fuerza de corte se calcula como perímetro por espesor por resistencia al corte, en newtons (N); 1 kN son 1.000 N. Estos valores son de ejemplo y los reales dependen del material y del fabricante.",
        f"Solo se leen documentos y se calcula en papel. {EMER} {AVISO}",
    ],
    vocab=[("altura cerrada", "altura de la matriz cuando está cerrada"), ("altura de cierre admitida", "rango de alturas de matriz que una prensa puede recibir"), ("fuerza máxima de la prensa", "mayor fuerza que la prensa puede aplicar"), ("fuerza de corte", "fuerza necesaria para cortar una chapa"), ("ficha de la matriz", "documento con el historial de golpes y mantenciones")],
    worked=[
        ("Calcular una fuerza", "Un corte de ejemplo tiene perímetro 100 mm, espesor 1 mm y resistencia de 200 N por mm². ¿Cuántos N se necesitan?", ["Se multiplican 100, 1 y 200.", "El resultado es 20.000 N."], "20.000 N"),
        ("Compatibilidad de altura", "Una matriz de ejemplo mide 250 mm cerrada y una prensa admite de 200 a 260 mm. ¿Es compatible en altura?", ["250 está entre 200 y 260.", "Sí, entra en el rango."], "Sí"),
    ],
    mistakes=[("Elegir una prensa solo por su fuerza.", "También debe calzar la altura de cierre.", "Comprueba fuerza y altura."),
              ("Usar la fuerza justa sin margen.", "Cualquier variación del material puede superarla.", "Elige una fuerza máxima con margen sobre la necesaria.")],
    T=[
        ("abc", "En Matricería: ¿qué es la altura cerrada de una matriz?", "La altura de la matriz cuando está cerrada", "La altura de la prensa completa", "El espesor de la chapa", "La altura cerrada se compara con la altura de cierre de la prensa."),
        ("abc", "En Matricería: ¿qué guarda la ficha de una matriz?", "Su historial de golpes y mantenciones", "El precio de venta", "El plano de la prensa", "La ficha registra la vida de la matriz."),
        ("abc", "En Matricería: ¿qué es la altura de cierre admitida de una prensa?", "El rango de alturas de matriz que puede recibir", "La altura del taller", "La fuerza máxima de la prensa", "Es el rango compatible con la prensa."),
        ("=", "{F} ¿Cuántas piezas suma la lista de piezas de la matriz M-02?", "1+1+1+2+4+1", "Se suman las cantidades de las seis piezas.", " piezas"),
        ("=", "{F} ¿Cuántos N de fuerza de corte necesita el disco, con perímetro 150 mm, espesor 2 mm y 300 N por mm²?", "150*2*300", "Se multiplican el perímetro, el espesor y la resistencia al corte.", " N"),
        ("=", "{F} ¿Cuántos kN son 90.000 N?", "90000//1000", "Se divide entre 1.000.", " kN"),
        ("abc", "{F} ¿Qué prensa admite la altura cerrada de 180 mm?", "La P1, que admite de 150 a 200 mm", "La P2, que admite de 220 a 300 mm", "Ninguna", "180 está dentro del rango de P1."),
        ("abc", "{F} Con 90 kN de fuerza necesaria, ¿qué prensa tiene fuerza suficiente?", "Ambas, pero P1 queda con poco margen", "Solo P1", "Solo P2 y con margen enorme", "P1 llega a 100 kN y P2 a 200 kN; P1 tiene solo 10 kN de margen."),
        ("=", "{F} ¿Cuántos kN de margen tiene P1 sobre la fuerza necesaria de 90 kN?", "100-90", "Se resta la fuerza necesaria a la máxima.", " kN"),
        ("abc", "{F} Un jefe dice: «usemos la P2 porque es la más fuerte». ¿Qué respuesta es correcta?", "No corresponde: la altura cerrada de 180 mm no entra en el rango de P2, que es de 220 a 300 mm", "Corresponde, porque tiene más fuerza", "Corresponde, si baja la velocidad", "La altura de cierre también debe calzar."),
        ("abc", "{F} Un compañero dice: «la matriz entra en la P1 y la fuerza alcanza justo; no hace falta margen». ¿Qué respuesta es correcta?", "Es incorrecto: conviene un margen, porque el material real puede ser más resistente", "Es correcto, si alcanza justo", "Es correcto, si la chapa es nueva", "Un margen cubre variaciones del material."),
        ("=", "{F} Para el mismo disco, con una chapa de 3 mm de espesor, ¿cuántos N de fuerza se necesitan?", "150*3*300", "Se multiplican el perímetro, el nuevo espesor y la resistencia al corte.", " N"),
        ("Una matriz de ejemplo mide 320 mm cerrada y hay prensas que admiten de 150 a 200 mm y de 220 a 300 mm. ¿Alguna es compatible en altura?", "Ninguna", "320 supera el máximo de ambas."),
    ],
    ctx=("abc", "El pañolero de ejemplo dice: «la matriz entra en esa prensa, la fuerza no importa». ¿Qué propones?", "Comprobar fuerza con margen y altura de cierre antes de aceptar la compatibilidad", "Aceptarlo si entra físicamente", "Comprobar solo la altura", "La compatibilidad exige fuerza y altura."),
    sc=[
        ("En Matricería: ¿cuántos newtons son 90 kN?", "90.000 N", "En este caso, Un kN son 1.000 N."),
        ("En Matricería: ¿qué dos datos se comparan para la compatibilidad con la prensa?", "La fuerza necesaria y la altura cerrada", "Ambos deben calzar con la prensa."),
        ("En Matricería: ¿qué conviene dejar entre la fuerza necesaria y la de la prensa?", "Un margen", "En este caso, cubre variaciones del material."),
    ],
    op=("Ficha de ejemplo: matriz de corte para un disco de 40 mm (perímetro de ejemplo 120 mm) en chapa de 2 mm, resistencia 250 N por mm². Altura cerrada 200 mm. Prensas: PA, fuerza 80 kN, altura admitida 180 a 210 mm; PB, fuerza 150 kN, altura admitida 230 a 280 mm. Escribe (a) la fuerza de corte en N y en kN, (b) qué prensa calza en altura, (c) si la fuerza de esa prensa alcanza y cuánto margen deja, (d) qué documento guarda el historial de la matriz.",
        "(a) 120 × 2 × 250 = 60.000 N, es decir 60 kN. (b) PA, porque 200 está entre 180 y 210. (c) Sí, 80 − 60 = 20 kN de margen. (d) La ficha de la matriz.",
        ["calcula la fuerza", "elige la prensa por altura", "calcula el margen", "nombra el documento"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la altura", "no pasar N a kN", "no dejar margen"],
        "Pregunta: «¿la altura cerrada está dentro del rango de la prensa?». Si duda, pídele que compare los números."),
    reinforce="Inventa una matriz con altura cerrada y dos prensas con rangos, y decide cuál calza.",
    extend="Explica con un ejemplo por qué una prensa más fuerte puede no ser compatible.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (hoja de recepción de una matriz, de ejemplo e inventada; las verificaciones las hizo personal autorizado). Matriz M-03 de doblado. Plano: altura cerrada 240 mm; ancho 400 mm; masa 180 kg; 6 resortes; 2 columnas. "
     "Prensa del taller: fuerza máxima 120 kN; altura de cierre admitida 200 a 260 mm; mesa de 500 mm de ancho; capacidad de la grúa del taller 150 kg. Datos recibidos con la matriz: lista de piezas con 6 resortes, 3 columnas y sin ficha de historial. "
     "Fuerza de doblado necesaria de ejemplo: 100 kN. Fecha de la última mantención: no consta.")
build(
    O1, 3, F,
    use="Aprenderé a revisar en papel los documentos y datos de una matriz que llega al taller, detectando incoherencias de piezas, capacidades y historial.",
    prior=["Sé leer una lista de piezas y una ficha de matriz.", "Sé comparar capacidades.", "Sé restar números enteros."],
    explain=[
        "Cuando una matriz llega al taller, se revisan sus documentos antes de cualquier trabajo. Se comprueba que la lista de piezas coincida con el plano, que haya ficha de historial, que la masa no supere la capacidad de la grúa, que el ancho quepa en la mesa de la prensa, que la altura cerrada esté dentro del rango de la prensa y que la fuerza máxima alcance con margen.",
        "Cada diferencia se registra con el dato y el motivo y se informa a la jefatura; el trabajo no avanza hasta resolverla. Una masa mayor que la capacidad de la grúa es un riesgo grave: nadie la mueve con un equipo insuficiente. La revisión es documental, y el montaje lo hace personal autorizado con el procedimiento de la empresa.",
        f"No se mueve, monta ni prueba ninguna matriz con este cuaderno. {EMER} {AVISO}",
    ],
    vocab=[("hoja de recepción", "documento donde se revisan los datos de una matriz que llega"), ("capacidad de la grúa", "masa máxima que puede levantar el equipo de izaje"), ("incoherencia", "dato que contradice a otro o al plano"), ("margen de fuerza", "diferencia entre la fuerza de la prensa y la necesaria"), ("historial", "registro de golpes y mantenciones")],
    worked=[
        ("Capacidad de la grúa", "Una matriz de ejemplo pesa 300 kg y la grúa admite 250 kg. ¿Se puede mover con esa grúa?", ["300 supera 250.", "La grúa no alcanza."], "No"),
        ("Cantidad de piezas", "El plano de ejemplo pide 4 resortes y la lista recibida trae 6. ¿Qué hay?", ["Los datos no coinciden.", "Es una incoherencia."], "Una incoherencia entre plano y lista"),
    ],
    mistakes=[("Mover una matriz sin comprobar su masa contra la grúa.", "Una masa excesiva puede romper el equipo y causar un accidente grave.", "Comprueba la masa antes de cualquier movimiento."),
              ("Aceptar una matriz sin historial.", "No se sabe cuántos golpes lleva ni su última mantención.", "Pide el historial o regístralo como pendiente.")],
    T=[
        ("abc", "En Matricería: ¿qué es una hoja de recepción de una matriz?", "Un documento donde se revisan los datos de una matriz que llega", "Un plano de la prensa", "Una pauta de limpieza", "Sirve para revisar antes de trabajar."),
        ("abc", "En Matricería: ¿qué es la capacidad de la grúa?", "La masa máxima que puede levantar el equipo de izaje", "La altura del taller", "El largo de la matriz", "En este caso, Es el límite de masa."),
        ("abc", "En Matricería: ¿qué es un margen de fuerza?", "La diferencia entre la fuerza de la prensa y la necesaria", "La suma de ambas", "La fuerza de la grúa", "En este caso, mide cuánta fuerza sobra."),
        ("=", "{F} ¿Cuántos kg supera la masa de la matriz la capacidad de la grúa?", "180-150", "Se resta la capacidad a la masa.", " kg"),
        ("abc", "{F} ¿Se puede mover la matriz M-03 con la grúa del taller?", "No, porque su masa de 180 kg supera los 150 kg de la grúa", "Sí, porque 180 es cercano a 150", "Sí, si se mueve despacio", "En este caso, La masa excede la capacidad."),
        ("abc", "{F} ¿Qué incoherencia hay en la lista de piezas recibida?", "Trae 3 columnas y el plano indica 2", "Trae 6 resortes y el plano indica 6", "Trae el mismo número de piezas", "En este caso, las columnas no coinciden."),
        ("=", "{F} ¿Cuántos kN de margen de fuerza tiene la prensa sobre la fuerza de doblado necesaria?", "120-100", "Se resta la fuerza necesaria a la máxima.", " kN"),
        ("abc", "{F} ¿Está la altura cerrada dentro del rango de la prensa?", "Sí, 240 mm está entre 200 y 260 mm", "No, porque supera 200", "No, porque 240 es distinto de 260", "En este caso, El rango incluye 240."),
        ("abc", "{F} ¿Qué se anota sobre el historial de la matriz?", "Que falta la ficha y no consta la última mantención", "Que la matriz es nueva", "Que está completo", "La ficha no está y se debe registrar como pendiente."),
        ("abc", "{F} Un jefe dice: «movamos la matriz con la grúa, que aguanta un poco más». ¿Qué respuesta es correcta?", "No corresponde: nadie mueve una matriz que supera la capacidad de la grúa; se pide un equipo adecuado", "Corresponde, si se hace despacio", "Corresponde, si es poca la diferencia", "Superar la capacidad es un riesgo grave."),
        ("abc", "{F} Falta el historial, pero todo lo demás calza. ¿Qué corresponde?", "Registrar el pendiente e informar a la jefatura antes de seguir", "Seguir y completar después", "Inventar el historial", "No se avanza con datos pendientes."),
        ("=", "{F} Si la matriz se instalara con 10 kN menos de fuerza disponible, ¿cuánto margen quedaría?", "(120-10)-100", "Se resta lo perdido a la fuerza máxima y luego la necesaria.", " kN"),
        ("Una matriz de ejemplo mide 550 mm de ancho y la mesa de la prensa 500 mm. ¿Cabe?", "No", "El ancho supera el de la mesa."),
    ],
    ctx=("abc", "El jefe de ejemplo apura: «usemos la matriz hoy, después arreglamos los papeles». ¿Qué propones?", "Completar la revisión de recepción y resolver las incoherencias antes de cualquier trabajo", "Usarla igual", "Dar por bueno el plano", "Los papeles de una matriz se resuelven antes de trabajar."),
    sc=[
        ("En Matricería: ¿qué se compara con la capacidad de la grúa?", "La masa de la matriz", "Una masa excesiva es un riesgo grave."),
        ("En Matricería: ¿qué se hace con una incoherencia en la recepción?", "Se registra e informa antes de avanzar", "No se trabaja con datos contradictorios."),
        ("En Matricería: ¿qué falta si no hay ficha de historial?", "Saber cuántos golpes lleva y su última mantención", "El historial guía la vida de la matriz."),
    ],
    op=("Ficha de ejemplo: matriz M-09: plano con 2 columnas y 4 resortes; lista recibida con 2 columnas y 5 resortes; masa 200 kg; sin ficha de historial. Prensa: 90 kN; el doblado pide 80 kN. Grúa: 250 kg. Escribe (a) qué incoherencia hay en la lista, (b) si la grúa alcanza, (c) el margen de fuerza, (d) qué haces con el historial faltante.",
        "(a) Sobra un resorte: 5 en vez de 4. (b) Sí, 200 kg no supera 250 kg. (c) 90 − 80 = 10 kN. (d) Registrarlo como pendiente e informar a la jefatura antes de seguir.",
        ["detecta la incoherencia", "evalúa la grúa", "calcula el margen", "trata el historial faltante"],
        ["hoja con las cuatro respuestas"],
        ["no detectar la diferencia", "confundir la grúa", "inventar el historial"],
        "Pregunta: «¿cuántos resortes pide el plano y cuántos trae la lista?». Si duda, pídele que compare ambos."),
    reinforce="Escribe cinco datos que revisarías al recibir una matriz.",
    extend="Explica con un ejemplo por qué una masa mayor que la capacidad de la grúa es un riesgo grave.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (cálculo de producción y de costo de una matriz, de ejemplo e inventado). Matriz de corte de discos. Prensa a 40 golpes por minuto, con un disco por golpe. Chapa en tiras de 1.000 mm de largo; cada disco usa 50 mm de largo de tira (incluye el desperdicio). "
     "Costo de ejemplo de la matriz: $1.200.000, que se reparte (amortiza) entre las 400.000 piezas que se espera fabricar. Costo de la prensa: $12.000 por hora. Costo de la chapa por disco: $40. Se pierden 2 de cada 100 piezas por defectos. Turno de 480 minutos con 60 minutos de paradas.")
build(
    O1, 4, F,
    use="Aprenderé a calcular las piezas por hora, el aprovechamiento de la chapa, la amortización de la matriz y el costo por pieza buena, con datos de ejemplo.",
    prior=["Sé multiplicar y dividir enteros.", "Sé calcular un porcentaje de números redondos.", "Sé calcular un costo por minuto."],
    explain=[
        "Las piezas por minuto son los golpes por minuto por las piezas por golpe. Las piezas por turno se calculan con los minutos de trabajo, que son los minutos del turno menos las paradas. El aprovechamiento de la chapa compara cuántas piezas salen de una tira: se divide el largo de la tira entre el largo que usa cada pieza. La amortización de la matriz reparte su costo entre las piezas que se espera fabricar: se divide el costo de la matriz entre esas piezas.",
        "El costo por pieza suma la amortización, la chapa y la prensa por pieza. Los defectuosos obligan a repartir el costo entre las piezas buenas. Todo es un cálculo de papel con valores de ejemplo, sin operar ninguna máquina.",
        f"Los números son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("golpes por minuto", "veces por minuto que la prensa cierra la matriz"), ("amortización", "reparto del costo de la matriz entre las piezas que fabrica"), ("aprovechamiento de la chapa", "cuántas piezas salen de una tira de chapa"), ("minutos de trabajo", "minutos del turno menos las paradas"), ("piezas buenas", "piezas que cumplen el plano")],
    worked=[
        ("Piezas por minuto", "Una prensa de ejemplo da 30 golpes por minuto y saca 2 piezas por golpe. ¿Cuántas piezas por minuto?", ["Se multiplican los golpes por las piezas por golpe.", "30 por 2 son 60."], "60 piezas por minuto"),
        ("Amortización", "Una matriz de ejemplo cuesta $500.000 y fabricará 100.000 piezas. ¿Cuánto es la amortización por pieza?", ["Se divide el costo entre las piezas.", "500.000 dividido en 100.000 son 5."], "$5 por pieza"),
    ],
    mistakes=[("Contar los minutos del turno completos sin descontar las paradas.", "En las paradas la prensa no produce.", "Resta las paradas a los minutos del turno."),
              ("Olvidar la amortización de la matriz en el costo.", "La matriz también cuesta y se paga con las piezas.", "Súmala al costo por pieza.")],
    T=[
        ("abc", "En Matricería: ¿qué es la amortización de una matriz?", "El reparto de su costo entre las piezas que fabricará", "El pago de la prensa por hora", "El precio de venta de la pieza", "La amortización reparte un costo fijo."),
        ("abc", "En Matricería: ¿cómo se obtienen las piezas por minuto?", "Golpes por minuto por piezas por golpe", "Golpes por minuto más piezas por golpe", "Golpes dividido por piezas por golpe", "Cada golpe produce las piezas de la matriz."),
        ("abc", "En Matricería: ¿qué son los minutos de trabajo?", "Los minutos del turno menos las paradas", "Los minutos totales del día", "Los minutos de cada golpe", "Solo se produce mientras la prensa trabaja."),
        ("=", "{F} ¿Cuántas piezas por minuto saca la prensa?", "40*1", "Se multiplican los golpes por las piezas por golpe.", " piezas"),
        ("=", "{F} ¿Cuántos minutos de trabajo tiene el turno?", "480-60", "Se restan las paradas a los minutos del turno.", " minutos"),
        ("=", "{F} ¿Cuántas piezas se fabrican en un turno?", "40*(480-60)", "Se multiplican las piezas por minuto por los minutos de trabajo.", " piezas"),
        ("=", "{F} ¿Cuántos discos salen de una tira de 1.000 mm si cada uno usa 50 mm?", "1000//50", "Se divide el largo de la tira entre lo que usa cada disco.", " discos"),
        ("=", "{F} ¿Cuántos pesos de ejemplo es la amortización por pieza?", "1200000//400000", "Se divide el costo de la matriz entre las piezas esperadas.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántas piezas por hora saca la prensa?", "40*60", "Se multiplican las piezas por minuto por 60.", " piezas"),
        ("=", "{F} ¿Cuánto cuesta la prensa por pieza, a $12.000 la hora y con 2.400 piezas por hora?", "12000//2400", "Se divide el costo por hora entre las piezas por hora.", " pesos de ejemplo"),
        ("abc", "{F} ¿Cuánto cuesta cada pieza entre amortización, chapa y prensa?", "$48", "$40", "$3", "Son 3 de amortización, 40 de chapa y 5 de prensa."),
        ("abc", "{F} Un jefe dice: «el costo por pieza es solo la chapa: $40». ¿Qué respuesta es correcta?", "Es incompleto: faltan la amortización de la matriz y el costo de la prensa", "Es correcto, porque la chapa es lo principal", "Es correcto, si se fabrican muchas piezas", "El costo incluye matriz, prensa y chapa."),
        ("=", "{F} Con 2 piezas defectuosas de cada 100, ¿cuántas piezas buenas hay en un lote de 10.000?", "10000-10000*2//100", "Se resta el 2 % de defectuosas al lote.", " piezas"),
    ],
    ctx=("abc", "El cliente de ejemplo pregunta el precio de un disco y el jefe solo suma la chapa. ¿Qué propones?", "Sumar también la amortización de la matriz y el costo de la prensa", "Dar solo el costo de la chapa", "Cobrar solo la prensa", "El costo real incluye todos los componentes."),
    sc=[
        ("En Matricería: ¿cuánto es la amortización de una matriz de $900.000 para 300.000 piezas?", "$3 por pieza", "Se divide el costo entre las piezas esperadas."),
        ("En Matricería: ¿qué se resta a los minutos del turno?", "Las paradas", "Solo se produce mientras la prensa trabaja."),
        ("En Matricería: ¿cómo se obtienen las piezas buenas?", "Restando los defectuosos al total", "En este caso, las defectuosas no se entregan."),
    ],
    op=("Ficha de ejemplo: una matriz de $600.000 fabricará 200.000 piezas. La prensa da 50 golpes por minuto con 1 pieza por golpe; el turno es de 480 minutos con 80 minutos de paradas. Chapa: $30 por pieza. Prensa: $15.000 la hora. Escribe (a) la amortización por pieza, (b) las piezas por turno, (c) las piezas por hora, (d) el costo de prensa por pieza.",
        "(a) 600.000 ÷ 200.000 = 3 pesos de ejemplo. (b) 50 × (480 − 80) = 20.000 piezas. (c) 50 × 60 = 3.000 piezas por hora. (d) 15.000 ÷ 3.000 = 5 pesos de ejemplo.",
        ["calcula la amortización", "calcula las piezas por turno", "calcula las piezas por hora", "calcula el costo de prensa"],
        ["hoja con las cuatro respuestas"],
        ["no descontar las paradas", "dividir al revés", "olvidar la amortización"],
        "Pregunta: «¿cuántas piezas por minuto?». Si duda, pídele que multiplique golpes por piezas por golpe."),
    reinforce="Inventa una matriz con costo y piezas esperadas y calcula la amortización por pieza.",
    extend="Explica con un ejemplo por qué la amortización baja si se fabrican más piezas.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El taller diseña moldes de inyección. Una máquina inyectora funde plástico y lo inyecta con presión en un molde, un conjunto de dos mitades con un hueco (la cavidad) que da la forma a la pieza. "
     "Partes del molde de ejemplo: mitad fija, mitad móvil, cavidad, canal de entrada (bebedero), canales de enfriamiento y expulsores (que sacan la pieza). Peligros anotados: superficies a temperatura alta, plástico fundido que puede quemar, presión alta, aplastamiento al cerrarse el molde, cargas pesadas, energía hidráulica, gases del plástico calentado y ruido.")
build(
    O2, 1, F,
    use="Aprenderé qué es un molde de inyección y su máquina, sus partes principales, sus peligros y los controles generales, sin montar ni operar nada.",
    prior=["Sé qué es una matriz y una prensa.", "Sé qué es la energía almacenada.", "Sé la jerarquía de controles."],
    explain=[
        "El moldeo por inyección fabrica piezas de plástico: la máquina inyectora calienta el plástico hasta fundirlo y lo inyecta con presión en un molde, que es un conjunto de dos mitades con un hueco, la cavidad, que da la forma. El plástico se enfría dentro del molde y los expulsores sacan la pieza. El bebedero es el canal por donde entra el plástico y los canales de enfriamiento llevan un líquido que enfría el molde.",
        "Los peligros principales son las altas temperaturas, el plástico fundido que puede quemar, la alta presión, el aplastamiento cuando el molde se cierra, las cargas pesadas, la energía hidráulica, los gases del plástico calentado y el ruido. Los controles incluyen puertas con enclavamiento, resguardos, ventilación o extracción de gases, bloqueo y etiquetado, orden y limpieza y EPP como última barrera. El plástico y los líquidos de enfriamiento se gestionan según la norma vigente.",
        f"Montar, mantener y operar un molde exige personal autorizado e instructor; este cuaderno no enseña a hacerlo. {EMER} {AVISO}",
    ],
    vocab=[("inyectora", "máquina que funde plástico y lo inyecta en un molde"), ("molde de inyección", "conjunto de dos mitades con una cavidad que da forma a la pieza"), ("cavidad", "hueco del molde que da la forma a la pieza"), ("bebedero", "canal por donde entra el plástico al molde"), ("expulsor", "pieza que saca la pieza ya enfriada del molde"), ("canal de enfriamiento", "conducto por donde circula un líquido que enfría el molde")],
    worked=[
        ("Nombrar la parte", "En un molde de ejemplo, el hueco da forma a la pieza. ¿Cómo se llama?", ["Es el hueco que da forma.", "Se llama cavidad."], "La cavidad"),
        ("Clasificar un control", "Una puerta de ejemplo no permite que el molde se cierre con ella abierta. ¿Qué tipo de control es?", ["Es un dispositivo físico que actúa por sí mismo.", "Es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Tocar un molde que acaba de detenerse porque «ya no se mueve».", "Puede estar muy caliente y tener energía almacenada.", "Solo personal autorizado interviene, según el procedimiento."),
              ("Creer que leer sobre moldes habilita para montarlos.", "El montaje exige personal autorizado e instructor.", "Aprende el concepto y deja la tarea a quien corresponde.")],
    T=[
        ("abc", "En Matricería: ¿qué hace una inyectora?", "Funde el plástico y lo inyecta con presión en un molde", "Corta chapas con una matriz", "Pule la superficie del molde", "En este caso, La inyectora funde e inyecta."),
        ("abc", "En Matricería: ¿qué es el bebedero?", "El canal por donde entra el plástico al molde", "El hueco que da forma a la pieza", "La pieza que saca la pieza terminada", "El bebedero es la entrada del plástico."),
        ("abc", "En Matricería: ¿qué hacen los expulsores?", "Sacan la pieza ya enfriada del molde", "Calientan el plástico", "Enfrían el molde", "En este caso, los expulsores retiran la pieza."),
        ("abc", "{F} ¿Qué parte del molde da la forma a la pieza?", "La cavidad", "El bebedero", "Los expulsores", "La cavidad es el hueco con la forma."),
        ("abc", "{F} ¿Cuál es el peligro que se relaciona con el plástico fundido?", "Las quemaduras", "El aplastamiento", "El ruido", "El plástico fundido está muy caliente."),
        ("abc", "{F} Una extracción de gases en el lugar de trabajo es un control:", "De ingeniería", "Administrativo", "De EPP", "La extracción cambia el lugar y retira los gases."),
        ("=", "{F} El taller tiene 3 inyectoras y 2 personas por máquina en la prueba de un molde. ¿Cuántas personas se necesitan?", "3*2", "Se multiplican las inyectoras por las personas de cada una.", " personas"),
        ("=", "{F} Cada inyectora usa 40 litros de líquido de enfriamiento a la semana. ¿Cuántos litros usan las 3 en 4 semanas?", "3*40*4", "Se multiplican las inyectoras, los litros y las semanas.", " litros"),
        ("abc", "{F} Un aprendiz dice: «el molde ya paró, lo toco para sacar la rebaba». ¿Qué respuesta es correcta?", "Es falso: puede estar muy caliente y con energía almacenada, y solo personal autorizado interviene", "Es cierto, porque ya paró", "Es cierto, si usa guantes", "En este caso, detenido no significa seguro."),
        ("abc", "En una visita a un taller de ejemplo, una persona recibe plástico fundido en la mano. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Quitarle el plástico con tus manos", "Taparle la quemadura con tela", "Los primeros auxilios los hacen quienes tienen formación."),
        ("abc", "En Matricería: ¿qué se hace con los bebederos y las piezas rechazadas de plástico?", "Se separan y se gestionan según la norma vigente, por ejemplo para reciclar", "Se botan a la basura común", "Se queman en el patio", "Los residuos plásticos tienen un manejo propio."),
        ("=", "{F} Si cada molde tiene 4 canales de enfriamiento y hay 5 moldes, ¿cuántos canales hay?", "4*5", "Se multiplican los moldes por los canales de cada uno.", " canales"),
        ("abc", "{F} Una cubierta que protege contra el aplastamiento al cerrarse el molde es un control:", "De ingeniería", "Administrativo", "De EPP", "La cubierta es una barrera física."),
    ],
    ctx=("abc", "Un amigo de ejemplo te dice: «el liceo tiene una inyectora, probemos con un poco de plástico». ¿Qué respondes?", "Que no, porque usarla exige instructor autorizado y norma vigente, y que consultarás a un adulto responsable", "Que sí, con guantes gruesos", "Que sí, a baja temperatura", "Este cuaderno no habilita para operar máquinas."),
    sc=[
        ("En Matricería: ¿qué es la cavidad de un molde?", "El hueco que da la forma a la pieza", "La cavidad define la forma de la pieza."),
        ("En Matricería: ¿qué peligro tiene el plástico fundido?", "Quemaduras graves", "En este caso, está a temperatura muy alta."),
        ("En Matricería: ¿quién puede montar un molde?", "Personal autorizado con instructor", "El trabajo exige formación y norma vigente."),
    ],
    op=("Ficha de ejemplo: un molde de dos mitades con una cavidad, un bebedero y 6 canales de enfriamiento en una inyectora ficticia. Peligros: plástico fundido, aplastamiento y gases. Escribe (a) qué parte da la forma a la pieza, (b) un control de ingeniería, (c) un control administrativo, (d) qué harías ante una quemadura de otra persona. No describas cómo se monta.",
        "(a) La cavidad. (b) Las puertas con enclavamiento o la extracción de gases. (c) La regla de que solo personal autorizado interviene y el bloqueo y etiquetado. (d) No acercarme a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["nombra la cavidad", "propone un control de ingeniería", "propone un control administrativo", "indica qué hacer ante un accidente"],
        ["hoja con las cuatro respuestas"],
        ["confundir cavidad con bebedero", "proponer solo EPP", "intervenir ante el accidente"],
        "Pregunta: «¿qué parte tiene el hueco con la forma?». Si duda, pídele que relea el vocabulario."),
    reinforce="Escribe cuatro partes de un molde de inyección con una frase de lo que hace cada una.",
    extend="Explica con un ejemplo por qué un molde detenido sigue siendo peligroso.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 2 (ficha de molde y especificaciones de inyectoras, de ejemplo e inventadas). Molde MI-01: 4 cavidades; masa de una pieza, 25 g; masa del canal de entrada (bebedero y canales) por ciclo, 20 g; ancho del molde, 350 mm; espesor del molde cerrado, 280 mm. "
     "Tiempo de ciclo de ejemplo: 30 segundos. Inyectora A: fuerza de cierre 400 kN; distancia entre columnas 400 mm; volumen máximo de inyección 150 g; espesor de molde admitido 200 a 300 mm. "
     "Inyectora B: fuerza de cierre 800 kN; distancia entre columnas 500 mm; volumen máximo de inyección 300 g; espesor de molde admitido 250 a 400 mm. Fuerza de cierre necesaria de ejemplo para este molde: 500 kN.")
build(
    O2, 2, F,
    use="Aprenderé a leer la ficha de un molde y las especificaciones de una inyectora y a comprobar en papel su compatibilidad: fuerza de cierre, tamaño y masa de inyección.",
    prior=["Sé qué es un molde de inyección.", "Sé multiplicar y sumar enteros.", "Sé comparar capacidades."],
    explain=[
        "La ficha de un molde indica cuántas cavidades tiene, la masa de cada pieza, la masa del canal de entrada, sus dimensiones y el tiempo de ciclo. Una cavidad es un hueco, y con 4 cavidades salen 4 piezas por ciclo. La masa de inyección por ciclo es la masa de las piezas más la del canal de entrada, que también se inyecta.",
        "Una inyectora tiene una fuerza de cierre, que mantiene el molde cerrado frente a la presión del plástico; una distancia entre columnas, que limita el ancho del molde; un volumen máximo de inyección y un rango de espesor de molde admitido. El molde es compatible si la fuerza de cierre alcanza con margen, el ancho cabe entre las columnas, la masa por ciclo no supera el máximo y el espesor está dentro del rango. Los valores son de ejemplo.",
        f"Es una comprobación de papel. {EMER} {AVISO}",
    ],
    vocab=[("cavidades", "huecos del molde, uno por cada pieza de un ciclo"), ("masa de inyección", "masa de las piezas más la del canal de entrada"), ("fuerza de cierre", "fuerza que mantiene el molde cerrado frente a la presión del plástico"), ("distancia entre columnas", "espacio horizontal útil de la inyectora para el molde"), ("tiempo de ciclo", "tiempo en que se produce un conjunto de piezas")],
    worked=[
        ("Masa por ciclo", "Un molde de ejemplo tiene 2 cavidades de 30 g cada una y un canal de 10 g. ¿Cuántos g se inyectan por ciclo?", ["Las piezas pesan 2 por 30, es decir 60 g.", "Con el canal de 10 g son 70 g."], "70 g"),
        ("Compatibilidad de fuerza", "Un molde de ejemplo requiere 300 kN y una inyectora tiene 350 kN. ¿Alcanza?", ["350 es mayor que 300.", "Alcanza, con 50 kN de margen."], "Sí, con 50 kN de margen"),
    ],
    mistakes=[("Calcular la masa de inyección sin el canal de entrada.", "El canal también se inyecta.", "Suma la masa del canal a la de las piezas."),
              ("Elegir una inyectora solo por su fuerza de cierre.", "También deben calzar el ancho, el espesor y la masa de inyección.", "Comprueba los cuatro datos.")],
    T=[
        ("abc", "En Matricería: ¿qué es la fuerza de cierre de una inyectora?", "La fuerza que mantiene el molde cerrado frente a la presión del plástico", "La fuerza con que se funde el plástico", "El peso de la máquina", "La fuerza de cierre evita que el molde se abra al inyectar."),
        ("abc", "En Matricería: ¿qué incluye la masa de inyección por ciclo?", "Las piezas más el canal de entrada", "Solo las piezas", "Solo el canal de entrada", "Todo el plástico inyectado se cuenta."),
        ("abc", "En Matricería: ¿qué limita la distancia entre columnas?", "El ancho del molde que cabe en la inyectora", "La masa de una pieza", "El tiempo de ciclo", "El molde debe pasar entre las columnas."),
        ("=", "{F} ¿Cuántos g pesan las 4 piezas de un ciclo?", "4*25", "Se multiplican las cavidades por la masa de una pieza.", " g"),
        ("=", "{F} ¿Cuántos g se inyectan por ciclo, con las 4 piezas más el canal de 20 g?", "4*25+20", "Se suman las piezas y el canal de entrada.", " g"),
        ("abc", "{F} ¿Qué inyectoras tienen un volumen máximo de inyección suficiente para los 120 g por ciclo del molde?", "Ambas, A y B, porque 150 g y 300 g superan los 120 g", "Solo la B, porque admite más gramos", "Ninguna", "El molde necesita 120 g por ciclo y A admite 150 g y B admite 300 g."),
        ("=", "{F} ¿Cuántos kN de margen deja la inyectora B sobre la fuerza de cierre necesaria de 500 kN?", "800-500", "Se resta la fuerza necesaria a la fuerza de la inyectora.", " kN"),
        ("abc", "{F} ¿Cabe el molde de 350 mm de ancho entre las columnas de la inyectora A?", "Sí, porque 350 mm es menor que los 400 mm entre columnas", "No, porque 350 mm supera los 300 mm de espesor admitido", "No, porque la distancia entre columnas es menor que 350 mm", "El ancho de 350 mm es menor que la distancia de 400 mm entre columnas."),
        ("abc", "{F} Con el espesor de 280 mm, ¿qué inyectoras lo admiten?", "Ambas, A y B", "Solo A", "Solo B", "A admite de 200 a 300 y B admite de 250 a 400."),
        ("abc", "{F} Con fuerza de cierre necesaria de 500 kN, ¿qué inyectora alcanza?", "Solo la B, de 800 kN", "La A, de 400 kN", "Ambas", "La inyectora A no llega a 500 kN."),
        ("abc", "{F} Un jefe dice: «usemos la A, que cabe el molde y es más barata». ¿Qué respuesta es correcta?", "No corresponde: la fuerza de cierre de A, 400 kN, es menor que los 500 kN necesarios", "Corresponde, porque cabe el molde", "Corresponde, si baja la presión", "En este caso, todos los datos deben calzar."),
        ("=", "{F} ¿Cuántas piezas salen por hora con un ciclo de 30 segundos y 4 cavidades? Un ciclo de 30 s son 120 ciclos por hora.", "120*4", "Se multiplican los ciclos por hora por las cavidades.", " piezas"),
        ("Un molde de ejemplo requiere 600 kN y una inyectora tiene 550 kN. ¿Alcanza?", "No", "En este caso, 550 es menor que 600."),
    ],
    ctx=("abc", "El pañolero de ejemplo dice: «el molde cabe en la inyectora A, ya está». ¿Qué propones?", "Comprobar también fuerza de cierre, masa de inyección y espesor", "Aceptarlo porque cabe", "Revisar solo la fuerza", "En este caso, todos los datos deben calzar."),
    sc=[
        ("En Matricería: ¿cuántas piezas salen por ciclo de un molde de 4 cavidades?", "4", "Cada cavidad produce una pieza por ciclo."),
        ("En Matricería: ¿qué se suma a las piezas en la masa de inyección?", "El canal de entrada", "En este caso, también se inyecta ese plástico."),
        ("En Matricería: ¿qué datos se comparan para la compatibilidad molde-inyectora?", "Fuerza de cierre, ancho, espesor y masa de inyección", "En este caso, los cuatro deben calzar."),
    ],
    op=("Ficha de ejemplo: molde de 2 cavidades, pieza de 40 g, canal de 10 g por ciclo, 300 mm de ancho, 220 mm de espesor, fuerza de cierre necesaria 250 kN. Inyectora X: 300 kN, 350 mm entre columnas, 100 g máximo, espesor 200 a 260 mm. Inyectora Y: 200 kN, 400 mm, 200 g, espesor 180 a 300 mm. Escribe (a) la masa de inyección por ciclo, (b) qué inyectoras alcanzan en fuerza de cierre, (c) qué inyectora es compatible con todos los datos, (d) qué compruebas para el espesor.",
        "(a) 2 × 40 + 10 = 90 g. (b) Solo la X, porque la Y tiene 200 kN y se necesitan 250. (c) La X: 300 kN alcanza, el ancho de 300 cabe en 350, 90 g no supera 100 y el espesor de 220 está entre 200 y 260. (d) Que 220 mm esté dentro del rango admitido.",
        ["calcula la masa por ciclo", "evalúa la fuerza de cierre", "elige la inyectora", "revisa el espesor"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el canal", "evaluar un solo dato", "no comprobar el espesor"],
        "Pregunta: «¿cuál alcanza en fuerza de cierre?». Si duda, pídele que compare cada fuerza con la necesaria."),
    reinforce="Inventa un molde con cavidades, masa de pieza y canal y calcula la masa de inyección por ciclo.",
    extend="Explica con un ejemplo por qué un molde puede caber en una inyectora y aun así no ser compatible.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 3 (hoja de proceso de ejemplo con errores, inventada). Molde MI-02 de 8 cavidades; pieza de 15 g; canal de entrada 24 g por ciclo. Hoja: masa de inyección por ciclo anotada, 120 g; ciclo anotado, 25 segundos; piezas por hora anotadas, 1.152. Material: polipropileno (un plástico); temperatura de molde anotada 40 °C. "
     "Inyectora asignada: fuerza de cierre 300 kN; fuerza necesaria para este molde, 350 kN; volumen máximo de inyección 200 g. Revisión de la hoja: B; del plano del molde: C. Producción de ejemplo: 28.800 piezas pedidas.")
build(
    O2, 3, F,
    use="Aprenderé a revisar en papel una hoja de proceso de inyección, calculando masa por ciclo y piezas por hora, y detectando incompatibilidades y revisiones distintas.",
    prior=["Sé calcular la masa de inyección por ciclo.", "Sé pasar un tiempo de ciclo a ciclos por hora.", "Sé comparar capacidades."],
    explain=[
        "Revisar una hoja de proceso de inyección es recalcular lo que anota: la masa de inyección por ciclo es las cavidades por la masa de la pieza más el canal; los ciclos por hora son 3.600 segundos divididos por el tiempo de ciclo; las piezas por hora son los ciclos por hora por las cavidades. También se comprueba que la inyectora asignada cumpla la fuerza de cierre y la masa máxima, y que la revisión de la hoja coincida con la del plano.",
        "Las diferencias se registran con el dato y el motivo y se informan a quien emitió la hoja. No se corrigen por cuenta propia. Los días de producción se calculan dividiendo las piezas pedidas entre las que salen por día. Un error en la hoja puede producir piezas defectuosas, daños al molde o accidentes. La revisión es documental.",
        f"El análisis es de papel. {EMER} {AVISO}",
    ],
    vocab=[("ciclos por hora", "3.600 segundos divididos por el tiempo de ciclo"), ("piezas por hora", "ciclos por hora por las cavidades"), ("hoja de proceso de inyección", "documento con las condiciones de producción de una pieza"), ("incompatibilidad", "dato que impide usar una máquina para un molde"), ("polipropileno", "tipo de plástico usado en inyección")],
    worked=[
        ("Ciclos por hora", "Un ciclo de ejemplo dura 20 segundos. ¿Cuántos ciclos hay por hora?", ["Una hora tiene 3.600 segundos.", "3.600 dividido en 20 son 180."], "180 ciclos"),
        ("Piezas por hora", "Un molde de ejemplo de 6 cavidades hace 150 ciclos por hora. ¿Cuántas piezas por hora?", ["Se multiplican los ciclos por las cavidades.", "150 por 6 son 900."], "900 piezas por hora"),
    ],
    mistakes=[("Usar la masa de las piezas sin el canal.", "El canal también se inyecta y cuenta para la masa por ciclo.", "Suma la masa del canal."),
              ("Dividir los segundos del ciclo entre 60 para ciclos por hora.", "Una hora tiene 3.600 segundos.", "Divide 3.600 entre el tiempo de ciclo.")],
    T=[
        ("abc", "En Matricería: ¿cuántos segundos tiene una hora?", "3.600", "60", "1.800", "Una hora son 60 minutos de 60 segundos."),
        ("abc", "En Matricería: ¿cómo se obtienen los ciclos por hora?", "Dividiendo 3.600 entre el tiempo de ciclo en segundos", "Multiplicando 3.600 por el tiempo de ciclo", "Sumando 3.600 y el tiempo de ciclo", "Se divide una hora entre lo que dura cada ciclo."),
        ("abc", "En Matricería: ¿qué es una incompatibilidad entre molde y máquina?", "Un dato que impide usar la máquina para ese molde", "Un molde muy nuevo", "Una pieza con muchas cavidades", "La incompatibilidad exige cambiar de máquina o de molde."),
        ("=", "{F} ¿Cuántos g de masa de inyección tiene realmente cada ciclo?", "8*15+24", "Se suman las piezas y el canal de entrada.", " g"),
        ("abc", "{F} La hoja anota 120 g por ciclo. ¿Es correcto?", "No, porque la masa real es 144 g", "Sí, porque 120 g es la suma", "Sí, porque no incluye el canal", "8 por 15 son 120 más 24 del canal da 144."),
        ("abc", "{F} ¿Supera la masa por ciclo el volumen máximo de la inyectora?", "No, 144 g es menor que 200 g", "Sí, porque 144 es mayor que 120", "Sí, porque 200 es menor", "En este caso, 144 no supera 200."),
        ("=", "{F} ¿Cuántos ciclos por hora hay con un ciclo de 25 segundos?", "3600//25", "Se divide una hora en segundos entre el tiempo de ciclo.", " ciclos"),
        ("=", "{F} ¿Cuántas piezas por hora salen con 144 ciclos por hora y 8 cavidades?", "144*8", "Se multiplican los ciclos por las cavidades.", " piezas"),
        ("abc", "{F} La hoja anota 1.152 piezas por hora. ¿Es correcto?", "Sí, porque 144 ciclos por 8 cavidades dan 1.152", "No, porque debería ser 1.000", "No, porque no incluye el canal", "El cálculo coincide con la hoja."),
        ("abc", "{F} ¿Qué incompatibilidad hay con la inyectora asignada?", "Su fuerza de cierre de 300 kN es menor que los 350 kN necesarios", "El volumen de 200 g es insuficiente", "El material no es plástico", "La fuerza de cierre no alcanza."),
        ("abc", "{F} La hoja es revisión B y el plano del molde es revisión C. ¿Qué corresponde?", "Informarlo y pedir la hoja actualizada antes de trabajar", "Usar la B porque ya está lista", "Cambiar la revisión con lápiz", "Una revisión distinta puede tener datos desactualizados."),
        ("abc", "{F} Un operario dice: «inyectemos igual, la presión aguanta». ¿Qué respuesta es correcta?", "No corresponde: sin la fuerza de cierre necesaria el molde puede abrirse y expulsar plástico fundido", "Corresponde, porque la presión aguanta", "Corresponde, si se baja la temperatura", "Una fuerza de cierre insuficiente es un riesgo grave."),
        ("=", "{F} ¿Cuántos días se necesitan para 28.800 piezas, si salen 9.216 por día? Redondea hacia arriba.", "(28800+9215)//9216", "Se divide entre las piezas por día redondeando hacia arriba.", " días"),
    ],
    ctx=("abc", "El jefe de ejemplo dice: «la hoja tiene un error en la masa, pero da igual, la inyectora es grande». ¿Qué propones?", "Registrar el error y pedir una nueva revisión a quien emitió la hoja", "Ignorar el error", "Corregirlo a lápiz", "Los errores se corrigen con una revisión formal."),
    sc=[
        ("En Matricería: ¿cuántos ciclos por hora hay con un ciclo de 30 segundos?", "120", "En este caso, una hora tiene 3.600 segundos."),
        ("En Matricería: ¿qué se suma a las piezas en la masa por ciclo?", "El canal de entrada", "La razón es que también se inyecta."),
        ("En Matricería: ¿qué se hace con un error en la hoja de proceso?", "Se registra e informa a quien la emitió", "Quien emitió la hoja la corrige."),
    ],
    op=("Ficha de ejemplo: molde de 4 cavidades, pieza de 20 g, canal de 10 g por ciclo, ciclo de 40 segundos. La hoja anota masa por ciclo 80 g y 360 piezas por hora. Inyectora: fuerza de cierre 250 kN, necesidad del molde 300 kN, volumen máximo 150 g. Escribe (a) la masa real por ciclo, (b) los ciclos por hora, (c) las piezas por hora reales, (d) la incompatibilidad con la inyectora.",
        "(a) 4 × 20 + 10 = 90 g. (b) 3.600 ÷ 40 = 90 ciclos. (c) 90 × 4 = 360 piezas; coincide con la hoja. (d) La fuerza de cierre de 250 kN es menor que los 300 kN necesarios.",
        ["calcula la masa real", "calcula los ciclos", "calcula las piezas", "detecta la incompatibilidad"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el canal", "dividir entre 60", "no revisar la inyectora"],
        "Pregunta: «¿cuántos segundos tiene una hora?». Si duda, pídele que relea la definición de ciclos por hora."),
    reinforce="Inventa un molde y calcula la masa por ciclo, los ciclos por hora y las piezas por hora.",
    extend="Explica con un ejemplo por qué una fuerza de cierre insuficiente es un riesgo grave.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 4 (costeo de una producción por inyección, de ejemplo e inventada). Molde de 4 cavidades; pieza de 25 g; canal de 24 g por ciclo, que se recupera y se muele para reutilizar el 50 % (la mitad). Ciclo de 30 segundos. Precio del plástico: $2.000 por kg. "
     "Inyectora: $24.000 por hora. Pedido: 28.800 piezas. Molde: $4.800.000, que se reparte entre 240.000 piezas esperadas. Rechazo de ejemplo: 2 piezas de cada 100.")
build(
    O2, 4, F,
    use="Aprenderé a calcular las piezas por hora, el consumo de plástico, el costo por pieza y el efecto del rechazo y del reciclaje del canal, con datos de ejemplo.",
    prior=["Sé calcular ciclos por hora y piezas por hora.", "Sé pasar gramos a kilogramos.", "Sé calcular un costo por pieza."],
    explain=[
        "El plástico consumido por ciclo es la masa de las piezas más la del canal, descontando la parte del canal que se recupera y se vuelve a usar. El consumo por pieza se obtiene dividiendo ese plástico entre las cavidades. El costo del plástico es los gramos por el precio por gramo, que es el precio por kg dividido por 1.000.",
        "El costo de la inyectora por pieza es el costo por hora dividido entre las piezas por hora. La amortización del molde reparte su costo entre las piezas esperadas. El rechazo obliga a fabricar más piezas de las pedidas: las piezas buenas son el total menos los rechazos. Todo es un cálculo de papel con valores de ejemplo.",
        f"No se opera ninguna máquina. {EMER} {AVISO}",
    ],
    vocab=[("recuperación del canal", "reutilización de parte del plástico del canal de entrada"), ("consumo por pieza", "plástico usado por cada pieza"), ("costo por gramo", "precio por kg dividido por 1.000"), ("rechazo", "piezas que no cumplen y se pierden"), ("amortización del molde", "reparto del costo del molde entre las piezas esperadas")],
    worked=[
        ("Costo del plástico", "Una pieza de ejemplo usa 50 g de plástico a $2.000 el kg. ¿Cuánto cuesta el plástico?", ["Un gramo cuesta 2.000 dividido en 1.000, es decir 2 pesos.", "50 por 2 son 100."], "$100"),
        ("Piezas con rechazo", "Se piden 1.000 piezas y se rechazan 2 de cada 100. ¿Cuántas piezas buenas salen si se fabrican 1.020?", ["El 2 % de 1.020 es aproximadamente 20.", "1.020 menos 20 son 1.000."], "1.000 piezas buenas"),
    ],
    mistakes=[("Contar todo el canal como perdido, aunque se recupere.", "Una parte se reutiliza y baja el consumo.", "Resta la parte recuperada."),
              ("Olvidar el rechazo al calcular las piezas por fabricar.", "Algunas piezas se pierden y hay que fabricar más.", "Suma el rechazo al pedido.")],
    T=[
        ("abc", "En Matricería: ¿qué es la recuperación del canal?", "La reutilización de parte del plástico del canal de entrada", "La pieza que se vende", "El molde ya usado", "Recuperar baja el consumo de plástico."),
        ("abc", "En Matricería: ¿cómo se pasa un precio por kg a precio por gramo?", "Dividiendo entre 1.000", "Multiplicando por 1.000", "Sumando 1.000", "En este caso, Un kg tiene 1.000 g."),
        ("abc", "En Matricería: ¿qué es la amortización de un molde?", "El reparto de su costo entre las piezas esperadas", "El pago por hora de la inyectora", "El precio del plástico", "La amortización reparte un costo fijo."),
        ("=", "{F} ¿Cuántos g de canal se recuperan por ciclo, con el 50 % de 24 g?", "24*50//100", "Se calcula el 50 % del canal.", " g"),
        ("=", "{F} ¿Cuántos g de plástico se consumen por ciclo, con 4 piezas y la parte del canal que no se recupera?", "4*25+(24-12)", "Se suman las piezas y el canal no recuperado.", " g"),
        ("=", "{F} ¿Cuántos g de plástico se consumen por pieza, con 112 g por ciclo y 4 cavidades?", "112//4", "Se divide el consumo por ciclo entre las cavidades.", " g"),
        ("=", "{F} ¿Cuánto cuesta el plástico de una pieza que usa 28 g, a $2 el gramo?", "28*2", "Se multiplican los gramos por el precio por gramo.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántas piezas por hora salen con 120 ciclos y 4 cavidades?", "120*4", "Se multiplican los ciclos por hora por las cavidades.", " piezas"),
        ("=", "{F} ¿Cuánto cuesta la inyectora por pieza, a $24.000 la hora y 480 piezas por hora?", "24000//480", "Se divide el costo por hora entre las piezas por hora, con enteros.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto es la amortización del molde por pieza?", "4800000//240000", "Se divide el costo del molde entre las piezas esperadas.", " pesos de ejemplo"),
        ("abc", "{F} Un jefe dice: «el costo de una pieza es solo el plástico». ¿Qué respuesta es correcta?", "Es incompleto: faltan la inyectora, la amortización del molde y el rechazo", "Es correcto, porque el plástico es lo principal", "Es correcto, si hay pocas piezas", "El costo incluye plástico, máquina, molde y pérdidas."),
        ("Un pedido de ejemplo pide 9.800 piezas buenas y el rechazo es de 2 de cada 100. ¿Cuántas piezas hay que fabricar? Las buenas son el 98 % de las fabricadas.", "10.000 piezas", "El 98 % de 10.000 son 9.800, que son las piezas buenas pedidas."),
        ("Si se fabrican 29.388 piezas y se rechazan 588, ¿cuántas piezas buenas salen?", "28.800", "En este caso, 29.388 menos 588 son 28.800."),
    ],
    ctx=("abc", "El cliente de ejemplo pide un precio por pieza y el jefe solo suma el plástico. ¿Qué propones?", "Sumar también la inyectora, la amortización del molde y el rechazo", "Dar solo el costo del plástico", "Cobrar solo la inyectora", "El costo real incluye todos los componentes."),
    sc=[
        ("En Matricería: ¿cuántos pesos cuesta 1 g de plástico a $2.000 el kg?", "2", "En este caso, Se divide entre 1.000."),
        ("En Matricería: ¿qué baja el consumo de plástico?", "Recuperar parte del canal", "En este caso, parte del plástico se reutiliza."),
        ("En Matricería: ¿qué se agrega al pedido para cubrir el rechazo?", "Piezas extra", "En este caso, algunas piezas se pierden."),
    ],
    op=("Ficha de ejemplo: molde de 2 cavidades, pieza de 30 g, canal de 10 g por ciclo del cual se recupera la mitad. Ciclo de 36 segundos. Plástico a $1.000 el kg. Inyectora a $18.000 la hora. Escribe (a) los g de plástico consumidos por ciclo, (b) los ciclos por hora, (c) las piezas por hora, (d) el costo de la inyectora por pieza.",
        "(a) 2 × 30 + (10 − 5) = 65 g. (b) 3.600 ÷ 36 = 100 ciclos. (c) 100 × 2 = 200 piezas. (d) 18.000 ÷ 200 = 90 pesos de ejemplo.",
        ["calcula el consumo por ciclo", "calcula los ciclos", "calcula las piezas", "calcula el costo de la inyectora"],
        ["hoja con las cuatro respuestas"],
        ["no restar lo recuperado", "dividir entre 60", "confundir kg y g"],
        "Pregunta: «¿cuánto del canal se recupera?». Si duda, pídele que relea el enunciado."),
    reinforce="Inventa un molde y calcula el consumo de plástico por ciclo con una parte recuperada del canal.",
    extend="Explica con un ejemplo por qué recuperar el canal baja el costo por pieza.",
)

# ============================================================ OAM-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). En el taller de ejemplo se producen piezas de chapa con una matriz y piezas de plástico con un molde. Defectos posibles: en piezas de chapa, rebabas (bordes con material sobrante), deformaciones y grietas; en piezas de plástico, falta de llenado (pieza incompleta), rechupes (hundimientos) y marcas. "
     "Una falla es el estado en que la matriz o el molde no cumple su función; las causas comunes son desgaste, holgura, desalineación, falta de lubricación o parámetros inadecuados. Peligros anotados al revisar: bordes filosos, superficies calientes, energía almacenada y piezas pesadas.")
build(
    O3, 1, F,
    use="Aprenderé qué defectos suelen aparecer en piezas de chapa y de plástico, qué es una falla de matriz o molde, sus causas comunes y los riesgos de revisarlas.",
    prior=["Sé qué es una matriz y un molde.", "Sé qué es una no conformidad.", "Sé la jerarquía de controles."],
    explain=[
        "Un defecto es una característica de la pieza que no cumple lo pedido. En piezas de chapa, los defectos comunes son la rebaba, que es un borde con material sobrante, la deformación y la grieta. En piezas de plástico son la falta de llenado, cuando la pieza sale incompleta, el rechupe, que es un hundimiento de la superficie, y las marcas. Una falla es el estado en que la matriz o el molde no cumple su función, y los defectos son sus síntomas.",
        "Las causas comunes de una falla son el desgaste, la holgura entre piezas, la desalineación, la falta de lubricación y los parámetros inadecuados. Detectar la causa exige comparar mediciones con el plano y con el historial. Revisar una matriz o un molde tiene riesgos: bordes filosos, superficies calientes, energía almacenada y piezas pesadas, por lo que solo lo hace personal autorizado con el equipo detenido y asegurado.",
        f"Aquí se aprenden los conceptos, no el diagnóstico en un equipo real. {EMER} {AVISO}",
    ],
    vocab=[("defecto", "característica de la pieza que no cumple lo pedido"), ("rebaba", "borde con material sobrante"), ("rechupe", "hundimiento de la superficie de una pieza de plástico"), ("falta de llenado", "pieza incompleta porque el plástico no llenó el molde"), ("falla", "estado en que la matriz o el molde no cumple su función"), ("holgura", "espacio excesivo entre piezas que deben calzar")],
    worked=[
        ("Reconocer un defecto", "Una pieza de chapa de ejemplo tiene un borde con material sobrante. ¿Qué defecto es?", ["El material sobrante en el borde tiene un nombre propio.", "Es una rebaba."], "Rebaba"),
        ("Falla o defecto", "Una matriz de ejemplo tiene el filo muy desgastado y produce rebabas. ¿Qué es el desgaste y qué es la rebaba?", ["El desgaste es la falla de la matriz.", "La rebaba es el defecto de la pieza."], "El desgaste es la falla y la rebaba es el defecto"),
    ],
    mistakes=[("Llamar defecto a la falla de la matriz.", "El defecto es lo que aparece en la pieza; la falla está en la herramienta.", "Distingue síntoma en la pieza y causa en la herramienta."),
              ("Revisar una matriz sin asegurar el equipo.", "Hay riesgos de aplastamiento y de energía almacenada.", "Solo personal autorizado revisa, con el procedimiento de la empresa.")],
    T=[
        ("abc", "En Matricería: ¿qué es una rebaba?", "Un borde con material sobrante", "Un hundimiento de la superficie", "Una pieza incompleta", "La rebaba es el exceso de material en el borde."),
        ("abc", "En Matricería: ¿qué es un rechupe?", "Un hundimiento de la superficie de una pieza de plástico", "Un borde con material sobrante", "Una grieta en la chapa", "El rechupe es un hundimiento en plástico."),
        ("abc", "En Matricería: ¿qué es una falla de una matriz?", "El estado en que no cumple su función", "Un defecto en la pieza fabricada", "Una pieza de repuesto", "La falla está en la herramienta; el defecto aparece en la pieza."),
        ("abc", "{F} ¿Cuál de los defectos de la lista es de piezas de plástico?", "Falta de llenado", "Rebaba", "Grieta en chapa", "La falta de llenado ocurre al inyectar plástico."),
        ("abc", "{F} ¿Cuál de las causas de la lista es un espacio excesivo entre piezas?", "Holgura", "Desalineación", "Falta de lubricación", "La holgura es espacio excesivo entre piezas."),
        ("abc", "{F} ¿Cuál es la diferencia entre defecto y falla en la ficha?", "El defecto aparece en la pieza y la falla está en la matriz o el molde", "Son lo mismo", "El defecto está en la herramienta y la falla en la pieza", "Son conceptos distintos con ubicación distinta."),
        ("=", "{F} La ficha lista 3 defectos de chapa y 3 de plástico. ¿Cuántos defectos suma?", "3+3", "Se suman los defectos de chapa y de plástico.", " defectos"),
        ("=", "{F} La ficha lista 5 causas comunes. Si se revisan 4 equipos con las 5 causas cada uno, ¿cuántas revisiones de causa se hacen?", "4*5", "Se multiplican los equipos por las causas revisadas en cada uno.", " revisiones"),
        ("abc", "{F} Una pieza sale con un borde con material sobrante. ¿Qué causa de falla es posible?", "El filo desgastado o la holgura entre punzón y matriz hembra", "Un exceso de plástico", "Un color de chapa distinto", "El desgaste y la holgura producen rebabas."),
        ("abc", "{F} Un operario dice: «el defecto es la matriz». ¿Qué observación es correcta?", "El defecto aparece en la pieza; la matriz presenta una falla que lo produce", "Es correcto, porque la matriz es el problema", "Es correcto, si la matriz es vieja", "Hay que distinguir defecto de falla."),
        ("abc", "En una visita a un taller de ejemplo, una persona se corta con la rebaba de una pieza y sangra mucho. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Presionar la herida con las manos sin protección", "Seguir trabajando", "Los primeros auxilios los hacen quienes tienen formación."),
        ("=", "{F} En una semana se revisan 7 matrices por día durante 5 días. ¿Cuántas revisiones documentales se hacen?", "7*5", "Se multiplican las matrices por los días.", " revisiones"),
        ("abc", "{F} Un estudiante dice: «yo reviso una matriz que acaba de parar, está lista». ¿Qué respuesta es correcta?", "Es falso: la revisión la hace personal autorizado con el equipo detenido y asegurado", "Es cierto, porque ya paró", "Es cierto, si usa guantes", "Hay energía almacenada y bordes filosos."),
    ],
    ctx=("abc", "Un amigo de ejemplo te dice: «arreglemos la matriz del colegio con una lima, tiene rebabas». ¿Qué respondes?", "Que no, porque intervenir una matriz exige personal autorizado, y que consultarás a un adulto responsable", "Que sí, con guantes", "Que sí, si la lima es nueva", "Este cuaderno no habilita para intervenir matrices."),
    sc=[
        ("En Matricería: ¿qué defecto es la falta de llenado?", "Una pieza incompleta", "El plástico no llenó toda la cavidad."),
        ("En Matricería: ¿qué es la holgura?", "Un espacio excesivo entre piezas que deben calzar", "Es una causa común de falla."),
        ("En Matricería: ¿quién revisa una matriz detenida?", "Personal autorizado", "Hay riesgos de energía y bordes filosos."),
    ],
    op=("Ficha de ejemplo: una matriz de corte produce piezas con rebabas desde hace una semana. Peligros: bordes filosos y energía almacenada. Escribe (a) qué es el defecto y qué es la falla, (b) dos causas comunes posibles, (c) quién revisa la matriz, (d) un control administrativo para la revisión. No expliques cómo se repara.",
        "(a) El defecto es la rebaba en la pieza; la falla es el estado de la matriz que no corta bien. (b) Desgaste del filo y holgura entre punzón y matriz hembra. (c) Personal autorizado. (d) Bloqueo y etiquetado, y una orden de trabajo para la revisión.",
        ["distingue defecto y falla", "nombra dos causas", "indica quién revisa", "propone un control administrativo"],
        ["hoja con las cuatro respuestas"],
        ["confundir defecto con falla", "proponer repararla uno mismo", "no mencionar a personal autorizado"],
        "Pregunta: «¿qué aparece en la pieza y qué está en la herramienta?». Si duda, pídele que relea las definiciones."),
    reinforce="Escribe tres defectos de piezas y una causa posible de falla para cada uno.",
    extend="Explica con un ejemplo por qué distinguir defecto y falla ayuda a encontrar la causa.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 2 (herramientas de calidad y documentos, de ejemplo e inventados). Diagrama de causa y efecto: dibujo que ordena las posibles causas de un problema en grupos (máquina, material, método, medición, personas). Hoja de control: tabla donde se anota cada defecto que aparece. "
     "Informe de no conformidad: documento que describe un incumplimiento. Registro de mantención de la matriz. Gráfico de control: gráfico que muestra una medida en el tiempo con límites; un punto fuera de los límites avisa de un problema. "
     "Plan de inspección de ejemplo: se mide 1 de cada 10 piezas. Roles: matricero, inspector de calidad, operador y supervisor.")
build(
    O3, 2, F,
    use="Aprenderé qué son el diagrama de causa y efecto, la hoja de control, el gráfico de control y el informe de no conformidad, y qué rol cumple cada persona en el control de calidad.",
    prior=["Sé qué es un defecto y una falla.", "Sé qué es una no conformidad.", "Sé leer una tabla."],
    explain=[
        "El diagrama de causa y efecto ordena las posibles causas de un problema en grupos como máquina, material, método, medición y personas, para no pasar por alto ninguna. La hoja de control es una tabla donde se anota cada defecto que aparece, con fecha y cantidad. El gráfico de control muestra una medida a lo largo del tiempo con límites superior e inferior; un punto fuera de los límites avisa de un problema.",
        "El informe de no conformidad describe un incumplimiento y el registro de mantención guarda las intervenciones de la matriz. El plan de inspección dice cada cuántas piezas se mide. El operador anota, el inspector mide y registra, el matricero analiza la herramienta y el supervisor decide. Las decisiones se basan en datos, no en suposiciones.",
        f"Aquí se aprenden documentos y herramientas de papel. {EMER} {AVISO}",
    ],
    vocab=[("diagrama de causa y efecto", "dibujo que ordena las causas posibles de un problema en grupos"), ("hoja de control", "tabla donde se anota cada defecto que aparece"), ("gráfico de control", "gráfico de una medida en el tiempo con límites superior e inferior"), ("plan de inspección", "documento que dice cada cuántas piezas se mide"), ("matricero", "persona especialista en construir y mantener matrices y moldes")],
    worked=[
        ("Elegir la herramienta", "Un taller de ejemplo quiere ordenar las posibles causas de un problema en grupos. ¿Qué herramienta usa?", ["Necesita ordenar causas por grupos.", "Usa el diagrama de causa y efecto."], "El diagrama de causa y efecto"),
        ("Leer el gráfico", "En un gráfico de control de ejemplo, un punto queda sobre el límite superior. ¿Qué avisa?", ["Fuera de los límites avisa un problema.", "Hay que investigar la causa."], "Un posible problema a investigar"),
    ],
    mistakes=[("Anotar los defectos de memoria al final del día.", "Se pierden datos y el registro queda impreciso.", "Anota en la hoja de control cuando aparecen."),
              ("Ignorar un punto fuera de límites porque «las piezas se ven bien».", "Puede avisar de un problema antes de que se note.", "Investiga la causa.")],
    T=[
        ("abc", "En Matricería: ¿para qué sirve el diagrama de causa y efecto?", "Para ordenar las posibles causas de un problema en grupos", "Para medir las piezas", "Para calcular el costo de la matriz", "En este caso, ordena causas por grupos."),
        ("abc", "En Matricería: ¿qué es una hoja de control?", "Una tabla donde se anota cada defecto que aparece", "Un plano de la matriz", "Un certificado de calibración", "La hoja de control registra defectos."),
        ("abc", "En Matricería: ¿qué avisa un punto fuera de los límites de un gráfico de control?", "Un posible problema a investigar", "Que todo está bien", "Que hay que cambiar el gráfico", "Fuera de límites es una alerta."),
        ("abc", "{F} ¿Cuál de los grupos de causas del diagrama se relaciona con el instrumento?", "Medición", "Material", "Personas", "En este caso, La medición incluye los instrumentos."),
        ("abc", "{F} ¿Qué documento describe un incumplimiento?", "El informe de no conformidad", "La hoja de control", "El gráfico de control", "En este caso, El informe describe el incumplimiento."),
        ("abc", "{F} ¿Quién mide y registra en el control de calidad?", "El inspector de calidad", "El operador solamente", "El supervisor", "En este caso, El inspector mide y registra."),
        ("=", "{F} Se produce un lote de 500 piezas y se mide 1 de cada 10. ¿Cuántas piezas se miden?", "500//10", "Se divide el lote entre el intervalo de inspección.", " piezas"),
        ("=", "{F} El diagrama tiene 5 grupos de causas y en cada uno se anotan 3 causas posibles. ¿Cuántas causas hay en total?", "5*3", "Se multiplican los grupos por las causas de cada uno.", " causas"),
        ("=", "{F} Una hoja de control anota 12 defectos de un tipo, 8 de otro y 5 de un tercero. ¿Cuántos defectos suma?", "12+8+5", "Se suman los defectos de los tres tipos.", " defectos"),
        ("abc", "{F} Un operario dice: «mido todas las piezas cuando quiero y no anoto nada». ¿Qué respuesta es correcta?", "No corresponde: el plan de inspección fija cada cuánto se mide y todo se anota", "Corresponde, porque mide más", "Corresponde, si no hay defectos", "En este caso, sin registro no hay evidencia."),
        ("abc", "{F} Un punto sale del límite superior de un gráfico de control. El supervisor dice «no importa, las piezas pasan». ¿Qué respuesta es correcta?", "Conviene investigar la causa antes de que aparezcan defectos", "Tiene razón, no importa", "Hay que borrar el punto", "Una alerta temprana permite corregir antes del defecto."),
        ("=", "{F} Si el plan mide 1 de cada 10 y se cambia a 1 de cada 5 para un lote de 500, ¿cuántas piezas más se miden?", "500//5-500//10", "Se calcula las piezas medidas con cada plan y se resta.", " piezas"),
        ("En una hoja de control de ejemplo hay 15 rebabas y 5 grietas. ¿Qué defecto es el más frecuente?", "La rebaba", "En este caso, 15 es mayor que 5."),
    ],
    ctx=("abc", "El jefe de ejemplo dice: «no necesitamos hoja de control, nos acordamos de los defectos». ¿Qué propones?", "Registrar los defectos en una hoja de control para analizar con datos", "Confiar en la memoria", "Anotar solo los graves", "En este caso, los datos permiten decidir mejor."),
    sc=[
        ("En Matricería: ¿qué muestra un gráfico de control?", "Una medida a lo largo del tiempo con límites", "Permite ver una tendencia o una alerta."),
        ("En Matricería: ¿qué describe el informe de no conformidad?", "Un incumplimiento", "Registra qué ocurrió y qué se decide."),
        ("En Matricería: ¿quién analiza la herramienta?", "El matricero", "Es el especialista en matrices y moldes."),
    ],
    op=("Ficha de ejemplo: un lote de 400 piezas se inspecciona midiendo 1 de cada 8. La hoja de control anota 9 rebabas, 4 deformaciones y 2 grietas. Escribe (a) cuántas piezas se miden, (b) cuántos defectos suma la hoja, (c) cuál es el defecto más frecuente, (d) qué herramienta usarías para ordenar las posibles causas.",
        "(a) 400 ÷ 8 = 50 piezas. (b) 9 + 4 + 2 = 15 defectos. (c) La rebaba. (d) El diagrama de causa y efecto.",
        ["calcula las piezas medidas", "suma los defectos", "identifica el más frecuente", "nombra la herramienta"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "sumar mal", "nombrar la herramienta equivocada"],
        "Pregunta: «¿cuál número es el mayor?». Si duda, pídele que compare las cantidades."),
    reinforce="Escribe cuatro herramientas de calidad y para qué sirve cada una.",
    extend="Explica con un ejemplo por qué un gráfico de control avisa antes que la pieza salga defectuosa.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 3 (registro de defectos de una semana, de ejemplo e inventado). Se produjeron 10.000 piezas de chapa con la matriz M-05 y se registraron estos defectos: rebaba, 120; deformación, 30; grieta, 20; marca, 10; otros, 20. "
     "Un análisis de Pareto ordena los defectos de mayor a menor frecuencia y muestra el porcentaje acumulado. Datos adicionales: el último afilado de la matriz fue hace 80.000 golpes y la pauta pide cada 50.000. Espesor de la rebaba tolerado de ejemplo: 50 µm; se midieron rebabas de 130 µm en una pieza.")
build(
    O3, 3, F,
    use="Aprenderé a analizar en papel un registro de defectos con un análisis de Pareto y a relacionar el defecto principal con una causa posible usando datos de mantención.",
    prior=["Sé qué es una hoja de control.", "Sé sumar y calcular porcentajes de números redondos.", "Sé qué es una causa posible."],
    explain=[
        "Un análisis de Pareto ordena los defectos de mayor a menor frecuencia, calcula el porcentaje de cada uno sobre el total de defectos y el porcentaje acumulado. Normalmente pocos defectos concentran la mayor parte de los problemas, por lo que conviene atacar primero los más frecuentes. El porcentaje de un defecto es sus unidades por 100 dividido por el total de defectos.",
        "Para relacionar el defecto principal con una causa se revisan datos de mantención, como los golpes desde el último afilado, y mediciones, como el espesor de la rebaba. Una causa posible se verifica con datos antes de actuar. Las decisiones las toma la jefatura y las intervenciones las hace personal autorizado.",
        f"El análisis es de papel. {EMER} {AVISO}",
    ],
    vocab=[("análisis de Pareto", "ordenamiento de defectos de mayor a menor frecuencia con porcentajes"), ("porcentaje acumulado", "suma de los porcentajes desde el defecto más frecuente"), ("defecto principal", "el más frecuente"), ("golpes desde el último afilado", "uso acumulado del filo de la matriz"), ("rebaba tolerada", "espesor de rebaba que se acepta")],
    worked=[
        ("Calcular un porcentaje", "En un registro de ejemplo hay 25 rebabas de 100 defectos. ¿Qué porcentaje es?", ["Se multiplican 25 por 100: 2.500.", "2.500 dividido en 100 son 25."], "25 %"),
        ("Atrasar", "Una pauta pide afilar cada 40.000 golpes y la matriz lleva 60.000 desde el último afilado. ¿Cuántos golpes se pasó?", ["Se resta la pauta a los golpes.", "60.000 menos 40.000 son 20.000."], "20.000 golpes"),
    ],
    mistakes=[("Atacar primero el defecto más fácil de arreglar y no el más frecuente.", "El más frecuente concentra el mayor problema.", "Ordena por frecuencia y empieza por el principal."),
              ("Afirmar una causa sin datos.", "Una suposición puede llevar a una acción equivocada.", "Verifica la causa con mediciones y registros.")],
    T=[
        ("abc", "En Matricería: ¿qué ordena un análisis de Pareto?", "Los defectos de mayor a menor frecuencia", "Los defectos por fecha", "Las piezas por peso", "En este caso, pareto ordena por frecuencia."),
        ("abc", "En Matricería: ¿qué es el defecto principal?", "El más frecuente", "El más grave en apariencia", "El último que apareció", "En este caso, Se define por frecuencia."),
        ("abc", "En Matricería: ¿cómo se calcula el porcentaje de un defecto?", "Sus unidades por 100 dividido por el total de defectos", "Sus unidades dividido por 100", "El total por 100 dividido por sus unidades", "Es una proporción sobre el total."),
        ("=", "{F} ¿Cuántos defectos suma el registro?", "120+30+20+10+20", "Se suman los defectos de todos los tipos.", " defectos"),
        ("abc", "{F} ¿Cuál es el defecto principal?", "La rebaba", "La deformación", "La grieta", "La rebaba tiene 120 defectos, el mayor número."),
        ("=", "{F} ¿Qué porcentaje de los defectos es rebaba?", "120*100//200", "Se multiplican las rebabas por 100 y se dividen por el total de 200.", " %"),
        ("=", "{F} ¿Qué porcentaje de los defectos es deformación?", "30*100//200", "Se multiplican por 100 y se dividen por el total de 200.", " %"),
        ("=", "{F} ¿Cuál es el porcentaje acumulado de rebaba y deformación?", "(120+30)*100//200", "Se suman ambas, se multiplican por 100 y se dividen por el total.", " %"),
        ("=", "{F} ¿Cuántos golpes se pasó la matriz respecto de la pauta de afilado?", "80000-50000", "Se resta la pauta a los golpes desde el último afilado.", " golpes"),
        ("abc", "{F} ¿Qué relación hay entre la rebaba y el atraso del afilado?", "Un filo desgastado por atraso es una causa posible de las rebabas, a verificar", "No hay ninguna relación", "El afilado atrasado produce grietas siempre", "El filo desgastado puede producir rebabas."),
        ("abc", "{F} Un jefe dice: «seguro es el material, cambiemos de proveedor». ¿Qué respuesta es adecuada?", "Conviene verificar con datos; la rebaba y el afilado atrasado apuntan a la herramienta", "Tiene razón, el material siempre es la causa", "Hay que culpar al operador", "La decisión se apoya en los datos disponibles."),
        ("=", "{F} La rebaba medida de 130 µm, ¿cuántos µm supera la tolerancia de 50 µm?", "130-50", "Se resta la tolerancia a la medida.", " µm"),
        ("En una semana de ejemplo hay 40 rebabas, 20 marcas y 20 grietas. ¿Cuál es el porcentaje acumulado de rebabas y marcas?", "75 %", "Rebabas y marcas suman 60; 60 por 100 dividido en 80 son 75."),
    ],
    ctx=("abc", "El jefe de ejemplo propone revisar todos los defectos por igual. ¿Qué le propones?", "Usar Pareto para empezar por el defecto más frecuente", "Revisarlos por orden alfabético", "Ignorar los más frecuentes", "En este caso, pareto ayuda a priorizar."),
    sc=[
        ("En Matricería: ¿cuánto es el 40 % de 50 defectos?", "20", "Se multiplica 50 por 40 y se divide por 100."),
        ("En Matricería: ¿qué defecto se ataca primero según Pareto?", "El más frecuente", "Concentra la mayor parte del problema."),
        ("En Matricería: ¿qué se hace antes de afirmar una causa?", "Se verifica con datos", "En este caso, una suposición no basta."),
    ],
    op=("Ficha de ejemplo: registro de una semana, 5.000 piezas: rebaba, 60; deformación, 25; grieta, 10; marca, 5. Pauta de afilado cada 30.000 golpes y la matriz lleva 45.000. Escribe (a) el total de defectos, (b) el defecto principal y su porcentaje, (c) el porcentaje acumulado de los dos más frecuentes, (d) una causa posible a verificar con los datos.",
        "(a) 60 + 25 + 10 + 5 = 100 defectos. (b) La rebaba, 60 %. (c) (60 + 25) × 100 ÷ 100 = 85 %. (d) El afilado atrasado en 15.000 golpes, que puede dar un filo desgastado.",
        ["suma los defectos", "calcula el porcentaje", "calcula el acumulado", "propone una causa a verificar"],
        ["hoja con las cuatro respuestas"],
        ["no ordenar por frecuencia", "calcular mal el porcentaje", "afirmar la causa sin verificar"],
        "Pregunta: «¿cuál es el defecto con más unidades?». Si duda, pídele que ordene la lista."),
    reinforce="Inventa un registro de cuatro defectos y calcula el porcentaje de cada uno.",
    extend="Explica con un ejemplo por qué conviene atacar primero el defecto más frecuente.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 4 (control de proceso de ejemplo, inventado). Una dimensión de una pieza se controla midiendo una muestra de 5 piezas cada hora. Especificación: 20.000 µm con tolerancia de ±30 µm. Límites de control de ejemplo del taller: de 19.980 a 20.020 µm para el promedio de la muestra. "
     "Muestras de cinco horas consecutivas (promedios, en µm): hora 1, 20.005; hora 2, 20.010; hora 3, 20.015; hora 4, 20.020; hora 5, 20.025. Regla del taller: si el promedio sale de los límites, se detiene el proceso y se avisa a la jefatura; si sube en tres muestras seguidas, se investiga. Costo de ejemplo de una hora de parada: $40.000. Costo de una pieza fuera de tolerancia: $500.")
build(
    O3, 4, F,
    use="Aprenderé a leer una serie de promedios de un control de proceso, a aplicar reglas de alerta y de detención y a comparar el costo de parar con el de seguir produciendo defectos.",
    prior=["Sé qué es un gráfico de control.", "Sé calcular un promedio de números enteros.", "Sé comparar un valor con un límite."],
    explain=[
        "En un control de proceso se mide una muestra de piezas cada cierto tiempo y se calcula el promedio. Cada promedio se compara con los límites de control; un promedio dentro de ellos indica un proceso estable, y uno fuera indica un problema. También se observa la tendencia: si los promedios suben varias veces seguidas, aunque estén dentro de los límites, el proceso se está desplazando y conviene investigar.",
        "Los límites de control son más estrechos que la tolerancia de la pieza: avisan antes de que las piezas salgan fuera de especificación. Detener el proceso cuesta, pero seguir produciendo piezas fuera de tolerancia también cuesta, y mucho más cuando son muchas. La decisión se basa en las reglas del taller y la toma la jefatura. Los valores son de ejemplo.",
        f"El análisis es de papel. {EMER} {AVISO}",
    ],
    vocab=[("muestra", "grupo pequeño de piezas medidas en un momento"), ("promedio de la muestra", "suma de las medidas dividida por el número de piezas"), ("límites de control", "valores entre los cuales el proceso se considera estable"), ("tendencia", "dirección en que cambian los promedios en el tiempo"), ("especificación", "valor y tolerancia pedidos en el plano")],
    worked=[
        ("Promedio", "Tres piezas de ejemplo miden 100, 104 y 108 µm sobre un valor base. ¿Cuál es el promedio?", ["La suma es 312.", "312 dividido en 3 son 104."], "104"),
        ("Tendencia", "Los promedios de ejemplo de cuatro horas son 10, 12, 14 y 16. ¿Cómo es la tendencia?", ["Cada promedio es mayor que el anterior.", "La tendencia es ascendente."], "Ascendente"),
    ],
    mistakes=[("Esperar a que el promedio salga de la tolerancia para actuar.", "Para entonces ya hay piezas defectuosas.", "Usa los límites de control y la tendencia como alerta temprana."),
              ("Mirar solo el último promedio.", "Una tendencia ascendente se ve en la serie.", "Compara varios promedios seguidos.")],
    T=[
        ("abc", "En Matricería: ¿qué son los límites de control?", "Los valores entre los cuales el proceso se considera estable", "La tolerancia del plano", "El costo de una parada", "Los límites avisan antes de salir de la tolerancia."),
        ("abc", "En Matricería: ¿qué es una tendencia?", "La dirección en que cambian los promedios en el tiempo", "El promedio de una sola muestra", "El valor del plano", "En este caso, Se ve comparando varios promedios."),
        ("abc", "En Matricería: ¿cómo se calcula el promedio de una muestra?", "Sumando las medidas y dividiendo por el número de piezas", "Multiplicando todas las medidas", "Restando la menor a la mayor", "El promedio es la suma entre la cantidad."),
        ("=", "{F} ¿Cuántos µm sube el promedio entre la hora 1 y la hora 5?", "20025-20005", "Se resta el promedio de la hora 1 al de la hora 5.", " µm"),
        ("abc", "{F} ¿Qué promedio llega justo al límite superior de control?", "El de la hora 4, de 20.020 µm", "El de la hora 1", "El de la hora 5", "En este caso, El límite superior es 20.020."),
        ("abc", "{F} ¿Qué promedio sale de los límites de control?", "El de la hora 5, de 20.025 µm", "El de la hora 3", "Ninguno", "La razón es que 20.025 supera 20.020."),
        ("abc", "{F} ¿Está el promedio de la hora 5 dentro de la tolerancia de la pieza (±30 µm)?", "Sí, porque se aparta 25 µm y la tolerancia es de 30 µm", "No, porque supera el límite de control", "No, porque es mayor que 20.000", "Está dentro de la tolerancia aunque fuera del límite de control."),
        ("abc", "{F} Según la regla del taller, ¿qué corresponde hacer en la hora 5?", "Detener el proceso y avisar a la jefatura, porque el promedio salió de los límites", "Seguir produciendo porque cumple la tolerancia", "Cambiar los límites", "La regla manda detener cuando sale de los límites."),
        ("abc", "{F} ¿Qué regla se activó antes, en las horas 2 y 3?", "La de tendencia: sube en tres muestras seguidas desde la hora 1", "La de detención", "Ninguna", "Los promedios 20.005, 20.010 y 20.015 suben seguidos."),
        ("abc", "{F} Un jefe dice: «las piezas están dentro de la tolerancia, no hay que parar». ¿Qué respuesta es correcta?", "Conviene aplicar la regla de control: la tendencia y el límite avisan antes de que haya defectos", "Tiene razón, no hay que parar", "Hay que borrar los datos altos", "Los límites de control son más estrechos para actuar a tiempo."),
        ("=", "{F} Si parar una hora cuesta $40.000 y seguir produciendo 100 piezas fuera de tolerancia cuesta $500 cada una, ¿cuánto cuesta seguir?", "100*500", "Se multiplican las piezas por el costo de cada una.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántos pesos más cuesta seguir con 100 piezas fuera de tolerancia que parar una hora?", "100*500-40000", "Se resta el costo de parar al costo de seguir.", " pesos de ejemplo"),
        ("Cinco piezas de ejemplo miden 20.000; 20.010; 20.020; 20.030 y 20.040 µm. ¿Cuál es el promedio?", "20.020 µm", "La suma es 100.100 y dividida en 5 son 20.020."),
    ],
    ctx=("abc", "El supervisor de ejemplo dice: «paremos solo si una pieza sale del plano». ¿Qué propones?", "Aplicar los límites de control y la tendencia como alerta temprana", "Esperar a que haya piezas defectuosas", "Medir menos piezas", "En este caso, La alerta temprana evita pérdidas."),
    sc=[
        ("En Matricería: ¿cuál es el promedio de 200, 206 y 212?", "206", "Se suman las tres medidas y se divide por 3."),
        ("En Matricería: ¿qué avisa una tendencia ascendente?", "Que el proceso se está desplazando", "Conviene investigar antes de salir de los límites."),
        ("En Matricería: ¿qué es más estrecho, los límites de control o la tolerancia?", "Los límites de control", "Avisan antes de salir de la tolerancia."),
    ],
    op=("Ficha de ejemplo: especificación 10.000 µm ±20 µm. Límites de control para el promedio: 9.990 a 10.010 µm. Promedios de cuatro horas: 10.002; 10.006; 10.009; 10.012. Regla: si sale de los límites se detiene; si sube en tres muestras seguidas se investiga. Escribe (a) cuántos µm sube el promedio entre la primera y la última hora, (b) qué hora sale de los límites, (c) si está dentro de la tolerancia, (d) qué dice la regla.",
        "(a) 10.012 − 10.002 = 10 µm. (b) La cuarta hora, porque 10.012 supera 10.010. (c) Sí, se aparta 12 µm y la tolerancia es de 20 µm. (d) Detener el proceso y avisar a la jefatura; además hubo tendencia ascendente desde la primera hora.",
        ["calcula la subida", "detecta la hora fuera", "compara con la tolerancia", "aplica la regla"],
        ["hoja con las cuatro respuestas"],
        ["confundir límite de control con tolerancia", "mirar solo el último dato", "no aplicar la regla"],
        "Pregunta: «¿cuál es el límite de control?». Si duda, pídele que relea el enunciado."),
    reinforce="Inventa cuatro promedios y decide si alguno sale de unos límites que tú definas.",
    extend="Explica con un ejemplo por qué los límites de control son más estrechos que la tolerancia.",
)
