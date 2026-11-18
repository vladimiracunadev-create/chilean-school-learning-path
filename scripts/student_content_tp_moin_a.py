"""Montaje Industrial TP 3.º y 4.º medio: OAE-01 (planos, simbología e instrumentos), OAE-02 (medir y calcular) y OAE-03 (trazar el área de maniobras). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_moin_common import AVISO, EMER, build

O1 = "TP-MOIN-3y4-OAE-01"
O2 = "TP-MOIN-3y4-OAE-02"
O3 = "TP-MOIN-3y4-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La empresa ficticia «Montajes Demo» recibe la carpeta de una nave industrial de ejemplo: 6 láminas de estructura, 3 de ubicación de equipos, "
     "2 de cañerías y 1 eléctrica, más unas especificaciones técnicas. Peligros anotados en la carpeta: piezas que se izan sobre una zona de paso, soldadura en terreno, trabajo a distintas alturas y caída de objetos.")
build(
    O1, 1, F,
    use="Aprenderé qué es el montaje industrial, qué documentos trae la carpeta de un proyecto, cómo se distinguen peligro y riesgo y cómo se ordenan las medidas de prevención.",
    prior=["Sé leer una tabla y un dibujo simple.", "Sé sumar, restar y dividir números enteros.", "Sé que una obra se hace según documentos escritos."],
    explain=[
        "El montaje industrial consiste en llevar a su lugar definitivo, según planos, las estructuras metálicas, los equipos, las cañerías, los ductos y los sistemas eléctricos de una planta, y dejarlos fijos y funcionando. Todo parte de la carpeta del proyecto: las láminas de planos, que son dibujos técnicos a escala, y las especificaciones técnicas, que fijan materiales y calidades. Cada lámina trae un rótulo, el recuadro con el nombre del proyecto, la escala, la fecha y la revisión.",
        "En el montaje hay peligros: un peligro es una fuente que puede causar daño, y el riesgo es la posibilidad de que ese daño ocurra. Para prevenir se usa la jerarquía de controles, de la más a la menos efectiva: eliminar el peligro, sustituirlo por otro menor, aplicar controles de ingeniería (barreras físicas que cambian el lugar o la máquina), aplicar controles administrativos (reglas, señales, permisos y capacitación) y, como última barrera, el equipo de protección personal (EPP). El EPP protege a una sola persona y no quita el peligro.",
        f"Las tareas de riesgo se hacen con un permiso de trabajo, un documento que emite la persona responsable antes de comenzar. La Dirección del Trabajo fiscaliza que se cumpla la normativa laboral. {EMER} {AVISO}",
    ],
    vocab=[("montaje industrial", "instalar y fijar en su lugar, según planos, estructuras, equipos y cañerías de una planta"), ("peligro", "fuente con capacidad de causar daño"), ("riesgo", "posibilidad de que un peligro cause daño"), ("jerarquía de controles", "orden de las medidas de prevención, de la más a la menos efectiva"), ("EPP", "equipo de protección personal, la última barrera"), ("permiso de trabajo", "documento que autoriza una tarea de riesgo antes de comenzar"), ("rótulo", "recuadro de la lámina con nombre del proyecto, escala, fecha y revisión")],
    worked=[
        ("Peligro y riesgo", "Una viga de ejemplo queda suspendida sobre un pasillo. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la viga suspendida, porque puede causar daño.", "El riesgo es que se suelte y golpee a quien pase por debajo."], "Peligro: la viga suspendida; riesgo: que golpee a quien pase por debajo"),
        ("Clasificar un control", "En un taller de ejemplo se cambia una herramienta muy ruidosa por otra mucho más silenciosa. ¿A qué nivel de la jerarquía corresponde?", ["El peligro, el ruido, no desaparece del todo, pero se reduce.", "Reemplazar una cosa por otra menos dañina es sustituir."], "Sustitución"),
    ],
    mistakes=[("Creer que usar casco basta para quedar protegido en cualquier tarea.", "El EPP es la última barrera: no quita el peligro y protege solo a quien lo usa.", "Primero se elimina o se controla el peligro; el EPP se suma a esos controles."),
              ("Creer que leer los planos habilita para hacer la tarea que muestran.", "Las tareas de riesgo exigen autorización, instructor y norma vigente.", "Aprende aquí el concepto y deja la tarea a personal autorizado.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es el montaje industrial?", "Instalar y fijar en su lugar, según planos, las estructuras, equipos y cañerías de una planta", "Producir en serie las piezas dentro de una fábrica", "Calcular y diseñar la estructura de una planta antes de construirla", "El montaje lleva y deja en su lugar lo ya fabricado; fabricar en serie y diseñar son otras etapas."),
        ("abc", "En Montaje Industrial: ¿qué es un riesgo?", "La posibilidad de que un peligro cause daño a una persona o a un bien", "Un objeto pesado de la obra", "Un permiso escrito para una tarea", "El riesgo es la posibilidad de daño; el objeto es una fuente de peligro y el permiso es un documento."),
        ("abc", "En Montaje Industrial: ¿cuál es el orden de la jerarquía de controles, del más al menos efectivo?", "Eliminar, sustituir, controles de ingeniería, controles administrativos y EPP", "EPP, controles administrativos, controles de ingeniería, sustituir y eliminar", "Controles administrativos, EPP, eliminar, sustituir y controles de ingeniería", "Se prefiere quitar el peligro de raíz; el EPP queda como última barrera."),
        ("=", "{F} ¿Cuántas láminas de planos trae la carpeta de la ficha?", "6+3+2+1", "Se suman las láminas de estructura, equipos, cañerías y electricidad.", " láminas"),
        ("abc", "{F} ¿Qué documento de la carpeta fija los materiales y las calidades que se exigen?", "Las especificaciones técnicas", "El rótulo de cada lámina", "Las láminas de cañerías", "Las especificaciones técnicas fijan materiales y calidades; el rótulo solo identifica la lámina."),
        ("abc", "{F} Un cartel que avisa «no pasar bajo cargas suspendidas» en la zona de paso es un control de tipo:", "Administrativo, porque informa y ordena una conducta", "De ingeniería, porque cambia físicamente el lugar", "De eliminación, porque quita la carga", "Un cartel informa; no cambia el lugar ni quita el peligro."),
        ("abc", "{F} Se propone que personal autorizado ponga una barrera física que impida el paso de personas bajo la zona donde se izan piezas. ¿Qué tipo de control es?", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla", "De EPP, porque protege a las personas", "Una barrera física modifica el lugar y no depende de que cada persona obedezca."),
        ("=", "El prevencionista de ejemplo dicta charlas de seguridad: hay 36 montajistas y a cada charla caben 9 personas. ¿Cuántas charlas se necesitan?", "36//9", "Se divide el total de personas entre las que caben en cada charla.", " charlas"),
        ("abc", "{F} Un compañero dice: «como leí la carpeta, puedo hacer la soldadura en terreno». ¿Qué respuesta es correcta?", "Es falso: soldar exige personal calificado, norma vigente y permiso de trabajo", "Es cierto, si usa casco", "Es cierto, si otro compañero lo mira", "Leer la carpeta no habilita para una tarea de riesgo; casco y compañía tampoco."),
        ("abc", "Durante una visita de ejemplo a un patio de montaje, una pieza cae y una persona queda atrapada. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a intentar levantar la pieza", "Tirar de la ropa de la persona para sacarla rápido", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "En Montaje Industrial: ¿por qué el EPP es el último nivel de la jerarquía de controles?", "Porque protege solo a quien lo usa y no quita el peligro; si falla, la persona queda expuesta", "Porque basta con tenerlo disponible en la bodega", "Porque su uso es voluntario en terreno", "El EPP no elimina el peligro, por eso se usa después de las otras medidas."),
        ("=", "Una carpeta de ejemplo trae 24 láminas y se leen 4 por hora. ¿Cuántas horas de lectura se necesitan?", "24//4", "Se divide el total de láminas entre las que se leen por hora.", " horas"),
        ("abc", "¿Qué institución fiscaliza que se cumpla la normativa laboral en una empresa?", "La Dirección del Trabajo", "El Servicio de Impuestos Internos", "El Instituto Nacional de Estadísticas", "La Dirección del Trabajo fiscaliza lo laboral; las otras instituciones tienen funciones tributarias y estadísticas."),
    ],
    ctx=("abc", "El dueño de una bodega de ejemplo te dice: «ponte un casco y sube a ayudar con el montaje, tú ya sabes leer planos». ¿Qué respondes?", "Que no, porque trabajar en un montaje exige instructor autorizado, norma vigente y permiso, y que consultarás a un adulto responsable", "Que sí, porque con casco basta", "Que sí, pero solo en la parte más baja de la estructura", "Leer planos no habilita para trabajar, y el casco por sí solo no reemplaza la autorización ni los controles."),
    sc=[
        ("En Montaje Industrial: ¿qué es un peligro?", "Una fuente que puede causar daño, como una carga suspendida", "El peligro es la fuente; el riesgo es la posibilidad de daño."),
        ("En montaje industrial: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
        ("¿Qué tipo de control es un cartel de advertencia?", "Un control administrativo", "El cartel informa y ordena una conducta sin cambiar el lugar."),
    ],
    op=("La empresa ficticia «Montajes Demo» anota una tarea de ejemplo: unir dos piezas de una estructura a gran altura. Peligros anotados: caída de la persona y caída de chispas sobre un pasillo. Escribe (a) cuál es el peligro de caída y cuál el riesgo asociado, (b) un control administrativo para el pasillo, (c) un control de ingeniería para el mismo pasillo, (d) por qué el EPP no basta.",
        "(a) Peligro: trabajar a gran altura sin protección en el borde; riesgo: que la persona caiga y se lesione. (b) Un cartel y una orden de no pasar bajo la zona mientras dura la tarea. (c) Una barrera o cubierta física que impida el paso y retenga las chispas. (d) Porque el EPP es la última barrera: no quita el peligro y protege solo a quien lo usa. La tarea la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer el EPP como único control", "no aclarar que la tarea la hace personal autorizado"],
        "Pregunta: «¿qué control quitaría el peligro de raíz?». Si no responde, pídele que relea el primer nivel de la jerarquía."),
    reinforce="Escribe la jerarquía de controles en orden y pon junto a cada nivel un ejemplo inventado de una obra de montaje.",
    extend="Explica con un ejemplo por qué un permiso de trabajo es un control administrativo y no reemplaza a una barrera física.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (lámina descrita por escrito, de ejemplo, inventada). Lámina E-03 «Planta de la nave», escala 1:100, revisión C. Leyenda: P = pilar; V = viga; A = arriostre. "
     "Lista de piezas de la lámina: P1 (4 unidades), P2 (2 unidades), V1 (6 unidades), A1 (8 unidades). Distancias medidas con regla en la lámina: del eje 1 al eje 2, 6 cm; del eje 2 al eje 3, 9 cm. "
     "En la carpeta también hay una lámina E-03 con revisión B.")
build(
    O1, 2, F,
    use="Aprenderé los tipos de planos de montaje, a leer la leyenda y la lista de piezas, a pasar medidas de la lámina a la realidad y qué función cumple cada rol de la obra.",
    prior=["Sé qué es un plano y qué es la carpeta de un proyecto.", "Sé multiplicar por 50 o por 100.", "Sé que 100 cm son 1 m."],
    explain=[
        "Un proyecto de montaje usa varios tipos de planos. La planta es la vista de la obra desde arriba; el corte muestra una rebanada vertical; la elevación muestra una fachada o un costado; el detalle amplía una unión o una pieza. Los ejes son líneas de referencia numeradas o con letras desde las cuales se miden las posiciones. Cada pieza tiene una marca, un nombre corto como P1 o V3, y la lista de piezas ordena las marcas con sus cantidades. La leyenda explica los símbolos y las siglas.",
        "La escala 1:100 significa que 1 cm de la lámina equivale a 100 cm reales. La cota escrita sobre el dibujo manda sobre la medida tomada con regla, y si no coinciden se registra la diferencia. La letra de revisión indica la versión: se trabaja solo con la vigente. Un error o una duda no se corrigen a mano: los registra quien los detecta y los consulta el proyectista, que es quien diseña y emite las revisiones.",
        f"Cada rol tiene su función. El proyectista diseña. El inspector técnico de obra (ITO) revisa que lo construido cumpla los planos y las especificaciones. El jefe de terreno organiza el trabajo. El prevencionista vela por la seguridad. El personal calificado y autorizado ejecuta las tareas que la norma le permite. {EMER} {AVISO}",
    ],
    vocab=[("planta", "vista de la obra desde arriba"), ("corte", "vista de una rebanada vertical de la obra"), ("detalle", "dibujo ampliado de una unión o una pieza"), ("eje", "línea de referencia desde la cual se miden las posiciones"), ("marca", "nombre corto de una pieza, como P1 o V3"), ("lista de piezas", "tabla con las marcas y sus cantidades"), ("proyectista", "persona que diseña el proyecto"), ("ITO", "inspector técnico de obra, que revisa que lo construido cumpla los planos")],
    worked=[
        ("Pasar a la realidad", "Una lámina de ejemplo está a escala 1:50 y un tramo mide 10 cm. ¿Cuántos metros reales mide?", ["10 por 50 son 500 cm.", "500 cm son 5 m."], "5 m"),
        ("Contar la lista", "Una lista de ejemplo dice V2 (3 unidades) y V3 (5 unidades). ¿Cuántas vigas hay en total?", ["Las dos marcas son vigas.", "3 más 5 son 8."], "8 vigas"),
    ],
    mistakes=[("Usar una lámina sin mirar su letra de revisión.", "Puede ser una versión antigua con datos que ya cambiaron.", "Lee la revisión del rótulo y confirma que sea la vigente."),
              ("Cambiar una cota por cuenta propia porque «parece un error».", "Solo el proyectista modifica el diseño.", "Registra la duda y consúltala con la jefatura o el ITO.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué muestra un plano de planta?", "La vista de la obra desde arriba", "Una rebanada vertical de la estructura", "Una unión ampliada con sus medidas", "La planta muestra la obra desde arriba; el corte es vertical y el detalle amplía una unión."),
        ("abc", "En Montaje Industrial: ¿qué es la lista de piezas de una lámina?", "Una tabla con las marcas de las piezas y sus cantidades", "Un dibujo a escala del terreno", "El permiso para izar las piezas", "La lista ordena marcas y cantidades; no es un dibujo ni un permiso."),
        ("abc", "En Montaje Industrial: ¿quién revisa en obra que lo construido cumpla los planos y las especificaciones?", "El inspector técnico de obra (ITO)", "El proveedor de las piezas", "El operador de la grúa", "El ITO fiscaliza el cumplimiento del proyecto; el proveedor y el operador tienen otras funciones."),
        ("=", "{F} ¿Cuántas piezas suma la lista de la lámina?", "4+2+6+8", "Se suman las unidades de P1, P2, V1 y A1.", " piezas"),
        ("abc", "{F} ¿Qué significa la sigla A en la leyenda?", "Arriostre", "Anclaje", "Armadura", "La leyenda de la ficha dice que A es arriostre; las otras palabras no aparecen en ella."),
        ("=", "{F} ¿Cuántos centímetros reales hay del eje 1 al eje 2?", "6*100", "Se multiplican los centímetros de la lámina por la escala 100.", " cm"),
        ("=", "{F} ¿Cuántos metros reales hay del eje 1 al eje 3, pasando por el eje 2?", "(6+9)*100//100", "Se suman los centímetros de la lámina, se multiplican por 100 y se pasan a metros.", " m"),
        ("abc", "{F} ¿Qué corresponde hacer con las dos láminas E-03, la de revisión B y la de revisión C?", "Usar la vigente, que se confirma con el rótulo o con quien emitió el plano", "Usar la B porque llegó primero a la obra", "Mezclar datos de ambas según convenga", "Entre dos revisiones solo sirve la vigente; mezclar versiones lleva a errores."),
        ("abc", "Un montajista de ejemplo cree que una cota está equivocada. ¿Qué corresponde?", "Avisar a la jefatura o al ITO para que lo consulten al proyectista", "Corregir la cota a mano en su copia", "Ignorarlo porque no es su función", "Solo el proyectista cambia el diseño; quien detecta el error lo informa."),
        ("abc", "{F} Un compañero dice: «mido con regla el tramo entre ejes y no necesito la cota, porque el papel no se equivoca». ¿Qué respuesta es correcta?", "Es falso: la cota escrita manda y el papel puede estar deformado; las diferencias se registran", "Es cierto, porque la regla es más exacta que lo escrito", "Es cierto, si la lámina es la última revisión", "La cota escrita prevalece sobre la regla, aunque la lámina sea vigente."),
        ("abc", "{F} En la obra de ejemplo se discute si un pilar puede cambiarse de posición. ¿Quién debe aprobar el cambio de diseño?", "El proyectista, y el ITO deja constancia", "El prevencionista, porque vela por la obra", "El montajista que lo instala", "El diseño lo cambia quien lo diseñó; los demás roles registran o consultan."),
        ("=", "Un tramo de una lámina a escala 1:50 mide 18 cm y otro, en una lámina a escala 1:200, mide 5 cm. ¿Cuántos metros reales suman ambos?", "(18*50+5*200)//100", "Cada tramo se multiplica por la escala de su lámina, se suman los centímetros y se pasan a metros.", " m"),
        ("=", "{F} Cada pilar de la lista, P1 y P2, lleva 8 pernos de anclaje, las piezas que lo fijan a su base (dato de ejemplo). ¿Cuántos pernos de anclaje se necesitan para todos los pilares?", "(4+2)*8", "Se suman los pilares de la lista y se multiplican por los pernos de cada uno.", " pernos"),
    ],
    ctx=("abc", "En una reunión de ejemplo, un montajista dice: «el plano está mal, lo hago a mi manera». Como estudiante, ¿qué propones?", "Registrar la duda por escrito y consultar al proyectista y al ITO antes de hacer cambios", "Dejar que lo haga a su manera, porque tiene experiencia", "Cambiar el plano con lápiz para que quede igual a lo que hará", "Los cambios de diseño los aprueba quien diseñó y el ITO deja constancia."),
    sc=[
        ("En Montaje Industrial: ¿qué dato manda si la cota escrita y la regla no coinciden?", "La cota escrita, registrando la diferencia", "La cota prevalece sobre la regla y la diferencia se consulta."),
        ("En montaje industrial: ¿qué indica la letra de revisión de una lámina?", "La versión del plano", "Permite saber cuál es la versión vigente."),
        ("En montaje industrial: ¿quién emite una nueva revisión del plano?", "El proyectista", "Solo quien diseñó puede modificar el diseño."),
    ],
    op=("Ficha de ejemplo: lámina E-07 «Corte transversal», escala 1:50, revisión A. Leyenda: P = pilar; C = cercha. Lista de piezas: P3 (6 unidades), C1 (3 unidades). La altura de un pilar medida en la lámina es 11 cm. Escribe (a) qué tipo de plano es, (b) la altura real del pilar en centímetros, (c) cuántas piezas suma la lista, (d) a quién se consulta si una cota parece equivocada.",
        "(a) Un corte, porque muestra una vista vertical. (b) 11 × 50 = 550 cm. (c) 6 + 3 = 9 piezas. (d) A la jefatura o al ITO, que lo consultan al proyectista.",
        ["identifica el tipo de plano", "calcula bien la altura real", "suma las piezas", "indica a quién se consulta"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar por una escala equivocada", "sumar mal las piezas", "proponer corregir la cota por cuenta propia"],
        "Pregunta: «¿quién puede cambiar una cota?». Si no responde, pídele que relea el rol del proyectista."),
    reinforce="Inventa una lista de tres marcas de piezas con sus cantidades y súmalas.",
    extend="Explica con un ejemplo por qué el ITO y el proyectista no cumplen la misma función.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (registro de ejemplo, inventado; las lecturas las tomó personal autorizado y se entregan por escrito). Longitud proyectada de tres pilares: 3.480 mm. Tolerancia de ejemplo: más o menos 5 mm. "
     "Pilar A, leído con una cinta métrica graduada en milímetros (instrumento análogo): 3.482 mm. Pilar B, leído con un medidor de longitud de pantalla numérica (instrumento digital): 3.488 mm. "
     "Pilar C, leído con la misma cinta: 3.475 mm. La cinta tiene certificado de calibración vigente; el medidor digital tiene el certificado vencido.")
build(
    O1, 3, F,
    use="Aprenderé a distinguir instrumentos análogos y digitales, a leer una escala descrita por escrito y a decidir si una lectura es confiable según su calibración.",
    prior=["Sé qué es una tolerancia.", "Sé restar y comparar números enteros.", "Sé leer una tabla o un registro escrito."],
    explain=[
        "Un instrumento análogo muestra la medida con una aguja o una marca sobre una escala graduada; se lee viendo entre qué marcas queda. Un instrumento digital muestra un número en una pantalla. Ambos tienen resolución, la menor variación que pueden mostrar: una cinta graduada en milímetros no distingue medios milímetros. Leer una escala mirando desde un lado produce el error de paralaje, que cambia la lectura sin que la pieza cambie.",
        "La calibración compara un instrumento con un patrón conocido y deja constancia de su error en un certificado de calibración con fecha de vigencia. Un instrumento con certificado vencido no se usa en un control formal: su lectura queda en duda. Que el número sea digital no lo vuelve exacto. Cada lectura se registra con su instrumento, la fecha, quién la tomó y la unidad.",
        f"Las mediciones de una obra las toma personal capacitado y autorizado, con instrumentos calibrados. Aquí solo se aprende a leer y a juzgar registros escritos. {EMER} {AVISO}",
    ],
    vocab=[("instrumento análogo", "muestra la medida con una aguja o una marca sobre una escala"), ("instrumento digital", "muestra la medida como un número en una pantalla"), ("resolución", "menor variación que un instrumento puede mostrar"), ("paralaje", "error de lectura por mirar la escala desde un ángulo"), ("calibración", "comparación de un instrumento con un patrón conocido"), ("certificado de calibración", "documento con el error del instrumento y su fecha de vigencia"), ("tolerancia", "diferencia máxima aceptada entre lo proyectado y lo medido")],
    worked=[
        ("Leer una escala análoga", "Una regla de ejemplo está graduada en milímetros. El extremo de una pieza queda 7 marcas después de la marca de 120 mm. ¿Qué longitud se lee?", ["Cada marca vale 1 mm.", "120 más 7 son 127 mm."], "127 mm"),
        ("Aplicar la tolerancia", "Un tramo proyectado en 2.500 mm se lee en 2.497 mm con una tolerancia de ejemplo de más o menos 4 mm. ¿Cumple?", ["La diferencia es 2.500 menos 2.497, es decir 3 mm.", "3 es menor que 4: cumple."], "Sí, cumple"),
    ],
    mistakes=[("Creer que un número en pantalla es siempre exacto.", "El instrumento digital tiene resolución limitada y puede tener un error de calibración.", "Revisa el certificado de calibración y la resolución antes de confiar en la lectura."),
              ("Leer una escala análoga mirándola desde un lado.", "El paralaje cambia la lectura.", "El personal capacitado se ubica de frente a la escala; tú aprende el concepto y registra el dato.")],
    T=[
        ("abc", "En Montaje Industrial: ¿cómo se lee un instrumento análogo?", "Viendo en qué marca de una escala graduada queda una aguja o un borde", "Leyendo un número que aparece en una pantalla", "Contando las veces que suena una alarma", "Un instrumento análogo se lee sobre una escala; el número en pantalla es propio del digital."),
        ("abc", "En Montaje Industrial: ¿qué es la calibración de un instrumento?", "Compararlo con un patrón conocido y dejar constancia de su error", "Limpiarlo al terminar el día", "Guardarlo en su caja después de usarlo", "La calibración compara con un patrón; limpiar o guardar son cuidados distintos."),
        ("abc", "En Montaje Industrial: ¿qué es la resolución de un instrumento?", "La menor variación que puede mostrar", "El valor más grande que puede medir", "El tiempo que dura su batería", "La resolución es el escalón mínimo de lectura; el rango máximo es otra característica."),
        ("=", "{F} ¿Cuántos milímetros por sobre la longitud proyectada está la lectura del pilar B?", "3488-3480", "Se resta la longitud proyectada a la lectura del pilar B.", " mm"),
        ("abc", "{F} Según las lecturas registradas, ¿qué pilares quedan dentro de la tolerancia?", "A y C", "A y B", "Solo C", "A difiere 2 mm, C difiere 5 mm (en el límite) y B difiere 8 mm, por sobre la tolerancia."),
        ("abc", "{F} ¿Con qué tipo de instrumento se leyeron los pilares A y B, respectivamente?", "A con uno análogo y B con uno digital", "A con uno digital y B con uno análogo", "Ambos con instrumentos digitales", "La cinta graduada es análoga y el medidor de pantalla numérica es digital."),
        ("abc", "{F} El medidor digital del pilar B tiene el certificado de calibración vencido. ¿Qué corresponde con esa lectura?", "Registrarla como dudosa y pedir repetirla a personal autorizado con un instrumento calibrado", "Aceptarla porque la pantalla digital no se equivoca", "Restarle 8 mm para que cumpla la tolerancia", "Un certificado vencido deja la lectura en duda; modificar el dato oculta el problema."),
        ("=", "{F} ¿Cuántos milímetros de diferencia hay entre la lectura del pilar C y la longitud proyectada?", "3480-3475", "Se resta la lectura de C a la longitud proyectada.", " mm"),
        ("=", "Un manómetro análogo de ejemplo (instrumento de aguja que muestra una presión) tiene marcas pequeñas que valen 2 unidades de ejemplo cada una. La aguja queda 3 marcas por sobre la marca de 40. ¿Qué lectura se obtiene?", "40+3*2", "Se suma a 40 el valor de las 3 marcas, de 2 unidades cada una.", " unidades de ejemplo"),
        ("abc", "{F} Un compañero dice: «si la pantalla muestra 3.488 mm, el pilar B mide exactamente 3.488 mm». ¿Qué respuesta es correcta?", "Es falso: la pantalla tiene resolución limitada y su calibración está vencida", "Es cierto, porque la pantalla es digital", "Es cierto, si la pantalla está limpia", "Un número digital puede tener error de calibración y limitaciones de resolución."),
        ("abc", "Dos personas de ejemplo leen la misma escala análoga: una la mira de frente y otra desde un lado, y obtienen lecturas distintas. ¿Cómo se llama ese error?", "Error de paralaje", "Error de calibración", "Error de resolución", "El paralaje aparece por mirar la escala desde un ángulo; los otros errores tienen otra causa."),
        ("abc", "{F} El jefe pide cerrar el control con la frase «todos los pilares cumplen». ¿Qué respuesta es correcta?", "No: la lectura de B supera la tolerancia y viene de un instrumento con certificado vencido; debe repetirse con uno calibrado", "Sí: dos pilares cumplen y eso basta", "Sí: el promedio de las lecturas está dentro de la tolerancia", "Un control se cierra con cada pilar conforme y con lecturas confiables, no con un promedio."),
        ("=", "{F} ¿Cuántos milímetros de diferencia hay entre las lecturas de los pilares B y C?", "3488-3475", "Se resta la lectura menor a la mayor.", " mm"),
    ],
    ctx=("abc", "El jefe de terreno de ejemplo te dice: «usa el medidor digital de la caja aunque su certificado esté vencido; la pantalla se ve clara». ¿Qué respondes?", "Que un instrumento con certificado vencido no sirve para un control formal y que las mediciones las hace personal autorizado con uno calibrado", "Que sí, porque una pantalla clara garantiza exactitud", "Que sí, pero anotando una medida menor", "Un certificado vencido deja la lectura en duda, y la pantalla clara no corrige el error."),
    sc=[
        ("En Montaje Industrial: ¿qué es un instrumento digital?", "El que muestra la medida como un número en pantalla", "El digital muestra un número; el análogo usa una escala."),
        ("¿Qué documento dice si un instrumento fue calibrado y hasta cuándo?", "El certificado de calibración", "El certificado deja constancia del error y de la vigencia."),
        ("¿Qué provoca el error de paralaje?", "Mirar la escala desde un ángulo", "Cambia la lectura sin que cambie la pieza."),
    ],
    op=("Ficha de ejemplo: longitud proyectada de dos vigas, 6.000 mm; tolerancia de ejemplo de más o menos 6 mm. Viga D, leída con cinta graduada en milímetros: 6.005 mm. Viga E, leída con un medidor digital de certificado vencido: 6.007 mm. Escribe (a) la diferencia de cada viga, (b) cuáles cumplen la tolerancia con esos números, (c) qué harías con la lectura de la viga E y por qué.",
        "(a) D: 5 mm; E: 7 mm. (b) D cumple (5 es menor o igual que 6); E no cumple (7 supera 6). (c) Registrar la lectura como dudosa porque el certificado está vencido y pedir que personal autorizado la repita con un instrumento calibrado.",
        ["calcula bien las dos diferencias", "clasifica con la tolerancia", "reconoce el problema del certificado vencido"],
        ["hoja con las diferencias, la clasificación y la decisión"],
        ["considerar que la pantalla digital no necesita calibración", "calcular mal la diferencia", "proponer modificar el dato para que cumpla"],
        "Pregunta: «¿qué falta para confiar en la lectura de E?». Si no responde, pídele que relea la regla del certificado de calibración."),
    reinforce="Escribe dos diferencias entre un instrumento análogo y uno digital y un riesgo de lectura propio de cada uno.",
    extend="Explica con un ejemplo por qué una lectura sin instrumento, fecha ni unidad no sirve como registro.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (planilla de control de ejemplo, inventada; las medidas las tomó personal autorizado). Regla de la planilla: un control cumple si la diferencia entre lo medido y lo del plano es igual o menor que su tolerancia. "
     "C1, longitud de una viga: plano 6.000 mm; medido 6.004 mm; tolerancia 5 mm. C2, distancia entre ejes: plano 9.000 mm; medido 9.012 mm; tolerancia 10 mm. "
     "C3, cota de un apoyo: plano 1.200 mm; medido 1.197 mm; tolerancia 3 mm. C4, desplome de un pilar de 5 m de altura: se admite 1 mm por cada metro de altura; medido 4 mm.")
build(
    O1, 4, F,
    use="Aprenderé a controlar distintas magnitudes con una planilla, a decidir si cada control cumple su tolerancia y a registrar una no conformidad sin ocultarla.",
    prior=["Sé restar y comparar números enteros.", "Sé qué es una tolerancia y una cota.", "Sé leer una planilla con varias filas."],
    explain=[
        "Un control de verificación compara lo medido en obra con lo que manda el plano. Las magnitudes más comunes son la longitud, la distancia entre ejes, la cota (la altura de un punto respecto de un nivel de referencia) y el desplome, la desviación horizontal de un elemento que debería estar vertical. Cada control tiene su tolerancia, la diferencia máxima aceptada, y cumple si la diferencia es igual o menor que ella.",
        "Un desplome admisible puede darse por metro de altura: se multiplica la altura en metros por los milímetros admitidos por cada metro. Un control que no cumple se llama no conformidad y se registra con el valor medido, la fecha y quién lo midió. No se corrige a ojo ni se promedia con otros controles: cada uno se evalúa por separado y la no conformidad se informa a la jefatura o al ITO.",
        f"Las tolerancias de este cuaderno son de ejemplo; las reales las fija el proyecto y la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("control de verificación", "comparación de lo medido en obra con lo que manda el plano"), ("tolerancia", "diferencia máxima aceptada"), ("cota", "altura de un punto respecto de un nivel de referencia"), ("desplome", "desviación horizontal de un elemento que debería estar vertical"), ("no conformidad", "resultado que no cumple lo pedido"), ("planilla de control", "tabla donde se anotan lo proyectado, lo medido y el resultado")],
    worked=[
        ("Aplicar una tolerancia", "Con tolerancia de ejemplo de 8 mm, una distancia proyectada de 4.000 mm se mide en 4.011 mm. ¿Cumple?", ["La diferencia es 11 mm.", "11 es mayor que 8: no cumple y se registra como no conformidad."], "No cumple"),
        ("Desplome admisible", "Un criterio de ejemplo admite 2 mm de desplome por metro de altura. ¿Cuántos mm admite un pilar de 3 m?", ["Se multiplican los metros por los mm de cada metro.", "3 por 2 son 6 mm."], "6 mm"),
    ],
    mistakes=[("Dar por bueno el control entero porque la mayoría de los puntos cumple.", "Cada control es independiente y los que no cumplen quedan pendientes.", "Registra cada no conformidad e informa a la jefatura o al ITO."),
              ("Corregir a ojo un punto que no cumple para que «calce» con el plano.", "Se oculta el problema y se pierde el registro.", "Informa y espera la decisión de quienes corresponde.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es una tolerancia?", "La diferencia máxima que se acepta entre lo proyectado y lo medido", "La diferencia mínima obligatoria entre dos piezas", "El precio máximo de una pieza", "La tolerancia fija hasta dónde puede apartarse un valor del plano."),
        ("abc", "En Montaje Industrial: ¿qué es el desplome de un pilar?", "La desviación horizontal que tiene respecto de la vertical", "La altura total del pilar", "El peso que el pilar soporta", "El desplome mide cuánto se aparta el pilar de la vertical; no es altura ni carga."),
        ("abc", "En Montaje Industrial: ¿qué es una no conformidad?", "Un resultado de control que no cumple lo pedido", "Una lámina impresa dos veces", "Una pieza que llegó antes de lo previsto", "La no conformidad es un incumplimiento que se registra e informa."),
        ("=", "{F} ¿Cuántos milímetros de diferencia hay entre lo medido y lo del plano en el control C1?", "6004-6000", "Se resta el valor del plano al valor medido.", " mm"),
        ("=", "{F} ¿Cuántos milímetros de desplome se admiten para el pilar del control C4?", "5*1", "Se multiplican los metros de altura por el milímetro admitido por cada metro.", " mm"),
        ("abc", "{F} ¿Qué control no cumple la regla de la planilla?", "C2", "C1", "C3", "C2 difiere 12 mm y su tolerancia es 10 mm; C1 y C3 quedan dentro."),
        ("=", "{F} ¿Cuántos milímetros se pasa la diferencia de C2 por sobre su tolerancia?", "(9012-9000)-10", "Se calcula la diferencia de C2 y se le resta la tolerancia.", " mm"),
        ("abc", "{F} El control C3 queda justo en el límite. ¿Cumple?", "Sí, porque su diferencia de 3 mm es igual a la tolerancia", "No, porque la diferencia debe ser menor que la tolerancia", "No, porque lo medido es menor que lo del plano", "La regla de la planilla acepta diferencias iguales o menores que la tolerancia."),
        ("=", "{F} ¿Qué porcentaje de los cuatro controles cumple?", "3*100//4", "Se divide lo que cumple entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} Una supervisora dice: «C2 solo se pasa por 2 mm, déjalo como si cumpliera». ¿Qué respuesta es correcta?", "No: se registra como no conformidad e informa al ITO, porque 12 mm supera la tolerancia", "Sí: 2 mm son despreciables", "Sí: si C1 y C3 cumplen, se compensa", "La tolerancia es un límite; superarlo es no conformidad aunque sea poco."),
        ("abc", "En otro control de ejemplo, un pilar de 8 m de altura tiene un desplome medido de 7 mm. Con el criterio de la ficha de 1 mm por metro de altura, ¿cumple?", "Sí, porque el admisible es 8 mm y lo medido es 7 mm", "No, porque 7 mm supera el admisible de 5 mm de la ficha", "No, porque 7 mm es mayor que 1 mm", "El admisible se calcula con la altura de este pilar: 8 m por 1 mm da 8 mm."),
        ("abc", "{F} Alguien propone cerrar el control porque «el promedio de las diferencias es pequeño». ¿Qué respuesta es correcta?", "Cada control se evalúa por separado y el promedio no compensa uno que no cumple", "Es correcto, porque un promedio bajo muestra una obra buena", "Es correcto si el promedio es menor que 5 mm", "Cada control tiene su propia tolerancia; el promedio la oculta."),
        ("=", "En un control de ejemplo, una viga proyectada en 7.200 mm se mide en 7.195 mm con tolerancia de 6 mm. ¿Cuántos milímetros de margen quedan antes de salir de la tolerancia?", "6-(7200-7195)", "Se resta a la tolerancia la diferencia medida.", " mm"),
    ],
    ctx=("abc", "Una supervisora de ejemplo te entrega la planilla de la ficha y pregunta: «¿podemos cerrar el control hoy?». ¿Qué respondes?", "Que no, porque C2 no cumple y debe registrarse e informarse antes de cerrar", "Que sí, porque tres de cuatro controles cumplen", "Que sí, si se anota que C2 también cumple", "Una no conformidad abierta impide cerrar el control, y los registros no se alteran."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula el desplome admisible por metro de altura?", "Se multiplica la altura en metros por los milímetros admitidos por metro", "Es una multiplicación simple de altura por criterio."),
        ("¿Qué se hace con un control que no cumple?", "Registrarlo como no conformidad e informar a la jefatura o al ITO", "No se corrige a ojo porque se perdería el registro."),
        ("¿Cuándo cumple un control según la regla de la planilla de la ficha?", "Cuando la diferencia es igual o menor que la tolerancia", "El límite exacto cumple según esa regla."),
    ],
    op=("Ficha de ejemplo: regla: cumple si la diferencia es igual o menor que la tolerancia. D1, longitud de una viga: plano 4.000 mm; medido 4.003 mm; tolerancia 4 mm. D2, distancia entre ejes: plano 7.500 mm; medido 7.509 mm; tolerancia 8 mm. D3, desplome de un pilar de 6 m con 1 mm admitido por metro: medido 5 mm. Escribe (a) la diferencia de D1 y de D2, (b) el desplome admisible de D3, (c) cuáles cumplen, (d) qué harías con el que no cumple.",
        "(a) D1: 3 mm; D2: 9 mm. (b) 6 × 1 = 6 mm. (c) D1 cumple (3 ≤ 4) y D3 cumple (5 ≤ 6); D2 no cumple (9 > 8). (d) Registrarlo como no conformidad e informar a la jefatura o al ITO, sin corregirlo a ojo.",
        ["calcula las dos diferencias", "calcula el desplome admisible", "clasifica los tres controles", "indica qué hacer con la no conformidad"],
        ["hoja con las diferencias, el admisible y la clasificación"],
        ["usar la tolerancia de otro control", "calcular el desplome sin multiplicar por la altura", "proponer corregir a ojo"],
        "Pregunta: «¿qué pasa con un control cuya diferencia es justo la tolerancia?». Si no responde, pídele que relea la regla de la planilla."),
    reinforce="Inventa una planilla de tres controles de longitud con una tolerancia de ejemplo y marca cuál no cumple.",
    extend="Explica con un ejemplo por qué ocultar una no conformidad puede costar más que informarla.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (hoja de datos de ejemplo, inventada). Pilar: altura 4.500 mm; masa 450 kg. Viga: longitud 6.000 mm; masa 300 kg. Instrumentos que anota la hoja: una cinta métrica con certificado de calibración vigente "
     "y un medidor de fuerza (dinamómetro) con el certificado vencido. Regla de conversión de ejemplo para el cálculo en papel: una masa de 1 kg pesa 10 N (newtons).")
build(
    O2, 1, F,
    use="Aprenderé por qué se miden y se calculan magnitudes en el montaje, qué unidades se usan, la diferencia entre masa y peso y por qué un instrumento debe estar calibrado.",
    prior=["Sé sumar, restar, multiplicar y dividir números enteros.", "Sé que 1 m son 1.000 mm.", "Sé qué es una tolerancia."],
    explain=[
        "En el montaje se miden y se calculan longitudes, superficies, pendientes, masas, fuerzas, tiempos y rendimientos. Un cálculo equivocado puede hacer que una pieza no calce, que un soporte reciba más carga de la que aguanta o que se pida material de menos. La metrología es la ciencia de medir, con sus unidades y sus instrumentos. Las unidades más usadas son el milímetro (mm) y el metro (m) para longitud, el kilogramo (kg) y la tonelada (t) para masa, el newton (N) para fuerza, y la hora (h) para el tiempo. Una tonelada equivale a 1.000 kg.",
        "La masa es la cantidad de materia de una pieza y se mide en kg. El peso es la fuerza con que la Tierra atrae esa masa y se mide en newtons. Para calcular en papel este cuaderno usa la regla de ejemplo de que 1 kg pesa 10 N. La exactitud es qué tan cerca está una medida del valor verdadero; la precisión es qué tan parecidas son varias medidas repetidas. Un instrumento se calibra comparándolo con un patrón, y si su certificado está vencido, sus medidas quedan en duda. Un número sin unidad no es un dato: 300 puede ser kg, t o N.",
        f"Los pesos y las capacidades reales de una pieza o de un equipo vienen en planos, placas y documentos del fabricante; nunca se estiman a ojo ni se prueban moviendo la pieza. {EMER} {AVISO}",
    ],
    vocab=[("metrología", "ciencia de medir, con sus unidades e instrumentos"), ("masa", "cantidad de materia de una pieza, en kg"), ("peso", "fuerza con que la Tierra atrae una masa, en N"), ("newton (N)", "unidad de fuerza"), ("tonelada (t)", "unidad de masa que equivale a 1.000 kg"), ("exactitud", "qué tan cerca está una medida del valor verdadero"), ("precisión", "qué tan parecidas son varias medidas repetidas"), ("calibración", "comparación de un instrumento con un patrón conocido")],
    worked=[
        ("Convertir unidades", "Una pieza de ejemplo tiene 2 t de masa. ¿Cuántos kilogramos son?", ["Una tonelada son 1.000 kg.", "2 por 1.000 son 2.000 kg."], "2.000 kg"),
        ("De masa a peso", "Una pieza de ejemplo tiene 25 kg. ¿Cuántos newtons pesa con la regla de 1 kg = 10 N?", ["Se multiplica la masa por 10.", "25 por 10 son 250 N."], "250 N"),
    ],
    mistakes=[("Anotar un valor sin su unidad, como «viga: 300».", "No se sabe si son kg, t o N, y se puede confundir la carga.", "Escribe siempre el número con su unidad, la fecha y la fuente."),
              ("Confundir masa con peso y escribir kg donde corresponde N.", "Son magnitudes distintas: una es cantidad de materia y la otra una fuerza.", "Usa kg para masa y N para peso, con la regla de conversión indicada.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué estudia la metrología?", "La ciencia de medir, con sus unidades e instrumentos", "El diseño de las estructuras de acero", "El cálculo del costo de una obra", "La metrología trata de medir; diseñar y presupuestar son otras tareas."),
        ("abc", "En Montaje Industrial: ¿cuál es la diferencia entre masa y peso?", "La masa es la cantidad de materia, en kg; el peso es una fuerza, en newtons", "La masa es la fuerza y el peso se mide en kilogramos", "Son lo mismo y solo cambia el nombre según la pieza", "Masa y peso son magnitudes distintas con unidades distintas."),
        ("abc", "En Montaje Industrial: ¿qué es la exactitud de una medida?", "Qué tan cerca está del valor verdadero", "Cuántas veces se repite la medida", "Qué tan rápido mide el instrumento", "La exactitud compara la medida con el valor verdadero; repetir es otra característica."),
        ("=", "{F} ¿Cuántos kilogramos suman el pilar y la viga de la ficha?", "450+300", "Se suman las masas de las dos piezas.", " kg"),
        ("=", "{F} ¿Cuántos newtons pesa la viga de la ficha con la regla de conversión de la ficha?", "300*10", "Se multiplica la masa en kilogramos por 10.", " N"),
        ("abc", "{F} ¿Con qué instrumento de la hoja se puede confiar en una medida de longitud?", "Con la cinta métrica, porque tiene certificado vigente", "Con el dinamómetro, porque mide fuerza", "Con cualquiera, porque ambos están anotados en la hoja", "Un instrumento calibrado y vigente es la base de una medida confiable; el dinamómetro mide otra magnitud."),
        ("=", "{F} ¿Cuántos metros mide la viga de la ficha?", "6000//1000", "Se divide entre 1.000 los milímetros para obtener metros.", " m"),
        ("=", "Una pieza de ejemplo tiene 3 t de masa y otra 1.500 kg. ¿Cuántos kilogramos suman las dos?", "3*1000+1500", "Se pasan las toneladas a kilogramos y se suman las dos masas.", " kg"),
        ("abc", "{F} Un compañero propone usar el dinamómetro de certificado vencido para comprobar el peso de la viga. ¿Qué corresponde?", "No usarlo en un control formal y pedir a personal autorizado un instrumento calibrado", "Usarlo, porque medir con algo siempre es mejor que no medir", "Usarlo y restar 10 N al resultado", "Con certificado vencido la medida queda en duda; corregirla a gusto la vuelve inventada."),
        ("abc", "Una persona anota «viga: 300» sin unidad. ¿Por qué es un problema?", "Porque pueden ser kg, t o N y se puede confundir la carga", "Porque los registros solo se aceptan en toneladas", "Porque 300 es un número demasiado grande para una viga", "Sin unidad el dato no se puede interpretar con seguridad."),
        ("abc", "Un cálculo de ejemplo da para una pieza una masa 100 veces mayor que la de su placa de datos. ¿Qué corresponde?", "Revisar unidades y cifras antes de usarlo y consultar a quien hizo el cálculo", "Usar el cálculo porque es más reciente que la placa", "Usar el promedio entre el cálculo y la placa", "Una diferencia tan grande sugiere un error de unidades o de digitación que debe aclararse."),
        ("abc", "{F} Un compañero dice: «con la masa de 450 kg del pilar ya puedo calcular yo solo cómo izarlo». ¿Qué respuesta es correcta?", "Es falso: izar exige un plan de personas responsables, equipo autorizado y norma vigente; este cuaderno solo enseña a calcular en papel", "Es cierto, porque ya conoce la masa", "Es cierto, si el pilar está limpio y seco", "Conocer una masa no habilita para una maniobra; la maniobra la planifica y ejecuta personal autorizado."),
        ("=", "{F} Un camión de ejemplo lleva el pilar y 2 vigas como las de la ficha. ¿Cuántos kilogramos de masa suman las tres piezas?", "450+2*300", "Se suma la masa del pilar y la de las dos vigas.", " kg"),
    ],
    ctx=("abc", "Una compañera de ejemplo quiere comprobar «a mano» si una pieza de 450 kg es pesada, intentando moverla en el patio. ¿Qué respondes?", "Que no lo haga: el peso se lee en los documentos o lo mide personal autorizado, y ante un accidente no hay que acercarse y se avisa a un adulto responsable y a emergencias", "Que lo haga con cuidado, porque así aprende el peso real", "Que lo haga solo si usa guantes", "Mover piezas pesadas sin autorización es riesgoso, y el peso ya está en los documentos."),
    sc=[
        ("En Montaje Industrial: ¿en qué unidad se expresa el peso como fuerza?", "En newtons (N)", "El peso es una fuerza y su unidad es el newton."),
        ("¿Qué debe llevar siempre un dato medido o calculado?", "Su unidad", "Sin unidad el número no se puede interpretar."),
        ("¿Qué se hace con un instrumento de certificado vencido?", "No se usa para un control formal", "Su medida queda en duda hasta que se calibre."),
    ],
    op=("Hoja de ejemplo: una columna con masa de 600 kg y una viga con masa de 2 t. Regla de ejemplo: 1 kg pesa 10 N. Escribe (a) la masa de la viga en kilogramos, (b) la masa de las dos piezas juntas, (c) el peso de la columna en newtons, (d) por qué cada dato lleva su unidad.",
        "(a) 2 × 1.000 = 2.000 kg. (b) 600 + 2.000 = 2.600 kg. (c) 600 × 10 = 6.000 N. (d) Porque sin unidad no se sabe si el número es kg, t o N y se pueden confundir las cargas.",
        ["convierte las toneladas", "suma las masas", "calcula el peso en newtons", "explica la razón de la unidad"],
        ["hoja con las cuatro respuestas"],
        ["no pasar las toneladas a kilogramos", "escribir kg donde corresponde N", "olvidar la unidad en un resultado"],
        "Pregunta: «¿qué pasaría si la viga se anotara solo como 2?». Si no responde, pídele que relea la regla de la unidad."),
    reinforce="Escribe tres magnitudes del montaje con la unidad que usa cada una (longitud, masa y fuerza).",
    extend="Explica con un ejemplo por qué un instrumento calibrado y una unidad bien escrita evitan un error de carga.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (datos de ejemplo, inventados, para una planilla en papel). Pasarela de acceso: sube 600 mm en un recorrido horizontal de 12.000 mm. Cubierta de una nave: rectángulo de 20 m de largo por 12 m de ancho. "
     "Frontón triangular: base 12 m y altura 4 m. Regla de la planilla: pendiente en % = desnivel ÷ recorrido horizontal × 100, con ambos datos en la misma unidad. Una plancha de revestimiento cubre 4 m².")
build(
    O2, 2, F,
    use="Aprenderé a calcular pendientes y superficies de rectángulos y triángulos, a leer una pendiente escrita como razón y a saber quién responde por los cálculos.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé que 1 m son 1.000 mm.", "Sé qué es una escala y una cota."],
    explain=[
        "La pendiente expresa cuánto sube o baja un tramo respecto de su recorrido horizontal. Se calcula con la regla pendiente en porcentaje igual al desnivel dividido por el recorrido horizontal, por 100, con los dos datos en la misma unidad. Una pendiente también puede escribirse como razón: 1:50 significa que sube 1 por cada 50 del recorrido, es decir, 2 %. Dividir 100 entre el segundo número da el porcentaje cuando el primero es 1.",
        "La superficie mide cuánto cubre una figura plana y se expresa en metros cuadrados (m²). La del rectángulo es largo por ancho. La del triángulo es base por altura dividido entre 2, porque un triángulo ocupa la mitad del rectángulo que tiene su misma base y altura. Con la superficie y la cobertura de cada plancha se calcula cuántas planchas se necesitan.",
        f"Los cálculos de un proyecto los respalda una memoria de cálculo firmada por el profesional responsable, y el ITO revisa que la obra los cumpla. Aquí solo se practica el cálculo con datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("pendiente", "cuánto sube o baja un tramo respecto de su recorrido horizontal, en porcentaje"), ("desnivel", "diferencia de altura entre los extremos de un tramo"), ("recorrido horizontal", "largo del tramo medido en horizontal"), ("superficie", "cuánto cubre una figura plana, en m²"), ("memoria de cálculo", "documento firmado que justifica con cuentas el proyecto"), ("razón 1:50", "forma de escribir una pendiente: sube 1 por cada 50 de recorrido")],
    worked=[
        ("Calcular una pendiente", "Una canaleta de ejemplo baja 300 mm en un recorrido horizontal de 10.000 mm. ¿Qué pendiente tiene, en %?", ["Se divide 300 entre 10.000 y se multiplica por 100.", "300 por 100 son 30.000, y 30.000 entre 10.000 son 3."], "3 %"),
        ("Superficie de un rectángulo", "Un panel de ejemplo mide 8 m por 3 m. ¿Cuál es su superficie?", ["Se multiplica el largo por el ancho.", "8 por 3 son 24."], "24 m²"),
    ],
    mistakes=[("Calcular una pendiente con el desnivel en mm y el recorrido en m.", "Los datos quedan en unidades distintas y el resultado es 1.000 veces mayor o menor.", "Pasa ambos datos a la misma unidad antes de dividir."),
              ("Calcular la superficie de un triángulo como base por altura, sin dividir entre 2.", "Eso da la superficie del rectángulo completo, el doble de la correcta.", "Divide base por altura entre 2.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué expresa la pendiente de un tramo?", "Cuánto sube o baja el tramo respecto de su recorrido horizontal", "El peso del tramo", "La longitud total de la pieza", "La pendiente relaciona el desnivel con el recorrido horizontal, no con el peso."),
        ("abc", "En Montaje Industrial: ¿cómo se calcula la superficie de un rectángulo?", "Multiplicando el largo por el ancho", "Sumando los cuatro lados", "Dividiendo el largo por el ancho", "Sumar los lados da el perímetro, no la superficie."),
        ("abc", "En Montaje Industrial: ¿en qué unidad se expresa una superficie?", "En metros cuadrados (m²)", "En metros (m)", "En metros cúbicos (m³)", "La superficie mide área y se expresa en metros cuadrados."),
        ("=", "{F} ¿Qué pendiente en porcentaje tiene la pasarela de acceso?", "600*100//12000", "Se divide el desnivel entre el recorrido y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos metros cuadrados tiene la cubierta de la nave?", "20*12", "Se multiplica el largo por el ancho.", " m²"),
        ("=", "{F} ¿Cuántos metros cuadrados tiene el frontón triangular?", "12*4//2", "Se multiplica la base por la altura y se divide entre 2.", " m²"),
        ("abc", "{F} Un compañero calcula la pendiente de la pasarela como 600 ÷ 12 × 100, usando 12 m sin pasarlos a mm. ¿Qué error cometió?", "No puso ambos datos en la misma unidad", "Multiplicó por 100 en vez de por 10", "No cometió ningún error", "Un dato estaba en milímetros y el otro en metros; hay que unificar antes de dividir."),
        ("=", "{F} ¿Cuántas planchas se necesitan para cubrir la cubierta de la nave, sin considerar merma?", "20*12//4", "Se divide la superficie de la cubierta entre lo que cubre cada plancha.", " planchas"),
        ("abc", "Dos tramos de ejemplo: el tramo X sube 200 mm en 4.000 mm de recorrido y el tramo Y sube 300 mm en 10.000 mm. ¿Cuál tiene mayor pendiente?", "El tramo X, con 5 % frente a 3 %", "El tramo Y, porque sube más milímetros", "Tienen la misma pendiente", "La pendiente compara el desnivel con el recorrido; subir más milímetros no basta."),
        ("abc", "{F} Un compañero calcula la superficie del frontón como 12 × 4 = 48 m². ¿Qué error cometió?", "Olvidó dividir entre 2, porque el triángulo es la mitad del rectángulo", "Debió sumar la base y la altura", "Usó metros en vez de centímetros", "Base por altura da el rectángulo; el triángulo es la mitad."),
        ("abc", "Un plano de ejemplo escribe la pendiente de un tramo como 1:25. ¿Qué porcentaje es?", "4 %", "25 %", "1 %", "Sube 1 por cada 25 de recorrido, y 100 dividido entre 25 es 4."),
        ("=", "Un tramo de ejemplo de 8 m de recorrido horizontal tiene una pendiente de 3 %. ¿Cuántos centímetros de desnivel resultan?", "800*3//100", "Se pasan 8 m a 800 cm y se calcula el 3 % de esa cantidad.", " cm"),
        ("abc", "{F} El documento de ejemplo pide una pendiente máxima de 6 % para la pasarela (valor de ejemplo, no normativo). ¿Cumple la pasarela de la ficha?", "Sí, porque su pendiente de 5 % es menor que 6 %", "No, porque 600 mm es mayor que 6", "No se puede saber sin pesar la pasarela", "Se comparan los porcentajes: 5 % no supera el máximo de 6 %."),
    ],
    ctx=("abc", "La supervisora de ejemplo te pide el desnivel de una rampa de 10 m de recorrido horizontal con 4 % de pendiente. Un compañero dice que son 4 m. ¿Qué respondes?", "Que son 40 cm: 10 m son 1.000 cm y el 4 % de 1.000 cm es 40 cm", "Que son 4 m, porque el 4 % de 10 es 4", "Que son 14 cm, porque se suman 10 y 4", "El porcentaje se aplica al recorrido en una misma unidad; 4 m confunde los metros con el resultado."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula la superficie de un triángulo?", "Base por altura, dividido entre 2", "El triángulo ocupa la mitad del rectángulo con su base y altura."),
        ("¿Cómo se calcula la pendiente en porcentaje?", "Desnivel dividido por recorrido horizontal, por 100, en la misma unidad", "La pendiente compara dos longitudes expresadas igual."),
        ("¿En qué unidad se mide una superficie?", "En metros cuadrados", "El área se expresa en m²."),
    ],
    op=("Ficha de ejemplo: una rampa con 360 mm de desnivel en 9.000 mm de recorrido horizontal; un panel triangular con base de 10 m y altura de 6 m. Escribe (a) la pendiente de la rampa en %, (b) la superficie del panel, (c) si la rampa cumple una pendiente máxima de ejemplo de 5 %.",
        "(a) 360 × 100 ÷ 9.000 = 4 %. (b) 10 × 6 ÷ 2 = 30 m². (c) Sí cumple, porque 4 % no supera 5 %.",
        ["calcula la pendiente", "calcula la superficie del triángulo", "compara con el máximo"],
        ["hoja con los cálculos y la conclusión"],
        ["no dividir entre 2 en el triángulo", "mezclar mm con m", "decir que no cumple porque 360 es mayor que 5"],
        "Pregunta: «¿qué unidad tienen el desnivel y el recorrido?». Si no responde, pídele que relea la regla de la misma unidad."),
    reinforce="Calcula en papel la pendiente de un tramo de ejemplo que sube 200 mm en 8.000 mm y la superficie de un rectángulo de 7 m por 5 m.",
    extend="Explica con un ejemplo por qué se revisa una memoria de cálculo antes de pedir el material.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (lista de piezas de ejemplo, inventada). Viga V1: 4 unidades, masa de 250 kg cada una. Pilar P1: 2 unidades, masa de 400 kg cada una. Plancha base: 6 unidades, masa de 50 kg cada una. "
     "Regla de la planilla: 1 kg pesa 10 N. Una plancha de acero de ejemplo tiene 8 kg por cada m² y por cada mm de espesor (valor de ejemplo, simplificado). Una plancha de 2 m por 3 m tiene 10 mm de espesor. "
     "Un estante de bodega de ejemplo está rotulado para 2.000 kg.")
build(
    O2, 3, F,
    use="Aprenderé a calcular la masa total de un conjunto de piezas, el peso en newtons, la masa de una plancha y a comparar una carga con la capacidad rotulada de un soporte.",
    prior=["Sé la diferencia entre masa y peso.", "Sé sumar y multiplicar números enteros.", "Sé calcular la superficie de un rectángulo."],
    explain=[
        "La masa total de un conjunto se calcula sumando, por cada tipo de pieza, la cantidad por su masa unitaria. El peso en newtons se obtiene multiplicando la masa en kg por 10, con la regla de ejemplo del cuaderno. La masa de una plancha se calcula con su superficie, su espesor y los kilogramos por m² y por mm del material: masa igual a superficie por espesor por kilogramos por m² por mm.",
        "Un soporte, una estantería o un equipo tiene una capacidad rotulada: el límite de carga que indica su fabricante en una placa o documento. La carga total se compara con ese límite, y si lo supera, aunque sea poco, no se acepta. La capacidad nunca se estima a ojo. Cuando un peso se reparte por igual entre varios apoyos, cada apoyo recibe el total dividido por la cantidad de apoyos. Al sumar, todos los datos deben estar en la misma unidad: no se mezclan kg con N.",
        f"Estos cálculos son de planilla, con números de ejemplo, y no autorizan a mover, apilar ni cargar piezas. {EMER} {AVISO}",
    ],
    vocab=[("masa total", "suma de las masas de todas las piezas de un conjunto"), ("capacidad rotulada", "límite de carga que indica el fabricante en una placa o documento"), ("reparto de carga", "división del peso total entre los apoyos que lo reciben"), ("masa unitaria", "masa de una sola pieza"), ("espesor", "grosor de una plancha")],
    worked=[
        ("Masa de un conjunto", "Un conjunto de ejemplo tiene 5 soportes de 30 kg y 2 marcos de 90 kg. ¿Cuál es su masa total?", ["Soportes: 5 por 30 son 150 kg. Marcos: 2 por 90 son 180 kg.", "Se suma: 150 más 180 son 330 kg."], "330 kg"),
        ("Comparar con la capacidad", "Un banco de ejemplo está rotulado para 400 kg y se pretende dejar 3 piezas de 150 kg. ¿Se puede?", ["La carga total es 3 por 150, es decir 450 kg.", "450 supera los 400 kg rotulados: no se puede."], "No, porque 450 kg supera 400 kg"),
    ],
    mistakes=[("Comparar cada pieza con la capacidad del soporte y no el total.", "Varias piezas livianas pueden sumar más que el límite.", "Suma primero la masa total y compárala con la capacidad."),
              ("Sumar en una misma columna masas en kg y pesos en N.", "Son magnitudes distintas y el total no significa nada.", "Pasa todo a una misma unidad antes de sumar.")],
    T=[
        ("abc", "En Montaje Industrial: ¿cómo se obtiene la masa total de un conjunto de piezas?", "Sumando, por cada tipo de pieza, la cantidad por su masa unitaria", "Multiplicando entre sí las masas de todas las piezas", "Tomando la masa de la pieza más pesada", "La masa total es la suma de las masas; multiplicar las masas entre sí no tiene sentido físico."),
        ("abc", "En Montaje Industrial: ¿qué es la capacidad rotulada de un soporte?", "El límite de carga que indica su fabricante en una placa o documento", "La carga que alguien estima a ojo", "El peso del propio soporte vacío", "La capacidad la fija el fabricante; estimarla a ojo no es válido."),
        ("abc", "En Montaje Industrial: ¿en qué unidad se expresa una fuerza?", "En newtons (N)", "En kilogramos (kg)", "En metros cuadrados (m²)", "La fuerza se mide en newtons; el kilogramo es unidad de masa."),
        ("=", "{F} ¿Cuántos kilogramos suman las 4 vigas V1?", "4*250", "Se multiplica la cantidad de vigas por la masa de cada una.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos suman los 2 pilares P1 y las 6 planchas base juntos?", "2*400+6*50", "Se suma la masa de los pilares y la de las planchas base.", " kg"),
        ("=", "{F} ¿Cuál es la masa total de todas las piezas de la lista?", "4*250+2*400+6*50", "Se suman las masas de los tres tipos de pieza.", " kg"),
        ("=", "{F} ¿Cuántos newtons pesa un pilar P1?", "400*10", "Se multiplica la masa en kilogramos por 10.", " N"),
        ("=", "{F} ¿Cuántos kilogramos tiene la plancha de 2 m por 3 m y 10 mm de espesor?", "2*3*10*8", "Se multiplican la superficie, el espesor y los kilogramos por m² y por mm.", " kg"),
        ("abc", "{F} ¿Pueden guardarse en el estante rotulado todas las piezas de la lista?", "No, porque suman 2.100 kg y superan los 2.000 kg rotulados", "Sí, porque 2.000 kg es casi igual a 2.100 kg", "Sí, si se pone primero lo más pesado", "La carga total supera lo rotulado; el orden de las piezas no cambia ese total."),
        ("abc", "{F} Un compañero dice: «el estante aguanta, 2.100 kg es solo un poco más que 2.000 kg». ¿Qué respuesta es correcta?", "La capacidad rotulada es un límite: superarla, aunque sea poco, no se acepta", "Es correcto, porque 100 kg es una diferencia pequeña", "Es correcto si las piezas se reparten parejo", "Un límite rotulado no admite pasarlo; repartir no cambia la carga total."),
        ("=", "Un soporte de ejemplo recibe 4.800 N repartidos por igual entre 4 apoyos. ¿Cuántos newtons recibe cada apoyo?", "4800//4", "Se divide el peso total entre la cantidad de apoyos.", " N"),
        ("abc", "Una planilla de ejemplo mezcla en una misma columna masas en kg y pesos en N. ¿Por qué es peligroso sumar esa columna?", "Porque se suman magnitudes distintas y el total no significa nada", "Porque la suma siempre da un número muy grande", "Porque los newtons no se pueden sumar", "Primero hay que pasar todo a una unidad; si no, el total puede llevar a una sobrecarga."),
        ("=", "{F} Si el espesor de la plancha de 2 m por 3 m bajara de 10 mm a 5 mm, ¿cuántos kilogramos menos tendría?", "2*3*10*8-2*3*5*8", "Se resta la masa con 5 mm a la masa con 10 mm.", " kg"),
    ],
    ctx=("abc", "Un compañero de ejemplo quiere dejar sobre un banco rotulado para 250 kg las 6 planchas base de 50 kg cada una, porque «cada plancha pesa mucho menos que 250». ¿Qué respondes?", "Que no: 6 × 50 = 300 kg supera los 250 kg rotulados", "Que sí, porque cada plancha pesa menos que el límite", "Que sí, si las apila bien", "El límite se compara con el total de todas las piezas, no con cada una."),
    sc=[
        ("En Montaje Industrial: ¿con qué se compara la masa total de las piezas guardadas en un soporte?", "Con la capacidad rotulada del soporte", "El límite del fabricante es la referencia."),
        ("¿Cómo se calcula el peso en newtons con la regla del cuaderno?", "Multiplicando la masa en kg por 10", "La regla de ejemplo es 1 kg igual a 10 N."),
        ("¿Qué se hace antes de sumar datos en distintas unidades?", "Pasarlos todos a una misma unidad", "Sumar magnitudes distintas da un total sin sentido."),
    ],
    op=("Lista de ejemplo: marco M1, 3 unidades de 120 kg cada una; soporte S1, 5 unidades de 40 kg cada una. Regla de ejemplo: 1 kg pesa 10 N. Un banco de ejemplo está rotulado para 500 kg. Escribe (a) la masa total, (b) el peso total en newtons, (c) si todo cabe en el banco y por cuánto se pasa o sobra.",
        "(a) 3 × 120 + 5 × 40 = 360 + 200 = 560 kg. (b) 560 × 10 = 5.600 N. (c) No cabe: 560 kg supera 500 kg en 60 kg.",
        ["calcula la masa total", "calcula el peso en newtons", "compara con la capacidad y dice cuánto se pasa"],
        ["hoja con los tres cálculos"],
        ["comparar cada pieza con el banco y no el total", "olvidar multiplicar la cantidad", "decir que cabe porque 500 y 560 se parecen"],
        "Pregunta: «¿qué se compara con la capacidad del banco?». Si no responde, pídele que relea el ejemplo del banco rotulado."),
    reinforce="Inventa una lista de dos tipos de pieza con sus cantidades y masas, y calcula la masa total.",
    extend="Explica con un ejemplo por qué una capacidad rotulada no se estima a ojo.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados). Cuadrilla A: monta 36 m² de panel en 4 horas. Cuadrilla B: monta 50 m² de panel en 5 horas. Hay que montar 360 m² de panel (dato de ejemplo). "
     "Un agujero de ejemplo mide 22 mm, con tolerancia de más o menos 1 mm; el perno de ejemplo mide 20 mm. Holgura = diámetro del agujero menos diámetro del perno.")
build(
    O2, 4, F,
    use="Aprenderé a calcular rendimientos y tiempos, a leer una tolerancia como un rango, a calcular una holgura y a reconocer qué instrumento de metrología mide cada tipo de magnitud.",
    prior=["Sé dividir y multiplicar números enteros.", "Sé qué es una tolerancia.", "Sé calcular la superficie de un rectángulo."],
    explain=[
        "El rendimiento es la cantidad de trabajo que se hace por unidad de tiempo, por ejemplo metros cuadrados por hora. Se calcula dividiendo la cantidad de trabajo entre el tiempo. Con el rendimiento se estima el tiempo de un trabajo: tiempo igual a cantidad dividida por rendimiento. El rendimiento es un valor de referencia, y el clima, el acceso al lugar o las pausas de seguridad pueden cambiarlo, por eso un programa serio agrega holgura y nunca presiona a trabajar sin protección para cumplirlo.",
        "Una dimensión con tolerancia se lee como un rango: 50 mm con tolerancia de más o menos 2 mm va de 48 a 52 mm. La holgura entre un perno y su agujero es el diámetro del agujero menos el del perno; tiene un valor mínimo y uno máximo según la tolerancia. Cada instrumento mide lo suyo: la cinta métrica mide largos grandes, el pie de metro mide diámetros y espesores pequeños, el nivel muestra si una superficie está horizontal y el manómetro mide presión.",
        f"Los rendimientos y las tolerancias de este cuaderno son de ejemplo; los reales dependen del proyecto y de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("rendimiento", "cantidad de trabajo por unidad de tiempo, como m² por hora"), ("holgura", "diferencia entre el diámetro del agujero y el del perno"), ("rango de tolerancia", "intervalo entre el valor mínimo y el máximo aceptados"), ("pie de metro", "instrumento que mide diámetros y espesores pequeños"), ("nivel", "instrumento que muestra si una superficie está horizontal"), ("manómetro", "instrumento que mide presión")],
    worked=[
        ("Calcular un rendimiento", "Una cuadrilla de ejemplo monta 42 m² de panel en 6 horas. ¿Cuál es su rendimiento?", ["Se divide la cantidad de trabajo entre el tiempo.", "42 entre 6 son 7 m² por hora."], "7 m² por hora"),
        ("Rango de tolerancia", "Un tubo de ejemplo debe medir 80 mm con tolerancia de más o menos 3 mm. ¿Entre qué valores se acepta?", ["Mínimo: 80 menos 3 son 77 mm.", "Máximo: 80 más 3 son 83 mm."], "Entre 77 mm y 83 mm"),
    ],
    mistakes=[("Prometer una fecha usando el rendimiento como si fuera exacto.", "El clima, el acceso y las pausas de seguridad pueden alargar el trabajo.", "Agrega holgura al programa y registra el supuesto de rendimiento."),
              ("Calcular la holgura máxima con el diámetro mínimo del agujero.", "La holgura máxima ocurre con el agujero en su diámetro máximo.", "Calcula los extremos por separado: mínimo con el agujero mínimo, máximo con el máximo.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es el rendimiento de una cuadrilla?", "La cantidad de trabajo que hace por unidad de tiempo, como m² por hora", "El sueldo que se paga por hora", "El peso de la herramienta que usa", "El rendimiento mide trabajo hecho en un tiempo; el sueldo y el peso no lo miden."),
        ("abc", "En Montaje Industrial: ¿qué es la holgura entre un perno y su agujero?", "La diferencia entre el diámetro del agujero y el del perno", "La suma de ambos diámetros", "El largo del perno", "La holgura es el espacio sobrante; sumar diámetros no tiene ese sentido."),
        ("abc", "En Montaje Industrial: ¿qué instrumento mide diámetros y espesores pequeños?", "El pie de metro", "La cinta métrica", "El manómetro", "El pie de metro mide piezas pequeñas; la cinta mide largos grandes y el manómetro, presión."),
        ("=", "{F} ¿Cuál es el rendimiento de la cuadrilla A, en m² por hora?", "36//4", "Se divide la superficie montada entre las horas.", " m² por hora"),
        ("=", "{F} ¿Cuál es el rendimiento de la cuadrilla B, en m² por hora?", "50//5", "Se divide la superficie montada entre las horas.", " m² por hora"),
        ("abc", "{F} ¿Qué cuadrilla tiene mayor rendimiento?", "La B, con 10 m² por hora frente a 9", "La A, porque trabaja menos horas", "Ninguna, porque montan cantidades distintas", "El rendimiento compara trabajo por hora, aunque las cantidades montadas sean distintas."),
        ("=", "{F} Si solo trabaja la cuadrilla B con su rendimiento, ¿cuántas horas se necesitan para montar los 360 m² de panel?", "360*5//50", "Se divide la superficie total entre el rendimiento de B, que es 50 entre 5.", " horas"),
        ("=", "{F} Si solo trabaja la cuadrilla A con su rendimiento, ¿cuántas horas se necesitan para montar los 360 m² de panel?", "360*4//36", "Se divide la superficie total entre el rendimiento de A, que es 36 entre 4.", " horas"),
        ("=", "{F} ¿Cuál es la holgura entre el agujero de 22 mm y el perno de 20 mm?", "22-20", "Se resta el diámetro del perno al del agujero.", " mm"),
        ("abc", "{F} ¿Cuál es la holgura mínima posible entre el perno y el agujero, según la tolerancia del agujero?", "1 mm, con el agujero en su diámetro mínimo de 21 mm", "2 mm, que es el valor nominal", "0 mm, porque el perno y el agujero deben ser iguales", "El agujero mínimo mide 21 mm, y 21 menos 20 da 1 mm."),
        ("abc", "{F} Un jefe dice: «la cuadrilla B rinde 10 m² por hora, así que hará los 360 m² en exactamente 36 horas sin importar nada». ¿Qué advertencia corresponde?", "El rendimiento es una referencia: clima, acceso y pausas de seguridad pueden cambiarlo, por eso se agrega holgura al programa", "Ninguna, porque un rendimiento es exacto", "Que hay que trabajar más rápido para cumplirlo", "Presionar con la velocidad aumenta el riesgo; el programa debe incluir holgura."),
        ("=", "Un sellante de ejemplo rinde 6 m de cordón por cartucho. ¿Cuántos cartuchos hacen falta para 90 m de cordón?", "90//6", "Se divide el largo total entre lo que rinde cada cartucho.", " cartuchos"),
        ("abc", "{F} La jefa necesita montar solo 180 m² en un máximo de 18 horas, con los rendimientos de la ficha. ¿Qué puede decir?", "La cuadrilla B alcanza justo, con 18 horas y sin margen; la A tardaría 20 horas", "Ambas cumplen, porque la diferencia es pequeña", "Ninguna cumple, porque 180 es más que 36", "B tarda 180 entre 10, es decir 18 horas; A tarda 180 entre 9, es decir 20 horas."),
    ],
    ctx=("abc", "Un jefe de ejemplo te pide: «anota que la cuadrilla terminó los 360 m² en 36 horas, aunque en realidad llevó 40». ¿Qué respondes?", "Que no se alteran los registros: se anota el tiempo real y las causas del retraso", "Que sí, para cumplir lo prometido", "Que sí, pero anotando 38 horas", "Un registro falso oculta problemas de rendimiento y afecta la planificación y la seguridad."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula el rendimiento de una cuadrilla?", "Dividiendo la cantidad de trabajo entre el tiempo", "El rendimiento es trabajo por unidad de tiempo."),
        ("¿Cómo se calcula la holgura entre un agujero y un perno?", "Restando el diámetro del perno al del agujero", "La holgura es el espacio sobrante."),
        ("¿Por qué se agrega holgura a un programa de obra?", "Porque el rendimiento es una referencia y puede cambiar", "El clima, el acceso y las pausas pueden alargar el trabajo."),
    ],
    op=("Ficha de ejemplo: cuadrilla C, 42 m² de panel en 6 horas; cuadrilla D, 56 m² en 7 horas. Hay que montar 168 m². Escribe (a) el rendimiento de cada cuadrilla, (b) cuántas horas tardaría cada una en los 168 m², (c) cuál termina antes y qué advertencia harías sobre el plazo.",
        "(a) C: 42 ÷ 6 = 7 m² por hora; D: 56 ÷ 7 = 8 m² por hora. (b) C: 168 ÷ 7 = 24 horas; D: 168 ÷ 8 = 21 horas. (c) D termina antes, pero el rendimiento es una referencia: se agrega holgura por clima, acceso y pausas de seguridad.",
        ["calcula los dos rendimientos", "calcula las horas de cada cuadrilla", "elige la más rápida y advierte sobre el plazo"],
        ["hoja con los cálculos y la advertencia"],
        ["dividir al revés", "decir que el plazo es exacto", "no considerar la seguridad en el plazo"],
        "Pregunta: «¿qué puede hacer que el trabajo tarde más?». Si no responde, pídele que relea el párrafo sobre el rendimiento como referencia."),
    reinforce="Calcula el rendimiento de una cuadrilla de ejemplo que monta 60 m de ducto en 5 horas, y el tiempo para 120 m.",
    extend="Explica con un ejemplo por qué una tolerancia se lee como un rango y no como un solo valor.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (sitio de ejemplo, inventado). Patio de premontaje de 40 m por 25 m. Los camiones entran por el portón norte. Hay una línea eléctrica aérea en el costado este y una oficina con paso de peatones en el costado oeste. "
     "Se prevé que las piezas suspendidas pasen por el centro del patio. La esquina sur-oeste tiene suelo blando. El plano de servicios muestra una cañería enterrada bajo el patio.")
build(
    O3, 1, F,
    use="Aprenderé qué es trazar un área de trabajo, qué es una zona de maniobras y una zona de exclusión, qué riesgos hay en un patio de montaje y qué significan los colores de las señales.",
    prior=["Sé calcular la superficie de un rectángulo.", "Sé qué es una lámina de plano y una escala.", "Sé qué es un permiso de trabajo."],
    explain=[
        "Trazar, o replantear, es llevar al terreno lo que dicen los planos: marcar ejes, niveles y límites con medidas y señales. El área de maniobras es la zona reservada para que se muevan piezas y equipos, y la zona de exclusión es el área donde nadie debe estar mientras hay una carga suspendida o una maniobra en curso. Ambas las define el plan de la tarea, no una opinión del momento, y las delimita personal autorizado antes de comenzar.",
        "Antes de reservar un área se revisan sus peligros: líneas eléctricas aéreas, que nunca se tocan ni se rodean de cerca; terreno blando o desnivelado; servicios enterrados como cañerías o cables, que se consultan en el plano de servicios antes de intervenir el suelo; y el cruce entre vehículos, cargas y peatones, que se evita con vías separadas. Las señales usan colores: rojo para prohibición, amarillo para advertencia, azul para obligación y verde para seguridad y salvamento.",
        f"Este cuaderno enseña a leer y calcular sobre el papel; no enseña a marcar, demarcar ni a mover piezas. {EMER} {AVISO}",
    ],
    vocab=[("trazado o replanteo", "llevar al terreno, con medidas y marcas, lo que dicen los planos"), ("área de maniobras", "zona reservada para el movimiento de piezas y equipos"), ("zona de exclusión", "área donde nadie debe estar mientras hay una carga suspendida o una maniobra en curso"), ("plano de servicios", "plano que muestra cañerías y cables enterrados"), ("señal azul", "indica una obligación"), ("señal roja", "indica una prohibición")],
    worked=[
        ("Calcular un área", "Un patio de ejemplo mide 30 m por 20 m. ¿Cuántos metros cuadrados tiene?", ["Se multiplica el largo por el ancho.", "30 por 20 son 600."], "600 m²"),
        ("Elegir el color de una señal", "Una señal de ejemplo dice «obligatorio usar protección auditiva». ¿Qué color corresponde?", ["Es una obligación.", "Las obligaciones se señalan en azul."], "Azul"),
    ],
    mistakes=[("Dar por libre un terreno porque se ve plano, sin mirar el plano de servicios.", "Pueden pasar cañerías o cables enterrados que no se ven.", "Consulta el plano de servicios y a la persona responsable antes de decidir."),
              ("Definir una zona de exclusión «a ojo» el día de la maniobra.", "Sin plan, se puede dejar gente dentro del área de caída de la carga.", "La zona la define el plan y la delimita personal autorizado.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es el trazado o replanteo de un área de trabajo?", "Llevar al terreno, con medidas y marcas, lo que dicen los planos", "Dibujar el plano de la obra en la oficina", "Calcular el costo del terreno", "El replanteo traslada el plano al terreno; dibujar o presupuestar son otras tareas."),
        ("abc", "En Montaje Industrial: ¿qué es una zona de exclusión?", "El área donde nadie debe estar mientras hay una carga suspendida o una maniobra en curso", "El área donde solo puede entrar personal con casco", "El área donde se guardan las piezas ya instaladas", "La exclusión impide la presencia de personas durante la maniobra; llevar casco no la reemplaza."),
        ("abc", "En Montaje Industrial: ¿qué color tiene una señal de prohibición, como «no pasar»?", "Rojo", "Azul", "Verde", "El rojo indica prohibición; el azul, obligación; el verde, seguridad y salvamento."),
        ("=", "{F} ¿Cuántos metros cuadrados tiene el patio de la ficha?", "40*25", "Se multiplica el largo por el ancho del patio.", " m²"),
        ("abc", "{F} ¿Qué peligro de la ficha exige que nadie se acerque y que se avise a la persona responsable?", "La línea eléctrica aérea del costado este", "La oficina del costado oeste", "El portón norte", "Una línea eléctrica aérea es un peligro grave; la oficina y el portón no lo son por sí mismos."),
        ("abc", "{F} ¿Dónde conviene consultar si hay servicios enterrados bajo el patio antes de intervenir el suelo?", "En el plano de servicios y con la persona responsable de la obra", "Preguntando a cualquier persona que pase", "Mirando la superficie del suelo", "Los servicios enterrados no se ven; se consultan en documentos."),
        ("abc", "{F} Las piezas suspendidas pasarán por el centro del patio y hay peatones que cruzan por el costado oeste. ¿Qué corresponde?", "Que el paso de los peatones quede separado de la ruta de las cargas, con vías y señales distintas", "Que los peatones crucen rápido cuando pasa la pieza", "Que los peatones crucen solo si usan casco", "Las cargas suspendidas y las personas no deben compartir la misma ruta."),
        ("=", "{F} Si el patio se divide en 4 zonas de igual superficie, ¿cuántos metros cuadrados tiene cada zona?", "40*25//4", "Se divide la superficie total entre las 4 zonas.", " m²"),
        ("abc", "{F} La esquina sur-oeste tiene suelo blando. ¿Qué corresponde respecto de esa esquina?", "Que la persona responsable decida en el plan si se usa para maniobras o se descarta", "Usarla igual, porque es la esquina más lejana", "Rellenarla con cualquier material disponible", "El suelo blando afecta la estabilidad de lo que se apoye; lo decide quien elabora el plan."),
        ("abc", "{F} Un compañero dice: «conozco el plano, así que marco yo la zona de exclusión con cintas mientras suben la pieza». ¿Qué respuesta es correcta?", "Es falso: la zona la define el plan y la delimita personal autorizado antes de comenzar la maniobra", "Es cierto, si usa cintas rojas", "Es cierto, si es de día", "Delimitar durante la maniobra deja a las personas expuestas; se hace antes y por personal autorizado."),
        ("abc", "Durante una visita de ejemplo, una pieza se suelta y cae cerca de ti sin heridos visibles. ¿Qué corresponde según las reglas generales?", "Alejarte de la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a revisar la pieza caída", "Seguir caminando, porque nadie salió herido", "Una pieza caída puede seguir inestable; se avisa a quienes pueden actuar."),
        ("=", "{F} Se pone un cartel de advertencia cada 8 m a lo largo de los 40 m del costado norte, con uno al comienzo y otro al final. ¿Cuántos carteles hacen falta?", "40//8+1", "Hay 5 tramos de 8 m y un cartel más al final del último tramo.", " carteles"),
        ("abc", "{F} Una jefa propone usar el centro del patio como acopio de piezas porque «tiene espacio libre». ¿Qué responde un técnico?", "Que el centro es la ruta de las cargas suspendidas, por lo que no puede ser acopio ni paso de personas", "Que está bien, porque hay espacio", "Que está bien si el acopio es bajo", "Un espacio libre no basta: el centro será ruta de cargas y debe quedar despejado."),
    ],
    ctx=("abc", "Un conductor de ejemplo quiere estacionar un camión alto bajo la línea eléctrica aérea del costado este «para ahorrar tiempo». ¿Qué respondes?", "Que no se acerque, que se avise a la persona responsable y que estacione donde indique el plan de tránsito", "Que sí, siempre que no toque los cables", "Que sí, pero solo unos minutos", "Acercarse a una línea eléctrica es un peligro grave; el lugar lo fija el plan de tránsito."),
    sc=[
        ("En Montaje Industrial: ¿quién define y delimita una zona de exclusión?", "El plan de la tarea y personal autorizado antes de comenzar", "No se improvisa durante la maniobra."),
        ("¿Dónde se consulta si hay cañerías o cables enterrados?", "En el plano de servicios", "Lo enterrado no se ve y se consulta en documentos."),
        ("¿Qué color indica una obligación?", "Azul", "Las señales de color azul indican una obligación de hacer algo."),
    ],
    op=("Ficha de ejemplo: patio de acopio de 30 m por 18 m. Entrada de camiones por el oeste; un cable eléctrico aéreo en el costado sur; una vía peatonal en el costado este; las cargas suspendidas pasarán por el centro. Escribe (a) cuántos metros cuadrados tiene el patio, (b) qué peligro exige avisar y no acercarse, (c) qué costado debe quedar separado de la ruta de las cargas, (d) quién define la zona de exclusión.",
        "(a) 30 × 18 = 540 m². (b) El cable eléctrico aéreo del costado sur. (c) El costado este, por la vía peatonal. (d) El plan de la tarea, y la delimita personal autorizado antes de comenzar.",
        ["calcula el área", "identifica el peligro eléctrico", "separa peatones y cargas", "indica quién define la zona de exclusión"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar mal el área", "proponer que los peatones crucen con casco", "decir que la zona la define cualquier trabajador"],
        "Pregunta: «¿qué haces si ves un cable eléctrico aéreo cerca de una maniobra?». Si no responde, pídele que relea la regla de no acercarse y avisar."),
    reinforce="Dibuja un patio de ejemplo con cuatro costados y escribe en cada uno un peligro inventado y el color de señal que corresponde.",
    extend="Explica con un ejemplo por qué la zona de exclusión se define antes de la maniobra y no durante ella.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (plano de replanteo descrito por escrito, de ejemplo, inventado). Ejes con letras A, B, C y D, separados cada 6 m. Ejes con números 1, 2, 3 y 4, separados cada 8 m. "
     "El punto de referencia es la intersección A-1. Un equipo de ejemplo, E-1, se ubica en la intersección B-3. El nivel de referencia (NR) es la cota 0; la base del equipo debe quedar 150 mm sobre el NR. "
     "El plan de maniobra de ejemplo está sin firma de la persona responsable.")
build(
    O3, 2, F,
    use="Aprenderé a leer un plano de replanteo con ejes y puntos de referencia, qué documentos respaldan una maniobra y qué función cumple cada rol.",
    prior=["Sé calcular la superficie de un rectángulo.", "Sé qué es una cota.", "Sé qué es una zona de exclusión."],
    explain=[
        "Un plano de replanteo muestra los ejes, las distancias entre ellos y la posición de cada equipo, medida desde un punto de referencia: un punto fijo y conocido. Una posición se nombra con la letra y el número de los ejes que se cruzan, como B-3. Las alturas se dan respecto de un nivel de referencia (NR), al que se asigna la cota 0: una cota positiva queda sobre el NR y una negativa, bajo él. La distancia entre el primer y el último eje es el número de espacios por la separación, no la cantidad de ejes por la separación.",
        "Antes de una maniobra se prepara un plan de izaje, un documento que reúne los datos de la carga, el equipo, la ubicación, la zona de exclusión y las personas responsables. Lo elabora y lo firma personal competente designado por la empresa. Sin plan firmado no se comienza. Los roles son: el topógrafo, que traza posiciones con instrumentos; el jefe de terreno, que organiza; el supervisor de montaje; el prevencionista; el señalero, que guía la maniobra con señales acordadas; y el operador autorizado del equipo.",
        f"Un rol no cambia el diseño: si dos láminas se contradicen, se registra y se consulta al proyectista. {EMER} {AVISO}",
    ],
    vocab=[("punto de referencia", "punto fijo y conocido desde el cual se miden las posiciones"), ("nivel de referencia (NR)", "altura a la que se asigna la cota 0"), ("plan de izaje", "documento que reúne carga, equipo, ubicación, zona de exclusión y responsables de una maniobra"), ("topógrafo", "persona que traza posiciones y niveles con instrumentos"), ("señalero", "persona que guía una maniobra con señales acordadas"), ("supervisor de montaje", "persona que dirige y controla el trabajo de montaje")],
    worked=[
        ("Distancia entre ejes", "Los ejes 1 a 5 de un plano de ejemplo están separados cada 5 m. ¿Cuántos metros hay entre el eje 1 y el eje 5?", ["Entre 5 ejes hay 4 espacios.", "4 por 5 son 20 m."], "20 m"),
        ("Leer una cota", "La base de un equipo de ejemplo queda 200 mm bajo el nivel de referencia. ¿Qué cota se anota?", ["Bajo el NR la cota es negativa.", "Se anota menos 200 mm."], "−200 mm"),
    ],
    mistakes=[("Calcular la distancia entre el primer y el último eje multiplicando la cantidad de ejes.", "Hay un espacio menos que ejes.", "Cuenta los espacios entre ejes y multiplica por la separación."),
              ("Empezar una maniobra con el plan de izaje sin firma «porque ya se habló».", "Sin firma no hay responsable ni aprobación.", "No se comienza hasta que el plan esté firmado.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es un punto de referencia en un plano de replanteo?", "Un punto fijo y conocido desde el cual se miden las posiciones", "El lugar donde se guarda el plano", "El punto más alto de la estructura", "Todas las posiciones se miden desde un punto conocido para que sean reproducibles."),
        ("abc", "En Montaje Industrial: ¿qué reúne un plan de izaje?", "Los datos de la carga, el equipo, la ubicación, la zona de exclusión y los responsables", "Solo el precio del equipo", "La lista de piezas de toda la obra", "El plan junta lo necesario para que la maniobra sea segura y revisable."),
        ("abc", "En Montaje Industrial: ¿qué función cumple el señalero?", "Guiar la maniobra con señales acordadas", "Diseñar el equipo", "Calcular la masa de la carga", "El señalero comunica la maniobra; el diseño y el cálculo son de otros roles."),
        ("=", "{F} ¿Cuántos metros hay entre el eje A y el eje D?", "3*6", "Hay 3 espacios entre los 4 ejes, de 6 m cada uno.", " m"),
        ("=", "{F} ¿Cuántos metros hay entre el eje 1 y el eje 4?", "3*8", "Hay 3 espacios entre los 4 ejes, de 8 m cada uno.", " m"),
        ("=", "{F} ¿Cuántos metros cuadrados tiene el rectángulo formado por los ejes A a D y 1 a 4?", "3*6*3*8", "Se multiplica el largo entre ejes A a D por el ancho entre ejes 1 a 4.", " m²"),
        ("abc", "{F} ¿A cuántos metros del eje A y del eje 1, en ese orden, está el equipo E-1?", "6 m y 16 m", "12 m y 24 m", "16 m y 6 m", "B está a un espacio de A (6 m) y el eje 3 está a dos espacios del eje 1 (16 m)."),
        ("abc", "{F} La base del equipo debe quedar 150 mm sobre el NR. ¿Qué cota se anota?", "+150 mm", "−150 mm", "0 mm", "Sobre el nivel de referencia la cota es positiva."),
        ("abc", "{F} El plan de maniobra está sin firma de la persona responsable. ¿Qué corresponde?", "No comenzar la maniobra hasta que esté firmado y aprobado", "Comenzar y firmar al terminar", "Pedir al señalero que lo firme", "Sin firma no hay responsable ni aprobación; la maniobra no empieza."),
        ("abc", "{F} Dos láminas de replanteo difieren en la posición de E-1: una dice B-3 y la otra B-2. ¿Qué corresponde?", "Registrar la discrepancia y consultar al proyectista antes de trazar", "Elegir B-3 porque es la más lejana", "Trazar entre B-2 y B-3", "Una discrepancia se aclara con quien diseñó; no se promedia ni se elige por gusto."),
        ("abc", "¿Quién debe elaborar y firmar el plan de izaje de una maniobra?", "Personal competente designado por la empresa, no un estudiante", "Cualquier persona que esté presente", "El proveedor de las piezas, sin revisión", "El plan exige competencia y responsabilidad designada."),
        ("=", "{F} ¿Cuántos metros cuadrados tiene la zona formada por los ejes B a C y 2 a 3?", "6*8", "Entre B y C hay 6 m y entre 2 y 3 hay 8 m; se multiplican.", " m²"),
        ("abc", "{F} Una compañera propone que el señalero cambie la posición de E-1 «por comodidad». ¿Qué respuesta es correcta?", "Es falso: la posición la fija el diseño; el señalero guía maniobras y no cambia el proyecto", "Es cierto, porque el señalero ve la maniobra en terreno", "Es cierto si lo avisa por radio", "Solo el proyectista cambia el diseño; los demás roles consultan."),
    ],
    ctx=("abc", "Un supervisor de ejemplo te pregunta qué documentos mirar para saber dónde reservar el área de maniobras y a qué distancia están los ejes. ¿Qué respondes?", "El plano de replanteo o de disposición general, y el plan de la maniobra, ambos en su revisión vigente", "Cualquier plano que esté a mano, aunque sea antiguo", "Solo la lista de piezas", "El área y los ejes salen de planos y planes vigentes, no de documentos antiguos."),
    sc=[
        ("En Montaje Industrial: ¿cuántos espacios hay entre 6 ejes?", "5 espacios", "Hay un espacio menos que ejes."),
        ("¿Qué cota tiene un punto bajo el nivel de referencia?", "Una cota negativa", "Bajo el NR la cota es negativa."),
        ("¿Qué se necesita antes de comenzar una maniobra?", "Un plan de izaje firmado por la persona responsable", "Sin plan firmado la maniobra no empieza."),
    ],
    op=("Ficha de ejemplo: ejes con letras A, B y C, separados cada 5 m; ejes con números 1, 2, 3 y 4, separados cada 7 m. El equipo E-2 se ubica en la intersección C-2. La base de E-2 debe quedar 100 mm bajo el nivel de referencia. Escribe (a) la distancia entre el eje A y el eje C, (b) la distancia entre el eje 1 y el eje 4, (c) a cuántos metros del eje 1 está E-2, (d) la cota de la base de E-2.",
        "(a) 2 espacios por 5 m son 10 m. (b) 3 espacios por 7 m son 21 m. (c) El eje 2 está a un espacio del eje 1: 7 m. (d) −100 mm.",
        ["cuenta bien los espacios", "calcula las distancias", "ubica E-2 desde el eje 1", "escribe la cota con signo"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar la cantidad de ejes por la separación", "olvidar el signo negativo", "contar mal los espacios"],
        "Pregunta: «¿cuántos espacios hay entre 4 ejes?». Si no responde, pídele que relea el párrafo de distancia entre ejes."),
    reinforce="Inventa un plano con 3 ejes de letras y 3 de números y calcula la distancia entre los ejes extremos.",
    extend="Explica con un ejemplo por qué una maniobra sin plan firmado no debe comenzar.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Zona de acopio de 20 m por 9 m. Se acopian 12 vigas; cada una ocupa 6 m por 1 m. Se reserva además un 50 % extra de superficie para pasillos de circulación (dato de ejemplo). "
     "Una zona alternativa P queda 9 m al este y 12 m al sur de una línea eléctrica aérea. Distancia mínima de ejemplo a esa línea: 20 m (valor de ejemplo, no normativo).")
build(
    O3, 3, F,
    use="Aprenderé a calcular la superficie que necesita un acopio con pasillos, a calcular una distancia en línea recta con la regla 3-4-5 y a descartar una ubicación que no cumple.",
    prior=["Sé calcular la superficie de un rectángulo.", "Sé calcular un porcentaje simple.", "Sé qué es una zona de exclusión."],
    explain=[
        "El acopio es el almacenamiento temporal y ordenado de piezas hasta que se montan. Para decidir si una zona sirve se compara la superficie que ocupan las piezas, más una reserva para pasillos de circulación, con la superficie disponible. Los pasillos permiten moverse y salir sin pasar sobre las piezas. Un porcentaje extra se calcula multiplicando la superficie por 100 más el porcentaje y dividiendo entre 100: con 20 % extra, se multiplica por 120 y se divide entre 100.",
        "Cuando una distancia se mide en dos direcciones perpendiculares, por ejemplo hacia el este y hacia el sur, la distancia en línea recta no es la suma. Con la regla 3-4-5, si los lados perpendiculares miden 3 y 4, la distancia en línea recta es 5; lo mismo vale para sus múltiplos, como 6 y 8 que dan 10. Si la distancia en línea recta es menor que el mínimo exigido a un peligro, la ubicación se descarta o se consulta a la persona responsable.",
        f"Las superficies, los porcentajes y las distancias mínimas de este cuaderno son de ejemplo y de planilla; en una obra real las fija el plan y la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("acopio", "almacenamiento temporal y ordenado de piezas hasta su montaje"), ("pasillo de circulación", "espacio libre para moverse y salir sin pasar sobre las piezas"), ("distancia en línea recta", "largo del camino más corto entre dos puntos"), ("regla 3-4-5", "con lados perpendiculares de 3 y 4 la línea recta mide 5, y sus múltiplos"), ("valor de ejemplo, no normativo", "número para practicar el cálculo que no reemplaza el valor de la norma vigente")],
    worked=[
        ("Distancia en línea recta", "Un punto está 6 m al este y 8 m al sur de un poste de ejemplo. ¿A qué distancia en línea recta está?", ["Los lados 6 y 8 son el doble de 3 y 4.", "La línea recta es el doble de 5, es decir 10 m."], "10 m"),
        ("Superficie con pasillos", "Diez piezas de ejemplo de 3 m por 1 m se acopian con un 40 % extra para pasillos. ¿Cuántos m² se necesitan?", ["Las piezas ocupan 10 por 3, es decir 30 m².", "Con 40 % extra: 30 por 140 entre 100 son 42 m²."], "42 m²"),
    ],
    mistakes=[("Sumar las dos distancias perpendiculares para obtener la distancia en línea recta.", "La línea recta es más corta que la suma de los dos lados.", "Usa la regla 3-4-5 o la relación entre los lados."),
              ("Llenar toda la zona con piezas sin dejar pasillos.", "Las personas quedarían atrapadas sin salida entre las piezas.", "Reserva siempre superficie para pasillos de circulación.")],
    T=[
        ("abc", "En Montaje Industrial: ¿para qué se reserva un pasillo de circulación en una zona de acopio?", "Para moverse y salir sin pasar sobre las piezas", "Para guardar más piezas", "Para que las piezas pesen menos", "El pasillo da libre tránsito y salida; no aumenta la capacidad de acopio."),
        ("abc", "En Montaje Industrial: ¿qué es el acopio?", "El almacenamiento temporal y ordenado de piezas hasta su montaje", "La unión definitiva de dos piezas", "La entrega final de la obra", "El acopio guarda piezas mientras llega su momento de montaje."),
        ("abc", "¿Qué significa que una distancia sea «de ejemplo, no normativa»?", "Que sirve para practicar el cálculo y no reemplaza el valor que fija la norma vigente", "Que es la distancia exigida por la norma", "Que puede cambiarse según la comodidad de la obra", "Un valor de ejemplo es didáctico; el real lo fija la norma."),
        ("=", "{F} ¿Cuántos metros cuadrados ocupan las 12 vigas?", "12*6*1", "Se multiplica la cantidad de vigas por lo que ocupa cada una.", " m²"),
        ("=", "{F} ¿Cuántos metros cuadrados tiene la zona de acopio?", "20*9", "Se multiplica el largo por el ancho de la zona.", " m²"),
        ("=", "{F} ¿Cuántos metros cuadrados se necesitan sumando el 50 % extra para pasillos?", "72*150//100", "Se multiplica por 150 y se divide entre 100 la superficie que ocupan las vigas.", " m²"),
        ("abc", "{F} ¿Caben las vigas con sus pasillos en la zona de acopio?", "Sí, se necesitan 108 m² y la zona tiene 180 m²", "No, porque 108 m² es mayor que 72 m²", "No, porque falta el 50 % extra", "El total necesario es menor que la superficie disponible."),
        ("abc", "{F} ¿A qué distancia en línea recta está la zona P de la línea eléctrica?", "15 m", "21 m", "3 m", "Los lados 9 y 12 son 3 veces 3 y 4; la línea recta es 3 veces 5, es decir 15 m."),
        ("abc", "{F} Con la distancia en línea recta calculada, ¿cumple la zona P el mínimo de ejemplo?", "No, porque 15 m es menor que 20 m", "Sí, porque 15 m es cercano a 20 m", "Sí, porque 9 más 12 es mayor que 20", "La distancia de 15 m no alcanza el mínimo de 20 m; se descarta o se consulta."),
        ("abc", "{F} Un compañero dice: «P cumple porque 9 m más 12 m son 21 m, que supera los 20 m». ¿Qué error comete?", "Sumó las dos distancias en vez de calcular la distancia en línea recta", "Debió multiplicarlas", "No comete ningún error", "La línea recta es más corta que la suma de los dos lados."),
        ("abc", "En un acopio de ejemplo, el apilado se desplaza y una pieza cae sobre el pasillo, con una persona atrapada. ¿Qué corresponde según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarse a mover la pieza entre varias personas", "Esperar a ver si la persona logra salir sola", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("=", "{F} Si se añaden 6 vigas más de las mismas medidas, con el mismo 50 % extra, ¿cuántos metros cuadrados se necesitan para las 18 vigas?", "18*6*1*150//100", "Se multiplica la superficie de las 18 vigas por 150 y se divide entre 100.", " m²"),
        ("=", "{F} Con 18 vigas y el 50 % extra, ¿cuántos metros cuadrados sobran en la zona de 20 m por 9 m?", "20*9-18*6*1*150//100", "Se resta la superficie necesaria a la superficie disponible.", " m²"),
    ],
    ctx=("abc", "Una jefa de ejemplo quiere acopiar en la zona P «porque está cerca del montaje». ¿Qué le respondes?", "Que a 15 m en línea recta de la línea eléctrica no cumple el mínimo de ejemplo de 20 m, y que se debe consultar a la persona responsable", "Que sí, porque la cercanía ahorra tiempo", "Que sí, si las piezas se apilan bajas", "La seguridad frente a la línea eléctrica pesa más que la cercanía."),
    sc=[
        ("En Montaje Industrial: ¿qué se compara para saber si un acopio cabe en una zona?", "La superficie necesaria con pasillos y la superficie disponible", "El acopio debe caber con espacio para circular."),
        ("¿Cuánto mide la línea recta si los lados perpendiculares miden 3 y 4?", "5", "Es la base de la regla 3-4-5."),
        ("¿Qué se hace si una ubicación queda más cerca de un peligro que el mínimo?", "Descartarla o consultar a la persona responsable", "La cercanía al peligro no se acepta por comodidad."),
    ],
    op=("Ficha de ejemplo: zona de acopio de 16 m por 8 m. Se acopian 10 perfiles de 5 m por 1 m, con un 40 % extra para pasillos. Una zona alternativa Q queda 12 m al este y 16 m al norte de una línea eléctrica aérea; el mínimo de ejemplo es 25 m. Escribe (a) cuántos m² ocupan los perfiles, (b) cuántos m² se necesitan con pasillos, (c) si caben en la zona, (d) la distancia en línea recta de Q a la línea y si cumple el mínimo.",
        "(a) 10 × 5 × 1 = 50 m². (b) 50 × 140 ÷ 100 = 70 m². (c) La zona tiene 16 × 8 = 128 m²: caben. (d) Los lados 12 y 16 son 4 veces 3 y 4, así que la línea recta mide 20 m; 20 es menor que 25 m, no cumple.",
        ["calcula la superficie de las piezas", "agrega el porcentaje de pasillos", "compara con la zona", "calcula la distancia y concluye"],
        ["hoja con los cuatro cálculos"],
        ["sumar 12 y 16 para la distancia", "olvidar el porcentaje extra", "decir que cumple porque 20 está cerca de 25"],
        "Pregunta: «¿la distancia en línea recta es la suma de los dos lados?». Si no responde, pídele que relea la regla 3-4-5."),
    reinforce="Calcula en papel cuántos m² ocupan 8 piezas de 4 m por 1 m con un 25 % extra de pasillos.",
    extend="Explica con un ejemplo por qué un pasillo de circulación es una medida de seguridad y no un desperdicio de espacio.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (planilla de verificación de un trazado de ejemplo; las medidas las tomó personal autorizado). Rectángulo de ejes de 6.000 mm por 8.000 mm. Diagonal 1 medida: 10.004 mm. Diagonal 2 medida: 9.997 mm. "
     "Regla de ejemplo: el trazado cumple si las dos diagonales difieren en 10 mm o menos. Cotas de tres puntos respecto del nivel de referencia: P1 = 0 mm; P2 = +4 mm; P3 = −7 mm. Tolerancia de cota de ejemplo: 5 mm.")
build(
    O3, 4, F,
    use="Aprenderé a interpretar una planilla de verificación de un trazado, a usar las diagonales para ver si un rectángulo está a escuadra y a juzgar cotas con su tolerancia.",
    prior=["Sé qué es una cota y un nivel de referencia.", "Sé qué es una tolerancia.", "Sé la regla 3-4-5."],
    explain=[
        "Un trazado está a escuadra cuando los ejes forman ángulos rectos. En un rectángulo bien trazado las dos diagonales miden lo mismo, y su valor ideal se calcula con la regla 3-4-5: un rectángulo de 3 m por 4 m tiene diagonal de 5 m. Si las diagonales medidas difieren más que la tolerancia, el trazado no está a escuadra y se registra como no conformidad.",
        "Las cotas de los puntos se comparan con el nivel de referencia y con su tolerancia: un punto cumple si su cota está entre el valor menos la tolerancia y el valor más la tolerancia. Un signo negativo indica que el punto queda bajo el nivel de referencia. La planilla de verificación debe dejar escritos los valores medidos, la regla usada, el resultado, la fecha y quién midió. Una planilla con solo «ok» no sirve.",
        f"Las mediciones de un trazado las toma personal autorizado con instrumentos calibrados; aquí solo se interpretan datos escritos. Las reglas y tolerancias son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("a escuadra", "con ángulos rectos entre los ejes"), ("diagonal", "línea que une dos esquinas opuestas de un rectángulo"), ("cota", "altura de un punto respecto del nivel de referencia"), ("planilla de verificación", "tabla que registra valores medidos, regla usada, resultado, fecha y responsable"), ("no conformidad", "resultado que no cumple lo pedido")],
    worked=[
        ("Comparar diagonales", "Un rectángulo de ejemplo de 3.000 mm por 4.000 mm tiene diagonales medidas de 5.006 mm y 4.998 mm. La regla de ejemplo admite 10 mm de diferencia. ¿Cumple?", ["La diferencia es 5.006 menos 4.998, es decir 8 mm.", "8 es menor que 10: cumple."], "Sí, cumple"),
        ("Cota fuera de tolerancia", "Un punto de ejemplo tiene cota +9 mm con tolerancia de 6 mm. ¿Cumple y por cuánto se pasa?", ["El límite superior es +6 mm.", "9 menos 6 son 3 mm: no cumple, se pasa 3 mm."], "No cumple; se pasa 3 mm"),
    ],
    mistakes=[("Dar por bueno un trazado solo porque una diagonal coincide con el valor ideal.", "Hay que comparar las dos diagonales entre sí.", "Mide y compara ambas diagonales y registra la diferencia."),
              ("Escribir solo «ok» en la planilla de verificación.", "No deja constancia de valores, regla ni responsable.", "Anota valores, regla, resultado, fecha y quién midió.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué se cumple en un rectángulo bien trazado respecto de sus diagonales?", "Las dos diagonales miden lo mismo", "Una diagonal mide la mitad del lado largo", "La diagonal mide lo mismo que el lado mayor", "En un rectángulo con ángulos rectos las dos diagonales son iguales."),
        ("abc", "En Montaje Industrial: ¿qué indica una cota negativa respecto del nivel de referencia?", "Que el punto queda por debajo del nivel de referencia", "Que el punto está mal medido", "Que el punto queda hacia la izquierda del eje", "Una cota negativa queda bajo el NR; no indica un error por sí sola."),
        ("abc", "En Montaje Industrial: ¿qué significa que un trazado esté a escuadra?", "Que los ejes forman ángulos rectos", "Que todos los puntos tienen la misma altura", "Que los ejes están a igual distancia del punto de referencia", "La escuadra se refiere a ángulos rectos entre los ejes."),
        ("=", "{F} ¿Cuántos milímetros difieren las dos diagonales?", "10004-9997", "Se resta la diagonal menor a la mayor.", " mm"),
        ("abc", "{F} ¿Cumple el trazado la regla de las diagonales?", "Sí, porque 7 mm es menor que 10 mm", "No, porque las diagonales no miden exactamente lo mismo", "No, porque 10.004 mm es mayor que 10.000 mm", "La regla admite hasta 10 mm de diferencia entre diagonales."),
        ("abc", "{F} ¿Qué puntos están dentro de la tolerancia de cota?", "P1 y P2", "P2 y P3", "Solo P3", "P1 y P2 están a 0 y 4 mm del NR; P3 está a 7 mm y supera 5 mm."),
        ("=", "{F} ¿Cuántos milímetros se pasa P3 por sobre la tolerancia de cota?", "7-5", "Se resta la tolerancia a la diferencia de P3.", " mm"),
        ("abc", "Un rectángulo de ejemplo mide 9 m por 12 m. ¿Cuánto debe medir su diagonal ideal?", "15 m", "21 m", "5 m", "Los lados 9 y 12 son 3 veces 3 y 4, así que la diagonal es 3 veces 5."),
        ("=", "{F} ¿Cuántos metros cuadrados tiene el rectángulo de ejes?", "6*8", "Se pasan los lados a metros y se multiplican: 6 m por 8 m.", " m²"),
        ("abc", "{F} Un compañero dice: «las diagonales difieren 7 mm, entonces el trazado es perfecto». ¿Qué respuesta es correcta?", "Cumple la regla de ejemplo, pero cumplir no es ser perfecto: se registra con su diferencia", "Es cierto, 7 mm no importa", "Es falso, porque la diferencia debería ser 0 siempre", "Cumplir significa estar dentro de la tolerancia, que se registra tal cual."),
        ("abc", "Con una regla de ejemplo que admite 10 mm de diferencia entre diagonales, dos diagonales de un trazado difieren 25 mm. ¿Qué corresponde?", "Registrar una no conformidad e informar al ITO o la jefatura antes de seguir", "Mover una esquina a ojo hasta que las diagonales calcen", "Promediar las diagonales y seguir", "Una diferencia mayor que la tolerancia se registra e informa, no se corrige a ojo."),
        ("abc", "Una planilla de ejemplo registra 5 cotas con tolerancia de 5 mm: +3, −5, +6, 0 y −4. ¿Cuántas cotas cumplen?", "4 cotas", "3 cotas", "5 cotas", "Solo +6 supera la tolerancia; −5 queda justo en el límite y cumple."),
        ("abc", "{F} ¿Qué debe quedar escrito en el registro de esta verificación?", "Los valores medidos, la regla usada, el resultado, la fecha y quién midió", "Solo la palabra «ok»", "Solo la firma del jefe", "Un registro útil permite que otra persona entienda y repita la revisión."),
    ],
    ctx=("abc", "El jefe de terreno de ejemplo te pide: «ajusta las cifras de la planilla para que P3 cumpla, así no hay que corregir nada». ¿Qué respondes?", "Que no se alteran los registros: P3 se anota como no conformidad y se informa al ITO", "Que sí, pero solo por 2 mm", "Que sí, si él firma el cambio", "Alterar los registros oculta el problema y anula su valor como control."),
    sc=[
        ("En Montaje Industrial: ¿qué diagonal ideal tiene un rectángulo de 3 m por 4 m?", "5 m", "Con la regla 3-4-5 la diagonal de lados 3 y 4 mide 5."),
        ("¿Cuándo cumple una cota?", "Cuando su diferencia con el valor del plano es igual o menor que la tolerancia", "Un valor justo en el límite de la tolerancia sí cumple."),
        ("¿Qué debe decir una planilla de verificación?", "Valores, regla, resultado, fecha y responsable", "Un «ok» solo no es evidencia."),
    ],
    op=("Ficha de ejemplo: rectángulo de ejes de 3.000 mm por 4.000 mm. Diagonal 1: 5.003 mm. Diagonal 2: 4.994 mm. Regla de ejemplo: cumple si las diagonales difieren 8 mm o menos. Cotas respecto del nivel de referencia, con tolerancia de 4 mm: Q1 = +2 mm; Q2 = −4 mm; Q3 = +6 mm. Escribe (a) la diferencia entre diagonales y si cumple, (b) qué cotas cumplen, (c) qué harías con la que no cumple.",
        "(a) 5.003 − 4.994 = 9 mm; no cumple, porque 9 supera 8. (b) Q1 cumple (2 ≤ 4) y Q2 cumple (4 ≤ 4); Q3 no cumple (6 > 4). (c) Registrar las no conformidades e informar al ITO o la jefatura, sin corregir a ojo.",
        ["calcula la diferencia entre diagonales", "clasifica las tres cotas", "indica qué hacer con las no conformidades"],
        ["hoja con los cálculos y la decisión"],
        ["decir que 9 mm cumple porque está cerca de 8", "considerar que −4 no cumple por ser negativa", "proponer corregir a ojo"],
        "Pregunta: «¿la cota negativa significa que está mal?». Si no responde, pídele que relea el párrafo de cotas."),
    reinforce="Escribe una planilla de verificación de ejemplo con dos diagonales y tres cotas, y marca cuáles cumplen.",
    extend="Explica con un ejemplo por qué comparar las dos diagonales entre sí es mejor que comparar solo una con el valor ideal.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 5 (alternativas de ejemplo, inventadas). Hay que elegir entre dos zonas para el acopio y las maniobras. Zona N: traslado de 20 m hasta el montaje; la ruta de las cargas cruza una vía de peatones en un punto. "
     "Zona S: traslado de 60 m; la ruta de las cargas no cruza vías de peatones. Matriz de ejemplo, con puntajes de 1 a 5 y pesos: seguridad (peso 5), tiempo (peso 3), costo (peso 2). "
     "Puntajes de la Zona N: seguridad 3, tiempo 5, costo 5. Puntajes de la Zona S: seguridad 5, tiempo 2, costo 3. Regla de descarte: se elimina toda zona cuya ruta de cargas cruce una vía de peatones, aunque tenga mejor puntaje.")
build(
    O3, 5, F,
    use="Aprenderé a comparar alternativas con una matriz de decisión, a aplicar una regla de descarte de seguridad y a dejar un registro de la decisión.",
    prior=["Sé multiplicar y sumar números enteros.", "Sé qué es una zona de exclusión.", "Sé qué es un registro."],
    explain=[
        "Una matriz de decisión compara alternativas según criterios. Cada criterio recibe un puntaje y un peso, que indica cuánto influye en el total. El total de cada alternativa es la suma de los puntajes multiplicados por sus pesos. Los pesos se acuerdan y se registran antes de comparar, y no se cambian después para favorecer una opción.",
        "Una regla de descarte es una condición que elimina una alternativa aunque tenga mejor puntaje. En seguridad, las reglas de descarte se aplican primero: una alternativa que mezcla cargas suspendidas con peatones no se elige, por muchos puntos que sume en tiempo o costo. Verificar la calidad de la decisión es dejarla registrada: alternativas, criterios, pesos, puntajes, reglas de descarte, resultado, quién decidió y la fecha.",
        f"Estas matrices son de papel y sus números son de ejemplo. La decisión real la toman las personas responsables con el plan y la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("matriz de decisión", "tabla que compara alternativas con criterios, puntajes y pesos"), ("peso", "cuánto influye un criterio en el total"), ("puntaje", "nota que recibe una alternativa en un criterio"), ("regla de descarte", "condición que elimina una alternativa aunque tenga buen puntaje"), ("registro de la decisión", "documento con alternativas, criterios, pesos, resultado, responsable y fecha")],
    worked=[
        ("Calcular un total", "Una matriz de ejemplo tiene dos criterios con pesos 3 y 2. La opción Y tiene puntajes 3 y 5. ¿Cuál es su total?", ["3 por 3 son 9, y 5 por 2 son 10.", "9 más 10 son 19."], "19 puntos"),
        ("Aplicar un descarte", "La opción X suma 30 puntos pero incumple una regla de descarte de seguridad; la opción Z suma 25 y la cumple. ¿Cuál se elige?", ["Las reglas de descarte se aplican primero.", "X queda eliminada aunque tenga más puntos."], "Z"),
    ],
    mistakes=[("Elegir la alternativa con más puntos sin mirar las reglas de descarte.", "Una alternativa insegura queda eliminada aunque sume mucho.", "Aplica primero las reglas de descarte de seguridad."),
              ("Cambiar los pesos después de ver los totales para que gane una opción.", "Se desvirtúa la comparación.", "Acuerda y registra los pesos antes de comparar.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es una matriz de decisión?", "Una tabla que compara alternativas con criterios, puntajes y pesos", "Un plano de ejes y cotas", "Un permiso de trabajo", "La matriz ordena la comparación de opciones; el plano y el permiso son otros documentos."),
        ("abc", "En Montaje Industrial: ¿qué significa que un criterio tenga mayor peso?", "Que influye más en el total", "Que cuesta más dinero", "Que se mide en kilogramos", "El peso de un criterio es su importancia relativa en el total."),
        ("abc", "En Montaje Industrial: ¿qué es una regla de descarte?", "Una condición que elimina una alternativa aunque tenga buen puntaje", "El criterio que recibe el puntaje más bajo", "El peso que se da a la seguridad", "El descarte elimina opciones que no cumplen un mínimo, sin importar el puntaje."),
        ("=", "{F} ¿Cuántos puntos pondera la seguridad de la Zona S (puntaje por peso)?", "5*5", "Se multiplica el puntaje de seguridad por su peso.", " puntos"),
        ("=", "{F} ¿Cuál es el total de la Zona N?", "3*5+5*3+5*2", "Se suman los puntajes multiplicados por sus pesos.", " puntos"),
        ("=", "{F} ¿Cuál es el total de la Zona S?", "5*5+2*3+3*2", "Se suman los puntajes multiplicados por sus pesos.", " puntos"),
        ("abc", "{F} Solo por el total de puntos, ¿qué zona gana?", "La Zona N, con 40 frente a 37", "La Zona S, con 37 frente a 25", "Empatan", "El total de N supera al de S."),
        ("abc", "{F} Aplicando la regla de descarte, ¿qué zona queda elegida?", "La Zona S, porque la ruta de cargas de N cruza una vía de peatones", "La Zona N, porque tiene más puntos", "Ninguna, hay que repetir todo", "El descarte de seguridad elimina a N aunque tenga mejor puntaje."),
        ("=", "{F} ¿Cuántos metros más de traslado tiene la Zona S que la Zona N?", "60-20", "Se resta el traslado de N al de S.", " m"),
        ("abc", "{F} Un compañero dice: «cambiemos los pesos para que gane la Zona N». ¿Qué respuesta es correcta?", "No: los pesos se acuerdan y registran antes de comparar; cambiarlos después desvirtúa la decisión", "Sí, porque los pesos se pueden ajustar al resultado deseado", "Sí, si se avisa en voz alta", "Ajustar pesos para favorecer una opción hace perder el sentido de comparar."),
        ("abc", "{F} ¿Qué tendría que cambiar para que la Zona N deje de estar descartada?", "Que un nuevo diseño de tránsito, aprobado por la persona responsable, elimine el cruce entre cargas y peatones", "Que se pinte la vía de peatones de otro color", "Que se cambie el nombre de la zona", "El descarte solo se levanta cuando desaparece la causa de seguridad."),
        ("=", "{F} Si el criterio tiempo pasara a tener peso 5 en lugar de 3, ¿cuántos puntos sumaría la Zona S?", "5*5+2*5+3*2", "Se recalculan los puntajes con el nuevo peso del tiempo.", " puntos"),
        ("abc", "{F} ¿Qué debe quedar en el registro de esta decisión?", "Las alternativas, los criterios, los pesos, los puntajes, la regla de descarte, quién decidió y la fecha", "Solo la zona elegida", "Solo el total de puntos de cada zona", "Un registro completo permite revisar y repetir la decisión."),
    ],
    ctx=("abc", "La jefa de ejemplo te dice: «elige la Zona N, los peatones saben cuidarse y ahorramos tiempo». ¿Qué respondes?", "Que la regla de descarte elimina la Zona N porque sus cargas cruzan una vía de peatones, y que se registra la decisión", "Que sí, porque el tiempo es lo más importante", "Que sí, si los peatones usan casco", "La seguridad es un descarte, no un criterio que se compense con ahorro de tiempo."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula el total de una alternativa en una matriz?", "Sumando los puntajes multiplicados por sus pesos", "Cada criterio influye según su peso."),
        ("¿Qué se aplica primero, el puntaje total o la regla de descarte de seguridad?", "La regla de descarte", "Una opción insegura queda eliminada antes de comparar totales."),
        ("¿Qué debe quedar escrito de una decisión?", "Alternativas, criterios, pesos, resultado, responsable y fecha", "Con ese registro otra persona puede revisar la decisión después."),
    ],
    op=("Ficha de ejemplo: dos rutas para trasladar piezas. Ruta R: seguridad 4, tiempo 5, costo 4. Ruta T: seguridad 5, tiempo 3, costo 3. Pesos: seguridad 5, tiempo 2, costo 1. Regla de descarte: se elimina toda ruta con cruce de peatones; R tiene un cruce y T no. Escribe (a) el total de cada ruta, (b) cuál gana solo por puntos, (c) cuál se elige aplicando la regla y por qué, (d) qué debe quedar en el registro.",
        "(a) R: 4×5 + 5×2 + 4×1 = 20 + 10 + 4 = 34. T: 5×5 + 3×2 + 3×1 = 25 + 6 + 3 = 34. (b) Empatan en puntos, así que los puntos no deciden. (c) Se elige T, porque R se elimina por el cruce de peatones. (d) Alternativas, criterios, pesos, puntajes, regla de descarte, resultado, quién decidió y fecha.",
        ["calcula los dos totales", "reconoce el empate", "aplica la regla de descarte", "lista el contenido del registro"],
        ["hoja con los cálculos y la decisión"],
        ["multiplicar mal los pesos", "elegir R por el tiempo", "no registrar la decisión"],
        "Pregunta: «¿qué pasa con una ruta que cruza peatones aunque sea la más rápida?». Si no responde, pídele que relea la regla de descarte."),
    reinforce="Inventa una matriz con dos alternativas y tres criterios, y calcula el total de cada una.",
    extend="Explica con un ejemplo por qué las reglas de descarte de seguridad se aplican antes de comparar los puntajes.",
)

# FIN
