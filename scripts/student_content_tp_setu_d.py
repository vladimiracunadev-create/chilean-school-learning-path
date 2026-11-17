"""Servicios de Turismo TP 3.º y 4.º medio: OAE-04 (conducir grupos de turistas por rutas establecidas). SOLO conceptos y avisos; todo en papel con datos de ejemplo."""
from __future__ import annotations

from tp_setu_common import build

O4 = "TP-SETU-3y4-OAE-04"

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (de ejemplo, inventada). Programa «Casco histórico de Villa Brisa»: caminata guiada urbana de 2 horas y 3.000 metros, con salida desde la plaza a las 10:00. "
     "Grupo inscrito: 12 adultos, 6 estudiantes de 14 y 15 años con 2 docentes, y 2 personas mayores. Hay un guía autorizado a cargo. "
     "Riesgos identificados por el prestador: tránsito en dos cruces, calor al mediodía y ritmo distinto entre las personas. Regla de ejemplo del prestador: máximo 12 personas por guía.")
build(
    O4, 1, F,
    use="Aprenderé qué es conducir un grupo por una ruta establecida, qué es un riesgo y su prevención, y por qué conducir grupos exige un guía autorizado y la norma vigente.",
    prior=["Sé que cada persona merece un trato respetuoso.", "Sé sumar y dividir con números enteros.", "Sé qué es un atractivo turístico."],
    explain=[
        "Conducir un grupo de turistas es acompañarlo y orientarlo por una ruta establecida, que es el recorrido definido de antemano por el prestador, con sus tramos, paradas y puntos de reunión. El programa es el conjunto de actividades, horarios y servicios del recorrido. El entorno puede ser urbano, rural o natural, y cada uno tiene sus propios riesgos. Conducir grupos corresponde a un guía autorizado, según la norma vigente.",
        "Un riesgo es la posibilidad de que algo cause daño a las personas o al ambiente. La prevención son las medidas que se toman antes para evitarlo, y el protocolo es el conjunto de pasos acordados que el prestador sigue ante una situación. El guía no improvisa cambios de ruta: si algo cambia, consulta al coordinador del prestador. Siempre se trata con respeto a cada integrante, según su edad, ritmo y necesidades.",
        "Aviso: este cuaderno es aprendizaje conceptual en papel. Conducir grupos, sobre todo en entornos naturales o en actividades de aventura, exige guía o instructor autorizado, norma vigente (por ejemplo, la entidad fiscalizadora de tu sector) y elementos de protección; este cuaderno no te habilita para trabajar.",
    ],
    vocab=[("ruta establecida", "recorrido definido de antemano por el prestador"), ("programa", "conjunto de actividades, horarios y servicios de un recorrido"), ("entorno", "tipo de lugar donde se hace el recorrido: urbano, rural o natural"), ("riesgo", "posibilidad de que algo cause daño"), ("prevención", "medidas que se toman antes para evitar un daño"), ("protocolo", "pasos acordados que se siguen ante una situación"), ("punto de reunión", "lugar acordado donde el grupo se junta")],
    worked=[
        ("Contar un grupo", "Un grupo de ejemplo tiene 8 adultos, 5 niños y 1 docente. ¿Cuántas personas son?", ["Se suman todos los integrantes.", "8 + 5 + 1 = 14."], "14 personas"),
        ("Guías necesarios", "Un prestador de ejemplo permite máximo 15 personas por guía. Viene un grupo de 30. ¿Cuántos guías se necesitan?", ["30 ÷ 15 = 2 exactos.", "Se necesitan 2 guías."], "2 guías"),
    ],
    mistakes=[("Cambiar la ruta en el camino «porque es más corta».", "La ruta fue evaluada por el prestador; otra puede tener riesgos que nadie revisó.", "Mantén la ruta establecida y consulta antes de cualquier cambio."),
              ("Dejar que un acompañante conduzca al grupo porque «conoce la zona».", "Solo un guía autorizado puede conducir, según la norma vigente.", "Agradece la ayuda y explica que la conducción corresponde al guía.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es una ruta establecida?", "El recorrido definido de antemano por el prestador, con sus tramos y paradas", "El camino que el guía elige en el momento, según le parezca", "El recorrido que prefiere el turista más rápido", "La ruta establecida se define antes, no se improvisa en el camino."),
        ("abc", "En Servicios de Turismo: ¿qué es un riesgo?", "La posibilidad de que algo cause daño a las personas o al ambiente", "Un plan para evitar que algo ocurra", "El horario de salida del programa", "El riesgo es la posibilidad de daño; el plan para evitarlo es la prevención."),
        ("abc", "En Servicios de Turismo: ¿qué es un protocolo?", "Un conjunto de pasos acordados que se siguen ante una situación", "Una lista de turistas inscritos", "El nombre de una ruta", "El protocolo ordena cómo actuar ante una situación; no es una lista ni un nombre."),
        ("abc", "{F} ¿Qué tipo de entorno tiene este programa?", "Urbano", "Natural", "Rural", "La caminata es por el casco histórico de un pueblo, es decir, un entorno urbano."),
        ("=", "{F} ¿Cuántas personas hay en el grupo inscrito?", "12+6+2+2", "Se suman adultos, estudiantes, docentes y personas mayores.", " personas"),
        ("=", "{F} Con la regla de ejemplo de máximo 12 personas por guía, ¿cuántos guías se necesitan como mínimo?", "(22+11)//12", "Se divide la cantidad de personas por 12 y se sube al entero siguiente.", " guías"),
        ("abc", "{F} Hay un solo guía autorizado. ¿Qué corresponde?", "No salir hasta contar con el guía que falta o ajustar el grupo, según la regla del prestador", "Salir igual, porque la diferencia es solo de unas pocas personas", "Pedir a un docente que haga de guía aunque no esté autorizado", "La regla fija un máximo por guía; incumplirla aumenta el riesgo."),
        ("abc", "{F} ¿Cuál es un riesgo identificado por el prestador?", "El tránsito en dos cruces", "El nombre de la plaza", "El precio de la caminata", "El tránsito en los cruces está en la ficha como riesgo; el nombre y el precio no lo son."),
        ("=", "{F} Si el recorrido de 3.000 metros durara exactamente 2 horas sin detenerse, ¿cuántos metros por minuto avanzaría el grupo en promedio?", "3000//(2*60)", "Se pasan 2 horas a minutos y se divide la distancia por ese tiempo.", " metros por minuto"),
        ("abc", "{F} En el grupo hay dos personas mayores. ¿Qué corresponde?", "Adaptar el ritmo y las pausas del grupo, preguntando a ellas qué necesitan", "Dejarlas fuera del programa por seguridad", "Mantener el ritmo más rápido para cumplir el horario", "El ritmo se adapta a las personas y se les pregunta, sin excluirlas por su edad."),
        ("abc", "{F} Se anuncia calor al mediodía. ¿Qué medida preventiva corresponde?", "Planificar pausas a la sombra y recordar hidratarse, según las indicaciones del prestador", "Acelerar para terminar antes del calor sin avisar", "Ignorarlo, porque el calor no es un riesgo", "La prevención se planifica antes e informa a las personas; ignorar un riesgo no lo elimina."),
        ("abc", "{F} Un docente propone pasar por una calle sin veredas «porque es más corta». ¿Qué corresponde?", "Mantener la ruta establecida y consultar al coordinador antes de cualquier cambio", "Cambiar la ruta, porque los docentes conocen a los estudiantes", "Decidir por votación del grupo en el momento", "Los cambios de ruta se consultan; la ruta fue evaluada por el prestador."),
        ("abc", "Un turista pide guiar al grupo porque conoce bien la zona. ¿Qué corresponde?", "Agradecerle y explicar que la conducción corresponde al guía autorizado", "Dejarlo guiar si el grupo está de acuerdo", "Entregarle la lista de pasajeros para que se organice", "La norma vigente exige un guía autorizado; el acuerdo del grupo no lo reemplaza."),
    ],
    ctx=("abc", "{F} Al llegar al primer cruce, una persona del grupo se queda atrás sacando fotos. ¿Qué principio aplica el guía?", "Mantener al grupo reunido y avanzar solo cuando todos estén presentes", "Seguir avanzando, porque cada quien es responsable de sí mismo", "Gritarle a la persona para que se apure", "Un grupo se conduce reunido; avanzar sin contar a todos deja a alguien sin acompañamiento."),
    sc=[
        ("En Servicios de Turismo: ¿qué es la prevención de riesgos?", "Medidas que se toman antes para evitar un daño", "Prevenir es actuar antes de que ocurra el daño."),
        ("¿Quién puede conducir un grupo según la norma vigente?", "Un guía autorizado", "El conocimiento de la zona no reemplaza la autorización."),
        ("¿Qué haces si quieres cambiar la ruta?", "Consulto al coordinador del prestador", "La ruta fue evaluada, por eso no se cambia sola."),
    ],
    op=("Un programa de ejemplo es una visita a una feria artesanal y un museo en el centro del pueblo, a pie, durante 2 horas. Escribe tres riesgos posibles y una medida preventiva para cada uno, usando solo ideas generales (sin procedimientos de actividades peligrosas), y una frase final recordando quién puede conducir el grupo.",
        "Riesgo 1: tránsito en cruces; medida: cruzar todos juntos por el paso habilitado. Riesgo 2: personas con ritmo distinto; medida: pausas y ritmo adaptado al más lento. Riesgo 3: calor o lluvia; medida: avisar antes y planificar pausas. Frase final: «La conducción del grupo corresponde a un guía autorizado, según la norma vigente».",
        ["escribe tres riesgos distintos", "cada riesgo tiene una medida preventiva coherente", "incluye la frase sobre el guía autorizado"],
        ["lista de tres riesgos, tres medidas y la frase final"],
        ["escribir una medida que no corresponde al riesgo", "describir un procedimiento de una actividad peligrosa", "no mencionar al guía autorizado"],
        "Pregunta: «¿qué haces si un riesgo no estaba previsto?». Si no responde, repasa el protocolo y la consulta al coordinador."),
    reinforce="Anota tres riesgos que puede haber en una caminata por tu barrio y una medida para cada uno.",
    extend="Explica con un ejemplo inventado por qué un grupo debe avanzar reunido.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (de ejemplo, inventada). Hoja de ruta del programa «Mirador de la Colina»: entorno rural, programa de 3 horas. Salida a las 9:00 desde la plaza. Tramo 1 a pie hasta el mirador, 45 minutos; pausa de 15 minutos; "
     "tramo 2 a pie hasta la feria campesina, 40 minutos; almuerzo de 60 minutos; regreso en el bus del prestador, 20 minutos. Equipo de apoyo del prestador: botiquín, teléfono con carga, chaleco reflectante y megáfono pequeño. "
     "Documentos: hoja de ruta con puntos de reunión, lista de pasajeros con nombre y contacto de emergencia (solo la ven el guía y el coordinador) y ficha del programa. Roles: guía autorizado, coordinador del prestador y conductor de una empresa de transporte autorizada.")
