"""Agropecuaria TP 4.º medio, mención Vitivinícola: OAM-01 (cultivo de vides), OAM-02 (vendimia y recepción de la uva) y OAM-03 (descubes, trasiegos y tratamientos enológicos, solo conceptos, calidad y registros). Todo en papel, con datos de ejemplo; sin procedimientos de elaboración."""
from __future__ import annotations

from tp_agvi_common import AVISO, EMER, build

O1 = "TP-AGVI-4-OAM-01"
O2 = "TP-AGVI-4-OAM-02"
O3 = "TP-AGVI-4-OAM-03"

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Viña Demo» es un predio ficticio de 8 hectáreas de vid para elaborar vino, con hileras sostenidas por postes y alambres tensados. Se hace poda, riego, control de malezas y de hongos y manejo del follaje (las hojas y los brotes). "
     "Peligros anotados: tijeras de podar muy afiladas, alambres tensados a la altura de la cara, trabajo repetitivo con los brazos sobre la cabeza, tractor y pulverizadora, sol y calor fuertes, zanjas de riego y tormentas.")
build(
    O1, 1, F,
    use="Aprenderé qué es el manejo cultural de la vid, qué se vigila en un viñedo y cuáles son los peligros y las normas del trabajo de campo.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "La vid es la planta que produce la uva. Un viñedo es el terreno plantado con vides, y se divide en cuarteles, que son sectores con la misma variedad y manejo. El manejo cultural son las labores de cuidado del cultivo: la poda, el riego, el control de malezas, el control de hongos y plagas y el manejo del follaje. Vigilar el viñedo es revisarlo con regularidad y anotar lo que se observa en un registro.",
        "El trabajo de campo en un viñedo tiene peligros. Las tijeras cortan; los alambres tensados pueden golpear la cara y los ojos si se rompen o se sueltan; el trabajo repetitivo daña la espalda y los hombros; el tractor y la pulverizadora pueden atrapar o intoxicar; y el sol fuerte provoca golpe de calor. La jerarquía de controles ordena las medidas: eliminar, sustituir, cambiar el lugar o el equipo, reglas y capacitación y, al final, el equipo de protección personal (EPP).",
        f"Una cubierta en los extremos de los alambres es un control de ingeniería; una regla de pausas con agua es administrativa. Las labores con maquinaria y productos las hace personal capacitado y autorizado, bajo la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("vid", "planta que produce la uva"), ("viñedo", "terreno plantado con vides"), ("cuartel", "sector del viñedo con la misma variedad y manejo"), ("manejo cultural", "labores de cuidado del cultivo, como poda, riego y control de hongos"), ("follaje", "hojas y brotes de la vid"), ("registro de campo", "documento donde se anotan las observaciones y labores"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Distinguir cuartel y viñedo", "Un viñedo de ejemplo tiene 10 hectáreas divididas en 2 sectores con variedades distintas. ¿Cómo se llaman los sectores?", ["Cada sector tiene su variedad y manejo.", "Se llaman cuarteles."], "Cuarteles"),
        ("Clasificar un control", "Un viñedo de ejemplo coloca tapas plásticas en los extremos de los alambres de las hileras. ¿Qué tipo de control es?", ["Cambia físicamente el lugar.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que un alambre tensado no es peligroso si está firme.", "Puede soltarse o romperse y golpear la cara.", "Se vigila su estado y se usa protección, según el plan de prevención."),
              ("Creer que leer sobre la poda habilita para usar tijeras de podar.", "Las herramientas cortantes exigen formación y autorización.", "Aprende aquí el concepto y deja el corte a personal capacitado.")],
    T=[
        ("abc", "En el viñedo: ¿qué es un cuartel?", "Un sector del viñedo con la misma variedad y manejo", "Una bodega para guardar el vino", "Una máquina para cortar racimos", "El cuartel es un sector del viñedo; la bodega y la máquina son otras cosas."),
        ("abc", "En el viñedo: ¿qué es el manejo cultural?", "Las labores de cuidado del cultivo, como poda, riego y control de hongos", "El proceso de fermentación en bodega", "La venta de la uva", "El manejo cultural cuida el cultivo; la fermentación ocurre después de la cosecha."),
        ("abc", "En el viñedo: ¿qué es el follaje de la vid?", "Las hojas y los brotes", "Los racimos de uva", "Las raíces", "El follaje son las hojas y brotes; los racimos son el fruto."),
        ("=", "{F} Si cada hectárea tiene 5 hileras de ejemplo, ¿cuántas hileras tiene el viñedo completo?", "8*5", "Se multiplican las hectáreas por las hileras de cada una.", " hileras"),
        ("abc", "{F} Cubrir con tapas plásticas los extremos de los alambres tensados es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla", "De EPP, porque protege a quien trabaja", "Las tapas son una parte física del viñedo y funcionan siempre."),
        ("abc", "{F} Una regla que dice «pausas de 10 minutos con agua a la sombra cada hora» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el viñedo", "De sustitución, porque cambia la labor", "Una regla de pausas es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a los alambres tensados a la altura de la cara?", "Que se suelten o se rompan y golpeen la cara o los ojos", "Los alambres mismos en el viñedo", "Que las hileras estén rectas", "El riesgo es la posibilidad de daño; los alambres tensados son el peligro."),
        ("abc", "{F} Una estudiante dice: «ya aprendí cómo se poda, así que tomo las tijeras y poda una hilera». ¿Qué respuesta es correcta?", "Es peligroso: las herramientas cortantes las usa personal capacitado y autorizado", "Es correcto, si usa guantes", "Es correcto, si poda poco", "Los guantes o la poca cantidad no reemplazan la formación."),
        ("abc", "{F} Durante una visita, una persona se desmaya por el calor entre las hileras. ¿Qué corresponde según las reglas generales?", "No quedarte sola, avisar a un adulto responsable y a emergencias", "Moverla sin saber qué le ocurre", "Esperar a que se despierte sola", "Se avisa a quienes pueden prestar ayuda sin riesgo."),
        ("abc", "En el viñedo: ¿por qué el trabajo con los brazos sobre la cabeza necesita pausas?", "Porque puede dañar la espalda y los hombros con el tiempo", "Porque la uva madura más lento", "Porque las hojas se caen", "El trabajo repetitivo daña músculos y articulaciones."),
        ("abc", "{F} Se propone solo entregar gafas para el peligro de los alambres. ¿Qué medida es más efectiva en la jerarquía?", "Proteger los extremos de los alambres con tapas y mantenerlos en buen estado", "Entregar gafas más gruesas", "Pedir que se trabaje con cuidado", "Cambiar el lugar actúa sobre el peligro."),
        ("=", "{F} Un equipo capacitado de ejemplo poda 2 hectáreas por semana. ¿Cuántas semanas necesita para todo el viñedo?", "8//2", "Se dividen las hectáreas totales entre las de cada semana.", " semanas"),
        ("abc", "En el viñedo: ¿por qué conviene anotar lo observado en un registro de campo?", "Porque permite comparar cuarteles y fechas y tomar decisiones con datos", "Porque reemplaza al jefe de viña", "Porque evita revisar el viñedo", "El registro guarda evidencia para decidir."),
    ],
    ctx=("abc", "Un vecino te ofrece pagarte por podar sus vides con sus tijeras «porque ya sabes cómo se hace». ¿Qué respondes?", "Que no, porque exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, si son pocas", "Que sí, con guantes", "Haber visto el concepto no habilita para usar herramientas cortantes."),
    sc=[
        ("En el viñedo: ¿qué es un viñedo?", "Un terreno plantado con vides", "El viñedo es el terreno donde crecen las vides."),
        ("En el viñedo: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En el viñedo: ¿qué es el manejo cultural?", "Las labores de cuidado del cultivo", "Incluye poda, riego y control de hongos."),
    ],
    op=("La «Viña Demo 2» anota una tarea de ejemplo: aplicar un producto contra hongos con una pulverizadora al mediodía de un día de calor fuerte, sin sombra ni agua, y sin autorización escrita. Escribe (a) el peligro del calor y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a alguien mareado.",
        "(a) Peligro: calor intenso sin sombra; riesgo: que una persona sufra un golpe de calor. (b) Una regla de trabajar en las horas más frescas, con pausas y agua. (c) Una cabina o una sombra fija en el equipo, instalada por personal autorizado. (d) Aviso a un adulto responsable y a emergencias, sin moverla.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "avisa a un adulto responsable"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al calor", "proponer solo EPP", "no avisar"],
        "Pregunta: «¿qué control cambia las condiciones y no depende de que alguien se acuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres labores del manejo cultural de la vid y un peligro de cada una.",
    extend="Explica con un ejemplo por qué un alambre tensado es un peligro aunque esté firme.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (datos de ejemplo, inventados). Ciclo anual de la vid en la «Viña Demo» con meses de ejemplo: reposo invernal (junio y julio), brotación (septiembre), floración (noviembre), cuajado (diciembre), envero (febrero, cambio de color de las bayas) y madurez y cosecha (marzo y abril). "
     "Marco de plantación del Cuartel 1: 200 cm entre hileras y 125 cm entre plantas; una hectárea tiene 100.000.000 cm². Documentos: el cuaderno de campo del cuartel, el calendario de labores y el registro de monitoreo. Roles: jefe de viña, capataz, operarios y enólogo asesor.")
