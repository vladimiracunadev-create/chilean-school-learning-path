"""Instalaciones Sanitarias TP 3.º y 4.º medio: OAE-03 (trazar redes: puntos de referencia, niveles y replanteo, solo conceptos y cálculos en papel) y OAE-04 (redes y artefactos de gas en baja presión: solo conceptos, documentos y seguridad)."""
from __future__ import annotations

from tp_insa_common import AVISO, EMER, build

O3 = "TP-INSA-3y4-OAE-03"
O4 = "TP-INSA-3y4-OAE-04"

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La empresa ficticia «Sanitaria Cordillera» debe preparar el trazado de la red de evacuación de una casa de ejemplo en un terreno de 20 m de largo. "
     "El plano indica un punto de referencia (P.R.) dentro del terreno, cotas de nivel, una cámara existente de una red pública de ejemplo y, en un plano de interferencias, una línea de gas enterrada. "
     "Riesgos anotados: zanjas, redes enterradas, maquinaria y tránsito de vehículos.")
build(
    O3, 1, F,
    use="Aprenderé qué significa trazar una red, qué riesgos tiene el trabajo en terreno, por qué se revisan las redes enterradas y qué cuidados ambientales corresponden.",
    prior=["Sé leer un plano y su escala.", "Sé qué es una cota y un desnivel de manera general.", "Sé qué es una red de evacuación."],
    explain=[
        "Trazar una red es pasar el diseño de los planos al terreno, para que cada tubería quede donde el proyecto la pide. Esa tarea se llama replanteo. Para hacerla se parte de un punto de referencia (P.R.), un punto fijo y conocido desde el cual se miden las posiciones y las alturas. El nivel de un punto es su altura respecto de un plano horizontal de comparación. El replanteo lo hace personal capacitado, como un topógrafo, con equipos e instrumentos que este cuaderno no enseña a manejar.",
        "El terreno tiene riesgos. Las zanjas pueden derrumbarse y atrapar o hacer caer a una persona. Bajo el suelo hay redes enterradas de gas, electricidad, agua y telecomunicaciones, y golpearlas puede causar incendio, explosión o electrocución. Una interferencia es otra red u obra que se cruza con el trazado; se identifica antes de intervenir el suelo, revisando los planos de interferencias y consultando a las empresas dueñas de las redes. También hay riesgos por maquinaria y tránsito. El cuidado ambiental exige manejar la tierra y los escombros según el plan de la obra, sin dañar cauces ni calles.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("trazar una red", "pasar el diseño de los planos al terreno"), ("replanteo", "tarea de marcar en el terreno la posición y la altura que indican los planos"), ("punto de referencia (P.R.)", "punto fijo y conocido desde el cual se miden posiciones y alturas"), ("nivel", "altura de un punto respecto de un plano horizontal de comparación"), ("interferencia", "otra red u obra que se cruza con el trazado"), ("topógrafo", "profesional que mide el terreno y marca el replanteo")],
    worked=[
        ("Reconocer una interferencia", "En un plano de ejemplo, el trazado de una tubería de evacuación cruza una canalización eléctrica enterrada. ¿Qué es la canalización respecto del trazado?", ["Es otra red que se cruza con el trazado.", "Eso es una interferencia."], "Una interferencia"),
        ("Perímetro de una zona de protección", "Una zona de ejemplo de 5 m por 3 m se rodea con una cinta de seguridad. ¿Cuántos metros de cinta se necesitan?", ["El perímetro suma los cuatro lados: 5 + 3 + 5 + 3.", "Eso da 16 m."], "16 m"),
    ],
    mistakes=[("Pensar que si una red enterrada está profunda no importa.", "Una máquina o una herramienta puede alcanzarla igual.", "Revisa los planos de interferencias y consulta a las empresas antes de intervenir el suelo."),
              ("Creer que leer este cuaderno habilita para excavar o para marcar el terreno.", "Esas tareas exigen personal capacitado y autorizado.", "Aprende los conceptos y deja el terreno a personal autorizado.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué significa trazar una red?", "Pasar el diseño de los planos al terreno", "Dibujar los planos de la red", "Hacer el presupuesto de la red", "Trazar es llevar el diseño al terreno; dibujar y presupuestar son tareas anteriores."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es un punto de referencia (P.R.)?", "Un punto fijo y conocido desde el cual se miden posiciones y alturas", "Un punto elegido al azar en cada medición", "La cámara más profunda de la red", "Un P.R. sirve de base común; si cambia de lugar, las mediciones no son comparables."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es una interferencia?", "Otra red u obra que se cruza con el trazado", "Un error de dibujo del plano", "Un cambio de escala entre dos láminas", "Una interferencia es algo que se cruza con el trazado y exige coordinación."),
        ("=", "{F} La red de la casa ocupa 12 m del terreno de 20 m de largo. ¿Cuántos metros del terreno quedan sin red?", "20-12", "Se resta lo que ocupa la red al largo del terreno.", " m"),
        ("abc", "{F} ¿Qué documento ayuda a prevenir un golpe a la línea de gas enterrada?", "El plano de interferencias, junto con la consulta a la empresa dueña de la red", "El presupuesto de la obra", "La lista de materiales de la casa", "El plano de interferencias muestra las redes que se cruzan con el trazado."),
        ("abc", "{F} ¿Cuál es el riesgo principal de las zanjas anotado en la ficha?", "Derrumbe, atrapamiento o caída de personas", "Quemaduras por el sol", "Pérdida de las láminas del plano", "Una zanja puede derrumbarse o provocar caídas; es un riesgo grave."),
        ("=", "Antes de trazar, un equipo de ejemplo consulta a 3 empresas dueñas de redes y cada consulta toma 2 horas. ¿Cuántas horas de consulta suman?", "3*2", "Se multiplican las empresas consultadas por las horas de cada consulta.", " horas"),
        ("abc", "En una obra de ejemplo, una persona observa que una zanja se derrumbó y hay alguien atrapado. ¿Qué corresponde según las reglas generales?", "No entrar a la zanja, avisar a un adulto responsable y a emergencias", "Entrar de inmediato a sacar a la persona", "Esperar a ver si se levanta sola", "Entrar a una zanja derrumbada puede causar un segundo atrapamiento; se avisa a quienes pueden rescatar."),
        ("ab", "Un estudiante que terminó este cuaderno quiere excavar en su patio para «comprobar» un trazado de ejemplo. ¿Qué corresponde?", "No hacerlo: excavar exige personal autorizado y revisar las redes enterradas", "Hacerlo con una pala pequeña, porque ya sabe qué es un P.R.", "Excavar sin revisar redes enterradas es de riesgo alto; el cuaderno no habilita para intervenir el terreno."),
        ("abc", "{F} Un compañero dice: «la línea de gas va profunda, no hay que preocuparse». ¿Qué respuesta es correcta?", "Es falso: igual se revisa el plano de interferencias y se consulta a la empresa antes de intervenir el suelo", "Es cierto: lo profundo nunca se alcanza", "Es cierto si la maquinaria es liviana", "Una red profunda puede alcanzarse con maquinaria; por eso se coordina antes."),
        ("abc", "¿Qué corresponde hacer con la tierra y los escombros de una obra de ejemplo, según el cuidado ambiental?", "Manejarlos según el plan de la obra, sin dañar cauces ni calles", "Botarlos en el cauce más cercano", "Dejarlos en la vereda para que alguien los retire", "El plan de la obra define el manejo de residuos para no dañar el entorno."),
        ("=", "Un cerco de seguridad de ejemplo rodea una zona de 6 m por 4 m. ¿Cuántos metros de cerco se necesitan?", "2*(6+4)", "El perímetro suma los dos largos y los dos anchos del rectángulo.", " m"),
        ("abc", "¿Cuál es un orden lógico de preparación antes de que personal calificado trabaje en el terreno?", "Revisar planos y permisos, consultar interferencias, planificar los riesgos y recién después autorizar el trabajo", "Autorizar el trabajo, luego revisar los planos y después consultar las interferencias", "Excavar primero y consultar las interferencias si algo aparece", "Primero se informa y se planifica; el trabajo se autoriza al final."),
    ],
    ctx=("abc", "Un contratista de ejemplo te dice: «ayúdame a excavar un poco para ver si hay algo debajo; eres joven y ágil». ¿Qué respondes?", "Que no, porque excavar sin revisar las redes enterradas es riesgoso y exige personal autorizado", "Que sí, pero solo un poco", "Que sí, si él se queda mirando", "El riesgo de golpear una red o de un derrumbe no depende de cuánto se excave."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué es el replanteo?", "Marcar en el terreno la posición y la altura que indican los planos", "El replanteo lleva el diseño de los planos al terreno."),
        ("¿Qué es una interferencia?", "Otra red u obra que se cruza con el trazado", "Se identifica antes de intervenir el suelo."),
        ("¿Quién hace el replanteo en una obra?", "Personal capacitado y autorizado, como un topógrafo", "Este cuaderno no habilita para trabajar en terreno."),
    ],
    op=("Ficha de ejemplo: terreno de 25 m de largo, red de evacuación que ocupa 15 m, un plano de interferencias que muestra un cable eléctrico enterrado que cruza el trazado y una zona de 4 m por 2 m que se debe cercar. Escribe (a) cuántos metros del terreno quedan sin red, (b) cuántos metros de cerco necesita la zona, (c) cómo se llama el cable respecto del trazado y qué documento lo muestra, (d) qué tarea de la obra no te corresponde.",
        "(a) 25 − 15 = 10 m. (b) 2 × (4 + 2) = 12 m. (c) Una interferencia; la muestra el plano de interferencias. (d) Excavar o intervenir el terreno: lo hace personal autorizado.",
        ["calcula los metros sin red", "calcula el perímetro", "nombra la interferencia y el documento", "reconoce la tarea que no le corresponde"],
        ["hoja con las cuatro respuestas"],
        ["sumar en vez de restar", "confundir el perímetro con el área", "creer que puede excavar"],
        "Pregunta: «¿qué se consulta antes de intervenir el suelo?». Si no responde, pídele que relea el párrafo de interferencias."),
    reinforce="Escribe una lista de cuatro riesgos de una obra en el terreno y, junto a cada uno, una medida general de prevención.",
    extend="Explica con un ejemplo por qué es importante coordinar con las empresas dueñas de las redes antes de intervenir el suelo.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (registro de cotas de ejemplo, inventado, tomado por personal autorizado). Cotas en cm sobre un plano horizontal de comparación. Punto de referencia P.R.: 500 cm. Punto A: 470 cm. Punto B: 455 cm. "
     "Cámara existente C (cota del fondo): 430 cm. La evacuación por gravedad exige que cada punto siguiente en el sentido del escurrimiento tenga una cota más baja que el anterior.")
build(
    O3, 2, F,
    use="Aprenderé los conceptos de cota, desnivel y escurrimiento por gravedad, qué documentos se usan para el trazado y qué rol cumple cada persona.",
    prior=["Sé restar números.", "Sé qué es un P.R. y un replanteo.", "Sé leer una tabla de valores."],
    explain=[
        "Una cota es la altura de un punto medida desde un plano de comparación. El desnivel entre dos puntos es la diferencia de sus cotas: si A está a 470 cm y B a 455 cm, el desnivel es 15 cm y B queda más abajo. Las aguas servidas escurren por gravedad: bajan desde el punto más alto hacia el más bajo. Por eso, en una evacuación, cada punto siguiente debe tener una cota menor que el anterior; si no, el agua no avanza como el proyecto espera.",
        "Los instrumentos de medición, como la huincha (una cinta métrica) y los niveles, los maneja personal capacitado; aquí solo se leen sus registros. Los documentos del trazado son el plano de replanteo, el registro de cotas, el plano de interferencias y la bitácora, que es el cuaderno de la obra donde se anotan los hechos del día. El topógrafo mide y marca, el jefe de obra organiza, el ITO verifica y el prevencionista cuida la seguridad.",
        f"Los números de este cuaderno son de ejemplo para practicar la lectura de un registro. {EMER} {AVISO}",
    ],
    vocab=[("cota", "altura de un punto medida desde un plano de comparación"), ("desnivel", "diferencia de cotas entre dos puntos"), ("escurrimiento por gravedad", "movimiento del agua desde un punto más alto hacia uno más bajo"), ("huincha", "cinta métrica"), ("bitácora", "cuaderno de la obra donde se anotan los hechos del día"), ("prevencionista", "persona que cuida la seguridad y la prevención de riesgos")],
    worked=[
        ("Calcular un desnivel", "En un registro de ejemplo, el punto M está a 380 cm y el punto N a 365 cm. ¿Cuántos centímetros de desnivel hay y cuál está más abajo?", ["380 menos 365 son 15 cm.", "El punto N tiene la cota menor, por eso está más abajo."], "15 cm; N está más abajo"),
        ("Sentido del escurrimiento", "El punto X está a 300 cm y el punto Y a 310 cm. ¿Puede escurrir el agua por gravedad de X hacia Y?", ["Para escurrir de X a Y, Y debe estar más abajo.", "Y está más arriba, así que no."], "No: Y está más arriba"),
    ],
    mistakes=[("Restar al revés y concluir que un punto bajo es más alto.", "Una cota menor significa un punto más bajo.", "Compara las cotas y recuerda que el agua baja hacia la cota menor."),
              ("Creer que el estudiante puede usar los instrumentos porque entiende el registro.", "Los instrumentos los maneja personal capacitado.", "Usa este cuaderno solo para leer registros.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es una cota?", "La altura de un punto medida desde un plano de comparación", "La distancia entre dos tuberías", "El diámetro de una tubería", "Una cota expresa una altura respecto de un plano de comparación."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es un desnivel?", "La diferencia de cotas entre dos puntos", "La suma de las longitudes de dos tramos", "El largo total de la red", "El desnivel mide cuánto más alto está un punto que otro."),
        ("abc", "En Instalaciones Sanitarias: ¿hacia dónde escurre el agua por gravedad?", "Desde el punto más alto hacia el más bajo", "Desde el punto más bajo hacia el más alto", "Hacia cualquier punto del mismo plano", "La gravedad empuja el agua hacia abajo."),
        ("=", "{F} ¿Cuántos centímetros de desnivel hay entre el punto A y el punto B?", "470-455", "Se resta la cota del punto más bajo a la del más alto.", " cm"),
        ("=", "{F} ¿Cuántos centímetros más bajo está la cámara C que el punto de referencia P.R.?", "500-430", "Se resta la cota de la cámara a la del P.R.", " cm"),
        ("abc", "{F} ¿Cuál de los puntos A, B y C es el más alto?", "El punto A", "El punto B", "La cámara C", "Entre 470, 455 y 430 cm, el mayor es 470 cm, el del punto A."),
        ("abc", "{F} ¿Puede escurrir el agua por gravedad desde A hacia B?", "Sí, porque B está más abajo que A", "No, porque B está más abajo que A", "No, porque están en el mismo plano", "Un punto siguiente más bajo permite el escurrimiento por gravedad."),
        ("abc", "{F} ¿Puede escurrir el agua por gravedad desde la cámara C hacia el punto A?", "No, porque A está más arriba que C", "Sí, porque C es una cámara", "Sí, porque A es el primer punto del registro", "Para bajar el agua, el punto de llegada debe tener una cota menor."),
        ("=", "{F} Un punto D está 25 cm más bajo que el punto B. ¿Cuál es la cota de D?", "455-25", "Se resta el desnivel a la cota del punto B.", " cm"),
        ("abc", "{F} Si el sentido de escurrimiento va A, B y C, ¿cuántos centímetros baja entre A y C?", "40 cm", "25 cm", "70 cm", "La cota baja de 470 a 430 cm, es decir, 40 cm; 70 cm es la distancia desde el P.R."),
        ("abc", "¿Dónde se anotan los hechos del día de una obra, como una revisión o una novedad?", "En la bitácora", "En la leyenda del plano", "En la lista de precios", "La bitácora es el cuaderno de la obra para registrar lo ocurrido cada día."),
        ("=", "{F} ¿Cuántos centímetros baja el nivel desde el P.R. hasta el punto B?", "500-455", "Se resta la cota de B a la del P.R.", " cm"),
        ("abc", "Un ayudante nuevo de ejemplo quiere usar un nivel porque «ya entendió el registro». ¿Qué corresponde?", "Que lo use solo personal capacitado y autorizado, y él se capacite con instructor", "Que lo use de inmediato, porque el registro es fácil", "Que lo use si nadie lo ve", "Entender un registro no capacita para manejar instrumentos."),
    ],
    ctx=("abc", "En una reunión de ejemplo, el jefe de obra pregunta a quién corresponde verificar que lo ejecutado cumpla el plano. ¿Qué respondes?", "Al inspector técnico de obra (ITO)", "Al proveedor de la tubería", "Al topógrafo, quien también construye la red", "El ITO verifica el cumplimiento del proyecto; el topógrafo mide y marca."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se calcula un desnivel?", "Restando las cotas de los dos puntos", "El desnivel es la diferencia de alturas."),
        ("¿Hacia dónde escurre el agua por gravedad?", "Hacia el punto de menor cota", "El agua baja desde lo alto hacia lo bajo."),
        ("¿Para qué sirve la bitácora de obra?", "Para anotar los hechos del día", "Deja constancia escrita de lo ocurrido."),
    ],
    op=("Ficha de ejemplo: registro de cotas en cm. P.R.: 600. Punto E: 570. Punto F: 540. Cámara G (fondo): 500. Escribe (a) el desnivel entre E y F, (b) el desnivel entre el P.R. y G, (c) si el agua puede escurrir de E a F a G y por qué, (d) si podría escurrir de G a E y por qué.",
        "(a) 570 − 540 = 30 cm. (b) 600 − 500 = 100 cm. (c) Sí, porque cada punto siguiente tiene una cota menor (570, 540, 500). (d) No, porque E está más arriba que G.",
        ["calcula los dos desniveles", "razona el sentido E-F-G", "razona el sentido inverso"],
        ["hoja con los cálculos y las razones"],
        ["restar al revés", "decir que el agua sube", "no justificar con las cotas"],
        "Pregunta: «¿qué punto del registro es el más bajo?». Si no responde, pídele que ordene las cotas de mayor a menor."),
    reinforce="Inventa un registro de cuatro cotas y escribe el desnivel entre cada par de puntos consecutivos.",
    extend="Explica con un ejemplo por qué la gravedad obliga a que cada punto siguiente tenga una cota menor.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (caso en papel, de ejemplo, inventado). Ruta de evacuación de una casa de ejemplo. Cotas en cm. Salida del baño S (fondo del tubo): 462 cm. "
     "Tramo S–CC de 8 m hasta la cámara de la casa CC. Tramo CC–CP de 10 m hasta la cámara pública existente CP, cuyo fondo está a 420 cm. "
     "Para esta planilla se usa una pendiente de ejemplo de 2 % (valor de ejemplo, no normativo): el desnivel en cm es la longitud en metros por 2.")
build(
    O3, 3, F,
    use="Aprenderé a recorrer en papel una ruta de evacuación calculando la cota de cada punto con una pendiente de ejemplo y a decidir si el desnivel disponible alcanza.",
    prior=["Sé calcular un desnivel.", "Sé usar la pendiente en porcentaje de una planilla.", "Sé qué es escurrimiento por gravedad."],
    explain=[
        "Un caso en papel se resuelve ordenando los datos. La cota de un punto aguas abajo (más adelante en el sentido del escurrimiento) es la cota del punto anterior menos el desnivel del tramo. Con una pendiente de ejemplo del 2 %, un tramo de 6 m baja 12 cm: 6 por 2. La cámara de llegada es el punto final de la ruta, y su fondo se compara con el fondo del último tramo.",
        "La ruta funciona por gravedad solo si el fondo de llegada calculado de la ruta queda a una cota mayor o igual que la cota del fondo de la cámara existente. El margen es esa diferencia. Si el margen es negativo, la ruta no cumple: no se cambia la pendiente por cuenta propia ni se rompe la cámara; se registra el resultado y se informa al proyectista y al ITO para que decidan.",
        f"El cálculo en planilla no reemplaza el proyecto ni la norma vigente: los valores reales los fijan ellos. {EMER} {AVISO}",
    ],
    vocab=[("aguas abajo", "más adelante en el sentido del escurrimiento"), ("cámara de llegada", "punto final de la ruta donde descarga la red"), ("margen", "diferencia disponible entre el valor calculado y el exigido"), ("planilla de cálculo", "cuadro de papel donde se ordenan datos y operaciones")],
    worked=[
        ("Cota de un punto", "En un caso de ejemplo, el punto P tiene cota 300 cm. El tramo siguiente mide 5 m con pendiente de ejemplo de 2 %. ¿Cuál es la cota del punto siguiente?", ["El tramo baja 5 por 2, es decir 10 cm.", "300 menos 10 son 290 cm."], "290 cm"),
        ("Margen", "La ruta de otro caso de ejemplo llega calculada a 355 cm y la cámara existente tiene el fondo a 350 cm. ¿Cuál es el margen?", ["Se resta la cota de la cámara a la cota calculada.", "355 menos 350 son 5 cm."], "5 cm de margen"),
    ],
    mistakes=[("Sumar el desnivel en lugar de restarlo al bajar por el tramo.", "Al avanzar con el escurrimiento la cota disminuye.", "Resta el desnivel a la cota del punto anterior."),
              ("Cambiar la pendiente a mano para que el cálculo dé.", "La pendiente la fija el proyecto y la norma vigente.", "Registra el resultado y consulta al proyectista y al ITO.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué significa «aguas abajo» en una ruta de evacuación?", "Más adelante en el sentido del escurrimiento", "Debajo del nivel del suelo", "En el punto de partida", "Aguas abajo es la dirección hacia donde avanza el agua."),
        ("abc", "En Instalaciones Sanitarias: ¿cómo se calcula la cota de un punto aguas abajo?", "Restando el desnivel del tramo a la cota del punto anterior", "Sumando el desnivel del tramo a la cota anterior", "Multiplicando las dos cotas", "Al avanzar con el escurrimiento la cota baja."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es el margen de una ruta?", "La diferencia disponible entre el valor calculado y el exigido", "El costo total de los tramos", "La longitud sobrante de tubería", "El margen indica cuánto sobra o falta para cumplir."),
        ("=", "{F} ¿Cuántos centímetros baja el tramo S–CC, de 8 m?", "8*2", "Se multiplica la longitud en metros por el porcentaje de pendiente.", " cm"),
        ("=", "{F} ¿Cuál es la cota del fondo en la cámara de la casa CC?", "462-8*2", "A la cota de S se resta lo que baja el tramo S–CC.", " cm"),
        ("=", "{F} ¿Cuántos centímetros baja el tramo CC–CP, de 10 m?", "10*2", "Se multiplica la longitud en metros por el porcentaje de pendiente.", " cm"),
        ("=", "{F} ¿Cuál es la cota calculada en la llegada a CP?", "462-8*2-10*2", "Se restan los desniveles de los dos tramos a la cota de S.", " cm"),
        ("=", "{F} ¿Cuántos centímetros de margen hay respecto del fondo de CP?", "462-8*2-10*2-420", "Se resta la cota del fondo de CP a la cota calculada de llegada.", " cm"),
        ("abc", "{F} Con el margen calculado, ¿qué se concluye sobre la ruta?", "Cumple por gravedad en el cálculo de ejemplo, con un margen pequeño", "No cumple, porque el margen es negativo", "No se puede concluir, porque falta la pendiente", "El margen resultó positivo y la planilla de ejemplo trae todos los datos."),
        ("abc", "En otro caso de ejemplo la cota calculada de llegada es 410 cm y el fondo de la cámara existente está a 415 cm. ¿Qué corresponde?", "Registrar que no cumple e informar al proyectista y al ITO", "Cambiar la pendiente para que dé", "Romper la cámara para bajar su fondo", "Con margen negativo la decisión es del proyecto, no de quien calcula."),
        ("abc", "{F} Un compañero propone subir la pendiente de 2 % a 4 % «para ganar margen», sin consultar. ¿Qué respuesta es correcta?", "No: la pendiente la fija el proyecto, y cualquier cambio se consulta", "Sí: más pendiente siempre es mejor", "Sí, pero solo si nadie lo nota", "Cambiar datos de diseño sin autorización altera el proyecto."),
        ("=", "En un caso de ejemplo, un tramo de 12 m baja con pendiente de ejemplo de 2 %. Si empieza en 400 cm, ¿en cuántos centímetros termina?", "400-12*2", "Se resta el desnivel del tramo a la cota inicial.", " cm"),
        ("abc", "¿Qué debe incluir la nota de registro de un resultado con margen negativo?", "Los puntos, las cotas, el margen y a quién se informó", "Solo la palabra «no cumple»", "El nombre de quien hizo el plano, sin cotas", "Una nota completa permite a otro revisar el cálculo."),
    ],
    ctx=("abc", "Un amigo de ejemplo te dice que su casa «tiene la cámara más alta que el baño» y pregunta si puedes arreglarlo rompiendo la cámara. ¿Qué respondes?", "Que no intervengas; debe consultar a un profesional autorizado, porque la solución depende del proyecto", "Que sí, que rompan la cámara y la bajen", "Que cambien la pendiente del tubo a ojo", "Un problema de niveles se resuelve con diseño y autorización, no improvisando."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se calcula el desnivel de un tramo en la planilla de ejemplo?", "Longitud en metros por pendiente en porcentaje", "Con la regla de la planilla, el resultado queda en centímetros."),
        ("¿Qué pasa con la cota al avanzar con el escurrimiento?", "Disminuye", "El agua baja, por eso la cota baja."),
        ("¿Qué se hace con un margen negativo?", "Se registra e informa al proyectista y al ITO", "No se improvisan cambios de diseño."),
    ],
    op=("Ficha de ejemplo: ruta de evacuación; pendiente de ejemplo de 2 %. Salida del baño S: 380 cm. Tramo S–CC de 6 m. Tramo CC–CP de 9 m. Fondo de la cámara existente CP: 340 cm. Escribe (a) la cota en CC, (b) la cota de llegada a CP, (c) el margen respecto de CP, (d) si cumple y qué harías si el margen fuera negativo.",
        "(a) 380 − 6 × 2 = 368 cm. (b) 368 − 9 × 2 = 350 cm. (c) 350 − 340 = 10 cm. (d) Cumple, porque el margen es positivo. Si fuera negativo se registraría e informaría al proyectista y al ITO sin cambiar la pendiente.",
        ["calcula la cota en CC", "calcula la cota de llegada", "calcula el margen", "concluye y propone qué hacer con un margen negativo"],
        ["hoja con la planilla de cálculo y la conclusión"],
        ["sumar en vez de restar", "olvidar restar la cota de CP", "proponer cambiar la pendiente"],
        "Pregunta: «¿qué cota tendría CC si el tramo S–CC fuera de 10 m?». Si no responde, pídele que relea cómo se calcula el desnivel."),
    reinforce="Calcula en papel las cotas de tres puntos consecutivos con tramos de 4 m, 7 m y 5 m, una pendiente de ejemplo de 2 % y una cota inicial de 300 cm.",
    extend="Explica con un ejemplo por qué la decisión sobre un margen negativo no corresponde a quien calcula.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (registro de ejemplo, inventado; las cotas las tomó personal autorizado). Cotas en cm. Terreno y fondo de las cámaras: cámara C1, terreno 500, fondo 446; cámara C2, terreno 497, fondo 426; cámara C3, terreno 495, fondo 340. "
     "Profundidad de una cámara = cota del terreno − cota del fondo. Criterio de ejemplo (no normativo): una cámara con más de 150 cm de profundidad exige un plan especial de seguridad. "
     "Verificación del P.R.: la primera lectura dio 500 cm y la segunda 503 cm; se acepta si ambas difieren en 1 cm o menos.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: calcular la profundidad de las cámaras, detectar las que exigen un plan especial y verificar un punto de referencia antes de usarlo.",
    prior=["Sé restar cotas.", "Sé qué es un P.R.", "Sé qué es una tolerancia."],
    explain=[
        "La profundidad de una cámara es la diferencia entre la cota del terreno y la del fondo. A mayor profundidad, mayor riesgo: las cámaras profundas pueden tener poco aire respirable o gases, y una persona atrapada o caída es difícil de rescatar. Un recinto cerrado o de acceso difícil se llama espacio confinado. Entrar a una cámara es una tarea de personal autorizado, con plan especial y equipos de protección y rescate; un estudiante nunca entra.",
        "Antes de usar un P.R. para trazar, se verifica: se toman dos lecturas y se comparan con una tolerancia. Si difieren más de lo permitido, no se usa ese P.R. hasta que personal autorizado lo revise, porque un error en la base se traspasa a todo el trazado. Este es un criterio técnico: se compara un dato con una regla y se decide con evidencia.",
        f"El límite de 150 cm de esta ficha es de ejemplo; los límites reales los fija la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("profundidad de una cámara", "diferencia entre la cota del terreno y la del fondo"), ("espacio confinado", "recinto cerrado o de acceso difícil donde puede faltar aire respirable o haber gases"), ("plan especial de seguridad", "documento que define cómo se controla un riesgo alto con personal autorizado"), ("verificación", "comparación de un dato con una regla para confirmar si es confiable")],
    worked=[
        ("Calcular la profundidad", "Una cámara de ejemplo tiene el terreno a 480 cm y el fondo a 410 cm. ¿Qué profundidad tiene?", ["Se resta la cota del fondo a la del terreno.", "480 menos 410 son 70 cm."], "70 cm"),
        ("Verificar un P.R.", "Dos lecturas de un P.R. de ejemplo dieron 600 cm y 602 cm, con tolerancia de 1 cm. ¿Se acepta?", ["La diferencia es 2 cm.", "2 cm es mayor que la tolerancia de 1 cm: no se acepta."], "No se acepta"),
    ],
    mistakes=[("Pensar que una cámara poco profunda no tiene riesgo de espacio confinado.", "También puede acumular gases y es de acceso difícil.", "Trata toda cámara como tarea de personal autorizado."),
              ("Usar un P.R. dudoso «porque ya estamos atrasados».", "El error se traspasa a todo el trazado.", "Informa y espera la revisión de personal autorizado.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es un espacio confinado?", "Un recinto cerrado o de acceso difícil donde puede faltar aire respirable o haber gases", "Una oficina pequeña de la obra", "Una bodega con mucha luz", "Un espacio confinado es peligroso por el aire y el acceso, no por su tamaño."),
        ("abc", "En Instalaciones Sanitarias: ¿cómo se calcula la profundidad de una cámara?", "Cota del terreno menos cota del fondo", "Cota del fondo menos cota del terreno", "Cota del terreno más cota del fondo", "La profundidad es cuánto está el fondo por debajo del terreno."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es verificar un dato?", "Compararlo con una regla para confirmar si es confiable", "Copiarlo a otra hoja", "Aumentarlo para tener margen", "La verificación pone el dato a prueba contra un criterio."),
        ("=", "{F} ¿Qué profundidad tiene la cámara C1?", "500-446", "Se resta la cota del fondo a la del terreno.", " cm"),
        ("=", "{F} ¿Qué profundidad tiene la cámara C2?", "497-426", "Se resta la cota del fondo a la del terreno.", " cm"),
        ("=", "{F} ¿Qué profundidad tiene la cámara C3?", "495-340", "Se resta la cota del fondo a la del terreno.", " cm"),
        ("abc", "{F} ¿Qué cámara supera el criterio de ejemplo de 150 cm?", "La cámara C3", "La cámara C1", "La cámara C2", "C3 tiene 155 cm de profundidad; C1 tiene 54 cm y C2 tiene 71 cm."),
        ("abc", "{F} ¿Qué corresponde para una cámara que supera el criterio?", "Que solo personal autorizado entre, con un plan especial de seguridad", "Que entre un estudiante con un compañero", "Que se entre sin plan si es por poco tiempo", "Los espacios confinados profundos son de alto riesgo y se manejan con plan especial."),
        ("=", "{F} ¿Cuántos centímetros de diferencia hay entre las dos lecturas del P.R.?", "503-500", "Se resta la primera lectura a la segunda.", " cm"),
        ("abc", "{F} ¿Se acepta el P.R. con esas lecturas y la tolerancia de 1 cm?", "No, porque la diferencia es de 3 cm y supera la tolerancia", "Sí, porque la diferencia es pequeña", "Sí, porque 500 es una cota exacta", "La diferencia supera la tolerancia, por lo que no se usa hasta revisarlo."),
        ("abc", "{F} Alguien propone usar de todos modos el P.R. «porque 3 cm no se nota». ¿Qué respuesta es correcta?", "No: un error en la base se traspasa a todo el trazado", "Sí: 3 cm es siempre despreciable", "Sí, pero solo en cámaras poco profundas", "Un P.R. dudoso afecta todas las cotas medidas desde él."),
        ("=", "{F} ¿Cuántos centímetros excede la profundidad de C3 sobre el criterio de ejemplo?", "(495-340)-150", "Se calcula la profundidad de C3 y se le resta el límite de 150 cm.", " cm"),
        ("abc", "Una compañera de ejemplo dice que «la cámara C1 es poco profunda, así que puedo entrar a mirar». ¿Qué respondes?", "Que no: entrar a una cámara es tarea de personal autorizado, sin importar la profundidad", "Que sí, porque no supera el criterio", "Que sí, si lleva una linterna", "El criterio señala dónde se exige un plan especial, pero ningún estudiante entra a una cámara."),
    ],
    ctx=("abc", "Durante una visita de ejemplo, ves a un trabajador inmóvil dentro de una cámara abierta. ¿Qué haces?", "No entras, avisas de inmediato a un adulto responsable y a emergencias", "Bajas rápido a ayudarlo", "Esperas a que se levante", "Entrar puede causar una segunda víctima por falta de aire; se avisa a quienes pueden rescatar."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué es la profundidad de una cámara?", "Cota del terreno menos cota del fondo", "Mide cuánto está el fondo por debajo del terreno."),
        ("¿Quién puede entrar a una cámara?", "Solo personal autorizado, con plan especial", "Entrar a una cámara es de riesgo alto: el estudiante nunca entra."),
        ("¿Qué se hace con un P.R. cuyas lecturas no coinciden?", "No se usa hasta que personal autorizado lo revise", "Su error se traspasaría a todo el trazado."),
    ],
    op=("Ficha de ejemplo (cotas en cm; criterio de ejemplo de 120 cm). Cámara H1: terreno 520, fondo 440. Cámara H2: terreno 515, fondo 380. Dos lecturas de un P.R.: 700 y 701, con tolerancia de 1 cm. Escribe (a) la profundidad de H1 y de H2, (b) cuál supera el criterio, (c) si se acepta el P.R., (d) qué haría un estudiante frente a la cámara que supera el criterio.",
        "(a) H1: 520 − 440 = 80 cm; H2: 515 − 380 = 135 cm. (b) H2 supera los 120 cm. (c) Se acepta: la diferencia es de 1 cm, igual a la tolerancia. (d) No entraría: avisaría que esa cámara exige personal autorizado y un plan especial de seguridad.",
        ["calcula las dos profundidades", "identifica la cámara que supera el criterio", "decide sobre el P.R.", "no propone entrar a la cámara"],
        ["hoja con los cálculos, la decisión y la regla de seguridad"],
        ["restar al revés", "rechazar el P.R. que cumple la tolerancia", "proponer entrar a la cámara"],
        "Pregunta: «¿qué haces si una cámara no supera el criterio?». Si no responde, pídele que relea la regla de que ningún estudiante entra."),
    reinforce="Calcula en papel la profundidad de tres cámaras de ejemplo con terreno a 500 cm y fondos a 450, 400 y 340 cm, y marca las que superan 150 cm.",
    extend="Explica con un ejemplo por qué se verifica un P.R. antes de usar sus cotas.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 5 (alternativas de ejemplo, inventadas). Trazado A: 18 m de largo, 2 curvas, cruza 1 línea enterrada existente, desnivel disponible 40 cm. "
     "Trazado B: 24 m de largo, 4 curvas, sin cruces, desnivel disponible 54 cm. Pendiente de ejemplo exigida: 2 % (el desnivel necesario en cm es la longitud en metros por 2). "
     "Puntajes de ejemplo de 1 a 3 (3 es lo mejor) y pesos: costo (peso 2), riesgo por cruces (peso 3), mantención futura (peso 1). "
     "A: costo 3, riesgo 1, mantención 3. B: costo 2, riesgo 3, mantención 2.")
build(
    O3, 5, F,
    use="Aprenderé a comparar dos trazados con una matriz de puntajes, a comprobar que cumplan el desnivel y a verificar la calidad con una lista de control.",
    prior=["Sé calcular el desnivel con la pendiente.", "Sé multiplicar y sumar.", "Sé qué es una interferencia."],
    explain=[
        "Comparar alternativas es elegir con criterios claros, no por costumbre. Cada alternativa debe cumplir primero lo obligatorio: aquí, que el desnivel disponible alcance para la pendiente exigida. Después se comparan los criterios con una matriz: a cada criterio se le asigna un peso (su importancia) y a cada alternativa un puntaje. El resultado de la alternativa es la suma de peso por puntaje.",
        "Un criterio de seguridad, como evitar cruces con redes enterradas, suele tener más peso que el costo. La matriz ayuda a decidir, pero la decisión final la toman el proyectista y el ITO con la norma vigente, y la dejan por escrito. Para verificar la calidad se usa una lista de control: una pauta de puntos a revisar, cada uno con la respuesta «cumple» o «no cumple» y una observación.",
        f"Los puntajes y los pesos de esta ficha son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("alternativa", "una de las opciones posibles para resolver un problema"), ("peso", "importancia asignada a un criterio"), ("matriz de decisión", "tabla que combina pesos y puntajes para comparar alternativas"), ("lista de control", "pauta de puntos a revisar con la respuesta «cumple» o «no cumple»"), ("criterio obligatorio", "condición que una alternativa debe cumplir para poder ser considerada")],
    worked=[
        ("Puntaje de una alternativa", "Una alternativa de ejemplo tiene costo 2 (peso 3) y riesgo 3 (peso 2). ¿Qué puntaje total obtiene?", ["Se multiplica cada puntaje por su peso: 2 por 3 y 3 por 2.", "6 más 6 son 12."], "12 puntos"),
        ("Porcentaje de cumplimiento", "Una lista de control de ejemplo tiene 5 puntos y cumplen 4. ¿Qué porcentaje cumple?", ["Se divide lo que cumple entre el total: 4 de 5.", "4 por 100 dividido en 5 son 80 %."], "80 %"),
    ],
    mistakes=[("Elegir la alternativa más barata sin comprobar el desnivel exigido.", "Una alternativa que no cumple lo obligatorio no sirve, aunque cueste menos.", "Primero verifica los criterios obligatorios y luego compara."),
              ("Dar el mismo peso al costo y a la seguridad.", "Un riesgo de golpear una red enterrada puede ser más grave que un costo mayor.", "Asigna más peso a los criterios de seguridad.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es un criterio obligatorio al comparar trazados?", "Una condición que la alternativa debe cumplir para ser considerada", "Un puntaje de 3 en el costo", "El nombre del proyectista", "Si no se cumple el criterio obligatorio, la alternativa se descarta."),
        ("abc", "En Instalaciones Sanitarias: ¿para qué sirve el peso en una matriz de decisión?", "Para indicar la importancia de cada criterio", "Para medir cuánto pesa la tubería", "Para fijar el precio de venta", "El peso hace que los criterios importantes cuenten más."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es una lista de control?", "Una pauta de puntos a revisar con la respuesta «cumple» o «no cumple»", "Una lista de proveedores", "Un registro de asistencia", "La lista de control ordena la revisión de la calidad."),
        ("=", "{F} ¿Cuántos centímetros de desnivel necesita el trazado A?", "18*2", "Se multiplica la longitud en metros por el porcentaje exigido.", " cm"),
        ("=", "{F} ¿Cuántos centímetros de desnivel necesita el trazado B?", "24*2", "Se multiplica la longitud en metros por el porcentaje exigido.", " cm"),
        ("abc", "{F} ¿Qué trazados cumplen el criterio obligatorio del desnivel?", "Ambos, porque A necesita 36 cm y tiene 40, y B necesita 48 cm y tiene 54", "Solo A", "Solo B", "A tiene 4 cm de sobra y B tiene 6 cm de sobra."),
        ("=", "{F} ¿Qué puntaje total obtiene el trazado A?", "2*3+3*1+1*3", "Se suma cada peso por su puntaje: costo, riesgo y mantención.", " puntos"),
        ("=", "{F} ¿Qué puntaje total obtiene el trazado B?", "2*2+3*3+1*2", "Se suma cada peso por su puntaje: costo, riesgo y mantención.", " puntos"),
        ("abc", "{F} Según la matriz, ¿cuál es la mejor alternativa?", "El trazado B, con 15 puntos frente a 12", "El trazado A, con 12 puntos frente a 15", "Ninguna, porque empatan", "B suma 15 y A suma 12 puntos."),
        ("abc", "{F} ¿Por qué el trazado B gana pese a ser más largo y costoso?", "Porque el criterio de riesgo por cruces tiene el mayor peso y B no cruza redes", "Porque 24 m es mejor que 18 m", "Porque el costo no se considera en la matriz", "El mayor peso está en el riesgo, y B lo evita."),
        ("abc", "{F} Un compañero dice que, con la matriz, la decisión ya está tomada y no hace falta consultar. ¿Qué respuesta es correcta?", "No: la decisión final la toman el proyectista y el ITO, con la norma vigente", "Sí: la matriz reemplaza a los profesionales", "Sí, si los puntajes son de 1 a 3", "La matriz ayuda, pero no reemplaza la decisión profesional."),
        ("=", "Una lista de control de ejemplo tiene 8 puntos y cumplen 6. ¿Qué porcentaje cumple?", "6*100//8", "Se divide lo que cumple entre el total y se pasa a porcentaje.", " %"),
        ("abc", "¿Cuál es el mejor registro de la comparación de los trazados?", "Criterios obligatorios cumplidos, puntajes por criterio, total por alternativa y quién decide", "Se eligió B porque sí", "Ambos trazados son buenos", "Un registro completo permite revisar y repetir la decisión."),
    ],
    ctx=("abc", "El jefe de obra de ejemplo dice: «elijamos el trazado A porque es más corto y barato». ¿Qué propones?", "Revisar el riesgo del cruce con la línea enterrada y dejar que decidan el proyectista y el ITO con la matriz", "Aceptar, porque el jefe siempre tiene razón", "Elegir A y no avisar del cruce", "El cruce con una red enterrada es un riesgo que debe pesar en la decisión."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué se verifica primero al comparar alternativas?", "Los criterios obligatorios", "Una alternativa que no los cumple no sirve."),
        ("¿Cómo se obtiene el total de una alternativa en la matriz?", "Sumando peso por puntaje de cada criterio", "Cada criterio aporta según su importancia."),
        ("¿Quién toma la decisión final de un trazado?", "El proyectista y el ITO, con la norma vigente", "La matriz solo ayuda a decidir."),
    ],
    op=("Ficha de ejemplo: trazado X de 15 m con desnivel disponible de 36 cm y puntajes (de 1 a 3) costo 3, riesgo 2, mantención 2; trazado Y de 20 m con desnivel disponible de 38 cm y puntajes costo 2, riesgo 3, mantención 3. Pendiente exigida de ejemplo: 2 %. Pesos: costo 2, riesgo 3, mantención 1. Escribe (a) el desnivel que necesita cada trazado y si cumple, (b) el puntaje de cada uno, (c) cuál conviene con la matriz y quién decide.",
        "(a) X necesita 15 × 2 = 30 cm y tiene 36: cumple. Y necesita 20 × 2 = 40 cm y tiene 38: no cumple, queda descartado. (b) X: 2 × 3 + 3 × 2 + 1 × 2 = 14. Y: 2 × 2 + 3 × 3 + 1 × 3 = 16, pero no cumple lo obligatorio. (c) Conviene X, porque Y no cumple el desnivel; la decisión final la toman el proyectista y el ITO.",
        ["calcula el desnivel necesario de ambos", "descarta Y por no cumplir lo obligatorio", "calcula los puntajes", "indica quién decide"],
        ["hoja con la comparación completa"],
        ["elegir Y por su puntaje sin revisar el desnivel", "calcular mal el puntaje", "olvidar quién decide"],
        "Pregunta: «¿qué pasa con una alternativa que no cumple el criterio obligatorio, aunque gane en puntaje?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa dos alternativas de trazado con puntajes de 1 a 3 en tres criterios y calcula su total con los pesos que elijas.",
    extend="Explica con un ejemplo por qué la seguridad suele tener más peso que el costo en una matriz de decisión.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La empresa ficticia «Gas Hogar Sur» recibe documentos de un proyecto de gas de ejemplo para un edificio de 4 pisos, con 2 departamentos por piso. "
     "Cada departamento tiene una cocina y un calentador de agua a gas. Documentos recibidos: plano de la red, especificaciones y lista de artefactos. Documento pendiente: certificado del instalador autorizado. "
     "Riesgos anotados: fuga, incendio, explosión, intoxicación por monóxido de carbono y asfixia.")
build(
    O4, 1, F,
    use="Aprenderé qué tipos de gas existen, por qué el gas es un trabajo de riesgo alto, qué institución lo fiscaliza y qué hacer (y no hacer) ante una sospecha de fuga.",
    prior=["Sé qué es una red sanitaria.", "Sé leer una ficha con documentos.", "Sé que algunas tareas solo las hace personal autorizado."],
    explain=[
        "El gas combustible llega a una vivienda de dos maneras. El gas licuado se entrega almacenado en cilindros o estanques. El gas natural y el gas de ciudad llegan por una red de tuberías. Una red interior de baja presión es la que distribuye el gas dentro de un edificio a una presión mucho menor que la de las redes de distribución; sus valores los fija la norma vigente y no se tratan en este cuaderno. Al gas se le agrega normalmente un olor característico, para que una fuga se note.",
        "Los riesgos son graves. Una fuga puede producir incendio o explosión. Un artefacto que quema mal el combustible, por falta de aire o de salida de gases, produce monóxido de carbono: un gas sin color ni olor que causa intoxicación y puede ser mortal. En Chile, la Superintendencia de Electricidad y Combustibles (SEC) fiscaliza la seguridad de las instalaciones y artefactos de gas, y solo un instalador autorizado puede intervenirlas y certificarlas. Un estudiante nunca arma, abre, prueba ni conecta nada de gas.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("gas licuado", "gas que se entrega almacenado en cilindros o estanques"), ("gas natural y gas de ciudad", "gases que llegan a las viviendas por una red de tuberías"), ("red interior de baja presión", "red que distribuye el gas dentro de un edificio a una presión baja"), ("monóxido de carbono", "gas sin color ni olor que se produce cuando un artefacto quema mal el combustible"), ("SEC", "Superintendencia de Electricidad y Combustibles, que fiscaliza el gas"), ("instalador autorizado", "persona habilitada por la entidad fiscalizadora para intervenir y certificar instalaciones de gas")],
    worked=[
        ("Clasificar el suministro", "Una casa de ejemplo recibe el gas en cilindros que se reponen cuando se acaban. ¿Qué tipo de gas es?", ["El gas que se entrega en cilindros se llama licuado.", "Los gases por red son el natural y el de ciudad."], "Gas licuado"),
        ("Contar artefactos", "Un edificio de ejemplo tiene 5 departamentos con 3 artefactos de gas cada uno. ¿Cuántos artefactos hay?", ["Se multiplican los departamentos por los artefactos.", "5 por 3 son 15."], "15 artefactos"),
    ],
    mistakes=[("Revisar una sospecha de fuga con una llama «para ver si sale».", "Una llama puede provocar un incendio o una explosión.", "No entres ni acciones nada: avisa a un adulto responsable y a emergencias."),
              ("Creer que un artefacto «funciona bien» si enciende.", "Puede estar quemando mal y producir monóxido de carbono, que no se ve ni se huele.", "La revisión la hace un instalador autorizado con la norma vigente.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es el gas licuado?", "Un gas que se entrega almacenado en cilindros o estanques", "Un gas que llega por una tubería de la calle", "Un gas que se produce dentro de la casa", "El gas licuado se almacena y se repone; el natural y el de ciudad llegan por red."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es el monóxido de carbono?", "Un gas sin color ni olor que se produce cuando un artefacto quema mal el combustible", "Un gas que se agrega al combustible para que huela", "El vapor de agua de la ducha", "El monóxido de carbono no se ve ni se huele y puede causar intoxicación grave."),
        ("abc", "¿Qué institución fiscaliza la seguridad de las instalaciones y artefactos de gas en Chile?", "La Superintendencia de Electricidad y Combustibles (SEC)", "El Servicio de Impuestos Internos", "La Dirección del Trabajo", "La SEC es la entidad fiscalizadora del gas; las otras tienen funciones tributarias y laborales."),
        ("=", "{F} ¿Cuántos artefactos de gas hay en total en el edificio de la ficha?", "4*2*2", "Se multiplican los pisos por los departamentos de cada piso y por los dos artefactos de cada uno.", " artefactos"),
        ("abc", "{F} ¿Qué documento falta en la carpeta de la ficha?", "El certificado del instalador autorizado", "El plano de la red", "La lista de artefactos", "La ficha dice que el certificado está pendiente; los otros ya se recibieron."),
        ("abc", "{F} ¿Qué riesgo está asociado a un artefacto que quema mal el combustible en un recinto sin buena ventilación?", "Intoxicación por monóxido de carbono", "Corte del suministro de agua", "Ruido en las tuberías", "La mala combustión produce monóxido de carbono, un gas tóxico."),
        ("=", "{F} Cada uno de los artefactos de la ficha trae un manual de 10 páginas. Si se imprime una copia de cada manual, ¿cuántas páginas son?", "4*2*2*10", "Se multiplican los 16 artefactos por las 10 páginas de cada manual.", " páginas"),
        ("abc", "Una persona de ejemplo percibe olor a gas en un pasillo cerrado. ¿Qué corresponde según las reglas generales?", "No entrar ni accionar interruptores o llamas, avisar a un adulto responsable y a emergencias", "Entrar rápido a abrir las ventanas y a buscar el origen del olor", "Ventilar a oscuras y quedarse a esperar dentro", "Una chispa o una llama puede encender una fuga; se avisa a quienes pueden intervenir."),
        ("ab", "Un vecino de ejemplo te pide que le muestres cómo cambiar el cilindro de gas de su cocina. ¿Qué corresponde?", "No intervenir: avisar a la empresa proveedora o a un instalador autorizado", "Hacerlo rápido, porque ya estudiaste sanitarias", "Intervenir gas sin autorización es de riesgo alto; este cuaderno no habilita para hacerlo."),
        ("abc", "¿Por qué es parte de la seguridad que los artefactos tengan buena ventilación y salida de gases?", "Porque necesitan aire para quemar bien y los gases de la combustión deben salir", "Porque así gastan más gas", "Porque la ventilación enfría el gas licuado", "Sin aire ni salida de gases se acumula monóxido de carbono."),
        ("abc", "{F} Un compañero dice: «como el certificado está pendiente, igual se puede usar la red mientras tanto». ¿Qué respuesta es correcta?", "No: sin certificado de un instalador autorizado no se pone la red en servicio, y se informa", "Sí: los certificados son un trámite", "Sí, si se usa solo la cocina", "El certificado respalda que la instalación es segura; sin él no se usa."),
        ("=", "{F} Entre los 16 artefactos, 13 tienen su manual en la carpeta. ¿Cuántos manuales faltan?", "16-13", "Se resta lo que hay al total de artefactos.", " manuales"),
        ("abc", "¿Cuál de estas tareas puede realizar un estudiante de la especialidad sin autorización?", "Leer la lista de artefactos de gas de un proyecto", "Abrir y revisar un calentador de gas de una casa", "Cambiar un artefacto de gas en una casa", "Leer documentos no interviene la instalación; las otras tareas son de personal autorizado."),
    ],
    ctx=("abc", "Un familiar de ejemplo dice: «el calentador de agua de la casa huele raro; ábrelo y míralo, que tú sabes de gas». ¿Qué respondes?", "Que no lo abrirás y que llame a un instalador autorizado; si hay olor a gas, que salgan del lugar y avisen a emergencias", "Que lo abres, pero con cuidado", "Que esperas a ver si el olor aumenta antes de avisar", "Abrir un artefacto de gas sin autorización es de riesgo alto, aunque se tenga formación."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué gases llegan por una red de tuberías?", "El gas natural y el gas de ciudad", "El gas licuado, en cambio, se entrega en cilindros o estanques."),
        ("¿Qué institución fiscaliza la seguridad del gas?", "La SEC", "La Superintendencia de Electricidad y Combustibles fiscaliza gas y electricidad."),
        ("¿Qué hace un estudiante ante olor a gas?", "No entra ni acciona nada y avisa a un adulto y a emergencias", "Una chispa podría provocar un incendio o una explosión."),
    ],
    op=("Ficha de ejemplo: edificio de 3 pisos con 2 departamentos por piso; cada departamento tiene una cocina y un calentador de agua a gas. Documentos recibidos: plano y lista de artefactos; pendientes: especificaciones y certificado del instalador autorizado. Escribe (a) cuántos artefactos de gas hay, (b) cuántos documentos faltan, (c) el riesgo de un artefacto que quema mal el combustible, (d) qué harías ante olor a gas.",
        "(a) 3 × 2 × 2 = 12 artefactos. (b) Faltan 2: las especificaciones y el certificado. (c) Intoxicación por monóxido de carbono. (d) No entrar ni accionar interruptores o llamas, avisar a un adulto responsable y a emergencias.",
        ["calcula los artefactos", "cuenta los documentos faltantes", "nombra el riesgo del monóxido de carbono", "describe la conducta correcta ante olor a gas"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar mal", "proponer comprobar la fuga con una llama", "no avisar a emergencias"],
        "Pregunta: «¿por qué no se debe accionar un interruptor ante una fuga?». Si no responde, pídele que relea la regla de qué hacer ante olor a gas."),
    reinforce="Escribe una lista de cuatro riesgos del gas combustible y, junto a cada uno, la conducta general de prevención.",
    extend="Explica con un ejemplo por qué la sensación de que un artefacto «funciona bien» no demuestra que sea seguro.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (departamento de ejemplo, inventado). Artefactos y potencias de ejemplo: cocina, 8 kW; calentador de agua, 24 kW; estufa, 4 kW. La capacidad de ejemplo del medidor es de 40 kW. "
     "El plano indica un regulador a la entrada de la red, una válvula de corte por departamento y un conducto de evacuación de gases por cada calentador. Regla de planilla: la suma de las potencias no debe superar la capacidad del medidor.")
build(
    O4, 2, F,
    use="Aprenderé el vocabulario de una red de gas, cómo se suma la potencia de los artefactos en una planilla y qué documentos y roles intervienen.",
    prior=["Sé sumar y restar.", "Sé que el gas es de riesgo alto.", "Sé qué es una lista de artefactos."],
    explain=[
        "La potencia es la cantidad de energía por unidad de tiempo que usa un artefacto; en gas se expresa en kilowatts (kW). Para dimensionar una red se suman las potencias de los artefactos y se compara con la capacidad del medidor, que es el equipo que mide el gas consumido. El regulador es la pieza que controla y estabiliza la presión del gas. La válvula de corte es la pieza que permite interrumpir el paso del gas; su operación en una red la hacen personas autorizadas. La ventilación asegura la entrada de aire, y el conducto de evacuación saca de forma segura los gases de la combustión.",
        "Los documentos básicos son el plano de la red, las especificaciones, la lista de artefactos, los manuales de los fabricantes y el certificado emitido por el instalador autorizado. El proyectista diseña, el instalador autorizado ejecuta y certifica, la SEC fiscaliza y el usuario usa los artefactos sin intervenir la red.",
        f"Los kW de esta ficha son de ejemplo para practicar la suma en una planilla. {EMER} {AVISO}",
    ],
    vocab=[("potencia", "cantidad de energía por unidad de tiempo que usa un artefacto, en kilowatts (kW)"), ("medidor", "equipo que mide el gas consumido"), ("regulador", "pieza que controla y estabiliza la presión del gas"), ("válvula de corte", "pieza que permite interrumpir el paso del gas"), ("ventilación", "entrada de aire necesaria para la combustión y para renovar el aire del recinto"), ("conducto de evacuación", "ducto que saca los gases de la combustión"), ("certificado", "documento del instalador autorizado que respalda la instalación")],
    worked=[
        ("Sumar potencias", "En un departamento de ejemplo hay una cocina de 7 kW y un calentador de 20 kW. ¿Cuántos kW suman?", ["Se suman las dos potencias.", "7 más 20 son 27."], "27 kW"),
        ("Comparar con la capacidad", "El medidor de ejemplo de otra vivienda admite 30 kW y los artefactos suman 27 kW. ¿Cumple?", ["La suma debe ser menor o igual que la capacidad.", "27 es menor que 30: cumple."], "Sí, cumple con 3 kW de margen"),
    ],
    mistakes=[("Sumar las potencias de solo algunos artefactos y dejar fuera la estufa.", "La suma incompleta subestima lo que debe soportar la red.", "Suma todos los artefactos de la lista."),
              ("Creer que el usuario puede abrir el regulador o la válvula de corte para «arreglar» algo.", "Esas piezas se intervienen solo por personal autorizado.", "Avisa a un instalador autorizado y deja la red como está.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es la potencia de un artefacto de gas?", "La energía por unidad de tiempo que usa, en kilowatts", "El largo de su tubería de conexión", "El precio de su cilindro", "La potencia mide cuánta energía usa el artefacto por unidad de tiempo."),
        ("abc", "En Instalaciones Sanitarias: ¿para qué sirve el regulador de una red de gas?", "Para controlar y estabilizar la presión del gas", "Para medir cuántos artefactos hay", "Para agregar olor al gas", "El regulador mantiene la presión controlada."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es el conducto de evacuación de gases?", "El ducto que saca de forma segura los gases de la combustión", "La tubería que lleva el gas al artefacto", "El cable que lleva electricidad al artefacto", "El conducto de evacuación saca los gases producidos al quemar el combustible."),
        ("=", "{F} ¿Cuántos kW suman la cocina, el calentador y la estufa de la ficha?", "8+24+4", "Se suman las potencias de los tres artefactos.", " kW"),
        ("=", "{F} ¿Cuántos kW de margen quedan respecto de la capacidad del medidor?", "40-(8+24+4)", "Se resta la potencia total a la capacidad de 40 kW.", " kW"),
        ("abc", "{F} ¿Qué artefacto de la ficha tiene la mayor potencia?", "El calentador de agua", "La cocina", "La estufa", "El calentador tiene 24 kW, más que la cocina y la estufa."),
        ("abc", "{F} ¿Cuántos conductos de evacuación de gases indica el plano para este departamento?", "Uno, porque tiene un calentador", "Tres, porque hay tres artefactos", "Ninguno", "El plano indica un conducto por cada calentador, y el departamento tiene uno."),
        ("=", "{F} Si se agrega una segunda estufa de 4 kW, ¿cuántos kW suman los artefactos?", "8+24+4+4", "Se suma la potencia de la estufa adicional a la suma anterior.", " kW"),
        ("abc", "{F} Con la segunda estufa, ¿se cumple la regla de planilla?", "Sí, porque la suma es igual a la capacidad y no la supera", "No, porque la suma supera la capacidad", "No se puede saber sin otro medidor", "La regla dice que la suma no debe superar la capacidad; 40 kW no supera 40 kW."),
        ("abc", "{F} Con una tercera estufa de 4 kW, la suma sería de 44 kW. ¿Quién decide qué hacer?", "El proyectista con el instalador autorizado, no el usuario", "El usuario, comprando un cilindro más grande", "Cualquier vecino con experiencia", "Cambiar potencias o equipos es una decisión de diseño que corresponde a personal autorizado."),
        ("abc", "Un dueño de ejemplo dice: «mi cuñado cambió el calentador de agua sin avisar y funciona». ¿Qué problema puede haber?", "Puede no tener ventilación ni certificado adecuados, con riesgo de monóxido de carbono; debe revisarlo un instalador autorizado", "Ninguno, si enciende está bien", "Solo que el cuñado cobró de más", "Un artefacto que enciende puede quemar mal y no estar certificado."),
        ("=", "Un edificio de ejemplo tiene 6 departamentos y cada uno suma 36 kW de artefactos. ¿Cuántos kW suman entre todos?", "6*36", "Se multiplica la potencia de un departamento por la cantidad de departamentos.", " kW"),
        ("abc", "¿Cuál es el papel del usuario respecto de la red de gas de su vivienda?", "Usar los artefactos sin intervenir la red", "Modificar la red si tiene herramientas", "Certificar la instalación", "El usuario usa los artefactos; la red la interviene y certifica un instalador autorizado."),
    ],
    ctx=("abc", "En la reunión de copropietarios de ejemplo alguien propone que «un vecino que sabe de gas» cambie una válvula del edificio para ahorrar. ¿Qué dices?", "Que solo un instalador autorizado puede intervenir la red, y que se debe contratar a uno", "Que adelante, si el vecino tiene herramientas", "Que se haga sin avisar para evitar discusiones", "La red de gas de un edificio es de riesgo alto y exige instalador autorizado."),
    sc=[
        ("En Instalaciones Sanitarias: ¿qué mide el medidor de gas?", "El gas consumido", "El medidor registra cuánto gas se usa."),
        ("¿Qué se suma para dimensionar una red de gas en la planilla de ejemplo?", "Las potencias de los artefactos", "Esa suma se compara con la capacidad del medidor."),
        ("¿Quién interviene y certifica la red de gas?", "Un instalador autorizado", "La norma vigente exige personal habilitado para el gas."),
    ],
    op=("Ficha de ejemplo: un departamento tiene una cocina de 6 kW, un calentador de agua de 20 kW y una estufa de 5 kW; la capacidad del medidor de ejemplo es de 35 kW. Escribe (a) la suma de potencias, (b) si cumple la regla de planilla y con cuánto margen, (c) para qué sirve el conducto de evacuación, (d) quién interviene la red.",
        "(a) 6 + 20 + 5 = 31 kW. (b) Cumple: 31 no supera 35, con 4 kW de margen. (c) Para sacar de forma segura los gases de la combustión. (d) Un instalador autorizado, no el usuario.",
        ["suma bien las potencias", "compara con la capacidad y calcula el margen", "explica el conducto de evacuación", "indica quién interviene la red"],
        ["hoja con la suma, la comparación y las explicaciones"],
        ["olvidar un artefacto", "restar mal el margen", "decir que el usuario puede intervenir la red"],
        "Pregunta: «¿qué pasa si la suma supera la capacidad?». Si no responde, pídele que relea la regla de planilla."),
    reinforce="Inventa una lista de tres artefactos con sus potencias, suma y compáralos con una capacidad de ejemplo.",
    extend="Explica con un ejemplo por qué la suma de potencias es solo una parte del diseño de una red de gas.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (revisión documental de ejemplo, inventada). Documentos que el proyecto de ejemplo exige: 1 plano de la red (recibido); 2 especificaciones técnicas (recibidas); 3 lista de artefactos (recibida); "
     "4 manuales de los 3 artefactos (recibidos 2 de 3: falta el de la estufa); 5 plano de ventilación y evacuación (recibido); 6 certificado del instalador autorizado (pendiente); 7 plano de ubicación del medidor (recibido); 8 bitácora (recibida). "
     "Un documento cuenta como completo solo si está entero. Datos de potencia: la lista de artefactos dice calentador 24 kW; el manual del calentador dice 28 kW.")
build(
    O4, 3, F,
    use="Aprenderé a revisar una carpeta de documentos de un proyecto de gas, a detectar lo que falta o no coincide y a decidir qué se informa, sin intervenir la instalación.",
    prior=["Sé qué documentos tiene un proyecto de gas.", "Sé calcular un porcentaje.", "Sé que la puesta en servicio la hace personal autorizado."],
    explain=[
        "Una revisión documental compara los documentos que el proyecto exige con los que realmente llegaron. Se anota para cada uno si está completo, incompleto o pendiente. También se comparan los datos entre documentos: si la lista de artefactos y el manual del fabricante dan potencias distintas, hay una discrepancia, y no se supone cuál es la correcta.",
        "La puesta en servicio es el momento en que la instalación empieza a usarse. En el gas, solo la autoriza personal habilitado, y únicamente cuando la documentación está completa y respaldada por el certificado del instalador autorizado. Quien revisa los papeles no pone en servicio nada: registra, informa y espera. El informe de la revisión dice qué está completo, qué falta, qué no coincide y a quién se informó.",
        f"Esta revisión es un ejercicio de lectura: no incluye pruebas, conexiones ni mediciones en una instalación. {EMER} {AVISO}",
    ],
    vocab=[("revisión documental", "comparación entre los documentos exigidos y los recibidos"), ("completo", "documento que está entero"), ("pendiente", "documento que aún no se ha entregado"), ("discrepancia", "diferencia entre dos datos que deberían coincidir"), ("puesta en servicio", "momento en que una instalación empieza a usarse, autorizado por personal habilitado")],
    worked=[
        ("Clasificar un documento", "En un proyecto de ejemplo, el manual de un artefacto llegó con solo la mitad de las páginas. ¿Está completo?", ["Un documento cuenta como completo solo si está entero.", "Está incompleto."], "Incompleto"),
        ("Calcular una diferencia", "La lista de artefactos de ejemplo dice 10 kW y el manual dice 12 kW. ¿Cuántos kW difieren?", ["Se resta el menor del mayor.", "12 menos 10 son 2 kW."], "2 kW de diferencia"),
    ],
    mistakes=[("Dar por bueno el manual y cambiar la lista de artefactos cuando los kW no coinciden.", "No se sabe cuál dato es el correcto sin consultar.", "Registra la discrepancia e informa al proyectista y al instalador autorizado."),
              ("Pensar que, con casi todos los documentos, ya se puede poner en servicio.", "Falta el certificado y un manual; la autorización exige todo completo.", "Informa lo que falta y espera la decisión del personal habilitado.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es una revisión documental?", "Comparar los documentos exigidos con los recibidos", "Probar la instalación de gas con herramientas", "Medir los tramos de tubería en la obra", "La revisión documental trabaja con papeles, no con la instalación."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es la puesta en servicio de una instalación de gas?", "El momento en que empieza a usarse, autorizado por personal habilitado", "El día en que se compra el artefacto", "La limpieza final de la obra", "En gas, la puesta en servicio la autoriza personal habilitado."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es una discrepancia entre dos documentos?", "Una diferencia entre datos que deberían coincidir", "Un documento escrito a mano", "Un plano con muchas láminas", "Una discrepancia se registra y se consulta; no se resuelve suponiendo."),
        ("=", "{F} ¿Cuántos de los 8 documentos están completos? (Hay 1 incompleto y 1 pendiente.)", "8-1-1", "Se restan del total el documento incompleto y el pendiente.", " documentos"),
        ("abc", "{F} ¿Qué documento está incompleto?", "Los manuales, porque falta el de la estufa", "El plano de ubicación del medidor", "La bitácora", "Los manuales llegaron 2 de 3; el resto está entero."),
        ("abc", "{F} ¿Qué documento está pendiente?", "El certificado del instalador autorizado", "El plano de ventilación y evacuación", "La lista de artefactos", "La ficha marca el certificado como pendiente."),
        ("=", "{F} ¿Qué porcentaje de los documentos exigidos está completo?", "6*100//8", "Se divide lo completo entre el total y se pasa a porcentaje.", " %"),
        ("=", "{F} ¿Cuántos kW difieren la lista de artefactos y el manual para el calentador?", "28-24", "Se resta el valor menor al mayor.", " kW"),
        ("abc", "{F} ¿Qué corresponde hacer con la discrepancia de potencia del calentador?", "Registrarla e informar al proyectista y al instalador autorizado, sin suponer cuál es la correcta", "Usar el valor mayor y seguir", "Borrar el dato del manual", "No se sabe cuál es correcto; la consulta resuelve la duda."),
        ("abc", "{F} Con esta carpeta, ¿se puede poner la instalación en servicio?", "No: faltan un manual y el certificado, y hay una discrepancia por aclarar", "Sí: solo faltan detalles", "Sí, si se usa un artefacto a la vez", "La autorización exige documentación completa y el certificado."),
        ("abc", "{F} Un compañero dice: «yo puedo encender la cocina para comprobar que funciona». ¿Qué respuesta es correcta?", "No: poner en servicio y probar la instalación corresponde a personal habilitado", "Sí: encender una cocina no tiene riesgo", "Sí, si abre la ventana", "Probar una instalación sin certificado es de riesgo alto."),
        ("=", "Otra carpeta de ejemplo exige 10 documentos y llegaron 7 completos. ¿Cuántos faltan?", "10-7", "Se resta lo recibido completo al total exigido.", " documentos"),
        ("abc", "¿Cuál es el mejor informe de revisión documental?", "Documentos completos, incompletos y pendientes, discrepancias encontradas y a quién se informó", "La carpeta está más o menos bien", "Se recomienda poner en servicio ya", "Un buen informe es específico y deja constancia de a quién se informó."),
    ],
    ctx=("abc", "La administradora de un edificio de ejemplo te pregunta: «con 6 de 8 documentos, ¿ya podemos usar el gas?». ¿Qué respondes?", "Que no: faltan documentos y el certificado, y la puesta en servicio la autoriza personal habilitado", "Que sí, porque son más de la mitad", "Que sí, si el instalador promete traer lo que falta", "La seguridad del gas exige documentación y certificado completos antes de usar."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cuándo cuenta un documento como completo?", "Cuando está entero", "Un documento a medias se registra como incompleto."),
        ("¿Qué se hace con una discrepancia de datos?", "Se registra y se informa, sin suponer", "El dato correcto lo confirma quien diseñó o certifica."),
        ("¿Quién autoriza la puesta en servicio del gas?", "Personal habilitado", "No la autoriza quien solo revisa los papeles."),
    ],
    op=("Ficha de ejemplo: un proyecto exige 5 documentos: plano (recibido), especificaciones (recibidas), lista de artefactos (recibida), manuales (recibidos 1 de 2) y certificado del instalador autorizado (pendiente). La lista dice cocina 6 kW y el manual de la cocina dice 8 kW. Escribe (a) cuántos documentos están completos y qué porcentaje es, (b) cuáles faltan, (c) la diferencia de potencia, (d) si se puede poner en servicio y por qué.",
        "(a) 3 de 5 están completos: 60 %. (b) Faltan los manuales completos y el certificado. (c) 8 − 6 = 2 kW. (d) No: faltan documentos, hay una discrepancia y la puesta en servicio la autoriza personal habilitado.",
        ["cuenta los documentos completos y su porcentaje", "identifica lo que falta", "calcula la diferencia", "concluye con la razón correcta"],
        ["hoja con la revisión y la conclusión"],
        ["contar como completo el documento a medias", "suponer cuál dato es el correcto", "afirmar que se puede poner en servicio"],
        "Pregunta: «¿qué le dirías a quien quiere encender el artefacto igual?». Si no responde, pídele que relea el párrafo de puesta en servicio."),
    reinforce="Inventa una lista de seis documentos de un proyecto de gas y marca cuáles están completos, incompletos o pendientes.",
    extend="Explica con un ejemplo por qué no se debe suponer cuál de dos datos distintos es el correcto.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada). Edificio de 4 departamentos. Cada departamento tiene cocina (8 kW) y calentador de agua (24 kW). Capacidad de la red del edificio en esta planilla: 150 kW. "
     "Regla de planilla: la suma de las potencias no debe superar la capacidad (simplificación de ejemplo; el diseño real usa otros criterios de la norma vigente). "
     "Opción 1: solo cocina y calentador. Opción 2: cocina, calentador y 1 estufa de 4 kW por departamento. Opción 3: cocina, calentador y 2 estufas de 4 kW por departamento.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar un criterio técnico en papel: sumar potencias por opción, compararlas con la capacidad y decidir cuáles cumplen y quién toma la decisión.",
    prior=["Sé sumar potencias de artefactos.", "Sé multiplicar por la cantidad de departamentos.", "Sé comparar una suma con un límite."],
    explain=[
        "Aplicar un criterio técnico es comparar un dato calculado con una regla y decidir con evidencia. En esta planilla de ejemplo el dato es la potencia total de una opción y la regla es no superar la capacidad de la red. Se calcula la potencia por departamento, se multiplica por la cantidad de departamentos y se resta de la capacidad para obtener el margen. Si el margen es cero o positivo, la opción cumple; si es negativo, no cumple.",
        "Una opción que no cumple no se aprueba, y tampoco se arregla agregando artefactos a escondidas ni cambiando la capacidad en el papel. Se informa al proyectista, que puede rediseñar la red o limitar los artefactos. La decisión se deja por escrito, con la opción elegida, los cálculos y quién la aprobó.",
        f"La regla de este ejercicio es una simplificación de ejemplo y no reemplaza el diseño ni la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("potencia total", "suma de las potencias de todos los artefactos de una opción"), ("capacidad de la red", "potencia máxima que la red admite según su diseño"), ("margen", "diferencia entre la capacidad y la potencia total"), ("opción", "cada combinación posible de artefactos"), ("rediseño", "cambio del diseño hecho por el proyectista")],
    worked=[
        ("Potencia por departamento", "En un edificio de ejemplo cada departamento tiene artefactos de 6 kW y 18 kW. ¿Cuántos kW suma cada uno?", ["Se suman las dos potencias.", "6 más 18 son 24 kW."], "24 kW"),
        ("Aplicar la regla", "Un edificio de ejemplo con 3 departamentos de 24 kW cada uno tiene una red de 80 kW. ¿Cumple?", ["La potencia total es 3 por 24, es decir 72 kW.", "72 no supera 80: cumple, con 8 kW de margen."], "Sí, cumple con 8 kW de margen"),
    ],
    mistakes=[("Agregar artefactos a escondidas porque «ya hay otro con más potencia».", "Cada artefacto cuenta en la suma total.", "Informa y deja que decida el proyectista."),
              ("Cambiar la capacidad en la planilla para que la opción cumpla.", "La capacidad la fija el diseño de la red, no quien calcula.", "Mantén el dato y registra que la opción no cumple.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es la capacidad de la red en esta planilla?", "La potencia máxima que la red admite según su diseño", "La suma de todos los artefactos futuros", "El número de departamentos", "La capacidad es el límite de potencia que fija el diseño de la red."),
        ("abc", "En Instalaciones Sanitarias: ¿cómo se calcula el margen?", "Capacidad menos potencia total", "Potencia total menos capacidad", "Potencia total más capacidad", "El margen es lo que sobra de la capacidad después de sumar las potencias."),
        ("abc", "En Instalaciones Sanitarias: ¿qué se hace con una opción que no cumple la regla?", "Se informa al proyectista, que puede rediseñar o limitar los artefactos", "Se aprueba igual", "Se cambia la capacidad en la planilla", "Una opción que no cumple se resuelve con el diseño, no manipulando datos."),
        ("=", "{F} ¿Cuántos kW suma cada departamento en la opción 1?", "8+24", "Se suman la cocina y el calentador.", " kW"),
        ("=", "{F} ¿Cuántos kW suma el edificio completo en la opción 1?", "4*(8+24)", "Se multiplica la potencia de un departamento por los 4 departamentos.", " kW"),
        ("=", "{F} ¿Cuántos kW de margen queda en la opción 1?", "150-4*(8+24)", "Se resta la potencia total a la capacidad de 150 kW.", " kW"),
        ("=", "{F} ¿Cuántos kW suma el edificio en la opción 2?", "4*(8+24+4)", "Cada departamento suma cocina, calentador y una estufa, y se multiplica por 4.", " kW"),
        ("abc", "{F} ¿Cumple la opción 2 la regla de planilla?", "Sí, con 6 kW de margen", "No, porque supera la capacidad", "No se puede saber", "La opción 2 suma 144 kW, menos que 150 kW."),
        ("=", "{F} ¿Cuántos kW suma el edificio en la opción 3?", "4*(8+24+4+4)", "Cada departamento suma cocina, calentador y dos estufas, y se multiplica por 4.", " kW"),
        ("abc", "{F} ¿Cumple la opción 3 la regla de planilla?", "No, porque supera la capacidad en 10 kW", "Sí, con 10 kW de margen", "Sí, porque 160 está cerca de 150", "La opción 3 suma 160 kW y la capacidad es de 150 kW."),
        ("abc", "{F} Un propietario pide la opción 3 y propone subir la capacidad a 160 kW en la planilla. ¿Qué respuesta es correcta?", "No: la capacidad la fija el diseño de la red, y cualquier cambio lo decide el proyectista", "Sí: basta cambiar el número", "Sí, si el propietario firma", "Cambiar el dato sin rediseñar no cambia la red real."),
        ("=", "{F} ¿Cuántos kW debería reducir la opción 3 para igualar la capacidad?", "4*(8+24+4+4)-150", "Se resta la capacidad a la potencia total de la opción 3.", " kW"),
        ("abc", "¿Cuál es el mejor registro de la decisión?", "Opción elegida, cálculos de cada opción, margen y quién la aprobó", "Se eligió la opción 2", "La opción 1 se ve bien", "Un registro completo permite revisar la decisión."),
    ],
    ctx=("abc", "Una persona del comité de un edificio de ejemplo dice: «pongamos dos estufas por departamento y después vemos si la red aguanta». ¿Qué propones?", "Calcular antes la potencia total y consultar al proyectista; si no cumple, no se avanza", "Instalar primero y probar después", "Pedir a un vecino con herramientas que revise las tuberías por su cuenta", "La capacidad se verifica antes, en el diseño, no después de instalar."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cuándo cumple una opción la regla de planilla?", "Cuando la potencia total no supera la capacidad", "Un margen cero o positivo indica que cumple."),
        ("¿Quién puede rediseñar una red de gas?", "El proyectista", "Los cambios de diseño los decide quien proyecta."),
        ("¿Se puede cambiar la capacidad en la planilla para que cumpla?", "No, porque la capacidad la fija el diseño de la red", "Cambiar el número no cambia la red real."),
    ],
    op=("Ficha de ejemplo: edificio de 5 departamentos con cocina (7 kW) y calentador de agua (20 kW) cada uno; capacidad de la red de ejemplo: 150 kW. Opción A: solo cocina y calentador. Opción B: además 1 estufa de 5 kW por departamento. Escribe (a) la potencia total de cada opción, (b) el margen de cada una, (c) cuál cumple la regla, (d) qué harías si ninguna cumpliera.",
        "(a) A: 5 × (7 + 20) = 135 kW. B: 5 × (7 + 20 + 5) = 160 kW. (b) A: 15 kW de margen. B: −10 kW. (c) Cumple A; B supera la capacidad. (d) Informar al proyectista para rediseñar o limitar artefactos, sin cambiar la capacidad ni agregar artefactos a escondidas.",
        ["calcula las dos potencias totales", "calcula los márgenes", "decide cuál cumple", "propone informar al proyectista"],
        ["hoja con los cálculos y la decisión"],
        ["olvidar multiplicar por los departamentos", "restar al revés", "cambiar la capacidad"],
        "Pregunta: «¿qué margen tendría la opción B con solo 4 departamentos?». Si no responde, pídele que repita el cálculo con 4."),
    reinforce="Calcula en papel la potencia total de un edificio de 3 departamentos con artefactos de 6, 18 y 4 kW cada uno, y compárala con 100 kW.",
    extend="Explica con un ejemplo por qué una opción que no cumple no se aprueba con un cambio de números.",
)

# ============================================================ OAE-04, clase 5
F = ("Ficha 5 (alternativas y control de calidad de ejemplo, inventados). Casa de ejemplo. Alternativa 1: gas licuado en cilindros; costo de instalación $300.000; costo mensual de uso $24.000. "
     "Alternativa 2: gas por red; costo de conexión $450.000; costo mensual de uso $18.000. Horizonte de comparación: 24 meses. Todos los precios son de ejemplo. "
     "Condiciones no económicas: la red solo existe si la empresa distribuidora la tiene disponible en la zona; los cilindros requieren un espacio ventilado. "
     "Lista de control documental de ejemplo: 8 puntos, cumplen 6.")
build(
    O4, 5, F,
    use="Aprenderé a comparar dos formas de suministro de gas con costos y condiciones de seguridad, y a verificar la calidad documental con una lista de control, sin intervenir la instalación.",
    prior=["Sé calcular costos acumulados.", "Sé qué es gas licuado y gas por red.", "Sé calcular un porcentaje."],
    explain=[
        "Comparar alternativas de suministro incluye costos y condiciones. El costo total en un horizonte es el costo de instalación más el costo mensual multiplicado por los meses. También se evalúan condiciones que el dinero no resuelve: si la red está disponible en la zona, si hay un espacio ventilado para los cilindros y si el instalador autorizado puede certificar la solución. La seguridad no se negocia: cualquier alternativa de gas exige instalador autorizado, certificado y la norma vigente.",
        "Cuando la diferencia de costo entre alternativas es pequeña, decide la disponibilidad y la seguridad. La verificación de la calidad documental usa una lista de control: se cuenta qué puntos cumplen, se calcula el porcentaje y se listan los que no cumplen. Un punto que no cumple se informa y se corrige antes de cualquier uso.",
        f"Los costos de esta ficha son de ejemplo y no representan precios reales. {EMER} {AVISO}",
    ],
    vocab=[("horizonte de comparación", "cantidad de meses en que se comparan los costos"), ("costo total", "costo de instalación más el costo mensual por los meses del horizonte"), ("disponibilidad", "posibilidad real de contar con un servicio en un lugar"), ("espacio ventilado", "lugar con renovación de aire adecuada"), ("lista de control", "pauta de puntos a revisar con la respuesta «cumple» o «no cumple»")],
    worked=[
        ("Costo total", "Una alternativa de ejemplo cuesta $100.000 de instalación y $10.000 por mes. ¿Cuánto cuesta en 12 meses?", ["El uso en 12 meses cuesta 12 por 10.000, es decir 120.000.", "Se suma la instalación: 220.000."], "$220.000"),
        ("Diferencia", "Dos alternativas de ejemplo cuestan $500.000 y $540.000 en el horizonte. ¿Cuánto difieren?", ["Se resta el menor al mayor.", "540.000 menos 500.000 son 40.000."], "$40.000"),
    ],
    mistakes=[("Elegir solo por el costo total sin ver la disponibilidad ni la seguridad.", "Una opción barata puede no estar disponible o no poder certificarse.", "Revisa también las condiciones no económicas."),
              ("Dar un punto de la lista de control como cumplido «a ojo».", "Si no hay evidencia escrita, no se puede asegurar.", "Marca «cumple» solo con respaldo documental.")],
    T=[
        ("abc", "En Instalaciones Sanitarias: ¿qué es el costo total en un horizonte de comparación?", "El costo de instalación más el costo mensual por los meses", "Solo el costo mensual", "Solo el costo de instalación", "El costo total suma lo que se paga al instalar y lo que se paga mes a mes."),
        ("abc", "En Instalaciones Sanitarias: ¿qué es la disponibilidad de la red de gas en una zona?", "La posibilidad real de contar con ella en ese lugar", "El precio del gas por mes", "La cantidad de cilindros que caben", "Sin disponibilidad, la alternativa por red no es posible."),
        ("abc", "En Instalaciones Sanitarias: ¿para qué sirve una lista de control documental?", "Para revisar qué puntos cumplen y cuáles no", "Para ordenar los documentos por tamaño", "Para calcular el consumo mensual", "La lista ordena la verificación punto por punto."),
        ("=", "{F} ¿Cuánto cuesta el uso mensual del gas licuado durante los 24 meses?", "24*24000", "Se multiplican los meses por el costo mensual de la alternativa 1.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la alternativa 1 en 24 meses?", "300000+24*24000", "Se suma la instalación al costo de uso de 24 meses.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la alternativa 2 en 24 meses?", "450000+24*18000", "Se suma la conexión al costo de uso de 24 meses.", " pesos"),
        ("=", "{F} ¿Cuántos pesos difieren los costos totales de las dos alternativas?", "(450000+24*18000)-(300000+24*24000)", "Se resta el costo total menor al mayor.", " pesos"),
        ("abc", "{F} Dada la diferencia de costos, ¿qué debería decidir la elección?", "La disponibilidad de la red y las condiciones de seguridad, porque el costo es parecido", "Solo el costo, aunque la diferencia sea pequeña", "El color del cilindro", "Con costos parecidos, deciden la disponibilidad y la seguridad."),
        ("abc", "{F} Si la empresa distribuidora no tiene red en la zona, ¿qué ocurre con la alternativa 2?", "No es posible, aunque su costo mensual sea menor", "Se puede instalar igual con un cilindro más grande", "Se vuelve la más barata", "La disponibilidad es una condición para que la alternativa exista."),
        ("abc", "{F} Un familiar dice: «con cilindros no necesito instalador autorizado, es más simple». ¿Qué respuesta es correcta?", "Falso: cualquier alternativa de gas exige instalador autorizado, certificado y norma vigente", "Cierto: los cilindros no tienen riesgos", "Cierto si los cilindros son pequeños", "El gas licuado también es de riesgo alto."),
        ("=", "{F} ¿Qué porcentaje de los puntos de la lista de control cumple?", "6*100//8", "Se divide lo que cumple entre el total y se pasa a porcentaje.", " %"),
        ("abc", "{F} Dos puntos de la lista no cumplen. ¿Qué corresponde?", "Informarlos y corregirlos antes de cualquier uso, con respaldo documental", "Marcarlos como cumplidos para cerrar la lista", "Ignorarlos porque cumple el 75 %", "Un punto que no cumple se corrige antes de usar."),
        ("abc", "¿Cuál es el mejor registro de la comparación?", "Costos totales por alternativa, condiciones de disponibilidad y seguridad, y quién decide", "Se eligió la alternativa 2", "Las dos alternativas son parecidas", "Un registro completo permite revisar la decisión."),
    ],
    ctx=("abc", "Una familia de ejemplo te pide que le digas «cuál conviene» para su casa. ¿Qué respondes?", "Que muestres la comparación en papel y que consulten a un instalador autorizado y a la empresa distribuidora; este cuaderno no reemplaza esa asesoría", "Que elijan la más barata sin consultar", "Que instalen ellos mismos la que prefieran", "Una decisión real exige disponibilidad confirmada e instalador autorizado."),
    sc=[
        ("En Instalaciones Sanitarias: ¿cómo se calcula el costo total en un horizonte?", "Instalación más costo mensual por los meses", "Se suman el costo inicial y el uso acumulado."),
        ("¿Qué decide cuando los costos son parecidos?", "La disponibilidad y la seguridad", "El costo deja de ser decisivo si la diferencia es pequeña."),
        ("¿Quién debe intervenir cualquier instalación de gas?", "Un instalador autorizado", "Aplica tanto al gas por red como al gas licuado."),
    ],
    op=("Ficha de ejemplo: alternativa X: instalación $200.000 y $15.000 por mes; alternativa Y: instalación $350.000 y $10.000 por mes; horizonte de 36 meses. La alternativa Y requiere que la red esté disponible en la zona. Escribe (a) el costo total de cada alternativa, (b) la diferencia, (c) una condición no económica que decidiría si Y es posible, (d) por qué ambas necesitan instalador autorizado.",
        "(a) X: 200.000 + 36 × 15.000 = 740.000 pesos. Y: 350.000 + 36 × 10.000 = 710.000 pesos. (b) 30.000 pesos. (c) La disponibilidad de la red en la zona. (d) Porque cualquier instalación de gas es de riesgo alto y exige instalador autorizado, certificado y norma vigente.",
        ["calcula los dos costos totales", "calcula la diferencia", "nombra la condición no económica", "explica por qué se exige instalador autorizado"],
        ["hoja con los cálculos y las razones"],
        ["olvidar el costo de instalación", "decidir solo por costo", "decir que el gas licuado no necesita instalador autorizado"],
        "Pregunta: «¿qué pasaría si la red no estuviera disponible?». Si no responde, pídele que relea el párrafo de condiciones."),
    reinforce="Calcula en papel el costo total en 12 meses de una alternativa con instalación de $120.000 y $9.000 por mes.",
    extend="Explica con un ejemplo por qué una opción más barata puede no ser la mejor para una familia.",
)
