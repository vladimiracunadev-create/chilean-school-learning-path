"""Student material for 8.º básico Música, OA 06 (explicar fortalezas y áreas de crecimiento personal en la audición, interpretación, creación y reflexión, y su influencia en el trabajo musical propio y colectivo).

Todos los puntajes, tomas y casos de los ejercicios son datos de ejemplo inventados para esta clase.
"""
from __future__ import annotations

from student_content_mu8_a import L
from student_lessons import arith, ex

OA6 = "MU08 OA 06"

NIVELES = "1 = aún no se observa; 2 = en desarrollo; 3 = logrado; 4 = profundizado"

# ---------------------------------------------------------------- OA 06 · clase 1 (autoevaluar con evidencia)
L(
    OA6, 1,
    f"Lápiz y papel. Niveles de la clase: {NIVELES}. Las tomas, los mapas y las notas están descritos en los ejercicios (son de ejemplo). Puedes aplicar lo aprendido a tu propio trabajo musical de la unidad.",
    "Aprenderé a autoevaluarme en cuatro dimensiones (audición, interpretación, creación y reflexión) usando evidencia y niveles. Sirve para saber qué hago bien y qué puedo mejorar, sin juzgarme como persona.",
    ["Sé hacer un mapa de escucha y medir la precisión de una toma.", "Sé que una creación se revisa con criterios.", "Sé sumar y calcular porcentajes sencillos."],
    [
        "Autoevaluarse es revisar el propio trabajo con la misma seriedad que se revisaría el de otra persona. Se hace en cuatro dimensiones. En la audición, se comprueba si identifico rasgos audibles y los ubico en el tiempo. En la interpretación, se mide la precisión del ritmo y las notas. En la creación, se revisa si cumplí las reglas y si mi variación se oye. En la reflexión, se verifica si explico mis decisiones con evidencia.",
        f"Cada dimensión se ubica en un nivel de la escala: {NIVELES}. Un nivel solo vale si se apoya en evidencia, que es un dato del propio trabajo, como un mapa de escucha con marcas correctas, una toma con 17 de 20 notas acertadas o una creación que cumple las cuatro reglas. Decir «soy malo para cantar» es un juicio sobre la persona. Decir «acerté 12 de 20 notas» es evidencia sobre el trabajo.",
        "Con los niveles se pueden hacer cálculos: la suma de los cuatro puntajes se compara con el máximo, que es 16. Un nivel bajo no dice que alguien no sirva para la música: indica qué dimensión conviene trabajar. Al repetir la autoevaluación unas semanas después, se compara con la anterior para ver qué cambió.",
    ],
    [("autoevaluación", "revisar el propio trabajo con criterios y evidencia"), ("dimensión", "cada una de las cuatro áreas: audición, interpretación, creación y reflexión"), ("nivel", "puntaje de 1 a 4 que describe qué tanto se observa un logro"), ("evidencia", "dato del propio trabajo que apoya un nivel"), ("juicio sobre la persona", "frase que dice cómo soy en lugar de describir lo que hice")],
    [
        ("Clasificar la evidencia", "La frase «ubiqué 4 de las 5 marcas del mapa de escucha» ¿en cuál dimensión se ubica?", ["Habla de ubicar marcas en el tiempo.", "Eso es identificar rasgos al escuchar."], "En la audición"),
        ("Sumar puntajes", "Una estudiante se pone 3 en audición, 2 en interpretación, 4 en creación y 2 en reflexión. ¿Cuántos puntos suma de 16?", ["Se suman los cuatro puntajes.", "3 + 2 + 4 + 2 = 11."], "11 de 16"),
    ],
    [
        ("Ponerse un nivel solo porque «me siento segura».", "Sin evidencia no se puede comprobar el nivel.", "Anota un dato del trabajo que apoye el puntaje."),
        ("Pensar que un nivel bajo significa que no sirvo para la música.", "El nivel describe el trabajo de hoy y se puede mejorar.", "Elige una dimensión y trabájala con un plan."),
    ],
    [
        ex("La frase «Entra un tambor a los 12 segundos» describe lo que una persona logró al escuchar. ¿En qué dimensión se ubica?", "En la audición", "Identifica un rasgo audible y su momento."),
        ex("La frase «Canté 17 de 20 notas bien en la toma 2» ¿en qué dimensión se ubica?", "En la interpretación", "Mide la precisión al cantar."),
        ex("La frase «Escribí una variación que cambia el ritmo» ¿en qué dimensión se ubica?", "En la creación", "Se trata de crear una variación."),
    ],
    [
        ex("¿Cuál es evidencia sobre el trabajo? A) «Soy malo para cantar». B) «En la toma 1 acerté 12 de 20 notas».", "B", "La segunda frase es un dato comprobable; la primera juzga a la persona."),
        ex("En la escala de la clase, ¿qué significa el nivel 3?", "Logrado", "La escala es 1 aún no, 2 en desarrollo, 3 logrado y 4 profundizado."),
        ex("¿Qué evidencia sirve para la dimensión de reflexión? A) Un texto que explica por qué elegí un acorde, citando una nota de la melodía. B) Una lista de los instrumentos que había en la sala.", "A", "La reflexión se evidencia explicando decisiones con datos."),
    ],
    [
        arith("Otra estudiante se pone 4 en audición, 3 en interpretación, 2 en creación y 3 en reflexión. ¿Cuántos puntos suma?", "4+3+2+3", "Se suman los cuatro puntajes.", " puntos"),
        ex("Con los puntajes de audición 4, interpretación 3, creación 2 y reflexión 3, ¿cuál es la dimensión con el nivel más bajo?", "Creación", "Tiene nivel 2, el más bajo de los cuatro."),
        arith("En una toma de 24 notas, 18 son correctas. ¿Qué porcentaje de aciertos hay?", "18*100//24", "Se divide lo correcto por el total y se multiplica por 100.", " %"),
    ],
    [
        ex("Marta se pone 4 en interpretación solo porque «me siento segura». ¿Qué le falta a su autoevaluación?", "Evidencia", "Necesita un dato, como los aciertos de una toma."),
        ex("Pedro dice: «Tengo 2 en creación, así que no sirvo para la música». ¿Es correcta su conclusión? Responde sí o no.", "No", "El nivel 2 indica trabajo en desarrollo, no falta de capacidad."),
    ],
    [
        arith("Cuatro dimensiones tienen los niveles 2, 3, 3 y 4. ¿Cuál es el promedio de los niveles?", "(2+3+3+4)//4", "Se suman los niveles y se divide por cuatro.", ""),
        arith("En la primera unidad una estudiante sumó 9 puntos y en la segunda sumó 13, de un máximo de 16. ¿Cuántos puntos le faltan en la segunda para llegar al máximo?", "16-13", "Se resta lo obtenido del máximo de 16.", " puntos"),
    ],
    [ex("Para autoevaluarte tienes cuatro evidencias: un mapa con 4 de 5 marcas correctas, una toma con 17 de 20 notas acertadas, una creación que cumple las cuatro reglas y un texto que explica una decisión. ¿En cuántas de las cuatro dimensiones tienes evidencia?", "En las 4", "Cada evidencia corresponde a una dimensión distinta.")],
    [ex("¿Cuáles son las cuatro dimensiones de la clase?", "Audición, interpretación, creación y reflexión", "Son las áreas del trabajo musical."), ex("¿Qué debe apoyar un nivel?", "Evidencia", "Sin evidencia no se puede comprobar."), ex("¿Cuál es el puntaje máximo con cuatro dimensiones y niveles de 1 a 4?", "16", "Cuatro dimensiones por 4 puntos.")],
    (
        f"Autoevalúate con este caso de ejemplo y la escala ({NIVELES}). Evidencias de una estudiante: mapa de escucha con 3 de 5 marcas correctas; toma con 15 de 20 notas correctas; creación que cumple 3 de las 4 reglas; texto de reflexión que explica una decisión citando un dato. Escribe 1) un nivel para cada dimensión con la evidencia que lo apoya, 2) la suma de puntos, 3) la dimensión que trabajarías primero. Después haz lo mismo con tu propio trabajo, usando datos de tus tareas.",
        "Audición 2 (3 de 5 marcas); interpretación 3 (75 % de aciertos); creación 3 (3 de 4 reglas); reflexión 3 (explica con un dato). Suma: 2 + 3 + 3 + 3 = 11 de 16. Trabajaría primero la audición, porque tiene el nivel más bajo.",
        ["pone un nivel apoyado en un dato", "suma bien los puntos", "elige una dimensión con una razón"],
        ["cuatro niveles con evidencia", "suma y dimensión elegida"],
        ["poner niveles sin evidencia", "usar frases que juzgan a la persona"],
        "Reconoce los niveles y pide señalar, en una dimensión, el dato exacto que apoya el nivel elegido.",
    ),
    "Escribe una frase de evidencia sobre tu trabajo musical que incluya un número.",
    "Compara tu autoevaluación de dos unidades distintas y explica qué dimensión cambió más.",
)

