"""Electrónica TP 3.º y 4.º medio: OAE-04 (instalar y montar sistemas electrónicos industriales: solo documentos, normas y cálculo), OAE-05 (mantenimiento preventivo y correctivo: planes, registros y costos) y OAE-06 (automatismos simples: sensores, reglas y parámetros). Todo en papel, con tensiones bajas y datos de ejemplo."""
from __future__ import annotations

from tp_eltr_common import AVISO, EMER, build

O4 = "TP-ELTR-3y4-OAE-04"
O5 = "TP-ELTR-3y4-OAE-05"
O6 = "TP-ELTR-3y4-OAE-06"

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). La planta ficticia «Envases del Sur» encarga el montaje de un sistema de conteo de cajas para una cinta transportadora: 1 sensor de paso, 1 controlador, 1 pantalla de conteo, 1 fuente de 24 V, cables y un gabinete. "
     "Documentos: diseño del proyecto (diagrama de bloques), lista de equipos, hoja de seguridad de la planta y plan de residuos. "
     "Riesgos anotados: la cinta tiene partes móviles, el gabinete está a 2 metros de altura y la fuente se alimenta desde la red eléctrica de la planta.")
build(
    O4, 1, F,
    use="Aprenderé qué significa instalar y montar un sistema electrónico industrial, qué normas y permisos exigen las plantas y qué riesgos hacen que esas tareas sean solo de personal autorizado.",
    prior=["Sé qué es un esquema y una lista de componentes.", "Sé que la SEC fiscaliza la seguridad eléctrica.", "Sé sumar y multiplicar."],
    explain=[
        "Montar un sistema electrónico industrial es dejar sus equipos en el lugar que indica el diseño del proyecto y listos para funcionar, de acuerdo con las características técnicas del proyecto. Se trabaja con tres normativas a la vez: la eléctrica, que en Chile vigila la Superintendencia de Electricidad y Combustibles (SEC); la ambiental, que obliga a manejar bien los residuos; y la de seguridad de la planta. La norma vigente dice cómo cumplirlas; este cuaderno no las reemplaza.",
        "Antes de empezar se leen el diseño, la lista de equipos y la hoja de seguridad, y se pide el permiso de trabajo: la autorización escrita de la planta para una tarea riesgosa, con sus condiciones. Los elementos de protección personal (EPP), como casco y lentes, reducen el riesgo, pero no lo eliminan. Los residuos electrónicos, como cables cortados o fuentes dañadas, no se botan a la basura común: los retira un gestor autorizado a través del responsable de la planta.",
        f"{EMER} Trabajar en altura, con partes móviles o con energía eléctrica es tarea de personal autorizado. {AVISO}",
    ],
    vocab=[("montaje", "dejar los equipos en su lugar y listos para funcionar según el diseño del proyecto"), ("diagrama de bloques", "dibujo que muestra las partes principales de un sistema y cómo se relacionan"), ("permiso de trabajo", "autorización escrita de la planta para una tarea riesgosa, con sus condiciones"), ("EPP", "elementos de protección personal, como casco o lentes"), ("residuo electrónico", "desecho de cables, fuentes o equipos que debe retirar un gestor autorizado"), ("normativa ambiental", "reglas sobre el cuidado del entorno y el manejo de residuos")],
    worked=[
        ("Elegir el documento", "Una técnica de ejemplo quiere ver cómo se relacionan las partes principales de un sistema, sin entrar al detalle de cada conexión. ¿Qué documento consulta?", ["Se necesita un dibujo de partes principales.", "Ese dibujo es el diagrama de bloques."], "El diagrama de bloques"),
        ("Contar equipos", "Una planta de ejemplo monta 3 sistemas, y cada uno lleva 2 fuentes y 1 controlador. ¿Cuántos equipos de esos dos tipos se necesitan?", ["Cada sistema lleva 2 más 1, es decir, 3 equipos.", "3 equipos por 3 sistemas son 9."], "9 equipos"),
    ],
    mistakes=[("Pensar que, por ser de 24 V, el sistema queda fuera de la norma y de los permisos.", "La fuente se alimenta desde la red y la planta exige sus permisos igual.", "Cumple la norma vigente y el permiso de trabajo en todo el sistema."),
              ("Botar los cables cortados a la basura común al terminar.", "Los residuos electrónicos exigen un retiro autorizado.", "Entrégalos al responsable de la planta para su retiro por un gestor autorizado.")],
    T=[
        ("abc", "En Electrónica: ¿qué es el montaje de un sistema industrial?", "Dejar los equipos en su lugar y listos para funcionar según el diseño del proyecto", "Comprar los componentes más baratos del mercado", "Fabricar cada componente desde cero", "El montaje consiste en ubicar y dejar operativos los equipos según el diseño."),
        ("abc", "En Electrónica: ¿qué es un elemento de protección personal (EPP)?", "Un equipamiento, como casco o lentes, que reduce el riesgo para la persona", "Un repuesto de reserva del equipo", "Un manual de uso para el cliente", "Los EPP protegen a la persona; no son repuestos ni documentos."),
        ("abc", "En Electrónica: ¿qué es un permiso de trabajo?", "La autorización escrita de la planta para una tarea riesgosa, con condiciones", "La factura por el trabajo realizado", "El plano de ubicación de los equipos", "El permiso de trabajo autoriza por escrito una tarea riesgosa y fija sus condiciones."),
        ("abc", "{F} ¿Qué documento de la ficha muestra cómo se relacionan el sensor, el controlador, la pantalla y la fuente?", "El diagrama de bloques del diseño", "El plan de residuos", "La hoja de seguridad de la planta", "El diagrama de bloques presenta las partes principales y sus relaciones."),
        ("abc", "{F} ¿Qué riesgos de la ficha exigen personal autorizado?", "La energía de la red que alimenta la fuente y el gabinete a 2 metros de altura", "El color de la cinta y el tamaño de la pantalla", "El número de cajas que cuenta el sistema", "La energía eléctrica y el trabajo en altura son riesgos que requieren personal autorizado."),
        ("abc", "{F} Al terminar quedan cables cortados y una fuente dañada. ¿Qué corresponde según el criterio ambiental general?", "Entregarlos al responsable de la planta para su retiro por un gestor autorizado", "Botarlos en el basurero común", "Llevarlos a casa para guardarlos", "Los residuos electrónicos no van a la basura común y los retira un gestor autorizado."),
        ("=", "{F} La planta tiene 4 cintas iguales y cada una lleva un sistema con los 4 equipos principales de la ficha (sensor, controlador, pantalla y fuente). ¿Cuántos equipos principales se necesitan en total?", "4*4", "Los equipos principales de un sistema se multiplican por las 4 cintas.", " equipos"),
        ("abc", "{F} Un compañero dice que, como el sistema es de 24 V, no requiere norma ni permisos. ¿Qué respondes?", "Que la fuente se alimenta desde la red y se cumplen la norma vigente y el permiso de trabajo igual", "Que tiene razón, porque toda tensión baja queda fuera de la norma", "Que solo se cumple la norma si el cliente lo pide", "La fuente conecta el sistema a la red; la norma y los permisos aplican a todo el montaje."),
        ("ab", "Una estudiante terminó este cuaderno y la planta le ofrece subir al gabinete a 2 metros de altura «porque es rápido». ¿Qué corresponde?", "Negarse: el trabajo en altura con energía exige personal autorizado, permiso de trabajo y norma vigente", "Aceptar con cuidado, porque ya conoce los documentos", "Conocer documentos no habilita para trabajar en altura ni cerca de energía; lo hace personal autorizado."),
        ("abc", "{F} El diseño muestra una pantalla de conteo, pero la lista de equipos trae dos. ¿Qué corresponde?", "Informar la diferencia al supervisor y pedir que se corrija antes de montar", "Montar las dos pantallas por si acaso", "Montar solo una y no avisar", "Si dos documentos se contradicen se informa y se corrige antes de ejecutar."),
        ("abc", "{F} ¿Cuál es el orden lógico previo al montaje, en cuanto a documentos?", "Leer el diseño, la lista de equipos y la hoja de seguridad, y obtener los permisos antes de empezar", "Empezar a trabajar y consultar los documentos si surge una duda", "Revisar la lista de equipos solo al terminar", "Los documentos y permisos se revisan antes de empezar, no después."),
        ("=", "{F} El montaje toma 3 técnicos durante 2 días, a $20.000 por técnico por día (de ejemplo). ¿Cuánto cuesta la mano de obra?", "3*2*20000", "Se multiplican los técnicos, los días y el valor diario.", " pesos"),
        ("abc", "En una planta de ejemplo se nota olor a quemado y humo en un gabinete eléctrico. ¿Qué corresponde de forma general?", "Alejarse, avisar al responsable de la planta y a emergencias, y cortar el suministro solo si se está autorizado", "Abrir el gabinete para ver qué ocurre", "Echarle agua para enfriarlo", "Ante humo o incendio eléctrico se aleja a las personas y se avisa; no se manipula el gabinete."),
    ],
    ctx=("abc", "El jefe de una planta de ejemplo dice: «sáltate el permiso de trabajo, es solo un ratito arriba del gabinete». Como estudiante, ¿qué respondes?", "Que el permiso es obligatorio y que esa tarea la hace personal autorizado", "Que lo harás rápido para que no se note", "Que si él lo pide, el permiso ya no es necesario", "El permiso de trabajo no se omite por la duración de la tarea; lo exigen la planta y la norma."),
    sc=[
        ("En Electrónica: ¿qué institución fiscaliza la seguridad eléctrica en Chile?", "La Superintendencia de Electricidad y Combustibles (SEC)", "La SEC fiscaliza la seguridad de las instalaciones eléctricas."),
        ("¿Qué se hace con los residuos electrónicos de un montaje?", "Se entregan al responsable de la planta para su retiro autorizado", "Los residuos electrónicos exigen un gestor autorizado."),
        ("¿Quién trabaja en altura o con energía eléctrica en una planta?", "Personal autorizado, con permiso de trabajo y norma vigente", "Este cuaderno no habilita para trabajar."),
    ],
    op=("Ficha de ejemplo: la planta «Textiles Norte» (ficticia) encarga el montaje de un sistema de alarma de temperatura: 1 sensor, 1 controlador, 1 sirena, 1 fuente de 24 V y 1 gabinete a 3 metros de altura. Documentos: diagrama de bloques, lista de equipos, hoja de seguridad y plan de residuos. Se montan 5 sistemas iguales. Escribe (a) qué documento muestra cómo se relacionan las partes, (b) cuántos equipos principales se necesitan (sin contar cables), (c) dos riesgos que exigen personal autorizado, (d) qué se hace con un cable cortado sobrante.",
        "(a) El diagrama de bloques. (b) 5 equipos por sistema por 5 sistemas son 25 equipos. (c) La energía de la red que alimenta la fuente y el gabinete a 3 metros de altura. (d) Entregarlo al responsable de la planta para su retiro por un gestor autorizado.",
        ["nombra bien el documento", "calcula bien el total de equipos", "reconoce dos riesgos de personal autorizado", "describe el destino correcto del residuo"],
        ["hoja con las cuatro respuestas"],
        ["decir que ya puede subir al gabinete", "contar mal los equipos", "botar el cable a la basura común"],
        "Pregunta: «¿qué haría la planta si falta el permiso de trabajo?». Si no responde, pídele que relea la parte del permiso."),
    reinforce="Escribe una lista de cinco riesgos de un montaje industrial y, para cada uno, quién debe hacer la tarea.",
    extend="Explica con un ejemplo por qué un permiso de trabajo protege a la persona y a la planta.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (documentos de proyecto de ejemplo, inventados). Sistema de conteo de cajas: bloques SENSOR → CONTROLADOR → PANTALLA; la FUENTE de 24 V alimenta a los tres. "
     "Lista de cables: C1, sensor–controlador, 6 m; C2, controlador–pantalla, 4 m; C3, fuente–controlador, 3 m; C4, fuente–sensor, 5 m; C5, fuente–pantalla, 12 m. "
     "Cada cable lleva etiqueta con su nombre en ambos extremos. El plano de ubicación está a escala 1:50: 1 cm del plano son 50 cm reales; entre la fuente y el controlador hay 6 cm en el plano.")
