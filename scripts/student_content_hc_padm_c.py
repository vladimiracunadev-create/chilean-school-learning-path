"""Participación y argumentación en democracia (electivo HC, 3.º y 4.º medio): OAC-04 (elaborar argumentos con evidencias o información pública legitimada), clases 1 a 4, y OAC-05 (usar formas de argumentación y de legitimación pertinentes al ámbito, la comunidad y el propósito), clases 1 a 4. Casos ficticios y datos de ejemplo."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada texto, ficha o tabla está escrito en el enunciado. "
             "Todos los casos son ficticios (comuna «Villa Alerce», «Liceo Los Pinos») y los datos son de ejemplo: no son cifras reales ni se deben citar como si lo fueran. "
             "Las posturas se presentan con sus razones y sin tomar partido: tu tarea es construir y evaluar argumentos. Si un tema te afecta personalmente, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O4 = "LL-PADM-3y4-OAC-04"
O5 = "LL-PADM-3y4-OAC-05"

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (argumento de ejemplo). Afirmación: «La biblioteca de Villa Alerce debería abrir los sábados.» "
     "Evidencia: «En una encuesta municipal de ejemplo a 150 usuarios de la biblioteca, 90 dijeron que solo pueden ir los fines de semana.» "
     "Garantía: «Un servicio público debería abrir los días en que sus usuarios pueden usarlo.» "
     "Fuente: informe de ejemplo de la Municipalidad de Villa Alerce (ficticia), publicado con el detalle de cómo se hizo la encuesta.")
build(
    O4, 1, F,
    use="Aprenderé qué es una evidencia y qué es información pública legitimada, y a armar un argumento con afirmación, evidencia y garantía que sean pertinentes al problema.",
    prior=["Sé distinguir premisa y conclusión.", "Sé evaluar una fuente con aceptabilidad, suficiencia y pertinencia.", "Sé calcular un porcentaje."],
    explain=[
        "Elaborar un argumento basado en evidencia significa que cada afirmación importante se apoya en algo que otros pueden revisar. La evidencia puede ser un dato, un documento, un testimonio o un ejemplo bien descrito. La información pública legitimada es la que producen instituciones o personas con responsabilidad pública y se publica con fuente, fecha y método: informes oficiales, actas, datos abiertos o normas.",
        "Un argumento completo tiene tres partes. La afirmación es lo que se defiende. La evidencia es el dato o documento que la respalda. La garantía es el puente que explica por qué esa evidencia sirve para esa afirmación; sin ella, la evidencia queda suelta. En el ejemplo, saber que 90 de 150 usuarios solo pueden ir los fines de semana apoya abrir los sábados gracias a la garantía de que un servicio público debe estar abierto cuando sus usuarios pueden usarlo.",
        "La evidencia debe ser pertinente: tratar del problema. Datos sobre la cantidad de libros no apoyan abrir los sábados. También debe citarse con precisión, indicando quién la produjo, cuándo y qué midió, y sin exagerar: 90 de 150 es el 60 %, no «casi todos». Una buena argumentación presenta la evidencia tal como es, incluso cuando no apoya todo lo que quisiéramos.",
    ],
    vocab=[("evidencia", "dato, documento o testimonio que respalda una afirmación"), ("información pública legitimada", "información de fuente pública, con método y fecha, que otros pueden verificar"), ("afirmación", "lo que se defiende en un argumento"), ("garantía", "razón que une la evidencia con la afirmación"), ("cita de la fuente", "indicación de quién produjo la información y cuándo"), ("exagerar", "decir más de lo que muestran los datos")],
    worked=[
        ("Identificar las partes", "En la ficha, ¿cuál es la garantía?",
         ["La afirmación es abrir los sábados y la evidencia es la encuesta.", "La garantía es la razón que une ambas: un servicio público debería abrir los días en que sus usuarios pueden usarlo."],
         "Un servicio público debería abrir los días en que sus usuarios pueden usarlo"),
        ("Citar sin exagerar", "¿Cómo se debe expresar el dato de 90 de 150 usuarios?",
         ["90 ÷ 150 = 0,6, que es 60 %.", "Se escribe: «60 % de los 150 usuarios consultados dijo que solo puede ir los fines de semana»."],
         "60 % de los 150 usuarios consultados, y no «casi todos»"),
    ],
    mistakes=[("Presentar un dato sin explicar por qué apoya la afirmación.", "Se olvida la garantía.", "Agrega una oración que une el dato con la conclusión."),
              ("Usar evidencia que trata de otro tema.", "Se elige un dato llamativo sin revisar la pertinencia.", "Pregunta si el dato responde a lo que afirmas.")],
    T=[
        ("abc", "{F} ¿Cuál es la afirmación del argumento?", "La biblioteca debería abrir los sábados", "90 usuarios solo pueden ir los fines de semana", "Un servicio público debería abrir cuando sus usuarios pueden", "La afirmación es lo que se defiende."),
        ("abc", "{F} ¿Cuál es la evidencia?", "La encuesta a 150 usuarios, de los que 90 solo pueden ir en fin de semana", "Que un servicio público debe abrir los sábados", "Que la biblioteca existe", "Es el dato que respalda la afirmación."),
        ("abc", "{F} ¿Para qué sirve la garantía?", "Para explicar por qué la evidencia apoya la afirmación", "Para repetir la afirmación", "Para adornar el texto", "Sin ella la evidencia queda sin vínculo con la conclusión."),
        ("=", "{F} En otra pregunta de la misma encuesta, 30 de los 150 usuarios dijeron que prefieren ir en las tardes de lunes a viernes. ¿Qué porcentaje es?", "30*100//150", "30 de 150 es 1 de cada 5, es decir 20 por cada 100.", " %"),
        ("abc", "{F} ¿Por qué es información pública legitimada?", "Viene de una institución pública, con fuente, método y fecha", "Porque mucha gente la comparte", "Porque está escrita con convicción", "Los otros pueden verificarla porque su fuente es pública."),
        ("abc", "{F} ¿Cuál de estos datos NO es pertinente para apoyar abrir los sábados?", "La cantidad de libros de poesía de la biblioteca", "Cuántos usuarios solo pueden ir en fin de semana", "Cuántos usuarios dicen que no pueden ir entre semana", "Los libros de poesía no tratan sobre el horario de apertura."),
        ("ab", "{F} ¿Cuál es una forma fiel de citar el dato?", "«Según el informe municipal de ejemplo, 60 % de los 150 usuarios consultados solo puede ir en fin de semana»", "«Casi todos los usuarios solo pueden ir en fin de semana»", "La primera indica fuente y cifra exacta; la segunda exagera lo que los datos muestran."),
        ("abc", "{F} Un compañero añade: «Además, en Chile todas las bibliotecas abren los sábados». ¿Qué problema tiene?", "Es una afirmación sin fuente y probablemente falsa", "Es una garantía válida", "Es una buena evidencia por ser general", "Una generalización sin fuente no es evidencia verificable."),
        ("abc", "Alguien dice: «Hay que abrir los sábados porque yo lo prefiero». ¿Qué le falta a su argumento?", "Evidencia y garantía que no dependan solo de su preferencia", "Más volumen de voz", "Un título", "Una preferencia personal no basta como evidencia de que sea conveniente para la comunidad."),
        ("abc", "{F} Se cambia la evidencia por: «90 de 150 usuarios dicen que la biblioteca es bonita». ¿Qué ocurre?", "Deja de apoyar la afirmación porque trata de otro asunto", "Apoya mejor que antes", "Es la misma evidencia", "Mide la opinión sobre la belleza, no la posibilidad de asistir."),
        ("abc", "{F} ¿Qué dato adicional haría más fuerte el argumento?", "Cuántos usuarios llegarían un sábado según la misma encuesta", "El nombre del alcalde", "El color del edificio", "Se relaciona directamente con el uso de la apertura de sábado."),
        ("abc", "Una evidencia con fuente anónima y sin fecha, como «lo leí en un chat», ¿qué problema tiene para un argumento?", "No se puede verificar ni citar con precisión", "Es demasiado larga", "Es demasiado oficial", "Sin fuente identificable otros no pueden comprobarla."),
        ("abc", "{F} ¿Qué cambio de la garantía la volvería discutible?", "«Un servicio público debería abrir siempre, a cualquier costo»", "«Un servicio público debería abrir cuando sus usuarios pueden usarlo»", "«Los servicios públicos existen»", "Agrega un absoluto que se puede objetar: a cualquier costo."),
    ],
    ctx=("abc", "Un centro de estudiantes ficticio quiere pedir más bebederos. Tiene un informe interno de ejemplo con 200 estudiantes consultados, de los que 140 dicen que no encuentran agua fría en el patio. ¿Cuál es la afirmación mejor respaldada?", "Una parte importante de los consultados no encuentra agua fría en el patio", "Todos los estudiantes del país carecen de agua", "El liceo es el peor de la comuna", "Se limita a lo que los datos de la muestra muestran."),
    sc=[
        ("En Participación y argumentación: ¿qué es información pública legitimada?", "Información de fuente pública, con método y fecha, verificable", "Se publica con datos que otros pueden revisar."),
        ("¿Cuáles son las tres partes de un argumento con evidencia?", "Afirmación, evidencia y garantía", "Cada parte cumple una función distinta."),
        ("¿Qué significa exagerar una evidencia?", "Decir más de lo que muestran los datos", "Por ejemplo, convertir 60 % en «casi todos»."),
    ],
    op=("Elige uno. Caso 1: el liceo debería instalar más enchufes en la biblioteca; datos de ejemplo: de 80 estudiantes consultados, 50 dijeron que a veces no encuentran dónde cargar el computador. Caso 2: la feria debería tener un puesto de reciclaje; datos de ejemplo: un informe municipal indica que la feria genera 40 bolsas de basura por fin de semana. "
        "Escribe un argumento con afirmación, evidencia (citando fuente y cifra exacta), garantía y un cálculo de porcentaje o de cantidad.",
        "Caso 1. Afirmación: la biblioteca debería tener más enchufes. Evidencia: según una consulta de ejemplo, 50 de 80 estudiantes (62,5 %, es decir, más de la mitad) dijeron que a veces no encuentran dónde cargar el computador. Garantía: un espacio de estudio debería permitir usar los equipos que el estudiantado necesita.",
        ["afirmación clara", "evidencia citada con fuente y cifra exacta", "garantía que une evidencia y afirmación", "no exagera los datos"],
        ["texto de cuatro oraciones con las tres partes marcadas"],
        ["olvidar la garantía", "citar el dato sin fuente", "exagerar el porcentaje"],
        "Pregunta: «¿por qué ese dato apoya tu afirmación?». Pide escribir la garantía."),
    reinforce="Con la ficha, escribe una nueva garantía distinta que también una la evidencia con la afirmación.",
    extend="Explica una situación en la que una evidencia verdadera no sea pertinente al problema discutido.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (tres documentos de ejemplo). Documento 1, acta del concejo municipal de Villa Alerce (ficticia): «Se aprobó destinar $2.400.000 anuales a la mantención de la plaza.» "
     "Documento 2, informe municipal de ejemplo sobre asistencia a talleres de la plaza, por mes: marzo, 40 personas; abril, 55; mayo, 60; junio, 45. "
     "Documento 3, publicación anónima en redes: «La plaza es un desastre y nadie hace nada.»")
build(
    O4, 2, F,
    use="Aprenderé a investigar un caso público: escoger documentos verificables, extraer datos con exactitud, hacer cálculos simples y citarlos con precisión para sostener un argumento.",
    prior=["Sé qué es una evidencia pertinente.", "Sé calcular promedios y porcentajes simples.", "Sé que una fuente debe ser identificable."],
    explain=[
        "Investigar un caso público es buscar y leer documentos que ayuden a responder una pregunta. Un acta, un informe o una norma son fuentes públicas: tienen autor institucional, fecha y se pueden consultar. Una publicación anónima es solo una pista, porque no se puede verificar quién la escribió ni cómo sabe lo que dice. Lo primero es identificar el tipo de documento y qué información entrega realmente.",
        "Luego se extraen los datos con exactitud: se copian las cifras con su unidad y su período. Con los datos se pueden hacer cálculos simples que los hacen más comprensibles: totales, promedios, diferencias y porcentajes. Por ejemplo, si el presupuesto anual es de $2.400.000, lo que corresponde a cada mes se obtiene dividiendo por 12. Es importante no mezclar períodos ni unidades al comparar.",
        "Por último, se cita la evidencia dejando claro de dónde sale: «según el informe municipal de ejemplo, en mayo asistieron 60 personas a los talleres». Se separa lo que dice el documento de lo que se interpreta: el informe muestra cuántas personas asistieron, pero no explica por qué subió o bajó. Esa interpretación debe presentarse como hipótesis y no como dato.",
    ],
    vocab=[("acta", "registro oficial de lo tratado y acordado en una sesión"), ("informe", "documento que presenta datos o análisis sobre un asunto"), ("fuente pública", "documento de una institución, accesible para consulta"), ("promedio", "suma de los valores dividida por la cantidad de valores"), ("período", "tramo de tiempo al que se refiere un dato"), ("interpretación", "explicación que se propone a partir de los datos")],
    worked=[
        ("Extraer y calcular", "Con el documento 2, ¿cuántas personas asistieron a los talleres entre marzo y junio en total?",
         ["Se suman los cuatro meses: 40 + 55 + 60 + 45.", "40 + 55 = 95; 95 + 60 = 155; 155 + 45 = 200."],
         "200 personas"),
        ("Citar con exactitud", "Escribe cómo citarías el dato de mayo.",
         ["Indica el documento: informe municipal de ejemplo sobre asistencia a talleres.", "Indica la cifra con unidad y período: 60 personas en mayo."],
         "Según el informe municipal de ejemplo, en mayo asistieron 60 personas"),
    ],
    mistakes=[("Interpretar un aumento de asistencia como si el informe explicara la causa.", "Se confunde lo que el documento muestra con lo que uno supone.", "Separa el dato de la hipótesis: «subió, quizás por…»."),
              ("Mezclar un presupuesto anual con un dato mensual al comparar.", "Se olvida revisar el período de cada cifra.", "Convierte los datos a un mismo período antes de compararlos.")],
    T=[
        ("abc", "{F} ¿Qué documento es una fuente pública verificable?", "El documento 1 o el 2, emitidos por la municipalidad", "El documento 3, publicación anónima", "Ninguno de los tres", "Las actas e informes institucionales tienen autor y fecha."),
        ("abc", "{F} ¿Qué problema tiene el documento 3 como evidencia?", "Es anónimo y no entrega datos verificables", "Está en redes y es muy corto", "Dice la verdad", "No se puede saber quién lo escribió ni cómo lo sabe."),
        ("abc", "{F} ¿Qué mes tuvo más asistentes?", "Mayo", "Marzo", "Junio", "En el documento 2, mayo tiene 60, la cifra más alta."),
        ("=", "{F} ¿Cuántas personas más asistieron en mayo que en marzo?", "60-40", "Se resta la asistencia de marzo a la de mayo.", " personas"),
        ("=", "{F} ¿Cuál fue el promedio mensual de asistencia entre marzo y junio?", "(40+55+60+45)//4", "El total de 200 personas dividido en 4 meses es 50.", " personas"),
        ("=", "{F} Si el presupuesto anual es de $2.400.000, ¿cuánto corresponde a cada mes?", "2400000//12", "Se divide el presupuesto anual por los 12 meses del año.", " pesos"),
        ("abc", "{F} ¿Qué porcentaje del total de 200 asistentes fue el de mayo?", "30 %", "60 %", "15 %", "60 de 200 es 0,3, es decir, 30 por cada 100."),
        ("abc", "{F} ¿Cuál es una cita fiel del dato de junio?", "Según el informe municipal de ejemplo, en junio asistieron 45 personas", "En junio vinieron muchísimas personas", "Todos fueron en junio", "Indica fuente, período y cifra exacta."),
        ("abc", "{F} Una participante afirma: «Los talleres subieron en mayo porque el alcalde los promocionó». ¿Qué falla?", "El informe no explica la causa; es una hipótesis que habría que comprobar", "Es un dato del acta", "Es una cifra mal sumada", "Se atribuye una causa que el documento no entrega."),
        ("abc", "{F} Se quiere argumentar que la plaza recibe poca inversión. ¿Qué documento y dato conviene citar?", "El acta, con los $2.400.000 anuales, comparados con otras necesidades documentadas", "La publicación anónima", "El promedio de asistencia", "El acta es una fuente pública sobre el presupuesto."),
        ("abc", "{F} Alguien compara «$2.400.000 al año» con «$250.000 por mes» y dice que el segundo es menor. ¿Qué error comete?", "Compara cifras de períodos distintos sin convertir", "Suma mal los meses", "Usa una fuente privada", "Anual y mensual no se comparan sin igualar el período."),
        ("abc", "{F} De los cuatro meses, ¿qué conclusión es más prudente sobre la asistencia?", "Subió de marzo a mayo y bajó en junio, sin explicar la causa", "Seguirá subiendo siempre", "Los talleres fracasaron", "Describe lo que los datos muestran y no extrapola."),
        ("abc", "{F} Para investigar por qué bajó en junio, ¿qué sería un siguiente paso razonable?", "Consultar si hubo cambios de horario o clima en junio y preguntar a los asistentes", "Dar por cierto que fue por desinterés", "Cerrar los talleres", "Se buscan datos para poner a prueba hipótesis."),
    ],
    ctx=("abc", "En un informe de ejemplo del liceo, el uso de la biblioteca fue de 120, 150 y 90 visitas en tres semanas. ¿Cuál fue el promedio semanal de visitas?", "120", "150", "90", "La suma de 360 visitas dividida en 3 semanas da 120."),
    sc=[
        ("En Participación y argumentación: ¿qué se debe indicar al citar un dato?", "Quién lo produjo, la cifra con unidad y el período", "Así otras personas pueden verificar la información citada."),
        ("¿Por qué una publicación anónima es solo una pista?", "Porque no se puede verificar quién la escribió ni cómo lo sabe", "Le falta una fuente identificable que otros puedan revisar."),
        ("=", "En un informe de ejemplo, un taller tuvo 18, 22 y 20 asistentes. ¿Cuál es el promedio?", "(18+22+20)//3", "La suma es 60 y se divide en 3 datos."),
    ],
    op=("Elige uno. Caso 1: documentos de ejemplo del liceo: acta del consejo escolar («se aprobó comprar 10 balones para el recreo»), informe de inspectoría con préstamos de balones por semana (35, 40, 30, 45) y un mensaje anónimo («los balones se pierden siempre»). "
        "Caso 2: informe municipal de ejemplo sobre visitantes de un museo (lunes 20, martes 25, miércoles 30, jueves 25, viernes 50) y un comentario anónimo («el museo siempre está vacío»). "
        "Identifica qué documentos son fuentes públicas verificables, calcula total y promedio, y escribe una cita fiel con una hipótesis aparte.",
        "Caso 1. Fuentes verificables: acta e informe. Total de préstamos: 150; promedio: 37,5 por semana. Cita: según el informe de inspectoría de ejemplo, el préstamo más alto fue 45 balones en la cuarta semana. Hipótesis aparte: quizás subió por un campeonato.",
        ["distingue fuentes verificables de anónimas", "calcula bien el total y el promedio", "cita con exactitud", "separa dato e hipótesis"],
        ["hoja con clasificación de fuentes, cálculos y cita"],
        ["tratar el anónimo como evidencia", "calcular mal el promedio", "presentar una hipótesis como dato"],
        "Pregunta: «¿qué dice el documento y qué estás suponiendo tú?». Pide escribirlo en dos columnas."),
    reinforce="Con el documento 2, escribe una cita fiel del dato de abril y calcula cuántas personas menos asistieron en abril que en mayo.",
    extend="Explica por qué una cifra anual y una mensual no se pueden comparar directamente y cómo las igualarías.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (datos de ejemplo). Un panfleto afirma: «El taller de lectura sube las notas.» "
     "En el Liceo X, con taller de lectura voluntario, participan 40 estudiantes y 34 de ellos subieron su promedio. "
     "En el Liceo Y, sin taller, hay 60 estudiantes y 30 subieron su promedio. "
     "Una profesora del Liceo X comenta que quienes se inscribieron en el taller ya eran, en general, muy motivados.")
build(
    O4, 3, F,
    use="Aprenderé a contrastar evidencias a favor y en contra, distinguir evidencia fuerte de débil, detectar correlación sin causa y ajustar la afirmación a lo que los datos permiten.",
    prior=["Sé calcular porcentajes.", "Conozco la diferencia entre correlación y causa.", "Sé qué es una muestra."],
    explain=[
        "Una evidencia es fuerte cuando es pertinente, tiene fuente verificable, suficiente cantidad y un método que descarta otras explicaciones. Es débil cuando trata de otro asunto, es un caso aislado o tiene explicaciones alternativas. Para contrastar se comparan los datos con un punto de referencia: no basta saber que 34 de 40 subieron el promedio; hay que ver cuántos suben en un grupo que no participó.",
        "En el ejemplo, 34 de 40 es 85 % y 30 de 60 es 50 %. La diferencia es grande, pero hay una explicación alternativa: quienes se inscriben en un taller voluntario pueden ser personas más motivadas desde antes. Eso se llama sesgo de autoselección. Los datos muestran que ambas cosas ocurren juntas (correlación), pero no demuestran que el taller sea la causa de la mejora.",
        "Un argumento honesto ajusta su afirmación. En lugar de «el taller sube las notas», puede decir «entre quienes participan en el taller aumentan más a menudo las notas, aunque no se descarta que influya la motivación previa». También considera la contraevidencia: 6 de los 40 no mejoraron. Reconocer la contraevidencia no debilita el argumento: lo hace más creíble y más preciso.",
    ],
    vocab=[("evidencia fuerte", "pertinente, verificable, suficiente y que descarta explicaciones alternativas"), ("evidencia débil", "la que es aislada, impertinente o admite otras explicaciones"), ("punto de referencia", "grupo o dato con el cual se compara"), ("autoselección", "cuando las personas eligen participar y por eso difieren de las que no"), ("contraevidencia", "dato que no apoya o contradice la afirmación"), ("afirmación ajustada", "la que dice solo lo que los datos permiten")],
    worked=[
        ("Calcular y comparar", "En la ficha, ¿qué porcentaje subió su promedio en cada liceo?",
         ["Liceo X: 34 ÷ 40 = 0,85, es decir 85 %.", "Liceo Y: 30 ÷ 60 = 0,5, es decir 50 %."],
         "85 % en X y 50 % en Y"),
        ("Ajustar la afirmación", "Reescribe «el taller sube las notas» para que sea fiel a los datos.",
         ["Los datos muestran que más participantes mejoraron, pero hay una explicación alternativa: la motivación previa.", "La afirmación debe decir que se asocia con mejoras sin probar que las cause."],
         "Entre quienes participaron en el taller, suben las notas más a menudo, aunque no se descarta la motivación previa"),
    ],
    mistakes=[("Afirmar que el taller causó la mejora porque los participantes subieron más.", "Se confunde correlación con causa.", "Pregunta qué otras explicaciones hay y qué dato las descartaría."),
              ("Ocultar la contraevidencia, como los estudiantes que no mejoraron.", "Se cree que reconocerla debilita el argumento.", "Inclúyela y ajusta la afirmación; así gana credibilidad.")],
    T=[
        ("=", "{F} ¿Cuántos de los 60 estudiantes del Liceo Y NO subieron su promedio?", "60-30", "Se resta del total del Liceo Y los que subieron.", " estudiantes"),
        ("=", "{F} ¿Cuántos puntos de porcentaje más tiene el Liceo X que el Liceo Y? Resta el porcentaje de Y (50 %) al de X (85 %).", "85-50", "La diferencia entre los dos porcentajes es 35 puntos.", " puntos de porcentaje"),
        ("=", "{F} ¿Cuántos participantes del taller NO subieron su promedio?", "40-34", "Se resta del total de participantes los que subieron.", " estudiantes"),
        ("abc", "{F} ¿Qué explicación alternativa menciona la profesora?", "Quienes se inscribieron ya estaban muy motivados", "Que las notas se inventaron", "Que el taller es malo", "Plantea una autoselección que podría explicar la mejora."),
        ("abc", "{F} ¿Qué es el punto de referencia en este caso?", "El Liceo Y, sin taller", "El panfleto", "La profesora", "Es el grupo con el que se compara a quienes participaron."),
        ("abc", "{F} ¿Qué muestran los datos?", "Que la mejora y el taller ocurren juntos, sin probar causa", "Que el taller causa la mejora", "Que el taller no sirve", "Muestran una asociación, no la causa."),
        ("ab", "{F} ¿Cuál es una afirmación ajustada?", "Entre quienes participaron, subieron más a menudo las notas, aunque no se descarta la motivación previa", "El taller de lectura sube las notas de cualquier estudiante", "La primera dice solo lo que los datos permiten."),
        ("abc", "{F} ¿Qué dato haría más fuerte la evidencia?", "Comparar las notas de los mismos estudiantes antes y después, con un grupo equivalente sin taller", "Repetir el panfleto con letra más grande", "Preguntar solo a los participantes si les gustó", "Controla la motivación previa con una comparación equivalente."),
        ("abc", "{F} ¿Cuál es la contraevidencia en el Liceo X?", "6 de los 40 participantes no subieron su promedio", "34 participantes subieron su promedio", "El Liceo Y tiene 60 estudiantes", "Son los casos que no apoyan la afirmación."),
        ("abc", "Un anuncio dice: «Quienes toman nuestro jugo tienen menos resfríos». Los datos solo muestran que quienes lo compran son más deportistas. ¿Qué problema hay?", "La relación puede deberse a otra característica, como el deporte", "Que los resfríos no existen", "Que el jugo es caro", "Otra variable podría explicar ambos hechos."),
        ("abc", "{F} Un participante dice: «Aun si hay otras explicaciones, la evidencia del taller es inútil». ¿Qué respuesta es adecuada?", "Es útil como indicio, pero sin concluir que sea la causa", "Tiene razón: una evidencia imperfecta no sirve", "Es prueba total", "Un indicio con límites declarados sigue aportando."),
        ("abc", "Un estudio de ejemplo con 8 personas y otro con 800, elegidas al azar, muestran lo mismo. ¿Cuál sostiene mejor una conclusión general?", "El de 800 elegidas al azar", "El de 8 personas", "Ninguno aporta", "Mayor tamaño y selección aleatoria dan más suficiencia."),
        ("abc", "{F} Si en el Liceo Y 30 de 60 suben el promedio sin taller, ¿qué ocurre con la afirmación del panfleto?", "Pierde fuerza porque la mitad mejora aun sin taller", "Queda probada", "No tiene relación", "Muestra que la mejora ocurre también sin taller."),
    ],
    ctx=("abc", "Un municipio ficticio afirma: «Desde que pusimos cámaras, bajaron los robos de 40 a 30 en la plaza». Otro informe muestra que en las plazas sin cámaras bajaron de 40 a 31. ¿Qué conclusión es prudente?", "Los robos bajaron también donde no hay cámaras, así que no se puede atribuir la baja solo a ellas", "Las cámaras eliminan los robos", "Las cámaras no sirven", "La comparación con plazas sin cámaras debilita la atribución causal."),
    sc=[
        ("En Participación y argumentación: ¿qué es la autoselección?", "Que las personas eligen participar y por eso difieren de las que no", "Puede explicar los resultados sin que la causa sea el programa."),
        ("¿Para qué sirve un punto de referencia?", "Para comparar y saber si el resultado es distinto de lo esperado", "Sin comparación no se sabe si hay diferencia."),
        ("¿Qué es la contraevidencia?", "Un dato que no apoya o contradice la afirmación", "Reconocerla da más credibilidad al argumento y lo vuelve más preciso."),
    ],
    op=("Elige uno. Caso 1: un club ficticio afirma que su programa de ajedrez «mejora las notas de matemática»; datos de ejemplo: de 30 participantes, 24 subieron su promedio; de 90 no participantes, 54 subieron. "
        "Caso 2: una empresa afirma que su aplicación de estudio «aumenta la concentración»; datos de ejemplo: de 50 usuarios, 40 dicen sentir más concentración; de 50 no usuarios, 30 dicen lo mismo. "
        "Calcula los porcentajes, identifica una explicación alternativa y una contraevidencia, y reescribe la afirmación de forma ajustada.",
        "Caso 1. Participantes: 24 de 30 es 80 %. No participantes: 54 de 90 es 60 %. Alternativa: quienes eligen ajedrez podrían estudiar más. Contraevidencia: 6 participantes no subieron. Afirmación ajustada: entre quienes participan en ajedrez, subieron más a menudo las notas, sin probar que el club sea la causa.",
        ["calcula correctamente los porcentajes", "propone una explicación alternativa razonable", "identifica contraevidencia", "ajusta la afirmación a los datos"],
        ["hoja con cálculos, alternativa, contraevidencia y afirmación ajustada"],
        ["afirmar causalidad sin matices", "no comparar con el punto de referencia", "ocultar la contraevidencia"],
        "Pregunta: «¿qué otra cosa podría explicar este resultado?». Si no hay respuesta, sugiere pensar en quién elige participar."),
    reinforce="Con la ficha, escribe otra afirmación ajustada que use la frase «se asocia con» y mencione una limitación.",
    extend="Diseña en tres pasos cómo comprobarías mejor si el taller de lectura mejora las notas.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (modelo de párrafo argumentativo de ejemplo). Estructura: afirmación, evidencia con fuente, garantía, matiz, objeción y respuesta. "
     "Modelo: «Propongo que la feria de Villa Alerce use vasos reutilizables (afirmación). Según un informe municipal de ejemplo, la feria entrega 200 vasos plásticos por fin de semana (evidencia), y reutilizar vasos reduce los residuos que el municipio debe retirar (garantía). "
     "Probablemente un cambio gradual funcione mejor que uno inmediato (matiz). Se podría objetar que lavar vasos es costoso; por eso propongo comenzar con un puesto de lavado compartido (respuesta a la objeción).»")
build(
    O4, 4, F,
    use="Aprenderé a escribir un párrafo argumentativo completo con evidencia, garantía, matiz y respuesta a una objeción, y a evaluar si cada evidencia es pertinente al problema y a la comunidad.",
    prior=["Sé distinguir afirmación, evidencia y garantía.", "Sé ajustar una afirmación a los datos.", "Sé citar una fuente con exactitud."],
    explain=[
        "Un párrafo argumentativo completo organiza sus partes con orden. Comienza con la afirmación que se defiende. Sigue la evidencia, citada con su fuente y su cifra. Luego la garantía, que explica por qué esa evidencia apoya la afirmación. Después un matiz que muestra hasta dónde llega la conclusión, y una objeción posible con su respuesta. Cada parte puede escribirse en una o dos oraciones.",
        "La pertinencia se revisa en dos sentidos. Primero, la evidencia debe tratar del problema y de la comunidad: datos sobre vasos en una feria apoyan decisiones de la feria, no sobre un colegio. Segundo, debe ser suficiente para el alcance de la afirmación. Si se afirma algo muy general, se necesita más evidencia; si la afirmación es acotada («empezar con un puesto»), una evidencia modesta puede bastar.",
        "Antes de entregar un texto, se hace una revisión: ¿cada dato tiene fuente? ¿la garantía conecta de verdad? ¿el matiz es honesto? ¿la objeción es la más fuerte, no una débil elegida para ganar? Responder a la mejor objeción, y no a una caricatura, es lo que hace creíble una argumentación. Si la objeción tiene razón, la respuesta puede ajustar la propuesta en vez de rechazarla.",
    ],
    vocab=[("párrafo argumentativo", "texto breve que defiende una afirmación con evidencia y garantía"), ("matiz", "expresión que gradúa la fuerza de la conclusión"), ("objeción", "razón que cuestiona la propuesta"), ("respuesta a la objeción", "reacción con razones o con un ajuste a la propuesta"), ("alcance", "qué tan general es lo que se afirma"), ("revisión", "relectura crítica antes de entregar un texto")],
    worked=[
        ("Rotular el modelo", "En la ficha, ¿qué parte es «lavar vasos es costoso»?",
         ["La frase plantea una razón que cuestiona la propuesta.", "Por eso es la objeción, y la respuesta es el puesto de lavado compartido."],
         "La objeción"),
        ("Calcular con la evidencia", "Si la feria entrega 200 vasos por fin de semana, ¿cuántos entrega en 4 fines de semana?",
         ["Se multiplica la cantidad semanal por 4.", "200 × 4 = 800."],
         "800 vasos"),
    ],
    mistakes=[("Responder a una objeción inventada y débil para quedar bien.", "Se prefiere ganar la discusión que mejorar la propuesta.", "Elige la objeción más fuerte que podría hacer una persona razonable."),
              ("Afirmar algo muy general con una evidencia pequeña.", "No se compara el alcance con la cantidad de datos.", "Acota la afirmación o consigue más evidencia.")],
    T=[
        ("abc", "{F} ¿Cuál es la afirmación del modelo?", "La feria debería usar vasos reutilizables", "Lavar vasos es costoso", "La feria entrega 200 vasos plásticos", "Es lo que se defiende en el párrafo."),
        ("abc", "{F} ¿Cuál es la evidencia del modelo?", "El informe municipal indica 200 vasos plásticos por fin de semana", "Un cambio gradual funcionará mejor", "Lavar vasos es costoso", "Es el dato con fuente que respalda la propuesta."),
        ("abc", "{F} ¿Qué parte es «probablemente un cambio gradual funcione mejor»?", "El matiz", "La garantía", "La objeción", "Gradúa la fuerza de la conclusión."),
        ("=", "{F} ¿Cuántos vasos plásticos entrega la feria en 6 fines de semana, según el informe?", "200*6", "Se multiplica 200 vasos por 6 fines de semana.", " vasos"),
        ("abc", "{F} ¿Qué respuesta da el modelo a la objeción?", "Comenzar con un puesto de lavado compartido", "Negar que haya costos", "Ignorarla", "Ajusta la propuesta para atender la objeción."),
        ("abc", "{F} ¿Cuál es la garantía del modelo?", "Reutilizar vasos reduce los residuos que el municipio debe retirar", "La feria existe", "Los vasos son plásticos", "Une el dato de los vasos con la propuesta."),
        ("ab", "{F} Un estudiante quiere sustituir la evidencia por «mi tío piensa que es buena idea». ¿Es pertinente?", "No: es una opinión personal sin datos sobre el problema", "Sí: toda opinión sirve como evidencia", "No aporta información verificable sobre la cantidad de vasos."),
        ("abc", "{F} ¿Qué objeción más fuerte podría hacerse en lugar de la que está?", "Que los usuarios podrían no devolver los vasos reutilizables", "Que los vasos reutilizables se ven menos modernos", "Que a algunas personas les gusta el plástico", "Cuestiona un punto central de la propuesta."),
        ("abc", "{F} ¿Qué añadirías para responder a la objeción de los vasos no devueltos?", "Un depósito reembolsable al devolver el vaso", "Que la objeción no importa", "Quitar la propuesta sin explicar", "Es un ajuste que aborda la objeción."),
        ("abc", "Alguien escribe: «Todas las ferias del país deberían prohibir el plástico», usando solo los datos de una feria. ¿Qué problema tiene?", "El alcance supera lo que los datos permiten", "Es muy corta", "Usa cifras", "Una evidencia local no sostiene una afirmación nacional."),
        ("abc", "{F} ¿Qué cambio hace el matiz más honesto?", "«Probablemente un cambio gradual funcione mejor que uno inmediato»", "«Está demostrado que todo cambio funciona siempre»", "«No sé nada»", "Expresa el grado de certeza de modo proporcionado."),
        ("abc", "{F} Se cambia la evidencia por «en el liceo se usan 50 vasos por semana». ¿Es pertinente al caso de la feria?", "No: trata de otra comunidad", "Sí: tiene la palabra vasos", "Sí: las cifras siempre sirven", "La pertinencia exige datos del problema y de la comunidad discutidos."),
        ("abc", "¿Cuál es la mejor revisión final de un párrafo argumentativo?", "Comprobar fuentes, garantía, matiz y la objeción más fuerte", "Agregar más adjetivos", "Hacer el texto lo más largo posible", "Esas revisiones aseguran la calidad del argumento."),
    ],
    ctx=("abc", "Un grupo ficticio escribe: «Hay que abrir el gimnasio los domingos, pues un informe municipal de ejemplo dice que 90 de 120 familias consultadas lo apoyan». ¿Qué falta para completar el párrafo?", "La garantía, el matiz y la respuesta a una objeción", "Más adjetivos", "Quitar la cifra", "Faltan partes que conectan la evidencia con la propuesta y la hacen creíble."),
    sc=[
        ("En Participación y argumentación: ¿qué hace un matiz?", "Gradúa la fuerza de la conclusión", "Dice hasta dónde llegan las razones."),
        ("¿Qué objeción conviene responder?", "La más fuerte que haría una persona razonable", "Responder a una débil no mejora la propuesta."),
        ("=", "Si una feria entrega 150 bolsas por fin de semana, ¿cuántas entrega en 5 fines de semana?", "150*5", "Se multiplica la cantidad semanal por los 5 fines de semana."),
    ],
    op=("Elige uno. Caso 1: el liceo debería abrir la biblioteca los sábados por la mañana; datos de ejemplo: de 120 estudiantes consultados, 78 dicen que irían. Caso 2: el barrio debería instalar contenedores de reciclaje; datos de ejemplo: un informe municipal indica que se retiran 30 bolsas de basura por semana de la plaza. "
        "Escribe un párrafo argumentativo de seis a ocho oraciones con afirmación, evidencia con fuente y cifra, garantía, matiz y respuesta a una objeción fuerte.",
        "Caso 1. «Propongo abrir la biblioteca los sábados por la mañana. Según una consulta de ejemplo del liceo, 78 de 120 estudiantes, es decir, 65 %, dicen que irían. Un servicio debería abrir cuando quienes lo usan pueden asistir. Probablemente la asistencia varíe según la época del año. Se podría objetar que faltará personal; por eso propongo una prueba de seis sábados con un turno voluntario.»",
        ["incluye las seis partes", "usa evidencia con fuente y cifra exacta", "responde a una objeción fuerte con un ajuste o razón", "el matiz es honesto"],
        ["párrafo de seis a ocho oraciones con las partes rotuladas"],
        ["omitir la garantía", "elegir una objeción débil", "afirmar algo más general que los datos"],
        "Pregunta: «¿cuál es la objeción más fuerte a tu propuesta?». Pide reescribir si eligió una débil."),
    reinforce="Escribe una oración de garantía para la evidencia «30 bolsas de basura por semana en la plaza» y la afirmación «instalar contenedores de reciclaje».",
    extend="Reescribe tu párrafo para dirigirlo a una comunidad distinta, como el municipio, cambiando el tipo de evidencia que priorizas.",
)

# ============================================================ OAC-05, clase 1
F = ("Ficha 5 (cuatro situaciones de ejemplo). Situación 1: carta formal a la dirección del liceo para pedir una sala de estudio. Situación 2: intervención de un minuto en la asamblea de curso para proponer una salida pedagógica. "
     "Situación 3: mensaje en el chat del curso para invitar a limpiar el patio el viernes. Situación 4: columna de opinión en el diario mural sobre el uso de celulares.")
build(
    O5, 1, F,
    use="Aprenderé a reconocer los ámbitos de participación, sus comunidades y propósitos (pedir, informar, convencer, invitar) y a elegir forma de argumentar, tipo de evidencia y registro adecuados a cada situación.",
    prior=["Sé qué es un ámbito de participación y una comunidad discursiva.", "Sé distinguir afirmación, evidencia y garantía.", "Sé que el registro cambia según la situación."],
    explain=[
        "Cada situación de participación tiene un propósito: pedir algo, informar, convencer, invitar, proponer o responder. El propósito decide qué se dice y cómo. Una carta formal para pedir una sala debe explicar la necesidad, aportar evidencia y formular una petición clara. Un mensaje de invitación debe ser breve, amable y concreto: día, hora, lugar y para qué. Confundir el propósito produce textos que no logran lo que buscan.",
        "También importa quién escucha o lee, es decir, la comunidad discursiva. A una dirección se le habla con respeto formal y con datos verificables; a compañeras y compañeros, con cercanía; a una asamblea, con claridad y tiempos acotados. La extensión y el registro cambian. Lo que no cambia es la veracidad: no se exageran datos ni se inventan razones para agradar.",
        "Por último, cada situación admite distintas formas de legitimar. En una carta formal pesan los datos y los documentos. En una intervención oral breve, una cifra clave y un ejemplo claro. En un chat, la urgencia y la utilidad. En una columna de opinión, argumentos desarrollados con evidencia y una postura declarada. Antes de escribir conviene preguntarse: ¿para qué, para quién, dónde y con qué razones?",
    ],
    vocab=[("propósito", "lo que se busca lograr con un texto o intervención"), ("destinatario", "persona o grupo a quien se dirige un mensaje"), ("registro formal", "forma de hablar o escribir respetuosa, precisa y sin coloquialismos"), ("registro cercano", "forma de comunicarse más próxima, propia de personas de confianza"), ("petición", "solicitud clara y concreta de algo"), ("columna de opinión", "texto que defiende una postura con argumentos")],
    worked=[
        ("Identificar el propósito", "En la situación 3 (invitar a limpiar el patio), ¿cuál es el propósito principal y qué debe incluir el mensaje?",
         ["El propósito es invitar a participar en una actividad.", "Debe incluir día, hora, lugar y para qué se hace, de forma breve y amable."],
         "Invitar; incluir día, hora, lugar y finalidad"),
        ("Elegir el registro", "¿Qué registro conviene para la carta a la dirección?",
         ["La dirección es una autoridad del liceo y el texto es una petición oficial.", "Corresponde un registro formal, con datos verificables."],
         "Registro formal con datos verificables"),
    ],
    mistakes=[("Escribir con el mismo tono a la dirección y a los compañeros.", "No se piensa en quién lee.", "Antes de escribir, anota destinatario, propósito y registro."),
              ("Cambiar los datos para que el texto convenza más al público.", "Se confunde adaptar con distorsionar.", "Cambia la forma, el orden y el énfasis, nunca la veracidad de los hechos.")],
    T=[
        ("abc", "{F} ¿Cuál es el propósito de la situación 1?", "Pedir una sala de estudio", "Invitar a una actividad", "Contar una anécdota", "Una carta formal busca una petición concreta."),
        ("abc", "{F} ¿Cuál es el propósito de la situación 2?", "Proponer una salida pedagógica y convencer al curso", "Pedir una autorización escrita a la dirección", "Invitar a una jornada de limpieza", "Es una intervención oral en la asamblea para proponer algo a las compañeras y compañeros."),
        ("abc", "{F} ¿Qué situación requiere desarrollar argumentos con evidencia y una postura declarada?", "La situación 4, la columna de opinión", "La situación 3, el mensaje del chat", "La situación 2, de un minuto", "La columna tiene espacio para desarrollar su postura."),
        ("abc", "{F} ¿Qué situación tiene la extensión más limitada?", "La situación 2, de un minuto", "La situación 1", "La situación 4", "La intervención oral solo dura un minuto."),
        ("abc", "{F} ¿A quién se dirige principalmente la situación 2?", "A compañeras y compañeros de la asamblea de curso", "A la dirección del liceo", "A las familias del liceo", "Es una intervención dentro de la asamblea de curso."),
        ("abc", "{F} ¿Qué registro es adecuado en la situación 3?", "Cercano y amable", "Burocrático y extenso", "Agresivo", "Se invita a personas del mismo grupo con tono próximo."),
        ("ab", "{F} Para la intervención de un minuto, ¿qué es mejor?", "Una cifra clave y un ejemplo claro", "Veinte datos sin ordenar", "Con poco tiempo se priorizan pocas razones claras."),
        ("abc", "¿Qué debe permanecer igual cuando adaptas un mensaje a distintas comunidades?", "La veracidad de los hechos", "Las palabras exactas", "El largo del texto", "Adaptar cambia la forma, no los hechos."),
        ("abc", "{F} Una estudiante escribe en la carta formal: «Oye, director, necesitamos una sala porque sí». ¿Qué corregirías primero?", "El registro y la falta de razones", "El tamaño de la hoja", "El día de entrega", "El texto no es formal y no entrega evidencia."),
        ("abc", "{F} Un mensaje de invitación dice solo «Limpiemos el patio». ¿Qué falta?", "Día, hora, lugar y finalidad", "Una cita larga", "Cifras de presupuesto", "Una invitación necesita datos prácticos para participar."),
        ("abc", "{F} ¿Qué tipo de evidencia pesa más en la columna de opinión sobre celulares?", "Datos verificables y ejemplos que sostengan la postura", "Insultos a quienes piensan distinto", "Solo la fama de quien escribe", "Una columna argumentada requiere evidencia revisable."),
        ("abc", "Una nota para las familias sobre una salida pedagógica y otra para el equipo directivo con la misma salida. ¿Qué deben compartir?", "La misma información veraz sobre fecha, costo y objetivo", "El mismo tono", "La misma extensión", "Se adapta la forma, no el contenido de los hechos."),
        ("abc", "{F} Si el propósito es convencer, ¿qué conviene incluir?", "Razones y evidencia pertinentes para quien escucha", "Solo la insistencia", "Amenazas", "Persuadir exige razones que la comunidad pueda evaluar."),
    ],
    ctx=("abc", "Una dirigente ficticia debe pedir permiso al municipio para usar la plaza el sábado y, además, avisar a sus vecinos. ¿Qué diferencia debería tener cada texto?", "El permiso, formal y con detalles verificables; el aviso, cercano y breve", "Los dos iguales y formales", "Los dos con humor", "Cambian el registro y la extensión según destinatario y propósito."),
    sc=[
        ("En Participación y argumentación: ¿qué es el propósito de un texto?", "Lo que se busca lograr con él", "Define qué se dice y cómo."),
        ("¿Qué preguntas conviene hacerse antes de escribir?", "Para qué, para quién, dónde y con qué razones", "Así se elige propósito, registro y evidencia."),
        ("¿Qué no debe cambiar al adaptar un mensaje a otra comunidad?", "La veracidad de los hechos", "Se cambia la forma, no los hechos."),
    ],
    op=("Elige uno. Debes comunicar que el liceo tendrá una jornada de limpieza el viernes de 15:00 a 17:00 en el patio. Escribe (a) un mensaje de chat para el curso y (b) un párrafo para una carta formal a la dirección que pide autorización y herramientas de aseo. "
        "Caso alternativo: comunicar que el taller de lectura necesita más participantes (un mensaje a los cursos y una nota para la profesora jefa). "
        "Indica en cada texto propósito, destinatario, registro y evidencia o dato clave, sin cambiar los hechos entre uno y otro.",
        "(a) «Curso: este viernes de 15:00 a 17:00 limpiamos el patio para tener un recreo más agradable. Lleva ropa cómoda. ¡Los esperamos!». (b) «Solicitamos autorización para una jornada de limpieza el viernes de 15:00 a 17:00 y el préstamo de guantes y bolsas, para mejorar el uso del patio.» Mismo hecho, distinto registro y propósito.",
        ["identifica propósito y destinatario de cada texto", "usa registros adecuados", "mantiene los hechos sin cambios", "incluye lo indispensable en cada caso"],
        ["dos textos con una tabla de propósito, destinatario y registro"],
        ["usar el mismo tono en ambos", "olvidar día, hora o lugar", "cambiar los hechos entre un texto y otro"],
        "Pregunta: «¿qué dato es indispensable para que esta persona actúe?». Pide revisar que aparezca."),
    reinforce="Elige una situación de la ficha y escribe su propósito, su destinatario y el registro que usarías en una línea cada uno.",
    extend="Explica qué puede perderse si una carta formal se escribe como un mensaje de chat, y cómo repararlo.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 6 (mensaje base y datos de ejemplo). Mensaje base: «El liceo debería ofrecer talleres en la tarde.» "
     "Datos de ejemplo: 120 estudiantes se quedan sin actividades después de las 15:00; en una consulta a 30 familias, 21 apoyan los talleres; hay 4 docentes interesados en dirigir uno; hay dos salas libres entre las 15:00 y las 17:00. "
     "Destinatarios posibles: la dirección del liceo, las familias o el estudiantado.")
build(
    O5, 2, F,
    use="Aprenderé a adaptar un mismo mensaje a distintas comunidades (dirección, familias, estudiantes) escogiendo los datos, el tipo de razones y el registro que cada una puede evaluar, sin cambiar los hechos.",
    prior=["Sé identificar propósito y destinatario.", "Sé elegir evidencia pertinente.", "Sé calcular un porcentaje."],
    explain=[
        "Un mismo mensaje puede dirigirse a comunidades con preocupaciones distintas. La dirección piensa en viabilidad: recursos, personas disponibles, responsabilidades y reglamento. Las familias piensan en seguridad, horarios, traslados y costos. El estudiantado piensa en intereses, tiempo libre y utilidad. Un argumento pertinente selecciona, de todos los datos disponibles, los que responden a las preocupaciones de quien escucha.",
        "Seleccionar no es ocultar. No se omiten datos que cambien la conclusión, como los costos o los riesgos, solo para convencer. Se decide qué destacar y en qué orden, y se mantiene en el texto lo esencial para que la persona decida con información. Si hay un límite, como que solo hay dos salas libres, se declara y se propone cómo manejarlo.",
        "Para cada comunidad también cambia la forma de legitimar: a la dirección se le muestran documentos, cifras y un plan; a las familias, testimonios y compromisos de cuidado; a los estudiantes, ejemplos concretos y beneficios. El registro varía, pero las cifras son las mismas: si 21 de 30 familias apoyan los talleres, eso es el 70 % de las consultadas, para todos los destinatarios.",
    ],
    vocab=[("viabilidad", "posibilidad real de llevar a cabo algo"), ("preocupación del destinatario", "aspecto que le importa a quien escucha"), ("seleccionar datos", "escoger aquellos más pertinentes para esa comunidad"), ("omitir", "dejar fuera un dato; no debe hacerse con datos que cambian la conclusión"), ("plan", "conjunto ordenado de pasos para realizar algo"), ("compromiso de cuidado", "acuerdo sobre quién supervisará y protegerá")],
    worked=[
        ("Seleccionar para la dirección", "Con la ficha, ¿qué datos priorizarías para la dirección?",
         ["La dirección se preocupa por la viabilidad.", "Priorizaría: cuatro docentes interesados, dos salas libres y 120 estudiantes sin actividades."],
         "Docentes interesados, salas libres y estudiantes sin actividad"),
        ("Cuidar la veracidad", "Para las familias, ¿cómo expresar que 21 de 30 familias apoyan?",
         ["21 ÷ 30 = 0,7, es decir 70 %.", "Se dice «21 de las 30 familias consultadas apoyan los talleres (70 %)», sin decir «casi todas»."],
         "70 % de las 30 familias consultadas"),
    ],
    mistakes=[("Omitir un dato que cambia la conclusión, como el costo, solo para convencer.", "Se confunde seleccionar con ocultar.", "Declara los límites y propone cómo manejarlos."),
              ("Decir que la consulta representa a todas las familias del liceo.", "Se generaliza más allá de las 30 familias consultadas.", "Cita cuántas fueron consultadas y declara el límite.")],
    T=[
        ("=", "{F} ¿Cuántas de las 30 familias consultadas no figuran entre las que apoyan los talleres?", "30-21", "Se resta del total consultado las familias que apoyan.", " familias"),
        ("abc", "{F} ¿Qué preocupación principal tiene la dirección?", "La viabilidad: docentes, salas y recursos", "Los gustos musicales", "El color de las salas", "La dirección debe garantizar que se pueda llevar a cabo."),
        ("abc", "{F} ¿Qué preocupación principal tienen las familias?", "Seguridad, horarios y traslados", "Las notas del vecino", "Las marcas de ropa", "Es lo que influye en autorizar la participación."),
        ("abc", "{F} ¿Qué dato destacarías para el estudiantado?", "Las actividades posibles y que habría tiempo útil después de las 15:00", "El reglamento completo", "El presupuesto municipal", "Responde a sus intereses y tiempo libre."),
        ("abc", "{F} ¿Qué dato es clave para la dirección?", "Hay 4 docentes interesados y dos salas libres", "Que el mensaje tiene 12 palabras", "Que el liceo queda lejos", "Muestra que hay recursos para empezar."),
        ("abc", "{F} ¿Qué límite debe declararse a la dirección?", "Que solo hay dos salas libres entre las 15:00 y las 17:00", "Que no hay estudiantes", "Que los docentes no existen", "Un límite real se declara y se maneja."),
        ("ab", "{F} Al escribir a las familias, ¿cuál es la forma fiel de citar la consulta?", "«21 de las 30 familias consultadas apoyan los talleres»", "«Todas las familias apoyan los talleres»", "La primera conserva las cifras reales; la segunda exagera."),
        ("abc", "{F} ¿Qué legitimación conviene para la dirección?", "Documentos y cifras, con un plan de funcionamiento", "Un rumor de pasillo", "Una frase popular", "Una autoridad espera datos verificables y un plan."),
        ("abc", "{F} ¿Qué legitimación conviene para las familias?", "Un compromiso de cuidado y supervisión, además de los datos", "Una burla a quien duda", "Solo una frase emotiva", "La seguridad de sus hijos es su preocupación."),
        ("abc", "{F} Un estudiante propone ocultar a las familias que los talleres terminan a las 17:00. ¿Qué piensas?", "No es correcto: el horario es un dato que influye en la decisión", "Es correcto: si no preguntan, no se dice", "Es mejor decir que terminan antes", "Ocultar datos relevantes distorsiona la decisión de las familias."),
        ("abc", "{F} Si cada taller ocupa una sala y solo hay dos salas libres en ese horario, ¿cuántos talleres pueden funcionar a la vez?", "2", "4", "120", "Hay dos salas libres y cada taller usa una; los docentes interesados no aumentan las salas."),
        ("abc", "{F} Un mensaje a la dirección dice: «Hay 120 estudiantes sin actividad, 4 docentes disponibles y 2 salas libres; propongo comenzar con dos talleres». ¿Qué ventaja tiene?", "Prioriza la viabilidad y propone un paso inicial acotado", "Es muy extenso", "Oculta la información", "Es breve y responde a la preocupación de la dirección."),
        ("abc", "{F} Una nota para estudiantes dice: «Hay talleres para ti». ¿Qué le falta?", "Qué tipo de talleres, días y horarios", "Más adjetivos", "Una ley", "Para que alguien se inscriba necesita datos concretos."),
    ],
    ctx=("abc", "Una comisión ficticia debe explicar un cambio de la hora de salida del bus escolar a madres y padres, y al equipo del liceo. ¿Qué debería ser común a ambos mensajes?", "La hora real del cambio y el motivo", "El mismo tono", "Los mismos ejemplos", "Los hechos son iguales aunque cambie la forma de contarlos."),
    sc=[
        ("En Participación y argumentación: ¿qué significa seleccionar datos para una comunidad?", "Elegir los más pertinentes a lo que le preocupa", "No equivale a ocultar datos relevantes."),
        ("¿Qué preocupa principalmente a una dirección escolar al evaluar una propuesta?", "Su viabilidad: recursos, personas y reglamento", "Debe poder llevar a cabo lo propuesto con lo que tiene."),
        ("=", "Si 15 de 20 estudiantes consultados apoyan una actividad, ¿qué porcentaje es?", "15*100//20", "15 de 20 equivale a 75 por cada 100.", " %"),
    ],
    op=("Elige uno. Mensaje base A: «El liceo debería tener un día de intercambio de libros». Datos de ejemplo: 60 estudiantes dicen que tienen libros que no usan; la biblioteca ofrece una mesa gratis; hace falta un voluntario por turno. "
        "Mensaje base B: «El barrio debería tener una feria de trueque mensual». Datos de ejemplo: 25 de 40 vecinos consultados la apoyan; la junta tiene un salón libre los domingos; falta decidir quién la supervisa. "
        "Escribe dos versiones del mensaje, para dos comunidades distintas, destacando datos distintos y manteniendo los mismos hechos. Declara un límite en cada versión.",
        "Mensaje A. Dirección: «Proponemos un día de intercambio de libros; 60 estudiantes tienen libros sin usar, la biblioteca ofrece una mesa y necesitamos un voluntario por turno. Falta definir quién supervisa». Estudiantes: «¿Tienes libros que ya leíste? Tráelos y llévate otros. Habrá una mesa en la biblioteca; hay turnos de voluntarios».",
        ["adapta los datos a la preocupación de cada comunidad", "mantiene los hechos y las cifras", "declara un límite en cada versión", "usa el registro adecuado"],
        ["dos versiones del mensaje con una nota sobre los datos elegidos"],
        ["cambiar las cifras entre versiones", "omitir un dato que cambia la conclusión", "usar el mismo registro con todos"],
        "Pregunta: «¿qué cifra repetiste en las dos versiones sin cambiarla?». Si ninguna, revisa los hechos."),
    reinforce="Con la ficha, escribe una oración para la dirección y otra para el estudiantado, con la misma cifra de 120 estudiantes.",
    extend="Explica la diferencia entre adaptar un mensaje y manipular a la audiencia, con un ejemplo.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 7 (cinco argumentos breves de ejemplo). Argumento 1: «En el taller de teatro del año pasado participaron 25 estudiantes y todos terminaron la obra; por eso este año también funcionará.» "
     "Argumento 2: «Cerrar la calle los sábados es como cerrar una plaza para ferias: permite que la gente camine y compre con calma.» "
     "Argumento 3: «Si no se arregla el techo, entrará agua en invierno y se dañarán los libros.» "
     "Argumento 4: «La arquitecta del municipio indica que este techo requiere reparación antes del invierno.» "
     "Argumento 5: «Una encuesta de ejemplo a 100 usuarios mostró que 80 quieren más horas de apertura.»")
build(
    O5, 3, F,
    use="Aprenderé distintas formas de argumentar (por ejemplo, analogía, causa y consecuencia, autoridad, datos) y a elegir la más pertinente según el propósito y la comunidad.",
    prior=["Sé qué es una evidencia.", "Sé que la autoridad debe tener experticia.", "Sé reconocer un argumento y sus partes."],
    explain=[
        "Hay formas típicas de argumentar. Por ejemplos o casos: se apoya una idea con experiencias previas. Por analogía: se compara con una situación parecida («es como…»). Por causa y consecuencia: se dice que algo lleva a algo («si no se arregla el techo, se dañarán los libros»). Por autoridad: se cita a quien tiene experticia. Por datos: se presentan cifras verificables. Cada forma tiene fortalezas y riesgos.",
        "Las fortalezas dependen del propósito y la comunidad. Los datos convencen a quien debe decidir con criterios técnicos. Las consecuencias motivan a actuar cuando hay urgencia. Los ejemplos hacen comprensible una idea a un público amplio. La autoridad sirve si es pertinente. La analogía ayuda a comprender, pero solo es fuerte si las situaciones comparadas se parecen en lo que importa; si no, es débil.",
        "Los riesgos también se evalúan. Un ejemplo aislado no prueba una regla general. Una consecuencia debe ser verosímil y no exagerada. Una analogía se debilita si hay diferencias importantes. Lo mejor es combinar formas: un dato, una consecuencia y un ejemplo. Al elegir, se pregunta: ¿qué razón puede evaluar esta comunidad y cuál es la más adecuada para este propósito?",
    ],
    vocab=[("argumento por ejemplos", "apoya una idea en casos o experiencias previas"), ("analogía", "comparación entre dos situaciones parecidas"), ("argumento por consecuencias", "señala los efectos probables de actuar o no actuar"), ("argumento de autoridad", "se apoya en una persona o institución experta"), ("argumento por datos", "se apoya en cifras verificables"), ("verosímil", "creíble, que podría ocurrir")],
    worked=[
        ("Reconocer la forma", "¿Qué forma de argumentar usa el argumento 3?",
         ["Dice qué ocurrirá si no se hace algo: se dañarán los libros.", "Es un argumento por consecuencias."],
         "Por consecuencias"),
        ("Evaluar una analogía", "El argumento 2 compara cerrar una calle con cerrar una plaza para ferias. ¿Cuándo sería fuerte?",
         ["Una analogía es fuerte si las situaciones se parecen en lo que importa.", "Aquí importaría que ambas permitan caminar y comprar con calma, y que una calle no tenga problemas distintos, como ambulancias o buses."],
         "Es fuerte si no hay diferencias importantes entre ambas situaciones"),
    ],
    mistakes=[("Usar una analogía sin revisar las diferencias entre las situaciones.", "Se queda con el parecido y se ignora lo distinto.", "Pregunta en qué se diferencian las situaciones y si esa diferencia importa."),
              ("Creer que un ejemplo exitoso prueba que siempre funcionará.", "Se generaliza desde un solo caso.", "Presenta el ejemplo como indicio y busca más casos o datos.")],
    T=[
        ("abc", "{F} ¿Qué forma de argumentar usa el argumento 1?", "Por ejemplos o casos previos", "Por autoridad", "Por analogía", "Se apoya en lo que ocurrió el año pasado."),
        ("abc", "{F} ¿Qué forma usa el argumento 2?", "Por analogía", "Por datos", "Por autoridad", "Compara dos situaciones con «es como»."),
        ("abc", "{F} ¿Qué forma usa el argumento 4?", "Por autoridad", "Por consecuencias", "Por ejemplos", "Cita a una arquitecta con experticia en la materia."),
        ("abc", "{F} ¿Qué forma usa el argumento 5?", "Por datos", "Por analogía", "Por autoridad", "Presenta una cifra de una encuesta."),
        ("abc", "{F} ¿Cuál es el principal riesgo del argumento 1?", "Generalizar desde un solo año", "Usar cifras", "Citar a una persona", "Un caso previo no garantiza que ocurra lo mismo."),
        ("abc", "{F} ¿Cuándo es fuerte la analogía del argumento 2?", "Cuando ambas situaciones se parecen en lo que importa", "Siempre", "Nunca", "Se evalúa si las diferencias importan."),
        ("abc", "{F} ¿Qué se debe revisar en el argumento 3?", "Que la consecuencia sea verosímil y no exagerada", "Que no tenga verbo", "Que cite una ley", "Una consecuencia exagerada o poco creíble pierde fuerza argumentativa."),
        ("ab", "{F} Para el argumento 4, ¿qué hace falta para que sea una autoridad legítima?", "Que su experticia sea en la reparación de techos y que se pueda verificar", "Que sea una persona simpática", "La autoridad exige experticia pertinente y verificable."),
        ("abc", "{F} ¿Qué argumento convence más a un comité que decide con criterios técnicos?", "El 5, por datos, y el 4, por autoridad pertinente", "El 2, por analogía", "El 1, por un caso previo", "Un comité técnico valora datos y experticia verificables."),
        ("abc", "{F} Se debe motivar a la comunidad a reparar rápido el techo. ¿Qué argumento destaca la urgencia?", "El 3, porque señala una consecuencia", "El 1", "El 2", "Describe lo que ocurrirá si no se actúa."),
        ("=", "{F} Si la encuesta del argumento 5 hubiera sido a 200 usuarios y 120 estuvieran a favor, ¿qué porcentaje sería?", "120*100//200", "120 de 200 equivale a 60 por cada 100.", " %"),
        ("abc", "{F} Alguien reemplaza el argumento 2 por: «Cerrar una calle es como cerrar una escuela». ¿Qué ocurre con la analogía?", "Se debilita porque ambas situaciones se parecen poco en lo que importa", "Se fortalece", "Se mantiene igual", "Una escuela y una calle cumplen funciones muy distintas."),
        ("abc", "¿Cuál es la mejor combinación para convencer a la dirección de reparar el techo?", "Un dato de daños, la opinión de una arquitecta y una consecuencia verosímil", "Solo una frase emotiva", "Solo una analogía con otro edificio", "Combina datos, autoridad y consecuencias, que la dirección puede evaluar."),
    ],
    ctx=("abc", "Una dirigente ficticia quiere convencer a un comité técnico de instalar luminarias, y luego a sus vecinos para que participen en una jornada de limpieza. ¿Qué combinación es más adecuada?", "Para el comité, datos de oscuridad y accidentes; para los vecinos, ejemplos y consecuencias", "Para ambos solo una analogía", "Para ambos solo autoridad", "Cada comunidad evalúa mejor un tipo de razones."),
    sc=[
        ("En Participación y argumentación: ¿qué es un argumento por analogía?", "Comparar con otra situación parecida", "Es fuerte si se parecen en lo que importa."),
        ("¿Qué riesgo tiene argumentar con un solo ejemplo?", "Generalizar sin base suficiente", "Un caso no prueba una regla general."),
        ("¿Qué debe cumplir una autoridad para ser pertinente?", "Experticia en el tema y posibilidad de verificarla", "No basta cualquier cargo o título sin experticia pertinente."),
    ],
    op=("Elige uno. Debes convencer de crear un espacio de estudio en el liceo (caso 1) o de instalar un contenedor de reciclaje en la plaza (caso 2) a una comunidad que decide con criterios técnicos. "
        "Datos de ejemplo del caso 1: 90 estudiantes de 120 consultados dicen que estudian en casa con dificultades; una profesora de matemática confirma que muchos no tienen escritorio; la biblioteca cierra a las 17:00. "
        "Datos del caso 2: 30 bolsas de basura semanales; una encargada de aseo del municipio dice que hay camiones disponibles; en otra plaza ficticia, un contenedor redujo la basura en bolsas. "
        "Escribe tres argumentos de formas distintas (datos, autoridad y consecuencia o analogía) y di cuál priorizarías y por qué.",
        "Caso 1. Datos: 90 de 120 estudiantes (75 %) dicen que estudian con dificultades. Autoridad: una profesora de matemática confirma que muchos no tienen escritorio. Consecuencia: si no hay un espacio, seguirán estudiando en peores condiciones. Priorizaría los datos para un comité técnico.",
        ["escribe tres formas distintas de argumentar", "usa los datos dados sin modificarlos", "prioriza una forma con razones según la comunidad"],
        ["tres argumentos rotulados y una justificación de prioridad"],
        ["usar la misma forma tres veces", "exagerar consecuencias", "citar una autoridad sin experticia"],
        "Pregunta: «¿qué tipo de razón puede evaluar mejor esta comunidad?». Pide explicar su elección."),
    reinforce="Elige un argumento de la ficha y reescríbelo con otra forma de argumentar, por ejemplo cambiando una analogía por un dato.",
    extend="Explica una situación en que un argumento por consecuencias sería inadecuado porque exageraría el riesgo.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 8 (borrador de carta formal, de ejemplo). «Hola, director. Queremos que nos presten la sala 4 para estudiar en las tardes, porque es bacán y todos lo queremos. "
     "Muchos estudiantes no tienen dónde estudiar. Esperamos su respuesta pronto. Chao.» "
     "Datos disponibles: una consulta de ejemplo a 120 estudiantes mostró que 78 no tienen un lugar tranquilo para estudiar en casa; la sala 4 está libre entre las 15:00 y las 17:00; un inspector se ofreció para abrir y cerrar.")
build(
    O5, 4, F,
    use="Aprenderé a elaborar y mejorar una intervención o carta formal usando la estructura, el registro y la legitimación del conocimiento adecuados al ámbito, la comunidad y el propósito.",
    prior=["Sé elegir evidencia pertinente para una comunidad.", "Sé distinguir registro formal y cercano.", "Sé citar datos con exactitud."],
    explain=[
        "Una carta formal tiene partes: saludo adecuado, presentación de quién escribe y para qué, desarrollo con las razones y la evidencia, petición concreta, compromiso o propuesta de cuidado y cierre respetuoso con despedida. Cada parte cumple una función: el saludo muestra respeto, el desarrollo convence, la petición permite actuar, el cierre mantiene la relación.",
        "El registro formal evita expresiones coloquiales («bacán»), frases vagas («todos lo queremos») y un tono exigente («pronto»). En su lugar usa frases precisas: «solicitamos», «agradeceríamos». La legitimación del conocimiento también es formal: se citan los datos con su fuente y cifra exacta («según una consulta de ejemplo a 120 estudiantes, 78 no cuentan con un lugar tranquilo para estudiar en casa»).",
        "En una intervención oral breve la estructura se simplifica: saludo, afirmación, un dato clave, una garantía y una petición, con tiempos controlados. Revisar el borrador significa preguntarse: ¿se entiende qué pide, a quién y por qué? ¿hay evidencia? ¿está el registro adecuado? ¿se ofrece una solución a la preocupación de la persona que decide? Mejorar un texto es parte de participar bien.",
    ],
    vocab=[("saludo formal", "fórmula de respeto al iniciar una carta"), ("desarrollo", "parte en que se presentan razones y evidencia"), ("petición concreta", "solicitud precisa de qué, cuándo y quién"), ("cierre respetuoso", "final que agradece y mantiene la cortesía"), ("coloquialismo", "palabra o expresión propia de la conversación informal"), ("fórmula de cortesía", "expresión que muestra respeto, como «agradeceríamos»")],
    worked=[
        ("Detectar fallas del borrador", "En el borrador de la ficha, ¿qué falla en «porque es bacán y todos lo queremos»?",
         ["«Bacán» es un coloquialismo y no es razón.", "«Todos lo queremos» es vago y no tiene dato que lo respalde."],
         "Registro informal y razón sin evidencia"),
        ("Reescribir con evidencia", "Reescribe la razón con el dato de la consulta.",
         ["La consulta indica que 78 de 120 estudiantes no tienen un lugar tranquilo.", "78 ÷ 120 = 0,65, que es 65 %."],
         "«Según una consulta de ejemplo, 65 % de los 120 estudiantes consultados no cuenta con un lugar tranquilo para estudiar en casa»"),
    ],
    mistakes=[("Presentar una petición sin decir cuándo, dónde ni quién se hará cargo.", "Se piensa que la autoridad completará los detalles.", "Incluye día, horario, responsable y una propuesta de cuidado."),
              ("Cerrar con una exigencia como «esperamos respuesta pronto».", "Se confunde firmeza con presión.", "Usa una fórmula respetuosa: «agradeceríamos una respuesta antes del…».")],
    T=[
        ("abc", "{F} ¿Qué palabra del cierre del borrador es informal para una carta formal?", "Chao", "respuesta", "Esperamos", "Es una despedida coloquial; las otras palabras se pueden usar en una carta formal."),
        ("abc", "{F} ¿Qué parte de la carta falta en el borrador?", "Una petición concreta con horario y responsable", "El título del liceo", "Una caricatura", "El borrador no precisa cuándo, ni quién se hará cargo."),
        ("=", "{F} Si la consulta hubiera mostrado que 90 de los 120 estudiantes no tienen un lugar tranquilo, ¿qué porcentaje sería?", "90*100//120", "90 de 120 equivale a 75 por cada 100.", " %"),
        ("abc", "{F} ¿Cuál es una fórmula respetuosa de petición?", "«Solicitamos que nos autorice el uso de la sala 4 entre las 15:00 y las 17:00»", "«Préstennos la sala 4 ya»", "«Queremos la sala porque sí»", "Es precisa, respetuosa y concreta en lo que se pide."),
        ("abc", "{F} ¿Qué dato muestra viabilidad a la dirección?", "La sala 4 está libre entre las 15:00 y las 17:00", "La sala es bacán", "Todos la quieren", "Indica que no hay conflicto de uso en ese horario."),
        ("abc", "{F} ¿Qué dato ayuda a la preocupación de seguridad de la dirección?", "Un inspector se ofreció para abrir y cerrar", "El número de sillas", "El color de la sala", "Propone un responsable del cuidado del espacio."),
        ("ab", "{F} ¿Cuál es el cierre más adecuado?", "«Agradeceríamos una respuesta antes del viernes. Atentamente, el centro de estudiantes»", "«Esperamos respuesta pronto. Chao»", "El primero es respetuoso y fija un plazo; el segundo es informal y exigente."),
        ("abc", "{F} ¿Por qué «todos lo queremos» es débil?", "No indica cuántos ni cómo se supo", "Es muy específico", "Es muy formal", "No está respaldado por un dato verificable."),
        ("abc", "{F} Para una intervención oral de un minuto con el mismo propósito, ¿qué conviene incluir?", "Saludo, la petición, un dato clave y la propuesta de cuidado", "Todo el borrador leído sin cambios", "Solo el saludo", "En un minuto se priorizan los elementos esenciales."),
        ("abc", "{F} Una compañera propone exagerar el dato: «casi todos los estudiantes no tienen dónde estudiar». ¿Qué respondes?", "Hay que usar el dato exacto, 65 % de los consultados", "Sí, exagerar convence más", "Mejor no usar datos", "Un texto formal debe citar con exactitud."),
        ("abc", "{F} ¿Cuál es el orden adecuado de las partes?", "Saludo, presentación y propósito, razones con evidencia, petición y cierre", "Cierre, saludo, petición y razones", "Petición, cierre y saludo", "Es el orden que facilita entender y responder."),
        ("abc", "{F} Si la dirección objeta que la sala puede ensuciarse, ¿cuál es una respuesta adecuada?", "Proponer un turno de limpieza y un responsable por día", "Decir que no importa", "Insistir con más volumen", "Atiende la objeción con una medida concreta."),
        ("abc", "{F} ¿Qué mejora más el texto de la carta?", "Reemplazar frases vagas por datos y una petición con horario", "Hacerlo más largo con adjetivos", "Quitar el saludo", "Aporta claridad, evidencia y registro formal."),
    ],
    ctx=("abc", "Un grupo ficticio debe pedir permiso al municipio para usar un salón comunitario los domingos. ¿Cuál es la mejor apertura de su carta?", "«Estimada encargada: solicitamos autorización para usar el salón comunitario los domingos de 10:00 a 13:00»", "«Hola, queremos el salón»", "«Oye, préstenos el salón, ¿sí?»", "Saluda con respeto y plantea la petición precisa."),
    sc=[
        ("En Participación y argumentación: ¿qué partes tiene una carta formal?", "Saludo, presentación, razones con evidencia, petición y cierre", "Cada parte cumple una función distinta."),
        ("¿Qué es un coloquialismo?", "Palabra o expresión propia de la conversación informal", "No se recomienda en un texto formal."),
        ("¿Qué datos debe incluir una petición concreta?", "Qué se pide, cuándo, dónde y quién se hace cargo", "Así la persona puede decidir y responder."),
    ],
    op=("Elige uno. Escribe una carta formal de cinco a siete oraciones para: (a) pedir a la dirección autorización para organizar una feria de libros usados en el patio un viernes de 15:00 a 17:00, con 60 libros disponibles y un docente que supervisaría; o (b) pedir a la junta de vecinos el salón los domingos de 10:00 a 12:00 para un taller de lectura, con 20 personas inscritas y una vecina responsable. "
        "Incluye saludo, propósito, evidencia con cifra exacta, petición concreta, propuesta de cuidado y cierre.",
        "(a) «Estimado director: nos dirigimos a usted para solicitar autorización para realizar una feria de libros usados el viernes de 15:00 a 17:00 en el patio. Contamos con 60 libros para intercambiar y con el apoyo de un docente que supervisaría la actividad. Agradeceríamos una respuesta antes del miércoles. Atentamente, el centro de estudiantes.»",
        ["usa registro formal", "incluye todas las partes de la carta", "cita las cifras sin cambiarlas", "propone un responsable o medida de cuidado"],
        ["carta de cinco a siete oraciones con las partes marcadas"],
        ["usar coloquialismos", "pedir sin horario ni responsable", "exagerar la cifra"],
        "Pregunta: «¿qué haría la persona que lee esta carta después de leerla?». Si no sabe qué decidir, falta precisión."),
    reinforce="Reescribe la oración «Todos lo queremos» de la ficha usando el dato de los 78 estudiantes de 120 y un registro formal.",
    extend="Prepara una versión oral de un minuto de la misma petición y señala qué partes de la carta recortaste y por qué.",
)
