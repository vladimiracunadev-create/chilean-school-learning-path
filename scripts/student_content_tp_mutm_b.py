"""Muebles y Terminaciones en Madera (3.º y 4.º medio TP): OAE-03 (cubicar materiales e insumos: listas de materiales, merma, aprovechamiento de tableros y presupuestos) y OAE-04 (fabricar partes y piezas: riesgos del taller, órdenes de trabajo, programación y tolerancias, solo conceptos y planillas). Datos de ejemplo."""
from __future__ import annotations

from tp_mutm_common import AVISO, EMER, build

O3 = "TP-MUTM-3y4-OAE-03"
O4 = "TP-MUTM-3y4-OAE-04"
TAIL = f"{EMER} {AVISO}"

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (pedido de ejemplo, inventado). El taller ficticio «Carpintería Los Boldos» debe cubicar el material para 8 bancas. Cada banca lleva 4 patas de 45 cm, 1 asiento de tablero de 120 cm por 30 cm y 2 travesaños de 100 cm. "
     "Riesgos anotados: un faltante de material por mala cubicación, que presiona a improvisar con piezas no previstas; un sobrante que ocupa espacio y se apila mal; y residuos (aserrín y recortes) que se acumulan y aumentan el riesgo de incendio. "
     "Medidas anotadas: revisar la lista de piezas con una segunda persona, firmar el registro de cubicación, mantener pilas ordenadas en la bodega y programar el retiro de residuos.")
build(
    O3, 1, F,
    use="Aprenderé qué es cubicar, por qué la cubicación afecta la seguridad y el costo, y qué es la merma.",
    prior=["Sé multiplicar y sumar.", "Sé leer un despiece.", "Sé qué es un registro."],
    explain=[
        "Cubicar es calcular qué cantidad de cada material e insumo se necesita para fabricar o reparar un mueble, siguiendo los planos y las especificaciones técnicas. Se parte del despiece y se multiplica la cantidad de piezas de cada mueble por la cantidad de muebles. La merma es la parte del material que se pierde o no se aprovecha, como recortes y aserrín; por eso la cantidad a comprar suele ser algo mayor que la cantidad estrictamente necesaria.",
        "Una cubicación mal hecha tiene consecuencias. Si falta material, aparece la presión por terminar y se improvisa con piezas que no corresponden. Si sobra mucho, se pagan costos innecesarios, el espacio de la bodega se llena y las pilas se vuelven inestables. Los residuos de madera, como el aserrín y los recortes, se acumulan y pueden incendiarse, por lo que su retiro se programa. Para evitar errores, otra persona revisa la lista y el responsable firma el registro.",
        TAIL,
    ],
    vocab=[("cubicar", "calcular las cantidades de material e insumos que se necesitan según planos y especificaciones"), ("lista de materiales", "documento que enumera los materiales y la cantidad de cada uno"), ("merma", "parte del material que se pierde o no se aprovecha"), ("sobrante", "material que queda sin usar después de la fabricación"), ("residuo", "material descartado, como aserrín y recortes"), ("registro de cubicación", "documento firmado donde se anotan los cálculos")],
    worked=[
        ("Cantidad por pedido", "Un mueble de ejemplo lleva 6 patas y se piden 5 muebles. ¿Cuántas patas se necesitan?", ["Se multiplican las patas de cada mueble por los muebles pedidos.", "6 por 5 son 30."], "30 patas"),
        ("Aplicar una merma", "Se necesitan 50 m de listón y la merma de ejemplo es de 10 %. ¿Cuántos metros conviene comprar?", ["La merma es 10 % de 50, es decir 5 m.", "Se suman 50 y 5."], "55 m"),
    ],
    mistakes=[("Comprar el doble «por si acaso».", "El sobrante cuesta dinero, ocupa espacio y puede generar pilas inestables.", "Se calcula la cantidad con una merma razonable y se revisa."),
              ("Cubicar sin que nadie revise la lista.", "Un error de multiplicación puede pasar inadvertido.", "Una segunda persona revisa y el responsable firma el registro.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es cubicar?", "Calcular las cantidades de material necesarias según planos y especificaciones", "Cortar las piezas a la medida del plano", "Medir la humedad de las tablas recibidas", "Cubicar es calcular cantidades; cortar y medir humedad son otras tareas."),
        ("abc", "En la cubicación de un mueble, ¿qué es la merma?", "La parte del material que se pierde o no se aprovecha", "El material que el cliente entrega para reparar", "El precio total del mueble", "La merma son recortes y aserrín que no pasan a formar parte del mueble."),
        ("=", "{F} ¿Cuántas patas se necesitan para las 8 bancas?", "8*4", "Se multiplican las bancas por las patas de cada una.", " patas"),
        ("=", "{F} ¿Cuántos travesaños se necesitan para las 8 bancas?", "8*2", "Se multiplican las bancas por los travesaños de cada una.", " travesaños"),
        ("abc", "{F} Si por mala cubicación falta material, ¿qué riesgo anota la ficha?", "La presión por terminar lleva a improvisar con piezas no previstas", "Que sobrará madera para el año siguiente", "Que el aserrín se vuelva más liviano", "El faltante presiona a improvisar, que es la consecuencia que anota la ficha."),
        ("abc", "{F} ¿Qué medida de la ficha ayuda a detectar un error de multiplicación?", "Que otra persona revise la lista de piezas", "Que se compre más madera", "Que se guarde el aserrín en la bodega", "Una segunda revisión detecta errores que quien calculó no vio."),
        ("=", "{F} ¿Cuántos centímetros de travesaño se necesitan en total para las 8 bancas?", "8*2*100", "Se multiplican bancas, travesaños por banca y largo de cada travesaño.", " cm"),
        ("=", "{F} ¿Cuántos centímetros de patas se necesitan en total para las 8 bancas?", "8*4*45", "Se multiplican bancas, patas por banca y largo de cada pata.", " cm"),
        ("abc", "{F} El taller compra el doble de material «por si acaso». ¿Qué problema anota la ficha para un sobrante grande?", "Ocupa espacio y se apila mal", "Hace que las bancas salgan más livianas", "Reduce la merma a cero", "La ficha advierte que el sobrante ocupa espacio y se apila mal."),
        ("ab", "{F} Un compañero dice: «los recortes y el aserrín no importan, no son un riesgo». ¿Qué respuesta es correcta?", "No: se acumulan y pueden incendiarse, por eso se programa su retiro", "Sí: son material sin valor ni riesgo", "La ficha pide programar el retiro de residuos."),
        ("abc", "{F} Una estudiante dice: «ya cubico bancas, puedo manejar las máquinas de corte». ¿Qué respuesta es correcta?", "No: operar máquinas exige instructor autorizado y norma vigente", "Sí: cubicar habilita para operar", "Sí, si trabaja con guantes", "Cubicar es un cálculo en papel y no habilita para operar máquinas."),
        ("=", "{F} Si el taller agrega 2 bancas más al pedido, ¿cuántas patas se necesitan en total?", "(8+2)*4", "Se suman las bancas al pedido y se multiplican por las patas de cada una.", " patas"),
        ("abc", "{F} ¿Qué lleva el registro de cubicación firmado?", "Los cálculos, las cantidades y la firma del responsable", "Solo el color de las bancas", "Solo el nombre del cliente", "El registro deja constancia de los cálculos y de quien los aprobó."),
    ],
    ctx=("abc", "En una bodega de ejemplo, el aserrín acumulado empieza a humear cerca de un enchufe. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Apagarlo con las manos para evitar que crezca", "Esperar a que se apague solo", "Un conato de incendio se informa a quien corresponde y a emergencias, sin acercarse."),
    sc=[
        ("En Muebles y Terminaciones en Madera: ¿qué es la merma?", "La parte del material que se pierde o no se aprovecha", "La merma son los recortes y el aserrín que no se usan."),
        ("¿Qué se multiplica para obtener las piezas de un pedido?", "Las piezas de un mueble por la cantidad de muebles", "Así se pasa del despiece al total del pedido."),
        ("¿Por qué se programa el retiro de residuos de madera?", "Porque se acumulan y aumentan el riesgo de incendio", "El aserrín y los recortes acumulados son combustible."),
    ],
    op=("Pedido de ejemplo «Taller Quillay» (ficticio): 7 repisas. Cada repisa lleva 2 soportes de listón de 60 cm y 1 tabla de 90 cm. Merma de ejemplo: 10 % sobre los metros de tabla. Escribe (a) cuántos soportes se necesitan, (b) cuántos centímetros de tabla se necesitan sin merma, (c) cuántos centímetros comprar con la merma y (d) qué haces con los recortes de madera acumulados.",
        "(a) 7×2 son 14 soportes. (b) 7×90 son 630 cm. (c) 10 % de 630 son 63; 630+63 son 693 cm. (d) Se programa su retiro porque aumentan el riesgo de incendio.",
        ["calcula los soportes", "calcula los cm de tabla sin merma", "aplica la merma del 10 %", "propone retirar los residuos"],
        ["hoja con los cuatro cálculos"],
        ["olvidar multiplicar por las repisas", "aplicar la merma al número equivocado", "dejar acumular los recortes"],
        "Pregunta: «¿por qué conviene comprar algo más que lo calculado?». Si no responde, pídele que relea la definición de merma."),
    reinforce="Escribe con tus palabras qué ocurre si una cubicación calcula de menos y qué ocurre si calcula de más.",
    extend="Explica por qué la revisión de una segunda persona forma parte de la prevención de riesgos.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (planilla de cubicación de ejemplo, inventada). Taller ficticio, pedido de 5 sillas «S-1». "
     "Ítem A: listón para patas, 4 por silla, 40 cm cada una (merma 0 %). Ítem B: tablero de asiento, 1 por silla, de 40 cm por 40 cm (merma 0 %). Ítem C: listón de respaldo, 2 metros lineales por silla (merma de ejemplo 20 %). "
     "Columnas de la planilla: ítem, unidad, cantidad por silla, cantidad total, merma y cantidad a comprar. Una cotización es el precio por escrito que entrega un proveedor.")
