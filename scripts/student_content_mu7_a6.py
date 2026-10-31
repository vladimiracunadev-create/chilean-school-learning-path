"""Student material for 7.º básico Música, OA 06 (reconocer fortalezas y áreas de crecimiento personal en la audición, interpretación, creación y reflexión).

Todos los puntajes, registros y casos de los ejercicios son inventados para esta clase. La autoevaluación es privada: cada persona decide qué comparte, y los resultados describen lo que se hizo en un momento, no lo que una persona «es».
"""
from __future__ import annotations

from student_content_mu7_a import L
from student_lessons import arith, ex

OA6 = "MU07 OA 06"
AREAS = "audición (escuchar y reconocer), interpretación (cantar y tocar), creación (improvisar y componer) y reflexión (explicar y valorar lo que hago)"

# ---------------------------------------------------------------- OA 06 · clase 1 (autoevaluar con evidencia)
L(
    OA6, 1,
    "Lápiz y papel. Los puntajes y casos están escritos en los ejercicios. Tu autoevaluación es privada: tú decides si la compartes y con quién.",
    f"Aprenderé a mirar mi trabajo musical en cuatro áreas ({AREAS}) y a describirlo con evidencia concreta. Sirve para reconocer en qué me va bien y qué quiero mejorar, sin etiquetas.",
    ["Sé que escuchar, interpretar y crear son cosas distintas.", "Sé comparar números de una tabla.", "Sé que una opinión no es lo mismo que un dato."],
    [
        f"En música podemos mirar nuestro trabajo en cuatro áreas: {AREAS}. Una autoevaluación es mirar lo que hice y describirlo con evidencia. La evidencia es un dato concreto que otra persona podría comprobar, como «acerté 6 de 8 notas» o «mantuve el pulso 4 de 5 veces». Una frase como «soy malo para la música» no es evidencia, es un juicio general que no dice nada comprobable.",
        "Los resultados describen lo que ocurrió en un momento y con una tarea, no lo que una persona es. Una persona puede ir muy bien en interpretación y estar aprendiendo en creación, y eso cambia con la práctica. Por eso se anotan datos de cada área por separado, por ejemplo con puntajes de 0 a 8. Una tabla simple permite ver en qué área el puntaje es más alto y en cuál es más bajo.",
        "La autoevaluación es privada. Cada persona decide si comparte sus resultados y a quién. Lo que se busca no es compararse con otras personas, sino con uno mismo a lo largo del tiempo. Una buena autoevaluación nombra el área, entrega una evidencia concreta y dice qué se podría hacer para seguir avanzando. Así los resultados sirven para decidir qué practicar, sin sentir vergüenza ni presión.",
    ],
    [("autoevaluación", "mirar mi propio trabajo y describirlo con evidencia"), ("evidencia", "dato concreto que se puede comprobar"), ("área", "parte del trabajo musical: audición, interpretación, creación o reflexión"), ("juicio general", "frase como «soy malo» que no dice nada comprobable"), ("fortaleza", "área o habilidad en que me va bien con evidencia")],
    [
        ("Clasificar una frase", "«Reconozco el timbre de 4 de 5 instrumentos al escuchar.» ¿A qué área pertenece?", ["Habla de reconocer sonidos al escuchar.", "Eso es la audición."], "Audición"),
        ("Distinguir evidencia", "¿Cuál es una evidencia: «Acerté 6 de 8 notas» o «Soy malo para la música»?", ["La primera se puede comprobar contando.", "La segunda es un juicio general."], "«Acerté 6 de 8 notas»"),
    ],
    [
        ("Describir mi trabajo con «soy bueno» o «soy malo».", "Son juicios generales y no dicen qué hice ni cómo mejorar.", "Cambia el juicio por un dato: «acerté 6 de 8»."),
        ("Compararme solo con otras personas.", "Cada persona parte de un lugar distinto y avanza a su ritmo.", "Compárate con tus propios resultados anteriores."),
    ],
    [
        ex("¿Cuáles son las cuatro áreas de la clase?", "Audición, interpretación, creación y reflexión", "Así se organiza el trabajo musical en esta unidad."),
        ex("¿Cuál es una evidencia: «Mantuve el pulso 4 de 5 veces» o «Soy malo para la música»?", "«Mantuve el pulso 4 de 5 veces»", "Es un dato concreto que se puede comprobar."),
        ex("La autoevaluación, ¿es privada o pública?", "Privada", "Cada persona decide si la comparte."),
    ],
    [
        ex("«Toqué el compás sin errores 3 veces seguidas.» ¿A qué área pertenece?", "Interpretación", "Se trata de tocar una pieza."),
        ex("«Inventé una melodía de 8 notas que termina en 1.» ¿A qué área pertenece?", "Creación", "Se trata de crear una melodía propia."),
        ex("«Expliqué con un ejemplo por qué cambié el volumen de mi canción.» ¿A qué área pertenece?", "Reflexión", "Se trata de explicar y valorar el propio trabajo."),
    ],
    [
        ex("Los puntajes de una estudiante son audición 5 de 8, interpretación 7 de 8, creación 4 de 8 y reflexión 6 de 8. ¿En qué área tiene el puntaje más alto?", "Interpretación", "7 es el número mayor de los cuatro."),
        arith("Los puntajes de una estudiante son 5, 7, 4 y 6 en las cuatro áreas. ¿Cuántos puntos suma en total?", "5+7+4+6", "Se suman los cuatro puntajes.", " puntos"),
        ex("Puntajes de 8: audición 5, interpretación 7, creación 4, reflexión 6. ¿Cuántas áreas tienen un puntaje mayor que 5?", "2", "Son interpretación (7) y reflexión (6)."),
    ],
    [
        ex("Luis tiene 7 de 8 en interpretación. Dice que no le va bien en nada. ¿Hay evidencia de un buen resultado en esa área? Responde sí o no.", "Sí", "7 de 8 es un resultado alto y comprobable; para hablar de una fortaleza sostenida, se miran varias ocasiones."),
        ex("Una estudiante tiene 4 de 8 en las cuatro áreas. ¿Tiene una fortaleza clara sobre las otras? Responde sí o no.", "No", "Todas las áreas están igual."),
    ],
    [
        ex("Estudiante A: audición 6 de 8 y creación 3 de 8. Estudiante B: audición 4 de 8 y creación 8 de 8. ¿Quién tiene mayor diferencia entre sus dos áreas?", "El estudiante B", "B tiene una diferencia de 4 y A de 3."),
        ex("Una estudiante dice «soy malo en música» después de equivocarse en una pieza. ¿Cuál frase sería más precisa: «me equivoqué en 2 de 8 notas» o «no sirvo para esto»?", "«Me equivoqué en 2 de 8 notas»", "Describe un hecho que se puede mejorar."),
    ],
    [ex("Ana anotó su semana: en 5 días de práctica de 10 minutos, tocó la pieza sin errores en 3 de los días. ¿Cuántos minutos practicó en total?", "50 minutos", "5 días × 10 minutos = 50 minutos.", "5*10")],
    [ex("En una autoevaluación musical, ¿qué es la evidencia?", "Un dato concreto que se puede comprobar", "Por eso sirve para evaluar."), ex("¿Qué área trata de improvisar o componer?", "La creación", "Es el área de crear música."), ex("¿Con quién conviene compararse?", "Con mis resultados anteriores", "Cada persona avanza a su ritmo.")],
    (
        "Completa una autoevaluación de ejemplo para Ana con estos datos inventados: audición, reconoció 5 de 8 timbres; interpretación, tocó sin errores 3 de 5 intentos; creación, su improvisación de 8 notas cumplió 2 de las 3 reglas; reflexión, explicó con evidencia 2 de 4 decisiones. Para cada área escribe el dato, el nivel y una frase de evidencia. Niveles: 1 si logró menos de la mitad; 2 si logró la mitad; 3 si logró más de la mitad y hasta tres cuartos; 4 si logró más de tres cuartos. Si ya hiciste actividades de esta unidad, haz lo mismo con tus propios datos, solo para ti.",
        "Audición: 5 de 8, nivel 3, «reconoció 5 de 8 timbres». Interpretación: 3 de 5, nivel 3, «tocó sin errores 3 de 5 intentos». Creación: 2 de 3 reglas, nivel 3. Reflexión: 2 de 4, nivel 2. Es el área donde más puede crecer: reflexión. Con una sola medición aún no se habla de fortaleza sostenida.",
        ["escribe un dato por área", "asigna un nivel con razón", "usa evidencia y no juicios generales"],
        ["tabla de cuatro áreas", "frases de evidencia"],
        ["usar «soy bueno» o «soy malo»", "inventar datos sin evidencia"],
        "Reconoce la tabla y pide reemplazar cada juicio general por un dato comprobable.",
    ),
    "Escribe una evidencia de tu audición, otra de tu interpretación y otra de tu creación.",
    "Haz una tabla de las cuatro áreas con un dato propio y compárala con la de hace dos semanas.",
)

