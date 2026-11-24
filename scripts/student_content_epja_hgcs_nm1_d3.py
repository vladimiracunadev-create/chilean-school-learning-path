"""Historia, Geografía y Ciencias Sociales EPJA Media N1, módulo 4 (parte 3): OAD-15, elaborar y comunicar explicaciones multicausales y multidimensionales sobre multiculturalismo, identidades y patrimonio material e inmaterial en Chile. Casos y datos de comunidades inventados («de ejemplo»)."""
from __future__ import annotations

from epja_hgcs_nm1_d_common import K

O = "EPJA-HGCS-NM1-OAD-15"

# ======================================================= clase 1
F1 = ("Ficha 1 (comuna ficticia «Villa Alta»; un taller comunitario anota lo que la gente siente como propio). "
      "A) El mercado antiguo de la plaza, levantado en 1930. "
      "B) La fiesta de la cosecha, con música y comidas que preparan las familias. "
      "C) El oficio de tejer en lana, que enseñan las mujeres mayores del barrio. "
      "D) La receta de pan amasado que traen muchas familias y la receta de arepas que trajo una familia migrante; hoy ambas se venden en la feria.")
K(O, 1, F1,
  "Hoy parto de lo que ya conozco: reconozco lo que en mi barrio se siente propio y lo relaciono con las ideas de identidad, cultura y patrimonio.",
  ["Tu identidad es el conjunto de rasgos con los que te reconoces y con los que otras personas te reconocen: tu lugar, tu oficio, tus costumbres, tu lengua. También existen identidades colectivas, como la de un barrio, un pueblo o un país. Cambian en el tiempo y se construyen con aportes de muchas personas.",
   "Chile es un país multicultural: en un mismo territorio conviven distintos pueblos y comunidades, como los pueblos originarios, las personas de origen europeo, las afrodescendientes y las migrantes de otros países. Cada una aporta lenguas, comidas, fiestas y saberes. Convivir con respeto es parte de vivir en comunidad.",
   "El patrimonio es la herencia que una comunidad valora y quiere cuidar y transmitir. Puede ser material, como un edificio o un objeto, o inmaterial, como una fiesta, una receta, un oficio o una lengua. En la ficha hay ejemplos de las dos clases. Hoy los reconocerás con la experiencia que ya traes."],
  [("identidad", "rasgos con los que una persona o un grupo se reconoce"), ("multicultural", "que reúne varias culturas en un mismo lugar"), ("patrimonio", "herencia que una comunidad valora, cuida y transmite"), ("migrante", "persona que se traslada a vivir a otro lugar o país"), ("tradición", "costumbre que se transmite de generación en generación")],
  [("Reconocer lo propio", "Ficha de ejemplo: «El oficio de tejer en lana, que enseñan las mujeres mayores del barrio». ¿Es patrimonio material o inmaterial?", ["Se trata de un saber que se transmite.", "No es un objeto sino una práctica."], "Patrimonio inmaterial"),
   ("Una identidad con aportes", "La ficha dice que se venden pan amasado y arepas en la feria. ¿Qué muestra sobre la identidad del barrio?", ["Hay comidas de familias de distintos orígenes.", "La identidad se construye con varios aportes."], "Que la identidad del barrio se enriquece con aportes distintos")],
  [("Pensar que la identidad es algo fijo que nunca cambia.", "Las identidades se transforman con el tiempo y los aportes.", "Pregunta qué aportes nuevos se sumaron."),
   ("Creer que el patrimonio solo son edificios antiguos.", "También son patrimonio las fiestas, los saberes, las lenguas y las recetas.", "Recuerda que existen el patrimonio material y el inmaterial.")],
  [("abc", "{F} ¿Cuál es un ejemplo de patrimonio material?", "El mercado antiguo de la plaza", "La fiesta de la cosecha", "El oficio de tejer en lana", "Un edificio es un objeto que se puede tocar; las otras son prácticas."),
   ("ab", "En Historia: ¿qué es el patrimonio?", "Una herencia que la comunidad valora y quiere transmitir", "Un ahorro en el banco", "El patrimonio reúne lo que una comunidad cuida y transmite."),
   ("{F} ¿En qué año se levantó el mercado antiguo?", "1930", "La ficha lo fecha en 1930."),
   ("abc", "{F} ¿Qué receta trajo una familia migrante?", "La de arepas", "La de pan amasado", "La de empanadas", "La ficha dice que las arepas las trajo una familia migrante."),
   ("ab", "En Historia: ¿qué significa que Chile es multicultural?", "Que en el país conviven distintos pueblos y comunidades", "Que todas las personas piensan igual", "Multicultural quiere decir que hay varias culturas conviviendo."),
   ("=", "{F} Si el mercado se levantó en 1930, ¿cuántos años tenía en 2020?", "2020-1930", "Se restan los años para calcular la antigüedad del mercado.", " años"),
   ("abc", "{F} ¿Qué práctica es patrimonio inmaterial según la ficha?", "La fiesta de la cosecha", "El mercado antiguo", "Un edificio nuevo", "Una fiesta es una práctica cultural que se transmite."),
   ("abc", "{F} Alguien dice: «Las arepas no pueden ser parte de la identidad del barrio porque son de otro país». ¿Qué falla?", "La identidad se construye con aportes de distintas personas y comunidades", "Nada falla", "Las arepas no existen", "La ficha muestra que ambas recetas se venden en la feria."),
   ("ab", "{F} ¿Quiénes enseñan el oficio de tejer en lana?", "Las mujeres mayores del barrio", "Una empresa", "La ficha indica que lo enseñan las mujeres mayores."),
   ("abc", "{F} Si el taller quiere cuidar la fiesta de la cosecha, ¿qué debería hacer primero?", "Conversar con las familias que la organizan", "Cambiarla sin preguntar", "Cobrar por ella", "Lo primero es incluir a quienes sostienen esa tradición."),
   ("abc", "{F} De los cuatro elementos de la ficha (A a D), ¿cuántos son prácticas o saberes y no objetos?", "Tres", "Uno", "Cuatro", "La fiesta, el oficio de tejer y las recetas son prácticas o saberes; solo el mercado es un edificio."),
   ("abc", "{F} Una persona pregunta qué cambió en el barrio con las arepas. ¿Qué explicación es mejor?", "Se sumó una comida nueva a la feria por la llegada de una familia migrante", "Se perdió el pan amasado", "Se cerró la feria", "La ficha muestra que ambas se venden hoy."),
   ("abc", "{F} Para decir qué es más importante, el mercado o la fiesta, ¿qué es lo más honesto?", "Reconocer que ambos son valiosos para distintas personas y preguntar por qué", "Elegir uno sin preguntar", "Decir que no hay patrimonio", "El valor del patrimonio lo reconoce cada comunidad.")],
  ("abc", "En una junta de vecinos de ejemplo se propone hacer una lista de lo que el barrio quiere cuidar. Una vecina sugiere incluir las recetas de las abuelas. ¿Qué tipo de patrimonio son?", "Inmaterial", "Material", "Geográfico", "Una receta es un saber que se transmite."),
  [("En Historia: ¿qué es la identidad colectiva?", "Los rasgos con los que se reconoce un grupo", "Un barrio o un país también tienen identidad."),
   ("En Historia: ¿qué es patrimonio inmaterial?", "Saberes, fiestas, lenguas y costumbres que se transmiten", "No son objetos, sino prácticas y saberes que se transmiten."),
   ("En Historia: ¿qué es un migrante?", "Una persona que se traslada a vivir a otro lugar o país", "Puede ser de otra región o de otro país.")],
  ("Con la ficha 1, haz una lista de cuatro elementos y clasifícalos como patrimonio material o inmaterial. Después escribe una frase que explique por qué la identidad del barrio incluye aportes distintos.",
   "Mercado antiguo: material. Fiesta de la cosecha: inmaterial. Tejido en lana: inmaterial. Pan y arepas: inmaterial. La identidad del barrio incluye aportes distintos porque conviven recetas de familias de distintos orígenes.",
   ["clasifica correctamente cuatro elementos", "explica con evidencia de la ficha", "habla con respeto de los aportes"],
   ["lista de cuatro elementos y una frase"], ["decir que lo inmaterial no es patrimonio", "excluir los aportes migrantes"],
   "Pregunta: «¿Es un objeto o es una práctica?»."),
  "Piensa en algo que tu comunidad o tu barrio hace «desde siempre» y cuéntale a otra persona por qué es importante para ti; no hace falta dar datos personales.",
  "Escribe qué aporte nuevo se ha sumado en los últimos años a tu barrio o comunidad.")

