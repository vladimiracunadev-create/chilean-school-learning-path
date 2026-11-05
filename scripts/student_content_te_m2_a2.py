"""Cuaderno del estudiante, 2.º medio Tecnología: OA 02 (soluciones colaborativas para reducir efectos perjudiciales del uso de energía y materiales, con herramientas TIC colaborativas), clases 1 a 5.

Seguridad: trabajo en papel, cartón y maquetas; sin electricidad de red, herramientas cortantes ni productos químicos.
Las herramientas colaborativas se nombran por tipo (documento, planilla, tablero compartido); su uso real, con cuentas y equipos, queda para el docente. Todas las cifras son datos de ejemplo.
"""
from __future__ import annotations

from student_content_te_m2_a import reg
from student_lessons import arith, ex

OA2 = "TE2M OA 02"

# ------------------------------------------------------------------ OA 02, clase 1
reg(
    OA2, 1,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno. Un documento compartido se simula con una hoja de tres columnas.",
    use="Aprenderé a redactar una necesidad sin nombrar la solución, a definir criterios medibles y restricciones y a repartir el trabajo en un equipo. Sirve para empezar una solución sustentable con una meta clara.",
    prior=["Sé que un efecto perjudicial es un gasto o daño sin beneficio.", "Sé calcular porcentajes y promedios sencillos.", "Sé qué es un recurso."],
    explain=[
        "Una necesidad se redacta como algo que falta o sobra, con un dato: «El casino bota 90 vasos desechables al día». No dice «hay que comprar vasos lavables», porque eso ya es una solución. El usuario es la persona que se beneficia o que usará la solución, y conviene saber qué necesita de verdad. La línea base es lo que se gasta hoy, medido antes de actuar, por ejemplo el promedio de varios días.",
        "Un criterio dice cuándo la solución será buena y se puede medir: tiene un indicador (qué se mide) y una meta (cuánto). Por ejemplo, «reducir 25 % las hojas usadas por semana». Una restricción es un límite que la solución no puede sobrepasar, como un presupuesto máximo, un plazo o una regla de seguridad. El criterio dice lo que debe lograr; la restricción, lo que no puede pasar.",
        "El trabajo se hace en equipo. Una herramienta colaborativa, como un documento o una planilla compartida, permite que varias personas escriban y editen el mismo archivo, cada una con un rol. Antes de empezar se acuerda quién redacta, quién registra datos y quién revisa, para que todas las tareas tengan responsable.",
    ],
    vocab=[("necesidad", "algo que falta o sobra, descrito con un dato y sin nombrar la solución"), ("usuario", "persona que usará la solución o se beneficia con ella"), ("línea base", "lo que se gasta hoy, medido antes de actuar"), ("criterio", "condición medible que dice cuándo la solución es buena"), ("restricción", "límite que la solución no puede sobrepasar"), ("herramienta colaborativa", "archivo o servicio compartido que varias personas editan")],
    worked=[
        ("Pasar de solución a necesidad", "Un grupo escribe: «Hay que instalar contenedores de colores en el patio». Reescríbelo como necesidad.", ["Pregunto qué problema hay: los residuos del patio se mezclan.", "Agrego un dato y el efecto: «Los residuos del patio se mezclan y no se pueden separar para reutilizar»."], "Los residuos del patio se mezclan y no se pueden separar"),
        ("Meta desde la línea base", "Un curso de ejemplo usa 120 botellas plásticas por semana y quiere bajar 25 %. ¿Cuántas botellas como máximo?", ["Calculo 25 % de 120: 120 × 25 ÷ 100 = 30.", "Resto: 120 − 30 = 90."], "90 botellas como máximo"),
    ],
    mistakes=[
        ("Escribir la necesidad como «necesitamos una aplicación para…».", "Nombra una solución antes de describir el problema y limita las ideas.", "Escribe primero qué falta o sobra y cuánto; la solución se elige después."),
        ("Poner como criterio «que sea buena».", "No tiene indicador ni meta, así que nadie puede comprobarlo.", "Usa un indicador y un número: «bajar 25 % las hojas usadas»."),
    ],
    R=[
        ("¿Cuál enunciado es una necesidad y no una solución? A) «El curso gasta 30 hojas al día en guías que no se usan» B) «Hay que comprar una impresora que gaste menos tinta»", "A", "Describir un gasto con un dato es una necesidad; «hay que comprar…» ya propone una solución."),
        ("¿Cuál es un criterio medible? A) «que se vea moderno» B) «reducir 25 % el gasto de papel en un mes»", "B", "«Reducir 25 % el gasto de papel en un mes» tiene indicador (gasto de papel) y meta (25 %)."),
        ("¿Qué es una restricción? A) un límite como un presupuesto máximo de $20.000 B) lo que el usuario sueña lograr", "A", "La restricción es un límite que no se puede pasar."),
    ],
    C=[
        ("Un equipo escribe: «Necesitamos una aplicación para apagar luces». ¿Qué falla tiene esa frase? A) nombra una solución antes de describir el efecto B) no incluye el nombre del equipo", "A", "Una necesidad describe el gasto o daño, no el objeto que se propone."),
        ("La solución será un aviso para quienes cierran el liceo cada tarde. ¿Quién es el usuario directo? A) quienes cierran el liceo B) todos los estudiantes del liceo", "A", "El usuario directo es quien usará el aviso."),
        ("El criterio es «reducir 25 % las hojas usadas por semana». ¿Cuál es su indicador? A) las hojas usadas por semana B) la cantidad de integrantes del equipo", "A", "El indicador es lo que se mide: hojas por semana."),
    ],
    A=[
        arith("Un curso de ejemplo usa 80 hojas a la semana. Su meta es bajar 25 %. ¿Cuántas hojas como máximo debe usar?", "80-80*25//100", "Se calcula el 25 % de la línea base y se resta.", " hojas"),
        ("Clasifica como criterio (C) o restricción (R): (1) «presupuesto máximo de $15.000», (2) «reducir 30 % el gasto de energía», (3) «trabajar solo con papel y cartón».", "1 R, 2 C, 3 R", "Los límites de dinero y de materiales son restricciones; la reducción es lo que debe lograr."),
        arith("Una planilla compartida de ejemplo registra las hojas usadas de lunes a viernes: 42, 38, 51, 44 y 45. ¿Cuál es la línea base, es decir, el promedio diario?", "(42+38+51+44+45)//5", "El promedio se calcula sumando los cinco días y dividiendo entre 5.", " hojas"),
    ],
    Z=[
        ("Un equipo define el criterio «que a todos les guste la solución». ¿Qué falla tiene y cómo se corrige?", "No tiene indicador ni meta; se corrige con «al menos 8 de 10 usuarios dicen que la usarían»", "Un criterio debe poder medirse con un número."),
        ("Una necesidad dice: «Los estudiantes no ahorran energía». ¿Es suficiente para empezar?", "No: falta medir cuánto, dónde y desde cuándo", "Sin línea base no se puede saber si la solución mejora algo."),
    ],
    D=[
        arith("Un curso de ejemplo bajó de 600 a 450 hojas al mes. ¿Qué porcentaje redujo?", "(600-450)*100//600", "Se calcula la diferencia, se multiplica por 100 y se divide entre el valor inicial.", " %"),
        arith("Un casino de ejemplo usa 250 vasos a la semana y la meta es bajar 20 %. En la primera semana de prueba usó 215. ¿Cuántos vasos más debe reducir para cumplir la meta?", "215-(250-250*20//100)", "La meta es 200 vasos; se resta del valor actual.", " vasos"),
    ],
    ctx=arith("Un casino de ejemplo bota 90 vasos desechables al día y se propone bajar 40 %. ¿Cuántos vasos al día quedarían?", "90-90*40//100", "Se calcula el 40 % de 90 y se resta del total.", " vasos"),
    sc=[
        ("¿Qué debe evitar una necesidad bien redactada?", "Nombrar la solución", "Si nombra el objeto, la solución ya está decidida."),
        ("En Tecnología: ¿qué es la línea base?", "Lo que se gasta hoy, medido antes de actuar", "Sirve para saber si la solución mejora algo."),
        ("¿Qué permite hacer un documento compartido?", "Que varias personas editen el mismo archivo", "Es el sentido de una herramienta colaborativa."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: un casino de ejemplo bota 70 vasos al día. Caso 2: un laboratorio de computación deja 12 equipos encendidos 3 horas después de la jornada. Caso 3: un taller de ejemplo desecha 15 kg de cartón por semana. En una hoja con tres columnas (una por integrante) escribe: (1) la necesidad con su dato, sin nombrar la solución, (2) el usuario, (3) dos criterios con indicador y meta, (4) una restricción y (5) el rol de cada integrante.",
        "Caso 1: necesidad, se botan 70 vasos al día; usuario, quienes almuerzan; criterios, bajar 40 % los vasos y que el 80 % de los usuarios la use; restricción, presupuesto máximo de $20.000; roles, redactar, registrar datos y revisar",
        ["la necesidad tiene dato y no nombra solución", "los criterios tienen indicador y meta", "incluye una restricción", "cada integrante tiene un rol"],
        ["hoja con las cinco partes"],
        ["escribir «hay que comprar…» como necesidad", "criterios sin número"],
        "Pregunta: «¿cómo sabrías, con un número, que tu criterio se cumplió?». Si no puede decirlo, pídele agregar indicador y meta.",
    ),
    reinforce="Elige un gasto de tu curso y escribe su necesidad con un dato, sin nombrar la solución.",
    extend="Explica por qué una buena necesidad no nombra la solución y qué ideas se perderían si lo hiciera.",
)

# ------------------------------------------------------------------ OA 02, clase 2
reg(
    OA2, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y las tablas escritas en este cuaderno.",
    use="Aprenderé a evaluar fuentes, a descartar alternativas que no cumplen las restricciones y a compararlas con una matriz con pesos. Sirve para elegir una solución con razones y no por costumbre.",
    prior=["Sé redactar una necesidad con criterios y restricciones.", "Sé multiplicar y sumar.", "Sé calcular porcentajes."],
    explain=[
        "Investigar soluciones es buscar y comparar alternativas en fuentes confiables. Una fuente es más confiable si tiene autoría identificable, fecha, datos y método, y si no gana dinero con lo que afirma. Una promesa publicitaria como «reduce 90 % el gasto» sin datos ni método no sirve como evidencia. Las fuentes se anotan en una planilla compartida para que todo el equipo las revise.",
        "Primero se aplican las restricciones: una alternativa que las incumple se descarta, aunque sea muy buena en lo demás. Con las que quedan se arma una matriz de decisión. Cada criterio tiene un peso, que dice su importancia (1 baja, 3 alta), fijado antes de puntuar. Cada alternativa recibe un puntaje de 1 a 3 en cada criterio, donde 3 es siempre lo mejor: en costo, 3 significa más barata. El aporte es peso × puntaje y el total es la suma de los aportes.",
        "Una alternativa también se puede comparar por su costo por uso: el precio dividido entre las veces que se usará. Cambiar los pesos después de ver los resultados, solo para que gane la idea favorita, hace trampa. Si los datos son dudosos, se anota que falta información y se busca más antes de decidir.",
    ],
    vocab=[("fuente confiable", "fuente con autoría, fecha, datos y método, sin interés en vender"), ("matriz de decisión", "tabla que compara alternativas con criterios"), ("peso", "importancia de un criterio, de 1 a 3"), ("puntaje", "nota de 1 a 3 que recibe una alternativa en un criterio"), ("descartar", "sacar una alternativa porque incumple una restricción"), ("costo por uso", "precio dividido entre las veces que se usa")],
    worked=[
        ("Matriz con dos alternativas", "Criterios: costo (peso 2) y ahorro (peso 1). Alternativa K: costo 3, ahorro 1. Alternativa L: costo 1, ahorro 3. ¿Cuál suma más?", ["K: 2 × 3 + 1 × 1 = 6 + 1 = 7.", "L: 2 × 1 + 1 × 3 = 2 + 3 = 5."], "K, con 7 puntos"),
        ("Evaluar una fuente", "Un aviso dice «nuestro aparato ahorra 80 %» y no muestra autoría, fecha ni método. ¿Es confiable?", ["Reviso autoría, fecha, datos y método: no trae ninguno.", "Además quien lo publica vende el aparato."], "No es confiable"),
    ],
    mistakes=[
        ("Sumar los puntajes sin multiplicar por el peso.", "Un criterio importante debe influir más que uno secundario.", "Calcula siempre peso × puntaje antes de sumar."),
        ("Elegir la alternativa con más puntos aunque supere el presupuesto máximo.", "Las restricciones se aplican antes: lo que las incumple se descarta.", "Descarta primero y puntúa después."),
    ],
    R=[
        ("¿Cuál fuente es más confiable? A) un video anónimo sin fecha ni datos B) un informe de una institución pública con autoría, fecha y datos", "B", "La autoría, la fecha y los datos permiten comprobar la información."),
        ("El presupuesto máximo es $10.000 y la alternativa X cuesta $14.000. ¿Qué se hace? A) se descarta porque supera la restricción B) se le sube el peso al costo", "A", "Una alternativa que incumple una restricción no sigue en la comparación."),
        arith("En una matriz, el criterio «seguridad» tiene peso 3 y una alternativa recibe puntaje 2. ¿Cuántos puntos aporta?", "3*2", "El aporte es peso × puntaje.", " puntos"),
    ],
    C=[
        ("¿Por qué se comparan varias alternativas? A) para ver cuál cumple mejor los criterios y no quedarse con la primera idea B) porque siempre hay que elegir la más barata", "A", "La comparación evita decidir por costumbre."),
        ("Una tienda promete «reduce 90 % el gasto». Un estudio con método y datos mide 20 %. ¿Cuál es más confiable? A) la tienda, porque promete más B) el estudio, porque muestra método y datos y no vende el producto", "B", "La confianza depende de la evidencia, no de la promesa."),
        ("¿Cuál es una restricción de seguridad para el taller escolar? A) trabajar solo con papel, cartón y maquetas, sin electricidad de red B) lograr un ahorro de 30 %", "A", "Es un límite de seguridad; el ahorro es un criterio."),
    ],
    A=[
        ("Criterios: costo (peso 3) y ahorro (peso 2). Alternativa P: costo 3, ahorro 1. Alternativa Q: costo 2, ahorro 3. ¿Cuál suma más y cuántos puntos?", "Q, 12 puntos", "P suma 3 × 3 + 2 × 1 = 11 y Q suma 3 × 2 + 2 × 3 = 12."),
        arith("Una alternativa cuesta $4.500 en materiales y se usará 90 veces. ¿Cuál es su costo por uso?", "4500//90", "Costo por uso = precio ÷ veces de uso.", " pesos"),
        ("Planilla de ejemplo: F1, informe de una universidad con autoría y fecha; F2, aviso comercial sin autoría ni fecha; F3, guía de un ministerio con autoría y fecha. ¿Cuáles cumplen «tiene autoría y fecha»?", "F1 y F3", "F2 no muestra ninguno de los dos datos."),
    ],
    Z=[
        ("Un equipo ve que su alternativa favorita perdería. Entonces baja el peso del costo de 3 a 1. ¿Es válido?", "No: los pesos se fijan antes de puntuar, según la necesidad", "Cambiarlos al final es hacer trampa para que gane una idea."),
        ("Una alternativa suma el puntaje más alto, pero cuesta $18.000 y el presupuesto máximo es $15.000. ¿Se elige?", "No: se descarta porque incumple la restricción", "Las restricciones se aplican antes de la matriz."),
    ],
    D=[
        ("Criterios: costo (peso 3), impacto (peso 3), facilidad (peso 1). A: costo 2, impacto 3, facilidad 3. B: costo 3, impacto 2, facilidad 3. C: costo 3, impacto 3, facilidad 1. ¿Cuál suma más y cuántos puntos?", "C, 19 puntos", "A suma 18, B suma 18 y C suma 9 + 9 + 1 = 19."),
        arith("Una alternativa de ejemplo ahorra 120 hojas por semana y cuesta $2.400 en materiales. ¿Cuánto cuesta cada hoja ahorrada en 10 semanas?", "2400//(120*10)", "Se divide el costo entre el total de hojas ahorradas.", " pesos"),
    ],
    ctx=arith("En una encuesta de ejemplo a 40 estudiantes, 28 prefieren la alternativa de las tarjetas reutilizables. ¿Qué porcentaje es?", "28*100//40", "Se multiplica por 100 y se divide entre el total.", " %"),
    sc=[
        ("¿Qué se hace primero: descartar por restricción o puntuar?", "Descartar por restricción", "Lo que incumple una restricción no entra a la matriz."),
        ("¿Cómo se calcula el aporte de un criterio en la matriz?", "Peso × puntaje", "Así los criterios importantes influyen más."),
        ("Nombra una señal de que una fuente es poco confiable.", "No tiene autoría, fecha ni datos", "Sin esos datos no se puede comprobar."),
    ],
    open_task=(
        "Usa estos datos de ejemplo. Restricción: costo máximo $12.000. Alternativas: 1) guías impresas por ambos lados, $3.000, ahorro de papel alto; 2) tablero compartido digital, $0 en materiales, ahorro alto pero requiere conexión estable; 3) máquina nueva de reciclaje, $40.000. Descarta lo que incumple, fija pesos para costo, ahorro y facilidad, puntúa y escribe cuál recomiendas y qué información falta.",
        "Se descarta la 3 por costo; con pesos costo 3, ahorro 3, facilidad 2 se compara la 1 y la 2; se recomienda la que más sume y se anota que falta saber si todos tienen conexión estable",
        ["descarta por la restricción", "fija pesos antes de puntuar", "calcula peso × puntaje", "indica qué información falta"],
        ["hoja con la matriz y la recomendación"],
        ["sumar sin pesos", "cambiar los pesos al final"],
        "Pregunta: «¿qué alternativa quedó fuera y por qué restricción?». Debe poder señalarlo antes de mostrar los puntajes.",
    ),
    reinforce="Busca dos afirmaciones sobre ahorro de energía o materiales (una publicitaria y otra con datos) y compara si tienen autoría, fecha y método.",
    extend="Explica por qué fijar los pesos después de ver los resultados invalida una matriz de decisión.",
)

# ------------------------------------------------------------------ OA 02, clase 3
reg(
    OA2, 3,
    materials="Hoja, lápiz, regla y los casos escritos en este cuaderno.",
    use="Aprenderé a planificar tareas con responsables y tiempos, a calcular la duración de un plan y a representar un prototipo con un boceto a escala. Sirve para organizar el trabajo colaborativo antes de construir.",
    prior=["Sé elegir una alternativa con una matriz de decisión.", "Sé sumar tiempos.", "Sé usar una regla."],
    explain=[
        "Un plan se representa con una tabla de tareas: qué se hace, quién lo hace, cuánto dura y de qué tarea depende. «Depende de» significa que esa tarea no puede empezar hasta que termine otra. Dos tareas que no dependen una de la otra pueden hacerse al mismo tiempo, por personas distintas. La duración del plan es la de la ruta más larga, que es la cadena de tareas que van una tras otra.",
        "Para coordinar al equipo se usa un tablero compartido con tres columnas: por hacer, en curso y hecha. En un documento compartido se asignan permisos: el editor puede cambiar el contenido, el comentarista solo puede dejar comentarios y el lector solo puede leer. Así se evita que alguien borre sin querer una parte ajena.",
        "El prototipo se representa antes con un boceto rotulado, con las partes nombradas y las medidas. A veces se usa una escala: en la escala 1:3, cada centímetro del dibujo representa 3 centímetros reales. Para pasar de una medida real al dibujo se divide entre 3, y del dibujo a la realidad se multiplica por 3.",
    ],
    vocab=[("depende de", "tarea que no puede empezar hasta que otra termine"), ("ruta más larga", "cadena de tareas seguidas que fija la duración del plan"), ("tablero compartido", "lista de tareas por hacer, en curso y hechas"), ("permiso", "lo que una persona puede hacer en un archivo compartido"), ("boceto", "dibujo rotulado del prototipo antes de construirlo"), ("escala", "relación entre una medida del dibujo y la real")],
    worked=[
        ("Duración con tareas a la vez", "Tarea X: 1 h. Tarea Y: 2 h (después de X). Tarea Z: 3 h (después de X). Tarea W: 1 h (después de Y y Z). ¿Cuántas horas dura el plan?", ["Y y Z se hacen a la vez; manda la más larga, Z, de 3 h.", "La ruta más larga es X, Z y W: 1 + 3 + 1 = 5."], "5 horas"),
        ("Usar una escala", "Un dibujo mide 8 cm en escala 1:5. ¿Cuánto mide el objeto real?", ["Cada centímetro del dibujo representa 5 reales.", "Multiplico 8 × 5 = 40."], "40 cm"),
    ],
    mistakes=[
        ("Sumar la duración de todas las tareas, aunque algunas se hagan a la vez.", "El plan dura lo que dura su ruta más larga, no la suma de todo.", "Busca qué tareas pueden ir al mismo tiempo."),
        ("Dar a todo el equipo permiso de editor en todo el documento.", "Cualquiera puede borrar una parte ajena sin querer.", "Da permiso de editor solo en cada sección y de comentarista en el resto."),
    ],
    R=[
        ("En una tabla de tareas, la columna «depende de» indica… A) qué tarea debe estar terminada antes B) cuál tarea es la más difícil", "A", "Marca el orden obligatorio entre tareas."),
        ("Quien solo debe leer el documento compartido necesita permiso de… A) lector B) editor", "A", "El permiso de lector no permite cambiar el contenido."),
        arith("Plan en cadena de ejemplo: boceto 40 minutos, maqueta 90 minutos y prueba 30 minutos. ¿Cuántos minutos dura en total?", "40+90+30", "Al ir una tras otra, se suman.", " minutos"),
    ],
    C=[
        ("Las tareas B y C dependen de A, pero no entre sí. Después de A pueden hacerse… A) a la vez, por personas distintas B) solo una después de la otra", "A", "Sin dependencia entre ellas, no hay que esperar."),
        ("¿Por qué un plan debe incluir un responsable por tarea? A) para que cada tarea tenga quien responda y nadie espere que otro la haga B) para que sus nombres queden escritos", "A", "El responsable evita que una tarea quede sin hacer."),
        ("¿Qué debe llevar un boceto del prototipo? A) medidas y partes rotuladas B) solo el nombre del prototipo y su color", "A", "Con medidas y rótulos otro integrante puede construirlo."),
    ],
    A=[
        arith("Plan de ejemplo: boceto 2 h y lista de materiales 1 h, hechos a la vez por dos personas; luego la maqueta, 3 h. ¿Cuántas horas dura el plan?", "2+3", "Manda el boceto (2 h) y después se suma la maqueta.", " horas"),
        ("Tareas de ejemplo: a) probar la maqueta, b) dibujar el boceto, c) armar la maqueta. ¿Cuál es el orden correcto?", "b, c, a", "Primero se dibuja, luego se arma y al final se prueba."),
        arith("Una tarea de 120 minutos de trabajo se reparte en partes iguales entre 5 integrantes. ¿Cuántos minutos le tocan a cada uno?", "120//5", "Se divide el trabajo total entre las personas.", " minutos"),
    ],
    Z=[
        ("Un plan tiene 7 tareas y a Camila le asignan 6. ¿Cuál es el riesgo principal?", "Que todo el plan se atrase si ella no alcanza y que el resto no aporte", "Una carga desigual retrasa el plan y desaprovecha al equipo."),
        ("En un documento compartido todos tienen permiso de editor y alguien borra por error una sección. ¿Qué medida corresponde?", "Ajustar los permisos y recuperar la versión anterior desde el historial", "Los permisos limitan quién puede cambiar y el historial permite deshacer."),
    ],
    D=[
        arith("Plan de ejemplo: A dura 3 h; B, 2 h y C, 4 h (ambas después de A); D, 1 h (después de B y C). ¿Cuántas horas dura el plan?", "3+4+1", "La ruta más larga es A, C y D.", " horas"),
        arith("Otro plan: P dura 2 h; Q, 5 h y R, 3 h (ambas después de P); S, 2 h (después de Q y R). ¿Cuántas horas dura?", "2+5+2", "La ruta más larga pasa por Q.", " horas"),
    ],
    ctx=arith("El prototipo real de una caja organizadora mide 60 cm de largo. En un boceto a escala 1:3, ¿cuántos centímetros mide el dibujo?", "60//3", "Se divide la medida real entre 3.", " cm"),
    sc=[
        ("¿Cuánto dura un plan: lo que suman todas sus tareas o su ruta más larga?", "Su ruta más larga", "Las tareas independientes se hacen a la vez."),
        ("¿Qué puede hacer una persona con permiso de comentarista?", "Dejar comentarios sin cambiar el contenido", "No puede editar el texto."),
        ("En una escala 1:4, ¿cuánto mide en la realidad un dibujo de 5 cm?", "20 cm", "Se multiplica 5 × 4.", "5*4"),
    ],
    open_task=(
        "Usa este proyecto de ejemplo: una caja de papel para separar residuos en una sala. Tareas: boceto (2 h), lista de materiales (1 h), armado de la maqueta en cartón (3 h, depende del boceto y de la lista), prueba con 10 papeles (1 h, depende de la maqueta). Arma la tabla de tareas con responsable, duración y «depende de», calcula la duración del plan, dibuja un boceto rotulado con una medida en escala 1:2 y asigna permisos de documento a tres integrantes.",
        "Duración: 2 + 3 + 1 = 6 horas porque boceto y lista van a la vez; caja real de 30 cm de alto se dibuja de 15 cm; una persona editora por sección y las otras comentaristas",
        ["la tabla tiene responsable, duración y dependencia", "calcula bien la duración", "el boceto está rotulado y con escala", "asigna permisos con sentido"],
        ["hoja con tabla, boceto y permisos"],
        ["sumar todas las tareas", "dibujar sin medidas"],
        "Pregunta: «¿qué tareas se pueden hacer a la vez?». Debe notar que el boceto y la lista no dependen entre sí.",
    ),
    reinforce="Haz una tabla con tres tareas de una actividad de tu casa, con quién las hace y de cuál depende cada una.",
    extend="Explica por qué acortar una tarea que no está en la ruta más larga no acorta el plan.",
)

# ------------------------------------------------------------------ OA 02, clase 4
reg(
    OA2, 4,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. El prototipo, si se hace, es de papel y cartón, sin cortes con herramientas.",
    use="Aprenderé a construir un prototipo seguro y a trabajar en archivos compartidos cuidando versiones, permisos, datos personales y fuentes. Sirve para colaborar sin riesgos para las personas ni para el trabajo.",
    prior=["Sé planificar tareas con responsables.", "Sé que un permiso limita lo que alguien puede hacer.", "Sé que las cuentas son personales."],
    explain=[
        "Un prototipo es un modelo para probar una idea antes de fabricarla. En el colegio y en la casa se hace con materiales seguros: papel, cartón, cinta y objetos de reuso limpios. No se usa electricidad de red, no se manipulan herramientas cortantes ni productos químicos. Si una pieza necesita corte, se diseña con dobleces o se le pide al docente que la prepare.",
        "En un archivo compartido hay normas de cuidado. El historial de versiones permite volver a una versión anterior si algo se borra. Los nombres de archivo llevan fecha o número de versión. Cada persona usa su propia cuenta y no comparte su contraseña; lo que se comparte es el archivo, con permisos. Conviene guardar un respaldo en otro lugar.",
        "También hay normas éticas. No se suben fotos ni datos personales de compañeros sin su consentimiento. Las imágenes y los textos ajenos se citan con autor y fuente, y solo se usan si su licencia lo permite. Los datos se escriben tal como se midieron: inventarlos o maquillarlos engaña al equipo y a los usuarios.",
    ],
    vocab=[("prototipo", "modelo para probar una idea antes de fabricarla"), ("historial de versiones", "registro que permite volver a un estado anterior del archivo"), ("respaldo", "copia guardada en otro lugar"), ("consentimiento", "permiso claro de una persona para usar su imagen o datos"), ("cita", "mención del autor y la fuente de lo que se usa"), ("licencia", "permiso del autor que dice cómo se puede usar una obra")],
    worked=[
        ("Elegir material seguro", "Para una maqueta de un contenedor, ¿cuál es seguro: cartón con cinta o un cargador conectado al enchufe?", ["El cartón y la cinta no tienen riesgo eléctrico ni de corte.", "La electricidad de red no se manipula en una maqueta."], "Cartón con cinta"),
        ("Revisar un archivo compartido", "Un archivo se llama «final.doc», tiene una foto de un compañero sin permiso y una imagen sin fuente. ¿Qué tres cosas se corrigen?", ["Se nombra con versión y fecha.", "Se retira la foto o se pide consentimiento; se cita la imagen o se cambia."], "Nombre con versión, consentimiento para la foto y cita de la imagen"),
    ],
    mistakes=[
        ("Compartir la contraseña para que todos editen con la misma cuenta.", "No se sabe quién hizo cada cambio y se pierde el control de la cuenta.", "Cada persona usa su cuenta y se comparte el archivo con permisos."),
        ("Pensar que, si es un trabajo escolar, se puede copiar sin citar.", "El autor sigue siendo el autor, y copiar sin citar es engañar.", "Anota autor y fuente y verifica que se pueda usar."),
    ],
    R=[
        ("¿Qué material es seguro para hacer una maqueta en casa? A) cartón y cinta B) un cable conectado al enchufe", "A", "El cartón y la cinta no tienen riesgo eléctrico."),
        ("¿Para qué sirve el historial de versiones? A) para recuperar una versión anterior si algo se borra B) para impedir que otros comenten", "A", "Permite deshacer un error sin perder el trabajo."),
        ("Quieres subir al documento común una foto de un compañero. ¿Qué haces? A) pides su consentimiento antes B) la subes si salió bien", "A", "Una imagen personal solo se usa con permiso de la persona."),
    ],
    C=[
        ("¿Por qué no se comparte la contraseña con el equipo? A) porque la cuenta es personal y lo que se comparte es el archivo con permisos B) porque la contraseña ocupa mucho espacio", "A", "Compartir la cuenta impide saber quién hizo qué."),
        ("Una pieza del prototipo requiere cortar cartón grueso. ¿Qué es lo seguro? A) rediseñarla con dobleces o pedir al docente que la prepare B) cortarla con cualquier herramienta que haya", "A", "Las herramientas cortantes no se usan sin docente."),
        ("Quieres usar una imagen de otra persona en tu presentación. ¿Qué haces? A) anotas autor y fuente y verificas que se pueda usar B) la copias sin nombre porque es un trabajo escolar", "A", "La cita reconoce al autor y la licencia define el uso."),
    ],
    A=[
        arith("El equipo guarda una versión cada 25 minutos en una sesión de 100 minutos. ¿Cuántas versiones guarda?", "100//25", "Se divide el tiempo de la sesión entre el intervalo.", " versiones"),
        ("Acciones de ejemplo: (1) armar con cartón y cinta, (2) conectar una luz a un enchufe, (3) subir una foto con nombre completo de un compañero sin permiso, (4) guardar un respaldo del archivo, (5) pedir ayuda al docente. ¿Cuáles son inseguras o incorrectas?", "2 y 3", "Una conecta electricidad de red y la otra publica datos sin consentimiento."),
        arith("Cada prototipo necesita 3 cartones y el equipo quiere armar 4. Tiene 10 cartones. ¿Cuántos cartones le faltan?", "4*3-10", "Se calcula lo necesario y se resta lo que tiene.", " cartones"),
    ],
    Z=[
        ("Un compañero propone usar un cargador abierto como parte del prototipo «para que sea real». ¿Qué se responde?", "No: se usa una maqueta de papel del mismo tamaño, porque la electricidad de red no se manipula", "Un prototipo seguro representa el aparato sin riesgo."),
        ("Un integrante sobrescribió el archivo y se perdió la sección de otra persona, pero hay historial. ¿Qué se hace?", "Restaurar la versión anterior y acordar quién edita cada sección", "El historial permite recuperar y los acuerdos evitan repetirlo."),
    ],
    D=[
        arith("Se revisan 25 aportes del documento y 5 no tienen fuente. ¿Qué porcentaje no tiene fuente?", "5*100//25", "Se multiplica por 100 y se divide entre el total revisado.", " %"),
        arith("En una sesión de 80 minutos se destinan 5 revisiones de 4 minutos para chequear permisos y fuentes. ¿Qué porcentaje del tiempo es?", "5*4*100//80", "Se calcula el tiempo total de revisión y se pasa a porcentaje.", " %"),
    ],
    ctx=arith("Un equipo de ejemplo cumple 6 de las 8 normas de su lista de seguridad. ¿Qué porcentaje cumple?", "6*100//8", "Se multiplica por 100 y se divide entre el total de normas.", " %"),
    sc=[
        ("¿Qué se comparte en un trabajo colaborativo: la contraseña o el archivo con permisos?", "El archivo con permisos", "Cada cuenta es personal."),
        ("¿Qué se necesita antes de subir la foto de un compañero?", "Su consentimiento", "Es un dato personal."),
        ("Nombra un material seguro para un prototipo escolar.", "Cartón, papel o cinta", "No tienen riesgo eléctrico ni de corte."),
    ],
    open_task=(
        "Usa este caso de ejemplo: un equipo hace una maqueta de papel de un punto de acopio de pilas que sea seguro de usar, y comparte el informe en un documento. Escribe una lista de seguridad con seis normas (materiales, herramientas, electricidad, datos personales, fuentes y versiones), marca cuáles cumple este equipo según su descripción: «usó cartón y cinta, guardó la versión 2, subió una foto de un compañero sin avisar y copió una imagen sin citar», y explica cómo corregir lo que no cumple.",
        "Cumple materiales y versiones; no cumple datos personales (pedir consentimiento o retirar la foto) ni fuentes (citar autor y fuente)",
        ["la lista cubre las seis áreas", "identifica lo que cumple y lo que no", "propone una corrección concreta", "ninguna corrección propone electricidad de red ni herramientas cortantes"],
        ["hoja con lista y correcciones"],
        ["dejar una norma sin revisar", "proponer una corrección vaga"],
        "Pregunta: «¿qué haría exactamente el equipo mañana para corregirlo?». Pide una acción concreta por cada incumplimiento.",
    ),
    reinforce="Revisa un archivo escolar tuyo y anota cómo se llama, si cita sus fuentes y si tiene datos personales de alguien.",
    extend="Explica por qué compartir el archivo con permisos es más seguro que compartir una contraseña.",
)

# ------------------------------------------------------------------ OA 02, clase 5
reg(
    OA2, 5,
    materials="Hoja, lápiz, calculadora si la necesitas y los registros escritos en este cuaderno.",
    use="Aprenderé a probar una solución con mediciones antes y después, a calcular el porcentaje de reducción, a decidir si se cumplió la meta y a proponer una mejora. Sirve para demostrar con datos que la solución funciona.",
    prior=["Sé calcular promedios y porcentajes.", "Sé qué es una meta con indicador.", "Sé que una línea base se mide antes de actuar."],
    explain=[
        "Probar con evidencia es comparar la situación antes y después con el mismo indicador. La evidencia es un registro con fecha y cifras, no una sensación. El porcentaje de reducción se calcula así: (valor antes − valor después) × 100 ÷ valor antes. Una solución cumple la meta si su reducción es igual o mayor que la fijada.",
        "Una buena prueba cambia una sola cosa a la vez; si se cambian dos, no se sabe cuál produjo el resultado. También dura varios días, porque un solo día puede ser excepcional. Se registra todo en una planilla compartida, incluso los resultados malos, porque ayudan a mejorar.",
        "Si la meta no se cumple, no se ajustan los números: se revisa con los datos qué parte falló, se cambia una cosa y se prueba de nuevo. Además se miran los efectos no deseados, como un aumento del tiempo de trabajo. Al final el equipo comunica el resultado con honestidad: lo logrado y lo que falta.",
    ],
    vocab=[("prueba", "medición de la solución para ver si logra la meta"), ("evidencia", "registro con fecha y cifras de lo que ocurrió"), ("porcentaje de reducción", "(antes − después) × 100 ÷ antes"), ("meta", "reducción que se quiere lograr con el indicador"), ("efecto no deseado", "consecuencia negativa que aparece al aplicar la solución"), ("mejora", "ajuste que se prueba tras revisar los datos")],
    worked=[
        ("Calcular la reducción", "Antes de la solución se usaban 150 hojas por semana y después 120. ¿Qué porcentaje se redujo?", ["Diferencia: 150 − 120 = 30.", "Cálculo: 30 × 100 ÷ 150 = 20."], "20 %"),
        ("Decidir si se cumplió la meta", "La meta era 25 % y el resultado fue 20 %. ¿Se cumplió? ¿Qué se hace?", ["20 es menor que 25, así que no se cumplió.", "Se revisan los datos, se cambia una cosa y se prueba otra vez."], "No se cumplió; se ajusta y se prueba de nuevo"),
    ],
    mistakes=[
        ("Decir «funcionó» porque al equipo le pareció que mejoró.", "Una sensación no es evidencia y no se puede comprobar.", "Compara cifras antes y después con el mismo indicador."),
        ("Cambiar tres cosas a la vez y concluir que la solución funciona.", "No se sabe cuál de los cambios produjo el resultado.", "Cambia una cosa por vez y registra cada resultado."),
    ],
    R=[
        ("Para saber si algo mejoró se necesita… A) una medición antes y otra después con el mismo indicador B) la opinión de quien diseñó la solución", "A", "Solo las cifras comparables permiten afirmarlo."),
        arith("Antes se usaban 80 hojas por día y después 60. ¿Qué porcentaje se redujo?", "(80-60)*100//80", "Se divide la diferencia entre el valor inicial.", " %"),
        ("La meta era reducir 30 % y se logró 22 %. ¿Se cumplió la meta? A) sí B) no", "B", "22 es menor que 30."),
    ],
    C=[
        ("¿Por qué se cambia una sola cosa a la vez al probar? A) para saber qué cambio produjo el resultado B) para gastar menos papel", "A", "Con dos cambios no se puede separar el efecto de cada uno."),
        ("Un equipo probó un solo día y dijo «funciona». ¿Por qué es débil? A) un día no muestra si el resultado se repite B) un día cuesta más dinero", "A", "Un día puede ser excepcional."),
        ("¿Qué es evidencia? A) un registro con fecha y cifras de la prueba B) la sensación del grupo", "A", "La evidencia se puede revisar por otras personas."),
    ],
    A=[
        arith("Registro de ejemplo de hojas usadas en 5 días con la solución: 35, 30, 28, 32 y 25. ¿Cuál es el promedio diario?", "(35+30+28+32+25)//5", "Se suman los cinco días y se divide entre 5.", " hojas"),
        arith("Otro equipo usaba 50 hojas por día y con su solución usa un promedio de 35. ¿Qué porcentaje redujo?", "(50-35)*100//50", "Se calcula la diferencia sobre el valor inicial.", " %"),
        arith("La línea base es de 60 vasos por día y la meta es bajar 20 %. ¿Cuál es el máximo de vasos para cumplirla?", "60-60*20//100", "Se resta de la línea base el 20 %.", " vasos"),
    ],
    Z=[
        ("Un equipo dice que su solución mejoró mucho, pero sus datos son 52 hojas antes y 51 después. ¿Se puede afirmar una mejora importante?", "No: la diferencia es 1 hoja, cerca de 2 %, y faltan más días de registro", "Una diferencia tan pequeña puede ser casualidad."),
        ("El resultado no alcanza la meta. ¿Cuál es la reacción correcta?", "Revisar con los datos qué falló, cambiar una cosa y probar de nuevo", "No se cambian las cifras: se mejora la solución."),
    ],
    D=[
        arith("Con la solución, las hojas bajaron de 60 a 45 por día, pero el tiempo de trabajo subió de 30 a 33 minutos. ¿En qué porcentaje aumentó el tiempo?", "(33-30)*100//30", "Se calcula el aumento sobre el valor inicial.", " %"),
        ("Línea base: 80 hojas por semana. Meta: bajar 25 %. Resultados de tres semanas: 70, 64 y 58. ¿En qué semana se cumple la meta por primera vez?", "En la semana 3", "La meta es 60 hojas o menos y solo 58 la cumple."),
    ],
    ctx=arith("Un equipo ahorra 20 hojas por semana. Si mantiene el resultado 12 semanas, ¿cuántas hojas ahorra?", "20*12", "Se multiplica el ahorro semanal por las semanas.", " hojas"),
    sc=[
        ("¿Cómo se calcula el porcentaje de reducción?", "(antes − después) × 100 ÷ antes", "Es la fórmula de la clase."),
        ("¿Qué se hace si la meta no se cumple?", "Revisar qué falló, cambiar una cosa y probar de nuevo", "Se mejora con base en datos."),
        ("¿Por qué conviene registrar también los resultados malos?", "Porque ayudan a saber qué mejorar", "Ocultarlos impide corregir."),
    ],
    open_task=(
        "Usa este registro de ejemplo. Un curso quiere bajar 25 % sus hojas por día. Antes: 40, 44, 36, 40, 40 hojas. Con la solución: 36, 30, 32, 28, 34 hojas. Calcula el promedio antes, el promedio después y el porcentaje de reducción, decide si cumplió la meta y propone una mejora que cambie una sola cosa. Escribe también un posible efecto no deseado que habría que medir.",
        "Antes: 40 hojas de promedio; después: 32; reducción: 20 %; no cumple la meta de 25 %; mejora: cambiar solo el uso del reverso de las hojas; efecto no deseado: más tiempo de revisión",
        ["calcula los dos promedios", "calcula el porcentaje", "decide con la meta y no con una sensación", "propone una sola mejora y un efecto por medir"],
        ["hoja con cálculos y conclusión"],
        ["cambiar varias cosas a la vez", "decidir sin comparar con la meta"],
        "Pregunta: «¿qué número usaste para decidir si cumplió?». Debe ser el porcentaje de reducción frente a la meta.",
    ),
    reinforce="Mide durante tres días cuántas hojas o bolsas usas en tu casa, anota las cifras y calcula el promedio.",
    extend="Explica por qué una prueba de un solo día no basta para afirmar que una solución funciona.",
)