build(
    O4, 2, F,
    use="Aprenderé a leer los documentos de un proyecto de montaje: diagrama de bloques, lista de cables, rotulado y plano de ubicación, y a cuidar que todos coincidan.",
    prior=["Sé qué es un diagrama de bloques.", "Sé usar una escala.", "Sé calcular porcentajes sencillos."],
    explain=[
        "El diagrama de bloques dibuja las partes principales de un sistema como cajas unidas por flechas y dice cómo se relacionan, sin mostrar cada conexión. La lista de cables nombra cada cable, entre qué dos equipos va y su largo. El rotulado es la etiqueta con el nombre de cada cable, puesta en ambos extremos, para no confundirlos. El plano de ubicación muestra dónde va cada equipo en el lugar, a escala.",
        "En un proyecto, todos los documentos deben coincidir. Si se agrega un equipo, se actualizan el diagrama, la lista de equipos, la lista de cables, el rotulado y el plano. Al comprar cable se pide algo más que el total: la reserva, un porcentaje extra que cubre curvas, recortes y errores de medida del plano. Al terminar, el plano se corrige con lo realmente montado: es el plano «como quedó construido».",
        f"Los cables y las fuentes se manejan solo con personal autorizado y con la energía controlada por la planta. {AVISO}",
    ],
    vocab=[("lista de cables", "documento con el nombre, los extremos y el largo de cada cable"), ("rotulado", "etiqueta con el nombre del cable puesta en ambos extremos"), ("plano de ubicación", "dibujo a escala que muestra dónde va cada equipo en el lugar"), ("reserva de cable", "cantidad extra de cable que se pide por curvas, recortes y errores de medida"), ("plano como quedó construido", "plano corregido con lo realmente montado")],
    worked=[
        ("Largo total", "Una lista de ejemplo tiene tres cables de 2 m, 5 m y 7 m. ¿Cuántos metros suman?", ["Se suman los largos de todos los cables.", "2 más 5 más 7 son 14."], "14 m"),
        ("Reserva", "Una planta de ejemplo necesita 40 m de cable y pide una reserva del 10 %. ¿Cuántos metros compra?", ["El 10 % de 40 es 4.", "40 más 4 son 44."], "44 m"),
    ],
    mistakes=[("Cortar los cables a la medida exacta del plano, sin reserva.", "El recorrido real suele ser algo mayor que el dibujado.", "Pide una reserva de cable y deja constancia en la lista."),
              ("Agregar un equipo en la obra sin actualizar los documentos.", "Los documentos dejan de coincidir con lo montado.", "Informa el cambio para que se actualicen todos los documentos.")],
    T=[
        ("abc", "En Electrónica: ¿qué es un diagrama de bloques?", "Un dibujo que muestra las partes principales de un sistema y cómo se relacionan", "Un esquema con todos los componentes y sus valores", "Una lista con los precios de los equipos", "El diagrama de bloques muestra partes principales, no el detalle de cada componente."),
        ("abc", "En Electrónica: ¿para qué se rotula un cable en ambos extremos?", "Para identificarlo y no confundirlo con otro", "Para que conduzca más corriente", "Para que el cable dure más años", "El rotulado ayuda a identificar el cable desde cualquiera de sus puntas."),
        ("abc", "En Electrónica: ¿qué es un plano de ubicación?", "Un dibujo a escala que muestra dónde va cada equipo en el lugar", "Una lista de los cables y sus largos", "Una tabla con los consumos de los equipos", "El plano de ubicación indica la posición de cada equipo."),
        ("=", "{F} ¿Cuántos metros de cable suma la lista de cables?", "6+4+3+5+12", "Se suman los largos de los cinco cables de la lista.", " m"),
        ("abc", "{F} ¿Qué cable une la fuente con la pantalla?", "El cable C5", "El cable C3", "El cable C2", "La lista dice que C5 va entre la fuente y la pantalla."),
        ("=", "Un cable de 2 m reales se dibuja en un plano a escala 1:50. ¿Cuántos centímetros mide en el plano?", "200//50", "Se pasan 2 m a 200 cm y se divide por la escala 50.", " cm"),
        ("=", "{F} El proyecto exige una reserva del 10 % sobre el total de cable. ¿Cuántos metros se deben pedir?", "30+30*10//100", "Al total de la lista se le suma el 10 % de reserva.", " m"),
        ("abc", "{F} ¿Qué bloque recibe la señal del sensor según el diagrama?", "El controlador", "La pantalla", "La fuente", "La flecha va del sensor al controlador; la pantalla recibe del controlador."),
        ("abc", "{F} Un técnico de ejemplo ve un cable sin etiqueta en un extremo. ¿Qué corresponde?", "Identificarlo con la lista y el diagrama y, si queda duda, informar al supervisor", "Adivinar cuál es por su largo", "Dejarlo así porque el otro extremo sí tiene etiqueta", "Un cable sin identificar puede conectarse mal; se resuelve con los documentos o se consulta."),
        ("abc", "{F} El plano marca 6 cm entre la fuente y el controlador, y la lista dice que C3 mide 3 m. ¿Coinciden?", "Sí, porque 6 cm por 50 son 300 cm, es decir 3 m", "No, porque el plano da 6 m", "No, porque el plano da 12 m", "Con escala 1:50, 6 cm del plano equivalen a 300 cm reales, igual que 3 m."),
        ("abc", "Un compañero propone cortar cada cable justo a la medida de la lista, sin reserva. ¿Qué problema puede tener?", "Si el recorrido real es mayor que el dibujado, el cable no alcanzará", "El cable conduciría menos corriente", "El cable se rotularía mal", "El recorrido real puede ser mayor que el del plano; por eso se pide reserva."),
        ("=", "{F} El cable cuesta $800 por metro (de ejemplo). ¿Cuánto cuesta comprar los 33 metros que incluyen la reserva?", "33*800", "El precio por metro se multiplica por los metros comprados.", " pesos"),
        ("abc", "{F} Se agrega un segundo sensor al sistema. ¿Qué documentos deben actualizarse?", "El diagrama, la lista de equipos, la lista de cables, el rotulado y el plano", "Solo la lista de equipos", "Ninguno, porque basta con montarlo", "Si un cambio no llega a todos los documentos, estos dejan de coincidir entre sí."),
    ],
    ctx=("abc", "Al terminar un montaje de ejemplo, el técnico nota que un cable pasó por un recorrido distinto del dibujado. ¿Qué corresponde con los documentos?", "Informar el cambio para que el plano se corrija como quedó construido", "Dejar el plano como estaba, para no complicarlo", "Cambiar el rotulado del cable para que coincida con el plano", "El plano debe reflejar lo montado; esa corrección la autoriza quien administra el proyecto."),
    sc=[
        ("En Electrónica: ¿qué documento da el largo de cada cable?", "La lista de cables", "La lista de cables nombra los extremos y el largo."),
        ("¿Para qué se pide una reserva de cable?", "Para cubrir curvas, recortes y errores de medida", "El recorrido real puede ser mayor que el del plano."),
        ("¿Qué es el plano «como quedó construido»?", "El plano corregido con lo realmente montado", "Refleja los cambios hechos durante la obra."),
    ],
    op=("Ficha de ejemplo: sistema de aviso de nivel de un estanque. Lista de cables: A1, sensor–controlador, 8 m; A2, controlador–alarma, 5 m; A3, fuente–controlador, 4 m; A4, fuente–sensor, 3 m. Reserva exigida: 10 % del total. Escala del plano: 1:20. El cable A3 mide 20 cm en el plano. Escribe (a) cuántos metros suma la lista, (b) cuántos metros se piden con la reserva, (c) si A3 coincide con la lista según el plano, con el cálculo, (d) qué documentos actualizarías si se agrega un segundo sensor.",
        "(a) 8 + 5 + 4 + 3 = 20 m. (b) 20 + 2 = 22 m. (c) 20 cm por 20 son 400 cm, es decir 4 m: coincide con A3 (4 m). (d) Diagrama de bloques, lista de equipos, lista de cables, rotulado y plano de ubicación.",
        ["suma bien los largos", "calcula bien la reserva", "aplica bien la escala", "nombra los documentos a actualizar"],
        ["hoja con los cálculos y las respuestas"],
        ["olvidar la reserva", "no multiplicar por la escala", "actualizar solo un documento"],
        "Pregunta: «¿qué pasa si el plano y la lista no coinciden?». Si no responde, pídele que relea la regla de coincidencia de documentos."),
    reinforce="Inventa una lista de cuatro cables con sus largos, calcula el total y el pedido con una reserva del 10 %.",
    extend="Explica con un ejemplo por qué el plano «como quedó construido» ayuda en una futura mantención.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (cálculo de ejemplo, inventado). Una fuente de 24 V entrega como máximo 5 A. Equipos conectados a ella, con sus consumos de ejemplo: sensor, 300 mA; controlador, 1200 mA; pantalla, 800 mA; alarma sonora, 1500 mA. "
     "1 A son 1000 mA; potencia = tensión × corriente. Regla del proyecto: la corriente total no debe superar el 80 % de lo que entrega la fuente.")
build(
    O4, 3, F,
    use="Aprenderé a sumar consumos, a respetar el margen de una fuente y a calcular costos e inventarios de un montaje, siempre en papel y con valores de ejemplo.",
    prior=["Sé la ley de Ohm y la potencia.", "Sé pasar de amperios a miliamperios.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Una fuente entrega una tensión y una corriente máxima. La corriente total que se le pide es la suma de las corrientes de todos los equipos conectados a ella. Si la suma supera el máximo, la fuente se calienta y puede fallar. Por eso el proyecto fija un margen: por ejemplo, no pasar del 80 % de la corriente máxima. Así la fuente no trabaja al límite.",
        "Todas las corrientes deben estar en la misma unidad antes de sumar: 1 A son 1000 mA. La potencia de un equipo es tensión por corriente, de modo que 24 V y 1 A son 24 W. Además de los cálculos eléctricos se calculan costos e inventarios: cuántos metros de cable se usaron, cuántos quedan en bodega y cuánto cuesta cada cosa.",
        f"Si un equipo nuevo hace pasar el límite, se informa al proyectista: puede usarse otra fuente o una de mayor capacidad aprobada. Nunca se ignora la regla ni se retira una protección. {AVISO}",
    ],
    vocab=[("corriente total", "suma de las corrientes de todos los equipos conectados a una fuente"), ("margen", "parte de la capacidad que se deja libre para no trabajar al límite"), ("capacidad de la fuente", "corriente máxima que puede entregar"), ("consumo", "corriente o potencia que un equipo usa"), ("inventario", "recuento de lo que hay en bodega")],
    worked=[
        ("Corriente total", "Dos equipos de ejemplo conectados a una fuente consumen 400 mA y 600 mA. ¿Cuánta corriente total piden?", ["Se suman los consumos.", "400 más 600 son 1000 mA, es decir 1 A."], "1000 mA, es decir 1 A"),
        ("Margen del 80 %", "Una fuente de ejemplo entrega como máximo 2 A. ¿Cuántos mA es el 80 % de su corriente máxima?", ["2 A son 2000 mA.", "El 80 % de 2000 es 1600."], "1600 mA"),
    ],
    mistakes=[("Sumar 300 mA y 1,2 A directamente como si fueran la misma unidad.", "Hay que pasar todo a la misma unidad antes de sumar.", "Convierte los amperios a miliamperios y luego suma."),
              ("Retirar el fusible porque la suma de consumos se acerca al límite.", "Se pierde la protección de la fuente.", "Informa al proyectista para que decida otra fuente o un cambio autorizado.")],
    T=[
        ("abc", "En Electrónica: ¿qué es la corriente total que se le pide a una fuente?", "La suma de las corrientes de todos los equipos conectados a ella", "La corriente del equipo que más consume", "La tensión de la fuente multiplicada por dos", "La fuente debe entregar la suma de lo que consume cada equipo."),
        ("abc", "En Electrónica: ¿por qué el proyecto deja un margen en la fuente?", "Para que la fuente no trabaje al límite y no se caliente ni falle", "Para gastar menos energía en la planta", "Para que los equipos se enciendan más rápido", "El margen evita que la fuente opere en su máximo, donde se calienta y falla más."),
        ("abc", "¿Cuál es la relación correcta entre amperios y miliamperios?", "1 A son 1000 mA", "1 A son 100 mA", "1 mA son 1000 A", "Un amperio equivale a mil miliamperios."),
        ("=", "{F} ¿Cuántos miliamperios suman los cuatro equipos de la ficha?", "300+1200+800+1500", "Se suman los consumos de los cuatro equipos.", " mA"),
        ("=", "{F} ¿Cuántos miliamperios es el 80 % de la corriente máxima de la fuente?", "5*1000*80//100", "Se pasan los 5 A a mA y se toma el 80 %.", " mA"),
        ("abc", "{F} ¿Cumple el sistema la regla del 80 %?", "Sí, porque 3800 mA es menor que 4000 mA", "No, porque la suma supera los 5 A de la fuente", "No, porque 3800 mA es mayor que 3000 mA", "El tope del 80 % es 4000 mA, y la suma de 3800 mA queda por debajo."),
        ("=", "{F} ¿Cuántos vatios consume la alarma sonora a 24 V?", "24*1500//1000", "La potencia es tensión por corriente, con la corriente pasada a amperios.", " W"),
        ("=", "{F} Se agrega un quinto equipo de 600 mA. ¿Cuántos mA suma ahora el sistema?", "300+1200+800+1500+600", "Se suma el nuevo consumo a los cuatro anteriores.", " mA"),
        ("abc", "{F} Con el quinto equipo de 600 mA, ¿cumple la regla del 80 %?", "No, porque 4400 mA supera el máximo de 4000 mA", "Sí, porque 4400 mA es menor que 5000 mA", "Sí, porque el quinto equipo es pequeño", "La regla pone el tope en 4000 mA, no en la corriente máxima total."),
        ("abc", "{F} Con el quinto equipo, ¿qué alternativa respeta la regla?", "Alimentar el equipo nuevo con una segunda fuente aprobada por el proyectista", "Ignorar la regla, porque la fuente aún no llega a 5 A", "Quitar el fusible para que no se abra", "Una segunda fuente aprobada reparte la carga; ignorar la regla o quitar la protección aumenta el riesgo."),
        ("=", "Una bodega de ejemplo compra 100 m de cable. Tras montar 3 sistemas iguales quedan 40 m. ¿Cuántos metros usó cada sistema?", "(100-40)//3", "Se resta lo que queda a lo comprado y se divide por los 3 sistemas.", " m"),
        ("abc", "La hoja del fabricante dice que un equipo consume 1500 mA. Un técnico anota 1,5 A y otro anota 15 A. ¿Quién anota bien?", "El que anota 1,5 A", "El que anota 15 A", "Ninguno, porque 1500 mA son 150 A", "1500 mA equivalen a 1,5 A, porque 1 A son 1000 mA."),
        ("=", "Un sistema de ejemplo pide 3800 mA. Una fuente de ejemplo de 20 A se usa con la regla del 80 %. ¿Cuántos sistemas completos puede alimentar como máximo?", "20*1000*80//100//3800", "Se calcula el tope en mA y se divide por el consumo de cada sistema, sin contar sistemas incompletos.", " sistemas"),
    ],
    ctx=("abc", "El proyectista de ejemplo recibe esta consulta de un técnico: «la fuente da 5 A y los equipos suman 4,6 A: ¿lo dejamos así?». La regla del proyecto es no pasar del 80 %. ¿Qué respuesta corresponde?", "No: el tope es 4 A; hay que cambiar de fuente o repartir la carga", "Sí: 4,6 A es menor que 5 A", "Sí: la regla del 80 % solo vale si la fuente es vieja", "El 80 % de 5 A es 4 A, y 4,6 A lo supera; la regla manda sobre el máximo absoluto."),
    sc=[
        ("En Electrónica: ¿cómo se calcula la corriente total de una fuente?", "Sumando las corrientes de los equipos conectados", "Todos los consumos se suman en una misma unidad."),
        ("¿Cuántos mA son 2 A?", "2000 mA", "Cada amperio son 1000 miliamperios, así que 2 A son 2000."),
        ("¿Qué se hace si el consumo supera la regla del proyecto?", "Informar al proyectista; no retirar protecciones", "El proyectista decide otra fuente o una solución autorizada."),
    ],
    op=("Ficha de ejemplo: fuente de 12 V que entrega como máximo 4 A, con regla del 75 % de la corriente máxima. Equipos de ejemplo: luz de aviso, 900 mA; sensor, 200 mA; relé, 700 mA; timbre, 1000 mA. Escribe (a) cuántos mA suman, (b) cuántos mA es el tope del 75 %, (c) si cumple la regla y por qué, (d) cuántos vatios consume el timbre.",
        "(a) 900 + 200 + 700 + 1000 = 2800 mA. (b) 4000 por 75 ÷ 100 = 3000 mA. (c) Cumple: 2800 mA es menor que 3000 mA. (d) 12 V por 1 A son 12 W.",
        ["suma bien los consumos", "calcula bien el tope", "concluye con la comparación", "calcula la potencia"],
        ["hoja con los cálculos"],
        ["sumar sin convertir unidades", "usar 4000 mA como tope", "no justificar la conclusión"],
        "Pregunta: «¿qué harías si se agrega un equipo de 400 mA?». Si no responde, pídele que relea qué se hace si el consumo supera la regla."),
    reinforce="Calcula en papel la corriente total y el 80 % de una fuente de 3 A con tres equipos de ejemplo de tu elección.",
    extend="Explica con un ejemplo por qué un margen de la fuente ahorra problemas después del montaje.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (pauta de recepción de ejemplo, inventada, completada por un supervisor). Comparación entre el proyecto y la obra, ocho ítems: 1 sensor ubicado donde indica el plano, Sí; 2 cables rotulados en ambos extremos, No (el cable C4 no tiene etiqueta en un extremo); "
     "3 fuente con la capacidad del proyecto, Sí; 4 gabinete cerrado y rotulado, Sí; 5 residuos retirados, No (queda una caja con cables cortados); 6 plano actualizado como quedó construido, Sí; 7 hoja de seguridad firmada, Sí; 8 instrucciones de uso entregadas, Sí.")