# ======================================================= clase 2
F2 = ("Ficha 2 (lista de ejemplos; los dos primeros son conocidos: Patrimonio Mundial). "
      "1) Las iglesias de madera de Chiloé. "
      "2) El casco histórico de Valparaíso. "
      "3) La cueca, baile tradicional chileno. "
      "4) El mapuzugun, lengua del pueblo mapuche. "
      "5) Un puente antiguo de piedra de la comuna ficticia «Villa Alta». "
      "6) Un cuento oral que cuentan las abuelas de Villa Alta. "
      "7) Una olla de greda guardada en el museo local. "
      "8) El saber de hacer ollas de greda, que se transmite en los talleres de oficio.")
K(O, 2, F2,
  "Hoy aprendo el vocabulario de patrimonio, multiculturalismo e identidad y lo uso para clasificar ejemplos con cuidado.",
  ["El patrimonio material es el que se puede tocar: edificios, ciudades históricas, puentes, objetos. Puede ser inmueble (no se mueve, como una iglesia) o mueble (se puede trasladar, como una olla guardada en un museo). El patrimonio inmaterial es el que se vive y se transmite: lenguas, bailes, fiestas, cuentos, oficios y saberes.",
   "Ambos conviven y se necesitan. Una olla de greda es patrimonio material, y el saber de hacerla es patrimonio inmaterial. Si nadie transmite el saber, el objeto queda sin quien lo continúe. Por eso se cuidan los dos.",
   "Cada pueblo y comunidad es quien porta y explica su patrimonio. Los pueblos originarios, como el mapuche, tienen su propia lengua y sus propias tradiciones, y quienes las enseñan en cada lugar son sus sabias, sabios y comunidades. En la escuela las estudiamos con respeto, sin reducirlas a un espectáculo ni inventar significados."],
  [("patrimonio material", "bienes que se pueden tocar: edificios, objetos, ciudades"), ("patrimonio inmaterial", "saberes, fiestas, lenguas y tradiciones que se transmiten"), ("inmueble", "bien que no se puede trasladar, como un edificio"), ("mueble", "bien que se puede trasladar, como un objeto de museo"), ("pueblo originario", "pueblo que habitaba un territorio antes de la formación del Estado actual")],
  [("Material o inmaterial", "Ficha de ejemplo: «La cueca, baile tradicional chileno». ¿Qué tipo de patrimonio es?", ["La cueca es un baile que se transmite.", "No se toca como un objeto."], "Patrimonio inmaterial"),
   ("Mueble o inmueble", "Ficha de ejemplo: «Un puente antiguo de piedra de la comuna». ¿Es patrimonio mueble o inmueble?", ["No se puede trasladar de un lugar a otro.", "Es una construcción fija."], "Patrimonio material inmueble")],
  [("Clasificar como material solo lo antiguo o grande.", "El patrimonio material puede ser pequeño, como una olla.", "Fíjate si se puede tocar, no en su tamaño."),
   ("Hablar de las tradiciones de un pueblo originario como si estuvieran terminadas o «detenidas en el pasado».", "Los pueblos y sus culturas siguen vivos y cambian.", "Habla en presente y deja que cada comunidad cuente sus saberes.")],
  [("abc", "{F} ¿Cuál es patrimonio material inmueble?", "Las iglesias de madera de Chiloé", "El mapuzugun", "El cuento oral de las abuelas", "Una iglesia es un edificio que no se traslada."),
   ("ab", "En Historia: ¿qué es patrimonio inmaterial?", "Saberes, fiestas y lenguas que se transmiten", "Solo edificios", "Lo inmaterial son las prácticas y los saberes vivos."),
   ("{F} ¿Qué número de la ficha corresponde al cuento oral?", "6", "El cuento oral de las abuelas es el número 6."),
   ("abc", "{F} ¿Cuál es patrimonio inmaterial?", "El mapuzugun", "El puente de piedra", "La olla guardada en el museo", "Una lengua se transmite al hablarla."),
   ("ab", "{F} La olla de greda del museo es…", "Patrimonio material mueble", "Patrimonio inmaterial", "Es un objeto trasladable que se puede tocar."),
   ("=", "{F} De los ocho ejemplos, cuatro son materiales (1, 2, 5 y 7). ¿Cuántos son inmateriales?", "8-4", "Se restan los materiales del total de ocho ejemplos.", " ejemplos"),
   ("abc", "{F} ¿Qué ejemplo es el saber que se transmite en talleres de oficio?", "El 8", "El 5", "El 1", "El número 8 es el saber de hacer ollas de greda."),
   ("abc", "{F} Una persona dice: «La olla y el saber de hacerla son lo mismo». ¿Qué falla?", "La olla es material y el saber es inmaterial", "Nada falla", "Ambas son inmateriales", "Se complementan pero son distintos tipos de patrimonio."),
   ("ab", "En Historia: ¿qué es un pueblo originario?", "Un pueblo que habitaba el territorio antes del Estado actual", "Un grupo recién llegado", "Son pueblos con presencia anterior a la formación del Estado actual."),
   ("abc", "{F} ¿Quién explica mejor el significado de la lengua mapuzugun?", "El propio pueblo mapuche y sus educadoras y educadores", "Quien la estudia desde afuera sin consultar a la comunidad", "Una página cualquiera de internet", "El saber lo porta la comunidad que lo vive."),
   ("abc", "{F} ¿Qué pasaría si se pierde el saber de hacer ollas, pero se conservan las ollas?", "Quedaría el objeto sin quien transmita la técnica", "No cambiaría nada", "Se perderían todas las ollas de inmediato", "El saber inmaterial necesita transmisión para seguir vivo."),
   ("abc", "{F} ¿Qué dimensión está presente al decir que una fiesta reúne a la comunidad?", "Social y cultural", "Solo económica", "Solo política", "Una fiesta involucra costumbres y vínculos entre personas."),
   ("abc", "{F} Alguien dice: «Las tradiciones indígenas son cosa del pasado». ¿Cuál es la mejor respuesta?", "Los pueblos y sus culturas siguen vivos y cambian", "Tiene razón", "Ya nadie las practica", "Hablar en presente respeta a los pueblos y a su continuidad.")],
  ("abc", "En un museo comunitario de ejemplo se exhiben tejidos y también se realiza un taller donde una artesana enseña la técnica. ¿Qué par de patrimonios aparece?", "Material (tejidos) e inmaterial (la técnica)", "Solo material", "Solo inmaterial", "Los tejidos se tocan y la técnica se transmite al enseñarla."),
  [("En Historia: ¿qué es patrimonio material?", "Bienes que se pueden tocar, como edificios y objetos", "Se distingue de lo inmaterial porque se puede tocar."),
   ("En Historia: ¿qué es un inmueble?", "Un bien que no se puede trasladar", "Un edificio es un ejemplo claro de bien inmueble."),
   ("¿Por qué se cuidan los dos tipos de patrimonio?", "Porque se necesitan entre sí", "Un objeto sin el saber queda incompleto.")],
  ("Con la ficha 2, arma una tabla de dos columnas (material e inmaterial) y ubica los ocho ejemplos. Escribe una frase sobre cómo se relacionan el ejemplo 7 y el 8.",
   "Material: 1, 2, 5, 7. Inmaterial: 3, 4, 6, 8. La olla de greda (7) es el objeto y el saber de hacerla (8) permite que se siga produciendo.",
   ["ubica los ocho ejemplos sin errores", "explica la relación entre objeto y saber", "habla de los pueblos y comunidades en presente"],
   ["una tabla de dos columnas y una frase"], ["poner la olla como inmaterial", "usar tiempo pasado para los pueblos"],
   "Pregunta: «¿Se puede tocar o se transmite?»."),
  "Nombra un elemento del patrimonio material y uno inmaterial de tu comuna y dile a alguien por qué son valiosos.",
  "Escribe una frase que explique por qué las tradiciones deben presentarse en tiempo presente.")