# ---------------------------------------------------------------- OA 06 · clase 2 (fortalezas y su aporte al trabajo colectivo)
L(
    OA6, 2,
    "Lápiz y papel. Los grupos, las tomas y los datos están en los ejercicios (son de ejemplo). Puedes aplicar lo aprendido a un trabajo en grupo que hayas hecho o hagas en la unidad.",
    "Aprenderé a reconocer mis fortalezas musicales con evidencia y a explicar cómo aportan al trabajo del grupo. Sirve para repartir roles con sentido y para aprender de las fortalezas de otras personas.",
    ["Sé autoevaluarme con evidencia en cuatro dimensiones.", "Sé calcular un porcentaje de aciertos.", "Sé que un grupo se organiza con roles."],
    [
        "Una fortaleza es algo que hago bien y que puedo mostrar con evidencia, como mantener un pulso parejo en tres tomas seguidas, anotar cifrados (los acordes escritos con letras) sin errores o entrar siempre a tiempo con mi voz. No se trata de ser mejor que otra persona, sino de saber qué puedo aportar. Reconocer una fortaleza con datos evita dos extremos: presumir sin pruebas o creer que no se tiene ninguna.",
        "En el trabajo colectivo, cada fortaleza cumple un papel. Quien mantiene el pulso ayuda a que todos suenen juntos. Quien lee bien el cifrado ayuda a que el acompañamiento sea correcto. Quien entra a tiempo da seguridad a las otras voces. Un grupo con fortalezas distintas es más completo que uno donde todos hacen lo mismo. Conocer las fortalezas permite repartir roles y rotarlos, para que todas las personas aprendan.",
        "Tener una fortaleza no significa que no haya nada que mejorar, ni que una sola persona deba hacerlo todo. Quien tiene una fortaleza la comparte: muestra cómo lo hace y ayuda a practicar. De esa manera el grupo mejora completo. Para decidir quién cumple un rol, se usan los datos de las tomas y no la simpatía ni la costumbre.",
    ],
    [("fortaleza", "algo que hago bien y puedo mostrar con evidencia"), ("aporte", "lo que mi fortaleza le entrega al trabajo del grupo"), ("rol", "tarea que una persona asume en el grupo"), ("rotar", "cambiar los roles para que todas las personas los practiquen"), ("evidencia", "dato comprobable del trabajo")],
    [
        ("Elegir con datos", "En una toma de 20 pulsos, Ana mantuvo 19 parejos, Beto 14 y Carla 17. ¿A quién conviene encargar que marque el pulso para el grupo?", ["Se compara quién mantuvo más pulsos parejos.", "Ana tuvo 19, el número mayor."], "A Ana"),
        ("Calcular el aporte", "Ana acierta el 95 % de las notas y Beto el 70 %. Si Ana ayuda a Beto, ¿cuántos puntos de diferencia hay entre los dos porcentajes hoy?", ["Se resta lo de Beto de lo de Ana.", "95 − 70 = 25."], "25 puntos"),
    ],
    [
        ("Pensar que una fortaleza me hace mejor que las demás personas.", "Una fortaleza es un aporte al grupo, no un título.", "Preséntala como algo que puedo compartir."),
        ("Hacer yo solo todo lo que se me da bien.", "Los demás no aprenden y el grupo depende de una sola persona.", "Rota los roles y enseña cómo lo haces."),
    ],
    [
        ex("¿Una fortaleza se demuestra con una opinión o con evidencia?", "Con evidencia", "Debe ser un dato comprobable."),
        ex("Ana mantiene un pulso parejo. ¿Qué aporta al grupo?", "Ayuda a que todos suenen juntos", "Un pulso parejo ordena a las demás voces."),
        ex("¿Para qué sirve conocer las fortalezas de cada integrante?", "Para repartir roles y aprender unos de otros", "Así el grupo se organiza mejor."),
    ],
    [
        ex("¿Qué actitud es mejor? A) Ana usa su fortaleza para ayudar al grupo a mantener el pulso. B) Ana dice que nadie más puede hacerlo.", "A", "Una fortaleza se comparte; no se usa para presumir."),
        ex("Un grupo tiene personas con fortalezas distintas (pulso, cifrado y entradas). ¿Esto es una ventaja o una dificultad?", "Una ventaja", "Se cubren más necesidades del trabajo."),
        ex("Quien tiene una fortaleza, ¿debe hacer todo el trabajo del grupo? Responde sí o no.", "No", "El grupo aprende cuando los roles se reparten y rotan."),
    ],
    [
        arith("Ana acertó 19 de 20 pulsos. ¿Qué porcentaje de aciertos tiene?", "19*100//20", "Se divide lo correcto por el total y se multiplica por 100.", " %"),
        arith("Un ensayo de 40 minutos se divide en turnos de 10 minutos en los que se rotan los roles. ¿Cuántos turnos hay?", "40//10", "Se divide el tiempo total por la duración de cada turno.", " turnos"),
        arith("Carla tiene 90 % de aciertos y Beto 70 %. ¿Cuántos puntos de diferencia hay entre los dos porcentajes?", "90-70", "Se resta el porcentaje menor del mayor.", " puntos"),
    ],
    [
        ex("Beto anota los cifrados sin errores, pero siempre hace él solo el trabajo de cifrado del grupo. ¿Qué pierde el grupo? A) Que las demás personas aprendan a hacerlo. B) Que el cifrado esté bien escrito.", "A", "El cifrado ya está bien; lo que se pierde es el aprendizaje de los demás."),
        ex("Carla tiene una fortaleza en las entradas a tiempo. ¿Significa que no necesita mejorar nada? Responde sí o no.", "No", "Una fortaleza no elimina otras áreas de crecimiento."),
    ],
    [
        arith("En 6 ensayos, tres personas rotan por igual el rol de marcar el pulso. ¿Cuántos ensayos marca el pulso cada una?", "6//3", "Se reparten los 6 ensayos en partes iguales entre 3 personas.", " ensayos"),
        arith("Ana acertó 19, 20 y 18 notas en tres tomas de 20 notas cada una. ¿Cuántas notas acertó en total?", "19+20+18", "Se suman las notas acertadas de las tres tomas.", " notas"),
    ],
    [ex("El grupo debe elegir quién marca el pulso según la evidencia de otra toma de 20 pulsos: Ana 17 parejos, Beto 20 y Carla 15. ¿A quién le corresponde marcar el pulso?", "A Beto", "Tuvo el mayor número de pulsos parejos.")],
    [ex("¿Qué es una fortaleza?", "Algo que hago bien y puedo mostrar con evidencia", "No es una opinión."), ex("¿Qué hace quien tiene una fortaleza con el grupo?", "La comparte", "Muestra cómo lo hace y ayuda a practicar."), ex("¿Por qué se rotan los roles?", "Para que todos aprendan", "Cada persona practica todos los roles.")],
    (
        "Lee este caso de ejemplo de un grupo de cuatro. Ana: 19 de 20 pulsos parejos. Beto: 20 de 20 cifrados correctos. Carla: 18 de 20 entradas a tiempo. Diego: organizó tres ensayos con horario cumplido. Escribe 1) la fortaleza de cada persona con su dato, 2) el aporte de cada una al grupo, 3) un plan de rotación de tres ensayos para que cada persona practique un rol distinto, 4) qué fortaleza tuya aportarías a un grupo y qué dato la apoya.",
        "Ana: pulso, 95 % de pulsos parejos; ayuda a que todos suenen juntos. Beto: cifrado, 100 % correcto; asegura un acompañamiento correcto. Carla: entradas a tiempo, 90 %; da seguridad a las voces. Diego: organización, 3 de 3 ensayos con horario cumplido; ordena el trabajo. Rotación: en cada ensayo cambian los roles entre las cuatro personas.",
        ["usa un dato para cada fortaleza", "relaciona cada fortaleza con un aporte", "propone una rotación de roles"],
        ["cuatro fortalezas con dato y aporte", "plan de rotación"],
        ["decir una fortaleza sin dato", "dejar a una sola persona con el mismo rol"],
        "Reconoce el análisis y pide explicar cómo ayudaría Ana a una persona que quiere mejorar su pulso.",
    ),
    "Escribe una fortaleza tuya en la música y el dato que la apoya.",
    "Describe cómo tu fortaleza ayudaría a un grupo y qué aprenderías tú de otra persona.",
)

