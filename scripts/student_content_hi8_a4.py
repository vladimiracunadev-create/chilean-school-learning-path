"""Material del estudiante de 8.º básico, Historia, Geografía y Ciencias Sociales: OA 04 (mercantilismo y expansión económica europea)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI08 OA 04"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (resumen y hitos redondeados). Mercantilismo del siglo XVI: idea de que la riqueza de un Estado se mide por el oro y la plata que acumula; para lograrlo, el Estado intenta vender más de lo que compra (balanza comercial favorable), controla el comercio y busca colonias que le entreguen materias primas y metales. "
     "Hitos: 1492, Colón llega a América; 1498, el portugués Vasco da Gama llega a la India por mar rodeando África; 1519-1522, expedición Magallanes-Elcano da la primera vuelta al mundo; 1545, se descubre la plata de Potosí, en el Alto Perú; 1565, comienza la ruta del galeón entre Manila y Acapulco; 1600 y 1602, se crean las compañías de las Indias Orientales de Inglaterra y de los Países Bajos.")
build(
    OA, 1, F,
    use="Aprenderé a situar la economía mercantilista del siglo XVI en el tiempo y el espacio, y a nombrar los cinco fenómenos económicos que el OA pide estudiar.",
    prior=["Conozco la expansión europea y el Estado moderno.", "Sé calcular diferencias entre años.", "Sé ubicar continentes y océanos."],
    explain=[
        "El mercantilismo fue un conjunto de ideas y prácticas económicas del siglo XVI y siguientes. Según ellas, un Estado es más poderoso mientras más metales preciosos, como oro y plata, acumula. Para lograrlo debe vender al extranjero más de lo que compra, esa es la balanza comercial favorable, y debe controlar el comercio y sus colonias.",
        "El OA pide estudiar cinco fenómenos: la acumulación y circulación de metales preciosos, la ampliación de las rutas comerciales, la expansión mundial de la economía europea, la revolución de los precios y el aumento de la competencia entre Estados y compañías. Se relacionan entre sí: más rutas traen más metales, más metales en circulación suben los precios y la competencia aumenta cuando varios Estados quieren lo mismo.",
        "Hay que cuidar el tiempo y el espacio. Las rutas conectaron Europa con América, Asia y África. La plata de Potosí, descubierta en 1545, es un ejemplo de metal que cruzó el Atlántico y el Pacífico. No todos los países aplicaron el mercantilismo de la misma manera; por eso no es una receta única.",
    ],
    vocab=[("mercantilismo", "ideas económicas que miden la riqueza por los metales preciosos y la intervención del Estado"), ("metal precioso", "oro o plata, valorados como riqueza"), ("balanza comercial favorable", "situación en que un Estado vende al exterior más de lo que compra"), ("colonia", "territorio controlado por otro Estado"), ("ruta comercial", "camino por tierra o mar que se usa para comerciar")],
    worked=[
        ("Calcular una distancia en años", "Según la ficha, ¿cuántos años pasaron entre la llegada de Colón a América y la de Vasco da Gama a la India?", ["Busco los años: 1492 y 1498.", "Resto: 1498 − 1492 = 6."], "6 años"),
        ("Reconocer un rasgo mercantilista", "Un Estado prohíbe a sus colonias comerciar con otros países. ¿Qué rasgo mercantilista aparece?", ["El Estado controla el comercio.", "La colonia solo comercia con la metrópoli."], "Control del comercio y de las colonias por el Estado"),
    ],
    mistakes=[("Creer que el mercantilismo era igual en todos los países.", "Se ignora que cada Estado lo aplicó de forma distinta.", "Compara casos y evita hablar de una receta única."),
              ("Pensar que la riqueza era solo el dinero en el bolsillo de las personas.", "Se confunde la riqueza de las personas con la del Estado en esa teoría.", "Recuerda que se medía por los metales que acumulaba el Estado.")],
    T=[
        ("{F} ¿Con qué se mide la riqueza de un Estado según el mercantilismo?", "Con el oro y la plata que acumula", "La ficha lo define así."),
        ("{F} ¿Qué es una balanza comercial favorable?", "Vender al exterior más de lo que se compra", "Así lo explica la ficha."),
        ("{F} ¿Dónde se descubrió la plata que se menciona en 1545?", "En Potosí, en el Alto Perú", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años duró la expedición Magallanes-Elcano, de 1519 a 1522?", "1522-1519", "Se resta el año de inicio al de término.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre el descubrimiento de la plata de Potosí y el inicio de la ruta del galeón de Manila?", "1565-1545", "Se restan los dos años.", " años"),
        ("{F} ¿A qué siglo pertenecen las compañías de las Indias Orientales creadas en 1600 y 1602?", "Siglo XVI la de 1600 y siglo XVII la de 1602", "El siglo XVI llega hasta 1600 y el XVII comienza en 1601."),
        ("{F} Clasifica cada situación con un fenómeno del OA: a) llegan barcos con plata a Sevilla, b) se abre la ruta Manila-Acapulco, c) dos compañías europeas disputan el mismo comercio.", "a) acumulación y circulación de metales; b) ampliación de rutas; c) aumento de la competencia", "Cada situación corresponde a un fenómeno distinto."),
        ("{F} Un reino vende 800 piezas de tela y compra 500 piezas de otros países. ¿Su balanza es favorable? A) Sí, porque vende más de lo que compra B) No, porque compra más de lo que vende", "A) Sí, porque vende más de lo que compra", "800 es mayor que 500."),
        ("=", "{F} Otro reino vende 950 piezas de tela y compra 700. ¿Cuántas piezas más vende que compra?", "950-700", "Se resta lo comprado de lo vendido.", " piezas"),
        ("{F} ¿Por qué se dice que el mercantilismo no era una receta única?", "Porque cada Estado lo aplicó de manera distinta", "La ficha lo presenta como un conjunto de ideas aplicadas con variaciones."),
        ("{F} Un compañero dice: «El mercantilismo es lo mismo que el comercio libre». ¿Qué dato de la ficha lo contradice?", "El Estado controla el comercio y las colonias", "El comercio libre sin control estatal no es mercantilismo."),
        ("{F} Una línea de tiempo usa 1 cm = 20 años y parte en 1492. ¿A cuántos cm queda 1602, redondeando hacia abajo?", "5 cm", "La diferencia es 110 años y 110 dividido por 20 da 5 completos."),
        ("{F} ¿Qué rutas de la ficha unen Europa con Asia y con América? A) Vasco da Gama por África y Colón por el Atlántico B) Solo viajes por el Mediterráneo", "A) Vasco da Gama por África y Colón por el Atlántico", "Ambos son viajes por mar."),
    ],
    ctx=("Un museo prepara una vitrina sobre Potosí. Con la ficha, ¿qué rasgo mercantilista destacaría y por qué? {F}", "La acumulación de metales preciosos, porque la plata que sale de Potosí sirve para enriquecer a un Estado europeo", "Conecta el metal con la riqueza del Estado."),
    sc=[("¿Qué es una colonia?", "Un territorio controlado por otro Estado", "Se definió en la clase."),
        ("¿Qué año se descubrió la plata de Potosí?", "1545", "Aparece en la ficha."),
        ("=", "¿Cuántos años pasaron entre la creación de la compañía inglesa (1600) y la de los Países Bajos (1602)?", "1602-1600", "Se restan los dos años.", " años")],
    op=("Dibuja una línea de tiempo con 1 cm = 20 años desde 1480 hasta 1620. Marca cuatro hitos de la ficha (1492, 1498, 1545 y 1602) con su nombre. Debajo escribe una frase que relacione uno de ellos con la acumulación de metales preciosos. {F}",
        "1492 a 0,6 cm, 1498 a 0,9 cm, 1545 a 3,25 cm, 1602 a 6,1 cm; frase: «La plata de Potosí cruza el océano y aumenta la riqueza del Estado».",
        ["respeta la escala", "ubica los cuatro hitos", "relaciona un hito con los metales"], ["línea de tiempo", "frase"], ["no respetar la escala", "escribir que el mercantilismo era comercio libre"],
        "Pide que explique por qué 1545 queda lejos de 1492."),
    reinforce="Nombra los cinco fenómenos del OA y explica uno con tus palabras.",
    extend="Escribe una pregunta que un historiador haría para saber si un Estado aplicaba el mercantilismo.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son datos históricos reales). "
     "Fuente A, carta de un consejero del rey de un reino imaginario, 1590: «Un reino es rico mientras tenga más oro y plata. Debemos vender más de lo que compramos, no dejar salir el metal y prohibir que las colonias comercien con extranjeros.» "
     "Fuente B, registro de llegada de plata al puerto, en toneladas, por periodos de cinco años (cifras de ejemplo): 1550-1554: 40; 1560-1564: 60; 1570-1574: 80; 1580-1584: 100; 1590-1594: 140.")
build(
    OA, 2, F,
    use="Aprenderé a leer una carta y una tabla de datos sobre el mercantilismo, a calcular cambios en la llegada de metales y a distinguir lo que las fuentes prueban.",
    prior=["Sé contextualizar una fuente.", "Sé leer tablas y comparar cantidades.", "Conozco el mercantilismo."],
    explain=[
        "Las fuentes económicas pueden ser textos que opinan y registros que cuentan datos. La carta del consejero opina que un reino es rico si acumula metales y propone medidas: vender más de lo que se compra, evitar que salga metal y prohibir el comercio de las colonias con extranjeros. Es una fuente de ideas y de política, no una descripción neutra.",
        "El registro de llegadas de plata es una fuente de datos, aquí de ejemplo. Permite ver una tendencia: la cantidad de plata que llega a un puerto aumenta con los años. Para interpretarla hay que contextualizar: ¿quién llevó el registro?, ¿qué periodos cubre?, ¿se registraron los metales que entraban sin permiso? Un registro oficial puede dejar fuera el contrabando.",
        "Al cruzar ambas fuentes se ve que la teoría del consejero se relaciona con el flujo de plata, pero la carta no prueba que las medidas funcionaran. Una buena conclusión se limita a lo que las fuentes permiten: el flujo de metales creció y había una idea que lo valoraba.",
    ],
    vocab=[("tendencia", "dirección en que cambian los datos con el tiempo"), ("registro", "documento donde se anotan datos de manera ordenada"), ("contrabando", "comercio hecho sin permiso del Estado"), ("consejero", "persona que aconseja al rey en asuntos de gobierno"), ("flujo", "movimiento continuo de algo, como el metal que llega a un puerto")],
    worked=[
        ("Calcular un aumento", "En la Fuente B, ¿cuántas toneladas más llegaron en 1590-1594 que en 1550-1554?", ["Busco: 140 y 40.", "Resto: 140 − 40 = 100."], "100 toneladas más"),
        ("Distinguir tipos de fuente", "¿Qué tipo de fuente es la Fuente A y por qué no es neutral?", ["La escribe un consejero que opina.", "Propone medidas, así que defiende una idea."], "Fuente de opinión que defiende una política"),
    ],
    mistakes=[("Creer que un registro oficial cuenta todo lo que entraba.", "Se ignora el contrabando.", "Pregunta qué quedaba fuera del registro."),
              ("Tratar una carta de opinión como si fuera un dato.", "Se confunde idea con medición.", "Separa lo que se opina de lo que se mide.")],
    T=[
        ("{F} ¿Quién escribió la Fuente A?", "Un consejero del rey", "La ficha lo indica."),
        ("{F} ¿Cuántas toneladas de plata llegaron en 1570-1574?", "80", "Es el dato del registro de ese periodo."),
        ("{F} ¿Qué prohíbe el consejero a las colonias?", "Comerciar con extranjeros", "La carta lo dice."),
        ("=", "{F} ¿Cuántas toneladas llegaron en total en los tres primeros periodos de la tabla (1550-1554, 1560-1564 y 1570-1574)?", "40+60+80", "Se suman los tres periodos.", " toneladas"),
        ("=", "{F} ¿Cuántas toneladas más llegaron en 1590-1594 que en 1580-1584?", "140-100", "Se restan los valores de los dos periodos.", " toneladas"),
        ("{F} ¿Qué tendencia muestra la tabla? A) La llegada de plata aumenta con los años B) La llegada de plata disminuye", "A) La llegada de plata aumenta con los años", "Los números suben de 40 a 140."),
        ("{F} ¿En cuál de los periodos de la tabla aumentó más la plata respecto del anterior?", "En 1590-1594, con 40 toneladas más", "Los aumentos fueron de 20, 20, 20 y 40."),
        ("{F} Clasifica: a) «Un reino es rico si tiene más oro y plata», b) «En 1580-1584 llegaron 100 toneladas». ¿Cuál es opinión y cuál dato?", "a) opinión; b) dato", "La primera es una idea del consejero; la segunda es una cifra del registro."),
        ("=", "{F} Si el consejero lograra que el reino venda 600 piezas de tela y compre 450, ¿cuántas piezas más vende que compra?", "600-450", "Se resta lo comprado de lo vendido.", " piezas"),
        ("{F} Un compañero concluye con la tabla: «Las medidas del consejero hicieron aumentar la plata». ¿Qué falla?", "La tabla muestra el aumento, pero no prueba que fuera por esas medidas", "Correlación no es causa."),
        ("{F} ¿Por qué un registro oficial puede mostrar menos plata de la que realmente entraba?", "Porque dejaba fuera el contrabando", "Lo que entraba sin permiso no se anotaba."),
        ("{F} ¿Qué otra fuente ayudaría a comprobar si la plata entraba por contrabando? A) Una denuncia o un juicio por contrabando de la época B) Otro registro oficial de llegada de plata de la misma época", "A) Una denuncia o un juicio por contrabando de la época", "Mostraría casos de entrada sin permiso."),
        ("{F} ¿Qué conclusión es proporcional a las dos fuentes? A) El registro muestra aumento de plata y la carta expresa una idea que valoraba acumularla B) El mercantilismo fue la única causa del aumento", "A) El registro muestra aumento de plata y la carta expresa una idea que valoraba acumularla", "No sobrepasa lo que dicen las fuentes."),
    ],
    ctx=("Un diario escolar de ejemplo quiere titular: «La plata creció en cada periodo registrado». ¿Qué dato de la tabla confirma que no creció siempre lo mismo entre un periodo y el siguiente? {F}", "Entre 1590-1594 y 1580-1584 creció 40, el doble que los 20 de los periodos anteriores", "Los aumentos fueron de 20, 20, 20 y 40."),
    sc=[("¿Qué es el contrabando?", "Comercio hecho sin permiso del Estado", "Se definió en la clase."),
        ("¿Qué es una tendencia?", "La dirección en que cambian los datos con el tiempo", "Se definió en el vocabulario."),
        ("=", "Entre 1550-1554 y 1560-1564, ¿cuántas toneladas más llegaron?", "60-40", "Se restan los dos valores.", " toneladas")],
    op=("Dibuja un gráfico de barras con los cinco periodos de la tabla, una barra por periodo, con la altura proporcional a las toneladas. Debajo escribe dos frases: una que describa la tendencia y otra que explique por qué las cifras no prueban que el mercantilismo causara el aumento. {F}",
        "Barras de 40, 60, 80, 100 y 140; frases: la llegada de plata aumenta; la tabla no prueba que fuera por las medidas del consejero.",
        ["las barras son proporcionales", "describe la tendencia", "explica el límite"], ["gráfico", "dos frases"], ["barras de alturas incorrectas", "afirmar que la carta causó el aumento"],
        "Pide que diga qué fuente agregaría para comprobar la causa."),
    reinforce="Explica con tus palabras la diferencia entre una opinión y un dato en estas fuentes.",
    extend="Escribe dos preguntas que harías a quien llevaba el registro de llegada de plata.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (rutas del comercio mundial en el siglo XVI, simplificadas). Ruta del Atlántico: Sevilla, en España, con Veracruz, en el actual México, y con Portobelo, en el actual Panamá; lleva manufacturas y trae plata y productos americanos. "
     "Ruta del Pacífico: Manila, en las Filipinas, con Acapulco, en México; trae sedas y porcelanas de Asia y lleva plata americana. "
     "Ruta del Índico: Lisboa, en Portugal, con Goa, en la India, rodeando África por el cabo de Buena Esperanza; trae especias. "
     "Antes de 1500 gran parte del comercio con Asia pasaba por el mar Mediterráneo, con ciudades como Venecia y Génova. Después de 1500, ciudades del Atlántico como Sevilla, Lisboa, Ámsterdam y Londres ganaron importancia.")
build(
    OA, 3, F,
    use="Aprenderé a describir las rutas comerciales del siglo XVI y a explicar qué cambió y qué continuó en el comercio europeo al expandirse por el mundo.",
    prior=["Sé ubicar continentes y océanos.", "Conozco los fenómenos del mercantilismo.", "Sé distinguir cambio y continuidad."],
    explain=[
        "La ampliación de las rutas comerciales y la expansión mundial de la economía europea se ven en el mapa. Por el Atlántico, naves iban de Sevilla a Veracruz y Portobelo y volvían con plata y productos de América. Por el Pacífico, naves unían Manila con Acapulco y traían sedas y porcelanas de Asia. Por el Índico, Portugal unía Lisboa con Goa, en la India, rodeando África.",
        "El cambio principal fue el desplazamiento de los centros del comercio. Antes de 1500, ciudades del Mediterráneo como Venecia y Génova concentraban el comercio con Asia. Después, ciudades atlánticas como Sevilla, Lisboa, Ámsterdam y Londres ganaron importancia, porque desde ellas salían las naves hacia otros continentes.",
        "También hubo continuidades: se seguían comerciando especias y telas, existían ferias y ciudades mercantiles, y los comerciantes dependían de permisos de los reyes. No todo el mundo participó de la misma manera: América, Asia y África aportaron productos y personas, pero en estas rutas europeas las decisiones principales las tomaban los Estados y las compañías de Europa.",
    ],
    vocab=[("manufactura", "producto fabricado, como telas o herramientas"), ("especia", "producto vegetal como pimienta o canela que se usa para dar sabor"), ("cabo de Buena Esperanza", "extremo sur de África que se bordea para ir de Europa a la India por mar"), ("puerto", "lugar de la costa donde llegan y salen barcos"), ("Mediterráneo", "mar entre Europa, África y Asia")],
    worked=[
        ("Leer una ruta", "Según la ficha, ¿qué trae la ruta del Pacífico desde Manila hasta Acapulco?", ["Leo la ruta del Pacífico.", "Dice que trae sedas y porcelanas de Asia."], "Sedas y porcelanas de Asia"),
        ("Clasificar cambio y continuidad", "Después de 1500, Sevilla gana importancia y se siguen vendiendo especias. ¿Qué es cambio y qué continuidad?", ["Sevilla gana importancia: cambio.", "Las especias se siguen vendiendo: continuidad."], "Cambio: la importancia de Sevilla; continuidad: el comercio de especias"),
    ],
    mistakes=[("Pensar que todas las rutas salían de un solo puerto.", "Se ignora la variedad de rutas y ciudades.", "Nombra la ruta, los puertos de salida y de llegada."),
              ("Creer que el comercio mundial empezó de cero en 1500.", "Se ignora el comercio anterior con Asia por el Mediterráneo.", "Distingue lo que cambió y lo que continuó.")],
    T=[
        ("{F} ¿Qué puerto español sale en la ruta del Atlántico?", "Sevilla", "La ficha lo indica."),
        ("{F} ¿Qué producto trae la ruta del Índico a Lisboa?", "Especias", "Está en la ficha."),
        ("{F} ¿Qué ciudad de la India aparece en la ruta del Índico?", "Goa", "Figura en la ficha."),
        ("{F} ¿Qué ruta une Manila con Acapulco?", "La del Pacífico", "La ficha la nombra así."),
        ("{F} Clasifica cada puerto con su ruta: a) Veracruz, b) Goa, c) Manila.", "a) Atlántico; b) Índico; c) Pacífico", "Cada puerto aparece en la ruta que lo menciona."),
        ("=", "{F} Una línea de tiempo usa 1 cm = 25 años. ¿A cuántos cm de 1500 queda 1600?", "(1600-1500)//25", "Se divide la diferencia de años por la escala.", " cm"),
        ("{F} ¿Qué ciudades ganaron importancia después de 1500? A) Sevilla, Lisboa, Ámsterdam y Londres B) Venecia y Génova únicamente", "A) Sevilla, Lisboa, Ámsterdam y Londres", "Son las atlánticas que cita la ficha."),
        ("{F} ¿Por qué cambió el centro del comercio de Europa?", "Porque las naves salían hacia otros continentes desde puertos del Atlántico", "Las nuevas rutas favorecieron a las ciudades atlánticas."),
        ("{F} Clasifica como cambio o continuidad: a) Sevilla gana importancia, b) se siguen comerciando especias, c) los comerciantes necesitan permiso del rey.", "a) cambio; b) continuidad; c) continuidad", "Solo el desplazamiento de los centros es nuevo."),
        ("{F} Un mapa muestra solo flechas de Europa hacia otros continentes. ¿Qué omite? A) Los productos que volvían a Europa, como plata y sedas B) Los países de Asia", "A) Los productos que volvían a Europa, como plata y sedas", "Las rutas eran de ida y vuelta."),
        ("{F} ¿Por qué se dice que la economía europea se expandió por el mundo?", "Porque sus rutas conectaron Europa con América, Asia y África", "Las tres rutas de la ficha lo muestran."),
        ("{F} Un compañero dice: «Antes de 1500 Europa no comerciaba con Asia». ¿Qué dato de la ficha lo contradice?", "Gran parte del comercio con Asia pasaba por el Mediterráneo, con Venecia y Génova", "La ficha describe un comercio anterior."),
        ("{F} ¿Quiénes tomaban las decisiones principales en las rutas europeas de la ficha?", "Los Estados y compañías de Europa", "La explicación señala que en estas rutas decidían los Estados y compañías de Europa."),
    ],
    ctx=("Un guía quiere explicar por qué la plata de América llegó a Asia. Con la ficha, ¿qué ruta nombra? {F}", "La ruta del Pacífico, de Acapulco a Manila", "La ficha dice que esa ruta lleva plata americana."),
    sc=[("¿Qué ruta rodea África para llegar a la India?", "La del Índico", "Lisboa-Goa rodea África."),
        ("¿Qué mar concentraba el comercio con Asia antes de 1500?", "El Mediterráneo", "Lo dice la ficha."),
        ("¿Qué trae la ruta del Atlántico de vuelta a Sevilla? A) Plata y productos americanos B) Sedas y porcelanas", "A) Plata y productos americanos", "La ficha lo indica para el Atlántico.")],
    op=("Dibuja un croquis del mundo con cuatro puntos: Sevilla, Veracruz, Manila y Goa. Une con flechas de tres colores las tres rutas de la ficha. Al lado de cada flecha escribe un producto que viaja. Escribe una frase sobre un cambio y otra sobre una continuidad. {F}",
        "Atlántico: Sevilla-Veracruz con plata; Pacífico: Manila-Acapulco con seda; Índico: Lisboa-Goa con especias. Cambio: ganan importancia ciudades atlánticas. Continuidad: se siguen comerciando especias.",
        ["tres flechas de rutas", "un producto por ruta", "un cambio y una continuidad"], ["croquis", "dos frases"], ["mezclar las rutas", "decir que no había comercio antes de 1500"],
        "Pide que explique por qué las ciudades del Mediterráneo perdieron importancia."),
    reinforce="Cuenta una ruta de la ficha diciendo su origen, su destino y un producto.",
    extend="Escribe una pregunta sobre cómo vivían los marineros que cruzaban esas rutas.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno; no son testimonios reales). "
     "Voz 1, comerciante de Sevilla, 1580: «Llega plata, pero los precios suben y mis clientes compran menos.» "
     "Voz 2, noble que vive de rentas fijas, 1580: «Cobro lo mismo que mi abuelo, pero todo me cuesta más; me empobrezco.» "
     "Voz 3, trabajador de un taller, 1580: «Mi sueldo sube menos que el pan.» "
     "Voz 4, capitán de una compañía comercial de los Países Bajos, 1605: «Mi compañía disputa a los portugueses el comercio de especias; mientras más naves, más competencia.» "
     "Causas de la subida de precios que mencionan los historiadores: llegada de mucha plata; aumento de la población; mayor demanda de alimentos y productos; y guerras que elevaron los gastos de los Estados.")
build(
    OA, 4, F,
    use="Aprenderé a explicar la revolución de los precios y el aumento de la competencia con varias causas, y a contrastar cómo la vivían distintos actores.",
    prior=["Conozco el mercantilismo y sus rutas.", "Sé que un hecho puede tener varias causas.", "Sé qué es una perspectiva."],
    explain=[
        "La revolución de los precios fue una larga alza de precios en Europa durante el siglo XVI. No ocurrió de un día para otro: los precios subieron poco a poco durante décadas. Entre las causas están la llegada de mucha plata americana, el aumento de la población, que demandaba más alimentos, y los gastos de las guerras. Una sola causa no la explica por completo.",
        "Los actores la vivieron de distinta manera. Un comerciante podía ganar o perder según si sus clientes podían comprar. Un noble con rentas fijas, es decir, que recibía siempre la misma cantidad, perdía poder de compra. Un trabajador veía que su sueldo subía menos que el precio del pan.",
        "La competencia también aumentó: varios Estados y compañías, como las de las Indias Orientales de Inglaterra y los Países Bajos, disputaron rutas y productos a Portugal y España. Quien quiere explicar la época debe combinar causas y perspectivas, no elegir solo una.",
    ],
    vocab=[("revolución de los precios", "larga alza de precios en Europa durante el siglo XVI"), ("renta fija", "ingreso que se recibe siempre en la misma cantidad"), ("poder de compra", "cantidad de cosas que se pueden comprar con un ingreso"), ("competencia", "situación en que varios actores disputan el mismo mercado"), ("demanda", "cantidad de un producto que la gente quiere comprar")],
    worked=[
        ("Identificar una causa", "¿Qué causa de la ficha relaciona la llegada de metales con la subida de precios?", ["Leo las causas.", "La primera es la llegada de mucha plata."], "La llegada de mucha plata americana"),
        ("Calcular una pérdida de poder de compra", "Un noble cobra siempre 100 monedas. Si el pan que costaba 2 monedas pasa a costar 4, ¿cuántos panes compra antes y después?", ["Antes: 100 ÷ 2 = 50 panes.", "Después: 100 ÷ 4 = 25 panes."], "De 50 a 25 panes"),
    ],
    mistakes=[("Explicar la subida de precios solo por la plata.", "Se ignoran población, demanda y guerras.", "Nombra al menos tres causas."),
              ("Creer que todos perdían por igual con la subida de precios.", "Se olvida que algunos actores ganaban y otros perdían.", "Compara al comerciante con el noble y el trabajador.")],
    T=[
        ("{F} ¿Quién dice que vive de rentas fijas?", "El noble", "Es la voz 2."),
        ("{F} ¿Qué dice el trabajador sobre su sueldo?", "Que sube menos que el pan", "Es la voz 3."),
        ("{F} ¿Con quién disputa el capitán holandés el comercio de especias?", "Con los portugueses", "La voz 4 lo dice."),
        ("=", "{F} Un noble cobra siempre 120 monedas. Si el pan que valía 2 monedas pasa a valer 3, ¿cuántos panes menos puede comprar?", "120//2-120//3", "Antes compraba 60 y ahora 40.", " panes"),
        ("{F} ¿Cuál de estas es una causa de la revolución de los precios? A) El aumento de la población B) La disminución de la población", "A) El aumento de la población", "La ficha lo incluye entre las causas."),
        ("{F} ¿Quién pierde poder de compra con la subida de precios: el noble con renta fija o un comerciante que sube sus precios?", "El noble con renta fija", "Su ingreso no sube mientras todo cuesta más."),
        ("{F} Clasifica cada causa como relacionada con metales, población o guerras: a) llegada de plata, b) más gente que demanda alimentos, c) gastos de los Estados en guerras.", "a) metales; b) población; c) guerras", "Cada causa es una de las tres de la lista."),
        ("{F} ¿Qué fenómeno del OA ilustra la voz del capitán de los Países Bajos?", "El aumento de la competencia", "Habla de disputar el comercio y más naves."),
        ("=", "{F} Si hacia 1580 un trabajador gana 30 monedas y el pan cuesta 3, ¿cuántos panes compra con su sueldo?", "30//3", "Se divide el sueldo por el precio del pan.", " panes"),
        ("{F} Un compañero dice: «La subida de precios la causó solo la plata». ¿Qué otra causa de la ficha le opones?", "El aumento de la población o la mayor demanda o las guerras", "La ficha menciona varias causas."),
        ("{F} ¿Por qué el comerciante de la voz 1 y el trabajador de la voz 3 pueden sentir de forma distinta la subida de precios?", "Porque tienen ingresos distintos y no sufren igual el alza", "Cada actor ve el proceso desde su posición."),
        ("{F} ¿Qué conclusión es proporcional? A) La subida de precios tuvo varias causas y afectó de manera distinta a cada grupo B) Todos se empobrecieron por igual", "A) La subida de precios tuvo varias causas y afectó de manera distinta a cada grupo", "Las voces muestran efectos distintos."),
        ("{F} ¿Qué dato necesitarías para saber si los sueldos subieron menos que los precios en toda Europa?", "Registros de sueldos y de precios de muchas ciudades", "Se necesitan series de datos amplias."),
    ],
    ctx=("Un maestro pregunta al curso: «¿Permite la ficha afirmar quién sale ganando con la competencia entre compañías comerciales?». Responde con la voz 4 y la voz 1. {F}", "No: la voz 4 solo muestra más disputa por el comercio y la voz 1 habla de precios que suben, sin datos de ganancias", "Ninguna voz entrega datos de ganancias, así que no hay base para decidir un ganador."),
    sc=[("¿Qué es la revolución de los precios?", "Una larga alza de precios en Europa en el siglo XVI", "Así se definió."),
        ("¿Qué actor tiene renta fija?", "El noble", "Es la voz 2."),
        ("¿Qué aumentó cuando varios Estados quisieron las mismas rutas? A) La competencia B) La renta fija", "A) La competencia", "Más actores disputaban el mismo comercio.")],
    op=("Escribe un diálogo de seis líneas entre el noble y el trabajador de la ficha sobre la subida del pan. Cada uno debe usar un dato de su voz y uno de los dos debe nombrar una causa de la lista. Cierra con una frase tuya sobre en qué se parece y en qué se diferencia su situación. {F}",
        "Noble: cobro lo mismo que mi abuelo y todo cuesta más. Trabajador: mi sueldo sube menos que el pan. Causa: llegó mucha plata. Cierre: ambos pierden poder de compra, pero el noble tiene renta fija.",
        ["usa datos de las voces", "nombra una causa", "cierra comparando"], ["diálogo", "frase de cierre"], ["inventar datos que contradicen la ficha", "atribuir todo a una causa"],
        "Pide que explique qué voz falta y por qué importaría."),
    reinforce="Explica con tus palabras qué es la revolución de los precios y nombra dos causas.",
    extend="Escribe una pregunta que le harías a un comerciante de 1580 sobre los precios.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (pregunta y datos de ejemplo). Pregunta: ¿por qué subieron los precios en Europa durante el siglo XVI? "
     "Índice de precios de ejemplo, con el año 1500 igual a 100: 1500: 100; 1550: 180; 1600: 300. Población de ejemplo en millones de habitantes: 1500: 80; 1550: 95; 1600: 110. Plata de ejemplo llegada a Europa, en toneladas por periodo de cincuenta años: 1500-1549: 20; 1550-1599: 60. "
     "Dato: en las mismas décadas hubo guerras caras entre Estados europeos. "
     "Criterio de la clase: una explicación es sólida si usa más de una causa y cada causa se apoya en un dato.")
build(
    OA, 5, F,
    use="Aprenderé a construir un argumento multicausal sobre la revolución de los precios, apoyado en datos de ejemplo, y a reconocer lo que esos datos no prueban.",
    prior=["Conozco las causas de la revolución de los precios.", "Sé que un argumento tiene tesis, evidencias y límite.", "Sé leer tablas de datos."],
    explain=[
        "Para explicar por qué subieron los precios en el siglo XVI no basta con elegir una causa. Una explicación multicausal combina varios factores y los apoya en datos. En la ficha hay tres series de ejemplo: el índice de precios, la población y la plata que llegó. Las tres crecen en el mismo periodo, lo que hace plausible que se relacionen.",
        "Pero que dos cosas crezcan juntas no prueba que una cause la otra. Para sostener un argumento hay que explicar el mecanismo: más plata en circulación significa más dinero para comprar los mismos productos; más población significa más demanda de alimentos; las guerras elevan los gastos y los impuestos. Cada mecanismo se escribe con una razón, no solo con una cifra.",
        "Un buen argumento cierra con un límite. Los datos de la ficha son de ejemplo y no distinguen entre regiones; en algunos lugares los precios subieron más que en otros. Reconocer eso es parte del trabajo del historiador.",
    ],
    vocab=[("índice de precios", "número que compara los precios de un año con los de un año base"), ("mecanismo", "forma en que una causa produce un efecto"), ("multicausal", "que combina varias causas"), ("correlación", "dos datos que cambian juntos sin que eso pruebe que uno causa al otro"), ("serie de datos", "conjunto de datos ordenados en el tiempo")],
    worked=[
        ("Leer un índice", "Si el índice de precios de 1500 es 100 y el de 1600 es 300, ¿cuántas veces mayor era el índice de 1600 que el de 1500?", ["Divido 300 entre 100.", "El resultado es 3."], "3 veces mayor"),
        ("Explicar un mecanismo", "¿Cómo puede el aumento de la población subir los precios?", ["Más gente necesita más alimentos.", "Si hay pocos alimentos, su precio sube."], "Mayor demanda de alimentos eleva su precio"),
    ],
    mistakes=[("Concluir que dos series que crecen juntas se causan mutuamente.", "Se confunde correlación con causa.", "Explica un mecanismo y busca otras causas."),
              ("Citar solo una cifra para sostener toda la explicación.", "Una cifra aislada no prueba una causa.", "Usa al menos dos causas y datos de cada una.")],
    T=[
        ("{F} ¿Cuál era el índice de precios en 1550?", "180", "Está en la ficha."),
        ("{F} ¿Cuál era la población de ejemplo en 1600?", "110 millones", "Aparece en la ficha."),
        ("{F} ¿Cuántas toneladas de plata llegaron entre 1550 y 1599?", "60", "Es el dato del periodo."),
        ("=", "{F} ¿Cuántas veces mayor fue la plata llegada entre 1550 y 1599 que la de 1500 a 1549?", "60//20", "Se divide el segundo periodo por el primero.", " veces"),
        ("=", "{F} ¿Cuántos puntos subió el índice de precios entre 1500 y 1600?", "300-100", "Se resta el índice inicial al final.", " puntos"),
        ("=", "{F} ¿Cuántos millones de habitantes más había en 1600 que en 1500?", "110-80", "Se resta la población inicial a la final.", " millones"),
        ("{F} ¿Qué causa se apoya en el dato de la población? A) Mayor demanda de alimentos B) Menos plata en circulación", "A) Mayor demanda de alimentos", "Más gente significa más demanda."),
        ("{F} Un compañero dice: «Como la plata aumentó, ella explica todo». ¿Qué le falta según el criterio de la clase?", "Usar más de una causa y apoyar cada una con un dato", "El criterio exige varias causas."),
        ("{F} ¿Qué mecanismo une la plata con los precios?", "Más dinero en circulación para comprar los mismos productos", "Más dinero con pocas mercancías eleva los precios."),
        ("{F} ¿Por qué la correlación entre población y precios no prueba por sí sola una causa?", "Porque dos datos pueden crecer juntos por otras razones", "Falta explicar un mecanismo."),
        ("{F} ¿Qué dato de la ficha apoya la causa de las guerras?", "Que hubo guerras caras entre Estados europeos en las mismas décadas", "Es el dato que se menciona."),
        ("{F} Escribe un límite honesto para el argumento de la ficha.", "Los datos son de ejemplo y no distinguen entre regiones", "El límite reconoce lo que no se puede concluir."),
        ("{F} ¿Qué tesis se apoya mejor en la ficha? A) Los precios subieron por varias causas: plata, población y guerras B) Los precios subieron solo por la plata, sin importar otras causas", "A) Los precios subieron por varias causas: plata, población y guerras", "Hay datos para varias causas."),
    ],
    ctx=("Un concurso pide una explicación de la subida de precios en una frase con dos causas. {F}", "Los precios subieron porque llegó mucha plata y porque creció la población que demandaba alimentos", "Combina dos causas apoyadas por datos de la ficha."),
    sc=[("¿Qué significa multicausal?", "Que combina varias causas", "Se definió en el vocabulario."),
        ("¿Qué es un límite en un argumento?", "Lo que los datos no permiten concluir", "Se explicó en la clase."),
        ("=", "El índice de precios fue 180 en 1550 y 300 en 1600. ¿Cuántos puntos subió?", "300-180", "Se resta el índice anterior al posterior.", " puntos")],
    op=("Escribe un párrafo de seis líneas con tu tesis sobre por qué subieron los precios en el siglo XVI. Debe incluir dos causas, un dato de la ficha para cada una, el mecanismo de una de ellas y un límite. {F}",
        "Pienso que subieron por varias causas. Plata: de 20 a 60 toneladas, más dinero para los mismos productos. Población: de 80 a 110 millones, más demanda. Límite: los datos son de ejemplo y no distinguen regiones.",
        ["tiene tesis", "dos causas con datos", "explica un mecanismo y un límite"], ["párrafo"], ["usar una sola causa", "concluir causa solo por correlación"],
        "Pide que diga qué dato nuevo buscaría para mejorar su explicación."),
    reinforce="Di en voz alta dos causas de la revolución de los precios y un dato para cada una.",
    extend="Escribe una pregunta sobre cómo cambiaron los precios en un lugar donde no llegó plata.",
)
