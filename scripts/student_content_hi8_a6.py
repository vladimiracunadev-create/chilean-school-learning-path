"""Material del estudiante de 8.º básico, Historia, Geografía y Ciencias Sociales: OA 06 (conquista y caída de imperios americanos)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI08 OA 06"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (cronología simplificada). Imperio mexica: 1519, Hernán Cortés desembarca en la costa de México con unos 500 hombres y se une a pueblos enemigos de los mexicas; 1520, una epidemia de viruela afecta a Tenochtitlan; 1521, cae Tenochtitlan. "
     "Imperio inca: hacia 1529-1532, guerra civil entre los hermanos Huáscar y Atahualpa; 1532, Francisco Pizarro, con unos 170 hombres, captura al Inca Atahualpa en Cajamarca; 1533, los españoles entran en Cusco. "
     "Mapuche: 1541, Pedro de Valdivia funda Santiago; 1553, Valdivia muere en combate contra los mapuche y la guerra continúa durante décadas.")
build(
    OA, 1, F,
    use="Aprenderé a situar la conquista de los grandes imperios americanos en el tiempo y en el espacio y a plantear por qué fue tan rápida.",
    prior=["Conozco a los mexicas, incas y mapuche.", "Sé calcular diferencias entre años.", "Conozco el encuentro entre culturas."],
    explain=[
        "El OA pide analizar los factores que explican la rapidez de la conquista y la caída de los grandes imperios americanos. «Rapidez» significa que, en pocos años, dos imperios muy extensos pasaron a ser controlados por pequeños grupos de españoles y sus aliados. El imperio mexica cayó en 1521, a solo dos años de la llegada de Cortés. El imperio inca perdió a su Inca en 1532 y su capital, Cusco, fue ocupada en 1533.",
        "Para situar la conquista conviene ubicar las fechas y los lugares: Veracruz y Tenochtitlan en México; Cajamarca y Cusco en los Andes. También hay que notar que no todo fue igual: en el sur de Chile, los mapuche no fueron derrotados con rapidez y la guerra continuó durante décadas. Esa diferencia ayuda a ver que hubo factores propios de cada caso.",
        "Los cuatro factores del OA serán nuestro hilo: la organización política de los imperios, la forma de hacer la guerra, los intereses de los conquistadores y la catástrofe demográfica, es decir, la gran disminución de la población indígena. Hay que evitar una explicación única: la conquista no se explica solo por la superioridad militar europea.",
    ],
    vocab=[("conquista", "dominio de un territorio y su población por la fuerza"), ("imperio", "Estado extenso que gobierna a varios pueblos"), ("epidemia", "enfermedad que se propaga rápido entre muchas personas"), ("catástrofe demográfica", "gran disminución de la población"), ("aliado", "grupo que se une a otro para un fin común")],
    worked=[
        ("Calcular la rapidez", "Según la ficha, ¿cuántos años pasaron entre la llegada de Cortés a México y la caída de Tenochtitlan?", ["Busco los años: 1519 y 1521.", "Resto: 1521 − 1519 = 2."], "2 años"),
        ("Comparar dos casos", "Valdivia fundó Santiago en 1541 y murió en 1553. ¿Cuántos años pasaron, y qué indica sobre la rapidez de la conquista mapuche?", ["Resto: 1553 − 1541 = 12.", "En ese tiempo no se había controlado el territorio mapuche."], "12 años; la conquista mapuche no fue rápida"),
    ],
    mistakes=[("Pensar que toda América cayó con la misma rapidez.", "Se ignora la resistencia prolongada de otros pueblos.", "Compara mexicas, incas y mapuche."),
              ("Explicar la conquista solo por la superioridad militar.", "Se olvidan alianzas, guerra civil y epidemias.", "Nombra los cuatro factores del OA.")],
    T=[
        ("{F} ¿En qué año cayó Tenochtitlan?", "1521", "Es el año indicado."),
        ("{F} ¿Dónde fue capturado Atahualpa?", "En Cajamarca", "La ficha lo indica."),
        ("{F} ¿Qué hermanos se enfrentaron en la guerra civil inca?", "Huáscar y Atahualpa", "La ficha los nombra."),
        ("=", "{F} ¿Cuántos años pasaron entre la captura de Atahualpa y la entrada de los españoles en Cusco?", "1533-1532", "Se resta el primer año al segundo.", " año"),
        ("=", "{F} ¿Cuántos años pasaron entre la caída de Tenochtitlan y la captura de Atahualpa?", "1532-1521", "Se restan los dos años.", " años"),
        ("{F} ¿A qué siglo pertenecen todas las fechas de conquista de la ficha?", "Siglo XVI", "Van de 1519 a 1553, dentro del siglo XVI."),
        ("{F} Ordena de más antiguo a más reciente: muerte de Valdivia, captura de Atahualpa, desembarco de Cortés, fundación de Santiago.", "Desembarco de Cortés, captura de Atahualpa, fundación de Santiago, muerte de Valdivia", "Los años son 1519, 1532, 1541 y 1553."),
        ("{F} Clasifica cada dato con el imperio al que pertenece: a) guerra civil entre Huáscar y Atahualpa, b) epidemia de viruela en 1520 en Tenochtitlan. Opciones: inca, mexica.", "a) inca; b) mexica", "Cada dato está en la ficha dentro de ese imperio."),
        ("=", "{F} Una línea de tiempo usa 1 cm = 5 años y parte en 1519. ¿A cuántos cm queda 1553, redondeando hacia abajo?", "(1553-1519)//5", "Se divide la diferencia de años por la escala.", " cm"),
        ("{F} ¿Por qué la conquista mapuche no fue rápida, según la ficha?", "Porque Valdivia murió en combate en 1553 y la guerra continuó durante décadas", "La ficha muestra una resistencia prolongada."),
        ("{F} Un compañero dice: «Cortés conquistó México con solo 500 hombres». ¿Qué dato de la ficha corrige su afirmación?", "Cortés se unió a pueblos enemigos de los mexicas y hubo una epidemia", "No actuó solo."),
        ("{F} ¿Qué afirmación es correcta? A) La conquista fue rápida en los imperios mexica e inca, pero más lenta entre los mapuche B) Fue igual de rápida en todos los territorios", "A) La conquista fue rápida en los imperios mexica e inca, pero más lenta entre los mapuche", "Las fechas lo muestran."),
        ("{F} ¿Qué pregunta problema plantea esta clase?", "Por qué la conquista y caída de los imperios americanos fue tan rápida", "Es el problema del OA."),
    ],
    ctx=("Una compañera dice: «Los españoles conquistaron América en dos años». ¿Qué datos de la ficha le sirven para corregirla? {F}", "Tenochtitlan cayó en 1521, pero los incas en 1532-1533 y los mapuche resistieron más de una década", "Las fechas muestran que no fue igual en todos lados."),
    sc=[("¿Qué es una epidemia?", "Una enfermedad que se propaga rápido entre muchas personas", "Se definió en el vocabulario."),
        ("¿Qué año murió Valdivia según la ficha?", "1553", "Es el dato de la ficha."),
        ("=", "¿Cuántos años pasaron entre 1519 y 1533?", "1533-1519", "Se resta el año de Cortés al de Cusco.", " años")],
    op=("Dibuja una línea de tiempo con 1 cm = 5 años desde 1515 hasta 1555. Marca los hechos de la ficha de México, de los Andes y de Chile con tres colores. Debajo escribe una frase que explique por qué el caso mapuche no calza con la idea de «conquista rápida». {F}",
        "México (1519, 1520, 1521) en un color; Andes (1532, 1533) en otro; Chile (1541, 1553) en otro. Frase: «Los mapuche resistieron más de una década sin ser derrotados».",
        ["respeta la escala", "usa colores por zona", "explica el caso mapuche"], ["línea de tiempo", "frase"], ["mezclar los colores", "decir que todos cayeron igual de rápido"],
        "Pide que explique qué factor podría explicar la diferencia."),
    reinforce="Nombra los cuatro factores que el OA pide analizar.",
    extend="Escribe una pregunta que le harías a un historiador para saber por qué los mapuche resistieron más tiempo.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, carta de un capitán español de ejemplo al rey, 1521: «Con pocos hombres y gran esfuerzo hemos vencido a un gran imperio. Pedimos que Su Majestad nos premie con tierras y servicio de los habitantes.» "
     "Fuente B, relato de un habitante de una ciudad vecina de ejemplo, escrito décadas después y traducido: «Muchos de nosotros nos unimos a los extranjeros porque queríamos dejar de pagar tributos a los dominadores. Después llegó una enfermedad y murió mucha gente.»")
build(
    OA, 2, F,
    use="Aprenderé a analizar una carta de conquistador y un relato indígena, a detectar el interés de cada autor y a reconocer qué factores de la conquista aparecen en las fuentes.",
    prior=["Sé contextualizar una fuente.", "Conozco los factores de la conquista.", "Sé distinguir hecho y opinión."],
    explain=[
        "Una carta de un capitán al rey es una fuente escrita con un propósito claro: pedir premios. Por eso el autor puede exagerar sus logros y mostrar que venció con pocos hombres. Para contextualizar hay que preguntar quién escribe, a quién, cuándo y qué quiere conseguir. Aquí el capitán pide tierras y servicio de los habitantes.",
        "El relato indígena de ejemplo fue escrito décadas después y traducido. Muestra otra perspectiva: algunos grupos se unieron a los extranjeros porque querían dejar de pagar tributos. También menciona una enfermedad que causó muchas muertes. Estos datos apuntan a factores del OA: organización política con pueblos descontentos y catástrofe demográfica.",
        "Ninguna fuente basta por sí sola. La carta resalta el esfuerzo militar y oculta el papel de los aliados; el relato indígena explica las alianzas, pero fue escrito mucho después y puede mezclar recuerdos. Comparar ambas permite una conclusión más cuidadosa.",
    ],
    vocab=[("tributo", "pago que un pueblo entrega a quien lo domina"), ("capitán", "jefe de un grupo armado"), ("propósito", "lo que quiere conseguir quien escribe"), ("sesgo", "inclinación de una fuente por los intereses de su autor"), ("traducción", "paso de un texto a otro idioma, con posible pérdida de matices")],
    worked=[
        ("Detectar el propósito", "¿Qué quiere conseguir el capitán de la Fuente A con su carta?", ["Leo el final de la carta.", "Pide tierras y servicio de los habitantes."], "Un premio de tierras y servicio de habitantes"),
        ("Relacionar fuente y factor", "¿Qué factor del OA aparece cuando el relato dice «queríamos dejar de pagar tributos»?", ["Hay pueblos descontentos con el imperio.", "Eso se relaciona con la organización política."], "La organización política y los descontentos"),
    ],
    mistakes=[("Creer que la carta del capitán cuenta toda la verdad.", "Su autor tiene interés en mostrarse héroe.", "Busca otra fuente que cuente el papel de los aliados."),
              ("Tomar el relato indígena como si lo hubiera escrito alguien de un único pueblo.", "No se especifica a qué grupo pertenece.", "Nombra el pueblo o lugar de origen de la fuente cuando se conoce.")],
    T=[
        ("{F} ¿Quién escribe la Fuente A?", "Un capitán español", "La ficha lo indica."),
        ("{F} ¿Qué pide el capitán al rey?", "Tierras y el servicio de los habitantes", "Lo dice la carta."),
        ("{F} ¿Por qué se unieron algunos grupos a los extranjeros según la Fuente B?", "Para dejar de pagar tributos a los dominadores", "La fuente lo explica."),
        ("{F} ¿Qué otro hecho menciona la Fuente B que causó muchas muertes?", "Una enfermedad", "La fuente dice que llegó una enfermedad."),
        ("{F} ¿Qué fuente fue escrita más cerca de los hechos, la A o la B?", "La A, porque es de 1521 y la B se escribió décadas después", "La carta es de 1521 y el relato es posterior."),
        ("{F} ¿Qué rasgo del propósito del capitán puede sesgar su carta? A) Quiere que lo premien, así que puede exagerar su éxito B) Escribe para entretener", "A) Quiere que lo premien, así que puede exagerar su éxito", "El interés del autor influye en lo que cuenta."),
        ("{F} Clasifica: a) «Pedimos que Su Majestad nos premie», b) «Con pocos hombres hemos vencido a un gran imperio». ¿Cuál es una petición y cuál una afirmación que destaca el mérito del autor?", "a) petición; b) afirmación que destaca su mérito", "La primera pide un premio; la segunda resalta lo que el autor logró."),
        ("{F} ¿Qué factor del OA aparece en la frase «Muchos de nosotros nos unimos a los extranjeros»?", "La organización política y las alianzas", "Los grupos descontentos se aliaron."),
        ("{F} ¿Qué factor del OA aparece en la frase «llegó una enfermedad y murió mucha gente»?", "La catástrofe demográfica", "La enfermedad redujo la población."),
        ("{F} Un compañero dice: «La carta prueba que unos pocos españoles vencieron solos». ¿Qué falla?", "La carta es del capitán, tiene interés en mostrarse héroe y la otra fuente habla de aliados", "Falta contrastar con la fuente B."),
        ("{F} ¿Qué límite tiene la Fuente B? A) Fue escrita décadas después y traducida B) Fue escrita el mismo día de los hechos", "A) Fue escrita décadas después y traducida", "El paso del tiempo y la traducción pueden cambiar detalles."),
        ("{F} ¿Qué conclusión es proporcional al comparar las dos fuentes? A) La conquista tuvo factores militares, alianzas y enfermedades B) Solo hubo factores militares", "A) La conquista tuvo factores militares, alianzas y enfermedades", "Ambas fuentes aportan factores distintos."),
        ("{F} ¿Qué otra fuente ayudaría a medir la mortalidad? A) Registros de población de la época y estudios actuales B) La carta del capitán al rey", "A) Registros de población de la época y estudios actuales", "Permiten comparar cifras antes y después."),
    ],
    ctx=("Una profesora pide un titular para un trabajo que use ambas fuentes. ¿Cuál es más proporcional? A) «La conquista se explica por armas, alianzas y enfermedades» B) «Pocos soldados vencieron solos a un imperio»", "A) «La conquista se explica por armas, alianzas y enfermedades»", "El titular A recoge ambas fuentes."),
    sc=[("¿Qué es un tributo?", "Un pago que un pueblo entrega a quien lo domina", "Se definió en el vocabulario."),
        ("¿Qué es un sesgo?", "La inclinación de una fuente por los intereses de su autor", "Se definió en el vocabulario."),
        ("¿Qué fuente muestra el descontento de grupos con el imperio? A) La Fuente B B) La Fuente A", "A) La Fuente B", "El relato indígena menciona los tributos.")],
    op=("Haz una tabla con las dos fuentes y cuatro filas: autor, fecha, propósito y un factor del OA que muestra. Escribe después dos frases: una descripción de la Fuente A y una interpretación que no exagere. {F}",
        "A: capitán español, 1521, pedir premios, fuerza militar. B: habitante de ciudad vecina, décadas después, contar lo vivido, alianzas y enfermedad. Descripción: el capitán pide tierras. Interpretación: quería premios, por eso pudo destacar su mérito; falta contrastar con otras fuentes.",
        ["completa las cuatro filas", "separa descripción e interpretación", "nombra un factor"], ["tabla", "dos frases"], ["tomar la carta como verdad completa", "no distinguir autor y fecha"],
        "Pide que diga qué otra fuente buscaría para el papel de los aliados."),
    reinforce="Explica a otra persona por qué la carta de un capitán puede tener un sesgo.",
    extend="Escribe una pregunta que le harías al autor de la Fuente B.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (rutas y cambios, simplificados). Ruta de Cortés: desembarco en la costa de Veracruz (1519), marcha hacia el interior, alianzas con pueblos como los tlaxcaltecas y llegada al valle de México, donde está Tenochtitlan, ciudad en una isla del lago de Texcoco. "
     "Ruta de Pizarro: desde Panamá hacia el sur por la costa del Pacífico, subida a los Andes, Cajamarca (1532) y Cusco (1533). "
     "Cambios después de la caída: las capitales pasan a ser controladas por españoles; se fundan ciudades españolas; muchos tributos se pagan ahora a la Corona y a los conquistadores. "
     "Continuidades: la mayoría de la población sigue viviendo en comunidades y cultivando la tierra; los pueblos conservan sus lenguas; algunas autoridades locales, llamadas caciques, siguen mediando entre su pueblo y los españoles.")
build(
    OA, 3, F,
    use="Aprenderé a describir el recorrido de la conquista en el territorio y a distinguir qué cambió y qué continuó en los pueblos después de la caída de los imperios.",
    prior=["Sé ubicar México, Perú y Chile.", "Conozco los factores de la conquista.", "Sé distinguir cambio y continuidad."],
    explain=[
        "El territorio explica parte de la conquista. Cortés avanzó desde la costa de Veracruz hasta el valle de México, donde estaba Tenochtitlan, con ayuda de pueblos aliados. Pizarro avanzó por el Pacífico desde Panamá y subió los Andes hasta Cajamarca y Cusco. En ambos casos, los españoles llegaron al corazón político del imperio y lo desorganizaron.",
        "Después de la caída hubo cambios. Las capitales pasaron a ser controladas por españoles, se fundaron ciudades españolas y muchos tributos se pagaron a la Corona y a los conquistadores. La estructura política anterior se transformó, aunque no de golpe en todos los lugares.",
        "También hubo continuidades. La mayoría de la población siguió viviendo en comunidades, cultivando la tierra y hablando sus lenguas. Algunas autoridades locales, los caciques, siguieron mediando entre su pueblo y los españoles. Conquistar un imperio no significó borrar de inmediato la vida cotidiana de millones de personas.",
    ],
    vocab=[("cacique", "autoridad local de un pueblo indígena que media con los españoles"), ("Corona", "gobierno del rey y de su Estado"), ("valle de México", "zona alta y rodeada de montañas donde estaba Tenochtitlan"), ("marcha", "avance de un grupo por un territorio"), ("ciudad española", "ciudad fundada por españoles en América")],
    worked=[
        ("Seguir una ruta", "Según la ficha, ¿por dónde avanzó Pizarro hacia el interior?", ["Desde Panamá, por la costa del Pacífico.", "Luego subió a los Andes."], "Por la costa del Pacífico y luego por los Andes"),
        ("Clasificar cambio y continuidad", "Una aldea paga ahora tributos a la Corona, pero sigue cultivando la tierra y hablando su lengua. ¿Qué cambió y qué continuó?", ["Pagar tributos a la Corona es nuevo.", "Cultivar y hablar su lengua continúa."], "Cambió: a quién pagan tributos; continuó: cultivo y lengua"),
    ],
    mistakes=[("Creer que la conquista cambió de inmediato toda la vida de los pueblos.", "Se ignora que muchas comunidades siguieron con su vida cotidiana.", "Nombra continuidades como cultivo, lengua y caciques."),
              ("Pensar que las rutas eran caminos vacíos.", "Se olvida que atravesaban territorios de pueblos con aliados y enemigos.", "Menciona las alianzas y los pueblos del trayecto.")],
    T=[
        ("{F} ¿Dónde desembarcó Cortés?", "En la costa de Veracruz", "La ficha lo indica."),
        ("{F} ¿Desde qué lugar parte Pizarro hacia el sur?", "Desde Panamá", "La ficha lo indica."),
        ("{F} ¿En qué lago estaba la isla donde se levantaba Tenochtitlan?", "En el lago de Texcoco", "La ficha lo dice."),
        ("{F} ¿Qué pueblos aliados se mencionan en la ruta de Cortés?", "Los tlaxcaltecas", "La ficha los nombra."),
        ("{F} Clasifica como cambio o continuidad: a) los tributos se pagan a la Corona, b) la gente cultiva la tierra, c) se fundan ciudades españolas.", "a) cambio; b) continuidad; c) cambio", "Solo cultivar la tierra se mantiene."),
        ("=", "{F} Una expedición avanza 15 km por día durante 12 días hacia el interior. ¿Cuántos kilómetros recorre?", "15*12", "Se multiplica lo que avanza por día por los días.", " km"),
        ("{F} ¿Por qué se dice que Tenochtitlan y Cusco eran el «corazón político» de sus imperios? A) Porque allí se concentraba el gobierno B) Porque estaban lejos del gobierno", "A) Porque allí se concentraba el gobierno", "Eran las capitales."),
        ("{F} ¿Qué efecto tuvo llegar a la capital en la rapidez de la conquista?", "Al caer o ser tomada la capital, se desorganizó el gobierno", "Se alteró el centro del poder."),
        ("{F} Un compañero dice: «Después de la conquista nadie siguió hablando lenguas originarias». ¿Qué dato de la ficha lo contradice?", "Los pueblos conservan sus lenguas", "La ficha lo dice como una continuidad."),
        ("{F} ¿Qué papel cumplían los caciques después de la conquista?", "Mediaban entre su pueblo y los españoles", "La ficha lo indica."),
        ("{F} ¿Qué afirmación es proporcional? A) La conquista cambió el poder en las capitales y dejó continuidades en la vida de las comunidades B) La conquista no cambió nada", "A) La conquista cambió el poder en las capitales y dejó continuidades en la vida de las comunidades", "La ficha muestra ambos aspectos."),
        ("{F} Una línea de tiempo usa 1 cm = 5 años y parte en 1519. ¿A cuántos cm queda 1533?", "2 cm", "La diferencia es 14 años; 14 dividido por 5 da 2 completos."),
        ("{F} ¿Qué pregunta ayudaría a entender mejor el territorio de la conquista?", "¿Qué pueblos vivían en el camino y qué hicieron frente a los españoles?", "Los pueblos del trayecto influyeron en el resultado."),
    ],
    ctx=("Un guía quiere explicar un mapa de la ruta de Cortés. ¿Qué dos cosas debe señalar para no hablar de «un camino vacío»? {F}", "Que hubo alianzas con pueblos como los tlaxcaltecas y que la ruta llegaba a una gran ciudad en el valle de México", "La ficha menciona aliados y una ciudad en el valle de México."),
    sc=[("¿Qué es un cacique?", "Una autoridad local indígena que media con los españoles", "Se definió en el vocabulario."),
        ("¿Qué ciudad andina tomaron los españoles en 1533?", "Cusco", "La ficha lo indica."),
        ("¿Qué continuó después de la caída de los imperios? A) La vida en comunidades B) El gobierno de los antiguos emperadores", "A) La vida en comunidades", "La ficha lo señala como continuidad.")],
    op=("Dibuja un croquis con dos rutas: la de Cortés (Veracruz a Tenochtitlan) y la de Pizarro (Panamá a Cajamarca y Cusco). Marca con un color los lugares clave y con una flecha los años. Escribe debajo un cambio y una continuidad después de la caída. {F}",
        "Ruta de Cortés: Veracruz, tlaxcaltecas, Tenochtitlan 1521; ruta de Pizarro: Panamá, Cajamarca 1532, Cusco 1533. Cambio: tributos a la Corona. Continuidad: la gente sigue cultivando.",
        ["marca las dos rutas", "incluye los años", "nombra cambio y continuidad"], ["croquis", "dos frases"], ["mezclar las rutas", "decir que no hubo continuidades"],
        "Pide que explique el papel de los aliados en la ruta de Cortés."),
    reinforce="Cuenta una de las dos rutas con sus lugares y un cambio posterior.",
    extend="Escribe una pregunta sobre qué pasó en una comunidad lejana de las capitales.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno; no son testimonios reales). "
     "Voz 1, capitán español, 1520: «Mis hombres tienen espadas de acero, caballos y armas de fuego, y buscamos oro y tierras para el rey y para nosotros.» "
     "Voz 2, jefe de un pueblo tributario de un imperio, 1520: «Pagamos tributos pesados; si estos extranjeros nos ayudan a derrotar a nuestros dominadores, nos aliaremos.» "
     "Voz 3, guerrero de un ejército local, 1530: «Combatimos con lanzas, arcos y hondas, y nunca habíamos visto caballos ni armas de fuego.» "
     "Voz 4, habitante de una aldea, 1540: «Muchas personas de mi aldea enfermaron y murieron; falta gente para cultivar los campos.» "
     "Causas que mencionan los historiadores: pueblos tributarios descontentos; guerra civil entre pretendientes al trono inca; tecnología militar distinta; intereses de los conquistadores en riqueza y tierras; enfermedades traídas de Europa, como la viruela.")
build(
    OA, 4, F,
    use="Aprenderé a contrastar las causas de la conquista desde distintos actores y a explicar cómo se combinaron la organización política, la guerra, los intereses y las enfermedades.",
    prior=["Conozco los cuatro factores del OA.", "Sé contrastar perspectivas.", "Sé que una explicación puede ser multicausal."],
    explain=[
        "La rapidez de la conquista tuvo varias causas que se combinaron. La primera es la organización política: los imperios tenían pueblos tributarios descontentos, que se aliaron con los extranjeros, y en el caso inca había una guerra civil entre pretendientes al trono. Estas divisiones facilitaron que un grupo pequeño se apoyara en aliados numerosos.",
        "La segunda es la manera de hacer la guerra. Los españoles usaban espadas de acero, caballos y armas de fuego, que los ejércitos locales no conocían. Los ejércitos locales combatían con lanzas, arcos y hondas, bien adaptados a su forma de pelear. La diferencia de tecnología ayudó, pero no explica todo. La tercera son los intereses de los conquistadores en riqueza y tierras, que los empujaron a seguir avanzando.",
        "La cuarta es la catástrofe demográfica: enfermedades como la viruela, desconocidas en América, mataron a mucha gente y debilitaron la capacidad de resistir. Ninguna causa actuó sola. La mirada de cada actor —el capitán, el jefe tributario, el guerrero, el aldeano— permite ver partes distintas de la misma historia.",
    ],
    vocab=[("pueblo tributario", "pueblo que paga tributos a otro más poderoso"), ("tecnología militar", "armas y técnicas usadas en la guerra"), ("viruela", "enfermedad contagiosa que causó muchas muertes en América"), ("pretendiente al trono", "persona que aspira a gobernar"), ("multicausal", "que combina varias causas")],
    worked=[
        ("Reconocer una causa", "¿Qué causa muestra la voz 2 de la ficha?", ["El jefe dice que paga tributos pesados.", "Está dispuesto a aliarse con los extranjeros."], "La organización política y el descontento de pueblos tributarios"),
        ("Evitar una causa única", "Un texto dice: «Los españoles vencieron solo por sus caballos». ¿Qué otras causas de la ficha faltan?", ["Busco las otras causas.", "Faltan alianzas, guerra civil inca, intereses y enfermedades."], "Alianzas, guerra civil, intereses y enfermedades"),
    ],
    mistakes=[("Atribuir la conquista solo a la superioridad militar.", "Se ignoran las alianzas, la guerra civil y las epidemias.", "Combina los cuatro factores."),
              ("Presentar a los pueblos indígenas solo como víctimas pasivas.", "Se olvida que tomaron decisiones, como aliarse.", "Muestra su agencia: negociar, aliarse o resistir.")],
    T=[
        ("{F} ¿Quién dice que busca oro y tierras para el rey y para sí mismo?", "El capitán español", "Es la voz 1."),
        ("{F} ¿Qué dice el jefe tributario que haría si los extranjeros lo ayudan?", "Se aliaría con ellos", "Es lo que dice la voz 2."),
        ("{F} ¿Con qué armas combatía el guerrero local?", "Con lanzas, arcos y hondas", "Lo dice la voz 3."),
        ("{F} ¿Qué efecto de la enfermedad cuenta la voz 4?", "Faltaba gente para cultivar los campos", "La aldea perdió a muchas personas."),
        ("=", "{F} ¿Cuántos años pasaron entre las voces 1 (1520) y 4 (1540)?", "1540-1520", "Se resta el primer año al segundo.", " años"),
        ("{F} Clasifica cada voz con el factor del OA que ilustra: a) voz 2, b) voz 3, c) voz 4. Opciones: organización política; forma de hacer la guerra; catástrofe demográfica.", "a) organización política; b) forma de hacer la guerra; c) catástrofe demográfica", "Cada voz muestra un factor."),
        ("{F} ¿Qué voz ilustra los intereses de los conquistadores? A) La voz 1 B) La voz 4", "A) La voz 1", "Habla de oro y tierras."),
        ("{F} ¿Qué no conocían los guerreros locales antes de enfrentarse a los españoles? A) Los caballos y las armas de fuego B) Las lanzas, los arcos y las hondas", "A) Los caballos y las armas de fuego", "La voz 3 dice que nunca los habían visto."),
        ("{F} Un compañero dice: «Los pueblos indígenas no tomaron decisiones». ¿Qué voz lo contradice?", "La voz 2, el jefe tributario que decide aliarse", "Muestra una decisión propia."),
        ("{F} ¿Por qué las divisiones internas de los imperios ayudaron a los conquistadores?", "Porque permitieron aliarse con grupos descontentos o enfrentados", "Un grupo pequeño se apoyó en aliados."),
        ("{F} ¿Qué conclusión es proporcional? A) La conquista se explica por una combinación de causas políticas, militares, de intereses y de enfermedades B) Se explica solo por la tecnología", "A) La conquista se explica por una combinación de causas políticas, militares, de intereses y de enfermedades", "Las voces muestran varios factores."),
        ("{F} ¿Qué voz falta en la ficha y sería importante escuchar?", "La de una mujer indígena o la de un niño", "La ficha no incluye mujeres ni jóvenes."),
        ("{F} ¿Qué debilita la capacidad de resistir según la voz 4? A) Falta gente para cultivar los campos y sostener a la comunidad B) La aldea tiene más armas", "A) Falta gente para cultivar los campos y sostener a la comunidad", "La enfermedad debilita la sociedad."),
    ],
    ctx=("Un maestro propone un debate: «¿Fue la tecnología lo que explicó la conquista?». Con dos voces de la ficha, ¿cómo respondes con cuidado? {F}", "Que ayudó, como dice la voz 1, pero también influyeron las alianzas de la voz 2 y la enfermedad de la voz 4", "Ninguna causa actuó sola."),
    sc=[("¿Qué es un pueblo tributario?", "Un pueblo que paga tributos a otro más poderoso", "Se definió en el vocabulario."),
        ("¿Qué enfermedad menciona la ficha como causa de muertes?", "La viruela", "Está en la lista de causas."),
        ("¿Qué causa ilustra la guerra civil inca? A) La organización política B) La tecnología militar", "A) La organización política", "Divisiones internas debilitaron el imperio.")],
    op=("Escribe un diálogo de seis líneas entre el capitán español y el jefe tributario de la ficha. Cada uno debe nombrar sus razones y sus intereses con datos de su voz. Cierra con una frase tuya sobre por qué la alianza facilitó la conquista. {F}",
        "Capitán: buscamos oro y tierras. Jefe: pagamos tributos pesados y si nos ayudan nos aliamos. Cierre: la alianza unió fuerzas contra el imperio.",
        ["usa datos de las voces", "muestra los intereses de cada uno", "cierra con una explicación"], ["diálogo", "frase"], ["mostrar al jefe sin decisión propia", "inventar hechos que contradicen la ficha"],
        "Pide que explique qué pierde y qué gana cada parte con la alianza."),
    reinforce="Nombra los cuatro factores de la conquista y una voz de la ficha para cada uno.",
    extend="Escribe una pregunta que le harías al jefe tributario sobre su alianza.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (pregunta y evidencias de ejemplo). Pregunta: ¿se explica la caída de los imperios americanos solo por la superioridad militar europea? "
     "Evidencia 1 (organización política): pueblos tributarios descontentos se aliaron con los españoles. "
     "Evidencia 2 (organización política): en el imperio inca hubo guerra civil entre Huáscar y Atahualpa antes de 1532. "
     "Evidencia 3 (guerra): los españoles usaban acero, caballos y armas de fuego. "
     "Evidencia 4 (intereses): los conquistadores buscaban riqueza y tierras, y financiaban expediciones para obtener premios del rey. "
     "Evidencia 5 (catástrofe demográfica): la viruela y otras enfermedades mataron a mucha gente. "
     "Evidencia 6 (límite): en el sur de Chile, los mapuche resistieron por décadas.")
build(
    OA, 5, F,
    use="Aprenderé a construir un argumento multicausal sobre la rapidez de la conquista, con evidencias de los cuatro factores y con un límite que reconozca los casos distintos.",
    prior=["Sé que un argumento tiene tesis, evidencias y límite.", "Conozco los cuatro factores de la conquista.", "Sé que hubo resistencia prolongada."],
    explain=[
        "Para explicar la rapidez de la conquista, una tesis sólida combina los cuatro factores del OA: organización política, forma de hacer la guerra, intereses de los conquistadores y catástrofe demográfica. Cada factor necesita al menos una evidencia. La ficha entrega seis, incluida una que muestra un caso distinto: los mapuche.",
        "La tesis puede formularse así: «La conquista fue rápida porque los imperios tenían divisiones internas que facilitaron alianzas, los europeos tenían ventajas militares, los conquistadores buscaban riqueza y las epidemias debilitaron a la población». Cada parte se apoya en una evidencia numerada. La evidencia 6 sirve de límite: la conquista no fue igual en todos los territorios.",
        "El error más común es atribuirlo todo a la superioridad militar. Eso invisibiliza el papel de las alianzas, de los conflictos internos y de las epidemias, y también la agencia indígena, es decir, la capacidad de decidir y actuar de los pueblos. Un buen argumento reconoce que los pueblos eligieron aliarse o resistir.",
    ],
    vocab=[("agencia", "capacidad de las personas de decidir y actuar en su historia"), ("tesis", "respuesta que se defiende con evidencias"), ("evidencia", "dato de una fuente que sostiene la tesis"), ("límite", "lo que la evidencia no permite concluir"), ("invisibilizar", "dejar fuera de un relato a alguien o algo importante")],
    worked=[
        ("Asignar evidencia a un factor", "¿Qué factor ilustra la evidencia 5?", ["Habla de enfermedades que matan a mucha gente.", "Eso es catástrofe demográfica."], "La catástrofe demográfica"),
        ("Usar la evidencia 6", "¿Para qué sirve la evidencia 6 en el argumento?", ["Muestra un caso donde la conquista no fue rápida.", "Eso limita la generalización."], "Sirve de límite: no fue igual en todos los territorios"),
    ],
    mistakes=[("Explicar la conquista solo por la superioridad militar.", "Se dejan fuera alianzas, guerra civil y epidemias.", "Cita evidencias de los cuatro factores."),
              ("Decir que todos los pueblos fueron derrotados rápido.", "Se ignora a los mapuche.", "Usa la evidencia 6 para matizar.")],
    T=[
        ("{F} ¿Qué evidencia muestra la guerra civil inca?", "La evidencia 2", "Menciona a Huáscar y Atahualpa."),
        ("{F} ¿Qué evidencia habla de tecnología militar?", "La evidencia 3", "Cita acero, caballos y armas de fuego."),
        ("{F} ¿Qué evidencia muestra la agencia de pueblos tributarios?", "La evidencia 1", "Dice que se aliaron con los españoles."),
        ("{F} Clasifica cada evidencia con su factor: a) 2, b) 4, c) 5. Opciones: organización política; intereses de los conquistadores; catástrofe demográfica.", "a) organización política; b) intereses de los conquistadores; c) catástrofe demográfica", "Cada evidencia corresponde a un factor."),
        ("{F} ¿Cuáles evidencias corresponden a organización política?", "La 1 y la 2", "Son las rotuladas así."),
        ("{F} ¿Qué evidencia sirve como límite de la tesis?", "La evidencia 6", "Muestra que la conquista no fue rápida en todas partes."),
        ("{F} ¿Qué tesis se apoya mejor en las evidencias? A) La rapidez se explica por una combinación de factores políticos, militares, de intereses y de enfermedades B) Se explica solo por el acero y los caballos", "A) La rapidez se explica por una combinación de factores políticos, militares, de intereses y de enfermedades", "Hay evidencias para los cuatro factores."),
        ("{F} Un compañero dice: «La viruela por sí sola explica todo». ¿Qué le falta?", "Evidencias de los otros factores, como las alianzas y la tecnología", "Una sola causa no basta."),
        ("{F} ¿Qué se invisibiliza si solo se menciona la superioridad militar?", "El papel de las alianzas, las divisiones internas, las epidemias y la agencia indígena", "Esos factores también explican el resultado."),
        ("{F} Escribe un límite honesto para la tesis.", "Las evidencias no distinguen entre pueblos, y los mapuche resistieron durante décadas", "Un argumento reconoce los casos distintos."),
        ("{F} Un compañero cita solo la evidencia 3 y concluye que «los españoles eran superiores». ¿Qué error comete?", "Ignora las evidencias de alianzas, guerra civil, intereses y enfermedades", "Selecciona solo lo que apoya su idea."),
        ("{F} ¿Qué respuesta es más sólida? A) «Fue una combinación de alianzas, divisiones internas, armas, intereses y enfermedades, aunque no ocurrió igual en todos lados» B) «Los españoles eran invencibles»", "A) «Fue una combinación de alianzas, divisiones internas, armas, intereses y enfermedades, aunque no ocurrió igual en todos lados»", "Cita varios factores y reconoce un límite."),
        ("{F} ¿Por qué citar la evidencia 1 muestra la agencia indígena?", "Porque muestra que algunos pueblos decidieron aliarse", "No actuaron como víctimas pasivas."),
    ],
    ctx=("En un concurso se pide responder en una frase por qué cayeron rápido los imperios. Redáctala con dos factores y una evidencia. {F}", "Porque había pueblos tributarios descontentos que se aliaron con los españoles (evidencia 1) y las epidemias debilitaron a la población (evidencia 5)", "Combina dos factores apoyados en evidencias."),
    sc=[("¿Qué es la agencia?", "La capacidad de las personas de decidir y actuar en su historia", "Se definió en el vocabulario."),
        ("¿Qué evidencia habla de la viruela?", "La evidencia 5", "Menciona la viruela y otras enfermedades."),
        ("¿Para qué sirve el límite? A) Para reconocer lo que la evidencia no prueba B) Para repetir la tesis", "A) Para reconocer lo que la evidencia no prueba", "Así se definió.")],
    op=("Escribe un párrafo de seis líneas con tu tesis sobre por qué fue rápida la conquista. Debe incluir tres evidencias numeradas de la ficha de factores distintos, un enunciado que reconozca la agencia indígena y un límite. {F}",
        "Pienso que fue rápida por una combinación de factores. Evidencia 1: pueblos tributarios se aliaron. Evidencia 3: armas de acero. Evidencia 5: epidemias. Los pueblos decidieron aliarse. Límite: los mapuche resistieron décadas.",
        ["tiene tesis", "tres evidencias de factores distintos", "reconoce la agencia indígena y un límite"], ["párrafo"], ["citar solo un factor", "presentar a los pueblos solo como víctimas"],
        "Pide que explique cómo el límite cambia la tesis."),
    reinforce="Explica oralmente por qué no basta la superioridad militar para explicar la conquista.",
    extend="Escribe una pregunta que ayudaría a medir cuánto influyeron las epidemias.",
)

# ---------------------------------------------------------------- clase 6
F = ("Ficha 6 (casos y datos de ejemplo). Caso 1, mexicas: la capital cae en 1521, dos años después de la llegada de Cortés. Caso 2, incas: la capital es ocupada en 1533, pero en 1536 Manco Inca encabeza un levantamiento contra los españoles. "
     "Caso 3, mapuche: Valdivia funda Santiago en 1541 y muere en combate en 1553; la guerra continúa durante décadas y en el siglo XVII los mapuche negocian en parlamentos con los españoles. "
     "Caso 4, mayas: el último reino maya independiente, Nojpetén, cae en 1697. "
     "Población de ejemplo de un valle en miles de habitantes: antes de la conquista, 1.000; 80 años después, 200. "
     "Consecuencia posterior: ante la falta de trabajadores indígenas, los españoles recurrieron también a la trata de personas africanas.")
build(
    OA, 6, F,
    use="Aprenderé a evaluar hasta dónde sirve la idea de «conquista rápida», a reconocer los límites de ese concepto con varios casos y a analizar una de sus consecuencias.",
    prior=["Conozco los cuatro factores de la conquista.", "Sé argumentar con evidencias y límites.", "Sé comparar casos."],
    explain=[
        "Evaluar una idea significa ver hasta dónde sirve. La idea de «conquista rápida» describe bien la caída de las capitales mexica e inca. Pero la ficha muestra que hubo levantamientos incas desde 1536, una guerra de décadas contra los mapuche y un reino maya independiente hasta 1697. Por eso la idea tiene límites: no vale igual para todos los pueblos ni para todas las etapas.",
        "El caso de la población de un valle, que bajó de 1.000 a 200 miles de habitantes en 80 años, ilustra la catástrofe demográfica. Esa caída tuvo consecuencias: faltaban trabajadores para minas y campos. Los españoles organizaron el trabajo forzado de indígenas y recurrieron también a la trata de personas africanas. Es una proyección: una causa lleva a nuevos cambios posteriores.",
        "Al evaluar proyecciones hay que ser cuidadoso. No podemos aplicar el presente al pasado ni usar datos de ejemplo como si fueran reales. Un buen análisis dice qué se puede concluir, qué no y qué otras fuentes se necesitarían para saber más.",
    ],
    vocab=[("levantamiento", "rebelión armada contra una autoridad"), ("parlamento", "reunión formal de negociación entre mapuche y autoridades españolas"), ("proyección", "efecto posterior de un hecho en el tiempo"), ("trata de personas", "comercio de personas como esclavas"), ("etapa", "tramo de un proceso en el tiempo")],
    worked=[
        ("Calcular una disminución", "En el valle de la ficha, ¿cuánto bajó la población, en miles de habitantes, de 1.000 a 200?", ["Resto: 1.000 − 200.", "El resultado es 800."], "800 mil habitantes menos"),
        ("Evaluar una idea", "¿Sirve la idea de «conquista rápida» para el caso mapuche?", ["Valdivia murió en 1553 y la guerra siguió décadas.", "No hubo derrota rápida."], "No, tiene un límite en el caso mapuche"),
    ],
    mistakes=[("Aplicar «conquista rápida» a todos los pueblos.", "Se ignoran levantamientos y resistencias.", "Compara casos y usa el concepto con límites."),
              ("Tratar los datos de población de ejemplo como cifras reales.", "Los datos fueron escritos para este cuaderno.", "Rotula los datos de ejemplo y no los generalices.")],
    T=[
        ("{F} ¿Quién encabezó el levantamiento inca de 1536?", "Manco Inca", "La ficha lo indica."),
        ("{F} ¿En qué año cayó el último reino maya independiente de la ficha?", "1697", "Es el año indicado."),
        ("{F} ¿Qué hicieron los mapuche en el siglo XVII según la ficha?", "Negociaron con los españoles en parlamentos", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre la caída de Tenochtitlan (1521) y la de Nojpetén (1697)?", "1697-1521", "Se restan los dos años.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la ocupación de Cusco y el levantamiento de Manco Inca?", "1536-1533", "Se resta el primer año al segundo.", " años"),
        ("=", "{F} Según el dato de ejemplo, ¿cuántos miles de habitantes menos había en el valle 80 años después de la conquista?", "1000-200", "Se resta la población final a la inicial.", " mil habitantes"),
        ("{F} Clasifica cada caso según si la conquista fue rápida o prolongada: a) mexicas, b) mapuche, c) mayas de Nojpetén.", "a) rápida; b) prolongada; c) prolongada", "Tenochtitlan cae en dos años; los otros resistieron mucho más."),
        ("{F} ¿Para qué casos sirve mejor la idea de «conquista rápida»? A) Mexicas e incas en sus capitales B) Mapuche y mayas de Nojpetén", "A) Mexicas e incas en sus capitales", "Sus capitales cayeron en pocos años."),
        ("{F} ¿Qué consecuencia tuvo la disminución de la población según la ficha?", "Faltaron trabajadores y se recurrió también a la trata de personas africanas", "La ficha menciona esa consecuencia."),
        ("{F} Un compañero dice: «Todos los indígenas fueron derrotados rápido». ¿Qué dato de la ficha lo contradice?", "La guerra mapuche duró décadas y Nojpetén cayó recién en 1697", "Hubo resistencias prolongadas."),
        ("{F} ¿Por qué hay que ser cuidadoso con los datos de población de la ficha?", "Porque son de ejemplo y no representan cifras reales", "Están rotulados como ejemplo."),
        ("{F} ¿Qué conclusión es proporcional? A) La conquista fue rápida en algunas capitales y prolongada en otros territorios B) La conquista fue igual en todos lados", "A) La conquista fue rápida en algunas capitales y prolongada en otros territorios", "Los cuatro casos lo muestran."),
        ("{F} ¿Qué otra fuente agregarías para saber la mortalidad real en un valle? A) Registros de población y estudios actuales B) Una carta de un conquistador que pide premios", "A) Registros de población y estudios actuales", "Permiten medir mejor los cambios."),
    ],
    ctx=("Un historiador escolar debe decidir si un título dice «La rápida caída de los imperios americanos». ¿Qué cambio propondrías con la ficha? {F}", "Precisar que fue rápida en las capitales mexica e inca, pero prolongada entre mapuche y mayas", "Reconoce los casos distintos."),
    sc=[("¿Qué es una proyección?", "El efecto posterior de un hecho en el tiempo", "Se definió en el vocabulario."),
        ("¿Qué caso muestra una resistencia prolongada?", "El de los mapuche", "La guerra continuó durante décadas."),
        ("=", "El levantamiento de Manco Inca fue en 1536 y la ocupación de Cusco en 1533. ¿Cuántos años pasaron?", "1536-1533", "Se restan los dos años.", " años")],
    op=("Escribe un texto de cinco a seis líneas que evalúe la idea de «conquista rápida». Debe incluir dos casos de la ficha donde sirve y dos donde no, el dato de población de ejemplo y un límite que diga qué otras fuentes necesitarías. {F}",
        "Sirve para Tenochtitlan (1521) y Cusco (1533). No sirve para los mapuche (guerra de décadas) ni para Nojpetén (1697). El valle bajó de 1.000 a 200 miles de habitantes, un dato de ejemplo. Necesitaría registros de población.",
        ["incluye dos casos donde sirve y dos donde no", "usa el dato de población como ejemplo", "señala otras fuentes"], ["texto"], ["usar solo casos de caída rápida", "tomar el dato de ejemplo como real"],
        "Pide que explique por qué es importante comparar casos."),
    reinforce="Cuenta un caso donde la conquista fue rápida y otro donde fue prolongada.",
    extend="Escribe una pregunta sobre qué factores permitieron a un pueblo resistir más tiempo.",
)
