"""Historia, Geografía y Ciencias Sociales EPJA Básica N2, módulo 3 (parte 3): OAD-11, seleccionar fuentes y preparar una presentación oral sobre la relación entre pueblos originarios y espacio geográfico. Fuentes y situaciones de ejemplo; todo se resuelve en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz, goma y reloj o cronómetro de celular si se tiene. Las fuentes, fichas y guiones están escritos en cada ficha y son de ejemplo. La presentación se ensaya en voz alta con una persona de confianza; no se necesita audio, video ni internet."
build = make_build(MATERIALS)

O = "EPJA-HGCS-NB2-OAD-11"
PRIOR = ["He participado en reuniones donde alguien explica un tema.", "Sé que los pueblos originarios habitaron distintos paisajes de Chile.", "Puedo leer textos breves y anotar ideas con mis palabras."]


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    build(O, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ===================================================== clase 1
F = ("Ficha 1 (situación de ejemplo). En una reunión de la organización vecinal «Los Alerces», tres personas presentan sobre pueblos originarios y su territorio. "
     "Persona A habla 2 minutos sin orden y mira solo su papel. Persona B dice primero el tema, explica tres ideas con un ejemplo cada una, cierra con una frase y habla 3 minutos mirando a las personas. "
     "Persona C lee 8 minutos un texto copiado, sin decir de dónde lo sacó.")
K(1, F,
  "Hoy parto de lo que ya sé de reuniones y presentaciones para entender qué hace buena a una presentación oral sobre pueblos originarios y su territorio.",
  ["Una presentación oral es explicar un tema hablando ante otras personas. Tú ya lo haces cuando cuentas algo en una reunión de vecinos, explicas una tarea en el trabajo o informas algo en la familia. Para que otras personas entiendan, hace falta pensar en quién escucha, que se llama audiencia, y en para qué se habla, que se llama propósito.",
   "Una presentación clara tiene tres partes. La apertura dice el tema y por qué importa. El desarrollo explica las ideas principales, cada una con un ejemplo o un dato. El cierre repite lo más importante y deja una idea final. Además, se cuida el tiempo, se habla con voz clara y se mira a quienes escuchan.",
   "Cuando el tema son los pueblos originarios y el espacio donde se desenvolvieron, la información debe venir de fuentes que se puedan nombrar, y el trato debe ser respetuoso: se habla de pueblos que viven hoy, sin burlas ni generalizaciones."],
  [("presentación oral", "explicar un tema hablando ante otras personas"), ("audiencia", "las personas que escuchan"), ("propósito", "para qué se habla"), ("apertura, desarrollo y cierre", "las tres partes de una presentación")],
  [("Reconocer las partes", "Una persona dice: «Hoy les voy a hablar de cómo viven los pueblos del norte junto al agua». ¿Qué parte de la presentación es?", ["Dice el tema.", "Eso se hace al comenzar."], "La apertura"),
   ("Usar el tiempo", "Una presentación debe durar 3 minutos y la apertura dura 30 segundos. ¿Cuánto queda para el desarrollo y el cierre?", ["3 minutos son 180 segundos.", "Resto los 30 segundos de la apertura a 180."], "150 segundos")],
  [("Leer un texto de principio a fin como si fuera la presentación.", "Se pierde el contacto con la audiencia y las ideas principales.", "Prepara un guion con ideas clave y úsalo como apoyo."),
   ("Hablar sin tener claro el tema.", "La audiencia no sabe qué esperar.", "Di el tema en la primera frase.")],
  [("abc", "{F} ¿Quién hizo la presentación más clara?", "Persona B", "Persona A", "Persona C", "Persona B dice el tema, ordena ideas con ejemplos y cuida el tiempo."),
   ("ab", "{F} ¿Cuántos minutos habló la Persona B?", "3 minutos", "8 minutos", "La ficha dice que habló 3 minutos mirando a las personas."),
   ("abc", "{F} ¿Qué problema principal tiene la Persona C?", "lee un texto copiado sin decir de dónde lo sacó", "habló poco", "no usó ningún texto", "Copiar sin citar impide comprobar la fuente y no explica con palabras propias."),
   ("ab", "La audiencia es", "las personas que escuchan", "la persona que habla", "La audiencia son quienes escuchan la presentación."),
   ("abc", "{F} ¿Qué parte falta en la presentación de la Persona A?", "orden en sus ideas", "un micrófono", "una canción", "Habló sin orden y mirando solo su papel."),
   ("abc", "¿Cuál es la función de la apertura?", "decir el tema y por qué importa", "repetir todo el desarrollo", "despedirse sin decir nada", "La apertura presenta el tema y capta la atención."),
   ("ab", "El cierre sirve para", "repetir lo más importante y dejar una idea final", "empezar un tema nuevo", "El cierre resume y deja una idea que se recuerda."),
   ("abc", "{F} ¿Cuántos ejemplos usó la Persona B?", "uno por cada idea, es decir, tres", "ninguno", "diez", "La ficha dice que explicó tres ideas con un ejemplo cada una."),
   ("ab", "Al hablar de pueblos originarios, lo más respetuoso es hablar de ellos", "como pueblos que viven hoy y tienen cultura", "como si ya no existieran", "Los pueblos originarios continúan existiendo y manteniendo su cultura."),
   ("abc", "El propósito de una presentación es", "para qué se habla", "cuántas personas hay", "qué hora es", "El propósito responde para qué se presenta el tema."),
   ("abc", "{F} ¿Qué hace la Persona B que ayuda a la audiencia?", "mira a las personas mientras habla", "mira solo el piso", "habla en voz muy baja", "El contacto visual mantiene la atención de la audiencia."),
   ("ab", "Una buena presentación necesita fuentes porque", "así se puede comprobar de dónde viene la información", "así dura más tiempo", "Citar fuentes da respaldo al contenido."),
   ("=", "{F} La Persona C habló 8 minutos y la reunión asignó 3 minutos a cada persona. ¿Cuántos minutos de más usó?", "8-3", "Se resta el tiempo asignado del tiempo usado.", " minutos")],
  ("abc", "En una reunión vecinal te piden presentar durante 3 minutos lo que se sabe sobre un pueblo originario de tu región. ¿Qué es lo primero?", "decidir el tema y pensar a quién le hablas", "empezar a leer cualquier texto", "elegir la ropa", "Definir tema y audiencia orienta toda la preparación."),
  [("En HGCS, al presentar: ¿cuáles son las tres partes de una presentación?", "Apertura, desarrollo y cierre", "Ordenan las ideas para que la audiencia siga el hilo."),
   ("En una presentación oral, ¿quiénes son la audiencia?", "Quienes escuchan", "Pensar en ellos ayuda a explicar con claridad."),
   ("¿Por qué conviene citar las fuentes?", "Para que se pueda comprobar la información", "Mostrar de dónde viene un dato da confianza.")],
  ("Lee en voz alta la ficha 1 y escribe tres frases: qué hizo bien la Persona B, qué podrían mejorar A y C, y cuál sería tu apertura para un tema que tú elijas sobre pueblos originarios y su territorio.",
   "B dijo el tema y dio ejemplos. A debe ordenar sus ideas; C debe explicar con sus palabras y citar. Mi apertura: «Hoy voy a contar cómo los pueblos del norte aprovechaban el agua».",
   ["describe lo que hizo bien B", "propone mejoras a A y C", "escribe una apertura clara"],
   ["tres frases escritas"],
   ["decir solo «estuvo mal»", "abrir sin decir el tema"],
   "Pregunta: «¿Mi apertura dice el tema?»."),
  "Cuenta en voz alta durante un minuto algo que sepas de tu barrio sin mirar papeles.",
  "Escribe dos razones por las que ayuda hablar con orden y mirar a la audiencia.")

# ===================================================== clase 2
F = ("Ficha 2 (tres fuentes de ejemplo sobre los kawésqar y la canoa). Fuente A: panel de un museo regional de ejemplo; indica el nombre del museo, la fecha de elaboración y que se basa en conversaciones con personas de la comunidad. "
     "Fuente B: mensaje reenviado por teléfono, sin autor ni fecha, que dice «los kawésqar eran gigantes». "
     "Fuente C: libro de divulgación de ejemplo, con autora y año, que cita sus fuentes y coincide con el panel en que usaban canoas en los canales.")
K(2, F,
  "Hoy aprendo las palabras para seleccionar fuentes y distingo una fuente confiable de una dudosa.",
  ["Seleccionar fuentes es elegir de dónde sacar información. Una fuente confiable tiene cuatro rasgos: se sabe quién la hizo (autor), se sabe cuándo (fecha), explica para qué fue hecha (propósito) y cita en qué se basa. Además, sus datos coinciden con los de otras fuentes. Esto se llama contrastar.",
   "No toda información que circula sirve. Un mensaje reenviado sin autor ni fecha es difícil de comprobar, y puede contener datos inventados o exagerados. Una buena fuente, en cambio, se puede revisar: si alguien duda, puede buscar el panel, el libro o a la persona que dio la información.",
   "En temas de pueblos originarios es especialmente importante usar fuentes respetuosas, que se apoyen en la voz de las propias comunidades y no repitan estereotipos. Cuando se tengan dudas sobre la forma tradicional de una costumbre, se consulta a las personas de la comunidad."],
  [("autor", "la persona o institución que hizo la fuente"), ("contrastar", "comparar dos o más fuentes para ver si coinciden"), ("estereotipo", "idea simplificada y falsa que se repite sobre un grupo"), ("confiable", "que se puede comprobar y merece confianza")],
  [("Evaluar una fuente", "La fuente B no tiene autor ni fecha. ¿Es confiable?", ["No se sabe quién la hizo ni cuándo.", "No se puede comprobar."], "No, porque no se puede comprobar"),
   ("Contrastar", "¿Qué dato coincide entre las fuentes A y C?", ["Reviso qué dice cada una.", "Ambas hablan de canoas en los canales."], "Que los kawésqar usaban canoas en los canales")],
  [("Creer algo porque llegó por mensaje y muchos lo comparten.", "Compartir no es comprobar.", "Busca autor, fecha y otra fuente."),
   ("Descartar una fuente solo porque es antigua.", "Una fuente antigua puede ser valiosa, depende de su origen.", "Revisa cuatro rasgos: autor, fecha, propósito y fuentes que cita.")],
  [("abc", "{F} ¿Cuál es la fuente menos confiable?", "Fuente B", "Fuente A", "Fuente C", "La B no tiene autor, fecha ni respaldo."),
   ("abc", "{F} ¿En qué se basa el panel del museo?", "en conversaciones con personas de la comunidad", "en un mensaje reenviado", "en una receta", "La ficha dice que el panel se basa en conversaciones con personas de la comunidad."),
   ("ab", "{F} ¿Qué fuente cita sus fuentes y tiene autora y año?", "Fuente C", "Fuente B", "La fuente C tiene autora y año y cita en qué se apoya."),
   ("abc", "Un rasgo de fuente confiable es", "tener autor y fecha", "ser compartida por muchas personas", "ser muy corta", "Autor y fecha permiten comprobar el origen."),
   ("ab", "Contrastar es", "comparar fuentes para ver si coinciden", "copiar una fuente", "Contrastar significa revisar si distintas fuentes dicen lo mismo."),
   ("abc", "{F} ¿Qué dice la fuente B que parece un estereotipo exagerado?", "que los kawésqar eran gigantes", "que usaban canoas", "que vivían en canales", "Decir que eran gigantes es una exageración sin respaldo."),
   ("abc", "{F} ¿Cuántas de las tres fuentes tienen autor o institución identificada?", "dos: la A y la C", "una: solo la B", "las tres", "La A tiene museo y la C tiene autora; la B no tiene autor."),
   ("ab", "Un mensaje sin autor llega por teléfono con un dato sorprendente. Lo mejor es", "buscar otra fuente que lo confirme", "reenviarlo de inmediato", "Compartir sin comprobar puede difundir errores."),
   ("abc", "El propósito de una fuente es", "para qué fue hecha", "cuánto pesa", "de qué color es", "Saber para qué se hizo ayuda a ver si hay un sesgo."),
   ("ab", "Si dudas de la forma tradicional de una costumbre, lo mejor es consultar a", "las personas de la comunidad", "cualquier persona", "Quienes viven la costumbre conocen su forma tradicional."),
   ("abc", "{F} Si debes elegir dos fuentes de la ficha para una presentación, ¿cuáles eliges?", "A y C", "B y A", "B solamente", "A y C tienen autor, fecha y se confirman entre sí."),
   ("abc", "Un estereotipo es", "una idea simplificada y falsa sobre un grupo", "un dato comprobado", "una fecha", "Los estereotipos reducen a un pueblo a una imagen falsa."),
   ("ab", "Una fuente antigua", "puede ser valiosa si se conoce su origen", "nunca sirve", "La edad no decide: importa quién la hizo y con qué respaldo.")],
  ("abc", "En la biblioteca del barrio, una persona encuentra un folleto sin autor sobre pueblos originarios. ¿Qué hace antes de usarlo en una presentación?", "busca otra fuente con autor que confirme los datos", "lo usa tal cual", "lo guarda sin leer", "Contrastar con una fuente confiable reduce el riesgo de errores."),
  [("Al preparar un tema de pueblos originarios, ¿qué es contrastar fuentes?", "Compararlas para ver si coinciden", "Si coinciden, el dato es más seguro."),
   ("¿Qué cuatro rasgos tiene una fuente confiable?", "Autor, fecha, propósito y fuentes citadas", "Esos cuatro rasgos permiten comprobar la fuente."),
   ("¿Por qué evitar los estereotipos?", "Porque reducen a un pueblo a una imagen falsa", "Cada pueblo tiene una cultura rica y diversa.")],
  ("Con las tres fuentes de la ficha 2, haz una tabla con tres filas (A, B y C) y tres columnas: autor o fecha, ¿coincide con otra fuente?, ¿la usarías? Responde con sí o no y una razón de una línea.",
   "A: tiene museo y fecha; coincide con C; sí. B: sin autor ni fecha; no coincide; no. C: tiene autora y año; coincide con A; sí.",
   ["completa las tres filas", "da razones breves", "explica por qué no usa la fuente B"],
   ["una tabla de tres filas"],
   ["usar la fuente B sin dudar", "no justificar"],
   "Pregunta: «¿Podría otra persona comprobar esta fuente?»."),
  "Piensa en un mensaje que hayas recibido por teléfono y escribe qué datos le faltaban para saber si era confiable.",
  "Escribe tres preguntas que te harías antes de usar una fuente sobre un pueblo originario.")

# ===================================================== clase 3
F = ("Ficha 3 (dos fuentes de ejemplo sobre el pueblo aymara y el altiplano). Fuente 1, panel de un centro cultural de ejemplo: «Los aymara viven en el altiplano del norte, a gran altura. Cultivan papas en terrazas y crían llamas y alpacas, que les dan lana y transporte». "
     "Fuente 2, cuaderno de divulgación de ejemplo, con autor: «Para los aymara, la Pachamama es la Madre Tierra; se le agradece y se la cuida antes de sembrar». "
     "Modelo de ficha de datos: Tema | Dato | Con mis palabras | Fuente.")
K(3, F,
  "Hoy sigo los pasos para sacar datos de dos fuentes, anotarlos en una ficha y decirlos con mis propias palabras.",
  ["Preparar una presentación empieza por buscar y anotar. Paso uno: elige el tema y una pregunta, por ejemplo: «¿cómo aprovechaban el altiplano los aymara?». Paso dos: lee cada fuente y subraya datos que respondan la pregunta. Paso tres: pasa cada dato a una ficha con cuatro columnas: tema, dato, con mis palabras y fuente. Paso cuatro: revisa que cada dato tenga su fuente anotada.",
   "Decir un dato con tus palabras se llama parafrasear. Se cambia la forma de decirlo, pero se mantiene el sentido. Así no copias y demuestras que lo entendiste. Si usas las palabras exactas de la fuente, se ponen entre comillas y se dice de quién son: eso es una cita.",
   "Con dos fuentes puedes armar una idea más completa: la primera da cuenta de lo que se hace con el territorio y la segunda, de cómo se entiende la tierra. Juntas muestran la relación entre el pueblo y su espacio."],
  [("parafrasear", "decir una idea con otras palabras sin cambiar su sentido"), ("cita", "palabras exactas de una fuente, entre comillas, con su autor"), ("ficha de datos", "cuadro donde se anota cada dato con su fuente"), ("pregunta de investigación", "lo que quieres averiguar")],
  [("Parafrasear", "Dato de la fuente 1: «Cultivan papas en terrazas». ¿Cómo se dice con otras palabras?", ["Cambio la forma de decirlo.", "Mantengo el sentido."], "Siembran papas en escalones de terreno"),
   ("Llenar la ficha", "Para el dato «La Pachamama es la Madre Tierra», ¿qué va en la columna Fuente?", ["Reviso de qué fuente salió.", "Es la fuente 2."], "El cuaderno de divulgación (fuente 2)")],
  [("Copiar la frase de la fuente sin comillas.", "Se presenta como propia una frase ajena.", "Usa comillas y nombra la fuente, o parafrasea."),
   ("Anotar un dato sin la fuente.", "Después no se sabe de dónde salió.", "Completa siempre la columna Fuente.")],
  [("abc", "{F} ¿Cuál es la pregunta de investigación del ejemplo de la clase?", "¿cómo aprovechaban el altiplano los aymara?", "¿cuántos años tiene el panel?", "¿dónde se vende lana?", "La pregunta orienta qué datos buscar."),
   ("abc", "{F} Según la fuente 1, ¿qué animales crían?", "llamas y alpacas", "caballos", "vacas", "La fuente 1 dice que crían llamas y alpacas."),
   ("abc", "{F} ¿Cuántas columnas tiene el modelo de ficha de datos?", "cuatro", "tres", "cinco", "El modelo tiene Tema, Dato, Con mis palabras y Fuente: son cuatro."),
   ("abc", "Parafrasear es", "decir una idea con otras palabras sin cambiar su sentido", "copiar sin comillas", "inventar datos", "Cambia la forma pero conserva el significado."),
   ("ab", "Una cita se escribe", "entre comillas y con el nombre de quien lo dijo", "sin comillas ni autor", "Las comillas y el autor muestran que las palabras no son propias."),
   ("abc", "{F} ¿Qué dato de la fuente 1 explica la lana y el transporte?", "las llamas y las alpacas", "las papas", "las terrazas", "La fuente 1 dice que esos animales dan lana y transporte."),
   ("abc", "{F} ¿Qué columna de la ficha de datos responde «de dónde salió»?", "Fuente", "Tema", "Con mis palabras", "La columna Fuente registra el origen del dato."),
   ("ab", "{F} ¿Qué paráfrasis conserva el sentido de «se le agradece y se la cuida antes de sembrar»?", "se respeta y se cuida la tierra antes de sembrar", "se vende la tierra antes de sembrar", "La paráfrasis mantiene la idea de agradecer y cuidar la tierra."),
   ("abc", "{F} ¿Qué relación entre pueblo y espacio muestran las dos fuentes juntas?", "se aprovechan los recursos del altiplano y se respeta a la tierra", "no hay relación", "solo viven en ciudades", "La fuente 1 da recursos y la 2 da cosmovisión."),
   ("ab", "Un compañero copia una frase y no la pone entre comillas. El error es", "no citar", "usar lápiz", "Presentar una frase ajena como propia es un error de citación."),
   ("abc", "El paso 4 del método es", "revisar que cada dato tenga su fuente", "borrar la ficha", "empezar de nuevo", "Cada dato debe quedar con su origen."),
   ("abc", "{F} ¿Cuántas fuentes tiene la ficha 3?", "dos", "una", "cinco", "La ficha incluye la fuente 1 y la fuente 2."),
   ("ab", "Si una fuente no responde tu pregunta, lo mejor es", "buscar otra fuente", "inventar la respuesta", "Una pregunta sin respuesta se resuelve con más fuentes.")],
  ("abc", "En una reunión de la organización vecinal te piden explicar por qué el agua es clave en los pueblos del desierto. Tienes un panel con autor y un folleto sin autor. ¿Qué usas?", "el panel con autor, y verificas el folleto en otra fuente", "solo el folleto", "ninguno", "El panel con autor se puede comprobar y el folleto necesita contraste."),
  [("En HGCS, al presentar: ¿qué es parafrasear?", "Decir una idea con otras palabras", "Se mantiene el sentido sin copiar."),
   ("¿Qué debe llevar toda ficha de datos?", "La fuente de cada dato", "Así se puede comprobar el dato después."),
   ("En una ficha de datos, ¿cómo se escribe una cita textual?", "Entre comillas y con su autor", "Muestra que son palabras ajenas y de quién son.")],
  ("Con las dos fuentes de la ficha 3, completa una ficha de datos con tres filas: una sobre ubicación, una sobre recursos y una sobre cosmovisión. En «con mis palabras» no copies la frase original.",
   "Ubicación | viven en el altiplano del norte | están en las alturas del norte | fuente 1. Recursos | cultivan papas y crían llamas | siembran en terrazas y cuidan animales | fuente 1. Cosmovisión | la Pachamama | respetan y cuidan la tierra | fuente 2.",
   ["tres filas completas", "cada dato con su fuente", "parafrasea y no copia"],
   ["una ficha de tres filas"],
   ["copiar la frase literal", "dejar la fuente en blanco"],
   "Pregunta: «¿Qué cambiaste de la frase original sin cambiar su sentido?»."),
  "Parafrasea con tus palabras la frase: «Los aymara viven en el altiplano del norte, a gran altura».",
  "Explica por qué conviene usar dos fuentes en lugar de una.")

# ===================================================== clase 4
F = ("Ficha 4 (ideas sueltas de una presentación de ejemplo sobre pueblos y territorio, a ordenar). "
     "1) Al final, mencionar que los pueblos originarios viven hoy y mantienen su cultura. "
     "2) Presentarse y decir: «Hoy hablaré de cómo tres pueblos aprovechan su territorio». "
     "3) Explicar que en el norte los atacameños cuidan el agua con canales y cultivan en oasis. "
     "4) Explicar que en el sur los mapuche, en particular los pehuenche, recolectan piñones de la araucaria. "
     "5) Explicar que los kawésqar recorrían canales en canoa y se alimentaban de mariscos. "
     "Tiempo total: 3 minutos (180 segundos).")
K(4, F,
  "Hoy practico con apoyo cómo ordenar las ideas de una presentación en apertura, desarrollo y cierre, cuidando el tiempo.",
  ["Armar un guion es ordenar las ideas antes de hablar. La apertura presenta el tema y dice qué se va a explicar. El desarrollo tiene una idea por cada fuente o pueblo, cada una con su dato. El cierre recuerda lo más importante. Un guion no se lee de corrido: se usa como apoyo con palabras clave.",
   "Para cuidar el tiempo, se reparten los segundos entre las partes. En una presentación de 3 minutos, por ejemplo, se pueden dedicar 30 segundos a la apertura, 2 minutos al desarrollo y 30 segundos al cierre. Si tienes tres ideas en el desarrollo, cada una dura 40 segundos.",
   "Cuando uses ejemplos de pueblos distintos, ordénalos con un criterio claro: por ejemplo, de norte a sur. Así la audiencia entiende la relación entre paisaje y pueblo, y no mezcla los datos."],
  [("guion", "apoyo escrito con las ideas ordenadas de una presentación"), ("palabra clave", "palabra que recuerda una idea importante"), ("criterio", "regla para ordenar o decidir"), ("repartir el tiempo", "dar a cada parte una duración")],
  [("Ordenar por criterio", "Si ordenas los pueblos de norte a sur, ¿cuál va primero: atacameños o kawésqar?", ["El norte va primero.", "Los atacameños viven en el norte."], "Atacameños"),
   ("Repartir tiempo", "Una presentación de 180 segundos usa 30 segundos en la apertura y 30 en el cierre. ¿Cuántos quedan para el desarrollo?", ["180 − 30 − 30.", "Resto 120."], "120 segundos")],
  [("Poner tanta información en una idea que se acaba el tiempo.", "No se reparte el tiempo.", "Asigna segundos a cada parte antes de hablar."),
   ("Cerrar con un dato nuevo.", "El cierre debe resumir, no abrir otro tema.", "Usa el cierre para repetir lo más importante.")],
  [("abc", "{F} ¿Cuál idea es la apertura?", "la idea 2", "la idea 1", "la idea 5", "La idea 2 presenta el tema, por eso va al comienzo."),
   ("abc", "{F} ¿Cuál idea es el cierre?", "la idea 1", "la idea 3", "la idea 4", "La idea 1 resume que los pueblos viven hoy; es una idea final."),
   ("abc", "{F} Si ordenas las ideas de desarrollo de norte a sur, ¿cuál va en el medio?", "la idea 4, sobre los mapuche", "la idea 3, sobre los atacameños", "la idea 5, sobre los kawésqar", "El orden es atacameños (norte), mapuche (centro y sur) y kawésqar (extremo sur)."),
   ("abc", "{F} Si ordenas de norte a sur, ¿cuál va última en el desarrollo?", "la idea 5, sobre kawésqar", "la idea 3", "la idea 4", "Los kawésqar están en el extremo sur."),
   ("=", "{F} Si se destinan 20 segundos a la apertura y 30 al cierre, ¿cuántos segundos quedan para el desarrollo?", "180-20-30", "Se restan las dos partes al total de 180 segundos.", " segundos"),
   ("=", "{F} Si el desarrollo dura 120 segundos y tiene 3 ideas de igual duración, ¿cuántos segundos dura cada idea?", "120/3", "Se reparte el tiempo en partes iguales.", " segundos"),
   ("ab", "Un guion se usa", "como apoyo con palabras clave", "leyéndolo palabra por palabra", "El guion ayuda a recordar; leerlo entero hace perder la mirada."),
   ("abc", "{F} ¿Qué recurso aprovechan los kawésqar según la ficha?", "mariscos", "piñones", "canales de riego", "La idea 5 menciona mariscos como parte de su alimentación."),
   ("abc", "{F} ¿Qué recurso aprovechan los pehuenche según la ficha?", "piñones de la araucaria", "mariscos", "llamas", "La idea 4 habla de recolectar piñones."),
   ("ab", "{F} Un cierre con un dato completamente nuevo es", "poco recomendable", "lo mejor", "El cierre debe resumir lo dicho, no abrir otro tema."),
   ("abc", "{F} ¿Cuántos pueblos o grupos se nombran en el desarrollo de la ficha?", "tres", "uno", "diez", "Se nombran atacameños, mapuche (pehuenche) y kawésqar."),
   ("abc", "Para que la audiencia no mezcle los datos de los pueblos conviene", "ordenarlos con un criterio claro", "decir todo a la vez", "hablar más rápido", "Un criterio como norte a sur facilita seguir las ideas."),
   ("ab", "{F} La idea 1 refuerza", "que los pueblos originarios viven hoy", "que solo existieron antes", "Cierra reconociendo que son pueblos vivos con cultura.")],
  ("abc", "En la organización vecinal te dan 3 minutos para presentar. Ensayas y te pasas por 40 segundos. ¿Qué es lo más sensato?", "reducir ejemplos y ajustar el tiempo de cada parte", "hablar más rápido todo el tiempo", "saltarte el cierre", "Ajustar el contenido mantiene claridad dentro del tiempo."),
  [("En HGCS, al presentar: ¿qué es una palabra clave?", "Una palabra que recuerda una idea importante", "Sirve para apoyar la presentación mientras hablas."),
   ("¿Qué va en el cierre?", "Un resumen de lo más importante", "Así queda una idea final clara."),
   ("¿Por qué conviene repartir el tiempo?", "Para que cada parte tenga su espacio", "Se evita quedarse sin tiempo para el cierre.")],
  ("Con las ideas de la ficha 4, escribe tu guion: una línea para la apertura, tres líneas para el desarrollo (con una palabra clave cada una) y una línea para el cierre. Anota cuántos segundos asignas a cada parte, sumando 180.",
   "Apertura (30 s): tema. Desarrollo (40 s cada una): canales y oasis; piñones; canoa y mariscos. Cierre (30 s): pueblos vivos hoy. Total 180 s.",
   ["usa las cinco ideas", "ordena norte a sur", "los segundos suman 180"],
   ["un guion de cinco líneas con tiempos"],
   ["no sumar 180", "mezclar los datos de dos pueblos"],
   "Pregunta: «¿Cuántos segundos suman todas tus partes?»."),
  "Anota tres palabras clave para recordar la idea de los kawésqar.",
  "Rehace el reparto de tiempo si la presentación dura 4 minutos en vez de 3.")

# ===================================================== clase 5
F = ("Ficha 5 (situación de ejemplo). En la reunión de la organización vecinal de ejemplo «Los Alerces» se debate si el cartel de bienvenida del centro cultural debe incluir una frase sobre los pueblos originarios de la zona. "
     "Dos posturas con razones. Postura 1: «Sí, porque el centro cultural está en un territorio con historia de pueblos originarios y las personas visitantes lo deben saber». "
     "Postura 2: «No, porque el cartel ya tiene muchas palabras». "
     "Datos de apoyo: el cartel tiene espacio para 20 palabras y ya usa 15; la frase propuesta tiene 8 palabras. Un texto de 360 palabras se lee a 120 palabras por minuto.")
K(5, F,
  "Hoy aplico lo aprendido a una situación de la comunidad: presento con voz clara y asumo una postura con razones respetuosas.",
  ["Hablar en público es una habilidad que se aprende practicando. Cuida cuatro cosas: la voz, que debe oírse sin gritar; el ritmo, ni muy rápido ni muy lento; la mirada, que se reparte entre las personas; y el lenguaje, claro y respetuoso. Antes de hablar, ensaya en voz alta con alguien de confianza y mide el tiempo.",
   "Asumir una postura razonada es decir lo que se piensa y dar razones que se apoyen en datos. Una postura se compone de una afirmación, razones y un dato o ejemplo. Por ejemplo: «Conviene incluir la frase porque el territorio tiene historia de pueblos originarios». Se debate sobre ideas, nunca sobre las personas, y se escuchan las razones de quien piensa distinto.",
   "Si alguien pregunta algo que no sabes, es válido decir «no lo sé, lo averiguaré». Eso es más honesto que inventar una respuesta. Y si un dato depende de una comunidad, se dice que lo enseña la propia comunidad."],
  [("postura razonada", "opinión apoyada en razones y datos"), ("ritmo", "la velocidad al hablar"), ("debatir", "intercambiar ideas distintas con respeto"), ("ensayar", "practicar antes de presentar")],
  [("Identificar razones", "Postura 1: «Sí, porque el centro cultural está en un territorio con historia de pueblos originarios». ¿Cuál es la razón?", ["Busco la palabra «porque».", "Después viene la razón."], "Que el centro está en un territorio con historia de pueblos originarios"),
   ("Calcular el tiempo de lectura", "Un texto de 360 palabras se lee a 120 palabras por minuto. ¿Cuántos minutos dura?", ["Divido 360 en 120.", "El resultado es minutos."], "3 minutos")],
  [("Responder a una postura atacando a la persona.", "Se debate sobre ideas, no sobre personas.", "Responde a las razones, no a quien las dice."),
   ("Inventar una respuesta ante una pregunta que no sabes.", "Se pierde la confianza si se descubre el error.", "Di «no lo sé, lo averiguaré» y busca la fuente.")],
  [("abc", "{F} ¿Cuál es la razón de la postura 2?", "que el cartel ya tiene muchas palabras", "que el centro tiene historia", "que el cartel es azul", "La postura 2 se apoya en la cantidad de palabras."),
   ("ab", "{F} ¿Qué postura propone incluir la frase?", "la postura 1", "la postura 2", "La postura 1 dice «Sí» a incluirla."),
   ("=", "{F} El cartel tiene espacio para 20 palabras y ya usa 15. ¿Cuántas palabras quedan libres?", "20-15", "Se resta lo usado al espacio total.", " palabras"),
   ("abc", "{F} La frase propuesta tiene 8 palabras y quedan 5 libres. ¿Cabe sin cambiar nada?", "no, faltan 3 palabras de espacio", "sí, cabe justo", "sí, sobran 3", "Con 5 libres y 8 necesarias, faltan 3 palabras."),
   ("ab", "{F} Para que la frase quepa, una solución razonable es", "acortar la frase o reorganizar el cartel", "borrar el cartel entero", "Ajustar el texto permite incluir la idea sin perder espacio."),
   ("=", "{F} Un texto de 480 palabras se lee a 120 palabras por minuto. ¿Cuántos minutos dura?", "480/120", "Se divide el número de palabras por las palabras de cada minuto.", " minutos"),
   ("abc", "Una postura razonada tiene", "afirmación, razones y un dato o ejemplo", "solo una opinión", "solo un enojo", "Esas partes hacen que la postura se pueda discutir con respeto."),
   ("ab", "Ante una pregunta que no sabes responder, es mejor decir", "no lo sé, lo averiguaré", "cualquier cosa para salir del paso", "Admitir lo que no se sabe es honesto y permite averiguarlo."),
   ("abc", "Al debatir, lo adecuado es", "responder a las razones, no a la persona", "gritar para ganar", "burlarse", "Se debate sobre ideas con respeto."),
   ("abc", "Ensayar sirve para", "medir el tiempo y mejorar el ritmo", "memorizar sin mirar a nadie", "cambiar el tema", "Ensayar permite ajustar tiempo y claridad."),
   ("ab", "Hablar en voz muy baja en una reunión", "dificulta que la audiencia escuche", "es lo mejor", "La voz debe oírse con claridad sin gritar."),
   ("abc", "{F} ¿Qué postura se apoya en un dato sobre el territorio?", "la postura 1", "la postura 2", "ninguna", "La postura 1 habla de la historia del territorio."),
   ("ab", "Si el dato depende de una comunidad, lo correcto es", "decir que lo enseña la propia comunidad", "inventar la versión tradicional", "La forma tradicional la enseñan las personas de la comunidad.")],
  ("abc", "En la reunión, una vecina responde a tu postura diciendo que no estás de acuerdo con tus razones. ¿Qué haces?", "escuchas sus razones y respondes con respeto", "te enojas y levantas la voz", "te vas de la reunión", "Escuchar y responder con respeto mantiene el debate productivo."),
  [("En HGCS, al presentar: ¿qué es una postura razonada?", "Una opinión apoyada en razones y datos", "Se puede discutir con respeto porque tiene razones."),
   ("¿Qué se responde si no sabes un dato?", "No lo sé, lo averiguaré", "Es una respuesta honesta y permite averiguarlo después."),
   ("¿Sobre qué se debate?", "Sobre ideas, no sobre personas", "El respeto sostiene el diálogo entre personas que piensan distinto.")],
  ("Elige la postura 1 o la 2 de la ficha 5 y escribe tu intervención de 30 segundos: una afirmación, una razón con datos de la ficha y una frase para responder con respeto a quien piensa distinto. Léela en voz alta y mide el tiempo.",
   "Creo que conviene incluir la frase porque el territorio tiene historia de pueblos originarios. Con 8 palabras faltarían 3 de espacio, pero se puede acortar. Entiendo que preocupe el espacio.",
   ["usa afirmación y razón", "usa datos de la ficha", "responde con respeto"],
   ["una intervención escrita de 30 segundos"],
   ["dar solo la opinión", "atacar a quien piensa distinto"],
   "Pregunta: «¿Qué razón apoya tu opinión?»."),
  "Ensaya en voz alta una frase de apertura de 10 segundos para tu presentación.",
  "Escribe una razón a favor y una en contra de incluir la frase y decide cuál te convence más.")

# ===================================================== clase 6
F = ("Ficha 6 (pauta de revisión de una presentación oral y un guion de ejemplo). Pauta: 1) Dice el tema al comenzar. 2) Usa al menos dos fuentes con autor. 3) Explica con sus palabras. "
     "4) Cada idea tiene un dato. 5) Cuida el tiempo. 6) Cierra resumiendo. 7) Habla con respeto de los pueblos originarios. "
     "Guion de ejemplo: «Los pueblos originarios ya no existen. Los datos los saqué de un mensaje. Hablé 7 minutos de 3 permitidos y no tuve cierre».")
K(6, F,
  "Hoy reviso una presentación con una pauta, corrijo un guion con errores y decido qué quiero mejorar.",
  ["Una pauta de revisión es una lista de criterios para comprobar un trabajo. Con ella se mira la presentación como lo haría otra persona. En la ficha hay siete preguntas: el tema, las fuentes, las palabras propias, los datos, el tiempo, el cierre y el respeto. Si falta algo, se corrige antes de presentar.",
   "Revisar con la pauta ayuda a encontrar errores en el guion de ejemplo: dice que los pueblos originarios ya no existen, lo que no es cierto; usa un mensaje sin autor como fuente; se pasa de tiempo y no tiene cierre. Cada error se corrige con una acción concreta: cambiar la frase, buscar una fuente con autor, recortar ideas y escribir un cierre.",
   "Al terminar, haz un balance: qué hice bien, qué mejoraré y qué quiero repasar. Reconocer lo logrado y lo pendiente es parte de aprender."],
  [("pauta", "lista de criterios para revisar un trabajo"), ("corregir", "cambiar algo para que quede bien"), ("balance", "mirar lo que se logró y lo que falta"), ("criterio", "regla para juzgar un trabajo")],
  [("Aplicar la pauta", "En el guion de ejemplo, ¿qué criterio no cumple «los datos los saqué de un mensaje»?", ["Busco el criterio de las fuentes.", "Es el criterio 2."], "El 2: usar al menos dos fuentes con autor"),
   ("Corregir una frase", "Corrige «los pueblos originarios ya no existen».", ["La frase es falsa: los pueblos originarios viven hoy.", "Escribo una versión correcta."], "Los pueblos originarios viven hoy y mantienen su cultura")],
  [("Corregir el error sin explicar por qué.", "La persona no entiende cómo mejorar.", "Di qué criterio falla y cómo corregirlo."),
   ("Pensar que una pauta solo sirve para poner nota.", "Sirve para mejorar antes de presentar.", "Úsala como lista de verificación.")],
  [("abc", "{F} ¿Qué criterio incumple «ya no existen»?", "el 7: hablar con respeto de los pueblos originarios", "el 5: cuidar el tiempo", "el 1: decir el tema", "La frase borra a pueblos que viven hoy, lo que no es respetuoso ni exacto."),
   ("abc", "{F} ¿Qué criterio incumple hablar 7 minutos de 3 permitidos?", "el 5: cuidar el tiempo", "el 7", "el 2", "Se pasó del tiempo que estaba permitido."),
   ("ab", "{F} ¿Qué criterio incumple «no tuve cierre»?", "el 6: cerrar resumiendo", "el 4: cada idea tiene un dato", "Sin cierre no se resume lo más importante."),
   ("=", "{F} Si hablaste 7 minutos de 3 permitidos, ¿cuántos minutos te pasaste?", "7-3", "Se resta el tiempo permitido del usado.", " minutos"),
   ("abc", "{F} ¿Cuántos criterios tiene la pauta?", "siete", "tres", "diez", "La ficha lista siete criterios para revisar."),
   ("ab", "{F} Una buena corrección de «los datos los saqué de un mensaje» es", "buscar una fuente con autor que confirme", "mantener el mensaje", "Una fuente con autor se puede comprobar."),
   ("abc", "Un balance sirve para", "ver lo logrado y lo que falta mejorar", "ocultar errores", "dar premios", "Mirar lo logrado y lo pendiente orienta el aprendizaje."),
   ("abc", "Si una presentación no tiene tema claro al comienzo, falla el criterio", "1", "5", "7", "El criterio 1 pide decir el tema al comenzar."),
   ("ab", "Revisar con una pauta antes de presentar permite", "corregir los errores a tiempo", "no ensayar", "Detectar errores antes mejora el resultado."),
   ("abc", "Si una compañera olvida citar una fuente, lo más respetuoso es", "recordárselo con amabilidad y mostrar cómo hacerlo", "reírse", "ignorarlo", "Corregir con amabilidad ayuda a aprender."),
   ("abc", "{F} ¿Qué criterio se cumple si explica con sus palabras?", "el 3", "el 5", "el 7", "El criterio 3 pide explicar con palabras propias."),
   ("ab", "{F} El criterio 4 pide que", "cada idea tenga un dato", "cada idea tenga una canción", "Los datos dan respaldo a cada idea."),
   ("abc", "Una frase respetuosa para cerrar una presentación sobre pueblos originarios es", "los pueblos originarios viven hoy y mantienen su cultura", "ya no quedan", "no tienen cultura", "Reconoce su presencia actual y su cultura.")],
  ("abc", "Terminas de ensayar y notas que te falta citar una fuente y que te pasaste del tiempo. ¿Qué haces?", "agregas la cita y recortas una idea", "no cambias nada", "hablas más rápido", "Corriges lo que la pauta señala antes de presentar."),
  [("En HGCS, al presentar: ¿para qué sirve una pauta de revisión?", "Para comprobar y mejorar un trabajo", "Cada criterio señala algo que revisar."),
   ("¿Qué se corrige si una frase dice que los pueblos ya no existen?", "Se reemplaza por una frase que reconozca que viven hoy", "La frase corregida es exacta y respetuosa."),
   ("¿Qué es un balance?", "Mirar lo logrado y lo pendiente", "Permite decidir qué conviene repasar después.")],
  ("Reescribe el guion de ejemplo en cuatro frases correctas: una para cada error (pueblos que no existen, fuente sin autor, tiempo excedido y cierre ausente). Termina con una línea de balance con lo que quieres mejorar.",
   "Los pueblos originarios viven hoy y mantienen su cultura. Usaré fuentes con autor. Ajustaré el discurso a 3 minutos. Cerraré resumiendo lo importante. Quiero mejorar el ritmo.",
   ["corrige los cuatro errores", "usa lenguaje respetuoso", "incluye un balance"],
   ["cuatro frases y una línea de balance"],
   ["repetir el error", "no hacer balance"],
   "Pregunta: «¿Qué criterio de la pauta cumple ahora cada frase?»."),
  "Anota dos criterios de la pauta que ya cumples y uno que quieres practicar.",
  "Escribe cómo explicarías la pauta a una persona que va a presentar por primera vez.")
