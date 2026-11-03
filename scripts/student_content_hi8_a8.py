"""Material del estudiante de 8.º básico, Historia, Geografía y Ciencias Sociales: OA 08 (ciudad y administración del Imperio español)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI08 OA 08"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (resumen y hitos). Las ciudades españolas de América solían trazarse en damero, es decir, con calles que forman cuadras regulares, alrededor de una Plaza Mayor. "
     "Alrededor de la plaza se ubicaban la iglesia, el cabildo (consejo de la ciudad, con alcaldes y regidores) y la casa del gobernador. "
     "Instituciones del imperio: Casa de Contratación en Sevilla (1503), que controlaba el comercio con América; Consejo de Indias en España (1524), que asesoraba al rey en los asuntos americanos; Virreinato de Nueva España (1535) y Virreinato del Perú (1542), territorios gobernados por un virrey que representaba al rey. "
     "1541: Pedro de Valdivia funda Santiago. 1573: las Ordenanzas de Felipe II fijan reglas para fundar ciudades.")
build(
    OA, 1, F,
    use="Aprenderé a situar la ciudad colonial en el tiempo y el espacio, y a nombrar las instituciones que concentraba y su relación con España.",
    prior=["Conozco el Estado moderno y el mercantilismo.", "Sé calcular diferencias entre años.", "Conozco la conquista de América."],
    explain=[
        "En el Imperio español, la ciudad fue el centro desde el cual se administraba el territorio. Los españoles fundaban ciudades con un trazado en damero alrededor de una Plaza Mayor. Alrededor de la plaza se ubicaban las instituciones principales: la iglesia, el cabildo y la casa del gobernador. Así, desde un solo lugar se ejercían el poder religioso, el político y el judicial.",
        "El cabildo era el consejo de la ciudad, formado por alcaldes y regidores. Por encima estaban autoridades del imperio, como el gobernador o el virrey, que representaba al rey en un virreinato. En España, el Consejo de Indias asesoraba al rey y la Casa de Contratación, en Sevilla, controlaba el comercio con América. Eso se llama monopolio: solo ese camino estaba autorizado.",
        "Una ciudad no vivía aislada. Dependía de sus alrededores, de donde obtenía alimentos y trabajadores, y de la metrópoli, que dictaba leyes y controlaba el comercio. Las ciudades fueron además lugares donde se consolidó el poder local de las elites criollas, es decir, de los españoles nacidos en América.",
    ],
    vocab=[("cabildo", "consejo de una ciudad, formado por alcaldes y regidores"), ("virrey", "autoridad que representaba al rey en un virreinato"), ("metrópoli", "país que gobierna sus colonias, en este caso España"), ("damero", "trazado de ciudad con calles que forman cuadras regulares"), ("criollo", "español nacido en América")],
    worked=[
        ("Calcular un plazo", "Según la ficha, ¿cuántos años pasaron entre la fundación de la Casa de Contratación y la del Consejo de Indias?", ["Busco los años: 1503 y 1524.", "Resto: 1524 − 1503 = 21."], "21 años"),
        ("Identificar una institución", "¿Qué institución de la ficha controlaba el comercio con América desde España?", ["Leo las instituciones.", "La Casa de Contratación, en Sevilla."], "La Casa de Contratación"),
    ],
    mistakes=[("Pensar que las decisiones de la ciudad americana las tomaba directamente el rey desde España.", "Se ignora la existencia de autoridades locales como cabildos y gobernadores.", "Nombra autoridades locales y de la metrópoli."),
              ("Creer que la ciudad funcionaba aislada del territorio.", "Se olvida que dependía de los alrededores y de España.", "Explica de dónde venían alimentos, trabajadores y leyes.")],
    T=[
        ("{F} ¿Qué es un cabildo?", "El consejo de una ciudad, formado por alcaldes y regidores", "La ficha lo define así."),
        ("{F} ¿Qué institución española, creada en 1503, controlaba el comercio con América?", "La Casa de Contratación", "Está en la ficha."),
        ("{F} ¿Quién representaba al rey en un virreinato?", "El virrey", "Así lo dice la ficha."),
        ("=", "{F} ¿Cuántos años pasaron entre la creación del Virreinato de Nueva España y la del Perú?", "1542-1535", "Se resta el primer año al segundo.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la fundación de Santiago y las Ordenanzas de Felipe II?", "1573-1541", "Se restan los dos años.", " años"),
        ("{F} ¿A qué siglo pertenece la fundación del Virreinato de Nueva España en 1535?", "Siglo XVI", "El siglo XVI va de 1501 a 1600."),
        ("{F} Clasifica cada institución según dónde estaba: a) Consejo de Indias, b) cabildo, c) virreinato. Opciones: en España; en América.", "a) en España; b) en América; c) en América", "El Consejo de Indias estaba en España; las otras dos funcionaban en América."),
        ("{F} ¿Por qué la ciudad se llama centro de la administración? A) Porque desde allí se ejercían el poder religioso, político y judicial B) Porque era la ciudad más grande", "A) Porque desde allí se ejercían el poder religioso, político y judicial", "La plaza reunía iglesia, cabildo y casa del gobernador."),
        ("=", "{F} Una línea de tiempo usa 1 cm = 10 años y parte en 1500. ¿A cuántos cm queda 1573?", "(1573-1500)//10", "Se divide la diferencia de años por la escala.", " cm"),
        ("{F} ¿Qué es un monopolio comercial, según la clase?", "Que solo un camino o institución está autorizado para comerciar", "Se explicó con la Casa de Contratación."),
        ("{F} Un compañero dice: «Las ciudades coloniales funcionaban aisladas». ¿Qué dato de la ficha lo contradice?", "Dependían de la metrópoli, que controlaba el comercio y dictaba leyes", "La Casa de Contratación y el Consejo de Indias conectaban a la ciudad con España."),
        ("{F} ¿Qué elementos se ubicaban alrededor de la Plaza Mayor?", "La iglesia, el cabildo y la casa del gobernador", "La ficha lo indica."),
        ("{F} ¿Qué pregunta problema plantea esta clase?", "Qué papel cumplía la ciudad en la administración del Imperio español", "Es el problema del OA."),
    ],
    ctx=("Un guía quiere explicar a visitantes por qué en la Plaza de Armas de Santiago hay tantas instituciones juntas. Con la ficha, ¿qué respondería? {F}", "Porque la ciudad concentraba el poder religioso, político y judicial alrededor de la Plaza Mayor", "La ficha describe ese trazado."),
    sc=[("¿Qué es un criollo?", "Un español nacido en América", "Se definió en el vocabulario."),
        ("¿Qué es la metrópoli?", "El país que gobierna sus colonias, en este caso España", "Se definió en el vocabulario."),
        ("=", "¿Cuántos años pasaron entre 1503 y 1535?", "1535-1503", "Se resta el primer año al segundo.", " años")],
    op=("Dibuja el plano de una ciudad colonial de ejemplo con una plaza central y cuatro calles que se cruzan. Ubica la iglesia, el cabildo y la casa del gobernador alrededor de la plaza. Debajo escribe una frase que explique por qué la plaza era el centro de la administración. {F}",
        "Plaza al centro; iglesia en un lado, cabildo en otro y casa del gobernador en otro; frase: «Allí se reunían los poderes religioso, político y judicial».",
        ["dibuja plaza y calles", "ubica las tres instituciones", "explica por qué era el centro"], ["plano", "frase"], ["no ubicar las instituciones", "decir que la ciudad era aislada"],
        "Pide que explique de qué otras ciudades dependía su ciudad de ejemplo."),
    reinforce="Nombra tres instituciones de la ciudad colonial y di qué hacía cada una.",
    extend="Escribe una pregunta sobre cómo se comunicaba la ciudad con España.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, acta del cabildo de una ciudad de ejemplo, 1600: «Los alcaldes y regidores acuerdan reparar el puente con dinero de la ciudad y piden licencia al gobernador para cobrar una pequeña contribución a los comerciantes. Dos regidores son vecinos nacidos en la ciudad.» "
     "Fuente B, carta de un comerciante criollo de ejemplo, 1605, a un pariente: «Solo puedo vender mis cueros a los barcos que tienen permiso. Las mercaderías de España llegan caras y tardan meses. Aun así, en el cabildo defendemos los intereses de los vecinos.»")
build(
    OA, 2, F,
    use="Aprenderé a analizar un acta de cabildo y una carta de un comerciante para entender cómo funcionaba el poder en la ciudad colonial y qué límites tienen esas fuentes.",
    prior=["Sé contextualizar una fuente.", "Conozco las instituciones de la ciudad colonial.", "Sé distinguir descripción e interpretación."],
    explain=[
        "Un acta de cabildo es un documento donde se anotan los acuerdos de la reunión del cabildo. Sirve para ver qué temas preocupaban a la ciudad y quiénes decidían. En la ficha, el cabildo decide arreglar un puente con dinero de la ciudad, pero pide licencia al gobernador para cobrar una contribución. Eso muestra que el cabildo tenía poder local, pero dentro de límites.",
        "La carta de un comerciante criollo es una fuente personal. Cuenta que solo puede vender sus cueros a barcos con permiso, lo que revela el monopolio del comercio, y que las mercaderías de España llegan caras y con demora. También dice que en el cabildo defienden los intereses de los vecinos, lo que muestra el poder local de las elites criollas.",
        "Cada fuente tiene límites. El acta es oficial y no cuenta las discusiones internas. La carta expresa la opinión de un comerciante y puede exagerar los problemas. Las dos se complementan: una muestra la decisión, la otra, la vivencia.",
    ],
    vocab=[("acta", "documento que registra los acuerdos de una reunión"), ("regidor", "miembro del cabildo que participa en las decisiones de la ciudad"), ("licencia", "permiso oficial para hacer algo"), ("vecino", "persona con derechos y deberes en la ciudad colonial"), ("contribución", "pago que se exige para un fin público")],
    worked=[
        ("Contextualizar una fuente", "¿Quién escribió la Fuente B, a quién y cuándo?", ["Es un comerciante criollo.", "Escribe a un pariente en 1605."], "Un comerciante criollo, a un pariente, en 1605"),
        ("Relacionar fuente y concepto", "¿Qué concepto del OA muestra la frase «solo puedo vender a los barcos con permiso»?", ["Habla de un control del comercio.", "Eso es el monopolio."], "El monopolio del comercio"),
    ],
    mistakes=[("Creer que el cabildo tomaba decisiones sin límites.", "Se olvida que pedía licencia al gobernador.", "Observa los permisos que necesitaba."),
              ("Tomar la carta de un comerciante como si hablara por toda la ciudad.", "Expresa la visión de una persona.", "Compara con otras fuentes.")],
    T=[
        ("{F} ¿Quiénes acuerdan reparar el puente en la Fuente A?", "Los alcaldes y regidores del cabildo", "El acta lo dice."),
        ("{F} ¿A quién piden licencia para cobrar una contribución?", "Al gobernador", "El acta lo indica."),
        ("{F} ¿A quién escribe el comerciante de la Fuente B?", "A un pariente", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años separan el acta de la carta?", "1605-1600", "Se resta el primer año al segundo.", " años"),
        ("{F} ¿Con qué dinero se repara el puente según el acta?", "Con dinero de la ciudad", "Lo dice la Fuente A."),
        ("{F} ¿A qué barcos puede vender sus cueros el comerciante?", "A los que tienen permiso", "La Fuente B lo dice."),
        ("{F} ¿Qué muestra el hecho de que el cabildo pida licencia al gobernador? A) Que el cabildo tenía poder local, pero con límites B) Que el cabildo no existía", "A) Que el cabildo tenía poder local, pero con límites", "Decide, pero con autorización."),
        ("{F} Clasifica cada frase como hecho o juicio: a) «Los regidores acuerdan reparar el puente», b) «Las mercaderías de España llegan caras».", "a) hecho; b) juicio o queja del comerciante", "La primera es un acuerdo registrado; la segunda es una opinión."),
        ("{F} ¿Qué problema del monopolio muestra la Fuente B? A) Los productos de España llegan caros y tarde B) Los productos de España llegan baratos y rápido", "A) Los productos de España llegan caros y tarde", "El comerciante lo reclama."),
        ("{F} Un compañero dice: «La Fuente A prueba que los criollos mandaban en toda la ciudad». ¿Qué falla?", "El acta solo dice que dos regidores nacieron en la ciudad y que el cabildo pedía licencia al gobernador", "No permite concluir que mandaran en todo."),
        ("{F} ¿Qué límite tiene la Fuente B? A) Es la opinión de un solo comerciante B) Fue escrita por un gobernador enviado de España", "A) Es la opinión de un solo comerciante", "No representa a todos los vecinos."),
        ("{F} ¿Qué concepto del OA aparece en la frase «defendemos los intereses de los vecinos»?", "El poder local de las elites criollas", "El cabildo defendía intereses locales."),
        ("{F} ¿Qué otra fuente ayudaría a conocer a los comerciantes de la ciudad? A) Registros de ventas y de barcos que llegaron al puerto B) Un dibujo de la plaza", "A) Registros de ventas y de barcos que llegaron al puerto", "Muestra el comercio real."),
    ],
    ctx=("Una compañera quiere explicar con una frase cómo se relacionaba el cabildo con las autoridades superiores. Con la Fuente A, ¿qué escribiría? {F}", "Que el cabildo decidía algunos asuntos de la ciudad, pero necesitaba licencia del gobernador para otros", "Muestra poder local y límites."),
    sc=[("¿Qué es una licencia?", "Un permiso oficial para hacer algo", "Se definió en el vocabulario."),
        ("¿Qué es un acta?", "Un documento que registra los acuerdos de una reunión", "Se definió en el vocabulario."),
        ("¿Qué muestra la carta del comerciante? A) El monopolio del comercio B) La libertad total de comerciar", "A) El monopolio del comercio", "Solo podía vender a barcos con permiso.")],
    op=("Haz una tabla con las dos fuentes y cuatro filas: autor, fecha, qué muestra sobre el poder local y qué muestra sobre el control de España. Después escribe una frase de descripción y otra de interpretación que no exagere. {F}",
        "A: cabildo, 1600, decide el puente pero pide licencia, límite del gobernador. B: comerciante criollo, 1605, defiende intereses locales, monopolio. Descripción: el cabildo pide licencia. Interpretación: tenía poder local con límites.",
        ["completa las cuatro filas", "separa descripción e interpretación", "usa datos de la ficha"], ["tabla", "dos frases"], ["afirmar que mandaban sin límites", "no distinguir fuentes"],
        "Pide que diga qué otra fuente buscaría para saber qué opinaban los indígenas."),
    reinforce="Explica con tus palabras qué es un acta de cabildo y qué sirve para investigar.",
    extend="Escribe una pregunta que no se pueda responder con la ficha y sugiere qué fuente usar.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (territorio y comunicación, simplificados; los tiempos son de ejemplo). Una ciudad de la costa, como Valparaíso, funciona como puerto; la capital, como Santiago, concentra autoridades. "
     "Rutas de comercio autorizadas: de Sevilla a puertos como Veracruz, Portobelo y Cartagena; desde Portobelo, las mercaderías cruzaban Panamá y seguían por mar hasta el Callao, el puerto de Lima, y desde allí a otros puertos. "
     "Tiempos de ejemplo: una orden desde España tardaba unos 6 meses en llegar a una ciudad de Chile. "
     "Cambios: ciudades españolas se levantaron, a veces sobre ciudades indígenas, como México sobre Tenochtitlan y Cusco sobre la capital inca; el comercio quedó controlado por el monopolio. "
     "Continuidades: muchos pueblos indígenas siguieron viviendo en sus comunidades; los alimentos de la ciudad venían del campo cercano; el trabajo de la tierra seguía siendo la base de la economía.")
build(
    OA, 3, F,
    use="Aprenderé a explicar cómo la ciudad se relacionaba con su territorio y con España, y qué cambió y qué continuó con el monopolio comercial.",
    prior=["Conozco las instituciones de la ciudad colonial.", "Conozco el mercantilismo y las rutas.", "Sé distinguir cambio y continuidad."],
    explain=[
        "El territorio explica cómo funcionaba la ciudad colonial. Las ciudades de la costa eran puertos; las capitales concentraban autoridades; y en el campo cercano se producían los alimentos. Desde España, el comercio autorizado seguía rutas fijas: de Sevilla a puertos americanos como Veracruz, Portobelo y Cartagena, y desde Portobelo hacia el sur por el Pacífico, hasta el Callao, el puerto de Lima, y otros puertos.",
        "La distancia hacía lenta la comunicación. Una orden de España podía tardar unos seis meses en llegar a Chile, según el dato de ejemplo. Por eso las autoridades locales debían decidir muchas cosas sin consultar, y los vecinos influyentes tenían poder real. El monopolio también encarecía las mercaderías y limitaba a quienes podían comerciar.",
        "Hubo cambios: nuevas ciudades españolas, a veces sobre ciudades indígenas, como México sobre Tenochtitlan o Cusco sobre la capital inca, y un comercio controlado. Pero hubo continuidades: muchos pueblos indígenas siguieron en sus comunidades, el campo seguía alimentando la ciudad y el trabajo de la tierra era la base de la economía.",
    ],
    vocab=[("puerto", "lugar de la costa donde llegan y salen barcos"), ("ruta autorizada", "camino de comercio permitido por el Estado"), ("encarecer", "hacer más caro un producto"), ("comunicación", "paso de noticias y órdenes de un lugar a otro"), ("campo cercano", "zona rural que abastece a una ciudad")],
    worked=[
        ("Seguir una ruta", "Según la ficha, ¿por dónde llegaban las mercaderías españolas desde Portobelo hasta Lima?", ["Cruzaban Panamá por tierra.", "Seguían por mar hasta el Callao."], "Cruzando Panamá y luego por mar hasta el Callao"),
        ("Clasificar cambio y continuidad", "Una ciudad se levanta sobre una ciudad indígena, pero los pueblos siguen en sus comunidades del campo. ¿Qué es cambio y qué continuidad?", ["Levantar una ciudad española es nuevo: cambio.", "Seguir en sus comunidades es continuidad."], "Cambio: la nueva ciudad; continuidad: las comunidades"),
    ],
    mistakes=[("Creer que una orden del rey llegaba al instante.", "Se ignora la distancia y el tiempo de viaje.", "Usa el dato de seis meses como ejemplo."),
              ("Pensar que la ciudad no dependía del campo.", "Se olvida de dónde venían los alimentos.", "Menciona el campo cercano.")],
    T=[
        ("{F} ¿Cuál es el puerto de Lima mencionado en la ficha?", "El Callao", "La ficha lo indica."),
        ("{F} ¿Qué ciudad se levantó sobre Tenochtitlan?", "México", "La ficha lo dice."),
        ("{F} ¿Cuál de estas ciudades españolas se levantó sobre una capital indígena: Valparaíso o Cusco?", "Cusco", "La ficha dice que Cusco se levantó sobre la capital inca."),
        ("=", "{F} Una orden tarda 6 meses en llegar a Chile y otros 6 meses la respuesta vuelve a España. ¿Cuántos meses pasan en total?", "6+6", "Se suman ida y vuelta.", " meses"),
        ("=", "{F} Un barco recorre 90 km por día. ¿Cuántos km recorre en 10 días?", "90*10", "Se multiplica lo que recorre por día por los días.", " km"),
        ("{F} ¿De dónde venían los alimentos de la ciudad?", "Del campo cercano", "La ficha lo indica."),
        ("{F} Clasifica como cambio o continuidad: a) nuevas ciudades españolas, b) el trabajo de la tierra como base de la economía, c) el monopolio del comercio.", "a) cambio; b) continuidad; c) cambio", "Solo el trabajo de la tierra se mantiene."),
        ("{F} ¿Por qué las autoridades locales debían decidir muchas cosas sin consultar? A) Porque las órdenes tardaban meses en llegar B) Porque los vecinos no obedecían ninguna ley", "A) Porque las órdenes tardaban meses en llegar", "La distancia hacía lenta la comunicación."),
        ("{F} ¿Qué efecto tiene el monopolio comercial sobre los precios? A) Los encarece B) Los abarata", "A) Los encarece", "La ficha lo indica como un efecto del control del comercio."),
        ("{F} Un compañero dice: «Las ciudades coloniales funcionaban aisladas». ¿Qué datos de la ficha lo contradicen?", "Dependían del campo cercano y de rutas de comercio con España", "La ficha muestra relaciones con ambos."),
        ("{F} ¿Qué ruta pasaba por Panamá?", "La que unía Portobelo con el Pacífico hacia el Callao", "La ficha describe ese cruce."),
        ("{F} ¿Qué conclusión es proporcional? A) La ciudad dependía del campo y de España, y tenía autoridades locales por la distancia B) La ciudad era independiente de todos", "A) La ciudad dependía del campo y de España, y tenía autoridades locales por la distancia", "La ficha muestra esas relaciones."),
        ("{F} ¿Qué dato necesitarías para saber cuánto tardaba una orden a otra ciudad?", "Registros de fechas de salida y de llegada de órdenes", "Mostrarían el tiempo real."),
    ],
    ctx=("Un vecino de una ciudad chilena de ejemplo se queja de que la mercadería llega cara. Con la ficha, ¿qué explicación das? {F}", "Porque el comercio estaba controlado por un monopolio y las mercaderías viajaban por rutas largas autorizadas", "El monopolio y la distancia encarecían los productos."),
    sc=[("¿Qué es una ruta autorizada?", "Un camino de comercio permitido por el Estado", "Se definió en el vocabulario."),
        ("¿Qué provee el campo cercano a la ciudad?", "Alimentos", "La ficha lo indica."),
        ("¿Qué tardaba unos seis meses según el dato de ejemplo? A) Una orden de España B) La cosecha de un campo cercano", "A) Una orden de España", "El tiempo de comunicación era largo.")],
    op=("Dibuja un mapa muy simple con Sevilla, Veracruz, Portobelo, Callao y una ciudad de Chile. Une con flechas las rutas autorizadas y escribe al lado el tiempo de ejemplo de una orden. Debajo escribe un cambio y una continuidad de la ficha. {F}",
        "Sevilla a Veracruz y Portobelo; Portobelo a Callao; Callao a Chile; orden: 6 meses. Cambio: nuevas ciudades. Continuidad: el campo sigue alimentando la ciudad.",
        ["dibuja las rutas", "incluye el tiempo de ejemplo", "nombra cambio y continuidad"], ["mapa", "dos frases"], ["mezclar las rutas", "decir que no había continuidades"],
        "Pide que explique por qué la distancia dio poder a las autoridades locales."),
    reinforce="Cuenta una ruta autorizada con sus puertos y su efecto en los precios.",
    extend="Escribe una pregunta sobre cómo vivían los trabajadores de los puertos.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno; no son testimonios reales). "
     "Voz 1, gobernador enviado desde España, 1610: «Represento al rey y debo hacer cumplir sus leyes y cobrar sus impuestos; no puedo permitir que la ciudad decida sola.» "
     "Voz 2, regidor criollo, 1610: «Nací aquí, conozco las necesidades de la ciudad y mi familia posee tierras; en el cabildo defendemos los intereses de los vecinos.» "
     "Voz 3, comerciante venido de España, 1610: «Tengo licencia del rey para comerciar; el monopolio protege mi negocio.» "
     "Voz 4, obispo, 1610: «La Iglesia tiene un lugar central en la ciudad y debemos cuidar a todos los fieles.» "
     "Voz 5, indígena de un pueblo cercano, 1610: «Trabajamos las tierras y entregamos parte de lo que producimos para la ciudad; nadie nos pregunta qué necesitamos.» "
     "Causas del poder criollo: la distancia con España, la compra de cargos y la propiedad de tierras.")
build(
    OA, 4, F,
    use="Aprenderé a contrastar a los actores de la ciudad colonial y a explicar por qué las elites criollas consolidaron poder local.",
    prior=["Conozco las instituciones de la ciudad colonial.", "Sé contrastar perspectivas.", "Sé que un hecho puede tener varias causas."],
    explain=[
        "En la ciudad colonial convivían actores con intereses distintos. El gobernador representaba al rey y quería hacer cumplir sus leyes. Los comerciantes venidos de España defendían el monopolio. Los criollos, nacidos en América, tenían tierras y familias en la ciudad y querían influir en el cabildo. El obispo cuidaba el lugar de la Iglesia. Los indígenas de pueblos cercanos entregaban trabajo y productos, casi sin voz en las decisiones.",
        "El poder local de las elites criollas se consolidó por varias causas. La distancia con España daba autonomía de hecho. La compra de cargos, como el de regidor, permitía a familias ricas entrar al cabildo. Y la propiedad de tierras les daba riqueza y prestigio. No era una rebelión contra el rey, sino una forma de ganar influencia dentro del sistema.",
        "Contrastar las voces ayuda a ver tensiones: entre la metrópoli y la ciudad, entre peninsulares y criollos, entre la ciudad y el campo. Pero hay que recordar que las voces indígenas y de otros grupos suelen faltar en las fuentes. Una explicación completa debe reconocer también quién quedaba fuera de las decisiones.",
    ],
    vocab=[("peninsular", "español nacido en la península ibérica"), ("criollo", "español nacido en América"), ("elite", "grupo pequeño con mucho poder, riqueza o prestigio"), ("compra de cargos", "pago por un puesto público que daba poder en la ciudad"), ("autonomía", "capacidad de decidir sin depender de otros")],
    worked=[
        ("Reconocer un interés", "¿Qué interés tiene el comerciante de la voz 3?", ["Leo su voz.", "Dice que el monopolio protege su negocio."], "Mantener el monopolio que protege su negocio"),
        ("Explicar una causa", "¿Por qué la distancia ayudó al poder de los criollos?", ["Las órdenes tardaban meses.", "Las autoridades locales debían decidir."], "Daba autonomía de hecho a las decisiones locales"),
    ],
    mistakes=[("Pensar que criollos y peninsulares tenían los mismos intereses.", "Se ignoran las tensiones por cargos y comercio.", "Distingue ambos grupos."),
              ("Olvidar que los indígenas casi no participaban en las decisiones.", "Se mira solo a la elite.", "Incluye a quienes quedaban fuera.")],
    T=[
        ("{F} ¿Quién dice «represento al rey y debo hacer cumplir sus leyes»?", "El gobernador enviado desde España", "Es la voz 1."),
        ("{F} ¿Qué defiende el regidor criollo?", "Los intereses de los vecinos", "La voz 2 lo dice."),
        ("{F} ¿Qué dice el indígena de la voz 5 sobre las decisiones?", "Que nadie les pregunta qué necesitan", "La voz 5 lo expresa."),
        ("{F} ¿Qué es un criollo?", "Un español nacido en América", "Se definió en la clase."),
        ("=", "{F} En una ciudad de ejemplo, un cargo de regidor se vende en 300 monedas y una familia compra 2 cargos. ¿Cuántas monedas paga?", "300*2", "Se multiplica el precio de un cargo por la cantidad.", " monedas"),
        ("{F} Clasifica cada actor según defienda al rey, al monopolio o los intereses locales: a) gobernador, b) comerciante venido de España, c) regidor criollo.", "a) al rey; b) el monopolio; c) los intereses locales", "Cada voz tiene un interés distinto."),
        ("{F} ¿Qué causa del poder criollo se relaciona con la voz 2? A) La propiedad de tierras B) La prohibición de comerciar", "A) La propiedad de tierras", "El regidor dice que su familia posee tierras."),
        ("{F} ¿Qué tensión muestran las voces 1 y 2?", "Entre quien representa al rey y quien defiende los intereses locales", "El gobernador quiere cumplir leyes del rey; el regidor defiende a los vecinos."),
        ("{F} Un compañero dice: «Los criollos querían separarse de España en 1610». ¿Qué falla?", "La ficha muestra que querían influir en el cabildo, no separarse del imperio", "No hay evidencia de que buscaran separarse."),
        ("{F} ¿Qué voz tiene menos capacidad de decidir en la ciudad? A) La voz 5, la del indígena B) La voz 1, la del gobernador", "A) La voz 5, la del indígena", "Dice que nadie les pregunta."),
        ("{F} ¿Cuál es una causa de la autonomía de hecho de los criollos?", "La distancia con España", "Las órdenes tardaban meses."),
        ("{F} ¿Qué conclusión es proporcional? A) Las elites criollas ganaron poder local por distancia, compra de cargos y tierras B) Los criollos gobernaban solos", "A) Las elites criollas ganaron poder local por distancia, compra de cargos y tierras", "La ficha lista tres causas."),
        ("{F} ¿Qué voz falta en la ficha y sería importante escuchar?", "La de una mujer, un artesano o una persona esclavizada", "La ficha no incluye a esos grupos."),
    ],
    ctx=("En un debate de curso, un grupo defiende al gobernador y otro al regidor criollo. ¿Qué argumento clave daría cada uno? {F}", "El gobernador, que debe hacer cumplir las leyes del rey; el regidor, que conoce las necesidades locales y defiende a los vecinos", "Cada uno habla desde su interés."),
    sc=[("¿Qué es una elite?", "Un grupo pequeño con mucho poder, riqueza o prestigio", "Se definió en el vocabulario."),
        ("¿Qué es la compra de cargos?", "El pago por un puesto público que daba poder en la ciudad", "Se definió en el vocabulario."),
        ("¿Qué cargo de la ficha podían comprar las familias ricas para entrar al cabildo? A) El de regidor B) El de obispo", "A) El de regidor", "El cargo de regidor se podía comprar.")],
    op=("Escribe un diálogo de seis líneas entre el gobernador y el regidor criollo de la ficha. Cada uno debe usar una idea de su voz. Cierra con una frase tuya sobre por qué el regidor no necesitaba rebelarse contra el rey para ganar influencia. {F}",
        "Gobernador: debo hacer cumplir las leyes del rey. Regidor: conozco la ciudad y defiendo a los vecinos. Cierre: ganaba influencia dentro del cabildo, sin rebelarse.",
        ["usa ideas de la ficha", "respeta las dos posiciones", "explica la influencia dentro del sistema"], ["diálogo", "frase"], ["decir que quería independizarse", "inventar hechos"],
        "Pide que explique qué voz falta en su diálogo."),
    reinforce="Explica con tus palabras tres causas del poder local criollo.",
    extend="Escribe una pregunta que le harías a una persona indígena de un pueblo cercano a la ciudad.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (pregunta y evidencias de ejemplo). Pregunta: ¿era la ciudad colonial solo un instrumento del rey o también un espacio de poder local? "
     "Evidencia 1: el cabildo decide reparar un puente con dinero de la ciudad. "
     "Evidencia 2: el cabildo pide licencia al gobernador para cobrar una contribución. "
     "Evidencia 3: el comercio con América pasa por la Casa de Contratación y por rutas autorizadas. "
     "Evidencia 4: dos regidores del cabildo son criollos que poseen tierras. "
     "Evidencia 5: las órdenes de España tardan meses en llegar. "
     "Evidencia 6: los pueblos indígenas cercanos entregan trabajo y productos sin participar en las decisiones.")
build(
    OA, 5, F,
    use="Aprenderé a construir un argumento sobre el rol de la ciudad en la administración del imperio, considerando instituciones, monopolio, relación con la metrópoli y poder criollo.",
    prior=["Sé que un argumento tiene tesis, evidencias y límite.", "Conozco las instituciones y el monopolio.", "Conozco el poder local criollo."],
    explain=[
        "Para responder si la ciudad colonial era solo un instrumento del rey o también un espacio de poder local, hay que mirar evidencias de ambos lados. A favor del control del rey están el monopolio y la necesidad de licencias del gobernador. A favor del poder local están las decisiones del cabildo, los regidores criollos con tierras y la distancia que retrasaba las órdenes.",
        "Una tesis equilibrada puede decir que la ciudad fue, a la vez, un centro de control del imperio y un espacio donde las elites criollas ganaron poder dentro de ese sistema. Esa respuesta usa evidencias de los dos tipos y evita las dos simplificaciones: que todo venía del rey o que la ciudad era independiente.",
        "El límite debe reconocer quién queda fuera: los pueblos indígenas aparecen entregando trabajo sin participar en las decisiones. Eso muestra que el poder local fue de elites, no de todos los habitantes.",
    ],
    vocab=[("instrumento", "medio que usa alguien para lograr un fin"), ("espacio de poder", "lugar donde se toman decisiones importantes"), ("tesis", "respuesta que se defiende con evidencias"), ("elite criolla", "grupo de criollos con tierras, riqueza y cargos"), ("límite", "lo que la evidencia no permite concluir")],
    worked=[
        ("Clasificar evidencias", "¿Qué evidencias muestran control del rey?", ["Busco licencias y monopolio.", "Las evidencias 2 y 3."], "Las evidencias 2 y 3"),
        ("Redactar un límite", "Tesis: «La ciudad fue un espacio de poder criollo». ¿Qué límite agregas?", ["La evidencia 6 muestra a quien queda fuera.", "El poder era de elites."], "El poder local no incluía a los pueblos indígenas"),
    ],
    mistakes=[("Decir que todas las decisiones venían del rey.", "Se ignora la autonomía de hecho del cabildo.", "Cita las evidencias 1, 4 y 5."),
              ("Decir que la ciudad era independiente de España.", "Se ignora el monopolio y las licencias.", "Cita las evidencias 2 y 3.")],
    T=[
        ("{F} ¿Qué evidencia muestra el monopolio?", "La evidencia 3", "Habla de la Casa de Contratación y rutas autorizadas."),
        ("{F} ¿Qué evidencia muestra poder criollo?", "La evidencia 4", "Dos regidores son criollos con tierras."),
        ("{F} ¿Qué evidencia muestra que el cabildo necesitaba autorización?", "La evidencia 2", "Pide licencia al gobernador."),
        ("{F} ¿Qué evidencias muestran poder local?", "La 1, la 4 y la 5", "El cabildo decide, hay regidores criollos y la distancia da autonomía."),
        ("{F} Clasifica cada evidencia como control del rey o poder local: a) 2, b) 4, c) 5.", "a) control del rey; b) poder local; c) poder local", "La licencia limita al cabildo; los regidores criollos y la distancia dan poder local."),
        ("{F} ¿Qué tesis se apoya mejor en las evidencias? A) La ciudad fue centro de control del imperio y también espacio de poder criollo B) La ciudad fue totalmente independiente", "A) La ciudad fue centro de control del imperio y también espacio de poder criollo", "Hay evidencias de ambos tipos."),
        ("{F} Un compañero dice: «Todas las decisiones venían de España». ¿Qué evidencia lo contradice?", "La evidencia 1, porque el cabildo decide reparar un puente con dinero de la ciudad", "Muestra decisiones locales."),
        ("{F} ¿Qué evidencia funciona como límite del poder local?", "La evidencia 6", "Muestra quién queda sin participar."),
        ("{F} Escribe un límite honesto para la tesis.", "Las evidencias no muestran que todos los habitantes participaran; los pueblos indígenas quedan fuera", "Un argumento reconoce quién queda fuera."),
        ("{F} ¿Por qué la evidencia 5 ayuda a explicar el poder local? A) Porque la distancia daba autonomía de hecho B) Porque el gobernador no obedecía al rey", "A) Porque la distancia daba autonomía de hecho", "Las órdenes tardaban meses."),
        ("{F} ¿Qué respuesta es más sólida? A) «El rey controló con el monopolio y las licencias, pero los criollos ganaron poder local en el cabildo» B) «Todo fue del rey»", "A) «El rey controló con el monopolio y las licencias, pero los criollos ganaron poder local en el cabildo»", "Combina evidencias de ambos tipos."),
        ("{F} ¿Qué error comete quien cita solo la evidencia 3?", "Muestra solo el control del rey y deja fuera el poder local", "No cubre los dos lados."),
        ("{F} ¿Qué evidencia nueva buscarías para saber más sobre las decisiones del cabildo?", "Más actas de cabildo de distintos años", "Mostrarían qué temas decidía y con qué límites."),
    ],
    ctx=("Para una exposición escolar se pide una frase que resuma el rol de la ciudad colonial. Redáctala con dos evidencias de la ficha. {F}", "La ciudad fue un centro de control del imperio por el monopolio (evidencia 3) y también un espacio de poder criollo en el cabildo (evidencia 4)", "Combina control y poder local."),
    sc=[("¿Qué evidencia muestra el trabajo indígena sin participación?", "La evidencia 6", "Habla de entregar trabajo sin participar."),
        ("¿Qué es una tesis?", "Una respuesta que se defiende con evidencias", "Se definió en el vocabulario."),
        ("¿Qué partes tiene un argumento? A) Tesis, evidencias y límite B) Solo fechas", "A) Tesis, evidencias y límite", "Son las tres partes.")],
    op=("Escribe un párrafo de seis líneas que responda la pregunta de la ficha. Incluye tu tesis, una evidencia de control del rey, una evidencia de poder local y un límite. {F}",
        "Pienso que la ciudad fue ambas cosas. Evidencia 3: monopolio. Evidencia 4: regidores criollos con tierras. Límite: los pueblos indígenas quedan fuera de las decisiones.",
        ["tiene tesis", "una evidencia de cada tipo", "incluye un límite"], ["párrafo"], ["citar solo un tipo de evidencia", "olvidar el límite"],
        "Pide que explique qué evidencia le costó más clasificar."),
    reinforce="Explica oralmente por qué la ciudad fue a la vez centro de control y espacio de poder local.",
    extend="Escribe una pregunta sobre cómo cambió el cabildo con los años.",
)