# ---------------------------------------------------------------- OA 06 · clase 2 (reconocer fortalezas)
L(
    OA6, 2,
    "Lápiz y papel. Los puntajes de las tres ocasiones están escritos en los ejercicios; cada puntaje es de 0 a 8. Regla de la clase: una fortaleza es un puntaje de 6 o más en al menos 2 de 3 ocasiones.",
    "Aprenderé a reconocer fortalezas con una regla clara, usando varias ocasiones en vez de una sola. Sirve para saber en qué me va bien de manera sostenida y apoyarme en eso para seguir creciendo.",
    ["Sé que hay cuatro áreas: audición, interpretación, creación y reflexión.", "Sé que la evidencia es un dato concreto.", "Sé sumar y restar números pequeños."],
    [
        "Una fortaleza no es un resultado aislado. Una persona puede tener un día muy bueno por casualidad. Para reconocer una fortaleza con más seguridad miramos varias ocasiones. En esta clase usamos esta regla: hay una fortaleza cuando el puntaje es de 6 o más sobre 8 en al menos 2 de 3 ocasiones. Así se distingue entre una habilidad que se mantiene y un buen resultado que ocurrió una vez.",
        "También conviene mirar la mejora, es decir, cuánto cambió el puntaje entre la primera y la última ocasión. Un área que todavía no es fortaleza puede estar mejorando mucho. Si pasó de 4 a 6, mejoró 2 puntos, y eso es un logro aunque la regla de fortaleza aún no se cumpla. Ver la mejora nos recuerda que las habilidades se aprenden y que la práctica funciona.",
        "Una fortaleza sirve para apoyar el resto del trabajo. Quien tiene buena audición puede ayudar a su grupo a escuchar si afinan; quien tiene buena interpretación puede dar seguridad al ensayo. Reconocer una fortaleza no es presumir, es saber con qué recursos cuento. Se anotan la evidencia, las ocasiones y una forma de aprovecharla, por ejemplo ayudando a un compañero con una tarea en la que yo ya me siento seguro.",
    ],
    [("fortaleza", "habilidad en la que me va bien de manera sostenida"), ("ocasión", "cada vez que se mide o se observa un trabajo"), ("mejora", "cuántos puntos subió el resultado entre la primera y la última ocasión"), ("regla de fortaleza", "6 o más de 8 en al menos 2 de 3 ocasiones"), ("sostenida", "que se mantiene en varias ocasiones")],
    [
        ("Aplicar la regla", "Reflexión: 8, 4 y 6 puntos en tres ocasiones. ¿Es una fortaleza?", ["Cuento las ocasiones con 6 o más: 8 y 6.", "Son 2 de 3, y la regla pide al menos 2."], "Sí, es una fortaleza"),
        ("Medir la mejora", "Audición: 2, 4 y 5 puntos en tres ocasiones. ¿Cuántos puntos mejoró y es fortaleza?", ["Mejora: 5 − 2 = 3.", "Ninguna ocasión tiene 6 o más, y la regla pide 2."], "Mejoró 3 puntos, aún no es fortaleza"),
    ],
    [
        ("Decir que una fortaleza es un solo buen resultado.", "Una vez puede ser casualidad; la fortaleza se sostiene.", "Mira al menos tres ocasiones."),
        ("Ignorar las áreas que todavía no son fortaleza.", "Pueden estar mejorando mucho y eso también es un logro.", "Calcula la mejora además de la regla."),
    ],
    [
        ex("Interpretación: 7, 7 y 8 puntos. ¿En cuántas ocasiones obtuvo 6 o más?", "3", "Las tres ocasiones son 6 o más."),
        ex("Audición: 6, 5 y 7 puntos. ¿Cuántas ocasiones tienen 6 o más?", "2", "Son la primera y la tercera."),
        ex("Reflexión: 5, 5 y 6 puntos. ¿Cumple la regla de fortaleza? Responde sí o no.", "No", "Solo una ocasión tiene 6 o más."),
    ],
    [
        ex("Con estos puntajes (audición 6, 5, 7; interpretación 7, 7, 8; creación 4, 5, 6; reflexión 5, 5, 6), ¿cuántas áreas son fortaleza?", "2", "Son audición e interpretación."),
        ex("Puntajes en tres ocasiones: audición 6, 5, 7; interpretación 7, 7, 8; creación 4, 5, 6. ¿Qué área tiene más ocasiones con 6 o más?", "Interpretación", "Tiene las tres."),
        ex("Creación obtuvo 4, 5 y 6 puntos en tres ocasiones. ¿Cuántos puntos mejoró entre la primera y la tercera?", "2", "6 − 4 = 2."),
    ],
    [
        arith("Interpretación obtuvo 7, 7 y 8 puntos. ¿Cuántos puntos suma en las tres ocasiones?", "7+7+8", "Se suman los tres puntajes.", " puntos"),
        ex("Creación sube un punto en cada ocasión: 4, 5, 6. Si sigue igual, ¿qué puntaje tendrá en la cuarta ocasión?", "7", "Cada ocasión sube 1: 6 + 1 = 7."),
        ex("¿En qué área hubo mayor mejora entre la ocasión 1 y la 3: audición (6, 5, 7), creación (4, 5, 6) o reflexión (5, 5, 6)?", "Creación", "Creación subió 2; las otras dos subieron 1."),
    ],
    [
        ex("Pedro sacó 8 en una sola ocasión y dice que ya tiene una fortaleza. ¿Basta una ocasión? Responde sí o no.", "No", "La regla pide un resultado alto en al menos 2 de 3 ocasiones."),
        ex("Un área tuvo 6, 3 y 6 puntos. ¿Cumple la regla de fortaleza? Responde sí o no.", "Sí", "Tiene 2 ocasiones con 6 o más."),
    ],
    [
        arith("Interpretación suma 7+7+8 puntos y audición suma 6+5+7. ¿Cuántos puntos más suma interpretación?", "7+7+8-(6+5+7)", "Interpretación suma 22 y audición 18.", " puntos"),
        ex("¿Cuántas ocasiones con 6 o más son el mínimo para que haya una fortaleza según la regla?", "2", "La regla pide al menos 2 de 3."),
    ],
    [ex("Camila anotó sus puntajes de coro en tres ensayos: 5, 6 y 6. ¿Tiene una fortaleza en interpretación? Responde sí o no.", "Sí", "Dos ocasiones tienen 6 o más.")],
    [ex("¿Cuántas ocasiones pide la regla para reconocer una fortaleza?", "3", "Se mira en tres ocasiones."), ex("¿Cuántas de esas ocasiones deben ser de 6 o más?", "Al menos 2", "Así lo dice la regla."), ex("¿Para qué sirve conocer una fortaleza?", "Para apoyarme en ella y ayudar a otras personas", "Es un recurso para seguir creciendo.")],
    (
        "Usa este registro inventado de Tomás, con puntajes de 0 a 8 en tres ocasiones. Audición: 4, 6, 6. Interpretación: 5, 5, 7. Creación: 3, 5, 7. Reflexión: 6, 6, 5. Escribe qué áreas son fortaleza según la regla, cuántos puntos mejoró cada área entre la primera y la tercera ocasión y una frase de evidencia sobre su mayor mejora. Después, si quieres, haz lo mismo con tu propio registro, solo para ti.",
        "Fortalezas: audición (6 y 6) y reflexión (6 y 6). Interpretación solo tiene 1 de 3 y creación solo 1 de 3. Mejoras: audición 2, interpretación 2, creación 4, reflexión −1. Mayor mejora: creación, que subió 4 puntos, de 3 a 7.",
        ["aplica la regla en cada área", "calcula bien las mejoras", "da una frase con evidencia"],
        ["tabla con fortalezas", "cálculo de mejoras"],
        ["declarar fortaleza con un solo resultado", "olvidar las mejoras"],
        "Reconoce la tabla y pide mostrar con el dedo en qué ocasiones se cumple la regla.",
    ),
    "Anota tres puntajes de una práctica tuya y revisa si cumples la regla de fortaleza.",
    "Inventa un registro de tres áreas con una fortaleza, un área que mejora y otra que baja, y explica qué harías.",
)

