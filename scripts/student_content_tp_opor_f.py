"""Operaciones Portuarias TP 3.º y 4.º medio: OAE-06 (tramitación aduanera como lectura de documentos y cálculo de planilla; tasas y plazos de ejemplo). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_opor_common import AVISO, EMER, build

O6 = "TP-OPOR-3y4-OAE-06"

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Agencia Demo», una agencia de aduanas ficticia, tramita en un día: 5 importaciones, 3 exportaciones, 2 trámites de cabotaje, 1 redestinación y 1 tránsito. "
     "Plazo de ejemplo para presentar cada declaración: 3 días hábiles desde el arribo de la nave; pasado el plazo, el almacenaje cuesta $4.000 por contenedor por día (valor de ejemplo). "
     "Observaciones anotadas: un cliente pide declarar un valor menor al real «para pagar menos»; una persona debe llevar un documento al patio y pasa por el área de maniobras de vehículos de carga; y se comparten los datos de un cliente por un mensaje sin protección. El equipo es de 3 personas.")
build(
    O6, 1, F,
    use="Aprenderé qué es la tramitación aduanera, qué tipos de trámite existen, cuál es el rol del agente de aduanas y qué riesgos éticos, de información y físicos tiene este trabajo.",
    prior=["Sé qué son el conocimiento de embarque y la lista de embalaje.", "Sé sumar y multiplicar números enteros.", "Sé qué es el principio de cero faltas."],
    explain=[
        "La aduana es la autoridad que controla la entrada y la salida de mercancías de un país. La tramitación aduanera es el conjunto de trámites que se hacen ante ella. La importación es el ingreso de mercancías al país; la exportación es su salida; el cabotaje es el transporte de carga entre puertos del mismo país; la redestinación es el cambio del destino de una carga que ya llegó; y el tránsito es el paso de una mercancía por el país hacia otro destino. Se hacen por vía marítima, aérea o terrestre, según la norma vigente y los tratados internacionales.",
        "El agente de aduanas es el profesional autorizado que realiza los trámites por cuenta de un cliente, que le da un mandato, una autorización por escrito. La declaración aduanera es el documento donde se declara la mercancía, con su tipo, cantidad y valor. Debe ser veraz: declarar un valor falso es una infracción según la norma vigente, aunque el cliente lo pida. Los datos de los clientes son confidenciales y no se comparten sin protección. Si una persona debe ir al patio, no pasa por el área de maniobras de vehículos y usa las rutas peatonales.",
        f"Cada trámite tiene plazos, que se cuentan en días hábiles, es decir, los días en que funcionan las oficinas. Pasado el plazo, la carga paga almacenaje y pueden aplicarse sanciones según la norma vigente. Todos los plazos y valores de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("aduana", "autoridad que controla la entrada y la salida de mercancías del país"), ("importación y exportación", "ingreso de mercancías al país y salida de mercancías del país"), ("cabotaje", "transporte de carga entre puertos del mismo país"), ("redestinación", "cambio del destino de una carga que ya llegó"), ("tránsito", "paso de una mercancía por el país hacia otro destino"), ("agente de aduanas", "profesional autorizado que hace los trámites aduaneros por un cliente"), ("mandato", "autorización por escrito del cliente al agente"), ("declaración aduanera", "documento donde se declara la mercancía, su cantidad y su valor")],
    worked=[
        ("Clasificar un trámite", "Una carga de ejemplo sale desde un puerto del país hacia otro puerto del mismo país. ¿Qué tipo de trámite es?", ["El origen y el destino están en el mismo país.", "El transporte entre puertos del mismo país es cabotaje."], "Cabotaje"),
        ("Contar trámites", "Una agencia de ejemplo hace 4 importaciones y 6 exportaciones. ¿Cuántos trámites de comercio exterior son?", ["Se suman los dos tipos.", "4 más 6 son 10."], "10 trámites"),
    ],
    mistakes=[("Creer que declarar un valor menor es solo un favor al cliente.", "Una declaración falsa es una infracción según la norma vigente.", "Declara siempre el valor real y consulta a la jefatura."),
              ("Creer que un mensaje con datos de un cliente es privado si nadie más lo ve.", "Un mensaje sin protección puede ser leído por otros.", "Comparte datos solo por medios seguros y a quien corresponde.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es una importación?", "El ingreso de mercancías al país", "La salida de mercancías del país", "El transporte de carga entre puertos del mismo país", "La importación es el ingreso; la salida es exportación y entre puertos del país es cabotaje."),
        ("abc", "En Operaciones Portuarias: ¿qué es el cabotaje?", "El transporte de carga entre puertos del mismo país", "El paso de una mercancía por el país hacia otro destino", "El cambio de destino de una carga que ya llegó", "El cabotaje ocurre dentro del país; el paso hacia otro destino es tránsito."),
        ("abc", "En Operaciones Portuarias: ¿qué hace un agente de aduanas?", "Realiza los trámites aduaneros por cuenta de un cliente que le dio un mandato", "Conduce los camiones que llevan la carga al puerto", "Cuenta los bultos que descargan de la nave", "El agente tramita ante la aduana; conducir y contar son otros roles."),
        ("abc", "{F} ¿Qué observación de la ficha corresponde a una posible declaración falsa?", "El cliente que pide declarar un valor menor al real", "La persona que pasa por el área de maniobras", "El mensaje sin protección", "Declarar un valor menor al real es declarar algo falso."),
        ("abc", "{F} ¿Qué riesgo físico tiene pasar por el área de maniobras de vehículos de carga?", "Ser atropellado o golpeado por un vehículo en movimiento", "Perder el mensaje del cliente", "Pagar más derechos de aduana", "El área de maniobras expone a atropellos; los otros problemas no son daños físicos."),
        ("abc", "{F} ¿Qué trámite de la ficha cambia el destino de una carga que ya llegó?", "La redestinación", "El cabotaje", "El tránsito", "La redestinación cambia el destino de una carga que ya llegó."),
        ("=", "{F} ¿Cuántos trámites hace la agencia en total en el día?", "5+3+2+1+1", "Se suman los trámites de todos los tipos.", " trámites"),
        ("=", "{F} ¿Cuántos trámites de comercio exterior hay, contando importaciones y exportaciones?", "5+3", "Se suman las importaciones y las exportaciones.", " trámites"),
        ("=", "{F} Cuatro contenedores se atrasan 2 días en presentar su declaración. ¿Cuántos pesos paga la agencia por almacenaje?", "4*4000*2", "Se multiplican los contenedores, el costo por día y los días de atraso.", " pesos"),
        ("abc", "{F} El cliente insiste en declarar un valor menor al real. ¿Qué corresponde?", "Negarse a declarar un valor falso, declarar el real e informar a la jefatura", "Aceptar si el cliente asume la responsabilidad", "Aceptar si la diferencia es pequeña", "Una declaración falsa es una infracción, aunque el cliente la pida."),
        ("abc", "En Operaciones Portuarias: ¿por qué conviene cumplir los plazos de presentación de la declaración?", "Porque el atraso genera costos de almacenaje y puede traer sanciones según la norma vigente", "Porque los plazos solo importan a la aduana", "Porque el plazo permite cambiar el valor declarado", "Pasado el plazo se pagan costos y pueden haber sanciones."),
        ("=", "{F} Si los trámites del día se reparten por igual entre las 3 personas del equipo, ¿cuántos trámites hace cada una?", "(5+3+2+1+1)//3", "Se calcula el total de trámites y se divide entre las personas.", " trámites"),
        ("abc", "{F} Para reducir el riesgo de atropello de la persona que lleva el documento, ¿cuál medida es de nivel más efectivo?", "Enviar el documento por un medio digital para que nadie deba pasar por el área de maniobras", "Pedirle que camine con atención", "Entregarle un chaleco reflectante", "Eliminar el desplazamiento quita el peligro; la atención y el chaleco dependen de la persona."),
    ],
    ctx=("abc", "Un conocido te pide que «ayudes» a un amigo suyo a presentar unos papeles de importación escribiendo un valor más bajo, «total nadie revisa». ¿Qué respondes?", "Que no, porque declarar un valor falso es una infracción y los trámites los hace un agente autorizado con datos reales", "Que sí, si el amigo es de confianza", "Que sí, pero solo por una vez", "La veracidad de la declaración no depende de la confianza ni de la frecuencia."),
    sc=[
        ("En Operaciones Portuarias: ¿qué es la exportación?", "La salida de mercancías del país", "La exportación es el movimiento de salida del país."),
        ("¿Qué es un mandato?", "La autorización por escrito del cliente al agente de aduanas", "El agente actúa en nombre del cliente con ese documento."),
        ("¿Qué se hace con los datos de un cliente?", "Se tratan como confidenciales y se comparten solo por medios seguros", "Los datos de los clientes no se difunden."),
    ],
    op=("Un cliente de ejemplo pide a la «Agencia Demo» una redestinación urgente de una carga que ya llegó y sugiere anotar un valor menor «para ahorrar». Además, la persona que lleva el documento al patio debe pasar por el área de maniobras. Escribe (a) qué tipo de trámite es la redestinación, (b) qué respondes sobre el valor, (c) un riesgo físico del patio y un control de nivel alto, (d) por qué los datos del cliente son confidenciales.",
        "(a) Es el cambio del destino de una carga que ya llegó. (b) Que se declara el valor real, porque declarar uno falso es una infracción según la norma vigente, y que se informa a la jefatura. (c) Riesgo: atropello o golpe por un vehículo; control: enviar el documento por medio digital para que nadie pase por el área de maniobras. (d) Porque contienen información comercial de una persona o empresa que no debe difundirse sin protección.",
        ["define la redestinación", "se niega a declarar un valor falso", "identifica el riesgo físico y un control alto", "explica la confidencialidad"],
        ["hoja con las cuatro respuestas"],
        ["aceptar declarar un valor menor", "proponer solo un chaleco como control", "no mencionar la confidencialidad"],
        "Pregunta: «¿qué pasa si se declara un valor falso?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Escribe un ejemplo inventado de cada tipo de trámite: importación, exportación, cabotaje, redestinación y tránsito.",
    extend="Explica con un ejemplo por qué el agente de aduanas no puede declarar un valor falso aunque el cliente lo pida.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (importación de ejemplo, inventada). Mercancía: 200 cajas de herramientas. Valor de la mercancía puesta a bordo (FOB): $8.000.000; flete: $1.200.000; seguro: $200.000. "
     "Tasa de derechos de ejemplo: 6 % sobre el valor CIF. Se presenta un certificado de origen de un país con un tratado de ejemplo que reduce la tasa de esta mercancía a 0 %.")
build(
    O6, 2, F,
    use="Aprenderé el vocabulario de la tramitación aduanera: valor FOB y CIF, derechos, certificado de origen, tratados y documentos de la declaración, y a calcular el valor CIF y los derechos con una tasa de ejemplo.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé calcular un porcentaje sencillo.", "Sé qué es la declaración aduanera."],
    explain=[
        "El valor FOB es el valor de la mercancía puesta a bordo de la nave, sin contar flete ni seguro. El flete es lo que cuesta transportarla y el seguro cubre su riesgo en el viaje. El valor CIF es la suma de valor FOB, seguro y flete: es el valor de la mercancía puesta en el puerto de destino. Los derechos de aduana son un pago al Estado que se calcula aplicando una tasa, un porcentaje, a una base, que en esta clase de ejemplo es el valor CIF. Un porcentaje se calcula multiplicando la base por la tasa y dividiendo entre 100.",
        "La declaración aduanera se respalda con documentos: la factura comercial, el conocimiento de embarque, la lista de embalaje y, cuando corresponde, el certificado de origen, que indica el país donde se produjo la mercancía. Los tratados internacionales son acuerdos entre países que pueden reducir o eliminar la tasa de derechos para mercancías de origen de ciertos países, si se presenta el certificado. La clasificación arancelaria es el código que identifica el tipo de mercancía y fija la tasa que le corresponde.",
        f"Las tasas y los valores de esta clase son de ejemplo; las reales dependen de la norma vigente y de los tratados. {EMER} {AVISO}",
    ],
    vocab=[("valor FOB", "valor de la mercancía puesta a bordo, sin flete ni seguro"), ("valor CIF", "valor FOB más seguro y flete"), ("derechos de aduana", "pago al Estado calculado con una tasa sobre una base"), ("tasa", "porcentaje que se aplica a una base"), ("certificado de origen", "documento que indica el país donde se produjo la mercancía"), ("clasificación arancelaria", "código que identifica el tipo de mercancía y fija su tasa")],
    worked=[
        ("Calcular el CIF", "Una mercancía de ejemplo tiene valor FOB de $5.000.000, flete de $600.000 y seguro de $100.000. ¿Cuál es su valor CIF?", ["El CIF suma FOB, flete y seguro.", "5.000.000 más 600.000 más 100.000 son 5.700.000."], "$5.700.000"),
        ("Calcular derechos", "Una base de ejemplo de $2.000.000 tiene una tasa de 5 %. ¿Cuánto son los derechos?", ["Se multiplica la base por la tasa y se divide entre 100.", "2.000.000 por 5 son 10.000.000, y dividido en 100 son 100.000."], "$100.000"),
    ],
    mistakes=[("Calcular los derechos sobre el FOB cuando la base indicada es el CIF.", "Se omiten el flete y el seguro y el resultado es menor al correcto.", "Suma FOB, flete y seguro antes de aplicar la tasa."),
              ("Creer que el certificado de origen indica el peso de la carga.", "El certificado indica el país donde se produjo la mercancía.", "Relaciona el certificado con el origen y los tratados.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es el valor CIF?", "El valor de la mercancía más el seguro y el flete hasta el puerto de destino", "El valor de la mercancía sin flete ni seguro", "El valor de los derechos pagados a la aduana", "El CIF incluye costo de la mercancía, seguro y flete."),
        ("abc", "En Operaciones Portuarias: ¿qué es un certificado de origen?", "Un documento que indica el país donde se produjo la mercancía", "Un documento que indica el peso de la mercancía", "Un documento que autoriza a un camión a entrar al puerto", "El certificado de origen se relaciona con el país de producción."),
        ("abc", "En Operaciones Portuarias: ¿qué es un mandato en el trámite aduanero?", "La autorización por escrito del cliente para que el agente de aduanas realice el trámite por él", "El plazo para pagar los derechos", "El número de la declaración aduanera", "El mandato da al agente facultad de actuar por su cliente."),
        ("=", "{F} ¿Cuál es el valor CIF de la mercancía?", "8000000+1200000+200000", "Se suman el valor FOB, el flete y el seguro.", " pesos"),
        ("abc", "{F} ¿Qué documento permite aplicar la tasa reducida por el tratado de ejemplo?", "El certificado de origen", "La lista de embalaje", "El seguro de la carga", "El certificado demuestra el origen que da derecho a la tasa reducida."),
        ("=", "{F} Sin tratado, ¿cuántos pesos serían los derechos con la tasa de 6 % sobre el valor CIF?", "(8000000+1200000+200000)*6//100", "Se calcula el CIF, se multiplica por la tasa y se divide entre 100.", " pesos"),
        ("=", "{F} ¿Cuántos pesos vale en promedio una caja en valor FOB?", "8000000//200", "Se divide el valor FOB entre las cajas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta el flete por caja?", "1200000//200", "Se divide el flete entre las cajas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos vale cada caja en valor CIF?", "(8000000+1200000+200000)//200", "Se calcula el CIF total y se divide entre las cajas.", " pesos"),
        ("abc", "{F} Si el flete subiera a $1.500.000, ¿cómo cambia el valor CIF?", "Sube en $300.000, porque el flete forma parte del CIF", "No cambia, porque el flete no forma parte del valor", "Baja en $300.000", "El CIF suma el flete; si este sube, el CIF sube lo mismo."),
        ("abc", "{F} Con el certificado de origen del tratado de ejemplo, ¿cuánto se pagaría de derechos?", "Nada, porque la tasa de ejemplo se reduce a 0 %", "$564.000, porque el tratado no cambia la tasa", "$282.000, la mitad de lo que se pagaría sin tratado", "Una tasa de 0 % aplicada a cualquier base da 0 de derechos."),
        ("=", "{F} Si no hubiera tratado y la tasa de ejemplo fuera 10 % en lugar de 6 %, ¿cuántos pesos serían los derechos?", "(8000000+1200000+200000)*10//100", "Se aplica la tasa de 10 % sobre el valor CIF.", " pesos"),
        ("abc", "{F} Un cliente pide declarar el valor CIF como $7.000.000. ¿Qué corresponde?", "Declarar el valor real y no aceptar el pedido, que sería una declaración falsa", "Aceptar, porque el cliente decide el valor", "Aceptar, si firma un mandato", "El valor debe ser el real; el mandato no autoriza a declarar algo falso."),
    ],
    ctx=("abc", "Un amigo te dice: «los derechos se calculan sobre el valor de la mercancía, no sobre el flete ni el seguro, así que no los sumes». En este caso de ejemplo, ¿qué le respondes?", "Que la base de ejemplo es el CIF, que sí suma flete y seguro", "Que tiene razón, porque el flete nunca cuenta", "Que el seguro cuenta pero el flete no", "En esta clase la base es el valor CIF, que incluye flete y seguro."),
    sc=[
        ("En Operaciones Portuarias: ¿cómo se calcula el valor CIF?", "Sumando el valor FOB, el flete y el seguro", "El CIF incluye los tres componentes."),
        ("¿Cómo se calculan los derechos con una tasa?", "Multiplicando la base por la tasa y dividiendo entre 100", "Un porcentaje se calcula con la base y la tasa."),
        ("¿Para qué sirve un certificado de origen?", "Para demostrar el país de producción y acceder a un tratado", "Algunos tratados reducen la tasa según el origen."),
    ],
    op=("Importación de ejemplo: 100 cajas de repuestos; valor FOB $3.000.000; flete $500.000; seguro $100.000; tasa de derechos de ejemplo de 5 % sobre el valor CIF, sin tratado. Escribe (a) el valor CIF, (b) los derechos que corresponden, (c) el valor CIF por caja, (d) qué documento permitiría una tasa reducida si existiera un tratado.",
        "(a) 3.000.000 + 500.000 + 100.000 = $3.600.000. (b) 3.600.000 × 5 ÷ 100 = $180.000. (c) 3.600.000 ÷ 100 = $36.000 por caja. (d) El certificado de origen, que demuestra el país de producción.",
        ["calcula el CIF sumando los tres valores", "calcula los derechos con la tasa", "calcula el CIF por caja", "nombra el certificado de origen"],
        ["hoja con las cuatro respuestas"],
        ["calcular los derechos sobre el FOB", "dividir mal entre 100", "confundir el certificado de origen con la lista de embalaje"],
        "Pregunta: «¿qué se suma para obtener el CIF?». Si no responde, pídele que relea la definición de valor CIF."),
    reinforce="Inventa un valor FOB, un flete y un seguro, y calcula el valor CIF y los derechos con una tasa de ejemplo.",
    extend="Explica con un ejemplo por qué un tratado puede cambiar el monto de los derechos.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Los días hábiles se numeran en orden. La «Nave Demo» arriba el día 10 con 5 contenedores de un cliente. Plazo de ejemplo para presentar la declaración: 3 días hábiles desde el arribo. "
     "Almacenaje de ejemplo por atraso: $4.000 por contenedor por día. La agencia presenta la declaración el día 15. Se pagan los derechos el día 17. Plazo de ejemplo para retirar la carga: 2 días hábiles desde el pago. El retiro se hace el día 18.")
build(
    O6, 3, F,
    use="Aprenderé a controlar plazos de una tramitación aduanera en días hábiles, a calcular atrasos y costos de almacenaje y a registrar siempre la fecha real.",
    prior=["Sé sumar y restar números enteros.", "Sé qué es un cronograma y un desfase.", "Sé qué es la declaración aduanera."],
    explain=[
        "Una tramitación tiene plazos: tiempos máximos para cumplir cada paso. Se cuentan en días hábiles, que son los días en que funcionan las oficinas, sin contar sábados, domingos ni feriados. Aquí los numeramos en orden para calcular más fácil. El último día de un plazo es el día de inicio más la cantidad de días. Si se actúa después, hay un atraso, que se calcula restando el último día del plazo al día en que realmente se actuó.",
        "El atraso trae un costo de almacenaje: cada día que la carga permanece guardada después del plazo se cobra por contenedor. Por eso se planifican los pasos con anticipación. Si se prevé que un plazo no se cumplirá, se avisa al cliente y a quien corresponde, y se registra la razón. La fecha que se anota es siempre la real: falsear una fecha es una infracción según la norma vigente.",
        f"Los plazos y los cobros de esta clase son de ejemplo; los reales dependen de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("plazo", "tiempo máximo para cumplir un paso"), ("día hábil", "día en que funcionan las oficinas, sin sábados, domingos ni feriados"), ("atraso", "días que pasan después del último día del plazo"), ("almacenaje", "cobro por mantener la carga guardada"), ("fecha real", "fecha en que efectivamente se hizo el paso")],
    worked=[
        ("Último día del plazo", "Una nave de ejemplo arriba el día 20 y el plazo es de 4 días hábiles. ¿Cuál es el último día?", ["El último día es el día de inicio más los días del plazo.", "20 más 4 son 24."], "Día 24"),
        ("Calcular un atraso", "El plazo de ejemplo termina el día 24 y se actúa el día 27. ¿Cuántos días de atraso hay?", ["El atraso es el día real menos el último día del plazo.", "27 menos 24 son 3."], "3 días de atraso"),
    ],
    mistakes=[("Contar los días corridos en vez de los días hábiles.", "Se incluyen días en que las oficinas no funcionan y el plazo queda mal calculado.", "Cuenta solo los días hábiles."),
              ("Anotar una fecha anterior a la real para evitar un cobro.", "Falsear una fecha es una infracción y oculta el atraso.", "Anota la fecha real y explica la razón.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es un día hábil?", "Un día en que funcionan las oficinas, sin contar sábados, domingos ni feriados", "Cualquier día del calendario", "Un día en que la nave está en el puerto", "Los plazos hábiles se cuentan solo en días de funcionamiento de las oficinas."),
        ("abc", "En Operaciones Portuarias: ¿qué es el plazo de presentación de una declaración?", "El tiempo máximo para presentarla", "El tiempo que tarda la aduana en revisar la carga", "El tiempo que dura el viaje de la nave", "El plazo de presentación fija el límite para presentar la declaración."),
        ("abc", "En Operaciones Portuarias: ¿qué es el cobro de almacenaje por atraso?", "El cobro por cada día que la carga permanece guardada después del plazo", "El pago de los derechos de aduana", "El pago al agente de aduanas", "El almacenaje se cobra por los días de más que la carga queda guardada."),
        ("=", "{F} ¿Cuál es el último día del plazo de presentación de la declaración?", "10+3", "Se suman al día de arribo los días hábiles del plazo.", ""),
        ("=", "{F} ¿Cuántos días de atraso tuvo la presentación de la declaración?", "15-(10+3)", "Se resta el último día del plazo al día en que se presentó.", " días"),
        ("abc", "{F} ¿Se cumplió el plazo de presentación?", "No, porque se presentó después del último día del plazo", "Sí, porque se presentó antes del pago de los derechos", "Sí, porque la nave ya había arribado", "La presentación fue posterior al último día del plazo."),
        ("=", "{F} ¿Cuántos pesos se pagan por el almacenaje de los 5 contenedores durante el atraso?", "5*4000*(15-(10+3))", "Se multiplican los contenedores, el costo diario y los días de atraso.", " pesos"),
        ("=", "{F} ¿Cuál es el último día del plazo para retirar la carga?", "17+2", "Se suman al día de pago los días hábiles del plazo de retiro.", ""),
        ("abc", "{F} ¿Se cumplió el plazo de retiro?", "Sí, porque el retiro se hizo el día 18, antes del día 19", "No, porque el retiro debía hacerse el día del pago", "No, porque el retiro se hizo después de la presentación", "El último día para retirar era el 19 y se retiró el 18."),
        ("abc", "{F} Si el retiro se hubiera hecho el día 21, ¿qué ocurriría?", "Habría 2 días de atraso en el retiro y se cobraría almacenaje por ellos", "Nada, porque el plazo de retiro no existe", "Se perdería para siempre el derecho a retirar", "El día 21 supera el último día, el 19, en dos días."),
        ("abc", "En Operaciones Portuarias: ¿qué corresponde hacer cuando se prevé que un plazo no se cumplirá?", "Avisar con anticipación al cliente y a quien corresponde y registrar la razón", "Anotar una fecha anterior en el registro", "Esperar a que pase el plazo y luego avisar", "Avisar a tiempo permite reprogramar y reducir costos, y se deja constancia."),
        ("=", "{F} Si la declaración se hubiera presentado el día 14, ¿cuántos pesos menos se habrían pagado de almacenaje?", "5*4000*2-5*4000*1", "Se compara el costo con 2 días de atraso con el de 1 día.", " pesos"),
        ("abc", "{F} Un cliente pide anotar que la declaración se presentó el día 13 «para evitar el cobro». ¿Qué respuesta es correcta?", "Es falso: se debe anotar la fecha real, porque falsear una fecha es una infracción", "Es cierto: el cliente decide la fecha", "Es cierto, si la diferencia es de solo 2 días", "La fecha real es la única que se puede registrar."),
    ],
    ctx=("abc", "Un compañero de práctica dice: «como el atraso fue de pocos días, anotemos la fecha del plazo y nadie se entera». ¿Qué respondes?", "Que se anota la fecha real y se informa la razón del atraso", "Que lo anotas, porque son pocos días", "Que lo anotas y corriges si preguntan", "Registrar una fecha falsa es una infracción y oculta la causa del atraso."),
    sc=[
        ("En Operaciones Portuarias: ¿cómo se calcula el último día de un plazo?", "Sumando los días hábiles al día de inicio", "El último día es el inicio más la duración del plazo."),
        ("¿Cómo se calcula el atraso?", "Restando el último día del plazo al día real", "El atraso mide los días que pasaron del plazo."),
        ("¿Qué fecha se anota en un registro?", "La fecha real en que se hizo el paso", "Falsear una fecha es una infracción."),
    ],
    op=("Caso de ejemplo con días hábiles numerados: la nave arriba el día 20 con 6 contenedores; el plazo de presentación es de 4 días hábiles desde el arribo; el almacenaje por atraso es de $3.000 por contenedor por día; la declaración se presenta el día 26. Escribe (a) el último día del plazo, (b) los días de atraso, (c) el costo de almacenaje, (d) qué fecha se anota y por qué.",
        "(a) 20 + 4 = día 24. (b) 26 − 24 = 2 días. (c) 6 × 3.000 × 2 = $36.000. (d) Se anota el día 26, que es la real, porque falsear una fecha es una infracción y oculta el atraso.",
        ["calcula el último día del plazo", "calcula los días de atraso", "calcula el costo de almacenaje", "indica anotar la fecha real"],
        ["hoja con las cuatro respuestas"],
        ["contar días corridos", "olvidar multiplicar por los contenedores", "anotar la fecha del plazo en vez de la real"],
        "Pregunta: «¿qué día debía ser el último?». Si no responde, pídele que relea cómo se calcula el último día de un plazo."),
    reinforce="Inventa una nave que arriba un día y un plazo de días hábiles, y calcula el último día y un atraso supuesto.",
    extend="Explica con un ejemplo por qué conviene avisar a tiempo cuando se prevé un atraso.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (importación de ejemplo, inventada). Se importan 500 unidades de una mercancía. Valor FOB: $10.000.000; flete: $1.500.000; seguro: $500.000. Tasa de derechos de ejemplo: 5 % sobre el valor CIF. "
     "Honorarios del agente de aduanas: $200.000 (valor de ejemplo). Almacenaje por atraso: 3 días a $30.000 por día (valor de ejemplo).")
build(
    O6, 4, F,
    use="Aprenderé a calcular el costo total de una internación y el costo por unidad, y a reconocer qué parte depende de cumplir los plazos.",
    prior=["Sé calcular el valor CIF y los derechos con una tasa.", "Sé calcular atrasos y almacenaje.", "Sé dividir números enteros."],
    explain=[
        "El costo total de internación es todo lo que cuesta dejar la mercancía disponible en el país. Suma el valor CIF, los derechos de aduana, los honorarios del agente y, si hubo atraso, el almacenaje. El costo unitario es el costo total dividido entre las unidades importadas. Sirve para que el cliente decida a qué precio puede vender cada unidad.",
        "Cada parte del costo tiene su origen: el valor CIF depende de la compra, del flete y del seguro; los derechos dependen de la tasa de ejemplo y de la base; los honorarios, del contrato con el agente; y el almacenaje solo aparece si se pasa un plazo. Por eso es la parte que se puede evitar con buena planificación. Todo cálculo se hace con los valores reales declarados: no se rebajan valores para pagar menos.",
        f"Todos los valores y tasas de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("costo total de internación", "suma del valor CIF, los derechos, los honorarios y el almacenaje"), ("costo unitario", "costo total dividido entre las unidades"), ("honorarios", "pago al agente de aduanas por su trabajo"), ("base de cálculo", "valor sobre el que se aplica la tasa"), ("tasa de ejemplo", "porcentaje inventado para practicar cálculos")],
    worked=[
        ("Costo total", "Una importación de ejemplo tiene CIF de $4.000.000, derechos de $200.000 y honorarios de $100.000, sin atraso. ¿Cuál es el costo total?", ["Se suman las tres partes.", "4.000.000 más 200.000 más 100.000 son 4.300.000."], "$4.300.000"),
        ("Costo unitario", "El costo total de ejemplo es $4.300.000 para 100 unidades. ¿Cuánto cuesta cada unidad?", ["Se divide el costo total entre las unidades.", "4.300.000 dividido en 100 son 43.000."], "$43.000"),
    ],
    mistakes=[("Olvidar sumar los honorarios o el almacenaje al costo total.", "El costo queda subestimado y el precio de venta puede quedar bajo.", "Haz una lista de todas las partes antes de sumar."),
              ("Rebajar el valor declarado para disminuir los derechos.", "Es una declaración falsa y una infracción.", "Declara siempre el valor real.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es el costo total de internación?", "Todo lo que cuesta dejar la mercancía disponible en el país: valor CIF, derechos y gastos", "Solo el valor de la mercancía en el país de origen", "Solo los derechos que se pagan a la aduana", "El costo total reúne todas las partes, no solo una."),
        ("abc", "En Operaciones Portuarias: ¿qué es la base de cálculo de los derechos?", "El valor sobre el que se aplica la tasa, en estos ejemplos el CIF", "El peso de la mercancía", "El número de contenedores", "La tasa se aplica sobre un valor, no sobre el peso ni el número de contenedores."),
        ("abc", "En Operaciones Portuarias: ¿qué es el costo unitario?", "El costo total dividido entre las unidades importadas", "El costo de un solo contenedor", "El valor de los honorarios", "El costo unitario reparte el costo total entre las unidades."),
        ("=", "{F} ¿Cuál es el valor CIF de la importación?", "10000000+1500000+500000", "Se suman el valor FOB, el flete y el seguro.", " pesos"),
        ("=", "{F} ¿Cuántos pesos son los derechos de ejemplo?", "(10000000+1500000+500000)*5//100", "Se aplica la tasa de 5 % sobre el valor CIF.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta el almacenaje por el atraso?", "3*30000", "Se multiplican los días de atraso por el costo diario.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de internación?", "12000000+600000+200000+3*30000", "Se suman el CIF, los derechos, los honorarios y el almacenaje.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta cada unidad, dividiendo el costo total entre las unidades?", "(12000000+600000+200000+3*30000)//500", "Se calcula el costo total y se divide entre las 500 unidades.", " pesos"),
        ("=", "{F} ¿Cuántos pesos de derechos corresponden a cada unidad?", "((10000000+1500000+500000)*5//100)//500", "Se calculan los derechos totales y se dividen entre las unidades.", " pesos"),
        ("abc", "{F} Un compañero dice: «los derechos se calculan sobre el valor FOB». ¿Qué respuesta es correcta en este caso de ejemplo?", "Es falso: en este caso la base es el valor CIF, que suma flete y seguro", "Es cierto: el FOB es el único valor de la mercancía", "Es cierto, si el flete es alto", "La ficha indica que la tasa se aplica sobre el CIF."),
        ("abc", "{F} ¿Qué componente del costo total depende de cumplir los plazos?", "El almacenaje por atraso", "El flete", "El valor FOB", "El almacenaje solo aparece si se pasa un plazo."),
        ("=", "{F} Si el flete subiera a $2.000.000, ¿cuántos pesos más se pagarían de derechos?", "500000*5//100", "Se calcula cuánto aumenta el CIF y se aplica la tasa.", " pesos"),
        ("abc", "{F} El cliente quiere vender cada unidad a $27.000. Con el costo unitario calculado, ¿gana o pierde, antes de otros costos?", "Gana $1.220 por unidad", "Pierde $1.220 por unidad", "No gana ni pierde", "El costo unitario es $25.780 y el precio $27.000 deja una diferencia de $1.220."),
    ],
    ctx=("abc", "Un cliente de ejemplo te pide que, para que le salga más barato, no incluyas el flete en el valor que declaras. ¿Qué respondes?", "Que no, porque el valor declarado debe ser el real, incluyendo lo que la norma vigente establezca", "Que sí, porque es su dinero", "Que sí, si es solo el flete", "Rebajar un valor declarado es una declaración falsa."),
    sc=[
        ("En Operaciones Portuarias: ¿cómo se calcula el costo unitario?", "Dividiendo el costo total entre las unidades", "El costo unitario reparte el total entre las unidades."),
        ("¿Qué partes suma el costo total de internación?", "CIF, derechos, honorarios y almacenaje", "Son todas las partes del costo de la internación."),
        ("¿Qué parte del costo se evita cumpliendo los plazos?", "El almacenaje por atraso", "Solo se cobra si se pasa el plazo."),
    ],
    op=("Importación de ejemplo de 200 unidades: valor FOB $4.000.000; flete $600.000; seguro $200.000; tasa de derechos de ejemplo de 5 % sobre el valor CIF; honorarios del agente $150.000; sin atraso. Escribe (a) el valor CIF, (b) los derechos, (c) el costo total de internación, (d) el costo unitario.",
        "(a) 4.000.000 + 600.000 + 200.000 = $4.800.000. (b) 4.800.000 × 5 ÷ 100 = $240.000. (c) 4.800.000 + 240.000 + 150.000 = $5.190.000. (d) 5.190.000 ÷ 200 = $25.950 por unidad.",
        ["calcula el CIF", "calcula los derechos", "suma todas las partes del costo", "calcula el costo unitario"],
        ["hoja con las cuatro respuestas"],
        ["olvidar los honorarios", "calcular los derechos sobre el FOB", "dividir entre un número equivocado"],
        "Pregunta: «¿qué partes tiene el costo total?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa una importación con sus partes de costo y calcula el costo unitario.",
    extend="Explica con un ejemplo cómo un atraso aumenta el costo unitario de una importación.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Hay que enviar 4.000 kg de carga entre dos ciudades de ejemplo. Vía marítima: flete de $150 por kg, 20 días de tránsito. Vía aérea: $900 por kg, 2 días. Vía terrestre: $400 por kg, 6 días. "
     "Costo de inmovilización de ejemplo: $5.000 por cada día de tránsito. El cliente exige que la carga llegue en 7 días como máximo. "
     "Lista de verificación de la declaración (5 puntos): descripción de la mercancía; valor y moneda; cantidad y peso; consignatario; documentos de respaldo adjuntos. En la revisión de ejemplo, el valor y la moneda no coinciden con la factura.")
build(
    O6, 5, F,
    use="Aprenderé a comparar vías de transporte (marítima, aérea y terrestre) por costo y tiempo y a verificar una declaración con una lista de verificación bajo el principio de cero faltas.",
    prior=["Sé calcular costos totales y comparar con un plazo.", "Sé qué es una lista de verificación.", "Sé qué es una declaración aduanera."],
    explain=[
        "La carga internacional puede viajar por vía marítima, aérea o terrestre. En general, la marítima es la más barata y la más lenta; la aérea es la más rápida y la más cara; la terrestre queda entre ambas y solo sirve entre lugares conectados por tierra. Al comparar se calcula el costo de transportar, que es el costo por kilo por los kilos, y el costo de inmovilización, que es el costo de tener la mercancía en tránsito y sin poder usarla, por cada día de tránsito. El costo total es la suma de ambos.",
        "Para elegir, primero se descartan las vías que no cumplen el plazo exigido por el cliente; entre las que cumplen, se elige la de menor costo total. Antes de presentar una declaración, se verifica con una lista de verificación: se revisa cada punto y se compara con la factura y los demás documentos. Bajo el principio de cero faltas, si un punto no está en orden se corrige antes de presentar; no se presenta una declaración con una diferencia conocida.",
        f"Los precios y los tiempos de esta clase son de ejemplo. Las exigencias reales dependen de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("vía de transporte", "modo de transportar la carga: marítimo, aéreo o terrestre"), ("tiempo de tránsito", "tiempo que tarda la carga en llegar de origen a destino"), ("costo de inmovilización", "costo de tener la mercancía en tránsito sin poder usarla"), ("costo total", "costo de transporte más costo de inmovilización"), ("lista de verificación", "lista de puntos que se revisan antes de presentar la declaración")],
    worked=[
        ("Costo de una vía", "Se transportan 1.000 kg a $200 por kg durante 10 días con inmovilización de $3.000 por día. ¿Cuál es el costo total?", ["El transporte cuesta 1.000 por 200, o sea 200.000.", "La inmovilización cuesta 10 por 3.000, o sea 30.000. En total, 230.000."], "$230.000"),
        ("Elegir con plazo", "La vía A cuesta $230.000 y tarda 10 días; la vía B cuesta $400.000 y tarda 3 días. El cliente exige 5 días como máximo. ¿Cuál conviene?", ["La vía A no cumple los 5 días.", "Solo la vía B cumple el plazo."], "La vía B"),
    ],
    mistakes=[("Elegir la vía más barata sin comprobar el plazo que exige el cliente.", "Una vía barata que llega tarde no sirve.", "Descarta primero las vías que no cumplen el plazo."),
              ("Presentar la declaración aunque un punto de la lista no esté en orden.", "Se presenta con una diferencia conocida y se incumple cero faltas.", "Corrige el punto antes de presentar.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es el tiempo de tránsito?", "El tiempo que tarda la carga en llegar de origen a destino", "El tiempo que la carga espera en el patio del puerto", "El tiempo que dura el trámite en la aduana", "El tránsito se mide desde que sale hasta que llega."),
        ("abc", "En Operaciones Portuarias: ¿qué es el costo de inmovilización?", "El costo de tener la mercancía en tránsito, sin poder usarla", "El costo de comprar la mercancía", "El costo de los honorarios del agente", "Mientras viaja, la mercancía está inmovilizada y eso tiene un costo."),
        ("abc", "En Operaciones Portuarias: ¿qué significa verificar una declaración?", "Revisar que sus datos coincidan con los documentos y con la carga antes de presentarla", "Presentarla lo antes posible aunque falten documentos", "Cambiar los valores para que coincidan con los del cliente", "Verificar es comparar los datos con los documentos antes de presentar."),
        ("=", "{F} ¿Cuántos pesos cuesta el flete por vía marítima?", "4000*150", "Se multiplican los kilos por el precio por kilo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta el flete por vía aérea?", "4000*900", "Se multiplican los kilos por el precio por kilo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta el flete por vía terrestre?", "4000*400", "Se multiplican los kilos por el precio por kilo.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la vía marítima, sumando el costo de inmovilización?", "4000*150+20*5000", "Se suman el flete y la inmovilización de los días de tránsito.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la vía terrestre?", "4000*400+6*5000", "Se suman el flete y la inmovilización de los días de tránsito.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de la vía aérea?", "4000*900+2*5000", "Se suman el flete y la inmovilización de los días de tránsito.", " pesos"),
        ("abc", "{F} Con la exigencia de llegar en 7 días como máximo, ¿qué vía conviene?", "La terrestre, porque cumple el plazo y cuesta menos que la aérea", "La marítima, porque es la más barata", "La aérea, porque es la más rápida", "La marítima no cumple el plazo; entre las dos que cumplen, la terrestre cuesta menos."),
        ("abc", "{F} Si el cliente no exigiera plazo, ¿qué vía tendría el menor costo total?", "La marítima, porque su costo total es el más bajo", "La terrestre, porque tiene un tiempo intermedio", "La aérea, porque casi no hay inmovilización", "Sin plazo exigido, se elige la de menor costo total."),
        ("=", "{F} ¿Cuántos pesos más cuesta en total la vía aérea que la terrestre?", "(4000*900+2*5000)-(4000*400+6*5000)", "Se resta el costo total de la vía terrestre al de la vía aérea.", " pesos"),
        ("abc", "{F} En la revisión, el valor y la moneda no coinciden con la factura. ¿Se puede presentar la declaración?", "No: se corrige ese punto antes de presentar, por el principio de cero faltas", "Sí, porque 4 de 5 puntos están en orden", "Sí, si el cliente firma una autorización", "Con un punto pendiente no se presenta; cero faltas exige que todos estén en orden."),
    ],
    ctx=("abc", "Una persona de la oficina de ejemplo te dice: «el valor no coincide con la factura, pero presentémosla igual y la corregimos después, para no atrasarnos». ¿Qué respondes?", "Que se corrige antes de presentar y, si no alcanza el plazo, se avisa y se registra la razón", "Que se presenta igual, para cumplir el plazo", "Que se presenta con el valor de la factura y se anota otro internamente", "Presentar con una diferencia conocida incumple cero faltas y puede ser una infracción."),
    sc=[
        ("En Operaciones Portuarias: ¿cómo se calcula el costo total de una vía?", "Sumando el costo de transporte y el de inmovilización", "Ambos costos forman el costo total de la vía."),
        ("¿Qué se hace primero al elegir una vía con plazo exigido?", "Descartar las vías que no cumplen el plazo", "Entre las que cumplen, se elige la de menor costo."),
        ("¿Qué exige cero faltas antes de presentar una declaración?", "Que todos los puntos de la lista estén en orden", "Un punto pendiente se corrige antes de presentar."),
    ],
    op=("Hay que enviar 2.500 kg de carga. Vía X: $200 por kg, 10 días de tránsito. Vía Y: $500 por kg, 3 días de tránsito. Costo de inmovilización de ejemplo: $4.000 por día de tránsito. El cliente exige llegar en 5 días como máximo. Escribe (a) el flete de la vía X, (b) el costo total de la vía X, (c) el costo total de la vía Y, (d) qué vía conviene y por qué.",
        "(a) 2.500 × 200 = $500.000. (b) 500.000 + 10 × 4.000 = $540.000. (c) 2.500 × 500 = 1.250.000; más 3 × 4.000 = 12.000; total $1.262.000. (d) La vía Y, porque es la única que cumple el plazo de 5 días; la X tarda 10 días aunque cueste menos.",
        ["calcula el flete de X", "calcula el costo total de X", "calcula el costo total de Y", "elige según el plazo y justifica"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la inmovilización", "elegir la vía más barata sin comprobar el plazo", "multiplicar por los días en vez de por los kilos"],
        "Pregunta: «¿qué vía cumple el plazo de 5 días?». Si no responde, pídele que compare los días de cada vía con el plazo."),
    reinforce="Inventa dos vías de transporte con precio por kilo y días de tránsito y calcula el costo total de cada una.",
    extend="Explica con un ejemplo por qué la vía más cara puede ser la correcta cuando el plazo es corto.",
)