build(
    O4, 4, F,
    use="Aprenderé a usar una pauta de recepción para comparar un montaje de ejemplo con el proyecto, a decidir con criterio técnico y a dejar el registro.",
    prior=["Sé qué documentos tiene un proyecto.", "Sé calcular porcentajes sencillos.", "Sé que un registro deja constancia de lo hecho."],
    explain=[
        "Al terminar un montaje, el supervisor recibe la obra con una pauta de recepción: una lista de verificación que compara lo montado con el proyecto. Cada ítem se marca como cumplido o no cumplido. Lo que no se cumple se anota como observación: algo que debe corregirse, con un responsable y un plazo. El porcentaje de cumplimiento se calcula dividiendo los ítems cumplidos por el total, por cien.",
        "Un porcentaje alto no reemplaza el criterio. Un ítem de seguridad, como la hoja de seguridad firmada o la protección de una fuente, debe cumplirse siempre; si no se cumple, no se entrega. Las observaciones menores pueden quedar con un plazo acordado. La recepción termina con la firma de las partes y con los documentos corregidos.",
        f"Los residuos, la rotulación y los documentos cuentan en la recepción tanto como lo eléctrico. {AVISO}",
    ],
    vocab=[("pauta de recepción", "lista de verificación que compara la obra con el proyecto"), ("observación", "anotación de algo que no cumple y debe corregirse"), ("porcentaje de cumplimiento", "ítems cumplidos divididos por el total, por cien"), ("ítem de seguridad", "punto de la pauta que protege a las personas y que debe cumplirse siempre"), ("plazo", "fecha acordada para corregir una observación")],
    worked=[
        ("Contar cumplidos", "Una pauta de ejemplo tiene 5 ítems y se cumplen 4. ¿Cuántos no se cumplen y qué se hace con ellos?", ["5 menos 4 es 1.", "El que no se cumple se anota como observación con responsable y plazo."], "Uno; se anota como observación"),
        ("Porcentaje", "Una pauta de ejemplo tiene 10 ítems y se cumplen 9. ¿Cuál es el porcentaje de cumplimiento?", ["9 dividido en 10 es 0,9.", "Por cien son 90 %."], "90 %"),
    ],
    mistakes=[("Entregar la obra porque el porcentaje de cumplimiento es alto, aunque falle un ítem de seguridad.", "Los ítems de seguridad se cumplen siempre.", "No se entrega hasta cumplirlo."),
              ("Marcar «Sí» en un ítem que no se cumple para cerrar la recepción rápido.", "Un registro falso oculta el problema.", "Marca «No» y anota la observación con responsable y plazo.")],
    T=[
        ("abc", "En Electrónica: ¿qué es una pauta de recepción?", "Una lista de verificación que compara lo montado con el proyecto", "Una lista de precios de los equipos", "El permiso de trabajo de la planta", "La pauta de recepción verifica la obra frente al proyecto ítem por ítem."),
        ("abc", "En Electrónica: ¿qué es un plano «como quedó construido»?", "El plano actualizado con lo realmente montado", "El primer borrador del proyecto", "El plano de un proyecto de otra empresa", "Este plano refleja la obra real, con los cambios hechos."),
        ("abc", "En Electrónica: ¿qué es una observación en una recepción?", "La anotación de algo que no cumple y debe corregirse", "Una felicitación al equipo de montaje", "La firma del cliente al final", "La observación señala lo pendiente, con responsable y plazo."),
        ("=", "{F} ¿Cuántos ítems de la pauta están cumplidos?", "8-2", "Se resta al total de ítems los dos marcados «No».", " ítems"),
        ("abc", "{F} ¿Qué ítems no se cumplen?", "El 2 (rotulado) y el 5 (residuos)", "El 3 (fuente) y el 6 (plano)", "El 1 (sensor) y el 8 (instrucciones)", "La pauta marca «No» solo en los ítems 2 y 5."),
        ("=", "{F} ¿Cuál es el porcentaje de cumplimiento de la pauta?", "6*100//8", "Se dividen los ítems cumplidos por el total y se multiplica por cien.", " %"),
        ("abc", "{F} ¿Qué corresponde con el ítem 2, el cable C4 sin etiqueta?", "Anotarlo como observación y pedir al responsable que lo rotule antes de la entrega final", "Marcar «Sí», porque el otro extremo tiene etiqueta", "Borrar el nombre C4 de la lista de cables", "El ítem no se cumple: se anota como observación para corregirlo."),
        ("abc", "{F} ¿Qué corresponde con el ítem 5, los cables cortados que quedan?", "Entregarlos al responsable de la planta para su retiro por un gestor autorizado", "Dejarlos en el gabinete", "Botarlos en la basura común", "Los residuos electrónicos exigen un retiro autorizado."),
        ("abc", "{F} ¿Puede darse el montaje por recibido sin observaciones?", "No, porque hay dos ítems que no se cumplen", "Sí, porque 75 % es más de la mitad", "Sí, porque lo importante es lo eléctrico", "Con ítems en «No» deben anotarse observaciones."),
        ("abc", "{F} El cliente dice: «firmo igual y corrijan después». ¿Qué corresponde?", "Firmar dejando anotadas las observaciones, con responsable y plazo acordado", "Borrar las observaciones para que pueda firmar", "Rechazar la firma para siempre", "La recepción puede cerrarse con observaciones anotadas y plazo; no se ocultan."),
        ("=", "Corregir cada observación toma 2 horas a $9.000 la hora (de ejemplo). Hay 2 observaciones. ¿Cuánto cuesta corregirlas?", "2*2*9000", "Se multiplican las observaciones, las horas de cada una y el valor de la hora.", " pesos"),
        ("abc", "{F} Si el ítem 7, la hoja de seguridad firmada, fuera «No» aunque el resto estuviera bien, ¿qué corresponde?", "No entregar hasta cumplirlo, porque es un ítem de seguridad", "Entregar, porque el porcentaje sigue siendo alto", "Entregar y firmar la hoja después de un año", "Un ítem de seguridad no se negocia por un porcentaje alto."),
        ("=", "Otra pauta de ejemplo tiene 20 ítems y se cumplen 17. ¿Cuál es su porcentaje de cumplimiento?", "17*100//20", "Se dividen los ítems cumplidos por el total y se multiplica por cien.", " %"),
    ],
    ctx=("abc", "El jefe de una planta de ejemplo pide entregar hoy sin retirar los residuos electrónicos: «mañana pasa el camión». ¿Qué corresponde?", "Anotarlo como observación con plazo y responsable, sin marcarlo como cumplido", "Marcar «Sí» en residuos para poder entregar", "Botar los residuos en la basura común", "Lo pendiente se anota; no se marca como cumplido ni se resuelve de forma inadecuada."),
    sc=[
        ("En Electrónica: ¿cómo se calcula el porcentaje de cumplimiento?", "Ítems cumplidos entre el total, por cien", "Es la proporción de ítems cumplidos expresada en porcentaje."),
        ("¿Qué se hace con un ítem que no se cumple?", "Se anota como observación con responsable y plazo", "La observación deja constancia de lo pendiente."),
        ("¿Se entrega con un ítem de seguridad sin cumplir?", "No, hasta que se cumpla", "Los ítems de seguridad se cumplen siempre."),
    ],
    op=("Ficha de ejemplo: pauta de recepción de cinco ítems de una instalación de aviso de 12 V. 1 equipos en su lugar, Sí; 2 gabinete rotulado, No; 3 hoja de seguridad firmada, Sí; 4 plano actualizado, No; 5 residuos retirados, Sí. Escribe (a) cuántos ítems se cumplen, (b) el porcentaje de cumplimiento, (c) qué observaciones anotarías, (d) si puede entregarse y por qué.",
        "(a) 3 ítems. (b) 3 por 100 ÷ 5 son 60 %. (c) Rotular el gabinete y actualizar el plano, con responsable y plazo. (d) Puede entregarse con observaciones y plazo acordado, porque ninguno de los ítems pendientes es de seguridad; la hoja de seguridad está firmada.",
        ["cuenta bien los cumplidos", "calcula bien el porcentaje", "redacta las observaciones", "decide con la razón de seguridad"],
        ["hoja con las cuatro respuestas"],
        ["marcar «Sí» para cerrar", "no anotar responsable ni plazo", "decidir solo por el porcentaje"],
        "Pregunta: «¿cambiaría tu decisión si la hoja de seguridad no estuviera firmada?». Si no responde, pídele que relea la regla de los ítems de seguridad."),
    reinforce="Inventa una pauta de seis ítems con dos «No» y escribe las observaciones con responsable y plazo.",
    extend="Explica con un ejemplo por qué es mejor anotar una observación que cerrar la recepción sin decir lo pendiente.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El liceo ficticio «Liceo Austral» tiene 6 paneles informativos electrónicos de 12 V. Documentos: plan de mantenimiento (inspección visual cada mes y revisión de especificaciones cada 6 meses, hechas por personal autorizado), "
     "manual del fabricante y bitácora de fallas. En marzo se informó que 2 paneles se apagan solos. Riesgos anotados: los paneles están a 3 metros de altura y se alimentan desde un transformador conectado a la red eléctrica.")
