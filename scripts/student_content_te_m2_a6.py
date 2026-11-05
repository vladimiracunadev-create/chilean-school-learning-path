"""Cuaderno del estudiante, 2.º medio Tecnología: OA 06 (proyectar escenarios de posibles impactos positivos y/o negativos de las innovaciones tecnológicas actuales en ámbitos personales, sociales, ambientales, legales, económicos u otros), clases 1 a 4.

Seguridad: las tareas son de lectura, cálculo y escritura; los ensayos de escenarios se hacen en papel con datos de ejemplo, sin personas reales ni equipos. Las innovaciones se nombran por tipo, sin marcas.
Vacío declarado: la proyección usa cambios constantes y dos períodos de porcentaje; el uso de software de simulación o de herramientas de análisis de datos queda para el docente.
"""
from __future__ import annotations

from student_content_te_m2_a import reg
from student_lessons import arith, ex

OA6 = "TE2M OA 06"

# ------------------------------------------------------------------ OA 06, clase 1
reg(
    OA6, 1,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a identificar impactos positivos y negativos de una innovación en distintos ámbitos, a distinguir impactos directos e indirectos y a ubicarlos en el corto, mediano y largo plazo. Sirve para empezar a proyectar escenarios con orden.",
    prior=["Sé las dimensiones para evaluar una innovación.", "Sé qué es un efecto esperado y uno no esperado.", "Sé calcular porcentajes."],
    explain=[
        "Un impacto es el cambio que produce una innovación en las personas o en el entorno. Puede ser positivo o negativo, y se puede presentar en distintos ámbitos: personal (tiempo, bienestar, privacidad), social (empleo, convivencia, acceso), ambiental (energía, residuos, agua), legal (normas, derechos, responsabilidades) y económico (costos, ahorros, ingresos). Un mismo impacto puede ser positivo en un ámbito y negativo en otro.",
        "Un impacto directo es el efecto inmediato de usar la innovación, como gastar menos agua con un riego con sensores. Un impacto indirecto es una consecuencia de otra consecuencia, como que el ahorro de agua cambie los hábitos de toda una comunidad. Los indirectos son más difíciles de prever porque dependen de decisiones de muchas personas.",
        "Los impactos también se ubican en el tiempo. El corto plazo llega hasta un año, el mediano plazo va de uno a tres años y el largo plazo es más de tres años. Para ordenarlos se usa una tabla con los ámbitos en las filas y el plazo en las columnas. Proyectar escenarios no es adivinar: es pensar con orden qué podría pasar y bajo qué condiciones.",
    ],
    vocab=[("impacto", "cambio que produce una innovación en personas o entorno"), ("ámbito", "área donde ocurre el impacto: personal, social, ambiental, legal o económica"), ("impacto directo", "efecto inmediato de usar la innovación"), ("impacto indirecto", "consecuencia que viene de otra consecuencia"), ("corto plazo", "hasta un año"), ("largo plazo", "más de tres años")],
    worked=[
        ("Clasificar un impacto", "Un asistente automático de estudio ahorra tiempo a las personas, pero algunas dejan de practicar. Clasifica ambos impactos por ámbito y signo.", ["Ahorrar tiempo mejora lo personal: positivo.", "Dejar de practicar afecta lo personal: negativo."], "Personal positivo (tiempo) y personal negativo (práctica)"),
        ("Directo o indirecto", "Un reparto a domicilio hace que algunos locales cierren con los años. ¿Es un impacto directo o indirecto?", ["No ocurre al usar el servicio, sino después de que cambian las compras.", "Viene de otra consecuencia."], "Indirecto, en el ámbito económico"),
    ],
    mistakes=[
        ("Listar solo los impactos positivos.", "Se pierde la parte del escenario que más conviene prever.", "Busca al menos un impacto negativo por ámbito."),
        ("Confundir impacto directo con indirecto.", "El indirecto no es inmediato: nace de otra consecuencia.", "Pregunta si ocurre al usar la innovación o después de un cambio previo."),
    ],
    R=[
        ("Un impacto indirecto es… A) una consecuencia que viene de otra consecuencia B) el efecto que se ve de inmediato al usar la innovación", "A", "El efecto inmediato es el directo."),
        ("«Se necesita una nueva norma para proteger datos». Ese impacto pertenece al ámbito… A) legal B) ambiental", "A", "Las normas y derechos corresponden al ámbito legal."),
        ("«Dentro de las próximas semanas» corresponde al… A) corto plazo B) largo plazo", "A", "El corto plazo son semanas o meses."),
    ],
    C=[
        ("Un servicio ahorra tiempo a las personas y consume más energía. ¿Cómo se clasifican? A) positivo en lo personal y negativo en lo ambiental B) positivo en todos los ámbitos", "A", "El mismo servicio puede tener signos distintos según el ámbito."),
        ("¿Cuál es un impacto directo? A) al activar un riego con sensores se usa menos agua B) la comunidad cambia sus hábitos en cinco años", "A", "Ocurre al usar la innovación."),
        ("¿Por qué conviene mirar varios ámbitos? A) porque una innovación puede ayudar en uno y perjudicar en otro B) porque todos los ámbitos son iguales", "A", "Mirar un solo ámbito deja puntos ciegos."),
    ],
    A=[
        ("Clasifica por ámbito y signo: (1) menor gasto mensual, (2) pérdida de privacidad, (3) menos residuos.", "1 económico positivo, 2 personal negativo, 3 ambiental positivo", "Cada impacto cae en un ámbito distinto."),
        arith("Se identifican 10 impactos de una innovación de ejemplo y 6 son positivos. ¿Qué porcentaje son negativos?", "(10-6)*100//10", "Se calcula la cantidad de negativos y se pasa a porcentaje.", " %"),
        arith("Un servicio de ejemplo hace que 50 hogares usen 3 kWh más cada mes. ¿Cuántos kWh de más se usan en 12 meses?", "3*50*12", "Se multiplican kWh, hogares y meses.", " kWh"),
    ],
    Z=[
        ("Un informe solo lista los impactos positivos de una innovación. ¿Qué le falta?", "Los impactos negativos y los de otros ámbitos", "Un escenario completo incluye ambos signos."),
        ("¿Por qué un impacto indirecto es más difícil de prever?", "Porque depende de cadenas de consecuencias y de decisiones de muchas personas", "Cada paso agrega incertidumbre."),
    ],
    D=[
        arith("Un sistema de ejemplo ahorra 20 minutos diarios a cada una de 30 personas durante 5 días a la semana. ¿Cuántas horas se ahorran en una semana?", "20*30*5//60", "Se calculan los minutos totales y se pasan a horas.", " horas"),
        arith("Cada hogar de ejemplo genera 2 kg de embalajes a la semana y hay 250 hogares. ¿Cuántos kg se generan en 4 semanas?", "2*250*4", "Se multiplican kg, hogares y semanas.", " kg"),
    ],
    ctx=arith("De 60 impactos de ejemplo registrados por un curso, 36 son de ámbito ambiental. ¿Qué porcentaje es?", "36*100//60", "Se divide entre el total y se pasa a porcentaje.", " %"),
    sc=[
        ("Nombra cinco ámbitos de impacto.", "Personal, social, ambiental, legal y económico", "Son los ámbitos de la clase."),
        ("En Tecnología: ¿qué es un impacto indirecto?", "Una consecuencia que viene de otra consecuencia", "No es el efecto inmediato."),
        ("¿Desde cuándo se considera largo plazo?", "Desde más de tres años", "Mediano plazo es de uno a tres años."),
    ],
    open_task=(
        "Escoge una innovación de ejemplo. Caso 1: un asistente automático que responde preguntas de estudio. Caso 2: paneles solares en los techos de un barrio. Caso 3: un servicio de reparto de comida con motos. Haz una tabla con cinco filas (los cinco ámbitos) y tres columnas (corto, mediano y largo plazo) y escribe un impacto en cada fila, marcando si es positivo o negativo y si es directo o indirecto. Debe haber al menos dos negativos.",
        "Caso 3: económico corto, más ventas (positivo directo); social largo, cierre de locales (negativo indirecto); ambiental mediano, más envases (negativo directo); legal mediano, normas para repartidores; personal corto, comodidad",
        ["cubre los cinco ámbitos", "marca signo y tipo", "incluye al menos dos negativos", "ubica cada impacto en un plazo"],
        ["tabla de cinco filas"],
        ["solo impactos positivos", "no distinguir directo de indirecto"],
        "Pregunta: «¿esto ocurre al usarla o después de otra consecuencia?». Así distinguirá directo e indirecto.",
    ),
    reinforce="Piensa en una tecnología de tu casa y escribe un impacto positivo y uno negativo en ámbitos distintos.",
    extend="Explica por qué ver solo un ámbito puede llevar a una proyección demasiado optimista.",
)