build(
    O4, 2, F,
    use="Aprenderé los documentos de un programa (hoja de ruta, lista de pasajeros), los roles del equipo, qué son los implementos y equipos de seguridad y la tecnología de apoyo, y cómo comunicarse con el grupo.",
    prior=["Sé qué es una ruta establecida y un riesgo.", "Sé sumar tiempos en minutos.", "Sé que los datos personales son privados."],
    explain=[
        "La hoja de ruta es el documento que describe el recorrido: tramos, horarios, paradas y puntos de reunión. La lista de pasajeros reúne los nombres y el contacto de emergencia de cada integrante; es un dato personal, por lo que solo la ven quienes la necesitan, como el guía y el coordinador, y no se comparte en chats abiertos. La ficha del programa resume qué incluye y qué condiciones tiene. El equipo se reparte en roles: el guía autorizado conduce; el coordinador del prestador apoya y decide ante cambios; el conductor pertenece a una empresa de transporte autorizada.",
        "Los implementos y equipos de seguridad son los elementos que el prestador lleva para cuidar al grupo, como un botiquín, un teléfono con carga o un chaleco reflectante. Cuáles se necesitan depende del tipo de programa y de la norma vigente; en actividades de aventura los define el prestador autorizado, y este cuaderno solo los presenta como conceptos. La tecnología de apoyo son herramientas como un mapa digital o un teléfono para avisar al coordinador; sirve, pero no reemplaza el plan ni el criterio del guía.",
        "La comunicación efectiva con un grupo usa voz clara, frases cortas, señales acordadas y repetir los puntos de reunión. En inglés, dos frases útiles son «Please stay together» (Por favor, permanezcan juntos) y «We meet here at ten» (Nos reunimos aquí a las diez).",
    ],
    vocab=[("hoja de ruta", "documento con tramos, horarios, paradas y puntos de reunión"), ("lista de pasajeros", "documento con nombres y contacto de emergencia de los integrantes"), ("coordinador", "persona del prestador que apoya al guía y decide ante cambios"), ("equipo de seguridad", "elementos que el prestador lleva para cuidar al grupo"), ("tecnología de apoyo", "herramientas digitales, como un mapa o un teléfono, que ayudan a conducir"), ("señal acordada", "gesto o sonido que el grupo conoce de antemano")],
    worked=[
        ("Hora de término", "Un programa de ejemplo sale a las 14:00, tiene un tramo de 50 minutos, una pausa de 10 y un tramo de 60. ¿A qué hora termina?", ["Total: 50 + 10 + 60 = 120 minutos, es decir, 2 horas.", "14:00 más 2 horas son las 16:00."], "A las 16:00"),
        ("Privacidad", "Un coordinador de ejemplo quiere enviar la lista de pasajeros completa a un chat abierto del grupo. ¿Qué corresponde?", ["La lista tiene datos personales y contactos de emergencia.", "Solo la ven el guía y el coordinador; no se envía a un chat abierto."], "No enviarla al chat abierto"),
    ],
    mistakes=[("Pegar la lista de pasajeros en un chat abierto «para que todos sepan quién viene».", "Se exponen nombres y contactos de personas que no autorizaron compartirlos.", "Comparte solo lo necesario y por el medio que el prestador defina."),
              ("Confiar solo en el mapa digital y no mirar el entorno.", "La tecnología puede fallar o no tener señal, y no reemplaza el criterio del guía.", "Usa la tecnología como apoyo y sigue la hoja de ruta.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es una hoja de ruta?", "El documento que describe el recorrido, con tramos, horarios y puntos de reunión", "La lista de precios del programa", "El comprobante de pago de cada turista", "La hoja de ruta ordena el recorrido; los precios y los comprobantes son otros documentos."),
        ("abc", "¿Quién ve la lista de pasajeros con los contactos de emergencia?", "Solo quienes la necesitan, como el guía y el coordinador", "Todos los turistas del grupo", "Cualquier persona en un chat abierto", "La lista contiene datos personales y debe verla solo quien la necesita."),
        ("abc", "En Servicios de Turismo: ¿qué es el equipo de seguridad de un programa?", "Los elementos que el prestador lleva para cuidar al grupo, como un botiquín", "Las entradas que se compran en la ruta", "La ropa de moda del guía", "El equipo de seguridad protege al grupo; entradas y ropa de moda no lo hacen."),
        ("=", "{F} ¿A qué hora termina el programa si dura 3 horas desde la salida a las 9:00? Escribe solo la hora, sin los minutos.", "9+3", "Se suman las 3 horas de duración a la hora de salida.", " h"),
        ("=", "{F} ¿Cuántos minutos dura el programa sumando todos los tramos, pausas y almuerzo?", "45+15+40+60+20", "Se suman los cinco tiempos de la hoja de ruta.", " minutos"),
        ("=", "{F} ¿Cuántos minutos del programa se caminan?", "45+40", "Solo los tramos 1 y 2 se hacen a pie.", " minutos"),
        ("abc", "{F} ¿Quién decide si hay que cambiar la hoja de ruta durante el programa?", "El coordinador del prestador, a consulta del guía", "El turista que más pregunta", "El conductor del bus, por su cuenta", "Los cambios se consultan al coordinador, que representa al prestador."),
        ("abc", "{F} ¿Por qué el bus del programa pertenece a una empresa de transporte autorizada?", "Porque el transporte de personas requiere cumplir la norma vigente", "Porque así es más barato", "Porque el guía no tiene licencia de conducir", "El transporte de pasajeros debe cumplir la norma vigente de seguridad."),
        ("abc", "{F} Una persona del grupo usa silla de ruedas. ¿Qué corresponde antes de la salida?", "Preguntarle qué apoyo necesita y consultar al coordinador si el recorrido es adecuado", "Suponer que no puede participar y no invitarla", "Asegurar que todo el recorrido es accesible sin revisarlo", "No se supone: se le pregunta y se verifica el recorrido con el prestador."),
        ("ab", "{F} Un turista pide al guía una foto de la lista de pasajeros «para saber quién viaja». ¿Qué corresponde?", "No entregarla, porque tiene datos personales; las personas pueden presentarse entre ellas en persona", "Entregarla, porque todos viajan en el mismo grupo", "La lista tiene nombres y contactos de emergencia, que son datos personales."),
        ("ab", "{F} ¿Cuál frase en inglés significa «Por favor, permanezcan juntos»?", "Please stay together.", "Please go away.", "Stay together significa permanecer juntos; go away significa irse."),
        ("abc", "{F} El mapa digital del guía deja de funcionar por falta de señal. ¿Qué corresponde?", "Continuar con la hoja de ruta en papel y avisar al coordinador cuando sea posible", "Improvisar una ruta nueva", "Detener el programa y pedir al grupo que decida el camino", "La hoja de ruta impresa es el respaldo; no se improvisa."),
        ("abc", "En un programa en un entorno natural exigente, un turista pide hacer una actividad que no está en el programa. ¿Qué corresponde?", "Decirle que solo se hacen las actividades del programa con prestadores autorizados", "Aceptar si el grupo lo pide", "Hacerla si es breve", "Las actividades fuera del programa no fueron evaluadas por el prestador."),
    ],
    ctx=("abc", "{F} Antes de salir, el guía quiere asegurar que todos entienden dónde reunirse si se separan. ¿Qué técnica de comunicación corresponde?", "Repetir el punto de reunión con frases cortas y pedir que alguien lo repita", "Decirlo una sola vez, rápido, al subir al bus", "Escribirlo en un papel que solo tenga el guía", "Repetir y comprobar que el grupo entendió reduce el riesgo de que alguien se pierda."),
    sc=[
        ("En Servicios de Turismo: ¿qué contiene la hoja de ruta?", "Tramos, horarios, paradas y puntos de reunión", "Es el documento que ordena el recorrido."),
        ("¿Por qué la lista de pasajeros es privada?", "Porque tiene datos personales y contactos de emergencia", "Solo quienes la necesitan deben verla."),
        ("¿La tecnología reemplaza al guía?", "No: es un apoyo y no reemplaza el plan ni el criterio del guía", "Puede fallar o quedar sin señal."),
    ],
    op=("Crea la hoja de ruta de una caminata urbana de ejemplo de 2 horas que sale a las 15:00: define dos tramos a pie de 30 y 35 minutos, una pausa de 10 minutos y una visita a un museo de 45 minutos; calcula la hora de término e indica un punto de reunión, una señal acordada y dos frases en inglés de la lección.",
        "Tramo 1: 15:00 a 15:30. Tramo 2 y pausa: según el orden elegido. Museo: 45 minutos. Total: 30 + 35 + 10 + 45 = 120 minutos, es decir, término a las 17:00. Punto de reunión: frente a la puerta del museo. Señal: brazo en alto. Frases: «Please stay together» y «We meet here at ten».",
        ["suma bien los tiempos y calcula la hora de término", "define punto de reunión y señal acordada", "incluye dos frases en inglés correctas"],
        ["hoja de ruta con tramos, hora de término, punto de reunión y frases"],
        ["no sumar la pausa", "olvidar el punto de reunión", "incluir datos personales de pasajeros en la hoja"],
        "Pregunta: «¿a qué hora termina y cómo lo calculaste?». Si no responde, pídele que sume los tiempos en minutos."),
    reinforce="Anota tres elementos de una hoja de ruta que usarías para una salida con tu familia.",
    extend="Explica con un ejemplo inventado por qué se necesita una copia en papel de la hoja de ruta.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (de ejemplo, inventada). Grupo de 18 personas para el programa «Sendero del Mirador»: 6 personas mayores (ritmo de unos 40 metros por minuto), 1 persona que usa silla de ruedas (avanza a unos 50 metros por minuto), "
     "3 turistas que hablan inglés básico y 8 adultos (ritmo de unos 60 metros por minuto). Regla del prestador: el ritmo del grupo es el del integrante más lento. El programa dura como máximo 120 minutos e incluye 3 pausas de 10 minutos. "
     "Ruta A: 2.400 metros, con un tramo de 30 escalones hacia el mirador. Ruta B: 2.800 metros, sin escalones, por senderos habilitados junto a una zona de nidos protegida.")
