"""Montaje Industrial TP 3.º y 4.º medio: OAE-09 (residuos y desechos del montaje industrial) y OAE-10 (calcular y cubicar materiales). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_moin_common import AVISO, EMER, build

O9 = "TP-MOIN-3y4-OAE-09"
O10 = "TP-MOIN-3y4-OAE-10"

# ============================================================ OAE-09, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). En una semana de montaje una obra ficticia genera: 600 kg de chatarra metálica; 20 envases con restos de pintura (40 kg en total); 15 kg de trapos con solvente; 300 kg de madera de embalaje; "
     "80 kg de cartón y plástico; y 25 kg de restos de soldadura. La obra no tiene un lugar separado y señalizado para los residuos peligrosos.")
build(
    O9, 1, F,
    use="Aprenderé qué residuos genera un montaje industrial, cuáles son peligrosos, cuál es el orden de preferencia para manejarlos y qué riesgos tiene hacerlo mal.",
    prior=["Sé sumar y multiplicar números enteros.", "Sé qué es una hoja de datos de seguridad.", "Sé qué es la jerarquía de controles."],
    explain=[
        "Un residuo es todo material que ya no se usa y se desecha. En un montaje hay residuos no peligrosos, como la chatarra metálica, la madera de embalaje, el cartón y el plástico, y residuos peligrosos, como los solventes, los trapos con solvente y los envases con restos de pintura, que pueden dañar la salud o el ambiente. Un residuo peligroso nunca se mezcla con los demás ni se bota a la basura común, a un desagüe o al suelo.",
        "El orden de preferencia para manejar residuos es reducir, reutilizar, reciclar y, al final, eliminar. Reducir es generar menos; reutilizar es volver a usar un material sin transformarlo; reciclar es transformarlo en un material nuevo; eliminar es dejar el residuo en un lugar autorizado cuando no se pudo aprovechar. Los residuos se separan en el lugar donde se generan, se guardan temporalmente en contenedores rotulados y las empresas autorizadas los retiran, según la norma vigente y la autoridad competente. Los riesgos de hacerlo mal son incendios, contaminación, cortes con chatarra e intoxicaciones.",
        f"Este cuaderno no enseña a manipular sustancias ni a limpiar derrames. {EMER} Ante un derrame o un olor fuerte, aléjate también y avisa. {AVISO}",
    ],
    vocab=[("residuo", "material que ya no se usa y se desecha"), ("residuo peligroso", "residuo que puede dañar la salud o el ambiente"), ("reducir", "generar menos residuos"), ("reutilizar", "volver a usar un material sin transformarlo"), ("reciclar", "transformar un residuo en un material nuevo"), ("eliminar", "dejar el residuo en un lugar autorizado cuando no se pudo aprovechar")],
    worked=[
        ("Clasificar un residuo", "Un tarro de ejemplo con restos de pintura se quiere desechar. ¿Es un residuo peligroso o no peligroso?", ["La pintura con solvente puede dañar la salud y el ambiente.", "Es un residuo peligroso."], "Peligroso"),
        ("Sumar masas", "Una obra de ejemplo genera 120 kg, 45 kg y 15 kg de tres residuos. ¿Cuántos kilogramos son en total?", ["Se suman las tres masas.", "120 más 45 más 15 son 180."], "180 kg"),
    ],
    mistakes=[("Botar un envase con restos de pintura a la basura común.", "Es un residuo peligroso que contamina y puede causar incendios.", "Se guarda aparte y lo retira una empresa autorizada."),
              ("Mezclar todos los residuos en un solo contenedor para ahorrar espacio.", "Un residuo peligroso contamina al resto y encarece el retiro.", "Sepáralos por tipo en el lugar donde se generan.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es un residuo peligroso?", "Un residuo que puede dañar la salud o el ambiente, como los solventes", "Un residuo muy pesado", "Un residuo que se puede vender", "La peligrosidad se define por el daño posible, no por el peso ni por el valor."),
        ("abc", "En Montaje Industrial: ¿qué significa reciclar un residuo?", "Transformarlo en un material o producto nuevo", "Guardarlo para después en un rincón de la obra", "Reutilizarlo sin ningún cambio", "Reciclar implica transformar; volver a usar sin cambios es reutilizar."),
        ("abc", "En Montaje Industrial: ¿cuál es el orden de preferencia para manejar residuos, de mejor a menos deseable?", "Reducir, reutilizar, reciclar y eliminar", "Eliminar, reciclar, reutilizar y reducir", "Reciclar, eliminar, reducir y reutilizar", "Lo mejor es no generar el residuo y lo último es eliminarlo."),
        ("=", "{F} ¿Cuántos kilogramos de residuos genera la obra en la semana?", "600+40+15+300+80+25", "Se suman las masas de todos los residuos de la ficha.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos de residuos peligrosos hay, sumando los envases con restos de pintura y los trapos con solvente?", "40+15", "Se suman las masas de los dos residuos peligrosos.", " kg"),
        ("abc", "{F} ¿Cuál de estos residuos de la ficha es peligroso?", "Los trapos con solvente", "La madera de embalaje", "El cartón y el plástico", "El solvente de los trapos puede dañar la salud y el ambiente."),
        ("abc", "{F} ¿Qué le falta a la obra para manejar bien sus residuos peligrosos?", "Un lugar separado, señalizado y adecuado para guardarlos temporalmente", "Más cantidad de chatarra", "Un contenedor para el cartón", "Los peligrosos exigen un acopio temporal separado y señalizado."),
        ("=", "{F} El retiro de residuos peligrosos cuesta $1.500 por kg (valor de ejemplo). ¿Cuánto cuesta retirar los de la ficha?", "(40+15)*1500", "Se multiplican los kilogramos peligrosos por el costo de cada kilogramo.", " pesos"),
        ("=", "{F} La chatarra se vende a $200 por kg (valor de ejemplo). ¿Cuánto se obtiene por la chatarra de la semana?", "600*200", "Se multiplican los kilogramos de chatarra por el precio de cada kilogramo.", " pesos"),
        ("abc", "{F} Un compañero propone botar los trapos con solvente a la basura común porque «son pocos». ¿Qué respuesta es correcta?", "No: son residuos peligrosos y se guardan aparte para un retiro autorizado, sin importar la cantidad", "Sí, si están secos", "Sí, si se envuelven en una bolsa", "La peligrosidad no depende de la cantidad."),
        ("abc", "Durante una visita de ejemplo, un envase de solvente se vuelca y una persona siente picazón en los ojos. ¿Qué corresponde según las reglas generales?", "Alejarte de la zona de riesgo, avisar a un adulto responsable y a emergencias", "Limpiar el derrame con las manos", "Tirar agua sobre el derrame", "Un solvente derramado es un riesgo; lo atienden personas capacitadas."),
        ("=", "{F} Si toda la chatarra se vendiera para reciclar, ¿cuántos kilogramos de residuos quedarían por retirar?", "(600+40+15+300+80+25)-600", "Se resta la chatarra vendida a los residuos totales.", " kg"),
        ("abc", "{F} El jefe propone mezclar todo en un solo contenedor «para ahorrar espacio». ¿Qué respuesta es correcta?", "No: mezclar peligrosos con no peligrosos contamina todo y encarece el retiro; se separan en origen", "Sí, así se hace un solo retiro", "Sí, si el contenedor es grande", "Separar en origen evita contaminar y reduce costos y riesgos."),
    ],
    ctx=("abc", "El jefe de obra de ejemplo te dice: «vacía los restos de solvente en el desagüe del patio, nadie se va a dar cuenta». ¿Qué respondes?", "Que no, porque es un residuo peligroso que contamina el agua y debe retirarlo una empresa autorizada", "Que sí, si es poca cantidad", "Que sí, si abres el agua para diluirlo", "Un solvente en el desagüe contamina, y la cantidad no cambia su peligrosidad."),
    sc=[
        ("En Montaje Industrial: ¿cuál es la forma preferible de manejar un residuo?", "Reducirlo, generando menos", "Lo mejor es no generar el residuo."),
        ("¿Dónde no se botan los residuos peligrosos?", "A la basura común, al desagüe ni al suelo", "Contaminan el ambiente y pueden dañar a personas."),
        ("En montaje industrial: ¿quién retira los residuos peligrosos?", "Una empresa autorizada", "La norma vigente exige gestores autorizados."),
    ],
    op=("Obra de ejemplo: en una semana se generan 500 kg de chatarra, 25 kg de trapos con solvente, 10 envases con restos de pintura (20 kg en total), 200 kg de madera y 60 kg de cartón y plástico. Escribe (a) los kg totales, (b) los kg de residuos peligrosos, (c) qué se hace con los peligrosos, (d) una forma de reducir los residuos de madera.",
        "(a) 500 + 25 + 20 + 200 + 60 = 805 kg. (b) 25 + 20 = 45 kg. (c) Se guardan aparte en un lugar señalizado y los retira una empresa autorizada. (d) Pedir los materiales con embalajes retornables o reutilizar la madera de embalaje en la obra.",
        ["suma los kg totales", "suma los peligrosos", "indica cómo gestionarlos", "propone una forma de reducir"],
        ["hoja con las cuatro respuestas"],
        ["olvidar sumar un residuo", "botar los peligrosos a la basura común", "no proponer una medida de reducción"],
        "Pregunta: «¿qué hace peligroso a un residuo?». Si no responde, pídele que relea la definición."),
    reinforce="Clasifica en peligrosos y no peligrosos cinco residuos de un montaje inventado.",
    extend="Explica con un ejemplo por qué es mejor reducir un residuo que reciclarlo.",
)

# ============================================================ OAE-09, clase 2
F = ("Ficha 2 (plan de manejo y registro de ejemplo, inventados). Contenedores rotulados: A, chatarra metálica; B, madera; C, cartón y plástico; D, residuos peligrosos. "
     "Registro semanal en kg: semana 1: A 300, B 150, C 40, D 20; semana 2: A 450, B 100, C 60, D 35. Regla de ejemplo: el contenedor D se retira cuando acumula 100 kg. "
     "Documentos del retiro de D: una guía de transporte y, después, el certificado de disposición final de la empresa autorizada que lo recibe.")
build(
    O9, 2, F,
    use="Aprenderé los documentos y roles del manejo de residuos, qué es la separación en origen, el acopio temporal y la trazabilidad, y a leer un registro de residuos.",
    prior=["Sé la diferencia entre residuo peligroso y no peligroso.", "Sé leer una tabla.", "Sé sumar números enteros."],
    explain=[
        "El plan de manejo de residuos define qué residuos se generan, cómo se separan, en qué contenedores rotulados se guardan temporalmente y quién los retira. La separación en origen consiste en dejar cada residuo en su contenedor en el lugar donde se genera. El acopio temporal es el almacenamiento ordenado y señalizado mientras llega el retiro. La valorización es el aprovechamiento de un residuo por reutilización o reciclaje, y la disposición final es su destino definitivo en un lugar autorizado.",
        "La trazabilidad es poder seguir un residuo, con documentos, desde que se genera hasta su destino. Para los peligrosos, el retiro lo hace un transportista autorizado con una guía de transporte, y la empresa que los recibe entrega un certificado de disposición final. El registro de residuos anota las cantidades por tipo y por fecha. Los roles son los trabajadores, que separan en origen; el encargado ambiental o el prevencionista, que controla el plan; el jefe de obra, que responde por él; el transportista autorizado; y la empresa autorizada que recibe los residuos.",
        f"Los nombres, cantidades y reglas de esta clase son de ejemplo, y los reales dependen de la norma vigente y de la autoridad competente. {EMER} {AVISO}",
    ],
    vocab=[("separación en origen", "dejar cada residuo en su contenedor donde se genera"), ("acopio temporal", "almacenamiento ordenado y señalizado mientras llega el retiro"), ("valorización", "aprovechamiento de un residuo por reutilización o reciclaje"), ("disposición final", "destino definitivo de un residuo en un lugar autorizado"), ("trazabilidad", "posibilidad de seguir un residuo con documentos hasta su destino"), ("guía de transporte", "documento que acompaña un residuo peligroso durante su traslado")],
    worked=[
        ("Leer un registro", "Un registro de ejemplo anota, en la semana 1, 80 kg de madera y, en la semana 2, 120 kg. ¿Cuántos kg de madera se acumulan?", ["Se suman las dos semanas.", "80 más 120 son 200."], "200 kg"),
        ("Elegir el contenedor", "Un tarro con restos de pintura se debe guardar en el plan de ejemplo. ¿En qué tipo de contenedor?", ["Es un residuo peligroso.", "Va en el contenedor de peligrosos."], "El de residuos peligrosos"),
    ],
    mistakes=[("Retirar un residuo peligroso sin guía de transporte.", "Se pierde la trazabilidad y se puede incumplir la norma.", "El retiro lo hace un transportista autorizado con su guía."),
              ("Creer que el registro de residuos es solo un trámite.", "Sin registro no se controlan cantidades ni se planifican retiros.", "Anota cantidades por tipo y por fecha.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es la separación de residuos en origen?", "Dejar cada residuo en su contenedor en el lugar donde se genera", "Juntar todos los residuos en un contenedor", "Pesar los residuos al final del mes", "Separar en origen evita mezclas y contaminación."),
        ("abc", "En Montaje Industrial: ¿qué es la trazabilidad de un residuo peligroso?", "Poder seguirlo con documentos desde que se genera hasta su destino final", "Pintarlo de colores para reconocerlo", "Contarlo una vez al día", "La trazabilidad es el seguimiento documentado del residuo."),
        ("abc", "En Montaje Industrial: ¿qué es el acopio temporal de residuos?", "Su almacenamiento ordenado y señalizado mientras llega el retiro", "Su destino definitivo en un relleno", "Su transformación en un material nuevo", "El acopio es temporal; el destino definitivo es la disposición final."),
        ("=", "{F} ¿Cuántos kilogramos de residuos se registraron en la semana 1 en total?", "300+150+40+20", "Se suman los cuatro contenedores de la semana 1.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos de residuos se registraron en la semana 2 en total?", "450+100+60+35", "Se suman los cuatro contenedores de la semana 2.", " kg"),
        ("abc", "{F} ¿En qué contenedor se guardan los trapos con solvente?", "En D, el de residuos peligrosos", "En B, el de madera", "En C, el de cartón y plástico", "Los trapos con solvente son residuos peligrosos."),
        ("=", "{F} ¿Cuántos kilogramos lleva acumulados el contenedor D después de las dos semanas?", "20+35", "Se suman los kilogramos de D de las dos semanas.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos le faltan a D para alcanzar la regla de retiro?", "100-(20+35)", "Se resta lo acumulado a los 100 kg de la regla.", " kg"),
        ("abc", "{F} ¿Qué documentos acompañan el retiro de D?", "La guía de transporte y, después, el certificado de disposición final", "Solo una fotografía del contenedor", "La factura de compra de la pintura", "Esos documentos permiten seguir el residuo hasta su destino."),
        ("abc", "{F} Alguien propone retirar D de inmediato «para no acumular», sin guía de transporte. ¿Qué respuesta es correcta?", "No: sin guía no hay trazabilidad y el retiro debe hacerlo un transportista autorizado", "Sí, si el contenedor está lleno", "Sí, si lo lleva un compañero en su auto", "Un residuo peligroso solo se traslada con transportista autorizado y documentos."),
        ("abc", "{F} ¿Quién debe recibir los residuos peligrosos de D?", "Una empresa autorizada que entregue un certificado de disposición final", "Cualquier persona que acepte llevárselos", "El proveedor de la pintura, sin documento", "Solo un gestor autorizado puede recibirlos y certificar su destino."),
        ("=", "{F} ¿Cuántos kilogramos de chatarra se acumularon en las dos semanas?", "300+450", "Se suman los kilogramos del contenedor A de las dos semanas.", " kg"),
        ("abc", "{F} Un compañero dice: «el registro semanal es solo para cumplir». ¿Qué respuesta es correcta?", "Es falso: permite controlar cantidades, planificar retiros y demostrar el manejo correcto", "Es cierto, y se puede llenar sin medir", "Es cierto, si el jefe lo firma", "El registro es una herramienta de control y de evidencia."),
    ],
    ctx=("abc", "El jefe de obra de ejemplo te pide registrar 50 kg en el contenedor D aunque no se pesó, «para que cuadre con lo que dirá la empresa». ¿Qué respondes?", "Que se registra solo lo realmente medido, y que se pese antes de anotar", "Que sí, para que cuadre", "Que sí, si el número parece razonable", "Un registro inventado rompe la trazabilidad y puede ocultar un manejo incorrecto."),
    sc=[
        ("En Montaje Industrial: ¿qué es la valorización de un residuo?", "Aprovecharlo por reutilización o reciclaje", "La valorización evita eliminar lo que aún sirve."),
        ("¿Qué documento acompaña el traslado de un residuo peligroso?", "La guía de transporte", "Permite seguir el residuo durante el traslado."),
        ("¿Qué entrega la empresa que recibe un residuo peligroso?", "Un certificado de disposición final", "Es la evidencia del destino definitivo del residuo."),
    ],
    op=("Plan de ejemplo: contenedores A (chatarra), B (madera) y D (peligrosos). Registro: semana 1: A 200, B 80, D 10; semana 2: A 260, B 120, D 25 (kg). Regla de ejemplo: D se retira al llegar a 50 kg. Escribe (a) el total de cada semana, (b) lo acumulado en D y cuánto le falta para el retiro, (c) los documentos del retiro de D, (d) por qué se registra lo realmente pesado.",
        "(a) Semana 1: 200 + 80 + 10 = 290 kg; semana 2: 260 + 120 + 25 = 405 kg. (b) 10 + 25 = 35 kg; faltan 15 kg. (c) La guía de transporte y el certificado de disposición final de la empresa autorizada. (d) Porque el registro permite la trazabilidad y no debe contener datos inventados.",
        ["calcula los totales", "calcula lo acumulado y lo que falta", "nombra los documentos", "explica la veracidad del registro"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal las semanas", "olvidar la guía de transporte", "proponer anotar números sin pesar"],
        "Pregunta: «¿quién retira los residuos peligrosos?». Si no responde, pídele que relea el párrafo de trazabilidad."),
    reinforce="Inventa un registro de dos semanas para tres contenedores y calcula el total acumulado de cada uno.",
    extend="Explica con un ejemplo por qué el certificado de disposición final es parte de la trazabilidad.",
)

# ============================================================ OAE-09, clase 3
F = ("Ficha 3 (balance mensual de ejemplo, inventado). Residuos del mes: 2.000 kg en total. Chatarra, 800 kg, que se vende. Madera, 500 kg: se reutilizan 200 kg y 300 kg se retiran. Cartón y plástico, 200 kg, que se reciclan. "
     "Residuos peligrosos, 100 kg, que retira una empresa autorizada. Escombros, 400 kg, que van a disposición autorizada. Valores de ejemplo: retiro de peligrosos, $1.500 por kg; retiro de madera restante y escombros, $120 por kg; venta de chatarra, $200 por kg.")
build(
    O9, 3, F,
    use="Aprenderé a analizar un balance de residuos, a calcular qué parte se valoriza y cuál se elimina, y a calcular el costo neto del manejo de un mes.",
    prior=["Sé qué es valorizar y eliminar.", "Sé calcular un porcentaje simple.", "Sé multiplicar y sumar números enteros."],
    explain=[
        "Un balance de residuos reúne las cantidades generadas y su destino. La parte valorizada es la que se aprovecha: se vende, se reutiliza o se recicla. La parte eliminada es la que va a retiro o a disposición final. El porcentaje valorizado es lo valorizado por 100 dividido entre el total, y mientras más alto, menos residuos se eliminan.",
        "El costo neto del manejo se calcula sumando los costos de retiro y restando los ingresos por venta, como los de la chatarra. Un costo neto positivo es un gasto, y uno negativo es una ganancia. El costo no es el único criterio: un residuo peligroso mal manejado puede costar mucho más en salud, daño ambiental y multas, y por eso nunca se mezcla para ahorrar. Además, los números de un balance deben provenir de pesajes y documentos reales.",
        f"Todas las cifras de esta clase son de ejemplo, y los costos reales dependen del mercado y de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("balance de residuos", "tabla con las cantidades generadas y su destino"), ("parte valorizada", "residuos que se venden, reutilizan o reciclan"), ("parte eliminada", "residuos que van a retiro o a disposición final"), ("costo neto", "costos de retiro menos ingresos por venta"), ("ingreso por venta", "dinero que se recibe por vender un residuo aprovechable")],
    worked=[
        ("Porcentaje valorizado", "Un mes de ejemplo genera 500 kg de residuos, de los que se valorizan 350 kg. ¿Qué porcentaje se valoriza?", ["Se multiplica 350 por 100 y se divide entre 500.", "35.000 entre 500 son 70."], "70 %"),
        ("Costo neto", "Un mes de ejemplo tiene costos de retiro de $80.000 e ingresos por venta de $50.000. ¿Cuál es el costo neto?", ["Se restan los ingresos a los costos.", "80.000 menos 50.000 son 30.000."], "30.000 pesos"),
    ],
    mistakes=[("Contar como valorizada la madera que se retira a disposición.", "Solo se valoriza lo que se aprovecha.", "Suma solo lo vendido, reutilizado o reciclado."),
              ("Mezclar residuos peligrosos con otros para ahorrar un retiro.", "Todo el lote pasa a ser peligroso y se contamina.", "Mantén la separación en origen aunque cueste más.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es la parte valorizada de un balance de residuos?", "La que se aprovecha porque se vende, reutiliza o recicla", "La que va a retiro o a disposición final", "La que se genera durante el mes", "Valorizar es aprovechar; lo eliminado va a retiro o disposición."),
        ("abc", "En Montaje Industrial: ¿qué es la disposición final?", "El destino definitivo de un residuo que no se pudo aprovechar, en un lugar autorizado", "La venta de un residuo al mejor precio", "El reciclaje de un residuo", "La disposición final es el último destino cuando no hay valorización."),
        ("abc", "En Montaje Industrial: ¿qué es el costo neto de un manejo de residuos?", "Los costos de retiro menos los ingresos por venta", "El precio de un contenedor", "El total de kilogramos generados", "El costo neto descuenta los ingresos a los costos."),
        ("=", "{F} ¿Cuántos kilogramos se valorizan en el mes (chatarra vendida, madera reutilizada y cartón y plástico reciclados)?", "800+200+200", "Se suman la chatarra, la madera reutilizada y el cartón y plástico.", " kg"),
        ("=", "{F} ¿Qué porcentaje del total del mes se valoriza?", "(800+200+200)*100//2000", "Se multiplica lo valorizado por 100 y se divide entre el total.", " %"),
        ("=", "{F} ¿Cuántos kilogramos van a retiro o a disposición (madera restante, peligrosos y escombros)?", "300+100+400", "Se suman la madera restante, los peligrosos y los escombros.", " kg"),
        ("=", "{F} ¿Cuánto cuesta el retiro de los residuos peligrosos?", "100*1500", "Se multiplican los kilogramos por el costo de cada kilogramo.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta el retiro de la madera restante y de los escombros?", "(300+400)*120", "Se suman los kilogramos y se multiplican por el costo de cada kilogramo.", " pesos"),
        ("=", "{F} ¿Cuánto se obtiene por la venta de la chatarra?", "800*200", "Se multiplican los kilogramos de chatarra por el precio de cada kilogramo.", " pesos"),
        ("=", "{F} ¿Cuál es el costo neto del mes, con los costos de retiro menos el ingreso por la chatarra?", "100*1500+(300+400)*120-800*200", "Se suman los dos costos de retiro y se resta el ingreso por la chatarra.", " pesos"),
        ("abc", "{F} Un compañero propone mezclar los peligrosos con los escombros para pagar un solo retiro más barato. ¿Qué respuesta es correcta?", "No: mezclarlos contamina todo el lote, que pasaría a manejarse como peligroso", "Sí, si los escombros son pocos", "Sí, si el transportista no se da cuenta", "La mezcla convierte todo el lote en peligroso y daña el ambiente."),
        ("=", "{F} Si se reutilizaran 100 kg más de madera, ¿cuántos kilogramos de madera quedarían para retiro?", "300-100", "Se restan los kilogramos reutilizados adicionales a la madera restante.", " kg"),
        ("=", "{F} Con esa reutilización adicional de 100 kg de madera, ¿qué porcentaje del total del mes se valoriza?", "(800+200+200+100)*100//2000", "Se suma lo reutilizado adicional a lo valorizado y se calcula el porcentaje.", " %"),
    ],
    ctx=("abc", "El jefe de ejemplo quiere botar los envases con restos de pintura al contenedor de escombros para «bajar el costo neto». ¿Qué respondes?", "Que no: son residuos peligrosos, se mantienen separados y los retira una empresa autorizada aunque cueste más", "Que sí, si el costo neto baja", "Que sí, si se tapan los envases", "El costo no justifica mezclar residuos peligrosos con otros."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula el costo neto de un manejo?", "Costos de retiro menos ingresos por venta", "Se descuenta lo que se gana a lo que se paga."),
        ("¿Qué porcentaje valorizado indica más residuos aprovechados?", "El más alto", "A más valorización, menos residuos terminan eliminados."),
        ("¿De dónde deben provenir los números de un balance?", "De pesajes y documentos reales", "Un balance inventado no sirve para decidir."),
    ],
    op=("Balance de ejemplo: residuos del mes, 1.000 kg en total: chatarra, 400 kg (se vende); madera, 200 kg (se retiran); cartón y plástico, 150 kg (se reciclan); peligrosos, 50 kg (retiro autorizado); escombros, 200 kg (disposición). Valores de ejemplo: peligrosos, $1.500 por kg; madera y escombros, $100 por kg; chatarra, $200 por kg. Escribe (a) los kg valorizados y su porcentaje, (b) los kg eliminados, (c) el costo neto del mes.",
        "(a) 400 + 150 = 550 kg; 550 × 100 ÷ 1.000 = 55 %. (b) 200 + 50 + 200 = 450 kg. (c) Costos: 50 × 1.500 + (200 + 200) × 100 = 75.000 + 40.000 = 115.000; ingreso: 400 × 200 = 80.000; costo neto: 115.000 − 80.000 = 35.000 pesos.",
        ["calcula lo valorizado y su porcentaje", "calcula lo eliminado", "calcula el costo neto"],
        ["hoja con los cálculos"],
        ["incluir la madera como valorizada", "olvidar el ingreso de la chatarra", "mezclar los peligrosos con los escombros"],
        "Pregunta: «¿qué residuos se aprovechan?». Si no responde, pídele que relea la definición de parte valorizada."),
    reinforce="Calcula el porcentaje valorizado de un mes de ejemplo con 400 kg totales y 100 kg valorizados.",
    extend="Explica con un ejemplo por qué el menor costo no siempre es la mejor decisión en residuos.",
)

# ============================================================ OAE-09, clase 4
F = ("Ficha 4 (plan de reducción de ejemplo, inventado). Residuos del mes anterior: 2.000 kg. Residuos del mes actual: 1.700 kg. Meta de ejemplo: reducir 20 % respecto del mes anterior. "
     "Medidas propuestas: reutilizar la madera de embalaje en la obra, que evita 150 kg; devolver los pallets al proveedor, que evita 100 kg. Un retiro con contenedor admite 500 kg y cuesta $60.000 (valores de ejemplo).")
build(
    O9, 4, F,
    use="Aprenderé a fijar y verificar una meta de reducción de residuos, a calcular el efecto de medidas de reducción y de reutilización y a calcular los retiros necesarios y su costo.",
    prior=["Sé qué es reducir y reutilizar.", "Sé calcular un porcentaje simple.", "Sé dividir y redondear hacia arriba."],
    explain=[
        "Una meta de reducción es un objetivo de generar menos residuos, expresado en porcentaje o en kilogramos, para un período. Para verificarla se calcula el máximo permitido, restando el porcentaje de reducción al mes anterior, y se compara con lo generado. El porcentaje de reducción logrado es lo reducido por 100 dividido entre el mes anterior. Las medidas de reducción y de reutilización disminuyen lo generado y también el número de retiros.",
        "Los retiros se calculan dividiendo los kilogramos por retirar entre la capacidad de cada retiro y redondeando hacia arriba, porque un retiro parcial también se paga completo. Reducir en origen es preferible a reciclar o eliminar, porque evita generar el residuo y sus costos y riesgos. Si una meta no se cumple, se registra el resultado real y se proponen medidas; nunca se cambian los registros para parecer que sí.",
        f"Las cifras son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("meta de reducción", "objetivo de generar menos residuos en un período"), ("máximo permitido", "cantidad que no se debe superar para cumplir la meta"), ("reducción lograda", "diferencia entre lo generado el mes anterior y el actual"), ("retiro", "viaje de una empresa autorizada para llevarse los residuos acopiados"), ("pallet", "plataforma de madera o plástico sobre la que se transportan materiales")],
    worked=[
        ("Máximo permitido", "Un mes anterior de ejemplo generó 1.000 kg y la meta es reducir 10 %. ¿Cuántos kg se pueden generar como máximo?", ["Se calcula el 90 % del mes anterior.", "1.000 por 90 entre 100 son 900 kg."], "900 kg"),
        ("Retiros necesarios", "Hay 1.300 kg por retirar y cada retiro admite 400 kg. ¿Cuántos retiros se necesitan?", ["1.300 entre 400 da 3 y sobran 100 kg.", "Se redondea hacia arriba: 4 retiros."], "4 retiros"),
    ],
    mistakes=[("Contar la reducción como porcentaje del mes actual y no del anterior.", "La meta se mide respecto del mes anterior.", "Divide lo reducido entre lo generado el mes anterior."),
              ("Cambiar el registro para que la meta parezca cumplida.", "Se pierde el control real y no se corrige la causa.", "Registra lo real y propone medidas de reducción.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es una meta de reducción de residuos?", "Un objetivo de generar menos residuos en un período, en porcentaje o en kilogramos", "Una lista de contenedores", "El peso total de un retiro", "La meta fija cuánto se pretende reducir, no cuánto se retira."),
        ("abc", "En Montaje Industrial: ¿qué significa reutilizar un material?", "Volver a usarlo sin transformarlo", "Quemarlo en la obra", "Reciclarlo en una planta", "Reutilizar no transforma el material; reciclar sí."),
        ("abc", "En Montaje Industrial: ¿por qué reducir en origen es preferible a reciclar?", "Porque evita generar el residuo y sus costos y riesgos", "Porque es más difícil", "Porque no necesita planificación", "Lo mejor es no generar el residuo desde el principio."),
        ("=", "{F} ¿Cuántos kilogramos puede generar como máximo el mes actual para cumplir la meta?", "2000*80//100", "Se calcula el 80 % del mes anterior.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos se redujeron respecto del mes anterior?", "2000-1700", "Se resta lo del mes actual a lo del mes anterior.", " kg"),
        ("=", "{F} ¿Qué porcentaje de reducción se logró?", "(2000-1700)*100//2000", "Se multiplica por 100 lo reducido y se divide entre el mes anterior.", " %"),
        ("abc", "{F} ¿Se cumplió la meta de 20 % con los 1.700 kg del mes actual?", "No: se logró 15 % y faltan 100 kg para llegar al máximo permitido", "Sí, porque 1.700 es menor que 2.000", "Sí, porque 15 % es mayor que 10 %", "El máximo permitido es 1.600 kg y se generaron 1.700."),
        ("=", "{F} Con las dos medidas propuestas, ¿cuántos kilogramos generaría el mes?", "1700-150-100", "Se restan los kilogramos que evita cada medida.", " kg"),
        ("abc", "{F} Con esa generación de 1.450 kg, ¿se cumpliría la meta?", "Sí, porque 1.450 es menor que el máximo permitido de 1.600", "No, porque 1.450 es mayor que 1.000", "No, porque faltan 100 kg", "Con las medidas, lo generado queda bajo el máximo permitido."),
        ("=", "{F} Con 1.700 kg por retirar, ¿cuántos retiros de 500 kg hacen falta, redondeando hacia arriba?", "(1700+499)//500", "Se divide entre 500 y se redondea hacia arriba.", " retiros"),
        ("abc", "{F} Un compañero propone «cumplir la meta» sin registrar 150 kg de residuos. ¿Qué respuesta es correcta?", "No: falsear el registro no reduce residuos y oculta el problema", "Sí, si nadie revisa el registro", "Sí, si los 150 kg son de madera", "Un registro falso no cambia la cantidad real de residuos."),
        ("=", "{F} Con las medidas, ¿cuántos retiros de 500 kg hacen falta para 1.450 kg, redondeando hacia arriba?", "(1450+499)//500", "Se divide entre 500 y se redondea hacia arriba.", " retiros"),
        ("=", "{F} Sin las medidas hacen falta 4 retiros y con ellas 3. ¿Cuántos pesos se ahorran en retiros?", "(4-3)*60000", "Se multiplica el retiro que se evita por el costo de cada retiro.", " pesos"),
    ],
    ctx=("abc", "La jefa de ejemplo te pide: «anota 1.600 kg en el informe, así se cumple la meta». Se generaron 1.700 kg. ¿Qué respondes?", "Que no: se anota lo real, 1.700 kg, y se proponen medidas para el mes siguiente", "Que sí, para cumplir", "Que sí, pero anotando 1.650", "Un registro falso impide aprender y corregir."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula el máximo permitido con una meta de 20 %?", "Se calcula el 80 % del mes anterior", "Se resta el porcentaje de reducción al mes anterior."),
        ("¿Por qué los retiros se redondean hacia arriba?", "Porque un retiro parcial también se paga completo", "No existen retiros fraccionados: se paga el viaje completo."),
        ("En montaje industrial: ¿qué se hace si la meta no se cumple?", "Se registra el resultado real y se proponen medidas", "Los registros no se alteran para aparentar un resultado."),
    ],
    op=("Plan de ejemplo: mes anterior, 1.000 kg; mes actual, 880 kg; meta de reducir 15 %. Medida propuesta: reutilizar embalajes, que evita 50 kg. Cada retiro admite 300 kg. Escribe (a) el máximo permitido para cumplir la meta, (b) si se cumplió con 880 kg, (c) los kg con la medida y si cumpliría, (d) cuántos retiros hacen falta para esa cantidad.",
        "(a) 1.000 × 85 ÷ 100 = 850 kg. (b) No: 880 supera 850 en 30 kg. (c) 880 − 50 = 830 kg: sí cumpliría, porque es menor que 850. (d) 830 ÷ 300 es 2 con resto; se redondea hacia arriba: 3 retiros.",
        ["calcula el máximo permitido", "compara con lo generado", "aplica la medida", "calcula los retiros"],
        ["hoja con los cuatro cálculos"],
        ["restar mal el porcentaje", "no redondear los retiros hacia arriba", "alterar el registro para cumplir"],
        "Pregunta: «¿respecto de qué mes se mide la meta?». Si no responde, pídele que relea el párrafo de la meta de reducción."),
    reinforce="Calcula el máximo permitido de residuos si el mes anterior fue de 600 kg y la meta es reducir 10 %.",
    extend="Explica con un ejemplo por qué una medida de reducción también reduce el número de retiros.",
)

# ============================================================ OAE-10, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La empresa ficticia «Montajes Demo» cubica una estructura de ejemplo: 10 pilares, 16 vigas, 42 m de cañería y 90 pernos. La planilla digital incluye el nombre y el teléfono de la persona dueña del proyecto. "
     "Peligros anotados para la bodega: perfiles apilados muy altos que pueden caer y unidades confundidas (kg y t) en los pedidos.")
build(
    O10, 1, F,
    use="Aprenderé qué es cubicar materiales e insumos, para qué sirve, qué errores y riesgos tiene y cómo se cuidan los datos del cliente y la salud al trabajar con planillas.",
    prior=["Sé sumar y multiplicar números enteros.", "Sé qué es una escala y una lista de piezas.", "Sé que 1 t son 1.000 kg."],
    explain=[
        "Cubicar es calcular las cantidades de materiales, insumos y otros elementos que necesita un proyecto, a partir de los planos y las especificaciones técnicas. Cada elemento que se cuenta y se cobra por separado es una partida. Un insumo es un elemento auxiliar que se gasta al trabajar, como un disco de corte o un electrodo. La cubicación sirve para pedir materiales, presupuestar, programar el trabajo y planificar el almacenamiento y el transporte, porque la masa de lo pedido define cómo se guarda y se traslada.",
        "Un error de cantidad detiene la obra por faltantes, o encarece el proyecto por sobrantes. Una planilla digital calcula lo que se digita, aunque esté mal; por eso se revisa con una idea aproximada del tamaño esperado, y una segunda persona la mira. El archivo incluye datos del cliente, que son confidenciales y no se comparten sin autorización. Quien trabaja mucho rato frente a una pantalla debe hacer pausas activas y cuidar su postura. Al pedir se suma una merma, la parte del material que se pierde o no se usa; para sumar una merma de 10 % se multiplica la cantidad por 110 y se divide entre 100.",
        f"Una bodega con materiales mal almacenados también es un riesgo: las pilas muy altas pueden caer. {EMER} {AVISO}",
    ],
    vocab=[("cubicar", "calcular las cantidades de materiales e insumos de un proyecto"), ("partida", "cada ítem que se cuenta y se cobra por separado"), ("insumo", "elemento auxiliar que se gasta al trabajar, como un electrodo o un disco de corte"), ("planilla digital", "programa que calcula con fórmulas los datos que se escriben"), ("confidencial", "que no se debe compartir sin autorización"), ("pausa activa", "descanso corto con movimiento durante el trabajo en pantalla"), ("merma", "parte del material que se pierde o no se usa y se suma al pedido como porcentaje")],
    worked=[
        ("Contar partidas", "Una cubicación de ejemplo tiene 8 pilares, 12 vigas y 5 planchas. ¿Cuántas piezas son en total?", ["Se suman las tres cantidades.", "8 más 12 más 5 son 25."], "25 piezas"),
        ("Orden de magnitud", "Un plano de ejemplo muestra 25 m de cañería y la planilla dice 250 m. ¿Es razonable?", ["250 es diez veces el valor del plano.", "Probablemente se digitó un cero de más: hay que revisar."], "No es razonable: hay que revisarlo"),
    ],
    mistakes=[("Pedir con el total de la planilla sin revisarlo.", "El programa calcula lo que se escribe, aunque esté mal.", "Revisa con una idea aproximada del tamaño y con una segunda mirada."),
              ("Enviar la planilla con los datos del cliente a quien solo necesita las cantidades.", "Los datos del cliente son confidenciales.", "Comparte solo lo necesario y con autorización.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué significa cubicar materiales?", "Calcular las cantidades de materiales e insumos que necesita un proyecto", "Pintar de colores cada elemento de un plano", "Elegir el proveedor más barato", "Cubicar es calcular cantidades a partir de planos; no es elegir proveedor."),
        ("abc", "En Montaje Industrial: ¿qué es un insumo?", "Un elemento auxiliar que se gasta al trabajar, como un electrodo o un disco de corte", "La pieza principal de la estructura", "El plano de la obra", "El insumo se consume en el trabajo, a diferencia de la pieza que queda en la obra."),
        ("abc", "En Montaje Industrial: ¿por qué la masa de lo pedido importa para la bodega y el transporte?", "Porque define cómo se almacena y se traslada con seguridad", "Porque cambia el color de los materiales", "Porque reduce el precio de las piezas", "La masa condiciona el almacenamiento y el transporte seguros."),
        ("=", "{F} ¿Cuántas piezas estructurales (pilares y vigas) suma la planilla?", "10+16", "Se suman los pilares y las vigas.", " piezas"),
        ("abc", "{F} ¿En qué unidad se expresa la cantidad de cañería de la planilla?", "En metros (m)", "En metros cuadrados (m²)", "En kilogramos por pieza", "La cañería es una longitud, por eso se mide en metros."),
        ("abc", "{F} Los datos de la persona dueña del proyecto en la planilla, ¿cómo se tratan?", "Como confidenciales: se comparten solo con autorización", "Se envían a cualquier grupo que los pida", "Se imprimen y se dejan en la bodega", "Los datos de personas son confidenciales."),
        ("=", "{F} Si se piden los 90 pernos más una merma de ejemplo del 10 %, ¿cuántos pernos se piden?", "90*110//100", "Se multiplica por 110 y se divide entre 100 para sumar el 10 %.", " pernos"),
        ("=", "{F} Si cada perno cuesta $350 (valor de ejemplo), ¿cuánto cuestan 99 pernos?", "99*350", "Se multiplican los pernos por el precio de cada uno.", " pesos"),
        ("abc", "{F} En un pedido se escribió por error 420 m de cañería en lugar de 42 m. ¿Qué corresponde?", "Revisarlo antes de enviar: es diez veces el valor de la planilla", "Enviarlo porque el programa lo calculó", "Enviarlo y avisar después", "Un valor diez veces mayor sugiere un cero de más."),
        ("abc", "{F} Un compañero dice: «como el programa lo calculó, se puede pedir sin revisar». ¿Qué respuesta es correcta?", "Es falso: el programa calcula lo que se le escribe y un dato mal digitado da un resultado malo", "Es cierto: los programas nunca se equivocan", "Es cierto si el archivo tiene respaldo", "Un error de digitación produce un resultado erróneo sin aviso."),
        ("abc", "{F} ¿Qué corresponde frente a los perfiles apilados muy altos de la bodega?", "Avisar al supervisor para que se almacenen según el plan de la bodega, y no apilar más", "Apilar más para ganar espacio", "Subirse a la pila para revisar", "Una pila muy alta puede caer y aplastar; se aclara con quien organiza la bodega."),
        ("=", "{F} Si cada pilar pesa 300 kg y cada viga 150 kg (valores de ejemplo), ¿cuántos kilogramos suman todos?", "10*300+16*150", "Se suman las masas de los pilares y de las vigas.", " kg"),
        ("abc", "En la oficina de un taller de montaje, una persona de ejemplo trabaja tres horas seguidas frente a la pantalla con la planilla. ¿Qué medida de cuidado corresponde?", "Hacer pausas activas y cuidar la postura", "Seguir sin descanso para terminar antes", "Acercarse más a la pantalla", "Las pausas y la buena postura previenen molestias por trabajo prolongado."),
    ],
    ctx=("abc", "Un proveedor de ejemplo te pide: «pásame la planilla completa con el nombre y el teléfono del dueño para cotizar». ¿Qué respondes?", "Que se enviarán solo las cantidades necesarias, sin datos personales, y con autorización", "Que sí, para que cotice rápido", "Que sí, pero sin el respaldo", "Para cotizar bastan las cantidades; los datos personales se protegen."),
    sc=[
        ("En Montaje Industrial: ¿qué es una partida?", "Un ítem que se cuenta y se cobra por separado", "La partida es la unidad básica de la cubicación."),
        ("¿Qué se hace con el total de una planilla antes de pedir?", "Se revisa con una idea aproximada y una segunda mirada", "El programa no detecta un dato mal digitado."),
        ("¿Cómo se tratan los datos del cliente?", "Como confidenciales, compartiéndolos solo con autorización", "Los datos personales no se difunden."),
    ],
    op=("Ficha de ejemplo: casa «Los Álamos»: 6 pilares, 10 vigas, 30 m de cañería y 60 pernos. La planilla incluye el nombre y el teléfono de la dueña. Escribe (a) cuántas piezas estructurales hay, (b) qué magnitud es la cañería, (c) cuántos pernos se piden con una merma de ejemplo del 10 %, (d) una regla para cuidar los datos de la dueña.",
        "(a) 6 + 10 = 16 piezas. (b) Una longitud, en metros. (c) 60 × 110 ÷ 100 = 66 pernos. (d) Compartir solo las cantidades necesarias, con autorización, sin su nombre ni teléfono.",
        ["suma las piezas", "identifica la magnitud", "calcula los pernos con merma", "propone una regla de confidencialidad"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal", "calcular la merma sobre otra cantidad", "no proteger los datos"],
        "Pregunta: «¿qué datos de la planilla son personales?». Si no responde, pídele que relea la regla de confidencialidad."),
    reinforce="Escribe tres partidas de ejemplo de un montaje y la unidad que corresponde a cada una (m, kg, unidades o litros).",
    extend="Explica con un ejemplo por qué un error de cantidad puede detener una obra o encarecerla.",
)

# ============================================================ OAE-10, clase 2
F = ("Ficha 2 (planilla de ejemplo, inventada). Perfil PE-100: masa de ejemplo de 15 kg por metro. Lista de piezas: 8 vigas de 6 m y 4 columnas de 4 m, todas de perfil PE-100. "
     "Precio de ejemplo del acero: $1.200 por kg. Merma de ejemplo: 5 %.")
build(
    O10, 2, F,
    use="Aprenderé el vocabulario de la cubicación, a calcular la masa de perfiles por metro, a agregar merma y a calcular el costo con precio unitario, y qué documentos y roles intervienen.",
    prior=["Sé qué es una partida.", "Sé multiplicar y sumar números enteros.", "Sé calcular un porcentaje simple."],
    explain=[
        "La cubicación se anota en una planilla con la partida, la unidad, la cantidad, el precio unitario y el subtotal. El precio unitario es el precio de una unidad, como un kilogramo o un metro; el subtotal es la cantidad por el precio unitario; y el presupuesto es la suma de los subtotales. Para un perfil lineal se calcula primero el largo total en metros y luego la masa, multiplicando los metros por la masa por metro. La lista de materiales es una tabla con los materiales, sus cantidades y sus unidades.",
        "La merma es la parte del material que se pierde o no se usa, por cortes y otras causas. Se agrega al pedido como un porcentaje: la cantidad por 100 más el porcentaje, dividido entre 100. Por ejemplo, un perfil de 10 kg por metro en 3 piezas de 5 m da 150 kg, y con una merma de 4 % se piden 156 kg. La orden de compra es el documento que pide el material al proveedor. Los roles son el cubicador, que calcula; el jefe de obra, que revisa; el comprador, que pide; el bodeguero, que recibe; y el ITO, que revisa que lo recibido cumpla las especificaciones.",
        f"Todos los precios, masas y mermas son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("precio unitario", "precio de una unidad de material o de trabajo, como un kg o un m"), ("subtotal", "cantidad multiplicada por el precio unitario"), ("presupuesto", "suma de los subtotales de todas las partidas"), ("lista de materiales", "tabla con los materiales, sus cantidades y sus unidades"), ("merma", "parte del material que se pierde o no se usa"), ("orden de compra", "documento que pide el material al proveedor")],
    worked=[
        ("Masa de un perfil", "Un perfil de ejemplo de 8 kg por metro se usa en 5 piezas de 3 m. ¿Cuántos kg son?", ["Metros: 5 por 3 son 15.", "Masa: 15 por 8 son 120 kg."], "120 kg"),
        ("Subtotal", "Se piden 40 unidades de una pieza que cuesta $500 cada una. ¿Cuál es el subtotal?", ["Se multiplica la cantidad por el precio unitario.", "40 por 500 son 20.000."], "20.000 pesos"),
    ],
    mistakes=[("Cubicar solo una parte de la lista y olvidar las otras piezas.", "Faltaría material y se detendría la obra.", "Cuenta todas las piezas de la lista antes de calcular."),
              ("Pedir el material exacto sin merma.", "Los cortes y las pérdidas dejan la cantidad corta.", "Agrega la merma del proyecto y registra el porcentaje usado.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es la merma de un material?", "La parte que se pierde o no se usa, por cortes u otras causas", "El precio de una unidad", "El peso del embalaje", "La merma es material perdido, no un precio ni un embalaje."),
        ("abc", "En Montaje Industrial: ¿qué es una lista de materiales?", "Una tabla con los materiales, sus cantidades y sus unidades", "Un dibujo a escala del terreno", "El permiso para pedir material", "La lista ordena materiales y cantidades; el dibujo y el permiso son otros documentos."),
        ("abc", "En Montaje Industrial: ¿qué es el precio unitario?", "El precio de una unidad de material o de trabajo, como un kg o un m", "El precio total de toda la obra", "El descuento del proveedor", "El unitario es el precio de una sola unidad."),
        ("=", "{F} ¿Cuántos metros de perfil suman las vigas y las columnas?", "8*6+4*4", "Se multiplican las piezas por su largo y se suman los metros.", " m"),
        ("=", "{F} ¿Cuántos kilogramos de perfil son, sin merma?", "(8*6+4*4)*15", "Se multiplican los metros totales por la masa por metro.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos se piden con la merma de 5 %?", "(8*6+4*4)*15*105//100", "Se suma el 5 % a la masa sin merma.", " kg"),
        ("=", "{F} ¿Cuánto cuesta el acero sin merma?", "(8*6+4*4)*15*1200", "Se multiplican los kilogramos sin merma por el precio de cada kilogramo.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta pedir el acero con la merma de 5 %?", "(8*6+4*4)*15*105//100*1200", "Se multiplican los kilogramos con merma por el precio de cada kilogramo.", " pesos"),
        ("abc", "{F} ¿Por qué se agrega la merma al pedido?", "Porque al cortar y manipular se pierde material y sin merma faltaría", "Porque el proveedor lo exige para subir el precio", "Porque el acero crece al cortarlo", "La merma cubre las pérdidas esperadas."),
        ("abc", "{F} Un compañero cubicó solo las vigas y olvidó las columnas. ¿Qué error y qué consecuencia hay?", "Pediría 720 kg y harían falta 960 kg, y la obra se detendría por faltante", "Pediría de más y sobrarían 240 kg", "No hay error porque las columnas son pocas", "Las vigas suman 720 kg; con las columnas son 960 kg."),
        ("abc", "{F} Un compañero calcula la masa multiplicando los 64 m de perfil por los $1.200 por kg. ¿Qué error comete?", "Mezcla metros con precio en vez de multiplicar por la masa por metro", "Debió dividir en vez de multiplicar", "No comete ningún error", "La masa sale de metros por kilogramos por metro; el precio se aplica después."),
        ("=", "{F} Si se agregan 2 vigas más de 6 m, ¿cuántos kilogramos de perfil, sin merma, suma el pedido?", "(8*6+4*4+2*6)*15", "Se suman los metros de todas las piezas y se multiplican por la masa por metro.", " kg"),
        ("abc", "¿Qué documento pide el material al proveedor?", "La orden de compra", "La lista de piezas", "La lámina de planos", "La orden de compra es el pedido formal al proveedor."),
    ],
    ctx=("abc", "El jefe de ejemplo te dice: «pide el acero exacto, sin merma, para bajar el costo». ¿Qué respondes?", "Que sin merma faltará material por los cortes y que se pide con la merma del proyecto", "Que sí, porque el costo es lo único importante", "Que sí, y se compra más si falta", "Sin merma la obra se detiene por faltante, y comprar de apuro cuesta más."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula la masa de un perfil?", "Metros totales por masa por metro", "La masa por metro está en la ficha del perfil."),
        ("¿Cómo se calcula un subtotal?", "Cantidad por precio unitario", "El subtotal es de una sola partida."),
        ("¿Cómo se suma una merma de 5 %?", "Se multiplica por 105 y se divide entre 100", "Se agrega el 5 % a la cantidad."),
    ],
    op=("Ficha de ejemplo: perfil de 12 kg por metro; 5 vigas de 8 m y 3 columnas de 5 m; precio de $1.100 por kg; merma de ejemplo de 10 %. Escribe (a) los metros totales, (b) los kg sin merma, (c) los kg con merma, (d) el costo del pedido con merma.",
        "(a) 5 × 8 + 3 × 5 = 40 + 15 = 55 m. (b) 55 × 12 = 660 kg. (c) 660 × 110 ÷ 100 = 726 kg. (d) 726 × 1.100 = 798.600 pesos.",
        ["calcula los metros", "calcula los kg sin merma", "agrega la merma", "calcula el costo"],
        ["hoja con los cuatro cálculos"],
        ["olvidar una de las piezas", "no agregar la merma", "multiplicar los metros por el precio"],
        "Pregunta: «¿por qué se multiplica por 110?». Si no responde, pídele que relea el párrafo de la merma."),
    reinforce="Calcula la masa de 6 piezas de 4 m de un perfil de 9 kg por metro.",
    extend="Explica con un ejemplo por qué una cubicación se revisa antes de convertirse en una orden de compra.",
)

# ============================================================ OAE-10, clase 3
F = ("Ficha 3 (planilla de cubicación de ejemplo, con un error). Partida, cantidad, unidad y precio unitario: perfiles, 840 kg, $1.250 por kg; planchas base, 6 unidades, $25.000 cada una; "
     "pernos, 60 unidades, $350 cada uno; pintura, 8 tarros, $20.000 cada uno. El programa muestra solo el total: $13.810.000.")
build(
    O10, 3, F,
    use="Aprenderé a revisar una planilla de cubicación, a recalcular subtotales y total, a detectar un error por orden de magnitud y a decidir cómo corregirlo y registrarlo.",
    prior=["Sé qué es un subtotal.", "Sé qué es un orden de magnitud.", "Sé multiplicar y sumar números enteros."],
    explain=[
        "Revisar una planilla es recalcular cada subtotal multiplicando la cantidad por el precio unitario, sumar los subtotales para obtener el total y compararlo con el que muestra el programa. Una diferencia exacta de diez, cien o mil veces suele indicar un cero de más o de menos. También se revisan las unidades y se comparan las cantidades con los planos y la lista de piezas.",
        "Cuando se encuentra un error, se corrige en la planilla, se deja constancia de qué se corrigió, por qué y quién lo hizo, y otra persona lo vuelve a revisar. Un pedido o un presupuesto no se envía con un total que se sabe equivocado, aunque haya apuro: el costo de un error de pedido es mayor que el de una hora de revisión.",
        f"Los datos son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("recalcular", "hacer de nuevo una cuenta para comprobar un resultado"), ("total", "suma de los subtotales de todas las partidas"), ("constancia de corrección", "anotación de qué se corrigió, por qué y quién lo hizo"), ("segunda revisión", "revisión hecha por otra persona después de corregir"), ("cero de más", "error de digitación que multiplica un valor por diez")],
    worked=[
        ("Recalcular un subtotal", "Una partida de ejemplo tiene 30 unidades a $2.000 y el programa muestra $6.000. ¿Cuál es el subtotal correcto?", ["Se multiplica la cantidad por el precio unitario.", "30 por 2.000 son 60.000."], "60.000 pesos"),
        ("Detectar el cero", "La suma real de unos subtotales de ejemplo es $450.000 y el programa muestra $4.500.000. ¿Cuántas veces mayor es?", ["Se divide 4.500.000 entre 450.000.", "Da 10."], "10 veces mayor"),
    ],
    mistakes=[("Enviar el presupuesto con un total que se sabe equivocado «para corregirlo después».", "El cliente puede aceptar o rechazar con una cifra falsa.", "Corrige y revisa antes de enviar, aunque haya apuro."),
              ("Corregir la planilla sin dejar constancia.", "No se sabe qué cambió ni quién lo hizo.", "Anota qué se corrigió, por qué y quién.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es un subtotal en una planilla de cubicación?", "El resultado de multiplicar cantidad por precio unitario en una partida", "La suma de todas las partidas", "La cantidad de partidas de la planilla", "El subtotal es de una sola partida; la suma de todas es el total."),
        ("abc", "En Montaje Industrial: ¿qué es revisar un resultado por orden de magnitud?", "Compararlo con una idea aproximada del tamaño esperado", "Repetir exactamente la misma cuenta", "Redondear el resultado a cero", "El orden de magnitud detecta resultados absurdos de un vistazo."),
        ("abc", "En Montaje Industrial: ¿quién debe corregir un error de la planilla?", "Quien la elaboró, con una segunda revisión, dejando constancia", "Cualquiera, sin avisar", "El proveedor", "La corrección se hace, se revisa y se registra."),
        ("=", "{F} ¿Cuál es el subtotal correcto de los perfiles?", "840*1250", "Se multiplica la cantidad de kg por el precio de cada kg.", " pesos"),
        ("=", "{F} ¿Cuál es el subtotal de las planchas base?", "6*25000", "Se multiplica la cantidad de planchas por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuál es el subtotal de la pintura?", "8*20000", "Se multiplica la cantidad de tarros por el precio de cada uno.", " pesos"),
        ("=", "{F} ¿Cuál es el total correcto de la planilla?", "840*1250+6*25000+60*350+8*20000", "Se suman los subtotales de las cuatro partidas.", " pesos"),
        ("=", "{F} ¿Cuántas veces mayor es el total que muestra el programa respecto del total real?", "13810000//1381000", "Se divide el total del programa entre el total real.", " veces"),
        ("abc", "{F} ¿Cuál es la causa más probable de la diferencia entre ambos totales?", "Un cero de más digitado en el total", "El precio de los pernos", "La cantidad de pintura", "La diferencia es exactamente diez veces, típica de un cero de más."),
        ("abc", "{F} Un compañero dice: «pidamos con el total del programa, seguro está bien». ¿Qué respuesta es correcta?", "No: el total no coincide con la suma de los subtotales y debe corregirse antes de pedir", "Sí, porque el programa nunca falla", "Sí, si el proveedor acepta", "Un total que no cuadra con sus subtotales indica un error."),
        ("abc", "{F} ¿Qué otra revisión conviene hacer a las cantidades de la planilla?", "Compararlas con los planos y la lista de piezas", "Cambiar los precios por otros", "Borrar las partidas más pequeñas", "Las cantidades deben calzar con los documentos del proyecto."),
        ("=", "{F} Si se enviara el pedido con el total erróneo, ¿cuántos pesos de más aparecerían respecto del total real?", "13810000-1381000", "Se resta el total real al total erróneo.", " pesos"),
        ("=", "{F} Si los pernos tuvieran una merma de 10 %, ¿cuántos pernos habría que pedir?", "60*110//100", "Se multiplica por 110 y se divide entre 100 para sumar el 10 %.", " pernos"),
    ],
    ctx=("abc", "El jefe de ejemplo quiere enviar hoy la planilla al cliente con el total de $13.810.000 y decir «después se corrige». ¿Qué respondes?", "Que no: el total real es $1.381.000, se corrige y se revisa antes de enviar", "Que sí, porque hay apuro", "Que sí, si se avisa por teléfono", "Enviar una cifra que se sabe errónea puede causar un perjuicio al cliente y a la empresa."),
    sc=[
        ("En Montaje Industrial: ¿cómo se detecta un cero de más?", "Comparando el total con una idea aproximada o con la suma de los subtotales", "Un valor diez veces mayor es una señal."),
        ("¿Qué se anota al corregir una planilla?", "Qué se corrigió, por qué y quién lo hizo", "La constancia permite revisar el cambio."),
        ("¿Quién revisa la corrección?", "Una segunda persona", "Una segunda mirada evita repetir el error."),
    ],
    op=("Planilla de ejemplo: perfiles, 500 kg a $1.300; planchas, 4 unidades a $30.000; pernos, 40 unidades a $300; el programa muestra un total de $7.820.000. Escribe (a) el subtotal de cada partida, (b) el total real, (c) cuántas veces mayor es el total del programa, (d) qué anotarías en la constancia de corrección.",
        "(a) Perfiles: 500 × 1.300 = 650.000; planchas: 4 × 30.000 = 120.000; pernos: 40 × 300 = 12.000. (b) 650.000 + 120.000 + 12.000 = 782.000 pesos. (c) 7.820.000 ÷ 782.000 = 10 veces. (d) Que el total tenía un cero de más, que se corrigió a 782.000 pesos, quién lo corrigió y la fecha, y que otra persona lo revisó.",
        ["calcula los tres subtotales", "calcula el total real", "detecta el factor de diez", "redacta una constancia"],
        ["hoja con los cálculos y la constancia"],
        ["sumar mal los subtotales", "no dejar constancia", "proponer enviar el total erróneo"],
        "Pregunta: «¿por qué conviene que otra persona revise?». Si no responde, pídele que relea el párrafo de segunda revisión."),
    reinforce="Recalcula en papel una planilla de tres partidas de ejemplo y compara el total con el del programa.",
    extend="Explica con un ejemplo por qué es más barato revisar una planilla que corregir un pedido equivocado.",
)

# ============================================================ OAE-10, clase 4
F = ("Ficha 4 (cubicación de una estructura de ejemplo, inventada). 12 pilares de 5 m y 20 vigas de 6 m, de un perfil de 18 kg por metro. Merma de ejemplo: 5 %. Precio de ejemplo del acero: $1.300 por kg. "
     "Montaje: cada pieza requiere 2 horas de una cuadrilla de 3 personas; costo de ejemplo de $9.000 por hora-persona. Se dispone de 2 cuadrillas que pueden trabajar en paralelo; la jornada es de 8 horas.")
build(
    O10, 4, F,
    use="Aprenderé a cubicar una estructura completa con material, merma, mano de obra y tiempo, a calcular horas-persona y plazo y a reconocer qué advertencias de seguridad tiene acelerar un programa.",
    prior=["Sé calcular masa de perfiles y agregar merma.", "Sé qué es una persona-día y un programa de obra.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Una cubicación completa suma tres partes: el material con su merma, la mano de obra y el tiempo. La mano de obra se calcula en horas-persona, que es el trabajo de una persona durante una hora: las horas de cada cuadrilla se multiplican por las personas de esa cuadrilla y por el costo de cada hora-persona. El costo total de una partida de montaje es el costo del material más el de la mano de obra, y puede incluir otros gastos como el transporte.",
        "El plazo se estima dividiendo las horas de cuadrilla entre el número de cuadrillas que trabajan en paralelo y luego entre las horas de la jornada para obtener los días. Un programa más corto no vale si pone a demasiadas personas y piezas en la misma zona: el prevencionista revisa que se respeten las reglas de seguridad antes de acelerar nada. En un diagrama de Gantt, las cuadrillas en paralelo se dibujan como barras al mismo tiempo.",
        f"Todo es un cálculo de papel con cifras de ejemplo; no autoriza a iniciar ningún trabajo. {EMER} {AVISO}",
    ],
    vocab=[("hora-persona", "trabajo de una persona durante una hora"), ("mano de obra", "trabajo de las personas que ejecutan una tarea"), ("cuadrilla", "grupo de trabajadores que ejecuta una tarea junta"), ("costo total de la partida", "costo del material más el de la mano de obra y otros gastos"), ("jornada", "horas de trabajo de un día")],
    worked=[
        ("Costo de mano de obra", "Una tarea de ejemplo toma 5 horas de una cuadrilla de 4 personas a $8.000 por hora-persona. ¿Cuánto cuesta?", ["Hora-personas: 5 por 4 son 20.", "20 por 8.000 son 160.000."], "160.000 pesos"),
        ("Plazo con cuadrillas", "Hay 36 horas de cuadrilla y trabajan 3 cuadrillas en paralelo con jornadas de 6 horas. ¿Cuántos días tarda?", ["Horas de calendario: 36 entre 3 son 12.", "Días: 12 entre 6 son 2."], "2 días"),
    ],
    mistakes=[("Calcular la mano de obra sin multiplicar por las personas de la cuadrilla.", "Se subestima el costo, porque cada persona cuesta.", "Multiplica horas por personas y por el costo de cada hora-persona."),
              ("Poner todas las cuadrillas en la misma zona para terminar antes.", "Más personas juntas aumentan el riesgo de atrapamiento y de caída de piezas.", "Revisa el programa con el prevencionista y respeta las reglas de seguridad.")],
    T=[
        ("abc", "En Montaje Industrial: ¿qué es una hora-persona?", "El trabajo de una persona durante una hora", "Una hora de descanso de la cuadrilla", "El precio de una herramienta por hora", "La hora-persona mide el trabajo humano en una hora."),
        ("abc", "En Montaje Industrial: ¿qué se suma para obtener el costo total de una partida de montaje?", "El costo del material y el de la mano de obra, más otros gastos", "Solo el costo del material", "Solo el costo de la mano de obra", "La partida incluye todo lo necesario para ejecutarla."),
        ("abc", "En Montaje Industrial: ¿por qué dos cuadrillas en paralelo reducen el plazo?", "Porque trabajan al mismo tiempo y se reparten las horas de cuadrilla", "Porque cada cuadrilla trabaja más horas por día", "Porque el trabajo total disminuye", "El trabajo total es el mismo, pero se reparte en el tiempo."),
        ("=", "{F} ¿Cuántos metros de perfil suman los pilares y las vigas?", "12*5+20*6", "Se multiplican las piezas por su largo y se suman los metros.", " m"),
        ("=", "{F} ¿Cuántos kilogramos de perfil son, sin merma?", "(12*5+20*6)*18", "Se multiplican los metros totales por la masa por metro.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos se piden con la merma de 5 %?", "(12*5+20*6)*18*105//100", "Se suma el 5 % a la masa sin merma.", " kg"),
        ("=", "{F} ¿Cuánto cuesta el acero pedido con merma, que son 3.402 kg?", "3402*1300", "Se multiplican los kilogramos por el precio de cada kilogramo.", " pesos"),
        ("=", "{F} ¿Cuántas horas de cuadrilla requieren las 32 piezas?", "(12+20)*2", "Se multiplican las piezas por las horas que requiere cada una.", " horas"),
        ("=", "{F} ¿Cuánto cuesta la mano de obra del montaje de todas las piezas?", "(12+20)*2*3*9000", "Se multiplican las horas de cuadrilla por las personas y por el costo de cada hora-persona.", " pesos"),
        ("=", "{F} Con las 2 cuadrillas en paralelo, ¿cuántas horas de calendario tarda el montaje?", "(12+20)*2//2", "Se dividen las horas de cuadrilla entre las dos cuadrillas.", " horas"),
        ("=", "{F} Si el montaje tarda 32 horas de calendario y la jornada es de 8 horas, ¿cuántos días son?", "32//8", "Se dividen las horas de calendario entre las horas de la jornada.", " días"),
        ("=", "{F} ¿Cuánto cuestan en total el acero con merma, de 3.402 kg, y la mano de obra del montaje?", "3402*1300+(12+20)*2*3*9000", "Se suman el costo del acero con merma y el de la mano de obra.", " pesos"),
        ("abc", "{F} Se propone poner 6 cuadrillas en paralelo en la misma zona para terminar en un día. ¿Qué advertencia corresponde?", "Más cuadrillas juntas en una zona aumentan el riesgo de atrapamiento y de caída de piezas; el prevencionista debe revisarlo", "Ninguna, más cuadrillas siempre es más seguro", "Que se trabaje más rápido", "El trabajo simultáneo cambia el riesgo y debe evaluarse antes de acelerar."),
    ],
    ctx=("abc", "El jefe de ejemplo te pide un cálculo rápido de costo y plazo y dice: «quita la merma del acero para que el presupuesto se vea más barato». ¿Qué respondes?", "Que la merma es una pérdida real del material y se mantiene en el presupuesto, informando su porcentaje", "Que sí, porque un presupuesto bajo gana más contratos", "Que sí, y después se pide el resto", "Quitar la merma deja el presupuesto corto y la obra con faltantes."),
    sc=[
        ("En Montaje Industrial: ¿cómo se calcula el costo de mano de obra?", "Horas por personas por el costo de cada hora-persona", "La mano de obra depende de horas, personas y costo."),
        ("¿Cómo se calcula el plazo con cuadrillas en paralelo?", "Horas de cuadrilla entre las cuadrillas y luego entre la jornada", "Se reparten las horas entre las cuadrillas."),
        ("¿Qué riesgo aumenta con más cuadrillas en la misma zona?", "El atrapamiento y la caída de piezas", "Hay más personas y movimiento en el mismo espacio."),
    ],
    op=("Ficha de ejemplo: 6 pilares de 4 m y 10 vigas de 5 m, de un perfil de 20 kg por metro; merma de ejemplo de 10 %; precio de $1.000 por kg. Cada pieza requiere 3 horas de una cuadrilla de 2 personas, a $8.000 por hora-persona; trabajan 2 cuadrillas en paralelo y la jornada es de 8 horas. Escribe (a) los kg con merma, (b) el costo del acero, (c) el costo de la mano de obra, (d) los días de calendario.",
        "(a) Metros: 6 × 4 + 10 × 5 = 74; kg: 74 × 20 = 1.480; con merma: 1.480 × 110 ÷ 100 = 1.628 kg. (b) 1.628 × 1.000 = 1.628.000 pesos. (c) Piezas: 16; horas de cuadrilla: 16 × 3 = 48; costo: 48 × 2 × 8.000 = 768.000 pesos. (d) 48 ÷ 2 = 24 horas de calendario; 24 ÷ 8 = 3 días.",
        ["calcula los kg con merma", "calcula el costo del acero", "calcula la mano de obra", "calcula los días de calendario"],
        ["hoja con los cuatro cálculos"],
        ["olvidar la merma", "no multiplicar por las personas", "no repartir las horas entre las cuadrillas"],
        "Pregunta: «¿cuántas hora-persona tiene una cuadrilla de 2 en 3 horas?». Si no responde, pídele que relea el ejemplo de mano de obra."),
    reinforce="Calcula el costo de mano de obra de una tarea de 4 horas de una cuadrilla de 3 personas a $7.000 por hora-persona.",
    extend="Explica con un ejemplo por qué terminar antes con más cuadrillas puede requerir una revisión de seguridad.",
)

# FIN