# ------------------------------------------------------------------ OA 06, clase 2
reg(
    OA6, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y los datos escritos en este cuaderno.",
    use="Aprenderé a leer una tendencia, a construir escenarios optimista, probable y pesimista con una proyección simple, a escribir supuestos y a definir señales de alerta. Sirve para proyectar con datos y no con deseos.",
    prior=["Sé calcular porcentajes.", "Sé qué es un escenario base.", "Sé qué es un supuesto."],
    explain=[
        "Una tendencia es la dirección en que cambia un dato a lo largo del tiempo. Si el uso de una innovación fue 40, 46, 52 y 58 usuarios en cuatro años, la tendencia es subir 6 por año, y la proyección del quinto año es 58 + 6 = 64. Una variable clave es el dato que más influye en cómo evoluciona el escenario, como el número de usuarios.",
        "Los escenarios se construyen cambiando la tendencia. El probable sigue la tendencia observada, el optimista supone que mejora más y el pesimista que mejora menos o empeora. Cuando el cambio es un porcentaje, se calcula sobre el valor del período anterior: 200 que crecen 10 % dos años seguidos pasan a 220 y luego a 242, porque el segundo 10 % se calcula sobre 220.",
        "Cada escenario escribe sus supuestos. Una señal de alerta es un indicador que avisa que la realidad se está acercando a un escenario no deseado, por ejemplo cuando se llega al 90 % de un límite. Como el futuro es incierto, los escenarios se revisan con datos nuevos y no se presentan como certezas.",
    ],
    vocab=[("tendencia", "dirección en que cambia un dato en el tiempo"), ("variable clave", "dato que más influye en cómo evoluciona el escenario"), ("escenario probable", "el que sigue la tendencia observada"), ("proyección", "cálculo del valor futuro"), ("señal de alerta", "indicador que avisa que se acerca un escenario no deseado"), ("supuesto", "condición que se da por cierta para calcular")],
    worked=[
        ("Proyectar con cambio constante", "Los usuarios fueron 40, 46, 52 y 58 en cuatro años. ¿Cuántos serán en el quinto año si la tendencia sigue?", ["El cambio por año es 6.", "58 + 6 = 64."], "64 usuarios"),
        ("Porcentaje dos años seguidos", "Un valor de 200 crece 10 % cada año durante dos años. ¿Cuánto vale al final?", ["Año 1: 200 + 20 = 220.", "Año 2: 220 + 22 = 242."], "242"),
    ],
    mistakes=[
        ("Calcular el segundo año con el valor inicial.", "El cambio del segundo año se calcula sobre el valor del año anterior.", "Actualiza el valor cada período."),
        ("Presentar un solo escenario como seguro.", "El futuro es incierto y depende de supuestos.", "Muestra al menos un escenario optimista, uno probable y uno pesimista."),
    ],
    R=[
        ("Una tendencia es… A) la dirección en que cambia un dato en el tiempo B) un dato aislado", "A", "Se observa en varios períodos."),
        arith("El uso de una innovación fue 30, 35, 40 y 45 usuarios en cuatro años. Si el cambio se mantiene, ¿cuántos habrá tres años después del último dato?", "45+5*3", "Se suma el cambio por año multiplicado por los años.", " usuarios"),
        ("Una señal de alerta es… A) un indicador que avisa que se acerca un escenario no deseado B) un premio al equipo", "A", "Sirve para reaccionar a tiempo."),
    ],
    C=[
        ("El escenario probable es… A) el que sigue la tendencia observada B) el que más gusta al equipo", "A", "Se basa en datos y no en deseos."),
        ("Una variable clave es… A) el dato que más influye en cómo evoluciona el escenario B) un dato decorativo", "A", "Cambiarla mueve mucho el resultado."),
        ("¿Para qué se escriben los supuestos? A) para saber cuándo el escenario deja de ser válido B) no es necesario escribirlos", "A", "Si un supuesto falla, el escenario cambia."),
    ],
    A=[
        arith("Un valor de 100 crece 20 % cada año durante dos años. ¿Cuánto vale al final?", "100+100*20//100+(100+100*20//100)*20//100", "El segundo 20 % se calcula sobre el valor del primer año.", ""),
        arith("Una innovación de ejemplo tiene 40 usuarios hoy. En el escenario probable suma 5 por año, durante 3 años. ¿Cuántos usuarios tendrá?", "40+5*3", "Se suma el cambio de todos los años.", " usuarios"),
        arith("El límite de consumo es 250 kWh al mes y la alerta se activa al llegar al 90 %. ¿En cuántos kWh se activa?", "250*90//100", "Se calcula el 90 % del límite.", " kWh"),
    ],
    Z=[
        ("Dos escenarios dan resultados muy distintos porque usan supuestos diferentes. ¿Es un error?", "No: es normal, y por eso se escribe el supuesto de cada escenario", "Los supuestos explican las diferencias."),
        ("Un equipo proyecta diez años con el crecimiento de un solo año. ¿Qué cuidado falta?", "Revisar si la tendencia se mantiene y comunicar un rango", "Una tendencia corta no sostiene una proyección larga."),
    ],
    D=[
        arith("Los usuarios de un servicio de ejemplo fueron 200, 260 y 320 en tres años. Si el cambio se mantiene, ¿cuántos serán en el sexto año?", "200+60*5", "Desde el primer año se suman 5 cambios de 60.", " usuarios"),
        arith("Un servicio parte con 50 usuarios y crece 20 % cada año durante 2 años. ¿Cuántos usuarios tendrá?", "50+50*20//100+(50+50*20//100)*20//100", "El segundo aumento se calcula sobre 60.", " usuarios"),
    ],
    ctx=arith("En un barrio de ejemplo, 80 hogares usan la innovación y se suman 12 cada año. ¿Cuántos hogares la usarán en 4 años?", "80+12*4", "Se suma el aumento de los cuatro años.", " hogares"),
    sc=[
        ("¿Qué escenario sigue la tendencia observada?", "El probable", "Los otros suponen más o menos mejora."),
        ("¿Sobre qué valor se calcula un porcentaje del segundo año?", "Sobre el valor del año anterior", "Se actualiza el valor cada período."),
        ("En Tecnología: ¿qué es una señal de alerta?", "Un indicador que avisa que se acerca un escenario no deseado", "Permite reaccionar a tiempo."),
    ],
    open_task=(
        "Usa estos datos de ejemplo. Un servicio de reparto tuvo estos pedidos diarios en un barrio durante cuatro años: 100, 120, 140 y 160. Construye tres escenarios para el año 6 (dos años después del último dato): probable, con el mismo cambio; optimista, con un cambio de 30 por año; pesimista, con un cambio de 10 por año. Escribe un supuesto para cada uno, una variable clave y una señal de alerta con su valor.",
        "Probable: 160 + 20 × 2 = 200; optimista: 160 + 30 × 2 = 220; pesimista: 160 + 10 × 2 = 180; variable clave, número de pedidos; alerta, pasar de 190 pedidos diarios",
        ["calcula los tres escenarios", "escribe un supuesto por escenario", "nombra una variable clave", "define una señal de alerta con valor"],
        ["hoja con cálculos y supuestos"],
        ["un solo escenario", "no escribir supuestos"],
        "Pregunta: «¿qué tendría que pasar para que se cumpla el optimista?». Eso es el supuesto de ese escenario.",
    ),
    reinforce="Anota durante cuatro días cuántas veces usas una aplicación y proyecta cuántas serían los tres días siguientes si el cambio se mantiene.",
    extend="Explica por qué se presenta un rango de escenarios y no un solo número.",
)

