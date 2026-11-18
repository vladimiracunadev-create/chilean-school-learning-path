"""Mecánica Industrial, mención Máquinas-Herramientas, 4.º medio: OAM-01 (máquinas-herramientas convencionales: planos, hojas de proceso y costos), OAM-02 (fresadora universal: conceptos, documentos y cálculo de tiempos) y OAM-03 (rectificado y taladrado: conceptos, documentos y verificación). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_memh_common import AVISO, EMER, build

O1 = "TP-MEMH-4-OAM-01"
O2 = "TP-MEMH-4-OAM-02"
O3 = "TP-MEMH-4-OAM-03"

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Taller Demo de Mecanizado» tiene 3 tornos (máquinas donde la pieza gira y la herramienta la desbasta), 2 fresadoras (máquinas donde la herramienta gira y la pieza avanza) y 2 taladros. "
     "Peligros anotados: partes giratorias, virutas calientes y filosas que salen proyectadas, ropa suelta o pelo largo que puede quedar atrapado, ruido, fluido de corte que salpica y piso resbaladizo, y piezas pesadas. Personas del turno: 12.")
build(
    O1, 1, F,
    use="Aprenderé qué es mecanizar, qué máquinas-herramientas hay en un taller, qué peligros tienen y qué reglas generales protegen a las personas.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé la jerarquía de controles.", "Sé qué es un EPP."],
    explain=[
        "Mecanizar es dar forma a una pieza retirando material con una herramienta de corte, y el material retirado se llama viruta. Las máquinas-herramientas son las máquinas que lo hacen: el torno hace girar la pieza mientras la herramienta la desbasta; la fresadora hace girar la herramienta mientras la pieza avanza; el taladro hace agujeros con una broca. Convencionales son las máquinas que maneja una persona con volantes y palancas, sin control numérico.",
        "Sus peligros principales son las partes giratorias, las virutas proyectadas o filosas, el atrapamiento de ropa, pelo o joyas, el ruido y el fluido de corte, que enfría y lubrica la herramienta. Se controlan con resguardos que no se retiran, paradas de emergencia, orden y limpieza, capacitación y, al final, EPP como protección ocular y calzado de seguridad. En las máquinas con partes giratorias no se usan guantes sueltos ni ropa suelta, y el pelo se mantiene recogido.",
        f"El uso de cada máquina exige instructor autorizado, y este cuaderno no enseña a operarlas. Las virutas y fluidos de corte son residuos que se gestionan según la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("mecanizar", "dar forma a una pieza retirando material con una herramienta de corte"), ("viruta", "material que se retira al mecanizar"), ("torno", "máquina donde la pieza gira y la herramienta la desbasta"), ("fresadora", "máquina donde la herramienta gira y la pieza avanza"), ("máquina-herramienta convencional", "máquina que maneja una persona sin control numérico"), ("fluido de corte", "líquido que enfría y lubrica la herramienta")],
    worked=[
        ("Nombrar la máquina", "En una máquina de ejemplo la pieza gira y una herramienta fija la desbasta. ¿Qué máquina es?", ["La pieza es la que gira.", "Eso ocurre en un torno."], "Un torno"),
        ("Clasificar un control", "Un taller de ejemplo instala una cubierta fija sobre la zona giratoria de una máquina. ¿Qué tipo de control es?", ["La cubierta es una barrera física.", "Es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Usar guantes sueltos o ropa suelta cerca de una parte giratoria.", "Pueden quedar atrapados y arrastrar la mano.", "Se usa ropa ajustada y no se usan guantes que puedan enredarse, según la norma del taller."),
              ("Creer que leer sobre una máquina habilita para usarla.", "Su uso exige instructor autorizado y norma vigente.", "Aprende el concepto y deja el uso a quien está autorizado.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es mecanizar?", "Dar forma a una pieza retirando material con una herramienta de corte", "Unir dos piezas fundiendo el metal", "Pintar una pieza para protegerla", "Mecanizar retira material; soldar une y pintar recubre."),
        ("abc", "En Máquinas-Herramientas: ¿qué es la viruta?", "El material que se retira al mecanizar", "La herramienta de corte", "El fluido que enfría la herramienta", "La viruta es el material desprendido."),
        ("abc", "En Máquinas-Herramientas: ¿en qué máquina gira la herramienta mientras la pieza avanza?", "En la fresadora", "En el torno", "En el taladro de banco", "En la fresadora gira la herramienta; en el torno gira la pieza."),
        ("abc", "{F} ¿Qué peligro de la lista se previene con ropa ajustada y pelo recogido?", "El atrapamiento en partes giratorias", "El ruido", "El piso resbaladizo", "La ropa suelta y el pelo largo pueden quedar atrapados."),
        ("abc", "{F} Un resguardo que cubre la zona giratoria de un torno es un control:", "De ingeniería", "Administrativo", "De EPP", "El resguardo es una barrera física."),
        ("abc", "{F} ¿Cuál de las máquinas de la ficha hace agujeros con una broca?", "El taladro", "El torno", "La fresadora", "El taladro hace agujeros; torno y fresadora desbastan."),
        ("=", "{F} ¿Cuántas máquinas-herramientas tiene el taller?", "3+2+2", "Se suman los tornos, las fresadoras y los taladros.", " máquinas"),
        ("=", "{F} Cada persona del turno recibe 2 pares de gafas de protección al año. ¿Cuántos pares se necesitan para el turno?", "12*2", "Se multiplican las personas por los pares de cada una.", " pares"),
        ("=", "{F} El taller retira 15 kg de viruta por máquina a la semana. ¿Cuántos kg de viruta generan las 7 máquinas?", "15*7", "Se multiplican los kg por máquina por las máquinas.", " kg"),
        ("abc", "{F} Un aprendiz dice: «uso guantes sueltos para proteger las manos en el torno». ¿Qué respuesta es correcta?", "Es falso: cerca de partes giratorias un guante suelto puede quedar atrapado, según las reglas generales de seguridad", "Es cierto, porque los guantes siempre protegen", "Es cierto, si son de cuero", "Un guante suelto cerca de partes giratorias es un riesgo de atrapamiento."),
        ("abc", "En una visita a un taller de ejemplo, la manga de una persona queda atrapada en una parte giratoria. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar soltar la manga con las manos", "Apagar la máquina tú mismo", "Intervenir sin formación puede causar otro accidente."),
        ("=", "{F} En una semana de 5 días se hacen 2 limpiezas del piso por día en el taller. ¿Cuántas limpiezas se hacen en la semana?", "5*2", "Se multiplican los días por las limpiezas de cada día.", " limpiezas"),
        ("abc", "En Máquinas-Herramientas: ¿qué se hace con las virutas y el fluido de corte usado?", "Se almacenan y gestionan como residuos según la norma vigente", "Se vierten al desagüe", "Se mezclan con la basura común", "En este caso, son residuos que requieren gestión."),
    ],
    ctx=("abc", "Un amigo de ejemplo te dice: «prueba el torno del taller del colegio cuando no haya nadie». ¿Qué respondes?", "Que no, porque usar un torno exige instructor autorizado y norma vigente, y que consultarás a un adulto responsable", "Que sí, si vas con cuidado", "Que sí, con gafas puestas", "Este cuaderno no habilita para operar máquinas."),
    sc=[
        ("En Máquinas-Herramientas: ¿qué hace un torno con la pieza?", "La hace girar mientras una herramienta la desbasta", "En el torno gira la pieza."),
        ("En Máquinas-Herramientas: ¿qué es el fluido de corte?", "Un líquido que enfría y lubrica la herramienta", "Reduce el calor y el roce en el corte."),
        ("En Máquinas-Herramientas: ¿quién puede usar una máquina-herramienta?", "Personal autorizado con instructor y norma vigente", "El uso exige autorización y formación."),
    ],
    op=("Ficha de ejemplo: el taller de otro liceo tiene 2 tornos y 1 fresadora. Peligros: partes giratorias, virutas filosas y ruido. Escribe (a) cuántas máquinas hay, (b) un control de ingeniería, (c) un control administrativo, (d) qué reglas de vestimenta se aplican cerca de las partes giratorias. No describas cómo se opera una máquina.",
        "(a) 2 + 1 = 3 máquinas. (b) Un resguardo sobre las partes giratorias. (c) Una señal y la regla de que solo personal autorizado opera las máquinas. (d) Ropa ajustada, pelo recogido y sin guantes sueltos ni joyas que puedan enredarse.",
        ["suma las máquinas", "propone un control de ingeniería", "propone un control administrativo", "nombra las reglas de vestimenta"],
        ["hoja con las cuatro respuestas"],
        ["proponer solo EPP", "olvidar la regla de la ropa", "describir cómo se opera una máquina"],
        "Pregunta: «¿qué puede quedar atrapado en una parte giratoria?». Si duda, pídele que relea los peligros."),
    reinforce="Escribe tres máquinas-herramientas con lo que gira en cada una y un peligro propio.",
    extend="Explica con un ejemplo por qué un resguardo no se retira aunque estorbe.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (plano y hoja de proceso descritos por escrito, de ejemplo e inventados). Plano P-10 «Eje escalonado», acero de ejemplo, escala 1:1, revisión A. Cotas: largo total 120 mm; tramo A de diámetro 30 mm y 50 mm de largo; tramo B de diámetro 24 mm y 70 mm de largo. "
     "Tolerancia general del plano: ±100 µm. Rugosidad pedida en el tramo A: Ra 1 (unidad de ejemplo; menor número, más liso). Hoja de proceso de ejemplo: Op10, cortar la barra a 125 mm, sierra, 6 min; Op20, desbastar los tramos, torno, 25 min; "
     "Op30, terminar los tramos, torno, 15 min; Op40, controlar medidas, puesto de calidad, 5 min. Barra de partida: diámetro 32 mm.")
build(
    O1, 2, F,
    use="Aprenderé a leer un plano de pieza y una hoja de proceso, qué son el material de partida y la sobremedida, y qué rol cumple cada persona del taller.",
    prior=["Sé leer un plano con cotas.", "Sé qué es una tolerancia.", "Sé sumar y restar enteros."],
    explain=[
        "El plano de una pieza trae sus cotas, su tolerancia, el material y el acabado pedido, o rugosidad. La hoja de proceso es el documento que lista, en orden, las operaciones para fabricar la pieza, con la máquina o puesto y el tiempo de cada una. El material de partida, o barra, es la pieza bruta con la que se empieza y siempre es más grande que la pieza final; la diferencia es la sobremedida, que se retira como viruta.",
        "El programador o el jefe de producción prepara la hoja de proceso, el operador autorizado ejecuta cada operación, el control de calidad mide y registra y el supervisor aprueba. El manual del fabricante de cada máquina indica sus límites; la hoja de proceso no los puede superar. Un error en el plano se consulta con quien lo emitió y no se corrige por cuenta propia.",
        f"Aquí solo se leen documentos. {EMER} {AVISO}",
    ],
    vocab=[("hoja de proceso", "documento que lista, en orden, las operaciones para fabricar una pieza"), ("material de partida", "pieza bruta con la que se empieza a mecanizar"), ("sobremedida", "diferencia entre el material de partida y la pieza final"), ("rugosidad Ra", "valor del acabado de una superficie: menor número, más liso"), ("operación", "etapa de la hoja de proceso hecha en un puesto"), ("control de calidad", "área que mide y registra que la pieza cumpla el plano")],
    worked=[
        ("Calcular la sobremedida", "Una barra de ejemplo de 40 mm de diámetro se mecaniza hasta 36 mm. ¿Cuántos mm de diámetro se retiran?", ["Se resta el diámetro final al inicial.", "40 menos 36 son 4."], "4 mm de diámetro"),
        ("Sumar tiempos", "Una hoja de proceso de ejemplo tiene operaciones de 8, 20 y 12 minutos. ¿Cuántos minutos suma?", ["Se suman los tres tiempos.", "8 más 20 más 12 son 40."], "40 minutos"),
    ],
    mistakes=[("Creer que la pieza se parte del mismo diámetro final.", "El material de partida es mayor que la pieza final.", "Calcula la sobremedida y considera la viruta."),
              ("Corregir una cota del plano por cuenta propia.", "Solo quien emitió el plano lo modifica.", "Registra la duda y consúltala.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es una hoja de proceso?", "Un documento que lista, en orden, las operaciones para fabricar una pieza", "Un plano con las cotas de la pieza", "Una lista de las máquinas del taller", "La hoja de proceso ordena las operaciones."),
        ("abc", "En Máquinas-Herramientas: ¿qué es la sobremedida?", "La diferencia entre el material de partida y la pieza final", "El error de medición de un instrumento", "El sobrante de piezas buenas", "La sobremedida es lo que se retira como viruta."),
        ("abc", "En Máquinas-Herramientas: ¿qué significa una rugosidad Ra menor en un plano?", "Una superficie más lisa", "Una superficie más áspera", "Una pieza más pequeña", "En este caso, A menor Ra, mejor acabado."),
        ("=", "{F} ¿Cuántos minutos suman las cuatro operaciones de la hoja de proceso?", "6+25+15+5", "Se suman los tiempos de las cuatro operaciones.", " minutos"),
        ("abc", "{F} ¿Cuál es el material de partida de la hoja de proceso?", "Una barra de 32 mm de diámetro", "Una barra de 24 mm de diámetro", "Una pieza terminada de 30 mm", "La ficha indica una barra de partida de 32 mm."),
        ("abc", "{F} ¿Qué operación hace el control de calidad?", "La operación Op40, controlar medidas", "La operación Op10, cortar la barra", "La operación Op20, desbastar", "Op40 se hace en el puesto de calidad."),
        ("=", "{F} ¿Cuántos mm de diámetro se retiran del tramo A, desde la barra hasta el diámetro final?", "32-30", "Se resta el diámetro final al de la barra.", " mm"),
        ("=", "{F} ¿Cuántos mm de largo sobran en la barra cortada respecto del largo total de la pieza?", "125-120", "Se resta el largo de la pieza al de la barra cortada.", " mm"),
        ("=", "{F} ¿Cuántos mm suman los largos de los tramos A y B del plano?", "50+70", "Se suman los largos de los dos tramos.", " mm"),
        ("abc", "{F} Un compañero dice: «la barra es de 32 mm, así que la pieza mide 32 mm». ¿Qué respuesta es correcta?", "Es falso: la barra es el material de partida y el plano pide diámetros de 30 y 24 mm", "Es cierto, porque la barra define la pieza", "Es cierto, si no se desbasta", "El plano manda sobre la barra de partida."),
        ("abc", "{F} Un operario sugiere corregir la cota del tramo B de 70 a 72 mm «porque calza mejor». ¿Qué respuesta es correcta?", "No corresponde: el cambio lo decide quien emitió el plano y se registra la duda", "Corresponde, porque calza mejor", "Corresponde, si lo hace de noche", "Solo quien emitió el plano lo modifica."),
        ("=", "{F} Se fabrican 8 piezas y cada una necesita las 4 operaciones. ¿Cuántos minutos de torno hay en total con Op20 y Op30?", "8*(25+15)", "Se suman los tiempos de torno de una pieza y se multiplican por las piezas.", " minutos"),
        ("En una hoja de ejemplo, el control de calidad está al inicio de las operaciones en vez de al final. ¿Es razonable?", "No, porque debe controlarse la pieza ya mecanizada", "El control mide el resultado y por eso va después de mecanizar."),
    ],
    ctx=("abc", "El jefe de ejemplo dice: «saltemos el control de calidad para ganar tiempo». ¿Qué propones?", "Mantener el control, porque verifica que la pieza cumpla el plano antes de entregarla", "Saltarlo si hay apuro", "Hacerlo solo en la primera pieza del mes", "El control evita entregar piezas fuera de plano."),
    sc=[
        ("En Máquinas-Herramientas: ¿qué es el material de partida?", "La pieza bruta con la que se empieza a mecanizar", "Siempre es mayor que la pieza final."),
        ("En Máquinas-Herramientas: ¿qué lista la hoja de proceso?", "Las operaciones en orden con su puesto y tiempo", "Organiza la fabricación de la pieza."),
        ("En Máquinas-Herramientas: ¿quién modifica una cota del plano?", "Quien emitió el plano", "Los cambios de diseño no se hacen por cuenta propia."),
    ],
    op=("Ficha de ejemplo: plano P-12 «Pasador», diámetro 20 mm y largo 60 mm. Barra de partida: 22 mm de diámetro, cortada a 64 mm. Hoja de proceso: Op10, corte, 4 min; Op20, torno, 18 min; Op30, control, 3 min. Escribe (a) cuántos mm de diámetro se retiran, (b) cuántos mm de largo sobran, (c) cuántos minutos suma la hoja, (d) qué operación controla la calidad.",
        "(a) 22 − 20 = 2 mm. (b) 64 − 60 = 4 mm. (c) 4 + 18 + 3 = 25 minutos. (d) Op30.",
        ["calcula la sobremedida en diámetro", "calcula el sobrante de largo", "suma los tiempos", "identifica el control"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "olvidar una operación", "confundir el control"],
        "Pregunta: «¿el diámetro final es el de la barra o el del plano?». Si duda, pídele que relea la sobremedida."),
    reinforce="Inventa una barra de partida y una pieza final y calcula la sobremedida en diámetro y en largo.",
    extend="Explica con un ejemplo por qué el control de calidad va al final de una hoja de proceso.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (hoja de proceso de ejemplo con errores, inventada). Pieza «Buje»: diámetro exterior 40 mm, diámetro interior 20 mm, largo 50 mm, acero de ejemplo. Barra de partida en la hoja: diámetro 38 mm, largo 52 mm. "
     "Operaciones: Op10, cortar la barra, 5 min; Op20, desbastar el exterior, 20 min; Op30, hacer el agujero interior, 12 min; Op40, controlar, 4 min; suma anotada en la hoja: 45 min. "
     "Herramientas anotadas: una broca de 24 mm para el agujero interior. Máquina anotada para Op20: taladro de banco. Rotulado de la hoja: revisión A, pero el plano vigente es revisión B.")
build(
    O1, 3, F,
    use="Aprenderé a revisar una hoja de proceso en papel, detectando datos inconsistentes con el plano, errores de suma y de máquina, y decidiendo cómo informarlos.",
    prior=["Sé qué es una hoja de proceso.", "Sé qué es la sobremedida.", "Sé sumar tiempos."],
    explain=[
        "Revisar una hoja de proceso es compararla con el plano vigente y con la lógica del oficio. Se comprueba que el material de partida sea mayor que la pieza final, que los tiempos sumen lo anotado, que cada operación use la máquina que corresponde, que las herramientas anotadas calcen con las medidas del plano y que la revisión de la hoja coincida con la del plano.",
        "Cuando se encuentran errores, no se corrigen por cuenta propia: se registran con el dato y el motivo, y se informan a quien emitió la hoja, que la corrige y emite una nueva revisión. Un error no detectado puede producir piezas defectuosas, chatarra y accidentes. La revisión es solo documental.",
        f"El análisis es de papel. {EMER} {AVISO}",
    ],
    vocab=[("revisión documental", "comparación de una hoja de proceso con el plano y la lógica del oficio"), ("incoherencia", "dato que contradice a otro o al plano"), ("chatarra", "pieza defectuosa que no se puede recuperar"), ("emitir una revisión", "publicar una nueva versión de un documento corregido"), ("máquina que corresponde", "máquina capaz de hacer la operación pedida")],
    worked=[
        ("Barra más chica que la pieza", "Una hoja de ejemplo parte de una barra de 30 mm para una pieza de 34 mm de diámetro. ¿Es coherente?", ["La barra debe ser mayor que la pieza.", "30 es menor que 34."], "No es coherente"),
        ("Revisar la suma", "Una hoja de ejemplo anota operaciones de 10, 12 y 8 minutos y una suma de 32. ¿La suma es correcta?", ["10 más 12 más 8 son 30.", "La hoja anotó 32."], "No, la suma correcta es 30"),
    ],
    mistakes=[("Corregir la hoja con lápiz y seguir trabajando.", "Solo quien emitió la hoja puede cambiarla.", "Registra el error e infórmalo."),
              ("Revisar solo los números y no la lógica del proceso.", "Una operación asignada a una máquina que no corresponde también es un error.", "Revisa números, máquinas y herramientas.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es una incoherencia en una hoja de proceso?", "Un dato que contradice a otro o al plano", "Una operación con tiempo largo", "Una pieza ya terminada", "Una incoherencia es una contradicción a corregir."),
        ("abc", "En Máquinas-Herramientas: ¿qué es la chatarra?", "Una pieza defectuosa que no se puede recuperar", "La viruta que se retira", "La barra de partida", "La chatarra es una pieza perdida."),
        ("abc", "En Máquinas-Herramientas: ¿qué se hace al encontrar un error en una hoja de proceso?", "Se registra e informa a quien la emitió", "Se corrige con lápiz y se sigue", "Se ignora si es pequeño", "Quien emitió el documento lo corrige y emite una nueva revisión."),
        ("=", "{F} ¿Cuántos minutos suman realmente las cuatro operaciones?", "5+20+12+4", "Se suman los tiempos de las cuatro operaciones.", " minutos"),
        ("abc", "{F} ¿Es correcta la suma de 45 min anotada en la hoja?", "No, porque las operaciones suman 41", "Sí, porque 45 es la suma", "No se puede saber", "5 más 20 más 12 más 4 son 41."),
        ("abc", "{F} ¿Qué incoherencia hay entre la barra de partida y la pieza?", "La barra de 38 mm es menor que el diámetro exterior de 40 mm", "La barra es mayor que la pieza", "La barra mide lo mismo que la pieza", "El material de partida debe ser mayor que la pieza final."),
        ("abc", "{F} ¿Qué incoherencia hay en la máquina anotada para la operación Op20?", "El desbaste exterior no corresponde a un taladro de banco, que hace agujeros", "Un taladro de banco es la máquina ideal para desbastar", "La máquina se anotó dos veces", "El desbaste exterior de una pieza redonda se hace en un torno, no en un taladro."),
        ("abc", "{F} ¿Qué incoherencia hay con la herramienta del agujero interior?", "La broca de 24 mm no calza con un agujero de 20 mm", "La broca de 24 mm es la correcta para 20 mm", "No hay agujero interior", "Una broca mayor que el agujero pedido no lo deja en 20 mm."),
        ("=", "{F} ¿Cuántos mm de largo sobran entre la barra de la hoja y el largo de la pieza?", "52-50", "Se resta el largo de la pieza al de la barra.", " mm"),
        ("abc", "{F} La hoja es revisión A y el plano vigente es revisión B. ¿Qué corresponde?", "Informarlo y pedir la hoja actualizada antes de trabajar", "Usar la hoja porque ya está lista", "Cambiar la revisión de la hoja a B con lápiz", "Una hoja de otra revisión puede tener datos desactualizados."),
        ("abc", "{F} Un operario dice: «el taladro de banco está libre, desbastemos ahí». ¿Qué respuesta es correcta?", "No corresponde: la operación debe hacerse en una máquina capaz, y la hoja debe corregirla quien la emitió", "Corresponde, si el taladro está libre", "Corresponde, si lleva protección", "Una máquina inadecuada es un riesgo para la pieza y la persona."),
        ("=", "{F} Si corrigen las incoherencias y la suma pasa a 41 minutos, ¿cuántos minutos suman 6 piezas?", "6*41", "Se multiplican las piezas por los minutos de cada una.", " minutos"),
        ("En una hoja de ejemplo se anota un tiempo de 0 minutos para una operación. ¿Qué conviene hacer?", "Informarlo, porque ninguna operación toma 0 minutos", "Un tiempo de 0 minutos es incoherente con el proceso."),
    ],
    ctx=("abc", "Un aprendiz de ejemplo dice: «la hoja tiene errores, pero total, yo sé cómo se hace». ¿Qué propones?", "Registrar los errores y pedir la hoja corregida a quien la emitió antes de trabajar", "Trabajar según su memoria", "Corregir la hoja a mano", "Los documentos se corrigen con quien los emitió."),
    sc=[
        ("En Máquinas-Herramientas: ¿cuál es mayor, la barra de partida o la pieza final?", "La barra de partida", "La diferencia es la sobremedida que se retira."),
        ("En Máquinas-Herramientas: ¿qué hace quien emite una hoja con errores?", "Emite una nueva revisión corregida", "En este caso, así queda registro del cambio."),
        ("En Máquinas-Herramientas: ¿qué es una máquina que corresponde?", "La capaz de hacer la operación pedida", "Cada operación exige una máquina adecuada."),
    ],
    op=("Ficha de ejemplo: hoja para el «Casquillo»: diámetro exterior 30 mm, largo 40 mm. Barra de partida: 28 mm de diámetro. Operaciones: Op10 corte, 3 min; Op20 desbaste exterior, 15 min, en una fresadora; Op30 control, 4 min; suma anotada: 25 min. Escribe (a) la incoherencia de la barra, (b) la suma real, (c) si la máquina de Op20 es adecuada, (d) a quién informas los errores.",
        "(a) La barra de 28 mm es menor que el diámetro exterior de 30 mm. (b) 3 + 15 + 4 = 22 minutos. (c) No es lo habitual: el desbaste exterior de una pieza redonda corresponde a un torno. (d) A quien emitió la hoja, para que emita una revisión corregida.",
        ["detecta la barra chica", "calcula la suma real", "evalúa la máquina", "indica a quién informa"],
        ["hoja con las cuatro respuestas"],
        ["no detectar la barra menor", "calcular mal la suma", "corregir por cuenta propia"],
        "Pregunta: «¿qué debe ser mayor, la barra o la pieza?». Si duda, pídele que relea la definición de sobremedida."),
    reinforce="Escribe tres cosas que debes comparar al revisar una hoja de proceso con su plano.",
    extend="Explica con un ejemplo por qué un error no detectado en una hoja puede terminar en chatarra.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (costeo de una pieza de ejemplo, inventado). Lote de 40 ejes. Cada eje se hace con una barra cortada: costo del material por eje, $2.500. Tiempos por eje: torno, 20 min; fresadora, 10 min; control, 3 min. "
     "Costo de ejemplo de una hora: torno $12.000; fresadora $15.000; control $6.000. Preparación del lote en el torno: 60 min (una vez por lote). Chatarra de ejemplo: 4 ejes del lote de 40 salen defectuosos y se pierden. Turno de 8 horas = 480 min.")
build(
    O1, 4, F,
    use="Aprenderé a calcular el costo de una pieza y de un lote a partir de tiempos y costos por hora, a considerar la preparación y la chatarra y a calcular cuántas piezas caben en un turno.",
    prior=["Sé multiplicar y dividir enteros.", "Sé pasar minutos a horas.", "Sé qué es un lote."],
    explain=[
        "El costo de una pieza suma el material y el costo de cada operación. El costo de una operación se calcula multiplicando su tiempo en minutos por el costo por minuto, que es el costo por hora dividido por 60. La preparación del lote es el tiempo que se gasta una vez por lote antes de producir, por lo que su costo se reparte entre todas las piezas. La chatarra es una pérdida: el costo de las piezas defectuosas se reparte entre las buenas.",
        "Las piezas por turno se calculan dividiendo los minutos disponibles, restada la preparación, entre el tiempo de la operación más lenta. Con enteros, se redondea hacia abajo, porque no se cuentan piezas incompletas. Los valores de este cuaderno son de ejemplo.",
        f"El cálculo es de papel; no se opera ninguna máquina. {EMER} {AVISO}",
    ],
    vocab=[("costo por minuto", "costo por hora dividido por 60"), ("preparación del lote", "tiempo que se gasta una vez antes de producir un lote"), ("chatarra", "piezas defectuosas que se pierden"), ("piezas buenas", "piezas que cumplen el plano"), ("operación más lenta", "la que más tiempo toma por pieza")],
    worked=[
        ("Costo de una operación", "Una operación de ejemplo toma 30 minutos y la hora cuesta $6.000. ¿Cuánto cuesta la operación?", ["30 minutos son media hora.", "La mitad de 6.000 son 3.000."], "$3.000"),
        ("Piezas buenas", "Un lote de ejemplo es de 50 piezas y 5 salen defectuosas. ¿Cuántas piezas buenas hay?", ["Se restan las defectuosas al lote.", "50 menos 5 son 45."], "45 piezas buenas"),
    ],
    mistakes=[("Multiplicar los minutos por el costo de la hora sin dividir por 60.", "El costo de la hora corresponde a 60 minutos.", "Divide el costo por hora entre 60 antes de multiplicar."),
              ("Olvidar la chatarra al calcular el costo por pieza buena.", "Las piezas perdidas también costaron.", "Reparte el costo total entre las piezas buenas.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿cómo se calcula el costo por minuto de una máquina?", "Dividiendo el costo por hora entre 60", "Multiplicando el costo por hora por 60", "Sumando 60 al costo por hora", "En este caso, una hora tiene 60 minutos."),
        ("abc", "En Máquinas-Herramientas: ¿qué es la preparación del lote?", "El tiempo que se gasta una vez antes de producir un lote", "El tiempo de limpieza al final del día", "El tiempo de control de cada pieza", "La preparación se hace una vez y se reparte en el lote."),
        ("abc", "En Máquinas-Herramientas: ¿cómo se reparte el costo de la chatarra?", "Entre las piezas buenas del lote", "Solo entre las piezas defectuosas", "No se considera en el costo", "Las piezas buenas deben cubrir lo que costó el lote."),
        ("=", "{F} ¿Cuántos minutos de máquina y control necesita un eje, sumando torno, fresadora y control?", "20+10+3", "Se suman los tiempos de las tres operaciones.", " minutos"),
        ("=", "{F} ¿Cuánto cuesta el torno por eje, a $12.000 la hora y con 20 minutos?", "20*12000//60", "Se multiplican los minutos por el costo de la hora y se dividen por 60.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto cuesta la fresadora por eje, a $15.000 la hora y con 10 minutos?", "10*15000//60", "Se multiplican los minutos por el costo de la hora y se dividen por 60.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto cuesta el control por eje, a $6.000 la hora y con 3 minutos?", "3*6000//60", "Se multiplican los minutos por el costo de la hora y se dividen por 60.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto cuesta un eje entre material y operaciones? Material $2.500; torno $4.000; fresadora $2.500; control $300.", "2500+4000+2500+300", "Se suman el material y los tres costos de operación.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántos ejes buenos tiene el lote de 40 si 4 salen defectuosos?", "40-4", "Se restan los defectuosos al lote.", " ejes"),
        ("=", "{F} ¿Cuánto cuesta preparar el torno para el lote, con 60 minutos a $12.000 la hora?", "60*12000//60", "Se multiplican los minutos por el costo de la hora y se dividen por 60.", " pesos de ejemplo"),
        ("abc", "{F} Un jefe dice: «el costo del eje es solo el material y el torno». ¿Qué respuesta es correcta?", "Es incompleto: faltan la fresadora, el control, la preparación y la chatarra", "Es correcto, porque el torno es lo principal", "Es correcto, si hay pocos ejes", "El costo suma todas las operaciones y pérdidas."),
        ("=", "{F} Con el torno de 20 minutos por eje y 480 minutos de turno, descontando 60 de preparación, ¿cuántos ejes completos se pueden pasar por el torno en un turno?", "(480-60)//20", "Se restan los minutos de preparación y se divide por el tiempo por eje.", " ejes"),
        ("Si el lote de 40 ejes cuesta $720.000 en total y solo 36 salen buenos, ¿cuánto cuesta cada eje bueno?", "$20.000", "720.000 dividido en 36 es 20.000."),
    ],
    ctx=("abc", "Un cliente de ejemplo pide el precio de un eje y el jefe solo suma el material y el tiempo del torno. ¿Qué propones?", "Calcular también las demás operaciones, la preparación y la chatarra antes de dar el precio", "Dar el precio sin más", "Cobrar solo el material", "El precio debe cubrir todo el costo real."),
    sc=[
        ("En Máquinas-Herramientas: ¿cuánto cuesta una operación de 45 minutos a $8.000 la hora?", "$6.000", "45 minutos son tres cuartos de hora, y tres cuartos de 8.000 son 6.000."),
        ("En Máquinas-Herramientas: ¿qué se hace con los minutos de preparación al calcular las piezas del turno?", "Se restan de los minutos disponibles", "La preparación consume parte del turno."),
        ("En Máquinas-Herramientas: ¿cómo se redondean las piezas por turno?", "Hacia abajo", "En este caso, No se cuentan piezas incompletas."),
    ],
    op=("Ficha de ejemplo: lote de 20 bujes. Material por buje: $1.000. Torno: 12 minutos por buje a $12.000 la hora. Control: 3 minutos por buje a $6.000 la hora. Preparación: 30 minutos de torno a $12.000 la hora. Se pierden 2 bujes. Escribe (a) el costo de torno por buje, (b) el costo del lote en material, torno y control, sin la preparación, (c) el costo de la preparación, (d) cuántos bujes buenos hay.",
        "(a) 12 × 12.000 ÷ 60 = 2.400 pesos de ejemplo. (b) Material 20 × 1.000 = 20.000; torno 20 × 2.400 = 48.000; control 20 × 300 = 6.000; total 74.000. (c) 30 × 12.000 ÷ 60 = 6.000 pesos de ejemplo. (d) 20 − 2 = 18 bujes.",
        ["calcula el torno por buje", "calcula el costo del lote", "calcula la preparación", "calcula las piezas buenas"],
        ["hoja con las cuatro respuestas"],
        ["no dividir por 60", "olvidar el material", "olvidar la chatarra"],
        "Pregunta: «¿el costo de la hora corresponde a cuántos minutos?». Si duda, pídele que relea la definición de costo por minuto."),
    reinforce="Inventa una operación con minutos y costo por hora y calcula su costo.",
    extend="Explica con un ejemplo por qué la preparación del lote se reparte entre todas las piezas.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). En el taller de ejemplo hay una fresadora universal ficticia: máquina con una mesa que se mueve en tres direcciones (X, Y y Z) y un husillo (eje que hace girar la herramienta). La herramienta es una fresa, con varios filos o dientes. "
     "Peligros anotados: fresa giratoria con filos, virutas proyectadas, atrapamiento por ropa o pelo, ruido, fluido de corte, piezas pesadas y cortes al tocar una fresa o virutas. Elementos de seguridad de la máquina: resguardo de la fresa, parada de emergencia y tablero.")
build(
    O2, 1, F,
    use="Aprenderé qué es una fresadora universal, qué movimientos y partes tiene, qué peligros presenta y qué reglas generales la rodean.",
    prior=["Sé qué es mecanizar.", "Sé qué es un resguardo.", "Sé qué es una viruta."],
    explain=[
        "La fresadora universal es una máquina donde la herramienta, llamada fresa, gira con varios filos y la pieza, sujeta a una mesa, avanza contra ella; así se retira material en forma de virutas. La mesa se mueve en tres direcciones: X (de lado a lado), Y (hacia adelante y atrás) y Z (arriba y abajo). El husillo es el eje que hace girar la fresa. La palabra «universal» indica que la mesa también puede girar para trabajar en ángulos.",
        "Los peligros más graves son la fresa giratoria con filos, la proyección de virutas, el atrapamiento de ropa o pelo, el ruido y los cortes con fresas o virutas. Los controles incluyen el resguardo de la fresa, la parada de emergencia, el fluido de corte para reducir calor y orden en el piso, además de EPP como protección ocular y calzado de seguridad. Nunca se retira un resguardo ni se toca una fresa que gira o que acaba de detenerse.",
        f"La fresadora la opera solo personal autorizado con instructor. {EMER} {AVISO}",
    ],
    vocab=[("fresadora universal", "máquina con una fresa giratoria y una mesa que se mueve en tres direcciones"), ("fresa", "herramienta con varios filos que gira y retira material"), ("husillo", "eje que hace girar la herramienta"), ("eje X, Y y Z", "las tres direcciones en que se mueve la mesa"), ("resguardo", "barrera física que cubre una parte peligrosa"), ("parada de emergencia", "botón que detiene la máquina en una situación de peligro")],
    worked=[
        ("Identificar la parte", "Una parte de ejemplo hace girar la herramienta de una fresadora. ¿Cómo se llama?", ["Es el eje de la herramienta.", "Se llama husillo."], "El husillo"),
        ("Direcciones de la mesa", "La mesa de ejemplo sube y baja. ¿En qué eje se mueve?", ["El eje Z es vertical.", "Subir y bajar es el eje Z."], "En el eje Z"),
    ],
    mistakes=[("Tocar una fresa que acaba de detenerse porque «ya no gira».", "Puede seguir girando por inercia y tiene filos.", "No se toca una fresa; solo personal autorizado, con procedimiento."),
              ("Creer que leer sobre la fresadora habilita para usarla.", "Su uso exige instructor autorizado.", "Aprende el concepto y deja el uso a quien corresponde.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es el husillo de una fresadora?", "El eje que hace girar la herramienta", "La mesa que sostiene la pieza", "El botón de parada", "En este caso, El husillo gira la herramienta."),
        ("abc", "En Máquinas-Herramientas: ¿qué es una fresa?", "Una herramienta con varios filos que gira y retira material", "Una pieza que se vende terminada", "Un instrumento que mide el largo", "La fresa corta con varios filos."),
        ("abc", "En Máquinas-Herramientas: ¿en cuántas direcciones se mueve la mesa de una fresadora universal?", "En tres: X, Y y Z", "En una sola", "En dos solamente", "La mesa se mueve en los ejes X, Y y Z."),
        ("abc", "{F} ¿Qué elemento de seguridad de la máquina de la ficha cubre la fresa?", "El resguardo de la fresa", "La parada de emergencia", "El tablero", "El resguardo es la barrera sobre la fresa."),
        ("abc", "{F} ¿Qué peligro de la lista se relaciona con tocar una fresa?", "Los cortes por sus filos", "El ruido", "El fluido de corte", "En este caso, una fresa tiene varios filos."),
        ("abc", "{F} ¿Qué hace la parada de emergencia?", "Detiene la máquina en una situación de peligro", "Aumenta la velocidad", "Cambia la herramienta", "Es un control para detener rápido la máquina."),
        ("=", "{F} El taller tiene 2 fresadoras como la de la ficha y cada una requiere 1 persona operadora y 1 persona de apoyo en la prueba. ¿Cuántas personas se necesitan?", "2*(1+1)", "Se suman operadora y apoyo y se multiplican por las fresadoras.", " personas"),
        ("=", "{F} Cada fresadora genera 8 kg de viruta por día. ¿Cuántos kg generan 2 fresadoras en 5 días?", "2*8*5", "Se multiplican fresadoras, kg por día y días.", " kg"),
        ("abc", "{F} Una cubierta fija de protección sobre la fresa es un control:", "De ingeniería", "Administrativo", "De EPP", "La cubierta es una barrera física."),
        ("abc", "{F} Un aprendiz dice: «la fresa ya está parada, la toco para limpiarla». ¿Qué respuesta es correcta?", "Es falso: una fresa tiene filos y puede girar por inercia; solo personal autorizado interviene", "Es cierto, porque está parada", "Es cierto, si usa guantes", "Una fresa recién detenida sigue siendo peligrosa."),
        ("abc", "En una visita a un taller de ejemplo, una persona recibe un corte profundo con una fresa. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar detener el sangrado tú mismo con las manos", "Mover la máquina para sacar la pieza", "Los primeros auxilios y la atención los hacen quienes tienen formación."),
        ("=", "{F} Cada fresadora gasta 3 litros de fluido de corte por semana. ¿Cuántos litros gastan 2 fresadoras en 4 semanas?", "2*3*4", "Se multiplican fresadoras, litros y semanas.", " litros"),
        ("abc", "En Máquinas-Herramientas: ¿qué se hace con el fluido de corte usado?", "Se almacena y gestiona como residuo según la norma vigente", "Se vierte al desagüe", "Se guarda sin rotular", "Es un residuo que requiere gestión."),
    ],
    ctx=("abc", "Un compañero de ejemplo dice: «hagamos una ranura en una pieza con la fresadora, hay un video que lo explica». ¿Qué respondes?", "Que usar una fresadora exige instructor autorizado y norma vigente, y que consultarás a un adulto responsable", "Que sí, si seguimos el video", "Que sí, con gafas puestas", "Un video no habilita para operar una máquina."),
    sc=[
        ("En Máquinas-Herramientas: ¿qué eje es el vertical de la mesa?", "El eje Z", "En este caso, Z es arriba y abajo."),
        ("En Máquinas-Herramientas: ¿qué es la parada de emergencia?", "Un botón que detiene la máquina ante un peligro", "Es un control para actuar rápido."),
        ("En Máquinas-Herramientas: ¿puede un estudiante usar la fresadora solo?", "No, solo personal autorizado con instructor", "En este caso, El uso exige autorización."),
    ],
    op=("Ficha de ejemplo: un taller tiene una fresadora ficticia con resguardo y parada de emergencia. Peligros: fresa con filos, virutas y atrapamiento. Escribe (a) qué parte hace girar la fresa, (b) un control de ingeniería, (c) un control administrativo, (d) qué harías si una fresa acaba de detenerse. No describas cómo se opera.",
        "(a) El husillo. (b) El resguardo de la fresa. (c) Una señal y la regla de que solo personal autorizado opera la máquina. (d) No tocarla: puede seguir girando por inercia y tiene filos; solo interviene personal autorizado.",
        ["nombra el husillo", "propone un control de ingeniería", "propone un control administrativo", "indica no tocar la fresa"],
        ["hoja con las cuatro respuestas"],
        ["decir que parada es sin peligro", "proponer solo EPP", "describir cómo se opera"],
        "Pregunta: «¿qué parte hace girar la fresa?». Si duda, pídele que relea el vocabulario."),
    reinforce="Escribe los tres ejes de la mesa de una fresadora y un movimiento de cada uno.",
    extend="Explica con un ejemplo por qué una fresa que acaba de detenerse sigue siendo peligrosa.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 2 (plano y tabla de ejemplo, descritos por escrito, inventados). Pieza «Placa con ranura»: largo 100 mm, ancho 60 mm, espesor 20 mm. Ranura (canal) de 12 mm de ancho, 8 mm de profundidad y 100 mm de largo. Chaflán de 2 mm en las esquinas. "
     "Fresas disponibles según la ficha de herramientas: fresa A, diámetro 8 mm; fresa B, diámetro 12 mm; fresa C, diámetro 16 mm. Tabla de parámetros DE EJEMPLO (no sirve para trabajar): velocidad de giro 500 vueltas por minuto (rpm); número de dientes de la fresa B, 4; avance por diente de ejemplo, 50 µm. "
     "Fórmula de ejemplo: avance de la mesa en mm por minuto = rpm × dientes × avance por diente en µm ÷ 1.000.")
build(
    O2, 2, F,
    use="Aprenderé a leer un plano con ranura y chaflán, a elegir una fresa según una cota y a calcular un avance con una fórmula de ejemplo.",
    prior=["Sé leer cotas.", "Sé multiplicar y dividir enteros.", "Sé qué es una fresa."],
    explain=[
        "Un plano de una pieza fresada muestra elementos como la ranura, un canal con ancho, profundidad y largo, y el chaflán, una arista cortada en ángulo. La ficha de herramientas lista las fresas disponibles con su diámetro. Una ranura de cierto ancho se hace con una fresa de ese mismo diámetro o menor; una fresa mayor que el ancho de la ranura no cabe.",
        "Las condiciones de corte, como la velocidad de giro, el número de dientes y el avance por diente, se leen en tablas del fabricante. Con ellas se calcula el avance de la mesa: las vueltas por minuto por los dientes por el avance por diente. Los valores de esta ficha son de ejemplo y no sirven para trabajar: los reales dependen de la herramienta, el material y el manual del fabricante.",
        f"Aquí solo se leen documentos y se calcula en papel. {EMER} {AVISO}",
    ],
    vocab=[("ranura", "canal con ancho, profundidad y largo"), ("chaflán", "arista cortada en ángulo"), ("ficha de herramientas", "lista de las herramientas disponibles con sus medidas"), ("vueltas por minuto (rpm)", "cuántas vueltas da la herramienta en un minuto"), ("avance por diente", "cuánto material retira cada diente en cada vuelta"), ("avance de la mesa", "distancia que avanza la mesa por minuto")],
    worked=[
        ("Elegir la fresa", "Una ranura de ejemplo tiene 10 mm de ancho y hay fresas de 6, 10 y 14 mm. ¿Cuáles caben?", ["La fresa no puede ser mayor que el ancho de la ranura.", "Caben las de 6 y 10 mm."], "Las de 6 y 10 mm"),
        ("Calcular el avance", "Una fresa de ejemplo gira a 200 rpm, tiene 2 dientes y avanza 100 µm por diente. ¿Cuántos mm por minuto avanza la mesa?", ["200 por 2 por 100 son 40.000.", "40.000 dividido en 1.000 son 40."], "40 mm por minuto"),
    ],
    mistakes=[("Elegir una fresa más ancha que la ranura.", "No cabe en la ranura.", "Elige un diámetro igual o menor que el ancho."),
              ("Usar la fórmula de ejemplo en un trabajo real.", "Los valores reales los fija el fabricante y el manual.", "Úsala solo para calcular en papel.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es una ranura?", "Un canal con ancho, profundidad y largo", "Una arista cortada en ángulo", "Un agujero redondo", "La ranura es un canal; el chaflán es una arista inclinada."),
        ("abc", "En Máquinas-Herramientas: ¿qué es un chaflán?", "Una arista cortada en ángulo", "Un canal profundo", "Un agujero ciego", "El chaflán corta la arista en ángulo."),
        ("abc", "En Máquinas-Herramientas: ¿qué indica el avance por diente?", "Cuánto material retira cada diente en cada vuelta", "Cuántos dientes tiene la fresa", "La velocidad de giro", "El avance por diente es parte de las condiciones de corte."),
        ("abc", "{F} ¿Qué fresas de la ficha caben en la ranura de 12 mm de ancho?", "La A (8 mm) y la B (12 mm)", "Solo la C (16 mm)", "La B y la C", "La fresa no puede ser mayor que el ancho de la ranura."),
        ("=", "{F} ¿Cuántos mm de profundidad más tiene el espesor de la pieza que la ranura?", "20-8", "Se resta la profundidad de la ranura al espesor.", " mm"),
        ("=", "{F} ¿Cuántos mm cuadrados tiene la cara superior de la pieza, con largo por ancho?", "100*60", "Se multiplican el largo por el ancho.", " mm cuadrados"),
        ("=", "{F} Con la fórmula de ejemplo, ¿cuántos mm por minuto avanza la mesa con la fresa B?", "500*4*50//1000", "Se multiplican rpm, dientes y avance por diente y se divide por 1.000.", " mm por minuto"),
        ("=", "{F} ¿Cuántos minutos tarda en recorrer la mesa los 100 mm de la ranura, con el avance de ejemplo de 100 mm por minuto?", "100//100", "Se divide el largo entre el avance por minuto.", " minuto"),
        ("=", "{F} Si la ranura midiera 300 mm de largo en lugar de 100 mm, ¿cuántos minutos tardaría la mesa en recorrerla, con el avance de ejemplo de 100 mm por minuto?", "300//100", "Se divide la distancia entre el avance de la mesa por minuto.", " minutos"),
        ("abc", "{F} Un aprendiz propone usar la fresa C de 16 mm para la ranura de 12 mm. ¿Qué respuesta es correcta?", "No corresponde: la fresa C es más ancha que la ranura y no cabe", "Corresponde, porque es la más resistente", "Corresponde, si baja la velocidad", "Una fresa mayor que el ancho no puede hacer esa ranura."),
        ("abc", "{F} Un operario dice: «uso los valores de la tabla de este cuaderno para el trabajo real». ¿Qué respuesta es correcta?", "Es falso: son valores de ejemplo y los reales los fija el fabricante en su manual", "Es cierto, porque la tabla es oficial", "Es cierto, si usa la fresa correcta", "El cuaderno no entrega parámetros reales."),
        ("=", "{F} Se fabrican 12 placas iguales. ¿Cuántos mm de ranura se hacen en total?", "12*100", "Se multiplica el largo de la ranura por las placas.", " mm"),
        ("En un plano de ejemplo hay una ranura de 18 mm de ancho y fresas de 12, 18 y 25 mm. ¿Qué fresas caben?", "Las de 12 y 18 mm", "La de 25 mm es más ancha que la ranura de 18 mm."),
    ],
    ctx=("abc", "La ficha de herramientas de ejemplo solo tiene una fresa de 16 mm y la ranura es de 12 mm. ¿Qué propones?", "Informar que no hay fresa adecuada y pedir una de 12 mm o menos antes de planificar", "Usar la de 16 mm de todos modos", "Cambiar el ancho de la ranura en el plano", "La herramienta debe calzar con lo que pide el plano."),
    sc=[
        ("En Máquinas-Herramientas: ¿qué fresa cabe en una ranura de 10 mm?", "Una de 10 mm o menos", "No puede ser más ancha que la ranura."),
        ("En Máquinas-Herramientas: ¿quién fija los parámetros reales de corte?", "El fabricante, en su manual", "El cuaderno solo usa valores de ejemplo."),
        ("En Máquinas-Herramientas: ¿qué indica rpm?", "Las vueltas por minuto de la herramienta", "En este caso, mide qué tan rápido gira."),
    ],
    op=("Ficha de ejemplo: una pieza con una ranura de 10 mm de ancho, 6 mm de profundidad y 80 mm de largo. Fresas: A, 6 mm; B, 10 mm; C, 14 mm. Parámetros de ejemplo: 400 rpm; fresa de 2 dientes; avance por diente 100 µm. Fórmula: rpm × dientes × avance por diente ÷ 1.000. Escribe (a) qué fresas caben, (b) el avance de la mesa en mm por minuto, (c) cuántos minutos tarda en recorrer la ranura, (d) por qué esos valores no sirven para un trabajo real.",
        "(a) La A y la B. (b) 400 × 2 × 100 ÷ 1.000 = 80 mm por minuto. (c) 80 ÷ 80 = 1 minuto. (d) Porque son valores de ejemplo; los reales los fija el fabricante en su manual.",
        ["elige las fresas que caben", "calcula el avance", "calcula el tiempo", "explica el límite del ejercicio"],
        ["hoja con las cuatro respuestas"],
        ["elegir la fresa ancha", "equivocarse con el 1.000", "usar los valores en un trabajo real"],
        "Pregunta: «¿la fresa es más ancha que la ranura?». Si duda, pídele que compare cada diámetro."),
    reinforce="Inventa una ranura y tres fresas y elige cuáles caben.",
    extend="Explica con un ejemplo por qué una fresa más ancha que la ranura no sirve.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 3 (hoja de proceso de fresado de ejemplo con inconsistencias, inventada). Pieza «Soporte»: largo 150 mm, ancho 80 mm, espesor 25 mm; una ranura de 16 mm de ancho y 10 mm de profundidad, 150 mm de largo. Hoja: Op10, fresar la cara superior, 12 min; Op20, fresar la ranura con la fresa de 20 mm de diámetro, 15 min; Op30, fresar el chaflán, 6 min; "
     "Op40, controlar, 5 min; total anotado: 48 min. Máquina anotada: fresadora universal para Op10 a Op30. Avance de ejemplo de la hoja: 150 mm por minuto; para la ranura de 150 mm de largo se anotan 3 minutos de recorrido. Revisión de la hoja: B; del plano: B.")
build(
    O2, 3, F,
    use="Aprenderé a revisar en papel una hoja de proceso de fresado, a detectar incoherencias de herramienta, suma y tiempo, y a informar sin corregir por cuenta propia.",
    prior=["Sé qué es una ranura y una fresa.", "Sé calcular un tiempo de recorrido.", "Sé sumar tiempos."],
    explain=[
        "Al revisar una hoja de fresado se comprueban la herramienta contra el plano, la suma de tiempos y los tiempos de recorrido. El tiempo de recorrido se calcula dividiendo la distancia entre el avance de la mesa por minuto. Una fresa de diámetro mayor que el ancho de la ranura es una incoherencia, igual que un tiempo de recorrido que no coincide con el avance anotado.",
        "Quien detecta una incoherencia la registra con el dato y el motivo y la informa a quien emitió la hoja, que emite una nueva revisión. Nadie corrige el documento por cuenta propia. Una hoja corregida se revisa de nuevo. La revisión es solo documental.",
        f"El análisis es de papel. {EMER} {AVISO}",
    ],
    vocab=[("tiempo de recorrido", "distancia dividida por el avance de la mesa por minuto"), ("incoherencia de herramienta", "herramienta que no calza con lo que pide el plano"), ("revisión documental", "comparación de la hoja con el plano y los cálculos"), ("hoja corregida", "nueva revisión emitida por quien la hizo"), ("avance de la mesa", "distancia que avanza la mesa por minuto")],
    worked=[
        ("Tiempo de recorrido", "Un recorrido de ejemplo de 200 mm con un avance de 100 mm por minuto. ¿Cuántos minutos toma?", ["Se divide la distancia entre el avance.", "200 dividido en 100 son 2."], "2 minutos"),
        ("Fresa ancha", "Una ranura de ejemplo es de 8 mm y la hoja anota una fresa de 10 mm. ¿Es coherente?", ["La fresa es más ancha que la ranura.", "No cabe."], "No es coherente"),
    ],
    mistakes=[("Revisar solo la suma de la hoja y no la herramienta.", "Una herramienta incorrecta también produce una pieza defectuosa.", "Revisa herramienta, suma y tiempos."),
              ("Cambiar la hoja a mano.", "Solo quien la emitió la modifica.", "Informa y pide una nueva revisión.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿cómo se calcula un tiempo de recorrido?", "Dividiendo la distancia entre el avance de la mesa por minuto", "Multiplicando la distancia por el avance", "Sumando las rpm y los dientes", "El tiempo es distancia dividida por velocidad."),
        ("abc", "En Máquinas-Herramientas: ¿qué es una incoherencia de herramienta?", "Una herramienta que no calza con lo que pide el plano", "Una herramienta muy nueva", "Una herramienta guardada en el pañol", "Calzar con el plano es el requisito."),
        ("abc", "En Máquinas-Herramientas: ¿quién corrige una hoja de proceso con errores?", "Quien la emitió, con una nueva revisión", "Quien la detectó, a mano", "El operador que la usa", "Solo quien emitió el documento lo cambia."),
        ("=", "{F} ¿Cuántos minutos suman realmente las cuatro operaciones?", "12+15+6+5", "Se suman los tiempos de las cuatro operaciones.", " minutos"),
        ("abc", "{F} ¿Es correcto el total de 48 minutos anotado?", "No, porque las operaciones suman 38", "Sí, porque 48 es la suma", "Sí, porque incluye un descanso", "12 más 15 más 6 más 5 son 38."),
        ("abc", "{F} ¿Qué incoherencia hay en la herramienta de la ranura?", "La fresa de 20 mm es más ancha que la ranura de 16 mm", "La fresa de 20 mm es más angosta que la ranura", "No hay ninguna", "Una fresa de 20 mm no cabe en una ranura de 16 mm."),
        ("=", "{F} ¿Cuántos minutos de recorrido corresponden a la ranura de 150 mm con el avance de 150 mm por minuto?", "150//150", "Se divide el largo de la ranura entre el avance por minuto.", " minuto"),
        ("abc", "{F} La hoja anota 3 minutos de recorrido para la ranura. ¿Qué observación es correcta?", "Es inconsistente con el avance anotado, que daría 1 minuto de recorrido", "Es consistente con el avance", "Es consistente porque la ranura es larga", "El avance de 150 mm por minuto da 1 minuto de recorrido."),
        ("=", "{F} ¿Cuántos minutos más suman las tres operaciones de fresado (Op10 a Op30) que el control (Op40)?", "(12+15+6)-5", "Se suman las tres operaciones de fresado y se resta el control.", " minutos"),
        ("abc", "{F} Las revisiones de la hoja y del plano son ambas B. ¿Qué corresponde?", "Es correcto en ese punto: coinciden", "Es un error", "Hay que cambiar ambas a C", "La razón es que coinciden las revisiones."),
        ("abc", "{F} Un operario propone usar la fresa de 20 mm para ahorrar tiempo y ensanchar después la ranura. ¿Qué respuesta es correcta?", "No corresponde: el plano manda el ancho de 16 mm, y cualquier cambio lo decide quien lo emitió", "Corresponde, porque ahorra tiempo", "Corresponde, si lo anota", "El plano fija el ancho de la ranura."),
        ("=", "{F} Si se corrige el total a 38 minutos y se fabrican 10 soportes, ¿cuántos minutos suma la hoja para el lote?", "38*10", "Se multiplican los minutos por las piezas.", " minutos"),
        ("En una hoja de ejemplo se anota una profundidad de ranura de 30 mm en una pieza de 25 mm de espesor. ¿Qué conviene hacer?", "Informarlo, porque la ranura no puede ser más profunda que el espesor", "La profundidad supera el espesor, lo cual es imposible sin traspasar la pieza."),
    ],
    ctx=("abc", "Un operario de ejemplo dice: «en la hoja hay errores, pero yo los corrijo en la máquina». ¿Qué propones?", "Registrar los errores y pedir una nueva revisión a quien emitió la hoja antes de trabajar", "Corregir en la máquina", "Anotar los cambios a lápiz", "Los cambios de proceso se hacen por revisión de quien emitió la hoja."),
    sc=[
        ("En Máquinas-Herramientas: ¿cuánto tarda un recorrido de 300 mm a 100 mm por minuto?", "3 minutos", "Se divide la distancia entre el avance."),
        ("En Máquinas-Herramientas: ¿qué se compara con el plano al revisar una hoja?", "La herramienta, la suma y los tiempos", "Cada dato debe coincidir con el plano."),
        ("En Máquinas-Herramientas: ¿quién emite la revisión corregida?", "Quien emitió la hoja", "En este caso, así queda registro del cambio."),
    ],
    op=("Ficha de ejemplo: pieza con una ranura de 10 mm de ancho y 90 mm de largo. Hoja: Op10 fresar cara, 8 min; Op20 fresar la ranura con una fresa de 12 mm, 6 min de recorrido con un avance anotado de 90 mm por minuto; Op30 controlar, 4 min; total anotado 20 min. Escribe (a) la suma real, (b) la incoherencia de herramienta, (c) el tiempo de recorrido que corresponde con el avance, (d) a quién informas.",
        "(a) 8 + 6 + 4 = 18 minutos. (b) La fresa de 12 mm es más ancha que la ranura de 10 mm. (c) 90 ÷ 90 = 1 minuto. (d) A quien emitió la hoja, para que emita una nueva revisión.",
        ["suma los tiempos", "detecta la fresa ancha", "calcula el tiempo", "indica a quién informa"],
        ["hoja con las cuatro respuestas"],
        ["no detectar la fresa", "calcular mal el tiempo", "corregir por cuenta propia"],
        "Pregunta: «¿la fresa cabe en la ranura?». Si duda, pídele que compare los dos diámetros."),
    reinforce="Escribe tres incoherencias posibles en una hoja de fresado y cómo las detectarías.",
    extend="Explica con un ejemplo por qué un tiempo de recorrido inconsistente puede esconder otro error de la hoja.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 4 (planificación de ejemplo para un lote). Lote de 60 soportes en la fresadora. Ranura: 150 mm de largo, 2 pasadas por soporte; avance de ejemplo 100 mm por minuto; cada pasada se hace una tras otra. Cara superior: 5 minutos por soporte. "
     "Colocar y retirar la pieza: 3 minutos por soporte. Cambio de herramienta: 6 minutos, 2 veces por lote. Control: 2 minutos por soporte. Costo de ejemplo de la fresadora: $15.000 por hora. Turno: 480 minutos. 5 soportes del lote salen defectuosos.")
build(
    O2, 4, F,
    use="Aprenderé a calcular el tiempo de ciclo por pieza, el tiempo del lote, el costo y la cantidad de turnos, y a considerar los defectuosos, con datos de ejemplo.",
    prior=["Sé calcular tiempos de recorrido.", "Sé multiplicar, dividir y sumar enteros.", "Sé calcular un costo por minuto."],
    explain=[
        "El tiempo de ciclo de una pieza suma todos sus tiempos: el recorrido de cada pasada, el tiempo de otras operaciones, el de colocar y retirar la pieza y el control. El tiempo del lote es el tiempo de ciclo por el número de piezas más los tiempos que se hacen por lote, como los cambios de herramienta. El costo del lote es los minutos totales por el costo por minuto, que es el costo por hora dividido por 60.",
        "Los turnos necesarios se calculan dividiendo los minutos del lote entre los minutos del turno y se redondea hacia arriba. Los defectuosos se restan de las piezas del lote para obtener las piezas buenas, y el costo por pieza buena se obtiene dividiendo el costo del lote entre ellas. Todo es un cálculo en papel con valores de ejemplo.",
        f"No se opera ninguna máquina. {EMER} {AVISO}",
    ],
    vocab=[("tiempo de ciclo", "suma de todos los tiempos para hacer una pieza"), ("tiempo del lote", "tiempo de ciclo por las piezas más los tiempos por lote"), ("pasada", "recorrido de la herramienta sobre la pieza en una profundidad"), ("costo por pieza buena", "costo del lote dividido entre las piezas buenas"), ("turno", "jornada de 480 minutos en los ejemplos")],
    worked=[
        ("Tiempo de ciclo", "Una pieza de ejemplo toma 4 minutos de corte, 2 de colocar y 1 de control. ¿Cuánto es el tiempo de ciclo?", ["Se suman los tres tiempos.", "4 más 2 más 1 son 7."], "7 minutos"),
        ("Turnos", "Un lote de ejemplo requiere 900 minutos y el turno tiene 480. ¿Cuántos turnos se necesitan?", ["900 dividido en 480 da 1 y sobran 420.", "Se necesita otro turno para el resto."], "2 turnos"),
    ],
    mistakes=[("Olvidar los tiempos por lote, como los cambios de herramienta.", "Se hacen aunque el lote sea grande y suman tiempo.", "Suma los tiempos por pieza multiplicados y los tiempos por lote."),
              ("Redondear hacia abajo los turnos.", "Quedaría trabajo sin hacer.", "Redondea hacia arriba si hay resto.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es el tiempo de ciclo?", "La suma de todos los tiempos para hacer una pieza", "El tiempo que dura el turno", "El tiempo de cambio de herramienta solamente", "El ciclo incluye corte, colocación, control y otros."),
        ("abc", "En Máquinas-Herramientas: ¿qué es una pasada?", "Un recorrido de la herramienta sobre la pieza a una profundidad", "Una pieza terminada", "El cambio de herramienta", "Una pasada es un recorrido de corte."),
        ("abc", "En Máquinas-Herramientas: ¿cómo se redondea el número de turnos?", "Hacia arriba", "Hacia abajo", "No se redondea", "Un resto de trabajo exige otro turno."),
        ("=", "{F} ¿Cuántos minutos tarda una pasada de 150 mm a 100 mm por minuto, en minutos enteros redondeando hacia arriba?", "(150+99)//100", "Se divide el largo entre el avance, redondeando hacia arriba.", " minutos"),
        ("=", "{F} ¿Cuántos minutos de recorrido de ranura tiene un soporte, con 2 pasadas de 2 minutos cada una?", "2*2", "Se multiplican las pasadas por los minutos de cada una.", " minutos"),
        ("=", "{F} ¿Cuál es el tiempo de ciclo de un soporte, sumando ranura, cara, colocar y retirar, y control?", "4+5+3+2", "Se suman los tiempos de las cuatro partes.", " minutos"),
        ("=", "{F} ¿Cuántos minutos suman los cambios de herramienta del lote?", "6*2", "Se multiplican los minutos de cada cambio por las veces.", " minutos"),
        ("=", "{F} ¿Cuántos minutos necesita el lote de 60 soportes, con el tiempo de ciclo de 14 minutos y los cambios de herramienta?", "60*14+12", "Se multiplica el ciclo por las piezas y se suman los cambios.", " minutos"),
        ("=", "{F} ¿Cuántos turnos se necesitan para 852 minutos, con turnos de 480 minutos?", "(852+479)//480", "Se divide entre 480 redondeando hacia arriba.", " turnos"),
        ("=", "{F} ¿Cuántos soportes buenos tiene el lote?", "60-5", "Se restan los defectuosos al lote.", " soportes"),
        ("abc", "{F} Un jefe dice: «alcanza con un turno para el lote». ¿Qué respuesta es correcta?", "Es falso: el lote requiere 852 minutos y el turno tiene 480", "Es cierto, porque son 60 piezas", "Es cierto, si se trabaja rápido", "La razón es que 852 supera 480."),
        ("=", "{F} ¿Cuánto cuesta el lote de 852 minutos en fresadora, a $15.000 la hora?", "852*15000//60", "Se multiplican los minutos por el costo de la hora y se dividen por 60.", " pesos de ejemplo"),
        ("Si el lote cuesta $213.000 y salen 55 soportes buenos, ¿cuánto cuesta aproximadamente cada soporte bueno, sin decimales?", "$3.872", "213.000 dividido en 55 da 3.872 con enteros."),
    ],
    ctx=("abc", "El cliente de ejemplo quiere el lote en un turno. El cálculo da 852 minutos. ¿Qué propones?", "Informar que se necesitan 2 turnos o más personal o máquinas", "Prometer el turno único", "Omitir el control para ganar tiempo", "El plazo se basa en los minutos reales."),
    sc=[
        ("En Máquinas-Herramientas: ¿cuánto suman 4, 5, 3 y 2 minutos?", "14 minutos", "Es el tiempo de ciclo de la ficha."),
        ("En Máquinas-Herramientas: ¿qué tiempos se suman una vez por lote?", "Los cambios de herramienta", "No dependen del número de piezas."),
        ("En Máquinas-Herramientas: ¿qué se resta de las piezas del lote para obtener las buenas?", "Los defectuosos", "En este caso, los defectuosos no se entregan."),
    ],
    op=("Ficha de ejemplo: lote de 30 placas en una fresadora. Ranura: 1 pasada de 3 minutos por placa; cara: 4 minutos; colocar y retirar: 2 minutos; control: 1 minuto. Cambio de herramienta: 5 minutos, 2 veces por lote. Costo de la fresadora: $12.000 la hora. Turno: 480 minutos. Escribe (a) el tiempo de ciclo, (b) los minutos del lote, (c) cuántos turnos se necesitan, (d) el costo del lote.",
        "(a) 3 + 4 + 2 + 1 = 10 minutos. (b) 30 × 10 + 2 × 5 = 310 minutos. (c) 310 ÷ 480 es menos de 1, es decir 1 turno. (d) 310 × 12.000 ÷ 60 = 62.000 pesos de ejemplo.",
        ["calcula el ciclo", "calcula los minutos del lote", "calcula los turnos", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["olvidar los cambios", "redondear mal", "no dividir por 60"],
        "Pregunta: «¿qué tiempos se repiten por pieza y cuáles por lote?». Si duda, pídele que los separe."),
    reinforce="Inventa un ciclo de cuatro tiempos y calcula los minutos de un lote de 20 piezas.",
    extend="Explica con un ejemplo por qué los cambios de herramienta se suman una vez por lote y no por pieza.",
)

# ============================================================ OAM-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El taller tiene un taladro de columna y una rectificadora ficticios. Taladrar es hacer un agujero con una broca; rectificar es dar una terminación muy fina a una superficie con una muela, un disco de abrasivo. "
     "Peligros anotados: broca giratoria, atrapamiento por ropa o pelo, virutas, muela que podría romperse y proyectar fragmentos, polvo abrasivo, ruido, fluido de corte y piezas pesadas. Elementos de seguridad: resguardo de la muela, protección de la broca, parada de emergencia.")
build(
    O3, 1, F,
    use="Aprenderé qué es taladrar y rectificar, qué peligros tiene cada máquina y qué reglas generales de seguridad existen, sobre todo para la muela.",
    prior=["Sé qué es una máquina-herramienta.", "Sé qué es un abrasivo.", "Sé qué es un resguardo."],
    explain=[
        "Taladrar es hacer un agujero con una broca, una herramienta giratoria. Un agujero pasante atraviesa la pieza y uno ciego no. Rectificar es mejorar mucho la terminación y la medida de una superficie con una muela, un disco de abrasivo que gira muy rápido. La rectificadora logra tolerancias más finas que otras máquinas, porque retira cantidades muy pequeñas de material.",
        "La muela puede romperse si se daña o gira más rápido que su velocidad máxima, que viene marcada, y sus fragmentos salen proyectados con gran energía. Por eso tiene un resguardo y solo personal autorizado la revisa y la monta. En el taladro, el peligro principal es el atrapamiento por ropa o pelo en la broca. Se controlan con resguardos, paradas de emergencia, orden, capacitación y EPP, incluyendo protección ocular y auditiva.",
        f"Este cuaderno no enseña a operar estas máquinas. {EMER} {AVISO}",
    ],
    vocab=[("taladrar", "hacer un agujero con una broca"), ("agujero pasante", "el que atraviesa la pieza"), ("agujero ciego", "el que no atraviesa la pieza"), ("rectificar", "dar una terminación muy fina a una superficie con una muela"), ("muela", "disco de abrasivo que gira muy rápido"), ("velocidad máxima de la muela", "límite de giro marcado que no se debe superar")],
    worked=[
        ("Tipo de agujero", "Un agujero de ejemplo atraviesa totalmente la pieza. ¿Qué tipo de agujero es?", ["Atraviesa de lado a lado.", "Es un agujero pasante."], "Pasante"),
        ("Peligro de la muela", "Una muela de ejemplo gira más rápido que su velocidad máxima marcada. ¿Qué puede ocurrir?", ["La muela puede romperse.", "Sus fragmentos salen proyectados."], "Puede romperse y proyectar fragmentos"),
    ],
    mistakes=[("Retirar el resguardo de la muela para ver mejor.", "Si la muela se rompe, el resguardo retiene los fragmentos.", "El resguardo nunca se retira."),
              ("Creer que leer sobre rectificado habilita para operar la máquina.", "Su uso y el montaje de la muela exigen personal autorizado.", "Aprende el concepto y deja el uso a quien corresponde.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es un agujero ciego?", "El que no atraviesa la pieza", "El que atraviesa la pieza", "El que no tiene diámetro", "Ciego significa que no sale al otro lado."),
        ("abc", "En Máquinas-Herramientas: ¿qué es rectificar?", "Dar una terminación muy fina a una superficie con una muela", "Hacer un agujero con una broca", "Cortar una barra con una sierra", "Rectificar afina la superficie con abrasivo."),
        ("abc", "En Máquinas-Herramientas: ¿qué es la muela?", "Un disco de abrasivo que gira muy rápido", "Una broca de gran diámetro", "Un instrumento de medición", "La muela es el disco abrasivo."),
        ("abc", "{F} ¿Cuál es el peligro principal de la muela de la ficha?", "Que se rompa y proyecte fragmentos", "Que cambie de color", "Que se enfríe", "Una muela dañada puede romperse con gran energía."),
        ("abc", "{F} ¿Qué elemento de seguridad retiene los fragmentos de una muela que se rompe?", "El resguardo de la muela", "La parada de emergencia", "El fluido de corte", "El resguardo es la barrera que los retiene."),
        ("abc", "{F} ¿Qué peligro de la lista se relaciona con ropa suelta cerca de una broca?", "El atrapamiento", "El polvo abrasivo", "El ruido", "La ropa suelta puede quedar atrapada en una broca."),
        ("=", "{F} El taller tiene 2 máquinas y 4 personas por máquina en la prueba. ¿Cuántas personas se necesitan?", "2*4", "Se multiplican las máquinas por las personas de cada una.", " personas"),
        ("=", "{F} Cada día se retiran 6 kg de virutas del taladro y 2 kg de polvo de la rectificadora. ¿Cuántos kg se retiran en 5 días?", "(6+2)*5", "Se suman los residuos de un día y se multiplican por los días.", " kg"),
        ("abc", "{F} Un compañero dice: «la muela no tiene resguardo y es más fácil trabajar». ¿Qué respuesta es correcta?", "Es falso: una muela sin resguardo puede proyectar fragmentos, y no se retira", "Es cierto, porque se ve mejor", "Es cierto, si es una muela nueva", "El resguardo protege contra la rotura de la muela."),
        ("abc", "{F} Una muela marcada con una velocidad máxima de 3.000 rpm se querría usar a 3.500 rpm. ¿Qué respuesta es correcta?", "No corresponde: nunca se supera la velocidad máxima marcada en la muela", "Corresponde, si es por poco tiempo", "Corresponde, si la pieza es chica", "Superar el máximo puede romper la muela."),
        ("abc", "En una visita a un taller de ejemplo, se rompe una muela y una persona queda herida. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Recoger los fragmentos con las manos", "Mover la máquina", "Hay riesgo de otros fragmentos y de lesiones."),
        ("=", "{F} El taller de ejemplo cambia 3 muelas por año en la rectificadora y cada una cuesta $40.000. ¿Cuánto cuestan las muelas al año?", "3*40000", "Se multiplican las muelas por el precio de cada una.", " pesos de ejemplo"),
        ("abc", "En Máquinas-Herramientas: ¿qué se hace con el polvo abrasivo del taller?", "Se gestiona como residuo según la norma vigente", "Se barre al desagüe", "Se deja en el piso", "El polvo abrasivo es un residuo que requiere gestión."),
    ],
    ctx=("abc", "Un amigo de ejemplo te dice: «cambiemos la muela de la rectificadora del colegio, es fácil». ¿Qué respondes?", "Que montar una muela exige personal autorizado y norma vigente, y que consultarás a un adulto responsable", "Que sí, si vamos con gafas", "Que sí, si la máquina está apagada", "El montaje de una muela es un trabajo de personal autorizado."),
    sc=[
        ("En Máquinas-Herramientas: ¿qué es un agujero pasante?", "El que atraviesa la pieza", "Pasante significa que sale al otro lado."),
        ("En Máquinas-Herramientas: ¿qué no se debe superar en una muela?", "Su velocidad máxima marcada", "La razón es que superarla puede romperla."),
        ("En Máquinas-Herramientas: ¿quién monta una muela?", "Personal autorizado", "En este caso, exige formación y norma vigente."),
    ],
    op=("Ficha de ejemplo: un taller tiene un taladro de banco y una rectificadora ficticios. Peligros: broca giratoria, atrapamiento, muela que podría romperse y polvo. Escribe (a) qué tipo de control es el resguardo de la muela, (b) qué regla evita el atrapamiento en el taladro, (c) por qué no se supera la velocidad máxima de la muela, (d) qué haces si ves a alguien herido por una muela rota. No describas cómo se opera.",
        "(a) Un control de ingeniería. (b) Usar ropa ajustada y pelo recogido, sin joyas ni guantes sueltos. (c) Porque la muela puede romperse y proyectar fragmentos. (d) No acercarme a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["clasifica el resguardo", "indica la regla contra el atrapamiento", "explica la velocidad máxima", "indica qué hacer ante un accidente"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la regla de vestimenta", "decir que se puede superar la velocidad", "intervenir ante el accidente"],
        "Pregunta: «¿qué ocurre si una muela se rompe?». Si duda, pídele que relea el peligro de la muela."),
    reinforce="Escribe la diferencia entre taladrar y rectificar y un peligro propio de cada máquina.",
    extend="Explica con un ejemplo por qué el resguardo de la muela no se retira.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 2 (plano y ficha de herramientas descritos por escrito, de ejemplo e inventados). Pieza «Placa con agujeros»: espesor 20 mm. Cuatro agujeros pasantes de 10 mm de diámetro, separados 40 mm entre centros en línea recta. Un agujero ciego de 12 mm de diámetro y 15 mm de profundidad. "
     "Eje rectificado de la pieza: diámetro 30.000 µm con tolerancia ±8 µm, rugosidad Ra 0 (unidad de ejemplo; menor número, más liso). Broca disponible según la ficha de herramientas: 8 mm, 10 mm, 12 mm y 14 mm. Muela: velocidad máxima marcada 3.000 rpm.")
build(
    O3, 2, F,
    use="Aprenderé a leer un plano con agujeros pasantes y ciegos y con una pieza rectificada, a elegir la broca por diámetro y a reconocer las tolerancias del rectificado.",
    prior=["Sé qué es un agujero pasante y uno ciego.", "Sé qué es una tolerancia.", "Sé leer una lista de herramientas."],
    explain=[
        "Un plano de agujeros indica su diámetro, su profundidad (si son ciegos) y la distancia entre centros. Se elige una broca del diámetro del agujero. Una broca de diámetro distinto no sirve: una más pequeña deja un agujero menor y una más grande, uno mayor. En un agujero ciego, la profundidad pedida debe ser menor que el espesor de la pieza.",
        "El rectificado se pide cuando una superficie necesita una tolerancia fina y una rugosidad baja, por ejemplo ±8 µm. La muela tiene una velocidad máxima marcada que nunca se supera. Una pieza rectificada deja poca sobremedida: el material de partida es solo unos µm mayor que la medida final. El plano manda sobre la herramienta disponible.",
        f"Aquí solo se leen documentos y se calcula. {EMER} {AVISO}",
    ],
    vocab=[("distancia entre centros", "separación entre los centros de dos agujeros"), ("broca", "herramienta giratoria que hace agujeros"), ("profundidad", "cuánto entra un agujero ciego en la pieza"), ("rugosidad Ra", "valor del acabado de una superficie: menor número, más liso"), ("sobremedida de rectificado", "pocos µm de material que se retiran al rectificar")],
    worked=[
        ("Elegir la broca", "Un agujero de ejemplo es de 9 mm y hay brocas de 8, 9 y 10 mm. ¿Cuál se elige?", ["La broca debe tener el diámetro del agujero.", "Se elige la de 9 mm."], "La de 9 mm"),
        ("Revisar la profundidad", "Una pieza de ejemplo tiene 15 mm de espesor y un agujero ciego de 18 mm de profundidad. ¿Es posible?", ["Un agujero ciego no puede ser más profundo que el espesor.", "18 es mayor que 15."], "No es posible"),
    ],
    mistakes=[("Elegir una broca de diámetro mayor «para asegurar».", "El agujero queda más grande que lo pedido.", "Elige la broca del diámetro del agujero."),
              ("Dar por válido un agujero ciego más profundo que el espesor.", "Atravesaría la pieza y dejaría de ser ciego.", "Revisa que la profundidad sea menor que el espesor.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es la distancia entre centros de dos agujeros?", "La separación entre sus centros", "La suma de sus diámetros", "La profundidad de uno de ellos", "Se mide de centro a centro."),
        ("abc", "En Máquinas-Herramientas: ¿cuándo se pide el rectificado en un plano?", "Cuando una superficie necesita tolerancia fina y rugosidad baja", "Cuando la pieza es muy grande", "Cuando se quiere hacer un agujero", "El rectificado se pide por exigencias de precisión."),
        ("abc", "En Máquinas-Herramientas: ¿qué diámetro debe tener la broca para un agujero de 10 mm?", "10 mm", "12 mm", "8 mm", "La broca debe ser del diámetro del agujero."),
        ("abc", "{F} ¿Qué broca de la ficha se elige para los agujeros pasantes?", "La de 10 mm", "La de 8 mm", "La de 14 mm", "Los agujeros pasantes son de 10 mm."),
        ("abc", "{F} ¿Qué broca se elige para el agujero ciego?", "La de 12 mm", "La de 10 mm", "La de 14 mm", "El agujero ciego es de 12 mm de diámetro."),
        ("=", "{F} ¿Cuántos mm de profundidad sobran entre el espesor de la pieza y la profundidad del agujero ciego?", "20-15", "Se resta la profundidad al espesor.", " mm"),
        ("=", "{F} ¿Cuántos mm hay entre el primer y el último centro de los cuatro agujeros alineados, con 40 mm entre centros?", "40*3", "Hay 3 separaciones entre 4 agujeros.", " mm"),
        ("=", "{F} ¿Cuál es el límite superior del diámetro del eje rectificado, en µm?", "30000+8", "Se suma la tolerancia al valor del plano.", " µm"),
        ("=", "{F} ¿Cuál es el límite inferior del diámetro del eje rectificado, en µm?", "30000-8", "Se resta la tolerancia al valor del plano.", " µm"),
        ("abc", "{F} Un eje rectificado mide 30.006 µm. ¿Cumple?", "Sí, porque se aparta 6 µm y la tolerancia es de 8 µm", "No, porque no es 30.000", "No, porque supera 30.000", "En este caso, 6 es menor que 8."),
        ("abc", "{F} Un compañero propone hacer los agujeros pasantes con la broca de 12 mm «porque es más resistente». ¿Qué respuesta es correcta?", "No corresponde: el plano pide 10 mm y una broca mayor deja el agujero fuera de medida", "Corresponde, porque es más resistente", "Corresponde, si baja la velocidad", "En este caso, El diámetro del plano manda."),
        ("abc", "{F} Un operario dice: «uso la muela a 3.500 rpm para terminar antes». ¿Qué respuesta es correcta?", "No corresponde: la velocidad máxima marcada es de 3.000 rpm y no se supera", "Corresponde, si la pieza es pequeña", "Corresponde, si la muela es nueva", "Superar la velocidad máxima puede romper la muela."),
        ("=", "{F} Se fabrican 10 placas iguales y cada una tiene 4 agujeros pasantes. ¿Cuántos agujeros pasantes se hacen en total?", "10*4", "Se multiplican las placas por los agujeros de cada una.", " agujeros"),
    ],
    ctx=("abc", "El pañolero de ejemplo ofrece una broca de 11 mm «parecida» para un agujero de 10 mm. ¿Qué propones?", "No usarla y pedir una broca de 10 mm o consultar al responsable del proceso", "Usarla porque es parecida", "Cambiar el diámetro del plano a 11 mm", "En este caso, El diámetro del plano manda."),
    sc=[
        ("En Máquinas-Herramientas: ¿qué diámetro de broca corresponde a un agujero de 12 mm?", "12 mm", "La broca debe ser del diámetro del agujero."),
        ("En Máquinas-Herramientas: ¿cuántas separaciones hay entre 4 agujeros alineados?", "3", "En este caso, entre cuatro hay tres espacios."),
        ("En Máquinas-Herramientas: ¿qué es un agujero ciego?", "El que no atraviesa la pieza", "Ciego significa que no sale al otro lado."),
    ],
    op=("Ficha de ejemplo: pieza de 25 mm de espesor con 3 agujeros pasantes de 8 mm separados 30 mm entre centros y un agujero ciego de 10 mm y 20 mm de profundidad. Brocas: 6, 8, 10 y 12 mm. Un eje rectificado de 20.000 µm con tolerancia de ±6 µm. Escribe (a) qué broca para cada tipo de agujero, (b) cuántos mm hay entre el primero y el último centro de los 3 agujeros, (c) el rango del eje en µm, (d) si es posible la profundidad del agujero ciego.",
        "(a) Pasantes, broca de 8 mm; ciego, broca de 10 mm. (b) 30 × 2 = 60 mm. (c) Entre 19.994 y 20.006 µm. (d) Sí, 20 mm es menor que el espesor de 25 mm.",
        ["elige las brocas", "calcula la distancia", "calcula el rango del eje", "evalúa la profundidad"],
        ["hoja con las cuatro respuestas"],
        ["elegir una broca mayor", "contar mal las separaciones", "no incluir los límites"],
        "Pregunta: «¿qué diámetro pide el plano?». Si duda, pídele que relea los datos."),
    reinforce="Inventa un plano con dos tipos de agujeros y elige la broca de cada uno.",
    extend="Explica con un ejemplo por qué una broca mayor que el agujero no sirve aunque sea más resistente.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 3 (hoja de proceso de rectificado de ejemplo, inventada). Eje con diámetro final pedido de 40.000 µm y tolerancia ±5 µm. Antes del rectificado el eje mide 40.150 µm. En cada pasada de rectificado de ejemplo se retiran 20 µm de diámetro, y las últimas dos pasadas son de acabado de 5 µm de diámetro. "
     "Rugosidad pedida Ra 0 (unidad de ejemplo). Medición tras el rectificado: 40.007 µm. Instrumento: micrómetro con certificado vigente. Muela: velocidad máxima 3.000 rpm; velocidad anotada en la hoja: 2.800 rpm. Tiempo de ejemplo de una pasada: 2 minutos.")
build(
    O3, 3, F,
    use="Aprenderé a analizar en papel una hoja de rectificado, calculando la sobremedida, el número de pasadas y el tiempo, y juzgando si el resultado medido cumple.",
    prior=["Sé qué es la sobremedida.", "Sé qué es una tolerancia.", "Sé multiplicar y restar enteros."],
    explain=[
        "En un rectificado de ejemplo se retira poco material por pasada. La sobremedida es la diferencia entre el diámetro antes de rectificar y el diámetro final pedido. Con una cantidad retirada por pasada, el número de pasadas se calcula dividiendo la sobremedida entre lo que retira cada una; si hay pasadas de acabado distintas, se calculan aparte. El tiempo total es el número de pasadas por el tiempo de cada una.",
        "Después de rectificar se mide con un instrumento con certificado vigente y se compara con la tolerancia. Una medición fuera de tolerancia es una no conformidad que se registra y se informa. La velocidad anotada en la hoja debe ser menor o igual que la velocidad máxima de la muela. Los valores son de ejemplo y el análisis es de papel.",
        f"Este cuaderno no enseña a rectificar. {EMER} {AVISO}",
    ],
    vocab=[("pasada de desbaste", "pasada que retira bastante material"), ("pasada de acabado", "pasada final que retira muy poco material"), ("sobremedida", "diferencia entre el diámetro antes y después de rectificar"), ("no conformidad", "resultado que no cumple lo pedido"), ("instrumento calibrado", "instrumento con certificado vigente")],
    worked=[
        ("Número de pasadas", "Una sobremedida de ejemplo de 100 µm se retira con pasadas de 25 µm. ¿Cuántas pasadas se necesitan?", ["Se divide la sobremedida entre lo que retira cada pasada.", "100 dividido en 25 son 4."], "4 pasadas"),
        ("Cumplir la tolerancia", "Un diámetro final de ejemplo es de 20.000 µm ±4 µm y se mide 20.003 µm. ¿Cumple?", ["La diferencia es de 3 µm.", "3 es menor que 4."], "Sí, cumple"),
    ],
    mistakes=[("Ignorar las pasadas de acabado al calcular el total.", "Las pasadas de acabado también retiran material y toman tiempo.", "Calcula desbaste y acabado por separado y súmalos."),
              ("Aceptar una medición sin revisar el certificado del instrumento.", "Un instrumento sin certificado vigente deja la medición en duda.", "Verifica el certificado antes de aceptar.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es una pasada de acabado?", "La pasada final que retira muy poco material", "La primera pasada que retira mucho material", "El cambio de la muela", "La pasada de acabado deja la superficie en su medida final."),
        ("abc", "En Máquinas-Herramientas: ¿qué es una sobremedida de rectificado?", "La diferencia entre el diámetro antes y después de rectificar", "El diámetro de la muela", "La tolerancia del plano", "En este caso, Es el material a retirar."),
        ("abc", "En Máquinas-Herramientas: ¿qué se hace con una medición fuera de tolerancia?", "Se registra e informa como no conformidad", "Se anota que cumple", "Se descarta sin informar", "En este caso, La no conformidad se registra."),
        ("=", "{F} ¿Cuántos µm de sobremedida tiene el eje antes de rectificarse?", "40150-40000", "Se resta el diámetro final al diámetro antes del rectificado.", " µm"),
        ("=", "{F} Las dos pasadas de acabado retiran 5 µm cada una. ¿Cuántos µm retiran en total?", "2*5", "Se multiplican las pasadas de acabado por lo que retira cada una.", " µm"),
        ("=", "{F} ¿Cuántos µm deben retirarse en pasadas de desbaste, restando los de acabado de la sobremedida?", "150-10", "Se resta lo de acabado a la sobremedida.", " µm"),
        ("=", "{F} ¿Cuántas pasadas de desbaste de 20 µm se necesitan para retirar 140 µm?", "140//20", "Se divide lo que se retira entre lo que retira cada pasada.", " pasadas"),
        ("=", "{F} ¿Cuántas pasadas suma el rectificado, desbaste y acabado?", "7+2", "Se suman las pasadas de desbaste y las de acabado.", " pasadas"),
        ("=", "{F} ¿Cuántos minutos suma el rectificado, con 2 minutos por pasada?", "9*2", "Se multiplican las pasadas por los minutos de cada una.", " minutos"),
        ("abc", "{F} La medición posterior es de 40.007 µm. ¿Cumple?", "No, porque se aparta 7 µm y la tolerancia es de 5 µm", "Sí, porque es cercana a 40.000", "Sí, porque es menor que 40.150", "7 µm supera los ±5 µm."),
        ("abc", "{F} ¿Qué corresponde hacer tras esa medición?", "Registrar la no conformidad e informar a la jefatura, sin modificar el dato", "Anotar 40.005 en el registro", "Entregar la pieza igualmente", "Un valor fuera de tolerancia no se oculta."),
        ("abc", "{F} Un operario dice: «subo la velocidad de la muela a 3.200 rpm para terminar antes». ¿Qué respuesta es correcta?", "No corresponde: la velocidad máxima de la muela es 3.000 rpm y no se supera", "Corresponde, si el eje es pequeño", "Corresponde, si lo anota", "Superar la velocidad máxima puede romper la muela."),
        ("=", "{F} Si la muela gira a 2.800 rpm, ¿cuántas rpm hay de margen hasta su velocidad máxima de 3.000 rpm?", "3000-2800", "Se resta la velocidad usada a la máxima.", " rpm"),
    ],
    ctx=("abc", "El jefe de ejemplo dice: «la pieza mide 40.007 y la tolerancia es 5, pero se ve bien; entreguemos». ¿Qué propones?", "Registrar la no conformidad e informar, porque el valor está fuera de tolerancia", "Entregar la pieza", "Pulir un poco y anotar que cumple", "Un valor fuera de tolerancia no se entrega sin decisión formal."),
    sc=[
        ("En Máquinas-Herramientas: ¿cómo se calcula el número de pasadas?", "Dividiendo lo que se retira entre lo que retira cada pasada", "Cada pasada retira una cantidad fija."),
        ("En Máquinas-Herramientas: ¿qué velocidad no se supera en una muela?", "La velocidad máxima marcada", "En este caso, superarla puede romper la muela."),
        ("En Máquinas-Herramientas: ¿qué instrumento da una medición confiable?", "Uno con certificado de calibración vigente", "En este caso, El certificado respalda la medición."),
    ],
    op=("Ficha de ejemplo: un eje de 30.000 µm ±4 µm mide 30.090 µm antes de rectificar. Cada pasada de desbaste retira 20 µm; las dos últimas pasadas de acabado retiran 5 µm cada una; una pasada toma 2 minutos. La medición final es 30.006 µm. Escribe (a) la sobremedida, (b) cuántas pasadas de desbaste, (c) el tiempo total, (d) si cumple la tolerancia y qué haces.",
        "(a) 30.090 − 30.000 = 90 µm. (b) Se retiran 90 − 10 = 80 µm en desbaste: 80 ÷ 20 son 4 pasadas. (c) Con 4 de desbaste y 2 de acabado son 6 pasadas por 2 minutos, es decir 12 minutos. (d) No cumple: 6 µm supera 4 µm; se registra la no conformidad y se informa.",
        ["calcula la sobremedida", "calcula las pasadas", "calcula el tiempo", "decide la conformidad"],
        ["hoja con las cuatro respuestas"],
        ["olvidar las pasadas de acabado", "aceptar un valor fuera de tolerancia", "no registrar la no conformidad"],
        "Pregunta: «¿cuántos µm se retiran en total?». Si duda, pídele que reste el diámetro final al inicial."),
    reinforce="Inventa una sobremedida y una cantidad por pasada y calcula el número de pasadas.",
    extend="Explica con un ejemplo por qué una pasada de acabado retira menos material que una de desbaste.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 4 (costeo de un lote de ejemplo, inventado). Lote de 50 piezas: cada una lleva 4 agujeros de taladro y un tramo rectificado. Taladrado: 1 minuto por agujero. Rectificado: 5 minutos por pieza. Colocar y retirar la pieza: 2 minutos en cada máquina. "
     "Costo de ejemplo por hora: taladro $8.000; rectificadora $12.000. Una broca de ejemplo alcanza para 200 agujeros y cuesta $3.000. Una muela cuesta $40.000 y alcanza para 250 piezas. Turno de 480 minutos. Salen defectuosas 2 piezas.")
build(
    O3, 4, F,
    use="Aprenderé a calcular tiempos, costos de máquina y de herramientas (brocas y muelas) y piezas por turno de un lote que pasa por taladro y rectificadora.",
    prior=["Sé calcular un costo por minuto.", "Sé redondear hacia arriba en divisiones con resto.", "Sé multiplicar enteros."],
    explain=[
        "El tiempo de una pieza en cada máquina suma el trabajo y el tiempo de colocar y retirar la pieza. El costo de máquina se calcula con los minutos y el costo por hora dividido por 60. Las herramientas se desgastan: una broca o una muela alcanza para un número de agujeros o de piezas, que se llama su vida de ejemplo. El costo de herramienta por pieza se obtiene dividiendo el precio entre las piezas que alcanza.",
        "Para saber cuántas herramientas se usan, se divide el total de agujeros o de piezas entre lo que alcanza una herramienta, redondeando hacia arriba. El costo total suma máquinas y herramientas. Los defectuosos se restan para obtener las piezas buenas. Todo es un cálculo de papel con valores de ejemplo.",
        f"No se opera ninguna máquina. {EMER} {AVISO}",
    ],
    vocab=[("vida de la herramienta", "cantidad de agujeros o piezas que alcanza una herramienta"), ("costo de herramienta por pieza", "precio de la herramienta dividido entre las piezas que alcanza"), ("tiempo de colocar y retirar", "tiempo de poner y sacar la pieza de la máquina"), ("piezas buenas", "piezas que cumplen el plano"), ("costo total del lote", "suma de máquinas y herramientas")],
    worked=[
        ("Herramientas usadas", "Una broca de ejemplo alcanza para 100 agujeros y se hacen 250 agujeros. ¿Cuántas brocas se usan?", ["250 dividido en 100 da 2 y sobran 50 agujeros.", "Hace falta una broca más."], "3 brocas"),
        ("Costo de una operación", "Una operación de ejemplo dura 15 minutos a $8.000 la hora. ¿Cuánto cuesta?", ["15 minutos son un cuarto de hora.", "Un cuarto de 8.000 son 2.000."], "$2.000"),
    ],
    mistakes=[("Olvidar redondear hacia arriba las herramientas.", "Un resto de agujeros exige otra herramienta.", "Si sobra, se compra una más."),
              ("Calcular el costo sin el tiempo de colocar y retirar.", "Ese tiempo también ocupa la máquina.", "Súmalo al tiempo de cada pieza.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es la vida de una herramienta?", "La cantidad de agujeros o piezas que alcanza antes de cambiarla", "El tiempo que lleva en el pañol", "El precio de compra", "La vida mide cuánto trabajo da la herramienta."),
        ("abc", "En Máquinas-Herramientas: ¿cómo se calcula el costo de herramienta por pieza?", "Dividiendo el precio entre las piezas que alcanza", "Multiplicando el precio por las piezas", "Sumando el precio y las piezas", "Se reparte el precio entre las piezas que se hacen."),
        ("abc", "En Máquinas-Herramientas: ¿qué se hace con un resto al calcular cuántas herramientas se usan?", "Se redondea hacia arriba", "Se ignora", "Se resta", "Un resto exige una herramienta más."),
        ("=", "{F} ¿Cuántos agujeros de taladro tiene el lote?", "50*4", "Se multiplican las piezas por los agujeros de cada una.", " agujeros"),
        ("=", "{F} ¿Cuántos minutos de taladro, con colocar y retirar, requiere una pieza?", "4*1+2", "Se suman los 4 agujeros de 1 minuto y el tiempo de colocar y retirar.", " minutos"),
        ("=", "{F} ¿Cuántos minutos de rectificadora, con colocar y retirar, requiere una pieza?", "5+2", "Se suman el rectificado y el tiempo de colocar y retirar.", " minutos"),
        ("=", "{F} ¿Cuántas brocas se usan en el lote, con 200 agujeros por broca?", "(200+199)//200", "Se divide entre lo que alcanza cada broca, redondeando hacia arriba.", " broca"),
        ("=", "{F} ¿Cuántas muelas se usan en el lote, con 250 piezas por muela?", "(50+249)//250", "Se divide entre lo que alcanza cada muela, redondeando hacia arriba.", " muela"),
        ("=", "{F} ¿Cuánto cuesta el taladro por pieza, con 6 minutos a $8.000 la hora?", "6*8000//60", "Se multiplican los minutos por el costo de la hora y se dividen por 60.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto cuesta la rectificadora por pieza, con 7 minutos a $12.000 la hora?", "7*12000//60", "Se multiplican los minutos por el costo de la hora y se dividen por 60.", " pesos de ejemplo"),
        ("abc", "{F} Un jefe dice: «el costo por pieza es solo el de las máquinas». ¿Qué respuesta es correcta?", "Es incompleto: faltan las brocas y las muelas y la chatarra", "Es correcto, porque las herramientas no se desgastan", "Es correcto, si las piezas son pocas", "Las herramientas también tienen un costo."),
        ("=", "{F} ¿Cuántas piezas buenas tiene el lote?", "50-2", "Se restan las defectuosas.", " piezas"),
        ("Un taladro de ejemplo cuesta $6.000 la hora y una pieza ocupa 30 minutos. ¿Cuánto cuesta la pieza?", "$3.000", "30 minutos son media hora y la mitad de 6.000 son 3.000."),
    ],
    ctx=("abc", "El cliente de ejemplo pide un precio por pieza y el jefe solo suma el costo de las máquinas. ¿Qué propones?", "Calcular también las herramientas y la chatarra para no vender bajo el costo real", "Dar el precio sin herramientas", "Cobrar solo el material", "El costo real incluye herramientas y pérdidas."),
    sc=[
        ("En Máquinas-Herramientas: ¿cuántas brocas de 120 agujeros se usan para 300 agujeros?", "3", "Dos alcanzan para 240 agujeros y sobran 60 agujeros."),
        ("En Máquinas-Herramientas: ¿qué se suma al tiempo de cada pieza además del trabajo?", "El tiempo de colocar y retirar", "En este caso, ese tiempo ocupa la máquina."),
        ("En Máquinas-Herramientas: ¿qué se resta del lote para tener piezas buenas?", "Las defectuosas", "En este caso, las defectuosas no se entregan."),
    ],
    op=("Ficha de ejemplo: lote de 40 piezas, cada una con 3 agujeros de 1 minuto y un rectificado de 4 minutos; colocar y retirar, 2 minutos en cada máquina. Taladro: $6.000 la hora; rectificadora: $12.000 la hora. Una broca alcanza para 100 agujeros y cuesta $2.000. Escribe (a) los minutos de taladro por pieza, (b) los minutos de rectificadora por pieza, (c) cuántas brocas se usan, (d) el costo de máquina de una pieza.",
        "(a) 3 + 2 = 5 minutos. (b) 4 + 2 = 6 minutos. (c) 40 × 3 = 120 agujeros; 120 ÷ 100 da 1 con resto, es decir 2 brocas. (d) Taladro: 5 × 6.000 ÷ 60 = 500; rectificadora: 6 × 12.000 ÷ 60 = 1.200; total 1.700 pesos de ejemplo.",
        ["calcula los minutos de cada máquina", "calcula las brocas", "calcula el costo por pieza"],
        ["hoja con las cuatro respuestas"],
        ["olvidar colocar y retirar", "no redondear hacia arriba", "no dividir por 60"],
        "Pregunta: «¿cuántos agujeros hay en total?». Si duda, pídele que multiplique las piezas por los agujeros."),
    reinforce="Inventa una herramienta con su vida y un número de piezas y calcula cuántas herramientas se usan.",
    extend="Explica con un ejemplo por qué el costo de una herramienta debe repartirse entre las piezas.",
)

# ============================================================ OAM-03, clase 5
F = ("Ficha 5 (comparación de dos procesos para un agujero de precisión, de ejemplo). Se pide un agujero de 20 mm con tolerancia de ±10 µm. Proceso P1: taladrado y una terminación fina con una herramienta que logra ±20 µm; 4 minutos por pieza; $1.200 por pieza. "
     "Proceso P2: taladrado y rectificado interior, que logra ±5 µm; 9 minutos por pieza; $3.000 por pieza. Condición obligatoria: lograr la tolerancia pedida. Lote de 100 piezas. Lista de verificación: instrumento con certificado vigente; medición dentro de la tolerancia; registro firmado; residuos gestionados; muela dentro de su velocidad máxima.")
build(
    O3, 5, F,
    use="Aprenderé a comparar dos procesos con una condición obligatoria, a calcular su costo y tiempo para un lote y a verificar la calidad con una lista.",
    prior=["Sé qué es una tolerancia.", "Sé calcular costos y tiempos de un lote.", "Sé qué es una lista de verificación."],
    explain=[
        "Al comparar procesos se descartan primero los que no logran la tolerancia pedida, que es una condición obligatoria. Un proceso que logra ±20 µm no sirve para una exigencia de ±10 µm, aunque sea más rápido y barato. Entre los que cumplen se comparan tiempo y costo por pieza y para el lote completo.",
        "Después de fabricar se verifica la calidad con una lista de verificación: instrumento con certificado vigente, medición dentro de la tolerancia, registro firmado, residuos gestionados y la muela dentro de su velocidad máxima cuando hay rectificado. Una lista incompleta no se firma. La decisión la toma la jefatura y queda por escrito.",
        f"El análisis es de papel con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("condición obligatoria", "requisito que un proceso debe cumplir para ser considerado"), ("proceso", "combinación de máquinas y herramientas para obtener una pieza"), ("tolerancia lograda", "precisión que un proceso es capaz de alcanzar"), ("costo del lote", "costo por pieza por el número de piezas"), ("lista de verificación", "lista de puntos que se comprueban uno a uno")],
    worked=[
        ("Descartar un proceso", "Se pide una tolerancia de ±8 µm y un proceso de ejemplo logra ±15 µm. ¿Se considera?", ["La precisión del proceso es peor que la pedida.", "Se descarta."], "No, se descarta"),
        ("Costo del lote", "Un proceso de ejemplo cuesta $500 por pieza y el lote es de 40 piezas. ¿Cuánto cuesta el lote?", ["Se multiplica el costo por las piezas.", "500 por 40 son 20.000."], "$20.000"),
    ],
    mistakes=[("Elegir el proceso más barato sin revisar si logra la tolerancia.", "No cumple la condición obligatoria.", "Primero descarta los que no logran la tolerancia."),
              ("Firmar la lista con un punto sin comprobar.", "La firma indica que todo se verificó.", "Completa cada punto antes de firmar.")],
    T=[
        ("abc", "En Máquinas-Herramientas: ¿qué es una condición obligatoria al comparar procesos?", "Un requisito que el proceso debe cumplir para ser considerado", "El criterio de menor importancia", "El proceso más rápido", "Si no se cumple, el proceso se descarta."),
        ("abc", "En Máquinas-Herramientas: ¿qué es la tolerancia lograda de un proceso?", "La precisión que es capaz de alcanzar", "La tolerancia pedida en el plano", "El tiempo de cada pieza", "Mide qué tan preciso es el proceso."),
        ("abc", "En Máquinas-Herramientas: ¿cuándo se firma una lista de verificación?", "Cuando todos los puntos están comprobados", "Cuando se termina el turno", "Cuando falta solo un punto", "La firma exige que todo esté verificado."),
        ("abc", "{F} ¿Qué proceso cumple la tolerancia de ±10 µm?", "P2, que logra ±5 µm", "P1, que logra ±20 µm", "Ambos", "P1 no alcanza la precisión pedida."),
        ("=", "{F} ¿Cuántos µm de tolerancia logra P2 más estrecha que la pedida?", "10-5", "Se resta la tolerancia lograda a la pedida.", " µm"),
        ("=", "{F} ¿Cuántos minutos más toma P2 por pieza que P1?", "9-4", "Se resta el tiempo de P1 al de P2.", " minutos"),
        ("=", "{F} ¿Cuánto cuesta el lote de 100 piezas con P2?", "100*3000", "Se multiplica el costo por pieza por el lote.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto cuesta el lote con P1?", "100*1200", "Se multiplica el costo por pieza por el lote.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántos pesos de ejemplo más cuesta el lote con P2 que con P1?", "100*3000-100*1200", "Se resta el costo del lote con P1 al del lote con P2.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuántos minutos toma el lote de 100 piezas con P2?", "100*9", "Se multiplican las piezas por los minutos de cada una.", " minutos"),
        ("abc", "{F} Un jefe dice: «usemos P1, que es más barato y rápido». ¿Qué respuesta es correcta?", "No corresponde: P1 no logra la tolerancia de ±10 µm y se descarta", "Corresponde, porque ahorra dinero", "Corresponde, si los clientes no miden", "La condición obligatoria se aplica antes del costo."),
        ("abc", "{F} Falta firmar el registro de la medición y el resto cumple. ¿Qué corresponde con la lista?", "No firmarla hasta completar el punto del registro", "Firmarla porque el resto cumple", "Borrar el punto", "Una lista incompleta no se firma."),
        ("Un proceso de ejemplo logra ±12 µm y otro ±6 µm. La tolerancia pedida es de ±8 µm. ¿Cuál cumple?", "El de ±6 µm", "Solo el de ±6 µm es más preciso que ±8 µm."),
    ],
    ctx=("abc", "Un cliente de ejemplo apura y propone aceptar piezas fuera de tolerancia por un descuento. ¿Qué propones?", "Informar el estado real y no entregar piezas fuera de tolerancia sin una decisión formal", "Entregarlas con descuento", "Cambiar el plano sin avisar", "La tolerancia del plano no se negocia por descuentos."),
    sc=[
        ("En Máquinas-Herramientas: ¿qué se hace primero al comparar procesos?", "Descartar los que no logran la tolerancia pedida", "Después se comparan costos y tiempos."),
        ("En Máquinas-Herramientas: ¿cuánto cuesta un lote de 30 piezas a $400 cada una?", "$12.000", "Se multiplica el costo por las piezas."),
        ("En Máquinas-Herramientas: ¿qué hacer si falta un punto de la lista de verificación?", "No firmarla hasta completarlo", "La firma indica que todo se verificó."),
    ],
    op=("Ficha de ejemplo: se pide un agujero con tolerancia de ±6 µm. Proceso X: logra ±12 µm, 3 minutos y $800 por pieza. Proceso Y: logra ±4 µm, 8 minutos y $2.500 por pieza. Lote de 50 piezas. Escribe (a) qué proceso cumple y por qué, (b) el costo del lote con ese proceso, (c) los minutos del lote con ese proceso, (d) qué compruebas al terminar con la lista de verificación.",
        "(a) Y, porque logra ±4 µm, mejor que los ±6 µm pedidos; X se descarta. (b) 50 × 2.500 = 125.000 pesos de ejemplo. (c) 50 × 8 = 400 minutos. (d) Instrumento con certificado vigente, medición dentro de la tolerancia, registro firmado, residuos gestionados y velocidad de la muela dentro del máximo.",
        ["elige el proceso con razón", "calcula el costo", "calcula los minutos", "usa la lista de verificación"],
        ["hoja con las cuatro respuestas"],
        ["elegir por precio", "no calcular el lote", "firmar sin verificar"],
        "Pregunta: «¿qué proceso logra la tolerancia pedida?». Si duda, pídele que compare las tolerancias."),
    reinforce="Inventa dos procesos con tolerancia lograda, tiempo y costo, y elige uno para una exigencia dada.",
    extend="Explica con un ejemplo por qué un proceso más barato que no logra la tolerancia no sirve.",
)
