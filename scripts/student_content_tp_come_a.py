"""Construcciones Metálicas TP 3.º y 4.º medio: OAE-01 (planos e instrumentos), OAE-02 (trazado en papel) y OAE-03 (corte, soldadura y uniones: solo conceptos). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_come_common import AVISO, EMER, build

O1 = "TP-COME-3y4-OAE-01"
O2 = "TP-COME-3y4-OAE-02"
O3 = "TP-COME-3y4-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El taller ficticio «Estructuras Demo» fabrica galpones livianos y escaleras de acero. Su matriz de peligros anota: ruido, chispas y humos, bordes filosos de los perfiles, "
     "perfiles apilados que pueden caer, cargas suspendidas y vapores de pintura. Personal del taller: 9 en preparación de piezas, 12 en armado y 6 en pintura. "
     "Regla de la matriz de ejemplo: puntaje de riesgo = probabilidad (de 1 a 5) × gravedad (de 1 a 5). Caída de perfiles apilados: probabilidad 3 y gravedad 5. Ruido: probabilidad 4 y gravedad 2.")
build(
    O1, 1, F,
    use="Aprenderé qué son las construcciones metálicas, qué peligros tiene un taller de este sector y cómo se ordenan las medidas de prevención antes de leer planos.",
    prior=["Sé leer una tabla sencilla.", "Sé multiplicar y dividir números enteros.", "Sé que un taller se rige por reglas escritas."],
    explain=[
        "Una construcción metálica es una estructura u objeto armado con perfiles, planchas y barras de acero, como un galpón liviano, una escalera o un estanque. Pertenece al sector metalmecánico y se fabrica en un taller o se arma en la obra, siempre según planos y especificaciones técnicas, que son los documentos donde el proyecto fija materiales y calidades. Un taller anota sus peligros en una matriz de peligros, una tabla que los lista junto a sus medidas de control.",
        "Un peligro es una fuente que puede causar daño y el riesgo es la posibilidad de que ese daño ocurra. En la matriz de ejemplo el puntaje de riesgo se calcula como probabilidad por gravedad. Las medidas se ordenan en la jerarquía de controles, de la más a la menos efectiva: eliminar el peligro, sustituirlo por otro menor, aplicar controles de ingeniería (barreras físicas que cambian el lugar o la máquina), controles administrativos (reglas, señales, permisos y capacitación) y, al final, el equipo de protección personal (EPP), que protege solo a quien lo usa.",
        f"Las tareas de riesgo, como cortar o soldar, las hacen personas formadas y autorizadas bajo un permiso de trabajo, y la Dirección del Trabajo fiscaliza que se cumpla la normativa laboral. {EMER} {AVISO}",
    ],
    vocab=[("construcción metálica", "estructura u objeto armado con perfiles, planchas y barras de acero"), ("matriz de peligros", "tabla que lista los peligros del taller con sus medidas de control"), ("peligro", "fuente con capacidad de causar daño"), ("riesgo", "posibilidad de que un peligro cause daño"), ("jerarquía de controles", "orden de las medidas de prevención, de la más a la menos efectiva"), ("EPP", "equipo de protección personal, la última barrera"), ("permiso de trabajo", "documento que autoriza una tarea de riesgo antes de comenzar")],
    worked=[
        ("Peligro y riesgo", "Una escalera de ejemplo recién fabricada tiene un borde filoso en un peldaño. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el borde filoso, porque puede causar daño.", "El riesgo es que alguien se corte al tocarlo o rozarlo."], "Peligro: el borde filoso; riesgo: que alguien se corte"),
        ("Puntaje de riesgo", "En otra matriz de ejemplo, un resbalón en un piso mojado tiene probabilidad 5 y gravedad 2. ¿Qué puntaje de riesgo resulta?", ["Se multiplica la probabilidad por la gravedad.", "5 por 2 son 10."], "10 puntos"),
    ],
    mistakes=[("Creer que usar casco y guantes basta para quedar protegido en cualquier tarea.", "El EPP es la última barrera: no quita el peligro y protege solo a quien lo usa.", "Primero se elimina o se controla el peligro; el EPP se suma a esos controles."),
              ("Creer que leer los planos o la matriz habilita para cortar o soldar.", "Las tareas de riesgo exigen formación, autorización, norma vigente y permiso.", "Aprende aquí el concepto y deja la tarea a personal autorizado.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es una construcción metálica?", "Una estructura u objeto armado con perfiles, planchas y barras de acero, como un galpón o una escalera", "Una obra de hormigón que lleva fierros en su interior", "Una máquina que corta y dobla planchas de acero", "Las construcciones metálicas son estructuras de acero; el hormigón armado y las máquinas son otra cosa."),
        ("abc", "En Construcciones Metálicas: ¿qué es un riesgo?", "La posibilidad de que un peligro cause daño a una persona o a un bien", "Una fuente que puede causar daño, como un borde filoso", "El equipo que usa una persona para protegerse", "El riesgo es la posibilidad de daño; la fuente de daño es el peligro."),
        ("abc", "En Construcciones Metálicas: ¿cuál es el orden de la jerarquía de controles, del más al menos efectivo?", "Eliminar, sustituir, controles de ingeniería, controles administrativos y EPP", "Sustituir, eliminar, controles administrativos, controles de ingeniería y EPP", "EPP, controles administrativos, controles de ingeniería, sustituir y eliminar", "Se prefiere quitar el peligro de raíz y dejar el EPP como última barrera."),
        ("=", "{F} ¿Cuántas personas trabajan en total en el taller de la ficha?", "9+12+6", "Se suman las personas de preparación, armado y pintura.", " personas"),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «perfiles apilados que pueden caer»?", "Que los perfiles caigan sobre una persona y la lesionen", "Que haya perfiles apilados en el taller", "Que el taller necesite más estantes", "El riesgo es el daño posible; tener perfiles apilados es solo la situación que lo origina."),
        ("abc", "{F} Se instala una pantalla, una barrera física, que retiene las chispas para que no lleguen a una zona de paso. ¿Qué tipo de control es?", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque ordena una conducta", "EPP, porque protege a las personas", "Una barrera física cambia el lugar y no depende de que cada persona obedezca."),
        ("abc", "{F} El taller pone un cartel que obliga a usar protección auditiva en la zona de ruido. ¿Qué es el cartel y qué es el protector auditivo?", "El cartel es un control administrativo y el protector auditivo es un EPP", "Ambos son controles de ingeniería", "El cartel es un EPP y el protector es un control administrativo", "El cartel informa y ordena; el protector lo usa la persona y es la última barrera."),
        ("=", "{F} Se capacita a todo el personal de la ficha en grupos de 9 personas. ¿Cuántos grupos se forman?", "(9+12+6)//9", "Se divide el personal total entre las personas de cada grupo.", " grupos"),
        ("abc", "{F} Un joven en práctica dice: «leí la matriz del taller, así que ya puedo cortar y soldar en el galpón». ¿Qué es correcto?", "Leer la matriz no lo habilita: esas tareas exigen formación, personal autorizado, norma vigente y permiso", "Puede hacerlo si usa careta y guantes", "Puede hacerlo si otro compañero lo observa de lejos", "Leer un documento no basta, y ni el EPP ni la compañía reemplazan la autorización."),
        ("abc", "Durante una visita de ejemplo a un taller, una pila de perfiles cae y una persona queda atrapada. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Levantar tú solo los perfiles para liberarla", "Esperar a que termine la jornada para informar", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "{F} ¿Por qué conviene eliminar o sustituir un peligro antes de entregar EPP?", "Porque eliminar o sustituir quita o reduce el peligro para todos, y el EPP protege solo a quien lo usa", "Porque un EPP bien usado elimina el peligro para todo el taller", "Porque los controles de ingeniería siempre se instalan solos", "Los niveles más altos de la jerarquía actúan sobre el peligro mismo, no solo sobre una persona."),
        ("=", "{F} Con la regla de la matriz, ¿qué puntaje de riesgo tiene la caída de perfiles apilados?", "3*5", "Se multiplica la probabilidad por la gravedad anotadas en la ficha.", " puntos"),
        ("abc", "{F} Con la misma regla, ¿cuál de los dos peligros anotados, la caída de perfiles apilados o el ruido, debe atenderse primero?", "La caída de perfiles, porque su puntaje 15 supera al 8 del ruido", "El ruido, porque ocurre con más frecuencia (probabilidad 4)", "Da lo mismo el orden, porque ambos están en la matriz", "Se prioriza el mayor puntaje, que combina probabilidad y gravedad, no solo la frecuencia."),
    ],
    ctx=("abc", "El dueño de un taller de ejemplo te dice: «Ponte el casco y ayúdanos a soldar esta estructura, tú ya sabes leer planos». ¿Qué respondes?", "Que no, porque soldar exige instructor autorizado, norma vigente y permiso, y que consultarás a un adulto responsable", "Que sí, porque con casco basta", "Que sí, pero solo si la pieza es pequeña", "Leer planos no habilita para una tarea de riesgo, y el casco no reemplaza la autorización."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es un peligro?", "Una fuente que puede causar daño, como un borde filoso", "El peligro es la fuente; el riesgo es la posibilidad de daño."),
        ("En Construcciones Metálicas: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
        ("En Construcciones Metálicas: ¿qué tipo de control es un cartel de advertencia?", "Un control administrativo", "El cartel informa y ordena una conducta sin cambiar el lugar."),
    ],
    op=("El taller ficticio «Estructuras Demo» anota una situación de ejemplo: el cable de un alargador cruza tendido por un pasillo de paso del taller. Escribe (a) cuál es el peligro y cuál el riesgo asociado, (b) un control administrativo para el pasillo, (c) un control de ingeniería para el mismo pasillo, (d) por qué el EPP no basta.",
        "(a) Peligro: el cable tendido en el piso; riesgo: que alguien tropiece y caiga. (b) Un cartel y una orden de no dejar cables cruzando el pasillo. (c) Una canaleta o cubierta fija que deje el cable fuera del paso, o mover el enchufe para que el cable no cruce. (d) Porque el EPP es la última barrera: no quita el peligro y protege solo a quien lo usa. La tarea la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer el EPP como único control", "no aclarar que la tarea la hace personal autorizado"],
        "Pregunta: «¿qué control quitaría el peligro de raíz?». Si no responde, pídele que relea el primer nivel de la jerarquía."),
    reinforce="Escribe la jerarquía de controles en orden y pon junto a cada nivel un ejemplo inventado de un taller de construcciones metálicas.",
    extend="Explica con un ejemplo por qué un permiso de trabajo es un control administrativo y no reemplaza a una barrera física.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (lámina descrita por escrito, de ejemplo, inventada). Lámina E-02 «Pórtico de un galpón», escala 1:20, revisión D, dibujada para el taller «Estructuras Demo». "
     "Leyenda: P = pilar; V = viga; C = costanera; B = placa base. Lista de piezas: P1 (2 unidades), V1 (2 unidades), C1 (5 unidades), B1 (2 unidades). "
     "P1 se designa «perfil H de ejemplo 150×100×6» (alto × ancho × espesor, en mm). En la carpeta circula también una copia de la lámina E-02 con revisión C. "
     "Con regla se midió 7 cm entre dos ejes en la lámina; la cota escrita entre esos ejes dice 150 cm.")
build(
    O1, 2, F,
    use="Aprenderé los tipos de planos de una construcción metálica, a leer rótulo, leyenda, lista de piezas y designación de perfiles, a pasar medidas de la lámina a la realidad y qué función cumple cada rol.",
    prior=["Sé qué es una construcción metálica.", "Sé multiplicar por 10, 20 o 50.", "Sé que 100 cm son 1 m."],
    explain=[
        "Un proyecto usa varios tipos de planos. La planta es la vista de la obra desde arriba; la elevación la muestra de frente o de un costado; el corte muestra una rebanada vertical; el detalle amplía una unión o una pieza. El plano de taller describe cada pieza para fabricarla y el plano de montaje muestra dónde va cada una en la obra. El rótulo es el recuadro con nombre del proyecto, escala y revisión, y la leyenda explica las siglas. Cada pieza tiene una marca, como P1 o V3, y la lista de piezas ordena marcas y cantidades. Los perfiles se designan con su forma y sus medidas en milímetros: alto, ancho y espesor.",
        "La escala 1:20 significa que 1 cm de la lámina equivale a 20 cm reales. La cota escrita manda sobre la medida tomada con regla, y si no coinciden se registra la diferencia y se consulta. La letra de revisión indica la versión: se trabaja solo con la vigente, que confirma quien emite la lámina. Un error o una duda no se corrigen a mano ni se resuelven por intuición: se registran y se consultan al proyectista.",
        f"Cada rol tiene su función. El proyectista diseña y emite las revisiones. El inspector técnico de obra (ITO) revisa que lo construido cumpla los planos y las especificaciones. El jefe de taller organiza el trabajo. El prevencionista vela por la seguridad. El personal calificado y autorizado ejecuta solo las tareas que la norma le permite. {EMER} {AVISO}",
    ],
    vocab=[("planta", "vista de la obra desde arriba"), ("elevación", "vista de la obra de frente o de un costado"), ("detalle", "dibujo ampliado de una unión o una pieza"), ("rótulo", "recuadro con nombre del proyecto, escala y revisión"), ("marca", "nombre corto de una pieza, como P1 o V3"), ("designación", "nombre de un perfil con su forma y sus medidas en mm"), ("revisión", "versión de una lámina, indicada con una letra"), ("proyectista", "persona que diseña el proyecto y emite las revisiones"), ("ITO", "inspector técnico de obra, que revisa que lo construido cumpla los planos")],
    worked=[
        ("Pasar a la realidad", "Una lámina de ejemplo está a escala 1:10 y un tramo mide 12 cm en la lámina. ¿Cuántos centímetros reales mide?", ["La escala dice que 1 cm de lámina son 10 cm reales.", "12 por 10 son 120."], "120 cm"),
        ("Leer una designación", "Un perfil tubular de ejemplo se designa «80×40×3», con alto × ancho × espesor en mm. ¿Qué mide su ancho?", ["El orden es alto, ancho y espesor.", "La segunda medida es el ancho, 40."], "40 mm"),
    ],
    mistakes=[("Medir con regla y fabricar con esa medida aunque la cota escrita diga otra.", "La cota escrita manda; la regla sobre un papel puede tener error de impresión o de lectura.", "Usa la cota, registra la diferencia y consúltala al proyectista."),
              ("Trabajar con la primera copia de la lámina que se encuentra.", "Puede ser una revisión antigua que ya no cumple el proyecto.", "Revisa la letra de revisión y confirma cuál es la vigente.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué muestra un plano de elevación?", "La obra vista de frente o de un costado", "La obra vista desde arriba", "Una unión ampliada para ver su detalle", "Mirar desde arriba es la planta; ampliar una unión es el detalle."),
        ("abc", "En Construcciones Metálicas: ¿para qué sirve la lista de piezas de una lámina?", "Para listar la marca y la cantidad de cada pieza", "Para indicar el precio de cada pieza", "Para decir quién dibujó la lámina", "La lista ordena marcas y cantidades; precios y autores van en otros documentos."),
        ("abc", "En Construcciones Metálicas: ¿qué indica la letra de revisión de una lámina?", "La versión de la lámina; se trabaja con la vigente", "La cantidad de piezas que trae", "El nombre de quien la dibujó", "La revisión fecha la versión y evita fabricar con datos antiguos."),
        ("=", "{F} ¿Cuántas piezas suma en total la lista de piezas de la lámina?", "2+2+5+2", "Se suman las unidades de P1, V1, C1 y B1.", " piezas"),
        ("abc", "{F} ¿Qué significa la marca C1 según la leyenda?", "Una costanera", "Un pilar", "Una placa base", "La leyenda asigna la C a las costaneras; P es pilar y B es placa base."),
        ("abc", "{F} En la carpeta hay dos copias de la lámina E-02, con revisión C y con revisión D. ¿Con cuál se trabaja?", "Con la D, que es la vigente de la ficha, confirmándolo con el proyectista", "Con la C, porque se imprimió primero", "Con ambas, mezclando los datos que parezcan mejores", "Se trabaja solo con la revisión vigente, nunca con una mezcla."),
        ("=", "{F} La regla midió 7 cm entre dos ejes de la lámina. ¿Cuántos centímetros reales resultan según la escala?", "7*20", "Se multiplica la medida de la lámina por la escala.", " cm"),
        ("abc", "{F} ¿Qué dimensión es el espesor de P1 según su designación?", "6 mm", "150 mm", "100 mm", "El espesor es la tercera medida; 150 es el alto y 100 es el ancho."),
        ("abc", "{F} La cota escrita entre los dos ejes dice 150 cm y la regla da 140 cm reales. ¿Qué corresponde?", "Usar la cota escrita, registrar la diferencia y consultarla al proyectista", "Corregir la cota a mano para que coincida con la regla", "Usar la medida de la regla, porque es la real", "La cota escrita manda; no se altera un documento sin que lo emita el proyectista."),
        ("abc", "{F} Un jefe de taller de ejemplo ordena fabricar según la revisión C aunque existe la D. ¿Qué riesgo hay?", "Fabricar piezas con datos antiguos que ya no cumplen el proyecto, lo que obliga a rehacerlas", "Ninguno, porque la revisión solo cambia el color del dibujo", "Que la lámina se gaste por el uso", "Una revisión nueva corrige datos del proyecto; ignorarla genera piezas erróneas."),
        ("abc", "En Construcciones Metálicas: el ITO anota que una unión ejecutada no cumple lo exigido en las especificaciones. ¿Cuál es su función?", "Revisar que lo construido cumpla planos y especificaciones y dejarlo registrado", "Diseñar de nuevo la unión", "Reparar la unión él mismo en el momento", "El ITO verifica y registra; rediseñar es del proyectista y reparar es de personal autorizado."),
        ("=", "{F} Una pieza de ejemplo se dibuja con 25 cm en la lámina. ¿Cuántos metros reales mide?", "25*20//100", "Se multiplica por la escala y se pasan los centímetros a metros.", " m"),
        ("abc", "{F} Un practicante nota que falta una cota en la lámina. Un compañero propone deducirla midiendo con regla y fabricar. ¿Qué corresponde?", "Registrar la duda y consultarla al proyectista, sin inventar la cota", "Deducir la cota con la regla y fabricar", "Usar la cota de una obra parecida", "Las dudas no se resuelven por intuición; se consultan a quien emite el plano."),
    ],
    ctx=("abc", "Una compañera de práctica ve que la lista de piezas de una lámina de ejemplo dice 4 vigas V1, pero el dibujo solo muestra 3. ¿Qué haces?", "Anotar la discrepancia y consultarla al responsable del proyecto antes de fabricar", "Fabricar 4 por si acaso", "Fabricar 3 porque el dibujo siempre manda", "Una discrepancia entre documentos se registra y se consulta; no se resuelve por suposición."),
    sc=[
        ("En Construcciones Metálicas: ¿qué hace el proyectista?", "Diseña el proyecto y emite las revisiones de las láminas", "Diseñar y emitir revisiones es función del proyectista."),
        ("¿Qué significa una escala 1:20?", "1 cm de la lámina equivale a 20 cm reales", "La escala relaciona la medida dibujada con la real."),
        ("¿Qué manda si la cota escrita y la regla no coinciden?", "La cota escrita; se registra la diferencia", "La cota es el dato oficial y la regla solo una comprobación."),
    ],
    op=("Lámina de ejemplo F-07 «Escalera de acceso», escala 1:50, revisión B. Leyenda: Z = zanca; E = escalón. Lista de piezas: Z1 (2 unidades), E1 (9 unidades). Con regla se midieron 8 cm entre dos ejes. Escribe (a) cuántas piezas suma la lista, (b) cuántos metros reales son 8 cm a esa escala, (c) qué haces si falta la cota de un escalón, (d) qué función tiene el ITO.",
        "(a) 2 + 9 = 11 piezas. (b) 8 × 50 = 400 cm, es decir, 4 m. (c) Registro la duda y la consulto al proyectista, sin inventar la cota. (d) El ITO revisa que lo construido cumpla los planos y las especificaciones y lo deja registrado.",
        ["suma las piezas de la lista", "usa bien la escala", "consulta la cota faltante", "explica la función del ITO"],
        ["hoja con las cuatro respuestas"],
        ["olvidar pasar los centímetros a metros", "inventar la cota que falta", "confundir al ITO con el proyectista"],
        "Pregunta: «¿de quién es decidir una cota que falta?». Si no responde, pídele que relea los roles."),
    reinforce="Dibuja una tabla con las columnas marca, nombre y cantidad e inventa cuatro filas para una escalera.",
    extend="Explica con un ejemplo qué ocurre en una obra si dos personas trabajan con revisiones distintas de la misma lámina.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (datos de ejemplo, inventados). Taller «Estructuras Demo». Instrumentos: huincha metálica (análoga, graduada en milímetros, resolución 1 mm), pie de metro análogo (con escala y cursor) y pie de metro digital (con pantalla). "
     "La etiqueta del pie de metro digital dice «calibrado; certificado vigente». Un perfil tiene largo de plano 1.200 mm con tolerancia ± 3 mm. Lecturas de ejemplo con la huincha: lectura A = 1.201 mm; lectura B = 1.206 mm. "
     "Cinco perfiles iguales medidos en otro control: 1.199, 1.204, 1.200, 1.197 y 1.205 mm.")
build(
    O1, 3, F,
    use="Aprenderé a distinguir instrumentos análogos y digitales, qué es la resolución, la calibración y el error de paralaje, y a decidir si una lectura se acepta según la tolerancia.",
    prior=["Sé leer una escala graduada.", "Sé sumar y restar números enteros.", "Sé que una medida se escribe con su unidad."],
    explain=[
        "Un instrumento análogo se lee sobre una escala graduada, como la huincha, que es una cinta metálica con marcas cada milímetro. Un instrumento digital muestra el valor en una pantalla numérica. El pie de metro es un instrumento para medir largos exteriores, interiores y profundidades de piezas pequeñas, y existe en versión análoga y digital. La resolución es lo más pequeño que el instrumento permite distinguir. El error de paralaje ocurre cuando se mira la escala desde un costado y la lectura aparente cambia; por eso se lee de frente.",
        "Un instrumento se calibra comparándolo con un patrón conocido, y su certificado dice hasta cuándo es válido. Si el certificado está vencido o el instrumento se golpeó, su lectura queda en duda hasta que se calibre. La tolerancia es la variación permitida respecto de la medida del plano: con 1.200 mm ± 3 mm, el largo mínimo es 1.197 y el máximo 1.203, y los dos límites se aceptan. Una lectura dentro del rango se acepta y una fuera se rechaza y se registra.",
        f"Una lectura rechazada no se repite hasta que salga buena ni se borra: se registra con su valor real y se informa al responsable. Solo personal formado usa los instrumentos en un control formal. {EMER} {AVISO}",
    ],
    vocab=[("instrumento análogo", "se lee sobre una escala graduada"), ("instrumento digital", "muestra el valor en una pantalla numérica"), ("resolución", "lo más pequeño que el instrumento permite distinguir"), ("paralaje", "error de lectura por mirar la escala desde un costado"), ("calibración", "comparación de un instrumento con un patrón conocido"), ("tolerancia", "variación permitida respecto de la medida del plano"), ("huincha", "cinta metálica graduada para medir largos")],
    worked=[
        ("Revisar una tolerancia", "Un perfil de ejemplo tiene largo de plano 500 mm con tolerancia ± 2 mm. Se lee 503 mm. ¿Se acepta?", ["Los límites son 498 y 502 mm.", "503 supera el máximo de 502."], "Se rechaza y se registra"),
        ("Instrumento con certificado vencido", "Un instrumento de ejemplo tiene el certificado vencido hace un mes, aunque su pantalla muestra números claros. ¿Sirve para un control formal?", ["La pantalla clara no prueba que la lectura sea correcta.", "Un instrumento sin calibración vigente deja la medida en duda."], "No, hasta que se calibre"),
    ],
    mistakes=[("Creer que un instrumento digital es siempre más exacto que uno análogo.", "La exactitud depende de la calibración y del buen uso, no de la pantalla.", "Revisa el certificado y la resolución antes de confiar en la lectura."),
              ("Repetir la medición hasta que salga dentro del rango y anotar solo esa.", "Se oculta un hallazgo real y se altera el registro.", "Registra la lectura rechazada y su valor real, e informa al responsable.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué diferencia hay entre un instrumento análogo y uno digital?", "El análogo se lee sobre una escala graduada y el digital muestra el valor en una pantalla", "El análogo mide solo largos y el digital solo pesos", "El análogo es siempre más exacto que el digital", "La diferencia está en cómo se presenta la lectura, no en la exactitud ni en la magnitud."),
        ("abc", "En Construcciones Metálicas: ¿qué es la resolución de un instrumento?", "Lo más pequeño que el instrumento permite distinguir", "El valor máximo que puede medir", "El tiempo que tarda en dar la medida", "La resolución es el paso más pequeño de la lectura; el máximo es el alcance."),
        ("abc", "En Construcciones Metálicas: ¿qué es calibrar un instrumento?", "Compararlo con un patrón conocido y verificar o ajustar su lectura", "Limpiarlo y guardarlo", "Cambiar la unidad en que muestra la medida", "Calibrar es contrastar con un patrón; limpiar o cambiar unidad no verifica la lectura."),
        ("=", "{F} ¿Cuál es el largo máximo aceptable del perfil, en milímetros?", "1200+3", "Se suma la tolerancia al largo del plano.", " mm"),
        ("=", "{F} ¿Cuál es el largo mínimo aceptable del perfil, en milímetros?", "1200-3", "Se resta la tolerancia al largo del plano.", " mm"),
        ("abc", "{F} ¿Se acepta la lectura A, de 1.201 mm?", "Se acepta, porque está entre 1.197 y 1.203 mm", "Se rechaza, porque no es exactamente 1.200 mm", "Se rechaza, porque supera el largo del plano", "La tolerancia permite variar dentro del rango; no se exige el valor exacto."),
        ("abc", "{F} ¿Se acepta la lectura B, de 1.206 mm?", "Se rechaza, porque supera el máximo de 1.203 mm", "Se acepta, porque la diferencia es de solo 6 mm", "Se acepta, porque la huincha tiene resolución de 1 mm", "La resolución fina no cambia el rango; 1.206 queda fuera de los límites."),
        ("abc", "{F} Una persona lee la huincha mirando la escala desde un costado y no de frente. ¿Qué error puede ocurrir?", "Un error de paralaje: la lectura aparente cambia por el ángulo de la mirada", "Un error de calibración del certificado", "Un error de resolución, porque la escala cambia", "Mirar de costado desplaza la lectura aparente; eso es paralaje."),
        ("=", "{F} ¿Cuántos milímetros supera la lectura B el largo máximo aceptable?", "1206-1203", "Se resta el largo máximo a la lectura B.", " mm"),
        ("abc", "Un pie de metro de ejemplo se golpeó al caer de la mesa al piso, y desde entonces sus lecturas no han sido comprobadas. ¿Qué corresponde para un control formal?", "No usarlo hasta que lo calibren, porque su lectura queda en duda", "Usarlo, porque un número en pantalla siempre es correcto", "Usarlo y restar 1 mm a cada lectura", "Tras un golpe no se sabe cuánto se equivoca; corregir a ojo tampoco lo soluciona."),
        ("abc", "En Construcciones Metálicas: ¿por qué se registra una lectura rechazada en lugar de repetir la medición hasta que dé bien?", "Porque el registro deja evidencia del hallazgo y permite decidir qué hacer con la pieza", "Porque una lectura rechazada se borra al final del día", "Porque medir dos veces está prohibido", "Ocultar una lectura mala quita información que el responsable necesita para decidir."),
        ("abc", "{F} ¿Cuántos de los cinco perfiles medidos en el otro control se aceptan con el rango 1.197 a 1.203 mm?", "3 perfiles", "4 perfiles", "2 perfiles", "Se aceptan 1.199, 1.200 y 1.197; 1.204 y 1.205 superan el máximo."),
        ("abc", "{F} Otro perfil se lee en 1.203 mm. ¿Cumple?", "Sí, está justo en el límite máximo y los límites se aceptan", "No, porque llegó al límite", "No se puede saber, porque la huincha es análoga", "Los dos límites del rango se aceptan; la huincha es un instrumento válido si está calibrada."),
    ],
    ctx=("abc", "En una recepción de ejemplo, el jefe te pide anotar «aceptado» en un perfil cuya lectura quedó 4 mm sobre el máximo, para no atrasar la entrega. ¿Qué haces?", "Registro el valor real y la no conformidad, y no altero el registro", "Anoto «aceptado» para no atrasar", "Borro la fila del perfil", "El registro debe reflejar lo medido; alterarlo oculta un hallazgo."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es el paralaje?", "Un error de lectura por mirar la escala desde un costado", "Mirar de costado cambia la lectura aparente de la escala."),
        ("En Construcciones Metálicas: ¿qué se hace con un instrumento de certificado vencido?", "No se usa para un control formal hasta calibrarlo", "Sin calibración vigente la medida queda en duda."),
        ("En Construcciones Metálicas: ¿qué es la tolerancia?", "La variación permitida respecto de la medida del plano", "Define el rango entre el mínimo y el máximo aceptables."),
    ],
    op=("Plano de ejemplo: una pletina (barra plana) de largo 800 mm y tolerancia ± 2 mm. Tres lecturas con huincha: 799, 803 y 801 mm. Escribe (a) los límites mínimo y máximo, (b) qué lecturas se aceptan y cuáles se rechazan, (c) cómo registrarías la rechazada, (d) por qué se lee la escala de frente.",
        "(a) Mínimo 798 mm y máximo 802 mm. (b) Se aceptan 799 y 801; se rechaza 803, que supera el máximo. (c) Anotando su valor real, 803 mm, como no conformidad e informando al responsable. (d) Para evitar el error de paralaje, que cambia la lectura aparente.",
        ["calcula los límites", "clasifica las tres lecturas", "describe el registro", "explica el paralaje"],
        ["hoja con las cuatro respuestas"],
        ["aceptar una lectura fuera del rango", "anotar un valor corregido a ojo", "no explicar el paralaje"],
        "Pregunta: «¿qué valor escribirías en la planilla para 803?». Si responde 802, pídele que relea cómo se registra."),
    reinforce="Escribe tres lecturas inventadas para una pieza de 600 mm ± 2 mm e indica cuáles se aceptan.",
    extend="Explica con un ejemplo por qué la resolución de un instrumento debe ser menor que la tolerancia que se quiere controlar.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados). Planilla de control de recepción del taller «Estructuras Demo»: 5 pilares de largo de plano 2.400 mm, tolerancia ± 4 mm (límites 2.396 a 2.404 mm). "
     "Lecturas en mm: P-01 = 2.399; P-02 = 2.405; P-03 = 2.402; P-04 = 2.396; P-05 = 2.391. "
     "Un marco rectangular de la lámina mide 900 mm por 1.200 mm y su diagonal teórica es 1.500 mm; se midieron las dos diagonales: 1.502 y 1.498 mm. Diferencia máxima admitida entre las dos diagonales: 3 mm (valor de ejemplo).")
build(
    O1, 4, F,
    use="Aprenderé a llenar y revisar una planilla de control: aceptar o rechazar según la tolerancia, calcular porcentajes, comprobar un marco por sus diagonales y registrar una no conformidad.",
    prior=["Sé qué es una tolerancia.", "Sé restar y calcular porcentajes sencillos.", "Sé que un registro debe decir la verdad."],
    explain=[
        "Una planilla de control lista cada pieza con su lectura, el rango aceptable y el resultado: se acepta si la lectura está entre el mínimo y el máximo, incluidos los límites, y se rechaza si queda fuera. El porcentaje de piezas aceptadas es las aceptadas multiplicadas por 100 y divididas entre las controladas. Un hallazgo que no cumple lo exigido se llama no conformidad: se registra con su valor real y se informa al responsable, que decide qué se hace con la pieza.",
        "Un marco rectangular se comprueba midiendo sus dos diagonales: si el marco está en escuadra, las dos diagonales miden lo mismo dentro de la tolerancia. Si su diferencia supera lo admitido, el marco está fuera de escuadra y se registra como no conformidad, aunque cada diagonal esté cerca del valor teórico. También se calcula la diferencia entre lectura y plano restando el valor menor al mayor.",
        f"Un registro nunca se altera para que cuadre ni se borra una fila incómoda: la honestidad del dato es parte del control de calidad. {EMER} {AVISO}",
    ],
    vocab=[("planilla de control", "tabla con la lectura, el rango y el resultado de cada pieza"), ("no conformidad", "hallazgo que no cumple lo exigido y se registra"), ("diagonal", "línea que une dos esquinas opuestas de un marco"), ("fuera de escuadra", "marco cuyas diagonales difieren más de lo admitido"), ("límite", "valor mínimo o máximo aceptable, que se acepta")],
    worked=[
        ("Control de un largo", "Un tubo de ejemplo tiene largo de plano 3.000 mm con tolerancia ± 5 mm y se lee 3.006 mm. ¿Se acepta?", ["Los límites son 2.995 y 3.005 mm.", "3.006 supera el máximo de 3.005."], "Se rechaza y se registra como no conformidad"),
        ("Diagonales de un marco", "Un marco de ejemplo de 600 × 800 mm tiene diagonal teórica de 1.000 mm. Se miden 1.001 y 999 mm y se admite una diferencia de 3 mm. ¿Está en escuadra?", ["La diferencia entre diagonales es 1.001 menos 999, es decir, 2 mm.", "2 mm no supera los 3 mm admitidos."], "Sí, está en escuadra"),
    ],
    mistakes=[("Rechazar una pieza porque no mide exactamente el valor del plano.", "La tolerancia permite variar dentro del rango.", "Compara la lectura con el mínimo y el máximo."),
              ("Dar el marco por bueno porque cada diagonal está cerca del valor teórico.", "Lo que se compara es la diferencia entre las dos diagonales.", "Resta una diagonal a la otra y compárala con lo admitido.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es una tolerancia?", "La variación permitida respecto de la medida del plano", "El error que comete quien mide y que debe borrarse", "La medida más pequeña que lee un instrumento", "La tolerancia define el rango aceptable; la resolución es lo más pequeño que se lee."),
        ("abc", "En Construcciones Metálicas: ¿qué se compara entre las diagonales de un marco rectangular?", "Que ambas midan lo mismo dentro de la tolerancia", "Que sumen la longitud de los lados", "Que sean menores que los lados", "Un marco en escuadra tiene las dos diagonales iguales dentro de lo admitido."),
        ("abc", "En Construcciones Metálicas: ¿qué es una no conformidad?", "Un hallazgo que no cumple lo exigido y que se registra e informa", "Una pieza que se fabricó más rápido", "Un permiso que se niega", "Una no conformidad es un incumplimiento registrado, no un asunto de velocidad ni de permisos."),
        ("=", "{F} ¿Cuántos milímetros se aleja la lectura de P-02 de su largo de plano?", "2405-2400", "Se resta el largo de plano a la lectura.", " mm"),
        ("abc", "{F} ¿Se acepta P-03?", "Se acepta, porque 2.402 está entre 2.396 y 2.404", "Se rechaza, porque no mide 2.400", "Se rechaza, porque supera 2.400", "La lectura está dentro del rango, aunque no sea igual al valor del plano."),
        ("abc", "{F} ¿Se acepta P-04, con 2.396 mm?", "Se acepta: el límite mínimo es 2.396 y la lectura lo alcanza", "Se rechaza: está por debajo del largo del plano", "Se rechaza: está en el borde y no dentro del rango", "Los límites del rango se aceptan; estar en el borde no es estar fuera."),
        ("abc", "{F} ¿Cuántos de los cinco pilares se aceptan?", "3 pilares", "4 pilares", "2 pilares", "Se aceptan P-01, P-03 y P-04; P-02 supera el máximo y P-05 queda bajo el mínimo."),
        ("=", "{F} ¿Qué porcentaje de los pilares controlados queda aceptado?", "3*100//5", "Se multiplican por 100 los aceptados y se divide entre los controlados.", " %"),
        ("=", "{F} ¿Cuántos milímetros difieren entre sí las dos diagonales medidas del marco?", "1502-1498", "Se resta la diagonal menor a la mayor.", " mm"),
        ("abc", "{F} ¿Qué se concluye del marco medido?", "Está fuera de escuadra y se registra como no conformidad", "Cumple, porque cada diagonal está a 2 mm de 1.500", "Cumple, porque el promedio de las diagonales es 1.500", "Se compara la diferencia entre diagonales, 4 mm, con los 3 mm admitidos."),
        ("abc", "{F} P-05 se rechaza con 2.391 mm. ¿Qué corresponde hacer con ese hallazgo?", "Registrarlo como no conformidad e informar al responsable para que decida", "Dejarlo en la pila sin avisar, porque es solo un pilar", "Anotar 2.400 mm en la planilla para que cuadre", "El hallazgo se informa con su valor real; no se oculta ni se altera."),
        ("=", "En un control de ejemplo se revisa una muestra de 20 piezas y 3 quedan fuera de tolerancia. ¿Qué porcentaje de la muestra está fuera?", "3*100//20", "Se multiplican por 100 las piezas fuera y se divide entre la muestra.", " %"),
        ("abc", "Una planilla de ejemplo tiene un valor rechazado, pero el jefe pide anotarlo como aceptado para no atrasar la obra. ¿Qué corresponde?", "Registrar el valor real y la no conformidad, sin alterar el registro", "Anotar «aceptado» para no atrasar", "Borrar la fila de la pieza", "Alterar o borrar un registro oculta el hallazgo y es una falta de honestidad."),
    ],
    ctx=("abc", "Una compañera de práctica revisa el marco de una puerta de ejemplo de 500 × 1.200 mm (diagonal teórica 1.300 mm) y mide diagonales de 1.304 y 1.296 mm, con diferencia admitida de 3 mm. Ella dice «cada diagonal está a solo 4 mm, así que cumple». ¿Qué respondes?", "Que se compara la diferencia entre diagonales, que es 8 mm y supera 3 mm: está fuera de escuadra", "Que cumple, porque ambas están cerca de 1.300", "Que cumple, porque su promedio es exactamente 1.300", "El criterio es la diferencia entre diagonales; el promedio puede ser perfecto y el marco estar torcido."),
    sc=[
        ("En Construcciones Metálicas: ¿qué diferencia entre diagonales indica un marco en escuadra?", "Una diferencia dentro de lo admitido", "Dos diagonales casi iguales indican un marco rectangular."),
        ("¿Cómo se calcula el porcentaje de piezas aceptadas?", "Aceptadas por 100, divididas entre controladas", "El porcentaje compara las aceptadas con el total controlado."),
        ("¿Qué se hace con un valor fuera de tolerancia?", "Se registra como no conformidad y se informa", "El registro honesto permite que el responsable decida."),
    ],
    op=("Planilla de ejemplo: 4 vigas de largo de plano 2.500 mm, tolerancia ± 3 mm. Lecturas: 2.502; 2.504; 2.498; 2.503. Escribe (a) los límites mínimo y máximo, (b) qué vigas se aceptan y cuáles se rechazan, (c) el porcentaje de vigas aceptadas, (d) cómo registrarías la rechazada.",
        "(a) Mínimo 2.497 mm y máximo 2.503 mm. (b) Se aceptan 2.502, 2.498 y 2.503; se rechaza 2.504. (c) 3 × 100 ÷ 4 = 75 %. (d) Con su valor real, 2.504 mm, como no conformidad, informando al responsable.",
        ["calcula los límites", "clasifica las cuatro lecturas", "calcula el porcentaje", "describe el registro de la rechazada"],
        ["hoja con las cuatro respuestas"],
        ["rechazar una lectura que está en el límite", "dividir entre 3 en vez de entre 4", "anotar un valor corregido"],
        "Pregunta: «¿2.503 se acepta o se rechaza?». Si dice rechaza, pídele que relea que los límites se aceptan."),
    reinforce="Inventa una planilla de 5 piezas de 1.000 mm ± 2 mm con una lectura rechazada y calcula el porcentaje de aceptadas.",
    extend="Explica con un ejemplo por qué es mejor registrar una no conformidad pequeña que ocultarla.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 5 (caso de ejemplo, inventado). En «Estructuras Demo», el área de preparación recibe planchas y perfiles de acero para marcar sobre ellos los límites de cada pieza antes de cortarla. "
     "Peligros anotados: planchas pesadas que se mueven entre dos personas, bordes filosos, ruido de la zona vecina de corte y piezas marcadas con error que se cortan igual. "
     "Dato de costos de ejemplo: una plancha mal trazada pierde $12.000 en material; en un mes se detectaron 5 planchas mal trazadas. El área prepara 4 planchas por turno y trabaja 3 turnos por semana.")
build(
    O2, 1, F,
    use="Aprenderé qué es trazar una pieza, por qué un error de trazado sale caro, qué peligros tiene el área de preparación y qué dice la norma vigente sobre mover cargas a mano.",
    prior=["Sé leer un plano y una orden sencilla.", "Sé multiplicar y restar números enteros.", "Sé qué es un peligro y un riesgo."],
    explain=[
        "Trazar es marcar sobre el material, según el plano, las líneas y puntos que indican dónde se corta, se dobla o se perfora. Quien traza lee el plano, la lista de piezas y la orden de trabajo, que es el documento que indica qué fabricar, en qué cantidad y con qué plano de referencia. Trazar solo marca: cortar, doblar y unir son etapas posteriores que hace personal autorizado. Aquí no se enseña cómo se marca, solo para qué sirve y qué documentos y riesgos intervienen.",
        "Un error de trazado se arrastra: si la marca está mal, la pieza se corta mal, se arma mal y puede quedar inservible, con pérdida de material y de horas de trabajo. Por eso el trazado se revisa antes de cortar. En el área hay riesgos propios: las planchas pesadas pueden causar sobreesfuerzo o golpes, y los bordes son filosos. Una medida de ingeniería es usar una ayuda mecánica para mover la carga, y la norma vigente sobre manejo manual de carga fija el límite de lo que una persona puede levantar.",
        f"Nadie mueve una carga que exceda lo permitido a fuerza de brazos: se pide una ayuda mecánica y personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("trazar", "marcar sobre el material, según el plano, dónde se corta, se dobla o se perfora"), ("orden de trabajo", "documento que indica qué fabricar, en qué cantidad y con qué plano"), ("sobreesfuerzo", "daño al cuerpo por mover una carga demasiado pesada"), ("ayuda mecánica", "equipo que mueve una carga en lugar de las personas"), ("manejo manual de carga", "mover o levantar una carga con el cuerpo, regulado por la norma vigente")],
    worked=[
        ("Error que se arrastra", "Un jefe de taller de ejemplo dice: «marcar mal una pieza no importa, porque se corrige al cortar». ¿Por qué es un error pensar así?", ["La marca define dónde se corta.", "Si la marca está mal, el corte, el armado y las etapas siguientes quedan con el error."], "El error de trazado se arrastra a todas las etapas siguientes"),
        ("Costo de un error", "En otra área de ejemplo se marcaron mal 8 piezas y cada una pierde $5.000 de material. ¿Cuánto se perdió?", ["Se multiplica la cantidad de piezas por lo que pierde cada una.", "8 por 5.000 son 40.000."], "$40.000"),
    ],
    mistakes=[("Creer que se puede mover a mano una plancha pesada si se hace rápido.", "El límite de carga lo fija la norma vigente y el esfuerzo rápido aumenta el riesgo de lesión.", "Pide una ayuda mecánica y personal autorizado."),
              ("Dejar la revisión del trazado para después del corte.", "Una vez cortada, la pieza con error ya no tiene arreglo y el material se pierde.", "Revisa la marca contra el plano antes de cortar.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es trazar una pieza?", "Marcar sobre el material, según el plano, dónde se corta, se dobla o se perfora", "Cortar el material con la forma que pide el plano", "Unir dos piezas según el plano", "Trazar solo marca; cortar y unir son etapas posteriores."),
        ("abc", "En Construcciones Metálicas: ¿qué es una orden de trabajo?", "Un documento que indica qué fabricar, en qué cantidad y con qué plano de referencia", "Una tabla que lista los peligros del taller", "Una autorización para una tarea de riesgo", "La matriz de peligros y el permiso de trabajo son otros documentos."),
        ("abc", "En Construcciones Metálicas: ¿por qué un error de trazado es costoso?", "Porque se arrastra: se corta y se arma una pieza que luego no sirve", "Porque el trazado es la etapa más larga del proceso", "Porque las herramientas de marcado son muy caras", "El costo viene de perder material y horas en las etapas siguientes."),
        ("=", "{F} ¿Cuántos pesos se perdieron en el mes por las planchas mal trazadas?", "5*12000", "Se multiplican las planchas mal trazadas por lo que pierde cada una.", " pesos"),
        ("abc", "{F} ¿Qué riesgo se asocia a mover a mano planchas pesadas?", "Un sobreesfuerzo en la espalda o un golpe si la plancha resbala", "Una descarga eléctrica", "Una intoxicación por pintura", "El peso de la carga se relaciona con sobreesfuerzo y golpes, no con electricidad ni pintura."),
        ("abc", "{F} El taller usa una ayuda mecánica en lugar de mover las planchas a fuerza de brazos. ¿Qué tipo de control es?", "De ingeniería, porque cambia la forma de mover la carga", "EPP, porque protege a las personas", "Administrativo, porque es una regla", "Una ayuda mecánica modifica el trabajo mismo y no depende de la fuerza de cada persona."),
        ("=", "{F} ¿Cuántas planchas prepara el área en una semana?", "4*3", "Se multiplican las planchas de cada turno por los turnos de la semana.", " planchas"),
        ("abc", "{F} Una plancha supera lo que la norma vigente permite cargar a mano. ¿Qué corresponde?", "Usar una ayuda mecánica o pedir apoyo de personal autorizado, sin cargarla a mano", "Cargarla entre dos personas sin más trámite", "Pedir a la persona más fuerte que la levante sola", "El límite de carga se respeta con ayudas, no con más fuerza."),
        ("abc", "{F} Un practicante dice: «ya vi cómo se traza, puedo marcar y cortar planchas yo solo». ¿Qué corresponde?", "Ver o leer sobre una tarea no lo habilita: necesita instructor autorizado y norma vigente", "Puede hacerlo si usa guantes", "Puede hacerlo si la plancha es pequeña", "Observar no da la formación ni la autorización; el EPP no las reemplaza."),
        ("abc", "Durante una visita de ejemplo, una plancha mal apilada resbala y aplasta el pie de una persona. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Levantar tú solo la plancha para liberar el pie", "Esperar a que termine el turno para avisar", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "{F} ¿Por qué se revisa el trazado antes de cortar y no después?", "Porque un error detectado antes evita perder el material y las horas de las etapas siguientes", "Porque después de cortar ya no se puede ver el plano", "Porque el trazado solo se revisa cuando el cliente lo pide", "Una pieza ya cortada con error no tiene arreglo y el costo ya está hecho."),
        ("=", "{F} El taller baja las planchas mal trazadas de 5 a 2 en el mes siguiente. ¿Cuántos pesos deja de perder?", "(5-2)*12000", "Se multiplica la reducción de planchas por la pérdida de cada una.", " pesos"),
        ("abc", "{F} Una persona propone que el proveedor entregue las planchas ya en tamaños menores, para que cada una pese menos. ¿Qué nivel de la jerarquía es?", "Sustitución, porque reemplaza el material pesado por piezas más livianas", "EPP, porque protege a las personas", "Administrativo, porque es una regla", "Cambiar a un material menos peligroso es sustituir, un nivel alto de la jerarquía."),
    ],
    ctx=("abc", "El jefe de turno te pide mover tú solo una plancha que parece muy pesada «porque no hay nadie más». ¿Qué respondes?", "Que esperarás a personal autorizado y a la ayuda mecánica, porque la norma vigente limita el manejo manual de carga", "Que lo harás rápido para no atrasar", "Que la moverás arrastrándola por el piso", "Una carga excesiva no se mueve a fuerza propia ni se arrastra improvisando."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es trazar?", "Marcar sobre el material dónde se corta, se dobla o se perfora", "Trazar solo marca; las etapas siguientes las hace personal autorizado."),
        ("¿Qué documento indica qué fabricar, en qué cantidad y con qué plano?", "La orden de trabajo", "La orden de trabajo reúne esos tres datos para el taller."),
        ("¿Quién fija el límite de carga que una persona puede mover a mano?", "La norma vigente sobre manejo manual de carga", "El límite lo establece la norma, no la fuerza de cada persona."),
    ],
    op=("Caso de ejemplo: el área de preparación de otro taller detecta 4 piezas mal marcadas en una semana. Cada una pierde $7.000 de material y la causa fue usar una lámina de revisión antigua. Escribe (a) cuánto dinero se perdió, (b) un control administrativo que evitaría la causa, (c) por qué conviene revisar el trazado antes de cortar, (d) qué harías si una plancha supera lo que la norma permite cargar a mano.",
        "(a) 4 × 7.000 = 28.000 pesos. (b) Comprobar la revisión vigente de la lámina antes de marcar y anotarla en la orden de trabajo. (c) Porque un error detectado antes evita perder el material y las horas de las etapas siguientes. (d) Pedir una ayuda mecánica o apoyo de personal autorizado, sin cargarla a mano.",
        ["calcula la pérdida", "propone un control administrativo", "explica la revisión previa", "indica qué hacer con una carga excesiva"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar mal las piezas por el costo", "proponer el EPP como único control", "mover la carga a fuerza propia"],
        "Pregunta: «¿qué documento te dice qué revisión usar?». Si no responde, pídele que relea la orden de trabajo."),
    reinforce="Inventa una orden de trabajo de tres líneas con pieza, cantidad y plano de referencia.",
    extend="Explica con un ejemplo por qué una ayuda mecánica es un control más efectivo que pedirle a alguien «cuidado con la espalda».",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 6 (caso de ejemplo, inventado). Plano de taller de una placa base de ejemplo: rectángulo de 300 × 200 mm con 4 perforaciones. El dibujo está en el archivo digital «PB-01», creado en un programa de dibujo asistido por computador (CAD). "
     "Se agrega un margen de corte de 3 mm por cada lado, que es sobrematerial que se retira después. La plancha de partida mide 2.400 × 1.200 mm. Se cuentan solo placas enteras, sin girarlas.")
build(
    O2, 2, F,
    use="Aprenderé los conceptos del trazado digital: dibujo CAD, archivo digital, desarrollo, margen de corte y anidado de piezas, y quién responde por cada cambio.",
    prior=["Sé qué es trazar y qué es una orden de trabajo.", "Sé dividir números enteros.", "Sé que un plano tiene medidas y revisión."],
    explain=[
        "Hoy muchos trazados se preparan con un programa CAD, que es un programa de dibujo asistido por computador: permite dibujar piezas con sus medidas exactas y guardarlas en un archivo digital. El desarrollo de una pieza es su dibujo plano, antes de plegarla, con sus medidas totales. El margen de corte es el sobrematerial que se deja alrededor de la pieza y que se retira después, de modo que la pieza final quede en la medida del plano.",
        "El anidado es la disposición de las piezas sobre la plancha para aprovechar el material y dejar poco sobrante. Se calcula contando cuántas piezas enteras caben en cada fila y en cada columna, y multiplicando: el largo de la plancha dividido entre el largo ocupado por la pieza (solo la parte entera) por el ancho dividido entre el ancho ocupado. Un margen mayor hace que cada pieza ocupe más espacio y caben menos.",
        f"Un archivo digital es un documento del proyecto: se usa solo la versión vigente que entrega el responsable, y un cambio de medidas lo autoriza el proyectista, que emite la revisión. No se reconstruye de memoria ni se copia de otra obra. {EMER} {AVISO}",
    ],
    vocab=[("CAD", "programa de dibujo asistido por computador"), ("archivo digital", "documento del proyecto guardado en el computador"), ("desarrollo", "dibujo plano de una pieza antes de plegarla"), ("margen de corte", "sobrematerial alrededor de la pieza que se retira después"), ("anidado", "disposición de las piezas sobre la plancha para aprovechar el material")],
    worked=[
        ("Medida con margen", "Una pieza de ejemplo mide 150 × 90 mm y lleva un margen de 5 mm por cada lado. ¿Qué largo ocupa con margen?", ["El margen se agrega a cada lado, es decir, dos veces.", "150 más 5 más 5 son 160."], "160 mm"),
        ("Piezas que caben", "En una plancha de ejemplo de 1.800 × 800 mm se anidan piezas que ocupan 150 × 400 mm, sin girarlas. ¿Cuántas caben?", ["En el largo caben 1.800 entre 150, que son 12.", "En el ancho caben 800 entre 400, que son 2, y 12 por 2 son 24."], "24 piezas"),
    ],
    mistakes=[("Sumar el margen de corte solo a un lado de la pieza.", "El margen se deja alrededor, por los dos lados de cada medida.", "Suma el margen dos veces a cada medida."),
              ("Reconstruir de memoria un archivo perdido «para salir del paso».", "Una medida distinta del proyecto produce piezas que no encajan.", "Pide al responsable la versión vigente.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es un programa CAD?", "Un programa de dibujo asistido por computador que guarda las piezas en un archivo digital", "Una máquina que corta planchas siguiendo el plano", "Una norma que fija cómo se miden las piezas", "CAD es dibujo asistido; la máquina y la norma son otra cosa."),
        ("abc", "En Construcciones Metálicas: ¿qué es el anidado de piezas?", "Disponer las piezas sobre la plancha para aprovechar el material y dejar poco sobrante", "Guardar las piezas en cajas dentro de la bodega", "Ordenar los archivos de dibujo por fecha", "El anidado busca aprovechar la plancha, no ordenar bodegas ni archivos."),
        ("abc", "En Construcciones Metálicas: ¿qué es el desarrollo de una pieza?", "Su dibujo plano antes de plegarla, con las medidas totales", "La vista de la pieza desde arriba ya terminada", "La mejora del diseño año a año", "El desarrollo muestra la pieza extendida; la vista desde arriba es la planta."),
        ("=", "{F} ¿Cuántos milímetros de largo mide el rectángulo de la placa base con margen de corte?", "300+2*3", "Se suma el margen a cada lado del largo.", " mm"),
        ("=", "{F} ¿Cuántos milímetros de ancho mide el rectángulo de la placa base con margen de corte?", "200+2*3", "Se suma el margen a cada lado del ancho.", " mm"),
        ("abc", "{F} ¿Para qué sirve el margen de corte?", "Para dejar sobrematerial que se retira después, de modo que la pieza final quede en su medida", "Para que la pieza final quede más grande que el plano", "Para marcar el centro de las perforaciones", "El margen es material de sobra que se retira; no agranda la pieza final."),
        ("abc", "{F} El archivo «PB-01» se perdió y alguien propone dibujar la placa de memoria. ¿Qué corresponde?", "Pedir al responsable la versión vigente del archivo o del plano", "Dibujarla de memoria y marcar encima de la plancha", "Usar el archivo de otra placa que parezca igual", "Las medidas no se reconstruyen de memoria ni se toman de otra obra."),
        ("=", "{F} ¿Cuántas placas de 300 × 200 mm caben en la plancha, sin margen y sin girarlas?", "(2400//300)*(1200//200)", "Se multiplican las que caben a lo largo por las que caben a lo ancho.", " placas"),
        ("=", "{F} Con el margen, cada placa ocupa 306 × 206 mm. ¿Cuántas caben en la plancha, sin girarlas?", "(2400//306)*(1200//206)", "Se cuentan solo placas enteras a lo largo y a lo ancho.", " placas"),
        ("abc", "{F} ¿Por qué caben menos placas al considerar el margen?", "Porque cada placa ocupa más espacio y el sobrante ya no alcanza para otra fila o columna completa", "Porque la plancha se encoge al marcar", "Porque el archivo CAD borra piezas", "Con más espacio por pieza, las filas y columnas enteras disminuyen."),
        ("abc", "En Construcciones Metálicas: un dibujante cambió una cota del archivo sin avisar. ¿Quién debía autorizar el cambio?", "El proyectista, que emite las revisiones", "El prevencionista, que vela por la seguridad", "Cualquier persona del taller que lo crea necesario", "Un cambio de medidas es una revisión del proyecto y la emite quien diseña."),
        ("=", "{F} Se necesitan 70 placas y con margen caben 35 por plancha. ¿Cuántas planchas se necesitan?", "70//35", "Se divide el total de placas entre las que caben por plancha.", " planchas"),
        ("abc", "{F} Dos anidados distintos: el A da 35 placas por plancha y el B da 33. Si lo único que cambia es el material, ¿cuál conviene?", "El A, porque aprovecha mejor el material", "El B, porque tiene menos piezas", "Da lo mismo, porque la plancha es la misma", "Con la misma plancha, más piezas por plancha significa menos material por pieza."),
    ],
    ctx=("abc", "Un compañero propone usar el archivo que tiene guardado en su teléfono, «porque es más fácil que pedir el oficial». ¿Qué respondes?", "Que se usa solo el archivo vigente entregado por el responsable, para no fabricar con una versión equivocada", "Que sí, porque el suyo tiene la misma fecha", "Que sí, si lo imprime antes", "Un archivo sin control de versión puede tener medidas que ya no son las del proyecto."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es el margen de corte?", "Sobrematerial alrededor de la pieza que se retira después", "El margen deja material que luego se retira para llegar a la medida."),
        ("¿Cómo se cuentan las piezas que caben en una plancha?", "Solo piezas enteras, por filas y columnas", "Una pieza partida por el borde no cumple el plano."),
        ("¿Quién autoriza un cambio de medidas en un archivo del proyecto?", "El proyectista, mediante una nueva revisión", "El proyectista emite las revisiones del proyecto."),
    ],
    op=("Caso de ejemplo: una pletina de 450 × 250 mm lleva margen de corte de 4 mm por cada lado y se anida en una plancha de 2.400 × 1.200 mm, sin girarla. Escribe (a) cuánto mide la pletina con margen, (b) cuántas pletinas caben contando solo enteras, (c) qué haces si el archivo de la pletina no abre, (d) quién autoriza cambiarle una medida.",
        "(a) 458 × 258 mm. (b) 2.400 ÷ 458 son 5 enteras y 1.200 ÷ 258 son 4 enteras; 5 × 4 = 20 pletinas. (c) Pido al responsable la versión vigente y no la reconstruyo de memoria. (d) El proyectista, mediante una nueva revisión.",
        ["suma el margen a cada lado", "cuenta piezas enteras", "indica qué hacer con el archivo", "nombra a quien autoriza"],
        ["hoja con las cuatro respuestas"],
        ["sumar el margen una sola vez", "contar piezas partidas", "reconstruir el archivo de memoria"],
        "Pregunta: «¿cuántas veces suma el margen en cada medida?». Si responde una, pídele que relea la definición."),
    reinforce="Elige una pieza inventada de 100 × 60 mm, agrégale un margen de 2 mm por lado y escribe sus medidas con margen.",
    extend="Explica con un ejemplo por qué conviene registrar la versión del archivo CAD en la orden de trabajo.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 7 (caso de ejemplo, inventado). Plancha de 2.400 × 1.200 mm. Se necesitan 40 tapas «T1» de 500 × 450 mm. Se calcula con las medidas del plano, sin margen, y las tapas pueden anidarse en dos orientaciones: "
     "orientación 1, con el lado de 500 mm paralelo al lado largo de la plancha; orientación 2, con el lado de 450 mm paralelo al lado largo. Se cuentan solo tapas enteras, en filas y columnas. "
     "Costo de ejemplo de cada plancha: $48.000. La plancha tiene 28.800 cm² y cada tapa 2.250 cm².")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso de anidado en papel: comparar orientaciones, calcular planchas, ahorro y sobrante, y revisar el cálculo con una planilla verificable.",
    prior=["Sé contar piezas enteras en filas y columnas.", "Sé multiplicar y dividir números enteros.", "Sé qué es el anidado."],
    explain=[
        "En el anidado, una misma pieza puede colocarse en dos orientaciones sobre la plancha, y cada una puede dar una cantidad distinta de piezas. Para cada orientación se cuenta cuántas piezas enteras caben a lo largo, dividiendo el largo de la plancha entre el lado de la pieza que queda paralelo a él, y cuántas caben a lo ancho; el producto es la cantidad por plancha. El resultado de una división como 5,33 no significa 5,33 piezas: solo caben 5 enteras, porque una pieza partida no sirve.",
        "Con la cantidad por plancha se calcula cuántas planchas se necesitan para el total pedido y cuánto cuesta cada alternativa. El sobrante es la superficie de la plancha menos la que ocupan las piezas, y se calcula con áreas en cm². La alternativa que necesita menos planchas ahorra dinero, y esa diferencia es el argumento para elegirla.",
        f"El cálculo se hace en una planilla, porque así queda un registro que otra persona puede revisar y repetir; elegir «a ojo» o «porque siempre se hizo así» no es verificable. Si el plano cambia una medida, se rehace el cálculo. {EMER} {AVISO}",
    ],
    vocab=[("orientación", "forma en que se coloca la pieza sobre la plancha"), ("pieza entera", "pieza que cabe completa, sin quedar partida por el borde"), ("sobrante", "superficie de la plancha que no ocupa ninguna pieza"), ("planilla de cálculo", "tabla donde queda registrado el cálculo para poder revisarlo")],
    worked=[
        ("Piezas por plancha", "En una plancha de ejemplo de 1.800 × 1.200 mm se anidan piezas de 600 × 400 mm con el lado de 600 paralelo al largo. ¿Cuántas caben?", ["A lo largo caben 1.800 entre 600, que son 3.", "A lo ancho caben 1.200 entre 400, que son 3, y 3 por 3 son 9."], "9 piezas"),
        ("Planchas necesarias", "Para 36 piezas de ejemplo, con 9 por plancha, ¿cuántas planchas se necesitan?", ["Se divide el total de piezas entre las que caben por plancha.", "36 entre 9 son 4."], "4 planchas"),
    ],
    mistakes=[("Contar las piezas partidas, por ejemplo 5,33 por fila.", "Una pieza partida por el borde no cumple el plano.", "Cuenta solo la parte entera de la división."),
              ("Elegir una orientación «porque siempre se hizo así».", "Puede dar menos piezas y gastar más material.", "Calcula las dos orientaciones y compara.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿por qué en el anidado se cuentan solo piezas enteras?", "Porque una pieza partida por el borde de la plancha no cumple el plano", "Porque las piezas incompletas pesan menos", "Porque el borde de la plancha no se puede marcar", "Una pieza partida no sirve para el conjunto, por eso se descarta."),
        ("=", "{F} ¿Cuántas tapas caben en una plancha con la orientación 1?", "(2400//500)*(1200//450)", "Se multiplican las tapas enteras a lo largo por las enteras a lo ancho.", " tapas"),
        ("=", "{F} ¿Cuántas tapas caben en una plancha con la orientación 2?", "(2400//450)*(1200//500)", "Se multiplican las tapas enteras a lo largo por las enteras a lo ancho.", " tapas"),
        ("abc", "{F} Un compañero calcula 2.400 ÷ 450 = 5,33 y concluye que caben 5,33 tapas por fila. ¿Qué error cometió?", "Contó piezas partidas: solo caben 5 enteras en la fila", "Dividió por el lado equivocado de la plancha", "Debió redondear hacia arriba a 6", "Redondear hacia arriba contaría una pieza que no cabe completa."),
        ("abc", "{F} ¿Qué orientación conviene?", "La 2, porque da más tapas por plancha que la 1", "La 1, porque fue la primera que se probó", "Ambas igual, porque la tapa es la misma", "Conviene la orientación que aprovecha más la plancha."),
        ("=", "{F} ¿Cuántas planchas se necesitan para las 40 tapas con la orientación conveniente?", "40//10", "Se divide el total de tapas entre las que caben por plancha.", " planchas"),
        ("=", "{F} ¿Cuántas planchas se necesitarían con la otra orientación?", "40//8", "Se divide el total de tapas entre las que caben por plancha con esa orientación.", " planchas"),
        ("=", "{F} ¿Cuántos pesos se ahorran por elegir la orientación conveniente?", "(40//8-40//10)*48000", "Se multiplica la diferencia de planchas por el costo de cada una.", " pesos"),
        ("abc", "{F} Una revisión nueva cambia la tapa de 500 × 450 a 520 × 450 mm. ¿Qué corresponde?", "Rehacer el cálculo con la medida nueva, porque la cantidad por plancha puede cambiar", "Mantener el cálculo anterior, que ya estaba hecho", "Sumar 20 mm al resultado final", "Una medida distinta puede cambiar cuántas piezas enteras caben."),
        ("abc", "{F} ¿Por qué el anidado se calcula en una planilla y no «a ojo» sobre la plancha?", "Porque el cálculo es verificable y deja un registro que otras personas pueden revisar", "Porque mirar la plancha está prohibido", "Porque la intuición siempre da más piezas", "Un cálculo escrito se puede revisar y repetir; la intuición no."),
        ("=", "{F} ¿Cuántos cm² de sobrante deja cada plancha con la orientación conveniente?", "28800-10*2250", "Se resta a la superficie de la plancha la que ocupan las tapas.", " cm²"),
        ("abc", "{F} Con la orientación 2 queda a lo largo de la plancha una franja de 200 mm de ancho. Un compañero quiere sacar de ella una pieza cuadrada de 300 × 300 mm. ¿Es posible?", "No, porque el cuadrado de 300 mm es más ancho que la franja de 200 mm", "Sí, porque la franja es larga", "Sí, si se parte la pieza en dos", "La pieza no cabe si el ancho disponible es menor que su lado."),
        ("abc", "{F} El jefe prefiere la orientación 1 «porque siempre se hizo así». ¿Qué argumento basado en datos puedes darle?", "Que la orientación 2 necesita una plancha menos y ahorra dinero en las 40 tapas", "Que la orientación 1 es más lenta de dibujar", "Que la orientación 2 es más corta", "Un argumento con datos compara planchas y costos, no costumbres."),
    ],
    ctx=("abc", "Una compañera tiene la planilla que dice 4 planchas, pero el pedido a bodega fue de 5. ¿Qué haces?", "Comparar la planilla con el pedido, registrar la discrepancia y avisar al responsable antes de retirar el material", "Retirar 5 por si acaso", "Retirar 4 sin decir nada", "Una discrepancia entre documentos se registra y se informa antes de actuar."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calculan las piezas por plancha?", "Piezas enteras a lo largo por piezas enteras a lo ancho", "El producto de filas por columnas enteras da la cantidad."),
        ("¿Qué es el sobrante de una plancha?", "La superficie que no ocupa ninguna pieza", "Es lo que queda tras restar el área de las piezas."),
        ("¿Por qué se calculan las dos orientaciones?", "Porque pueden dar cantidades distintas de piezas", "Una orientación puede aprovechar mejor la plancha."),
    ],
    op=("Caso de ejemplo: plancha de 2.400 × 1.200 mm y una pieza de 800 × 350 mm; se necesitan 18 piezas y cada plancha cuesta $50.000. Escribe (a) cuántas piezas caben con el lado de 800 mm paralelo al largo, (b) cuántas caben con el lado de 350 mm paralelo al largo, (c) cuántas planchas y cuántos pesos cuesta la mejor orientación, (d) por qué dejas el cálculo en una planilla.",
        "(a) 3 a lo largo y 3 a lo ancho: 9 piezas. (b) 6 a lo largo y 1 a lo ancho: 6 piezas. (c) La primera da 9 por plancha: 18 ÷ 9 = 2 planchas, que cuestan 100.000 pesos. (d) Porque queda un registro que otras personas pueden revisar y repetir.",
        ["calcula la primera orientación", "calcula la segunda", "elige y calcula el costo", "justifica la planilla"],
        ["hoja con las cuatro respuestas"],
        ["contar piezas partidas", "no comparar las dos orientaciones", "calcular sin dejar registro"],
        "Pregunta: «¿cuánto da 1.200 entre 350?». Si responde 3,4, pídele que relea cómo se cuentan las piezas enteras."),
    reinforce="Inventa una pieza y una plancha, calcula cuántas caben en las dos orientaciones y elige la mejor.",
    extend="Explica con un ejemplo por qué la mejor orientación puede cambiar si cambia el tamaño de la pieza.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 8 (datos de ejemplo, inventados). Pieza en U de ejemplo: dos alas de 40 mm y un fondo de 100 mm (medidas exteriores), con 2 pliegues. Regla de la planilla de ejemplo (no es norma): "
     "longitud desarrollada = suma de los tramos exteriores − 2 mm por cada pliegue. Una platina de ejemplo de 400 mm de largo lleva 4 agujeros equidistantes, incluidos los dos extremos, con 360 mm entre los centros extremos "
     "y 20 mm desde cada extremo al centro del primer y último agujero. Equidistantes significa con la misma separación entre centros consecutivos.")
build(
    O2, 4, F,
    use="Aprenderé a calcular en papel la longitud desarrollada de una pieza plegada y la posición de agujeros equidistantes, con una regla de planilla de ejemplo.",
    prior=["Sé qué es el desarrollo de una pieza.", "Sé sumar, restar, multiplicar y dividir.", "Sé que la regla de una planilla la fija el proyecto."],
    explain=[
        "Un pliegue es el doblez de una plancha que forma un ángulo. La longitud desarrollada es el largo total de la pieza ya extendida, antes de plegarla; es el largo de material que hay que preparar. En esta clase se usa una regla de planilla de ejemplo: se suman los tramos exteriores de la pieza y se resta una pequeña reducción por cada pliegue. La regla real depende del material y del proyecto, y la fija el proyectista, no la intuición.",
        "Los agujeros equidistantes tienen la misma separación entre centros consecutivos. Para calcularla se divide la distancia entre los centros extremos entre el número de espacios, que es uno menos que el número de agujeros. Con 4 agujeros hay 3 espacios; dividir entre 4 es un error frecuente. La posición de cada agujero se obtiene sumando esa separación a la posición del anterior, partiendo desde el borde.",
        f"Estos cálculos orientan el trazado en papel; las medidas finales las confirman el plano y el responsable. Aquí no se enseña cómo se dobla ni se perfora. {EMER} {AVISO}",
    ],
    vocab=[("pliegue", "doblez de una plancha que forma un ángulo"), ("longitud desarrollada", "largo total de la pieza extendida, antes de plegarla"), ("equidistantes", "con la misma separación entre centros consecutivos"), ("centro de un agujero", "punto medio del agujero, desde donde se miden las posiciones"), ("espacio", "tramo entre dos agujeros consecutivos")],
    worked=[
        ("Desarrollo de una L", "Una pieza en L de ejemplo tiene tramos exteriores de 50 mm y 70 mm y 1 pliegue. Con la regla de 2 mm por pliegue, ¿qué longitud desarrollada tiene?", ["Se suman los tramos: 50 más 70 son 120.", "Se resta 1 pliegue por 2 mm: 120 menos 2 son 118."], "118 mm"),
        ("Agujeros equidistantes", "Una pletina de ejemplo lleva 3 agujeros equidistantes con 200 mm entre los centros extremos. ¿Cuánto hay entre centros consecutivos?", ["Con 3 agujeros hay 2 espacios.", "200 entre 2 son 100."], "100 mm"),
    ],
    mistakes=[("Dividir la distancia entre centros extremos por el número de agujeros.", "Entre 4 agujeros hay 3 espacios, no 4.", "Divide entre el número de espacios, que es uno menos que los agujeros."),
              ("Olvidar la reducción por pliegue o aplicarla una sola vez teniendo dos pliegues.", "Cada pliegue lleva su reducción.", "Multiplica la reducción por el número de pliegues.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es un pliegue?", "El doblez de una plancha que forma un ángulo", "Una perforación en el borde de la pieza", "Una línea que une dos centros de agujeros", "El pliegue es un doblez; la perforación y la línea son otros conceptos."),
        ("abc", "En Construcciones Metálicas: ¿qué es la longitud desarrollada?", "El largo total de la pieza extendida, antes de plegarla", "El largo de la pieza terminada medido de punta a punta", "La suma de los pliegues", "El desarrollo extiende la pieza para saber cuánto material se prepara."),
        ("abc", "En Construcciones Metálicas: ¿qué significa que 4 agujeros sean equidistantes?", "Que la separación entre centros consecutivos es la misma", "Que todos tienen el mismo diámetro", "Que todos están a 20 mm del borde", "Equidistante se refiere a la separación entre centros, no al diámetro."),
        ("=", "{F} ¿Cuál es la suma de los tramos exteriores de la pieza en U?", "40+100+40", "Se suman las dos alas y el fondo.", " mm"),
        ("=", "{F} ¿Cuántos milímetros se restan en total por los pliegues de la pieza en U?", "2*2", "Se multiplican los pliegues por la reducción de cada uno.", " mm"),
        ("=", "{F} ¿Cuál es la longitud desarrollada de la pieza en U?", "40+100+40-2*2", "Se suman los tramos y se restan las reducciones de los pliegues.", " mm"),
        ("=", "{F} ¿Cuántos milímetros hay entre centros consecutivos de los agujeros de la platina?", "360//3", "Se divide la distancia entre extremos entre los tres espacios.", " mm"),
        ("abc", "{F} Un compañero divide 360 entre 4 agujeros y obtiene 90 mm. ¿Qué error cometió?", "Dividió entre el número de agujeros y debía dividir entre los 3 espacios", "Debió sumar 20 mm del borde", "Debió dividir entre 5", "Entre 4 agujeros hay 3 espacios; esa es la cantidad por la que se divide."),
        ("=", "{F} ¿A qué distancia del extremo de la platina está el centro del tercer agujero?", "20+2*120", "Se suma la distancia al primer agujero y dos separaciones de 120 mm.", " mm"),
        ("abc", "{F} Al calcular la pieza en U se olvidó restar la reducción de los pliegues. ¿Qué ocurre con el largo de material preparado?", "Queda más largo que la longitud desarrollada y la pieza puede no encajar en el conjunto", "Queda más corto que la longitud desarrollada", "Queda igual, porque el pliegue no cambia el largo", "Sin restar la reducción de cada pliegue, el largo calculado sobra y la pieza se aparta de la medida del plano."),
        ("=", "{F} Se dibuja la pieza en U a escala 1:5 en una lámina. ¿Cuántos milímetros mide en la lámina su fondo de 100 mm?", "100//5", "Se divide la medida real entre la escala.", " mm"),
        ("=", "Una platina de ejemplo de 500 mm entre centros extremos lleva 6 agujeros equidistantes. ¿Cuántos milímetros hay entre centros consecutivos?", "500//5", "Con 6 agujeros hay 5 espacios y se divide entre ellos.", " mm"),
        ("=", "{F} Se piden 12 piezas en U. ¿Cuántos milímetros de largo de material en total se necesitan, sin considerar merma?", "12*(40+100+40-2*2)", "Se multiplica la longitud desarrollada por la cantidad de piezas.", " mm"),
    ],
    ctx=("abc", "Un jefe de taller de ejemplo te pide preparar una pieza en U con la reducción por pliegue de otra obra «porque es parecida». ¿Qué respondes?", "Que se usa la regla que fija el proyecto, y que cualquier duda se consulta al proyectista", "Que sí, porque las obras parecidas tienen las mismas reglas", "Que sí, pero restando 1 mm más por si acaso", "La regla de la planilla es del proyecto; no se improvisa con datos de otra obra."),
    sc=[
        ("En Construcciones Metálicas: ¿entre cuántos espacios se divide para 5 agujeros equidistantes?", "Entre 4 espacios", "Cinco agujeros dejan cuatro espacios entre ellos."),
        ("¿Qué se calcula con la longitud desarrollada?", "El largo de material que hay que preparar", "Es el largo de la pieza extendida antes de plegarla."),
        ("¿Quién fija la reducción por pliegue real?", "El proyecto, a través del proyectista", "La regla real depende del material y la fija el proyectista."),
    ],
    op=("Pieza en Z de ejemplo: tramos exteriores de 30 mm, 80 mm y 30 mm, con 2 pliegues, y la misma regla de ejemplo de 2 mm por pliegue. Además, una pletina de 5 agujeros equidistantes con 320 mm entre centros extremos. Escribe (a) la longitud desarrollada de la pieza en Z, (b) la separación entre centros consecutivos, (c) por qué se divide entre 4 y no entre 5, (d) quién confirma la regla real.",
        "(a) 30 + 80 + 30 − 2 × 2 = 136 mm. (b) 320 ÷ 4 = 80 mm. (c) Porque 5 agujeros dejan 4 espacios entre ellos. (d) El proyecto, a través del proyectista.",
        ["calcula la longitud desarrollada", "calcula la separación", "explica los espacios", "nombra quién confirma la regla"],
        ["hoja con las cuatro respuestas"],
        ["no restar los dos pliegues", "dividir entre 5", "tomar la regla de otra obra"],
        "Pregunta: «¿cuántos espacios hay entre 5 agujeros?». Si responde 5, pídele que los dibuje."),
    reinforce="Inventa una pieza en U con tres tramos, calcula su longitud desarrollada con la regla de 2 mm por pliegue y escribe el cálculo.",
    extend="Explica con un ejemplo por qué el número de espacios es siempre uno menos que el número de agujeros.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 9 (caso de ejemplo, inventado). En «Estructuras Demo» hay una zona de trabajos en caliente, es decir, tareas que producen chispas, llama o calor: corte con gas, soldadura con arco eléctrico y esmerilado. "
     "Peligros anotados: radiación luminosa del arco, humos metálicos, chispas, quemaduras, cilindros de gas combustible y de oxígeno, descarga eléctrica y fuego en materiales cercanos. "
     "Datos de ejemplo: la zona emite 3 permisos de trabajo en caliente por día y opera 5 días a la semana; tiene 4 sectores y cada sector cuenta con 2 extintores. Personal con calificación vigente: 7 de las 10 personas de la zona.")
build(
    O3, 1, F,
    use="Aprenderé qué son los trabajos en caliente, qué peligros tienen, qué papel cumplen el permiso, el vigilante de fuego y la calificación, y cómo se ordenan los controles.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé multiplicar y calcular porcentajes sencillos.", "Sé que una tarea de riesgo exige autorización."],
    explain=[
        "Fabricar, unir y reparar elementos metálicos incluye trabajos en caliente: tareas que producen chispas, llama o calor y pueden iniciar un fuego, como el corte con gas, la soldadura y el esmerilado. Sus peligros son la radiación luminosa del arco, los humos metálicos, las chispas, las quemaduras, los cilindros de gas combustible y de oxígeno, la descarga eléctrica y el fuego en materiales cercanos. Este cuaderno no enseña a ejecutar esas tareas: enseña los conceptos, los documentos y las reglas de seguridad.",
        "El permiso de trabajo en caliente autoriza la tarea después de revisar el lugar y las condiciones. El vigilante de fuego es una persona que observa la zona durante y después del trabajo para detectar un inicio de fuego y avisar. Entre los controles, la extracción de humos desde su origen es de ingeniería, el permiso y los carteles son administrativos, y la careta con filtro, los guantes y la ropa de cuero son EPP. Cuando el proyecto lo permite, una unión mecánica evita el trabajo en caliente. Solo personal con calificación vigente, formado y autorizado ejecuta estas tareas, y la Dirección del Trabajo fiscaliza la normativa laboral.",
        f"Los cilindros de gas y los equipos los maneja solo personal capacitado, según la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("trabajo en caliente", "tarea que produce chispas, llama o calor y puede iniciar un fuego"), ("permiso de trabajo en caliente", "documento que autoriza la tarea tras revisar el lugar"), ("vigilante de fuego", "persona que observa la zona para detectar un inicio de fuego y avisar"), ("calificación vigente", "reconocimiento de que una persona está habilitada según la norma para una tarea"), ("extracción de humos", "sistema que retira los humos desde donde se producen")],
    worked=[
        ("Clasificar un control", "En otra zona de ejemplo se instala una pantalla que protege del arco a las personas que pasan. ¿Qué tipo de control es?", ["La pantalla cambia físicamente el lugar.", "Una barrera física es un control de ingeniería."], "De ingeniería"),
        ("Permisos por semana", "Otra zona de ejemplo emite 2 permisos por día y trabaja 6 días. ¿Cuántos permisos emite en la semana?", ["Se multiplican los permisos diarios por los días.", "2 por 6 son 12."], "12 permisos"),
    ],
    mistakes=[("Creer que la careta y los guantes bastan para realizar un trabajo en caliente.", "El EPP es la última barrera: no reemplaza el permiso, la calificación ni los controles del lugar.", "Primero se controla el lugar y la tarea; el EPP se suma a eso."),
              ("Creer que quien vio hacer una soldadura puede hacerla.", "La tarea exige formación, calificación vigente, autorización y permiso.", "Aprende el concepto aquí y deja la tarea a personal calificado.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es un trabajo en caliente?", "Una tarea que produce chispas, llama o calor y puede iniciar un fuego", "Una tarea con herramientas eléctricas pesadas, aunque no produzca chispas", "Una tarea que se hace al aire libre bajo el sol", "Lo que define el trabajo en caliente es la chispa, la llama o el calor que puede iniciar fuego."),
        ("abc", "En Construcciones Metálicas: ¿para qué sirve el permiso de trabajo en caliente?", "Para autorizar la tarea después de revisar el lugar y las condiciones de seguridad", "Para certificar que la persona sabe soldar", "Para reservar la máquina durante el turno", "El permiso autoriza la tarea y el lugar; la calificación certifica a la persona."),
        ("abc", "En Construcciones Metálicas: ¿qué hace el vigilante de fuego?", "Observa la zona durante y después del trabajo para detectar un inicio de fuego y avisar", "Suelda mientras otra persona descansa", "Revisa que los planos estén vigentes", "Su función es vigilar y avisar, no ejecutar la tarea."),
        ("=", "{F} ¿Cuántos permisos de trabajo en caliente se emiten en una semana?", "3*5", "Se multiplican los permisos diarios por los días de la semana.", " permisos"),
        ("=", "{F} ¿Cuántos extintores hay en total en la zona?", "4*2", "Se multiplican los sectores por los extintores de cada sector.", " extintores"),
        ("abc", "{F} El taller instala un sistema que extrae los humos desde el lugar donde se producen. ¿Qué tipo de control es?", "De ingeniería, porque cambia físicamente el lugar de trabajo", "Administrativo, porque ordena una conducta", "EPP, porque protege a una persona", "La extracción actúa sobre el peligro en su origen, sin depender de cada persona."),
        ("abc", "{F} La careta con filtro y los guantes de cuero que usa una persona calificada son:", "EPP, la última barrera de la jerarquía", "Controles de ingeniería, porque son objetos físicos", "Controles administrativos, porque los entrega el taller", "Lo que protege a una sola persona es EPP, aunque sea un objeto físico."),
        ("=", "{F} ¿Qué porcentaje del personal de la zona tiene calificación vigente?", "7*100//10", "Se multiplican por 100 las personas calificadas y se divide entre el total.", " %"),
        ("abc", "{F} Una persona sin calificación vigente propone soldar «solo un punto pequeño» porque ya vio cómo se hace. ¿Qué corresponde?", "No hacerlo: esa tarea solo la hace personal calificado y con permiso", "Hacerlo si es muy rápido", "Hacerlo si usa careta", "Ni la rapidez ni el EPP reemplazan la calificación y el permiso."),
        ("abc", "{F} ¿Por qué conviene, cuando el proyecto lo permite, usar una unión mecánica en vez de una soldada en terreno?", "Porque evita o reduce el trabajo en caliente y con él sus peligros", "Porque la unión mecánica siempre resiste más carga", "Porque no necesita planos", "Evitar la tarea de riesgo es el nivel más alto de prevención."),
        ("abc", "Una chispa prende un material cercano y aparece fuego en una zona de ejemplo. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, dar la alarma y avisar a un adulto responsable y a emergencias", "Acercarte a apagarlo con lo que haya", "Seguir trabajando hasta terminar la pieza", "Un fuego exige avisar a quienes están capacitados; acercarse sin formación aumenta el peligro."),
        ("=", "{F} El taller cambia algunas uniones soldadas por mecánicas y baja de 15 a 9 los permisos semanales. ¿Cuántos permisos menos se emiten?", "3*5-9", "Se resta a los permisos semanales actuales los que quedan.", " permisos"),
        ("abc", "{F} Para el riesgo de chispas sobre un pasillo se discute entre un cartel de «prohibido el paso» y una cortina que no se quema y retiene las chispas. ¿Cuál es más efectiva según la jerarquía?", "La cortina, porque es un control de ingeniería y no depende de que cada persona obedezca", "El cartel, porque es más barato", "Ambas igual, porque las dos avisan del peligro", "La jerarquía prefiere el control físico al aviso, que depende de la conducta."),
    ],
    ctx=("abc", "Un compañero de práctica te ofrece su careta y te propone «probar» soldar un rato mientras nadie mira. ¿Qué respondes?", "Que no, porque soldar exige formación, autorización, permiso y supervisión, y que avisarás a un adulto responsable", "Que sí, pero solo un minuto", "Que sí, si él te mira", "Una tarea de riesgo no se prueba a escondidas; exige autorización y supervisión."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es un trabajo en caliente?", "Una tarea que produce chispas, llama o calor", "Esa característica la hace capaz de iniciar un fuego."),
        ("¿Qué función cumple el vigilante de fuego?", "Observar la zona y avisar ante un inicio de fuego", "Vigila durante y después del trabajo, sin ejecutarlo."),
        ("¿Qué tipo de control es una extracción de humos?", "Un control de ingeniería", "Cambia el lugar y retira el peligro desde su origen."),
    ],
    op=("Caso de ejemplo: un taller planea unir dos piezas de una baranda con soldadura en el pasillo principal. Peligros anotados: chispas sobre el pasillo, humos y un cilindro de gas cercano. Escribe (a) qué documento debe autorizar la tarea, (b) un control de ingeniería para el pasillo, (c) una alternativa que evitaría el trabajo en caliente, (d) por qué el EPP no basta.",
        "(a) El permiso de trabajo en caliente. (b) Una cortina o pantalla que no se queme y retenga las chispas, o una extracción de humos. (c) Una unión mecánica, si el proyecto lo permite, o hacer la unión en el taller y no en el pasillo. (d) Porque el EPP es la última barrera: no quita el peligro y protege solo a quien lo usa. La tarea la hace personal calificado.",
        ["nombra el permiso", "propone un control de ingeniería", "propone una alternativa que evita el trabajo en caliente", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["proponer solo el EPP", "confundir un cartel con un control de ingeniería", "no aclarar que la tarea la hace personal calificado"],
        "Pregunta: «¿qué nivel de la jerarquía elimina el peligro?». Si no responde, pídele que relea el primer nivel."),
    reinforce="Escribe tres peligros de un trabajo en caliente y un control para cada uno, indicando su nivel en la jerarquía.",
    extend="Explica con un ejemplo por qué el vigilante de fuego sigue observando un rato después de terminar el trabajo.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 10 (especificación técnica de ejemplo, inventada) de una escalera metálica. Tabla de uniones: U-1, unión a tope, posición plana, proceso arco manual; U-2, unión en T, posición horizontal, proceso MIG; "
     "U-3, unión por traslape con pernos (unión mecánica), 4 pernos por unión; U-4, unión en T, posición vertical, proceso TIG. La escalera lleva 5 uniones U-1, 10 uniones U-2, 6 uniones U-3 y 8 uniones U-4. "
     "Nota del documento: «los procesos y parámetros aprobados constan en el WPS del proyecto; solo ejecutan soldadores con calificación vigente».")
build(
    O3, 2, F,
    use="Aprenderé los conceptos de los procesos de corte y soldadura, los tipos de unión, las posiciones, las uniones mecánicas y los documentos que mandan, sin aprender a ejecutarlos.",
    prior=["Sé qué es un trabajo en caliente.", "Sé leer una tabla.", "Sé qué es un plano y una especificación técnica."],
    explain=[
        "Una unión se describe por su geometría: a tope, cuando dos piezas se unen extremo con extremo en un mismo plano; en T, cuando una pieza se une perpendicular a otra; y por traslape, cuando una pieza se superpone a otra. Los procesos se distinguen por cómo se forma la unión: el oxigás usa la llama de un gas combustible con oxígeno para calentar o cortar; el arco manual usa un arco eléctrico entre un electrodo revestido y la pieza; el TIG usa un electrodo de tungsteno que no se consume y un gas inerte; el MIG y el MAG usan un alambre continuo que se consume, con gas inerte (MIG) o gas activo (MAG).",
        "La posición describe cómo queda la unión: plana, si queda sobre una superficie horizontal y se trabaja desde arriba; horizontal, si la línea de unión es horizontal sobre una superficie vertical; y vertical, si la línea de unión sube o baja sobre una superficie vertical. Las uniones mecánicas usan pernos, tornillos o remaches; los pernos permiten desarmar la unión sin dañar las piezas, y una soldadura es permanente.",
        f"El WPS es la especificación del procedimiento de soldadura: el documento del proyecto que fija el proceso y los parámetros aprobados. Este cuaderno no los entrega ni los enseña a usar, porque solo los aplica personal con calificación vigente. {EMER} {AVISO}",
    ],
    vocab=[("unión a tope", "dos piezas unidas extremo con extremo en un mismo plano"), ("unión en T", "una pieza unida perpendicular a otra"), ("traslape", "una pieza superpuesta sobre otra"), ("TIG", "proceso con electrodo de tungsteno que no se consume y gas inerte"), ("MIG / MAG", "procesos con alambre continuo que se consume; gas inerte en MIG y gas activo en MAG"), ("WPS", "especificación del procedimiento de soldadura del proyecto"), ("unión mecánica", "unión hecha con pernos, tornillos o remaches")],
    worked=[
        ("Leer una unión", "Un documento de ejemplo dice «unión por traslape, 6 pernos». ¿Es una unión soldada o mecánica?", ["Los pernos son elementos mecánicos.", "Una unión con pernos es mecánica."], "Mecánica"),
        ("Contar pernos", "Una estructura de ejemplo lleva 5 uniones con 8 pernos cada una. ¿Cuántos pernos son?", ["Se multiplican las uniones por los pernos de cada una.", "5 por 8 son 40."], "40 pernos"),
    ],
    mistakes=[("Creer que dos uniones en T se sueldan igual.", "La posición, el espesor y el proceso pueden ser distintos y cada una sigue su especificación.", "Lee en la especificación el proceso y la posición de cada unión."),
              ("Creer que conocer los nombres de los procesos habilita para soldar.", "La ejecución exige calificación vigente, WPS y permiso.", "Usa los nombres para leer documentos, no para ejecutar.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es una unión a tope?", "Dos piezas que se unen extremo con extremo en un mismo plano", "Una pieza que se une perpendicular a otra", "Dos piezas superpuestas una sobre otra", "La unión a tope junta extremos; la perpendicular es en T y la superpuesta es traslape."),
        ("abc", "En Construcciones Metálicas: ¿qué es una unión en T?", "Una pieza que se une perpendicular a otra, formando una T", "Dos piezas unidas extremo con extremo", "Dos piezas superpuestas", "La forma de T viene de la pieza perpendicular."),
        ("abc", "En Construcciones Metálicas: ¿qué caracteriza al proceso de arco manual?", "Un arco eléctrico entre un electrodo revestido y la pieza", "Una llama de gas combustible con oxígeno", "Un alambre continuo protegido por gas", "El arco manual usa electrodo revestido; la llama es oxigás y el alambre continuo es MIG o MAG."),
        ("abc", "{F} ¿Qué proceso indica la unión U-2 y qué lo caracteriza?", "MIG: alambre continuo que se consume, con gas inerte", "MIG: electrodo de tungsteno que no se consume", "MIG: llama de gas combustible con oxígeno", "El electrodo de tungsteno es de TIG; MIG usa alambre continuo."),
        ("abc", "{F} ¿Qué proceso indica la unión U-4 y qué lo caracteriza?", "TIG: electrodo de tungsteno que no se consume, con gas inerte", "TIG: alambre continuo con gas activo", "TIG: llama de gas combustible con oxígeno", "TIG se reconoce por su electrodo de tungsteno que no se consume."),
        ("abc", "{F} La unión U-1 está en posición plana. ¿Qué significa?", "Que la unión queda sobre una superficie horizontal y se trabaja desde arriba", "Que la unión sube por una superficie vertical", "Que la unión es una línea horizontal sobre una pared", "Plana es sobre superficie horizontal; la línea sobre pared es horizontal y la que sube es vertical."),
        ("=", "{F} ¿Cuántos pernos llevan en total las uniones U-3 de la escalera?", "6*4", "Se multiplican las uniones por los pernos de cada una.", " pernos"),
        ("abc", "{F} ¿Qué documento del proyecto fija los procesos y parámetros aprobados para soldar?", "El WPS, la especificación del procedimiento de soldadura", "La lista de piezas de la lámina", "El permiso de trabajo en caliente", "El WPS fija el procedimiento; el permiso autoriza la tarea en un lugar."),
        ("abc", "{F} ¿Por qué este cuaderno no entrega los parámetros de soldadura?", "Porque los fija el WPS del proyecto y la norma vigente, y su uso exige personal calificado", "Porque la soldadura no tiene parámetros", "Porque son iguales en todas las obras", "Los parámetros dependen del proyecto y solo los aplica quien está calificado."),
        ("abc", "{F} ¿Qué ventaja suele tener la unión con pernos U-3 sobre una soldada si hay que desmontar una pieza?", "Puede desarmarse sin dañar las piezas, a diferencia de una soldadura permanente", "Siempre resiste más carga", "No necesita ningún documento", "Los pernos se sueltan; una soldadura se funde con las piezas."),
        ("abc", "En Construcciones Metálicas: ¿quién puede ejecutar una soldadura en una obra?", "Solo personal con calificación vigente, autorizado y con permiso", "Cualquier persona que haya leído el WPS", "Quien tenga careta y guantes", "Leer un documento o tener EPP no reemplaza la calificación y la autorización."),
        ("=", "{F} ¿Cuántas uniones soldadas lleva la escalera, sumando las uniones de tipo U-1, U-2 y U-4?", "5+10+8", "Se suman las uniones que no son mecánicas.", " uniones"),
        ("abc", "{F} Un compañero dice: «U-2 y U-4 son uniones en T, así que se ejecutan igual». ¿Qué corresponde responder?", "Que tienen la misma forma pero distinta posición y proceso, y cada una sigue su especificación", "Que tienen el mismo proceso y la misma posición", "Que ambas son mecánicas", "Dos uniones en T pueden diferir en posición y proceso; la tabla de la especificación manda."),
    ],
    ctx=("abc", "Una compañera ve que la unión U-1 pide arco manual, pero el taller solo tiene personal calificado en MIG. ¿Qué haces?", "Avisar al responsable para que lo resuelva con el proyectista, sin cambiar el proceso por cuenta propia", "Cambiar a MIG, que es parecido", "Usar el proceso que haya a mano", "El proceso lo fija el proyecto; un cambio lo decide quien lo emite."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es el WPS?", "La especificación del procedimiento de soldadura del proyecto", "Es el documento que fija proceso y parámetros aprobados."),
        ("¿Qué es una unión por traslape?", "Una pieza superpuesta sobre otra", "El traslape superpone piezas en lugar de juntar extremos."),
        ("¿Qué ventaja tiene una unión con pernos?", "Puede desarmarse sin dañar las piezas", "Los pernos permiten desmontar, a diferencia de una soldadura."),
    ],
    op=("Documento de ejemplo: unión V-1, a tope, posición vertical, proceso MAG; unión V-2, por traslape con 6 pernos. La obra lleva 3 uniones V-1 y 7 uniones V-2. Escribe (a) cuál unión es mecánica, (b) cuántos pernos hay en total, (c) qué caracteriza al proceso MAG, (d) qué documento fija los parámetros y quién puede aplicarlos.",
        "(a) V-2, porque usa pernos. (b) 7 × 6 = 42 pernos. (c) Usa un alambre continuo que se consume, con gas activo. (d) El WPS del proyecto; solo lo aplica personal con calificación vigente, autorizado y con permiso.",
        ["identifica la unión mecánica", "calcula los pernos", "describe el proceso", "nombra el documento y quién aplica"],
        ["hoja con las cuatro respuestas"],
        ["confundir MAG con TIG", "multiplicar por las uniones equivocadas", "decir que cualquiera puede aplicar el WPS"],
        "Pregunta: «¿qué diferencia hay entre gas inerte y gas activo?». Si no responde, pídele que relea la explicación."),
    reinforce="Haz una tabla con las columnas unión, tipo, posición y proceso, e inventa cuatro filas para una baranda.",
    extend="Explica con un ejemplo por qué una unión soldada es permanente y una con pernos permite desarmar.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 11 (datos de ejemplo, inventados). Lista de soldaduras de un soporte, con la convención del taller, que no es normativa: A = cordón en ángulo; T = cordón a tope; el número es el tamaño en mm; «taller» o «terreno» indica dónde se ejecuta. "
     "S-1: «A5, taller», 500 mm de cordón, 4 unidades. S-2: «T4, taller», 300 mm de cordón, 6 unidades. S-3: «A6, terreno», 600 mm de cordón, 2 unidades. "
     "Reglas de la planilla de ejemplo: cada metro de cordón usa 200 g de material de aporte; el material de aporte cuesta $8.000 el kilogramo.")
build(
    O3, 3, F,
    use="Aprenderé a leer en papel el símbolo de una soldadura, a calcular la longitud total de cordón y el material de aporte de una planilla y a decidir dónde conviene ejecutar cada unión.",
    prior=["Sé qué es una unión en ángulo y una unión a tope.", "Sé multiplicar y pasar de mm a m.", "Sé que una planilla guarda un cálculo revisable."],
    explain=[
        "Un símbolo de soldadura es una anotación del plano que indica el tipo de cordón, su tamaño y, a veces, dónde se ejecuta. Los símbolos reales los define la norma vigente; en esta clase se usa una convención de ejemplo escrita en la ficha. El cordón es el depósito de metal que forma la unión, y el material de aporte es el metal que se agrega para formarlo. Una lista de soldaduras anota para cada cordón su código, su largo y su cantidad.",
        "Para calcular el largo total de cordón se multiplica cada largo por su cantidad y se suman los resultados; no se usa un solo largo para cordones distintos. Después se pasa a metros, dividiendo los milímetros entre 1.000. El material de aporte se estima multiplicando los metros de cordón por el consumo de la planilla, y el costo multiplicando los kilogramos por el precio de ejemplo. Un cordón de terreno es más riesgoso que uno de taller, porque el lugar tiene menos condiciones controladas; por eso se prefiere el taller cuando el proyecto lo permite.",
        f"Es una estimación de planilla con valores de ejemplo: la cantidad real la define el responsable según el proyecto. Aquí no se enseña a soldar. {EMER} {AVISO}",
    ],
    vocab=[("símbolo de soldadura", "anotación del plano con el tipo, tamaño y lugar de un cordón"), ("cordón", "depósito de metal que forma la unión"), ("material de aporte", "metal que se agrega para formar el cordón"), ("cordón en ángulo", "cordón entre dos piezas que forman un ángulo"), ("cordón a tope", "cordón entre dos piezas unidas extremo con extremo")],
    worked=[
        ("Largo total de un tipo", "Un cordón de ejemplo mide 250 mm y hay 8 unidades. ¿Cuántos milímetros suman?", ["Se multiplica el largo por la cantidad.", "250 por 8 son 2.000."], "2.000 mm"),
        ("Aporte estimado", "Con una regla de ejemplo de 150 g por metro, ¿cuántos gramos se estiman para 4 m de cordón?", ["Se multiplican los metros por el consumo por metro.", "4 por 150 son 600."], "600 g"),
    ],
    mistakes=[("Multiplicar la suma de unidades por un solo largo de cordón.", "Los cordones distintos tienen largos distintos.", "Multiplica cada largo por su cantidad y luego suma."),
              ("Olvidar pasar los milímetros a metros antes de usar el consumo por metro.", "El consumo está dado por metro y el resultado queda 1.000 veces mayor.", "Divide los milímetros entre 1.000 primero.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué indica un símbolo de soldadura en un plano?", "El tipo de cordón, su tamaño y dónde se ejecuta, según la norma vigente", "La marca comercial del electrodo", "El nombre de la persona que soldará", "El símbolo comunica el cordón que pide el proyecto, no marcas ni nombres."),
        ("abc", "En Construcciones Metálicas: ¿qué es el material de aporte?", "El metal que se agrega para formar el cordón de la unión", "El metal de las piezas que se unen", "La pintura que protege la unión", "El aporte es el metal agregado; el de las piezas es el metal base."),
        ("abc", "{F} Según la convención de la ficha, ¿qué significa «A5, taller»?", "Cordón en ángulo de tamaño 5 mm, que se ejecuta en el taller", "Cordón a tope de 5 mm que se ejecuta en terreno", "Cordón en ángulo de 5 cm que se ejecuta en terreno", "A es ángulo, 5 es el tamaño en mm y taller indica el lugar."),
        ("=", "{F} ¿Cuántos milímetros de cordón suman las unidades de S-1?", "500*4", "Se multiplica el largo del cordón por su cantidad.", " mm"),
        ("=", "{F} ¿Cuántos milímetros de cordón suman las unidades de S-2?", "300*6", "Se multiplica el largo del cordón por su cantidad.", " mm"),
        ("=", "{F} ¿Cuántos metros de cordón suma todo el soporte?", "(500*4+300*6+600*2)//1000", "Se suman los tres totales y se pasan a metros.", " m"),
        ("=", "{F} ¿Cuántos gramos de material de aporte se estiman para todo el soporte?", "(500*4+300*6+600*2)*200//1000", "Se multiplican los metros de cordón por el consumo por metro.", " g"),
        ("abc", "{F} ¿Cuál es el cordón del soporte que se ejecuta en terreno?", "S-3, porque su código dice «terreno»", "S-1, porque es el más largo", "S-2, porque es a tope", "El lugar se lee en el código, no en el largo ni en el tipo."),
        ("=", "{F} ¿Cuántos pesos cuesta el material de aporte de todo el soporte?", "(500*4+300*6+600*2)*200*8000//1000000", "Se pasan los gramos a kilogramos y se multiplican por el precio.", " pesos"),
        ("abc", "{F} ¿Por qué el taller prefiere ejecutar los cordones en taller y no en terreno, cuando el proyecto lo permite?", "Porque en el taller las condiciones están más controladas y hay menos peligros del lugar", "Porque en terreno no se usan planos", "Porque en el taller no hace falta ningún permiso", "Un lugar controlado reduce el riesgo; el permiso se exige igualmente."),
        ("abc", "{F} Un compañero suma 4 + 6 + 2 = 12 unidades y multiplica por 500 mm para estimar el cordón. ¿Qué error cometió?", "Usó un solo largo para cordones de largos distintos; debía multiplicar cada tipo por su largo", "Debió restar las unidades", "Debió dividir entre 12", "Cada tipo de cordón tiene su largo y su cantidad."),
        ("=", "{F} El proyecto cambia S-3 a 3 unidades. ¿Cuántos milímetros de cordón suma ahora el soporte?", "500*4+300*6+600*3", "Se multiplica cada largo por su cantidad y se suman.", " mm"),
        ("abc", "{F} Una compañera dice: «con 1.000 g alcanza justo; mejor pedir menos y completar después». ¿Qué corresponde responder?", "Que es una estimación de planilla de ejemplo y que la cantidad real la define el responsable según el proyecto", "Que pida el doble sin consultar", "Que no pida nada y cuente al final", "La planilla estima; las cantidades de compra las decide quien responde del proyecto."),
    ],
    ctx=("abc", "El código de un cordón en un plano dice «A6, terreno» y el taller propone ejecutarlo en el taller «para que sea más seguro». ¿Qué respondes?", "Que se consulta al proyectista antes, porque cambiar dónde se ejecuta una unión puede alterar el diseño", "Que sí, porque en el taller siempre es mejor", "Que lo cambien sin avisar si es más seguro", "Un cambio respecto del plano lo decide quien emite el proyecto, aunque la intención sea buena."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calcula el largo total de un tipo de cordón?", "Multiplicando su largo por su cantidad", "Cada tipo tiene su largo y su cantidad."),
        ("¿Cómo se pasan milímetros a metros?", "Dividiendo entre 1.000", "Un metro equivale a mil milímetros exactos."),
        ("¿Qué es el cordón de una soldadura?", "El depósito de metal que forma la unión", "El cordón es el metal depositado entre las piezas."),
    ],
    op=("Lista de ejemplo: S-A «A4, taller», 400 mm, 5 unidades; S-B «T3, taller», 500 mm, 4 unidades. Consumo de ejemplo: 200 g de aporte por metro. Escribe (a) los milímetros de cordón de cada tipo, (b) los metros totales, (c) los gramos de aporte, (d) qué harías si el código de S-A dijera «terreno» y el taller propusiera cambiarlo.",
        "(a) S-A: 400 × 5 = 2.000 mm; S-B: 500 × 4 = 2.000 mm. (b) 4.000 mm son 4 m. (c) 4 × 200 = 800 g. (d) Consultaría al proyectista antes de cambiar dónde se ejecuta, sin decidirlo por mi cuenta.",
        ["multiplica cada largo por su cantidad", "pasa a metros", "calcula el aporte", "propone consultar al proyectista"],
        ["hoja con las cuatro respuestas"],
        ["usar un solo largo para ambos cordones", "olvidar pasar a metros", "cambiar el lugar sin consultar"],
        "Pregunta: «¿cuántos milímetros son 4 m?». Si no responde, pídele que relea la conversión."),
    reinforce="Inventa una lista de dos cordones con código, largo y cantidad, y calcula los metros totales.",
    extend="Explica con un ejemplo por qué cambiar un cordón de terreno a taller puede requerir consultar al proyectista.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 12 (criterios de ejemplo del taller, que no son norma). R1: si la unión debe poder desarmarse, se usa unión mecánica. R2: si la unión es permanente y el taller tiene personal calificado, se prefiere soldada. "
     "R3: en terreno, si el proyecto lo permite, se prefiere unión mecánica para reducir el trabajo en caliente. R4: si se exige acabado muy limpio en piezas delgadas y la unión es soldada, el taller elige TIG. "
     "Casos: A, una tapa de registro que se retira para inspección; B, una baranda de piezas delgadas con acabado limpio, fabricada en el taller, de unión permanente; C, la unión de las vigas de un galpón en terreno, donde el proyecto permite unión mecánica; "
     "D, un soporte permanente de piezas gruesas fabricado en el taller. Costos de ejemplo: unión soldada, $9.000 por unidad; unión mecánica, $6.000 por unidad. La obra tiene 15 uniones C y 8 uniones D.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar criterios escritos para elegir entre unión soldada y mecánica, a comparar costos de planilla y a justificar la decisión con datos.",
    prior=["Sé qué es una unión mecánica y una soldada.", "Sé multiplicar y restar números enteros.", "Sé qué es un trabajo en caliente."],
    explain=[
        "Un criterio de selección es una regla escrita que permite elegir entre alternativas de manera repetible: dos personas con los mismos datos llegan a la misma elección. En esta clase los criterios R1 a R4 son de ejemplo. Para aplicarlos se lee el caso, se busca qué criterio corresponde a sus condiciones (si debe desarmarse, si es permanente, si está en terreno, si exige acabado limpio) y se justifica citando el criterio.",
        "Además del criterio técnico, se compara el costo con una planilla: se multiplica la cantidad de uniones por el costo de cada alternativa y se calcula la diferencia. Elegir por costumbre («siempre se hizo así») o por gusto («es más bonito») no es un argumento verificable. Si un caso no calza con ningún criterio, no se improvisa: se consulta al responsable.",
        f"Una unión soldada, aunque se elija, solo la ejecuta personal calificado, con permiso y controles. {EMER} {AVISO}",
    ],
    vocab=[("criterio de selección", "regla escrita para elegir entre alternativas de manera repetible"), ("unión permanente", "unión que no está pensada para desarmarse"), ("unión desmontable", "unión pensada para poder desarmarse"), ("costo de planilla", "cantidad de uniones por el costo de cada una")],
    worked=[
        ("Aplicar un criterio", "Con los criterios de la ficha, un panel de ejemplo debe poder retirarse cada mes para limpiar. ¿Qué unión corresponde?", ["El panel debe poder desarmarse.", "Eso corresponde al criterio R1, que pide unión mecánica."], "Mecánica, por R1"),
        ("Diferencia de costo", "Para 10 uniones de otro tipo, ¿cuánto se ahorra al elegir la mecánica en lugar de la soldada, con los costos de la ficha?", ["Cada unión ahorra 9.000 menos 6.000, es decir, 3.000.", "10 por 3.000 son 30.000."], "$30.000"),
    ],
    mistakes=[("Elegir una unión por costumbre o por gusto.", "No es un argumento verificable y puede ir contra un criterio del proyecto.", "Cita el criterio y los datos del caso."),
              ("Aplicar un criterio sin revisar si se cumplen sus condiciones.", "R4 exige piezas delgadas y acabado limpio; con piezas gruesas no se aplica.", "Verifica las condiciones de cada criterio antes de usarlo.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es una unión mecánica?", "Una unión hecha con pernos, tornillos o remaches", "Una unión hecha con una soldadura que funde el metal", "Cualquier unión hecha con una máquina", "La unión mecánica se define por sus elementos de fijación, no por usar o no una máquina."),
        ("abc", "En Construcciones Metálicas: ¿qué es un criterio de selección?", "Una regla escrita que permite elegir entre alternativas de manera repetible", "La opinión del jefe de turno", "El precio de la alternativa más barata", "Un criterio es una regla escrita; la opinión y el precio solos no lo son."),
        ("abc", "{F} Según los criterios, ¿qué unión corresponde al caso A?", "Mecánica, por R1, porque la tapa debe poder desarmarse", "Soldada, porque es más resistente", "Soldada con TIG, porque es una pieza delgada", "La tapa se retira para inspección, de modo que debe ser desmontable."),
        ("abc", "{F} ¿Qué unión y proceso corresponde al caso B?", "Soldada con TIG, por R2 y R4", "Mecánica, por R1", "Soldada con arco manual, por R3", "La baranda es permanente, de piezas delgadas y con acabado limpio."),
        ("abc", "{F} ¿Qué unión se prefiere para el caso C?", "Mecánica, por R3, porque en terreno reduce el trabajo en caliente", "Soldada, por R2", "Soldada con TIG, por R4", "R3 manda en terreno cuando el proyecto lo permite, y aquí lo permite."),
        ("abc", "{F} ¿Qué unión se prefiere para el caso D?", "Soldada, por R2, con personal calificado y permiso", "Mecánica, por R3", "Mecánica, por R1", "D es permanente, de taller y de piezas gruesas, de modo que se aplica R2."),
        ("=", "{F} ¿Cuántos pesos cuestan las 15 uniones C si se hacen soldadas?", "15*9000", "Se multiplican las uniones por el costo de la unión soldada.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuestan las 15 uniones C si se hacen mecánicas?", "15*6000", "Se multiplican las uniones por el costo de la unión mecánica.", " pesos"),
        ("=", "{F} ¿Cuántos pesos se ahorran en las uniones C al elegir la que corresponde por criterio?", "15*(9000-6000)", "Se multiplican las uniones por la diferencia de costo de cada una.", " pesos"),
        ("abc", "{F} El jefe dice que las uniones C se hagan soldadas «porque siempre se hizo así». ¿Qué argumento de la ficha puedes darle?", "R3: en terreno se prefiere la unión mecánica, que además cuesta menos aquí", "R2: toda unión se suelda", "R1: las uniones de terreno siempre deben desarmarse", "Se responde con el criterio aplicable y con los datos de costo, no con costumbre."),
        ("abc", "{F} Una compañera propone usar TIG en el caso D «porque es más bonito». ¿Qué corresponde?", "Revisar el criterio: R4 se aplica a piezas delgadas con acabado limpio, y D tiene piezas gruesas", "Usar TIG siempre que se pueda", "Usar TIG si lo dice el jefe", "Un criterio se aplica solo si el caso cumple sus condiciones."),
        ("=", "{F} Con las uniones C mecánicas y las uniones D soldadas, ¿cuántos pesos cuestan en total ambas?", "15*6000+8*9000", "Se suma el costo de cada grupo con la alternativa que corresponde.", " pesos"),
        ("abc", "Caso E, de ejemplo: una unión permanente, en terreno, que el proyecto NO permite hacer mecánica. Con la lógica de los criterios, ¿qué corresponde?", "Una unión soldada, con permiso de trabajo en caliente, personal calificado y todos los controles", "Una unión mecánica de todas formas", "No se puede hacer nunca", "Si R3 no se puede aplicar, la unión permanente se suelda con todos los controles de seguridad."),
    ],
    ctx=("abc", "Una compañera quiere cambiar un perno por una soldadura «rápida» en un soporte que debe poder desarmarse, porque no encuentra el perno. ¿Qué respondes?", "Que no: el soporte debe desarmarse y la solución se consulta al responsable, sin improvisar", "Que sí, si la soldadura queda fuerte", "Que sí, mientras nadie se entere", "Un soporte desmontable no se convierte en permanente por conveniencia."),
    sc=[
        ("En Construcciones Metálicas: ¿qué unión corresponde si la pieza debe poder desarmarse?", "Una unión mecánica", "Los pernos permiten desmontar sin dañar las piezas."),
        ("¿Qué se debe citar al justificar una elección?", "El criterio aplicado y los datos del caso", "La justificación debe poder repetirse con los mismos datos."),
        ("¿Qué se hace si un caso no calza con ningún criterio?", "Se consulta al responsable", "No se improvisa una decisión sin criterio."),
    ],
    op=("Criterios de ejemplo de la ficha. Casos nuevos: F, una pasarela modular que se desarma y se traslada cada temporada; G, una escalera permanente de piezas gruesas fabricada en el taller; H, la unión de 12 vigas en terreno que el proyecto permite hacer mecánica. Costos: soldada $9.000, mecánica $6.000 por unidad. Escribe (a) la unión de F y su criterio, (b) la de G y su criterio, (c) la de H y su criterio, (d) cuánto cuestan las 12 uniones de H con la alternativa elegida.",
        "(a) Mecánica, por R1, porque debe poder desarmarse. (b) Soldada, por R2, con personal calificado y permiso. (c) Mecánica, por R3, porque en terreno reduce el trabajo en caliente. (d) 12 × 6.000 = 72.000 pesos.",
        ["aplica R1", "aplica R2", "aplica R3", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["no citar el criterio", "calcular con el costo de la unión soldada", "olvidar los controles de la unión soldada"],
        "Pregunta: «¿qué condición del caso H activa R3?». Si no responde, pídele que relea el criterio."),
    reinforce="Escribe tres casos breves propios y elige para cada uno una unión citando el criterio de la ficha.",
    extend="Explica con un ejemplo por qué un criterio escrito es mejor que decidir por costumbre.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 13 (datos de ejemplo, inventados). Inspección visual de 20 cordones de un lote: 2 con porosidad, 1 con socavación y 17 sin defectos visibles. "
     "Criterio de aceptación del documento de ejemplo: un lote se acepta si no más del 10 % de los cordones inspeccionados tiene defectos. "
     "Una viga de ejemplo presenta una fisura. Alternativas: reparar (evaluación $10.000, reparación $35.000 y reinspección $10.000) o reemplazar la viga ($90.000). Regla de ejemplo: se reemplaza si la reparación costara más del 70 % del reemplazo. "
     "Ensayos no destructivos de ejemplo: tintes penetrantes, partículas magnéticas, ultrasonido y radiografía.")
build(
    O3, 5, F,
    use="Aprenderé los defectos típicos de un cordón, qué son los ensayos no destructivos, cómo se acepta o rechaza un lote con un criterio y cómo se compara reparar con reemplazar.",
    prior=["Sé qué es un cordón y qué es una no conformidad.", "Sé calcular porcentajes y restar.", "Sé que un registro debe decir la verdad."],
    explain=[
        "La calidad de un cordón se verifica comparándolo con un criterio de aceptación escrito en el proyecto. Los defectos más conocidos son la porosidad, que son burbujas de gas atrapadas en el cordón; la falta de fusión, cuando el metal de aporte no se une bien a una pieza; la socavación, un surco en el borde del cordón sobre el metal base; la fisura o grieta, una rotura fina y grave; y las salpicaduras, gotas de metal pegadas cerca. Primero se hace una inspección visual y, si el proyecto lo exige, ensayos no destructivos.",
        "Un ensayo no destructivo revisa la pieza sin dañarla. Los tintes penetrantes revelan fisuras abiertas en la superficie; las partículas magnéticas detectan defectos superficiales o cercanos a la superficie en acero que se imanta; el ultrasonido usa ondas de sonido para detectar defectos internos; la radiografía usa radiación para ver el interior y solo la hace personal certificado. El porcentaje de defectos es los cordones con defectos por 100 dividido entre los inspeccionados. Si un cordón falla, el responsable evalúa la causa y decide entre reparar y reemplazar, comparando costos y la regla del proyecto.",
        f"Un defecto no se «tapa» sin evaluar su causa y el registro nunca se altera. Aquí no se enseña a reparar. {EMER} {AVISO}",
    ],
    vocab=[("porosidad", "burbujas de gas atrapadas en el cordón"), ("socavación", "surco en el borde del cordón sobre el metal base"), ("fisura", "rotura fina y grave"), ("ensayo no destructivo", "revisión de la pieza que no la daña"), ("criterio de aceptación", "regla escrita que dice cuándo un resultado se acepta"), ("inspección visual", "revisión a simple vista del cordón")],
    worked=[
        ("Porcentaje de defectos", "En una inspección de ejemplo de 25 cordones, 5 tienen defectos. ¿Qué porcentaje es?", ["Se multiplican por 100 los defectuosos y se divide entre los inspeccionados.", "5 por 100 son 500, y 500 entre 25 son 20."], "20 %"),
        ("Decidir un lote", "Con un criterio de ejemplo que acepta hasta 15 % de cordones con defectos, un lote tiene 20 %. ¿Se acepta?", ["El límite permitido es 15 %.", "20 % supera el 15 % permitido."], "Se rechaza"),
    ],
    mistakes=[("Repetir la inspección hasta que el resultado cuadre y anotar solo ese.", "Se oculta el hallazgo real y se altera el registro.", "Registra el resultado real y deja que el responsable decida."),
              ("Tapar una fisura sin evaluar su causa.", "Si la causa sigue, la fisura puede reaparecer o crecer.", "Informa el hallazgo; la evaluación la hace un responsable.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es una socavación?", "Un surco en el borde del cordón, sobre el metal base", "Burbujas de gas atrapadas dentro del cordón", "Gotas de metal pegadas cerca del cordón", "La socavación es un surco; las burbujas son porosidad y las gotas son salpicaduras."),
        ("abc", "En Construcciones Metálicas: ¿qué significa que un ensayo sea no destructivo?", "Que revisa la pieza sin dañarla ni dejarla inservible", "Que no deja ningún registro", "Que puede hacerlo cualquier persona sin formación", "El nombre se refiere a que la pieza queda intacta tras la revisión."),
        ("abc", "En Construcciones Metálicas: ¿qué es la porosidad de un cordón?", "Burbujas de gas atrapadas en el cordón", "Un surco en el borde del cordón", "Una rotura fina y grave", "La porosidad son burbujas; el surco es socavación y la rotura es fisura."),
        ("=", "{F} ¿Cuántos cordones del lote tienen algún defecto?", "2+1", "Se suman los cordones con porosidad y con socavación.", " cordones"),
        ("=", "{F} ¿Qué porcentaje de los cordones inspeccionados tiene defectos?", "(2+1)*100//20", "Se multiplican por 100 los defectuosos y se divide entre los inspeccionados.", " %"),
        ("abc", "{F} Con el criterio de aceptación de la ficha, ¿qué se concluye del lote?", "Se rechaza, porque el 15 % supera el 10 % permitido", "Se acepta, porque la mayoría no tiene defectos", "Se acepta, porque solo fallaron 3 cordones", "El criterio compara el porcentaje con el límite, no la mayoría."),
        ("abc", "{F} ¿Qué ensayo de la ficha usa ondas de sonido para detectar defectos internos?", "El ultrasonido", "Los tintes penetrantes", "Las partículas magnéticas", "Los tintes y las partículas se limitan a la superficie o cerca de ella."),
        ("=", "{F} ¿Cuántos pesos cuesta reparar la viga, sumando evaluación, reparación y reinspección?", "10000+35000+10000", "Se suman los tres costos de la reparación.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta reemplazar la viga que repararla?", "90000-(10000+35000+10000)", "Se resta el costo de reparar al costo de reemplazar.", " pesos"),
        ("abc", "{F} ¿Por qué no basta con «tapar» la fisura sin evaluar su causa?", "Porque si la causa sigue, la fisura puede reaparecer o crecer; por eso la evalúa un responsable", "Porque tapar es más caro que reemplazar", "Porque las fisuras no son defectos", "Sin entender la causa, el problema puede volver."),
        ("abc", "{F} Un compañero propone repetir la inspección hasta que el lote dé menos de 10 %. ¿Qué corresponde?", "Registrar el resultado real y esperar la decisión del responsable", "Repetir hasta que cuadre", "Borrar los cordones defectuosos del registro", "El registro refleja lo observado; no se ajusta para cumplir el criterio."),
        ("=", "{F} ¿Cuántos pesos es el 70 % del costo de reemplazar la viga?", "90000*70//100", "Se multiplica el costo por 70 y se divide entre 100.", " pesos"),
        ("abc", "{F} Con la regla de ejemplo de la ficha, ¿qué conviene hacer con la viga?", "Repararla, porque 55.000 no supera 63.000", "Reemplazarla, porque cuesta más", "Reemplazarla, porque 55.000 supera 35.000", "La regla compara el costo de reparar con el 70 % del reemplazo."),
    ],
    ctx=("abc", "Tras una inspección, el jefe te pide anotar «sin defectos» en un cordón con porosidad, porque «se ve poco». ¿Qué respondes?", "Que el registro debe reflejar lo observado y que informarás el hallazgo al responsable", "Que sí, si el defecto es pequeño", "Que anotarás «sin defectos» y lo dirás después", "Un registro verdadero es la base de la calidad; no se altera por tamaño ni por prisa."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calcula el porcentaje de cordones con defectos?", "Defectuosos por 100, divididos entre inspeccionados", "Compara los defectuosos con el total revisado."),
        ("¿Qué ensayo no destructivo detecta defectos internos con ondas de sonido?", "El ultrasonido", "Las ondas de sonido recorren la pieza y revelan lo interno."),
        ("¿Quién decide entre reparar y reemplazar?", "El responsable, con la evaluación de la causa y los costos", "No lo decide quien detecta el defecto por cuenta propia."),
    ],
    op=("Caso de ejemplo: se inspeccionan 50 cordones y 4 tienen defectos; el criterio acepta hasta 10 %. Para una pieza con fisura, reparar cuesta $20.000 en total y reemplazarla $60.000; la regla de ejemplo reemplaza si la reparación supera el 70 % del reemplazo. Escribe (a) el porcentaje de cordones con defectos, (b) si el lote se acepta, (c) el 70 % del costo de reemplazo y qué conviene, (d) qué haces si el jefe pide no registrar un defecto.",
        "(a) 4 × 100 ÷ 50 = 8 %. (b) Se acepta, porque 8 % no supera el 10 %. (c) El 70 % de 60.000 son 42.000, y 20.000 no lo supera: conviene reparar. (d) Registro el defecto con su valor real e informo al responsable.",
        ["calcula el porcentaje", "aplica el criterio", "compara con la regla", "defiende el registro honesto"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre 40 en vez de entre 50", "aceptar con un porcentaje mayor", "no registrar el defecto"],
        "Pregunta: «¿qué se escribe en el registro de un defecto pequeño?». Si responde que nada, pídele que relea la sección de registro."),
    reinforce="Inventa una inspección de 20 cordones con 2 defectos y calcula el porcentaje.",
    extend="Explica con un ejemplo por qué el ultrasonido y los tintes penetrantes sirven para casos distintos.",
)
