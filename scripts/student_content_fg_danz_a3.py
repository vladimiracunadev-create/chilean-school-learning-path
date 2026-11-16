"""Danza 3.º y 4.º medio FG: OAC-03 (creación individual y colectiva de danza), clases 1 a 5. Fichas inventadas; sin video real."""
from __future__ import annotations

from fg_danz_common import build

O3 = "FG-DANZ-3y4-OAC-03"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (elección de tema de ejemplo, inventada). Un grupo de 4 propone temas y los puntúa de 1 (bajo) a 3 (alto) en tres criterios: interés del grupo, posibilidad de traducirlo a movimiento y seguridad para ensayar en sala. "
     "Tema «el mar»: 3, 3, 3. Tema «un partido de fútbol»: 3, 2, 1 (hay riesgo de choques). Tema «la lluvia en el barrio»: 2, 3, 3. Tema «una pelea»: 1, 2, 1.")
build(
    O3, 1, F,
    use="Aprenderé a elegir un tema de interés para una creación individual o colectiva con criterios claros y a juntar un banco de movimientos propios para empezar a componer.",
    prior=["Sé pasar una idea a movimiento por abstracción.", "Sé componer una frase breve.", "Sé trabajar en grupo con respeto."],
    explain=[
        "Crear una obra de danza parte de una decisión: ¿de qué trata? Un tema de interés es un asunto que motiva a quien crea. Para elegirlo en grupo conviene usar criterios y no solo preferencias: cuánto interesa al grupo, si se puede traducir a movimiento con espacio, tiempo y energía y si se puede ensayar con seguridad. Cada criterio se puntúa y se suman los puntos; si hay empate, el grupo conversa y decide.",
        "Un banco de movimientos es una lista que reúne movimientos propuestos por cada integrante, descritos con apoyo, nivel, dirección, velocidad y energía. Sirve para no empezar de cero: después se seleccionan, se combinan y se transforman. En una creación individual el banco es de una persona; en una colectiva cada integrante aporta y el grupo decide con acuerdos claros.",
        "Los temas elegidos deben ser seguros y respetuosos: sin exponer vivencias privadas, sin burlarse de personas o grupos y sin movimientos con riesgo de golpes. Un tema como «una pelea» puede representarse con metáforas sin contacto, pero si genera incomodidad en alguien del grupo, se cambia y se avisa a una persona adulta.",
    ],
    vocab=[("tema de interés", "asunto que motiva a quien crea"), ("criterio", "regla para comparar y decidir"), ("banco de movimientos", "lista de movimientos propuestos para componer"), ("creación colectiva", "obra hecha entre varias personas con acuerdos"), ("acuerdo", "decisión compartida del grupo")],
    worked=[
        ("Sumar criterios", "En la ficha, ¿cuántos puntos suma «la lluvia en el barrio»?", ["Sus puntajes son 2, 3 y 3.", "2 + 3 + 3 = 8."], "8 puntos"),
        ("Decidir con criterios", "Un grupo debe escoger entre «el mar» (9 puntos) y «la lluvia en el barrio» (8 puntos), pero prefiere la lluvia. ¿Qué hace?", ["Los criterios dan ventaja al mar, pero el grupo puede conversar.", "Si decide la lluvia, debe explicar qué razón pesó más que los puntos."], "Conversa y explica la razón si se aparta de los puntos"),
    ],
    mistakes=[("Elegir el tema solo porque lo propuso la persona más popular.", "No se usaron criterios y se pueden perder ideas del grupo.", "Puntúa los temas con criterios y conversa el resultado."),
              ("Elegir un tema con riesgo de golpes porque «se vería más real».", "La seguridad va primero y existen metáforas sin contacto.", "Representa la idea con distancia, tiempo y energía, sin contacto.")],
    T=[
        ('abc', '¿Qué es un tema de interés?', 'Un asunto que motiva a quien crea', 'La lista de movimientos que se ensayarán', 'El nombre de la sala de ensayo del colegio', 'El tema es de qué trata la obra; la lista de movimientos es el banco.'),
        ('abc', '{F} ¿Cuántos criterios se usan en la ficha para puntuar?', 'Tres: interés, traducción a movimiento y seguridad', 'Dos: interés y traducción a movimiento, porque la seguridad no se puntúa', 'Cuatro: los tres criterios y además el número de integrantes', 'La ficha nombra tres criterios; seguridad también se puntúa.'),
        ('=', '{F} ¿Cuántos puntos suma el tema «el mar»?', '3+3+3', 'Se suman los puntajes 3, 3 y 3 del tema.', ' puntos'),
        ('abc', '{F} ¿Por qué «un partido de fútbol» tiene 1 en seguridad?', 'Porque hay riesgo de choques al ensayar en sala', 'Porque a nadie le interesa el fútbol y por eso la seguridad baja', 'Porque el fútbol no tiene movimientos para explorar con el cuerpo', 'En la ficha el 1 está justificado por el riesgo de choques.'),
        ('abc', 'Un banco de movimientos sirve para', 'reunir propuestas y seleccionar, combinar y transformar', 'sustituir el ensayo de la obra', 'decidir a qué hora se presenta la obra, ya que ordena el calendario', 'Es material de partida para componer.'),
        ('abc', '{F} Si dos temas empatan en puntos, ¿qué corresponde?', 'Conversar y decidir con una razón compartida', 'Elegir siempre el de la persona que habla más fuerte', 'Anular la votación y no elegir ningún tema', 'El empate se resuelve conversando con razones.'),
        ('=', '{F} ¿Cuántos puntos menos que «el mar» suma «la lluvia en el barrio»?', '(3+3+3)-(2+3+3)', 'Se restan las sumas de ambos temas.', ' punto'),
        ('abc', '{F} Un integrante quiere el tema «una pelea» porque «es lo más real». ¿Qué respuesta es más razonable?', 'Que el tema puntúa bajo en interés y seguridad, y que la idea se puede tratar sin contacto o elegir otro', 'Que lo tomen porque el realismo es lo más importante en danza y así la obra será más creíble', 'Que lo haga solo como creación individual y que los demás lo miren desde afuera', 'La ficha lo puntúa bajo y la seguridad es prioridad.'),
        ('abc', 'Tres integrantes proponen 4 movimientos cada uno para el banco, pero 2 se repiten. ¿Qué hace el grupo?', 'Los deja una vez y trabaja con los diferentes', 'Los repite todos igual', 'Elimina todos los movimientos que se repitieron', 'Un banco útil evita duplicados innecesarios.'),
        ('abc', 'Alguien propone un tema que alude a una vivencia privada de una compañera, sin que ella lo sepa. ¿Qué corresponde?', 'No usarlo y conversar con la compañera si ella desea compartirlo, o elegir otro tema', 'Usarlo porque es un buen tema y la obra tendría mucha verdad', 'Usarlo sin mencionarla, porque así no se expone a la compañera ante el curso', 'No se debe exponer una vivencia privada sin consentimiento.'),
        ('abc', 'Dos temas seguros tienen 8 y 7 puntos. El grupo prefiere el de 7 porque a todas las personas les da una idea de obra que las entusiasma. ¿Qué decisión es fundada?', 'Elegir el de 7 explicando que la motivación del grupo pesa más que un punto de diferencia', 'Elegir el de 8 porque la suma siempre manda y las razones del grupo no cuentan', 'Sortear sin hablar para que nadie se sienta responsable de la decisión', 'La suma orienta pero se puede decidir con razones explícitas.'),
        ('=', 'Un grupo de 5 integrantes aporta 4 movimientos cada uno al banco, pero 6 resultan repetidos y se descartan. ¿Cuántos movimientos distintos quedan?', '5*4-6', 'Se calculan los movimientos aportados y se restan los repetidos.', ' movimientos'),
        ('abc', 'Una creación individual y una colectiva se diferencian en', 'cómo se toman las decisiones y cómo se reparte el trabajo', 'en que la colectiva no necesita ensayo', 'en que la individual siempre es más corta, porque se hace con menos tiempo', 'La diferencia está en quién decide y en los acuerdos.'),
    ],
    ctx=('abc', 'Un grupo de 4 quiere elegir entre «el mar» (9 puntos) y «la lluvia en el barrio» (8 puntos). Dos integrantes sienten que el mar ya fue muy usado en el curso. ¿Qué decisión es mejor argumentada?', 'Conversar si la originalidad pesa más que un punto y decidir con esa razón dicha en voz alta', 'Elegir el mar sin hablar más, porque tiene la mayor cantidad de puntos', 'Elegir la lluvia porque a dos personas del grupo les gusta más que el mar', 'Se usan los criterios y se explicita otra razón para decidir.'),
    sc=[
        ("En Danza: ¿qué es un banco de movimientos?", "Una lista de movimientos propuestos para componer", "Reúne material para seleccionar y combinar."),
        ("¿Qué criterios se usaron para puntuar temas?", "Interés, traducción a movimiento y seguridad", "Son los tres criterios de la ficha."),
        ("¿Qué se hace con un tema que expone la vivencia privada de alguien?", "No se usa sin su consentimiento", "La privacidad de las demás personas se respeta siempre."),
    ],
    op=("Propón tres temas ficticios o neutros para una creación colectiva y puntúalos de 1 a 3 en interés, traducción a movimiento y seguridad. Suma los puntos y elige uno. Escribe tres movimientos que pondrías en el banco, con nivel y energía.",
        "Temas: el mar (3,3,3 = 9), el recreo (3,2,2 = 7), la biblioteca (2,2,3 = 7). Elijo el mar. Movimientos: ondular los brazos en nivel medio, energía suave; agacharse con rodillas flexionadas y subir lento; caminar de lado en curva.",
        ["puntúa los tres temas", "suma bien los puntos", "describe tres movimientos con nivel y energía"],
        ["hoja con tabla de puntajes y movimientos"],
        ["elegir un tema con riesgo", "no describir los movimientos", "sumar mal"],
        "Pregunta: «¿qué criterio pesó para elegir?». Si no lo dice, pídele que lo indique."),
    reinforce="Anota tres ideas de tema y puntúalas con los tres criterios de la clase. Suma y decide cuál ensayarías.",
    extend="Explica qué harías si el tema con más puntos incomoda a una persona del grupo.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (recursos de composición grupal, ejemplo inventado). Frase base de 8 tiempos. Grupo de 4 personas (P1 a P4). "
     "Unísono: las 4 personas hacen la frase al mismo tiempo. "
     "Canon (una persona empieza y otras entran después con la misma frase): P1 empieza en el tiempo 1, P2 en el 3, P3 en el 5 y P4 en el 7. "
     "Formaciones: línea (una al lado de otra), círculo y diagonal. Todo sin contacto, con 1 metro de distancia.")
