"""Explotación Minera TP 3.º y 4.º medio: OAE-07 (cubicación del mineral: conceptos y cálculos de planilla) y OAE-08 (chancado primario: solo conceptos, documentos y cálculos de planilla; sin operar equipos). Todo en papel, con datos de ejemplo."""
from __future__ import annotations

from tp_exmi_common import AVISO, EMER, build

O7 = "TP-EXMI-3y4-OAE-07"
O8 = "TP-EXMI-3y4-OAE-08"

# ============================================================ OAE-07, clase 1
F = ("Ficha 27 (caso de ejemplo, inventado). La faena ficticia «Mina Demo Cerro Pelado» saca cobre de un rajo con camiones que llevan la roca al chancado. Etapas: carguío (llenar el camión), transporte, descarga y regulación del flujo (que el chancado reciba una cantidad estable). "
     "Matriz de peligros de la logística del mineral: atropello o choque en los caminos (probabilidad 3 y gravedad 5), polvo (probabilidad 4 y gravedad 3), sobrecarga de un camión (probabilidad 2 y gravedad 5) y derrame de material en el camino (probabilidad 3 y gravedad 2). "
     "Regla de la matriz de ejemplo: puntaje de riesgo = probabilidad × gravedad. Personal de ejemplo en un turno: 12 en carguío, 8 en transporte y 4 en control de pesaje.")
build(
    O7, 1, F,
    use="Aprenderé qué es cubicar el mineral, cómo se mueve desde el carguío hasta la descarga, qué peligros tiene el tránsito en una faena y por qué la normativa de tránsito interno protege a las personas.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé calcular el volumen de una caja multiplicando tres medidas.", "Sé que las tareas de riesgo las hacen personas autorizadas."],
    explain=[
        "Cubicar es calcular el volumen de un material. En minería se cubica el mineral para planificar cuánto se carga, cuánto transporta cada camión, cuánto se descarga y cuánto recibe el chancado. El carguío es llenar los camiones, el transporte es llevarlos por los caminos y la descarga es vaciarlos. La regulación del flujo es lograr que el chancado reciba cantidades estables, sin vaciarse ni atascarse.",
        "Los peligros de la logística del mineral son el atropello y el choque, el polvo, la sobrecarga de un camión y los derrames. Un camión sobrecargado es más difícil de frenar y puede dañar el camino. Por eso la empresa fija normas internas de tránsito: velocidades máximas, prioridad de paso y zonas peatonales. En la matriz de ejemplo, el puntaje de riesgo es probabilidad por gravedad y se atiende primero el mayor.",
        f"Operar camiones y cargadores exige licencia interna, formación y autorización; este cuaderno solo enseña a calcular y a leer documentos. La autoridad minera y la norma vigente fijan las reglas de seguridad. {EMER} {AVISO}",
    ],
    vocab=[("cubicar", "calcular el volumen de un material"), ("carguío", "llenado de los camiones con mineral o roca"), ("transporte", "traslado del material por los caminos de la faena"), ("descarga", "vaciado del camión en su destino"), ("regulación del flujo", "lograr que el chancado reciba cantidades estables"), ("sobrecarga", "carga mayor que la capacidad del camión")],
    worked=[
        ("Puntaje de riesgo", "En la matriz de ejemplo de un patio de repuestos, el tránsito de una grúa horquilla tiene probabilidad 3 y gravedad 4. ¿Qué puntaje resulta?", ["Se multiplica la probabilidad por la gravedad.", "3 por 4 son 12."], "12 puntos"),
        ("Peligro y riesgo", "En un camino de ejemplo, una curva no tiene señal de velocidad. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la curva sin señal, porque un conductor puede entrar muy rápido.", "El riesgo es que un camión vuelque o choque."], "Peligro: la curva sin señal; riesgo: que un camión vuelque o choque"),
    ],
    mistakes=[("Creer que sobrecargar un camión «un poquito» no cambia nada.", "La sobrecarga aumenta el riesgo de frenado y de daño del camino.", "Respeta siempre la capacidad del camión."),
              ("Creer que quien sabe calcular volúmenes ya puede operar un camión o un cargador.", "Operar equipos exige licencia, formación y autorización.", "Aprende a calcular aquí y deja la operación a personal autorizado.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué significa cubicar un material?", "Calcular su volumen", "Pesarlo en una balanza", "Cargarlo en un camión", "Cubicar es calcular volumen, no pesar ni mover."),
        ("abc", "En Explotación Minera: ¿qué es el carguío?", "El llenado de los camiones con mineral o roca", "El traslado del material por los caminos", "El vaciado del camión en su destino", "El carguío es la etapa de llenar los camiones."),
        ("abc", "En Explotación Minera: ¿qué es la regulación del flujo en la entrada del chancado?", "Lograr que el chancado reciba cantidades estables", "Aumentar la velocidad de los camiones", "Pesar cada camión que llega", "Regular el flujo evita vaciar o atascar el chancado."),
        ("=", "{F} ¿Cuántas personas hay en total en el turno de la ficha?", "12+8+4", "Se suman las personas de carguío, transporte y control de pesaje.", " personas"),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «sobrecarga de un camión»?", "Que el camión frene mal o dañe el camino y ocurra un accidente", "Que el camión use más combustible", "Que el carguío demore más", "El riesgo es el daño posible a las personas o los equipos."),
        ("abc", "{F} ¿Por qué la empresa fija normas internas de tránsito?", "Para reducir el riesgo de atropello y choque en los caminos", "Para que los camiones lleguen todos a la misma hora", "Para cobrar peajes a los visitantes", "Las normas de tránsito protegen a las personas y a los equipos."),
        ("=", "{F} ¿Qué puntaje de riesgo tiene el atropello o choque en los caminos?", "3*5", "Se multiplica la probabilidad por la gravedad anotadas en la ficha.", " puntos"),
        ("=", "{F} ¿Qué puntaje de riesgo tiene el polvo?", "4*3", "Se multiplican la probabilidad y la gravedad de ese peligro.", " puntos"),
        ("abc", "{F} Con la regla de la matriz, ¿cuál de los cuatro peligros debe atenderse primero?", "El atropello o choque, porque tiene el mayor puntaje (15)", "El polvo, porque se ve en todos los turnos", "El derrame, porque es el más fácil de resolver", "Se atiende primero el mayor puntaje, que combina probabilidad y gravedad."),
        ("abc", "{F} Un joven en práctica dice: «ya sé calcular cuánto lleva un camión, así que puedo conducirlo». ¿Qué es correcto?", "No: conducir exige licencia interna, formación y autorización", "Sí, si va despacio", "Sí, si hay un compañero al lado", "Saber calcular no habilita para operar un equipo."),
        ("abc", "{F} ¿Por qué un camión sobrecargado es más peligroso aunque el camino esté en buen estado?", "Porque es más difícil de frenar y de controlar", "Porque se ve más grande", "Porque consume más agua", "El peso extra aumenta la distancia necesaria para detenerse."),
        ("=", "{F} Para un simulacro, el personal de carguío y el de transporte se reparte en grupos de 4 personas. ¿Cuántos grupos se forman?", "(12+8)//4", "Se suma el personal de las dos áreas y se divide entre las personas de cada grupo.", " grupos"),
        ("abc", "Durante una visita de ejemplo, ves que un camión pierde el control en una pendiente y se acerca a un grupo de personas. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Correr hacia el camión para detenerlo", "Tomar una foto para el registro", "Interponerse en el camino de un vehículo pesado es extremadamente peligroso."),
    ],
    ctx=("abc", "Un compañero de práctica te dice: «súbete al cargador un momento, yo te enseño y nadie se entera». ¿Qué respondes?", "Que no, porque operar equipos exige licencia, formación y autorización, y que consultarás a un adulto responsable", "Que sí, pero solo un minuto", "Que sí, si el cargador está detenido", "Operar un equipo sin autorización es una falta y un riesgo para todos."),
    sc=[
        ("En Explotación Minera: ¿qué es la descarga?", "El vaciado del camión en su destino", "Es la etapa que cierra el ciclo del camión."),
        ("En Explotación Minera: ¿qué es una sobrecarga?", "Una carga mayor que la capacidad del camión", "La capacidad es el límite que no se debe superar."),
        ("¿Cómo se calcula el puntaje de riesgo de la matriz de ejemplo?", "Probabilidad multiplicada por gravedad", "El puntaje combina cuán probable y cuán grave es el daño."),
    ],
    op=("La faena ficticia «Mina Demo Cerro Claro» tiene un camino de acarreo con una curva cerrada, sin señal de velocidad, y un camión que a veces sale cargado más allá de su capacidad. Escribe (a) un peligro del camino y su riesgo asociado, (b) por qué la sobrecarga es peligrosa, (c) quién puede conducir camiones, (d) qué haces si ves un camión sin control acercarse a personas.",
        "(a) Peligro: la curva sin señal; riesgo: que un camión vuelque o choque. (b) Porque el camión frena peor y puede dañar el camino. (c) Personal con licencia interna, formación y autorización. (d) No acercarme a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "explica el riesgo de la sobrecarga", "nombra quién puede conducir", "aplica la conducta de emergencia"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "creer que cualquiera puede conducir", "interponerse ante el camión"],
        "Pregunta: «¿qué le pasa al frenado de un camión sobrecargado?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa una matriz de tres peligros de un camino de acarreo con probabilidad y gravedad, y calcula los puntajes.",
    extend="Explica con un ejemplo por qué una norma de velocidad protege tanto a conductores como a peatones.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 28 (documentos y datos de ejemplo, inventados). Planilla de acarreo de la faena ficticia «Mina Demo Piedra Azul». El volumen de material en el banco, antes de ser removido, se llama volumen in situ y es de 1.000 m³. Al removerlo, la roca se esponja: aumenta su volumen porque queda con espacios entre los trozos. "
     "Esponjamiento de ejemplo: 25 %. Capacidad de un camión de ejemplo: 50 m³ de material suelto. Densidad de ejemplo del material in situ: 3 toneladas por m³. "
     "Documentos: plan de producción (cuánto se debe mover), boleta de pesaje (peso de cada camión) y registro de viajes. Roles: el planificador calcula las cantidades; el despachador asigna y controla los viajes; el personal de pesaje registra el peso; el jefe de turno organiza.")
