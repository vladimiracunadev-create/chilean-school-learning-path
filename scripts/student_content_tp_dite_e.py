"""Dibujo Técnico TP 3.º y 4.º medio: OAE-09 (cubicar manual y digitalmente, como cálculo y lectura de planillas). Papel; sin software; datos y precios de ejemplo."""
from __future__ import annotations

from tp_dite_common import build

O9 = "TP-DITE-3y4-OAE-09"

# ============================================================ OAE-09, clase 1
F = ("Ficha 1 (pedido de ejemplo, inventado). La «Constructora Ñire» pide la cubicación de un radier (losa de hormigón sobre el suelo) de una bodega de 8 m de largo, 5 m de ancho y 10 cm de espesor, "
     "y de un muro de bloques de 8 m de largo por 2,5 m de alto. Cubicar es medir y calcular cantidades (superficies, volúmenes y cantidad de materiales) para hacer un presupuesto y pedir materiales. "
     "El pedido debe entregarse en metros, metros cuadrados (m²) y metros cúbicos (m³).")
build(
    O9, 1, F,
    use="Aprenderé qué es cubicar, para qué sirve, qué sistemas de medida se usan y qué errores de unidades y de honestidad hay que evitar.",
    prior=["Sé calcular superficies de rectángulos.", "Sé que 100 cm son 1 m.", "Sé qué es un presupuesto."],
    explain=[
        "Cubicar es calcular cantidades de un proyecto a partir de sus planos: superficies (en m²), volúmenes (en m³), longitudes (en m) y cantidad de piezas o materiales. Sirve para hacer presupuestos y para pedir los materiales justos: si se calcula de menos, falta material y se detiene el trabajo; si se calcula de más, se gasta dinero de sobra. Esto es aprendizaje conceptual en papel y no un procedimiento de obra.",
        "Se usa el sistema métrico: milímetros (mm), centímetros (cm) y metros (m). La superficie de un rectángulo es largo por ancho, y el volumen de una caja es largo por ancho por alto, todo en la misma unidad. 1 m son 100 cm, 1 m son 1.000 mm, y algunos catálogos usan pulgadas: 1 pulgada son 25,4 mm. El error más común es mezclar unidades: 10 cm de espesor son 0,1 m, y hay que convertirlos antes de multiplicar por metros.",
        "La cubicación se puede hacer a mano o con una planilla de cálculo, programa donde cada dato está en una celda y las fórmulas hacen las operaciones. El programa no evita errores de datos: si se escribe una medida mal, la planilla calcula mal con total seguridad. Cubicar con honestidad significa no inflar las cantidades para ganar más dinero ni reducirlas para ganar una licitación (concurso en que varias empresas ofrecen precio para un trabajo), y dejar anotados los supuestos.",
    ],
    vocab=[("cubicar", "calcular cantidades de un proyecto a partir de sus planos"), ("superficie", "cantidad de plano que ocupa algo, en m²"), ("volumen", "espacio que ocupa algo, en m³"), ("radier", "losa de hormigón sobre el suelo"), ("planilla de cálculo", "programa con celdas y fórmulas para hacer cálculos"), ("supuesto", "dato que se asume y se deja anotado"), ("presupuesto", "estimación del costo de un trabajo")],
    worked=[
        ("Calcular una superficie", "Un piso de ejemplo mide 6 m de largo y 4 m de ancho. ¿Cuál es su superficie?", ["Superficie = largo × ancho.", "6 × 4 = 24 m²."], "24 m²"),
        ("Convertir antes de calcular", "Una losa de ejemplo mide 5 m por 4 m y tiene 20 cm de espesor. ¿Cuál es su volumen?", ["20 cm son 0,2 m.", "Volumen = 5 × 4 × 0,2 = 4 m³."], "4 m³"),
    ],
    mistakes=[("Multiplicar 8 m por 5 m por 10 sin convertir los 10 cm.", "Mezclar metros con centímetros da un volumen cien veces más grande.", "Convierte 10 cm a 0,1 m antes de multiplicar."),
              ("Confiar en la planilla porque «el computador no se equivoca».", "La planilla calcula bien lo que se escribe, pero no detecta un dato mal escrito.", "Revisa los datos de entrada y estima el orden de magnitud a mano.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es cubicar?", "Calcular cantidades de un proyecto a partir de sus planos", "Dibujar planos en tres dimensiones", "Imprimir copias de un plano", "Cubicar es calcular superficies, volúmenes y cantidades de materiales."),
        ("abc", "¿Qué unidad se usa para una superficie?", "m²", "m³", "m", "La superficie se mide en metros cuadrados."),
        ("abc", "¿Qué unidad se usa para un volumen?", "m³", "m²", "kg", "El volumen se mide en metros cúbicos."),
        ("=", "{F} ¿Cuántos m² de superficie tiene el radier?", "8*5", "La superficie es largo por ancho.", " m²"),
        ("=", "{F} ¿Cuántos m³ de hormigón tiene el radier? (10 cm son 0,1 m)", "8*5*0.1", "El volumen es largo por ancho por espesor, todo en metros.", " m³"),
        ("=", "{F} ¿Cuántos m² de superficie tiene el muro de bloques?", "8*2.5", "La superficie es largo por alto.", " m²"),
        ("abc", "{F} Una persona calcula el volumen como 8 × 5 × 10 = 400 m³. ¿Cuál es su error?", "No convirtió los 10 cm a metros", "Usó una fórmula incorrecta para el largo", "Olvidó sumar el ancho", "El espesor de 10 cm son 0,1 m; usar 10 hace el volumen cien veces mayor."),
        ("=", "{F} Un catálogo de ejemplo indica un tubo de 2 pulgadas de diámetro. ¿Cuántos milímetros son? (1 pulgada son 25,4 mm)", "2*25.4", "Se multiplican las pulgadas por 25,4 mm.", " mm"),
        ("abc", "{F} Si el radier se cubica en 400 m³ por error, ¿qué consecuencia tendría el pedido?", "Se pedirían muchísimos más materiales de los necesarios", "Faltaría material", "No pasaría nada", "Un volumen cien veces mayor haría pedir un exceso de materiales."),
        ("abc", "{F} Una planilla da 40 m³ para el radier. ¿Qué haces?", "Reviso los datos: el cálculo a mano da 4 m³ y hay un error de entrada", "Confío en la planilla porque es un programa", "Pido el doble por seguridad", "Una estimación a mano permite detectar datos mal escritos."),
        ("abc", "{F} La constructora te pide anotar menos bloques de los necesarios para ganar una licitación, «después se pide más». ¿Qué corresponde?", "Cubicar con honestidad y dejar anotados los supuestos", "Hacerlo, porque es su empresa", "Hacerlo y no avisar", "Reducir cantidades a propósito es engañar en el presupuesto."),
        ("=", "{F} Si el espesor del radier fuera 15 cm (0,15 m), ¿cuántos m³ de hormigón serían?", "8*5*0.15", "Se multiplica largo por ancho por el nuevo espesor.", " m³"),
        ("abc", "{F} Antes de calcular, descubres que el plano dice largo 8 m y el pedido dice 9 m. ¿Qué haces?", "Registro la diferencia y la consulto antes de cubicar", "Uso el mayor", "Uso el promedio", "Un dato contradictorio se consulta; no se elige a ojo."),
    ],
    ctx=("abc", "Calculas la cantidad de bloques y te das cuenta de que el pedido no dice las dimensiones del bloque. ¿Qué haces?", "Pido el dato o dejo anotado el supuesto que usé", "Invento una dimensión sin decirlo", "No cubico nada", "Un supuesto debe quedar anotado para que otro lo pueda revisar."),
    sc=[
        ("En Dibujo Técnico: ¿para qué sirve cubicar?", "Para hacer presupuestos y pedir los materiales justos", "Evita faltantes y gastos de más."),
        ("¿Cómo se calcula el volumen de una caja?", "Largo por ancho por alto, en la misma unidad", "Hay que convertir antes de multiplicar."),
        ("¿Qué haces con un supuesto?", "Lo dejo anotado", "Otra persona debe poder revisarlo y repetir el cálculo."),
    ],
    op=("Una bodega de ejemplo tiene un radier de 12 m de largo, 6 m de ancho y 12 cm de espesor, y un muro de 12 m de largo por 3 m de alto. Calcula la superficie del radier, el volumen de hormigón (en m³, convirtiendo el espesor), la superficie del muro, y escribe un supuesto que dejarías anotado y qué harías si una planilla te diera 864 m³.",
        "Superficie del radier: 12 × 6 = 72 m². Volumen: 12 × 6 × 0,12 = 8,64 m³. Muro: 12 × 3 = 36 m². Supuesto: el espesor es uniforme y sin desperdicio. Si la planilla da 864 m³, reviso los datos, porque 864 es cien veces mayor que 8,64; probablemente no se convirtió el espesor.",
        ["calcula superficies y volumen", "convierte el espesor", "anota un supuesto y detecta el error de la planilla"],
        ["hoja con cálculos y dos frases"],
        ["no convertir los 12 cm", "confiar en la planilla", "no anotar supuestos"],
        "Pregunta: «¿cuántos metros son 12 cm?». Si no responde, repasa las conversiones."),
    reinforce="Mide el largo y el ancho de tu pieza en metros y calcula su superficie.",
    extend="Explica con un ejemplo inventado qué pasa cuando una planilla de cálculo recibe un dato mal escrito.",
)