build(
    O4, 3, F,
    use="Aprenderé a analizar las características de un grupo (edad, movilidad, idioma), a calcular su ritmo y a elegir una ruta adecuada sin suponer lo que cada persona puede o no hacer.",
    prior=["Sé qué es una ruta establecida y una hoja de ruta.", "Sé dividir distancias por velocidades.", "Sé que se pregunta a cada persona qué apoyo necesita."],
    explain=[
        "Cada grupo tiene características distintas: edades, ritmos, idiomas y necesidades de accesibilidad. Conducirlo bien empieza por conocerlas, preguntando a cada persona qué apoyo necesita y sin suponer. El ritmo del grupo es el del integrante más lento: si se avanza al ritmo más rápido, parte del grupo se queda atrás o se cansa. Se pregunta primero, no se decide por ellos.",
        "Para calcular el tiempo de una ruta se divide la distancia por el ritmo y se suman las pausas. Por ejemplo, 1.200 metros a 40 metros por minuto son 30 minutos, más 3 pausas de 10 minutos dan 60 minutos. Se elige la ruta que cumple el tiempo del programa y que puede hacer todo el grupo, por ejemplo una ruta sin escalones si alguien usa silla de ruedas o prefiere evitarlos.",
        "Si hay una zona sensible, como una zona de nidos, se mantiene el grupo en los senderos habilitados y se explica por qué: es una norma de cuidado del medio ambiente. Para turistas con inglés básico se usan frases breves, mapas y señales. El guía autorizado, no este cuaderno, decide en terreno.",
    ],
    vocab=[("ritmo del grupo", "velocidad a la que avanza el integrante más lento"), ("accesibilidad", "que todas las personas puedan usar el recorrido con autonomía"), ("sendero habilitado", "camino autorizado por el administrador del lugar"), ("zona sensible", "lugar frágil, como una zona de nidos, que se debe proteger"), ("pausa", "detención programada para descansar o informar")],
    worked=[
        ("Tiempo de una ruta", "Una ruta de ejemplo mide 1.800 metros y el grupo avanza a 30 metros por minuto, con 2 pausas de 10 minutos. ¿Cuántos minutos dura?", ["1.800 ÷ 30 = 60 minutos de caminata.", "Pausas: 2 × 10 = 20. Total: 60 + 20 = 80 minutos."], "80 minutos"),
        ("Elegir con la necesidad", "Una turista de ejemplo prefiere evitar escalones. La ruta X tiene escalones y la ruta Y no. ¿Cuál corresponde, si ambas caben en el tiempo?", ["Ambas cumplen el tiempo.", "La Y respeta lo que la turista dijo que necesita."], "La ruta Y"),
    ],
    mistakes=[("Marcar el ritmo del grupo según los más rápidos.", "Las personas más lentas se agotan o se separan del grupo.", "Usa el ritmo del integrante más lento."),
              ("Suponer que una persona mayor no puede hacer ninguna ruta.", "Es un estereotipo: la persona decide qué le acomoda.", "Describe cada ruta y pregunta.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es el ritmo del grupo?", "La velocidad a la que avanza el integrante más lento", "La velocidad del integrante más rápido", "El promedio entre el guía y el coordinador", "El ritmo del grupo es el del más lento para que nadie se quede atrás."),
        ("abc", "En Servicios de Turismo: ¿qué es un sendero habilitado?", "Un camino autorizado por el administrador del lugar", "Cualquier camino que se vea marcado en el suelo", "El camino más corto entre dos puntos", "Habilitado significa autorizado; verse marcado o ser corto no basta."),
        ("abc", "En Servicios de Turismo: ¿qué es una zona sensible?", "Un lugar frágil, como una zona de nidos, que debe protegerse", "Un lugar con mucha gente", "Una zona de estacionamiento", "Sensible significa frágil ante la presencia de visitantes."),
        ("=", "{F} ¿Cuántos minutos tarda el grupo en recorrer la ruta A, al ritmo del más lento?", "2400//40", "Se divide la distancia por 40 metros por minuto.", " minutos"),
        ("=", "{F} ¿Cuántos minutos tarda el grupo en recorrer la ruta B, al ritmo del más lento?", "2800//40", "Se divide la distancia por 40 metros por minuto.", " minutos"),
        ("=", "{F} ¿Cuántos minutos suman las 3 pausas del programa?", "3*10", "Se multiplica la cantidad de pausas por su duración.", " minutos"),
        ("=", "{F} ¿Cuántos minutos dura en total la ruta B con sus pausas?", "2800//40+3*10", "Se suman el tiempo de caminata y el de las pausas.", " minutos"),
        ("abc", "{F} ¿Qué ruta corresponde recomendar al grupo y por qué?", "La B, porque no tiene escalones, cabe en el tiempo y puede hacerla toda la gente del grupo", "La A, porque es más corta aunque tenga escalones", "La A, porque los adultos caminan más rápido", "La B cumple el tiempo máximo de 120 minutos y evita los escalones."),
        ("abc", "{F} La persona que usa silla de ruedas, ¿qué debes hacer antes de definir la ruta?", "Preguntarle qué apoyo necesita y qué ruta prefiere", "Decidir por ella la ruta más fácil", "Pedir que otra persona decida por ella", "Cada persona sabe lo que necesita; se le pregunta y se respeta."),
        ("abc", "{F} Un adulto del grupo propone ir al ritmo de los 8 adultos «para llegar antes». ¿Qué corresponde?", "Mantener el ritmo del integrante más lento, como indica la regla del prestador", "Aceptar, porque son la mayoría", "Dividir al grupo en dos sin avisar al coordinador", "La regla es avanzar al ritmo del más lento; dividir al grupo sin consulta aumenta el riesgo."),
        ("abc", "{F} La ruta B pasa junto a una zona de nidos protegida. ¿Qué corresponde?", "Mantener al grupo en los senderos habilitados y explicar por qué se cuida esa zona", "Acercarse a los nidos para que los turistas los vean", "Pasar rápido y sin explicar nada", "Estar en senderos habilitados protege la zona y se explica para cuidar el ambiente."),
        ("ab", "{F} Para los 3 turistas con inglés básico, ¿qué conviene?", "Usar frases breves, mapas y señales simples, y confirmar que entendieron", "Hablarles más rápido en español", "Los apoyos visuales y las frases cortas facilitan entender cuando el idioma es básico."),
        ("abc", "{F} En medio de la ruta, una persona mayor dice que prefiere detenerse un momento. ¿Qué corresponde?", "Detener al grupo y hacer una pausa corta, informando al coordinador si el tiempo cambia", "Pedirle que siga para no atrasar al grupo", "Dejarla sola y continuar", "El ritmo y las pausas se adaptan a las personas; dejar a alguien solo es un riesgo."),
    ],
    ctx=("abc", "{F} Un turista pregunta si puede salirse del sendero habilitado para sacar una mejor foto de un nido. ¿Qué respondes?", "Que debe mantenerse en el sendero para no molestar a las aves y que la foto se toma desde ahí", "Que puede hacerlo si no se acerca demasiado", "Que sí, si le da una propina al guía", "Salir del sendero daña zonas sensibles; se explica y se ofrece una alternativa."),
    sc=[
        ("En Servicios de Turismo: ¿qué ritmo sigue el grupo?", "El del integrante más lento", "Así nadie se queda atrás ni se agota."),
        ("¿Cómo calculas el tiempo de una ruta?", "Divido la distancia por el ritmo y sumo las pausas", "El resultado se compara con el tiempo del programa."),
        ("¿Qué haces si una ruta tiene escalones y alguien prefiere evitarlos?", "Le pregunto y elijo una ruta sin escalones si cabe en el tiempo", "La persona decide qué le acomoda."),
    ],
    op=("Un grupo de ejemplo de 15 personas avanza a 50 metros por minuto. El programa dura como máximo 90 minutos e incluye 2 pausas de 10 minutos. Ruta P: 3.000 metros, plana. Ruta Q: 2.000 metros, con 40 escalones. Una persona del grupo prefiere evitar escalones. Calcula el tiempo de cada ruta con sus pausas y escribe cuál recomiendas, con una frase en que le consultas a esa persona.",
        "Ruta P: 3.000 ÷ 50 = 60 minutos más 20 de pausas = 80 minutos, cabe en 90. Ruta Q: 2.000 ÷ 50 = 40 más 20 = 60 minutos, también cabe, pero tiene escalones. Recomiendo la P porque cabe en el tiempo y respeta lo que la persona prefiere. Frase: «¿Le acomoda la ruta plana de 3.000 metros, o prefiere que revisemos otra opción?».",
        ["calcula bien el tiempo de ambas rutas", "elige la ruta que cumple tiempo y necesidad", "consulta a la persona sin decidir por ella"],
        ["cálculos, recomendación y frase de consulta"],
        ["olvidar sumar las pausas", "elegir por el menor tiempo sin ver la necesidad", "decidir por la persona sin preguntar"],
        "Pregunta: «¿qué dato hizo que descartaras la ruta Q?». Si no responde, repasa la necesidad de evitar escalones."),
    reinforce="Anota el ritmo de tres personas de tu casa al caminar (rápido, medio, lento) y qué ritmo debería seguir un grupo con ellas.",
    extend="Explica con un ejemplo inventado por qué preguntar a la persona es mejor que suponer lo que puede hacer.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (de ejemplo, inventada). Programa «Ruta de los Molinos» (entorno rural), grupo de 24 personas. Regla de ejemplo del prestador: máximo 12 personas por guía. Salida a las 9:00. "
     "Hay conteo del grupo en cuatro puntos de control: P1 (salida), P2 (primera pausa), P3 (almuerzo) y P4 (regreso). Tiempos: tramo 1, 35 minutos; pausa, 10; tramo 2, 40; almuerzo, 50; regreso, 45. "
     "Conteos anotados: P1, 24 personas; P2, 24; P3, 23. Protocolo del prestador (resumen conceptual): si el conteo no coincide, se detiene al grupo, se revisa la lista y se avisa al coordinador.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar criterios de conducción con datos: relación de guías y personas, conteo del grupo en puntos de control, tiempos del programa y reacción conceptual ante diferencias.",
    prior=["Sé qué son la hoja de ruta y la lista de pasajeros.", "Sé sumar y restar tiempos.", "Sé que el protocolo lo define el prestador."],
    explain=[
        "Un criterio técnico de conducción es una regla que se aplica con datos. Uno es la relación de guías: según la regla del prestador, hay un máximo de personas por guía, y se calculan los guías necesarios dividiendo y subiendo al entero siguiente. Otro es el conteo del grupo en puntos de control, que son lugares del recorrido donde se cuenta a las personas y se compara con la lista de pasajeros. Si el conteo no coincide, se actúa según el protocolo del prestador: detener al grupo, revisar la lista y avisar al coordinador.",
        "Un tercer criterio son los tiempos: se suman los tramos, las pausas y los traslados para saber a qué hora termina el programa y si se cumple el horario. Se comparan siempre con la hoja de ruta. Los datos de este cuaderno son de ejemplo y no sustituyen los protocolos reales de un prestador autorizado.",
        "El cuidado del medio ambiente también se aplica como criterio: se lleva la basura de vuelta, se permanece en senderos habilitados y no se extraen plantas ni piedras. Este cuaderno es aprendizaje conceptual en papel; guiar grupos exige guía autorizado y norma vigente.",
    ],
    vocab=[("punto de control", "lugar del recorrido donde se cuenta al grupo y se compara con la lista"), ("conteo", "cantidad de personas contadas en un momento"), ("coordinador", "persona del prestador a quien el guía avisa de las diferencias"), ("horario de término", "hora en que termina el programa"), ("residuos", "basura que se genera durante el recorrido")],
    worked=[
        ("Conteo", "Un grupo de ejemplo anotó 20 personas en la salida y 19 en la primera pausa. ¿Cuántas personas faltan y qué corresponde?", ["20 − 19 = 1 persona de diferencia.", "Se detiene al grupo, se revisa la lista y se avisa al coordinador."], "Falta 1 persona; se sigue el protocolo"),
        ("Hora de término", "Un programa de ejemplo sale a las 8:30 y dura 40 + 10 + 30 + 20 minutos. ¿A qué hora termina?", ["40 + 10 + 30 + 20 = 100 minutos, es decir, 1 hora y 40 minutos.", "8:30 más 1 hora y 40 minutos son las 10:10."], "A las 10:10"),
    ],
    mistakes=[("Contar al grupo una sola vez, al partir.", "Si alguien se queda atrás, no se notaría hasta el final.", "Cuenta en cada punto de control y compara con la lista."),
              ("Dejar la basura «porque alguien pasará a limpiar».", "Es un residuo que daña el ambiente y la imagen del lugar.", "Lleva los residuos de vuelta, como pide la norma de cuidado.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es un punto de control?", "Un lugar del recorrido donde se cuenta al grupo y se compara con la lista", "Un lugar donde se cobra la entrada", "El lugar donde se guarda el equipo", "El punto de control sirve para verificar que están todas las personas."),
        ("abc", "¿Para qué sirve el conteo en puntos de control?", "Para comprobar que están todas las personas y detectar diferencias a tiempo", "Para saber cuántas fotos se sacaron", "Para decidir el menú del almuerzo", "El conteo verifica el grupo; las fotos y el menú no tienen que ver."),
        ("abc", "¿A quién avisa el guía cuando el conteo no coincide con la lista?", "Al coordinador del prestador", "A los turistas del grupo, uno por uno", "A la prensa local", "El coordinador es quien decide con el guía según el protocolo."),
        ("=", "{F} Según la regla de ejemplo, ¿cuántos guías se necesitan para las 24 personas?", "(24+11)//12", "Se divide por 12 personas por guía y se sube al entero siguiente.", " guías"),
        ("=", "{F} ¿Cuántos minutos dura el programa sumando todos los tramos, pausas, almuerzo y regreso?", "35+10+40+50+45", "Se suman los cinco tiempos de la ficha.", " minutos"),
        ("=", "{F} ¿Cuántas horas dura el programa completo?", "(35+10+40+50+45)//60", "Se pasan los minutos totales a horas.", " horas"),
        ("=", "{F} Si el programa sale a las 9:00, ¿a qué hora termina? Escribe solo la hora, sin los minutos.", "9+(35+10+40+50+45)//60", "Se suman las horas de duración a la hora de salida.", " h"),
        ("=", "{F} ¿Cuántas personas faltan en el conteo del punto P3?", "24-23", "Se resta el conteo de P3 al conteo inicial.", " persona"),
        ("abc", "{F} ¿En qué punto de control apareció la diferencia?", "En P3, el almuerzo", "En P1, la salida", "En P2, la primera pausa", "P1 y P2 tienen 24; el conteo bajó recién en P3."),
        ("abc", "{F} El conteo de P3 es 23. ¿Qué corresponde primero?", "Detener al grupo, revisar la lista y avisar al coordinador, como indica el protocolo", "Continuar el programa y esperar que la persona reaparezca", "Esperar al próximo punto de control para volver a contar", "El protocolo del prestador ordena detener, revisar y avisar."),
        ("abc", "{F} Un turista dice que la persona que falta «seguro se fue sola, no importa». ¿Qué respondes?", "Que no se asume nada y se sigue el protocolo del prestador para encontrarla", "Que tiene razón y se continúa", "Que se le cobra a esa persona por irse", "No se supone; el protocolo busca la seguridad de cada integrante."),
        ("abc", "{F} El guía quiere pasar el conteo por un chat abierto del grupo para ahorrar tiempo. ¿Qué corresponde?", "Contar a las personas en el lugar y usar la lista privada, sin publicarla", "Publicar la lista de nombres en el chat", "No contar, porque el chat es más rápido", "La lista de pasajeros es privada y el conteo se hace en persona."),
        ("abc", "{F} Al final del almuerzo, un turista deja bolsas en el suelo diciendo «alguien las recogerá». ¿Qué corresponde?", "Pedir amablemente que se lleven los residuos de vuelta, como indica la norma de cuidado", "Recogerlas el guía sin decir nada", "Dejarlas, porque es un entorno rural", "El grupo debe llevarse sus residuos; se explica con amabilidad."),
    ],
    ctx=("abc", "{F} Al regreso se cuenta nuevamente al grupo en P4, y coincide con la lista. ¿Qué corresponde hacer a continuación?", "Registrar el conteo final y entregar el informe al coordinador", "Borrar la lista para proteger los datos sin avisar", "Compartir la lista con los turistas para que se contacten", "El cierre registra el conteo y se informa al coordinador; la lista se resguarda."),
    sc=[
        ("En Servicios de Turismo: ¿qué se hace si el conteo no coincide?", "Se detiene al grupo, se revisa la lista y se avisa al coordinador", "Es el resumen conceptual del protocolo del prestador."),
        ("¿Cómo se calcula la cantidad de guías necesarios?", "Se divide por el máximo y se sube al entero siguiente", "Así ningún guía supera el máximo."),
        ("¿Qué haces con los residuos de un recorrido?", "Los llevo de vuelta", "Dejar los residuos daña el ambiente del lugar."),
    ],
    op=("Un programa de ejemplo sale a las 10:00 con 30 personas. Regla del prestador: máximo 15 por guía. Tramos: 30 min, pausa 10, tramo de 45, almuerzo de 45, regreso de 30. Conteos: salida 30, pausa 30, almuerzo 29. Calcula guías, hora de término, la diferencia detectada, y escribe tres pasos conceptuales que seguirías, sin inventar procedimientos propios.",
        "Guías: 30 ÷ 15 = 2. Duración: 30 + 10 + 45 + 45 + 30 = 160 minutos, es decir, 2 horas y 40 minutos; término a las 12:40. Diferencia: 30 − 29 = 1 persona, detectada en el almuerzo. Pasos: detener al grupo, revisar la lista y avisar al coordinador, según el protocolo del prestador.",
        ["calcula guías, hora de término y diferencia", "identifica el punto de control donde apareció la diferencia", "nombra los tres pasos del protocolo sin inventar otros"],
        ["cálculos y tres pasos conceptuales"],
        ["olvidar el almuerzo en la suma", "inventar acciones propias fuera del protocolo", "no avisar al coordinador"],
        "Pregunta: «¿por qué avisas al coordinador y no resuelves tú solo?». Si no responde, repasa el rol del coordinador."),
    reinforce="Cuenta cuántos pasos tiene el camino de tu casa a la esquina más cercana y anota para qué serviría un punto de control.",
    extend="Explica con un ejemplo inventado por qué se cuenta al grupo en cada punto de control y no solo al final.",
)

