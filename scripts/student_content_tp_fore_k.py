"""Forestal TP 3.º y 4.º medio: OAE-10 (protección ambiental y desarrollo sustentable en la producción y preservación forestal). Todo en papel, con datos de ejemplo."""
from __future__ import annotations

from tp_fore_common import AVISO, EMER, build

O10 = "TP-FORE-3y4-OAE-10"

# ============================================================ OAE-10, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Predio «Demo Verde»: 100 ha, de las cuales 60 ha son plantación de «especie A» para producción, 30 ha son bosque nativo con propósito de preservación y 10 ha son una franja que protege un curso de agua. "
     "Impactos anotados de las actividades: erosión del suelo, residuos, derrame de combustible, ruido que afecta a la fauna y el hallazgo de un lugar con restos antiguos, que podría ser de valor cultural. "
     "Una bodega de ejemplo genera 36 kg de residuos al mes, de los cuales el 25 % es reciclable.")
build(
    O10, 1, F,
    use="Aprenderé qué es el desarrollo sustentable, qué impactos ambientales puede tener una actividad forestal, cómo se ordenan las medidas para cuidarlos y qué hacer ante un derrame o un hallazgo cultural.",
    prior=["Sé qué es un plan de manejo y la jerarquía de controles.", "Sé calcular porcentajes simples.", "Sé qué es bosque nativo y plantación."],
    explain=[
        "El desarrollo sustentable busca satisfacer las necesidades de hoy sin comprometer las de las generaciones futuras, y equilibra tres dimensiones: la ambiental, la social y la económica. Una actividad forestal puede tener impactos ambientales, es decir, cambios en el ambiente causados por ella, como la erosión del suelo, la generación de residuos, los derrames, el ruido que afecta a la fauna y la alteración de sitios de valor cultural. La biodiversidad es la variedad de seres vivos y ecosistemas de un lugar, y su cuidado es parte del manejo.",
        "Para cuidar el ambiente se aplica una jerarquía de mitigación, que ordena las medidas de la más a la menos preferible: evitar el impacto, reducirlo, repararlo y, en último lugar, compensarlo. Siempre es mejor que el daño no ocurra. El patrimonio cultural también se protege: si aparece un lugar con restos antiguos, no se toca ni se mueve nada, y un adulto responsable informa a la autoridad competente según la norma vigente.",
        f"Un derrame de combustible puede ser peligroso para las personas y el ambiente: se actúa con personal capacitado. {EMER} {AVISO}",
    ],
    vocab=[("desarrollo sustentable", "forma de satisfacer las necesidades de hoy sin comprometer las de las generaciones futuras"), ("impacto ambiental", "cambio en el ambiente causado por una actividad"), ("biodiversidad", "variedad de seres vivos y ecosistemas de un lugar"), ("jerarquía de mitigación", "orden de las medidas ambientales: evitar, reducir, reparar y compensar"), ("patrimonio cultural", "lugares y objetos de valor histórico o cultural"), ("erosión", "desgaste del suelo por agua o viento")],
    worked=[
        ("Identificar un impacto", "Una actividad de ejemplo deja el suelo sin vegetación en una ladera y la lluvia arrastra tierra al río. ¿Qué impacto ocurre?", ["El suelo se desgasta por la lluvia.", "Eso es erosión del suelo."], "Erosión del suelo"),
        ("Calcular un porcentaje", "Un predio de ejemplo tiene 200 ha y destina 50 ha a protección. ¿Qué porcentaje es?", ["50 ÷ 200 son 25 de cada 100.", "El porcentaje es 25 %."], "25 %"),
    ],
    mistakes=[("Creer que una empresa puede prometer «cero impacto».", "Toda actividad produce algún impacto; lo que se hace es evitarlo, reducirlo, repararlo y compensarlo.", "Habla de medidas de mitigación y no de impacto cero."),
              ("Creer que tomar un objeto antiguo hallado en un predio ayuda a protegerlo.", "Moverlo destruye información y está regulado por la norma vigente.", "No se toca; un adulto responsable informa a la autoridad competente.")],
    T=[
        ("abc", "En Forestal: ¿qué es el desarrollo sustentable?", "Satisfacer las necesidades de hoy sin comprometer las de las generaciones futuras, equilibrando lo ambiental, lo social y lo económico", "Obtener la mayor utilidad posible a corto plazo", "Dejar de producir para no generar ningún impacto", "El desarrollo sustentable equilibra tres dimensiones y mira el largo plazo."),
        ("abc", "En Forestal: ¿qué es la biodiversidad de un lugar?", "La variedad de seres vivos y ecosistemas que hay en él", "La cantidad total de madera que produce", "El número de árboles de una sola especie", "La biodiversidad es variedad, no una cantidad de madera ni de una sola especie."),
        ("abc", "En Forestal: ¿qué es un impacto ambiental?", "Un cambio en el ambiente causado por una actividad", "Un reporte de ventas de la empresa", "Una tormenta que cae sobre el predio", "El impacto ambiental es consecuencia de una actividad humana."),
        ("=", "{F} ¿Qué porcentaje del predio se destina a preservación o protección, sumando el bosque nativo y la franja del curso de agua?", "(30+10)*100//100", "Se suman las hectáreas de preservación y protección y se calcula su porcentaje del total.", " %"),
        ("=", "{F} ¿Cuántas hectáreas más tiene la plantación que el bosque nativo?", "60-30", "Se restan las hectáreas del bosque nativo a las de la plantación.", " ha"),
        ("abc", "{F} ¿Qué corresponde ante un derrame de combustible de gran tamaño?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a tapar el derrame con tierra", "Lavar con agua el derrame hacia el curso de agua", "Un derrame grande puede ser peligroso; lo manejan personas capacitadas."),
        ("abc", "{F} ¿Qué corresponde con el lugar de restos antiguos hallado en el predio?", "No tocar ni mover nada y avisar a un adulto responsable para que informe a la autoridad competente", "Recoger los objetos y guardarlos", "Taparlo con tierra para que nadie lo vea", "Un hallazgo cultural se protege y se informa; moverlo o taparlo lo daña."),
        ("abc", "En Forestal: ¿cuál es el orden de preferencia de la jerarquía de mitigación?", "Evitar, reducir, reparar y compensar", "Compensar, reparar, reducir y evitar", "Reparar, evitar, compensar y reducir", "Lo mejor es que el impacto no ocurra, y la compensación es el último recurso."),
        ("=", "{F} ¿Cuántos kg de los residuos de la bodega son reciclables cada mes?", "36*25//100", "Se calcula el 25 % de los 36 kg de residuos.", " kg"),
        ("abc", "{F} ¿Por qué se protege la franja que rodea el curso de agua?", "Porque protege el agua y el suelo, y es hábitat de muchos seres vivos", "Porque en esa franja no hay vegetación", "Porque nadie puede entrar nunca a esa franja", "La franja protege el agua, el suelo y la biodiversidad del lugar."),
        ("abc", "{F} Un compañero dice que la plantación es lo único importante porque da ingresos. ¿Qué respuesta es correcta?", "No: la sustentabilidad exige equilibrar lo ambiental, lo social y lo económico", "Sí, porque lo económico es lo único que se mide", "Sí, si el predio es privado", "Descuidar lo ambiental o lo social compromete el futuro del propio negocio."),
        ("=", "{F} Si la bodega mejorara y reciclara 18 kg al mes, ¿qué porcentaje de sus 36 kg de residuos sería reciclable?", "18*100//36", "Se divide lo reciclado entre el total y se multiplica por 100.", " %"),
        ("abc", "En Forestal: una empresa asegura que su actividad produce «cero impacto». ¿Qué respuesta es correcta?", "Es poco realista: toda actividad tiene impactos, y se busca evitarlos, reducirlos, repararlos y compensarlos", "Es realista si usa equipos nuevos", "Es realista si todo el personal usa EPP", "Siempre hay algún impacto; lo que se asegura son medidas de mitigación."),
    ],
    ctx=("abc", "Visitando un predio, encuentras unos objetos antiguos en el suelo y un amigo propone llevarlos a su casa «de recuerdo». ¿Qué respondes?", "Que no, porque no se tocan ni se mueven, y que avisas a un adulto responsable para que informe a la autoridad competente", "Que sí, si son pequeños", "Que sí, si nadie los reclama", "Un hallazgo cultural se protege; moverlo destruye información y está regulado."),
    sc=[
        ("En Forestal: ¿qué es la erosión?", "El desgaste del suelo por agua o viento", "La erosión se produce cuando el suelo queda sin protección."),
        ("¿Cuál es la medida más preferible de la jerarquía de mitigación?", "Evitar el impacto", "Un impacto evitado no necesita reparación ni compensación."),
        ("¿Qué haces si encuentras restos antiguos en un predio?", "No tocar nada y avisar a un adulto responsable", "El adulto responsable informa a la autoridad competente."),
    ],
    op=("Ficha de ejemplo: predio «Muestra Verde», 200 ha: 120 ha de plantación, 60 ha de bosque nativo con propósito de preservación y 20 ha de franja que protege un curso de agua. Impactos anotados: erosión y residuos. Una bodega genera 48 kg de residuos al mes, y el 25 % es reciclable. Escribe (a) qué porcentaje del predio es preservación o protección, (b) cuántos kg reciclables genera la bodega al mes, (c) una medida para evitar la erosión, (d) qué haces si ves un derrame de combustible.",
        "(a) (60 + 20) ÷ 200 = 40 %. (b) 48 × 25 ÷ 100 = 12 kg. (c) Mantener la cobertura vegetal del suelo y no intervenir la franja protegida. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["calcula el porcentaje de preservación", "calcula los kg reciclables", "propone una medida que evita", "indica qué hacer ante un derrame"],
        ["hoja con las cuatro respuestas"],
        ["no sumar bosque nativo y franja", "proponer reparar en vez de evitar", "acercarse al derrame"],
        "Pregunta: «¿qué es mejor: evitar un impacto o repararlo después?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres impactos ambientales posibles de una actividad forestal y una medida para cada uno.",
    extend="Explica con un ejemplo por qué evitar un impacto es preferible a repararlo.",
)

# ============================================================ OAE-10, clase 2
F = ("Ficha 2 (matriz de impactos de ejemplo, inventada). Predio «Demo Verde». Fila 1: impacto, erosión del suelo; medida, mantener la cobertura vegetal y no intervenir la franja protegida; responsable, jefe de predio. "
     "Fila 2: impacto, residuos; medida, separarlos y entregar los peligrosos a un gestor autorizado; responsable, encargado de residuos. Fila 3: impacto, ruido que afecta a la fauna; medida, horarios de trabajo que eviten las horas más sensibles; responsable, jefe de predio. "
     "Fila 4: impacto, hallazgo cultural; medida, no intervenir y avisar para informar a la autoridad competente; responsable, jefe de predio. Fila 5: impacto, derrames de combustible; medida y responsable, sin completar. "
     "Residuos mensuales de ejemplo: 108 kg no peligrosos y 12 kg peligrosos.")
build(
    O10, 2, F,
    use="Aprenderé los documentos y conceptos de la gestión ambiental de un predio: matriz de impactos, plan de manejo ambiental, especies nativas y protegidas, residuos peligrosos y roles.",
    prior=["Sé qué es un impacto ambiental y la jerarquía de mitigación.", "Sé calcular porcentajes simples.", "Sé qué es un plan de manejo."],
    explain=[
        "Una matriz de impactos es una tabla que lista los impactos de las actividades y, para cada uno, la medida y el responsable. Es parte del plan de manejo ambiental, el documento que dice cómo se cuidará el ambiente del predio. Una especie nativa es una especie originaria del país; una especie exótica es una traída de otro lugar. Una especie protegida es una que la norma cuida de manera especial: si se observa una en el predio, no se perturba y un adulto responsable informa a quien corresponde.",
        "Los residuos se separan en peligrosos y no peligrosos. Un residuo peligroso puede dañar a las personas o al ambiente, como un aceite usado o un envase de producto sanitario, y se entrega a un gestor autorizado. Los otros residuos se manejan según el plan. Cada rol cumple su función: el profesional ambiental diseña las medidas, el jefe de predio las hace cumplir, el encargado de residuos los gestiona y la autoridad ambiental fiscaliza.",
        f"Estos documentos se leen aquí en papel. {EMER} {AVISO}",
    ],
    vocab=[("matriz de impactos", "tabla con los impactos de las actividades, su medida y su responsable"), ("plan de manejo ambiental", "documento que dice cómo se cuidará el ambiente del predio"), ("especie nativa", "especie originaria del país"), ("especie exótica", "especie traída de otro lugar"), ("especie protegida", "especie que la norma cuida de manera especial"), ("residuo peligroso", "residuo que puede dañar a las personas o al ambiente y exige un gestor autorizado")],
    worked=[
        ("Leer una matriz", "Una fila de ejemplo dice: impacto, polvo en el camino; medida, humedecer el camino; responsable, jefe de predio. ¿Quién es el responsable?", ["El responsable aparece en su propia columna.", "Es el jefe de predio."], "El jefe de predio"),
        ("Residuos peligrosos", "Un predio de ejemplo genera 90 kg de residuos no peligrosos y 10 kg de peligrosos por mes. ¿Qué porcentaje es peligroso?", ["El total es 100 kg.", "10 ÷ 100 = 10 %."], "10 %"),
    ],
    mistakes=[("Mezclar los residuos peligrosos con los demás para ahorrar espacio.", "Los residuos peligrosos exigen manejo especial y un gestor autorizado.", "Sepáralos y entrégalos al gestor autorizado."),
              ("Dejar sin completar la medida y el responsable de un impacto.", "Sin medida ni responsable nadie hace nada.", "Completa cada fila de la matriz.")],
    T=[
        ("abc", "En Forestal: ¿qué es una matriz de impactos?", "Una tabla que lista los impactos de las actividades, con su medida y su responsable", "Un mapa que muestra solo los caminos del predio", "Una lista de precios de los productos forestales", "La matriz organiza impactos, medidas y responsables."),
        ("abc", "En Forestal: ¿qué es una especie nativa?", "Una especie originaria del país", "Una especie traída de otro lugar", "Una especie que solo vive en viveros", "La especie nativa es originaria; la traída de otro lugar es exótica."),
        ("abc", "En Forestal: ¿qué es un residuo peligroso?", "Un residuo que puede dañar a las personas o al ambiente y exige un gestor autorizado", "Cualquier residuo que huele mal", "Cualquier residuo de origen vegetal", "Lo que define a un residuo peligroso es su capacidad de dañar, no su olor ni su origen."),
        ("=", "{F} ¿Qué porcentaje de las filas de la matriz está completo?", "4*100//5", "Se divide las filas completas entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje de los residuos mensuales es peligroso?", "12*100//(108+12)", "Se divide los kg peligrosos entre el total de kg y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos kg de residuos peligrosos se generan en 6 meses?", "12*6", "Se multiplican los kg mensuales por los meses.", " kg"),
        ("abc", "{F} ¿Quién es el responsable del impacto «erosión del suelo» según la matriz?", "El jefe de predio", "El encargado de residuos", "La autoridad ambiental", "La matriz asigna la erosión al jefe de predio."),
        ("abc", "{F} ¿Qué corresponde con la fila 5, que no tiene medida ni responsable?", "Completarla con la medida y el responsable que fije la jefatura", "Eliminarla de la matriz", "Dejarla en blanco hasta que ocurra un derrame", "Cada impacto necesita medida y responsable antes de que ocurra."),
        ("abc", "{F} ¿Qué medida de la matriz corresponde al hallazgo cultural?", "No intervenir y avisar para informar a la autoridad competente", "Recoger los objetos para guardarlos", "Cubrir el lugar para ocultarlo", "El patrimonio cultural se protege sin tocarlo."),
        ("abc", "En Forestal: ¿por qué se separan los residuos peligrosos de los demás?", "Para evitar daños y entregarlos a un gestor autorizado", "Para que ocupen menos espacio en la bodega", "Para venderlos al mismo precio que los demás", "El manejo especial protege a las personas y al ambiente."),
        ("abc", "{F} Un compañero dice que el ruido no es un impacto porque «no deja huella». ¿Qué respuesta es correcta?", "Es falso: el ruido afecta a la fauna y a las personas, y por eso se mide y se controla", "Es cierto, porque el ruido desaparece al terminar", "Es cierto, porque la matriz solo considera el suelo", "Un impacto no necesita dejar una marca visible para ser un cambio en el ambiente."),
        ("=", "{F} Si el gestor cobra $1.500 por cada kg de residuo peligroso (valor de ejemplo), ¿cuánto cuesta entregar los residuos peligrosos de 6 meses?", "12*6*1500", "Se multiplican los kg de 6 meses por el valor de cada kg.", " pesos"),
        ("abc", "{F} Durante una visita se observa en el predio una especie protegida. ¿Qué corresponde?", "No perturbarla y avisar a un adulto responsable para que informe a quien corresponde", "Capturarla para estudiarla en la oficina", "Ignorarla, porque no es parte de la matriz", "Una especie protegida no se perturba ni se captura; se informa."),
    ],
    ctx=("abc", "Un proveedor propone botar los residuos de la obra en una quebrada «que nadie usa», para ahorrar el costo del gestor. ¿Qué respondes?", "Que no, porque los residuos se entregan según el plan y la norma, y que lo consultarás con un adulto responsable", "Que sí, si es solo una vez", "Que sí, si nadie ve", "Botar residuos en una quebrada daña el ambiente y no cumple la norma."),
    sc=[
        ("En Forestal: ¿qué contiene cada fila de una matriz de impactos?", "El impacto, su medida y su responsable", "La matriz organiza quién hace qué frente a cada impacto."),
        ("¿Qué es una especie exótica?", "Una especie traída de otro lugar", "Se distingue de la nativa por su origen."),
        ("¿Dónde se entregan los residuos peligrosos?", "A un gestor autorizado", "Estos residuos exigen un manejo especial y un gestor autorizado."),
    ],
    op=("Ficha de ejemplo: matriz de impactos de un predio con 4 filas. Fila 1: erosión, medida y responsable completos. Fila 2: residuos, medida y responsable completos. Fila 3: ruido, medida y responsable completos. Fila 4: derrame de combustible, sin medida ni responsable. Residuos mensuales de ejemplo: 95 kg no peligrosos y 5 kg peligrosos. Escribe (a) el porcentaje de filas completas, (b) el porcentaje de residuos peligrosos, (c) qué hacer con la fila 4, (d) a dónde se entregan los residuos peligrosos.",
        "(a) 3 ÷ 4 = 75 %. (b) 5 ÷ 100 = 5 %. (c) Completarla con la medida y el responsable que fije la jefatura. (d) A un gestor autorizado.",
        ["calcula el porcentaje de filas completas", "calcula el porcentaje peligroso", "completa la fila faltante", "nombra el destino de los residuos peligrosos"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el total al calcular el porcentaje", "dejar sin responsable", "mezclar los residuos peligrosos"],
        "Pregunta: «¿qué se necesita para que una medida se cumpla?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una fila de matriz de impactos con impacto, medida y responsable.",
    extend="Explica con un ejemplo por qué una especie protegida no se perturba ni se captura aunque se quiera estudiar.",
)

# ============================================================ OAE-10, clase 3
F = ("Ficha 3 (registro ambiental de ejemplo, inventado). Predio «Demo Verde», primer trimestre. Residuos por mes: mes 1, 120 kg en total, 36 kg reciclados; mes 2, 100 kg en total, 44 kg reciclados; mes 3, 80 kg en total, 40 kg reciclados. "
     "Objetivo ambiental de ejemplo: reciclar al menos el 40 % de los residuos. Franja de protección de un curso de agua: ancho medido de 18 m, y el plan de ejemplo exige al menos 24 m (valor de ejemplo; el real lo fija la norma vigente).")
build(
    O10, 3, F,
    use="Aprenderé a analizar un registro ambiental: calcular porcentajes mensuales y trimestrales, compararlos con un objetivo, revisar una franja de protección y proponer acciones sin ocultar incumplimientos.",
    prior=["Sé calcular porcentajes simples.", "Sé qué es un objetivo y un indicador.", "Sé qué es una franja de protección."],
    explain=[
        "Un objetivo ambiental es una meta medible, por ejemplo reciclar un porcentaje de los residuos. Para analizar su cumplimiento se calcula el indicador cada mes y para todo el periodo, y se compara con el objetivo. Un periodo puede cumplir aunque alguno de sus meses no lo haga, y por eso se revisa cada mes. Reciclar es transformar residuos en materia prima para fabricar nuevos productos. Los residuos que no se reciclan se manejan según el plan y la norma.",
        "Una franja ribereña es una franja de terreno junto a un curso de agua que se protege para cuidar el agua, el suelo y la fauna. Su ancho mínimo lo fija la norma vigente y el plan; aquí es un valor de ejemplo. Cuando una medición no cumple el mínimo, se informa la diferencia y se corrige según el plan; no se anota un valor falso para «cumplir». Los registros se conservan con su fecha.",
        f"Las mediciones reales las hace personal capacitado. {EMER} {AVISO}",
    ],
    vocab=[("objetivo ambiental", "meta medible de cuidado del ambiente"), ("reciclar", "transformar residuos en materia prima para nuevos productos"), ("franja ribereña", "franja de terreno junto a un curso de agua que se protege"), ("indicador mensual", "valor calculado cada mes para comparar con un objetivo"), ("incumplimiento", "resultado que no alcanza lo exigido")],
    worked=[
        ("Porcentaje reciclado", "Un mes de ejemplo genera 200 kg de residuos y recicla 50 kg. ¿Qué porcentaje reciclado es?", ["50 ÷ 200 son 25 de cada 100.", "El porcentaje es 25 %."], "25 %"),
        ("Comparar con el objetivo", "El objetivo de ejemplo es 30 % y un mes llegó a 28 %. ¿Cumple?", ["28 es menor que 30.", "No llega al objetivo."], "No cumple"),
    ],
    mistakes=[("Concluir que todos los meses cumplen porque el trimestre cumple.", "Un mes puede estar bajo el objetivo aunque el total del periodo lo cumpla.", "Revisa cada mes y también el periodo."),
              ("Anotar un valor mayor que el medido para cumplir el mínimo de la franja.", "Un dato falso oculta un incumplimiento real.", "Anota el valor medido, informa la diferencia y corrige según el plan.")],
    T=[
        ("abc", "En Forestal: ¿qué significa reciclar un residuo?", "Transformarlo en materia prima para fabricar nuevos productos", "Guardarlo en la bodega por un tiempo", "Enterrarlo en un terreno del predio", "Reciclar es reutilizar el material como materia prima; guardar o enterrar no es reciclar."),
        ("abc", "En Forestal: ¿qué es una franja ribereña?", "Una franja de terreno junto a un curso de agua que se protege", "Una franja de caminos para los camiones", "Una parcela donde se cultiva", "La franja ribereña cuida el agua, el suelo y la fauna."),
        ("abc", "En Forestal: ¿qué es un objetivo ambiental?", "Una meta medible de cuidado del ambiente", "Una opinión del jefe sobre el predio", "Una lista de las herramientas del taller", "Un objetivo ambiental se mide y se compara con un resultado."),
        ("=", "{F} ¿Qué porcentaje de los residuos se recicló en el mes 1?", "36*100//120", "Se divide lo reciclado entre el total del mes y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje de los residuos se recicló en el mes 2?", "44*100//100", "Se divide lo reciclado entre el total del mes y se multiplica por 100.", " %"),
        ("=", "{F} ¿Qué porcentaje de los residuos se recicló en el mes 3?", "40*100//80", "Se divide lo reciclado entre el total del mes y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué meses cumplen el objetivo de reciclar al menos el 40 %?", "Los meses 2 y 3", "Los meses 1 y 2", "Solo el mes 3", "El mes 1 llegó a 30 %; el mes 2 a 44 % y el mes 3 a 50 %."),
        ("=", "{F} ¿Cuántos kg de residuos se generaron en el trimestre?", "120+100+80", "Se suman los residuos de los tres meses.", " kg"),
        ("abc", "{F} ¿Cumple el trimestre el objetivo de reciclar al menos el 40 %?", "Sí, porque se reciclaron 120 de 300 kg, que es justo el 40 %", "No, porque el mes 1 estuvo bajo el objetivo", "No se puede saber con esos datos", "El total reciclado es 120 kg de 300 kg, es decir, 40 %, que alcanza el mínimo."),
        ("abc", "{F} El ancho medido de la franja es 18 m y el plan de ejemplo exige al menos 24 m. ¿Qué corresponde?", "Anotar el valor medido, informar la diferencia y corregir según el plan", "Anotar 24 m para cumplir", "Ignorar la diferencia porque es pequeña", "Un incumplimiento se informa y se corrige; anotar un valor falso lo oculta."),
        ("=", "{F} ¿Cuántos metros le faltan a la franja para cumplir el ancho mínimo de ejemplo?", "24-18", "Se resta el ancho medido al ancho mínimo exigido.", " m"),
        ("=", "{F} Para llegar al 50 % de reciclaje en el trimestre, ¿cuántos kg más habría que reciclar?", "300*50//100-120", "Se calcula el 50 % de los residuos del trimestre y se resta lo ya reciclado.", " kg"),
        ("abc", "{F} Como el trimestre cumple, un compañero concluye que todos los meses cumplen. ¿Qué respuesta es correcta?", "Es falso: el mes 1 quedó bajo el objetivo, así que conviene revisar cada mes", "Es cierto, porque el total manda", "Es cierto, si se promedia con el mes 2", "Un periodo puede cumplir aunque un mes no lo haga, y ese mes también se analiza."),
    ],
    ctx=("abc", "Un compañero quiere llevar los residuos no reciclables a un sitio cercano para no pagar al gestor. ¿Qué respondes?", "Que no, porque los residuos se manejan según el plan y la norma, y que lo consultarás con un adulto responsable", "Que sí, si es un terreno sin dueño", "Que sí, si lo hace de noche", "Botar residuos en cualquier lugar daña el ambiente y no cumple la norma."),
    sc=[
        ("En Forestal: ¿cómo se calcula el porcentaje reciclado?", "Lo reciclado dividido por el total, por 100", "Relaciona lo reciclado con lo generado."),
        ("¿Un periodo que cumple significa que todos los meses cumplen?", "No, se revisa cada mes", "Un mes puede estar bajo el objetivo."),
        ("¿Qué se hace si la franja mide menos que el mínimo?", "Se anota el valor medido, se informa y se corrige", "No se anota un valor falso."),
    ],
    op=("Ficha de ejemplo: residuos de un predio en dos meses. Mes 1: 150 kg en total y 60 kg reciclados. Mes 2: 50 kg en total y 30 kg reciclados. Objetivo de ejemplo: reciclar al menos el 50 %. Franja de protección: ancho medido de 17 m, y el plan de ejemplo exige al menos 22 m. Escribe (a) el porcentaje reciclado de cada mes, (b) qué mes cumple, (c) el porcentaje de los dos meses juntos, (d) qué haces con la franja.",
        "(a) Mes 1: 60 ÷ 150 = 40 %; mes 2: 30 ÷ 50 = 60 %. (b) Solo el mes 2. (c) 90 ÷ 200 = 45 %, que no cumple el 50 %. (d) Anotar 17 m, informar que faltan 5 m y corregir según el plan.",
        ["calcula cada porcentaje", "compara con el objetivo", "calcula el porcentaje del periodo", "propone qué hacer con la franja"],
        ["hoja con las cuatro respuestas"],
        ["promediar los porcentajes en vez de sumar los kg", "anotar un valor falso de la franja", "ignorar el mes que no cumple"],
        "Pregunta: «¿cómo calculas el porcentaje de los dos meses juntos?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un mes con kg de residuos y kg reciclados y calcula el porcentaje.",
    extend="Explica con un ejemplo por qué conviene revisar cada mes y también el periodo completo.",
)

# ============================================================ OAE-10, clase 4
F = ("Ficha 4 (alternativas de ejemplo, inventadas; los costos y las distancias son de ejemplo). Se debe construir un camino de acceso a un rodal. "
     "Alternativa A: trazado de 2 km que cruza la franja de protección de un curso de agua; costo de construcción $10.000.000; afecta 2 ha de la franja. "
     "Alternativa B: trazado de 3 km que evita la franja; costo de construcción $12.500.000; no afecta la franja. "
     "Si se elige A, el plan exige restaurar 3 ha por cada hectárea afectada, y restaurar una hectárea cuesta $1.000.000.")
build(
    O10, 4, F,
    use="Aprenderé a aplicar la jerarquía de mitigación con datos: comparar alternativas por costo total y por impacto, y a preferir evitar un daño antes que repararlo o compensarlo.",
    prior=["Sé qué es la jerarquía de mitigación.", "Sé calcular costos y porcentajes simples.", "Sé qué es una franja de protección."],
    explain=[
        "La jerarquía de mitigación ordena las medidas de la más a la menos preferible. Evitar es diseñar la actividad para que el impacto no ocurra, por ejemplo cambiar el trazado de un camino para no cruzar una franja protegida. Reducir es disminuir el impacto que no se pudo evitar. Restaurar es reparar el daño en el mismo lugar. Compensar es hacer una acción en otro lugar para equilibrar un impacto que no se pudo evitar ni reparar del todo.",
        "Para decidir, se compara el costo total de cada alternativa, que incluye la construcción y las medidas de restauración o compensación, y también el impacto ambiental y social. Evitar suele ser más barato que reparar, y hay daños que no se pueden reparar del todo. Aunque una alternativa parezca más barata, si afecta una zona que el plan protege, no es aceptable sin cumplir la norma. Los datos de esta clase son de ejemplo.",
        f"La decisión final la toma el profesional responsable con la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("evitar", "diseñar la actividad para que el impacto no ocurra"), ("reducir", "disminuir el impacto que no se pudo evitar"), ("restaurar", "reparar el daño en el mismo lugar para recuperar sus condiciones"), ("compensar", "hacer una acción en otro lugar para equilibrar un impacto que no se pudo evitar ni reparar"), ("costo total", "construcción más las medidas de restauración o compensación")],
    worked=[
        ("Costo de restaurar", "Una alternativa de ejemplo afecta 4 ha y el plan exige restaurar 2 ha por cada hectárea afectada, a $500.000 la hectárea. ¿Cuánto cuesta restaurar?", ["Se restauran 4 × 2 = 8 ha.", "8 × 500.000 = 4.000.000."], "$4.000.000"),
        ("Costo total", "Una alternativa de ejemplo cuesta $6.000.000 de construcción y $2.000.000 de restauración. ¿Cuál es su costo total?", ["Se suman ambos costos.", "6.000.000 + 2.000.000 = 8.000.000."], "$8.000.000"),
    ],
    mistakes=[("Elegir la alternativa de menor costo de construcción sin sumar la restauración.", "La restauración puede volverla más cara.", "Compara el costo total de cada alternativa."),
              ("Creer que compensar es lo mismo que evitar.", "Compensar no elimina el daño original, solo equilibra su efecto en otro lugar.", "Primero evita, luego reduce, después restaura y al final compensa.")],
    T=[
        ("abc", "En Forestal: ¿qué significa «evitar» en la jerarquía de mitigación?", "Diseñar la actividad para que el impacto no ocurra, por ejemplo cambiando un trazado", "Reparar el daño después de que ocurra", "Hacer una acción en otro lugar para equilibrar el daño", "Evitar actúa antes del daño; reparar y compensar actúan después."),
        ("abc", "En Forestal: ¿qué significa «restaurar» en la jerarquía de mitigación?", "Reparar el daño en el mismo lugar para recuperar sus condiciones", "Pagar una multa a la autoridad", "Avisar a las personas del daño ocurrido", "Restaurar significa recuperar el lugar dañado; una multa o un aviso no lo hacen."),
        ("abc", "En Forestal: ¿qué significa «compensar» en la jerarquía de mitigación?", "Hacer una acción en otro lugar para equilibrar un impacto que no se pudo evitar ni reparar", "Evitar que el impacto ocurra", "Reducir el impacto en el mismo lugar", "Compensar se hace en otro lugar y es el último recurso."),
        ("=", "{F} ¿Cuántos pesos más cuesta construir la alternativa B que la A, sin considerar la restauración?", "12500000-10000000", "Se resta el costo de A al costo de B.", " pesos"),
        ("=", "{F} ¿Qué porcentaje más cara es la construcción de B respecto de la de A?", "(12500000-10000000)*100//10000000", "Se divide la diferencia entre el costo de A y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas hectáreas habría que restaurar si se elige la alternativa A?", "2*3", "Se multiplican las hectáreas afectadas por las que exige restaurar el plan por cada una.", " ha"),
        ("=", "{F} ¿Cuánto costaría restaurar esas hectáreas?", "2*3*1000000", "Se multiplican las hectáreas a restaurar por el costo de cada una.", " pesos"),
        ("=", "{F} ¿Cuál sería el costo total de la alternativa A, sumando la construcción y la restauración?", "10000000+2*3*1000000", "Se suman el costo de construcción y el de restaurar.", " pesos"),
        ("abc", "{F} Considerando el costo total, ¿qué alternativa conviene económicamente?", "La alternativa B, porque su costo total es menor que el de A", "La alternativa A, porque su construcción es más barata", "Ninguna, porque cuestan lo mismo", "A cuesta 16.000.000 en total y B cuesta 12.500.000."),
        ("=", "{F} ¿Cuántos pesos se ahorran con B respecto del costo total de A?", "10000000+2*3*1000000-12500000", "Se resta el costo total de B al costo total de A.", " pesos"),
        ("abc", "{F} Aunque A tuviera un costo total menor, ¿qué otra razón impediría elegirla sin cumplir la norma?", "Que afecta una franja de protección que el plan y la norma exigen proteger", "Que su trazado es más corto", "Que su construcción termina antes", "Afectar una zona protegida exige cumplir la norma y no solo comparar costos."),
        ("abc", "En Forestal: ¿por qué se prefiere evitar un impacto antes que repararlo?", "Porque un daño evitado no ocurre y hay daños que no se pueden reparar del todo", "Porque reparar siempre cuesta menos", "Porque compensar elimina el daño original", "Evitar es lo más efectivo, mientras que reparar y compensar no siempre devuelven lo perdido."),
        ("=", "{F} ¿Cuánto más larga, en porcentaje, es la alternativa B respecto de la A?", "(3-2)*100//2", "Se divide la diferencia de kilómetros entre la longitud de A y se multiplica por 100.", " %"),
    ],
    ctx=("abc", "Un contratista propone construir el camino por la franja protegida y «arreglar después», porque es más rápido. ¿Qué respondes?", "Que primero se evita el daño, y que lo consultarás con un adulto responsable", "Que sí, si se repara rápido", "Que sí, si se avisa después", "Evitar es preferible; reparar después no devuelve siempre lo dañado y exige cumplir la norma."),
    sc=[
        ("En Forestal: ¿qué es lo más preferible en la jerarquía de mitigación?", "Evitar el impacto", "Un impacto evitado no requiere reparación."),
        ("¿Qué incluye el costo total de una alternativa?", "La construcción y las medidas de restauración o compensación", "El costo total incluye todo lo que exige la alternativa."),
        ("¿En qué lugar se compensa un impacto?", "En otro lugar, y es el último recurso", "La compensación equilibra el efecto sin devolver el lugar dañado."),
    ],
    op=("Ficha de ejemplo (datos de ejemplo): se debe construir un camino. Alternativa C: 1 km, cuesta $6.000.000 y afecta 1 ha de una franja protegida; el plan exige restaurar 4 ha por cada hectárea afectada, a $750.000 la hectárea. Alternativa D: 2 km, cuesta $8.500.000 y no afecta la franja. Escribe (a) cuántas hectáreas y cuánto cuesta restaurar con C, (b) el costo total de C y de D, (c) cuál conviene y cuánto se ahorra, (d) qué nivel de la jerarquía de mitigación es la alternativa D.",
        "(a) 1 × 4 = 4 ha; 4 × 750.000 = 3.000.000 pesos. (b) C: 6.000.000 + 3.000.000 = 9.000.000; D: 8.500.000. (c) Conviene D: cuesta 500.000 pesos menos y además evita el daño a la franja. (d) Evitar.",
        ["calcula las hectáreas y el costo de restaurar", "calcula los costos totales", "elige con la jerarquía y no solo con el costo", "identifica el nivel de la jerarquía"],
        ["hoja con las cuatro respuestas"],
        ["no sumar la restauración", "elegir por menor construcción", "confundir evitar con compensar"],
        "Pregunta: «¿qué alternativa evita el daño a la franja?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa dos alternativas con costo de construcción y costo de restauración, y calcula el costo total de cada una.",
    extend="Explica con un ejemplo por qué compensar no es lo mismo que evitar.",
)