# ============================================================ OAE-09, clase 2
F = ("Ficha 2 (cuadro de cubicación de ejemplo). Ítem 1: radier, 40 m². Ítem 2: muro de bloques, 20 m². Ítem 3: pintura del muro (2 manos), se cuenta cada mano como superficie, es decir, 40 m² de superficie pintada. "
     "Conversiones: 1 m² son 10.000 cm²; 1 m³ son 1.000.000 cm³. Plancha de ejemplo: 1 m por 2 m. Una planilla de cálculo de ejemplo tiene en las celdas B2 el largo, C2 el ancho y D2 la fórmula «B2 por C2». "
     "Desperdicio de ejemplo: 5 % sobre las planchas.")
build(
    O9, 2, F,
    use="Aprenderé los conceptos de superficie, volumen, desperdicio y conversión de unidades, y cómo se organiza un cuadro de cubicación.",
    prior=["Sé qué es cubicar.", "Sé calcular superficies y volúmenes.", "Sé calcular porcentajes."],
    explain=[
        "Un cuadro de cubicación ordena el trabajo en ítems. Cada fila lleva el ítem (qué se cuenta), la unidad (m, m² o m³), la cantidad y el supuesto. Así se pueden revisar los cálculos y compararlos con los planos. La superficie se mide en m² y el volumen en m³; 1 m² son 10.000 cm² y 1 m³ son 1.000.000 cm³, por lo que las conversiones de superficie y volumen no son por 100 sino por 100 al cuadrado y 100 al cubo.",
        "El desperdicio es la parte del material que se pierde al cortar o ajustar. Se calcula como porcentaje de la cantidad neta: con 5 %, a 100 planchas se suman 5. La cantidad a pedir es la neta más el desperdicio, redondeada hacia arriba si se piden piezas enteras. El porcentaje de desperdicio lo fija el proyecto; aquí los valores son de ejemplo.",
        "En una planilla de cálculo, cada dato está en una celda y una fórmula hace el cálculo, por ejemplo multiplicar la celda del largo por la del ancho. Se verifica probando con un caso conocido: si 2 por 3 no da 6, la fórmula está mal. La planilla no reemplaza al criterio de quien cubica.",
    ],
    vocab=[("ítem", "cada partida o concepto que se cuenta"), ("cantidad neta", "cantidad calculada sin desperdicio"), ("desperdicio", "parte del material que se pierde"), ("celda", "casilla de una planilla donde se escribe un dato o fórmula"), ("fórmula", "instrucción que calcula un resultado a partir de celdas"), ("partida", "cada trabajo que se cuantifica")],
    worked=[
        ("Calcular planchas", "Un muro de ejemplo tiene 30 m² y cada plancha cubre 2 m². ¿Cuántas planchas netas se necesitan?", ["30 ÷ 2 = 15.", "Hacen falta 15 planchas netas."], "15 planchas"),
        ("Agregar el desperdicio", "Se necesitan 40 planchas netas y el desperdicio de ejemplo es 10 %. ¿Cuántas se piden?", ["10 % de 40 son 4.", "40 + 4 = 44 planchas."], "44 planchas"),
    ],
    mistakes=[("Convertir 1 m² a 100 cm² porque «1 m son 100 cm».", "El metro cuadrado es un cuadrado de 100 cm por 100 cm: son 10.000 cm².", "Multiplica 100 por 100 al pasar de m² a cm²."),
              ("Pedir 12,4 planchas porque el cálculo dio ese número.", "Las planchas se piden enteras, y faltaría material si se redondea hacia abajo.", "Redondea hacia arriba.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es el desperdicio?", "La parte del material que se pierde al cortar o ajustar", "El material que sobra por error de cálculo", "El dinero que se ahorra", "El desperdicio es una pérdida normal de material."),
        ("abc", "¿Cuántos cm² son 1 m²?", "10.000", "100", "1.000", "Un cuadrado de 100 cm por 100 cm tiene 10.000 cm²."),
        ("abc", "¿Qué hace una fórmula en una planilla?", "Calcula un resultado a partir de otras celdas", "Pinta de colores la tabla", "Guarda el archivo", "La fórmula opera con los datos de las celdas."),
        ("=", "{F} ¿Cuántas planchas netas de 1 m por 2 m se necesitan para el muro de 20 m²?", "20//2", "Se divide la superficie del muro por la de una plancha.", " planchas"),
        ("=", "{F} ¿Cuántas planchas se piden si al resultado anterior se le suma el desperdicio de 5 %? (redondea hacia arriba)", "(10*105+99)//100", "Se suma el 5 % a las planchas netas y se redondea hacia arriba.", " planchas"),
        ("=", "{F} ¿Cuántos cm² son 40 m²?", "40*10000", "Se multiplica por 10.000.", " cm²"),
        ("abc", "{F} ¿Qué cantidad se entrega en el ítem 3, la pintura de 2 manos?", "40 m² de superficie pintada", "20 m², porque es un solo muro", "2 m², por las dos manos", "Cada mano cuenta como superficie: 20 m² por 2 manos son 40 m²."),
        ("abc", "{F} En la planilla de ejemplo, ¿qué debería calcular la celda D2?", "El producto de B2 por C2, es decir, la superficie", "La suma de B2 y C2", "El largo menos el ancho", "La fórmula descrita multiplica el largo por el ancho."),
        ("=", "{F} Si B2 vale 6 y C2 vale 4, ¿qué valor debe mostrar D2?", "6*4", "Se multiplica el largo por el ancho.", ""),
        ("abc", "{F} D2 muestra 10 con B2 = 6 y C2 = 4. ¿Qué indica?", "La fórmula está mal, porque debería dar 24", "La fórmula está bien", "La celda C2 es incorrecta", "6 × 4 es 24; el resultado 10 corresponde a una suma."),
        ("=", "{F} ¿Cuántos cm³ son 3 m³?", "3*1000000", "Se multiplica por 1.000.000.", " cm³"),
        ("abc", "{F} Una cantidad calculada da 13,2 planchas. ¿Cuántas se piden?", "14", "13", "12", "Se redondea hacia arriba porque no se pueden pedir fracciones."),
        ("abc", "{F} La cantidad del ítem 2 (muro de bloques) viene en m, no en m². ¿Qué problema produce?", "Se confunden la longitud y la superficie, y la cantidad pedida sería incorrecta", "Ninguno, porque es lo mismo", "Se pierde el rótulo", "Cada ítem debe tener su unidad correcta."),
    ],
    ctx=("abc", "Tu compañera copió una fórmula de una planilla ajena y los resultados no cuadran con los planos. ¿Qué haces?", "Compruebo la fórmula con un caso conocido y la corrijo", "Dejo los resultados porque vienen de una planilla ya hecha", "Cambio los datos hasta que cuadre", "Las fórmulas copiadas deben comprobarse con casos conocidos."),
    sc=[
        ("En Dibujo Técnico: ¿cómo se calcula la cantidad a pedir con desperdicio?", "Cantidad neta más el desperdicio, redondeada hacia arriba", "Se agrega el porcentaje y se suben las fracciones."),
        ("¿Cuántos cm³ son 1 m³?", "1.000.000", "Se multiplica 100 por 100 por 100 al pasar a centímetros."),
        ("¿Cómo se verifica una fórmula?", "Probándola con un caso conocido", "Si 2 por 3 no da 6, hay un error."),
    ],
    op=("Una pared de ejemplo mide 5 m por 3 m y se cubre con planchas de 1 m por 2 m, con un desperdicio de ejemplo de 10 %. Calcula la superficie, las planchas netas (redondea hacia arriba), las planchas con desperdicio y escribe la fórmula que usarías en una planilla para la superficie y cómo la verificarías.",
        "Superficie: 15 m². Planchas netas: 15 ÷ 2 = 7,5, que se redondea a 8. Con desperdicio sobre 7,5 planchas: 7,5 + 0,75 = 8,25, que se redondea a 9 planchas. Fórmula: celda del largo por celda del ancho. Verificación: con un caso conocido, como 2 por 3, debe dar 6.",
        ["calcula la superficie y las planchas", "aplica el desperdicio y redondea hacia arriba", "describe la fórmula y su verificación"],
        ["hoja con cálculos y una fórmula descrita"],
        ["no redondear hacia arriba", "olvidar el desperdicio", "no verificar la fórmula"],
        "Pregunta: «¿cuántas planchas pides y por qué?». Si no responde, repasa el redondeo."),
    reinforce="Calcula cuántas baldosas de 30 cm por 30 cm cubren un piso de 3 m por 3 m.",
    extend="Explica con un ejemplo inventado por qué una fórmula copiada debe verificarse.",
)

