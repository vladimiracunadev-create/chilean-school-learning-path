"""Cuaderno del estudiante, 2.º medio Historia, Geografía y Ciencias Sociales: OA 25 (diversidad, dignidad y no discriminación en un mundo global)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI2M OA 25"

# ---------------------------------------------------------------- Clase 1
F1 = ("Ficha 1 (definiciones y un hecho). Declaración Universal de Derechos Humanos, 1948, artículo 1: «Todos los seres humanos nacen libres e iguales en dignidad y derechos.» "
      "Discriminación: trato desfavorable hacia una persona por pertenecer a un grupo, sin una razón que lo justifique. "
      "Motivos que nombra el OA: raza o etnia, nacionalidad, situación socioeconómica, religión o creencia, género, orientación sexual y discapacidad. "
      "Globalización: conexión creciente entre países por el comercio, los viajes, la migración e internet. Dato de ejemplo: un curso tiene 40 estudiantes.")
build(
    OA, 1, F1,
    use="Aprenderé a situar el problema de la discriminación: qué es la diversidad, por qué se relaciona con la dignidad y quiénes participan en un mundo conectado.",
    prior=["Sé qué es un derecho y que los derechos humanos valen para todas las personas.", "Sé ubicar un año en su siglo.", "Sé calcular un porcentaje sencillo."],
    explain=[
        "La diversidad es la variedad de personas que forman una sociedad: distintos orígenes, creencias, géneros, capacidades y formas de vida. Es una manifestación de la libertad, porque cada persona puede ser y pensar distinto. La dignidad humana es el valor que tiene toda persona por el solo hecho de serlo; no depende de su origen ni de lo que posea.",
        "La discriminación aparece cuando una persona recibe un trato desfavorable por pertenecer a un grupo y no existe una razón que lo justifique. Los motivos son muchos: raza o etnia, nacionalidad, situación socioeconómica, religión o creencia, género, orientación sexual o discapacidad. Un trato distinto no siempre es discriminación: poner una rampa para quien usa silla de ruedas busca igualar oportunidades.",
        "En un mundo globalizado, las personas de culturas diferentes se encuentran más que antes, en la escuela, el trabajo y las redes. Eso abre oportunidades de aprender y convivir, pero también riesgos de rechazo. Los actores son las personas, las familias, los liceos, el Estado y los organismos internacionales. Ante una situación de discriminación, lo adecuado es avisar a una persona adulta de confianza.",
    ],
    vocab=[("diversidad", "variedad de personas y formas de vida dentro de una sociedad"), ("dignidad", "valor que tiene toda persona por ser persona"), ("discriminación", "trato desfavorable por pertenecer a un grupo, sin razón que lo justifique"), ("globalización", "conexión creciente entre países por comercio, viajes, migración e internet"), ("estereotipo", "imagen simplificada que se atribuye a todo un grupo")],
    worked=[
        ("Reconocer el motivo", "Un aviso de arriendo dice: «No se arrienda a extranjeros». ¿Qué motivo de discriminación aparece?", ["El aviso excluye según el país de origen.", "Ese motivo es la nacionalidad."], "Nacionalidad"),
        ("Distinguir trato distinto de discriminación", "Una escuela entrega un texto en letra grande a un estudiante con baja visión. ¿Es discriminación?", ["Se trata distinto, pero para igualar oportunidades.", "No hay trato desfavorable ni falta de razón."], "No es discriminación"),
    ],
    mistakes=[("Pensar que cualquier trato distinto es discriminación.", "Se olvida que la discriminación exige un trato desfavorable sin razón que lo justifique.", "Pregunta si el trato perjudica al grupo y si hay una razón válida."),
              ("Creer que diversidad y discriminación son lo mismo.", "Se confunde la variedad de personas con el rechazo hacia algunas de ellas.", "Diversidad es variedad; discriminación es el trato desfavorable hacia una parte de esa variedad.")],
    T=[
        ("{F} ¿En qué año se aprobó la Declaración Universal de Derechos Humanos?", "1948", "La ficha la ubica en 1948."),
        ("{F} ¿Cuántos motivos de discriminación nombra el OA en la ficha?", "7", "Son raza o etnia, nacionalidad, situación socioeconómica, religión o creencia, género, orientación sexual y discapacidad."),
        ("{F} ¿Qué es la discriminación según la ficha?", "Un trato desfavorable por pertenecer a un grupo, sin una razón que lo justifique", "Así la define la ficha."),
        ("{F} Un club niega la inscripción a un niño por usar silla de ruedas, sin dar otra razón. ¿Qué motivo aparece? A) Discapacidad B) Nacionalidad", "A) Discapacidad", "El rechazo se debe a su condición física, no a su origen."),
        ("{F} Un curso tiene familias de distintas religiones y todas son tratadas con respeto. ¿Qué describe esto? A) Diversidad B) Discriminación", "A) Diversidad", "Hay variedad de creencias y ningún trato desfavorable."),
        ("{F} ¿Cuál es un caso de discriminación? A) Un taller de robótica rechaza a una alumna por ser mujer B) Un taller rechaza a un alumno que no entregó la autorización firmada", "A) Un taller de robótica rechaza a una alumna por ser mujer", "El rechazo por género no tiene razón que lo justifique; el de la autorización sí la tiene."),
        ("=", "{F} En el curso de 40 estudiantes (de ejemplo), 8 nacieron en otro país. ¿Qué porcentaje es?", "8/40*100", "Se divide 8 entre 40 y se multiplica por 100.", " %"),
        ("{F} Una vecina le dice a una familia recién llegada: «Aquí no queremos gente de afuera». ¿Qué motivo aparece? A) Nacionalidad B) Religión o creencia", "A) Nacionalidad", "El rechazo se dirige al origen de la familia."),
        ("=", "{F} Si el 15 % de los 40 estudiantes del curso (de ejemplo) tiene alguna discapacidad, ¿cuántos son?", "40*15/100", "Se calcula el 15 % de 40.", " estudiantes"),
        ("{F} ¿Por qué la dignidad sirve de criterio para juzgar si un trato es discriminatorio?", "Porque toda persona la tiene por igual, así que un trato que la desconoce es injustificado", "El artículo 1 dice que todas las personas son iguales en dignidad."),
        ("{F} Un compañero afirma: «Tratar distinto siempre es discriminar». ¿Qué corrección haces? A) Solo es discriminación si el trato es desfavorable y sin razón que lo justifique B) Es correcto, porque cualquier diferencia perjudica", "A) Solo es discriminación si el trato es desfavorable y sin razón que lo justifique", "Poner una rampa trata distinto pero iguala oportunidades."),
        ("{F} ¿Qué afirmación se sostiene con la ficha? A) La globalización aumenta el contacto entre personas distintas, lo que da oportunidades de convivir y riesgos de rechazo B) La globalización elimina la discriminación porque conecta a los países", "A) La globalización aumenta el contacto entre personas distintas, lo que da oportunidades de convivir y riesgos de rechazo", "Conectar países no garantiza trato respetuoso; la ficha solo habla de conexión."),
        ("¿Cuál es la mejor pregunta para investigar este tema? A) ¿Cómo se manifiesta la diversidad y qué trato respeta la dignidad de todas las personas? B) ¿Qué grupo de personas es mejor?", "A) ¿Cómo se manifiesta la diversidad y qué trato respeta la dignidad de todas las personas?", "La A se puede responder con hechos y criterio; la B parte de un prejuicio."),
    ],
    ctx=("Un estudiante ve que en un grupo de mensajería del curso se burlan de un compañero por su acento extranjero. ¿Qué es lo más adecuado? A) Avisar a una persona adulta de confianza y no reenviar las burlas B) Reenviar los mensajes para que otros opinen", "A) Avisar a una persona adulta de confianza y no reenviar las burlas", "Reenviar amplía el daño; avisar a un adulto protege a la persona afectada."),
    sc=[("¿Qué es la dignidad?", "El valor que tiene toda persona por ser persona", "Así se define en el vocabulario de la clase."),
        ("En esta clase, ¿qué es un estereotipo?", "Una imagen simplificada que se atribuye a todo un grupo", "Así se define en el vocabulario."),
        ("=", "En un curso de 50 estudiantes (de ejemplo), 10 son de otra nacionalidad. ¿Qué porcentaje es?", "10/50*100", "Se divide 10 entre 50 y se multiplica por 100.", " %")],
    op=("Escribe una ficha de tres líneas. Línea 1: define diversidad con tus palabras. Línea 2: define discriminación e incluye uno de los siete motivos. Línea 3: describe un caso ficticio de trato distinto que NO sea discriminación y explica por qué. Usa uno de estos casos: texto en letra grande para un estudiante con baja visión, o una prueba reprogramada por una celebración religiosa familiar. {F}",
        "Diversidad: variedad de personas y formas de vida. Discriminación: trato desfavorable por religión o creencia sin razón. Caso: reprogramar una prueba por una celebración religiosa busca igualar oportunidades, por eso no es discriminación.",
        ["define bien diversidad y discriminación", "nombra un motivo de la lista", "distingue un trato distinto justificado"], ["ficha de tres líneas"], ["decir que todo trato distinto es discriminación", "no justificar por qué el caso no es discriminación"],
        "Pide que explique qué criterio usó para decidir que el trato estaba justificado."),
    reinforce="Explica en voz alta la diferencia entre diversidad y discriminación y da un ejemplo de cada una.",
    extend="Piensa en un lugar de tu comunidad con una rampa, una señal o un texto pensado para incluir a alguien y di a quién ayuda.",
)

# ---------------------------------------------------------------- Clase 2
F2 = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos reales). "
      "Fuente 1, informe de una junta de vecinos, 2019: «En nuestro barrio viven 120 familias; 30 llegaron de otros países en los últimos cinco años. Organizamos una feria con comidas de cada país.» "
      "Fuente 2, comentario anónimo en un foro de internet: «Los que llegan de afuera nos quitan el trabajo; siempre ha sido así.» "
      "Fuente 3, folleto de una municipalidad, 2021: «Todas las oficinas deben tener rampa y atención en lenguaje claro para personas con discapacidad. Atención de lunes a viernes.»")
build(
    OA, 2, F2,
    use="Aprenderé a interrogar fuentes sobre diversidad y discriminación: quién las escribe, para qué, con qué datos y cuánto se puede concluir de ellas.",
    prior=["Sé qué es una fuente y qué es su procedencia.", "Sé calcular un porcentaje sencillo.", "Conozco los motivos de discriminación de la clase anterior."],
    explain=[
        "Para interrogar una fuente se pregunta por su procedencia: quién la escribió, cuándo, para quién y con qué propósito. Una fuente con autor identificable y datos que se pueden revisar es más confiable que una afirmación anónima sin datos. Una opinión no es lo mismo que una prueba.",
        "También hay que pensar en el posible sesgo, es decir, la tendencia a mostrar solo una parte de la realidad. Una organización que cuenta lo bueno que hizo puede ser veraz, pero conviene contrastarla con otra fuente. Una afirmación como «siempre ha sido así» o «todos son…» generaliza sin evidencia y suele ser un estereotipo.",
        "Al concluir, se dice solo lo que la fuente permite. Un folleto que exige rampas prueba que existe una obligación, no que todos los lugares la cumplan. Antes de compartir un mensaje sobre un grupo de personas, revisa quién lo escribió y si trae datos; si contiene burlas u odio, avisa a una persona adulta de confianza.",
    ],
    vocab=[("procedencia", "origen de una fuente: quién la hizo, cuándo y para qué"), ("sesgo", "tendencia a mostrar solo una parte de la realidad"), ("generalizar", "atribuir a todo un grupo lo que se vio en unos pocos"), ("contrastar", "comparar una fuente con otras para ver si coinciden"), ("evidencia", "dato o hecho que sirve para apoyar una afirmación")],
    worked=[
        ("Evaluar la procedencia", "Un cartel sin firma dice que un grupo de vecinos «arruina el barrio». ¿Es una buena evidencia?", ["No tiene autor ni fecha.", "Tampoco trae datos que se puedan revisar."], "No, es una afirmación sin procedencia ni datos"),
        ("Calcular con una fuente", "Una fuente de ejemplo dice que 18 de 90 estudiantes de un liceo participan en un taller de lengua de señas. ¿Qué porcentaje es?", ["Divido 18 entre 90.", "El resultado es 0,2, o sea 20 %."], "20 %"),
    ],
    mistakes=[("Creer una afirmación porque muchos la comparten.", "Se confunde popularidad con evidencia.", "Revisa autor, fecha y datos antes de aceptarla."),
              ("Decir que algo de internet es siempre falso.", "Se descarta sin examinar la procedencia.", "Evalúa cada fuente: autor, propósito y datos, esté donde esté.")],
    T=[
        ("{F} ¿Quién escribió la fuente 2?", "Una persona anónima en un foro de internet", "La ficha no identifica al autor."),
        ("{F} ¿Cuántas familias del barrio llegaron de otros países según la fuente 1?", "30", "La fuente 1 lo indica."),
        ("{F} ¿Qué exige el folleto de la fuente 3 a las oficinas?", "Rampa y atención en lenguaje claro para personas con discapacidad", "Así lo dice el folleto."),
        ("{F} ¿Qué fuente tiene autor identificable y cifras? A) Fuente 1 B) Fuente 2", "A) Fuente 1", "La junta de vecinos firma y entrega números; el comentario es anónimo."),
        ("{F} ¿Por qué la fuente 2 es débil como evidencia? A) Es anónima y afirma sin datos B) Es de internet, y todo lo de internet es falso", "A) Es anónima y afirma sin datos", "El problema es la falta de autor y de datos, no el lugar donde aparece."),
        ("{F} ¿Cuál es el propósito principal de la fuente 3? A) Informar una obligación de accesibilidad B) Vender un servicio", "A) Informar una obligación de accesibilidad", "Es un folleto municipal que indica cómo deben ser las oficinas."),
        ("=", "{F} ¿Qué porcentaje de las familias del barrio llegó de otros países?", "30/120*100", "Se divide 30 entre 120 y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas familias del barrio NO llegaron de otros países en los últimos cinco años?", "120-30", "Se resta el grupo que llegó al total de familias.", " familias"),
        ("{F} ¿Qué se puede concluir de la fuente 1? A) Que en ese barrio 1 de cada 4 familias llegó de otro país en cinco años B) Que todos los extranjeros del país participan en ferias", "A) Que en ese barrio 1 de cada 4 familias llegó de otro país en cinco años", "30 de 120 es una cuarta parte; la fuente no habla de todo el país."),
        ("{F} ¿Se puede probar con la fuente 2 que las personas migrantes quitan empleos? A) No, no tiene autor identificable ni datos B) Sí, porque habla de trabajo", "A) No, no tiene autor identificable ni datos", "Sin autor ni datos, solo es una opinión generalizadora."),
        ("{F} ¿Qué fuente serviría mejor para revisar la afirmación de la fuente 2? A) Estadísticas de empleo de una institución que explica su método B) Otro comentario anónimo con la misma idea", "A) Estadísticas de empleo de una institución que explica su método", "Un dato con método se puede revisar; otro comentario anónimo solo repite la idea."),
        ("{F} La junta de vecinos cuenta la feria que ella misma organizó. ¿Qué precaución corresponde? A) Contrastarla con otra fuente, porque puede mostrar solo lo positivo B) Descartarla por haber sido escrita por vecinos", "A) Contrastarla con otra fuente, porque puede mostrar solo lo positivo", "Hay posible sesgo, pero eso no la invalida: se contrasta."),
        ("{F} Un compañero dice: «El folleto prueba que ya no hay discriminación por discapacidad». ¿Qué respondes? A) Prueba que existe una obligación, no que todos los lugares la cumplan B) Tiene razón, porque está impreso", "A) Prueba que existe una obligación, no que todos los lugares la cumplan", "Una norma no prueba por sí sola su cumplimiento."),
    ],
    ctx=("Te llega un mensaje reenviado que dice que un grupo religioso «hace daño a los demás», sin firma ni datos. ¿Qué haces primero? A) Revisar quién lo escribió y si trae datos, y avisar a una persona adulta de confianza si hay burlas u odio B) Reenviarlo porque muchas personas lo comparten", "A) Revisar quién lo escribió y si trae datos, y avisar a una persona adulta de confianza si hay burlas u odio", "Compartir sin revisar difunde un posible estereotipo."),
    sc=[("¿Qué es la procedencia de una fuente?", "El origen de la fuente: quién la hizo, cuándo y para qué", "Así se define en el vocabulario."),
        ("¿Qué significa generalizar?", "Atribuir a todo un grupo lo que se vio en unos pocos", "Así se define en la clase."),
        ("=", "Una fuente de ejemplo dice que 12 de 60 estudiantes usan un servicio de apoyo. ¿Qué porcentaje es?", "12/60*100", "Se divide 12 entre 60 y se multiplica por 100.", " %")],
    op=("Elige UNA fuente de la ficha. Escribe cuatro líneas: quién la produjo, para qué, un dato o afirmación que entrega y una conclusión que NO se puede sacar de ella. Termina con una pregunta que harías para contrastarla con otra fuente. {F}",
        "Fuente 3. Produjo: una municipalidad. Para: informar una obligación de accesibilidad. Dato: rampas y lenguaje claro. No se puede concluir que todas las oficinas la cumplan. Pregunta: ¿qué oficinas fueron revisadas y quién lo comprobó?",
        ["identifica autor y propósito", "extrae un dato o afirmación real de la fuente", "señala un límite de lo que se puede concluir"], ["cuatro líneas escritas", "pregunta de contraste"], ["tomar la fuente como prueba absoluta", "concluir más de lo que dice"],
        "Pide que explique por qué una fuente anónima necesita más contraste que una firmada."),
    reinforce="Explica a una persona de tu casa por qué conviene mirar quién escribió un mensaje antes de reenviarlo.",
    extend="Anota una frase que empiece con «todos los…» y reescríbela sin generalizar.",
)

# ---------------------------------------------------------------- Clase 3
F3 = ("Ficha 3 (escalas y perspectivas; casos de ejemplo escritos para este cuaderno). "
      "Escala local: un liceo de ejemplo reprograma una prueba cuando coincide con una celebración religiosa familiar. "
      "Escala nacional: en Chile, la ley antidiscriminación (llamada Ley Zamudio) es de 2012; entre los motivos que protege están el sexo, la orientación sexual, la religión o creencia y la discapacidad. "
      "Escala global: la Convención internacional sobre la eliminación de la discriminación racial se adoptó en 1965 y la Convención sobre los derechos de las personas con discapacidad, en 2006. "
      "Perspectivas del mismo caso: una alumna dice «me incomodaba pedir permiso»; un profesor dice «yo seguía el calendario»; la dirección dice «ahora tenemos una norma escrita».")
build(
    OA, 3, F3,
    use="Aprenderé a comparar cómo se enfrenta la discriminación en la escala local, nacional y global, y a comparar las perspectivas de quienes participan en un mismo caso.",
    prior=["Sé qué es discriminación y cuáles son sus motivos.", "Sé interrogar la procedencia de una fuente.", "Sé calcular diferencias entre años."],
    explain=[
        "La escala es el nivel desde el que se mira un problema. En la escala local se observan casos concretos, como un liceo o un barrio. En la escala nacional aparecen las leyes de un país. En la escala global están los tratados que firman muchos Estados. Un mismo problema se ve distinto en cada escala y las soluciones también.",
        "La perspectiva es el punto de vista de cada actor. La persona afectada puede sentir una exclusión que otros no notan; quien aplicó una regla puede haber seguido una costumbre sin mala intención; una institución puede responder con una norma. Comparar perspectivas no obliga a darles el mismo peso: el criterio de decisión es la dignidad de la persona afectada y los hechos comprobables.",
        "Una ley o un tratado es una condición necesaria, pero no suficiente. Si una norma nacional existe y un club local sigue excluyendo, falta aplicarla. Por eso conviene mirar las tres escalas juntas, incluyendo motivos como género, orientación sexual, religión o discapacidad, y reconocer que el cambio ocurre cuando las normas se cumplen en la vida diaria.",
    ],
    vocab=[("escala", "nivel desde el que se estudia un problema: local, nacional o global"), ("perspectiva", "punto de vista de un actor sobre un hecho"), ("tratado", "acuerdo escrito entre Estados"), ("norma", "regla escrita que orienta la conducta"), ("cumplimiento", "aplicación real de una norma")],
    worked=[
        ("Reconocer la escala", "Un municipio de ejemplo crea una oficina de atención a personas migrantes. ¿Qué escala es?", ["Afecta a una comuna y a su comunidad.", "No es una ley del país ni un tratado."], "Local"),
        ("Comparar perspectivas", "Un director de ejemplo dice que ahora existe una regla para reprogramar pruebas y una alumna dice que aún le da vergüenza pedirla. ¿Se contradicen?", ["El director habla de la existencia de la regla.", "La alumna habla de cómo se vive; ambas pueden ser ciertas."], "No, son perspectivas distintas del mismo caso"),
    ],
    mistakes=[("Pensar que si existe una ley el problema ya terminó.", "Se confunde norma escrita con cumplimiento real.", "Pregunta si la norma se aplica en lo local."),
              ("Resolver un conflicto dando razón a quien tiene más amigos o más cargo.", "Se olvida el criterio de dignidad y hechos.", "Juzga según los hechos comprobables y la dignidad de la persona afectada.")],
    T=[
        ("{F} ¿En qué año se promulgó la ley antidiscriminación chilena que nombra la ficha?", "2012", "La ficha la ubica en 2012."),
        ("{F} ¿Qué escala corresponde al caso del liceo que reprograma la prueba?", "Local", "Es un caso de un solo establecimiento."),
        ("{F} ¿Qué convención se adoptó en 2006?", "La Convención sobre los derechos de las personas con discapacidad", "La ficha lo indica."),
        ("{F} Un tratado firmado por muchos Estados corresponde a la escala: A) Global B) Local", "A) Global", "Involucra a varios países."),
        ("{F} La frase «me incomodaba pedir permiso» expresa la perspectiva de: A) La persona afectada B) La dirección del liceo", "A) La persona afectada", "Es la alumna quien lo dice."),
        ("{F} ¿Qué diferencia hay entre la ley chilena y la norma del liceo? A) La ley alcanza a todo el país y la norma solo a su comunidad B) La ley es local y la norma es global", "A) La ley alcanza a todo el país y la norma solo a su comunidad", "La escala nacional abarca el país; la local, un establecimiento."),
        ("{F} ¿Qué discriminación busca eliminar la convención de 1965? A) La discriminación racial B) La discriminación por discapacidad", "A) La discriminación racial", "La ficha la nombra como convención sobre la eliminación de la discriminación racial; la de discapacidad es de 2006."),
        ("{F} El profesor dice «yo seguía el calendario». ¿Qué perspectiva expresa? A) La de quien aplicó la regla por costumbre, sin mala intención B) La de la persona afectada", "A) La de quien aplicó la regla por costumbre, sin mala intención", "Cuenta que seguía una costumbre; no dice que quisiera excluir."),
        ("{F} La dirección dice «ahora tenemos una norma escrita». ¿Qué perspectiva expresa? A) Institucional B) De la persona afectada", "A) Institucional", "Habla de la respuesta de la organización."),
        ("{F} Existe una ley nacional contra la discriminación, pero un club de barrio sigue excluyendo a socias por ser mujeres. ¿Qué muestra? A) Que una norma escrita no basta si no se cumple en lo local B) Que la ley no sirve", "A) Que una norma escrita no basta si no se cumple en lo local", "La norma existe; falta aplicarla en la escala local."),
        ("{F} Dos personas relatan distinto un caso: una dice que sufrió un trato humillante y la otra que «era una broma». ¿Qué criterio corresponde? A) La dignidad de la persona afectada y los hechos comprobables B) La opinión de quien tiene más amigos", "A) La dignidad de la persona afectada y los hechos comprobables", "El criterio es la dignidad y la evidencia, no la popularidad."),
        ("{F} Un compañero dice: «La discriminación por orientación sexual ya está prohibida, así que no hay nada más que hacer». ¿Qué falta considerar? A) Que prohibirla no asegura que deje de ocurrir; hay que cumplir y respetar la norma B) Nada, porque la ley lo resuelve", "A) Que prohibirla no asegura que deje de ocurrir; hay que cumplir y respetar la norma", "Tener una norma es distinto de cumplirla."),
        ("{F} ¿Cuál es la mejor síntesis? A) Un mismo caso se entiende mejor mirando tres escalas y varias perspectivas, juzgadas con el criterio de dignidad B) Solo importa la escala global", "A) Un mismo caso se entiende mejor mirando tres escalas y varias perspectivas, juzgadas con el criterio de dignidad", "Reúne escalas, perspectivas y criterio."),
    ],
    ctx=("En el taller de tecnología algunos dicen que trabajar con herramientas «es cosa de hombres». ¿Qué respuesta respeta la dignidad? A) Todas las personas pueden participar según sus intereses, y si alguien lo impide se avisa a una persona adulta de confianza B) Separar los grupos por género", "A) Todas las personas pueden participar según sus intereses, y si alguien lo impide se avisa a una persona adulta de confianza", "Separar por género repite el estereotipo; avisar protege a quien es excluido."),
    sc=[("¿Qué es una perspectiva?", "El punto de vista de un actor sobre un hecho", "Así se define en la clase."),
        ("¿Qué es un tratado?", "Un acuerdo escrito entre Estados", "Así se define en el vocabulario."),
        ("En Historia: ¿qué escala estudia los tratados que firman muchos Estados?", "La escala global", "Así se define la escala global en la clase.")],
    op=("Arma una tabla con tres filas: local, nacional y global. En cada una escribe un hecho de la ficha y una acción posible para tu curso. Después escribe dos frases con las perspectivas de dos actores distintos del caso del liceo. Termina con el criterio que usarías para decidir quién tiene razón. {F}",
        "Local: el liceo reprograma pruebas; en el curso, avisar los cambios con tiempo. Nacional: ley de 2012; conocerla. Global: convención de 2006; respetar la accesibilidad. Criterio: dignidad y hechos comprobables.",
        ["completa las tres escalas con hechos de la ficha", "presenta dos perspectivas distintas", "explica un criterio de decisión"], ["tabla de tres filas", "dos frases con perspectivas"], ["repetir la misma información en las tres escalas", "decidir según quién tiene más poder"],
        "Pide que explique cómo cambia la solución según la escala."),
    reinforce="Cuenta a una persona de tu casa qué diferencia hay entre una regla del liceo, una ley del país y un tratado entre países.",
    extend="Anota una norma que haya en tu liceo para que todas las personas participen y di a qué escala corresponde.",
)

# ---------------------------------------------------------------- Clase 4
F4 = ("Ficha 4 (causas, cambios y continuidades). "
      "Causas de la discriminación: el prejuicio (juicio formado antes de conocer a la persona); el estereotipo (imagen simplificada de todo un grupo); la desigualdad económica; el desconocimiento. "
      "Cambios: en 1948 se aprobó la Declaración Universal de Derechos Humanos; en Chile, una ley de 1949 reconoció el derecho a voto de las mujeres en todas las elecciones; en 2012 se promulgó la ley antidiscriminación. "
      "Continuidades: todavía hay trato desigual en lugares de estudio, de trabajo y en internet. "
      "Globalización: ofrece oportunidades (redes de apoyo, contacto entre culturas) y desafíos (mensajes ofensivos que se difunden muy rápido).")
build(
    OA, 4, F4,
    use="Aprenderé a relacionar las causas de la discriminación con los cambios que se lograron y las continuidades que persisten, y a ver oportunidades y desafíos de un mundo globalizado.",
    prior=["Sé qué es discriminación y cuáles son sus motivos.", "Sé comparar escalas y perspectivas.", "Sé calcular diferencias entre años y potencias sencillas."],
    explain=[
        "La discriminación tiene varias causas que se refuerzan. El prejuicio es una opinión formada antes de conocer a la persona. El estereotipo es una imagen simplificada de todo un grupo, como pensar que «las mujeres no sirven para la tecnología». La desigualdad económica también influye: quienes tienen menos recursos suelen ser vistos con desconfianza, lo que se llama discriminación por situación socioeconómica.",
        "En el tiempo hubo cambios importantes. En 1948 se aprobó la Declaración Universal de Derechos Humanos; en Chile, una ley de 1949 reconoció el voto de las mujeres en todas las elecciones, y en 2012 se promulgó la ley antidiscriminación. Pero hay continuidades: todavía existen trato desigual y burlas por origen, religión, género, orientación sexual o discapacidad. Un cambio legal no borra de inmediato las costumbres.",
        "La globalización no creó la discriminación, que existía antes. Sí cambió su forma: un mensaje ofensivo puede llegar a muchas personas en minutos, pero también las redes permiten apoyar a quien lo sufre y conectar con otras culturas. Ante burlas o acoso, lo adecuado es no reenviar, guardar la evidencia y avisar a una persona adulta de confianza.",
    ],
    vocab=[("prejuicio", "juicio formado antes de conocer a la persona"), ("desigualdad", "diferencia injusta en el acceso a recursos u oportunidades"), ("cambio", "aspecto que se transformó con el tiempo"), ("continuidad", "aspecto que se mantiene con el tiempo"), ("viralizar", "difundir un mensaje a muchísimas personas muy rápido")],
    worked=[
        ("Clasificar cambio o continuidad", "Una ley nueva permite a las personas con discapacidad entrar a los edificios públicos, pero muchos edificios antiguos no tienen rampa. ¿Qué es cada cosa?", ["La ley es algo nuevo: un cambio.", "La falta de rampas es algo que persiste: una continuidad."], "La ley es un cambio y la falta de rampas es una continuidad"),
        ("Calcular una propagación", "Un mensaje llega a 3 personas; cada una lo reenvía a otras 3. ¿Cuántas personas lo reciben en esa segunda ronda?", ["Cada una de las 3 lo envía a 3.", "3 × 3 = 9."], "9 personas"),
    ],
    mistakes=[("Decir que la globalización causó la discriminación.", "Se ignora que existía antes de internet y de la conexión mundial.", "Di que la globalización puede acelerar su difusión, no que la creó."),
              ("Creer que una ley termina con la discriminación de inmediato.", "Se confunde un cambio legal con un cambio en las costumbres.", "Distingue lo que cambió en la ley de lo que persiste en la práctica.")],
    T=[
        ("{F} ¿En qué año una ley chilena reconoció el voto de las mujeres en todas las elecciones?", "1949", "La ficha lo indica."),
        ("{F} ¿Qué es un estereotipo?", "Una imagen simplificada que se atribuye a todo un grupo", "Así lo define la ficha."),
        ("{F} ¿Qué es un prejuicio?", "Un juicio formado antes de conocer a la persona", "Así lo define la ficha."),
        ("{F} La frase «los jóvenes de ese barrio son todos peligrosos» es: A) Un estereotipo B) Un dato comprobado", "A) Un estereotipo", "Atribuye una misma característica a todo un grupo sin evidencia."),
        ("{F} La promulgación de la ley antidiscriminación en 2012 es: A) Un cambio B) Una continuidad", "A) Un cambio", "Es algo nuevo respecto de antes de 2012."),
        ("{F} Que todavía haya burlas por la religión de una persona es: A) Una continuidad B) Un cambio", "A) Una continuidad", "Es algo que persiste a pesar de las leyes."),
        ("=", "{F} Un mensaje ofensivo lo reciben 5 personas en la ronda 1; en cada ronda siguiente, cada persona que lo recibió en la ronda anterior lo reenvía a 5 personas nuevas. ¿Cuántas lo reciben en la ronda 3?", "5*5*5", "Cada ronda multiplica por 5: 5, 25 y 125.", " personas"),
        ("{F} Una empresa de ejemplo solo contrata hombres porque «siempre ha sido así». ¿Cuál es la causa principal? A) Un estereotipo de género B) Falta de currículos", "A) Un estereotipo de género", "Se basa en una idea simplificada sobre un grupo y no en el mérito."),
        ("{F} ¿Cuál de estas es una oportunidad de la globalización según la ficha? A) Las redes de apoyo y el contacto entre culturas B) Los mensajes ofensivos que se difunden muy rápido", "A) Las redes de apoyo y el contacto entre culturas", "La ficha pone los mensajes ofensivos entre los desafíos."),
        ("{F} ¿Por qué la desigualdad económica puede reforzar la discriminación por situación socioeconómica? A) Porque quienes tienen menos recursos tienen menos acceso a oportunidades y el estereotipo los hace ver como culpables B) Porque todas las personas pobres piensan igual", "A) Porque quienes tienen menos recursos tienen menos acceso a oportunidades y el estereotipo los hace ver como culpables", "El estereotipo agrava la desventaja material."),
        ("{F} Un compañero dice: «La globalización creó la discriminación». ¿Qué corrección haces? A) La discriminación existía antes; la globalización puede acelerar su difusión y también las redes de apoyo B) Es correcto, porque antes no se viajaba", "A) La discriminación existía antes; la globalización puede acelerar su difusión y también las redes de apoyo", "La Declaración de 1948 ya la combatía, antes de internet."),
        ("{F} ¿Qué ejemplo muestra una continuidad y no un cambio? A) Un aviso que sigue rechazando a personas por su origen B) Una ley que amplió el voto a las mujeres", "A) Un aviso que sigue rechazando a personas por su origen", "El rechazo persiste; la ley de 1949 fue un cambio."),
        ("{F} ¿Cuál es la mejor síntesis? A) Hubo cambios legales importantes, pero persisten prejuicios y estereotipos, y la globalización ofrece apoyo y también difunde mensajes ofensivos B) Todo cambió y ya no queda discriminación", "A) Hubo cambios legales importantes, pero persisten prejuicios y estereotipos, y la globalización ofrece apoyo y también difunde mensajes ofensivos", "Reúne cambios, continuidades y la doble cara de la globalización."),
    ],
    ctx=("Una compañera recibe burlas en redes por vivir en un sector con menos recursos. ¿Qué es lo más adecuado? A) No reenviar los mensajes, guardar la evidencia y avisar a una persona adulta de confianza B) Responder con otras burlas para defenderla", "A) No reenviar los mensajes, guardar la evidencia y avisar a una persona adulta de confianza", "Responder con burlas escala el conflicto; avisar y guardar evidencia ayuda a detenerlo."),
    sc=[("¿Qué es una continuidad?", "Un aspecto que se mantiene con el tiempo", "Así se define en la clase."),
        ("¿Qué es viralizar un mensaje?", "Difundirlo a muchísimas personas muy rápido", "Así se define en el vocabulario."),
        ("=", "Un mensaje llega a 4 personas y cada una lo reenvía a otras 4. ¿Cuántas lo reciben en la segunda ronda?", "4*4", "Cada una de las 4 personas lo reenvía a 4.", " personas")],
    op=("Haz un cuadro con tres columnas: «causas», «cambios» y «continuidades». Escribe dos ideas en cada una usando la ficha, y marca con una estrella una oportunidad y un desafío de la globalización. Después escribe una frase que empiece con «La discriminación persiste, aunque…». {F}",
        "Causas: prejuicio y estereotipo. Cambios: ley de 1949 y ley de 2012. Continuidades: trato desigual en estudio y trabajo; burlas en internet. Frase: la discriminación persiste, aunque existen leyes que la prohíben.",
        ["clasifica bien causas, cambios y continuidades", "distingue una oportunidad y un desafío de la globalización", "evita decir que la globalización creó la discriminación"], ["cuadro de tres columnas", "frase con «aunque»"], ["confundir cambio con continuidad", "atribuir una causa única"],
        "Pide que explique por qué una ley no basta para cambiar las costumbres."),
    reinforce="Explica en voz alta la diferencia entre prejuicio y estereotipo y da un ejemplo ficticio de cada uno.",
    extend="Piensa en una norma antigua que hoy te parecería injusta y di quién la cambió y cómo.",
)

# ---------------------------------------------------------------- Clase 5
F5 = ("Ficha 5 (pregunta y evidencias de ejemplo). Pregunta de investigación: ¿cómo puede un liceo asegurar que estudiantes con discapacidad participen en igualdad? "
      "Evidencia 1, encuesta de ejemplo del liceo: se consultó a 60 estudiantes y 24 dijeron que tienen dificultad para entrar a la biblioteca. "
      "Evidencia 2, reglamento de ejemplo: «La biblioteca funciona en el segundo piso; el edificio tiene solo escalera.» "
      "Evidencia 3, testimonio de ejemplo de un estudiante con movilidad reducida: «Si hubiera rampa o ascensor, podría estudiar con mis compañeros.» "
      "Evidencia 4: la Convención de 2006 sobre los derechos de las personas con discapacidad busca que estas personas participen en igualdad de condiciones con las demás.")
build(
    OA, 5, F5,
    use="Aprenderé a construir una interpretación documentada: plantear una tesis, apoyarla con evidencias, y reconocer los límites de lo que esas evidencias permiten afirmar.",
    prior=["Sé interrogar la procedencia de una fuente.", "Sé distinguir causas, cambios y continuidades.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Una interpretación documentada responde una pregunta de investigación con una tesis, es decir, una afirmación que se puede defender. La tesis se apoya con evidencias de distinto tipo: datos, normas, testimonios. Cada evidencia se cita y se explica, para mostrar por qué apoya la tesis.",
        "También se señalan los límites. Una encuesta de un solo liceo no permite hablar de todo el país. Un testimonio muestra una experiencia, pero no prueba la intención de nadie. Una barrera, como una escalera sin rampa, puede excluir sin que haya mala intención; igual se debe corregir, porque afecta la dignidad y la participación de las personas.",
        "Un buen párrafo sigue este orden: tesis, evidencia citada, explicación y límite. Las soluciones que mejor respetan la dignidad incluyen a las personas afectadas: se las consulta antes de decidir. Esto vale para la discapacidad y para cualquier otro motivo de discriminación.",
    ],
    vocab=[("tesis", "afirmación que responde la pregunta y se defiende con evidencia"), ("barrera", "obstáculo físico, social o de comunicación que impide participar"), ("accesibilidad", "condición que permite a todas las personas usar un lugar o servicio"), ("testimonio", "relato de una persona sobre lo que vivió"), ("límite", "aquello que la evidencia no permite afirmar")],
    worked=[
        ("Elegir una evidencia", "Quieres probar que una piscina de ejemplo no tiene acceso para sillas de ruedas. ¿Qué evidencia sirve más: el plano con solo escaleras o un comentario que dice «es fea»?", ["El plano muestra una barrera concreta.", "El comentario opina sobre otra cosa."], "El plano con solo escaleras"),
        ("Fijar un límite", "Una encuesta de ejemplo a 30 estudiantes de un liceo muestra que 9 tienen dificultad para usar el patio. ¿Se puede decir que pasa en todos los liceos?", ["La encuesta solo consultó un liceo.", "No permite generalizar."], "No, solo describe ese liceo"),
    ],
    mistakes=[("Escribir una lista de datos sin una tesis.", "Se junta información pero no se responde la pregunta.", "Escribe primero una afirmación y usa los datos para apoyarla."),
              ("Afirmar la intención de alguien a partir de una barrera.", "Se confunde un obstáculo con una decisión de excluir.", "Describe la barrera y sus efectos; para hablar de intención se necesita otra evidencia.")],
    T=[
        ("{F} ¿Dónde funciona la biblioteca según el reglamento?", "En el segundo piso", "El reglamento de ejemplo lo indica."),
        ("{F} ¿Cuántos estudiantes se consultaron en la encuesta?", "60", "La evidencia 1 lo señala."),
        ("{F} ¿Qué evidencia es un testimonio?", "La evidencia 3", "Es el relato de un estudiante sobre su experiencia."),
        ("{F} ¿Qué es una tesis? A) Una afirmación que responde la pregunta y se defiende con evidencia B) Una lista de datos sueltos", "A) Una afirmación que responde la pregunta y se defiende con evidencia", "La tesis necesita evidencias que la apoyen."),
        ("{F} ¿Qué evidencia apoya que existe una barrera física? A) El reglamento: segundo piso y solo escalera B) El testimonio sobre estudiar con compañeros", "A) El reglamento: segundo piso y solo escalera", "Describe el obstáculo físico."),
        ("{F} ¿Qué busca la Convención de 2006? A) Que las personas con discapacidad participen en igualdad de condiciones B) Que las personas con discapacidad usen espacios separados de las demás", "A) Que las personas con discapacidad participen en igualdad de condiciones", "Así lo dice la evidencia 4."),
        ("=", "{F} ¿Qué porcentaje de los estudiantes encuestados dijo tener dificultad para entrar a la biblioteca?", "24/60*100", "Se divide 24 entre 60 y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos de los estudiantes encuestados NO dijeron tener esa dificultad?", "60-24", "Se resta el grupo con dificultad al total de encuestados.", " estudiantes"),
        ("{F} ¿Qué tesis tiene mejor apoyo en la ficha? A) El liceo debería mejorar el acceso a la biblioteca, porque 2 de cada 5 estudiantes encuestados tienen dificultad para entrar y el edificio solo tiene escalera B) Todos los liceos de Chile excluyen a su alumnado", "A) El liceo debería mejorar el acceso a la biblioteca, porque 2 de cada 5 estudiantes encuestados tienen dificultad para entrar y el edificio solo tiene escalera", "24 de 60 es 2 de cada 5; la otra tesis generaliza sin evidencia."),
        ("{F} ¿Cuál es un límite de la encuesta? A) Es de un solo liceo, así que no permite generalizar a todo el país B) Es una encuesta, y las encuestas nunca sirven", "A) Es de un solo liceo, así que no permite generalizar a todo el país", "El límite es el alcance, no el tipo de fuente."),
        ("{F} Un compañero concluye: «El liceo discrimina a propósito». ¿Se sostiene? A) No: la evidencia muestra una barrera, pero no la intención B) Sí, porque el reglamento dice segundo piso", "A) No: la evidencia muestra una barrera, pero no la intención", "Una barrera puede excluir sin intención; igual hay que corregirla."),
        ("{F} ¿Qué orden tiene un párrafo bien documentado? A) Tesis, evidencia citada, explicación y límite B) Límite, evidencia y al final la tesis", "A) Tesis, evidencia citada, explicación y límite", "Responde la pregunta y muestra por qué la evidencia la apoya."),
        ("{F} ¿Qué solución respeta mejor la dignidad? A) Instalar rampa o ascensor, o mover la biblioteca al primer piso, consultando a los estudiantes afectados B) Pedir a quienes tienen dificultad que solo usen libros que otros les lleven", "A) Instalar rampa o ascensor, o mover la biblioteca al primer piso, consultando a los estudiantes afectados", "Elimina la barrera e incluye a las personas afectadas."),
    ],
    ctx=("En un cine de ejemplo, la sala solo tiene entrada con escalones. Un grupo de espectadores pide una solución. ¿Qué argumento está mejor construido? A) Hay una barrera en la entrada; una rampa permitiría que todas las personas participen, como busca la Convención de 2006 B) Las escaleras son parte del diseño del cine, así que no hay nada que cambiar", "A) Hay una barrera en la entrada; una rampa permitiría que todas las personas participen, como busca la Convención de 2006", "Describe la barrera, propone una solución y la apoya con una norma."),
    sc=[("¿Qué es la accesibilidad?", "La condición que permite a todas las personas usar un lugar o servicio", "Así se define en el vocabulario."),
        ("¿Qué es un límite de una evidencia?", "Aquello que la evidencia no permite afirmar", "Así se define en la clase."),
        ("=", "Una encuesta de ejemplo consulta a 80 estudiantes y 20 dicen tener una dificultad. ¿Qué porcentaje es?", "20/80*100", "Se divide 20 entre 80 y se multiplica por 100.", " %")],
    op=("Escribe un párrafo de cinco líneas que responda la pregunta de la ficha. Línea 1: tu tesis. Líneas 2 y 3: dos evidencias de la ficha, con su explicación. Línea 4: una solución que consulte a las personas afectadas. Línea 5: un límite de la evidencia. {F}",
        "Tesis: el liceo debe eliminar la barrera de acceso a la biblioteca. Evidencia 1: 24 de 60 dicen tener dificultad. Evidencia 2: solo hay escalera. Solución: rampa, consultando a quienes la necesitan. Límite: la encuesta es de un solo liceo.",
        ["la tesis responde la pregunta", "usa dos evidencias de la ficha con explicación", "incluye una solución y un límite"], ["párrafo de cinco líneas"], ["listar datos sin tesis", "afirmar intención de excluir sin evidencia"],
        "Pide que explique por qué una barrera debe corregirse aunque nadie haya querido excluir."),
    reinforce="Explica a una persona de tu casa qué es una tesis y por qué necesita evidencias.",
    extend="Piensa en un lugar de tu comunidad que sea difícil de usar para alguien y escribe una mejora posible.",
)

# ---------------------------------------------------------------- Clase 6
F6 = ("Ficha 6 (debate; textos de ejemplo escritos para este cuaderno). "
      "Postura A, de ejemplo: «Cada persona debe poder expresar cualquier opinión sin restricciones; la mejor respuesta a una mala idea es discutirla.» "
      "Postura B, de ejemplo: «La libertad de expresión tiene un límite: no puede usarse para humillar a una persona por su origen, creencia, género, orientación sexual o discapacidad, porque daña su dignidad.» "
      "Criterio de la clase: una crítica a una idea se puede debatir; un ataque a una persona por pertenecer a un grupo es discriminación. "
      "Dato de ejemplo: un foro revisó 200 mensajes y 30 contenían insultos a un grupo. "
      "Para conocer las costumbres o la lengua de un pueblo originario, corresponde consultar a su educador o educadora tradicional o a la comunidad.")
build(
    OA, 6, F6,
    use="Aprenderé a debatir sobre las consecuencias y límites de convivir en la diversidad: dónde termina la libertad de opinar y empieza el daño a la dignidad de otra persona.",
    prior=["Sé qué es discriminación y cuáles son sus motivos.", "Sé construir una tesis con evidencias.", "Sé calcular porcentajes."],
    explain=[
        "Debatir es defender una postura con argumentos y evidencias, escuchando la postura contraria. Un argumento tiene una afirmación, una razón y una evidencia. Se puede criticar una idea, pero no atacar a una persona por pertenecer a un grupo. Esa es la línea que usamos en esta clase: la crítica se debate; el ataque por origen, etnia, creencia, género, orientación sexual, discapacidad o situación económica es discriminación.",
        "La libertad de expresión es un derecho valioso, pero convive con otros derechos. Cuando un mensaje humilla a alguien por su identidad, daña su dignidad y puede dejarlo fuera de la conversación. Las consecuencias de ignorarlo son la exclusión, el miedo y la pérdida de oportunidades. Las de restringir demasiado también existen: se puede silenciar la crítica legítima.",
        "Por eso los límites se debaten con cuidado, considerando casos concretos. En temas de pueblos originarios, de religión o de identidad, lo respetuoso es informarse en fuentes confiables y escuchar a las propias comunidades. Si ocurre una situación de acoso, no se enfrenta a solas: se guarda la evidencia, no se reenvía y se avisa a una persona adulta de confianza.",
    ],
    vocab=[("argumento", "afirmación apoyada con una razón y una evidencia"), ("libertad de expresión", "derecho a comunicar ideas y opiniones"), ("ataque", "mensaje que humilla a una persona por pertenecer a un grupo"), ("moderar", "revisar y retirar mensajes que dañan a otras personas"), ("consecuencia", "efecto que sigue a una decisión o a un hecho")],
    worked=[
        ("Distinguir crítica y ataque", "«Esa propuesta del centro de estudiantes es mala porque cuesta demasiado.» ¿Es crítica o ataque?", ["Se dirige a una idea y da una razón.", "No humilla a nadie por su grupo."], "Es una crítica a una idea"),
        ("Calcular una proporción", "Un grupo de ejemplo revisó 50 mensajes y 5 contenían insultos a un grupo. ¿Qué porcentaje es?", ["Divido 5 entre 50.", "El resultado es 0,1, es decir, 10 %."], "10 %"),
    ],
    mistakes=[("Defender cualquier mensaje diciendo que es «solo una opinión».", "Se confunde la crítica a una idea con el ataque a una persona.", "Pregunta si el mensaje discute una idea o humilla a alguien por su grupo."),
              ("Resolver un caso de acoso confrontando a solas a quien lo hace.", "Se arriesga la seguridad y se pierde la evidencia.", "Guarda la evidencia, no reenvíes y avisa a una persona adulta de confianza.")],
    T=[
        ("{F} ¿Cuántos mensajes revisó el foro?", "200", "El dato de ejemplo lo indica."),
        ("{F} ¿Qué límite propone la postura B para la libertad de expresión?", "No usarla para humillar a una persona por su origen, creencia, género, orientación sexual o discapacidad", "La postura B lo dice así."),
        ("{F} ¿A quién se debe consultar sobre las costumbres de un pueblo originario?", "A su educador o educadora tradicional o a la comunidad", "La ficha lo indica."),
        ("{F} «Creo que esta norma del liceo es injusta porque no consulta al alumnado» es: A) Una crítica a una idea B) Un ataque por pertenecer a un grupo", "A) Una crítica a una idea", "Discute una norma y da una razón."),
        ("{F} Un compañero se burla del apellido de otro por ser de un pueblo originario. ¿Qué motivo aparece? A) Raza o etnia B) Discapacidad", "A) Raza o etnia", "La burla se dirige a su origen étnico."),
        ("{F} ¿Qué postura pone un límite basado en la dignidad? A) La postura B B) La postura A", "A) La postura B", "B dice que la expresión no puede humillar por la identidad de una persona."),
        ("=", "{F} ¿Qué porcentaje de los mensajes revisados contenía insultos a un grupo?", "30/200*100", "Se divide 30 entre 200 y se multiplica por 100.", " %"),
        ("{F} Un mensaje dice: «Las personas de esa creencia no merecen trabajo». ¿Qué es? A) Un ataque por religión o creencia B) Una crítica a una idea", "A) Un ataque por religión o creencia", "Humilla a un grupo entero por lo que cree."),
        ("{F} Una estudiante recibe burlas por su acento en un chat del curso. ¿Qué haces? A) Guardar la evidencia, no reenviar y avisar a una persona adulta de confianza B) Responder con insultos para igualar", "A) Guardar la evidencia, no reenviar y avisar a una persona adulta de confianza", "Es el protocolo seguro; responder con insultos escala el conflicto."),
        ("{F} ¿Qué consecuencia puede tener ignorar los ataques por identidad en una conversación? A) Que algunas personas se sientan excluidas y dejen de participar B) Que la conversación mejore porque habla más gente", "A) Que algunas personas se sientan excluidas y dejen de participar", "El daño a la dignidad provoca exclusión."),
        ("{F} ¿Qué riesgo tiene restringir demasiado lo que se puede decir? A) Silenciar también la crítica legítima B) Que desaparezcan todos los desacuerdos", "A) Silenciar también la crítica legítima", "Un límite mal definido puede alcanzar a opiniones válidas."),
        ("{F} Un compañero dice: «Si es mi opinión, puedo decir lo que quiera de cualquier grupo». ¿Qué respuesta usa la ficha? A) La opinión se debate, pero humillar a una persona por su grupo daña su dignidad B) Tiene razón, la expresión no tiene límites", "A) La opinión se debate, pero humillar a una persona por su grupo daña su dignidad", "La postura B y el criterio de la clase lo distinguen."),
        ("{F} ¿Cuál es el mejor argumento para moderar mensajes? A) Retirar los que humillan por identidad protege la dignidad y permite que todas las personas participen B) Retirar mensajes impide que se debatan ideas, sean críticas o insultos", "A) Retirar los que humillan por identidad protege la dignidad y permite que todas las personas participen", "Tiene afirmación, razón y apunta a un derecho."),
    ],
    ctx=("En un debate del curso sobre un tema de religión, un estudiante critica una idea con argumentos y otro insulta a quienes la profesan. ¿Quién respeta el criterio de la clase? A) El que critica la idea con argumentos B) El que insulta, porque expresa su opinión", "A) El que critica la idea con argumentos", "La crítica a una idea se debate; el insulto a un grupo es discriminación."),
    sc=[("¿Qué es un argumento?", "Una afirmación apoyada con una razón y una evidencia", "Así se define en el vocabulario."),
        ("¿Qué es moderar?", "Revisar y retirar mensajes que dañan a otras personas", "Así se define en el vocabulario."),
        ("=", "Un grupo de ejemplo revisa 400 mensajes y 40 contienen insultos a un grupo. ¿Qué porcentaje es?", "40/400*100", "Se divide 40 entre 400 y se multiplica por 100.", " %")],
    op=("Prepara un mini debate escrito. Elige la postura A o la B de la ficha. Escribe tu argumento con afirmación, razón y evidencia (puedes usar el dato del foro). Escribe después la mejor objeción de la postura contraria y tu respuesta. Termina con una consecuencia de tu postura y un límite. {F}",
        "Postura B. Afirmación: la expresión tiene límites. Razón: humillar daña la dignidad. Evidencia: 30 de 200 mensajes contenían insultos. Objeción: se puede silenciar la crítica; respuesta: se retira el insulto, no la crítica. Límite: hay que revisar caso por caso.",
        ["el argumento tiene afirmación, razón y evidencia", "presenta y responde una objeción", "señala una consecuencia y un límite"], ["texto escrito", "objeción y respuesta"], ["defender sin evidencia", "tratar a quien piensa distinto como enemigo"],
        "Pide que explique cómo distingue una crítica a una idea de un ataque a una persona."),
    reinforce="Explica a una persona de tu casa la diferencia entre criticar una idea y atacar a una persona por su grupo.",
    extend="Piensa en una situación en que opinar distinto pueda hacerse con respeto y escribe dos frases que lo logren.",
)