build(
    O5, 1, F,
    use="Aprenderé qué es el mantenimiento preventivo y el correctivo, qué documentos lo guían y qué riesgos hacen que muchas tareas sean solo de personal autorizado.",
    prior=["Sé qué es una falla y un diagnóstico.", "Sé que la SEC fiscaliza la seguridad eléctrica.", "Sé multiplicar y dividir."],
    explain=[
        "Mantener un equipo es cuidarlo para que siga funcionando. El mantenimiento preventivo son tareas planificadas que se hacen antes de que el equipo falle, como las inspecciones periódicas. El mantenimiento correctivo es la reparación de una falla que ya ocurrió. El plan de mantenimiento es el documento que dice qué tarea se hace, cada cuánto tiempo y quién la hace. La bitácora es el registro cronológico de las revisiones, las fallas y los trabajos.",
        "Cada tarea sigue la normativa de seguridad, las especificaciones del fabricante y el plan. Desenergizar un equipo, es decir, dejarlo sin energía y señalado para que nadie lo active por error, lo hace solo personal autorizado según el procedimiento de la empresa y la norma vigente (SEC); este cuaderno no enseña ese procedimiento. Los instrumentos y materiales los elige y usa personal capacitado.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("mantenimiento preventivo", "tareas planificadas para evitar fallas antes de que ocurran"), ("mantenimiento correctivo", "reparación de una falla que ya ocurrió"), ("plan de mantenimiento", "documento que dice qué tarea, cada cuánto y quién la hace"), ("bitácora", "registro cronológico de revisiones, fallas y trabajos"), ("desenergizar", "dejar un equipo sin energía y señalado, tarea de personal autorizado")],
    worked=[
        ("Clasificar el trabajo", "Un plan de ejemplo pide revisar un detector cada tres meses, aunque funcione bien. ¿Qué tipo de mantenimiento es?", ["La revisión se hace antes de que falle.", "Es una tarea planificada."], "Preventivo"),
        ("Contar tareas", "El plan de ejemplo pide una inspección cada 2 meses. ¿Cuántas inspecciones hay en un año?", ["Un año tiene 12 meses.", "12 dividido en 2 son 6."], "6 inspecciones"),
    ],
    mistakes=[("Pensar que el mantenimiento solo se hace cuando un equipo falla.", "Eso es el correctivo; el preventivo se hace antes para evitar fallas.", "Distingue las tareas planificadas de las reparaciones."),
              ("Abrir un equipo conectado a la red para «ver qué pasa» porque se apaga solo.", "Es una tarea de riesgo reservada a personal autorizado.", "Anota el síntoma en la bitácora y deriva la revisión.")],
    T=[
        ("abc", "En Electrónica: ¿qué es el mantenimiento preventivo?", "Tareas planificadas para evitar fallas antes de que ocurran", "La reparación después de que el equipo falla", "El reemplazo del equipo todos los años", "El preventivo se anticipa a la falla; la reparación posterior es mantenimiento correctivo."),
        ("abc", "En Electrónica: ¿qué es el mantenimiento correctivo?", "La reparación de una falla que ya ocurrió", "Las inspecciones programadas del plan", "La limpieza que se hace antes de usar el equipo", "El correctivo actúa sobre una falla ya presente."),
        ("abc", "En Electrónica: ¿qué es una bitácora de mantenimiento?", "Un registro cronológico de revisiones, fallas y trabajos", "Una lista de repuestos con sus precios", "El manual de uso del fabricante", "La bitácora deja constancia por fecha de lo ocurrido."),
        ("abc", "{F} ¿Qué tipo de trabajo es la inspección visual mensual de los paneles?", "Preventivo", "Correctivo", "Ninguno, porque no repara nada", "Se hace con el equipo funcionando y de forma planificada, para evitar fallas."),
        ("abc", "{F} ¿Qué tipo de mantenimiento corresponde a los 2 paneles que se apagan solos?", "Correctivo, comenzando por registrar el síntoma y diagnosticar", "Preventivo, porque está en el plan", "Ninguno, porque el plan de mantenimiento no incluye reparaciones", "Hay una falla ya ocurrida, por lo que corresponde mantenimiento correctivo."),
        ("abc", "{F} ¿Quién hace la revisión de especificaciones de los paneles?", "Personal autorizado, según el plan", "Cualquier estudiante que pase por el patio", "El cliente, con las instrucciones del manual", "El plan asigna esa revisión a personal autorizado por el riesgo eléctrico."),
        ("=", "{F} Los 6 paneles se inspeccionan visualmente cada mes. ¿Cuántas inspecciones visuales hay en un año en total?", "6*12", "Los paneles se multiplican por los meses del año.", " inspecciones"),
        ("=", "{F} La revisión de especificaciones es cada 6 meses y hay 6 paneles. ¿Cuántas revisiones de especificaciones hay en un año?", "6*(12//6)", "En un año hay 2 revisiones por panel y eso se multiplica por 6 paneles.", " revisiones"),
        ("ab", "Una estudiante propone abrir el transformador de un panel para ver por qué se apaga solo. ¿Qué corresponde?", "No hacerlo: está conectado a la red y lo revisa personal autorizado con norma vigente", "Hacerlo con cuidado, porque ya sabe qué es un transformador", "Un transformador conectado a la red implica riesgo eléctrico; saber qué es no habilita para abrirlo."),
        ("abc", "{F} Se informan dos paneles que se apagan solos, el 3 y el 5. ¿Por qué conviene anotar ambos en la bitácora?", "Para detectar si hay un patrón común, como una misma fuente, que ayude al diagnóstico", "Para que la bitácora tenga más páginas", "Para poder cobrar más por la reparación", "Dos casos similares en la bitácora permiten buscar una causa común."),
        ("=", "Un mantenimiento preventivo anual cuesta $15.000 por panel y una reparación correctiva cuesta $60.000 (valores de ejemplo). ¿Cuántos pesos más cuesta una reparación correctiva que un preventivo?", "60000-15000", "Se resta el costo del preventivo al del correctivo.", " pesos"),
        ("abc", "{F} Un jefe propone dejar el mantenimiento preventivo para ahorrar y reparar solo cuando algo falle. ¿Qué riesgo tiene esa decisión?", "Más fallas imprevistas, más costo y más riesgo para las personas", "Ninguno, porque los equipos duran más sin revisiones", "Que el plan de mantenimiento se llene de hojas", "Sin preventivo se pierden las detecciones tempranas y las fallas llegan sin aviso."),
        ("abc", "Alguien nota que el transformador de un panel está muy caliente y huele a quemado. ¿Qué corresponde de forma general?", "Alejarse, avisar a un adulto responsable y a emergencias, y cortar el suministro solo si se está autorizado", "Tocarlo para comprobar cuánta temperatura tiene", "Taparlo con un paño para que no se vea el humo", "Un equipo caliente con olor a quemado es riesgo de incendio; no se toca ni se tapa."),
    ],
    ctx=("abc", "Un directivo de ejemplo dice: «los paneles están a solo 3 metros; que suba el conserje con una escalera y los reinicie». ¿Qué corresponde?", "Pedir que lo haga personal autorizado, con permiso y norma vigente, por la altura y la energía", "Aceptar, porque 3 metros no es una altura peligrosa", "Pedir a un estudiante que suba, porque pesa poco", "La altura y la energía de red hacen que la tarea sea de personal autorizado."),
    sc=[
        ("En Electrónica: ¿qué documento dice qué tarea de mantenimiento se hace y cada cuánto?", "El plan de mantenimiento", "El plan fija tarea, frecuencia y responsable."),
        ("¿Qué es el mantenimiento correctivo?", "La reparación de una falla que ya ocurrió", "El correctivo ocurre después de la falla."),
        ("¿Quién desenergiza un equipo conectado a la red?", "Personal autorizado, con procedimiento y norma vigente", "Este cuaderno no enseña ese procedimiento."),
    ],
    op=("Ficha de ejemplo: el colegio «Costa Verde» (ficticio) tiene 4 relojes electrónicos de pared de 6 V con pilas. Plan: inspección visual cada 2 meses; cambio de pilas cada 12 meses por personal autorizado. Hoy se informa que un reloj se detuvo. Escribe (a) qué tipo de mantenimiento es la inspección cada 2 meses, (b) cuántas inspecciones visuales hay en un año para los 4 relojes, (c) qué tipo de trabajo corresponde al reloj detenido y qué anotarías en la bitácora, (d) una tarea que no harías tú.",
        "(a) Preventivo. (b) 6 inspecciones por reloj por 4 relojes son 24. (c) Correctivo; en la bitácora: fecha, reloj detenido y síntoma. (d) Cambiar las pilas o abrir el reloj, que lo hace personal autorizado.",
        ["clasifica bien el mantenimiento", "calcula bien las inspecciones", "describe lo que se anota", "reconoce una tarea que no le corresponde"],
        ["hoja con las cuatro respuestas"],
        ["confundir preventivo con correctivo", "calcular mal las inspecciones", "decir que él mismo abriría el reloj"],
        "Pregunta: «¿qué otro dato anotarías para ayudar al diagnóstico?». Si no responde, pídele que relea qué se registra en la bitácora."),
    reinforce="Escribe cinco tareas de mantenimiento de un equipo cotidiano y clasifica cada una como preventiva o correctiva.",
    extend="Explica con un ejemplo por qué la bitácora ayuda a un técnico nuevo que llega a un liceo.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (plan y hoja de vida de ejemplo, inventados). Plan de mantenimiento de un sistema de luces automáticas, con inspecciones hechas por personal autorizado: E1, detector de presencia, cada 3 meses; E2, controlador, cada 6 meses; E3, fuente de 12 V, cada 12 meses. "
     "Hoja de vida de E3: instalada en el año 1; inspección del año 2 sin observaciones; inspección del año 3 con una observación (ventilación obstruida por polvo, corregida). Repuestos en bodega: 10 fusibles y 2 detectores de presencia.")
build(
    O5, 2, F,
    use="Aprenderé a leer un plan de mantenimiento, una hoja de vida y el stock de repuestos, y a calcular cuántas tareas hay en un año.",
    prior=["Sé qué es el mantenimiento preventivo.", "Sé qué es una bitácora.", "Sé dividir 12 meses en períodos."],
    explain=[
        "El plan de mantenimiento lista los equipos, la tarea de cada uno y su frecuencia. Para saber cuántas tareas hay en un año se divide 12 meses por la frecuencia: una tarea mensual son 12 por año. La hoja de vida de un equipo es su historia escrita: cuándo se instaló, cuándo se inspeccionó, qué observaciones hubo y qué se reparó. Sirve para ver si un equipo se está deteriorando.",
        "Un repuesto es una pieza de reserva para reemplazar otra dañada. Se lleva un inventario para saber cuántos hay y cuándo pedir más. Si el plan cambia, por ejemplo una frecuencia, el plan se actualiza por escrito y se avisa a quienes lo ejecutan. Registrar una inspección sin hallazgos también es útil: muestra que el equipo estuvo bien en esa fecha.",
        f"Si una inspección se atrasa, se registra el atraso tal como ocurrió; no se anota una fecha inventada. {AVISO}",
    ],
    vocab=[("frecuencia", "cada cuánto tiempo se repite una tarea"), ("hoja de vida", "historia escrita de un equipo: instalación, inspecciones, fallas y reparaciones"), ("repuesto", "pieza de reserva para reemplazar una dañada"), ("inventario de repuestos", "recuento de los repuestos que hay en bodega"), ("hallazgo", "algo que se encuentra en una inspección")],
    worked=[
        ("Tareas por año", "Un equipo de ejemplo se inspecciona cada 4 meses. ¿Cuántas inspecciones hay en un año?", ["Un año tiene 12 meses.", "12 dividido en 4 son 3."], "3 inspecciones"),
        ("Repuestos que quedan", "La bodega de ejemplo tiene 15 fusibles y se usan 6. ¿Cuántos quedan?", ["Se resta lo usado a lo que había.", "15 menos 6 son 9."], "9 fusibles"),
    ],
    mistakes=[("Anotar una fecha de inspección que no ocurrió para que el plan «cumpla».", "Un registro falso oculta el atraso y quita confianza a la hoja de vida.", "Registra el atraso tal como ocurrió y reprograma."),
              ("No registrar una inspección porque no hubo hallazgos.", "La hoja de vida pierde información sobre el estado del equipo.", "Registra siempre cada inspección, con o sin hallazgos.")],
    T=[
        ("abc", "En Electrónica: ¿qué es un plan de mantenimiento?", "El documento que dice qué tarea se hace, cada cuánto y quién la hace", "La lista de precios de los repuestos", "El manual de uso del cliente", "El plan fija tareas, frecuencias y responsables."),
        ("abc", "En Electrónica: ¿qué es la hoja de vida de un equipo?", "Su historia escrita: instalación, inspecciones, fallas y reparaciones", "El contrato con el fabricante", "El esquema eléctrico del equipo", "La hoja de vida reúne lo que ha ocurrido con el equipo a lo largo del tiempo."),
        ("abc", "En Electrónica: ¿qué es un repuesto?", "Una pieza de reserva para reemplazar una dañada", "Un documento con las fallas del año", "Una herramienta para abrir equipos", "El repuesto es una pieza guardada para reemplazos."),
        ("=", "{F} ¿Cuántas inspecciones del detector E1 hay en un año?", "12//3", "Se dividen los 12 meses del año por la frecuencia de 3 meses.", " inspecciones"),
        ("=", "{F} ¿Cuántas inspecciones en total, entre E1, E2 y E3, hay en un año?", "12//3+12//6+12//12", "Se suman las inspecciones anuales de cada equipo.", " inspecciones"),
        ("abc", "{F} ¿Qué se encontró en la inspección del año 3 de la fuente E3?", "Ventilación obstruida por polvo, que fue corregida", "Un fusible quemado que se reemplazó", "Ninguna observación", "La hoja de vida registra la observación del año 3 y su corrección."),
        ("abc", "{F} Un técnico dice que la fuente E3 «nunca tuvo observaciones». ¿Qué dato de la ficha lo contradice?", "La observación del año 3 sobre la ventilación obstruida", "La inspección del año 2 sin observaciones", "La cantidad de fusibles en bodega", "El año 3 tuvo una observación, así que la afirmación es falsa."),
        ("=", "{F} Se usan 3 fusibles de la bodega en una reparación. ¿Cuántos quedan?", "10-3", "Se resta lo usado a lo que había en la bodega.", " fusibles"),
        ("abc", "{F} Un plan de ejemplo exige tener siempre al menos 3 detectores de repuesto. ¿Qué corresponde con los 2 de la ficha?", "Pedir al menos 1 más para completar el mínimo", "Nada, porque 2 es casi 3", "Usar un detector del sistema que está funcionando", "Faltan repuestos para cumplir el mínimo del plan; se pide la diferencia."),
        ("abc", "{F} El calendario cambia: el detector E1 pasará a revisarse cada 2 meses. ¿Qué debe hacerse con los documentos?", "Actualizar el plan por escrito y avisar a quienes lo ejecutan", "Avisar solo de palabra y no cambiar el plan", "No cambiar nada hasta que falle", "Un cambio de frecuencia debe quedar en el plan para que todos trabajen con lo mismo."),
        ("=", "Un detector de ejemplo pasa a revisarse cada 2 meses. ¿Cuántas inspecciones por año tiene?", "12//2", "Se dividen los 12 meses por la nueva frecuencia de 2 meses.", " inspecciones"),
        ("abc", "{F} ¿Por qué conviene registrar en la hoja de vida cada inspección, aunque no encuentre problemas?", "Porque muestra la historia del equipo y permite ver cuándo cambian las cosas", "Para llenar más hojas", "Para cobrar una inspección más cara", "Una serie de registros permite comparar el estado del equipo en el tiempo."),
        ("abc", "Un técnico de ejemplo nota que la última inspección del detector E1 fue hace 5 meses y el plan exige una cada 3. ¿Qué corresponde?", "Registrar el atraso tal como ocurrió e informar para reprogramar la inspección", "Anotar que se hizo hace 3 meses", "No decir nada, porque el detector funciona", "Un registro verdadero muestra el atraso; falsearlo quita confianza a la hoja de vida."),
    ],
    ctx=("abc", "El supervisor de ejemplo pregunta si el sistema de luces cumplió el plan este año, y a un técnico se le olvidó una inspección de E2. ¿Qué responde un técnico íntegro?", "Que se omitió una inspección de E2, y propone reprogramarla", "Que se cumplió todo, porque el sistema funciona", "Que no recuerda y prefiere no responder", "La honestidad del registro es la base del plan; ocultar la omisión impide corregirla."),
    sc=[
        ("En Electrónica: ¿cómo se calculan las inspecciones por año de una tarea cada 6 meses?", "Dividiendo 12 meses por 6", "El año tiene 12 meses y la frecuencia es cada 6."),
        ("¿Qué registra la hoja de vida de un equipo?", "Su instalación, inspecciones, fallas y reparaciones", "Es la historia escrita del equipo."),
        ("¿Qué se hace si una inspección se atrasó?", "Se registra el atraso real y se reprograma", "Un registro verdadero no inventa fechas ni oculta atrasos."),
    ],
    op=("Ficha de ejemplo: plan de un sistema de riego automático. R1, sensor de humedad, inspección cada 4 meses; R2, controlador, cada 6 meses; R3, válvula, cada 12 meses. Repuestos: 5 sensores de humedad en bodega y el plan exige tener al menos 4. Hoja de vida de R3: año 1 instalada; año 2 sin observaciones. Escribe (a) cuántas inspecciones por año hay en total, (b) cuántos sensores sobran sobre el mínimo del plan, (c) cómo registrarías que la inspección de R3 del año 3 se atrasó 2 meses.",
        "(a) 3 + 2 + 1 = 6 inspecciones. (b) 5 menos 4 es 1 sensor. (c) En la hoja de vida: año 3, inspección atrasada 2 meses respecto del plan, motivo y nueva fecha programada.",
        ["calcula bien las inspecciones", "compara el stock con el mínimo", "registra el atraso con honestidad"],
        ["hoja con las tres respuestas"],
        ["dividir mal los meses", "olvidar el mínimo del plan", "inventar que se cumplió a tiempo"],
        "Pregunta: «¿qué dato nuevo agregarías a la hoja de vida?». Si no responde, pídele que relea qué debe registrar la hoja."),
    reinforce="Inventa un plan con tres equipos y sus frecuencias, y calcula cuántas inspecciones hay en un año.",
    extend="Explica con un ejemplo por qué un registro honesto del atraso es mejor que uno que «cumple».",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (registro del semestre de ejemplo, inventado) de un panel informativo. Mano de obra: $10.000 por hora. Órdenes de trabajo: enero, preventiva, 2 h, repuestos $0; febrero, correctiva, 5 h, repuestos $30.000; "
     "marzo, preventiva, 2 h, repuestos $5.000; abril, preventiva, 2 h, repuestos $0; mayo, correctiva, 3 h, repuestos $20.000; junio, preventiva, 2 h, repuestos $0.")
build(
    O5, 3, F,
    use="Aprenderé a leer un registro de órdenes de trabajo, a calcular horas, costos y disponibilidad y a comparar el costo del mantenimiento preventivo y el correctivo.",
    prior=["Sé qué es el mantenimiento preventivo y el correctivo.", "Sé multiplicar y sumar.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Una orden de trabajo de mantenimiento es el documento que pide y registra una tarea: equipo, tipo de mantenimiento, fecha, horas trabajadas y repuestos usados. Con muchas órdenes se arma una planilla que permite calcular costos. El costo de una tarea es la mano de obra, que es el valor del tiempo de las personas, más los repuestos.",
        "La disponibilidad de un equipo es el porcentaje del tiempo en que está en condiciones de funcionar. Se calcula restando las horas de detención a las horas totales, dividiendo por las horas totales y multiplicando por cien. Comparar el costo del preventivo y el del correctivo ayuda a decidir cuánto invertir en revisiones. El registro debe reflejar siempre lo realmente hecho: no se inflan ni se reducen las horas.",
        f"Los valores de este cuaderno son solo de ejemplo. {AVISO}",
    ],
    vocab=[("orden de trabajo", "documento que pide y registra una tarea de mantenimiento"), ("mano de obra", "valor del tiempo de trabajo de las personas"), ("costo de repuestos", "valor de las piezas usadas en la tarea"), ("disponibilidad", "porcentaje del tiempo en que un equipo está en condiciones de funcionar"), ("horas de detención", "horas en que el equipo no pudo funcionar")],
    worked=[
        ("Costo de una tarea", "Una orden de ejemplo tiene 3 horas de trabajo a $8.000 la hora y repuestos por $12.000. ¿Cuánto cuesta la tarea?", ["La mano de obra es 3 por 8.000, es decir 24.000.", "Se suma el costo de los repuestos: 24.000 más 12.000."], "$36.000"),
        ("Disponibilidad", "Un equipo de ejemplo tiene 100 horas en el período y estuvo detenido 10. ¿Qué disponibilidad tiene?", ["Funcionó 100 menos 10, es decir 90 horas.", "90 de 100 es 90 %."], "90 %"),
    ],
    mistakes=[("Anotar más horas de las trabajadas para que la orden «se vea mejor».", "El costo y la historia del equipo quedan falsos.", "Registra las horas realmente trabajadas."),
              ("Calcular el costo de una tarea sin incluir la mano de obra.", "La mano de obra es parte del costo.", "Suma la mano de obra y los repuestos.")],
    T=[
        ("abc", "En Electrónica: ¿qué es una orden de trabajo de mantenimiento?", "Un documento que pide y registra una tarea: equipo, tipo, horas y repuestos", "Una lista de precios de los repuestos", "El manual de uso del equipo", "La orden de trabajo documenta la tarea; la lista de precios y el manual cumplen otras funciones."),
        ("abc", "En Electrónica: ¿qué es la disponibilidad de un equipo?", "El porcentaje del tiempo en que está en condiciones de funcionar", "La cantidad de repuestos que hay en bodega", "El número de técnicos que lo atienden", "La disponibilidad mide cuánto del tiempo el equipo puede funcionar."),
        ("abc", "En Electrónica: ¿qué es la mano de obra dentro de un costo?", "El valor del tiempo de trabajo de las personas", "El valor de las piezas usadas", "El valor del arriendo de la bodega", "La mano de obra mide el tiempo de las personas; las piezas son repuestos."),
        ("=", "{F} ¿Cuántas horas de trabajo suman las seis órdenes?", "2+5+2+2+3+2", "Se suman las horas de las seis órdenes.", " horas"),
        ("=", "{F} ¿Cuántas horas de trabajo correctivo hubo en el semestre?", "5+3", "Se suman las horas de las dos órdenes correctivas.", " horas"),
        ("=", "{F} ¿Cuánto se gastó en repuestos en el semestre?", "30000+5000+20000", "Se suman los repuestos de las órdenes que los usaron.", " pesos"),
        ("=", "{F} ¿Cuánto costó la mano de obra de todo el semestre?", "16*10000", "Las 16 horas del semestre se multiplican por el valor de la hora.", " pesos"),
        ("=", "{F} ¿Cuál fue el costo total del semestre, entre mano de obra y repuestos?", "16*10000+55000", "Se suma la mano de obra de las 16 horas y los repuestos del semestre.", " pesos"),
        ("abc", "{F} ¿Qué tipo de trabajo costó más en el semestre?", "El correctivo, con $130.000", "El preventivo, con $215.000", "Costaron lo mismo", "Las dos correctivas suman 8 horas y $50.000 en repuestos, es decir, $130.000, más que las preventivas."),
        ("=", "{F} ¿Cuántos pesos más costaron las dos órdenes correctivas que las cuatro preventivas?", "(8*10000+50000)-(8*10000+5000)", "Se compara el costo correctivo con el preventivo, y las horas son iguales en ambos.", " pesos"),
        ("=", "Un equipo de ejemplo tiene 720 horas en un mes de 30 días y estuvo detenido 36 horas por fallas. ¿Cuál es su disponibilidad?", "(720-36)*100//720", "Se restan las horas de detención, se divide por las horas totales y se multiplica por cien.", " %"),
        ("abc", "{F} Un jefe dice que el mantenimiento correctivo «sale más barato» porque hubo menos órdenes correctivas que preventivas. ¿Qué dato lo contradice?", "Las 2 correctivas costaron $130.000 y las 4 preventivas, $85.000", "Las 4 preventivas costaron más que las 2 correctivas", "Los dos costaron lo mismo", "El número de órdenes no define el costo; las horas y los repuestos del correctivo fueron mayores."),
        ("abc", "Un técnico de ejemplo trabajó 3 horas en una orden, pero quiere anotar 5 porque «así se ve más trabajo». ¿Qué corresponde?", "Anotar las 3 horas realmente trabajadas", "Anotar las 5 horas para que cuadre el costo", "No anotar nada para evitar problemas", "El registro debe reflejar lo realmente hecho; inflar horas falsea el costo y la historia."),
    ],
    ctx=("abc", "El supervisor de ejemplo pide un informe del semestre del panel: ¿qué debe incluir como mínimo?", "Horas, repuestos y costo por tipo de trabajo, y las fechas de las órdenes", "Solo el costo total, sin el detalle", "Solo las órdenes preventivas, para que se vea mejor", "Un informe útil separa los tipos de trabajo y muestra el detalle, no solo un total."),
    sc=[
        ("En Electrónica: ¿de qué se compone el costo de una tarea?", "De la mano de obra y los repuestos", "Ambos conceptos, el trabajo y las piezas, forman el costo."),
        ("En electrónica: ¿cómo se calcula la disponibilidad?", "Restando las horas de detención, dividiendo por las totales y multiplicando por cien", "Es el porcentaje de tiempo funcional."),
        ("¿Se pueden aumentar horas en una orden para que cuadre?", "No, el registro debe reflejar lo realmente hecho", "Las horas falsas dañan el costo y la historia del equipo."),
    ],
    op=("Ficha de ejemplo: registro de 4 meses de un timbre automático. Mano de obra: $8.000 por hora. Órdenes: marzo, preventiva, 1 h, repuestos $0; abril, correctiva, 4 h, repuestos $24.000; mayo, preventiva, 1 h, repuestos $2.000; junio, preventiva, 1 h, repuestos $0. Escribe (a) las horas totales, (b) el costo total, (c) cuánto costó el trabajo correctivo y cuánto el preventivo, (d) qué conclusión obtienes.",
        "(a) 1 + 4 + 1 + 1 = 7 horas. (b) 7 por 8.000 son 56.000, más 26.000 de repuestos: 82.000 pesos. (c) Correctivo: 4 por 8.000 más 24.000 son 56.000. Preventivo: 3 por 8.000 más 2.000 son 26.000. (d) El correctivo costó más del doble que el preventivo, aunque fue una sola orden.",
        ["calcula bien las horas", "calcula bien el costo total", "separa preventivo y correctivo", "saca una conclusión con datos"],
        ["hoja con los cálculos y la conclusión"],
        ["olvidar la mano de obra", "mezclar los tipos de trabajo", "concluir sin datos"],
        "Pregunta: «¿qué pasaría con el costo total si el correctivo no hubiera ocurrido?». Si no responde, pídele que relea cómo se separan los costos por tipo."),
    reinforce="Calcula en papel el costo de una orden de 2 horas a $9.000 la hora con repuestos por $4.000.",
    extend="Explica con un ejemplo por qué comparar costos por tipo de trabajo ayuda a decidir la inversión en preventivo.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (criterio de decisión de ejemplo, inventado). Regla de la empresa: primero se atiende el equipo de mayor riesgo para las personas; si la reparación cuesta más del 60 % del reemplazo, se evalúa reemplazar el equipo. "
     "Equipos con falla: A, panel de aviso (riesgo bajo), reparación $40.000 y reemplazo $100.000; B, fuente de un sistema de alarma (riesgo alto), reparación $75.000 y reemplazo $100.000; C, sensor de nivel (riesgo medio), reparación $35.000 y reemplazo $50.000.")
build(
    O5, 4, F,
    use="Aprenderé a priorizar fallas por riesgo y a decidir con criterio entre reparar y reemplazar, usando datos de ejemplo y dejando la decisión por escrito.",
    prior=["Sé la diferencia entre preventivo y correctivo.", "Sé calcular porcentajes sencillos.", "Sé comparar costos."],
    explain=[
        "Cuando hay varias fallas a la vez, hay que priorizar: decidir cuál se atiende primero. El criterio principal es el riesgo, que es la posibilidad de daño a personas o a bienes si el equipo falla. Un equipo de riesgo alto se atiende antes, aunque su reparación sea más cara. El costo se usa después, para decidir entre reparar o reemplazar, que es cambiar el equipo por uno nuevo.",
        "Muchas empresas fijan una regla de decisión: si la reparación cuesta más de cierto porcentaje del reemplazo, se evalúa reemplazar. El porcentaje se calcula dividiendo el costo de reparación por el de reemplazo y multiplicando por cien. Evaluar no es decidir: también se mira la vida útil, la garantía y los repuestos disponibles, y lo decide quien tiene la autoridad.",
        f"La decisión se deja por escrito: qué equipo, qué criterio y quién aprobó. Los repuestos deben ser los indicados por el fabricante y la norma. {AVISO}",
    ],
    vocab=[("priorizar", "decidir cuál falla se atiende primero según un criterio"), ("riesgo", "posibilidad de daño a personas o bienes si el equipo falla"), ("reparar", "corregir la falla del equipo existente"), ("reemplazar", "cambiar el equipo por uno nuevo"), ("regla de decisión", "criterio escrito por la empresa para decidir entre alternativas")],
    worked=[
        ("Aplicar la regla", "Un equipo de ejemplo tiene reparación de $30.000 y reemplazo de $100.000. La regla pide evaluar reemplazo si la reparación supera el 60 %. ¿Qué decisión corresponde?", ["30.000 de 100.000 es 30 %.", "30 % no supera 60 %."], "Repararlo"),
        ("Priorizar", "Dos equipos de ejemplo fallan: uno de riesgo bajo y otro de riesgo alto. ¿Cuál se atiende primero?", ["El criterio principal es el riesgo.", "El de riesgo alto va primero."], "El de riesgo alto"),
    ],
    mistakes=[("Atender primero la reparación más barata sin mirar el riesgo.", "La regla da prioridad al riesgo para las personas.", "Ordena por riesgo y luego decide por costo."),
              ("Usar repuestos más baratos que los indicados por el fabricante para ahorrar.", "Pueden no cumplir la norma ni las especificaciones.", "Usa repuestos indicados por el fabricante y la norma, e informa el costo.")],
    T=[
        ("abc", "En Electrónica: ¿qué significa priorizar una falla?", "Decidir cuál falla se atiende primero según un criterio como el riesgo", "Ordenar las fallas alfabéticamente", "Atender siempre la más fácil de reparar", "Priorizar es ordenar la atención según un criterio, y el principal es el riesgo."),
        ("abc", "En Electrónica: ¿qué es el riesgo de un equipo?", "La posibilidad de daño a personas o bienes si el equipo falla", "El precio del equipo nuevo", "La antigüedad del equipo", "El riesgo mide el daño posible; el precio y la antigüedad son otros datos."),
        ("abc", "En Electrónica: ¿qué significa reemplazar un equipo?", "Cambiarlo por uno nuevo", "Corregir su falla sin cambiarlo", "Anotar la falla en la bitácora", "Reemplazar es cambiar el equipo; corregir la falla es reparar."),
        ("abc", "{F} Según la regla, ¿qué equipo se atiende primero?", "B, la fuente de riesgo alto", "A, el panel porque es el más barato", "C, el sensor porque cuesta menos reemplazarlo", "La regla prioriza el equipo de mayor riesgo para las personas, que es B."),
        ("=", "{F} ¿Qué porcentaje del reemplazo cuesta reparar el panel A?", "40000*100//100000", "Se divide el costo de reparación por el de reemplazo y se multiplica por cien.", " %"),
        ("=", "{F} ¿Qué porcentaje del reemplazo cuesta reparar la fuente B?", "75000*100//100000", "Se divide el costo de reparación por el de reemplazo y se multiplica por cien.", " %"),
        ("=", "{F} ¿Qué porcentaje del reemplazo cuesta reparar el sensor C?", "35000*100//50000", "Se divide el costo de reparación por el de reemplazo y se multiplica por cien.", " %"),
        ("abc", "{F} ¿Para qué equipos se evalúa reemplazar?", "Para B y C, porque su reparación supera el 60 % del reemplazo", "Solo para A, porque es el más barato", "Para los tres, porque todos fallaron", "La regla evalúa reemplazo cuando la reparación supera el 60 %, y eso ocurre en B (75 %) y en C (70 %)."),
        ("abc", "{F} ¿Qué se decide con el panel A?", "Repararlo, porque su reparación no supera el 60 % del reemplazo", "Reemplazarlo, porque es el más barato", "No hacer nada, porque su riesgo es bajo", "La reparación cuesta el 40 % del reemplazo, bajo el umbral, y aunque su riesgo sea bajo igual se corrige."),
        ("abc", "{F} Un compañero propone atender primero A porque es la reparación más barata. ¿Qué argumento es correcto?", "La regla da prioridad al riesgo, por lo que B va primero", "Tiene razón, porque lo barato se hace primero", "Da lo mismo el orden, porque todo se atenderá", "El criterio principal es el riesgo para las personas, no el costo de reparar."),
        ("=", "{F} Si se repara A y se reemplaza B, ¿cuánto se gasta en total?", "40000+100000", "Se suman la reparación de A y el reemplazo de B.", " pesos"),
        ("abc", "{F} La reparación de B cuesta $25.000 menos que su reemplazo, pero la fuente tiene riesgo alto. ¿Qué pesa más al evaluar?", "El riesgo para las personas, junto con la garantía y la vida útil, más que el ahorro de $25.000", "Solo el ahorro de $25.000", "El color de la fuente", "Con riesgo alto se miran la seguridad y la fiabilidad antes del pequeño ahorro."),
        ("=", "Un equipo D de ejemplo tiene reparación de $62.000 y reemplazo de $100.000. ¿Qué porcentaje del reemplazo cuesta repararlo? (Después compáralo con el 60 % de la regla.)", "62000*100//100000", "Se calcula el porcentaje y se compara con el 60 %: 62 supera 60, así que se evalúa reemplazar.", " %"),
    ],
    ctx=("abc", "Un cliente de ejemplo pide reparar la fuente B con un componente más barato que el que indica el fabricante, «para ahorrar». ¿Qué corresponde?", "Usar los repuestos indicados por el fabricante y la norma, informando el costo", "Aceptar, porque el cliente es quien paga", "Usar el componente más barato y no anotarlo", "Los repuestos no se cambian por precio si pueden afectar la seguridad ni las especificaciones."),
    sc=[
        ("En Electrónica: ¿cuál es el criterio principal para priorizar fallas?", "El riesgo para las personas", "El riesgo manda sobre el costo."),
        ("¿Cómo se calcula el porcentaje reparación sobre reemplazo?", "Dividiendo el costo de reparar por el de reemplazar, por cien", "Es la proporción del reemplazo que cuesta reparar."),
        ("¿Qué debe quedar escrito en una decisión de reparar o reemplazar?", "El equipo, el criterio usado y quién aprobó", "Esos datos permiten revisar la decisión."),
    ],
    op=("Ficha de ejemplo (regla: se atiende primero el mayor riesgo; si reparar supera el 60 % del reemplazo, se evalúa reemplazar): X, timbre (riesgo bajo), reparación $12.000, reemplazo $30.000; Y, fuente de una alarma (riesgo alto), reparación $56.000, reemplazo $80.000; Z, sensor (riesgo medio), reparación $20.000, reemplazo $40.000. Escribe (a) el orden de atención, (b) el porcentaje de cada equipo, (c) qué decisión de reparar o evaluar reemplazo corresponde a cada uno, (d) cuánto se gasta si se repara X y Z.",
        "(a) Y, Z y X. (b) X: 12.000 de 30.000 es 40 %; Y: 56.000 de 80.000 es 70 %; Z: 20.000 de 40.000 es 50 %. (c) X, reparar; Y, evaluar reemplazo, porque supera el 60 %; Z, reparar. (d) 12.000 más 20.000 son 32.000 pesos.",
        ["ordena por riesgo", "calcula bien los porcentajes", "aplica la regla del 60 %", "suma bien el gasto"],
        ["hoja con la tabla de decisión"],
        ["ordenar por costo", "calcular mal el porcentaje", "no aplicar la regla"],
        "Pregunta: «¿qué otro dato pedirías antes de decidir sobre Y?». Si no responde, pídele que relea las consideraciones adicionales de la explicación."),
    reinforce="Inventa tres equipos con riesgo, costo de reparación y de reemplazo, y decide el orden de atención y la acción de cada uno.",
    extend="Explica con un ejemplo por qué la regla de decisión debe estar escrita antes de que ocurra la falla.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (encargo de ejemplo, inventado). Un condominio ficticio pide automatizar cuatro cosas: (a) el riego del jardín, con un temporizador; (b) las luces del pasillo, con un sensor de presencia; "
     "(c) el portón del estacionamiento, con control remoto; (d) el ascensor del edificio. Documentos: requerimientos del proyecto y hojas de especificaciones del fabricante de cada equipo.")
build(
    O6, 1, F,
    use="Aprenderé qué significa configurar un sistema automático simple, qué documentos guían esa tarea y por qué portones y ascensores son tareas solo para personal autorizado.",
    prior=["Sé qué es un sensor y un controlador.", "Sé qué es una hoja de especificaciones.", "Sé que algunas tareas exigen personal autorizado."],
    explain=[
        "Un sistema automático simple actúa solo a partir de lo que detectan sus sensores o de un horario. La domótica es la automatización de funciones de una vivienda o un edificio: luces, riego, accesos, ascensores. Configurar un sistema es definir cómo debe funcionar, ajustando sus parámetros: valores como horas, tiempos o umbrales. Se hace según los requerimientos del proyecto, que son lo que el cliente necesita que el sistema haga, y según las especificaciones del fabricante.",
        "El riesgo cambia mucho según el sistema. Un riego o una luz tienen un riesgo mecánico bajo. Un portón puede atrapar o aplastar a una persona o a un vehículo, y un ascensor puede dejar a alguien detenido o provocar caídas. Por eso los portones y los ascensores los configuran empresas y personal autorizado y certificado según la norma vigente, y sus protecciones nunca se desactivan.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("sistema automático", "sistema que actúa solo según lo que detectan sus sensores o según un horario"), ("domótica", "automatización de funciones de una vivienda o edificio"), ("parámetro", "valor ajustable, como una hora, un tiempo o un umbral"), ("requerimiento", "lo que el cliente necesita que el sistema haga"), ("protección", "dispositivo o función que evita daños a personas o equipos")],
    worked=[
        ("Elegir el documento", "Una técnica de ejemplo quiere saber qué espera el cliente de un sistema de luces. ¿Qué documento consulta?", ["Lo que el cliente necesita está escrito en un documento del proyecto.", "Ese documento es el de requerimientos."], "Los requerimientos del proyecto"),
        ("Nivel de riesgo", "Un sistema de ejemplo controla una válvula de riego y otro un portón de reja. ¿Cuál tiene más riesgo de atrapar a una persona?", ["La válvula no tiene piezas grandes que cierren sobre una persona.", "El portón sí."], "El portón"),
    ],
    mistakes=[("Desactivar la protección de un portón para que cierre más rápido.", "La protección evita atrapamientos de personas y vehículos.", "Las protecciones nunca se desactivan; cualquier cambio lo decide personal autorizado."),
              ("Creer que si se sabe configurar una luz también se puede configurar un ascensor.", "El ascensor tiene riesgos distintos y exige personal certificado.", "Deriva ascensores y portones a personal autorizado según la norma vigente.")],
    T=[
        ("abc", "En Electrónica: ¿qué es configurar un sistema automático?", "Definir cómo debe funcionar ajustando sus parámetros según los requerimientos y el fabricante", "Fabricar los componentes del sistema", "Desarmar el sistema para guardarlo", "Configurar es ajustar el funcionamiento; fabricar o desarmar son otras tareas."),
        ("abc", "En Electrónica: ¿qué es la domótica?", "La automatización de funciones de una vivienda o un edificio", "El estudio de la corriente en las baterías", "La reparación de aparatos antiguos", "La domótica automatiza luces, riego, accesos y otras funciones de un edificio."),
        ("abc", "En Electrónica: ¿qué es un requerimiento del proyecto?", "Lo que el cliente necesita que el sistema haga", "El precio de los equipos del fabricante", "La lista de herramientas del taller", "El requerimiento expresa la necesidad del cliente."),
        ("abc", "{F} ¿Qué sistemas de la ficha pueden atrapar o aplastar a una persona?", "El portón del estacionamiento y el ascensor", "El riego y las luces del pasillo", "Solo las luces del pasillo", "El portón y el ascensor tienen partes grandes en movimiento."),
        ("abc", "{F} ¿Qué sistemas de la ficha tienen riesgo mecánico más bajo?", "El riego del jardín y las luces del pasillo", "El portón y el ascensor", "El ascensor y las luces del pasillo", "El riego y las luces no tienen cabinas ni hojas que cierren sobre una persona."),
        ("abc", "{F} ¿Qué documento de la ficha dice qué necesita el cliente?", "Los requerimientos del proyecto", "Las hojas de especificaciones del fabricante", "El control remoto del portón", "Los requerimientos recogen lo que el cliente quiere; las hojas dicen cómo funciona cada equipo."),
        ("=", "{F} Cada uno de los cuatro sistemas tiene 3 parámetros por configurar. ¿Cuántos parámetros hay en total?", "4*3", "Los parámetros de cada sistema se multiplican por los cuatro sistemas.", " parámetros"),
        ("abc", "{F} Un compañero propone configurar el ascensor «porque es como un portón». ¿Qué corresponde?", "Que lo haga personal autorizado y certificado según la norma vigente", "Que lo haga un estudiante con las hojas del fabricante", "Que se haga sin protecciones para ahorrar tiempo", "El ascensor tiene riesgos propios y su configuración es de personal certificado."),
        ("ab", "Una estudiante terminó este cuaderno y quiere cambiar el tiempo de cierre del portón de su colegio. ¿Qué corresponde?", "No hacerlo: el portón exige personal autorizado, norma vigente y protecciones", "Hacerlo con cuidado, porque ya sabe qué es un parámetro", "Un portón puede atrapar a personas; conocer el concepto de parámetro no habilita para ajustarlo."),
        ("abc", "{F} Los requerimientos piden luces con sensor de presencia, pero la hoja del fabricante dice que ese sensor solo sirve en exteriores. ¿Qué corresponde?", "Informar al supervisor o proyectista para que decida y corrija el diseño", "Instalarlo igual en el pasillo interior", "Cambiar el requerimiento por cuenta propia", "Si el equipo no cumple la hoja, se informa; nadie cambia por su cuenta documentos ni requisitos."),
        ("=", "El riego de un jardín de ejemplo tiene 3 zonas que riegan 15 minutos cada una, una tras otra. ¿Cuántos minutos dura el riego completo?", "3*15", "Los minutos de cada zona se multiplican por el número de zonas.", " minutos"),
        ("abc", "{F} ¿Por qué no se desactivan las protecciones de un portón automático para que cierre más rápido?", "Porque protegen a personas y vehículos de un atrapamiento", "Porque son solo decorativas", "Porque gastan más energía que el motor", "Las protecciones evitan daños graves y no son opcionales."),
        ("abc", "Una persona queda detenida dentro de un ascensor de un edificio. ¿Qué corresponde de forma general?", "Avisar a la administración del edificio y a emergencias, sin forzar las puertas", "Forzar las puertas para que salga más rápido", "Intentar mover la cabina con las manos", "Forzar un ascensor es peligroso; se avisa y se espera personal autorizado."),
    ],
    ctx=("abc", "El administrador de un condominio de ejemplo pide: «desactiva el sensor del portón, que se detiene demasiado seguido». Como estudiante, ¿qué respondes?", "Que las protecciones no se desactivan y que lo revise la empresa autorizada", "Que lo harás si él firma una autorización", "Que lo desactivarás solo de noche", "Las protecciones del portón no se desactivan; la revisión corresponde a personal autorizado."),
    sc=[
        ("En Electrónica: ¿qué es un parámetro de un sistema automático?", "Un valor ajustable, como un tiempo o un umbral", "Los parámetros definen cómo funciona el sistema."),
        ("¿Quién configura ascensores y portones?", "Personal autorizado y certificado, según la norma vigente", "Este cuaderno no habilita para trabajar con ellos."),
        ("¿Se pueden desactivar las protecciones de un portón?", "No, nunca", "Las protecciones del portón evitan atrapamientos de personas y vehículos."),
    ],
    op=("Ficha de ejemplo: una escuela ficticia pide (a) luces del patio con sensor de luz, (b) un portón corredero con control remoto, (c) riego de la cancha con temporizador, (d) un timbre automático por horario. Escribe (a) cuáles de los cuatro tienen más riesgo para las personas y por qué, (b) cuál documento dice lo que la escuela necesita, (c) quién configuraría el portón, (d) un ejemplo de parámetro del riego.",
        "(a) El portón corredero, que puede atrapar o aplastar. (b) Los requerimientos del proyecto. (c) Personal autorizado según la norma vigente. (d) La hora de inicio, la duración en minutos o los días del riego.",
        ["identifica el sistema de más riesgo con razón", "nombra el documento correcto", "dice quién configura el portón", "da un parámetro válido"],
        ["hoja con las cuatro respuestas"],
        ["decir que el estudiante configuraría el portón", "elegir el riego como el de más riesgo", "dar como parámetro algo que no se ajusta"],
        "Pregunta: «¿qué protección pedirías en el portón?». Si no responde, pídele que relea el párrafo sobre riesgos."),
    reinforce="Escribe cuatro sistemas automáticos de un hogar y ordénalos de menor a mayor riesgo para las personas, con una razón por cada uno.",
    extend="Explica con un ejemplo por qué una protección nunca se desactiva para ganar velocidad.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (sistema de iluminación de ejemplo, inventado). Entradas: PIR, sensor de presencia (digital: 1 hay alguien, 0 no hay); LUX, sensor de luz (analógico: de 0 V, oscuro, a 10 V, muy iluminado); SW, selector de modo (digital: 1 automático, 0 manual). "
     "Salida: RELÉ de la lámpara (digital: 1 enciende la lámpara). Regla en modo automático: la lámpara se enciende si PIR vale 1 y LUX marca menos de 3 V.")
build(
    O6, 2, F,
    use="Aprenderé el vocabulario de un sistema automático: entradas, controlador y salidas, señales digitales y analógicas, y a seguir en papel una regla si-entonces.",
    prior=["Sé qué es un sensor y una señal digital.", "Sé comparar un valor con un umbral.", "Sé calcular un porcentaje sencillo."],
    explain=[
        "Un sistema automático tiene tres partes. Las entradas son las señales que llegan al controlador desde sensores, pulsadores o selectores. El controlador compara esas señales con las reglas del programa y decide. Las salidas son lo que el controlador ordena: encender una lámpara, abrir una válvula, mover un motor. El componente que ejecuta la acción se llama actuador.",
        "Una señal digital solo tiene dos valores, 1 o 0. Una señal analógica varía de forma continua dentro de un rango, por ejemplo de 0 V a 10 V. Un relé es un componente que, con una señal pequeña, abre o cierra un interruptor para controlar una carga mayor. Una regla si-entonces dice: si se cumple la condición, entonces ocurre la acción. Seguir una regla en papel es comprobar condición por condición.",
        f"Solo se trabajan señales de bajo valor, en papel y con ejemplos. {AVISO}",
    ],
    vocab=[("entrada", "señal que llega al controlador desde un sensor, pulsador o selector"), ("salida", "orden que el controlador envía a un actuador"), ("actuador", "componente que ejecuta una acción, como encender una luz o mover una válvula"), ("señal analógica", "señal que varía de forma continua dentro de un rango"), ("relé", "componente que, con una señal pequeña, abre o cierra un interruptor para una carga mayor"), ("regla si-entonces", "instrucción que ejecuta una acción solo si se cumple una condición")],
    worked=[
        ("Clasificar una señal", "Un detector de humo de ejemplo entrega 1 si detecta humo y 0 si no. ¿Es digital o analógica?", ["Solo tiene dos valores.", "Eso corresponde a una señal digital."], "Digital"),
        ("Seguir una regla", "Regla de ejemplo: la bomba se enciende si el nivel es menor que 20 %. El nivel marca 15 %. ¿Se enciende la bomba?", ["15 es menor que 20.", "Se cumple la condición."], "Sí, se enciende"),
    ],
    mistakes=[("Decir que la salida de un relé es analógica porque el sensor de luz lo es.", "La salida del relé solo tiene dos valores: enciende o no.", "Clasifica cada señal por separado: sensor analógico, relé digital."),
              ("Aplicar la regla de modo automático cuando el selector está en manual.", "En manual la regla automática no gobierna la lámpara.", "Comprueba primero el modo y luego el resto de las condiciones.")],
    T=[
        ("abc", "En Electrónica: ¿qué es un actuador?", "Un componente que ejecuta una acción, como encender una luz o mover una válvula", "Un sensor que mide la luz del ambiente", "Una fuente que alimenta el controlador", "El actuador ejecuta la orden del controlador; el sensor mide y la fuente alimenta."),
        ("abc", "En Electrónica: ¿qué es una entrada de un sistema automático?", "Una señal que llega al controlador desde un sensor, un pulsador o un selector", "La orden que el controlador envía a la lámpara", "El cable que une la fuente con la pared", "Las entradas informan al controlador de lo que ocurre."),
        ("abc", "En Electrónica: ¿qué hace un relé?", "Con una señal pequeña abre o cierra un interruptor que controla una carga mayor", "Mide la luz del ambiente", "Guarda energía para después", "El relé es un interruptor accionado por una señal de control."),
        ("abc", "{F} ¿Cuál de las entradas de la ficha es analógica?", "LUX, que varía entre 0 V y 10 V", "PIR, que vale 1 o 0", "SW, que vale 1 o 0", "Solo LUX varía de forma continua; PIR y SW tienen dos valores."),
        ("abc", "{F} ¿Cuál es la salida del sistema de la ficha?", "El relé de la lámpara", "El sensor de presencia PIR", "El selector de modo SW", "Las salidas son lo que el controlador ordena; aquí, encender la lámpara mediante el relé."),
        ("abc", "{F} Con SW = 1, PIR = 1 y LUX = 2 V, ¿se enciende la lámpara?", "Sí, porque hay presencia y la luz es menor que 3 V", "No, porque 2 V es muy poco", "No, porque falta que SW valga 0", "En modo automático, con presencia y menos de 3 V, la regla manda encender."),
        ("abc", "{F} Con SW = 1, PIR = 1 y LUX = 7 V, ¿se enciende la lámpara?", "No, porque hay luz suficiente: 7 V no es menor que 3 V", "Sí, porque hay presencia", "Sí, porque 7 V es mayor", "Hay presencia, pero la regla exige también poca luz."),
        ("abc", "{F} Con SW = 0, PIR = 1 y LUX = 1 V, ¿actúa la regla automática?", "No: en modo manual la regla automática no gobierna la lámpara", "Sí, porque hay presencia y poca luz", "Sí, porque LUX vale 1", "La regla se aplica solo con SW en 1, que es el modo automático."),
        ("=", "{F} Si LUX marca 4 V en su rango de 0 a 10 V, ¿qué porcentaje del rango es?", "4*100//10", "Se divide la lectura por el máximo del rango y se multiplica por cien.", " %"),
        ("abc", "{F} El sensor LUX se desconecta y entrega siempre 0 V. Con SW = 1 y PIR = 1 en pleno día, ¿qué ocurre?", "La lámpara se enciende aunque haya luz, porque el controlador cree que está oscuro", "La lámpara nunca enciende", "El relé se rompe al instante", "Un 0 V falso equivale a oscuridad, de modo que se cumple la regla sin necesidad."),
        ("abc", "Un técnico afirma que la salida del relé es una señal analógica porque «la luz es analógica». ¿Qué corrección corresponde?", "La salida del relé es digital, porque solo tiene dos estados", "Tiene razón, porque la luz varía de forma continua", "La salida del relé no es una señal", "La salida del relé solo vale 1 o 0, aunque el sensor sea analógico."),
        ("=", "Un controlador de ejemplo tiene 10 entradas. Un sistema usa 3 sensores digitales, 2 sensores analógicos y 3 pulsadores, cada uno en una entrada. ¿Cuántas entradas quedan libres?", "10-(3+2+3)", "Se restan las entradas usadas a las que tiene el controlador.", " entradas"),
        ("abc", "{F} Se quiere agregar una segunda lámpara que encienda junto con la primera. ¿Qué debe revisarse antes?", "Que el relé y las especificaciones del fabricante soporten la carga adicional", "Que la lámpara sea del mismo color", "Nada, porque un relé soporta cualquier carga", "Cada relé tiene un límite de carga indicado en la hoja del fabricante."),
    ],
    ctx=("abc", "Una escuela de ejemplo quiere un timbre que suene a las 8:00 si el selector de modo está en automático. ¿Qué elementos tiene el sistema?", "Entrada: reloj y selector; controlador; salida: timbre", "Entrada: timbre; salida: reloj", "Solo un actuador, sin entradas ni controlador", "El reloj y el selector informan al controlador, que ordena sonar al timbre, que es el actuador."),
    sc=[
        ("En Electrónica: ¿qué es una señal analógica?", "Una señal que varía de forma continua dentro de un rango", "Se opone a la digital, que solo tiene dos valores."),
        ("¿Qué es un actuador?", "El componente que ejecuta la acción ordenada", "Por ejemplo, una válvula o una lámpara."),
        ("¿Qué se comprueba primero en una regla de modo automático?", "Que el selector esté en automático", "Sin modo automático la regla no gobierna."),
    ],
    op=("Ficha de ejemplo: sistema de riego de una maceta. Entradas: HUM, sensor de humedad (analógico, de 0 a 10 V; 0 es seco y 10 es muy húmedo); SW, selector (1 automático, 0 manual). Salida: VAL, válvula (1 abre). Regla en modo automático: la válvula abre si HUM marca menos de 4 V. Escribe (a) cuál entrada es analógica, (b) qué hace la válvula con SW = 1 y HUM = 3 V, (c) qué hace con SW = 0 y HUM = 3 V, (d) qué porcentaje del rango es HUM = 3 V.",
        "(a) HUM. (b) Abre, porque está en automático y 3 V es menor que 4 V. (c) La regla automática no gobierna: en manual la válvula no abre por la regla. (d) 3 por 100 ÷ 10 son 30 %.",
        ["identifica la entrada analógica", "aplica bien la regla en automático", "explica el modo manual", "calcula bien el porcentaje"],
        ["hoja con las cuatro respuestas"],
        ["ignorar el modo", "confundir analógica con digital", "calcular mal el porcentaje"],
        "Pregunta: «¿qué pasaría si HUM fallara y marcara 0 V siempre?». Si no responde, pídele que relea el ejemplo del sensor desconectado."),
    reinforce="Describe el sistema de luz de un baño con sensor de presencia, indicando entradas, controlador y salida.",
    extend="Explica con un ejemplo por qué una falla de un sensor puede hacer que una regla correcta dé un resultado equivocado.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (riego automático de ejemplo, inventado). Regla R1: el riego parte a las 7:00 y riega 15 minutos en cada una de 3 zonas, una después de otra, en los días programados (lunes, miércoles y viernes). "
     "Regla R2: si el sensor de lluvia marca 1, ese día no se riega. Regla R3: si la humedad del suelo es más del 70 %, ese día no se riega. Caudal de cada zona: 20 litros por minuto.")
build(
    O6, 3, F,
    use="Aprenderé a analizar en papel un programa horario con reglas si-entonces, a calcular tiempos y litros y a anticipar qué hará el sistema en cada día.",
    prior=["Sé qué es una regla si-entonces.", "Sé qué es un parámetro.", "Sé multiplicar y sumar."],
    explain=[
        "Un temporizador es una función que cuenta tiempo y actúa cuando se cumple. Un programa horario es la tabla que fija los días y las horas en que el sistema actúa. En un riego automático se combinan el horario y las condiciones de los sensores: el sistema solo riega si el día y la hora están programados y ninguna condición lo impide. Si una condición se cumple, la regla correspondiente manda no regar.",
        "Para anticipar el comportamiento se revisa cada día con sus datos. Se comprueba primero si es día programado, luego la lluvia y luego la humedad. Para estimar el agua se multiplica el caudal por los minutos de cada zona, y eso por el número de zonas. «Más del 70 %» significa mayor que 70.",
        f"Un cambio de parámetro, como la duración, se registra y se verifica con casos en papel antes de aplicarse por personal autorizado. {AVISO}",
    ],
    vocab=[("temporizador", "función que cuenta tiempo y actúa cuando se cumple"), ("programa horario", "tabla que fija los días y las horas en que el sistema actúa"), ("caudal", "cantidad de agua que pasa por minuto"), ("condición", "situación que se debe cumplir para que una regla actúe"), ("zona de riego", "sector del jardín regado por una misma válvula")],
    worked=[
        ("Duración total", "Un riego de ejemplo tiene 2 zonas de 10 minutos cada una. ¿Cuánto dura el riego completo?", ["Cada zona dura 10 minutos.", "10 por 2 son 20."], "20 minutos"),
        ("Litros de una zona", "Una zona de ejemplo tiene un caudal de 12 litros por minuto y riega 10 minutos. ¿Cuántos litros usa?", ["Se multiplica el caudal por los minutos.", "12 por 10 son 120."], "120 litros"),
    ],
    mistakes=[("Contar un día de lluvia como día de riego porque está en el programa horario.", "Cuando una condición lo impide, la regla manda no regar.", "Revisa el día programado y luego cada condición."),
              ("Creer que «más del 70 %» incluye el 70 %.", "70 no es mayor que 70.", "Lee la condición exacta: solo el valor mayor cuenta.")],
    T=[
        ("abc", "En Electrónica: ¿qué es una regla si-entonces en un programa de control?", "Una instrucción que ejecuta una acción solo si se cumple una condición", "Una lista de precios de los sensores", "Un dibujo de las conexiones", "La regla si-entonces liga una condición con una acción."),
        ("abc", "En Electrónica: ¿qué es un temporizador?", "Una función que cuenta tiempo y actúa cuando se cumple", "Un sensor que mide la humedad", "Una fuente de energía de respaldo", "El temporizador actúa según el tiempo, no según una medición."),
        ("abc", "En Electrónica: ¿qué es un programa horario?", "La tabla que fija los días y las horas en que el sistema actúa", "El manual de mantenimiento del fabricante", "La lista de componentes del controlador", "El programa horario define cuándo actúa el sistema."),
        ("=", "{F} ¿Cuántos minutos dura el riego completo de las 3 zonas?", "3*15", "Los minutos de cada zona se multiplican por las 3 zonas.", " minutos"),
        ("abc", "{F} Si el riego parte a las 7:00 y las zonas se riegan una tras otra, ¿a qué hora termina?", "A las 7:45", "A las 7:15", "A las 8:00", "Son 45 minutos en total: 15 minutos por cada una de las 3 zonas."),
        ("=", "{F} ¿Cuántos litros usa una zona en una pasada?", "20*15", "El caudal se multiplica por los minutos de riego de la zona.", " litros"),
        ("=", "{F} ¿Cuántos litros se usan en un día de riego completo, con las 3 zonas?", "3*20*15", "Se multiplican las zonas, el caudal y los minutos de cada una.", " litros"),
        ("abc", "{F} Un miércoles con el sensor de lluvia en 1 y humedad de 40 %, ¿se riega?", "No, porque la regla R2 manda no regar si llueve", "Sí, porque es día programado y la humedad es baja", "Sí, porque la humedad no pasa del 70 %", "R2 impide regar cuando el sensor de lluvia marca 1, aunque el día esté programado."),
        ("abc", "{F} Un viernes con el sensor de lluvia en 0 y humedad de 75 %, ¿se riega?", "No, porque la humedad es más del 70 % y R3 lo impide", "Sí, porque no llueve", "Sí, porque 75 está cerca de 70", "R3 impide regar cuando la humedad supera el 70 %."),
        ("abc", "{F} Un lunes con lluvia en 0 y humedad de exactamente 70 %, ¿se riega?", "Sí, porque 70 % no es más del 70 %", "No, porque la humedad llegó al 70 %", "No, porque se necesita una humedad menor que 50 %", "R3 impide regar solo con más del 70 %; 70 no es mayor que 70."),
        ("=", "{F} Si se riega los tres días programados de una semana sin que ninguna regla lo impida, ¿cuántos litros se usan en la semana?", "3*3*20*15", "Se multiplican los días de riego, las zonas, el caudal y los minutos por zona.", " litros"),
        ("abc", "{F} El sensor de lluvia falla y marca siempre 0. ¿Qué consecuencia tiene?", "El sistema también riega cuando llueve y gasta agua sin necesidad", "El sistema nunca riega", "El sistema riega todos los días de la semana", "Con lluvia falsamente en 0, R2 nunca se aplica y el riego sigue el horario aunque llueva."),
        ("abc", "{F} Se propone cambiar la duración de 15 a 10 minutos por zona. ¿Qué corresponde hacer con el cambio de parámetro?", "Registrarlo, recalcular los litros y avisar a quien lo aprobó", "Cambiarlo sin avisar", "Cambiar también el caudal de cada zona", "Un cambio de parámetro se registra y se comunica, porque modifica el consumo y el comportamiento."),
    ],
    ctx=("abc", "El jardinero de un condominio de ejemplo se queja de que el riego «funciona los lunes aunque llueve». ¿Qué revisa un técnico que sigue la ficha?", "Si el sensor de lluvia entrega 1 en esos días, porque la regla R2 depende de él", "Si el caudal de las zonas es de 20 litros por minuto", "Si el riego parte a las 7:00 y no a las 8:00", "Si llueve y se riega, lo lógico es revisar la entrada que debería impedir el riego, que es el sensor de lluvia."),
    sc=[
        ("En Electrónica: ¿qué es un caudal?", "La cantidad de agua que pasa por minuto", "Se mide, por ejemplo, en litros por minuto."),
        ("¿Qué significa «más del 70 %»?", "Un valor mayor que 70", "Se lee como mayor que 70."),
        ("¿Qué se comprueba primero para saber si hoy se riega?", "Si es un día programado", "Sin día programado las demás condiciones no importan."),
    ],
    op=("Ficha de ejemplo: riego de un huerto escolar. Regla R1: riega a las 8:00, 10 minutos en cada una de 2 zonas, una tras otra, martes y jueves. Regla R2: si la lluvia marca 1, no riega. Caudal de cada zona: 15 litros por minuto. Datos de una semana: martes, lluvia 0; jueves, lluvia 1. Escribe (a) cuántos minutos dura un riego completo, (b) a qué hora termina, (c) cuántos litros se usan en un riego completo, (d) cuántos litros se usaron esa semana.",
        "(a) 2 por 10 son 20 minutos. (b) A las 8:20. (c) 2 zonas por 15 litros por minuto por 10 minutos son 300 litros. (d) Solo se regó el martes (el jueves llovió y R2 lo impidió): 300 litros.",
        ["calcula bien la duración", "calcula bien la hora de término", "calcula bien los litros", "aplica R2 al jueves"],
        ["hoja con los cálculos y la explicación de cada día"],
        ["contar el jueves como día de riego", "calcular mal los litros", "olvidar sumar solo los días regados"],
        "Pregunta: «¿qué pasaría si el sensor de lluvia estuviera malo?». Si no responde, pídele que relea el efecto de un sensor que falla."),
    reinforce="Escribe el programa horario de un sistema de luces que se enciendan de lunes a viernes de 18:00 a 22:00, y calcula las horas de encendido por semana.",
    extend="Explica con un ejemplo por qué conviene probar en papel un cambio de horario antes de aplicarlo.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (hoja del fabricante de ejemplo, inventada) de un termostato de ambiente. Parámetros: temperatura de encendido ajustable de 10 °C a 30 °C; histéresis ajustable de 1 °C a 5 °C (diferencia entre la temperatura de apagado y la de encendido); retardo de encendido de 0 a 120 segundos. "
     "Valores de fábrica: encendido 18 °C, histéresis 2 °C, retardo 30 s. Requerimiento del cliente: calefacción que encienda a 20 °C y se apague a 24 °C.")
build(
    O6, 4, F,
    use="Aprenderé a leer parámetros y rangos de una hoja del fabricante y a comprobar en papel si una configuración pedida es posible, antes de proponerla.",
    prior=["Sé qué es un parámetro.", "Sé qué es una regla si-entonces.", "Sé restar y sumar temperaturas."],
    explain=[
        "La hoja del fabricante dice qué parámetros tiene un equipo y qué valores admite cada uno: su rango. Un valor de fábrica es con el que el equipo sale configurado. Un termostato enciende la calefacción cuando la temperatura baja de cierto valor y la apaga cuando sube. La histéresis es la diferencia entre la temperatura de apagado y la de encendido; evita que el equipo se encienda y apague muy seguido cerca del valor, lo que lo desgastaría.",
        "Para decidir si una configuración es posible, se comprueba cada parámetro contra su rango. Si un valor pedido queda fuera, no se aplica: se informa y se propone otra alternativa aprobada. Todo cambio de parámetro se registra con el valor anterior, el valor nuevo, el motivo, la fecha y quién lo autorizó.",
        f"Ningún valor de este cuaderno es real: son datos de ejemplo para ejercitar la lectura de rangos. {AVISO}",
    ],
    vocab=[("rango", "intervalo de valores que se puede ajustar sin salir de lo especificado"), ("valor de fábrica", "valor con que el equipo sale configurado"), ("histéresis", "diferencia entre la temperatura de apagado y la de encendido"), ("retardo", "tiempo de espera antes de ejecutar una acción"), ("registro de cambio", "nota con valor anterior, valor nuevo, motivo, fecha y autorización")],
    worked=[
        ("Dentro del rango", "Un parámetro de ejemplo admite de 5 a 25 °C. ¿Se puede ajustar a 30 °C?", ["30 es mayor que el máximo de 25.", "Queda fuera del rango."], "No, está fuera del rango"),
        ("Temperatura de apagado", "Un termostato de ejemplo enciende a 16 °C y tiene histéresis de 3 °C. ¿A qué temperatura apaga?", ["La histéresis es la diferencia entre apagado y encendido.", "16 más 3 son 19."], "A 19 °C"),
    ],
    mistakes=[("Aplicar un valor fuera del rango del fabricante porque el cliente lo pidió.", "El equipo puede funcionar mal o dañarse fuera de su rango.", "Informa que el valor no es posible y propone una alternativa aprobada."),
              ("Cambiar un parámetro sin dejar registro del valor anterior.", "Si algo falla, no se podrá volver a la configuración previa.", "Registra el valor anterior, el nuevo, el motivo, la fecha y quién autorizó.")],
    T=[
        ("abc", "En Electrónica: ¿qué es la histéresis de un termostato?", "La diferencia entre la temperatura de apagado y la de encendido", "La temperatura más alta que soporta el aparato", "El tiempo que tarda en encender", "La histéresis separa las temperaturas de encendido y apagado."),
        ("abc", "En Electrónica: ¿qué es el valor de fábrica de un parámetro?", "El valor con que el equipo sale configurado", "El último valor que dejó el técnico", "El valor máximo que admite el equipo", "El valor de fábrica viene definido por el fabricante."),
        ("abc", "En Electrónica: ¿qué es el rango de un parámetro?", "El intervalo de valores que se puede ajustar sin salir de lo especificado", "El precio del parámetro en el mercado", "El nombre del parámetro en el manual", "El rango marca los límites mínimo y máximo."),
        ("=", "{F} Con los valores de fábrica, ¿a qué temperatura en °C apaga el termostato?", "18+2", "La temperatura de apagado es la de encendido más la histéresis.", " °C"),
        ("=", "{F} ¿Qué histéresis necesita el requerimiento del cliente, en °C?", "24-20", "La histéresis es la diferencia entre la temperatura de apagado y la de encendido.", " °C"),
        ("abc", "{F} ¿Está la histéresis que pide el cliente dentro del rango del fabricante?", "Sí, porque 4 °C está entre 1 °C y 5 °C", "No, porque 4 °C es mayor que el valor de fábrica", "No, porque el rango solo admite 2 °C", "El rango admitido va de 1 °C a 5 °C y 4 °C queda dentro."),
        ("abc", "{F} Un técnico propone una temperatura de encendido de 35 °C. ¿Qué corresponde?", "No aplicarla, porque está fuera del rango de 10 °C a 30 °C, e informar", "Aplicarla, porque el equipo la aceptará", "Aplicarla y anotar que fue una prueba", "Un valor fuera del rango no se aplica; se informa y se propone otra alternativa."),
        ("abc", "{F} Otro técnico propone un retardo de encendido de 150 segundos. ¿Qué corresponde?", "No aplicarlo, porque supera el máximo de 120 segundos", "Aplicarlo, porque el retardo no afecta al equipo", "Aplicarlo, porque 150 es múltiplo de 30", "El retardo máximo admitido es 120 segundos."),
        ("=", "{F} Si se fija el encendido en 15 °C y la histéresis en 3 °C, ¿a qué temperatura en °C apaga?", "15+3", "Se suma la histéresis a la temperatura de encendido.", " °C"),
        ("abc", "{F} ¿Por qué se usa una histéresis en un termostato?", "Para que el equipo no se encienda y apague seguido cerca del valor, lo que lo desgastaría", "Para ahorrar el sensor de temperatura", "Para que la calefacción nunca apague", "La histéresis separa los valores de encendido y apagado y evita ciclos muy rápidos."),
        ("abc", "{F} Otro cliente pide encender a 20 °C y apagar a 27 °C. ¿Se puede con este termostato?", "No: necesitaría una histéresis de 7 °C, mayor que el máximo de 5 °C; se informa y se propone otra alternativa", "Sí, porque 27 °C es menor que 30 °C", "Sí, porque la histéresis es de fábrica", "La histéresis pedida supera el rango, aunque las temperaturas por separado estén dentro."),
        ("abc", "{F} Antes de cambiar un parámetro de este termostato, ¿qué conviene registrar?", "El valor anterior, el valor nuevo, el motivo, la fecha y quién lo autorizó", "Solo el valor nuevo", "Solo la marca del equipo", "El registro completo permite volver atrás y entender el cambio."),
        ("=", "{F} Si la histéresis queda en el máximo de 5 °C y el apagado no debe pasar de 30 °C, ¿cuál es la temperatura de encendido máxima en °C?", "30-5", "La temperatura de encendido es la de apagado menos la histéresis.", " °C"),
    ],
    ctx=("abc", "Un cliente de ejemplo dice: «quiero que encienda a 8 °C»; el rango del termostato es de 10 °C a 30 °C. ¿Qué respondes?", "Que ese valor está fuera del rango del fabricante y que se debe proponer una alternativa aprobada", "Que se pondrá igual y se verá si funciona", "Que se cambiará el rango del equipo en la hoja de datos", "Un valor fuera del rango no se aplica, y la hoja del fabricante no se modifica."),
    sc=[
        ("En Electrónica: ¿cómo se calcula la temperatura de apagado de un termostato?", "Sumando la histéresis a la de encendido", "La histéresis es la diferencia entre ambas."),
        ("¿Qué se hace con un valor pedido que está fuera del rango?", "Se informa y se propone una alternativa aprobada", "No se aplica un valor fuera de lo especificado."),
        ("¿Qué debe llevar el registro de un cambio de parámetro?", "Valor anterior, valor nuevo, motivo, fecha y autorización", "Con esos datos se puede volver atrás."),
    ],
    op=("Ficha de ejemplo: controlador de un ventilador. Parámetros del fabricante: temperatura de encendido de 20 °C a 40 °C; histéresis de 2 °C a 6 °C; retardo de 0 a 60 s. Valores de fábrica: encendido 28 °C, histéresis 3 °C, retardo 10 s. Requerimiento: ventilador que encienda a 30 °C y apague a 33 °C, con retardo de 20 s. Escribe (a) la histéresis necesaria, (b) si cada parámetro pedido está en rango, (c) a qué temperatura apagaría con los valores de fábrica, (d) qué anotarías en el registro de cambio.",
        "(a) 33 menos 30 son 3 °C. (b) Encendido 30 °C está entre 20 y 40: en rango. Histéresis 3 °C está entre 2 y 6: en rango. Retardo 20 s está entre 0 y 60: en rango. (c) 28 más 3 son 31 °C. (d) Valores anteriores (28 °C, 3 °C, 10 s), valores nuevos (30 °C, 3 °C, 20 s), motivo, fecha y quién autorizó.",
        ["calcula bien la histéresis", "comprueba cada rango", "calcula el apagado de fábrica", "redacta bien el registro de cambio"],
        ["hoja con las comprobaciones y el registro"],
        ["no comprobar todos los rangos", "calcular mal la temperatura de apagado", "olvidar el valor anterior en el registro"],
        "Pregunta: «¿qué harías si el cliente pidiera encender a 45 °C?». Si no responde, pídele que relea qué se hace con un valor fuera del rango."),
    reinforce="Inventa tres parámetros con su rango y propón un valor válido y uno inválido para cada uno.",
    extend="Explica con un ejemplo por qué un registro de cambio permite volver a la configuración anterior.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (alternativas y pruebas de ejemplo, inventadas) para iluminar un pasillo 10 horas al día durante 30 días. Alternativa 1: lámpara de 100 W, $3.000 de compra, sin sensor. "
     "Alternativa 2: lámpara de 20 W, $9.000 de compra, con sensor de presencia que la deja encendida solo 4 horas al día. Precio de la energía de ejemplo: $150 por kWh (1 kWh es la energía de 1000 W durante 1 hora). "
     "Pruebas de la alternativa 2 (resultados de ejemplo de personal autorizado): caso 1, sin presencia y oscuro, esperado apagada, obtenido apagada; caso 2, con presencia y oscuro, esperado encendida, obtenido encendida; "
     "caso 3, con presencia y claro, esperado apagada, obtenido encendida; caso 4, sin presencia y claro, esperado apagada, obtenido apagada.")
build(
    O6, 5, F,
    use="Aprenderé a comparar alternativas de un sistema automático por costo y consumo y a verificar su calidad con casos de prueba en papel.",
    prior=["Sé qué es la potencia en vatios.", "Sé calcular costos.", "Sé qué es un criterio de aceptación."],
    explain=[
        "Para comparar alternativas se miran varios datos a la vez: el costo de compra, el consumo de energía, las funciones y si cumplen los requerimientos. La energía se mide en vatios hora (Wh) o en kilovatios hora (kWh): la energía de un equipo es su potencia por las horas que funciona, y 1 kWh son 1000 Wh. El costo de la energía es los kWh por el precio de cada kWh. Una alternativa más cara de comprar puede costar menos en total si gasta menos energía.",
        "Para verificar la calidad se usan casos de prueba: situaciones con entradas definidas y un resultado esperado, que se compara con el resultado obtenido. Si todos coinciden, el sistema cumple. Si uno falla, se registra una no conformidad y no se acepta hasta corregirlo. No se descarta un requisito porque la alternativa sea barata.",
        f"Los precios y consumos son de ejemplo. Las pruebas en equipos reales las hace personal autorizado. {AVISO}",
    ],
    vocab=[("alternativa", "una de las opciones posibles para resolver un requerimiento"), ("kilovatio hora (kWh)", "energía de 1000 W usados durante 1 hora"), ("caso de prueba", "situación con entradas definidas y resultado esperado para compararlo con el obtenido"), ("resultado esperado", "lo que el sistema debería hacer según el diseño"), ("no conformidad", "resultado que no cumple lo esperado")],
    worked=[
        ("Energía de un equipo", "Una lámpara de ejemplo de 50 W funciona 4 horas. ¿Cuántos Wh usa?", ["Se multiplica la potencia por las horas.", "50 por 4 son 200."], "200 Wh"),
        ("Comparar una prueba", "Un caso de prueba de ejemplo esperaba «apagada» y se obtuvo «apagada». ¿Cumple?", ["Esperado y obtenido coinciden.", "El caso cumple."], "Sí, cumple"),
    ],
    mistakes=[("Elegir la alternativa más barata de comprar sin mirar la energía que gastará.", "El gasto de energía puede superar el ahorro inicial.", "Compara costo de compra y costo de energía en el período."),
              ("Aceptar un sistema cuando un caso de prueba falla porque «los otros salieron bien».", "Basta un caso fallido para que no cumpla.", "Registra la no conformidad y no aceptes hasta corregirlo.")],
    T=[
        ("abc", "En Electrónica: ¿qué es un caso de prueba?", "Una situación con entradas definidas y un resultado esperado para compararlo con el obtenido", "Una lista de precios de los sensores", "Un permiso de trabajo", "El caso de prueba permite verificar si el sistema actúa como se diseñó."),
        ("abc", "En Electrónica: ¿qué es un kilovatio hora (kWh)?", "La energía de 1000 W usados durante 1 hora", "La potencia máxima de una lámpara", "El precio de una lámpara", "El kWh mide energía, no potencia ni precio."),
        ("abc", "En Electrónica: ¿para qué se comparan alternativas de un sistema automático?", "Para decidir según costo, consumo, funciones y requerimientos", "Para elegir siempre la más cara", "Para elegir la que tenga más piezas", "Se comparan varios criterios y se decide cuál cumple mejor."),
        ("=", "{F} ¿Cuántos Wh usa en el mes la lámpara de la alternativa 1?", "100*10*30", "Se multiplican la potencia, las horas por día y los días.", " Wh"),
        ("=", "{F} ¿Cuántos pesos cuesta en el mes la energía de la alternativa 1?", "100*10*30*150//1000", "Se pasan los Wh a kWh y se multiplican por el precio del kWh.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta en el mes la energía de la alternativa 2?", "20*4*30*150//1000", "Se pasan los Wh a kWh y se multiplican por el precio del kWh.", " pesos"),
        ("=", "{F} ¿Cuántos pesos se ahorran por mes en energía con la alternativa 2?", "4500-360", "Se resta el costo mensual de energía de la 2 al de la 1.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta comprar la alternativa 2 que la 1?", "9000-3000", "Se resta el costo de compra de la 1 al de la 2.", " pesos"),
        ("abc", "{F} El caso 3 esperaba «apagada» y se obtuvo «encendida». ¿Qué corresponde?", "Registrar una no conformidad y no aceptar el sistema hasta corregirlo", "Aceptar el sistema, porque tres casos salieron bien", "Cambiar el resultado esperado a «encendida»", "Un caso fallido impide aceptar; el resultado esperado no se cambia para que coincida."),
        ("=", "{F} ¿Cuántos casos de prueba cumplieron lo esperado?", "4-1", "Se resta al total de casos el que falló.", " casos"),
        ("abc", "{F} Un jefe elige la alternativa 1 «porque es más barata de comprar». ¿Qué dato de la ficha cuestiona esa decisión?", "Su energía cuesta $4.500 al mes, frente a $360 de la alternativa 2", "Su lámpara es más antigua", "Su compra cuesta $3.000", "El costo mensual de energía es mucho mayor y compensa pronto la diferencia de compra."),
        ("=", "{F} Tras 2 meses de uso, ¿cuántos pesos quedan a favor de la alternativa 2 si se suma su ahorro de energía de los 2 meses y se resta lo que costó de más comprarla?", "2*4140-6000", "Se multiplican por 2 los pesos que ahorra por mes y se resta la diferencia de compra.", " pesos"),
        ("abc", "Una alternativa 3 de ejemplo cuesta $5.000, pero no apaga la luz cuando hay luz natural, que era un requerimiento. ¿Qué corresponde?", "Descartarla porque no cumple un requerimiento, aunque sea barata", "Elegirla por ser la más barata", "Elegirla y quitar el requerimiento", "Un requerimiento no cumplido deja fuera a la alternativa, sin importar el precio."),
    ],
    ctx=("abc", "El cliente de ejemplo prefiere la alternativa 1 por el costo de compra. ¿Qué entrega un técnico para ayudar a decidir con honestidad?", "Una tabla comparativa con compra, energía mensual y funciones de cada alternativa", "Solo el precio de compra, para cerrar la venta", "Una opinión sin números", "Una comparación con datos completos permite decidir sin presionar ni ocultar información."),
    sc=[
        ("En Electrónica: ¿cómo se calcula la energía de un equipo?", "Multiplicando su potencia por las horas que funciona", "La energía se obtiene como la potencia por el tiempo."),
        ("¿Qué pasa si un caso de prueba falla?", "Se registra una no conformidad y no se acepta hasta corregir", "El criterio debe cumplirse en todos los casos."),
        ("¿Qué se compara entre alternativas?", "Costo de compra, energía, funciones y requerimientos", "Una comparación completa evita decidir por un solo dato."),
    ],
    op=("Ficha de ejemplo: iluminar una bodega 8 horas al día durante 30 días. Alternativa A: lámpara de 80 W, $2.500, sin sensor. Alternativa B: lámpara de 20 W, $7.000, con sensor que la deja encendida 2 horas al día. Precio de la energía de ejemplo: $150 por kWh. Casos de prueba de B (resultados de ejemplo): sin presencia y oscuro, esperado apagada, obtenido apagada; con presencia y oscuro, esperado encendida, obtenido encendida. Escribe (a) el costo mensual de energía de A, (b) el de B, (c) cuánto se ahorra al mes con B, (d) si B cumple las pruebas.",
        "(a) 80 por 8 por 30 son 19.200 Wh, que a $150 por cada 1000 Wh son 2.880 pesos. (b) 20 por 2 por 30 son 1.200 Wh: 180 pesos. (c) 2.880 menos 180 son 2.700 pesos. (d) Sí, los dos casos coinciden con lo esperado.",
        ["calcula bien la energía de A", "calcula bien la energía de B", "calcula bien el ahorro", "verifica los casos de prueba"],
        ["hoja con los cálculos y la verificación"],
        ["no convertir de Wh a kWh", "comparar solo el precio de compra", "dar por buenos casos que fallaron"],
        "Pregunta: «¿qué harías si un caso de prueba no coincidiera?». Si no responde, pídele que relea qué ocurre con un caso fallido."),
    reinforce="Calcula en papel la energía en Wh de una lámpara de 40 W encendida 5 horas al día durante 30 días.",
    extend="Explica con un ejemplo por qué el precio de compra no basta para elegir entre dos alternativas.",
)
