"""Administración, mención Logística, 4.º medio TP: OAM-03 (cubicar productos y espacios), OAM-04 (informar y comunicar datos de bodega) y OAM-05 (prevenir riesgos de accidentes laborales). Bodegas, productos y cifras inventados; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, papel y, si quieres, una calculadora simple. Todas las fichas, medidas, informes y casos están escritos en cada ejercicio: las bodegas, los productos y las personas son inventados y las cifras son «de ejemplo», "
             "así que no necesitas bodega, programas ni internet. Esto es aprendizaje conceptual en papel. Practicar esta tarea en una bodega real exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar. "
             "Las alturas de apilado, las cargas máximas y las reglas sobre sustancias que aparecen son de ejemplo: las reales las fijan el fabricante, la norma vigente y la persona responsable de prevención de riesgos. "
             "Aquí no se enseña a operar maquinaria ni a manipular sustancias: ante cualquier duda de seguridad, se pide ayuda a la persona responsable.")

build = make_build(MATERIALS)

O3 = "TP-ADLO-4-OAM-03"
O4 = "TP-ADLO-4-OAM-04"
O5 = "TP-ADLO-4-OAM-05"

# ============================================================ OAM-03, clase 1
F = ("Ficha 35 (caso de ejemplo, inventado) de «Distribuidora Andes del Sur». Sector de almacenamiento: 6 m de largo, 4 m de ancho y una altura máxima de apilado de ejemplo de 2 m (la altura real la fijan el fabricante y la norma vigente). "
     "Caja del producto H: 40 cm de largo, 30 cm de ancho y 20 cm de alto. Equivalencias: 1 m = 100 cm; 1 m³ = 1.000.000 cm³. Se reserva el 30 % del sector para pasillos y circulación, por lo que se usa el 70 %.")
build(
    O3, 1, F,
    use="Aprenderé qué es cubicar, para qué sirve en la bodega y cómo calcular el volumen de una caja y de un sector con medidas de ejemplo.",
    prior=["Sé multiplicar y dividir.", "Conozco las unidades de longitud (cm y m).", "Sé qué es el almacenamiento ordenado."],
    explain=[
        "Cubicar es calcular el volumen que ocupa un producto y el volumen disponible de un espacio, para decidir cuántas unidades caben y cómo disponerlas. Sirve para aprovechar bien la bodega, calcular cuántos sectores se necesitan y evitar sobrecargas. El volumen de una caja con forma de prisma recto es largo × ancho × alto.",
        "Las medidas deben estar en la misma unidad. Si el sector se mide en metros y la caja en centímetros, se convierte: 1 m = 100 cm, y el volumen se expresa en cm³ o en m³ (1 m³ = 1.000.000 cm³). Para saber cuántas cajas caben por volumen se divide el volumen utilizable del sector por el volumen de una caja. Es un cálculo teórico: no considera pasillos ni la forma de colocar las cajas.",
        "En la práctica se reserva un espacio para pasillos y circulación, se respeta la altura máxima de apilado y no se supera la carga máxima de los estantes. Esos límites los fijan el fabricante, la norma vigente y la persona responsable de seguridad, y se anotan en la ficha del sector. Este cuaderno solo calcula en papel.",
    ],
    vocab=[("cubicar", "calcular el volumen de productos y espacios"), ("volumen", "espacio que ocupa un cuerpo: largo × ancho × alto"), ("cm³", "centímetro cúbico, unidad de volumen"), ("m³", "metro cúbico, igual a 1.000.000 cm³"), ("espacio utilizable", "parte del sector que se destina a producto"), ("altura de apilado", "altura máxima permitida para apilar cajas")],
    worked=[
        ("Volumen de una caja", "Una caja ficticia mide 50 cm de largo, 20 cm de ancho y 10 cm de alto. ¿Cuál es su volumen?", ["Volumen = largo × ancho × alto.", "50 × 20 × 10 = 10.000."], "10.000 cm³"),
        ("Pasar a metros cúbicos", "Un espacio de ejemplo mide 3 m × 2 m × 1 m. ¿Cuántos m³ tiene?", ["3 × 2 × 1 = 6.", "Las tres medidas están en metros."], "6 m³"),
    ],
    mistakes=[("Multiplicar centímetros por metros sin convertir.", "Se mezclan unidades y el resultado no tiene sentido.", "Convierte todas las medidas a la misma unidad antes de multiplicar."),
              ("Usar todo el volumen del sector para guardar cajas.", "No se deja espacio para pasillos ni seguridad.", "Reserva el espacio de circulación que indica la ficha.")],
    T=[
        ("abc", "En Logística: ¿qué es cubicar?", "Calcular el volumen de productos y de espacios para decidir cuántos caben", "Pintar las cajas de un solo color", "Contar cuántos clientes hay", "Cubicar es calcular volúmenes para disponer bien los productos."),
        ("=", "{F} ¿Cuál es el volumen de una caja del producto H?", "40*30*20", "Volumen = largo × ancho × alto.", " cm³"),
        ("=", "{F} ¿Cuántos m³ tiene el sector hasta la altura de apilado (6 m × 4 m × 2 m)?", "6*4*2", "Las tres medidas ya están en metros.", " m³"),
        ("=", "{F} ¿Cuántos cm³ tiene el sector (600 cm × 400 cm × 200 cm)?", "600*400*200", "Se multiplican las tres medidas en centímetros.", " cm³"),
        ("abc", "{F} ¿Por qué se convierten las medidas a una misma unidad?", "Para que el producto de las medidas tenga sentido", "Para que las cajas se vean más grandes", "Porque lo exige el color de la ficha", "Mezclar cm y m da un volumen sin sentido."),
        ("=", "{F} ¿Cuántas cajas caben por volumen en todo el sector, sin pasillos?", "600*400*200//(40*30*20)", "Cajas teóricas = volumen del sector ÷ volumen de una caja.", " cajas"),
        ("=", "{F} Con el 70 % utilizable, ¿cuántas cajas caben?", "600*400*200//(40*30*20)*70//100", "Se aplica el 70 % a las cajas teóricas.", " cajas"),
        ("=", "{F} ¿Cuántos m² de piso tiene el sector (largo por ancho)?", "6*4", "Superficie = largo × ancho.", " m²"),
        ("abc", "{F} Un compañero dice que las 2.000 cajas teóricas caben todas porque el cálculo da 2.000. ¿Qué respondes?", "Hay que descontar pasillos y respetar los límites de apilado y de carga", "Tiene razón, el cálculo basta", "Hay que agregar más cajas", "El cálculo teórico no incluye circulación ni seguridad."),
        ("abc", "{F} ¿Qué dato de la ficha limita la cantidad de capas de cajas que se pueden apilar?", "La altura máxima de apilado de 2 m", "El nombre del producto", "El color de las cajas", "La altura de apilado fija el máximo de capas."),
        ("abc", "{F} ¿Quién fija la altura real de apilado en una bodega?", "El fabricante, la norma vigente y la persona responsable de seguridad", "El que apila más rápido", "Cualquier cliente", "Los límites no se improvisan: se consultan."),
        ("abc", "Un bodeguero apila una pared de cajas hasta el techo para ganar espacio. ¿Qué es lo más adecuado?", "Detenerse y consultar el límite de apilado antes de seguir", "Seguir si la pared se ve firme", "Seguir si hay más personas cerca", "La altura de apilado es un límite de seguridad que se respeta."),
        ("=", "Una caja ficticia mide 25 cm × 20 cm × 10 cm. ¿Cuál es su volumen?", "25*20*10", "Volumen = largo × ancho × alto.", " cm³"),
    ],
    ctx=("abc", "La jefatura pregunta cuántas cajas de H caben en el sector si se usa el 70 % del espacio. ¿Qué responde un buen cálculo?", "1.400 cajas aproximadamente, según el cálculo teórico de ejemplo", "2.000 cajas exactas", "No se puede calcular", "El cálculo usa el volumen utilizable y se declara como aproximado."),
    sc=[
        ("En Logística: ¿cómo se calcula el volumen de una caja?", "Largo por ancho por alto", "Se multiplican las tres medidas para obtener el volumen."),
        ("¿Cuántos cm³ tiene 1 m³?", "1.000.000", "Un metro cúbico equivale a un millón de cm³."),
        ("¿Quién fija los límites de apilado?", "El fabricante y la norma vigente", "No se improvisan en la bodega."),
    ],
    op=("Con la Ficha 35, escribe una hoja de cubicaje con: volumen de una caja, volumen del sector, cajas teóricas, cajas con el 70 % utilizable y una frase sobre los límites de seguridad que consultarías.\n{F}",
        "Volumen de una caja: 24.000 cm³. Volumen del sector: 48.000.000 cm³ (48 m³). Cajas teóricas: 2.000. Con el 70 % utilizable: 1.400. Consultaría la altura máxima de apilado, la carga máxima de los estantes y la señalética con el responsable de prevención de riesgos.",
        ["calcula los volúmenes", "aplica el 70 %", "reconoce límites de seguridad"],
        ["hoja de cubicaje de cinco líneas"],
        ["mezclar unidades", "usar todo el volumen", "olvidar los límites"],
        "Rehace los cálculos con la ficha. Si no menciona límites, pregunta quién los fija."),
    reinforce="Calcula en papel el volumen de tres cajas ficticias con medidas que inventes.",
    extend="Explica con un ejemplo inventado por qué una caja más alta puede reducir la cantidad que cabe en un sector.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 36 (datos de ejemplo, inventados) de «Distribuidora Andes del Sur». Paleta (plataforma para apilar cajas) de ejemplo: 120 cm de largo y 100 cm de ancho; altura máxima de carga de ejemplo: 100 cm; peso máximo de ejemplo de la paleta cargada: 400 kg. "
     "Caja del producto H: 40 cm × 30 cm × 20 cm; peso 8 kg. Las cajas se colocan sin girar: el lado de 40 cm va a lo largo de la paleta y el de 30 cm a lo ancho. "
     "Documentos: ficha técnica del producto (medidas y peso), plano de la bodega, planilla de cubicaje. Roles: bodeguero(a) y jefe(a) de bodega.")
build(
    O3, 2, F,
    use="Aprenderé a calcular cuántas cajas caben en una paleta por capa y por altura, a comprobar el peso y los documentos que respaldan el cubicaje.",
    prior=["Sé calcular el volumen de una caja.", "Sé dividir y quedarme con la parte entera.", "Sé convertir entre cm y m."],
    explain=[
        "Para saber cuántas cajas caben en una paleta no basta dividir volúmenes, porque las cajas no se parten. Se calcula por capas: cuántas cajas caben a lo largo (largo de la paleta ÷ largo de la caja, tomando solo el número entero), cuántas a lo ancho, y se multiplican para obtener las cajas por capa. Luego se calculan cuántas capas caben en la altura máxima (altura de carga ÷ alto de la caja, número entero).",
        "Después se verifica el peso: cajas totales × peso por caja, y se compara con el peso máximo permitido. Si lo supera, se reduce la cantidad. La ocupación es el volumen usado ÷ volumen disponible, expresada en porcentaje, y muestra cuánto del espacio se aprovecha.",
        "Los datos salen de documentos: la ficha técnica del producto trae las medidas y el peso; el plano de la bodega muestra los sectores; la planilla de cubicaje registra los cálculos. El jefe de bodega revisa y autoriza. Las capacidades reales las fija el fabricante y la norma vigente; las de aquí son de ejemplo.",
    ],
    vocab=[("paleta", "plataforma sobre la cual se apilan cajas"), ("capa", "nivel horizontal de cajas en una paleta"), ("parte entera", "número sin decimales que sobra al dividir"), ("peso máximo", "carga límite permitida"), ("ocupación", "volumen usado × 100 ÷ volumen disponible"), ("planilla de cubicaje", "registro de los cálculos de cubicaje")],
    worked=[
        ("Cajas por capa", "Una paleta ficticia mide 90 cm × 60 cm y una caja 30 cm × 20 cm (sin girar). ¿Cuántas cajas hay por capa?", ["90 ÷ 30 = 3 a lo largo.", "60 ÷ 20 = 3 a lo ancho; 3 × 3 = 9."], "9 cajas por capa"),
        ("Parte entera", "Una paleta ficticia mide 100 cm y la caja 30 cm. ¿Cuántas caben a lo largo?", ["100 ÷ 30 = 3,3.", "No existe 0,3 de caja: se toma 3."], "3 cajas"),
    ],
    mistakes=[("Redondear hacia arriba el número de cajas por fila.", "No hay espacio para una caja incompleta.", "Toma solo la parte entera de la división."),
              ("Olvidar comprobar el peso máximo.", "Puede sobrepasarse la carga permitida.", "Multiplica las cajas por su peso y compara con el máximo.")],
    T=[
        ("abc", "En Logística: ¿qué se hace con el resultado de dividir el largo de la paleta por el largo de la caja?", "Se toma la parte entera", "Se redondea hacia arriba", "Se multiplica por 2", "Una caja incompleta no cabe, por eso se toma la parte entera."),
        ("=", "{F} ¿Cuántas cajas caben a lo largo de la paleta (120 cm ÷ 40 cm)?", "120//40", "División entera del largo de la paleta por el de la caja.", " cajas"),
        ("=", "{F} ¿Cuántas cajas caben a lo ancho de la paleta (100 cm ÷ 30 cm, parte entera)?", "100//30", "Se toma la parte entera de la división.", " cajas"),
        ("=", "{F} ¿Cuántas cajas hay por capa?", "(120//40)*(100//30)", "Cajas por capa = cajas a lo largo × cajas a lo ancho.", " cajas"),
        ("=", "{F} ¿Cuántas capas caben en la altura máxima de 100 cm?", "100//20", "Capas = altura máxima ÷ alto de la caja.", " capas"),
        ("=", "{F} ¿Cuántas cajas caben en total en la paleta?", "(120//40)*(100//30)*(100//20)", "Total = cajas por capa × capas.", " cajas"),
        ("=", "{F} ¿Cuántos kg pesan las cajas de la paleta cargada?", "(120//40)*(100//30)*(100//20)*8", "Peso = cajas × peso por caja.", " kg"),
        ("abc", "{F} ¿La paleta cargada cumple el peso máximo de 400 kg?", "Sí, porque 360 kg es menor que 400 kg", "No, porque 360 kg es mayor que 400 kg", "No se puede saber", "360 kg no supera el máximo de 400 kg."),
        ("=", "{F} ¿Cuántos cm³ ocupan las cajas de la paleta (cajas × 24.000 cm³)?", "45*24000", "Volumen usado = cajas × volumen de una caja.", " cm³"),
        ("=", "{F} ¿Qué porcentaje del volumen de la paleta (120 × 100 × 100 cm) ocupan las cajas?", "45*24000*100//(120*100*100)", "Ocupación = volumen usado × 100 ÷ volumen disponible.", " %"),
        ("abc", "{F} ¿Qué documento trae las medidas y el peso de una caja?", "La ficha técnica del producto", "El plano de la bodega", "La planilla de cubicaje", "La ficha técnica del producto trae esos datos."),
        ("abc", "{F} Un compañero dice que 45 cajas valen igual aunque las giren al revés. ¿Qué respondes?", "Al girarlas cambia el número por capa y hay que recalcular", "Siempre vale lo mismo", "No se puede girar ninguna caja", "Otra orientación cambia las divisiones y, por tanto, el total."),
        ("abc", "{F} Si la caja pesara 10 kg, ¿qué ocurriría con el peso de la paleta (45 cajas)?", "Pesaría 450 kg y superaría el máximo, por lo que habría que reducir cajas", "Pesaría 360 kg", "No cambiaría", "45 × 10 = 450 kg, más que 400 kg."),
    ],
    ctx=("abc", "El jefe de bodega pide revisar el cubicaje de una paleta nueva. ¿Qué datos necesita el bodeguero antes de calcular?", "Medidas y peso de la caja, medidas de la paleta y los límites de altura y peso", "El color de la caja", "El nombre del proveedor", "El cálculo exige medidas, peso y límites de la ficha."),
    sc=[
        ("En Logística: ¿cómo se calcula el número de cajas por capa?", "Cajas a lo largo por cajas a lo ancho", "Cada lado se calcula con la parte entera."),
        ("¿Qué se compara con el peso máximo?", "El peso total de las cajas", "Se verifica que no se sobrepase."),
        ("¿Qué mide la ocupación?", "Cuánto del volumen disponible se usa", "El resultado se expresa en porcentaje del total."),
    ],
    op=("Con la Ficha 36, escribe una planilla de cubicaje de la paleta con: cajas por capa, capas, total de cajas, peso, cumplimiento del máximo y ocupación. Agrega una frase sobre quién revisa los datos y qué documento los respalda.\n{F}",
        "Cajas por capa: 9. Capas: 5. Total: 45 cajas. Peso: 360 kg, cumple el máximo de 400 kg. Ocupación: 90 %. El jefe de bodega revisa; los datos de las cajas se respaldan con la ficha técnica del producto.",
        ["calcula por capas con parte entera", "verifica el peso", "calcula la ocupación", "nombra quién revisa y el documento"],
        ["planilla de cubicaje de seis líneas"],
        ["redondear hacia arriba", "olvidar el peso", "no indicar el respaldo"],
        "Rehace los cálculos. Si redondea hacia arriba, pide explicar por qué no cabe media caja."),
    reinforce="Calcula en papel las cajas por capa de una paleta ficticia de 80 cm × 60 cm con cajas de 20 cm × 15 cm.",
    extend="Explica con un ejemplo inventado por qué la forma de colocar las cajas puede cambiar el total.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 37 (caso de ejemplo, inventado) de «Distribuidora Andes del Sur». Estante de ejemplo: cada nivel mide 200 cm de largo, 60 cm de fondo y 50 cm de alto libre; tiene 3 niveles; capacidad de carga de ejemplo: 450 kg por estante. "
     "Caja del producto H: 40 cm × 30 cm × 20 cm; peso 8 kg. Disposición A: el lado de 40 cm va a lo largo del estante y el de 30 cm a lo fondo. Disposición B: el lado de 30 cm va a lo largo y el de 40 cm a lo fondo. "
     "En cada nivel se apilan cajas en capas del alto de la caja (20 cm).")
build(
    O3, 3, F,
    use="Aprenderé a analizar dos disposiciones de cajas en un estante, elegir la que aprovecha mejor el espacio y comprobar que no supere la carga permitida.",
    prior=["Sé calcular cajas por capa con parte entera.", "Sé calcular el peso total.", "Sé comparar dos alternativas con el mismo criterio."],
    explain=[
        "Al analizar dos disposiciones se calcula, para cada una, cuántas cajas caben por nivel: cajas a lo largo × cajas a lo fondo × capas en la altura libre. Luego se multiplica por los niveles del estante. Se comparan los totales y se elige la disposición que permite más cajas, siempre que cumpla las reglas de seguridad.",
        "La capacidad de carga del estante es un límite obligatorio. Se calcula el peso total (cajas × peso por caja) y se compara con la capacidad. Si la supera, se reduce el número de cajas: se divide la capacidad por el peso de una caja y se toma la parte entera. Una disposición que ocupe más espacio pero supere la carga no es válida.",
        "El análisis termina con una conclusión: qué disposición se elige, cuántas cajas se guardan y qué límite fue el que decidió. Se anota en la planilla de cubicaje y la revisa el jefe de bodega. Las medidas y límites son de ejemplo.",
    ],
    vocab=[("disposición", "forma de colocar las cajas"), ("fondo", "medida de adelante hacia atrás del estante"), ("alto libre", "altura disponible en un nivel"), ("capacidad de carga", "peso máximo que soporta el estante"), ("criterio obligatorio", "límite que siempre debe cumplirse"), ("conclusión", "decisión justificada del análisis")],
    worked=[
        ("Cajas por nivel", "Un nivel de ejemplo mide 100 cm de largo, 40 cm de fondo y 30 cm de alto. La caja mide 20 cm × 20 cm × 10 cm. ¿Cuántas caben por nivel?", ["100 ÷ 20 = 5; 40 ÷ 20 = 2; 30 ÷ 10 = 3.", "5 × 2 × 3 = 30."], "30 cajas"),
        ("Carga máxima", "Un estante ficticio soporta 100 kg y cada caja pesa 6 kg. ¿Cuántas cajas puede cargar como máximo?", ["100 ÷ 6 = 16,6.", "Se toma la parte entera: 16."], "16 cajas"),
    ],
    mistakes=[("Elegir la disposición con más cajas sin revisar el peso.", "Puede superar la carga del estante.", "Verifica el peso total antes de decidir."),
              ("Olvidar las capas en altura y contar solo una capa por nivel.", "Se subestima la capacidad.", "Divide la altura libre por el alto de la caja.")],
    T=[
        ("abc", "En Logística: ¿qué se calcula primero al comparar dos disposiciones?", "Las cajas por nivel de cada una", "El color de las cajas", "El precio del estante", "Primero se calcula la cantidad que cabe con cada disposición."),
        ("=", "{F} Disposición A: ¿cuántas cajas caben a lo largo (200 ÷ 40)?", "200//40", "Se divide el largo del nivel por el lado de la caja que va a lo largo.", " cajas"),
        ("=", "{F} Disposición A: ¿cuántas cajas caben a lo fondo (60 ÷ 30)?", "60//30", "Se divide el fondo por el lado de la caja que va a lo fondo.", " cajas"),
        ("=", "{F} Disposición A: ¿cuántas capas caben en 50 cm de alto libre?", "50//20", "Capas = alto libre ÷ alto de la caja, solo parte entera.", " capas"),
        ("=", "{F} Disposición A: ¿cuántas cajas caben por nivel?", "(200//40)*(60//30)*(50//20)", "Cajas = largo × fondo × capas.", " cajas"),
        ("=", "{F} Disposición B: ¿cuántas cajas caben por nivel?", "(200//30)*(60//40)*(50//20)", "Se repite el cálculo con los lados intercambiados.", " cajas"),
        ("abc", "{F} ¿Qué disposición permite más cajas por nivel?", "La A, con 20 cajas por nivel", "La B, con 12 cajas por nivel", "Ambas lo mismo", "La A permite 20 y la B 12."),
        ("=", "{F} Con la disposición A y 3 niveles, ¿cuántas cajas caben en total?", "(200//40)*(60//30)*(50//20)*3", "Total = cajas por nivel × niveles.", " cajas"),
        ("=", "{F} ¿Cuántos kg pesan esas cajas?", "(200//40)*(60//30)*(50//20)*3*8", "Peso = cajas × peso por caja.", " kg"),
        ("abc", "{F} ¿Qué ocurre con la capacidad de carga del estante (450 kg)?", "Se supera, porque 480 kg es más que 450 kg", "Se cumple, porque 480 kg es menos que 450 kg", "No se puede saber", "480 kg supera el límite del estante."),
        ("=", "{F} ¿Cuántas cajas puede cargar como máximo el estante según su capacidad (450 ÷ 8, parte entera)?", "450//8", "Máximo = capacidad ÷ peso por caja, solo parte entera.", " cajas"),
        ("abc", "{F} ¿Qué conclusión corresponde?", "Usar la disposición A con un máximo de 56 cajas por el límite de carga", "Usar la A con las 60 cajas", "Usar la B sin límite", "El límite de carga obliga a reducir las cajas aunque la disposición permita más."),
        ("abc", "{F} Un compañero propone cargar las 60 cajas «porque el estante es resistente a la vista». ¿Qué respondes?", "La carga máxima se respeta aunque el estante parezca firme", "Tiene razón", "Hay que cargar 80 cajas", "Los límites de carga no se sustituyen por la apariencia."),
    ],
    ctx=("abc", "El jefe de bodega pregunta cuántas cajas de H guardar en cada estante. ¿Qué responde un buen análisis?", "56 cajas con la disposición A, por el límite de carga de 450 kg", "60 cajas porque caben", "36 cajas con la disposición B", "La respuesta combina la mejor disposición con el límite de carga."),
    sc=[
        ("En Logística: ¿qué es un criterio obligatorio en un estante?", "Un límite que siempre debe cumplirse, como la carga máxima", "No se negocia ni se compensa."),
        ("¿Cómo se calcula el máximo por carga?", "Capacidad dividida por el peso de una caja, parte entera", "Así se evita superar el límite."),
        ("¿Qué disposición se elige?", "La que permite más cajas dentro de los límites", "El límite de seguridad manda sobre cualquier otro criterio."),
    ],
    op=("Con la Ficha 37, escribe un análisis de seis líneas: cajas por nivel y totales de cada disposición, el peso de la mejor, el límite de carga, la conclusión final y quién revisa.\n{F}",
        "A: 20 cajas por nivel y 60 en total. B: 12 por nivel y 36 en total. La A pesa 480 kg y supera 450 kg. Máximo por carga: 56 cajas. Conclusión: usar la disposición A con 56 cajas. Revisa el jefe de bodega.",
        ["calcula ambas disposiciones", "compara el peso con el límite", "concluye con el límite", "nombra quién revisa"],
        ["análisis de seis líneas"],
        ["no revisar el peso", "elegir B sin comparar", "no concluir"],
        "Revisa cada cálculo. Si concluye 60 cajas, pide revisar el límite de carga."),
    reinforce="Calcula en papel cajas por nivel de un estante ficticio con dos disposiciones de caja.",
    extend="Explica con un ejemplo inventado cuándo la disposición con menos cajas es la mejor.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 38 (datos de ejemplo, inventados) de «Distribuidora Andes del Sur». Se deben guardar 1.680 cajas del producto H (24.000 cm³ cada una). Sector de ejemplo: 6 m × 4 m de piso; se usa el 70 % del volumen útil. "
     "Alternativa X: apilar hasta una altura de 2 m. Alternativa Y: apilar hasta una altura de 1 m (criterio de seguridad reforzado de la empresa). Costo de arrendar un sector de ejemplo: $96.000 al mes por sector. "
     "Cada sector se calcula igual: volumen = 600 cm × 400 cm × altura de apilado; cajas = volumen ÷ 24.000 cm³ × 70 % (parte entera).")
build(
    O3, 4, F,
    use="Aprenderé a aplicar el cubicaje para decidir cuántos sectores se necesitan y a comparar alternativas con un criterio de seguridad y de costo.",
    prior=["Sé calcular volúmenes y cajas por volumen.", "Sé calcular porcentajes.", "Conozco los límites de apilado."],
    explain=[
        "Con el cubicaje se decide cuántos sectores se necesitan. Primero se calcula la capacidad de un sector: volumen útil ÷ volumen de una caja, aplicando el porcentaje utilizable. Después se divide el total de cajas entre la capacidad de un sector y, si no es exacto, se aproxima hacia arriba, porque no se puede arrendar medio sector.",
        "Si hay dos alternativas, primero se revisa el criterio de seguridad. Una altura de apilado más baja reduce la capacidad pero cumple un límite más exigente. Si la norma vigente o la empresa exigen esa altura, la alternativa de mayor altura se descarta, aunque cueste menos. Después se calcula el costo y se compara.",
        "El resultado se presenta con los cálculos a la vista, la ocupación del espacio y la recomendación; la decisión es de la jefatura. Las cifras y límites de este cuaderno son de ejemplo.",
    ],
    vocab=[("capacidad de un sector", "cajas que caben en un sector"), ("sector", "espacio de bodega destinado a almacenar"), ("aproximar hacia arriba", "subir al entero siguiente cuando sobra"), ("ocupación", "porcentaje de la capacidad usada"), ("criterio de seguridad", "límite que protege a las personas"), ("recomendación", "propuesta a quien decide")],
    worked=[
        ("Sectores necesarios", "Se deben guardar 500 cajas y cada sector de ejemplo guarda 200. ¿Cuántos sectores se necesitan?", ["500 ÷ 200 = 2,5.", "Se aproxima hacia arriba: 3."], "3 sectores"),
        ("Ocupación", "Con 3 sectores de 200 cajas se guardan 500. ¿Qué porcentaje de la capacidad se usa?", ["Capacidad = 600.", "500 × 100 ÷ 600 = 83 (parte entera)."], "83 %"),
    ],
    mistakes=[("Dejar la cantidad de sectores como número con coma.", "No existen fracciones de sector.", "Aproxima hacia arriba."),
              ("Elegir la alternativa más barata aunque incumpla el criterio de seguridad.", "Pone en riesgo a las personas y a los productos.", "Descarta primero lo que no cumple.")],
    T=[
        ("abc", "En Logística: ¿qué se hace si el número de sectores no es exacto?", "Se aproxima hacia arriba", "Se aproxima hacia abajo", "Se ignora el resto", "No se puede arrendar medio sector, por eso se sube."),
        ("=", "{F} Alternativa X: ¿cuántas cajas caben en un sector (600 × 400 × 200 ÷ 24.000, con 70 %)?", "600*400*200//24000*70//100", "Cajas = volumen ÷ volumen de una caja, aplicando el 70 %.", " cajas"),
        ("=", "{F} Alternativa Y: ¿cuántas cajas caben en un sector (600 × 400 × 100 ÷ 24.000, con 70 %)?", "600*400*100//24000*70//100", "La altura es la mitad, por eso la capacidad es la mitad.", " cajas"),
        ("=", "{F} Alternativa X: ¿cuántos sectores se necesitan para las 1.680 cajas (aproximando hacia arriba)?", "(1680+1399)//1400", "Sectores = cajas ÷ capacidad, subiendo al entero siguiente.", " sectores"),
        ("=", "{F} Alternativa Y: ¿cuántos sectores se necesitan?", "(1680+699)//700", "Sectores = cajas ÷ capacidad, subiendo al entero siguiente.", " sectores"),
        ("=", "{F} ¿Cuántos pesos al mes cuesta la alternativa X?", "2*96000", "Costo = sectores × costo por sector.", " pesos"),
        ("=", "{F} ¿Cuántos pesos al mes cuesta la alternativa Y?", "3*96000", "Costo = sectores × costo por sector.", " pesos"),
        ("=", "{F} ¿Cuántos pesos de diferencia mensual hay entre ambas?", "3*96000-2*96000", "Se resta el costo menor al mayor.", " pesos"),
        ("=", "{F} Con la alternativa X, ¿qué porcentaje de la capacidad de 2 sectores usan las 1.680 cajas?", "1680*100//(2*1400)", "Ocupación = cajas × 100 ÷ capacidad.", " %"),
        ("abc", "{F} Si la empresa exige la altura de 1 m como criterio de seguridad, ¿qué alternativa corresponde?", "La Y, aunque cueste más", "La X, porque cuesta menos", "Ninguna", "Un criterio de seguridad obligatorio descarta la X."),
        ("abc", "{F} Un compañero propone usar la X «porque ahorramos $96.000». ¿Qué respondes?", "Si el criterio de seguridad es obligatorio, la X no puede elegirse", "Tiene razón, el costo manda", "Hay que apilar hasta 3 m", "La seguridad es un criterio obligatorio que se cumple antes del ahorro."),
        ("abc", "{F} Si no hubiera criterio obligatorio de altura, ¿qué alternativa sería más económica?", "La X", "La Y", "Cuestan igual", "La X cuesta $192.000 al mes y la Y $288.000."),
        ("abc", "{F} ¿Qué debe incluir la recomendación a la jefatura?", "Los cálculos, la ocupación, el costo y el criterio de seguridad aplicado", "Solo el nombre de la alternativa", "Solo el costo", "La jefatura decide con cálculos y criterios a la vista."),
    ],
    ctx=("abc", "La jefatura pregunta cuántos sectores y cuánto cuesta cumplir la altura de seguridad reforzada. ¿Qué responde un buen cálculo?", "3 sectores y $288.000 al mes con la alternativa Y", "2 sectores y $192.000 al mes", "1 sector", "Con la altura de 1 m caben 700 cajas por sector y se necesitan 3."),
    sc=[
        ("En Logística: ¿qué se descarta primero?", "Las alternativas que no cumplen el criterio de seguridad", "Los criterios obligatorios van antes que el costo."),
        ("¿Cómo se calcula la ocupación?", "Cajas por cien dividido por la capacidad", "Mide cuánto de la capacidad se usa."),
        ("¿Quién decide la alternativa?", "La jefatura", "El análisis se presenta para su decisión."),
    ],
    op=("Con la Ficha 38, escribe una recomendación de cinco líneas: capacidad por sector de cada alternativa, sectores necesarios, costo mensual, cuál recomiendas con el criterio de seguridad y la ocupación de la elegida.\n{F}",
        "X: 1.400 cajas por sector, 2 sectores, $192.000. Y: 700 cajas por sector, 3 sectores, $288.000. Recomiendo la Y si la altura de 1 m es obligatoria. Ocupación de la Y: 1.680 × 100 ÷ 2.100 = 80 %. La decisión final es de la jefatura.",
        ["calcula capacidades y sectores", "calcula costos", "aplica el criterio de seguridad", "indica la ocupación"],
        ["recomendación de cinco líneas"],
        ["no aproximar hacia arriba", "ignorar la seguridad", "no calcular la ocupación"],
        "Rehace los cálculos. Si elige por costo sin ver seguridad, pide revisar el criterio."),
    reinforce="Calcula en papel cuántos sectores de 300 cajas se necesitan para guardar 1.000 cajas.",
    extend="Explica con un ejemplo inventado cuándo conviene pagar más por una alternativa más segura.",
)

# ============================================================ OAM-04, clase 1
F = ("Ficha 39 (caso de ejemplo, inventado) de «Distribuidora Andes del Sur». Sistemas de la bodega: lectores de código de barras (leen líneas impresas en la caja con un haz de luz), etiquetas de radiofrecuencia o RFID (llevan un chip que se lee por ondas de radio, sin ver la etiqueta) y un sistema computacional que guarda las existencias. "
     "Situación: el jefe de ventas pregunta por correo cuántas unidades del producto A hay disponibles. El sistema muestra 150 unidades, pero 20 están reservadas para un pedido ya comprometido. Solo el personal autorizado entra al sistema con clave personal.")
build(
    O4, 1, F,
    use="Aprenderé para qué sirve comunicar los datos de la bodega, qué sistemas se usan (código de barras, radiofrecuencia y computación) y qué cuidados de exactitud y privacidad se aplican.",
    prior=["Sé leer un kárdex.", "Sé qué es el stock.", "Sé que las claves son personales."],
    explain=[
        "Comunicar los datos de la bodega es entregar a quien lo necesita la información correcta sobre lo que entra, lo que sale y lo que se guarda. El jefe de ventas necesita saber cuánto puede vender; el jefe de compras, cuándo reponer. Un dato oportuno, claro y exacto evita ventas sin stock y compras de más.",
        "Los datos se capturan con distintos sistemas. El código de barras se lee con un lector óptico. La radiofrecuencia (RFID) usa etiquetas con un chip que se leen por ondas de radio a distancia, sin necesidad de ver la etiqueta. Un sistema computacional guarda los datos y permite consultarlos. Cada sistema puede fallar: una etiqueta dañada o una lectura incompleta entrega un dato errado, por eso se verifica con el conteo.",
        "Al informar se cuida la privacidad: se comparte solo con personas autorizadas, sin entregar datos de clientes o proveedores que no se necesitan, y con claves personales. El stock disponible es el saldo menos lo reservado; informar el saldo sin descontar lo reservado puede llevar a prometer lo que no existe.",
    ],
    vocab=[("código de barras", "líneas impresas que se leen con un lector óptico"), ("radiofrecuencia (RFID)", "etiquetas con chip que se leen por ondas de radio"), ("sistema computacional", "programa que guarda y entrega datos"), ("stock disponible", "saldo menos lo reservado"), ("reservado", "comprometido para un pedido ya acordado"), ("oportuno", "entregado a tiempo")],
    worked=[
        ("Stock disponible", "Un sistema ficticio muestra 80 unidades y 12 están reservadas. ¿Cuántas están disponibles?", ["Disponible = saldo − reservado.", "80 − 12 = 68."], "68 unidades"),
        ("Elegir el sistema", "Se quiere leer sin ver las etiquetas de cajas dentro de un camión. ¿Qué sistema sirve?", ["Se necesita leer a distancia.", "La radiofrecuencia lo permite."], "Radiofrecuencia (RFID)"),
    ],
    mistakes=[("Informar el saldo del sistema como si fuera el stock disponible.", "Se promete producto que ya está comprometido.", "Descuenta lo reservado antes de informar."),
              ("Compartir la clave del sistema para «ahorrar tiempo».", "No se sabe quién hizo cada consulta o cambio.", "Cada persona usa su clave personal.")],
    T=[
        ("abc", "En Logística: ¿para qué se comunican los datos de la bodega?", "Para que quienes deciden tengan información correcta y oportuna", "Para llenar informes largos", "Para evitar usar el sistema", "La comunicación sirve para decidir con datos."),
        ("abc", "{F} ¿Qué es la radiofrecuencia (RFID)?", "Etiquetas con chip que se leen por ondas de radio sin verlas", "Líneas impresas que se leen con luz", "Un tipo de papel", "La RFID usa chips que se leen a distancia."),
        ("abc", "{F} ¿Cómo se lee un código de barras?", "Con un lector óptico que lee las líneas impresas", "Con ondas de radio", "A simple vista, sin lector", "El código de barras usa un lector óptico."),
        ("=", "{F} ¿Cuántas unidades del producto A están disponibles para vender?", "150-20", "Disponible = saldo − reservado.", " unidades"),
        ("abc", "{F} El jefe de ventas pregunta cuántas hay. ¿Qué respuesta es la más completa?", "130 disponibles: hay 150 en el sistema y 20 reservadas", "150, porque el sistema lo dice", "Más o menos 100", "Informa el disponible y explica el saldo y lo reservado."),
        ("abc", "{F} ¿Por qué no se informa solo el saldo de 150?", "Porque 20 están comprometidas y se podría prometer producto que no está libre", "Porque el saldo es un secreto", "Porque 150 es un número alto", "El stock disponible descuenta lo reservado."),
        ("=", "En un conteo de ejemplo se esperaban 50 cajas con etiqueta y el lector RFID leyó 48. ¿Cuántas etiquetas no se leyeron?", "50-48", "Diferencia = esperadas − leídas.", " etiquetas"),
        ("abc", "Dos etiquetas no se leyeron en el conteo RFID. ¿Qué es lo más adecuado?", "Revisar las cajas físicamente para ver si falta producto o si la etiqueta está dañada", "Dar por perdidas las cajas", "Ignorar la diferencia", "Una lectura incompleta se verifica con el conteo físico."),
        ("abc", "Un compañero pide la clave de otra persona para entrar al sistema. ¿Qué corresponde?", "Negarse y pedir acceso a la jefatura", "Compartirla si es de confianza", "Compartirla por un rato", "Las claves son personales para saber quién hizo cada consulta."),
        ("abc", "Un informe de existencias incluye teléfonos y direcciones de clientes que no se necesitan. ¿Qué corresponde?", "Sacar esos datos: se comparte solo lo necesario", "Dejarlos por si acaso", "Enviarlo a todos", "La privacidad exige entregar solo los datos necesarios."),
        ("abc", "{F} ¿Qué cualidades tiene un buen dato comunicado?", "Es correcto, claro y oportuno", "Es largo y complicado", "Llega una semana tarde", "Un buen dato permite decidir bien y a tiempo."),
        ("abc", "{F} Si el sistema falla y no se puede consultar, ¿qué es lo más adecuado?", "Avisar al responsable del sistema y usar el kárdex en papel con aviso de que es manual", "Inventar una cifra", "No informar nada ni avisar", "Se informa del problema y se usa el respaldo disponible."),
        ("abc", "{F} Un compañero dice que el lector de código de barras nunca se equivoca. ¿Qué respondes?", "Puede fallar si la etiqueta está dañada, por eso se verifica con el conteo", "Tiene razón, nunca falla", "Solo falla en Navidad", "Los lectores pueden fallar con etiquetas dañadas."),
    ],
    ctx=("abc", "Una bodeguera debe avisar al área de compras que el producto A bajó del mínimo. ¿Qué dato esencial incluye su aviso?", "Producto, saldo disponible, mínimo, fecha y hora", "El color de las cajas", "El nombre del chofer", "Un aviso útil entrega datos claros y la hora de consulta."),
    sc=[
        ("En Logística: ¿cómo se calcula el stock disponible?", "Saldo menos reservado", "Así no se promete producto comprometido."),
        ("¿Cómo se lee la radiofrecuencia?", "Por ondas de radio, sin ver la etiqueta", "Se lee a distancia con un lector."),
        ("¿Qué se cuida al comunicar datos?", "La exactitud y la privacidad", "Solo se comparte con personas autorizadas."),
    ],
    op=("Con la Ficha 39, escribe la respuesta por correo al jefe de ventas en cinco líneas: asunto, saludo, stock disponible con explicación del saldo y lo reservado, la hora de consulta (inventa una) y una advertencia sobre cualquier dato por confirmar.\n{F}",
        "Asunto: Stock disponible del producto A. Hola, Pedro: al corte de las 10:00 hay 130 unidades disponibles del producto A (150 en el sistema, 20 reservadas para un pedido comprometido). Si el conteo físico muestra otra cifra, te avisaré. Saludos, Camila, bodega.",
        ["asunto claro", "stock disponible bien calculado", "explica saldo y reservado", "advierte sobre el dato por confirmar"],
        ["correo de cinco líneas"],
        ["informar 150", "sin hora", "datos personales innecesarios"],
        "Revisa el cálculo. Si informa 150, pide explicar las reservas."),
    reinforce="Explica en papel con tus palabras la diferencia entre código de barras y radiofrecuencia.",
    extend="Explica con un ejemplo inventado qué problema produce un dato desactualizado en el sistema.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 40 (formatos y roles de ejemplo, inventados) de «Distribuidora Andes del Sur». Informe de existencias: producto, ubicación, saldo, reservado, disponible, fecha y hora de consulta, fuente. "
     "Informe de movimientos del día: entradas, salidas y documento de cada una. Alerta de stock mínimo: aviso cuando el saldo baja del mínimo. Formato de mensaje: asunto, datos clave, hora, responsable. "
     "Roles: operador(a) de bodega (captura y registra los datos); jefe(a) de bodega (revisa y comunica); soporte informático (mantiene el sistema); usuarios (ventas y compras, que leen los informes).")
build(
    O4, 2, F,
    use="Aprenderé los informes, las alertas y los formatos de mensaje de la bodega, y los roles de quienes capturan, revisan y usan los datos.",
    prior=["Sé qué es stock disponible.", "Conozco código de barras y RFID.", "Sé redactar un mensaje breve."],
    explain=[
        "La bodega usa informes con una función clara. El informe de existencias muestra cuánto hay de cada producto, dónde está, cuánto está reservado y cuánto queda disponible, con la fecha y hora de la consulta. El informe de movimientos del día lista las entradas y salidas con su documento. La alerta de stock mínimo avisa cuando un saldo baja del mínimo para que se reponga.",
        "Un mensaje de bodega bien escrito lleva un asunto claro, los datos clave, la hora de la consulta y el responsable. Las cifras se acompañan de su fuente (por ejemplo, el sistema o el conteo físico). Los datos sensibles, como información de clientes, se entregan solo a quienes los necesitan.",
        "Cada rol cumple su parte: el operador captura y registra los datos con lectores o a mano; el jefe de bodega revisa y comunica; el soporte informático mantiene el sistema y respalda los datos; los usuarios leen y deciden. Quien detecta un error en un informe lo informa y no lo corrige a escondidas.",
    ],
    vocab=[("informe de existencias", "reporte de lo que hay, dónde y cuánto está disponible"), ("informe de movimientos", "lista de entradas y salidas del día"), ("alerta de stock mínimo", "aviso automático cuando el saldo baja del mínimo"), ("fuente", "origen de un dato"), ("operador", "persona que captura los datos"), ("soporte informático", "equipo que mantiene el sistema")],
    worked=[
        ("Elegir el informe", "Un jefe quiere saber qué salió ayer de la bodega. ¿Qué informe usa?", ["Se trata de movimientos de un día.", "Es el informe de movimientos."], "Informe de movimientos del día"),
        ("Alerta", "El mínimo de un producto ficticio es 30 y el saldo es 25. ¿Se activa la alerta?", ["25 es menor que 30.", "Sí, se activa."], "Sí"),
    ],
    mistakes=[("Enviar cifras sin indicar la fecha y hora.", "No se sabe si el dato sigue vigente.", "Incluye siempre fecha, hora y fuente."),
              ("Corregir un error de un informe sin avisar.", "Nadie sabe qué se cambió ni por qué.", "Informa y deja registro de la corrección.")],
    T=[
        ("abc", "En Logística: ¿qué muestra el informe de existencias?", "Cuánto hay de cada producto, dónde está y cuánto está disponible", "Las ventas del año", "Los sueldos del personal", "El informe de existencias describe el stock y su ubicación."),
        ("abc", "{F} ¿Qué informe lista las entradas y salidas del día?", "El informe de movimientos", "La alerta de stock mínimo", "El informe de existencias", "El informe de movimientos lista cada entrada y salida."),
        ("abc", "{F} ¿Cuándo se activa la alerta de stock mínimo?", "Cuando el saldo baja del mínimo", "Cuando el saldo sube", "Cada día a las 12:00", "La alerta avisa que hay que reponer."),
        ("=", "{F} Un producto de ejemplo tiene saldo 120 y 35 reservadas. ¿Cuántas están disponibles?", "120-35", "Disponible = saldo − reservado.", " unidades"),
        ("abc", "{F} El saldo de un producto es 28 y su mínimo es 30. ¿Qué ocurre?", "Se activa la alerta, porque 28 es menor que 30", "No se activa, porque 28 es alto", "Se borra el producto", "El saldo está bajo el mínimo, entonces corresponde reponer."),
        ("abc", "{F} ¿Qué rol revisa y comunica los datos?", "El jefe o la jefa de bodega", "El proveedor", "El cliente", "Según la ficha, el jefe de bodega revisa y comunica."),
        ("abc", "{F} ¿Quién mantiene el sistema y respalda los datos?", "El soporte informático", "El operador solo", "Ventas", "La ficha asigna esa tarea al soporte informático."),
        ("abc", "{F} ¿Qué datos lleva un informe de existencias?", "Producto, ubicación, saldo, reservado, disponible, fecha y hora, fuente", "Solo el nombre del producto", "El nombre del chofer", "La ficha de formatos lista exactamente esos campos."),
        ("=", "En un informe de movimientos de ejemplo hubo 3 entradas (40, 25 y 15 unidades) y 2 salidas (30 y 20). ¿Cuál fue el movimiento neto del día (entradas − salidas)?", "40+25+15-30-20", "Neto = entradas − salidas.", " unidades"),
        ("abc", "Un informe de existencias llega sin fecha ni hora. ¿Qué problema tiene?", "No se sabe si el dato sigue vigente", "Ninguno, porque las cifras son iguales siempre", "Es más seguro", "La fecha y hora indican cuándo se consultó."),
        ("abc", "Un operador detecta un error en el informe. ¿Qué corresponde?", "Informar al jefe de bodega y dejar registro de la corrección", "Corregirlo sin avisar", "Ignorarlo", "Los errores se informan y se corrigen con trazabilidad."),
        ("abc", "Ventas pide el informe con los nombres de los clientes de cada pedido. ¿Qué corresponde?", "Entregar solo lo necesario y consultar a la jefatura si incluye datos de clientes", "Entregar todo sin revisar", "Publicarlo", "Los datos de clientes se entregan solo cuando hay necesidad y autorización."),
        ("abc", "{F} Una alerta se activa un domingo y nadie la lee hasta el lunes. ¿Qué puede ocurrir?", "Se demora la reposición y puede faltar producto", "Nada, porque el producto se repone solo", "El producto se vence", "Una alerta sin responsable atrasa la decisión de reponer."),
    ],
    ctx=("abc", "Compras pregunta qué productos están bajo el mínimo hoy. ¿Qué informe o aviso le sirve?", "La alerta de stock mínimo o el informe de existencias con la columna de saldo", "El informe de sueldos", "El horario de atención", "Estos informes muestran qué productos están bajo el mínimo."),
    sc=[
        ("En Logística: ¿qué incluye un buen mensaje de bodega?", "Asunto claro, datos clave, hora y responsable", "Eso lo hace claro y verificable."),
        ("¿Qué hace un operador al detectar un error?", "Lo informa y deja registro", "No corrige a escondidas: informa lo que detecta."),
        ("¿Para qué sirve la alerta de stock mínimo?", "Para avisar que hay que reponer", "Así se evita quedarse sin producto para vender."),
    ],
    op=("Con la Ficha 40, arma un informe de existencias de ejemplo con tres productos que inventes (producto, ubicación, saldo, reservado, disponible) y una alerta para el que esté bajo el mínimo, indicando la fecha y la hora de consulta y la fuente.\n{F}",
        "Consulta: 3 de abril, 10:00, sistema. Producto A, Z1-E2-N1, saldo 120, reservado 20, disponible 100. Producto B, Z2-E1-N2, saldo 28, reservado 0, disponible 28, mínimo 30: ALERTA. Producto C, Z3-E4-N1, saldo 60, reservado 10, disponible 50.",
        ["calcula el disponible de cada producto", "activa la alerta correcta", "incluye fecha, hora y fuente"],
        ["informe de existencias con tres productos y una alerta"],
        ["no restar lo reservado", "alerta sin explicar", "sin fecha ni fuente"],
        "Rehace el disponible de cada producto. Si falta la fuente, pide agregarla."),
    reinforce="Escribe en papel un informe de movimientos de un día con tres entradas y dos salidas inventadas.",
    extend="Explica con un ejemplo inventado por qué el soporte informático es parte del control de existencias.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 41 (caso de ejemplo, inventado) de «Distribuidora Andes del Sur». Conteo con lector de radiofrecuencia (RFID) de tres productos. Producto P1: sistema 50, lectura 48. Producto P2: sistema 30, lectura 30. Producto P3: sistema 20, lectura 21. "
     "Informe enviado ayer a las 18:00 por un operador: «Todo cuadra». Hoy el jefe de ventas escribe: «El informe de ayer no coincide con el conteo de hoy». Causas posibles de una diferencia de lectura: etiqueta dañada, caja mal ubicada, lectura incompleta, error de registro.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un informe con datos que no coinciden, buscar la causa y redactar un mensaje claro y honesto a la persona que lo necesita.",
    prior=["Conozco los informes de bodega.", "Sé calcular diferencias.", "Sé qué es una etiqueta RFID."],
    explain=[
        "Cuando un informe no coincide con un conteo, se compara cifra por cifra: diferencia = sistema − lectura. Se registran las diferencias, se clasifican (falta o sobra) y se busca la causa en el orden más probable: error de lectura, producto mal ubicado, error de registro o diferencia real de stock. Antes de afirmar una causa se verifica con un conteo físico o con los documentos.",
        "El mensaje al usuario debe ser honesto, claro y breve: qué se encontró, qué cifras, qué se hará para verificar y cuándo se informará de nuevo. No se dice «todo cuadra» si hay diferencias. No se culpa a una persona sin evidencia; se describen los hechos.",
        "El mensaje incluye la fecha y hora del conteo, la fuente, las diferencias y un plazo para el próximo aviso. Las cifras provisorias se marcan como tales hasta confirmarlas.",
    ],
    vocab=[("lectura", "cantidad detectada por el lector"), ("diferencia", "sistema menos lectura"), ("causa posible", "explicación que aún debe verificarse"), ("dato provisorio", "cifra aún por confirmar"), ("verificar", "comprobar con otra fuente"), ("plazo", "momento comprometido para informar")],
    worked=[
        ("Diferencia de lectura", "Un producto ficticio muestra sistema 40 y lectura 37. ¿Cuál es la diferencia y qué indica?", ["Diferencia = 40 − 37 = 3.", "El lector detectó 3 menos que el sistema."], "3 de menos en la lectura"),
        ("Mensaje honesto", "Un operador ficticio escribe «Todo bien» aunque hay 3 de diferencia. ¿Qué falla?", ["Oculta una diferencia conocida.", "Corresponde informar la diferencia y cómo se verificará."], "Oculta la diferencia"),
    ],
    mistakes=[("Escribir «todo cuadra» sin comparar cifra por cifra.", "Puede haber diferencias no detectadas.", "Compara cada producto antes de afirmar."),
              ("Afirmar una causa sin verificar.", "Puede ser otra y el problema seguirá.", "Verifica con conteo físico o documentos.")],
    T=[
        ("abc", "En Logística: ¿cómo se calcula la diferencia de lectura?", "Sistema menos lectura", "Sistema más lectura", "Lectura por sistema", "La resta muestra cuánto difieren ambos datos."),
        ("=", "{F} ¿Cuál es la diferencia del producto P1?", "50-48", "Diferencia = sistema − lectura.", " unidades"),
        ("=", "{F} ¿Cuál es la diferencia del producto P3 (sistema − lectura)?", "20-21", "El resultado negativo indica que el lector detectó más que el sistema.", " unidades"),
        ("abc", "{F} ¿Qué productos coinciden?", "Solo el P2", "El P1 y el P3", "Ninguno", "El P2 tiene sistema y lectura iguales."),
        ("abc", "{F} Con el conteo de hoy, ¿se puede afirmar «Todo cuadra»?", "No, porque hay diferencias en P1 y P3", "Sí, porque P2 coincide", "Sí, porque las diferencias son pequeñas", "El conteo muestra diferencias en P1 y P3; decir que todo cuadra las oculta."),
        ("abc", "{F} En P3, ¿qué sugiere una lectura mayor que el sistema?", "Una entrada no registrada o una lectura doble, por verificar", "Que el lector nunca se equivoca", "Que el producto se multiplicó", "Se debe verificar con conteo físico y documentos."),
        ("abc", "{F} En P1, la lectura de 48 puede deberse a:", "Etiquetas dañadas, cajas mal ubicadas o faltantes reales, por verificar", "Que el producto se evaporó", "Que 50 es un número mágico", "Son causas posibles que se comprueban."),
        ("=", "{F} Si de las 2 etiquetas de P1 no leídas se encuentran 2 dañadas en cajas presentes, ¿cuántas cajas leídas más las dañadas hay?", "48+2", "Se suman las leídas y las dañadas halladas.", " cajas"),
        ("abc", "{F} Con ese hallazgo, ¿cuál es la diferencia real de P1?", "Cero, porque aparecieron las 50 cajas", "2 de menos", "2 de más", "Con las 2 cajas halladas el total coincide con el sistema."),
        ("abc", "{F} Un compañero dice que el operador mintió en el informe de ayer. ¿Qué respondes?", "No hay evidencia: se describen los hechos y se verifica", "Tiene razón, hay que sancionarlo", "No importa", "No se acusa a nadie sin tener evidencia."),
        ("abc", "{F} ¿Qué incluye un buen mensaje al jefe de ventas?", "Las diferencias halladas, cómo se verificarán y cuándo se informará", "Solo «Todo en orden»", "Solo disculpas", "El mensaje debe ser claro y honesto."),
        ("abc", "{F} ¿Cómo se marca la cifra de P3 mientras no se verifique?", "Como dato provisorio", "Como cifra definitiva", "No se marca", "Una cifra por confirmar se declara provisoria."),
        ("abc", "{F} Una persona de ventas pide detener un despacho de P1 hasta verificar. ¿Qué es lo más adecuado?", "Coordinar con la jefatura de bodega y confirmar el stock disponible antes de despachar", "Despachar sin avisar", "Cancelar todo", "La decisión se coordina con la jefatura con datos verificados."),
    ],
    ctx=("abc", "Una operadora debe responder al jefe de ventas. ¿Cuál es el mejor inicio de su mensaje?", "«El conteo de hoy muestra diferencias en dos productos; verificaremos y te informaré a las 16:00»", "«No pasa nada»", "«Fue culpa de quien contó ayer»", "Un buen inicio informa el hecho y el plazo."),
    sc=[
        ("En Logística: ¿qué se hace antes de afirmar una causa?", "Verificarla con conteo físico o documentos", "Una causa no verificada puede ser errónea."),
        ("¿Cómo se marca una cifra por confirmar?", "Como provisoria", "Así se evita que se tome por definitiva."),
        ("¿Se oculta una diferencia conocida?", "No, se informa", "La honestidad es parte del trabajo."),
    ],
    op=("Con la Ficha 41, escribe un mensaje de cinco líneas para el jefe de ventas: asunto, las diferencias de cada producto, la causa posible de cada una (sin afirmarla), cómo se verificará y a qué hora darás el próximo aviso.\n{F}",
        "Asunto: Diferencias en el conteo de hoy. P1: sistema 50, lectura 48 (2 menos); puede haber etiquetas dañadas o cajas mal ubicadas. P3: sistema 20, lectura 21 (1 más); posible entrada no registrada. P2 coincide. Verificaré con conteo físico y documentos y te aviso a las 16:00. Cifras provisorias.",
        ["compara producto por producto", "menciona causas posibles sin afirmarlas", "indica verificación y plazo"],
        ["mensaje de cinco líneas"],
        ["decir «todo cuadra»", "culpar a una persona", "sin plazo"],
        "Revisa cada diferencia. Si afirma una causa, pide marcarla como posible."),
    reinforce="Compara en papel las cifras de dos informes ficticios y marca cuáles coinciden.",
    extend="Explica con un ejemplo inventado por qué es mejor avisar pronto de una diferencia.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 42 (datos de ejemplo, inventados) de «Distribuidora Andes del Sur», al corte de las 10:00 del 3 de abril. Producto 1: saldo 200, reservado 50, mínimo 60. Producto 2: saldo 90, reservado 40, mínimo 60. Producto 3: saldo 150, reservado 0, mínimo 40. "
     "Producto 4: saldo 75, reservado 10, mínimo 70. Conteo físico de control de los productos 1 y 2: producto 1, 200; producto 2, 88. Responsable de la consulta: operador Mateo. Destinatario: jefe de compras.")
build(
    O4, 4, F,
    use="Aprenderé a armar un informe de existencias con datos, a detectar alertas, a medir la exactitud y a redactar un mensaje breve para el jefe de compras.",
    prior=["Conozco los informes y la alerta de stock mínimo.", "Sé calcular el disponible y diferencias.", "Sé redactar un mensaje claro."],
    explain=[
        "Un informe de existencias se arma con tres cálculos por producto: disponible (saldo − reservado), alerta (si el disponible es menor que el mínimo) y diferencia con el conteo físico de control (saldo − conteo). Se agrega la fecha, la hora y la fuente. La exactitud del control es el número de productos sin diferencia × 100 ÷ el número de productos controlados.",
        "Luego se redacta el mensaje: asunto claro, resumen en una o dos líneas (cuántos productos están bajo el mínimo y cuáles), las diferencias de control y la acción pedida o propuesta. Se marcan como provisorias las cifras en revisión.",
        "Los datos se entregan solo a quien corresponde, con la clave personal del responsable de la consulta. El informe no incluye datos de clientes. Cualquier decisión de compra la autoriza la jefatura.",
    ],
    vocab=[("disponible", "saldo menos reservado"), ("alerta", "aviso porque el disponible está bajo el mínimo"), ("conteo de control", "recuento físico para verificar el sistema"), ("exactitud del control", "productos sin diferencia × 100 ÷ controlados"), ("resumen", "frase breve con lo principal"), ("responsable de la consulta", "persona que obtuvo los datos")],
    worked=[
        ("Alerta", "Un producto ficticio tiene saldo 80, reservado 30 y mínimo 40. ¿Hay alerta?", ["Disponible = 80 − 30 = 50.", "50 es mayor que 40: no hay alerta."], "No hay alerta"),
        ("Exactitud", "En un control ficticio de 4 productos, 3 no tienen diferencia. ¿Qué exactitud hay?", ["3 × 100 ÷ 4 = 75.", "El resultado se expresa en porcentaje del total."], "75 %"),
    ],
    mistakes=[("Comparar el saldo (y no el disponible) con el mínimo.", "Puede ocultar una alerta real.", "Compara siempre el disponible con el mínimo."),
              ("Mandar el informe sin indicar la hora de la consulta.", "No se sabe si los datos están vigentes.", "Incluye fecha, hora y fuente.")],
    T=[
        ("abc", "En Logística: ¿qué se compara con el mínimo para decidir una alerta?", "El disponible", "El saldo", "El reservado", "El disponible es lo realmente libre para usar."),
        ("=", "{F} ¿Cuántas unidades disponibles tiene el producto 1?", "200-50", "Disponible = saldo − reservado.", " unidades"),
        ("=", "{F} ¿Cuántas unidades disponibles tiene el producto 2?", "90-40", "Disponible = saldo − reservado.", " unidades"),
        ("=", "{F} ¿Cuántas unidades disponibles tiene el producto 3?", "150-0", "Sin reservas, el disponible es igual al saldo.", " unidades"),
        ("=", "{F} ¿Cuántas unidades disponibles tiene el producto 4?", "75-10", "Disponible = saldo − reservado.", " unidades"),
        ("abc", "{F} ¿Qué productos tienen alerta, es decir, disponible menor que el mínimo?", "El 2 y el 4", "El 1 y el 3", "Solo el 1", "El 2 tiene 50 de 60 y el 4 tiene 65 de 70."),
        ("abc", "{F} ¿El producto 1 tiene alerta?", "No, porque su disponible de 150 supera el mínimo de 60", "Sí, porque su saldo es alto", "Sí, porque su reservado es alto", "El disponible de 150 es mayor que el mínimo de 60."),
        ("=", "{F} ¿Cuál es la diferencia de control del producto 2 (saldo − conteo físico)?", "90-88", "Diferencia = saldo del sistema − conteo.", " unidades"),
        ("=", "{F} ¿Cuál es la exactitud del control de los dos productos controlados?", "1*100//2", "Exactitud = productos sin diferencia × 100 ÷ controlados.", " %"),
        ("abc", "{F} ¿Qué debe señalar el mensaje sobre el producto 2?", "Que tiene alerta y una diferencia de 2 unidades por verificar", "Que todo está bien", "Que no existe", "Es el único producto con alerta y diferencia a la vez."),
        ("abc", "{F} ¿A quién se entrega el informe?", "Al jefe de compras", "A un cliente", "A cualquier persona", "El destinatario es el que indica la ficha."),
        ("abc", "{F} ¿Qué cuidado de privacidad se aplica al informe?", "No incluir datos de clientes y entregarlo solo al destinatario autorizado", "Publicarlo en un lugar visible", "Enviarlo a todos", "El informe de existencias no necesita datos de clientes."),
        ("abc", "{F} ¿Quién autoriza las compras de reposición?", "La jefatura", "El operador", "El proveedor", "El informe propone; la jefatura decide."),
    ],
    ctx=("abc", "El jefe de compras pregunta qué debe reponer hoy. ¿Qué responde un buen mensaje?", "Productos 2 y 4 con disponible bajo el mínimo; el 2 tiene además 2 unidades por verificar", "Todo está bien", "Debes reponer los cuatro", "El mensaje identifica alertas y diferencias."),
    sc=[
        ("En Logística: ¿cómo se calcula el disponible?", "Saldo menos reservado", "Es la cantidad que realmente está libre para usar."),
        ("¿Qué indica una alerta?", "Que el disponible está bajo el mínimo", "En ese caso corresponde proponer una reposición a la jefatura."),
        ("¿Qué datos no se incluyen en el informe?", "Datos de clientes", "No son necesarios y son reservados."),
    ],
    op=("Con la Ficha 42, escribe el informe y el mensaje al jefe de compras: tabla con disponible y alerta de cada producto, diferencias de control, exactitud, un resumen de dos líneas, fecha y hora, y la acción que propones.\n{F}",
        "Corte: 3 de abril, 10:00, sistema; consulta de Mateo. Producto 1: disponible 150, sin alerta. Producto 2: disponible 50, alerta; diferencia de control de 2. Producto 3: disponible 150, sin alerta. Producto 4: disponible 65, alerta. Exactitud del control: 50 %. Resumen: hay 2 productos bajo el mínimo (2 y 4). Propongo reponer ambos, sujeto a tu autorización.",
        ["calcula disponible y alertas", "calcula diferencia y exactitud", "redacta un resumen", "propone sin decidir por la jefatura"],
        ["tabla, resumen y propuesta"],
        ["usar saldo en vez de disponible", "olvidar la hora", "incluir datos de clientes"],
        "Rehace los cálculos. Si usa el saldo, pide corregir con el disponible."),
    reinforce="Calcula en papel el disponible y la alerta de cuatro productos que inventes.",
    extend="Explica con un ejemplo inventado cómo se vería un informe si el sistema estuviera desactualizado.",
)

# ============================================================ OAM-05, clase 1
F = ("Ficha 43 (caso de ejemplo, inventado) de la zona de andén de carga de «Distribuidora Andes del Sur». Observaciones de un día de ejemplo: cajas apiladas hasta tapar un extintor; un derrame de líquido de un envase en el piso, sin señal; "
     "una persona sin el calzado de seguridad que la empresa exige para la zona de carga; una salida de emergencia con cajas delante; un envase con la rotulación de sustancia peligrosa dañada e ilegible.")
build(
    O5, 1, F,
    use="Aprenderé qué son peligro, riesgo y accidente laboral, las normas básicas de seguridad en zonas de almacenamiento y distribución y por qué las condiciones inseguras se avisan.",
    prior=["Sé qué es una zona de almacenamiento.", "Sé qué es una señal de seguridad.", "Sé que hay normas que se consultan."],
    explain=[
        "Un peligro es algo que puede causar daño, como una caja que puede caer. El riesgo es la probabilidad de que ese daño ocurra y su gravedad. Un accidente laboral es un hecho ocurrido por el trabajo que produce lesión. Prevenir significa actuar antes para evitarlos: eliminar o reducir el peligro, señalizar y usar elementos de protección.",
        "Las normas básicas de seguridad en zonas de almacenamiento y distribución incluyen mantener el orden y el aseo, dejar despejados los pasillos y las salidas de emergencia, no tapar equipos de emergencia como extintores, respetar la señalética, usar los elementos de protección que exige la empresa y mantener visibles las rotulaciones de las sustancias peligrosas. La norma vigente y la persona responsable de prevención de riesgos fijan las reglas concretas.",
        "Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar. Ante una condición insegura se avisa de inmediato a la persona responsable; nadie debe intentar resolver por su cuenta lo que supera su capacitación, como limpiar un derrame de una sustancia que no conoce.",
    ],
    vocab=[("peligro", "algo que puede causar daño"), ("riesgo", "probabilidad y gravedad de un daño"), ("accidente laboral", "hecho del trabajo que causa lesión"), ("prevención", "acciones para evitar accidentes"), ("elemento de protección", "equipo que protege a la persona, como el calzado de seguridad"), ("condición insegura", "situación del lugar que puede causar un accidente")],
    worked=[
        ("Peligro y riesgo", "Una caja pesada está sobre el borde de un estante alto de una bodega ficticia. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es que la caja puede caer.", "El riesgo es que alguien sea golpeado, con consecuencias graves."], "Peligro: caída de la caja; riesgo: golpe a una persona"),
        ("Condición insegura", "Un pasillo de una bodega ficticia está bloqueado con cajas. ¿Qué es y qué se hace?", ["Es una condición insegura del lugar.", "Se avisa y se despeja."], "Condición insegura; se avisa y se despeja"),
    ],
    mistakes=[("Tapar un extintor con cajas para ganar espacio.", "En una emergencia no se podrá usar a tiempo.", "Mantén los equipos de emergencia visibles y accesibles."),
              ("Intentar limpiar un derrame sin saber qué sustancia es.", "Puede haber riesgos para la salud.", "Aleja a las personas, señaliza y avisa al responsable.")],
    T=[
        ("abc", "En Logística: ¿qué es un peligro?", "Algo que puede causar daño", "La probabilidad de que algo ocurra", "Un accidente que ya pasó", "El peligro es la fuente del daño; el riesgo es la probabilidad."),
        ("abc", "{F} ¿Qué condición insegura aparece por las cajas que tapan el extintor?", "El equipo de emergencia queda inaccesible", "Sobra espacio", "Se ve más ordenado", "En una emergencia el extintor debe poder alcanzarse."),
        ("abc", "{F} ¿Qué debe hacerse con la salida de emergencia con cajas delante?", "Despejarla y mantenerla libre", "Dejarla si pasa una persona", "Usarla para guardar cajas", "Las salidas de emergencia deben permanecer libres."),
        ("abc", "{F} ¿Qué es lo más adecuado ante el derrame de líquido sin señal?", "Alejarse, señalizar si es seguro y avisar al responsable", "Limpiarlo sin saber qué es", "Pasar por encima", "No se enfrenta lo que se desconoce; se avisa."),
        ("abc", "{F} ¿Qué falla muestra la persona sin calzado de seguridad en la zona de carga?", "No usa el elemento de protección que la empresa exige", "Usa un calzado demasiado cómodo", "Llega temprano", "El elemento de protección es parte de las normas."),
        ("abc", "{F} ¿Qué problema genera el envase con la rotulación dañada?", "No se sabe qué sustancia contiene ni qué riesgos tiene", "Se gasta más espacio", "Es más pesado", "La rotulación informa los peligros y debe ser legible."),
        ("=", "{F} Se observan 5 condiciones inseguras en la zona. Si se corrigen 3, ¿cuántas quedan pendientes?", "5-3", "Pendientes = observadas − corregidas.", " condiciones"),
        ("abc", "¿Quién fija las reglas concretas de seguridad de una bodega?", "La norma vigente y la persona responsable de prevención de riesgos", "Cada trabajador según su gusto", "Los clientes", "Las reglas concretas se consultan en la norma y con el responsable."),
        ("abc", "Un compañero dice que no hay que avisar de una condición insegura si no ha pasado nada. ¿Qué respondes?", "Se avisa antes de que ocurra un accidente", "Tiene razón, se espera a que pase algo", "Se avisa solo a un amigo", "La prevención actúa antes del daño."),
        ("abc", "Una persona nueva debe mover un equipo pesado que no sabe operar. ¿Qué es lo más adecuado?", "Decir que no está capacitada y pedir que lo haga una persona autorizada", "Intentarlo para no quedar mal", "Pedir que alguien le explique en un minuto", "Solo quien está capacitada y autorizada opera el equipo."),
        ("abc", "{F} ¿Qué condición de la ficha es más urgente de resolver por riesgo de daño inmediato?", "La salida de emergencia bloqueada y el derrame sin señal", "El orden de las etiquetas", "El color del piso", "Ambas condiciones pueden causar daño inmediato a las personas."),
        ("abc", "El encargado de prevención pide un registro de condiciones inseguras. ¿Qué debe anotar un trabajador?", "Qué ve, dónde, cuándo y quién avisa", "Su opinión sobre sus compañeros", "El nombre del cliente", "El registro debe describir solo hechos que se puedan verificar."),
        ("abc", "{F} Un compañero quita la cinta de peligro del derrame porque «ya se secó». ¿Qué corresponde?", "Dejarla hasta que el responsable revise y autorice retirarla", "Quitarla", "Taparla con cajas", "Solo el responsable autoriza retirar una señal de peligro."),
    ],
    ctx=("abc", "En una inspección se detecta una caja que sobresale de un estante a la altura de la cabeza. ¿Qué es lo más adecuado?", "Avisar al responsable y señalizar la zona hasta que se corrija", "Dejarla porque nadie se ha golpeado", "Taparla con papel", "Se previene avisando y señalizando antes del golpe."),
    sc=[
        ("En Logística: ¿qué es un riesgo?", "La probabilidad y la gravedad de un daño", "El riesgo mide qué tan probable y grave es el daño."),
        ("¿Qué haces ante una condición insegura?", "Aviso al responsable de inmediato", "La prevención actúa antes del accidente."),
        ("¿Qué mantienes siempre libre?", "Los pasillos y las salidas de emergencia", "Son necesarios para evacuar y circular."),
    ],
    op=("Con la Ficha 43, escribe un parte de cinco líneas para el responsable de prevención: las cinco condiciones inseguras, cuál es la más urgente y por qué, qué señalizarías si es seguro hacerlo y a quién avisarías. Recuerda que este cuaderno no te habilita para trabajar.\n{F}",
        "Condiciones: extintor tapado, derrame sin señal, calzado inadecuado, salida de emergencia bloqueada y rotulación dañada. Más urgentes: el derrame y la salida bloqueada, por riesgo inmediato. Señalizaría el derrame si es seguro. Aviso al responsable de prevención y a la jefatura.",
        ["identifica las cinco condiciones", "prioriza con razón", "no propone enfrentar peligros sin capacitación", "indica a quién avisar"],
        ["parte de cinco líneas"],
        ["limpiar sustancias desconocidas", "ocultar condiciones", "no avisar"],
        "Revisa que ninguna acción exija enfrentar un peligro sin capacitación. Si falta avisar, pide agregarlo."),
    reinforce="Escribe en papel tres condiciones inseguras de un lugar ficticio y qué se avisaría.",
    extend="Explica con un ejemplo inventado cómo un aviso a tiempo evita un accidente.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 44 (conceptos de ejemplo, inventados) de «Distribuidora Andes del Sur». Señalética: prohibición (círculo rojo con una barra); advertencia (triángulo amarillo); obligación (círculo azul); seguridad o salida de emergencia (verde). "
     "Elementos de protección personal (EPP): calzado de seguridad, guantes, casco, lentes de seguridad y protección auditiva, según lo que indique la norma vigente y la empresa para cada tarea. "
     "Hoja de datos de seguridad (HDS): documento del fabricante que informa los peligros de una sustancia y las precauciones. Roles: trabajador(a), supervisor(a), encargado(a) de prevención de riesgos. Registro: parte de condición insegura y parte de incidente.")
build(
    O5, 2, F,
    use="Aprenderé la señalética básica, los elementos de protección personal, la hoja de datos de seguridad y los roles de la prevención en una bodega.",
    prior=["Sé qué es un riesgo y una condición insegura.", "Sé que hay normas que se consultan.", "Sé leer un cartel."],
    explain=[
        "La señalética usa formas y colores para avisar: las señales de prohibición son un círculo rojo con una barra (por ejemplo, prohibido el paso); las de advertencia son un triángulo amarillo (cuidado, peligro); las de obligación son un círculo azul (uso obligatorio de un elemento de protección); y las de seguridad o salida de emergencia son verdes. Se respetan siempre, aunque el lugar sea conocido.",
        "Los elementos de protección personal (EPP) protegen a la persona de un peligro que no se pudo eliminar: calzado de seguridad, guantes, casco, lentes y protección auditiva, según lo que indiquen la norma vigente y la empresa para cada tarea. La hoja de datos de seguridad (HDS) es un documento del fabricante que informa los peligros de una sustancia y las precauciones. Se consulta antes de almacenar o manejar una sustancia.",
        "Los roles se reparten: el trabajador cumple las reglas y avisa de lo inseguro; el supervisor organiza el trabajo y corrige; el encargado de prevención de riesgos asesora y revisa. Un parte de condición insegura describe un riesgo observado; un parte de incidente describe un hecho que pudo causar daño o lo causó. Esto es aprendizaje conceptual en papel: practicar esta tarea exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar.",
    ],
    vocab=[("señalética", "conjunto de señales de seguridad"), ("EPP", "elementos de protección personal"), ("HDS", "hoja de datos de seguridad de una sustancia"), ("señal de obligación", "círculo azul que ordena usar algo"), ("parte de incidente", "informe de un hecho que pudo causar daño"), ("encargado de prevención", "persona que asesora la seguridad")],
    worked=[
        ("Leer una señal", "Un cartel ficticio es un triángulo amarillo con un signo de exclamación. ¿Qué tipo de señal es?", ["La forma triangular amarilla es de advertencia.", "Avisa que hay un peligro."], "Advertencia"),
        ("Elegir quién avisa", "Un trabajador ve un cable pelado en una bodega ficticia. ¿Qué rol cumple al avisar?", ["Cumple la regla de avisar lo inseguro.", "Avisa al supervisor o al encargado de prevención."], "Trabajador que avisa"),
    ],
    mistakes=[("Ignorar una señal porque «ya conozco el lugar».", "Las condiciones cambian y la señal avisa del riesgo actual.", "Respeta siempre la señalética."),
              ("Manejar una sustancia sin leer su HDS.", "No se conocen sus peligros ni las precauciones.", "Consulta la HDS y pregunta al responsable.")],
    T=[
        ("abc", "En Logística: ¿qué indica un círculo azul?", "Una obligación, como usar un elemento de protección", "Una prohibición", "Una salida de emergencia", "El círculo azul es una señal de obligación."),
        ("abc", "{F} ¿De qué color es la señal de salida de emergencia?", "Verde", "Rojo", "Amarillo", "La ficha indica verde para seguridad y salida."),
        ("abc", "{F} ¿Qué indica un triángulo amarillo?", "Advertencia de peligro", "Prohibición", "Obligación", "El triángulo amarillo advierte un peligro."),
        ("abc", "{F} ¿Qué indica un círculo rojo con una barra?", "Una prohibición", "Una obligación", "Una salida", "El círculo rojo con barra prohíbe una acción."),
        ("abc", "{F} ¿Qué es la HDS?", "Un documento del fabricante con los peligros y precauciones de una sustancia", "Un tipo de casco", "Un horario de turnos", "La HDS informa los peligros de una sustancia."),
        ("abc", "{F} ¿Quién asesora y revisa la prevención de riesgos?", "El encargado de prevención de riesgos", "El cliente", "El proveedor", "Según la ficha, ese rol asesora y revisa."),
        ("abc", "¿Para qué sirve un EPP?", "Para proteger a la persona de un peligro que no se pudo eliminar", "Para reemplazar la prevención", "Para decorar el uniforme", "El EPP protege cuando el peligro no se elimina."),
        ("=", "Un registro de ejemplo tiene 12 partes de condición insegura; 9 fueron resueltos. ¿Cuántos faltan por resolver?", "12-9", "Pendientes = totales − resueltos.", " partes"),
        ("=", "De esos 12 partes de ejemplo, 9 fueron resueltos. ¿Qué porcentaje fue resuelto (parte entera)?", "9*100//12", "Porcentaje = resueltos × 100 ÷ totales.", " %"),
        ("abc", "{F} Un trabajador ve la señal de obligación de usar lentes de seguridad y decide no usarlos «porque va a tardar poco». ¿Qué falla?", "No cumple una señal de obligación", "Nada, porque tarda poco", "Usa demasiados lentes", "Las señales de seguridad se cumplen siempre y sin excepciones."),
        ("abc", "{F} Un supervisor ve un envase sin rotulación legible. ¿Qué es lo más adecuado?", "Apartar la zona si es seguro, no manipularlo y avisar al encargado de prevención", "Manipularlo para leer la etiqueta", "Mezclarlo con otros", "Un envase sin información se trata como desconocido y se avisa."),
        ("abc", "{F} ¿Cuál es la diferencia entre un parte de condición insegura y uno de incidente?", "El primero describe un riesgo observado; el segundo, un hecho que pudo causar o causó daño", "Son lo mismo", "El primero es de clientes", "Describen cosas distintas y se usan en momentos distintos."),
        ("abc", "{F} Un compañero pide quitar un cartel de advertencia porque «afea la bodega». ¿Qué respondes?", "La señal avisa de un riesgo y no se retira sin autorización", "Tiene razón, afea", "Se debe pintar de otro color", "Las señales solo las retira quien corresponda cuando el riesgo ya no existe."),
    ],
    ctx=("abc", "Una persona nueva llega a una zona con un círculo azul que muestra un casco. ¿Qué debe hacer?", "Usar el casco que exige la señal antes de entrar", "Entrar sin casco porque va rápido", "Pedir permiso para no usarlo", "La señal de obligación se cumple siempre."),
    sc=[
        ("En Logística: ¿qué forma y color tiene una señal de advertencia?", "Triángulo amarillo", "Así se reconoce un aviso de peligro."),
        ("¿Para qué sirve la HDS?", "Para conocer los peligros de una sustancia y sus precauciones", "Se consulta antes de almacenar o manejar."),
        ("¿Qué haces ante un envase sin rotulación legible?", "Aviso y no lo manipulo", "Un desconocido se trata con precaución."),
    ],
    op=("Con la Ficha 44, escribe una tabla de cinco filas con Señal o documento, Qué indica y Qué debe hacer la persona: círculo rojo con barra, triángulo amarillo, círculo azul, salida verde y HDS.\n{F}",
        "Círculo rojo con barra: prohibición; no hacer lo prohibido. Triángulo amarillo: advertencia; tener precaución. Círculo azul: obligación; usar el elemento de protección. Verde: seguridad o salida; mantener el acceso libre. HDS: peligros y precauciones; consultarla antes de manejar una sustancia.",
        ["identifica bien cada señal", "indica la conducta correcta", "incluye la HDS"],
        ["tabla de cinco filas"],
        ["confundir advertencia y prohibición", "no incluir la conducta", "omitir la HDS"],
        "Compara con la ficha. Si confunde formas y colores, pide revisar la explicación."),
    reinforce="Dibuja en papel las cuatro señales de la ficha y escribe qué indica cada una.",
    extend="Explica con un ejemplo inventado por qué el EPP no reemplaza a la prevención.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 45 (caso de ejemplo, inventado) de una inspección en papel de la zona de almacenamiento de «Distribuidora Andes del Sur». Se anotan hallazgos con dos valores de ejemplo de 1 a 3: probabilidad (1 baja, 2 media, 3 alta) y gravedad (1 leve, 2 media, 3 grave). "
     "Prioridad = probabilidad × gravedad. Hallazgo 1: cajas en el borde de un estante alto (probabilidad 2, gravedad 3). Hallazgo 2: cable de una extensión cruzando un pasillo (probabilidad 3, gravedad 2). "
     "Hallazgo 3: señal de salida de emergencia despintada (probabilidad 1, gravedad 3). Hallazgo 4: estante con un rótulo de capacidad de carga ilegible (probabilidad 2, gravedad 2). Hallazgo 5: papel suelto en el piso (probabilidad 2, gravedad 1).")
build(
    O5, 3, F,
    use="Aprenderé a analizar una inspección en papel: describir hallazgos, calcular su prioridad con un método simple de ejemplo y proponer acciones sin enfrentar peligros por cuenta propia.",
    prior=["Conozco la señalética y los EPP.", "Sé qué es una condición insegura.", "Sé multiplicar."],
    explain=[
        "Una inspección revisa un lugar para encontrar condiciones inseguras. Cada hallazgo se describe con hechos: qué se vio, dónde y cuándo. Para decidir qué atender primero se puede usar un método simple: se asigna un valor a la probabilidad de que ocurra un daño y otro a su gravedad, y la prioridad es el producto de ambos. A mayor prioridad, más urgente la acción. Los valores de este cuaderno son de ejemplo.",
        "Después se propone una acción por hallazgo: corregir la condición, señalizar mientras se corrige y avisar al responsable. Las acciones son generales y se ejecutan solo por personas autorizadas y capacitadas; el trabajador que detecta el hallazgo avisa y no actúa fuera de su capacitación.",
        "La inspección se cierra con un registro: lista de hallazgos con su prioridad, responsable de la corrección y plazo, que fija la jefatura. Esto es aprendizaje conceptual en papel: practicar inspecciones exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar.",
    ],
    vocab=[("inspección", "revisión de un lugar para hallar condiciones inseguras"), ("hallazgo", "condición insegura encontrada"), ("probabilidad", "qué tan posible es que ocurra el daño"), ("gravedad", "qué tan serio sería el daño"), ("prioridad", "producto de probabilidad por gravedad"), ("plazo", "tiempo para corregir")],
    worked=[
        ("Calcular prioridad", "Un hallazgo ficticio tiene probabilidad 3 y gravedad 2. ¿Cuál es su prioridad?", ["Prioridad = 3 × 2.", "Resulta 6."], "6"),
        ("Comparar", "Un hallazgo ficticio de prioridad 6 y otro de prioridad 3. ¿Cuál se atiende primero?", ["A mayor prioridad, más urgente.", "El de 6."], "El de prioridad 6"),
    ],
    mistakes=[("Describir un hallazgo con una opinión («la bodega es un desorden»).", "No es verificable ni indica qué corregir.", "Describe hechos: qué, dónde y cuándo."),
              ("Arreglar por cuenta propia una instalación eléctrica detectada en la inspección.", "Puede causar un accidente grave.", "Avisa al responsable y a una persona autorizada.")],
    T=[
        ("abc", "En Logística: ¿cómo se calcula la prioridad con el método de ejemplo?", "Probabilidad por gravedad", "Probabilidad más gravedad", "Gravedad menos probabilidad", "La prioridad de ejemplo es el producto de ambos valores."),
        ("=", "{F} ¿Cuál es la prioridad del hallazgo 1?", "2*3", "Prioridad = probabilidad × gravedad.", " puntos"),
        ("=", "{F} ¿Cuál es la prioridad del hallazgo 2?", "3*2", "Prioridad = probabilidad × gravedad.", " puntos"),
        ("=", "{F} ¿Cuál es la prioridad del hallazgo 3?", "1*3", "Prioridad = probabilidad × gravedad.", " puntos"),
        ("=", "{F} ¿Cuál es la prioridad del hallazgo 4?", "2*2", "Prioridad = probabilidad × gravedad.", " puntos"),
        ("=", "{F} ¿Cuál es la prioridad del hallazgo 5?", "2*1", "Prioridad = probabilidad × gravedad.", " puntos"),
        ("abc", "{F} ¿Qué hallazgos tienen la prioridad más alta según el método de ejemplo?", "El 1 y el 2, ambos con 6", "El 3 y el 5", "El 4 solamente", "Los hallazgos 1 y 2 suman 6 cada uno."),
        ("abc", "{F} ¿Qué hallazgo tiene la prioridad más baja?", "El 5, con 2", "El 1, con 6", "El 4, con 4", "El papel suelto tiene prioridad 2, la más baja."),
        ("=", "{F} ¿Cuántos puntos de prioridad suman los cinco hallazgos?", "2*3+3*2+1*3+2*2+2*1", "Se suman las cinco prioridades calculadas.", " puntos"),
        ("abc", "{F} ¿Qué acción es adecuada para el hallazgo 1 por parte de quien lo detecta?", "Avisar al responsable y señalizar la zona si es seguro", "Subir al estante a corregirlo sin autorización", "Dejarlo para otro día", "El que detecta avisa; la corrección la hace una persona autorizada."),
        ("abc", "{F} El hallazgo 3 tiene prioridad 3. ¿Significa que la señal de salida despintada no importa?", "No: se corrige igual aunque tenga prioridad menor que los hallazgos 1 y 2", "Sí, se ignora", "Se retira la señal", "Tener menor prioridad no significa no atenderlo."),
        ("abc", "{F} Un compañero describe el hallazgo 2 como «cables, qué lata». ¿Qué falta?", "Un hecho verificable: qué, dónde y cuándo", "Más adjetivos", "Su opinión personal", "Una descripción útil nombra el hecho."),
        ("abc", "{F} ¿Quién fija el plazo para corregir los hallazgos?", "La jefatura, con la persona responsable de prevención", "El proveedor", "Cualquier cliente", "El plazo lo fija quien decide y responde por la corrección."),
    ],
    ctx=("abc", "El jefe de bodega pregunta qué corregir primero. ¿Qué responde la inspección?", "Los hallazgos 1 y 2, por su prioridad de 6", "El hallazgo 5, por ser el más fácil", "Ninguno", "Se prioriza lo de mayor probabilidad por gravedad."),
    sc=[
        ("En Logística: ¿cómo se describe un hallazgo?", "Con hechos: qué se vio, dónde y cuándo", "Así lo descrito se puede verificar por otra persona."),
        ("¿Qué indica una prioridad alta?", "Que el hallazgo es más urgente", "A mayor producto de ambos valores, más urgente es el hallazgo."),
        ("¿Quién corrige una instalación peligrosa?", "Una persona autorizada y capacitada", "Quien detecta el problema avisa y no actúa solo."),
    ],
    op=("Con la Ficha 45, escribe un registro de inspección con una tabla de cinco filas (hallazgo, prioridad, acción, quién la hace, plazo propuesto) y una frase que diga qué parte de la corrección no te corresponde hacer a ti.\n{F}",
        "H1 cajas en el borde: prioridad 6; reubicarlas; personal autorizado; hoy. H2 cable en el pasillo: 6; guardar o canalizar; personal autorizado; hoy. H3 señal despintada: 3; renovar; mantención; esta semana. H4 rótulo de carga ilegible: 4; reponer rótulo; supervisor; esta semana. H5 papel suelto: 2; recoger; quien lo ve. No me corresponde corregir instalaciones eléctricas ni alturas.",
        ["calcula las cinco prioridades", "ordena por prioridad", "propone acciones seguras", "indica lo que no corresponde hacer a un trabajador"],
        ["registro con tabla y frase"],
        ["acciones peligrosas", "prioridades mal calculadas", "no mencionar al responsable"],
        "Rehace las prioridades. Si propone que el trabajador arregle algo peligroso, pide reemplazarlo por avisar."),
    reinforce="Calcula en papel la prioridad de cuatro hallazgos ficticios con valores de 1 a 3.",
    extend="Explica con un ejemplo inventado por qué un hallazgo de baja probabilidad y alta gravedad también se atiende.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 46 (datos de ejemplo, inventados) de «Distribuidora Andes del Sur». Pictogramas del Sistema Globalmente Armonizado (SGA) que aparecen en etiquetas: llama (inflamable); llama sobre un círculo (comburente, que favorece que algo arda); corrosión (corrosivo); "
     "calavera con tibias cruzadas (tóxico de gravedad); signo de exclamación (irritante o nocivo); peligro para la salud (silueta con una estrella en el pecho, peligro grave para la salud); medio ambiente (árbol y pez, daño al ambiente); botella de gas (gas a presión); bomba explotando (explosivo). "
     "Productos ficticios: Alfa tiene el pictograma de llama; Beta, llama sobre un círculo; Gamma, corrosión; Delta, calavera con tibias cruzadas; Épsilon, signo de exclamación. Regla de ejemplo: los productos se guardan según su HDS y separados de los incompatibles.")
build(
    O5, 4, F,
    use="Aprenderé a reconocer la rotulación internacional de sustancias peligrosas (pictogramas del SGA) y a aplicar reglas generales de separación y de aviso en papel.",
    prior=["Conozco la señalética y la HDS.", "Sé qué es un riesgo.", "Sé que hay que avisar de lo inseguro."],
    explain=[
        "El Sistema Globalmente Armonizado (SGA) es una forma internacional de rotular las sustancias peligrosas con pictogramas, para que se entiendan en distintos países. Cada pictograma indica un peligro: la llama avisa que es inflamable; la llama sobre un círculo, que es comburente (favorece que algo arda); la corrosión, que daña tejidos y materiales; la calavera con tibias cruzadas, que es tóxico de gravedad; el signo de exclamación, que irrita o es nocivo; la silueta con estrella en el pecho, que es un peligro grave para la salud; el árbol y el pez, que daña el ambiente; la botella de gas, que es un gas a presión; y la bomba explotando, que es explosivo.",
        "Los pictogramas se leen junto con la hoja de datos de seguridad (HDS) y la etiqueta del fabricante. Según estos documentos y la norma vigente, los productos se almacenan separados de los incompatibles; por ejemplo, un inflamable se mantiene alejado de un comburente. Los envases deben mantener su etiqueta legible; uno sin etiqueta se trata como desconocido y se avisa.",
        "Este cuaderno es conceptual y no enseña a manipular sustancias. Practicar con sustancias peligrosas exige instructor autorizado, norma vigente y elementos de protección. Ante un derrame, una fuga o una duda, la persona se aleja, avisa a la persona responsable y sigue sus instrucciones.",
    ],
    vocab=[("SGA", "Sistema Globalmente Armonizado de rotulación de peligros"), ("pictograma", "dibujo que indica un tipo de peligro"), ("inflamable", "que puede arder con facilidad"), ("comburente", "que favorece que otra cosa arda"), ("corrosivo", "que daña tejidos y materiales"), ("incompatible", "que no debe guardarse junto con otro producto")],
    worked=[
        ("Leer un pictograma", "Una etiqueta ficticia lleva el signo de exclamación. ¿Qué indica?", ["El signo de exclamación avisa de un peligro menor.", "Es irritante o nocivo."], "Irritante o nocivo"),
        ("Separar", "Un producto ficticio es inflamable y otro es comburente. ¿Deben guardarse juntos?", ["Un inflamable se mantiene alejado de un comburente.", "No deben guardarse juntos."], "No, se separan"),
    ],
    mistakes=[("Guardar juntos productos «porque caben en el mismo estante».", "Si son incompatibles, juntarlos aumenta el riesgo.", "Consulta la HDS y sepáralos según la norma."),
              ("Quitar la etiqueta de un envase para que se vea ordenado.", "Se pierde la información de peligro.", "Mantén la etiqueta legible.")],
    T=[
        ("abc", "En Logística: ¿qué indica el pictograma de la llama?", "Que el producto es inflamable", "Que es corrosivo", "Que daña el ambiente", "La llama es el pictograma de los inflamables."),
        ("abc", "{F} ¿Qué indica la calavera con tibias cruzadas?", "Que el producto es tóxico de gravedad", "Que es un gas a presión", "Que es irritante leve", "Esa figura indica toxicidad grave para las personas."),
        ("abc", "{F} ¿Qué indica el pictograma de corrosión?", "Que el producto daña tejidos y materiales", "Que es explosivo", "Que no tiene riesgos", "La corrosión indica que daña tejidos y materiales."),
        ("abc", "{F} ¿Qué pictograma lleva el producto Beta?", "Llama sobre un círculo, es decir comburente", "Llama sola, es decir inflamable", "Corrosión", "La ficha dice que Beta tiene llama sobre un círculo."),
        ("abc", "{F} ¿Qué peligro indica la etiqueta del producto Delta?", "Tóxico de gravedad", "Irritante o nocivo", "Inflamable", "Delta lleva la calavera con tibias cruzadas."),
        ("abc", "{F} ¿Qué peligro indica la etiqueta del producto Épsilon?", "Irritante o nocivo", "Tóxico de gravedad", "Explosivo", "Épsilon lleva el signo de exclamación."),
        ("abc", "{F} ¿Pueden guardarse juntos Alfa (inflamable) y Beta (comburente)?", "No, se mantienen separados según la HDS y la norma vigente", "Sí, porque son del mismo tamaño", "Sí, si caben en un estante", "Un inflamable se mantiene alejado de un comburente."),
        ("abc", "{F} ¿Qué se hace con un envase de Gamma cuya etiqueta se despegó?", "Se trata como desconocido, se aparta si es seguro y se avisa al responsable", "Se guarda igual", "Se mezcla con otros", "Un envase sin etiqueta es información perdida y se avisa."),
        ("=", "{F} En una bodega de ejemplo hay 5 productos de la ficha. Si 2 son inflamables o comburentes, ¿cuántos no lo son?", "5-2", "Se resta del total los dos que sí lo son.", " productos"),
        ("=", "En un inventario de ejemplo hay 18 envases rotulados y 2 sin rótulo legible. ¿Cuántos envases hay en total?", "18+2", "Total = rotulados + sin rótulo legible.", " envases"),
        ("=", "Con esos 20 envases de ejemplo, ¿qué porcentaje tiene el rótulo legible?", "18*100//20", "Porcentaje = legibles × 100 ÷ total.", " %"),
        ("abc", "Un compañero dice que no hace falta leer la HDS si la etiqueta tiene pictogramas. ¿Qué respondes?", "La HDS entrega más información y se consulta junto con la etiqueta", "Tiene razón, no hace falta", "La HDS es solo para el fabricante", "El pictograma resume; la HDS detalla peligros y precauciones."),
        ("abc", "Se detecta olor fuerte cerca de unos envases de la zona de sustancias. ¿Qué es lo más adecuado?", "Alejarse, avisar al responsable de inmediato y seguir sus instrucciones", "Abrir los envases para revisar", "Mezclar los productos", "Ante una duda con sustancias, la persona se aleja y avisa."),
    ],
    ctx=("abc", "Una supervisora pide a su equipo separar en el plano los productos Alfa, Beta, Gamma, Delta y Épsilon. ¿Qué dato debe tener a la vista?", "Los pictogramas de cada producto y su HDS", "El precio de cada producto", "El nombre del proveedor", "La separación se decide con la información de peligros."),
    sc=[
        ("En Logística: ¿qué indica el pictograma de llama sobre un círculo?", "Comburente, que favorece que algo arda", "Es distinto de la llama sola, que es inflamable."),
        ("¿Dónde se consulta la información detallada de una sustancia?", "En la hoja de datos de seguridad", "La HDS detalla peligros y precauciones."),
        ("¿Qué haces ante un derrame de una sustancia?", "Me alejo, aviso al responsable y sigo sus instrucciones", "No se enfrenta lo que supera la capacitación."),
    ],
    op=("Con la Ficha 46, arma una tabla de los cinco productos con su pictograma, el peligro que indica, un producto con el que no deben guardarse juntos (si corresponde) y la acción si se pierde su etiqueta. Termina con la frase: «Este cuaderno no me habilita para manejar sustancias».\n{F}",
        "Alfa: llama, inflamable; no junto a Beta; si pierde la etiqueta, apartar si es seguro y avisar. Beta: llama sobre círculo, comburente; no junto a Alfa. Gamma: corrosión, daña tejidos y materiales. Delta: calavera con tibias, tóxico de gravedad. Épsilon: exclamación, irritante o nocivo. Este cuaderno no me habilita para manejar sustancias.",
        ["identifica los pictogramas", "separa inflamable y comburente", "propone acción segura ante etiqueta perdida", "declara el límite"],
        ["tabla de cinco filas y una frase final"],
        ["mezclar productos incompatibles", "enfrentar derrames", "omitir el límite"],
        "Compara con la ficha. Si propone manipular una sustancia, pide reemplazarlo por avisar."),
    reinforce="Dibuja en papel tres pictogramas de la ficha y escribe qué indica cada uno.",
    extend="Explica con un ejemplo inventado por qué una etiqueta legible es parte de la seguridad.",
)
