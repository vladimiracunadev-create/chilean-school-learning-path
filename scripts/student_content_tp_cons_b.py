"""Construcción TP 3.º medio: OAE-04 (carpintería de instalación de faenas, solo vocabulario y cubicación), OAE-05 (cubicación) y OAE-06 (equipos y herramientas: manuales y registros). Solo conceptos, documentos y planillas, con datos de ejemplo."""
from __future__ import annotations

from tp_cons_common import AVISO, EMER, build

O4 = "TP-CONS-3-OAE-04"
O5 = "TP-CONS-3-OAE-05"
O6 = "TP-CONS-3-OAE-06"

# ============================================================ OAE-04, clase 1
F = ("Ficha 15 (obra de ejemplo, inventada). Obra «Condominio Peumo»: plano de instalación de faenas con una bodega de 6 m por 3 m, una oficina de 4 m por 3 m, un comedor de 5 m por 3 m y un cierro de 60 m de largo. "
     "Riesgos anotados: corte con herramientas, golpe, caída, ruido y polvo de madera. Elementos de protección personal (EPP) exigidos en el ejemplo: casco, lentes, guantes, protección auditiva y zapatos de seguridad.")
build(
    O4, 1, F,
    use="Aprenderé qué es la instalación de faenas, qué trabajos de carpintería incluye, qué riesgos tiene y cómo se ordenan los controles de seguridad.",
    prior=["Sé leer un plano descrito por escrito.", "Sé calcular áreas de rectángulos.", "Sé qué es un riesgo."],
    explain=[
        "La instalación de faenas es el conjunto de construcciones y servicios provisorios que se arman al comienzo de una obra: bodega, oficina, comedor, baños y cierro perimetral. La carpintería de obra es el trabajo con madera y tableros para esas instalaciones y para otras partes de la obra. Se hace según los trazados y los planos. Los elementos de construcción son las piezas con que se arman: maderas, tableros, clavos, tornillos y herramientas. Este cuaderno solo enseña su vocabulario y a calcular cantidades.",
        "La seguridad se piensa con una jerarquía de controles, de más a menos efectiva: eliminar el riesgo, sustituirlo por otro menor, usar protecciones o barreras, organizar el trabajo con capacitación y señales, y por último usar elementos de protección personal (EPP), como casco, lentes, guantes, protección auditiva y zapatos de seguridad. El EPP es la última barrera y cada tipo protege un riesgo distinto. Las herramientas y su uso las maneja solo personal capacitado y autorizado, según la norma vigente.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("instalación de faenas", "construcciones y servicios provisorios de una obra"), ("carpintería de obra", "trabajo con madera y tableros en una obra"), ("EPP", "elemento de protección personal"), ("jerarquía de controles", "orden de medidas de seguridad, de la más a la menos efectiva"), ("cierro perimetral", "cierre que rodea la obra")],
    worked=[
        ("Elegir un EPP", "Una persona de ejemplo está cerca de trabajos que lanzan partículas hacia la cara. ¿Qué EPP la protege?", ["La amenaza apunta a los ojos.", "Los lentes de seguridad protegen los ojos."], "Lentes de seguridad"),
        ("Sumar superficies", "Una faena de ejemplo tiene dos recintos: uno de 4 m por 2 m y otro de 3 m por 3 m. ¿Cuántos m² suman?", ["Se calcula cada área: 8 y 9.", "Se suman: 8 más 9 son 17."], "17 m²"),
    ],
    mistakes=[("Pensar que con el casco ya no hacen falta las otras protecciones.", "Cada EPP protege un riesgo distinto.", "Usa el EPP que el riesgo exige, además de las otras medidas."),
              ("Tomar una herramienta ajena «solo un momento».", "Su uso exige capacitación y autorización.", "Pide la herramienta al responsable autorizado.")],
    T=[
        ("abc", "En Construcción: ¿qué es la instalación de faenas?", "Las construcciones y servicios provisorios de una obra", "El plano de arquitectura del edificio terminado", "La entrega final de la obra al cliente", "La instalación de faenas es provisoria y de apoyo; no es el plano ni la entrega."),
        ("abc", "¿Qué es un EPP?", "Un elemento de protección personal", "Un equipo para pintar paredes", "Un plano de planta", "El EPP protege a la persona frente a un riesgo; no es una herramienta de pintura ni un plano."),
        ("abc", "En la jerarquía de controles, ¿qué medida es la más efectiva?", "Eliminar el riesgo", "Usar un EPP", "Poner una señal", "Eliminar el riesgo lo quita por completo; el EPP es la última barrera."),
        ("=", "{F} ¿Cuántos m² suman la bodega, la oficina y el comedor?", "6*3+4*3+5*3", "Se calcula el área de cada recinto y se suman.", " m²"),
        ("abc", "{F} ¿Qué riesgos anota la ficha?", "Corte, golpe, caída, ruido y polvo de madera", "Solo el corte con herramientas", "Corte, golpe y electrocución", "La ficha anota cinco riesgos; las otras opciones omiten o agregan alguno."),
        ("abc", "{F} Hay mucho ruido en la faena. ¿Qué EPP de la ficha corresponde?", "Protección auditiva", "Guantes", "Casco", "El ruido daña el oído y lo protege la protección auditiva; guantes y casco protegen otras partes."),
        ("=", "{F} Se entrega 1 pieza de cada uno de los 5 tipos de EPP a 8 personas. ¿Cuántas piezas se necesitan?", "5*8", "Cinco tipos por ocho personas.", " piezas"),
        ("abc", "{F} Una persona sin autorización quiere usar una sierra eléctrica de la bodega «un ratito». ¿Qué corresponde?", "No hacerlo: solo personal capacitado y autorizado usa la herramienta", "Hacerlo si usa lentes", "Hacerlo si alguien la mira", "Los lentes o la compañía no reemplazan la capacitación ni la autorización."),
        ("abc", "{F} Una herramienta tiene la protección rota. ¿Qué corresponde?", "No usarla y avisar para que la retiren o reparen personal autorizado", "Usarla con más cuidado", "Repararla con cinta", "Una herramienta con protección dañada es un riesgo; se retira y avisa."),
        ("ab", "{F} Un trabajador dice: «tengo casco, así que no necesito lentes ni protección auditiva». ¿Qué respuesta es correcta?", "No: cada EPP protege un riesgo distinto", "Sí: el casco protege de todo", "El casco protege la cabeza; ojos y oídos se protegen con otros EPP."),
        ("abc", "En una faena de ejemplo alguien se cae de una estructura provisoria y no puede levantarse. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Moverlo rápido para que se levante", "Esperar a que se recupere solo", "Mover a una persona caída puede agravarla; se mantiene la distancia segura y se avisa de inmediato."),
        ("=", "{F} El cierro de 60 m se divide en tramos de 3 m. ¿Cuántos tramos son?", "60//3", "Se divide el largo total por el largo de cada tramo.", " tramos"),
        ("abc", "{F} Se puede quitar un riesgo del todo cambiando la forma de trabajar. ¿Qué nivel de la jerarquía es?", "Eliminar el riesgo", "Usar EPP", "Capacitar", "Quitar el riesgo del todo es eliminarlo, el nivel más efectivo."),
    ],
    ctx=("abc", "Un estudiante en práctica ve que falta la protección auditiva en la bodega y tiene mucho trabajo. ¿Qué hace?", "Avisa al supervisor y no trabaja en la zona ruidosa hasta tenerla", "Trabaja un rato sin ella", "Usa algodón del botiquín", "Un EPP faltante no se reemplaza con improvisaciones; se avisa y se espera."),
    sc=[
        ("En Construcción: ¿qué es la carpintería de obra?", "El trabajo con madera y tableros en una obra", "Se aplica a instalaciones provisorias y partes de la obra."),
        ("¿Cuál es la última barrera en la jerarquía de controles?", "El EPP", "Se usa cuando las otras medidas no bastan."),
        ("¿Quién usa las herramientas eléctricas de la faena?", "Personal capacitado y autorizado", "Este cuaderno no habilita para usarlas."),
    ],
    op=("Obra de ejemplo «Faena Alerce»: bodega de 5 m por 4 m, oficina de 3 m por 3 m y comedor de 4 m por 3 m. Riesgos: corte, golpe y ruido. Escribe (a) cuántos m² suman los tres recintos, (b) un EPP para cada riesgo, (c) qué es la jerarquía de controles, (d) qué haces si ves una herramienta dañada.",
        "(a) 20+9+12 son 41 m². (b) Guantes para el corte, casco para el golpe, protección auditiva para el ruido. (c) Un orden de medidas de la más a la menos efectiva, que termina en el EPP. (d) No la uso y aviso a un responsable autorizado.",
        ["suma las áreas", "asocia un EPP a cada riesgo", "explica la jerarquía", "informa la herramienta dañada"],
        ["hoja con las cuatro respuestas"],
        ["olvidar un recinto", "decir que el casco protege de todo", "usar la herramienta dañada"],
        "Pregunta: «¿cuál es la medida más efectiva?». Si no responde, pídele que relea la jerarquía."),
    reinforce="Escribe los cinco niveles de la jerarquía de controles en orden y un ejemplo inventado de cada uno.",
    extend="Explica por qué el EPP se considera la última barrera y no la primera.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 16 (lista de ejemplo, inventada). Lista de materiales de un cobertizo de faena: 8 pies derechos de 240 cm; 4 soleras de 300 cm; 7 riostras de 120 cm; 10 tableros. "
     "Escuadría de los pies derechos: 7 cm por 7 cm (dato de ejemplo).")
build(
    O4, 2, F,
    use="Aprenderé el vocabulario de las piezas de una estructura liviana de madera y a leer una lista de materiales.",
    prior=["Sé multiplicar y sumar longitudes.", "Sé qué es una instalación de faenas.", "Sé leer una lista."],
    explain=[
        "Una estructura liviana de madera se arma con piezas que tienen nombres propios. El pie derecho es una pieza vertical que sostiene. La solera es una pieza horizontal a la que se unen los pies derechos. La riostra es una pieza inclinada que da rigidez. El tablero es una plancha que cubre una superficie. La escuadría es la medida de la sección de una pieza, por ejemplo 7 cm por 7 cm. La lista de materiales dice cuántas piezas hay de cada tipo y qué largo tienen.",
        "Para leer una lista se mira el nombre, la cantidad y el largo de cada pieza. Con ellos se calculan largos totales y cantidades de piezas. Un cambio de pieza, de escuadría o de cantidad lo decide el proyectista y no quien arma. Este cuaderno no enseña cómo se unen o se instalan las piezas: ese trabajo es de personal capacitado con norma vigente y protección.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("pie derecho", "pieza vertical que sostiene"), ("solera", "pieza horizontal a la que se unen los pies derechos"), ("riostra", "pieza inclinada que da rigidez"), ("tablero", "plancha que cubre una superficie"), ("escuadría", "medida de la sección de una pieza"), ("lista de materiales", "documento con tipo, cantidad y largo de cada pieza")],
    worked=[
        ("Largo total", "Una lista de ejemplo trae 5 piezas de 200 cm. ¿Cuántos cm suman?", ["Se multiplica la cantidad por el largo.", "5 por 200 son 1000."], "1000 cm"),
        ("Área de sección", "Una pieza de ejemplo tiene escuadría de 5 cm por 10 cm. ¿Cuántos cm² tiene su sección?", ["Se multiplica ancho por alto.", "5 por 10 son 50."], "50 cm²"),
    ],
    mistakes=[("Confundir pie derecho y solera.", "Uno es vertical y otro horizontal.", "Recuerda: el pie derecho está de pie, la solera va acostada."),
              ("Reemplazar una pieza por otra de distinta escuadría sin avisar.", "Cambia la resistencia y es una decisión de diseño.", "Informa al proyectista o al supervisor.")],
    T=[
        ("abc", "En Construcción: ¿qué es un pie derecho?", "Una pieza vertical que sostiene", "Una pieza horizontal a ras de suelo", "Una plancha que cubre una pared", "El pie derecho es vertical; la solera es horizontal y el tablero es una plancha."),
        ("abc", "En Construcción: ¿para qué sirve una riostra?", "Para dar rigidez con una pieza inclinada", "Para cubrir una superficie", "Para medir una distancia", "La riostra da rigidez; cubrir es función del tablero y medir de un instrumento."),
        ("abc", "¿Qué indica la escuadría de una pieza de madera?", "La medida de su sección", "Su precio", "El lugar de la obra donde va", "La escuadría describe la sección; precio y lugar son otros datos."),
        ("=", "{F} ¿Cuántos cm suman los largos de todos los pies derechos?", "8*240", "Se multiplica la cantidad por el largo de cada pieza.", " cm"),
        ("=", "{F} ¿Cuántas piezas de madera (pies derechos, soleras y riostras) hay en total?", "8+4+7", "Se suman las cantidades de las tres piezas.", " piezas"),
        ("=", "{F} ¿Cuántos cm² tiene la sección de un pie derecho?", "7*7", "Se multiplica ancho por alto.", " cm²"),
        ("=", "{F} ¿Cuántos cm de madera suman los pies derechos, las soleras y las riostras?", "8*240+4*300+7*120", "Se suma el largo total de cada tipo de pieza.", " cm"),
        ("abc", "{F} ¿Qué pieza de la lista da rigidez?", "Las riostras", "Los tableros", "Las soleras", "Las riostras inclinadas dan rigidez; las soleras son horizontales y los tableros cubren."),
        ("abc", "{F} Una pieza llega con una grieta profunda. ¿Qué corresponde?", "Apartarla y avisar al supervisor para que decida", "Usarla en un lugar que no se vea", "Taparla con pintura", "Una grieta puede debilitar la pieza; decide el supervisor."),
        ("ab", "{F} Un ayudante cambia los pies derechos por otros de 5 cm por 5 cm «porque son más baratos». ¿Qué respuesta es correcta?", "No: cambiar la escuadría es una decisión del proyectista", "Sí: son piezas equivalentes", "Una escuadría menor cambia la resistencia de la estructura."),
        ("abc", "{F} ¿Quién decide agregar una riostra más?", "El proyectista, informado por el supervisor", "El ayudante que arma", "Cualquiera que tenga una pieza sobrante", "Cambios de cantidad de piezas son de diseño."),
        ("=", "{F} ¿Cuántos tableros quedan si se ocupan 6 de los 10?", "10-6", "Se resta lo usado del total.", " tableros"),
        ("abc", "{F} ¿Cuál de estos datos NO está en la lista de la ficha?", "El precio de cada pieza", "La cantidad de pies derechos", "El largo de las soleras", "La ficha entrega cantidades y largos; los precios no aparecen."),
    ],
    ctx=("abc", "Un proveedor de ejemplo envía soleras de 280 cm en vez de 300. ¿Qué corresponde?", "Registrar la diferencia y consultar al supervisor antes de usarlas", "Usarlas igual porque son parecidas", "Alargarlas con otra pieza", "Una pieza de otro largo no cumple la lista; se registra y consulta."),
    sc=[
        ("En Construcción: ¿qué es una solera?", "Una pieza horizontal a la que se unen los pies derechos", "Es horizontal, a diferencia del pie derecho."),
        ("¿Cuántos cm suman 6 piezas de 150 cm?", "900 cm", "Se multiplica la cantidad por el largo."),
        ("¿Quién cambia la escuadría de una pieza?", "El proyectista", "Cambiar la escuadría altera el diseño."),
    ],
    op=("Lista de ejemplo de un cobertizo: 6 pies derechos de 200 cm; 3 soleras de 400 cm; 4 riostras de 100 cm; escuadría de pies derechos de 6 cm por 6 cm. Escribe (a) cuántas piezas hay, (b) cuántos cm suman los pies derechos, (c) el área de sección de un pie derecho, (d) qué haces si llega una solera de otro largo.",
        "(a) 6+3+4 son 13 piezas. (b) 6 por 200 son 1200 cm. (c) 6 por 6 son 36 cm². (d) Registro la diferencia y consulto al supervisor antes de usarla.",
        ["suma las piezas", "calcula el largo total", "calcula el área", "consulta antes de usar"],
        ["hoja con las cuatro respuestas"],
        ["sumar largos con cantidades", "confundir ancho por alto", "usar la pieza sin consultar"],
        "Pregunta: «¿cuál va vertical?». Si no responde, pídele que relea el vocabulario."),
    reinforce="Haz una tabla con las seis piezas del vocabulario y escribe cómo se orienta cada una.",
    extend="Explica por qué dos piezas del mismo largo pero distinta escuadría no son equivalentes.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 17 (caso de ejemplo, inventado). «Faena Quillay». Plano de instalación de faenas: cierro de 60 m en total, que incluye un portón de 6 m; el resto se cubre con módulos de 3 m cada uno. "
     "Lista de materiales: 20 módulos de cierro y 1 portón. En la obra trabajan 12 personas y la lista de EPP incluye 10 cascos. Regla de ejemplo para baños: 1 por cada 6 personas.")
build(
    O4, 3, F,
    use="Aprenderé a cruzar un plano de faenas con su lista de materiales, a detectar faltantes y a registrar la diferencia.",
    prior=["Sé qué es una discrepancia.", "Sé dividir y restar.", "Sé qué es EPP."],
    explain=[
        "En un caso de instalación de faenas se cruzan dos documentos: el plano, que dice qué debe haber, y la lista de materiales, que dice qué se pidió. Si las cantidades no coinciden, hay un faltante cuando se pidió menos de lo necesario, o un exceso cuando se pidió más. El módulo de cierro es una pieza prefabricada de largo fijo. El portón es la abertura por donde entra y sale la gente y la maquinaria.",
        "Una regla de ejemplo, como un baño cada seis personas, se usa para calcular cantidades; el valor real lo fija la norma vigente. Antes de comprar o de usar, las diferencias se registran con documentos, valores, fecha y quién las detectó, y se informan al supervisor. Nadie compensa un faltante con una improvisación, y menos con elementos de protección que no cumplen lo exigido.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("módulo de cierro", "pieza prefabricada de largo fijo que forma el cierre"), ("portón", "abertura por donde entran y salen personas y maquinaria"), ("faltante", "cantidad pedida menor que la necesaria"), ("exceso", "cantidad pedida mayor que la necesaria")],
    worked=[
        ("Módulos necesarios", "Un cierro de ejemplo de 30 m incluye un portón de 6 m y el resto va con módulos de 4 m. ¿Cuántos módulos se necesitan?", ["Al total se le resta el portón: 24 m.", "24 dividido en 4 son 6."], "6 módulos"),
        ("Faltante de EPP", "Una obra de ejemplo tiene 9 trabajadores y 7 pares de guantes. ¿Cuántos pares faltan?", ["Se resta lo disponible de lo necesario.", "9 menos 7 son 2."], "2 pares"),
    ],
    mistakes=[("Contar el portón como si fuera cierro cubierto con módulos.", "El portón tiene su propia pieza y no se cubre con módulos.", "Resta el largo del portón antes de dividir."),
              ("Tapar un faltante de cascos con gorros de tela.", "Un gorro no protege contra un golpe como el casco.", "Informa y espera el EPP correcto.")],
    T=[
        ("abc", "En Construcción: ¿qué es un módulo de cierro?", "Una pieza prefabricada de largo fijo que forma el cierre", "Una herramienta para medir el cierre", "El permiso de la obra", "El módulo es una pieza del cierro; no es una herramienta ni un permiso."),
        ("abc", "¿Qué es un faltante en una lista de materiales?", "Una cantidad pedida menor que la necesaria", "Una cantidad pedida mayor que la necesaria", "Un material de mejor calidad", "El faltante es pedir menos; pedir más es un exceso."),
        ("abc", "¿Qué es un portón en una faena?", "Una abertura por donde entran y salen personas y maquinaria", "Un módulo extra de cierro", "Un tipo de EPP", "El portón es la abertura; no es un módulo común ni un EPP."),
        ("=", "{F} ¿Cuántos metros del cierro se cubren con módulos?", "60-6", "Se resta el portón del largo total.", " m"),
        ("=", "{F} ¿Cuántos módulos de 3 m se necesitan?", "(60-6)//3", "Los metros a cubrir se dividen por el largo de cada módulo.", " módulos"),
        ("=", "{F} ¿Cuántos módulos de diferencia hay entre la lista y lo que pide el plano?", "20-(60-6)//3", "Se resta lo necesario de lo pedido.", " módulos"),
        ("abc", "{F} La lista pide 20 módulos y el plano necesita 18. ¿Qué es la diferencia?", "Un exceso de 2 módulos", "Un faltante de 2 módulos", "No hay diferencia", "Se pidieron 2 módulos más de los necesarios."),
        ("=", "{F} ¿Cuántos cascos faltan para las 12 personas?", "12-10", "Se resta lo disponible de lo necesario.", " cascos"),
        ("=", "{F} Con la regla de ejemplo, ¿cuántos baños corresponden para 12 personas?", "12//6", "Se divide el número de personas por el valor de la regla.", " baños"),
        ("ab", "{F} Un ayudante propone reemplazar los 2 cascos que faltan por gorros de tela. ¿Qué respuesta es correcta?", "No: se informa el faltante y se espera el casco correcto", "Sí: los gorros cubren la cabeza", "Un gorro no protege contra golpes como un casco."),
        ("abc", "{F} ¿Qué debe incluir el registro de la diferencia de módulos?", "Los documentos, los dos valores, quién la detectó y la fecha", "Solo la cantidad mayor", "El nombre del proveedor", "El registro deja constancia de qué, dónde, quién y cuándo."),
        ("=", "{F} Si el portón fuera de 9 m, ¿cuántos módulos de 3 m se necesitarían?", "(60-9)//3", "Se resta el nuevo portón y se divide por 3.", " módulos"),
        ("abc", "{F} ¿Se compra el exceso de módulos «por si acaso»?", "No: se informa y se espera la decisión", "Sí: siempre conviene tener extras", "Sí, si son baratos", "Una compra de más es un costo que debe aprobarse; se informa."),
    ],
    ctx=("abc", "El portón del cierro llega más angosto que lo indicado en el plano. ¿Qué corresponde?", "Registrar la diferencia y avisar al supervisor antes de instalarlo", "Instalarlo igual", "Ensancharlo en obra", "Un portón distinto al plano puede dificultar el acceso; decide el supervisor."),
    sc=[
        ("En Construcción: ¿qué es un exceso en una lista?", "Una cantidad pedida mayor que la necesaria", "Es pedir más de lo que pide el plano."),
        ("Un cierro de 20 m con módulos de 4 m necesita cuántos?", "5", "Se divide el largo por el largo del módulo."),
        ("¿Se compensa un EPP faltante con otra cosa?", "No, se informa y se espera el EPP correcto", "Un reemplazo improvisado no protege igual."),
    ],
    op=("Caso de ejemplo: cierro de 45 m con un portón de 6 m y módulos de 3 m; lista pide 12 módulos. En la obra hay 9 personas y 8 pares de lentes. Escribe (a) cuántos módulos necesita el plano, (b) si hay faltante o exceso y de cuántos, (c) cuántos lentes faltan, (d) qué haces.",
        "(a) 45 menos 6 son 39 m y 39 dividido en 3 son 13 módulos. (b) Faltante de 1 módulo. (c) Falta 1 par. (d) Registro ambas diferencias e informo al supervisor.",
        ["calcula los módulos", "clasifica la diferencia", "calcula los lentes", "informa"],
        ["hoja con las cuatro respuestas"],
        ["no restar el portón", "confundir faltante con exceso", "no informar"],
        "Pregunta: «¿qué restas antes de dividir?». Si no responde, pídele que relea el ejemplo del portón."),
    reinforce="Inventa un cierro con portón y calcula el número de módulos.",
    extend="Explica por qué un exceso de materiales también debe informarse.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 18 (cubicación de ejemplo, inventada). Cierro recto de 40 m de largo. Pies derechos cada 4 m, incluidos los dos extremos. Cada tablero de cierre cubre 2 m de largo. "
     "Merma de ejemplo: 10 % sobre los tableros calculados. Precios de ejemplo: pie derecho $5.000; tablero $9.000.")
build(
    O4, 4, F,
    use="Aprenderé a cubicar los pies derechos y tableros de un cierro y a calcular merma y costo con datos de ejemplo.",
    prior=["Sé dividir.", "Sé calcular un porcentaje simple de números redondos.", "Sé multiplicar cantidad por precio."],
    explain=[
        "Para cubicar un cierro recto se cuentan los tramos, que son los espacios entre pies derechos. El número de tramos es el largo dividido por la separación. Los pies derechos son siempre un elemento más que los tramos, porque hay uno en cada extremo. La merma es la parte del material que se pierde o se descarta; se calcula como un porcentaje y se suma a lo calculado. El costo se obtiene multiplicando la cantidad por el precio unitario.",
        "Antes de comprar, la cantidad con merma se anota en la planilla y se informa al supervisor. Los valores de separación, altura y merma son de ejemplo: los reales los fijan el proyecto y la norma vigente. Armar un cierro es trabajo de personal capacitado y autorizado, con protección. Aquí solo se calculan cantidades en papel.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("tramo", "espacio entre dos pies derechos consecutivos"), ("merma", "parte del material que se pierde o se descarta"), ("precio unitario", "precio de una unidad"), ("separación", "distancia entre dos pies derechos consecutivos")],
    worked=[
        ("Contar pies derechos", "Un cierro de ejemplo de 30 m con pies derechos cada 5 m, incluidos los extremos. ¿Cuántos pies derechos necesita?", ["Los tramos son 30 dividido en 5, es decir 6.", "Los pies derechos son 6 más 1, es decir 7."], "7 pies derechos"),
        ("Merma", "De 50 piezas de ejemplo se agrega una merma de 10 %. ¿Cuántas piezas se compran?", ["El 10 % de 50 son 5.", "50 más 5 son 55."], "55 piezas"),
    ],
    mistakes=[("Contar tantos pies derechos como tramos.", "Siempre hay un pie derecho más que tramos, por el extremo.", "Suma 1 al número de tramos."),
              ("Comprar la cantidad exacta sin merma.", "Parte del material se pierde y la obra puede quedar corta.", "Agrega la merma indicada en la planilla.")],
    T=[
        ("abc", "En Construcción: ¿qué es la merma de material?", "La parte que se pierde o se descarta", "El precio del material", "La cantidad que sobra del proyecto", "La merma es pérdida o descarte; no es precio ni sobrante del diseño."),
        ("abc", "En un cierro recto con pies derechos en ambos extremos, ¿cuántos pies derechos hay respecto de los tramos?", "Uno más que los tramos", "Uno menos que los tramos", "Los mismos que los tramos", "Hay un pie derecho en cada extremo, por eso uno más que los tramos."),
        ("abc", "En Construcción: ¿qué es un tramo de cierro?", "El espacio entre dos pies derechos consecutivos", "La suma de todos los pies derechos", "El precio de un tablero", "El tramo es el espacio entre dos pies derechos."),
        ("=", "{F} ¿Cuántos tramos tiene el cierro?", "40//4", "Se divide el largo por la separación.", " tramos"),
        ("=", "{F} ¿Cuántos pies derechos necesita el cierro?", "40//4+1", "Los tramos más uno por el extremo.", " pies derechos"),
        ("=", "{F} ¿Cuántos tableros se necesitan sin merma?", "40//2", "Se divide el largo por lo que cubre cada tablero.", " tableros"),
        ("=", "{F} ¿Cuántos tableros representa la merma de 10 %?", "20*10//100", "El 10 % de los tableros calculados.", " tableros"),
        ("=", "{F} ¿Cuántos tableros se compran con la merma incluida?", "20+20*10//100", "Se suman los tableros calculados y la merma.", " tableros"),
        ("=", "{F} ¿Cuánto cuestan los pies derechos?", "11*5000", "Cantidad por precio unitario.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan en total los pies derechos y los tableros con merma?", "11*5000+22*9000", "Se suman los dos costos.", " pesos"),
        ("ab", "{F} Un ayudante dice: «necesito 10 pies derechos porque hay 10 tramos». ¿Qué respuesta es correcta?", "No: son 11, uno más que los tramos", "Sí: uno por tramo", "Con extremos, siempre se cuenta un pie derecho más que los tramos."),
        ("abc", "{F} Se propone agregar 5 tableros más «por si acaso» sin avisar. ¿Qué corresponde?", "Informar y justificar el cambio en la planilla antes de comprar", "Comprarlos para tenerlos", "Quitar los tableros de merma", "Las compras extra se justifican y se informan; no se hacen a escondidas."),
        ("abc", "{F} Una persona sin autorización quiere armar el cierro un fin de semana. ¿Qué corresponde?", "No hacerlo: lo arma personal capacitado y autorizado según la norma vigente", "Hacerlo si el cliente se lo pide", "Hacerlo si usa guantes", "El permiso del cliente o los guantes no reemplazan capacitación ni autorización."),
    ],
    ctx=("abc", "Un proveedor de ejemplo rebaja el precio del tablero si se compra el doble. ¿Qué hace el encargado?", "Consultar al supervisor porque comprar más que la cantidad calculada cambia el presupuesto", "Comprar el doble porque es más barato", "Comprar la mitad", "Una compra mayor que la calculada cambia el presupuesto y debe aprobarse."),
    sc=[
        ("En Construcción: ¿cómo se calcula el número de tramos de un cierro?", "Dividiendo el largo por la separación", "Los tramos son los espacios entre pies derechos."),
        ("En un cierro de 20 m con pies derechos cada 5 m, ¿cuántos pies derechos hay?", "5", "Hay 4 tramos y un pie derecho más."),
        ("En construcción: ¿cuánto es el 10 % de 80?", "8", "Se divide 80 por 10 para obtener el diez por ciento."),
    ],
    op=("Cierro de ejemplo: 36 m de largo, pies derechos cada 6 m con ambos extremos, tableros que cubren 3 m cada uno, merma de 10 % sobre los tableros calculados (se redondea hacia arriba si no es entero). Precios de ejemplo: pie derecho $6.000, tablero $8.000. Escribe (a) cuántos pies derechos, (b) cuántos tableros sin merma, (c) cuántos con merma, (d) el costo total.",
        "(a) 36 dividido en 6 son 6 tramos y 7 pies derechos. (b) 36 dividido en 3 son 12 tableros. (c) El 10 % de 12 es 1,2, que se redondea a 2: 14 tableros. (d) 7 por $6.000 son $42.000 y 14 por $8.000 son $112.000; total $154.000.",
        ["cuenta los pies derechos", "calcula los tableros", "aplica la merma", "calcula el costo"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el pie derecho extra", "no redondear hacia arriba", "olvidar la merma"],
        "Pregunta: «¿cuántos tramos hay?». Si no responde, pídele que relea cómo se cuentan los pies derechos."),
    reinforce="Calcula pies derechos y tableros de dos cierros inventados de distinto largo.",
    extend="Explica por qué contar tramos y contar pies derechos no da el mismo número.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 19 (planilla de ejemplo, inventada). Obra «Posta Rural Radal». Planilla de cubicación con columnas partida, unidad, cantidad y precio unitario. "
     "P1 muro de bloques: m², 40, $12.000. P2 cierro: m, 25, $8.000. P3 radier: m³, 6, $90.000. P4 puertas: un, 5, $35.000. "
     "Riesgos anotados en la obra: acopios muy altos que pueden caer y golpes al descargar materiales.")
build(
    O5, 1, F,
    use="Aprenderé qué es cubicar, qué unidades se usan para longitud, superficie y volumen, y cómo se lee una planilla de cubicación.",
    prior=["Sé multiplicar y sumar.", "Sé qué es el área de un rectángulo.", "Sé leer una tabla."],
    explain=[
        "Cubicar es calcular las cantidades de elementos y materiales que necesita una obra. Se cubican longitudes en metros (m), superficies en metros cuadrados (m²), volúmenes en metros cúbicos (m³) y piezas en unidades (un). La cubicación puede hacerse a mano, con lápiz y calculadora, o de forma digital, en una planilla de cálculo o un programa que repite las fórmulas. Aquí todo se escribe en papel, y también la cubicación digital se revisa con una estimación rápida: un cálculo con números redondos que muestra si el resultado tiene sentido.",
        "Una partida es una parte de la obra con su unidad, su cantidad y su precio unitario. El total de una partida es la cantidad por el precio unitario. El radier es una losa de hormigón apoyada sobre el suelo; aquí solo se cubica. Cubicar de menos deja a la obra sin material y cubicar de más sube el costo y llena la obra de acopios. Los acopios son montones de material guardado y, si son muy altos, pueden caer.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("cubicar", "calcular las cantidades de elementos y materiales de una obra"), ("partida", "parte de la obra con unidad, cantidad y precio unitario"), ("m²", "metro cuadrado, unidad de superficie"), ("m³", "metro cúbico, unidad de volumen"), ("radier", "losa de hormigón apoyada sobre el suelo"), ("acopio", "montón de material guardado en la obra")],
    worked=[
        ("Elegir la unidad", "Una partida de ejemplo pide pintar un muro. ¿En qué unidad se cubica?", ["Pintar cubre una superficie.", "La superficie se mide en m²."], "m²"),
        ("Total de partida", "Una partida de ejemplo tiene 12 un y cada una cuesta $5.000. ¿Cuánto es su total?", ["Se multiplica la cantidad por el precio unitario.", "12 por 5.000 son 60.000."], "$60.000"),
    ],
    mistakes=[("Anotar una cantidad sin unidad.", "40 puede ser metros, m² o unidades y cambia el cálculo.", "Anota siempre cantidad y unidad."),
              ("Aceptar el resultado digital solo porque salió de una planilla.", "Una fórmula mal puesta repite el error en toda la planilla.", "Verifica con una estimación rápida.")],
    T=[
        ("abc", "En Construcción: ¿qué significa cubicar?", "Calcular las cantidades de elementos y materiales de una obra", "Cubrir la obra con una lona", "Dibujar un cubo en el plano", "Cubicar es calcular cantidades; cubrir o dibujar no tiene relación."),
        ("abc", "¿Qué unidad se usa para una superficie?", "Metro cuadrado (m²)", "Metro cúbico (m³)", "Metro (m)", "La superficie se mide en m²; m³ es volumen y m longitud."),
        ("abc", "¿Qué unidad se usa para el volumen de un material?", "Metro cúbico (m³)", "Metro cuadrado (m²)", "Unidad (un)", "El volumen se mide en m³; m² es superficie y un cuenta piezas."),
        ("=", "{F} ¿Cuánto es el total de la partida P1?", "40*12000", "Cantidad por precio unitario.", " pesos"),
        ("=", "{F} ¿Cuánto es el total de la partida P4?", "5*35000", "Cantidad por precio unitario.", " pesos"),
        ("abc", "{F} ¿Qué unidad usa la partida del radier?", "m³", "m²", "m", "El radier se cubica en volumen y su unidad en la ficha es m³."),
        ("=", "{F} ¿Cuánto suman los totales de las cuatro partidas?", "40*12000+25*8000+6*90000+5*35000", "Se suman los cuatro totales.", " pesos"),
        ("abc", "{F} ¿Qué partida de la ficha usa una unidad de longitud?", "El cierro (P2)", "El muro de bloques (P1)", "Las puertas (P4)", "El cierro está en metros; el muro en m² y las puertas en unidades."),
        ("abc", "{F} Un acopio de bloques está muy alto y se ve inestable. ¿Qué corresponde?", "Mantenerse lejos de la zona y avisar al supervisor", "Subir para ordenarlo", "Sacar un bloque de abajo para bajarlo", "Un acopio inestable puede caer; se mantiene la distancia y se avisa."),
        ("ab", "{F} Un ayudante anota 40 en P1 sin escribir la unidad. ¿Qué respuesta es correcta?", "Está incompleto: falta la unidad m²", "Está completo: se entiende", "Sin la unidad no se sabe si son metros, m² o unidades."),
        ("abc", "{F} Se cubicó el radier de menos. ¿Qué consecuencia es la más probable?", "Falta de material y compras de urgencia", "Material de sobra en todos los casos", "Ningún efecto", "Cubicar de menos deja a la obra corta de material y obliga a comprar apurado."),
        ("=", "{F} Si el precio de P2 subiera $1.000 por metro, ¿cuánto aumentaría el total de P2?", "25*1000", "Se multiplica el aumento por los metros.", " pesos"),
        ("abc", "{F} Alguien propone cambiar la unidad del radier de m³ a m² «para que sea más fácil». ¿Qué corresponde?", "Rechazarlo: la unidad es parte del dato y cambia el cálculo", "Aceptarlo si se mantiene la cantidad", "Aceptarlo si se avisa por mensaje", "Cambiar la unidad cambia el significado de la cantidad."),
    ],
    ctx=("abc", "Una planilla digital de ejemplo da un total 10 veces mayor que el cálculo a mano. ¿Qué corresponde?", "Revisar las fórmulas y las unidades antes de usar el resultado", "Confiar porque es digital", "Dividir por 10 sin averiguar", "Una diferencia grande indica un error de fórmula o de unidad que se revisa."),
    sc=[
        ("En Construcción: ¿qué es una partida?", "Una parte de la obra con unidad, cantidad y precio unitario", "La partida reúne los datos que permiten calcular su costo."),
        ("Una partida de 8 un a $2.000 cada una, ¿cuánto es?", "$16.000", "Se multiplica la cantidad por el precio unitario."),
        ("¿Qué unidad se usa para el volumen?", "m³", "El volumen se mide en metros cúbicos."),
    ],
    op=("Planilla de ejemplo «Kiosco Litre»: A1 cierro, m, 18, $7.000; A2 revestimiento de muro, m², 30, $11.000; A3 radier, m³, 4, $85.000. Escribe (a) la unidad de cada partida en palabras, (b) el total de cada una, (c) el total de las tres, (d) qué haces si el cálculo digital da un total diez veces mayor.",
        "(a) A1 longitud en metros; A2 superficie en metros cuadrados; A3 volumen en metros cúbicos. (b) 126.000; 330.000; 340.000. (c) 796.000. (d) Reviso fórmulas y unidades con una estimación rápida e informo.",
        ["asocia unidad y magnitud", "calcula cada total", "suma los totales", "revisa el resultado digital"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la unidad", "multiplicar mal", "confiar en el resultado digital"],
        "Pregunta: «¿qué haces con un total muy distinto?». Si no responde, pídele que relea la estimación rápida."),
    reinforce="Haz una tabla con tres partidas inventadas, su unidad, cantidad, precio y total.",
    extend="Explica por qué una cubicación digital también necesita una revisión a mano.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 20 (obra de ejemplo, inventada). Muro de 8 m de largo por 3 m de alto, con una puerta de 1 m por 2 m y una ventana de 2 m por 1 m. "
     "Piso de 5 m por 4 m y 10 cm de espesor. Consumo de ejemplo: 12 bloques por m² de muro.")
build(
    O5, 2, F,
    use="Aprenderé las fórmulas básicas para cubicar longitud, superficie y volumen, y a descontar vanos y aplicar consumos.",
    prior=["Sé calcular el área de un rectángulo.", "Sé multiplicar.", "Sé pasar de centímetros a metros."],
    explain=[
        "El perímetro de un rectángulo es la suma de sus cuatro lados: dos veces el largo más dos veces el ancho. La superficie de un rectángulo es largo por ancho y se expresa en m². El volumen de una pieza de forma de caja es largo por ancho por alto, en m³; si el espesor viene en centímetros, se divide por 100 para pasarlo a metros. Un vano es una abertura en un muro, como una puerta o una ventana.",
        "La superficie bruta de un muro es su largo por su alto. La superficie neta es la bruta menos la superficie de los vanos. Para calcular un material que se coloca solo donde hay muro, se usa la superficie neta, salvo que el documento indique otra cosa. El consumo es la cantidad de material por unidad de superficie, como 12 bloques por m²; en este cuaderno son valores de ejemplo y los reales los fija el proyecto o el fabricante.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("perímetro", "suma de los lados de una figura"), ("vano", "abertura en un muro, como una puerta o ventana"), ("superficie bruta", "largo por alto del muro, sin descontar vanos"), ("superficie neta", "superficie bruta menos los vanos"), ("consumo", "cantidad de material por unidad de superficie")],
    worked=[
        ("Superficie neta", "Un muro de ejemplo de 5 m por 2 m tiene una ventana de 1 m por 1 m. ¿Cuánto mide su superficie neta?", ["La superficie bruta es 10 m².", "Se resta la ventana: 10 menos 1 son 9."], "9 m²"),
        ("Volumen de una losa", "Una losa de ejemplo de 3 m por 5 m y 20 cm de espesor, ¿cuántos m³ tiene?", ["La superficie es 15 m².", "15 por 20 son 300; dividido en 100 son 3."], "3 m³"),
    ],
    mistakes=[("Calcular el material con la superficie bruta sin descontar vanos.", "Se pediría material de más.", "Usa la superficie neta cuando el documento no indique otra cosa."),
              ("Multiplicar por el espesor en centímetros sin pasar a metros.", "El volumen sale 100 veces mayor.", "Divide el espesor en cm por 100.")],
    T=[
        ("abc", "En Construcción: ¿qué es un vano?", "Una abertura en un muro, como una puerta o ventana", "Un muro sin terminar", "Una unidad de medida", "El vano es una abertura; no es un muro ni una unidad."),
        ("abc", "En Construcción: ¿qué es la superficie neta de un muro?", "La bruta menos los vanos", "La bruta más los vanos", "Solo la suma de los vanos", "La neta descuenta las aberturas de la bruta."),
        ("abc", "En Construcción: ¿qué es el consumo de un material?", "La cantidad de material por unidad de superficie", "El precio del material", "El plazo de entrega", "El consumo relaciona cantidad de material con superficie."),
        ("=", "{F} ¿Cuál es la superficie bruta del muro?", "8*3", "Largo por alto.", " m²"),
        ("=", "{F} ¿Cuántos m² suman la puerta y la ventana?", "1*2+2*1", "Se calcula el área de cada vano y se suman.", " m²"),
        ("=", "{F} ¿Cuál es la superficie neta del muro?", "8*3-(1*2+2*1)", "A la superficie bruta se le restan los vanos.", " m²"),
        ("=", "{F} ¿Cuántos bloques se necesitan para la superficie neta?", "20*12", "Superficie neta por consumo.", " bloques"),
        ("=", "{F} ¿Cuántos m³ tiene el piso?", "5*4*10//100", "Superficie por espesor, pasando el espesor de cm a m.", " m³"),
        ("abc", "{F} ¿Por qué se divide el espesor de 10 cm por 100?", "Para pasarlo a metros", "Para pasarlo a unidades", "Para descontar los vanos", "Hay 100 cm en 1 m, por eso se pasa de cm a m."),
        ("ab", "{F} Un ayudante calcula los bloques con la superficie bruta. ¿Qué respuesta es correcta?", "No: se usa la neta, que descuenta los vanos", "Sí: siempre se usa la bruta", "Los vanos no llevan bloques y deben descontarse."),
        ("abc", "{F} ¿Qué unidad tiene el resultado de multiplicar largo por alto del muro?", "m²", "m³", "m", "Largo por alto da una superficie en metros cuadrados."),
        ("=", "{F} ¿Cuántos metros mide el perímetro del piso?", "2*(5+4)", "El doble de la suma de los lados.", " m"),
        ("abc", "{F} El plano dice que la puerta mide 90 cm por 210 cm y la ficha dice 1 m por 2 m. ¿Qué se hace?", "Anotar la diferencia e informar al proyectista o al supervisor", "Elegir la medida más grande", "Promediar las dos", "No se elige entre documentos: se informa para que decida quien diseña."),
    ],
    ctx=("abc", "Un proveedor de ejemplo pide la cantidad de bloques y el ayudante le dice la calculada con la superficie bruta. ¿Qué es lo más prudente?", "Corregir con la superficie neta antes de comprar", "Comprar igual para tener sobrante", "Pedir el doble", "Comprar sin descontar vanos genera material de más y costo innecesario."),
    sc=[
        ("En Construcción: ¿qué es la superficie bruta de un muro?", "Largo por alto, sin descontar vanos", "La neta se obtiene restando vanos."),
        ("Un muro de 4 m por 3 m, ¿cuántos m² tiene?", "12 m²", "Se multiplica el largo por el alto del muro."),
        ("¿Cuánto es el 5 % de 200?", "10", "Se divide 200 por 20 para obtener el cinco por ciento."),
    ],
    op=("Muro de ejemplo de 6 m por 3 m con una puerta de 1 m por 2 m y una ventana de 1 m por 1 m; consumo de ejemplo 10 piezas por m²; piso de 4 m por 5 m y 10 cm de espesor. Escribe (a) la superficie bruta, (b) la neta, (c) las piezas necesarias, (d) el volumen del piso en m³.",
        "(a) 18 m². (b) 18 menos 3 son 15 m². (c) 15 por 10 son 150 piezas. (d) 20 m² por 10 cm son 200; dividido en 100 son 2 m³.",
        ["calcula la bruta", "descuenta los vanos", "aplica el consumo", "pasa el espesor a metros"],
        ["hoja con las cuatro respuestas"],
        ["olvidar descontar", "no pasar de cm a m", "sumar en vez de multiplicar"],
        "Pregunta: «¿qué restas de la bruta?». Si no responde, pídele que relea qué es un vano."),
    reinforce="Calcula la superficie neta de un muro inventado con dos vanos.",
    extend="Explica por qué el espesor se pasa a metros antes de calcular el volumen.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 21 (caso de ejemplo, inventado). Sala de 6 m por 4 m y 3 m de alto, con una puerta de 2 m² y sin otras aberturas. Cubicación manual de los muros: 58 m². "
     "La planilla digital dice 580 m². Un revestimiento de ejemplo viene en cajas que cubren 10 m² cada una. Precio de ejemplo: $20.000 la caja.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso con dos cubicaciones que no coinciden y a decidir cuál se revisa y qué se informa.",
    prior=["Sé qué es superficie bruta y neta.", "Sé dividir.", "Sé qué es una estimación rápida."],
    explain=[
        "Cuando una cubicación manual y una digital no coinciden, se compara la razón entre los dos resultados. Si una es exactamente 10 veces la otra, el error suele estar en una coma, un cero o una unidad. La estimación rápida ayuda: la sala tiene un perímetro de 20 m y una altura de 3 m; eso da cerca de 60 m², por lo que 580 m² no tiene sentido. Una caja de material cubre una cantidad fija, y las cajas se redondean hacia arriba, porque no se compra media caja.",
        "El costo de un error de cubicación se mide en dinero y en tiempo. Quien detecta la diferencia la registra con ambos valores, la posible causa, la fecha y quién la vio, y la informa al supervisor. Nadie corrige la planilla de otro sin avisar. Todos los datos son de ejemplo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("razón", "cuántas veces cabe un valor en otro"), ("redondear hacia arriba", "subir al siguiente número entero cuando hay resto"), ("caja", "unidad de venta que cubre una cantidad fija de superficie"), ("estimación rápida", "cálculo con números redondos para ver si un resultado tiene sentido")],
    worked=[
        ("Detectar un factor", "Un cálculo manual de ejemplo da 35 m² y la planilla da 350 m². ¿Cuántas veces mayor es?", ["Se divide 350 por 35.", "El resultado es 10."], "10 veces"),
        ("Cajas necesarias", "Hacen falta 23 m² y cada caja cubre 5 m². ¿Cuántas cajas se compran?", ["23 dividido en 5 es 4 y sobran 3 m².", "Se redondea hacia arriba: 5 cajas."], "5 cajas"),
    ],
    mistakes=[("Confiar en un resultado digital sin compararlo con una estimación.", "Un error de coma pasa inadvertido.", "Haz una estimación rápida con números redondos."),
              ("Comprar cajas «por la mitad» para no sobrar.", "No se venden medias cajas y el material puede faltar.", "Redondea hacia arriba.")],
    T=[
        ("abc", "En Construcción: ¿qué es una estimación rápida?", "Un cálculo con números redondos para ver si un resultado tiene sentido", "Un cálculo exacto de todas las partidas", "Un cálculo que hace solo el programa", "La estimación rápida es una comprobación aproximada; no es el cálculo exacto ni automático."),
        ("abc", "Un resultado digital es exactamente 10 veces el manual. ¿Cuál es la causa más probable?", "Un error de coma, un cero o una unidad", "Una puerta que se agregó", "Un material más caro", "Un factor 10 exacto suele venir de una coma, un cero o una unidad."),
        ("abc", "¿Cómo se redondea el número de cajas cuando sobra superficie por cubrir?", "Hacia arriba", "Hacia abajo", "Se compra media caja", "No se vende media caja y redondear hacia abajo deja superficie sin cubrir."),
        ("=", "{F} ¿Cuántos m² de muro da la cubicación manual, calculando perímetro por alto menos la puerta?", "(6+4)*2*3-2", "El perímetro por el alto, menos la puerta.", " m²"),
        ("abc", "{F} La planilla da 580 m² y la cubicación manual da 58 m². ¿Qué sugiere?", "Un factor 10: un error de coma o de cero", "Que la sala se agrandó", "Que la caja cubre más", "580 es exactamente 10 veces 58."),
        ("=", "{F} ¿Cuántas veces mayor es el valor digital que el manual?", "580//58", "Se divide el valor digital por el manual.", " veces"),
        ("=", "{F} ¿Cuántas cajas se necesitan con 58 m²?", "(58+9)//10", "Se divide 58 por 10 y se redondea hacia arriba.", " cajas"),
        ("=", "{F} ¿Cuántas cajas saldrían con 580 m²?", "(580+9)//10", "Se divide 580 por 10 y se redondea hacia arriba.", " cajas"),
        ("=", "{F} ¿Cuántos pesos cuesta de más la compra con la cifra digital respecto de la manual?", "(58-6)*20000", "Las cajas de más por el precio de cada caja.", " pesos"),
        ("abc", "{F} ¿Qué corresponde hacer ante la diferencia?", "Revisar fórmulas y unidades, registrar la diferencia e informar al supervisor", "Usar la cifra mayor para no quedar corto", "Borrar la planilla digital sin avisar", "Se revisa la causa y se informa; no se elige una cifra sin verificar."),
        ("ab", "{F} Un estudiante dice: «confío en la planilla porque es automática». ¿Qué respuesta es correcta?", "No: una fórmula mal puesta repite el error y debe revisarse", "Sí: los programas no se equivocan", "El error de una fórmula se repite automáticamente en toda la planilla."),
        ("=", "{F} ¿Cuántos m² de muro serían sin descontar la puerta?", "(6+4)*2*3", "Perímetro por alto, sin restar la puerta.", " m²"),
        ("abc", "{F} ¿Qué debe incluir el registro de la diferencia?", "Los dos valores, la causa probable, quién la vio y la fecha", "Solo la cifra digital", "El nombre del proveedor de cajas", "Un registro útil dice qué, por qué, quién y cuándo."),
    ],
    ctx=("abc", "El supervisor de ejemplo pide la orden de compra de cajas y solo tiene la planilla digital con 580 m². ¿Qué hace el encargado?", "Pide revisar el resultado antes de comprar y entrega el cálculo manual", "Compra 58 cajas", "Compra la mitad", "Comprar con un valor sospechoso genera gastos innecesarios."),
    sc=[
        ("En Construcción: ¿qué indica un resultado exactamente 10 veces mayor?", "Un error de coma, cero o unidad", "Un factor 10 exacto apunta a una coma, un cero o una unidad."),
        ("Con 31 m² y cajas de 10 m², ¿cuántas cajas?", "4", "Se redondea hacia arriba porque sobra superficie."),
        ("¿Quién decide cuál cifra se usa?", "El supervisor, tras la revisión", "No decide quien detecta la diferencia."),
    ],
    op=("Caso de ejemplo: sala de 5 m por 4 m y 3 m de alto sin aberturas. La cubicación manual da 54 m² de muro y la planilla da 540 m². Cajas de 6 m² a $15.000. Escribe (a) cuántas veces mayor es la cifra digital, (b) cuántas cajas con la cifra manual, (c) el costo con esa cifra, (d) qué haces con la planilla.",
        "(a) 540 dividido en 54 son 10 veces. (b) 54 dividido en 6 son 9 cajas. (c) 9 por $15.000 son $135.000. (d) Reviso las fórmulas y unidades, registro la diferencia e informo al supervisor.",
        ["calcula la razón", "calcula las cajas", "calcula el costo", "informa la diferencia"],
        ["hoja con las cuatro respuestas"],
        ["usar la cifra mayor", "no redondear", "corregir sin avisar"],
        "Pregunta: «¿por qué sospechas de la planilla?». Si no responde, pídele que relea la estimación rápida."),
    reinforce="Inventa dos cubicaciones que difieren en un factor 10 y escribe qué revisarías.",
    extend="Explica por qué una diferencia de factor exacto 10 orienta la búsqueda del error.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 22 (cubicación de ejemplo, inventada). Piso de 7 m por 5 m. Piezas de 50 cm por 50 cm, es decir, 4 piezas por m². Merma de ejemplo: 10 % sobre las piezas calculadas. "
     "Las piezas se venden en cajas de 10 piezas. Precio de ejemplo: $18.000 la caja.")
build(
    O5, 4, F,
    use="Aprenderé a cubicar piezas con merma, a convertirlas en cajas y a calcular el costo con datos de ejemplo.",
    prior=["Sé calcular áreas y porcentajes simples.", "Sé redondear hacia arriba.", "Sé calcular costos."],
    explain=[
        "Para cubicar piezas pequeñas se calcula la superficie y se multiplica por las piezas que caben en cada m². A esa cantidad se le suma la merma, que es un porcentaje de piezas que se pierden o se descartan. Con las piezas totales se calculan las cajas dividiendo por las piezas de cada caja y redondeando hacia arriba. El costo es el número de cajas por el precio de una caja. Las piezas sobrantes se anotan: son un excedente.",
        "Todos los valores de este cuaderno son de ejemplo. Los consumos, las mermas y los tamaños reales los fijan el proyecto y el fabricante. Una persona que cubica no decide cambiar un producto, y menos instalarlo: eso es trabajo de personal autorizado. Cualquier cambio de pieza se informa y lo aprueba quien diseña.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("pieza", "elemento individual que se coloca, como un trozo de revestimiento"), ("merma", "porcentaje de material que se pierde o descarta"), ("excedente", "material que sobra después de comprar"), ("caja", "unidad de venta con un número fijo de piezas")],
    worked=[
        ("Piezas de una superficie", "Una superficie de ejemplo de 4 m por 3 m con 4 piezas por m². ¿Cuántas piezas son?", ["La superficie es 12 m².", "12 por 4 son 48."], "48 piezas"),
        ("Cajas de 12", "Se necesitan 50 piezas y cada caja trae 12. ¿Cuántas cajas se compran?", ["50 dividido en 12 es 4 y sobran 2.", "Se redondea hacia arriba: 5 cajas."], "5 cajas"),
    ],
    mistakes=[("Olvidar sumar la merma.", "Las piezas pueden faltar al final.", "Suma la merma antes de calcular las cajas."),
              ("Redondear las cajas hacia abajo.", "Se compra menos material del necesario.", "Redondea siempre hacia arriba.")],
    T=[
        ("abc", "En Construcción: ¿qué es un excedente de material?", "El material que sobra después de comprar", "El material que falta", "El precio de una caja", "El excedente es sobrante; faltante es lo contrario."),
        ("abc", "¿Por qué las cajas se redondean hacia arriba?", "Porque no se vende media caja y hacia abajo faltaría material", "Porque es más barato", "Porque el proveedor lo exige siempre", "No se compra media caja y redondear hacia abajo deja piezas sin cubrir."),
        ("abc", "¿Qué es una pieza en esta cubicación?", "Un elemento individual que se coloca", "Un plano de la obra", "El perímetro del piso", "La pieza es el elemento individual que se cuenta."),
        ("=", "{F} ¿Cuántos m² tiene el piso?", "7*5", "Largo por ancho.", " m²"),
        ("=", "{F} ¿Cuántas piezas se necesitan sin merma?", "7*5*4", "La superficie por las piezas de cada m².", " piezas"),
        ("=", "{F} ¿Cuántas piezas son la merma de 10 %?", "140*10//100", "El 10 % de las piezas calculadas.", " piezas"),
        ("=", "{F} ¿Cuántas piezas hay que comprar contando la merma?", "140+140*10//100", "Se suman las piezas y la merma.", " piezas"),
        ("=", "{F} ¿Cuántas cajas se compran?", "(154+9)//10", "Se divide 154 por 10 y se redondea hacia arriba.", " cajas"),
        ("=", "{F} ¿Cuánto cuestan las cajas?", "16*18000", "Número de cajas por precio de cada caja.", " pesos"),
        ("=", "{F} ¿Cuántas piezas sobran después de comprar las cajas?", "16*10-154", "Las piezas de las cajas menos las necesarias.", " piezas"),
        ("=", "{F} Si se compraran solo 15 cajas, ¿cuántas piezas faltarían respecto de las necesarias?", "154-15*10", "Las necesarias menos las que traen las 15 cajas.", " piezas"),
        ("ab", "{F} Un ayudante dice: «con 150 piezas basta, la merma no importa». ¿Qué respuesta es correcta?", "No: se necesitan 154 contando la merma", "Sí: la merma nunca se usa", "Sin merma pueden faltar piezas al final."),
        ("abc", "{F} Un proveedor ofrece una pieza distinta de tamaño. ¿Qué corresponde?", "Informar y esperar la aprobación del proyectista antes de cambiarla", "Aceptarla si es más barata", "Aceptarla si se ve igual", "Cambiar el producto altera el diseño; decide quien diseña."),
    ],
    ctx=("abc", "Al recibir las cajas, una trae menos piezas de las indicadas. ¿Qué corresponde?", "Registrar la diferencia y avisar al supervisor", "Usarla sin avisar", "Quedarse con las piezas sobrantes de otra caja", "Una caja incompleta es una diferencia de recepción que se informa."),
    sc=[
        ("En Construcción: ¿qué es la merma?", "El porcentaje de material que se pierde o descarta", "Se suma a lo calculado antes de comprar."),
        ("Con 45 piezas y cajas de 10, ¿cuántas cajas?", "5", "Se redondea hacia arriba porque sobran piezas."),
        ("¿Cuánto es el 10 % de 120?", "12", "Se divide 120 por 10 para obtener el diez por ciento."),
    ],
    op=("Piso de ejemplo de 6 m por 4 m; 4 piezas por m²; merma de ejemplo 10 %; cajas de 12 piezas; caja $20.000. Escribe (a) cuántas piezas sin merma, (b) cuántas con merma (se redondea hacia arriba si no es entero), (c) cuántas cajas, (d) el costo y qué haces si el proveedor cambia el producto.",
        "(a) 24 por 4 son 96 piezas. (b) El 10 % de 96 es 9,6, que sube a 10: 106 piezas. (c) 106 dividido en 12 son 8 y sobran 10, es decir, 9 cajas. (d) 9 por $20.000 son $180.000; informo y espero la aprobación del proyectista.",
        ["calcula piezas", "aplica la merma", "calcula cajas", "calcula costo y consulta"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la merma", "redondear hacia abajo", "aceptar el cambio por su cuenta"],
        "Pregunta: «¿qué haces con el resto de la división?». Si no responde, pídele que relea el redondeo."),
    reinforce="Cubica las piezas de un piso inventado y calcula las cajas.",
    extend="Explica por qué algunas obras guardan unas piezas extra para futuras reparaciones.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 23 (obra de ejemplo, inventada). Obra «Bodega Maitén». Inventario de equipos: una sierra circular eléctrica, un taladro eléctrico y una hormigonera. "
     "Horas de uso en el mes (4 semanas): sierra 40 horas; taladro 24 horas; hormigonera 60 horas. Documentos: manual del fabricante, hoja de vida del equipo y pauta de revisión diaria. "
     "Riesgos anotados: corte, atrapamiento, golpe, descarga eléctrica y ruido.")
build(
    O6, 1, F,
    use="Aprenderé la diferencia entre equipo, herramienta y maquinaria, qué dice el manual del fabricante y qué riesgos tiene usar y mantener equipos.",
    prior=["Sé qué es un riesgo y un EPP.", "Sé sumar y dividir.", "Sé leer una tabla."],
    explain=[
        "Una herramienta es un objeto que se usa con las manos para hacer una tarea, como un taladro. Un equipo es un conjunto de piezas que cumple una función en la obra. La maquinaria son equipos más grandes con motor, como una hormigonera, que es una máquina que mezcla hormigón. El manual del fabricante dice para qué sirve el equipo, sus límites, sus advertencias de seguridad y cada cuánto debe mantenerse. Cada equipo tiene una hoja de vida, que registra su historia, y una pauta de revisión, que es una lista de puntos a marcar antes de usarlo.",
        "El mantenimiento es el cuidado que mantiene un equipo en buen estado. El mantenimiento preventivo se hace antes de que falle, según un plan; el correctivo se hace después de una falla. El llamado mantenimiento básico lo realizan personas capacitadas y autorizadas, siguiendo el manual y la norma vigente. Este cuaderno no enseña cómo se usa, se revisa ni se repara un equipo. Un equipo dañado se retira de servicio y se avisa.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("herramienta", "objeto que se usa con las manos para hacer una tarea"), ("maquinaria", "equipos grandes con motor"), ("manual del fabricante", "documento que dice usos, límites, advertencias y mantenimiento de un equipo"), ("hoja de vida", "registro de la historia de un equipo"), ("mantenimiento preventivo", "el que se hace antes de que el equipo falle"), ("mantenimiento correctivo", "el que se hace después de una falla")],
    worked=[
        ("Tipo de mantenimiento", "Una máquina de ejemplo se detiene por una falla y luego se repara. ¿Qué tipo de mantenimiento es?", ["Se actúa después de que falló.", "Eso es mantenimiento correctivo."], "Correctivo"),
        ("Horas de uso", "Un equipo de ejemplo se usa 15 horas por semana durante 4 semanas. ¿Cuántas horas suma?", ["Se multiplican las horas por las semanas.", "15 por 4 son 60."], "60 horas"),
    ],
    mistakes=[("Pensar que el manual del fabricante es opcional.", "Contiene advertencias de seguridad y límites de uso.", "Se consulta siempre y quien usa el equipo lo conoce."),
              ("Seguir usando un equipo con una falla visible.", "El riesgo aumenta con cada uso.", "Retíralo de servicio y avisa al responsable.")],
    T=[
        ("abc", "En Construcción: ¿qué dice el manual del fabricante de un equipo?", "Usos, límites, advertencias de seguridad y mantenimiento", "El precio de venta de la obra", "El nombre del cliente", "El manual describe el equipo y su cuidado; no trata de precios de obra ni de clientes."),
        ("abc", "¿Qué es el mantenimiento preventivo?", "El que se hace antes de que el equipo falle, según un plan", "El que se hace después de una falla", "El que solo hace el cliente", "El preventivo se anticipa a la falla; el correctivo la repara."),
        ("abc", "¿Qué es el mantenimiento correctivo?", "El que se hace después de una falla", "El que se hace según un plan antes de fallar", "El que reemplaza al manual", "El correctivo corrige una falla ya ocurrida."),
        ("=", "{F} ¿Cuántas horas suman en el mes los tres equipos?", "40+24+60", "Se suman las horas de uso de cada equipo.", " horas"),
        ("abc", "{F} ¿Qué documento registra la historia de un equipo?", "La hoja de vida", "La pauta de revisión diaria", "El manual del fabricante", "La hoja de vida guarda su historia; la pauta se marca cada día y el manual es del fabricante."),
        ("abc", "{F} ¿Qué riesgo se asocia a partes móviles que pueden agarrar la ropa o una mano?", "Atrapamiento", "Ruido", "Descarga eléctrica", "Las partes móviles que agarran producen atrapamiento; ruido y descarga son otros riesgos."),
        ("=", "{F} ¿Cuántas horas por semana usó la sierra en promedio?", "40//4", "Se divide las horas del mes por las semanas.", " horas"),
        ("abc", "{F} El taladro tiene el cable pelado. ¿Qué corresponde?", "No usarlo, retirarlo de servicio y avisar", "Usarlo con guantes", "Cubrir el cable con cinta y seguir", "Un cable pelado es riesgo de descarga eléctrica; se retira y se avisa."),
        ("abc", "{F} Alguien quiere limpiar la hormigonera mientras funciona. ¿Qué corresponde?", "No hacerlo: el mantenimiento lo hace personal autorizado según el manual", "Hacerlo con cuidado", "Hacerlo con guantes gruesos", "Un equipo en funcionamiento puede atrapar; el mantenimiento es de personal autorizado."),
        ("ab", "{F} Un ayudante dice: «el manual es opcional, ya sé usar la sierra». ¿Qué respuesta es correcta?", "No: el manual contiene advertencias y límites de uso", "Sí: la experiencia lo reemplaza", "El manual del fabricante no se reemplaza con experiencia."),
        ("abc", "En una obra de ejemplo un trabajador recibe una descarga eléctrica de un equipo y sigue en contacto. ¿Qué se hace según las reglas generales?", "No acercarse ni tocarlo, avisar a un adulto responsable y a emergencias", "Tirarlo del brazo para separarlo", "Esperar a que se suelte solo", "Tocarlo puede transmitir la descarga; se mantiene la distancia y se avisa de inmediato."),
        ("=", "{F} La pauta de revisión diaria se marca 5 días a la semana durante 4 semanas. ¿Cuántas revisiones son?", "5*4", "Días por semanas.", " revisiones"),
        ("abc", "{F} ¿Quién usa la sierra circular de la obra?", "Personal capacitado y autorizado", "Cualquier persona que la necesite", "Quien llegue primero", "Un equipo con riesgo de corte exige capacitación y autorización."),
    ],
    ctx=("abc", "Un estudiante en práctica ve una hormigonera con una protección suelta y el equipo está encendido. ¿Qué hace?", "Se aleja, avisa al responsable y no se acerca hasta que lo detengan y revisen", "Intenta apretar la protección", "Apaga el equipo por la fuerza", "Acercarse a un equipo en funcionamiento con una falla expone a un accidente."),
    sc=[
        ("En Construcción: ¿qué es una hoja de vida de un equipo?", "El registro de su historia", "La hoja de vida guarda sus revisiones y mantenciones."),
        ("¿Qué mantenimiento se hace tras una falla?", "El correctivo", "Corrige una falla que ya ocurrió."),
        ("¿Quién realiza el mantenimiento de un equipo?", "Personal capacitado y autorizado", "Este cuaderno no habilita para intervenir equipos."),
    ],
    op=("Obra de ejemplo «Taller Roble»: sierra (30 horas en el mes), taladro (18 horas) y hormigonera (45 horas). Riesgos: corte, atrapamiento y ruido. Escribe (a) las horas totales, (b) qué documento dice cada cuánto se mantiene un equipo, (c) qué tipo de mantenimiento es el que se hace antes de que falle, (d) qué haces si un equipo tiene una falla visible.",
        "(a) 30+18+45 son 93 horas. (b) El manual del fabricante. (c) Preventivo. (d) No lo uso, lo retiro de servicio y aviso al responsable.",
        ["suma las horas", "nombra el documento", "diferencia los mantenimientos", "retira el equipo dañado"],
        ["hoja con las cuatro respuestas"],
        ["confundir preventivo y correctivo", "usar el equipo dañado", "olvidar un equipo"],
        "Pregunta: «¿cuál se hace antes?». Si no responde, pídele que relea los dos tipos de mantenimiento."),
    reinforce="Escribe una frase de cada término del vocabulario con un ejemplo inventado.",
    extend="Explica por qué un equipo con una falla pequeña se retira igual de servicio.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 24 (hoja de vida de ejemplo, inventada). Equipo: hormigonera H-1. Horas acumuladas: 230. Mantenimiento preventivo según el manual de ejemplo: cada 100 horas. "
     "Último mantenimiento realizado a las 200 horas. Pauta de revisión diaria de 6 puntos.")
build(
    O6, 2, F,
    use="Aprenderé a leer una hoja de vida, a calcular cuándo toca el mantenimiento y a registrar lo que corresponde.",
    prior=["Sé qué es el mantenimiento preventivo.", "Sé sumar y restar.", "Sé leer registros."],
    explain=[
        "La hoja de vida de un equipo anota las horas acumuladas de uso, los mantenimientos hechos y las fallas. El intervalo de mantenimiento es el número de horas de uso que el manual fija entre un mantenimiento y el siguiente. La próxima hora de mantenimiento es la hora del último mantenimiento más el intervalo. Para saber cuánto falta, se resta a esa hora las horas acumuladas. Si las horas acumuladas pasan la próxima hora, el mantenimiento está vencido.",
        "La pauta de revisión diaria es una lista de puntos que se marca antes de usar el equipo. Si un punto no está marcado, la revisión está incompleta. Después de un mantenimiento se registra la fecha, las horas acumuladas, qué se hizo y quién lo hizo. El mantenimiento lo realiza personal autorizado según el manual; este cuaderno solo enseña a leer los registros.",
        f"Los valores son de ejemplo; los reales los fija el manual del fabricante. {EMER} {AVISO}",
    ],
    vocab=[("horas acumuladas", "total de horas de uso de un equipo"), ("intervalo de mantenimiento", "horas de uso entre un mantenimiento y el siguiente"), ("próxima hora de mantenimiento", "hora del último mantenimiento más el intervalo"), ("vencido", "pasado de la hora de mantenimiento"), ("pauta de revisión", "lista de puntos que se marca antes de usar el equipo")],
    worked=[
        ("Próximo mantenimiento", "Un equipo de ejemplo tuvo su último mantenimiento a las 150 horas y el intervalo es de 80 horas. ¿A qué hora toca el próximo?", ["Se suma el intervalo a la hora del último.", "150 más 80 son 230."], "A las 230 horas"),
        ("Horas que faltan", "El equipo de ejemplo tiene 205 horas acumuladas y el próximo mantenimiento es a las 230. ¿Cuántas horas faltan?", ["Se resta lo acumulado de lo que se espera.", "230 menos 205 son 25."], "25 horas"),
    ],
    mistakes=[("Contar el intervalo desde cero y no desde el último mantenimiento.", "Se calcula mal la hora del próximo.", "Suma el intervalo a la hora del último."),
              ("Postergar el mantenimiento porque «el equipo funciona bien».", "Las fallas pueden aparecer sin aviso.", "Respeta el plan del manual.")],
    T=[
        ("abc", "En Construcción: ¿qué es el intervalo de mantenimiento?", "Las horas de uso entre un mantenimiento y el siguiente", "El tiempo que dura el mantenimiento", "El precio del mantenimiento", "El intervalo mide horas de uso entre mantenimientos; no la duración ni el costo."),
        ("abc", "¿Qué anota la hoja de vida de un equipo?", "Horas acumuladas, mantenimientos hechos y fallas", "Los planos de la obra", "Los nombres de los clientes", "La hoja de vida registra la historia del equipo, no planos ni clientes."),
        ("abc", "¿Qué es una pauta de revisión diaria?", "Una lista de puntos que se marca antes de usar el equipo", "Un plan de compras de la obra", "Un informe de ventas", "La pauta es una lista de verificación previa al uso."),
        ("=", "{F} ¿A qué hora de uso toca el próximo mantenimiento?", "200+100", "Se suma el intervalo a la hora del último mantenimiento.", " horas"),
        ("=", "{F} ¿Cuántas horas faltan para el próximo mantenimiento?", "300-230", "Se resta lo acumulado de la hora del próximo.", " horas"),
        ("abc", "{F} Con 230 horas acumuladas, ¿está vencido el mantenimiento?", "No: aún faltan 70 horas", "Sí: ya pasó el intervalo", "Sí: no hay registro", "El próximo es a las 300 horas y aún no se llega."),
        ("=", "{F} Si se usa 10 horas por semana, ¿en cuántas semanas llega a la hora del próximo mantenimiento?", "70//10", "Las horas que faltan divididas por las horas semanales.", " semanas"),
        ("=", "{F} Si en la pauta se marcaron 4 de los 6 puntos, ¿cuántos faltan?", "6-4", "Se resta lo marcado del total.", " puntos"),
        ("abc", "{F} El equipo llegó a 310 horas acumuladas sin mantenimiento. ¿Qué corresponde?", "No usarlo y avisar para el mantenimiento vencido", "Seguir usándolo hasta que falle", "Marcar el mantenimiento como hecho", "El mantenimiento está vencido por 10 horas; se retira y se avisa."),
        ("ab", "{F} Un ayudante dice: «el mantenimiento puede esperar porque el equipo funciona». ¿Qué respuesta es correcta?", "No: se respeta el plan del manual aunque funcione", "Sí: mientras funciona no hace falta", "Una falla puede aparecer sin aviso; el plan previene."),
        ("abc", "{F} ¿Quién realiza el mantenimiento de la hormigonera?", "Personal autorizado según el manual", "Quien la use ese día", "Cualquier persona con herramientas", "El mantenimiento exige capacitación y autorización."),
        ("=", "{F} Después de 3 semanas de 10 horas cada una, ¿cuántas horas acumuladas tendrá?", "230+3*10", "Se suman las horas de las tres semanas a lo acumulado.", " horas"),
        ("abc", "{F} ¿Qué se anota después de un mantenimiento?", "La fecha, las horas acumuladas, qué se hizo y quién lo hizo", "Solo la fecha", "Solo el nombre del equipo", "Un registro útil permite revisar qué, cuándo y quién."),
    ],
    ctx=("abc", "La pauta diaria de un equipo tiene un punto sin marcar y el trabajo urgente apura. ¿Qué corresponde?", "Completar la pauta antes de usar el equipo", "Marcarla sin revisar", "Usar el equipo y marcar después", "Una pauta incompleta es una revisión pendiente; se completa antes de usar."),
    sc=[
        ("En Construcción: ¿qué son las horas acumuladas?", "El total de horas de uso del equipo", "Se anotan en la hoja de vida."),
        ("Último mantenimiento a las 60 horas e intervalo de 40. ¿Cuándo toca el próximo?", "A las 100 horas", "Se suma el intervalo a la hora del último."),
        ("¿Qué se hace con un mantenimiento vencido?", "No usar el equipo y avisar", "Usarlo sin mantenimiento aumenta el riesgo."),
    ],
    op=("Hoja de vida de ejemplo: compactadora C-1, horas acumuladas 175; intervalo 50 horas; último mantenimiento a las 150 horas; uso de 5 horas por semana. Escribe (a) a qué hora toca el próximo, (b) cuántas horas faltan, (c) en cuántas semanas llega, (d) qué anotas después del mantenimiento.",
        "(a) 150 más 50 son 200 horas. (b) 200 menos 175 son 25 horas. (c) 25 dividido en 5 son 5 semanas. (d) Fecha, horas acumuladas, qué se hizo y quién lo hizo.",
        ["calcula la próxima hora", "calcula las horas restantes", "calcula las semanas", "completa el registro"],
        ["hoja con las cuatro respuestas"],
        ["no sumar el intervalo al último", "restar al revés", "olvidar quién lo hizo"],
        "Pregunta: «¿desde dónde cuentas el intervalo?». Si no responde, pídele que relea la definición."),
    reinforce="Inventa una hoja de vida con tres datos y calcula la próxima hora de mantenimiento.",
    extend="Explica por qué el mantenimiento se mide en horas de uso y no solo en días.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 25 (caso de ejemplo, inventado). Taladro T-2. Hoja de vida: horas acumuladas 480; mantenimiento preventivo cada 120 horas; último a las 360 horas. "
     "Pauta diaria de 5 puntos: hoy se marcaron 4 y el punto «cable sin daños» quedó en blanco. Un operario comenta que el taladro hace un ruido anormal. "
     "Costos de ejemplo: mantenimiento preventivo $15.000; reparación correctiva $60.000.")
build(
    O6, 3, F,
    use="Aprenderé a analizar un caso de un equipo con señales de alerta y a decidir qué se registra, a quién se avisa y qué no se hace.",
    prior=["Sé calcular la próxima hora de mantenimiento.", "Sé qué es una pauta de revisión.", "Sé diferenciar mantenimiento preventivo y correctivo."],
    explain=[
        "Una señal de alerta es un hecho que indica que un equipo puede estar fallando: un ruido anormal, una vibración, un olor, un cable dañado o un punto sin revisar. Ante una señal de alerta el equipo se deja de usar y se avisa al responsable; no se hacen pruebas por cuenta propia. Si además el mantenimiento preventivo llegó a su hora, el equipo no vuelve a usarse hasta que lo revise personal autorizado.",
        "El costo de un mantenimiento preventivo suele ser menor que el de una reparación después de una falla. En este caso los costos son solo de ejemplo. Lo importante es registrar lo observado: qué equipo, qué se vio, quién lo dijo y la fecha. Un equipo eléctrico no se abre ni se repara en la obra sin autorización.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("señal de alerta", "hecho que indica que un equipo puede estar fallando"), ("ruido anormal", "ruido distinto del habitual del equipo"), ("retirar de servicio", "dejar de usar un equipo hasta que lo revise personal autorizado"), ("falla", "mal funcionamiento de un equipo")],
    worked=[
        ("Reconocer una señal", "Un operario de ejemplo nota un olor a quemado en una máquina. ¿Es una señal de alerta?", ["Un olor a quemado no es normal en un equipo.", "Sí, es una señal de alerta."], "Sí"),
        ("Diferencia de costos", "Un mantenimiento preventivo de ejemplo cuesta $8.000 y una reparación correctiva $30.000. ¿Cuánto más cuesta la correctiva?", ["Se resta el costo menor del mayor.", "30.000 menos 8.000 son 22.000."], "$22.000"),
    ],
    mistakes=[("Seguir usando el equipo «solo por hoy» tras un ruido anormal.", "El ruido puede anunciar una falla inminente.", "Retíralo de servicio y avisa."),
              ("Abrir el taladro para ver qué tiene.", "Un equipo eléctrico solo lo interviene personal autorizado.", "Informa lo observado y espera.")],
    T=[
        ("abc", "En Construcción: ¿qué es una señal de alerta de un equipo?", "Un hecho que indica que puede estar fallando", "Un cartel de color", "El nombre del fabricante", "La señal de alerta es un indicio de falla; no es un cartel ni un nombre."),
        ("abc", "¿Qué significa retirar un equipo de servicio?", "Dejar de usarlo hasta que lo revise personal autorizado", "Regalarlo", "Guardarlo en la bodega para usarlo mañana", "Retirar de servicio es no usarlo hasta su revisión por quien corresponde."),
        ("abc", "¿Cuál de estas es una señal de alerta?", "Un ruido anormal", "Un equipo limpio", "Una caja con el manual", "Un ruido distinto del habitual puede indicar una falla."),
        ("=", "{F} ¿A qué hora de uso toca el próximo mantenimiento del taladro?", "360+120", "Se suma el intervalo a la hora del último.", " horas"),
        ("abc", "{F} Con 480 horas acumuladas, ¿qué se puede decir del mantenimiento?", "Corresponde hacerlo hoy", "Faltan 120 horas", "Ya pasó hace 120 horas", "La hora 480 coincide con las horas acumuladas."),
        ("=", "{F} ¿Cuántos pesos más cuesta la reparación correctiva que el mantenimiento preventivo?", "60000-15000", "Se resta el costo menor del mayor.", " pesos"),
        ("abc", "{F} ¿Qué punto quedó sin marcar en la pauta?", "El cable sin daños", "El ruido", "La fecha", "La ficha dice que el punto «cable sin daños» quedó en blanco."),
        ("abc", "{F} ¿Qué corresponde hacer con el taladro?", "No usarlo y avisar al responsable", "Usarlo solo hoy", "Abrirlo para revisarlo", "Con una señal de alerta y mantenimiento vencido se retira de servicio."),
        ("ab", "{F} Un ayudante dice: «se usa hoy y se revisa mañana». ¿Qué respuesta es correcta?", "No: se retira de servicio desde ahora", "Sí: un día más no importa", "Una señal de alerta con mantenimiento vencido exige retirarlo de inmediato."),
        ("=", "{F} Si se hicieran 4 mantenimientos preventivos, ¿cuántos pesos costarían?", "4*15000", "Cantidad por el costo unitario.", " pesos"),
        ("=", "{F} ¿Cuántos puntos de la pauta faltan por marcar?", "5-4", "Se resta lo marcado del total.", " puntos"),
        ("abc", "{F} ¿Quién decide si el taladro vuelve a usarse?", "El responsable, tras la revisión de personal autorizado", "El operario que lo usa", "El primero que lo necesite", "El retorno al servicio lo decide quien tiene la responsabilidad tras la revisión."),
        ("abc", "{F} ¿Qué debe quedar escrito en el registro del caso?", "Qué equipo, qué se observó, quién lo dijo y la fecha", "Solo el nombre del operario", "Solo el costo del mantenimiento", "Un registro útil deja constancia de qué, qué se vio, quién y cuándo."),
    ],
    ctx=("abc", "El operario del caso dice que el taladro «anda bien, solo hace ruido». ¿Qué responde el supervisor?", "Que se retire de servicio y se registre la señal de alerta", "Que lo siga usando mientras no se trabe", "Que lo engrase por su cuenta", "Un ruido anormal es una señal de alerta y el equipo se retira."),
    sc=[
        ("En Construcción: ¿qué es retirar de servicio?", "Dejar de usar el equipo hasta su revisión", "Previene un accidente mientras no se revise."),
        ("¿Qué cuesta más, el preventivo o el correctivo (de ejemplo)?", "El correctivo", "Los costos de ejemplo muestran que reparar suele costar más."),
        ("¿Se abre un equipo eléctrico en la obra?", "No, solo personal autorizado", "Intervenir un equipo eléctrico exige autorización."),
    ],
    op=("Caso de ejemplo: la hormigonera H-2 tiene 340 horas acumuladas, intervalo de 100 horas y último mantenimiento a las 240. Hoy emite vibración anormal. Mantenimiento preventivo $20.000; correctivo $90.000. Escribe (a) cuándo tocaba el próximo mantenimiento, (b) si está vencido, (c) la diferencia de costos, (d) qué haces con el equipo.",
        "(a) 240 más 100 son 340 horas. (b) Corresponde hoy. (c) 90.000 menos 20.000 son $70.000. (d) Lo retiro de servicio, registro la señal y aviso al responsable.",
        ["calcula la próxima hora", "interpreta el estado", "calcula la diferencia", "retira y avisa"],
        ["hoja con las cuatro respuestas"],
        ["seguir usando el equipo", "restar mal", "intervenirlo por su cuenta"],
        "Pregunta: «¿qué significa la vibración anormal?». Si no responde, pídele que relea qué es una señal de alerta."),
    reinforce="Escribe tres señales de alerta de un equipo y qué haces ante cada una.",
    extend="Explica por qué una pauta con un punto sin marcar es una revisión pendiente.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 26 (programación de ejemplo, inventada). Tres equipos. E-1: 285 horas acumuladas, intervalo 100, último mantenimiento a las 200. "
     "E-2: 410 horas acumuladas, intervalo 150, último a las 300. E-3: 120 horas acumuladas, intervalo 60, último a las 60. "
     "Costos de ejemplo del mantenimiento preventivo: E-1 $20.000; E-2 $30.000; E-3 $10.000.")
build(
    O6, 4, F,
    use="Aprenderé a programar mantenimientos de varios equipos con datos de ejemplo, a priorizar por urgencia y a calcular el costo.",
    prior=["Sé calcular la próxima hora de mantenimiento.", "Sé calcular horas restantes.", "Sé sumar costos."],
    explain=[
        "Una programación de mantenimiento es una tabla con los equipos, su próxima hora de mantenimiento y las horas que faltan. Con ella se decide el orden: se atiende primero el equipo al que le faltan menos horas o que ya llegó a su hora. Priorizar es ordenar las tareas según su urgencia. Para calcular, se obtiene la próxima hora de cada equipo y se resta lo acumulado.",
        "El costo del plan es la suma de los costos de cada mantenimiento. La programación la aprueba el responsable de la obra y quien ejecuta es personal autorizado. En este cuaderno los datos son de ejemplo y no sustituyen el manual de ningún fabricante. Si un equipo llegó a su hora, se deja de usar hasta su mantenimiento.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("programación de mantenimiento", "tabla con equipos, próxima hora y horas que faltan"), ("priorizar", "ordenar tareas según su urgencia"), ("urgencia", "qué tan pronto hay que atender algo"), ("plan", "conjunto ordenado de tareas")],
    worked=[
        ("Priorizar dos equipos", "A un equipo de ejemplo le faltan 12 horas y a otro 30. ¿Cuál se atiende primero?", ["Se atiende primero al que le faltan menos horas.", "A 12 es menor que 30."], "El que tiene 12 horas"),
        ("Costo de un plan", "Un plan de ejemplo tiene dos mantenimientos de $12.000 y uno de $25.000. ¿Cuánto cuesta el plan?", ["Se suman los tres costos.", "12.000 más 12.000 más 25.000 son 49.000."], "$49.000"),
    ],
    mistakes=[("Atender primero el equipo que más se usa sin mirar las horas que faltan.", "La urgencia se mide por las horas que faltan.", "Ordena por horas restantes."),
              ("Dejar sin mantener un equipo que ya llegó a su hora.", "Está vencido y es un riesgo.", "Retíralo de servicio y avisa.")],
    T=[
        ("abc", "En Construcción: ¿qué es priorizar tareas de mantenimiento?", "Ordenarlas según su urgencia", "Hacerlas todas el mismo día", "Elegir las más baratas", "Priorizar es ordenar por urgencia; no es hacerlo todo ni elegir por costo."),
        ("abc", "¿Qué equipo se atiende primero en una programación?", "El que tiene menos horas restantes o ya llegó a su hora", "El más caro", "El que se compró primero", "La urgencia depende de las horas que faltan."),
        ("abc", "¿Qué contiene una programación de mantenimiento?", "Equipos, próxima hora y horas que faltan", "Los planos de la obra", "Los pagos de los trabajadores", "La programación ordena el mantenimiento y no incluye planos ni pagos."),
        ("=", "{F} ¿A qué hora toca el mantenimiento de E-1?", "200+100", "Se suma el intervalo a la hora del último.", " horas"),
        ("=", "{F} ¿Cuántas horas le faltan a E-1?", "300-285", "Se resta lo acumulado de la próxima hora.", " horas"),
        ("=", "{F} ¿A qué hora toca el mantenimiento de E-2?", "300+150", "Se suma el intervalo a la hora del último.", " horas"),
        ("=", "{F} ¿Cuántas horas le faltan a E-2?", "450-410", "Se resta lo acumulado de la próxima hora.", " horas"),
        ("abc", "{F} ¿A qué equipo le toca el mantenimiento hoy?", "E-3, porque llegó a la hora 120", "E-1", "E-2", "E-3 tiene 120 horas acumuladas y su próxima hora es 60 más 60, es decir 120."),
        ("=", "{F} ¿Cuánto cuestan los tres mantenimientos preventivos juntos?", "20000+30000+10000", "Se suman los tres costos.", " pesos"),
        ("=", "{F} Si E-2 se usa 5 horas por semana, ¿en cuántas semanas llega a su hora?", "40//5", "Horas restantes divididas por las horas semanales.", " semanas"),
        ("abc", "{F} ¿Cuál es el orden de prioridad según las horas que faltan?", "E-3, E-1 y E-2", "E-1, E-2 y E-3", "E-2, E-1 y E-3", "A E-3 le faltan 0, a E-1 le faltan 15 y a E-2 le faltan 40."),
        ("ab", "{F} Un ayudante dice: «dejemos E-3 para después porque funciona». ¿Qué respuesta es correcta?", "No: E-3 ya llegó a su hora y se retira de servicio", "Sí: si funciona puede esperar", "Un equipo que llegó a su hora de mantenimiento no se usa."),
        ("abc", "{F} ¿Quién aprueba la programación y quién ejecuta el mantenimiento?", "La aprueba el responsable de la obra y la ejecuta personal autorizado", "La aprueba y ejecuta cualquier trabajador", "La aprueba el proveedor y la ejecuta el cliente", "La programación se aprueba por el responsable y la ejecuta personal autorizado."),
    ],
    ctx=("abc", "El jefe de obra de ejemplo pide dejar E-1 y E-2 para el mes siguiente porque hay mucho trabajo. ¿Qué corresponde recordarle?", "Que a E-1 le faltan 15 horas y que si llega a su hora debe detenerse para su mantenimiento", "Que no hay problema porque los equipos duran", "Que el mantenimiento es opcional", "Llegar a la hora de mantenimiento sin hacerlo aumenta el riesgo y la probabilidad de falla."),
    sc=[
        ("En Construcción: ¿qué significa priorizar?", "Ordenar por urgencia", "Se atiende primero lo más urgente."),
        ("Último a las 100 horas e intervalo 80. ¿Cuándo toca el próximo?", "A las 180 horas", "Se suma el intervalo a la hora del último."),
        ("¿Quién aprueba la programación?", "El responsable de la obra", "Ese cargo responde por el plan."),
    ],
    op=("Programación de ejemplo: M-1 con 90 horas acumuladas, intervalo 50, último a las 50; M-2 con 130 horas, intervalo 80, último a las 80. Costos de ejemplo: M-1 $12.000; M-2 $18.000. Escribe (a) la próxima hora de cada uno, (b) cuántas horas faltan a cada uno, (c) cuál se atiende primero, (d) el costo total.",
        "(a) M-1: 100 horas; M-2: 160 horas. (b) M-1: 10 horas; M-2: 30 horas. (c) M-1. (d) $30.000.",
        ["calcula las próximas horas", "calcula las horas restantes", "prioriza bien", "suma los costos"],
        ["hoja con las cuatro respuestas"],
        ["no sumar el intervalo al último", "priorizar por costo", "olvidar un costo"],
        "Pregunta: «¿cuál tiene menos horas restantes?». Si no responde, pídele que relea cómo se prioriza."),
    reinforce="Inventa una programación de tres equipos y ordénalos por urgencia.",
    extend="Explica por qué un plan de mantenimiento ahorra más dinero que reparar solo cuando algo falla.",
)