# ======================================================= clase 3
F3 = ("Ficha 3 (caso inventado). Pregunta: «¿Por qué cambió la feria costumbrista de Villa Alta entre 1990 y 2023?» "
      "A) Registro municipal de ejemplo: 1990, 20 puestos; 2023, 45 puestos. "
      "B) Relato de ejemplo de una feriante: «Llegaron familias de otros países y trajeron comidas nuevas; también más gente de afuera viene a probar.» "
      "C) Nota de ejemplo del municipio: «Se habilitaron baños y se amplió el espacio de la plaza.» "
      "D) Relato de ejemplo de un artesano: «Antes los puestos eran de oficios; hoy hay más comida que artesanía.»")
K(O, 3, F3,
  "Hoy aprendo, paso a paso, a construir una explicación multicausal y multidimensional con evidencia.",
  ["Una explicación responde a una pregunta con causas y evidencias. Una explicación multicausal reúne varias causas, y una multidimensional las mira desde varios aspectos: cultural, social, económico, político. Los pasos son: 1) escribir la pregunta; 2) reunir las causas que muestran las fuentes; 3) clasificarlas por dimensión; 4) respaldar cada una con una evidencia; 5) redactar un texto con conectores; 6) revisar con honestidad.",
   "En la ficha, la pregunta es por qué cambió la feria. La fuente A muestra que pasó de 20 a 45 puestos. La B habla de familias de otros países que trajeron comidas nuevas (causa cultural y social) y de más visitantes (causa económica). La C muestra una decisión del municipio (causa política) que facilitó el espacio. La D muestra un cambio en los oficios.",
   "Redactar con honestidad es decir de dónde sale cada dato, no agregar lo que las fuentes no dicen y reconocer los límites. Una frase como «según el registro municipal» ayuda al lector a saber en qué te basas."],
  [("explicación", "texto que responde por qué o cómo ocurrió algo, con causas y evidencias"), ("multidimensional", "que mira un hecho desde varios aspectos a la vez"), ("conector", "palabra que une ideas: porque, además, sin embargo"), ("citar la fuente", "decir de dónde viene un dato"), ("límite", "lo que la evidencia no permite afirmar")],
  [("Paso 3: clasificar", "Causa de ejemplo: «el municipio habilitó baños y amplió el espacio». ¿Qué dimensión es?", ["Se trata de una decisión de una autoridad.", "Eso es dimensión política."], "Política"),
   ("Paso 4: respaldar", "Afirmación de ejemplo: «hay más puestos en 2023». ¿Qué evidencia la respalda?", ["Busco un dato en las fuentes.", "El registro municipal indica 20 puestos en 1990 y 45 en 2023."], "El registro municipal de 1990 y 2023")],
  [("Escribir una explicación con una sola causa y sin evidencia.", "Una buena explicación reúne varias causas y las respalda.", "Para cada causa, anota una fuente."),
   ("Agregar datos que no están en las fuentes para que suene mejor.", "Se pierde honestidad.", "Usa solo lo que las fuentes dicen y declara lo que falta.")],
  [("abc", "{F} ¿Cuántos puestos había en 1990?", "20", "45", "25", "El registro municipal indica 20 puestos en 1990."),
   ("ab", "En Historia: ¿qué es una explicación multicausal?", "La que reúne varias causas de un hecho", "La que da una sola causa", "Multi significa varias causas actuando juntas."),
   ("{F} ¿Qué trajeron las familias que llegaron de otros países, según la fuente B?", "comidas nuevas", "La feriante cuenta que trajeron comidas nuevas."),
   ("=", "{F} ¿Cuántos puestos más había en 2023 que en 1990?", "45-20", "Se restan los puestos de 1990 de los de 2023.", " puestos"),
   ("abc", "{F} ¿Qué dimensión destaca la llegada de familias con comidas nuevas?", "Cultural y social", "Solo política", "Solo económica", "Se refiere a costumbres y a la convivencia entre personas."),
   ("ab", "{F} La nota del municipio (C) corresponde a una causa…", "Política", "Religiosa", "Una decisión del municipio es una acción de poder público."),
   ("abc", "{F} ¿Qué cambio señala el artesano en la fuente D?", "Hay más comida que artesanía", "No hay comida", "Hay solo artesanía", "El artesano dice que antes los puestos eran de oficios y hoy hay más comida."),
   ("abc", "{F} ¿Qué paso consiste en respaldar cada causa con una evidencia?", "El paso 4", "El paso 1", "El paso 6", "El paso 4 pide una evidencia para cada causa."),
   ("abc", "{F} Una persona escribe: «La feria creció solo por el municipio». ¿Qué falla?", "Las fuentes muestran otras causas además de la municipal", "Nada falla", "El municipio no existe", "La fuente B muestra causas culturales y económicas."),
   ("ab", "{F} ¿Qué conector sirve para añadir otra causa?", "además", "sin embargo", "«Además» suma una idea nueva; «sin embargo» marca un contraste."),
   ("abc", "{F} ¿Qué dato NO permite afirmar la ficha?", "Cuánto dinero ganan los feriantes", "Que hay 45 puestos en 2023", "Que hay más comida que artesanía", "Ninguna fuente entrega cifras de ingresos."),
   ("abc", "{F} Elige la redacción más honesta:", "Según el registro y los relatos, la feria creció por varias causas, aunque no sabemos cuánto pesó cada una", "La feria creció solo por una causa, y eso es seguro", "La feria no cambió", "Cita fuentes, muestra varias causas y declara un límite."),
   ("abc", "{F} ¿Cuál es una buena pregunta para seguir investigando?", "¿Qué comidas se sumaron y quiénes las preparan?", "¿Cuántos puestos había en 1990?", "¿Qué feria es la mejor del país?", "Se relaciona con el tema y puede responderse con fuentes nuevas; la segunda ya está respondida y la tercera no se puede comprobar.")],
  ("abc", "Un comité cultural de ejemplo prepara un panel sobre cómo cambió su fiesta patronal. Tiene un registro de asistentes (más personas en 2023) y relatos de organizadoras. ¿Cuál es el mejor primer paso?", "Escribir la pregunta que el panel va a responder", "Imprimir fotos", "Elegir los colores", "Todo parte de una pregunta clara."),
  [("¿Qué hago en el paso 5 del método?", "Redacto con conectores usando las causas y evidencias", "Une las ideas en un texto."),
   ("En Historia: ¿qué es citar la fuente?", "Decir de dónde viene un dato", "Permite verificar la información con la fuente original."),
   ("¿Qué es un límite en una explicación?", "Lo que la evidencia no permite afirmar", "Reconocerlo muestra honestidad frente a quien lee.")],
  ("Usa la ficha 3 para escribir una explicación de cuatro frases: una causa cultural, una política, una económica y un límite. Cita la fuente de cada dato.",
   "Según el registro municipal, los puestos pasaron de 20 a 45. Por una parte, la llegada de familias de otros países trajo comidas nuevas (cultural; relato B). Además, el municipio amplió el espacio (política; nota C), y llegó más gente a probar (económica; relato B). No sabemos cuánto pesó cada causa.",
   ["incluye tres dimensiones", "cita la fuente de cada dato", "declara un límite"],
   ["un párrafo de cuatro frases"], ["inventar ingresos o cifras", "no citar fuentes"],
   "Pregunta: «¿Qué fuente respalda esto?»."),
  "Elige un cambio de tu barrio y escribe la pregunta que lo explicaría y dos causas posibles.",
  "Explica con un ejemplo la diferencia entre multicausal y multidimensional.")

