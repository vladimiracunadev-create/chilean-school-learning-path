"""Historia, Geografía y Ciencias Sociales EPJA Básica N2, módulo 4 (parte 3): OAD-15, identificar mediante un cómic, con información de fuentes seleccionadas, los deberes del Estado y los derechos y responsabilidades de las personas en una democracia. Los cómics se describen viñeta por viñeta en palabras; datos de ejemplo rotulados."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz y goma; si quieres, una hoja dividida en cuatro cuadros para dibujar viñetas. Todo se resuelve con lo escrito en la ficha: los cómics y las fuentes son de ejemplo, descritos en palabras."
build = make_build(MATERIALS)

O = "EPJA-HGCS-NB2-OAD-15"
PRIOR = ["Ya he visto cómics, tiras o dibujos con globos de diálogo.", "Sé que las personas tienen derechos y que las instituciones públicas prestan servicios."]


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    build(O, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ====================================================== clase 1
F = ("Ficha 1 (cómic de ejemplo «La fila del consultorio», cuatro viñetas descritas en palabras). "
     "Viñeta 1: dos personas esperan en una fila; un letrero dice «Atención por orden de llegada». "
     "Viñeta 2: una persona se cuela delante de otra; la persona de atrás dice en un globo: «Disculpa, yo llegué antes». "
     "Viñeta 3: la funcionaria dice: «Les atiendo a todas las personas por orden de llegada». "
     "Viñeta 4: la persona que se coló dice: «Tienes razón, perdón» y vuelve al final de la fila.")
K(1, F,
  "Hoy reconozco qué es un cómic, cómo cuenta una situación en viñetas y qué derechos, deberes y responsabilidades se ven en la vida diaria.",
  ["Un cómic cuenta una historia con dibujos ordenados en cuadros llamados viñetas. Los globos muestran lo que dicen los personajes y los recuadros ofrecen explicaciones. Tú ya lo has visto en diarios, folletos o campañas que explican un trámite con dibujos.",
   "Un cómic también sirve para enseñar sobre la vida en democracia. En «La fila del consultorio» aparecen tres ideas: el derecho de las personas a ser atendidas en igualdad, el deber de una institución de atender con un criterio justo y la responsabilidad de respetar el turno.",
   "Para leer un cómic, mira las viñetas en orden, lee los globos y pregúntate: ¿qué ocurre?, ¿quién ejerce un derecho?, ¿qué debe hacer la institución? y ¿qué responsabilidad tiene cada persona? Así identificas ideas importantes sin necesidad de un texto largo."],
  [("viñeta", "cada cuadro de un cómic"), ("globo de diálogo", "espacio donde se escribe lo que dice un personaje"), ("deber del Estado", "lo que las instituciones públicas deben hacer para que se cumplan los derechos"), ("responsabilidad", "lo que cada persona debe hacer para respetar a las demás y cuidar lo común")],
  [("Leer una viñeta", "Viñeta: una persona dice «Yo llegué antes». ¿Qué derecho reclama?", ["Pide que se respete el orden de llegada.", "Ese orden asegura un trato igualitario."], "El derecho a ser tratada con igualdad"),
   ("Identificar la responsabilidad", "En una viñeta, una persona vuelve al final de la fila tras equivocarse. ¿Qué responsabilidad muestra?", ["Reconoce que no respetó el turno.", "Corrige su conducta."], "Respetar el turno de las demás")],
  [("Leer solo el dibujo e ignorar los globos.", "Se pierde lo que dicen los personajes.", "Lee dibujos y globos juntos."),
   ("Creer que un cómic es solo para niños.", "Se asocia el formato con un público infantil.", "Es una forma de comunicar ideas a cualquier edad.")],
  [("abc", "{F} ¿Qué dice el letrero de la primera viñeta?", "Atención por orden de llegada", "Atención solo para personas conocidas", "Atención por sorteo", "El letrero da el criterio de atención en esa viñeta."),
   ("ab", "{F} En la viñeta 2, ¿quién reclama por el turno?", "La persona que estaba atrás", "La funcionaria", "La persona de atrás dice «Disculpa, yo llegué antes»."),
   ("abc", "{F} ¿Qué hace la persona que se coló en la viñeta 4?", "Reconoce su error y vuelve al final de la fila", "Se queda sin decir nada", "Discute con la funcionaria", "El globo dice «Tienes razón, perdón» y vuelve a la fila."),
   ("abc", "{F} ¿Cuántas viñetas tiene el cómic?", "4", "3", "6", "La ficha describe cuatro viñetas, numeradas del uno al cuatro."),
   ("abc", "{F} ¿Qué deber de la institución se ve en la viñeta 3?", "Atender a todas las personas con un criterio justo", "Cerrar la atención", "Dar prioridad a los conocidos", "La funcionaria afirma que atiende por orden de llegada."),
   ("abc", "{F} ¿Qué derecho se ve en la situación de la persona que llegó antes?", "Ser tratada con igualdad", "Votar en una elección", "Viajar sin pagar", "Pide que se respete su turno igual que el de las demás."),
   ("abc", "{F} ¿Qué responsabilidad de las personas muestra el cómic?", "Respetar el turno de las demás", "Cobrar por pasar primero", "Evitar la fila", "La viñeta 4 muestra cómo se corrige la falta de respeto al turno."),
   ("ab", "¿Para qué sirve un globo de diálogo?", "Para mostrar lo que dice un personaje", "Para indicar el color del dibujo", "El globo lleva las palabras de quien habla."),
   ("abc", "Un cómic muestra a una persona que reclama con calma y respeto ante una oficina pública. ¿Qué idea de democracia refleja?", "Que se puede exigir un derecho sin faltar el respeto", "Que reclamar está prohibido", "Que solo se reclama gritando", "Ejercer un derecho respetando a otros es una actitud cívica."),
   ("ab", "Si en el cómic la funcionaria hubiera atendido primero a un conocido, ¿qué deber habría incumplido?", "Atender con un criterio justo para todas las personas", "Ninguno", "Dar prioridad por amistad rompe el trato igualitario que debe ofrecer la institución."),
   ("abc", "En una sala de espera, un cartel dice: «Por favor, respete su turno». ¿A quién recuerda esta responsabilidad?", "A las personas que esperan", "Solo a la funcionaria", "A nadie", "Es un llamado a quienes esperan a cuidar el orden común."),
   ("abc", "¿Qué ventaja tiene explicar una norma de convivencia con un cómic?", "Se entiende rápido con pocas palabras y dibujos", "Se vuelve más difícil de leer", "Se pueden omitir las ideas principales", "Combina imagen y texto breve, y así se entiende rápido."),
   ("abc", "Un cómic tiene viñetas desordenadas: «Reclama con respeto», «Espera en la fila», «Es atendida». ¿Cuál es el orden más lógico?", "Espera en la fila, reclama con respeto, es atendida", "Es atendida, espera, reclama", "Reclama, es atendida, espera", "La historia tiene primero la espera, luego el reclamo y al final la atención.")],
  ("abc", "Un centro comunitario quiere un cómic para explicar por qué hay que respetar el orden de llegada en los servicios. ¿Cuál es la idea central más adecuada?", "Todas las personas merecen el mismo trato y todas deben respetar el turno", "Solo algunos merecen atención", "Pasar primero depende de quién grita más", "Une un derecho a la igualdad y una responsabilidad."),
  [("En Historia: ¿qué es una viñeta?", "Cada cuadro de un cómic", "Las viñetas se leen en orden."),
   ("¿Qué es un deber del Estado?", "Lo que las instituciones públicas deben hacer para que se cumplan los derechos", "Se relaciona con servicios como la atención de salud."),
   ("¿Qué muestra una responsabilidad en el cómic?", "Lo que cada persona hace para respetar a las demás", "Respetar el turno es un ejemplo.")],
  ("Mira este cómic de ejemplo: Viñeta 1: una vecina pide una hora en una oficina pública. Viñeta 2: la funcionaria le explica con calma qué documentos necesita. Viñeta 3: la vecina dice «Gracias, vuelvo con el papel». Escribe: (a) qué derecho se ejerce, (b) qué deber de la institución aparece, (c) qué responsabilidad de la vecina aparece.",
   "(a) El derecho a ser atendida e informada. (b) Informar y atender con claridad. (c) Llevar los documentos y tratar con respeto.",
   ["nombra un derecho", "nombra un deber de la institución", "nombra una responsabilidad de la persona"],
   ["tres frases escritas, una por cada pregunta"],
   ["confundir el deber de la institución con la responsabilidad de la persona", "mencionar solo el dibujo"],
   "Pregunta: «¿Quién hace qué en esta viñeta?»."),
  "Piensa en una norma de convivencia y di cómo la contarías en cuatro viñetas.",
  "Escribe qué derecho, qué deber de una institución y qué responsabilidad hay en una fila de un trámite.")

# ====================================================== clase 2
F = ("Ficha 2 (glosario y viñetas de ejemplo). Derecho: lo que una persona puede ejercer por ser persona. "
     "Deber del Estado: lo que las instituciones públicas deben hacer para que los derechos se cumplan, como ofrecer educación, atención de salud, justicia y protección. "
     "Responsabilidad de las personas: respetar los derechos de las demás, cumplir las normas acordadas, participar y cuidar lo común. "
     "Viñeta A: una persona adulta se inscribe en una escuela pública para terminar sus estudios. Viñeta B: un vecino deja los escombros de una reparación en la vereda y bloquea el paso. "
     "Viñeta C: un tribunal escucha a una persona que presentó un reclamo. Viñeta D: un grupo de vecinos limpia una plaza el domingo. "
     "Viñeta E: una persona mayor es atendida en un consultorio público sin importar su origen.")
K(2, F,
  "Hoy distingo, en situaciones de un cómic, el derecho de una persona, el deber del Estado y la responsabilidad de las personas.",
  ["En una democracia, derechos, deberes del Estado y responsabilidades de las personas se complementan. El derecho es lo que puedes ejercer: estudiar, atenderte, expresarte. El deber del Estado es lo que las instituciones públicas deben hacer para que eso se cumpla.",
   "Las responsabilidades de las personas son nuestras tareas para que la vida en común funcione: respetar a las demás, cumplir normas acordadas, participar y cuidar lo común, como las veredas o las plazas. Un derecho no se ejerce a costa de los derechos de otras personas.",
   "Para identificar cada idea en un cómic, pregúntate: ¿quién recibe o ejerce algo?, eso es el derecho. ¿Quién ofrece un servicio público?, eso es el deber del Estado. ¿Quién hace algo por el bien de todos?, eso es la responsabilidad de las personas."],
  [("derecho", "lo que una persona puede ejercer por ser persona"), ("deber del Estado", "lo que las instituciones públicas deben hacer para que los derechos se cumplan"), ("responsabilidad", "lo que cada persona hace para respetar a las demás y cuidar lo común"), ("bien común", "lo que sirve y pertenece a todos, como una plaza o una vereda")],
  [("Clasificar una viñeta", "Una persona adulta se inscribe en una escuela pública para terminar sus estudios. ¿Qué derecho ejerce?", ["Está estudiando.", "Eso corresponde a la educación."], "El derecho a la educación"),
   ("Clasificar una acción", "Un grupo de vecinos limpia una plaza el domingo. ¿Es derecho, deber del Estado o responsabilidad de las personas?", ["Lo hace un grupo de personas.", "Cuidan un bien común."], "Responsabilidad de las personas")],
  [("Poner el cuidado de la plaza solo como deber del Estado.", "Se piensa que las personas no tienen ninguna tarea.", "El Estado presta servicios y las personas cuidan lo común."),
   ("Creer que un derecho permite bloquear el paso de otras personas.", "Se olvida que los derechos tienen el límite del derecho ajeno.", "Ejerce tus derechos sin impedir los de las demás.")],
  [("abc", "{F} ¿Qué viñeta muestra una responsabilidad de las personas por el bien común?", "D, la limpieza de la plaza", "A, la inscripción en la escuela", "C, el tribunal", "Limpiar una plaza es cuidar un espacio de todos."),
   ("abc", "{F} ¿Qué viñeta muestra una institución cumpliendo su deber de impartir justicia?", "C, el tribunal que escucha un reclamo", "B, el vecino con los escombros", "D, la limpieza de la plaza", "Un tribunal es una institución pública que resuelve reclamos."),
   ("ab", "{F} La viñeta B, ¿muestra una responsabilidad cumplida o incumplida?", "Incumplida", "Cumplida", "Los escombros en la vereda impiden el paso de otras personas."),
   ("abc", "{F} ¿Qué derecho se ve en la viñeta E?", "El derecho a la salud, sin discriminar", "El derecho a votar", "El derecho a la educación", "Atender en un consultorio a una persona mayor, sin importar su origen, respeta la salud y la igualdad."),
   ("abc", "{F} ¿Qué deber del Estado se ve en la viñeta A?", "Ofrecer educación", "Ofrecer transporte gratis", "Construir una plaza", "Una escuela pública es un servicio educativo del Estado."),
   ("abc", "{F} ¿Qué viñeta muestra un derecho y un deber del Estado al mismo tiempo?", "A, la escuela pública", "B, los escombros", "D, la limpieza de la plaza", "La persona ejerce su derecho a estudiar y la escuela presta el servicio."),
   ("{F} ¿Cuántas viñetas muestran a personas cumpliendo una responsabilidad por el bien común?", "1", "Solo la viñeta D muestra personas cuidando lo común; la B muestra lo contrario."),
   ("abc", "Un vecino dice: «Si pago mis impuestos, no tengo que cuidar la plaza». ¿Qué corrección haces?", "Cuidar los espacios comunes es una responsabilidad de todas las personas", "Tiene razón, no debe hacer nada", "Debe ir a un tribunal", "Cuidar lo común también es tarea de las personas."),
   ("ab", "¿Qué deber del Estado cumple un consultorio público?", "Proteger el derecho a la salud", "Cobrar por el servicio", "Un consultorio público presta atención de salud a las personas."),
   ("abc", "{F} Para mejorar la situación de la viñeta B, ¿qué debe hacer el vecino?", "Retirar los escombros y despejar la vereda", "Dejarlos un mes más", "Pedir que otras personas pasen por la calle", "Despejar la vereda restituye el paso de todos."),
   ("abc", "Una persona reclama con respeto en un servicio público porque no la atendieron. ¿Qué derecho ejerce?", "Reclamar y ser escuchada", "No hacer fila", "Pasar por sobre otros", "Reclamar con respeto es una forma de participación."),
   ("abc", "Una escuela pública cierra sin avisar y no ofrece otra opción. ¿Qué deber del Estado está en duda?", "Asegurar el derecho a la educación", "Cuidar la plaza", "Organizar una fiesta", "Si falla el servicio educativo, se ve afectado el derecho a estudiar."),
   ("abc", "¿Por qué los derechos de una persona terminan donde empiezan los derechos de otra?", "Porque todas las personas tienen los mismos derechos", "Porque los derechos son un favor", "Porque solo algunas personas pueden ejercerlos", "La igualdad exige respetar a las demás al ejercer los propios derechos.")],
  ("abc", "En un cómic, una vecina cuenta que fue a pedir un certificado y la atendieron con respeto. Luego ayuda a una persona mayor a leer el formulario. ¿Qué responsabilidad muestra la vecina?", "Colaborar y tratar con respeto a otras personas", "Cobrar por la ayuda", "Pasar primero en la fila", "Ayudar con respeto es una conducta cívica."),
  [("En Historia: ¿qué es el bien común?", "Lo que sirve y pertenece a todos, como una plaza", "Se cuida entre todas las personas."),
   ("¿Qué es un deber del Estado?", "Lo que las instituciones públicas deben hacer para que los derechos se cumplan", "Ejemplos: ofrecer educación o atención de salud."),
   ("¿Qué es una responsabilidad de las personas?", "Respetar a las demás y cuidar lo común", "Se ejerce en las acciones cotidianas con otras personas.")],
  ("Con las viñetas A a E de la ficha, haz una tabla con tres columnas: «Derecho», «Deber del Estado» y «Responsabilidad de las personas». Ubica cada letra donde corresponda (una letra puede ir en más de una columna) y escribe una razón corta por cada ubicación.",
   "Derecho: A y E. Deber del Estado: A, C y E. Responsabilidad: D (y B muestra lo que no se debe hacer).",
   ["ubica las cinco viñetas", "da una razón por cada ubicación", "usa los términos del glosario"],
   ["tabla con tres columnas y razones breves"],
   ["no distinguir deber del Estado y responsabilidad de las personas", "ubicar todo en una sola columna"],
   "Pregunta: «¿Quién hace aquí algo: una institución o una persona?»."),
  "Escribe una frase con cada término: derecho, deber del Estado y responsabilidad.",
  "Inventa una viñeta que muestre una responsabilidad de las personas por el bien común.")

# ====================================================== clase 3
F = ("Ficha 3 (de la fuente a la viñeta). Fuente de ejemplo, con autor e institución: «Manual de convivencia cívica» de una institución educativa (ejemplo), edición 2022. Texto: «Las instituciones públicas deben atender a todas las personas con igualdad. Las personas deben respetar los turnos y cuidar los espacios comunes». "
     "Pasos del guion: 1) seleccionar la fuente, 2) extraer la idea principal, 3) dividir la idea en cuatro escenas, 4) escribir un globo breve en cada escena, 5) anotar la fuente al pie. "
     "Guion de ejemplo: escena 1, una persona llega a una oficina; escena 2, otra persona se coloca delante; escena 3, la funcionaria recuerda el orden de llegada; escena 4, ambas personas acuerdan respetar el turno.")
K(3, F,
  "Hoy aprendo, paso a paso, a convertir la información de una fuente en un cómic de cuatro viñetas que muestre derechos, deberes y responsabilidades.",
  ["Para hacer un cómic con sentido, primero se elige una fuente confiable y se extrae su idea principal. Luego se divide la idea en escenas simples: inicio, problema, intervención y cierre. Cada viñeta cuenta una parte de la historia, como en un relato breve.",
   "Después se escribe un globo corto en cada escena, con frases de menos de diez palabras. Las imágenes se describen con trazos simples: no necesitas dibujar bien, sino mostrar quién hace qué. Al final, se anota la fuente al pie, como hacemos en un afiche.",
   "En el cómic debe verse con claridad quién ejerce un derecho, qué deber cumple una institución y qué responsabilidad asumen las personas. Así quien lo lea identifica estas ideas sin explicaciones largas y puede comprobar de dónde viene la información."],
  [("guion", "plan escrito de lo que se mostrará y dirá en cada escena"), ("escena", "momento de la historia que se muestra en una viñeta"), ("idea principal", "lo más importante que dice una fuente"), ("anotar la fuente", "escribir de dónde viene la información, con nombre y año")],
  [("Extraer la idea principal", "Texto: «Las personas deben cuidar la plaza porque es de todos». ¿Cuál es la idea principal?", ["Busco qué se afirma sobre la plaza.", "Se afirma que es de todos y hay que cuidarla."], "Cuidar la plaza es responsabilidad de todas las personas"),
   ("Dividir en escenas", "Idea: respetar los turnos. ¿Qué podría mostrar la escena 3?", ["Las escenas siguen inicio, problema, intervención y cierre.", "La tercera es la intervención."], "Alguien recuerda el orden de llegada")],
  [("Copiar un párrafo largo dentro de un globo.", "Se olvida que un cómic usa frases breves.", "Resume la idea en una frase corta por viñeta."),
   ("Inventar un dato y no anotar la fuente.", "Se pierde la posibilidad de comprobar.", "Usa datos de una fuente y anótala al pie.")],
  [("abc", "{F} ¿Cuál es el primer paso del guion?", "Seleccionar la fuente", "Colorear el cómic", "Escribir los nombres de los personajes", "La ficha lo numera como paso 1."),
   ("ab", "{F} ¿La fuente de ejemplo tiene autor e institución?", "Sí, es un manual de una institución educativa", "No tiene ninguno", "La ficha nombra el manual, la institución y la edición."),
   ("{F} ¿Cuántos pasos tiene el guion?", "5", "La lista numerada llega hasta el paso 5."),
   ("abc", "{F} ¿Cuál es la idea principal de la fuente?", "Las instituciones atienden con igualdad y las personas respetan turnos y cuidan lo común", "Los turnos no existen", "Solo las instituciones tienen tareas", "El texto menciona deberes de las instituciones y responsabilidades de las personas."),
   ("abc", "{F} ¿Qué ocurre en la escena 2 del guion de ejemplo?", "Otra persona se coloca delante", "La funcionaria recuerda el orden", "Ambas acuerdan respetar el turno", "La ficha dice que en la escena 2 alguien se pone delante."),
   ("abc", "{F} ¿Qué escena muestra el cierre?", "La escena 4", "La escena 1", "La escena 2", "La cuarta escena muestra el acuerdo de respetar el turno."),
   ("abc", "¿Cuál es un globo adecuado para la escena 3?", "«Aquí se atiende por orden de llegada»", "«Hoy cocinaremos una receta»", "«Nadie debe respetar nada»", "Resume la regla en una frase breve."),
   ("abc", "{F} ¿Dónde debe anotarse la fuente del cómic?", "Al pie, con nombre y año", "En el título", "No es necesario anotarla", "La ficha indica anotarla al pie para poder comprobarla."),
   ("ab", "Una persona dice que para hacer un cómic hay que dibujar muy bien. ¿Es correcto?", "No, bastan trazos simples que muestren quién hace qué", "Sí, sin buen dibujo no se entiende", "Lo importante es que se entienda la idea, no la calidad del dibujo."),
   ("abc", "Un globo dice: «Las instituciones públicas, conforme a la normativa vigente y a la Constitución, deben atender con criterios objetivos a todas las personas inscritas en el registro». ¿Qué problema tiene para un cómic?", "Es demasiado largo y complejo", "Es demasiado breve", "No tiene ninguna palabra", "En un cómic las frases deben ser breves."),
   ("abc", "Se quiere mostrar en el cómic una responsabilidad de las personas. ¿Cuál escena sirve?", "Un vecino recoge la basura de la plaza", "Una funcionaria atiende un reclamo", "Un tribunal dicta una sentencia", "Recoger la basura muestra una acción personal por el bien común."),
   ("abc", "Un cómic inventa la cifra «el 99 % de las personas no respeta turnos» sin citar fuente. ¿Qué debe hacerse?", "Quitar la cifra o respaldarla con una fuente fiable", "Dejarla porque llama la atención", "Escribirla más grande", "Un dato sin fuente no puede comprobarse."),
   ("abc", "¿Cuál es el orden correcto de los pasos para preparar un cómic?", "Fuente, idea principal, escenas, globos, anotar fuente", "Globos, colores, fuente, escenas", "Escenas, fuente, globos, idea", "Sigue la numeración del guion de la ficha.")],
  ("abc", "Un centro de personas jóvenes y adultas prepara un cómic sobre cuidar un espacio común. Tienen una fuente con autor y año. ¿Qué escena corresponde al «problema»?", "Alguien deja basura en el espacio común", "Todos ayudan a limpiar", "Se escribe la fuente al pie", "El problema es la situación que rompe la responsabilidad compartida."),
  [("En Historia: ¿qué es un guion?", "Plan escrito de lo que se mostrará y dirá en cada escena", "Organiza el cómic antes de dibujar."),
   ("¿Para qué se anota la fuente en un cómic?", "Para que otras personas comprueben de dónde viene la información", "Así el cómic gana confianza porque se puede comprobar."),
   ("¿Cuántas escenas tiene el cómic de esta clase?", "4", "Las escenas son inicio, problema, intervención y cierre.")],
  ("Con esta fuente de ejemplo: «Las instituciones públicas deben informar con claridad. Las personas deben pedir información con respeto». Escribe un guion de cuatro escenas (una frase cada una), un globo breve para cada escena y la línea de fuente al pie (usa «Manual de convivencia cívica (ejemplo), 2022»).",
   "Escena 1: una persona llega a una oficina. Escena 2: no entiende un formulario. Escena 3: la funcionaria explica con claridad. Escena 4: la persona agradece. Fuente: Manual de convivencia cívica (ejemplo), 2022.",
   ["cuatro escenas en orden", "globos breves", "fuente anotada al pie"],
   ["guion escrito o boceto de las cuatro viñetas"],
   ["globos demasiado largos", "olvidar la fuente"],
   "Pregunta: «¿Cada viñeta cuenta una parte distinta de la idea?»."),
  "Cuenta las palabras de uno de tus globos y acórtalo si pasa de diez.",
  "Convierte otra idea de convivencia en un guion de cuatro escenas.")

# ====================================================== clase 4
F = ("Ficha 4 (cómic de ejemplo «El ruido de la obra», cuatro viñetas descritas). "
     "Viñeta 1: una vecina escribe una carta a la municipalidad: «Hay ruido de una obra desde muy temprano». "
     "Viñeta 2: un funcionario municipal responde: «Registramos su reclamo y revisaremos los horarios permitidos». "
     "Viñeta 3: el encargado de la obra dice: «Perdón, ajustaremos el horario». "
     "Viñeta 4: la vecina dice: «Gracias por responder; avisaré si el problema continúa». "
     "Fuente al pie: Manual de convivencia cívica (ejemplo), 2022.")
K(4, F,
  "Hoy practico identificar en un cómic de cuatro viñetas el derecho que se ejerce, el deber de la institución y las responsabilidades de las personas.",
  ["Leer un cómic con atención significa mirar las viñetas en orden y buscar quién hace qué. En «El ruido de la obra», una vecina presenta un reclamo por escrito. Ejerce su derecho a ser escuchada y a vivir sin ruido excesivo.",
   "La municipalidad cumple un deber del Estado cuando recibe el reclamo, lo registra y responde. El encargado de la obra asume una responsabilidad al aceptar ajustar el horario. La vecina también: reclama con respeto y se compromete a informar si el problema sigue.",
   "Practicar significa señalar en cada viñeta qué idea aparece. Una misma viñeta puede mostrar más de una idea. Y siempre se verifica con lo que dicen los globos, no con lo que uno supone. La fuente al pie respalda la información."],
  [("reclamo", "pedido formal para que se atienda un problema"), ("registrar", "anotar algo para que quede constancia"), ("constancia", "prueba escrita de que algo ocurrió o se pidió"), ("compromiso", "promesa de hacer algo")],
  [("Ubicar el derecho", "Viñeta 1: la vecina presenta un reclamo por escrito. ¿Qué derecho ejerce?", ["Pide ser escuchada.", "Eso es el derecho a presentar peticiones y ser respondida."], "Pedir y ser escuchada"),
   ("Ubicar el deber", "Viñeta 2: el funcionario registra el reclamo y promete revisar. ¿Qué deber cumple la institución?", ["Atiende y responde a la persona.", "Eso es parte del servicio público."], "Atender y responder al reclamo")],
  [("Decir que la vecina no tiene responsabilidades porque solo reclama.", "Se olvida que reclamar con respeto y colaborar también son responsabilidades.", "Observa lo que ella promete y cómo habla."),
   ("Suponer lo que ocurre sin mirar los globos.", "Se interpreta con ideas previas y no con el texto.", "Apóyate en lo que dicen los personajes.")],
  [("abc", "{F} ¿Qué hace la vecina en la viñeta 1?", "Escribe una carta de reclamo a la municipalidad", "Grita en la calle", "Ignora el ruido", "El globo de la viñeta 1 describe una carta de reclamo."),
   ("ab", "{F} ¿Qué dice el funcionario en la viñeta 2?", "Que registra el reclamo y revisará los horarios", "Que no puede hacer nada", "El funcionario promete registrar y revisar los horarios permitidos."),
   ("abc", "{F} ¿Qué se compromete a hacer el encargado de la obra en la viñeta 3?", "Ajustar el horario", "Cerrar la obra para siempre", "Trabajar más ruidosamente", "El encargado dice «ajustaremos el horario» en su globo."),
   ("abc", "{F} ¿Qué responsabilidad asume la vecina en la viñeta 4?", "Agradecer e informar si el problema continúa", "Dejar de reclamar siempre", "Amenazar al encargado", "Se compromete a avisar si el ruido sigue."),
   ("abc", "{F} ¿Qué viñeta muestra el agradecimiento y el compromiso de la vecina?", "la viñeta 4", "la viñeta 2", "la viñeta 3", "En la viñeta 4 la vecina agradece y dice que avisará si el problema continúa."),
   ("abc", "{F} ¿Qué problema denuncia la vecina en la viñeta 1?", "el ruido de una obra desde muy temprano", "el humo de una fábrica", "la basura de la calle", "La carta dice que hay ruido de una obra desde muy temprano."),
   ("ab", "{F} ¿La viñeta 3 muestra una actitud cívica?", "Sí, reconoce el problema y propone ajustar el horario", "No, ignora el problema", "El encargado reconoce el reclamo y se compromete a cambiar."),
   ("abc", "{F} ¿Cuál es la fuente anotada al pie?", "Manual de convivencia cívica (ejemplo), 2022", "Un mensaje de chat", "Un afiche sin autor", "La ficha la anota al pie del cómic."),
   ("{F} ¿Cuántos personajes distintos hablan en las cuatro viñetas?", "3", "Los globos pertenecen a tres personajes: la vecina, el funcionario y el encargado."),
   ("abc", "Si el funcionario hubiera respondido «ese no es mi trabajo» y no hubiera registrado nada, ¿qué deber habría incumplido?", "Atender y responder el reclamo", "Cuidar la plaza", "Votar en una elección", "Un servicio público debe recibir y orientar a la persona que reclama."),
   ("ab", "Si la vecina hubiera insultado al funcionario, ¿qué responsabilidad no habría cumplido?", "Reclamar con respeto", "Pagar una multa", "Insultar rompe el respeto que se debe a todas las personas."),
   ("abc", "¿Qué cambiaría al cómic si la vecina no hubiera dejado constancia escrita de su reclamo?", "Costaría más comprobar que reclamó", "Nada en absoluto", "Se acabaría el ruido", "La constancia sirve de prueba de que se hizo el reclamo."),
   ("abc", "Un lector dice que el cómic muestra que la municipalidad debe obedecer sin límites a cualquier vecina. ¿Qué observación es correcta?", "El cómic muestra que atiende un reclamo y revisa los horarios permitidos", "Es correcto: obedece a cualquiera", "El cómic no menciona a la municipalidad", "La institución actúa según los horarios permitidos, no por capricho.")],
  ("abc", "Una persona ve un cómic en el que un vecino deja su basura en la plaza y otro la recoge. ¿Qué idea de democracia se muestra mejor?", "El cuidado de lo común es responsabilidad compartida", "El Estado decide todo sin las personas", "Los derechos solo existen para unos pocos", "Recoger basura muestra un compromiso personal con el espacio de todos."),
  [("En Historia: ¿qué es un reclamo?", "Un pedido formal para que se atienda un problema", "Se presenta con respeto y, si se puede, por escrito."),
   ("¿Qué es una constancia?", "Prueba escrita de que algo ocurrió o se pidió", "Sirve para comprobar que se hizo un reclamo."),
   ("¿Qué deber cumple una institución cuando responde un reclamo?", "Atender y responder a la persona", "Es parte del servicio que presta.")],
  ("Lee este cómic de ejemplo: Viñeta 1: un vecino pide por escrito reparar una luminaria. Viñeta 2: la municipalidad registra el pedido y da un plazo estimado de ejemplo. Viñeta 3: el vecino agradece y avisa a otro vecino. Viñeta 4: la luminaria se arregla. Escribe el derecho, el deber de la institución y la responsabilidad del vecino, citando la viñeta de cada uno.",
   "Derecho: pedir y ser escuchado (viñeta 1). Deber de la institución: registrar y responder (viñeta 2). Responsabilidad: pedir con respeto y colaborar (viñetas 1 y 3).",
   ["identifica los tres elementos", "cita la viñeta de cada uno", "usa lo que dicen los globos"],
   ["tres frases con el número de viñeta"],
   ["no citar la viñeta", "mezclar institución y persona"],
   "Pregunta: «¿En qué viñeta lo veo?»."),
  "Cambia un globo del cómic para que la vecina reclame con más respeto.",
  "Escribe qué faltaría si la municipalidad no respondiera.")

# ====================================================== clase 5
F = ("Ficha 5 (situación de comunidad y cómic de ejemplo «La sede de la junta de vecinos»). "
     "Situación: la sede de una junta de vecinos tiene una gotera. Se quiere explicar con un cómic cómo participan los vecinos y qué debe hacer el municipio. "
     "Viñeta 1: tres vecinos observan la gotera. Viñeta 2: escriben una carta al municipio con la descripción del problema. "
     "Viñeta 3: el municipio envía a una persona a revisar. Viñeta 4: los vecinos limpian la sede antes de la reparación. "
     "Fuentes de ejemplo: A) «Manual de convivencia cívica (ejemplo), 2022», con autor y fecha; B) mensaje anónimo que dice que «el municipio nunca arregla nada». "
     "Globos de ejemplo: «Escribamos al municipio», «Gracias por venir a revisar», «Dejemos todo despejado».")
K(5, F,
  "Hoy aplico lo aprendido a una situación de comunidad: armo un cómic que muestre derechos, deberes del Estado y responsabilidades, usando una fuente confiable.",
  ["Una gotera en la sede del barrio es un problema común. Un cómic puede mostrar cómo los vecinos ejercen su derecho a pedir una solución, cómo el municipio cumple su deber de atender y cómo las personas colaboran con su responsabilidad de cuidar la sede.",
   "Para que el cómic sea confiable, la información debe venir de una fuente con autor y fecha, no de un mensaje anónimo que exagera. Si dos fuentes se contradicen, se contrasta con otra. Además, los globos deben ser respetuosos y claros.",
   "Al aplicar, ordena las escenas, elige una fuente, escribe globos breves y revisa que se vean las tres ideas: derecho, deber del Estado y responsabilidad. No hace falta que el municipio resuelva todo de inmediato: lo importante es mostrar cómo funciona el diálogo entre personas e instituciones."],
  [("gotera", "filtración de agua por el techo"), ("diálogo", "conversación en que las partes se escuchan y buscan acuerdos"), ("colaborar", "trabajar junto a otras personas"), ("contradecirse", "decir cosas que no pueden ser ciertas a la vez")],
  [("Elegir la fuente", "Fuente A tiene autor y fecha; fuente B es un mensaje anónimo. ¿Cuál usas para el cómic?", ["Reviso autor y fecha.", "La fuente A los muestra."], "La fuente A"),
   ("Ubicar una responsabilidad", "Viñeta 4: los vecinos limpian la sede antes de la reparación. ¿Qué responsabilidad muestran?", ["Colaboran con el trabajo.", "Cuidan un espacio común."], "Colaborar y cuidar lo común")],
  [("Usar la fuente anónima porque es más llamativa.", "No se puede comprobar quién lo dice ni cuándo.", "Elige la fuente con autor y fecha."),
   ("Mostrar solo la queja y no la colaboración.", "Se omite la responsabilidad de las personas.", "Incluye qué hacen las personas además de reclamar.")],
  [("abc", "{F} ¿Qué problema se quiere explicar con el cómic?", "Una gotera en la sede de la junta de vecinos", "Un corte de luz en una escuela", "La falta de transporte", "La situación describe la gotera en la sede."),
   ("ab", "{F} En la viñeta 2, los vecinos escriben una carta al municipio. ¿Qué derecho ejercen?", "Presentar una petición", "Votar en elecciones", "Una carta al municipio es una forma de petición y de participación."),
   ("abc", "{F} ¿Qué deber del Estado se ve en la viñeta 3?", "Atender el pedido enviando a revisar", "Cobrar a los vecinos", "Ignorar la carta", "El municipio envía a una persona a revisar la gotera."),
   ("abc", "{F} ¿Qué hacen los tres vecinos en la viñeta 1?", "observan la gotera", "limpian la sede", "escriben una carta", "En la viñeta 1 los vecinos observan la gotera; escribir la carta es la viñeta 2."),
   ("abc", "{F} ¿Cuántas viñetas tiene el cómic de la ficha?", "4", "3", "6", "La ficha describe las viñetas 1, 2, 3 y 4."),
   ("abc", "{F} ¿Por qué no conviene usar la fuente B?", "No se puede comprobar quién lo dice y exagera", "Porque es breve", "Porque es muy ordenada", "Dice que «nunca arregla nada» sin pruebas ni autor."),
   ("{F} ¿Cuántos globos de ejemplo se ofrecen en la ficha?", "3", "Se listan tres: «Escribamos al municipio», «Gracias por venir a revisar» y «Dejemos todo despejado»."),
   ("abc", "{F} ¿Qué globo corresponde mejor a la viñeta 2?", "«Escribamos al municipio»", "«Gracias por venir a revisar»", "«Dejemos todo despejado»", "En la viñeta 2 los vecinos redactan la carta."),
   ("abc", "{F} ¿Qué globo corresponde mejor a la viñeta 4?", "«Dejemos todo despejado»", "«Escribamos al municipio»", "«Gracias por venir a revisar»", "En la viñeta 4 los vecinos limpian y despejan."),
   ("ab", "Una persona propone terminar el cómic diciendo «los vecinos se enojan con todos». ¿Es adecuado?", "No, no refleja el diálogo respetuoso del cómic", "Sí, es lo más realista", "El cómic muestra diálogo y colaboración, no enojo generalizado."),
   ("abc", "Si el municipio no respondiera a la carta, ¿qué podrían hacer los vecinos de manera respetuosa?", "Volver a pedir respuesta por escrito y buscar otra instancia", "Dañar la oficina", "Dejar la sede sin cuidado", "Insistir con respeto es una vía de participación."),
   ("abc", "Dos fuentes dan datos distintos sobre los plazos de respuesta del municipio. ¿Qué haces?", "Contrastar con la información oficial del municipio", "Elegir la que más te guste", "Inventar un plazo", "Se contrasta con una fuente institucional."),
   ("abc", "¿Qué debe mostrar el cierre del cómic para ser coherente con la idea de democracia?", "Que personas e instituciones colaboran con respeto", "Que una parte vence a la otra", "Que nadie hace nada", "La democracia se apoya en diálogo y colaboración.")],
  ("abc", "Una organización comunitaria arma un cómic sobre cuidar una plaza. Tiene una fuente institucional con fecha y un mensaje anónimo que exagera. ¿Qué decisión es correcta?", "Usar la fuente institucional y no el mensaje anónimo", "Usar solo el mensaje anónimo", "Mezclar ambos sin revisar", "La fuente con autor y fecha permite comprobar la información."),
  [("En Historia: ¿qué es el diálogo?", "Conversación en que las partes se escuchan y buscan acuerdos", "Es una forma de convivir en democracia."),
   ("En un cómic sobre la comunidad, ¿qué es colaborar?", "Trabajar junto a otras personas", "Las responsabilidades de las personas se cumplen colaborando."),
   ("¿Qué conviene hacer si dos fuentes se contradicen?", "Contrastar con otra fuente confiable", "Así se decide qué dato es correcto.")],
  ("Arma un cómic de cuatro viñetas para esta situación de ejemplo: «una vereda con un hoyo peligroso en un barrio». Escribe una frase por viñeta, un globo breve por viñeta y la fuente al pie (usa «Manual de convivencia cívica (ejemplo), 2022»). Debe verse un derecho, un deber de la institución y una responsabilidad de las personas.",
   "V1: vecinos ven el hoyo. V2: escriben al municipio. V3: el municipio revisa. V4: los vecinos señalan el lugar mientras tanto. Fuente: Manual de convivencia cívica (ejemplo), 2022.",
   ["cuatro viñetas con globos breves", "se ven derecho, deber del Estado y responsabilidad", "fuente anotada al pie"],
   ["borrador del cómic con cuatro viñetas"],
   ["no mostrar la responsabilidad de las personas", "globos largos"],
   "Pregunta: «¿En cuál viñeta se ve cada una de las tres ideas?»."),
  "Revisa que cada viñeta tenga una sola idea.",
  "Haz una versión del cómic para otro problema de tu comunidad.")

# ====================================================== clase 6
F = ("Ficha 6 (pauta de revisión de un cómic, un punto por criterio). 1) Parte de una fuente con autor y fecha. 2) Tiene cuatro viñetas ordenadas. "
     "3) Muestra un derecho. 4) Muestra un deber de una institución. 5) Muestra una responsabilidad de las personas. 6) Los globos son breves y respetuosos. "
     "Cómic revisado: viñeta 1, un vecino ve una luz apagada; viñeta 2, escribe a la municipalidad; viñeta 3, la municipalidad la repara; viñeta 4, el vecino agradece. "
     "Fuente al pie: «un mensaje que me llegó» sin autor ni fecha. Los globos son breves y respetuosos. No hay una escena que muestre una acción de los vecinos por el bien común distinta de reclamar.")
K(6, F,
  "Hoy reviso mi cómic con una pauta, corrijo lo que falta y decido qué voy a seguir practicando.",
  ["Revisar un cómic es comparar lo hecho con criterios claros. La pauta de seis puntos mira la fuente, el orden de las viñetas, el derecho, el deber de la institución, la responsabilidad de las personas y la claridad de los globos.",
   "Marca sí o no en cada criterio, suma los puntos y escribe una mejora concreta por cada no. Por ejemplo: «cambiar la fuente por una con autor y fecha» o «agregar una viñeta donde los vecinos cuiden lo común». Una mejora concreta indica qué cambiar y dónde.",
   "Para cerrar el módulo, recuerda lo esencial: los derechos humanos valen para todas las personas, el Estado tiene deberes para que se cumplan, y las personas tenemos responsabilidades de respeto y cuidado de lo común. Decide qué seguirás practicando."],
  [("pauta", "lista de criterios para revisar un trabajo"), ("criterio", "regla para decidir si algo está bien hecho"), ("mejora concreta", "cambio específico que hace mejor un trabajo"), ("balance", "mirada final de lo logrado y lo que falta")],
  [("Contar puntos", "Un cómic cumple los criterios 1, 2, 3, 4 y 6. ¿Cuántos puntos tiene de seis?", ["Cuento los sí.", "Son cinco."], "5 de 6"),
   ("Escribir una mejora", "El cómic no muestra una responsabilidad de las personas. ¿Qué mejora escribes?", ["Digo qué falta.", "Propongo una viñeta concreta."], "Agregar una viñeta en que los vecinos cuidan lo común")],
  [("Marcar sí sin mirar el cómic.", "No se compara con la pauta.", "Marca cada criterio con un dato del trabajo."),
   ("Escribir «hacerlo mejor» como mejora.", "No indica qué cambiar.", "Escribe una acción concreta.")],
  [("abc", "{F} ¿Cuántos criterios tiene la pauta?", "6", "4", "8", "La ficha de revisión numera seis criterios en total."),
   ("ab", "{F} ¿El cómic revisado cumple el criterio 2, cuatro viñetas ordenadas?", "Sí", "No", "El cómic describe cuatro viñetas en una secuencia ordenada."),
   ("abc", "{F} ¿Qué criterio incumple el cómic revisado por su fuente?", "El 1", "El 6", "El 3", "La fuente no tiene autor ni fecha."),
   ("abc", "{F} ¿Qué criterio incumple por no mostrar una acción de los vecinos distinta de reclamar?", "El 5", "El 2", "El 4", "Falta la responsabilidad de las personas por el bien común."),
   ("{F} ¿Cuántos puntos obtiene el cómic revisado?", "4", "Cumple los criterios 2, 3, 4 y 6 y no cumple el 1 ni el 5, que suman cuatro puntos."),
   ("abc", "{F} ¿Qué viñeta muestra el deber de una institución?", "La viñeta 3, la municipalidad repara la luz", "La viñeta 1, el vecino ve la luz", "La viñeta 4, el vecino agradece", "La municipalidad es la institución que actúa en la viñeta 3."),
   ("abc", "{F} ¿Qué viñeta muestra el derecho a pedir una solución?", "La viñeta 2, escribe a la municipalidad", "La viñeta 1", "La viñeta 4", "Escribir una petición ejerce ese derecho."),
   ("abc", "{F} ¿Qué mejora arregla el criterio 1?", "Cambiar la fuente por una con autor y fecha", "Cambiar el color de los globos", "Quitar la viñeta 3", "La fuente confiable muestra quién la hizo y cuándo."),
   ("abc", "{F} ¿Qué viñeta podría agregarse para cumplir el criterio 5?", "Los vecinos señalizan el lugar y cuidan el espacio mientras esperan la reparación", "La municipalidad no responde", "Un vecino insulta al funcionario", "Es una acción de las personas por el bien común."),
   ("abc", "Si el cómic revisado corrigiera los criterios 1 y 5, ¿cuántos puntos tendría?", "6", "5", "4", "Se sumarían los dos puntos que faltaban a los cuatro obtenidos."),
   ("ab", "Una persona dice que revisar es solo decir si gustó o no. ¿Qué respuesta es correcta?", "Revisar es comparar con una pauta y escribir mejoras concretas", "Sí, basta con que guste", "Revisar con criterios permite saber qué corregir y justificarlo."),
   ("abc", "¿Cuál de estas frases resume mejor lo aprendido en este módulo?", "Los derechos valen para todas las personas, el Estado debe asegurarlos y las personas debemos respetarlos", "Los derechos son favores", "Solo las instituciones tienen tareas", "Recoge la relación entre derechos, deberes del Estado y responsabilidades."),
   ("abc", "Después de revisar un cómic, ¿cuál es un próximo paso razonable?", "Mostrarlo a otra persona y recoger sus comentarios", "Guardarlo sin revisarlo", "Cambiar el tema sin motivo", "Un comentario externo ayuda a mejorar.")],
  ("abc", "Un grupo de personas prepara un cómic para una campaña de convivencia. Cumple 5 de 6 criterios y le falta la fuente confiable. ¿Qué hace?", "Reemplaza la fuente por una con autor y fecha antes de compartirlo", "Lo comparte sin cambios", "Elimina las viñetas", "La mejora concreta lo lleva a los seis puntos."),
  [("En Historia: ¿qué es una pauta?", "Lista de criterios para revisar un trabajo", "Permite revisar un trabajo con orden y criterios compartidos."),
   ("¿Qué es una mejora concreta?", "Un cambio específico que mejora el trabajo", "Una mejora concreta dice qué cambiar y dónde hacerlo."),
   ("¿Qué muestra un cómic sobre derechos y deberes?", "Quién ejerce un derecho, qué debe hacer la institución y qué hacen las personas", "Son las tres ideas centrales de esta etapa.")],
  ("Revisa con la pauta este cómic de ejemplo: «Fuente: Manual de convivencia cívica (ejemplo), 2022. V1: una persona llega a una oficina. V2: pide información con respeto. V3: la funcionaria explica los pasos. V4: la persona agradece». Marca sí o no en cada uno de los seis criterios, suma los puntos y escribe una mejora para cada no.",
   "Criterios 1, 2, 3 (pide información), 4 (la institución informa) y 6: sí. Criterio 5: no hay una acción de cuidado de lo común. Puntos: 5. Mejora: agregar una viñeta donde la persona ayude a otra a entender el trámite.",
   ["marca los seis criterios con razones", "suma bien", "escribe una mejora concreta por cada no"],
   ["pauta marcada con las mejoras"],
   ["marcar sin razones", "mejoras vagas"],
   "Pregunta: «¿Qué cambio haría que este criterio pase de no a sí?»."),
  "Escribe dos aprendizajes de este módulo sobre derechos y deberes.",
  "Piensa cómo explicarías en un cómic de cuatro viñetas una responsabilidad que valoras en tu comunidad.")