# ---------------------------------------------------------------- OA 06 · clase 3 (áreas de crecimiento y metas)
L(
    OA6, 3,
    "Lápiz y papel. Todos los puntajes y planes están escritos en los ejercicios. Una meta es privada y la defines tú; nadie debe verla si no quieres.",
    "Aprenderé a ver un área de crecimiento como algo en lo que puedo avanzar y a escribir una meta específica, medible, con plazo y con pasos pequeños. Sirve para practicar con un plan y no solo con ganas.",
    ["Sé reconocer una fortaleza con la regla de 6 o más en 2 de 3 ocasiones.", "Sé calcular mejoras sumando y restando.", "Sé multiplicar números pequeños."],
    [
        "Un área de crecimiento es aquella en la que quiero avanzar. No quiere decir que sea malo en ella: significa que todavía estoy aprendiendo. Se reconoce porque su evidencia aún no es alta o porque la practico poco. Para mejorar conviene escribir una meta. Una buena meta es específica (dice qué), medible (tiene un número), tiene plazo (dice hasta cuándo) y es realista (da un paso pequeño).",
        "«Mejorar mi ritmo» no es una buena meta, porque no se puede medir. En cambio, «tocar el compás sin errores 3 veces seguidas en 2 semanas» sí lo es. También hay que planear la práctica: cuántos minutos, cuántos días y qué se hará en cada sesión. Si practicas 10 minutos al día durante 4 días, practicas 40 minutos en la semana. Una meta realista sube un paso por vez: pasar de 3 a 4 aciertos es más realista que de 3 a 8 en un día.",
        "Al final del plazo se mira la evidencia y se decide qué sigue: si la meta se cumplió, se plantea otra un poco más alta; si no, se revisa el plan sin culparse. Quizás hizo falta más tiempo, otra estrategia o un paso más pequeño. Pedir ayuda a un compañero o al profesor también es parte de un buen plan. Aprender música es un proceso, y las metas pequeñas lo hacen visible.",
    ],
    [("área de crecimiento", "habilidad en la que quiero seguir avanzando"), ("meta específica", "dice con claridad qué quiero lograr"), ("meta medible", "tiene un número que permite comprobarla"), ("plazo", "fecha o tiempo en que se revisa la meta"), ("plan de práctica", "minutos, días y tareas para llegar a la meta")],
    [
        ("Elegir la mejor meta", "¿Qué meta está mejor formulada: A) practicar más o B) practicar 10 minutos al día, 4 días, y lograr 3 intentos sin errores?", ["La opción A no tiene número ni plazo.", "La opción B es específica y medible."], "B"),
        ("Calcular un plan", "Practicas 15 minutos 3 veces por semana durante 4 semanas. ¿Cuántos minutos practicas en total?", ["En una semana: 15 × 3 = 45.", "En 4 semanas: 45 × 4 = 180."], "180 minutos"),
    ],
    [
        ("Pensar que un área de crecimiento significa que soy malo.", "Solo significa que todavía estoy aprendiendo y puedo avanzar.", "Escríbelo como «quiero mejorar mi ritmo» y define una meta."),
        ("Plantear una meta enorme para una semana.", "Es imposible de cumplir y desanima.", "Elige un paso pequeño y realista."),
    ],
    [
        ex("¿«Mejorar» es una meta medible? Responde sí o no.", "No", "No tiene un número para comprobar."),
        ex("¿Qué meta es medible: «tocar el compás sin errores 3 veces seguidas» o «tocar mejor»?", "«Tocar el compás sin errores 3 veces seguidas»", "Tiene un número que se puede comprobar."),
        ex("Un área de crecimiento, ¿significa que soy malo en esa área? Responde sí o no.", "No", "Significa que todavía estoy aprendiendo."),
    ],
    [
        ex("La meta es pasar de 4 a 6 aciertos de 8 en 2 semanas. ¿Cuántos aciertos más son?", "2", "6 − 4 = 2."),
        ex("¿Qué meta tiene plazo: A) lograr 6 aciertos de 8 en 3 semanas o B) lograr 6 aciertos de 8?", "A", "Solo la opción A dice hasta cuándo."),
        arith("Practicas 10 minutos al día durante 4 días. ¿Cuántos minutos practicas en la semana?", "10*4", "Se multiplican los minutos por los días.", " minutos"),
    ],
    [
        ex("En creación pasas de 4 a 7 puntos subiendo 1 por semana. ¿Cuántas semanas te toma?", "3", "7 − 4 = 3 puntos, a uno por semana."),
        arith("Practicas 20 minutos 2 veces por semana durante 5 semanas. ¿Cuántos minutos son?", "20*2*5", "Se multiplican minutos, veces y semanas.", " minutos"),
        ex("Dos metas: A) pasar de 3 a 8 puntos en un día o B) pasar de 3 a 4 puntos en una semana. ¿Cuál es más realista?", "B", "Es un paso pequeño con un plazo razonable."),
    ],
    [
        ex("Lucas se propone ser perfecto en una semana. ¿Es una meta realista? Responde sí o no.", "No", "Una meta debe ser un paso pequeño y medible."),
        ex("Una persona no cumplió su meta. ¿Qué conviene hacer: culparse o revisar el plan y ajustarlo?", "Revisar el plan y ajustarlo", "Quizás faltó tiempo o una estrategia mejor."),
    ],
    [
        arith("Necesitas 150 minutos de práctica y planeas 4 semanas con 3 días a la semana y 12 minutos por día. ¿Cuántos minutos te faltan?", "150-4*3*12", "El plan suma 144 minutos.", " minutos"),
        arith("Quieres pasar de 4 a 8 puntos subiendo 1 punto cada 2 semanas. ¿Cuántas semanas necesitas?", "(8-4)*2", "Son 4 puntos y cada uno toma 2 semanas.", " semanas"),
    ],
    [ex("Diego quiere mejorar su afinación. Escribe: «cantar la melodía 1-3-5-3-1 con las 5 notas correctas, 3 veces seguidas, en 2 semanas». ¿Tiene número y plazo? Responde sí o no.", "Sí", "Tiene números (5 notas, 3 veces) y plazo (2 semanas).")],
    [ex("Según la clase, ¿qué cuatro características tiene una buena meta musical?", "Específica, medible, con plazo y realista", "Así se puede comprobar y cumplir."), ex("¿Qué haces si no cumpliste tu meta?", "Revisar el plan y ajustarlo", "No es culpa, es información."), ex("¿Cuántos minutos son 3 días de 10 minutos?", "30", "3 × 10 = 30.")],
    (
        "Elige un área de crecimiento tuya (o la de Ana: interpretación 3 de 5 intentos sin errores) y escribe una meta con estas partes: qué quieres lograr (específico), con qué número (medible), en cuántos días o semanas (plazo) y un plan de práctica (minutos por día y días). Calcula cuántos minutos practicarás en total y qué evidencia mostrará que cumpliste la meta.",
        "Meta de Ana: tocar el compás sin errores 4 de 5 intentos en 3 semanas. Plan: 12 minutos al día, 4 días por semana. Total: 12 × 4 × 3 = 144 minutos. Evidencia: un registro de 5 intentos con 4 sin errores.",
        ["la meta es específica y medible", "tiene plazo y pasos pequeños", "calcula los minutos y define la evidencia"],
        ["meta escrita", "cálculo del plan"],
        ["usar «mejorar» sin número", "plantear una meta imposible"],
        "Reconoce la meta y pide comprobar que tiene número, plazo y una evidencia final concreta.",
    ),
    "Escribe una meta medible para tu práctica de esta semana.",
    "Diseña un plan de 4 semanas para una meta de creación con una revisión al final de cada semana.",
)