# ======================================================= clase 4
F4 = ("Ficha 4 (borrador desordenado de ejemplo sobre la feria de Villa Alta). "
      "1) «Sin embargo, no hay datos sobre cuánto vende cada puesto.» "
      "2) «La feria costumbrista de Villa Alta pasó de 20 puestos en 1990 a 45 en 2023, según el registro municipal.» "
      "3) «Esto ocurrió porque llegaron familias de otros países, además de que el municipio amplió el espacio.» "
      "4) «En conclusión, el cambio de la feria tiene causas culturales, políticas y económicas.»")
K(O, 4, F4,
  "Hoy practico, con apoyo, cómo ordenar y comunicar una explicación con inicio, desarrollo y cierre, usando conectores y citando las fuentes.",
  ["Una explicación escrita se entiende mejor si tiene tres partes. El inicio presenta el hecho y la pregunta (qué cambió). El desarrollo da las causas con sus evidencias. El cierre resume y dice qué queda por saber. Entre las partes usamos conectores: «porque» y «ya que» para dar causas, «además» para sumar, «sin embargo» y «aunque» para marcar un límite, «por lo tanto» o «en conclusión» para cerrar.",
   "Comunicar con honestidad significa decir quién dijo qué. Si un dato viene de un relato, se escribe «según el relato de una feriante». Si es una opinión, no se presenta como hecho. Si hay vacíos, se dice «no hay datos sobre…».",
   "También puedes comunicar de otras formas: una exposición oral de un minuto, un cartel con tres causas o una línea de tiempo con dos fechas. Lo importante es que cada afirmación se apoye en una fuente y que se entienda."],
  [("inicio", "parte que presenta el hecho y la pregunta"), ("desarrollo", "parte que da causas y evidencias"), ("cierre", "parte que resume y señala lo que falta saber"), ("fuente citada", "dato con indicación de dónde sale"), ("exposición oral", "explicación hablada ante otras personas")],
  [("Ordenar el borrador", "Con las cuatro frases de ejemplo (1 límite, 2 hecho, 3 causas, 4 conclusión), ¿cuál va primero?", ["El inicio presenta el hecho con su dato.", "La frase 2 presenta el cambio de 20 a 45."], "La frase 2"),
   ("Elegir un conector", "Quieres decir que el cambio tuvo una causa y, además, otra. ¿Qué conector sirve?", ["Hay que sumar una idea.", "«Además» agrega otra causa."], "Además")],
  [("Escribir un solo párrafo sin partes.", "Se pierde el orden y cuesta entender.", "Separa inicio, desarrollo y cierre."),
   ("Usar «por lo tanto» sin que haya una causa antes.", "El conector promete una conclusión que no llega.", "Úsalo solo cuando cierres con lo ya explicado.")],
  [("abc", "{F} ¿Qué frase del borrador es el inicio?", "La 2", "La 1", "La 4", "La frase 2 presenta el hecho y su dato."),
   ("ab", "En Historia: ¿qué es el cierre de una explicación?", "La parte que resume y dice qué falta saber", "La parte que presenta el hecho", "El cierre concluye con las ideas principales."),
   ("{F} ¿Cuántos puestos había en 2023, según la frase 2?", "45", "La frase 2 indica 45 puestos en 2023."),
   ("=", "{F} Según la frase 2, ¿cuántos puestos se sumaron entre 1990 y 2023?", "45-20", "Se restan los puestos de 1990 a los de 2023.", " puestos"),
   ("abc", "{F} ¿Qué frase es el desarrollo con causas?", "La 3", "La 4", "La 2", "La frase 3 da las causas con «porque» y «además»."),
   ("ab", "{F} ¿Qué frase marca un límite?", "La 1", "La 3", "La 1 dice que no hay datos sobre lo que vende cada puesto."),
   ("abc", "{F} ¿Qué orden es mejor?", "2, 3, 1, 4", "4, 1, 2, 3", "1, 2, 3, 4", "El hecho, las causas, el límite y la conclusión se entienden mejor así."),
   ("abc", "¿Qué conector marca un contraste o límite?", "Sin embargo", "Además", "Porque", "«Sin embargo» introduce una idea que matiza lo anterior."),
   ("abc", "{F} ¿Qué dimensión nombra la frase 4 con «culturales»?", "Se refiere a las costumbres y comidas que trajeron las familias", "Se refiere a la lluvia", "Se refiere al transporte", "La causa cultural viene de la llegada de familias con comidas nuevas."),
   ("ab", "¿Cómo se cita bien un relato?", "«Según el relato de una feriante…»", "«Todo el mundo sabe…»", "Citar es indicar quién lo dijo."),
   ("abc", "{F} Una persona cambia la frase 2 por: «La feria se triplicó». ¿Qué falla?", "20 a 45 no es el triple y cambia el dato de la fuente", "Nada falla", "El triple es correcto", "Pasar de 20 a 45 no equivale a triplicar; hay que usar el dato exacto."),
   ("abc", "{F} Si prefieres exponer en voz alta, ¿cuál es una versión breve y fiel?", "«La feria pasó de 20 a 45 puestos; hubo varias causas, y falta saber cuánto vende cada puesto»", "«La feria es lo mejor del país»", "«No pasó nada»", "Resume el hecho, las causas y el límite."),
   ("abc", "{F} ¿Qué parte del texto te pide aclarar qué falta por saber?", "El cierre", "El inicio", "El título", "El cierre reconoce los límites y propone qué investigar.")],
  ("abc", "En un taller de la biblioteca de ejemplo se pide escribir un párrafo sobre cómo cambió una fiesta del barrio. Una persona empieza con «En conclusión, la fiesta cambió por varias razones». ¿Qué le conviene?", "Empezar con el hecho y su dato, y dejar la conclusión para el final", "Dejarlo así", "Borrar todo", "El orden inicio-desarrollo-cierre ayuda a entender."),
  [("En Historia: ¿qué es el desarrollo?", "La parte que da causas y evidencias", "Es el centro de la explicación."),
   ("En una explicación de HGCS: ¿qué conector sirve para dar la causa de un hecho?", "Porque", "Introduce la razón o causa de algo que ocurrió."),
   ("¿Para qué sirve citar la fuente?", "Para que otras personas puedan verificar el dato", "Da transparencia al texto y confianza a quien lee.")],
  ("Con las cuatro frases de la ficha 4, reescribe un párrafo ordenado: inicio, desarrollo con una causa más, y cierre. Incluye dos conectores distintos y una cita de fuente.",
   "La feria pasó de 20 puestos en 1990 a 45 en 2023, según el registro municipal. Esto ocurrió porque llegaron familias de otros países; además, el municipio amplió el espacio. Sin embargo, no hay datos sobre lo que vende cada puesto. En conclusión, el cambio tiene causas culturales, políticas y económicas.",
   ["ordena inicio, desarrollo y cierre", "usa dos conectores adecuados", "cita la fuente"],
   ["un párrafo de cuatro a cinco frases"], ["cambiar los datos", "no usar conectores"],
   "Pregunta: «¿Se entiende el orden de mi texto?»."),
  "Cuéntale a otra persona en un minuto cómo cambió una costumbre de tu barrio; usa dos conectores.",
  "Haz un cartel con tres causas de un cambio de tu comunidad y la evidencia de cada una.")