build(
    O3, 2, F,
    use="Aprenderé a usar recursos de composición grupal (unísono, canon, contraste solo-grupo y formaciones) y a calcular y describir cómo se organizan las personas en el espacio y en el tiempo.",
    prior=["Sé hacer repetición, variación y contraste.", "Sé mantener la distancia y no tocarme.", "Sé contar conteos de 8 tiempos."],
    explain=[
        "En una creación colectiva se decide cómo se relacionan las personas entre sí. El unísono es cuando todas hacen el mismo movimiento al mismo tiempo. El canon es cuando una persona empieza una frase y las demás la repiten entrando una después de otra, con un intervalo fijo. El contraste solo-grupo alterna una persona que se mueve con el resto en quietud, o al revés.",
        "La formación es la disposición de las personas en el espacio: línea, círculo, diagonal, grupos separados. Cambiar de formación entre conteos crea variación sin cambiar la frase. En un canon con 4 personas que entran cada 2 tiempos y hacen una frase de 8 tiempos, la última persona entra en el tiempo 7 y termina en el tiempo 14; el canon completo dura 8 + 3 × 2 = 14 tiempos.",
        "Para ensayar con seguridad se mantiene una distancia de al menos un metro, se acuerdan las trayectorias antes de moverse y se evitan giros rápidos y cambios de lugar apresurados. Todos los roles son de igual valor: quien dirige propone y el grupo decide.",
    ],
    vocab=[("unísono", "todas las personas hacen lo mismo al mismo tiempo"), ("canon", "la misma frase entra una persona después de otra"), ("intervalo", "tiempo que separa una entrada de otra"), ("formación", "disposición de las personas en el espacio"), ("solo-grupo", "contraste entre una persona y el resto")],
    worked=[
        ("Calcular una entrada en canon", "En la ficha, ¿en qué tiempo entra P3?", ["P1 entra en el 1 y cada entrada suma 2 tiempos.", "P3 es la tercera: 1 + 2 + 2 = 5."], "En el tiempo 5"),
        ("Duración de un canon", "¿Cuánto dura el canon completo de la ficha?", ["P4 entra en el tiempo 7 y su frase dura 8 tiempos: termina en 7 + 8 − 1 = 14.", "Equivale a 8 + 3 × 2 = 14 tiempos."], "14 tiempos"),
    ],
    mistakes=[("Llamar canon a cualquier frase en la que todos empiezan juntos.", "Si todos empiezan a la vez es unísono.", "Es canon solo si las entradas son escalonadas con un intervalo."),
              ("Cambiar de lugar en la formación corriendo y sin acordar el camino.", "Aumenta el riesgo de choques.", "Acuerda las trayectorias y pásalas despacio con distancia.")],
    T=[
        ('abc', '¿Qué es el unísono?', 'Todas las personas hacen el mismo movimiento al mismo tiempo', 'Una persona hace un movimiento mientras las otras hacen otros distintos', 'Cada persona entra en un momento distinto con la frase', 'En unísono hay simultaneidad; en canon hay entradas escalonadas.'),
        ('=', '{F} ¿Cuántos tiempos pasan entre la entrada de P1 y la de P4?', '7-1', 'P1 entra en el tiempo 1 y P4 en el 7, así que se restan esos tiempos.', ' tiempos'),
        ('=', '{F} ¿En qué tiempo entra P2 si P1 entra en el 1 y cada entrada suma 2?', '1+2', 'Se suma el intervalo de 2 tiempos al tiempo de entrada de P1.', ''),
        ('=', '{F} ¿En qué tiempo termina la frase de P4?', '7+8-1', 'P4 entra en el 7 y su frase dura 8 tiempos, por lo que termina 7 tiempos después de empezar.', ''),
        ('abc', '{F} ¿Qué diferencia hay entre unísono y canon?', 'En el canon las entradas son escalonadas', 'En el canon se usa música y en el unísono no, ya que son recursos que se distinguen por el sonido', 'En el canon se cambia la frase en cada persona', 'Se distinguen por el momento de entrada.'),
        ('abc', 'Una formación es', 'la disposición de las personas en el espacio', 'el orden de los conteos de 8 tiempos', 'la lista de personas del grupo, ya que cada formación se escribe con las personas en orden', 'Línea, círculo o diagonal son formaciones.'),
        ('abc', '{F} Quieres un contraste solo-grupo. ¿Cuál propuesta lo es?', 'P1 se mueve mientras P2, P3 y P4 se quedan quietas', 'P1 a P4 se mueven igual y al mismo tiempo, todas con la misma frase', 'P1 a P4 entran una tras otra, con dos tiempos de diferencia entre cada una', 'El contraste solo-grupo es una persona en movimiento frente a las demás en quietud.'),
        ('=', '{F} Un canon similar tiene 5 personas, entradas cada 2 tiempos y frase de 8 tiempos. ¿Cuántos tiempos dura todo?', '8+4*2', 'Se suman los 8 tiempos de la frase y los 4 intervalos hasta la última entrada.', ' tiempos'),
        ('abc', '{F} Durante el canon, P3 y P4 quedan a menos de 1 metro de distancia. ¿Qué corresponde?', 'Detener, reacomodar con distancia y repetir despacio', 'Seguir porque falta poco y así se mantiene el ritmo del canon', 'Pedir que ensayen más rápido para que no se noten las dudas', 'La distancia es una regla de seguridad.'),
        ('abc', 'Un grupo quiere pasar de línea a círculo sin chocar. ¿Qué plan es seguro?', 'Acordar el camino de cada persona y hacerlo despacio con distancia', 'Cada persona se mueve libre y rápido hacia su lugar', 'Tomarse de las manos y girar de golpe hasta quedar en círculo', 'Se acuerdan las trayectorias antes del movimiento.'),
        ('abc', 'Un canon con 4 personas y frase de 8 tiempos, con entrada cada 3 tiempos, ¿cuándo entra P4?', 'En el tiempo 10', 'En el tiempo 7', 'En el tiempo 12', 'Entradas en 1, 4, 7 y 10; P4 entra en el 10.'),
        ('abc', 'Dos estudiantes discuten quién dirige la formación. ¿Qué solución respeta el trabajo colectivo?', 'Quien dirige propone y el grupo decide con acuerdos', 'La persona que dirige impone la formación', 'No hay formación, cada uno se ubica donde quiera', 'En una creación colectiva se decide con acuerdos.'),
        ('=', 'Un canon de 4 personas con entradas cada 2 tiempos se repite 2 veces seguidas, sin pausa entre repeticiones. ¿Cuántos tiempos dura en total?', '2*(8+3*2)', 'Cada canon dura 14 tiempos y se hace dos veces.', ' tiempos'),
    ],
    ctx=('abc', 'Un grupo de 6 quiere un inicio con un solo bailarín, luego un canon con entradas cada 2 tiempos y un final en unísono. ¿Qué orden respeta esa idea?', 'Solo, canon con entradas escalonadas, unísono final', 'Unísono, canon y después solo, con el cierre de una sola persona', 'Canon, solo, canon, aunque la idea pedía empezar con una sola persona', 'Solo, canon y unísono es el orden pedido.'),
    sc=[
        ("En Danza: ¿qué es un canon?", "La misma frase con entradas escalonadas", "Una persona entra después de otra."),
        ("¿Qué distancia se mantiene al ensayar en grupo?", "Al menos un metro", "Esa distancia evita choques y contacto innecesario."),
        ("¿Qué es una formación?", "La disposición de las personas en el espacio", "Línea, círculo o diagonal son ejemplos de formaciones."),
    ],
    op=("Para una frase de 8 tiempos y un grupo de 3 personas, diseña un canon con entradas cada 2 tiempos. Indica en qué tiempo entra cada persona, cuántos tiempos dura todo y qué formación usarás.",
        "Entradas: P1 en 1, P2 en 3, P3 en 5. Termina P3 en 5 + 8 − 1 = 12. Dura 12 tiempos. Formación: diagonal, con un metro entre personas.",
        ["indica las entradas correctas", "calcula la duración", "describe una formación segura"],
        ["hoja con entradas, duración y formación"],
        ["confundir canon con unísono", "calcular mal la duración", "formación sin distancia"],
        "Pregunta: «¿en qué tiempo entra la tercera?». Si dice 4, pídele repasar el intervalo."),
    reinforce="Inventa una frase de 8 tiempos y escribe en qué tiempo entraría cada integrante de un trío en canon con intervalo de 2.",
    extend="Explica cómo cambia el efecto de una frase si se pasa de unísono a canon.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (obra de ejemplo de 3 minutos, inventada). Sección 1 «llegada»: 40 segundos. Sección 2 «encuentro»: 70 segundos. "
     "Sección 3 «tensión»: 50 segundos. Sección 4 «calma» (final): lo que falta para completar los 3 minutos. "
     "Entre sección y sección hay una transición (cambio de formación o de energía) que forma parte de cada sección.")
