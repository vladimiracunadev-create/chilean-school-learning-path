"""Ciencias del ejercicio físico y deportivo, 3.º y 4.º medio HC: OAC-03 (programas de entrenamiento para mejorar la condición física propia y de otras personas), clases 1 a 5, y OAC-04 (efectos de la actividad física, la alimentación saludable y las ayudas ergogénicas), clases 1 a 5. Datos de ejemplo escritos en cada enunciado; sin dietas, suplementos ni dosis."""
from __future__ import annotations

from hc_cefd_common import build

O3 = "EF-CEFD-3y4-OAC-03"
O4 = "EF-CEFD-3y4-OAC-04"

# ============================================================ OAC-03, clase 1
F = ("Ficha 10 (resultados de ejemplo, inventados, de una persona ficticia llamada Ignacia, en pruebas simples hechas con calentamiento y en condiciones iguales). "
     "Resistencia: camina y trota sin detenerse 9 minutos. Fuerza de piernas: se sienta y se para de una silla estable 14 veces en 30 segundos. "
     "Meta que quiere trabajar: aumentar su resistencia. Disponibilidad: 3 días por semana, 40 minutos por día, con actividades en grupo en la plaza.")
build(
    O3, 1, F,
    use="Aprenderé a diagnosticar la condición física de forma privada y segura con pruebas simples, a fijar una meta medible y a decidir qué capacidad trabajar antes de armar un programa de entrenamiento.",
    prior=["Sé qué es una adaptación crónica.", "Sé registrar mediciones en condiciones iguales.", "Sé que cada persona se compara solo consigo misma."],
    explain=[
        "Un programa de entrenamiento físico es un plan organizado con una meta, una evaluación inicial, sesiones planificadas y una evaluación final. La condición física es el conjunto de capacidades que permiten realizar esfuerzos: la resistencia (sostener un esfuerzo durante más tiempo), la fuerza muscular (vencer una resistencia), la resistencia muscular (repetir un esfuerzo muchas veces) y la flexibilidad (mover las articulaciones con amplitud).",
        "El diagnóstico inicial usa pruebas simples y seguras, hechas con calentamiento y en condiciones iguales, para obtener una línea de base. Con ella se fija una meta medible: específica (qué capacidad), con un número (cuánto), con plazo (cuándo) y realista para el tiempo disponible. «Estar mejor» no es una meta medible; «subir de 9 a 13 minutos seguidos en 4 semanas» sí lo es.",
        "Las pruebas miden un rendimiento, no el cuerpo de una persona, y los resultados son privados: sirven para compararse consigo misma, no para ordenar al curso. Si durante una prueba aparecen dolor, mareo o falta de aire inusual, se detiene y se avisa a una persona adulta o a un profesional de la salud. Las pruebas se hacen con supervisión de tu docente.",
    ],
    vocab=[("condición física", "conjunto de capacidades para realizar esfuerzos"), ("resistencia", "capacidad de sostener un esfuerzo durante más tiempo"), ("fuerza muscular", "capacidad de los músculos para vencer una resistencia"), ("prueba inicial", "medición simple que da la línea de base"), ("meta medible", "objetivo con capacidad, número y plazo"), ("línea de base", "primera medición para comparar después")],
    worked=[
        ("Convertir un deseo en meta medible", "Una persona de ejemplo dice: «quiero estar mejor». Conviértelo en una meta medible para resistencia.", ["Elige la capacidad: resistencia.", "Agrega número y plazo a partir de su prueba inicial de 8 minutos: «subir a 11 minutos seguidos en 6 semanas»."], "Subir de 8 a 11 minutos seguidos en 6 semanas"),
        ("Elegir la prueba que corresponde", "Una persona de ejemplo quiere mejorar la fuerza de sus piernas. ¿Qué prueba inicial usa?", ["Busca una prueba que use esa capacidad.", "Sentarse y pararse de una silla estable durante 30 segundos mide la fuerza y la resistencia de piernas."], "Sentarse y pararse de una silla en 30 segundos"),
    ],
    mistakes=[("Fijar una meta como «ser mejor que el resto».", "Depende de otras personas y no se puede medir con datos propios.", "Fija una meta con tu propia línea de base, un número y un plazo."),
              ("Hacer las pruebas sin calentar o en distintas condiciones cada vez.", "Aumenta el riesgo y la comparación deja de ser válida.", "Calienta y repite la prueba en condiciones iguales.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es la condición física?', 'El conjunto de capacidades para realizar esfuerzos, como resistencia y fuerza', 'La apariencia del cuerpo de cada persona, que sirve para compararlas', 'El resultado de un solo partido o de una sola competencia del año', 'La condición física son capacidades para el esfuerzo, no la apariencia del cuerpo.'),
        ('abc', '{F} ¿Qué capacidad mide la prueba de caminar y trotar 9 minutos sin detenerse?', 'La resistencia, o sea, sostener un esfuerzo', 'La flexibilidad de las articulaciones', 'La fuerza de los brazos', 'Sostener un esfuerzo continuo mide la resistencia.'),
        ('abc', '{F} ¿Qué prueba usa la ficha para observar la fuerza de las piernas?', 'Sentarse y pararse de una silla estable 14 veces en 30 segundos', 'Trotar 9 minutos sin detenerse, con un ritmo suave y parejo', 'Lanzar una pelota blanda a una pared desde 3 metros de distancia', 'La ficha mide la fuerza de piernas con repeticiones de sentarse y pararse.'),
        ('abc', '¿Para qué sirve una prueba inicial?', 'Para tener una línea de base y comparar después consigo misma', 'Para ordenar al curso de mejor a peor según los resultados', 'Para decidir quién debe dejar de practicar y quién puede seguir', 'Sirve de punto de partida propio; no ordena ni excluye a nadie.'),
        ('abc', '{F} ¿Cuál de estas es una meta medible?', 'Subir de 9 a 13 minutos seguidos en 4 semanas', 'Estar mejor pronto, sin decir cuánto ni cuándo', 'Ser mejor que la mayoría del curso en la prueba', 'Una meta medible tiene capacidad, número y plazo.'),
        ('abc', '¿Por qué las pruebas se hacen con calentamiento y en condiciones iguales?', 'Para cuidar el cuerpo y poder comparar con las siguientes mediciones', 'Para que el resultado salga mejor que el de otras personas', 'Para que las pruebas duren menos', 'El calentamiento protege y las condiciones iguales hacen válida la comparación.'),
        ('=', '{F} Ignacia quiere subir de 9 a 13 minutos en 4 semanas, aumentando lo mismo cada semana. ¿Cuántos minutos más por semana?', '(13-9)/4', 'Se calcula cuántos minutos faltan para la meta y se reparten entre las 4 semanas.', ' minuto por semana'),
        ('abc', '{F} Ignacia dispone de 3 días y 40 minutos por día. ¿Qué meta es realista para ella?', 'Subir de 9 a 13 minutos seguidos en 4 semanas, con tres sesiones', 'Correr 40 minutos seguidos desde la primera semana de práctica', 'Hacer sesiones de 2 horas todos los días de la semana, sin descanso', 'Una meta realista usa su tiempo y avanza de forma gradual.'),
        ('abc', '{F} Ignacia decide trabajar la fuerza de piernas. ¿Qué dato de la ficha usa como línea de base?', 'Las 14 repeticiones de sentarse y pararse en 30 segundos', 'Los 9 minutos continuos de caminata-trote', 'Ninguno: primero debe entrenar y recién después medir algo', 'La línea de base es la medición inicial de la capacidad que se quiere mejorar.'),
        ('abc', 'Una compañera te pide tus resultados para armar un ranking del curso. ¿Qué corresponde?', 'Explicar que son privados y que no se usan para ordenar a las personas', 'Entregarlos para saber quién necesita más práctica', 'Cambiar los números para quedar a la altura de otras personas', 'Los resultados son propios y privados, y un ranking compara personas, no rendimientos.'),
        ('abc', 'Una prueba de resistencia se hizo un día con calor extremo y otra vez en clima templado. ¿Qué problema hay al comparar?', 'Las condiciones no son iguales, así que la comparación no es válida', 'Ninguno, porque el clima no influye en el resultado', 'Que la prueba debe repetirse hasta lograr el mejor resultado', 'Con condiciones distintas no se sabe si el cambio viene del entrenamiento.'),
        ('=', 'En otra prueba de ejemplo, una persona pasó de 10 a 15 repeticiones de sentarse y pararse en 30 segundos. ¿En qué porcentaje aumentó?', '(15-10)*100/10', 'Se calcula el aumento de 5 repeticiones y se divide entre las 10 iniciales.', ' %'),
        ('abc', 'Un diagnóstico dice: «Ignacia es floja porque solo aguantó 9 minutos». ¿Qué defecto tiene?', 'Juzga a la persona y no registra datos ni condiciones de la prueba', 'Está bien, porque 9 minutos es poco para todas las personas', 'Debería decir 8 minutos para ser más exacto', 'Un diagnóstico registra datos y condiciones; no etiqueta a la persona.'),
    ],
    ctx=('abc', 'Mateo, persona ficticia, quiere mejorar su resistencia. Su prueba inicial fue de 7 minutos continuos; tiene 30 minutos, 3 días por semana, y prefiere trotar en grupo. ¿Qué diagnóstico y meta son coherentes?', 'Línea de base de 7 minutos y meta de 10 minutos continuos en 4 semanas', 'Meta de 40 minutos continuos en una semana para llegar más rápido', 'Sin prueba inicial, porque basta con una meta como estar mejor pronto', 'La meta usa su línea de base, un número y un plazo realista para su tiempo.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué partes tiene una meta medible?", "Capacidad, número y plazo", "Así se puede comprobar si se cumplió."),
        ("¿Con quién se comparan los resultados de las pruebas?", "Contigo en otra medición", "Cada persona parte de una línea de base distinta."),
        ("¿Qué haces si aparece dolor o mareo durante una prueba?", "Detenerte y avisar a una persona adulta o a un profesional de la salud", "La seguridad va antes que terminar la prueba."),
    ],
    op=("Con estos datos de ejemplo de una persona ficticia: camina y trota 6 minutos seguidos; dispone de 3 días por semana y 30 minutos por día; le gusta el trabajo en grupo. Escribe su diagnóstico (capacidad, línea de base y condiciones), una meta medible con número y plazo, y dos medidas de seguridad para las pruebas.",
        "Capacidad: resistencia. Línea de base: 6 minutos continuos. Condiciones: 3 días, 30 minutos, en grupo. Meta: subir a 9 minutos continuos en 6 semanas. Seguridad: calentar antes de la prueba y parar y avisar ante dolor o mareo.",
        ["capacidad y línea de base", "meta con número y plazo realistas", "dos medidas de seguridad"],
        ["diagnóstico y meta escritos"],
        ["fijar una meta sin número", "compararse con otras personas", "no incluir calentamiento ni señales de detención"],
        "Pregunta: «¿cómo sabrás si cumpliste la meta?». Si responde con una sensación, pídele un número."),
    reinforce="Escribe en papel una meta medible para una capacidad de tu interés, con línea de base, número y plazo. No hagas pruebas sin calentar ni sin supervisión.",
    extend="Explica por qué una prueba inicial mide un rendimiento y no es una evaluación del cuerpo de la persona.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 11 (opciones de programa de ejemplo, inventadas). Ignacia quiere subir de 9 a 13 minutos seguidos de caminata-trote en 4 semanas. "
     "Opción A: 3 veces por semana, 15 minutos de caminata-trote continuo suave en la parte principal. Opción B: 1 vez por semana, 60 minutos exigentes. "
     "Opción C: 3 veces por semana, 15 minutos de estiramientos suaves. Opción D: 6 veces por semana sin descanso, 40 minutos exigentes.")
build(
    O3, 2, F,
    use="Aprenderé a elegir un tipo de entrenamiento que calce con la meta usando principios como especificidad, sobrecarga y recuperación, y a describir un programa con frecuencia, intensidad, tiempo y tipo.",
    prior=["Sé fijar una meta medible.", "Sé qué es una línea de base.", "Sé que el descanso es parte del entrenamiento."],
    explain=[
        "Los programas se apoyan en principios. La especificidad dice que se mejora principalmente lo que se entrena: para mejorar la resistencia hay que practicar esfuerzos continuos, no solo estiramientos. La sobrecarga es pedir al cuerpo algo mayor a lo habitual, de forma gradual, para que se adapte; la progresión es ese aumento paso a paso. La recuperación es el descanso necesario para que el cuerpo se adapte.",
        "Para describir un programa se usa la sigla FITT: frecuencia (cuántas veces por semana), intensidad (qué tan exigente), tiempo (cuánto dura cada sesión) y tipo (qué actividad). Cambiar una sola de estas letras a la vez permite saber qué produjo el efecto. Aumentar todo junto eleva el riesgo de cansancio excesivo y de lesión.",
        "Un programa seguro incluye calentamiento, enfriamiento, agua y señales de detención: ante dolor, mareo o malestar se para y se avisa a una persona adulta o a un profesional de la salud. Las cifras de intensidad de este cuaderno son de ejemplo; la intensidad adecuada para cada persona la orienta su docente o un profesional.",
    ],
    vocab=[("especificidad", "se mejora principalmente lo que se entrena"), ("sobrecarga", "pedir algo mayor a lo habitual, de forma gradual"), ("progresión", "aumento paso a paso de una condición del programa"), ("recuperación", "descanso necesario para adaptarse"), ("FITT", "frecuencia, intensidad, tiempo y tipo")],
    worked=[
        ("Elegir según especificidad", "Una persona de ejemplo quiere mejorar su resistencia al trote. Opciones: (A) trote suave continuo 3 veces por semana; (B) solo estiramientos. ¿Cuál elige?", ["La resistencia se mejora practicando esfuerzos continuos: la especificidad.", "Los estiramientos trabajan la flexibilidad, otra capacidad."], "La opción A"),
        ("Describir con FITT", "Un programa de ejemplo: caminata rápida, 4 días por semana, 25 minutos, esfuerzo suave. Descríbelo con FITT.", ["Frecuencia: 4 días por semana; tiempo: 25 minutos.", "Tipo: caminata rápida; intensidad: suave."], "F: 4 días; I: suave; T: 25 minutos; T: caminata rápida"),
    ],
    mistakes=[("Entrenar una capacidad distinta de la que se quiere mejorar.", "No se cumple la especificidad: la mejora aparece sobre todo en lo que se practica.", "Elige sesiones que se parezcan a la meta."),
              ("Subir frecuencia, tiempo e intensidad a la vez.", "No se sabe qué cambio funcionó y se arriesga la recuperación.", "Cambia una sola condición por vez.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué dice el principio de especificidad?', 'Se mejora sobre todo lo que se entrena, así que se imita la meta', 'Todas las capacidades mejoran igual con cualquier ejercicio que se haga', 'Se mejora igual lo que se entrena y lo que no, porque el cuerpo se adapta a todo', 'Especificidad significa que la mejora está ligada a lo que se practica.'),
        ('abc', 'En Ciencias del ejercicio: ¿qué significa la sigla FITT?', 'Frecuencia, intensidad, tiempo y tipo de ejercicio', 'Fuerza, intensidad, técnica y tipo de entrenamiento', 'Flexibilidad, intensidad, tiempo y tolerancia al esfuerzo', 'FITT resume las cuatro condiciones que describen un programa.'),
        ('abc', '{F} ¿Cuál es la frecuencia de la opción A?', '3 veces por semana', '15 minutos por sesión', '6 veces por semana', 'La frecuencia cuenta cuántas veces por semana se entrena.'),
        ('abc', '{F} Según la especificidad, ¿qué opción conviene para subir de 9 a 13 minutos de caminata-trote continuo?', 'La A, porque practica caminata-trote continuo con regularidad', 'La C, porque los estiramientos mejoran la resistencia más que cualquier práctica', 'La B, porque una sola sesión larga basta para adaptarse', 'La A entrena lo mismo que la meta y con regularidad.'),
        ('abc', '{F} ¿Qué problema tiene la opción D?', 'No incluye descanso y exige mucho, lo que aumenta el riesgo de cansancio', 'Es demasiado corta para producir cambios en la resistencia de la persona', 'No incluye ejercicio de ningún tipo, solo una rutina de estiramientos', 'Seis sesiones exigentes sin descanso no dejan recuperar al cuerpo.'),
        ('abc', '¿Qué es la sobrecarga en un programa?', 'Pedir algo mayor a lo habitual, de forma gradual, para que el cuerpo se adapte', 'Pedir el máximo esfuerzo posible desde la primera sesión de entrenamiento', 'Repetir siempre exactamente lo mismo, sin ningún cambio durante semanas', 'La sobrecarga es un aumento gradual, no un esfuerzo máximo ni una repetición idéntica.'),
        ('=', '{F} En la opción A, cada sesión suma 8 minutos de calentamiento y 5 de enfriamiento, además de la parte principal. ¿Cuántos minutos por semana?', '3*(15+8+5)', 'Se suman los minutos de las tres partes de cada sesión y se multiplican por las 3 sesiones.', ' minutos'),
        ('abc', '{F} Ignacia quiere aplicar sobrecarga a la opción A sin riesgo. ¿Qué cambio es adecuado?', 'Aumentar 1 minuto el trote cada semana y mantener lo demás igual', 'Duplicar la duración, la frecuencia y la intensidad en la semana 2', 'Quitar los descansos entre sesiones para ganar tiempo de práctica', 'Un aumento pequeño de una sola condición es una progresión segura.'),
        ('ab', '{F} ¿Qué letra de FITT cambia si Ignacia pasa de 3 a 4 sesiones por semana?', 'La frecuencia', 'El tipo', 'Cambiar el número de sesiones semanales modifica la frecuencia.'),
        ('abc', 'Un compañero dice: «Para mejorar mi resistencia bastan los estiramientos todos los días». ¿Qué principio contradice?', 'La especificidad: la práctica debe parecerse a lo que se quiere mejorar', 'La sobrecarga: los estiramientos son demasiado exigentes', 'La progresión: los estiramientos se hacen demasiado rápido', 'Los estiramientos trabajan otra capacidad; no entrenan la resistencia.'),
        ('abc', 'Un programa de ejemplo sube a la vez frecuencia, tiempo e intensidad de la semana 1 a la 2. ¿Qué dificulta eso?', 'Saber qué cambio produjo el cansancio o la mejora, y aumenta el riesgo', 'Nada, porque más cambios siempre mejoran más el rendimiento de todos', 'Medir con precisión el tiempo de cada una de las sesiones de la semana', 'Con varios cambios juntos no se puede atribuir el efecto.'),
        ('=', '{F} Con la opción A, tres sesiones por semana y un aumento de 1 minuto de trote por semana desde los 15 minutos, ¿cuántos minutos de parte principal suma en 4 semanas?', '3*(15+16+17+18)', 'Se suman los minutos por sesión de cada semana y se multiplican por las 3 sesiones semanales.', ' minutos'),
        ('abc', 'Dos programas buscan lo mismo. Uno cambia una condición cada semana y registra; el otro cambia todo cada semana y no registra. ¿Cuál permite evaluar mejor?', 'El primero, porque permite relacionar cada cambio con el resultado', 'El segundo, porque cambiar todo cubre más posibilidades', 'Ninguno, porque evaluar un programa no es necesario', 'Para evaluar hay que cambiar una condición por vez y registrar.'),
    ],
    ctx=('abc', 'Camila, persona ficticia, quiere mejorar su resistencia. Plan 1: caminata-trote continuo 3 veces por semana, más 1 minuto por semana, esfuerzo suave a moderado. Plan 2: sesiones muy exigentes todos los días, sin ningún descanso. Plan 3: solo estiramientos 3 veces por semana. ¿Cuál es el más coherente?', 'El plan 1', 'El plan 2', 'El plan 3', 'Solo el plan 1 respeta especificidad, progresión gradual y recuperación.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué significa FITT?", "Frecuencia, intensidad, tiempo y tipo", "Son las cuatro condiciones que describen un programa."),
        ("¿Qué principio dice que se mejora lo que se entrena?", "La especificidad", "Las sesiones deben parecerse a la meta."),
        ("¿Cuántas condiciones conviene aumentar a la vez?", "Una sola", "Así se sabe qué produjo el efecto."),
    ],
    op=("Describe con FITT un programa de 4 semanas para una persona ficticia que quiere mejorar su resistencia, tiene 3 días por semana y 40 minutos por día, y prefiere caminar o trotar en grupo. Indica qué condición aumentarás cada semana (solo una), cómo incluyes la recuperación y dos medidas de seguridad.",
        "F: 3 días. I: suave a moderada. T: 20 minutos de parte principal más calentamiento y enfriamiento. T: caminata-trote en grupo. Progresión: +1 minuto por semana en el tiempo, lo demás igual. Recuperación: días de descanso entre sesiones. Seguridad: calentar, agua; ante dolor o mareo, paro y aviso.",
        ["usa FITT completo", "una sola condición aumenta por semana", "incluye recuperación y seguridad"],
        ["programa descrito con FITT y progresión"],
        ["no describir las cuatro letras", "subir varias condiciones a la vez", "olvidar la recuperación"],
        "Pregunta: «¿cuál condición cambia cada semana y cuáles quedan iguales?». Si cambia varias, pídele dejar una."),
    reinforce="Elige una meta y escribe qué tipo de actividad le calza mejor según la especificidad y qué condición aumentarías primero. Hazlo solo en papel.",
    extend="Explica por qué aumentar una sola condición por vez es parte de la sobrecarga y de la progresión.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 12 (programa de ejemplo, inventado, de una persona ficticia llamada Ignacia). Meta: subir su resistencia en 4 semanas. Frecuencia: 3 sesiones por semana (lunes, miércoles y viernes). Tipo: caminata-trote alternado. "
     "Parte principal por sesión: semana 1, 12 minutos; semana 2, 14; semana 3, 16; semana 4, 18. Calentamiento de 8 minutos y enfriamiento de 5 minutos en cada sesión. "
     "Intensidad: esfuerzo percibido entre 4 y 6 de 10 (cifras de ejemplo; tu docente define la zona adecuada). Se lleva agua y se detiene ante dolor, mareo o malestar.")
build(
    O3, 3, F,
    use="Aprenderé a armar un programa de 4 semanas con sesiones completas, progresión gradual y cuidados, y a calcular su duración y su carga de manera ordenada.",
    prior=["Sé describir un programa con FITT.", "Sé aplicar sobrecarga gradual.", "Conozco las señales de detención."],
    explain=[
        "Implementar un programa es llevar el plan a la práctica con orden. Cada sesión tiene tres partes: el calentamiento prepara el cuerpo con movimientos suaves; la parte principal trabaja la capacidad de la meta; el enfriamiento baja poco a poco la exigencia. El programa se escribe por semanas, indicando frecuencia, tipo, tiempo e intensidad.",
        "La progresión reparte el aumento de una condición en pasos pequeños, por ejemplo +2 minutos por semana en la parte principal, mientras el resto se mantiene. Una semana no avanza más rápido porque la anterior fue fácil: se sigue el plan y se registran el esfuerzo y las molestias. Si una sesión se pierde, no se recupera duplicando la siguiente.",
        "Un buen programa prevé las contingencias: calor, lluvia, cansancio o falta de tiempo. En esos casos se acorta o se cambia por una actividad parecida, bajo techo o más suave. Ante dolor, mareo o malestar se detiene la sesión, se descansa y se avisa a una persona adulta o a un profesional de la salud. Los números de este cuaderno son de ejemplo, no una prescripción personal.",
    ],
    vocab=[("sesión", "momento de práctica con calentamiento, parte principal y enfriamiento"), ("parte principal", "trabajo de la capacidad que se quiere mejorar"), ("enfriamiento", "bajada gradual de la exigencia al final"), ("contingencia", "situación imprevista, como lluvia o cansancio"), ("carga", "cantidad y exigencia del trabajo de una sesión o semana")],
    worked=[
        ("Sumar el tiempo de una sesión", "Una sesión de ejemplo tiene 6 minutos de calentamiento, 20 de parte principal y 4 de enfriamiento. ¿Cuánto dura?", ["Suma las tres partes.", "6 + 20 + 4 = 30."], "30 minutos"),
        ("Aplicar una contingencia", "Una persona de ejemplo planeó trote al aire libre y llueve fuerte. ¿Qué hace?", ["No cancela todo ni compensa duplicando después.", "Cambia por una actividad parecida bajo techo o más suave, con calentamiento y agua."], "Cambiar a una actividad parecida bajo techo"),
    ],
    mistakes=[("Compensar una sesión perdida duplicando la siguiente.", "Sube de golpe la carga y deja menos recuperación.", "Sigue el plan y, si hace falta, ajusta una sola condición."),
              ("Omitir el calentamiento o el enfriamiento para ahorrar tiempo.", "Aumenta el riesgo de molestias y de lesión.", "Mantén las tres partes y acorta la parte principal si falta tiempo.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué partes tiene una sesión de entrenamiento?', 'Calentamiento, parte principal y enfriamiento', 'Calentamiento, parte principal y evaluación final del programa', 'Parte principal, descanso total y registro de resultados', 'Las tres partes preparan, trabajan la meta y bajan la exigencia.'),
        ('abc', '{F} ¿Cuántos minutos tiene la parte principal de cada sesión de la semana 1?', '12 minutos', '8 minutos', '5 minutos', 'Los 8 y 5 minutos son calentamiento y enfriamiento; la parte principal tiene 12.'),
        ('=', '{F} ¿Cuántas sesiones tiene el programa en las 4 semanas?', '3*4', 'Se multiplican las 3 sesiones semanales por las 4 semanas.', ' sesiones'),
        ('=', '{F} ¿Cuántos minutos de parte principal suma el programa en las 4 semanas?', '3*(12+14+16+18)', 'Se suman los minutos por sesión de cada semana y se multiplican por las 3 sesiones semanales.', ' minutos'),
        ('=', '{F} ¿Cuántos minutos dura una semana 3 con calentamiento y enfriamiento incluidos?', '3*(16+8+5)', 'Se suman las tres partes de cada sesión de la semana 3 y se multiplican por 3.', ' minutos'),
        ('abc', '{F} ¿Qué condición del programa aumenta de una semana a otra?', 'El tiempo de la parte principal, 2 minutos por semana', 'La frecuencia semanal, que pasa de 3 a 4 sesiones', 'El tipo de actividad, que cambia de caminata a baile', 'La ficha mantiene la frecuencia y el tipo, y sube el tiempo principal.'),
        ('abc', '{F} ¿Por qué el programa cambia solo el tiempo y mantiene lo demás?', 'Para ver si tolera el aumento de tiempo y relacionarlo con los resultados', 'Para que el programa sea más corto y no exija anotar ningún dato', 'Porque el tiempo es lo único que se puede medir en una sesión de trote', 'Un cambio por vez permite relacionar la respuesta con esa condición.'),
        ('=', '{F} Por lluvia se pierde una sesión de la semana 2. ¿Cuántos minutos de parte principal tuvo esa semana?', '2*14', 'Quedan 2 sesiones de 14 minutos de parte principal.', ' minutos'),
        ('ab', '{F} En una sesión hay mucho calor y Ignacia siente mareo. ¿Qué corresponde?', 'Detener la sesión, descansar, tomar agua y avisar a una persona adulta', 'Seguir con la parte principal pero más lento, para no perder la sesión', 'El mareo es una señal de detención y se informa; seguir puede agravarlo.'),
        ('abc', 'Un programa dice: «semana 1: 12 minutos; semana 2: 24; semana 3: 36». ¿Qué problema tiene la progresión?', 'Aumenta demasiado y de golpe, lo que eleva el riesgo de cansancio excesivo', 'Aumenta muy poco para notar cambios en la resistencia de la persona', 'Mezcla los minutos de calentamiento con los del enfriamiento', 'Duplicar y triplicar el tiempo no es una progresión gradual.'),
        ('abc', 'Un programa incluye sesiones exigentes los siete días sin descanso. ¿Qué se descuida?', 'La recuperación: sin descanso el cuerpo no se adapta bien', 'La progresión: el tiempo aumentó demasiado rápido', 'El calentamiento: se hace demasiado corto', 'Sin días de descanso no hay tiempo de recuperación.'),
        ('=', '{F} ¿Cuántos minutos de calentamiento y enfriamiento suman las 12 sesiones del programa?', '12*(8+5)', 'Se suman 8 y 5 minutos de cada sesión y se multiplican por las 12 sesiones.', ' minutos'),
        ('abc', '{F} Quien aplica el programa pregunta qué datos anotar en cada sesión. ¿Cuál respuesta es más completa?', 'Minutos de la parte principal, esfuerzo percibido y cualquier molestia', 'Solo si la sesión se hizo o no se hizo, sin ningún otro detalle', 'Solo el tiempo total de la sesión y el clima de ese día, sin esfuerzo ni molestias', 'Esos tres datos permiten evaluar la carga y la seguridad.'),
    ],
    ctx=('abc', 'Gabriela, persona ficticia, sigue un programa parecido al de la ficha. En la semana 2 falta una sesión por un examen y se siente cansada el viernes. ¿Qué decisión es más razonable?', 'Mantener el plan, suavizar la sesión del viernes y registrar el cansancio', 'Duplicar la sesión del viernes para compensar la que faltó esa semana', 'Saltarse el calentamiento para que la sesión del viernes quede más corta', 'Ante cansancio y una sesión perdida se mantiene el plan y se suaviza una sesión.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué se hace si se pierde una sesión?", "Seguir el plan sin duplicar la siguiente", "Duplicar sube de golpe la carga."),
        ("¿Cuántas condiciones aumentan a la vez en la progresión del programa?", "Una sola", "Así se entiende la respuesta del cuerpo."),
        ("¿Qué haces ante mareo, dolor o malestar durante una sesión?", "Detenerte y avisar a una persona adulta o a un profesional de la salud", "La seguridad va antes que el plan."),
    ],
    op=("Escribe un programa de ejemplo de 4 semanas, 3 sesiones por semana, para una persona ficticia que quiere trabajar su resistencia con caminata rápida y trote suave. Indica por semana los minutos de parte principal (con una progresión pequeña), el calentamiento, el enfriamiento, el esfuerzo percibido de ejemplo y qué hará si llueve o está muy cansada. Calcula los minutos totales de parte principal.",
        "Semana 1: 10; semana 2: 12; semana 3: 14; semana 4: 16 minutos de parte principal; calentamiento 8 y enfriamiento 5 en cada sesión; esfuerzo de ejemplo 4 a 6. Total de parte principal: 3 × (10+12+14+16) = 156 minutos. Si llueve: bajo techo con una actividad parecida. Ante dolor o mareo, paro y aviso.",
        ["progresión pequeña y una sola condición", "calcula bien los minutos", "incluye alternativa y seguridad"],
        ["programa por semanas con cálculo total"],
        ["subir varias condiciones a la vez", "omitir calentamiento o enfriamiento", "no tener alternativa para contingencias"],
        "Pregunta: «¿qué haces si una semana te sientes muy cansada?». Si dice que entrena más fuerte, vuelve a la seguridad."),
    reinforce="Reescribe el programa de la ficha cambiando solo el tiempo de la parte principal y calcula los minutos totales. Solo en papel.",
    extend="Explica por qué prever contingencias hace que un programa sea más seguro y más sostenible.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 13 (registro de ejemplo, inventado, del programa de 4 semanas de Ignacia). Prueba inicial: 9 minutos continuos. Meta: 13 minutos. "
     "Parte principal por sesión: 12, 14, 16 y 18 minutos en las semanas 1 a 4. "
     "Semana 1: 3 de 3 sesiones hechas, esfuerzo 4. Semana 2: 3 de 3, esfuerzo 5. Semana 3: 2 de 3, esfuerzo 6; anotó una molestia en la rodilla en una sesión, se detuvo y avisó a su docente. Semana 4: 3 de 3, esfuerzo 5. Prueba final: 12 minutos continuos.")
build(
    O3, 4, F,
    use="Aprenderé a registrar sesiones, esfuerzo y resultados de un programa, a calcular el avance hacia la meta y a interpretarlo sin juzgar a las personas.",
    prior=["Sé armar un programa con progresión.", "Sé calcular porcentajes sencillos.", "Sé que ante molestias se detiene y se avisa."],
    explain=[
        "Evaluar un programa requiere datos. Un indicador de logro es un dato medible que muestra cuánto se avanza hacia la meta: el resultado de la prueba final comparado con la inicial, las sesiones hechas sobre las planificadas y el esfuerzo percibido. El avance hacia la meta se calcula como porcentaje: mejora lograda dividida por mejora esperada.",
        "Para interpretar se miran juntos los indicadores y las condiciones. Si la meta no se cumplió completa, no es un fracaso: se mide cuánto se avanzó y se revisan posibles causas, como una molestia, una sesión perdida o un aumento muy rápido. La molestia de la rodilla en la semana 3 es una señal que se registra, se informa y se vigila; si vuelve, se consulta a un profesional.",
        "El registro es propio y privado. Las comparaciones válidas son con la prueba inicial de la misma persona, no con los resultados de otras. Ante dolor, mareo o malestar, se detiene la práctica y se avisa a una persona adulta o a un profesional de la salud.",
    ],
    vocab=[("indicador de logro", "dato medible que muestra el avance hacia la meta"), ("prueba final", "medición al terminar el programa, igual a la inicial"), ("avance hacia la meta", "mejora lograda dividida por la mejora esperada"), ("molestia", "sensación incómoda que se registra y se informa"), ("evaluación", "análisis de los datos para decidir ajustes")],
    worked=[
        ("Calcular el avance hacia la meta", "Una persona de ejemplo pasó de 8 a 11 minutos y su meta era 12. ¿Qué porcentaje de la mejora esperada logró?", ["Mejora lograda: 11 − 8 = 3. Mejora esperada: 12 − 8 = 4.", "3 de 4 es 75 %."], "75 %"),
        ("Interpretar una meta no cumplida", "Con ese 75 %, ¿se concluye que el programa fracasó?", ["No: hubo avance y se pueden revisar causas.", "Se ajusta una condición y se evalúa de nuevo."], "No: se evalúa el avance y se ajusta"),
    ],
    mistakes=[("Declarar fracaso si no se alcanzó la meta completa.", "Ignora el avance logrado y las causas posibles.", "Calcula el avance y revisa qué condición ajustar."),
              ("Tapar una molestia para no perder la meta.", "Puede convertirse en una lesión.", "Registra la molestia, detén la sesión y avisa.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es un indicador de logro?', 'Un dato medible que muestra cuánto se avanza hacia la meta', 'Una opinión sobre el cuerpo de la persona que entrena', 'El nombre de la actividad que se practica en la semana', 'Un indicador es medible y se refiere al avance, no a opiniones sobre el cuerpo.'),
        ('=', '{F} ¿Cuántas sesiones hizo en total en las 4 semanas?', '3+3+2+3', 'Se suman las sesiones hechas en cada una de las cuatro semanas.', ' sesiones'),
        ('=', '{F} ¿Cuántos minutos mejoró en la prueba continua, entre la inicial y la final?', '12-9', 'Se resta la prueba inicial a la final.', ' minutos'),
        ('=', '{F} ¿Cuántas sesiones planificadas no hizo?', '12-(3+3+2+3)', 'Se restan las sesiones hechas de las 12 planificadas.', ' sesión'),
        ('abc', '{F} ¿Se cumplió la meta de 13 minutos continuos?', 'No: llegó a 12, o sea 3 de los 4 minutos propuestos', 'Sí, porque mejoró más de 2 minutos respecto de su prueba inicial', 'Sí, porque hizo más de 10 sesiones de las 12 planificadas', 'La meta era 13; llegó a 12, así que avanzó pero no la cumplió.'),
        ('abc', '{F} ¿Qué se observa entre el esfuerzo y las sesiones de la semana 3?', 'El esfuerzo fue mayor (6) y se hizo una sesión menos', 'El esfuerzo más bajo coincide con menos sesiones', 'Se hicieron todas las sesiones con el mayor esfuerzo', 'En la semana 3 el esfuerzo subió a 6 y solo se hicieron 2 de 3 sesiones.'),
        ('=', '{F} ¿Qué porcentaje de la mejora esperada, de 9 a 13 minutos, logró Ignacia?', '(12-9)*100/(13-9)', 'Se divide la mejora lograda de 3 minutos entre la esperada de 4 y se pasa a porcentaje.', ' %'),
        ('abc', '{F} ¿Qué decisión conviene tras la molestia de rodilla de la semana 3?', 'Detener la sesión, registrar la molestia y consultar a un profesional si reaparece', 'Aumentar el esfuerzo para que el cuerpo se acostumbre al dolor', 'Ocultar la molestia para no perder la meta', 'Una molestia se registra y se informa; ocultarla o forzar puede agravarla.'),
        ('ab', '{F} Para saber si el programa funcionó, ¿qué dato es más sólido?', 'La prueba final repetida en las mismas condiciones que la inicial', 'La impresión de otras personas sobre cuánto le costó a Ignacia', 'Una prueba final en iguales condiciones permite comparar con la línea de base.'),
        ('abc', 'Alguien dice: «Como no llegó a 13, el programa fracasó». ¿Qué corresponde?', 'Evaluar el avance logrado y ajustar el programa en vez de declarar fracaso', 'Declararlo fracaso, porque una meta no cumplida no deja nada', 'Cambiar la meta a 12 y decir que se cumplió, sin revisar nada', 'El avance de 75 % es información para ajustar, no un fracaso.'),
        ('abc', 'Un registro dice solo: «mejoré mucho». ¿Qué le falta para evaluar el programa?', 'Datos medibles: prueba inicial, prueba final, sesiones y esfuerzo', 'Más adjetivos sobre cómo se sintió durante todo el programa', 'Los resultados de otras personas del curso, para compararlos', 'Evaluar necesita datos medibles y comparables.'),
        ('=', '{F} ¿Cuántos minutos de parte principal sumó en total, considerando que en la semana 3 hizo solo 2 sesiones?', '3*12+3*14+2*16+3*18', 'Se multiplican los minutos de cada semana por las sesiones que se hicieron y se suman.', ' minutos'),
        ('abc', '{F} Una persona compara: «Ignacia subió 3 minutos y yo 5, así que ella entrenó peor». ¿Qué corresponde?', 'Cada persona se evalúa contra su propia línea de base y meta', 'Aceptar la comparación, porque 5 minutos es más que 3 minutos', 'Pedir a Ignacia que repita la prueba hasta superar los 5 minutos', 'Las comparaciones válidas son con la línea de base propia, no entre personas.'),
    ],
    ctx=('abc', 'Camilo, persona ficticia, tuvo prueba inicial de 7 minutos, meta de 11 y prueba final de 10; hizo 11 de 12 sesiones. ¿Cómo se interpreta?', 'Avanzó 3 de 4 minutos, o 75 %, con buena asistencia, y se ajusta una condición', 'No se puede interpretar nada, porque la meta no se cumplió completa ni a tiempo', 'El programa fue un fracaso total, porque faltó una sesión de las doce', 'Hay avance claro y buena adherencia; lo razonable es ajustar una condición y volver a medir.'),
    sc=[
        ("En Ciencias del ejercicio: ¿cómo se calcula el avance hacia la meta?", "Mejora lograda dividida por mejora esperada", "Así se expresa el avance como porcentaje."),
        ("¿Con quién se comparan los resultados del programa?", "Con la prueba inicial de la misma persona", "Cada persona parte de un punto distinto."),
        ("¿Qué haces ante una molestia durante una sesión?", "Detenerte, registrarla y avisar a una persona adulta o a un profesional de la salud", "La salud va antes que la meta."),
    ],
    op=("Con estos datos de ejemplo de una persona ficticia: prueba inicial 10 minutos continuos; meta 15; sesiones hechas 10 de 12; esfuerzo 4, 5, 6 y 5 en las cuatro semanas; prueba final 14 minutos. Calcula el avance hacia la meta, las sesiones hechas y la adherencia, interpreta con cuidado y propone un ajuste de una sola condición.",
        "Mejora lograda 4 y esperada 5: avance de 80 %. Sesiones: 10 de 12, o sea 83 % de adherencia. El esfuerzo subió en la semana 3 y puede explicar sesiones faltantes. Ajuste: mantener la carga una semana más y volver a medir. Seguridad: ante dolor o mareo, paro y aviso.",
        ["calcula avance y adherencia", "interpreta sin declarar fracaso", "propone un ajuste de una condición"],
        ["cálculos e interpretación con ajuste"],
        ["declarar fracaso sin datos", "comparar con otras personas", "cambiar varias condiciones a la vez"],
        "Pregunta: «¿cuántos minutos faltaron para la meta?». Si no sabe, pídele que reste."),
    reinforce="Con datos inventados, calcula el avance hacia una meta y escribe dos posibles causas de que no se cumpliera completa.",
    extend="Explica por qué evaluar un programa con indicadores es más útil que decir solo «funcionó» o «no funcionó».",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 14 (caso de ejemplo, inventado). Joaquina y Pablo, estudiantes ficticios, entrenan juntos en la plaza 3 días por semana, con permiso y supervisión de su docente. "
     "Roles que rotan en cada sesión: guía (propone y conduce), observadora u observador (revisa seguridad y técnica) y registrador o registradora (anota minutos y esfuerzo). "
     "Reglas acordadas: respetar el ritmo de cada persona, ofrecer variantes más suaves o más exigentes, no comentar cuerpos, mantener privados los registros de cada una y detener la práctica ante dolor, mareo o malestar. "
     "Resultados tras 4 semanas: Joaquina pasó de 9 a 12 minutos continuos y Pablo de 14 a 17. Meta de cada uno: subir 4 minutos.")
build(
    O3, 5, F,
    use="Aprenderé a evaluar y ajustar un programa, y a colaborar para mejorar la condición física de otras personas con roles claros, respeto por la individualidad, privacidad y seguridad.",
    prior=["Sé evaluar un programa con indicadores.", "Sé que cada persona parte de una línea de base distinta.", "Conozco las señales de detención."],
    explain=[
        "Evaluar y ajustar significa mirar los indicadores, decidir qué cambiar y volver a medir. Si la meta no se alcanzó, se mantiene la carga una semana más, se alarga el plazo o se cambia una sola condición. Si hubo cansancio excesivo o molestias, se reduce la carga y se consulta. Nunca se ajusta aumentando todo a la vez ni usando el dolor como guía.",
        "Entrenar con otras personas exige roles y reglas. Un rol de guía conduce la sesión, quien observa cuida la seguridad y la técnica, y quien registra anota los datos. Los roles rotan para que todas las personas participen. Cada persona tiene su propia línea de base y sus necesidades: se ofrecen variantes más suaves o más exigentes y se evita comparar cuerpos o resultados para juzgar. Los registros de cada persona son privados.",
        "Mejorar la condición física de otras personas también tiene límites: se comparten esquemas generales, no prescripciones personales, y cuando alguien tiene una indicación de salud o dudas se recomienda consultar a su docente o a un profesional. Si alguien siente dolor, mareo o malestar, se detiene su participación, se descansa y se avisa a una persona adulta responsable.",
    ],
    vocab=[("rol", "función que cumple cada persona en la sesión"), ("variante", "versión más suave o más exigente de una actividad"), ("privacidad", "derecho a que los registros propios no se difundan"), ("ajuste", "cambio de una condición según los datos"), ("esquema general", "plan básico que se adapta a cada persona")],
    worked=[
        ("Ajustar tras una meta parcial", "Dos estudiantes de ejemplo lograron 3 de los 4 minutos propuestos. ¿Qué ajuste razonable hay?", ["Hubo avance de 75 %, así que el plan funciona en parte.", "Mantén la carga una semana más y vuelve a medir."], "Mantener la carga una semana más y volver a medir"),
        ("Organizar roles", "Tres estudiantes de ejemplo entrenan juntos 12 sesiones. ¿Cómo reparten el rol de guía?", ["Rotan el rol de guía por igual.", "12 sesiones entre 3 personas son 4 sesiones cada una."], "Cuatro sesiones de guía por persona"),
    ],
    mistakes=[("Exigir a todas las personas la misma carga «para que sea justo».", "Ignora que cada una parte de una línea de base distinta.", "Ofrece variantes y ajusta según cada persona."),
              ("Compartir los registros de una persona sin su permiso.", "Los registros son privados y pueden exponer o avergonzar.", "Comparte solo lo que cada persona decide compartir.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué hace la persona que observa en una sesión en parejas?', 'Revisa la seguridad y la técnica y avisa si hay riesgo', 'Compara el cuerpo de las demás personas', 'Decide que otra persona debe seguir pese al dolor', 'Quien observa cuida la seguridad y la técnica, no juzga cuerpos.'),
        ('abc', '{F} ¿Qué rol anota minutos y esfuerzo?', 'La persona registradora', 'La persona guía', 'La persona observadora', 'Registrar es anotar los datos de la sesión.'),
        ('=', '{F} ¿Cuántos minutos continuos subió Pablo en las 4 semanas?', '17-14', 'Se resta su prueba inicial a la final.', ' minutos'),
        ('=', '{F} ¿Qué porcentaje de su meta de 4 minutos logró Joaquina?', '(12-9)*100/4', 'Se divide su mejora de 3 minutos entre los 4 propuestos y se pasa a porcentaje.', ' %'),
        ('abc', '{F} ¿Cuál de las reglas protege la privacidad?', 'Mantener privados los registros de cada persona', 'Rotar los roles de guía, observación y registro', 'Ofrecer variantes más suaves o más exigentes', 'La regla de registros privados protege los datos de cada persona.'),
        ('abc', '¿Para qué sirven las variantes más suaves o más exigentes?', 'Para que cada persona entrene según su nivel y sus condiciones', 'Para que todas las personas hagan siempre exactamente lo mismo', 'Para decidir quién es mejor y quién necesita esforzarse más', 'Las variantes adaptan la actividad a cada persona sin compararlas.'),
        ('abc', '{F} Pablo dice que siente dolor de tobillo en una sesión. ¿Qué hace el grupo?', 'Detener su participación, descansar y avisar a la persona adulta que supervisa', 'Pedirle que siga tres minutos más para completar la meta del programa', 'Tapar el tema para que el grupo no pierda las sesiones planificadas', 'El dolor es señal de detención y se informa a una persona adulta.'),
        ('=', 'En un grupo de 4 estudiantes ficticios con 24 sesiones, el rol de guía rota por igual. ¿Cuántas sesiones guía cada persona?', '24/4', 'Se reparten las 24 sesiones en partes iguales entre las 4 personas.', ' sesiones'),
        ('ab', '{F} Una amiga que no participa pide el programa. ¿Qué corresponde?', 'Compartir el esquema general y sugerirle consultar a su docente', 'Entregarle los registros privados de Joaquina y Pablo para que los compare', 'Se comparte un esquema general; los registros son privados y la adaptación la orienta un profesional.'),
        ('abc', 'Alguien propone: «Pablo debe entrenar con la carga de Joaquina para que sea igual». ¿Qué falla?', 'Cada persona tiene otra línea de base y otras necesidades', 'Nada, porque la igualdad exige la misma carga para todas las personas', 'Joaquina debe entrenar menos para igualar a Pablo en la prueba final', 'La carga se adapta a cada persona, no se iguala entre ellas.'),
        ('abc', '{F} Los dos lograron 75 % de su meta de 4 minutos. ¿Qué ajuste es razonable?', 'Mantener la carga una semana más y volver a medir', 'Duplicar la carga para llegar a la meta lo antes posible', 'Eliminar los días de descanso para ganar tiempo de práctica', 'Con avance parcial se mantiene o se ajusta una condición, sin subir todo a la vez.'),
        ('=', '{F} Si cada uno agrega una semana de 3 sesiones de 40 minutos, ¿cuántos minutos de práctica suman los dos?', '2*3*40', 'Se calculan los minutos de una persona y se multiplican por las dos personas.', ' minutos'),
        ('abc', 'Un compañero dice: «Mejoremos la condición física de todo el curso con el mismo programa». ¿Qué conviene en cambio?', 'Entregar un esquema común y adaptar tiempos y variantes a cada línea de base', 'Aplicar el mismo programa sin cambios aunque algunas personas no lo toleren', 'Dejar que cada persona improvise sin plan ni registro durante el mes', 'Un esquema común con adaptaciones respeta la individualidad y mantiene el orden.'),
    ],
    ctx=('abc', 'Sofía y Tomás, estudiantes ficticios, entrenan juntos. Sofía logró 100 % de su meta; Tomás, 50 %, con una semana de poco sueño. Una compañera dice que Tomás «no se esfuerza». ¿Qué corresponde?', 'Revisar los datos de Tomás, como sueño y carga, y ajustar su programa', 'Pedirle que haga lo mismo que Sofía hasta lograr igualarla en la meta', 'Aceptar que Tomás no sirve para el programa y sacarlo del grupo', 'El ajuste se basa en datos propios y condiciones, no en etiquetas.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué se hace si la meta se cumple solo en parte?", "Se evalúa el avance y se ajusta una condición", "El avance parcial también es información."),
        ("¿Quién decide si un registro personal se comparte?", "La persona dueña del registro", "Los registros son propios y se mantienen privados."),
        ("¿Qué se hace si alguien siente dolor o mareo?", "Se detiene su participación y se avisa a una persona adulta o a un profesional de la salud", "La seguridad de todas las personas va primero siempre."),
    ],
    op=("Imagina que organizas entrenamientos con dos personas ficticias que parten de líneas de base distintas (una trota 6 minutos continuos y otra 12) y tienen 3 días por semana. Define roles, dos reglas de respeto y privacidad, dos variantes (suave y exigente) y qué ajustarías si una persona avanza el 50 % de su meta. Incluye una señal de detención.",
        "Roles que rotan: guía, observadora y registradora. Reglas: no comentar cuerpos y registros privados. Variantes: trote de 6 minutos con pausas caminando y trote de 12 con ritmo estable. Si alguien avanza 50 %, mantengo su carga una semana más y vuelvo a medir. Señal: dolor o mareo, paro y aviso.",
        ["roles y reglas de respeto", "variantes según línea de base", "ajuste razonable y señal de detención"],
        ["descripción de organización, variantes y ajuste"],
        ["la misma carga para todas las personas", "comentar cuerpos o resultados", "sin señal de detención"],
        "Pregunta: «¿cómo tratas distinto a dos personas que parten de puntos distintos sin compararlas?». Si dice que da lo mismo, pídele variantes."),
    reinforce="Escribe tres reglas de convivencia para entrenar en grupo y tres variantes para que participen personas con distinto nivel. Solo en papel.",
    extend="Explica por qué colaborar para mejorar la condición física de otras personas requiere privacidad, respeto y consulta a profesionales ante dudas de salud.",
)

# ============================================================ OAC-04, clase 1
F = ("Ficha 15 (datos de ejemplo, inventados). Dos grupos ficticios de 10 estudiantes hicieron la misma prueba de 1 kilómetro al inicio y después de 8 semanas. "
     "El grupo A practicó 3 sesiones semanales de caminata-trote suave. El grupo B mantuvo su rutina habitual. "
     "Tiempo promedio del grupo en la prueba: grupo A, inicio 400 segundos y final 380 segundos; grupo B, inicio 400 segundos y final 398 segundos. "
     "El promedio es la suma de los tiempos dividida por el número de estudiantes.")
build(
    O4, 1, F,
    use="Aprenderé a analizar el efecto de la actividad física regular en el rendimiento usando datos de grupos, un grupo de comparación y promedios, y a decir con cuidado qué se puede concluir.",
    prior=["Sé qué es una adaptación crónica.", "Sé calcular porcentajes sencillos.", "Sé registrar mediciones en condiciones iguales."],
    explain=[
        "La actividad física regular se asocia a mejoras en la resistencia, la fuerza y la coordinación, y también a beneficios de salud como más energía, mejor ánimo y mejor sueño. Para analizar su efecto en el rendimiento se comparan mediciones antes y después, y se usa un grupo de comparación: un grupo que no recibe el cambio estudiado y sirve de referencia para ver qué pasa sin él.",
        "Un promedio resume un grupo con un solo número: suma de los valores dividida por la cantidad. Es útil para comparar grupos, pero no describe a cada persona: algunas estarán por encima y otras por debajo. Una diferencia pequeña entre dos promedios puede ser variación normal, y un solo estudio con pocas personas no permite generalizar a todas las personas.",
        "Los datos de este cuaderno son de ejemplo. Analizamos efectos sobre el rendimiento, no sobre los cuerpos: nadie compara ni juzga a otras personas. Si al practicar alguien siente dolor, mareo o malestar, detiene la actividad y avisa a una persona adulta o a un profesional de la salud.",
    ],
    vocab=[("grupo de comparación", "grupo que no recibe el cambio estudiado y sirve de referencia"), ("promedio", "suma de los valores dividida por la cantidad de valores"), ("efecto", "cambio que se asocia a una práctica"), ("generalizar", "extender una conclusión a todas las personas"), ("variación normal", "diferencia pequeña que puede deberse al azar")],
    worked=[
        ("Calcular un promedio", "Tres estudiantes de ejemplo tardan 300, 330 y 360 segundos. ¿Cuál es el promedio?", ["Suma los tiempos: 300 + 330 + 360 = 990.", "Divide entre 3: 990 ÷ 3 = 330."], "330 segundos"),
        ("Usar el grupo de comparación", "Un grupo que practicó bajó 15 segundos y otro grupo que no practicó bajó 1 segundo. ¿Qué se dice con cuidado?", ["La diferencia entre grupos es 14 segundos.", "Sugiere un efecto de la práctica, pero se necesitan más datos para generalizar."], "Sugiere un efecto de la práctica, sin generalizar"),
    ],
    mistakes=[("Concluir un efecto mirando solo a un grupo que practicó.", "Sin grupo de comparación no se sabe si habría mejorado igual sin practicar.", "Compara con un grupo que no practicó."),
              ("Pensar que el promedio describe a cada persona.", "Dentro de un grupo hay valores mayores y menores que el promedio.", "Interpreta el promedio como resumen del grupo, no de cada persona.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es un grupo de comparación?', 'Un grupo que no recibe el cambio estudiado y sirve como referencia', 'El grupo que obtiene el mejor resultado en la prueba final', 'El grupo que tiene más personas participando en la prueba', 'Sirve para ver qué ocurre sin el cambio estudiado.'),
        ('=', '{F} ¿Cuántos segundos bajó el promedio del grupo A?', '400-380', 'Se resta el promedio final al inicial.', ' segundos'),
        ('=', '{F} ¿Cuántos segundos bajó el promedio del grupo B?', '400-398', 'Se resta el promedio final al inicial.', ' segundos'),
        ('abc', '{F} ¿Qué comparación muestra el posible efecto de la práctica regular?', 'El grupo A bajó 20 segundos y el B solo 2, con el mismo punto de partida', 'El grupo B bajó más porque no cambió su rutina', 'No se puede comparar, porque los grupos tienen estudiantes distintos', 'Con igual punto de partida, el grupo que practicó mejoró bastante más.'),
        ('=', 'Otro grupo de 5 estudiantes ficticios tiene tiempos de 390, 410, 400, 420 y 380 segundos. ¿Cuál es el promedio?', '(390+410+400+420+380)/5', 'Se suman los cinco tiempos y se divide la suma entre 5.', ' segundos'),
        ('abc', '¿Por qué un promedio no describe a cada persona del grupo?', 'Porque algunas personas están por encima y otras por debajo del promedio', 'Porque el promedio siempre es el mejor resultado de todo el grupo', 'Porque el promedio solo sirve cuando hay dos personas en el grupo', 'Un promedio resume al grupo; los valores individuales pueden ser distintos.'),
        ('abc', '{F} ¿Qué conclusión es adecuada?', 'La práctica se asocia a una mejora del promedio, pero faltan más datos', 'La práctica regular produce la misma mejora en cada estudiante del grupo', 'La práctica regular no cambia nada en el rendimiento del grupo', 'Los datos sugieren una asociación, no una mejora idéntica en todas las personas.'),
        ('=', '{F} Si cada estudiante del grupo A asistió a todas sus sesiones, de 45 minutos, durante las 8 semanas, ¿cuántos minutos practicó en total?', '3*8*45', 'Se multiplican las 3 sesiones semanales por las 8 semanas y por 45 minutos.', ' minutos'),
        ('ab', '{F} ¿Se puede afirmar que el cambio de 2 segundos en el grupo B es una mejora real?', 'No: con una diferencia tan pequeña puede ser variación normal', 'Sí, porque cualquier diferencia siempre es una mejora', 'Una diferencia mínima puede deberse al azar y no se interpreta como mejora real.'),
        ('abc', 'Un estudiante concluye: «Como el grupo A mejoró, yo mejoraré exactamente 20 segundos». ¿Qué falla?', 'Un promedio de grupo no predice el cambio exacto de una persona', 'Nada, porque el promedio es igual para todas las personas', 'Que el grupo B no cuenta', 'Cada persona puede cambiar distinto del promedio.'),
        ('abc', 'Alguien propone que el grupo A practique y además reciba una bebida especial, mientras el B no cambia nada. ¿Qué problema tiene?', 'Cambió dos cosas a la vez y no se sabe cuál produjo el efecto', 'Ninguno, porque más cambios siempre dan más información al estudio', 'Que el grupo B debe practicar también más de tres veces por semana', 'Para atribuir el efecto, solo debe cambiar una cosa entre los grupos.'),
        ('=', '{F} ¿Qué porcentaje del tiempo inicial bajó el promedio del grupo A?', '(400-380)*100/400', 'Se calcula la baja de 20 segundos y se divide entre los 400 iniciales.', ' %'),
        ('abc', '{F} Un informe dice que la actividad física «mejora todo en todas las personas» a partir de estos datos. ¿Qué limitación tiene?', 'Son dos grupos pequeños y una sola prueba, no se puede generalizar', 'Ninguna: con 10 estudiantes se puede asegurar para todas las personas', 'Que el promedio no se puede calcular con tan pocos estudiantes', 'Pocos datos de una prueba no permiten generalizar.'),
    ],
    ctx=('abc', 'En otro colegio de ejemplo, el grupo C (practicó 8 semanas) bajó su tiempo promedio de 420 a 405 segundos, y el grupo D (no practicó) de 420 a 419 segundos. ¿Qué es lo más razonable decir?', 'La práctica se asocia a una mejora mayor, aunque faltan datos para generalizar', 'La práctica no sirve, porque el grupo D también bajó su tiempo promedio', 'El grupo D es mejor porque cambió menos que el grupo que practicó', 'El grupo que practicó mejoró 15 segundos y el otro 1, con el mismo inicio.'),
    sc=[
        ("En Ciencias del ejercicio: ¿para qué sirve un grupo de comparación?", "Para ver qué ocurre sin el cambio estudiado", "Así se interpreta mejor el efecto."),
        ("¿Cómo se calcula un promedio?", "Sumando los valores y dividiendo por la cantidad", "El promedio resume al grupo con un número."),
        ("¿Qué haces si sientes dolor o mareo al practicar?", "Detenerte y avisar a una persona adulta o a un profesional de la salud", "La seguridad va antes que cualquier análisis."),
    ],
    op=("Con estos datos de ejemplo: el grupo X (8 estudiantes ficticios) practicó 3 veces por semana y bajó su tiempo promedio de 410 a 395 segundos en 8 semanas; el grupo Y (8 estudiantes ficticios) no cambió su rutina y bajó de 410 a 409. Calcula las bajas, compara con cuidado y escribe una conclusión y una limitación. Incluye una medida de seguridad al practicar.",
        "Grupo X bajó 15 segundos y el grupo Y 1. La práctica se asocia a una mejora mayor, pero con dos grupos pequeños no se puede generalizar a todas las personas. Seguridad: calentar y, ante dolor o mareo, parar y avisar a una persona adulta.",
        ["calcula las dos bajas", "conclusión cuidadosa con grupo de comparación", "una limitación y una medida de seguridad"],
        ["cálculos, conclusión y limitación escritos"],
        ["afirmar que todas las personas mejoran lo mismo", "ignorar el grupo de comparación", "olvidar la seguridad"],
        "Pregunta: «¿qué grupo sirve de referencia y por qué?». Si no sabe, pídele que busque el grupo que no cambió su rutina."),
    reinforce="Con datos inventados de dos grupos, calcula una baja de promedio para cada uno y escribe una conclusión que no exagere.",
    extend="Explica por qué un solo estudio con pocas personas no permite afirmar el mismo efecto para todas las personas.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 16 (menú de ejemplo, inventado, de un día de una estudiante ficticia que practica deporte escolar). "
     "Desayuno: pan con palta, leche y una fruta. Almuerzo: lentejas con arroz y ensalada de verduras. Once: yogur y una fruta. Cena: pescado al horno con verduras y papas. Durante el día: agua.")
build(
    O4, 2, F,
    use="Aprenderé en términos generales qué aportan los grupos de alimentos y el agua al rendimiento y la recuperación, a reconocer una alimentación variada y a pedir orientación profesional cuando las necesidades son personales.",
    prior=["Sé que el descanso ayuda a la recuperación.", "Sé que las necesidades varían entre personas.", "Sé que ante malestar se avisa a una persona adulta."],
    explain=[
        "Una alimentación saludable es variada, suficiente y equilibrada: incluye frutas y verduras, legumbres, cereales, lácteos, pescados o carnes, y agua. Cada grupo aporta nutrientes distintos. Los carbohidratos son la fuente principal de energía para moverse y para el cerebro. Las proteínas ayudan a construir y reparar tejidos, como los músculos. Las grasas entregan energía de reserva y participan en funciones del cuerpo. Las vitaminas y los minerales ayudan a regular funciones. El agua repone lo que se pierde al sudar y permite que el cuerpo funcione.",
        "No existe un alimento milagroso que mejore el rendimiento por sí solo: lo que ayuda es el conjunto de comidas variadas a lo largo del día y una buena hidratación. Los sellos «ALTO EN» de los envases avisan que un alimento tiene mucha cantidad de un nutriente que conviene limitar (como azúcares, sodio o grasas saturadas); por eso es mejor que no sean la base de la alimentación.",
        "Las cantidades y los ajustes dependen de la edad, la actividad y la salud de cada persona, y los define un profesional de la salud, como una nutricionista. Este cuaderno no entrega dietas ni cantidades ni juzga cuerpos. Si alguien se saltea comidas por preocupación por su cuerpo, o siente malestar, conviene hablar con una persona adulta de confianza o con un profesional.",
    ],
    vocab=[("alimentación variada", "incluye alimentos de distintos grupos a lo largo del día"), ("carbohidratos", "nutrientes que entregan energía principal"), ("proteínas", "nutrientes que construyen y reparan tejidos"), ("hidratación", "reponer los líquidos que se pierden, sobre todo con agua"), ("sello «ALTO EN»", "aviso en el envase de mucha cantidad de un nutriente a limitar")],
    worked=[
        ("Relacionar alimento y función", "En una comida de ejemplo hay arroz, pollo y ensalada. ¿Qué aporta sobre todo cada uno?", ["El arroz aporta sobre todo carbohidratos, o sea, energía.", "El pollo aporta proteínas, y la ensalada, vitaminas y minerales."], "Arroz: energía; pollo: proteínas; ensalada: vitaminas y minerales"),
        ("Leer una etiqueta", "Un envase de ejemplo trae un sello «ALTO EN sodio». ¿Cómo se interpreta?", ["El sello avisa de mucha cantidad de sodio.", "Conviene que ese alimento no sea la base de la alimentación."], "Tiene mucho sodio y no conviene que sea la base"),
    ],
    mistakes=[("Creer que existe un alimento milagroso para rendir más.", "El rendimiento depende del conjunto de hábitos y comidas.", "Prefiere comidas variadas y pide orientación profesional."),
              ("Saltarse comidas para cambiar el cuerpo antes de una competencia.", "Puede afectar la energía y la salud.", "Habla con una persona adulta de confianza o con un profesional.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿cuál es la función principal de los carbohidratos?', 'Entregar energía para el movimiento y para el cerebro', 'Reparar y construir tejidos como los músculos', 'Reemplazar el agua que se pierde al sudar', 'Los carbohidratos son la fuente principal de energía.'),
        ('abc', 'En Ciencias del ejercicio: ¿qué función principal cumplen las proteínas?', 'Construir y reparar tejidos, como los músculos', 'Ser la única fuente de energía del cuerpo', 'Reemplazar el agua que se pierde al sudar', 'Las proteínas ayudan a construir y reparar tejidos.'),
        ('abc', '{F} ¿Cuál de estos alimentos del menú es fuente de proteínas?', 'El pescado al horno', 'La fruta del desayuno', 'El arroz del almuerzo', 'El pescado aporta proteínas; la fruta y el arroz aportan sobre todo otros nutrientes.'),
        ('abc', '{F} ¿Qué alimento del desayuno aporta sobre todo grasas?', 'La palta', 'La fruta', 'El pan', 'La palta es el alimento del desayuno que aporta sobre todo grasas.'),
        ('abc', '{F} ¿Por qué se puede decir que el menú es variado?', 'Incluye cereales, legumbres, lácteos, pescado, frutas y verduras', 'Tiene solo alimentos de un mismo grupo en todas las comidas', 'Incluye un único alimento muy grande para todo el día', 'Reúne alimentos de varios grupos a lo largo del día.'),
        ('abc', '¿Qué es la hidratación?', 'Reponer los líquidos que el cuerpo pierde, sobre todo con agua', 'Beber solo cuando hay sed extrema, para no tomar de más', 'Tomar cualquier bebida con azúcar durante toda la actividad', 'Hidratarse es reponer líquidos, principalmente con agua.'),
        ('abc', '{F} Si el menú no tuviera ninguna fruta ni verdura, ¿qué se perdería sobre todo?', 'Una fuente importante de vitaminas y minerales', 'La única fuente de agua que tiene el menú durante el día', 'Toda la energía necesaria para la jornada de entrenamiento', 'Las frutas y verduras son fuente importante de vitaminas y minerales.'),
        ('abc', 'Un envase trae el sello «ALTO EN azúcares». ¿Cómo se interpreta?', 'Tiene mucha cantidad de azúcares, por lo que no conviene que sea la base', 'Es un alimento obligatorio para quien entrena todos los días de la semana', 'Tiene proteínas extra para ayudar a los músculos después de entrenar', 'El sello avisa de un nutriente a limitar, no de un beneficio.'),
        ('ab', 'Un estudiante dice: «Para rendir mejor, debo comer solo el alimento milagroso de un deportista famoso». ¿Qué corresponde?', 'Preferir una alimentación variada y consultar a un profesional', 'Seguir al deportista, porque su ejemplo basta para decidir qué comer', 'Un solo alimento no reemplaza una alimentación variada ni la orientación profesional.'),
        ('abc', 'Un estudiante omite el desayuno y la cena para cambiar su cuerpo antes de una competencia. ¿Qué corresponde?', 'Hablar con una persona adulta de confianza o con un profesional de la salud', 'Seguir, porque saltarse comidas siempre mejora el rendimiento en la competencia', 'Pedir a un compañero que haga lo mismo para ir juntos a la competencia', 'Ese comportamiento afecta la energía y la salud, y se conversa con alguien de confianza.'),
        ('abc', 'Dos estudiantes entrenan lo mismo. Uno come variado y toma agua; el otro come solo lo que más le gusta, con sellos «ALTO EN», y casi no toma agua. ¿Cuál tiene mejores condiciones para recuperarse?', 'El primero: la variedad y el agua apoyan la energía y la recuperación', 'El segundo, porque come lo que más le gusta y eso lo motiva', 'Ambos igual, porque lo que se come no influye en la recuperación', 'La variedad y el agua apoyan la recuperación; el gusto por sí solo no la garantiza.'),
        ('abc', '{F} La estudiante quiere recuperarse mejor después de entrenar. ¿Qué decisión es coherente con el menú?', 'Mantener comidas variadas con proteínas y agua, y consultar a una nutricionista', 'Reemplazar todo el menú por un producto en polvo que prometa recuperación', 'Eliminar los carbohidratos del menú, porque no sirven para recuperarse', 'Lo coherente es variedad, agua y orientación profesional; eliminar un grupo es un error.'),
        ('abc', 'Un estudiante pregunta cuántos gramos exactos de cada nutriente debe comer. ¿Qué respuesta es adecuada?', 'Depende de cada persona y lo define un profesional de la salud', 'Siempre 100 gramos de cada nutriente, todos los días del año', 'El mismo número que su amigo, para igualarse en la competencia', 'Las cantidades dependen de cada persona y las define un profesional.'),
    ],
    ctx=('abc', 'Sofía anota su día: en el desayuno toma solo un jugo; almuerza completo, con legumbres y verduras; no toma agua en todo el día; y entrena 40 minutos al final. ¿Qué mejora es coherente?', 'Agregar al desayuno alimentos con energía y proteínas, y tomar agua durante el día', 'Eliminar el almuerzo para entrenar más liviana y sentirse más ágil', 'Tomar solo bebidas con sellos «ALTO EN» para tener más energía rápida', 'Se agrega variedad y agua; eliminar comidas o elegir productos con sellos no ayuda.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué nutriente aporta la energía principal?", "Los carbohidratos", "Entregan la energía principal para el movimiento."),
        ("¿Qué función cumplen las proteínas?", "Construir y reparar tejidos como los músculos", "Ayudan a la recuperación después del esfuerzo."),
        ("¿Quién define cantidades personales de alimentos?", "Un profesional de la salud, como una nutricionista", "Las necesidades varían de persona a persona."),
    ],
    op=("Con este menú de ejemplo de una persona ficticia: desayuno, un pan con queso y un jugo; almuerzo, fideos con carne y una ensalada; once, una galleta con sello «ALTO EN azúcares»; cena, un huevo con arroz. Indica qué grupos de alimentos incluye, cuáles faltan, cómo mejorarías la variedad sin dar cantidades y cuándo consultarías a un profesional.",
        "Incluye cereales, lácteos, carnes, verduras y huevo. Faltan fruta entera y legumbres, y no se menciona agua. Mejoraría agregando fruta en la once y agua durante el día. Si hubiera dudas por entrenamiento o preocupaciones con la comida, consultaría a una nutricionista o a una persona adulta de confianza.",
        ["identifica grupos presentes y ausentes", "propone mejoras de variedad sin cantidades", "menciona consulta a un profesional"],
        ["texto con análisis del menú y mejoras"],
        ["dar cantidades exactas o dietas", "juzgar el cuerpo de la persona", "olvidar el agua"],
        "Pregunta: «¿qué grupo de alimentos falta y qué aportaría?». Si no sabe, pídele que revise el menú."),
    reinforce="Anota en papel lo que comiste en un día y señala qué grupos de alimentos incluyó. No hagas dietas ni compares con otras personas.",
    extend="Explica por qué no existe un alimento milagroso para el rendimiento y qué hábitos sí ayudan.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 17 (lista de ejemplo, inventada, de ayudas que se ofrecen a una estudiante deportista ficticia). "
     "(1) Calzado adecuado a la superficie. (2) Una rutina de respiración lenta y de concentración antes de competir. "
     "(3) Una bebida que dice «mejora tu energía» y promete resultados inmediatos. (4) Un calentamiento bien planificado. "
     "(5) Una sustancia que figura en la lista de prohibidas de un organismo antidopaje.")
build(
    O4, 3, F,
    use="Aprenderé qué son las ayudas ergogénicas, en qué categorías se agrupan, qué es el dopaje y por qué una persona menor de edad no decide por su cuenta usar productos, y a analizarlas con espíritu crítico.",
    prior=["Sé qué incluye una alimentación variada.", "Sé que los hábitos básicos influyen en el rendimiento.", "Sé que ante dudas de salud se consulta."],
    explain=[
        "Una ayuda ergogénica es un recurso, técnica o sustancia que se usa con la idea de mejorar el rendimiento. Se agrupan en categorías: mecánicas (calzado y equipo adecuados), psicológicas (respiración, concentración, visualización), fisiológicas (calentamiento y descanso planificados), nutricionales (alimentos, bebidas y productos) y farmacológicas (medicamentos y otras sustancias). Algunas son comunes y de bajo riesgo; otras no tienen evidencia o pueden dañar la salud.",
        "El dopaje es el uso de sustancias o métodos prohibidos por los organismos antidopaje para mejorar el rendimiento. Es una trampa que rompe el juego limpio y puede dañar la salud. Que algo sea «natural» o venga de una persona conocida no garantiza que sea seguro ni permitido. Una promesa de resultados inmediatos no es evidencia.",
        "Una persona menor de edad no decide por su cuenta usar productos o fármacos: consulta antes a una persona adulta y a un profesional de la salud. Este cuaderno no recomienda productos ni dosis. Si alguien siente presión de otras personas para usar algo, dice no y avisa a una persona adulta de confianza.",
    ],
    vocab=[("ayuda ergogénica", "recurso, técnica o sustancia usado para intentar mejorar el rendimiento"), ("categoría", "grupo al que pertenece una ayuda"), ("dopaje", "uso de sustancias o métodos prohibidos para mejorar el rendimiento"), ("juego limpio", "competir con honestidad y respeto por las reglas"), ("evidencia", "datos confiables que respaldan una afirmación")],
    worked=[
        ("Clasificar una ayuda", "Una rutina de visualización antes de un salto, ¿a qué categoría pertenece?", ["Trabaja la mente y la concentración.", "Es una ayuda psicológica."], "Psicológica"),
        ("Reconocer el dopaje", "Un equipo de ejemplo usa una sustancia prohibida para ganar. ¿Qué es?", ["Usa una sustancia prohibida por organismos antidopaje.", "Rompe el juego limpio y puede dañar la salud: es dopaje."], "Dopaje"),
    ],
    mistakes=[("Pensar que si es «natural» no tiene riesgos.", "Algo natural puede ser riesgoso o estar prohibido.", "Revisa la evidencia y consulta a un profesional."),
              ("Aceptar un producto porque lo ofreció un amigo.", "La confianza personal no reemplaza la evidencia ni la consulta a un profesional.", "Di no y consulta a una persona adulta.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es una ayuda ergogénica?', 'Un recurso, técnica o sustancia usado para intentar rendir más', 'Un alimento obligatorio para quien entrena todos los días', 'Una lesión que ocurre durante la competencia por falta de calentar', 'Una ayuda ergogénica se usa para intentar rendir más.'),
        ('abc', '{F} ¿Cuál de las ayudas de la lista es mecánica?', 'El calzado adecuado a la superficie', 'La rutina de respiración y concentración', 'El calentamiento bien planificado', 'El calzado es un equipo, o sea, una ayuda mecánica.'),
        ('abc', '{F} ¿Cuál de las ayudas es psicológica?', 'La rutina de respiración lenta y de concentración', 'La bebida que promete energía inmediata en la competencia', 'El calzado adecuado a la superficie de la pista', 'La respiración y la concentración trabajan la mente.'),
        ('abc', '{F} La ayuda (5) es una sustancia de la lista de prohibidas. ¿Qué es usarla para competir?', 'Dopaje, una falta ética que puede dañar la salud', 'Una ayuda fisiológica permitida si se usa con calentamiento', 'Una ayuda nutricional común', 'Usar una sustancia prohibida para competir es dopaje.'),
        ('abc', '{F} ¿A qué categoría pertenece el calentamiento bien planificado (4)?', 'Fisiológica', 'Farmacológica', 'Nutricional', 'Prepara el cuerpo; es una ayuda fisiológica.'),
        ('abc', '¿Por qué no basta que un producto prometa «resultados inmediatos»?', 'Porque la promesa no es evidencia de que funcione ni de que sea seguro', 'Porque los productos más caros siempre funcionan mejor que los otros', 'Porque lo importante es que el producto aparezca mucho en televisión', 'Una promesa no reemplaza la evidencia.'),
        ('abc', '{F} ¿A qué categoría pertenece la bebida (3)?', 'Nutricional', 'Mecánica', 'Psicológica', 'Una bebida o alimento es una ayuda nutricional.'),
        ('abc', 'Una estudiante de 16 años quiere probar un producto en polvo que vio en redes. ¿Qué corresponde?', 'Consultar antes a una persona adulta y a un profesional, sin decidir sola', 'Probarlo sin avisar a nadie para ver si funciona antes de contarlo', 'Pedir a una amiga que lo pruebe primero para ver si le hace efecto', 'Una persona menor de edad no decide sola y consulta a un profesional.'),
        ('ab', 'Una estudiante dice: «Si una ayuda es natural, no tiene riesgos». ¿Es correcto?', 'No: algo natural puede tener riesgos o estar prohibido', 'Sí, porque lo natural siempre es seguro y está permitido', 'Natural no significa seguro ni permitido.'),
        ('abc', 'Un equipo propone: «Todos usemos la ayuda prohibida para competir en igualdad». ¿Qué falla?', 'Es dopaje y trampa: daña la salud aunque todos lo hagan', 'Nada, porque si todos la usan, la competencia es justa para todos', 'Que no se pueden usar dos ayudas a la vez en una misma competencia', 'Que todos lo hagan no cambia que sea una trampa y un riesgo.'),
        ('abc', 'Antes de culpar la falta de una ayuda por un mal resultado, ¿qué conviene revisar primero?', 'Si hubo sueño, alimentación variada, hidratación y entrenamiento adecuados', 'Si el rival usa un producto más caro o más conocido que el propio', 'Si el equipo de otro colegio tenía una ropa deportiva mejor que la nuestra', 'Los hábitos básicos explican muchas diferencias y se revisan primero.'),
        ('abc', '{F} Alguien pregunta qué ayudas de la lista son de bajo riesgo y se pueden aprender en la escuela. ¿Cuál respuesta es más adecuada?', 'Calzado adecuado, respiración y concentración, y calentamiento planificado', 'La bebida que promete energía inmediata y también la sustancia prohibida', 'Solo la sustancia prohibida, porque es la más potente de la lista', 'Calzado, respiración y calentamiento son de bajo riesgo; las otras requieren cuidado o están prohibidas.'),
        ('abc', 'Un producto dice: «Probado: 9 de cada 10 deportistas rindieron más». No dice cuántas personas fueron ni si hubo grupo de comparación. ¿Qué conviene?', 'Desconfiar hasta conocer la muestra y si hubo grupo de comparación', 'Creerlo, porque 9 de 10 es un número alto y suena convincente', 'Comprarlo para comprobarlo en uno mismo antes de que se agote', 'Sin esos datos la afirmación no tiene respaldo suficiente.'),
    ],
    ctx=('abc', 'Un club escolar de ejemplo ofrece a sus deportistas calzado adecuado, una rutina de respiración y concentración, y un polvo que promete músculos en una semana. ¿Qué decisión es coherente?', 'Adoptar el calzado y la rutina, y no usar el polvo sin consultar', 'Usar el polvo, porque promete justamente lo que más interesa lograr', 'Rechazar todo, incluso el calzado y la rutina, por precaución', 'Se adoptan las ayudas de bajo riesgo y se consulta antes de usar cualquier producto.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué es el dopaje?", "Usar sustancias o métodos prohibidos para mejorar el rendimiento", "Rompe el juego limpio y puede dañar la salud."),
        ("¿Qué se hace antes de usar un producto para rendir más?", "Consultar a una persona adulta y a un profesional de la salud", "Una persona menor de edad no decide sola."),
        ("¿Qué categorías de ayudas ergogénicas hay?", "Mecánicas, psicológicas, fisiológicas, nutricionales y farmacológicas", "Cada una actúa de manera distinta."),
    ],
    op=("Con esta lista de ejemplo: una raqueta del tamaño adecuado, una rutina de concentración antes de competir, un jugo con promesa de «energía sin límites» y una pastilla prohibida por un organismo antidopaje, clasifica cada ayuda por categoría, señala cuáles son de bajo riesgo y cuál es dopaje, y escribe qué harías si alguien te ofrece un producto en una competencia.",
        "Raqueta: mecánica. Rutina de concentración: psicológica. Jugo: nutricional, con promesa sin evidencia. Pastilla prohibida: farmacológica y dopaje. De bajo riesgo: raqueta y rutina de concentración. Si me ofrecen un producto: digo no y aviso a una persona adulta de confianza.",
        ["clasifica las cuatro ayudas", "identifica el dopaje y las de bajo riesgo", "dice no y avisa a una persona adulta"],
        ["clasificación y plan ante la presión"],
        ["creer una promesa sin evidencia", "decidir sola sobre un producto", "confundir natural con seguro"],
        "Pregunta: «¿qué haces si alguien te ofrece un producto?». Si dice «lo pruebo», pídele recordar a quién consultaría."),
    reinforce="Escribe una lista de cinco ayudas de ejemplo y clasifícalas por categoría. No pruebes productos ni sustancias.",
    extend="Explica por qué el dopaje afecta tanto la salud como el juego limpio.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 18 (afirmaciones de ejemplo, inventadas). Afirmación A: «Con el producto Z, 8 de 10 deportistas rindieron más». El estudio lo hizo la empresa que vende Z, con 10 personas y sin grupo de comparación. "
     "Afirmación B: «Tomar agua durante una actividad larga ayuda a mantener el rendimiento». Respaldo de ejemplo: varios estudios independientes con grupo de comparación, citados por una guía de salud. "
     "Afirmación C: «El producto Y elimina el cansancio para siempre». No presenta ningún estudio.")
build(
    O4, 4, F,
    use="Aprenderé a analizar con espíritu crítico las afirmaciones sobre actividad física, alimentación y ayudas ergogénicas, mirando quién las dice, cuántas personas se estudiaron, si hubo comparación y qué riesgos existen.",
    prior=["Sé qué es una ayuda ergogénica.", "Sé qué es un grupo de comparación.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Para analizar una afirmación se hacen preguntas. ¿Quién la dice y quién ganó dinero con ella? Si quien informa vende el producto, hay un conflicto de interés. ¿A cuántas personas se estudió? Con muy pocas, no se puede generalizar. ¿Hubo grupo de comparación? Sin él no se sabe si habrían mejorado igual. ¿Otros estudios independientes encontraron lo mismo? Una sola fuente es débil. ¿Es creíble? Las promesas absolutas, como «para siempre», son señales de alerta.",
        "Un porcentaje alto no basta: 8 de 10 es 80 %, pero con 10 personas, sin comparación y con interés comercial, la afirmación es débil. En cambio, varios estudios independientes con comparación y resultados parecidos dan un respaldo más fuerte, aunque rara vez certeza absoluta. También se revisan los riesgos para la salud y si el producto está permitido en el deporte.",
        "Un caso personal («yo lo uso y rindo más») o la publicidad no son evidencia. Una persona menor de edad no decide por su cuenta usar productos: consulta a una persona adulta y a un profesional de la salud. Todas las cifras de este cuaderno son de ejemplo.",
    ],
    vocab=[("conflicto de interés", "cuando quien informa puede ganar algo si se le cree"), ("muestra", "personas estudiadas en una investigación"), ("estudio independiente", "estudio hecho por quienes no ganan con el resultado"), ("respaldo", "evidencia que apoya una afirmación"), ("señal de alerta", "rasgo que invita a desconfiar")],
    worked=[
        ("Calcular un porcentaje", "En un estudio de ejemplo, 6 de 12 personas mejoraron. ¿Qué porcentaje es?", ["Divide 6 entre 12: 0,5.", "Multiplica por 100: 50 %."], "50 %"),
        ("Detectar una señal de alerta", "Un aviso de ejemplo dice: «cura todo en un día». ¿Qué señal tiene?", ["Promete un resultado absoluto.", "No presenta estudios: es una señal de alerta."], "Promesa absoluta sin respaldo"),
    ],
    mistakes=[("Creer una afirmación porque el porcentaje suena alto.", "Con pocas personas, sin comparación o con interés comercial, el porcentaje no es confiable.", "Revisa muestra, comparación e independencia."),
              ("Tomar la experiencia personal de una persona famosa como evidencia.", "Puede haber otros factores y además interés comercial.", "Busca estudios independientes y consulta a un profesional.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué es un conflicto de interés?', 'Cuando quien informa puede ganar algo si se le cree', 'Cuando dos personas piensan distinto sobre un resultado', 'Cuando un estudio es muy largo y tiene muchas páginas', 'Hay conflicto de interés si quien informa gana con que se le crea.'),
        ('abc', '{F} ¿Qué afirmación no presenta ningún estudio?', 'La C', 'La A', 'La B', 'La C no tiene respaldo alguno.'),
        ('=', '{F} ¿Qué porcentaje de las 10 personas de la afirmación A rindió más?', '8*100/10', 'Se divide el número de personas que rindieron más entre el total y se pasa a porcentaje.', ' %'),
        ('abc', '{F} ¿Por qué la afirmación A es débil aunque el 80 % suena alto?', 'La hizo la empresa vendedora, con solo 10 personas y sin grupo de comparación', 'Porque 80 % es un porcentaje bajo', 'Porque los estudios hechos por empresas siempre dicen la verdad', 'Interés comercial, pocas personas y falta de comparación debilitan la afirmación.'),
        ('abc', '{F} ¿Qué falta en A para saber si el producto Z funcionó?', 'Un grupo que no use el producto, para ver si mejoraba igual', 'Más publicidad en redes para que más personas conozcan el producto', 'Otro nombre para el producto, que suene más serio y científico', 'Sin grupo de comparación no se sabe si habrían mejorado igual.'),
        ('abc', '{F} ¿Qué señal de alerta tiene la afirmación C?', 'Promete un resultado absoluto, «para siempre», sin respaldo', 'Habla de cansancio, un tema que no puede evaluarse con estudios', 'No menciona el precio del producto Y ni dónde se vende', 'Una promesa absoluta sin estudios es una señal de alerta.'),
        ('abc', '{F} ¿Qué afirmación está mejor respaldada?', 'La B, por varios estudios independientes con grupo de comparación', 'La A, porque tiene un porcentaje alto y lo hizo la empresa vendedora', 'La C, porque es la más segura y promete resultados para siempre', 'La B tiene varias fuentes independientes con comparación.'),
        ('=', '{F} En B, supón que 3 de 5 estudios independientes de ejemplo apoyan la afirmación y 2 no encuentran diferencias. ¿Qué porcentaje de los estudios la apoya?', '3*100/5', 'Se divide el número de estudios que apoyan entre el total y se pasa a porcentaje.', ' %'),
        ('ab', '{F} Si 3 de 5 estudios apoyan B, ¿qué se concluye con cuidado?', 'Hay respaldo parcial, pero no unánime; conviene seguir leyendo evidencia', 'Está probado para siempre y es válido para todas las personas sin excepción', 'Con 3 de 5 estudios hay apoyo parcial, no certeza.'),
        ('abc', 'Un influencer dice: «Yo lo uso y rindo más; es prueba suficiente». ¿Qué falla?', 'Un caso personal no es evidencia: hay otros factores y puede haber interés', 'Nada, porque la experiencia personal de un famoso es la mejor evidencia', 'Que los influencers no pueden usar ningún producto ni recomendarlo', 'Un caso aislado no permite concluir un efecto.'),
        ('abc', 'Una persona de 16 años lee la afirmación A y quiere comprar el producto Z. ¿Qué paso corresponde?', 'Preguntar a una persona adulta y a un profesional antes de decidir', 'Comprarlo, porque 8 de 10 es un porcentaje alto y convincente', 'Pedir a una amiga que lo compre para no tener que decidir sola', 'La decisión se consulta con una persona adulta y un profesional de la salud.'),
        ('=', '{F} En una versión nueva de A, con 50 personas, 40 rindieron más. ¿Qué porcentaje es?', '40*100/50', 'Se divide 40 entre 50 y se pasa a porcentaje.', ' %'),
        ('abc', '{F} Con 50 personas, grupo de comparación, estudio independiente y el resultado repetido en otro lugar, ¿cómo cambia la confianza en la afirmación?', 'Aumenta, aunque no llega a ser certeza absoluta para todas las personas', 'Pasa a ser una prueba absoluta para todas las personas', 'No cambia, porque el porcentaje sigue siendo 80 % igual que antes', 'Más muestra, comparación e independencia aumentan la confianza, sin certeza absoluta.'),
    ],
    ctx=('abc', 'Un aviso de ejemplo dice: «El 90 % de quienes lo usan rinde más». Solo informa el aviso de la empresa; no indica cuántas personas fueron ni si hubo comparación. ¿Qué conviene hacer?', 'Pedir datos de muestra, comparación e independencia y consultar a un profesional', 'Creerlo, porque 90 % es un número muy alto y viene de la empresa', 'Comprarlo y compartirlo con el equipo para que todos lo prueben', 'Sin esos datos no se puede evaluar la afirmación.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué tres preguntas ayudan a analizar una afirmación?", "Quién la dice, a cuántas personas se estudió y si hubo comparación", "Con ellas se evalúa el respaldo."),
        ("¿Qué es una señal de alerta?", "Un rasgo que invita a desconfiar, como una promesa absoluta", "Puede indicar publicidad que no tiene evidencia."),
        ("¿Quién decide si una persona menor de edad usa un producto?", "No decide sola: consulta a una persona adulta y a un profesional", "Es una decisión de salud que requiere consulta."),
    ],
    op=("Analiza esta afirmación de ejemplo: «Con la barra Q, 9 de 10 corredores bajaron su tiempo. Estudio realizado por la empresa que la vende, con 10 personas, sin grupo de comparación». Responde: porcentaje, quién informa, cuántas personas, si hubo comparación, qué señal de alerta ves y qué harías antes de decidir.",
        "Porcentaje: 90 %. Informa la empresa vendedora, hay conflicto de interés. Fueron 10 personas y no hubo grupo de comparación. Es una afirmación débil. Antes de decidir, buscaría estudios independientes y consultaría a una persona adulta y a un profesional de la salud.",
        ["calcula el porcentaje", "analiza fuente, muestra y comparación", "dice qué haría antes de decidir"],
        ["análisis escrito de la afirmación"],
        ["creer por el porcentaje alto", "decidir sin consultar", "no mencionar el conflicto de interés"],
        "Pregunta: «¿quién gana si creemos esta afirmación?». Si no encuentra a nadie, pídele que revise quién hizo el estudio."),
    reinforce="Busca en tu casa un aviso o envase con una promesa de rendimiento y analízalo con las preguntas de la clase, sin comprar ni probar nada.",
    extend="Explica por qué una promesa absoluta y un estudio de la empresa vendedora no bastan para confiar en una afirmación.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 19 (caso de ejemplo, inventado). Sebastián, estudiante ficticio de 17 años, quiere «rendir más» en el atletismo escolar. "
     "Su registro de la semana: durmió poco tres noches; se saltó el desayuno cuatro días; tomó poca agua durante los entrenamientos; hizo 4 sesiones y una fue con dolor en el tobillo que no avisó. "
     "Un amigo le ofrece un polvo que promete más rendimiento.")
build(
    O4, 5, F,
    use="Aprenderé a evaluar y ajustar decisiones sobre actividad física, alimentación y ayudas ergogénicas, partiendo de la seguridad y los hábitos básicos, y a actuar con juego limpio y consulta profesional.",
    prior=["Sé qué es una ayuda ergogénica y el dopaje.", "Sé analizar afirmaciones con evidencia.", "Sé que ante dolor se detiene la práctica."],
    explain=[
        "Al evaluar una decisión se ordenan las prioridades. Primero, la seguridad y la salud: ante dolor o malestar se detiene la práctica y se avisa a una persona adulta o a un profesional. Segundo, los hábitos básicos: dormir lo suficiente, comer de forma variada, hidratarse, calentar y descansar. Tercero, un entrenamiento bien planificado. Solo después, y con una persona adulta y un profesional, se podría conversar sobre cualquier otra ayuda, nunca una prohibida.",
        "Para ajustar, se cambia una sola condición a la vez y se registra, por ejemplo agregar un desayuno variado una semana, y luego se evalúa con datos. Atribuir una mejora a un producto sin revisar los hábitos puede ser un error: los hábitos pueden explicar el cambio. La mejora, si existe, se interpreta con cuidado, porque otros factores también influyen.",
        "El juego limpio es competir con honestidad y respeto por las reglas: usar una sustancia prohibida es dopaje y es trampa. Ante presión de otras personas («todos lo usan»), se puede decir no con firmeza y avisar a una persona adulta de confianza. Todos los datos de este cuaderno son ficticios y no entregan dietas, dosis ni indicaciones personales.",
    ],
    vocab=[("prioridad", "lo que se atiende primero al decidir"), ("hábitos básicos", "sueño, alimentación variada, hidratación, calentamiento y descanso"), ("juego limpio", "competir con honestidad y respeto por las reglas"), ("presión de pares", "insistencia de otras personas para que uno haga algo"), ("ajuste", "cambio de una condición según los datos")],
    worked=[
        ("Ordenar prioridades", "Una persona de ejemplo duerme poco, entrena con dolor y quiere un producto. ¿Qué atiende primero?", ["Primero la seguridad: el dolor se informa y se detiene la práctica.", "Luego los hábitos básicos, como el sueño; el producto queda al final y con consulta."], "El dolor, luego los hábitos, y el producto al final"),
        ("Decir no ante la presión", "Alguien dice: «todos usan este polvo». ¿Qué respuesta es adecuada?", ["Decir no con claridad y mantener la decisión.", "Avisar a una persona adulta de confianza si la presión sigue."], "Decir no y avisar a una persona adulta"),
    ],
    mistakes=[("Atribuir una mejora a un producto sin mirar los hábitos.", "El sueño, la comida o el descanso pudieron explicar el cambio.", "Revisa y ajusta hábitos antes de pensar en cualquier otra ayuda."),
              ("Ocultar un dolor para no perder entrenamientos.", "Puede empeorar y llevar a una lesión.", "Detén la práctica y avisa a una persona adulta o a un profesional.")],
    T=[
        ('abc', 'En Ciencias del ejercicio: ¿qué se revisa primero antes de pensar en una ayuda ergogénica?', 'Los hábitos básicos, como sueño, alimentación e hidratación', 'El producto más caro del mercado, que promete más resultados', 'Lo que usa otro deportista famoso para rendir en la competencia', 'Los hábitos básicos explican gran parte del rendimiento y van primero.'),
        ('=', '{F} ¿Qué porcentaje de sus sesiones de la semana fue con dolor en el tobillo?', '1*100/4', 'Se divide la sesión con dolor entre las 4 sesiones y se pasa a porcentaje.', ' %'),
        ('abc', '{F} ¿Qué dato del registro exige actuar primero por seguridad?', 'El dolor en el tobillo que no avisó', 'El desayuno omitido durante cuatro días', 'El poco sueño de tres noches de la semana', 'El dolor es una señal de detención y tiene prioridad.'),
        ('abc', '{F} ¿Qué debería hacer Sebastián con el dolor de tobillo?', 'Dejar de entrenar con dolor y avisar a una persona adulta o profesional', 'Entrenar con una venda para sostener el tobillo y seguir con las sesiones', 'Esperar a que el dolor pase solo y no contárselo a nadie por ahora', 'El dolor se informa y no se entrena con él.'),
        ('abc', '{F} ¿Qué respuesta es adecuada al amigo que ofrece el polvo?', 'Decir no y consultar a una persona adulta y a un profesional', 'Aceptarlo, porque viene de un amigo y los amigos no hacen daño', 'Probarlo a escondidas para no preocupar a nadie con una decisión', 'Una persona menor de edad no decide sola sobre un producto.'),
        ('abc', '¿Qué es el dopaje?', 'Usar sustancias o métodos prohibidos para rendir más en el deporte', 'Cualquier alimento que da energía antes o durante una competencia', 'Un calentamiento muy largo antes de empezar la competencia', 'El dopaje es usar sustancias o métodos prohibidos para rendir más.'),
        ('abc', '{F} Una vez resuelto el dolor con ayuda, ¿qué ajuste de una sola condición es más adecuado para empezar?', 'Agregar un desayuno variado y mantener lo demás, registrando la semana', 'Cambiar el sueño, la comida, el entrenamiento y el calzado a la vez', 'Duplicar las sesiones de entrenamiento', 'Una sola condición cambiada y registrada permite evaluar con datos.'),
        ('abc', '{F} Sebastián mejora su sueño y su desayuno y vuelve a registrar. ¿Qué conviene en la semana siguiente?', 'Mantener los cambios, registrar de nuevo y evaluar con datos', 'Cambiar todo otra vez para ver si aparece una mejora mayor', 'Dejar de registrar porque ya mejoró y no hace falta seguir', 'Seguir registrando permite saber si el cambio se mantiene.'),
        ('ab', '{F} ¿Qué principio se vulnera si usara una sustancia prohibida para competir?', 'El juego limpio, porque obtendría ventaja con trampa', 'Ninguno, porque lo que haga con su cuerpo es solo asunto suyo', 'El juego limpio es competir con honestidad y respeto por las reglas.'),
        ('abc', 'Su amigo insiste: «Todos en el club lo usan». ¿Qué corresponde?', 'Mantener la decisión de no usarlo y avisar a una persona adulta si hay presión', 'Ceder, porque es mejor encajar con el grupo y no quedar excluido', 'Aceptar el polvo y no usarlo, solo para evitar la discusión con él', 'Se mantiene la decisión y se avisa; ceder expone a riesgos.'),
        ('abc', 'Un informe dice: «Con el polvo, el rendimiento subirá», pero no habla del sueño ni de la alimentación. ¿Qué falla en el análisis?', 'Atribuye el efecto a una ayuda sin revisar hábitos que podrían explicarlo', 'Nada: solo importa el polvo, porque los demás hábitos no cambian nada', 'Que los hábitos no influyen en el rendimiento de ninguna persona', 'Si no se revisan los hábitos, no se sabe qué produjo el cambio.'),
        ('=', 'Un seguimiento dura 4 semanas, con 4 sesiones por semana y 2 datos anotados por sesión, esfuerzo y sueño. ¿Cuántos datos acumula?', '4*4*2', 'Se multiplican las semanas, las sesiones por semana y los datos por sesión.', ' datos'),
        ('abc', '{F} Tras 4 semanas con mejores hábitos y sin dolor, Sebastián mejora un poco su tiempo. ¿Qué se concluye con cuidado?', 'Los hábitos pudieron contribuir, aunque otros factores también influyen', 'Que el polvo era necesario para lograr esa mejora en el tiempo', 'Que los hábitos no sirven, porque la mejora fue muy pequeña', 'Se interpreta la mejora con cuidado, sin atribuirla a un solo factor.'),
    ],
    ctx=('abc', 'Antonia, persona ficticia, tiene una semana de pruebas, duerme poco y piensa tomar un producto que ve en redes para tener más energía en el entrenamiento. ¿Qué decisión es más razonable?', 'Priorizar el sueño y las comidas variadas, y consultar antes del producto', 'Tomar el producto, porque la semana de pruebas es muy difícil y exigente', 'Entrenar más fuerte para compensar el poco sueño de toda la semana', 'Se atienden primero los hábitos y se consulta antes de cualquier producto.'),
    sc=[
        ("En Ciencias del ejercicio: ¿qué se atiende primero al decidir?", "La seguridad y los hábitos básicos", "Son la base del rendimiento y la salud."),
        ("¿Qué haces ante la presión de usar un producto?", "Dices no y avisas a una persona adulta de confianza", "Nadie debe presionar a otra persona."),
        ("¿Se puede atribuir una mejora a un producto sin revisar hábitos?", "No: otros factores pueden explicarla", "Hay que interpretar el resultado con cuidado."),
    ],
    op=("Con este caso de ejemplo: una persona ficticia de 16 años duerme poco, se saltea el almuerzo y toma poca agua; un compañero le ofrece un producto que promete rendimiento. Ordena por prioridad qué atendería, propone un ajuste de una sola condición, escribe cómo respondería al compañero y señala cuándo consultaría a un profesional.",
        "Prioridades: seguridad (si hay dolor), luego sueño, comida variada y agua; el producto, al final y con consulta. Ajuste: agregar el almuerzo y registrar la semana. Respuesta: «no, gracias, lo hablaré con una persona adulta». Consultaría a un profesional ante dudas de salud o de alimentación.",
        ["prioridades en orden", "ajuste de una condición y registro", "respuesta firme y consulta profesional"],
        ["texto con prioridades, ajuste y respuesta"],
        ["recomendar el producto", "cambiar muchas condiciones a la vez", "no avisar a una persona adulta"],
        "Pregunta: «¿qué atiendes primero y por qué?». Si dice «el producto», pídele volver a los hábitos básicos."),
    reinforce="Escribe tres frases para decir no a la presión de usar un producto y a quién avisarías. Hazlo en papel.",
    extend="Explica por qué los hábitos básicos y el juego limpio importan más que cualquier ayuda ofrecida.",
)