# ---------------------------------------------------------------- OA 06 · clase 3 (áreas de crecimiento y metas)
L(
    OA6, 3,
    "Lápiz y papel. Las tomas, las metas y los planes están en los ejercicios (son de ejemplo). Puedes aplicar lo aprendido a una meta propia de práctica musical que quepa en tu semana.",
    "Aprenderé a describir un área de crecimiento con un dato, a formular una meta específica, medible y con plazo, y a armar un plan de práctica. Sirve para mejorar de manera ordenada y comprobable.",
    ["Sé reconocer una fortaleza con evidencia.", "Sé calcular un porcentaje de aciertos.", "Sé multiplicar números pequeños."],
    [
        "Un área de crecimiento es algo que aún puedo mejorar en mi trabajo musical. Se describe con un dato y sin juzgar a la persona: «en la toma 1 acerté 12 de 20 notas» es una descripción; «soy desafinado» es un juicio. Conviene elegir una o dos áreas al comienzo, porque trabajar muchas cosas a la vez dispersa el esfuerzo. Elegir un área para mejorar no significa que lo demás esté mal.",
        "Una meta útil es específica, medible y tiene plazo. Por ejemplo: «pasar de 12 a 16 notas correctas de 20 en 2 semanas». Dice qué mejora, cuánto y para cuándo. Con la meta se arma un plan de práctica, que indica cuántos minutos, cuántos días y qué trozo se ensaya. Si se practican 10 minutos, 4 días por semana, durante 2 semanas, son 10 × 4 × 2 = 80 minutos en total.",
        "Al final del plazo se mide de nuevo y se compara con el dato inicial. Si se logró, se plantea una meta nueva. Si no se logró, se revisa el plan: tal vez faltaron minutos, o se ensayó un trozo equivocado. Ajustar el plan es parte del trabajo, no un fracaso. También conviene contarle la meta a una persona del grupo, porque el avance de cada uno ayuda al trabajo colectivo.",
    ],
    [("área de crecimiento", "aspecto del trabajo musical que aún puedo mejorar"), ("meta", "objetivo específico, medible y con plazo"), ("plan de práctica", "cuántos minutos, cuántos días y qué trozo se ensaya"), ("medible", "que se puede comprobar con un número"), ("plazo", "tiempo en que se quiere lograr la meta")],
    [
        ("Elegir la meta", "¿Cuál es una meta mejor formulada? A) «Quiero mejorar». B) «Quiero pasar de 12 a 16 notas correctas de 20 en 2 semanas».", ["La meta debe ser específica, medible y con plazo.", "La segunda dice qué mejora, cuánto y para cuándo."], "La segunda"),
        ("Calcular la práctica", "Un plan es practicar 10 minutos, 4 días por semana, durante 2 semanas. ¿Cuántos minutos son en total?", ["Se multiplican los minutos por los días y por las semanas.", "10 × 4 × 2 = 80."], "80 minutos"),
    ],
    [
        ("Plantear metas vagas como «tocar mejor».", "No se puede comprobar si se cumplió.", "Agrega un número y un plazo."),
        ("Abandonar la meta cuando no se cumple a tiempo.", "Conviene revisar el plan y ajustarlo.", "Cambia minutos, días o el trozo que ensayas."),
    ],
    [
        ex("¿Una meta vaga como «quiero mejorar» se puede comprobar? Responde sí o no.", "No", "No tiene número ni plazo."),
        ex("Un área de crecimiento, ¿es un defecto de la persona? Responde sí o no.", "No", "Es un aspecto del trabajo que se puede mejorar."),
        ex("Al comienzo, ¿cuántas áreas conviene priorizar: una o dos, o todas?", "Una o dos", "Trabajar todo a la vez dispersa el esfuerzo."),
    ],
    [
        arith("Una estudiante practica 20 minutos, 3 días por semana. ¿Cuántos minutos practica en una semana?", "20*3", "Se multiplican los minutos de cada día por los días.", " minutos"),
        ex("En la meta «pasar de 9 a 15 notas correctas de 20 en 3 semanas», ¿qué parte indica el plazo?", "En 3 semanas", "El plazo es el tiempo para lograr la meta."),
        ex("¿Qué dato mide el progreso en la meta de notas correctas? A) El número de notas correctas por toma. B) Cuántos instrumentos hay en la sala.", "A", "Se compara la cantidad de notas correctas entre tomas."),
    ],
    [
        arith("Una meta sube las notas correctas de 9 a 15 en una toma de 20 notas. ¿Cuántas notas correctas más son?", "15-9", "Se resta lo inicial de lo que se quiere lograr.", " notas más"),
        arith("Una estudiante pasa de 9 de 20 a 15 de 20 notas correctas. ¿Cuántos puntos sube su porcentaje de aciertos?", "15*100//20-9*100//20", "Se calcula el porcentaje de cada toma y se resta.", " puntos"),
        arith("Un plan indica 15 minutos por día, 3 días por semana, durante 3 semanas. ¿Cuántos minutos practica en total?", "15*3*3", "Se multiplican minutos, días y semanas.", " minutos"),
    ],
    [
        ex("¿Qué meta es mejor? A) «Tocar bien el ritmo». B) «Tocar 3 de 3 tomas con el pulso parejo en 10 días».", "B", "La segunda se puede medir y tiene plazo."),
        ex("Pasadas dos semanas, una estudiante no alcanzó su meta. ¿Qué es más útil: ajustar el plan o concluir que no sirve para la música?", "Ajustar el plan", "Revisar minutos, días o el trozo ensayado ayuda a mejorar."),
    ],
    [
        arith("Una meta quiere pasar de 10 a 18 notas correctas subiendo 2 notas por semana. ¿Cuántas semanas necesita?", "(18-10)//2", "La diferencia se divide por el avance semanal.", " semanas"),
        arith("Un plan indica 12 minutos por día, 5 días por semana, durante 3 semanas. ¿Cuántos minutos practica en total?", "12*5*3", "Se multiplican minutos, días y semanas.", " minutos"),
    ],
    [arith("Tomás tiene 40 minutos a la semana para practicar y los reparte en 5 días iguales. ¿Cuántos minutos practica por día?", "40//5", "Se reparte el tiempo semanal entre los días.", " minutos")],
    [ex("¿Qué tres características tiene una buena meta?", "Específica, medible y con plazo", "Así se puede comprobar."), ex("¿Qué se hace si no se cumple la meta a tiempo?", "Se revisa y ajusta el plan", "El plan se mejora."), ex("¿Con qué se describe un área de crecimiento?", "Con un dato", "No con un juicio sobre la persona.")],
    (
        "Usa este caso de ejemplo: en la toma 1 de una canción de 20 notas, una estudiante acertó 12 notas y entró tarde en 2 de 5 entradas. 1) Describe dos áreas de crecimiento con datos. 2) Elige una y escribe una meta con número y plazo de 2 semanas. 3) Arma un plan con minutos, días por semana y el trozo que ensayará; calcula los minutos totales. 4) Indica cómo medirá el progreso al final. Después haz lo mismo con una meta musical tuya.",
        "Áreas: notas correctas (12 de 20) y entradas a tiempo (3 de 5). Meta: pasar de 12 a 16 notas correctas de 20 en 2 semanas. Plan: 10 minutos, 4 días por semana, ensayando despacio los trozos con notas incorrectas; total 80 minutos. Medición: una nueva toma al final de las 2 semanas, comparando las notas correctas.",
        ["describe áreas con datos y sin juicios", "formula una meta con número y plazo", "calcula los minutos totales del plan"],
        ["dos áreas descritas", "meta", "plan con minutos totales"],
        ["escribir «soy desafinado»", "plantear una meta sin plazo"],
        "Reconoce la meta y pide mostrar cómo comprobará, con un número, si se cumplió.",
    ),
    "Escribe una meta musical con un número y un plazo de una semana.",
    "Arma un plan de práctica de tres semanas con minutos y días, y calcula los minutos totales.",
)