build(
    O3, 3, F,
    use="Aprenderé a dar estructura a una obra de danza con inicio, desarrollo y final, a planificar sus secciones y transiciones, y a calcular la duración total.",
    prior=["Sé usar unísono, canon y formaciones.", "Sé componer frases con repetición y cierre.", "Sé contar tiempos y convertirlos a segundos."],
    explain=[
        "Una obra de danza se organiza en secciones, cada una con una intención y decisiones propias de espacio, tiempo y energía. La estructura más simple tiene inicio (presenta la idea), desarrollo (la transforma con variaciones y contrastes) y final (la cierra). Una transición es el cambio entre secciones: puede ser una pausa, un cambio de formación o de energía. Si la transición es clara, el público entiende que algo cambia.",
        "Planificar la duración ayuda a ensayar y a no pasarse del tiempo disponible. Se anota cuánto dura cada sección y se suma. Si la obra debe durar 3 minutos, que son 180 segundos, y las tres primeras secciones suman 40 + 70 + 50 = 160 segundos, el final dura 180 − 160 = 20 segundos. Las duraciones pueden ajustarse después de ensayar, pero siempre con un plan.",
        "Se ensaya por secciones antes de unirlas, con calentamiento previo y pausas para tomar agua. Si una sección tiene movimiento rápido o cambios de lugar, se ensaya primero lento. Si alguien siente dolor o mareo, se detiene el ensayo y se avisa a una persona adulta.",
    ],
    vocab=[("sección", "parte de la obra con una intención propia"), ("inicio", "parte que presenta la idea"), ("desarrollo", "parte que transforma la idea"), ("final", "parte que cierra la obra"), ("transición", "cambio entre dos secciones")],
    worked=[
        ("Sumar secciones", "En la ficha, ¿cuánto suman las secciones 1, 2 y 3?", ["40 + 70 + 50.", "El resultado es 160 segundos."], "160 segundos"),
        ("Duración del final", "Si la obra dura 3 minutos, ¿cuánto dura la sección 4?", ["3 minutos son 180 segundos.", "180 − 160 = 20 segundos."], "20 segundos"),
    ],
    mistakes=[("Hacer todas las secciones con la misma energía y la misma formación.", "Sin cambios no se percibe estructura.", "Cambia energía, formación o velocidad entre secciones y marca la transición."),
              ("Pasar de una sección a otra sin ninguna señal.", "El público no sabe que algo cambia.", "Usa una pausa o un cambio claro de formación o energía.")],
    T=[
        ('abc', '¿Qué es una transición?', 'El cambio entre dos secciones de la obra', 'La primera sección de la obra, que presenta la idea', 'El nombre de la obra', 'La transición une secciones y marca un cambio.'),
        ('abc', '{F} ¿Cuántas transiciones hay entre las secciones de la obra?', '3', '4', '2', 'Con cuatro secciones hay una transición entre la 1 y la 2, otra entre la 2 y la 3 y otra entre la 3 y la 4.'),
        ('abc', '{F} ¿Qué sección es el final?', 'La sección 4, «calma»', 'La sección 1, «llegada»', 'La sección 3, «tensión», porque es la de mayor energía', 'El final cierra la obra y está al final.'),
        ('=', '{F} ¿Cuántos segundos suman las secciones 1 y 2?', '40+70', 'Se suman 40 y 70 segundos.', ' segundos'),
        ('abc', '{F} La obra dura 3 minutos. ¿Cuántos segundos son?', '180 segundos', '300 segundos', '90 segundos', 'Cada minuto tiene 60 segundos y 3 × 60 = 180.'),
        ('abc', 'Una sección de «desarrollo» sirve para', 'transformar la idea con variaciones y contrastes', 'repetir la presentación sin cambiar nada', 'avisar que la obra terminó, porque el desarrollo es la parte que cierra', 'El desarrollo trabaja la idea inicial.'),
        ('=', '{F} ¿Cuántos segundos dura el final?', '3*60-(40+70+50)', 'Se convierten 3 minutos a segundos y se restan las tres primeras secciones.', ' segundos'),
        ('abc', '{F} Entre «encuentro» y «tensión» quieres una transición clara. ¿Cuál sirve?', 'Una pausa de 2 tiempos y un cambio de energía suave a cortada', 'Seguir exactamente igual', 'Aumentar el volumen de la música, ya que una transición se hace con el sonido', 'Un cambio perceptible marca la sección.'),
        ('abc', 'Al unir dos secciones, el grupo nota que se pasaron 15 segundos del tiempo disponible. ¿Qué decisión es adecuada?', 'Ajustar la duración de alguna sección o recortar repeticiones', 'Seguir adelante y acelerar al final, porque no se puede cambiar el plan', 'Eliminar la sección del final', 'Se revisa el plan para ajustar duración.'),
        ('abc', 'Una sección con cambios rápidos de lugar debe ensayarse', 'primero lento y con distancia', 'directo a la velocidad final', 'solo el día de la presentación, porque se ensaya en el escenario', 'Ensayar lento permite acordar caminos y evita choques entre personas.'),
        ('abc', 'Una obra de 4 minutos tiene cuatro secciones; las tres primeras duran 60, 90 y 70 segundos. ¿Cuánto debe durar la última?', '20 segundos', '30 segundos', '40 segundos', 'Son 240 segundos totales y 60 + 90 + 70 = 220.'),
        ('=', 'Una obra de 5 minutos tiene 4 secciones iguales y 12 segundos de cierre fuera de ellas. ¿Cuánto dura cada sección?', '(5*60-12)//4', 'Se convierte a segundos, se resta el cierre y se reparte entre cuatro.', ' segundos'),
        ('abc', 'Un grupo cambia de formación entre dos secciones para marcar la transición. ¿Qué cuidado de seguridad corresponde?', 'Acordar el camino y la distancia de cada persona antes de ensayar', 'Hacerlo rápido para que no se note el cambio y nadie tenga que esperar', 'Pedir que alguien dirija el cambio tomando de la mano a las demás personas', 'Los cambios de formación se acuerdan y ensayan lento.'),
    ],
    ctx=('abc', 'Un grupo tiene 4 secciones: 45, 60, 50 y x segundos, y debe sumar 3 minutos. Si el grupo quisiera que x fuera 40 segundos, ¿qué debe hacer?', 'Recortar 15 segundos de las otras secciones, porque 155 + 40 = 195 y pasa de 180', 'Nada, porque 155 + 40 es menos de 180', 'Agregar 15 segundos a las otras secciones, porque 155 + 40 es menos de 180', '45 + 60 + 50 = 155; con x = 40 serían 195 segundos, 15 más que los 180 de 3 minutos.'),
    sc=[
        ("En Danza: ¿qué es una sección?", "Una parte de la obra con una intención propia", "Cada sección organiza la estructura con una intención distinta."),
        ("En Danza: ¿Cuántos segundos tiene un minuto?", "60", "Sirve para convertir minutos a segundos."),
        ("¿Cómo se ensaya un cambio rápido de lugar?", "Primero lento y con distancia", "La seguridad va antes que la velocidad."),
    ],
    op=("Planifica una obra de 2 minutos con inicio, desarrollo (2 secciones) y final. Escribe qué hace cada sección, cuánto dura y cómo marcas las transiciones. Comprueba que suman 120 segundos.",
        "Inicio 20 s: entrada en línea. Desarrollo 1 40 s: canon. Desarrollo 2 40 s: formación en círculo, energía cortada. Final 20 s: pausa y cierre. 20 + 40 + 40 + 20 = 120. Transiciones: pausa de 2 tiempos y cambio de formación.",
        ["secciones con intención", "duraciones que suman 120", "transiciones claras"],
        ["hoja con plan de secciones"],
        ["no sumar bien", "no marcar transiciones"],
        "Pregunta: «¿cómo sabe el público que cambió la sección?». Si no responde, pídele marcar una transición."),
    reinforce="Escribe una obra imaginaria de 90 segundos con 3 secciones y comprueba la suma.",
    extend="Explica qué pasa con la estructura si todas las secciones tienen igual energía y no hay transición.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (puesta en escena de ejemplo, inventada). Sala de 6 metros de ancho y 4 metros de fondo. Grupo de 8 intérpretes; cada persona necesita 2 metros cuadrados para moverse sin chocar. "
     "Elementos: vestuario simple (ropa cómoda de un solo color), luz de sala con dos niveles (encendida y baja), música creada por el grupo (original, sin derechos de terceros), utilería liviana (una tela liviana y suave).")