build(
    O1, 2, F,
    use="Aprenderé las etapas del ciclo de la vid, el marco de plantación y la densidad, y los documentos y roles del cuidado de un viñedo.",
    prior=["Sé qué son el viñedo y el manejo cultural.", "Sé multiplicar y dividir enteros.", "Sé leer una ficha de datos."],
    explain=[
        "La vid cumple cada año un ciclo con etapas. En el reposo invernal la planta no tiene hojas; en la brotación abren las yemas; en la floración salen las flores; en el cuajado las flores se transforman en bayas pequeñas; en el envero las bayas cambian de color; y en la madurez la uva llega al punto de cosecha. Cada etapa pide cuidados distintos, por eso el manejo se programa según el ciclo.",
        "El marco de plantación es la distancia entre hileras y entre plantas. La densidad es el número de plantas por hectárea: se divide una hectárea (100.000.000 cm²) por el área de cada planta, que es la distancia entre hileras por la distancia entre plantas. Los documentos son el cuaderno de campo, que anota lo observado y las labores; el calendario de labores, que programa lo que se hará cada mes; y el registro de monitoreo, que guarda los controles de madurez y sanidad. El jefe de viña organiza, el capataz supervisa, los operarios capacitados ejecutan y el enólogo asesora.",
        f"Un registro no se altera para que una observación «se vea mejor». {EMER} {AVISO}",
    ],
    vocab=[("reposo invernal", "etapa en que la vid no tiene hojas y no crece"), ("brotación", "etapa en que abren las yemas"), ("floración", "etapa en que salen las flores"), ("cuajado", "etapa en que las flores se transforman en bayas pequeñas"), ("envero", "etapa en que las bayas cambian de color"), ("densidad de plantación", "número de plantas por hectárea"), ("calendario de labores", "documento que programa lo que se hará cada mes")],
    worked=[
        ("Etapa del ciclo", "Las bayas de una vid de ejemplo están cambiando de verde a rojo. ¿Qué etapa es?", ["El cambio de color de las bayas tiene nombre propio.", "Es el envero."], "Envero"),
        ("Densidad", "Un marco de ejemplo es de 250 cm por 200 cm. ¿Cuántas plantas por hectárea?", ["Cada planta ocupa 250 por 200, o sea 50.000 cm².", "100.000.000 entre 50.000 es 2.000."], "2.000 plantas por hectárea"),
    ],
    mistakes=[("Creer que mientras más plantas por hectárea, siempre mejor.", "Las plantas compiten por luz, agua y nutrientes.", "La densidad se fija según la variedad y el asesor."),
              ("Confundir el calendario de labores con el cuaderno de campo.", "El calendario programa y el cuaderno anota lo realizado.", "Consulta cada documento para lo que fue hecho.")],
    T=[
        ("abc", "En el viñedo: ¿qué es la brotación?", "La etapa en que abren las yemas", "La etapa en que cambian de color las bayas", "La etapa en que se cosecha", "La brotación es la apertura de las yemas."),
        ("abc", "En el viñedo: ¿qué es el envero?", "La etapa en que las bayas cambian de color", "La etapa en que salen las flores", "La etapa de reposo invernal", "El envero es el cambio de color de las bayas."),
        ("abc", "En el viñedo: ¿qué es la densidad de plantación?", "El número de plantas por hectárea", "El peso de la uva por planta", "La distancia entre dos hectáreas", "La densidad cuenta plantas por hectárea."),
        ("=", "{F} ¿Cuántas plantas por hectárea hay en el Cuartel 1?", "100000000//(200*125)", "Se divide el área de una hectárea entre el área de cada planta.", " plantas"),
        ("abc", "{F} ¿Qué etapa corresponde a febrero según la ficha?", "El envero", "La brotación", "El reposo invernal", "La ficha asigna el envero a febrero."),
        ("abc", "{F} ¿Qué etapa viene después de la floración?", "El cuajado", "La brotación", "El reposo invernal", "Las flores se transforman en bayas en el cuajado."),
        ("abc", "{F} ¿Qué documento programa lo que se hará cada mes?", "El calendario de labores", "El cuaderno de campo", "El registro de monitoreo", "El calendario programa; el cuaderno anota lo realizado."),
        ("abc", "{F} ¿Qué rol asesora sobre la madurez de la uva?", "El enólogo asesor", "El operario", "El comprador", "El enólogo asesora sobre la calidad de la uva."),
        ("=", "{F} Si el Cuartel 1 mide 3 hectáreas, ¿cuántas plantas tiene en total?", "3*(100000000//(200*125))", "Se multiplican las hectáreas por las plantas de cada hectárea.", " plantas"),
        ("abc", "{F} Una compañera dice: «la cosecha ocurre en la brotación». ¿Qué respuesta es correcta?", "Es incorrecto: la cosecha ocurre en la madurez, en marzo y abril", "Es correcto, porque ahí aparece la uva", "Es correcto, si hay sol", "La ficha ubica la cosecha en la madurez."),
        ("abc", "{F} El capataz quiere anotar en el cuaderno que se podó un cuartel que aún no se poda, «para adelantar». ¿Qué corresponde?", "Rechazarlo: el cuaderno anota solo lo realizado", "Aceptarlo, si se poda mañana", "Aceptarlo, para cumplir el calendario", "Anotar lo que no se hizo falsea el registro."),
        ("abc", "{F} Una persona se lastima con una herramienta cortante y no puede hablar. ¿Qué corresponde a quien lo ve?", "No tocar la herramienta ni la herida, avisar a un adulto responsable y a emergencias", "Quitar la herramienta con las manos", "Esperar a que mejore", "Se avisa a quienes pueden prestar ayuda."),
        ("abc", "En el viñedo: ¿por qué el cuidado cambia según la etapa del ciclo?", "Porque cada etapa tiene necesidades distintas", "Porque el calendario no existe", "Porque la vid siempre necesita lo mismo", "Cada etapa pide un manejo propio."),
    ],
    ctx=("abc", "Un conocido te pide que le «ajustes» el calendario de labores de su viñedo sin ver sus cuarteles. ¿Qué respondes?", "Que el calendario lo define un asesor con los cuarteles a la vista", "Que haga todas las labores en octubre", "Que no haga ninguna", "El calendario depende de la variedad, el clima y la etapa."),
    sc=[
        ("En el viñedo: ¿cómo se calcula la densidad de plantación?", "Una hectárea dividida por el área de cada planta", "La densidad es plantas por hectárea."),
        ("En el viñedo: ¿qué documento anota las labores realizadas?", "El cuaderno de campo", "El cuaderno de campo guarda lo que ya se realizó en el cuartel."),
        ("En el viñedo: ¿qué etapa sigue al envero?", "La madurez", "Tras el cambio de color, la uva llega a la madurez."),
    ],
    op=("Ficha de ejemplo de la «Viña Demo 3»: marco de plantación de 250 cm entre hileras y 100 cm entre plantas; el cuartel mide 2 hectáreas; una hectárea tiene 100.000.000 cm². Escribe (a) el área de cada planta, (b) las plantas por hectárea, (c) las plantas del cuartel, (d) en qué documento anotas lo observado en el cuartel.",
        "(a) 250 × 100 = 25.000 cm². (b) 100.000.000 ÷ 25.000 = 4.000 plantas. (c) 2 × 4.000 = 8.000 plantas. (d) En el cuaderno de campo.",
        ["calcula el área por planta", "calcula la densidad", "calcula las plantas del cuartel", "nombra el documento"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar las distancias", "confundir plan con registro"],
        "Pregunta: «¿cuántos cm² ocupa cada planta?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Calcula las plantas por hectárea de un marco inventado de 200 cm por 100 cm.",
    extend="Explica con un ejemplo por qué una densidad muy alta puede perjudicar la calidad de la uva.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (monitoreo de madurez de ejemplo, inventado). Cuartel 2 de la «Viña Demo». Contenido de azúcar de la uva en grados Brix (°Brix), medido cada semana: semana 1, 18; semana 2, 20; semana 3, 22; semana 4, 23. Objetivo de ejemplo del enólogo: 24 °Brix. "
     "Pronóstico: lluvias fuertes en 5 días (la lluvia puede favorecer hongos en los racimos). Aumento semanal: 2 °Brix en las primeras semanas y 1 en la última.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un monitoreo de madurez en papel, a calcular el avance semanal y a relacionarlo con el clima y con la decisión que corresponde al enólogo.",
    prior=["Sé qué es la madurez de la uva.", "Sé calcular diferencias y promedios de enteros.", "Sé leer una tabla de datos."],
    explain=[
        "Los grados Brix miden el contenido de azúcar del jugo de la uva. Mientras la uva madura, los °Brix suben. El monitoreo de madurez consiste en medir los °Brix cada cierto tiempo para ver cómo avanzan. El avance semanal es la diferencia entre dos mediciones consecutivas. Cuando el avance se frena, la uva se acerca a su máximo de azúcar. El enólogo decide el momento de la cosecha mirando varios datos, no solo el azúcar.",
        "Para analizar el caso se calculan los avances, se compara el último valor con el objetivo y se considera el clima. Una lluvia fuerte antes de la cosecha puede diluir el jugo y favorecer hongos, y por eso el enólogo y el jefe de viña la consideran. Quien analiza el caso en papel prepara la información; la decisión final y las medidas las toman el enólogo y el jefe de viña.",
        f"Las mediciones en terreno las hace personal capacitado; este cuaderno no habilita para tomar muestras ni para cosechar. {EMER} {AVISO}",
    ],
    vocab=[("grados Brix", "medida del contenido de azúcar del jugo de la uva"), ("monitoreo de madurez", "medición periódica de los °Brix para ver cómo madura la uva"), ("avance semanal", "diferencia entre dos mediciones consecutivas"), ("objetivo de madurez", "valor de °Brix que fija el enólogo para cosechar"), ("hongo", "microorganismo que daña los racimos con humedad")],
    worked=[
        ("Avance semanal", "En un cuartel de ejemplo los °Brix pasan de 19 a 21 en una semana. ¿Cuál es el avance?", ["Se resta la primera medición a la segunda.", "21 menos 19."], "2 °Brix"),
        ("Comparar con el objetivo", "El objetivo de ejemplo es 24 y la última medición es 22. ¿Cuántos °Brix faltan?", ["Se resta la medición al objetivo.", "24 menos 22."], "2 °Brix"),
    ],
    mistakes=[("Decidir la cosecha mirando solo el azúcar.", "El enólogo considera también la acidez, el estado sanitario y el clima.", "La decisión la toma el enólogo con varios datos."),
              ("Creer que si el avance se frena, la uva ya está madura para cualquier destino.", "Puede faltar para el objetivo del vino que se busca.", "Se compara con el objetivo del enólogo.")],
    T=[
        ("abc", "En el viñedo: ¿qué miden los grados Brix?", "El contenido de azúcar del jugo de la uva", "La cantidad de agua de la lluvia", "El peso del racimo", "Los °Brix miden el azúcar del jugo."),
        ("abc", "En el viñedo: ¿qué es el avance semanal de madurez?", "La diferencia entre dos mediciones consecutivas", "El total de °Brix", "El objetivo del enólogo", "El avance resta una medición a la siguiente."),
        ("abc", "En el viñedo: ¿qué riesgo trae una lluvia fuerte antes de la cosecha?", "Puede diluir el jugo y favorecer hongos", "Hace subir los °Brix de inmediato", "Elimina la necesidad de registrar", "La lluvia puede afectar la calidad de la uva."),
        ("=", "{F} ¿Cuántos °Brix subió la uva entre la semana 1 y la semana 4?", "23-18", "Se resta la primera medición a la última.", " °Brix"),
        ("=", "{F} ¿Cuántos °Brix faltan para el objetivo de 24, tras la semana 4?", "24-23", "Se resta la última medición al objetivo.", " °Brix"),
        ("=", "{F} ¿Cuál fue el avance entre la semana 3 y la semana 4?", "23-22", "Se resta la semana 3 a la semana 4.", " °Brix"),
        ("abc", "{F} ¿Qué se observa en el avance semanal?", "Se frena: de 2 °Brix pasa a 1", "Sube cada vez más rápido", "Se mantiene igual", "Los avances son 2, 2 y 1."),
        ("abc", "{F} ¿Qué dato de la ficha preocupa respecto de los hongos?", "El pronóstico de lluvias fuertes en 5 días", "El objetivo de 24 °Brix", "El avance de la semana 2", "La lluvia puede favorecer hongos en los racimos."),
        ("abc", "{F} ¿Quién decide el momento de la cosecha?", "El enólogo, con el jefe de viña", "Una estudiante con la ficha", "El comprador del vino", "La decisión final es del enólogo."),
        ("abc", "{F} Una compañera dice: «ya van 23 °Brix, así que cosechamos mañana yo y mi grupo». ¿Qué respuesta es correcta?", "Es incorrecto: la decisión es del enólogo y la cosecha la hace personal capacitado", "Es correcto, porque 23 es casi 24", "Es correcto, si hay sol", "Este cuaderno no habilita para decidir ni para cosechar."),
        ("abc", "{F} El jefe de viña quiere anotar 24 °Brix en el registro, aunque midió 23, «para que se pueda cosechar». ¿Qué corresponde?", "Rechazarlo: se anota la medición real e informa", "Aceptarlo, para ganar tiempo", "Aceptarlo, si lo firma el capataz", "Alterar el dato falsea el registro y pone en riesgo la calidad."),
        ("=", "{F} Si siguiera avanzando 1 °Brix por semana, ¿cuántas semanas más tardaría en llegar al objetivo?", "(24-23)//1", "Se dividen los °Brix que faltan entre el avance semanal de 1.", " semana"),
        ("abc", "En el viñedo: ¿por qué conviene medir en varias semanas y no una sola vez?", "Porque muestra el avance y la tendencia", "Porque cada medición cambia el objetivo", "Porque la uva no madura sola", "Varias mediciones muestran la evolución de la madurez de la uva."),
    ],
    ctx=("abc", "Un conocido te pregunta si ya puede cosechar y te da una sola medición de °Brix. ¿Qué respondes?", "Que necesita más datos y que lo decide su enólogo", "Que coseche de inmediato", "Que espere un mes", "Una sola medición no basta para decidir."),
    sc=[
        ("En el viñedo: ¿qué miden los °Brix?", "El azúcar del jugo de la uva", "Los °Brix miden el azúcar que contiene el jugo de la uva."),
        ("En el viñedo: ¿quién decide el momento de la cosecha?", "El enólogo", "La decisión usa varios datos de calidad."),
        ("En el viñedo: ¿qué se calcula entre dos mediciones?", "El avance", "El avance es la diferencia entre mediciones."),
    ],
    op=("Monitoreo de ejemplo del «Viña Demo 4»: °Brix de 4 semanas: 17, 19, 21, 22; objetivo del enólogo de 24; pronóstico de lluvias fuertes en 3 días. Escribe (a) el avance entre la semana 3 y la 4, (b) cuántos °Brix faltan para el objetivo, (c) el riesgo del pronóstico, (d) quién decide la cosecha.",
        "(a) 22 − 21 = 1 °Brix. (b) 24 − 22 = 2 °Brix. (c) La lluvia puede diluir el jugo y favorecer hongos. (d) El enólogo, con el jefe de viña.",
        ["calcula el avance", "calcula lo que falta", "explica el riesgo", "nombra quién decide"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "decidir la cosecha por cuenta propia"],
        "Pregunta: «¿qué dos mediciones restas para el avance?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula los avances semanales de este monitoreo inventado: 16, 18, 21, 22.",
    extend="Explica con un ejemplo por qué la acidez y el estado sanitario también importan para elegir la cosecha.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Cuartel de 3 hectáreas de la «Viña Demo» con 4.000 plantas por hectárea. Producción de la temporada: 36.000 kg de uva. Límite de rendimiento de ejemplo fijado por el enólogo: 14.000 kg por hectárea. "
     "Precio de ejemplo de la uva: $400 por kilo. Costo anual del manejo cultural de ejemplo: $2.100.000 por hectárea.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular rendimiento, kilos por planta, ingreso y margen de un cuartel, y compararlos con un límite de calidad.",
    prior=["Sé qué es la densidad y el rendimiento.", "Sé multiplicar y dividir enteros.", "Sé restar enteros."],
    explain=[
        "El rendimiento es los kilos de uva por hectárea: se divide la producción total entre las hectáreas. Los kilos por planta se obtienen dividiendo el rendimiento entre las plantas por hectárea. Un rendimiento muy alto puede bajar la calidad de la uva, por eso el enólogo fija un límite. El ingreso es los kilos por el precio, y el margen es el ingreso menos el costo del manejo.",
        "Con estos números se compara un cuartel contra el límite y contra otros cuarteles. Un margen alto no justifica superar el límite de calidad ni descuidar el manejo. Los valores de esta clase son de ejemplo, y las decisiones las toman el enólogo y el jefe de viña con los datos reales del predio.",
        f"Calcular no reemplaza la seguridad en el trabajo de campo. {EMER} {AVISO}",
    ],
    vocab=[("rendimiento", "kilos de uva por hectárea"), ("kilos por planta", "rendimiento dividido por las plantas por hectárea"), ("límite de rendimiento", "máximo de kilos por hectárea fijado por el enólogo para cuidar la calidad"), ("ingreso", "kilos por el precio de cada kilo"), ("margen", "ingreso menos costo")],
    worked=[
        ("Rendimiento", "Un cuartel de ejemplo de 2 hectáreas produjo 24.000 kg. ¿Cuál es el rendimiento?", ["Se divide la producción entre las hectáreas.", "24.000 entre 2."], "12.000 kg por hectárea"),
        ("Kilos por planta", "Con 3.000 plantas por hectárea en ese cuartel de ejemplo, ¿cuántos kilos da cada planta?", ["Se divide el rendimiento entre las plantas por hectárea.", "12.000 entre 3.000."], "4 kg por planta"),
    ],
    mistakes=[("Aumentar el rendimiento sin mirar la calidad.", "Un rendimiento muy alto puede bajar la calidad de la uva.", "Se respeta el límite que fija el enólogo."),
              ("Calcular el ingreso por hectárea y compararlo con el costo total.", "Se mezclan magnitudes distintas.", "Se compara el ingreso del cuartel con el costo del cuartel.")],
    T=[
        ("abc", "En el viñedo: ¿qué es el rendimiento de un cuartel?", "Los kilos de uva por hectárea", "El número de plantas por hectárea", "El precio por kilo", "El rendimiento relaciona producción y superficie."),
        ("abc", "En el viñedo: ¿qué es el límite de rendimiento?", "El máximo de kilos por hectárea fijado para cuidar la calidad", "El mínimo de uva que se cosecha", "El precio máximo de la uva", "El límite protege la calidad de la uva."),
        ("abc", "En el viñedo: ¿qué es el margen de un cuartel?", "El ingreso menos el costo", "El costo más el ingreso", "El número de hileras", "El margen resta el costo del ingreso."),
        ("=", "{F} ¿Cuál es el rendimiento del cuartel, en kilos por hectárea?", "36000//3", "Se divide la producción total entre las hectáreas.", " kg por hectárea"),
        ("=", "{F} ¿Cuántos kilos da cada planta, en promedio?", "(36000//3)//4000", "Se divide el rendimiento entre las plantas por hectárea.", " kg por planta"),
        ("abc", "{F} ¿Cumple el cuartel el límite de rendimiento de ejemplo?", "Sí, porque 12.000 es menor que 14.000", "No, porque 12.000 es mayor que 14.000", "No se puede saber", "12.000 kg por hectárea está bajo el límite de 14.000."),
        ("=", "{F} ¿Cuál es el ingreso del cuartel?", "36000*400", "Se multiplican los kilos por el precio de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuál es el costo anual del manejo del cuartel?", "3*2100000", "Se multiplican las hectáreas por el costo de cada una.", " pesos"),
        ("=", "{F} ¿Cuál es el margen del cuartel?", "36000*400-3*2100000", "Se resta el costo al ingreso.", " pesos"),
        ("abc", "{F} Un jefe propone aumentar la producción a 16.000 kg por hectárea para ganar más. ¿Qué corresponde?", "Rechazarlo: supera el límite del enólogo y baja la calidad", "Aceptarlo, porque más kilos dan más dinero", "Aceptarlo, si el precio sube", "El límite protege la calidad de la uva."),
        ("abc", "{F} Una estudiante quiere calcular en terreno cuántas plantas hay contándolas entre las hileras con las tijeras en la mano. ¿Qué corresponde?", "Rechazarla: el trabajo en terreno lo hace personal capacitado", "Aceptarla, si lleva guantes", "Aceptarla, si va con una compañera", "Las herramientas cortantes exigen formación, autorización y norma vigente."),
        ("=", "{F} Si el precio bajara a $350 por kilo, ¿cuál sería el margen?", "36000*350-3*2100000", "Se calcula el ingreso con el nuevo precio y se resta el costo.", " pesos"),
        ("abc", "En el viñedo: ¿por qué conviene probar el cálculo con otro precio?", "Porque el precio es un supuesto que puede cambiar el margen", "Porque el costo siempre es cero", "Porque el rendimiento no importa", "Un cambio de precio puede cambiar el margen."),
    ],
    ctx=("abc", "Un conocido te pregunta si le conviene producir más kilos por hectárea y te da solo el precio. ¿Qué respondes?", "Que también hay que mirar la calidad, el límite y el costo, y que lo decide su enólogo", "Que sí, siempre", "Que no, nunca", "El rendimiento por hectárea afecta la calidad final de la uva."),
    sc=[
        ("En el viñedo: ¿cómo se calcula el rendimiento?", "Producción entre hectáreas", "El rendimiento se obtiene con una división entre producción y hectáreas."),
        ("En el viñedo: ¿cómo se calcula el margen?", "Ingreso menos costo", "El margen es lo que queda tras pagar costos."),
        ("En el viñedo: ¿quién fija el límite de rendimiento?", "El enólogo", "El enólogo cuida la calidad de la uva."),
    ],
    op=("Datos de ejemplo de la «Viña Demo 5»: 2 hectáreas con 2.500 plantas por hectárea; producción de 30.000 kg; límite de 16.000 kg por hectárea; precio $300 por kilo; costo de $1.800.000 por hectárea. Escribe (a) el rendimiento y si cumple el límite, (b) los kilos por planta, (c) el ingreso y el costo, (d) el margen.",
        "(a) 30.000 ÷ 2 = 15.000 kg por hectárea; cumple, porque es menor que 16.000. (b) 15.000 ÷ 2.500 = 6 kg por planta. (c) Ingreso: 30.000 × 300 = $9.000.000; costo: 2 × 1.800.000 = $3.600.000. (d) 9.000.000 − 3.600.000 = $5.400.000.",
        ["calcula el rendimiento y concluye", "estima los kilos por planta", "calcula ingreso y costo", "calcula el margen"],
        ["hoja con las cuatro respuestas"],
        ["no dividir entre las hectáreas", "no restar el costo"],
        "Pregunta: «¿entre cuántas hectáreas divides la producción?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el rendimiento de un cuartel inventado de 4 hectáreas que produjo 52.000 kg.",
    extend="Explica con un ejemplo por qué producir más kilos puede bajar el valor de la uva.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). En la vendimia (la cosecha de la uva) de la «Viña Demo» se cosecha a mano en cajas de 15 kg (dato de ejemplo), se vacían en bins (contenedores grandes) y un camión los lleva a la bodega, donde la uva se pesa y llega a una tolva con tornillo sin fin. "
     "Peligros anotados: tijeras afiladas, cajas y bins pesados, tractor y camión en el camino, calor, una tolva con tornillo sin fin que puede atrapar, piso resbaladizo y gas dióxido de carbono en la bodega.")
build(
    O2, 1, F,
    use="Aprenderé qué son la vendimia, el transporte y el acondicionamiento de la uva, qué son las buenas prácticas de manufactura y cuáles son los peligros de la vendimia y la recepción.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "La vendimia es la cosecha de la uva para vinificar, es decir, para elaborar vino. Después de cosechar, la uva se transporta a la bodega y se acondiciona: se recibe, se pesa, se revisa su calidad y se prepara para la molienda. La molienda es romper las bayas para liberar el mosto, que es el jugo de la uva. Todo el proceso debe cumplir las buenas prácticas de manufactura (BPM): higiene, limpieza, orden y registros que cuidan la calidad y la inocuidad del producto.",
        "La vendimia tiene peligros: las tijeras cortan; las cajas y los bins pesados pueden aplastar; el tractor y el camión pueden atropellar; el calor fuerte provoca golpe de calor; la tolva con tornillo sin fin atrapa manos y ropa; y el dióxido de carbono, un gas sin olor que se acumula en lugares bajos o cerrados de la bodega, puede quitar el aire. La jerarquía de controles ordena las medidas: eliminar, sustituir, cambiar el lugar o el equipo, reglas y, al final, el EPP.",
        f"Una protección fija sobre el tornillo sin fin es un control de ingeniería; una regla de no meter las manos a la tolva es administrativa. Las labores con maquinaria las hace personal capacitado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("vendimia", "cosecha de la uva para elaborar vino"), ("bin", "contenedor grande para transportar la uva"), ("molienda", "ruptura de las bayas para liberar el mosto"), ("mosto", "jugo de la uva"), ("buenas prácticas de manufactura", "reglas de higiene, orden y registro que cuidan la calidad del producto"), ("tolva", "recipiente en forma de embudo por donde entra la uva a la máquina"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Distinguir mosto y uva", "En una bodega de ejemplo se rompen las bayas y se obtiene el jugo. ¿Cómo se llama ese jugo?", ["El jugo de la uva tiene un nombre propio.", "Se llama mosto."], "Mosto"),
        ("Clasificar un control", "Una bodega de ejemplo instala un piso antideslizante en la zona de recepción de la uva. ¿Qué tipo de control es?", ["El piso cambia físicamente el lugar de trabajo.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que se puede meter la mano a la tolva para destrabar la uva si el motor va lento.", "El tornillo sin fin atrapa en un instante.", "Solo personal autorizado interviene, con el equipo sin energía."),
              ("Creer que el dióxido de carbono se detecta por el olor.", "No tiene olor ni color.", "Se vigila con instrumentos y no se entra a lugares cerrados.")],
    T=[
        ("abc", "En la vendimia: ¿qué es el mosto?", "El jugo de la uva", "El vino ya terminado", "La cáscara de la uva", "El mosto es el jugo de la uva obtenido tras romper las bayas."),
        ("abc", "En la vendimia: ¿qué es la molienda?", "La ruptura de las bayas para liberar el mosto", "La cosecha de la uva", "El envasado del vino", "La molienda libera el jugo de las bayas."),
        ("abc", "En la vendimia: ¿qué son las buenas prácticas de manufactura?", "Reglas de higiene, orden y registro que cuidan la calidad del producto", "El precio de la uva", "Las máquinas de la bodega", "Las BPM cuidan la calidad y la inocuidad."),
        ("=", "{F} Cada caja de ejemplo tiene 15 kg de uva y un bin recibe 40 cajas. ¿Cuántos kilos de uva tiene un bin?", "15*40", "Se multiplican los kilos de cada caja por las cajas del bin.", " kg"),
        ("abc", "{F} Una reja fija sobre el tornillo sin fin de la tolva es un control de tipo:", "De ingeniería, porque cambia físicamente el equipo", "Administrativo, porque es una regla", "De EPP, porque protege a quien se acerca", "La reja es una parte del equipo y funciona siempre."),
        ("abc", "{F} Una regla que dice «nadie mete las manos a la tolva» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia la tolva", "De sustitución, porque cambia la uva", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al tornillo sin fin de la tolva?", "Que atrape la mano o la ropa y cause una lesión grave", "El tornillo mismo", "Que la uva se pese mal", "El riesgo es la posibilidad de daño; el tornillo sin fin es el peligro."),
        ("abc", "{F} Una estudiante dice: «ya aprendí cómo funciona la tolva, así que destrabo la uva con la mano». ¿Qué respuesta es correcta?", "Es peligroso: intervenir la máquina lo hace personal autorizado con el equipo sin energía", "Es correcto, si va lento", "Es correcto, si usa guantes", "El guante o la lentitud no evitan el atrapamiento."),
        ("abc", "{F} En una visita, una persona queda con la mano atrapada en la tolva. ¿Qué corresponde según las reglas generales?", "No acercarte, avisar a un adulto responsable y a emergencias", "Intentar sacarla tirando", "Encender el equipo para liberar", "Acercarse o mover el equipo puede agravar la lesión."),
        ("abc", "En la vendimia: ¿por qué el dióxido de carbono es peligroso en la bodega?", "Porque no tiene olor ni color y puede quitar el aire", "Porque huele muy fuerte", "Porque es muy caliente", "Es un gas imposible de notar con los sentidos."),
        ("abc", "{F} Se propone solo entregar guantes para el peligro de la tolva. ¿Qué medida es más efectiva?", "Cubrir el tornillo sin fin con una protección fija", "Entregar guantes más gruesos", "Pedir mayor cuidado", "Cubrir el peligro actúa más arriba que el EPP."),
        ("=", "{F} El camión lleva 10 bins de ejemplo por viaje. ¿Cuántos bins llegan a la bodega en 4 viajes?", "10*4", "Se multiplican los bins de cada viaje por los viajes.", " bins"),
        ("abc", "En la vendimia: ¿por qué las BPM exigen registros?", "Porque permiten seguir el origen y la historia de cada lote de uva", "Porque aceleran la molienda", "Porque eliminan la limpieza", "Los registros dan trazabilidad a cada lote de uva recibido."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por operar la tolva en su vendimia «porque ya viste cómo funciona». ¿Qué respondes?", "Que no, porque exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, si va lenta", "Que sí, con guantes", "Haber visto el concepto no habilita para operar maquinaria."),
    sc=[
        ("En la vendimia: ¿qué es la vendimia?", "La cosecha de la uva para elaborar vino", "La vendimia es la cosecha para vinificar."),
        ("En la bodega de recepción: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En la vendimia: ¿qué es un bin?", "Un contenedor grande para transportar la uva", "El bin sirve para llevar la uva a la bodega."),
    ],
    op=("La «Viña Demo 2» anota una tarea de ejemplo: vaciar cajas de uva a una tolva con el tornillo sin fin al descubierto, con el piso mojado y una persona cerca sin autorización. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a alguien atrapado.",
        "(a) Peligro: tornillo sin fin al descubierto; riesgo: que atrape la mano o la ropa y cause una lesión grave. (b) Una regla de que solo personal autorizado opera la tolva. (c) Una reja fija sobre el tornillo sin fin y un piso antideslizante. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer liberar a la persona", "proponer solo EPP"],
        "Pregunta: «¿qué control cubre la parte móvil aunque alguien se olvide de la regla?». Si no responde, pídele que relea el tercer párrafo."),
    reinforce="Escribe tres peligros de la recepción de uva en bodega y el riesgo de cada uno.",
    extend="Explica con un ejemplo por qué una tolva con tornillo sin fin sin reja es un peligro.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 2 (registro de recepción de ejemplo, inventado). Lote U-03, Cuartel 2 de la «Viña Demo»: 24.000 kg de uva en 40 bins. Cuatro muestras de grados Brix: 23, 24, 24 y 25. Uva podrida en la muestra: 3 % (límite de rechazo de ejemplo: 5 %). "
     "Tiempo máximo de ejemplo entre cosecha y molienda: 6 horas; la cosecha terminó a las 7 horas y la uva llegó a recepción a las 11 horas. Documentos: la guía de recepción (qué llegó, cuándo y de dónde), la ficha del lote de uva y el registro de limpieza de equipos. Roles: jefe de vendimia, controlador de calidad, operador de recepción y enólogo.")
build(
    O2, 2, F,
    use="Aprenderé los indicadores de calidad de la uva en la recepción, los documentos de la vendimia y los roles de quienes la reciben y controlan.",
    prior=["Sé qué son los grados Brix y la vendimia.", "Sé calcular promedios y porcentajes enteros.", "Sé restar enteros."],
    explain=[
        "En la recepción se controla la calidad de la uva con indicadores: los grados Brix, que miden el azúcar; el porcentaje de uva podrida o dañada, que indica el estado sanitario; y el tiempo desde la cosecha, porque una uva que espera mucho se deteriora. Cada indicador tiene un límite: mínimo de grados Brix, máximo de uva podrida y máximo de horas. Un valor fuera del límite se informa tal cual.",
        "Los documentos dan trazabilidad: la guía de recepción anota qué llegó, cuándo y de qué cuartel; la ficha del lote de uva identifica el lote; el registro de limpieza dice cuándo se limpiaron los equipos y quién lo hizo. El jefe de vendimia organiza, el operador de recepción pesa y recibe, el controlador de calidad toma muestras y el enólogo decide qué se hace con un lote dudoso.",
        f"Las BPM exigen que nadie falsee un registro para que un lote «cumpla». {EMER} {AVISO}",
    ],
    vocab=[("indicador de calidad", "dato que muestra qué tan buena es la uva, como los °Brix"), ("uva podrida", "uva dañada por hongos u otros problemas"), ("lote de uva", "grupo de uva del mismo cuartel y día de cosecha"), ("guía de recepción", "documento que anota qué llegó, cuándo y de dónde"), ("controlador de calidad", "persona que toma muestras y revisa los indicadores"), ("límite de rechazo", "valor desde el cual un lote no se acepta")],
    worked=[
        ("Promedio de °Brix", "Cuatro muestras de ejemplo marcan 22, 24, 24 y 26 °Brix. ¿Cuál es el promedio?", ["Se suman: 22 más 24 más 24 más 26 es 96.", "96 entre 4."], "24 °Brix"),
        ("Tiempo de espera", "La uva de ejemplo se cosechó a las 8 y llegó a las 12. ¿Cuántas horas esperó?", ["Se resta la hora de cosecha a la de llegada.", "12 menos 8."], "4 horas"),
    ],
    mistakes=[("Aceptar un lote con uva podrida sobre el límite «porque llegó mucha uva».", "La uva dañada baja la calidad del vino.", "Se informa y decide el enólogo."),
              ("Cambiar la hora de llegada para cumplir el máximo.", "Falsea el registro.", "Se anota la hora real.")],
    T=[
        ("abc", "En la recepción de uva: ¿qué indica el porcentaje de uva podrida?", "El estado sanitario de la uva", "El azúcar de la uva", "El tamaño de la uva", "La uva podrida indica el estado sanitario."),
        ("abc", "En la recepción de uva: ¿qué es un lote de uva?", "Un grupo de uva del mismo cuartel y día de cosecha", "Un bin vacío", "Un tipo de máquina", "El lote identifica el origen y la fecha."),
        ("abc", "En la recepción de uva: ¿para qué sirve la guía de recepción?", "Para anotar qué llegó, cuándo y de dónde", "Para fijar el precio del vino", "Para medir el azúcar", "La guía da trazabilidad a lo recibido."),
        ("=", "{F} ¿Cuántos kilos tiene cada bin del lote U-03, en promedio?", "24000//40", "Se divide los kilos totales entre el número de bins.", " kg"),
        ("=", "{F} ¿Cuál es el promedio de grados Brix de las cuatro muestras?", "(23+24+24+25)//4", "Se suman las cuatro muestras y se divide entre 4.", " °Brix"),
        ("=", "{F} ¿Cuántas horas pasaron entre el fin de la cosecha y la llegada a recepción?", "11-7", "Se resta la hora de cosecha a la hora de llegada.", " horas"),
        ("abc", "{F} ¿Cumple el lote el límite de uva podrida?", "Sí, porque 3 % es menor que 5 %", "No, porque 3 % es menor que 5 %", "No se puede saber", "3 % está bajo el límite de 5 %."),
        ("abc", "{F} ¿Cumple el lote el tiempo máximo hasta la molienda?", "Sí, hasta ahora, porque pasaron 4 horas y el máximo es 6", "No, porque pasaron 11 horas", "No se puede saber", "Entre las 7 y las 11 pasan 4 horas, que están bajo el máximo."),
        ("abc", "{F} ¿Qué documento anota qué llegó, cuándo y de qué cuartel?", "La guía de recepción", "El registro de limpieza", "La ficha del lote", "La guía registra la llegada de la uva a la bodega."),
        ("abc", "{F} ¿Qué rol decide qué hacer con un lote dudoso?", "El enólogo", "El operador de recepción", "El camionero", "El enólogo decide sobre la calidad."),
        ("abc", "{F} Una compañera dice: «la uva podrida es 3 %, así que se puede esconder en el lote». ¿Qué respuesta es correcta?", "Es incorrecto: la uva podrida se informa y se maneja según el criterio del enólogo", "Es correcto, si es poca", "Es correcto, si nadie lo ve", "Ocultar la uva dañada afecta la calidad."),
        ("abc", "{F} El jefe de vendimia quiere anotar que la uva llegó a las 9 horas, aunque llegó a las 11, «para que cumpla». ¿Qué corresponde?", "Rechazarlo: se anota la hora real", "Aceptarlo, para cumplir el máximo", "Aceptarlo, si lo firma otro", "Cambiar la hora falsea el registro."),
        ("abc", "En la recepción de uva: ¿por qué conviene tomar varias muestras y no una sola?", "Porque una muestra puede no representar a todo el lote", "Porque cuesta menos", "Porque cada muestra cambia el límite", "Varias muestras describen mejor el lote."),
    ],
    ctx=("abc", "Un conocido te pide que firmes como «controlador de calidad» una recepción que no revisaste. ¿Qué respondes?", "Que no, porque firmar sin revisar lo falsea, y que lo consultarás con un adulto responsable", "Que sí, si confías en él", "Que sí, solo una vez", "Una firma certifica una revisión que debe haber ocurrido."),
    sc=[
        ("En la recepción de uva: ¿cómo se calcula el promedio de cuatro muestras?", "Se suman y se dividen entre 4", "El promedio resume las muestras en un solo número."),
        ("En la recepción de uva: ¿qué se hace con un valor fuera del límite?", "Se anota tal cual e informa", "Un registro veraz permite decidir con datos reales."),
        ("En la recepción de uva: ¿quién decide sobre un lote dudoso?", "El enólogo", "El enólogo evalúa la calidad de la uva y del vino."),
    ],
    op=("Registro de ejemplo de la «Viña Demo 3»: lote U-07, 18.000 kg en 30 bins; muestras de °Brix 22, 23, 23 y 24; uva podrida 6 % (límite 5 %); cosecha terminada a las 9 horas y llegada a las 13 horas (máximo 6). Escribe (a) los kilos por bin, (b) el promedio de °Brix, (c) qué indicador no cumple, (d) quién decide qué hacer con el lote.",
        "(a) 18.000 ÷ 30 = 600 kg. (b) (22 + 23 + 23 + 24) ÷ 4 = 23 °Brix. (c) La uva podrida: 6 % supera el límite de 5 %. (d) El enólogo.",
        ["calcula los kilos por bin", "calcula el promedio", "identifica el indicador que no cumple", "nombra al enólogo"],
        ["hoja con las cuatro respuestas"],
        ["no dividir entre los bins", "decir que cumple la uva podrida"],
        "Pregunta: «¿6 está arriba o abajo del límite de 5?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el promedio de estas muestras de °Brix inventadas: 21, 23, 25 y 23.",
    extend="Explica con un ejemplo por qué el tiempo de espera de la uva afecta su calidad.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Cuatro lotes recibidos en la «Viña Demo». L1: 24 °Brix, 2 % de uva podrida, 3 horas desde la cosecha. L2: 24 °Brix, 8 % de uva podrida, 3 horas. L3: 25 °Brix, 1 % de uva podrida, 9 horas. L4: 21 °Brix, 2 % de uva podrida, 4 horas. "
     "Criterios de ejemplo: mínimo 23 °Brix, máximo 5 % de uva podrida y máximo 6 horas. Categorías: A, aceptar; B, retener y consultar al enólogo; C, rechazar por estado sanitario.")
build(
    O2, 3, F,
    use="Aprenderé a analizar lotes de uva recibidos en papel, a comparar cada indicador con su criterio y a clasificar cada lote con evidencia, sin tomar decisiones que corresponden al enólogo.",
    prior=["Sé qué son los indicadores de calidad de la uva.", "Sé comparar valores con límites.", "Sé leer una tabla de datos."],
    explain=[
        "Para analizar un lote se compara cada indicador con su criterio: los °Brix con el mínimo, la uva podrida con el máximo y las horas con el máximo. Si todos cumplen, el lote se acepta. Si falla un indicador de proceso, como el tiempo o el azúcar, el lote se retiene y se consulta al enólogo, que decide qué hacer. Si falla el estado sanitario, es decir, hay demasiada uva podrida, se rechaza el lote, porque puede afectar a toda la partida.",
        "Un buen análisis nombra el lote, el indicador que falla, el criterio y la categoría. El operador de recepción registra, el controlador de calidad revisa y el enólogo decide los casos dudosos. Nadie cambia un dato ni mezcla un lote rechazado con los demás. Cada decisión se anota en la guía de recepción.",
        f"Este análisis es en papel; el manejo de la uva y de las máquinas lo hace personal capacitado. {EMER} {AVISO}",
    ],
    vocab=[("criterio", "valor mínimo o máximo con que se compara un indicador"), ("retener", "dejar un lote aparte hasta que el enólogo decida"), ("rechazar", "no aceptar un lote por incumplir un criterio sanitario"), ("partida", "conjunto de uva que se procesa junta"), ("evidencia", "dato del lote que respalda la categoría")],
    worked=[
        ("Aceptar un lote", "Un lote de ejemplo tiene 25 °Brix, 1 % de uva podrida y 3 horas. Con mínimo 23, máximo 5 % y máximo 6 horas, ¿qué categoría tiene?", ["Cumple los tres criterios.", "Categoría A: aceptar."], "A"),
        ("Retener un lote", "Otro lote de ejemplo tiene 20 °Brix y cumple los demás criterios. ¿Qué categoría tiene?", ["Falla el mínimo de azúcar.", "Se retiene y se consulta al enólogo: categoría B."], "B"),
    ],
    mistakes=[("Mezclar un lote rechazado con otros para «diluir» la uva podrida.", "Contamina la partida y baja la calidad.", "Un lote rechazado se maneja aparte."),
              ("Decidir un lote dudoso sin el enólogo.", "La decisión de calidad es del enólogo.", "Se retiene y se consulta.")],
    T=[
        ("abc", "En la recepción de uva: ¿qué significa retener un lote?", "Dejarlo aparte hasta que el enólogo decida", "Procesarlo de inmediato", "Devolverlo al cuartel", "Retener es esperar la decisión del enólogo."),
        ("abc", "En la recepción de uva: ¿qué es un criterio de aceptación?", "Un valor mínimo o máximo con el que se compara un indicador", "El precio del lote", "El nombre del cuartel", "El criterio es el límite de comparación."),
        ("abc", "En la recepción de uva: ¿por qué no se mezcla un lote rechazado con otros?", "Porque contamina la partida y baja la calidad", "Porque ocupa más espacio", "Porque pesa menos", "La uva dañada afecta a toda la partida."),
        ("abc", "{F} ¿A qué categoría corresponde el lote L1?", "A, aceptar", "B, retener", "C, rechazar", "L1 cumple los tres criterios de aceptación de ejemplo."),
        ("abc", "{F} ¿A qué categoría corresponde el lote L2?", "C, rechazar por estado sanitario", "A, aceptar", "B, retener", "L2 tiene 8 % de uva podrida, más del 5 % permitido."),
        ("abc", "{F} ¿A qué categoría corresponde el lote L3?", "B, retener y consultar al enólogo, por las 9 horas", "A, aceptar", "C, rechazar por estado sanitario", "L3 supera el máximo de 6 horas."),
        ("abc", "{F} ¿A qué categoría corresponde el lote L4?", "B, retener y consultar al enólogo, por los 21 °Brix", "A, aceptar", "C, rechazar", "L4 está bajo el mínimo de 23 °Brix."),
        ("=", "{F} ¿Cuántas horas excede L3 el máximo de ejemplo?", "9-6", "Se resta el máximo al tiempo del lote.", " horas"),
        ("=", "{F} ¿Cuántos puntos de uva podrida excede L2 el límite?", "8-5", "Se resta el límite al porcentaje del lote.", " puntos"),
        ("abc", "{F} Una compañera dice: «mezclemos L2 con L1 para que el promedio de uva podrida sea 5 %». ¿Qué respuesta es correcta?", "Es incorrecto: un lote rechazado no se mezcla y contamina la partida", "Es correcto, porque el promedio cumple", "Es correcto, si se mezcla bien", "Mezclar oculta el problema y daña toda la partida."),
        ("abc", "{F} El jefe de vendimia quiere anotar en L3 que llegó 5 horas después de la cosecha, aunque fueron 9. ¿Qué corresponde?", "Rechazarlo: se anota el tiempo real", "Aceptarlo, para cumplir", "Aceptarlo, si lo firma el capataz", "Cambiar el dato falsea el registro."),
        ("abc", "{F} Una persona se resbala con uva en el piso junto a la tolva y queda cerca del tornillo sin fin. ¿Qué corresponde a quien lo ve?", "No acercarte, avisar a un adulto responsable y a emergencias", "Acercarte a levantarla", "Apagar la tolva tú", "Acercarse a una tolva en marcha es peligroso."),
        ("abc", "En la recepción de uva: ¿por qué la decisión de un lote dudoso es del enólogo?", "Porque conoce los criterios de calidad del vino que se busca", "Porque el enólogo opera la tolva", "Porque el operador no sabe sumar", "El enólogo tiene la responsabilidad técnica de la calidad."),
    ],
    ctx=("abc", "Un conocido te muestra un lote con 8 % de uva podrida y te pide ayuda para «esconderlo» entre los demás. ¿Qué respondes?", "Que no, porque se informa y decide el enólogo, y que lo consultarás con un adulto responsable", "Que sí, si es poca", "Que sí, mezclándola bien", "Ocultar uva dañada afecta la calidad y la inocuidad."),
    sc=[
        ("En la recepción de uva: ¿qué categoría tiene un lote que cumple todos los criterios?", "A, aceptar", "Cumplir todos los criterios permite aceptar."),
        ("En la recepción de uva: ¿qué se hace con un lote con uva podrida sobre el límite?", "Se rechaza por estado sanitario", "La uva dañada afecta a toda la partida."),
        ("En la recepción de uva: ¿quién decide un lote retenido?", "El enólogo", "El enólogo decide los casos dudosos."),
    ],
    op=("Lotes de ejemplo de la «Viña Demo 4» con criterios mínimo 23 °Brix, máximo 5 % de uva podrida y máximo 6 horas: M1, 24 °Brix, 3 %, 2 horas; M2, 22 °Brix, 1 %, 3 horas; M3, 25 °Brix, 9 %, 2 horas. Categorías: A, aceptar; B, retener y consultar; C, rechazar por estado sanitario. Escribe (a) la categoría de cada lote, (b) cuántos puntos excede M3 el límite de uva podrida, (c) quién decide sobre M2, (d) qué haces si alguien queda atrapado en la tolva.",
        "(a) M1: A; M2: B; M3: C. (b) 9 − 5 = 4 puntos. (c) El enólogo. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["clasifica bien los tres lotes", "calcula el exceso", "nombra al enólogo", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["clasificar mal un lote", "proponer liberar a la persona"],
        "Pregunta: «¿qué indicador falla en cada lote?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Clasifica en A, B o C un lote inventado con 24 °Brix, 2 % de uva podrida y 8 horas.",
    extend="Explica con un ejemplo por qué una sola decisión de calidad afecta a toda una partida de uva.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). La «Viña Demo» recibe 24.000 kg de uva en 40 bins con un promedio de 24 °Brix. Precio de ejemplo: $400 por kilo para uva con 23 °Brix, más una bonificación de $10 por kilo por cada °Brix sobre 23. "
     "Rendimiento de mosto de ejemplo: 70 litros de mosto por cada 100 kg de uva. Camión de ejemplo: 10 bins por viaje, $100.000 por viaje.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular el pago por °Brix, el mosto esperado y el costo del transporte de una partida de uva.",
    prior=["Sé qué son los °Brix y el mosto.", "Sé multiplicar y dividir enteros.", "Sé calcular porcentajes sencillos."],
    explain=[
        "El pago de la uva puede depender de su calidad: se fija un precio base para cierto nivel de °Brix y se agrega una bonificación por cada grado sobre ese nivel. El ingreso es los kilos por el precio por kilo, con la bonificación. El mosto esperado es los kilos de uva por el rendimiento de mosto: litros por cada 100 kg, dividido entre 100.",
        "El costo del transporte es el número de viajes por el costo de cada viaje. El número de viajes es los bins totales divididos por los bins de cada viaje. Con estos cálculos se compara el valor de la partida con sus costos. Los valores son de ejemplo y las decisiones las toman el jefe de vendimia y el enólogo. Ningún ahorro justifica saltarse una norma de higiene o de seguridad.",
        f"Los cálculos no reemplazan los controles de calidad ni las BPM. {EMER} {AVISO}",
    ],
    vocab=[("precio base", "precio por kilo para un nivel de calidad de referencia"), ("bonificación", "pago adicional por calidad sobre la referencia"), ("rendimiento de mosto", "litros de mosto por cada 100 kg de uva"), ("viaje", "un recorrido completo del camión cargado"), ("partida", "conjunto de uva que se procesa junta")],
    worked=[
        ("Precio con bonificación", "Un precio base de ejemplo es $300 con una bonificación de $5 por °Brix sobre 20, y la uva tiene 22 °Brix. ¿Cuál es el precio por kilo?", ["Hay 2 °Brix sobre 20.", "300 más 2 por 5 es 310."], "$310"),
        ("Mosto esperado", "Se procesan 5.000 kg de ejemplo con un rendimiento de 60 litros por 100 kg. ¿Cuántos litros de mosto?", ["Se calcula cuántas veces cabe 100 en 5.000.", "50 por 60."], "3.000 litros"),
    ],
    mistakes=[("Aplicar la bonificación a todos los °Brix, y no solo a los que superan la referencia.", "La bonificación es por los grados sobre la referencia.", "Se cuentan solo los °Brix sobre 23."),
              ("Olvidar el costo del transporte al calcular el valor de la partida.", "El costo reduce el margen.", "Se resta el costo de los viajes.")],
    T=[
        ("abc", "En la vendimia: ¿qué es una bonificación por calidad?", "Un pago adicional por calidad sobre la referencia", "Un descuento por baja calidad", "El costo del transporte", "La bonificación premia la calidad sobre la referencia."),
        ("abc", "En la vendimia: ¿qué es el rendimiento de mosto?", "Los litros de mosto por cada 100 kg de uva", "Los kilos de uva por hectárea", "El precio de la uva", "El rendimiento relaciona uva y mosto."),
        ("abc", "En la vendimia: ¿cómo se obtiene el número de viajes del camión?", "Dividiendo los bins totales entre los bins de cada viaje", "Multiplicando los kilos por el precio", "Sumando los °Brix", "Los viajes resultan de dividir el total entre la capacidad."),
        ("=", "{F} ¿Cuántos °Brix sobre la referencia de 23 tiene la uva?", "24-23", "Se resta la referencia al promedio de °Brix.", " °Brix"),
        ("=", "{F} ¿Cuál es el precio por kilo, con la bonificación?", "400+10*(24-23)", "Se suma al precio base la bonificación por cada °Brix sobre 23.", " pesos"),
        ("=", "{F} ¿Cuál es el ingreso por toda la partida?", "24000*(400+10*(24-23))", "Se multiplican los kilos por el precio por kilo con bonificación.", " pesos"),
        ("=", "{F} ¿Cuántos litros de mosto se esperan?", "24000//100*70", "Se calcula cuántas veces cabe 100 kg en la partida y se multiplica por 70 litros.", " litros"),
        ("=", "{F} ¿Cuántos viajes necesita el camión para los 40 bins?", "40//10", "Se dividen los bins totales entre los bins de cada viaje.", " viajes"),
        ("=", "{F} ¿Cuánto cuesta el transporte de la partida?", "40//10*100000", "Se multiplican los viajes por el costo de cada uno.", " pesos"),
        ("=", "{F} ¿Cuál es el ingreso menos el costo del transporte?", "24000*(400+10*(24-23))-40//10*100000", "Se resta el costo del transporte al ingreso.", " pesos"),
        ("abc", "{F} Un jefe propone cargar 12 bins por viaje para ahorrar un viaje. ¿Qué corresponde?", "Rechazarlo: se respeta la capacidad de carga del camión", "Aceptarlo, para ahorrar", "Aceptarlo, si el camino es corto", "Sobrecargar un camión es peligroso para las personas y la carga."),
        ("abc", "{F} Una estudiante quiere manejar el camión de bins porque ya calculó los viajes. ¿Qué corresponde?", "Rechazarlo: conducir exige licencia y autorización", "Aceptarlo, si va despacio", "Aceptarlo, si hay poco tránsito", "Calcular viajes no habilita para conducir."),
        ("abc", "En la vendimia: ¿por qué el costo del transporte reduce el margen?", "Porque es un gasto que se resta al ingreso", "Porque suma al ingreso", "Porque no se paga", "El costo se resta del ingreso."),
    ],
    ctx=("abc", "Un conocido te pregunta cuánto le pagarán por su uva y te da solo los kilos. ¿Qué respondes?", "Que faltan los °Brix y las condiciones del contrato, y que lo calcula con su comprador", "Que le pagarán $400 por kilo", "Que no le pagarán", "El pago depende de la calidad y del contrato."),
    sc=[
        ("En la vendimia: ¿cómo se calcula el ingreso por la uva?", "Kilos por precio por kilo", "El ingreso multiplica kilos y precio."),
        ("En la vendimia: ¿cómo se calcula el mosto esperado?", "Kilos entre 100 por los litros de rendimiento", "El rendimiento se aplica por cada 100 kg."),
        ("En la vendimia: ¿cómo se calcula el costo del transporte?", "Viajes por el costo de cada viaje", "El costo se multiplica por los viajes."),
    ],
    op=("Datos de ejemplo de la «Viña Demo 5»: 12.000 kg de uva en 20 bins con 25 °Brix; precio base $350 por kilo a 23 °Brix, más $10 por kilo por cada °Brix sobre 23; rendimiento de 65 litros de mosto por 100 kg; camión de 10 bins por viaje a $80.000 por viaje. Escribe (a) el precio por kilo, (b) el ingreso, (c) el mosto esperado, (d) el costo de transporte.",
        "(a) 350 + 10 × (25 − 23) = $370. (b) 12.000 × 370 = $4.440.000. (c) 12.000 ÷ 100 × 65 = 7.800 litros. (d) 20 ÷ 10 × 80.000 = $160.000.",
        ["calcula el precio por kilo", "calcula el ingreso", "calcula el mosto", "calcula el costo de transporte"],
        ["hoja con las cuatro respuestas"],
        ["aplicar la bonificación a todos los °Brix", "olvidar dividir entre 100"],
        "Pregunta: «¿cuántos °Brix hay sobre 23?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el mosto esperado de 8.000 kg de uva con 60 litros por 100 kg.",
    extend="Explica con un ejemplo por qué no se sobrecarga un camión aunque se ahorre un viaje.",
)

# ============================================================ OAM-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Bodega Demo» tiene estanques de acero con mosto en fermentación, una pasarela sobre los estanques con barandas parciales, bombas y mangueras para mover líquidos, y productos de uso enológico guardados en una sala. "
     "Peligros anotados: dióxido de carbono que se acumula en la bodega y dentro de los estanques, la entrada a los estanques (un espacio cerrado), la pasarela en altura, bombas con partes móviles, piso mojado, agua caliente de limpieza y productos de uso enológico que pueden irritar la piel y los ojos.")
build(
    O3, 1, F,
    use="Aprenderé qué son la fermentación, el descube, el trasiego y los tratamientos enológicos como conceptos, y cuáles son los peligros de una bodega de vinificación, sin aprender a hacerlos.",
    prior=["Sé qué son la vendimia, el mosto y las BPM.", "Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita."],
    explain=[
        "El mosto se transforma en vino por la fermentación alcohólica: unos microorganismos llamados levaduras convierten el azúcar del mosto en alcohol y en dióxido de carbono, un gas. Al terminar, el descube es separar el vino líquido de los orujos, que son los restos sólidos de la uva, como los hollejos y las semillas. El trasiego es pasar el vino de un recipiente a otro para separarlo de las borras, que son los sedimentos del fondo. Los tratamientos enológicos son prácticas, como clarificar o filtrar, que indica el enólogo según lo que permite la norma vigente.",
        "Estos trabajos tienen peligros graves. El dióxido de carbono no tiene olor ni color, es más pesado que el aire y se acumula en estanques, fosos y lugares bajos, donde puede quitar el aire y causar la muerte; por eso nadie entra a un estanque. La pasarela en altura puede causar caídas; las bombas pueden atrapar; los productos de uso enológico pueden irritar. La jerarquía de controles ordena las medidas: eliminar, sustituir, cambiar el lugar o el equipo, reglas y, al final, EPP.",
        f"Un detector de dióxido de carbono con alarma es un control de ingeniería; una regla de no entrar a los estanques es administrativa. Estas tareas las hace personal capacitado y autorizado; este cuaderno no enseña a elaborar vino. {EMER} {AVISO}",
    ],
    vocab=[("fermentación alcohólica", "transformación del azúcar del mosto en alcohol y dióxido de carbono por levaduras"), ("descube", "separación del vino líquido de los orujos"), ("orujo", "restos sólidos de la uva, como hollejos y semillas"), ("trasiego", "paso del vino de un recipiente a otro para separarlo de las borras"), ("borras", "sedimentos del fondo del recipiente"), ("tratamiento enológico", "práctica que indica el enólogo, como clarificar o filtrar"), ("dióxido de carbono", "gas sin olor ni color que se forma en la fermentación")],
    worked=[
        ("Distinguir descube y trasiego", "En una bodega de ejemplo se pasa el vino de un estanque a otro para separarlo de los sedimentos del fondo. ¿Es descube o trasiego?", ["No se separa de los orujos, sino de las borras.", "Es trasiego."], "Trasiego"),
        ("Clasificar un control", "Una bodega de ejemplo instala una baranda completa en toda la pasarela sobre los estanques. ¿Qué tipo de control es?", ["La baranda cambia físicamente el lugar de trabajo.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que se puede entrar a un estanque «solo un momento» si se contiene la respiración.", "El dióxido de carbono puede ser mortal en segundos.", "Nadie entra a un estanque: lo hace personal autorizado con equipos."),
              ("Creer que los tratamientos enológicos son recetas que cualquiera puede aplicar.", "El enólogo los indica según la norma vigente.", "Se aprenden los conceptos y se deja la práctica a personal autorizado.")],
    T=[
        ("abc", "En la bodega: ¿qué es el descube?", "La separación del vino líquido de los orujos", "El paso del vino a otro recipiente para separarlo de las borras", "La ruptura de las bayas", "El descube separa vino y orujo; el trasiego separa vino y borras."),
        ("abc", "En la bodega: ¿qué son las borras?", "Los sedimentos del fondo del recipiente", "La cáscara de la uva", "El azúcar del mosto", "Las borras son sedimentos; el orujo son restos sólidos de la uva."),
        ("abc", "En la bodega: ¿qué produce la fermentación alcohólica?", "Alcohol y dióxido de carbono a partir del azúcar", "Azúcar a partir del alcohol", "Agua y sal", "Las levaduras convierten el azúcar en alcohol y gas."),
        ("=", "{F} Un estanque de ejemplo tiene 6.000 litros. ¿Cuántos litros hay en 3 estanques iguales?", "6000*3", "Se multiplican los litros de cada estanque por el número de estanques.", " litros"),
        ("abc", "{F} Un detector de dióxido de carbono con alarma es un control de tipo:", "De ingeniería, porque es un equipo que actúa sin depender de las personas", "Administrativo, porque es una regla", "De EPP, porque protege a quien trabaja", "El detector funciona aunque nadie se acuerde de la regla."),
        ("abc", "{F} Una regla que dice «nadie entra a un estanque sin autorización» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el estanque", "De sustitución, porque cambia el mosto", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al dióxido de carbono acumulado en un estanque?", "Que quite el aire a quien entre y cause la muerte", "El gas mismo en el estanque", "Que la bodega tenga estanques", "El riesgo es la posibilidad de daño; el gas acumulado es el peligro."),
        ("abc", "{F} Una estudiante dice: «ya aprendí el trasiego, así que me meto al estanque a limpiar el fondo». ¿Qué respuesta es correcta?", "Es mortal: nadie entra a un estanque y la limpieza la hace personal autorizado", "Es correcto, si contiene la respiración", "Es correcto, si la acompaña una compañera", "El gas puede quitar el aire en segundos."),
        ("abc", "{F} Una persona se desmaya cerca de un estanque abierto. ¿Qué corresponde según las reglas generales?", "No acercarte, avisar a un adulto responsable y a emergencias", "Acercarte a ayudarla", "Entrar al estanque a buscar", "Acercarte puede hacerte perder el conocimiento a ti también."),
        ("abc", "En la bodega: ¿por qué el dióxido de carbono se acumula en lugares bajos?", "Porque es más pesado que el aire", "Porque es más liviano que el aire", "Porque tiene olor fuerte", "El gas pesado se acumula abajo."),
        ("abc", "{F} Se propone solo entregar mascarillas contra el dióxido de carbono. ¿Qué medida es más efectiva?", "Ventilar la bodega, instalar detectores y no entrar a los estanques", "Entregar mascarillas más gruesas", "Pedir que se contenga la respiración", "Una mascarilla común no protege de la falta de aire."),
        ("=", "{F} Una bomba de ejemplo mueve 3.000 litros por hora. ¿Cuántas horas necesita para mover un estanque de 6.000 litros?", "6000//3000", "Se divide el volumen del estanque entre lo que mueve la bomba por hora.", " horas"),
        ("abc", "En la bodega: ¿por qué los tratamientos enológicos los indica el enólogo?", "Porque deben ajustarse a lo que permite la norma vigente y a cada vino", "Porque cualquier persona puede indicarlos", "Porque no tienen efectos", "Los tratamientos exigen criterio técnico y respeto de la norma."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por entrar a limpiar un estanque vacío «porque ya sabes cómo se hace». ¿Qué respondes?", "Que no, porque es un espacio cerrado peligroso y exige formación y equipos, y que lo consultarás con un adulto responsable", "Que sí, un rato", "Que sí, con una cuerda", "Un estanque puede acumular dióxido de carbono aunque parezca vacío."),
    sc=[
        ("En la bodega: ¿qué es el trasiego?", "Pasar el vino de un recipiente a otro para separarlo de las borras", "El trasiego separa el vino de las borras."),
        ("En la bodega de vinificación: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En la bodega: ¿qué gas peligroso se acumula en los estanques?", "El dióxido de carbono", "Es un gas sin olor ni color."),
    ],
    op=("La «Bodega Demo 2» anota una tarea de ejemplo: entrar a limpiar un estanque donde acaba de terminar la fermentación, sin ventilar y sin detector, con otra persona esperando afuera. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si la persona que entró no responde.",
        "(a) Peligro: dióxido de carbono acumulado en el estanque; riesgo: que la persona pierda el conocimiento y muera. (b) Una regla de que nadie entra a un estanque sin autorización. (c) Un detector con alarma y un sistema de ventilación. (d) No entro, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no entra y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al gas", "proponer entrar a rescatar", "proponer solo mascarilla"],
        "Pregunta: «¿qué control avisa del gas aunque nadie se acuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Une cada término con su definición: descube, trasiego, orujo y borras.",
    extend="Explica con un ejemplo por qué un estanque vacío puede seguir siendo peligroso.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 2 (registros de ejemplo, inventados). Libro de bodega de la «Bodega Demo»: 5 de abril, estanque E-1, entran 7.000 litros de mosto de la variedad A; 20 de abril, descube del E-1, se obtienen 6.300 litros de vino. "
     "Registro de temperaturas de fermentación del E-1: rango de ejemplo de 22 a 28 grados; lecturas de tres días: 24, 26 y 30. Documentos: el libro de bodega (movimientos de cada estanque), el registro de temperaturas, el registro de análisis del laboratorio y el registro de tratamientos indicados por el enólogo. Roles: enólogo, jefe de bodega, bodeguero y analista de laboratorio.")
build(
    O3, 2, F,
    use="Aprenderé a leer los registros de una bodega, a calcular volúmenes y pérdidas y a conocer los roles de quienes controlan los descubes, trasiegos y tratamientos.",
    prior=["Sé qué son descube, trasiego y tratamiento enológico.", "Sé restar y calcular porcentajes enteros.", "Sé leer una ficha de datos."],
    explain=[
        "Un registro de bodega anota cada movimiento del vino: qué estanque, cuántos litros, qué día y quién lo hizo. El libro de bodega permite saber cuánto vino hay y de dónde viene cada partida. La diferencia entre lo que entra y lo que sale es una pérdida y debe tener explicación: orujo, borras o evaporación. Un registro cuyo balance no cuadra se informa tal cual.",
        "La temperatura de fermentación se controla con un rango, porque si sube demasiado se pierden aromas y si baja demasiado la fermentación se detiene. El análisis de laboratorio mide características del vino, como el alcohol o la acidez. Los tratamientos se anotan con su fecha, su producto y su indicación del enólogo. El jefe de bodega organiza, el bodeguero ejecuta con capacitación, el analista mide y el enólogo decide.",
        f"Un registro de bodega nunca se altera para que el balance «cuadre». {EMER} {AVISO}",
    ],
    vocab=[("libro de bodega", "registro de los movimientos de cada estanque"), ("balance de volumen", "comparación entre los litros que entran y los que salen"), ("pérdida", "diferencia entre lo que entra y lo que sale"), ("rango de temperatura", "valores mínimo y máximo aceptables de temperatura"), ("registro de análisis", "documento con los resultados del laboratorio"), ("analista de laboratorio", "persona que mide las características del vino")],
    worked=[
        ("Pérdida de volumen", "Un estanque de ejemplo recibe 5.000 litros y entrega 4.600 litros de vino. ¿Cuál es la pérdida?", ["Se resta lo que sale a lo que entra.", "5.000 menos 4.600."], "400 litros"),
        ("Comparar con el rango", "El rango es de 20 a 26 grados y la lectura es 28. ¿Está fuera de rango?", ["28 es mayor que 26.", "Está fuera de rango."], "Sí, está fuera de rango"),
    ],
    mistakes=[("Anotar un volumen distinto para que el balance cuadre.", "Un registro alterado oculta pérdidas o errores.", "Se anota el volumen real y se informa."),
              ("Creer que una temperatura alta durante la fermentación no importa.", "Puede perjudicar la calidad del vino.", "Se informa al enólogo.")],
    T=[
        ("abc", "En la bodega: ¿qué es el libro de bodega?", "El registro de los movimientos de cada estanque", "El plano de la bodega", "El manual de las bombas", "El libro de bodega anota los movimientos."),
        ("abc", "En la bodega: ¿qué es una pérdida de volumen?", "La diferencia entre los litros que entran y los que salen", "El total de litros guardados", "El precio de un litro", "La pérdida resulta de la comparación entre lo que entra y sale."),
        ("abc", "En la bodega: ¿qué rol mide las características del vino en el laboratorio?", "El analista de laboratorio", "El bodeguero", "El comprador", "El analista mide en el laboratorio."),
        ("=", "{F} ¿Cuántos litros se perdieron entre el mosto que entró al E-1 y el vino que se obtuvo?", "7000-6300", "Se resta el vino obtenido al mosto que entró.", " litros"),
        ("=", "{F} ¿Qué porcentaje del mosto que entró representa la pérdida?", "(7000-6300)*100//7000", "Se divide la pérdida entre el mosto que entró y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos grados superó la lectura del tercer día el máximo del rango?", "30-28", "Se resta el máximo del rango a la lectura.", " grados"),
        ("abc", "{F} ¿Qué lectura de la ficha está fuera del rango de temperatura?", "La de 30 grados", "La de 24 grados", "La de 26 grados", "Solo 30 supera el máximo de 28."),
        ("abc", "{F} ¿Qué documento anota los tratamientos indicados por el enólogo?", "El registro de tratamientos", "El libro de bodega", "El registro de temperaturas", "El registro de tratamientos guarda las indicaciones."),
        ("abc", "{F} ¿A quién se informa la lectura fuera de rango?", "Al enólogo y al jefe de bodega", "Al comprador", "A nadie, porque es un solo día", "La temperatura puede perjudicar el vino y debe informarse."),
        ("abc", "{F} Un bodeguero dice: «el balance no cuadra por 200 litros, anoto 7.000 litros de vino para que cuadre». ¿Qué respuesta es correcta?", "Es incorrecto: se anota el volumen real y se informa la diferencia", "Es correcto, para que el balance cuadre", "Es correcto, si nadie revisa", "Alterar un registro oculta una pérdida."),
        ("abc", "{F} El jefe de bodega quiere anotar 28 grados en vez de 30 en la tercera lectura. ¿Qué corresponde?", "Rechazarlo: se anota el valor real e informa", "Aceptarlo, para cumplir el rango", "Aceptarlo, si lo firma el enólogo", "Cambiar la lectura falsea el registro."),
        ("abc", "{F} Una persona se asoma a un estanque en fermentación para mirar y se marea. ¿Qué corresponde a quien lo ve?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Asomarte a ayudar", "Entrar al estanque", "El gas puede hacerte perder el conocimiento a ti también."),
        ("abc", "En la bodega: ¿por qué un balance de volumen que no cuadra debe informarse?", "Porque puede señalar una fuga, un error o una pérdida", "Porque ocupa espacio en el libro", "Porque se corrige solo", "Un balance que no cuadra puede ocultar un problema."),
    ],
    ctx=("abc", "Un conocido te pide que firmes como «jefe de bodega» un libro con movimientos que no viste. ¿Qué respondes?", "Que no, porque firmar sin haber visto lo falsea, y que lo consultarás con un adulto responsable", "Que sí, si confías", "Que sí, solo una vez", "Una firma certifica algo que debe haber ocurrido."),
    sc=[
        ("En la bodega: ¿cómo se calcula la pérdida de volumen?", "Litros que entran menos litros que salen", "La pérdida es la diferencia entre entrada y salida."),
        ("En la bodega: ¿qué se hace con una lectura fuera de rango?", "Se anota tal cual y se informa", "Un registro veraz permite actuar a tiempo ante un problema."),
        ("En la bodega: ¿quién indica los tratamientos?", "El enólogo", "El enólogo decide los tratamientos según la norma."),
    ],
    op=("Libro de bodega de ejemplo de la «Bodega Demo 3»: entran 9.000 litros de mosto al estanque E-2 y se obtienen 8.100 litros de vino tras el descube; temperaturas de fermentación 23, 25 y 29 grados con rango de ejemplo de 22 a 27. Escribe (a) la pérdida en litros, (b) el porcentaje de pérdida, (c) qué lectura está fuera de rango, (d) a quién la informas.",
        "(a) 9.000 − 8.100 = 900 litros. (b) 900 × 100 ÷ 9.000 = 10 %. (c) La de 29 grados, porque supera 27. (d) Al enólogo y al jefe de bodega.",
        ["calcula la pérdida", "calcula el porcentaje", "identifica la lectura fuera de rango", "informa a quien corresponde"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "alterar la lectura"],
        "Pregunta: «¿cuántos litros entraron y cuántos salieron?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula la pérdida de un estanque inventado que recibe 4.000 litros y entrega 3.700.",
    extend="Explica con un ejemplo por qué un balance de volumen debe tener una explicación para cada pérdida.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Observaciones del día en la «Bodega Demo». X1, la temperatura de fermentación del estanque E-3 es de 31 grados y el rango de ejemplo es de 22 a 28. "
     "X2, el detector de dióxido de carbono de la sala de estanques suena y un operario dice sentirse mareado. X3, el libro de bodega del E-4 no cuadra: entraron 8.000 litros y salieron 7.200, con 400 litros anotados como orujo y borras. "
     "X4, el E-5 fermenta con 25 grados y sin anomalías. Categorías: A, evacuar el lugar y avisar de inmediato; B, informar al enólogo o al jefe de bodega; C, sin acción.")
build(
    O3, 3, F,
    use="Aprenderé a analizar un caso de bodega en papel, a clasificar cada observación por su urgencia y a decidir quién actúa, sin intervenir estanques ni equipos.",
    prior=["Sé qué son el dióxido de carbono y los registros de bodega.", "Sé calcular pérdidas de volumen.", "Sé comparar un valor con un rango."],
    explain=[
        "Para analizar un caso de bodega se clasifica cada observación según su urgencia. Una alarma del detector de dióxido de carbono con una persona mareada es una emergencia: se evacúa el lugar y se avisa. Una temperatura fuera de rango no es una emergencia inmediata, pero se informa al enólogo porque puede perjudicar el vino. Un balance de volumen que no cuadra también se informa. Lo normal no necesita acción, pero se sigue vigilando.",
        "Un buen análisis nombra la observación, la categoría, la evidencia y quién actúa. El operario avisa, el jefe de bodega decide la evacuación y la parada de equipos, el enólogo decide los ajustes del proceso y el personal autorizado, con equipos y formación, revisa el lugar. Nadie entra a buscar a una persona caída en un estanque ni sigue trabajando con la alarma encendida.",
        f"Si suena una alarma de gas, las personas se alejan por el camino indicado y piden ayuda. {EMER} {AVISO}",
    ],
    vocab=[("evacuar", "salir de un lugar de forma ordenada por una emergencia"), ("alarma", "señal sonora o luminosa que avisa de un peligro"), ("urgencia", "qué tan rápido hay que actuar"), ("diferencia sin explicar", "litros que faltan y no tienen justificación en el registro"), ("evidencia", "dato del caso que respalda una categoría")],
    worked=[
        ("Clasificar la urgencia", "Un estanque de ejemplo marca 29 grados y el rango es de 22 a 28. ¿A qué categoría corresponde?", ["Es un desvío del proceso, no una emergencia.", "Se informa al enólogo o al jefe de bodega: categoría B."], "B"),
        ("Diferencia sin explicar", "Un estanque de ejemplo recibió 5.000 litros y entregó 4.500, con 300 litros justificados. ¿Cuántos litros quedan sin explicar?", ["La pérdida es 500.", "500 menos 300."], "200 litros"),
    ],
    mistakes=[("Seguir trabajando con la alarma de gas encendida «porque debe estar fallando».", "El gas es invisible y puede ser real.", "Se evacúa y se avisa; personal autorizado revisa."),
              ("Entrar a un estanque a buscar a una persona caída.", "Quien entra puede perder el conocimiento también.", "Se avisa a emergencias y no se entra.")],
    T=[
        ("abc", "En la bodega: ¿qué significa evacuar un lugar?", "Salir de forma ordenada por una emergencia", "Limpiar el lugar", "Cerrar el lugar con llave", "Evacuar es salir por una emergencia."),
        ("abc", "En la bodega: ¿qué es una alarma?", "Una señal que avisa de un peligro", "Un registro de temperatura", "Un tratamiento enológico", "La alarma avisa de un peligro."),
        ("abc", "En la bodega: ¿qué es una diferencia sin explicar en un balance?", "Litros que faltan y no tienen justificación en el registro", "Litros que sobran por una buena cosecha", "El total de litros del estanque", "La diferencia sin explicar es un faltante sin justificación."),
        ("abc", "{F} ¿A qué categoría corresponde X2, alarma de gas con un operario mareado?", "A, evacuar el lugar y avisar de inmediato", "B, informar al enólogo", "C, sin acción", "Hay riesgo inmediato para las personas."),
        ("abc", "{F} ¿A qué categoría corresponde X1, temperatura de 31 grados con rango de 22 a 28?", "B, informar al enólogo o al jefe de bodega", "A, evacuar el lugar", "C, sin acción", "Es un desvío del proceso, no una emergencia."),
        ("abc", "{F} ¿A qué categoría corresponde X3, el balance que no cuadra?", "B, informar al enólogo o al jefe de bodega", "A, evacuar el lugar", "C, sin acción", "La diferencia sin explicar debe informarse."),
        ("abc", "{F} ¿A qué categoría corresponde X4, el E-5 con 25 grados y sin anomalías?", "C, sin acción", "A, evacuar el lugar", "B, informar", "25 grados está dentro del rango."),
        ("=", "{F} ¿Cuántos litros salieron menos de los que entraron en el E-4?", "8000-7200", "Se resta lo que salió a lo que entró.", " litros"),
        ("=", "{F} ¿Cuántos litros quedan sin explicar en el E-4, descontando los 400 litros anotados?", "8000-7200-400", "Se resta la pérdida justificada a la pérdida total.", " litros"),
        ("abc", "{F} Una compañera dice: «la alarma debe estar mala, sigamos trabajando». ¿Qué respuesta es correcta?", "Es peligroso: se evacúa y se avisa, y personal autorizado revisa el detector", "Es correcto, si no huele nada", "Es correcto, si el operario está bien", "El gas no tiene olor y puede ser real."),
        ("abc", "{F} Un operario se desmaya junto a un estanque abierto y otro quiere entrar a sacarlo. ¿Qué corresponde a quien lo ve?", "Impedirlo con aviso: no entrar y avisar a un adulto responsable y a emergencias", "Ayudarlo a entrar", "Entrar tú primero", "Entrar puede costar la vida de otra persona."),
        ("abc", "{F} El jefe de bodega quiere anotar que los 200 litros sin explicar fueron «evaporación». ¿Qué corresponde?", "Rechazarlo: no se inventa una explicación, se informa", "Aceptarlo, para que cuadre", "Aceptarlo, si nadie pregunta", "Una explicación inventada falsea el registro."),
        ("abc", "En la bodega: ¿por qué la categoría A tiene prioridad sobre la B?", "Porque hay riesgo inmediato para las personas", "Porque es más fácil de atender", "Porque no necesita registro", "El riesgo inmediato se atiende primero."),
    ],
    ctx=("abc", "Un conocido te cuenta que suena la alarma de gas de su bodega y pregunta si puede ignorarla porque «siempre falla». ¿Qué respondes?", "Que evacúe y avise, y que personal autorizado revise la alarma", "Que la ignore", "Que se acerque a mirar el estanque", "Una alarma de gas siempre se toma en serio."),
    sc=[
        ("En la bodega: ¿qué se hace cuando suena la alarma de gas?", "Se evacúa y se avisa", "El gas puede quitar el aire."),
        ("En la bodega: ¿qué categoría tiene una temperatura fuera de rango?", "B, informar al enólogo o al jefe de bodega", "Es un desvío, no una emergencia."),
        ("En la bodega: ¿qué se hace con una diferencia sin explicar?", "Se informa, sin inventar una explicación", "Inventar una explicación falsea el registro."),
    ],
    op=("Observaciones de ejemplo de la «Bodega Demo 4»: Y1, el detector de gas suena y una persona se tambalea; Y2, el E-6 marca 30 grados con rango de ejemplo de 22 a 28; Y3, el E-7 entró con 6.000 litros y salió con 5.400, con 300 litros justificados; Y4, el E-8 está normal. Categorías: A, evacuar y avisar; B, informar; C, sin acción. Escribe (a) la categoría de cada observación, (b) cuántos litros quedan sin explicar en Y3, (c) quién decide sobre Y2, (d) qué haces si alguien cae junto a un estanque.",
        "(a) Y1: A; Y2: B; Y3: B; Y4: C. (b) 6.000 − 5.400 − 300 = 300 litros. (c) El enólogo, con el jefe de bodega. (d) No me acerco ni entro, aviso a un adulto responsable y a emergencias.",
        ["clasifica bien las cuatro observaciones", "calcula los litros sin explicar", "nombra quién decide", "no entra y avisa"],
        ["hoja con las cuatro respuestas"],
        ["clasificar el gas como normal", "proponer entrar a rescatar"],
        "Pregunta: «¿qué observación tiene riesgo inmediato para las personas?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Clasifica en A, B o C tres observaciones inventadas: alarma de gas, temperatura normal y balance que no cuadra.",
    extend="Explica con un ejemplo por qué nadie entra a un estanque a rescatar a otra persona.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Estanque E-9 de la «Bodega Demo»: entran 8.000 litros de mosto. Tras el descube se obtienen 7.200 litros de vino. Primer trasiego: se pierde el 2 % del volumen en borras. Segundo trasiego: se pierden 56 litros. "
     "Valor de ejemplo del vino: $800 por litro. Costo de ejemplo de cada trasiego: $120.000 (personal y energía).")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular volúmenes, pérdidas y costos de un estanque a lo largo del descube y los trasiegos.",
    prior=["Sé qué son descube y trasiego.", "Sé calcular porcentajes y pérdidas.", "Sé multiplicar y restar enteros."],
    explain=[
        "El volumen de vino disminuye en cada etapa: en el descube porque parte del líquido queda retenido en los orujos, y en cada trasiego porque se separan las borras. El rendimiento del descube es el vino obtenido dividido por el mosto que entró, por 100. La pérdida de un trasiego puede darse como porcentaje del volumen; se calcula multiplicando el volumen por el porcentaje y dividiendo entre 100, y se resta al volumen. La pérdida total es el mosto inicial menos el vino final.",
        "El valor de la pérdida es los litros perdidos por el valor del litro, y el costo de los trasiegos es su número por el costo de cada uno. Con esto se decide, junto con el enólogo, si un trasiego adicional conviene. Los valores son de ejemplo, y nada de esto reemplaza el criterio técnico del enólogo ni la seguridad de las personas.",
        f"Los trasiegos y los tratamientos los hace personal capacitado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("rendimiento del descube", "vino obtenido dividido por el mosto que entró, por 100"), ("pérdida total", "mosto inicial menos vino final"), ("valor de la pérdida", "litros perdidos por el valor de cada litro"), ("costo de trasiego", "gasto de cada trasiego en personal y energía"), ("volumen final", "litros de vino después de todas las etapas")],
    worked=[
        ("Rendimiento", "En un estanque de ejemplo entran 5.000 litros y se obtienen 4.500. ¿Cuál es el rendimiento del descube?", ["Se divide 4.500 entre 5.000, que es nueve décimos.", "Nueve décimos son 90 de cada 100."], "90 %"),
        ("Pérdida de un trasiego", "Un trasiego de ejemplo pierde el 2 % de 4.500 litros. ¿Cuántos litros se pierden?", ["Se calcula el 2 % de 4.500.", "4.500 por 2 entre 100."], "90 litros"),
    ],
    mistakes=[("Calcular la pérdida del segundo trasiego sobre el mosto inicial.", "Cada trasiego pierde sobre el volumen que tiene en ese momento.", "Se actualiza el volumen después de cada etapa."),
              ("Alterar los volúmenes del libro de bodega para que el balance cuadre.", "Se oculta una pérdida real.", "Se anotan los volúmenes reales.")],
    T=[
        ("abc", "En la bodega: ¿qué es el rendimiento del descube?", "El vino obtenido dividido por el mosto que entró, por 100", "Los litros que caben en el estanque", "El número de trasiegos", "El rendimiento compara vino obtenido y mosto inicial."),
        ("abc", "En la bodega: ¿qué es la pérdida total de un estanque?", "El mosto inicial menos el vino final", "El vino final menos el mosto inicial", "El precio del vino", "La pérdida total resta lo que queda de lo que entró."),
        ("abc", "En la bodega: ¿por qué cada trasiego pierde sobre el volumen del momento?", "Porque el volumen ya disminuyó en las etapas anteriores", "Porque siempre se pierde sobre el mosto inicial", "Porque el costo cambia", "Cada etapa parte con el volumen que quedó."),
        ("=", "{F} ¿Cuál es el rendimiento del descube, en porcentaje?", "7200*100//8000", "Se divide el vino obtenido entre el mosto que entró y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos litros se pierden en el primer trasiego?", "7200*2//100", "Se calcula el 2 % del volumen que tiene el estanque.", " litros"),
        ("=", "{F} ¿Cuántos litros quedan después del primer trasiego?", "7200-7200*2//100", "Se resta la pérdida del primer trasiego al volumen del descube.", " litros"),
        ("=", "{F} ¿Cuántos litros quedan después del segundo trasiego?", "7200-7200*2//100-56", "Se resta la pérdida del segundo trasiego al volumen anterior.", " litros"),
        ("=", "{F} ¿Cuál es la pérdida total del estanque, desde el mosto inicial?", "8000-(7200-7200*2//100-56)", "Se resta el vino final al mosto inicial.", " litros"),
        ("=", "{F} ¿Cuál es el valor de la pérdida de los dos trasiegos, a $800 por litro?", "(7200*2//100+56)*800", "Se multiplican los litros perdidos en los trasiegos por el valor de cada litro.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan los dos trasiegos en total?", "2*120000", "Se multiplican los trasiegos por el costo de cada uno.", " pesos"),
        ("abc", "{F} Un bodeguero propone no registrar la pérdida del segundo trasiego «porque es chica». ¿Qué corresponde?", "Rechazarlo: toda pérdida se registra para que el balance cuadre con datos reales", "Aceptarlo, porque es chica", "Aceptarlo, si nadie pregunta", "Una pérdida no registrada oculta el volumen real."),
        ("abc", "{F} Una estudiante quiere ayudar con el trasiego porque ya sabe calcular las pérdidas. ¿Qué corresponde?", "Rechazarlo: el trasiego lo hace personal capacitado y autorizado", "Aceptarlo, si usa guantes", "Aceptarlo, si va con un compañero", "Calcular no habilita para trabajar con equipos y estanques."),
        ("abc", "En la bodega: ¿por qué conviene calcular el costo de cada etapa?", "Para decidir con datos si un trasiego adicional conviene", "Para reemplazar al enólogo", "Para evitar los registros", "El costo ayuda a decidir junto con el criterio técnico."),
    ],
    ctx=("abc", "Un conocido te pregunta cuánto vino saldrá de su mosto y te da solo los litros de mosto. ¿Qué respondes?", "Que faltan los rendimientos y las pérdidas de cada etapa, y que lo calcula con su enólogo", "Que saldrá lo mismo", "Que saldrá la mitad", "Cada etapa tiene pérdidas que dependen del proceso."),
    sc=[
        ("En la bodega: ¿cómo se calcula el rendimiento del descube?", "Vino obtenido entre mosto, por 100", "El rendimiento es un porcentaje del mosto que entró."),
        ("En la bodega: ¿cómo se calcula la pérdida de un trasiego en porcentaje?", "Volumen por porcentaje entre 100", "La pérdida es un porcentaje del volumen actual."),
        ("En la bodega: ¿cómo se calcula el valor de una pérdida?", "Litros perdidos por el valor del litro", "El valor multiplica litros y precio."),
    ],
    op=("Datos de ejemplo de la «Bodega Demo 5»: entran 6.000 litros de mosto; tras el descube se obtienen 5.100; el primer trasiego pierde el 4 %; el valor del vino es $700 por litro. Escribe (a) el rendimiento del descube, (b) los litros perdidos en el trasiego, (c) el volumen final, (d) el valor de la pérdida del trasiego.",
        "(a) 5.100 × 100 ÷ 6.000 = 85 %. (b) 5.100 × 4 ÷ 100 = 204 litros. (c) 5.100 − 204 = 4.896 litros. (d) 204 × 700 = $142.800.",
        ["calcula el rendimiento", "calcula la pérdida", "calcula el volumen final", "calcula el valor de la pérdida"],
        ["hoja con las cuatro respuestas"],
        ["calcular la pérdida sobre el mosto inicial", "no multiplicar por el valor"],
        "Pregunta: «¿sobre qué volumen se calcula el 4 %?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el 3 % de 6.000 litros.",
    extend="Explica con un ejemplo por qué las pérdidas de cada etapa se registran por separado.",
)