# ---------------------------------------------------------------- OA 06 · clase 4 (retroalimentación y reflexión)
L(
    OA6, 4,
    "Lápiz y papel. Los comentarios, las tomas y los casos están en los ejercicios (son de ejemplo). Puedes practicar con una persona de tu casa, dándole un comentario respetuoso sobre algo que haya hecho.",
    "Aprenderé a dar y recibir retroalimentación respetuosa y útil, y a escribir una reflexión sobre cómo mi trabajo influye en el grupo. Sirve para mejorar mi trabajo y el del equipo, cuidando a las personas.",
    ["Sé describir un hecho audible con precisión.", "Sé formular una meta con número y plazo.", "Sé reconocer una fortaleza con evidencia."],
    [
        "La retroalimentación es un comentario sobre el trabajo que ayuda a mejorarlo. Es útil cuando describe lo que se oyó, dice qué funcionó y sugiere un cambio concreto. Una forma sencilla es: «Se oye…; sugiero…». Por ejemplo: «Se oyó el 4 en vez del 3 en la tercera nota; sugiero cantarla partiendo de la nota 2». El comentario habla de la música y no de la persona: «eres desafinado» es un juicio, no una ayuda.",
        "Para recibir retroalimentación, se escucha completa, se pregunta si algo no se entendió y se prueba un cambio a la vez. Si se cambian muchas cosas juntas, no se sabe cuál ayudó. También se agradece, aunque no se esté de acuerdo en todo. Si un comentario es ofensivo o hace sentir muy mal, no se responde con otro insulto: se avisa a una persona adulta de confianza.",
        "La reflexión es pensar y escribir sobre el propio trabajo. Una reflexión completa tiene cuatro partes: lo que hice, la evidencia, el efecto en el grupo y el próximo paso. Por ejemplo: «Marqué el pulso con el pie; en la toma 2 hubo 17 de 20 notas correctas; el grupo entró junto; ensayaré las entradas». Reflexionar muestra cómo el trabajo propio influye en el colectivo y qué decisión tomar a continuación.",
    ],
    [("retroalimentación", "comentario sobre el trabajo que ayuda a mejorarlo"), ("sugerencia", "cambio concreto que se propone"), ("reflexión", "pensar y escribir sobre el propio trabajo con evidencia"), ("juicio sobre la persona", "frase que dice cómo es alguien en lugar de describir su trabajo"), ("persona adulta de confianza", "adulto al que se le pide ayuda si algo me hace sentir mal")],
    [
        ("Reconocer un buen comentario", "¿Cuál comentario es útil? A) «Eres desafinado». B) «En la tercera nota se oyó 4 en vez de 3; prueba cantarla partiendo de la nota 2».", ["Debe describir lo que se oyó.", "Y sugerir un cambio concreto, sin juzgar a la persona."], "El segundo"),
        ("Completar una reflexión", "Una reflexión dice: «Marqué el pulso con el pie. En la toma 2 hubo 17 de 20 notas correctas, 5 más que en la 1. El grupo entró junto en 3 de 4 entradas». ¿Qué parte de las cuatro falta?", ["Hay lo que hice, la evidencia y el efecto en el grupo.", "No dice qué hará después."], "El próximo paso"),
    ],
    [
        ("Criticar a la persona en lugar de la música.", "Un juicio sobre la persona no ayuda a mejorar y puede herir.", "Describe lo que se oyó y sugiere un cambio."),
        ("Cambiar todo a la vez al recibir tres sugerencias.", "No se sabe cuál cambio sirvió.", "Prueba una sugerencia a la vez."),
    ],
    [
        ex("La retroalimentación útil, ¿habla de la música o de la persona?", "De la música", "Describe lo que se oyó y propone un cambio."),
        ex("En la fórmula «Se oye…; sugiero…», ¿qué parte entrega el hecho audible?", "«Se oye…»", "Ahí se describe lo que se escuchó."),
        ex("Si un comentario te ofende o te hace sentir muy mal, ¿qué haces?", "Aviso a una persona adulta de confianza", "No se responde con otro insulto."),
    ],
    [
        ex("¿Qué comentario es respetuoso y útil? A) «Tu pulso se aceleró en el compás 3; prueba marcarlo con el pie». B) «Qué mal tocas».", "A", "Describe lo que se oyó y sugiere un cambio sin juzgar a la persona."),
        ex("Al recibir retroalimentación, ¿conviene discutir cada comentario o escuchar y probar un cambio?", "Escuchar y probar un cambio", "Así se comprueba si la sugerencia ayuda."),
        ex("Una reflexión completa tiene cuatro partes: lo que hice, la evidencia, el efecto en el grupo y el próximo paso. ¿Cuántas partes tiene?", "4", "Son las cuatro partes nombradas."),
    ],
    [
        arith("Tres compañeros dan 2 sugerencias cada uno, y solo se prueban 2 sugerencias por ensayo. ¿Cuántos ensayos hacen falta para probarlas todas?", "(3*2)//2", "Son 6 sugerencias y se prueban de a 2 por ensayo.", " ensayos"),
        arith("Antes del ajuste, una estudiante acertó 9 de 15 notas. Después acertó 12 de 15. ¿Cuántas notas correctas más tiene?", "12-9", "Se resta lo de antes de lo de después.", " notas más"),
        ex("Ana oye la grabación y nota que la voz 2 entró en el compás 6 en vez del 5. ¿Qué comentario es mejor? A) «Se oyó la voz 2 entrar en el compás 6 y no en el 5; prueben contar un compás en silencio». B) «Ustedes siempre fallan».", "A", "Describe lo que se oyó y sugiere un cambio concreto."),
    ],
    [
        ex("Lucas recibe tres sugerencias y cambia todo a la vez. ¿Qué no podrá saber?", "Cuál sugerencia produjo la mejora", "Cambió varias cosas juntas."),
        ex("Un compañero dice: «Se ve que no ensayaste». ¿Por qué no es un comentario útil?", "Supone algo y no describe lo que se oyó", "No entrega un dato ni una sugerencia concreta."),
    ],
    [
        ex("Una reflexión dice: «Practiqué la célula 3 durante tres días. En la toma 3 hubo 18 de 20 notas correctas. Mi próximo paso es ensayar la dinámica». ¿Qué parte de las cuatro falta?", "El efecto en el grupo", "No dice cómo influyó su trabajo en el grupo."),
        arith("En un grupo de 4 personas, cada una da una sugerencia a cada compañera. ¿Cuántas sugerencias se dan en total?", "4*3", "Cada persona da sugerencias a las otras tres.", " sugerencias"),
    ],
    [ex("Tu grupo graba una toma de ensayo y una compañera dice: «Se oyó que dos voces entraron juntas y la tercera se retrasó». ¿Qué falta para que sea retroalimentación completa: una sugerencia concreta o el nombre de la persona que se retrasó?", "Una sugerencia concreta", "Ya describe lo que se oyó; falta proponer un cambio.")],
    [ex("¿Cuál es la fórmula de la retroalimentación de la clase?", "Se oye…; sugiero…", "Describe y propone."), ex("¿Cuántas sugerencias se prueban a la vez?", "Una", "Así se ve cuál sirvió."), ex("¿Qué parte de la reflexión dice qué haré después?", "El próximo paso", "Es la cuarta parte.")],
    (
        "Lee esta toma de ejemplo de un grupo: «Se cantaron 20 notas, 16 correctas; la voz 2 entró en el compás 6 y debía entrar en el 5; el volumen se mantuvo parejo». 1) Escribe tres comentarios de retroalimentación con la fórmula «Se oye…; sugiero…», uno sobre las notas, otro sobre las entradas y uno sobre algo que salió bien. 2) Escribe una reflexión de cuatro partes sobre cómo tu trabajo en este grupo influyó en el resultado. 3) Si un comentario fuera ofensivo, escribe qué harías.",
        "Notas: «Se oyeron 16 de 20 notas correctas; sugiero ensayar despacio las cuatro que fallaron». Entradas: «Se oyó la voz 2 entrar en el compás 6; sugiero contar un compás en silencio». Lo que salió bien: «Se oyó un volumen parejo; sugiero mantenerlo». Reflexión: hice, evidencia, efecto en el grupo, próximo paso. Si fuera ofensivo: no respondo y aviso a una persona adulta de confianza.",
        ["usa la fórmula Se oye…; sugiero…", "habla de la música y no de la persona", "incluye las cuatro partes de la reflexión"],
        ["tres comentarios", "reflexión de cuatro partes", "acción ante un comentario ofensivo"],
        ["juzgar a la persona", "omitir el próximo paso en la reflexión"],
        "Reconoce los comentarios y pide revisar cuál de ellos entrega un dato y cuál una sugerencia.",
    ),
    "Escribe un comentario con la fórmula Se oye…; sugiero… sobre algo que hayas cantado o tocado.",
    "Escribe una reflexión de cuatro partes sobre un trabajo musical tuyo de esta unidad.",
)