# ============================================================ OAE-04, clase 5
F = ("Ficha 5 (de ejemplo, inventada). Dos propuestas de ruta para un grupo de 20 personas que avanza a 50 metros por minuto, con un máximo de 90 minutos y 3 pausas de 10 minutos. "
     "Propuesta X: 2.000 metros por un atajo que cruza un terreno privado sin permiso. Propuesta Y: 2.500 metros por senderos habilitados, con un tramo de 20 escalones y una alternativa plana de 400 metros más. "
     "Lista de cotejo (1 punto cada una): ruta autorizada por el prestador y el dueño del lugar; cabe en el tiempo; accesible o con alternativa; cuida el ambiente; incluye puntos de reunión y de control. "
     "Encuesta posterior a 10 participantes de ejemplo: 8 dijeron sentirse bien atendidos y 2 sugirieron más pausas.")
build(
    O4, 5, F,
    use="Aprenderé a comparar propuestas de ruta con una lista de cotejo, a revisar un programa al terminar y a incorporar sugerencias, cuidando el ambiente y la seguridad.",
    prior=["Sé calcular tiempos de rutas.", "Sé calcular porcentajes exactos.", "Sé qué es el protocolo y el punto de control."],
    explain=[
        "Comparar alternativas es usar los mismos criterios para todas las propuestas. Una lista de cotejo da un punto por cada criterio cumplido: ruta autorizada por el prestador y por el dueño del lugar, que cabe en el tiempo, que es accesible o tiene alternativa, que cuida el ambiente y que incluye puntos de reunión y de control. Una ruta que cruza un terreno privado sin permiso incumple la autorización y no se usa, aunque sea más corta.",
        "Después del programa se verifica la calidad con evidencia: conteo final, registro de incidentes, encuesta a los participantes y revisión del tiempo real. Con una encuesta se calcula el porcentaje de satisfechos y se leen las sugerencias; por ejemplo, 7 de 10 dan 70 por ciento. Las sugerencias, como agregar pausas, se informan al coordinador para mejorar el programa.",
        "Este cuaderno es conceptual: los programas reales con riesgos los diseña y valida un prestador autorizado, con guía o instructor autorizado y norma vigente.",
    ],
    vocab=[("autorización", "permiso del prestador y del dueño o administrador del lugar"), ("alternativa accesible", "otra ruta que permite evitar un obstáculo, como escalones"), ("informe de cierre", "registro de lo ocurrido en el programa"), ("incidente", "hecho inesperado que se registra aunque no haya daño"), ("porcentaje de satisfechos", "parte de los participantes que se sintió bien, por cada 100")],
    worked=[
        ("Puntaje de una propuesta", "Una ruta de ejemplo está autorizada, cabe en el tiempo, tiene alternativa accesible, cuida el ambiente pero no define puntos de control. ¿Cuántos puntos tiene?", ["Cumple 4 de los 5 criterios.", "Cada criterio vale un punto."], "4 puntos"),
        ("Porcentaje de satisfechos", "En una encuesta de ejemplo, 9 de 12 participantes quedaron conformes. ¿Qué porcentaje es?", ["9 ÷ 12 equivale a 75 de cada 100.", "9 × 100 ÷ 12 = 75."], "75 %"),
    ],
    mistakes=[("Elegir la ruta más corta sin revisar si está autorizada.", "Cruzar un terreno sin permiso incumple las reglas y el respeto por el dueño.", "Verifica la autorización antes de comparar el tiempo."),
              ("No leer las sugerencias de la encuesta porque «la mayoría estuvo conforme».", "Dos personas pueden estar mostrando un problema real del programa.", "Lee todas las sugerencias y evalúa si corresponde mejorar.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué significa que una ruta esté autorizada?", "Que cuenta con el permiso del prestador y del dueño o administrador del lugar", "Que es la más corta", "Que la usan muchos turistas", "La autorización es un permiso; ser corta o popular no la reemplaza."),
        ("abc", "En Servicios de Turismo: ¿qué es un informe de cierre?", "El registro de lo ocurrido en el programa, como conteos e incidentes", "La lista de turistas que desean volver", "El menú del almuerzo", "El informe de cierre documenta cómo resultó el programa."),
        ("abc", "¿Por qué se registra un incidente aunque no haya habido daño?", "Porque ayuda a prevenir que se repita en otros programas", "Para identificar quién tuvo la culpa y sancionarlo", "Para dejar el programa sin cambios", "Registrar permite aprender y mejorar la prevención."),
        ("=", "{F} ¿Cuántos minutos de caminata tiene la propuesta Y por el sendero con escalones?", "2500//50", "Se divide la distancia por el ritmo del grupo.", " minutos"),
        ("=", "{F} ¿Cuántos minutos dura la propuesta Y en total, con las 3 pausas?", "2500//50+3*10", "Se suman el tiempo de caminata y el de las pausas.", " minutos"),
        ("=", "{F} ¿Cuántos minutos le sobran a la propuesta Y respecto del máximo de 90?", "90-(2500//50+3*10)", "Se resta el tiempo total al máximo permitido.", " minutos"),
        ("=", "{F} Con la alternativa plana de 400 metros más, ¿cuántos minutos dura la propuesta Y en total?", "(2500+400)//50+3*10", "Se suma la distancia extra, se divide por el ritmo y se agregan las pausas.", " minutos"),
        ("abc", "{F} ¿Por qué la propuesta X no se puede usar aunque sea más corta?", "Porque cruza un terreno privado sin permiso", "Porque el grupo es muy grande", "Porque no tiene pausas", "Una ruta sin autorización del dueño no cumple las reglas, aunque ahorre tiempo."),
        ("abc", "{F} ¿Qué criterio cumple Y gracias a la alternativa plana?", "Accesible o con alternativa", "Cuida el ambiente", "Cabe en el tiempo", "Evitar los escalones con otra ruta corresponde a tener una alternativa accesible."),
        ("=", "{F} ¿Qué porcentaje de los 10 participantes dijo sentirse bien atendido?", "8*100//10", "Ocho de diez se pasan a porcentaje.", " %"),
        ("abc", "{F} Dos participantes sugirieron más pausas. ¿Qué corresponde?", "Registrar la sugerencia y evaluarla con el coordinador para mejorar el programa", "Ignorarla, porque son solo dos personas", "Eliminar las pausas para avanzar más rápido", "Las sugerencias son evidencia; se evalúan con el coordinador."),
        ("abc", "{F} Una compañera propone usar el atajo X «una sola vez, si nadie lo ve». ¿Qué corresponde?", "Negarse, porque no cuenta con autorización y no se hace aunque nadie lo vea", "Aceptar, porque es solo una vez", "Aceptar si el grupo está de acuerdo", "Una ruta no autorizada incumple las reglas; la discreción no la hace válida."),
        ("abc", "{F} Al cierre del programa, ¿qué verificas respecto de los residuos y el lugar?", "Que el grupo se llevó sus residuos y no quedaron marcas en el entorno", "Que el grupo dejó sus residuos en bolsas bien cerradas en el lugar", "Que se tomaron muchas fotos", "Cuidar el lugar incluye llevar de vuelta todo lo que se trajo."),
    ],
    ctx=("abc", "{F} El coordinador pregunta cuál propuesta presentar al prestador. ¿Qué recomiendas?", "La Y, con su alternativa plana, porque está autorizada, cabe en el tiempo y cuida el ambiente", "La X, porque es más corta", "Las dos por igual, porque ambas caben en el tiempo", "La Y cumple más criterios de la lista de cotejo y respeta la autorización."),
    sc=[
        ("En Servicios de Turismo: ¿qué hace una ruta no autorizada?", "Incumple las reglas, aunque sea más corta", "La autorización es un criterio básico."),
        ("En una salida con un grupo, ¿cómo se calcula el porcentaje de turistas satisfechos?", "Se multiplica por 100 y se divide por el total de participantes", "Así se expresa cuántos se sintieron bien por cada 100."),
        ("¿Qué haces con las sugerencias?", "Las registro y las evalúo con el coordinador", "Son evidencia para mejorar el programa."),
    ],
    op=("Compara dos propuestas de ejemplo para 16 personas que avanzan a 40 metros por minuto, con máximo de 100 minutos y 2 pausas de 10: Propuesta M, 2.400 metros, autorizada, con puntos de reunión, sin alternativa a un tramo de escalones; Propuesta N, 2.800 metros, autorizada, con puntos de reunión y plana. Calcula el tiempo total de cada una, aplica la lista de cotejo de la ficha y recomienda una.",
        "M: 2.400 ÷ 40 = 60 más 20 de pausas = 80 minutos, cabe. N: 2.800 ÷ 40 = 70 más 20 = 90 minutos, cabe. Cotejo: ambas autorizadas, caben y tienen puntos de reunión; N es accesible y M no tiene alternativa. Recomiendo N, porque cumple más criterios y puede hacerla todo el grupo.",
        ["calcula el tiempo total de ambas propuestas", "aplica los criterios de la lista de cotejo", "recomienda con razones y no solo por el tiempo"],
        ["cálculos, puntaje por criterio y recomendación"],
        ["olvidar sumar las pausas", "elegir solo por el menor tiempo", "no aplicar el criterio de accesibilidad"],
        "Pregunta: «¿qué criterio cumple N que M no cumple?». Si no responde, repasa la lista de cotejo."),
    reinforce="Compara dos caminos que conozcas para ir a un mismo lugar y anota cuál cumple más criterios de seguridad y comodidad.",
    extend="Explica con un ejemplo inventado por qué una sugerencia de pocos participantes puede revelar un problema real.",
)
