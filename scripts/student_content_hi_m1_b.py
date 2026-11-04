"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 10 (Chile, mercados atlánticos y economía rural)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 10"
MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = "Mapa-resumen de ejemplo del siglo XIX: en el Norte Chico hay minas de plata y de cobre; en la zona central hay haciendas que cultivan trigo; en la zona de Concepción hay minas de carbón; Valparaíso es el puerto principal del comercio con Europa y Estados Unidos."
build(
    OA, 1, F1,
    use="Aprenderé a ubicar a Chile en el comercio mundial del siglo XIX y a distinguir entre vender recursos naturales y ser un país industrializado. Sirve para no confundir «exportar mucho» con «tener fábricas».",
    prior=["Sé qué es una república y qué fue la Independencia de Chile.", "Sé leer un mapa y una tabla sencilla.", "Sé que un producto puede venderse dentro o fuera del país."],
    explain=[
        "Llamamos mundo atlántico a los países europeos y a Estados Unidos que, en el siglo XIX, se industrializaron: Inglaterra, Francia, Alemania y otros. Industrialización es el proceso en que la producción se hace con máquinas y fábricas en gran escala. Esas fábricas necesitaban materias primas (productos naturales sin transformar) y necesitaban mercados donde vender lo que producían.",
        "Chile se conectó con ese mundo. Exportó, es decir, vendió al extranjero, recursos naturales: plata y cobre del norte, carbón de la zona de Concepción y trigo de la zona central, que a mediados de siglo tuvo compradores en California y Australia. A cambio importó, es decir, compró afuera, telas, herramientas y maquinaria. Valparaíso fue el puerto por donde entraba y salía gran parte de ese comercio.",
        "Pero insertarse en el mercado internacional no es lo mismo que industrializarse. Chile vendía sobre todo materias primas y compraba manufacturas, y la mayoría de la población seguía viviendo en el campo, en una economía tradicional y rural basada en la hacienda (gran propiedad agrícola) y el inquilinaje (sistema en que una familia recibía casa y tierra a cambio de trabajar para el dueño).",
    ],
    vocab=[("industrialización", "producción con máquinas y fábricas en gran escala"), ("materia prima", "producto natural sin transformar, como el cobre o el trigo"), ("exportación / importación", "venta de productos al extranjero / compra de productos del extranjero"), ("hacienda", "gran propiedad agrícola, sobre todo de la zona central"), ("inquilinaje", "sistema en que una familia recibe casa y tierra a cambio de trabajo para el dueño")],
    worked=[
        ("Reconocer qué se exporta", "Un puerto de ejemplo despacha al extranjero cobre en barras, trigo en sacos y carbón. Recibe telas, herramientas y una máquina de vapor. ¿Qué productos son materias primas exportadas y cuáles son manufacturas importadas?",
         ["Separo lo que sale del puerto de lo que entra.", "Lo que sale (cobre, trigo, carbón) se extrae o cultiva y casi no se transforma: materias primas.", "Lo que entra (telas, herramientas, máquina) fue fabricado en fábricas extranjeras: manufacturas."], "Exporta materias primas e importa manufacturas"),
        ("Distinguir inserción e industrialización", "Una compañera afirma: «Como Chile vendía tanto afuera, ya era tan industrial como Inglaterra». ¿Qué le falta considerar?",
         ["Vender mucho al exterior muestra conexión con el mercado mundial.", "Pero lo vendido eran recursos naturales y las máquinas se compraban afuera.", "Además, la mayor parte de la gente vivía de la agricultura en haciendas."], "Chile se insertó en el mercado mundial sin industrializarse plenamente"),
    ],
    mistakes=[
        ("Creer que exportar equivale a tener industria.", "Se pueden vender recursos sin transformarlos y comprar las manufacturas afuera.", "Pregunta qué se vende (materia prima o producto fabricado) y dónde se fabrica."),
        ("Pensar que la hacienda desapareció cuando creció el comercio.", "Las haciendas siguieron produciendo, a veces trigo para vender afuera, con trabajo tradicional.", "Busca evidencia de haciendas en la misma época del comercio exterior."),
    ],
    T=[
        ("En Historia: ¿qué es una exportación?", "Un producto que un país vende al extranjero", "Exportar es vender hacia afuera del país."),
        ("{F} ¿Qué recurso se extrae en la zona de Concepción según el mapa-resumen?", "Carbón", "El mapa-resumen lo asigna a esa zona."),
        ("En Historia: ¿qué es la industrialización?", "Un proceso en que se produce con máquinas y fábricas en gran escala", "Es el rasgo del mundo atlántico del siglo XIX."),
        ("{F} ¿Qué zona produce trigo según el mapa-resumen y en qué tipo de propiedad?", "La zona central, en haciendas", "El mapa-resumen une trigo, zona central y hacienda."),
        ("Elige la frase que describe mejor lo que Chile vendía en el siglo XIX. A) sobre todo máquinas fabricadas en el país, B) sobre todo recursos naturales como plata, cobre, trigo y carbón, C) sobre todo ropa y herramientas.", "B", "La economía exportadora chilena se basaba en recursos naturales."),
        ("Una compañera dice: «Valparaíso era importante solo porque tenía muchas fábricas». ¿Qué corrección haces según lo explicado?", "Era importante porque era el puerto principal por donde salían las exportaciones y entraban las importaciones", "Su papel era comercial, no fabril."),
        ("=", "De cada 100 pesos exportados en un año de ejemplo, 60 fueron minerales (plata y cobre) y 25 fueron trigo. ¿Cuántos pesos de cada 100 corresponden a otros productos?", "100-60-25", "Al total se le restan las dos partes conocidas."),
        ("=", "En un contrato de ejemplo (cifras inventadas para practicar), un inquilino debe trabajar 200 días al año para la hacienda. ¿Cuántos días del año (365) le quedan para su propio terreno y descanso?", "365-200", "Se resta el trabajo para la hacienda del total de días."),
        ("Clasifica estos dos rasgos: A) hacienda con inquilinos, B) fábrica con máquinas de vapor. ¿Cuál es el rasgo de la economía rural tradicional?", "A", "La hacienda con inquilinos es el rasgo tradicional y rural."),
        ("{F} Un lector dice que el mapa-resumen prueba que Chile era un país industrial. ¿Qué dato del mapa lo contradice?", "Muestra recursos naturales y haciendas de trigo, no fábricas", "Los datos del mapa son extracción y agricultura."),
        ("Explica en una frase cómo pueden convivir exportaciones al mercado mundial y una hacienda tradicional.", "La hacienda podía producir trigo con trabajo de inquilinos y venderlo en mercados externos", "El comercio externo y el trabajo tradicional no se excluyen."),
        ("Evalúa la idea «Chile entró al mercado mundial como proveedor de materias primas, no como fábrica». A) es acertada porque vendía recursos y compraba manufacturas, B) es falsa porque Chile fabricaba la mayoría de las máquinas, C) es falsa porque Chile no exportaba nada.", "A", "Resume la inserción exportadora sin industrialización plena."),
        ("Una persona dice: «Si Chile exportaba, su campo debía estar modernizado en todo». Da una razón del texto de la clase que muestre que no era así.", "Seguía existiendo una economía tradicional basada en hacienda e inquilinaje", "Persistió el trabajo tradicional en el campo."),
    ],
    ctx=("{F} Para una exposición de curso, un grupo escribe el título «Chile, el país de las grandes fábricas del siglo XIX». Usando el mapa-resumen y lo aprendido, ¿qué título más exacto propones en una frase?", "Por ejemplo: «Chile, exportador de recursos naturales con una economía rural»", "El título debe reflejar minería, trigo y hacienda, no fábricas."),
    sc=[("En Historia: ¿qué es la hacienda?", "Una gran propiedad agrícola, sobre todo de la zona central", "Es el centro de la economía rural tradicional."),
        ("¿Qué es el inquilinaje?", "Un sistema en que una familia recibía casa y tierra a cambio de trabajar para el dueño", "Define la relación entre inquilino y hacendado."),
        ("¿Chile se industrializó plenamente en el siglo XIX por exportar recursos? Responde sí o no y por qué.", "No, porque vendía materias primas y compraba manufacturas", "Exportar no es lo mismo que industrializarse.")],
    op=("Imagina que un compañero resume: «En el siglo XIX Chile vendía cobre y trigo, así que ya era un país industrial». Escribe una respuesta de cuatro líneas que incluya: una corrección, dos productos que Chile exportaba, uno que importaba y una pista de que la economía rural continuaba (por ejemplo, la hacienda).",
        "Exportar no es industrializarse. Chile vendía cobre y trigo, pero compraba telas y máquinas fabricadas afuera. Además, muchas familias vivían como inquilinos en haciendas, lo que muestra una economía rural tradicional.",
        ["corrige la idea de país industrial", "nombra dos exportaciones y una importación", "menciona hacienda o inquilinaje"], ["texto breve de cuatro líneas"], ["decir que exportar es industrializarse", "olvidar la economía rural"], "Pide a una persona de tu casa que marque en tu texto la corrección principal."),
    reinforce="Dibuja un mapa simple de Chile y rotula tres zonas con su recurso o actividad (plata y cobre, trigo, carbón).",
    extend="Escribe dos frases que expliquen por qué Valparaíso era importante para el comercio exterior.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = "Fuente A (informe de un comerciante extranjero a su empresa, texto de ejemplo): «El puerto envía trigo y cobre y recibe telas y herramientas; los campos son extensos y los inquilinos viven en la hacienda.» Fuente B (contrato de ejemplo): «Se entrega al inquilino una casa y una parcela; a cambio trabajará para la hacienda cuando se le ordene.» Fuente C (tabla estatal de ejemplo): exportaciones del año, 60 % minerales, 25 % trigo, 15 % otros. Fuente D (libro de un historiador actual, texto de ejemplo): «La economía chilena creció hacia afuera sin transformar su estructura rural.»"
build(
    OA, 2, F2,
    use="Aprenderé a leer una fuente preguntando quién la escribió, cuándo, para qué y qué no puede decirnos. Sirve para usar bien la evidencia sobre el comercio exterior y la hacienda.",
    prior=["Conozco el comercio de recursos naturales de Chile en el siglo XIX.", "Sé qué son la hacienda y el inquilinaje.", "Sé que una fuente puede ser un texto, una tabla o un mapa."],
    explain=[
        "Una fuente histórica es cualquier testimonio que permite conocer el pasado: un informe, un contrato, una tabla, un libro. Una fuente primaria nació en la época que se estudia, como el contrato de un inquilino o un informe de comerciante. Una fuente secundaria es un estudio posterior, como el libro de un historiador actual, que interpreta fuentes primarias.",
        "Para usar una fuente hay que contextualizarla: preguntar por su procedencia (quién la escribió y cuándo), su intención (para qué se escribió) y su público. Un comerciante extranjero escribe para informar a su empresa y mira la economía desde el negocio; un contrato refleja lo que quería el dueño de la hacienda y lo que aceptaba el inquilino; una tabla estatal muestra lo que el Estado contaba y cómo lo clasificaba.",
        "Ninguna fuente lo dice todo. Cada una tiene límites: el informe del comerciante no cuenta cómo vivía una familia inquilina, y el contrato no dice cuánto se exportaba. Por eso se combinan fuentes distintas y se redacta una conclusión proporcional, es decir, que no afirma más de lo que la evidencia permite.",
    ],
    vocab=[("fuente primaria", "testimonio creado en la época que se estudia"), ("fuente secundaria", "estudio posterior que interpreta fuentes primarias"), ("procedencia", "quién produjo la fuente y cuándo"), ("intención", "propósito con el que se creó la fuente"), ("límite de una fuente", "aquello que la fuente no permite conocer")],
    worked=[
        ("Clasificar y contextualizar", "Se tiene un contrato de ejemplo entre un hacendado y un inquilino, firmado en el siglo XIX. ¿Es fuente primaria o secundaria, y quién tiene más voz en ella?",
         ["El contrato nació en la época estudiada: es primaria.", "Lo redactan las condiciones que impone la hacienda.", "Por eso la voz del dueño pesa más que la del inquilino."], "Fuente primaria; predomina la perspectiva del dueño"),
        ("Señalar un límite", "Un informe de comerciante extranjero dice que las exportaciones aumentaron. ¿Qué no permite saber ese informe?",
         ["El informe habla de comercio, escrito para una empresa.", "No describe el trabajo en la hacienda ni la vida de las familias.", "Falta otra fuente sobre el mundo rural."], "No permite conocer la vida de las familias del campo"),
    ],
    mistakes=[
        ("Aceptar una fuente como verdad completa sin preguntar por su autor.", "Cada autor mira desde su interés y su lugar.", "Anota quién escribió, cuándo y para qué antes de usarla."),
        ("Pensar que una fuente secundaria vale menos o más por ser moderna.", "No es mejor ni peor: tiene otra función, interpretar con distancia.", "Úsala para interpretar y contrástala con fuentes primarias."),
    ],
    T=[
        ("En Historia: ¿qué es una fuente primaria?", "Un testimonio creado en la época que se estudia", "Se define por su origen en el pasado estudiado."),
        ("En Historia: ¿qué significa la procedencia de una fuente?", "Quién la produjo y cuándo", "Es la primera pregunta de contexto."),
        ("{F} ¿La Fuente D es primaria o secundaria?", "Secundaria", "Es un estudio de un historiador actual."),
        ("{F} ¿Quién es el autor de la Fuente A y para quién escribe?", "Un comerciante extranjero, para su empresa", "El enunciado de la fuente entrega autor y destinatario."),
        ("{F} ¿Qué rasgo de la hacienda muestra la Fuente B? A) el inquilino recibe casa y parcela a cambio de trabajo, B) el inquilino es dueño de la tierra, C) el inquilino recibe un sueldo en dinero y no trabaja para la hacienda.", "A", "El contrato plantea intercambio de vivienda y tierra por trabajo."),
        ("{F} Una compañera dice: «La Fuente C, por ser una tabla, no tiene perspectiva». ¿Qué le responderías?", "Que la tabla la hizo el Estado y muestra lo que decidió contar y cómo lo clasificó", "Toda fuente tiene autor y criterios."),
        ("=", "{F} Si el valor total exportado fue 200 millones de pesos de ejemplo, ¿cuántos millones corresponden al 25 % de trigo según la Fuente C?", "200*25//100", "El 25 % de 200 es la cuarta parte."),
        ("=", "{F} Si en la tabla los minerales son el 60 % y el trigo el 25 %, ¿qué porcentaje suman los dos?", "60+25", "Se suman los porcentajes de ambas categorías."),
        ("{F} Según la Fuente A, ¿qué productos entran al puerto desde afuera?", "Telas y herramientas", "El comerciante los menciona como productos que recibe el puerto."),
        ("{F} ¿Qué pregunta sobre el campo no puede responder la Fuente C? A) cuánto del total exportado fue trigo, B) qué sentían las familias inquilinas, C) qué porcentaje fue de minerales.", "B", "La tabla solo cuantifica exportaciones."),
        ("{F} Explica por qué conviene combinar la Fuente B con la Fuente D.", "Porque el contrato muestra la relación concreta de la hacienda y el historiador la interpreta en el conjunto de la economía", "Una fuente primaria y una secundaria se complementan."),
        ("{F} Evalúa la conclusión «Con las Fuentes A y C basta para conocer toda la vida del campo». A) es correcta, B) es excesiva porque ambas hablan de comercio y no de las familias del campo, C) es correcta porque son datos oficiales.", "B", "La conclusión debe ser proporcional a la evidencia."),
        ("{F} Redacta una conclusión de una frase que use la Fuente A y la Fuente B sin afirmar más de lo que dicen.", "Por ejemplo: el puerto comerciaba trigo y cobre mientras en las haciendas los inquilinos trabajaban a cambio de casa y parcela", "Une comercio y hacienda con base en dos fuentes."),
    ],
    ctx=("{F} En una feria escolar se muestra solo la Fuente A y el cartel dice «Así vivían todos los chilenos del siglo XIX». ¿Qué problema de contexto y de límite tiene ese cartel?", "La fuente la escribió un comerciante para su empresa y no cuenta cómo vivían las familias; generaliza demasiado", "La fuente tiene autor y límites."),
    sc=[("En Historia: ¿qué es una fuente secundaria?", "Un estudio posterior que interpreta fuentes primarias", "La define su distancia respecto de la época estudiada."),
        ("Nombra dos preguntas para contextualizar una fuente.", "Quién la escribió y cuándo, o para qué se escribió", "Procedencia e intención son las preguntas básicas."),
        ("¿Qué es el límite de una fuente?", "Aquello que la fuente no permite conocer", "Ninguna fuente lo dice todo.")],
    op=("{F} Con las Fuentes A, B y D de arriba, escribe un párrafo de cinco líneas que responda: «¿Cómo se relacionaban el comercio exterior y la hacienda?». Indica cuál es primaria y cuál secundaria, y anota un límite de las fuentes.",
        "La Fuente A (primaria) muestra que el puerto exportaba trigo y cobre. La Fuente B (primaria) muestra que en la hacienda el inquilino trabajaba a cambio de casa y parcela. La Fuente D (secundaria) interpreta que la economía creció hacia afuera sin cambiar lo rural. Límite: ninguna cuenta la voz de las familias inquilinas.",
        ["usa las tres fuentes", "clasifica primaria y secundaria", "anota un límite"], ["párrafo de cinco líneas"], ["citar solo una fuente", "no anotar límites"], "Pide a alguien de tu casa que lea tu párrafo y señale qué fuente usaste primero."),
    reinforce="Haz una tabla de tres columnas (fuente, autor, límite) con las Fuentes A, B y C.",
    extend="Escribe qué otra fuente (por ejemplo, el testimonio de un inquilino) completaría lo que las fuentes de la clase no dicen.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = "Cuadro de ejemplo, siglo XIX. Cambio: antes los puertos recibían pocos barcos; después, el comercio con Europa y Estados Unidos creció, llegó el ferrocarril entre Santiago y Valparaíso en 1863 y se exportó plata, cobre, trigo y carbón. Continuidad: en la zona central las haciendas seguían siendo la gran unidad agrícola y las familias inquilinas trabajaban a cambio de casa y tierra."
build(
    OA, 3, F3,
    use="Aprenderé a distinguir qué cambió y qué continuó en la economía chilena del siglo XIX y a ubicar esos procesos en el territorio. Sirve para explicar que un país puede modernizarse en algunos aspectos y seguir igual en otros.",
    prior=["Sé qué son exportación, hacienda e inquilinaje.", "Sé leer una fuente con autor y fecha.", "Sé ubicar el Norte Chico, la zona central y Concepción en un mapa."],
    explain=[
        "Un cambio es algo que se transforma con el tiempo; una continuidad es algo que se mantiene. En la historia casi siempre ocurren ambos a la vez. En el siglo XIX cambió la conexión con el mundo: crecieron los puertos, llegaron barcos y capitales extranjeros, y se abrieron minas y vías férreas. El ferrocarril entre Santiago y Valparaíso, inaugurado en 1863, acortó el viaje entre la capital y el puerto.",
        "También hay continuidades. En la zona central la hacienda siguió siendo la gran unidad agrícola y el inquilinaje siguió organizando el trabajo de muchas familias. Eso significa que las nuevas exportaciones, como el trigo, convivían con una forma tradicional de trabajar la tierra y con relaciones de poder desiguales entre el dueño y las familias inquilinas.",
        "El territorio ayuda a ordenar la información. El norte se asocia con minería, el centro con haciendas y trigo, la zona de Concepción con carbón y Valparaíso con comercio. Para comparar, se usa una tabla de cambio y continuidad, y se pregunta siempre: ¿en qué lugar y en qué fechas ocurre esto?",
    ],
    vocab=[("cambio", "algo que se transforma con el tiempo"), ("continuidad", "algo que se mantiene en el tiempo"), ("ferrocarril", "transporte por vías de hierro que conecta lugares y acelera el comercio"), ("territorio", "espacio con características naturales y sociales propias"), ("relación de poder", "vínculo desigual en que una parte decide más que la otra")],
    worked=[
        ("Clasificar cambio y continuidad", "Del cuadro de ejemplo: «llega el ferrocarril entre Santiago y Valparaíso» y «las familias inquilinas siguen trabajando a cambio de casa y tierra». ¿Cuál es un cambio y cuál una continuidad?",
         ["El ferrocarril es algo nuevo: cambio.", "El trabajo del inquilino se mantiene como antes: continuidad."], "El ferrocarril es cambio; el inquilinaje es continuidad"),
        ("Relacionar con el territorio", "¿Por qué el ferrocarril entre la capital y el puerto favorecía la zona central y no tanto el carbón de Concepción?",
         ["El tren unía Santiago con Valparaíso, es decir, la zona central con su puerto.", "Esa línea facilitaba sacar el trigo y otros productos del valle hacia el puerto.", "El carbón de Concepción dependía de otras rutas."], "Porque conectaba la zona central con su puerto"),
    ],
    mistakes=[
        ("Contar solo los cambios y olvidar lo que continúa.", "El resultado parece una modernización total que no existió.", "Haz siempre dos columnas: cambio y continuidad."),
        ("Asignar un cambio a todo el territorio por igual.", "Minería, haciendas y puertos estaban en zonas distintas.", "Escribe en qué región ocurre cada proceso."),
    ],
    T=[
        ("En Historia: ¿qué es una continuidad?", "Algo que se mantiene en el tiempo", "Se opone a cambio."),
        ("{F} ¿En qué año llegó el ferrocarril entre Santiago y Valparaíso según el cuadro?", "1863", "El cuadro lo señala en la fila de cambio."),
        ("{F} ¿Qué unidad agrícola siguió siendo central en la zona central?", "La hacienda", "El cuadro la presenta como continuidad."),
        ("{F} Clasifica como cambio o continuidad: «se exporta plata, cobre, trigo y carbón».", "Cambio", "Es parte de la conexión con mercados nuevos."),
        ("{F} Clasifica como cambio o continuidad: «las familias inquilinas trabajan a cambio de casa y tierra».", "Continuidad", "El cuadro lo describe como práctica que sigue."),
        ("Une cada actividad con su zona: 1) minería de plata y cobre, 2) haciendas de trigo, 3) carbón. a) zona central, b) Concepción, c) Norte Chico. Escribe las parejas.", "1-c, 2-a, 3-b", "Cada recurso se ubica en su zona."),
        ("=", "En un problema de ejemplo (cifras inventadas para practicar), un viaje de carga entre Santiago y Valparaíso tardaba 48 horas por camino y 12 horas por tren. ¿Cuántas horas se ahorraban?", "48-12", "El ahorro es la diferencia entre ambos tiempos."),
        ("=", "En una hacienda de ejemplo había 40 familias inquilinas; 6 se fueron a trabajar a una mina. ¿Cuántas familias inquilinas quedaron?", "40-6", "Se resta las que se fueron."),
        ("{F} Una compañera dice: «Con el ferrocarril, toda la economía rural dejó de ser tradicional». ¿Qué evidencia del cuadro la contradice?", "Las haciendas y el inquilinaje continuaban en la zona central", "La continuidad rural sigue en el cuadro."),
        ("Explica por qué hablar solo de «modernización» deja fuera a las familias inquilinas.", "Porque ellas seguían bajo relaciones de poder tradicionales con el dueño aunque llegara el comercio", "El trabajo del campo no cambió al mismo ritmo."),
        ("Evalúa la afirmación «el ferrocarril y las exportaciones cambiaron el comercio, pero no eliminaron la hacienda». A) es exacta, B) es inexacta porque la hacienda desapareció en 1863, C) es inexacta porque no hubo exportaciones.", "A", "Combina cambio comercial y continuidad rural."),
        ("Propón dos columnas para un cuadro de tu curso sobre la economía chilena del siglo XIX, con un dato en cada una.", "Cambio: llegada del ferrocarril; continuidad: haciendas con inquilinos", "El cuadro debe tener ambos tipos de datos."),
        ("¿Qué pregunta de territorio harías ante la frase «el trigo se exportaba»? Escríbela.", "Por ejemplo: ¿de qué zona salía el trigo y por qué puerto?", "La pregunta ubica el proceso en el espacio."),
    ],
    ctx=("{F} Un afiche escolar dice: «En el siglo XIX todo cambió en Chile». Con el cuadro de ejemplo, escribe una frase que lo corrija mencionando un cambio y una continuidad.", "Cambió la conexión con el mundo por puertos y ferrocarril, pero continuó la hacienda con inquilinos", "La corrección debe incluir ambos aspectos."),
    sc=[("En Historia: ¿qué es un cambio?", "Algo que se transforma con el tiempo", "Es lo contrario de continuidad."),
        ("Nombra una continuidad rural del siglo XIX.", "La hacienda o el inquilinaje", "Siguieron organizando el campo."),
        ("¿En qué zona se asocian las haciendas de trigo?", "En la zona central", "Es la zona de haciendas.")],
    op=("{F} Con el cuadro de ejemplo de arriba, construye una tabla de dos columnas (cambio y continuidad) con al menos tres filas, y escribe una frase final que diga por qué no puede decirse que «todo cambió».",
        "Cambio: llegada del ferrocarril 1863; cambio: exportación de plata, cobre, trigo y carbón; continuidad: hacienda como unidad agrícola; continuidad: inquilinos trabajan por casa y tierra. Conclusión: aunque creció el comercio, el campo mantuvo relaciones tradicionales.",
        ["tabla con dos columnas", "al menos tres filas", "frase final con límite"], ["tabla y frase"], ["poner todo como cambio", "no cerrar con conclusión"], "Revisa con una persona de tu casa que cada dato esté en la columna correcta."),
    reinforce="Toma tres datos del cuadro de la clase y clasifícalos en cambio o continuidad en una tabla.",
    extend="Escribe una pregunta sobre qué zonas del territorio se beneficiaron menos del ferrocarril.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = "Voces de ejemplo, redactadas para este cuaderno. Hacendado: «Los precios del trigo suben; necesito más trabajo en la cosecha.» Comerciante del puerto: «Compro trigo y cobre y vendo telas.» Familia inquilina: «Tenemos casa y tierra, pero debemos trabajar cuando la hacienda lo ordena.» Minero del norte: «El trabajo en la mina es duro y se paga según el mineral que se saque.»"
build(
    OA, 4, F4,
    use="Aprenderé a distinguir actores, sus intereses y las causas del comercio exterior y de la hacienda. Sirve para explicar un proceso sin culpar a un solo grupo ni suponer que todos pensaban igual.",
    prior=["Distingo cambio y continuidad en un cuadro.", "Sé qué es una fuente y quién la escribe.", "Sé que hacendados, comerciantes, mineros e inquilinos tenían trabajos distintos."],
    explain=[
        "Un actor histórico es una persona o grupo que actúa y toma decisiones en un proceso. En la economía del siglo XIX actuaban hacendados, comerciantes, empresarios extranjeros, mineros, familias inquilinas y el Estado. Cada uno tenía intereses distintos: el hacendado buscaba vender su trigo y contar con trabajadores; el comerciante, ganar con la compra y venta; la familia inquilina, mantener su casa y su tierra.",
        "Los procesos históricos casi nunca tienen una sola causa. La multicausalidad significa que un hecho se explica por varias causas al mismo tiempo. El crecimiento de las exportaciones se explica por la demanda del mundo atlántico, por la riqueza de las minas, por las rutas marítimas y por las políticas del Estado, entre otras causas, y no solo por una de ellas.",
        "Una perspectiva es el punto de vista desde el que se mira un hecho. La economía exportadora favoreció más a quienes tenían tierras, capital o barcos que a quienes trabajaban para ellos. Al contrastar perspectivas se ve que un mismo proceso fue vivido de modo diferente, y que las relaciones entre dueños y trabajadores eran desiguales.",
    ],
    vocab=[("actor histórico", "persona o grupo que actúa y toma decisiones en un proceso"), ("interés", "aquello que un actor busca lograr"), ("causa", "factor que ayuda a explicar por qué ocurre un hecho"), ("multicausalidad", "explicación de un hecho por varias causas a la vez"), ("perspectiva", "punto de vista desde el que se mira un hecho")],
    worked=[
        ("Reconocer intereses", "En las voces de ejemplo, ¿qué buscan la familia inquilina y el hacendado?",
         ["La familia inquilina dice que tiene casa y tierra, pero debe trabajar cuando se le ordena: busca conservar su vivienda y su tierra.", "El hacendado menciona precios altos y necesidad de más trabajo: busca vender trigo y asegurar mano de obra."], "La familia busca conservar casa y tierra; el hacendado, vender y asegurar trabajo"),
        ("Pasar de una causa a varias", "Un compañero afirma: «Las exportaciones crecieron solo porque había minas». Da dos causas más que complementen su explicación.",
         ["Las minas son una causa.", "El mundo atlántico demandaba materias primas.", "Los puertos y barcos hacían posible vender afuera."], "Demanda del mundo atlántico y puertos y barcos"),
    ],
    mistakes=[
        ("Explicar el crecimiento exportador con una sola causa.", "Los hechos históricos suelen tener varias causas que se combinan.", "Escribe al menos tres factores y ordénalos por su peso."),
        ("Suponer que todos los actores quedaron igual de beneficiados.", "Dueños y trabajadores tenían intereses y posiciones distintas.", "Compara qué ganó y qué perdió cada actor."),
    ],
    T=[
        ("En Historia: ¿qué es un actor histórico?", "Una persona o grupo que actúa y toma decisiones en un proceso", "Define a quienes participan en los hechos."),
        ("{F} ¿Qué compra y qué vende el comerciante del puerto?", "Compra trigo y cobre y vende telas", "Su voz de ejemplo lo dice."),
        ("En Historia: ¿qué es una perspectiva?", "El punto de vista desde el que se mira un hecho", "Cada actor mira desde su lugar."),
        ("{F} ¿Quién menciona los precios del trigo como motivo de actuar?", "El hacendado", "Su voz lo dice."),
        ("{F} Une cada actor con su interés: 1) hacendado, 2) familia inquilina, 3) comerciante. a) ganar con la compra y venta, b) conservar casa y tierra, c) vender trigo y asegurar trabajadores. Escribe las parejas.", "1-c, 2-b, 3-a", "Cada voz expresa un interés propio."),
        ("{F} Elige la mejor razón de que la voz del minero sea una perspectiva distinta a la del hacendado. A) su trabajo es la mina y su pago depende del mineral que saque, B) es el dueño de la mina y decide cuánto pagar, C) busca lo mismo que el hacendado: vender trigo.", "A", "Su lugar en la economía es distinto."),
        ("=", "En una hacienda de ejemplo, de 50 familias, 35 son inquilinas y el resto son peones sin tierra. ¿Cuántas son peones?", "50-35", "El total menos las inquilinas."),
        ("=", "Una mina de ejemplo emplea 120 mineros; 30 son extranjeros. ¿Cuántos mineros no son extranjeros?", "120-30", "Se resta el grupo extranjero del total."),
        ("Una compañera dice que «el éxito del trigo se debe solo a la voluntad de los hacendados». Según lo explicado en la clase, menciona una causa distinta que lo complete.", "La demanda de compradores en mercados externos", "El trigo se vendió por la demanda externa."),
        ("Explica por qué la frase «el hacendado y la familia inquilina tenían los mismos intereses» es discutible.", "Porque el hacendado buscaba trabajo y ganancias mientras la familia buscaba conservar casa y tierra bajo órdenes", "Las posiciones de poder eran desiguales."),
        ("{F} ¿Qué diferencia hay entre la situación de la familia inquilina y la del comerciante en las voces de ejemplo?", "La familia depende del permiso del dueño para trabajar y vivir; el comerciante vive de comprar y vender", "Una relación es de dependencia y la otra de intercambio."),
        ("Evalúa la afirmación «el comercio exterior benefició a todos los grupos del campo por igual». A) es correcta, B) es discutible porque dueños y trabajadores tenían posiciones desiguales, C) es correcta porque había exportaciones.", "B", "Las ganancias y las cargas no se repartieron igual."),
        ("Redacta una pregunta que contraste la perspectiva del hacendado con la de la familia inquilina.", "Por ejemplo: ¿qué ganaba y qué perdía cada uno con el aumento del trigo exportado?", "La pregunta compara beneficios de ambos."),
    ],
    ctx=("{F} Un compañero prepara una dramatización sobre una hacienda y pone a todos los personajes diciendo «estamos felices con el comercio». Con las voces de ejemplo, ¿qué cambiarías para mostrar perspectivas distintas?", "Haría que el hacendado hablara de vender y la familia inquilina de las órdenes y de conservar casa y tierra", "Las perspectivas deben diferir según el interés y el poder."),
    sc=[("En Historia: ¿qué significa multicausalidad?", "Que un hecho se explica por varias causas a la vez", "Evita las explicaciones de una sola causa."),
        ("¿Qué es un interés en historia?", "Aquello que un actor busca lograr", "Orienta sus decisiones."),
        ("Nombra dos actores de la economía del siglo XIX.", "Por ejemplo: el hacendado y la familia inquilina", "Son actores con posiciones distintas.")],
    op=("{F} Elige dos voces de ejemplo de arriba (por ejemplo, el hacendado y la familia inquilina). Escribe cinco líneas: qué busca cada uno, una causa del crecimiento de las exportaciones y una diferencia de poder entre ambos.",
        "El hacendado busca vender trigo y asegurar trabajo. La familia inquilina busca conservar casa y tierra. Una causa del crecimiento exportador fue la demanda de materias primas del mundo atlántico. El hacendado decidía las órdenes y la familia dependía de ellas.",
        ["usa dos voces", "señala una causa", "marca la diferencia de poder"], ["texto de cinco líneas"], ["decir que ambos tienen el mismo interés", "no marcar poder"], "Muestra tu texto a una persona y pregúntale qué diferencia de poder identifica."),
    reinforce="Haz una tabla con tres actores del campo y escribe un interés para cada uno.",
    extend="Explica por qué la multicausalidad ayuda a evitar explicaciones que culpan a un solo grupo.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = "Dossier de ejemplo. Dato 1: la exportación de trigo, cobre y carbón creció en el siglo XIX gracias a mercados externos. Dato 2: Chile compraba textiles y maquinaria fabricados afuera. Dato 3: en la zona central la hacienda y el inquilinaje continuaron organizando el trabajo. Dato 4: el ferrocarril entre Santiago y Valparaíso abrió en 1863."
build(
    OA, 5, F5,
    use="Aprenderé a construir un argumento: una tesis, evidencia y un límite. Sirve para responder con claridad si Chile se industrializó o si siguió siendo un país rural con comercio exterior.",
    prior=["Conozco la exportación de recursos naturales y la hacienda.", "Sé distinguir cambio y continuidad.", "Sé que una conclusión debe apoyarse en fuentes."],
    explain=[
        "Un argumento es una respuesta razonada a una pregunta. Tiene una tesis (la afirmación que defiendes), evidencias (datos o fuentes que la apoyan) y un límite (aquello que la evidencia no permite afirmar). Por ejemplo, ante la pregunta «¿Se industrializó Chile en el siglo XIX?», una tesis posible es que Chile se insertó en el mercado mundial como exportador de materias primas, sin industrializarse plenamente.",
        "Las evidencias deben ser pertinentes, es decir, estar relacionadas con la tesis. Para la tesis anterior sirven el dato de que se exportaban trigo, cobre y carbón, el dato de que se importaban textiles y maquinaria, y el dato de que la hacienda y el inquilinaje continuaban. Un dato que no se relaciona, como el nombre de un barco, no sostiene la tesis.",
        "El límite protege de exagerar. Con el dossier no podemos afirmar que no hubo ninguna fábrica en Chile ni que todos los inquilinos vivieran igual; solo que, en el conjunto, la economía dependía de la exportación de recursos y de un campo tradicional. Un buen argumento es claro, usa dos o más evidencias y reconoce su límite.",
    ],
    vocab=[("argumento", "respuesta razonada a una pregunta, con tesis y evidencias"), ("tesis", "afirmación principal que se defiende"), ("evidencia", "dato o fuente que apoya una tesis"), ("pertinente", "que se relaciona directamente con lo que se discute"), ("límite", "aquello que la evidencia no permite afirmar")],
    worked=[
        ("Elegir evidencias", "Para sostener la tesis «Chile exportaba materias primas sin industrializarse plenamente», ¿qué dos datos del dossier sirven?",
         ["El dato 1 muestra exportaciones de trigo, cobre y carbón.", "El dato 2 muestra que compraba textiles y maquinaria afuera.", "Ambos se relacionan directamente con la tesis."], "Los datos 1 y 2"),
        ("Formular un límite", "Con el dossier, ¿qué afirmación sería excesiva: «no existió ninguna fábrica en Chile»?",
         ["El dossier no menciona fábricas, pero tampoco prueba que no existieran.", "Decir «ninguna» afirma más de lo que los datos permiten."], "Es excesiva porque el dossier no prueba que no existiera ninguna fábrica"),
    ],
    mistakes=[
        ("Escribir una tesis sin evidencia.", "Una opinión sin datos no convence ni se puede comprobar.", "Añade al menos dos datos del dossier."),
        ("Usar evidencia que no tiene relación con la pregunta.", "El dato no es pertinente.", "Pregúntate cómo apoya cada dato la tesis."),
    ],
    T=[
        ("En Historia: ¿qué es una tesis?", "La afirmación principal que se defiende", "Es el centro del argumento."),
        ("En Historia: ¿qué es una evidencia?", "Un dato o fuente que apoya una tesis", "Sostiene lo que se afirma."),
        ("{F} ¿Qué dato del dossier muestra que Chile compraba productos fabricados afuera?", "El dato 2", "Menciona textiles y maquinaria."),
        ("{F} ¿Qué dato del dossier se relaciona con la persistencia de la economía rural? A) dato 1, B) dato 3, C) dato 4.", "B", "El dato 3 habla de hacienda e inquilinaje."),
        ("Elige la tesis mejor formulada. A) Chile era un país bonito, B) Chile se insertó en el mercado mundial como exportador de materias primas sin industrializarse plenamente, C) Hubo muchos barcos.", "B", "Es una afirmación defendible con datos."),
        ("Una compañera usa como evidencia «el ferrocarril abrió en 1863» para sostener que la hacienda desapareció. ¿Por qué no es pertinente?", "Porque el ferrocarril no prueba que la hacienda desapareciera", "El dato no se relaciona con esa tesis."),
        ("=", "{F} Si el dossier tiene 4 datos y 2 apoyan la inserción exportadora, ¿cuántos datos quedan para otras ideas?", "4-2", "Se restan los datos usados."),
        ("=", "Un grupo escribe 5 líneas: 1 de tesis, 3 de evidencia y el resto de límite. ¿Cuántas líneas son de límite?", "5-1-3", "Se restan tesis y evidencia del total."),
        ("{F} Con los datos 3 y 4, ¿qué conclusión proporcional puedes escribir?", "Que el ferrocarril mejoró la conexión, pero el campo central siguió con hacienda e inquilinaje", "Une cambio y continuidad sin exagerar."),
        ("Explica por qué un buen argumento incluye un límite.", "Porque evita afirmar más de lo que la evidencia permite", "El límite da honestidad intelectual."),
        ("Un compañero escribe: «Chile no tuvo nada de industria; todos los inquilinos vivían igual». Señala la exageración.", "Afirma «nada» y «todos» sin evidencia suficiente", "Los absolutos rara vez se sostienen."),
        ("Evalúa este argumento: «Chile exportó recursos (dato 1) y siguió con hacienda (dato 3), por lo que no se industrializó plenamente». A) es sólido porque usa dos evidencias pertinentes, B) es débil porque no usa datos, C) es falso porque no hubo exportaciones.", "A", "Tiene tesis y dos evidencias que la sostienen."),
        ("Redacta una pregunta que exigiría otra fuente para completar el argumento.", "Por ejemplo: ¿qué opinaban las familias inquilinas sobre su trabajo en la hacienda?", "La pregunta señala un vacío del dossier."),
    ],
    ctx=("{F} Para un debate, te piden defender o refutar «Chile fue un país industrializado en el siglo XIX». Con el dossier, escribe en dos frases tu posición y tu mejor evidencia.", "Refuto: Chile exportaba recursos y compraba manufacturas (datos 1 y 2), y la hacienda continuaba (dato 3)", "La posición debe usar evidencia pertinente."),
    sc=[("En Historia: ¿qué es un argumento?", "Una respuesta razonada a una pregunta, con tesis y evidencias", "Se apoya en datos."),
        ("¿Para qué sirve el límite en un argumento?", "Para no afirmar más de lo que la evidencia permite", "Evita exagerar las conclusiones."),
        ("Nombra una evidencia sobre la persistencia de lo rural.", "La hacienda y el inquilinaje continuaban", "Es el dato 3 del dossier.")],
    op=("{F} Responde en un párrafo de seis líneas con el dossier de ejemplo de arriba: «¿Cuál fue la relación de Chile con el mundo atlántico en el siglo XIX y qué continuó en el campo?». Incluye una tesis, dos datos del dossier y un límite.",
        "Chile se vinculó al mundo atlántico exportando trigo, cobre y carbón y comprando textiles y maquinaria, pero no se industrializó plenamente. Al mismo tiempo, en la zona central la hacienda y el inquilinaje continuaron. Con estos datos no puede afirmarse cómo vivía cada familia.",
        ["tesis clara", "dos datos del dossier", "límite explícito"], ["párrafo de seis líneas"], ["no escribir tesis", "no incluir límite"], "Pide a una persona de tu casa que subraye tu tesis en tu texto."),
    reinforce="Reescribe tu tesis en una sola frase y debajo anota los dos datos del dossier que la apoyan.",
    extend="Escribe una segunda tesis posible sobre el campo chileno y señala qué dato nuevo necesitarías.",
    materials=MAT,
)
