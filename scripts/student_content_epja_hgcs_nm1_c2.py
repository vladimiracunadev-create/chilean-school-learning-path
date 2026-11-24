"""Historia, Geografía y Ciencias Sociales EPJA Media N1, módulo 3 (parte 2): OAD-10, explicar con multicausalidad y multidimensionalidad procesos de Chile del siglo XIX y la primera mitad del siglo XX considerando distintas perspectivas. Todas las fuentes y los datos numéricos son de ejemplo, inventados para este cuaderno, y se leen en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y cuaderno. Todas las fuentes y los datos numéricos son extractos o cifras inventados «de ejemplo», escritos en cada ejercicio: no son citas de personas reales y no necesitas internet, mapas ni libros. "
             "Los hechos generales que se mencionan son los que se enseñan en los programas escolares. Tu experiencia de vida es bienvenida, pero nadie te pide contar datos personales ni de tu familia. "
             "Si un tema te trae recuerdos difíciles, puedes trabajar solo con los casos del cuaderno.")
build = make_build(MATERIALS)

O = "EPJA-HGCS-NM1-OAD-10"

# ======================================================= clase 1
F1 = ("Ficha 1 (de ejemplo). Carta inventada de la familia Soto (ficticia), hacia 1910, a unos parientes: «Dejamos el campo y nos vinimos a la ciudad. "
      "La tierra ya no alcanzaba para todos los hijos. En la ciudad se decía que había trabajo en las fábricas. El tren nos permitió viajar. Y un primo ya vivía aquí y nos recibió.»")
build(
    O, 1, F1,
    use="Hoy descubro que los hechos tienen varias causas, parto de ejemplos de la vida diaria y los llevo a un proceso de la historia de Chile.",
    prior=["Reconozco quién habla en una fuente.", "Sé que una perspectiva es un punto de vista.", "Distingo un hecho de una opinión."],
    explain=[
        "Casi nada ocurre por una sola razón. Cuando sube la cuenta de la luz influye el consumo, el precio y quizás un cambio de tarifa. Tú ya lo sabes por experiencia: para explicar algo buscas varias causas. En historia hacemos lo mismo; a esto se le llama multicausalidad.",
        "Un proceso también tiene varias dimensiones, es decir, aspectos desde los que se mira: lo político, lo económico, lo social y lo medioambiental. En el siglo XX muchas familias dejaron el campo y se fueron a las ciudades. Las razones fueron económicas (trabajo), sociales (parientes que ya vivían allí) y de transporte (llegó el tren).",
        "Explicar bien es nombrar varias causas, decir de qué tipo son y mostrar de qué fuente salen. Así no quedamos con una explicación simple y cerrada.",
    ],
    vocab=[("causa", "razón que ayuda a que algo ocurra"), ("consecuencia", "efecto que se produce después de un hecho"), ("multicausalidad", "idea de que un hecho tiene varias causas"), ("dimensión", "aspecto desde el que se mira un proceso"), ("migrar", "dejar un lugar para vivir en otro")],
    worked=[
        ("Contar causas", "{F} ¿Cuántas razones da la familia en la carta?", ["Primera: la tierra no alcanzaba.", "Segunda: había trabajo en fábricas; tercera: el tren; cuarta: un primo los recibió."], "Cuatro razones"),
        ("Clasificar una causa", "{F} ¿A qué dimensión pertenece «había trabajo en las fábricas»?", ["Habla de trabajo y producción.", "El trabajo y la producción son parte de lo económico."], "Dimensión económica"),
    ],
    mistakes=[("Explicar un proceso con una sola causa («se fueron porque el campo era pobre»).", "Los procesos reales se explican con varias causas al mismo tiempo.", "Pregunta siempre: ¿qué más influyó?, y busca otras razones en las fuentes."),
              ("Mezclar una causa con una consecuencia.", "Lo que pasa después no es la razón de lo que pasó antes.", "Pregunta: ¿esto pasó antes y provocó el hecho, o pasó después?")],
    T=[
        ("abc", "En HGCS: ¿qué es una causa?", "Una razón que ayuda a que algo ocurra", "Un efecto que viene después", "Una fecha importante", "La causa precede y contribuye a que algo suceda."),
        ("abc", "{F} ¿Dónde vivía la familia Soto antes de venir a la ciudad?", "En el campo", "En el extranjero", "En un puerto", "La carta comienza diciendo que dejaron el campo."),
        ("{F} ¿Cuál fue el medio de transporte mencionado en la carta?", "El tren", "La carta nombra el tren como el que les permitió viajar."),
        ("abc", "{F} ¿Qué causa de la carta es de tipo social?", "Un primo ya vivía en la ciudad y los recibió", "Había trabajo en las fábricas", "La tierra no alcanzaba", "Las redes de parientes y vecinos son parte de lo social."),
        ("ab", "{F} La frase «la tierra ya no alcanzaba para todos los hijos» se refiere a:", "Una razón económica del campo", "Un efecto del tren", "Habla de recursos para vivir, que es un tema económico."),
        ("abc", "{F} ¿Cuál es la consecuencia de las causas descritas?", "La familia se trasladó a la ciudad", "El tren se averió", "Las fábricas cerraron", "El traslado es el hecho que las causas explican."),
        ("=", "Dato de ejemplo: la ciudad tenía 30.000 habitantes en 1900 y 48.000 en 1930. ¿Cuántos habitantes más había en 1930?", "48000-30000", "Se resta la población inicial de la final para ver el aumento.", " habitantes"),
        ("abc", "Una persona explica por qué subió el precio del pan: «Solo porque los panaderos quieren ganar más». ¿Qué falla en esa explicación?", "Menciona una sola causa, sin revisar otras como el costo de la harina", "Usa la palabra pan", "No tiene verbos", "Los hechos económicos suelen tener varias causas."),
        ("abc", "{F} Un vecino dice: «Se fueron del campo solo por el tren». ¿Qué respuesta es más exacta?", "El tren ayudó, pero también influyeron la falta de tierra, el trabajo y los parientes", "El tren no tuvo ninguna influencia", "Es la única causa", "La carta da cuatro razones, no solo el tren."),
        ("abc", "{F} Si la carta no dijera que había trabajo en la ciudad, ¿qué causa faltaría en la explicación?", "La económica de buscar trabajo", "La medioambiental", "La política", "El trabajo fue una razón central en el relato."),
        ("ab", "{F} ¿Por qué no basta una sola causa?", "Porque los procesos tienen varias razones que se influyen", "Porque la carta es muy corta", "Una sola causa deja afuera otras que también influyen."),
        ("abc", "{F} ¿Qué pregunta ayuda a buscar más causas?", "¿Qué más influyó en esta decisión?", "¿Quién tiene la razón?", "¿Cuántas líneas tiene la carta?", "Ampliar la mirada lleva a encontrar otras razones."),
        ("abc", "{F} Una buena explicación breve del traslado es:", "La familia se fue a la ciudad porque no alcanzaba la tierra, había trabajo en fábricas, existía el tren y un primo los recibió", "La familia se fue por gusto", "Solo se fueron por el tren", "Reúne varias causas de distinto tipo con datos de la carta."),
    ],
    ctx=("abc", "En un taller de empleo, una persona cuenta que cambió de ciudad porque «surgió trabajo». El facilitador pregunta qué otras razones influyeron. ¿Por qué hace esa pregunta?", "Porque las decisiones suelen tener varias causas", "Porque quiere cambiar el tema", "Porque duda de su palabra", "Buscar otras razones es parte de explicar con varias causas."),
    sc=[("En HGCS: ¿qué es la multicausalidad?", "La idea de que un hecho tiene varias causas", "Explica por qué una sola razón no basta."),
        ("En HGCS: ¿Qué es una consecuencia?", "Un efecto que viene después de un hecho", "Se produce a partir de las causas."),
        ("¿Qué dimensión tiene el trabajo y la producción?", "La económica", "Se relacionan con la producción y los empleos.")],
    op=("Ficha de ejemplo: «Entre 1920 y 1940 una ciudad de ejemplo duplicó su población. Datos: llegaron familias del campo; se abrieron escuelas; se instalaron fábricas; mejoró el transporte público.» "
        "Escribe tres causas de ese crecimiento, indica la dimensión de cada una y una consecuencia posible.",
        "Causas: llegaron familias del campo (social), se instalaron fábricas (económica), mejoró el transporte (económica y social). Consecuencia posible: faltaron viviendas y se llenaron los barrios populares.",
        ["nombra tres causas tomadas del texto", "indica una dimensión para cada una", "propone una consecuencia razonable"],
        ["una lista de tres causas con su dimensión y una consecuencia"], ["dar una sola causa", "confundir causa y consecuencia"],
        "Pregunta: «¿Esto pasó antes y provocó el hecho, o vino después?»."),
    reinforce="Elige un cambio de tu barrio o trabajo y anota tres razones que lo explican, sin nombrar a personas.",
    extend="Explica con un ejemplo por qué una sola causa nunca alcanza para explicar un proceso histórico.",
)

# ======================================================= clase 2
F2 = ("Ficha 2 (de ejemplo). Texto escrito para este cuaderno. Hacia 1930, la crisis económica mundial redujo las ventas de salitre y cobre al exterior y muchas personas perdieron su trabajo en la minería. "
      "Muchas familias se trasladaron a las ciudades o dependieron de ayuda. Más adelante el Estado impulsó la industria nacional, y en 1939 se creó la CORFO. "
      "Causa de fondo: la dependencia de la economía de pocas exportaciones. Causa inmediata: la caída de la demanda mundial. Consecuencias a corto plazo: desempleo; a largo plazo: apoyo del Estado a la industria.")
build(
    O, 2, F2,
    use="Hoy aprendo las palabras para explicar procesos con varias causas: causa de fondo, causa inmediata, consecuencias a corto y largo plazo.",
    prior=["Sé que un hecho tiene varias causas.", "Conozco las cuatro dimensiones.", "Distingo entre causa y consecuencia."],
    explain=[
        "Para explicar con claridad conviene ordenar las causas. Una causa de fondo es una situación que existe desde hace tiempo y prepara el hecho; una causa inmediata es la que lo desencadena. Piensa en una gotera: el techo viejo es la causa de fondo y la lluvia fuerte es la inmediata.",
        "Las consecuencias también se ordenan. Las de corto plazo aparecen rápido (por ejemplo, desempleo después de una crisis) y las de largo plazo se notan años después (por ejemplo, nuevas políticas del Estado). Un proceso tiene además varias dimensiones: política, económica, social y medioambiental.",
        "Por último, los actores (trabajadores, empresarios, mujeres, pueblos indígenas, el Estado) pueden ver el mismo proceso de modos distintos. Por eso explicar bien incluye distintas perspectivas, no solo una.",
    ],
    vocab=[("causa de fondo", "situación antigua que prepara un hecho"), ("causa inmediata", "hecho que desencadena el proceso"), ("consecuencia a corto plazo", "efecto que aparece rápido"), ("consecuencia a largo plazo", "efecto que se nota años después"), ("multidimensionalidad", "idea de que un proceso se mira desde varias dimensiones")],
    worked=[
        ("De fondo o inmediata", "{F} Clasifica «la caída de la demanda mundial».", ["La ficha la presenta como lo que desencadenó la crisis para Chile.", "Lo que desencadena es la causa inmediata."], "Causa inmediata"),
        ("Corto o largo plazo", "{F} Clasifica «apoyo del Estado a la industria».", ["Ocurrió después de años, con la CORFO en 1939.", "Los efectos que aparecen años después son de largo plazo."], "Consecuencia a largo plazo"),
    ],
    mistakes=[("Llamar «causa» a cualquier cosa que se mencione en el texto.", "Hay que decidir si algo vino antes y ayudó a producir el hecho.", "Pregunta: ¿esto preparó el hecho o fue un efecto posterior?"),
              ("Poner todas las causas al mismo nivel, sin distinguir fondo de inmediata.", "Se pierde la idea de qué estaba preparado desde antes y qué lo detonó.", "Anota «de fondo» o «inmediata» al lado de cada causa.")],
    T=[
        ("abc", "{F} ¿Qué reducción ocurrió hacia 1930 según la ficha?", "Las ventas de salitre y cobre al exterior", "La población de las ciudades", "El número de escuelas", "La ficha lo indica en su primera frase."),
        ("ab", "En HGCS: ¿qué es una causa de fondo?", "Una situación antigua que prepara el hecho", "El efecto que viene al final", "La de fondo existe desde antes y prepara el cambio."),
        ("abc", "{F} ¿Qué hecho de la ficha fue una respuesta del Estado después de la crisis?", "La creación de la CORFO", "La caída de la demanda mundial", "La dependencia de pocas exportaciones", "La ficha dice que el Estado impulsó la industria y creó la CORFO."),
        ("abc", "{F} ¿Cuál es una consecuencia a corto plazo?", "El desempleo", "La creación de la CORFO en 1939", "La dependencia de pocas exportaciones", "El desempleo aparece rápido, tras la caída de ventas."),
        ("ab", "{F} La creación de la CORFO ocurrió en:", "1939", "1830", "La ficha dice que se creó en 1939."),
        ("abc", "{F} ¿A qué dimensión corresponde principalmente «muchas personas perdieron su trabajo»?", "A la social y la económica", "A la medioambiental", "A ninguna", "Habla de empleo y de cómo vivían las familias."),
        ("=", "Dato de ejemplo: una mina empleaba 1.200 personas antes de la crisis y 450 después. ¿Cuántas personas dejaron de trabajar?", "1200-450", "Se resta lo que quedó a lo que había para ver cuántos empleos se perdieron.", " personas"),
        ("abc", "{F} Una persona dice: «La dependencia de pocas exportaciones es la causa inmediata». ¿Qué respuesta es correcta?", "Es una causa de fondo, porque era una situación de larga duración", "Tiene razón, es inmediata", "No es ninguna causa", "Es una condición previa, no el detonante."),
        ("abc", "{F} Un titular de ejemplo dice «Cerró la mina por la crisis mundial». ¿Qué tipo de causa identifica?", "Una causa inmediata", "Una causa de fondo", "Una consecuencia a largo plazo", "La crisis mundial desencadenó el cierre."),
        ("ab", "{F} Para explicar la crisis, ¿qué conviene mencionar además del desempleo?", "La causa de fondo y la inmediata", "Solo la fecha", "Una explicación completa distingue causas y consecuencias."),
        ("abc", "{F} ¿Qué perspectiva falta para entender cómo vivieron la crisis las familias mineras?", "La de las propias familias trabajadoras", "La de un banco extranjero", "La de un ministerio", "Las familias vivieron el proceso en carne propia."),
        ("abc", "{F} ¿Cuál es una buena frase que ordene causas y consecuencias?", "La economía dependía de pocas exportaciones; cuando cayó la demanda mundial hubo desempleo y después el Estado apoyó la industria", "Hubo desempleo porque sí", "La CORFO causó la crisis", "Ordena fondo, inmediata, corto y largo plazo."),
        ("abc", "{F} ¿Qué error tiene esta frase: «La CORFO causó la crisis de 1930»?", "Presenta como causa algo que ocurrió después", "Nombra la CORFO", "Usa una fecha", "La CORFO se creó en 1939, después de la crisis."),
    ],
    ctx=("abc", "En una charla de un centro de capacitación laboral se explica por qué cerró una fábrica de ejemplo: la máquina estaba obsoleta desde hace años y un día se rompió y no hubo repuestos. ¿Cuál es la causa inmediata?", "La rotura de la máquina sin repuestos", "La máquina obsoleta desde hace años", "El cierre de la fábrica", "Lo que desencadena el cierre es la rotura; la obsolescencia es de fondo."),
    sc=[("¿Qué es una causa inmediata?", "El hecho que desencadena el proceso", "Es lo que detona el cambio."),
        ("En HGCS: ¿Qué es una consecuencia a largo plazo?", "Un efecto que se nota años después", "Se ve con el paso del tiempo."),
        ("En HGCS: ¿qué es multidimensionalidad?", "Mirar un proceso desde varias dimensiones", "Incluye lo político, económico, social y medioambiental.")],
    op=("Ficha de ejemplo: «Una ciudad de ejemplo creció mucho entre 1930 y 1950. Antes, hubo años de mala cosecha en el campo. Un año se abrió una gran fábrica. Después la ciudad tuvo falta de viviendas.» "
        "Clasifica cada hecho en causa de fondo, causa inmediata o consecuencia, y explica en dos frases el crecimiento.",
        "Mala cosecha en el campo: causa de fondo. Apertura de la fábrica: causa inmediata. Falta de viviendas: consecuencia. Explicación: la ciudad creció porque había problemas en el campo y se abrió una fábrica; después faltaron viviendas.",
        ["clasifica los tres hechos", "escribe una explicación con causas y consecuencia", "no confunde antes y después"],
        ["una lista de tres clasificaciones y dos frases"], ["llamar causa a la falta de viviendas", "no distinguir fondo e inmediata"],
        "Pregunta: «¿Esto estaba preparado desde antes o lo desencadenó?»."),
    reinforce="Piensa en una cuenta del hogar que subió y separa una causa de fondo y una inmediata.",
    extend="Explica con un ejemplo la diferencia entre consecuencia a corto y a largo plazo.",
)

# ======================================================= clase 3
F3 = ("Ficha 3 (de ejemplo). Pregunta: «¿Por qué creció tanto la ciudad de Villa Norte (ficticia) entre 1900 y 1930 y qué efectos tuvo?» "
      "Datos de ejemplo: población en 1900, 20.000 personas; en 1930, 50.000. "
      "Fuente A (trabajadora, relato de ejemplo): «Vine del campo porque en la fábrica pagaban un sueldo cada semana; vivimos seis personas en una pieza.» "
      "Fuente B (dueño de una fábrica, nota de ejemplo): «La ciudad progresa gracias a las industrias y al ferrocarril.» "
      "Fuente C (profesora, carta de ejemplo): «Se abrió una escuela nueva, pero faltan salas porque llegan más familias de las que caben.»")
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a explicar un proceso con varias causas, dimensiones y perspectivas usando una pregunta y una tabla.",
    prior=["Distingo causa de fondo e inmediata.", "Sé qué es una dimensión.", "Comparo fuentes de distintos actores."],
    explain=[
        "Para explicar un proceso con orden puedes seguir seis pasos. Paso 1: escribe la pregunta. Paso 2: lista las causas que aparecen en las fuentes. Paso 3: clasifica cada causa por dimensión (política, económica, social o medioambiental). Paso 4: marca cuáles son de fondo y cuáles inmediatas. Paso 5: anota las consecuencias, a corto y largo plazo. Paso 6: redacta la explicación y cita la fuente.",
        "En el caso de Villa Norte, las fuentes muestran distintas perspectivas: una trabajadora habla del sueldo y la vivienda, un empresario del progreso y una profesora de la escuela. Cada una ve una parte. Al reunirlas, la explicación gana en precisión y en justicia con los distintos actores.",
        "Recuerda ser honesto al explicar: indica de qué fuente sale cada dato y reconoce cuando algo no se puede saber con los textos disponibles.",
    ],
    vocab=[("pregunta guía", "pregunta que ordena la explicación"), ("clasificar", "ordenar según un criterio"), ("citar", "indicar de qué fuente sale un dato"), ("progreso", "avance material; no todos lo viven igual"), ("hacinamiento", "muchas personas viviendo en un espacio muy pequeño")],
    worked=[
        ("Listar y clasificar", "{F} Escribe dos causas y su dimensión.", ["De A: sueldo semanal en la fábrica, económica.", "De B: ferrocarril e industrias, económica."], "Sueldo semanal (económica) y ferrocarril e industrias (económica)"),
        ("Consecuencias", "{F} Escribe una consecuencia con su fuente y su plazo.", ["En A: seis personas en una pieza, hacinamiento.", "Aparece rápido con la llegada de familias: corto plazo."], "Hacinamiento en la vivienda (fuente A), corto plazo"),
    ],
    mistakes=[("Escribir la explicación sin indicar de qué fuente sale cada dato.", "Nadie puede comprobar de dónde viene lo que se afirma.", "Pon la letra de la fuente entre paréntesis después de cada dato."),
              ("Quedarse con la perspectiva del empresario porque suena «oficial».", "El texto B solo muestra una mirada sobre el crecimiento.", "Incluye también lo que cuentan la trabajadora y la profesora.")],
    T=[
        ("abc", "{F} ¿Qué pregunta guía plantea la ficha?", "Por qué creció tanto Villa Norte y qué efectos tuvo", "Cuántas escuelas había", "Cuál era la mejor fábrica", "Está escrita al comienzo de la ficha."),
        ("{F} ¿Cuántas personas había en 1930 en Villa Norte, según los datos?", "50.000", "Los datos de la ficha lo indican."),
        ("abc", "{F} ¿Qué fuente habla de la falta de salas en la escuela?", "La fuente C", "La fuente A", "La fuente B", "La profesora escribe sobre las salas."),
        ("abc", "{F} ¿Qué dimensión muestra «vivimos seis personas en una pieza»?", "La social", "La política", "La medioambiental", "Habla de condiciones de vida de las personas."),
        ("ab", "{F} ¿Qué actor habla del progreso?", "El dueño de una fábrica", "La profesora", "La nota del empresario destaca industrias y ferrocarril."),
        ("abc", "{F} ¿Qué paso del método consiste en marcar causas de fondo e inmediatas?", "El paso 4", "El paso 1", "El paso 6", "Es el paso en que se jerarquizan las causas."),
        ("=", "{F} ¿Cuántas personas más había en 1930 que en 1900?", "50000-20000", "Se restan las dos poblaciones para ver el aumento total.", " personas"),
        ("=", "{F} Si las seis personas de una pieza ocupan 12 metros cuadrados (dato de ejemplo), ¿cuántos metros cuadrados corresponden a cada persona?", "12/6", "Se divide el espacio total entre las personas.", " metros cuadrados"),
        ("abc", "{F} ¿Qué efecto social se vincula con el aumento de población según A y C?", "Hacinamiento y falta de salas escolares", "Más espacio en las casas", "Sobran escuelas", "Ambas fuentes señalan falta de espacio por la llegada de familias."),
        ("abc", "{F} Una compañera dice: «El crecimiento fue solo progreso». ¿Qué respuesta es más completa?", "Para B fue progreso, pero A y C muestran problemas de vivienda y escuela", "Tiene razón porque lo dice B", "Fue solo un problema", "Incluye varias perspectivas con datos tomados de las fuentes."),
        ("ab", "{F} Para citar bien el dato del sueldo semanal, ¿cómo conviene escribir?", "«Había sueldo semanal en la fábrica (fuente A)»", "«Se sabe que había sueldos»", "Citar significa indicar de qué fuente sale el dato."),
        ("abc", "{F} ¿Qué información falta para saber cuánto cambió el nivel de vida?", "Datos de sueldos y precios de esa época", "Más adjetivos", "Un dibujo de la fábrica", "Con los textos no se puede medir ese cambio."),
        ("abc", "{F} ¿Cuál es una explicación bien redactada?", "Villa Norte creció porque la industria y el ferrocarril atrajeron trabajadores (B, A); esto causó hacinamiento y falta de salas (A, C)", "Villa Norte creció porque sí", "Solo hubo progreso", "Cita fuentes y une causas con consecuencias."),
    ],
    ctx=("abc", "Una junta de vecinos quiere explicar a los nuevos vecinos por qué el barrio creció tanto. Tienen un aviso de ejemplo de una inmobiliaria, el relato de una dirigente y un dato de población. ¿Cuál es el primer paso del método?", "Escribir la pregunta guía", "Redactar la conclusión", "Elegir la fuente más bonita", "El método parte de una pregunta clara."),
    sc=[("¿Cuál es el primer paso para explicar un proceso?", "Escribir la pregunta", "La pregunta ordena todo el trabajo."),
        ("¿Para qué se cita la fuente?", "Para que se pueda comprobar de dónde sale el dato", "Citar ayuda a ser honesto y verificable."),
        ("¿Qué es el hacinamiento?", "Muchas personas viviendo en un espacio muy pequeño", "Es una consecuencia de la falta de viviendas.")],
    op=("Pregunta de ejemplo: «¿Por qué se abrieron escuelas nocturnas para trabajadores en una ciudad de ejemplo en 1925?». Fuentes de ejemplo: a) aviso de un sindicato: ‘Pedimos escuelas de noche porque trabajamos de día’. "
        "b) nota de una empresa: ‘Los obreros que saben leer cometen menos errores’. c) carta de una profesora: ‘Hay mucha gente adulta que quiere aprender’. "
        "Lista las causas, clasifícalas por dimensión y redacta una explicación de tres líneas citando las fuentes.",
        "Causas: trabajan de día (a, social y económica); mayor utilidad para la empresa (b, económica); adultos con ganas de aprender (c, social). Explicación: se abrieron escuelas nocturnas porque los trabajadores solo podían estudiar de noche (a), la empresa vio ventajas (b) y había interés de la gente adulta (c).",
        ["lista causas tomadas de las fuentes", "clasifica por dimensión", "cita la fuente en la explicación"],
        ["una lista de causas con dimensión y una explicación de tres líneas"], ["no citar", "inventar causas"],
        "Pregunta: «¿De qué fuente sale cada afirmación?»."),
    reinforce="Escribe una pregunta guía sobre un cambio en tu barrio y lista dos causas con su dimensión.",
    extend="Explica por qué conviene incluir en una explicación las voces de actores que no tuvieron mucho poder.",
)

# ======================================================= clase 4
F4 = ("Ficha 4 (de ejemplo). Pregunta: «¿Por qué el Estado ocupó la Araucanía en la segunda mitad del siglo XIX?» Cinco textos inventados. "
      "1) Informe de un ministerio (de ejemplo): «Se necesitan tierras para sembrar trigo y vender más al exterior.» "
      "2) Discurso de un parlamentario (de ejemplo): «El Estado debe tener autoridad en todo su territorio.» "
      "3) Artículo de un diario (de ejemplo): «Hay que llevar el progreso y la civilización a esas tierras.» "
      "4) Relato de una comunidad mapuche (de ejemplo): «Defendimos nuestro territorio y nuestra forma de vivir.» "
      "5) Nota de un viajero (de ejemplo): «El bosque del sur fue talado en grandes extensiones tras la llegada de colonos.»")
build(
    O, 4, F4,
    use="Hoy practico con apoyo la explicación de un proceso complejo: clasifico causas por dimensión, distingo perspectivas y señalo consecuencias.",
    prior=["Uso los seis pasos para explicar.", "Distingo causa de fondo e inmediata.", "Sé que cada actor mira el proceso de forma distinta."],
    explain=[
        "La ocupación de la Araucanía fue un proceso que se desarrolló en la segunda mitad del siglo XIX. Participaron el Estado, familias colonas y el pueblo mapuche, que perdió gran parte de sus tierras. Se explica por varias causas a la vez: económicas (tierras para sembrar y vender), políticas (extender la autoridad del Estado) y de ideas de la época (la creencia de algunos de que había que «civilizar»). Hoy esa idea es muy cuestionada.",
        "Para practicar, ordena en una tabla: la causa, la fuente, la dimensión y el actor que la plantea. Luego marca qué perspectiva falta. Aquí, la voz de la comunidad mapuche no habla de causas del Estado, sino de lo que se defendía; eso también es parte de la explicación.",
        "Explicar con empatía y respeto es dar espacio a todos los actores sin repetir sus ideas como si fueran nuestras. Podemos decir «según el informe del ministerio…» y no «la tierra estaba vacía».",
    ],
    vocab=[("ocupación", "toma de control de un territorio por parte de un Estado u otro grupo"), ("colonizar", "enviar familias a poblar un territorio"), ("exportar", "vender productos a otros países"), ("autoridad", "poder reconocido para tomar decisiones"), ("territorio", "espacio que un grupo habita y usa")],
    worked=[
        ("Causa y dimensión", "{F} Clasifica la causa del texto 1.", ["El texto 1 habla de sembrar trigo y vender más al exterior.", "Es una razón de producción y comercio."], "Causa económica"),
        ("Qué perspectiva aporta", "{F} ¿Qué aporta el texto 4?", ["El texto 4 es el relato de la comunidad mapuche.", "Muestra lo que ellos defendían: su territorio y su forma de vivir."], "La perspectiva de la comunidad, que defendía su territorio"),
    ],
    mistakes=[("Repetir como verdad las ideas de la época, por ejemplo que esas tierras «estaban vacías».", "Había personas y comunidades viviendo allí.", "Atribuye la idea al autor: «según el informe…»."),
              ("Explicar solo con las causas que dio el Estado.", "Faltan otras voces que muestran por qué el proceso fue tan conflictivo.", "Incluye la perspectiva de la comunidad y las consecuencias para ella.")],
    T=[
        ("abc", "{F} ¿Cuál es la pregunta de la ficha?", "Por qué el Estado ocupó la Araucanía en la segunda mitad del siglo XIX", "Cuánto trigo se vendió", "Quién ganó una elección", "Es la pregunta guía de la ficha."),
        ("abc", "{F} ¿Quién escribe el texto 4?", "Una comunidad mapuche", "Un ministerio", "Un viajero", "El relato es de la comunidad."),
        ("ab", "En HGCS: ¿qué es exportar?", "Vender productos a otros países", "Comprar productos de otros países", "Exportar es enviar mercancías al exterior para venderlas."),
        ("abc", "{F} ¿Qué causa política aparece en la ficha?", "Que el Estado debe tener autoridad en todo su territorio", "Que hacía falta trigo", "Que el bosque era hermoso", "El texto 2 habla del poder del Estado."),
        ("abc", "{F} ¿Qué idea de la época aparece en el texto 3?", "Llevar el progreso y la civilización", "Proteger el bosque", "Pagar impuestos", "El diario sostiene esa idea, hoy muy cuestionada."),
        ("ab", "{F} ¿Qué efecto medioambiental menciona el texto 5?", "La tala de grandes extensiones del bosque del sur", "La creación de un parque", "El viajero describe un cambio en el paisaje por la tala."),
        ("=", "Dato de ejemplo: una comunidad usaba 600 hectáreas antes de la ocupación y 90 después. ¿Qué porcentaje de su terreno conservó?", "90/600*100", "Se divide el terreno que quedó entre el original y se multiplica por cien.", " %"),
        ("abc", "{F} ¿Qué dimensión muestra mejor el texto 2?", "La política", "La medioambiental", "La económica", "El texto habla de autoridad del Estado en su territorio."),
        ("abc", "{F} Una persona dice: «Según el texto 3, esas tierras estaban vacías». ¿Qué falla?", "El texto 3 no dice eso y, además, la comunidad vivía allí", "Está bien porque el diario lo dice", "No hay ningún error", "Hay que citar lo que el texto dice y recordar a la comunidad."),
        ("abc", "{F} ¿Cuál es una explicación que combina varias dimensiones?", "El Estado buscó tierras para producir y autoridad en su territorio, y se defendió una forma de vida, con efectos en el bosque", "Todo ocurrió por un solo motivo", "Fue solo por el bosque", "Reúne lo económico, lo político, lo social y lo ambiental."),
        ("ab", "{F} ¿Qué perspectiva falta para entender las consecuencias para las mujeres de esas comunidades?", "El relato de una mujer de esas comunidades", "Otro informe oficial", "Las consecuencias para ellas no aparecen en los cinco textos."),
        ("abc", "{F} ¿Cómo se debe citar la idea del texto 3?", "«Según un artículo de un diario de ejemplo, había que llevar el progreso»", "«Todos pensaban así»", "«Es la verdad»", "Citar la fuente evita presentar una idea como verdad general."),
        ("abc", "{F} ¿Qué consecuencia de largo plazo es razonable señalar con los textos 4 y 5?", "Cambios duraderos en el territorio y en la vida de las comunidades", "El fin de todas las exportaciones", "Que el Estado no tuvo autoridad", "El texto 5 muestra un cambio en el bosque y el 4 la defensa del territorio: son cambios que se prolongan en el tiempo."),
    ],
    ctx=("abc", "En un centro cultural, una persona explica a los visitantes que «el Estado ocupó la Araucanía solo por patriotismo». ¿Qué le pueden preguntar para ampliar la explicación?", "¿Qué otras razones aparecen, como las económicas y las ideas de la época?", "¿Por qué no usa dibujos?", "¿Cuántas palabras tiene su frase?", "Una explicación completa incorpora varias causas."),
    sc=[("¿Qué es colonizar?", "Enviar familias a poblar un territorio", "Se asocia a la ocupación y poblamiento de tierras."),
        ("¿Qué causas económicas aparecen en la ficha?", "Tierras para sembrar y vender más al exterior", "Se refiere a producción y comercio."),
        ("¿Por qué incluir la voz de la comunidad?", "Porque vivía en el territorio y vio el proceso desde otro lugar", "Su perspectiva completa la explicación de todo el proceso.")],
    op=("Pregunta de ejemplo: «¿Por qué el pueblo mapuche perdió gran parte de sus tierras?». Fuentes de ejemplo: a) informe de una oficina de tierras: ‘Se entregaron terrenos menores a las comunidades’. b) relato de una comunidad: ‘Se llevaron a nuestras familias a terrenos pequeños’. c) artículo de una historiadora: ‘Hubo razones económicas y políticas, y la fuerza militar’. "
        "Haz una tabla con causa, fuente, dimensión y actor, y escribe una explicación de cuatro líneas que cite las fuentes.",
        "Causas: reducción de terrenos (a, política y económica); traslado de familias (b, social); razones económicas y políticas más fuerza militar (c). Explicación: la comunidad perdió tierras porque el Estado entregó terrenos menores (a), muchas familias fueron trasladadas (b) y hubo razones económicas y políticas (c).",
        ["completa la tabla con datos de los textos", "cita las fuentes", "incluye la perspectiva de la comunidad"],
        ["una tabla de tres filas y una explicación de cuatro líneas"], ["no citar", "inventar causas"],
        "Pregunta: «¿Qué actor falta y qué dimensión no mencioné?»."),
    reinforce="Elige una causa de la ficha y escribe una pregunta que le harías a ese autor.",
    extend="Explica por qué una explicación completa no justifica ni condena automáticamente, sino que muestra causas, actores y efectos.",
)

# ======================================================= clase 5
F5 = ("Ficha 5 (de ejemplo). Pregunta: «¿Por qué se reconoció el voto de las mujeres en todas las elecciones en 1949 y no antes?» (En 1934 una ley les permitió votar en elecciones municipales.) Textos inventados. "
      "A) Informe de una asociación de mujeres (de ejemplo): «Desde hace décadas las mujeres estudian, trabajan en fábricas y oficinas y se organizan; es injusto que no voten.» "
      "B) Nota de un periódico (de ejemplo): «En otros países las mujeres ya votan, y el tema se discute en nuestro Congreso.» "
      "C) Discurso de un parlamentario contrario (de ejemplo): «No hay apuro; la política es cosa de hombres.» "
      "D) Carta de una obrera (de ejemplo): «Trabajo y sostengo mi casa; mi opinión también cuenta.»")
build(
    O, 5, F5,
    use="Hoy aplico la explicación multicausal y multidimensional a otro proceso, el voto de las mujeres, con distintas perspectivas.",
    prior=["Uso los seis pasos para explicar.", "Distingo causas de fondo e inmediatas.", "Sé que hay perspectivas a favor y en contra."],
    explain=[
        "El voto de las mujeres se reconoció en etapas: en 1934 en elecciones municipales y en 1949 en todas las elecciones. Para explicarlo hay que combinar causas. De fondo: más mujeres estudiaban y trabajaban fuera del hogar, y se organizaban en asociaciones. Inmediatas: la presión de esas organizaciones y el debate en el Congreso. También influyó que en otros países las mujeres ya votaban.",
        "Las dimensiones se mezclan: política (leyes y derechos), social (cambios en la vida de las mujeres), económica (su trabajo remunerado) y de ideas de la época (lo que se pensaba que podía hacer una mujer). Hubo perspectivas opuestas, como la de quienes decían que la política era «cosa de hombres».",
        "Al comunicar tu explicación, usa conectores como «porque», «por eso», «como consecuencia» y «sin embargo». Ayudan a que se entienda qué causa produjo qué efecto y qué perspectiva se compara con cuál.",
    ],
    vocab=[("conector", "palabra que une ideas, como «porque» o «por eso»"), ("remunerado", "que se paga con un sueldo"), ("derecho político", "derecho a participar en las decisiones del país"), ("organización", "grupo que actúa en conjunto"), ("etapa", "parte de un proceso que ocurre en un momento")],
    worked=[
        ("Causa de fondo", "{F} Clasifica la causa «las mujeres estudian y trabajan fuera del hogar».", ["Es un cambio que venía ocurriendo desde hacía décadas.", "Un cambio previo que prepara el hecho es una causa de fondo."], "Causa de fondo, social y económica"),
        ("Un conector", "{F} Escribe una frase con «por eso» que una causa y una consecuencia.", ["Causa: las mujeres se organizaron y presionaron.", "Consecuencia: se reconoció su voto."], "Las mujeres se organizaron y presionaron; por eso se reconoció su voto"),
    ],
    mistakes=[("Explicar el voto solo como un «regalo» del Congreso.", "Se olvida la organización y la presión de las propias mujeres.", "Nombra a las asociaciones y a las trabajadoras como actoras."),
              ("Usar «porque» para unir hechos que no tienen relación.", "Se inventa una causa que las fuentes no muestran.", "Comprueba en la fuente que la relación existe.")],
    T=[
        ("abc", "{F} ¿Qué ley se reconoció en 1934 según la ficha?", "El voto de las mujeres en elecciones municipales", "El voto en todas las elecciones", "El derecho a estudiar", "La ficha lo indica entre paréntesis."),
        ("abc", "{F} ¿Quién escribe la fuente D?", "Una obrera", "Un parlamentario", "Un periodista", "Es una carta de ejemplo de una obrera."),
        ("ab", "En HGCS: ¿qué es un conector?", "Una palabra que une ideas, como «por eso»", "Un número que mide años", "Los conectores ordenan la explicación y muestran relaciones."),
        ("abc", "{F} ¿Qué dice la fuente A que es injusto?", "Que las mujeres no voten", "Que las mujeres trabajen", "Que existan fábricas", "El texto lo dice al final de la frase."),
        ("abc", "{F} ¿Qué argumento da el texto B?", "Que en otros países las mujeres ya votan", "Que no hay elecciones", "Que las mujeres no quieren votar", "El texto lo dice expresamente en sus palabras."),
        ("abc", "{F} ¿Qué opina el parlamentario de C?", "Que no hay apuro y que la política es cosa de hombres", "Que hay que votar ya", "Que se discutirá mañana", "Lo dice expresamente en su discurso."),
        ("=", "Dato de ejemplo: una fábrica tenía 800 trabajadoras y 200 trabajadores. ¿Qué porcentaje del total eran mujeres?", "800/1000*100", "Se divide el número de mujeres entre el total y se multiplica por cien.", " %"),
        ("abc", "{F} ¿Qué dimensión muestra principalmente D?", "La económica y la social", "La medioambiental", "Ninguna", "Habla de trabajo, de sostener su hogar y de opinión."),
        ("abc", "{F} ¿Cuál es una consecuencia de largo plazo del voto femenino?", "Las mujeres pudieron participar en todas las elecciones", "Se cerró el Congreso", "Se prohibieron las asociaciones", "Es un efecto duradero de la ley de 1949."),
        ("abc", "{F} Alguien dice: «El voto se reconoció solo porque otros países lo hicieron». ¿Qué respuesta es más completa?", "Influyó eso, pero también el estudio, el trabajo y la organización de las mujeres", "Tiene toda la razón", "Nada de eso influyó", "La respuesta correcta combina varias causas que se influyen."),
        ("ab", "{F} ¿Qué conector sirve para expresar oposición entre A y C?", "«Sin embargo»", "«Por eso»", "Oposición se expresa con «sin embargo»."),
        ("abc", "{F} ¿Cuál es una explicación bien construida?", "Las mujeres estudiaban, trabajaban y se organizaron (A, D); por eso su demanda creció, y aunque hubo oposición (C), se reconoció su voto en 1949", "Hubo una ley y listo", "Solo importa el parlamentario", "Cita fuentes y une causas y consecuencias."),
        ("abc", "{F} ¿Qué falta para tener una visión más completa?", "La perspectiva de mujeres del campo y de pueblos indígenas", "Otra opinión como la de C", "Un listado de fechas", "Se necesitan voces diversas para completar la visión."),
    ],
    ctx=("abc", "En una asamblea de una organización de mujeres, alguien dice: «El derecho a voto fue simplemente concedido». ¿Cómo se puede completar esa explicación con respeto?", "Agregando que muchas mujeres se organizaron y lo pidieron durante años", "Diciendo que no importa cómo ocurrió", "Callando la discusión", "Se amplía la explicación con otras causas."),
    sc=[("¿Qué conectores ayudan a explicar causas?", "«Porque», «por eso» y «como consecuencia»", "Estas palabras unen las causas con sus efectos."),
        ("¿En qué años hubo voto municipal y voto en todas las elecciones?", "1934 y 1949", "Son las dos etapas mencionadas en la ficha."),
        ("¿Qué actores aparecen en la explicación?", "Mujeres organizadas, trabajadoras, parlamentarios y prensa", "Hay distintas perspectivas sobre el mismo proceso.")],
    op=("Pregunta de ejemplo: «¿Por qué las mujeres empezaron a estudiar en las universidades?». Fuentes de ejemplo: a) decreto de 1877: permite a las mujeres rendir exámenes de ingreso a la universidad. "
        "b) carta de una joven: ‘Mi profesora me animó a seguir’. c) editorial: ‘La nación necesita ciudadanas instruidas’. d) carta de un lector opuesto: ‘Se apartarán de sus deberes’. "
        "Escribe una explicación de cinco líneas con al menos dos causas, dos perspectivas y un conector de oposición.",
        "El decreto de 1877 abrió el camino (a); una joven fue animada por su profesora (b) y algunos pensaban que el país necesitaba ciudadanas instruidas (c); sin embargo, otros temían que se apartaran del hogar (d).",
        ["incluye al menos dos causas", "muestra dos perspectivas", "usa un conector de oposición"],
        ["una explicación de cinco líneas"], ["dar una sola mirada", "no citar fuentes"],
        "Pregunta: «¿Qué conector uso para mostrar que dos perspectivas se oponen?»."),
    reinforce="Escribe una frase con «por eso» sobre un cambio que haya visto tu familia o tu comunidad, sin dar datos personales.",
    extend="Explica por qué una explicación con perspectivas opuestas es más precisa que una con una sola voz.",
)

# ======================================================= clase 6
F6 = ("Ficha 6 (de ejemplo). Pregunta: «¿Por qué cambió la vida de las mujeres entre 1900 y 1950?» Un borrador inventado de una estudiante: «La vida de las mujeres cambió porque salieron a trabajar. Antes no hacían nada. Después votaron y todo fue mejor.» "
      "Criterios de una buena explicación (de ejemplo): 1) indica varias causas; 2) usa más de una dimensión; 3) distingue fondo de inmediata; 4) incluye una perspectiva distinta; 5) cita la fuente; 6) reconoce lo que no se sabe. "
      "Datos que la estudiante tenía: decreto de 1877 sobre estudios universitarios; ley de 1934 sobre voto municipal; ley de 1949 sobre voto en todas las elecciones; carta de una obrera que trabaja en una fábrica; discurso de un parlamentario contrario al voto.")
build(
    O, 6, F6,
    use="Hoy reviso una explicación, la evalúo con criterios, la mejoro y decido cómo comunicarla con honestidad.",
    prior=["Uso los seis pasos para explicar.", "Distingo causas, consecuencias y perspectivas.", "Cito fuentes."],
    explain=[
        "Revisar una explicación es compararla con criterios. Una buena explicación indica varias causas, usa más de una dimensión, distingue causas de fondo e inmediatas, incluye distintas perspectivas, cita las fuentes y reconoce los límites de lo que se sabe. Si falta alguno, se corrige antes de comunicarla.",
        "Corregir no es «tachar» a la persona. Se pregunta qué funciona (por ejemplo, que nombra el trabajo de las mujeres) y qué se puede mejorar (por ejemplo, que usa palabras exageradas como «antes no hacían nada»). Cuando una frase absoluta se contradice con una fuente, se cambia por una frase precisa.",
        "Comunicar con honestidad es mostrar qué fuentes se usaron y qué no se sabe, y asumir que una explicación puede mejorar con nuevas fuentes. Esa responsabilidad forma parte de aprender historia.",
    ],
    vocab=[("criterio", "regla para evaluar un trabajo"), ("exagerar", "decir más de lo que muestran los datos"), ("precisar", "hacer una frase más exacta"), ("honestidad", "decir la verdad sobre lo que se sabe y lo que no"), ("borrador", "primer texto que se puede mejorar")],
    worked=[
        ("Evaluar con un criterio", "{F} ¿Cumple el borrador el criterio 5 (cita la fuente)?", ["El borrador no menciona ninguna fuente.", "No dice de dónde sale ningún dato."], "No cumple: falta citar fuentes"),
        ("Precisar una frase", "{F} Reescribe «antes no hacían nada» de forma más exacta.", ["Esa frase exagera: las mujeres ya realizaban muchas tareas.", "Se puede decir que tenían pocos derechos y oportunidades de estudio y de voto."], "Antes de 1877 las mujeres tenían pocas oportunidades de estudio y no votaban"),
    ],
    mistakes=[("Corregir solo la ortografía y no el contenido.", "La explicación puede estar bien escrita y aun así ser incompleta.", "Revisa primero los criterios y luego la redacción."),
              ("Usar frases absolutas como «todo fue mejor».", "Los procesos tienen ventajas y límites según el actor.", "Cambia «todo» por datos precisos y por quién fue favorecido.")],
    T=[
        ("abc", "{F} ¿Cuántos criterios tiene la lista de la ficha?", "Seis", "Cuatro", "Ocho", "La ficha los enumera del 1 al 6."),
        ("abc", "{F} ¿Qué dice el borrador sobre el voto?", "Que después votaron y todo fue mejor", "Que votaron solo en 1900", "Que nunca votaron", "Es lo que escribe la estudiante."),
        ("ab", "En HGCS: ¿qué es exagerar?", "Decir más de lo que muestran los datos", "Citar una fuente", "Una frase exagerada va más allá de la evidencia."),
        ("abc", "{F} ¿Qué criterio incumple «Antes no hacían nada»?", "Ser precisa y no exagerar", "Usar conectores", "Escribir un título", "La frase afirma algo falso y absoluto."),
        ("ab", "{F} ¿Qué dato de la ficha corrige mejor la idea de que «todo fue mejor»?", "El discurso de un parlamentario contrario al voto, que muestra oposición", "La fecha 1949", "Muestra que no todos apoyaban el cambio."),
        ("abc", "{F} ¿Qué dimensión del proceso aparece en el borrador?", "La económica, al mencionar el trabajo", "La medioambiental", "Ninguna", "El borrador habla de salir a trabajar por un pago."),
        ("=", "{F} ¿Cuántos años pasaron entre el decreto de 1877 y la ley de 1949?", "1949-1877", "Se restan las dos fechas para saber el tiempo entre ambas.", " años"),
        ("abc", "{F} ¿Cuál es una frase mejorada para «Después votaron y todo fue mejor»?", "Desde 1949 las mujeres pudieron votar en todas las elecciones, aunque antes hubo oposición (según el parlamentario)", "Votaron y punto", "Votaron todos", "Es precisa y reconoce la oposición."),
        ("abc", "{F} ¿Qué falta en el borrador según el criterio 4?", "Una perspectiva distinta, como la de la obrera o la del parlamentario", "Más adjetivos", "Más signos de exclamación", "Hay datos que no se aprovecharon."),
        ("abc", "{F} Una compañera dice: «No hace falta citar, es obvio». ¿Qué responder con honestidad?", "Citar permite comprobar de dónde sale cada dato", "Tiene razón", "Basta con la intuición", "Sin cita nadie puede verificar de dónde viene el dato."),
        ("ab", "{F} Para el criterio 6, ¿qué se puede escribir?", "«Con estas fuentes no sé cómo vivían las mujeres del campo»", "«Lo sé todo del tema»", "Reconocer límites forma parte de una explicación honesta."),
        ("abc", "{F} ¿Cuál es el mejor plan para mejorar el borrador?", "Agregar causas, citar fuentes, incluir dos perspectivas y precisar frases", "Borrarlo", "Hacerlo más largo sin cambiar el contenido", "Responde a los criterios con acciones concretas."),
        ("abc", "{F} Tras mejorar el borrador, ¿qué decisión posterior es razonable?", "Leerlo a otra persona y pedir que diga qué entendió", "Guardarlo sin leerlo", "Rendirse", "Comunicar permite saber si se entiende."),
    ],
    ctx=("abc", "En un taller de la biblioteca municipal, un participante lee su explicación sobre el proceso de las mujeres y otra persona le pide que cite las fuentes y diga qué no se sabe. ¿Qué valor muestra ese pedido?", "Honestidad y responsabilidad al comunicar", "Ganas de criticar sin motivo", "Desinterés por el tema", "Transparentar fuentes y límites es comunicar con responsabilidad."),
    sc=[("En HGCS: ¿Qué incluye una buena explicación?", "Varias causas, varias dimensiones, perspectivas y fuentes", "Una buena explicación cumple los criterios que se revisaron."),
        ("¿Qué significa precisar una frase?", "Hacerla más exacta según los datos", "Precisar evita exagerar más de lo que dicen las fuentes."),
        ("¿Por qué reconocer lo que no se sabe?", "Porque muestra honestidad y límites de la evidencia", "Ninguna explicación es completa y siempre puede mejorar.")],
    op=("Elige una pregunta de las clases (migración del campo a la ciudad, Araucanía o voto de las mujeres) y escribe una explicación de ocho líneas con: dos causas, dos dimensiones, dos perspectivas, una consecuencia y las fuentes de ejemplo que citas. "
        "Después evalúala con los seis criterios de la ficha y escribe qué mejorarías.",
        "Explicación de ejemplo sobre el voto de las mujeres: causas (estudian y trabajan, se organizan), dimensiones (social y política), perspectivas (asociación y parlamentario), consecuencia (votan en 1949). Autoevaluación: cumple 1, 2, 4, 5; falta el 6, reconocer que no se conoce la perspectiva del campo; mejora: agregar una frase sobre ese vacío.",
        ["cumple los seis criterios o dice cuál le falta", "cita fuentes del cuaderno", "propone una mejora concreta"],
        ["una explicación de ocho líneas y una autoevaluación"], ["no citar fuentes", "exagerar con frases absolutas"],
        "Pregunta: «¿Qué criterio me falta cumplir?»."),
    reinforce="Revisa con los seis criterios una explicación corta que hayas escrito en esta unidad y marca cuál cumples.",
    extend="Explica a otra persona, con tus palabras, qué cambia en una explicación cuando se agregan perspectivas y dimensiones.",
)