# ------------------------------------------------------------------ OA 06, clase 3
reg(
    OA6, 3,
    materials="Hoja, lápiz, regla y los casos escritos en este cuaderno.",
    use="Aprenderé a representar escenarios con una línea de tiempo, un árbol de consecuencias y una matriz de probabilidad e impacto. Sirve para ordenar los impactos y decidir cuáles atender primero.",
    prior=["Sé qué es un impacto directo e indirecto.", "Sé multiplicar números enteros.", "Sé leer una tabla."],
    explain=[
        "Un escenario se puede representar de tres maneras. La línea de tiempo ordena los impactos según cuándo ocurren. El árbol de consecuencias parte de un cambio y muestra cómo lleva a otros con flechas: más pedidos a domicilio lleva a más envases, y estos llevan a más residuos en el barrio. Cada flecha dice «lleva a» y es una afirmación que necesita evidencia.",
        "La matriz de probabilidad e impacto ayuda a priorizar. A cada impacto se le da una probabilidad de 1 (baja), 2 (media) o 3 (alta), y un tamaño de impacto de 1, 2 o 3. La prioridad es probabilidad × impacto y va de 1 a 9. Con 6 o más la prioridad es alta; con 3 o 4 es media; con 2 o menos es baja. Los puntajes son juicios del equipo, no mediciones exactas, y se anotan como de ejemplo.",
        "Mientras más pasos tiene una cadena de consecuencias, menos segura es: cada paso agrega incertidumbre. Por eso conviene escribir qué evidencia respalda cada flecha y marcar las que son hipótesis. Dos impactos con la misma prioridad pueden pedir medidas distintas.",
    ],
    vocab=[("línea de tiempo", "orden de los impactos según cuándo ocurren"), ("árbol de consecuencias", "esquema de causas y efectos encadenados"), ("probabilidad", "qué tan posible es que ocurra, de 1 a 3"), ("impacto (tamaño)", "qué tan grande sería el efecto, de 1 a 3"), ("prioridad", "probabilidad × impacto"), ("hipótesis", "afirmación que aún no está comprobada")],
    worked=[
        ("Calcular la prioridad", "Un riesgo tiene probabilidad 2 e impacto 3. ¿Qué prioridad tiene?", ["Multiplico 2 × 3.", "El resultado es 6, que es prioridad alta."], "6, alta"),
        ("Completar un árbol", "Más pedidos a domicilio lleva a más envases. ¿Qué consecuencia sigue en la cadena?", ["Los envases se desechan.", "Eso lleva a más residuos en el barrio."], "Más residuos en el barrio"),
    ],
    mistakes=[
        ("Dar probabilidad 3 a todos los impactos.", "La matriz deja de distinguir cuáles atender primero.", "Compara los impactos entre sí y usa los tres niveles."),
        ("Dibujar flechas sin evidencia.", "Una cadena larga de hipótesis parece segura sin serlo.", "Marca qué flechas tienen datos y cuáles son hipótesis."),
    ],
    R=[
        ("Un árbol de consecuencias muestra… A) una cadena de efectos que se producen unos a otros B) una lista de materiales", "A", "Las flechas indican «lleva a»."),
        arith("Un riesgo de ejemplo tiene probabilidad 3 e impacto 2. ¿Qué prioridad tiene?", "3*2", "Prioridad = probabilidad × impacto.", ""),
        ("Una línea de tiempo ordena los impactos según… A) cuándo ocurren B) el tamaño de la letra", "A", "Sirve para ver la secuencia."),
    ],
    C=[
        ("Riesgo X: probabilidad 3 e impacto 1. Riesgo Y: probabilidad 1 e impacto 3. ¿Cómo son sus prioridades? A) iguales, ambas valen 3 B) la de X es mayor", "A", "3 × 1 y 1 × 3 dan lo mismo."),
        ("¿Para qué se unen los hechos con flechas en un árbol? A) para ver cómo un cambio lleva a otros B) para decorar el esquema", "A", "Las flechas muestran la relación causa y efecto."),
        ("Un impacto con prioridad 6 o más se trata… A) primero, con medidas preventivas B) al final, porque es muy raro", "A", "Prioridad alta significa atender primero."),
    ],
    A=[
        arith("Un impacto de ejemplo tiene probabilidad 2 e impacto 3. ¿Cuántos puntos de prioridad tiene?", "2*3", "Se multiplican probabilidad e impacto.", " puntos"),
        ("Ordena de mayor a menor prioridad: R1 con probabilidad 2 e impacto 2, R2 con probabilidad 3 e impacto 3, R3 con probabilidad 1 e impacto 2.", "R2, R1, R3", "Las prioridades son 9, 4 y 2."),
        ("Completa la cadena: se instalan cajas de autoservicio, lo que lleva a que se necesiten menos cajeros, lo que lleva a… A) menos puestos de caja disponibles en la zona B) más envases reciclados en la zona", "A", "Si se necesitan menos cajeros, hay menos puestos de caja."),
    ],
    Z=[
        ("Un árbol de consecuencias llega a seis pasos sin evidencia. ¿Qué pasa con su confianza?", "Disminuye, porque cada paso agrega incertidumbre", "Una cadena larga de hipótesis es poco segura."),
        ("Un equipo da probabilidad 3 a todos los impactos. ¿Qué pierde la matriz?", "La capacidad de distinguir cuáles atender primero", "Si todo es igual, no sirve para priorizar."),
    ],
    D=[
        arith("Cinco riesgos de ejemplo tienen prioridades 9, 6, 4, 3 y 2. ¿Qué porcentaje tiene prioridad alta (6 o más)?", "2*100//5", "Solo el 9 y el 6 llegan a 6 o más: 2 de 5.", " %"),
        arith("Cuatro riesgos de ejemplo tienen prioridades 9, 6, 3 y 2. ¿Qué porcentaje del total de prioridades suman los dos altos?", "(9+6)*100//(9+6+3+2)", "Se suman los altos y se divide entre el total.", " %"),
    ],
    ctx=arith("En una línea de tiempo de ejemplo, el impacto A ocurre en el mes 2 y el B en el mes 8. ¿Cuántos meses después ocurre B?", "8-2", "Se restan los meses.", " meses"),
    sc=[
        ("¿Cómo se calcula la prioridad en la matriz?", "Probabilidad × impacto", "Es la fórmula de la clase."),
        ("En Tecnología: ¿qué es un árbol de consecuencias?", "Un esquema de causas y efectos encadenados", "Cada flecha dice «lleva a»."),
        ("¿Qué hace menos segura una cadena larga de consecuencias?", "Que cada paso agrega incertidumbre", "Hay que marcar las hipótesis."),
    ],
    open_task=(
        "Escoge una innovación de ejemplo. Caso 1: un asistente automático de estudio en un liceo. Caso 2: paneles solares en techos de un barrio. Caso 3: cajas de autoservicio en un supermercado. Para el caso elegido dibuja un árbol de consecuencias con al menos tres niveles, escribe cinco impactos en una línea de tiempo y arma una matriz con la probabilidad y el impacto de cada uno (de ejemplo). Indica cuáles tienen prioridad alta y marca una flecha que sea solo una hipótesis.",
        "Caso 3: menos cajeros contratados lleva a ahorro de costos lleva a precios más bajos; el impacto del empleo tiene probabilidad 3 e impacto 3, prioridad 9; la flecha de precios más bajos es una hipótesis",
        ["árbol de al menos tres niveles", "línea de tiempo de cinco impactos", "calcula la prioridad con probabilidad × impacto", "marca una hipótesis"],
        ["hoja con árbol, línea de tiempo y matriz"],
        ["todas las prioridades iguales", "flechas sin sentido"],
        "Pregunta: «¿qué dato respalda esta flecha?». Si no hay dato, es una hipótesis y se marca.",
    ),
    reinforce="Dibuja un árbol de consecuencias de tres pasos para una tecnología de tu casa.",
    extend="Explica por qué dos impactos con la misma prioridad pueden pedir medidas distintas.",
)