build(
    O3, 4, F,
    use="Aprenderé a pensar la puesta en escena de mi obra: espacio escénico, vestuario, luz, sonido y utilería, y a elegir sus elementos con seguridad y coherencia con la idea.",
    prior=["Sé estructurar una obra en secciones.", "Sé usar formaciones.", "Sé que los derechos de autor protegen las obras."],
    explain=[
        "La puesta en escena es el conjunto de decisiones que rodean al movimiento: el espacio escénico (dónde se presenta y cómo se ubica el público), el vestuario, la iluminación, el sonido o música y la utilería (objetos que se usan). Se eligen para apoyar la idea de la obra y no para decorar. Por ejemplo, un vestuario de un solo color puede ayudar a que se vea el movimiento y no la ropa.",
        "El espacio escénico tiene frente (donde mira el público), fondo, lados y entradas. Se calcula cuánto espacio necesita cada persona: en una sala de 6 × 4 metros hay 24 metros cuadrados. Si cada persona necesita 2 metros cuadrados, caben 12, así que 8 personas caben con holgura. La música debe ser creada por el grupo o usarse con autorización; no se copian obras sin permiso.",
        "La seguridad en la puesta en escena incluye piso despejado, sin cables sueltos, utilería liviana y sin bordes, vestuario que no se pise ni enrede, y nada de fuego ni vidrio. Si la luz es oscura, se mantiene visible el camino de entradas y salidas. Ante cualquier riesgo se detiene el ensayo y se avisa a una persona adulta.",
    ],
    vocab=[("puesta en escena", "decisiones de espacio, vestuario, luz, sonido y utilería"), ("espacio escénico", "lugar donde se presenta la obra"), ("vestuario", "ropa que usan las y los intérpretes"), ("utilería", "objetos que se usan en la obra"), ("derechos de autor", "protección de una obra creada por alguien")],
    worked=[
        ("Calcular el área", "¿Cuántos metros cuadrados tiene la sala de la ficha?", ["Se multiplica ancho por fondo.", "6 × 4 = 24."], "24 metros cuadrados"),
        ("Revisar si caben", "¿Caben los 8 intérpretes con 2 metros cuadrados cada uno?", ["Se necesitan 8 × 2 = 16 metros cuadrados.", "Hay 24, así que caben."], "Sí, porque 16 es menor que 24"),
    ],
    mistakes=[("Usar la canción de un artista sin permiso porque «está en internet».", "La obra tiene derechos de autor.", "Usa música creada por el grupo o con autorización."),
              ("Llenar el escenario de objetos para que se vea más «teatral».", "Los objetos pueden estorbar el movimiento y generar riesgos.", "Elige solo los elementos que apoyan la idea.")],
    T=[
        ('abc', '¿Qué es la puesta en escena?', 'Las decisiones de espacio, vestuario, luz, sonido y utilería que rodean la obra', 'Solo el vestuario que se usa en la presentación', 'La lista de movimientos de la obra y el orden en que se ensayan', 'Es el conjunto de decisiones, no solo una de ellas.'),
        ('=', '{F} ¿Cuántos metros cuadrados tiene la sala?', '6*4', 'El área de un rectángulo es ancho por fondo.', ' metros cuadrados'),
        ('=', '{F} ¿Cuántos metros cuadrados necesitan los 8 intérpretes en total?', '8*2', 'Se multiplica el número de personas por el espacio que cada una necesita.', ' metros cuadrados'),
        ('abc', '{F} ¿Caben los 8 intérpretes en la sala?', 'Sí, porque necesitan 16 y hay 24', 'No, porque la sala tiene solo 16', 'Solo caben si se quitan las luces, porque la luz ocupa espacio', 'La sala tiene más metros cuadrados que los necesarios.'),
        ('abc', '{F} ¿Por qué es mejor un vestuario de un solo color?', 'Porque ayuda a que se vea el movimiento y no la ropa', 'Porque es obligatorio en danza', 'Porque oculta los errores de la coreografía y se nota menos quién se equivoca', 'La elección del vestuario apoya la idea y no distrae del movimiento.'),
        ('abc', 'Un grupo quiere usar una canción conocida sin permiso. ¿Qué corresponde?', 'Usar música propia o con autorización', 'Usarla porque es para fines escolares, y todo es de libre uso', 'Cortar un fragmento breve', 'Las obras tienen derechos de autor.'),
        ('abc', '{F} ¿Qué cuidado corresponde con la tela suave de utilería?', 'Que sea liviana, sin bordes duros ni nudos, y que no se pise ni se enrede', 'Que sea larga para que se arrastre por el piso y se vea el movimiento', 'Que se ate a la cintura de otra persona para moverse en pareja', 'La utilería no debe generar riesgos.'),
        ('=', '{F} ¿Cuántas personas más podrían entrar en la sala con 2 metros cuadrados cada una?', '24//2-8', 'Se calcula cuántas personas caben en total y se restan las 8 del grupo.', ' personas'),
        ('abc', 'La luz de la escena baja y el piso queda poco visible. ¿Qué corresponde?', 'Marcar con claridad el camino de entradas y salidas y ensayar con esa luz', 'Ensayar a oscuras sin marcar nada, para acostumbrarse al piso', 'Pedir al público que mire de lejos para que no se note la poca luz', 'Se asegura la visibilidad del camino.'),
        ('abc', 'Un intérprete propone usar velas para dar ambiente. ¿Qué respuesta es adecuada?', 'No, porque el fuego es riesgoso; se puede usar luz baja de sala', 'Sí, si están cerca de la pared y lejos de las demás personas', 'Sí, si alguien las vigila durante toda la presentación y hay agua cerca', 'No se usa fuego en ensayos ni presentaciones escolares.'),
        ('abc', 'Dos propuestas de vestuario: ropa cómoda de un solo color, o un vestido largo que se arrastra. ¿Cuál es más segura?', 'La ropa cómoda, porque permite moverse sin tropezar', 'El vestido largo, porque se ve más elegante y llama la atención del público', 'Ninguna, porque el vestuario siempre es peligroso', 'La ropa larga que se arrastra puede enredarse.'),
        ('=', 'Un escenario de 6 metros de ancho y 4 de fondo se reparte en dos zonas iguales. ¿Cuántos metros cuadrados tiene cada zona?', '(6*4)//2', 'Se calcula el área total de 6 por 4 y se divide entre dos zonas iguales.', ' metros cuadrados'),
        ('abc', 'Quieres que el público note el contraste entre calma y tensión. ¿Qué decisión de puesta en escena ayuda?', 'Cambiar la luz de baja a encendida junto con el cambio de energía', 'Cambiar la música sin avisar al grupo para que el cambio sea sorpresivo', 'Mover al público de lugar durante la obra para cambiar el punto de vista', 'Un cambio de luz acompaña el cambio de sección.'),
    ],
    ctx=('abc', 'Un grupo de 10 intérpretes dispone de una sala de 4 × 4 metros y cada persona necesita 2 metros cuadrados. ¿Qué decisión es adecuada?', 'Dividir en dos grupos de 5 que se presentan por turnos', 'Presentarse los 10 a la vez, apretándose un poco más', 'Reducir el espacio de cada persona sin avisar', '4 × 4 = 16 metros cuadrados y 10 personas necesitan 20: no caben todas a la vez, y por turnos se evita el choque.'),
    sc=[
        ("En Danza: ¿qué es la utilería?", "Los objetos que se usan en la obra", "Forma parte de la puesta en escena."),
        ("¿Qué se debe hacer con la música de otra persona?", "Pedir autorización o usar música propia", "Las obras tienen derechos de autor."),
        ("¿Se usan velas o fuego en las presentaciones escolares?", "No", "El fuego es un riesgo innecesario en ensayos y presentaciones escolares."),
    ],
    op=("Para tu obra, describe en 5 líneas la puesta en escena: espacio y formación, vestuario, luz, sonido (propio o autorizado) y utilería. Calcula si caben las personas del grupo en el espacio disponible.",
        "Espacio: sala de 6 × 5 m, 10 intérpretes, 2 m² cada uno: 30 m² disponibles, necesito 20. Vestuario: ropa cómoda azul. Luz: sala encendida en inicio y baja en la sección de calma. Sonido: percusión corporal creada por el grupo. Utilería: ninguna.",
        ["decide los cinco elementos", "calcula el espacio", "elige sin riesgos y sin copiar obras"],
        ["hoja con descripción y cálculo"],
        ["copiar música ajena", "usar fuego o vidrio", "no calcular el espacio"],
        "Pregunta: «¿qué apoya la luz que elegiste?». Si responde «se ve bonito», pídele la idea de la obra."),
    reinforce="Describe tres elementos de puesta en escena para una obra sobre la lluvia, con seguridad y sin copiar obras.",
    extend="Explica por qué una puesta en escena sencilla puede comunicar mejor que una recargada.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (proyecto colectivo de ejemplo, inventado). Grupo de 5: Ana, Bruno, Carla, Diego y Elena. Roles: dirección del ensayo, registro de acuerdos, música, vestuario y puesta en escena. "
     "Plan: 5 ensayos de 45 minutos, uno por semana, y una muestra de 6 minutos. Acuerdos: cada persona puede decir «no quiero hacer este movimiento» y proponer otro; los cambios se deciden por mayoría después de escuchar a todos.")
