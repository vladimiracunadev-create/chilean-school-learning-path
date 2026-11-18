"""Mecánica Industrial (tronco) TP 3.º medio: OAE-01 (leer planos, especificaciones y simbología), OAE-02 (mediciones y controles) y OAE-03 (corte y soldadura, solo conceptos y documentos). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_mein_common import AVISO, EMER, build

O1 = "TP-MEIN-3-OAE-01"
O2 = "TP-MEIN-3-OAE-02"
O3 = "TP-MEIN-3-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Taller Demo» fabrica soportes de acero para cintas transportadoras. Su matriz de peligros anota: ruido de una máquina, chispas y partículas metálicas, "
     "piezas pesadas que se mueven con un puente grúa, aceite derramado en el piso, bordes filosos de las planchas y partes giratorias sin protección. Dotación del turno de día: 18 personas.")
build(
    O1, 1, F,
    use="Aprenderé qué trabajos reúne la mecánica industrial, qué peligros típicos tiene un taller metalmecánico y cómo se ordenan las medidas de prevención.",
    prior=["Sé leer una tabla sencilla.", "Sé multiplicar y dividir números enteros.", "Sé que un taller sigue reglas escritas."],
    explain=[
        "La mecánica industrial reúne la fabricación, el mantenimiento y la reparación de piezas y de conjuntos mecánicos, que son varias piezas unidas que cumplen una función en conjunto. Se trabaja en talleres y plantas del sector metalmecánico, siempre guiados por planos y especificaciones técnicas. Un taller anota sus peligros en una matriz de peligros, una tabla que los lista junto a sus medidas de control.",
        "Un peligro es una fuente que puede causar daño y el riesgo es la posibilidad de que ese daño ocurra. La matriz de ejemplo puede puntuar el riesgo multiplicando la probabilidad (de 1 a 5) por la gravedad (de 1 a 5). Las medidas se ordenan en la jerarquía de controles, de la más a la menos efectiva: eliminar, sustituir, controles de ingeniería (como un resguardo, una barrera física que impide tocar una parte peligrosa), controles administrativos (reglas, señales, permisos) y, al final, el equipo de protección personal (EPP).",
        f"La Dirección del Trabajo fiscaliza que se cumpla la normativa laboral. {EMER} {AVISO}",
    ],
    vocab=[("mecánica industrial", "fabricación, mantenimiento y reparación de piezas y conjuntos mecánicos"), ("conjunto mecánico", "varias piezas unidas que cumplen una función en conjunto"), ("matriz de peligros", "tabla que lista los peligros de un lugar y sus medidas de control"), ("resguardo", "barrera física que impide el contacto con una parte peligrosa"), ("jerarquía de controles", "orden de las medidas de prevención, de la más a la menos efectiva"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Peligro y riesgo", "En un taller de ejemplo hay una manguera de aire tendida en el pasillo. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la manguera tendida, que puede causar daño.", "El riesgo es que alguien tropiece y se lesione."], "Peligro: la manguera tendida; riesgo: que alguien tropiece y se lesione"),
        ("Tipo de control", "Una polea de ejemplo gira sin cubierta y se le instala una cubierta fija. ¿Qué tipo de control es?", ["La cubierta es una barrera física que cambia el lugar.", "Una barrera física es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Creer que con casco y guantes basta para manejar cualquier equipo del taller.", "El EPP es la última barrera y no reemplaza la formación ni la autorización.", "Primero se controla el peligro; el equipo lo maneja personal autorizado."),
              ("Llamar «riesgo» al objeto que puede dañar.", "El objeto es el peligro; el riesgo es la posibilidad de daño.", "Nombra primero el peligro y luego cuál es el daño posible.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué trabajos reúne esta especialidad?", "Fabricar, mantener y reparar piezas y conjuntos mecánicos", "Solo fabricar piezas nuevas, sin mantener ni reparar", "Diseñar edificios y calcular sus fundaciones", "La especialidad abarca fabricación, mantenimiento y reparación; las otras opciones recortan o cambian el oficio."),
        ("abc", "En Mecánica Industrial: ¿qué es un resguardo?", "Una barrera física que impide el contacto con una parte peligrosa", "Un cartel que prohíbe acercarse a una parte peligrosa", "Un permiso firmado para trabajar cerca de una parte peligrosa", "El resguardo es una barrera física; el cartel y el permiso son controles administrativos."),
        ("abc", "En Mecánica Industrial: ¿qué es una matriz de peligros?", "Una tabla que lista los peligros de un lugar y sus medidas de control", "Un plano que muestra la ubicación de las máquinas", "Una lista de las personas autorizadas para trabajar", "La matriz de peligros ordena peligros y controles; no es un plano ni una nómina."),
        ("abc", "{F} De los peligros de la matriz, ¿cuál se previene mejor con un resguardo?", "Las partes giratorias sin protección", "El aceite derramado en el piso", "El ruido de una máquina", "Un resguardo impide tocar una parte giratoria; el aceite y el ruido se controlan de otra manera."),
        ("abc", "{F} El taller entrega protectores auditivos a quienes trabajan cerca de la máquina ruidosa. ¿En qué nivel de la jerarquía de controles está esa medida?", "En el EPP, el último nivel", "En los controles de ingeniería", "En la eliminación del peligro", "Los protectores auditivos protegen a quien los usa y no quitan el ruido, por eso son EPP."),
        ("abc", "{F} Sobre el aceite derramado en el piso, ¿qué afirmación distingue bien peligro y riesgo?", "El peligro es el aceite derramado y el riesgo es que alguien resbale y se lesione", "El peligro es que alguien resbale y el riesgo es el aceite derramado", "Peligro y riesgo significan lo mismo", "El peligro es la fuente y el riesgo es la posibilidad del daño."),
        ("=", "{F} El taller asigna 1 persona monitora de seguridad por cada 6 personas de la dotación. ¿Cuántas monitoras corresponden?", "18//6", "Se divide la dotación entre las personas que cubre cada monitora.", " monitoras"),
        ("=", "La matriz de ejemplo puntúa el riesgo como probabilidad por gravedad. Un peligro tiene probabilidad 3 y gravedad 4. ¿Qué puntaje obtiene?", "3*4", "Se multiplican la probabilidad y la gravedad.", " puntos"),
        ("abc", "{F} Para el peligro de las piezas pesadas que se mueven con puente grúa, ¿cuál es un control administrativo?", "Una señal y una regla de no pasar bajo la carga", "Una barrera fija que impide el paso", "Un casco para cada persona de la zona", "Una señal y una regla ordenan la conducta; la barrera es de ingeniería y el casco es EPP."),
        ("abc", "{F} Un aprendiz dice: «tengo casco y guantes, ya puedo manejar el puente grúa». ¿Qué respuesta es correcta?", "Es falso: manejar equipos de izaje exige formación, autorización y norma vigente, y el EPP no lo reemplaza", "Es cierto, porque el EPP lo protege de todo riesgo", "Es cierto, si otra persona lo observa", "Usar EPP no habilita para operar equipos; la autorización y la formación son aparte."),
        ("abc", "En una visita a un taller de ejemplo, una persona queda con una mano atrapada en una parte giratoria. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar detener la máquina por tu cuenta", "Tirar del brazo de la persona para soltarla", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("=", "Un peligro de ejemplo tiene probabilidad 4 y gravedad 5. Tras instalar un resguardo, la probabilidad baja a 1 y la gravedad sigue igual. ¿Cuántos puntos baja el puntaje?", "4*5-1*5", "Se calcula el puntaje antes y después, y se resta.", " puntos"),
        ("abc", "¿Qué institución fiscaliza el cumplimiento de la normativa laboral en un taller?", "La Dirección del Trabajo", "El Servicio de Impuestos Internos", "El Instituto Nacional de Estadísticas", "La Dirección del Trabajo fiscaliza lo laboral; las otras instituciones tienen funciones tributarias y estadísticas."),
    ],
    ctx=("abc", "El dueño de un taller de ejemplo te dice: «ponte unos guantes y ayúdame con la máquina, tú ya sabes leer planos». ¿Qué respondes?", "Que no, porque operar una máquina exige instructor autorizado y norma vigente, y que consultarás a un adulto responsable", "Que sí, porque con guantes basta", "Que sí, pero solo si la máquina trabaja despacio", "Leer planos y usar guantes no habilitan para operar una máquina."),
    sc=[
        ("En Mecánica Industrial: ¿qué es un peligro?", "Una fuente que puede causar daño, como una pieza pesada suspendida", "El peligro es la fuente; el riesgo es la posibilidad de daño."),
        ("En Mecánica Industrial: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("¿Qué tipo de control es un resguardo?", "Un control de ingeniería", "El resguardo cambia el lugar con una barrera física."),
    ],
    op=("El «Taller Demo» anota una tarea de ejemplo: cambiar la correa de una máquina que tiene una polea giratoria sin protección. Escribe (a) cuál es el peligro y cuál el riesgo, (b) un control de ingeniería, (c) un control administrativo, (d) por qué el EPP no basta por sí solo. No describas cómo se hace la tarea: la hace personal autorizado.",
        "(a) Peligro: la polea giratoria sin protección; riesgo: que una mano o la ropa quede atrapada y cause una lesión. (b) Instalar un resguardo fijo sobre la polea. (c) Una señal de advertencia y la regla de que solo personal autorizado interviene. (d) Porque el EPP es la última barrera: no quita el peligro y solo protege a quien lo usa.",
        ["distingue peligro y riesgo", "propone un control de ingeniería", "propone un control administrativo", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la polea", "proponer solo el EPP", "describir cómo se hace la tarea"],
        "Pregunta: «¿qué medida quitaría el contacto con la polea?». Si no responde, pídele que relea la definición de resguardo."),
    reinforce="Escribe los cinco niveles de la jerarquía de controles en orden y pon junto a cada uno un ejemplo inventado de taller.",
    extend="Explica con un ejemplo por qué un cartel de advertencia no reemplaza a un resguardo.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (lámina descrita por escrito, de ejemplo, inventada). Lámina T-02 «Soporte de rodillo», escala 1:2, revisión B (la revisión A es una copia antigua que sigue en el archivo). Vistas: frontal, superior y lateral. "
     "Lista de piezas: pieza 1, base (1 unidad); pieza 2, costilla (2 unidades); pieza 3, eje (1 unidad); pieza 4, tornillo (4 unidades). Cota del largo de la base: 80 mm. Rótulo: dibujó «Dibujante Demo»; aprobó «Jefatura Demo».")
build(
    O1, 2, F,
    use="Aprenderé los tipos de plano de un taller, qué dice el rótulo y la lista de piezas, cómo pasar de la escala a la medida real y qué función cumple cada rol.",
    prior=["Sé que un plano es un dibujo técnico.", "Sé multiplicar y dividir números enteros.", "Sé leer una lista con cantidades."],
    explain=[
        "Un plano de conjunto muestra cómo se arman varias piezas; un plano de despiece muestra cada pieza por separado; un plano de taller trae cotas y tolerancias para fabricar una pieza. Las vistas (frontal, superior y lateral) muestran la pieza desde distintos lados. El rótulo es el recuadro con el nombre de la lámina, la escala, la revisión y las firmas, y la lista de piezas anota cada pieza con su cantidad.",
        "La escala 1:2 significa que el dibujo mide la mitad de la pieza real; la escala 1:5, la quinta parte. La cota es la medida real escrita sobre el dibujo y manda sobre lo que se mide con una regla en el papel. La revisión se marca con letras que avanzan (A, B, C) cada vez que el plano cambia, y solo sirve la vigente, que es la más reciente. Un error no se corrige por cuenta propia: se consulta a quien dibujó o aprobó.",
        f"El dibujante emite los planos, la jefatura de taller organiza el trabajo, el control de calidad verifica que lo fabricado cumpla el plano y el personal autorizado ejecuta las tareas. {EMER} {AVISO}",
    ],
    vocab=[("plano de conjunto", "muestra cómo se arman varias piezas"), ("plano de despiece", "muestra cada pieza por separado"), ("plano de taller", "trae cotas y tolerancias para fabricar una pieza"), ("rótulo", "recuadro con nombre, escala, revisión y firmas de la lámina"), ("cota", "medida real escrita sobre el dibujo"), ("escala", "relación entre el tamaño del dibujo y el real"), ("revisión", "letra que indica la versión del plano")],
    worked=[
        ("Pasar a la medida real", "Un dibujo a escala 1:5 muestra un tramo de 30 mm. ¿Cuántos mm reales mide?", ["La escala 1:5 multiplica por 5 la medida del dibujo.", "30 por 5 son 150."], "150 mm"),
        ("Sumar una lista", "Una lista de ejemplo dice: pieza 7 (3 unidades) y pieza 8 (6 unidades). ¿Cuántas unidades suma?", ["Se suman las cantidades de las dos piezas.", "3 más 6 son 9."], "9 unidades"),
    ],
    mistakes=[("Tomar la medida del dibujo con regla y usarla como medida de la pieza.", "A escala distinta de 1:1 el dibujo no mide lo mismo que la pieza.", "Usa la cota escrita o multiplica por la escala."),
              ("Usar la copia de la revisión A porque «siempre se hizo así».", "La revisión vigente es la más reciente y la A puede estar superada.", "Confirma la revisión en el rótulo y descarta las antiguas.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es un plano de despiece?", "Un plano que muestra cada pieza por separado", "Un plano que muestra el conjunto ya armado", "Un plano que muestra la ubicación de las máquinas del taller", "El despiece separa las piezas; el conjunto las muestra armadas."),
        ("abc", "En Mecánica Industrial: ¿qué indica una cota escrita en un plano de taller?", "La medida real de la pieza", "La medida del dibujo en el papel", "La revisión del plano", "La cota es la medida real y por eso manda sobre la regla."),
        ("abc", "En Mecánica Industrial: ¿qué datos trae el rótulo de una lámina?", "Nombre, escala, revisión y firmas", "Solo las cotas de cada pieza", "El precio y el plazo de entrega", "El rótulo identifica la lámina; las cotas van en el dibujo."),
        ("=", "{F} ¿Cuántas unidades suma la lista de piezas?", "1+2+1+4", "Se suman las cantidades de las cuatro piezas.", " unidades"),
        ("abc", "{F} ¿Qué documento de la lámina permite saber cuántos tornillos lleva el soporte?", "La lista de piezas", "El rótulo", "La vista superior", "La cantidad de cada pieza está anotada en la lista de piezas."),
        ("abc", "{F} Hay dos copias de la lámina T-02. ¿Cuál corresponde usar?", "La revisión B, porque es la más reciente", "La revisión A, porque se emitió primero y ya se usó", "Ambas, tomando de cada una la medida que convenga", "Solo sirve la revisión vigente; mezclar versiones lleva a errores."),
        ("=", "{F} La costilla mide 22 mm de alto en el dibujo. ¿Cuántos mm mide en la pieza real?", "22*2", "A escala 1:2 la medida real es el doble de la del dibujo.", " mm"),
        ("=", "Un eje dibujado a escala 1:10 mide 45 mm en la lámina. ¿Cuántos mm reales mide?", "45*10", "La escala 1:10 multiplica por 10 la medida del dibujo.", " mm"),
        ("abc", "{F} Una persona necesita ver cómo se arman las cuatro piezas entre sí. ¿Qué tipo de plano necesita?", "Uno de conjunto", "Uno de taller de una sola pieza", "Solo la lista de piezas", "El plano de conjunto muestra el armado de varias piezas."),
        ("abc", "{F} Un compañero dice: «mi regla mide 40 mm en el dibujo de la base, así que la base mide 40 mm». ¿Qué respuesta es correcta?", "Es falso: a escala 1:2 el dibujo mide la mitad, y la cota de 80 mm es la medida real", "Es cierto, porque la regla es más exacta que la cota", "Es cierto, porque la escala solo sirve para dibujar", "La cota manda y a escala 1:2 el dibujo es la mitad de la pieza."),
        ("abc", "{F} La lámina nombra la pieza 3 como «eje», pero otra lista del taller la nombra «pasador». ¿Qué corresponde?", "Registrar la diferencia y consultarla a quien dibujó o aprobó, sin cambiarla por cuenta propia", "Elegir el nombre que parezca más lógico", "Usar siempre la otra lista, porque es más nueva", "Una discrepancia se consulta con quien emitió el plano."),
        ("=", "{F} Para fabricar 6 soportes iguales se necesitan los tornillos de la pieza 4 de cada soporte y 3 tornillos de repuesto. ¿Cuántos tornillos se necesitan?", "6*4+3", "Se multiplican los soportes por los tornillos de cada uno y se suman los de repuesto.", " tornillos"),
        ("abc", "En Mecánica Industrial: ¿quién emite el plano y quién verifica que la pieza fabricada lo cumpla?", "El dibujante emite el plano y el control de calidad verifica la pieza", "El control de calidad emite el plano y el dibujante verifica la pieza", "El personal que fabrica emite el plano y verifica la pieza", "Cada rol cumple una función distinta: emitir y verificar no recaen en la misma persona."),
    ],
    ctx=("abc", "Una persona del taller de ejemplo dice: «ese plano está viejo, yo fabrico con lo que recuerdo». Como estudiante, ¿qué propones?", "Pedir la revisión vigente y trabajar con el documento actualizado", "Aceptarlo porque tiene experiencia", "Dibujar un plano nuevo de memoria para que el equipo lo use", "Los planos se usan en su revisión vigente, no de memoria."),
    sc=[
        ("En Mecánica Industrial: ¿qué dato manda si la cota y la regla no coinciden?", "La cota escrita", "La cota es la medida real; el dibujo puede estar a escala."),
        ("¿Qué indica la letra de revisión?", "La versión del plano", "Permite saber cuál es la versión vigente."),
        ("¿Qué muestra un plano de conjunto?", "Cómo se arman varias piezas", "El conjunto muestra el armado; el despiece muestra las piezas separadas."),
    ],
    op=("Ficha de ejemplo: lámina T-05 «Tapa de caja», escala 1:5, revisión A. Lista de piezas: pieza 1, tapa (1 unidad); pieza 2, perno (6 unidades). El largo de la tapa mide 24 mm en el dibujo. Escribe (a) qué tipo de plano es, si muestra cada pieza por separado, (b) el largo real de la tapa, (c) cuántas unidades suma la lista, (d) a quién se consulta si una cota parece equivocada.",
        "(a) Un plano de despiece. (b) 24 × 5 = 120 mm. (c) 1 + 6 = 7 unidades. (d) A quien dibujó o aprobó el plano, sin corregirlo por cuenta propia.",
        ["identifica el tipo de plano", "calcula la medida real", "suma las unidades", "indica a quién consulta"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar por una escala equivocada", "sumar mal las unidades", "corregir la cota por cuenta propia"],
        "Pregunta: «¿la medida del dibujo es la medida de la pieza?». Si responde que sí, pídele que relea qué significa la escala."),
    reinforce="Inventa una lista de tres piezas con sus cantidades y súmalas; luego inventa una escala y una medida de dibujo y calcula la medida real.",
    extend="Explica con un ejemplo por qué el dibujante y el control de calidad no cumplen la misma función.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (lecturas de ejemplo, inventadas; las tomó personal autorizado). Unidad: 1 mm = 1.000 µm (micrones). Plano: eje de diámetro 25.000 µm con tolerancia de ±30 µm (se acepta entre 24.970 y 25.030). "
     "Lectura A, con pie de metro análogo (resolución 20 µm): 25.020 µm. Lectura B, con micrómetro digital (resolución 10 µm) de certificado vigente: 25.040 µm. "
     "Lectura C, con un pie de metro digital de certificado vencido: 24.990 µm. Símbolos de la lámina: Ø = diámetro; M = rosca métrica; Ra = rugosidad, es decir el acabado de la superficie.")
build(
    O1, 3, F,
    use="Aprenderé a leer símbolos de un plano, a distinguir instrumentos análogos y digitales y a juzgar si una lectura es confiable por su resolución y su certificado.",
    prior=["Sé qué es una tolerancia.", "Sé restar y comparar números enteros.", "Sé que 1 mm tiene 1.000 µm."],
    explain=[
        "Los planos usan símbolos: Ø indica un diámetro, M una rosca métrica y Ra la rugosidad, que describe qué tan lisa es una superficie. Un instrumento análogo, como un pie de metro con escala, se lee viendo en qué marca queda la medida; uno digital muestra un número en una pantalla. La resolución es la menor variación que el instrumento puede mostrar, y mirar una escala de lado produce el error de paralaje.",
        "La calibración compara un instrumento con un patrón y deja constancia en un certificado de calibración con fecha de vigencia. Una lectura de un instrumento con certificado vencido queda en duda y no sirve en un control formal, aunque la pantalla sea digital. Las medidas finas se expresan en micrones (µm): 1 mm son 1.000 µm. Cada lectura se registra con instrumento, fecha, quién la tomó y unidad.",
        f"Las lecturas las toma personal autorizado y capacitado; aquí solo se aprende a leerlas y juzgarlas en papel. {EMER} {AVISO}",
    ],
    vocab=[("Ø", "símbolo de diámetro"), ("Ra", "valor de la rugosidad, es decir del acabado de una superficie"), ("instrumento análogo", "muestra la medida sobre una escala"), ("instrumento digital", "muestra la medida como número en una pantalla"), ("resolución", "menor variación que un instrumento puede mostrar"), ("certificado de calibración", "documento con el error del instrumento y su vigencia"), ("micrón (µm)", "milésima parte de un milímetro")],
    worked=[
        ("Aplicar la tolerancia", "Un diámetro de ejemplo debe ser 40.000 µm con tolerancia de ±50 µm y se lee 40.035 µm. ¿Cumple?", ["La diferencia es 40.035 menos 40.000, es decir 35 µm.", "35 es menor que 50: cumple."], "Sí, cumple"),
        ("Pasar de mm a µm", "Un largo de ejemplo es de 12 mm. ¿Cuántos µm son?", ["1 mm tiene 1.000 µm.", "12 por 1.000 son 12.000."], "12.000 µm"),
    ],
    mistakes=[("Creer que un número digital siempre es exacto.", "El instrumento digital tiene resolución limitada y puede tener un certificado vencido.", "Revisa la resolución y el certificado antes de confiar en la lectura."),
              ("Leer una escala análoga mirándola de lado.", "El paralaje cambia la lectura sin que cambie la pieza.", "Quien mide se ubica de frente a la escala; tú aprende el concepto y registra el dato.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es la resolución de un instrumento de medición?", "La menor variación que puede mostrar", "El valor más grande que puede medir", "El tiempo que dura su batería", "La resolución es el escalón mínimo de lectura; el máximo medible es otra característica."),
        ("abc", "En Mecánica Industrial: ¿qué indica el símbolo Ø en un plano?", "Un diámetro", "Un radio", "Una rosca métrica", "Ø es el símbolo de diámetro; la rosca se marca con M."),
        ("abc", "En Mecánica Industrial: ¿qué es el error de paralaje?", "El error de lectura por mirar la escala desde un lado", "La diferencia entre la medida y el valor del plano", "El error por usar un instrumento sin calibrar", "El paralaje nace del ángulo de la mirada; los otros errores tienen otra causa."),
        ("=", "{F} ¿Cuántos µm de diferencia hay entre la lectura A y el valor del plano?", "25020-25000", "Se resta el valor del plano a la lectura A.", " µm"),
        ("abc", "{F} Considerando solo la diferencia con el plano, ¿qué lectura supera la tolerancia?", "La lectura B", "La lectura A", "La lectura C", "B se aparta 40 µm del plano, A se aparta 20 µm y C se aparta 10 µm."),
        ("abc", "{F} ¿Por qué la lectura C no se acepta como evidencia en un control formal?", "Porque su instrumento tiene el certificado de calibración vencido", "Porque los instrumentos digitales no sirven para controles", "Porque su valor es menor que el del plano", "El certificado vencido deja la lectura en duda, sea digital o análoga."),
        ("=", "{F} ¿Cuántos µm vale el límite superior de la tolerancia del eje?", "25000+30", "Se suma la tolerancia al valor del plano.", " µm"),
        ("=", "Una pieza de ejemplo debe medir 60.000 µm con una tolerancia de ±40 µm. ¿Cuántos µm vale su límite inferior?", "60000-40", "Se resta la tolerancia al valor del plano.", " µm"),
        ("abc", "{F} Se repite la lectura C con un instrumento calibrado y da 25.036 µm. ¿Cumple la tolerancia?", "No, porque se aparta 36 µm del plano y la tolerancia es de 30 µm", "Sí, porque 25.036 es muy parecido a 25.000", "Sí, porque el primer valor leído era menor", "La diferencia de 36 µm supera los 30 µm permitidos."),
        ("abc", "{F} Un compañero propone promediar las lecturas A y B para que el eje «cumpla». ¿Qué respuesta es correcta?", "No corresponde: cada lectura se evalúa por separado y la B es una no conformidad que se registra", "Corresponde, porque el promedio es más exacto", "Corresponde, si el promedio cae dentro de la tolerancia", "Promediar oculta una lectura fuera de tolerancia; se evalúa y se registra cada una."),
        ("abc", "En un taller de ejemplo, una partícula de metal salta al ojo de una persona. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Frotarle el ojo para sacar la partícula", "Esperar a ver si el dolor pasa", "Frotar o esperar puede empeorar la lesión; se avisa a quienes pueden actuar."),
        ("Un lote de ejemplo de 10 ejes tiene tolerancia de ±30 µm. Las diferencias medidas con el plano, en µm, son 12, 28, 35, 30, 9, 41, 22, 30, 31 y 18. ¿Cuántos ejes cumplen? Un eje cumple si su diferencia es 30 µm o menos.", "7 ejes", "Cumplen 12, 28, 30, 9, 22, 30 y 18; no cumplen 35, 41 y 31."),
        ("abc", "En Mecánica Industrial: ¿qué datos debe incluir un registro de lectura para ser útil?", "Instrumento, fecha, quién midió, valor y unidad", "Solo el valor leído", "Solo el valor y el nombre de la pieza", "Sin instrumento, fecha, responsable y unidad la lectura no se puede verificar."),
    ],
    ctx=("abc", "Una persona de ejemplo te dice: «usa ese pie de metro digital aunque su certificado esté vencido; la pantalla se ve clara». ¿Qué respondes?", "Que un instrumento con certificado vencido no sirve en un control formal y que mide personal autorizado con uno calibrado", "Que sí, porque una pantalla clara garantiza exactitud", "Que sí, pero anotando una medida menor", "Un certificado vencido deja la lectura en duda, y la pantalla clara no lo corrige."),
    sc=[
        ("En Mecánica Industrial: ¿qué es un instrumento digital?", "El que muestra la medida como un número en pantalla", "El digital muestra un número; el análogo usa una escala."),
        ("En Mecánica Industrial: ¿qué documento dice si un instrumento fue calibrado y hasta cuándo?", "El certificado de calibración", "El certificado deja constancia del error y de la vigencia."),
        ("En Mecánica Industrial: ¿cuántos µm hay en 1 mm de un plano de taller?", "1.000 µm", "El micrón es la milésima parte del milímetro."),
    ],
    op=("Ficha de ejemplo: un eje debe medir 30.000 µm con tolerancia de ±20 µm. Lectura D, con micrómetro digital de certificado vigente: 30.015 µm. Lectura E, con pie de metro digital de certificado vencido: 30.008 µm. Escribe (a) la diferencia de cada lectura con el plano, (b) cuáles cumplen con esos números, (c) qué harías con la lectura E y por qué.",
        "(a) D: 15 µm; E: 8 µm. (b) Ambas están dentro de ±20 µm. (c) La E se registra como dudosa porque su certificado está vencido, y se pide a personal autorizado repetirla con un instrumento calibrado.",
        ["calcula bien las dos diferencias", "compara con la tolerancia", "reconoce el problema del certificado vencido"],
        ["hoja con las diferencias, la comparación y la decisión"],
        ["considerar que la pantalla digital no necesita calibración", "calcular mal la diferencia", "proponer modificar el dato"],
        "Pregunta: «¿qué falta para confiar en la lectura E?». Si no responde, pídele que relea la regla del certificado de calibración."),
    reinforce="Escribe dos diferencias entre un instrumento análogo y uno digital y un riesgo de lectura propio de cada uno.",
    extend="Explica con un ejemplo por qué una lectura sin instrumento, fecha ni unidad no sirve como registro.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (planilla de control de ejemplo, inventada; las medidas las tomó personal autorizado). Regla: una característica cumple si la diferencia entre lo medido y lo del plano es igual o menor que su tolerancia; "
     "la pieza cumple solo si cumplen todas. C1, diámetro de un eje: plano 30.000 µm, tolerancia ±25 µm, medido 30.018 µm. C2, diámetro de un agujero: plano 12.000 µm, tolerancia ±15 µm, medido 12.021 µm. "
     "C3, largo: plano 120.000 µm, tolerancia ±100 µm, medido 119.940 µm. C4, altura: plano 45.000 µm, tolerancia ±40 µm, medido 45.040 µm. C5, rugosidad Ra: máximo permitido 3 unidades de ejemplo, medido 4 unidades de ejemplo.")
build(
    O1, 4, F,
    use="Aprenderé a controlar una pieza con una planilla, a decidir característica por característica si cumple y a registrar una no conformidad sin ocultarla.",
    prior=["Sé restar y comparar números enteros.", "Sé qué es una tolerancia y una cota.", "Sé leer una planilla con varias filas."],
    explain=[
        "Una planilla de control compara, característica por característica, lo medido con lo que manda el plano. Cada característica cumple si la diferencia es igual o menor que su tolerancia; el límite exacto sí cumple. Algunas características, como la rugosidad Ra, no llevan más o menos sino un valor máximo permitido, y cumplen si lo medido no lo supera.",
        "Una pieza cumple solo si todas sus características cumplen: basta una que falle para que la pieza no conforme. Una no conformidad es un resultado que no cumple lo pedido y se registra con el valor medido, la fecha y quien midió. No se promedia con otras características, no se corrige a ojo y se informa al control de calidad.",
        f"Las tolerancias de este cuaderno son de ejemplo; las reales las fija el plano, el fabricante y la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("planilla de control", "tabla donde se anotan lo del plano, lo medido y el resultado"), ("tolerancia", "diferencia máxima aceptada"), ("característica", "dimensión o propiedad de la pieza que se controla"), ("no conformidad", "resultado que no cumple lo pedido"), ("valor máximo permitido", "límite que lo medido no debe superar"), ("control de calidad", "área que verifica que lo fabricado cumpla el plano")],
    worked=[
        ("Aplicar el límite", "Un largo de ejemplo debe ser 80.000 µm con tolerancia de ±50 µm y se mide 80.045 µm. ¿Cumple?", ["La diferencia es 45 µm.", "45 es menor que 50: cumple."], "Sí, cumple"),
        ("Decidir sobre la pieza", "Una pieza de ejemplo tiene 4 características y 3 cumplen. ¿La pieza cumple?", ["La pieza cumple solo si cumplen todas.", "Una característica falla."], "No, la pieza no cumple"),
    ],
    mistakes=[("Aprobar la pieza porque la mayoría de las características cumple.", "Basta una característica fuera de tolerancia para que la pieza no cumpla.", "Revisa todas y registra la que falla."),
              ("Cambiar el valor medido para que entre en tolerancia.", "Se oculta un problema real y se pierde la trazabilidad del registro.", "Anota el valor real y registra la no conformidad.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿cuándo cumple una característica con tolerancia?", "Cuando la diferencia entre lo medido y el plano es igual o menor que la tolerancia", "Cuando lo medido es exactamente igual al plano", "Cuando la mayoría de las demás características cumple", "El límite de la tolerancia sí cumple; no se exige coincidir exacto."),
        ("abc", "En Mecánica Industrial: ¿qué es una no conformidad?", "Un resultado que no cumple lo pedido", "Una pieza que aún no se ha medido", "Una tolerancia más amplia que la normal", "La no conformidad es un incumplimiento que se registra."),
        ("abc", "En Mecánica Industrial: ¿cuándo cumple una pieza con varias características controladas?", "Cuando cumplen todas sus características", "Cuando cumple más de la mitad", "Cuando cumple la característica más importante", "Basta una característica que falle para que la pieza no cumpla."),
        ("=", "{F} ¿Cuántos µm de diferencia hay entre lo medido y el plano en el agujero C2?", "12021-12000", "Se resta el valor del plano al medido.", " µm"),
        ("abc", "{F} ¿Qué dos características no cumplen?", "C2 y C5", "C3 y C4", "C1 y C2", "C2 se aparta 21 µm con tolerancia 15, y C5 supera el máximo de Ra."),
        ("abc", "{F} La característica C4 se aparta exactamente 40 µm y su tolerancia es de 40 µm. ¿Cumple?", "Sí, porque el límite de la tolerancia sí cumple", "No, porque la diferencia debe ser estrictamente menor que la tolerancia", "No, porque todo valor distinto del plano falla", "La regla dice igual o menor que la tolerancia."),
        ("=", "{F} ¿Cuántos µm vale el límite inferior aceptado del largo C3?", "120000-100", "Se resta la tolerancia al valor del plano.", " µm"),
        ("=", "{F} ¿Cuántas características cumplen en total?", "5-2", "Son cinco características y dos no cumplen.", " características"),
        ("=", "En otra planilla de ejemplo, una altura debe ser 70.000 µm con tolerancia de ±35 µm. ¿Cuántos µm vale su límite superior?", "70000+35", "Se suma la tolerancia al valor del plano.", " µm"),
        ("abc", "{F} Un compañero dice: «cuatro de cinco cumplen, así que la pieza cumple». ¿Qué respuesta es correcta?", "Es falso: solo cumplen tres de cinco, y basta una que falle para que la pieza no cumpla", "Es cierto, porque la mayoría cumple", "Es cierto, si las que fallan son las menos importantes", "La pieza cumple solo si todas las características cumplen."),
        ("abc", "{F} Para que la pieza entre en tolerancia, alguien propone anotar 12.010 µm en lugar de 12.021 µm en el agujero. ¿Qué corresponde?", "No se anota un valor falso: se registra la medida real y la no conformidad", "Se anota el valor menor porque la diferencia es pequeña", "Se anota el promedio con el eje C1", "Cambiar un valor medido oculta un problema y rompe el registro."),
        ("Se inspeccionan 24 piezas de ejemplo y se rechazan 6. Con las piezas aprobadas se arman conjuntos de 3 piezas cada uno. ¿Cuántos conjuntos se arman?", "6 conjuntos", "Se aprueban 24 menos 6, es decir 18 piezas, y 18 dividido en 3 son 6 conjuntos."),
        ("En una planilla de ejemplo, el valor máximo permitido de Ra es 5 unidades de ejemplo. Tres piezas miden 4, 5 y 6 unidades de ejemplo. ¿Cuántas piezas cumplen?", "2 piezas", "Cumplen las que no superan 5: la de 4 y la de 5; la de 6 supera el máximo."),
    ],
    ctx=("abc", "El jefe de taller de ejemplo te dice: «si falta poco, anota que cumple y listo». ¿Qué respondes?", "Que se anota el valor medido real y la no conformidad, y que se informa al control de calidad", "Que sí, porque falta poco", "Que sí, pero solo si es la última pieza del lote", "El registro debe reflejar lo medido, aunque falle por poco."),
    sc=[
        ("En Mecánica Industrial: ¿qué se compara en una planilla de control?", "Lo medido con lo que manda el plano", "La planilla contrasta valor medido y valor del plano."),
        ("¿Qué se hace con una no conformidad?", "Se registra con su valor y se informa al control de calidad", "Ocultarla impide corregir la causa del problema."),
        ("¿Cuántas características deben cumplir para que la pieza cumpla?", "Todas", "Basta una fuera de tolerancia para que la pieza no cumpla."),
    ],
    op=("Ficha de ejemplo: planilla de una pieza con tres características. D1, diámetro: plano 20.000 µm, tolerancia ±20 µm, medido 20.012 µm. D2, largo: plano 90.000 µm, tolerancia ±60 µm, medido 90.075 µm. D3, rugosidad Ra: máximo permitido 3 unidades de ejemplo, medido 2. Escribe (a) la diferencia de D1 y de D2, (b) si cada característica cumple, (c) si la pieza cumple y qué se registra.",
        "(a) D1: 12 µm; D2: 75 µm. (b) D1 cumple (12 es menor o igual que 20); D2 no cumple (75 supera 60); D3 cumple (2 no supera 3). (c) La pieza no cumple porque D2 falla; se registra la no conformidad con el valor medido, la fecha y quién midió.",
        ["calcula bien las diferencias", "decide cada característica", "concluye sobre la pieza completa", "indica qué se registra"],
        ["hoja con las diferencias, las decisiones y el registro"],
        ["aprobar la pieza porque la mayoría cumple", "calcular mal una diferencia", "no registrar la no conformidad"],
        "Pregunta: «¿cuántas características deben cumplir para que la pieza cumpla?». Si no responde, pídele que relea la regla de la planilla."),
    reinforce="Inventa una característica con valor del plano, tolerancia y valor medido, y decide si cumple.",
    extend="Explica con un ejemplo por qué una pieza con cuatro características conformes y una no conforme no se aprueba.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (orden de trabajo de ejemplo, inventada). La orden OT-100 del «Taller Demo» pide verificar cuatro magnitudes de una pieza: largo de una barra, 500 mm; ángulo de un chaflán, 45 grados; masa de la pieza, 12 kg; "
     "temperatura máxima de un rodamiento en funcionamiento, 60 °C. Riesgos anotados en la orden: bordes filosos, piezas pesadas, superficies calientes y partes en movimiento.")
build(
    O2, 1, F,
    use="Aprenderé qué es una magnitud, qué unidades usa el taller, qué riesgos tiene medir y quiénes miden o controlan en una orden de trabajo.",
    prior=["Sé leer una lista con datos.", "Sé que el metro y el kilogramo son unidades.", "Sé sumar y restar números enteros."],
    explain=[
        "Una magnitud es una propiedad que se puede medir, como el largo, el ángulo, la masa, la temperatura, la presión o el tiempo. Cada magnitud se expresa con una unidad: el milímetro (mm) para largos, el grado para ángulos, el kilogramo (kg) para masa, el grado Celsius (°C) para temperatura. Una orden de trabajo es el documento que pide una tarea y lista las magnitudes que hay que verificar.",
        "Verificar es comprobar que una magnitud cumple lo pedido. En el taller hay medidas directas, que se leen en un instrumento, y medidas indirectas, que se calculan a partir de otras. Medir tiene riesgos: bordes filosos, piezas pesadas, superficies calientes y partes en movimiento. Por eso se mide con el equipo detenido y asegurado y lo hace personal autorizado.",
        f"El metrólogo o el inspector de calidad verifica las magnitudes; la jefatura emite la orden; el personal autorizado ejecuta. {EMER} {AVISO}",
    ],
    vocab=[("magnitud", "propiedad que se puede medir"), ("unidad", "patrón con que se expresa una magnitud"), ("orden de trabajo", "documento que pide una tarea y lista lo que se debe verificar"), ("verificar", "comprobar que una magnitud cumple lo pedido"), ("medida directa", "la que se lee en un instrumento"), ("medida indirecta", "la que se calcula a partir de otras medidas")],
    worked=[
        ("Magnitud y unidad", "Una pieza de ejemplo pesa 8 kg. ¿Qué magnitud es y con qué unidad se expresa?", ["Lo que se mide es el peso o masa de la pieza.", "Se expresa en kilogramos."], "Masa, en kg"),
        ("Medida indirecta", "Una placa de ejemplo mide 30 mm de ancho y 20 mm de alto. ¿Cuántos mm cuadrados tiene su superficie?", ["El área de un rectángulo es ancho por alto.", "30 por 20 son 600."], "600 mm cuadrados"),
    ],
    mistakes=[("Medir una pieza mientras la máquina que la sostiene sigue en movimiento.", "Hay riesgo de atrapamiento o de lesión por partes giratorias.", "La medición la hace personal autorizado con el equipo detenido y asegurado."),
              ("Dar una medida sin unidad.", "Sin unidad el número no dice qué se midió.", "Escribe siempre la unidad junto al valor.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es una magnitud?", "Una propiedad que se puede medir, como el largo", "Un instrumento que mide longitudes", "El número que se anota en una planilla", "La magnitud es la propiedad medida; el número y el instrumento son otra cosa."),
        ("abc", "En Mecánica Industrial: ¿qué es una orden de trabajo?", "Un documento que pide una tarea y lista lo que se debe verificar", "Un plano que muestra las piezas de un conjunto", "Un certificado que indica si un instrumento está calibrado", "La orden de trabajo pide y organiza la tarea; el plano y el certificado son otros documentos."),
        ("abc", "En Mecánica Industrial: ¿qué es una medida indirecta?", "La que se calcula a partir de otras medidas", "La que se lee directamente en un instrumento", "La que toma una persona distinta del inspector", "La medida indirecta se calcula, como un área a partir de largo y ancho."),
        ("abc", "{F} ¿Qué magnitud se expresa en grados y se pide para el chaflán?", "El ángulo", "La masa", "La temperatura", "El chaflán se verifica con un ángulo; la masa va en kg y la temperatura en °C."),
        ("abc", "{F} ¿Cuál de las cuatro magnitudes de la orden se expresa en kilogramos?", "La masa de la pieza", "El largo de la barra", "La temperatura del rodamiento", "Los kilogramos son unidad de masa."),
        ("abc", "{F} Entre los riesgos anotados en la orden, ¿cuál se relaciona con medir la temperatura de un rodamiento en funcionamiento?", "Las superficies calientes", "Los bordes filosos", "Las piezas pesadas", "Una superficie caliente puede quemar; los otros riesgos se asocian a otras magnitudes."),
        ("=", "{F} Una barra recta debe medir 500 mm. Se necesitan 7 barras iguales dispuestas una a continuación de otra. ¿Cuántos mm miden en total?", "500*7", "Se multiplica el largo de una barra por el número de barras.", " mm"),
        ("=", "Una placa de ejemplo mide 40 mm de ancho y 25 mm de alto. ¿Cuántos mm cuadrados tiene su superficie?", "40*25", "El área es ancho por alto.", " mm cuadrados"),
        ("=", "{F} La pieza pesa 12 kg y se envían 5 piezas iguales en una caja que pesa 4 kg vacía. ¿Cuántos kg pesa la caja con las piezas?", "12*5+4", "Se multiplican las piezas por su masa y se suma la caja.", " kg"),
        ("abc", "{F} Una persona de ejemplo propone medir el rodamiento en funcionamiento acercando la mano para saber si está a 60 °C. ¿Qué respuesta es correcta?", "No corresponde: la temperatura la verifica personal autorizado con un instrumento adecuado, sin tocar partes calientes ni en movimiento", "Corresponde, porque la mano es un instrumento rápido", "Corresponde, si usa guantes", "Tocar partes calientes o en movimiento es peligroso y no es una medición confiable."),
        ("abc", "{F} Un compañero anota «largo de la barra: 500» sin unidad. ¿Qué observación es correcta?", "Falta la unidad: sin ella no se sabe si son milímetros, centímetros o metros", "Está bien, porque la orden ya la nombra", "Está bien, porque 500 solo puede ser milímetros", "Todo valor medido se anota con su unidad para evitar errores."),
        ("=", "Una orden de ejemplo lista 3 magnitudes por pieza y hay 8 piezas. ¿Cuántas verificaciones se registran en total?", "3*8", "Se multiplica el número de magnitudes por el número de piezas.", " verificaciones"),
        ("abc", "Durante una visita a un taller de ejemplo, una pieza pesada cae sobre el pie de una persona. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Levantar la pieza tú mismo para liberar el pie", "Mover a la persona rápido, aunque pueda tener una lesión grave", "Mover piezas o personas sin formación puede agravar la lesión."),
    ],
    ctx=("abc", "En un taller de ejemplo te piden «ayúdame a medir esta pieza con la máquina andando». ¿Qué respondes?", "Que se mide con el equipo detenido y asegurado, y que lo hace personal autorizado", "Que sí, siempre que vayas con cuidado", "Que sí, si la máquina gira despacio", "Una parte en movimiento puede atrapar; la medición la hace personal autorizado con el equipo detenido."),
    sc=[
        ("En Mecánica Industrial: ¿qué es verificar una magnitud?", "Comprobar que cumple lo pedido", "Verificar es contrastar con lo que pide el documento."),
        ("¿Qué unidad se usa para la masa?", "El kilogramo (kg)", "El kilogramo es la unidad de masa."),
        ("¿Qué documento pide una tarea y lista las magnitudes por verificar?", "La orden de trabajo", "La orden organiza qué se debe verificar."),
    ],
    op=("Ficha de ejemplo: la orden OT-120 pide verificar en una pieza el largo de un eje, 200 mm; la masa, 5 kg; y el ángulo de un chaflán, 30 grados. Riesgos anotados: bordes filosos y pieza pesada. Escribe (a) la unidad de cada magnitud, (b) un riesgo de medir esta pieza y un control administrativo para él, (c) quién debe realizar la medición.",
        "(a) Largo: mm; masa: kg; ángulo: grados. (b) Riesgo: cortarse con un borde filoso; control administrativo: una regla escrita de que solo personal autorizado manipula la pieza, con una señal en el puesto. (c) Personal autorizado, con el equipo detenido y asegurado.",
        ["asigna bien las unidades", "relaciona riesgo y control", "indica quién mide"],
        ["hoja con unidades, riesgo con control y responsable"],
        ["olvidar la unidad", "proponer el EPP como único control", "decir que mide cualquier persona"],
        "Pregunta: «¿esa medida es del largo, de la masa o del ángulo?». Si duda, pídele que relea la definición de magnitud."),
    reinforce="Escribe cinco magnitudes que se miden en un taller con la unidad de cada una.",
    extend="Explica con un ejemplo la diferencia entre una medida directa y una indirecta.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (hoja de inspección de ejemplo, inventada). Una barra de referencia mide 100.000 µm según un certificado. El inspector A la midió cinco veces con el mismo instrumento y obtuvo, en µm: 100.012; 100.010; 100.014; 100.011 y 100.013. "
     "El inspector B la midió cinco veces con otro instrumento y obtuvo: 100.002; 99.998; 100.004; 99.996 y 100.000. En la hoja, el rango es el valor mayor menos el menor; el sesgo es el promedio menos el valor de referencia.")
build(
    O2, 2, F,
    use="Aprenderé los documentos de una inspección, qué es exactitud y precisión de una medición y qué hace cada rol.",
    prior=["Sé calcular promedios exactos de números enteros.", "Sé restar números enteros.", "Sé qué es un certificado de calibración."],
    explain=[
        "Una hoja de inspección es el documento donde se anotan las mediciones de una pieza con su fecha, su instrumento y su responsable. Medir varias veces la misma pieza muestra dos cosas. La precisión (o repetibilidad) dice qué tan parecidas son las lecturas entre sí: se mide con el rango, el valor mayor menos el menor. La exactitud dice qué tan cerca está el promedio del valor de referencia: la diferencia se llama sesgo.",
        "Un instrumento puede ser preciso y poco exacto, si sus lecturas se repiten pero todas se desvían del valor de referencia, o exacto y poco preciso, si el promedio es bueno pero las lecturas se dispersan. Un plan de control es el documento que indica qué magnitudes se controlan, con qué instrumento y cada cuánto tiempo.",
        f"El metrólogo calibra y compara instrumentos, el inspector de calidad mide y registra, y la jefatura decide con los registros. {EMER} {AVISO}",
    ],
    vocab=[("hoja de inspección", "documento donde se anotan las mediciones de una pieza"), ("precisión", "qué tan parecidas son las lecturas repetidas entre sí"), ("exactitud", "qué tan cerca está el promedio del valor de referencia"), ("rango", "valor mayor menos valor menor"), ("sesgo", "promedio menos valor de referencia"), ("plan de control", "documento que dice qué se controla, con qué y cada cuánto")],
    worked=[
        ("Calcular el rango", "Un inspector de ejemplo anota, en µm, 50.003; 50.009 y 50.006. ¿Cuál es el rango?", ["El mayor es 50.009 y el menor es 50.003.", "50.009 menos 50.003 son 6."], "6 µm"),
        ("Calcular el sesgo", "Tres lecturas de ejemplo de una pieza de referencia de 20.000 µm son 20.007; 20.008 y 20.006. ¿Cuál es el sesgo?", ["La suma es 60.021 y el promedio es 20.007.", "20.007 menos 20.000 son 7."], "7 µm"),
    ],
    mistakes=[("Creer que una lectura muy repetida es necesariamente exacta.", "Las lecturas pueden repetirse y estar todas desviadas del valor de referencia.", "Calcula el rango para la precisión y el sesgo para la exactitud."),
              ("Confundir el rango con el promedio.", "El rango es mayor menos menor; el promedio es la suma dividida por el número de lecturas.", "Escribe cada fórmula antes de calcular.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué mide la precisión de una serie de mediciones?", "Qué tan parecidas son las lecturas entre sí", "Qué tan cerca está el promedio del valor de referencia", "Qué tan reciente es el certificado", "La precisión describe la dispersión de lecturas; la cercanía al valor de referencia es la exactitud."),
        ("abc", "En Mecánica Industrial: ¿cómo se calcula el rango de una serie de lecturas?", "Valor mayor menos valor menor", "Suma de las lecturas dividida por su número", "Promedio menos valor de referencia", "El rango resta el menor al mayor; las otras fórmulas son el promedio y el sesgo."),
        ("abc", "En Mecánica Industrial: ¿qué es un plan de control?", "El documento que dice qué se controla, con qué instrumento y cada cuánto", "El plano de la pieza con todas sus cotas", "La lista de las personas del taller", "El plan de control organiza las verificaciones."),
        ("=", "{F} ¿Cuántos µm vale el rango de las lecturas del inspector A?", "100014-100010", "Se resta la lectura menor a la mayor.", " µm"),
        ("=", "{F} ¿Cuántos µm suman las diferencias de las cinco lecturas del inspector A con la referencia?", "12+10+14+11+13", "Cada diferencia se calcula con 100.000 y se suman las cinco.", " µm"),
        ("abc", "{F} ¿Qué inspector tiene lecturas más parecidas entre sí?", "El inspector A, con un rango menor", "El inspector B, con un rango menor", "Ambos por igual, porque usan la misma barra", "El rango de A es 4 µm y el de B es 8 µm."),
        ("=", "{F} ¿Cuántos µm vale el sesgo del inspector A?", "(100012+100010+100014+100011+100013)//5-100000", "Se calcula el promedio de las cinco lecturas y se resta el valor de referencia.", " µm"),
        ("=", "{F} ¿Cuántos µm vale el rango de las lecturas del inspector B?", "100004-99996", "Se resta la lectura menor a la mayor.", " µm"),
        ("abc", "{F} El inspector B tiene un promedio de 100.000 µm. Frente al inspector A, ¿qué se puede decir?", "B es más exacto, con sesgo 0, y A es más preciso, con rango menor", "A es más exacto porque su sesgo es mayor", "B es más preciso porque su promedio es igual a la referencia", "El sesgo de B es 0, así que es más exacto, y el rango de A es menor."),
        ("abc", "{F} Un jefe dice: «el inspector A repite casi lo mismo, así que mide exacto». ¿Qué respuesta es correcta?", "Es falso: repetir lecturas indica precisión, y su promedio se desvía 12 µm de la referencia", "Es cierto, porque repetir lecturas prueba exactitud", "Es cierto, si usa un instrumento digital", "La precisión no implica exactitud; el sesgo de A es de 12 µm."),
        ("abc", "{F} Para decidir con qué instrumento seguir controlando la barra, el jefe pide primero verificar el certificado de calibración de cada uno. ¿Por qué es razonable?", "Porque el certificado informa el error del instrumento y su vigencia", "Porque el certificado reemplaza las mediciones", "Porque el certificado dice quién midió mejor", "El certificado de calibración respalda la confiabilidad del instrumento."),
        ("=", "{F} Se miden 6 barras de referencia iguales a la de la ficha con el instrumento del inspector A, y cada una presenta el mismo sesgo que él. ¿Cuántos µm suman los sesgos de las 6 barras?", "12*6", "Se multiplica el sesgo de una barra por el número de barras.", " µm"),
        ("Las lecturas de ejemplo de una pieza de referencia de 12.000 µm son 12.003; 12.006 y 12.009. ¿Qué sesgo tiene este instrumento?", "6 µm", "La suma es 36.018, el promedio es 12.006 y 12.006 menos 12.000 son 6."),
    ],
    ctx=("abc", "En un taller de ejemplo, el inspector anota solo una lectura de 3 piezas y declara que el instrumento «es exacto». ¿Qué le propones?", "Que repita las mediciones y calcule el rango y el sesgo antes de afirmarlo", "Que no mida más porque ya sabe que es exacto", "Que cambie de instrumento sin comparar", "Una sola lectura no permite hablar de precisión ni de exactitud."),
    sc=[
        ("En Mecánica Industrial: ¿qué es el sesgo?", "El promedio menos el valor de referencia", "El sesgo mide qué tan cerca está el promedio de la referencia."),
        ("¿Qué mide el rango?", "La dispersión de las lecturas", "El rango resta el menor al mayor."),
        ("¿Qué documento dice cada cuánto se controla una magnitud?", "El plan de control", "El plan de control define qué, con qué y cada cuánto."),
    ],
    op=("Ficha de ejemplo: una pieza de referencia mide 40.000 µm según su certificado. Un inspector la mide cuatro veces y obtiene, en µm: 40.004; 40.006; 40.002 y 40.008. Escribe (a) el rango, (b) el promedio, (c) el sesgo, (d) si te parece más un instrumento preciso o uno exacto, y por qué.",
        "(a) 40.008 − 40.002 = 6 µm. (b) La suma es 160.020 y el promedio es 40.005 µm. (c) 40.005 − 40.000 = 5 µm. (d) Las lecturas se parecen entre sí (rango pequeño), pero el promedio se desvía 5 µm de la referencia: es más preciso que exacto.",
        ["calcula el rango", "calcula el promedio y el sesgo", "distingue precisión y exactitud"],
        ["hoja con los tres cálculos y la conclusión"],
        ["calcular el promedio sin sumar todas las lecturas", "confundir rango con sesgo", "decir que repetir lecturas prueba exactitud"],
        "Pregunta: «¿qué compara el sesgo?». Si duda, pídele que relea su definición."),
    reinforce="Inventa tres lecturas de una pieza de referencia y calcula el rango y el sesgo.",
    extend="Explica con un ejemplo por qué un instrumento preciso puede estar mal calibrado.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (dos informes de inspección de ejemplo sobre la misma pieza, inventados). Plano: largo 150.000 µm con tolerancia de ±50 µm. "
     "Informe del inspector Uno: instrumento análogo con resolución de 10 µm, certificado vigente, pieza a 20 °C, lectura 150.040 µm, resultado «cumple». "
     "Informe del inspector Dos: instrumento digital con resolución de 10 µm, certificado vencido, pieza recién retirada de un proceso caliente, lectura 150.070 µm, resultado «no cumple». Temperatura de referencia de las mediciones: 20 °C.")
build(
    O2, 3, F,
    use="Aprenderé a analizar en papel dos informes que discrepan, a buscar las causas posibles y a decidir cuál lectura es confiable.",
    prior=["Sé qué es una tolerancia.", "Sé qué es la resolución de un instrumento.", "Sé restar números enteros."],
    explain=[
        "Cuando dos informes de la misma pieza discrepan, no se elige el que conviene: se analizan las condiciones de cada medición. Las causas más comunes son un instrumento con certificado vencido, una resolución distinta, un error de paralaje, una pieza medida a otra temperatura y un registro incompleto. Las mediciones se refieren a una temperatura de referencia, en estos ejemplos 20 °C, porque los metales cambian de tamaño con el calor.",
        "Una lectura es confiable cuando el instrumento está calibrado, su resolución es suficiente para la tolerancia (en estos ejemplos, la resolución no debe ser mayor que la tolerancia) y la pieza está en las condiciones de referencia. Si no se puede confiar en ninguna, se pide repetir la medición a personal autorizado. La decisión y sus razones se escriben en el registro.",
        f"Este análisis se hace con los papeles; no se interviene ninguna pieza ni instrumento. {EMER} {AVISO}",
    ],
    vocab=[("discrepancia", "diferencia entre dos resultados que deberían coincidir"), ("temperatura de referencia", "temperatura a la que se refieren las mediciones, en los ejemplos 20 °C"), ("condiciones de medición", "instrumento, resolución, temperatura y estado de la pieza al medir"), ("lectura confiable", "la que viene de un instrumento calibrado, con resolución suficiente y condiciones de referencia"), ("repetir la medición", "volver a medir en condiciones controladas")],
    worked=[
        ("Revisar la resolución", "Una tolerancia de ejemplo es de ±20 µm y el instrumento tiene resolución de 100 µm. ¿Sirve para ese control?", ["El instrumento solo distingue saltos de 100 µm.", "Eso es mayor que la tolerancia de 20 µm."], "No sirve: su resolución es mayor que la tolerancia"),
        ("Buscar una causa", "Dos lecturas de ejemplo de una pieza difieren en 30 µm. Una se tomó con la pieza a 20 °C y la otra con la pieza recién retirada de un proceso caliente. ¿Cuál es una causa posible?", ["Las condiciones de medición no son las mismas.", "El calor cambia el tamaño de un metal."], "La temperatura distinta de la pieza"),
    ],
    mistakes=[("Quedarse con el informe que dice «cumple» sin revisar sus condiciones.", "Un resultado favorable puede venir de una medición mal hecha.", "Revisa certificado, resolución y temperatura de ambos informes."),
              ("Promediar dos lecturas hechas en condiciones distintas.", "Mezclar una lectura confiable con una dudosa no da una medida confiable.", "Descarta la dudosa y repite la medición si hace falta.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es una discrepancia entre dos informes de inspección?", "Una diferencia entre dos resultados que deberían coincidir", "Una pieza que cumple todas sus tolerancias", "Un instrumento recién calibrado", "La discrepancia es el desacuerdo que obliga a analizar causas."),
        ("abc", "En Mecánica Industrial: ¿qué es la temperatura de referencia de una medición?", "Aquella a la que se refieren las mediciones, en los ejemplos 20 °C", "La temperatura máxima que soporta el instrumento", "La temperatura del taller ese día", "La referencia es fija, para poder comparar mediciones."),
        ("abc", "En Mecánica Industrial: ¿cuándo es confiable una lectura?", "Cuando el instrumento está calibrado, tiene resolución suficiente y la pieza está en condiciones de referencia", "Cuando la pantalla es digital", "Cuando el resultado es «cumple»", "La confiabilidad depende de las condiciones y no del resultado."),
        ("=", "{F} ¿Cuántos µm de diferencia hay entre las lecturas de los inspectores Uno y Dos?", "150070-150040", "Se resta la lectura menor a la mayor.", " µm"),
        ("abc", "{F} ¿Qué condición del informe del inspector Uno respalda su lectura?", "Su certificado vigente y la pieza a 20 °C", "Que la pantalla era digital", "Que el resultado fuera «cumple»", "Calibración vigente y temperatura de referencia dan confianza a una lectura."),
        ("abc", "{F} ¿Qué condición del informe del inspector Dos pone en duda su lectura?", "Su certificado vencido y la pieza recién retirada de un proceso caliente", "Que su instrumento sea digital", "Que haya medido en µm", "El certificado vencido y la pieza caliente alejan la medición de las condiciones de referencia."),
        ("=", "{F} ¿Cuántos µm vale el límite superior de la tolerancia del largo?", "150000+50", "Se suma la tolerancia al valor del plano.", " µm"),
        ("abc", "{F} Usando solo el número de la lectura, ¿qué ocurre con la lectura del inspector Dos respecto de la tolerancia?", "Se aparta 70 µm y supera la tolerancia de 50 µm", "Se aparta 40 µm y está dentro de la tolerancia", "Coincide exactamente con el plano", "La diferencia 150.070 menos 150.000 es 70 µm."),
        ("abc", "{F} ¿Es adecuada la resolución del instrumento del inspector Uno para esta tolerancia de ±50 µm?", "Sí, porque su resolución de 10 µm es menor que la tolerancia y permite distinguir si la pieza cumple", "No, porque la resolución análoga nunca sirve", "No, porque la resolución debe ser mayor que la tolerancia", "Una resolución del orden de la tolerancia o menor permite decidir."),
        ("abc", "{F} Un jefe propone aceptar el informe Uno porque dice «cumple» y descartar el Dos sin más análisis. ¿Qué respuesta es correcta?", "Conviene analizar las condiciones de ambos y, si hay dudas, pedir repetir la medición a personal autorizado", "Es correcto, porque el resultado favorable es el real", "Es correcto, porque el informe Dos tiene más resolución", "Se decide por las condiciones de medición y no por el resultado que se prefiere."),
        ("abc", "{F} Se repite la medición con un instrumento calibrado, la pieza a 20 °C, y da 150.045 µm. ¿Qué conclusión corresponde?", "La pieza cumple, porque se aparta 45 µm y la tolerancia es de 50 µm", "La pieza no cumple, porque 150.045 es distinto de 150.000", "No se puede concluir nada, porque ya hay dos informes", "La lectura confiable cumple la tolerancia."),
        ("=", "{F} Una lectura confiable sale a 150.045 µm. Si el taller fabrica 12 piezas iguales y la desviación de cada una fuera la misma, ¿cuántos µm sumarían las desviaciones respecto del plano en las 12 piezas?", "45*12", "Se multiplica la desviación de una pieza por el número de piezas.", " µm"),
        ("En un lote de ejemplo, de 10 informes, 3 se descartan por certificado vencido y 2 por pieza fuera de temperatura de referencia. ¿Cuántos informes quedan para analizar?", "5 informes", "Se descartan 3 más 2, es decir 5, y quedan 10 menos 5."),
    ],
    ctx=("abc", "Un compañero de ejemplo dice: «si dos inspectores discrepan, se saca el promedio y listo». ¿Qué respondes?", "Que primero se revisan las condiciones de cada medición y se repite si hay dudas", "Que sí, porque el promedio resuelve cualquier discrepancia", "Que se elige al inspector con más años", "Promediar mezcla lecturas confiables y dudosas."),
    sc=[
        ("En Mecánica Industrial: ¿qué se revisa primero ante dos informes que discrepan?", "Las condiciones de cada medición", "Instrumento, resolución, temperatura y registro explican muchas discrepancias."),
        ("¿Qué pasa si no se puede confiar en ninguna lectura?", "Se pide repetir la medición a personal autorizado", "Repetir en condiciones controladas aclara la discrepancia."),
        ("¿A qué temperatura de referencia se refieren los ejemplos?", "A 20 °C", "La referencia fija permite comparar mediciones."),
    ],
    op=("Ficha de ejemplo: un diámetro debe ser 18.000 µm con tolerancia de ±20 µm. Inspector Tres: instrumento con certificado vigente y resolución de 10 µm, pieza a 20 °C, lectura 18.014 µm. Inspector Cuatro: instrumento con certificado vencido, pieza recién salida de un proceso caliente, lectura 18.031 µm. Escribe (a) la diferencia de cada lectura con el plano, (b) cuál lectura es más confiable y por qué, (c) qué harías con la otra.",
        "(a) Tres: 14 µm; Cuatro: 31 µm. (b) La del inspector Tres, porque su instrumento está calibrado y la pieza estaba a la temperatura de referencia. (c) La del inspector Cuatro se registra como dudosa y se pide repetirla a personal autorizado en condiciones de referencia.",
        ["calcula las diferencias", "elige la lectura confiable con razones", "propone repetir la medición"],
        ["hoja con las diferencias, la elección y la razón"],
        ["elegir por el resultado favorable", "promediar ambas lecturas", "olvidar el certificado y la temperatura"],
        "Pregunta: «¿en qué condiciones se midió cada pieza?». Si no responde, pídele que relea la definición de lectura confiable."),
    reinforce="Escribe tres causas posibles de que dos inspectores midan distinto la misma pieza.",
    extend="Explica con un ejemplo por qué una resolución mayor que la tolerancia impide decidir si una pieza cumple.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (plan de muestreo y registro de ejemplo, inventados). Un lote de 200 casquillos se controla midiendo una muestra de 20. Plan de ejemplo: si en la muestra hay 2 casquillos defectuosos o menos, se acepta el lote; "
     "si hay 3 o más, se rechaza para una inspección completa. Registro de la muestra: diámetros interiores medidos en µm, con tolerancia de ±20 µm sobre 15.000 µm. "
     "Diferencias con el plano (en µm) de los 20 casquillos: 4, 9, 22, 15, 18, 2, 11, 7, 25, 19, 3, 16, 12, 30, 8, 5, 14, 20, 6, 10. Costo de ejemplo: la inspección de un casquillo cuesta $150.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar un plan de muestreo sencillo, a contar defectuosos en un registro y a calcular el costo de inspeccionar con datos de ejemplo.",
    prior=["Sé contar elementos en una lista.", "Sé multiplicar y restar números enteros.", "Sé qué es una tolerancia."],
    explain=[
        "Cuando un lote es grande, no siempre se mide cada pieza: se mide una muestra, un grupo pequeño tomado del lote. Un plan de muestreo dice cuántas piezas se miden y cuántas defectuosas se aceptan. Una pieza defectuosa es la que tiene alguna medida fuera de tolerancia. Si el número de defectuosas de la muestra no supera el límite del plan, se acepta el lote; si lo supera, se rechaza y se inspecciona completo.",
        "El registro de la muestra permite contar defectuosas: en cada fila se compara la diferencia con la tolerancia, y la pieza es defectuosa si la diferencia es mayor. El muestreo ahorra costos, pero acepta un riesgo: un lote bueno puede rechazarse o uno malo aceptarse. Los planes reales los fija la norma vigente; aquí son de ejemplo.",
        f"El análisis es solo de papel, con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("lote", "conjunto de piezas fabricadas en las mismas condiciones"), ("muestra", "grupo pequeño de piezas tomado del lote"), ("plan de muestreo", "regla que dice cuántas piezas se miden y cuántas defectuosas se aceptan"), ("pieza defectuosa", "la que tiene alguna medida fuera de tolerancia"), ("inspección completa", "medir todas las piezas del lote")],
    worked=[
        ("Contar defectuosas", "Una muestra de ejemplo tiene tolerancia de ±10 µm y las diferencias de 5 piezas son 3, 12, 8, 10 y 15. ¿Cuántas son defectuosas?", ["Es defectuosa si la diferencia supera 10.", "Superan 10 las de 12 y 15."], "2 defectuosas"),
        ("Aplicar el plan", "Un plan de ejemplo acepta el lote con 1 defectuosa o menos. La muestra tiene 2. ¿Qué se hace?", ["2 supera el límite de 1.", "Se rechaza el lote."], "Rechazar el lote"),
    ],
    mistakes=[("Contar como defectuosa una pieza cuya diferencia es exactamente igual a la tolerancia.", "El límite de la tolerancia sí cumple.", "Es defectuosa solo cuando la diferencia es mayor que la tolerancia."),
              ("Aceptar el lote porque «casi todo está bien».", "El plan fija un límite exacto de defectuosas y no admite excepciones.", "Cuenta las defectuosas y aplica la regla del plan.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es una muestra?", "Un grupo pequeño de piezas tomado del lote", "El lote completo", "La pieza que se usa como patrón", "La muestra representa al lote sin medirlo entero."),
        ("abc", "En Mecánica Industrial: ¿qué dice un plan de muestreo?", "Cuántas piezas se miden y cuántas defectuosas se aceptan", "Cuánto cuesta cada pieza del lote", "Qué instrumento se compra", "El plan fija tamaño de muestra y límite de defectuosas."),
        ("abc", "En Mecánica Industrial: ¿cuándo una pieza es defectuosa?", "Cuando tiene alguna medida fuera de tolerancia", "Cuando es la última del lote", "Cuando su medida es igual a la del plano", "Fuera de tolerancia define a la pieza defectuosa."),
        ("=", "{F} ¿Cuántas piezas del lote quedan sin medir si se mide la muestra de 20?", "200-20", "Se resta el tamaño de la muestra al del lote.", " casquillos"),
        ("abc", "{F} ¿Cuál es la regla de aceptación del plan de la ficha?", "Aceptar el lote si hay 2 defectuosos o menos en la muestra", "Aceptar el lote si hay al menos 3 defectuosos", "Aceptar el lote si no hay ninguna medida repetida", "El plan acepta con 2 defectuosos o menos y rechaza con 3 o más."),
        ("abc", "{F} Un casquillo de la muestra tiene una diferencia de 20 µm con tolerancia de ±20 µm. ¿Es defectuoso?", "No, porque el límite de la tolerancia sí cumple", "Sí, porque no coincide con el plano", "Sí, porque la diferencia es igual a la tolerancia", "Se acepta la diferencia igual o menor que la tolerancia."),
        ("{F} Con la tolerancia de ±20 µm, ¿cuántos casquillos de la muestra son defectuosos?", "3 casquillos", "Son defectuosos los de 22, 25 y 30 µm; el de 20 µm cumple porque es igual a la tolerancia."),
        ("=", "{F} ¿Cuánto cuesta inspeccionar la muestra completa de 20 casquillos?", "20*150", "Se multiplica el costo por casquillo por el número de casquillos.", " pesos de ejemplo"),
        ("=", "{F} ¿Cuánto costaría inspeccionar el lote completo de 200 casquillos?", "200*150", "Se multiplica el costo por casquillo por el tamaño del lote.", " pesos de ejemplo"),
        ("abc", "{F} Con las diferencias del registro, ¿qué decide el plan para el lote?", "Rechazarlo, porque hay 3 defectuosos y el límite es 2", "Aceptarlo, porque son menos de 5", "Aceptarlo, porque la mayoría cumple", "Con 3 defectuosos el plan manda rechazar el lote."),
        ("abc", "{F} Un jefe propone aceptar el lote porque 17 de 20 casquillos cumplen. ¿Qué respuesta es correcta?", "Es incorrecto: el plan fija un máximo de 2 defectuosos y hay 3", "Es correcto, porque 17 es más de la mitad", "Es correcto, porque el plan solo se aplica si hay 10 defectuosos", "La decisión sigue la regla del plan y no una impresión general."),
        ("=", "{F} Se rechaza el lote y se inspecciona completo, pero ya se midió la muestra. ¿Cuánto cuesta inspeccionar solo los casquillos que faltan por medir?", "(200-20)*150", "Se restan los ya medidos y se multiplica por el costo de cada uno.", " pesos de ejemplo"),
        ("Un lote de ejemplo de 300 piezas se acepta con 1 defectuosa o menos en una muestra de 30. Tres muestras sucesivas de lotes distintos traen 0, 1 y 2 defectuosas. ¿Cuántos de esos tres lotes se aceptan?", "2 lotes", "Se aceptan los de 0 y 1 defectuosa; el de 2 supera el límite de 1."),
    ],
    ctx=("abc", "En un taller de ejemplo, la jefatura quiere medir solo 5 piezas de un lote de 500 y decir «el lote está bien» sin plan escrito. ¿Qué propones?", "Aplicar un plan de muestreo escrito que fije el tamaño de la muestra y el límite de defectuosas", "Aceptar el lote sin medir nada", "Medir solo las piezas de la caja de arriba", "Sin un plan no hay regla objetiva para aceptar o rechazar."),
    sc=[
        ("En Mecánica Industrial: ¿qué es un lote?", "Un conjunto de piezas fabricadas en las mismas condiciones", "El lote es el conjunto del que se toma la muestra."),
        ("¿Qué se hace si las defectuosas de la muestra superan el límite del plan?", "Se rechaza el lote y se inspecciona completo", "Superar el límite obliga a revisar todo."),
        ("¿Cuándo no es defectuosa una pieza con tolerancia?", "Cuando su diferencia es igual o menor que la tolerancia", "El límite de la tolerancia sí cumple."),
    ],
    op=("Ficha de ejemplo: un lote de 100 pasadores se controla con una muestra de 10. El plan de ejemplo acepta el lote si hay 1 defectuoso o menos. Tolerancia de ±15 µm. Diferencias con el plano de la muestra, en µm: 3, 15, 8, 18, 5, 11, 2, 9, 14, 6. Costo de inspeccionar un pasador: $200. Escribe (a) cuántos pasadores son defectuosos, (b) si se acepta el lote y por qué, (c) cuánto cuesta inspeccionar la muestra.",
        "(a) Solo el de 18 µm supera 15, o sea 1 defectuoso (el de 15 cumple porque es igual a la tolerancia). (b) Se acepta, porque 1 defectuoso no supera el límite de 1. (c) 10 × 200 = 2.000 pesos de ejemplo.",
        ["cuenta bien los defectuosos", "aplica la regla del plan", "calcula el costo"],
        ["hoja con la cuenta, la decisión y el costo"],
        ["contar como defectuoso el valor igual a la tolerancia", "aceptar sin comparar con el límite", "multiplicar por el tamaño del lote"],
        "Pregunta: «¿la diferencia de 15 µm supera la tolerancia de 15 µm?». Si duda, pídele que relea la regla del límite."),
    reinforce="Inventa un plan de muestreo con tamaño de muestra y límite, y decide qué pasa con dos muestras distintas.",
    extend="Explica con un ejemplo por qué medir una muestra ahorra costos pero acepta un riesgo.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Taller Demo» une y repara estructuras de acero con procesos de corte y soldadura. Peligros anotados en su matriz: radiación y destellos del arco, humos de soldadura, chispas y salpicaduras, "
     "quemaduras por piezas calientes, cilindros de gas a presión, descarga eléctrica de los equipos, material inflamable cerca y ruido. Dotación del área de soldadura: 12 personas.")
build(
    O3, 1, F,
    use="Aprenderé qué peligros tienen el corte y la soldadura, qué controles existen en cada nivel de la jerarquía y qué documentos y autorizaciones exigen estas tareas.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé la jerarquía de controles.", "Sé que algunas tareas exigen permiso."],
    explain=[
        "Soldar es unir piezas metálicas fundiendo el material en la unión, y cortar con calor es separarlas. Ambas tareas producen radiación del arco o de la llama, humos, chispas, calor y, según el equipo, gases a presión o electricidad. Por eso se anotan en la matriz de peligros y se aplica la jerarquía de controles: eliminar o sustituir cuando se puede, extraer los humos y proteger con pantallas (ingeniería), exigir permiso, orden y capacitación (administrativos) y, al final, usar EPP.",
        "El permiso de trabajo en caliente es el documento que autoriza una tarea con chispas o llama y exige despejar el material inflamable de la zona. Solo hacen estas tareas personas calificadas, es decir, con una acreditación vigente, bajo supervisión. El EPP típico incluye careta con filtro, guantes, ropa resistente al calor, calzado de seguridad y, según el caso, protección respiratoria.",
        f"Este cuaderno no enseña a soldar ni a cortar; solo conceptos y documentos. {EMER} {AVISO}",
    ],
    vocab=[("soldadura", "unión de piezas metálicas fundiendo el material en la unión"), ("trabajo en caliente", "tarea que produce chispas, llama o calor"), ("permiso de trabajo en caliente", "documento que autoriza una tarea con chispas o llama"), ("persona calificada", "quien tiene una acreditación vigente para la tarea"), ("careta con filtro", "protección de la cara y los ojos contra el arco"), ("extracción de humos", "sistema que retira el humo del lugar de trabajo")],
    worked=[
        ("Clasificar un control", "En un taller de ejemplo se instala un sistema que retira el humo de soldadura del lugar. ¿A qué nivel de la jerarquía de controles corresponde?", ["El sistema cambia el lugar y reduce el humo sin depender de una persona.", "Es un control de ingeniería."], "Control de ingeniería"),
        ("Documento necesario", "Una tarea de ejemplo producirá chispas cerca de un sector con cajas de cartón. ¿Qué documento debe existir antes de comenzar?", ["La tarea produce chispas, es un trabajo en caliente.", "Ese tipo de tarea exige un permiso de trabajo en caliente."], "Permiso de trabajo en caliente"),
    ],
    mistakes=[("Creer que leer sobre soldadura habilita para soldar.", "Estas tareas exigen formación, calificación, supervisión y norma vigente.", "Aprende aquí los conceptos y deja la tarea a personal calificado."),
              ("Pensar que la careta con filtro basta para controlar todos los peligros.", "El EPP no retira el humo ni evita el incendio por chispas.", "Aplica primero los demás niveles de la jerarquía y suma el EPP.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es la soldadura?", "La unión de piezas metálicas fundiendo el material en la unión", "El pulido de una superficie metálica", "La separación de una pieza con una sierra manual", "La soldadura une fundiendo el material; el pulido y el aserrado no lo hacen."),
        ("abc", "En Mecánica Industrial: ¿qué documento autoriza una tarea con chispas o llama?", "El permiso de trabajo en caliente", "El plano de despiece", "El certificado de calibración de un instrumento", "El permiso de trabajo en caliente autoriza las tareas con chispas o llama."),
        ("abc", "En Mecánica Industrial: ¿qué es una persona calificada para soldar?", "La que tiene una acreditación vigente para esa tarea", "Cualquiera que haya visto el procedimiento", "La que lleva más años en el taller", "La calificación es una acreditación y no basta con ver o con antigüedad."),
        ("abc", "{F} ¿Cuál de los peligros de la matriz se relaciona con un incendio?", "El material inflamable cerca", "El ruido", "La radiación del arco", "El material inflamable cerca de las chispas puede encenderse."),
        ("abc", "{F} Instalar un sistema que retire los humos de soldadura del lugar de trabajo es un control:", "De ingeniería", "Administrativo", "De EPP", "El sistema cambia el lugar sin depender de la conducta de cada persona."),
        ("abc", "{F} Un cartel que dice «solo personal calificado» en el área de soldadura es un control:", "Administrativo", "De ingeniería", "De sustitución", "El cartel informa y ordena una conducta."),
        ("=", "{F} Cada 4 personas del área de soldadura debe haber 1 persona asignada a observar que se cumpla el permiso. ¿Cuántas observadoras corresponden?", "12//4", "Se divide la dotación entre las personas que cubre cada observadora.", " observadoras"),
        ("=", "Una matriz de ejemplo puntúa el riesgo como probabilidad por gravedad. Un peligro tiene probabilidad 4 y gravedad 5. Tras sacar el material inflamable de la zona la probabilidad baja a 2. ¿Cuántos puntos baja el puntaje?", "4*5-2*5", "Se calcula el puntaje antes y después, y se resta.", " puntos"),
        ("abc", "{F} Se propone unir dos piezas con pernos en lugar de soldarlas, cuando el proyecto lo permite. ¿Qué nivel de la jerarquía representa?", "Sustitución", "EPP", "Control administrativo", "Cambiar por un método con menos peligro es sustituir."),
        ("abc", "{F} Un estudiante dice: «ya sé cuáles son los peligros, así que puedo hacer una soldadura en el patio del liceo con un equipo prestado». ¿Qué respuesta es correcta?", "Es falso: soldar exige personal calificado, norma vigente, supervisión y permiso, y este cuaderno no habilita para hacerlo", "Es cierto, si usa careta", "Es cierto, si lo hace de día", "Conocer los peligros no habilita para trabajar."),
        ("abc", "En una visita a un taller de ejemplo, se incendia un material cerca de un equipo de soldadura. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Intentar apagar el fuego tú mismo con lo que encuentres", "Tapar el fuego con tu ropa", "Intervenir sin formación puede causar quemaduras u otro accidente."),
        ("=", "El taller de ejemplo tiene 3 áreas de soldadura y en cada una hay 5 puestos. Cada puesto necesita 1 careta con filtro más 2 de repuesto en total para todo el taller. ¿Cuántas caretas se necesitan?", "3*5+2", "Se multiplican áreas por puestos y se suman los repuestos.", " caretas"),
        ("abc", "En Mecánica Industrial: ¿por qué el EPP queda en el último nivel de la jerarquía de controles?", "Porque no quita el peligro y protege solo a quien lo usa", "Porque no es necesario usarlo", "Porque lo reemplaza el permiso de trabajo", "El EPP es la última barrera, no la primera."),
    ],
    ctx=("abc", "Un familiar de ejemplo te dice: «prueba soldar este soporte en el garaje, solo es una vez». ¿Qué respondes?", "Que no, porque soldar exige formación, norma vigente y protección, y que consultarás a un adulto responsable", "Que sí, con unas gafas oscuras", "Que sí, mientras haya agua cerca", "Sin formación ni autorización no se hacen tareas de soldadura."),
    sc=[
        ("En Mecánica Industrial: ¿qué es un trabajo en caliente?", "Una tarea que produce chispas, llama o calor", "Estas tareas exigen permiso por el riesgo de incendio."),
        ("¿Qué tipo de control es la extracción de humos?", "Un control de ingeniería", "Cambia el lugar de trabajo sin depender de personas."),
        ("¿Quién puede hacer tareas de soldadura?", "Personas calificadas, con supervisión y norma vigente", "La calificación es una acreditación vigente."),
    ],
    op=("El «Taller Demo» anota una tarea de ejemplo: reparar un soporte metálico con soldadura en un sector donde hay cajas de cartón y un cilindro de gas. Peligros anotados: chispas, humos y material inflamable cerca. Escribe (a) un control de ingeniería, (b) un control administrativo, (c) qué EPP se suma, (d) qué documento debe existir antes de comenzar. No describas cómo se suelda: la tarea la hace personal calificado.",
        "(a) Una extracción de humos y una pantalla que retenga las chispas. (b) Una regla de despejar el sector y una señal de zona de trabajo en caliente. (c) Careta con filtro, guantes y ropa resistente al calor, como última barrera. (d) El permiso de trabajo en caliente. La tarea la hace personal calificado.",
        ["propone un control de ingeniería", "propone un control administrativo", "nombra EPP como última barrera", "nombra el permiso"],
        ["hoja con las cuatro respuestas"],
        ["proponer solo EPP", "olvidar el permiso", "describir cómo se hace la tarea"],
        "Pregunta: «¿qué se hace con las cajas de cartón antes de comenzar?». Si duda, pídele que relea la definición del permiso de trabajo en caliente."),
    reinforce="Escribe los peligros de un trabajo en caliente y un control de cada nivel de la jerarquía.",
    extend="Explica con un ejemplo por qué el permiso de trabajo en caliente es un control administrativo y no reemplaza a la extracción de humos.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (cuadro de procesos de ejemplo, inventado). Oxicorte: corta con una llama de un gas combustible y oxígeno. Soldadura por arco manual: un electrodo revestido, que es una varilla que se consume, mantiene un arco eléctrico con la pieza. "
     "Soldadura TIG: un electrodo de tungsteno que no se consume y un gas protector inerte; el material de aporte se agrega aparte. Soldadura MIG: un alambre continuo que se consume y un gas protector. "
     "Posiciones de la pieza al unir: plana, horizontal y vertical. Documentos: especificación del procedimiento de soldadura (WPS) y registro de calificación de la persona soldadora.")
build(
    O3, 2, F,
    use="Aprenderé a distinguir los procesos de corte y soldadura por lo que usan, qué es una posición de soldadura y qué documentos respaldan una tarea.",
    prior=["Sé qué es una soldadura.", "Sé qué es un permiso de trabajo en caliente.", "Sé leer una tabla."],
    explain=[
        "Los procesos se distinguen por lo que usan. El oxicorte emplea una llama de gas combustible y oxígeno y sirve para cortar. La soldadura por arco manual usa un electrodo revestido que se consume. La TIG usa un electrodo de tungsteno que no se consume, un gas protector inerte y un material de aporte aparte. La MIG usa un alambre continuo que se consume y un gas protector. El gas protector evita que el aire dañe la unión.",
        "La posición es cómo está orientada la unión: plana, horizontal o vertical. La especificación del procedimiento de soldadura (WPS) es un documento que indica el proceso, el material de la pieza, la posición y el material de aporte que respaldan una unión. El registro de calificación dice qué procesos y posiciones puede hacer una persona soldadora, y por cuánto tiempo.",
        f"Un inspector de soldadura revisa que se cumpla la WPS; la jefatura asigna el trabajo; la persona calificada ejecuta. {EMER} {AVISO}",
    ],
    vocab=[("oxicorte", "corte con llama de gas combustible y oxígeno"), ("electrodo revestido", "varilla que se consume y mantiene el arco en la soldadura por arco manual"), ("TIG", "soldadura con electrodo de tungsteno que no se consume y gas protector"), ("MIG", "soldadura con alambre continuo que se consume y gas protector"), ("WPS", "especificación del procedimiento de soldadura"), ("posición", "orientación de la unión: plana, horizontal o vertical"), ("registro de calificación", "documento con los procesos y posiciones que puede hacer una persona soldadora")],
    worked=[
        ("Identificar el proceso", "Un cuadro de ejemplo dice: «alambre continuo que se consume y gas protector». ¿Qué proceso describe?", ["El alambre continuo que se consume es propio de un proceso.", "Es la soldadura MIG."], "Soldadura MIG"),
        ("Leer una calificación", "El registro de una persona de ejemplo dice: «arco manual, posición plana». ¿Puede hacer una unión vertical con arco manual?", ["El registro solo cubre la posición plana.", "La posición vertical no está incluida."], "No, su registro cubre solo la posición plana"),
    ],
    mistakes=[("Confundir TIG con MIG.", "La TIG usa un electrodo de tungsteno que no se consume y la MIG usa un alambre que se consume.", "Pregunta qué electrodo se consume para distinguirlas."),
              ("Creer que una calificación cubre cualquier proceso y posición.", "El registro de calificación indica qué procesos y posiciones cubre.", "Verifica proceso y posición del registro antes de asignar una tarea.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué caracteriza a la soldadura TIG?", "Un electrodo de tungsteno que no se consume y un gas protector", "Un alambre continuo que se consume y un gas protector", "Una varilla revestida que se consume sin gas protector externo", "El electrodo que no se consume distingue a la TIG."),
        ("abc", "En Mecánica Industrial: ¿qué es la WPS?", "La especificación del procedimiento de soldadura que respalda una unión", "El registro de calificación de una persona soldadora", "El permiso de trabajo en caliente", "La WPS indica proceso, material, posición y aporte."),
        ("abc", "En Mecánica Industrial: ¿qué es la posición de una soldadura?", "La orientación de la unión, como plana, horizontal o vertical", "El lugar del taller donde se trabaja", "El turno en que se realiza", "La posición describe cómo está orientada la unión."),
        ("abc", "{F} ¿Cuál proceso usa una llama de gas combustible y oxígeno para cortar?", "El oxicorte", "La soldadura MIG", "La soldadura TIG", "El oxicorte emplea llama y oxígeno; las otras soldaduras usan electrodo o alambre."),
        ("abc", "{F} ¿Qué proceso usa un electrodo revestido que se consume?", "La soldadura por arco manual", "La soldadura TIG", "El oxicorte", "El electrodo revestido es propio del arco manual."),
        ("abc", "{F} ¿Qué diferencia hay entre el electrodo de la TIG y el alambre de la MIG?", "El de la TIG no se consume y el alambre de la MIG sí", "Ambos se consumen igual", "El de la TIG se consume y el alambre de la MIG no", "El electrodo de tungsteno no se consume; el alambre MIG se va consumiendo."),
        ("=", "{F} Una unión puede quedar en 3 posiciones (plana, horizontal, vertical) y se evalúan 4 procesos de soldadura o corte de la ficha. ¿Cuántas combinaciones posibles de proceso y posición hay?", "3*4", "Se multiplican las posiciones por los procesos.", " combinaciones"),
        ("abc", "{F} Una persona tiene un registro con «MIG, posición plana». ¿Qué trabajo queda cubierto?", "Una unión con MIG en posición plana", "Una unión con TIG en posición plana", "Una unión con MIG en posición vertical", "Solo coinciden proceso y posición en la primera opción."),
        ("abc", "{F} El inspector detecta que una tarea usa un proceso distinto del que dice la WPS. ¿Qué corresponde?", "Detener la tarea y consultar a la jefatura para corregir el documento o el proceso", "Continuar porque el resultado final será el mismo", "Cambiar a mano la WPS para que coincida", "La WPS respalda la tarea; si no coincide se corrige antes de seguir."),
        ("abc", "{F} Un compañero dice: «mi amigo sabe soldar con TIG, así que puede hacerlo sin registro». ¿Qué respuesta es correcta?", "Es falso: la tarea exige un registro de calificación vigente para ese proceso y esa posición", "Es cierto, porque saber soldar basta", "Es cierto, si tiene años de experiencia", "La calificación se acredita con un registro, no con la experiencia dicha."),
        ("abc", "En una visita a un taller de ejemplo, un cilindro de gas cae y suena un escape. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte para cerrar la válvula", "Mover el cilindro hacia afuera", "Intervenir sin formación puede causar otro accidente."),
        ("=", "El taller de ejemplo tiene 15 personas soldadoras y el registro muestra que 9 están calificadas para MIG. ¿Cuántas no lo están?", "15-9", "Se resta las calificadas al total de personas.", " personas"),
        ("=", "Una ficha de ejemplo cubre arco manual en 2 posiciones, TIG en 1 posición y MIG en 3 posiciones. ¿Cuántas combinaciones de proceso y posición cubre en total?", "2+1+3", "Se suman las posiciones cubiertas en cada proceso.", " combinaciones"),
    ],
    ctx=("abc", "El jefe de un taller de ejemplo asigna una unión vertical con TIG a una persona cuyo registro dice «MIG, plana». ¿Qué propones?", "Revisar el registro de calificación y asignar la tarea a quien esté calificado para TIG en posición vertical", "Asignarla igual porque ya tiene experiencia con soldadura", "Cambiar la WPS para que diga MIG", "La tarea se asigna según proceso y posición registrados."),
    sc=[
        ("En Mecánica Industrial: ¿qué proceso usa un alambre continuo que se consume?", "La soldadura MIG", "El alambre continuo es propio de la MIG."),
        ("¿Qué documento indica proceso, material, posición y aporte de una unión?", "La WPS", "La WPS especifica el procedimiento de la unión."),
        ("¿Qué documento dice qué procesos y posiciones puede hacer una persona?", "El registro de calificación", "Acredita lo que la persona puede ejecutar."),
    ],
    op=("Ficha de ejemplo: una WPS pide arco manual, posición vertical. En el taller hay tres personas: Ana, con registro «arco manual, plana y horizontal»; Beto, con «arco manual, vertical»; Carla, con «MIG, vertical». Escribe (a) cuál proceso exige la WPS, (b) quién puede hacer esa tarea según los registros, (c) por qué las otras dos no, (d) qué documento mostrarías para respaldarlo.",
        "(a) Arco manual. (b) Beto. (c) Ana no tiene la posición vertical y Carla tiene otro proceso, MIG. (d) El registro de calificación de cada persona junto a la WPS.",
        ["identifica el proceso", "elige a la persona correcta", "explica por qué las otras no", "nombra los documentos"],
        ["hoja con las cuatro respuestas"],
        ["elegir por la experiencia dicha", "no revisar la posición", "olvidar el registro de calificación"],
        "Pregunta: «¿qué proceso y qué posición pide la WPS?». Si duda, pídele que subraye ambos datos."),
    reinforce="Escribe una frase para cada proceso (oxicorte, arco manual, TIG y MIG) con lo que lo distingue.",
    extend="Explica con un ejemplo por qué una persona calificada para una posición no está calificada para todas.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (WPS y registros de ejemplo, inventados). WPS-DEMO-1: material de las piezas, acero de ejemplo; proceso, MIG; posición, plana; unión, a tope. WPS-DEMO-2: acero de ejemplo; proceso, arco manual; posición, horizontal; unión, en filete. "
     "Registros de calificación: Persona P: MIG, plana, vigente hasta fin de año. Persona Q: arco manual, plana y horizontal, vencido. Persona R: arco manual, horizontal, vigente. Trabajos pedidos: T1, unión a tope con MIG en plana; T2, unión en filete con arco manual en horizontal; T3, unión en filete con arco manual en vertical.")
build(
    O3, 3, F,
    use="Aprenderé a cruzar un trabajo pedido con una WPS y con registros de calificación para decidir, en papel, quién puede asumirlo y qué falta.",
    prior=["Sé qué es una WPS y un registro de calificación.", "Sé qué es una posición de soldadura.", "Sé comparar datos de dos tablas."],
    explain=[
        "Para asignar un trabajo se cruzan tres documentos. El trabajo pedido dice qué unión, con qué proceso y en qué posición. La WPS debe cubrir ese proceso, esa posición y ese tipo de unión; si no existe una WPS para el trabajo, el trabajo no puede asignarse. El registro de calificación de la persona debe cubrir el mismo proceso y la misma posición y estar vigente.",
        "Una unión a tope junta dos piezas puestas extremo contra extremo; una unión en filete junta dos piezas puestas en ángulo, como una L. Cuando algo no coincide, se registra qué falta (WPS, proceso, posición o vigencia) y se informa a la jefatura. No se asigna «para salir del paso».",
        f"Este análisis se hace con papeles; no se ejecuta ninguna soldadura. {EMER} {AVISO}",
    ],
    vocab=[("unión a tope", "junta dos piezas puestas extremo contra extremo"), ("unión en filete", "junta dos piezas puestas en ángulo"), ("vigente", "que todavía no ha vencido"), ("trabajo pedido", "tarea que se quiere asignar, con su proceso, posición y unión"), ("cobertura", "lo que un documento cubre y lo que no")],
    worked=[
        ("Cruzar un trabajo", "Un trabajo de ejemplo pide unión en filete con TIG en horizontal. La única WPS que existe es para MIG en plana. ¿Se puede asignar?", ["La WPS no cubre ni el proceso ni la posición pedidos.", "Falta una WPS para ese trabajo."], "No, falta una WPS que lo cubra"),
        ("Revisar la vigencia", "Una persona de ejemplo tiene registro de MIG en plana, pero venció la semana pasada. ¿Puede asumir un trabajo con MIG en plana?", ["El proceso y la posición coinciden.", "El registro no está vigente."], "No, el registro está vencido"),
    ],
    mistakes=[("Asignar un trabajo porque la persona «tiene experiencia» aunque falte la WPS.", "Sin WPS no hay procedimiento que respalde la unión.", "Verifica que exista una WPS para el trabajo antes de asignar."),
              ("Olvidar la vigencia del registro de calificación.", "Un registro vencido no respalda la tarea.", "Revisa proceso, posición y vigencia de cada persona.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es una unión a tope?", "La que junta dos piezas puestas extremo contra extremo", "La que junta dos piezas puestas en ángulo", "La que une una pieza sobre otra con pernos", "A tope significa extremo contra extremo; en ángulo es unión en filete."),
        ("abc", "En Mecánica Industrial: ¿qué es una unión en filete?", "La que junta dos piezas puestas en ángulo, como una L", "La que junta dos piezas extremo contra extremo", "La que corta una pieza en dos partes", "El filete une piezas en ángulo."),
        ("abc", "En Mecánica Industrial: ¿qué debe cubrir una WPS respecto del trabajo pedido?", "El proceso, la posición y el tipo de unión", "Solo el nombre de la persona", "Solo la fecha de entrega", "La WPS respalda el trabajo cuando cubre proceso, posición y unión."),
        ("abc", "{F} ¿Qué WPS corresponde al trabajo T1?", "WPS-DEMO-1, porque cubre MIG, plana y unión a tope", "WPS-DEMO-2, porque cubre arco manual", "Ninguna, porque no hay WPS para MIG", "T1 pide MIG en plana a tope, igual que la WPS-DEMO-1."),
        ("abc", "{F} ¿Qué persona tiene un registro vigente que cubre el trabajo T1?", "La persona P", "La persona Q", "La persona R", "P tiene MIG en plana vigente; Q tiene arco manual y vencido; R tiene arco manual."),
        ("abc", "{F} ¿Por qué la persona Q no puede asumir el trabajo T2 aunque su registro cubre arco manual horizontal?", "Porque su registro está vencido", "Porque su registro cubre solo la posición plana", "Porque la WPS no existe", "El registro de Q dice horizontal pero está vencido."),
        ("{F} De los tres trabajos pedidos, ¿cuántos tienen hoy una persona con registro vigente que los cubra?", "2 trabajos", "T1 lo cubre P y T2 lo cubre R; para T3 no hay registro vigente en posición vertical."),
        ("abc", "{F} ¿Qué falta para poder asignar el trabajo T3?", "Una WPS para arco manual en posición vertical y una persona calificada para esa posición", "Solo más experiencia de la persona R", "Nada, porque R sabe arco manual", "La WPS-DEMO-2 es horizontal y R está calificada solo en horizontal."),
        ("abc", "{F} Se propone asignar T3 a la persona R usando la WPS-DEMO-2. ¿Qué respuesta es correcta?", "No corresponde: la WPS y el registro de R cubren la posición horizontal, no la vertical", "Corresponde, porque ambos son arco manual", "Corresponde, si R tiene experiencia", "Proceso igual no basta: la posición también debe coincidir."),
        ("abc", "{F} Un compañero dice: «a T1 lo puede hacer Q, porque sabe soldar». ¿Qué respuesta es correcta?", "Es falso: el registro de Q es de arco manual y está vencido, y T1 pide MIG", "Es cierto, porque cualquier registro sirve", "Es cierto, si Q trabaja despacio", "El proceso y la vigencia del registro no coinciden con el trabajo."),
        ("abc", "En un taller de ejemplo, una persona recibe una quemadura grave en una mano. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Aplicar una pomada casera", "Reventar las ampollas", "Los primeros auxilios y la atención los hacen quienes tienen formación."),
        ("=", "{F} Se agregan 5 trabajos nuevos al listado de la ficha, todos de tipo T1. Si cada trabajo toma 6 horas de una persona calificada, ¿cuántas horas suman los 5 trabajos nuevos y el trabajo T1 original?", "(5+1)*6", "Se suman los trabajos y se multiplican por las horas de cada uno.", " horas"),
        ("=", "Un taller de ejemplo tiene 8 registros de calificación: 3 vencidos y 5 vigentes. De los vigentes, 2 son de TIG y el resto de MIG. ¿Cuántas personas tienen un registro de MIG vigente?", "8-3-2", "Se descuentan los vencidos y los de TIG del total de registros.", " personas"),
    ],
    ctx=("abc", "Un cliente de ejemplo apura al taller: «da lo mismo quién lo haga, que lo haga cualquiera». ¿Qué propones?", "Explicar que cada trabajo requiere una WPS y una persona calificada vigente, y que la jefatura lo asigna", "Asignarlo a quien esté libre", "Pedir a la persona más rápida aunque no tenga registro", "El cumplimiento de la WPS y la calificación no se negocia por apuro."),
    sc=[
        ("En Mecánica Industrial: ¿qué es una unión en filete?", "La que junta dos piezas puestas en ángulo", "El filete une piezas en ángulo."),
        ("¿Qué se revisa además del proceso y la posición en un registro de calificación?", "Su vigencia", "Un registro vencido no respalda la tarea."),
        ("¿Qué pasa si no existe una WPS para el trabajo pedido?", "No se asigna hasta contar con una", "Sin WPS no hay procedimiento que respalde la unión."),
    ],
    op=("Ficha de ejemplo: trabajo pedido TX: unión a tope con arco manual en posición plana. WPS disponibles: WPS-A, arco manual, plana, a tope; WPS-B, MIG, plana, a tope. Registros: Persona U, arco manual plana, vigente; Persona V, MIG plana, vigente; Persona W, arco manual plana, vencido. Escribe (a) qué WPS usarías, (b) quién puede asumir TX, (c) por qué las otras dos personas no, (d) qué harías si no hubiera ninguna persona calificada vigente.",
        "(a) WPS-A, porque cubre arco manual, plana y a tope. (b) La persona U. (c) V tiene otro proceso y W tiene el registro vencido. (d) Informar a la jefatura para que no asigne el trabajo hasta renovar una calificación vigente.",
        ["elige la WPS correcta", "elige a la persona vigente", "explica por qué las otras no", "propone qué hacer sin personas calificadas"],
        ["hoja con las cuatro respuestas"],
        ["elegir la WPS por el nombre", "olvidar la vigencia", "asignar a quien está libre"],
        "Pregunta: «¿el registro cubre este proceso y está vigente?». Si duda, pídele que revise ambos datos persona por persona."),
    reinforce="Escribe una tabla con dos trabajos, dos WPS y dos personas, y marca quién puede asumir cada trabajo.",
    extend="Explica con un ejemplo por qué una WPS correcta no basta si la persona no está calificada.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (planilla de cordón de soldadura de ejemplo, inventada; solo cálculo en papel). Estructura de ejemplo con 4 uniones. Longitudes de cordón, en mm: U1, 1.500; U2, 2.200; U3, 800; U4, 1.000. "
     "Consumo de material de aporte de ejemplo: 120 g por cada 1.000 mm de cordón. Precio de ejemplo del material de aporte: $4.000 el kilogramo. "
     "Tiempo de ejemplo: se avanzan 250 mm de cordón por hora de trabajo en arco. Se agrega una holgura de 10 % de ejemplo al material por pérdidas (descuentos y puntas).")
build(
    O3, 4, F,
    use="Aprenderé a calcular en una planilla la longitud total de cordón, el material de aporte, el costo y el tiempo de una estructura con datos de ejemplo.",
    prior=["Sé multiplicar, dividir y sumar enteros.", "Sé pasar de gramos a kilogramos.", "Sé qué es un porcentaje simple."],
    explain=[
        "El cordón de soldadura es el material depositado en la unión, y su longitud se mide a lo largo de la unión. Una planilla de cordón suma las longitudes de todas las uniones de una estructura y, con un consumo de ejemplo por metro de cordón, calcula la masa de material de aporte necesaria. Con el precio por kilogramo se obtiene el costo, y con un avance de ejemplo por hora se obtiene el tiempo de trabajo.",
        "Se agrega una holgura, un porcentaje extra para cubrir pérdidas. Para pasar de gramos a kilogramos se divide por 1.000. Los valores de este cuaderno son de ejemplo: los reales los fija la WPS, el fabricante del material y la norma vigente. Una planilla bien hecha anota unidades, supuestos y quién la revisó.",
        f"Es solo un cálculo en papel; no se prepara ni se ejecuta ninguna soldadura. {EMER} {AVISO}",
    ],
    vocab=[("cordón de soldadura", "material depositado a lo largo de la unión"), ("material de aporte", "material que se agrega para formar el cordón"), ("planilla de cordón", "tabla que suma longitudes y calcula material, costo y tiempo"), ("holgura", "porcentaje extra que cubre pérdidas"), ("consumo", "cantidad de material por unidad de longitud de cordón")],
    worked=[
        ("Material de una unión", "Un cordón de ejemplo mide 3.000 mm y se consumen 100 g por cada 1.000 mm. ¿Cuántos gramos de material se necesitan?", ["3.000 mm son 3 veces 1.000 mm.", "3 por 100 son 300."], "300 g"),
        ("Costo", "Un pedido de ejemplo necesita 2 kg de material y cada kg cuesta $3.000. ¿Cuánto cuesta?", ["Se multiplican los kilogramos por el precio.", "2 por 3.000 son 6.000."], "$6.000"),
    ],
    mistakes=[("Sumar gramos y kilogramos sin convertir.", "Las unidades distintas no se pueden sumar directamente.", "Convierte todo a gramos o todo a kilogramos antes de calcular."),
              ("Calcular el tiempo con la masa en vez de la longitud.", "El avance por hora se mide sobre la longitud del cordón.", "Usa la longitud total dividida por el avance por hora.")],
    T=[
        ("abc", "En Mecánica Industrial: ¿qué es el cordón de soldadura?", "El material depositado a lo largo de la unión", "El cable del equipo de soldadura", "La pieza que se corta antes de unir", "El cordón es el material depositado en la unión."),
        ("abc", "En Mecánica Industrial: ¿para qué sirve la holgura en una planilla de cordón?", "Para cubrir pérdidas de material con un porcentaje extra", "Para reducir el costo del material", "Para aumentar el avance por hora", "La holgura es un margen por pérdidas."),
        ("abc", "En Mecánica Industrial: ¿qué dato permite calcular el tiempo de trabajo a partir de la longitud total del cordón?", "El avance por hora", "El precio por kilogramo", "La holgura", "Longitud dividida por avance da las horas."),
        ("=", "{F} ¿Cuántos mm de cordón suman las cuatro uniones?", "1500+2200+800+1000", "Se suman las longitudes de las cuatro uniones.", " mm"),
        ("abc", "{F} ¿Cuál es el consumo de material de aporte de ejemplo por cada 1.000 mm de cordón?", "120 g", "250 g", "4.000 g", "La ficha fija 120 g por 1.000 mm."),
        ("abc", "{F} ¿Por cuánto se divide la masa en gramos para pasarla a kilogramos?", "Por 1.000", "Por 100", "Por 10", "Un kilogramo equivale a 1.000 gramos."),
        ("=", "{F} ¿Cuántos gramos de material de aporte necesita la unión U2 sin holgura?", "2200*120//1000", "Se multiplica la longitud por el consumo y se divide por 1.000 mm.", " g"),
        ("=", "{F} ¿Cuántas horas de trabajo en arco requiere la unión U1?", "1500//250", "Se divide la longitud entre el avance por hora.", " horas"),
        ("=", "{F} ¿Cuántos gramos necesitan en total las cuatro uniones sin holgura? La longitud total es de 5.500 mm.", "5500*120//1000", "Se multiplica la longitud total por el consumo y se divide por 1.000.", " g"),
        ("abc", "{F} Un compañero calcula el costo multiplicando la longitud total en mm por el precio por kg. ¿Qué observación es correcta?", "Falta pasar primero la longitud a masa de material y la masa a kilogramos", "Está bien, porque mm y kg se pueden multiplicar", "Está bien, si agrega la holgura", "El costo depende de la masa en kg y no de los mm directamente."),
        ("abc", "{F} Se discute si la planilla debe incluir la holgura. ¿Qué respuesta es correcta?", "Conviene incluirla, porque hay pérdidas y el material necesario es mayor que el teórico", "No conviene, porque reduce el costo", "No conviene, porque el avance por hora la cubre", "La holgura es un margen que se suma al material teórico."),
        ("=", "{F} Con la holgura de 10 %, el material necesario es 660 g más su 10 %. ¿Cuántos gramos hay que preparar? El material sin holgura es de 660 g.", "660+660//10", "Se suma al material el 10 % de ese mismo material.", " g"),
        ("=", "{F} Con 726 g de material y un precio de $4.000 el kilogramo, ¿cuántos pesos cuesta el material?", "726*4000//1000", "Se multiplica la masa en gramos por el precio del kilogramo y se divide por 1.000.", " pesos"),
    ],
    ctx=("abc", "Un cliente de ejemplo pregunta cuánto material de aporte debe comprar para la estructura, pero la planilla solo tiene la longitud total. ¿Qué dato necesitas para calcularlo?", "El consumo de material por cada 1.000 mm de cordón", "El color de la estructura", "El número de personas del taller", "La longitud y el consumo permiten calcular el material."),
    sc=[
        ("En Mecánica Industrial: ¿qué es la holgura?", "Un porcentaje extra para cubrir pérdidas", "Se suma al material teórico calculado."),
        ("¿Cómo se pasa de gramos a kilogramos?", "Dividiendo por 1.000", "Un kilogramo equivale a 1.000 gramos."),
        ("¿Qué dato se divide por el avance por hora para obtener las horas?", "La longitud total del cordón", "Longitud dividida por avance da las horas."),
    ],
    op=("Ficha de ejemplo: una estructura tiene tres uniones de 2.000 mm, 1.000 mm y 3.000 mm. Consumo de ejemplo: 100 g por cada 1.000 mm. Avance de ejemplo: 500 mm por hora. Precio de ejemplo: $5.000 el kilogramo. Escribe (a) la longitud total de cordón, (b) los gramos de material sin holgura, (c) el tiempo en horas, (d) el costo del material sin holgura en pesos de ejemplo.",
        "(a) 2.000 + 1.000 + 3.000 = 6.000 mm. (b) 6.000 × 100 ÷ 1.000 = 600 g. (c) 6.000 ÷ 500 = 12 horas. (d) 600 g son 0,6 kg y a $5.000 el kg son $3.000; con enteros: 600 × 5 = 3.000 pesos de ejemplo.",
        ["suma las longitudes", "calcula gramos", "calcula las horas", "calcula el costo con las unidades correctas"],
        ["hoja con los cuatro cálculos y sus unidades"],
        ["no convertir unidades", "olvidar dividir por el avance", "usar la masa en vez de la longitud para el tiempo"],
        "Pregunta: «¿el precio es por gramo o por kilogramo?». Si duda, pídele que escriba la conversión antes de calcular."),
    reinforce="Inventa tres longitudes de cordón y calcula su suma, el material con un consumo de ejemplo y el tiempo con un avance de ejemplo.",
    extend="Explica con un ejemplo por qué hay que convertir unidades antes de calcular un costo.",
)
