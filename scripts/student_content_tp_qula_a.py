"""Química Industrial, mención Laboratorio Químico (4.º medio TP): OAM-01 (muestras para análisis químico) y OAM-02 (clasificar y rotular muestras e insumos). Todo en papel, con datos de ejemplo; sin técnicas de muestreo, solo conceptos, documentos y cálculos de planilla."""
from __future__ import annotations

from tp_qula_common import AVISO, EMER, build, em

O1 = "TP-QULA-4-OAM-01"
O2 = "TP-QULA-4-OAM-02"

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Llega al laboratorio de control de calidad de la empresa ficticia «Química Demo Valle Claro» un lote de 40 sacos de un material de ejemplo. Plan de muestreo de ejemplo: se muestrean 10 de los 40 sacos, elegidos al azar. "
     "Peligros anotados: sacos pesados, polvo del material y piso resbaladizo. Matriz de ejemplo: puntaje de riesgo = probabilidad (1 a 5) × gravedad (1 a 5). Sacos pesados: probabilidad 3 y gravedad 3. Polvo: probabilidad 4 y gravedad 3. Piso resbaladizo: probabilidad 4 y gravedad 2. "
     "De cada saco muestreado se reserva una porción de 200 g (de ejemplo).")
build(
    O1, 1, F,
    use="Aprenderé por qué se toman muestras para análisis químico, qué significan integridad y representatividad, qué peligros tiene el muestreo y por qué solo personal formado toma muestras.",
    prior=["Sé qué es un lote y un registro.", "Sé calcular porcentajes sencillos.", "Sé multiplicar y sumar números enteros."],
    explain=[
        "En el laboratorio químico, una muestra es una porción pequeña que se analiza para conocer cómo es un lote completo. El muestreo es el conjunto de decisiones y registros para obtener esa porción. Para que el análisis sirva, la muestra debe ser representativa, es decir, reflejar al lote entero, y debe conservar su integridad, es decir, no contaminarse ni cambiar entre el lugar de origen y el laboratorio. Si no es representativa, el resultado engaña, aunque el análisis sea perfecto.",
        "El muestreo se hace según un protocolo, que es un documento con las reglas aprobadas por la empresa, y respeta la norma vigente y las indicaciones de la hoja de datos de seguridad, que solo se lee. Un peligro es una fuente de daño y el riesgo es la posibilidad de que ocurra; el puntaje de riesgo de la matriz de ejemplo es probabilidad por gravedad.",
        f"Tomar muestras exige formación, autorización y elementos de protección. Este cuaderno no enseña a tomarlas: solo trabaja con documentos y cálculos en papel. {EMER} {AVISO}",
    ],
    vocab=[("muestra", "porción pequeña que se analiza para conocer un lote completo"), ("muestreo", "decisiones y registros para obtener una muestra"), ("representatividad", "capacidad de la muestra de reflejar al lote entero"), ("integridad de la muestra", "que no se contamine ni cambie entre el origen y el laboratorio"), ("protocolo", "documento con las reglas aprobadas para hacer una tarea"), ("puntaje de riesgo", "probabilidad multiplicada por gravedad, según la matriz")],
    worked=[
        ("Porcentaje del lote", "En un plan de ejemplo se muestrean 6 de 30 bultos. ¿Qué porcentaje del lote se muestrea?", ["Se divide 6 entre 30 y se multiplica por 100.", "6 por 100 son 600, y 600 entre 30 son 20."], "20 %"),
        ("Puntaje de riesgo", "Un riesgo de ejemplo del muestreo, el tránsito de una carretilla, tiene probabilidad 2 y gravedad 4. ¿Qué puntaje tiene?", ["Se multiplica la probabilidad por la gravedad.", "2 por 4 son 8."], "8 puntos"),
    ],
    mistakes=[("Creer que quien leyó el plan de muestreo ya puede tomar muestras.", "Tomar muestras exige formación, autorización y elementos de protección.", "Usa el plan para entender el trabajo y pide autorización para hacerlo."),
              ("Pensar que una muestra sirve aunque se haya contaminado en el camino, porque «el análisis es exacto».", "Un análisis exacto de una muestra alterada no refleja al lote.", "Cuida la integridad y registra cualquier incidente.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es una muestra?", "Una porción pequeña que se analiza para conocer un lote completo", "El lote completo que llega a la planta", "El informe con los resultados del análisis", "La muestra es una parte que representa al todo."),
        ("abc", "En el laboratorio químico: ¿qué significa que una muestra sea representativa?", "Que refleja al lote entero", "Que es la más grande que se pudo tomar", "Que fue tomada por la persona más antigua", "La representatividad se refiere a reflejar al lote, no al tamaño ni a quién la toma."),
        ("abc", "En el laboratorio químico: ¿qué es la integridad de una muestra?", "Que no se contamine ni cambie entre el origen y el laboratorio", "Que la muestra pese exactamente un kilo", "Que la muestra tenga un rótulo de colores", "La integridad evita que la muestra deje de reflejar al lote."),
        ("=", "{F} ¿Qué porcentaje del lote de 40 sacos se muestrea?", "10*100//40", "Se divide los sacos muestreados entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos gramos suman las porciones de los 10 sacos muestreados?", "10*200", "Se multiplican los sacos muestreados por los gramos de cada porción.", " g"),
        ("=", "{F} ¿Qué puntaje de riesgo tiene el polvo del material?", "4*3", "Se multiplica la probabilidad por la gravedad.", " puntos"),
        ("abc", "{F} Según la matriz, ¿qué peligro tiene el mayor puntaje de riesgo?", "El polvo, con 12 puntos", "Los sacos pesados, con 9 puntos", "El piso resbaladizo, con 8 puntos", "Se compara probabilidad por gravedad de cada peligro."),
        ("abc", "{F} ¿Por qué el plan elige los 10 sacos «al azar»?", "Para que todos los sacos tengan la misma posibilidad de ser elegidos y la muestra sea representativa", "Para que se elijan siempre los más cercanos a la puerta", "Para terminar más rápido sin importar el resultado", "Elegir al azar evita el sesgo."),
        ("abc", "{F} Un compañero propone tomar solo los 10 sacos de la parte alta de la pila «porque son más fáciles». ¿Qué corresponde?", "Rechazarlo, porque esa muestra podría no representar al lote entero", "Aceptarlo, porque el total de sacos es el mismo", "Aceptarlo si los sacos están bien rotulados", "Elegir lo más cómodo introduce un sesgo."),
        ("=", "{F} ¿Cuántos sacos del lote quedan sin muestrear?", "40-10", "Se resta los sacos muestreados al total.", " sacos"),
        ("abc", "Una estudiante de ejemplo ve en el laboratorio una muestra de un polvo y propone «tomar una pizca» para probarla ella misma. ¿Qué corresponde?", "No hacerlo: tomar y manipular muestras es tarea de personal formado y autorizado", "Hacerlo si usa guantes", "Hacerlo solo si es una cantidad pequeña", "Las muestras se manejan solo con formación y autorización."),
        ("=", "{F} Si el plan subiera a 12 sacos muestreados, ¿cuántos gramos sumarían las porciones de 200 g?", "12*200", "Se multiplican los sacos por los gramos de cada porción.", " g"),
        em("Lees el plan de muestreo de ejemplo en el laboratorio cuando alguien avisa que un saco se rompió y que hay polvo en el aire con olor irritante.", 0),
    ],
    ctx=("abc", "Una jefatura de ejemplo te dice: «Ve a la bodega y toma tú las muestras de los 10 sacos, ya leíste el plan». No hay instructor ni autorización. ¿Qué respondes?", "Que no, porque tomar muestras exige formación, autorización y norma vigente, y que consultarás a un adulto responsable", "Que sí, si usas guantes", "Que sí, pero solo los sacos de arriba", "Leer el plan no habilita para tomar muestras."),
    sc=[
        ("En el laboratorio químico: ¿qué es el muestreo?", "El conjunto de decisiones y registros para obtener una muestra", "Incluye el plan, la toma y el registro."),
        ("En el laboratorio químico: ¿qué es un protocolo?", "Un documento con las reglas aprobadas para hacer una tarea", "Define cómo se hace el trabajo de forma uniforme."),
        ("¿Por qué una muestra no representativa es un problema?", "Porque el análisis no refleja al lote entero", "El resultado puede llevar a decisiones equivocadas."),
    ],
    op=("Plan ficticio del «Laboratorio Demo Costa Norte»: un lote de 50 cajas de un material de ejemplo; se muestrean 5 cajas elegidas al azar; de cada una se reserva una porción de 100 g. Escribe (a) qué porcentaje del lote se muestrea, (b) cuántos gramos suman las porciones, (c) por qué conviene elegir al azar, (d) por qué leer este plan no te habilita para tomar las muestras.",
        "(a) 5 por 100 entre 50 son 10 %. (b) 5 por 100 son 500 g. (c) Para que todas las cajas tengan la misma posibilidad y la muestra refleje al lote. (d) Porque tomar muestras exige formación, autorización y norma vigente.",
        ["calcula el porcentaje", "calcula los gramos", "justifica el azar", "aclara que leer no habilita"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "creer que el plan autoriza", "elegir lo más cómodo"],
        "Pregunta: «¿qué pasa si solo se eligen las cajas más cercanas?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un lote con su número de bultos, decide cuántos muestrear y calcula el porcentaje y los gramos totales.",
    extend="Explica con un ejemplo por qué una muestra contaminada puede hacer rechazar un lote bueno.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (documento de ejemplo, inventado). Registro de muestreo M-0231 del «Laboratorio Demo Valle Claro». Material: «Material A de ejemplo». Lote: L-4821. Fecha y hora de toma: 09:30. Muestreador: personal formado y autorizado. "
     "Muestras simples: 5 porciones de 200 g cada una, de puntos distintos del lote. Con ellas se forma una muestra compuesta (mezcla de las porciones, solo como concepto) de 1.000 g, y se reserva una contramuestra (porción guardada para repetir el análisis si hace falta) de 250 g. "
     "Condición de conservación: ambiente seco. Hora de entrega al laboratorio: 10:15. Plazo máximo de entrega de ejemplo: 2 horas. Firmas: muestreador y receptor.")
build(
    O1, 2, F,
    use="Aprenderé los conceptos y documentos del muestreo: muestra simple y compuesta, contramuestra, cadena de custodia, registro de muestreo y los roles de cada persona.",
    prior=["Sé qué es una muestra representativa.", "Sé calcular porcentajes.", "Sé calcular diferencias de horas."],
    explain=[
        "En el laboratorio químico, una muestra simple es una porción tomada en un punto del lote, y una muestra compuesta se forma juntando varias muestras simples para representar mejor al lote. La contramuestra es una porción que se guarda sin analizar para repetir el análisis si hay dudas. El registro de muestreo es el documento que anota qué material se muestreó, cuándo, quién, cuánto y en qué condición de conservación.",
        "La cadena de custodia es el registro de quién tuvo la muestra en cada momento, desde la toma hasta el análisis, con fecha, hora y firma. Si la cadena se rompe, no se sabe si la muestra mantuvo su integridad. Cada rol tiene su tarea: el muestreador toma y registra, el receptor recibe y firma, el analista analiza y el jefe de laboratorio revisa y autoriza.",
        f"Esta clase trabaja con documentos de ejemplo en papel. {EMER} {AVISO}",
    ],
    vocab=[("muestra simple", "porción tomada en un solo punto del lote"), ("muestra compuesta", "muestra formada juntando varias muestras simples"), ("contramuestra", "porción guardada para repetir el análisis si hace falta"), ("registro de muestreo", "documento que anota qué se muestreó, cuándo, quién, cuánto y en qué condición"), ("cadena de custodia", "registro de quién tuvo la muestra en cada momento"), ("plazo de entrega", "tiempo máximo para llevar la muestra al laboratorio")],
    worked=[
        ("Masa de una compuesta", "Una muestra compuesta de ejemplo se forma con 4 porciones de 150 g. ¿Cuántos gramos tiene?", ["Se multiplica el número de porciones por la masa de cada una.", "4 por 150 son 600."], "600 g"),
        ("Tiempo de entrega", "Una muestra de ejemplo se tomó a las 14:00 y se entregó a las 15:20, con plazo máximo de 2 horas. ¿Cumple?", ["Pasaron 1 hora y 20 minutos.", "1 hora 20 minutos es menos que 2 horas."], "Sí, cumple el plazo"),
    ],
    mistakes=[("Entregar una muestra sin firma ni hora de entrega «porque se entiende quién la trajo».", "Sin firma y hora se rompe la cadena de custodia.", "Registra siempre quién entrega, quién recibe, y fecha y hora."),
              ("Descartar la contramuestra apenas se obtiene un resultado.", "La contramuestra sirve para repetir el análisis si hay dudas.", "Guárdala según el plazo del protocolo.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es una muestra compuesta?", "Una muestra formada juntando varias muestras simples", "Una muestra tomada en un solo punto", "La porción que se guarda sin analizar", "La compuesta reúne varias simples para representar mejor al lote."),
        ("abc", "En el laboratorio químico: ¿qué es una contramuestra?", "Una porción guardada para repetir el análisis si hace falta", "La primera muestra que se analiza", "Una muestra de otro lote", "La contramuestra permite verificar un resultado dudoso."),
        ("abc", "En el laboratorio químico: ¿qué es la cadena de custodia?", "El registro de quién tuvo la muestra en cada momento", "La lista de proveedores del laboratorio", "El orden de los estantes", "La cadena de custodia documenta el recorrido de la muestra."),
        ("=", "{F} ¿Cuántos gramos suman las 5 muestras simples?", "5*200", "Se multiplica el número de porciones por la masa de cada una.", " g"),
        ("=", "{F} ¿Qué porcentaje de la muestra compuesta es la contramuestra?", "250*100//1000", "Se divide la contramuestra entre la compuesta y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos minutos pasaron entre la toma y la entrega al laboratorio?", "(10*60+15)-(9*60+30)", "Se pasan las horas a minutos y se restan.", " minutos"),
        ("abc", "{F} ¿Se cumplió el plazo máximo de entrega de 2 horas?", "Sí, porque pasaron 45 minutos", "No, porque pasaron más de 2 horas", "No, porque la entrega fue de mañana", "45 minutos es menor que 120 minutos."),
        ("abc", "{F} ¿Qué rol recibe y firma la muestra, según los roles del texto?", "El receptor", "El analista", "El jefe de laboratorio", "La ficha asigna la recepción al receptor."),
        ("abc", "{F} ¿Por qué el registro anota que las 5 muestras son de puntos distintos?", "Porque así la compuesta representa mejor al lote", "Porque cada punto tiene un precio distinto", "Porque lo pide el proveedor de los sacos", "Varios puntos reflejan mejor la variación del lote."),
        ("abc", "{F} Si la muestra llegó sin firma del receptor, ¿qué ocurre con la cadena de custodia?", "Queda rota y debe informarse al jefe de laboratorio", "No pasa nada, porque la hora está registrada", "Se completa la firma por cuenta de otra persona", "La cadena exige firma en cada traspaso."),
        ("abc", "{F} Un analista propone botar la contramuestra de 250 g apenas obtenga el resultado. ¿Qué corresponde?", "Conservarla según el plazo del protocolo", "Botarla si el resultado se ve normal", "Usarla para otro lote", "La contramuestra sirve para repetir el análisis si hay dudas."),
        ("=", "{F} Si la contramuestra fuera de 300 g, ¿cuántos gramos quedarían de la compuesta de 1.000 g para analizar?", "1000-300", "Se resta la contramuestra a la compuesta.", " g"),
        em("Revisas un registro de muestreo de ejemplo cuando alguien avisa que se rompió un envase de la zona de recepción de muestras y que hay un olor fuerte.", 1),
    ],
    ctx=("abc", "Un técnico de ejemplo te dice: «Anota que la muestra se entregó a las 09:45, aunque llegó a las 11:50; así cumple el plazo». ¿Qué respondes?", "Que no: el registro debe reflejar la hora real, y el atraso se informa al jefe de laboratorio", "Que sí, si la muestra se ve bien", "Que sí, pero solo esta vez", "Un registro falso rompe la cadena de custodia."),
    sc=[
        ("En el laboratorio químico: ¿para qué sirve la contramuestra?", "Para repetir el análisis si hay dudas", "Permite verificar un resultado dudoso con la misma muestra."),
        ("En el laboratorio químico: ¿qué datos lleva la cadena de custodia?", "Quién, cuándo y con firma", "Cada traspaso de la muestra queda documentado y firmado."),
        ("¿Cómo se calcula la masa de una muestra compuesta de porciones iguales?", "Número de porciones por masa de cada una", "La compuesta reúne y suma todas las porciones simples."),
    ],
    op=("Registro ficticio del «Laboratorio Demo Costa Norte»: 4 muestras simples de 150 g cada una, una contramuestra de 200 g, toma a las 08:10 y entrega a las 09:25, plazo máximo de 2 horas, sin firma del receptor. Escribe (a) la masa total de las muestras simples, (b) si cumple el plazo y cuántos minutos pasaron, (c) qué falla tiene el registro, (d) para qué se guarda la contramuestra.",
        "(a) 4 por 150 son 600 g. (b) Pasaron 75 minutos, menos de 120: cumple. (c) Falta la firma del receptor, así que se rompe la cadena de custodia. (d) Para repetir el análisis si hay dudas.",
        ["calcula la masa", "calcula y compara el tiempo", "detecta la falla del registro", "explica la contramuestra"],
        ["hoja con las cuatro respuestas"],
        ["restar mal las horas", "no ver la firma faltante", "descartar la contramuestra"],
        "Pregunta: «¿quién recibió la muestra y dónde queda su constancia?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Escribe un registro de muestreo de ejemplo con material, lote, hora, porciones y firma.",
    extend="Explica con un ejemplo por qué una cadena de custodia interrumpida invalida un resultado.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Plan de muestreo de ejemplo del «Laboratorio Demo Valle Claro»: se muestrea el 10 % de los bultos del lote, redondeando hacia arriba, y nunca menos de 5 bultos. Los bultos se numeran y se eligen con números sorteados. "
     "Lote A: 120 bultos. Lote B: 30 bultos. Lote C: 85 bultos. Números sorteados para el lote A (de ejemplo): 7; 19; 33; 48; 52; 66; 71; 85; 90; 104; 111; 118. "
     "Bultos 1 a 40 = primer tercio; 41 a 80 = segundo tercio; 81 a 120 = último tercio del lote A.")
build(
    O1, 3, F,
    use="Aprenderé a analizar en papel un plan de muestreo: calcular cuántos bultos muestrear con una regla, comprobar que el sorteo sea representativo y detectar planes con sesgo.",
    prior=["Sé qué es una muestra representativa.", "Sé calcular el 10 % de un número.", "Sé redondear hacia arriba."],
    explain=[
        "En el laboratorio químico, un plan de muestreo es la regla escrita que dice cuántos bultos se muestrean y cómo se eligen. En este cuaderno la regla de ejemplo es muestrear el 10 % de los bultos, redondeando hacia arriba, y nunca menos de 5 bultos. Redondear hacia arriba significa subir al entero siguiente cuando sobra una parte: el 10 % de 85 es 8,5, así que se muestrean 9.",
        "Para que la muestra sea representativa, los bultos se eligen al azar: se numeran y se sortean los números, de modo que todos tengan la misma posibilidad. Un sesgo es una desviación sistemática que hace que la muestra no refleje al lote, como elegir siempre los bultos más cómodos. Se revisa la distribución del sorteo: si todos los números caen en una sola zona del lote, el plan debe repetirse y consultarse al responsable.",
        f"Todo es un ejercicio de planilla y no autoriza a tomar muestras. {EMER} {AVISO}",
    ],
    vocab=[("plan de muestreo", "regla escrita que dice cuántos bultos se muestrean y cómo se eligen"), ("sorteo", "elección al azar de los números de los bultos"), ("sesgo", "desviación sistemática que hace que la muestra no refleje al lote"), ("redondear hacia arriba", "subir al entero siguiente cuando sobra una parte"), ("distribución del sorteo", "cómo se reparten los números sorteados en las zonas del lote")],
    worked=[
        ("Aplicar la regla", "Con la regla de ejemplo, un lote de 60 bultos, ¿cuántos bultos se muestrean?", ["El 10 % de 60 es 6.", "6 es mayor que 5, así que se muestrean 6."], "6 bultos"),
        ("Aplicar el mínimo", "Con la misma regla, un lote de 20 bultos, ¿cuántos se muestrean?", ["El 10 % de 20 es 2.", "Como el mínimo es 5, se muestrean 5."], "5 bultos"),
    ],
    mistakes=[("Redondear hacia abajo cuando el 10 % da un número con decimales.", "La regla dice redondear hacia arriba.", "Sube al entero siguiente, por ejemplo de 8,5 a 9."),
              ("Aceptar un sorteo en que todos los números caen en la parte baja de la pila.", "Esa muestra podría no representar al resto del lote.", "Revisa la distribución y repite el sorteo si hace falta.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es un plan de muestreo?", "La regla escrita que dice cuántos bultos se muestrean y cómo se eligen", "El informe de resultados del análisis", "El lugar donde se guardan las muestras", "El plan fija cantidad y forma de elegir."),
        ("abc", "En el laboratorio químico: ¿qué es un sesgo en el muestreo?", "Una desviación sistemática que hace que la muestra no refleje al lote", "Una muestra más grande de lo normal", "El tiempo que tarda el sorteo", "El sesgo aleja la muestra de lo que representa."),
        ("abc", "En el laboratorio químico: ¿para qué se sortean los números de los bultos?", "Para que todos tengan la misma posibilidad de ser elegidos", "Para elegir los más fáciles de alcanzar", "Para terminar antes sin importar el resultado", "Elegir al azar evita el sesgo en la muestra."),
        ("=", "{F} ¿Cuántos bultos se muestrean en el lote A?", "120*10//100", "Se calcula el 10 % de 120.", " bultos"),
        ("=", "{F} ¿Cuántos bultos se muestrean en el lote B?", "5", "El 10 % de 30 son 3, pero el mínimo es 5.", " bultos"),
        ("=", "{F} ¿Cuántos bultos se muestrean en el lote C? Redondea hacia arriba.", "(85*10+99)//100", "El 10 % de 85 es 8,5 y se redondea hacia arriba a 9.", " bultos"),
        ("abc", "{F} ¿Cuántos números sorteados tiene el lote A?", "12", "10", "15", "El 10 % de 120 son 12 bultos; la lista tiene 12 números."),
        ("=", "{F} ¿Cuántos números sorteados caen en el último tercio del lote A (bultos 81 a 120)?", "5", "Caen el 85, 90, 104, 111 y 118.", " números"),
        ("abc", "{F} ¿Está bien repartido el sorteo del lote A entre los tres tercios?", "Sí: hay números en el primer, el segundo y el último tercio", "No, porque todos están en el último tercio", "No, porque falta el número 1", "Hay números en las tres zonas del lote."),
        ("abc", "{F} Si el sorteo hubiera dado solo los números 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32 y 35, ¿qué corresponde?", "Repetir el sorteo y consultar al responsable, porque todos están en el primer tercio", "Aceptarlo porque son 12 números", "Aceptarlo porque están en orden", "La muestra no representaría al resto del lote."),
        ("=", "{F} Con la misma regla, un lote de 200 bultos, ¿cuántos bultos se muestrean?", "200*10//100", "Se calcula el 10 % de 200.", " bultos"),
        ("abc", "{F} Una persona propone muestrear 3 bultos del lote B «porque el 10 % de 30 es 3». ¿Qué corresponde?", "Muestrear 5, porque la regla fija un mínimo de 5 bultos", "Aceptar 3, porque es el 10 %", "Muestrear 10, porque conviene más", "La regla de ejemplo exige al menos 5 bultos."),
        em("Calculas el plan de muestreo de ejemplo en la oficina del laboratorio cuando alguien avisa que se cayó un envase y que hay humo en la sala de recepción.", 2),
    ],
    ctx=("abc", "Un jefe de ejemplo dice: «Para ahorrar tiempo, usa los 12 bultos de la primera fila en lugar de sortear». ¿Qué respondes?", "Que no, porque esa muestra no sería representativa y el plan exige sorteo", "Que sí, porque el número de bultos es el correcto", "Que sí, si se anota en el registro", "Sin azar, la muestra puede quedar sesgada."),
    sc=[
        ("En el laboratorio químico: ¿qué significa redondear hacia arriba?", "Subir al entero siguiente cuando sobra una parte", "Así se cumple el mínimo exigido por la regla."),
        ("¿Cuántos bultos se muestrean de un lote de 40 con la regla de ejemplo?", "5 bultos", "El 10 % de 40 son 4, pero el mínimo es 5."),
        ("En el laboratorio químico: ¿qué se hace si el sorteo cae en una sola zona?", "Se repite y se consulta al responsable", "Así se evita un sesgo y la muestra sigue siendo representativa."),
    ],
    op=("Plan ficticio del «Laboratorio Demo Costa Norte» con la regla de la clase (10 % de los bultos, redondeo hacia arriba, mínimo 5). Lote P: 70 bultos. Lote Q: 33 bultos. Lote R: 12 bultos. Sorteo del lote P: 5; 12; 20; 31; 40; 52; 66. Escribe (a) cuántos bultos se muestrean en cada lote, (b) si el sorteo del lote P cubre todo el lote, (c) una razón para elegir al azar, (d) qué harías si el sorteo cayera solo en los primeros 20 bultos.",
        "(a) P: 7; Q: 5 (el 10 % es 3,3 y el mínimo es 5); R: 5. (b) Sí, hay números de la parte baja a la alta del lote. (c) Para que todos los bultos tengan la misma posibilidad y evitar el sesgo. (d) Repetir el sorteo y consultar al responsable.",
        ["aplica la regla en cada lote", "revisa la distribución", "justifica el azar", "propone la acción ante un sorteo sesgado"],
        ["hoja con las cuatro respuestas"],
        ["redondear hacia abajo", "olvidar el mínimo", "aceptar un sorteo concentrado"],
        "Pregunta: «¿cuál es el mínimo y cuándo se aplica?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Aplica la regla a tres lotes inventados y revisa un sorteo de números.",
    extend="Explica con un ejemplo por qué un plan con mínimo de bultos protege a los lotes pequeños.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada). Lote de ejemplo de 2.000 kg en 80 bultos de 25 kg del «Laboratorio Demo Valle Claro». Regla del plan: se muestrea el 10 % de los bultos y de cada bulto muestreado se reserva una muestra simple de 250 g. "
     "Con ellas se forma una muestra compuesta que se reparte en 4 porciones iguales: una para análisis, una contramuestra, una de retención y una para el cliente. Costo de ejemplo del análisis: $15.000 por porción analizada, con 2 repeticiones por análisis. "
     "La contramuestra se conserva 90 días (de ejemplo) y han pasado 62 días.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar criterios de muestreo con datos de ejemplo: calcular bultos y masa de muestra, repartir la compuesta, estimar costos de análisis y controlar el plazo de conservación.",
    prior=["Sé qué es una muestra compuesta y una contramuestra.", "Sé calcular el 10 % de un número.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "En el laboratorio químico, los cálculos de un plan de muestreo ordenan el trabajo antes de empezar. Primero se calcula cuántos bultos se muestrean (aquí, el 10 % del total). Luego se calcula la masa de la muestra compuesta multiplicando los bultos muestreados por la masa de cada muestra simple, y se reparte entre las porciones que exige el protocolo.",
        "Una repetición, o réplica, es repetir el análisis sobre la misma muestra para comprobar que el resultado se repite; por eso el costo de un análisis puede incluir varias repeticiones. Las porciones guardadas, como la contramuestra y la retención, se conservan durante un plazo fijado por el protocolo; para saber cuántos días quedan, se resta lo transcurrido al plazo total. Los cálculos se hacen con números enteros exactos.",
        f"Estos cálculos son de planilla; el muestreo real lo hace personal formado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("réplica", "repetición del análisis sobre la misma muestra"), ("muestra de retención", "porción guardada como respaldo durante un plazo"), ("porción", "parte de la muestra compuesta que se separa para un fin"), ("plazo de conservación", "tiempo durante el cual se guarda una porción"), ("costo de análisis", "valor de analizar una porción, incluidas sus repeticiones")],
    worked=[
        ("Masa de la compuesta", "Un plan de ejemplo muestrea 6 bultos y reserva 300 g de cada uno. ¿Cuántos gramos tiene la compuesta?", ["Se multiplican los bultos por la masa de cada muestra simple.", "6 por 300 son 1.800."], "1.800 g"),
        ("Plazo restante", "Una contramuestra de ejemplo se conserva 120 días y han pasado 85. ¿Cuántos días quedan?", ["Se resta lo transcurrido al plazo.", "120 menos 85 son 35."], "35 días"),
    ],
    mistakes=[("Calcular el 10 % de los kg y no de los bultos.", "La regla se aplica a los bultos, no a los kilos.", "Cuenta los bultos y calcula el 10 % de esa cantidad."),
              ("Olvidar las repeticiones al calcular el costo del análisis.", "Cada repetición también se paga y se registra.", "Multiplica el costo por porción por las repeticiones.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es una réplica de un análisis?", "La repetición del análisis sobre la misma muestra", "Una muestra de otro lote", "El informe del análisis", "Las réplicas comprueban que el resultado se repite."),
        ("abc", "En el laboratorio químico: ¿qué es la muestra de retención?", "Una porción guardada como respaldo durante un plazo", "La porción que se consume en el análisis", "Una muestra que se envía al cliente", "La retención queda guardada por si se necesita después."),
        ("abc", "En el laboratorio químico: ¿cómo se obtiene la masa de una muestra compuesta de porciones iguales?", "Multiplicando los bultos muestreados por la masa de cada porción", "Dividiendo los kg del lote entre 10", "Sumando los kg de los bultos del lote", "La compuesta es la suma de las muestras simples."),
        ("=", "{F} ¿Cuántos bultos se muestrean?", "80*10//100", "Se calcula el 10 % de los 80 bultos.", " bultos"),
        ("=", "{F} ¿Cuántos gramos tiene la muestra compuesta?", "8*250", "Se multiplican los bultos muestreados por la masa de cada muestra simple.", " g"),
        ("=", "{F} ¿Cuántos gramos tiene cada una de las 4 porciones?", "2000//4", "Se divide la compuesta entre las 4 porciones.", " g"),
        ("=", "{F} ¿Cuánto cuesta el análisis de la porción para análisis, con 2 repeticiones?", "15000*2", "Se multiplica el costo por las repeticiones.", " pesos"),
        ("=", "{F} ¿Cuántos días le quedan a la contramuestra para cumplir su plazo de conservación?", "90-62", "Se resta lo transcurrido al plazo total.", " días"),
        ("abc", "{F} ¿Qué parte del lote representa la muestra compuesta de 2 kg frente a los 2.000 kg?", "Una milésima parte: 1 kg de cada 1.000 kg", "Una décima parte, porque se muestrea el 10 % de los bultos", "Una cuarta parte, porque se reparte en 4 porciones", "Son 2 kg de 2.000 kg: una cantidad muy pequeña que debe ser representativa."),
        ("=", "{F} Si el cliente pide una quinta porción igual, ¿cuántos gramos tendría que haber en la compuesta para mantener 500 g por porción?", "5*500", "Se multiplican las porciones por la masa de cada una.", " g"),
        ("abc", "{F} Un compañero dice: «si el 10 % de 80 es 8 bultos, entonces 8 kg bastan para la muestra». ¿Qué corresponde?", "Corregir: son 8 muestras simples de 250 g, no 8 kg", "Aceptarlo porque 8 es el 10 %", "Aceptarlo si los bultos están rotulados", "La regla pide 250 g por bulto muestreado, no 1 kg."),
        ("=", "{F} ¿Cuánto costaría analizar las 4 porciones con 2 repeticiones cada una?", "4*15000*2", "Se multiplican porciones, costo por porción y repeticiones.", " pesos"),
        em("Revisas la planilla del plan de muestreo cuando alguien avisa que una de las muestras de retención se volcó en el estante y que sale un olor irritante.", 3),
    ],
    ctx=("abc", "Un jefe de ejemplo propone no guardar la contramuestra «para ahorrar espacio» aunque el plazo de conservación no ha vencido. ¿Qué respondes?", "Que debe guardarse hasta cumplir el plazo del protocolo", "Que sí, si el resultado salió normal", "Que sí, si el cliente no la pidió", "La contramuestra respalda el resultado durante todo su plazo."),
    sc=[
        ("En el laboratorio químico: ¿qué se multiplica para obtener los gramos de la compuesta?", "Bultos muestreados por masa de cada porción", "La compuesta suma las porciones simples."),
        ("En el laboratorio químico: ¿qué es una réplica?", "La repetición del análisis sobre la misma muestra", "Sirve para comprobar que el resultado se repite."),
        ("¿Cómo se calcula cuántos días quedan de un plazo?", "Plazo total menos días transcurridos", "La resta indica lo que falta."),
    ],
    op=("Planilla ficticia del «Laboratorio Demo Costa Norte»: lote de 60 bultos de 20 kg; se muestrea el 10 % de los bultos y de cada uno se reserva una muestra simple de 200 g; la compuesta se reparte en 3 porciones iguales; análisis de $12.000 por porción con 2 repeticiones; contramuestra con plazo de 60 días, 28 transcurridos. Escribe (a) cuántos bultos se muestrean, (b) los gramos de la compuesta y de cada porción, (c) el costo de analizar una porción, (d) los días que le quedan a la contramuestra.",
        "(a) 6 bultos. (b) 6 por 200 son 1.200 g y cada porción es de 400 g. (c) 12.000 por 2 son 24.000 pesos. (d) 60 menos 28 son 32 días.",
        ["calcula los bultos", "calcula las masas", "calcula el costo con repeticiones", "calcula el plazo restante"],
        ["hoja con los cuatro cálculos"],
        ["calcular el 10 % de los kg", "olvidar las repeticiones", "restar al revés"],
        "Pregunta: «¿a qué se aplica el 10 %?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un lote con bultos, calcula el muestreo del 10 % y el costo de analizar una porción con repeticiones.",
    extend="Explica con un ejemplo por qué el plazo de conservación de una contramuestra debe estar escrito en el protocolo.",
)

# ============================================================ OAM-01, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Dos planes para muestrear un lote de 100 bultos en el «Laboratorio Demo Valle Claro». Plan A: sorteo de 10 bultos repartidos en todo el lote, tiempo de ejemplo 60 minutos, costo de ejemplo $20.000. "
     "Plan B: tomar 2 bultos de la capa superior de la pila, tiempo 15 minutos, costo $5.000. Condición obligatoria de ejemplo: la muestra debe ser representativa. "
     "Lista de control de un registro de muestreo, 6 puntos: (1) material y lote; (2) fecha y hora; (3) responsable; (4) cantidad; (5) condición de conservación; (6) firmas. Se revisaron 20 registros: 15 cumplen los 6 puntos, 3 no tienen firma y 2 no tienen hora.")
build(
    O1, 5, F,
    use="Aprenderé a comparar planes de muestreo con una condición obligatoria de representatividad, tiempo y costo, y a verificar la calidad de los registros de muestreo con una lista de control.",
    prior=["Sé qué es una muestra representativa.", "Sé calcular porcentajes.", "Sé qué es una condición obligatoria."],
    explain=[
        "En el laboratorio químico, comparar planes de muestreo exige mirar primero las condiciones obligatorias: un plan que no produce muestras representativas se descarta aunque sea más rápido o más barato. Entre los planes que sí cumplen, se compara el tiempo y el costo. Un plan barato con muestras no representativas termina saliendo caro, porque lleva a decisiones equivocadas sobre el lote.",
        "Verificar la calidad de los registros es revisar con una lista de control que cada uno tenga todos los datos exigidos. El porcentaje de cumplimiento se calcula dividiendo los registros que cumplen todo entre los revisados, por 100. Los registros incompletos se informan al jefe de laboratorio y se completan solo con respaldo, nunca por suposición.",
        f"Todo es análisis en papel; el muestreo real es tarea de personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("condición obligatoria", "requisito que un plan debe cumplir para poder elegirse"), ("lista de control", "tabla de puntos que se marcan como cumple o no cumple"), ("registro incompleto", "registro al que le falta un dato exigido"), ("decisión equivocada", "decisión tomada a partir de datos que no reflejan al lote")],
    worked=[
        ("Descartar un plan", "Un plan de ejemplo muestrea solo la primera fila de un lote y cuesta la mitad. ¿Se elige?", ["La representatividad es una condición obligatoria.", "Una sola fila no refleja al lote, así que se descarta."], "No, se descarta"),
        ("Porcentaje de registros completos", "De 25 registros de ejemplo, 20 cumplen todos los puntos. ¿Qué porcentaje cumple?", ["Se divide 20 entre 25 y se multiplica por 100.", "20 por 100 son 2.000, y 2.000 entre 25 son 80."], "80 %"),
    ],
    mistakes=[("Elegir el plan más rápido y barato sin revisar si la muestra será representativa.", "Una muestra no representativa invalida el análisis.", "Aplica primero la condición obligatoria y compara después costo y tiempo."),
              ("Completar de memoria la hora que falta en un registro de muestreo.", "Un dato inventado rompe la trazabilidad.", "Informa lo que falta y completa solo con respaldo.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué se hace con un plan que no produce muestras representativas?", "Se descarta, aunque sea más rápido o barato", "Se elige si es el más barato", "Se elige si tiene menos bultos", "La representatividad es una condición obligatoria."),
        ("abc", "En el laboratorio químico: ¿qué es un registro incompleto?", "Uno al que le falta un dato exigido", "Uno que es muy largo", "Uno firmado por el jefe", "El registro incompleto debe informarse y completarse con respaldo."),
        ("abc", "En el laboratorio químico: ¿para qué sirve la lista de control de registros?", "Para revisar punto por punto si cada registro cumple lo exigido", "Para decidir qué bultos se muestrean", "Para calcular el costo del análisis", "La lista ordena la revisión de calidad."),
        ("=", "{F} ¿Cuántos minutos más toma el plan A que el plan B?", "60-15", "Se resta el tiempo del plan B al del plan A.", " minutos"),
        ("=", "{F} ¿Cuántos pesos más cuesta el plan A que el B?", "20000-5000", "Se resta el costo del plan B al del plan A.", " pesos"),
        ("abc", "{F} ¿Por qué el plan B no cumple la condición obligatoria?", "Porque 2 bultos de la capa superior no representan a todo el lote", "Porque su costo es muy bajo", "Porque tarda menos de una hora", "La muestra solo refleja la capa de arriba."),
        ("abc", "{F} ¿Qué plan conviene elegir y por qué?", "El A, porque cumple la representatividad aunque cueste más", "El B, porque es más barato", "El B, porque es más rápido", "Entre los que cumplen la condición obligatoria, solo queda el A."),
        ("=", "{F} ¿Qué porcentaje de los 20 registros revisados cumple los 6 puntos?", "15*100//20", "Se dividen los registros que cumplen entre los revisados y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos registros tienen algún punto incumplido?", "3+2", "Se suman los que no tienen firma y los que no tienen hora.", " registros"),
        ("abc", "{F} ¿Qué corresponde con los 3 registros sin firma?", "Informarlos al jefe de laboratorio para completar con respaldo", "Firmarlos otra persona para cerrar la lista", "Archivarlos porque cumplen 5 de 6 puntos", "Un registro sin firma no se completa por suposición."),
        ("=", "{F} Si los 5 registros incompletos se corrigen con respaldo, ¿cuántos de los 20 cumplirían los 6 puntos?", "15+5", "Se suman los que cumplían y los que se corrigen.", " registros"),
        ("abc", "{F} Una jefatura dice: «usemos el plan B este mes y el A el mes siguiente, para mezclar». ¿Qué corresponde?", "Rechazarlo: el plan B no es representativo en ningún mes", "Aceptarlo si el precio es menor", "Aceptarlo si las muestras están rotuladas", "Un plan que no cumple la condición obligatoria no se usa."),
        em("Comparas planes de muestreo en la oficina del laboratorio cuando alguien avisa que un envase con muestras se cayó y que sale humo de la zona de almacenamiento.", 4),
    ],
    ctx=("abc", "Un proveedor de ejemplo dice: «No hace falta sortear; analice solo los sacos que le entrego en la puerta». ¿Qué respondes?", "Que no, porque esa muestra no sería representativa del lote", "Que sí, si los sacos están bien rotulados", "Que sí, para ahorrar tiempo", "Una muestra elegida por quien entrega el lote puede estar sesgada."),
    sc=[
        ("En el laboratorio químico: ¿qué condición obligatoria debe cumplir un plan de muestreo?", "Producir muestras representativas", "Sin eso, el análisis no refleja al lote."),
        ("En el laboratorio químico: ¿cómo se calcula el porcentaje de cumplimiento?", "Registros que cumplen entre revisados, por 100", "Es una proporción expresada en porcentaje."),
        ("¿Se completan de memoria los datos faltantes de un registro?", "No, se informa y se corrige con respaldo", "Los datos inventados rompen la trazabilidad."),
    ],
    op=("Caso ficticio del «Laboratorio Demo Costa Norte»: lote de 60 bultos. Plan X: sorteo de 6 bultos en todo el lote, 40 minutos, $10.000. Plan Y: muestrear 2 bultos de la entrada, 10 minutos, $3.000. De 10 registros revisados, 8 cumplen los puntos y 2 no tienen firma. Escribe (a) qué plan se descarta y por qué, (b) cuántos pesos más cuesta el plan elegido, (c) el porcentaje de registros que cumple, (d) qué harías con los 2 registros incompletos.",
        "(a) Se descarta Y, porque no es representativo. (b) 10.000 menos 3.000 son 7.000 pesos. (c) 80 %. (d) Informarlos al jefe de laboratorio y completarlos con respaldo.",
        ["descarta por la condición obligatoria", "calcula la diferencia de costo", "calcula el porcentaje", "propone la acción correcta"],
        ["hoja con las cuatro respuestas"],
        ["elegir por precio", "completar firmas sin respaldo", "no informar"],
        "Pregunta: «¿qué plan refleja a todo el lote?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Compara dos planes de muestreo inventados en una tabla de representatividad, tiempo y costo.",
    extend="Explica con un ejemplo por qué ahorrar en el muestreo puede costar más a la empresa.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). En un día llegan 12 muestras al «Laboratorio Demo Valle Claro»: 5 de materia prima (MP), 4 de producto intermedio (PI) y 3 de producto final (PF). 3 de las 12 requieren conservación refrigerada y 9 se guardan a temperatura ambiente; 2 son urgentes (resultado el mismo día). "
     "Rótulo mínimo de ejemplo: código único, descripción, fecha y hora, responsable y condición de conservación. Peligros anotados: muestra sin rótulo, envase roto y etiqueta despegada. Matriz de ejemplo: puntaje de riesgo = probabilidad × gravedad. "
     "Muestra sin rótulo: probabilidad 4 y gravedad 3. Envase roto: probabilidad 2 y gravedad 4. Etiqueta despegada: probabilidad 3 y gravedad 2.")
build(
    O2, 1, F,
    use="Aprenderé por qué se clasifican y se rotulan las muestras y los insumos de un laboratorio, qué datos lleva un rótulo mínimo y qué riesgos tiene un rótulo faltante o ilegible.",
    prior=["Sé qué es una muestra y la cadena de custodia.", "Sé calcular porcentajes.", "Sé qué es un peligro y un riesgo."],
    explain=[
        "En el laboratorio químico, clasificar es agrupar las muestras y los insumos según criterios: tipo (materia prima, producto intermedio o producto final), urgencia, condición de conservación y peligro. Rotular es identificar cada una con una etiqueta legible y duradera. Los insumos son los materiales y productos que el laboratorio usa en sus análisis; sus envases traen el rótulo del fabricante, que no se tapa ni se cambia. Sin clasificación y rótulo, las muestras se confunden y los resultados dejan de ser confiables.",
        "El rótulo mínimo de ejemplo lleva código único, descripción, fecha y hora, responsable y condición de conservación. La trazabilidad es poder seguir una muestra desde que llega hasta que se informa su resultado, y depende del rótulo y de la cadena de custodia. La hoja de datos de seguridad del fabricante informa los peligros de un insumo y se lee, no se interpreta por cuenta propia.",
        f"Esta clase es de papel: manipular muestras y reactivos exige formación y autorización. {EMER} {AVISO}",
    ],
    vocab=[("clasificar", "agrupar muestras o insumos según criterios como tipo, urgencia y conservación"), ("rotular", "identificar cada muestra o insumo con una etiqueta legible y duradera"), ("insumo", "material o producto que el laboratorio usa en sus análisis"), ("rótulo mínimo", "datos básicos de la etiqueta: código, descripción, fecha y hora, responsable y conservación"), ("código único", "identificador que no se repite entre muestras"), ("trazabilidad", "posibilidad de seguir una muestra desde que llega hasta su resultado")],
    worked=[
        ("Contar por categoría", "En un día de ejemplo llegan 7 muestras de materia prima y 5 de producto final. ¿Cuántas muestras llegan en total?", ["Se suman las dos categorías.", "7 más 5 son 12."], "12 muestras"),
        ("Porcentaje de conservación", "De 20 muestras de ejemplo, 5 requieren conservación refrigerada. ¿Qué porcentaje es?", ["Se divide 5 entre 20 y se multiplica por 100.", "5 por 100 son 500, y 500 entre 20 son 25."], "25 %"),
    ],
    mistakes=[("Rotular una muestra solo con «muestra 1».", "No dice qué es, cuándo llegó ni quién la recibió; se puede confundir.", "Usa el rótulo mínimo completo."),
              ("Tapar el rótulo del fabricante de un insumo con una etiqueta propia.", "Se pierden los pictogramas y datos de peligro del fabricante.", "Agrega tu etiqueta sin cubrir el rótulo original.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué significa clasificar las muestras?", "Agruparlas según criterios como tipo, urgencia y conservación", "Mezclarlas para analizarlas juntas", "Botar las que no son urgentes", "Clasificar es agrupar con criterios definidos."),
        ("abc", "En el laboratorio químico: ¿para qué sirve un código único en el rótulo?", "Para que ninguna muestra se confunda con otra", "Para que todas las muestras tengan el mismo código", "Para reemplazar la fecha", "Un código único identifica a cada muestra sin repetirse."),
        ("abc", "En el laboratorio químico: ¿qué es un insumo?", "Un material o producto que el laboratorio usa en sus análisis", "Una muestra que llega del cliente", "El informe del resultado", "Los insumos se usan en el trabajo del laboratorio."),
        ("=", "{F} ¿Cuántas muestras llegaron en total?", "5+4+3", "Se suman las muestras de materia prima, producto intermedio y producto final.", " muestras"),
        ("=", "{F} ¿Qué porcentaje de las muestras requiere conservación refrigerada?", "3*100//12", "Se divide las refrigeradas entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas muestras se guardan a temperatura ambiente?", "12-3", "Se resta las refrigeradas al total.", " muestras"),
        ("abc", "{F} Según la matriz, ¿qué peligro tiene el mayor puntaje de riesgo?", "La muestra sin rótulo, con 12 puntos", "El envase roto, con 8 puntos", "La etiqueta despegada, con 6 puntos", "Se compara probabilidad por gravedad de cada peligro."),
        ("=", "{F} ¿Qué puntaje de riesgo tiene el envase roto?", "2*4", "Se multiplica la probabilidad por la gravedad.", " puntos"),
        ("abc", "{F} Una muestra llega sin rótulo. ¿Qué corresponde?", "No analizarla hasta identificarla con documentos y avisar al responsable", "Rotularla según lo que parezca", "Abrirla para ver qué es y luego rotularla", "Una muestra sin identificar no se analiza ni se abre."),
        ("abc", "{F} ¿Por qué las 2 muestras urgentes se identifican y rotulan primero?", "Porque su resultado se necesita el mismo día", "Porque son las más baratas", "Porque no necesitan rótulo completo", "La urgencia fija el orden de atención, no reduce los datos del rótulo."),
        ("abc", "{F} Un compañero tapa con una etiqueta propia el rótulo del fabricante de un insumo. ¿Qué corresponde?", "Corregirlo: no se cubre el rótulo original, porque trae datos de peligro", "Dejarlo si la etiqueta propia es más clara", "Dejarlo si el insumo es de uso diario", "El rótulo del fabricante debe quedar visible."),
        ("=", "{F} Si 6 de las 12 muestras llegaron con la etiqueta despegada, ¿qué porcentaje de las muestras es?", "6*100//12", "Se divide las muestras con etiqueta despegada entre el total y se multiplica por 100.", " %"),
        em("Clasificas muestras de ejemplo en el laboratorio cuando alguien avisa que un envase se rompió y que hay un olor fuerte y vapores en la mesa de recepción.", 0),
    ],
    ctx=("abc", "Un técnico de ejemplo te dice: «Pon el mismo rótulo a las dos muestras, son casi iguales». ¿Qué respondes?", "Que no, porque cada muestra necesita un código único para no confundirse", "Que sí, si llegaron a la misma hora", "Que sí, si son del mismo cliente", "Dos muestras con el mismo rótulo no se pueden distinguir."),
    sc=[
        ("En el laboratorio químico: ¿qué datos lleva el rótulo mínimo de ejemplo?", "Código único, descripción, fecha y hora, responsable y conservación", "Son los datos básicos para identificar la muestra."),
        ("En el laboratorio químico: ¿qué es la trazabilidad de una muestra?", "Poder seguirla desde que llega hasta su resultado", "Depende del rótulo y de la cadena de custodia."),
        ("¿Qué se hace con una muestra sin rótulo?", "No se analiza y se avisa al responsable", "Sin identificación no se puede confiar en el resultado."),
    ],
    op=("Caso ficticio del «Laboratorio Demo Costa Norte»: llegan 10 muestras, 4 de materia prima, 3 de producto intermedio y 3 de producto final; 2 requieren refrigeración; una llega sin rótulo y otra con la hora ilegible. Escribe (a) cuántas muestras llegan de cada tipo y en total, (b) qué porcentaje es refrigerado, (c) qué haces con la muestra sin rótulo, (d) qué datos mínimos debe llevar cada rótulo.",
        "(a) 4 de materia prima, 3 de producto intermedio y 3 de producto final: 10 en total. (b) 2 por 100 entre 10 son 20 %. (c) No se analiza, se identifica con documentos y se avisa al responsable. (d) Código único, descripción, fecha y hora, responsable y condición de conservación.",
        ["cuenta por categoría", "calcula el porcentaje", "describe la conducta ante la muestra sin rótulo", "nombra los datos del rótulo"],
        ["hoja con las cuatro respuestas"],
        ["rotular por suposición", "no calcular el porcentaje", "olvidar la fecha y hora"],
        "Pregunta: «¿qué dato permite distinguir una muestra de otra?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa un día de recepción con cinco muestras, clasifícalas por tipo y conservación y escribe un rótulo mínimo.",
    extend="Explica con un ejemplo por qué confundir dos muestras puede cambiar la decisión sobre un lote.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 2 (documento de ejemplo, inventado). Rótulo de ejemplo: Código PI-0234; descripción: producto intermedio, línea 2; fecha y hora: 14 de mayo de ejemplo, 11:40; responsable: analista de recepción; conservación: refrigerada; estado: recibida. "
     "Estados posibles de una muestra: recibida, en análisis, analizada y descartada. Registro de recepción del día: 8 muestras recibidas, de las cuales 6 tienen el rótulo completo y 2 tienen algún dato faltante. "
     "Roles de ejemplo: el receptor recibe, rotula y firma; el analista analiza; el jefe de laboratorio revisa y autoriza; el cliente entrega la muestra. Una etiqueta indeleble es la que no se borra ni se corre con el uso o el agua.")
build(
    O2, 2, F,
    use="Aprenderé los documentos y roles de la identificación de muestras: rótulo, registro de recepción, estados de una muestra, etiqueta indeleble y responsabilidades de cada persona.",
    prior=["Sé qué es un rótulo mínimo y un código único.", "Sé calcular porcentajes.", "Sé qué es la cadena de custodia."],
    explain=[
        "En el laboratorio químico, el registro de recepción es el documento donde se anota cada muestra que llega, con su rótulo, la hora, quién la entregó y quién la recibió. El estado de una muestra indica en qué etapa está: recibida, en análisis, analizada o descartada, y se actualiza cada vez que cambia. Una etiqueta indeleble es la que no se borra ni se corre por la humedad o el roce, y por eso es la adecuada para rotular.",
        "Cada rol tiene una función: el receptor recibe, rotula y firma; el analista analiza; el jefe de laboratorio revisa y autoriza; el cliente entrega la muestra. Los datos del rótulo y del registro deben ser iguales: si no coinciden, hay un error de transcripción que se corrige tachando con una línea, anotando el valor correcto, la fecha y la firma. Los rótulos no se sobrescriben ni se borran.",
        f"Se trabaja con documentos de ejemplo; manipular muestras exige formación. {EMER} {AVISO}",
    ],
    vocab=[("registro de recepción", "documento donde se anota cada muestra que llega"), ("estado de una muestra", "etapa en que está: recibida, en análisis, analizada o descartada"), ("etiqueta indeleble", "etiqueta que no se borra ni se corre con el uso"), ("error de transcripción", "error al copiar un dato de un documento a otro"), ("receptor", "persona que recibe, rotula y firma la muestra")],
    worked=[
        ("Porcentaje de rótulos completos", "De 10 muestras de ejemplo, 8 tienen rótulo completo. ¿Qué porcentaje es?", ["Se divide 8 entre 10 y se multiplica por 100.", "8 por 100 son 800, y 800 entre 10 son 80."], "80 %"),
        ("Estado de una muestra", "Una muestra de ejemplo ya fue analizada y el informe se emitió. Antes estaba «en análisis». ¿Qué estado corresponde ahora?", ["Los estados son recibida, en análisis, analizada y descartada.", "El análisis terminó, así que corresponde «analizada»."], "Analizada"),
    ],
    mistakes=[("Rotular con lápiz de mina o con tinta que se corre.", "El rótulo puede borrarse y la muestra queda sin identificar.", "Usa etiquetas indelebles."),
              ("No actualizar el estado de una muestra cuando cambia de etapa.", "El registro deja de reflejar la realidad y se pierde la trazabilidad.", "Actualiza el estado en cada cambio, con fecha y firma.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es un registro de recepción?", "El documento donde se anota cada muestra que llega", "El informe final del análisis", "La lista de precios de los análisis", "El registro de recepción deja constancia de lo que llega."),
        ("abc", "En el laboratorio químico: ¿qué es una etiqueta indeleble?", "Una etiqueta que no se borra ni se corre con el uso", "Una etiqueta de colores", "Una etiqueta que se puede reescribir", "Indeleble significa que no se borra."),
        ("abc", "En el laboratorio químico: ¿qué indica el estado de una muestra?", "La etapa en que está, como recibida o en análisis", "El precio del análisis", "El nombre del cliente", "El estado muestra en qué etapa va la muestra."),
        ("abc", "{F} ¿Qué dato del rótulo identifica la muestra de manera única?", "El código PI-0234", "La descripción «línea 2»", "La conservación refrigerada", "El código no se repite entre muestras."),
        ("abc", "{F} ¿Qué estado tiene la muestra del rótulo?", "Recibida", "Analizada", "Descartada", "El rótulo anota el estado «recibida»."),
        ("=", "{F} ¿Cuántas muestras tienen algún dato faltante en el registro de recepción?", "8-6", "Se resta las completas al total.", " muestras"),
        ("=", "{F} ¿Qué porcentaje de las muestras tiene el rótulo completo?", "6*100//8", "Se divide las completas entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Quién recibe, rotula y firma la muestra?", "El receptor", "El cliente", "El analista", "Según los roles, esa es la tarea del receptor."),
        ("abc", "{F} Un receptor rotuló con lápiz de mina porque no encontró la tinta. ¿Qué corresponde?", "Rotular con etiqueta indeleble antes de guardar la muestra", "Dejarlo así si la muestra es de poco valor", "Dejarlo y avisar al día siguiente", "El rótulo debe resistir el uso sin borrarse."),
        ("abc", "{F} Un registro de recepción de ejemplo anota que la muestra PI-0234 llegó a las 11:04, pero el rótulo de la ficha dice 11:40. ¿Qué corresponde?", "Detectar el error de transcripción y corregirlo tachando con una línea, anotando el valor correcto, fecha y firma", "Borrar uno de los dos con corrector", "Dejarlo así porque la diferencia es pequeña", "La corrección debe dejar visible el valor original y quién corrigió."),
        ("abc", "{F} El analista cambia el estado a «en análisis». ¿Qué debe hacer también?", "Dejar constancia con fecha y firma", "Borrar el estado anterior", "Pedir al cliente que lo firme", "Cada cambio de estado se registra con responsable."),
        ("=", "{F} Si las 2 muestras con datos faltantes se corrigen con respaldo, ¿cuántas de las 8 tendrán rótulo completo?", "6+2", "Se suman las completas y las corregidas.", " muestras"),
        em("Revisas un registro de recepción cuando alguien avisa que el refrigerador de muestras se está incendiando y que sale humo de la sala.", 1),
    ],
    ctx=("abc", "Una compañera de ejemplo propone borrar con corrector un código equivocado del registro y escribir el correcto encima. ¿Qué respondes?", "Que no: se tacha con una línea, se escribe el correcto, con fecha y firma", "Que sí, porque queda más limpio", "Que sí, si nadie lo ve", "El registro no se borra: la corrección debe dejar traza."),
    sc=[
        ("En el laboratorio químico: ¿qué debe tener una etiqueta para rotular?", "Ser indeleble y legible", "Si se borra, la muestra queda sin identificar."),
        ("En el laboratorio químico: ¿cómo se corrige un dato del registro?", "Se tacha con una línea y se anota el valor correcto con fecha y firma", "La corrección conserva visible el valor original."),
        ("¿Quién recibe, rotula y firma la muestra?", "El receptor", "Esa es su función dentro del flujo."),
    ],
    op=("Registro ficticio del «Laboratorio Demo Costa Norte»: 5 muestras recibidas; el rótulo de la muestra PF-0121 dice 10:15, pero el registro dice 10:51; una muestra tiene la etiqueta escrita con lápiz de mina; 3 muestras tienen todo completo. Escribe (a) qué porcentaje de las muestras está completo, (b) cómo corregirías la hora, (c) qué harías con el rótulo de lápiz, (d) qué rol firma la recepción.",
        "(a) 3 por 100 entre 5 son 60 %. (b) Tachar con una línea el valor errado, anotar el correcto con fecha y firma. (c) Reemplazarlo por una etiqueta indeleble sin perder los datos. (d) El receptor.",
        ["calcula el porcentaje", "describe la corrección con traza", "propone etiqueta indeleble", "nombra el rol"],
        ["hoja con las cuatro respuestas"],
        ["borrar con corrector", "dejar el lápiz", "no nombrar el rol"],
        "Pregunta: «¿cómo quedará visible el dato original?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Escribe un rótulo de ejemplo con los seis datos y un registro de recepción de cuatro muestras.",
    extend="Explica con un ejemplo por qué el estado de la muestra debe actualizarse siempre.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Lista de muestras recibidas en el «Laboratorio Demo Valle Claro» (cada una debe tener código único, hora, firma del receptor y etiqueta legible): "
     "1) MP-001, refrigerada, 08:00, firmada. 2) MP-002, ambiente, 08:05, firmada. 3) PI-003, refrigerada, sin hora, firmada. 4) PI-003, ambiente, 08:20, firmada (el código se repite con la muestra 3). "
     "5) PF-005, ambiente, 08:30, sin firma. 6) PF-006, refrigerada, 08:40, firmada, con la etiqueta ilegible porque la tinta se corrió. 7) MP-007, ambiente, 08:50, firmada. 8) MP-008, ambiente, 09:00, firmada.")
build(
    O2, 3, F,
    use="Aprenderé a analizar una lista de muestras recibidas: detectar rótulos incompletos, códigos repetidos y etiquetas ilegibles, decidir qué problema compromete más la trazabilidad e informar sin corregir de memoria.",
    prior=["Sé qué lleva un rótulo mínimo.", "Sé calcular porcentajes.", "Sé qué es un código único."],
    explain=[
        "En el laboratorio químico, revisar una lista de muestras recibidas es comparar cada una con los requisitos: código único, hora, firma del receptor y etiqueta legible. Una muestra con algún requisito incumplido es una no conformidad. Las no conformidades no se resuelven por suposición: se anotan, se informa al jefe de laboratorio y se corrigen con respaldo, como el documento de entrega o la verificación del cliente.",
        "No todos los problemas pesan igual. Un código repetido es muy grave, porque dos muestras diferentes ya no se pueden distinguir y un resultado podría asignarse a la muestra equivocada. Una etiqueta ilegible o una firma que falta también comprometen la trazabilidad, pero se pueden resolver con respaldo. Mientras no se resuelvan, las muestras involucradas no se analizan.",
        f"Todo se resuelve en papel. {EMER} {AVISO}",
    ],
    vocab=[("no conformidad", "incumplimiento de un requisito del rótulo o del registro"), ("código repetido", "mismo código en dos muestras distintas"), ("etiqueta ilegible", "etiqueta que no se puede leer"), ("respaldo", "documento o verificación que permite corregir un dato sin inventarlo"), ("muestra retenida", "muestra que no se analiza hasta resolver su problema")],
    worked=[
        ("Detectar un código repetido", "En una lista de ejemplo aparecen MP-010, MP-011 y MP-011. ¿Qué problema hay?", ["El código MP-011 se repite en dos muestras.", "Dos muestras distintas no se pueden distinguir."], "Código repetido"),
        ("Comparar gravedad", "Una muestra de ejemplo tiene el código repetido y otra tiene la hora ilegible. ¿Cuál complica más la trazabilidad?", ["Con el código repetido ya no se distinguen dos muestras.", "La hora ilegible se puede resolver con respaldo."], "El código repetido"),
    ],
    mistakes=[("Corregir un código repetido cambiando uno de los dos por un número «libre» sin avisar.", "Se pierde el origen de cada muestra y la trazabilidad.", "Informa al jefe de laboratorio para resolverlo con respaldo."),
              ("Analizar una muestra con etiqueta ilegible porque «se sabe cuál es».", "Sin rótulo legible no se puede garantizar la identidad.", "Retén la muestra hasta identificarla con respaldo.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es un código repetido?", "El mismo código en dos muestras distintas", "Un código con más de tres letras", "Un código escrito con tinta", "El repetido impide distinguir las muestras."),
        ("abc", "En el laboratorio químico: ¿qué se hace con una muestra con un problema de rótulo?", "Se retiene y se informa al jefe de laboratorio", "Se analiza igual", "Se descarta sin avisar", "No se analiza hasta resolver el problema."),
        ("abc", "En el laboratorio químico: ¿qué es un respaldo?", "Un documento o verificación que permite corregir un dato sin inventarlo", "Una copia del informe final", "El nombre de un analista", "El respaldo evita corregir por suposición."),
        ("=", "{F} ¿Cuántas muestras de la lista tienen algún problema?", "4", "Tienen problema la 3, la 4, la 5 y la 6.", " muestras"),
        ("=", "{F} ¿Cuántas muestras de la lista están completas?", "8-4", "Se restan las que tienen problema al total.", " muestras"),
        ("=", "{F} ¿Qué porcentaje de las muestras está completo?", "4*100//8", "Se divide las completas entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué dato le falta a la muestra 3 en la lista?", "La hora", "La firma del receptor", "La etiqueta legible", "La lista anota la muestra 3 sin hora."),
        ("abc", "{F} ¿Qué muestras comparten el código PI-003?", "La 3 y la 4", "La 5 y la 6", "La 7 y la 8", "La lista repite ese código en las muestras 3 y 4."),
        ("abc", "{F} ¿Qué problema compromete más la trazabilidad?", "El código repetido de las muestras 3 y 4", "La falta de firma de la muestra 5", "La etiqueta ilegible de la muestra 6", "Con un código repetido no se distingue una muestra de otra."),
        ("abc", "{F} La muestra 6 tiene la etiqueta ilegible. ¿Qué corresponde?", "Retenerla y verificar su identidad con respaldo antes de analizar", "Analizarla porque la tinta corrida no cambia el contenido", "Rotularla de nuevo según lo que parezca", "Sin etiqueta legible no se confirma la identidad."),
        ("=", "{F} ¿Cuántos minutos pasaron entre la primera y la última recepción de la lista?", "60", "Entre las 08:00 y las 09:00 pasa una hora, es decir, 60 minutos.", " minutos"),
        ("abc", "{F} Un receptor propone cambiar el código de la muestra 4 a PI-004 «para resolverlo ya». ¿Qué corresponde?", "Informar al jefe de laboratorio y resolverlo con respaldo, sin cambiarlo por cuenta propia", "Hacerlo, porque PI-004 está libre", "Hacerlo si se avisa por mensaje", "Un cambio de código sin respaldo rompe la trazabilidad."),
        em("Revisas la lista de muestras cuando alguien avisa que en el refrigerador de muestras hay un envase que gotea y que se siente un olor fuerte.", 2),
    ],
    ctx=("abc", "Una supervisora de ejemplo te pide marcar como «completas» las 8 muestras de la lista «para cumplir el informe del día». ¿Qué respondes?", "Que no: se informan las 4 no conformidades y las muestras involucradas quedan retenidas", "Que sí, si se corrigen mañana", "Que sí, si el cliente no se entera", "El informe debe reflejar lo real; una mentira rompe la cadena de custodia."),
    sc=[
        ("En el laboratorio químico: ¿qué problema es más grave, un código repetido o una firma faltante?", "El código repetido", "Impide distinguir dos muestras entre sí."),
        ("En el laboratorio químico: ¿qué se hace con una muestra cuya identidad no es segura?", "Se retiene hasta confirmarla con respaldo", "No se analiza si no se puede identificar."),
        ("¿Se cambia un código por cuenta propia para resolver un repetido?", "No, se informa y se resuelve con respaldo", "Un cambio sin registro destruye la trazabilidad."),
    ],
    op=("Lista ficticia del «Laboratorio Demo Costa Norte»: 1) MP-101, completa. 2) MP-102, sin firma. 3) PI-103, completa. 4) PI-103, completa (código repetido con la 3). 5) PF-105, etiqueta ilegible. Escribe (a) cuántas muestras tienen problema, (b) qué porcentaje de la lista está completo, (c) cuál es el problema más grave y por qué, (d) qué harías con las muestras involucradas.",
        "(a) La 2, la 3, la 4 y la 5: 4 muestras (la 3 y la 4 por el código repetido). (b) Solo la 1 está completa: 1 de 5, es decir, 20 %. (c) El código repetido, porque no se distingue una muestra de otra. (d) Retenerlas, informar al jefe de laboratorio y resolverlo con respaldo.",
        ["cuenta las muestras con problema", "expresa la proporción completa", "identifica el problema más grave", "indica la conducta correcta"],
        ["hoja con las cuatro respuestas"],
        ["no contar la repetida", "corregir por suposición", "no retener las muestras"],
        "Pregunta: «¿qué muestras no se pueden distinguir?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa una lista de seis muestras con dos errores de rótulo y descríbelos.",
    extend="Explica con un ejemplo por qué es mejor retener una muestra dudosa que analizarla.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada). Reglas de ejemplo del «Laboratorio Demo Valle Claro»: (1) el código de una muestra es el tipo (MP, PI o PF), un guion y un número correlativo del día de 3 cifras que parte en 001, sin importar el tipo; (2) se rotulan primero las muestras urgentes; "
     "(3) el refrigerador tiene 24 posiciones y ya hay 16 ocupadas. Hoy llegan 15 muestras: 6 MP, 5 PI y 4 PF, de las cuales 12 son refrigeradas. Cada muestra lleva 2 etiquetas (envase y tapa) y las etiquetas vienen en paquetes de 25. "
     "Las muestras de retención se conservan 30 días (de ejemplo) y han pasado 21.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar reglas de codificación y de gestión con datos de ejemplo: construir códigos, calcular posiciones de refrigerador, etiquetas necesarias y plazos de retención.",
    prior=["Sé qué es un rótulo mínimo.", "Sé sumar, restar y dividir números enteros.", "Sé redondear hacia arriba."],
    explain=[
        "En el laboratorio químico, una regla de codificación define cómo se arma el código de cada muestra. Con la regla de ejemplo, el código es el tipo, un guion y un número correlativo del día de 3 cifras: la primera muestra del día es 001, la segunda 002, y así, sin importar el tipo. Aplicar la regla sin saltarse números ayuda a detectar muestras que faltan.",
        "Las posiciones de refrigerador disponibles se calculan restando las ocupadas al total; si llegan más muestras refrigeradas que posiciones libres, hay un problema de capacidad que se informa al jefe de laboratorio, no se resuelve apilando muestras sin control. Las etiquetas necesarias se calculan multiplicando las muestras por las etiquetas de cada una y dividiendo entre las de cada paquete, redondeando hacia arriba. El plazo de retención restante se obtiene restando los días transcurridos.",
        f"Los cálculos orientan la gestión; manipular muestras lo hace personal formado. {EMER} {AVISO}",
    ],
    vocab=[("regla de codificación", "norma que define cómo se arma el código de cada muestra"), ("correlativo", "número que sigue el orden 001, 002, 003, sin saltos"), ("posición de refrigerador", "lugar numerado donde se guarda una muestra refrigerada"), ("capacidad", "cantidad máxima de posiciones que existen"), ("plazo de retención", "tiempo durante el cual se conserva una muestra de respaldo")],
    worked=[
        ("Armar un código", "Con la regla de la clase, la 4.ª muestra del día es de producto final. ¿Cuál es su código?", ["El correlativo de la 4.ª muestra es 004.", "El tipo es PF, así que el código es PF-004."], "PF-004"),
        ("Etiquetas necesarias", "Un laboratorio de ejemplo recibe 18 muestras con 2 etiquetas cada una y los paquetes traen 20. ¿Cuántos paquetes necesita? Redondea hacia arriba.", ["Se necesitan 18 por 2, es decir, 36 etiquetas.", "36 entre 20 es 1 y sobran 16, así que se necesitan 2 paquetes."], "2 paquetes"),
    ],
    mistakes=[("Reiniciar el correlativo en 001 para cada tipo.", "La regla dice que el correlativo es del día y no depende del tipo.", "Numera de corrido las muestras del día."),
              ("Guardar muestras refrigeradas sin posición porque «caben apiladas».", "La capacidad se mide en posiciones numeradas; apilar rompe el control.", "Informa que faltan posiciones y espera instrucciones.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué define una regla de codificación?", "Cómo se arma el código de cada muestra", "El precio de cada análisis", "El horario del laboratorio", "La regla fija la estructura del código."),
        ("abc", "En el laboratorio químico: ¿qué significa que el correlativo sea del día?", "Que el número parte en 001 cada día y sigue sin saltos", "Que el número depende del tipo de muestra", "Que cambia según el cliente", "El correlativo del día numera todas las muestras de ese día."),
        ("abc", "En el laboratorio químico: ¿qué se hace si llegan más muestras refrigeradas que posiciones libres?", "Se informa al jefe de laboratorio", "Se apilan las muestras", "Se dejan fuera del refrigerador sin avisar", "La falta de capacidad se informa; no se improvisa."),
        ("=", "{F} ¿Cuántas muestras llegan hoy en total?", "6+5+4", "Se suman las muestras de los tres tipos.", " muestras"),
        ("abc", "{F} ¿Cuál es el código de la última muestra del día, si es un PF?", "PF-015", "PF-004", "PF-001", "La muestra 15 del día lleva el correlativo 015."),
        ("abc", "{F} ¿Qué código lleva la 7.ª muestra del día si es un PI?", "PI-007", "PI-001", "PI-070", "El correlativo es del día: la 7.ª lleva 007."),
        ("=", "{F} ¿Cuántas posiciones libres tiene el refrigerador?", "24-16", "Se resta las ocupadas al total de posiciones.", " posiciones"),
        ("=", "{F} ¿Cuántas muestras refrigeradas quedarían sin posición?", "12-(24-16)", "Se resta las posiciones libres a las muestras refrigeradas.", " muestras"),
        ("=", "{F} ¿Cuántas etiquetas se necesitan para las 15 muestras?", "15*2", "Se multiplica las muestras por las etiquetas de cada una.", " etiquetas"),
        ("=", "{F} ¿Cuántos paquetes de etiquetas se necesitan? Redondea hacia arriba.", "(30+24)//25", "30 etiquetas son más de un paquete de 25; hay que redondear hacia arriba.", " paquetes"),
        ("=", "{F} ¿Cuántos días le quedan a la muestra de retención?", "30-21", "Se resta lo transcurrido al plazo.", " días"),
        ("abc", "{F} Una persona propone apilar las 4 muestras que no caben en el refrigerador. ¿Qué corresponde?", "Informar al jefe de laboratorio para resolver la falta de posiciones", "Apilarlas si están bien rotuladas", "Dejarlas fuera hasta el día siguiente sin avisar", "La capacidad no se sobrepasa por cuenta propia."),
        em("Calculas las posiciones del refrigerador de ejemplo cuando alguien avisa que un estante de la sala de muestras se cayó y que un frasco se rompió con olor irritante.", 3),
    ],
    ctx=("abc", "Una compañera de ejemplo numera las muestras PF empezando en 001 «porque son de otro tipo». ¿Qué corresponde según la regla?", "Corregirla: el correlativo es del día y continúa sin importar el tipo", "Aceptarlo, porque cada tipo tiene su número", "Aceptarlo si los códigos no se repiten ese día", "La regla de ejemplo numera todo el día de corrido."),
    sc=[
        ("En el laboratorio químico: ¿cuál es el código de la 3.ª muestra del día si es MP?", "MP-003", "El correlativo del día es 003."),
        ("¿Cómo se calculan las posiciones libres de un refrigerador?", "Total de posiciones menos las ocupadas", "La resta da la capacidad disponible."),
        ("En el laboratorio químico: ¿qué se hace con una muestra que no cabe en el refrigerador?", "Se informa y se espera instrucción", "No se improvisa un lugar sin control."),
    ],
    op=("Reglas ficticias del «Laboratorio Demo Costa Norte» (iguales a las de la clase): llegan 10 muestras, 4 MP, 3 PI y 3 PF, 6 refrigeradas; el refrigerador tiene 12 posiciones con 8 ocupadas; cada muestra lleva 2 etiquetas y los paquetes traen 15. Escribe (a) el código de la 10.ª muestra si es PF, (b) cuántas muestras refrigeradas no tendrían posición, (c) cuántos paquetes de etiquetas se necesitan, (d) qué haces con las muestras sin posición.",
        "(a) PF-010. (b) Hay 4 posiciones libres y 6 muestras refrigeradas: quedan 2 sin posición. (c) 20 etiquetas; se necesitan 2 paquetes (redondeo hacia arriba). (d) Informar al jefe de laboratorio y esperar instrucción.",
        ["arma el código", "calcula las muestras sin posición", "calcula los paquetes", "indica la conducta correcta"],
        ["hoja con las cuatro respuestas"],
        ["reiniciar el correlativo", "no restar las posiciones ocupadas", "no redondear hacia arriba"],
        "Pregunta: «¿cuántas posiciones hay libres?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Aplica la regla de codificación a seis muestras inventadas y calcula las etiquetas necesarias.",
    extend="Explica con un ejemplo por qué un correlativo sin saltos ayuda a detectar muestras perdidas.",
)

# ============================================================ OAM-02, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Dos sistemas de codificación para el «Laboratorio Demo Valle Claro». Sistema A: número correlativo simple (1, 2, 3…) que se reinicia cada semana, 2 minutos por rótulo. "
     "Sistema B: tipo, fecha y correlativo del día (por ejemplo MP-250314-007), 3 minutos por rótulo. Se rotulan 40 muestras por día y se trabaja 20 días al mes. Condición obligatoria: el código debe ser único en el tiempo. "
     "En un mes de 200 muestras con el sistema A hubo 8 muestras confundidas; con el sistema B hubo 2. "
     "Lista de control de rótulos, 5 puntos: (1) código único; (2) descripción; (3) fecha y hora; (4) responsable; (5) conservación. Se revisaron 20 rótulos: 16 cumplen los 5 puntos, 2 no tienen responsable, 1 no tiene hora y 1 tiene el código repetido.")
build(
    O2, 5, F,
    use="Aprenderé a comparar sistemas de codificación con una condición obligatoria de código único, tiempo y errores, y a verificar la calidad de los rótulos con una lista de control.",
    prior=["Sé qué es un código único y un rótulo mínimo.", "Sé calcular porcentajes.", "Sé qué es una condición obligatoria."],
    explain=[
        "En el laboratorio químico, un sistema de codificación debe cumplir la condición obligatoria de dar códigos únicos en el tiempo: un código no puede repetirse nunca. Un correlativo simple que se reinicia cada semana repite los mismos números en semanas distintas, y por eso solo es único si se acompaña de la fecha. Un código con tipo, fecha y correlativo es único y además da información al leerlo.",
        "Entre los sistemas que cumplen la condición obligatoria se comparan el tiempo que toma rotular y la cantidad de errores. Más tiempo por rótulo puede compensarse si se reducen las confusiones de muestras. La calidad de los rótulos se verifica con una lista de control: cada rótulo se marca como cumple o no cumple, y el porcentaje de cumplimiento es los que cumplen todo entre los revisados, por 100.",
        f"Todo es análisis en papel. {EMER} {AVISO}",
    ],
    vocab=[("sistema de codificación", "conjunto de reglas para dar código a las muestras"), ("único en el tiempo", "que no se repite nunca, ni en otras semanas ni en otros meses"), ("muestra confundida", "muestra que se tomó o analizó como si fuera otra"), ("lista de control", "tabla de puntos que se marcan como cumple o no cumple")],
    worked=[
        ("Tiempo extra", "Un sistema de ejemplo toma 1 minuto más por rótulo que otro y se rotulan 30 muestras por día. ¿Cuántos minutos más por día?", ["Se multiplican los minutos extra por las muestras.", "1 por 30 son 30."], "30 minutos más por día"),
        ("Tasa de confusión", "En un mes de ejemplo, 5 de 250 muestras se confundieron. ¿Qué porcentaje es?", ["Se divide 5 entre 250 y se multiplica por 100.", "5 por 100 son 500, y 500 entre 250 son 2."], "2 %"),
    ],
    mistakes=[("Elegir el sistema más rápido aunque repita códigos.", "Un código repetido es una falla grave de trazabilidad.", "Aplica primero la condición de código único y compara después el tiempo."),
              ("Contar como correcto un rótulo al que le falta el responsable.", "Un punto faltante lo vuelve no conforme.", "Marca «no cumple» si falta cualquiera de los puntos.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué significa que un código sea único en el tiempo?", "Que no se repite nunca, ni en otras semanas ni en otros meses", "Que solo se usa en un día", "Que tiene una sola letra", "Único en el tiempo evita confusiones entre periodos."),
        ("abc", "En el laboratorio químico: ¿por qué el sistema A no cumple la condición obligatoria?", "Porque reinicia los números cada semana y se repiten", "Porque toma 2 minutos por rótulo", "Porque usa solo números", "Al reiniciar, el mismo código identifica muestras distintas."),
        ("abc", "En el laboratorio químico: ¿para qué sirve una lista de control de rótulos?", "Para revisar punto por punto si cada rótulo cumple lo exigido", "Para calcular el costo de los análisis", "Para elegir qué muestras analizar primero", "La lista ordena la verificación de calidad."),
        ("=", "{F} ¿Cuántos minutos más por día toma el sistema B que el A?", "(3-2)*40", "Se resta el tiempo del A al del B y se multiplica por las muestras del día.", " minutos"),
        ("=", "{F} ¿Cuántos minutos más al mes toma el sistema B que el A?", "(3-2)*40*20", "Se multiplica la diferencia diaria por los días de trabajo del mes.", " minutos"),
        ("=", "{F} ¿Qué porcentaje de las 200 muestras se confundió con el sistema A?", "8*100//200", "Se divide las muestras confundidas entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje de las 200 muestras se confundió con el sistema B?", "2*100//200", "Se divide las muestras confundidas entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué sistema conviene elegir y por qué?", "El B, porque da códigos únicos y menos confusiones aunque tarde más", "El A, porque es más rápido", "El A, porque usa números más cortos", "El B cumple la condición obligatoria y reduce los errores."),
        ("=", "{F} ¿Cuántas muestras menos se confunden con el sistema B que con el A?", "8-2", "Se resta las confundidas del B a las del A.", " muestras"),
        ("=", "{F} ¿Qué porcentaje de los 20 rótulos revisados cumple los 5 puntos?", "16*100//20", "Se dividen los rótulos que cumplen entre los revisados y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué corresponde con el rótulo que tiene el código repetido?", "Informar al jefe de laboratorio y resolverlo con respaldo", "Cambiar el código por cuenta propia", "Dejarlo porque cumple 4 de 5 puntos", "Un código repetido es una falla grave que se resuelve con respaldo."),
        ("=", "{F} Si se corrigen con respaldo los 4 rótulos con problemas, ¿cuántos de los 20 cumplirán los 5 puntos?", "16+4", "Se suman los que cumplían y los que se corrigen.", " rótulos"),
        em("Comparas sistemas de rotulado en la oficina cuando alguien avisa que se rompió un envase de muestras y que hay un olor muy fuerte en la sala.", 4),
    ],
    ctx=("abc", "Una jefatura de ejemplo dice: «Usemos el sistema A para ahorrar tiempo; si se repite un número, lo vemos después». ¿Qué respondes?", "Que no corresponde, porque un código repetido rompe la trazabilidad", "Que sí, si se ahorra más de 30 minutos al día", "Que sí, si se anota en un cuaderno", "La condición de código único no se negocia por el tiempo."),
    sc=[
        ("En el laboratorio químico: ¿qué condición debe cumplir un sistema de codificación?", "Dar códigos únicos en el tiempo", "Sin eso se pierde la trazabilidad."),
        ("En el laboratorio químico: ¿cómo se calcula el porcentaje de rótulos conformes?", "Rótulos que cumplen entre revisados, por 100", "Es una proporción expresada en porcentaje."),
        ("¿Se corrige un rótulo faltante de memoria?", "No, se corrige con respaldo", "Los datos inventados rompen la trazabilidad."),
    ],
    op=("Caso ficticio del «Laboratorio Demo Costa Norte»: sistema X (número simple que se reinicia cada mes) toma 2 minutos por rótulo; sistema Y (tipo, fecha y correlativo) toma 4 minutos. Se rotulan 30 muestras por día. Con X se confundieron 6 de 300 muestras en un mes y con Y, 3 de 300. De 10 rótulos revisados, 8 cumplen todo. Escribe (a) qué sistema cumple el código único y por qué, (b) cuántos minutos más por día toma Y, (c) el porcentaje de muestras confundidas con cada sistema, (d) el porcentaje de rótulos conformes.",
        "(a) Y, porque incluye la fecha y no se repite; X reinicia cada mes. (b) 2 por 30 son 60 minutos más por día. (c) X: 2 %; Y: 1 %. (d) 80 %.",
        ["aplica la condición obligatoria", "calcula el tiempo extra", "calcula los porcentajes de confusión", "calcula la conformidad"],
        ["hoja con las cuatro respuestas"],
        ["elegir por velocidad", "dividir al revés", "no usar el total de muestras"],
        "Pregunta: «¿qué sistema puede repetir un código en otro mes?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Compara dos sistemas de codificación inventados con tiempo, errores y unicidad, y elige uno.",
    extend="Explica con un ejemplo por qué agregar la fecha al código ayuda a que sea único en el tiempo.",
)
