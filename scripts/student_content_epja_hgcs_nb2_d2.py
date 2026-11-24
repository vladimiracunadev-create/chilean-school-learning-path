"""Historia, Geografía y Ciencias Sociales EPJA Básica N2, módulo 4 (parte 2): OAD-14, seleccionar fuentes y evaluar su fiabilidad para caracterizar la democracia, la participación y representación y la organización político-administrativa de Chile mediante un debate. Todo en papel; datos de ejemplo rotulados."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz y goma. Todo se resuelve con lo escrito en la ficha: las fuentes, tablas y argumentos son de ejemplo y no se usa internet."
build = make_build(MATERIALS)

O = "EPJA-HGCS-NB2-OAD-14"
PRIOR = ["Ya me informo por conversaciones, noticias, carteles y mensajes.", "Sé que en Chile se vota para elegir autoridades."]


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    build(O, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ====================================================== clase 1
F = ("Ficha 1 (pregunta de debate de ejemplo: «¿Cómo podemos participar en las decisiones de nuestra comuna?»). "
     "Fuente 1: página de la municipalidad (ejemplo) con la lista de organizaciones comunitarias y las fechas de reuniones abiertas. "
     "Fuente 2: entrevista oral a una dirigente de una junta de vecinos sobre cómo se organizan los vecinos. "
     "Fuente 3: afiche de una elección pasada que solo muestra el rostro de una persona candidata. "
     "Fuente 4: video de una receta de cocina. Fuente 5: texto de un libro de educación cívica sobre formas de participación.")
K(1, F,
  "Hoy reconozco distintos tipos de fuente y elijo, entre varias, las que sirven para responder una pregunta sobre cómo participar en la democracia.",
  ["Una fuente es el lugar o la persona de donde viene una información. Tú ya usas fuentes todos los días: preguntas a un vecino, lees un cartel, miras las noticias, escuchas un aviso. Hoy aprendemos a elegir cuáles sirven para responder una pregunta concreta.",
   "Las fuentes pueden ser orales (una entrevista o una conversación), escritas (un libro, una página o un documento), visuales (un afiche o una fotografía) y audiovisuales (un video). Una fuente es relevante cuando ayuda a responder la pregunta que nos hacemos.",
   "Para seleccionar bien, primero se lee la pregunta, después se mira qué dice cada fuente y se descartan las que hablan de otro tema. No importa si la fuente es larga o llamativa: importa si aporta información útil para el tema."],
  [("fuente", "lugar o persona de donde viene una información"), ("relevante", "que sirve para responder la pregunta que nos hacemos"), ("fuente oral", "información que se recibe hablando, como una entrevista"), ("participar", "tomar parte en las decisiones y actividades de una comunidad")],
  [("Elegir una fuente relevante", "Pregunta: «¿Cuándo son las reuniones abiertas de la municipalidad?». Hay una página de la municipalidad con fechas y un video de cocina. ¿Cuál sirve?", ["Leo la pregunta: busca fechas de reuniones.", "La página las trae; el video habla de otro tema."], "La página de la municipalidad"),
   ("Clasificar el tipo de fuente", "Una persona entrevista a un funcionario y graba su voz. ¿Qué tipo de fuente es?", ["La información viene hablando.", "No es un texto ni una imagen."], "Fuente oral")],
  [("Elegir la fuente más larga o la más llamativa.", "Se mira el tamaño y el color, no el tema.", "Pregúntate: ¿responde mi pregunta?"),
   ("Usar solo una fuente aunque haya varias relevantes.", "Se pierde la oportunidad de comparar.", "Reúne dos o tres fuentes relevantes para contrastar.")],
  [("abc", "{F} ¿Qué tipo de fuente es la entrevista a la dirigente de la junta de vecinos (fuente 2)?", "Oral", "Visual", "Escrita", "La información se recibe hablando, por eso es una fuente oral."),
   ("ab", "{F} ¿Qué tipo de fuente es el afiche de la elección pasada (fuente 3)?", "Visual", "Oral", "Un afiche es una imagen con poco texto, es decir, una fuente visual."),
   ("abc", "{F} ¿Cuál es la pregunta de debate de la ficha?", "¿Cómo podemos participar en las decisiones de nuestra comuna?", "¿Quién ganó la última elección?", "¿Cómo se hace una receta?", "La ficha comienza con la pregunta que se quiere responder."),
   ("abc", "{F} ¿Cuál fuente NO sirve para responder la pregunta de debate?", "Fuente 4, el video de cocina", "Fuente 1, la página de la municipalidad", "Fuente 5, el libro de educación cívica", "Una receta no habla de participar en decisiones de la comuna."),
   ("{F} ¿Cuántas de las cinco fuentes sirven para responder la pregunta de debate?", "3", "Las fuentes 1, 2 y 5 hablan de organizaciones, vecinos y formas de participar; la 3 y la 4 no."),
   ("abc", "{F} ¿Por qué la fuente 3, el afiche del rostro, aporta poco a la pregunta?", "Porque no explica cómo se puede participar", "Porque es muy antigua", "Porque tiene colores", "Muestra solo un rostro y no explica ninguna forma de participación."),
   ("ab", "{F} Si necesitas fechas de reuniones abiertas, ¿qué fuente conviene?", "Fuente 1, la página de la municipalidad", "Fuente 4, el video de cocina", "La página lista las fechas de reuniones; el video no habla del tema."),
   ("abc", "Una persona dice: «Si el texto es largo, es mejor fuente». ¿Qué respuesta es correcta?", "Una fuente es mejor si ayuda a responder la pregunta", "Sí, lo largo siempre aporta más", "Solo importa el color de la hoja", "La utilidad depende del tema, no del tamaño."),
   ("abc", "Quieres saber cómo se organizan los vecinos de un barrio. ¿Cuál fuente es la más directa?", "Una entrevista a una dirigente de la junta de vecinos", "Una receta de cocina", "Un afiche sin texto", "La persona que participa en la organización conoce cómo funciona."),
   ("ab", "Para responder «¿qué formas de participación existen?», ¿es mejor combinar fuentes 1, 2 y 5 o usar solo la 3?", "Combinar fuentes 1, 2 y 5", "Usar solo la 3", "Varias fuentes relevantes dan más información y permiten compararla."),
   ("abc", "Dos fuentes relevantes dan la misma fecha de una reunión. ¿Qué indica eso?", "Que el dato se fortalece por coincidir", "Que ambas están equivocadas", "Que no sirve ninguna", "Si dos fuentes distintas coinciden, es más probable que el dato sea correcto."),
   ("abc", "Alguien busca el significado de «representar» y solo encuentra un video de baile. ¿Qué hace?", "Busca una fuente escrita que lo defina", "Usa el video de todas formas", "No busca más", "Debe buscar otra fuente que sí hable del tema."),
   ("abc", "Se quiere decidir si una fuente es útil para el tema «participación en la comuna». ¿Cuál es la primera pregunta?", "¿Habla del tema que quiero investigar?", "¿Cuántas páginas tiene?", "¿De qué color es la portada?", "Primero se comprueba que el contenido se relacione con la pregunta.")],
  ("abc", "Una organización vecinal prepara un debate sobre la participación en la comuna. ¿Qué conjunto de fuentes le conviene reunir?", "La lista de organizaciones del municipio, una entrevista a una dirigente y un libro de educación cívica", "Tres recetas y un afiche sin texto", "Solo un mensaje reenviado", "Cada una de las tres aporta información sobre participación."),
  [("En Historia: ¿qué es una fuente?", "Lugar o persona de donde viene una información", "Puede ser oral, escrita, visual o audiovisual."),
   ("¿Cuándo una fuente es relevante?", "Cuando ayuda a responder la pregunta", "Se compara su contenido con el tema de la pregunta."),
   ("¿Qué tipo de fuente es una entrevista?", "Oral", "La información se recibe hablando con una persona.")],
  ("Pregunta: «¿Qué organizaciones de un barrio permiten participar?». Fuentes de ejemplo: (a) lista de organizaciones de una municipalidad, (b) entrevista a una presidenta de un club deportivo, (c) video de un partido, (d) afiche de una feria. Escribe cuáles elegirías, cuáles descartarías y por qué, y qué tipo de fuente es cada una.",
   "Elijo (a) escrita y (b) oral porque hablan de organizaciones. Descarto (c) y (d) porque no explican cómo participar.",
   ["elige fuentes que responden la pregunta", "da una razón para cada descarte", "dice el tipo de cada fuente"],
   ["lista escrita con elegidas, descartadas y tipo de fuente"],
   ["elegir por llamativas", "no decir por qué se descarta"],
   "Pregunta: «¿Esta fuente responde la pregunta o habla de otra cosa?»."),
  "Anota dos fuentes que usas a diario para informarte y di qué tipo son.",
  "Escribe una pregunta sobre tu comuna y tres fuentes que podrías consultar.")

# ====================================================== clase 2
F = ("Ficha 2 (glosario de ejemplo). Democracia: forma de organizar un país en la que las personas eligen a sus autoridades y sus derechos son respetados. "
     "Elección: momento en que las personas votan para elegir autoridades. Voto: forma de expresar una decisión en una elección. "
     "Representante: persona elegida para decidir en nombre de otras. Participación: tomar parte en las decisiones de la comunidad. "
     "Frases de ejemplo: A) «La junta de vecinos eligió a su directiva por votación». B) «Una vecina pidió por escrito más luz en la plaza». "
     "C) «En el país se elige cada cierto tiempo a quien presidirá». D) «Un grupo decidió no ir a la reunión y se quejó después».")
K(2, F,
  "Hoy aprendo las palabras clave de la democracia: elección, voto, representación y participación, para poder hablar de ellas con precisión.",
  ["La democracia es una forma de organizar un país en la que las personas eligen a sus autoridades y sus derechos son respetados. Chile se organiza así. Tú ya has vivido elecciones pequeñas: elegir una directiva, votar en un grupo o decidir entre varias opciones.",
   "En una elección, las personas votan para elegir a quienes ocuparán cargos. Esas personas son representantes: deciden en nombre de otras. Pero la democracia no termina en el voto: también se participa en organizaciones, reuniones, peticiones y consultas.",
   "En Chile pueden votar las personas desde los 18 años que cumplan los requisitos de la ley. El voto es secreto: nadie debe presionarte ni saber por quién votaste. Estas palabras te servirán para el debate de las próximas clases."],
  [("democracia", "forma de organizar un país en que las personas eligen autoridades y sus derechos se respetan"), ("elección", "momento en que las personas votan para elegir autoridades"), ("representante", "persona elegida para decidir en nombre de otras"), ("participación", "tomar parte en las decisiones de la comunidad")],
  [("Definir con palabras simples", "Una junta de vecinos vota para elegir presidenta. ¿Qué palabra describe a la persona elegida?", ["La votación elige a una persona.", "Esa persona decidirá en nombre de los vecinos."], "Representante"),
   ("Distinguir representación y participación", "Una vecina entrega por escrito una petición al municipio. ¿Es representación o participación?", ["Ella misma toma parte en un asunto de la comunidad.", "No elige a otra persona para hacerlo."], "Participación")],
  [("Creer que la democracia es solo votar cada cierto tiempo.", "Se olvida la participación diaria en organizaciones y peticiones.", "Piensa en votar y en participar entre elecciones."),
   ("Pensar que el voto debe decirse en voz alta.", "Se confunde el voto con una opinión pública.", "El voto es secreto: nadie puede obligarte a decir por quién votaste.")],
  [("abc", "{F} ¿Qué es un representante?", "Persona elegida para decidir en nombre de otras", "Persona que no vota nunca", "Persona que escribe la ley sin elección", "Según el glosario, un representante es elegido para decidir en nombre de otras personas."),
   ("ab", "{F} La frase A, «La junta de vecinos eligió a su directiva por votación», ¿muestra una elección?", "Sí", "No", "Hubo una votación para elegir a personas que ocuparán cargos."),
   ("abc", "{F} ¿Qué frase muestra una forma de participación mediante una petición?", "B, la petición por escrito para más luz", "A, la elección de la directiva", "D, quien se queja sin ir", "La vecina intervino en un asunto de la comunidad con una petición."),
   ("abc", "¿Desde qué edad pueden votar las personas en Chile, si cumplen los requisitos de la ley?", "Desde los 18 años", "Desde los 14 años", "Desde los 25 años", "La explicación indica que votan quienes cumplen los requisitos desde los 18 años."),
   ("abc", "{F} ¿Qué frase muestra una falta de participación?", "D, un grupo decidió no ir y se quejó después", "A, la votación de la directiva", "B, la petición por escrito", "Quien no asiste a la reunión pierde la oportunidad de opinar."),
   ("ab", "¿El voto es secreto?", "Sí, nadie debe presionar ni exigir saber por quién se votó", "No, debe decirse en voz alta", "El secreto del voto protege la libertad de decidir."),
   ("abc", "{F} ¿Qué frase del glosario describe mejor una democracia?", "Las personas eligen autoridades y se respetan sus derechos", "Una sola persona decide sin consultar", "Nadie puede opinar", "Combina la elección de autoridades con el respeto de los derechos."),
   ("abc", "Una persona dice: «Con votar una vez, ya cumplí todo en la democracia». ¿Qué falta en su idea?", "Participar entre elecciones, por ejemplo en organizaciones", "Nada, porque el voto lo es todo", "Dejar de opinar", "La democracia incluye participación continua además del voto."),
   ("abc", "{F} La frase C dice que en el país se elige cada cierto tiempo a quien presidirá. ¿Qué idea muestra?", "Que las autoridades se eligen y no se heredan", "Que el cargo es para siempre", "Que no hay elecciones", "Elegir cada cierto tiempo es una característica de la democracia."),
   ("ab", "Un grupo de vecinos elige a tres personas para hablar con el municipio en su nombre. ¿Qué es esto?", "Representación", "Discriminación", "Se eligió a personas que hablarán en nombre del grupo."),
   ("abc", "Una persona presiona a otra para que vote por cierta opción y vea su voto. ¿Qué principio se rompe?", "El voto secreto", "El derecho a la salud", "La igualdad de género", "Presionar a alguien a mostrar su voto rompe el secreto."),
   ("abc", "¿Cuál es una forma de participación que no es votar?", "Asistir a una reunión de vecinos y opinar", "Esperar en silencio sin ir", "Evitar toda actividad comunitaria", "Opinar en una reunión es tomar parte en las decisiones."),
   ("abc", "Si en un país no hay elecciones y las autoridades no cambian nunca, ¿es una democracia según la definición de la ficha?", "No, falta elegir a las autoridades", "Sí, porque hay autoridades", "Sí, porque hay leyes", "La definición exige que las personas elijan a sus autoridades.")],
  ("abc", "En una reunión, la directiva pide opiniones sobre usar una plaza para una feria. Una persona asiste, opina y vota. ¿Qué hizo?", "Participó en una decisión de la comunidad", "Evitó la democracia", "Se comportó como autoridad", "Asistir, opinar y votar es participar en una decisión común."),
  [("En Historia: ¿qué es una democracia?", "Forma de organizar un país en que las personas eligen sus autoridades y sus derechos se respetan", "Combina elección de autoridades con respeto de derechos."),
   ("¿Qué es un representante?", "Persona elegida para decidir en nombre de otras", "Actúa en nombre de quienes lo eligieron."),
   ("¿Qué quiere decir que el voto es secreto?", "Que nadie puede obligar a decir por quién se votó", "El secreto protege la libertad de decidir sin presiones.")],
  ("Lee estas cuatro frases: (1) Una persona vota en su junta de vecinos. (2) Una vecina escribe una petición al municipio. (3) Una persona asiste a una reunión de la comunidad y opina. (4) Un grupo elige a una vocera. Escribe una columna «elección o voto», otra «participación» y otra «representación» y ubica los números (una frase puede ir en más de una).",
   "Elección o voto: 1. Participación: 2 y 3. Representación: 4, y también 1 si se vota para elegir a alguien.",
   ["ubica las cuatro frases", "justifica una decisión con una razón", "usa las palabras del glosario"],
   ["tabla o lista escrita en el cuaderno"],
   ["confundir participar con votar", "creer que el voto no es secreto"],
   "Pregunta: «¿Aquí se elige a alguien o se toma parte directamente?»."),
  "Escribe una frase con la palabra «representante» y otra con la palabra «participación».",
  "Explica con tus palabras la diferencia entre votar y participar.")

# ====================================================== clase 3
F = ("Ficha 3 (cuatro fuentes de ejemplo sobre cómo se hace una ley). Fuente A: libro de educación cívica con autor, editorial y año de edición; explica las etapas con ejemplos. "
     "Fuente B: mensaje reenviado por chat, sin autor ni fecha, que dice «las leyes las hace una sola persona». "
     "Fuente C: página de una institución pública de ejemplo, con fecha de actualización, que explica quién participa en el proceso. "
     "Fuente D: publicación de una persona que vende un curso y afirma que «nadie te cuenta cómo funciona el Estado», sin citar de dónde saca los datos. "
     "Criterios: 1) muestra autor o institución, 2) muestra fecha, 3) explica de dónde sale la información, 4) no busca vender ni convencer sin pruebas.")
K(3, F,
  "Hoy aprendo, paso a paso, a evaluar si una fuente es fiable con cuatro criterios: autor, fecha, origen de la información y propósito.",
  ["Fiable quiere decir que podemos confiar en la fuente porque se puede comprobar lo que dice. Para evaluarla se hacen cuatro preguntas: ¿quién la hizo?, ¿cuándo?, ¿de dónde sacó la información? y ¿para qué la hizo: informar, vender o convencer?",
   "Una fuente que muestra su autor o institución, su fecha y sus fuentes es más fiable que un mensaje anónimo. El propósito también importa: si alguien quiere vender, puede exagerar. Eso no significa que mienta siempre, pero exige comprobar con otra fuente.",
   "Se evalúa paso a paso: se anota cada criterio con un sí o un no, se cuenta cuántos se cumplen y se decide. Una sola fuente no basta: lo mejor es contrastar al menos dos fuentes antes de usar un dato en un debate."],
  [("fiable", "que se puede comprobar y por eso se puede confiar en ella"), ("autor", "persona o institución que hizo la fuente"), ("propósito", "para qué se hizo la fuente: informar, vender o convencer"), ("contrastar", "comparar lo que dicen dos o más fuentes")],
  [("Aplicar los criterios", "Una página institucional muestra institución, fecha y origen de los datos, y solo informa. ¿Cuántos criterios cumple de 4?", ["Reviso los cuatro criterios uno por uno.", "Cumple los cuatro."], "4 de 4"),
   ("Detectar un propósito", "Un mensaje dice «compra mi curso, nadie te cuenta cómo funciona el Estado». ¿Cuál es su propósito principal?", ["Pide comprar algo.", "Busca vender."], "Vender un curso")],
  [("Creer que una fuente es fiable porque tiene buena presentación.", "Se confunde apariencia con comprobación.", "Revisa autor, fecha, origen y propósito."),
   ("Descartar una fuente solo porque no me gusta lo que dice.", "Se usa la opinión personal como criterio.", "Aplica los mismos criterios a todas las fuentes.")],
  [("abc", "{F} ¿Qué fuente muestra autor, editorial y año?", "Fuente A", "Fuente B", "Fuente D", "El libro de educación cívica identifica autor, editorial y año de edición."),
   ("ab", "{F} ¿La fuente B, el mensaje reenviado, muestra autor y fecha?", "No", "Sí", "La ficha dice que no tiene autor ni fecha."),
   ("abc", "{F} ¿Cuál es el propósito más probable de la fuente D?", "Vender un curso", "Informar con datos comprobables", "Explicar el funcionamiento de una ley", "La persona que escribe vende un curso y no cita sus datos."),
   ("abc", "{F} ¿Qué criterio incumple la fuente D por querer vender un curso?", "el 4", "el 2", "el 1", "El criterio 4 pide no buscar vender ni convencer sin pruebas."),
   ("abc", "{F} ¿Cuántos criterios cumple la fuente B, el mensaje reenviado sin autor ni fecha?", "0", "2", "4", "No muestra autor, ni fecha, ni origen y no aporta pruebas, así que no cumple ninguno."),
   ("abc", "{F} ¿Qué fuente conviene usar para un debate?", "Fuente C, o la A", "Fuente B", "Fuente D", "Las fuentes A y C se pueden comprobar; B y D no."),
   ("ab", "¿Una fuente con buen diseño y colores atractivos es siempre fiable?", "No, la apariencia no prueba que sea cierta", "Sí, el buen diseño garantiza que es verdad", "Hay que revisar autor, fecha, origen y propósito, no solo el diseño."),
   ("abc", "Dos fuentes fiables dicen cosas distintas sobre una fecha. ¿Qué haces?", "Buscar una tercera fuente fiable para contrastar", "Elegir la que más te guste", "Ignorar el dato en silencio", "Contrastar con otra fuente permite decidir cuál dato es correcto."),
   ("abc", "{F} ¿Qué fuente tiene el mismo problema que un afiche sin autor?", "Fuente B", "Fuente A", "Fuente C", "Ambos carecen de autor y fecha, por lo que no se pueden comprobar."),
   ("ab", "Una persona dice: «Si lo dice una institución pública, siempre es perfecto». ¿Tiene razón?", "No, igual conviene contrastar con otra fuente", "Sí, nunca se equivocan", "Las instituciones también pueden tener errores o datos desactualizados."),
   ("abc", "¿Por qué importa la fecha de una fuente?", "Porque la información puede estar desactualizada", "Porque las fechas son bonitas", "Porque define el color", "Una norma o un dato pueden cambiar con el tiempo."),
   ("abc", "Una fuente dice que «el 90 % de las personas está de acuerdo» y no explica de dónde sacó la cifra. ¿Cuál criterio no cumple?", "El origen de la información", "La fecha de la fuente", "El tamaño de las letras", "No dice de dónde viene la cifra, así que no se puede comprobar."),
   ("abc", "Para evaluar una fuente, ¿cuál es el mejor orden de preguntas?", "¿Quién la hizo?, ¿cuándo?, ¿de dónde sacó los datos?, ¿para qué la hizo?", "¿Qué color tiene?, ¿cuánto pesa?", "¿Cuántas personas la compartieron?", "Estas cuatro preguntas son los criterios de fiabilidad de la clase.")],
  ("abc", "Antes de un debate sobre cómo participar en la comuna, una vecina encuentra un mensaje anónimo con cifras y una página de la municipalidad con fecha. ¿Qué debería hacer?", "Usar la página y contrastar el dato del mensaje con otra fuente", "Usar el mensaje, porque trae más cifras", "No usar ninguna", "La página se puede comprobar; el mensaje exige verificación."),
  [("En Historia: ¿qué significa que una fuente sea fiable?", "Que se puede comprobar y por eso se puede confiar en ella", "Cumple criterios como autor, fecha y origen."),
   ("Al evaluar una fuente sobre el Estado, ¿qué es su propósito?", "Para qué se hizo: informar, vender o convencer", "Ayuda a ver si puede exagerar."),
   ("¿Para qué se contrastan fuentes?", "Para comprobar un dato con otra fuente", "Si coinciden, el dato es más seguro.")],
  ("Evalúa estas dos fuentes de ejemplo con los cuatro criterios (autor, fecha, origen de la información, propósito). Fuente 1: boletín de una municipalidad con nombre, fecha y lista de reuniones, que informa. Fuente 2: cadena de mensajes sin nombre, sin fecha, que pide «reenviar a todos». Escribe sí o no en cada criterio, cuenta los puntos y di cuál usarías.",
   "Fuente 1: sí, sí, sí, sí = 4. Fuente 2: no, no, no, no = 0. Usaría la fuente 1.",
   ["aplica los cuatro criterios a las dos fuentes", "cuenta bien los puntos", "decide con una razón"],
   ["tabla de criterios con sí o no para cada fuente"],
   ["decidir por el diseño", "olvidar el propósito"],
   "Pregunta: «¿Puedo comprobar esto con el autor, la fecha y el origen?»."),
  "Evalúa un mensaje que recibiste esta semana con los cuatro criterios.",
  "Escribe qué harías si dos fuentes fiables se contradicen.")

# ====================================================== clase 4
F = ("Ficha 4 (organización político-administrativa de Chile, tabla de ejemplo). "
     "Nivel «País»: lo dirige el Gobierno, con el Presidente o la Presidenta; las leyes se discuten en el Congreso. "
     "Nivel «Región»: Chile está dividido en 16 regiones; cada región tiene un gobierno regional. "
     "Nivel «Provincia»: cada región se divide en provincias. "
     "Nivel «Comuna»: cada provincia se divide en comunas; la administra una municipalidad, con un alcalde o una alcaldesa y un concejo municipal. "
     "Orden de mayor a menor: país, región, provincia, comuna. "
     "Poderes: Ejecutivo (gobierno), Legislativo (Congreso: Cámara de Diputadas y Diputados y Senado) y Judicial (tribunales).")
K(4, F,
  "Hoy practico cómo se organiza Chile: país, regiones, provincias y comunas, quién representa en cada nivel y qué hace cada poder del Estado.",
  ["Chile es un país organizado en niveles. El mayor es el país entero; se divide en 16 regiones; cada región en provincias; y cada provincia en comunas. La comuna es el nivel más cercano a las personas: ahí están la municipalidad y la junta de vecinos.",
   "Cada nivel tiene autoridades. El país lo dirige el Gobierno, con el Presidente o la Presidenta. En la región hay un gobierno regional. En la comuna hay una municipalidad, con un alcalde o una alcaldesa y un concejo municipal. Muchas de estas autoridades se eligen por votación.",
   "Además, el Estado reparte sus funciones en tres poderes. El Ejecutivo gobierna y administra. El Legislativo, el Congreso, discute y aprueba las leyes. El Judicial, los tribunales, resuelve conflictos y aplica las leyes. Separar funciones ayuda a que ninguna persona concentre todo el poder."],
  [("región", "gran división del territorio de Chile; el país tiene 16"), ("comuna", "división más pequeña del territorio; la administra una municipalidad"), ("municipalidad", "institución que administra una comuna, con un alcalde o alcaldesa y un concejo"), ("poder del Estado", "una de las tres funciones del Estado: ejecutivo, legislativo y judicial")],
  [("Ordenar niveles", "Ordena de mayor a menor: comuna, país, provincia, región.", ["El país contiene a todo lo demás.", "Después viene la región, luego la provincia y por último la comuna."], "País, región, provincia, comuna"),
   ("Reconocer un poder", "Un tribunal resuelve un conflicto aplicando la ley. ¿De qué poder se trata?", ["Resolver conflictos con la ley es función de los tribunales.", "Eso corresponde al poder judicial."], "Poder Judicial")],
  [("Creer que la región y la provincia son lo mismo.", "Se confunden dos niveles del territorio.", "Una región contiene varias provincias."),
   ("Pensar que el Congreso gobierna y los tribunales hacen las leyes.", "Se mezclan las funciones de los poderes.", "Congreso: leyes. Gobierno: administrar. Tribunales: resolver conflictos.")],
  [("abc", "{F} ¿Cuántas regiones tiene Chile?", "16", "10", "25", "La ficha indica que Chile está dividido en 16 regiones."),
   ("abc", "{F} ¿Qué nivel es el más pequeño?", "Comuna", "Región", "País", "La comuna es la división más pequeña del territorio."),
   ("ab", "{F} ¿Quién administra una comuna?", "Una municipalidad con alcalde o alcaldesa y concejo", "El Congreso", "La ficha indica que la comuna se administra por una municipalidad."),
   ("abc", "{F} ¿Qué poder discute y aprueba las leyes?", "El Legislativo, el Congreso", "El Judicial", "El Ejecutivo", "El Congreso, que es el poder Legislativo, discute y aprueba las leyes."),
   ("abc", "{F} ¿En qué se divide directamente cada región?", "en provincias", "en comunas", "en países", "La ficha dice que cada región se divide en provincias."),
   ("abc", "{F} Si quieres saber cuántas comunas hay en una provincia, ¿en qué parte del orden de la ficha debes mirar?", "Después de la provincia, el nivel más pequeño", "Antes del país", "Entre el país y la región", "La comuna es el último nivel: cada provincia se divide en comunas."),
   ("abc", "¿A qué poder corresponde el Presidente o la Presidenta de la República?", "Al Ejecutivo", "Al Judicial", "Al Legislativo", "Dirige el Gobierno, que es el poder Ejecutivo."),
   ("abc", "Una persona quiere reclamar por el alumbrado de su calle. ¿A qué nivel conviene acudir primero?", "La comuna, a la municipalidad", "El Congreso", "Los tribunales", "El alumbrado de una calle suele atenderse en la comuna, que es el nivel más cercano."),
   ("abc", "{F} ¿Cuántos poderes del Estado se nombran en la ficha?", "3", "2", "4", "Se nombran Ejecutivo, Legislativo y Judicial."),
   ("ab", "{F} El Congreso está compuesto por la Cámara de Diputadas y Diputados y por el Senado. ¿Qué poder es?", "El Legislativo", "El Judicial", "La ficha lo ubica en el poder que hace las leyes."),
   ("abc", "Un conflicto entre dos personas por un contrato lo resuelve un tribunal. ¿Qué poder cumple esa función?", "El Judicial", "El Legislativo", "El Ejecutivo", "Aplicar la ley a un conflicto particular corresponde a los tribunales."),
   ("abc", "¿Por qué el Estado reparte funciones entre tres poderes?", "Para que una sola persona no concentre todo el poder", "Para que no haya leyes", "Para evitar las elecciones", "Separar funciones limita el poder y protege los derechos."),
   ("ab", "Una persona dice: «Una comuna contiene varias regiones». ¿Es correcto?", "No: una región contiene varias comunas", "Sí, la comuna es más grande", "La comuna es la división más pequeña, por lo que está dentro de las demás.")],
  ("abc", "Un grupo de vecinos quiere pedir una mejora en su plaza. ¿Cuál es el camino más cercano a ellos?", "Presentar la petición a la municipalidad de su comuna", "Escribir primero al Congreso", "Acudir a un tribunal sin hablar con nadie", "La municipalidad es la institución local que administra la comuna."),
  [("¿Quién dirige el país, según la ficha de organización?", "El Gobierno, con el Presidente o la Presidenta", "El Gobierno es el poder Ejecutivo y lo encabeza quien preside la República."),
   ("¿Cuáles son los tres poderes del Estado?", "Ejecutivo, Legislativo y Judicial", "Cada uno cumple una función distinta."),
   ("¿Qué es una comuna?", "La división más pequeña del territorio, administrada por una municipalidad", "Es el nivel más cercano a las personas.")],
  ("Con la ficha, completa esta tabla: (1) poder que hace las leyes, (2) poder que resuelve conflictos, (3) quién administra una comuna, (4) cuántas regiones tiene Chile, (5) orden de mayor a menor de los cuatro niveles del territorio.",
   "(1) Legislativo. (2) Judicial. (3) La municipalidad, con alcalde o alcaldesa y concejo. (4) 16. (5) País, región, provincia, comuna.",
   ["completa los cinco puntos", "usa los nombres correctos", "ordena bien los niveles"],
   ["tabla con cinco respuestas en el cuaderno"],
   ["confundir región con provincia", "mezclar funciones de los poderes"],
   "Pregunta: «¿Esta función es de hacer leyes, gobernar o resolver conflictos?»."),
  "Dibuja un esquema de cuatro cajas con el orden de los niveles del territorio.",
  "Escribe qué autoridad local conoces por nombre de cargo y a qué poder o nivel corresponde.")

# ====================================================== clase 5
F = ("Ficha 5 (debate de ejemplo: «¿Debe usarse la plaza del barrio para una feria cada sábado?»). "
     "Postura A (a favor): «La feria da la oportunidad de que los vecinos se encuentren y compren cerca. Según el boletín municipal de ejemplo, hubo 12 ferias el año pasado sin reclamos de seguridad». "
     "Postura B (en contra): «La feria deja basura y ruido. Una encuesta de ejemplo del centro vecinal consultó a 40 personas y 26 dijeron que les preocupaba el ruido». "
     "Postura C: «Yo creo que sí, porque sí». "
     "Reglas del debate: hablar por turnos, usar un argumento con razón y evidencia, escuchar sin interrumpir y responder a lo que dijo la otra persona.")
K(5, F,
  "Hoy preparo un debate sobre una decisión de comunidad: distingo opinión de argumento, uso evidencia de fuentes y respeto las reglas del diálogo.",
  ["Un debate es una conversación ordenada en la que cada persona defiende una postura con razones. Es una forma de participación democrática: permite que se oigan distintas ideas antes de decidir. Tú ya has debatido en reuniones, aunque sea sin ese nombre.",
   "Una opinión dice lo que pienso. Un argumento agrega una razón y, si es posible, evidencia: un dato de una fuente fiable. «Me gusta la feria» es una opinión; «la feria reúne a los vecinos, y hubo 12 ferias sin reclamos de seguridad según el boletín» es un argumento.",
   "Una postura razonada se puede cambiar si aparecen mejores datos. Por eso se escucha a los demás sin interrumpir, se pide la fuente de los datos y se responde a lo que se dijo. Al final se puede votar o buscar un acuerdo, y todas las personas respetan el resultado."],
  [("debate", "conversación ordenada en que cada persona defiende una postura con razones"), ("argumento", "razón que apoya una postura, con evidencia si es posible"), ("evidencia", "dato o hecho de una fuente que respalda una idea"), ("postura", "la posición que alguien defiende sobre un tema")],
  [("Opinión o argumento", "«Esta feria es lo mejor que ha pasado». ¿Es opinión o argumento?", ["No da razón ni dato.", "Solo dice lo que piensa la persona."], "Opinión"),
   ("Formar un argumento", "Postura: «Hay que mantener limpia la plaza». Razón: «Es un espacio de todos». Evidencia de ejemplo: «El boletín contó 3 reclamos por basura». ¿Cuántas partes tiene el argumento?", ["Cuento postura, razón y evidencia.", "Son tres partes."], "3 partes")],
  [("Defender una postura repitiéndola más fuerte.", "Se cree que gritar es argumentar.", "Da una razón y un dato de una fuente."),
   ("No escuchar a la otra postura para responderle.", "Se piensa solo en la propia respuesta.", "Resume lo que dijo la otra persona antes de responder.")],
  [("abc", "{F} ¿Cuál de las posturas es solo una opinión sin razón?", "Postura C", "Postura A", "Postura B", "La postura C dice «yo creo que sí, porque sí» y no da ninguna razón."),
   ("ab", "{F} ¿La postura A usa evidencia?", "Sí, el dato de 12 ferias sin reclamos de seguridad", "No, no usa ningún dato", "La postura A cita un dato de un boletín municipal."),
   ("abc", "{F} ¿Qué dato usa la postura B?", "26 de 40 personas consultadas se preocupan por el ruido", "12 ferias sin reclamos", "40 reclamos de basura", "Es el dato de la encuesta del centro vecinal."),
   ("=", "{F} En la encuesta de la postura B, ¿cuántas de las 40 personas consultadas no manifestaron preocupación por el ruido?", "40-26", "Se resta de los consultados la cantidad que sí se preocupa.", " personas"),
   ("abc", "{F} ¿Cuál es una regla del debate según la ficha?", "Hablar por turnos y escuchar sin interrumpir", "Gritar más fuerte que los demás", "Hablar sin pruebas", "La ficha lista turnos y escucha como reglas."),
   ("abc", "¿Cuál frase es un argumento y no solo una opinión?", "«La feria conviene porque reúne a los vecinos; el boletín contó 12 ferias sin incidentes»", "«Me gusta la feria»", "«Es lo mejor»", "Tiene razón y dato de una fuente."),
   ("ab", "Una persona de la postura B recibe un dato nuevo que la contradice. ¿Qué hace una persona que argumenta bien?", "Considera el dato y ajusta su postura si corresponde", "Lo ignora y repite lo mismo", "Una postura razonada puede cambiar al conocer mejores datos."),
   ("abc", "{F} Si quisieras responder a la postura B con respeto, ¿qué frase usarías?", "«Entiendo la preocupación por el ruido; propongo un horario limitado y una limpieza al terminar»", "«Eso es una tontería»", "«No me importa lo que digan»", "Reconoce el argumento del otro y propone una solución."),
   ("abc", "¿Por qué un debate es una forma de participación democrática?", "Porque permite que se oigan varias ideas antes de decidir", "Porque obliga a que gane la voz más fuerte", "Porque elimina las votaciones", "Dar espacio a distintas ideas es parte de la democracia."),
   ("abc", "En el debate, una persona interrumpe a otra todo el tiempo. ¿Qué regla se incumple?", "Escuchar sin interrumpir", "Usar evidencia", "Citar una fuente", "Interrumpir impide que la otra persona termine su argumento."),
   ("abc", "Al terminar el debate se vota y gana la postura A. ¿Qué actitud cívica corresponde a quienes defendían la B?", "Respetar el resultado y colaborar para reducir el ruido", "Desconocer el resultado", "Dejar la comunidad", "Aceptar un resultado acordado es una actitud cívica."),
   ("abc", "Un participante dice: «Según la encuesta, 26 de 40 personas se preocupan por el ruido». ¿Qué debes pedirle para evaluar el dato?", "Quién hizo la encuesta y cuándo", "El color del papel", "Que repita más fuerte", "Para saber si la fuente es fiable hay que conocer autor y fecha."),
   ("abc", "Un argumento ordenado tiene postura, razón y evidencia. ¿Cuál es el orden más claro?", "Postura, razón y evidencia", "Evidencia, color y postura", "Voz fuerte, razón y silencio", "Se dice qué se defiende, por qué y con qué dato.")],
  ("abc", "En una reunión de vecinos se decide si instalar un paradero con techo en la esquina. Una persona dice: «Instalémoslo porque da seguridad en días de lluvia; el boletín municipal registró 9 reclamos de ejemplo por mojarse». ¿Qué hizo?", "Presentó un argumento con razón y evidencia", "Dio una opinión sin razón", "Interrumpió a otra persona", "Dio una postura, una razón y un dato de una fuente."),
  [("En una reunión de comunidad, ¿qué es un debate?", "Conversación ordenada en que cada persona defiende una postura con razones", "Se hace por turnos y con respeto."),
   ("En un argumento sobre la comuna, ¿qué es la evidencia?", "Dato o hecho de una fuente que respalda una idea", "La evidencia sirve para comprobar si el argumento es cierto."),
   ("¿Cuál es la diferencia entre opinión y argumento?", "El argumento agrega razón y evidencia", "Una opinión dice lo que pienso; un argumento lo respalda.")],
  ("Debate de ejemplo: «¿Debe haber una biblioteca comunitaria abierta los fines de semana?». Escribe un argumento a favor o en contra (tú decides la postura) con tres partes: postura, razón y una evidencia que inventes rotulada «de ejemplo» (por ejemplo, una cifra de visitas). Escribe también una frase respetuosa para responder a quien piensa distinto.",
   "A favor: la biblioteca abierta ayuda a quienes trabajan en la semana. Evidencia de ejemplo: 35 personas la visitaron un sábado de prueba. Respuesta: entiendo que cuesta mantenerla, propongo turnos de voluntarios.",
   ["incluye postura, razón y evidencia de ejemplo", "usa un lenguaje respetuoso", "responde a una idea distinta"],
   ["tres líneas de argumento y una frase de respuesta"],
   ["opinión sin razón", "evidencia sin rótulo de ejemplo"],
   "Pregunta: «¿Qué razón y qué dato apoyan mi postura?»."),
  "Escribe una opinión sobre un tema del barrio y conviértela en un argumento.",
  "Anota dos preguntas que harías para evaluar la fuente del dato de otra persona.")

# ====================================================== clase 6
F = ("Ficha 6 (pauta de revisión de ejemplo, un punto por criterio). 1) Elige fuentes relevantes. 2) Evalúa su fiabilidad con autor, fecha, origen y propósito. "
     "3) Explica la democracia con elección, voto, representación y participación. 4) Ubica los niveles: país, región, provincia, comuna. "
     "5) Argumenta con razón y evidencia. 6) Escucha y responde con respeto. "
     "Trabajo revisado: la persona usó dos fuentes con autor y fecha, definió democracia y representación, ubicó país, región y comuna pero olvidó la provincia, "
     "dio un argumento con razón y evidencia y respondió con respeto, pero no revisó el propósito de sus fuentes.")
K(6, F,
  "Hoy reviso lo aprendido en este módulo: fuentes, fiabilidad, democracia, participación y organización de Chile, y decido mis próximos pasos.",
  ["Revisar es comparar lo que hiciste con una pauta clara. Hoy usamos una pauta de seis criterios: elegir fuentes relevantes, evaluar su fiabilidad, explicar la democracia, ubicar los niveles del territorio, argumentar con evidencia y escuchar con respeto.",
   "Para cada criterio marca sí o no, suma los puntos y escribe una mejora concreta por cada «no». Por ejemplo: «revisar el propósito de cada fuente» o «agregar la provincia al esquema de niveles». Una mejora concreta dice qué cambiar y cómo.",
   "Después decide qué seguirás practicando: contrastar fuentes antes de usar un dato, usar bien las palabras de la democracia o participar en una conversación de tu comunidad con argumentos respetuosos. Aprender también es saber qué falta."],
  [("criterio", "regla para decidir si algo está bien hecho"), ("pauta", "lista de criterios para revisar un trabajo"), ("mejora concreta", "cambio específico que hace mejor un trabajo"), ("autoevaluación", "revisar el propio trabajo con una pauta")],
  [("Contar puntos", "Un trabajo cumple los criterios 1, 2, 3 y 5. ¿Cuántos puntos tiene de seis?", ["Cuento los criterios cumplidos.", "Son cuatro."], "4 de 6"),
   ("Escribir una mejora", "No se revisó el propósito de las fuentes. ¿Qué mejora escribes?", ["Digo qué falta.", "Escribo cómo corregirlo."], "Anotar si cada fuente busca informar, vender o convencer")],
  [("Marcar sí en todos los criterios sin mirar el trabajo.", "No se compara con la pauta.", "Revisa cada criterio con un dato del trabajo."),
   ("Escribir una mejora vaga, como «hacerlo mejor».", "No indica qué cambiar.", "Nombra qué falta y cómo corregirlo.")],
  [("abc", "{F} ¿Cuántos criterios tiene la pauta?", "6", "4", "8", "La pauta de la ficha numera seis criterios en total."),
   ("ab", "{F} ¿El trabajo revisado cumple el criterio 1, elegir fuentes relevantes?", "Sí, usó dos fuentes con autor y fecha", "No, no usó fuentes", "La ficha indica que el trabajo usó dos fuentes."),
   ("abc", "{F} ¿Qué criterio incumple el trabajo revisado en el nivel del territorio?", "El 4, porque olvidó la provincia", "El 3, porque olvidó la democracia", "El 6, porque no respondió", "Ubicó país, región y comuna pero no la provincia."),
   ("abc", "{F} ¿Qué criterio incumple por no revisar el propósito de sus fuentes?", "El 2", "El 5", "El 6", "El criterio 2 incluye autor, fecha, origen y propósito."),
   ("{F} ¿Cuántos puntos obtiene el trabajo revisado?", "4", "Cumple los criterios 1, 3, 5 y 6 y falla el 2 y el 4, lo que suma cuatro puntos."),
   ("abc", "{F} ¿Qué mejora corrige el criterio 4?", "Agregar la provincia entre la región y la comuna", "Cambiar el color del cuaderno", "Escribir más rápido", "El nivel que falta es la provincia."),
   ("abc", "¿Cuál es el orden correcto de los niveles que debe incluir el esquema?", "País, región, provincia, comuna", "País, comuna, región, provincia", "Provincia, país, comuna, región", "Se ordenan del mayor al menor territorio del país."),
   ("ab", "Una persona dice que votar es lo único que hace una democracia. ¿Qué corrección haces?", "También incluye participación, derechos y representación", "Tiene razón, es solo votar", "La democracia combina elecciones con participación y respeto de derechos."),
   ("abc", "Dos fuentes dicen cosas distintas sobre quién hace las leyes. ¿Qué haces?", "Contrastar con una tercera fuente fiable", "Elegir al azar", "No usar ninguna", "Contrastar ayuda a decidir qué dato es correcto."),
   ("abc", "¿Qué hace de un comentario un argumento?", "Que tenga razón y evidencia de una fuente", "Que se diga con voz fuerte", "Que sea muy corto", "El argumento respalda la postura con razones y datos."),
   ("abc", "Tras el debate, tu grupo pierde la votación. ¿Qué actitud cívica corresponde?", "Respetar el resultado y seguir participando", "Boicotear la decisión", "No volver nunca", "Respetar un resultado acordado es parte de convivir en democracia."),
   ("abc", "{F} Si en el trabajo revisado se agregara el propósito de las fuentes y la provincia, ¿cuántos puntos tendría?", "6", "5", "4", "Se cumplirían los criterios 2 y 4 que faltaban."),
   ("abc", "¿Qué conclusión resume mejor este módulo?", "Para participar bien conviene usar fuentes fiables, conocer cómo se organiza el país y argumentar con respeto", "Basta con repetir lo que dicen los chats", "La democracia no necesita información", "Integra lo trabajado sobre fuentes, democracia y debate.")],
  ("abc", "Una organización prepara un debate sobre una plaza. Ya tiene fuentes con autor y fecha, y un argumento con evidencia, pero no ubicó qué autoridad decide. ¿Qué debe mejorar?", "Averiguar qué institución local, la municipalidad, administra la comuna", "Quitar las fuentes", "Cambiar el tema", "Falta el criterio de ubicar el nivel y la autoridad."),
  [("En Historia: ¿qué es una pauta de revisión?", "Lista de criterios para revisar un trabajo", "Ordena qué cosas se deben comprobar en el trabajo."),
   ("¿Qué es una mejora concreta?", "Un cambio específico que mejora un trabajo", "Dice qué falta y cómo corregirlo."),
   ("¿Cuáles son los cuatro niveles del territorio en orden?", "País, región, provincia, comuna", "Va de lo más grande a lo más pequeño.")],
  ("Revisa con la pauta de seis criterios un trabajo de ejemplo: «Usé un mensaje anónimo y un libro con autor y año; expliqué democracia y representación; ordené país, región, provincia y comuna; di una opinión sin razón; interrumpí a otra persona». Marca sí o no en cada criterio, suma los puntos y escribe una mejora por cada «no».",
   "Criterios: 1 sí, 2 no (usó fuente anónima), 3 sí, 4 sí, 5 no, 6 no. Puntos: 3 de 6. Mejoras: reemplazar el mensaje anónimo, agregar razón y evidencia, escuchar sin interrumpir.",
   ["marca los seis criterios", "suma bien los puntos", "escribe una mejora concreta por cada no"],
   ["pauta marcada con las mejoras"],
   ["marcar sí sin comprobar", "mejoras vagas"],
   "Pregunta: «¿Qué cambio haría que este criterio pase de no a sí?»."),
  "Elige dos criterios de la pauta y escribe cómo los practicarías esta semana.",
  "Escribe una pregunta de debate sobre tu comuna y las dos fuentes que consultarías.")