# ======================================================= clase 5
F5 = ("Ficha 5 (barrio ficticio «Las Palmas»; datos inventados). "
      "A) Hay un mural colectivo pintado por vecinas y vecinos, entre ellos jóvenes y adultos mayores. "
      "B) El club de baile ensaya cueca y también bailes que trajeron familias de otros países. "
      "C) Un taller de lengua mapuzugun es dirigido por una educadora tradicional mapuche invitada por la comunidad. "
      "D) La junta de vecinos quiere hacer una publicación sobre estas actividades y duda cómo hacerlo con respeto.")
K(O, 5, F5,
  "Hoy aplico lo aprendido a una situación de comunidad: explico y comunico un patrimonio local con responsabilidad y respeto.",
  ["Cuando una comunidad quiere contar su patrimonio, la primera responsabilidad es preguntar a las personas que lo portan. Una publicación sobre un baile, una lengua o una fiesta debe contar con el permiso y la mirada de quienes participan. Así se evita hablar «por» otras personas.",
   "Una explicación honesta en este caso incluye varias dimensiones. Cultural: qué prácticas hay. Social: quiénes participan y cómo se organizan. Económica: si hay costos o apoyos. Política: qué decisiones o permisos hay detrás. Y varias causas: por qué existe hoy esta variedad de actividades (migraciones, interés de vecinos, apoyo de la junta).",
   "Responsabilidad también significa no generalizar. Una educadora mapuche no representa a todo su pueblo, ni una familia migrante a todos sus países. La explicación debe decir «en este barrio» y citar a las personas que aceptaron ser mencionadas."],
  [("consentimiento", "permiso libre de una persona para usar su nombre, imagen o relato"), ("educadora tradicional", "persona que enseña saberes de su pueblo, reconocida por su comunidad"), ("generalizar", "extender algo de un caso a todos los casos"), ("responsabilidad", "hacerse cargo de lo que se dice y se hace"), ("inclusión", "que todas las personas puedan participar")],
  [("Pedir permiso antes de publicar", "La junta quiere publicar una foto de la educadora de mapuzugun. ¿Qué paso es primero?", ["Se trata de su imagen y de su saber.", "Debe aceptar antes."], "Pedirle su consentimiento"),
   ("No generalizar", "Una vecina dice: «Como la educadora enseña así, todos los mapuche lo hacen igual». ¿Qué falla?", ["Es un caso concreto.", "Un pueblo reúne comunidades con realidades distintas."], "Generaliza un caso a todo un pueblo")],
  [("Publicar el relato de una persona sin avisarle.", "Se vulnera su decisión y su confianza.", "Pide consentimiento y muestra el texto antes."),
   ("Explicar la lengua o los saberes de un pueblo con palabras inventadas.", "Se falsea su cultura.", "Deja que la educadora o la comunidad enseñe y explique.")],
  [("abc", "{F} ¿Qué actividad enseña una educadora tradicional mapuche?", "El taller de lengua mapuzugun", "El mural", "El club de baile", "La ficha indica que el taller de mapuzugun lo dirige ella."),
   ("ab", "En Historia: ¿qué es el consentimiento?", "El permiso libre de una persona para usar su relato o imagen", "Un impuesto", "Sin consentimiento no se debe publicar lo de otra persona."),
   ("{F} ¿Qué baile tradicional chileno ensaya el club de baile? Responde con una palabra.", "cueca", "La ficha dice que ensaya cueca."),
   ("=", "{F} Si al mural aportaron 12 jóvenes y 18 personas adultas mayores, ¿cuántas personas de esos dos grupos lo pintaron en total?", "12+18", "Se suman los dos grupos para saber cuántas personas participaron.", " personas"),
   ("abc", "{F} ¿Qué hace la junta primero para publicar con respeto?", "Preguntar a quienes participan y pedir permiso", "Escribir sin consultar", "Copiar un texto de otro lugar", "Debe contar con quienes portan esas prácticas."),
   ("ab", "{F} ¿A qué dimensión pertenece que jóvenes y adultos mayores pinten juntos?", "Social", "Económica", "Se refiere a cómo se relacionan las personas."),
   ("abc", "{F} ¿Qué causa social explica que haya bailes de otros países en el club?", "La llegada de familias migrantes", "La decisión de la junta de cerrar el club", "El cierre de un mercado", "La ficha dice que las familias de otros países trajeron sus bailes."),
   ("abc", "{F} Una persona propone: «Escribamos que todas las familias migrantes bailan lo mismo». ¿Qué responder?", "Mejor decir «en este barrio, el club ensaya también bailes que trajeron algunas familias de otros países»", "Está bien así", "Es mejor agregar un baile inventado", "Se evita generalizar y se cita el caso concreto."),
   ("ab", "{F} ¿Quién debe explicar el sentido del mapuzugun?", "La educadora tradicional y la comunidad", "Quien lo estudia desde afuera sin consultar", "El saber lo transmite quien lo porta."),
   ("abc", "{F} Para incluir a todas las personas en la publicación, ¿qué conviene?", "Ofrecer formas de participar (texto, dibujo, voz) y respetar quien no quiera aparecer", "Obligar a todos a salir", "Dejar fuera a los mayores", "La inclusión respeta la decisión de cada persona."),
   ("abc", "{F} ¿Qué frase del borrador es más honesta?", "«En Las Palmas conviven prácticas de distintos orígenes, según sus participantes»", "«Todas las comunidades del país hacen esto»", "«Nada de esto es patrimonio»", "Habla de un caso y cita a quienes participan."),
   ("abc", "{F} ¿Qué dimensión política podría haber en el caso?", "Los permisos y acuerdos de la junta para usar un espacio", "El tamaño del mural", "La edad de las personas que bailan", "Los permisos son decisiones de organización y poder."),
   ("abc", "{F} Si una persona de la comunidad no quiere aparecer, ¿qué corresponde?", "Respetar su decisión", "Publicar igual", "Insistir hasta que acepte", "El consentimiento incluye poder decir que no.")],
  ("abc", "Una radio comunitaria de ejemplo prepara un programa sobre las fiestas del barrio y quiere entrevistar a una abuela. ¿Qué debe hacer antes de grabar?", "Explicarle el objetivo y pedir su permiso", "Grabar sin avisar", "Cambiar sus palabras", "Se respeta a la persona y se informa del uso de su voz."),
  [("En Historia: ¿qué es generalizar?", "Extender lo de un caso a todos los casos", "Se debe evitar sin evidencia suficiente."),
   ("¿Quién enseña los saberes de un pueblo?", "Quienes los portan, como sus educadoras y educadores", "No se inventan por fuera de la comunidad."),
   ("En el trabajo con patrimonio comunitario: ¿qué es la inclusión?", "Que todas las personas puedan participar", "Implica respeto y apoyo según cada necesidad.")],
  ("Con la ficha 5, diseña un plan de tres pasos para que la junta publique de forma respetuosa y escribe un párrafo explicativo de cuatro frases sobre una actividad (causa, dimensión, cita de fuente y un límite).",
   "Plan: 1) conversar con quienes participan; 2) pedir permiso y mostrar el texto; 3) citar quién aporta cada dato. Párrafo: El club de baile de Las Palmas ensaya cueca y bailes de otros países, según la ficha. Esto ocurre porque llegaron familias migrantes (social y cultural). No sabemos cuántas personas participan.",
   ["plan con consentimiento y citas", "explicación con causa y dimensión", "límite declarado"],
   ["plan de tres pasos y un párrafo"], ["publicar sin permiso", "inventar datos de las comunidades"],
   "Pregunta: «¿Hablo con ellas y ellos o por ellas y ellos?»."),
  "Pregunta a alguien de tu comunidad qué costumbre le gustaría que se registrara y cómo prefiere que se cuente.",
  "Escribe tres criterios de respeto para presentar la cultura de un pueblo.")