# ============================================================ OAE-09, clase 3
F = ("Ficha 3 (caso de ejemplo). Muro de una casa de ejemplo: 6 m de largo por 2,5 m de alto. Vanos (aberturas): una puerta de 1 m de ancho por 2 m de alto y una ventana de 2 m de ancho por 1 m de alto. "
     "Cada m² de muro lleva 10 bloques (valor de ejemplo). Desperdicio de ejemplo: 10 %. "
     "Cuadro entregado por un compañero: «Superficie neta del muro: 11 m²; bloques: 110; con desperdicio: 121».")
build(
    O9, 3, F,
    use="Aprenderé a cubicar un muro con aberturas, a calcular la cantidad de piezas con desperdicio y a revisar un cuadro entregado por otra persona.",
    prior=["Sé calcular superficies.", "Sé calcular porcentajes.", "Sé qué es el desperdicio."],
    explain=[
        "Para cubicar un muro con aberturas se calcula primero la superficie total del muro (largo por alto) y luego se restan las superficies de los vanos, que son las puertas y ventanas. Lo que queda es la superficie neta. Para saber cuántas piezas se necesitan se multiplica la superficie neta por la cantidad de piezas por m², y se agrega el desperdicio.",
        "Al revisar un cuadro de otra persona se rehacen los cálculos a mano y se comparan paso a paso: superficie total, superficie de vanos, superficie neta, piezas netas, desperdicio y piezas a pedir. Si hay diferencias, se anota en qué paso aparece la primera y se consulta a quien lo hizo. Revisar es verificar, no corregir por cuenta propia.",
        "Una buena práctica es anotar siempre los supuestos, como la cantidad de bloques por m² y el porcentaje de desperdicio, ya que son datos del proyecto o del fabricante. Si cambian, el cuadro se recalcula. Esto es un ejercicio de papel y no una instrucción de construcción.",
    ],
    vocab=[("vano", "abertura de un muro, como una puerta o una ventana"), ("superficie neta", "superficie sin los vanos"), ("piezas por m²", "cantidad de piezas que cubren un m²"), ("paso a paso", "revisar cada etapa de un cálculo en orden")],
    worked=[
        ("Superficie neta", "Un muro de ejemplo mide 4 m por 3 m y tiene una puerta de 1 m por 2 m. ¿Cuál es su superficie neta?", ["Muro: 4 × 3 = 12 m². Puerta: 1 × 2 = 2 m².", "Neta: 12 − 2 = 10 m²."], "10 m²"),
        ("Piezas con desperdicio", "Con 10 m² netos, 8 piezas por m² y un desperdicio de 5 %, ¿cuántas piezas se piden?", ["Piezas netas: 10 × 8 = 80.", "Desperdicio: 5 % de 80 son 4: se piden 84."], "84 piezas"),
    ],
    mistakes=[("Restar el ancho de la puerta en vez de su superficie.", "Se resta superficie con superficie: ancho por alto.", "Calcula cada vano como largo por alto antes de restar."),
              ("Dar por bueno un cuadro porque «lo hizo un compañero de confianza».", "Los errores no distinguen entre personas; revisar es parte del trabajo.", "Rehaz los cálculos a mano y compara.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es un vano?", "Una abertura en un muro, como una puerta o ventana", "La parte más gruesa del muro", "Un tipo de bloque", "Un vano es una abertura, como una puerta o ventana."),
        ("abc", "¿Qué es la superficie neta de un muro?", "La superficie sin los vanos", "La superficie con los vanos", "La superficie del suelo", "La neta es la que queda después de restar los vanos."),
        ("abc", "Al revisar el cuadro de otra persona, ¿qué haces?", "Rehago los cálculos a mano y comparo paso a paso", "Lo acepto porque es de confianza", "Lo cambio sin avisar", "Revisar es verificar con un cálculo propio."),
        ("=", "{F} ¿Cuántos m² tiene el muro completo?", "6*2.5", "Se multiplica el largo por el alto.", " m²"),
        ("=", "{F} ¿Cuántos m² suman los dos vanos?", "1*2+2*1", "Se calcula la superficie de la puerta y de la ventana y se suman.", " m²"),
        ("=", "{F} ¿Cuántos m² de superficie neta tiene el muro?", "6*2.5-(1*2+2*1)", "Se resta la superficie de los vanos a la del muro.", " m²"),
        ("=", "{F} ¿Cuántos bloques netos se necesitan?", "11*10", "Se multiplica la superficie neta por los bloques por m².", " bloques"),
        ("=", "{F} ¿Cuántos bloques son con el desperdicio de 10 %?", "110+110*10//100", "Se suma el 10 % a los bloques netos.", " bloques"),
        ("abc", "{F} Comparando con el cuadro del compañero, ¿qué conclusión sacas?", "El cuadro está correcto: coincide en los tres resultados", "El cuadro tiene un error en la superficie", "El cuadro olvidó el desperdicio", "11 m², 110 bloques y 121 bloques coinciden con el cálculo."),
        ("abc", "{F} Otro cuadro dice «superficie neta: 15 m²; bloques: 150». ¿Qué error probable cometió?", "No restó los vanos del muro completo", "Restó los vanos dos veces", "Usó otros bloques por m²", "6 por 2,5 son 15 m²; no restó puerta ni ventana."),
        ("=", "{F} ¿Cuántos bloques de más pediría quien usó 15 m² en vez de 11 m², sin contar desperdicio?", "(15-11)*10", "Se multiplica la diferencia de superficie por los bloques por m².", " bloques"),
        ("abc", "{F} Al revisar, el cuadro dice 10 bloques por m², pero el proveedor informa 12 por m². ¿Qué haces?", "Registro la diferencia y consulto cuál valor corresponde al proyecto", "Uso el promedio de los dos", "Uso 12, porque es mayor", "Un dato que cambia el pedido se consulta, no se elige a ojo."),
        ("=", "{F} Con 12 bloques por m², ¿cuántos bloques netos se necesitarían para los 11 m²?", "11*12", "Se multiplica la superficie neta por los nuevos bloques por m².", " bloques"),
    ],
    ctx=("abc", "Encuentras un error de 100 bloques en el cuadro de tu jefe. ¿Qué haces?", "Le muestro el cálculo y le pido que lo confirme", "Lo corrijo en silencio", "No digo nada para evitar problemas", "El error se muestra con el cálculo, de forma respetuosa, para que se confirme."),
    sc=[
        ("En Dibujo Técnico: ¿cómo se calcula la superficie neta?", "Superficie del muro menos la de los vanos", "Se restan las puertas y ventanas a la superficie del muro."),
        ("¿Cómo se calculan los bloques netos?", "Superficie neta por bloques por m²", "Es una multiplicación de superficie por cantidad por m²."),
        ("¿Qué haces si un dato del cuadro cambia?", "Recalculo el cuadro", "Todo se recalcula con el dato nuevo."),
    ],
    op=("Un muro de ejemplo mide 8 m por 2,5 m y tiene una puerta de 1 m por 2 m y dos ventanas de 1 m por 1 m. Cada m² lleva 10 bloques y el desperdicio es de 10 %. Calcula la superficie total, la de los vanos, la neta, los bloques netos y con desperdicio, y revisa este cuadro ajeno: «neta 20 m²; bloques 200; con desperdicio 220».",
        "Muro: 20 m². Vanos: 2 + 1 + 1 = 4 m². Neta: 16 m². Bloques netos: 160. Con desperdicio: 176. El cuadro ajeno no restó los vanos (neta 20 m²), por lo que hay un error de 4 m² y 40 bloques; se lo muestro al autor para que lo confirme.",
        ["calcula cada paso", "revisa el cuadro ajeno", "comunica la diferencia sin corregir por su cuenta"],
        ["hoja con cálculos y una frase de comunicación"],
        ["no restar los vanos", "restar anchos en vez de superficies", "corregir el cuadro ajeno sin avisar"],
        "Pregunta: «¿en qué paso aparece la primera diferencia?». Si no responde, repasa los pasos."),
    reinforce="Mide una pared de tu casa, resta una puerta o ventana y calcula la superficie neta.",
    extend="Explica con un ejemplo inventado por qué se revisan los cuadros de cubicación entre dos personas.",
)