# ---------------------------------------------------------------- OA 06 · clase 4 (retroalimentación y reflexión)
FRASE = "Una compañera canta 1-3-5-3-1: llega a tiempo, pero en la cuarta nota baja el volumen y en la última se queda sin aire."

L(
    OA6, 4,
    f"Lápiz y papel. Caso de la clase (inventado): «{FRASE}». Los comentarios se dan con respeto y solo si la persona quiere recibirlos; nadie está obligado a compartir su trabajo.",
    "Aprenderé a dar y recibir comentarios útiles y a escribir una reflexión sobre mi trabajo musical. Sirve para decidir qué mantener y qué ajustar, usando también la mirada de otras personas.",
    ["Sé reconocer fortalezas y áreas de crecimiento.", "Sé que una evidencia es un dato que se puede comprobar.", "Sé escribir una meta medible."],
    [
        "Un comentario útil habla de lo que se oye, no de la persona. Tiene tres partes: qué observo, dónde ocurre y una sugerencia. Por ejemplo: «En el compás 4 la entrada llegó tarde; prueba contar un pulso antes». Un comentario como «está bien» o «está mal» es vago, y uno como «eres malo» es un juicio sobre la persona y no se dice. También se dicen cosas que salieron bien, con evidencia: «Me gustó cómo bajaste el volumen al final».",
        "Recibir comentarios también se aprende. Se escucha sin interrumpir, se piden ejemplos si algo no queda claro y se decide qué usar. No hay que aceptar todo: se prioriza lo que se apoya en evidencia y lo que ayuda a la meta. Compartir una grabación o una interpretación es voluntario y se hace solo con quien la persona elija, por ejemplo con el profesor o con un compañero de confianza.",
        "La reflexión escrita completa el ciclo. Se responden tres preguntas: qué hice, qué aprendí y qué cambiaría la próxima vez. Con las respuestas se actualizan las fortalezas, las áreas de crecimiento y la meta. Reunir en una carpeta los trabajos y las reflexiones forma un portafolio, que muestra con evidencia cómo se avanza a lo largo del tiempo y ayuda a recordar los logros.",
    ],
    [("comentario útil", "habla de lo que se oye, dice dónde y propone un ajuste"), ("sugerencia", "propuesta concreta para mejorar"), ("reflexión", "escrito que responde: qué hice, qué aprendí y qué cambiaría"), ("portafolio", "carpeta con trabajos y reflexiones que muestra el avance"), ("voluntario", "que cada persona decide si lo hace o no")],
    [
        ("Elegir el mejor comentario", f"Caso: «{FRASE}» ¿Qué comentario es más útil: A) «Se te acabó el aire en la última nota; prueba respirar antes de ese compás» o B) «Cantas mal»?", ["La opción A dice qué se oye, dónde y propone un ajuste.", "La opción B es un juicio sobre la persona."], "A"),
        ("Ordenar la reflexión", "La reflexión tiene tres preguntas: 1) qué hice, 2) qué aprendí, 3) qué cambiaría. ¿Cuál es la segunda?", ["El orden está numerado.", "El número 2 es «qué aprendí»."], "Qué aprendí"),
    ],
    [
        ("Dar un comentario sobre la persona, como «eres malo».", "Duele y no dice qué mejorar; el comentario debe hablar de lo que se oye.", "Describe lo observado y propone un ajuste."),
        ("Aceptar todos los comentarios sin pensar.", "No todos se apoyan en evidencia ni ayudan a tu meta.", "Prioriza los comentarios con evidencia y que ayuden a tu meta."),
    ],
    [
        ex("Un comentario útil, ¿habla de lo que se oye o de la persona?", "De lo que se oye", "Así se puede mejorar."),
        ex("¿Es respetuoso decir «eres malo» a una compañera? Responde sí o no.", "No", "Es un juicio sobre la persona."),
        ex("¿Qué es un portafolio?", "Una carpeta con trabajos y reflexiones que muestra el avance", "Reúne evidencia del progreso."),
    ],
    [
        ex("Comentarios: 1) «Está bien». 2) «En el compás 4 la entrada llegó tarde; prueba contar un pulso antes». 3) «Eres malo». 4) «Me gustó cómo bajaste el volumen al final». ¿Cuáles son comentarios útiles?", "El 2 y el 4", "Hablan de lo que se oye, con evidencia."),
        ex("En el comentario «En el compás 4 la entrada llegó tarde; prueba contar un pulso antes», ¿cuál es la sugerencia?", "Prueba contar un pulso antes", "Es la parte que propone un ajuste."),
        ex("La reflexión pregunta qué cambiaría la próxima vez. ¿Mira hacia el pasado o hacia el futuro?", "Hacia el futuro", "Propone qué hacer distinto en adelante."),
    ],
    [
        ex("¿Qué comentario sobre una melodía sin cierre es mejor: A) «Terminó sin cierre porque no acabó en 1; prueba terminar en la nota 1» o B) «Terminó mal»?", "A", "La A dice qué se oye, por qué y qué hacer."),
        arith("Un portafolio tiene 3 trabajos por cada una de las 4 áreas. ¿Cuántos trabajos tiene?", "3*4", "Se multiplican los trabajos por las áreas.", " trabajos"),
        ex("Marta no quiere compartir su grabación con el curso. ¿Hay que obligarla? Responde sí o no.", "No", "Compartir es voluntario."),
    ],
    [
        ex("Una persona escribe «¡Eres genial!» como único comentario. ¿Ayuda a mejorar? Responde sí o no.", "No", "No dice qué se oyó ni qué ajustar."),
        ex("Recibes tres comentarios: uno vago y dos con evidencia. ¿Cuántos usas para decidir un ajuste?", "2", "Los dos que se apoyan en evidencia."),
    ],
    [
        arith("Haces 3 sesiones de reflexión de 10 minutos por semana durante 4 semanas. ¿Cuántos minutos son?", "3*10*4", "Se multiplican sesiones, minutos y semanas.", " minutos"),
        ex("Tu reflexión dice: qué hice, qué aprendí y qué cambiaría. ¿Cuántas preguntas responde?", "3", "Son tres preguntas."),
    ],
    [ex("Un compañero te dice: «En el compás 7 el volumen subió demasiado; prueba bajar un poco». ¿Cuántas partes del comentario útil tiene: qué observa, dónde y una sugerencia?", "3", "Observa el volumen, dice el compás 7 y sugiere bajar un poco.")],
    [ex("¿Qué se hace al recibir un comentario que no queda claro?", "Pedir un ejemplo", "Así se entiende lo que se observó."), ex("¿Cuántas partes tiene un comentario útil?", "3", "Qué observo, dónde y una sugerencia."), ex("¿Quién decide si se comparte un trabajo?", "La persona que lo hizo", "Compartir es voluntario.")],
    (
        f"Lee el caso: «{FRASE}» Escribe un comentario con tres partes (lo que observas, dónde y una sugerencia) y un comentario positivo con evidencia. Después escribe tu propia reflexión con las tres preguntas (qué hice, qué aprendí, qué cambiaría) sobre el último trabajo musical que hiciste en esta unidad (si no recuerdas uno, usa la improvisación de 8 notas o el compás de 4/4 que escribiste).",
        "Comentario: «En la cuarta nota el volumen bajó; prueba mantener el aire parejo hasta ahí». Comentario positivo: «Llegaste justo a tiempo en todas las notas». Reflexión: hice una improvisación de 8 notas; aprendí que terminar en 1 se siente como final; la próxima vez repetiría una idea corta para que tenga más sentido.",
        ["el comentario tiene qué, dónde y sugerencia", "incluye un comentario positivo con evidencia", "la reflexión responde las tres preguntas"],
        ["comentarios escritos", "reflexión de tres preguntas"],
        ["hablar de la persona y no de lo que se oye", "responder la reflexión con una sola palabra"],
        "Reconoce los comentarios y pide cambiar cualquier frase vaga por un dato que se pueda comprobar.",
    ),
    "Escribe un comentario con tres partes sobre una canción que hayas escuchado hoy.",
    "Arma una página de portafolio con un trabajo, una evidencia, una reflexión y una meta.",
)
