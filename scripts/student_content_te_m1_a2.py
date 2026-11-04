"""Cuaderno del estudiante, 1.º medio Tecnología: OA 03 (evaluación y mejora técnica y valórica de un servicio, clases 1 a 5) y OA 04 (comunicación del diseño y desarrollo para distintas audiencias, clases 1 a 4).

Seguridad: las tareas son de lectura, cálculo y escritura; no se manipulan herramientas ni materiales.
Cifras enteras. Los resultados, los tiempos y los porcentajes son inventados («de ejemplo») para practicar y no nombran marcas ni personas reales. Las herramientas se nombran por tipo (planilla, presentación, diagrama).
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_content_te_m1_a import reg
from student_lessons import arith, ex

OA3 = "TE1M OA 03"
OA4 = "TE1M OA 04"

# ------------------------------------------------------------------ OA 03, clase 1
reg(
    OA3, 1,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a distinguir criterios propios, técnicos y valóricos para evaluar un servicio, y a separar la evaluación del proceso de la del producto final. Sirve para juzgar un servicio con razones y no solo con gustos.",
    prior=["Sé que un criterio necesita indicador y umbral.", "Sé describir el flujo de un servicio.", "Sé calcular porcentajes."],
    explain=[
        "Evaluar un servicio es juzgar, con criterios y evidencia, si cumple su propósito y qué se puede mejorar. Los criterios propios son los que el equipo y los usuarios consideran importantes según sus expectativas, como «que sea simple de usar». Los criterios técnicos se pueden medir: tiempo de respuesta, porcentaje de solicitudes atendidas, errores, horas de disponibilidad o costo.",
        "Los criterios valóricos revisan si el servicio respeta valores como el respeto, la honestidad, la privacidad, el cuidado del ambiente y la equidad, que significa que todos puedan acceder aunque partan de situaciones distintas. Un valor se evalúa con preguntas que se pueden observar, por ejemplo: ¿alguien quedó fuera por no tener internet?",
        "También se distingue qué se evalúa. El proceso es cómo se presta el servicio: orden de los pasos, roles y tiempos. El producto final es lo que recibe el usuario: el apunte entregado, la respuesta o la ayuda. Un servicio puede tener un buen producto final y un mal proceso, o al revés, por eso se evalúan las dos cosas.",
    ],
    vocab=[("criterio propio", "el que el equipo y los usuarios consideran importante según sus expectativas"), ("criterio técnico", "el que se puede medir, como un tiempo o un porcentaje"), ("criterio valórico", "el que revisa si se respetan valores"), ("equidad", "que todos puedan acceder aunque partan de situaciones distintas"), ("proceso", "cómo se presta el servicio"), ("producto final", "lo que recibe el usuario")],
    worked=[
        ("Clasificar criterios", "Clasifica en propio, técnico o valórico: (a) «al menos 90 % de las solicitudes atendidas en 2 días», (b) «que quienes no tienen celular también puedan pedir el servicio», (c) «que el equipo se sienta cómodo trabajando así».", ["(a) se mide con un porcentaje: técnico.", "(b) protege el acceso de todos: valórico (equidad). (c) depende de lo que siente el equipo: propio."], "(a) técnico, (b) valórico, (c) propio"),
        ("Proceso o producto final", "Clasifica: (a) «los apuntes entregados están completos y se leen bien», (b) «cada solicitud se registra en menos de 2 minutos».", ["(a) es lo que recibe el usuario: producto final.", "(b) es una forma de trabajar del equipo: proceso."], "(a) producto final, (b) proceso"),
    ],
    mistakes=[
        ("Evaluar un servicio solo con «me gustó».", "Es un criterio propio sin evidencia ni medida.", "Agrega al menos un criterio técnico y uno valórico."),
        ("Creer que lo valórico no se puede evaluar.", "Los valores se evalúan con preguntas observables.", "Pregunta si hubo consentimiento, si alguien quedó fuera o si se cumplió lo prometido."),
    ],
    R=[
        ("¿Qué tipo de criterio es «tiempo de respuesta menor a 2 días»? A) técnico B) valórico", "A", "Se puede medir con un número."),
        ("El criterio «todos pueden usar el servicio, tengan o no internet» expresa el valor de la…", "Equidad", "Busca que nadie quede fuera por su situación."),
        ("¿Qué se evalúa cuando se mira el proceso? A) cómo se presta el servicio B) lo que el usuario recibe al final", "A", "El proceso son los pasos, roles y tiempos."),
    ],
    C=[
        ("Criterio: «que el usuario sea tratado con respeto». ¿Es técnico o valórico?", "Valórico", "Se refiere a un valor y no a una medida."),
        ("Un equipo mide cuántas solicitudes atiende por hora. ¿Qué tipo de criterio usa? A) técnico B) propio", "A", "Es una medida de rendimiento."),
        ("Dos criterios: (1) «las 40 hojas de apuntes entregadas están completas», (2) «cada solicitud se registra en menos de 2 minutos». ¿Cuál evalúa el producto final y cuál el proceso?", "1 el producto final y 2 el proceso", "El primero mira lo entregado; el segundo, cómo trabaja el equipo."),
    ],
    A=[
        ("Clasifica cada criterio en propio, técnico o valórico: (1) que el servicio sea simple de usar según el equipo, (2) 95 % de las solicitudes respondidas en 1 día, (3) no se publican datos personales sin consentimiento.", "1 propio, 2 técnico, 3 valórico", "Expectativa del equipo, medida con porcentaje y valor de privacidad."),
        arith("Un servicio abre 3 horas por día durante 4 días a la semana. ¿Cuántas horas de disponibilidad tiene por semana?", "3*4", "Se multiplican las horas diarias por los días.", " horas"),
        arith("De 40 solicitudes de ejemplo, 34 se respondieron dentro del plazo. ¿Qué porcentaje cumplió el plazo?", "34*100//40", "Se calcula cuántas de cada 100 cumplieron.", " %"),
    ],
    Z=[
        ("Un equipo dice «nuestro servicio es excelente» sin medir nada, porque «nos gusta». ¿Qué tipo de criterio usó y qué le falta?", "Solo criterios propios; le faltan técnicos y valóricos con evidencia", "El gusto del equipo no demuestra que se cumpla el propósito."),
        ("Un servicio responde al 100 % de las solicitudes en 1 día, pero exige a todos entregar su dirección y teléfono sin necesidad. ¿Qué tipo de criterio incumple?", "Valórico, el de la privacidad", "Cumple lo técnico, pero pide datos que no hacen falta."),
    ],
    D=[
        arith("Un servicio estuvo disponible 12 horas por semana y atendió 36 solicitudes. En promedio, ¿cuántas solicitudes atendió por hora?", "36//12", "Se divide el total de solicitudes entre las horas.", " solicitudes"),
        ("Un equipo evalúa con tres criterios: el técnico se cumple, el propio se cumple y el valórico no. Su regla dice que solo se aprueba si se cumplen los tres tipos. ¿Se aprueba y qué se hace?", "No se aprueba; se mejora lo valórico", "Falla un tipo de criterio y la regla exige los tres."),
    ],
    ctx=ex("Un servicio de ejemplo respondió 45 de 50 solicitudes dentro del plazo. ¿Qué porcentaje es y qué tipo de criterio usó el equipo?", "90 %; técnico", "Se calcula 45 × 100 ÷ 50 = 90, y es una medida.", calc="45*100//50"),
    sc=[
        ("¿Qué es un criterio técnico?", "Uno que se puede medir", "Por ejemplo, un tiempo o un porcentaje."),
        ("¿Qué es el producto final de un servicio?", "Lo que recibe el usuario", "Es el resultado de la atención."),
        ("¿Qué quiere decir equidad?", "Que todos puedan acceder aunque partan de situaciones distintas", "Es un valor que se evalúa en el acceso."),
    ],
    open_task=(
        "Servicio de ejemplo: «Apuntes para quienes faltan»; un equipo de 4 estudiantes reúne los apuntes de la clase y los entrega en una carpeta digital o en papel dentro de 2 días. Escribe seis criterios para evaluarlo: dos propios, dos técnicos (con indicador y umbral) y dos valóricos (con una pregunta observable). Indica de cada uno si evalúa el proceso o el producto final.",
        "Propio 1: que los apuntes sean fáciles de leer (producto). Propio 2: que el equipo se organice sin discutir (proceso). Técnico 1: al menos 90 % de las ausencias con apuntes entregados en 2 días (proceso). Técnico 2: apuntes completos en al menos 95 % de las hojas de la clase (producto). Valórico 1: nadie queda sin apuntes por no tener internet; ¿hubo alternativa en papel? (proceso). Valórico 2: ¿se cumplió lo prometido en el afiche? (producto)",
        ["dos criterios de cada tipo", "los técnicos tienen indicador y umbral", "los valóricos tienen pregunta observable", "indica proceso o producto en cada uno"],
        ["lista de seis criterios con su clasificación"],
        ["criterio técnico sin cifra", "criterio valórico que es solo una opinión"],
        "Pregunta: «¿cómo sabrías en la práctica si este criterio se cumple?». Si no puede responder, el criterio no está bien escrito.",
    ),
    reinforce="Elige un servicio que uses y anota un criterio propio, uno técnico y uno valórico con que lo evaluarías.",
    extend="Explica por qué un servicio rápido puede, aun así, ser un mal servicio.",
)

# ------------------------------------------------------------------ OA 03, clase 2
reg(
    OA3, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y los registros escritos en este cuaderno.",
    use="Aprenderé a registrar datos de una prueba del servicio y a resumirlos con promedio, rango y porcentaje. Sirve para evaluar con números honestos y no con impresiones.",
    prior=["Sé qué es un indicador y un umbral.", "Sé calcular porcentajes.", "Sé sumar y dividir enteros."],
    explain=[
        "Para evaluar un criterio técnico se recogen datos durante una prueba del servicio. Un registro simple anota la fecha, el tiempo de respuesta, si la solicitud quedó resuelta y, si se quiere, una nota de satisfacción de 1 a 5, donde 5 es la más alta. No se registran nombres ni teléfonos: solo lo que hace falta para evaluar.",
        "Los datos se resumen con algunos números. El promedio es la suma de los datos dividida entre cuántos son. El máximo y el mínimo son el dato mayor y el menor. El rango es máximo menos mínimo y muestra cuánto varían los datos. El porcentaje dice cuántos de cada 100 cumplieron algo. El promedio solo no basta: un dato muy distinto puede quedar escondido en él.",
        "La evaluación es honesta cuando se anotan todos los resultados, también los malos. Ocultar las fallas impide mejorar y engaña a quien lee el informe. Si un resultado no cumple el umbral, se anota igual y se busca su causa.",
    ],
    vocab=[("registro", "tabla donde se anotan los datos de la prueba"), ("promedio", "suma de los datos dividida entre cuántos son"), ("máximo y mínimo", "el dato mayor y el menor"), ("rango", "máximo menos mínimo"), ("satisfacción", "nota de 1 a 5 que da el usuario"), ("evaluación honesta", "la que anota todos los resultados, también los malos")],
    worked=[
        ("Calcular un promedio", "Tiempos de respuesta de cuatro solicitudes de ejemplo, en horas: 3, 5, 8 y 4. ¿Cuál es el promedio?", ["Sumo: 3 + 5 + 8 + 4 = 20.", "Divido entre 4 datos: 20 ÷ 4 = 5."], "5 horas"),
        ("Resumir notas de satisfacción", "Cinco usuarios dieron estas notas de 1 a 5: 5, 4, 4, 3 y 4. ¿Qué porcentaje dio 4 o más?", ["Cuento las notas de 4 o más: 5, 4, 4 y 4, o sea 4 de 5.", "Calculo 4 × 100 ÷ 5 = 80."], "80 %"),
    ],
    mistakes=[
        ("Informar solo el promedio.", "Un dato muy distinto queda escondido y el promedio no lo muestra.", "Agrega el máximo, el mínimo o el rango."),
        ("No anotar las fallas «porque quedan mal».", "Sin ellas no se sabe qué mejorar y la evaluación no es honesta.", "Anota todos los resultados."),
    ],
    R=[
        arith("Los tiempos de respuesta (en horas) fueron 2, 4 y 6. ¿Cuál es el promedio?", "(2+4+6)//3", "Se suman y se divide entre 3 datos.", " horas"),
        arith("Con tiempos de 3, 9 y 6 horas, ¿cuál es el rango (máximo menos mínimo)?", "9-3", "El mayor es 9 y el menor es 3.", " horas"),
        arith("Una usuaria dio nota 2 y otro usuario dio nota 5 en la escala de 1 a 5. ¿Cuántos puntos de diferencia hay entre ambas notas?", "5-2", "Se resta la menor de la mayor.", " puntos"),
    ],
    C=[
        ("Un promedio de 6 horas, ¿puede esconder que una solicitud tardó 20 horas? A) sí, por eso conviene mirar también el máximo B) no, el promedio siempre lo muestra todo", "A", "Un dato extremo se diluye al promediar."),
        ("¿Qué columna sobra en un registro de la prueba? A) nombre y teléfono del usuario B) tiempo de respuesta", "A", "No se necesitan para evaluar y exponen la privacidad."),
        ("Tiempos de cuatro solicitudes: 3, 12, 3 y 6 horas. ¿Cuál es el mínimo y cuál el máximo?", "Mínimo 3 y máximo 12", "Son el menor y el mayor de los datos."),
    ],
    A=[
        arith("Tiempos de respuesta de una prueba de ejemplo, en horas: 4, 10, 6, 2, 8 y 6. ¿Cuál es el promedio?", "(4+10+6+2+8+6)//6", "Se suman los seis datos y se divide entre 6.", " horas"),
        arith("Con los tiempos 4, 10, 6, 2, 8 y 6 horas, ¿cuál es el rango?", "10-2", "El máximo es 10 y el mínimo es 2.", " horas"),
        arith("Notas de satisfacción de ejemplo (1 a 5) de 10 usuarios: 5, 5, 4, 4, 4, 3, 5, 2, 4 y 4. ¿Qué porcentaje dio nota 4 o 5?", "8*100//10", "Se calcula cuántos de cada 100 dieron 4 o 5.", " %"),
    ],
    Z=[
        ("Un equipo informa «el tiempo promedio fue de 4 horas», pero los tiempos de cinco solicitudes fueron 1, 1, 1, 1 y 16. ¿Por qué el promedio puede engañar?", "Un solo dato de 16 horas lo sube; cuatro de cinco se atendieron en 1 hora", "La suma es 20 y 20 ÷ 5 = 4, pero ese valor no describe a ninguna solicitud típica."),
        ("Un equipo decide no anotar dos solicitudes que salieron mal. ¿Qué problema hay? A) falta honestidad y la evaluación queda incompleta B) ninguno, porque son pocas", "A", "Ocultar fallas impide mejorar y engaña a quien lee el informe."),
    ],
    D=[
        arith("Tiempos de respuesta en horas: la semana 1 tuvo 5, 7 y 6, y la semana 2 tuvo 4, 4 y 4. ¿En cuántas horas bajó el promedio de la semana 1 a la 2?", "(5+7+6)//3-(4+4+4)//3", "Los promedios son 6 y 4.", " horas"),
        ex("El umbral pide un promedio de satisfacción de al menos 4. Notas de seis usuarios: 5, 3, 4, 4, 3 y 5. ¿Cumple y cuál es el promedio?", "Sí, el promedio es 4", "Suman 24 y 24 ÷ 6 = 4, que alcanza el umbral.", calc="(5+3+4+4+3+5)//6"),
    ],
    ctx=arith("En una prueba de ejemplo, tres solicitudes tardaron 12, 8 y 10 horas en responderse. ¿Cuál es el promedio?", "(12+8+10)//3", "Se suman los tres tiempos y se divide entre 3.", " horas"),
    sc=[
        ("¿Cómo se calcula el rango?", "Máximo menos mínimo", "Muestra cuánto varían los datos."),
        ("¿Qué datos personales conviene anotar en un registro de prueba?", "Ninguno que no haga falta", "Se aplica el principio de datos mínimos."),
        ("¿Por qué se anotan también los resultados malos?", "Para poder mejorar y ser honestos", "Sin ellos la evaluación queda incompleta."),
    ],
    open_task=(
        "Escoge un registro de ejemplo. Registro 1: tiempos de respuesta en horas de 6 solicitudes: 8, 12, 6, 4, 10 y 8. Registro 2: notas de satisfacción de 8 usuarios: 5, 3, 4, 4, 2, 5, 4 y 5. Calcula promedio, máximo, mínimo y rango (registro 1) o promedio y porcentaje con 4 o más (registro 2). Compara con un umbral de ejemplo (registro 1: promedio de 8 horas o menos; registro 2: al menos 70 % con nota 4 o 5) y escribe si se cumple y qué dato te llama la atención.",
        "Registro 1: suma 48 y 48 ÷ 6 = 8 horas, que cumple el umbral de 8; máximo 12, mínimo 4 y rango 8. Llama la atención que una solicitud tardó 12 horas, el triple del mínimo",
        ["calcula bien cada estadístico", "compara con el umbral", "señala un dato llamativo", "no oculta resultados malos"],
        ["hoja con cálculos y conclusión"],
        ["calcular el rango con la suma", "informar solo el promedio"],
        "Pregunta: «¿hay algún dato que el promedio esté escondiendo?». Debe mirar máximo y mínimo.",
    ),
    reinforce="Anota durante tres días cuánto demoras en una tarea cotidiana y calcula el promedio y el rango.",
    extend="Explica por qué dos servicios con el mismo promedio pueden ser muy distintos para el usuario.",
)

# ------------------------------------------------------------------ OA 03, clase 3
reg(
    OA3, 3,
    materials="Hoja, lápiz, calculadora si la necesitas y los registros escritos en este cuaderno.",
    use="Aprenderé a comparar los resultados con lo planificado, a calcular la desviación y a buscar la causa de un problema en el proceso o en el producto final. Sirve para saber qué mejorar sin culpar a nadie.",
    prior=["Sé calcular promedio y porcentaje.", "Sé distinguir proceso de producto final.", "Sé qué es un umbral."],
    explain=[
        "Evaluar es comparar lo real con lo planificado. Si un indicador alcanza el umbral, el criterio se cumple; si no, hay una brecha que explicar. La desviación porcentual mide cuánto se alejó lo real de lo planificado: (real − planificado) × 100 ÷ planificado. Siempre se calcula sobre lo planificado.",
        "Cuando algo no se cumple se busca la causa en la evidencia: el registro de la prueba y la bitácora, que es el cuaderno donde el equipo anota lo que va ocurriendo. Hay que decidir si falló el proceso (cómo se trabajó: pasos, roles, registro, tiempos) o el producto final (lo que recibió el usuario: contenido, formato, claridad).",
        "Las causas se buscan en cómo está organizado el trabajo y no en las personas. Decir «fulano es irresponsable» no ayuda a mejorar; decir «no había reemplazo cuando faltó un encargado» sí. También conviene cambiar una cosa a la vez para saber cuál produjo la mejora.",
    ],
    vocab=[("brecha", "diferencia entre lo esperado y lo logrado"), ("desviación porcentual", "(real − planificado) × 100 ÷ planificado"), ("bitácora", "cuaderno donde se anota lo que ocurre"), ("causa", "razón por la que ocurrió un problema"), ("evidencia", "datos y registros que respaldan una conclusión")],
    worked=[
        ("Calcular la desviación", "Se planificó responder en 24 horas, pero en la prueba se respondió en 30 horas en promedio. ¿Cuál es la desviación porcentual?", ["Calculo la diferencia: 30 − 24 = 6 horas.", "La paso a porcentaje sobre lo planificado: 6 × 100 ÷ 24 = 25."], "25 % sobre lo planificado"),
        ("Ubicar la causa", "Bitácora de ejemplo: «el lunes llegaron 15 solicitudes y solo había 1 encargado; el martes no se anotaron 2 de ellas». ¿Falló el proceso o el producto final?", ["Los problemas son la falta de gente y el registro incompleto.", "Eso es de organización del trabajo, no del contenido entregado."], "Falló el proceso"),
    ],
    mistakes=[
        ("Buscar un culpable.", "No se corrige a una persona, sino la forma de trabajar.", "Pregunta qué parte del proceso permitió el error."),
        ("Cambiar varias cosas a la vez.", "Después no se sabe cuál produjo el cambio.", "Cambia una cosa y vuelve a medir."),
    ],
    R=[
        ("El umbral pide al menos 80 % y el resultado fue 72 %. ¿El criterio se cumple?", "No", "72 es menor que 80."),
        ("Las solicitudes se pierden porque nadie las anota. ¿Falló el proceso o el producto final?", "El proceso", "Es un problema de cómo se trabaja."),
        ("La desviación compara A) lo real con lo planificado B) a una persona con otra", "A", "Mide la distancia entre el resultado y el plan."),
    ],
    C=[
        ("¿Sobre qué valor se calcula la desviación porcentual? A) sobre el valor planificado B) sobre el valor real", "A", "La referencia es lo que se había propuesto."),
        ("Bitácora: «los apuntes se entregaron con las hojas desordenadas». ¿Qué falló, el proceso o el producto final?", "El producto final", "Es una falla de lo que recibió el usuario."),
        ("Para explicar un atraso conviene A) buscar la causa en el registro y la bitácora B) decidir quién tuvo la culpa", "A", "La evidencia muestra qué ocurrió sin culpar a nadie."),
    ],
    A=[
        arith("Se planificó atender cada solicitud en 20 minutos y en la prueba se tardaron 25 minutos. ¿Cuál es la desviación porcentual?", "(25-20)*100//20", "La diferencia se calcula sobre lo planificado.", " %"),
        arith("Se planificaron 40 atenciones y se hicieron 34. ¿Qué porcentaje de lo planificado no se hizo?", "(40-34)*100//40", "Faltaron 6 de 40.", " %"),
        ("Registro de problemas de una prueba: 5 solicitudes llegaron fuera de horario y no se atendieron, 3 se atendieron tarde y 12 salieron bien. ¿Cuál es la causa de problemas más frecuente?", "Las solicitudes fuera de horario", "Son 5, más que las 3 atendidas tarde."),
    ],
    Z=[
        ("El tiempo de respuesta subió de 6 a 9 horas y el equipo cambia de herramienta, de horario y de integrantes a la vez. ¿Qué problema tiene? A) no sabrá qué cambio mejoró o empeoró las cosas B) mejorará más rápido porque habrá más cambios", "A", "Cambiar varias cosas juntas impide ver el efecto de cada una."),
        ("Bitácora: «martes: faltaron 2 encargados; las solicitudes esperaron 2 días». Conclusión 1: los dos encargados son irresponsables. Conclusión 2: no había un reemplazo previsto. ¿Cuál se apoya en la evidencia?", "La 2", "La bitácora muestra falta de reemplazo; no dice nada sobre la responsabilidad personal."),
    ],
    D=[
        arith("Se planificaron 60 atenciones por semana. La semana 1 se hicieron 45 y la semana 2, 54. ¿Cuántos puntos porcentuales mejoró el cumplimiento?", "54*100//60-45*100//60", "El cumplimiento pasó de 75 % a 90 %.", " puntos"),
        ("Resultados de una prueba: tiempo promedio 30 horas (umbral: 24 horas como máximo), satisfacción promedio 4 (umbral: al menos 4) y 0 reclamos de privacidad (umbral: 0). ¿Qué umbrales se cumplen?", "Satisfacción y privacidad", "El tiempo de 30 horas supera el máximo de 24."),
    ],
    ctx=ex("Un servicio de ejemplo respondió en promedio en 18 horas cuando el plan era 12 horas. ¿Cuál es la desviación porcentual?", "50 %", "La diferencia es 6 horas y 6 × 100 ÷ 12 = 50.", calc="(18-12)*100//12"),
    sc=[
        ("En Tecnología: ¿Qué es una bitácora?", "Un cuaderno donde se anota lo que va ocurriendo", "Aporta evidencia para buscar causas."),
        ("¿Se buscan las causas en las personas o en la forma de trabajar?", "En la forma de trabajar", "Así se puede mejorar el proceso."),
        ("¿Cómo se calcula la desviación porcentual?", "(real − planificado) × 100 ÷ planificado", "Se calcula siempre sobre lo planificado."),
    ],
    open_task=(
        "Analiza este servicio de ejemplo. Plan: 4 hitos, respuesta en 24 horas y 50 atenciones por semana. Real: se cumplieron 3 hitos, la respuesta tardó 30 horas y se hicieron 40 atenciones. La bitácora dice: «día 2, el formulario se cayó y no se usó el plan B; día 4, un encargado faltó y nadie lo reemplazó». Calcula los tres porcentajes de desviación o cumplimiento, indica si cada causa es de proceso o de producto, y escribe una mejora para cada causa sin culpar a personas.",
        "Hitos: 75 % cumplidos; tiempo: +25 %; atenciones: 80 % del plan. Causas: formulario caído sin plan B (proceso); falta de reemplazo (proceso). Mejoras: tener formulario en papel y definir un reemplazo por turno",
        ["calcula los porcentajes", "usa la bitácora para las causas", "distingue proceso de producto", "propone mejoras sin culpar"],
        ["hoja con cálculos, causas y mejoras"],
        ["calcular la desviación sobre el valor real", "culpar a una persona"],
        "Pregunta: «¿esta causa habla de una persona o de cómo se organizó el trabajo?». Debe hablar de lo segundo.",
    ),
    reinforce="Recuerda una tarea que no saliste como planificaste y anota si falló el proceso o el producto final y por qué.",
    extend="Explica por qué es mejor cambiar una sola cosa a la vez después de una evaluación.",
)

# ------------------------------------------------------------------ OA 03, clase 4
reg(
    OA3, 4,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a evaluar un servicio desde sus valores, a reconocer un dilema entre criterios y a decidir con razones. Sirve para que la evaluación no mire solo la rapidez o el costo.",
    prior=["Sé qué es un criterio valórico.", "Sé calcular totales con pesos.", "Sé distinguir proceso de producto final."],
    explain=[
        "Evaluar con valores es revisar si el servicio respeta a las personas y al ambiente. Se traducen los valores en preguntas que se pueden observar: ¿se pidió consentimiento antes de usar una foto? (privacidad), ¿alguien quedó fuera por no tener internet? (equidad), ¿se cumplió lo que se prometió? (honestidad), ¿se evitaron residuos? (cuidado del ambiente).",
        "Un dilema ocurre cuando dos criterios chocan: por ejemplo, pedir muchos datos hace más rápida la atención pero afecta la privacidad. Para decidir se piensa a quién afecta cada opción, si el daño se puede reparar y si existe una alternativa que cumpla ambos criterios. Si no existe, se compara con pesos: cada criterio recibe un peso y cada opción un puntaje, y se suma peso × puntaje.",
        "Que un criterio técnico se cumpla no basta. Un servicio muy rápido que excluye a una parte de los usuarios no es un buen servicio. Por eso se evalúa lo técnico y lo valórico, y se deja registrado por qué se tomó cada decisión.",
    ],
    vocab=[("dilema", "situación en que dos criterios o valores chocan"), ("privacidad", "cuidado de los datos y la imagen de las personas"), ("equidad", "acceso para todos aunque partan de situaciones distintas"), ("honestidad", "cumplir lo que se dice y no ocultar fallas"), ("alternativa", "otra opción que resuelve el mismo problema"), ("peso", "importancia que se da a un criterio")],
    worked=[
        ("Resolver un dilema", "Para atender más rápido, un servicio pide la foto del carné de cada usuario. La atención baja de 4 a 2 horas. ¿Qué criterios chocan y qué alternativa hay?", ["Chocan la rapidez (técnico) y la privacidad (valórico): la foto es un dato que no hace falta.", "Una alternativa es pedir solo el curso y confirmar la identidad de otra forma, sin guardar la foto."], "Chocan rapidez y privacidad; conviene pedir solo el curso"),
        ("Detectar un riesgo de equidad", "Quienes piden por formulario digital reciben respuesta en 1 día y quienes piden en papel, en 4 días. ¿Qué valor está en riesgo?", ["Los dos grupos reciben un trato distinto por el medio que usan.", "Eso afecta la igualdad de acceso."], "La equidad"),
    ],
    mistakes=[
        ("Pensar que la rapidez siempre vale más que la privacidad.", "Un dato entregado de más puede causar un daño que no se repara.", "Pondera los criterios y busca una alternativa."),
        ("Evaluar los valores con «me parece».", "Una opinión sin evidencia no sirve para decidir.", "Usa preguntas observables."),
    ],
    R=[
        ("El valor de que todos puedan acceder aunque no tengan internet es A) la equidad B) la rapidez", "A", "Busca que nadie quede fuera por su situación."),
        ("Pedir permiso antes de usar la foto de alguien protege su… A) privacidad B) equidad", "A", "La imagen es un dato personal."),
        ("Un servicio promete una cosa y entrega otra. ¿Qué valor falla?", "La honestidad", "Se dijo algo que no se cumplió."),
    ],
    C=[
        ("¿Cuál es una pregunta observable para evaluar la equidad? A) ¿alguien quedó fuera por no tener internet? B) ¿el afiche es bonito?", "A", "Se puede comprobar con hechos."),
        ("Un dilema ocurre cuando A) dos criterios o valores chocan B) el servicio no tiene usuarios", "A", "Cumplir uno afecta al otro."),
        ("Existe una alternativa que cumple la rapidez y la privacidad a la vez. ¿Qué conviene hacer? A) usarla antes de sacrificar uno de los dos B) elegir siempre lo más rápido", "A", "Si se puede cumplir ambos, no hay que renunciar a ninguno."),
    ],
    A=[
        ("Relaciona cada pregunta con un valor (equidad, honestidad o privacidad): (1) ¿el afiche promete algo que el equipo puede cumplir?, (2) ¿se borran las direcciones al terminar?, (3) ¿los usuarios sin celular tienen otra forma de pedir?", "1 honestidad, 2 privacidad, 3 equidad", "Cada pregunta revisa un valor distinto."),
        ex("Pesos: privacidad 3 y rapidez 2. Opción X: privacidad 1 y rapidez 3. Opción Y: privacidad 3 y rapidez 1. ¿Cuál tiene el mayor total ponderado y cuánto es?", "Y, con 11", "X suma 3 + 6 = 9 e Y suma 9 + 2 = 11.", calc="3*3+2*1"),
        arith("De 40 solicitudes de ejemplo, 12 llegaron en papel y 6 de ellas se atendieron tarde. ¿Qué porcentaje de las solicitudes en papel se atendió tarde?", "6*100//12", "Se calcula sobre las 12 solicitudes en papel.", " %"),
    ],
    Z=[
        ("Un equipo elimina el formulario en papel para ahorrar tiempo de registro. ¿Qué valor sacrifica? A) la equidad B) la honestidad", "A", "Quienes no tienen internet quedan sin forma de pedir."),
        ("Para evitar solicitudes falsas, la propuesta 1 pide RUT y dirección; la propuesta 2 pide solo el curso y lo confirma con el profesor jefe. ¿Cuál respeta mejor la privacidad?", "La propuesta 2", "Logra el mismo objetivo con menos datos personales."),
    ],
    D=[
        ex("Pesos: privacidad 3, equidad 3 y rapidez 1. Puntajes en el orden privacidad, equidad, rapidez: opción M, 3, 1 y 3; opción N, 2, 3 y 1; opción O, 3, 2 y 2. ¿Cuál gana y con cuántos puntos?", "O, con 17", "M suma 9 + 3 + 3 = 15; N, 6 + 9 + 1 = 16; O, 9 + 6 + 2 = 17.", calc="3*3+3*2+1*2"),
        ex("Un servicio atendió 50 solicitudes de ejemplo y registró consentimiento en 45. El umbral valórico pide 100 %. ¿Cumple y qué porcentaje alcanzó?", "No cumple; alcanzó 90 %", "45 × 100 ÷ 50 = 90, que es menor que 100.", calc="45*100//50"),
    ],
    ctx=ex("De 50 solicitudes de ejemplo, 8 se pidieron en papel y esperaron 3 días; 42 se pidieron por chat y esperaron 1 día. ¿Qué valor está en riesgo y cuántos días más esperan quienes piden en papel?", "La equidad; 2 días más", "El medio de pedido genera un trato distinto: 3 − 1 = 2.", calc="3-1"),
    sc=[
        ("En Tecnología: ¿Qué es un dilema?", "Una situación en que dos criterios o valores chocan", "Obliga a ponderar y decidir con razones."),
        ("¿Cómo se evalúa un valor?", "Con preguntas que se pueden observar", "Así se apoya en hechos."),
        ("¿Basta que el servicio sea rápido para aprobarlo?", "No", "También deben cumplirse los criterios valóricos."),
    ],
    open_task=(
        "Dilema de ejemplo: un servicio de tutorías entre compañeros puede (opción 1) pedir a cada estudiante nombre completo, RUT y teléfono para evitar abusos y atender en 1 día, o (opción 2) pedir solo curso y materia, confirmar con el profesor jefe y atender en 2 días. Pesos: privacidad 3, rapidez 2, equidad 3. Puntajes de ejemplo: opción 1, privacidad 1, rapidez 3, equidad 2; opción 2, privacidad 3, rapidez 2, equidad 3. Calcula los totales, decide y justifica en cuatro oraciones, indicando a quién afecta cada opción.",
        "Opción 1: 3×1 + 2×3 + 3×2 = 15. Opción 2: 3×3 + 2×2 + 3×3 = 22. Se elige la opción 2: protege los datos de todos y no deja fuera a nadie, aunque demora un día más. La opción 1 afecta sobre todo a quienes entregan datos sin necesidad",
        ["calcula los totales", "decide según el resultado", "indica a quién afecta cada opción", "justifica con valores"],
        ["hoja con cálculos y justificación"],
        ["elegir solo por rapidez", "no mencionar quién se ve afectado"],
        "Pregunta: «¿quién sale perjudicado con la opción que elegiste y puedes reducir ese daño?».",
    ),
    reinforce="Piensa en un servicio que uses y anota una situación en que la rapidez choque con la privacidad.",
    extend="Explica por qué, ante un dilema, conviene buscar una alternativa antes de sacrificar un valor.",
)

# ------------------------------------------------------------------ OA 03, clase 5
reg(
    OA3, 5,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a proponer mejoras al proceso y al producto final, a priorizarlas y a comprobar con una nueva prueba si funcionaron. Sirve para cerrar el ciclo de evaluar y mejorar.",
    prior=["Sé calcular desviación y porcentaje.", "Sé distinguir proceso de producto final.", "Sé buscar causas con evidencia."],
    explain=[
        "Una mejora es un cambio concreto que ataca una causa encontrada en la evaluación. Se escribe así: «Si [cambio], entonces [indicador] pasará de [valor actual] a [valor esperado]». «Trabajar mejor» no es una mejora, porque no dice qué cambiar ni cómo se comprobará. La mejora del proceso cambia cómo se presta el servicio (orden, roles, tiempos); la del producto cambia lo que recibe el usuario (contenido, formato, claridad).",
        "Cuando hay varias mejoras se priorizan por impacto, que es cuánto mejora el indicador, y por esfuerzo, que es cuánto tiempo, dinero o trabajo cuesta. Se hace primero la de mayor impacto y, si empatan, la de menor esfuerzo. Después se hace una nueva prueba y se compara el antes y el después: la mejora porcentual de un tiempo que baja es (antes − después) × 100 ÷ antes.",
        "Una mejora puede arreglar un indicador y empeorar otro. Por eso se revisan de nuevo los criterios técnicos y los valóricos. Lo que funcionó se conserva, y lo aprendido se anota en la bitácora para la siguiente versión del servicio.",
    ],
    vocab=[("mejora", "cambio concreto que ataca una causa"), ("impacto", "cuánto mejora un indicador"), ("esfuerzo", "cuánto tiempo, dinero o trabajo cuesta"), ("antes y después", "comparación entre la prueba inicial y la nueva"), ("mejora porcentual", "(antes − después) × 100 ÷ antes, si el valor baja")],
    worked=[
        ("Priorizar mejoras", "Regla: primero el mayor impacto y, si empatan, el menor esfuerzo. Mejora P: impacto 3, esfuerzo 1. Mejora Q: impacto 3, esfuerzo 3. Mejora R: impacto 1, esfuerzo 1. ¿Cuál se hace primero?", ["P y Q tienen el mayor impacto, 3.", "Entre ellas, P tiene menor esfuerzo."], "La mejora P"),
        ("Medir la mejora", "El tiempo promedio bajó de 20 a 15 horas tras un cambio. ¿Qué porcentaje mejoró?", ["La diferencia es 20 − 15 = 5 horas.", "La paso a porcentaje del valor de antes: 5 × 100 ÷ 20 = 25."], "25 %"),
    ],
    mistakes=[
        ("Proponer mejoras vagas como «trabajar mejor».", "No dicen qué cambiar ni cómo comprobar el resultado.", "Escribe «si cambio X, el indicador pasará de A a B»."),
        ("No volver a probar después de mejorar.", "Sin nueva prueba no se sabe si funcionó.", "Repite la medición y compara."),
    ],
    R=[
        ("¿Cuál es una mejora concreta? A) «Si se asigna un reemplazo por turno, las solicitudes sin atender bajarán de 8 a 2.» B) «Hay que trabajar mejor.»", "A", "Dice qué cambiar y cómo se medirá."),
        ("Cambiar el orden de los pasos de atención, ¿mejora el proceso o el producto final?", "El proceso", "Cambia cómo se presta el servicio."),
        ("Escribir los apuntes con letra más grande para que se lean mejor, ¿mejora el proceso o el producto final?", "El producto final", "Cambia lo que recibe el usuario."),
    ],
    C=[
        ("¿Qué mejora conviene hacer primero? A) la de alto impacto y poco esfuerzo B) la de bajo impacto y mucho esfuerzo", "A", "Da más resultado con menos costo."),
        ("¿Para qué se repite la prueba después de una mejora? A) para comprobar con datos si mejoró el indicador B) para cambiar el criterio", "A", "La nueva medición confirma o descarta el cambio."),
        ("El tiempo de respuesta bajó de 20 a 15 horas. Si menos tiempo es mejor, ¿mejoró o empeoró?", "Mejoró", "El tiempo es menor que antes."),
    ],
    A=[
        arith("El tiempo promedio de respuesta bajó de 30 a 24 horas. ¿Qué porcentaje mejoró?", "(30-24)*100//30", "La diferencia se calcula sobre el valor de antes.", " %"),
        arith("Las solicitudes sin atender eran 12 por semana y con la mejora son 3. ¿Qué porcentaje bajaron?", "(12-3)*100//12", "Bajaron 9 de 12.", " %"),
        ("Regla: mayor impacto y, si empatan, menor esfuerzo. Mejora A: impacto 3, esfuerzo 2. Mejora B: impacto 2, esfuerzo 1. Mejora C: impacto 3, esfuerzo 1. ¿Cuál se hace primero?", "C", "A y C empatan en impacto 3 y C requiere menos esfuerzo."),
    ],
    Z=[
        ("Los datos muestran que 8 de 20 solicitudes se pierden por falta de registro, pero el equipo propone agregar 10 funciones nuevas y un logo. ¿Qué falla? A) la propuesta no ataca la causa que muestran los datos B) no incluye ninguna mejora del producto final", "A", "Una mejora debe responder a la causa encontrada."),
        ("Con una mejora el tiempo bajó de 24 a 18 horas, pero ahora 6 de 30 usuarios dicen no haber entendido la respuesta. ¿Qué indica? A) mejoró el proceso, pero el producto final necesita ajuste B) todo mejoró", "A", "El tiempo mejoró, pero la claridad de lo entregado quedó débil."),
    ],
    D=[
        arith("Antes de una mejora, el 40 % de 50 solicitudes quedaba sin atender. Después, quedan 10 sin atender de 50. ¿Cuántas solicitudes más se atienden ahora?", "50*40//100-10", "Antes quedaban 20 sin atender y ahora 10.", " solicitudes"),
        ("Metas: tiempo promedio de hasta 18 horas y al menos 80 % de usuarios con nota 4 o 5. En la nueva prueba el tiempo promedio fue de 18 horas y 15 de 20 usuarios dieron nota 4 o 5. ¿Qué metas se cumplen?", "Solo la del tiempo", "15 de 20 es 75 %, menos que el 80 % pedido."),
    ],
    ctx=ex("Antes de una mejora, 25 de 100 solicitudes de ejemplo se perdían. Después se pierden 5 de 100. ¿Qué porcentaje bajaron las pérdidas?", "80 %", "Bajaron 20 de 25 pérdidas: 20 × 100 ÷ 25 = 80.", calc="(25-5)*100//25"),
    sc=[
        ("¿Cómo se escribe una mejora concreta?", "«Si cambio X, el indicador pasará de A a B»", "Dice qué se cambia y cómo se medirá."),
        ("¿Qué se prioriza primero, alto impacto con bajo esfuerzo o bajo impacto con alto esfuerzo?", "Alto impacto con bajo esfuerzo", "Da más resultado con menos costo."),
        ("¿Por qué se vuelve a probar?", "Para comprobar si la mejora funcionó", "Se compara el antes con el después."),
    ],
    open_task=(
        "Evaluación de ejemplo de un servicio de apuntes: tiempo promedio 30 horas (meta 24), 8 de 40 solicitudes se pierden por falta de registro, 6 de 30 usuarios no entienden letra desordenada de los apuntes. Escribe tres mejoras con el formato «si cambio X, entonces el indicador pasará de A a B» (al menos una de proceso y una de producto final), ordénalas con impacto y esfuerzo del 1 al 3 y escribe cómo repetirías la prueba.",
        "Proceso: si se anota cada solicitud en una planilla al llegar, las pérdidas pasarán de 8 a 1 de 40 (impacto 3, esfuerzo 1). Producto: si se pasan los apuntes a limpio con un formato único, los usuarios que no entienden pasarán de 6 a 1 de 30 (impacto 2, esfuerzo 2). Proceso: si hay un reemplazo por turno, el tiempo pasará de 30 a 24 horas (impacto 3, esfuerzo 2). Nueva prueba con 40 solicitudes",
        ["tres mejoras con el formato", "una de proceso y una de producto", "priorización con impacto y esfuerzo", "plan de nueva prueba con medición"],
        ["hoja con mejoras, orden y plan de prueba"],
        ["mejoras vagas", "no relacionar la mejora con la causa"],
        "Pregunta: «¿qué número cambiaría si tu mejora funciona?». Debe nombrar el indicador.",
    ),
    reinforce="Elige un hábito de estudio tuyo, propón un cambio concreto y anota cómo medirías si mejoró.",
    extend="Explica por qué una mejora puede empeorar otro indicador y cómo lo descubrirías.",
)

# ------------------------------------------------------------------ OA 04, clase 1
reg(
    OA4, 1,
    materials="Hoja, lápiz y los mensajes escritos en este cuaderno.",
    use="Aprenderé a definir el objetivo y la audiencia de una comunicación y a adaptar el mensaje a cada audiencia. Sirve para explicar el diseño y la planificación de un servicio de forma que se entienda.",
    prior=["Sé describir el flujo y la planificación de un servicio.", "Sé escribir criterios con indicador y umbral.", "Sé calcular enteros."],
    explain=[
        "Comunicar el diseño o la planificación de un servicio es contar a otras personas qué se hizo, cómo y por qué. Primero se define el objetivo: informar (dar datos), instruir (enseñar cómo hacer algo), persuadir (convencer de algo) o pedir retroalimentación (preguntar qué opinan para mejorar).",
        "Luego se define la audiencia, que son las personas a las que se dirige el mensaje: los usuarios, el equipo, la dirección del colegio, las familias o la comunidad. Cada audiencia necesita un nivel de detalle, un lenguaje y un formato distintos. Los usuarios necesitan saber cómo pedir el servicio, con palabras simples. El equipo necesita los pasos, los roles y los tiempos. Quien debe autorizar el servicio necesita saber sus beneficios, su costo y las medidas de cuidado.",
        "Un mensaje claro tiene una idea principal, un ejemplo o dato que la respalda y una invitación a actuar, como «pide tu apunte en el formulario». Se evitan los términos técnicos que la audiencia no conoce.",
    ],
    vocab=[("objetivo comunicativo", "para qué se comunica: informar, instruir, persuadir o pedir opinión"), ("audiencia", "personas a las que se dirige un mensaje"), ("instruir", "enseñar cómo hacer algo paso a paso"), ("persuadir", "convencer de algo"), ("retroalimentación", "opinión que se pide para mejorar"), ("idea principal", "lo más importante que se quiere decir")],
    worked=[
        ("Reconocer objetivo y audiencia", "Un cartel en el pasillo dice: «Pide tus apuntes en el formulario del curso. Respuesta en 2 días». ¿Cuál es su objetivo y su audiencia?", ["Enseña cómo hacer algo y da un plazo: es instruir e informar.", "Está dirigido a quienes van a pedir apuntes: los usuarios."], "Instruir e informar; audiencia: los usuarios"),
        ("Adaptar el mensaje", "Mensaje para el equipo: «Paso 3: copiar, 6 minutos, cuello de botella». ¿Sirve para los usuarios? Reescríbelo.", ["Los usuarios no conocen «cuello de botella» ni les importa el paso interno.", "Les interesa cuándo recibirán su apunte."], "No sirve; para los usuarios: «Tus apuntes estarán listos en 2 días»"),
    ],
    mistakes=[
        ("Enviar el mismo mensaje a todos.", "Cada audiencia necesita un nivel de detalle y un lenguaje distintos.", "Adapta el mensaje a quién lo va a leer."),
        ("Llenar a los usuarios de detalles técnicos.", "Solo necesitan saber cómo usar el servicio.", "Deja los detalles para el equipo."),
    ],
    R=[
        ("Un texto que explica paso a paso cómo pedir el servicio, ¿tiene objetivo de instruir o de persuadir?", "Instruir", "Enseña cómo hacer algo."),
        ("Un afiche que invita a usar el servicio y destaca sus beneficios, ¿tiene objetivo de persuadir o de pedir retroalimentación?", "Persuadir", "Busca convencer de usar el servicio."),
        ("¿Qué es la audiencia de un mensaje? A) las personas a quienes se dirige B) quien lo escribe", "A", "La audiencia es quien recibe el mensaje."),
    ],
    C=[
        ("Para el equipo de trabajo conviene un mensaje con A) pasos, tiempos y responsables B) solo una frase corta de invitación", "A", "El equipo necesita el detalle para trabajar."),
        ("A los usuarios les conviene que se les diga A) cómo pedir el servicio con palabras simples B) los detalles internos del cuello de botella", "A", "Necesitan saber cómo usarlo, no cómo funciona por dentro."),
        ("Quien debe autorizar el servicio necesita saber, antes que nada, A) beneficios, costo y medidas de cuidado B) los colores del afiche", "A", "Con eso decide si lo autoriza."),
    ],
    A=[
        ("Relaciona cada mensaje con su audiencia (usuarios, equipo o dirección del colegio): (1) «Recepción registra, copia prepara y entrega reparte, en turnos de 1 hora», (2) «Pide tus apuntes en el formulario; respuesta en 2 días», (3) «El servicio no tiene costo, usa la sala los miércoles y protege los datos personales».", "1 equipo, 2 usuarios, 3 dirección del colegio", "Cada mensaje trae el detalle que esa audiencia necesita."),
        arith("Un cartel para usuarios debe leerse en menos de 30 segundos. Se leen 2 palabras por segundo (dato de ejemplo). ¿Cuántas palabras puede tener como máximo?", "30*2", "Se multiplican los segundos por las palabras por segundo.", " palabras"),
        ("Mensaje: «Para pedir apuntes, entra al formulario, elige la materia y espera la respuesta». ¿Cuál es su objetivo?", "Instruir", "Explica los pasos para hacer algo."),
    ],
    Z=[
        ("Un equipo envía a las familias el mismo diagrama técnico de 12 pasos que usó internamente. ¿Qué falla? A) no adaptó el detalle ni el lenguaje a la audiencia B) el diagrama no tenía el logo del colegio", "A", "Las familias necesitan una explicación simple, no el trabajo interno."),
        ("Para convencer a la comunidad de apoyar el servicio, ¿qué dato sirve más? A) «30 de 40 vecinos lo necesitan» B) «el paso más lento dura 6 minutos»", "A", "Muestra la necesidad, que es lo que convence."),
    ],
    D=[
        arith("Un afiche para usuarios admite como máximo 60 palabras. El título tiene 5, el cómo pedir tiene 25, el plazo tiene 10 y el cuidado de datos tiene 12. ¿Cuántas palabras quedan disponibles?", "60-(5+25+10+12)", "Se suman las palabras usadas y se restan del máximo.", " palabras"),
        arith("Una presentación de 10 minutos se reparte así: 3 minutos para el problema y 4 para el servicio. El resto es para pedir apoyo. ¿Cuántos minutos son?", "10-3-4", "Se restan los minutos ya asignados.", " minutos"),
    ],
    ctx=arith("Un cartel de ejemplo para vecinos tiene 3 frases de 14 palabras cada una. El máximo es 50 palabras. ¿Cuántas palabras le quedan por usar?", "50-3*14", "Se multiplican frases por palabras y se resta del máximo.", " palabras"),
    sc=[
        ("¿Cuáles son cuatro objetivos de comunicar?", "Informar, instruir, persuadir y pedir retroalimentación", "Son los objetivos que se definen primero."),
        ("¿Qué necesita saber un usuario del servicio?", "Cómo pedirlo y cuándo recibirá la respuesta", "Es lo que necesita para usarlo."),
        ("¿Se envía el mismo mensaje a todas las audiencias?", "No", "Cada una necesita distinto detalle y lenguaje."),
    ],
    open_task=(
        "Servicio de ejemplo: «Apuntes para quienes faltan»; el equipo de 4 estudiantes entrega los apuntes en 2 días mediante un formulario o un cuaderno en la sala. Escribe tres mensajes de máximo 40 palabras cada uno: uno para usuarios (objetivo instruir), uno para el equipo (objetivo informar los roles y tiempos) y uno para la dirección del colegio (objetivo persuadir para que lo autorice). Indica la idea principal y la invitación a actuar de cada uno.",
        "Usuarios: «Si faltaste, pide tus apuntes en el formulario del curso o en el cuaderno de la sala. Te respondemos en 2 días. Hoy mismo puedes hacerlo». Idea principal: cómo pedir; invitación: pídelos hoy. Equipo: «Recepción registra en 1 minuto, copia prepara en 6 minutos y entrega reparte en 2; turnos de 1 hora». Idea principal: quién hace qué y en cuánto tiempo; invitación: confirmen su turno. Dirección: «El servicio ayuda a 30 de 40 estudiantes que no consiguen apuntes, no tiene costo, usa la sala los miércoles y protege los datos personales. Les pedimos autorizarlo». Idea principal: beneficio sin costo y con cuidado; invitación: autorizarlo",
        ["tres mensajes con la audiencia correcta", "máximo 40 palabras", "idea principal clara", "invitación a actuar", "lenguaje adaptado"],
        ["tres mensajes escritos con su idea principal"],
        ["usar el mismo texto para las tres audiencias", "pasar de 40 palabras"],
        "Pregunta: «¿quién lo lee y qué necesita saber para actuar?». Úsala para ajustar cada mensaje.",
    ),
    reinforce="Escribe dos mensajes sobre una actividad de tu curso: uno para tus compañeros y otro para una persona adulta de tu casa.",
    extend="Explica qué se pierde cuando un mensaje usa términos técnicos que la audiencia no conoce.",
)

# ------------------------------------------------------------------ OA 04, clase 2
reg(
    OA4, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a elegir la herramienta TIC y el formato adecuados según el objetivo y la audiencia, y a comprobar su accesibilidad. Sirve para que el mensaje llegue a todos y se pueda leer con facilidad.",
    prior=["Sé definir objetivo y audiencia.", "Sé que un servicio debe tener alternativa sin conexión.", "Sé calcular enteros."],
    explain=[
        "Las TIC (tecnologías de la información y la comunicación) son herramientas para crear y compartir información: un procesador de texto, una planilla de cálculo, un programa de presentaciones, un programa de diagramas, un formulario, el correo y la mensajería. La herramienta se elige según el objetivo y la audiencia, no según cuál me gusta más. Para mostrar cantidades por día sirve una planilla con un gráfico de barras; para mostrar pasos y decisiones, un diagrama de flujo; para exponer ante un grupo, una presentación; para avisar algo rápido, un mensaje corto.",
        "La accesibilidad es que el mensaje lo pueda usar la mayor cantidad de personas. Se cuida con letra grande (en una presentación, de 24 puntos o más), buen contraste entre el texto y el fondo, un texto alternativo que describe cada imagen para quien no la ve, y no usar solo el color para dar información: se agregan palabras o símbolos. También se piensa en el acceso: si parte de la audiencia no tiene internet o tiene datos limitados, se entrega además en papel o en un archivo liviano.",
        "Un mensaje bien diseñado tiene pocas ideas por pantalla, títulos claros y un orden lógico. Antes de difundirlo se prueba con una persona de la audiencia para ver si lo entiende.",
    ],
    vocab=[("TIC", "tecnologías de la información y la comunicación"), ("accesibilidad", "que el mensaje lo pueda usar la mayor cantidad de personas"), ("contraste", "diferencia entre el color del texto y el del fondo"), ("texto alternativo", "descripción escrita de una imagen"), ("gráfico de barras", "dibujo que compara cantidades con barras"), ("diagrama de flujo", "dibujo de pasos y decisiones")],
    worked=[
        ("Elegir la herramienta", "Debes mostrar al equipo cuántas solicitudes llegaron cada día de la semana. ¿Qué herramienta usas?", ["Son cantidades por día que se quieren comparar.", "Una planilla permite anotarlas y hacer un gráfico de barras."], "Una planilla con un gráfico de barras"),
        ("Revisar la accesibilidad", "Un afiche digital tiene texto gris claro sobre fondo blanco y una imagen sin descripción. ¿Qué corriges?", ["El gris claro sobre blanco tiene poco contraste y cuesta leerlo.", "La imagen necesita un texto alternativo."], "Más contraste y texto alternativo"),
    ],
    mistakes=[
        ("Elegir la herramienta que más me gusta aunque la audiencia no pueda abrirla.", "El mensaje no llega a quien lo necesita.", "Elige según la audiencia y su acceso."),
        ("Mostrar «cumple» y «no cumple» solo con verde y rojo.", "Quien no distingue esos colores pierde la información.", "Agrega palabras o símbolos además del color."),
    ],
    R=[
        ("Para comparar cantidades por día conviene un A) gráfico de barras B) párrafo largo", "A", "Las barras permiten comparar de un vistazo."),
        ("El texto alternativo sirve para que A) quien no ve la imagen sepa qué muestra B) la imagen pese menos", "A", "Describe la imagen con palabras."),
        ("El texto gris claro sobre fondo blanco, ¿tiene buen contraste?", "No", "Los colores son demasiado parecidos."),
    ],
    C=[
        ("Quieres explicar a los usuarios cómo pedir el servicio en el pasillo del colegio, donde no hay internet. ¿Qué formato conviene? A) un cartel impreso con los pasos B) un video de 10 minutos en línea", "A", "No depende de la conexión."),
        ("Un gráfico distingue «cumple» y «no cumple» solo con verde y rojo. ¿Qué se agrega para quien no distingue colores? A) palabras o símbolos además del color B) más colores", "A", "La información no debe depender solo del color."),
        ("Para mostrar los pasos del servicio y sus decisiones sí o no, ¿qué herramienta sirve más? A) un diagrama de flujo B) una planilla de costos", "A", "El diagrama muestra el orden y las decisiones."),
    ],
    A=[
        ("Elige la herramienta para cada necesidad (planilla, diagrama de flujo o presentación): (1) mostrar el orden de los pasos y sus decisiones, (2) registrar y sumar las solicitudes por día, (3) exponer el servicio ante el curso en 5 minutos.", "1 diagrama de flujo, 2 planilla, 3 presentación", "Cada herramienta se adapta a un objetivo distinto."),
        arith("Una presentación de ejemplo tiene 12 diapositivas y dispone de 6 minutos. Si el tiempo se reparte por igual, ¿cuántos segundos dura cada una?", "6*60//12", "Seis minutos son 360 segundos y se dividen entre 12.", " segundos"),
        ("Lista de accesibilidad: (1) letra de 28 puntos, (2) texto gris claro sobre fondo blanco, (3) foto con descripción escrita, (4) información dada solo por color. ¿Cuáles cumplen?", "1 y 3", "Tienen letra grande y texto alternativo; las otras dos dificultan el acceso."),
    ],
    Z=[
        ("Un equipo envía el instructivo del servicio como un archivo de 40 MB a familias que usan datos móviles limitados. ¿Qué falla y cómo corregirlo?", "No considera el acceso de la audiencia; entregar un archivo liviano o en papel", "El formato debe poder usarlo quien recibe el mensaje."),
        ("Debes comunicar a la vez a 30 adultos mayores sin celular y a 20 estudiantes con celular. ¿Qué combinación sirve? A) un cartel impreso más un mensaje digital B) solo un mensaje digital", "A", "Cada medio llega a una parte de la audiencia."),
    ],
    D=[
        arith("Hay que imprimir 32 afiches y en cada hoja caben 4. ¿Cuántas hojas se necesitan?", "32//4", "Se divide el total de afiches entre los que caben en una hoja.", " hojas"),
        arith("Una rúbrica tiene 4 criterios (letra, contraste, texto alternativo y no depender solo del color) y cada uno vale 2 puntos si se cumple. Un afiche cumple letra y contraste. ¿Qué porcentaje del puntaje máximo obtiene?", "(2+2)*100//(4*2)", "Obtiene 4 de 8 puntos.", " %"),
    ],
    ctx=ex("Se debe avisar un horario a 60 vecinos de ejemplo: 45 usan mensajería y 15 no. ¿Qué porcentaje necesita el aviso en papel?", "25 %", "Se calcula 15 × 100 ÷ 60 = 25.", calc="15*100//60"),
    sc=[
        ("En Tecnología: ¿Qué significan las siglas TIC?", "Tecnologías de la información y la comunicación", "Son las herramientas para crear y compartir información."),
        ("¿Para qué sirve un buen contraste?", "Para que el texto se lea con facilidad", "Se distingue bien del fondo."),
        ("¿Qué se agrega cuando la información se da con colores?", "Palabras o símbolos", "Así la entienden quienes no distinguen colores."),
    ],
    open_task=(
        "Escoge una situación. A: avisar a 30 adultos mayores (sin celular) el horario del servicio. B: mostrar al equipo cuántas solicitudes llegaron de lunes a viernes (6, 9, 4, 7 y 8). C: explicar a las familias, en una reunión de 5 minutos, para qué sirve el servicio. Elige la herramienta y el formato, explica por qué se ajustan al objetivo y a la audiencia, y escribe tres decisiones de accesibilidad (por ejemplo tamaño de letra, contraste y alternativa para quien no tiene internet).",
        "A: cartel impreso grande en la sede vecinal, con letra de 28 puntos, texto negro sobre fondo blanco y una persona del equipo que repite el horario por teléfono. Se ajusta porque la audiencia no tiene celular",
        ["herramienta ajustada a objetivo y audiencia", "tres decisiones de accesibilidad", "alternativa para quien no tiene internet", "justificación clara"],
        ["hoja con la elección y su justificación"],
        ["elegir una herramienta que la audiencia no puede usar", "no mencionar la accesibilidad"],
        "Pregunta: «¿esta persona puede abrir, leer y entender lo que le entrego?».",
    ),
    reinforce="Mira un afiche o una pantalla de tu entorno y anota si su contraste, su tamaño de letra y su orden son buenos.",
    extend="Explica por qué la accesibilidad también beneficia a personas que no tienen ninguna dificultad.",
)

# ------------------------------------------------------------------ OA 04, clase 3
reg(
    OA4, 3,
    materials="Hoja, lápiz, calculadora si la necesitas y los planes escritos en este cuaderno.",
    use="Aprenderé a representar y comunicar la planificación con un cronograma, dependencias y duración total. Sirve para mostrar a otras personas qué se hará, quién y cuándo.",
    prior=["Sé describir el flujo de un servicio.", "Sé identificar el paso más lento.", "Sé sumar enteros."],
    explain=[
        "Planificar es decidir qué tareas se hacen, quién las hace y cuándo. Se comunica con una lista de tareas, una tabla de responsables y un cronograma, que muestra las tareas en el tiempo. Una forma de dibujarlo es la carta Gantt: cada tarea es una fila y una barra indica cuándo empieza y cuándo termina. Un hito es un punto de control importante, como «terminar la prueba piloto».",
        "Algunas tareas son dependientes: no pueden empezar hasta que otra termine, como imprimir afiches después de aprobar el diseño. Si las tareas van una tras otra, la duración es la suma de sus duraciones. Si dos tareas pueden hacerse al mismo tiempo, ese tramo dura lo que dura la más larga. La ruta crítica es la cadena de tareas que determina la duración total: si se alarga una de ellas, se alarga todo el plan.",
        "Un buen cronograma lleva responsables, duraciones y hitos, y se actualiza si algo cambia. Acortar una tarea que no está en la ruta crítica no reduce la duración total.",
    ],
    vocab=[("cronograma", "representación de las tareas en el tiempo"), ("carta Gantt", "cronograma con una barra por tarea"), ("hito", "punto de control importante del plan"), ("tarea dependiente", "la que no puede empezar hasta que otra termine"), ("tareas en paralelo", "las que se hacen al mismo tiempo"), ("ruta crítica", "cadena de tareas que determina la duración total")],
    worked=[
        ("Tareas en secuencia", "Tarea A dura 2 días; después B, 3 días; después C, 1 día. ¿Cuánto dura todo?", ["Cada tarea espera a la anterior.", "Sumo: 2 + 3 + 1 = 6."], "6 días"),
        ("Tareas en paralelo", "Después de A (2 días), las tareas B (3 días) y C (4 días) se hacen a la vez; luego D (1 día). ¿Cuánto dura todo?", ["El tramo de B y C dura lo que la más larga: 4 días.", "Sumo 2 + 4 + 1 = 7."], "7 días"),
    ],
    mistakes=[
        ("Sumar como seguidas tareas que se hacen a la vez.", "El plan parece más largo de lo que es.", "En el tramo en paralelo toma solo la tarea más larga."),
        ("Hacer un cronograma sin responsables ni hitos.", "No se sabe quién hace qué ni cuándo revisar el avance.", "Anota un responsable y un hito en el plan."),
    ],
    R=[
        arith("Dos tareas van una después de la otra: la primera dura 3 días y la segunda 2. ¿Cuánto dura el tramo?", "3+2", "Se suman porque van en secuencia.", " días"),
        ("Dos tareas se hacen a la vez: una dura 3 días y la otra 5 días. ¿Cuánto dura el tramo?", "5 días", "Dura lo que la más larga."),
        ("¿Qué es un hito? A) un punto de control importante del plan B) una tarea muy larga", "A", "Permite revisar el avance."),
    ],
    C=[
        ("En una carta Gantt, ¿qué muestra una barra? A) cuándo empieza y termina una tarea B) cuánto cuesta la tarea", "A", "Representa la tarea en el tiempo."),
        ("¿Cuál es una tarea dependiente? A) imprimir los afiches, que no puede empezar hasta aprobar el diseño B) ponerle nombre al servicio, que se puede hacer cuando sea", "A", "Depende de que termine otra tarea."),
        ("Si dos tareas pueden hacerse a la vez, ¿cómo se calcula ese tramo? A) se toma la más larga B) se suman", "A", "Mientras una avanza, la otra también."),
    ],
    A=[
        arith("Tareas en secuencia: encuesta 3 días, análisis 2 días, diseño del flujo 4 días y prueba piloto 5 días. ¿Cuántos días dura el plan?", "3+2+4+5", "Se suman las cuatro duraciones.", " días"),
        arith("Después del diseño (2 días), las tareas P (5 días) y Q (3 días) se hacen a la vez; luego viene la prueba (4 días). ¿Cuánto dura el plan?", "2+5+4", "En el tramo en paralelo cuenta la tarea más larga, P.", " días"),
        ("Después del diseño (3 días), las tareas X (4 días) e Y (6 días) se hacen a la vez; luego sigue la prueba (2 días). ¿Cuál de las dos tareas determina la duración total?", "Y", "Es la más larga del tramo en paralelo."),
    ],
    Z=[
        ("Un equipo suma todas las tareas de su plan (3 + 4 + 6 + 2 = 15 días), aunque dos de ellas se hacen a la vez. ¿Qué error comete?", "Suma como seguidas tareas que se hacen en paralelo", "El plan real dura menos de 15 días."),
        ("Si se acorta una tarea que no está en la ruta crítica de 5 a 3 días, ¿cambia la duración total? A) no cambia B) baja 2 días", "A", "La duración la marca la ruta crítica."),
    ],
    D=[
        arith("Plan: A (2 días); luego B (4 días) y C (3 días) a la vez; luego D (2 días); luego E (3 días). El equipo quiere terminar en 12 días. ¿Cuántos días de margen quedan?", "12-(2+4+2+3)", "La duración es 2 + 4 + 2 + 3 = 11 días.", " día"),
        arith("Un plan tiene un tramo secuencial de 3, 5 y 4 días. Debe terminar en 9 días. ¿Cuántos días hay que recortar o paralelizar?", "3+5+4-9", "El tramo dura 12 días y se necesitan 9.", " días"),
    ],
    ctx=ex("Cronograma de ejemplo: encuesta (2 días), diseño (3 días, después de la encuesta); luego carteles (2 días) y formulario (4 días) a la vez; luego prueba piloto (2 días). ¿Cuántos días dura el plan?", "11 días", "2 + 3 + 4 + 2 = 11, porque en el tramo en paralelo cuenta la tarea más larga.", calc="2+3+4+2"),
    sc=[
        ("¿Qué es una tarea dependiente?", "La que no puede empezar hasta que otra termine", "Su inicio depende de otra tarea."),
        ("¿Cómo se calcula la duración de dos tareas en paralelo?", "Se toma la más larga", "Se hacen al mismo tiempo."),
        ("¿Qué es la ruta crítica?", "La cadena de tareas que determina la duración total", "Si una se alarga, se alarga todo."),
    ],
    open_task=(
        "Plan de ejemplo para abrir un servicio de apuntes. Tareas: encuesta (2 días, curso completo), análisis (1 día, después de la encuesta), diseño del flujo (3 días, después del análisis), afiche (2 días) y formulario (3 días), ambos después del diseño y a la vez, prueba piloto (2 días, después de ambos), ajustes (1 día). Dibuja el cronograma en una tabla con semanas o días, asigna un responsable de ejemplo a cada tarea, marca dos hitos, calcula la duración total y señala la ruta crítica.",
        "Duración: 2 + 1 + 3 + 3 + 2 + 1 = 12 días. Ruta crítica: encuesta, análisis, diseño, formulario, prueba piloto y ajustes. Hitos: diseño aprobado (día 6) y prueba piloto terminada (día 11). El afiche tiene 1 día de holgura. Responsables de ejemplo: encuesta y análisis, Ana; diseño y formulario, Luis; afiche, Camila; prueba piloto y ajustes, todo el equipo",
        ["cronograma completo", "responsables asignados", "dos hitos", "duración total correcta", "ruta crítica"],
        ["tabla con el cronograma y el cálculo"],
        ["sumar las tareas en paralelo", "olvidar a los responsables"],
        "Pregunta: «¿cuáles tareas se hacen a la vez y cuál de ellas es más larga?». Revisa el tramo en paralelo.",
    ),
    reinforce="Planifica un trabajo de tu casa con tres tareas, una de ellas dependiente, y calcula cuánto demora en total.",
    extend="Explica por qué conviene mostrar la ruta crítica a quien te pide apoyar el plan.",
)

# ------------------------------------------------------------------ OA 04, clase 4
reg(
    OA4, 4,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a comunicar con ética: con datos verdaderos, con créditos, con respeto y cuidando la privacidad. Sirve para que lo que difundes sea honesto y no dañe a nadie.",
    prior=["Sé qué es una fuente confiable.", "Sé cuidar datos personales.", "Sé calcular porcentajes."],
    explain=[
        "Comunicar con ética es mostrar la información de forma veraz, respetuosa y justa. Ser veraz es presentar datos verdaderos y completos: no esconder los resultados malos ni mostrar solo la cifra favorable. Un gráfico puede engañar si su eje no parte de cero, porque exagera las diferencias. Se corrige un error en cuanto se descubre, a la vista de todos.",
        "Dar crédito es nombrar de dónde sale lo que se usa. Una cita completa incluye quién lo hizo (autor o institución), el título o de qué se trata y la fecha, además de la licencia cuando la tiene. Copiar sin citar es plagio. También se verifica un rumor con otra fuente confiable antes de difundirlo.",
        "El respeto implica un lenguaje que no ofenda ni discrimine, y la privacidad implica no mostrar datos, fotos ni comentarios de otras personas sin su consentimiento. Pedir permiso, citar y mostrar los datos completos es parte del mensaje, no un trámite.",
    ],
    vocab=[("veracidad", "presentar datos verdaderos y completos"), ("crédito", "nombrar de dónde sale lo que se usa"), ("cita", "referencia con autor o institución, título y fecha"), ("plagio", "presentar como propio el trabajo de otra persona"), ("eje", "línea de un gráfico donde se marcan los valores"), ("consentimiento", "permiso claro y libre de la persona")],
    worked=[
        ("Detectar un gráfico que engaña", "El servicio A atendió 40 solicitudes (dato de ejemplo) y el B atendió 50. Un gráfico con el eje desde 30 muestra la barra de B el doble de alta que la de A. ¿Engaña? ¿Cuánto más es B?", ["Con el eje desde 30, las barras miden 10 y 20, y parece el doble.", "En realidad B es 10 más que A: 10 × 100 ÷ 40 = 25 % más."], "Sí engaña; B es 25 % mayor que A"),
        ("Escribir una cita", "Usaste una cifra de un informe de una municipalidad. ¿Qué datos incluyes en la cita?", ["Indico la institución que lo escribió.", "Agrego el título del informe y la fecha."], "Institución, título y fecha"),
    ],
    mistakes=[
        ("Publicar solo los datos favorables.", "Se engaña a quien lee y no se puede mejorar.", "Muestra los resultados completos."),
        ("Citar solo «internet».", "No indica quién lo creó ni cuándo.", "Escribe autor o institución, título y fecha."),
    ],
    R=[
        ("Presentar solo los resultados buenos y esconder los malos, ¿es honesto?", "No", "Oculta información y engaña."),
        ("Cuando usas una cifra de otra fuente, ¿qué debes hacer? A) nombrar la fuente B) decir que es tuya", "A", "Dar crédito es parte de la ética."),
        ("Publicar el comentario de un usuario con su nombre sin avisarle, ¿qué falta? A) su consentimiento B) un color más llamativo", "A", "Los datos de una persona se usan con su permiso."),
    ],
    C=[
        ("Un gráfico de barras cuyo eje no parte de cero puede A) exagerar las diferencias B) ocultar las diferencias", "A", "Hace que parezcan mayores de lo que son."),
        ("¿Cuál es una cita completa? A) «Informe de la municipalidad, Plan de ciclovías, 2023 (de ejemplo)» B) «lo vi en internet»", "A", "Indica quién, qué y cuándo."),
        ("Te llega un rumor de que otro servicio cobra a escondidas. Antes de difundirlo, A) verificas con otra fuente confiable B) lo reenvías para que otros opinen", "A", "Difundir sin verificar puede dañar a otras personas."),
    ],
    A=[
        arith("En un gráfico de ejemplo, el servicio A atendió 30 solicitudes y el servicio B atendió 36. Con el eje desde cero, ¿qué porcentaje más es B que A?", "(36-30)*100//30", "La diferencia, 6, se calcula sobre A.", " %"),
        ("Marca las prácticas éticas: (1) citar de dónde sale una cifra, (2) usar la foto de una compañera sin avisarle, (3) mostrar también los resultados que no cumplieron la meta, (4) copiar un texto sin nombrar al autor.", "1 y 3", "Son veraces y dan crédito; las otras dos faltan al consentimiento y a la autoría."),
        ex("Una encuesta de ejemplo tuvo 20 respuestas: 5 «excelente», 10 «bueno» y 5 «malo». El equipo publica «¡El 100 % está satisfecho!». ¿Es honesto? ¿Cuál es el porcentaje real de «excelente» o «bueno»?", "No; es 75 %", "Quince de veinte dieron esas respuestas: 15 × 100 ÷ 20 = 75.", calc="15*100//20"),
    ],
    Z=[
        ("Un equipo reporta solo la semana en que atendió 95 % a tiempo y omite las otras tres, que fueron 60 %, 65 % y 70 %. ¿Qué principio ético incumple?", "La veracidad, porque oculta datos", "Mostrar solo lo favorable da una imagen falsa."),
        ("Un afiche llama «los más flojos del colegio» a quienes no usan el servicio. ¿Qué falla? A) el lenguaje irrespetuoso B) el tamaño de la letra", "A", "Ofende y discrimina a un grupo."),
    ],
    D=[
        arith("Un informe de ejemplo cita 8 cifras: 5 tienen fuente completa, 1 tiene fuente incompleta y el resto no tiene fuente. ¿Cuántas cifras no tienen fuente?", "8-5-1", "Se restan las que sí la tienen.", " cifras"),
        ex("Un grupo decide corregir el afiche si el 10 % o más de las cifras publicadas está mal. Publicó 20 cifras y 3 estaban mal. ¿Debe corregir y qué porcentaje está mal?", "Sí; 15 %", "3 × 100 ÷ 20 = 15, que supera el 10 %.", calc="3*100//20"),
    ],
    ctx=ex("Un equipo de ejemplo publicó 40 comentarios de usuarios y 10 no tenían consentimiento. ¿Qué porcentaje de los comentarios se publicó sin consentimiento?", "25 %", "Se calcula 10 × 100 ÷ 40 = 25.", calc="10*100//40"),
    sc=[
        ("¿Qué datos lleva una cita completa?", "Autor o institución, título y fecha", "Permite encontrar y reconocer la fuente."),
        ("En Tecnología: ¿Qué es el plagio?", "Presentar como propio el trabajo de otra persona", "Falta al crédito y a la autoría."),
        ("¿Qué haces con un rumor antes de difundirlo?", "Lo verifico con otra fuente confiable", "Así no se daña a otros con información falsa."),
    ],
    open_task=(
        "Revisa este informe de ejemplo del servicio «Apuntes para quienes faltan». Dice: «Atendimos al 100 % de los usuarios». Los datos reales son 36 de 40 usuarios atendidos. Incluye una foto de un compañero que no dio permiso, un gráfico con eje desde 30 que muestra 36 de atendidos junto a 40 de solicitudes, una frase sacada de un artículo sin autor ni fecha y el comentario «los que no usan el servicio son unos flojos». Escribe (a) el porcentaje real de atención, (b) cinco problemas éticos y (c) cómo corregirías cada uno.",
        "(a) 36 × 100 ÷ 40 = 90 %. (b) Cifra falsa, foto sin consentimiento, gráfico que exagera, frase sin crédito y comentario irrespetuoso. (c) Escribir 90 %, pedir permiso o quitar la foto, usar el eje desde 0, citar autor y fecha o quitar la frase, y cambiar el comentario por un lenguaje respetuoso",
        ["calcula el porcentaje real", "identifica los problemas éticos", "propone una corrección para cada uno", "usa los términos consentimiento, crédito y veracidad"],
        ["hoja con la revisión del informe"],
        ["corregir solo uno de los problemas", "dejar la cifra falsa"],
        "Pregunta: «¿qué diría una persona que no participó si leyera esto sin explicación?». Úsala para ver qué corregir.",
    ),
    reinforce="Revisa una noticia o publicación que hayas visto y anota si cita su fuente y si muestra los datos completos.",
    extend="Explica por qué corregir un error a la vista de todos aumenta la confianza en un equipo.",
)