build(
    O3, 5, F,
    use="Aprenderé a gestionar una creación colectiva: repartir roles, tomar acuerdos, planificar ensayos y resolver desacuerdos con respeto y consentimiento.",
    prior=["Sé elegir un tema con criterios.", "Sé estructurar una obra.", "Sé trabajar en grupo respetando el cuerpo propio y ajeno."],
    explain=[
        "Una creación colectiva funciona mejor con roles claros y acuerdos explícitos. Un rol es una responsabilidad concreta: dirigir el ensayo, anotar los acuerdos, cuidar la música, el vestuario o la puesta en escena. Los roles no jerarquizan a las personas: todas interpretan y crean, y los roles se pueden rotar. Los acuerdos se anotan para que no dependan de la memoria.",
        "El consentimiento es aceptar de manera libre una acción que involucra al cuerpo propio o al ajeno. En danza significa que nadie debe hacer un movimiento que no quiera hacer, ni ser tocado o movido por otra persona sin su permiso, y que cada persona puede proponer una alternativa. Un grupo respetuoso escucha, decide por mayoría o por consenso y no presiona a quien dice que no.",
        "Planificar ensayos ayuda a repartir el tiempo: por ejemplo, 5 ensayos de 45 minutos suman 225 minutos, o 3 horas y 45 minutos. Cada ensayo tiene calentamiento, trabajo en secciones y cierre. Cuando hay un desacuerdo se conversa con respeto, se prueban ambas propuestas y se decide. Si algo molesta o hay maltrato, se avisa a una persona adulta.",
    ],
    vocab=[("rol", "responsabilidad concreta dentro del grupo"), ("acuerdo", "decisión compartida y anotada"), ("consentimiento", "aceptación libre sobre el propio cuerpo"), ("consenso", "decisión que todas las personas aceptan"), ("mayoría", "decisión de más de la mitad del grupo")],
    worked=[
        ("Calcular el tiempo de ensayo", "En la ficha, ¿cuántos minutos suman los 5 ensayos?", ["Cada ensayo dura 45 minutos.", "5 × 45 = 225 minutos."], "225 minutos"),
        ("Aplicar el consentimiento", "Diego no quiere hacer un movimiento en el que debe apoyarse en un compañero. ¿Qué hace el grupo?", ["Respeta su decisión y propone alternativas sin contacto.", "Prueba la alternativa y la anota como acuerdo."], "Respeta su decisión y prueba una alternativa sin contacto"),
    ],
    mistakes=[("Presionar a alguien para que haga un movimiento que dijo no querer hacer.", "El consentimiento es libre y puede cambiar.", "Escucha, propone otra opción y decide en grupo."),
              ("Decidir entre dos personas y avisar al resto después.", "Los acuerdos colectivos se toman con todo el grupo.", "Anota la propuesta y decide por mayoría o consenso después de escuchar.")],
    T=[
        ('abc', '¿Qué es un rol en un grupo?', 'Una responsabilidad concreta dentro del trabajo', 'Una jerarquía en que unas personas valen más que otras', 'Un movimiento obligatorio para todas las personas', 'Es una responsabilidad; no implica que alguien valga más.'),
        ('abc', '{F} ¿Cuántos roles hay en la ficha?', '5', '4', '6', 'La ficha lista cinco roles: dirección, registro, música, vestuario y puesta en escena.'),
        ('abc', '{F} ¿Qué puede decir cualquier persona según los acuerdos?', '«No quiero hacer este movimiento» y proponer otro', 'Solo «sí» a lo que decide la dirección, para no retrasar el ensayo', 'Nada, porque en el trabajo en grupo decide siempre quien dirige', 'Los acuerdos ponen el consentimiento por delante.'),
        ('=', '{F} ¿Cuántos minutos suman los 5 ensayos?', '5*45', 'Se multiplica el número de ensayos por su duración.', ' minutos'),
        ('abc', '{F} Los cambios se deciden por mayoría. ¿Cuántos votos mínimos hacen mayoría en un grupo de 5?', '3', '2', '5', 'La mayoría es más de la mitad: más de 2,5, o sea 3.'),
        ('abc', 'El consentimiento en danza significa', 'aceptar libremente lo que involucra al propio cuerpo y poder cambiar de opinión', 'aceptar siempre lo que propone el grupo para no entorpecer el trabajo', 'aceptar un movimiento si lo piden varias veces y con buena voluntad', 'El consentimiento es libre y puede retirarse.'),
        ('abc', '{F} Carla propone un movimiento en que Elena levanta a Carla. Elena dice que no. ¿Qué corresponde?', 'Descartar el movimiento y proponer una alternativa sin cargas', 'Insistir, porque ya está decidido y el grupo no puede cambiar la obra', 'Intentarlo despacio varias veces para que Elena se acostumbre a la carga', 'Las cargas no se hacen y el no se respeta.'),
        ('=', '{F} La muestra dura 6 minutos y el grupo de 5 quiere dividirla en 3 secciones iguales. ¿Cuántos segundos dura cada sección?', '6*60//3', 'Se pasan los minutos a segundos y se reparten entre tres secciones.', ' segundos'),
        ('abc', '{F} Dos integrantes discuten sobre el orden de dos secciones. ¿Qué solución es mejor?', 'Probar ambos órdenes, escuchar al grupo y decidir por mayoría', 'Que decida siempre quien dirige, porque tiene más experiencia que las demás personas', 'Que no se ensaye nada hasta que las dos personas se pongan de acuerdo', 'Probar y decidir con acuerdos resuelve el desacuerdo.'),
        ('abc', 'Un integrante hace bromas sobre el cuerpo de otra persona durante el ensayo. ¿Qué corresponde?', 'Detener la broma, recordar los acuerdos de respeto y avisar a una persona adulta si continúa', 'Ignorarla porque es una broma y reaccionar solo empeora las cosas', 'Responder con otra broma para que se den cuenta de cómo se siente', 'El respeto al cuerpo ajeno es una regla del trabajo.'),
        ('abc', 'Un grupo rota los roles cada ensayo. ¿Qué ventaja tiene?', 'Todas las personas experimentan distintas responsabilidades', 'Nadie se responsabiliza de nada, porque todos pasan por todos los roles', 'La obra se ensaya menos porque cada rol se aprende en un solo ensayo', 'Rotar reparte la experiencia y la carga.'),
        ('=', 'Un grupo de 6 quiere ensayar 3 horas en total, repartidas en sesiones de 45 minutos. ¿Cuántas sesiones necesita?', '3*60//45', 'Se pasan las horas a minutos y se divide entre los 45 minutos de cada sesión.', ' sesiones'),
        ('abc', 'Un grupo registra en una hoja los acuerdos de cada ensayo. ¿Para qué sirve?', 'Para recordar las decisiones y evitar discusiones por malentendidos', 'Para reemplazar los ensayos cuando una parte del grupo no puede asistir', 'Para castigar a quien se equivoca o llega tarde a un ensayo', 'Un registro hace visibles las decisiones.'),
    ],
    ctx=('abc', 'Un grupo de 6 debe elegir entre dos finales. Hay 3 votos para cada uno y ninguno alcanza la mayoría de 4. ¿Qué es lo más razonable?', 'Conversar las razones, probar ambos finales y volver a votar', 'Elegir uno al azar sin hablar para evitar una discusión larga', 'Que decida quien dirige, porque en un empate le toca desempatar', 'Un empate se resuelve con conversación y nueva votación.'),
    sc=[
        ("En Danza: ¿qué es el consentimiento?", "Aceptar libremente lo que involucra al propio cuerpo", "El consentimiento puede retirarse en cualquier momento sin dar explicaciones."),
        ("¿Cuántos votos hacen mayoría en un grupo de 5?", "3", "La mayoría es más de la mitad de los votos del grupo."),
        ("¿Qué hace el grupo ante una broma sobre el cuerpo de alguien?", "La detiene y avisa a una persona adulta si sigue", "El respeto al cuerpo ajeno es una regla básica del trabajo."),
    ],
    op=("Escribe el plan de un proyecto colectivo de 4 personas (nombres inventados): 4 roles, 3 acuerdos de respeto y consentimiento, y un calendario de ensayos con minutos totales.",
        "Ana dirige, Bruno anota, Carla música, Diego espacio. Acuerdos: se puede decir no, se decide por mayoría, no hay comentarios sobre el cuerpo. Calendario: 4 ensayos de 45 minutos = 180 minutos.",
        ["roles claros", "acuerdos de consentimiento y respeto", "calcula bien el tiempo"],
        ["hoja con roles, acuerdos y calendario"],
        ["no incluir consentimiento", "calcular mal el tiempo"],
        "Pregunta: «¿qué pasa si alguien dice que no?». Si responde «lo convencemos», pídele otra respuesta."),
    reinforce="Escribe tres acuerdos de respeto para trabajar en grupo en una creación de danza.",
    extend="Explica cómo cambia el trabajo de un grupo si los roles rotan en cada ensayo.",
)
