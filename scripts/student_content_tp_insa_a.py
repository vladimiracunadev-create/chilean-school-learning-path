"""Instalaciones Sanitarias TP 3.º y 4.º medio: OAE-01 (leer y utilizar planos de redes de gas, agua y evacuación) y OAE-02 (cubicar). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_insa_common import AVISO, EMER, build

O1 = "TP-INSA-3y4-OAE-01"
O2 = "TP-INSA-3y4-OAE-02"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La constructora ficticia «Obras del Sur» entrega a un taller sanitario de ejemplo la carpeta de un edificio de 3 pisos: "
     "planos de gas (1 lámina), de agua potable (2 láminas) y de evacuación de aguas servidas y lluvias (2 láminas), una memoria de cálculo y unas especificaciones técnicas de 12 páginas. "
     "Riesgos anotados en la carpeta: posible olor a gas, excavaciones, cámaras de inspección y contacto con aguas servidas.")
build(
    O1, 1, F,
    use="Aprenderé qué redes forman un proyecto sanitario, qué documentos trae una carpeta de planos, qué institución vigila el gas y qué riesgos hay que reconocer antes de leer un plano.",
    prior=["Sé leer una tabla y un dibujo simple.", "Sé sumar y multiplicar números pequeños.", "Sé que una obra se hace según documentos escritos."],
    explain=[
        "Un proyecto sanitario reúne tres redes. La red de agua potable trae agua limpia hasta los artefactos. La red de evacuación retira fuera del edificio las aguas servidas y las aguas lluvias. La red de gas lleva combustible gaseoso hasta las cocinas y otros artefactos. Cada red tiene su propio plano: un dibujo técnico a escala, dividido en láminas, que muestra dónde y cómo va la instalación. La carpeta del proyecto suma la memoria de cálculo, que justifica con cuentas las dimensiones, y las especificaciones técnicas, que fijan materiales y calidades.",
        "Leer bien los planos es una forma de prevenir accidentes. En Chile, la Superintendencia de Electricidad y Combustibles (SEC) fiscaliza la seguridad de las instalaciones de gas. Los riesgos del oficio son fugas de gas (incendio, explosión e intoxicación), caídas y atrapamientos en zanjas y cámaras, y el riesgo biológico de las aguas servidas, que pueden transmitir enfermedades. Si un símbolo del plano no está en la leyenda, o dos documentos se contradicen, no se supone: se consulta a quien diseñó. Al terminar la lectura se deja un registro con la fecha, quién leyó y las dudas encontradas.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("red de agua potable", "tuberías que traen agua limpia hasta los artefactos"), ("red de evacuación", "tuberías y obras que retiran del edificio las aguas servidas y lluvias"), ("red de gas", "tuberías que llevan combustible gaseoso hasta los artefactos"), ("plano", "dibujo técnico a escala que muestra dónde y cómo va una instalación"), ("lámina", "hoja de un plano"), ("memoria de cálculo", "documento que justifica con cuentas las dimensiones del proyecto"), ("especificaciones técnicas", "documento que fija los materiales y las calidades del proyecto"), ("SEC", "Superintendencia de Electricidad y Combustibles, que fiscaliza la seguridad de las instalaciones de gas"), ("riesgo biológico", "posibilidad de contagio por microbios presentes en las aguas servidas")],
    worked=[
        ("Reconocer la red", "Un plano de ejemplo dibuja tuberías que llevan combustible gaseoso hasta una cocina. ¿A qué red pertenece?", ["La red que lleva combustible gaseoso es la red de gas.", "No es de agua potable ni de evacuación."], "A la red de gas"),
        ("Láminas pendientes", "Otra carpeta de ejemplo trae 4 láminas de agua, 3 de evacuación y 1 de gas. Ya se leyeron 5 láminas. ¿Cuántas faltan?", ["Se suman todas: 4 + 3 + 1 = 8 láminas.", "Se resta lo leído: 8 menos 5 son 3."], "Faltan 3 láminas"),
    ],
    mistakes=[("Suponer el significado de un símbolo que no está en la leyenda.", "Un símbolo parecido puede significar otra cosa y llevar a un error de obra.", "Consulta al proyectista o a la jefatura y anota la duda."),
              ("Creer que saber leer un plano de gas habilita para intervenir una red de gas.", "Esa tarea exige instalador autorizado y norma vigente de la SEC.", "Aprende aquí los conceptos y deja la intervención a personal autorizado.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es una red de evacuación?", "Tuberías y obras que retiran fuera del edificio las aguas servidas y lluvias", "Tuberías que traen el agua potable hasta los artefactos", "Tuberías que llevan combustible gaseoso hasta las cocinas", "La evacuación retira aguas usadas; el agua potable y el gas son redes de abastecimiento."),
        ("abc", "En Instalaciones Sanitarias: ¿para qué sirve la memoria de cálculo de un proyecto?", "Para justificar con cuentas las dimensiones del proyecto", "Para dibujar a escala cada tubería", "Para fijar la fecha en que se entrega la obra", "La memoria explica con cálculos por qué el proyecto tiene esas dimensiones; el dibujo está en los planos."),
        ("abc", "¿Qué institución fiscaliza la seguridad de las instalaciones de gas en Chile?", "La Superintendencia de Electricidad y Combustibles (SEC)", "La Dirección del Trabajo", "El Servicio de Impuestos Internos", "La SEC fiscaliza la seguridad del gas; las otras instituciones tienen funciones laborales y tributarias."),
        ("=", "{F} ¿Cuántas láminas de planos entrega la constructora en total, sumando gas, agua y evacuación?", "1+2+2", "Se suman las láminas de las tres redes de la ficha.", " láminas"),
        ("abc", "{F} ¿Qué documento de la carpeta fija los materiales y las calidades que exige el proyecto?", "Las especificaciones técnicas", "La memoria de cálculo", "La lámina de gas", "Las especificaciones técnicas describen materiales y calidades; la memoria solo justifica las dimensiones."),
        ("abc", "{F} Entre los riesgos de la ficha, ¿cuál tarea está reservada a personal autorizado?", "Entrar a una cámara de inspección", "Contar las láminas de la carpeta", "Leer las especificaciones técnicas", "Una cámara puede tener gases y riesgo de caída o atrapamiento; leer documentos no tiene ese riesgo."),
        ("=", "El edificio de la ficha tiene 3 pisos y la planta de cada piso muestra 5 artefactos sanitarios de ejemplo. ¿Cuántos artefactos hay en el edificio?", "3*5", "Se multiplica la cantidad de pisos por los artefactos de cada planta.", " artefactos"),
        ("abc", "Un plano de ejemplo trae un símbolo que no aparece en la leyenda. ¿Qué corresponde?", "Consultar al proyectista o a la jefatura antes de suponer su significado", "Suponer que es el símbolo más parecido de otro plano", "Ignorar el símbolo porque no está en la leyenda", "Un símbolo sin leyenda puede significar otra cosa; se aclara con quien diseñó el plano."),
        ("ab", "Una compañera quiere revisar si la red de gas de su casa tiene fugas usando lo aprendido en este cuaderno. ¿Qué corresponde?", "No hacerlo: avisar a un adulto responsable y a una empresa instaladora autorizada", "Hacerlo con cuidado, porque ya sabe leer planos", "Leer un plano no habilita para intervenir una red de gas; eso lo hace personal autorizado por la SEC."),
        ("abc", "Durante una visita a una obra de ejemplo, una persona percibe olor a gas en un recinto cerrado. ¿Qué corresponde según las reglas generales?", "No entrar ni accionar interruptores o llamas, avisar a un adulto responsable y a emergencias", "Entrar rápido a buscar el origen del olor", "Esperar unos minutos dentro del recinto a ver si desaparece", "Entrar o encender algo puede causar intoxicación o explosión; se avisa a quienes pueden intervenir."),
        ("abc", "{F} Un compañero dice: «con las láminas de agua ya puedo trabajar en la red de gas». ¿Qué respuesta es correcta?", "Es falso: cada red tiene su plano y su norma, y el gas exige personal autorizado por la SEC", "Es cierto, porque todas las redes sanitarias se instalan igual", "Es cierto, si las láminas están a la misma escala", "Cada red tiene riesgos y reglas propias; el gas requiere instalador autorizado."),
        ("=", "{F} Una copia de una lámina cuesta $1.500 (valor de ejemplo). La constructora pide 2 copias de cada una de las láminas de la ficha. ¿Cuánto cuestan las copias?", "1500*(1+2+2)*2", "Se multiplica el precio por las láminas de la ficha y por las dos copias de cada una.", " pesos"),
        ("abc", "¿Qué debe dejar escrito como mínimo el registro de una lectura de planos?", "La fecha, quién leyó y las dudas o diferencias encontradas", "Solo el nombre del proyecto", "Solo la cantidad de láminas leídas", "Un registro útil deja constancia de cuándo, quién y qué se encontró."),
    ],
    ctx=("abc", "Un familiar de ejemplo te dice: «como estudias sanitarias, suelta la unión del medidor de gas para limpiarla; yo te muestro el plano». ¿Qué respondes?", "Que no, porque intervenir una red de gas exige personal autorizado, y que se llame a una empresa instaladora autorizada", "Que sí, pero solo si el plano está a mano", "Que sí, si el familiar firma que acepta el riesgo", "Un plano o una firma no reemplazan la autorización ni la norma vigente; el gas es de riesgo alto."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué red lleva combustible gaseoso a los artefactos?", "La red de gas", "La red de gas se distingue de las de agua y evacuación."),
        ("¿Qué institución fiscaliza la seguridad de las instalaciones de gas?", "La SEC", "La Superintendencia de Electricidad y Combustibles fiscaliza el gas."),
        ("¿Qué se hace si un símbolo del plano no está en la leyenda?", "Consultar a quien diseñó y anotar la duda", "Suponer el significado puede producir un error de obra."),
    ],
    op=("La constructora de ejemplo «Obras del Sur» entrega la carpeta de una casa: 1 lámina de gas, 1 de agua potable y 2 de evacuación, más unas especificaciones técnicas de 8 páginas. Escribe (a) cuántas láminas hay, (b) qué documento mirarías para saber qué materiales se exigen, (c) una tarea riesgosa de la obra que no te corresponde y quién la haría.",
        "(a) 1 + 1 + 2 = 4 láminas. (b) Las especificaciones técnicas. (c) Entrar a una cámara de inspección o intervenir la red de gas: lo hace personal autorizado, con norma vigente y protección.",
        ["suma bien las láminas", "nombra el documento correcto", "reconoce una tarea riesgosa y a quién corresponde"],
        ["hoja con las tres respuestas"],
        ["decir que ya puede intervenir una red de gas", "sumar mal las láminas", "no indicar quién hace la tarea riesgosa"],
        "Pregunta: «¿qué haces si el plano y las especificaciones se contradicen?». Si no responde, pídele que relea la regla de consultar y registrar."),
    reinforce="Escribe una lista con las tres redes de un proyecto sanitario y, junto a cada una, una frase sobre qué lleva o retira.",
    extend="Explica con un ejemplo inventado por qué anotar las dudas en un registro de lectura protege a la obra y al equipo.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (lámina descrita por escrito, de ejemplo, inventada). Lámina A-02 «Agua potable, piso 2», escala 1:50, revisión B. Proyecto «Edificio Los Aromos» (ficticio). "
     "Leyenda de ejemplo: AF = tubería de agua fría; AC = tubería de agua caliente; MD = medidor; VP = válvula de paso; CI = cámara de inspección. "
     "Tramos medidos con regla en la lámina: T1 (AF) mide 12 cm; T2 (AC) mide 7 cm; T3 (AF) mide 9 cm. La cota escrita junto a T2 dice 350 cm.")
build(
    O1, 2, F,
    use="Aprenderé a leer el rótulo, la leyenda y la escala de una lámina, a pasar medidas del plano a la realidad y qué función cumple cada persona que usa los planos.",
    prior=["Sé qué es un plano y qué son las redes de una obra.", "Sé multiplicar por 10, 20, 25 o 50.", "Sé que 100 cm son 1 m."],
    explain=[
        "Cada lámina trae un rótulo: un recuadro con el nombre del proyecto, el título de la lámina, la escala, la fecha y la letra de revisión. La revisión indica la versión del plano; se trabaja con la última que esté vigente. La leyenda explica los símbolos y las siglas, que forman la simbología y la nomenclatura del plano. La planta es la vista del edificio desde arriba; el corte muestra una rebanada vertical. Las cotas son medidas escritas sobre el dibujo.",
        "La escala es la razón entre la medida del dibujo y la real. A escala 1:50, 1 cm de la lámina equivale a 50 cm reales, así que 3 cm de la lámina son 150 cm. Regla importante: lo que está acotado no se mide con regla; la cota escrita manda sobre la medida tomada en la lámina, y si ambas no coinciden se registra la diferencia y se consulta al proyectista, que es quien diseñó y es el único que emite una nueva revisión.",
        f"Cada rol tiene su función. El proyectista diseña. El inspector técnico de obra (ITO) revisa que la obra cumpla los planos y las especificaciones. El jefe de obra organiza el trabajo. El instalador autorizado ejecuta las tareas que la norma le permite. El prevencionista vela por la seguridad. {EMER} {AVISO}",
    ],
    vocab=[("rótulo", "recuadro del plano con el nombre del proyecto, el título, la escala, la fecha y la revisión"), ("revisión", "versión del plano, indicada con una letra"), ("leyenda", "tabla que explica los símbolos y las siglas del plano"), ("planta", "vista del edificio desde arriba"), ("cota", "medida escrita sobre el dibujo"), ("escala", "razón entre la medida del dibujo y la medida real"), ("proyectista", "persona que diseña el proyecto"), ("ITO", "inspector técnico de obra, que revisa que la obra cumpla los planos y las especificaciones"), ("instalador autorizado", "persona que la entidad fiscalizadora habilita para ejecutar ciertas tareas")],
    worked=[
        ("Pasar a la realidad", "Una lámina de ejemplo está a escala 1:20. Un tramo mide 6 cm en la lámina. ¿Cuánto mide en la realidad?", ["Cada centímetro de la lámina son 20 cm reales.", "6 por 20 son 120 cm."], "120 cm"),
        ("Cota contra regla", "En un plano de ejemplo a escala 1:100, un tramo mide 4 cm con regla y su cota escrita dice 380 cm. ¿Qué se usa?", ["La regla da 4 por 100, es decir 400 cm; no coincide con la cota.", "La cota escrita manda, y se registra la diferencia para consultar al proyectista."], "Se usa la cota de 380 cm y se consulta la diferencia"),
    ],
    mistakes=[("Medir con regla un tramo que ya tiene cota y usar esa medida.", "La regla sobre el papel puede estar deformada o mal impresa.", "Usa la cota escrita y registra cualquier diferencia."),
              ("Trabajar con una lámina de una revisión antigua porque «estaba más a mano».", "Puede tener datos corregidos después.", "Confirma la revisión vigente en el rótulo o con la jefatura.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es el rótulo de una lámina?", "El recuadro con el nombre del proyecto, el título, la escala, la fecha y la revisión", "La tabla que explica cada símbolo del plano", "La medida escrita sobre un tramo", "El rótulo identifica la lámina; la leyenda explica los símbolos y la cota es una medida."),
        ("abc", "En Instalaciones Sanitarias: ¿qué significa una escala 1:50?", "Que 1 cm del dibujo equivale a 50 cm reales", "Que el dibujo es 50 veces más grande que la realidad", "Que la lámina tiene 50 tramos", "En una escala 1:50 el dibujo está reducido: 1 cm dibujado son 50 cm reales."),
        ("abc", "En Instalaciones Sanitarias: ¿para qué sirve la leyenda de un plano?", "Para saber qué significan los símbolos y las siglas", "Para saber cuánto cuesta cada tubería", "Para saber quién firmó el contrato de obra", "La leyenda traduce la simbología y las siglas del plano."),
        ("=", "{F} ¿Cuántos centímetros reales mide el tramo T1?", "12*50", "Se multiplican los centímetros de la lámina por la escala 50.", " cm"),
        ("abc", "{F} ¿Qué significa la sigla AC en la leyenda de la ficha?", "Tubería de agua caliente", "Tubería de agua clorada", "Tubería de alcantarillado común", "La leyenda de la ficha dice AC = tubería de agua caliente."),
        ("abc", "{F} ¿Cuáles tramos de la lámina son de agua fría?", "T1 y T3", "T2 solamente", "T1 y T2", "Los tramos AF son T1 y T3; T2 es AC."),
        ("=", "{F} ¿Cuántos centímetros reales mide el tramo T3?", "9*50", "Se multiplican los centímetros de la lámina por la escala 50.", " cm"),
        ("abc", "Un técnico de ejemplo tiene dos láminas del mismo plano: una con revisión A y otra con revisión C. ¿Qué corresponde?", "Usar la revisión C solo si el rótulo o la jefatura la confirman como vigente", "Usar la A porque es la primera", "Mezclar datos de ambas láminas según convenga", "La letra más avanzada suele ser la versión más nueva, pero se confirma que sea la vigente."),
        ("abc", "¿Quién revisa que la obra cumpla los planos y las especificaciones técnicas?", "El inspector técnico de obra (ITO)", "El proveedor de los materiales", "El cliente, al recibir la factura", "El ITO fiscaliza en obra el cumplimiento del proyecto."),
        ("=", "{F} Si se suman los largos reales de los tres tramos T1, T2 y T3, ¿cuántos centímetros resultan?", "(12+7+9)*50", "Se suman los centímetros de la lámina y se multiplican por la escala.", " cm"),
        ("abc", "Otro plano de ejemplo a escala 1:100 muestra un tramo que mide 7 cm con regla, pero su cota escrita dice 650 cm. ¿Qué corresponde?", "Usar la cota de 650 cm y registrar la diferencia para consultar al proyectista", "Usar los 700 cm de la regla porque es lo que se ve", "Promediar ambos valores y usar el resultado", "La cota escrita manda sobre la regla; la diferencia se registra para aclararla."),
        ("=", "Un tramo de una lámina a escala 1:50 mide 14 cm y otro de una lámina a escala 1:20 mide 5 cm. ¿Cuántos centímetros reales suman ambos tramos?", "14*50+5*20", "Cada tramo se multiplica por la escala de su lámina y luego se suman.", " cm"),
        ("abc", "Un instalador de ejemplo cree que un plano tiene un error. ¿Qué corresponde?", "Avisar al proyectista para que revise y emita una nueva revisión si corresponde", "Corregir el plano a mano y seguir trabajando con su versión", "Esperar a que otra persona lo note", "Solo el proyectista cambia el diseño; quien detecta el error lo informa."),
    ],
    ctx=("abc", "En una reunión de ejemplo, un instalador dice: «el plano está mal, lo hago a mi manera». Como estudiante, ¿qué propones?", "Registrar la duda por escrito y consultar al proyectista y al ITO antes de hacer cambios", "Dejar que lo haga a su manera, porque tiene experiencia", "Cambiar el plano con lápiz para que quede igual a lo que hará", "Los cambios de diseño los aprueba quien diseñó y el ITO deja constancia."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué dato manda si la cota escrita y la regla no coinciden?", "La cota escrita, registrando la diferencia", "La cota prevalece sobre la regla y se consulta la diferencia."),
        ("¿Qué indica la letra de revisión de una lámina?", "La versión del plano", "La revisión señala qué versión es la vigente."),
        ("¿Quién emite una nueva revisión del plano?", "El proyectista", "Solo quien diseñó puede modificar el diseño."),
    ],
    op=("Ficha de ejemplo: lámina A-05 «Evacuación, piso 1», escala 1:25. Leyenda: AS = aguas servidas; CI = cámara de inspección. Tramos medidos en la lámina: E1 (AS) 8 cm; E2 (AS) 5 cm. La cota escrita junto a E2 dice 140 cm. Escribe (a) el largo real de E1, (b) el largo que da la regla en E2, (c) qué usarías para E2 y qué harías con la diferencia.",
        "(a) 8 × 25 = 200 cm. (b) 5 × 25 = 125 cm. (c) Se usa la cota escrita de 140 cm y se registra la diferencia de 15 cm para consultar al proyectista.",
        ["calcula bien E1", "calcula bien con regla E2", "usa la cota y registra la diferencia"],
        ["hoja con los dos cálculos y la decisión"],
        ["usar la medida de la regla en lugar de la cota", "olvidar registrar la diferencia", "multiplicar por una escala equivocada"],
        "Pregunta: «¿quién resuelve la diferencia?». Si no responde, pídele que relea el rol del proyectista."),
    reinforce="Inventa un rótulo de lámina con cinco datos y señala cuál sirve para saber si la versión es la vigente.",
    extend="Explica con un ejemplo por qué una cota escrita es más confiable que una medida tomada con regla sobre el papel.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (tabla de ejemplo, inventada). Lámina del baño de un departamento de ejemplo, escala 1:25. Nomenclatura: TA, TB, TC y TD son tramos de agua fría. "
     "Medida tomada en la lámina (cm) y cota escrita (cm): TA = 8 y 200; TB = 6 y 150; TC = 10 y 300; TD = 4 y 100.")
build(
    O1, 3, F,
    use="Aprenderé a analizar una tabla de tramos, a comparar la medida de la lámina con la cota escrita y a registrar una discrepancia antes de pedir material.",
    prior=["Sé pasar medidas de un plano a la realidad con la escala.", "Sé que la cota escrita manda sobre la regla.", "Sé leer una tabla de varias columnas."],
    explain=[
        "Una tabla de tramos ordena la información de un plano: cada fila es un tramo con su nombre y sus medidas. La nomenclatura es el sistema de nombres; usar siempre el mismo nombre para el mismo tramo evita confundir pedidos, registros y conversaciones. Para verificar un dato se calcula la medida que da la regla multiplicando por la escala y se compara con la cota escrita.",
        "Una discrepancia es una diferencia entre dos datos del mismo documento que deberían coincidir. Cuando aparece, se toma como referencia la cota escrita, se anota la diferencia en un registro, se avisa al proyectista y no se pide material ni se avanza en ese tramo hasta aclararla. Una buena anotación dice el tramo, los dos valores, la diferencia y a quién se consulta; una anotación que solo dice «hay un error» no sirve.",
        f"Los datos de este cuaderno son de ejemplo. En una obra real, medir y verificar en terreno lo hace personal capacitado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("tabla de tramos", "lista que ordena cada tramo con su nombre y sus medidas"), ("nomenclatura", "sistema de nombres de los elementos del plano"), ("discrepancia", "diferencia entre dos datos del mismo documento que deberían coincidir"), ("referencia", "dato que se toma como base para comparar"), ("registro", "anotación escrita con fecha y responsable")],
    worked=[
        ("Calcular y comparar", "En una lámina de ejemplo a escala 1:40, un tramo mide 5 cm y su cota dice 200 cm. ¿Hay discrepancia?", ["La regla da 5 por 40, es decir 200 cm.", "Coincide con la cota: no hay discrepancia."], "No hay discrepancia"),
        ("Medir la diferencia", "En otra lámina de ejemplo a escala 1:10, un tramo mide 9 cm y su cota dice 80 cm. ¿Cuántos centímetros difieren?", ["La regla da 9 por 10, es decir 90 cm.", "La diferencia es 90 menos 80, es decir 10 cm."], "10 cm de diferencia"),
    ],
    mistakes=[("Escribir en el registro solo «hay un error en la lámina».", "No dice dónde está ni quién debe aclararlo.", "Anota el tramo, los dos valores, la diferencia y a quién se consulta."),
              ("Pedir el material de un tramo con discrepancia para no perder tiempo.", "Se puede pedir de más o de menos y perder dinero.", "Espera la aclaración del proyectista antes de pedir.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es una discrepancia en un plano?", "Una diferencia entre dos datos del mismo documento que deberían coincidir", "Un símbolo que no está en la leyenda", "Una lámina que se imprimió doble", "Una discrepancia es un desacuerdo entre datos; un símbolo faltante es otro problema."),
        ("abc", "Si la cota escrita y la medida de la regla no coinciden, ¿qué dato se toma como referencia?", "La cota escrita, registrando la diferencia para consultar al proyectista", "La medida de la regla, porque es más reciente", "El promedio de ambos datos", "La cota escrita manda sobre la regla, pero la diferencia se registra y se consulta."),
        ("abc", "En Instalaciones Sanitarias: ¿para qué sirve usar siempre la misma nomenclatura de tramos?", "Para que todos hablen del mismo tramo y no se confundan pedidos y registros", "Para que el plano ocupe menos páginas", "Para que los tramos cuesten menos", "Un mismo nombre para un mismo tramo evita confusiones entre pedidos y registros."),
        ("=", "{F} ¿Cuántos centímetros reales da la regla para el tramo TA?", "8*25", "Se multiplican los centímetros de la lámina por la escala 25.", " cm"),
        ("abc", "{F} ¿Qué tramo presenta una discrepancia entre la regla y la cota?", "TC", "TA", "TD", "Solo TC da 250 cm con regla y tiene cota de 300 cm; los demás coinciden."),
        ("=", "{F} ¿Cuántos centímetros de diferencia hay entre la cota escrita de TC y lo que da la regla?", "300-10*25", "Se resta lo que da la regla a la cota escrita de TC.", " cm"),
        ("=", "{F} Si se suman las cotas escritas de los cuatro tramos, ¿cuántos centímetros resultan?", "200+150+300+100", "Se suman las cotas de la ficha, que son la referencia.", " cm"),
        ("abc", "{F} ¿Qué corresponde hacer con TC antes de pedir material?", "Registrar la discrepancia y consultar al proyectista", "Pedir el material con el valor de la regla", "Pedir el material con el promedio de los dos valores", "Con una discrepancia abierta no se pide material hasta aclararla."),
        ("=", "En otro baño de ejemplo hay tres tramos de 2 m, 3 m y 4 m. Si el material cuesta $2.500 por metro (valor de ejemplo), ¿cuánto cuesta en total?", "(2+3+4)*2500", "Se suman los metros de los tres tramos y se multiplican por el precio por metro.", " pesos"),
        ("abc", "{F} Un compañero propone usar los 250 cm de la regla para TC «porque la regla no se equivoca». ¿Qué respuesta es correcta?", "No: la cota manda y la diferencia debe aclararla el proyectista", "Sí: la regla es más exacta que lo escrito", "Sí, pero solo si el material sobrante se devuelve", "La decisión no corresponde a quien lee el plano, sino a quien lo diseñó."),
        ("abc", "{F} ¿Por qué es útil que la tabla de la ficha rotule cada tramo con un nombre distinto?", "Porque permite registrar y consultar cada tramo sin confundirlo con otro", "Porque así los tramos se dibujan más rápido", "Porque los nombres cambian la escala del plano", "Un nombre único por tramo permite señalar con precisión dónde está la discrepancia."),
        ("=", "En una lámina de ejemplo a escala 1:20, un tramo mide 15 cm y su cota escrita dice 320 cm. ¿Cuántos centímetros de diferencia hay entre la cota y lo que da la regla?", "320-15*20", "Se resta lo que da la regla a la cota escrita.", " cm"),
        ("abc", "¿Cuál de estas anotaciones de registro está mejor redactada?", "Tramo TC: cota 300 cm y regla 250 cm; diferencia de 50 cm; se consulta al proyectista antes de pedir material", "Tramo TC: hay un error", "Tramo TC: se usa 250 porque sí", "La mejor anotación nombra el tramo, los valores, la diferencia y a quién se consulta."),
    ],
    ctx=("abc", "El jefe de obra de ejemplo te pide el listado de materiales para mañana y el tramo TC aún tiene la discrepancia sin aclarar. ¿Qué haces?", "Entregas el listado sin ese tramo, con una nota que explica la discrepancia y la consulta pendiente", "Incluyes el tramo con el valor que te parezca más probable", "Esperas en silencio hasta que alguien se dé cuenta", "Se informa la pendiente por escrito; así el tramo no se pide con un dato dudoso."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué es una nomenclatura de tramos?", "El sistema de nombres de los tramos del plano", "La nomenclatura identifica cada tramo con un nombre único."),
        ("¿Cómo se calcula lo que da la regla en la realidad?", "Multiplicando los centímetros de la lámina por la escala", "Con escala 1:25, cada centímetro del dibujo son 25 centímetros."),
        ("¿Qué debe decir una buena anotación de discrepancia?", "El tramo, los dos valores, la diferencia y a quién se consulta", "Debe permitir que otra persona entienda y resuelva el problema."),
    ],
    op=("Ficha de ejemplo: baño de una casa, escala 1:20. Tramos de agua fría: TE = 10 cm con cota 200 cm; TF = 7 cm con cota 150 cm; TG = 3 cm con cota 60 cm. Escribe (a) lo que da la regla en cada tramo, (b) qué tramo tiene discrepancia y cuántos centímetros, (c) una anotación de registro bien redactada.",
        "(a) TE: 10 × 20 = 200 cm; TF: 7 × 20 = 140 cm; TG: 3 × 20 = 60 cm. (b) TF: la cota dice 150 y la regla da 140, es decir 10 cm de diferencia. (c) «Tramo TF: cota 150 cm y regla 140 cm; diferencia de 10 cm; se consulta al proyectista antes de pedir material.»",
        ["calcula bien los tres tramos", "identifica TF y su diferencia", "redacta un registro completo"],
        ["hoja con los cálculos, el tramo y la anotación"],
        ["usar la escala equivocada", "marcar un tramo sin discrepancia", "redactar un registro sin la diferencia"],
        "Pregunta: «¿qué falta en tu anotación para que otra persona la resuelva?». Si no responde, pídele que relea el modelo de buena anotación."),
    reinforce="Inventa una tabla de tres tramos con una discrepancia y escribe la anotación de registro.",
    extend="Explica con un ejemplo cómo una discrepancia sin resolver puede costar dinero en una compra de materiales.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (control de verificación de ejemplo, inventado; las medidas las tomó personal autorizado y se entregan escritas). Criterio de ejemplo: un tramo cumple si la diferencia entre la longitud proyectada y la registrada es de 3 cm o menos. "
     "Tramo R1: proyectada 400 cm, registrada 402 cm. Tramo R2: proyectada 250 cm, registrada 255 cm. Tramo R3: proyectada 180 cm, registrada 177 cm. Tramo R4: proyectada 320 cm, registrada 310 cm. "
     "Planilla de pendiente: para un tramo de evacuación de 9 m se usa una pendiente de ejemplo de 2 % (valor de ejemplo, no normativo).")
build(
    O1, 4, F,
    use="Aprenderé a controlar una magnitud comparando el valor del plano con un registro, a decidir si cumple una tolerancia de ejemplo y a calcular un desnivel en una planilla.",
    prior=["Sé restar y comparar números.", "Sé qué es una cota y una discrepancia.", "Sé leer una tabla."],
    explain=[
        "Un control de verificación compara el valor que manda el plano con el valor registrado en obra por personal autorizado. La tolerancia es la diferencia máxima que se acepta; si la diferencia es igual o menor a la tolerancia, el tramo cumple, y si es mayor, se registra como no conformidad: un resultado que no cumple lo pedido. Las magnitudes más comunes son la longitud (en cm o m), el nivel o cota de altura y la pendiente.",
        "La pendiente expresa cuánto baja un tramo por cada metro de largo. En una planilla de papel, el desnivel en centímetros se calcula así: desnivel = longitud en metros × pendiente en porcentaje. Con un tramo de 5 m y una pendiente de ejemplo de 4 %, el desnivel es 20 cm. Los porcentajes y las tolerancias de este cuaderno son de ejemplo para practicar la cuenta; los valores reales los fija el proyecto y la norma vigente.",
        f"Cada tramo se controla por separado: que otros cumplan no compensa uno que no cumple. Ante una no conformidad no se corrige a ojo: se informa a la jefatura o al ITO. {EMER} {AVISO}",
    ],
    vocab=[("control de verificación", "comparación entre el valor del plano y el valor registrado en obra"), ("tolerancia", "diferencia máxima que se acepta entre lo proyectado y lo registrado"), ("no conformidad", "resultado que no cumple lo pedido"), ("pendiente", "cuánto baja un tramo por cada metro de largo, expresado en porcentaje"), ("desnivel", "diferencia de altura entre los dos extremos de un tramo")],
    worked=[
        ("Aplicar la tolerancia", "Con tolerancia de ejemplo de 5 cm, un tramo proyectado en 300 cm se registra en 304 cm. ¿Cumple?", ["La diferencia es 304 menos 300, es decir 4 cm.", "4 es menor que 5: cumple."], "Sí, cumple"),
        ("Calcular el desnivel", "Una planilla de ejemplo usa una pendiente de 3 % en un tramo de 5 m. ¿Cuántos centímetros de desnivel resultan?", ["Se multiplica la longitud en metros por el porcentaje.", "5 por 3 son 15."], "15 cm"),
    ],
    mistakes=[("Dar por bueno todo el control porque la mayoría de los tramos cumple.", "Cada tramo es un control independiente.", "Registra cada tramo que no cumple como no conformidad."),
              ("Corregir a ojo un tramo que no cumple para que «quede igual al plano».", "Se oculta el problema y se pierde el registro.", "Informa a la jefatura o al ITO para decidir qué hacer.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es una tolerancia?", "La diferencia máxima que se acepta entre lo proyectado y lo registrado", "La diferencia mínima obligatoria entre dos tramos", "El precio máximo de un tramo", "La tolerancia fija hasta cuánto se acepta que un valor se aparte del proyecto."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es un control de verificación?", "Comparar el valor del plano con el valor registrado en obra y anotar si cumple", "Pintar los tramos de un color para reconocerlos", "Calcular el costo de los tramos de la obra", "El control compara lo proyectado con lo registrado y deja constancia del resultado."),
        ("abc", "En Instalaciones Sanitarias: ¿qué expresa la pendiente de un tramo?", "Cuánto baja el tramo por cada metro de largo", "Qué largo tiene el tramo en total", "Cuánto cuesta cada metro del tramo", "La pendiente relaciona el desnivel con el largo del tramo."),
        ("=", "{F} ¿Cuántos centímetros de diferencia hay entre lo proyectado y lo registrado en R1?", "402-400", "Se resta la longitud proyectada a la registrada.", " cm"),
        ("abc", "{F} ¿Qué tramos cumplen con el criterio de la ficha?", "R1 y R3", "R2 y R4", "Solo R1", "R1 y R3 difieren en 2 y 3 cm; R2 y R4 difieren en 5 y 10 cm."),
        ("abc", "{F} El tramo R3 difiere exactamente 3 cm. ¿Cumple?", "Sí, porque el criterio acepta 3 cm o menos", "No, porque no es menor que 3", "No, porque está al límite", "El criterio de la ficha dice «3 cm o menos», así que 3 cm cumple."),
        ("=", "{F} ¿Cuántos centímetros de desnivel resulta para el tramo de evacuación de la planilla?", "9*2", "Se multiplica la longitud en metros por el porcentaje de pendiente.", " cm"),
        ("=", "{F} ¿Cuántos centímetros excede la diferencia del tramo R4 sobre la tolerancia?", "(320-310)-3", "Se calcula la diferencia de R4 y se le resta la tolerancia de 3 cm.", " cm"),
        ("abc", "{F} ¿Qué corresponde hacer con el tramo R2?", "Registrarlo como no conformidad e informar a la jefatura o al ITO", "Corregirlo a ojo para que coincida con el plano", "No anotar nada porque la diferencia es pequeña", "Un tramo fuera de tolerancia se registra e informa; no se corrige por cuenta propia."),
        ("abc", "{F} Un compañero dice: «R2 y R4 no importan porque R1 y R3 cumplen». ¿Qué respuesta es correcta?", "Es falso: cada tramo se controla por separado y los que no cumplen se registran", "Es cierto: si cumple la mitad, la obra está bien", "Es cierto, siempre que los dos tramos buenos sean los más largos", "Que unos tramos cumplan no compensa a los que no cumplen."),
        ("abc", "En una obra real, ¿quién toma las mediciones que alimentan una tabla como la de la ficha?", "Personal capacitado y autorizado por la obra", "Cualquier estudiante que haya leído este cuaderno", "El cliente, cuando recibe la cuenta", "Medir y verificar en terreno exige capacitación y autorización; el cuaderno solo enseña a leer la tabla."),
        ("=", "{F} De los cuatro tramos de la ficha, cumplen 2. ¿Qué porcentaje de los tramos cumple?", "2*100//4", "Se divide lo que cumple entre el total y se pasa a porcentaje.", " %"),
        ("abc", "Dos tramos de evacuación de ejemplo: el tramo P mide 6 m con pendiente de ejemplo de 3 %; el tramo Q mide 12 m con pendiente de ejemplo de 1 %. ¿Cuál tiene mayor desnivel?", "El tramo P, con 18 cm frente a 12 cm", "El tramo Q, porque es más largo", "Ambos tienen el mismo desnivel", "P da 6 × 3 = 18 cm y Q da 12 × 1 = 12 cm; el largo solo no decide."),
    ],
    ctx=("abc", "Una supervisora de ejemplo te entrega la tabla de la ficha y pregunta: «¿podemos cerrar el control hoy?». ¿Qué respondes?", "Que no, porque R2 y R4 están fuera de tolerancia y deben registrarse y resolverse antes", "Que sí, porque la mayoría de los tramos casi cumple", "Que sí, si se corrigen los registros para que coincidan", "El control no se cierra con tramos fuera de tolerancia ni se alteran los registros."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué es una no conformidad?", "Un resultado que no cumple lo pedido", "Una no conformidad se registra e informa."),
        ("¿Cómo se calcula el desnivel en la planilla de ejemplo?", "Longitud en metros por pendiente en porcentaje", "El resultado queda en centímetros según la regla de la clase."),
        ("¿Qué se hace con un tramo fuera de tolerancia?", "Registrarlo e informar a la jefatura o al ITO", "No se corrige a ojo porque se perdería el registro."),
    ],
    op=("Ficha de ejemplo: criterio de ejemplo de 4 cm de tolerancia. Tramo U1: proyectada 500 cm, registrada 503 cm. Tramo U2: proyectada 350 cm, registrada 357 cm. Tramo U3: proyectada 120 cm, registrada 116 cm. Planilla de ejemplo: un tramo de 7 m con pendiente de ejemplo de 2 %. Escribe (a) la diferencia de cada tramo, (b) cuáles cumplen, (c) el desnivel de la planilla, (d) qué harías con el que no cumple.",
        "(a) U1: 3 cm; U2: 7 cm; U3: 4 cm. (b) U1 y U3 cumplen (3 y 4 cm son menores o iguales que 4); U2 no cumple. (c) 7 × 2 = 14 cm. (d) Registrarlo como no conformidad e informar a la jefatura o al ITO, sin corregirlo a ojo.",
        ["calcula las tres diferencias", "clasifica los tramos con la tolerancia", "calcula el desnivel", "indica qué hacer con la no conformidad"],
        ["hoja con la tabla de diferencias, la clasificación y el desnivel"],
        ["considerar que 4 cm no cumple", "multiplicar mal el desnivel", "proponer corregir a ojo"],
        "Pregunta: «¿qué pasa con un tramo que difiere exactamente lo que dice la tolerancia?». Si no responde, pídele que relea el ejemplo de R3."),
    reinforce="Calcula en papel el desnivel de tres tramos de ejemplo de 4 m, 6 m y 10 m con una pendiente de ejemplo de 2 %.",
    extend="Explica con un ejemplo por qué es importante que quede un registro escrito de una no conformidad.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La constructora ficticia «Obras del Sur» pide al taller una cubicación para la casa «Los Pinos»: partidas de la red sanitaria: "
     "tubería de agua potable, 48 m; tubería de evacuación, 36 m; 4 artefactos sanitarios; 1 estanque de 2 m³. La planilla se guarda en un archivo digital que incluye el nombre y la dirección de la persona dueña de la casa.")
build(
    O2, 1, F,
    use="Aprenderé qué es cubicar, para qué sirve una planilla digital, qué errores y riesgos puede tener y cómo cuidar los datos del cliente.",
    prior=["Sé qué son metros, metros cuadrados y metros cúbicos.", "Sé multiplicar y sumar.", "Sé leer una lista con cantidades."],
    explain=[
        "Cubicar es calcular las cantidades de un proyecto a partir de los planos: longitudes (en metros), superficies (en metros cuadrados) y volúmenes (en metros cúbicos). Cada cosa que se cuenta y se cobra por separado es una partida. La cubicación sirve para pedir materiales, armar un presupuesto y planificar el trabajo. Hoy se hace con una planilla digital, un programa que calcula con fórmulas lo que la persona escribe. El programa no piensa: si se digita un dato mal, calcula mal sin avisar.",
        "Por eso toda cubicación se revisa. Un error de cantidad provoca faltantes que detienen la obra, o sobrantes que cuestan dinero. Un resultado absurdo, como pedir 480 m cuando el plano muestra 48 m, se detecta comparando con una idea aproximada del tamaño esperado. El archivo contiene datos del cliente, que son confidenciales: no se comparten sin autorización y se guarda una copia de respaldo. Quien trabaja mucho rato frente a una pantalla debe hacer pausas activas y cuidar su postura.",
        f"Este cuaderno calcula en papel con datos de ejemplo. Medir en una obra real exige personal autorizado, y no hay que ir a un lugar de trabajo sin permiso. {EMER} {AVISO}",
    ],
    vocab=[("cubicar", "calcular las cantidades de longitud, superficie y volumen de un proyecto"), ("partida", "cada ítem de trabajo o material que se cuenta y se cobra por separado"), ("planilla digital", "programa que calcula con fórmulas los datos que se escriben"), ("confidencial", "que no se debe compartir sin autorización"), ("respaldo", "copia de un archivo guardada por seguridad"), ("pausa activa", "descanso corto con movimiento durante el trabajo en pantalla"), ("merma", "parte del material que se pierde o no se usa")],
    worked=[
        ("Elegir la unidad", "En una cubicación de ejemplo, un muro se mide por el área que cubre. ¿Qué unidad corresponde?", ["El área es una superficie.", "Las superficies se miden en metros cuadrados."], "Metros cuadrados (m²)"),
        ("Orden de magnitud", "Un plano de ejemplo muestra un tramo de 15 m y la planilla dice 150 m. ¿Es razonable?", ["150 es diez veces el valor del plano.", "Probablemente se digitó un cero de más: hay que revisar."], "No es razonable: hay que revisarlo"),
    ],
    mistakes=[("Pedir los materiales con el total que muestra el programa sin revisarlo.", "El programa calcula lo que se escribe, aunque esté mal.", "Revisa con una idea aproximada del tamaño y con una segunda mirada."),
              ("Enviar la planilla con el nombre y la dirección del cliente a un grupo de mensajes.", "Los datos del cliente son confidenciales.", "Comparte solo lo necesario y con autorización.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué significa cubicar?", "Calcular las cantidades de longitud, superficie y volumen que lleva el proyecto", "Pintar de colores cada elemento del plano", "Elegir al proveedor más barato", "Cubicar es calcular cantidades a partir de los planos; no es elegir proveedor ni pintar."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es una partida?", "Cada ítem de trabajo o material que se cuenta y se cobra por separado", "Un tramo roto de tubería", "La firma del cliente en el presupuesto", "Una partida es un ítem de la cubicación y del presupuesto."),
        ("abc", "¿En qué unidad se expresa un volumen?", "En metros cúbicos (m³)", "En metros cuadrados (m²)", "En metros lineales (m)", "El volumen mide espacio en tres dimensiones, por eso se usa el metro cúbico."),
        ("=", "{F} ¿Cuántos metros de tubería suman las dos redes de la ficha?", "48+36", "Se suman los metros de agua potable y de evacuación.", " m"),
        ("abc", "{F} ¿Qué magnitud expresan los 2 m³ del estanque?", "Un volumen", "Una superficie", "Una longitud", "Los metros cúbicos son la unidad con que se expresa un volumen."),
        ("abc", "{F} ¿Qué partidas de la ficha se miden en longitud?", "Las dos tuberías", "Los artefactos y el estanque", "Solo la tubería de agua potable", "Las dos tuberías se miden en metros; los artefactos se cuentan y el estanque se expresa en volumen."),
        ("=", "{F} La tubería de agua potable se paga a $1.800 el metro (valor de ejemplo). ¿Cuánto cuestan los 48 m?", "48*1800", "Se multiplican los metros por el precio de cada metro.", " pesos"),
        ("abc", "En otra planilla de ejemplo la tubería de agua tiene 480 m, pero el plano muestra un tramo de 48 m. ¿Qué corresponde?", "Revisar si se digitó un cero de más antes de pedir el material", "Pedir los 480 m porque el programa lo calculó", "Pedir 48 m sin explicar la diferencia", "Un valor diez veces mayor al plano sugiere un error de digitación que debe revisarse."),
        ("abc", "{F} El archivo de la ficha incluye el nombre y la dirección de la persona dueña. ¿Qué corresponde?", "Compartirlo solo con quienes lo necesitan, con autorización, y guardar un respaldo", "Enviarlo a un grupo de mensajes para que todos lo vean", "Imprimirlo y dejarlo a la vista en la bodega", "Los datos del cliente son confidenciales y se protegen."),
        ("abc", "{F} Un compañero dice: «como la planilla la calculó el programa, se puede pedir sin revisar». ¿Qué respuesta es correcta?", "Es falso: el programa calcula lo que se le escribe y un dato mal digitado da un resultado malo", "Es cierto: los programas nunca se equivocan", "Es cierto si el archivo tiene respaldo", "La máquina calcula lo que se digita; por eso se revisa."),
        ("abc", "Una persona de ejemplo trabaja tres horas seguidas frente a la pantalla con la planilla. ¿Qué medida de cuidado corresponde?", "Hacer pausas activas y cuidar la postura", "Seguir sin descanso para terminar antes", "Acercarse más a la pantalla", "Las pausas y la buena postura previenen molestias por trabajo prolongado."),
        ("=", "Un pedido de ejemplo necesita 60 m de tubería más una merma de ejemplo del 10 %. ¿Cuántos metros se piden en total?", "60*110//100", "Se suma el 10 % al total, es decir, se multiplica por 110 y se divide por 100.", " m"),
        ("abc", "¿Cuál es el orden lógico de una cubicación?", "Leer planos y especificaciones, medir en el plano, calcular por partida, revisar y entregar", "Leer los planos, pedir el material, calcular por partida y recién entonces revisar", "Calcular por partida, leer los planos, entregar y revisar al final", "Primero se leen los documentos; la revisión va antes de entregar."),
    ],
    ctx=("abc", "El cliente de ejemplo pide que la planilla completa, con su nombre y su dirección, se envíe a un grupo de mensajes con 30 personas. ¿Qué respondes?", "Que se enviará solo la información necesaria y con autorización, para proteger los datos personales", "Que sí, para que todos puedan opinar", "Que sí, pero sin el respaldo", "Los datos personales se protegen; se comparte solo lo necesario y con permiso."),
    sc=[
        ("En Instalaciones Sanitarias: ¿en qué unidad se mide una superficie?", "En metros cuadrados", "La superficie mide área y usa m²."),
        ("¿Qué debe hacerse antes de pedir con un total de una planilla digital?", "Revisarlo con una idea aproximada del tamaño y una segunda mirada", "El programa no detecta un dato mal digitado."),
        ("¿Qué se hace con los datos del cliente de una planilla?", "Protegerlos y compartirlos solo con autorización", "Los datos del cliente son confidenciales y no se difunden."),
    ],
    op=("Ficha de ejemplo: casa «Los Álamos». Partidas: tubería de agua potable, 30 m; tubería de evacuación, 22 m; 3 artefactos sanitarios; 1 estanque de 1 m³. La planilla incluye nombre y teléfono del dueño. Escribe (a) cuántos metros de tubería suman las dos redes, (b) qué magnitud es el volumen del estanque, (c) una regla para cuidar los datos del dueño, (d) una revisión que harías antes de pedir.",
        "(a) 30 + 22 = 52 m. (b) Volumen, en m³. (c) Compartir el archivo solo con quien lo necesita, con autorización, y guardar un respaldo. (d) Comparar los totales con los planos (orden de magnitud) y pedir una segunda mirada.",
        ["suma bien los metros", "clasifica la magnitud", "propone una regla de confidencialidad", "propone una revisión concreta"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal", "confundir volumen con superficie", "no proteger los datos del dueño"],
        "Pregunta: «¿qué pasa si se digita un dato de más en la planilla?». Si no responde, pídele que relea la idea de que el programa calcula lo que se escribe."),
    reinforce="Escribe tres partidas de ejemplo de una red sanitaria y la unidad que corresponde a cada una (m, m², m³ o unidad).",
    extend="Explica con un ejemplo por qué un error de cantidad detiene una obra o encarece los materiales.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (planilla de cubicación de ejemplo, inventada). Columnas: partida; unidad; cantidad; precio unitario (de ejemplo); total = cantidad × precio unitario. "
     "Fila 1: tubería de agua fría, m, 40, $1.200. Fila 2: tubería de evacuación, m, 25, $2.000. Fila 3: base de hormigón del estanque, m³, 3, $90.000. Fila 4: cinta de señalización, unidad, 10, $500.")
build(
    O2, 2, F,
    use="Aprenderé las fórmulas de superficie y volumen, la conversión de m³ a litros, cómo se arma una planilla con totales y qué rol cumple cada persona.",
    prior=["Sé multiplicar y sumar números grandes.", "Sé qué es cubicar y qué es una partida.", "Sé que 1 m son 100 cm."],
    explain=[
        "Para cubicar se usan fórmulas simples. La superficie de un rectángulo es el largo por el ancho y se expresa en m²: un paño de 3 m por 2 m tiene 6 m². El volumen de un bloque rectangular es el largo por el ancho por el alto y se expresa en m³: 2 m por 2 m por 3 m son 12 m³. Un metro cúbico equivale a 1.000 litros, así que 2 m³ son 2.000 litros. Hay que anotar siempre la unidad: 6 m y 6 m² son cantidades distintas.",
        "Una planilla de cubicación ordena las partidas en filas. Cada fila tiene la unidad, la cantidad, el precio unitario (lo que cuesta una unidad de la partida) y el total, que se obtiene multiplicando cantidad por precio unitario. En una planilla digital, esa multiplicación se escribe una vez como fórmula y el programa la repite en cada fila. El total general suma los totales de todas las filas.",
        f"Cada persona cumple un rol: el presupuestista o cubicador calcula cantidades y costos; el jefe de obra decide cuándo se necesitan los materiales; el bodeguero recibe y cuenta lo que llega; el ITO verifica que la obra cumpla el proyecto. {EMER} {AVISO}",
    ],
    vocab=[("superficie", "área que ocupa algo, en m²"), ("volumen", "espacio que ocupa algo, en m³"), ("precio unitario", "lo que cuesta una unidad de la partida"), ("total de la fila", "cantidad multiplicada por el precio unitario"), ("fórmula", "regla escrita que el programa aplica para calcular"), ("presupuestista", "persona que calcula cantidades y costos"), ("bodeguero", "persona que recibe, cuenta y guarda los materiales")],
    worked=[
        ("Total de una fila", "Una fila de ejemplo dice: codo de evacuación, unidad, 12, precio unitario $700. ¿Cuánto es el total de la fila?", ["El total es cantidad por precio unitario.", "12 por 700 son 8.400."], "$8.400"),
        ("Pasar a litros", "Un estanque de ejemplo tiene un volumen de 5 m³. ¿Cuántos litros son?", ["Cada metro cúbico son 1.000 litros.", "5 por 1.000 son 5.000."], "5.000 litros"),
    ],
    mistakes=[("Escribir «m» en una partida que es una superficie.", "Un metro es una longitud y un metro cuadrado es un área: se pediría la cantidad equivocada.", "Anota la unidad correcta: m² para superficies."),
              ("Sumar el precio unitario con la cantidad para sacar el total.", "El total se obtiene multiplicando.", "Multiplica cantidad por precio unitario.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué calcula la superficie de una pared?", "El área que cubre, en m²", "El largo del borde, en m", "El espacio que ocupa, en m³", "La superficie mide área y se expresa en metros cuadrados."),
        ("abc", "¿Cuántos litros tiene un metro cúbico?", "1.000 litros", "100 litros", "10 litros", "Un metro cúbico equivale a 1.000 litros."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es el precio unitario?", "Lo que cuesta una unidad de la partida", "El total de toda la planilla", "El precio de la partida más cara", "El precio unitario es el valor de una unidad; el total se calcula con la cantidad."),
        ("=", "{F} ¿Cuánto es el total de la fila de la tubería de agua fría?", "40*1200", "El total de la fila es cantidad por precio unitario.", " pesos"),
        ("=", "{F} ¿Cuánto es el total de la fila de la tubería de evacuación?", "25*2000", "El total de la fila es cantidad por precio unitario.", " pesos"),
        ("abc", "{F} ¿Qué partida de la ficha se expresa en metros cúbicos?", "La base de hormigón del estanque", "La cinta de señalización", "La tubería de agua fría", "La base de hormigón es un volumen y por eso lleva m³."),
        ("=", "{F} ¿Cuánto es el total general de la planilla?", "40*1200+25*2000+3*90000+10*500", "Se suman los totales de las cuatro filas, cada uno cantidad por precio.", " pesos"),
        ("=", "Un estanque de ejemplo tiene base de 2 m por 4 m y una altura de 1 m. ¿Cuántos metros cúbicos de volumen tiene?", "2*4*1", "El volumen se calcula como largo por ancho por alto.", " m³"),
        ("=", "Un paño de pared de ejemplo mide 5 m de largo y 4 m de alto. ¿Cuántos metros cuadrados tiene?", "5*4", "La superficie de un rectángulo es el largo por el alto.", " m²"),
        ("abc", "En una planilla, una partida de superficie aparece con la unidad «m». ¿Qué problema produce?", "Se puede pedir una cantidad equivocada porque un metro y un metro cuadrado son distintos", "Ninguno, porque son la misma unidad", "Solo cambia el color de la fila", "Longitud y superficie no son equivalentes; confundirlas altera el pedido."),
        ("abc", "En una obra de ejemplo llega un camión con materiales. ¿Quién recibe y cuenta lo que llega?", "El bodeguero", "El proyectista", "El presupuestista", "El bodeguero recibe, cuenta y guarda los materiales."),
        ("=", "{F} El volumen de la base de hormigón es 3 m³. ¿Cuántos litros son?", "3*1000", "Cada metro cúbico equivale a 1.000 litros.", " litros"),
        ("abc", "¿Qué fórmula describe mejor la columna «total» de una planilla de cubicación?", "Cantidad multiplicada por precio unitario", "Cantidad más precio unitario", "Precio unitario dividido en la cantidad", "El total de una fila es lo que cuestan todas las unidades: cantidad por precio."),
    ],
    ctx=("abc", "Una compañera de ejemplo calcula el volumen de un estanque y anota 6 m². ¿Qué le dices?", "Que un volumen va en metros cúbicos (m³), no en metros cuadrados", "Que está bien, porque ambos son metros", "Que lo escriba sin unidad para no equivocarse", "Un volumen se expresa en m³; la unidad correcta evita errores de pedido."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se calcula el total de una fila?", "Cantidad por precio unitario", "El total es lo que cuestan todas las unidades."),
        ("¿Cuántos litros son 4 m³?", "4.000 litros", "Cada metro cúbico son 1.000 litros."),
        ("¿Quién calcula cantidades y costos en una obra?", "El presupuestista o cubicador", "Es su rol dentro del equipo."),
    ],
    op=("Ficha de ejemplo: planilla con la fila 1: tubería de agua fría, m, 35, $1.500; fila 2: codo de evacuación, unidad, 8, $900; fila 3: estanque de 2 m por 2 m de base y 2 m de alto. Escribe (a) el total de la fila 1, (b) el total de la fila 2, (c) el volumen del estanque y cuántos litros son, (d) qué rol decide cuándo llegan los materiales.",
        "(a) 35 × 1.500 = 52.500 pesos. (b) 8 × 900 = 7.200 pesos. (c) 2 × 2 × 2 = 8 m³, que son 8.000 litros. (d) El jefe de obra.",
        ["calcula los dos totales", "calcula el volumen y lo convierte", "reconoce el rol del jefe de obra"],
        ["hoja con los cálculos y el rol"],
        ["sumar en vez de multiplicar", "no convertir a litros", "confundir roles"],
        "Pregunta: «¿qué unidad lleva el volumen?». Si no responde, pídele que relea la explicación de fórmulas."),
    reinforce="Calcula el total de tres filas de ejemplo con cantidades y precios unitarios a tu elección y súmalas.",
    extend="Explica con un ejemplo por qué es importante anotar la unidad en cada partida de una planilla.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (casa de ejemplo, inventada). Tramos de la tubería de agua en la planilla: 12 m, 8 m, 15 m, 5 m y 10 m. Merma de ejemplo: 10 %. "
     "La tubería se vende en barras de 6 m (de ejemplo) a $9.000 la barra (de ejemplo). La losa (radier) de la bodega mide 4 m de largo, 5 m de ancho y 10 cm de espesor.")
build(
    O2, 3, F,
    use="Aprenderé a pasar de los tramos del plano a una lista de materiales: sumar, aplicar la merma, redondear hacia arriba las barras, calcular el costo y el volumen de una losa.",
    prior=["Sé calcular un porcentaje simple.", "Sé el volumen de un bloque rectangular.", "Sé convertir m³ a litros."],
    explain=[
        "La lista de materiales dice qué se necesita y cuánto. Se parte sumando los tramos del plano. Luego se agrega la merma, que es la parte del material que se pierde o no se puede usar: con una merma de ejemplo de 10 %, 40 m se transforman en 44 m. Como el material se vende en barras de largo fijo, las barras se calculan dividiendo y redondeando hacia arriba: si 65 m se dividen en barras de 6 m, hay 10 barras completas y sobran 5 m, por lo que se necesitan 11 barras.",
        "El redondeo hacia arriba se hace porque no se pueden comprar fracciones de una barra: con 10 barras (60 m) faltaría material. El sobrante se calcula restando lo necesario de lo comprado. El costo se obtiene multiplicando las barras por el precio de cada una. Cuando el espesor se da en centímetros, el volumen de una losa se calcula convirtiendo el espesor a metros, es decir, dividiendo por 100.",
        f"Cada resultado se anota en la planilla con su unidad y con el supuesto usado (merma, largo de barra). Una cubicación sin supuestos escritos no se puede revisar. {EMER} {AVISO}",
    ],
    vocab=[("lista de materiales", "documento que dice qué materiales se necesitan y en qué cantidad"), ("merma", "parte del material que se pierde o no se puede usar"), ("redondear hacia arriba", "subir a la cantidad entera siguiente cuando sobra una fracción"), ("sobrante", "material comprado que no se usa"), ("espesor", "grosor de una losa o capa")],
    worked=[
        ("Barras necesarias", "Una casa de ejemplo necesita 40 m de tubería y se vende en barras de 6 m. ¿Cuántas barras se necesitan?", ["40 dividido en 6 da 6 y sobran 4 m.", "No alcanza con 6 barras: se necesitan 7."], "7 barras"),
        ("Volumen de una losa", "Una losa de ejemplo mide 3 m de largo, 2 m de ancho y 20 cm de espesor. ¿Cuántos litros de hormigón se necesitan?", ["El espesor es 20 cm; el volumen en m³ es 3 por 2 por 20 dividido en 100, es decir 1,2 m³.", "1,2 m³ equivalen a 1.200 litros."], "1.200 litros"),
    ],
    mistakes=[("Redondear hacia abajo las barras porque «sobra poco».", "Con una barra menos faltaría material.", "Redondea hacia arriba."),
              ("Olvidar convertir el espesor de centímetros a metros al calcular el volumen.", "Mezclar cm con m da un volumen 100 veces mayor.", "Divide los centímetros por 100 antes de multiplicar.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es la merma?", "La parte del material que se pierde o no se puede usar", "El descuento que hace el proveedor", "El material que sobra después de la obra por azar", "La merma se considera al pedir, para no quedarse corto."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es una lista de materiales?", "Un documento que dice qué materiales se necesitan y en qué cantidad", "Un plano de la casa a escala", "Una tabla de pagos al personal", "La lista de materiales traduce el proyecto en cantidades a pedir."),
        ("abc", "¿Por qué las barras se redondean hacia arriba?", "Porque no se pueden comprar fracciones de barra y faltaría material", "Porque así el pedido es más barato", "Porque las barras siempre sobran", "Con menos barras de las necesarias, el material no alcanza."),
        ("=", "{F} ¿Cuántos metros suman los cinco tramos de tubería de la planilla?", "12+8+15+5+10", "Se suman los metros de los cinco tramos.", " m"),
        ("=", "{F} ¿Cuántos metros hay que pedir al agregar la merma de 10 % al total de los tramos?", "50*110//100", "Se multiplica el total por 110 y se divide por 100 para sumar el 10 %.", " m"),
        ("=", "{F} Con 55 m a cubrir y barras de 6 m, ¿cuántas barras hay que comprar?", "(55+5)//6", "55 dividido en 6 da 9 y sobra material, por eso se redondea hacia arriba a 10.", " barras"),
        ("=", "{F} ¿Cuánto cuestan las barras que hay que comprar?", "10*9000", "Se multiplican las barras por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuántos metros cúbicos tiene la losa de la bodega? (El espesor se pasa a metros dividiendo por 100.)", "4*5*10//100", "Se multiplica largo por ancho por el espesor expresado en metros.", " m³"),
        ("=", "{F} Con 10 barras de 6 m y 55 m a cubrir, ¿cuántos metros sobran?", "10*6-55", "Se restan los metros necesarios de los metros comprados.", " m"),
        ("abc", "{F} Un compañero pide solo 9 barras porque «55 dividido en 6 da 9 y poquito». ¿Qué ocurre?", "Faltarían materiales: 9 barras son 54 m y se necesitan 55 m", "Sobrarían 2 m", "Alcanza justo", "9 barras de 6 m dan 54 m y se necesitan 55 m."),
        ("abc", "{F} Otro proveedor de ejemplo vende barras de 5 m. ¿Cuántas barras se necesitan para los 55 m?", "11 barras", "10 barras", "12 barras", "55 dividido en 5 da 11 exactos; 10 darían 50 m y 12 serían de más."),
        ("=", "{F} ¿Cuántos litros equivale el volumen de la losa de la bodega?", "4*5*10//100*1000", "Se calcula el volumen en m³ y se multiplica por 1.000.", " litros"),
        ("abc", "{F} ¿Cuál es el mejor registro de la cubicación de la tubería?", "Tramos 50 m, merma 10 %, 55 m; barras de 6 m: 10; sobran 5 m", "Se necesitan 10 barras", "Hay que comprar bastante tubería", "Un buen registro anota los supuestos y los resultados para poder revisarlos."),
    ],
    ctx=("abc", "Tu jefe de ejemplo pregunta por qué pediste 10 barras si «con 9 alcanza». ¿Qué respondes?", "Que 9 barras dan 54 m y se necesitan 55 m con la merma, por eso hay que redondear hacia arriba", "Que fue un error y que pedirás 9", "Que da lo mismo porque siempre sobra material", "Mostrar el cálculo con los supuestos permite revisar la decisión."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se obtienen las barras necesarias?", "Dividiendo los metros entre el largo de la barra y redondeando hacia arriba", "No se pueden comprar fracciones de barra."),
        ("¿Cómo se pasa un espesor de 10 cm a metros?", "Dividiendo por 100", "Cada metro equivale a 100 centímetros, por eso se divide."),
        ("¿Qué se debe anotar junto al resultado de una cubicación?", "Los supuestos usados, como la merma y el largo de la barra", "Sin supuestos escritos no se puede revisar."),
    ],
    op=("Ficha de ejemplo: una casa tiene tramos de tubería de 14 m, 9 m y 7 m. Merma de ejemplo: 10 %. Barras de 6 m a $8.000 cada una (valores de ejemplo). Escribe (a) el total de metros, (b) los metros con merma, (c) las barras que se necesitan, (d) el costo, (e) los metros que sobran.",
        "(a) 14 + 9 + 7 = 30 m. (b) 30 × 110 ÷ 100 = 33 m. (c) 33 ÷ 6 da 5 y sobran 3 m: se necesitan 6 barras. (d) 6 × 8.000 = 48.000 pesos. (e) 6 × 6 − 33 = 3 m.",
        ["suma bien los tramos", "aplica la merma", "redondea hacia arriba", "calcula costo y sobrante"],
        ["hoja con los cinco cálculos y los supuestos anotados"],
        ["redondear hacia abajo", "olvidar la merma", "no anotar los supuestos"],
        "Pregunta: «¿cuántas barras serían si el pedido fuera de 36 m?». Si no responde, pídele que relea el redondeo hacia arriba."),
    reinforce="Calcula en papel las barras de 4 m que se necesitan para tramos de 10 m, 7 m y 5 m con una merma de ejemplo de 10 %.",
    extend="Explica con un ejemplo qué pasa con el costo cuando el largo de la barra no calza con los tramos del plano.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada, completada por otra persona). Fila 1: tubería de agua fría, m, 30, $1.500, total $45.000. Fila 2: tubería de evacuación, m, 20, $2.500, total $55.000. "
     "Fila 3: base de hormigón, m³, 2, $80.000, total $160.000. Fila 4: tubería de agua fría, m, 30, $1.500, total $45.000. Fila 5: cinta de señalización, unidad, 8, $400, total $3.200. "
     "Total que muestra la planilla: $308.200. El plano indica una sola red de agua fría, de 30 m.")
build(
    O2, 4, F,
    use="Aprenderé a revisar una planilla hecha por otra persona: encontrar filas duplicadas, totales mal calculados y unidades mezcladas, y a dejar constancia del cambio.",
    prior=["Sé calcular el total de una fila.", "Sé sumar totales.", "Sé que una planilla digital calcula lo que se escribe."],
    explain=[
        "Revisar una planilla es parte de la cubicación. La revisión cruzada consiste en que otra persona, o un segundo cálculo, verifique el trabajo. Se buscan tres errores comunes: una fila duplicada, que cuenta dos veces la misma partida; un total que no coincide con cantidad por precio unitario; y una unidad mezclada, como anotar 250 m cuando el plano dice 250 cm. Para detectar errores gruesos sirve el orden de magnitud: una idea aproximada de cuánto debería dar el resultado.",
        "Después de revisar se recalcula el total correcto. Al encontrar un error no se borra el archivo original ni se corrige sin avisar: se trabaja en una copia con número de versión, se avisa a quien hizo la planilla y se deja un registro de cambios con la fila, el error, el valor corregido y la fecha. Así otras personas saben qué versión usar.",
        f"Una planilla revisada protege al cliente y a la empresa de pedir de más o de menos. Los datos de este cuaderno son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("revisión cruzada", "verificación del trabajo por otra persona o por un segundo cálculo"), ("fila duplicada", "fila que cuenta dos veces la misma partida"), ("unidad mezclada", "error de anotar una cantidad en una unidad distinta de la correcta"), ("orden de magnitud", "idea aproximada del tamaño que debería tener un resultado"), ("registro de cambios", "anotación de qué se corrigió, cuándo y por qué")],
    worked=[
        ("Encontrar un total mal calculado", "Una fila de ejemplo dice: 15 unidades a $600 cada una, total $8.000. ¿Está bien?", ["El total correcto es 15 por 600, es decir 9.000.", "El total anotado es 8.000: está mal."], "No: el total correcto es $9.000"),
        ("Detectar duplicado", "Una planilla de ejemplo trae dos filas idénticas de «llave de paso, unidad, 6, $3.000». El plano muestra 6 llaves en total. ¿Qué pasa?", ["Con dos filas se cuentan 12 llaves.", "Una de las filas está duplicada y sobra."], "Hay una fila duplicada"),
    ],
    mistakes=[("Borrar el archivo original al encontrar un error y dejar solo el corregido.", "Se pierde la trazabilidad de qué cambió.", "Trabaja en una copia con número de versión y deja un registro de cambios."),
              ("Confiar en el total que muestra el programa sin recalcular alguna fila.", "Una fórmula mal escrita da un total mal calculado.", "Recalcula al menos algunas filas por orden de magnitud y por cuenta exacta.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es una revisión cruzada de una planilla?", "Que otra persona o un segundo cálculo verifique el trabajo", "Que la misma persona repita el mismo cálculo sin cambiar nada", "Que se cruce el nombre de las filas con colores", "En la revisión cruzada otra mirada detecta errores que el autor no ve."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es una fila duplicada?", "Una fila que cuenta dos veces la misma partida", "Una fila con una cantidad grande", "Una fila con precio alto", "La duplicada repite la partida y aumenta el total."),
        ("abc", "En Instalaciones Sanitarias: ¿para qué sirve el orden de magnitud?", "Para detectar errores gruesos con una idea aproximada del resultado", "Para ordenar las filas de mayor a menor", "Para fijar el precio unitario", "El orden de magnitud permite notar un resultado absurdo antes de calcular exacto."),
        ("=", "{F} ¿Cuánto debería ser el total de la fila 2, la tubería de evacuación?", "20*2500", "El total correcto es cantidad por precio unitario.", " pesos"),
        ("abc", "{F} ¿Qué fila repite la partida de la fila 1 y debe eliminarse?", "La fila 4", "La fila 3", "La fila 5", "La fila 4 tiene la misma partida, cantidad y precio que la fila 1, y el plano muestra una sola red."),
        ("=", "{F} Si se corrige la fila 2 y se elimina la fila duplicada, ¿cuál es el total correcto de la planilla?", "45000+50000+160000+3200", "Se suman los totales de las filas 1, 2 corregida, 3 y 5.", " pesos"),
        ("=", "{F} ¿Cuántos pesos de diferencia hay entre el total que muestra la planilla y el total correcto?", "308200-258200", "Se resta el total correcto al total mostrado.", " pesos"),
        ("abc", "{F} ¿Qué error tiene la fila 2?", "El total no coincide con cantidad por precio unitario", "La unidad está mal escrita", "Está repetida", "20 por 2.500 da 50.000 y la fila dice 55.000."),
        ("=", "{F} ¿Cuánto debería ser el total de la fila 5, la cinta de señalización?", "8*400", "Se multiplican las unidades por el precio unitario.", " pesos"),
        ("abc", "En otra planilla de ejemplo, un tramo de 250 cm del plano se anotó como 250 m. ¿Qué efecto tendría?", "Se pediría una cantidad 100 veces mayor a la necesaria", "No cambiaría nada", "Se pediría la mitad", "Pasar de cm a m cambia el valor 100 veces."),
        ("abc", "El programa de una planilla de ejemplo muestra un total. Una compañera dice: «con eso basta, es del programa». ¿Qué respuesta es correcta?", "No basta: el programa suma lo que se escribió y no detecta filas duplicadas ni unidades mezcladas", "Sí basta: las planillas digitales no se equivocan", "Sí basta si el archivo tiene contraseña", "Un programa no detecta errores de contenido, solo calcula."),
        ("=", "Otra planilla de ejemplo tiene tres filas con totales de $12.000, $18.000 y $25.000, pero muestra un total de $65.000. ¿Cuántos pesos de diferencia hay con la suma correcta?", "65000-(12000+18000+25000)", "Se resta la suma correcta de las tres filas al total mostrado.", " pesos"),
        ("abc", "Al encontrar un error en una planilla de otra persona, ¿qué corresponde?", "Trabajar en una copia con versión, avisar a quien la hizo y dejar un registro de cambios", "Borrar el archivo original y dejar solo el corregido", "Corregir sin avisar para no incomodar", "Avisar y registrar mantiene la trazabilidad de qué versión es la correcta."),
    ],
    ctx=("abc", "Tu jefe de ejemplo dice: «entrega hoy el pedido con la planilla tal como está, no hay tiempo de revisar». ¿Qué propones?", "Hacer al menos una revisión rápida por orden de magnitud y de filas duplicadas antes de enviar", "Enviar sin revisar para cumplir el plazo", "Esperar a que el proveedor encuentre los errores", "Una revisión mínima evita pedidos errados que cuestan más tiempo después."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué es una unidad mezclada?", "Anotar una cantidad en una unidad distinta de la correcta", "Por ejemplo, cm en vez de m cambia el valor 100 veces."),
        ("¿Cómo se registra la corrección de una planilla ajena?", "En una copia con versión y un registro de cambios", "Así se sabe qué cambió y cuál versión usar."),
        ("¿Qué se recalcula para revisar una planilla?", "El total de las filas y el total general", "Los totales pueden estar mal aunque el programa los muestre."),
    ],
    op=("Ficha de ejemplo (planilla hecha por otra persona). Fila 1: tubería de agua, m, 25, $1.200, total $30.000. Fila 2: codos, unidad, 10, $700, total $8.000. Fila 3: tubería de agua, m, 25, $1.200, total $30.000. Total que muestra: $68.000. El plano muestra una sola tubería de agua de 25 m. Escribe (a) qué fila repite la partida de la fila 1, (b) el total correcto de la fila 2, (c) el total general correcto, (d) cómo registrarías el cambio.",
        "(a) La fila 3. (b) 10 × 700 = 7.000 pesos. (c) 30.000 + 7.000 = 37.000 pesos. (d) En una copia con versión: «fila 3 eliminada por duplicada; fila 2 corregida a $7.000; total corregido $37.000», con fecha, y avisar a quien hizo la planilla.",
        ["encuentra la fila duplicada", "recalcula la fila 2", "obtiene el total correcto", "redacta un registro de cambios con fecha y aviso"],
        ["hoja con las correcciones y el registro de cambios"],
        ["no ver el duplicado", "calcular mal la fila 2", "no avisar a quien hizo la planilla"],
        "Pregunta: «¿qué dato del plano te permitió decidir qué fila sobra?». Si no responde, pídele que relea el ejemplo del duplicado."),
    reinforce="Inventa una planilla de cuatro filas con un total mal calculado y escribe cómo la corregirías.",
    extend="Explica con un ejemplo por qué es útil guardar versiones numeradas de una planilla.",
)