# ------------------------------------------------------------------ OA 06, clase 4
reg(
    OA6, 4,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno. El ensayo del escenario se hace en papel, con datos de ejemplo.",
    use="Aprenderé a proponer medidas para prevenir, mitigar y adaptarse a un impacto negativo, a medir su efecto sobre la prioridad y a comunicar escenarios con responsabilidad. Sirve para pasar de proyectar a actuar con cuidado.",
    prior=["Sé calcular la prioridad de un impacto.", "Sé qué es una señal de alerta.", "Sé que debo hablar con una persona adulta de confianza si algo me preocupa."],
    explain=[
        "Frente a un impacto negativo hay tres tipos de medidas. Prevenir es evitar que ocurra, por ejemplo hacer una prueba piloto pequeña antes de extender una innovación. Mitigar es reducir el daño si ocurre, como contar con un fondo para reparar equipos. Adaptarse es prepararse para convivir con el cambio, como ofrecer cursos para aprender a usar un servicio. Una medida bien planteada dice quién la hace, cuándo y con qué indicador se mide.",
        "El efecto de una medida se ve en la prioridad: si baja la probabilidad o el tamaño del impacto, baja la prioridad. Un riesgo con probabilidad 3 e impacto 3 vale 9; si una medida baja la probabilidad a 1, vale 3. Una medida se ensaya primero en papel, con un caso de ejemplo y roles repartidos, sin personas ni equipos reales, y se corrige antes de proponerla.",
        "Comunicar un escenario exige responsabilidad. Se dice el rango, los supuestos y qué se puede hacer. No se usa el alarmismo, como «esto destruirá todos los empleos», ni el triunfalismo, como «no habrá ningún problema». Tampoco se oculta el escenario pesimista para no asustar, porque entonces nadie puede prepararse. Si un escenario te produce angustia, conversa con una persona adulta de confianza; en Chile, el Fono Niños 147 atiende a niños, niñas y adolescentes.",
    ],
    vocab=[("prevenir", "evitar que el impacto ocurra"), ("mitigar", "reducir el daño si el impacto ocurre"), ("adaptarse", "prepararse para convivir con el cambio"), ("prueba piloto", "ensayo pequeño antes de extender una innovación"), ("alarmismo", "exagerar el peligro para asustar"), ("triunfalismo", "negar los problemas y exagerar los logros")],
    worked=[
        ("Clasificar medidas", "Clasifica: (a) exigir consentimiento antes de recoger datos, (b) reciclar los equipos al final de su vida útil, (c) capacitar a trabajadores para nuevos puestos.", ["(a) evita que el problema ocurra: prevenir.", "(b) reduce el daño ambiental, y (c) ayuda a convivir con el cambio: adaptarse."], "a prevenir, b mitigar, c adaptarse"),
        ("Efecto en la prioridad", "Un riesgo con probabilidad 2 e impacto 3 baja su probabilidad a 1 con una medida. ¿Cuánto baja su prioridad?", ["Antes: 2 × 3 = 6.", "Después: 1 × 3 = 3, es decir, baja 3 puntos."], "3 puntos"),
    ],
    mistakes=[
        ("Proponer una medida sin responsable ni indicador.", "No se sabe quién la hará ni cómo comprobar que funciona.", "Escribe quién, cuándo y con qué indicador."),
        ("Ocultar el escenario pesimista para no asustar.", "Quien decide no puede prepararse.", "Comunícalo con rango, supuestos y medidas posibles."),
    ],
    R=[
        ("Mitigar significa… A) reducir el daño si el impacto ocurre B) evitar que ocurra", "A", "Evitar que ocurra es prevenir."),
        ("Prevenir significa… A) evitar que el impacto ocurra B) reducir el daño una vez que ocurre", "A", "La prevención actúa antes."),
        arith("Un riesgo de ejemplo tiene probabilidad 3 e impacto 2. Con una medida, la probabilidad baja a 1. ¿Cuántos puntos baja su prioridad?", "3*2-1*2", "Se resta la prioridad de después a la de antes.", " puntos"),
    ],
    C=[
        ("¿Por qué es seguro ensayar un escenario en papel? A) porque usa datos de ejemplo y no involucra personas ni equipos reales B) porque no se puede equivocar", "A", "No hay riesgo para nadie."),
        ("¿Cómo se comunica mejor un escenario? A) con el rango, los supuestos y lo que se puede hacer B) afirmando que ocurrirá seguro", "A", "La honestidad incluye reconocer la incertidumbre."),
        ("Si leer escenarios te produce angustia, ¿qué haces? A) conversas con una persona adulta de confianza B) lo guardas en secreto", "A", "Compartirlo con un adulto de confianza ayuda."),
    ],
    A=[
        ("Clasifica como prevenir, mitigar o adaptarse: (1) prueba piloto con un grupo pequeño antes de extender, (2) fondo para reparar equipos dañados, (3) cursos para aprender a usar el servicio.", "1 prevenir, 2 mitigar, 3 adaptarse", "La primera evita el problema, la segunda repara el daño y la tercera prepara a las personas."),
        arith("Un riesgo de ejemplo con probabilidad 3 e impacto 3 baja a probabilidad 1 con una medida. ¿Cuántos puntos baja su prioridad?", "3*3-1*3", "Se resta la prioridad nueva de la anterior.", " puntos"),
        arith("Se activa una alerta al llegar al 15 % de 200 hogares sin acceso. ¿Con cuántos hogares sin acceso se activa?", "200*15//100", "Se calcula el 15 % de 200.", " hogares"),
    ],
    Z=[
        ("Un informe dice que una innovación «destruirá todos los empleos». ¿Qué falta para comunicarlo con responsabilidad?", "Datos, supuestos, rango y medidas posibles, sin alarmismo", "Una afirmación absoluta sin evidencia asusta sin ayudar."),
        ("Un equipo omite el escenario pesimista para no asustar. ¿Qué problema crea?", "Esconde información y impide que se preparen medidas", "Quien decide necesita conocer todos los escenarios."),
    ],
    D=[
        arith("Cuatro riesgos de ejemplo tienen prioridades 9, 6, 6 y 4 y, tras las medidas, 6, 3, 4 y 2. ¿Cuánto baja la suma de prioridades?", "(9+6+6+4)-(6+3+4+2)", "Se resta la suma de después a la de antes.", " puntos"),
        arith("La suma de prioridades baja de 25 a 15. ¿Qué porcentaje bajó?", "(25-15)*100//25", "Se calcula la diferencia sobre el valor inicial.", " %"),
    ],
    ctx=arith("Una medida cuesta $24.000 y se reparte en partes iguales entre 8 integrantes de un equipo. ¿Cuánto aporta cada uno?", "24000//8", "Se divide el costo entre los integrantes.", " pesos"),
    sc=[
        ("¿Qué diferencia hay entre prevenir y mitigar?", "Prevenir evita que ocurra; mitigar reduce el daño si ocurre", "Son medidas en momentos distintos."),
        ("En Tecnología: ¿qué es el alarmismo?", "Exagerar el peligro para asustar", "Es una forma poco responsable de comunicar."),
        ("¿Qué debe decir una medida bien planteada?", "Quién la hace, cuándo y con qué indicador se mide", "Así se puede comprobar."),
    ],
    open_task=(
        "Usa este caso de ejemplo. Un liceo piensa usar un asistente automático para apoyar el estudio. Riesgos de ejemplo: a) algunos estudiantes dejan de practicar (probabilidad 3, impacto 2); b) hay datos personales mal protegidos (probabilidad 2, impacto 3); c) quienes no tienen conexión quedan atrás (probabilidad 2, impacto 2). Calcula las prioridades, propone una medida de prevención, una de mitigación y una de adaptación con responsable e indicador, calcula la nueva prioridad de uno de los riesgos y escribe un párrafo corto que comunique el escenario con rango, supuestos y sin alarmismo.",
        "Prioridades: a) 6, b) 6, c) 4; prevenir: pedir consentimiento (docente, 100 % de los casos); mitigar: reparar equipos; adaptarse: talleres; b baja a probabilidad 1 y prioridad 3; párrafo con rango y supuestos",
        ["calcula las tres prioridades", "propone tres tipos de medida con responsable e indicador", "calcula una prioridad nueva", "comunica sin alarmismo"],
        ["hoja con cálculos y párrafo"],
        ["medidas sin indicador", "comunicar con alarmismo"],
        "Pregunta: «¿cómo sabrías si la medida funcionó?». Debe poder nombrar un indicador.",
    ),
    reinforce="Elige un riesgo de una tecnología que uses y escribe una medida para prevenirlo y otra para mitigarlo.",
    extend="Explica por qué ocultar el escenario pesimista es tan problemático como exagerarlo.",
)