build(
    O3, 2, F,
    use="Aprenderé a leer una planilla de cubicación: columnas, unidades, merma y quién usa cada documento.",
    prior=["Sé qué es cubicar y la merma.", "Sé calcular un porcentaje sencillo.", "Sé leer un despiece."],
    explain=[
        "La planilla de cubicación ordena el cálculo en filas y columnas: cada ítem lleva su unidad de medida, la cantidad por mueble, la cantidad total, la merma y la cantidad a comprar. La unidad depende del material: las piezas se cuentan en unidades, los listones en metros lineales (metros de largo), los tableros en unidades o en metros cuadrados, y la madera aserrada en metros cúbicos. Elegir mal la unidad es un error frecuente.",
        "La lista de materiales alimenta la planilla; la planilla se envía a compras para pedir una cotización, que es el precio por escrito de un proveedor, y después se emite la orden de compra. Quien cubica es el jefe de producción o su asistente; compras gestiona los precios; bodega comprueba lo que llega. Cada uno firma su parte para saber quién respondió por cada cifra. Todas las cantidades de esta clase son de ejemplo.",
        TAIL,
    ],
    vocab=[("planilla de cubicación", "tabla que ordena ítems, unidades, cantidades, merma y cantidad a comprar"), ("metro lineal", "metro de largo de un listón o moldura"), ("unidad de medida", "forma de contar un material: unidades, metros lineales, m² o m³"), ("cotización", "precio por escrito que entrega un proveedor"), ("cantidad a comprar", "cantidad total más la merma")],
    worked=[
        ("Elegir la unidad", "Un listón largo de ejemplo se compra por metros de largo. ¿Qué unidad de medida corresponde?", ["Lo que se mide es el largo.", "El largo se mide en metros lineales."], "Metros lineales"),
        ("Cantidad con merma", "Un ítem de ejemplo necesita 40 unidades y su merma es 25 %. ¿Cuántas unidades se compran?", ["25 % de 40 es 10.", "40 más 10 son 50."], "50 unidades"),
    ],
    mistakes=[("Contar un listón en unidades cuando se vende por metros.", "El proveedor cobra por largo, no por pieza.", "Se usa la unidad que el proveedor cobra: metros lineales."),
              ("Olvidar la merma en la columna de cantidad a comprar.", "La compra queda corta y falta material.", "Se suma la merma al total antes de comprar.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué muestra una planilla de cubicación?", "Ítems, unidades, cantidades, merma y cantidad a comprar", "El plano del mueble con sus cotas", "Los riesgos de la bodega", "La planilla ordena el cálculo de cantidades; el plano y los riesgos están en otros documentos."),
        ("abc", "En Muebles y Terminaciones en Madera: ¿Qué es una cotización?", "El precio por escrito que entrega un proveedor", "La cantidad de merma de un ítem", "La firma del bodeguero", "Cotizar es pedir y recibir un precio escrito."),
        ("=", "{F} ¿Cuántos listones de patas se necesitan en total para las 5 sillas?", "5*4", "Se multiplican las sillas por las patas de cada una.", " patas"),
        ("=", "{F} ¿Cuántos centímetros de listón de patas hay en total?", "5*4*40", "Se multiplican sillas, patas por silla y largo de cada pata.", " cm"),
        ("abc", "{F} ¿En qué unidad se cuenta el listón de respaldo?", "En metros lineales", "En metros cúbicos", "En unidades de tablero", "El respaldo se pide en metros de largo, es decir, metros lineales."),
        ("=", "{F} ¿Cuántos metros lineales de listón de respaldo se necesitan sin merma?", "5*2", "Se multiplican las sillas por los metros que lleva cada una.", " m"),
        ("=", "{F} ¿Cuántos metros lineales de listón de respaldo se compran con la merma de 20 %?", "10*120//100", "Se calcula el 120 % del total: el total más el 20 % de merma.", " m"),
        ("=", "{F} ¿Cuántos cm² de tablero de asiento se necesitan en total?", "5*40*40", "Se multiplican sillas, largo y ancho de cada asiento.", " cm²"),
        ("abc", "{F} ¿Quién gestiona los precios con los proveedores?", "Compras", "Bodega", "El cliente que pidió las sillas", "Compras pide cotizaciones; bodega recibe lo comprado."),
        ("abc", "{F} Una persona anota 10 m de listón de respaldo en la columna «cantidad a comprar». ¿Qué le falta?", "Sumar la merma de 20 %", "Dividir por 5 sillas", "Cambiar la unidad a m³", "La cantidad a comprar incluye la merma y aquí se anotó solo el total."),
        ("ab", "{F} Un estudiante dice: «los tableros de asiento no llevan merma, porque la ficha dice 0 %». ¿Qué respuesta es correcta?", "Sí: la ficha indica merma de 0 % en esos ítems", "No: todos los ítems llevan merma de 20 %", "La ficha rotula la merma de cada ítem por separado."),
        ("abc", "{F} Otra persona dice: «ya sé llenar la planilla, puedo armar las sillas». ¿Qué respuesta es correcta?", "No: armar exige instructor autorizado, norma vigente y EPP; la planilla no habilita", "Sí: llenar la planilla habilita para armar", "Sí, si trabaja con compañeros", "La planilla es un cálculo en papel y no habilita para trabajar en taller."),
        ("abc", "{F} Si bodega recibe menos listón del comprado, ¿qué corresponde?", "Registrar la diferencia y avisar a compras", "Corregir la planilla para que coincida", "Callar para no retrasar la producción", "La diferencia se registra y se informa; no se altera el documento."),
    ],
    ctx=("abc", "En una bodega de ejemplo, un trabajador resbala con aserrín en el piso y se golpea la cabeza. ¿Qué se hace según las reglas generales?", "No mover a la persona, avisar a un adulto responsable y a emergencias", "Levantarla de inmediato y llevarla caminando", "Dejarla sola hasta que se recupere", "Ante un golpe en la cabeza no se mueve a la persona y se avisa a quien corresponde y a emergencias."),
    sc=[
        ("¿En qué unidad se cuenta un listón largo?", "En metros lineales", "El listón se mide por su largo."),
        ("En Muebles y Terminaciones en Madera: ¿qué incluye la «cantidad a comprar»?", "El total más la merma", "La compra debe cubrir el material perdido."),
        ("¿Quién pide cotizaciones a los proveedores?", "Compras", "Compras gestiona precios con los proveedores."),
    ],
    op=("Planilla de ejemplo «Taller Peumo» (ficticio): 4 mesas «M-5». Ítem A: patas de listón, 4 por mesa, 70 cm cada una, merma 0 %. Ítem B: tapa de tablero, 1 por mesa, 120 cm por 60 cm, merma 0 %. Ítem C: listón de refuerzo, 5 metros lineales por mesa, merma de ejemplo 20 %. Escribe (a) las patas totales, (b) los cm² de tablero totales, (c) los metros lineales de refuerzo a comprar con la merma y (d) quién pide la cotización.",
        "(a) 4×4 son 16 patas. (b) 4×120×60 son 28.800 cm². (c) 4×5 son 20 m; con 20 % son 20×120÷100 = 24 m. (d) Compras.",
        ["calcula las patas", "calcula los cm² de tablero", "aplica la merma al listón", "nombra a compras"],
        ["hoja con los cuatro cálculos"],
        ["olvidar la merma", "multiplicar por 3 y no por 4 mesas", "confundir cotización con orden de compra"],
        "Pregunta: «¿qué columna de la planilla incluye la merma?». Si no responde, pídele que relea la explicación."),
    reinforce="Escribe tres ítems de una planilla de ejemplo para un mueble pequeño, con su unidad de medida.",
    extend="Explica qué pasa si el jefe de producción y compras usan unidades distintas para el mismo listón.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (caso de aprovechamiento de tableros de ejemplo, inventado). Un tablero de ejemplo mide 200 cm por 100 cm. Cada pieza pedida mide 60 cm por 50 cm. "
     "En la distribución dibujada caben 3 piezas a lo largo y 2 a lo ancho, es decir, 6 piezas por tablero, y no caben más. Se piden 26 piezas.")