build(
    O7, 2, F,
    use="Aprenderé los conceptos de volumen in situ, esponjamiento, capacidad y densidad, los documentos de un acarreo y el rol de cada persona.",
    prior=["Sé qué es cubicar.", "Sé calcular un porcentaje de un número.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "El material en el banco tiene un volumen in situ, que es el que ocupa sin remover. Cuando se remueve, la roca queda con espacios entre los trozos y ocupa más volumen: a eso se llama esponjamiento y se expresa en porcentaje. Si el esponjamiento es 25 %, el volumen suelto es el volumen in situ más el 25 %. Un camión se llena en volumen suelto, y su capacidad es el máximo que puede llevar sin sobrecargarse.",
        "La densidad es cuánto pesa cada metro cúbico, en toneladas por metro cúbico. Con la densidad se pasa de volumen a toneladas: toneladas igual a volumen por densidad. Los documentos de un acarreo son el plan de producción, la boleta de pesaje y el registro de viajes. Cada rol tiene su tarea: el planificador calcula, el despachador controla los viajes, el personal de pesaje registra y el jefe de turno organiza.",
        f"Los valores de este cuaderno son de ejemplo: los reales los miden y fijan especialistas de la faena. {EMER} {AVISO}",
    ],
    vocab=[("volumen in situ", "volumen del material en el banco, antes de removerlo"), ("esponjamiento", "aumento de volumen de la roca al removerla, en porcentaje"), ("volumen suelto", "volumen que ocupa el material ya removido"), ("capacidad del camión", "volumen o peso máximo que puede llevar sin sobrecarga"), ("densidad", "peso de cada metro cúbico de un material"), ("boleta de pesaje", "documento con el peso de cada camión")],
    worked=[
        ("Volumen suelto", "Un volumen in situ de ejemplo de 400 m³ tiene un esponjamiento de 30 %. ¿Cuál es el volumen suelto?", ["El aumento es 30 % de 400, es decir, 120 m³.", "400 más 120 son 520 m³."], "520 m³"),
        ("Toneladas", "Un volumen in situ de ejemplo de 200 m³ con densidad de 2 toneladas por m³, ¿cuántas toneladas pesa?", ["Toneladas igual a volumen por densidad.", "200 por 2 son 400 t."], "400 toneladas"),
    ],
    mistakes=[("Calcular los viajes del camión con el volumen in situ en lugar del volumen suelto.", "El camión se llena con material removido, que ocupa más volumen.", "Primero pasa a volumen suelto y luego divide entre la capacidad."),
              ("Confundir el volumen con el peso.", "El volumen se mide en m³ y el peso, en toneladas; se conectan con la densidad.", "Usa la densidad para pasar de uno a otro.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es el volumen in situ?", "El volumen del material en el banco, antes de removerlo", "El volumen del material ya cargado en el camión", "El volumen de agua que hay en la mina", "In situ significa en su lugar original."),
        ("abc", "En Explotación Minera: ¿qué es el esponjamiento?", "El aumento de volumen de la roca al removerla", "La disminución de volumen de la roca al triturarla", "El peso que se agrega al camión", "Al remover la roca quedan espacios entre los trozos y el volumen crece."),
        ("abc", "En Explotación Minera: ¿qué documento muestra el peso de cada camión?", "La boleta de pesaje", "El plan de producción", "El registro de viajes", "La boleta de pesaje registra el peso."),
        ("=", "{F} ¿Cuántos m³ aumenta el volumen por el esponjamiento?", "1000*25//100", "Se calcula el 25 % del volumen in situ.", " m³"),
        ("=", "{F} ¿Cuál es el volumen suelto del material?", "1000+1000*25//100", "Se suma el aumento por esponjamiento al volumen in situ.", " m³"),
        ("=", "{F} ¿Cuántos viajes de camión de 50 m³ hacen falta para mover el material?", "(1000+1000*25//100)//50", "Se divide el volumen suelto entre la capacidad del camión.", " viajes"),
        ("=", "{F} ¿Cuántas toneladas pesa el material in situ?", "1000*3", "Se multiplica el volumen in situ por la densidad.", " t"),
        ("abc", "{F} ¿Qué rol calcula las cantidades que se deben mover?", "El planificador", "El despachador", "El personal de pesaje", "El planificador calcula; el despachador controla los viajes."),
        ("abc", "{F} ¿Qué documento dice cuánto se debe mover en el período?", "El plan de producción", "La boleta de pesaje", "El registro de viajes", "El plan fija la meta de movimiento."),
        ("abc", "{F} Un asistente calcula los viajes dividiendo el volumen in situ entre la capacidad del camión. ¿Qué respondes?", "Que debe usar el volumen suelto, porque el camión se llena con material removido", "Que está correcto, porque el volumen no cambia", "Que debe dividir entre la densidad", "El material removido ocupa más volumen que en el banco."),
        ("abc", "{F} ¿Por qué un camión de 50 m³ de capacidad no debe cargarse con 60 m³ de material suelto?", "Porque sería una sobrecarga, que lo vuelve más difícil de frenar", "Porque el material se perdería de todos modos", "Porque el camión sería demasiado liviano", "La capacidad es el máximo seguro del camión."),
        ("=", "{F} Si el esponjamiento fuera 40 % en lugar de 25 %, ¿cuántos m³ sueltos habría?", "1000+1000*40//100", "Se suma el nuevo aumento al volumen in situ.", " m³"),
        ("abc", "Una persona te cuenta que, en una zona de carguío de ejemplo, un cargador rodó cerca de un compañero que quedó herido. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a mover el cargador", "Subirte al cargador para sacarlo", "Un equipo pesado puede moverse otra vez; lo correcto es avisar."),
    ],
    ctx=("abc", "Una compañera de práctica calcula los viajes para 800 m³ in situ con 25 % de esponjamiento y camiones de 50 m³ y escribe «800 ÷ 50 = 16 viajes». ¿Qué respondes?", "Que debe pasar a volumen suelto: 800 más 200 son 1.000 m³, y 1.000 ÷ 50 son 20 viajes", "Que está correcto, porque 800 entre 50 son 16", "Que son 15 viajes porque se resta el esponjamiento", "El camión se llena con material removido, que ocupa más volumen."),
    sc=[
        ("En Explotación Minera: ¿cómo se calcula el volumen suelto?", "Volumen in situ más el aumento por esponjamiento", "El esponjamiento aumenta el volumen del material removido."),
        ("En Explotación Minera: ¿qué relaciona volumen y toneladas?", "La densidad", "Toneladas igual a volumen por densidad."),
        ("En Explotación Minera: ¿qué rol controla los viajes de los camiones?", "El despachador", "Asigna los viajes y verifica que se cumplan."),
    ],
    op=("Datos ficticios de la faena «Mina Demo Cerro Claro»: volumen in situ de 600 m³, esponjamiento de 50 %, camiones de 45 m³ y densidad de 2 toneladas por m³. Escribe (a) el volumen suelto, (b) los viajes necesarios, (c) las toneladas in situ, (d) qué documento usarías para comprobar el peso de cada camión.",
        "(a) 600 + 300 = 900 m³. (b) 900 ÷ 45 = 20 viajes. (c) 600 × 2 = 1.200 t. (d) La boleta de pesaje.",
        ["calcula el volumen suelto", "calcula los viajes con el volumen suelto", "calcula las toneladas", "elige el documento"],
        ["hoja con las cuatro respuestas"],
        ["dividir el volumen in situ entre la capacidad", "confundir volumen con peso", "elegir el plan de producción en vez de la boleta"],
        "Pregunta: «¿con qué volumen se llenan los camiones?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un banco de 300 m³ con 20 % de esponjamiento y un camión de 30 m³, y calcula los viajes.",
    extend="Explica con un ejemplo por qué el esponjamiento hace que se necesiten más viajes de los que sugiere el volumen in situ.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 29 (caso de ejemplo, inventado). Registro de viajes de un turno en la faena ficticia «Mina Demo Lomas Bajas». Capacidad máxima de peso de cada camión: 50 toneladas. Pesos medidos (t): T1 = 48; T2 = 50; T3 = 52; T4 = 49; T5 = 47; T6 = 55; T7 = 50; T8 = 46. "
     "Regla de ejemplo: un camión con peso mayor que su capacidad está sobrecargado; el despachador no lo autoriza a salir y lo informa al jefe de turno, quien decide cómo se corrige. La capacidad de 50 toneladas sí se acepta. "
     "Plan del turno: mover 400 toneladas con 8 viajes.")
build(
    O7, 3, F,
    use="Aprenderé a analizar un registro de viajes: detectar sobrecargas, calcular totales y porcentajes, compararlos con el plan y decidir a quién se informa.",
    prior=["Sé qué es la capacidad de un camión.", "Sé sumar y calcular porcentajes.", "Sé qué es un registro."],
    explain=[
        "Un registro de viajes anota, por cada viaje, el peso medido del camión. Se compara cada peso con la capacidad: si es igual o menor, el viaje cumple; si es mayor, hay sobrecarga. El exceso es cuánto se pasa: peso menos capacidad. El porcentaje de viajes sobrecargados es los sobrecargados por 100 divididos entre el total de viajes.",
        "La regla del caso es que el despachador no autoriza a salir a un camión sobrecargado y lo informa al jefe de turno, que decide cómo se corrige. Nadie ajusta un peso en el registro para que parezca bien. Además, la suma de los pesos permite comparar lo movido con lo planificado.",
        f"Este análisis es de papel: operar camiones o balanzas exige personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("peso medido", "peso que registra la balanza del camión"), ("exceso", "diferencia entre el peso medido y la capacidad, cuando lo supera"), ("viaje que cumple", "viaje cuyo peso es igual o menor que la capacidad"), ("despachador", "persona que asigna y controla los viajes de los camiones")],
    worked=[
        ("Detectar sobrecarga", "Un camión de ejemplo con capacidad de 80 t pesa 84 t. ¿Está sobrecargado y cuál es el exceso?", ["Se compara el peso con la capacidad.", "84 es mayor que 80, y la diferencia es 4 t."], "Sí, con un exceso de 4 toneladas"),
        ("Porcentaje de sobrecargas", "En 5 viajes de ejemplo hubo 1 sobrecargado. ¿Qué porcentaje es?", ["Se multiplican por 100 los viajes sobrecargados y se divide entre el total.", "1 por 100 dividido entre 5 son 20."], "20 %"),
    ],
    mistakes=[("Considerar sobrecargado a un camión que pesa exactamente su capacidad.", "El peso igual a la capacidad se acepta.", "Compara con «mayor que», no con «igual o mayor que»."),
              ("Cambiar un peso en el registro para que no haya sobrecargas.", "Alterar un registro oculta un problema real.", "Anota el peso real e informa.")],
    T=[
        ("abc", "En Explotación Minera: ¿cuándo hay sobrecarga de un camión?", "Cuando el peso medido es mayor que su capacidad", "Cuando el peso medido es igual a su capacidad", "Cuando el camión va lleno de volumen", "La sobrecarga ocurre al superar la capacidad."),
        ("abc", "En Explotación Minera: ¿qué es el exceso de una sobrecarga?", "La diferencia entre el peso medido y la capacidad", "El peso total del camión vacío", "La suma de todos los viajes", "El exceso es lo que sobra por encima de la capacidad."),
        ("abc", "En Explotación Minera: ¿qué hace el despachador ante un camión sobrecargado?", "No lo autoriza a salir y lo informa al jefe de turno", "Lo autoriza si el camino está seco", "Descarga el material por su cuenta", "El despachador no decide la corrección: informa a la jefatura."),
        ("abc", "{F} ¿Cuál de estos viajes está sobrecargado?", "T3, con 52 toneladas", "T2, con 50 toneladas", "T5, con 47 toneladas", "Solo T3 y T6 superan las 50 toneladas."),
        ("=", "{F} ¿Cuántas toneladas de exceso tiene el viaje T6?", "55-50", "Se resta la capacidad al peso medido.", " t"),
        ("abc", "{F} ¿El viaje T2, de 50 toneladas, está sobrecargado?", "No, porque el peso es igual a la capacidad", "Sí, porque llegó al máximo", "Sí, porque no tiene margen", "La regla acepta un peso igual a la capacidad."),
        ("=", "{F} ¿Cuántos de los 8 viajes están sobrecargados?", "8-6", "Se restan los 6 viajes que cumplen al total de viajes.", " viajes"),
        ("=", "{F} ¿Qué porcentaje de los viajes está sobrecargado?", "2*100//8", "Se multiplican por 100 los viajes sobrecargados y se divide entre el total.", " %"),
        ("=", "{F} ¿Cuántas toneladas se movieron en total en los 8 viajes?", "48+50+52+49+47+55+50+46", "Se suman los pesos medidos de los 8 viajes.", " t"),
        ("abc", "{F} ¿Se cumplió el plan del turno de mover 400 toneladas?", "No, porque se movieron 397 toneladas, 3 menos que el plan", "Sí, porque se hicieron los 8 viajes", "Sí, porque 397 es cercano a 400", "El plan exige 400 toneladas y se movieron 397."),
        ("abc", "{F} Un despachador propone anotar 50 t en el viaje T6 «para que no se note». ¿Qué corresponde?", "Rechazarlo: se registra el peso real de 55 t y se informa al jefe de turno", "Hacerlo si el jefe no se entera", "Hacerlo si el camión llegó hasta el chancado", "El registro debe reflejar la realidad."),
        ("=", "{F} Si T3 y T6 hubieran pesado 50 toneladas cada uno, ¿cuántas toneladas habría movido el turno?", "48+50+50+49+47+50+50+46", "Se suman los pesos de los 8 viajes con los dos valores corregidos hipotéticamente.", " t"),
        ("abc", "Una persona te cuenta que, junto a una balanza de camiones de ejemplo, un camión se desplazó solo y hay una persona atrapada entre el camión y un muro. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a mover el camión", "Subirte a la cabina a frenarlo", "Un camión que se mueve solo puede volver a moverse."),
    ],
    ctx=("abc", "Un jefe de turno de ejemplo dice: «hoy se movieron 397 toneladas de 400, está bien, no importa que dos camiones hayan ido sobrecargados». ¿Qué respondes?", "Que las sobrecargas son un incumplimiento que se debe informar y corregir, aunque la meta casi se cumpla", "Que tiene razón, porque la meta casi se cumple", "Que mejor se ocultan para no tener problemas", "Producir casi lo planificado no justifica un incumplimiento de seguridad."),
    sc=[
        ("En Explotación Minera: ¿cómo se calcula el exceso de un camión sobrecargado?", "Peso medido menos capacidad", "El exceso es lo que sobra por encima del límite."),
        ("¿Cómo se calcula el porcentaje de viajes sobrecargados?", "Sobrecargados por 100, divididos entre el total", "El porcentaje compara los sobrecargados con todos los viajes."),
        ("¿Se acepta un camión con peso igual a su capacidad?", "Sí, porque no supera el límite", "La regla pide que el peso no sea mayor que la capacidad."),
    ],
    op=("Registro ficticio de la «Mina Demo Cerro Claro»: camiones de capacidad 80 toneladas; pesos medidos: 78; 80; 83; 79; 81; 85. Escribe (a) qué viajes están sobrecargados, (b) el exceso de cada uno, (c) el porcentaje de viajes sobrecargados, (d) qué hace el despachador con los viajes sobrecargados.",
        "(a) Los de 83, 81 y 85 toneladas. (b) 3 t, 1 t y 5 t. (c) 3 × 100 ÷ 6 = 50 %. (d) No los autoriza a salir y los informa al jefe de turno.",
        ["detecta las sobrecargas", "calcula los excesos", "expresa la proporción de sobrecargas", "describe la acción del despachador"],
        ["hoja con las cuatro respuestas"],
        ["considerar sobrecargado el de 80 t", "no restar la capacidad", "ajustar los pesos"],
        "Pregunta: «¿el camión de 80 t se acepta?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un registro de 5 viajes con capacidad de 60 toneladas, dos sobrecargas y calcula los excesos.",
    extend="Explica con un ejemplo por qué una meta de producción no justifica sobrecargar camiones.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 30 (planilla de ejemplo, inventada). Cubicación para la faena ficticia «Mina Demo Río Hondo». Banco de 20 m de largo, 15 m de ancho y 10 m de alto. Esponjamiento de ejemplo: 25 %. Capacidad de un camión: 50 m³ sueltos. Densidad de ejemplo del material in situ: 3 toneladas por m³. "
     "Se quiere mover todo el banco en 15 horas. Cada camión hace 1 viaje por hora. El chancado recibe, como máximo, 700 toneladas por hora (valor de ejemplo). Regla de ejemplo: viajes = volumen suelto ÷ capacidad; toneladas por hora = toneladas totales ÷ horas.")
build(
    O7, 4, F,
    use="Aprenderé a calcular en una planilla el volumen de un banco, el volumen suelto, los viajes, el tonelaje, la flota necesaria y si el flujo que llega al chancado es compatible con su capacidad.",
    prior=["Sé calcular un volumen multiplicando tres medidas.", "Sé calcular el esponjamiento.", "Sé qué es la densidad."],
    explain=[
        "Se parte del volumen in situ: largo por ancho por alto. Al volumen in situ se suma el esponjamiento para obtener el volumen suelto. Los viajes necesarios son el volumen suelto dividido entre la capacidad del camión. El tonelaje se calcula con el volumen in situ por la densidad, porque la masa no cambia al remover la roca.",
        "La flota necesaria depende del tiempo disponible: viajes totales divididos entre las horas, y luego entre los viajes por hora de cada camión. El flujo al chancado son las toneladas totales divididas entre las horas, y debe ser menor o igual que lo que el chancado puede recibir; si lo supera, el chancado se atasca y hay que repartir el trabajo en más tiempo.",
        f"Estas cuentas son de planilla y los datos son de ejemplo: los reales los fijan especialistas y la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("flota", "conjunto de camiones asignados a una tarea"), ("ciclo", "recorrido completo de un camión: cargar, transportar, descargar y volver"), ("flujo", "toneladas que llegan al chancado por hora"), ("capacidad del chancado", "máximo de toneladas por hora que el chancado puede recibir"), ("tonelaje", "peso total, en toneladas")],
    worked=[
        ("Volumen de un banco", "Un banco de ejemplo mide 10 m de largo, 8 m de ancho y 5 m de alto. ¿Cuál es su volumen in situ?", ["Se multiplican largo, ancho y alto.", "10 por 8 son 80, y 80 por 5 son 400 m³."], "400 m³"),
        ("Flota necesaria", "Se deben hacer 60 viajes en 6 horas y cada camión hace 2 viajes por hora. ¿Cuántos camiones se necesitan?", ["Los viajes por hora son 60 dividido entre 6, es decir, 10.", "Cada camión hace 2 por hora, por lo que se necesitan 5 camiones."], "5 camiones"),
    ],
    mistakes=[("Calcular el tonelaje con el volumen suelto y la densidad del material in situ.", "La densidad de la ficha corresponde al material in situ.", "Usa el volumen in situ para el tonelaje."),
              ("Ignorar la capacidad del chancado al decidir cuántos camiones enviar.", "Si llega más de lo que el chancado soporta, se atasca.", "Compara el flujo con la capacidad del chancado.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es la flota de camiones?", "El conjunto de camiones asignados a una tarea", "El peso total de los camiones", "La velocidad de los camiones", "La flota es el grupo de camiones que hace la tarea."),
        ("abc", "En Explotación Minera: ¿qué es el flujo hacia el chancado?", "Las toneladas que llegan al chancado por hora", "El número de camiones del turno", "La densidad del material", "El flujo se mide en toneladas por hora."),
        ("abc", "En Explotación Minera: ¿con qué volumen se calcula el tonelaje en la planilla de ejemplo?", "Con el volumen in situ y la densidad", "Con el volumen suelto y la capacidad del camión", "Con el número de viajes", "La masa no cambia al remover; la densidad de la ficha es in situ."),
        ("=", "{F} ¿Cuántos m³ tiene el banco in situ?", "20*15*10", "Se multiplican largo, ancho y alto.", " m³"),
        ("=", "{F} ¿Cuántos m³ sueltos hay después del esponjamiento?", "20*15*10*125//100", "Se aumenta el volumen in situ en un 25 %.", " m³"),
        ("=", "{F} ¿Cuántos viajes de camión se necesitan?", "20*15*10*125//100//50", "Se divide el volumen suelto entre la capacidad del camión.", " viajes"),
        ("=", "{F} ¿Cuántas toneladas pesa el material del banco?", "20*15*10*3", "Se multiplica el volumen in situ por la densidad.", " t"),
        ("=", "{F} ¿Cuántas toneladas por hora llegan al chancado si se mueve todo el banco en 15 horas?", "20*15*10*3//15", "Se dividen las toneladas totales entre las horas.", " t/h"),
        ("abc", "{F} ¿El flujo calculado es compatible con la capacidad del chancado?", "Sí, porque 600 t/h es menor que las 700 t/h que puede recibir", "No, porque supera las 700 t/h", "No, porque el chancado debe recibir exactamente 700 t/h", "El flujo debe ser menor o igual que la capacidad del chancado."),
        ("=", "{F} ¿Cuántos viajes por hora se necesitan para cumplir las 15 horas?", "20*15*10*125//100//50//15", "Se dividen los viajes totales entre las horas disponibles.", " viajes/h"),
        ("=", "{F} Cada camión hace 1 viaje por hora. ¿Cuántos camiones se necesitan?", "20*15*10*125//100//50//15//1", "Se dividen los viajes por hora entre los viajes por hora de cada camión.", " camiones"),
        ("abc", "{F} Un asistente propone mover todo el banco en 5 horas para terminar antes. ¿Qué corresponde evaluar?", "Que el flujo sería de 1.800 t/h, mucho más de lo que el chancado puede recibir", "Que 5 horas es el tiempo ideal para cualquier banco", "Que no importa el flujo si hay más camiones", "El flujo es la carga de toneladas dividida entre las horas y debe respetar al chancado."),
        ("abc", "Una persona te cuenta que, en una zona de descarga de ejemplo, un camión retrocede hacia una persona que no lo ve. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Correr a ponerte detrás del camión", "Hacer señas con los brazos desde cerca", "Acercarse al camión que retrocede puede causar otro atropello."),
    ],
    ctx=("abc", "Una compañera de práctica calcula las toneladas de un banco de 100 m³ in situ con densidad 3 t/m³ y esponjamiento de 25 %, y escribe «125 m³ × 3 = 375 t». ¿Qué respondes?", "Que el tonelaje se calcula con el volumen in situ: 100 × 3 son 300 t, porque la masa no cambia al esponjar", "Que está correcto, porque se usa el volumen suelto", "Que son 100 t porque se divide entre la densidad", "El esponjamiento aumenta el volumen, pero la masa del material sigue igual."),
    sc=[
        ("En Explotación Minera: ¿cómo se calcula el volumen de un banco?", "Largo por ancho por alto", "Es el volumen de una caja."),
        ("En Explotación Minera: ¿cómo se calcula el flujo hacia el chancado?", "Toneladas totales divididas entre las horas", "El flujo se expresa en toneladas por hora."),
        ("En Explotación Minera: ¿por qué se calcula el tonelaje con el volumen in situ?", "Porque la masa no cambia al remover la roca", "El esponjamiento solo cambia el volumen."),
    ],
    op=("Planilla ficticia de la faena «Mina Demo Cerro Claro»: banco de 10 m de largo, 6 m de ancho y 4 m de alto; esponjamiento de 25 %; camiones de 25 m³ sueltos; densidad in situ de 2 toneladas por m³; se debe mover todo en 4 horas; cada camión hace 1 viaje por hora; el chancado recibe hasta 150 toneladas por hora. Escribe (a) el volumen in situ y el suelto, (b) los viajes y los camiones necesarios, (c) las toneladas y el flujo por hora, (d) si el flujo es compatible con el chancado.",
        "(a) 10 × 6 × 4 = 240 m³ in situ y 240 × 125 ÷ 100 = 300 m³ sueltos. (b) 300 ÷ 25 = 12 viajes; 12 ÷ 4 = 3 viajes por hora, es decir, 3 camiones. (c) 240 × 2 = 480 t; 480 ÷ 4 = 120 t/h. (d) Sí, porque 120 es menor que 150.",
        ["calcula volúmenes", "calcula viajes y camiones", "calcula toneladas y flujo", "compara con la capacidad del chancado"],
        ["hoja con las cuatro respuestas"],
        ["calcular los viajes con el volumen in situ", "usar el volumen suelto para el tonelaje", "olvidar comparar con el chancado"],
        "Pregunta: «¿qué volumen usas para los viajes y cuál para las toneladas?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un banco de 12 × 10 × 5 m, define esponjamiento y camión, y calcula los viajes.",
    extend="Explica con un ejemplo por qué mover un banco demasiado rápido puede ser un problema para el chancado.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 31 (caso de ejemplo, inventado). La planta de beneficio ficticia «Planta Demo Quebrada Seca» recibe roca de la mina en una tolva de recepción; un alimentador la pasa al chancador primario, que reduce su tamaño, y una correa transportadora la lleva a la pila de acopio. "
     "Matriz de peligros del chancado primario: polvo (probabilidad 5 y gravedad 3), ruido (probabilidad 4 y gravedad 3), partes en movimiento (probabilidad 2 y gravedad 5) y arranque inesperado de un equipo mientras alguien lo interviene (probabilidad 2 y gravedad 4). "
     "Regla de la matriz de ejemplo: puntaje de riesgo = probabilidad × gravedad. Personal de ejemplo en un turno: 3 personas en la sala de control, 5 en la planta y 4 en mantención.")
build(
    O8, 1, F,
    use="Aprenderé qué es el chancado primario, qué peligros tiene, qué papel cumplen el control y la automatización, y por qué solo personal autorizado opera o interviene los equipos.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé calcular un puntaje multiplicando dos números.", "Sé que las tareas de riesgo las hacen personas autorizadas."],
    explain=[
        "El chancado primario es la primera reducción de tamaño de la roca que llega de la mina, en una planta de beneficio, que es la instalación donde se trata el mineral para separar el metal. La roca entra por una tolva, que es un recipiente que recibe y guarda el material; un alimentador la entrega al chancador, que es la máquina que la rompe; y una correa transportadora la lleva a la etapa siguiente. Los equipos modernos tienen sistemas de control y automatización: sensores, alarmas y programas que vigilan y comandan la planta desde una sala de control.",
        "Los peligros son el polvo, el ruido, las partes en movimiento y el arranque inesperado de un equipo mientras alguien lo interviene. Para evitar ese arranque existe el bloqueo y etiquetado, un método de la empresa que aplica solo personal capacitado y autorizado; este cuaderno solo lo nombra y no lo enseña como procedimiento. El polvo y el ruido también afectan al ambiente, por lo que la empresa debe cumplir las normas de seguridad y de protección del medio ambiente.",
        f"En la matriz de ejemplo, el puntaje de riesgo es probabilidad por gravedad y se atiende primero el mayor. Operar o intervenir un chancador exige formación, autorización y permiso. {EMER} {AVISO}",
    ],
    vocab=[("chancado primario", "primera reducción de tamaño de la roca que llega de la mina"), ("planta de beneficio", "instalación donde se trata el mineral para separar el metal"), ("tolva", "recipiente que recibe y guarda el material"), ("chancador", "máquina que rompe la roca para reducir su tamaño"), ("sala de control", "lugar desde donde se vigila y comanda la planta"), ("automatización", "uso de sensores y programas para vigilar y comandar equipos"), ("bloqueo y etiquetado", "método de la empresa para impedir que un equipo se encienda mientras alguien lo interviene")],
    worked=[
        ("Puntaje de riesgo", "En la matriz de ejemplo de una sala de bombas, el piso mojado tiene probabilidad 4 y gravedad 2. ¿Qué puntaje resulta?", ["Se multiplica la probabilidad por la gravedad.", "4 por 2 son 8."], "8 puntos"),
        ("Peligro y riesgo", "En una escalera de acceso de ejemplo falta un peldaño. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el peldaño que falta.", "El riesgo es que una persona caiga."], "Peligro: el peldaño que falta; riesgo: que una persona caiga"),
    ],
    mistakes=[("Creer que quien entiende cómo funciona el chancado ya puede intervenirlo.", "Intervenir un chancador exige formación, autorización, permiso y bloqueo y etiquetado.", "Aprende el concepto aquí y deja la tarea a personal autorizado."),
              ("Creer que la sala de control hace innecesaria la seguridad en terreno.", "La automatización ayuda a vigilar, pero no elimina los peligros del equipo.", "Los peligros siguen existiendo aunque el equipo se comande a distancia.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es el chancado primario?", "La primera reducción de tamaño de la roca que llega de la mina", "La separación final del metal en la planta", "El transporte del mineral por los caminos", "El chancado primario rompe la roca; la separación del metal es otra etapa."),
        ("abc", "En Explotación Minera: ¿qué es una tolva?", "Un recipiente que recibe y guarda el material", "Una máquina que rompe la roca", "Una cinta que transporta el mineral", "La tolva recibe el material; el chancador lo rompe."),
        ("abc", "En Explotación Minera: ¿qué es la automatización de una planta?", "El uso de sensores y programas para vigilar y comandar equipos", "El cambio de turnos del personal", "El pesaje de los camiones", "La automatización usa sensores y programas, no cambia los turnos."),
        ("=", "{F} ¿Cuántas personas hay en total en el turno de la ficha?", "3+5+4", "Se suman las personas de la sala de control, la planta y mantención.", " personas"),
        ("abc", "{F} ¿Cuál es el riesgo asociado al peligro «partes en movimiento»?", "Que una persona sufra un atrapamiento o un golpe grave", "Que el equipo se calienta", "Que la correa se desgaste", "El riesgo es el daño posible a las personas."),
        ("abc", "{F} ¿Para qué existe el bloqueo y etiquetado, según la explicación?", "Para impedir que un equipo se encienda mientras alguien lo interviene", "Para aumentar la producción del chancador", "Para anotar la hora de cada turno", "Evita el arranque inesperado mientras una persona interviene el equipo."),
        ("=", "{F} ¿Qué puntaje de riesgo tiene el polvo?", "5*3", "Se multiplica la probabilidad por la gravedad anotadas en la ficha.", " puntos"),
        ("=", "{F} ¿Qué puntaje de riesgo tiene el ruido?", "4*3", "Se multiplican la probabilidad y la gravedad de ese peligro.", " puntos"),
        ("abc", "{F} Con la regla de la matriz, ¿cuál de los cuatro peligros debe atenderse primero?", "El polvo, porque tiene el mayor puntaje (15)", "Las partes en movimiento, porque su gravedad es la más alta (5)", "El arranque inesperado, porque es el menos probable", "Se atiende primero el mayor puntaje, que combina probabilidad y gravedad."),
        ("abc", "{F} Un joven en práctica dice: «entiendo cómo funciona el chancador, así que puedo ayudar a limpiarlo mientras está detenido». ¿Qué es correcto?", "No: intervenir un chancador exige formación, autorización, permiso y bloqueo y etiquetado", "Sí, si el chancador está apagado", "Sí, si un compañero lo vigila", "Que parezca detenido no basta: puede arrancar si no hay bloqueo."),
        ("abc", "{F} ¿Por qué la sala de control no elimina los peligros del chancador?", "Porque los peligros de las partes en movimiento y del polvo siguen existiendo aunque se comande a distancia", "Porque la sala de control está lejos del chancador", "Porque la sala de control solo vigila el ruido", "La automatización ayuda a vigilar, pero no quita los peligros."),
        ("=", "{F} Para un simulacro, el personal de planta y el de mantención se reparte en grupos de 3 personas. ¿Cuántos grupos se forman?", "(5+4)//3", "Se suma el personal de las dos áreas y se divide entre las personas de cada grupo.", " grupos"),
        ("abc", "Durante una visita de ejemplo, ves que la manga de un compañero queda atrapada en una correa transportadora en movimiento. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a jalar a tu compañero", "Intentar detener la correa con las manos", "Acercarte a una correa en movimiento puede atrapar a una segunda persona."),
    ],
    ctx=("abc", "Un contratista de ejemplo te dice: «Está detenido el chancador, ayúdame a sacar unas piedras de adentro, nadie lo va a encender». ¿Qué respondes?", "Que no, porque intervenir exige formación, autorización, permiso y bloqueo y etiquetado, y que consultarás a un adulto responsable", "Que sí, si hay buena luz", "Que sí, si lo haces rápido", "Un equipo detenido puede arrancar si no está bloqueado."),
    sc=[
        ("En Explotación Minera: ¿qué hace el chancador?", "Rompe la roca para reducir su tamaño", "Es la máquina central del chancado primario."),
        ("En Explotación Minera: ¿qué es una sala de control?", "El lugar desde donde se vigila y comanda la planta", "Allí se ven las alarmas y los datos de los equipos."),
        ("¿Cómo se calcula el puntaje de riesgo de la matriz de ejemplo?", "Probabilidad multiplicada por gravedad", "El puntaje combina cuán probable y cuán grave es el daño."),
    ],
    op=("La planta ficticia «Planta Demo Cerro Claro» tiene un chancador primario que recibe roca por una tolva y la entrega a una correa. Escribe (a) un peligro del chancado y su riesgo asociado, (b) para qué sirve el bloqueo y etiquetado y quién lo aplica, (c) por qué la sala de control no elimina los peligros, (d) qué haces si ves a alguien atrapado en la correa.",
        "(a) Peligro: las partes en movimiento; riesgo: un atrapamiento o un golpe grave. (b) Sirve para impedir que el equipo se encienda mientras alguien lo interviene, y lo aplica personal capacitado y autorizado. (c) Porque la automatización vigila, pero los peligros de los equipos siguen existiendo. (d) No acercarme a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "explica el bloqueo y etiquetado", "explica los límites de la automatización", "aplica la conducta de emergencia"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "creer que un equipo detenido es seguro", "acercarse a la correa"],
        "Pregunta: «¿por qué un equipo detenido puede ser peligroso?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa una matriz de tres peligros de una planta de chancado con probabilidad y gravedad, y calcula los puntajes.",
    extend="Explica con un ejemplo por qué el polvo del chancado es un tema de seguridad y también de medio ambiente.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 32 (documentos y datos de ejemplo, inventados). Diagrama de flujo de la «Planta Demo Piedra Azul»: tolva de recepción, con capacidad de 200 toneladas; alimentador; chancador primario; correa transportadora; pila de acopio. La roca entra con un tamaño máximo de 800 mm y el producto sale con un tamaño máximo de 200 mm. "
     "La razón de reducción es el tamaño de entrada dividido entre el tamaño de salida. La granulometría es la distribución de tamaños de un material. Sistema de control de ejemplo: un sensor de nivel de la tolva, una alarma de sobrecarga del chancador y un enclavamiento, que es una condición que impide arrancar o hace detener un equipo si no se cumple una condición de seguridad. "
     "Documentos: pauta de inspección, reporte de turno, registro de alarmas e instrucción de operación de la empresa. Roles: el operador de sala de control vigila las pantallas y las alarmas; el operador de planta recorre y reporta; el mantenedor interviene los equipos con autorización; el supervisor organiza; el laboratorista mide la granulometría.")
build(
    O8, 2, F,
    use="Aprenderé el vocabulario del chancado primario (razón de reducción, granulometría, sensor, alarma y enclavamiento), los documentos de un turno y el rol de cada persona.",
    prior=["Sé qué es el chancado primario.", "Sé dividir números enteros.", "Sé qué es un registro."],
    explain=[
        "Un diagrama de flujo muestra por dónde pasa el material en una planta. En el chancado primario el orden es: tolva, alimentador, chancador, correa y pila de acopio. La razón de reducción es el tamaño máximo de entrada dividido entre el tamaño máximo de salida; si entra roca de 800 mm y sale de 200 mm, la razón es 4. La granulometría es la distribución de tamaños del material y se controla midiendo qué parte pasa por una abertura determinada.",
        "El sistema de control tiene sensores, que miden una variable como el nivel de una tolva; alarmas, que avisan cuando algo sale de lo normal; y enclavamientos, que son condiciones que impiden arrancar o hacen detener un equipo si no se cumple una condición de seguridad. Un enclavamiento no se anula ni se salta: es una protección. Los documentos del turno son la pauta de inspección, el reporte de turno, el registro de alarmas y la instrucción de operación de la empresa.",
        f"Cada rol tiene su límite: el operador de sala vigila, el operador de planta recorre y reporta, el mantenedor interviene con autorización, el supervisor organiza y el laboratorista mide. {EMER} {AVISO}",
    ],
    vocab=[("diagrama de flujo", "dibujo que muestra por dónde pasa el material en una planta"), ("razón de reducción", "tamaño máximo de entrada dividido entre el tamaño máximo de salida"), ("granulometría", "distribución de tamaños de un material"), ("sensor", "dispositivo que mide una variable, como un nivel"), ("alarma", "aviso que se activa cuando algo sale de lo normal"), ("enclavamiento", "condición que impide arrancar o hace detener un equipo si no se cumple una condición de seguridad"), ("reporte de turno", "documento que resume lo ocurrido en un turno")],
    worked=[
        ("Razón de reducción", "Un chancador de ejemplo recibe roca de hasta 600 mm y entrega producto de hasta 150 mm. ¿Cuál es la razón de reducción?", ["Se divide el tamaño de entrada entre el de salida.", "600 dividido entre 150 son 4."], "4"),
        ("Leer una alarma", "Un sensor de ejemplo marca el nivel de una tolva y una alarma se activa cuando pasa del 90 %. El nivel marca 94 %. ¿Qué ocurre y qué corresponde?", ["El nivel superó el límite de la alarma.", "La alarma se activa y se informa al supervisor; nadie la anula."], "La alarma se activa y se informa"),
    ],
    mistakes=[("Creer que se puede anular una alarma que molesta para seguir produciendo.", "Una alarma es una protección: avisa de una condición fuera de lo normal.", "Registra la alarma e informa al supervisor."),
              ("Dividir el tamaño de salida entre el de entrada al calcular la razón de reducción.", "La razón de reducción es entrada dividida entre salida.", "Ordena la división: primero el tamaño de entrada.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es la razón de reducción de un chancador?", "El tamaño máximo de entrada dividido entre el de salida", "El tamaño de salida dividido entre el de entrada", "El peso de la roca dividido entre las horas", "La razón de reducción compara cuánto se reduce el tamaño."),
        ("abc", "En Explotación Minera: ¿qué es la granulometría?", "La distribución de tamaños de un material", "El peso de un camión cargado", "La velocidad de una correa", "La granulometría describe los tamaños de las partículas."),
        ("abc", "En Explotación Minera: ¿qué es un enclavamiento?", "Una condición que impide arrancar o hace detener un equipo si no se cumple una condición de seguridad", "Un cable que une dos equipos", "Un registro de las horas de trabajo", "Un enclavamiento es una protección que depende de condiciones de seguridad."),
        ("=", "{F} ¿Cuál es la razón de reducción del chancador de la ficha?", "800//200", "Se divide el tamaño máximo de entrada entre el de salida.", ""),
        ("abc", "{F} ¿Cuál es el orden correcto del flujo del material en el diagrama?", "Tolva, alimentador, chancador, correa y pila de acopio", "Chancador, tolva, alimentador, pila de acopio y correa", "Alimentador, tolva, correa, chancador y pila de acopio", "El material entra por la tolva y sale a la pila de acopio."),
        ("abc", "{F} ¿Qué rol vigila las pantallas y las alarmas?", "El operador de sala de control", "El mantenedor", "El laboratorista", "La sala de control vigila; el mantenedor interviene los equipos."),
        ("abc", "{F} ¿Qué documento resume lo ocurrido en el turno?", "El reporte de turno", "La pauta de inspección", "La instrucción de operación", "El reporte de turno resume el turno."),
        ("=", "{F} Si el producto saliera con un tamaño máximo de 100 mm en lugar de 200 mm, ¿cuál sería la razón de reducción?", "800//100", "Se divide el tamaño de entrada entre el nuevo tamaño de salida.", ""),
        ("=", "{F} La tolva se llena a 8 toneladas por minuto y no sale material. ¿En cuántos minutos se llenan sus 200 toneladas?", "200//8", "Se divide la capacidad de la tolva entre las toneladas que entran por minuto.", " min"),
        ("abc", "{F} Una alarma de sobrecarga del chancador molesta al operador de planta, que propone anularla «para que no siga sonando». ¿Qué corresponde?", "No anularla: se registra e informa al supervisor, que decide con personal autorizado", "Anularla si suena muchas veces", "Anularla si la sala de control no lo nota", "Una alarma es una protección, no una molestia."),
        ("abc", "{F} ¿Por qué el enclavamiento no se salta aunque haga perder tiempo?", "Porque protege a las personas al impedir un arranque o una operación insegura", "Porque ahorra energía", "Porque evita que la correa se gaste", "Un enclavamiento existe para proteger a las personas y a los equipos."),
        ("abc", "{F} ¿Quién interviene los equipos y con qué condición?", "El mantenedor, con autorización", "El operador de sala, con su contraseña", "El laboratorista, si pasa por la planta", "La intervención de equipos exige autorización."),
        ("abc", "Un compañero te cuenta que en una planta de ejemplo salió humo del motor de una correa y que hay un trabajador cerca. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a apagar el motor", "Echar agua al motor", "Un motor con humo puede incendiarse o tener energía; hay que avisar."),
    ],
    ctx=("abc", "Un compañero de práctica lee la ficha y dice: «la razón de reducción es 200 ÷ 800 = 0,25». ¿Qué respondes?", "Que se divide el tamaño de entrada entre el de salida: 800 ÷ 200 = 4", "Que está correcto, porque se divide el producto entre la roca", "Que es 1.000, porque se suman los dos tamaños", "La razón de reducción pone el tamaño de entrada arriba y el de salida abajo."),
    sc=[
        ("En Explotación Minera: ¿cómo se calcula la razón de reducción?", "Tamaño de entrada dividido entre tamaño de salida", "La entrada es siempre mayor que la salida."),
        ("En Explotación Minera: ¿qué hace un sensor?", "Mide una variable, como el nivel de una tolva", "Los sensores alimentan a las alarmas y al control."),
        ("En Explotación Minera: ¿qué se hace con una alarma?", "Se registra y se informa, sin anularla", "Silenciarla no soluciona el problema que la causó."),
    ],
    op=("Diagrama ficticio de la «Planta Demo Cerro Claro»: tolva de 120 toneladas, alimentador, chancador que recibe roca de hasta 900 mm y entrega producto de hasta 150 mm, y correa. Escribe (a) la razón de reducción, (b) qué hace un sensor de nivel en la tolva, (c) qué haces si suena la alarma de nivel alto, (d) qué rol interviene los equipos.",
        "(a) 900 ÷ 150 = 6. (b) Mide el nivel de la tolva y envía el dato al sistema de control. (c) Se registra e informa al supervisor; nadie anula la alarma. (d) El mantenedor, con autorización.",
        ["calcula la razón de reducción", "explica la función del sensor", "describe la conducta ante una alarma", "asigna el rol de intervención"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "anular la alarma", "creer que el operador de sala interviene los equipos"],
        "Pregunta: «¿cuál va arriba en la división, la entrada o la salida?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un chancador con tamaños de entrada y salida y calcula su razón de reducción.",
    extend="Explica con un ejemplo por qué una alarma silenciada puede ser más peligrosa que una alarma que suena.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 33 (caso de ejemplo, inventado). Reporte de un turno de 12 horas del chancado primario de la «Planta Demo Lomas Bajas». Toneladas procesadas: 7.200. Horas operando: 9. Paradas: 1 hora por falta de alimentación, 1 hora por mantención programada y 1 hora por falla de un sensor. "
     "Meta de ejemplo: al menos 750 toneladas por hora operando. Alarmas del turno: 3 alarmas de nivel alto de tolva, atendidas por la sala de control; y a las 15:20, una alarma de sobrecarga del chancador. "
     "Reglas de ejemplo: toda alarma se registra con su hora y se informa al supervisor; nadie anula una alarma para seguir produciendo; tras una alarma de sobrecarga, el chancador no se vuelve a arrancar hasta que personal autorizado lo revise.")
build(
    O8, 3, F,
    use="Aprenderé a analizar en papel el reporte de un turno de chancado: calcular toneladas por hora, porcentajes de tiempo y cumplimiento de meta, y decidir qué se informa ante una alarma.",
    prior=["Sé qué es una alarma y un reporte de turno.", "Sé dividir números enteros.", "Sé calcular un porcentaje."],
    explain=[
        "El rendimiento de un chancado se expresa en toneladas por hora operando: toneladas procesadas divididas entre las horas en que realmente funcionó. Las horas de parada se restan del tiempo del turno y se dividen en tipos: por falta de alimentación, por mantención programada y por falla. El porcentaje de tiempo operando es las horas operando por 100, divididas entre las horas del turno.",
        "Una meta se compara con el rendimiento: si lo iguala o lo supera, cumple. Las alarmas se registran con su hora y se informan al supervisor; una alarma de sobrecarga indica que el chancador recibió más de lo que puede romper, y nadie vuelve a arrancarlo hasta que personal autorizado lo revise. Anular una alarma para seguir produciendo es una falta grave.",
        f"Este análisis es de papel: operar o reiniciar un chancador real exige personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("rendimiento", "toneladas procesadas por hora operando"), ("parada", "tiempo en que el equipo no funciona"), ("mantención programada", "parada planificada para revisar o reparar un equipo"), ("sobrecarga del chancador", "situación en que recibe más material del que puede romper"), ("meta", "valor que se quiere alcanzar")],
    worked=[
        ("Rendimiento", "Un chancador de ejemplo procesó 4.500 toneladas en 6 horas operando. ¿Cuál es el rendimiento?", ["Se dividen las toneladas entre las horas operando.", "4.500 dividido entre 6 son 750 t/h."], "750 t/h"),
        ("Tiempo operando", "En un turno de ejemplo de 8 horas, el equipo operó 6. ¿Qué porcentaje del tiempo operó?", ["Se multiplican por 100 las horas operando y se divide entre las del turno.", "6 por 100 dividido entre 8 son 75."], "75 %"),
    ],
    mistakes=[("Dividir las toneladas entre las horas del turno completo en lugar de las horas operando.", "El rendimiento se mide mientras el equipo funciona.", "Usa las horas operando."),
              ("Anular una alarma de sobrecarga y volver a arrancar el chancador sin revisión.", "Tras una alarma de sobrecarga, el equipo se revisa por personal autorizado antes de arrancarlo.", "Registra la alarma, informa y espera la revisión.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es el rendimiento de un chancado?", "Las toneladas procesadas por hora operando", "Las horas de parada del turno", "El peso de la roca que llega a la tolva", "El rendimiento compara toneladas con horas operando."),
        ("abc", "En Explotación Minera: ¿qué es una mantención programada?", "Una parada planificada para revisar o reparar un equipo", "Una falla inesperada de un equipo", "Un turno sin trabajo", "Programada significa que se planifica con anticipación y no es una falla."),
        ("abc", "En Explotación Minera: ¿qué indica una alarma de sobrecarga del chancador?", "Que recibió más material del que puede romper", "Que el turno terminó", "Que la correa está vacía", "La sobrecarga ocurre cuando entra más material del que el equipo procesa."),
        ("=", "{F} ¿Cuántas horas de parada tuvo el turno en total?", "1+1+1", "Se suman las horas de parada por los tres motivos.", " horas"),
        ("=", "{F} ¿Cuántas horas tuvo el turno en total entre operando y paradas?", "9+1+1+1", "Se suman las horas operando y las horas de parada.", " horas"),
        ("=", "{F} ¿Cuál fue el rendimiento del chancado en toneladas por hora operando?", "7200//9", "Se dividen las toneladas procesadas entre las horas operando.", " t/h"),
        ("abc", "{F} ¿Cumplió el turno la meta de al menos 750 t/h?", "Sí, porque 800 es mayor que 750", "No, porque tuvo paradas", "No, porque hubo una alarma de sobrecarga", "La meta se compara con el rendimiento, no con las paradas."),
        ("=", "{F} ¿Qué porcentaje del turno estuvo operando el chancado?", "9*100//12", "Se multiplican por 100 las horas operando y se divide entre las horas del turno.", " %"),
        ("=", "{F} ¿Cuántas toneladas más que la meta se procesaron en las horas operando?", "7200-750*9", "Se resta lo que daría la meta en 9 horas a lo procesado.", " t"),
        ("abc", "{F} ¿Qué se hace con la alarma de las 15:20?", "Se registra con su hora, se informa al supervisor y no se arranca hasta la revisión", "Se anula para recuperar la producción", "Se anota solo si el equipo se detiene", "La regla exige registrar, informar y esperar la revisión."),
        ("abc", "{F} Un operador propone volver a arrancar el chancador de inmediato para recuperar producción. ¿Qué corresponde?", "No hacerlo: personal autorizado debe revisar el equipo antes de cualquier arranque", "Hacerlo si la alarma ya dejó de sonar", "Hacerlo si la sala de control lo permite", "Tras una sobrecarga, el equipo se revisa antes de arrancar."),
        ("abc", "{F} ¿Por qué las 3 alarmas de nivel alto, aunque se atendieron, deben registrarse?", "Porque el registro permite ver si el problema se repite y corregir su causa", "Porque se pagan por alarma registrada", "Porque las alarmas se borran solas", "El registro sirve para analizar causas y prevenir repeticiones."),
        ("abc", "Una persona te cuenta que, en una planta de ejemplo, una piedra grande se atascó en el chancador y alguien se subió a sacarla con una barra. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Subir a ayudarlo con otra barra", "Encender el chancador para soltar la piedra", "Intervenir un chancador sin bloqueo puede causar un accidente grave."),
    ],
    ctx=("abc", "Un jefe de ejemplo mira el reporte y dice: «rendimos 800 t/h, más que la meta, así que no hace falta informar la alarma de sobrecarga». ¿Qué respondes?", "Que toda alarma se registra e informa, aunque la meta se cumpla, y que el chancador se revisa antes de volver a arrancarlo", "Que tiene razón, porque la meta se cumplió", "Que se informa solo si se detiene el turno", "La meta no reemplaza la regla de registrar e informar alarmas."),
    sc=[
        ("En Explotación Minera: ¿cómo se calcula el rendimiento de un chancado?", "Toneladas procesadas divididas entre horas operando", "Se mide mientras el equipo funciona."),
        ("En Explotación Minera: ¿qué se hace con una alarma?", "Se registra con su hora y se informa al supervisor", "Nadie anula una alarma para seguir produciendo."),
        ("¿Qué se hace tras una alarma de sobrecarga?", "No se arranca hasta que personal autorizado revise el equipo", "El equipo puede tener un daño que no se ve."),
    ],
    op=("Reporte ficticio de un turno de 12 horas de la «Planta Demo Cerro Claro»: toneladas procesadas 5.400; horas operando 6; paradas: 3 horas por falta de alimentación y 3 horas por una falla; meta de ejemplo de 850 toneladas por hora operando; a las 09:40 sonó una alarma de sobrecarga. Escribe (a) el rendimiento, (b) si cumple la meta, (c) el porcentaje del turno que estuvo operando, (d) qué haces con la alarma de las 09:40.",
        "(a) 5.400 ÷ 6 = 900 t/h. (b) Sí, porque 900 es mayor que 850. (c) 6 × 100 ÷ 12 = 50 %. (d) Se registra con su hora, se informa al supervisor y no se arranca hasta que personal autorizado revise el equipo.",
        ["calcula el rendimiento", "compara con la meta", "interpreta el tiempo operando", "describe la conducta ante la alarma"],
        ["hoja con las cuatro respuestas"],
        ["usar las horas del turno en vez de las horas operando", "anular la alarma", "confundir paradas con horas operando"],
        "Pregunta: «¿qué horas usaste para dividir las toneladas?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un turno de 10 horas con 7 operando y 1.400 toneladas, y calcula el rendimiento.",
    extend="Explica con un ejemplo por qué una meta cumplida no justifica saltarse una regla de seguridad.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 34 (planilla de ejemplo, inventada). Indicadores de un día del chancado primario de la «Planta Demo Río Hondo». Horas del día: 24. Mantención programada: 2 horas. Paradas por falla: 4 horas. Horas operando: 9. Toneladas procesadas: 6.300. Capacidad nominal (máxima de diseño, de ejemplo): 1.000 toneladas por hora. "
     "Definiciones de ejemplo: horas disponibles = horas del día − mantención programada − paradas por falla; disponibilidad = horas disponibles × 100 ÷ horas del día; utilización = horas operando × 100 ÷ horas disponibles. "
     "Calidad: de una muestra de 100 kg del producto, 90 kg pasan por una abertura de 200 mm; estándar de ejemplo: al menos 85 % del producto debe pasar por esa abertura. Para controlar el polvo se usa agua: 3 m³ por cada hora operando (valor de ejemplo).")
build(
    O8, 4, F,
    use="Aprenderé a calcular en una planilla la disponibilidad, la utilización, el rendimiento, el porcentaje de la capacidad, el cumplimiento de un estándar de calidad y el consumo de agua para controlar el polvo.",
    prior=["Sé qué es el rendimiento.", "Sé calcular un porcentaje.", "Sé qué es la granulometría."],
    explain=[
        "La disponibilidad es qué parte del día el equipo estuvo en condiciones de funcionar: se restan al día la mantención programada y las paradas por falla, y se compara con las horas del día. La utilización es qué parte de ese tiempo disponible el equipo realmente operó. El porcentaje de la capacidad es el rendimiento dividido entre la capacidad nominal, por 100.",
        "La calidad del producto se mide con la granulometría: se toma una muestra y se calcula qué porcentaje pasa por una abertura dada. Si ese porcentaje es igual o mayor que el estándar, el producto cumple. El agua para controlar el polvo es una medida de protección del medio ambiente y de las personas: se calcula multiplicando las horas operando por el consumo por hora.",
        f"Estos valores son de ejemplo; los reales los fijan el diseño de la planta, la empresa y la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("disponibilidad", "porcentaje del día en que el equipo estuvo en condiciones de funcionar"), ("utilización", "porcentaje del tiempo disponible en que el equipo realmente operó"), ("capacidad nominal", "máximo de toneladas por hora para el que fue diseñado el equipo"), ("estándar de calidad", "valor mínimo que debe cumplir el producto"), ("control de polvo", "uso de medidas, como el agua, para reducir el polvo")],
    worked=[
        ("Disponibilidad", "Un equipo de ejemplo trabaja en un turno de 10 horas, con 1 hora de mantención programada y 1 hora de falla. ¿Cuál es su disponibilidad?", ["Las horas disponibles son 10 menos 2, es decir, 8.", "8 por 100 dividido entre 10 son 80."], "80 %"),
        ("Porcentaje de la capacidad", "Un chancador de ejemplo con capacidad nominal de 500 t/h trabaja a 450 t/h. ¿Qué porcentaje de su capacidad usa?", ["Se divide el rendimiento entre la capacidad nominal.", "450 por 100 dividido entre 500 son 90."], "90 %"),
    ],
    mistakes=[("Calcular la utilización dividiendo las horas operando entre las 24 horas del día.", "La utilización se compara con las horas disponibles.", "Usa las horas disponibles como base."),
              ("Considerar que cumple el estándar solo si el porcentaje es mayor que 85, y rechazar el 85 exacto.", "«Al menos» incluye el valor exacto.", "Compara con «igual o mayor».")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es la disponibilidad de un equipo?", "El porcentaje del día en que estuvo en condiciones de funcionar", "El porcentaje del tiempo en que realmente operó", "El porcentaje de su capacidad que usó", "La disponibilidad se refiere a poder funcionar, no a haber operado."),
        ("abc", "En Explotación Minera: ¿qué es la utilización de un equipo?", "El porcentaje del tiempo disponible en que realmente operó", "El porcentaje del día en que estuvo detenido", "El porcentaje de producto que cumple el estándar", "La utilización compara las horas operando con las horas disponibles."),
        ("abc", "En Explotación Minera: ¿qué es la capacidad nominal?", "El máximo de toneladas por hora para el que fue diseñado el equipo", "Las toneladas que procesó el equipo ayer", "El tamaño de la roca más grande", "La capacidad nominal es el máximo de diseño."),
        ("=", "{F} ¿Cuántas horas disponibles tuvo el equipo en el día?", "24-2-4", "Se restan al día la mantención programada y las paradas por falla.", " horas"),
        ("=", "{F} ¿Cuál fue la disponibilidad del equipo?", "(24-2-4)*100//24", "Se multiplican por 100 las horas disponibles y se divide entre las horas del día.", " %"),
        ("=", "{F} ¿Cuál fue la utilización del equipo?", "9*100//(24-2-4)", "Se multiplican por 100 las horas operando y se divide entre las horas disponibles.", " %"),
        ("=", "{F} ¿Cuál fue el rendimiento del chancado en toneladas por hora operando?", "6300//9", "Se dividen las toneladas procesadas entre las horas operando.", " t/h"),
        ("=", "{F} ¿Qué porcentaje de la capacidad nominal usó el chancador?", "700*100//1000", "Se divide el rendimiento entre la capacidad nominal y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Cumple el producto el estándar de calidad de ejemplo?", "Sí, porque 90 % es mayor que el 85 % exigido", "No, porque 90 kg es menos que 100 kg", "No, porque debe pasar el 100 %", "El estándar pide al menos 85 % y la muestra alcanzó 90 %."),
        ("=", "{F} ¿Cuántos metros cúbicos de agua se usan en el día para controlar el polvo?", "3*9", "Se multiplican las horas operando por el consumo por hora.", " m³"),
        ("abc", "{F} Un jefe propone aumentar la utilización anotando 12 horas operando aunque fueron 9. ¿Qué corresponde?", "Rechazarlo: el registro debe decir las horas reales, porque alterarlo oculta problemas", "Aceptarlo si mejora el indicador", "Aceptarlo si lo aprueba el supervisor", "Un indicador se calcula con datos reales."),
        ("=", "{F} Si se eliminara la parada por falla, ¿cuántas horas disponibles tendría el equipo?", "24-2", "Se resta solo la mantención programada al día.", " horas"),
        ("abc", "Una persona te cuenta que, en una planta de ejemplo, un camión descargó mal y una persona cayó a la tolva. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte al borde de la tolva a mirar", "Bajar a la tolva a ayudar", "Una tolva es una zona de gran riesgo; el rescate lo hacen equipos formados."),
    ],
    ctx=("abc", "Una compañera de práctica dice: «utilizamos el equipo 9 horas de 24, es decir, 37,5 %, la utilización es muy baja». ¿Qué respondes?", "Que la utilización se compara con las horas disponibles, 18, y da 50 %, porque las horas de mantención y de falla no estaban disponibles", "Que está correcto, porque se divide entre las 24 horas", "Que son 9 % porque se divide entre 100", "La utilización usa como base el tiempo disponible, no el día completo."),
    sc=[
        ("En Explotación Minera: ¿cómo se calcula la disponibilidad?", "Horas disponibles por 100, divididas entre las horas del día", "Las horas disponibles descuentan mantención y fallas."),
        ("En Explotación Minera: ¿cómo se calcula el porcentaje de la capacidad?", "Rendimiento por 100, dividido entre la capacidad nominal", "Compara lo que el equipo procesa con su máximo de diseño."),
        ("¿Para qué se usa agua en el chancado?", "Para controlar el polvo", "El agua reduce el polvo y protege a las personas y al ambiente."),
    ],
    op=("Planilla ficticia de la «Planta Demo Cerro Claro»: día de 24 horas, 4 horas de mantención programada, 8 horas de falla, 9 horas operando, 5.400 toneladas procesadas, capacidad nominal de 750 toneladas por hora y consumo de agua de 2 m³ por hora operando. Escribe (a) las horas disponibles y la disponibilidad, (b) la utilización, (c) el rendimiento y el porcentaje de la capacidad, (d) el agua usada en el día.",
        "(a) 24 − 4 − 8 = 12 horas; 12 × 100 ÷ 24 = 50 %. (b) 9 × 100 ÷ 12 = 75 %. (c) 5.400 ÷ 9 = 600 t/h; 600 × 100 ÷ 750 = 80 %. (d) 2 × 9 = 18 m³.",
        ["calcula las horas disponibles", "calcula la utilización", "calcula el rendimiento y el porcentaje de la capacidad", "calcula el agua usada"],
        ["hoja con las cuatro respuestas"],
        ["no restar la mantención y la falla", "usar las 24 horas para la utilización", "olvidar multiplicar el agua por las horas operando"],
        "Pregunta: «¿entre qué número dividiste en la utilización?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un día con 3 horas de mantención, 3 de falla y 9 operando, y calcula la disponibilidad y la utilización.",
    extend="Explica con un ejemplo por qué la utilización puede ser baja aunque la disponibilidad sea alta.",
)

# ============================================================ OAE-08, clase 5
F = ("Ficha 35 (informes de ejemplo, inventados). Dos turnos de 12 horas del chancado primario de la «Planta Demo Piedra Azul». Turno A: 7.200 toneladas, 9 horas operando; el 90 % del producto pasa por la abertura de 200 mm; sonaron 2 alarmas de sobrecarga que no se registraron; y se derramó mineral junto a la correa sin que se informara. "
     "Turno B: 6.000 toneladas, 8 horas operando; el 96 % del producto pasa por la abertura de 200 mm; todas las alarmas se registraron e informaron; no hubo derrames. "
     "Criterios obligatorios de ejemplo: (1) al menos 90 % del producto bajo 200 mm; (2) todas las alarmas registradas e informadas; (3) todo derrame informado. Meta de producción de ejemplo: al menos 700 toneladas por hora operando.")
build(
    O8, 5, F,
    use="Aprenderé a comparar dos turnos de chancado frente a criterios obligatorios y a una meta de producción, y a verificar la calidad de un reporte antes de decidir.",
    prior=["Sé calcular el rendimiento.", "Sé qué es un criterio obligatorio.", "Sé qué es una alarma."],
    explain=[
        "Comparar dos turnos exige más que mirar quién produjo más. Primero se revisan los criterios obligatorios: calidad del producto, alarmas registradas e informadas y derrames informados. Un turno que incumple un criterio obligatorio no cumple los estándares, aunque haya producido más. Recién después se compara la producción con la meta, y el rendimiento se calcula como toneladas divididas entre horas operando.",
        "Verificar la calidad de un reporte es comprobar que tenga los datos necesarios, que los números cuadren y que no falten registros. Una alarma no registrada o un derrame no informado es una no conformidad: se informa y se corrige, y no se oculta para mejorar el turno. El cuidado del medio ambiente incluye informar los derrames de mineral, el polvo y el uso del agua.",
        f"Este análisis es de papel: las decisiones reales las toma el supervisor con la información verificada. {EMER} {AVISO}",
    ],
    vocab=[("criterio obligatorio", "condición que un turno debe cumplir para cumplir los estándares"), ("no conformidad", "hallazgo que no cumple lo exigido y se registra e informa"), ("derrame", "caída de material fuera de su lugar, por ejemplo junto a la correa"), ("verificar un reporte", "comprobar que tenga los datos necesarios y que cuadren")],
    worked=[
        ("Elegir entre dos turnos", "Un turno de ejemplo X produjo más pero no informó un derrame; el turno Y produjo menos y cumplió todos los criterios. ¿Cuál cumple los estándares?", ["Un criterio obligatorio decide antes que la producción.", "El turno X incumple y el turno Y cumple."], "El turno Y"),
        ("Rendimiento", "Un turno de ejemplo procesó 4.800 toneladas en 6 horas operando. ¿Cuál es su rendimiento?", ["Se dividen las toneladas entre las horas operando.", "4.800 dividido entre 6 son 800 t/h."], "800 t/h"),
    ],
    mistakes=[("Elegir siempre el turno que produjo más.", "Un incumplimiento de un criterio obligatorio descalifica al turno, aunque produzca más.", "Primero revisa los criterios obligatorios y luego la producción."),
              ("No informar un derrame pequeño porque «es poco».", "Todo derrame se informa, para cuidar el ambiente y evitar accidentes.", "Informa y deja constancia.")],
    T=[
        ("abc", "En Explotación Minera: ¿qué es un criterio obligatorio al comparar turnos?", "Una condición que se debe cumplir para cumplir los estándares", "El turno con mayor producción", "El turno más corto", "Un criterio obligatorio se revisa antes de comparar la producción."),
        ("abc", "En Explotación Minera: ¿qué es un derrame de mineral?", "Material que cae fuera de su lugar, por ejemplo junto a la correa", "Una parada planificada del chancador", "Una alarma del sistema de control", "Un derrame es material fuera de su lugar y se informa."),
        ("abc", "En Explotación Minera: ¿qué significa verificar un reporte?", "Comprobar que tenga los datos necesarios y que cuadren", "Copiarlo en otro formato", "Firmarlo sin leerlo", "Verificar es comprobar datos y registros."),
        ("=", "{F} ¿Cuál fue el rendimiento del turno A en toneladas por hora operando?", "7200//9", "Se dividen las toneladas procesadas entre las horas operando.", " t/h"),
        ("=", "{F} ¿Cuál fue el rendimiento del turno B en toneladas por hora operando?", "6000//8", "Se dividen las toneladas procesadas entre las horas operando.", " t/h"),
        ("abc", "{F} ¿Qué criterio obligatorio incumplió el turno A respecto de las alarmas?", "No registró ni informó las dos alarmas de sobrecarga", "Procesó demasiadas toneladas", "Operó demasiadas horas", "El criterio 2 exige registrar e informar todas las alarmas."),
        ("abc", "{F} ¿Qué otro criterio obligatorio incumplió el turno A?", "No informó el derrame de mineral", "No alcanzó el 90 % bajo 200 mm", "No cumplió la meta de producción", "El criterio 3 exige informar todo derrame."),
        ("abc", "{F} ¿Cumplió el turno A el criterio de calidad del producto?", "Sí, porque 90 % es igual al mínimo exigido", "No, porque debía pasar más del 90 %", "No, porque produjo demasiado", "El criterio dice al menos 90 %, e incluye el 90."),
        ("=", "{F} ¿Cuántas toneladas más produjo el turno A que el B?", "7200-6000", "Se resta la producción de B a la de A.", " t"),
        ("abc", "{F} ¿Cuál turno cumple los estándares y por qué?", "El turno B, porque cumple los tres criterios obligatorios y la meta", "El turno A, porque produjo más", "Ninguno, porque ambos tuvieron paradas", "El turno A incumple dos criterios obligatorios."),
        ("abc", "{F} Un jefe propone que el turno A «corrija» el reporte anotando las alarmas como no ocurridas. ¿Qué corresponde?", "Rechazarlo: las alarmas se registran con su hora y se informa la no conformidad", "Aceptarlo si el turno produjo más", "Aceptarlo si el supervisor no lo nota", "Alterar un registro oculta un problema real."),
        ("=", "{F} ¿Cuántos puntos porcentuales más de producto bajo 200 mm tiene el turno B que el turno A?", "96-90", "Se resta el porcentaje del turno A al del turno B.", " puntos"),
        ("abc", "Una persona te cuenta que, en una planta de ejemplo, hubo una explosión de polvo cerca de una correa y que hay personas heridas. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar a ayudar a los heridos", "Esperar a que termine el turno para informar", "Entrar a una zona con riesgo de nueva explosión pone en peligro a otras personas."),
    ],
    ctx=("abc", "Un reporte de turno de ejemplo anota 6.300 toneladas, 9 horas operando y «rendimiento 900 t/h». ¿Qué respondes?", "Que los números no cuadran, porque 6.300 ÷ 9 son 700 t/h, y que el reporte se devuelve para corregirlo", "Que está correcto, porque lo anotó el supervisor", "Que se corrige a 900 t/h solo en el informe final", "Verificar un reporte es comprobar que los números cuadren antes de usarlo."),
    sc=[
        ("En Explotación Minera: ¿qué se revisa primero al comparar dos turnos?", "Los criterios obligatorios", "Un incumplimiento obligatorio descalifica al turno."),
        ("En Explotación Minera: ¿qué se hace con una alarma no registrada?", "Se informa como no conformidad y se corrige", "Ocultarla impide aprender del problema y corregir su causa."),
        ("En Explotación Minera: ¿cómo se calcula el rendimiento de un turno?", "Toneladas divididas entre horas operando", "Se mide mientras el chancado funciona."),
    ],
    op=("Dos turnos ficticios de la «Planta Demo Cerro Claro». Turno X: 5.600 toneladas en 8 horas operando; 88 % del producto bajo 200 mm; todas las alarmas registradas; sin derrames. Turno Y: 4.500 toneladas en 6 horas operando; 93 % bajo 200 mm; todas las alarmas registradas; sin derrames. Criterio obligatorio: al menos 90 % bajo 200 mm. Meta: al menos 700 t/h. Escribe (a) el rendimiento de cada turno, (b) cuál cumple el criterio de calidad, (c) cuál cumple la meta de producción, (d) cuál elegirías como el que cumple los estándares y por qué.",
        "(a) X: 5.600 ÷ 8 = 700 t/h; Y: 4.500 ÷ 6 = 750 t/h. (b) El turno Y, porque 93 % es al menos 90 %. (c) Ambos, porque 700 y 750 son al menos 700. (d) El turno Y, porque cumple el criterio obligatorio de calidad y también la meta; el X incumple la calidad.",
        ["calcula los rendimientos", "aplica el criterio de calidad", "compara con la meta", "decide con los criterios obligatorios primero"],
        ["hoja con las cuatro respuestas"],
        ["elegir por producción", "rechazar el 700 exacto", "no revisar el criterio de calidad"],
        "Pregunta: «¿qué criterio revisaste antes de mirar la producción?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa dos turnos con tres criterios y una meta, y decide cuál cumple los estándares.",
    extend="Explica con un ejemplo por qué informar un derrame pequeño ayuda a prevenir accidentes y a cuidar el ambiente.",
)
