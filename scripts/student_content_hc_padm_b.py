"""Participación y argumentación en democracia (electivo HC, 3.º y 4.º medio): OAC-03 (formas de legitimar el conocimiento: aceptabilidad, suficiencia y pertinencia), clases 1 a 6. Casos ficticios y datos de ejemplo."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada texto, ficha o tabla está escrito en el enunciado. "
             "Todos los casos son ficticios (comuna «Villa Alerce», «Liceo Los Pinos») y los datos son de ejemplo: no son cifras reales ni se deben citar como si lo fueran. "
             "Las posturas se presentan con sus razones y sin tomar partido: tu tarea es evaluar el conocimiento y los argumentos. Si un tema te afecta personalmente, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O3 = "LL-PADM-3y4-OAC-03"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (cuatro afirmaciones de ejemplo sobre un mismo tema: el sueño y la concentración). "
     "Afirmación 1: «Un estudio de ejemplo midió las horas de sueño y el rendimiento de 300 estudiantes y publicó cómo lo hizo.» "
     "Afirmación 2: «La orientadora del liceo, que trabaja hace años con jóvenes, dice que dormir poco afecta la concentración.» "
     "Afirmación 3: «Yo duermo poco y me va bien en clases.» "
     "Afirmación 4: «En mi familia siempre se ha dicho que dormir temprano hace bien.»")
build(
    O3, 1, F,
    use="Aprenderé qué significa que un conocimiento esté legitimado, qué formas de legitimarlo existen (investigación, autoridad, experiencia, tradición) y con qué tres criterios se evalúan: aceptabilidad, suficiencia y pertinencia.",
    prior=["Sé qué es un argumento y una premisa.", "Sé que un dato necesita fuente.", "Sé distinguir un hecho de una opinión."],
    explain=[
        "Legitimar un conocimiento es dar razones de por qué una comunidad lo acepta como válido. Hay formas distintas: la investigación científica (método sistemático, datos y posibilidad de verificar), la autoridad (una persona o institución con experiencia reconocida en el tema), la experiencia personal (lo que alguien vivió), la tradición (lo que se ha dicho siempre) y la popularidad (lo que mucha gente repite). Las últimas dos, por sí solas, legitiman poco.",
        "Para evaluar cada forma se usan tres criterios. Aceptabilidad: ¿es creíble la fuente y el modo en que se generó el conocimiento? Suficiencia: ¿alcanza lo presentado para sostener la conclusión, o es muy poco? Pertinencia: ¿tiene que ver con el tema, con el ámbito de participación y con lo que la comunidad necesita decidir? Un conocimiento puede ser aceptable pero insuficiente, o suficiente pero impertinente.",
        "Evaluar no es descartar. La experiencia personal es valiosa para saber cómo se vive algo, aunque no sirve para generalizar a todos. La autoridad ayuda cuando es experta en el tema específico. La investigación es potente, pero también puede tener errores o muestras pequeñas. Por eso se pregunta siempre cómo se generó el conocimiento, quién lo afirma y para qué se usa.",
    ],
    vocab=[("legitimar", "dar razones para que una comunidad acepte un conocimiento"), ("aceptabilidad", "credibilidad de la fuente y de cómo se generó el conocimiento"), ("suficiencia", "que lo presentado alcance para sostener la conclusión"), ("pertinencia", "relación adecuada con el tema, el ámbito y el propósito"), ("autoridad", "persona o institución con experiencia reconocida en un tema"), ("tradición", "lo que se ha dicho o hecho desde antes")],
    worked=[
        ("Identificar la forma de legitimación", "En la ficha, ¿qué forma de legitimar usa la afirmación 2?",
         ["Se apoya en que la orientadora trabaja hace años con jóvenes.", "Esa es una razón de experiencia reconocida: autoridad."],
         "Autoridad"),
        ("Aplicar un criterio", "La afirmación 3, ¿es suficiente para concluir que dormir poco no afecta a nadie?",
         ["Es una sola experiencia personal.", "Una sola persona no basta para generalizar a todo el estudiantado: es insuficiente."],
         "No es suficiente: es un solo caso"),
    ],
    mistakes=[("Aceptar un conocimiento solo porque mucha gente lo repite.", "Se confunde popularidad con razones.", "Pregunta cómo se generó y quién lo respalda, no cuántos lo dicen."),
              ("Descartar toda experiencia personal por no ser científica.", "Se piensa que solo vale lo medido.", "Úsala como testimonio de lo vivido y no la generalices a todos sin más datos.")],
    T=[
        ("abc", "{F} ¿Qué forma de legitimación usa la afirmación 1?", "Investigación con método publicado", "Autoridad", "Tradición", "Se apoya en datos recogidos y en que el método fue publicado."),
        ("abc", "{F} ¿Qué forma de legitimación usa la afirmación 3?", "Experiencia personal", "Investigación", "Autoridad", "Se basa en lo que vive quien habla."),
        ("abc", "{F} ¿Qué forma de legitimación usa la afirmación 4?", "Tradición familiar", "Investigación", "Experiencia profesional", "Se apoya en lo que siempre se ha dicho."),
        ("abc", "¿Qué criterio pregunta si lo presentado alcanza para sostener la conclusión?", "Suficiencia", "Aceptabilidad", "Pertinencia", "La suficiencia se refiere a la cantidad y fuerza de lo presentado."),
        ("abc", "¿Qué criterio pregunta si la fuente es creíble y cómo se generó el conocimiento?", "Aceptabilidad", "Suficiencia", "Pertinencia", "La aceptabilidad evalúa la fuente y su modo de generación."),
        ("abc", "¿Qué criterio pregunta si el conocimiento tiene que ver con el tema y el ámbito en que se discute?", "Pertinencia", "Suficiencia", "Aceptabilidad", "La pertinencia relaciona el conocimiento con el tema y el propósito."),
        ("ab", "{F} Para concluir que «el estudiantado en general rinde mejor con más sueño», ¿cuál afirmación aporta más?", "La 1, porque midió a 300 estudiantes con un método publicado", "La 3, porque es la experiencia de quien habla", "Un estudio con muchos casos y método a la vista es más suficiente que una experiencia individual."),
        ("abc", "{F} Un compañero dice: «La 4 vale porque mucha gente la repite». ¿Qué falla?", "La popularidad y la tradición no explican por qué es cierta", "Nada, repetir una idea la hace verdadera", "La tradición siempre es falsa", "Repetirse no es una razón sobre cómo se generó el conocimiento."),
        ("abc", "Una orientadora experta en convivencia escolar afirma cómo reaccionan los estudiantes ante una norma. Es pertinente porque:", "Su experiencia se refiere al tema que se discute", "Tiene un cargo importante en cualquier tema", "Habla con mucha seguridad", "La autoridad se evalúa por su relación con el tema específico."),
        ("abc", "Un estudio de ejemplo con 10 personas, sin explicar cómo las eligieron, concluye algo sobre todo el país. ¿Qué criterio falla más?", "Suficiencia y aceptabilidad: muestra mínima y método poco claro", "Pertinencia, porque el estudio es científico", "Ninguno, porque es un estudio", "Pocos casos y método oculto no sostienen una conclusión tan amplia."),
        ("abc", "{F} Se debe decidir si el liceo cambia el horario de inicio. ¿Qué es más pertinente?", "Datos sobre sueño y atrasos del propio estudiantado", "Una frase de tradición sobre dormir temprano", "El gusto de una persona por las mañanas", "Los datos del propio liceo tratan el tema que se decide."),
        ("{F} Una persona dice: «Mi tío vive bien sin dormir mucho, así que dormir no importa». ¿Qué criterio falla?", "La suficiencia", "Un solo caso no sostiene una conclusión general."),
        ("abc", "¿Por qué evaluar una afirmación no significa descartarla automáticamente?", "Porque se puede usar con sus límites declarados", "Porque toda afirmación es igual de válida", "Porque evaluar es votar", "Una experiencia sirve como testimonio, aunque no permita generalizar."),
    ],
    ctx=("abc", "Una vecina ficticia dice en el consejo: «En mi calle todos los años se inunda, lo vi durante diez años». Para decidir dónde poner una obra, el consejo la escucha. ¿Cómo usar su aporte?", "Como testimonio valioso que se complementa con datos del lugar", "Descartarlo por ser solo experiencia personal", "Considerarlo prueba suficiente para toda la comuna", "Su experiencia informa sobre su calle, pero para decidir una obra se necesita más evidencia."),
    sc=[
        ("En Participación y argumentación: ¿qué significa legitimar un conocimiento?", "Dar razones para que una comunidad lo acepte", "Se justifica por qué algo se considera conocimiento válido."),
        ("¿Cuáles son los tres criterios para evaluar un conocimiento?", "Aceptabilidad, suficiencia y pertinencia", "Evalúan la fuente, la cantidad de apoyo y la relación con el tema."),
        ("¿Por qué la experiencia personal no basta para generalizar?", "Porque es un caso o pocos casos que pueden no representar a los demás", "Representa lo vivido por una persona, no necesariamente por todos."),
    ],
    op=("Elige uno. Tema 1: ¿conviene que el liceo ofrezca un taller de ajedrez en el recreo? Tema 2: ¿conviene cerrar un sábado la calle Central? "
        "Para el tema elegido, escribe una afirmación de ejemplo por cada forma de legitimación (investigación, autoridad, experiencia personal, tradición), y evalúa cada una con aceptabilidad, suficiencia y pertinencia, señalando cuál usarías primero y por qué.",
        "Tema 1. Investigación: «Un registro de ejemplo muestra que el taller reunió a 25 estudiantes por semana». Autoridad: «La profesora de matemática dice que ayuda a la concentración». Experiencia: «Yo jugué y me gustó». Tradición: «En el liceo siempre hubo ajedrez». Usaría primero el registro, que es más suficiente. La tradición es poco pertinente para decidir ahora.",
        ["escribe una afirmación por cada forma de legitimación", "evalúa con los tres criterios con razones propias", "justifica cuál usaría primero y qué límites tiene"],
        ["tabla de cuatro filas con afirmación, forma y evaluación"],
        ["usar la popularidad como forma de legitimación", "evaluar con un solo criterio", "descartar una forma por no ser científica"],
        "Pregunta: «¿qué criterio falla más en esta afirmación?». Si no distingue, vuelve a las definiciones de la clase."),
    reinforce="Elige una de las cuatro afirmaciones de la ficha y evalúala con los tres criterios, escribiendo una oración por criterio.",
    extend="Explica una situación en que una experiencia personal sea más pertinente que un estudio con muchos datos.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (dos sondeos de ejemplo sobre si el liceo debe tener un kiosco saludable). "
     "Sondeo 1: el encargado del centro de estudiantes preguntó mediante un formulario a 20 estudiantes de 3.º A, elegidos entre sus amistades; 16 respondieron que sí. "
     "Sondeo 2: una profesora sorteó 60 nombres desde una lista con todos los estudiantes del liceo y les hizo la misma pregunta; 39 respondieron que sí.")
build(
    O3, 2, F,
    use="Aprenderé a analizar cómo se genera un conocimiento a partir de una encuesta (quién pregunta, a quiénes, cuántos y cómo se eligen) y a juzgar si es aceptable y suficiente.",
    prior=["Sé qué es un porcentaje.", "Sé que la investigación necesita un método.", "Sé que muestra es la parte de un grupo a la que se pregunta."],
    explain=[
        "Para evaluar un conocimiento hay que mirar su modo de generación. En una encuesta importan cuatro cosas: quién la hizo, a quiénes se preguntó (la muestra), cuántas personas respondieron y cómo se las eligió. Una muestra es representativa cuando se parece al conjunto del que se quiere hablar, por ejemplo cuando todos tuvieron la misma oportunidad de ser elegidos mediante un sorteo.",
        "Si la muestra se elige entre amistades o entre quienes estaban a mano, aparece un sesgo de selección: el resultado puede reflejar solo a esas personas. El tamaño también influye: con pocas personas, un resultado puede cambiar mucho al preguntar a otras. Una muestra grande no corrige una mala selección, pero una selección al azar con tamaño razonable permite hablar con más confianza del conjunto. También importa cómo se redacta la pregunta: una pregunta cargada, que ya sugiere la respuesta esperada, orienta a quien responde y resta calidad al dato.",
        "Por eso, ante dos sondeos distintos, se compara su aceptabilidad (método y selección) y su suficiencia (cantidad de respuestas). El porcentaje se calcula dividiendo los casos a favor por el total y multiplicando por 100. Aun con una buena muestra, un sondeo informa lo que opina la gente, no si algo es cierto ni conveniente. Es un insumo para decidir, no la decisión.",
    ],
    vocab=[("muestra", "parte de un conjunto a la que se pregunta o mide"), ("representativa", "que se parece al conjunto del que se quiere hablar"), ("sesgo de selección", "distorsión por elegir a quienes responden de manera no aleatoria"), ("azar", "elección en que todos tienen la misma oportunidad"), ("porcentaje", "parte de cada cien"), ("modo de generación", "cómo se produjo un conocimiento")],
    worked=[
        ("Calcular y comparar", "En el sondeo 1, ¿qué porcentaje respondió que sí?",
         ["16 de 20 es 16 ÷ 20 = 0,8.", "Multiplicando por 100 se obtiene 80 %."],
         "80 %"),
        ("Detectar el sesgo", "¿Por qué el sondeo 1 representa mal al liceo?",
         ["Se eligió a amistades del encargado, no al azar.", "Además, solo se preguntó a un curso de todo el liceo."],
         "Tiene sesgo de selección y no abarca todo el liceo"),
    ],
    mistakes=[("Creer que una muestra grande siempre es representativa.", "Se olvida que importa cómo se eligió a las personas.", "Revisa primero cómo se seleccionó y luego cuántas personas respondieron."),
              ("Interpretar «80 % dijo que sí» como «80 % de todo el liceo piensa eso».", "Se generaliza más allá de a quiénes se preguntó.", "Di: «80 % de las 20 personas consultadas», y evalúa si pueden representar a otras.")],
    T=[
        ("=", "{F} En el sondeo 2, ¿qué porcentaje respondió que sí? (39 de 60)", "39*100//60", "39 ÷ 60 = 0,65, que es 65 por cada 100.", " %"),
        ("abc", "{F} ¿Cómo se eligió la muestra del sondeo 2?", "Por sorteo desde una lista con todos los estudiantes", "Entre las amistades de quien preguntó", "Entre quienes estaban a mano en el patio", "La ficha dice que se sorteó desde la lista completa."),
        ("abc", "{F} ¿Cuál es el problema principal del sondeo 1?", "Sesgo de selección: se eligió entre amistades de un curso", "Que usó formulario", "Que 16 es un número par", "Quien eligió a los encuestados favoreció a su entorno cercano."),
        ("abc", "{F} ¿Cuál sondeo es más aceptable por su método de selección?", "El sondeo 2", "El sondeo 1", "Ambos por igual", "El sorteo da a todos la misma oportunidad de estar en la muestra."),
        ("=", "{F} ¿Cuántas personas del sondeo 2 NO respondieron que sí? (60 menos 39)", "60-39", "Se resta del total de la muestra la cantidad de respuestas afirmativas.", " personas"),
        ("abc", "{F} Una persona dice: «El 80 % del liceo quiere el kiosco». ¿Qué error comete?", "Generaliza el resultado de 20 personas elegidas sin azar a todo el liceo", "Calculó mal 16 ÷ 20", "Usó un sondeo de otro país", "El porcentaje es correcto para la muestra, pero esta no representa al liceo."),
        ("ab", "El sondeo 2, ¿garantiza que 65 % de todo el liceo está a favor?", "No: es una estimación con una muestra de 60 personas", "Sí: el sorteo asegura el mismo resultado exacto", "El sorteo mejora la representatividad, pero una muestra no entrega el valor exacto del conjunto."),
        ("abc", "{F} Si el liceo tiene 600 estudiantes, ¿qué fracción del total es la muestra del sondeo 2?", "Una décima parte", "Una centésima parte", "La mitad", "60 de 600 es 1 de cada 10."),
        ("abc", "Un sondeo pregunta «¿no cree que es absurdo que no haya kiosco?». ¿Qué falla además de la muestra?", "La pregunta orienta la respuesta", "Que usa signos de interrogación", "Que es muy corta", "Una pregunta cargada induce a responder en un sentido y baja la aceptabilidad."),
        ("abc", "{F} Si solo hubiera existido el sondeo 1, ¿cuál sería una conclusión prudente?", "Que 16 de 20 consultados en 3.º A dijeron que sí, sin generalizar", "Que todo el liceo quiere el kiosco", "Que el kiosco mejorará la salud", "Describe lo que se midió sin extenderlo."),
        ("abc", "Un sondeo con 1.000 respuestas en un sitio web abierto, donde cualquiera puede votar varias veces, ¿es suficiente para hablar de toda la comuna?", "No: la cantidad no corrige que cualquiera pueda votar varias veces y que no se sepa quién responde", "Sí: 1.000 es mucho", "Sí: porque es en línea", "Los votos repetidos y que responda solo quien quiere debilitan el método aunque haya muchas respuestas."),
        ("abc", "{F} ¿Qué pregunta le harías a quien hizo el sondeo 2 para saber si es aceptable?", "¿Cómo sorteaste los nombres y respondieron todos los sorteados?", "¿Cuál es tu color favorito?", "¿Podrías repetir el sondeo con tus amistades?", "Examina el método de selección y cuántos respondieron."),
        ("abc", "{F} Aun con una buena muestra, un sondeo de opinión permite concluir que:", "La gente consultada prefiere el kiosco en cierta proporción", "El kiosco es la mejor solución de salud", "El kiosco no tendrá problemas", "Un sondeo informa opiniones, no la conveniencia técnica del kiosco."),
    ],
    ctx=("abc", "Un club deportivo ficticio quiere saber si los socios apoyan subir la cuota. Envía una encuesta y responden 12 de 200 socios, casi todos directivos. ¿Qué se puede afirmar con cuidado?", "Que 12 respondieron y que pueden no representar a los 200 socios", "Que los socios apoyan la subida", "Que el club tiene un problema de dinero", "Responden pocos y de un grupo particular, por lo que no se sabe qué piensa el resto."),
    sc=[
        ("En Participación y argumentación: ¿qué es una muestra representativa?", "Una que se parece al conjunto del que se quiere hablar", "Un sorteo con tamaño razonable ayuda a lograrla."),
        ("¿Qué es el sesgo de selección?", "Distorsión por elegir a quienes responden de manera no aleatoria", "Elegir entre amistades o personas a mano cambia el resultado."),
        ("=", "Si 18 de 24 consultados dicen que sí, ¿qué porcentaje es?", "18*100//24", "18 ÷ 24 = 0,75, o 75 por cada 100.", " %"),
    ],
    op=("Elige uno. Caso 1: un taller ficticio quiere saber si hay interés en una radio escolar. Datos de ejemplo: la radio preguntó a 25 estudiantes que pasaban por el patio y 20 dijeron que sí. Caso 2: una junta de vecinos ficticia preguntó a 50 hogares sorteados de un listado de 400 si prefieren feria el sábado o el domingo; 30 prefirieron el sábado. "
        "Calcula el porcentaje, evalúa cómo se generó el dato (selección, tamaño, pregunta) y redacta una conclusión prudente en dos oraciones.",
        "Caso 2. 30 de 50 es 60 %. El sorteo desde un listado completo mejora la representatividad; 50 hogares de 400 es una muestra razonable para una estimación. Conclusión: aproximadamente seis de cada diez hogares consultados prefieren el sábado; conviene confirmarlo con una prueba breve.",
        ["calcula correctamente el porcentaje", "evalúa selección, tamaño y pregunta", "redacta una conclusión que no generaliza más de lo medido"],
        ["cálculo, evaluación y conclusión de dos oraciones"],
        ["generalizar a toda la comunidad", "calcular el porcentaje sobre el total equivocado", "no evaluar cómo se eligió la muestra"],
        "Pregunta: «¿a quiénes se preguntó y quiénes quedaron fuera?». Si no lo menciona, pide revisarlo."),
    reinforce="Con los datos del sondeo 1 de la ficha, redacta una frase que describa el resultado sin generalizar al liceo.",
    extend="Explica por qué dos sondeos con resultados parecidos pueden tener distinta calidad, y cómo lo mostrarías a tu curso.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (caso de ejemplo: ¿reduce el ruido un nuevo tipo de pavimento para la calle Central?). "
     "Persona 1: un ingeniero de la empresa que vende ese pavimento afirma que sí lo reduce mucho. "
     "Persona 2: una vecina que vive hace veinte años en la calle cuenta que con el pavimento viejo no podía dormir por el ruido. "
     "Persona 3: un profesor de acústica de una universidad, sin vínculo con empresas, explica cómo se mide el ruido y que conviene medir antes y después. "
     "Persona 4: un usuario de redes sociales dice «lo vi en un video, funciona».")
build(
    O3, 3, F,
    use="Aprenderé a evaluar la autoridad (cuándo una persona o institución es una fuente confiable) y la experiencia personal (qué aporta y cuáles son sus límites) como formas de legitimar conocimiento.",
    prior=["Conozco los criterios de aceptabilidad, suficiencia y pertinencia.", "Sé que la experiencia personal es un caso.", "Sé qué es un interés."],
    explain=[
        "La autoridad es una forma legítima de conocimiento cuando se cumplen condiciones: la persona o institución tiene experiencia en el tema específico, no depende de que una respuesta le convenga (independencia), sus afirmaciones se pueden verificar y coincide con lo que dicen otras fuentes expertas. Un cargo o un título no bastan: la experticia es sobre un tema, no sobre todo.",
        "El conflicto de interés no vuelve falsa una afirmación, pero obliga a pedir verificación independiente. Si quien afirma que un producto funciona es quien lo vende, hay que contrastar con otra fuente. Una autoridad también se equivoca, por lo que se evalúa si explica cómo sabe lo que dice y si reconoce los límites de su conocimiento, como cuando recomienda medir antes y después.",
        "La experiencia personal tiene un valor propio: informa cómo se vive algo, qué dificultades aparecen y qué no se había medido. Pero es una experiencia individual, influida por memoria, emociones y circunstancias. Sirve para formular preguntas y reconocer problemas; para generalizar se necesita contrastarla con más casos. Una buena deliberación escucha ambas y las combina con datos.",
    ],
    vocab=[("experticia", "conocimiento especializado en un tema determinado"), ("independencia", "no depender de que una respuesta le convenga"), ("conflicto de interés", "situación en que quien afirma se beneficia de que se le crea"), ("verificación independiente", "comprobación hecha por otra fuente sin vínculo con la primera"), ("testimonio", "relato de lo que una persona vivió"), ("generalizar", "extender lo observado en algunos casos a todos los casos")],
    worked=[
        ("Evaluar una autoridad", "En la ficha, ¿qué problema plantea la afirmación de la persona 1?",
         ["La persona trabaja para la empresa que vende el pavimento: tiene un interés en que se le crea.", "Eso no la vuelve falsa, pero pide verificación independiente."],
         "Hay conflicto de interés; se necesita verificación independiente"),
        ("Valorar una experiencia", "¿Qué aporta el relato de la persona 2 y qué no puede probar?",
         ["Muestra cómo vivió el ruido una persona durante años.", "No prueba que el pavimento nuevo lo reduzca ni que otras casas lo vivan igual."],
         "Aporta una vivencia, pero no prueba el efecto del pavimento"),
    ],
    mistakes=[("Creer una afirmación solo porque quien la dice tiene un título.", "Se confunde cargo con experticia en el tema.", "Pregunta si su experticia es en este tema y si hay conflicto de interés."),
              ("Descartar una afirmación por conflicto de interés sin revisarla.", "Se piensa que el interés la vuelve falsa.", "Un interés exige verificarla con una fuente independiente, no la refuta.")],
    T=[
        ("abc", "{F} ¿Qué persona tiene un conflicto de interés evidente?", "La persona 1", "La persona 2", "La persona 3", "El ingeniero trabaja para quien vende el pavimento."),
        ("abc", "{F} La vecina agrega: «Todas las casas de la comuna sufren el mismo ruido que yo». ¿Qué error comete?", "Generaliza su vivencia a todas las casas sin otros datos", "Usa una medición con método", "Es una autoridad independiente", "Su experiencia informa sobre su calle, no sobre toda la comuna."),
        ("abc", "{F} ¿Cuál es la fuente más independiente de la ficha?", "La persona 3", "La persona 1", "La persona 4", "El profesor no tiene vínculo con empresas y explica cómo medir."),
        ("abc", "{F} La persona 4 dice «lo vi en un video». ¿Qué criterio falla más?", "Aceptabilidad: no se sabe quién lo hizo ni cómo", "Pertinencia, porque habla de pavimentos", "Ninguno, porque es muy popular", "No hay fuente identificable ni método."),
        ("ab", "Un título universitario en cualquier área, ¿basta para ser autoridad en ruido de calles?", "No: la experticia debe ser en el tema específico", "Sí: un título vale para cualquier tema", "La autoridad se evalúa por su relación con el tema."),
        ("abc", "{F} ¿Qué recomienda la persona 3 que mejora la aceptabilidad?", "Medir el ruido antes y después del cambio", "Confiar en la palabra del ingeniero", "Preguntar solo a los vecinos", "Una medición antes y después permite comparar con datos."),
        ("abc", "{F} Un participante dice: «El ingeniero miente porque trabaja en la empresa». ¿Qué respuesta es más razonable?", "Su afirmación debe verificarse con una fuente independiente, sin darla por falsa", "Tiene razón: todo lo que dice una empresa es falso", "No importa quién lo diga", "El conflicto de interés pide verificar, no concluir que miente."),
        ("abc", "¿Cuál es el límite principal de una experiencia personal?", "Es un caso individual que puede no representar a los demás", "Siempre es falsa", "No puede ser sincera", "La experiencia es valiosa pero no generaliza por sí sola."),
        ("abc", "Un médico opina con total seguridad sobre cómo se construye un puente. ¿Cómo debe evaluarse?", "Su experticia no está en construcción, así que su opinión pesa poco en ese tema", "Es autoridad en todo por ser médico", "Es falsa porque es médico", "La autoridad se limita al tema en que se tiene experticia."),
        ("abc", "{F} Si 5 vecinos con pavimento nuevo dicen que el ruido bajó y 5 que no cambió, ¿qué conclusión es más prudente?", "No hay evidencia clara con solo esos relatos; conviene medir el ruido", "El pavimento funciona", "El pavimento no funciona", "Los testimonios divididos no resuelven un hecho medible."),
        ("abc", "Dos expertos independientes, de universidades distintas, llegan por separado a la misma conclusión con datos abiertos. ¿Qué aporta esto?", "Mayor aceptabilidad por coincidencia y verificabilidad", "Nada, porque los expertos son lo mismo", "Menor aceptabilidad", "Coincidencias independientes con datos verificables refuerzan la confianza."),
        ("abc", "{F} ¿Qué dos tipos de fuente combinarías para decidir si poner el pavimento nuevo?", "Una medición independiente del ruido y los testimonios de vecinos", "Solo la opinión del ingeniero de la empresa", "Solo lo que se vio en un video", "Las mediciones evalúan el efecto y los testimonios aportan cómo se vive el problema."),
        ("abc", "{F} ¿Qué haría más fuerte la afirmación de la persona 1?", "Que un laboratorio sin vínculo con la empresa repita la medición", "Que la repita con más fuerza", "Que la diga otra persona de la misma empresa", "Una verificación independiente resuelve el conflicto de interés."),
    ],
    ctx=("abc", "En el consejo vecinal ficticio, una médica de la comuna afirma que cierta planta del sendero no es peligrosa para niños, pero reconoce que su especialidad es la medicina interna y recomienda consultar a un especialista en botánica. ¿Cómo evalúas su aporte?", "Es honesta sobre los límites de su experticia y convendría consultar al especialista", "No sirve, porque no es botánica", "Vale por completo, porque es médica", "Reconocer los límites y derivar es señal de aceptabilidad."),
    sc=[
        ("En Participación y argumentación: ¿qué condiciones hacen legítima a una autoridad?", "Experticia en el tema, independencia y verificabilidad", "No bastan el cargo o el título."),
        ("¿Qué obliga a hacer un conflicto de interés?", "A buscar verificación independiente", "No vuelve falsa la afirmación, pero exige contrastarla."),
        ("¿Para qué sirve la experiencia personal en una deliberación?", "Para mostrar cómo se vive un problema y formular preguntas", "Informa sobre lo vivido sin generalizar."),
    ],
    op=("Elige uno. Caso 1: se debate si un huerto en el liceo mejora la convivencia. Fuentes de ejemplo: un docente de ciencias que coordina el huerto, un estudio de un liceo vecino con 120 estudiantes y un relato de una estudiante que participó. "
        "Caso 2: se debate poner cámaras en una plaza. Fuentes: la empresa que vende cámaras, un informe de ejemplo del municipio con denuncias por mes y el relato de una vecina que sufrió un robo. "
        "Para las tres fuentes del caso elegido, evalúa su aceptabilidad (experticia, independencia), qué aporta y qué límite tiene, y escribe qué fuente adicional pedirías.",
        "Caso 2. Empresa: tiene conflicto de interés; aporta información técnica; hay que verificar. Informe municipal: fuente pública con datos por mes; aporta tendencias; no explica causas. Relato: vivencia valiosa; no generaliza. Pediría una evaluación independiente de otras comunas que usaron cámaras.",
        ["evalúa cada fuente con experticia e independencia", "dice qué aporta y qué límite tiene cada una", "propone una fuente adicional pertinente"],
        ["tabla de tres fuentes con aporte, límite y fuente adicional"],
        ["descartar una fuente solo por su interés", "aceptar una fuente por su cargo", "no declarar el límite de la experiencia"],
        "Pregunta: «¿quién se beneficia de que le creamos?». Luego pide una verificación independiente."),
    reinforce="Escribe tres preguntas que harías a una autoridad antes de aceptar su afirmación, usando experticia, independencia y verificabilidad.",
    extend="Explica por qué una autoridad con conflicto de interés puede igualmente tener razón y cómo se podría comprobar.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (tres ámbitos de ejemplo y tres aportes). Ámbito 1: asamblea escolar que decide cómo usar el patio. Ámbito 2: informe técnico que se entrega al municipio para pedir fondos. Ámbito 3: conversación familiar sobre cómo celebrar un cumpleaños. "
     "Aporte X: el relato de un estudiante sobre un accidente en el patio. Aporte Y: un conteo de ejemplo de 40 accidentes leves en el patio durante un año, con fechas y lugares. Aporte Z: la preferencia de la persona que cumple años.")
build(
    O3, 4, F,
    use="Aprenderé a decidir qué conocimiento es pertinente según el ámbito de participación, la comunidad que escucha, el tema y el propósito, y a explicar por qué algo sirve en una situación y no en otra.",
    prior=["Conozco aceptabilidad, suficiencia y pertinencia.", "Sé diferenciar conversación informal y texto formal.", "Sé que un propósito es para qué se argumenta."],
    explain=[
        "No todo conocimiento sirve en cualquier lugar. El ámbito de participación es el espacio donde se discute (una familia, una asamblea, un informe técnico, un medio de comunicación). Cada ámbito tiene una comunidad discursiva, es decir, un conjunto de personas con costumbres y expectativas sobre qué razones valen. En un informe técnico se espera medición con método; en una conversación familiar basta el afecto y la costumbre.",
        "La pertinencia depende de cuatro cosas: el tema (¿de qué se trata?), el propósito (¿informar, decidir, pedir, convencer?), la comunidad (¿quién escucha?) y el ámbito. El mismo aporte puede ser pertinente en un lugar y no en otro. Un relato personal es muy valioso en una asamblea que quiere conocer cómo se vive un problema, pero por sí solo es insuficiente en un informe que pide fondos.",
        "Adaptarse al ámbito no es cambiar la verdad según el público. Es elegir la forma de legitimar que esa comunidad puede evaluar y que el propósito requiere. En una asamblea conviene combinar un relato con un conteo. En un informe técnico se priorizan datos y fuentes. En lo familiar pesan los gustos de las personas. Siempre se evita presentar como dato lo que es una impresión.",
    ],
    vocab=[("ámbito de participación", "espacio donde se discute o decide un asunto"), ("comunidad discursiva", "grupo con costumbres sobre qué razones valen"), ("propósito", "para qué se argumenta: informar, decidir, pedir o convencer"), ("pertinente", "adecuado al tema, ámbito, comunidad y propósito"), ("informe técnico", "documento que presenta datos y método para fundamentar una petición"), ("registro", "forma de hablar o escribir adecuada a la situación")],
    worked=[
        ("Elegir según el ámbito", "En la ficha, ¿qué aporte es más pertinente para el informe técnico del ámbito 2?",
         ["Un informe técnico pide datos con fechas y lugares.", "El aporte Y es un conteo con fechas y lugares; el relato X es una vivencia sin medición."],
         "El aporte Y"),
        ("Cambiar de ámbito", "¿Por qué el aporte Z (preferencia de la persona que cumple años) sirve en el ámbito 3 y no en el 2?",
         ["En una celebración familiar, decide la preferencia de quien celebra.", "En un informe para pedir fondos no responde al tema ni al propósito."],
         "Es pertinente al tema y propósito de la conversación familiar, no del informe"),
    ],
    mistakes=[("Usar el mismo tipo de prueba en todos los ámbitos.", "Se piensa que existe una única forma correcta de argumentar.", "Pregunta qué razones espera la comunidad y qué propósito tiene el texto."),
              ("Creer que adaptarse al ámbito significa decir cosas distintas según quién escuche.", "Se confunde adaptación con engaño.", "Mantén la información veraz y cambia la forma de presentarla y de respaldarla.")],
    T=[
        ("{F} ¿Qué dos datos del aporte Y permiten verificarlo?", "Las fechas y los lugares de los accidentes", "Con fechas y lugares otra persona puede revisar cada caso del conteo."),
        ("abc", "{F} ¿Qué aporte es más pertinente para la conversación familiar (ámbito 3)?", "El aporte Z", "El aporte Y", "El aporte X", "La preferencia de quien celebra es lo que decide en ese ámbito."),
        ("abc", "{F} En la asamblea escolar (ámbito 1), ¿qué combinación aporta más?", "Un conteo y un relato que muestre cómo se vive el problema", "Solo la preferencia de una persona", "Ninguna, porque son opiniones", "El conteo informa cuántos casos hubo y el relato cómo se viven."),
        ("abc", "¿Qué es una comunidad discursiva?", "Un grupo con costumbres sobre qué razones valen en su espacio", "Un grupo de personas que vive cerca", "Una lista de nombres", "Cada comunidad discursiva espera ciertas formas de justificar."),
        ("abc", "{F} El propósito del ámbito 2 es pedir fondos al municipio. ¿Qué es más importante en el texto?", "Datos claros con fuente y fecha", "Frases emotivas sin datos", "La opinión de un amigo", "Un informe que pide fondos debe poder ser verificado."),
        ("ab", "Adaptar un argumento al ámbito significa:", "Elegir la forma de respaldarlo que esa comunidad puede evaluar", "Decir algo distinto según quién escucha", "La verdad se mantiene; cambia la forma de justificarla."),
        ("abc", "{F} Un relato personal en un informe técnico, usado como única prueba, es:", "Insuficiente para ese ámbito y propósito", "Siempre suficiente", "Falso", "El informe requiere datos medidos, no solo una vivencia."),
        ("abc", "Una estudiante cuenta en el consejo de curso que se sintió excluida en un recreo. Su relato en ese ámbito sirve para:", "Mostrar cómo se vive el problema y motivar una revisión", "Probar que ocurre en todos los cursos", "Demostrar quién tiene la culpa", "Informa de una vivencia, sin probar frecuencia ni culpables."),
        ("abc", "{F} Un estudiante prepara el informe técnico y escribe: «Todos saben que el patio es peligroso». ¿Qué falla?", "No cita datos ni fuente", "Es muy formal", "Es muy corta", "Una afirmación de popularidad no sirve en un informe."),
        ("abc", "{F} ¿Cómo cambiarías la frase «Todos saben que el patio es peligroso» para el informe?", "«En el último año se registraron 40 accidentes leves en el patio»", "«El patio es un horror»", "«Yo me caí una vez»", "Reemplaza la popularidad por un dato con medición."),
        ("abc", "Una vecina quiere convencer a su familia de ir a un picnic y al municipio de darle un permiso. ¿Qué cambia entre ambos casos?", "El tipo de razones y el registro, no la verdad de lo que dice", "Los hechos, que se ajustan a lo que quiere oír cada público", "Nada: se usa el mismo texto en ambos casos", "Adaptarse al ámbito no significa cambiar los hechos."),
        ("abc", "¿Cuál de estos factores NO determina la pertinencia de un aporte?", "La cantidad de personas que lo repiten", "El propósito del texto", "La comunidad que lo escuchará", "La pertinencia depende de tema, propósito, comunidad y ámbito."),
        ("abc", "{F} El ámbito 1 es una asamblea con estudiantes de 14 a 18 años. ¿Qué registro es más pertinente?", "Claro y respetuoso, con ejemplos que entienda todo el curso", "Muy técnico, con siglas sin explicar", "Burlesco para entretener", "La comunidad debe entender y sentirse respetada."),
    ],
    ctx=("abc", "Un centro de estudiantes ficticio debe elegir qué razones presentar para pedir a la dirección una sala de estudio. Opciones: un listado de 90 firmas de estudiantes con nombre y curso, una anécdota graciosa o una frase popular. ¿Qué es más pertinente?", "El listado de 90 firmas, porque la dirección puede verificar el apoyo", "La anécdota graciosa", "La frase popular", "La dirección necesita evidencia verificable del apoyo estudiantil."),
    sc=[
        ("En Participación y argumentación: ¿qué es un ámbito de participación?", "El espacio donde se discute o decide un asunto", "Cada ámbito tiene su comunidad y sus expectativas."),
        ("¿De qué cuatro cosas depende la pertinencia?", "Del tema, el propósito, la comunidad y el ámbito", "Un aporte se adecua a esas cuatro dimensiones."),
        ("¿Adaptar el argumento al ámbito cambia la verdad de lo que se dice?", "No, solo la forma de respaldarlo y presentarlo", "La adaptación no autoriza a distorsionar los hechos."),
    ],
    op=("Debes defender que el liceo mantenga su biblioteca abierta en la tarde. Elige dos ámbitos: una asamblea del estudiantado, una carta formal a la dirección o un afiche para el patio. "
        "Datos de ejemplo disponibles: un conteo de 150 visitas por semana en la tarde, el testimonio de una estudiante que prepara sus pruebas allí y la opinión de una profesora de lenguaje. "
        "Para cada ámbito elegido, escribe cómo combinarías esos datos, qué priorizarías y qué registro usarías, explicando la pertinencia.",
        "Carta formal: prioriza el conteo de 150 visitas, cita la opinión de la profesora y el testimonio como ejemplo; registro formal. Afiche: frase breve con la cifra de 150 visitas y una cita corta de la estudiante; registro cercano.",
        ["elige y prioriza datos según el ámbito", "adapta el registro sin cambiar los hechos", "explica la pertinencia con tema, propósito y comunidad"],
        ["cuadro con dos ámbitos, datos priorizados y registro"],
        ["usar el mismo texto para todo", "cambiar los hechos para convencer", "usar solo una anécdota en un texto formal"],
        "Pregunta: «¿quién leerá esto y qué le serviría para decidir?». Ajusta datos y registro."),
    reinforce="Escribe cómo contarías, en un registro formal y en uno familiar, que el taller del liceo tendrá una actividad abierta con 40 invitados.",
    extend="Explica por qué la misma anécdota puede ser muy pertinente en una asamblea y poco en un informe técnico.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (cuatro preguntas de ejemplo para una comisión del liceo). Pregunta 1: ¿a qué hora pasa el bus 14 por la plaza? Pregunta 2: ¿mejoró la convivencia con el nuevo horario de recreo? "
     "Pregunta 3: ¿cómo vivieron el cierre de la calle las personas mayores del barrio? Pregunta 4: ¿se puede instalar un letrero de este tamaño en la fachada? "
     "Formas de conocimiento: documento oficial o registro público, estudio con datos antes y después, testimonios recogidos con entrevistas y consulta a la autoridad competente.")
build(
    O3, 5, F,
    use="Aprenderé a diseñar un plan de evidencia para una pregunta pública: qué forma de conocimiento conviene, qué fuentes consultar y qué sería suficiente para decidir.",
    prior=["Sé evaluar fuentes con aceptabilidad, suficiencia y pertinencia.", "Sé que cada ámbito pide razones distintas.", "Sé hacer una tabla simple."],
    explain=[
        "Diseñar una acción democrática basada en conocimiento comienza por la pregunta. Cada pregunta pide un tipo de conocimiento. Un dato fijo, como un horario, se busca en un documento oficial. Si algo mejoró o no, se necesita comparar antes y después con datos. Para conocer cómo lo viven las personas se recogen testimonios. Para saber si algo está permitido se consulta a la entidad competente o la norma.",
        "Un plan de evidencia indica: la pregunta, la forma de conocimiento elegida, las fuentes concretas, cómo se verificará y qué se considerará suficiente. Conviene triangular, es decir, usar al menos dos fuentes de tipo distinto: por ejemplo un dato medido y un testimonio. Si coinciden, la conclusión se fortalece; si no, aparece una pregunta nueva que investigar.",
        "También hay que prever límites: plazos, personas a las que no se alcanzó y datos que no existen. Un buen plan declara qué no podrá responder. Por último, el plan incluye cómo se comunicará el resultado a quienes decidirán y cómo se registrarán las fuentes (nombre, fecha, quién la produjo), para que otros puedan comprobarlo.",
    ],
    vocab=[("plan de evidencia", "lista de fuentes y pasos para responder una pregunta"), ("triangular", "usar fuentes de distinto tipo que se contrastan"), ("documento oficial", "texto emitido por una institución con responsabilidad pública"), ("testimonio", "relato de lo que vivió una persona"), ("competente", "con la responsabilidad de decidir sobre un asunto"), ("registro de fuentes", "anotación de quién produjo la información, cuándo y dónde se obtuvo")],
    worked=[
        ("Asignar la forma de conocimiento", "En la ficha, ¿qué forma de conocimiento conviene para la pregunta 1 (hora del bus)?",
         ["Es un dato fijo, publicado por quien presta el servicio.", "Conviene un documento oficial o registro público."],
         "Documento oficial o registro público"),
        ("Triangular", "Para la pregunta 2 (¿mejoró la convivencia?), ¿qué dos fuentes de tipo distinto combinarías?",
         ["Una fuente de datos: el número de conflictos registrados antes y después del cambio.", "Una fuente de testimonios: entrevistas a estudiantes y docentes sobre cómo viven los recreos."],
         "Registro de conflictos antes y después, más entrevistas"),
    ],
    mistakes=[("Responder todas las preguntas con encuestas de opinión.", "Se usa la misma herramienta sin pensar qué pide cada pregunta.", "Primero identifica si la pregunta pide un dato fijo, una comparación, una vivencia o una norma."),
              ("No anotar de dónde viene cada dato.", "Se cree que basta con recordarlo.", "Registra nombre, fecha y quién produjo cada fuente para que otras personas la verifiquen.")],
    T=[
        ("abc", "{F} ¿Qué forma conviene para la pregunta 2 (¿mejoró la convivencia?)?", "Estudio con datos antes y después", "Un documento oficial de horarios", "Consulta a una autoridad sobre permisos", "Para saber si algo mejoró se necesita comparar dos momentos."),
        ("abc", "{F} ¿Qué forma conviene para la pregunta 3 (¿cómo vivieron el cierre las personas mayores?)?", "Testimonios con entrevistas", "Documento de horarios", "Conteo de autos", "Se pregunta por una vivencia que solo ellas pueden contar."),
        ("abc", "{F} ¿Qué forma conviene para la pregunta 4 (¿se puede instalar el letrero?)?", "Consulta a la autoridad competente o a la norma", "Encuesta de gustos", "Testimonios de vecinos", "Es una cuestión de permiso, que decide una autoridad."),
        ("abc", "{F} Dos vecinos recuerdan horas distintas para el bus 14. ¿Qué resuelve la diferencia?", "El horario publicado por quien presta el servicio de transporte", "Promediar lo que recuerda cada vecino", "Elegir la hora que dice el vecino que habla más fuerte", "Un dato fijo se verifica en el registro de quien lo produce."),
        ("abc", "¿Qué significa triangular?", "Usar fuentes de tipo distinto y contrastarlas", "Preguntar tres veces a la misma persona", "Dibujar un triángulo", "El contraste entre tipos de fuente fortalece o cuestiona la conclusión."),
        ("abc", "{F} Para la pregunta 3, ¿qué límite debe declarar el plan?", "Que los testimonios no representan a todas las personas mayores", "Que no se puede preguntar a nadie", "Que no hay límites", "Un plan honesto declara a quiénes no alcanzó."),
        ("ab", "Un buen plan de evidencia incluye:", "Qué se considerará suficiente y cómo se registrarán las fuentes", "Solo la conclusión deseada", "Debe indicar cómo se sabrá que alcanza la información."),
        ("abc", "{F} Dos fuentes sobre la pregunta 2 se contradicen: los registros muestran menos conflictos, pero los estudiantes dicen que se sienten peor. ¿Qué conviene hacer?", "Formular una nueva pregunta para entender por qué difieren", "Descartar la fuente que no conviene", "Votar cuál es la correcta", "Una discrepancia entre fuentes es una pista para investigar más."),
        ("abc", "Un registro de ejemplo del liceo indica 18 conflictos en el mes anterior al cambio y 12 en el mes posterior. ¿Qué es lo más prudente decir?", "Hubo 6 conflictos menos entre ambos meses, y conviene ver más meses", "El cambio es la causa segura de la baja", "No hubo diferencia", "Dos meses son pocos para atribuir causa con seguridad."),
        ("=", "En otro registro de ejemplo, los conflictos bajaron de 20 a 15 entre dos meses. ¿Qué porcentaje bajaron?", "(20-15)*100//20", "La baja fue de 5 conflictos sobre 20, es decir, un cuarto.", " %"),
        ("abc", "{F} Una comisión usa para la pregunta 4 un grupo de mensajería de vecinos. ¿Qué falla?", "No es la entidad competente, así que no responde la pregunta de permiso", "Que es muy rápida", "Que tiene muchos mensajes", "Un permiso lo informa la autoridad que lo otorga."),
        ("abc", "{F} ¿Cuál es un registro de fuentes completo para el dato de conflictos de la pregunta 2?", "Registro de convivencia del liceo, producido por inspectoría, con datos de marzo a mayo de ejemplo", "«Lo vi por ahí»", "«Me lo contaron»", "Indica nombre, quién lo produjo y período, para poder verificarlo."),
        ("abc", "{F} ¿Qué plan de evidencia es más sólido para la pregunta 3?", "Entrevistar a personas de distintas edades del barrio y complementarlas con un registro de uso de la calle", "Preguntar solo a la dirigente", "Usar una encuesta de gustos del liceo", "Combina testimonios variados con un dato objetivo."),
    ],
    ctx=("abc", "Una comisión ficticia debe decidir si instalar bebederos en el patio. Preguntas: cuántos estudiantes hay, si hay presupuesto y cómo se vive hoy la falta de agua. ¿Qué fuentes corresponden respectivamente?", "Matrícula del liceo, informe de presupuesto y testimonios del estudiantado", "Testimonios, matrícula y encuesta de gustos", "Informe de presupuesto, testimonios y matrícula", "Cada pregunta pide su tipo de fuente: dato institucional, documento financiero y vivencia."),
    sc=[
        ("En Participación y argumentación: ¿qué incluye un plan de evidencia?", "Pregunta, fuentes, verificación y qué sería suficiente", "Así se sabe qué buscar y cuándo basta."),
        ("¿Para qué sirve triangular fuentes?", "Para contrastar y fortalecer o cuestionar la conclusión", "Fuentes distintas se corrigen entre sí."),
        ("¿Qué fuente conviene para saber si algo está permitido?", "La norma o la autoridad competente", "Es quien decide sobre el permiso."),
    ],
    op=("Elige uno. Pregunta 1: ¿ha mejorado el uso de la biblioteca con el nuevo horario? Pregunta 2: ¿cómo se sienten los vecinos con la feria de los domingos? "
        "Diseña un plan de evidencia con: forma de conocimiento, al menos dos fuentes concretas de tipo distinto, cómo las verificarías, qué considerarías suficiente y un límite que declararías.",
        "Pregunta 1. Forma: datos antes y después. Fuentes: registro de visitas del mes anterior y posterior al cambio, y entrevistas breves a cinco estudiantes. Verificación: pedir el registro a la biblioteca. Suficiente: tres meses de datos. Límite: no se sabe qué pasa con quienes no van a la biblioteca.",
        ["relaciona la pregunta con una forma de conocimiento", "propone al menos dos fuentes de tipo distinto", "declara qué sería suficiente y un límite"],
        ["tabla con pregunta, fuentes, verificación, suficiencia y límite"],
        ["usar una sola fuente", "no precisar qué es suficiente", "no declarar límites"],
        "Pregunta: «¿cómo podrías comprobar que tu fuente es confiable?». Si no sabe, ayúdale a escribir una verificación."),
    reinforce="Elige una pregunta de la ficha y escribe cómo registrarías su fuente (nombre, quién la produjo, fecha).",
    extend="Explica cómo cambiaría un plan de evidencia si el plazo fuera de dos días en lugar de dos meses.",
)

# ============================================================ OAC-03, clase 6
F = ("Ficha 6 (caso de ejemplo). Un municipio ficticio instaló lomos de toro en cinco calles porque «un vecino contó que un auto pasó muy rápido frente al colegio». "
     "Después, un conteo de ejemplo mostró que en tres de esas calles casi nunca pasaban autos a alta velocidad, mientras que una calle sin lomos tenía más tránsito veloz. "
     "Una concejala dijo: «Decidimos con la información que había, pero ahora sabemos que fue insuficiente».")
build(
    O3, 6, F,
    use="Aprenderé a evaluar los efectos y límites de cada forma de conocimiento: qué puede fallar en la ciencia, la autoridad y la experiencia, qué pasa si se decide con evidencia débil y cómo corregir.",
    prior=["Sé evaluar autoridad y experiencia personal.", "Sé planificar evidencia con fuentes distintas.", "Sé qué es una conclusión provisoria."],
    explain=[
        "Cada forma de conocimiento tiene límites. La investigación es provisoria: puede tener errores, muestras pequeñas y descubrir cosas nuevas que cambien las conclusiones. Hay que cuidar la confusión entre correlación (dos cosas ocurren juntas) y causa (una produce la otra). La autoridad se equivoca y puede tener intereses. La experiencia personal es parcial. La tradición puede perpetuar errores y la popularidad no prueba nada.",
        "Decidir con evidencia insuficiente tiene efectos en la comunidad: gastar recursos en problemas que no existen, dejar sin atender los que sí existen, o perder la confianza en las instituciones. En el caso, un solo relato llevó a instalar cinco lomos, y los datos posteriores mostraron que no estaban donde más se necesitaba. Revisar una decisión y corregirla es parte de una buena deliberación, no una vergüenza.",
        "Para evitar esos efectos se combinan fuentes, se declara la incertidumbre y se deja la decisión abierta a revisión. Se dice «con la información actual» y se anotan qué datos podrían cambiar la decisión. Aceptar los límites del conocimiento no obliga a no decidir: significa decidir proporcionalmente, con pasos reversibles cuando hay dudas y con más cautela cuando el error es costoso.",
    ],
    vocab=[("provisorio", "sujeto a cambiar si aparece nueva evidencia"), ("correlación", "relación entre dos hechos que ocurren juntos"), ("causa", "hecho que produce otro"), ("incertidumbre", "grado de duda que queda sobre una conclusión"), ("decisión reversible", "la que puede corregirse sin grandes costos"), ("proporcional", "acorde con la gravedad y el costo de equivocarse")],
    worked=[
        ("Detectar la insuficiencia", "En la ficha, ¿qué criterio falló en la decisión de instalar cinco lomos?",
         ["La decisión se apoyó en un solo relato sobre un solo lugar.", "Un caso no basta para decidir en cinco calles: falló la suficiencia."],
         "La suficiencia"),
        ("Distinguir correlación y causa", "Los fines de semana en que hay feria, el helado se vende más y el cobro de estacionamiento sube. ¿Una causa la otra?",
         ["Ambas ocurren juntas, pero hay otra explicación común: la mayor cantidad de gente.", "Que ocurran juntas es correlación, no prueba que una cause la otra."],
         "Es correlación; no se puede afirmar causa"),
    ],
    mistakes=[("Concluir que A causa B porque ambos aparecen juntos.", "Se confunde correlación con causa.", "Pregunta si una tercera cosa explica a ambos o si el orden temporal es el contrario."),
              ("Considerar un error de decisión como prueba de mala fe.", "Se piensa que quien decide con poca información miente.", "Evalúa si la información era suficiente y cómo se corrige; la mala fe requiere evidencia propia.")],
    T=[
        ("{F} Según el conteo, ¿en cuántas de las cinco calles con lomos casi nunca pasaban autos veloces?", "En tres", "La ficha indica que fue en tres de esas cinco calles."),
        ("abc", "{F} ¿Qué mostró el conteo posterior?", "En tres calles casi nunca pasaban autos veloces, y una sin lomos tenía más tránsito veloz", "Que todas las calles eran peligrosas", "Que los lomos no sirven nunca", "El conteo desmintió la ubicación de parte de las obras."),
        ("abc", "{F} ¿Qué efecto tuvo la información insuficiente en la comunidad?", "Se gastaron recursos donde no eran más necesarios y se dejó sin atender una calle", "No hubo ningún efecto", "Se resolvió el problema completo", "Los recursos se orientaron a lugares donde no eran lo más urgente."),
        ("abc", "{F} La concejala dice que ahora sabe que la información fue insuficiente. ¿Qué actitud muestra?", "Reconoce el límite del conocimiento y está abierta a corregir", "Culpa a otra persona", "Niega el problema", "Revisar la decisión es parte de deliberar bien."),
        ("abc", "¿Qué diferencia hay entre correlación y causa?", "Correlación es que ocurran juntas; causa es que una produce la otra", "No hay diferencia", "Correlación significa que una produce la otra", "Dos hechos pueden coincidir sin que uno cause el otro."),
        ("abc", "En los meses de ejemplo con más calor se venden más helados y hay más personas en la playa. ¿Qué conclusión es adecuada?", "El calor puede explicar ambos; no se puede decir que los helados atraen gente", "Los helados atraen gente a la playa", "La playa produce helados", "Un tercer factor, el calor, puede explicar ambas cosas."),
        ("ab", "Una investigación publicada hoy, ¿es una conclusión definitiva?", "No: es provisoria y puede cambiar con nueva evidencia", "Sí: lo publicado ya no cambia", "La investigación mejora con nueva información, por eso es provisoria."),
        ("abc", "{F} ¿Qué decisión sería proporcional si hay dudas y el error costaría poco?", "Probar los lomos en una calle y medir antes y después", "Instalarlos en todas las calles ya", "No hacer nada nunca", "Un paso reversible permite aprender antes de comprometer más."),
        ("abc", "{F} ¿Qué datos podrían cambiar la decisión de dónde poner más lomos?", "Conteos de velocidad por calle y reportes de incidentes", "El color de las calles", "El nombre de las calles", "Muestran dónde está el riesgo real."),
        ("abc", "{F} Una vecina dice: «Cuando se instalan lomos, baja la velocidad. Entonces donde baja la velocidad, es por los lomos». ¿Qué error hay?", "Puede haber otras causas de baja velocidad, como el tránsito o la hora", "Ninguno, porque es lógica válida", "La velocidad no se puede medir", "Afirma el consecuente: la baja de velocidad pudo tener otras causas."),
        ("abc", "{F} ¿Cuál es una frase que comunica la decisión con incertidumbre honesta?", "«Con la información actual, instalaremos lomos en la calle con más tránsito veloz y revisaremos en tres meses»", "«Está comprobado que los lomos eliminan el problema»", "«No sabemos nada, así que no haremos nada»", "Declara el límite y deja abierta la revisión."),
        ("abc", "¿Por qué una tradición no es una prueba de que algo sea correcto?", "Porque puede perpetuar errores que nunca se revisaron", "Porque todas las tradiciones son falsas", "Porque las tradiciones no son de nadie", "Que algo se haga hace mucho no demuestra que esté bien."),
        ("abc", "Dos fuentes de tipo distinto, un conteo y testimonios, coinciden en que una calle es peligrosa. ¿Qué aporta eso?", "Mayor confianza, aunque quedan límites por declarar", "Certeza absoluta", "Nada, porque son distintas", "La coincidencia independiente fortalece la conclusión sin hacerla infalible."),
    ],
    ctx=("abc", "Un liceo ficticio cambió el horario del recreo porque «un grupo de estudiantes dijo que así había menos peleas». Tres meses después, un registro de ejemplo muestra 20 peleas antes del cambio y 19 después. ¿Qué conviene concluir?", "Que casi no hay diferencia y hay que revisar la medida y su causa", "Que el cambio fue un gran éxito", "Que el registro es falso", "Un descenso de una pelea no respalda la afirmación inicial."),
    sc=[
        ("En Participación y argumentación: ¿qué significa que la investigación sea provisoria?", "Que puede cambiar si aparece nueva evidencia", "Los resultados se revisan con nueva información."),
        ("¿Qué es una decisión proporcional?", "La que guarda relación con la gravedad y el costo de equivocarse", "Con error caro se exige más evidencia; con error barato se puede probar."),
        ("¿Qué diferencia hay entre correlación y causa?", "La correlación es que ocurran juntas; la causa es que una produce la otra", "Coincidir en el tiempo no prueba que una produzca la otra."),
    ],
    op=("Elige uno. Caso 1: un liceo ficticio decidió quitar el kiosco porque «una nutricionista invitada dijo que vendía poco saludable», sin revisar lo que se vendía. Caso 2: una junta de vecinos ficticia instaló alarmas comunitarias porque «el año pasado hubo dos robos». "
        "Describe qué forma de conocimiento se usó, qué criterio falló, qué efecto pudo tener en la comunidad, y propone una corrección proporcional con la evidencia que reunirías.",
        "Caso 2. Forma: hechos aislados (dos robos). Criterio: suficiencia, pues dos casos no muestran una tendencia. Efecto: gasto en alarmas sin saber si reducen robos. Corrección: pedir al municipio un registro de delitos por mes y probar las alarmas en una cuadra, comparando antes y después.",
        ["identifica la forma de conocimiento y el criterio que falla", "explica el efecto posible en la comunidad", "propone una corrección proporcional y reversible"],
        ["texto de cinco a seis líneas con corrección propuesta"],
        ["atribuir mala fe sin evidencia", "proponer una corrección irreversible", "no distinguir correlación y causa"],
        "Pregunta: «¿cómo se sabría que la corrección funcionó?». Pide una medida concreta."),
    reinforce="Escribe una frase con incertidumbre honesta para comunicar una decisión basada en datos de solo dos meses.",
    extend="Explica cuándo conviene tomar una decisión aun con información incompleta y qué precauciones tomarías.",
)
