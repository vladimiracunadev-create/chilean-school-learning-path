"""Seminario de filosofía (electivo HC, 3.º y 4.º medio): OAC-02 (evaluar y contrastar métodos de razonamiento para abordar un concepto o problema filosófico, clases 1 a 5). Casos, diálogos y argumentos ficticios o «de ejemplo»."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada caso, diálogo y argumento está escrito en el enunciado. "
             "Los personajes, los lugares y los textos son ficticios o «de ejemplo»: sirven para practicar el razonamiento y no son citas de ninguna obra real. "
             "Los métodos se presentan con sus fortalezas y sus límites, sin declarar uno mejor que los demás: tu tarea es entenderlos, compararlos y evaluarlos con razones. "
             "Si un caso te incomoda, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O2 = "FI-SEFI-3y4-OAC-02"

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (caso ficticio). El liceo «Bahía Clara» (no existe) tiene un robot de biblioteca llamado Tila, que responde preguntas de los estudiantes. Tres estudiantes discuten si Tila «entiende» lo que dice. "
     "Valeria: «Hagámosle cien preguntas distintas y veamos cuántas acierta.» "
     "Samuel: «Si entender es usar símbolos según reglas, y Tila usa símbolos según reglas, entonces Tila entiende.» "
     "Noa: «Imaginemos una persona encerrada en una sala que responde con un manual de reglas escrito en un idioma que no conoce. Contesta bien, ¿entiende el idioma?»")
build(
    O2, 1, F,
    use="Aprenderé a reconocer cómo un problema filosófico puede abordarse con distintos métodos de razonamiento y a ver qué permite concluir cada uno.",
    prior=["Sé qué es un argumento válido.", "Sé reconstruir premisas y conclusión.", "Sé formular un problema filosófico."],
    explain=[
        "Un método de razonamiento es una manera ordenada de pasar de razones a una conclusión. Ante un mismo problema filosófico se pueden usar métodos distintos, y cada uno destaca un tipo de razones. Observar muchos casos y mirar qué ocurre es un camino. Partir de una definición y deducir qué se sigue de ella es otro. Imaginar un caso inventado, un experimento mental, y preguntarse qué diríamos sobre él es un tercero.",
        "En la ficha, el problema es qué significa entender. Valeria propone reunir casos y contar aciertos. Samuel parte de una definición de entender y deduce una conclusión. Noa propone un caso imaginado para poner a prueba la idea de que responder bien basta para entender. Los tres hablan del mismo problema, pero cada método puede llevar a respuestas distintas.",
        "Antes de decidir qué respuesta aceptar conviene preguntar de cada método qué supone, qué permite concluir y qué no. Un método no se evalúa por si da la conclusión que nos gusta, sino por la calidad de las razones que ofrece y por sus límites.",
    ],
    vocab=[("método de razonamiento", "manera ordenada de pasar de razones a una conclusión"), ("observar casos", "reunir muchos casos y examinar qué ocurre en ellos"), ("deducir", "sacar una conclusión que se sigue necesariamente de ciertas premisas"), ("experimento mental", "caso imaginado que se usa para poner a prueba una idea"), ("límite de un método", "aquello que un método no permite concluir")],
    worked=[
        ("Identificar el método", "En la ficha, ¿qué método usa Valeria?",
         ["Veo qué hace: propone reunir cien preguntas distintas y contar los aciertos.", "Su razón se apoya en muchos casos observados."],
         "Observar casos y contar aciertos"),
        ("Qué permite concluir", "Si Tila acierta 98 de 100 preguntas de ejemplo, ¿qué permite concluir el método de Valeria?",
         ["Los aciertos muestran que Tila suele responder bien.", "No muestran por sí solos qué ocurre dentro de Tila ni si entiende."],
         "Que Tila suele acertar, pero no que entienda"),
    ],
    mistakes=[("Evaluar un método por si da la conclusión que uno prefiere.", "Se mira el resultado y no la calidad de las razones.", "Pregunta qué supone el método, qué permite concluir y qué límites tiene."),
              ("Creer que un solo método sirve para todos los problemas.", "Se ignora que cada método destaca un tipo de razones.", "Pregunta qué tipo de razones necesita el problema y qué método las da.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es un método de razonamiento?", "Una manera ordenada de pasar de razones a una conclusión", "Una lista de datos sobre un tema", "Una opinión repetida muchas veces", "Es un camino ordenado de razones a conclusión, no un dato ni una opinión."),
        ("abc", "{F} ¿Cuál es el problema que comparten los tres estudiantes?", "Qué significa que Tila entienda lo que dice", "Cuántas preguntas pueden hacerse a un robot", "Cómo se construyó el robot", "Los tres discuten si responder bien equivale a entender."),
        ("abc", "{F} ¿Qué método propone Samuel?", "Partir de una definición y deducir qué se sigue de ella", "Imaginar un caso inventado", "Contar aciertos en muchas preguntas", "Su razonamiento usa «si entender es…, entonces…» para sacar una conclusión."),
        ("abc", "{F} ¿Qué método propone Noa?", "Un experimento mental con una persona imaginada", "Contar los aciertos de Tila", "Deducir desde una definición de entender", "Propone un caso inventado, la persona con el manual, para examinar una idea."),
        ("abc", "{F} ¿Qué idea pone a prueba el caso de Noa?", "Que responder bien basta para entender", "Que Tila se equivoca mucho", "Que los manuales son inútiles", "Muestra a alguien que responde bien sin entender, para discutir si lo primero basta."),
        ("ab", "{F} ¿Cuál de los tres métodos usa un caso que no necesita existir en la realidad?", "El de Noa", "El de Valeria", "El experimento mental trabaja con una situación imaginada, mientras Valeria necesita casos reales de preguntas a Tila."),
        ("abc", "Dos estudiantes de ejemplo llegan a conclusiones opuestas usando métodos distintos. ¿Qué conviene hacer primero?", "Examinar qué supone cada método y qué permite concluir", "Votar y aceptar la respuesta de la mayoría", "Elegir al estudiante que habla con más seguridad", "Antes de decidir hay que ver los supuestos y límites de cada camino."),
        ("abc", "{F} Si Tila acierta 92 de 100 preguntas de ejemplo, ¿qué es lo máximo que se puede concluir con el método de Valeria?", "Que Tila suele acertar", "Que Tila entiende todo lo que dice", "Que Tila nunca se equivoca", "El resultado muestra regularidad de aciertos, pero no qué hay detrás de ellos."),
        ("abc", "{F} Samuel dice: «Entender es usar símbolos según reglas». ¿Qué parte de su razonamiento es la más discutible?", "Su definición de entender, porque la conclusión depende de ella", "Que concluye algo sobre un robot y no sobre una persona", "Que la forma «si…, entonces…» nunca permite deducir nada", "Si la definición es dudosa, la conclusión que se deduce de ella también lo es."),
        ("abc", "Un estudiante dice: «Mi método es el correcto porque me dio la respuesta que quería». ¿Qué error comete?", "Evalúa el método por su resultado y no por la calidad de sus razones", "Aplica bien el principio de caridad", "Usa un método deductivo", "Un método se evalúa por sus razones y límites, no por si coincide con lo que uno prefería."),
        ("abc", "¿Por qué un mismo problema puede recibir respuestas distintas según el método?", "Porque cada método destaca un tipo de razones diferente", "Porque los problemas filosóficos no tienen sentido", "Porque los métodos siempre se equivocan", "Observar casos, deducir o imaginar casos aportan clases distintas de razones."),
        ("abc", "{F} Si en el caso de Noa la persona encerrada sí conociera el idioma del manual, ¿qué cambiaría para el experimento?", "Dejaría de mostrar que se puede responder bien sin entender", "Seguiría mostrándolo igual", "Mostraría que Tila no entiende nada", "El caso pierde su fuerza si se quita la condición de no conocer el idioma."),
        ("abc", "¿Qué hace un experimento mental con un concepto?", "Lo pone a prueba con un caso imaginado para ver qué diríamos de él", "Lo mide con instrumentos", "Lo reemplaza por un dato", "Se usa un caso inventado para examinar si una idea resiste."),
    ],
    ctx=("abc", "En un taller ficticio se pregunta si una persona que memoriza un poema entiende el poema. Un estudiante imagina a alguien que repite perfecto un poema en un idioma que no conoce. ¿Qué método usa?", "Un experimento mental, porque pone a prueba la idea con un caso imaginado", "Una deducción desde una definición de memoria", "Una medición con cronómetro", "Se apoya en un caso inventado para examinar si repetir basta para entender."),
    sc=[
        ("En Seminario de filosofía: ¿qué es un experimento mental?", "Un caso imaginado que sirve para poner a prueba una idea", "Se razona sobre una situación inventada para ver qué diríamos de ella."),
        ("¿Cómo se evalúa un método de razonamiento?", "Por la calidad de sus razones y sus límites", "No se evalúa por si da la respuesta que preferimos."),
        ("¿Qué preguntas conviene hacer de cada método?", "Qué supone, qué permite concluir y qué no", "Son las tres preguntas de la explicación."),
    ],
    op=("Elige un problema ficticio. Problema 1: ¿puede una persona ser libre si todas sus decisiones se explican por su historia? Problema 2: ¿cuenta como mentir decir algo falso en una obra de teatro? "
        "Escribe qué método usarías para abordarlo (observar casos, deducir desde una definición o un caso imaginado), cómo lo aplicarías en dos o tres pasos, qué permitiría concluir y qué no.",
        "Problema 2. Método: caso imaginado. Imagino a una actriz que dice «el rey ha muerto» en una función, y a un vendedor que dice algo falso para engañar. Comparo: el vendedor busca que el otro crea algo falso y la actriz no. Permite concluir que la intención de engañar importa. No permite concluir cuál es la definición completa de mentir.",
        ["elige un método y lo aplica en pasos", "usa un caso o razón concretos", "dice qué permite concluir", "indica un límite del método"],
        ["método elegido, aplicación en pasos, qué permite concluir y un límite"],
        ["nombrar el método sin aplicarlo", "no decir ningún límite", "elegir el método por su resultado"],
        "Pregunta: «¿qué no podrías concluir con ese método?». Si no sabe, pídele que busque un caso que la conclusión no explique."),
    reinforce="Elige un problema de tu entorno y escribe una pregunta que se pueda abordar observando casos y otra que se aborde mejor con un caso imaginado.",
    extend="Escribe un experimento mental propio de cuatro líneas sobre qué significa «aprender» y qué idea pone a prueba.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (argumentos de ejemplo). "
     "M1: «Todos los mamíferos respiran aire. La ballena de la ficha es un mamífero. Por lo tanto, respira aire.» "
     "M2: «Las seis plantas de ejemplo que se regaron a diario crecieron; las seis que no se regaron se secaron. Por lo tanto, regar ayuda a que crezcan.» "
     "M3: «El taller amaneció con la puerta abierta y barro en el piso. La mejor explicación es que alguien entró en la noche.» "
     "M4: «La memoria se parece a una libreta: ambas guardan información. Una libreta se puede borrar, así que la memoria también.»")
build(
    O2, 2, F,
    use="Aprenderé a definir los principales métodos de razonamiento y a distinguir, con criterios, qué garantiza y qué no garantiza cada uno.",
    prior=["Sé qué es un método de razonamiento.", "Sé qué es validez y solidez.", "Sé qué es un experimento mental."],
    explain=[
        "El razonamiento deductivo saca una conclusión que se sigue necesariamente de las premisas: si estas son verdaderas, la conclusión también lo es. Se evalúa con la validez. El razonamiento inductivo generaliza desde casos observados a otros casos o a todos: la conclusión es probable, no segura, y se evalúa como fuerte o débil según cuántos casos hay y qué tan variados son.",
        "La inferencia a la mejor explicación parte de un hecho y elige la explicación que mejor lo explica entre varias posibles; es probable y puede cambiar si aparece otra explicación mejor. El razonamiento por analogía sostiene que, si dos cosas se parecen en ciertos aspectos, también se parecerán en otro; es más fuerte cuando las semejanzas son relevantes y débil cuando las diferencias lo son. El experimento mental y la reducción al absurdo, que supone algo para mostrar que lleva a una consecuencia inaceptable, son otros caminos.",
        "Para contrastar métodos se usan tres criterios: qué grado de seguridad ofrece la conclusión, qué supuestos necesita y en qué casos falla. Ningún método sirve para todo: la deducción da seguridad, pero no aporta información que no estaba ya en las premisas; la inducción amplía el conocimiento, pero con riesgo.",
    ],
    vocab=[("razonamiento deductivo", "saca una conclusión que se sigue necesariamente de las premisas"), ("razonamiento inductivo", "generaliza desde casos observados con una conclusión probable"), ("inferencia a la mejor explicación", "elige entre varias la explicación que mejor da cuenta de un hecho"), ("analogía", "razonamiento que concluye que dos cosas parecidas también lo serán en otro aspecto"), ("reducción al absurdo", "supone algo para mostrar que lleva a una consecuencia inaceptable"), ("argumento fuerte", "argumento inductivo cuyas premisas hacen muy probable la conclusión")],
    worked=[
        ("Clasificar un argumento", "¿Qué tipo de razonamiento es M2 de la ficha?",
         ["Veo que parte de casos observados (seis plantas regadas, seis sin regar).", "Generaliza a una conclusión que no es necesaria, sino probable."],
         "Inductivo: generaliza desde casos observados"),
        ("Contrastar garantías", "¿Qué diferencia de seguridad hay entre M1 y M2?",
         ["En M1, si las premisas son verdaderas, la conclusión necesariamente lo es.", "En M2, aunque las premisas sean verdaderas, la conclusión solo es probable."],
         "M1 es seguro si sus premisas son verdaderas; M2 solo probable"),
    ],
    mistakes=[("Decir que un argumento inductivo es inválido porque su conclusión no es segura.", "Se evalúa con el criterio de la deducción un razonamiento que busca probabilidad.", "Evalúa la inducción como fuerte o débil, no como válida o inválida."),
              ("Creer que la conclusión de una inferencia a la mejor explicación es segura.", "Se olvida que puede aparecer una explicación mejor.", "Pregunta qué otras explicaciones hay y qué evidencia las distingue.")],
    T=[
        ("abc", "{F} ¿Qué tipo de razonamiento es M1?", "Deductivo, porque la conclusión se sigue necesariamente de las premisas", "Inductivo, porque habla de animales", "Por analogía, porque compara mamíferos", "Va de una regla general a un caso particular con garantía."),
        ("abc", "{F} ¿Qué tipo de razonamiento es M3?", "Inferencia a la mejor explicación", "Deductivo", "Reducción al absurdo", "Elige la explicación que mejor da cuenta de la puerta abierta y el barro."),
        ("abc", "{F} ¿Qué tipo de razonamiento es M4?", "Analogía", "Inducción a partir de seis casos", "Deducción desde una regla", "Concluye algo de la memoria a partir de su parecido con una libreta."),
        ("abc", "En Seminario de filosofía, ¿qué distingue a un argumento deductivo válido?", "Si las premisas son verdaderas, la conclusión necesariamente lo es", "Que su conclusión es probable", "Que usa muchos ejemplos", "Esa es la garantía propia de la validez."),
        ("abc", "¿Cómo se evalúa un argumento inductivo?", "Como fuerte o débil, según la cantidad y variedad de casos", "Como válido o inválido solamente", "Por cuántas personas lo repiten", "La inducción no ofrece necesidad, sino probabilidad mayor o menor."),
        ("ab", "{F} ¿Cuál de estos argumentos de la ficha tiene una conclusión solo probable?", "M2", "M1", "M2 generaliza desde casos y puede fallar, mientras M1 es deductivo."),
        ("abc", "{F} En M3 aparece otro dato: el guardia ve que el viento abrió la puerta y entró barro. ¿Qué efecto tiene en la inferencia?", "Ofrece una explicación alternativa y debilita la conclusión de que alguien entró", "La hace deductiva", "No tiene ningún efecto", "Una explicación igual de buena baja la probabilidad de la que se había elegido."),
        ("abc", "{F} En M4, ¿qué diferencia relevante debilitaría la analogía?", "Que los recuerdos se reconstruyen y no se borran como un texto", "Que la libreta tiene hojas", "Que ambas guardan información", "Una diferencia relevante para la conclusión (borrar) debilita la semejanza."),
        ("abc", "Un estudiante dice: «Visité tres veces la cafetería y siempre estaba cerrada los lunes; así que siempre está cerrada los lunes». ¿Cuál es la mejor evaluación?", "Inducción débil: tres casos es poco para generalizar", "Deducción válida", "Inducción fuerte, porque coincidió todas las veces", "Con pocos casos, la generalización es débil, aunque no haya excepciones observadas."),
        ("abc", "«Supongamos que solo existe lo que se puede ver. Entonces el aire no existiría, pero respiramos aire y sentimos el viento. Eso es inaceptable. Así que no solo existe lo que se puede ver.» ¿Qué método usa?", "Reducción al absurdo", "Inducción", "Analogía", "Supone algo para mostrar que lleva a una consecuencia inaceptable."),
        ("abc", "¿Cuál es una ventaja de la deducción sobre la inducción?", "Si las premisas son verdaderas, la conclusión es segura", "Siempre aporta información nueva", "Nunca necesita premisas", "Esa seguridad es su ventaja, a costa de no ampliar lo ya contenido en las premisas."),
        ("abc", "{F} ¿Por qué M2 no es un argumento deductivo?", "Porque, aunque las premisas sean verdaderas, la conclusión podría ser falsa", "Porque no tiene premisas", "Porque habla de plantas", "Generaliza desde algunos casos y no garantiza la conclusión."),
        ("abc", "Alguien dice: «La inferencia a la mejor explicación es segura porque elige la mejor». ¿Qué falla?", "Que puede aparecer una explicación mejor y cambiar la conclusión", "Que no usa premisas", "Que solo funciona con números", "La conclusión es provisional: depende de las explicaciones alternativas conocidas."),
    ],
    ctx=("abc", "En un taller ficticio, una estudiante afirma: «Cada vez que probé la linterna nueva funcionó, así que siempre funcionará». Otro responde: «No hay garantía, pero tras muchas pruebas es muy probable». ¿Qué tipo de razonamiento discuten?", "Inductivo, que ofrece probabilidad y no seguridad", "Deductivo, que ofrece seguridad", "Por reducción al absurdo", "Generalizar desde pruebas pasadas es inducción, y su conclusión es probable."),
    sc=[
        ("En Seminario de filosofía: ¿qué es la inferencia a la mejor explicación?", "Elegir entre varias la explicación que mejor da cuenta de un hecho", "Su conclusión es probable y puede cambiar."),
        ("¿Qué garantía ofrece la deducción válida?", "Si las premisas son verdaderas, la conclusión también", "Es el criterio de validez de un argumento deductivo."),
        ("¿Qué tres criterios sirven para contrastar métodos?", "Seguridad de la conclusión, supuestos y casos en que falla", "Son los criterios de la explicación."),
    ],
    op=("Elige un tema de ejemplo: «los videojuegos distraen del estudio», «hay que leer los libros antes de ver su película» o «la amistad se mantiene mejor en persona». "
        "Escribe un argumento breve para el tema por cada uno de dos métodos distintos (por ejemplo, inductivo y por analogía), nombra el método y di qué tan segura es cada conclusión.",
        "Tema: la amistad se mantiene mejor en persona. Inductivo: en muchas amistades de ejemplo que se mantienen, los amigos se ven seguido; probablemente es lo que ocurre en general (conclusión probable). Analogía: la amistad se parece a una planta que necesita atención diaria; sin contacto se marchita (depende de que la semejanza sea relevante).",
        ["escribe dos argumentos con métodos distintos", "nombra bien cada método", "indica qué tan segura es cada conclusión", "no los confunde con deducciones"],
        ["dos argumentos con su método y su grado de seguridad"],
        ["llamar «deductivo» a cualquier argumento", "afirmar que una inducción es segura", "no explicar la semejanza de una analogía"],
        "Pregunta: «¿qué pasaría si apareciera un caso contrario?». Si la conclusión cae del todo, probablemente era deductiva."),
    reinforce="Escribe un ejemplo propio de argumento deductivo, uno inductivo y uno por analogía sobre la vida escolar, y rotula cada uno.",
    extend="Elige un argumento por analogía que hayas oído y escribe una semejanza relevante y una diferencia relevante entre las cosas comparadas.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (diálogo ficticio). La profesora Íris conversa con Gael en un taller. "
     "Íris: «¿Qué es ser honesto?» Gael: «Ser honesto es decir siempre todo lo que pienso.» "
     "Íris: «A veces tengo sospechas sin pruebas; por ejemplo, creo que un compañero copió. Si las dijera todas, ¿cumpliría tu definición?» Gael: «Sí, si las pienso, tendría que decirlas.» "
     "Íris: «¿Y acusar a alguien sin pruebas te parece justo?» Gael: «No, sería injusto.» "
     "Íris: «Entonces tu definición me obligaría a hacer algo injusto.» Gael: «Entonces mi definición está mal. Ser honesto es decir lo que creo verdadero y tengo razones para creer.»")
build(
    O2, 3, F,
    use="Aprenderé a reconstruir paso a paso un método de razonamiento a partir de un diálogo y a distinguir la refutación de una tesis de su corrección.",
    prior=["Sé qué es la reducción al absurdo.", "Sé definir con rasgos y contraejemplos.", "Sé reconstruir tesis y razones."],
    explain=[
        "Un diálogo filosófico puede contener un método. La refutación por preguntas consiste en examinar una tesis con preguntas que muestran que lleva a consecuencias que quien la sostiene no puede aceptar. Se parece a la reducción al absurdo: se supone provisoriamente una tesis, se deducen consecuencias y se muestra que alguna choca con algo que ya se aceptaba. Si choca, la tesis se rechaza o se corrige.",
        "Para reconstruir el método de un diálogo se identifican los pasos. Primero, la tesis que se examina (la definición de Gael). Segundo, el supuesto provisional (aceptarla por un momento). Tercero, la consecuencia que se deduce (decir toda sospecha sin pruebas). Cuarto, la creencia que choca con ella (acusar sin pruebas es injusto). Quinto, el resultado: la tesis se rechaza o se mejora.",
        "Reconstruir no es lo mismo que estar de acuerdo con el método. Un diálogo así tiene límites: muestra que una tesis es inconsistente con otras creencias de la persona, pero no prueba qué es lo verdadero, y puede depender de qué creencias acepta quien conversa.",
    ],
    vocab=[("refutación por preguntas", "método que examina una tesis con preguntas hasta mostrar consecuencias inaceptables"), ("consecuencia", "lo que se sigue de aceptar una tesis"), ("inconsistencia", "choque entre dos cosas que se aceptan a la vez"), ("tesis provisoria", "tesis que se acepta por un momento para examinar sus consecuencias"), ("corrección de una tesis", "mejora de la tesis a partir de las objeciones")],
    worked=[
        ("Reconstruir los pasos", "Ordena el diálogo de la ficha en cinco pasos.",
         ["Tesis: ser honesto es decir siempre todo lo que se piensa. Supuesto provisional: la acepto por un momento.", "Consecuencia: habría que decir también las sospechas sin pruebas. Choque: acusar sin pruebas es injusto."],
         "Tesis, supuesto provisional, consecuencia, choque con otra creencia y corrección de la definición"),
        ("Qué muestra el método", "¿Qué logra el diálogo respecto de la definición de Gael?",
         ["Muestra una consecuencia que Gael no puede aceptar.", "No prueba por sí solo cuál es la definición verdadera de honestidad."],
         "Muestra que la definición inicial es inconsistente con otra creencia de Gael y lo lleva a corregirla"),
    ],
    mistakes=[("Creer que si el diálogo refuta una definición, la nueva definición ya es verdadera.", "Se confunde mostrar un problema con probar una respuesta.", "Somete también la nueva definición al mismo examen."),
              ("Pensar que la refutación depende de quién conversa mejor y no de las razones.", "Se mira el desempeño y no la estructura del razonamiento.", "Reconstruye los pasos y revisa si la consecuencia realmente se sigue.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué es una consecuencia?", "Lo que se sigue de aceptar una tesis", "La opinión de quien conversa", "Un dato de contexto", "Se deduce de lo que se supone."),
        ("abc", "{F} ¿Qué tesis examina Íris en la ficha?", "La definición de honestidad de Gael", "Que el compañero copió", "Que acusar es justo", "La conversación gira en torno a la definición inicial de Gael."),
        ("abc", "{F} ¿Qué consecuencia saca Íris de la definición de Gael?", "Habría que decir también las sospechas sin pruebas", "Nunca habría que decir nada", "Todos los compañeros copiaron", "Si hay que decir todo lo que se piensa, se deben decir las sospechas."),
        ("abc", "{F} ¿Con qué creencia de Gael choca esa consecuencia?", "Acusar a alguien sin pruebas es injusto", "Un compañero copió", "La honestidad es un valor", "Gael reconoce que sería injusto, y su definición lo obligaría a hacerlo."),
        ("abc", "{F} ¿Cómo termina el diálogo?", "Gael corrige su definición", "Íris acepta la definición inicial", "Gael abandona el taller", "Gael reformula: decir lo que cree verdadero y tiene razones para creer."),
        ("ab", "{F} ¿A qué se parece el método de Íris?", "A la reducción al absurdo", "A la inducción desde muchos casos", "Supone la tesis, deduce una consecuencia inaceptable y la rechaza, igual que la reducción al absurdo."),
        ("abc", "{F} Un estudiante dice: «El diálogo prueba que la definición nueva de Gael es la verdadera». ¿Qué falla?", "Mostrar un problema en la primera definición no prueba que la segunda sea correcta", "Nada: la prueba es completa", "Gael no corrigió su definición", "Para evaluar la nueva definición habría que someterla también a examen."),
        ("abc", "{F} Si Gael hubiera respondido «acusar sin pruebas me parece justo», ¿qué habría ocurrido con el método?", "No habría choque entre la consecuencia y sus creencias, y el argumento no refutaría su definición", "Íris habría probado que la definición es verdadera", "El diálogo habría sido deductivo", "La refutación depende de que la consecuencia choque con algo que la persona acepta."),
        ("abc", "¿Qué límite tiene la refutación por preguntas?", "Depende de las creencias que acepta quien conversa y no prueba qué es verdadero", "Solo se puede usar con números", "Nunca permite corregir una tesis", "Muestra inconsistencia con otras creencias, pero no demuestra por sí misma la respuesta."),
        ("abc", "Aplica el método a esta tesis de ejemplo: «Toda promesa debe cumplirse sin excepción». ¿Qué consecuencia podría examinarse?", "Habría que cumplir una promesa aunque cumplirla causara un daño grave", "Nadie prometería nada", "Las promesas serían inútiles", "Es la consecuencia que puede chocar con la creencia de que no debemos causar daños graves."),
        ("abc", "{F} Una compañera resume: «Íris no discute la definición de Gael, solo se burla de él». ¿Es una buena reconstrucción?", "No: Íris deduce consecuencias de la definición y las compara con creencias de Gael", "Sí: no hay argumento en el diálogo", "Sí: porque Íris es la profesora", "El diálogo tiene pasos de razonamiento y no solo burla."),
        ("abc", "{F} ¿Cuál es el paso en que se muestra el choque?", "Cuando Íris concluye que la definición obligaría a Gael a hacer algo que él mismo reconoció injusto", "Cuando Íris pregunta qué es ser honesto", "Cuando Gael dice «sí» a la primera pregunta", "El choque aparece al contrastar la consecuencia con una creencia aceptada."),
        ("abc", "Dos personas discuten la tesis «es honesto quien nunca se equivoca». ¿Qué primera pregunta usaría el método de Íris?", "¿Qué se seguiría si una persona honesta se equivocara sin querer?", "¿Qué dice el diccionario sobre la palabra «honesto»?", "¿Cuántas personas conoces que nunca se equivocan?", "Busca una consecuencia que choque con la tesis, y no una definición de diccionario ni un recuento de casos."),
    ],
    ctx=("abc", "En un grupo ficticio, Rafa sostiene: «Todo lo que da placer es bueno». Otro le pregunta: «¿Y si alguien disfruta molestando a un compañero?». Rafa responde: «Eso no es bueno». ¿Qué método se está usando?", "Refutación por preguntas: la tesis lleva a una consecuencia que Rafa no acepta", "Inducción desde un solo caso", "Deducción válida desde premisas verdaderas", "Se examina una tesis con una consecuencia que choca con otra creencia."),
    sc=[
        ("En Seminario de filosofía: ¿qué es la refutación por preguntas?", "Examinar una tesis con preguntas hasta mostrar consecuencias inaceptables", "Se parece a la reducción al absurdo en forma dialogada."),
        ("¿Qué pasos tiene la reconstrucción de un diálogo con este método?", "Tesis, supuesto provisional, consecuencia, choque y corrección", "Son los cinco pasos de la explicación."),
        ("¿Qué no prueba una refutación?", "Que la nueva definición sea la verdadera", "Solo muestra una inconsistencia con otras creencias."),
    ],
    op=("Elige una de estas tesis de ejemplo: «ser valiente es no sentir miedo», «un regalo es siempre algo que se da gratis» o «ser amigo es estar de acuerdo con la otra persona». "
        "Escribe un diálogo breve de cinco o seis líneas entre dos personas que use el método de la clase: pide una consecuencia, muestra el choque con otra creencia y corrige la tesis.",
        "Tesis: ser valiente es no sentir miedo. A: ¿Ser valiente es no sentir miedo? B: Sí. A: ¿Una persona que siente mucho miedo pero igual se acerca a ayudar a un amigo es valiente? B: Creo que sí. A: Pero sentía miedo, así que tu tesis diría que no es valiente. B: Entonces mi tesis falla: valiente es actuar bien a pesar del miedo.",
        ["la tesis aparece claramente", "se deduce una consecuencia", "se muestra un choque con otra creencia", "la tesis se corrige"],
        ["diálogo breve con los cinco pasos del método"],
        ["atacar a la persona y no a la tesis", "no deducir ninguna consecuencia", "presentar la corrección como prueba"],
        "Pregunta: «¿dónde está el choque?». Pídele que subraye la consecuencia y la creencia con la que choca."),
    reinforce="Reconstruye el diálogo de la ficha en una tabla de cinco filas: paso y frase de apoyo.",
    extend="Aplica el método a una definición tuya de «amistad» y escribe una consecuencia que te haga corregirla.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (argumentos de ejemplo). "
     "A1 (analogía): «Un liceo funciona como un barco: en el barco debe haber una sola persona al mando para decidir; por lo tanto, el liceo necesita una sola persona que decida todo.» "
     "A2 (generalización): «Entrevisté a 8 estudiantes del 3.º A y todos aprobaron el nuevo horario; por lo tanto, la mayoría de los estudiantes del liceo lo aprueba.» "
     "A3 (mejor explicación): «Las plantas del jardín se secaron la misma semana en que se rompió la llave del riego; la mejor explicación es la falta de agua.»")
build(
    O2, 4, F,
    use="Aprenderé a evaluar con criterios argumentos por analogía, por generalización y por mejor explicación, y a mejorar un argumento débil.",
    prior=["Sé clasificar métodos de razonamiento.", "Sé qué es una objeción.", "Distingo argumento válido de argumento fuerte."],
    explain=[
        "Cada método se evalúa con criterios propios. En una analogía se comparan las semejanzas y las diferencias relevantes para la conclusión: es más fuerte si las cosas se parecen en lo que importa y débil si difieren en lo que importa. En una generalización se mira el tamaño de la muestra, que sea representativa (que incluya variedad del grupo) y si hay casos contrarios. En una inferencia a la mejor explicación se piensa en explicaciones alternativas y se elige la que explica todos los datos con menos supuestos.",
        "Una muestra es la parte del grupo que se examina. Es representativa cuando se parece al grupo completo en lo relevante. Una muestra pequeña o tomada de un solo lugar suele ser débil para generalizar. Un sesgo es una distorsión que hace que la muestra o el razonamiento favorezcan una conclusión sin razón suficiente.",
        "Un argumento débil puede mejorarse: ampliar y variar la muestra, buscar más semejanzas relevantes o descartar explicaciones alternativas. Evaluar no es solo decir «es débil»: es indicar qué falla y cómo se podría fortalecer.",
    ],
    vocab=[("semejanza relevante", "parecido que importa para la conclusión de una analogía"), ("diferencia relevante", "diferencia que debilita la conclusión de una analogía"), ("muestra", "parte del grupo que se examina"), ("muestra representativa", "muestra que se parece al grupo completo en lo relevante"), ("sesgo", "distorsión que favorece una conclusión sin razón suficiente"), ("explicación alternativa", "otra explicación posible del mismo hecho")],
    worked=[
        ("Evaluar una generalización", "Evalúa A2 de la ficha.",
         ["Tamaño: 8 estudiantes es poco comparado con todo el liceo.", "Representatividad: todos son de un solo curso, y no aparece nadie de los otros cursos."],
         "Es débil: muestra pequeña y de un solo curso, no representativa"),
        ("Fortalecer un argumento", "¿Cómo se podría fortalecer A3?",
         ["Busco explicaciones alternativas: calor extremo, plaga, falta de abono.", "Reviso si la falta de agua explica los datos mejor: dato extra, el agua estaba cortada solo en el jardín."],
         "Descartando las explicaciones alternativas con datos y mostrando que la falta de agua explica todos los datos"),
    ],
    mistakes=[("Decir «es débil» sin indicar qué criterio falla.", "Se emite un juicio sin mostrar su razón.", "Nombra el criterio (muestra, semejanza relevante, alternativas) y explica qué falla."),
              ("Aceptar una analogía solo porque hay muchas semejanzas.", "Se cuentan semejanzas sin ver si importan para la conclusión.", "Pregunta si las semejanzas y las diferencias son relevantes para lo que se concluye.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿cuándo una muestra es representativa?", "Cuando se parece al grupo completo en lo relevante", "Cuando es la más fácil de conseguir", "Cuando todos opinan lo mismo", "Representativa significa que refleja la variedad relevante del grupo."),
        ("abc", "¿Qué se compara en una analogía para evaluarla?", "Semejanzas y diferencias relevantes para la conclusión", "Cuántas palabras tiene cada elemento", "Cuál de las dos cosas es más conocida", "Lo que importa es si las cosas se parecen en lo que sustenta la conclusión."),
        ("abc", "{F} ¿Qué dato de A2 hace dudar más de que represente a todo el liceo?", "Que todos los entrevistados sean del mismo curso", "Que los 8 entrevistados estuvieran de acuerdo", "Que el horario sea nuevo", "Un solo curso puede no reflejar a los demás; que coincidan en opinión no es una falla."),
        ("abc", "{F} ¿Qué diferencia relevante debilita A1?", "Un liceo reúne a muchas personas con tareas distintas y no solo una situación de mando en una emergencia", "Que un barco flota", "Que el liceo tiene sala de profesores", "La conclusión (una sola persona decide todo) no calza con la complejidad del liceo."),
        ("abc", "{F} ¿Cuál es una explicación alternativa a A3?", "Una ola de calor que secó las plantas la misma semana", "Que el jardín es grande", "Que la llave es de metal", "Es otra causa posible del mismo hecho."),
        ("ab", "{F} Si se entrevistaran 80 estudiantes de todos los cursos y la mayoría aprobara el horario, ¿qué ocurriría con A2?", "Se fortalecería, porque la muestra es mayor y más variada", "Quedaría igual de débil", "Mejoran tamaño y variedad, que son los criterios de una buena generalización."),
        ("abc", "Un estudiante dice: «Pregunté a mis cinco mejores amigos y todos prefieren las clases por la tarde, así que la mayoría del liceo las prefiere». ¿Qué problema principal tiene?", "Muestra pequeña y sesgada, porque son personas muy parecidas entre sí", "Es una deducción inválida", "Es una analogía débil", "La muestra tiene poca variedad: sus amigos pueden compartir gustos."),
        ("abc", "{F} Alguien propone fortalecer A1 así: «Un barco y un liceo se parecen en que ambos tienen personas». ¿Qué falla en esa mejora?", "Es una semejanza irrelevante para concluir que una sola persona deba decidir todo", "Es una diferencia relevante", "Es una muestra representativa", "Una semejanza debe sostener la conclusión, no ser solo un rasgo común cualquiera."),
        ("abc", "{F} Un dato dice que el jardín del vecino, con riego normal, también se secó esa semana. ¿Qué efecto tiene en A3?", "Debilita la explicación de la llave rota y sugiere otras causas", "La fortalece, porque se secó otro jardín", "La vuelve deductiva", "Si el hecho ocurre sin esa causa, la explicación pierde fuerza."),
        ("abc", "Dos explicaciones dan cuenta de los mismos datos, pero una necesita más supuestos. ¿Cuál conviene según la explicación?", "La que explica todos los datos con menos supuestos", "La más complicada, porque parece más completa", "La que dice la persona con mayor edad", "Entre explicaciones equivalentes, se prefiere la que supone menos."),
        ("abc", "Alguien evalúa un argumento diciendo solo «es débil». ¿Qué le falta?", "Indicar qué criterio falla y cómo mejorarlo", "Decir si le agrada la conclusión", "Citar a una persona conocida", "Evaluar es mostrar la razón del juicio."),
        ("abc", "{F} Para fortalecer A2, ¿cuál es la mejor medida?", "Entrevistar a estudiantes de todos los cursos, elegidos al azar", "Entrevistar a otros ocho del 3.º A", "Preguntar solo a quienes ya aprobaron", "Aumentar y variar la muestra es el camino indicado."),
        ("abc", "Un argumento por analogía compara a los estudiantes con una orquesta: «cada uno debe tocar lo mismo, o sonará mal». ¿Qué pregunta ayuda más a evaluarlo?", "¿Qué diferencias hay entre aprender y tocar juntos una partitura?", "¿Cuántos instrumentos hay en una orquesta?", "¿Quién dirigió la orquesta?", "Hay que ver si las diferencias relevantes debilitan la conclusión."),
    ],
    ctx=("abc", "En un taller ficticio se discute si conviene prohibir los celulares en la sala. Un estudiante argumenta: «Con la nueva norma de un curso, el 90 % de las notas subió; por lo tanto, prohibirlos mejora las notas en todo el liceo». ¿Qué criterio falla más?", "Que un solo curso no es una muestra representativa del liceo", "Que usa números", "Que habla de celulares", "Se generaliza desde un solo caso que puede no representar al resto."),
    sc=[
        ("En Seminario de filosofía: ¿qué es un sesgo en una muestra?", "Una distorsión que favorece una conclusión sin razón suficiente", "Hace que la muestra no represente al grupo."),
        ("¿Qué criterios evalúan una generalización?", "Tamaño, representatividad y casos contrarios", "Son los tres criterios de la explicación."),
        ("En Seminario de filosofía: ¿Qué es una explicación alternativa?", "Otra explicación posible del mismo hecho", "Hay que descartarlas para fortalecer una inferencia a la mejor explicación."),
    ],
    op=("Elige uno de estos argumentos de ejemplo. Opción 1: «Todos mis vecinos que tienen perro son simpáticos, así que las personas con perro son simpáticas». Opción 2: «El cerebro es como un computador: ambos procesan información; por lo tanto, el cerebro funciona con programas». Opción 3: «Hoy hay muchos jóvenes cansados; la mejor explicación es que las clases empiezan temprano». "
        "Evalúalo con los criterios de la clase (indica cuál) y propón una forma de fortalecerlo.",
        "Opción 1. Criterio: muestra. Los vecinos son pocos y de un solo barrio; la muestra es pequeña y poco variada. Mejora: preguntar a personas de distintos barrios y edades, y buscar casos de personas con perro que no sean simpáticas.",
        ["nombra el criterio que usa", "explica qué falla con una razón", "propone una mejora concreta", "no se limita a decir «es débil»"],
        ["evaluación con criterio y una propuesta de mejora"],
        ["decir «es débil» sin explicar", "aplicar el criterio de otro método", "proponer una mejora que no corrige la falla"],
        "Pregunta: «¿qué criterio de los tres estás usando?». Pídele que lo nombre y diga qué dato lo cumple o no."),
    reinforce="Escribe una analogía propia y una semejanza relevante y una diferencia relevante entre las cosas comparadas.",
    extend="Elige una creencia popular («el que madruga…») y analiza si se basa en una generalización, una analogía o una explicación, y qué criterio falla.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 5 (objeciones y respuestas de ejemplo). Tesis: «Los experimentos mentales sirven para aclarar conceptos filosóficos.» "
     "Objeción 1: «Imaginan casos imposibles, así que no nos dicen nada de la vida real.» "
     "Objeción 2: «Cada persona imagina el caso a su manera y llega a conclusiones distintas.» "
     "Respuesta a la objeción 1 (R1): «Lo que importa no es que el caso ocurra, sino qué muestra sobre lo que sostiene un concepto; un caso imposible puede aclarar una consecuencia que un concepto tiene.» "
     "Respuesta a la objeción 2 (R2): «Eso es cierto, y por eso conviene dar los detalles del caso y comparar las conclusiones; el desacuerdo, una vez expuesto, también sirve para discutir.»")
build(
    O2, 5, F,
    use="Aprenderé a responder objeciones a un método de razonamiento con una respuesta bien construida y a contrastar métodos con sus fortalezas y límites.",
    prior=["Sé qué es una objeción.", "Sé evaluar un argumento con criterios.", "Sé qué es un experimento mental."],
    explain=[
        "Una objeción es una razón en contra de una tesis, de una premisa o de un método. Responderla bien supone entenderla primero con caridad y luego elegir una estrategia. Se puede negar una premisa de la objeción y mostrar por qué es falsa o dudosa. Se puede distinguir dos sentidos de una palabra y mostrar que la objeción solo vale en uno. Se puede aceptar la objeción en parte y limitar el alcance de la tesis. O se puede ofrecer un contraejemplo.",
        "Una respuesta es mala si cambia de tema, si repite la tesis sin razones o si ataca a quien objeta. Una respuesta es buena si responde exactamente a la objeción, entrega una razón y reconoce lo que concede. En la ficha, R1 niega una premisa que la objeción da por supuesta (que un caso debe ocurrir para decir algo) y señala qué importa de verdad (qué muestra el caso), y R2 acepta la objeción en parte y limita el método.",
        "Contrastar métodos es poner sus fortalezas y límites lado a lado. La deducción da seguridad, pero no aporta información nueva. La inducción amplía el conocimiento, pero con riesgo. El experimento mental aclara conceptos, pero depende de cómo se imagine el caso. El mejor uso de un método es el que respeta su límite.",
    ],
    vocab=[("estrategia de respuesta", "forma de contestar una objeción: negar, distinguir, conceder en parte o dar un contraejemplo"), ("distinguir", "separar dos sentidos de una palabra o dos aspectos de una idea"), ("conceder", "aceptar parte de una objeción"), ("contraejemplo", "caso que muestra que una afirmación general es falsa"), ("alcance", "hasta dónde vale una tesis o un método")],
    worked=[
        ("Identificar la estrategia", "¿Qué estrategia usa R2 de la ficha?",
         ["R2 empieza reconociendo que la objeción es cierta: «Eso es cierto».", "Luego propone una forma de limitar el problema: dar los detalles del caso y comparar."],
         "Concede en parte y limita el alcance del método"),
        ("Evaluar una respuesta", "Alguien responde a la objeción 1: «Los experimentos mentales son buenos porque son útiles». ¿Es una buena respuesta?",
         ["Veo si responde a la objeción: no explica por qué un caso imposible dice algo de la vida real.", "Repite la tesis sin dar una razón nueva."],
         "No: repite la tesis sin responder la objeción"),
    ],
    mistakes=[("Responder a una objeción repitiendo la tesis con más fuerza.", "Se sustituye una razón por insistencia.", "Ofrece una razón nueva o muestra qué premisa de la objeción falla."),
              ("Rechazar una objeción sin entenderla y deformarla.", "Se responde a una versión débil, no a la que se planteó.", "Reformula la objeción en su versión más fuerte antes de contestar.")],
    T=[
        ("abc", "En Seminario de filosofía, ¿qué hace una respuesta que «concede en parte»?", "Acepta parte de la objeción y limita el alcance de la tesis", "Niega toda la objeción", "Cambia de tema", "Reconoce lo que la objeción tiene de razón y ajusta la tesis."),
        ("abc", "{F} ¿Qué estrategia usa R1?", "Niega la premisa que la objeción supone (que el caso deba ocurrir) y señala qué importa del caso", "Ataca a quien objeta", "Repite la tesis", "Muestra que la objeción descansa en una premisa dudosa: lo que importa es lo que el caso muestra."),
        ("abc", "{F} ¿Qué parte de la objeción 2 reconoce R2 como cierta?", "Que cada persona puede imaginar el caso de manera distinta", "Que los experimentos mentales sean inútiles", "Que el caso deba ocurrir en la realidad", "R2 empieza con «Eso es cierto» y se refiere a las imaginaciones distintas."),
        ("abc", "¿Cuál es una respuesta mala a una objeción?", "Cambiar de tema o repetir la tesis sin razones", "Dar un contraejemplo", "Distinguir dos sentidos de una palabra", "Una respuesta debe contestar a la objeción con razones."),
        ("abc", "Alguien responde a la objeción 2: «No hay que escucharla porque quien la dice no sabe filosofía». ¿Qué error comete?", "Ataca a la persona en vez de responder a la razón", "Distingue dos sentidos", "Concede en parte", "No responde a la objeción: descalifica a quien la plantea."),
        ("ab", "{F} Frente a la objeción 1, ¿cuál es mejor respuesta?", "R1, porque explica por qué un caso imposible puede aclarar un concepto", "«Los experimentos son útiles porque lo dicen muchos»", "R1 contesta con una razón; la otra opción apela a la cantidad y no al fundamento."),
        ("abc", "Una objeción a la inducción dice: «No hay garantía de que el futuro sea como el pasado». ¿Qué respuesta concede en parte?", "Es cierto que no hay garantía, pero la inducción da conclusiones probables que se pueden revisar", "La inducción siempre es segura", "Nadie debería usarla jamás", "Reconoce el límite de la objeción y precisa el alcance del método."),
        ("abc", "Una objeción dice: «La deducción no enseña nada nuevo». ¿Qué respuesta distingue dos sentidos de «nuevo»?", "No agrega información a las premisas, pero puede mostrar consecuencias que no se veían a simple vista", "Siempre agrega datos nuevos", "La objeción es falsa porque las premisas son verdaderas", "Separa dos sentidos de «nuevo» y mantiene la parte verdadera de la objeción."),
        ("abc", "{F} ¿Qué contraejemplo serviría contra la afirmación «un caso imposible nunca dice nada de la vida real»?", "Un caso imposible, como una persona que de pronto se duplica en dos idénticas, y que nos hace ver qué rasgos importan para seguir siendo la misma persona", "Un caso posible de una persona que llega tarde a clases", "Un caso imposible que nadie logra entender", "Un contraejemplo muestra que la afirmación general falla en al menos un caso."),
        ("abc", "{F} Una compañera dice: «R2 admite que la objeción 2 es cierta, así que fracasó». ¿Qué responde mejor?", "Concede en parte, pero propone cómo limitar el problema; no se rinde", "Tiene razón: conceder siempre es perder", "R2 no responde a nada", "Conceder una parte y ajustar el alcance es una estrategia legítima."),
        ("abc", "Al contrastar deducción e inducción, ¿qué afirmación es correcta?", "La deducción da seguridad sin ampliar lo que ya está en las premisas; la inducción amplía con riesgo", "La inducción es siempre mejor porque amplía", "Ambas dan seguridad total", "Cada método tiene una fortaleza y un límite propios."),
        ("abc", "{F} Si las personas imaginaran el caso con los mismos detalles, ¿qué ocurriría con la objeción 2?", "Se debilitaría, porque el desacuerdo dependía de detalles distintos", "Se fortalecería", "Desaparecería la tesis", "Fijar los detalles reduce la fuente de desacuerdo que la objeción señalaba."),
        ("abc", "Al responder una objeción, ¿qué se hace primero según la explicación?", "Entenderla con caridad y reformularla en su versión más fuerte", "Contestar lo antes posible", "Buscar a quién se la oyó decir", "Una buena respuesta contesta a la objeción real, no a una versión débil."),
    ],
    ctx=("abc", "Un estudiante ficticio dice: «Imaginar casos no sirve, porque cada persona imagina algo distinto». Otro responde: «Eso pasa si no se detalla el caso; si lo escribimos con todos sus datos, es más fácil discutir». ¿Qué estrategia usa el segundo?", "Concede en parte y limita el problema con una precisión", "Ataca a la persona", "Repite su tesis sin razones", "Reconoce la dificultad y ofrece una forma de reducirla."),
    sc=[
        ("En Seminario de filosofía: ¿qué es conceder en parte?", "Aceptar parte de una objeción y ajustar el alcance de la tesis", "Es una estrategia legítima de respuesta."),
        ("¿Cuáles son cuatro estrategias para responder una objeción?", "Negar una premisa, distinguir, conceder en parte y dar un contraejemplo", "Son las cuatro estrategias de la explicación."),
        ("¿Por qué repetir la tesis no responde a una objeción?", "Porque no ofrece una razón nueva", "Una respuesta necesita razones que respondan a la objeción."),
    ],
    op=("Elige un método de la unidad (deducción, inducción, analogía, mejor explicación o experimento mental). Escribe: una objeción fuerte contra ese método, una respuesta con una de las cuatro estrategias, y qué límite del método reconoces que queda en pie.",
        "Método: analogía. Objeción: «Dos cosas nunca son iguales, así que toda analogía falla». Respuesta (distinguir): no se pide igualdad total, sino parecido en lo relevante para la conclusión. Límite: una analogía es más débil cuando hay diferencias relevantes que no se han considerado.",
        ["formula una objeción real y no una caricatura", "usa una estrategia nombrada", "responde exactamente a la objeción", "reconoce un límite que subsiste"],
        ["objeción, respuesta con estrategia y límite reconocido"],
        ["responder con otra tesis", "no nombrar la estrategia", "decir que el método no tiene límites"],
        "Pregunta: «¿tu respuesta contesta justo lo que la objeción dice?». Si no, pídele que reescriba la objeción en una frase y vuelva a responder."),
    reinforce="Escribe una objeción a la deducción y dos formas distintas de responderla.",
    extend="Haz una tabla de cinco filas con un método, su fortaleza y su límite, y escribe en qué tipo de problema usarías cada uno.",
)