build(
    O3, 3, F,
    use="Aprenderé a analizar cuántos tableros se necesitan según la distribución de las piezas, y a comparar con el cálculo solo por área.",
    prior=["Sé calcular el área de un rectángulo.", "Sé qué es la merma.", "Sé dividir con resto."],
    explain=[
        "Para cubicar tableros hay dos cálculos que se comparan. El cálculo por área divide el área total de las piezas por el área de un tablero. El cálculo por distribución cuenta cuántas piezas caben realmente en un tablero y divide las piezas pedidas por esa cantidad. Como las piezas no se pueden fraccionar entre tableros, el resultado de una división con resto se redondea siempre hacia arriba: un tablero incompleto igual se compra entero.",
        "El cálculo por área es un mínimo teórico: nunca da más que el real, y puede dar menos porque ignora cómo caben las piezas. Por eso la cubicación de tableros usa la distribución. El sobrante se anota: son las piezas que quedan de más en el último tablero y el área del tablero que no se aprovecha. Todo se calcula en papel y se deja registrado; la forma de cortar los tableros la enseña un instructor autorizado y no se trata aquí.",
        TAIL,
    ],
    vocab=[("distribución", "forma en que se acomodan las piezas sobre un tablero dibujado en papel"), ("área", "superficie de una pieza o tablero, en cm²"), ("redondear hacia arriba", "pasar al entero siguiente cuando una división deja resto"), ("aprovechamiento", "parte del tablero que realmente se usa en piezas"), ("sobrante", "piezas o superficie que quedan sin usar")],
    worked=[
        ("Redondear hacia arriba", "En un caso de ejemplo se pide 17 piezas y en cada tablero caben 4. ¿Cuántos tableros se necesitan?", ["17 dividido en 4 da 4 y sobra 1 pieza.", "Esa pieza necesita un tablero más: se redondea hacia arriba."], "5 tableros"),
        ("Área de una pieza", "Una pieza de ejemplo mide 30 cm por 20 cm. ¿Qué área tiene?", ["Se multiplican las dos medidas.", "30 por 20 son 600."], "600 cm²"),
    ],
    mistakes=[("Calcular los tableros solo dividiendo áreas.", "Ignora cómo caben las piezas y puede dar un número insuficiente.", "Se usa la distribución y se compara con el área como mínimo teórico."),
              ("Redondear hacia abajo.", "Quedarían piezas sin tablero.", "Si la división deja resto, se compra un tablero más.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué significa redondear hacia arriba al cubicar tableros?", "Comprar un tablero más cuando la división deja resto", "Cortar las piezas un poco más grandes", "Descartar las piezas que sobran", "Un tablero incompleto igual se compra entero."),
        ("abc", "¿Qué es el aprovechamiento de un tablero?", "La parte del tablero que realmente se usa en piezas", "El precio que paga el cliente", "El número de piezas que se descartan", "El aprovechamiento mide cuánto del tablero se usa."),
        ("=", "{F} ¿Cuántos cm² tiene un tablero?", "200*100", "El área de un rectángulo es largo por ancho.", " cm²"),
        ("=", "{F} ¿Cuántos cm² tiene una pieza?", "60*50", "El área de una pieza es largo por ancho.", " cm²"),
        ("=", "{F} ¿Cuántos cm² suman las 26 piezas pedidas?", "26*3000", "Se multiplican las piezas por el área de cada una (3.000 cm²).", " cm²"),
        ("abc", "{F} Dividiendo el área total de las piezas (78.000 cm²) por el área de un tablero (20.000 cm²) se obtiene 3,9. ¿Qué número entero da el cálculo por área al redondear hacia arriba?", "4 tableros", "3 tableros", "5 tableros", "3,9 redondeado hacia arriba es 4."),
        ("=", "{F} ¿Cuántas piezas entran en 4 tableros según la distribución?", "4*6", "Se multiplican los tableros por las 6 piezas que caben en cada uno.", " piezas"),
        ("abc", "{F} ¿Qué conclusión sale de comparar 24 piezas posibles en 4 tableros con las 26 pedidas?", "Con 4 tableros no alcanza; hacen falta 5", "Con 4 tableros sobra una pieza", "Con 4 tableros alcanza justo", "Con 4 tableros solo salen 24 piezas y se piden 26."),
        ("=", "{F} ¿Cuántos tableros se necesitan según la distribución (26 piezas, 6 por tablero, redondeando hacia arriba)?", "(26+5)//6", "Se divide 26 en 6 redondeando hacia arriba: 4 con resto y 1 más.", " tableros"),
        ("=", "{F} Con 5 tableros salen 30 piezas posibles. ¿Cuántas sobran de las 26 pedidas?", "30-26", "Se resta lo pedido de lo que salen en total.", " piezas"),
        ("abc", "{F} Una persona dice: «el cálculo por área da 4, así que compro 4 tableros». ¿Qué respuesta es correcta?", "No: la distribución exige 5, y el cálculo por área es solo un mínimo teórico", "Sí: el área siempre manda", "Sí, porque 3,9 se redondea hacia abajo", "El área no considera cómo caben las piezas; la distribución da lo real."),
        ("abc", "{F} Una estudiante dice: «si sé cuántos tableros comprar, sé cómo cortarlos con la máquina». ¿Qué respuesta es correcta?", "No: el corte lo enseña un instructor autorizado; la cubicación no habilita", "Sí: son lo mismo", "Sí, si compra tableros de mayor calidad", "Cubicar es un cálculo; operar una máquina exige autorización y capacitación."),
        ("=", "{F} Cada tablero tiene un área de 20.000 cm² y 6 piezas ocupan 18.000 cm². ¿Cuántos cm² de cada tablero no se aprovechan?", "20000-18000", "Se restan los cm² ocupados por piezas del área del tablero.", " cm²"),
    ],
    ctx=("abc", "En el taller de ejemplo, un tablero resbala de una pila y golpea el pie de una persona. ¿Qué se hace según las reglas generales?", "No mover la pila, avisar a un adulto responsable y a emergencias", "Levantar solo el tablero y seguir trabajando", "Esperar sin avisar si no hay sangre", "Se avisa a quien corresponde y a emergencias; no se improvisa con la pila inestable."),
    sc=[
        ("¿Por qué se redondea hacia arriba al contar tableros?", "Porque un tablero incompleto igual se compra entero", "Las piezas no se pueden fraccionar entre tableros."),
        ("En Muebles y Terminaciones en Madera: ¿qué es el cálculo por área al cubicar tableros?", "Un mínimo teórico que ignora cómo caben las piezas", "No considera cómo caben realmente las piezas en el tablero."),
        ("¿Qué se anota como sobrante?", "Las piezas de más y la superficie sin aprovechar", "El sobrante se registra para conocer el aprovechamiento."),
    ],
    op=("Caso de ejemplo «Taller Ñire» (ficticio): tablero de 200 cm por 100 cm; pieza cuadrada de 50 cm por 50 cm. En la distribución dibujada caben 4 piezas a lo largo y 2 a lo ancho, y no caben más (el área de 8 piezas llena justo el tablero). Se piden 30 piezas. Escribe (a) cuántas piezas caben por tablero, (b) cuántos tableros se necesitan según la distribución, (c) cuántas piezas sobran y (d) por qué no basta con dividir las áreas.",
        "(a) 4×2 son 8 piezas. (b) 30÷8 da 3 con resto 6; se necesitan 4 tableros. (c) 4×8 son 32 piezas posibles; sobran 2. (d) Porque el área ignora cómo caben las piezas y puede dar menos tableros de los reales.",
        ["calcula las piezas por tablero", "redondea hacia arriba", "calcula el sobrante", "explica la limitación del área"],
        ["hoja con las cuatro respuestas"],
        ["redondear hacia abajo", "no multiplicar 4 por 2", "creer que el área basta"],
        "Pregunta: «¿qué pasa con las 6 piezas que sobran después de 3 tableros?». Si no responde, pídele que relea la parte de redondear."),
    reinforce="Calcula cuántos tableros se necesitan si se piden 13 piezas y en cada tablero caben 4.",
    extend="Explica por qué dos tableros con la misma área pueden permitir un distinto número de piezas.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (presupuesto de ejemplo, inventado). Pedido de 6 muebles «V-2» del taller ficticio. Costos de ejemplo: 5 tableros a $34.000 cada uno; 30 metros lineales de listón a $1.500 el metro; 12 herrajes a $2.500 cada uno; mano de obra de $90.000 para todo el pedido. "
     "Margen de ejemplo: 20 % sobre el costo total. Alternativa de tablero de ejemplo: tablero B a $40.000 cada uno, con 4 tableros en lugar de 5.")
