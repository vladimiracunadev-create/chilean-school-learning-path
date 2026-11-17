"""Instalaciones Sanitarias TP 3.º y 4.º medio: OAE-07 (artefactos sanitarios, cámaras y empalmes: solo conceptos, lectura de fichas, cálculos y verificación documental) y OAE-08 (verificar el funcionamiento de equipos, herramientas y maquinarias: manuales, inspección en papel, jerarquía de controles, EPP y señalética)."""
from __future__ import annotations

from tp_insa_common import AVISO, EMER, build

O7 = "TP-INSA-3y4-OAE-07"
O8 = "TP-INSA-3y4-OAE-08"

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La empresa ficticia «Sanitaria Costa» recibe el encargo de revisar la documentación de 6 baños de un edificio de ejemplo; cada baño lleva 3 artefactos sanitarios (lavamanos, inodoro y ducha). "
     "Documentos: plano, hoja de especificación del fabricante de cada artefacto y lista de materiales. Riesgos anotados: aguas servidas, gases en las cámaras de inspección, cortes con cerámica rota, cargas pesadas y resbalones.")
build(
    O7, 1, F,
    use="Aprenderé qué es un artefacto sanitario, para qué sirven el sifón, la cámara y el empalme, qué institución vigila los servicios sanitarios y qué riesgos tiene esta tarea.",
    prior=["Sé qué son las redes sanitarias.", "Sé multiplicar.", "Sé que las cámaras son espacios de riesgo alto."],
    explain=[
        "Un artefacto sanitario es un aparato fijo que usa o descarga agua, como el lavamanos, el inodoro o la ducha. Cada artefacto tiene un sifón: una pieza curva que retiene un poco de agua para impedir que los malos olores y los gases de la red de evacuación vuelvan al recinto. La cámara de inspección es una obra con acceso a la red de evacuación para poder revisarla. El empalme es la conexión entre la red de la propiedad y la red pública. En Chile, la Superintendencia de Servicios Sanitarios (SISS) fiscaliza a las empresas de servicios sanitarios, y la norma vigente regula las instalaciones.",
        "Los riesgos son varios. Las aguas servidas tienen microbios (riesgo biológico). Las cámaras pueden tener gases tóxicos, poco aire respirable y riesgo de caída o atrapamiento: son espacios confinados y entrar es tarea de personal autorizado. Los artefactos de cerámica tienen bordes cortantes cuando se quiebran y son pesados, por lo que se mueven con ayuda y con elementos de protección. Un estudiante nunca instala artefactos ni abre cámaras.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("artefacto sanitario", "aparato fijo que usa o descarga agua, como lavamanos, inodoro o ducha"), ("sifón", "pieza que retiene agua para impedir que olores y gases de la red vuelvan al recinto"), ("cámara de inspección", "obra con acceso a la red de evacuación para revisarla"), ("empalme", "conexión entre la red de la propiedad y la red pública"), ("SISS", "Superintendencia de Servicios Sanitarios, que fiscaliza a las empresas de servicios sanitarios"), ("espacio confinado", "recinto cerrado o de acceso difícil donde puede faltar aire respirable o haber gases")],
    worked=[
        ("Reconocer un artefacto", "Un aparato fijo de ejemplo, instalado en una cocina, descarga el agua de lavar la loza. ¿Es un artefacto sanitario?", ["Es un aparato fijo que usa y descarga agua.", "Sí, es un artefacto sanitario."], "Sí, es un artefacto sanitario"),
        ("Contar artefactos", "Un edificio de ejemplo tiene 5 baños con 2 artefactos cada uno. ¿Cuántos artefactos son?", ["Se multiplican los baños por los artefactos de cada uno.", "5 por 2 son 10."], "10 artefactos"),
    ],
    mistakes=[("Pensar que el sifón sirve para aumentar la presión del agua.", "El sifón retiene agua para frenar olores y gases de la red.", "Recuerda su función: sello de agua contra los gases."),
              ("Creer que mirar el interior de una cámara «solo un momento» no es riesgoso.", "Los gases tóxicos y la falta de aire actúan rápido.", "Deja las cámaras a personal autorizado.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es un sifón?", "Una pieza que retiene agua para impedir que olores y gases de la red vuelvan al recinto", "Una pieza que aumenta la presión del agua", "Una llave que corta el paso del agua", "El sifón forma un sello de agua; no regula presión ni corta el agua."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es una cámara de inspección?", "Una obra con acceso a la red de evacuación para revisarla", "Una caja que guarda los planos", "Un artefacto de la cocina", "La cámara permite acceder a la red para inspeccionarla."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es un artefacto sanitario?", "Un aparato fijo que usa o descarga agua", "La tubería principal de la calle", "El medidor de agua del edificio", "Lavamanos, inodoro y ducha son artefactos sanitarios."),
        ("=", "{F} ¿Cuántos artefactos sanitarios hay en total en los 6 baños de la ficha?", "6*3", "Se multiplican los baños por los artefactos de cada uno.", " artefactos"),
        ("abc", "{F} ¿Qué riesgo de la ficha corresponde a las cámaras de inspección?", "Gases tóxicos, falta de aire y riesgo de caída o atrapamiento", "Solo que se ensucien los planos", "Que se acabe el agua del edificio", "Las cámaras son espacios confinados con riesgos graves."),
        ("abc", "{F} ¿Qué riesgo se asocia a la cerámica quebrada de los artefactos?", "Cortes por bordes cortantes", "Descarga eléctrica", "Intoxicación por monóxido de carbono", "La cerámica rota tiene bordes cortantes."),
        ("=", "{F} Cada artefacto tiene una hoja de especificación de 3 páginas. ¿Cuántas páginas suman las hojas de todos los artefactos?", "6*3*3", "Se multiplican los artefactos por las páginas de cada hoja.", " páginas"),
        ("abc", "Una persona de ejemplo ve un derrame de aguas servidas en un pasillo de la obra. ¿Qué corresponde?", "Alejarse, impedir que otros se acerquen y avisar al responsable de la obra", "Limpiarlo de inmediato con las manos desnudas", "Taparlo con tierra y seguir", "Las aguas servidas tienen riesgo biológico; se avisa a quien corresponde."),
        ("abc", "En una obra de ejemplo, un trabajador queda inmóvil dentro de una cámara abierta. ¿Qué haces?", "No entrar, avisar de inmediato a un adulto responsable y a emergencias", "Bajar rápido a ayudarlo", "Esperar a ver si despierta", "Entrar puede producir otra víctima por falta de aire; se avisa a quienes pueden rescatar."),
        ("ab", "Un estudiante de ejemplo quiere instalar el lavamanos de su casa porque «ya vio los planos». ¿Qué corresponde?", "No hacerlo: la instalación la hace personal autorizado", "Hacerlo con ayuda del plano", "Leer planos no habilita para instalar; esa tarea exige personal autorizado y norma vigente."),
        ("abc", "{F} Un compañero dice: «con guantes puedo abrir la tapa de la cámara y mirar un segundo». ¿Qué respuesta es correcta?", "Es falso: los guantes no protegen de los gases, y entrar o asomarse es tarea de personal autorizado", "Es cierto: los guantes bastan", "Es cierto si es solo un segundo", "Los gases tóxicos no se evitan con guantes."),
        ("=", "{F} Para planificar el transporte, 6 lavamanos de 12 kg y 6 inodoros de 24 kg se cuentan como una sola carga. ¿Cuántos kilos suman?", "6*12+6*24", "Se suman los kilos de los lavamanos y de los inodoros.", " kg"),
        ("abc", "¿Cuál es el orden preventivo correcto antes de que personal autorizado trabaje con artefactos?", "Revisar documentos, identificar riesgos, definir quién hace cada tarea y recién autorizar", "Autorizar y revisar los riesgos después", "Empezar y corregir si ocurre algo", "Primero se informa y se planifica; el trabajo se autoriza al final."),
    ],
    ctx=("abc", "Un amigo de ejemplo te pide que le ayudes a levantar un inodoro de 24 kg de una bodega sin avisar a nadie. ¿Qué respondes?", "Que las cargas pesadas se mueven con ayuda y con protección, y que avise al responsable de la bodega", "Que lo levante solo, para ahorrar tiempo", "Que lo levante con un compañero, pero sin protección ni aviso", "Las cargas pesadas y la cerámica quebrada son riesgos; se planifica con ayuda."),
    sc=[
        ("En Instalaciones Sanitarias: ¿para qué sirve el sifón?", "Para impedir que olores y gases de la red vuelvan al recinto", "Retiene agua como sello contra los gases."),
        ("¿Quién entra a una cámara de inspección?", "Solo personal autorizado, con plan de seguridad", "El estudiante nunca entra a una cámara."),
        ("¿Qué institución fiscaliza a las empresas de servicios sanitarios?", "La SISS", "Superintendencia de Servicios Sanitarios es su nombre completo."),
    ],
    op=("Ficha de ejemplo: un edificio tiene 4 baños con 3 artefactos cada uno, y cada artefacto tiene una hoja de especificación de 2 páginas. Escribe (a) cuántos artefactos hay, (b) cuántas páginas suman las hojas, (c) para qué sirve el sifón, (d) por qué un estudiante no entra a una cámara de inspección.",
        "(a) 4 × 3 = 12 artefactos. (b) 12 × 2 = 24 páginas. (c) Retiene agua para que los olores y gases de la red no vuelvan al recinto. (d) Porque es un espacio confinado con gases y falta de aire; solo personal autorizado entra.",
        ["calcula los artefactos", "calcula las páginas", "explica el sifón", "explica el riesgo de la cámara"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar mal", "confundir el sifón con una llave", "creer que un estudiante puede entrar a una cámara"],
        "Pregunta: «¿qué harías si vieras a alguien inmóvil dentro de una cámara?». Si no responde, pídele que relea la regla de emergencia."),
    reinforce="Escribe una lista de cuatro artefactos sanitarios y, junto a cada uno, para qué sirve, sin describir cómo se instala.",
    extend="Explica con un ejemplo por qué los gases de la red de evacuación no deben volver al interior de una vivienda.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (hoja de especificación de ejemplo, inventada). Lavamanos modelo L-1: ancho 55 cm, profundidad 45 cm, peso 12 kg, uso de agua de ejemplo 6 litros por minuto. "
     "Inodoro modelo I-1: ancho 40 cm, profundidad 70 cm, peso 24 kg, uso de agua de ejemplo 6 litros por descarga. Plano de planta del baño: pared de apoyo de 220 cm. "
     "Piezas de accesorios que trae el fabricante: lavamanos, 3 piezas; inodoro, 5 piezas.")
build(
    O7, 2, F,
    use="Aprenderé a leer una hoja de especificación del fabricante, a sacar datos de dimensiones, pesos y consumos y a reconocer el rol de cada persona.",
    prior=["Sé leer una tabla de datos.", "Sé sumar y multiplicar.", "Sé qué es un artefacto sanitario."],
    explain=[
        "La hoja de especificación (o ficha técnica) del fabricante dice cómo es un artefacto: su modelo, sus dimensiones, su peso, su consumo de agua y los accesorios que trae. Es un documento de referencia y se lee antes de planificar el espacio, el transporte y la recepción. Si un dato de la hoja contradice el plano, no se supone cuál es el correcto: se registra la diferencia y se consulta al proyectista.",
        "El consumo de un artefacto es la cantidad de agua que usa: un inodoro de 6 litros por descarga usa 30 litros si se descarga 5 veces. La recepción de un artefacto es el momento en que el bodeguero o el supervisor revisa, antes de aceptarlo, que llegue completo, sin daños visibles y con su hoja técnica. Los roles son: el instalador autorizado instala; el supervisor planifica y revisa; el ITO verifica el proyecto; el bodeguero recibe; el usuario usa los artefactos.",
        f"Los números de esta ficha son de ejemplo para practicar la lectura. {EMER} {AVISO}",
    ],
    vocab=[("hoja de especificación", "documento del fabricante con modelo, dimensiones, peso, consumo y accesorios de un artefacto"), ("dimensiones", "medidas del artefacto: ancho, profundidad y altura"), ("consumo", "cantidad de agua que usa un artefacto"), ("accesorios", "piezas complementarias que trae un artefacto"), ("recepción", "momento en que se revisa un artefacto antes de aceptarlo")],
    worked=[
        ("Leer un dato", "La hoja de un lavamanos de ejemplo dice: ancho 50 cm, peso 10 kg. Si se llevan 3 iguales, ¿cuántos kilos suman?", ["Se multiplica el peso por la cantidad.", "10 por 3 son 30 kg."], "30 kg"),
        ("Consumo", "Un inodoro de ejemplo usa 5 litros por descarga y se descarga 8 veces al día. ¿Cuántos litros usa por día?", ["Se multiplican los litros por las descargas.", "5 por 8 son 40."], "40 litros por día"),
    ],
    mistakes=[("Suponer que el dato del plano siempre es el correcto cuando difiere de la hoja del fabricante.", "No se sabe cuál es el correcto sin consultar.", "Registra la diferencia y consulta al proyectista."),
              ("Aceptar un artefacto sin revisar que traiga sus accesorios y su hoja técnica.", "Después faltan piezas y no hay respaldo documental.", "Revisa la lista de recepción antes de aceptar.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es la hoja de especificación de un artefacto?", "El documento del fabricante con sus dimensiones, peso, consumo y accesorios", "El plano de la casa", "La factura de compra", "La hoja del fabricante describe el artefacto con datos técnicos."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es el consumo de un artefacto?", "La cantidad de agua que usa", "El precio que cuesta", "El peso que tiene", "El consumo mide el agua que usa el artefacto."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es la recepción de un artefacto?", "Revisar, antes de aceptarlo, que llegue completo y sin daños visibles", "Instalarlo en el baño", "Pagarlo al proveedor", "La recepción es una verificación antes de aceptar lo que llega."),
        ("=", "{F} ¿Cuántos centímetros de ancho suman el lavamanos L-1 y el inodoro I-1?", "55+40", "Se suman los anchos de los dos artefactos.", " cm"),
        ("=", "{F} ¿Cuántos kilos pesan juntos un lavamanos L-1 y un inodoro I-1?", "12+24", "Se suman los pesos de los dos artefactos.", " kg"),
        ("=", "{F} ¿Cuántos accesorios entregan en total los dos artefactos de la ficha?", "3+5", "Se suman las piezas de accesorios de cada artefacto.", " piezas"),
        ("=", "{F} Si el inodoro I-1 se descarga 10 veces en un día, ¿cuántos litros usa?", "10*6", "Se multiplican las descargas por los litros de cada una.", " litros"),
        ("=", "{F} Si el lavamanos L-1 se usa 4 minutos en total en un día, ¿cuántos litros usa?", "4*6", "Se multiplican los minutos por los litros por minuto.", " litros"),
        ("=", "{F} ¿Cuántos centímetros de la pared de 220 cm quedan libres después de poner los dos artefactos uno al lado del otro?", "220-(55+40)", "Se resta el ancho de ambos artefactos al largo de la pared.", " cm"),
        ("abc", "{F} El plano dice que el lavamanos pesa 15 kg, pero la hoja del fabricante dice 12 kg. ¿Qué corresponde?", "Registrar la diferencia y consultar al proyectista, sin suponer cuál es la correcta", "Usar el dato del plano sin avisar", "Usar la hoja y cambiar el plano", "Una diferencia entre documentos se registra y se consulta."),
        ("abc", "{F} Llega el inodoro sin la hoja técnica y le faltan 2 de las 5 piezas de accesorios. ¿Qué corresponde en la recepción?", "Registrar lo que falta y no aceptarlo hasta completar", "Aceptarlo y buscar las piezas después", "Aceptarlo sin anotar nada", "La recepción verifica que el artefacto llegue completo."),
        ("=", "{F} Una obra recibe 8 lavamanos y 8 inodoros iguales a los de la ficha. ¿Cuántos kilos pesan en total?", "8*12+8*24", "Se suman los kilos de los lavamanos y de los inodoros.", " kg"),
        ("abc", "¿Quién instala los artefactos en una obra?", "El instalador autorizado", "El usuario del baño", "El estudiante que leyó la ficha", "La instalación corresponde a personal autorizado; los demás roles planifican, revisan o usan."),
    ],
    ctx=("abc", "El supervisor de ejemplo te pide leer una hoja de especificación y pasarle los pesos de los artefactos para planificar el transporte. ¿Qué haces?", "Leer los datos de la hoja, calcular los pesos totales y entregárselos por escrito", "Levantar los artefactos para comprobar su peso", "Inventar los pesos sin mirar la hoja", "Leer y calcular es el aprendizaje de esta tarea; mover cargas lo planifica personal capacitado."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué datos entrega una hoja de especificación?", "Modelo, dimensiones, peso, consumo y accesorios", "Es el documento técnico del fabricante."),
        ("¿Qué se hace con una diferencia entre el plano y la hoja del fabricante?", "Se registra y se consulta al proyectista", "No se sabe cuál dato es el correcto."),
        ("¿Cuándo se revisa que un artefacto llegue completo?", "En la recepción, antes de aceptarlo", "Después de aceptarlo sería más difícil reclamar al proveedor."),
    ],
    op=("Ficha de ejemplo: lavamanos modelo L-2: ancho 50 cm, peso 10 kg, 5 litros por minuto; inodoro modelo I-2: ancho 38 cm, peso 22 kg, 5 litros por descarga; pared de apoyo de 200 cm; el inodoro se descarga 8 veces al día. Escribe (a) el ancho y el peso de ambos juntos, (b) cuántos cm quedan libres en la pared, (c) cuántos litros usa el inodoro por día, (d) qué harías si el plano diera otro peso que la hoja.",
        "(a) 50 + 38 = 88 cm; 10 + 22 = 32 kg. (b) 200 − 88 = 112 cm. (c) 8 × 5 = 40 litros. (d) Registrar la diferencia y consultar al proyectista sin suponer cuál es la correcta.",
        ["suma ancho y peso", "calcula el espacio libre", "calcula el consumo", "propone registrar y consultar"],
        ["hoja con los cuatro resultados"],
        ["restar mal el espacio libre", "multiplicar mal el consumo", "suponer el dato correcto"],
        "Pregunta: «¿quién decide cuál dato es el correcto?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Escribe una hoja de especificación de ejemplo de un artefacto con cinco datos y una pregunta de cálculo sobre ella.",
    extend="Explica con un ejemplo por qué conviene revisar los accesorios en la recepción y no después.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (caso en papel, de ejemplo, inventado). Planta de un baño de ejemplo. Anchos: lavamanos 55 cm, inodoro 40 cm, ducha 90 cm. Regla de ejemplo: entre artefactos contiguos debe quedar una separación libre de 15 cm. "
     "Opción 1: los tres artefactos alineados en una pared de 200 cm. Opción 2: los tres artefactos alineados en una pared de 240 cm. "
     "Además, el plano muestra 6 baños con 3 artefactos cada uno, mientras que la lista de materiales pide 20 sifones.")
build(
    O7, 3, F,
    use="Aprenderé a comprobar en papel si los artefactos caben en una pared con las separaciones del plano y a detectar diferencias entre el plano y la lista de materiales.",
    prior=["Sé sumar y restar medidas en cm.", "Sé leer una planta descrita por escrito.", "Sé qué es una discrepancia."],
    explain=[
        "Para saber si los artefactos caben en una pared se suman los anchos de todos los artefactos y las separaciones entre ellos. Con tres artefactos alineados hay dos separaciones, una entre el primero y el segundo, y otra entre el segundo y el tercero. Si el total es igual o menor que el largo de la pared, caben; la diferencia es el margen. Si es mayor, no caben y se informa al proyectista, que puede rediseñar la distribución.",
        "También se compara el plano con la lista de materiales. Si el plano muestra 5 baños con 2 artefactos, hay que pedir 10 sifones. Si la lista pide otra cantidad, hay una discrepancia que se registra y se consulta, y no se pide el material hasta aclararla. Se anota qué documento dice qué, la diferencia y a quién se informó.",
        f"Este es un ejercicio de lectura de planos y listas: la instalación real la hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("alineados", "puestos en fila a lo largo de una pared"), ("separación libre", "espacio que debe quedar entre dos artefactos contiguos"), ("margen", "espacio que sobra en la pared"), ("lista de materiales", "documento que dice qué materiales se necesitan y en qué cantidad"), ("distribución", "forma de ubicar los artefactos en el recinto")],
    worked=[
        ("Largo necesario", "Dos artefactos de ejemplo de 50 cm y 45 cm van alineados con una separación de 20 cm. ¿Qué largo de pared necesitan?", ["Se suman los dos anchos y la separación.", "50 más 45 más 20 son 115 cm."], "115 cm"),
        ("Comparar con la lista", "El plano de ejemplo muestra 4 baños con 2 artefactos y la lista pide 9 sifones. ¿Hay discrepancia?", ["Se necesitan 4 por 2, es decir 8 sifones.", "La lista pide 9: hay discrepancia de 1."], "Sí, hay una discrepancia de 1 sifón"),
    ],
    mistakes=[("Contar tres separaciones entre tres artefactos alineados.", "Entre tres artefactos hay solo dos espacios.", "Cuenta los espacios entre artefactos contiguos."),
              ("Pedir el material de la lista aunque no coincida con el plano.", "Se podría pedir de más o de menos.", "Registra la discrepancia y consulta antes de pedir.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es la separación libre entre dos artefactos?", "El espacio que debe quedar entre dos artefactos contiguos", "El ancho del primer artefacto", "El largo de la pared", "La separación es el espacio libre entre artefactos."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es el margen en una pared con artefactos?", "El espacio que sobra después de ubicar los artefactos y sus separaciones", "El ancho de un artefacto", "El peso de la pared", "El margen se obtiene restando lo necesario al largo disponible."),
        ("abc", "En Instalaciones Sanitarias: ¿cuántas separaciones hay entre tres artefactos alineados?", "Dos", "Tres", "Cuatro", "Entre tres artefactos contiguos solo hay dos espacios."),
        ("=", "{F} ¿Cuántos centímetros suman los anchos de los tres artefactos?", "55+40+90", "Se suman los anchos de lavamanos, inodoro y ducha.", " cm"),
        ("=", "{F} ¿Cuántos centímetros suman las dos separaciones libres de 15 cm?", "2*15", "Se multiplica el número de separaciones por 15 cm.", " cm"),
        ("=", "{F} ¿Qué largo de pared necesitan los tres artefactos con sus separaciones?", "55+40+90+2*15", "Se suman los anchos y las dos separaciones.", " cm"),
        ("abc", "{F} ¿Caben los tres artefactos en la pared de 200 cm de la opción 1?", "No, porque necesitan 215 cm y la pared mide 200 cm", "Sí, porque 215 es casi 200", "Sí, con un artefacto menos", "Los artefactos necesitan 215 cm y la pared tiene 200 cm."),
        ("=", "{F} ¿Cuántos centímetros de margen quedan en la pared de 240 cm de la opción 2?", "240-(55+40+90+2*15)", "Se resta lo necesario al largo de la pared.", " cm"),
        ("abc", "{F} Según el cálculo, ¿qué opción es posible?", "La opción 2, con un margen de 25 cm", "La opción 1, con un margen de 15 cm", "Ninguna de las dos", "La opción 2 cumple y la opción 1 queda corta."),
        ("=", "{F} ¿Cuántos sifones indica el plano para los 6 baños de la ficha?", "6*3", "Se multiplican los baños por los artefactos de cada uno.", " sifones"),
        ("=", "{F} ¿Cuántos sifones de diferencia hay entre la lista de materiales y el plano?", "20-6*3", "Se resta lo que indica el plano a lo que pide la lista.", " sifones"),
        ("abc", "{F} ¿Qué corresponde hacer con esa diferencia antes de pedir sifones?", "Registrar la discrepancia y consultar al proyectista", "Pedir los 20 de la lista y listo", "Pedir 18 sin avisar", "No se pide hasta aclarar cuál es el dato correcto."),
        ("abc", "{F} Un compañero dice: «los 2 sifones de más pueden servir de repuesto». ¿Qué respuesta es correcta?", "Es una hipótesis; se consulta y, si corresponde, se anota como repuesto en la lista", "Siempre se piden los repuestos sin registrar", "Los repuestos no existen", "Una cantidad de más puede ser un error o un repuesto previsto, y solo se aclara consultando."),
    ],
    ctx=("abc", "El dueño de la obra de ejemplo propone aprovechar la opción 1 «apretando» los artefactos para ahorrar pared. ¿Qué propones?", "Informar que no caben con sus separaciones y consultar al proyectista por un rediseño", "Instalarlos igual, apretados", "Quitar una separación para que quepan", "Las separaciones son parte del diseño; reducirlas sin autorización es un riesgo."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se calcula el largo de pared que necesitan los artefactos alineados?", "Anchos más separaciones entre artefactos contiguos", "Se suman los anchos y los espacios libres entre artefactos."),
        ("¿Qué se hace con una diferencia entre el plano y la lista de materiales?", "Se registra y se consulta antes de pedir", "No se sabe cuál es el dato correcto."),
        ("¿Quién rediseña una distribución?", "El proyectista", "La distribución es parte del diseño."),
    ],
    op=("Ficha de ejemplo: lavamanos 50 cm e inodoro 38 cm alineados con una separación de 20 cm, y una ducha de 80 cm con otra separación de 20 cm, en una pared de 220 cm. El plano muestra 5 baños con 3 artefactos y la lista de materiales pide 14 sifones. Escribe (a) el largo necesario, (b) si caben y con qué margen, (c) cuántos sifones indica el plano y la diferencia con la lista, (d) qué harías con la diferencia.",
        "(a) 50 + 38 + 80 + 2 × 20 = 208 cm. (b) Caben: 220 − 208 = 12 cm de margen. (c) 5 × 3 = 15 sifones; la lista pide 14, es decir 1 menos. (d) Registrar la discrepancia y consultar antes de pedir.",
        ["calcula el largo necesario", "calcula el margen", "calcula los sifones y la diferencia", "propone registrar y consultar"],
        ["hoja con los cálculos y el registro"],
        ["contar tres separaciones", "restar mal el margen", "pedir el material sin consultar"],
        "Pregunta: «¿cuántas separaciones hay entre tres artefactos?». Si no responde, pídele que dibuje los tres artefactos en fila."),
    reinforce="Calcula en papel si tres artefactos de 45, 40 y 60 cm caben en una pared de 180 cm con separaciones de 15 cm.",
    extend="Explica con un ejemplo por qué las separaciones de un plano no se reducen sin autorización.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (comparación de consumo de ejemplo, inventada). Una familia de 4 personas usa el inodoro 5 veces al día cada una (dato de ejemplo). Modelo A: 6 litros por descarga. Modelo B: 4 litros por descarga. "
     "Mes de 30 días; año de 12 meses. Precio del agua de ejemplo: $1 por litro (valor de ejemplo). Precio del modelo B de ejemplo: $30.000 más caro que el modelo A.")
build(
    O7, 4, F,
    use="Aprenderé a aplicar un criterio técnico de consumo de agua con datos de ejemplo: calcular las descargas, los litros por mes y por año, el ahorro y el tiempo de recuperación.",
    prior=["Sé multiplicar varias cantidades.", "Sé calcular un ahorro.", "Sé qué es el consumo de un artefacto."],
    explain=[
        "Un criterio técnico de consumo compara cuánta agua usa cada modelo. Primero se calculan las descargas de la familia por día, multiplicando las personas por los usos de cada una. Después se multiplica por los litros de cada descarga y por los días del mes. Con la diferencia entre los dos modelos se obtiene el ahorro de agua. El ahorro mensual multiplicado por el precio del agua da el ahorro en pesos.",
        "El tiempo de recuperación es la cantidad de meses que tarda el ahorro en igualar la diferencia de precio de los modelos. Un modelo que gasta menos agua es mejor para el entorno, pero la decisión también debe considerar que cumpla la norma vigente y que lo instale personal autorizado.",
        f"Los consumos y los precios de esta ficha son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("descarga", "salida de agua cada vez que se usa el inodoro"), ("ahorro de agua", "diferencia de litros entre dos modelos"), ("ahorro mensual en pesos", "ahorro de litros por mes multiplicado por el precio del agua"), ("tiempo de recuperación", "meses que tarda el ahorro en igualar la diferencia de precio"), ("criterio técnico", "regla con la que se compara un dato para decidir")],
    worked=[
        ("Descargas por día", "Una familia de ejemplo de 3 personas usa el inodoro 4 veces al día cada una. ¿Cuántas descargas son por día?", ["Se multiplican las personas por los usos.", "3 por 4 son 12."], "12 descargas"),
        ("Ahorro mensual", "Un modelo de ejemplo ahorra 600 litros al mes y el agua cuesta $2 por litro. ¿Cuánto ahorra por mes?", ["Se multiplican los litros por el precio.", "600 por 2 son 1.200."], "$1.200 por mes"),
    ],
    mistakes=[("Elegir el modelo más barato sin calcular el agua que usa en un año.", "Un modelo barato puede gastar más agua y salir más caro con el tiempo.", "Calcula el consumo y el ahorro antes de decidir."),
              ("Calcular el consumo mensual sin multiplicar por los 30 días.", "El resultado queda en un solo día.", "Multiplica por los días del mes.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es el ahorro de agua entre dos modelos?", "La diferencia de litros que usan", "La suma de los litros que usan", "El precio de cada modelo", "El ahorro es lo que se deja de gastar al elegir el modelo de menor consumo."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es el tiempo de recuperación?", "Los meses que tarda el ahorro en igualar la diferencia de precio", "Los años de garantía", "Los minutos de una descarga", "Compara el precio extra con el ahorro que se logra."),
        ("abc", "En Instalaciones Sanitarias: ¿qué datos se necesitan para calcular las descargas por día?", "El número de personas y los usos de cada una", "El color del artefacto", "La marca del proveedor", "Las descargas dependen de cuántas personas usan el inodoro y cuántas veces."),
        ("=", "{F} ¿Cuántas descargas hace la familia por día?", "4*5", "Se multiplican las personas por los usos de cada una.", " descargas"),
        ("=", "{F} ¿Cuántos litros usa por día el modelo A?", "4*5*6", "Se multiplican las descargas por los litros de cada una.", " litros"),
        ("=", "{F} ¿Cuántos litros usa por día el modelo B?", "4*5*4", "Se multiplican las descargas por los litros de cada una.", " litros"),
        ("=", "{F} ¿Cuántos litros ahorra por mes el modelo B frente al A?", "(4*5*6-4*5*4)*30", "Se resta el consumo diario de B al de A y se multiplica por 30 días.", " litros"),
        ("=", "{F} ¿Cuántos litros ahorra por año el modelo B frente al A?", "(4*5*6-4*5*4)*30*12", "Se multiplica el ahorro mensual por 12 meses.", " litros"),
        ("=", "{F} ¿Cuánto ahorra por mes en pesos el modelo B?", "(4*5*6-4*5*4)*30*1", "Se multiplican los litros ahorrados por el precio de $1 por litro.", " pesos"),
        ("=", "{F} ¿En cuántos meses el ahorro mensual iguala la diferencia de precio de $30.000?", "30000//1200", "Se divide la diferencia de precio entre el ahorro mensual.", " meses"),
        ("abc", "{F} Si la familia piensa vivir muchos años en la casa, ¿qué modelo conviene por costo y agua?", "El modelo B, porque recupera su costo extra y ahorra agua", "El modelo A, porque es más barato al comprarlo", "Ninguno, porque cuestan lo mismo", "Después del tiempo de recuperación el modelo B sigue ahorrando."),
        ("abc", "{F} Un compañero propone instalar el modelo B él mismo para ahorrar el pago del instalador. ¿Qué respuesta es correcta?", "No: la instalación la hace personal autorizado, aunque el modelo sea más eficiente", "Sí: es más fácil que instalar el A", "Sí, si el modelo trae manual", "El ahorro de agua no autoriza a instalar sin personal habilitado."),
        ("abc", "¿Cuál es el mejor registro de la comparación?", "Descargas por día, litros por mes de cada modelo, ahorro, tiempo de recuperación y quién decide", "El modelo B parece mejor", "Los dos modelos son parecidos", "Un registro completo permite revisar la decisión."),
    ],
    ctx=("abc", "Una administradora de edificio de ejemplo te pregunta si cambiar los inodoros del edificio «vale la pena». ¿Qué respondes?", "Que puedes mostrar la comparación de consumo y costos en papel, y que el cambio lo decide y ejecuta personal autorizado", "Que cambien todos mañana", "Que no vale nunca la pena", "La comparación en papel ayuda, pero la instalación exige personal autorizado."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se obtiene el consumo diario de un modelo?", "Descargas por litros de cada descarga", "Se multiplica la cantidad de usos por los litros."),
        ("¿Cómo se calcula el tiempo de recuperación?", "Diferencia de precio dividida en el ahorro mensual", "Compara la inversión extra con lo que se ahorra."),
        ("¿Quién instala un modelo más eficiente?", "Personal autorizado", "La eficiencia no reemplaza la autorización."),
    ],
    op=("Ficha de ejemplo: una familia de 3 personas usa el inodoro 4 veces al día cada una; modelo X: 6 litros por descarga; modelo Y: 3 litros por descarga; mes de 30 días; el agua cuesta $1 por litro; el modelo Y cuesta $27.000 más. Escribe (a) las descargas por día, (b) los litros por mes de cada modelo, (c) el ahorro mensual en pesos, (d) en cuántos meses se recupera la diferencia de precio.",
        "(a) 3 × 4 = 12 descargas. (b) X: 12 × 6 × 30 = 2.160 litros. Y: 12 × 3 × 30 = 1.080 litros. (c) 2.160 − 1.080 = 1.080 litros, es decir $1.080 por mes. (d) 27.000 ÷ 1.080 = 25 meses.",
        ["calcula las descargas", "calcula los litros mensuales de ambos", "calcula el ahorro", "calcula el tiempo de recuperación"],
        ["hoja con la comparación completa"],
        ["olvidar los 30 días", "restar al revés", "decir que el estudiante instala"],
        "Pregunta: «¿qué pasa después de recuperar la diferencia de precio?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Calcula en papel los litros por día de dos modelos con 5 y 4 litros por descarga para una familia de 4 personas que lo usa 3 veces al día cada una.",
    extend="Explica con un ejemplo por qué un ahorro pequeño por día se vuelve grande en un año.",
)

# ============================================================ OAE-07, clase 5
F = ("Ficha 5 (alternativas y recepción de ejemplo, inventadas). Dos lavamanos de ejemplo. Modelo M1: precio $40.000, vida útil estimada 10 años. Modelo M2: precio $65.000, vida útil estimada 20 años. "
     "Lista de verificación de recepción de artefactos (12 puntos: sin grietas, accesorios completos, hoja técnica, etiquetas, embalaje íntegro y otros): cumplen 9. "
     "Registro de prueba hecho por personal autorizado en una obra anterior, presentado como evidencia: «cumple».")
build(
    O7, 5, F,
    use="Aprenderé a comparar dos artefactos por costo y vida útil, a verificar la calidad en la recepción con una lista de control y a interpretar un registro de prueba hecho por personal autorizado.",
    prior=["Sé calcular el costo por año.", "Sé calcular un porcentaje.", "Sé qué es la recepción de un artefacto."],
    explain=[
        "Para comparar dos artefactos se calcula el costo por año de vida útil: el precio dividido en los años que se espera que dure. Un artefacto más caro puede salir más barato por año si dura más. Además, se consideran la disponibilidad de repuestos, el consumo de agua y el cumplimiento de la norma vigente. La decisión final la toman el proyectista y quien compra, con registro escrito.",
        "En la recepción se usa una lista de verificación: se revisa cada punto con «cumple» o «no cumple». Los puntos que no cumplen se informan y se corrigen antes de aceptar el artefacto. Un registro de prueba es el documento en el que personal autorizado deja constancia de una prueba y su resultado; quien lo lee comprueba que exista, que tenga fecha, responsable y resultado, pero no repite la prueba. La prueba de funcionamiento de una instalación no es tarea de un estudiante.",
        f"Los precios y las vidas útiles de esta ficha son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("costo por año", "precio dividido en los años de vida útil esperados"), ("lista de verificación", "pauta de puntos a revisar con la respuesta «cumple» o «no cumple»"), ("registro de prueba", "documento donde personal autorizado deja constancia de una prueba y su resultado"), ("evidencia", "documento o dato que respalda una afirmación"), ("no conformidad", "resultado que no cumple lo pedido")],
    worked=[
        ("Costo por año", "Un artefacto de ejemplo cuesta $90.000 y se espera que dure 15 años. ¿Cuánto cuesta por año?", ["Se divide el precio entre los años.", "90.000 dividido en 15 son 6.000."], "$6.000 por año"),
        ("Porcentaje de cumplimiento", "Una lista de ejemplo tiene 8 puntos y cumplen 6. ¿Qué porcentaje cumple?", ["Se divide lo que cumple entre el total.", "6 por 100 dividido en 8 son 75 %."], "75 %"),
    ],
    mistakes=[("Dar por cumplido un punto de la lista sin evidencia.", "Sin respaldo no se puede asegurar.", "Marca «cumple» solo con evidencia revisada."),
              ("Aceptar un artefacto con un punto que no cumple «porque cumple casi todo».", "Un punto grave puede afectar la seguridad.", "Informa la no conformidad y corrige antes de aceptar.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es el costo por año de un artefacto?", "Su precio dividido en los años de vida útil esperados", "Su precio multiplicado por los años", "El costo de la última cuenta de agua", "El costo por año reparte el precio en el tiempo que se espera que dure."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es una lista de verificación de recepción?", "Una pauta de puntos a revisar con «cumple» o «no cumple» antes de aceptar un artefacto", "Una lista de precios de proveedores", "Un registro de asistencia", "La lista ordena la revisión de lo que llega."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es una evidencia?", "Un documento o dato que respalda una afirmación", "Una opinión sin respaldo", "Un precio de venta", "La evidencia permite comprobar lo que se afirma."),
        ("=", "{F} ¿Cuánto cuesta por año el modelo M1?", "40000//10", "Se divide el precio entre los años de vida útil.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta por año el modelo M2?", "65000//20", "Se divide el precio entre los años de vida útil.", " pesos"),
        ("abc", "{F} Según el costo por año, ¿qué modelo conviene?", "El M2, porque cuesta menos por año", "El M1, porque es más barato", "Ninguno", "M2 cuesta 3.250 por año y M1 cuesta 4.000 por año."),
        ("=", "{F} ¿Cuántos pesos por año ahorra el M2 respecto del M1?", "40000//10-65000//20", "Se resta el costo por año de M2 al de M1.", " pesos"),
        ("=", "{F} ¿Qué porcentaje de los 12 puntos de la lista de recepción cumple?", "9*100//12", "Se divide lo que cumple entre el total y se pasa a porcentaje.", " %"),
        ("=", "{F} ¿Cuántos puntos de la lista no cumplen?", "12-9", "Se resta lo que cumple al total de puntos.", " puntos"),
        ("abc", "{F} ¿Qué corresponde hacer con los 3 puntos que no cumplen?", "Informarlos y corregirlos antes de aceptar el artefacto", "Aceptar igual, porque cumple el 75 %", "Marcarlos como «cumple» para cerrar la lista", "Un artefacto con puntos incumplidos no se acepta hasta corregirlos."),
        ("abc", "{F} ¿Qué debe revisar quien lee el registro de prueba que dice «cumple»?", "Que tenga fecha, responsable y resultado, sin repetir la prueba", "Que él mismo repita la prueba", "Solo que tenga un sello de colores", "Quien lee comprueba el documento; la prueba la hace personal autorizado."),
        ("abc", "{F} Un compañero propone repetir la prueba de funcionamiento de un artefacto instalado «para estar seguros». ¿Qué respuesta es correcta?", "No: las pruebas las hace personal autorizado y un estudiante lee sus registros", "Sí: probar es fácil", "Sí, si usa el manual", "La prueba de funcionamiento de una instalación no es tarea de un estudiante."),
        ("abc", "¿Cuál es el mejor registro de la comparación y la recepción?", "Costo por año de cada modelo, puntos incumplidos de la lista, evidencia revisada y quién decide", "Se compró el M2", "El lavamanos estaba bien", "Un registro completo permite revisar la decisión."),
    ],
    ctx=("abc", "Un proveedor de ejemplo ofrece el modelo M2 con un descuento y te pide que firmes la recepción sin revisar la lista «porque llegó bien embalado». ¿Qué respondes?", "Que debes revisar la lista de recepción antes de firmar, aunque el embalaje se vea bien", "Que firmas, porque confías en el embalaje", "Que firmas y revisas después", "La firma de recepción acredita lo que se revisó."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se calcula el costo por año?", "Precio dividido en los años de vida útil", "Reparte el precio en el tiempo esperado de uso."),
        ("¿Qué se hace con un punto incumplido de la lista de recepción?", "Se informa y se corrige antes de aceptar", "Un artefacto con puntos incumplidos no se acepta."),
        ("¿Quién realiza una prueba de funcionamiento de una instalación?", "Personal autorizado", "El estudiante solo lee los registros."),
    ],
    op=("Ficha de ejemplo: modelo P1 cuesta $48.000 y dura 8 años; modelo P2 cuesta $90.000 y dura 18 años. La lista de recepción tiene 10 puntos y cumplen 7. Escribe (a) el costo por año de cada modelo, (b) cuál conviene, (c) el porcentaje de la lista que cumple, (d) qué harías con los puntos incumplidos.",
        "(a) P1: 48.000 ÷ 8 = 6.000 pesos por año. P2: 90.000 ÷ 18 = 5.000 pesos por año. (b) P2. (c) 7 de 10 son 70 %. (d) Informarlos y corregirlos antes de aceptar el artefacto.",
        ["calcula ambos costos por año", "elige con ese criterio", "calcula el porcentaje", "propone informar y corregir"],
        ["hoja con los cálculos y la conclusión"],
        ["comparar solo el precio", "dividir al revés", "aceptar con puntos incumplidos"],
        "Pregunta: «¿qué otra condición, además del costo por año, miras?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula en papel el costo por año de tres artefactos de ejemplo con precios de $30.000, $60.000 y $90.000 y vidas útiles de 5, 12 y 15 años.",
    extend="Explica con un ejemplo por qué una lista de verificación llena sin evidencia no sirve.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El taller ficticio «Obras Sanitarias Andes» tiene seis equipos: taladro eléctrico, esmeril angular, sierra eléctrica, bomba de agua, compresor y escalera de tijera. "
     "Riesgos anotados: cortes, atrapamiento, ruido, proyección de partículas, electricidad y caídas. Documentos: el manual del fabricante de cada equipo y una pauta de inspección.")
build(
    O8, 1, F,
    use="Aprenderé qué significa verificar el funcionamiento de un equipo, qué riesgos tienen las herramientas y máquinas y cómo se ordenan las medidas de control, desde la más efectiva hasta la menos efectiva.",
    prior=["Sé que algunas tareas solo las hace personal autorizado.", "Sé qué es un manual del fabricante.", "Sé multiplicar."],
    explain=[
        "Verificar el funcionamiento de un equipo es comprobar, según el manual del fabricante y por personal autorizado, que está apto para usarse. Se hace antes de usarlo y de forma periódica. Este cuaderno no enseña a operar equipos ni herramientas: enseña a leer manuales y registros de inspección, y a decidir por escrito si un equipo se usa, se repara o se retira.",
        "Los riesgos de las herramientas y máquinas son cortes, atrapamientos, ruido, proyección de partículas, electricidad y caídas. Las medidas de control se ordenan de la más efectiva a la menos efectiva. Primero, eliminar el peligro. Segundo, sustituirlo por algo menos peligroso. Tercero, usar controles de ingeniería, como los resguardos, que son protecciones físicas que cubren las partes peligrosas. Cuarto, controles administrativos, como procedimientos, capacitación y señalización. Último, el equipo de protección personal (EPP), como casco o lentes, que no elimina el peligro. Un equipo con una falla se retira de servicio y se señaliza.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("verificar el funcionamiento", "comprobar, según el manual y por personal autorizado, que un equipo está apto para usarse"), ("resguardo", "protección física que cubre las partes peligrosas de una máquina"), ("equipo de protección personal (EPP)", "elemento que usa la persona para protegerse, como casco o lentes"), ("control de ingeniería", "medida física que reduce el riesgo, como un resguardo"), ("control administrativo", "medida de organización, como capacitación o señalización"), ("retirar de servicio", "dejar un equipo sin uso y señalizado hasta que se revise")],
    worked=[
        ("Ordenar las medidas", "En un taller de ejemplo hay ruido fuerte. Una medida es comprar protectores auditivos y otra es reemplazar la máquina por una más silenciosa. ¿Cuál es más efectiva según el orden?", ["Sustituir es una medida anterior al EPP.", "Reemplazar la máquina es más efectiva que los protectores."], "Reemplazar la máquina"),
        ("Contar inspecciones", "Un taller de ejemplo tiene 4 equipos y cada uno se inspecciona 3 veces al año. ¿Cuántas inspecciones son?", ["Se multiplican los equipos por las inspecciones.", "4 por 3 son 12."], "12 inspecciones"),
    ],
    mistakes=[("Creer que el EPP es la medida más importante.", "El EPP es el último recurso y no elimina el peligro.", "Antes de usar EPP se intenta eliminar, sustituir o proteger."),
              ("Seguir usando un equipo con una falla «solo un momento más».", "La falla puede causar un accidente.", "Retira el equipo de servicio, señalízalo y avisa a personal autorizado.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es un resguardo en una máquina?", "Una protección física que cubre las partes peligrosas", "Un manual de uso", "Un casco de seguridad", "El resguardo es un control de ingeniería que aísla las partes peligrosas."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es el equipo de protección personal (EPP)?", "Un elemento que usa la persona para protegerse, como casco o lentes", "Una norma escrita", "Una pauta de inspección", "El EPP protege a la persona pero no elimina el peligro."),
        ("abc", "En Instalaciones Sanitarias: ¿cuál es la medida de control más efectiva?", "Eliminar el peligro", "Usar EPP", "Poner un letrero", "Eliminar el peligro suprime el riesgo en su origen."),
        ("=", "{F} ¿Cuántas inspecciones al año suman los seis equipos si cada uno se inspecciona 2 veces?", "6*2", "Se multiplican los equipos por las inspecciones de cada uno.", " inspecciones"),
        ("abc", "{F} ¿Qué documento de la ficha dice qué puntos revisar de un equipo?", "La pauta de inspección", "El manual de otro equipo", "La factura de compra", "La pauta de inspección ordena los puntos a revisar."),
        ("abc", "{F} ¿Qué riesgo de la ficha está asociado al esmeril angular?", "Proyección de partículas y cortes", "Pérdida de las pautas", "Sobrecarga del estante", "El esmeril lanza partículas y puede cortar."),
        ("=", "{F} Cada equipo tiene un manual de 12 páginas. Si se imprime una copia de cada manual, ¿cuántas páginas son?", "6*12", "Se multiplican los equipos por las páginas de cada manual.", " páginas"),
        ("abc", "En un taller de ejemplo hay un esmeril sin su resguardo. ¿Qué corresponde?", "Retirarlo de servicio, señalizarlo y avisar a personal autorizado", "Usarlo con lentes de seguridad", "Usarlo solo un rato", "Sin resguardo falta un control de ingeniería; el EPP no lo reemplaza."),
        ("abc", "Una persona de ejemplo queda atrapada en una máquina del taller. ¿Qué corresponde según las reglas generales?", "No acercarse a la máquina, avisar a un adulto responsable y a emergencias", "Intentar sacarla con las manos", "Encender la máquina de nuevo para liberarla", "Acercarse o manipular la máquina puede causar más daño; se avisa a quienes pueden rescatar."),
        ("ab", "Un estudiante de ejemplo quiere probar el taladro del taller porque «leyó el manual». ¿Qué corresponde?", "No hacerlo: usar equipos exige personal autorizado y capacitación", "Hacerlo con lentes puestos", "Leer el manual no habilita para operar; el cuaderno solo enseña a leer y a decidir."),
        ("abc", "{F} El taller propone solo repartir cascos y lentes para reducir los riesgos. ¿Qué respuesta es correcta?", "El EPP es el último recurso: antes hay que eliminar, sustituir o proteger con resguardos", "El EPP basta, porque protege del todo", "El EPP es más efectivo que los resguardos", "El EPP no elimina el peligro y está al final del orden de control."),
        ("=", "{F} El taller retira 2 de los 6 equipos de servicio por fallas. ¿Cuántos equipos quedan en uso?", "6-2", "Se restan los equipos retirados al total de equipos.", " equipos"),
        ("abc", "¿Cuál es el orden correcto de las medidas de control, de la más efectiva a la menos efectiva?", "Eliminar, sustituir, controles de ingeniería, controles administrativos y EPP", "EPP, controles administrativos, controles de ingeniería, sustituir y eliminar", "Controles administrativos, EPP, eliminar, sustituir y controles de ingeniería", "El orden va de actuar sobre el origen a proteger a la persona."),
    ],
    ctx=("abc", "El dueño de un taller de ejemplo te pide: «usa el esmeril que no tiene resguardo, pero ponte lentes y listo». ¿Qué respondes?", "Que no lo usarás: sin resguardo debe retirarse de servicio y avisar a personal autorizado", "Que lo usas, con lentes", "Que lo usas, pero más lento", "El EPP no reemplaza un resguardo; usar el equipo es de riesgo alto."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cuál es el último recurso de control?", "El equipo de protección personal", "No elimina el peligro, solo protege a la persona."),
        ("¿Qué se hace con un equipo con una falla?", "Se retira de servicio y se señaliza", "Así nadie lo usa por error."),
        ("¿Quién opera los equipos y herramientas de un taller?", "Personal autorizado y capacitado", "Este cuaderno no habilita para operar equipos."),
    ],
    op=("Ficha de ejemplo: un taller tiene 8 equipos y cada uno se inspecciona 2 veces al año. Hay una máquina con ruido fuerte y una sierra sin resguardo. Escribe (a) cuántas inspecciones al año suman, (b) qué medida de control es más efectiva para el ruido: reemplazar la máquina o dar protectores auditivos, y por qué, (c) qué harías con la sierra sin resguardo.",
        "(a) 8 × 2 = 16 inspecciones. (b) Reemplazar la máquina, porque sustituir el peligro es más efectivo que el EPP. (c) Retirarla de servicio, señalizarla y avisar a personal autorizado.",
        ["calcula las inspecciones", "elige la medida más efectiva con la razón", "propone retirar la sierra de servicio"],
        ["hoja con las tres respuestas"],
        ["multiplicar mal", "elegir el EPP como mejor medida", "proponer usar la sierra sin resguardo"],
        "Pregunta: «¿qué medidas van antes del EPP?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres riesgos de un taller sanitario y, para cada uno, una medida de cada nivel: eliminar o sustituir, control de ingeniería y EPP.",
    extend="Explica con un ejemplo por qué el EPP no reemplaza a un resguardo.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (placa de datos y señales, de ejemplo, inventadas). Bomba de agua modelo B-1: caudal máximo 40 L/min; potencia 750 W; uso continuo máximo 2 horas seguidas y luego una pausa. "
     "Señales de ejemplo: un círculo rojo con una raya indica prohibición; un círculo azul indica obligación; un triángulo amarillo indica advertencia; un rectángulo verde indica salida o seguridad. "
     "Hoja de vida de la bomba: instalada en el mes 0; inspecciones en los meses 3 y 6.")
build(
    O8, 2, F,
    use="Aprenderé el vocabulario de los documentos de un equipo (manual, placa de datos, hoja de vida, pauta), la señalética de seguridad, qué EPP corresponde a cada riesgo y los roles del taller.",
    prior=["Sé qué es el EPP.", "Sé leer una tabla de datos.", "Sé qué es una pauta de inspección."],
    explain=[
        "La placa de datos es una etiqueta fija en el equipo con sus datos nominales: lo que el fabricante indica que puede hacer, como su caudal máximo, su potencia o su tiempo de uso continuo. Superar esos límites daña el equipo y es riesgoso. La hoja de vida registra las inspecciones, fallas y reparaciones. La pauta de inspección lista los puntos a revisar. Un certificado de calibración indica que un instrumento de medición fue comparado con un patrón y está dentro de lo permitido.",
        "La señalética usa formas y colores convenidos: el círculo rojo con una raya indica una prohibición, el círculo azul una obligación, el triángulo amarillo una advertencia y el rectángulo verde una salida o condición segura. Cada riesgo se asocia a un EPP: casco para golpes en la cabeza, lentes para partículas, protectores auditivos para ruido y calzado de seguridad para golpes en los pies. Los roles son: el técnico autorizado inspecciona y opera, el supervisor planifica, el prevencionista cuida la seguridad y el encargado de herramientas controla su entrega y estado.",
        f"Los datos de esta ficha son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("placa de datos", "etiqueta fija en el equipo con sus datos nominales"), ("datos nominales", "valores que el fabricante indica como los que el equipo puede dar o soportar"), ("hoja de vida", "registro de las inspecciones, fallas y reparaciones de un equipo"), ("certificado de calibración", "documento que indica que un instrumento fue comparado con un patrón"), ("señalética", "conjunto de señales de seguridad con formas y colores convenidos"), ("encargado de herramientas", "persona que controla la entrega y el estado de las herramientas")],
    worked=[
        ("Leer una señal", "Una señal de ejemplo es un círculo azul con un casco dibujado. ¿Qué indica?", ["El círculo azul indica obligación.", "Indica que el uso del casco es obligatorio."], "Obligación de usar casco"),
        ("Leer una placa", "La placa de un equipo de ejemplo dice: uso continuo máximo 3 horas. Se usa 5 horas seguidas. ¿Cumple?", ["5 horas supera las 3 horas.", "No cumple."], "No cumple"),
    ],
    mistakes=[("Usar un equipo por encima del dato de su placa «porque aguanta».", "Superar los datos nominales daña el equipo y es riesgoso.", "Respeta los límites de la placa."),
              ("Confundir la señal de advertencia con la de prohibición.", "Una advertencia avisa un peligro y la prohibición impide una acción.", "Recuerda el color y la forma de cada una.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es la placa de datos de un equipo?", "Una etiqueta fija con los datos nominales que indica el fabricante", "La factura del equipo", "El manual completo", "La placa trae los límites y valores del fabricante."),
        ("abc", "En Instalaciones Sanitarias: ¿qué indica un círculo rojo con una raya?", "Una prohibición", "Una obligación", "Una salida segura", "El círculo rojo con una raya prohíbe una acción."),
        ("abc", "En Instalaciones Sanitarias: ¿qué indica un triángulo amarillo?", "Una advertencia de peligro", "Una obligación", "Una prohibición", "El triángulo amarillo advierte de un peligro."),
        ("=", "{F} ¿Cuántos minutos son las 2 horas de uso continuo máximo de la bomba?", "2*60", "Se multiplican las horas por 60 minutos.", " minutos"),
        ("abc", "{F} ¿Qué indica el rectángulo verde de la ficha?", "Una salida o condición segura", "Una prohibición", "Una advertencia", "El verde indica seguridad o salida."),
        ("abc", "{F} Según la placa, ¿cuál es el caudal máximo de la bomba?", "40 L/min", "750 L/min", "2 L/min", "El caudal máximo es el dato de 40 L/min; 750 es la potencia en W."),
        ("abc", "Un trabajador de ejemplo opera una máquina que lanza partículas. ¿Qué EPP corresponde a ese riesgo?", "Lentes de seguridad", "Protectores auditivos", "Casco", "Los lentes protegen los ojos de las partículas."),
        ("abc", "Un taller de ejemplo tiene mucho ruido. ¿Qué EPP corresponde a ese riesgo?", "Protectores auditivos", "Lentes de seguridad", "Calzado de seguridad", "Los protectores auditivos atenúan el ruido."),
        ("=", "{F} ¿Cuántos meses pasan entre la instalación de la bomba y su última inspección?", "6-0", "Se resta el mes de instalación al mes de la última inspección.", " meses"),
        ("abc", "{F} Si la inspección es cada 3 meses, ¿en qué mes toca la próxima?", "En el mes 9", "En el mes 8", "En el mes 12", "Se suma la frecuencia de 3 meses al mes de la última inspección, el mes 6."),
        ("abc", "{F} Un compañero dice: «la bomba aguanta 3 horas seguidas, solo dice 2 por cuidarse». ¿Qué respuesta es correcta?", "No: la placa fija un límite y no se supera", "Sí: las placas son muy exigentes", "Sí, si se mira la bomba mientras trabaja", "Los datos nominales son el límite que indica el fabricante."),
        ("=", "{F} Una tarea necesita 5 horas de trabajo de la bomba; en cada bloque se usa el máximo continuo. ¿Cuántos bloques hacen falta?", "(5+1)//2", "Se divide el tiempo entre las 2 horas máximas y se redondea hacia arriba.", " bloques"),
        ("abc", "¿Quién controla la entrega y el estado de las herramientas del taller?", "El encargado de herramientas", "El cliente", "El proveedor", "Ese es el rol del encargado de herramientas."),
    ],
    ctx=("abc", "Un trabajador de ejemplo dice que «el letrero de prohibición está de adorno» y usa la herramienta de todos modos. ¿Qué respondes?", "Que la señal indica una prohibición y que debe respetarla; si hay duda, consulta al prevencionista", "Que si lo hace con cuidado no importa", "Que mejor tapa el letrero", "Las señales de seguridad se cumplen; la duda se consulta al prevencionista."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué indica un círculo azul?", "Una obligación", "El azul indica algo que se debe hacer."),
        ("¿Qué EPP protege los ojos de las partículas?", "Los lentes de seguridad", "Cada riesgo se asocia a un EPP."),
        ("¿Qué contiene la hoja de vida de un equipo?", "Inspecciones, fallas y reparaciones", "Es la historia escrita del equipo."),
    ],
    op=("Ficha de ejemplo: compresor modelo C-1: uso continuo máximo 3 horas, inspecciones cada 4 meses; instalado en el mes 0, última inspección en el mes 8. Señales: círculo rojo con raya, círculo azul, triángulo amarillo. Escribe (a) en qué mes toca la próxima inspección, (b) cuántos minutos son las 3 horas de uso continuo, (c) qué indica el círculo azul y el triángulo amarillo, (d) qué EPP asocias a un riesgo de ruido.",
        "(a) 8 + 4 = mes 12. (b) 3 × 60 = 180 minutos. (c) El círculo azul indica obligación y el triángulo amarillo, advertencia. (d) Protectores auditivos.",
        ["calcula la próxima inspección", "convierte las horas a minutos", "interpreta las dos señales", "asocia el EPP al riesgo"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal los meses", "confundir señales", "asociar lentes al ruido"],
        "Pregunta: «¿qué pasa si se supera el uso continuo de la placa?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Dibuja en papel una señal de prohibición, una de obligación y una de advertencia y escribe una frase de ejemplo para cada una.",
    extend="Explica con un ejemplo por qué un certificado de calibración importa para un instrumento de medición.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (registro de inspección de ejemplo, inventado; las inspecciones las hizo personal autorizado). Mes actual: 7. Equipo; mes de la última inspección; frecuencia en meses; resultado. "
     "Taladro: 2; 3; apto. Esmeril: 1; 3; no apto, falta el resguardo. Sierra: 4; 6; apto. Bomba: 3; 6; apto. Compresor: 0; 6; apto. Escalera: 5; 12; no apto, peldaño dañado. "
     "Un equipo está vencido si el mes de su próxima inspección es menor o igual que el mes actual. Solo se usa un equipo apto y no vencido.")
build(
    O8, 3, F,
    use="Aprenderé a leer un registro de inspección, a calcular cuándo vence cada control y a decidir por escrito qué equipos se usan y cuáles se retiran de servicio.",
    prior=["Sé sumar meses.", "Sé qué es una frecuencia.", "Sé que un equipo con falla se retira de servicio."],
    explain=[
        "Un registro de inspección ordena, para cada equipo, cuándo se inspeccionó por última vez, cada cuánto debe inspeccionarse y qué resultado dio. La próxima inspección se calcula sumando la frecuencia al mes de la última. Si ese mes ya llegó o pasó, el control está vencido: aunque el equipo parezca bien, no se usa hasta que personal autorizado lo inspeccione.",
        "Un equipo declarado no apto se retira de servicio y se señaliza, y se informa al supervisor. Para decidir se combinan dos condiciones: el resultado debe ser apto y el control no debe estar vencido. La decisión se anota con los datos que la respaldan, para que cualquier persona pueda revisarla.",
        f"Este análisis es de lectura de un registro: no incluye abrir ni probar equipos. {EMER} {AVISO}",
    ],
    vocab=[("registro de inspección", "tabla con la última inspección, la frecuencia y el resultado de cada equipo"), ("apto", "equipo que superó la inspección"), ("no apto", "equipo que no superó la inspección"), ("control vencido", "inspección cuya fecha ya llegó o pasó"), ("próxima inspección", "mes de la última más la frecuencia")],
    worked=[
        ("Próxima inspección", "Un equipo de ejemplo se inspeccionó en el mes 2 y se inspecciona cada 4 meses. ¿Cuándo toca la próxima?", ["Se suma la frecuencia al mes de la última.", "2 más 4 son 6."], "En el mes 6"),
        ("Vencido o vigente", "Con mes actual 9, un equipo de ejemplo tiene su próxima inspección en el mes 12. ¿Está vencido?", ["El mes 12 es posterior al mes 9.", "No está vencido: el control sigue vigente."], "No, está vigente"),
    ],
    mistakes=[("Usar un equipo con control vencido porque «se ve bien».", "El control vencido significa que no hay constancia vigente de que esté apto.", "No lo uses hasta que personal autorizado lo inspeccione."),
              ("Mirar solo el resultado y olvidar la fecha del control.", "Un equipo apto con control vencido tampoco se usa.", "Combina las dos condiciones.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿cuándo está vencido un control de inspección?", "Cuando el mes de la próxima inspección ya llegó o pasó", "Cuando el equipo es nuevo", "Cuando el equipo fue aprobado", "Un control vencido ya cumplió su plazo y debe repetirse."),
        ("abc", "En Instalaciones Sanitarias: ¿cómo se calcula la próxima inspección?", "Sumando la frecuencia al mes de la última inspección", "Restando la frecuencia al mes actual", "Multiplicando los meses por dos", "La próxima fecha es la última más la frecuencia."),
        ("abc", "En Instalaciones Sanitarias: ¿qué significa que un equipo sea «no apto»?", "Que no superó la inspección y se retira de servicio", "Que es muy antiguo", "Que está sin usar", "No apto es un resultado de la inspección."),
        ("=", "{F} ¿En qué mes toca la próxima inspección del taladro?", "2+3", "Se suma la frecuencia de 3 meses al mes de la última inspección.", ""),
        ("=", "{F} ¿En qué mes toca la próxima inspección de la sierra?", "4+6", "Se suma la frecuencia de 6 meses al mes de la última inspección.", ""),
        ("=", "{F} ¿En qué mes toca la próxima inspección del compresor?", "0+6", "Se suma la frecuencia de 6 meses al mes de la última inspección.", ""),
        ("abc", "{F} ¿Qué equipos tienen su control vencido en el mes actual 7?", "El taladro, el esmeril y el compresor", "Solo la sierra y la bomba", "Solo la escalera", "Sus próximas inspecciones son los meses 5, 4 y 6, que ya pasaron."),
        ("abc", "{F} ¿Qué equipos están declarados no aptos?", "El esmeril y la escalera", "El taladro y el compresor", "La sierra y la bomba", "El registro marca esmeril sin resguardo y escalera con peldaño dañado."),
        ("=", "{F} ¿Cuántos equipos son aptos y tienen su control vigente?", "6-4", "De los 6 equipos se restan los 4 que están vencidos o no aptos.", " equipos"),
        ("abc", "{F} ¿Qué equipos se pueden usar según la regla de la ficha?", "La sierra y la bomba", "El taladro y el compresor", "Los seis equipos", "Solo la sierra y la bomba son aptos y con control vigente."),
        ("abc", "{F} Un compañero dice: «el taladro está apto, así que se puede usar». ¿Qué respuesta es correcta?", "No: su control está vencido y debe inspeccionarlo personal autorizado", "Sí: apto significa que se puede usar", "Sí, si se usa poco tiempo", "Un control vencido no permite usar el equipo."),
        ("=", "{F} ¿Cuántos equipos están vencidos o no aptos? (El esmeril está en ambos grupos y se cuenta una sola vez.)", "3+2-1", "Se suman vencidos y no aptos y se resta el esmeril, que se contó dos veces.", " equipos"),
        ("abc", "{F} ¿Cuál es el mejor registro de la decisión?", "Equipos aptos y vigentes, equipos vencidos, equipos no aptos y a quién se informó", "Algunos equipos no sirven", "Se podrán usar los equipos", "Un registro útil lista los equipos y las razones de la decisión."),
    ],
    ctx=("abc", "El supervisor de ejemplo tiene una urgencia y dice: «usemos el taladro aunque esté vencido, hoy no hay tiempo». ¿Qué propones?", "Registrar el control vencido, no usarlo y pedir la inspección a personal autorizado antes de usarlo", "Usarlo solo hoy", "Cambiar la fecha en el registro", "Alterar o saltarse un control pone en riesgo a las personas."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se sabe si un control está vencido?", "Comparando el mes de la próxima inspección con el mes actual", "Si ya llegó o pasó, está vencido."),
        ("¿Qué dos condiciones debe cumplir un equipo para usarse?", "Ser apto y tener el control vigente", "Cumplir solo una de las dos condiciones no basta."),
        ("¿Qué se hace con un equipo no apto?", "Se retira de servicio y se señaliza", "Así no se usa por error."),
    ],
    op=("Ficha de ejemplo: mes actual 10. Equipo; última inspección; frecuencia en meses; resultado. Sierra: 6; 3; apto. Bomba: 2; 6; apto. Taladro: 8; 4; no apto, cable dañado. Compresor: 5; 6; apto. Escribe (a) el mes de la próxima inspección de cada equipo, (b) cuáles están vencidos, (c) cuáles se pueden usar, (d) qué harías con el no apto.",
        "(a) Sierra: 9; bomba: 8; taladro: 12; compresor: 11. (b) Sierra y bomba, porque 9 y 8 son menores o iguales que 10. (c) Solo el compresor, que es apto y con control vigente. (d) El taladro se retira de servicio, se señaliza y se informa al supervisor.",
        ["calcula las próximas inspecciones", "identifica los vencidos", "decide cuál se puede usar", "propone retirar el equipo no apto"],
        ["hoja con la tabla de cálculo y la decisión"],
        ["sumar mal los meses", "olvidar que apto y vencido no se puede usar", "no retirar el equipo no apto"],
        "Pregunta: «¿cuál sería tu decisión con la sierra?». Si no responde, pídele que relea la regla de las dos condiciones."),
    reinforce="Escribe un registro de inspección de ejemplo con cuatro equipos, sus frecuencias y resultados, y decide cuáles se usan.",
    extend="Explica con un ejemplo por qué un equipo apto con control vencido no se usa.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (comparación con la placa de datos, de ejemplo, inventada). Bomba de agua B-1: caudal máximo 40 L/min; uso continuo máximo 2 horas seguidas y luego una pausa. "
     "Tarea planificada: abastecer tres puntos de agua a la vez que piden 15, 20 y 12 L/min, durante 5 horas de trabajo. Alternativa del supervisor: abastecer en dos turnos, el primero con los puntos de 15 y 20 L/min y el segundo con el de 12 L/min. "
     "Riesgos del taller y EPP disponibles: ruido, partículas, golpes en los pies y caída de objetos; protectores auditivos, lentes, calzado de seguridad y casco.")
build(
    O8, 4, F,
    use="Aprenderé a aplicar un criterio técnico: comparar la demanda de una tarea con los datos de la placa, decidir si el equipo sirve y asociar el EPP a cada riesgo.",
    prior=["Sé leer una placa de datos.", "Sé sumar caudales.", "Sé asociar EPP a riesgos."],
    explain=[
        "Un criterio técnico compara una exigencia con un límite. Si la demanda de una tarea supera el dato nominal de la placa, el equipo no sirve para esa tarea tal como está planteada y se rediseña la tarea o se busca otro equipo; nunca se fuerza el equipo ni se modifica su protección. En una bomba, la demanda de caudal es la suma de lo que piden los puntos que se abastecen a la vez. El tiempo de uso continuo también tiene un límite: el trabajo se divide en bloques con pausas.",
        "El EPP se asigna según el riesgo que no pudo eliminarse: protectores auditivos para el ruido, lentes para las partículas, calzado de seguridad para los golpes en los pies y casco para la caída de objetos. Se registra qué EPP corresponde a cada riesgo y quién lo entrega. El EPP complementa los controles anteriores y no los reemplaza.",
        f"Los datos de esta ficha son de ejemplo y no son indicaciones de uso de equipos. {EMER} {AVISO}",
    ],
    vocab=[("demanda", "lo que exige una tarea, por ejemplo un caudal"), ("dato nominal", "límite que indica el fabricante en la placa"), ("bloque de trabajo", "período de uso continuo entre pausas"), ("rediseñar la tarea", "cambiar cómo se organiza la tarea para respetar los límites del equipo"), ("asignar EPP", "decidir qué elemento de protección corresponde a cada riesgo")],
    worked=[
        ("Comparar con la placa", "Una bomba de ejemplo admite 30 L/min y dos puntos piden 12 y 15 L/min. ¿Sirve?", ["La demanda total es 12 más 15, es decir 27 L/min.", "27 no supera 30: sirve."], "Sí, sirve"),
        ("Bloques de trabajo", "Una tarea de ejemplo exige 4 horas y el equipo admite 3 horas seguidas. ¿Cuántos bloques hacen falta?", ["4 dividido en 3 da 1 y sobra tiempo.", "Se redondea hacia arriba: 2 bloques."], "2 bloques"),
    ],
    mistakes=[("Forzar el equipo por encima de su placa para terminar antes.", "Superar el límite daña el equipo y es riesgoso.", "Rediseña la tarea o usa otro equipo."),
              ("Entregar EPP sin revisar qué riesgo cubre.", "Un elemento inadecuado da falsa seguridad.", "Asocia cada EPP al riesgo que corresponde.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es un dato nominal de una placa?", "El límite o valor que indica el fabricante", "El precio del equipo", "El color del equipo", "La placa trae los valores que fija el fabricante."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es un bloque de trabajo?", "Un período de uso continuo entre pausas", "Un conjunto de equipos", "Un tipo de herramienta", "El trabajo se divide en bloques para respetar el uso continuo máximo."),
        ("abc", "En Instalaciones Sanitarias: ¿qué significa rediseñar una tarea?", "Cambiar su organización para respetar los límites del equipo", "Forzar el equipo hasta que aguante", "Quitarle la placa al equipo", "Rediseñar es adaptar la tarea al equipo, no el equipo a la tarea."),
        ("=", "{F} ¿Cuántos L/min piden juntos los tres puntos de agua?", "15+20+12", "Se suman los caudales de los tres puntos.", " L/min"),
        ("abc", "{F} ¿Sirve la bomba B-1 para abastecer los tres puntos a la vez?", "No, porque piden 47 L/min y la placa admite 40 L/min", "Sí, porque 47 es cercano a 40", "Sí, si se abre más la llave", "La demanda de 47 L/min supera el máximo de 40 L/min."),
        ("=", "{F} ¿Cuántos L/min piden juntos los puntos del primer turno de la alternativa del supervisor?", "15+20", "Se suman los caudales de los dos puntos del turno.", " L/min"),
        ("abc", "{F} ¿Cumple el primer turno de la alternativa con la placa de la bomba?", "Sí, porque 35 L/min no supera 40 L/min", "No, porque 35 es mayor que 40", "No se puede saber", "El turno pide 35 L/min, menos que el máximo."),
        ("abc", "{F} ¿Cumple el segundo turno, con el punto de 12 L/min?", "Sí, porque 12 L/min es menos que 40 L/min", "No, porque un turno necesita dos puntos", "No, porque 12 es muy pequeño", "12 L/min está dentro del límite de la bomba."),
        ("=", "{F} Si cada bloque usa el máximo continuo de 2 horas, ¿cuántos bloques hacen falta para las 5 horas de trabajo?", "(5+1)//2", "Se divide el tiempo entre el máximo continuo y se redondea hacia arriba.", " bloques"),
        ("=", "{F} ¿Cuántas pausas hay entre esos bloques?", "(5+1)//2-1", "Entre n bloques hay una pausa menos que bloques.", " pausas"),
        ("abc", "{F} ¿Qué EPP asocias al riesgo de partículas?", "Lentes de seguridad", "Protectores auditivos", "Casco", "Los lentes protegen los ojos de las partículas."),
        ("abc", "{F} ¿Qué EPP asocias al riesgo de golpes en los pies?", "Calzado de seguridad", "Casco", "Lentes de seguridad", "El calzado de seguridad protege los pies de golpes."),
        ("abc", "{F} El supervisor propone usar la bomba con los tres puntos y «quitarle el límite de uso continuo». ¿Qué respuesta es correcta?", "No: el límite de la placa no se anula; se usa la alternativa en turnos y bloques", "Sí: los límites son sugerencias", "Sí, si se vigila la bomba", "Los límites del fabricante se respetan y no se modifican."),
    ],
    ctx=("abc", "El dueño de un taller de ejemplo dice: «saca la protección de la bomba para que rinda más». ¿Qué respondes?", "Que no se quitan protecciones; se rediseña la tarea con los límites de la placa", "Que la sacas, pero solo hoy", "Que la sacas y compras otra después", "Quitar una protección aumenta el riesgo; los equipos se usan según el manual."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué se hace si la demanda supera el dato de la placa?", "Se rediseña la tarea o se busca otro equipo", "No se fuerza el equipo ni se anulan sus protecciones."),
        ("¿Qué EPP corresponde al ruido?", "Protectores auditivos", "Cada riesgo tiene un EPP asociado."),
        ("¿Quién decide cambios en el uso de un equipo?", "El supervisor con personal autorizado", "Los límites del fabricante no se modifican por cuenta propia."),
    ],
    op=("Ficha de ejemplo: bomba con máximo de 50 L/min y uso continuo máximo de 3 horas. Tarea: abastecer tres puntos que piden 20, 25 y 15 L/min durante 7 horas. Riesgos: ruido y caída de objetos. Escribe (a) la demanda de los tres puntos a la vez y si sirve, (b) un reparto en dos turnos que cumpla, (c) cuántos bloques de trabajo hacen falta para las 7 horas, (d) qué EPP asocias a cada riesgo.",
        "(a) 20 + 25 + 15 = 60 L/min, que supera los 50 L/min: no sirve. (b) Turno 1 con 25 y 15 (40 L/min) y turno 2 con 20 L/min. (c) 7 ÷ 3 da 2 y sobra; se necesitan 3 bloques. (d) Ruido: protectores auditivos; caída de objetos: casco.",
        ["calcula la demanda y compara", "propone un reparto que cumple", "calcula los bloques", "asocia el EPP a cada riesgo"],
        ["hoja con los cálculos y las asignaciones"],
        ["no sumar todos los puntos", "redondear hacia abajo los bloques", "asociar mal el EPP"],
        "Pregunta: «¿qué harías si el supervisor quisiera ignorar el límite?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Arma en papel un reparto en turnos para cuatro puntos que piden 10, 20, 25 y 15 L/min con una bomba de máximo 45 L/min.",
    extend="Explica con un ejemplo por qué los límites de una placa de datos no se anulan.",
)