# ======================================================= clase 6
F6 = ("Ficha 6 (tres explicaciones inventadas «de ejemplo» para revisar). "
      "A) «La fiesta del barrio cambió porque sí.» "
      "B) «La fiesta del barrio cambió porque llegaron familias migrantes (según un relato), el municipio prestó la cancha (según una nota) y los jóvenes organizaron el programa (según un afiche); falta saber cuánto aportó cada causa.» "
      "C) «Los mapuche hacen todos la fiesta de la misma manera y así será siempre.»")
K(O, 6, F6,
  "Hoy reviso lo logrado: evalúo explicaciones con una pauta, corrijo la mía y decido qué debo repasar.",
  ["Una pauta de revisión tiene cinco preguntas: ¿responde la pregunta?, ¿tiene varias causas?, ¿mira varias dimensiones?, ¿cita fuentes y declara límites?, ¿habla con respeto y sin generalizar? La explicación B de la ficha cumple casi todo. La A no da causas. La C generaliza a todo un pueblo y lo presenta como algo fijo.",
   "Corregir un texto es parte de aprender. Una buena revisión señala lo que falta (por ejemplo, una causa o una cita) y propone cómo mejorarlo. También sirve leer el texto en voz alta o pedir a otra persona que te diga qué entiende.",
   "Para cerrar el módulo, haz una autoevaluación honesta: qué explicas con tus palabras, qué te cuesta y qué vas a hacer. La honestidad incluye reconocer lo que no sabes y asumir la responsabilidad de lo que dices."],
  [("pauta", "lista de preguntas para revisar un trabajo"), ("revisión", "leer de nuevo para mejorar"), ("generalización", "afirmación que extiende un caso a todos"), ("honestidad", "decir la verdad y reconocer lo que no se sabe"), ("responsabilidad", "hacerse cargo de lo que se dice")],
  [("Revisar con la pauta", "Explicación de ejemplo: «La fiesta cambió porque sí». ¿Qué pregunta de la pauta incumple?", ["No da causas.", "No cita ninguna fuente."], "No tiene causas ni fuentes"),
   ("Corregir una causa única", "Frase de ejemplo: «Las familias migrantes cambiaron la feria ellas solas». ¿Cómo se corrige con honestidad?", ["Se evita atribuir todo a una sola causa.", "Se agregan las otras causas y se cita la fuente."], "«Según el registro y los relatos, las familias migrantes aportaron comidas nuevas, junto con otras causas»")],
  [("Corregir solo la ortografía y no el contenido.", "La revisión debe mirar causas, fuentes y respeto.", "Usa las cinco preguntas de la pauta."),
   ("Dejar una explicación sin límites para que parezca más segura.", "Es menos honesta.", "Agrega lo que falta saber.")],
  [("abc", "{F} ¿Qué explicación es la mejor?", "La B", "La A", "La C", "La B cita fuentes, tiene varias causas y declara un límite."),
   ("ab", "En Historia: ¿qué es una pauta de revisión?", "Una lista de preguntas para mejorar un trabajo", "Un premio", "Sirve para revisar un trabajo con criterios claros."),
   ("{F} ¿Cuántas causas menciona la explicación B?", "tres", "Llegada de familias migrantes, cancha prestada y programa organizado por jóvenes."),
   ("=", "{F} Si la pauta tiene cinco preguntas y la explicación A cumple una, ¿cuántas no cumple?", "5-1", "Se restan las preguntas cumplidas del total de la pauta.", " preguntas"),
   ("abc", "{F} ¿Qué falla en la explicación C?", "Generaliza a todo un pueblo", "Tiene muchas causas", "Cita varias fuentes", "Dice que todos hacen la fiesta igual y para siempre."),
   ("ab", "{F} ¿Qué parte de la explicación B es el límite?", "«falta saber cuánto aportó cada causa»", "«llegaron familias migrantes»", "Reconoce lo que no se sabe."),
   ("abc", "{F} ¿Qué dimensión corresponde a «el municipio prestó la cancha»?", "Política", "Climática", "Familiar", "Es una decisión de una autoridad municipal."),
   ("abc", "{F} ¿Cómo se podría mejorar la explicación A?", "Agregando causas, dimensiones y fuentes", "Dejándola igual", "Quitando la fiesta", "Una explicación necesita causas respaldadas con fuentes."),
   ("abc", "{F} Alguien dice: «La explicación C es mejor porque es más corta». ¿Qué falla?", "La calidad depende de la evidencia y del respeto, no del largo", "Nada falla", "No es corta", "Se evalúa con la pauta, no con la extensión."),
   ("ab", "{F} Hablar de un pueblo solo en pasado, ¿qué problema tiene?", "Sugiere que ya no existe o no cambia", "Ninguno", "Los pueblos viven y cambian en el presente."),
   ("abc", "En tu autoevaluación escribes: «Me cuesta separar las dimensiones». ¿Qué conviene hacer?", "Repasar la clase 3 con ejemplos y practicar una tabla", "No hacer nada", "Borrar la dimensión", "Convertir la dificultad en una acción concreta ayuda a avanzar."),
   ("abc", "{F} Si apareciera un nuevo relato que muestra otra causa, ¿qué pasaría con la explicación B?", "Se revisaría y se agregaría con su fuente", "Se ignoraría", "Se borraría todo", "El conocimiento se ajusta con nueva evidencia."),
   ("abc", "{F} ¿Qué frase de cierre es más responsable?", "«Según estas fuentes, hubo varias causas y falta saber cuánto aportó cada una»", "«Ya lo sé todo»", "«No importa»", "Reconoce los límites del conocimiento y evita exagerar.")],
  ("abc", "En una exposición de ejemplo en un centro de adultos, una persona presenta un cartel que dice «Los inmigrantes cambiaron todo en el barrio». ¿Qué corrección es mejor?", "«Según los relatos del barrio, las personas migrantes aportaron nuevas comidas y bailes junto a otros factores»", "Dejar el cartel igual", "Quitar a los migrantes", "Cita fuentes, evita exagerar y reconoce varios factores."),
  [("¿Qué cinco aspectos revisa la pauta?", "Pregunta, causas, dimensiones, fuentes y respeto", "Son las preguntas de la pauta."),
   ("En Historia: ¿qué es la honestidad al explicar?", "Decir lo que las fuentes dicen y reconocer lo que no se sabe", "Por eso no se agregan datos inventados al texto."),
   ("¿Qué hago si mi explicación no cita fuentes?", "Agrego la fuente de cada dato", "Así otras personas pueden verificar lo que afirmas.")],
  ("Elige una explicación tuya de esta unidad (o la A de la ficha) y revísala con las cinco preguntas. Escribe una versión mejorada de tres frases y una autoevaluación de dos frases.",
   "Versión mejorada: la fiesta cambió por varias causas, según relato y afiche: llegaron familias migrantes y los jóvenes organizaron el programa. Falta saber cuánto aportó cada causa. Autoevaluación: logré usar causas y fuentes; me cuesta separar dimensiones; repasaré la tabla.",
   ["aplica las cinco preguntas", "mejora el texto con evidencia", "autoevalúa con una acción"],
   ["texto mejorado y dos frases de autoevaluación"], ["generalizar a un pueblo", "no declarar límites"],
   "Pregunta: «¿Qué le falta a mi explicación?»."),
  "Lee tu explicación en voz alta a alguien y pregúntale qué entendió y qué le faltó.",
  "Escribe tus cinco preguntas de pauta con tus propias palabras.")
