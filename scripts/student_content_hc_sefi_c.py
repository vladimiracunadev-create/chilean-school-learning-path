"""Seminario de filosofía (electivo HC, 3.º y 4.º medio): OAC-03 (analizar el devenir de un problema filosófico: continuidades, cambios, impactos y formas de expresión, clases 1 a 5). Etapas, autores y textos ficticios o «de ejemplo», sin fechas."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada panel, texto y caso está escrito en el enunciado. "
             "Las etapas, los autores y los textos son ficticios o «de ejemplo»: sirven para practicar el análisis de cómo cambia un problema filosófico y no tienen fechas ni son citas de ninguna obra real. "
             "La historia real del problema, con sus autores y sus fuentes, queda para tu docente. Las posturas se presentan con sus razones y sin tomar partido: tu tarea es entenderlas y compararlas. "
             "Si un caso te incomoda, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O3 = "FI-SEFI-3y4-OAC-03"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (paneles ficticios de la «Sala del Tiempo», un museo de ideas que no existe). Problema: ¿somos libres de elegir lo que hacemos? "
     "Panel de la etapa A: «Lo que le sucede a cada persona está fijado de antemano por fuerzas superiores.» "
     "Panel de la etapa B: «Cada persona puede deliberar y elegir; por eso responde por sus actos.» "
     "Panel de la etapa C: «Todo lo que ocurre tiene causas; si se conocen las causas de una decisión, ¿cuánto queda de libre?»")
build(
    O3, 1, F,
    use="Aprenderé a seguir cómo cambia un problema filosófico con el tiempo: qué permanece, qué cambia y qué efectos tiene en la sociedad.",
    prior=["Sé qué es un problema filosófico.", "Sé buscar antecedentes y contexto en un texto.", "Sé reconstruir tesis y razones."],
    explain=[
        "El devenir de un problema filosófico es la manera en que ese problema aparece, cambia y se transforma a lo largo del tiempo. Para analizarlo se separan tres cosas. La continuidad es lo que permanece: la pregunta de fondo, que reaparece en distintas épocas. El cambio es lo que se modifica: las respuestas, las razones que se ofrecen, los conceptos y el lenguaje. El impacto es lo que esas ideas provocan en la sociedad, por ejemplo en las leyes, la educación o las formas de convivir.",
        "En la ficha, el problema es la libertad de elegir. En las tres etapas de ejemplo la pregunta de fondo se mantiene: cuánto depende de nosotros lo que hacemos y de qué somos responsables. Cambian las razones: primero se apela a fuerzas superiores, luego a la deliberación y después a las causas. Las etapas son de ejemplo y no se ubican en fechas ni en autores reales.",
        "Problematizar el devenir es preguntar qué se mantiene, qué cambia y por qué. Una buena pregunta de devenir evita dos errores. Uno es creer que el problema es siempre el mismo y que solo cambian las palabras. El otro es creer que cada etapa discute algo totalmente distinto, sin relación con las anteriores.",
    ],
    vocab=[("devenir", "manera en que un problema aparece, cambia y se transforma en el tiempo"), ("continuidad", "lo que permanece de un problema a lo largo del tiempo"), ("cambio", "lo que se modifica de un problema: respuestas, razones o conceptos"), ("impacto", "efecto de las ideas en la sociedad, como leyes, educación o convivencia"), ("etapa", "período de ejemplo en que predomina una manera de plantear un problema"), ("deliberar", "pensar con calma las razones a favor y en contra antes de elegir")],
    worked=[
        ("Separar continuidad y cambio", "En la ficha, ¿qué permanece y qué cambia entre las etapas A y B?",
         ["Comparo las dos frases: ambas hablan de lo que le sucede a las personas y de su responsabilidad.", "Cambia la razón: en A, fuerzas superiores; en B, la deliberación de cada persona."],
         "Permanece la pregunta sobre lo que depende de nosotros; cambia la razón que se da"),
        ("Un impacto posible", "Si la etapa B influyera en cómo un colegio ficticio trata las faltas, ¿qué impacto tendría?",
         ["Si cada persona puede deliberar y elegir, se espera que responda por sus actos.", "Entonces el colegio pediría explicar y reparar lo hecho."],
         "Pediría a los estudiantes responder por sus actos, por ejemplo con explicaciones y reparación"),
    ],
    mistakes=[("Creer que el problema es siempre exactamente el mismo y que solo cambian las palabras.", "Se ignoran los cambios de razones, conceptos y supuestos.", "Compara qué razones y qué conceptos usa cada etapa para responder."),
              ("Describir cada etapa como si no tuviera relación con las anteriores.", "Se pierde la continuidad del problema.", "Busca la pregunta de fondo que se mantiene en todas las etapas.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es el devenir de un problema filosófico?", "La manera en que el problema aparece, cambia y se transforma en el tiempo", "Una lista de autores famosos", "La respuesta definitiva al problema", "Se refiere a la historia del problema, no a una lista ni a una solución final."),
        ("abc", "¿Qué es una continuidad en el devenir de un problema?", "Lo que permanece, como la pregunta de fondo", "Lo que cambia en cada etapa", "El efecto sobre las leyes", "La continuidad es lo que se mantiene a lo largo del tiempo."),
        ("abc", "{F} ¿Cuál es el problema de fondo que aparece en los tres paneles?", "Cuánto depende de nosotros lo que hacemos", "Cómo construir un museo", "Quién escribió los paneles", "Los tres paneles discuten la libertad de elegir y la responsabilidad."),
        ("abc", "{F} ¿Qué razón ofrece el panel de la etapa A?", "Lo que sucede está fijado de antemano por fuerzas superiores", "Las personas deliberan y eligen", "Todo tiene causas que se pueden estudiar", "Es la razón central que plantea ese panel."),
        ("abc", "{F} ¿Qué razón ofrece el panel de la etapa C?", "Todo lo que ocurre tiene causas, por lo que se duda de cuánto queda de libre", "Las personas son responsables porque eligen", "Las fuerzas superiores deciden", "Plantea la cuestión desde las causas de una decisión."),
        ("ab", "{F} Al pasar de la etapa B a la C, ¿qué cambia principalmente?", "La razón que se da: de la deliberación de cada persona a las causas de la decisión", "La pregunta de fondo, que desaparece", "Cambia el modo de justificar la respuesta, pero la pregunta de lo que depende de nosotros sigue."),
        ("abc", "{F} ¿Qué parte del devenir es el siguiente enunciado: «las etapas usan razones distintas para responder lo mismo»?", "El cambio", "La continuidad", "El impacto", "Se refiere a lo que se modifica entre una etapa y otra."),
        ("abc", "Un tribunal ficticio, al aceptar que las decisiones tienen causas en el entorno, empieza a considerar las condiciones de vida de una persona al decidir una sanción. ¿Qué parte del devenir ilustra?", "El impacto en la sociedad", "La continuidad", "Una definición", "Muestra el efecto de una idea en una institución."),
        ("abc", "Alguien dice: «El problema de la libertad es exactamente el mismo desde siempre; solo cambian las palabras». ¿Qué error comete?", "Ignora que cambian las razones, los conceptos y los supuestos", "Ignora que hay una pregunta de fondo", "Confunde problema con respuesta única", "El devenir implica cambios reales, no solo de vocabulario."),
        ("abc", "Otro dice: «La etapa A y la etapa C no tienen nada que ver entre sí». ¿Qué error comete?", "Pierde de vista la continuidad: ambas se preguntan cuánto depende de nosotros", "Confunde la etapa C con la B", "Dice que hay cambios", "El problema de fondo atraviesa las etapas."),
        ("abc", "{F} Si apareciera una etapa D que dijera «las decisiones se pueden estudiar en el cerebro», ¿qué sería lo más probable que ocurriera con el problema?", "Se mantendría la pregunta, con nuevas razones y conceptos", "Desaparecería el problema por completo", "Volvería idéntica a la etapa A", "Los problemas suelen conservar su pregunta de fondo, pero cambian las razones."),
        ("abc", "¿Por qué las etapas de la ficha no tienen fechas?", "Porque son de ejemplo para practicar el análisis y no un relato histórico real", "Porque no importa cuándo pasaron las cosas", "Porque son todas de la misma época", "Se aclara que son ejemplos y que la historia real queda para la lectura guiada."),
        ("abc", "Si un panel dijera «si las personas no eligen, castigar sería injusto», ¿qué parte del devenir muestra?", "Un posible impacto de la idea en la manera de juzgar a las personas", "Una definición de libertad", "El antecedente del problema", "Relaciona la idea con una práctica social: castigar."),
    ],
    ctx=("abc", "En una exposición escolar ficticia, un grupo presenta tres carteles que representan tres etapas de ejemplo sobre cómo se entiende la amistad: uno dice que la amistad se basa en la lealtad, otro en la utilidad y otro en la afinidad de gustos. ¿Qué pregunta sobre el devenir del problema conviene hacerse?", "¿Qué se mantiene y qué cambia entre estas respuestas?", "¿Cuál cartel tiene más colores?", "¿Cuántos estudiantes hicieron el trabajo?", "Pregunta por la continuidad y el cambio del problema, no por detalles externos."),
    sc=[
        ("En Seminario de filosofía: ¿qué es un cambio en el devenir de un problema?", "Lo que se modifica: respuestas, razones o conceptos", "Se compara qué razones se usan en cada etapa."),
        ("¿Qué es el impacto de una idea?", "El efecto que tiene en la sociedad, como leyes o educación", "Se observa en instituciones y prácticas."),
        ("¿Qué dos errores evita una buena pregunta de devenir?", "Creer que todo es siempre igual o que no hay relación entre etapas", "Se busca ver a la vez continuidad y cambio."),
    ],
    op=("Elige un problema de ejemplo: «¿qué debemos a quienes vienen después de nosotros?» o «¿qué es una vida buena?». Imagina tres etapas de ejemplo (A, B y C) con una frase cada una, sin fechas. "
        "Luego escribe qué permanece, qué cambia y un posible impacto en la sociedad.",
        "Problema: ¿qué es una vida buena? Etapa A: una vida buena es cumplir con la comunidad. Etapa B: es elegir con libertad el propio camino. Etapa C: es vivir en equilibrio con el entorno. Permanece: la pregunta por una vida buena. Cambia: el criterio (comunidad, libertad personal, entorno). Impacto: las escuelas valoran distintas cosas según la etapa.",
        ["escribe tres etapas con una frase cada una", "identifica una continuidad", "identifica un cambio con razones distintas", "propone un impacto posible"],
        ["tres etapas, continuidad, cambio e impacto escritos"],
        ["inventar fechas o autores reales", "decir que no hay continuidad", "describir solo una etapa"],
        "Pregunta: «¿qué pregunta de fondo se mantiene en las tres etapas?». Si no la ve, pídele que la formule en una frase."),
    reinforce="Elige un debate de tu entorno (por ejemplo, sobre las tareas) y escribe qué se mantiene y qué cambió en cómo se discute respecto de hace unos años.",
    extend="Escribe un panel de ejemplo para una cuarta etapa del problema de la libertad y explica qué continuidad y qué cambio introduce.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (de ejemplo). Tres usos de la palabra «libertad» en un taller ficticio. "
     "Uso 1: «Libre es quien no está encadenado ni amenazado.» "
     "Uso 2: «Libre es quien elige según sus razones y no según un impulso.» "
     "Uso 3: «Libre es quien podría haber hecho otra cosa en las mismas circunstancias.» "
     "Casos: Caso P: Lía firma un documento porque la amenazan. Caso Q: Iván elige entre dos carreras tras pensar en sus razones. Caso R: Dani deja que un dado decida qué camino tomar.")
build(
    O3, 2, F,
    use="Aprenderé a definir conceptos clave de un problema filosófico y a ver cómo su significado cambia entre etapas.",
    prior=["Sé qué es devenir, continuidad y cambio.", "Sé probar una definición con casos.", "Distingo condición necesaria de suficiente."],
    explain=[
        "Los conceptos de un problema filosófico cambian de significado con el tiempo. «Libertad» puede entenderse como ausencia de coacción (nadie te fuerza ni amenaza), como autodeterminación (eliges según tus razones) o como poder hacer otra cosa en las mismas circunstancias. Cada significado lleva a distintas conclusiones: con el primero, alguien puede ser libre aunque sus actos tengan causas; con el tercero, parece que todo lo causado quitaría libertad.",
        "El determinismo es la idea de que todo suceso tiene causas anteriores que lo hacen necesario. El azar es lo que ocurre sin causa que lo determine. La responsabilidad es poder ser considerado autor de un acto y tener que responder por él. Si la libertad fuera solo azar, los actos no serían de la persona; por eso el azar no es lo mismo que la libertad. Una postura sostiene que se puede ser libre aun con causas, si el acto nace de las propias razones; otra sostiene que sin posibilidad de hacer otra cosa no hay libertad.",
        "Definir con cuidado permite ver si dos etapas discuten lo mismo o solo usan la misma palabra con sentidos distintos. Antes de comparar respuestas, conviene fijar el significado de los conceptos en cada etapa.",
    ],
    vocab=[("libertad como ausencia de coacción", "no estar forzado ni amenazado"), ("autodeterminación", "elegir según las propias razones"), ("libertad como poder hacer otra cosa", "poder haber actuado de otra manera en las mismas circunstancias"), ("determinismo", "idea de que todo suceso tiene causas anteriores que lo hacen necesario"), ("azar", "lo que ocurre sin una causa que lo determine"), ("responsabilidad", "poder ser considerado autor de un acto y responder por él")],
    worked=[
        ("Aplicar un uso", "Según el Uso 1 de la ficha, ¿Lía (Caso P) es libre al firmar?",
         ["El Uso 1 pide no estar encadenado ni amenazado.", "Lía firma porque la amenazan."],
         "No: según el Uso 1, la amenaza le quita la libertad"),
        ("El azar no es libertad", "¿Por qué el Caso R (Dani y el dado) no muestra libertad en el sentido del Uso 2?",
         ["El Uso 2 pide elegir según las propias razones.", "Dani no elige según razones: deja que el azar decida."],
         "Porque no elige según sus razones, sino según el azar"),
    ],
    mistakes=[("Creer que el azar es lo contrario del determinismo y por lo tanto es libertad.", "Se confunde ausencia de causa con elección propia.", "Pregunta si el acto nace de las razones de la persona; el azar no las incluye."),
              ("Usar la palabra «libertad» sin decir en qué sentido se entiende.", "Se discute con la misma palabra, pero con significados diferentes.", "Aclara qué rasgos tiene la libertad en el sentido que usas.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es el determinismo?", "La idea de que todo suceso tiene causas anteriores que lo hacen necesario", "La idea de que todo ocurre al azar", "La idea de que somos siempre libres", "Esa es la definición de la explicación."),
        ("abc", "{F} ¿Qué uso de «libertad» corresponde a la autodeterminación?", "Uso 2", "Uso 1", "Uso 3", "Uso 2 habla de elegir según las propias razones."),
        ("abc", "{F} ¿Qué uso exige poder haber hecho otra cosa en las mismas circunstancias?", "Uso 3", "Uso 1", "Uso 2", "El Uso 3 pide explícitamente esa condición."),
        ("abc", "{F} Según el Uso 2, ¿Iván (Caso Q) es libre al elegir su carrera?", "Sí, porque elige según sus razones", "No, porque tiene dos opciones", "No, porque piensa demasiado", "Cumple lo que el Uso 2 pide: elegir según razones."),
        ("abc", "{F} Según el Uso 1, ¿Iván (Caso Q) es libre?", "Sí, porque nadie lo fuerza ni lo amenaza", "No, porque pensó en razones", "No, porque tuvo que elegir", "El Uso 1 solo exige no estar forzado."),
        ("ab", "{F} ¿Con qué uso es más difícil sostener que un acto con causas es libre?", "Uso 3", "Uso 1", "Si todo tiene causas anteriores, parece que no se podía hacer otra cosa; en cambio el Uso 1 solo pide ausencia de amenaza."),
        ("abc", "{F} ¿Qué dificultad plantea el Caso R (Dani y el dado) al Uso 3?", "Dani podría haber hecho otra cosa porque el dado pudo caer distinto, y aun así no parece libre", "Dani no habría podido hacer otra cosa, porque el dado lo obliga", "Dani sería libre solo si el dado cayera siempre igual", "Poder hacer otra cosa por azar no basta: el acto no nace de las razones de la persona."),
        ("abc", "¿Por qué el azar no puede ser lo mismo que la libertad según la explicación?", "Porque los actos azarosos no nacen de las razones de la persona", "Porque el azar es siempre malo", "Porque el azar no existe", "Un acto debe poder atribuirse a la persona para ser libre."),
        ("abc", "Alguien dice: «Si todo tiene causas, la libertad como autodeterminación sigue siendo posible». ¿En qué idea se apoya?", "En que las causas pueden ser las propias razones de la persona", "En que las causas no existen", "En que el azar decide", "Para esa postura, que haya causas no impide que el acto nazca de las razones propias."),
        ("abc", "¿Qué es la responsabilidad según la explicación?", "Poder ser considerado autor de un acto y responder por él", "No tener causas anteriores", "Hacer siempre lo mismo", "Se vincula con atribuir el acto a la persona."),
        ("abc", "Dos personas discuten si una persona amenazada fue libre. Una usa el Uso 1 y la otra el Uso 2. ¿Qué conviene hacer primero?", "Fijar en qué sentido usa cada una la palabra «libertad»", "Votar cuál suena mejor", "Aceptar el uso más antiguo", "Antes de comparar respuestas hay que fijar el significado."),
        ("abc", "{F} Si alguien dijera «Lía firmó porque la amenazaron, pero eligió según sus razones», ¿qué muestra respecto de los usos 1 y 2?", "Que algo puede cumplir el Uso 2 sin cumplir el Uso 1", "Que ambos usos son idénticos", "Que el Uso 3 es el correcto", "Los usos no coinciden en todos los casos."),
        ("abc", "¿Qué ventaja tiene fijar los conceptos antes de comparar etapas de un problema?", "Permite ver si discuten lo mismo o solo usan la misma palabra", "Evita todo desacuerdo", "Hace innecesario leer los textos", "Aclara si hay desacuerdo de fondo o solo de lenguaje."),
    ],
    ctx=("abc", "Un grupo ficticio discute: «¿Fue libre Camila al ceder su turno?». Camila dijo: «Nadie me obligó, pero lo hice por no quedar mal». ¿Cuál de estas observaciones usa distintos sentidos de «libertad»?", "Según no estar forzada fue libre, pero según elegir por sus razones podría discutirse", "La libertad se mide solo por lo que la persona dice sentir", "La libertad solo existe cuando hay azar", "Muestra cómo un mismo caso se evalúa distinto según el significado elegido."),
    sc=[
        ("En Seminario de filosofía: ¿qué es la autodeterminación?", "Elegir según las propias razones", "Es uno de los sentidos de libertad vistos."),
        ("¿Qué diferencia hay entre azar y libertad?", "El azar no nace de las razones de la persona; la libertad sí", "Un acto azaroso no se atribuye a la persona como elección."),
        ("¿Por qué conviene fijar los conceptos antes de comparar etapas?", "Para saber si discuten lo mismo o solo usan igual palabra", "Evita confundir desacuerdos de fondo con desacuerdos de lenguaje."),
    ],
    op=("Elige un concepto: «justicia», «castigo» o «familia». Escribe dos significados distintos que podría tener en dos etapas de ejemplo, un caso breve donde los significados den respuestas diferentes y qué cambia en la discusión según el significado.",
        "Concepto: castigo. Etapa A: castigo es hacer pagar por el daño (retribución). Etapa B: castigo es corregir para que no se repita (educar). Caso: un estudiante rompe un mueble por rabia. Según A, debe pagar; según B, debe aprender a manejar la rabia. Cambia el objetivo de la medida.",
        ["escribe dos significados claros", "presenta un caso concreto", "muestra respuestas distintas según el significado", "explica qué cambia en la discusión"],
        ["dos significados, un caso y su análisis"],
        ["definir con sinónimos", "usar un caso que no distingue los significados", "olvidar explicar el cambio"],
        "Pregunta: «¿tu caso da respuestas distintas con cada significado?». Si no, pídele que cambie un detalle del caso."),
    reinforce="Escribe tres frases sobre libertad usando cada uno de los tres usos de la ficha, con un caso cotidiano distinto en cada una.",
    extend="Explica con un ejemplo por qué «poder hacer otra cosa» y «elegir según razones» no siempre coinciden.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (textos de ejemplo; autores y obras ficticios, sin fechas). "
     "Texto A (Cleto Barrios, etapa A): «El hilo de cada vida lo hilan fuerzas más grandes que nosotros; por eso conviene aceptar lo que llega, y no culpar a quien actúa.» "
     "Texto B (Mirta Olivares, etapa B): «Antes de actuar delibero, pondero razones y elijo. Por eso respondo por lo que hago.» "
     "Texto C (Aurelio Ponce, etapa C): «Cada decisión tiene causas en la historia y el entorno de la persona. Por eso, en vez de castigar con dureza, conviene educar y mejorar las condiciones.»")
build(
    O3, 3, F,
    use="Aprenderé a reconstruir perspectivas de distintas etapas de un problema y a explicar sus continuidades y cambios en una línea de tiempo.",
    prior=["Sé separar continuidad y cambio.", "Sé reconstruir tesis, razón y supuesto.", "Sé qué es el contexto sociocultural."],
    explain=[
        "Para analizar el devenir de un problema se reconstruye la perspectiva de cada etapa con tesis, razones y supuesto, y luego se comparan. En la ficha, el Texto A sostiene que conviene aceptar lo que llega porque fuerzas superiores lo deciden; su razón es el hilo fijado de antemano, y su supuesto es que lo humano no puede cambiar el rumbo. El Texto B sostiene que la persona responde por sus actos porque delibera y elige. El Texto C sostiene que, como las decisiones tienen causas, conviene educar en lugar de castigar con dureza.",
        "La continuidad entre los tres textos es la relación entre lo que causa nuestros actos y cuánto se nos puede reprochar. El cambio está en qué se considera la causa: fuerzas superiores, la deliberación personal o las condiciones históricas y del entorno. El impacto aparece en cómo se trata a las personas: aceptar sin culpar, pedir responsabilidad o educar y mejorar condiciones.",
        "Una línea de tiempo es una forma de expresión que ordena las etapas y muestra cambios y continuidades de un vistazo. Otras formas son el ensayo, que argumenta; el diálogo, que enfrenta posturas; y el mapa conceptual, que muestra relaciones. Elegir la forma depende de lo que quieres mostrar y a quién.",
    ],
    vocab=[("línea de tiempo", "forma de expresión que ordena etapas y muestra cambios y continuidades"), ("mapa conceptual", "forma de expresión que muestra conceptos y sus relaciones"), ("ensayo", "texto que argumenta una idea con razones"), ("diálogo", "forma de expresión que enfrenta posturas en una conversación"), ("perspectiva de una etapa", "tesis, razones y supuestos propios de un momento del problema")],
    worked=[
        ("Reconstruir una etapa", "Reconstruye el Texto C: tesis, razón y supuesto.",
         ["Tesis: en vez de castigar con dureza, conviene educar y mejorar las condiciones.", "Razón: cada decisión tiene causas en la historia y el entorno."],
         "Tesis: educar en lugar de castigar con dureza. Razón: las decisiones tienen causas en la historia y el entorno. Supuesto: conocer las causas permite cambiar las conductas"),
        ("Continuidad entre textos", "¿Qué tienen en común A, B y C?",
         ["Los tres hablan de qué causa nuestros actos.", "Los tres sacan una consecuencia sobre cómo tratar a las personas."],
         "Relacionan lo que causa los actos con cómo corresponde tratar a las personas"),
    ],
    mistakes=[("Atribuir a una etapa ideas de otra, como poner la neurociencia en el Texto A.", "Se comete anacronismo: se usan conceptos que esa etapa no tenía.", "Usa solo las ideas y razones que el texto de esa etapa ofrece."),
              ("Describir cada texto por separado sin compararlos.", "No se logra ver el devenir del problema.", "Después de reconstruir cada texto, anota qué se mantiene y qué cambia.")],
    T=[
        ("abc", "{F} ¿Cuál es la tesis del Texto B?", "La persona responde por lo que hace porque delibera y elige", "Las fuerzas superiores deciden todo", "Hay que educar en lugar de castigar", "La conclusión del texto es que la persona responde por sus actos."),
        ("abc", "{F} ¿Qué supuesto se aprecia en el Texto A?", "Que lo humano no puede cambiar el rumbo fijado por fuerzas mayores", "Que las personas siempre eligen", "Que las causas se pueden estudiar", "Si el hilo lo hilan fuerzas mayores, se supone que no se puede modificar."),
        ("abc", "{F} ¿Qué razón ofrece el Texto C para preferir la educación al castigo duro?", "Cada decisión tiene causas en la historia y el entorno de la persona", "Las fuerzas superiores lo exigen", "Nadie delibera nunca", "La razón es que las decisiones tienen causas que se pueden mejorar."),
        ("abc", "{F} Una compañera dice: «Los tres textos coinciden en defender el castigo duro». ¿Qué responde mejor?", "Ninguno lo defiende: A pide no culpar, B pide responder por los actos y C prefiere educar", "Tiene razón, porque los tres hablan de responsabilidad", "Tiene razón en A y en B, pero no en C", "Ninguno de los tres textos propone el castigo duro como respuesta."),
        ("abc", "{F} ¿Qué cambia entre el Texto B y el Texto C?", "La causa que se destaca: de la deliberación personal a las condiciones y la historia", "El problema, que desaparece", "La idea de fuerzas superiores", "En C se subraya el papel del entorno y de la historia."),
        ("ab", "{F} ¿Qué texto concluye que no conviene culpar a quien actúa?", "Texto A", "Texto B", "Texto A pide aceptar lo que llega y no culpar; el B pide responder por los actos."),
        ("abc", "Una estudiante explica el Texto A así: «Cleto Barrios propone mejorar las condiciones del entorno para reducir los delitos». ¿Qué error comete?", "Anacronismo: atribuye al Texto A una idea que es propia de otra etapa", "Falacia genética", "Aplica bien el principio de caridad", "Esa idea corresponde al Texto C, no a la etapa A."),
        ("abc", "{F} ¿Qué impacto social sugiere el Texto C?", "Educar y mejorar condiciones en lugar de castigar con dureza", "Aceptar lo que llega sin culpar", "Pedir cuentas de cada acto por la deliberación", "Es la consecuencia práctica que el texto propone."),
        ("abc", "{F} ¿Qué forma de expresión mostraría mejor el orden de A, B y C y sus cambios?", "Una línea de tiempo", "Un solo párrafo sin títulos", "Una lista de autores sin textos", "La línea de tiempo ordena las etapas y permite ver cambios de un vistazo."),
        ("abc", "{F} ¿Qué forma de expresión serviría mejor para enfrentar las posturas de B y C en una conversación?", "Un diálogo", "Una tabla de números", "Un dibujo sin texto", "El diálogo pone en confrontación las razones de dos posturas."),
        ("abc", "¿Cuándo conviene un mapa conceptual en un análisis del devenir?", "Cuando se quiere mostrar cómo se relacionan conceptos como causa, libertad y responsabilidad", "Cuando se quiere argumentar con un largo texto", "Cuando se quiere citar a una persona", "El mapa muestra relaciones entre conceptos."),
        ("abc", "{F} Si un texto de la etapa C agregara «aun así cada persona debe reparar lo que dañó», ¿qué muestra respecto del devenir?", "Que ideas de etapas anteriores pueden mantenerse mezcladas con las nuevas", "Que la etapa C desaparece", "Que el problema se terminó", "El devenir combina continuidades y cambios, no solo reemplazos."),
        ("abc", "Un estudiante dice: «Como el Texto C es más nuevo, es más verdadero». ¿Qué falla?", "Ser posterior no prueba que sea verdadero: hay que evaluar sus razones", "Nada: lo nuevo siempre es verdadero", "El texto C no tiene razones", "La cronología no decide la verdad de una tesis."),
    ],
    ctx=("abc", "Un grupo ficticio debe presentar a su curso cómo cambió la manera de entender «el trabajo» a lo largo de tres etapas de ejemplo. Quieren que se vea el orden y los cambios de un vistazo. ¿Qué forma de expresión conviene?", "Una línea de tiempo con una frase por etapa y flechas de cambio", "Una sola frase final", "Un listado de nombres", "Una línea de tiempo muestra el orden y los cambios con claridad."),
    sc=[
        ("En Seminario de filosofía: ¿qué es una línea de tiempo?", "Una forma de expresión que ordena etapas y muestra cambios y continuidades", "Sirve para ver el devenir de un problema."),
        ("¿Qué es el anacronismo al comparar etapas de un problema?", "Atribuir a una etapa ideas o conceptos de otra", "Se evita usando solo lo que ofrece cada texto."),
        ("¿Qué se hace tras reconstruir cada texto?", "Compararlos para ver qué se mantiene y qué cambia", "Así se analiza el devenir y no solo cada texto."),
    ],
    op=("Elige uno de los dos temas y elabora una línea de tiempo de tres etapas de ejemplo, sin fechas. Tema 1: cómo se entiende «ser un buen estudiante». Tema 2: cómo se entiende «un buen vecino». "
        "Para cada etapa escribe una frase, y entre etapas anota una continuidad y un cambio. Cierra con una frase sobre el posible impacto.",
        "Tema 2. Etapa A: buen vecino es el que cumple con la comunidad. Etapa B: es el que respeta la libertad de cada uno. Etapa C: es el que se involucra en el bien común del barrio. Continuidad: la pregunta de cómo convivir. Cambio: de cumplir a respetar y luego a participar. Impacto: cambian las reglas de las juntas de vecinos.",
        ["incluye tres etapas ordenadas", "señala una continuidad", "señala un cambio con razones", "propone un impacto"],
        ["línea de tiempo de tres etapas con continuidad, cambio e impacto"],
        ["usar fechas o personas reales", "confundir cambio con reemplazo total", "no señalar la continuidad"],
        "Pregunta: «¿qué pregunta se mantiene de una etapa a otra?». Pídele que la escriba sobre la flecha."),
    reinforce="Dibuja una línea de tiempo de tres etapas sobre cómo se entiende «ser libre» y rotula una continuidad y un cambio.",
    extend="Reescribe tu línea de tiempo como un diálogo breve entre dos etapas y compara qué se ve mejor en cada forma de expresión.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (argumentos de ejemplo sobre el devenir de la libertad). "
     "Arg. 1: «Si todo tiene causas, nadie es responsable de lo que hace. Todo tiene causas. Por lo tanto, nadie es responsable.» "
     "Arg. 2: «El entorno influye en nuestras decisiones. Por lo tanto, nadie decide nada.» "
     "Arg. 3: «Si una sociedad cree que las personas eligen libremente, castiga con dureza. Esta sociedad castiga con dureza. Por lo tanto, cree que las personas eligen libremente.»")
build(
    O3, 4, F,
    use="Aprenderé a formular y evaluar argumentos sobre cómo un problema ha cambiado y qué impacto tiene en la sociedad, sin confundir explicar con justificar.",
    prior=["Sé reconstruir argumentos en premisas y conclusión.", "Sé qué es validez y qué es objeción.", "Sé separar continuidad y cambio."],
    explain=[
        "Un argumento sobre el devenir de un problema puede sostener que una idea tuvo ciertos efectos en la sociedad, o que un cambio de postura debería llevar a cambiar una práctica. Para evaluarlo se reconstruye en premisas y conclusión, se revisa su validez y se examinan las premisas. Una distinción útil es entre explicar y excusar: que un acto tenga causas lo explica, pero no por eso se concluye automáticamente que nadie debe responder por él.",
        "En la ficha, el Arg. 1 es válido: si las premisas fueran verdaderas, la conclusión se seguiría. La discusión se concentra en la premisa 1, que mezcla dos ideas: tener causas y no ser responsable. El Arg. 2 pasa de «influye» a «nadie decide nada», y esa conclusión no se sigue: influir no es lo mismo que determinar por completo. El Arg. 3 afirma el consecuente: una sociedad puede castigar con dureza por otras razones.",
        "Una postura sostiene que una persona puede ser responsable aun cuando sus actos tengan causas, si actúa a partir de sus propias razones. Otra sostiene que, si todo está causado, la responsabilidad pierde sentido. En ambos casos conviene exponer las razones y no solo nombrar la postura.",
    ],
    vocab=[("explicar un acto", "dar las causas que lo produjeron"), ("excusar un acto", "sostener que la persona no debe responder por él"), ("afirmar el consecuente", "concluir A desde «si A entonces B» y B, error de forma"), ("de «influye» a «determina»", "pasar de decir que algo influye a decir que lo determina por completo sin razones suficientes"), ("impacto social", "efecto de una idea en las prácticas e instituciones de una sociedad")],
    worked=[
        ("Evaluar un argumento", "¿Es válido el Arg. 1 de la ficha y dónde está la discusión?",
         ["Ordeno: P1: si todo tiene causas, nadie es responsable. P2: todo tiene causas. C: nadie es responsable.", "Si P1 y P2 fueran verdaderas, C se sigue; luego es válido."],
         "Es válido; la discusión está en la premisa 1, que une tener causas con no ser responsable"),
        ("Explicar y excusar", "¿Por qué explicar un acto no equivale a excusarlo?",
         ["Explicar es dar las causas que lo produjeron.", "Excusar es decir que la persona no debe responder; eso necesita una razón adicional."],
         "Porque conocer las causas no prueba por sí solo que la persona no deba responder"),
    ],
    mistakes=[("Concluir que, si un acto tiene causas, nadie tiene responsabilidad alguna.", "Se salta la distinción entre explicar y excusar.", "Examina si la premisa que une causas y responsabilidad está justificada."),
              ("Decir que un cambio de idea en una sociedad prueba que la idea sea verdadera.", "Se confunde impacto o aceptación con verdad.", "Distingue qué efectos tuvo una idea y si sus razones son buenas.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué diferencia hay entre explicar y excusar un acto?", "Explicar da sus causas; excusar sostiene que la persona no debe responder", "Son sinónimos", "Excusar es dar las causas", "Una cosa es dar causas y otra, concluir sobre la responsabilidad."),
        ("abc", "{F} ¿Cuál es la conclusión del Arg. 1?", "Nadie es responsable", "Todo tiene causas", "Si todo tiene causas, alguien es responsable", "Es la afirmación que viene tras «por lo tanto»."),
        ("abc", "{F} Si el Arg. 1 es válido y se acepta su premisa 1, ¿qué más hace falta para que sea sólido?", "Que la premisa 2 también sea verdadera", "Que la conclusión sea falsa", "Nada más: es sólido por ser válido", "La solidez exige validez y premisas verdaderas, todas."),
        ("abc", "{F} ¿Por qué el Arg. 2 no es válido?", "De «influye» no se sigue «nadie decide nada»", "Porque tiene tres premisas", "Porque habla de sociedades", "Influir en algo no equivale a determinarlo por completo."),
        ("abc", "{F} ¿Qué error de forma tiene el Arg. 3?", "Afirma el consecuente", "Es una deducción válida", "Ataca a la persona", "Concluye A desde «si A entonces B» y B."),
        ("ab", "{F} ¿Cómo se puede mostrar que el Arg. 3 es inválido?", "Con una sociedad que castiga con dureza por tradición y no por creer en la libertad", "Mostrando que la premisa 1 es falsa", "Un caso con premisas verdaderas y conclusión falsa muestra la invalidez; negar una premisa es otra cosa."),
        ("abc", "Un estudiante responde al Arg. 1: «Hay causas, pero una persona puede actuar a partir de sus propias razones y por eso responde». ¿Qué ataca?", "La premisa 1", "La forma del argumento", "La premisa 2, afirmando que no todo tiene causas", "Acepta las causas y discute que de ellas se siga que nadie responda."),
        ("abc", "Un docente ficticio dice: «Como en esta sociedad dejó de castigarse con dureza, la idea de que se puede educar es verdadera». ¿Qué error comete?", "Confunde el impacto o la aceptación de una idea con su verdad", "Aplica bien el principio de caridad", "Usa una analogía fuerte", "Que una práctica cambie no prueba que la idea que la sostenía sea correcta."),
        ("abc", "{F} ¿Cuál de estas es una objeción pertinente al Arg. 2?", "Se necesitaría mostrar que el entorno no solo influye, sino que determina por completo", "El entorno es un tema aburrido", "Quien lo escribió no vive en un barrio", "Señala la brecha entre las premisas y la conclusión."),
        ("abc", "{F} Si cambiamos el Arg. 3 por «si una sociedad cree que las personas eligen libremente, castiga con dureza; esta sociedad cree que eligen libremente; luego castiga con dureza», ¿qué ocurre?", "Pasa a ser válido", "Sigue siendo inválido", "Se vuelve inductivo", "La nueva forma, «si A entonces B; A; luego B», garantiza la conclusión."),
        ("abc", "Alguien argumenta: «Como Mateo creció en un entorno con muchos problemas, no es responsable de nada». ¿Qué conviene preguntar?", "Si de tener causas se sigue que no deba responder", "Cuántos años tiene Mateo", "Si el entorno tiene plazas", "Examina la premisa que une causa con ausencia de responsabilidad."),
        ("abc", "¿Por qué conviene exponer las razones de una postura y no solo nombrarla?", "Porque solo con las razones se puede evaluar si es una buena postura", "Porque nombrarla es suficiente", "Porque las razones no importan", "Las razones permiten examinar premisas y supuestos."),
        ("abc", "{F} Un lector dice del Arg. 2: «Es una falacia». ¿Qué debería hacer para que su crítica valga?", "Reconstruirlo y mostrar qué premisa o qué paso falla", "Repetir la palabra falacia", "Atacar a quien lo escribió", "La crítica necesita mostrar dónde y por qué falla el argumento."),
    ],
    ctx=("abc", "En un liceo ficticio, algunos docentes sostienen: «Un estudiante que faltó por un paro del transporte público no debe ser sancionado, porque no pudo evitarlo». Otros: «Se pueden explicar sus faltas, pero igual debe recuperar el contenido». ¿Qué distinción usa la segunda postura?", "Entre explicar las causas de un acto y excusar la responsabilidad de reparar", "Entre faltar y asistir", "Entre sanción y premio", "Reconoce las causas y mantiene una responsabilidad de recuperar el contenido."),
    sc=[
        ("En Seminario de filosofía: ¿qué significa afirmar el consecuente?", "Concluir A desde «si A entonces B» y B", "Es un error de forma, pues B puede tener otras causas."),
        ("¿Qué es excusar un acto?", "Sostener que la persona no debe responder por él", "No es lo mismo que explicar sus causas."),
        ("¿Por qué la aceptación de una idea no prueba que sea verdadera?", "Porque el impacto o la aceptación no son razones", "Hay que evaluar sus razones, no solo sus efectos."),
    ],
    op=("Elige una de estas ideas: «si se acepta que el entorno influye mucho, los colegios deberían cambiar sus reglas de convivencia» o «si las personas eligen libremente, las normas deben ser más estrictas». "
        "Escribe un argumento breve con dos premisas y una conclusión, indica si es válido, escribe una objeción a una premisa y exprésalo en una forma a elegir (ensayo breve, diálogo o mapa).",
        "Idea 1. P1: si el entorno influye mucho, conviene adaptar las reglas a las condiciones de cada estudiante. P2: el entorno influye mucho. C: conviene adaptar las reglas. Es válido. Objeción a P1: adaptar demasiado puede tratar distinto a quienes están en la misma situación. Forma: diálogo breve entre dos docentes.",
        ["ordena premisas y conclusión", "evalúa la validez", "formula una objeción a una premisa", "elige una forma de expresión adecuada"],
        ["argumento, juicio de validez, objeción y forma elegida"],
        ["nombrar una falacia sin reconstruir", "confundir explicar con excusar", "atacar a las personas"],
        "Pregunta: «¿qué premisa podría ser falsa?». Pídele que la subraye y explique su objeción."),
    reinforce="Escribe un argumento válido con la forma «si A entonces B; A; luego B» sobre una práctica escolar y otro inválido que afirme el consecuente.",
    extend="Escribe en una página un ensayo breve sobre si explicar las causas de un acto cambia lo que le corresponde a la persona.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (objeciones de ejemplo al relato del devenir). Relato: «La libertad se entendió primero como destino, luego como deliberación y por último como resultado de causas.» "
     "Objeción 1: «Cada idea nueva reemplaza a la anterior, así que las etapas pasadas ya no importan.» "
     "Objeción 2: «Si cambian tanto las razones y los conceptos, no es el mismo problema; no hay devenir de un problema.» "
     "Objeción 3: «Ese relato muestra un progreso hacia la verdad; las etapas anteriores estaban equivocadas.»")
build(
    O3, 5, F,
    use="Aprenderé a responder objeciones a un análisis del devenir de un problema y a elegir formas de expresión adecuadas para comunicarlo.",
    prior=["Sé separar continuidad, cambio e impacto.", "Sé responder una objeción con una estrategia.", "Sé qué es una línea de tiempo."],
    explain=[
        "Un relato del devenir de un problema puede recibir objeciones. Una objeción frecuente es creer que cada etapa reemplaza por completo a la anterior. Pero las ideas antiguas siguen presentes: reaparecen, se corrigen o se combinan con las nuevas. Otra objeción dice que, si cambian los conceptos, ya no es el mismo problema. Una respuesta es distinguir entre el problema de fondo (la pregunta que se mantiene) y las formulaciones, que cambian.",
        "Una tercera objeción interpreta el relato como un progreso lineal hacia la verdad. Pero que una etapa sea posterior no prueba que sea más verdadera: cada una debe evaluarse por sus razones. Responder bien exige reconocer lo que la objeción tiene de razón, por ejemplo que las etapas no son idénticas, y mostrar qué parte no se sostiene.",
        "Comunicar un análisis del devenir exige elegir una forma de expresión según el propósito y la audiencia. La línea de tiempo muestra el orden y los cambios, el ensayo argumenta con razones, el diálogo pone en confrontación posturas, el mapa conceptual muestra relaciones y un cartel sintetiza para un público amplio. Se puede combinar más de una.",
    ],
    vocab=[("progreso lineal", "idea de que cada etapa es mejor y más verdadera que la anterior"), ("reemplazo total", "idea de que una etapa nueva borra por completo a la anterior"), ("problema de fondo", "pregunta que se mantiene a pesar de que cambien las formulaciones"), ("formulación", "manera concreta de plantear un problema en una etapa"), ("audiencia", "personas a quienes se dirige una forma de expresión")],
    worked=[
        ("Responder la objeción 1", "¿Cómo se puede responder a la objeción 1 de la ficha?",
         ["Pregunto si es cierto que las ideas antiguas desaparecen del todo.", "Muestro un contraejemplo: la idea de que cada persona responde por sus actos sigue discutiéndose en otras etapas."],
         "Con un contraejemplo: las ideas anteriores reaparecen, se corrigen o se combinan"),
        ("Elegir una forma", "Un grupo quiere mostrar al curso, de un vistazo, cómo cambió un problema. ¿Qué forma elige?",
         ["Busco la forma que ordena etapas y cambios en poco espacio.", "La línea de tiempo cumple esa función para un curso entero."],
         "Una línea de tiempo"),
    ],
    mistakes=[("Responder a la objeción de progreso diciendo que el pasado era mejor.", "Se cambia un progreso lineal por un retroceso lineal, que tampoco se justifica.", "Evalúa cada etapa por sus razones, no por su lugar en el tiempo."),
              ("Usar la misma forma de expresión para cualquier propósito y audiencia.", "No se considera lo que se quiere mostrar ni a quién.", "Elige la forma según el propósito y la audiencia.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es un progreso lineal?", "La idea de que cada etapa es mejor y más verdadera que la anterior", "Una línea de tiempo con fechas", "La repetición de una misma idea", "Es la idea que la objeción 3 atribuye al relato."),
        ("abc", "{F} ¿Qué afirma la objeción 1?", "Que cada idea nueva reemplaza a la anterior y las etapas pasadas ya no importan", "Que el problema no existe", "Que la libertad es siempre la misma", "Es la tesis del reemplazo total."),
        ("abc", "{F} ¿Qué estrategia sirve para responder la objeción 2?", "Distinguir entre el problema de fondo y sus formulaciones", "Repetir el relato sin cambios", "Atacar a quien objeta", "Se acepta que cambian las formulaciones, pero la pregunta de fondo continúa."),
        ("abc", "{F} ¿Por qué la objeción 3 no se sostiene por sí sola?", "Porque que una etapa sea posterior no prueba que sea más verdadera", "Porque las etapas tempranas no existieron", "Porque las razones no importan", "Cada etapa se evalúa por sus razones y no por el momento."),
        ("abc", "{F} ¿Qué verdad parcial tiene la objeción 2?", "Que las razones y los conceptos sí cambian entre etapas", "Que el problema no tiene pregunta de fondo", "Que nada permanece", "Reconocerlo permite responder a la objeción con precisión."),
        ("ab", "{F} Frente a la objeción 1, ¿cuál es mejor respuesta?", "Las ideas antiguas reaparecen, se corrigen o se combinan con las nuevas", "Las ideas antiguas siempre son mejores", "La primera ofrece una razón concreta; la segunda cambia un reemplazo por un retroceso igual de dudoso."),
        ("abc", "Alguien responde a la objeción 3: «Al contrario, el pasado siempre fue mejor». ¿Qué falla?", "Cambia un progreso lineal por un retroceso lineal, que tampoco se justifica", "Responde exactamente a la objeción", "Concede en parte con razones", "Ambas ideas olvidan evaluar las razones de cada etapa."),
        ("abc", "{F} ¿Qué forma de expresión conviene para explicar a un curso, con poco texto, cómo cambió el problema?", "Un cartel con las etapas y un cambio clave", "Un ensayo de diez páginas", "Una lista de nombres", "Un cartel sintetiza para una audiencia amplia."),
        ("abc", "Si se quiere argumentar con razones que una etapa no reemplazó a otra, ¿qué forma conviene?", "Un ensayo", "Una línea de tiempo", "Un cartel", "El ensayo desarrolla razones y objeciones."),
        ("abc", "Si se quiere que dos posturas se enfrenten con sus mejores razones, ¿qué forma conviene?", "Un diálogo", "Una línea de tiempo", "Un mapa conceptual", "El diálogo coloca cara a cara las posturas."),
        ("abc", "Si se quiere mostrar cómo se conectan los conceptos de causa, libertad y responsabilidad, ¿qué forma conviene?", "Un mapa conceptual", "Una línea de tiempo", "Un diálogo", "El mapa conceptual muestra las relaciones entre conceptos."),
        ("abc", "{F} Un estudiante dice: «Como las etapas A, B y C son tan distintas, no hay nada en común». ¿Qué conviene responderle?", "Que hay una pregunta de fondo común, aunque cambien las formulaciones", "Que tiene razón en todo", "Que lo que cambia no importa", "Se distingue continuidad de cambio y se muestra que ambas existen."),
        ("abc", "¿Qué se necesita para elegir bien una forma de expresión?", "Considerar qué se quiere mostrar y a quién", "Elegir siempre la más larga", "Elegir la que usaron otros", "El propósito y la audiencia orientan la elección."),
    ],
    ctx=("abc", "Una estudiante ficticia presentó una línea de tiempo y alguien objetó: «Eso muestra que todo mejora con el tiempo». Ella respondió: «Mi línea de tiempo muestra el orden, no cuál etapa es más verdadera; cada una se evalúa por sus razones». ¿Qué hizo?", "Distinguió entre orden temporal y verdad", "Atacó a quien objetó", "Cambió de tema", "Aclara que el orden de las etapas no mide su verdad."),
    sc=[
        ("En Seminario de filosofía: ¿qué es el problema de fondo?", "La pregunta que se mantiene aunque cambien las formulaciones", "Permite hablar de devenir de un mismo problema."),
        ("¿Por qué ser posterior no prueba ser más verdadero?", "Porque cada postura se evalúa por sus razones, no por su fecha", "El orden temporal no decide la verdad."),
        ("¿Qué dos cosas se consideran al elegir una forma de expresión?", "El propósito y la audiencia", "Ambos factores determinan qué forma comunica mejor."),
    ],
    op=("Elige una objeción a un relato del devenir: «la idea nueva reemplaza a la antigua» o «ser más nuevo es ser más verdadero». Escribe una respuesta en tres líneas con una estrategia nombrada, y elige una forma de expresión (línea de tiempo, ensayo, diálogo, mapa o cartel) para comunicarla a un público de tu elección, explicando por qué esa forma.",
        "Objeción: «ser más nuevo es ser más verdadero». Respuesta (distinguir): el orden en el tiempo no es una razón; cada postura se evalúa por sus premisas. Forma: diálogo breve entre dos estudiantes para un público de compañeros, porque enfrenta las razones de manera cercana.",
        ["responde exactamente a la objeción", "nombra la estrategia", "elige una forma de expresión adecuada", "explica la elección con el propósito y la audiencia"],
        ["respuesta de tres líneas y una forma de expresión justificada"],
        ["repetir el relato sin responder", "elegir la forma sin explicar por qué", "no considerar la audiencia"],
        "Pregunta: «¿para quién es tu producto y qué quieres que entiendan?». Pídele que ajuste la forma a esa respuesta."),
    reinforce="Elige una de las tres objeciones de la ficha y escribe dos respuestas distintas con estrategias diferentes.",
    extend="Transforma tu línea de tiempo de la clase 3 en un cartel para otro público (por ejemplo, estudiantes de primero medio) y explica qué cambiaste.",
)
