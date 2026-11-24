"""Historia, Geografía y Ciencias Sociales EPJA Básica N2, módulo 3 (parte 4): OAD-12, inferir cómo los paisajes de Chile se relacionan con la cultura y la cosmovisión de los pueblos originarios y comunicarlo en un afiche. Todos los afiches, mapas y fotos están descritos con palabras; datos y textos de ejemplo."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel (una hoja tamaño oficio o más grande), lápices de color o plumones si se tienen, regla y goma. Los afiches, fotografías y mapas están descritos con palabras en la ficha de cada clase y son de ejemplo. Lo que cada comunidad enseña sobre su propia cultura lo transmiten las personas de esa comunidad."
build = make_build(MATERIALS)

O = "EPJA-HGCS-NB2-OAD-12"
PRIOR = ["He visto afiches en la calle, el consultorio o la biblioteca.", "Sé que Chile tiene paisajes distintos de norte a sur.", "Conozco algunos pueblos originarios y dónde viven."]


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    build(O, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ===================================================== clase 1
F = ("Ficha 1 (afiche de ejemplo descrito con palabras). Título grande en la parte de arriba: «Feria del barrio». En el centro, un dibujo de puestos con toldos de colores. "
     "Debajo, tres líneas breves: «Sábado, 10 a 14 horas», «Plaza Los Aromos» y «Trae tu bolsa». En el borde inferior, en letra pequeña, el nombre de la organización vecinal de ejemplo. "
     "Anotación de una persona mayor del barrio sobre otro afiche: «En el sur llovía mucho, por eso las casas tenían techos inclinados».")
K(1, F,
  "Hoy parto de los afiches que veo en mi vida diaria para entender cómo se comunica una idea con imagen y pocas palabras, y qué es inferir.",
  ["Un afiche es un cartel que comunica una idea con una imagen y pocas palabras. Tú ya los lees en la calle, en la biblioteca o en el consultorio. Un buen afiche tiene un título grande, una imagen que apoya la idea, un texto breve con los datos importantes y se entiende rápido, incluso desde lejos.",
   "Inferir es sacar una conclusión a partir de pistas y de lo que ya sabes. La persona mayor de la ficha dice: «En el sur llovía mucho, por eso las casas tenían techos inclinados». Con una pista (la lluvia) y un conocimiento (el agua resbala por un techo inclinado) se puede explicar una costumbre. Así, el paisaje ayuda a entender cómo viven las personas.",
   "En esta unidad vamos a inferir cómo los distintos paisajes de Chile se relacionan con la cultura y la cosmovisión de los pueblos originarios, y a comunicarlo en un afiche. Hoy practicamos con afiches de la vida diaria y con inferencias sencillas."],
  [("afiche", "cartel con imagen y pocas palabras que comunica una idea"), ("inferir", "sacar una conclusión a partir de pistas y de lo que ya se sabe"), ("pista", "dato que ayuda a entender algo"), ("título", "frase grande que dice de qué trata el afiche")],
  [("Leer un afiche", "En el afiche de la ficha, ¿cuál es el título?", ["Busco la frase más grande, arriba.", "La copio tal cual."], "«Feria del barrio»"),
   ("Inferir con una pista", "Pista: en un lugar llueve mucho todo el año. ¿Qué es esperable que las casas tengan?", ["Pienso: ¿qué pasa con el agua en el techo?", "Un techo inclinado la deja escurrir."], "Techos inclinados para que el agua escurra")],
  [("Poner demasiado texto en un afiche.", "No se alcanza a leer desde lejos.", "Usa frases cortas y deja espacio vacío."),
   ("Tomar una inferencia como un hecho seguro.", "Una inferencia es una conclusión probable, no una certeza.", "Usa palabras como «probablemente» o «es posible que».")],
  [("abc", "{F} ¿Qué día dice el afiche que se hará la feria?", "sábado", "domingo", "lunes", "La primera línea breve dice sábado de 10 a 14 horas."),
   ("abc", "{F} ¿Dónde se hará la feria?", "en la Plaza Los Aromos", "en la biblioteca", "en el consultorio", "La segunda línea breve nombra la Plaza Los Aromos."),
   ("ab", "{F} ¿Qué parte del afiche es el dibujo de los puestos con toldos?", "la imagen", "el título", "El dibujo central es la imagen que apoya la idea."),
   ("=", "{F} La feria es de 10 a 14 horas. ¿Cuántas horas dura?", "14-10", "Se resta la hora de inicio de la de término.", " horas"),
   ("abc", "Un afiche debe tener", "un título grande, una imagen y texto breve", "mucho texto pequeño y sin imagen", "solo una lista de nombres", "Un afiche eficaz se entiende rápido, con pocas palabras y una imagen."),
   ("ab", "Inferir es", "sacar una conclusión a partir de pistas y de lo que ya sabes", "copiar una frase", "Inferir une pistas con conocimientos para llegar a una conclusión."),
   ("abc", "{F} ¿Cuántas líneas breves de texto tiene el afiche debajo del dibujo?", "tres", "una", "seis", "La ficha dice que son tres: día y hora, lugar e indicación."),
   ("abc", "Pista: un lugar es muy seco y casi no tiene agua. ¿Qué es esperable que valoren más sus habitantes?", "el agua", "los paraguas", "las botas de goma", "Donde hay poca agua, se la cuida y valora."),
   ("ab", "{F} La frase «Trae tu bolsa» del afiche es", "una indicación breve", "un título", "Es una de las tres líneas de texto breve con datos."),
   ("abc", "{F} La parte inferior del afiche, en letra pequeña, indica", "la organización que lo hizo", "el precio de los puestos", "la lluvia", "La ficha dice que ahí va el nombre de la organización vecinal."),
   ("ab", "Una inferencia es", "una conclusión probable apoyada en pistas", "un dato seguro e imposible de discutir", "Se apoya en pistas y puede revisarse con más información."),
   ("abc", "Un afiche con mucho texto en letra pequeña tiene el problema de", "no leerse desde lejos", "ser muy colorido", "tener título", "La lectura rápida se dificulta con mucha letra pequeña."),
   ("abc", "Una buena palabra para expresar que una inferencia no es totalmente segura es", "probablemente", "siempre", "jamás", "«Probablemente» muestra que es una conclusión posible, no una certeza.")],
  ("abc", "En la biblioteca ves un afiche que anuncia una charla. Tiene un título enorme, una foto y las tres líneas de fecha, hora y lugar. ¿Por qué se entiende rápido?", "porque tiene poco texto, imagen y datos claros", "porque usa muchas palabras", "porque no tiene imagen", "La combinación de título, imagen y datos breves facilita la lectura."),
  [("En Historia: ¿qué es inferir?", "Sacar una conclusión a partir de pistas", "Se usa lo observado y lo que ya se sabe."),
   ("¿Qué partes tiene un afiche?", "Título, imagen y texto breve", "Se leen rápido y comunican la idea."),
   ("¿Qué palabras muestran que una inferencia no es una certeza?", "Probablemente o es posible que", "Dejan abierta la posibilidad de revisar.")],
  ("Con la persona mayor de la ficha o con tu propia experiencia, completa esta frase de inferencia: «En un lugar donde ___, probablemente las personas ___, porque ___». Escribe dos frases distintas. Luego dibuja el boceto de un afiche con título, imagen y una línea de texto para una de ellas.",
   "En un lugar donde llueve mucho, probablemente las casas tienen techos inclinados, porque el agua escurre. Boceto: título «Techos para la lluvia», dibujo de una casa, línea: «El agua escurre».",
   ["usa pista y conocimiento", "usa «probablemente»", "el boceto tiene título, imagen y texto breve"],
   ["dos frases y un boceto"],
   ["decir que es seguro", "escribir mucho texto en el boceto"],
   "Pregunta: «¿Qué pista te hizo pensar eso?»."),
  "Anota un afiche que hayas visto esta semana y qué parte de él te llamó la atención primero.",
  "Escribe una inferencia sobre cómo un paisaje que conozcas influye en cómo viven las personas allí.")

# ===================================================== clase 2
F = ("Ficha 2 (tabla de ejemplo, resumen general). Paisaje | Pista del paisaje | Rasgo cultural asociado | Cosmovisión asociada. "
     "Desierto y oasis del norte | muy poca agua | canales para cuidar y repartir el agua | el agua se valora y se cuida. "
     "Altiplano | frío y a gran altura | terrazas de cultivo, cría de llamas y alpacas | la Pachamama es la Madre Tierra. "
     "Bosques y lagos del sur | mucha lluvia y madera | casas de madera y paja, recolección de piñones | la tierra y el pehuén son respetados. "
     "Canales e islas del extremo sur | mucha agua de mar | canoas y alimentación con mariscos | el mar y los canales son el hogar. "
     "Isla volcánica del Pacífico | aislada en el océano, con piedra volcánica | esculturas de piedra llamadas moai | la relación con los antepasados y el territorio es muy importante.")
K(2, F,
  "Hoy aprendo palabras clave y leo una tabla que relaciona paisajes con rasgos culturales y cosmovisión de pueblos originarios.",
  ["Un paisaje es lo que se ve de un lugar: relieve, plantas, agua y construcciones. Los pueblos originarios habitaron paisajes muy distintos, y esos paisajes les ofrecieron recursos y también desafíos. Así, en un desierto el agua es lo más valioso, y en una zona de canales el mar es el camino y el alimento.",
   "La relación entre paisaje y cultura se ve en los rasgos culturales: las técnicas, las construcciones, los alimentos y las fiestas. Y se ve en la cosmovisión: la manera de entender la naturaleza. Por eso, quien vive del mar y quien vive del altiplano cuentan el mundo de formas distintas, pero ambos suelen respetar la naturaleza de la que dependen.",
   "La tabla de la ficha es un resumen. Sirve para inferir y no para encasillar: cada pueblo tiene su historia, y hoy muchas personas de estos pueblos viven en ciudades. Si algo no está en la tabla, no se puede afirmar solo con ella."],
  [("paisaje", "lo que se ve de un lugar: relieve, plantas, agua y construcciones"), ("rasgo cultural", "técnica, construcción, alimento o fiesta propios de un pueblo"), ("cosmovisión", "manera de entender el mundo y la naturaleza"), ("desafío", "dificultad que hay que enfrentar")],
  [("Leer una fila", "Según la tabla, ¿qué rasgo cultural se asocia a los canales e islas del extremo sur?", ["Busco la fila de canales e islas.", "Leo la tercera columna."], "Canoas y alimentación con mariscos"),
   ("Relacionar", "En el desierto con oasis, ¿cómo se relaciona la pista del paisaje con el rasgo cultural?", ["El paisaje tiene muy poca agua.", "Entonces se construyen canales para cuidarla."], "La falta de agua se relaciona con los canales para cuidarla y repartirla")],
  [("Pensar que todo lo cultural viene solo del paisaje.", "También influyen la historia y las decisiones de cada pueblo.", "Usa «se relaciona» y no «viene solo de»."),
   ("Encasillar a una persona por el paisaje de su pueblo.", "Cada persona es distinta y hoy muchas viven en ciudades.", "Habla de pueblos y no de «todos los individuos».")],
  [("abc", "{F} ¿Qué pista del paisaje tiene el desierto y oasis del norte?", "muy poca agua", "mucha lluvia", "mucho frío", "La primera fila dice que hay muy poca agua."),
   ("abc", "{F} ¿Qué rasgo cultural se asocia a los bosques y lagos del sur?", "casas de madera y paja, y recolección de piñones", "terrazas de cultivo", "esculturas de piedra", "La tercera fila nombra casas de madera y paja y piñones."),
   ("ab", "{F} ¿Qué cosmovisión se asocia al altiplano?", "la Pachamama es la Madre Tierra", "el mar es el hogar", "La fila del altiplano asocia la Pachamama como Madre Tierra."),
   ("abc", "{F} ¿Qué pista tiene la isla volcánica del Pacífico?", "aislada en el océano, con piedra volcánica", "mucho bosque", "desierto de arena", "La última fila nombra su aislamiento y la piedra volcánica."),
   ("abc", "{F} ¿Qué rasgo cultural se asocia a la isla volcánica del Pacífico?", "esculturas de piedra llamadas moai", "canoas de corteza", "terrazas", "La fila de la isla nombra los moai."),
   ("ab", "{F} Un paisaje con mucha lluvia y madera favorece", "casas de madera", "terrazas en laderas de desierto", "La tabla relaciona los bosques con casas de madera."),
   ("abc", "{F} ¿Cuál inferencia se apoya mejor en la tabla?", "como el altiplano es frío y alto, probablemente se crían llamas y alpacas", "como hay desierto, probablemente se pesca en el mar", "como hay bosques, no se usa madera", "La tabla asocia el altiplano con llamas y alpacas."),
   ("abc", "{F} ¿Qué parte de la tabla es la cosmovisión del extremo sur?", "el mar y los canales son el hogar", "las canoas", "los mariscos", "La cuarta columna de esa fila es la cosmovisión."),
   ("ab", "Un paisaje ofrece recursos y", "también desafíos", "nunca desafíos", "Los paisajes ofrecen recursos, pero también dificultades como el frío o la sequía."),
   ("abc", "{F} Un estudiante dice «los pueblos del desierto no valoran el agua». Según la tabla, es", "falso: el agua se valora y se cuida", "verdadero", "irrelevante", "La tabla dice que allí el agua se valora y se cuida."),
   ("abc", "¿Por qué una tabla es solo un resumen?", "porque cada pueblo tiene su propia historia y hoy muchas personas viven en ciudades", "porque está mal hecha", "porque no tiene datos", "Un resumen no abarca toda la diversidad."),
   ("ab", "{F} Un rasgo cultural es", "una técnica o construcción propia de un pueblo", "una nube del cielo", "Los rasgos culturales son técnicas, construcciones, alimentos o fiestas."),
   ("abc", "{F} ¿Cuál de estas es una pista del paisaje?", "mucha agua de mar", "las canoas", "la cosmovisión", "Las canoas son un rasgo cultural; la abundancia de agua de mar es una característica del paisaje.")],
  ("abc", "Un cartel de una exposición dice: «Quienes vivían en el desierto ponían canales para llevar agua a las parcelas». ¿Qué inferencia se desprende?", "el agua era un recurso muy valioso", "el agua era abundante y barata", "no había parcelas", "Quien construye canales para llevar agua la considera valiosa."),
  [("Al relacionar cultura y territorio, ¿qué es un paisaje?", "Lo que se ve de un lugar", "Incluye relieve, plantas, agua y construcciones del lugar."),
   ("¿Qué es un rasgo cultural?", "Una técnica, construcción o costumbre de un pueblo", "Los rasgos culturales expresan cómo vive un pueblo."),
   ("¿Para qué sirve la tabla del paisaje y la cultura?", "Para inferir relaciones, sin encasillar", "Es un resumen y no abarca toda la diversidad.")],
  ("Con la tabla de la ficha 2, elige dos filas y escribe, para cada una, una inferencia con la estructura «En un lugar con ___, probablemente ___, porque ___». Agrega una frase que recuerde que la tabla es un resumen.",
   "En un lugar con muy poca agua, probablemente se construyen canales, porque el agua es valiosa. En un lugar con mucha agua de mar, probablemente se usan canoas, porque el mar es el camino. La tabla es un resumen.",
   ["usa la estructura", "relaciona paisaje y cultura", "advierte que es un resumen"],
   ["dos inferencias y una advertencia"],
   ["decir que es seguro", "inventar rasgos que la tabla no tiene"],
   "Pregunta: «¿Qué fila de la tabla respalda tu inferencia?»."),
  "Elige un paisaje de la tabla y dibuja tres elementos que lo representen.",
  "Explica con tus palabras por qué un paisaje no determina por completo la cultura de un pueblo.")

# ===================================================== clase 3
F = ("Ficha 3 (método de inferencia y tres casos de ejemplo). Método: 1) Observo la pista del paisaje. 2) Recuerdo lo que sé del paisaje y los recursos. "
     "3) Armo la conclusión con «probablemente» y «porque». 4) Reviso si la conclusión sirve para otro pueblo o es solo para este. "
     "Caso A: valle del norte chico con ríos que bajan de la cordillera. Caso B: bosque del sur con lluvia todo el año. Caso C: canales con viento y oleaje fuerte.")
K(3, F,
  "Hoy sigo cuatro pasos para inferir cómo un paisaje se relaciona con la cultura y la cosmovisión, y los aplico a tres casos.",
  ["Para inferir con orden, seguimos cuatro pasos. Primero, observa la pista del paisaje: agua, relieve, clima o plantas. Segundo, recuerda lo que sabes sobre ese paisaje y sus recursos. Tercero, arma una conclusión con «probablemente» y «porque». Cuarto, revisa: ¿esta conclusión es cierta solo para este pueblo o sirve para otros? Si no tienes datos, dilo.",
   "Por ejemplo, en un valle con ríos que bajan de la cordillera, hay agua para regar. Probablemente, entonces, se cultiva en las orillas, porque allí hay agua y suelo. Una buena inferencia no dice «todos hacían lo mismo»: dice qué es probable y deja lugar a comprobarlo en una fuente.",
   "Las inferencias también se pueden aplicar a la cosmovisión. Si un pueblo depende del agua de un río, es esperable que el río tenga un valor especial para él. Pero ojo: la forma exacta de esa creencia solo la conoce y enseña la comunidad. Nuestro trabajo es inferir con respeto y decir qué falta por consultar."],
  [("pista del paisaje", "dato del lugar que ayuda a inferir"), ("conclusión", "idea final a la que se llega con datos"), ("comprobar", "revisar con una fuente si algo es cierto"), ("valle", "terreno bajo entre cerros o cordilleras")],
  [("Aplicar los pasos al caso A", "Caso A: valle con ríos que bajan de la cordillera. ¿Qué conclusión probable sobre cultivos?", ["Pista: hay ríos.", "Conclusión: se cultiva cerca del agua."], "Probablemente se cultiva en las orillas de los ríos, porque allí hay agua"),
   ("Revisar", "Una persona dice: «Todos los pueblos con ríos cultivan igual». ¿Qué falla?", ["La palabra «todos» generaliza.", "Cada pueblo tiene sus propias técnicas."], "Generaliza: no todos cultivan igual")],
  [("Concluir sin nombrar la pista.", "No se sabe en qué se apoya.", "Nombra la pista del paisaje antes de concluir."),
   ("Usar «seguro» en una inferencia sin datos.", "Una inferencia es probable, no segura.", "Usa «probablemente» o «es posible que».")],
  [("abc", "{F} ¿Cuál es el primer paso del método?", "observar la pista del paisaje", "revisar la conclusión", "dibujar el afiche", "Todo parte de lo que se observa en el paisaje."),
   ("abc", "{F} ¿Cuál es el cuarto paso?", "revisar si la conclusión sirve para otros pueblos o solo para este", "inventar un dato", "borrar el caso", "El cuarto paso pide revisar el alcance de la conclusión."),
   ("ab", "{F} En el caso B (bosque con lluvia todo el año), una pista del paisaje es", "la lluvia y la madera", "el desierto", "El caso B menciona lluvia, y los bosques ofrecen madera."),
   ("abc", "{F} En el caso B, ¿qué conclusión es más probable?", "probablemente se usa la madera para construir, porque abunda", "probablemente se usa piedra del desierto", "no se construye nada", "La madera abunda en un bosque, por eso es un material probable."),
   ("abc", "{F} En el caso C (canales con viento y oleaje), ¿qué inferencia es razonable?", "probablemente se navega con canoas resistentes y con conocimiento del mar", "probablemente se cultiva trigo", "probablemente no hay agua", "En un paisaje de canales, la navegación es un medio de moverse."),
   ("ab", "{F} ¿Qué palabra debe llevar la conclusión del paso 3?", "probablemente", "seguro", "«Probablemente» y «porque» muestran que es una inferencia razonada."),
   ("abc", "En un valle con río, ¿qué recurso natural es la pista principal?", "el agua del río", "la nieve del desierto", "la playa", "El río entrega agua para regar y beber."),
   ("ab", "Para saber si una inferencia es cierta, hay que", "comprobarla en una fuente", "creerla sin revisar", "Una inferencia se confirma o se corrige con fuentes."),
   ("abc", "{F} ¿Qué falla tiene la frase «todos los pueblos del valle hacían exactamente lo mismo»?", "generaliza", "es muy corta", "habla de ríos", "«Todos» ignora las diferencias entre pueblos."),
   ("abc", "Si un río es muy importante para un pueblo, ¿qué es esperable en su cosmovisión?", "que el río tenga un valor especial", "que no importe", "que se oculte", "Quien depende de algo suele valorarlo mucho."),
   ("ab", "La forma exacta de una creencia de un pueblo la enseña", "la propia comunidad", "cualquier persona que la invente", "Las creencias las conocen y las explican las comunidades."),
   ("abc", "{F} ¿Qué caso tiene como pista un río que baja de la cordillera?", "el caso A", "el caso B", "el caso C", "El caso A describe un valle con ríos."),
   ("ab", "{F} Si no tienes datos para completar una inferencia, lo honesto es", "decir que falta información", "inventar el dato", "Reconocer lo que falta evita errores.")],
  ("abc", "En una charla comunitaria alguien dice: «En la zona donde llueve todo el año, seguro todos vivían en casas de madera». ¿Cómo la reformulas?", "probablemente muchas casas eran de madera, porque abunda", "todos vivían en cuevas", "no se puede decir nada nunca", "Se cambia «seguro» por «probablemente» y se da una razón."),
  [("En Geografía: ¿qué es una pista del paisaje?", "Un dato del lugar que ayuda a inferir", "Puede ser agua, relieve, clima o plantas."),
   ("¿Cuáles son los cuatro pasos para inferir?", "Observar, recordar, concluir con probablemente y revisar", "Ordenan el razonamiento para no saltar pasos."),
   ("¿Quién enseña la forma exacta de una creencia?", "La comunidad que la vive", "Su sentido lo conocen quienes la practican.")],
  ("Aplica el método de la ficha 3 al caso C (canales con viento y oleaje fuerte): escribe los cuatro pasos en cuatro líneas, con una conclusión que use «probablemente» y «porque», y di qué fuente te serviría para comprobarla.",
   "1) Hay viento y oleaje en canales. 2) El mar es el camino y la fuente de alimento. 3) Probablemente se navegaba con canoas, porque el territorio es de agua. 4) No sirve para el desierto. Fuente: panel o libro sobre pueblos de los canales.",
   ["cuatro pasos escritos", "conclusión con probablemente y porque", "propone una fuente"],
   ["cuatro líneas y una fuente propuesta"],
   ["omitir la pista", "afirmar algo sin fuente"],
   "Pregunta: «¿Qué fuente podría confirmar tu conclusión?»."),
  "Aplica el método al caso A y escribe una conclusión con probablemente y porque.",
  "Escribe qué dato necesitarías para convertir tu inferencia del caso B en un dato comprobado.")

# ===================================================== clase 4
F = ("Ficha 4 (tres bocetos de afiche de ejemplo para el tema «Paisaje y cultura»). "
     "Boceto A: título en letra muy pequeña; un bloque de 120 palabras; sin imagen. "
     "Boceto B: título grande «Agua y cultura en el norte»; imagen de un canal con parcelas verdes en el desierto; tres líneas de texto breve; abajo, en letra pequeña, las fuentes. "
     "Boceto C: solo una imagen de un desierto; sin título ni texto. "
     "Texto del boceto B: «En el desierto, el agua es lo más valioso» / «Los canales la reparten a las parcelas» / «Se la cuida y se la agradece».")
K(4, F,
  "Hoy practico con apoyo cómo pasar de una inferencia a un afiche que se lea rápido, con título, imagen, texto breve y fuentes.",
  ["Un afiche sobre paisaje y cultura convierte una inferencia en un mensaje visual. Elige una idea central, por ejemplo: «en el desierto el agua es lo más valioso». El título la dice en pocas palabras. La imagen la muestra, por ejemplo, un canal con parcelas verdes. El texto breve da dos o tres datos que la explican. Y las fuentes, en letra pequeña, permiten comprobarla.",
   "Un buen afiche se entiende en pocos segundos. Para eso se usa un título grande, letras claras y de color contrastante, espacio libre alrededor y no más de unas cuarenta palabras. La imagen y el texto se apoyan entre sí: la imagen no contradice lo que dice el texto. Los datos deben ser los que investigaste, no suposiciones.",
   "Al tratar de pueblos originarios, evita imágenes de disfraces o estereotipos y no uses símbolos sagrados sin permiso de la comunidad. Mejor usa imágenes del paisaje y de actividades que tu fuente describa, y menciona que estos pueblos viven hoy."],
  [("idea central", "mensaje principal de un afiche"), ("contraste", "diferencia clara entre colores, por ejemplo letra oscura sobre fondo claro"), ("boceto", "dibujo rápido que muestra cómo quedará algo"), ("estereotipo", "imagen simplificada y falsa sobre un grupo")],
  [("Elegir el mejor boceto", "Entre los tres bocetos de la ficha, ¿cuál se leerá mejor desde lejos?", ["Busco título grande, imagen y texto breve.", "Ese es el boceto B."], "El boceto B"),
   ("Contar palabras", "El texto del boceto B tiene tres líneas: 9, 7 y 7 palabras. ¿Cuántas palabras tiene el texto?", ["Sumo las tres líneas.", "9 + 7 + 7."], "23 palabras")],
  [("Poner una imagen que contradice el texto.", "Confunde a quien lee.", "Revisa que imagen y texto digan lo mismo."),
   ("Usar una imagen estereotipada de un pueblo originario.", "Reduce al pueblo a una caricatura.", "Usa imágenes del paisaje o actividades descritas en fuentes.")],
  [("abc", "{F} ¿Cuál boceto tiene un título grande?", "el B", "el A", "el C", "La ficha dice que el título del boceto B es grande."),
   ("abc", "{F} ¿Qué problema principal tiene el boceto A?", "mucho texto en un bloque y título pequeño", "demasiada imagen", "tiene fuentes", "Un bloque de 120 palabras no se lee rápido."),
   ("ab", "{F} ¿Qué le falta al boceto C?", "título y texto", "imagen", "Solo tiene una imagen, sin título ni texto."),
   ("=", "{F} Cuenta las palabras de las tres líneas del texto del boceto B (9, 7 y 7 palabras). ¿Cuántas suma el texto, sin contar el título?", "9+7+7", "Se suman las palabras de las tres líneas.", " palabras"),
   ("abc", "{F} ¿Dónde van las fuentes del boceto B?", "abajo, en letra pequeña", "en el título", "en el centro, en grande", "La ficha las ubica abajo en letra pequeña."),
   ("ab", "{F} ¿Qué imagen tiene el boceto B?", "un canal con parcelas verdes en el desierto", "una nevada", "La imagen del boceto B muestra un canal con parcelas verdes."),
   ("abc", "Un afiche debe tener, como máximo, unas", "cuarenta palabras", "cuatrocientas palabras", "cuatro mil palabras", "Pocas palabras permiten leerlo rápido y desde lejos."),
   ("abc", "El contraste en un afiche ayuda a", "que se lea con facilidad", "que se vea oscuro", "ahorrar tinta", "Letra oscura sobre fondo claro es más legible."),
   ("ab", "{F} Si la imagen muestra un canal con agua y el texto dice «hay un desierto sin agua», hay", "una contradicción", "una idea perfecta", "La imagen y el texto deben apoyarse, no contradecirse."),
   ("abc", "¿Cuál es la idea central del boceto B?", "en el desierto el agua es lo más valioso", "el desierto no tiene vida", "los pueblos ya no existen", "El título y el texto repiten esa idea."),
   ("ab", "Para dibujar a un pueblo originario en un afiche, conviene", "usar imágenes del paisaje y actividades descritas en fuentes", "dibujar disfraces", "Los estereotipos reducen a un pueblo a una caricatura."),
   ("abc", "{F} ¿Qué pregunta ayuda a decidir si un boceto es bueno?", "¿se entiende en pocos segundos?", "¿tiene muchas palabras?", "¿es grande?", "La rapidez de lectura mide la eficacia."),
   ("abc", "{F} ¿Qué falta en el boceto A además de imagen?", "un título legible", "más palabras", "un fondo negro", "El título en letra muy pequeña no ayuda a leerlo.")],
  ("abc", "La organización vecinal te pide un afiche para la biblioteca sobre «el agua en los pueblos del norte». Tienes tres ideas. ¿Cuál es la mejor?", "título grande, imagen de un canal y tres líneas con fuentes abajo", "una página llena de texto", "solo una foto sin título", "Es la que se entiende rápido y se puede comprobar."),
  [("En un afiche: ¿qué es el contraste de colores?", "Una diferencia clara que ayuda a leer", "Letra oscura sobre fondo claro se lee mejor."),
   ("¿Qué es una idea central?", "El mensaje principal del afiche", "Debe aparecer en el título del afiche."),
   ("En un afiche, ¿por qué conviene evitar los estereotipos?", "Porque reducen a un pueblo a una caricatura", "Mejor usar imágenes del paisaje y las actividades descritas en las fuentes.")],
  ("Diseña un boceto de afiche para la idea «En el desierto el agua es lo más valioso». Escribe el título, describe la imagen en una línea y escribe tres líneas de texto de no más de 8 palabras cada una. Agrega una línea de fuentes.",
   "Título: «Agua y cultura en el norte». Imagen: un canal con parcelas verdes. Texto: «El agua es valiosa» / «Los canales la reparten» / «Se la cuida». Fuentes: panel de museo, de ejemplo.",
   ["título, imagen, tres líneas y fuentes", "no más de 8 palabras por línea", "imagen y texto coinciden"],
   ["un boceto con cinco partes"],
   ["poner más texto del permitido", "no citar fuentes"],
   "Pregunta: «¿Se lee en pocos segundos?»."),
  "Dibuja el boceto de un afiche con título, imagen y texto breve sobre el paisaje de tu región.",
  "Escribe dos cambios que harías al boceto A para mejorarlo.")

# ===================================================== clase 5
F = ("Ficha 5 (encargo de ejemplo). La biblioteca municipal de ejemplo pide un afiche sobre «Paisaje y cultura de los pueblos originarios». Condiciones: texto de hasta 40 palabras; el afiche se verá a dos metros de distancia; debe incluir las fuentes. "
     "Borrador de ejemplo: título de 6 palabras, tres frases de 8 palabras cada una. "
     "Fuentes de ejemplo disponibles: un panel de museo con autor y un mensaje reenviado sin autor. "
     "Idea de la autora: «En el sur, mucha lluvia y madera: casas de madera y recolección de piñones».")
K(5, F,
  "Hoy aplico lo aprendido a un encargo de la comunidad: diseño un afiche con inferencias claras, buen diseño, fuentes confiables y respeto.",
  ["Un encargo real tiene condiciones: cantidad de palabras, distancia de lectura y fuentes. Antes de diseñar, revisa el encargo con atención. Si el afiche se verá a dos metros, el título y el texto deben ser grandes, y el contraste, claro. Si el límite es de cuarenta palabras, se cuentan y se ajustan.",
   "El contenido se arma con la inferencia: pista del paisaje, rasgo cultural y cosmovisión. La idea de la ficha dice que en el sur hay mucha lluvia y madera, y que eso se relaciona con casas de madera y recolección de piñones. La inferencia debe decirse con «probablemente» o con un dato de la fuente. Elige solo fuentes confiables: el panel con autor, no el mensaje sin autor.",
   "Antes de entregar, revisa con una pauta: ¿se entiende rápido?, ¿cumple las palabras y la distancia?, ¿tiene fuentes confiables?, ¿es respetuoso? Si hay un símbolo sagrado, pide permiso a la comunidad o no lo uses."],
  [("encargo", "pedido de un trabajo con condiciones"), ("condición", "requisito que se debe cumplir"), ("fuente confiable", "fuente con autor, fecha y respaldo"), ("pauta", "lista de criterios para revisar")],
  [("Revisar las palabras", "Un borrador tiene un título de 4 palabras y dos frases de 10 palabras. ¿Cuántas palabras suma?", ["Multiplico 2 por 10.", "Sumo el título."], "24 palabras"),
   ("Elegir la fuente", "De las fuentes disponibles, ¿cuál se usa para el afiche?", ["Busco la que tiene autor.", "Descarto el mensaje sin autor."], "El panel de museo con autor")],
  [("Elegir una letra pequeña para ahorrar espacio.", "No se lee a dos metros.", "Aumenta la letra y recorta palabras."),
   ("Usar un mensaje sin autor porque «lo dice mucha gente».", "Compartido no es comprobado.", "Usa el panel con autor o busca otra fuente.")],
  [("=", "{F} El borrador tiene un título de 6 palabras y tres frases de 8 palabras cada una. ¿Cuántas palabras tiene en total?", "6+3*8", "Se suman el título y las tres frases.", " palabras"),
   ("=", "{F} El afiche puede tener hasta 40 palabras y el borrador usa 30. ¿Cuántas palabras de margen quedan?", "40-30", "Se resta lo usado al límite.", " palabras"),
   ("abc", "{F} ¿A qué distancia se verá el afiche, según el encargo?", "a dos metros", "a veinte metros", "en la mano", "El encargo dice que el afiche se verá a dos metros de distancia."),
   ("abc", "{F} Como el afiche se verá a dos metros, el título debe ser", "grande y con buen contraste", "muy pequeño", "del mismo color del fondo", "A dos metros solo se lee lo grande y contrastado."),
   ("ab", "{F} ¿Qué se infiere de la idea de la autora?", "que la lluvia y la madera se relacionan con las casas de madera", "que en el sur hace calor", "La idea une el paisaje (lluvia y madera) con un rasgo cultural."),
   ("abc", "{F} ¿Qué recurso del bosque menciona la idea de la autora?", "madera y piñones", "arena", "agua salada", "La frase menciona madera y la recolección de piñones."),
   ("abc", "{F} La biblioteca pide un afiche que incluya", "las fuentes", "una fotografía de personas sin permiso", "un símbolo sagrado sin consultar", "Las fuentes son una condición del encargo."),
   ("ab", "Si el afiche usa un símbolo sagrado de un pueblo, antes se debe", "pedir permiso a la comunidad", "usarlo sin consultar", "Un símbolo sagrado se usa solo con permiso."),
   ("abc", "Una frase de la inferencia que expresa duda razonable es", "probablemente las casas eran de madera, porque abunda", "las casas eran de madera siempre", "nunca hubo casas", "«Probablemente» y «porque» expresan una conclusión apoyada en datos."),
   ("ab", "{F} Si el texto supera las 40 palabras, lo mejor es", "recortar palabras", "achicar la letra", "Recortar mantiene la legibilidad a dos metros."),
   ("abc", "{F} ¿Qué pregunta de la pauta revisa el respeto?", "¿evita estereotipos y símbolos sagrados sin permiso?", "¿tiene colores?", "¿está en una hoja grande?", "El respeto implica no caricaturizar ni usar símbolos sagrados sin permiso."),
   ("abc", "{F} ¿Cuántas fuentes de las dos disponibles se usan?", "una", "dos", "ninguna", "Solo el panel con autor es una fuente confiable."),
   ("ab", "Al terminar el afiche, conviene", "revisarlo con una pauta", "entregarlo sin mirarlo", "La pauta ayuda a encontrar errores antes de entregar.")],
  ("abc", "Un grupo de vecinos prepara un afiche con la inferencia «en el sur, mucha lluvia y madera». Alguien propone usar un dibujo de personas con ropa de disfraz. ¿Qué conviene?", "usar una imagen del bosque o de una casa de madera descrita en la fuente", "usar el disfraz", "no usar imagen", "Una imagen basada en fuentes respeta al pueblo y evita estereotipos."),
  [("En un afiche: ¿para qué sirve respetar la distancia de lectura?", "Para que el afiche se lea desde donde se verá", "A dos metros se necesita letra grande."),
   ("¿Qué fuente conviene elegir?", "La que tiene autor y respaldo", "Se puede comprobar lo que dice la fuente."),
   ("¿Qué se hace con un símbolo sagrado?", "Se pide permiso a la comunidad", "Es una muestra de respeto hacia la comunidad.")],
  ("Diseña tu afiche final sobre «Paisaje y cultura de los pueblos originarios» usando la tabla de la clase 2: elige un paisaje y escribe el título, la descripción de la imagen, tres líneas de texto (máximo 40 palabras en total) y las fuentes. Cuenta las palabras y anota si cumples el límite.",
   "Título: «Lluvia, madera y piñones». Imagen: bosque con una casa de madera. Texto: «En el sur llueve mucho» / «Probablemente se usa la madera para construir» / «Se recolectan piñones». Fuentes: panel de museo (de ejemplo). Título y texto suman 19 palabras: cumple.",
   ["cuenta las palabras y cumple el límite", "usa fuentes confiables", "usa «probablemente» o dato de fuente"],
   ["un afiche descrito con título, imagen, texto y fuentes"],
   ["superar las 40 palabras", "no citar fuentes"],
   "Pregunta: «¿Cuántas palabras son y cuál es tu fuente?»."),
  "Dibuja tu afiche en una hoja y pide a alguien que lo mire a dos metros para comprobar que se lea.",
  "Anota dos cambios para que tu afiche respete aún más a los pueblos originarios.")

# ===================================================== clase 6
F = ("Ficha 6 (afiche de ejemplo con errores y pauta). Afiche: título «Los indígenas del desierto vivían sin agua»; imagen de personas con disfraz de plumas; texto: «Todos los pueblos hacían lo mismo». Sin fuentes. "
     "Pauta: 1) El título dice la idea central. 2) La inferencia se apoya en una pista del paisaje. 3) Usa palabras como «probablemente», no «todos». "
     "4) La imagen respeta al pueblo y coincide con el texto. 5) Cita fuentes confiables. 6) Reconoce que los pueblos viven hoy.")
K(6, F,
  "Hoy reviso un afiche con una pauta, corrijo los errores y decido qué quiero repasar sobre paisaje, cultura y cosmovisión.",
  ["Revisar un afiche es mirarlo como lo haría otra persona. La pauta de la ficha tiene seis preguntas: el título, la pista del paisaje, el lenguaje de la inferencia, la imagen, las fuentes y el reconocimiento de que los pueblos viven hoy. Cada «no» marca una corrección.",
   "El afiche de ejemplo tiene varios errores. El título dice que vivían sin agua, pero en el desierto había oasis y canales. La imagen usa un disfraz, que es un estereotipo. El texto dice «todos los pueblos hacían lo mismo», que generaliza. Y no cita fuentes ni reconoce que los pueblos existen hoy. Cada error se corrige con una acción concreta.",
   "Al terminar, haz un balance: qué ya sabes hacer y qué quieres practicar. En esta unidad aprendiste a caracterizar pueblos, a leer representaciones del espacio, a preparar una presentación y a inferir relaciones entre paisaje y cultura. Decidir qué repasar también es aprender."],
  [("generalizar", "decir de todos lo que solo se sabe de algunos"), ("estereotipo", "imagen simplificada y falsa sobre un grupo"), ("corrección", "cambio para arreglar un error"), ("balance", "mirada a lo logrado y lo pendiente")],
  [("Detectar una generalización", "En el afiche de la ficha: «Todos los pueblos hacían lo mismo». ¿Qué criterio incumple?", ["Busco el criterio del lenguaje.", "Es el 3."], "El 3: usa «todos» en lugar de «probablemente»"),
   ("Corregir un título", "Corrige «Los indígenas del desierto vivían sin agua».", ["En el desierto había oasis y canales.", "Escribo un título que lo muestre."], "«Agua y cultura en el desierto»")],
  [("Corregir solo la ortografía.", "El problema de fondo es el contenido y el respeto.", "Revisa con las seis preguntas de la pauta."),
   ("Mantener la imagen disfrazada porque «se ve bonita».", "Es un estereotipo, aunque se vea llamativa.", "Reemplázala por una imagen basada en fuentes.")],
  [("abc", "{F} ¿Qué criterio incumple la imagen de personas con disfraz de plumas?", "el 4: respetar al pueblo", "el 1", "el 5", "El disfraz es un estereotipo que no respeta al pueblo."),
   ("abc", "{F} ¿Qué criterio incumple «sin fuentes»?", "el 5", "el 2", "el 6", "El criterio 5 pide citar fuentes confiables."),
   ("ab", "{F} ¿Qué criterio incumple «los indígenas del desierto vivían sin agua»?", "el 2: la inferencia debe apoyarse en una pista del paisaje", "el 5", "En el desierto había oasis y canales; el título contradice los datos."),
   ("abc", "{F} ¿Cuántas preguntas tiene la pauta?", "seis", "tres", "doce", "La ficha lista seis preguntas de revisión."),
   ("abc", "{F} ¿Qué criterio pide reconocer que los pueblos viven hoy?", "el 6", "el 3", "el 1", "El criterio 6 lo dice expresamente."),
   ("ab", "{F} Para corregir «todos los pueblos hacían lo mismo», es mejor", "probablemente cada pueblo aprovechaba los recursos de su paisaje", "todos hacían exactamente lo mismo", "Cambia la generalización por una inferencia matizada."),
   ("abc", "Un estereotipo es", "una imagen simplificada y falsa sobre un grupo", "un dato comprobado", "un color", "Los estereotipos reducen a las personas a una caricatura."),
   ("abc", "Una buena imagen para el afiche del desierto es", "un canal con parcelas verdes descrito en las fuentes", "un disfraz", "una caricatura", "Se basa en una fuente y respeta al pueblo."),
   ("ab", "Revisar con la pauta sirve para", "mejorar el afiche antes de mostrarlo", "no hacer nada", "Permite corregir los errores a tiempo."),
   ("abc", "Un cierre respetuoso para el afiche es", "los pueblos originarios viven hoy y mantienen su cultura", "ya desaparecieron", "no tienen cultura", "Reconoce su presencia actual y su cultura."),
   ("abc", "{F} ¿Qué criterio exige usar «probablemente» en lugar de «todos»?", "el 3", "el 1", "el 5", "El criterio 3 pide un lenguaje de inferencia, no de generalización."),
   ("ab", "Al hacer un balance de lo aprendido conviene", "decir qué ya sé hacer y qué quiero practicar", "ocultar lo que no entendí", "Un balance honesto orienta el aprendizaje."),
   ("abc", "Si un compañero presenta un afiche con errores, lo más respetuoso es", "señalarlos con amabilidad y mostrar cómo corregirlos", "burlarse", "ignorarlos", "Corregir con respeto ayuda a aprender sin humillar.")],
  ("abc", "En una jornada de la organización vecinal alguien trae un afiche similar al de la ficha. ¿Qué haces?", "compartes la pauta y propones corregirlo juntos", "lo criticas con ironía", "lo cuelgas sin mirar", "Revisar con una pauta y con respeto mejora el trabajo."),
  [("En un afiche sobre pueblos, ¿qué significa generalizar?", "Decir de todos lo que solo se sabe de algunos", "Los pueblos son distintos entre sí y no hacen todos lo mismo."),
   ("Antes de mostrar un afiche, ¿para qué sirve la pauta de revisión?", "Para detectar y corregir errores antes de mostrar un trabajo", "Cada criterio guía la revisión del trabajo."),
   ("¿Qué debe reconocer siempre el afiche?", "Que los pueblos originarios viven hoy", "Son pueblos vivos con cultura propia.")],
  ("Reescribe el afiche de la ficha 6: nuevo título, descripción de una imagen basada en fuentes, tres líneas de texto con «probablemente» y una línea de fuentes de ejemplo. Termina con una frase de balance: qué quieres repasar de toda la unidad.",
   "Título: «Agua y cultura en el desierto». Imagen: canal con parcelas verdes. Texto: «El agua es muy valiosa» / «Probablemente se cuida con canales» / «Los pueblos viven hoy». Fuentes: panel de museo (de ejemplo). Quiero repasar cómo citar fuentes.",
   ["corrige título, imagen y texto", "usa «probablemente»", "incluye fuentes y balance"],
   ["afiche reescrito y una frase de balance"],
   ["mantener la generalización", "olvidar las fuentes"],
   "Pregunta: «¿Qué criterio de la pauta cumple ahora cada parte?»."),
  "Escribe una pregunta de revisión para cada criterio de la pauta.",
  "Explica con tus palabras cómo se relacionan el paisaje, la cultura y la cosmovisión de un pueblo originario.")
