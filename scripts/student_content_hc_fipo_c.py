"""Filosofía política (electivo HC, 3.º y 4.º medio): OAC-05 (problemas sociales y desigualdad de género con perspectivas filosóficas, clases 1 a 5) y OAC-06 (argumentos válidos o falaces, clases 1 a 4). Casos y datos ficticios o de ejemplo."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada caso, dato y texto está escrito en el enunciado. "
             "Los lugares, las personas, los datos y los textos son ficticios o «de ejemplo»: sirven para practicar el razonamiento y no describen la realidad de ninguna institución. "
             "Las posturas se presentan con sus razones y sin tomar partido por un sector político: tu tarea es entenderlas, compararlas y evaluarlas con argumentos y respeto. "
             "Si un tema te incomoda, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O5 = "FI-FIPO-3y4-OAC-05"
O6 = "FI-FIPO-3y4-OAC-06"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (datos de ejemplo, ficticios). El club juvenil «Horizonte» (no existe) tiene 40 integrantes: 20 mujeres y 20 hombres. "
     "De sus 10 cargos de coordinación, 7 los ocupan hombres y 3 mujeres. "
     "En una conversación de ejemplo, varias integrantes comentan que dudan en postular porque «no se ve a mujeres en esos cargos».")
build(
    O5, 1, F,
    use="Aprenderé a convertir una situación de desigualdad de género en un problema de investigación: separar hechos de interpretaciones y formular una pregunta y una hipótesis.",
    prior=["Sé formular una pregunta filosófica y una hipótesis.", "Sé qué es un porcentaje.", "Distingo un hecho de una interpretación."],
    explain=[
        "La desigualdad de género es una diferencia en oportunidades, recursos, poder o trato entre personas según su género, que no se justifica por razones válidas. Para investigarla como problema social se parte de una situación concreta, se delimita su contexto (dónde, quiénes, cuándo) y se separan tres cosas: los hechos (datos que se pueden comprobar), las interpretaciones (explicaciones posibles de esos datos) y las valoraciones (juicios sobre si es justo).",
        "Una pregunta de investigación puede ser descriptiva (¿qué ocurre?), explicativa (¿por qué ocurre?) o normativa (¿es justo y qué debería hacerse?). Una hipótesis es una respuesta tentativa que se podrá apoyar o rechazar con evidencia y argumentos. Los porcentajes ayudan a describir: si 7 de 10 cargos los ocupan hombres, se dice que ocupan el 70 % de los cargos.",
        "Un dato por sí solo no explica nada: muestra una diferencia, y varias explicaciones pueden dar cuenta de ella. Por eso se necesita evidencia adicional y perspectivas filosóficas distintas. En este cuaderno los casos y datos son de ejemplo: sirven para practicar el método y no describen a ninguna institución real.",
    ],
    vocab=[("desigualdad de género", "diferencia en oportunidades, recursos, poder o trato según el género que no se justifica"), ("hecho", "dato que se puede comprobar"), ("interpretación", "explicación posible de un dato"), ("valoración", "juicio sobre si algo es justo o injusto"), ("pregunta explicativa", "pregunta que busca el porqué de un fenómeno"), ("delimitar", "precisar dónde, quiénes y cuándo se estudia un problema")],
    worked=[
        ("Separar hecho e interpretación", "De la ficha: «Hay 7 hombres y 3 mujeres en los cargos» y «Las mujeres no postulan porque no les interesa». ¿Cuál es hecho y cuál interpretación?",
         ["La primera frase se puede comprobar contando los cargos.", "La segunda propone una explicación que los datos no prueban."],
         "La primera es un hecho de ejemplo; la segunda, una interpretación"),
        ("Formular una pregunta explicativa", "Formula una pregunta explicativa sobre el club de la ficha.",
         ["Veo la diferencia: la mitad de integrantes son mujeres y una minoría ocupa cargos.", "Pregunto por el porqué de esa diferencia, sin responderla de antemano."],
         "¿Qué factores influyen en que menos mujeres ocupen cargos de coordinación en el club Horizonte?"),
    ],
    mistakes=[("Pasar de un dato a una explicación como si el dato la probara.", "Se confunde hecho con interpretación.", "Plantea la explicación como hipótesis y busca evidencia."),
              ("Formular una pregunta tan amplia que no se puede investigar («¿Hay desigualdad?»).", "Falta delimitar quiénes, dónde y cuándo.", "Precisa el contexto y el aspecto que se estudia.")],
    T=[
        ("=", "{F} ¿Qué porcentaje de las 40 personas integrantes del club son mujeres?", "20*100//40", "Se divide 20 mujeres entre 40 integrantes y se multiplica por 100.", " %"),
        ("=", "{F} Si las mujeres ocuparan los cargos de coordinación en la misma proporción en que son integrantes del club, ¿cuántos de los 10 cargos ocuparían?", "10*20//40", "Se calcula la parte de 10 cargos que corresponde a 20 de cada 40 integrantes."),
        ("abc", "{F} ¿Cuál de estas frases es un hecho de ejemplo?", "El club tiene 20 mujeres y 20 hombres", "Las integrantes se sienten poco bienvenidas en los cargos", "El club debería repartir los cargos por igual", "Se puede comprobar contando; la segunda es una interpretación y la tercera una valoración."),
        ("abc", "{F} ¿Cuál de estas frases es una valoración?", "Es injusto que casi nadie vea mujeres en los cargos", "Hay 7 hombres en los cargos", "El club tiene 40 integrantes", "Afirma un juicio sobre lo justo y no un dato."),
        ("abc", "En una biblioteca juvenil ficticia, 9 de las 12 personas voluntarias del turno de tarde son mujeres. ¿Cuál es una pregunta explicativa?", "¿Por qué el turno de tarde reúne a más mujeres que hombres?", "¿Cuántas personas voluntarias hay en el turno de tarde?", "¿Debe cerrarse el turno de tarde?", "Busca el porqué de la diferencia, no solo el dato ni una decisión."),
        ("ab", "{F} ¿Qué pregunta está mejor delimitada?", "¿Por qué hay menos mujeres que hombres en los cargos de coordinación del club Horizonte?", "¿Hay desigualdad en el mundo?", "La primera dice dónde, quiénes y qué aspecto se estudia."),
        ("abc", "{F} ¿Cuál es una hipótesis que se puede poner a prueba?", "Las integrantes postulan menos porque perciben que esos cargos no se les asignan, por la ausencia de modelos", "Los cargos deberían repartirse por igual", "El club tiene diez cargos de coordinación", "Propone una explicación con una razón que se podría examinar con evidencia adicional."),
        ("abc", "{F} ¿Qué dato adicional ayudaría más a evaluar la hipótesis anterior?", "Cuántas mujeres y cuántos hombres postularon a cada cargo", "El año en que se fundó el club", "El nombre de quien fundó el club", "Permite saber si la diferencia está en las postulaciones o en la selección."),
        ("abc", "Un grupo de curso ficticio dice: «En nuestro taller hay 4 mujeres y 8 hombres; por eso el taller discrimina». ¿Qué falta para sostener esa conclusión?", "Evidencia sobre cómo se postula y se selecciona, porque el número por sí solo no explica el porqué", "Nada, porque ya hay un dato", "Más estudiantes en el taller", "Un dato muestra una diferencia, pero no prueba una causa."),
        ("abc", "{F} ¿Qué tipo de pregunta es «¿Qué debería hacer el club para que más mujeres ocupen cargos?»?", "Normativa", "Descriptiva", "Explicativa", "Pregunta qué debería hacerse, es decir, un deber."),
        ("{F} La frase de las integrantes (no se ve a mujeres en esos cargos), ¿es un hecho comprobable o una percepción que hay que examinar? Justifica.", "Es una percepción que hay que examinar, aunque el dato de 3 mujeres entre 10 cargos la apoya parcialmente", "Una percepción puede orientar la investigación, y los datos permiten contrastarla."),
        ("abc", "{F} Una estudiante concluye: «Los hombres del club excluyen a las mujeres». ¿Qué error comete?", "Atribuye una intención a personas concretas sin evidencia", "Usa un porcentaje mal calculado", "Cambia el tema del problema", "Pasa del dato a una explicación sobre intenciones sin evidencia."),
        ("abc", "{F} Para dar un primer paso de investigación responsable, ¿qué conviene hacer?", "Delimitar el contexto, separar hechos de interpretaciones y formular una hipótesis", "Escribir quién tiene la culpa", "Elegir una solución inmediata", "Es el método que enseña la clase."),
    ],
    ctx=("abc", "En un liceo ficticio, un delegado observa que en el centro de estudiantes casi todas las vocerías las ocupan hombres. Quiere investigar. ¿Cuál es su mejor primer paso?", "Anotar cuántas personas de cada género hay en el curso y en los cargos, y formular una pregunta explicativa", "Acusar a la directiva", "Hacer una campaña inmediata", "Describir los datos y delimitar la pregunta permite luego buscar explicaciones."),
    sc=[
        ("En Filosofía política: ¿qué es la desigualdad de género?", "Una diferencia en oportunidades, recursos, poder o trato según el género que no se justifica", "Es la definición de la clase."),
        ("¿Qué diferencia hay entre hecho e interpretación?", "El hecho se puede comprobar y la interpretación explica el hecho", "La interpretación debe ponerse a prueba."),
        ("¿Por qué un dato no basta para afirmar una causa?", "Porque varias explicaciones pueden dar cuenta de la misma diferencia", "Hace falta evidencia adicional para pasar del dato a una causa."),
    ],
    op=("Elige una situación ficticia: (1) en un taller de ciencias hay 14 estudiantes y solo 4 son mujeres; (2) en un grupo de voluntariado, las tareas de organizar la sala las hacen siempre las mismas personas, todas del mismo género. "
        "Separa un hecho, una interpretación y una valoración, formula una pregunta explicativa delimitada y una hipótesis con una razón.",
        "Situación 1. Hecho: 4 de 14 estudiantes son mujeres. Interpretación: quizá no se sienten invitadas. Valoración: es injusto que haya tan pocas. Pregunta: ¿qué factores influyen en que haya menos mujeres en el taller de ciencias de este curso? Hipótesis: influye que la invitación al taller no llega por igual.",
        ["distingue hecho, interpretación y valoración", "formula una pregunta explicativa delimitada", "la hipótesis incluye una razón", "no atribuye intenciones sin evidencia"],
        ["registro con hecho, interpretación, valoración, pregunta e hipótesis"],
        ["tratar una interpretación como hecho", "formular una pregunta demasiado amplia", "atribuir intenciones a personas"],
        "Pregunta: «¿qué dato ayudaría a poner a prueba tu hipótesis?». Pídele que lo nombre."),
    reinforce="Anota una situación de tu entorno que te haga pensar en igualdad de género y sepárala en hecho, interpretación y valoración.",
    extend="Escribe tres hipótesis posibles para una misma diferencia y ordénalas según qué evidencia necesitaría cada una.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (glosario de ejemplo). "
     "Género: ideas, roles y expectativas que una sociedad asocia con ser mujer, hombre u otras identidades. "
     "Estereotipo de género: creencia simplificada y rígida sobre cómo son o deben ser las personas según su género. "
     "Discriminación: trato desfavorable a una persona por una característica, como su género, sin justificación razonable. "
     "Igualdad formal: mismos derechos ante la ley. Igualdad de oportunidades: que nada injustificado limite el acceso a un bien o cargo. Igualdad de resultados: que los resultados se distribuyan de modo parecido entre grupos. "
     "Brecha: diferencia medible entre grupos.")
build(
    O5, 2, F,
    use="Aprenderé a definir con precisión género, estereotipo, discriminación, brecha y tres tipos de igualdad, y a usarlos para analizar casos.",
    prior=["Sé distinguir hecho, interpretación y valoración.", "Sé buscar un contraejemplo.", "Sé qué es una brecha en un dato."],
    explain=[
        "Para estudiar la desigualdad de género con rigor hay que definir bien los términos. El género es el conjunto de ideas, roles y expectativas que una sociedad asocia con ser mujer, hombre u otras identidades. Un estereotipo de género es una creencia simplificada y rígida sobre cómo son o deben ser las personas según su género. La discriminación es un trato desfavorable sin justificación razonable. La brecha es una diferencia medible entre grupos.",
        "Existen distintos sentidos de igualdad. La igualdad formal exige los mismos derechos ante la ley. La igualdad de oportunidades exige que nada injustificado limite el acceso a un bien o cargo. La igualdad de resultados exige que lo logrado se distribuya de modo parecido entre grupos. Una situación puede cumplir la primera y no la segunda: la ley permite postular a todas las personas, pero un horario o una costumbre limita a algunas.",
        "Una postura asociada con la filósofa Simone de Beauvoir sostiene que muchos rasgos que se asignan a las mujeres no son naturales sino aprendidos socialmente. No todas las posturas coinciden con ella, y en esta clase se examina como perspectiva. Definir con precisión evita discutir sin entenderse y permite contrastar casos con criterios claros.",
    ],
    vocab=[("género", "ideas, roles y expectativas que una sociedad asocia con ser mujer, hombre u otras identidades"), ("estereotipo de género", "creencia simplificada y rígida sobre cómo son o deben ser las personas según su género"), ("discriminación", "trato desfavorable sin justificación razonable por una característica como el género"), ("igualdad formal", "mismos derechos ante la ley"), ("igualdad de oportunidades", "que nada injustificado limite el acceso a un bien o cargo"), ("brecha", "diferencia medible entre grupos")],
    worked=[
        ("Clasificar un caso", "Una academia ficticia permite postular a todas las personas, pero fija las clases a una hora en que quienes cuidan a familiares no pueden asistir. ¿Cumple igualdad formal y de oportunidades?",
         ["Todas pueden postular: cumple igualdad formal.", "El horario limita a quienes cuidan a familiares: puede incumplir la igualdad de oportunidades."],
         "Cumple la igualdad formal y puede no cumplir la igualdad de oportunidades"),
        ("Reconocer un estereotipo", "Un profesor ficticio dice: «Las mujeres no son buenas en robótica». ¿Qué es esa afirmación?",
         ["Es una creencia general y rígida sobre un grupo.", "No distingue a cada persona ni ofrece evidencia."],
         "Un estereotipo de género"),
    ],
    mistakes=[("Creer que si la ley no distingue, no puede haber desigualdad.", "Se confunde igualdad formal con igualdad de oportunidades.", "Revisa si hay barreras prácticas aunque la ley sea igual para todos."),
              ("Usar «discriminación» para cualquier diferencia.", "Se pierde el rasgo de trato desfavorable sin justificación razonable.", "Pregunta si el trato desfavorable tiene o no una justificación razonable.")],
    T=[
        ("abc", "{F} ¿Qué es un estereotipo de género?", "Una creencia simplificada y rígida sobre cómo son o deben ser las personas según su género", "Una ley sobre los derechos de las mujeres", "Una diferencia medible entre grupos", "Así define la ficha del glosario ese término."),
        ("abc", "{F} ¿Qué es una brecha?", "Una diferencia medible entre grupos", "Una creencia rígida", "Un trato desfavorable", "Así define la ficha del glosario esa palabra."),
        ("abc", "{F} ¿Qué exige la igualdad formal?", "Los mismos derechos ante la ley", "Que los resultados sean iguales", "Que todos tengan el mismo cargo", "Es la definición que da el glosario de la ficha."),
        ("abc", "{F} Un reglamento ficticio exige a las mujeres un puntaje mayor que a los hombres para ingresar, sin ninguna razón. ¿Qué es?", "Discriminación", "Estereotipo", "Brecha", "Es un trato desfavorable por género sin justificación razonable."),
        ("abc", "{F} En un liceo ficticio, 70 % de los puestos de delegado los ocupan hombres, y 50 % del alumnado son hombres. ¿Qué es esa diferencia entre 70 % y 50 %?", "Una brecha", "Un estereotipo", "Una discriminación comprobada", "Es una diferencia medible entre grupos, pero no prueba por sí sola una causa."),
        ("abc", "{F} Un concurso ficticio permite que cualquier persona postule, pero el premio se entrega en un lugar al que algunas no pueden llegar por falta de transporte. ¿Qué igualdad falla?", "La de oportunidades", "La formal", "Ninguna", "Todas pueden postular, pero hay una barrera práctica."),
        ("abc", "{F} Una empresa ficticia dice: «Buscamos una persona de oficina; si es hombre, mejor, porque las mujeres se distraen». ¿Qué ocurre?", "Un estereotipo que lleva a un trato desfavorable", "Igualdad formal", "Igualdad de resultados", "Una creencia rígida se usa como razón para preferir."),
        ("abc", "En un concurso ficticio todas las personas pueden postular, y los 10 cargos ganados el año pasado fueron 8 de hombres y 2 de mujeres. ¿Qué es correcto afirmar?", "La igualdad de resultados no se cumple, pero falta evidencia para saber si falla la de oportunidades", "La igualdad formal falla, porque la ley es injusta", "Todas las igualdades se cumplen, porque todas pudieron postular", "Hay una brecha en los resultados, y para decidir si hubo barreras hace falta averiguar cómo se postuló y se seleccionó."),
        ("abc", "¿En qué se diferencian igualdad de oportunidades e igualdad de resultados?", "La primera mira las barreras de acceso y la segunda cómo se distribuyen los logros", "Son lo mismo", "La primera es una ley", "Se distinguen por lo que miden."),
        ("abc", "{F} Una estudiante dice: «Si hay una brecha, hay discriminación». ¿Qué falla tiene?", "Una brecha es una diferencia medible y no prueba por sí sola que haya trato desfavorable injustificado", "Es una frase correcta", "Confunde género con brecha", "Hace falta mostrar que hay trato desfavorable sin justificación."),
        ("abc", "Una postura asociada con Simone de Beauvoir sostiene que muchos rasgos asignados a las mujeres…", "Son aprendidos socialmente y no naturales", "Son siempre biológicos", "Son imposibles de cambiar", "Así resume la explicación esa postura asociada con Beauvoir."),
        ("abc", "{F} Un alumno dice: «Los estereotipos son solo bromas, no afectan a nadie». ¿Cuál es la mejor respuesta?", "Pueden orientar decisiones y limitar oportunidades de las personas", "Tiene razón porque son pequeños", "Solo afectan a quienes los dicen", "Un estereotipo puede orientar trato y expectativas."),
        ("abc", "{F} ¿Cómo corregirías la definición «Discriminación es cualquier diferencia entre mujeres y hombres»?", "Agregando el rasgo de trato desfavorable sin justificación razonable", "Dejándola como está", "Sustituyendo «diferencia» por «brecha medible»", "La definición original es demasiado amplia."),
    ],
    ctx=("abc", "Un municipio ficticio abre becas para estudiar un oficio técnico. Pueden postular todas las personas, pero la postulación solo se hace presencialmente de lunes a viernes por la mañana. Una vecina que trabaja de lunes a viernes no puede asistir. ¿Qué se puede decir?", "Cumple igualdad formal, pero puede fallar la igualdad de oportunidades", "Cumple todos los tipos de igualdad", "No hay ninguna barrera", "El horario crea una barrera práctica aunque la regla sea igual para todos."),
    sc=[
        ("En Filosofía política: ¿qué es la igualdad de oportunidades?", "Que nada injustificado limite el acceso a un bien o cargo", "Se distingue de la igualdad formal."),
        ("¿Qué es el género según la ficha?", "Ideas, roles y expectativas que una sociedad asocia con ser mujer, hombre u otras identidades", "Es la definición que ofrece el glosario de la ficha."),
        ("¿Por qué una brecha no prueba por sí sola una discriminación?", "Porque es una diferencia medible y falta mostrar el trato desfavorable sin justificación", "Se necesita evidencia adicional que muestre dónde ocurre la diferencia."),
    ],
    op=("Elige un caso ficticio: (1) un club de debate ofrece cupos iguales, pero reúne a sus integrantes de noche, cuando muchas personas no pueden salir; (2) una guía escolar usa solo ejemplos de personas de un género en roles de liderazgo. "
        "Aplica al caso al menos tres términos de la ficha, indica qué tipo de igualdad se cumple y cuál no, y propone un cambio posible.",
        "Caso 1. Igualdad formal: se cumple, los cupos son iguales. Igualdad de oportunidades: puede fallar por el horario. Posible barrera: transporte y seguridad nocturna. Cambio: reunirse en un horario alcanzable para todas las personas.",
        ["usa al menos tres términos correctamente", "indica qué igualdad se cumple y cuál no", "propone un cambio pertinente", "no atribuye intenciones sin evidencia"],
        ["análisis con tres términos y una propuesta de cambio"],
        ["decir que hay discriminación sin mostrar trato desfavorable", "confundir igualdad formal con de oportunidades", "proponer un cambio que no responde al problema"],
        "Pregunta: «¿qué barrera práctica aparece en tu caso aunque la regla sea igual?». Pídele que la nombre."),
    reinforce="Escribe tu propia definición de «estereotipo de género» y un ejemplo ficticio.",
    extend="Explica con un ejemplo cómo una norma igual para todas las personas puede producir resultados distintos.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (resúmenes de ejemplo; no son las obras completas). Cuatro perspectivas filosóficas sobre la desigualdad de género. "
     "P1 (igualitarismo liberal): lo central es garantizar iguales derechos y oportunidades eliminando barreras injustificadas, para que cada persona decida su vida. "
     "P2 (ética del cuidado, asociada con Carol Gilligan y otras autoras): el cuidado y la interdependencia son valores centrales; el trabajo de cuidar suele ser poco visible y estar repartido de modo desigual. "
     "P3 (construcción social del género, asociada con Simone de Beauvoir): muchos rasgos asignados según el género se aprenden; cambiar expectativas es parte de la solución. "
     "P4 (distinción entre oportunidades y resultados): las diferencias de resultados pueden deberse a elecciones libres; antes de corregir hay que mostrar que existen barreras o trato injusto.")
build(
    O5, 3, F,
    use="Aprenderé a reconstruir cuatro perspectivas filosóficas sobre la desigualdad de género y a aplicarlas a un caso con sus razones y límites.",
    prior=["Sé la diferencia entre igualdad formal, de oportunidades y de resultados.", "Sé reconstruir una perspectiva.", "Sé formular una objeción."],
    explain=[
        "Las perspectivas filosóficas ofrecen lentes distintas para entender un problema social. Ninguna se reduce a una opinión: cada una tiene razones, supuestos sobre las personas y límites. En esta clase se presentan cuatro resúmenes de ejemplo: un igualitarismo liberal, que pone el acento en derechos y oportunidades; una ética del cuidado, que destaca la interdependencia; una mirada de construcción social del género, que cuestiona lo que parece natural; y una postura que distingue oportunidades de resultados y pide mostrar las barreras antes de corregir.",
        "Aplicar una perspectiva consiste en preguntar qué ve ella en un caso. P1 pregunta qué barreras injustificadas hay. P2 pregunta quién cuida y si ese trabajo se reconoce y reparte. P3 pregunta qué expectativas se aprendieron y cómo se mantienen. P4 pregunta si hay evidencia de que la diferencia proviene de barreras y no de decisiones libres.",
        "Comparar perspectivas no es elegir la más simpática. Es mostrar qué ilumina cada una y qué deja sin explicar. Un mismo caso puede entenderse mejor combinando dos de ellas. Y se cuida el rigor: se habla de «una perspectiva asociada con…» y no se atribuye a una autora más de lo que sabemos.",
    ],
    vocab=[("igualitarismo liberal", "perspectiva centrada en iguales derechos y oportunidades"), ("ética del cuidado", "perspectiva que valora el cuidado y la interdependencia"), ("construcción social", "idea de que ciertos rasgos se aprenden en sociedad"), ("interdependencia", "necesidad que las personas tienen unas de otras"), ("barrera injustificada", "obstáculo que limita el acceso sin razón válida"), ("elección libre", "decisión tomada sin presión injusta")],
    worked=[
        ("Aplicar P2", "En un grupo de voluntariado ficticio, las tareas de preparar y ordenar la sala las hacen siempre las mismas tres personas, que son mujeres, sin que nadie lo decidiera formalmente. ¿Qué preguntaría P2?",
         ["P2 mira quién cuida y si ese trabajo se reconoce y reparte.", "Preguntaría por qué esas tareas recaen siempre en las mismas personas y cómo se valoran."],
         "¿Por qué ese trabajo de cuidado recae siempre en las mismas personas y se reconoce poco?"),
        ("Contrastar dos lentes", "Para el mismo caso, ¿qué preguntaría P4?",
         ["P4 distingue oportunidades de resultados.", "Preguntaría si hay barreras o trato injusto, o si las personas eligieron libremente esas tareas."],
         "¿Hay evidencia de barreras o las personas eligieron libremente esas tareas?"),
    ],
    mistakes=[("Elegir una perspectiva porque «me cae bien» y no por lo que explica.", "Se confunde perspectiva con opinión sin razones.", "Justifica la elección diciendo qué muestra y qué deja sin explicar."),
              ("Atribuir a una autora ideas que no figuran en el resumen.", "Se confunde el resumen con la obra.", "Di «una perspectiva asociada con…» y limita la atribución al resumen.")],
    T=[
        ("abc", "{F} ¿Qué pregunta hace P1?", "¿Qué barreras injustificadas limitan derechos y oportunidades?", "¿Quién cuida y cómo se reconoce ese trabajo?", "¿Qué expectativas se aprendieron?", "P1 se centra en derechos y oportunidades."),
        ("abc", "{F} ¿Qué pregunta hace P2?", "¿Quién cuida y se reconoce ese trabajo?", "¿Hay barreras legales?", "¿Qué se elige libremente?", "P2 destaca el cuidado y la interdependencia."),
        ("abc", "{F} ¿Qué pregunta hace P3?", "¿Qué expectativas se aprendieron y cómo se mantienen?", "¿Quién cuida?", "¿Hay evidencia de barreras?", "P3 destaca que ciertos rasgos se aprenden."),
        ("abc", "{F} Una comisión ficticia propone corregir una diferencia de resultados en un concurso, pero antes pide mostrar si hubo barreras o trato injusto. ¿Con qué perspectiva coincide?", "Con P4", "Con P2", "Con P3", "P4 pide mostrar barreras o trato injusto antes de corregir."),
        ("abc", "{F} Un club ficticio publica solo fotos de hombres en sus cargos de liderazgo, y las socias creen que «el liderazgo es de hombres». ¿Qué perspectiva ayuda más a ver cómo se mantiene esa creencia?", "P3", "P1", "P4", "Muestra cómo se aprenden y mantienen las expectativas."),
        ("abc", "{F} Una ley ficticia prohíbe contratar solo hombres para un cargo, pero igual las postulantes son pocas. ¿Qué perspectiva mira primero las barreras de acceso?", "P1", "P2", "P4", "P1 pregunta por barreras injustificadas en derechos y oportunidades."),
        ("abc", "{F} Un equipo ficticio nota que las reuniones se hacen cuando muchas personas cuidan a familiares. ¿Qué perspectiva destaca esta realidad?", "P2", "P3", "P4", "P2 pone el cuidado y la interdependencia en el centro."),
        ("abc", "{F} Una estudiante dice: «P1 y P3 son lo mismo, porque las dos quieren cambiar cosas». ¿Qué falla tiene?", "P1 se centra en eliminar barreras injustificadas de derechos y oportunidades, y P3 en cuestionar expectativas aprendidas", "Ninguna, porque las dos tienen el mismo criterio", "P1 y P3 se refieren al cuidado", "Cada perspectiva destaca aspectos distintos y se debe respetar lo que cada una dice."),
        ("abc", "{F} ¿Cuál es un límite posible de P4?", "Puede dejar de lado cómo las expectativas influyen en lo que parece una elección libre", "Considera que toda diferencia es discriminación", "Rechaza que existan barreras en cualquier caso", "P3 podría objetarle que las elecciones también se ven influidas por expectativas aprendidas."),
        ("abc", "{F} ¿Cuál es un límite posible de P1?", "Puede no ver el trabajo de cuidado y las costumbres que sostienen la desigualdad aunque las leyes sean iguales", "Niega que las personas puedan decidir su vida", "Solo habla de cuidado", "P2 y P3 podrían señalar lo que P1 deja en segundo plano."),
        ("abc", "{F} Una estudiante dice: «Elijo P2 porque me gusta». ¿Qué falta?", "Explicar qué muestra P2 en el caso y qué deja sin explicar", "Citar a la autora completa", "Cambiar de perspectiva", "Elegir una perspectiva exige razones sobre lo que ilumina en el caso."),
        ("abc", "{F} Para entender un reparto desigual de tareas de cuidado en un grupo ficticio, ¿qué combinación de perspectivas es útil?", "P2 y P3, porque muestran quién cuida y qué expectativas lo sostienen", "Solo P1, por ser la más conocida", "Solo P4", "Combina la mirada sobre el cuidado con la de las expectativas aprendidas."),
        ("abc", "{F} Un periodista ficticio escribe: «Según Beauvoir, todo es social». ¿Qué problema tiene?", "Atribuye más de lo que dice el resumen, que habla de «muchos rasgos»", "Es correcto, porque Beauvoir lo afirma en el resumen", "Confunde a las autoras", "El resumen no afirma que todo sea social."),
    ],
    ctx=("abc", "Una escuela de oficios ficticia observa que casi todas las personas inscritas en electricidad son hombres, y que en cuidado infantil casi todas son mujeres. ¿Qué pregunta de P3 ayuda a investigar?", "¿Qué expectativas aprendidas orientan la elección de cada oficio?", "¿Qué ley prohíbe elegir?", "¿Cuál oficio es mejor?", "P3 se ocupa de las expectativas aprendidas."),
    sc=[
        ("En Filosofía política: ¿qué destaca la ética del cuidado?", "El cuidado y la interdependencia", "Es su eje, según la ficha."),
        ("¿Qué pide P4 antes de corregir una diferencia de resultados?", "Mostrar que existen barreras o trato injusto", "Evita atribuir toda diferencia a discriminación."),
        ("¿Por qué una perspectiva no es una opinión sin razones?", "Porque tiene razones, supuestos sobre las personas y límites", "Se justifica por lo que muestra."),
    ],
    op=("Elige un caso ficticio: (1) un grupo de curso reparte siempre las tareas de cocina del paseo a las mismas personas; (2) una olimpiada de matemática tiene pocas postulantes mujeres. "
        "Aplica dos perspectivas de la ficha: qué pregunta haría cada una, qué podrían ver o no ver, y cuál sería tu primera pregunta de investigación combinando ambas.",
        "Caso 1. P2: ¿por qué esas tareas recaen en las mismas personas y se reconocen poco? P3: ¿qué expectativas aprendidas lo sostienen? P2 no ve las expectativas; P3 no ve el reconocimiento del trabajo. Primera pregunta: ¿qué ideas sobre «quién cuida» influyen en cómo reparte las tareas el grupo?",
        ["aplica correctamente dos perspectivas", "indica lo que cada una deja sin ver", "formula una pregunta de investigación que combina ambas", "no atribuye más de lo que dice el resumen"],
        ["aplicación de dos perspectivas con pregunta de investigación"],
        ["elegir por gusto", "atribuir a una autora ideas que no están", "no mencionar los límites"],
        "Pregunta: «¿qué ve tu segunda perspectiva que la primera no ve?». Pídele que lo escriba."),
    reinforce="Elige una situación de tu entorno y explica qué perspectiva de la ficha la ilumina mejor y por qué.",
    extend="Escribe una quinta perspectiva posible y la pregunta que haría a un caso.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (argumento de ejemplo). «En el club Horizonte, 3 de los 10 cargos de coordinación los ocupan mujeres, aunque la mitad de las integrantes lo son. "
     "En otro club vecino, 4 de 10. Por lo tanto, todos los clubes juveniles discriminan a las mujeres, y la solución es exigir que la mitad de los cargos sea de mujeres.»")
build(
    O5, 4, F,
    use="Aprenderé a evaluar con rigor un argumento sobre desigualdad de género: a detectar generalizaciones apresuradas, a distinguir correlación de causa y a pedir evidencia.",
    prior=["Sé separar hecho, interpretación y valoración.", "Sé reconstruir premisas y conclusión.", "Conozco cuatro perspectivas sobre desigualdad de género."],
    explain=[
        "La rigurosidad argumentativa consiste en que las conclusiones se apoyen en razones y evidencia suficientes. Cuatro cuidados ayudan. Definir los términos usados (¿qué es discriminar?). Indicar la fuente y la muestra de los datos (¿cuántos casos, de dónde?). Evitar la generalización apresurada, que es concluir sobre todos a partir de pocos casos. Distinguir correlación de causa: que dos cosas ocurran juntas no prueba que una cause la otra.",
        "También hay que considerar explicaciones alternativas. Una diferencia puede deberse a barreras, a expectativas aprendidas, a decisiones libres o a varias cosas a la vez; un buen argumento muestra por qué descarta algunas. Y hay que separar el diagnóstico (qué ocurre y por qué) de la propuesta (qué hacer): la propuesta necesita su propio argumento.",
        "Un argumento riguroso reconoce sus límites: dice qué muestra la evidencia disponible y qué no. Eso no lo debilita, sino que lo hace creíble. Los datos de esta clase son de ejemplo y no describen a clubes reales.",
    ],
    vocab=[("rigurosidad", "cuidado de apoyar las conclusiones en razones y evidencia suficientes"), ("muestra", "conjunto de casos que se observan"), ("generalización apresurada", "concluir sobre todos a partir de pocos casos"), ("correlación", "que dos cosas ocurran juntas"), ("causa", "factor que produce un efecto"), ("explicación alternativa", "otra manera posible de dar cuenta de un dato")],
    worked=[
        ("Detectar una generalización apresurada", "En la ficha, ¿qué falla tiene concluir que «todos los clubes juveniles discriminan»?",
         ["El argumento observa solo dos clubes.", "Concluye sobre todos los clubes juveniles a partir de dos casos."],
         "Es una generalización apresurada"),
        ("Distinguir correlación y causa", "En la ficha, 3 de 10 cargos son de mujeres. ¿Eso prueba que el club impide que ocupen cargos?",
         ["El dato muestra una diferencia, no su causa.", "Podría deberse a barreras, a pocas postulaciones u otras razones."],
         "No lo prueba; hace falta evidencia sobre las causas"),
    ],
    mistakes=[("Concluir una causa directamente desde una diferencia en un dato.", "Se confunde correlación con causa.", "Formula la causa como hipótesis y busca evidencia."),
              ("Proponer una solución sin mostrar que responde a la causa identificada.", "La propuesta no tiene su propio argumento.", "Explica cómo la solución se relaciona con la causa que investigaste.")],
    T=[
        ("=", "{F} Entre los dos clubes suman 20 cargos de coordinación. ¿Qué porcentaje de esos 20 cargos ocupan mujeres?", "(3+4)*100//20", "Se suman 3 y 4 cargos de mujeres, se dividen entre 20 y se multiplica por 100.", " %"),
        ("=", "{F} Para llegar a la mitad de sus 10 cargos, ¿cuántos cargos más deberían ocupar mujeres en el club Horizonte?", "10//2-3", "La mitad de 10 cargos es 5 y las mujeres ya ocupan 3."),
        ("abc", "{F} El argumento no dice de dónde salen los datos ni cómo se contaron. ¿Qué cuidado de rigor no cumple?", "Indicar la fuente y la muestra de los datos", "Definir los términos usados", "Distinguir correlación de causa", "Sin fuente ni muestra no se puede evaluar cuán confiables son los datos."),
        ("abc", "{F} ¿Cuál es la premisa de apoyo en la ficha?", "Que en dos clubes hay menos mujeres que hombres en cargos", "Que todos los clubes discriminan", "Que se debe exigir paridad", "Las dos primeras oraciones entregan los datos."),
        ("abc", "{F} ¿Cuál de estas conclusiones se sigue de los datos de ejemplo sobre el club Horizonte?", "Las mujeres ocupan menos cargos de coordinación que su proporción entre las integrantes", "Todos los clubes juveniles discriminan a las mujeres", "El club Horizonte excluye a las mujeres a propósito", "Es lo que muestran los datos: 3 de 10 cargos frente a la mitad de las integrantes; las otras conclusiones exceden la evidencia."),
        ("abc", "{F} ¿Qué evidencia adicional ayudaría a evaluar si hay barreras en el club Horizonte?", "Cuántas personas de cada género postularon y cómo se seleccionó a quienes ocupan los cargos", "El presupuesto anual del club", "La cantidad de integrantes del club vecino", "Permite ver dónde ocurre la diferencia."),
        ("abc", "{F} Un estudiante dice: «Si hay 30 % de mujeres en cargos y 50 % de integrantes, es evidente que se las excluye a propósito». ¿Qué falla tiene?", "Atribuye una intención sin evidencia", "Calcula mal el porcentaje", "Compara clubes distintos", "El dato solo muestra una diferencia y no las intenciones de nadie."),
        ("abc", "{F} ¿Qué explicación alternativa a la discriminación podría considerarse?", "Que haya habido pocas postulaciones de mujeres por razones que hay que averiguar", "Que todas las mujeres prefieren no ocupar cargos", "Ninguna: un dato ya demuestra la discriminación", "Es una explicación que se debe examinar con evidencia, sin dar por cierta ninguna."),
        ("abc", "{F} ¿Por qué la propuesta de exigir la mitad de los cargos necesita su propio argumento?", "Porque no se desprende automáticamente del diagnóstico y requiere razones y objeciones propias", "Porque es una opinión que no importa", "Porque ya está probada", "Una propuesta se evalúa con razones sobre su pertinencia y efectos."),
        ("abc", "{F} Una estudiante reformula: «En dos clubes de ejemplo se observa una diferencia; hace falta indagar sus causas antes de proponer una medida». ¿Qué mejora?", "Reconoce los límites de la evidencia y pide investigar", "Afirma que no hay diferencia en los clubes", "Acusa a los clubes", "Es una conclusión proporcionada a la evidencia."),
        ("abc", "{F} Si se quisiera usar el argumento para todo un país, ¿qué haría falta?", "Una muestra amplia y con criterios claros, no solo dos clubes", "Más propuestas de solución", "Un cargo más en cada club", "Una generalización requiere una muestra suficiente."),
        ("abc", "{F} ¿Cuál es el término definido que el argumento usa sin precisar?", "Discriminar", "Club", "Cargo", "No explica qué entiende por discriminar."),
        ("abc", "Un grupo ficticio observa que las ventas de helado y los accidentes en piscina suben juntos y concluye que los helados causan accidentes. ¿Qué error ilustra?", "Confundir correlación con causa", "Generalizar desde un solo caso", "Atacar a una persona", "Ambos aumentan en verano y no se prueba que uno cause el otro."),
    ],
    ctx=("abc", "Un diario escolar ficticio escribe: «Como en el curso A hay menos mujeres en robótica, las mujeres no son buenas para la tecnología». ¿Cuál es la mejor corrección?", "Con un solo curso no se puede concluir sobre las mujeres en general; hay que averiguar por qué ocurre la diferencia", "Está bien escrito", "Hay que borrar el dato", "Corrige la generalización y pide explicar la causa."),
    sc=[
        ("En Filosofía política: ¿qué es una generalización apresurada?", "Concluir sobre todos a partir de pocos casos", "Se evita ampliando la muestra y precisando cuántos casos se observaron."),
        ("¿Por qué la correlación no prueba una causa?", "Porque dos cosas pueden ocurrir juntas sin que una cause la otra", "Pueden existir otras explicaciones que expliquen la misma coincidencia."),
        ("¿Por qué reconocer límites fortalece un argumento?", "Porque lo hace proporcionado a la evidencia y creíble", "Dice con honestidad qué muestran los datos."),
    ],
    op=("Lee este argumento de ejemplo: «En el curso B, 2 de 12 delegadas del año pasado fueron mujeres. Por lo tanto, los estudiantes no quieren que las mujeres los representen, y hay que prohibir que los hombres postulen». "
        "Detecta al menos dos fallas de rigor, reescribe el argumento con una conclusión proporcionada y propone qué evidencia buscarías.",
        "Fallas: generalización apresurada desde un curso; atribuye intención sin evidencia; la propuesta no se desprende del diagnóstico. Reescritura: en el curso B, 2 de 12 delegadas fueron mujeres; falta saber cuántas postularon y cómo se votó. Evidencia: postulaciones por género, resultados de votación y razones de las y los votantes.",
        ["detecta al menos dos fallas de rigor", "la reescritura es proporcionada a la evidencia", "propone evidencia pertinente", "separa diagnóstico de propuesta"],
        ["análisis de fallas, reescritura y evidencia propuesta"],
        ["aceptar la generalización", "reescribir sin cambiar la conclusión", "proponer evidencia irrelevante"],
        "Pregunta: «¿qué dato te falta para afirmar la causa?». Pídele que lo nombre."),
    reinforce="Toma una afirmación que hayas oído sobre diferencias entre grupos y escribe qué evidencia pedirías antes de aceptarla.",
    extend="Elabora una pregunta de investigación y un diseño simple de recolección de datos para el caso del curso B.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 5 (objeciones y propuestas de ejemplo). Situación: en el club Horizonte, menos mujeres que hombres ocupan cargos de coordinación, y varias integrantes dudan en postular. "
     "Objeción 1: «Es exagerado: hoy todas las personas tienen los mismos derechos.» Objeción 2: «Las diferencias vienen de lo que cada persona prefiere.» Objeción 3: «Ya hay reglas; no hace falta hacer más.» "
     "Propuesta A: rotar los cargos y abrir convocatorias claras. Propuesta B: pegar afiches con frases de ánimo. Propuesta C: cambiar los horarios de reunión para que puedan asistir quienes cuidan a otras personas.")
build(
    O5, 5, F,
    use="Aprenderé a responder objeciones sobre desigualdad de género con razones, a evaluar propuestas con criterios y a expresar mi análisis en distintos formatos.",
    prior=["Sé evaluar un argumento con rigor.", "Conozco cuatro perspectivas filosóficas sobre el tema.", "Sé responder una objeción."],
    explain=[
        "Proponer soluciones a un problema social exige criterios. Cuatro ayudan: pertinencia (¿ataca la causa que identificamos?), viabilidad (¿se puede hacer con los recursos disponibles?), justicia (¿trata bien a todas las personas afectadas y evita nuevas desventajas?) y evaluabilidad (¿podemos saber si funcionó?). Una propuesta puede ser bien intencionada y poco pertinente.",
        "Las objeciones son parte del proceso. Para responderlas se concede lo cierto, se distingue entre conceptos (igualdad formal frente a igualdad de oportunidades), se pide evidencia o se ajusta la propuesta. La objeción «hoy todos tienen los mismos derechos» se responde distinguiendo derechos de condiciones reales; «es lo que cada quien prefiere» se responde preguntando por qué algunas opciones parecen disponibles y otras no; «ya hay reglas» se responde preguntando si las reglas cumplen lo que buscan.",
        "El análisis puede expresarse en formatos distintos: un ensayo breve, un mapa de argumentos, un afiche con una tesis y sus razones, un diálogo escrito, una exposición oral o un relato ficticio basado en el caso. Cada formato exige claridad en la tesis y rigor en las razones. Lo importante es que quien lo lea o escuche pueda reconstruir el argumento.",
    ],
    vocab=[("pertinencia", "que una propuesta ataque la causa identificada"), ("viabilidad", "posibilidad de realizar la propuesta con los recursos disponibles"), ("evaluabilidad", "posibilidad de saber si la propuesta funcionó"), ("propuesta", "acción que se sugiere para mejorar un problema"), ("formato de expresión", "forma de presentar un análisis, como ensayo, afiche, mapa o diálogo"), ("tesis", "idea central que se defiende")],
    worked=[
        ("Evaluar una propuesta", "Evalúa la Propuesta B (afiches de ánimo) con el criterio de pertinencia.",
         ["Pregunto qué causa identificamos: dudas para postular por la baja presencia de mujeres en cargos y posibles barreras prácticas.", "Los afiches animan, pero no cambian horarios ni convocatorias."],
         "Es poco pertinente: no ataca las causas identificadas"),
        ("Responder una objeción", "Responde la Objeción 1 con una distinción.",
         ["Concedo que hay mismos derechos.", "Distingo: tener derechos no garantiza oportunidades reales si hay barreras prácticas."],
         "Igualdad de derechos no es lo mismo que igualdad de oportunidades reales"),
    ],
    mistakes=[("Elegir una propuesta porque suena bien, sin comprobar si ataca la causa.", "Se confunde buena intención con pertinencia.", "Compara la propuesta con la causa que identificaste."),
              ("Responder a una objeción diciendo que quien la hace no entiende.", "Se ataca a la persona y no la razón.", "Reconoce lo cierto y responde con una distinción o evidencia.")],
    T=[
        ("abc", "{F} ¿Qué criterio evalúa si una propuesta ataca la causa identificada?", "Pertinencia", "Viabilidad", "Evaluabilidad", "La pertinencia se refiere a la relación con la causa."),
        ("abc", "{F} ¿Qué criterio evalúa si podemos saber si una propuesta funcionó?", "Evaluabilidad", "Pertinencia", "Justicia", "Pregunta por la posibilidad de comprobar resultados."),
        ("abc", "{F} ¿Qué propuesta es la más pertinente si la causa identificada son los horarios de reunión?", "La Propuesta C", "La Propuesta B", "La Propuesta A", "Cambia el horario que crea la barrera."),
        ("abc", "{F} ¿Qué propuesta pretende reducir la sensación de que los cargos son para unas pocas personas?", "La Propuesta A, rotar cargos y abrir convocatorias claras", "La Propuesta B", "La Propuesta C", "Rotar y abrir convocatorias cambia el acceso a los cargos."),
        ("abc", "{F} ¿Qué supone la Objeción 2?", "Que las diferencias se explican por preferencias libres", "Que no hay derechos", "Que la ley es injusta", "Atribuye las diferencias a lo que cada persona prefiere."),
        ("abc", "{F} ¿Cuál es una buena respuesta a la Objeción 2?", "Preguntar por qué algunas opciones parecen disponibles y otras no", "Decir que quien objeta no entiende", "Aceptarla sin examen", "Examina si la preferencia es libre o influida por condiciones."),
        ("abc", "{F} ¿Cuál es una buena respuesta a la Objeción 3 («ya hay reglas»)?", "Examinar si las reglas cumplen lo que buscan en la práctica", "Eliminar las reglas", "Repetir la regla", "Pide comprobar los efectos de las reglas."),
        ("abc", "{F} Una estudiante responde a la Objeción 1: «Los que piensan así son retrógrados». ¿Qué falla tiene?", "Ataca a las personas y no la razón", "Hace una distinción", "Concede lo cierto", "No examina la razón de la objeción."),
        ("abc", "{F} ¿Qué criterio evalúa la Propuesta A si se pregunta si ayuda a todas las personas y evita nuevas desventajas?", "Justicia", "Viabilidad", "Pertinencia", "Mira el trato a todas las personas afectadas."),
        ("abc", "{F} Un comité dice: «Aprobamos la Propuesta C: es pertinente, pero nadie puede asistir en ese nuevo horario». ¿Qué criterio falla?", "Viabilidad", "Evaluabilidad", "Pertinencia", "Es pertinente, pero no se puede realizar."),
        ("abc", "¿Qué formato de expresión es más adecuado para mostrar de forma ordenada tesis, razones y objeciones?", "Un mapa de argumentos", "Una lista de datos sin conexión entre ellos", "Un dibujo sin título ni explicación", "Permite a quien lo lee reconstruir tesis, razones y objeciones."),
        ("abc", "Una estudiante presenta su análisis como relato ficticio. ¿Qué debe cuidar para que siga siendo un análisis?", "Que se pueda reconstruir la tesis y sus razones", "Que use palabras difíciles", "Que tenga muchos personajes", "El formato no debe ocultar el argumento."),
        ("abc", "{F} Se propone evaluar la Propuesta C a los dos meses, contando cuántas personas nuevas postulan. ¿Qué criterio cumple?", "Evaluabilidad", "Justicia", "Pertinencia", "Define cómo se podrá saber si la propuesta funcionó."),
    ],
    ctx=("abc", "Un centro de estudiantes ficticio propone contratar a diez monitores profesionales para un taller, pero no tiene fondos para pagarlos. ¿Qué criterio falla más claramente?", "Viabilidad", "Pertinencia", "Evaluabilidad", "La propuesta no se puede realizar con los recursos disponibles."),
    sc=[
        ("En Filosofía política: ¿qué es la pertinencia de una propuesta?", "Que ataque la causa que se identificó", "Es el primer criterio de la clase."),
        ("Nombra los cuatro criterios para evaluar una propuesta.", "Pertinencia, viabilidad, justicia y evaluabilidad", "Son los cuatro criterios que enseña la explicación de la clase."),
        ("¿Qué distinción responde a «hoy todos tienen los mismos derechos»?", "Igualdad de derechos frente a igualdad de oportunidades reales", "Los derechos no siempre garantizan condiciones reales."),
    ],
    op=("Elige una situación ficticia: (1) un equipo deportivo con pocas arqueras mujeres; (2) un grupo de teatro en que casi todo el trabajo de organizar la sala lo hacen las mismas personas. "
        "Produce un texto breve, un mapa de argumentos o un afiche con: la tesis sobre la causa más probable, una propuesta evaluada con dos criterios, y una objeción con su respuesta.",
        "Situación 2. Tesis: el trabajo de organizar recae en las mismas personas por costumbres no discutidas. Propuesta: turnos rotativos publicados. Pertinencia: ataca la costumbre. Viabilidad: se puede hacer con una planilla. Objeción: nadie quiere organizar; respuesta: se acuerdan turnos y se reconoce el trabajo.",
        ["formula una tesis con una causa probable", "evalúa la propuesta con dos criterios", "incluye una objeción y su respuesta", "el formato permite reconstruir el argumento"],
        ["producto breve con tesis, propuesta, criterios y objeción"],
        ["proponer sin vincular con la causa", "no evaluar con criterios", "ignorar la objeción"],
        "Pregunta: «¿cómo se relaciona tu propuesta con la causa que identificaste?». Pídele que lo explique."),
    reinforce="Elige un problema de tu entorno relacionado con el tema y escribe una propuesta evaluada con pertinencia y viabilidad.",
    extend="Presenta oralmente en dos minutos tu tesis, propuesta y respuesta a una objeción, y pide a otra persona que reconstruya el argumento.",
)

# ============================================================ OAC-06, clase 1
F = ("Ficha 6 (textos de ejemplo). "
     "Texto 1: «El reglamento del liceo Aurora es horrible.» "
     "Texto 2: «Debemos revisar el reglamento, porque nadie del curso participó en su redacción y todos debemos cumplirlo.» "
     "Texto 3: «Si un reglamento no es conocido por quienes lo cumplen, no obliga con justicia. El reglamento del liceo Aurora no fue conocido por el estudiantado. Por lo tanto, no obliga con justicia.»")
build(
    O6, 1, F,
    use="Aprenderé a distinguir un argumento de una opinión, a identificar premisas y conclusión y a separar verdad, validez y solidez.",
    prior=["Sé qué es una premisa y una conclusión.", "Sé reconstruir una postura.", "Sé qué es una falacia por su nombre."],
    explain=[
        "Un argumento ofrece razones (premisas) para apoyar una conclusión. Una opinión sin razones, como «el reglamento es horrible», no es un argumento. Palabras como «porque», «ya que», «por lo tanto» y «luego» suelen indicar relaciones entre premisas y conclusión, aunque no siempre aparecen. Reconstruir un argumento es ordenarlo: premisas, conclusión y, si hace falta, la premisa que quedó implícita.",
        "Tres ideas deben distinguirse. Una afirmación es verdadera o falsa según los hechos. Un argumento es válido cuando la conclusión se sigue necesariamente de las premisas: si las premisas fueran verdaderas, la conclusión no podría ser falsa. Un argumento es sólido cuando es válido y además sus premisas son verdaderas. Un argumento válido puede tener premisas falsas, y un argumento con premisas verdaderas puede ser inválido.",
        "Un ejemplo no político: «Todas las aves vuelan; el pingüino es un ave; luego el pingüino vuela». Es válido, pero su primera premisa es falsa, así que no es sólido. En política interesa saber si un razonamiento es válido y si sus premisas son aceptables, para poder comparar posturas con rigor.",
    ],
    vocab=[("argumento", "premisas que apoyan una conclusión"), ("opinión sin razones", "afirmación que no ofrece apoyo"), ("validez", "la conclusión se sigue necesariamente de las premisas"), ("solidez", "argumento válido con premisas verdaderas"), ("premisa implícita", "premisa que no se dice pero se necesita"), ("reconstruir", "ordenar un argumento en premisas y conclusión")],
    worked=[
        ("Distinguir argumento y opinión", "¿Cuáles de los textos de la ficha son argumentos?",
         ["El Texto 1 solo valora, sin razones.", "Los Textos 2 y 3 dan razones para una conclusión."],
         "Los Textos 2 y 3 son argumentos; el Texto 1 es una opinión sin razones"),
        ("Reconstruir el Texto 3", "Reconstruye el Texto 3 en premisas y conclusión.",
         ["Premisa 1: si un reglamento no es conocido por quienes lo cumplen, no obliga con justicia.", "Premisa 2: el reglamento del liceo Aurora no fue conocido por el estudiantado. Conclusión: no obliga con justicia."],
         "P1 y P2 apoyan la conclusión de que el reglamento no obliga con justicia"),
    ],
    mistakes=[("Creer que un argumento válido siempre tiene una conclusión verdadera.", "Se confunde validez con verdad.", "Pregunta si las premisas son verdaderas: eso es la solidez."),
              ("Tomar cualquier frase con «porque» como un buen argumento.", "La palabra indica forma, no calidad.", "Evalúa si la razón apoya la conclusión.")],
    T=[
        ("abc", "{F} ¿Qué palabra del Texto 2 introduce la razón que apoya su conclusión?", "porque", "Debemos", "revisar", "«Porque» señala lo que se ofrece como razón."),
        ("abc", "{F} ¿Cuál es la conclusión del Texto 2?", "Debemos revisar el reglamento", "Nadie del curso participó", "Todos debemos cumplirlo", "Es lo que se defiende; lo demás son razones."),
        ("abc", "{F} ¿Cuál es una premisa del Texto 2?", "Nadie del curso participó en su redacción", "Debemos revisar el reglamento", "El reglamento es horrible", "Es una de las razones que apoyan la conclusión."),
        ("abc", "{F} ¿Qué palabra indica la conclusión del Texto 3?", "Por lo tanto", "Si", "No", "Esa expresión introduce lo que se concluye de las premisas."),
        ("abc", "Según la explicación, ¿cuándo es válido un argumento?", "Cuando la conclusión se sigue necesariamente de las premisas", "Cuando la conclusión es verdadera", "Cuando todas las personas lo aceptan", "La validez trata de la relación entre premisas y conclusión."),
        ("abc", "Según la explicación, ¿cuándo es sólido un argumento?", "Cuando es válido y sus premisas son verdaderas", "Cuando tiene al menos tres premisas", "Cuando su conclusión es verdadera", "Es un argumento válido con premisas verdaderas."),
        ("abc", "Todas las aves vuelan; el pingüino es un ave; luego el pingüino vuela. ¿Cómo es este argumento?", "Válido, pero no sólido, porque la primera premisa es falsa", "Inválido, porque el pingüino no vuela", "Sólido, porque es válido", "La conclusión se sigue, pero una premisa es falsa."),
        ("abc", "{F} El Texto 3 dice: «Si un reglamento no es conocido por quienes lo cumplen, no obliga con justicia». ¿Qué premisa necesita aceptar quien lo lea para que el argumento sea sólido?", "Que esa regla general es aceptable y que el reglamento no fue conocido", "Que el reglamento es injusto en todos sus artículos", "Que la conclusión es una opinión compartida", "Debe aceptar la regla general y también el hecho sobre el reglamento."),
        ("abc", "Un estudiante dice: «Si el argumento es válido, entonces la conclusión es verdadera». ¿Qué le falta?", "Que además las premisas sean verdaderas", "Nada, es correcto", "Que la conclusión sea compartida por todos", "Un argumento válido con premisas falsas puede tener conclusión falsa."),
        ("abc", "Un argumento tiene premisas verdaderas, pero la conclusión no se sigue de ellas. ¿Qué es?", "Inválido", "Sólido", "Válido", "Sin relación necesaria, es inválido aunque las premisas sean verdaderas."),
        ("abc", "{F} Se reescribe el Texto 2 así: «Debemos revisar el reglamento porque es horrible». ¿Qué problema tiene?", "La razón es una valoración que no apoya claramente la conclusión", "Es un argumento sólido", "Es una pregunta", "«Horrible» no explica por qué debe revisarse."),
        ("abc", "{F} El Texto 2 no dice una premisa necesaria: «Quienes cumplen un reglamento deberían poder participar en su redacción». ¿Qué es esa premisa?", "Una premisa implícita", "Una opinión sin razones", "Una conclusión", "No aparece, pero hace falta para llegar a la conclusión."),
        ("abc", "{F} ¿Cuál es el uso correcto del término «válido» para el Texto 3?", "Es válido: si las premisas son verdaderas, la conclusión también lo es", "Es válido porque el liceo realmente no entregó el reglamento", "Es válido porque su conclusión es una opinión compartida", "La conclusión se sigue necesariamente de las premisas del texto."),
    ],
    ctx=("abc", "En una asamblea ficticia, una vecina dice: «Debemos votar el presupuesto en abierto, porque cuando se decide a puertas cerradas la gente deja de confiar». ¿Cuáles son la conclusión y la premisa?", "Conclusión: votar el presupuesto en abierto; premisa: a puertas cerradas la gente deja de confiar", "Conclusión: la gente deja de confiar; premisa: votar en abierto", "No hay argumento", "La frase con «porque» da la razón y la otra es lo que se defiende."),
    sc=[
        ("En Filosofía política: ¿qué es un argumento?", "Un conjunto de premisas que apoyan una conclusión", "Se distingue de una opinión sin razones."),
        ("¿Qué diferencia hay entre validez y solidez?", "La validez trata de la relación entre premisas y conclusión; la solidez agrega que las premisas sean verdaderas", "Un argumento sólido siempre es válido y además tiene premisas verdaderas."),
        ("¿Puede un argumento válido tener una conclusión falsa?", "Sí, si alguna premisa es falsa", "La validez no garantiza premisas verdaderas."),
    ],
    op=("Elige un texto de ejemplo: (1) «Los consejos de curso deben tener un acta pública, porque quien no sabe qué se decidió no puede controlar a su representante»; (2) «Los horarios de uso de la cancha deben rotar, porque si no, siempre usan la cancha los mismos grupos». "
        "Reconstrúyelo en premisas y conclusión, indica si es válido y escribe una premisa implícita.",
        "Texto 1. Premisa: quien no sabe qué se decidió no puede controlar a su representante. Premisa implícita: la ciudadanía debe poder controlar a su representante. Conclusión: los consejos deben tener un acta pública. Es válido con la premisa implícita.",
        ["reconstruye premisas y conclusión", "indica si es válido y por qué", "formula una premisa implícita razonable", "no confunde validez con verdad"],
        ["reconstrucción con premisas, conclusión y premisa implícita"],
        ["no distinguir premisa y conclusión", "confundir validez con verdad", "no formular premisa implícita"],
        "Pregunta: «¿qué necesitas aceptar para que tu conclusión se siga?». Pídele que lo escriba."),
    reinforce="Elige una frase política que hayas oído y reescríbela como argumento con premisas y conclusión.",
    extend="Construye un argumento válido con una premisa falsa y explica por qué no es sólido.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 7 (formas de argumento de ejemplo). "
     "Forma 1: Si P, entonces Q. P. Por lo tanto, Q. "
     "Forma 2: Si P, entonces Q. No Q. Por lo tanto, no P. "
     "Forma 3: Si P, entonces Q. Q. Por lo tanto, P. "
     "Forma 4: Si P, entonces Q. No P. Por lo tanto, no Q.")
build(
    O6, 2, F,
    use="Aprenderé a reconocer cuatro formas de razonamiento con «si… entonces», dos válidas y dos falaces, y a comprobar la validez con un contraejemplo.",
    prior=["Sé qué es un argumento válido.", "Sé qué es una premisa.", "Sé qué es un contraejemplo."],
    explain=[
        "Muchos razonamientos políticos tienen la forma «si… entonces». Se llama antecedente a lo que sigue al «si» y consecuente a lo que sigue al «entonces». La Forma 1, afirmar el antecedente (modus ponens), es válida: si la condición se cumple, se cumple la consecuencia. La Forma 2, negar el consecuente (modus tollens), también es válida: si la consecuencia no ocurre, la condición no se dio.",
        "Las formas 3 y 4 son inválidas y se llaman falacias formales. La Forma 3 afirma el consecuente: de «si hay un acuerdo, entonces se firma» y «se firmó» no se sigue que hubo acuerdo, pues pudo firmarse por otra causa. La Forma 4 niega el antecedente: de «si hay un acuerdo, entonces se firma» y «no hubo acuerdo» no se sigue que no se firmó. Para comprobar la invalidez se busca un contraejemplo: un caso con premisas verdaderas y conclusión falsa.",
        "Una falacia formal es un error de forma: aunque el contenido cambie, la estructura no garantiza la conclusión. Distinguir la forma de un razonamiento ayuda a evaluar discursos políticos sin depender de si la conclusión nos gusta o no.",
    ],
    vocab=[("antecedente", "lo que sigue al «si» en una condicional"), ("consecuente", "lo que sigue al «entonces» en una condicional"), ("afirmar el antecedente", "forma válida: si P entonces Q; P; luego Q"), ("negar el consecuente", "forma válida: si P entonces Q; no Q; luego no P"), ("afirmar el consecuente", "falacia formal: si P entonces Q; Q; luego P"), ("negar el antecedente", "falacia formal: si P entonces Q; no P; luego no Q")],
    worked=[
        ("Reconocer una forma válida", "«Si una ley se aprueba, entonces se publica. La ley X se aprobó. Por lo tanto, la ley X se publica». ¿Qué forma tiene y es válida?",
         ["El argumento afirma el antecedente (se aprobó).", "Es la Forma 1, que es válida."],
         "Forma 1 (afirmar el antecedente), válida"),
        ("Hallar un contraejemplo", "«Si un acuerdo se firma, entonces es público. Este acuerdo es público. Por lo tanto, se firmó». Muestra que es inválido con un contraejemplo.",
         ["Es la Forma 3, que afirma el consecuente.", "Un acuerdo puede ser público porque se publicó un borrador, sin haberse firmado."],
         "Es inválido: un acuerdo puede hacerse público sin haberse firmado"),
    ],
    mistakes=[("Creer que afirmar el consecuente prueba el antecedente.", "Se confunde «si P entonces Q» con «si Q entonces P».", "Busca otra causa posible de Q."),
              ("Creer que negar el antecedente prueba que no ocurre el consecuente.", "El consecuente puede ocurrir por otras causas.", "Busca un caso en que no se cumpla P y sí Q.")],
    T=[
        ("abc", "{F} ¿Cuál de las formas se llama afirmar el antecedente?", "Forma 1", "Forma 2", "Forma 3", "La Forma 1 afirma P, que es el antecedente."),
        ("abc", "{F} ¿Cuál de las formas se llama negar el consecuente?", "Forma 2", "Forma 1", "Forma 4", "La Forma 2 niega Q, que es el consecuente."),
        ("abc", "{F} ¿Cuáles de las formas son válidas?", "Formas 1 y 2", "Formas 3 y 4", "Formas 1 y 3", "Son las dos formas válidas de la explicación."),
        ("abc", "«Si la propuesta se aprueba, entonces se aplica. La propuesta se aprobó. Por lo tanto, se aplica.» ¿Qué forma tiene?", "Forma 1", "Forma 3", "Forma 4", "Afirma el antecedente de la condicional y por eso es válido."),
        ("abc", "«Si hay quórum, entonces se vota. No se votó. Por lo tanto, no hubo quórum.» ¿Qué forma tiene y es válida?", "Forma 2, válida", "Forma 3, inválida", "Forma 4, inválida", "Niega el consecuente y es válida."),
        ("abc", "«Si hay consenso, entonces la propuesta pasa. La propuesta pasó. Por lo tanto, hubo consenso.» ¿Qué forma tiene y es válida?", "Forma 3, inválida", "Forma 1, válida", "Forma 2, válida", "Afirma el consecuente; la propuesta pudo pasar por mayoría sin consenso."),
        ("abc", "«Si una norma es injusta, entonces debe revisarse. Esta norma no es injusta. Por lo tanto, no debe revisarse.» ¿Qué forma tiene y es válida?", "Forma 4, inválida", "Forma 2, válida", "Forma 1, válida", "Niega el antecedente; la norma podría revisarse por otras razones."),
        ("abc", "«Si un gobierno es legítimo, entonces rinde cuentas. El gobierno X no rinde cuentas. Por lo tanto, X no es legítimo.» ¿Qué forma tiene?", "Forma 2, y es válida", "Forma 3, y es inválida", "Forma 4, y es inválida", "La estructura niega el consecuente, aunque la primera premisa pueda discutirse."),
        ("abc", "{F} Para el argumento «Si P entonces Q; Q; luego P», ¿qué contraejemplo funciona con P: «llueve» y Q: «el patio está mojado»?", "El patio puede estar mojado porque alguien lo lavó, aunque no llueva", "Si llueve, el patio siempre se moja", "Llueve y el patio está mojado", "Muestra premisas verdaderas con conclusión falsa."),
        ("abc", "Alguien dice: «El argumento es válido porque la conclusión me parece correcta». ¿Qué error comete?", "Confunde validez con que la conclusión sea agradable o verdadera", "Evalúa la forma", "Busca un contraejemplo", "La validez depende de la forma."),
        ("abc", "«Si una consulta es vinculante, entonces el municipio debe cumplirla. Esta consulta no es vinculante. Por lo tanto, el municipio no debe cumplirla.» ¿Qué falla tiene?", "Niega el antecedente: el municipio podría deber cumplirla por otra razón", "Afirma el antecedente", "Niega el consecuente", "Que la condición no se cumpla no prueba que la consecuencia no pueda darse."),
        ("abc", "{F} Un estudiante dice: «Una forma válida con una premisa falsa produce siempre una conclusión falsa». ¿Es correcto?", "No: la conclusión puede ser verdadera o falsa aunque una premisa sea falsa", "Sí, siempre", "Solo en la Forma 2", "La validez no determina la verdad de la conclusión."),
        ("abc", "¿Qué hace un contraejemplo a un argumento inválido?", "Muestra que las premisas pueden ser verdaderas y la conclusión falsa", "Prueba que la conclusión es verdadera", "Confirma la forma", "Esa es su función: mostrar que la forma no garantiza la conclusión."),
    ],
    ctx=("abc", "Una dirigente ficticia dice: «Si la comunidad participa, entonces la obra se termina antes. La obra se terminó antes. Por lo tanto, la comunidad participó». ¿Qué falla tiene?", "Afirma el consecuente: la obra pudo terminarse antes por otras razones", "Es válido", "Niega el antecedente", "El adelanto de la obra podría deberse a otras razones."),
    sc=[
        ("En Filosofía política: ¿qué es una falacia formal?", "Un error en la forma del razonamiento, que no garantiza la conclusión", "No depende del contenido, sino de la estructura del razonamiento."),
        ("¿Qué forma válida niega el consecuente?", "Si P entonces Q; no Q; luego no P", "Es la forma que la explicación llama negar el consecuente."),
        ("¿Cómo se comprueba que una forma es inválida?", "Con un contraejemplo de premisas verdaderas y conclusión falsa", "Es el método de la clase."),
    ],
    op=("Elige una condicional de ejemplo: (1) «Si un reglamento fue discutido por el estudiantado, entonces se considera legítimo»; (2) «Si una autoridad rinde cuentas, entonces es confiable». "
        "Escribe un argumento con la Forma 1, uno con la Forma 2, uno con la Forma 3 y uno con la Forma 4, y señala cuáles son válidos. Para una forma inválida, escribe un contraejemplo.",
        "Condicional 2. Forma 1: la autoridad rinde cuentas; luego es confiable. Forma 2: no es confiable; luego no rinde cuentas. Forma 3: es confiable; luego rinde cuentas (inválido: pudo ser confiable por otra razón). Forma 4: no rinde cuentas; luego no es confiable (inválido). Contraejemplo: una autoridad puede ser confiable por su historial sin rendir cuentas formales.",
        ["escribe correctamente las cuatro formas", "señala cuáles son válidas", "da un contraejemplo adecuado", "no confunde validez con verdad de las premisas"],
        ["cuatro argumentos, clasificación y contraejemplo"],
        ["invertir antecedente y consecuente", "no dar contraejemplo", "decidir por la verdad de la conclusión"],
        "Pregunta: «¿qué otra causa podría producir el consecuente?». Pídele que la nombre."),
    reinforce="Escribe una condicional sobre la convivencia en tu curso y construye las cuatro formas con ella.",
    extend="Explica por qué confundir «si P entonces Q» con «si Q entonces P» es un error frecuente en discursos políticos.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 8 (fragmentos de ejemplo, ficticios). "
     "F1: «No hay que escuchar su propuesta de reciclaje: esa compañera nunca ha ordenado su propia pieza.» "
     "F2: «O se aprueba mi plan de seguridad completo, o nos quedamos sin seguridad.» "
     "F3: «Si permitimos que los cursos elijan sus colores de delegación, mañana elegirán sus propias normas, y terminaremos sin reglamento.» "
     "F4: «Todo el mundo dice que esa medida es buena, así que debe serlo.» "
     "F5: «Pidieron más tiempo para estudiar la propuesta; es decir, quieren que nunca se tome ninguna decisión.» "
     "F6: «La ingeniera civil del municipio explica que un muro de contención de esa altura requiere cálculos de resistencia antes de construirse.»")
build(
    O6, 3, F,
    use="Aprenderé a reconstruir un argumento antes de nombrar una falacia informal y a reconocer ocho falacias frecuentes en discursos sobre poder y política.",
    prior=["Sé distinguir validez y solidez.", "Sé reconstruir premisas y conclusión.", "Conozco formas válidas e inválidas con «si… entonces»."],
    explain=[
        "Una falacia informal es un error de razonamiento que depende del contenido o del contexto. Primero se reconstruye el argumento; recién entonces se decide si hay falacia. El ad hominem rechaza una tesis por rasgos de quien la dice, no por sus razones. El hombre de paja deforma la tesis de otra persona para refutarla más fácil. La falsa dicotomía presenta solo dos opciones cuando hay más. La pendiente resbaladiza afirma, sin pruebas, que un paso llevará inevitablemente a una cadena de males.",
        "La apelación a la mayoría sostiene que algo es verdadero o bueno porque muchos lo creen. La apelación a una autoridad no pertinente invoca a alguien con prestigio en un área ajena al tema; en cambio, citar a una persona experta en el asunto aporta una razón que se puede evaluar. La generalización apresurada concluye sobre todos a partir de pocos casos. La petición de principio da por cierto en las premisas lo que se quiere probar.",
        "Nombrar una falacia sin reconstruir el argumento es un error en sí mismo: puede que el fragmento no sea una falacia, o que lo sea de otro tipo. Conviene preguntar qué se afirma, qué razón se da y si esa razón apoya la conclusión. Luego se formula, si se puede, una versión mejorada del argumento.",
    ],
    vocab=[("falacia informal", "error de razonamiento que depende del contenido o contexto"), ("ad hominem", "rechazar una tesis por rasgos de quien la dice"), ("hombre de paja", "deformar la tesis ajena para refutarla más fácil"), ("falsa dicotomía", "presentar solo dos opciones cuando hay más"), ("pendiente resbaladiza", "afirmar sin pruebas que un paso llevará a una cadena de males"), ("petición de principio", "dar por cierto en las premisas lo que se quiere probar")],
    worked=[
        ("Reconstruir antes de nombrar", "Analiza el fragmento F1.",
         ["Reconstruyo: conclusión, no hay que escuchar su propuesta de reciclaje; razón, la compañera nunca ha ordenado su propia pieza.", "La razón habla de la persona y no del contenido de la propuesta."],
         "Ad hominem: rechaza la propuesta por rasgos de quien la presenta"),
        ("Distinguir una autoridad pertinente", "¿Por qué el fragmento F6 no es una apelación a una autoridad no pertinente?",
         ["Reconstruyo: la ingeniera civil explica un requisito técnico sobre un muro de contención.", "Su experiencia pertenece al tema y su razón se puede evaluar."],
         "Porque la autoridad pertenece al tema y aporta una razón evaluable"),
    ],
    mistakes=[("Nombrar una falacia sin reconstruir el argumento.", "Se etiqueta por el parecido de superficie y se puede equivocar.", "Reconstruye premisas y conclusión antes de nombrar."),
              ("Rechazar cualquier cita de una persona experta como falacia.", "Se confunde autoridad pertinente con autoridad no pertinente.", "Pregunta si la persona es experta en el tema y si ofrece razones.")],
    T=[
        ("abc", "Un estudiante dice: «Su plan de reciclaje es inútil, porque llega siempre atrasado a clases». ¿Qué falacia ilustra?", "Ad hominem", "Hombre de paja", "Falsa dicotomía", "Rechaza el plan por un rasgo de la persona y no por sus razones."),
        ("abc", "{F} ¿Qué falacia ilustra F2?", "Falsa dicotomía", "Pendiente resbaladiza", "Petición de principio", "Presenta solo dos opciones cuando existen otras posibles."),
        ("abc", "{F} ¿Qué falacia ilustra F3?", "Pendiente resbaladiza", "Falsa dicotomía", "Apelación a la mayoría", "Afirma, sin pruebas, una cadena de males."),
        ("abc", "{F} ¿Qué falacia ilustra F4?", "Apelación a la mayoría", "Ad hominem", "Hombre de paja", "Concluye que es bueno porque muchos lo dicen."),
        ("abc", "{F} ¿Qué falacia ilustra F5?", "Hombre de paja", "Ad hominem", "Pendiente resbaladiza", "Deforma la petición de más tiempo como si fuera querer que nunca se decida."),
        ("abc", "Una arquitecta del municipio explica que una rampa de acceso debe tener cierta inclinación máxima para ser segura. ¿Qué se puede decir?", "No es falacia: es una persona experta en el asunto y da una razón técnica", "Es ad hominem", "Es apelación a la mayoría", "La persona es experta en el asunto y ofrece una razón que se puede evaluar."),
        ("abc", "Una dirigente ficticia dice: «Mi plan es bueno porque es el mejor». ¿Qué falacia ilustra?", "Petición de principio", "Ad hominem", "Falsa dicotomía", "La conclusión se repite como premisa."),
        ("abc", "«Dos conductores de esa línea de micro llegaron tarde; los conductores de esa línea son impuntuales». ¿Qué falacia ilustra?", "Generalización apresurada", "Pendiente resbaladiza", "Hombre de paja", "Concluye sobre todos con pocos casos."),
        ("abc", "«Un actor famoso opina que esta reforma educativa es mala, así que lo es». ¿Qué falacia ilustra?", "Apelación a una autoridad no pertinente", "Ad hominem", "Falsa dicotomía", "El prestigio del actor no es experiencia en educación."),
        ("abc", "Alguien dice: «Es una falacia ad hominem», pero no explica qué argumento criticó. ¿Qué error comete?", "Nombrar una falacia sin reconstruir el argumento", "Reconstruir con caridad", "Formular una versión mejorada", "Falta mostrar el argumento y su relación con la razón."),
        ("abc", "{F} Una estudiante responde a F3: «Permitir colores no lleva automáticamente a cambiar normas». ¿Qué hace?", "Cuestiona la cadena de consecuencias sin pruebas de la pendiente resbaladiza", "Ataca a quien habla", "Cita una autoridad", "Pide evidencia de que cada paso lleve al siguiente."),
        ("abc", "{F} Reescribe F2 como un argumento mejorado. ¿Cuál es una versión más razonable?", "Mi plan tiene estas ventajas y otras alternativas serían estas; comparemos antes de decidir", "O mi plan, o nada", "Quien no me apoya no quiere seguridad", "Reconoce más opciones y propone comparar."),
        ("abc", "{F} Se dice: «F4 no es falacia, porque si muchos lo creen, es verdadero». ¿Qué problema tiene?", "El número de personas que lo cree no establece por sí solo que sea verdadero o bueno", "Es una respuesta correcta", "Confunde con ad hominem", "La popularidad no es una razón suficiente."),
    ],
    ctx=("abc", "En un foro ficticio sobre un presupuesto participativo, un asistente dice: «Quien propone eso trabaja para el municipio, así que no hay que escucharlo». ¿Qué falacia ilustra y cuál es la respuesta adecuada?", "Ad hominem; discutir las razones de la propuesta", "Hombre de paja; callar", "Falsa dicotomía; elegir una opción", "Rechaza una propuesta por la persona; hay que discutir sus razones."),
    sc=[
        ("En Filosofía política: ¿qué es un hombre de paja?", "Deformar la tesis ajena para refutarla más fácil", "Se ataca una versión débil en vez de la tesis real."),
        ("¿Qué se debe hacer antes de nombrar una falacia?", "Reconstruir el argumento", "Sin esa base se puede etiquetar mal."),
        ("¿Cuándo una cita a una persona experta no es falacia?", "Cuando es experta en el tema y ofrece razones que se pueden evaluar", "Es una autoridad pertinente porque domina el tema y da razones."),
    ],
    op=("Elige un fragmento de ejemplo: (1) «Si dejan que una vez se vote con voz alta, pronto se votará solo por amistad, y se acabará la democracia del curso»; (2) «Mi compañero propone revisar los turnos, es decir, quiere eliminar el esfuerzo de todos». "
        "Reconstruye el argumento, nombra la falacia, explica por qué lo es y escribe una versión mejorada del razonamiento.",
        "Fragmento 2. Reconstrucción: premisa, mi compañero propone revisar los turnos; conclusión, quiere eliminar el esfuerzo de todos. Falacia: hombre de paja, porque deforma la propuesta. Versión mejorada: mi compañero propone revisar los turnos; veamos si el cambio reparte mejor el esfuerzo.",
        ["reconstruye el argumento", "nombra la falacia adecuada", "explica por qué lo es", "escribe una versión mejorada"],
        ["reconstrucción, nombre de la falacia, explicación y versión mejorada"],
        ["nombrar sin reconstruir", "nombrar una falacia equivocada", "no mejorar el razonamiento"],
        "Pregunta: «¿qué decía exactamente la propuesta original?». Pídele que la compare con la versión deformada."),
    reinforce="Busca en una conversación o noticia un razonamiento que pueda ser falaz y reconstruye su argumento antes de decidir si lo es.",
    extend="Explica una situación en la que una cita a una autoridad es pertinente y otra en la que no, sobre el mismo tema.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 9 (razonamientos de ejemplo). "
     "Razonamiento 1 (centrado en el acuerdo): «Si una decisión se impone sin el acuerdo de quienes deben obedecerla, entonces no es legítima. La decisión X se impuso sin el acuerdo de quienes deben obedecerla. Por lo tanto, X no es legítima.» "
     "Razonamiento 2 (centrado en el bienestar total): «Si una medida produce más bienestar total que sus alternativas, entonces es correcta. La medida X produce más bienestar total que sus alternativas. Por lo tanto, X es correcta.» "
     "Caso de ejemplo: un liceo ficticio decide cerrar una sala de estudio nocturna que usa poca gente, sin consultar, para abrir un taller que beneficia a muchas más personas.")
build(
    O6, 4, F,
    use="Aprenderé a comparar razonamientos de distintas corrientes, a evaluar sus premisas y a posicionarme de modo consistente.",
    prior=["Sé las formas válidas e inválidas de argumento.", "Sé reconocer falacias informales.", "Conozco criterios de legitimidad y de bienestar."],
    explain=[
        "Comparar razonamientos de distintas corrientes de pensamiento exige dos pasos. Primero se reconstruyen con caridad y se comprueba su forma: los dos razonamientos de la ficha son válidos, porque afirman el antecedente de una condicional. Luego se evalúan sus premisas: la primera premisa de cada uno expresa un criterio distinto (acuerdo de quienes obedecen o bienestar total) y ahí está el desacuerdo de fondo. Dos argumentos válidos pueden llegar a conclusiones opuestas sobre el mismo caso.",
        "Posicionarse de modo consistente significa que la propia postura no se contradice y que se aplica el mismo criterio a casos semejantes. Si en un caso exijo consultar a quienes resultan afectados, no puedo negarlo en otro caso igual sin dar una razón relevante de la diferencia. Esa razón debe ser relevante para el criterio, no una simple conveniencia.",
        "Una posición consistente puede cambiar si aparecen razones mejores, pero ese cambio se explica y se aplica a todos los casos del mismo tipo. También puede combinar criterios, por ejemplo, exigir acuerdo y considerar el bienestar, siempre que indique cuál pesa más cuando entran en conflicto y por qué.",
    ],
    vocab=[("consistencia", "no contradecirse y aplicar el mismo criterio a casos semejantes"), ("criterio", "regla general que se usa para juzgar"), ("doble estándar", "aplicar un criterio a unos casos y otro a casos semejantes sin razón"), ("diferencia relevante", "rasgo que justifica tratar dos casos de modo distinto"), ("ponderar", "decidir qué criterio pesa más cuando entran en conflicto"), ("posicionarse", "tomar una posición argumentada")],
    worked=[
        ("Comparar dos razonamientos", "En el caso de ejemplo, ¿qué concluye cada razonamiento?",
         ["R1 pregunta si hubo acuerdo o consulta: no hubo, así que concluye que la decisión no es legítima.", "R2 pregunta por el bienestar total: el taller beneficia a más personas, así que concluye que la medida es correcta."],
         "R1: la decisión no es legítima; R2: la medida es correcta"),
        ("Detectar un doble estándar", "Alguien dice: «Si el centro de estudiantes decide sin consultar, está mal; si lo hace mi curso, está bien». ¿Qué falla tiene?",
         ["Aplica un criterio (consultar) a un caso y no a otro semejante.", "No ofrece una diferencia relevante."],
         "Es un doble estándar sin diferencia relevante"),
    ],
    mistakes=[("Elegir una postura según si la conclusión conviene en un caso, y cambiarla en otro.", "Se pierde la consistencia.", "Declara el criterio y aplícalo a todos los casos semejantes."),
              ("Decir que, como los dos razonamientos son válidos, ambos son igual de aceptables.", "Se confunde validez con solidez.", "Evalúa si sus premisas son aceptables.")],
    T=[
        ("abc", "{F} ¿Qué forma tiene el Razonamiento 1?", "Afirmar el antecedente, válida", "Afirmar el consecuente, inválida", "Negar el antecedente, inválida", "Afirma el antecedente de la condicional."),
        ("abc", "{F} ¿Qué forma tiene el Razonamiento 2?", "Afirmar el antecedente, válida", "Negar el consecuente, válida", "Afirmar el consecuente, inválida", "Afirma el antecedente de la condicional."),
        ("abc", "{F} ¿Qué criterio usa la primera premisa del Razonamiento 1?", "El acuerdo de quienes obedecen", "El bienestar total", "El prestigio de la autoridad", "Dice que una decisión impuesta sin ese acuerdo no es legítima."),
        ("abc", "{F} ¿Qué criterio usa la primera premisa del Razonamiento 2?", "El bienestar total", "El acuerdo de quienes obedecen", "La tradición", "Compara el bienestar total de las alternativas."),
        ("abc", "{F} ¿Por qué dos argumentos válidos pueden llevar a conclusiones opuestas sobre un mismo caso?", "Porque parten de premisas y criterios distintos", "Porque uno de los dos tiene necesariamente un error de forma", "Porque uno de ellos es siempre falaz", "El desacuerdo de fondo está en las premisas."),
        ("abc", "{F} Para cuestionar la solidez de R2 en el caso de ejemplo, ¿qué premisa conviene examinar?", "Que el taller realmente produzca más bienestar total que las alternativas", "Que el razonamiento afirme el antecedente", "Que la sala sea nocturna", "Si esa premisa fuera falsa, R2 seguiría siendo válido pero no sólido."),
        ("abc", "{F} ¿Qué objeción apunta a la primera premisa de R1?", "Que en una emergencia una decisión sin acuerdo previo podría ser legítima", "Que el razonamiento no es válido", "Que X sí fue consultada", "Cuestiona la regla general, no el hecho sobre X ni la forma del razonamiento."),
        ("abc", "{F} Una estudiante dice: «Mi posición es que hay que consultar siempre que una decisión afecte a un grupo». Si luego apoya cerrar la sala sin consultar, ¿qué falla tiene?", "Es inconsistente, porque no aplica su criterio a un caso semejante", "Es consistente", "Es una falacia formal", "Contradice su propio criterio al aplicarlo solo a veces."),
        ("abc", "Un estudiante dice: «Consultar es importante cuando afecta a mi curso, pero no cuando afecta a otro curso en la misma situación». ¿Qué falla tiene?", "Aplica un doble estándar sin diferencia relevante", "Es consistente", "Es una pendiente resbaladiza", "Trata distinto casos semejantes sin razón."),
        ("abc", "Una estudiante explica: «Aceptaré no consultar solo en una emergencia, porque no hay tiempo, y lo haré con todos los casos de emergencia». ¿Qué cumple?", "Consistencia con una diferencia relevante", "Doble estándar", "Falsa dicotomía", "Ofrece una diferencia relevante (la urgencia) y la aplica a todos."),
        ("abc", "{F} Si alguien combina ambos razonamientos, ¿qué debe indicar para ser consistente?", "Qué criterio pesa más cuando entran en conflicto y por qué", "Que ambos son iguales", "Que no hay conflicto posible", "Debe ponderar los criterios e indicar cuál pesa más."),
        ("abc", "{F} Un participante dice: «R1 y R2 son válidos, así que ambos son igual de buenos». ¿Qué error comete?", "Confunde validez con solidez", "Reconstruye con caridad", "Pondera los criterios", "No evalúa si las premisas son aceptables."),
        ("abc", "Una estudiante cambia su posición tras escuchar una razón nueva, la explica y la aplica a todos los casos semejantes. ¿Es consistente?", "Sí, porque el cambio se explica y se aplica de forma pareja", "No, porque cambió", "No, porque dijo la razón", "La consistencia no impide revisar la posición con razones."),
    ],
    ctx=("abc", "Un municipio ficticio instala un nuevo semáforo sin consultar a los vecinos, y un vecino lo critica por falta de consulta. Luego el mismo vecino apoya instalar otro semáforo sin consultar en su calle, porque «es urgente para mi cuadra». ¿Qué falla tiene su posición?", "Un doble estándar, salvo que muestre una diferencia relevante que también aplicaría a otros casos", "Ninguna", "Una falacia formal de afirmar el consecuente", "Aplica un criterio distinto a casos semejantes."),
    sc=[
        ("En Filosofía política: ¿qué es la consistencia?", "No contradecirse y aplicar el mismo criterio a casos semejantes", "Es el rasgo central para posicionarse con coherencia."),
        ("¿Qué es un doble estándar?", "Aplicar un criterio a unos casos y otro a casos semejantes sin razón", "Rompe la consistencia porque trata distinto casos semejantes."),
        ("¿Por qué dos argumentos válidos pueden contradecirse?", "Porque sus premisas expresan criterios distintos", "La validez no garantiza premisas aceptables."),
    ],
    op=("Elige un caso ficticio: (1) un equipo debe decidir si publica las actas de reunión aunque eso incomode a algunas personas; (2) un liceo debe decidir si cambia el horario de los talleres sin consultar a los inscritos. "
        "Formula un razonamiento centrado en el acuerdo y otro centrado en el bienestar, indica sus formas, compara qué concluyen y escribe tu posición con un criterio que aplicarías a otro caso semejante.",
        "Caso 2. R1: si una decisión afecta a las inscritas y se toma sin consulta, no es legítima; fue sin consulta; luego no es legítima. R2: si el cambio produce más bienestar que las alternativas, es correcto; lo produce; luego es correcto. Posición: consultar siempre que sea posible, excepto en emergencias; lo aplicaría también al reparto de salas.",
        ["formula dos razonamientos válidos con criterios distintos", "indica su forma", "compara sus conclusiones", "su posición es consistente con un criterio aplicable a otro caso"],
        ["dos razonamientos, comparación y posición"],
        ["usar el mismo criterio en ambos razonamientos", "no aplicar la posición a otro caso", "olvidar la diferencia relevante"],
        "Pregunta: «¿qué otro caso resolverías con el mismo criterio?». Pídele que lo escriba."),
    reinforce="Identifica un criterio que usas para juzgar decisiones de tu curso y comprueba si lo aplicas igual a decisiones semejantes de otros grupos.",
    extend="Escribe una situación en la que dos criterios entren en conflicto y explica cuál ponderarías primero y por qué.",
)