build(
    O3, 4, F,
    use="Aprenderé a armar un presupuesto de ejemplo: sumar costos, aplicar un margen y comparar alternativas de material.",
    prior=["Sé calcular un porcentaje sencillo.", "Sé cubicar con merma.", "Sé leer una cotización."],
    explain=[
        "Un presupuesto es el cálculo anticipado del costo de un pedido. Se suman los costos directos, que son los materiales y la mano de obra, y se agrega un margen, que es un porcentaje sobre el costo para cubrir gastos generales y obtener una ganancia. El precio de venta es el costo total más el margen. Dividir el precio de venta por el número de muebles da el precio por mueble.",
        "Cuando hay alternativas de material, se compara el costo total de cada una y no solo el precio unitario: una opción más cara por unidad puede ser más barata si se necesitan menos unidades. Un presupuesto confiable parte de una cubicación revisada y de cotizaciones por escrito. Todos los precios y porcentajes de esta clase son inventados; los valores reales los entregan los proveedores y las normas vigentes.",
        TAIL,
    ],
    vocab=[("presupuesto", "cálculo anticipado del costo de un pedido"), ("costo directo", "costo de materiales y mano de obra del pedido"), ("margen", "porcentaje sobre el costo para cubrir gastos y ganancia"), ("precio de venta", "costo total más margen"), ("alternativa", "otra opción de material o de diseño que se compara")],
    worked=[
        ("Sumar costos", "Un pedido de ejemplo tiene materiales por $80.000 y mano de obra por $20.000. ¿Cuál es el costo total?", ["Se suman los dos costos directos.", "80.000 más 20.000 son 100.000."], "$100.000"),
        ("Aplicar el margen", "Con costo de $100.000 y margen de ejemplo de 10 %, ¿cuál es el precio de venta?", ["El 10 % de 100.000 es 10.000.", "Se suma al costo."], "$110.000"),
    ],
    mistakes=[("Aplicar el margen solo a los materiales.", "El margen cubre el costo total del pedido.", "Se calcula el margen sobre materiales más mano de obra."),
              ("Elegir la alternativa solo por el precio unitario.", "Una opción más cara por unidad puede necesitar menos unidades.", "Se compara el costo total de cada alternativa.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es el margen de un presupuesto?", "Un porcentaje sobre el costo para cubrir gastos y ganancia", "El material que sobra del pedido", "El descuento que se hace al proveedor", "El margen se suma al costo, no es un material ni un descuento."),
        ("abc", "¿Qué se suma para obtener el precio de venta?", "El costo total y el margen", "La merma y el sobrante", "El plano y el despiece", "El precio de venta es el costo más el margen."),
        ("=", "{F} ¿Cuánto cuestan los 5 tableros?", "5*34000", "Se multiplican los tableros por su precio unitario.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan los 30 metros lineales de listón?", "30*1500", "Se multiplican los metros por el precio de cada uno.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan los 12 herrajes?", "12*2500", "Se multiplican los herrajes por su precio unitario.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total del pedido (tableros 170.000, listón 45.000, herrajes 30.000 y mano de obra 90.000)?", "170000+45000+30000+90000", "Se suman los cuatro costos directos del pedido.", " pesos"),
        ("=", "{F} ¿Cuánto es el margen de 20 % sobre un costo total de $335.000?", "335000*20//100", "El 20 % del costo total es el margen.", " pesos"),
        ("=", "{F} ¿Cuál es el precio de venta (costo 335.000 más margen 67.000)?", "335000+67000", "Se suman el costo total y el margen.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta cada mueble si el precio de venta de $402.000 se divide entre los 6 muebles?", "402000//6", "Se divide el precio de venta por el número de muebles.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan 4 tableros B?", "4*40000", "Se multiplican los tableros por su precio unitario.", " pesos"),
        ("abc", "{F} Comparando el costo de los tableros: ¿qué alternativa es más barata?", "Los 4 tableros B", "Los 5 tableros de $34.000", "Cuestan lo mismo", "Los 4 tableros B cuestan $160.000 y los 5 tableros cuestan $170.000."),
        ("abc", "{F} Una persona dice: «el tablero B es más caro por unidad, así que es peor». ¿Qué respuesta es correcta?", "No: se compara el costo total y B necesita menos tableros", "Sí: el precio unitario siempre decide", "Sí, porque 40.000 es mayor", "Se compara el costo total, no solo el precio unitario."),
        ("abc", "{F} Un estudiante dice: «ya sé hacer un presupuesto, puedo fabricar el mueble solo». ¿Qué respuesta es correcta?", "No: fabricar exige instructor autorizado, norma vigente y EPP", "Sí: presupuestar habilita para fabricar", "Sí, si compra los materiales", "Un presupuesto es un cálculo en papel y no habilita para trabajar."),
    ],
    ctx=("abc", "En el taller de ejemplo, un trabajador se desmaya al respirar vapores de un producto cerca de la bodega de insumos. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar de inmediato sin protección a sacarlo", "Esperar a ver si se recupera sin avisar", "Entrar sin protección puede intoxicar también a quien ayuda; se avisa a quien corresponde y a emergencias."),
    sc=[
        ("¿Qué incluyen los costos directos de un presupuesto?", "Materiales y mano de obra", "Son los costos propios del pedido."),
        ("En Muebles y Terminaciones en Madera: ¿cómo se calcula el precio de venta?", "Costo total más margen", "El margen se suma al costo total."),
        ("¿Qué se compara al elegir entre dos alternativas de material?", "El costo total de cada una", "El precio unitario solo no considera la cantidad."),
    ],
    op=("Presupuesto de ejemplo «Taller Quillay» (ficticio): 4 estantes «E-6». Costos: 3 tableros a $30.000 cada uno, 20 m de listón a $1.200 el metro, 8 herrajes a $2.000 cada uno y mano de obra de $50.000. Margen de ejemplo: 25 % sobre el costo. Escribe (a) el costo total, (b) el margen, (c) el precio de venta y (d) el precio por estante.",
        "(a) 90.000+24.000+16.000+50.000 son 180.000. (b) 25 % de 180.000 son 45.000. (c) 180.000+45.000 son 225.000. (d) 225.000÷4 son 56.250.",
        ["calcula cada costo y el total", "calcula el margen", "calcula el precio de venta", "calcula el precio por estante"],
        ["hoja con los cuatro resultados"],
        ["aplicar el margen solo a materiales", "olvidar la mano de obra", "dividir por el número equivocado"],
        "Pregunta: «¿sobre qué costo se calcula el margen?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula el precio de venta de un pedido de ejemplo con costo de $60.000 y margen de 10 %.",
    extend="Explica por qué un presupuesto debe partir de una cubicación revisada.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 5 (taller de ejemplo, inventado). El taller ficticio «Carpintería Los Boldos» tiene una zona de máquinas con 3 puestos, cada uno con un operador autorizado, y 2 aprendices que observan desde una zona demarcada. "
     "Riesgos anotados: atrapamiento, corte, proyección de partículas, ruido, polvo de madera acumulado, incendio por acumulación de polvo y recortes, y ropa suelta o cabello largo que puede engancharse. "
     "Medidas anotadas: resguardos en cada máquina, etiqueta de «fuera de servicio» en una máquina con falla, zona demarcada para aprendices, aspiración de polvo, protección auditiva, lentes de seguridad, orden y aseo, y solo personal autorizado en las máquinas.")
build(
    O4, 1, F,
    use="Aprenderé qué riesgos tiene la fabricación de piezas de muebles en un taller y qué medidas generales de prevención existen, sin ningún procedimiento de uso de máquinas.",
    prior=["Sé qué es la jerarquía de controles.", "Sé qué es un EPP.", "Sé contar y sumar."],
    explain=[
        "Fabricar partes y piezas de muebles significa transformar la madera y los tableros en las piezas que pide el plano. Esa transformación se hace con máquinas y herramientas que pueden causar atrapamientos, cortes, proyección de partículas, ruido y polvo. El polvo de madera irrita la vista y las vías respiratorias y, si se acumula, aumenta el riesgo de incendio. El ruido, mantenido en el tiempo, puede dañar la audición. Cómo se operan las máquinas lo enseña un instructor autorizado y no se explica aquí.",
        "La prevención sigue la jerarquía de controles: eliminar el peligro, sustituirlo, usar resguardos y ventilación, organizar el trabajo y, al final, el EPP. Un resguardo es una protección física que cubre la parte peligrosa de una máquina. Una máquina con falla se deja fuera de servicio con una etiqueta y no se usa. La señalética informa con colores: el rojo prohíbe, el azul obliga, el amarillo advierte y el verde indica seguridad o salida de emergencia.",
        TAIL,
    ],
    vocab=[("atrapamiento", "riesgo de que una parte del cuerpo o la ropa quede enganchada en una máquina"), ("resguardo", "protección física que cubre la parte peligrosa de una máquina"), ("fuera de servicio", "estado de una máquina con falla que no se debe usar"), ("señalética", "señales de colores y símbolos que informan peligros y obligaciones"), ("proyección de partículas", "salida de fragmentos o polvo que puede alcanzar los ojos o la piel"), ("personal autorizado", "personas formalmente capacitadas y habilitadas para una tarea")],
    worked=[
        ("Reconocer la señal", "En un taller de ejemplo hay un letrero azul que muestra lentes de seguridad. ¿Qué significa por su color?", ["El azul indica obligación.", "El letrero obliga a usar los lentes."], "Es una obligación de usar lentes"),
        ("Contar personas", "Una zona de ejemplo tiene 4 operadores y 3 aprendices. ¿Cuántas personas hay en total?", ["Se suman operadores y aprendices.", "4 más 3 son 7."], "7 personas"),
    ],
    mistakes=[("Usar una máquina con falla porque «solo falta un poco» para terminar.", "Una máquina con falla puede causar un accidente grave.", "Se deja fuera de servicio con etiqueta y se avisa al responsable."),
              ("Creer que los lentes bastan para acercarse a una máquina sin autorización.", "El EPP es el último nivel y no reemplaza la autorización.", "Solo el personal autorizado y capacitado opera las máquinas.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es un resguardo de máquina?", "Una protección física que cubre la parte peligrosa", "Un documento con el plano del mueble", "Un tipo de tablero resistente", "El resguardo es una barrera física; el plano y el tablero son otras cosas."),
        ("abc", "¿Qué significa un letrero rojo en el taller?", "Una prohibición", "Una obligación", "La salida de emergencia", "El rojo prohíbe; el azul obliga y el verde indica seguridad."),
        ("abc", "¿Qué significa un letrero amarillo en el taller?", "Una advertencia de peligro", "Una prohibición", "Una obligación de usar EPP", "El amarillo advierte; el rojo prohíbe y el azul obliga."),
        ("=", "{F} ¿Cuántas personas hay en total en la zona (operadores y aprendices)?", "3+2", "Se suman los operadores autorizados y los aprendices.", " personas"),
        ("abc", "{F} ¿Dónde observan los aprendices según la ficha?", "Desde una zona demarcada", "Junto a las máquinas para aprender más rápido", "Dentro de la bodega de tableros", "La ficha indica una zona demarcada para ellos."),
        ("abc", "{F} ¿Qué se hace con la máquina que tiene una falla?", "Se deja fuera de servicio con una etiqueta", "Se usa con cuidado hasta terminar", "Se prueba por si funciona", "La falla se señala y la máquina no se usa."),
        ("=", "{F} Cada una de las 5 personas de la zona recibe protección auditiva y lentes de seguridad. ¿Cuántas piezas de EPP se entregan?", "5*2", "Se multiplican las personas por las dos piezas que recibe cada una.", " piezas"),
        ("abc", "{F} ¿Qué riesgo de la ficha se relaciona con las partículas que pueden alcanzar los ojos?", "La proyección de partículas", "El ruido", "La intoxicación por solventes", "La proyección de partículas puede alcanzar los ojos; por eso hay lentes."),
        ("abc", "{F} Una persona pone un polvo acumulado en un rincón detrás de la máquina para «ordenar rápido». ¿Qué corresponde?", "Retirarlo según el plan de aseo, porque el polvo acumulado aumenta el riesgo de incendio", "Dejarlo porque ahí nadie lo ve", "Taparlo con una tela", "La acumulación de polvo es un riesgo de incendio; el aseo lo reduce."),
        ("abc", "{F} Un estudiante dice: «si uso lentes y protección auditiva, puedo operar una máquina sin autorización». ¿Qué respuesta es correcta?", "No: el EPP es el último nivel y no reemplaza la autorización", "Sí: con EPP completo basta", "Sí, si hay otra persona mirando", "La autorización y la capacitación no se reemplazan con EPP."),
        ("ab", "{F} Un aprendiz dice: «puedo acercarme a la máquina con cabello largo suelto». ¿Qué respuesta es correcta?", "No: el cabello suelto puede engancharse y es un riesgo anotado en la ficha", "Sí: el cabello no es un riesgo", "La ficha anota la ropa suelta y el cabello largo como riesgo de enganche."),
        ("=", "{F} Si cada puesto tiene 2 resguardos (dato de ejemplo), ¿cuántos resguardos hay en los 3 puestos?", "3*2", "Se multiplican los puestos por los resguardos de cada uno.", " resguardos"),
        ("abc", "{F} ¿Qué medida de la ficha reduce el polvo en el aire?", "La aspiración de polvo", "La etiqueta de fuera de servicio", "La zona demarcada para aprendices", "La aspiración retira el polvo del aire; las otras medidas cubren otros riesgos."),
    ],
    ctx=("abc", "En un taller de ejemplo, una persona queda con la manga atrapada en una máquina en movimiento. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar sacarla tirando de la ropa sin avisar", "Apagar la máquina sin autorización y moverla", "Se pide ayuda a quien está autorizado y a emergencias, sin acercarse a la zona."),
    sc=[
        ("¿Qué indica el color azul en la señalética?", "Una obligación", "El azul señala algo que se debe hacer."),
        ("En Muebles y Terminaciones en Madera: ¿qué es el atrapamiento?", "Que una parte del cuerpo o la ropa quede enganchada en una máquina", "Es el riesgo de quedar enganchado en una máquina."),
        ("¿Quién puede operar las máquinas?", "Solo personal autorizado y capacitado", "La autorización no la reemplaza ningún EPP."),
    ],
    op=("Taller de ejemplo «Taller Peumo» (ficticio): 2 puestos de máquinas con operadores autorizados y 3 aprendices en zona demarcada. Riesgos: ruido, polvo acumulado y ropa suelta. Medidas: resguardos, aspiración de polvo, protección auditiva y lentes. Cada persona de la zona recibe protección auditiva y lentes. Escribe (a) cuántas personas hay, (b) cuántas piezas de EPP se entregan, (c) una medida que reduzca el polvo en el aire y (d) qué haces si ves a alguien con la ropa atrapada en una máquina.",
        "(a) 2+3 son 5 personas. (b) 5×2 son 10 piezas. (c) La aspiración de polvo. (d) No me acerco a la zona de riesgo, aviso a un adulto responsable y a emergencias.",
        ["suma las personas", "calcula el EPP entregado", "propone una medida contra el polvo", "avisa sin acercarse al riesgo"],
        ["hoja con las cuatro respuestas"],
        ["decir que el EPP reemplaza la autorización", "proponer sacar a la persona sin avisar", "olvidar a los aprendices en el conteo"],
        "Pregunta: «¿por qué la aspiración va antes que la mascarilla?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe la diferencia entre un letrero rojo, uno azul y uno amarillo con un ejemplo de cada uno en un taller.",
    extend="Explica por qué el ruido es un riesgo aunque no cause un accidente inmediato.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 6 (orden de trabajo de ejemplo, inventada). Orden de trabajo «OT-ej 12» del taller ficticio: fabricar 6 cómodas «C-2». Lista de corte de una cómoda (medidas de ejemplo): pieza A, 2 unidades, 80 cm por 45 cm; pieza B, 3 unidades, 70 cm por 40 cm; pieza C, 1 unidad, 100 cm por 50 cm. "
     "Hoja de ruta (solo nombres de etapas): 1 preparación de piezas, 2 ensamble, 3 terminación, 4 control de calidad. Tolerancia de ejemplo: 3 mm más o menos en cada medida. "
     "Roles: jefe de producción, que emite la orden; operador autorizado, que la ejecuta; controlador de calidad, que verifica; prevencionista, que revisa los riesgos.")
build(
    O4, 2, F,
    use="Aprenderé qué documentos organizan la fabricación de piezas: orden de trabajo, lista de corte, hoja de ruta y tolerancias, y qué rol cumple cada persona.",
    prior=["Sé leer un despiece.", "Sé multiplicar.", "Sé qué es la cubicación."],
    explain=[
        "La orden de trabajo es el documento con que el jefe de producción pide fabricar algo: qué, cuántos, para cuándo y con qué documentos. La lista de corte detalla las piezas que hay que obtener: nombre, cantidad y medidas. La hoja de ruta ordena las etapas por las que pasa el producto, por ejemplo preparación de piezas, ensamble, terminación y control de calidad; es una lista de nombres de etapas y no explica cómo se hace cada una.",
        "La tolerancia es la diferencia permitida entre la medida pedida y la medida real de una pieza. Si la medida real cae dentro de la tolerancia, la pieza se acepta; si queda fuera, se separa. Los roles se reparten así: el jefe de producción emite la orden, el operador autorizado la ejecuta, el controlador de calidad verifica y el prevencionista revisa los riesgos. Cada uno firma su parte, para que se sepa quién respondió por qué. Todas las cifras son de ejemplo.",
        TAIL,
    ],
    vocab=[("orden de trabajo", "documento que pide fabricar algo: qué, cuántos y para cuándo"), ("lista de corte", "lista de las piezas que hay que obtener, con cantidad y medidas"), ("hoja de ruta", "lista ordenada de las etapas por las que pasa el producto"), ("tolerancia", "diferencia permitida entre la medida pedida y la real"), ("controlador de calidad", "persona que verifica que las piezas cumplan lo pedido"), ("prevencionista", "persona que revisa los riesgos y las medidas de prevención")],
    worked=[
        ("Leer la lista de corte", "Una lista de corte de ejemplo dice: pieza X, 4 unidades; pieza Y, 2 unidades. ¿Cuántas piezas lleva un mueble?", ["Se suman las unidades de cada pieza.", "4 más 2 son 6."], "6 piezas"),
        ("Leer una tolerancia", "Una pieza de ejemplo se pide de 500 mm con tolerancia de más o menos 2 mm. ¿Entre qué medidas se acepta?", ["Se resta y se suma la tolerancia.", "498 y 502."], "Entre 498 mm y 502 mm"),
    ],
    mistakes=[("Confundir la hoja de ruta con las instrucciones de uso de las máquinas.", "La hoja de ruta solo ordena las etapas.", "Las instrucciones de uso las da un instructor autorizado y el fabricante."),
              ("Aceptar una pieza fuera de la tolerancia porque «se ve bien».", "La tolerancia se aplica con la medida real y no con la apariencia.", "Se separa la pieza y decide el controlador de calidad.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es la lista de corte?", "La lista de piezas que hay que obtener, con cantidad y medidas", "El orden de las etapas por las que pasa el producto", "El precio de cada tablero", "La lista de corte detalla piezas; la hoja de ruta ordena etapas."),
        ("abc", "En Muebles y Terminaciones en Madera: ¿Qué es una tolerancia?", "La diferencia permitida entre la medida pedida y la real", "El nombre de la última etapa de producción", "El número de muebles de una orden", "La tolerancia fija un margen de error aceptable."),
        ("=", "{F} ¿Cuántas piezas lleva una cómoda según la lista de corte?", "2+3+1", "Se suman las unidades de las piezas A, B y C.", " piezas"),
        ("=", "{F} ¿Cuántas piezas B se necesitan para las 6 cómodas?", "6*3", "Se multiplican las cómodas por las piezas B de cada una.", " piezas"),
        ("=", "{F} ¿Cuántas piezas en total se necesitan para las 6 cómodas?", "6*6", "Se multiplican las cómodas por las 6 piezas de cada una.", " piezas"),
        ("abc", "{F} ¿Qué rol emite la orden de trabajo?", "El jefe de producción", "El controlador de calidad", "El prevencionista", "La orden la emite quien programa, el jefe de producción."),
        ("abc", "{F} ¿Qué etapa de la hoja de ruta verifica que las piezas cumplan lo pedido?", "El control de calidad", "La preparación de piezas", "El ensamble", "El control de calidad es la etapa de verificación."),
        ("abc", "{F} ¿Qué rol revisa los riesgos de la orden?", "El prevencionista", "El operador", "El proveedor", "Revisar riesgos y medidas es función del prevencionista."),
        ("abc", "{F} Una pieza A se mide con 2 mm más de lo pedido en una de sus medidas. ¿Qué corresponde?", "Aceptarla, porque 2 mm está dentro de la tolerancia de 3 mm", "Rechazarla porque no es exacta", "Cortarla de nuevo sin registrar", "La diferencia es menor que la tolerancia, por lo que se acepta."),
        ("abc", "{F} Una pieza C se mide con 5 mm de diferencia respecto de lo pedido. ¿Qué corresponde?", "Separarla y avisar al controlador de calidad", "Aceptarla porque 5 está cerca de 3", "Corregirla por cuenta propia", "Cinco milímetros superan la tolerancia de 3 mm."),
        ("ab", "{F} Una persona dice: «la hoja de ruta me enseña cómo hacer cada etapa». ¿Qué respuesta es correcta?", "No: solo lista los nombres de las etapas", "Sí: incluye el procedimiento de cada etapa", "La ficha dice que son solo nombres de etapas."),
        ("abc", "{F} Una estudiante dice: «ya entiendo la orden de trabajo, puedo ejecutar la etapa de ensamble». ¿Qué respuesta es correcta?", "No: ejecutar exige instructor autorizado y norma vigente; leer no habilita", "Sí: leer la orden habilita para ejecutar", "Sí, con lentes de seguridad", "Entender un documento no autoriza a operar ni a armar."),
        ("=", "{F} Si el taller añade 2 cómodas a la orden, ¿cuántas piezas A se necesitan en total?", "(6+2)*2", "Se suman las cómodas a la orden y se multiplican por las 2 piezas A de cada una.", " piezas"),
    ],
    ctx=("abc", "En el taller de ejemplo, un operador se corta un dedo y la herida sangra mucho. Un compañero propone seguir trabajando para no atrasar la orden. ¿Qué respuesta es correcta?", "No: se avisa a un adulto responsable y a emergencias, sin acercarse a la máquina", "Sí: la orden es más importante", "Sí, si usan guantes", "Una lesión grave se informa a quien corresponde y a emergencias."),
    sc=[
        ("¿Qué contiene una lista de corte?", "Las piezas con su cantidad y medidas", "Detalla qué piezas se obtienen y en qué cantidad."),
        ("En Muebles y Terminaciones en Madera: ¿qué dice una hoja de ruta?", "El orden de las etapas del producto", "Ordena las etapas sin explicar cómo se hacen."),
        ("¿Quién verifica que las piezas cumplan lo pedido?", "El controlador de calidad", "La verificación es función del controlador de calidad."),
    ],
    op=("Orden de ejemplo «OT-ej 20» (ficticia): fabricar 5 mesas de arrimo. Lista de corte de una mesa: pieza P, 4 unidades, 60 cm por 5 cm; pieza Q, 2 unidades, 90 cm por 20 cm; pieza R, 1 unidad, 100 cm por 40 cm. Tolerancia de ejemplo: 2 mm. Escribe (a) cuántas piezas lleva una mesa, (b) cuántas piezas P se necesitan para las 5 mesas, (c) qué rol verifica las piezas y (d) qué haces con una pieza que supera la tolerancia.",
        "(a) 4+2+1 son 7 piezas. (b) 5×4 son 20 piezas P. (c) El controlador de calidad. (d) La separo y aviso al controlador de calidad.",
        ["suma las piezas de una mesa", "calcula las piezas P del pedido", "nombra al controlador", "separa la pieza fuera de tolerancia"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por el número de mesas", "aceptar una pieza fuera de tolerancia", "confundir roles"],
        "Pregunta: «¿qué diferencia hay entre la lista de corte y la hoja de ruta?». Si no responde, pídele que relea el vocabulario."),
    reinforce="Escribe quién emite, quién ejecuta y quién verifica una orden de trabajo, con una frase para cada rol.",
    extend="Explica por qué la tolerancia debe estar escrita en la orden y no depender del criterio de cada operador.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 7 (programación de producción de ejemplo, inventada). Pedido de 9 muebles «A-8». Tiempos de ejemplo por mueble, en minutos: preparación de piezas 20; ensamble 45; terminación 25; control de calidad 10. "
     "Jornada productiva de ejemplo: 300 minutos al día por línea. El taller ficticio tiene una sola línea. Fecha de entrega comprometida: 3 jornadas desde el inicio.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un caso de programación de producción: sumar tiempos por etapa, calcular las jornadas necesarias y reconocer la etapa más larga.",
    prior=["Sé multiplicar y dividir.", "Sé qué es una hoja de ruta.", "Sé convertir horas a minutos."],
    explain=[
        "Programar la producción es decidir cuándo y en qué orden se hace cada etapa para entregar a tiempo. Se parte de los tiempos por mueble en cada etapa, se suman para obtener el tiempo total por mueble y se multiplica por el número de muebles. Dividiendo ese total por los minutos productivos de una jornada se obtiene cuántas jornadas se necesitan; si la división deja resto, se redondea hacia arriba.",
        "La etapa que más tiempo toma limita el ritmo de toda la producción y se llama cuello de botella. Si el tiempo necesario supera el comprometido, hay que informar con anticipación y renegociar la entrega, no apurar el trabajo ni saltarse etapas de control o de seguridad. Presionar para llegar a tiempo es un riesgo: aumenta los errores y los accidentes. Todos los tiempos de esta clase son de ejemplo y no representan tiempos reales.",
        TAIL,
    ],
    vocab=[("programación de producción", "decisión de cuándo y en qué orden se hace cada etapa"), ("jornada productiva", "tiempo útil de trabajo de un día"), ("cuello de botella", "etapa más lenta, que limita el ritmo de toda la producción"), ("plazo de entrega", "fecha comprometida con el cliente"), ("renegociar", "volver a acordar un plazo cuando no se puede cumplir")],
    worked=[
        ("Tiempo por mueble", "Un mueble de ejemplo tiene dos etapas, de 15 y 35 minutos. ¿Cuántos minutos tarda en total?", ["Se suman los tiempos de las etapas.", "15 más 35 son 50."], "50 minutos"),
        ("Jornadas necesarias", "Un pedido de ejemplo necesita 800 minutos y una jornada productiva tiene 400. ¿Cuántas jornadas se necesitan?", ["Se divide el tiempo total por los minutos de una jornada.", "800 dividido en 400 son 2."], "2 jornadas"),
    ],
    mistakes=[("Acortar la etapa de control para cumplir el plazo.", "Sin control, los errores llegan al cliente.", "Se informa la demora y se renegocia el plazo."),
              ("Olvidar el redondeo hacia arriba al calcular las jornadas.", "Una jornada incompleta igual se trabaja.", "Si la división deja resto, se cuenta una jornada más.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es un cuello de botella en la producción?", "La etapa más lenta, que limita el ritmo de toda la producción", "La etapa más cara del pedido", "El lugar más estrecho de la bodega", "El cuello de botella es la etapa que más tiempo toma."),
        ("abc", "¿Qué hacer si el tiempo necesario supera el plazo comprometido?", "Informar con anticipación y renegociar el plazo", "Saltarse la etapa de control", "Trabajar sin pausas para llegar", "Presionar a tiempo aumenta errores y accidentes; se renegocia."),
        ("=", "{F} ¿Cuántos minutos tarda un mueble en total?", "20+45+25+10", "Se suman los tiempos de las cuatro etapas.", " min"),
        ("=", "{F} ¿Cuántos minutos necesita todo el pedido de 9 muebles (100 minutos cada uno)?", "9*100", "Se multiplican los muebles por el tiempo de cada uno.", " min"),
        ("=", "{F} ¿Cuántas jornadas productivas necesita el pedido (900 minutos en total y 300 por jornada)?", "900//300", "Se divide el tiempo total por los minutos de cada jornada.", " jornadas"),
        ("abc", "{F} ¿Cuál es la etapa más lenta según la ficha?", "El ensamble", "La preparación de piezas", "El control de calidad", "El ensamble tarda 45 minutos, más que las otras etapas."),
        ("=", "{F} ¿Cuántos minutos necesita la etapa de ensamble para los 9 muebles?", "9*45", "Se multiplican los muebles por los minutos de ensamble.", " min"),
        ("=", "{F} ¿Cuántas horas son los 900 minutos del pedido?", "900//60", "Se divide el total de minutos por 60 para pasar a horas.", " horas"),
        ("abc", "{F} ¿Se cumple la entrega comprometida de 3 jornadas?", "Sí, justo: el pedido necesita 3 jornadas", "No: se necesitan 4 jornadas", "No: se necesitan 2 jornadas", "El pedido necesita 900 minutos y 3 jornadas dan 900."),
        ("abc", "{F} Un cliente pide 2 muebles más en el mismo plazo. ¿Qué corresponde?", "Recalcular y renegociar el plazo con anticipación", "Aceptar sin calcular", "Quitar la etapa de control para ganar tiempo", "Con 11 muebles el tiempo supera el plazo; se recalcula y se informa."),
        ("ab", "{F} Un jefe dice: «acortamos el control de calidad para entregar a tiempo». ¿Qué respuesta es correcta?", "No: se informa la demora y se mantiene el control", "Sí: el control es opcional", "La ficha lista el control como etapa de 10 minutos."),
        ("abc", "{F} Una estudiante dice: «sé programar la producción, puedo hacerme cargo del ensamble». ¿Qué respuesta es correcta?", "No: ejecutar el ensamble exige instructor autorizado y norma vigente", "Sí: programar habilita para ejecutar", "Sí, si usa EPP", "Programar es un cálculo en papel y no habilita para trabajar en el taller."),
        ("=", "{F} Si el pedido fuera de 12 muebles de 100 minutos cada uno, ¿cuántas jornadas de 300 minutos necesitaría?", "(12*100)//300", "Se multiplican los muebles por su tiempo y se divide por los minutos de una jornada.", " jornadas"),
    ],
    ctx=("abc", "En el taller de ejemplo, por apurar el pedido, un operador cansado trabaja sin pausa y se distrae cerca de una máquina en movimiento. ¿Qué respuesta es correcta?", "Avisar al responsable para detener el trabajo: la presión y el cansancio aumentan el riesgo", "Seguir porque el plazo es lo más importante", "Pedirle que use dos EPP más", "El apuro y el cansancio provocan accidentes; el responsable debe resolverlo."),
    sc=[
        ("¿Cómo se obtiene el tiempo total por mueble?", "Sumando los tiempos de todas las etapas", "Cada etapa aporta su tiempo al total."),
        ("En Muebles y Terminaciones en Madera: ¿qué hacer si el plazo no se puede cumplir?", "Informar y renegociar con anticipación", "Apurar el trabajo aumenta los accidentes."),
        ("¿Por qué se redondea hacia arriba el número de jornadas?", "Porque una jornada incompleta igual se trabaja", "Si hay resto, hace falta una jornada más."),
    ],
    op=("Programación de ejemplo «Taller Ñire» (ficticio): pedido de 8 muebles; tiempos por mueble en minutos: preparación 30, ensamble 50, terminación 30 y control 10. Jornada productiva de 220 minutos; plazo comprometido de 3 jornadas. Escribe (a) el tiempo por mueble, (b) el tiempo del pedido, (c) cuántas jornadas se necesitan y (d) qué haces si no se alcanza el plazo.",
        "(a) 30+50+30+10 son 120 minutos. (b) 8×120 son 960 minutos. (c) 960÷220 da 4 con resto 80; se necesitan 5 jornadas. (d) Informo con anticipación y renegocio el plazo, sin saltarme el control ni apurar el trabajo.",
        ["suma los tiempos por mueble", "calcula el total del pedido", "calcula las jornadas con redondeo hacia arriba", "propone renegociar el plazo"],
        ["hoja con las cuatro respuestas"],
        ["no redondear hacia arriba", "saltarse el control", "olvidar multiplicar por los muebles"],
        "Pregunta: «¿por qué no conviene apurar el trabajo?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula cuántas jornadas de 200 minutos necesita un pedido de 750 minutos.",
    extend="Explica por qué presionar para cumplir un plazo puede ser un riesgo de accidentes.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 8 (registro de control de ejemplo, inventado). Pieza de ejemplo: medida pedida de 700 mm, tolerancia de ejemplo de 3 mm más o menos, es decir, se acepta de 697 mm a 703 mm. "
     "Registro de ocho piezas medidas, con una medida cada una por el controlador de calidad: pieza 1: 698; pieza 2: 701; pieza 3: 704; pieza 4: 697; pieza 5: 700; pieza 6: 696; pieza 7: 703; pieza 8: 699. Todas las medidas están en milímetros.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar una tolerancia a un registro de medidas: decidir qué piezas se aceptan, calcular la tasa de rechazo y registrar la decisión.",
    prior=["Sé qué es la tolerancia.", "Sé calcular un porcentaje sencillo.", "Sé leer una lista de medidas."],
    explain=[
        "Para aplicar una tolerancia se calculan los límites: el límite inferior es la medida pedida menos la tolerancia y el límite superior es la medida pedida más la tolerancia. Una pieza se acepta si su medida real está entre ambos límites, incluidos los extremos; si queda fuera, se separa y se registra. El controlador de calidad anota cada medida con el número de la pieza para que el registro permita rastrear cada decisión.",
        "La tasa de rechazo es el porcentaje de piezas separadas respecto del total medido: se multiplica el número de piezas rechazadas por 100 y se divide por el total. Una tasa alta indica un problema del proceso, que se informa al jefe de producción; no se corrige repitiendo la medición hasta que salga bien. Los instrumentos de medida los usa personal capacitado; aquí solo se leen los registros.",
        TAIL,
    ],
    vocab=[("límite inferior", "medida pedida menos la tolerancia"), ("límite superior", "medida pedida más la tolerancia"), ("tasa de rechazo", "porcentaje de piezas separadas respecto del total medido"), ("rastrear", "poder seguir la historia de una pieza a través de los registros"), ("registro de control", "documento donde se anotan las medidas y las decisiones")],
    worked=[
        ("Calcular los límites", "Una pieza de ejemplo se pide de 400 mm con tolerancia de 2 mm. ¿Entre qué valores se acepta?", ["Límite inferior: 400 menos 2.", "Límite superior: 400 más 2."], "Entre 398 mm y 402 mm"),
        ("Tasa de rechazo", "En un registro de ejemplo se miden 20 piezas y se rechazan 3. ¿Qué porcentaje se rechaza?", ["Se multiplica 3 por 100 y se divide por 20.", "300 dividido en 20 son 15."], "15 %"),
    ],
    mistakes=[("Medir de nuevo una pieza rechazada hasta que dé una medida aceptable.", "Se oculta el resultado real y se pierde la trazabilidad.", "Se registra la primera medición y se separa la pieza."),
              ("Incluir como aceptada una pieza que justo supera el límite por 1 mm.", "El límite es un valor fijo del criterio.", "Toda medida fuera del rango se separa.")],
    T=[
        ("abc", "En Muebles y Terminaciones en Madera: ¿qué es la tasa de rechazo?", "El porcentaje de piezas separadas respecto del total medido", "El precio de las piezas defectuosas", "El tiempo que tarda el control", "La tasa de rechazo compara piezas separadas con piezas medidas."),
        ("abc", "¿Cómo se calcula el límite superior de una tolerancia?", "Sumando la tolerancia a la medida pedida", "Restando la tolerancia a la medida pedida", "Multiplicando la medida por la tolerancia", "El límite superior es la medida pedida más la tolerancia."),
        ("=", "{F} ¿Cuántos mm vale el límite superior?", "700+3", "Se suma la tolerancia a la medida pedida.", " mm"),
        ("abc", "{F} ¿Qué pieza está por encima del límite superior?", "La pieza 3", "La pieza 7", "La pieza 5", "La pieza 3 mide 704 mm, más de 703 mm; la pieza 7 justo está en el límite."),
        ("abc", "{F} ¿Qué pieza está por debajo del límite inferior?", "La pieza 6", "La pieza 4", "La pieza 8", "La pieza 6 mide 696 mm, menos que 697 mm."),
        ("=", "{F} ¿Cuántas piezas se rechazan en total?", "1+1", "Se suma la pieza sobre el límite superior y la pieza bajo el inferior.", " piezas"),
        ("=", "{F} ¿Cuántas piezas se aceptan?", "8-2", "Se restan las piezas rechazadas del total medido.", " piezas"),
        ("=", "{F} ¿Cuál es la tasa de rechazo en porcentaje (2 rechazadas de 8 medidas)?", "2*100//8", "Se multiplican las rechazadas por 100 y se dividen por el total medido.", " %"),
        ("abc", "{F} La pieza 7 mide 703 mm. ¿Qué corresponde?", "Aceptarla, porque está en el límite superior", "Rechazarla por estar en el extremo", "Medirla de nuevo hasta que dé menos", "El criterio incluye los extremos del rango."),
        ("abc", "{F} Una persona propone medir de nuevo la pieza 3 hasta que dé 703 mm. ¿Qué respuesta es correcta?", "No: se registra la primera medición y se separa la pieza", "Sí: así se mejora la tasa de rechazo", "Sí, si nadie lo nota", "Repetir hasta que salga bien oculta el resultado real."),
        ("ab", "{F} Un compañero dice: «la pieza 5 mide exactamente 700 mm, así que la tolerancia no importa». ¿Qué respuesta es correcta?", "Sí: la pieza 5 coincide con la medida pedida y se acepta", "No: toda pieza debe estar a 3 mm de 700", "La pieza 5 mide exactamente lo pedido."),
        ("abc", "{F} Una estudiante dice: «ya sé interpretar el registro, puedo medir y cortar las piezas sin supervisión». ¿Qué respuesta es correcta?", "No: operar exige instructor autorizado y norma vigente", "Sí: interpretar un registro habilita para cortar", "Sí, si usa lentes", "Interpretar un registro es un trabajo de papel y no habilita para operar."),
        ("=", "{F} Si en otro lote de 25 piezas se rechazan 5, ¿qué porcentaje se rechaza?", "5*100//25", "Se multiplican las rechazadas por 100 y se dividen por el total.", " %"),
    ],
    ctx=("abc", "En el taller de ejemplo, un fragmento de una pieza sale proyectado y alcanza el ojo de un compañero. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Frotarle el ojo para sacar el fragmento", "Esperar a ver si se pasa", "Una lesión ocular se informa a quien corresponde y a emergencias; no se manipula."),
    sc=[
        ("¿Cómo se calcula el límite inferior de una tolerancia?", "Restando la tolerancia a la medida pedida", "El límite inferior es la medida menos la tolerancia."),
        ("En Muebles y Terminaciones en Madera: ¿qué se hace con una pieza fuera de los límites?", "Se separa y se registra", "El criterio se aplica con la medida real."),
        ("¿Por qué no se repite la medición hasta que salga bien?", "Porque se oculta el resultado real", "El registro debe reflejar la primera medición."),
    ],
    op=("Registro de ejemplo «Lote 5» (ficticio): medida pedida 500 mm, tolerancia de ejemplo de 2 mm (se acepta de 498 a 502). Seis piezas medidas: 497, 499, 502, 500, 503 y 498 mm. Escribe (a) los límites inferior y superior, (b) qué piezas se rechazan, (c) cuántas se aceptan y (d) qué haces con las rechazadas.",
        "(a) 498 mm y 502 mm. (b) Se rechazan 497 y 503. (c) Se aceptan 4. (d) Las separo, las registro y aviso al controlador de calidad.",
        ["calcula ambos límites", "identifica las dos piezas rechazadas", "cuenta las aceptadas", "propone separar y registrar"],
        ["hoja con las cuatro respuestas"],
        ["no incluir los extremos", "repetir la medición", "confundir límite inferior y superior"],
        "Pregunta: «¿por qué una pieza de 502 mm se acepta?». Si no responde, pídele que relea la explicación."),
    reinforce="Calcula los límites de una pieza de 350 mm con tolerancia de 4 mm.",
    extend="Explica por qué una tasa de rechazo alta se informa al jefe de producción y no se corrige solo.",
)
