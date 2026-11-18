"""Agropecuaria TP 4.º medio, mención Pecuaria: OAM-01 (entornos de los planteles), OAM-02 (contención, conducción y transporte, solo conceptos) y OAM-03 (reproducción animal, solo conceptos y registros). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_agpe_common import AVISO, EMER, build

O1 = "TP-AGPE-4-OAM-01"
O2 = "TP-AGPE-4-OAM-02"
O3 = "TP-AGPE-4-OAM-03"

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Plantel Demo» es un establecimiento ficticio con un galpón cerrado para 2.000 aves y un potrero abierto para vacunos. "
     "Peligros anotados: polvo y olor a amoníaco en el galpón, calor, ventiladores con partes móviles, tableros eléctricos en un lugar húmedo, un cerco eléctrico del potrero, piso mojado cerca de los bebederos y animales grandes que pueden empujar o golpear.")
build(
    O1, 1, F,
    use="Aprenderé qué son los entornos naturales y artificiales de un plantel, por qué se vigilan sus condiciones físicas y cuáles son los peligros de ese trabajo.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Un plantel pecuario es un establecimiento donde se crían animales con fines productivos. Su entorno puede ser natural, como un potrero con pasto, sombra y agua, o artificial, como un galpón o un corral construido. Las condiciones físicas son la temperatura, la humedad, la ventilación, la luz, la limpieza y el espacio que tienen los animales. Se vigilan según parámetros establecidos, es decir, valores que fija el fabricante, el veterinario o la norma sanitaria vigente.",
        "Vigilar las condiciones es parte del bienestar animal y de la bioseguridad, que son las medidas para evitar que entren o salgan enfermedades del plantel. El trabajo tiene peligros: gases como el amoníaco, que irritan; calor; partes móviles de ventiladores; electricidad cerca del agua; cercos eléctricos; y animales que se asustan. La jerarquía de controles ordena las medidas: eliminar, sustituir, cambiar el lugar o el equipo, reglas y capacitación y, al final, el EPP.",
        f"Una protección fija sobre un ventilador es un control de ingeniería; una regla de no tocar el cerco eléctrico es administrativa. Estas tareas las hace personal capacitado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("entorno natural", "lugar de crianza al aire libre, como un potrero"), ("entorno artificial", "lugar de crianza construido, como un galpón o corral"), ("parámetro", "valor que se fija como referencia para vigilar una condición"), ("bioseguridad", "medidas para evitar que entren o salgan enfermedades del plantel"), ("ventilación", "renovación del aire de un lugar cerrado"), ("amoníaco", "gas de olor fuerte que irrita los ojos y las vías respiratorias"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Natural o artificial", "Un plantel de ejemplo cría ovejas en un potrero con pasto y un cerco. ¿Su entorno es natural o artificial?", ["El potrero es un lugar al aire libre.", "Es un entorno natural."], "Natural"),
        ("Clasificar un control", "Un plantel de ejemplo cambia el piso resbaladizo junto a los bebederos por uno antideslizante con desagüe. ¿Qué tipo de control es?", ["El piso cambia físicamente el lugar.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que si el galpón huele a amoníaco, basta con acostumbrarse.", "El amoníaco irrita y daña a animales y personas.", "Se informa para que se corrija la ventilación y la limpieza."),
              ("Creer que tocar un cerco eléctrico «un segundo» no es peligroso.", "La descarga puede ser dañina.", "Solo personal autorizado interviene los cercos.")],
    T=[
        ("abc", "En el plantel pecuario: ¿qué es un entorno artificial?", "Un lugar de crianza construido, como un galpón o corral", "Un potrero con pasto y sombra", "Un río cercano al plantel", "El entorno artificial es construido; el potrero es natural."),
        ("abc", "En el plantel pecuario: ¿qué es la bioseguridad?", "Las medidas para evitar que entren o salgan enfermedades", "El número de animales por corral", "El color de la ropa de trabajo", "La bioseguridad previene enfermedades que entran o salen del plantel."),
        ("abc", "En el plantel pecuario: ¿qué es un parámetro de un entorno?", "Un valor de referencia para vigilar una condición", "Una enfermedad común", "Un alimento para los animales", "El parámetro fija el valor de referencia, como una temperatura."),
        ("=", "{F} Cada ave consume 2 litros de agua por semana (dato de ejemplo). ¿Cuántos litros consumen todas las aves del galpón en una semana?", "2000*2", "Se multiplica el número de aves por el consumo de cada una.", " litros"),
        ("abc", "{F} Una malla fija sobre las hélices de los ventiladores es un control de tipo:", "De ingeniería, porque cambia físicamente el equipo", "Administrativo, porque es una regla", "De EPP, porque protege a quien trabaja", "La malla es una parte del equipo y funciona siempre."),
        ("abc", "{F} Una regla que dice «no se toca el cerco eléctrico sin autorización» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el cerco", "De sustitución, porque cambia el potrero", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al olor a amoníaco en el galpón?", "Que irrite los ojos y las vías respiratorias de aves y personas", "El olor mismo", "Que el galpón sea grande", "El riesgo es la posibilidad de daño; el gas es el peligro."),
        ("abc", "{F} Una estudiante dice: «puedo arreglar el tablero eléctrico mojado del galpón». ¿Qué respuesta es correcta?", "Es peligroso: la electricidad la trata solo personal eléctrico autorizado", "Es correcto, si apaga la luz", "Es correcto, si usa guantes", "La electricidad en lugar húmedo exige personal autorizado."),
        ("abc", "{F} En una visita, un vacuno se asusta y empuja a una persona contra el cerco. ¿Qué corresponde según las reglas generales?", "No acercarte al animal ni a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte para calmar al animal", "Sacar a la persona tirándola", "Un animal asustado es impredecible; se avisa a quienes pueden actuar."),
        ("abc", "En el plantel pecuario: ¿por qué es importante la ventilación en un galpón cerrado?", "Porque renueva el aire y baja el amoníaco, el calor y la humedad", "Porque hace más ruido", "Porque calienta el galpón siempre", "La ventilación renueva el aire y baja el amoníaco acumulado."),
        ("abc", "{F} Se propone solo entregar mascarillas por el polvo del galpón. ¿Qué medida es más efectiva?", "Mejorar la ventilación y la limpieza que reducen el polvo", "Entregar más mascarillas", "Pedir que se respire por la nariz", "Reducir el polvo en su origen está más arriba que el EPP."),
        ("=", "{F} El potrero tiene 60 vacunos y cada uno bebe 40 litros por día (dato de ejemplo). ¿Cuántos litros se necesitan al día?", "60*40", "Se multiplica el número de animales por el consumo de cada uno.", " litros"),
        ("abc", "En el plantel pecuario: ¿por qué el piso mojado cerca de los bebederos es un peligro?", "Porque puede hacer resbalar a personas y animales", "Porque aumenta el calibre de los animales", "Porque reduce la ventilación", "El piso mojado causa caídas de personas y animales."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por revisar el cerco eléctrico de su potrero «porque ya viste cómo funciona en clases». ¿Qué respondes?", "Que no, porque exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, con guantes", "Que sí, si lo desconectas un rato", "Haber visto el concepto no habilita para intervenir una instalación eléctrica."),
    sc=[
        ("En el plantel pecuario: ¿qué es un entorno natural?", "Un lugar de crianza al aire libre, como un potrero", "El potrero es un entorno al aire libre."),
        ("En el galpón de aves: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En el plantel pecuario: ¿qué gas irrita en un galpón sucio y mal ventilado?", "El amoníaco", "El amoníaco irrita los ojos y las vías respiratorias."),
    ],
    op=("El «Plantel Demo 2» anota una tarea de ejemplo: limpiar el galpón de aves con el piso mojado, sin ventilar, junto a un tablero eléctrico con la tapa abierta. Escribe (a) el peligro del tablero y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a un animal grande asustado cerca de personas.",
        "(a) Peligro: tablero eléctrico abierto en un lugar húmedo; riesgo: que una persona reciba una descarga eléctrica. (b) Una regla de no ingresar al galpón mojado sin autorización. (c) Una tapa fija y un tablero en un lugar seco, instalados por personal eléctrico autorizado. (d) No me acerco al animal, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca al animal y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer tocar el tablero", "proponer calmar al animal"],
        "Pregunta: «¿qué control separa el tablero del agua aunque nadie se acuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres condiciones físicas de un galpón de aves y di cuál instrumento inventado las mediría.",
    extend="Explica con un ejemplo por qué la bioseguridad cuida a los animales y a las personas.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (parámetros y registro de ejemplo, inventados). Galpón de 2.000 aves del «Plantel Demo» en 400 m². Parámetros de ejemplo: temperatura de 18 a 24 grados; humedad del aire de 50 a 70 %; máximo de 8 aves por m². "
     "Lecturas del día: mañana, 17 grados y 65 %; mediodía, 25 grados y 60 %; tarde, 22 grados y 75 %. Documentos: el registro ambiental diario (lecturas de cada día), el plan de bioseguridad y el plan sanitario. Instrumentos: termómetro (temperatura) e higrómetro (humedad).")
build(
    O1, 2, F,
    use="Aprenderé a leer parámetros y lecturas de un galpón, a calcular densidad y a conocer los documentos y roles de la vigilancia del entorno.",
    prior=["Sé qué es el entorno de un plantel.", "Sé comparar un valor con un rango.", "Sé dividir enteros."],
    explain=[
        "Un parámetro tiene un rango, con un mínimo y un máximo. Una lectura es el valor medido con un instrumento: el termómetro mide la temperatura y el higrómetro mide la humedad del aire. Si la lectura queda dentro del rango, está conforme; si queda fuera, no está conforme y se informa. La densidad es el número de animales por metro cuadrado: se calcula dividiendo los animales entre la superficie. Una densidad alta estresa a los animales y favorece las enfermedades.",
        "Los documentos del entorno son el registro ambiental diario, que anota las lecturas con fecha, hora y responsable; el plan de bioseguridad, que dice cómo evitar que entren o salgan enfermedades; y el plan sanitario, que dice cómo cuidar la salud de los animales. El encargado del plantel vigila y registra, el auxiliar ayuda en las tareas y el médico veterinario asesora en salud y bienestar.",
        f"Un registro no se altera para que una lectura «cumpla» el rango. {EMER} {AVISO}",
    ],
    vocab=[("rango", "valores entre un mínimo y un máximo aceptables"), ("lectura", "valor medido con un instrumento"), ("termómetro", "instrumento que mide la temperatura"), ("higrómetro", "instrumento que mide la humedad del aire"), ("conforme", "que está dentro de lo permitido"), ("densidad", "número de animales por metro cuadrado"), ("registro ambiental", "documento que anota las lecturas de cada día")],
    worked=[
        ("Comparar con el rango", "El rango de ejemplo es de 18 a 24 grados y la lectura es 26. ¿Está conforme?", ["26 es mayor que el máximo de 24.", "Está fuera de rango."], "No, está fuera de rango"),
        ("Calcular la densidad", "Un corral de ejemplo tiene 300 aves en 100 m². ¿Cuál es la densidad?", ["Se divide los animales entre la superficie.", "300 entre 100."], "3 aves por m²"),
    ],
    mistakes=[("Anotar una lectura distinta para que cumpla el rango.", "Un registro alterado oculta un problema real.", "Se anota el valor real y se informa."),
              ("Creer que una densidad alta es buena porque «caben más animales».", "El estrés y las enfermedades aumentan.", "Se respeta el máximo del parámetro.")],
    T=[
        ("abc", "En el plantel pecuario: ¿qué es una lectura?", "El valor medido con un instrumento", "El rango aceptable", "La enfermedad de un animal", "La lectura es el valor medido."),
        ("abc", "En el plantel pecuario: ¿qué mide un higrómetro?", "La humedad del aire", "La temperatura del aire", "El peso de los animales", "El higrómetro mide humedad; el termómetro mide temperatura."),
        ("abc", "En el plantel pecuario: ¿qué es la densidad de animales?", "El número de animales por metro cuadrado", "El peso de cada animal", "El tamaño del galpón", "La densidad relaciona animales y superficie."),
        ("=", "{F} ¿Cuál es la densidad del galpón, en aves por metro cuadrado?", "2000//400", "Se dividen las aves entre la superficie del galpón.", " aves por m²"),
        ("abc", "{F} ¿Cumple la densidad del galpón el máximo de ejemplo?", "Sí, porque 5 aves por m² es menor que 8", "No, porque 5 es menor que 8", "No se puede saber sin pesar", "5 aves por m² está bajo el máximo de 8."),
        ("abc", "{F} ¿Qué lectura de la mañana está fuera del rango de temperatura?", "17 grados, que es menor que 18", "22 grados", "25 grados de mediodía", "17 grados está bajo el mínimo de 18; 25 grados está sobre el máximo, pero es la lectura de mediodía."),
        ("abc", "{F} ¿Qué lectura de la tarde está fuera del rango de humedad?", "75 %, que es mayor que 70", "60 %", "65 %", "75 % supera el máximo de 70 %."),
        ("abc", "{F} ¿Qué documento anota las lecturas de cada día?", "El registro ambiental diario", "El plan de bioseguridad", "El plan sanitario", "El registro ambiental guarda las lecturas."),
        ("=", "{F} ¿Cuántas aves como máximo permite el parámetro en el galpón?", "8*400", "Se multiplica el máximo por la superficie.", " aves"),
        ("abc", "{F} Una compañera dice: «la lectura de mediodía es 25 grados, pero la anotamos como 24 para que cumpla». ¿Qué respuesta es correcta?", "Es incorrecto: se anota 25 e informa al encargado", "Es correcto, porque 24 es el máximo", "Es correcto, si es solo un grado", "Alterar un dato oculta un problema."),
        ("abc", "{F} El encargado ve que un ventilador no gira y una estudiante quiere repararlo. ¿Qué corresponde?", "Rechazarlo: la reparación la hace personal autorizado y el encargado informa", "Aceptarlo, si lo apaga", "Aceptarlo, si usa guantes", "Los equipos eléctricos y con partes móviles los repara personal autorizado."),
        ("abc", "{F} ¿Quién asesora en salud y bienestar de las aves?", "El médico veterinario", "El auxiliar del galpón", "El comprador de huevos", "El veterinario asesora en salud y bienestar."),
        ("abc", "En el plantel pecuario: ¿por qué conviene tomar las lecturas siempre a las mismas horas?", "Para poder comparar entre días", "Para que el rango cambie", "Para evitar usar instrumentos", "Tomar las lecturas a las mismas horas permite comparar entre días."),
    ],
    ctx=("abc", "Un conocido te pide que firmes como «encargado» un registro ambiental que no tomaste. ¿Qué respondes?", "Que no, porque firmar un registro que no hiciste lo falsea, y que lo consultarás con un adulto responsable", "Que sí, si confías", "Que sí, solo una vez", "Una firma debe corresponder a la lectura realizada."),
    sc=[
        ("En el plantel pecuario: ¿cómo se calcula la densidad?", "Animales entre superficie", "La densidad es animales por metro cuadrado."),
        ("En el galpón de aves: ¿qué se hace con una lectura fuera de rango?", "Se anota tal cual y se informa", "Ocultarla impide corregir el problema a tiempo."),
        ("En el plantel pecuario: ¿quién vigila y registra el entorno?", "El encargado del plantel", "El encargado registra y vigila el entorno."),
    ],
    op=("Parámetros de ejemplo del «Plantel Demo 3»: temperatura de 20 a 26 grados; humedad de 50 a 70 %; máximo 10 aves por m². Corral de 600 aves en 100 m². Lecturas: 19 grados y 72 %. Escribe (a) la densidad del corral y si cumple, (b) si la temperatura está conforme, (c) si la humedad está conforme, (d) qué haces con las lecturas no conformes.",
        "(a) 600 ÷ 100 = 6 aves por m²; cumple, porque es menor que 10. (b) No, porque 19 es menor que 20. (c) No, porque 72 es mayor que 70. (d) Las anoto tal cual e informo al encargado.",
        ["calcula la densidad", "evalúa la temperatura", "evalúa la humedad", "no altera las lecturas"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "cambiar las lecturas"],
        "Pregunta: «¿19 está arriba o abajo del mínimo de 20?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula la densidad de 450 aves en 90 m².",
    extend="Explica con un ejemplo por qué una densidad muy alta favorece las enfermedades.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Registro de tres días del galpón del «Plantel Demo». Día 1: 22 grados, 60 %, sin olor. Día 2: 26 grados, 75 %, olor leve a amoníaco; un ventilador no gira. Día 3: 27 grados, 80 %, olor fuerte a amoníaco; la cama (material del piso) está mojada bajo un bebedero que gotea; "
     "varias aves jadean. Parámetros de ejemplo: de 18 a 24 grados y de 50 a 70 % de humedad.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un registro de varios días, a relacionar cada desviación con una causa posible y a decidir a quién informar y qué no hacer.",
    prior=["Sé comparar una lectura con un rango.", "Sé qué es la ventilación y el amoníaco.", "Sé leer un registro con datos."],
    explain=[
        "Para analizar un registro se compara cada lectura con su rango y se mira la tendencia: si los valores empeoran día a día, hay un problema que crece. La temperatura alta con humedad alta y amoníaco suele indicar poca ventilación y cama húmeda. Un bebedero que gotea moja la cama; la cama mojada libera más amoníaco y favorece enfermedades. Aves que jadean (respiran con el pico abierto) pueden estar sufriendo calor.",
        "Un buen análisis ordena las causas posibles, las evidencias y las acciones, y aclara quién actúa. El encargado informa al jefe del plantel y al veterinario; el personal de mantención autorizado repara el ventilador y el bebedero; el veterinario evalúa la salud de las aves. Nadie sin formación entra a reparar equipos eléctricos ni maneja aves enfermas por cuenta propia.",
        f"El bienestar de los animales se vigila a diario, y los desvíos se informan el mismo día. {EMER} {AVISO}",
    ],
    vocab=[("tendencia", "dirección en que cambian los valores día tras día"), ("cama", "material que cubre el piso del galpón"), ("jadeo", "respiración con el pico abierto por calor"), ("desvío", "lectura que se sale del rango"), ("evidencia", "dato del registro que respalda una conclusión")],
    worked=[
        ("Ver la tendencia", "Las temperaturas de tres días de ejemplo son 21, 23 y 25 grados. ¿La tendencia sube o baja?", ["Cada valor es mayor que el anterior.", "Sube."], "Sube"),
        ("Causa y efecto", "En un galpón de ejemplo un bebedero gotea y la cama está mojada. ¿Qué efecto es probable?", ["La cama mojada libera más amoníaco.", "También favorece enfermedades."], "Más amoníaco y más riesgo de enfermedades"),
    ],
    mistakes=[("Esperar a que el problema se solucione solo.", "Una tendencia que empeora crece si nadie actúa.", "Se informa desde el primer desvío."),
              ("Intentar reparar el ventilador sin autorización.", "Hay partes móviles y electricidad.", "Se informa a mantención autorizada.")],
    T=[
        ("abc", "En el plantel pecuario: ¿qué es la tendencia de una serie de lecturas?", "La dirección en que cambian los valores día tras día", "El promedio de las lecturas", "El rango aceptable", "La tendencia muestra si los valores suben o bajan."),
        ("abc", "En el plantel pecuario: ¿qué es la cama de un galpón?", "El material que cubre el piso", "El lugar donde duerme el encargado", "El bebedero", "La cama cubre el piso del galpón."),
        ("abc", "En el plantel pecuario: ¿qué es el jadeo en aves?", "Respirar con el pico abierto por calor", "Cantar de madrugada", "Comer más de lo normal", "El jadeo es respirar con el pico abierto."),
        ("abc", "{F} ¿Qué día muestra la temperatura fuera del rango por primera vez?", "El día 2, con 26 grados", "El día 1, con 22 grados", "El día 3, con 27 grados", "El día 1 está dentro del rango; el día 2 supera por primera vez los 24."),
        ("=", "{F} ¿Cuántos grados superó el día 3 el máximo del parámetro?", "27-24", "Se resta el máximo a la lectura del día 3.", " grados"),
        ("abc", "{F} ¿Qué evidencia de la ficha explica la cama mojada?", "Un bebedero que gotea", "Un día de calor", "Una cama nueva", "La ficha dice que la cama está mojada bajo un bebedero que gotea."),
        ("abc", "{F} ¿Qué evidencia sugiere poca ventilación?", "Un ventilador que no gira y amoníaco que aumenta", "Una temperatura de 22 grados", "Un bebedero nuevo", "El ventilador parado y el amoníaco apuntan a poca renovación de aire."),
        ("abc", "{F} ¿Cuál es la tendencia de la humedad durante los tres días?", "Sube", "Baja", "Se mantiene", "60, 75 y 80 % suben cada día."),
        ("abc", "{F} Una compañera dice: «puedo arreglar el ventilador, es solo cambiar una correa». ¿Qué respuesta es correcta?", "Es incorrecto: lo repara personal autorizado, con el equipo sin energía", "Es correcto, si no es difícil", "Es correcto, si apaga la luz", "Un ventilador tiene partes móviles y electricidad."),
        ("abc", "{F} Varias aves jadean y una persona quiere entrar al galpón a tocarlas una por una. ¿Qué corresponde?", "Informar al encargado y al veterinario, sin manipularlas por cuenta propia", "Entrar a revisarlas", "Darles agua con un medicamento", "La salud de las aves la evalúa el veterinario."),
        ("=", "{F} Si el galpón tiene 2.000 aves y jadean el 5 %, ¿cuántas aves jadean?", "2000*5//100", "Se calcula el porcentaje sobre el total de aves.", " aves"),
        ("abc", "{F} ¿A quién se informa que el bebedero gotea?", "Al personal de mantención autorizado", "A un estudiante", "Al comprador", "La mantención la ejecuta personal autorizado."),
        ("abc", "En el plantel pecuario: ¿por qué conviene informar el primer desvío en vez de esperar?", "Porque una tendencia que empeora puede dañar a los animales", "Porque los desvíos se solucionan solos", "Porque informar demora el trabajo", "Corregir temprano evita daños mayores a los animales."),
    ],
    ctx=("abc", "Un conocido te describe un galpón con olor fuerte a amoníaco y te pide que le recomiendes un producto. ¿Qué respondes?", "Que no puedes recomendarlo, que mejore la ventilación y la limpieza con personal autorizado y que consulte al veterinario", "Que use cualquier desinfectante", "Que cubra el olor con otro olor", "El olor indica un problema de ambiente que debe evaluarse."),
    sc=[
        ("En el plantel pecuario: ¿qué efecto tiene un bebedero que gotea sobre la cama?", "La moja y aumenta el amoníaco", "La cama mojada libera más amoníaco."),
        ("En el galpón de aves: ¿quién repara un ventilador?", "Personal de mantención autorizado", "Los equipos con electricidad y partes móviles los repara personal autorizado."),
        ("En el plantel pecuario: ¿qué se hace al notar un desvío?", "Se informa el mismo día", "Informar a tiempo evita daños a animales y personas."),
    ],
    op=("Registro de ejemplo del «Plantel Demo 4», parámetros 18 a 24 grados y 50 a 70 %: día 1, 23 grados y 65 %; día 2, 25 grados y 72 %, olor a amoníaco; día 3, 27 grados y 78 %, olor fuerte, bebedero que gotea. Escribe (a) cuántos grados superó el día 3 el máximo, (b) la tendencia de la humedad, (c) una causa posible y su evidencia, (d) a quién informas y qué no haces.",
        "(a) 27 − 24 = 3 grados. (b) Sube. (c) Cama mojada por un bebedero que gotea, porque la ficha lo indica. (d) Informo al encargado y al veterinario; no reparo ni manipulo aves por cuenta propia.",
        ["calcula el exceso", "describe la tendencia", "cita causa y evidencia", "informa sin intervenir"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "intervenir por cuenta propia"],
        "Pregunta: «¿qué valores de humedad aparecen cada día?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Escribe una tendencia inventada de tres temperaturas que suba y otra que baje.",
    extend="Explica con un ejemplo por qué un bebedero que gotea puede ser un problema sanitario.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Potrero de 20 hectáreas del «Plantel Demo» con 80 vacunos. Consumo de agua: 50 litros por animal por día (dato de ejemplo). Estanque de agua de 12.000 litros (de ejemplo). "
     "Carga animal máxima de ejemplo: 5 animales por hectárea. Un galpón de aves de 300 m² con máximo de 8 aves por m².")
build(
    O1, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular carga animal, consumo de agua y capacidad de un galpón para mantener las condiciones de un plantel.",
    prior=["Sé qué es la densidad.", "Sé multiplicar y dividir enteros.", "Sé comparar un valor con un máximo."],
    explain=[
        "La carga animal es el número de animales por hectárea en un potrero. Si supera el máximo, el pasto no alcanza y el suelo se deteriora. Se calcula dividiendo los animales entre las hectáreas y se compara con el máximo. En un galpón, la capacidad es el máximo de animales por metro cuadrado multiplicado por los metros cuadrados.",
        "El consumo diario de agua es el número de animales por los litros que bebe cada uno. Los días de agua que dura un estanque son su volumen dividido entre el consumo diario. Se debe vigilar que el agua nunca falte, porque la sed es un problema grave de bienestar. Estos valores son de ejemplo y las decisiones las toma el encargado con el veterinario.",
        f"Los cálculos no reemplazan la revisión en terreno hecha por personal capacitado. {EMER} {AVISO}",
    ],
    vocab=[("carga animal", "número de animales por hectárea"), ("capacidad", "máximo de animales que caben según un parámetro"), ("consumo diario", "litros que bebe un animal por día"), ("estanque", "depósito que guarda agua"), ("bienestar", "vivir sin hambre, sed, dolor ni miedo excesivos")],
    worked=[
        ("Carga animal", "Un potrero de ejemplo de 10 hectáreas tiene 30 vacunos. ¿Cuál es la carga animal?", ["Se dividen los animales entre las hectáreas.", "30 entre 10."], "3 animales por hectárea"),
        ("Días de agua", "Un estanque de ejemplo tiene 6.000 litros y se consumen 2.000 por día. ¿Cuántos días dura?", ["Se divide el volumen entre el consumo diario.", "6.000 entre 2.000."], "3 días"),
    ],
    mistakes=[("Creer que se puede aumentar la carga animal sin límite mientras haya agua.", "El pasto y el suelo también se agotan.", "Se respeta la carga máxima."),
              ("Calcular el agua sin multiplicar por los días.", "El estanque se gasta cada día.", "Se divide el volumen entre el consumo diario.")],
    T=[
        ("abc", "En el plantel pecuario: ¿qué es la carga animal de un potrero?", "El número de animales por hectárea", "El peso de los animales", "El agua que bebe cada animal", "La carga animal relaciona animales y superficie."),
        ("abc", "En el plantel pecuario: ¿qué es el consumo diario de agua de un animal?", "Los litros que bebe en un día", "La capacidad del estanque", "La densidad del galpón", "El consumo diario mide lo que bebe cada día."),
        ("abc", "En el plantel pecuario: ¿por qué no debe faltar agua nunca?", "Porque la sed es un problema grave de bienestar", "Porque los animales comerían menos pasto", "Porque se usa menos el pasto", "La falta de agua daña el bienestar."),
        ("=", "{F} ¿Cuál es la carga animal del potrero, en animales por hectárea?", "80//20", "Se dividen los vacunos entre las hectáreas.", " animales por hectárea"),
        ("abc", "{F} ¿Cumple la carga animal el máximo de ejemplo?", "Sí, porque 4 es menor que 5", "No, porque 4 es menor que 5", "No se puede saber", "4 animales por hectárea está bajo el máximo de 5."),
        ("=", "{F} ¿Cuántos litros de agua beben los 80 vacunos al día?", "80*50", "Se multiplican los animales por el consumo de cada uno.", " litros"),
        ("=", "{F} ¿Cuántos días alcanza el estanque de 12.000 litros?", "12000//(80*50)", "Se divide el volumen del estanque entre el consumo diario.", " días"),
        ("=", "{F} ¿Cuántas aves como máximo caben en el galpón?", "8*300", "Se multiplica el máximo por la superficie del galpón.", " aves"),
        ("=", "{F} ¿Cuántos vacunos como máximo admitiría el potrero según la carga de ejemplo?", "5*20", "Se multiplica el máximo de animales por hectárea por las hectáreas.", " vacunos"),
        ("abc", "{F} El encargado quiere agregar 40 vacunos al potrero «porque hay agua». ¿Cuál es el problema?", "Superaría la carga máxima y el pasto y el suelo se deteriorarían", "Ninguno, porque hay agua", "Que los vacunos beberían menos", "Con 120 animales habría 6 por hectárea, más que el máximo."),
        ("abc", "{F} Un estudiante quiere ayudar a mover a los vacunos al potrero nuevo. ¿Qué corresponde?", "Rechazarlo: el manejo de animales lo hace personal capacitado", "Aceptarlo, si son dóciles", "Aceptarlo, si va acompañado", "Mover animales exige formación, autorización y norma vigente."),
        ("abc", "{F} Un vacuno herido cae al suelo y patalea cerca de ti. ¿Qué corresponde según las reglas generales?", "No acercarte, avisar a un adulto responsable y a emergencias", "Acercarte a levantarlo", "Sujetarlo del cuello", "Un animal herido es impredecible; se avisa a quienes pueden actuar."),
        ("abc", "En el plantel pecuario: ¿por qué no conviene superar la carga animal máxima?", "Porque el pasto no alcanza y el suelo se deteriora", "Porque los animales aprenden más rápido", "Porque el estanque se llena", "Una carga excesiva agota el pasto."),
    ],
    ctx=("abc", "Un conocido te pregunta cuántos animales puede poner en su potrero y te dice solo cuántas hectáreas tiene. ¿Qué respondes?", "Que depende de la carga máxima del lugar y del pasto, y que lo define un asesor", "Que ponga 10 por hectárea", "Que ponga los que quepan", "La carga depende del pasto y del suelo."),
    sc=[
        ("En el plantel pecuario: ¿cómo se calcula la carga animal?", "Animales entre hectáreas", "La carga animal es la relación entre animales y superficie."),
        ("En el potrero: ¿cómo se calculan los días que dura un estanque?", "Volumen entre consumo diario", "Los días resultan de dividir el volumen entre el consumo."),
        ("En el plantel pecuario: ¿cuántas aves caben en 100 m² con un máximo de 8 por m²?", "800 aves", "Se multiplica el máximo por la superficie."),
    ],
    op=("Datos de ejemplo del «Plantel Demo 5»: potrero de 30 hectáreas con 120 vacunos; carga máxima de ejemplo de 5 por hectárea; consumo de 40 litros por animal por día; estanque de 9.600 litros. Escribe (a) la carga animal y si cumple, (b) el consumo diario del potrero, (c) cuántos días dura el estanque, (d) qué haces si ves un animal descontrolado.",
        "(a) 120 ÷ 30 = 4 animales por hectárea; cumple, porque es menor que 5. (b) 120 × 40 = 4.800 litros. (c) 9.600 ÷ 4.800 = 2 días. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["calcula la carga y concluye", "calcula el consumo", "calcula los días", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "olvidar multiplicar por el consumo"],
        "Pregunta: «¿cuántos litros bebe cada animal por día?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Calcula la carga animal de un potrero inventado de 15 hectáreas con 60 animales.",
    extend="Explica con un ejemplo por qué una carga animal excesiva daña el suelo.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Plantel Demo» debe trasladar un grupo de vacunos y un grupo de ovinos a otro predio en un camión. Peligros anotados: animales grandes que pueden patear, empujar o aplastar contra un cerco, personas que se acercan por detrás, pisos resbaladizos, rampas de carga, "
     "un camión que puede volcar en un camino de tierra y el miedo de los animales ante lo desconocido.")
build(
    O2, 1, F,
    use="Aprenderé qué significan contención, sujeción, conducción y transporte de animales, por qué son tareas de alto riesgo y por qué las hace solo personal capacitado.",
    prior=["Sé qué es el bienestar animal.", "Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita."],
    explain=[
        "La contención es limitar el movimiento de un animal a un espacio, como un corral. La sujeción es inmovilizar a un animal para atenderlo. La conducción es moverlo de un lugar a otro. El transporte es trasladarlo en un vehículo. Todas estas tareas se hacen según la especie, el sexo y la edad del animal, y según la naturaleza de la labor. Un animal asustado es impredecible, aunque sea manso.",
        "Estas tareas tienen riesgos graves para las personas, como golpes, patadas, aplastamientos y caídas, y para los animales, como estrés, lesiones y muerte. Por eso solo las hace personal capacitado, autorizado y con instalaciones adecuadas, con respeto por el bienestar animal. Este cuaderno no enseña cómo hacerlo: solo explica los conceptos, los peligros y los documentos.",
        f"La norma vigente de bienestar animal y de transporte regula cómo se mueve a los animales. {EMER} {AVISO}",
    ],
    vocab=[("contención", "limitar el movimiento de un animal a un espacio"), ("sujeción", "inmovilizar a un animal para atenderlo"), ("conducción", "mover a los animales de un lugar a otro"), ("transporte", "traslado de animales en un vehículo"), ("bienestar animal", "vivir sin hambre, sed, dolor ni miedo excesivos"), ("estrés", "reacción del animal ante miedo, dolor o cambios bruscos"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Distinguir tareas", "En un predio de ejemplo se lleva a un grupo de ovejas desde un potrero hasta el corral. ¿Es contención, sujeción, conducción o transporte?", ["Se mueve a los animales de un lugar a otro.", "Eso es conducción."], "Conducción"),
        ("Clasificar un control", "Un predio de ejemplo construye un pasillo con paredes fijas para separar a las personas de los animales. ¿Qué tipo de control es?", ["El pasillo con paredes cambia físicamente el lugar.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que un animal manso nunca reacciona.", "El miedo o el dolor lo vuelven impredecible.", "Se asume que cualquier animal puede reaccionar."),
              ("Creer que leer sobre sujeción habilita para inmovilizar un animal.", "Esa labor exige formación y autorización.", "Aprende aquí el concepto y deja la labor a personal capacitado.")],
    T=[
        ("abc", "En el manejo de animales: ¿qué es la contención?", "Limitar el movimiento de un animal a un espacio", "Inmovilizar a un animal para atenderlo", "Trasladarlo en un vehículo", "La contención limita el movimiento a un espacio."),
        ("abc", "En el manejo de animales: ¿qué es la sujeción?", "Inmovilizar a un animal para atenderlo", "Mover animales de un potrero a otro", "Dar de comer a los animales", "La sujeción inmoviliza al animal para poder atenderlo."),
        ("abc", "En el manejo de animales: ¿qué es el estrés de un animal?", "Su reacción ante miedo, dolor o cambios bruscos", "Su aumento de peso", "Su color de pelaje", "El estrés es una reacción al miedo o al dolor."),
        ("=", "{F} El camión tiene 36 m² de superficie y se asigna 1 m² por animal (dato de ejemplo). ¿Cuántos animales caben como máximo?", "36//1", "Se divide la superficie del camión entre el espacio por animal.", " animales"),
        ("abc", "{F} Una rampa de carga con paredes laterales fijas es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla", "De EPP, porque protege a quien carga", "La rampa es una estructura fija que ayuda a conducir."),
        ("abc", "{F} Una regla que dice «solo personal capacitado conduce a los animales al camión» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia la rampa", "De sustitución, porque cambia a los animales", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a acercarse por detrás a un vacuno?", "Que el animal patee y cause una lesión grave", "El animal mismo", "Que el vacuno coma menos", "El riesgo es la posibilidad de daño; el animal asustado es el peligro."),
        ("abc", "{F} Una estudiante dice: «los terneros son pequeños, así que puedo sujetarlos yo». ¿Qué respuesta es correcta?", "Es peligroso: sujetar animales exige formación y autorización", "Es correcto, si son pequeños", "Es correcto, si hay un adulto mirando", "El tamaño o un observador no reemplazan la formación."),
        ("abc", "{F} En una visita, un vacuno se asusta en la rampa y empuja a una persona. ¿Qué corresponde según las reglas generales?", "No acercarte al animal ni a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a calmar al animal", "Tirar de la persona hacia ti", "Un animal asustado es impredecible; se avisa a quienes pueden actuar."),
        ("abc", "En el manejo de animales: ¿por qué el miedo hace más peligroso a un animal?", "Porque lo vuelve impredecible y puede huir o golpear", "Porque lo vuelve más lento", "Porque le quita la fuerza", "El miedo provoca reacciones bruscas e impredecibles en el animal."),
        ("abc", "{F} Se propone solo entregar cascos para evitar golpes de patadas. ¿Qué medida es más efectiva?", "Contar con instalaciones adecuadas y personal capacitado que eviten el contacto", "Entregar cascos más resistentes", "Pedir que no se acerquen mucho", "Reducir el contacto con instalaciones y formación actúa sobre el peligro."),
        ("=", "{F} Si se cargan 30 vacunos en un camión de 36 m² a razón de 1 m² por animal, ¿cuántos m² quedan libres?", "36-30", "Se resta el espacio ocupado a la superficie del camión.", " m²"),
        ("abc", "En el manejo de animales: ¿por qué las instalaciones adecuadas protegen a personas y animales?", "Porque limitan el contacto y reducen el estrés", "Porque los animales se acostumbran a cualquier lugar", "Porque no necesitan personal", "Instalaciones adecuadas reducen golpes y estrés."),
    ],
    ctx=("abc", "Un conocido te pide que lo ayudes a subir sus vacunos a un camión «porque eres joven y ágil». ¿Qué respondes?", "Que no, porque exige formación, instalaciones y autorización, y que lo consultarás con un adulto responsable", "Que sí, si son pocos", "Que sí, si vas por delante", "La agilidad no reemplaza la capacitación."),
    sc=[
        ("En el manejo de animales: ¿qué es la conducción?", "Mover a los animales de un lugar a otro", "La conducción es el movimiento entre lugares."),
        ("En el manejo de animales: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En el manejo de animales: ¿quién realiza la sujeción de un animal?", "Personal capacitado y autorizado", "La sujeción exige formación y norma vigente."),
    ],
    op=("El «Plantel Demo 2» anota una tarea de ejemplo: cargar vacunos a un camión por una rampa resbaladiza, con personas que se acercan por detrás, de noche. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si un animal se asusta y empuja a alguien.",
        "(a) Peligro: rampa resbaladiza y personas por detrás de los animales; riesgo: que alguien resbale o reciba una patada y se lastime. (b) Una regla de cargar solo con luz y con personal capacitado. (c) Una rampa antideslizante con paredes laterales fijas. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer calmar al animal", "proponer solo EPP"],
        "Pregunta: «¿qué control cambia la rampa y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el tercer párrafo."),
    reinforce="Clasifica como contención, sujeción, conducción o transporte: mover ovejas al corral, llevar vacunos en camión y cerrar un portón del potrero.",
    extend="Explica con un ejemplo por qué un animal manso puede ser peligroso si se asusta.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 2 (datos y documentos de ejemplo, inventados). Traslado de 24 ovinos adultos y 12 terneros de 4 meses del «Plantel Demo» a otro predio, a 120 km por camino. Instalaciones del plantel: corral de espera, pasillo estrecho de paso y rampa de carga. "
     "Documentos: el documento oficial de movimiento animal que exige la norma vigente, el registro de identificación individual de cada animal y la hoja de transporte con la hora de salida y de llegada. Roles: encargado, personal de manejo capacitado, transportista autorizado y médico veterinario.")
build(
    O2, 2, F,
    use="Aprenderé cómo la especie, el sexo y la edad influyen en el manejo, y cuáles son las instalaciones, los documentos y los roles del traslado de animales, sin aprender cómo se manipulan.",
    prior=["Sé qué son contención, sujeción, conducción y transporte.", "Sé qué es el bienestar animal.", "Sé leer una ficha de datos."],
    explain=[
        "La especie, el sexo y la edad cambian cómo reacciona un animal y cuánto riesgo hay. Las hembras con crías suelen proteger mucho a sus crías; los machos adultos pueden ser más agresivos, sobre todo en época de reproducción; los animales jóvenes son más frágiles y se estresan con facilidad. Por eso cada traslado se planifica con el veterinario y el encargado, no se improvisa.",
        "Las instalaciones sirven para que los animales se muevan con menos estrés: un corral de espera, un pasillo estrecho de paso y una rampa de carga. Los documentos dan trazabilidad: el documento oficial de movimiento animal indica qué animales salen, de dónde y hacia dónde; la identificación individual dice quién es cada animal; la hoja de transporte registra horarios. El transportista autorizado conduce el vehículo, el personal de manejo capacitado trabaja con los animales y el veterinario asesora sobre su estado.",
        f"Un documento de transporte no se altera ni se omite. {EMER} {AVISO}",
    ],
    vocab=[("identificación individual", "marca o código que distingue a cada animal"), ("documento de movimiento animal", "documento oficial que acompaña el traslado de animales"), ("hoja de transporte", "documento con los horarios de salida y llegada"), ("corral de espera", "corral donde esperan los animales antes de ser movidos"), ("rampa de carga", "rampa por la que suben los animales al vehículo"), ("trazabilidad", "posibilidad de seguir el recorrido de un animal")],
    worked=[
        ("Elegir el documento", "Un encargado de ejemplo quiere saber a qué hora salió un camión con animales. ¿Qué documento consulta?", ["Los horarios se anotan en la hoja de transporte.", "No es la identificación individual."], "La hoja de transporte"),
        ("Cálculo de horas", "Un camión de ejemplo salió a las 8 y llegó a las 11. ¿Cuántas horas duró el viaje?", ["Se resta la hora de salida a la de llegada.", "11 menos 8."], "3 horas"),
    ],
    mistakes=[("Trasladar animales sin el documento oficial «porque es poca distancia».", "La norma exige el documento para el movimiento.", "Se consulta el documento antes de mover."),
              ("Cargar juntos a machos adultos y hembras con crías sin evaluar.", "Pueden reaccionar de forma violenta.", "El veterinario y el encargado planifican el traslado.")],
    T=[
        ("abc", "En el manejo de animales: ¿qué es la identificación individual?", "Una marca o código que distingue a cada animal", "El nombre del dueño del predio", "La hoja de transporte", "La identificación distingue a cada animal de los demás del plantel."),
        ("abc", "En el manejo de animales: ¿para qué sirve la hoja de transporte?", "Para registrar los horarios de salida y llegada", "Para fijar el precio de los animales", "Para medir la altura de la rampa", "La hoja de transporte anota los horarios."),
        ("abc", "En el manejo de animales: ¿qué es una rampa de carga?", "Una rampa por la que suben los animales al vehículo", "Un corral de espera", "Un estanque de agua", "La rampa permite subir al vehículo."),
        ("=", "{F} ¿Cuántos animales se trasladan en total?", "24+12", "Se suman los ovinos y los terneros.", " animales"),
        ("=", "{F} Si el camión viaja a 60 km por hora, ¿cuántas horas toma recorrer los 120 km?", "120//60", "Se divide la distancia entre la velocidad.", " horas"),
        ("abc", "{F} ¿Qué documento acompaña el traslado e indica qué animales salen y hacia dónde van?", "El documento oficial de movimiento animal", "El registro de identificación individual", "La hoja de transporte", "El documento oficial acompaña el movimiento; la hoja solo anota horarios."),
        ("abc", "{F} ¿Qué rol conduce el vehículo?", "El transportista autorizado", "El personal de manejo", "El veterinario", "El transportista autorizado conduce el vehículo."),
        ("abc", "{F} ¿Qué rol asesora sobre el estado de los animales?", "El médico veterinario", "El transportista", "El comprador", "El veterinario asesora sobre la salud y el estado de los animales."),
        ("abc", "{F} Una compañera dice: «los terneros de 4 meses son frágiles, así que los llevo yo en brazos al camión». ¿Qué respuesta es correcta?", "Es peligroso: el manejo lo hace personal capacitado", "Es correcto, si son livianos", "Es correcto, si se asustan", "Un animal asustado puede lesionar a la persona."),
        ("abc", "{F} El encargado quiere salir sin el documento oficial «para ganar tiempo». ¿Qué corresponde?", "Rechazarlo: el documento es obligatorio y se consulta antes de salir", "Aceptarlo, si la distancia es corta", "Aceptarlo, si se compra después", "La norma vigente exige el documento para mover animales."),
        ("=", "{F} Si cada ovino y cada ternero ocupa 1 m² (dato de ejemplo), ¿cuántos m² necesita el traslado?", "24*1+12*1", "Se suman los metros cuadrados de ovinos y de terneros.", " m²"),
        ("abc", "{F} Un ternero se cae en la rampa y los otros se asustan. ¿Qué corresponde a quien observa?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Entrar a levantarlo", "Gritar para que se muevan", "Entrar con animales asustados es peligroso."),
        ("abc", "En el manejo de animales: ¿por qué se planifica el traslado con el veterinario?", "Porque la especie, la edad y el estado del animal cambian el riesgo", "Porque el veterinario conduce el camión", "Porque reemplaza al transportista", "Cada caso tiene riesgos distintos según la especie y la edad."),
    ],
    ctx=("abc", "Un conocido te pide que firmes la hoja de transporte de un traslado en el que no estuviste. ¿Qué respondes?", "Que no, porque firmarla sin haber estado la falsea, y que lo consultarás con un adulto responsable", "Que sí, si confías", "Que sí, solo una vez", "Una firma certifica algo que debe haber ocurrido."),
    sc=[
        ("En el manejo de animales: ¿qué documento acompaña el traslado?", "El documento oficial de movimiento animal", "La norma vigente exige ese documento."),
        ("En el traslado de animales: ¿quién conduce el vehículo?", "El transportista autorizado", "Conducir un vehículo con animales exige autorización."),
        ("En el manejo de animales: ¿cómo se calcula el tiempo de viaje?", "Distancia entre velocidad", "El tiempo resulta de dividir la distancia entre la velocidad."),
    ],
    op=("Ficha de ejemplo del «Plantel Demo 3»: traslado de 30 ovinos en un camión de 40 m² (1 m² por animal) a 180 km, con un camión que viaja a 60 km por hora; salida a las 8 horas. Escribe (a) cuántos m² quedan libres, (b) cuántas horas dura el viaje, (c) a qué hora llega, (d) qué documento oficial debe acompañar el traslado.",
        "(a) 40 − 30 = 10 m². (b) 180 ÷ 60 = 3 horas. (c) 8 + 3 = 11 horas. (d) El documento oficial de movimiento animal.",
        ["calcula el espacio libre", "calcula las horas", "calcula la hora de llegada", "nombra el documento"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "omitir el documento oficial"],
        "Pregunta: «¿entre qué número divides la distancia para obtener las horas?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Calcula las horas de un viaje de 150 km a 50 km por hora.",
    extend="Explica con un ejemplo por qué la identificación individual ayuda a la trazabilidad.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). El «Plantel Demo» evalúa los riesgos de dos traslados. Traslado X: 20 terneros recién separados de sus madres, 120 km, temperatura de 32 grados, 4 horas de viaje, sin agua en el trayecto. "
     "Traslado Y: 10 vacas con crías de pocos días, 20 km, temperatura de 18 grados, 40 minutos de viaje. Máximo de ejemplo recomendado sin agua: 3 horas. Rampa resbaladiza en el predio de origen.")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso de traslado con evidencias de riesgo para personas y animales, a priorizar y a derivar las decisiones a quien corresponde, sin planificar el manejo.",
    prior=["Sé qué factores cambian el riesgo del manejo.", "Sé qué es el bienestar animal.", "Sé comparar valores con un máximo."],
    explain=[
        "Para analizar un caso de traslado se leen los factores de riesgo: la edad y el estado de los animales, la distancia y el tiempo de viaje, la temperatura, el acceso a agua y las instalaciones. Los animales jóvenes recién separados de sus madres están estresados; el calor y los viajes largos sin agua aumentan el estrés y la deshidratación; las vacas con crías recientes son muy protectoras. Estos factores se suman: cuantos más haya, mayor es el riesgo.",
        "La priorización ordena los riesgos de mayor a menor. Un buen análisis nombra el factor, su evidencia y qué decisión se deriva: por ejemplo, consultar al veterinario sobre el momento del viaje, programar una hora más fresca o acortar el tiempo. Las decisiones las toman el encargado y el veterinario; el manejo lo hace personal capacitado; este cuaderno no enseña cómo hacerlo.",
        f"Si un animal cae durante el traslado o se descontrola, las personas se alejan y piden ayuda. {EMER} {AVISO}",
    ],
    vocab=[("factor de riesgo", "condición que aumenta la posibilidad de daño"), ("deshidratación", "falta de agua en el cuerpo"), ("priorización", "orden de los riesgos de mayor a menor"), ("destete", "separación de las crías de sus madres"), ("derivar", "pasar una decisión a quien corresponde")],
    worked=[
        ("Identificar un factor", "Un viaje de ejemplo dura 5 horas con calor y sin agua. ¿Qué factor de riesgo hay?", ["El calor y el tiempo sin agua se suman.", "Hay riesgo de deshidratación."], "Deshidratación"),
        ("Comparar con el máximo", "El máximo sin agua es 3 horas y un viaje de ejemplo la pasa 5 horas. ¿Cuánto lo excede?", ["Se resta el máximo al tiempo real.", "5 menos 3."], "2 horas"),
    ],
    mistakes=[("Pensar que solo la distancia define el riesgo del traslado.", "También cuentan el calor, la edad y el agua.", "Se suman todos los factores."),
              ("Decidir el traslado sin consultar al veterinario.", "El veterinario evalúa el estado de los animales.", "Se deriva la decisión.")],
    T=[
        ("abc", "En el manejo de animales: ¿qué es un factor de riesgo?", "Una condición que aumenta la posibilidad de daño", "Una enfermedad común", "Un documento oficial", "El factor de riesgo hace más probable el daño."),
        ("abc", "En el manejo de animales: ¿qué es la deshidratación?", "La falta de agua en el cuerpo", "El exceso de agua en el pasto", "La falta de pasto", "La deshidratación es falta de agua en el cuerpo."),
        ("abc", "En el manejo de animales: ¿qué significa derivar una decisión?", "Pasarla a quien corresponde", "Ocultarla", "Tomarla sin consultar", "Derivar es entregar la decisión al responsable que corresponde."),
        ("=", "{F} ¿Cuántas horas excede el Traslado X el máximo sin agua?", "4-3", "Se resta el máximo de ejemplo al tiempo de viaje.", " hora"),
        ("abc", "{F} ¿Qué traslado tiene más factores de riesgo?", "El X, por el calor, el tiempo sin agua y el estrés de los terneros", "El Y, por la distancia", "Ambos por igual", "El X suma calor, tiempo sin agua y estrés."),
        ("abc", "{F} ¿Qué evidencia indica estrés en los terneros del Traslado X?", "Están recién separados de sus madres", "Viajan a 120 km", "La temperatura es de 18 grados", "La separación reciente estresa a los terneros."),
        ("abc", "{F} ¿Qué factor de riesgo especial tiene el Traslado Y?", "Las vacas con crías recientes son muy protectoras", "El calor intenso", "El viaje largo", "La ficha dice que las vacas tienen crías de pocos días."),
        ("abc", "{F} ¿Qué decisión conviene derivar al veterinario y al encargado respecto del Traslado X?", "Evaluar si conviene otra hora más fresca o acortar el tiempo sin agua", "Aumentar la temperatura", "Cargar más terneros", "Los factores de calor y tiempo se pueden reducir con la planificación."),
        ("abc", "{F} Una estudiante dice: «ya sé qué hacer, así que mañana sujeto a los terneros para cargarlos». ¿Qué respuesta es correcta?", "Es peligroso: el manejo lo hace personal capacitado y autorizado", "Es correcto, si hace frío", "Es correcto, si son pocos", "El análisis en papel no habilita para sujetar animales."),
        ("=", "{F} Si el Traslado Y dura 40 minutos y el X dura 4 horas (240 minutos), ¿cuántos minutos más dura el X?", "240-40", "Se resta la duración del Y a la del X, ambas en minutos.", " minutos"),
        ("abc", "{F} Durante la carga, un ternero cae de la rampa resbaladiza y un adulto intenta levantarlo a mano mientras los demás se agolpan. ¿Qué corresponde a quien lo observa?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Entrar a ayudar", "Empujar a los otros animales", "Entre animales asustados puede haber golpes; se avisa a quienes pueden actuar."),
        ("abc", "{F} Si en el Traslado X el viaje se acortara a 3 horas, ¿qué cambiaría respecto del máximo sin agua?", "Dejaría de excederlo", "Seguiría excediéndolo", "No se puede comparar", "3 horas no supera el máximo de 3."),
        ("abc", "En el manejo de animales: ¿por qué conviene priorizar los riesgos?", "Para atender primero los más graves", "Para ignorar los pequeños", "Para evitar escribir el análisis", "Priorizar ordena la atención de los riesgos."),
    ],
    ctx=("abc", "Un conocido te pide que le digas, sin conocer sus animales, si puede trasladarlos hoy con calor. ¿Qué respondes?", "Que lo decide con su veterinario según el estado de los animales y las condiciones", "Que sí, siempre", "Que no, nunca", "Las condiciones y el estado de los animales cambian la decisión."),
    sc=[
        ("En el manejo de animales: ¿qué factores aumentan el riesgo de un traslado?", "Calor, tiempo sin agua y estrés", "Esos factores se suman y aumentan el riesgo total."),
        ("En el traslado de animales: ¿a quién se derivan las decisiones sobre el estado de los animales?", "Al médico veterinario", "El veterinario evalúa el estado de los animales."),
        ("En el manejo de animales: ¿qué hace quien observa un animal caído y asustado?", "Se aleja y avisa", "Un animal asustado es impredecible, aunque sea manso."),
    ],
    op=("Caso de ejemplo del «Plantel Demo 4»: Traslado P, 15 ovinos jóvenes, 6 horas de viaje, 34 grados, sin agua; Traslado Q, 10 ovinos adultos, 1 hora de viaje, 20 grados. Máximo sin agua: 3 horas. Escribe (a) cuántas horas excede P el máximo, (b) cuál traslado tiene más factores de riesgo y dos evidencias, (c) a quién derivas la decisión, (d) qué haces si un animal se cae y se descontrola.",
        "(a) 6 − 3 = 3 horas. (b) El P: viaje largo sin agua y calor de 34 grados. (c) Al encargado y al médico veterinario. (d) Me alejo y aviso a un adulto responsable y a emergencias.",
        ["calcula el exceso", "elige el traslado de más riesgo con dos evidencias", "deriva la decisión", "se aleja y avisa"],
        ["hoja con las cuatro respuestas"],
        ["no citar evidencias", "decidir por cuenta propia"],
        "Pregunta: «¿qué traslado tiene más horas sin agua y más calor?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Escribe tres factores de riesgo de un traslado inventado de animales jóvenes en verano.",
    extend="Explica con un ejemplo por qué el calor y la falta de agua se suman al estrés.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). El «Plantel Demo» compara dos camiones para trasladar 120 animales. Camión A: 40 m², 1 m² por animal, viaje de 2 horas, costo $200.000 por viaje. Camión B: 60 m², 1 m² por animal, viaje de 2 horas, costo $270.000 por viaje. "
     "Pérdida por estrés de ejemplo: 1 animal por viaje, a $300.000 por animal perdido.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular capacidad, número de viajes, costo y pérdida esperada por estrés de un traslado.",
    prior=["Sé qué es la capacidad de un camión.", "Sé multiplicar y dividir enteros.", "Sé calcular porcentajes sencillos."],
    explain=[
        "La capacidad de un camión es la superficie dividida por el espacio que se asigna a cada animal. El número de viajes es el total de animales dividido por la capacidad; si no sale exacto, se redondea hacia arriba. El costo del traslado es el número de viajes por el costo de cada viaje. También se considera la pérdida esperada: si cada viaje transporta más animales, aumenta el riesgo de estrés y de pérdidas.",
        "Un cálculo ayuda a comparar, pero no decide solo. Más animales por viaje reducen el costo, pero no se puede superar el espacio asignado a cada animal, porque el hacinamiento daña el bienestar. La decisión final la toma el encargado con el veterinario y el transportista autorizado, que conocen el estado de los animales y las condiciones del viaje.",
        f"Los valores son de ejemplo, y ningún ahorro justifica poner en riesgo a personas o animales. {EMER} {AVISO}",
    ],
    vocab=[("capacidad del camión", "superficie dividida por el espacio de cada animal"), ("viaje", "un recorrido completo del camión cargado"), ("hacinamiento", "exceso de animales en un espacio pequeño"), ("pérdida esperada", "animales que se estima que se perderán"), ("costo del traslado", "viajes por el costo de cada viaje")],
    worked=[
        ("Capacidad", "Un camión de ejemplo de 30 m² asigna 1 m² por animal. ¿Cuántos animales caben?", ["Se divide la superficie entre el espacio por animal.", "30 entre 1."], "30 animales"),
        ("Número de viajes", "Hay que trasladar 90 animales en un camión de capacidad 30. ¿Cuántos viajes?", ["Se divide el total entre la capacidad.", "90 entre 30."], "3 viajes"),
    ],
    mistakes=[("Cargar más animales que la capacidad para ahorrar un viaje.", "El hacinamiento daña el bienestar y aumenta las pérdidas.", "Se respeta el espacio asignado."),
              ("Comparar solo el costo del viaje.", "La pérdida por estrés también cuesta.", "Se suma la pérdida esperada.")],
    T=[
        ("abc", "En el manejo de animales: ¿qué es la capacidad de un camión?", "La superficie dividida por el espacio de cada animal", "El peso del camión", "La velocidad del viaje", "La capacidad indica cuántos animales caben."),
        ("abc", "En el manejo de animales: ¿qué es el hacinamiento?", "Un exceso de animales en un espacio pequeño", "La falta de animales en un camión", "La distancia entre predios", "El hacinamiento daña el bienestar y aumenta las pérdidas."),
        ("abc", "En el manejo de animales: ¿qué hay que hacer si el número de viajes no sale exacto?", "Redondear hacia arriba", "Redondear hacia abajo y dejar animales sin trasladar", "Cargar más animales", "No se puede dejar animales sin viaje."),
        ("=", "{F} ¿Cuántos animales caben en el Camión A?", "40//1", "Se divide la superficie entre el espacio por animal.", " animales"),
        ("=", "{F} ¿Cuántos animales caben en el Camión B?", "60//1", "Se divide la superficie entre el espacio por animal.", " animales"),
        ("=", "{F} ¿Cuántos viajes necesita el Camión A para los 120 animales?", "120//40", "Se divide el total de animales entre la capacidad del camión.", " viajes"),
        ("=", "{F} ¿Cuántos viajes necesita el Camión B para los 120 animales?", "120//60", "Se divide el total de animales entre la capacidad del camión.", " viajes"),
        ("=", "{F} ¿Cuál es el costo total del traslado con el Camión A?", "120//40*200000", "Se multiplican los viajes por el costo de cada uno.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total del traslado con el Camión B?", "120//60*270000", "Se multiplican los viajes por el costo de cada uno.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan las pérdidas por estrés del traslado completo con el Camión A?", "120//40*1*300000", "Se multiplican los viajes por los animales perdidos en cada uno y por su valor.", " pesos"),
        ("abc", "{F} Un chofer propone cargar 10 animales más en el Camión A para ahorrar un viaje. ¿Qué corresponde?", "Rechazarlo: se respeta el espacio por animal y la capacidad", "Aceptarlo, si son livianos", "Aceptarlo, si el viaje es corto", "El hacinamiento daña el bienestar y puede causar pérdidas."),
        ("abc", "{F} Una estudiante quiere ayudar a cargar los animales al camión. ¿Qué corresponde?", "Rechazarlo: la carga la hace personal capacitado y autorizado", "Aceptarlo, si va con un adulto", "Aceptarlo, si usa guantes", "El manejo y la carga exigen formación."),
        ("abc", "En el manejo de animales: ¿por qué el cálculo más barato no siempre es el mejor?", "Porque también cuentan el bienestar y las pérdidas por estrés", "Porque los camiones más baratos no existen", "Porque el costo no importa", "El bienestar y las pérdidas son parte de la decisión."),
    ],
    ctx=("abc", "Un conocido te pregunta cuántos animales puede poner en su camión y te da solo el largo. ¿Qué respondes?", "Que faltan el ancho y el espacio por animal, y que lo define el transportista con el veterinario", "Que ponga los que quepan", "Que ponga el doble", "La capacidad depende del espacio por animal que fija la norma."),
    sc=[
        ("En el manejo de animales: ¿cómo se calcula la capacidad de un camión?", "Superficie entre espacio por animal", "La capacidad resulta de dividir la superficie entre el espacio por animal."),
        ("En el traslado de animales: ¿cómo se calcula el costo del traslado?", "Viajes por el costo de cada viaje", "El costo se multiplica por los viajes."),
        ("En el manejo de animales: ¿se puede superar la capacidad para ahorrar un viaje?", "No, daña el bienestar", "El hacinamiento daña a los animales."),
    ],
    op=("Datos de ejemplo del «Plantel Demo 5»: trasladar 90 animales; camión R de 30 m² (1 m² por animal), $150.000 por viaje; camión S de 45 m² (1 m² por animal), $210.000 por viaje. Escribe (a) los viajes de R, (b) los viajes de S, (c) el costo de cada opción, (d) por qué no cargarías más animales para ahorrar.",
        "(a) 90 ÷ 30 = 3 viajes. (b) 90 ÷ 45 = 2 viajes. (c) R: 3 × 150.000 = $450.000; S: 2 × 210.000 = $420.000. (d) Porque el hacinamiento daña el bienestar y aumenta las pérdidas.",
        ["calcula los viajes de R", "calcula los viajes de S", "calcula los costos", "explica por qué no superar la capacidad"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "proponer superar la capacidad"],
        "Pregunta: «¿cuántos animales caben en cada camión?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula los viajes para trasladar 100 animales en un camión de capacidad 25.",
    extend="Explica con un ejemplo por qué el hacinamiento puede aumentar las pérdidas.",
)

# ============================================================ OAM-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Plantel Demo» tiene 100 vacas de leche y un grupo de ovejas. Se planea el programa reproductivo del año con ayuda de un médico veterinario. "
     "Peligros anotados: animales en celo, que están más inquietos; machos reproductores, que pueden ser agresivos; recipientes con nitrógeno líquido (un líquido extremadamente frío) para guardar semen; productos hormonales de uso veterinario; agujas y otros elementos cortopunzantes; y el contacto con fluidos de los animales, que puede transmitir enfermedades (zoonosis).")
build(
    O3, 1, F,
    use="Aprenderé qué es la reproducción animal, qué son el celo, la monta, la inseminación artificial y la sincronización, y por qué estas técnicas son de alto riesgo y las hace solo personal autorizado.",
    prior=["Sé qué es el bienestar animal.", "Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita."],
    explain=[
        "La reproducción animal busca que las hembras queden preñadas y tengan crías, según los objetivos de producción del plantel. El celo es el período en que la hembra acepta al macho. La monta natural es el apareamiento directo; la inseminación artificial es llevar semen del macho a la hembra con una técnica, hecha por personal capacitado; la sincronización de celos es usar productos veterinarios para que varias hembras entren en celo en fechas cercanas. El control del estado gestacional es confirmar con el veterinario si una hembra está preñada.",
        "Estas técnicas tienen riesgos. Las hembras en celo y los machos reproductores pueden golpear o embestir. El nitrógeno líquido causa quemaduras por frío. Los productos hormonales deben usarse solo con receta del veterinario y pueden dañar a personas, en especial a embarazadas. Las agujas pueden cortar o pinchar. Y los fluidos de los animales pueden transmitir zoonosis. La jerarquía de controles ordena las medidas, desde eliminar hasta el EPP.",
        f"Este cuaderno es una simulación en papel: no enseña a realizar estas técnicas. Las hace personal capacitado y autorizado, con receta veterinaria y bajo la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("reproducción animal", "conjunto de acciones para que las hembras queden preñadas y tengan crías"), ("celo", "período en que la hembra acepta al macho"), ("monta natural", "apareamiento directo entre el macho y la hembra"), ("inseminación artificial", "llevar semen del macho a la hembra con una técnica, hecha por personal capacitado"), ("sincronización de celos", "uso de productos veterinarios para que varias hembras entren en celo en fechas cercanas"), ("gestación", "tiempo que dura la preñez"), ("nitrógeno líquido", "líquido extremadamente frío que se usa para guardar semen")],
    worked=[
        ("Distinguir técnicas", "En un plantel de ejemplo se lleva semen guardado a la hembra con una técnica especial. ¿Es monta natural o inseminación artificial?", ["No hay contacto directo entre macho y hembra.", "Es inseminación artificial."], "Inseminación artificial"),
        ("Clasificar un control", "Un plantel de ejemplo instala una puerta con cierre en la sala donde se guardan los productos de uso veterinario. ¿Qué tipo de control es?", ["La puerta con cierre cambia físicamente el acceso.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que un producto hormonal se puede aplicar sin receta si es poco.", "Los productos veterinarios exigen receta y personal autorizado.", "Solo el veterinario los indica."),
              ("Creer que el nitrógeno líquido es seguro porque «es solo frío».", "Causa quemaduras graves por frío.", "Solo lo maneja personal capacitado con equipos.")],
    T=[
        ("abc", "En la reproducción animal: ¿qué es el celo?", "El período en que la hembra acepta al macho", "El período en que la hembra amamanta", "El período del parto", "El celo es la aceptación del macho."),
        ("abc", "En la reproducción animal: ¿qué es la inseminación artificial?", "Llevar semen del macho a la hembra con una técnica, hecha por personal capacitado", "El apareamiento directo entre macho y hembra", "El uso de productos para sincronizar celos", "La inseminación artificial no es apareamiento directo."),
        ("abc", "En la reproducción animal: ¿qué es la sincronización de celos?", "Usar productos veterinarios para que varias hembras entren en celo en fechas cercanas", "Contar los celos de una hembra", "Guardar semen", "La sincronización agrupa celos en fechas cercanas."),
        ("=", "{F} Si en el programa del año quedan preñadas 80 de las 100 vacas, ¿cuántas vacas no quedan preñadas?", "100-80", "Se resta al total las vacas preñadas.", " vacas"),
        ("abc", "{F} Guardar el nitrógeno líquido en un lugar ventilado y con llave es un control de tipo:", "De ingeniería, porque cambia el lugar y el acceso", "Administrativo, porque es una regla", "De EPP, porque protege a quien trabaja", "El lugar y la llave limitan el acceso y funcionan siempre."),
        ("abc", "{F} Una regla que dice «solo el veterinario indica los productos hormonales» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el producto", "De sustitución, porque cambia al veterinario", "Una regla escrita es un control de tipo administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al nitrógeno líquido?", "Que cause quemaduras graves por frío", "El recipiente mismo", "Que el semen no se guarde", "El riesgo es la posibilidad de daño; el líquido extremadamente frío es el peligro."),
        ("abc", "{F} Una estudiante dice: «ya aprendí cómo se insemina, así que lo hago yo con una vaca del plantel». ¿Qué respuesta es correcta?", "Es peligroso: la inseminación la hace personal capacitado y autorizado", "Es correcto, si lleva guantes", "Es correcto, si la vaca es dócil", "Una vaca dócil igual puede reaccionar; la técnica exige formación."),
        ("abc", "{F} En una visita, un toro reproductor embiste a una persona. ¿Qué corresponde según las reglas generales?", "No acercarte al animal ni a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a distraer al toro", "Tirar de la persona hacia ti", "Un animal agresivo es impredecible; se avisa a quienes pueden actuar."),
        ("abc", "En la reproducción animal: ¿por qué los productos hormonales exigen receta del veterinario?", "Porque pueden dañar a animales y personas si se usan mal", "Porque son caros", "Porque no se pueden guardar", "El mal uso de hormonas causa daños."),
        ("abc", "{F} Se propone solo entregar guantes por el riesgo de zoonosis. ¿Qué medida es más efectiva?", "Cumplir el plan sanitario y la higiene, y evitar el contacto con fluidos", "Entregar guantes más gruesos", "Pedir mayor cuidado", "Reducir el contacto y cumplir el plan actúa sobre el peligro."),
        ("=", "{F} Un recipiente de ejemplo guarda 24 pajuelas (tubitos con semen). Si se usan 6 por semana, ¿para cuántas semanas alcanza?", "24//6", "Se divide el total de pajuelas entre las que se usan por semana.", " semanas"),
        ("abc", "En la reproducción animal: ¿por qué conviene que el veterinario confirme la gestación?", "Porque puede diagnosticar con certeza si la hembra está preñada", "Porque la gestación no se puede medir", "Porque reemplaza al encargado", "El veterinario evalúa el estado gestacional."),
    ],
    ctx=("abc", "Un conocido te pide que le inyectes un producto a una vaca para «adelantar el celo». ¿Qué respondes?", "Que no, porque exige receta y personal autorizado, y que lo consultarás con un adulto responsable", "Que sí, si es una dosis pequeña", "Que sí, con guantes", "Los productos veterinarios exigen receta y personal autorizado."),
    sc=[
        ("En la reproducción animal: ¿qué es la monta natural?", "El apareamiento directo entre macho y hembra", "La monta no usa técnicas de laboratorio."),
        ("En el programa reproductivo: ¿quién indica los productos hormonales?", "El médico veterinario", "Los productos veterinarios exigen receta del médico veterinario."),
        ("En la reproducción animal: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
    ],
    op=("El «Plantel Demo 2» anota una tarea de ejemplo: sacar semen de un recipiente de nitrógeno líquido, sin guantes aislantes, en una bodega cerrada y sin ventilación. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a alguien con una quemadura grave por frío.",
        "(a) Peligro: nitrógeno líquido extremadamente frío en un lugar cerrado; riesgo: quemaduras por frío y falta de aire. (b) Una regla de que solo personal capacitado lo manipule. (c) Un lugar ventilado y con llave para guardarlo. (d) No me acerco a tocar, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "avisa a un adulto responsable"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer tocar el líquido", "no avisar"],
        "Pregunta: «¿qué control cambia el lugar y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Une cada término con su definición: celo, monta natural, inseminación artificial, gestación.",
    extend="Explica con un ejemplo por qué un producto hormonal no puede usarse sin receta.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 2 (datos y registro de ejemplo, inventados). Vacas lecheras del «Plantel Demo». Duración del ciclo del celo de ejemplo: 21 días. Duración de la gestación de ejemplo: 280 días. "
     "Registro reproductivo de la vaca V-12: celo observado el día 60 del año; servicio (inseminación) el día 60; diagnóstico de gestación por el veterinario el día 120. "
     "Documentos: el registro reproductivo individual, el calendario reproductivo y la ficha del semen (macho de origen y lote). Roles: encargado reproductivo, inseminador autorizado y médico veterinario.")
build(
    O3, 2, F,
    use="Aprenderé los conceptos de ciclo del celo, servicio, gestación y parto, cómo se leen los registros reproductivos y qué rol cumple cada persona.",
    prior=["Sé qué son el celo y la inseminación artificial.", "Sé sumar y restar enteros.", "Sé leer una ficha de datos."],
    explain=[
        "El ciclo del celo es el tiempo entre un celo y el siguiente, y se repite si la hembra no queda preñada. El servicio es el momento en que se insemina o se hace la monta. La gestación es el tiempo que dura la preñez, hasta el parto. Para saber cuándo se espera el siguiente celo se suma la duración del ciclo a la fecha del celo; para saber cuándo se espera el parto se suma la duración de la gestación a la fecha del servicio.",
        "Los registros dan trazabilidad: el registro reproductivo individual anota las fechas de celo, servicio, diagnóstico y parto de cada hembra; el calendario reproductivo muestra qué esperar cada mes; la ficha del semen dice el macho de origen y el lote. El encargado reproductivo lleva los registros, el inseminador autorizado realiza la técnica y el veterinario hace los diagnósticos.",
        f"Para contar fechas se usa el número del día del año, de 1 a 365; si una suma pasa de 365, la diferencia es el día del año siguiente. {EMER} {AVISO}",
    ],
    vocab=[("ciclo del celo", "tiempo entre un celo y el siguiente"), ("servicio", "momento en que se insemina o se hace la monta"), ("parto", "nacimiento de la cría"), ("registro reproductivo", "documento con las fechas reproductivas de cada hembra"), ("calendario reproductivo", "documento que muestra qué esperar cada mes"), ("pajuela", "tubito pequeño donde se guarda una dosis de semen")],
    worked=[
        ("Próximo celo", "Una vaca de ejemplo tuvo celo el día 50 y su ciclo dura 20 días. ¿Cuándo se espera el siguiente celo si no queda preñada?", ["Se suma la duración del ciclo.", "50 más 20."], "El día 70"),
        ("Fecha de parto", "Un servicio de ejemplo se hizo el día 30 con una gestación de 200 días. ¿Cuándo se espera el parto?", ["Se suma la gestación al servicio.", "30 más 200."], "El día 230"),
    ],
    mistakes=[("Contar la gestación desde la fecha del celo anterior.", "La gestación se cuenta desde el servicio.", "Se suma la gestación a la fecha del servicio."),
              ("Anotar de memoria una fecha de servicio.", "Un registro con datos dudosos pierde valor.", "Se anota solo lo realizado, con fecha real.")],
    T=[
        ("abc", "En la reproducción animal: ¿qué es el ciclo del celo?", "El tiempo entre un celo y el siguiente", "El tiempo que dura la gestación", "El tiempo entre dos partos", "El ciclo del celo es el intervalo entre celos."),
        ("abc", "En la reproducción animal: ¿qué es el servicio?", "El momento en que se insemina o se hace la monta", "El nacimiento de la cría", "El diagnóstico de gestación", "El servicio es la inseminación o la monta."),
        ("abc", "En la reproducción animal: ¿para qué sirve el calendario reproductivo?", "Para mostrar qué esperar cada mes", "Para registrar el peso de las vacas", "Para guardar el semen", "El calendario muestra las fechas esperadas."),
        ("=", "{F} ¿En qué día del año se espera el siguiente celo de V-12 si no queda preñada?", "60+21", "Se suma la duración del ciclo del celo a la fecha del celo observado.", " (día del año)"),
        ("=", "{F} ¿En qué día del año se espera el parto de V-12, si queda preñada?", "60+280", "Se suma la duración de la gestación a la fecha del servicio.", " (día del año)"),
        ("=", "{F} Otra vaca tuvo su servicio el día 120 del año. La suma con la gestación pasa de 365. ¿Qué día del año siguiente se espera el parto?", "120+280-365", "Se suma la gestación al servicio y se resta 365 para pasar al año siguiente.", " (día del año siguiente)"),
        ("=", "{F} ¿Cuántos días pasaron entre el servicio y el diagnóstico de V-12?", "120-60", "Se resta la fecha del servicio a la fecha del diagnóstico.", " días"),
        ("abc", "{F} ¿Qué documento dice de qué macho viene el semen usado?", "La ficha del semen", "El registro reproductivo individual", "El calendario reproductivo", "La ficha del semen identifica el macho de origen."),
        ("abc", "{F} ¿Qué rol hace los diagnósticos de gestación?", "El médico veterinario", "El inseminador autorizado", "El encargado de la leche", "El veterinario diagnostica el estado de gestación de la hembra."),
        ("abc", "{F} Una compañera dice: «contamos la gestación desde el celo del año pasado». ¿Qué respuesta es correcta?", "Es incorrecto: se cuenta desde la fecha del servicio", "Es correcto, porque ahí partió la vaca", "Es correcto, si hubo celo", "La gestación comienza con el servicio que resultó en preñez."),
        ("abc", "{F} El encargado reproductivo quiere anotar en el registro que el servicio se hizo el día 95, aunque se hizo el día 100, «para que calcen las fechas». ¿Qué corresponde?", "Rechazarlo: se anota la fecha real", "Aceptarlo, si calzan las fechas", "Aceptarlo, si nadie revisa", "Alterar una fecha falsea el registro."),
        ("abc", "{F} Una vaca en celo patea a un ayudante que se acerca por detrás. ¿Qué corresponde a quien lo ve?", "Alejarte de la zona de riesgo y avisar a un adulto responsable", "Acercarte a ayudarlo", "Gritar a la vaca", "Un animal en celo es impredecible; se avisa a quienes pueden actuar."),
        ("abc", "En la reproducción animal: ¿por qué un registro reproductivo completo ayuda a decidir?", "Porque permite ver fechas, intervalos y resultados de cada hembra", "Porque reemplaza al veterinario", "Porque evita las inseminaciones", "Los registros permiten planificar y detectar problemas."),
    ],
    ctx=("abc", "Una conocida te pide que cambies en el registro la fecha de un servicio para que el parto caiga en un mes mejor. ¿Qué respondes?", "Que no, porque se anota la fecha real, y que lo consultarás con un adulto responsable", "Que sí, un día", "Que sí, si el veterinario no lo ve", "Cambiar la fecha falsea el registro."),
    sc=[
        ("En la reproducción animal: ¿cómo se calcula la fecha esperada de parto?", "Fecha del servicio más la duración de la gestación", "La gestación se cuenta desde el servicio."),
        ("En el programa reproductivo: ¿qué rol hace el diagnóstico de gestación?", "El médico veterinario", "El diagnóstico es función del veterinario."),
        ("En la reproducción animal: ¿qué anota el registro reproductivo?", "Las fechas de celo, servicio, diagnóstico y parto", "El registro guarda la historia reproductiva."),
    ],
    op=("Datos de ejemplo del «Plantel Demo 3»: ciclo del celo de 21 días; gestación de 280 días. La vaca V-30 tuvo celo y servicio el día 45 del año. Escribe (a) el día esperado del siguiente celo si no queda preñada, (b) el día esperado del parto (si pasa de 365, resta 365 y escribe el día del año siguiente), (c) en qué documento anotas las fechas de la vaca, (d) quién hace el diagnóstico de gestación.",
        "(a) 45 + 21 = día 66. (b) 45 + 280 = 325; es el día 325 del mismo año. (c) En el registro reproductivo individual. (d) El médico veterinario.",
        ["calcula el siguiente celo", "calcula el parto", "nombra el documento", "nombra al veterinario"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal", "contar la gestación desde otra fecha"],
        "Pregunta: «¿a qué fecha se suma la gestación?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el siguiente celo de una vaca inventada con celo el día 40 y ciclo de 21 días.",
    extend="Explica con un ejemplo por qué las fechas reales son importantes en el registro reproductivo.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Programa reproductivo del «Plantel Demo» en un año. 100 vacas servidas; 60 quedaron preñadas. Meta de ejemplo: 70 preñadas de cada 100 servidas. "
     "Observaciones: en 12 vacas no se registró el celo; el intervalo promedio entre partos fue de 400 días (meta de ejemplo: 365 días); el semen de un lote llegó con el recipiente sin nivel de nitrógeno líquido; las vacas flacas tuvieron menos preñez.")
build(
    O3, 3, F,
    use="Aprenderé a analizar un caso de resultados reproductivos con evidencias, a relacionar las observaciones con posibles causas y a derivar las decisiones al veterinario.",
    prior=["Sé qué son servicio, gestación y registro reproductivo.", "Sé calcular porcentajes enteros.", "Sé comparar un valor con una meta."],
    explain=[
        "Para analizar los resultados se compara el porcentaje de vacas preñadas con la meta. Si es menor, se buscan posibles causas en las observaciones: celos no registrados, que impiden servir a tiempo; semen mal conservado, que pierde calidad; mala alimentación, que reduce la fertilidad; o intervalos largos entre partos, que hacen producir menos crías por año. Las causas son hipótesis hasta que el veterinario las confirma.",
        "Un análisis útil nombra el resultado, la meta, la brecha entre ambos y dos evidencias. La brecha es la diferencia entre la meta y el resultado. Luego se deriva cada hipótesis a quien corresponde: el encargado revisa la detección de celos y los registros; el veterinario evalúa la fertilidad y el semen; el nutricionista revisa la alimentación. Ninguna decisión sobre productos o técnicas se toma sin el veterinario.",
        f"El análisis no incluye aplicar ni indicar productos. {EMER} {AVISO}",
    ],
    vocab=[("tasa de preñez", "porcentaje de hembras servidas que quedan preñadas"), ("brecha", "diferencia entre la meta y el resultado"), ("intervalo entre partos", "días entre un parto y el siguiente"), ("fertilidad", "capacidad de quedar preñada o de preñar"), ("hipótesis", "explicación posible que aún hay que confirmar")],
    worked=[
        ("Tasa de preñez", "En un plantel de ejemplo, 40 de 50 vacas servidas quedan preñadas. ¿Cuál es la tasa de preñez?", ["Se divide 40 entre 50.", "40 de 50 equivale a 80 de 100."], "80 %"),
        ("Brecha", "La meta de ejemplo es 80 % y se logró 65 %. ¿Cuál es la brecha?", ["Se resta el resultado a la meta.", "80 menos 65."], "15 puntos porcentuales"),
    ],
    mistakes=[("Dar por cierta una causa sin confirmación del veterinario.", "Las causas son hipótesis hasta comprobarlas.", "Se deriva y se confirma."),
              ("Culpar solo al semen sin revisar el registro de celos.", "Varias causas pueden sumarse.", "Se listan todas las evidencias.")],
    T=[
        ("abc", "En la reproducción animal: ¿qué es la tasa de preñez?", "El porcentaje de hembras servidas que quedan preñadas", "El número de crías por parto", "La duración de la gestación", "La tasa de preñez relaciona preñadas y servidas."),
        ("abc", "En la reproducción animal: ¿qué es la brecha frente a una meta?", "La diferencia entre la meta y el resultado", "La suma de la meta y el resultado", "El promedio del año", "La brecha mide cuánto falta para llegar a la meta."),
        ("abc", "En la reproducción animal: ¿qué es un intervalo largo entre partos?", "Muchos días entre un parto y el siguiente", "Un parto con muchas crías", "Una gestación corta", "El intervalo largo reduce las crías por año."),
        ("=", "{F} ¿Cuál es la tasa de preñez del programa, en porcentaje?", "60*100//100", "Se divide las vacas preñadas entre las servidas y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es la brecha de la tasa de preñez frente a la meta, en puntos?", "70-60", "Se resta el resultado a la meta.", " puntos"),
        ("=", "{F} ¿Cuántos días más que la meta tuvo el intervalo entre partos?", "400-365", "Se resta la meta al intervalo observado.", " días"),
        ("abc", "{F} ¿Qué evidencia de la ficha puede explicar que se pierdan servicios oportunos?", "En 12 vacas no se registró el celo", "El semen es nuevo", "La meta es de 70 %", "Sin celo registrado no se sabe cuándo servir."),
        ("abc", "{F} ¿Qué evidencia apunta a un problema con el semen?", "El recipiente llegó sin nivel de nitrógeno líquido", "Hay 100 vacas", "El intervalo es de 400 días", "Sin nitrógeno el semen puede perder calidad."),
        ("abc", "{F} ¿A quién se deriva la evaluación de la fertilidad y del semen?", "Al médico veterinario", "Al transportista", "Al comprador de leche", "El veterinario evalúa la fertilidad y el semen."),
        ("abc", "{F} Una estudiante dice: «ya sé la causa, así que les doy un producto hormonal a todas las vacas». ¿Qué respuesta es correcta?", "Es peligroso: los productos los indica el veterinario y los aplica personal autorizado", "Es correcto, si es poco producto", "Es correcto, si las vacas son dóciles", "Las causas son hipótesis y los productos exigen receta."),
        ("abc", "{F} El encargado quiere anotar que los 12 celos faltantes sí se registraron, para mejorar el registro. ¿Qué corresponde?", "Rechazarlo: se informa lo que falta y no se inventan datos", "Aceptarlo, para cumplir la meta", "Aceptarlo, si nadie lo revisa", "Inventar datos falsea el registro y quita su valor."),
        ("abc", "{F} Una vaca flaca cae en el corral y patalea. ¿Qué corresponde a quien lo observa?", "No acercarte, avisar a un adulto responsable y a emergencias", "Intentar levantarla tú", "Sujetarla del cuello", "Un animal caído y asustado es impredecible."),
        ("abc", "En la reproducción animal: ¿por qué una buena alimentación mejora la fertilidad?", "Porque una hembra bien nutrida tiene más posibilidades de quedar preñada", "Porque los alimentos reemplazan al semen", "Porque la gestación se acorta", "La nutrición influye en la fertilidad."),
    ],
    ctx=("abc", "Un conocido te muestra que solo 50 % de sus vacas quedó preñado y te pide que le digas qué hormona usar. ¿Qué respondes?", "Que no puedes indicarla y que debe consultar a un veterinario", "Que use la del vecino", "Que use cualquiera", "Las causas y los productos los define el veterinario."),
    sc=[
        ("En la reproducción animal: ¿cómo se calcula la tasa de preñez?", "Preñadas entre servidas, por 100", "La tasa mide qué porcentaje de servidas queda preñada."),
        ("En el programa reproductivo: ¿qué son las causas antes de la confirmación?", "Hipótesis", "Las causas se confirman con el veterinario."),
        ("En la reproducción animal: ¿qué es la brecha?", "La diferencia entre la meta y el resultado", "La brecha dice cuánto falta para llegar a la meta."),
    ],
    op=("Caso de ejemplo del «Plantel Demo 4»: 80 vacas servidas y 48 preñadas; meta de ejemplo 70 %; en 10 vacas no se registró el celo; el intervalo entre partos fue de 390 días y la meta es 365. Escribe (a) la tasa de preñez, (b) la brecha frente a la meta, (c) dos evidencias que puedan explicar el resultado, (d) a quién derivas las hipótesis.",
        "(a) 48 × 100 ÷ 80 = 60 %. (b) 70 − 60 = 10 puntos. (c) 10 vacas sin celo registrado y un intervalo entre partos 25 días mayor que la meta. (d) Al médico veterinario.",
        ["calcula la tasa", "calcula la brecha", "cita dos evidencias", "deriva al veterinario"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por 100", "dar una causa como cierta", "proponer aplicar un producto"],
        "Pregunta: «¿cuántas preñadas hay entre las servidas?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula la tasa de preñez de 60 vacas servidas con 45 preñadas.",
    extend="Explica con un ejemplo por qué una causa es una hipótesis hasta que la confirma el veterinario.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). El «Plantel Demo» sirve 100 vacas con inseminación artificial. Costo de ejemplo del semen y la técnica: $15.000 por servicio. Quedan preñadas 80 vacas. "
     "Cada vaca preñada produce una cría que se valora en $400.000 (valor de ejemplo). Costo adicional de un servicio sin preñez: se pierde el servicio y 21 días de espera por el siguiente celo.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular la tasa de preñez, el costo por preñez y el valor de las crías de un programa reproductivo.",
    prior=["Sé qué es la tasa de preñez.", "Sé multiplicar y dividir enteros.", "Sé calcular porcentajes enteros."],
    explain=[
        "El costo por preñez es el costo total de los servicios dividido entre las vacas que quedaron preñadas. Si la tasa de preñez es baja, cada preñez cuesta más. El valor de las crías es el número de preñeces por el valor de cada cría. El margen del programa es el valor de las crías menos el costo de los servicios.",
        "Con estos cálculos se compara, por ejemplo, un programa con 80 preñadas contra uno con 60 preñadas. Pero el cálculo no reemplaza el criterio del veterinario: una tasa baja puede deberse a causas que no se arreglan gastando más. Los valores son de ejemplo y las decisiones las toma el veterinario con el encargado.",
        f"Nunca se ahorra en bienestar animal ni en seguridad de las personas. {EMER} {AVISO}",
    ],
    vocab=[("costo por preñez", "costo total de los servicios entre las vacas preñadas"), ("valor de las crías", "preñeces por el valor de cada cría"), ("margen del programa", "valor de las crías menos el costo de los servicios"), ("servicio", "inseminación o monta de una hembra"), ("programa reproductivo", "plan de servicios de un año")],
    worked=[
        ("Costo por preñez", "Un programa de ejemplo cuesta $600.000 y logra 20 preñeces. ¿Cuál es el costo por preñez?", ["Se divide el costo entre las preñeces.", "600.000 entre 20."], "$30.000"),
        ("Margen", "Esas 20 crías valen $100.000 cada una. ¿Cuál es el margen del programa?", ["Valor de las crías: 20 por 100.000.", "2.000.000 menos 600.000."], "$1.400.000"),
    ],
    mistakes=[("Calcular el costo por preñez dividiendo entre las vacas servidas.", "Debe dividirse entre las preñadas.", "El divisor son las vacas que quedaron preñadas."),
              ("Creer que gastar más en servicios siempre sube la tasa de preñez.", "Las causas de una tasa baja pueden ser otras.", "El veterinario evalúa las causas.")],
    T=[
        ("abc", "En la reproducción animal: ¿qué es el costo por preñez?", "El costo total de los servicios entre las vacas preñadas", "El costo de una sola inseminación", "El costo del semen por pajuela", "El costo por preñez reparte el costo entre las preñeces logradas."),
        ("abc", "En la reproducción animal: ¿qué es el margen de un programa reproductivo?", "El valor de las crías menos el costo de los servicios", "El costo de los servicios más el valor de las crías", "El número de vacas servidas", "El margen resta los costos del valor."),
        ("abc", "En la reproducción animal: ¿por qué una tasa de preñez baja aumenta el costo por preñez?", "Porque el mismo costo se reparte entre menos preñeces", "Porque el semen cuesta más", "Porque la gestación dura más", "Con menos preñeces, cada una cuesta más."),
        ("=", "{F} ¿Cuál es el costo total de los servicios?", "100*15000", "Se multiplican las vacas servidas por el costo de cada servicio.", " pesos"),
        ("=", "{F} ¿Cuál es la tasa de preñez del programa, en porcentaje?", "80*100//100", "Se dividen las preñadas entre las servidas y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es el costo por preñez?", "100*15000//80", "Se divide el costo total entre las vacas preñadas.", " pesos"),
        ("=", "{F} ¿Cuál es el valor de las crías esperadas?", "80*400000", "Se multiplican las preñeces por el valor de cada cría.", " pesos"),
        ("=", "{F} ¿Cuál es el margen del programa?", "80*400000-100*15000", "Se resta el costo de los servicios al valor de las crías.", " pesos"),
        ("=", "{F} Si solo quedaran preñadas 60 vacas, ¿cuál sería el costo por preñez?", "100*15000//60", "Se divide el mismo costo entre las 60 vacas preñadas.", " pesos"),
        ("abc", "{F} Un jefe propone repetir el servicio a todas las vacas sin esperar el diagnóstico del veterinario para ahorrar tiempo. ¿Qué corresponde?", "Rechazarlo: el diagnóstico lo hace el veterinario antes de decidir", "Aceptarlo, para ganar tiempo", "Aceptarlo, si hay semen", "Sin diagnóstico se pierden recursos y se afecta el bienestar."),
        ("abc", "{F} Una estudiante quiere ayudar con la inseminación porque entendió los cálculos. ¿Qué corresponde?", "Rechazarlo: la técnica la hace personal capacitado y autorizado", "Aceptarlo, si está supervisada", "Aceptarlo, si usa guantes", "Calcular costos no habilita para realizar la técnica."),
        ("abc", "En la reproducción animal: ¿por qué conviene ver el costo por preñez y no solo el costo total?", "Porque muestra cuánto cuesta cada resultado logrado", "Porque el costo total no existe", "Porque oculta los gastos", "El costo por preñez relaciona el gasto con el resultado."),
        ("abc", "{F} Si el costo por preñez sube de un año a otro, ¿qué corresponde hacer?", "Revisar las causas con el veterinario", "Aumentar los servicios sin revisar", "Eliminar el registro", "Un aumento de costo requiere revisar las causas."),
    ],
    ctx=("abc", "Un conocido te pregunta si le conviene usar inseminación artificial y te da solo el costo del semen. ¿Qué respondes?", "Que faltan la tasa de preñez esperada y el valor de las crías, y que decide con un veterinario", "Que sí, siempre", "Que no, nunca", "Sin tasa ni valor no se puede comparar."),
    sc=[
        ("En la reproducción animal: ¿cómo se calcula el costo por preñez?", "Costo de los servicios entre vacas preñadas", "Se divide el costo por los resultados logrados."),
        ("En el programa reproductivo: ¿cómo se calcula el margen?", "Valor de las crías menos costo de los servicios", "El margen es lo que queda tras pagar los costos."),
        ("En la reproducción animal: ¿qué pasa con el costo por preñez si hay menos preñadas?", "Sube", "Menos preñeces repartirían el mismo costo."),
    ],
    op=("Datos de ejemplo del «Plantel Demo 5»: 50 vacas servidas a $20.000 por servicio; quedan preñadas 40; cada cría vale $300.000. Escribe (a) el costo total, (b) la tasa de preñez, (c) el costo por preñez, (d) el margen del programa.",
        "(a) 50 × 20.000 = $1.000.000. (b) 40 × 100 ÷ 50 = 80 %. (c) 1.000.000 ÷ 40 = $25.000. (d) 40 × 300.000 − 1.000.000 = $11.000.000.",
        ["calcula el costo total", "calcula la tasa", "calcula el costo por preñez", "calcula el margen"],
        ["hoja con las cuatro respuestas"],
        ["dividir entre las servidas", "no restar el costo"],
        "Pregunta: «¿entre cuántas vacas divides el costo para el costo por preñez?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el costo por preñez de un programa inventado de $900.000 con 30 preñeces.",
    extend="Explica con un ejemplo por qué ahorrar en servicios puede salir más caro.",
)

# ============================================================ OAM-03, clase 5
F = ("Ficha 5 (comparación y control de ejemplo, inventada). El «Plantel Demo» compara tres alternativas reproductivas con puntajes de ejemplo de 1 a 5 (5 es lo mejor). "
     "Monta natural: costo 4, mejora genética 2, riesgo para las personas 1 (el macho es peligroso), trabajo 5. Inseminación artificial: costo 3, mejora genética 5, riesgo para las personas 4, trabajo 3. Inseminación con sincronización de celos: costo 2, mejora genética 5, riesgo para las personas 3, trabajo 4. "
     "Control del registro reproductivo: se revisaron 10 puntos de ejemplo (fecha del celo, fecha del servicio, macho o semen, responsable, diagnóstico, fecha del parto, cría, identificación, firma y observaciones) y 8 estaban completos.")
build(
    O3, 5, F,
    use="Aprenderé a comparar alternativas reproductivas con una matriz de puntajes, a mirar el riesgo para las personas y a verificar la calidad de un registro reproductivo.",
    prior=["Sé sumar puntajes y calcular porcentajes.", "Sé qué son las técnicas de reproducción.", "Sé qué es un registro reproductivo."],
    explain=[
        "Para comparar alternativas se usa una matriz con criterios como costo, mejora genética, riesgo para las personas y trabajo requerido. Cada alternativa recibe un puntaje por criterio y se suman los puntajes. Gana la de mayor total, pero el criterio del riesgo para las personas se mira aparte: una alternativa con riesgo muy alto solo se elige si hay personal capacitado y medidas de control. Cuanto más alto el puntaje de riesgo, más seguro es.",
        "La calidad de un registro se verifica con una lista de puntos que se marcan completos o incompletos. El porcentaje de cumplimiento es los completos entre el total, por 100. Los puntos incompletos se informan y los completa quien tiene el dato real; no se inventan. La decisión de qué técnica usar la toma el veterinario con el encargado, según la especie, los objetivos de producción y los procedimientos establecidos.",
        f"Esta comparación es un ejercicio en papel y no habilita para realizar ninguna técnica. {EMER} {AVISO}",
    ],
    vocab=[("mejora genética", "mejoramiento de las características de las crías por elegir mejores padres"), ("matriz de comparación", "tabla con criterios y puntajes para comparar alternativas"), ("criterio crítico", "criterio que no puede quedar muy bajo"), ("cumplimiento", "porcentaje de puntos completos de una lista"), ("puntaje", "número que mide qué tan bien cumple una alternativa un criterio")],
    worked=[
        ("Sumar puntajes", "Una alternativa de ejemplo obtiene 3 en costo, 4 en mejora genética y 2 en riesgo. ¿Cuál es su total?", ["Se suman los tres puntajes.", "3 más 4 más 2."], "9 puntos"),
        ("Cumplimiento", "En un registro de ejemplo se revisaron 5 puntos y 4 estaban completos. ¿Cuál es el cumplimiento?", ["4 de 5 equivale a 80 de 100.", "80 %."], "80 %"),
    ],
    mistakes=[("Elegir la alternativa de menor costo sin mirar el riesgo para las personas.", "El riesgo para las personas es un criterio crítico.", "Se revisa el riesgo aparte."),
              ("Marcar completo un punto dudoso del registro.", "Se falsea el registro.", "Se informa y lo completa quien tiene el dato real.")],
    T=[
        ("abc", "En la reproducción animal: ¿qué es la mejora genética?", "El mejoramiento de las crías por elegir mejores padres", "El aumento del peso de la madre", "La duración de la gestación", "La mejora genética busca mejores características en las crías."),
        ("abc", "En la reproducción animal: ¿qué es un criterio crítico en una matriz?", "Un criterio que no puede quedar muy bajo", "El criterio con menos puntaje", "El criterio más barato", "El crítico es el que no puede fallar."),
        ("abc", "En la reproducción animal: ¿qué se hace con un punto incompleto del registro?", "Se informa y lo completa quien tiene el dato real", "Se inventa un dato parecido", "Se borra la línea", "Los registros se completan con datos reales."),
        ("=", "{F} ¿Cuál es el total de puntaje de la monta natural?", "4+2+1+5", "Se suman sus puntajes de costo, mejora genética, riesgo y trabajo.", " puntos"),
        ("=", "{F} ¿Cuál es el total de puntaje de la inseminación artificial?", "3+5+4+3", "Se suman sus puntajes de costo, mejora genética, riesgo y trabajo.", " puntos"),
        ("=", "{F} ¿Cuál es el total de puntaje de la inseminación con sincronización?", "2+5+3+4", "Se suman sus puntajes de costo, mejora genética, riesgo y trabajo.", " puntos"),
        ("abc", "{F} ¿Qué alternativa tiene el mayor total?", "Inseminación artificial, con 15 puntos", "Monta natural, con 12 puntos", "Inseminación con sincronización, con 14 puntos", "La inseminación artificial suma 15, más que las otras dos."),
        ("abc", "{F} ¿Qué alternativa tiene el menor puntaje en riesgo para las personas?", "Monta natural, porque el macho es peligroso", "Inseminación artificial", "Inseminación con sincronización", "La monta natural tiene puntaje 1 en riesgo."),
        ("=", "{F} ¿Qué porcentaje del registro reproductivo estaba completo?", "8*100//10", "Se dividen los puntos completos entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} Una compañera dice: «la monta natural tiene el mayor puntaje de trabajo, así que es la mejor». ¿Qué respuesta es correcta?", "Es incompleto: se suman todos los criterios y el riesgo para las personas es crítico", "Es correcto, porque el trabajo es lo único que importa", "Es correcto, si el macho es dócil", "Se compara con todos los criterios."),
        ("abc", "{F} El encargado marca como completos los 2 puntos faltantes del registro para llegar a 100 %. ¿Qué corresponde?", "Rechazarlo: se informa lo que falta y se completa con datos reales", "Aceptarlo, para mejorar el registro", "Aceptarlo, si nadie lo revisa", "Marcar completo lo que no lo está falsea el registro."),
        ("abc", "{F} Una estudiante quiere entrar al corral del macho para observar si está en celo. ¿Qué corresponde?", "Rechazarlo: un macho reproductor puede ser peligroso y el acceso es de personal capacitado", "Aceptarlo, si no se acerca", "Aceptarlo, si lleva casco", "Los machos reproductores son impredecibles y pueden embestir."),
        ("abc", "En la reproducción animal: ¿por qué la decisión de la técnica la toma el veterinario con el encargado?", "Porque conocen la especie, los objetivos y los procedimientos establecidos", "Porque los estudiantes no pueden decidir nada", "Porque la matriz no sirve", "El veterinario conoce los criterios técnicos del caso."),
    ],
    ctx=("abc", "Un conocido te pide que elijas, solo por el puntaje, una técnica reproductiva para sus animales y la apliques mañana. ¿Qué respondes?", "Que el puntaje ayuda a analizar, pero decide el veterinario y aplica personal autorizado", "Que aplique la de mayor puntaje sin más consulta", "Que aplique la más barata", "La matriz ordena el análisis, pero no reemplaza al veterinario ni habilita para aplicar."),
    sc=[
        ("En la reproducción animal: ¿cómo se calcula el total de una alternativa?", "Sumando sus puntajes", "El total suma los puntajes de cada criterio."),
        ("En el programa reproductivo: ¿qué criterio se mira aparte?", "El riesgo para las personas", "El riesgo para las personas es un criterio crítico."),
        ("En la reproducción animal: ¿cómo se calcula el cumplimiento de un registro?", "Puntos completos entre el total, por 100", "El cumplimiento es un porcentaje de la lista."),
    ],
    op=("Puntajes de ejemplo del «Plantel Demo 6» (1 a 5, 5 es lo mejor): alternativa P (costo 4, mejora genética 3, riesgo 2, trabajo 4); alternativa Q (costo 2, mejora genética 5, riesgo 4, trabajo 3). El registro revisó 8 puntos y 6 estaban completos. Escribe (a) el total de P y de Q, (b) cuál tiene mayor total, (c) cuál es más segura para las personas, (d) el cumplimiento del registro.",
        "(a) P: 4 + 3 + 2 + 4 = 13; Q: 2 + 5 + 4 + 3 = 14. (b) Q. (c) Q, con riesgo 4. (d) 6 × 100 ÷ 8 = 75 %.",
        ["suma bien los totales", "elige el mayor", "elige la más segura", "calcula el cumplimiento"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal", "ignorar el riesgo", "marcar incompletos como completos"],
        "Pregunta: «¿qué número es el riesgo de cada alternativa?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Crea una matriz con dos alternativas y cuatro criterios inventados, suma los totales y elige una.",
    extend="Explica con un ejemplo por qué el riesgo para las personas debe revisarse aparte del total.",
)