# ============================================================ OAE-09, clase 4
F = ("Ficha 4 (cubicación de ejemplo con costos). Radier de 10 m de largo, 6 m de ancho y 10 cm de espesor. Hormigón: se pide en camiones de 4 m³ (valor de ejemplo) y se agrega 10 % de desperdicio. "
     "Precios de ejemplo: hormigón $90.000 por m³; malla de acero $2.000 por m²; mano de obra $3.000 por m². Cuadro de planilla de ejemplo: ítem | unidad | cantidad | precio unitario | subtotal (cantidad × precio). "
     "Todos los precios son de ejemplo.")
build(
    O9, 4, F,
    use="Aprenderé a armar un cuadro de cubicación con costos, a aplicar el desperdicio y a redondear los pedidos, y a comparar el resultado manual con el de una planilla.",
    prior=["Sé calcular volúmenes.", "Sé calcular el desperdicio.", "Sé multiplicar cantidad por precio."],
    explain=[
        "Un cuadro de cubicación con costos tiene por cada ítem la unidad, la cantidad, el precio unitario y el subtotal, que es la cantidad por el precio. El total es la suma de los subtotales. Para armar el cuadro, primero se calculan las cantidades netas, luego se agrega el desperdicio, después se redondean los pedidos a las unidades que vende el proveedor y por último se calculan los costos.",
        "En el hormigón se calcula el volumen: largo por ancho por espesor, todo en metros. Si el desperdicio es 10 %, se suma. Si se pide en camiones de un volumen fijo, el número de camiones se redondea hacia arriba. La diferencia entre el volumen pedido y el necesario es un sobrante, que se anota. Los precios pueden cambiar: aquí son de ejemplo y se indica la fecha de la cotización.",
        "Una planilla de cálculo hace estas operaciones con fórmulas, pero se comprueba el resultado con un cálculo manual rápido. Si coinciden, hay confianza; si no, se busca el error antes de entregar. Cada cuadro lleva fecha, supuestos y autor. Es un ejercicio en papel y no una instrucción de obra.",
    ],
    vocab=[("subtotal", "cantidad por precio unitario de un ítem"), ("total", "suma de los subtotales"), ("cotización", "precio informado por un proveedor"), ("sobrante", "cantidad pedida de más"), ("precio unitario", "precio de una unidad")],
    worked=[
        ("Calcular un subtotal", "Un ítem de ejemplo: 25 m² de malla a $1.500 por m². ¿Cuál es el subtotal?", ["Subtotal = cantidad × precio unitario.", "25 × 1.500 = $37.500."], "$37.500"),
        ("Redondear camiones", "Se necesitan 9 m³ de hormigón y cada camión lleva 4 m³. ¿Cuántos camiones se piden y cuánto sobra?", ["9 ÷ 4 = 2,25: se redondea a 3 camiones.", "3 × 4 = 12 m³; sobran 12 − 9 = 3 m³."], "3 camiones; sobran 3 m³"),
    ],
    mistakes=[("Multiplicar el volumen por el precio sin haber agregado el desperdicio.", "El pedido real es mayor y el presupuesto queda corto.", "Agrega el desperdicio antes de calcular el costo."),
              ("Cobrar el volumen necesario en vez del volumen pedido.", "El proveedor cobra lo que entrega, incluidos los sobrantes.", "Calcula el costo con lo que realmente se pide.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿cómo se calcula el subtotal de un ítem?", "Cantidad por precio unitario", "Cantidad más precio unitario", "Precio unitario menos cantidad", "El subtotal es el producto de cantidad y precio."),
        ("abc", "¿Qué es el total de un cuadro de cubicación?", "La suma de los subtotales", "El mayor subtotal", "El precio unitario del primer ítem", "El total reúne los costos de todos los ítems."),
        ("abc", "¿Qué se hace con los camiones que dan una fracción?", "Se redondea hacia arriba", "Se redondea hacia abajo", "Se ignora la fracción", "Si se redondea hacia abajo faltaría hormigón."),
        ("=", "{F} ¿Cuántos m³ de hormigón se necesitan (10 cm son 0,1 m)?", "10*6*0.1", "El volumen es largo por ancho por espesor.", " m³"),
        ("=", "{F} ¿Cuántos m³ son con el desperdicio de 10 % sobre 6 m³?", "6*110/100", "Se multiplica por 110 % para sumar el desperdicio de 10 %.", " m³"),
        ("abc", "{F} Con 6,6 m³ y camiones de 4 m³, ¿cuántos camiones se piden?", "2 camiones, que dan 8 m³", "1 camión, que da 4 m³", "3 camiones, que dan 12 m³", "6,6 ÷ 4 da 1,65; se redondea hacia arriba a 2."),
        ("abc", "{F} ¿Cuántos m³ sobran con los 2 camiones, si se necesitan 6,6 m³?", "1,4 m³, porque 8 menos 6,6 es 1,4", "8 m³, que es todo lo pedido", "1,65 m³, que es el resultado de 6,6 ÷ 4", "Sobra el volumen pedido menos el necesario: 8 − 6,6."),
        ("=", "{F} ¿Cuánto cuesta el hormigón de los 2 camiones?", "2*4*90000", "Se multiplican los m³ pedidos por el precio por m³.", " pesos"),
        ("=", "{F} ¿Cuántos m² de superficie tiene el radier?", "10*6", "Se multiplica el largo por el ancho.", " m²"),
        ("=", "{F} ¿Cuánto cuesta la malla de acero para el radier?", "10*6*2000", "Se multiplica la superficie por el precio por m².", " pesos"),
        ("=", "{F} ¿Cuánto cuesta la mano de obra del radier?", "10*6*3000", "Se multiplica la superficie por el precio por m².", " pesos"),
        ("=", "{F} ¿Cuál es el total del presupuesto (hormigón de 2 camiones, malla y mano de obra)?", "2*4*90000+10*6*2000+10*6*3000", "Se suman los tres subtotales.", " pesos"),
        ("abc", "{F} Una planilla da un total de $10.200.000. ¿Qué haces?", "Reviso el cálculo manual: el total debe ser $1.020.000, y busco el error", "Entrego el total, porque lo calculó el programa", "Divido el resultado por dos", "Un total diez veces mayor indica un error en los datos o las fórmulas."),
    ],
    ctx=("abc", "El proveedor de hormigón cambia el precio a $95.000 por m³ después de que entregaste el cuadro. ¿Qué haces?", "Recalculo el cuadro con el precio nuevo y anoto la fecha y la cotización", "Dejo el cuadro como está", "Cambio solo el total sin avisar", "Los precios cambian: se recalcula y se registra."),
    sc=[
        ("En Dibujo Técnico: ¿qué se agrega antes de calcular el costo del hormigón?", "El desperdicio", "El pedido real es mayor que el necesario."),
        ("¿Cómo se calcula el total del cuadro?", "Sumando los subtotales", "Cada ítem aporta su subtotal al total del cuadro."),
        ("¿Qué haces con el resultado de una planilla?", "Lo compruebo con un cálculo manual rápido", "Así se detectan errores de datos o de fórmulas."),
    ],
    op=("Un radier de ejemplo mide 8 m por 5 m con 10 cm de espesor. El desperdicio es 10 %, los camiones llevan 4 m³, el hormigón cuesta $90.000 por m³ y la malla $2.000 por m². Calcula el volumen, el volumen con desperdicio, el número de camiones, el costo del hormigón, el costo de la malla y el total; indica una forma de comprobar el resultado de una planilla.",
        "Volumen: 8 × 5 × 0,1 = 4 m³. Con desperdicio: 4,4 m³. Camiones: 4,4 ÷ 4 = 1,1, es decir, 2 camiones (8 m³). Hormigón: 8 × 90.000 = $720.000. Malla: 40 × 2.000 = $80.000. Total: $800.000. Comprobación: repetir el cálculo manual y comparar con la planilla.",
        ["calcula volúmenes y camiones", "calcula costos y total", "describe una comprobación"],
        ["tabla con ítems, cantidades, precios y subtotales"],
        ["no convertir el espesor", "no redondear los camiones hacia arriba", "olvidar un subtotal"],
        "Pregunta: «¿por qué cobras 8 m³ y no 4,4?». Si no responde, repasa el redondeo y el sobrante."),
    reinforce="Inventa tres ítems de un presupuesto con cantidad y precio y calcula el total.",
    extend="Explica con un ejemplo inventado por qué se anota la fecha de la cotización en un cuadro de cubicación.",
)
