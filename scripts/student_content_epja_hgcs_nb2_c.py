"""Historia, Geografía y Ciencias Sociales EPJA Básica N2, módulo 3 (parte 1): OAD-09, caracterizar a los pueblos originarios de Chile (ubicación, rasgos culturales, cosmovisión y recursos) a partir de fuentes. Todos los textos son de ejemplo, escritos para este cuaderno; sin mapas ni audio reales."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz y goma. Todos los textos, cuadros y descripciones de mapas son de ejemplo y están escritos en la ficha de cada clase. No se necesita internet, audio ni calculadora. Lo que sabe cada comunidad sobre su propia cultura lo enseñan las personas de esa comunidad."
build = make_build(MATERIALS)

O = "EPJA-HGCS-NB2-OAD-09"
PRIOR = ["Sé que Chile es largo y angosto y que tiene paisajes distintos.", "He escuchado relatos de personas mayores sobre cómo se vivía antes.", "Leo textos breves y tablas con apoyo."]


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_, prior=None):
    build(O, n, F, use=use, prior=prior or PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ===================================================== clase 1: partir de lo que ya se sabe
F = ("Ficha 1 (texto de ejemplo). Relato anotado: «Una vecina mayor cuenta que su abuela hablaba mapuzugun, que en otoño la llevaba a recoger piñones "
     "y que en el campo no se cortaba un árbol sin antes agradecer a la tierra». Cuadro de fuentes posibles: A) una conversación con una persona mayor; "
     "B) un libro de historia; C) una fotografía de archivo; D) un letrero de museo.")
K(1, F,
  "Hoy parto de lo que ya sé y de lo que cuentan las personas mayores para entender qué es una fuente y qué es un pueblo originario.",
  ["Todas las personas guardamos historias: lo que nos contaron las abuelas, los abuelos y los vecinos. Esas historias son información sobre el pasado. En Historia, a todo lo que entrega información sobre el pasado o el presente se le llama fuente. Una conversación es una fuente oral; un libro o un documento es una fuente escrita; una fotografía o un mapa es una fuente visual.",
   "Los pueblos originarios son los pueblos cuyos antepasados ya vivían en el territorio que hoy es Chile antes de la llegada de los conquistadores españoles. No son solo parte del pasado: siguen viviendo hoy, en el campo y en las ciudades, y mantienen su lengua, sus costumbres y su forma de ver el mundo.",
   "Para caracterizar a un pueblo, es decir, describirlo con sus rasgos principales, buscamos tres cosas: dónde vive, qué rasgos culturales tiene (lengua, comida, oficios, fiestas) y cómo entiende el mundo (su cosmovisión). Hoy practicamos con un relato oral, tratándolo con respeto y sin sacar conclusiones apresuradas."],
  [("fuente", "todo lo que entrega información sobre el pasado o el presente"), ("fuente oral", "información que se transmite hablando, como un relato"), ("pueblo originario", "pueblo cuyos antepasados ya vivían aquí antes de la llegada de los españoles"), ("caracterizar", "describir algo con sus rasgos principales")],
  [("Reconocer el tipo de fuente", "Una persona lee una carta escrita a mano hace muchos años. ¿Qué tipo de fuente es?", ["La carta está escrita con letras.", "Las fuentes escritas son textos o documentos."], "Es una fuente escrita"),
   ("Sacar datos de un relato", "Relato de ejemplo: «Mi tío pescaba en el río con una red y vendía los peces en la feria». ¿Qué actividad se nombra?", ["Busco el verbo de la actividad: pescaba.", "Anoto también dónde: en el río."], "Pescar en el río")],
  [("Pensar que los pueblos originarios solo existieron en el pasado.", "Se confunde «antepasados que vivían aquí antes» con «ya no existen».", "Recuerda que mantienen su lengua y su cultura hoy, en distintos lugares."),
   ("Tomar un solo relato como verdad para todo un pueblo.", "Una persona cuenta su experiencia, no la de todos.", "Contrasta con otra fuente antes de generalizar.")],
  [("abc", "{F} ¿Cuál de las fuentes del cuadro es una fuente oral?", "A) la conversación con una persona mayor", "B) el libro de historia", "D) el letrero de museo", "Una conversación se transmite hablando, por eso es oral; las otras son textos escritos."),
   ("abc", "{F} ¿Cuál de las fuentes del cuadro es una fuente visual?", "C) la fotografía de archivo", "B) el libro de historia", "A) la conversación", "La fotografía entrega información mediante una imagen que se mira."),
   ("ab", "Una fuente es", "todo lo que entrega información sobre el pasado o el presente", "solo un libro muy antiguo", "Las fuentes pueden ser orales, escritas o visuales, no solo libros antiguos."),
   ("abc", "{F} Según el relato, ¿qué hacía la abuela con su nieta en otoño?", "recogía piñones", "sembraba trigo", "pescaba en el mar", "El relato menciona expresamente que la llevaba a recoger piñones."),
   ("ab", "{F} ¿Qué lengua hablaba la abuela según el relato?", "mapuzugun", "quechua", "El relato dice que la abuela hablaba mapuzugun, la lengua mapuche."),
   ("abc", "Un pueblo originario es un pueblo", "cuyos antepasados ya vivían en el territorio antes de la llegada de los españoles", "que llegó a Chile hace pocos años", "que dejó de existir hace siglos", "La definición habla de antepasados anteriores a los conquistadores y de una cultura que continúa."),
   ("abc", "Una persona quiere saber cómo se veía un barrio hace cincuenta años. ¿Qué fuente le muestra una imagen directa de esa época?", "una fotografía de aquel tiempo", "una receta de cocina", "una boleta de hoy", "Solo la fotografía de la época muestra cómo se veía el lugar entonces."),
   ("ab", "{F} La frase «no se cortaba un árbol sin antes agradecer a la tierra» muestra", "una forma de entender la naturaleza con respeto", "una norma de tránsito", "La frase expresa cómo se ve la relación con la naturaleza, que es parte de la cosmovisión."),
   ("abc", "Al anotar un relato, una vecina escribe el nombre de quien cuenta y la fecha. ¿Para qué sirve?", "para saber de quién viene la información y cuándo se obtuvo", "para que el relato sea más largo", "para que nadie más lo lea", "Registrar quién y cuándo permite revisar y citar la fuente después."),
   ("abc", "{F} Una compañera dice: «El relato prueba que todas las personas mapuche recogen piñones». ¿Qué respuesta es correcta?", "Es un solo relato y no permite afirmar eso de todas las personas", "Tiene razón porque el relato es oral", "Tiene razón porque la vecina es mayor", "Un relato cuenta un caso; para generalizar hacen falta más fuentes."),
   ("ab", "Para conversar con una persona mayor sobre el pasado, ¿qué pregunta invita a contar más?", "¿Qué recuerda de las fiestas que se hacían en su infancia?", "¿Había fiestas, sí o no?", "Una pregunta abierta invita a un relato; la de sí o no corta la conversación."),
   ("abc", "Alguien quiere ubicar dónde vivió un pueblo. ¿Qué fuente le sirve más directamente?", "un mapa que muestre el lugar", "una receta de cocina", "una boleta de pago", "Un mapa señala ubicaciones; las otras fuentes no informan sobre territorios."),
   ("ab", "Antes de anotar y usar el relato de una persona, lo correcto es", "pedirle permiso y explicarle para qué se usará", "grabar sin avisar para que no se ponga nerviosa", "El respeto exige consentimiento antes de registrar y usar lo que alguien cuenta.")],
  ("abc", "En una reunión de vecinos, alguien propone reunir historias del barrio contadas por personas mayores. ¿Qué tipo de fuente están reuniendo?", "fuentes orales", "fuentes escritas únicamente", "mapas", "Los relatos que cuentan las personas hablando son fuentes orales."),
  [("En Historia: ¿qué es una fuente?", "Todo lo que entrega información sobre el pasado o el presente", "Una fuente puede ser un relato, un texto, una imagen o un objeto."),
   ("Hoy, ¿siguen existiendo los pueblos originarios de Chile?", "Sí, mantienen su cultura y viven en distintos lugares", "Sus antepasados vivían aquí antes de los españoles y sus descendientes continúan hoy."),
   ("¿Qué hay que pedir antes de usar el relato de una persona?", "Su permiso", "Respetar a quien cuenta es parte de trabajar con fuentes orales.")],
  ("Con la ficha de esta clase: escribe en tres líneas (1) qué tipo de fuente es el relato de la vecina, (2) dos datos que entrega y (3) una pregunta nueva que le harías para saber más.",
   "1) Es una fuente oral. 2) La abuela hablaba mapuzugun y recogía piñones en otoño. 3) ¿Qué otras cosas se hacían en otoño en el campo?",
   ["nombra el tipo de fuente", "da dos datos que están en el relato", "formula una pregunta abierta"],
   ["tres líneas escritas con la respuesta"],
   ["agregar datos que el relato no dice", "afirmar que el relato vale para todo un pueblo"],
   "Pregunta: «¿Esto lo dice el relato o lo agregué yo?»."),
  "Piensa en una historia que te hayan contado sobre cómo se vivía antes y escribe de qué tipo de fuente se trata.",
  "Escribe dos preguntas abiertas para una persona mayor que quiera contarte cómo era su barrio antes.")

# ===================================================== clase 2: reconocer la idea y su vocabulario
F = ("Ficha 2 (cuadro de ejemplo; zonas generales). Aymara: norte del país, altiplano y precordillera. Atacameño o lickanantay: norte, oasis y salares del desierto. "
     "Diaguita: valles del norte chico. Mapuche: centro y sur del país. Rapa Nui: Isla de Pascua, en el océano Pacífico. Kawésqar: canales de la Patagonia occidental. "
     "Yagán: canales del extremo sur. Selk'nam: isla grande de Tierra del Fuego. Quechua y colla: norte del país, en zonas altas. Chango: costa del norte.")
K(2, F,
  "Hoy aprendo las palabras clave para caracterizar a un pueblo originario y ubico a algunos pueblos en el territorio.",
  ["Para describir a un pueblo usamos cuatro palabras. La ubicación geográfica es el lugar donde vive. Un rasgo cultural es algo propio de su forma de vivir: la lengua, la comida, la vestimenta, los oficios, las fiestas o la música. Un recurso natural es algo que da la naturaleza y las personas aprovechan, como el agua, la tierra fértil, las plantas, los animales o el mar.",
   "La cosmovisión es la manera en que un pueblo entiende el mundo: cómo se relacionan las personas, la naturaleza y lo sagrado. En muchos pueblos originarios la tierra y el agua no son solo «cosas para usar»: se cuidan y se respetan. Por ejemplo, para los aymara la Pachamama es la Madre Tierra, y para los mapuche la tierra, el mapu, es parte de la identidad.",
   "Una buena caracterización junta estas ideas: dónde viven, qué hacen y cómo ven el mundo. En Chile viven más pueblos originarios de los que se estudian en detalle en este cuaderno: por ejemplo, los pueblos quechua, colla y chango del norte. El cuadro de la ficha da ubicaciones generales, no límites exactos: los pueblos se movían, se relacionaban entre sí y hoy viven también en ciudades."],
  [("ubicación geográfica", "el lugar del territorio donde vive un pueblo"), ("rasgo cultural", "algo propio de la forma de vivir: lengua, comida, oficios, fiestas"), ("recurso natural", "lo que da la naturaleza y las personas aprovechan"), ("cosmovisión", "la manera de entender el mundo y la relación con la naturaleza")],
  [("Clasificar un dato", "Dato: «Tejen mantas con lana de camélidos». ¿Es ubicación, rasgo cultural o recurso natural?", ["Tejer es un oficio de la gente, no un lugar.", "La lana es el recurso, pero el dato dice qué hacen con ella."], "Es un rasgo cultural: un oficio"),
   ("Ubicar con el cuadro", "Según el cuadro de la ficha, ¿dónde se ubica el pueblo Diaguita?", ["Busco la palabra Diaguita en la ficha.", "Leo la zona que se le asigna."], "En los valles del norte chico")],
  [("Confundir cosmovisión con una creencia aislada.", "Una cosmovisión es toda la manera de entender el mundo, no un solo dato.", "Piensa: ¿cómo se relacionan personas, naturaleza y lo sagrado?"),
   ("Pensar que la ubicación del cuadro es un límite exacto.", "El cuadro da zonas generales; los pueblos se movían y hoy también viven en ciudades.", "Lee «zona general» y no «frontera».")],
  [("abc", "{F} ¿En qué zona general se ubica el pueblo Rapa Nui?", "en la Isla de Pascua, en el océano Pacífico", "en los valles del norte chico", "en el altiplano del norte", "El cuadro lo ubica en la Isla de Pascua, en el océano Pacífico."),
   ("abc", "{F} ¿Qué pueblo del cuadro se ubica en los canales de la Patagonia occidental?", "Kawésqar", "Aymara", "Diaguita", "El cuadro asigna los canales de la Patagonia occidental al pueblo Kawésqar."),
   ("ab", "Un rasgo cultural es", "algo propio de su forma de vivir, como la lengua o las fiestas", "un tipo de roca de la zona", "Los rasgos culturales son costumbres y expresiones de las personas, no elementos del paisaje."),
   ("abc", "{F} ¿Cuál pueblo del cuadro vive en el altiplano del norte?", "Aymara", "Mapuche", "Selk'nam", "El cuadro ubica a los aymara en el altiplano y la precordillera del norte."),
   ("abc", "¿Cuál de estos es un recurso natural?", "el agua de un río", "una canción", "un horario de buses", "Un recurso natural viene de la naturaleza; la canción y el horario son creaciones humanas."),
   ("ab", "La cosmovisión de un pueblo es", "su manera de entender el mundo y la relación con la naturaleza", "la lista de sus alimentos", "La cosmovisión no es una lista de alimentos, es la forma de ver el mundo."),
   ("abc", "{F} Una persona escribe que el pueblo Mapuche vive solo en Isla de Pascua. ¿Qué error cometió?", "Cambió la ubicación: según el cuadro viven en el centro y sur del país", "Ningún error", "Confundió el pueblo con el idioma", "El cuadro ubica a los mapuche en el centro y sur, y a los rapanui en Isla de Pascua."),
   ("abc", "Dato: «Celebran una fiesta en honor a la Madre Tierra». ¿Qué tipo de dato es?", "rasgo cultural ligado a la cosmovisión", "ubicación geográfica", "recurso natural", "Una fiesta es una costumbre y expresa cómo se entiende la relación con la tierra."),
   ("ab", "{F} Un estudiante dice que los selk'nam viven en la isla grande de Tierra del Fuego. Según el cuadro, es", "correcto", "incorrecto", "El cuadro ubica a los selk'nam en la isla grande de Tierra del Fuego."),
   ("abc", "{F} ¿Qué pueblo del cuadro se asocia a los oasis y salares del desierto?", "Atacameño o lickanantay", "Yagán", "Rapa Nui", "El cuadro dice que el pueblo atacameño habita oasis y salares del desierto del norte."),
   ("ab", "Dato: «Viven en oasis y cerca de salares del desierto». Es", "una ubicación geográfica", "una cosmovisión", "Dice dónde viven, por eso es una ubicación geográfica y no una manera de ver el mundo."),
   ("abc", "¿Por qué el cuadro dice «zonas generales»?", "porque los pueblos se movían y hoy también viven en ciudades", "porque nadie sabe dónde viven", "porque los mapas están prohibidos", "Las zonas son una guía; no marcan límites exactos."),
   ("abc", "{F} ¿Qué pueblo del cuadro se ubica en los canales del extremo sur?", "Yagán", "Diaguita", "Aymara", "El cuadro asigna los canales del extremo sur al pueblo Yagán.")],
  ("abc", "Una guía de museo dice: «Pueblo del norte, altiplano; cultivan papas en terrazas y cuidan a la Madre Tierra». ¿Qué parte es la cosmovisión?", "cuidar a la Madre Tierra", "cultivar papas", "estar en el altiplano", "Cuidar a la Madre Tierra expresa una manera de entender el mundo."),
  [("En Historia: ¿qué es la cosmovisión?", "La manera de entender el mundo", "Incluye cómo se relacionan las personas, la naturaleza y lo sagrado."),
   ("En Geografía: ¿qué es un recurso natural para un pueblo?", "Algo que da la naturaleza y se aprovecha", "El agua, la tierra y los animales son buenos ejemplos de recursos."),
   ("¿Qué indica una ubicación geográfica?", "El lugar donde vive un pueblo", "Responde la pregunta «¿dónde vive este pueblo?» en una caracterización.")],
  ("Usando el cuadro de la ficha, escribe tres frases: una sobre la ubicación de un pueblo a tu elección, una sobre un rasgo cultural general (por ejemplo, la lengua) y una sobre cosmovisión. Marca con subrayado la palabra clave de cada frase.",
   "Los aymara viven en el altiplano del norte. Hablan aymara. Para ellos la Pachamama es la Madre Tierra.",
   ["usa la ubicación del cuadro", "distingue rasgo cultural y cosmovisión", "tres frases completas"],
   ["tres frases escritas y subrayadas"],
   ["poner un dato de otro pueblo", "mezclar la ubicación con la cosmovisión"],
   "Pregunta: «¿Esta frase responde dónde, qué hacen o cómo ven el mundo?»."),
  "Escribe con tus palabras qué es una cosmovisión y un ejemplo del cuadro.",
  "Explica por qué una zona general no es lo mismo que un límite exacto.")

# ===================================================== clase 3: ver cómo se hace
F = ("Ficha 3 (texto de ejemplo, fuente A, un cuaderno de divulgación). «Los aymara viven en el norte, en el altiplano y la precordillera, a gran altura. "
     "Crían llamas y alpacas, cultivan papas y quinua en terrazas y honran a la Pachamama, la Madre Tierra». "
     "Plantilla de trabajo: 1) ¿Dónde? 2) ¿Qué rasgos culturales? 3) ¿Cómo ven el mundo? 4) ¿Qué recursos usan? 5) ¿De qué fuente salió?")
K(3, F,
  "Hoy sigo, paso a paso, un método para sacar de una fuente la ubicación, los rasgos, la cosmovisión y los recursos de un pueblo.",
  ["Caracterizar un pueblo a partir de una fuente tiene pasos que se repiten. Primero, lee el texto completo una vez, sin lápiz. Segundo, lee de nuevo y subraya con distintos colores o marcas la ubicación, los rasgos culturales, la cosmovisión y los recursos. Tercero, pasa lo subrayado a una plantilla con preguntas: ¿dónde?, ¿qué hacen?, ¿cómo ven el mundo?, ¿qué recursos usan? Cuarto, anota de qué fuente salió cada dato.",
   "Un recurso natural no siempre se usa de la misma manera. En el altiplano, por ejemplo, las terrazas son escalones construidos en una ladera que permiten cultivar donde el terreno es empinado, y los camélidos, como la llama y la alpaca, dan lana y transporte. Aprovechar un recurso con técnicas propias, y cuidarlo, es parte del dominio de los recursos naturales de un pueblo.",
   "Al terminar, revisa: ¿cada dato está en la fuente? Si algo lo sabías de antes pero el texto no lo dice, anótalo aparte como «dato mío» para comprobarlo en otra fuente. Así separamos lo que dice la fuente de lo que suponemos."],
  [("terraza de cultivo", "escalón construido en una ladera para sembrar"), ("camélido", "animal de la familia de la llama y la alpaca"), ("plantilla", "cuadro con preguntas para ordenar datos"), ("dominio de recursos", "saber aprovechar y cuidar lo que da el entorno")],
  [("Llenar la plantilla", "Con la fuente A de la ficha: ¿dónde viven los aymara según el texto?", ["Busco una palabra de lugar: norte, altiplano, precordillera.", "Anoto las tres."], "En el norte, en el altiplano y la precordillera"),
   ("Separar fuente y supuesto", "Una persona dice: «Los aymara también viven en el mar». ¿Está en la fuente A?", ["Reviso el texto: habla de altiplano y precordillera.", "El mar no aparece."], "No está: es un dato que habría que comprobar en otra fuente")],
  [("Copiar la fuente completa en la plantilla.", "Así no se distingue lo central de los detalles.", "Anota solo las palabras clave de cada pregunta."),
   ("Mezclar datos de dos pueblos en una misma plantilla.", "Se pierde qué rasgo corresponde a cuál pueblo.", "Haz una plantilla por pueblo y cita la fuente.")],
  [("abc", "{F} Según la fuente A, ¿qué animales crían los aymara?", "llamas y alpacas", "caballos y vacas", "lobos marinos y ballenas", "El texto nombra expresamente llamas y alpacas."),
   ("abc", "{F} ¿Qué cultivan según la fuente A?", "papas y quinua", "uvas y olivos", "arroz y caña", "La fuente A dice que cultivan papas y quinua en terrazas."),
   ("ab", "{F} ¿Cuál es la cosmovisión que se nombra?", "honrar a la Pachamama, la Madre Tierra", "viajar en bus", "La fuente muestra una relación de respeto con la Madre Tierra."),
   ("abc", "¿Cuál es el primer paso del método?", "leer el texto completo una vez", "copiar todo el texto", "inventar los datos que faltan", "Primero se lee para comprender el sentido general."),
   ("ab", "Una terraza de cultivo sirve para", "sembrar en una ladera empinada", "guardar agua del mar", "Las terrazas son escalones que permiten cultivar donde el terreno tiene pendiente."),
   ("abc", "{F} ¿En qué pregunta de la plantilla va «a gran altura»?", "1) ¿Dónde?", "3) ¿Cómo ven el mundo?", "5) ¿De qué fuente salió?", "Habla del lugar donde viven, por eso responde a dónde."),
   ("abc", "{F} ¿En qué pregunta de la plantilla va «crían llamas y alpacas»?", "2) rasgos culturales y 4) recursos", "1) ¿Dónde?", "5) ¿De qué fuente salió?", "Criar animales es un oficio y los animales son un recurso que se aprovecha."),
   ("ab", "Una persona anota «dato mío» junto a algo que no dice la fuente. Esto sirve para", "comprobarlo después en otra fuente", "esconderlo", "Marcar lo que sale de la memoria evita mezclarlo con lo que dice la fuente."),
   ("abc", "{F} Una estudiante escribe en la plantilla: «Los aymara viven en el sur y pescan ballenas». ¿Qué problema tiene?", "No coincide con la fuente A, que dice norte y altiplano", "Está perfecta", "Solo falta la fecha", "Los datos de la plantilla deben salir de la fuente, y este contradice el texto."),
   ("ab", "Las llamas y las alpacas dan lana y transporte. Eso las convierte en", "un recurso natural aprovechado", "una ubicación", "Un recurso es lo que da la naturaleza y se aprovecha."),
   ("abc", "Para mantener claro qué dato pertenece a cada pueblo conviene", "hacer una plantilla por pueblo", "mezclarlos en una sola lista", "borrar el nombre del pueblo", "Una plantilla por pueblo evita atribuir rasgos al pueblo equivocado."),
   ("ab", "{F} La cosmovisión del texto trata de la relación con la", "tierra", "ciudad", "La Pachamama es la Madre Tierra, según la fuente."),
   ("abc", "{F} ¿Cuál es el último paso de la plantilla de trabajo?", "anotar de qué fuente salió cada dato", "borrar el texto original", "cambiar el pueblo estudiado", "La pregunta 5 de la plantilla pide registrar la fuente de cada dato.")],
  ("abc", "En una biblioteca municipal, una persona encuentra un cuaderno de divulgación como el de la ficha y quiere usarlo para un trabajo. ¿Qué debe anotar además de los datos?", "el nombre del cuaderno, quién lo escribió y cuándo", "solo su propia opinión", "nada, porque ya está en el cuaderno", "Citar la fuente permite que otros comprueben lo que escribió."),
  [("¿Qué se hace con un texto después de leerlo una vez?", "Se vuelve a leer y se subrayan los datos", "El subrayado ordena ubicación, rasgos, cosmovisión y recursos.", ),
   ("En Historia: ¿qué es una terraza de cultivo?", "Un escalón construido en una ladera para sembrar", "Permite cultivar en terreno empinado, como en las laderas."),
   ("¿Qué se anota aparte si un dato no está en la fuente?", "Que es un dato mío para comprobar", "Separa lo que dice la fuente de lo que suponemos.")],
  ("Lee esta fuente B de ejemplo: «Los atacameños o lickanantay viven en el norte, en oasis y cerca de salares del desierto. Cuidan el agua con canales y cultivan maíz en pequeñas parcelas. Valoran la cercanía con el paisaje». Llena la plantilla de la ficha con las cinco preguntas.",
   "1) Norte, oasis y cerca de salares. 2) Cultivan maíz y cuidan el agua con canales. 3) Valoran la cercanía con el paisaje. 4) Agua y parcelas para maíz. 5) Fuente B, de ejemplo.",
   ["cada respuesta sale de la fuente B", "responde las cinco preguntas", "separa rasgos, cosmovisión y recursos"],
   ["la plantilla completa con cinco respuestas"],
   ["agregar datos que la fuente no dice", "dejar sin citar la fuente"],
   "Pregunta: «¿En qué línea de la fuente lo leíste?»."),
  "Vuelve a leer la fuente A y subraya con tres marcas distintas la ubicación, un recurso y la cosmovisión.",
  "Escribe una pregunta que la fuente B no responde y que tendrías que buscar en otra fuente.")

# ===================================================== clase 4: practicar juntos con apoyo
F = ("Ficha 4 (dos textos de ejemplo). Texto M: «Mapuche significa gente (che) de la tierra (mapu). Viven en el centro y el sur del país, en el campo y en las ciudades. "
     "Cultivan papa y maíz, y parte de la población pehuenche recolecta los piñones del pehuén, la araucaria. La tierra es parte de su identidad». "
     "Texto K: «Los kawésqar recorrían en canoa los canales de la Patagonia occidental, un territorio de agua, islas y viento. Se alimentaban de mariscos y de la caza de lobos marinos».")
K(4, F,
  "Hoy practico con apoyo cómo caracterizar a dos pueblos a partir de dos textos y cómo compararlos sin mezclar sus datos.",
  ["Caracterizar a un pueblo no es solo copiar datos: es ordenarlos y compararlos. Dos pueblos pueden vivir en lugares muy distintos y por eso usar recursos distintos. Los mapuche viven en el centro y sur, donde hay tierra para cultivar y bosques; los kawésqar recorrían canales, donde el recurso principal era el mar. El paisaje explica en parte qué recursos se aprovechan.",
   "Los textos de la ficha entregan palabras en lenguas originarias. «Mapu» quiere decir tierra y «che», gente. «Pehuén» es el nombre de la araucaria, árbol cuyas semillas, los piñones, se recolectan. Si necesitas la forma tradicional de una palabra o de una costumbre, la enseñan las personas de la comunidad; este cuaderno solo usa lo que dicen los textos.",
   "Al comparar, usa una tabla con una columna por pueblo y una fila por pregunta. Así ves en qué se parecen y en qué se diferencian. Cuando algo no está en los textos, la casilla se deja vacía y se anota que falta información."],
  [("comparar", "ver en qué se parecen y en qué se diferencian dos cosas"), ("pehuén", "nombre mapuche de la araucaria"), ("piñón", "semilla comestible de la araucaria"), ("canoa", "embarcación angosta que se mueve con remos")],
  [("Comparar con una tabla", "Texto M y texto K: ¿qué recurso principal aprovechan los kawésqar?", ["Busco la columna del texto K.", "Leo qué comían: mariscos y lobos marinos."], "El mar: mariscos y lobos marinos"),
   ("Casilla sin información", "El texto K, ¿dice qué cultivan los kawésqar?", ["Reviso el texto K completo.", "No menciona cultivos."], "No: la casilla queda vacía; falta información")],
  [("Llenar una casilla con un dato del otro pueblo.", "Se cruzan las columnas de la tabla.", "Revisa que el dato esté en el texto del pueblo de esa columna."),
   ("Suponer que si un texto no menciona algo, no existía.", "La ausencia en un texto breve no prueba nada.", "Anota «falta información» y busca otra fuente.")],
  [("abc", "{F} Según el texto M, ¿qué significa «mapu»?", "tierra", "agua", "montaña", "El texto M explica que mapu es la tierra y che es la gente."),
   ("abc", "{F} ¿Dónde viven los mapuche según el texto M?", "en el centro y el sur del país", "en el altiplano del norte", "en los canales del extremo sur", "El texto M los ubica en el centro y el sur."),
   ("ab", "{F} Los kawésqar se movían principalmente", "en canoa por los canales", "a caballo por las pampas", "El texto K dice que recorrían los canales en canoa."),
   ("abc", "{F} ¿Qué es el pehuén según el texto M?", "la araucaria", "un tipo de pescado", "una canoa", "El texto M lo nombra como la araucaria, cuyas semillas son los piñones."),
   ("abc", "{F} ¿Qué tres elementos describe el texto K en el territorio de los kawésqar?", "agua, islas y viento", "cerros, desierto y sol", "bosques, lagos y volcanes", "El texto K habla de un territorio de agua, islas y viento."),
   ("ab", "{F} Al comparar los dos textos, ¿qué recurso es propio del texto M y no del K?", "los cultivos de papa y maíz", "los lobos marinos", "Los cultivos aparecen solo en el texto M; los lobos marinos, solo en el K."),
   ("abc", "{F} Una estudiante pone en la columna «kawésqar»: «recolectan piñones». ¿Qué error hay?", "Es un dato del texto M, de los pehuenche", "Está bien", "Falta la fecha", "Los piñones del pehuén aparecen en el texto M, no en el K."),
   ("abc", "{F} ¿Qué paisaje explica que el mar fuera el recurso principal de los kawésqar?", "un territorio de canales, islas y mar", "un desierto sin agua", "un altiplano frío", "El texto K describe un territorio de agua e islas."),
   ("ab", "{F} Una persona dice: «Como el texto K no habla de cultivos, los kawésqar no cultivaban». Su conclusión es", "apresurada: falta información", "segura", "Un texto breve no prueba que algo no existiera; solo no lo menciona."),
   ("abc", "{F} En una tabla de comparación, ¿qué va en las columnas?", "un pueblo en cada columna", "las fechas de los textos", "los nombres de los autores", "Cada columna agrupa los datos de un pueblo para compararlos."),
   ("ab", "Quien necesita la forma tradicional de una costumbre debe consultar a", "las personas de la comunidad", "cualquier persona que la invente", "Quienes la viven y enseñan son quienes conocen la forma tradicional."),
   ("abc", "{F} ¿Qué tienen en común los dos textos?", "ambos describen un pueblo, su lugar y cómo aprovecha su entorno", "ambos hablan del desierto", "ambos hablan de ciudades", "Los dos relacionan el pueblo con un territorio y sus recursos."),
   ("abc", "{F} ¿En cuál texto aparece una construcción de la lengua, «mapu» y «che»?", "en el texto M", "en el texto K", "en ninguno", "El texto M explica el significado de mapuche.")],
  ("abc", "Un cartel de un centro cultural presenta dos pueblos: uno que recolecta piñones en el sur y otro que navega canales. Para un visitante, ¿qué tabla ayuda a comparar?", "una con una columna por pueblo y filas con ubicación, recursos y rasgos", "una lista mezclada de datos", "un dibujo sin texto", "La tabla ordenada permite ver parecidos y diferencias."),
  [("¿Cómo se ordena una comparación?", "Una columna por pueblo y una fila por pregunta", "Así cada dato queda en su lugar y se compara fácil."),
   ("Si un texto no menciona algo, ¿qué escribo?", "Falta información", "No se puede afirmar que no existía."),
   ("En Historia: ¿qué es el pehuén?", "La araucaria", "Es la araucaria, y sus semillas son los piñones.")],
  ("Completa una tabla de dos columnas, «mapuche» y «kawésqar», con tres filas: ubicación, recurso principal y rasgo del territorio. Usa solo los textos M y K. Si falta información, escribe «falta información».",
   "Ubicación: centro y sur / canales de la Patagonia occidental. Recurso: tierra para cultivar y piñones / mariscos y lobos marinos. Territorio: campo y ciudades / agua, islas y viento.",
   ["usa solo datos de los textos", "una columna por pueblo", "marca lo que falta"],
   ["la tabla de 2 columnas y 3 filas"],
   ["cruzar datos entre columnas", "agregar datos que los textos no dicen"],
   "Pregunta: «¿En qué texto está este dato?»."),
  "Escribe una diferencia y una semejanza entre los dos pueblos de la ficha.",
  "Anota una pregunta que te gustaría responder sobre el pueblo kawésqar y dónde podrías buscar la respuesta.")

# ===================================================== clase 5: aplicar a la comunidad
F = ("Ficha 5 (panel de ejemplo de un centro cultural). «Palabras en mapuzugun que se ven en el territorio: mapu, tierra; ko, agua; lafken, mar o lago; ruka, casa. "
     "Muchos nombres de lugares vienen de lenguas originarias. Un panel debe nombrar siempre sus fuentes y recordar que los pueblos originarios viven hoy». "
     "Lista de lugares inventados para el ejercicio: «Lafken Alto», «Ko Chico», «Mapu Verde».")
K(5, F,
  "Hoy aplico lo aprendido a una situación de la comunidad: leer nombres de lugares y un panel informativo con espíritu crítico.",
  ["Los pueblos originarios no están solo en los libros: están en los nombres de calles, ríos, ciudades y volcanes. Muchos nombres de lugares, llamados topónimos, vienen de las lenguas originarias. Entender una palabra como «ko», agua, o «lafken», mar o lago, nos da una pista sobre cómo se veía y se usaba ese lugar.",
   "Cuando leemos un panel de museo o un letrero informativo, conviene hacer cuatro preguntas: ¿quién lo hizo?, ¿qué pueblo describe?, ¿qué datos entrega sobre ubicación y recursos?, ¿habla de los pueblos como parte del presente? Un buen panel nombra sus fuentes y no presenta a los pueblos como si ya no existieran.",
   "En la vida diaria, esto sirve para leer con más atención un cartel en una plaza, un folleto turístico o un trabajo de otra persona. Respetar a los pueblos originarios también significa escribir bien sus nombres y no usar sus palabras como adorno sin saber qué significan."],
  [("topónimo", "nombre propio de un lugar"), ("mapuzugun", "lengua del pueblo mapuche"), ("panel", "cartel informativo de un museo o espacio público"), ("espíritu crítico", "revisar con cuidado lo que dice una fuente")],
  [("Interpretar un topónimo", "Un lugar se llama «Ko Chico». Según la ficha, ¿qué parte del nombre alude al agua?", ["Busco ko en la lista de palabras.", "Ko significa agua."], "«Ko» alude al agua"),
   ("Evaluar un panel", "Un panel dice «Los mapuche vivieron en el sur hace siglos y ya no existen». ¿Qué falla tiene?", ["Compara con la ficha: los pueblos viven hoy.", "El panel habla solo en pasado."], "Presenta al pueblo como si ya no existiera")],
  [("Inventar el significado de una palabra por cómo suena.", "Una palabra puede significar algo muy distinto de lo que parece.", "Consulta una fuente confiable o a la comunidad."),
   ("Creer que un panel dice siempre la verdad completa.", "Los paneles resumen y pueden dejar fuera partes.", "Revisa quién lo hizo, qué fuentes cita y si habla del presente.")],
  [("abc", "{F} ¿Qué significa «lafken» según el panel?", "mar o lago", "casa", "tierra", "La ficha lista lafken como mar o lago."),
   ("abc", "{F} ¿Qué significa «ruka»?", "casa", "agua", "mar", "El panel indica que ruka es casa."),
   ("ab", "{F} Un topónimo es", "el nombre propio de un lugar", "una receta de cocina", "Los topónimos son los nombres de lugares, como ríos y ciudades."),
   ("abc", "{F} El nombre inventado «Mapu Verde» contiene la palabra mapu. ¿Qué parte alude a la tierra?", "Mapu", "Verde", "El nombre completo", "Mapu significa tierra según el panel."),
   ("ab", "{F} Según el panel, un buen cartel debe", "nombrar sus fuentes", "evitar decir de dónde saca los datos", "Citar fuentes permite comprobar que la información es confiable."),
   ("abc", "{F} ¿Qué lugar inventado de la lista alude al mar o a un lago?", "Lafken Alto", "Ko Chico", "Mapu Verde", "Lafken significa mar o lago, según la lista del panel."),
   ("abc", "Un folleto turístico dice: «Los antiguos habitantes desaparecieron». ¿Qué conviene preguntar?", "si el folleto reconoce que los pueblos originarios viven hoy", "cuánto cuesta el folleto", "qué color tiene la portada", "La pregunta clave es si el texto presenta el pasado y el presente."),
   ("ab", "Escribir correctamente el nombre de un pueblo originario es", "una forma de respeto", "una pérdida de tiempo", "Los nombres bien escritos reconocen la identidad del pueblo."),
   ("abc", "{F} ¿Qué pregunta ayuda a evaluar un panel?", "¿Quién lo hizo y qué fuentes cita?", "¿Cuántas letras tiene?", "¿Cuál es su precio?", "Quién escribe y con qué fuentes define la confiabilidad."),
   ("ab", "Si no estás seguro de lo que significa una palabra en una lengua originaria, lo mejor es", "consultar una fuente confiable o a la comunidad", "adivinar por el sonido", "Adivinar puede dar un significado falso."),
   ("abc", "{F} Un panel dice «ko» y otro dice «mapu». ¿Qué pareja de significados es correcta?", "ko es agua y mapu es tierra", "ko es tierra y mapu es agua", "ko es casa y mapu es mar", "La ficha define ko como agua y mapu como tierra."),
   ("abc", "Un cartel en una plaza dice: «Pueblo de pescadores, fuente: investigación sin citar». ¿Qué falta?", "que cite sus fuentes", "que sea más largo", "que tenga fotos", "Sin fuentes citadas no se puede comprobar lo que afirma."),
   ("ab", "El texto de un panel explica solo el pasado de un pueblo. Un lector atento debería", "preguntarse cómo viven hoy esas comunidades", "creer que ya no existen", "Los pueblos originarios continúan viviendo, y el panel debería mencionarlo.")],
  ("abc", "Una organización vecinal quiere poner un cartel con el origen del nombre de su calle, que lleva una palabra de una lengua originaria. ¿Qué paso es el más prudente?", "consultar fuentes confiables y a personas de la comunidad", "adivinar el significado más bonito", "copiar un cartel de otra ciudad", "Comprobar con fuentes evita transmitir un significado falso."),
  [("¿Qué es un topónimo?", "El nombre propio de un lugar", "Muchos topónimos de Chile vienen de lenguas originarias."),
   ("¿Qué debe nombrar siempre un panel?", "Sus fuentes", "Así otras personas pueden comprobar la información."),
   ("¿Cómo debe presentar un panel a los pueblos originarios?", "Como parte del presente, no solo del pasado", "Los pueblos originarios viven hoy y mantienen su cultura.")],
  ("Revisa este panel de ejemplo: «El pueblo kawésqar fue un pueblo de canoas. Hoy no queda nada de él». Escribe (1) un dato que sí está en los textos de la clase 4, (2) qué falla tiene la segunda frase y (3) cómo la corregirías.",
   "1) Recorrían los canales en canoa. 2) Dice que hoy no queda nada, y hay personas que mantienen su cultura. 3) «El pueblo kawésqar navegaba en canoa; hoy sus descendientes mantienen su cultura».",
   ["distingue un dato de la fuente", "detecta la falla del panel", "propone una corrección respetuosa"],
   ["tres respuestas escritas"],
   ["no reconocer que los pueblos viven hoy", "agregar datos sin fuente"],
   "Pregunta: «¿Este panel habla de gente viva o solo de gente del pasado?»."),
  "Anota un nombre de lugar de tu zona que venga de una lengua originaria y qué fuente consultarías para saber qué significa.",
  "Escribe dos preguntas que harías al leer un letrero sobre un pueblo originario.")

# ===================================================== clase 6: revisar lo logrado
F = ("Ficha 6 (resumen de ejemplo con errores). «Todos los pueblos originarios vivían en el norte, comían lo mismo y hablaban la misma lengua. "
     "Ya no existen, así que solo hay que mirarlos en los museos». Cuadro de repaso de la ficha 2: Aymara, norte y altiplano; Mapuche, centro y sur; "
     "Rapa Nui, Isla de Pascua; Kawésqar, canales de la Patagonia occidental.")
K(6, F,
  "Hoy reviso lo que logré caracterizando pueblos originarios, corrijo un resumen con errores y decido qué quiero repasar.",
  ["Revisar es parte de aprender. Un buen resumen sobre un pueblo originario responde tres preguntas: dónde vive, qué rasgos culturales y recursos tiene y cómo entiende el mundo. Además, usa fuentes que se pueden nombrar y habla de los pueblos como parte del presente. Con esa lista puedes revisar tu trabajo o el de otra persona.",
   "Hay errores comunes que conviene reconocer. Generalizar: decir «todos los pueblos» como si fueran iguales, cuando viven en paisajes distintos, hablan lenguas distintas y aprovechan recursos distintos. Hablar solo en pasado: olvidar que hoy existen comunidades vivas. Mezclar datos: atribuir a un pueblo lo que es de otro. Y afirmar sin fuente: decir algo sin poder decir de dónde viene.",
   "Cuando encuentras un error en un resumen, lo corriges con la fuente en la mano, no con una impresión. Y cuando una pregunta no tiene respuesta en tus fuentes, la anotas como pendiente: reconocer lo que falta también es trabajo bien hecho."],
  [("generalizar", "decir de todos lo que solo se sabe de algunos"), ("atribuir", "decir que algo pertenece a alguien"), ("pendiente", "lo que aún falta por hacer o averiguar"), ("revisar", "mirar de nuevo para comprobar y mejorar")],
  [("Detectar una generalización", "Frase: «Todos los pueblos originarios comían lo mismo». ¿Qué error tiene?", ["La palabra «todos» agrupa pueblos distintos.", "Viven en paisajes distintos y usan recursos distintos."], "Generaliza: cada pueblo aprovecha los recursos de su zona"),
   ("Corregir con el cuadro", "Frase: «Los kawésqar viven en el altiplano». ¿Cómo se corrige con el cuadro de repaso?", ["El cuadro ubica a los kawésqar en los canales de la Patagonia occidental.", "Cambio la ubicación."], "Los kawésqar se ubican en los canales de la Patagonia occidental")],
  [("Corregir un error con otro error.", "Se corrige sin volver a la fuente.", "Comprueba cada cambio en el cuadro o en el texto."),
   ("Pensar que revisar es solo buscar faltas de ortografía.", "Revisar incluye datos, fuentes y respeto.", "Usa la lista: dónde, qué, cómo ven el mundo y de qué fuente.")],
  [("abc", "{F} ¿Qué error tiene la frase «todos los pueblos vivían en el norte»?", "no es cierto: viven en distintas zonas del país", "es correcto", "falta un adjetivo", "Según el cuadro de repaso, los pueblos viven en el norte, el centro, el sur y las islas."),
   ("abc", "{F} ¿Qué error tiene la frase «ya no existen»?", "los pueblos originarios viven hoy", "está bien escrita", "es demasiado larga", "Los pueblos originarios continúan existiendo y manteniendo su cultura."),
   ("ab", "{F} El resumen dice que todos hablaban la misma lengua. Eso es", "una generalización", "un dato comprobado", "Cada pueblo tiene su propia lengua; decir «la misma» generaliza."),
   ("abc", "{F} Según el cuadro de repaso, ¿dónde viven los rapanui?", "en la Isla de Pascua", "en el altiplano", "en los canales", "El cuadro ubica a Rapa Nui en la Isla de Pascua."),
   ("ab", "{F} Según el cuadro, los mapuche se ubican en", "el centro y el sur", "el norte y el altiplano", "El cuadro dice centro y sur para los mapuche."),
   ("abc", "Un resumen escribe que los aymara navegan los canales de la Patagonia. ¿Qué tipo de error es?", "mezcla datos entre pueblos", "falta de fuentes en el título", "un error de ortografía", "La navegación por canales corresponde al pueblo kawésqar, no al aymara."),
   ("abc", "Una persona afirma algo sobre un pueblo y no puede decir de dónde sacó el dato. ¿Qué conviene hacer?", "buscar una fuente que lo confirme o no usarlo", "repetirlo con más fuerza", "cambiar el nombre del pueblo", "Un dato sin fuente debe comprobarse antes de usarlo."),
   ("ab", "Si una pregunta no tiene respuesta en tus fuentes, lo mejor es", "anotarla como pendiente", "inventar una respuesta", "Reconocer lo que falta es honesto y permite seguir investigando."),
   ("abc", "{F} Para corregir «ya no existen, solo hay que mirarlos en los museos», ¿qué frase es mejor?", "los pueblos originarios viven hoy y mantienen su cultura", "los pueblos originarios solo viven en museos", "los pueblos originarios no tienen cultura", "La frase corregida reconoce que están vivos y siguen creando cultura."),
   ("ab", "Revisar un resumen sirve para", "comprobar datos, fuentes y respeto", "alargar el texto", "Revisar es mejorar la calidad y la exactitud."),
   ("abc", "{F} ¿Cuál es un dato correcto según el cuadro de repaso?", "los kawésqar se ubican en los canales de la Patagonia occidental", "los aymara viven en Isla de Pascua", "los rapanui viven en el altiplano", "Solo la primera opción coincide con el cuadro."),
   ("abc", "Un compañero dice «todos los pueblos aprovechaban el mar». ¿Qué respuesta es más adecuada?", "los pueblos del altiplano o del valle no vivían junto al mar, así que depende de cada pueblo", "tiene razón", "no importa", "Cada pueblo aprovecha los recursos de su territorio."),
   ("ab", "Antes de entregar un trabajo, conviene revisar que", "cada dato tenga su fuente", "el texto sea lo más largo posible", "Las fuentes permiten comprobar lo escrito.")],
  ("abc", "En un taller de la biblioteca, una persona comparte un resumen sobre pueblos originarios con una frase como la de la ficha. ¿Qué es lo más respetuoso y útil?", "señalar el error con amabilidad y mostrar la fuente que lo corrige", "reírse del error", "corregirlo sin explicar", "Corregir con fuente y amabilidad ayuda a aprender sin humillar."),
  [("En Historia: ¿qué es generalizar?", "Decir de todos lo que solo se sabe de algunos", "Cada pueblo es distinto y tiene su propia historia."),
   ("¿Qué se hace si una pregunta no tiene respuesta en las fuentes?", "Se anota como pendiente", "Así se sabe qué hay que buscar después."),
   ("¿Qué tres cosas debe tener un buen resumen sobre un pueblo?", "Ubicación, rasgos y recursos, y cosmovisión", "Responde dónde, qué hacen y cómo ven el mundo.")],
  ("Reescribe el resumen de la ficha 6 en tres frases correctas usando el cuadro de repaso: una sobre la diversidad de ubicaciones, una sobre la presencia de los pueblos hoy y una sobre la importancia de citar fuentes. Al final escribe qué parte de la unidad quieres repasar.",
   "Los pueblos originarios viven en distintas zonas: norte, centro, sur e islas. Hoy mantienen su cultura y viven en el campo y en las ciudades. Es importante citar la fuente de cada dato. Quiero repasar la cosmovisión.",
   ["corrige las tres ideas", "usa datos del cuadro", "dice qué quiere repasar"],
   ["tres frases y una línea de balance"],
   ["decir «todos» sin matices", "no reconocer la presencia actual"],
   "Pregunta: «¿Esta frase vale para todos los pueblos o solo para uno?»."),
  "Escribe una pregunta sobre un pueblo originario y dos fuentes distintas donde podrías buscar la respuesta.",
  "Explica con tus palabras por qué decir «todos los pueblos originarios» puede ser un error.")
