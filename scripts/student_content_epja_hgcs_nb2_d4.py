"""Historia, Geografía y Ciencias Sociales EPJA Básica N2, módulo 4 (parte 4): OAD-16, relacionar mediante un conversatorio los Derechos Humanos con el funcionamiento de la democracia y los deberes del Estado, comunicándose con claridad. Los conversatorios se simulan por escrito; datos de ejemplo rotulados."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz y goma. Todo se resuelve con lo escrito en la ficha: los guiones de conversatorio y las situaciones son de ejemplo. Si lo deseas, puedes leer las intervenciones en voz alta con otra persona."
build = make_build(MATERIALS)

O = "EPJA-HGCS-NB2-OAD-16"
PRIOR = ["Ya conversé en reuniones, filas o grupos y sé que cada persona tiene algo que aportar.", "Conozco algunas ideas sobre derechos, deberes del Estado y democracia."]


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    build(O, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ====================================================== clase 1
F = ("Ficha 1 (conversatorio de ejemplo sobre «¿Por qué importa que todas las personas puedan opinar?»). Reglas del conversatorio: 1) hablar por turnos; 2) escuchar sin interrumpir; "
     "3) dar una razón; 4) respetar a quien piensa distinto; 5) hablar de ideas y no de las personas. "
     "Intervención de Marta (nombre de ejemplo): «Importa porque así los problemas del barrio se conocen». "
     "Intervención de Luis (nombre de ejemplo): «Estoy de acuerdo con Marta, y agrego que opinar es un derecho que protege la democracia». "
     "Intervención de Rosa (nombre de ejemplo): «Eso es una tontería».")
K(1, F,
  "Hoy reconozco qué es un conversatorio, qué reglas tiene y cómo se relacionan los derechos humanos con la vida en democracia en una conversación.",
  ["Un conversatorio es una conversación organizada en la que varias personas comparten ideas sobre un tema. No se trata de ganar, sino de entender distintas miradas. Tú ya has conversado en reuniones, en la fila o en un grupo, y lo hacías con tu manera de hablar.",
   "Tiene reglas simples: hablar por turnos, escuchar sin interrumpir, dar una razón de lo que se dice, respetar a quien piensa distinto y hablar de ideas, no de las personas. Estas reglas son también parte de una actitud democrática.",
   "Hoy relacionamos dos ideas: opinar es un derecho humano, y la democracia lo protege cuando existen espacios donde todas las personas pueden hablar. Para comunicarte con claridad, di primero tu idea, después la razón y, si puedes, un ejemplo breve."],
  [("conversatorio", "conversación organizada en que varias personas comparten ideas sobre un tema"), ("turno", "momento que le toca hablar a cada persona"), ("razón", "motivo que explica por qué se piensa algo"), ("actitud democrática", "forma de actuar que respeta las ideas y los derechos de las demás personas")],
  [("Reconocer una regla", "Una persona espera su turno para hablar. ¿Qué regla cumple?", ["Espera sin interrumpir.", "Esa es la regla de turnos."], "Hablar por turnos"),
   ("Dar una razón", "Idea: «Hay que escuchar a todas las personas». ¿Cuál es una razón?", ["Una razón explica por qué.", "Cada persona conoce problemas distintos."], "Porque cada persona conoce problemas distintos")],
  [("Interrumpir para defender mi idea más rápido.", "Se cree que quien habla más gana.", "Espera el turno y escucha primero."),
   ("Criticar a la persona en vez de su idea.", "Se confunde a la persona con lo que dice.", "Responde a la idea con una razón.")],
  [("abc", "{F} ¿Cuántas reglas tiene el conversatorio de la ficha?", "5", "3", "7", "La ficha del conversatorio numera cinco reglas."),
   ("abc", "{F} ¿Qué intervención no cumple las reglas de respeto?", "La de Rosa", "La de Marta", "La de Luis", "Rosa califica una idea de tontería sin dar razón, lo que no respeta a quien piensa distinto."),
   ("ab", "{F} ¿Marta da una razón de su idea?", "Sí, dice que así los problemas del barrio se conocen", "No, solo opina", "Marta explica por qué importa opinar."),
   ("abc", "{F} ¿Qué agrega Luis a lo dicho por Marta?", "Que opinar es un derecho que protege la democracia", "Que nadie debe opinar", "Que las reglas no sirven", "Relaciona un derecho con la democracia."),
   ("abc", "¿Qué relación muestra Luis entre derechos humanos y democracia?", "La democracia protege el derecho a opinar", "Opinar prohíbe la democracia", "No hay ninguna relación", "El derecho a opinar se protege en una democracia con espacios para hablar."),
   ("abc", "En un conversatorio, ¿qué hace una persona que respeta el turno?", "Espera a que la otra termine antes de hablar", "Habla al mismo tiempo", "Se va sin decir nada", "Respetar el turno es dejar terminar a quien habla."),
   ("ab", "Una persona critica el aspecto de quien habla en vez de su idea. ¿Qué regla incumple?", "Hablar de ideas y no de las personas", "Hablar por turnos", "Centrarse en la persona deja de lado lo que se dice."),
   ("abc", "¿Cuál es la mejor forma de ordenar una intervención clara?", "Idea, razón y ejemplo breve", "Ejemplo, silencio y queja", "Gritar y repetir", "Ordena lo que se afirma, por qué y con qué caso."),
   ("abc", "Un conversatorio termina sin que todas las personas coincidan. ¿Qué indica?", "Que se pudieron compartir ideas distintas con respeto", "Que fracasó siempre", "Que alguien ganó", "El objetivo es entender miradas diferentes, no vencer."),
   ("abc", "Una vecina dice «no hablaré porque nadie me escucha». ¿Qué regla ayudaría a que hable?", "Escuchar sin interrumpir y dar turnos a todas las personas", "Hablar más fuerte", "Cortar a los demás", "Dar turno y escuchar protege el derecho a opinar."),
   ("ab", "Si en el conversatorio se impide hablar a una persona por su origen, ¿qué derecho se afecta?", "La igualdad y el derecho a opinar", "El derecho a viajar", "Se limita la voz de una persona por una característica suya."),
   ("abc", "¿Qué frase relaciona bien un derecho con la democracia?", "«Votar es un derecho que permite elegir a las autoridades»", "«Votar es obligatorio gritar»", "«La democracia no existe»", "Une el derecho de participar con la elección de autoridades."),
   ("abc", "Un moderador da cuatro minutos a cada persona. ¿Por qué sirve este orden?", "Porque todas pueden hablar con tiempo similar", "Porque solo habla el moderador", "Porque se evita escuchar", "Distribuir el tiempo garantiza participación pareja.")],
  ("abc", "En una reunión de una organización comunitaria se acuerda dar tres minutos a cada persona. Una vecina propone respetar ese orden. ¿Qué actitud cívica muestra?", "Cuidar que todas las personas puedan expresarse", "Evitar que alguien opine", "Hablar sin límite", "Garantizar turnos protege la participación de todas."),
  [("En Historia: ¿qué es un conversatorio?", "Conversación organizada en que varias personas comparten ideas sobre un tema", "Busca entender distintas miradas sobre un mismo tema."),
   ("En un conversatorio sobre derechos, ¿qué es una razón?", "Motivo que explica por qué se piensa algo", "Una razón hace más claro y sólido un argumento."),
   ("¿Qué derecho se ejerce al opinar?", "La libertad de expresión", "Permite compartir ideas sin ser silenciado.")],
  ("Imagina este conversatorio de ejemplo sobre «¿Por qué es importante votar?». Escribe tu aporte en tres líneas: una idea, una razón y un ejemplo breve. Debe relacionar el voto con un derecho humano o con el funcionamiento de la democracia, y usar un lenguaje respetuoso.",
   "Idea: votar permite elegir autoridades. Razón: así las personas participan en las decisiones. Ejemplo: en una junta de vecinos, votar permite elegir una directiva.",
   ["tiene idea, razón y ejemplo", "relaciona con derecho o democracia", "lenguaje respetuoso"],
   ["tres líneas escritas o una intervención leída en voz alta"],
   ["opinión sin razón", "frases irrespetuosas"],
   "Pregunta: «¿Se entiende qué pienso, por qué y con qué caso?»."),
  "Lee en voz alta tu aporte y cuenta cuánto dura.",
  "Escribe una pregunta para iniciar un conversatorio sobre derechos en tu comunidad.")

# ====================================================== clase 2
F = ("Ficha 2 (glosario de ejemplo). Estado de Derecho: situación en que las personas y las autoridades se rigen por leyes conocidas y los poderes del Estado tienen límites. "
     "Ley: norma obligatoria aprobada según un procedimiento. Igualdad ante la ley: todas las personas deben ser tratadas por igual por las leyes. "
     "Justicia: dar a cada persona lo que le corresponde con reglas justas. Libertad de expresión: derecho a expresar ideas sin censura previa, respetando a las demás personas. "
     "Frases de ejemplo: A) «Una autoridad no puede aplicar una sanción que la ley no establece». B) «Una persona con poder tiene un trato especial ante un tribunal». "
     "C) «Toda persona puede pedir ser escuchada por un tribunal». D) «Un periódico publica la opinión de una vecina».")
K(2, F,
  "Hoy aprendo las palabras clave para conversar sobre derechos y democracia: Estado de Derecho, ley, igualdad ante la ley, justicia y libertad de expresión.",
  ["Un Estado de Derecho es aquel en que las personas y las autoridades se rigen por leyes conocidas. Nadie está sobre la ley y el poder tiene límites. Es una base de la democracia, porque protege los derechos de las personas frente a abusos.",
   "La ley es una norma obligatoria que se aprueba según un procedimiento. La igualdad ante la ley dice que todas las personas deben ser tratadas por igual. La justicia busca dar a cada persona lo que le corresponde con reglas justas, y los tribunales la aplican.",
   "La libertad de expresión es el derecho a expresar ideas sin censura previa, respetando a las demás personas. Para un conversatorio, estas palabras permiten explicar con precisión cómo los derechos humanos y la democracia se apoyan mutuamente."],
  [("Estado de Derecho", "situación en que personas y autoridades se rigen por leyes conocidas y el poder tiene límites"), ("ley", "norma obligatoria aprobada según un procedimiento"), ("igualdad ante la ley", "todas las personas deben ser tratadas por igual por las leyes"), ("libertad de expresión", "derecho a expresar ideas sin censura previa, respetando a las demás personas")],
  [("Reconocer el Estado de Derecho", "Una autoridad solo puede sancionar según lo que dice la ley. ¿Qué principio se cumple?", ["La autoridad está sujeta a la ley.", "Eso limita el poder."], "El Estado de Derecho"),
   ("Reconocer la igualdad ante la ley", "Dos personas cometen la misma falta y reciben el mismo trato legal. ¿Qué principio se cumple?", ["Ambas son tratadas igual.", "Eso es igualdad ante la ley."], "Igualdad ante la ley")],
  [("Creer que la ley sirve solo para quienes tienen menos poder.", "Se olvida que el Estado de Derecho rige para todas las personas y autoridades.", "Nadie está sobre la ley."),
   ("Pensar que la libertad de expresión permite insultar.", "Se confunde expresar ideas con dañar a otra persona.", "Se puede opinar respetando a las demás personas.")],
  [("abc", "{F} ¿Cuántas frases de ejemplo trae la ficha?", "cuatro", "tres", "seis", "La ficha trae las frases A, B, C y D."),
   ("abc", "{F} ¿Qué frase contradice la igualdad ante la ley?", "B, el trato especial para una persona con poder", "C, pedir ser escuchado", "A, no aplicar sanciones sin ley", "Dar trato especial por poder rompe la igualdad."),
   ("ab", "{F} ¿Qué derecho se ejerce en la frase D?", "La libertad de expresión", "El derecho a la salud", "Un periódico publica una opinión, lo que permite expresar ideas."),
   ("abc", "{F} ¿Qué frase muestra el derecho a ser escuchado por la justicia?", "C", "A", "D", "Pedir ser escuchado por un tribunal es acceder a la justicia."),
   ("abc", "¿Qué significa que el poder tiene límites?", "Que las autoridades deben respetar la ley", "Que las autoridades hacen lo que quieran", "Que no hay leyes", "Ningún poder está sobre la ley."),
   ("abc", "¿Quién aplica la justicia, según esta clase?", "Los tribunales", "Los vecinos", "Los periódicos", "Los tribunales resuelven conflictos aplicando las leyes."),
   ("ab", "¿Qué protege la libertad de expresión?", "La posibilidad de expresar ideas respetando a otros", "La posibilidad de insultar", "Expresar ideas no implica agredir a nadie."),
   ("abc", "Una persona dice: «Soy autoridad, así que la ley no se aplica a mí». ¿Qué principio contradice?", "El Estado de Derecho", "El derecho a la salud", "El derecho a la vivienda", "En un Estado de Derecho las autoridades también se rigen por la ley."),
   ("abc", "{F} Si juntas el Estado de Derecho y la igualdad ante la ley, ¿qué resultado esperas?", "Que las personas sean tratadas con reglas iguales y conocidas", "Que algunas personas queden sin reglas", "Que las leyes cambien cada día sin aviso", "Ambos principios dan seguridad y trato parejo."),
   ("abc", "¿Por qué el Estado de Derecho es una base de la democracia?", "Porque protege los derechos frente a los abusos", "Porque evita que haya elecciones", "Porque quita derechos a algunas personas", "Los límites al poder cuidan a las personas."),
   ("abc", "Una persona publica una opinión respetuosa sobre el servicio de un consultorio. ¿Qué derecho ejerce?", "La libertad de expresión", "El derecho a no ser escuchada", "El derecho a la discriminación", "Expresar ideas respetuosas es ejercer ese derecho."),
   ("ab", "Una persona dice que toda opinión, incluso un insulto, está protegida sin límite. ¿Es correcto?", "No, se debe expresar respetando a las demás personas", "Sí, no hay límites", "La libertad de expresión convive con el respeto a los derechos ajenos."),
   ("abc", "¿Cuál es un ejemplo de ley, según la ficha?", "Una norma obligatoria aprobada según un procedimiento", "Una opinión de un vecino", "Un afiche sin autor", "Se aprueba con un procedimiento y obliga a todas las personas.")],
  ("abc", "En una reunión, una dirigente dice: «las reglas del grupo valen para todas las personas, incluida la directiva». ¿Qué principio expresa?", "Un principio parecido al Estado de Derecho: nadie está sobre las reglas", "Que la directiva no tiene reglas", "Que algunos pueden saltarse los turnos", "Aplica las mismas reglas a quien dirige y a quienes participan."),
  [("En Historia: ¿qué es el Estado de Derecho?", "Situación en que personas y autoridades se rigen por leyes y el poder tiene límites", "El Estado de Derecho protege a las personas contra abusos."),
   ("¿Qué es la igualdad ante la ley?", "Que todas las personas sean tratadas por igual por las leyes", "No hay trato especial por poder."),
   ("¿Qué es la libertad de expresión?", "Derecho a expresar ideas sin censura previa, respetando a las demás personas", "Permite opinar con respeto y sin agredir a nadie.")],
  ("Con las frases A a D de la ficha, haz una tabla con dos columnas: «Se cumple un principio democrático» y «No se cumple». Ubica cada frase y escribe una razón corta por cada ubicación.",
   "Se cumple: A, C y D. No se cumple: B, porque da trato especial por poder.",
   ["ubica las cuatro frases", "da una razón corta por cada una", "usa palabras del glosario"],
   ["tabla de dos columnas con razones"],
   ["no dar razón", "confundir libertad de expresión con insultar"],
   "Pregunta: «¿Aquí todas las personas siguen las mismas reglas?»."),
  "Escribe una frase con Estado de Derecho y otra con igualdad ante la ley.",
  "Explica con tus palabras por qué la ley limita el poder de las autoridades.")

# ====================================================== clase 3
F = ("Ficha 3 (cómo relacionar un derecho con la democracia y el Estado, pasos de ejemplo). "
     "Paso 1: nombrar el derecho. Paso 2: explicar cómo lo protege la democracia (por ejemplo con elecciones, participación y leyes). "
     "Paso 3: decir qué debe hacer el Estado. Paso 4: decir qué podemos hacer las personas. "
     "Modelo para el derecho a la educación: «La educación es un derecho (paso 1). En una democracia, las leyes y la participación permiten exigirlo (paso 2). El Estado debe ofrecer escuelas y apoyo para estudiar (paso 3). Las personas podemos asistir y respetar a quienes enseñan y aprenden (paso 4)». "
     "Plantilla: «[derecho] es un derecho porque ___; en democracia se protege con ___; el Estado debe ___; las personas podemos ___».")
K(3, F,
  "Hoy aprendo, paso a paso, a relacionar un derecho humano con el funcionamiento de la democracia, los deberes del Estado y nuestras responsabilidades.",
  ["Relacionar significa mostrar cómo dos ideas se conectan. Para conversar con claridad usaremos cuatro pasos: nombrar un derecho, explicar cómo lo protege la democracia, decir qué debe hacer el Estado y mencionar qué podemos hacer las personas.",
   "Un modelo es el derecho a la educación: es un derecho, las leyes y la participación permiten exigirlo, el Estado debe ofrecer escuelas y apoyo, y las personas podemos asistir y respetar a quienes enseñan y aprenden. Cada paso responde a una pregunta distinta.",
   "Usar una plantilla ayuda a ordenar la intervención. Después puedes agregar un ejemplo breve y escuchar lo que dicen otras personas. Si alguien aporta un dato, pide la fuente. Así tu conversación será clara, razonada y respetuosa."],
  [("relacionar", "mostrar cómo dos ideas se conectan"), ("plantilla", "esquema con espacios para completar"), ("intervención", "lo que dice una persona durante su turno en una conversación"), ("ejemplo", "caso concreto que ayuda a entender una idea")],
  [("Nombrar el derecho", "Una persona dice «poder ir al consultorio cuando me enfermo». ¿Qué derecho es?", ["Habla de atenderse cuando hay enfermedad.", "Eso es el derecho a la salud."], "El derecho a la salud"),
   ("Completar la plantilla", "Derecho: expresar opiniones. ¿Qué podemos hacer las personas, paso 4?", ["Pienso en una conducta respetuosa.", "Escuchar a quienes piensan distinto."], "Escuchar y opinar con respeto")],
  [("Saltarse pasos y solo decir «es un derecho».", "No se explica cómo se protege ni qué deben hacer el Estado y las personas.", "Usa los cuatro pasos."),
   ("Culpar al Estado de todo y olvidar lo que podemos hacer las personas.", "Se deja fuera el paso 4.", "Menciona también las responsabilidades personales.")],
  [("abc", "{F} ¿Cuántos pasos tiene la forma de relacionar de la ficha?", "4", "2", "6", "La ficha del modelo numera cuatro pasos en total."),
   ("abc", "{F} ¿Qué se hace en el paso 3?", "Decir qué debe hacer el Estado", "Nombrar un color", "Elegir un título", "El paso 3 es el deber del Estado."),
   ("abc", "{F} En el modelo, ¿qué debe hacer el Estado respecto de la educación?", "Ofrecer escuelas y apoyo para estudiar", "Cobrar por opinar", "Cerrar los tribunales", "El modelo lo dice en el paso 3."),
   ("abc", "{F} En el modelo, ¿qué podemos hacer las personas?", "Asistir y respetar a quienes enseñan y aprenden", "Evitar toda actividad", "Pedir un trato especial", "El paso 4 describe la responsabilidad de las personas."),
   ("abc", "{F} Completa el paso 2 para el derecho a opinar: «en democracia se protege con ___».", "espacios de participación y libertad de expresión", "silencio obligatorio", "castigos por hablar", "La democracia protege la voz de las personas."),
   ("abc", "Una persona dice: «Votar es un derecho; la democracia lo protege con elecciones; el Estado debe organizarlas; las personas podemos informarnos y votar». ¿Qué hizo?", "Usó los cuatro pasos", "Solo dio una opinión", "No relacionó nada", "Pasó por derecho, protección, deber del Estado y responsabilidad."),
   ("ab", "Una persona dice solo «la salud es un derecho». ¿Qué falta?", "Cómo lo protege la democracia, qué debe hacer el Estado y qué hacemos las personas", "Nada, está completo", "La intervención se queda en el primer paso."),
   ("abc", "Para relacionar el derecho a la información con la democracia, ¿qué puede decir el paso 3?", "El Estado debe entregar información pública clara", "El Estado debe esconder la información", "Solo las empresas informan", "Entregar información es un deber del Estado en una democracia."),
   ("abc", "¿Qué ejemplo sirve para el paso 4 del derecho a la educación?", "Asistir a clases y respetar a las demás personas", "Evitar estudiar siempre", "Esperar que otros lo hagan todo", "Asistir y respetar es una acción que depende de la persona."),
   ("abc", "Una persona pide a otra la fuente de una cifra. ¿Qué hace bien?", "Aplica el cuidado por las fuentes confiables", "Interrumpe sin motivo", "Pierde el tiempo", "Pedir la fuente ayuda a comprobar el dato."),
   ("abc", "Para el derecho a la no discriminación, ¿qué completa mejor el paso 3?", "El Estado debe tratar por igual a las personas y sancionar la discriminación según la ley", "El Estado debe discriminar un poco", "El Estado no tiene tareas", "Tratar por igual a las personas es un deber de igualdad."),
   ("abc", "¿Por qué una plantilla ayuda en un conversatorio?", "Porque ordena las ideas y permite hablar con claridad", "Porque reemplaza la conversación", "Porque impide hablar", "Sirve para estructurar lo que se dirá."),
   ("abc", "Si dos personas relacionan distintos derechos con la democracia usando los mismos cuatro pasos, ¿qué ocurre?", "Ambas pueden compararse con claridad", "No se pueden comparar", "Una de ellas está equivocada siempre", "Los pasos comunes facilitan entender ambas intervenciones.")],
  ("abc", "Una dirigente dice en un conversatorio: «Reunirnos es un derecho; la democracia lo protege con espacios de participación; el Estado debe respetarlo; nosotras podemos cuidar la sede y escuchar a todas». ¿Cuál es el paso 3?", "El Estado debe respetarlo", "Nosotras podemos cuidar la sede", "Reunirnos es un derecho", "Es la parte que nombra lo que le corresponde al Estado."),
  [("En Historia: ¿qué significa relacionar?", "Mostrar cómo dos ideas se conectan", "Une un derecho con la democracia."),
   ("¿Qué hace el paso 3 de la ficha?", "Dice qué debe hacer el Estado", "Se refiere al deber del Estado."),
   ("¿Qué hace el paso 4 de la ficha?", "Dice qué podemos hacer las personas", "Se refiere a las responsabilidades personales.")],
  ("Completa la plantilla para el derecho a la salud: «La salud es un derecho porque ___; en democracia se protege con ___; el Estado debe ___; las personas podemos ___». Escribe las cuatro partes y un ejemplo breve.",
   "La salud es un derecho porque permite vivir con dignidad; en democracia se protege con leyes y participación; el Estado debe ofrecer atención en consultorios públicos; las personas podemos asistir a controles y respetar al personal de salud. Ejemplo: asistir a un control con respeto.",
   ["completa los cuatro pasos", "agrega un ejemplo", "usa lenguaje claro y respetuoso"],
   ["plantilla completa en el cuaderno"],
   ["omitir la responsabilidad de las personas", "no explicar la protección democrática"],
   "Pregunta: «¿Está cada uno de los cuatro pasos?»."),
  "Lee la plantilla completada en voz alta y revisa si se entiende.",
  "Haz otra plantilla para el derecho a la participación.")

# ====================================================== clase 4
F = ("Ficha 4 (tabla de ejemplo: derecho, cómo lo protege la democracia, deber del Estado, responsabilidad de las personas). "
     "Fila 1. Derecho a la educación: se protege con leyes y participación; el Estado debe ofrecer escuelas; las personas asistimos y respetamos. "
     "Fila 2. Derecho a la salud: se protege con leyes y servicios públicos; el Estado debe ofrecer atención; las personas asistimos a controles y tratamos con respeto. "
     "Fila 3. Derecho a participar: se protege con elecciones y organizaciones; el Estado debe organizar las elecciones; las personas nos informamos y votamos. "
     "Fila 4. Derecho a no ser discriminado: se protege con igualdad ante la ley; el Estado debe tratar por igual y sancionar según la ley; las personas tratamos con respeto. "
     "Nota de memoria: en Chile, entre 1973 y 1990, hubo un régimen militar (dictadura) en el que ocurrieron graves violaciones a los derechos humanos; informes oficiales, como los de la Comisión Rettig (1991) y la Comisión Valech (2004), las reconocieron. En 1990 el país volvió a la democracia. Por eso se valora un Estado de Derecho que proteja a todas las personas.")
K(4, F,
  "Hoy practico, con apoyo de una tabla, cómo se relacionan distintos derechos humanos con la democracia y los deberes del Estado, y por qué importa el Estado de Derecho.",
  ["Practicar es aplicar los cuatro pasos a varios derechos. La tabla muestra cuatro: educación, salud, participación y no discriminación. En cada fila ves cómo se protege el derecho en democracia, qué debe hacer el Estado y qué hacemos las personas.",
   "Esta relación existe porque la democracia no solo es elegir autoridades: también es proteger derechos con leyes iguales para todas las personas. Cuando el Estado de Derecho funciona, los derechos tienen límites claros frente al poder y existen vías para reclamar.",
   "En Chile, entre 1973 y 1990, hubo un régimen militar en el que se violaron gravemente los derechos humanos; informes oficiales, como los de la Comisión Rettig (1991) y la Comisión Valech (2004), lo reconocieron, y en 1990 el país volvió a la democracia. Fue un tiempo doloroso para muchas personas y familias. Recordarlo con rigor y respeto ayuda a valorar instituciones que protejan a todas las personas y a conversar sin descalificar; para profundizar, conviene acudir a especialistas y a fuentes oficiales."],
  [("violación de derechos humanos", "acto que atenta gravemente contra los derechos de una persona, especialmente cuando lo cometen agentes del Estado"), ("memoria", "recuerdo compartido de hechos del pasado para no repetirlos"), ("vía de reclamo", "camino formal para pedir que se respete un derecho"), ("institución", "organización pública estable que cumple una función para la sociedad")],
  [("Leer una fila", "Fila 2: ¿qué debe hacer el Estado respecto de la salud?", ["Busco la fila de salud.", "Leo la columna del deber del Estado."], "Ofrecer atención en servicios públicos"),
   ("Comparar filas", "¿En qué se parecen las filas 1 y 2 en la responsabilidad de las personas?", ["Ambas piden acudir al servicio.", "Ambas piden tratar con respeto."], "En que las personas asisten y tratan con respeto")],
  [("Pensar que recordar el pasado es buscar culpables entre las personas de hoy.", "Se confunde memoria con acusación.", "La memoria busca entender hechos y evitar que se repitan."),
   ("Creer que el Estado de Derecho solo importa a las autoridades.", "Se olvida que protege a todas las personas.", "Protege a cualquier persona frente a abusos.")],
  [("abc", "{F} ¿Qué debe hacer el Estado respecto del derecho a participar?", "Organizar las elecciones", "Evitar elecciones", "Silenciar organizaciones", "La fila 3 de la tabla lo indica con claridad."),
   ("abc", "{F} ¿Con qué se protege el derecho a no ser discriminado, según la tabla?", "Con la igualdad ante la ley", "Con el silencio", "Con el trato especial", "La fila 4 de la tabla relaciona ambos conceptos."),
   ("ab", "{F} ¿Qué responsabilidad de las personas aparece en la fila 3?", "Informarnos y votar", "No participar", "La fila 3 dice que las personas nos informamos y votamos."),
   ("{F} ¿Cuántas filas tiene la tabla?", "4", "La tabla describe educación, salud, participación y no discriminación."),
   ("abc", "{F} ¿Qué fila usarías para hablar de las escuelas públicas?", "La fila 1", "La fila 3", "La fila 4", "La fila 1 trata el derecho a la educación."),
   ("abc", "{F} ¿Qué dice la nota de memoria?", "Entre 1973 y 1990 hubo graves violaciones a los derechos humanos, reconocidas por informes oficiales, y en 1990 se volvió a la democracia", "Nunca hubo problemas con los derechos", "Los derechos no importan", "La nota explica la importancia de un Estado de Derecho."),
   ("abc", "¿Por qué se recuerda con rigor y respeto ese pasado?", "Para valorar instituciones que protejan a todas las personas", "Para acusar a las personas que viven hoy", "Para olvidar los derechos", "La memoria cuida a las personas y evita repetir daños."),
   ("abc", "Una persona dice: «Si el Estado respeta la ley, no hay violaciones de derechos». ¿Qué falta en su idea?", "Que además existan vías para reclamar y vigilancia por parte de las personas", "Nada", "Que se eliminen las leyes", "La protección requiere instituciones y participación."),
   ("abc", "¿Qué ejemplo muestra una vía de reclamo?", "Presentar un reclamo ante una institución pública", "Gritar en la calle sin hablar con nadie", "Esperar sin hacer nada", "Es un camino formal para pedir que se respete un derecho."),
   ("ab", "Si un servicio público trata distinto a una persona por su origen, ¿qué fila de la tabla se ve afectada?", "La fila 4, no discriminación", "La fila 3", "Se afecta la igualdad ante la ley."),
   ("abc", "¿Cuál de estas opciones relaciona bien el derecho a participar con la democracia?", "Las elecciones y organizaciones permiten que las personas influyan en decisiones", "La democracia prohíbe opinar", "Solo las autoridades participan", "Une el derecho con las formas de participación."),
   ("abc", "En un conversatorio alguien describe un hecho del pasado reciente con insultos. ¿Qué respuesta ayuda a cuidar el diálogo?", "Pedir que se hable con respeto y apoyarse en fuentes confiables", "Responder con otro insulto", "Callar para siempre", "Se mantiene el respeto y la información verificable."),
   ("abc", "¿Qué conclusión resume mejor esta tabla?", "Cada derecho se apoya en la democracia, el deber del Estado y la responsabilidad de las personas", "Los derechos dependen solo de las personas", "El Estado no tiene deberes", "Combina los cuatro pasos de la clase.")],
  ("abc", "Una organización vecinal quiere conversar sobre el derecho a la salud. ¿Cuál es la relación más completa?", "Se protege con leyes y servicios públicos; el Estado debe ofrecer atención; las personas asisten y tratan con respeto", "Solo se necesita fe", "Es un favor del municipio", "Incluye democracia, deber del Estado y responsabilidad."),
  [("En Historia: ¿qué es la memoria?", "Recuerdo compartido de hechos del pasado para no repetirlos", "Se recuerda con rigor y respeto."),
   ("¿Qué es una vía de reclamo?", "Camino formal para pedir que se respete un derecho", "Permite exigir una respuesta sin usar la violencia."),
   ("En Historia y Ciencias Sociales, ¿qué es una institución pública?", "Organización pública estable que cumple una función para la sociedad", "Por ejemplo, un tribunal o un consultorio.")],
  ("Con la tabla de la ficha elige dos filas y escribe, para cada una, una frase que las relacione en cuatro partes (derecho, democracia, deber del Estado, responsabilidad de las personas). Después escribe una pregunta respetuosa que harías en un conversatorio.",
   "Fila 1: la educación es un derecho; en democracia se protege con leyes y participación; el Estado debe ofrecer escuelas; las personas asistimos y respetamos. Pregunta: ¿cómo podemos apoyar a quienes quieren terminar sus estudios?",
   ["dos filas con las cuatro partes", "una pregunta respetuosa", "lenguaje claro"],
   ["dos frases completas y una pregunta"],
   ["omitir una de las cuatro partes", "pregunta que descalifica"],
   "Pregunta: «¿Están las cuatro partes en cada frase?»."),
  "Elige un derecho de la tabla y explica su relación en voz alta.",
  "Escribe una pregunta que invite a conversar sobre cómo cuidar los derechos en una comunidad.")

# ====================================================== clase 5
F = ("Ficha 5 (conversatorio de ejemplo de una organización comunitaria sobre «¿Cómo cuidamos los derechos en nuestra comunidad?»). "
     "Moderadora: «Cada persona tendrá tres minutos. Escuchemos sin interrumpir». "
     "Intervención 1 (Ana, nombre de ejemplo): «El derecho a la salud se protege con servicios públicos. El Estado debe ofrecer atención, y nosotras podemos asistir a los controles. Por ejemplo, hoy hubo fila en el consultorio, pero todas esperamos el turno». "
     "Intervención 2 (Pedro, nombre de ejemplo): «Yo creo que todo está mal». "
     "Intervención 3 (Carla, nombre de ejemplo): «Coincido con Ana. Agrego que la participación es un derecho: si no votamos ni vamos a reuniones, nadie conoce lo que necesita la comunidad». "
     "Intervención 4 (Jorge, nombre de ejemplo): «Entiendo a Carla, pero me parece que a veces falta información. ¿De qué fuente sale lo que dijo?».")
K(5, F,
  "Hoy aplico lo aprendido a un conversatorio de comunidad: analizo intervenciones, escribo la mía y me comunico con claridad y respeto.",
  ["Un conversatorio de comunidad es un espacio donde las personas hablan de lo que viven y de lo que se puede mejorar. Aplicar lo aprendido significa relacionar un derecho con la democracia y con el deber del Estado, y hacerlo con claridad y respeto.",
   "Mira las intervenciones de la ficha. La de Ana usa varios pasos: nombra el derecho, dice el deber del Estado, la responsabilidad personal y da un ejemplo. La de Pedro es solo una queja general. La de Carla coincide con Ana y agrega la participación. Jorge pide una fuente con respeto.",
   "Al preparar tu intervención, escribe una idea, una razón, un ejemplo y una pregunta para quien piensa distinto. Una buena conversación termina con acuerdos o con nuevas preguntas, y siempre cuida el trato respetuoso entre las personas."],
  [("moderadora", "persona que organiza los turnos y cuida el orden de una conversación"), ("coincidir", "estar de acuerdo en una idea"), ("acuerdo", "decisión o idea en que las personas coinciden"), ("pregunta abierta", "pregunta que invita a explicar y no solo a responder sí o no")],
  [("Evaluar una intervención", "Una persona dice «todo está mal». ¿Relaciona un derecho con la democracia?", ["No nombra un derecho.", "No da razón ni ejemplo."], "No, es una queja general"),
   ("Escribir una pregunta abierta", "Idea: la participación importa. ¿Qué pregunta abierta puedes hacer?", ["Quiero que expliquen.", "No puede responderse con sí o no."], "¿Cómo podemos animar a más vecinos a participar?")],
  [("Responder a una idea con una descalificación.", "Se ataca a la persona y no la idea.", "Responde con una razón y una pregunta."),
   ("Dar un dato sin decir su fuente.", "Los demás no pueden comprobarlo.", "Cita de dónde sale el dato.")],
  [("abc", "{F} ¿Cuánto tiempo tiene cada persona para hablar?", "Tres minutos", "Un minuto", "Diez minutos", "La moderadora lo dice al iniciar."),
   ("abc", "{F} ¿Qué pide la moderadora al comenzar el conversatorio?", "escuchar sin interrumpir", "hablar todas a la vez", "no dar turnos", "La moderadora dice: «Escuchemos sin interrumpir»."),
   ("ab", "{F} ¿Ana relaciona el derecho a la salud con un deber del Estado?", "Sí, dice que el Estado debe ofrecer atención", "No lo menciona", "Ana lo dice en su intervención."),
   ("abc", "{F} ¿Qué derecho agrega Carla?", "La participación", "La educación", "La vivienda", "Carla dice que la participación es un derecho."),
   ("abc", "{F} ¿Qué hace Jorge al final?", "Pide con respeto la fuente de lo dicho", "Se burla de Carla", "Se va de la reunión", "Jorge pregunta de qué fuente sale lo dicho."),
   ("abc", "{F} ¿Qué ejemplo usa Ana?", "La fila del consultorio donde todas esperaron su turno", "Una elección nacional", "Un tribunal", "Ana lo menciona al final de su intervención."),
   ("{F} ¿Cuántas intervenciones hay en la ficha?", "4", "Se numeran cuatro: Ana, Pedro, Carla y Jorge."),
   ("abc", "{F} ¿Qué mejora le darías a la intervención de Pedro?", "Nombrar un derecho, dar una razón y un ejemplo", "Gritar más fuerte", "Quitarle la palabra", "Así pasaría de queja a argumento."),
   ("abc", "¿Cuál es una buena pregunta para continuar el conversatorio?", "¿Qué podemos hacer para que más personas participen?", "¿Por qué eres tan malo?", "¿Quién calla?", "Invita a aportar con ideas y no ataca."),
   ("ab", "Una persona dice que la moderadora impide la libertad de expresión por dar turnos. ¿Es correcto?", "No, los turnos permiten que todas las personas hablen", "Sí, los turnos limitan toda opinión", "Ordenar los turnos protege la participación de todas las personas."),
   ("abc", "En el conversatorio se dice que el 80 % de la comunidad no participa, sin citar fuente. ¿Qué es lo más adecuado?", "Pedir de dónde sale la cifra antes de usarla", "Aceptarla sin preguntar", "Repetirla más fuerte", "Una cifra sin fuente debe comprobarse."),
   ("abc", "Dos personas no coinciden. ¿Cuál cierre muestra una actitud democrática?", "Agradecer, resumir lo que cada una dijo y buscar un acuerdo posible", "Declarar que una está equivocada", "Terminar la reunión de inmediato", "Resumir y buscar acuerdos reconoce ambas ideas."),
   ("abc", "¿Qué intervención relaciona mejor derechos, democracia y deber del Estado?", "La de Ana, completa con derecho, deber y ejemplo", "La de Pedro", "Ninguna", "Es la única que desarrolla varios pasos.")],
  ("abc", "Una joven dice en un conversatorio: «Tengo derecho a opinar; la democracia nos da espacios para hacerlo; el Estado debe respetarlo; yo respeto el turno de los demás». ¿Qué hizo bien?", "Relacionó derecho, democracia, Estado y responsabilidad", "Solo dio una opinión", "No usó ninguna idea", "Cada parte de la frase corresponde a uno de los pasos."),
  [("En Historia: ¿qué hace una moderadora?", "Organiza los turnos y cuida el orden de la conversación", "Ayuda a que todas las personas hablen."),
   ("En un conversatorio de comunidad, ¿qué es una pregunta abierta?", "Una pregunta que invita a explicar y no solo a responder sí o no", "Una pregunta abierta fomenta el diálogo entre las personas."),
   ("Al cerrar un conversatorio, ¿qué es un acuerdo?", "Una idea o decisión en la que las personas coinciden", "Puede surgir al final de un conversatorio.")],
  ("Escribe tu intervención para el conversatorio «¿Cómo cuidamos los derechos en nuestra comunidad?». Incluye: un derecho, cómo lo protege la democracia, qué debe hacer el Estado, qué podemos hacer las personas, un ejemplo (puedes inventarlo, rotulado «de ejemplo») y una pregunta abierta para quien piensa distinto. Léela en voz alta y revisa que dure menos de tres minutos.",
   "La educación es un derecho; la democracia lo protege con leyes y participación; el Estado debe ofrecer escuelas; las personas asistimos y respetamos. Ejemplo (de ejemplo): una persona retoma sus estudios en una escuela de adultos. Pregunta: ¿cómo podemos apoyar a quienes quieren terminar sus estudios?",
   ["incluye derecho, democracia, deber del Estado y responsabilidad", "agrega ejemplo y pregunta abierta", "lenguaje respetuoso y de menos de tres minutos"],
   ["texto escrito o intervención leída en voz alta"],
   ["omitir una de las partes", "usar una cifra sin fuente"],
   "Pregunta: «¿Se escucha mi idea, mi razón y mi pregunta?»."),
  "Lee tu intervención a otra persona y pide un comentario.",
  "Prepara una segunda intervención para otro derecho.")

# ====================================================== clase 6
F = ("Ficha 6 (pauta de revisión de un conversatorio, un punto por criterio). 1) Nombra un derecho humano. 2) Explica cómo lo protege la democracia. 3) Dice qué debe hacer el Estado. "
     "4) Dice qué podemos hacer las personas. 5) Usa una razón y un ejemplo con lenguaje claro. 6) Escucha y responde con respeto. "
     "Intervención revisada (de ejemplo): «La salud es un derecho. En democracia se protege con leyes y servicios públicos. El Estado debe ofrecer atención en consultorios. Por ejemplo, en un control de salud, una persona recibe orientación. A veces algunas personas hablan muy fuerte, pero yo escucho a quien piensa distinto». "
     "No dice qué podemos hacer las personas para cuidar ese derecho.")
K(6, F,
  "Hoy reviso mi participación en un conversatorio con una pauta, corrijo lo que falta y decido qué voy a seguir practicando.",
  ["Revisar es mirar tu intervención con criterios claros. La pauta de seis puntos pregunta si nombraste un derecho, si explicaste cómo lo protege la democracia, si dijiste qué debe hacer el Estado, qué podemos hacer las personas, si fuiste claro y si escuchaste con respeto.",
   "Marca sí o no en cada criterio y suma los puntos. Por cada no, escribe una mejora concreta, por ejemplo: «agregar que las personas podemos asistir a controles» o «reducir la frase para que se entienda en menos tiempo». Así sabes qué cambiar en la próxima conversación.",
   "Para cerrar el módulo, recuerda que los derechos humanos, la democracia y el Estado de Derecho se apoyan entre sí. Usar fuentes confiables, comunicar con claridad y respetar a las demás personas son formas de cuidarlos todos los días."],
  [("pauta", "lista de criterios para revisar un trabajo"), ("criterio", "regla para decidir si algo está bien hecho"), ("mejora concreta", "cambio específico que hace mejor un trabajo"), ("autoevaluación", "revisar el propio trabajo con una pauta")],
  [("Contar puntos", "Una intervención cumple los criterios 1, 2, 3 y 6. ¿Cuántos puntos tiene de seis?", ["Cuento los sí.", "Son cuatro."], "4 de 6"),
   ("Escribir una mejora", "A la intervención le falta decir qué hacen las personas. ¿Qué mejora escribes?", ["Digo qué falta.", "Propongo una frase concreta."], "Agregar una frase sobre lo que podemos hacer las personas")],
  [("Marcar sí en todo sin releer la intervención.", "No se compara con la pauta.", "Revisa cada criterio con una frase de tu texto."),
   ("Escribir «hablar mejor» como mejora.", "No dice qué cambiar.", "Escribe una acción concreta.")],
  [("abc", "{F} ¿Cuántos criterios tiene la pauta?", "6", "4", "8", "La ficha de revisión numera seis criterios en total."),
   ("ab", "{F} ¿La intervención revisada nombra un derecho?", "Sí, la salud", "No", "La primera frase dice que la salud es un derecho."),
   ("abc", "{F} ¿Qué criterio no cumple la intervención revisada?", "El 4, lo que podemos hacer las personas", "El 1, nombrar el derecho", "El 3, el deber del Estado", "La ficha dice que no menciona esa parte."),
   ("abc", "{F} ¿Qué deber del Estado menciona la intervención?", "Ofrecer atención en consultorios", "Cobrar por hablar", "Cerrar los tribunales", "La tercera frase de la intervención lo dice."),
   ("{F} ¿Cuántos puntos obtiene la intervención revisada?", "5", "Cumple los criterios 1, 2, 3, 5 y 6 y solo falta el 4, así que suma cinco puntos."),
   ("abc", "{F} ¿Qué mejora corrige el criterio 4?", "Agregar «las personas podemos asistir a controles y tratar con respeto»", "Cambiar el título", "Eliminar el ejemplo", "Esa frase cumple lo que pide el criterio."),
   ("abc", "{F} ¿Qué frase muestra el criterio 6?", "«Escucho a quien piensa distinto»", "«La salud es un derecho»", "«El Estado debe ofrecer atención»", "La frase expresa escucha y respeto hacia otras personas."),
   ("abc", "Una intervención no tiene ejemplo. ¿Qué criterio no cumple?", "El 5", "El 1", "El 2", "El criterio 5 pide razón y ejemplo."),
   ("abc", "Si agregas al texto revisado la frase de la mejora, ¿cuántos puntos tendría?", "6", "5", "4", "Se suma el criterio que faltaba."),
   ("ab", "Una persona dice que revisar es solo juzgar si habló bien o mal. ¿Qué respuesta es correcta?", "Revisar es comparar con criterios y proponer mejoras", "Sí, es solo juzgar", "Una revisión útil dice qué mejorar y cómo."),
   ("abc", "¿Qué resumen se acerca más a lo aprendido en este módulo?", "Los derechos humanos se apoyan en la democracia, el Estado de Derecho y la responsabilidad de las personas", "Los derechos dependen de la suerte", "La democracia no necesita leyes", "Integra los conceptos principales que se vieron en el módulo."),
   ("abc", "Después de revisar tu intervención, ¿cuál es un próximo paso razonable?", "Practicarla de nuevo con la mejora y pedir un comentario", "Olvidarla", "Cambiar el tema sin revisar", "Practicar la mejora consolida lo aprendido."),
   ("abc", "En un grupo de conversación, ¿qué muestra una buena actitud cívica al final?", "Agradecer las ideas y resumir los acuerdos", "Culpar a otra persona", "Ignorar lo hablado", "Cuida el respeto y deja constancia de lo conversado.")],
  ("abc", "Una organización revisa sus conversatorios y descubre que casi nadie da ejemplos. ¿Qué mejora concreta propone?", "Pedir que cada intervención incluya un ejemplo breve", "Suspender los conversatorios", "Prohibir las preguntas", "La mejora apunta al criterio 5."),
  [("En Historia: ¿qué es una autoevaluación?", "Revisar el propio trabajo con una pauta", "Permite saber qué cosas conviene mejorar."),
   ("¿Qué es una mejora concreta?", "Un cambio específico que mejora un trabajo", "Una mejora concreta dice qué cambiar y cómo hacerlo."),
   ("¿Qué cuida un conversatorio respetuoso?", "Los turnos, las razones y el trato entre personas", "Permite convivir con personas que tienen ideas distintas.")],
  ("Revisa con la pauta de seis puntos esta intervención de ejemplo: «La participación es un derecho. En democracia se protege con elecciones y organizaciones. El Estado debe organizar las elecciones. Las personas podemos informarnos y votar. Interrumpí a otra persona porque tenía prisa». Marca sí o no en cada criterio, suma los puntos y escribe una mejora para cada no.",
   "Criterios 1 a 4: sí. Criterio 5: no hay ejemplo. Criterio 6: no, interrumpió. Puntos: 4. Mejoras: agregar un ejemplo breve y esperar el turno para hablar.",
   ["marca los seis criterios con razones", "suma bien los puntos", "escribe una mejora concreta por cada no"],
   ["pauta marcada con las mejoras"],
   ["marcar sin razones", "mejoras vagas"],
   "Pregunta: «¿Qué cambio haría que este criterio pase de no a sí?»."),
  "Escribe un compromiso para mejorar una conversación en tu comunidad.",
  "Prepara una pregunta abierta para iniciar un conversatorio sobre derechos y democracia.")
