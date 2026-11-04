"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 13 (ocupación austral, inmigración y pueblos originarios)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 13"
MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = "Línea de tiempo: 1826, Chiloé se incorpora a la República de Chile; 1843, se funda el Fuerte Bulnes en el estrecho de Magallanes; 1845, ley que autoriza traer colonos extranjeros; 1846, llegan las primeras familias alemanas a la zona de Valdivia; 1848, se funda Punta Arenas; 1852-1853, comienza la colonización de Llanquihue y se funda Puerto Montt."
build(
    OA, 1, F1,
    use="Aprenderé a ubicar en el tiempo y en el mapa la ocupación de Valdivia, Llanquihue, Chiloé y el estrecho de Magallanes y a explicar por qué esas zonas eran estratégicas. Sirve para entender cómo el Estado extendió su presencia hacia el sur.",
    prior=["Conozco la exploración estatal del territorio.", "Sé ubicar el sur de Chile en un mapa.", "Sé qué son una frontera y un censo."],
    explain=[
        "Durante el siglo XIX el Estado chileno quiso extender su presencia hacia el sur. Ocupar un territorio significa instalar en él población, autoridades e instituciones del Estado. Las zonas que se ocuparon fueron Valdivia, Llanquihue, Chiloé y el estrecho de Magallanes. Chiloé se había incorporado a la República en 1826; en Magallanes se fundó el Fuerte Bulnes en 1843 y Punta Arenas en 1848.",
        "La ocupación tenía importancia estratégica, es decir, valor para los objetivos del Estado. El estrecho de Magallanes era una ruta marítima entre los océanos Atlántico y Pacífico. Las tierras de Valdivia y Llanquihue servían para la agricultura, la ganadería y la madera. Además, ocupar esos lugares permitía afirmar la soberanía de Chile frente a otros países que también miraban esos territorios.",
        "Para poblar, el Estado impulsó la inmigración europea: una ley de 1845 autorizó traer colonos extranjeros, y desde 1846 llegaron familias alemanas a la zona de Valdivia. Pero esas tierras ya estaban habitadas por pueblos originarios, como los huilliche en el sur y los kawésqar, selk'nam, yagán y aónikenk en el extremo austral. Por eso decimos ocupación y no descubrimiento ni colonización de espacios vacíos.",
    ],
    vocab=[("ocupación", "instalación de población, autoridades e instituciones del Estado en un territorio"), ("colono", "persona que se instala en un territorio para poblarlo y trabajarlo"), ("inmigración", "llegada de personas de otro país para vivir en el país"), ("soberanía", "autoridad exclusiva de un Estado sobre un territorio"), ("importancia estratégica", "valor de un lugar para los objetivos de un Estado")],
    worked=[
        ("Ubicar en el tiempo", "Con la línea de tiempo, ¿cuántos años pasaron entre la fundación del Fuerte Bulnes y la fundación de Punta Arenas?",
         ["Busco las fechas: 1843 y 1848.", "Resto: 1848 - 1843."], "5 años"),
        ("Explicar la importancia estratégica", "¿Por qué el estrecho de Magallanes tenía importancia estratégica para Chile?",
         ["Era una ruta marítima entre el Atlántico y el Pacífico.", "Ocuparlo permitía afirmar la soberanía chilena sobre ese paso."], "Por ser una ruta entre dos océanos y afirmar la soberanía"),
    ],
    mistakes=[
        ("Decir que el sur era un territorio vacío antes de la ocupación.", "Estaba habitado por pueblos originarios.", "Nombra quién vivía allí antes de la llegada del Estado."),
        ("Creer que llegaron colonos en el mismo año a todas las zonas.", "La ocupación fue gradual y distinta según lugar.", "Ubica cada hecho con su fecha y su zona."),
    ],
    T=[
        ("En Historia: ¿qué significa ocupar un territorio?", "Instalar población, autoridades e instituciones del Estado en él", "Es el sentido de ocupación en la clase."),
        ("{F} ¿En qué año se funda Punta Arenas?", "1848", "La línea de tiempo lo indica."),
        ("{F} ¿Qué zona recibió en 1846 las primeras familias alemanas?", "La zona de Valdivia", "La línea lo señala."),
        ("En Historia: ¿qué es un colono?", "Una persona que se instala en un territorio para poblarlo y trabajarlo", "Es el término para quienes llegaban a poblar."),
        ("{F} ¿Qué hecho de 1826 conecta a Chiloé con el Estado chileno? A) se incorpora a la República, B) se funda Punta Arenas, C) llegan colonos alemanes.", "A", "La línea lo indica."),
        ("Una compañera dice: «El estrecho de Magallanes importaba solo por la pesca». ¿Qué corrección haces?", "Importaba además como ruta marítima entre el Atlántico y el Pacífico y para afirmar la soberanía", "Su importancia era estratégica y marítima."),
        ("=", "{F} ¿Cuántos años pasaron entre la incorporación de Chiloé y la fundación del Fuerte Bulnes?", "1843-1826", "Se restan las dos fechas."),
        ("=", "{F} ¿Cuántos años pasaron entre la ley de 1845 y la fundación de Puerto Montt en 1853?", "1853-1845", "Se restan las dos fechas."),
        ("Une cada lugar con una razón de su valor: 1) estrecho de Magallanes, 2) Valdivia y Llanquihue, 3) Chiloé. a) tierras para agricultura y madera, b) ruta entre océanos, c) isla ya poblada que se incorporó en 1826. Escribe las parejas.", "1-b, 2-a, 3-c", "Cada lugar se asocia a una razón distinta."),
        ("{F} ¿Qué dato de la línea muestra que el Estado impulsó la llegada de extranjeros?", "La ley de 1845 que autoriza traer colonos extranjeros", "La ley es la base legal de la inmigración."),
        ("Explica por qué hablar de «colonización de espacios vacíos» es inexacto.", "Porque esos lugares estaban habitados por pueblos originarios como los huilliche, kawésqar, selk'nam, yagán y aónikenk", "No eran lugares sin población."),
        ("Evalúa la frase «la ocupación del sur ocurrió en un solo año». A) es falsa porque fue gradual, con hechos entre 1826 y 1853, B) es verdadera porque todo ocurrió en 1846, C) es verdadera porque la ley de 1845 bastó para poblar todo el sur.", "A", "La línea muestra varios años."),
        ("Una persona dice: «Si llegaron alemanes, el éxito de la ocupación fue solo obra de ellos». Da una razón para dudar usando la clase.", "Porque también participaron el Estado, otros pobladores y, aunque no figuren en la línea, había pueblos originarios en esos lugares", "El resultado fue obra de varios actores."),
    ],
    ctx=("Un afiche escolar dice: «En 1846 el sur de Chile empezó a existir cuando llegaron los alemanes». Escribe una frase que corrija el afiche con lo aprendido.", "El sur ya estaba habitado por pueblos originarios; en 1846 llegaron colonos alemanes impulsados por el Estado", "La frase debe reconocer a los pueblos previos."),
    sc=[("En Historia: ¿qué es la soberanía?", "La autoridad exclusiva de un Estado sobre un territorio", "Es una razón para ocupar territorios."),
        ("Nombra dos zonas del sur que se ocuparon en el siglo XIX.", "Por ejemplo: Valdivia y Llanquihue", "Son parte del OA."),
        ("{F} ¿Qué ley de 1845 se menciona en la línea de tiempo?", "Una ley que autoriza traer colonos extranjeros", "Es el sustento legal de la inmigración.")],
    op=("{F} Con la línea de tiempo de arriba, escribe cinco líneas que expliquen cómo avanzó la ocupación del sur entre 1826 y 1853. Nombra dos zonas, dos fechas, una razón estratégica y recuerda a los pueblos originarios que ya vivían ahí.",
        "En 1826 Chiloé se incorporó a la República y en 1843 se fundó el Fuerte Bulnes en el estrecho de Magallanes, una ruta entre dos océanos. En 1846 llegaron familias alemanas a Valdivia. Estos lugares ya estaban habitados por pueblos originarios.",
        ["dos zonas", "dos fechas", "una razón estratégica", "recuerda a los pueblos originarios"], ["texto de cinco líneas"], ["omitir a los pueblos originarios", "no usar fechas"], "Léele tu texto a alguien de tu casa y pídele que anote las fechas que usaste."),
    reinforce="Dibuja un mapa simple del sur de Chile y rotula Valdivia, Llanquihue, Chiloé y el estrecho de Magallanes.",
    extend="Escribe una frase que explique por qué una ruta entre dos océanos era valiosa para un país.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = "Fuente A (texto de ejemplo basado en el tipo de leyes de la época): «El gobierno podrá conceder tierras a colonos extranjeros que se establezcan en las provincias del sur.» Fuente B (carta de un colono, de ejemplo): «Llegamos a la orilla del lago; hay que despejar el bosque con hacha y construir una casa antes del invierno.» Fuente C (tabla de ejemplo): en una localidad del sur se registraron 120 familias colonas y 60 familias de pobladores locales, entre ellas familias chilotas que trabajaban en el despeje del bosque. Fuente D (relato de ejemplo atribuido a una comunidad huilliche): «Nuestras familias vivían aquí desde antes; después se nos fue reduciendo la tierra.»"
build(
    OA, 2, F2,
    use="Aprenderé a leer una ley, una carta de colono, una tabla y un relato de comunidad sobre la ocupación del sur, preguntando quién habla y qué deja fuera. Sirve para armar una explicación con varias voces.",
    prior=["Conozco la ocupación del sur y la inmigración.", "Sé distinguir fuente primaria y secundaria.", "Sé contextualizar una fuente."],
    explain=[
        "La ocupación del sur dejó fuentes de muchos tipos. Una ley muestra la política del Estado: qué se quería y con qué incentivos. La carta de un colono muestra la experiencia de quien llegó: esfuerzo, trabajo y condiciones difíciles. Una tabla cuenta grupos de personas, y un relato de una comunidad originaria aporta la voz de quienes ya vivían en el territorio.",
        "Cada fuente tiene perspectiva y límites. La ley habla de conceder tierras, pero no dice quién las había usado antes. La carta cuenta el esfuerzo del colono, pero no cuenta la historia de las personas que ya estaban allí. La tabla de ejemplo muestra que no solo había colonos europeos: también había familias locales y familias chilotas que trabajaban, un dato que evita atribuir todo el resultado a un solo grupo.",
        "Los relatos de comunidades originarias son fuentes importantes, aunque a veces se conservan en la memoria y no en documentos oficiales. Para usarlos con rigor hay que indicar de quién proviene el relato y no generalizarlo a todos los pueblos. Al contrastar la ley, la carta, la tabla y el relato se logra una explicación más equilibrada de la ocupación del sur.",
    ],
    vocab=[("incentivo", "beneficio que se ofrece para animar a hacer algo, como tierra a un colono"), ("memoria oral", "relato transmitido de boca en boca en una comunidad"), ("perspectiva", "punto de vista desde el que se cuenta un hecho"), ("generalizar", "extender lo que vale para un caso a todos los casos"), ("chilote", "persona originaria de Chiloé")],
    worked=[
        ("Identificar lo que cada fuente aporta", "¿Qué aporta la Fuente B (carta de un colono) y qué no dice?",
         ["Aporta la experiencia del colono: despejar el bosque y construir una casa antes del invierno.", "No dice quién había vivido antes en esas tierras."], "Aporta la experiencia del colono; no menciona a quienes ya vivían allí"),
        ("Evitar la generalización", "La Fuente D es un relato de una comunidad huilliche. ¿Por qué no debe usarse como si hablara por todos los pueblos originarios?",
         ["Procede de una comunidad concreta.", "Cada pueblo y cada comunidad tuvo experiencias distintas."], "Porque representa una comunidad y no a todos los pueblos"),
    ],
    mistakes=[
        ("Usar la ley como prueba de lo que ocurrió en la práctica.", "Una ley muestra una intención del Estado, no su aplicación.", "Contrasta la ley con testimonios y datos."),
        ("Ignorar la voz de las comunidades originarias.", "Es una perspectiva clave que otras fuentes omiten.", "Incluye al menos una fuente que la recoja."),
    ],
    T=[
        ("En Historia: ¿qué es la memoria oral?", "Un relato transmitido de boca en boca en una comunidad", "Es el tipo de fuente de la Fuente D."),
        ("{F} ¿Qué ofrece el gobierno a los colonos según la Fuente A?", "Conceder tierras", "La ley lo dice."),
        ("{F} ¿Qué debe hacer el colono antes del invierno según la Fuente B?", "Despejar el bosque y construir una casa", "La carta lo dice."),
        ("{F} ¿Cuántas familias colonas se registraron en la localidad de la Fuente C?", "120", "La tabla lo indica."),
        ("{F} ¿Qué dice la Fuente D que ocurrió con la tierra de las familias huilliche? A) se fue reduciendo, B) aumentó, C) nunca cambió.", "A", "El relato lo afirma."),
        ("{F} Una compañera afirma que la Fuente A prueba que todas las tierras entregadas estaban vacías. ¿Qué corrección haces?", "La ley no dice si estaban vacías; solo muestra la intención de conceder tierras", "Una ley no describe el estado previo."),
        ("=", "{F} ¿Cuántas familias hay en total en la localidad de la Fuente C?", "120+60", "Se suman colonas y locales."),
        ("=", "{F} De las 180 familias de la localidad, ¿cuántas más son colonas que locales?", "120-60", "Se resta el número de familias locales del de colonas."),
        ("{F} ¿Qué fuente permite evitar atribuir todo el resultado a los colonos europeos? A) la A, B) la C, C) la B.", "B", "La tabla incluye pobladores locales y chilotes."),
        ("{F} Explica por qué conviene contrastar la Fuente A con la Fuente D.", "Porque la ley muestra la política estatal y el relato muestra cómo la vivió una comunidad que ya habitaba el lugar", "Una es voz oficial y otra voz comunitaria."),
        ("{F} Redacta una conclusión de una frase que use las Fuentes B y C sin exagerar.", "En la zona había colonos que despejaban el bosque y también familias locales y chilotas que trabajaban en ello", "Une la carta y la tabla con cuidado."),
        ("{F} Evalúa la frase «la Fuente D demuestra lo que vivieron todos los pueblos originarios del sur». A) es excesiva porque es el relato de una comunidad, B) es correcta, C) es correcta porque es oral.", "A", "No se debe generalizar."),
        ("¿Qué otra fuente sumarías para conocer el trabajo de las familias chilotas? Escríbela y explica para qué.", "Por ejemplo: un registro de contratación de trabajadores, para ver cuántos eran y qué hacían", "Cierra un vacío de las fuentes."),
    ],
    ctx=("{F} Un compañero prepara una presentación con solo la Fuente B y el título «La ocupación del sur fue un acto heroico de colonos». ¿Qué fuentes agregarías y por qué?", "La Fuente C, porque muestra otros pobladores, y la D, que aporta la voz de la comunidad huilliche", "Se requiere contrastar para evitar una sola perspectiva."),
    sc=[("En Historia: ¿qué es un incentivo?", "Un beneficio que se ofrece para animar a hacer algo", "Una concesión de tierras es un incentivo."),
        ("¿Por qué no se debe generalizar un relato de una comunidad?", "Porque cada comunidad tuvo experiencias distintas", "Representa un caso."),
        ("{F} ¿La Fuente B es primaria o secundaria?", "Primaria", "Es una carta escrita en la época.")],
    op=("{F} Con las Fuentes A, B, C y D de arriba, escribe un párrafo de siete líneas que responda: «¿Cómo se vivió la ocupación del sur según distintas fuentes?». Indica qué dice cada fuente, qué actor aporta y un límite.",
        "La Fuente A muestra que el Estado concedía tierras a colonos. La Fuente B muestra el esfuerzo de un colono por despejar el bosque. La Fuente C muestra que también había familias locales y chilotas. La Fuente D, de una comunidad huilliche, dice que su tierra se fue reduciendo. Límite: no sabemos qué pasó en cada lugar.",
        ["usa las cuatro fuentes", "nombra actores", "anota un límite"], ["párrafo de siete líneas"], ["omitir la fuente D", "generalizar"], "Pide a alguien de tu casa que verifique que usaste las cuatro fuentes."),
    reinforce="Haz una tabla de cuatro filas con las fuentes A a D: quién habla, qué dice y un límite.",
    extend="Escribe dos preguntas que le harías a una comunidad sobre lo ocurrido con su tierra, sin suponer la respuesta.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = "Cuadro de ejemplo. Cambio: en Valdivia y Llanquihue se instalaron familias colonas, se despejaron bosques, se fundaron pueblos como Puerto Montt y se desarrollaron cultivos, ganadería y pequeñas industrias; en Magallanes se fundaron Fuerte Bulnes y Punta Arenas y creció la ganadería ovina. Continuidad: Chiloé siguió siendo una isla con población campesina y marinera; la presencia de pueblos originarios continuó, aunque con menos tierra; los caminos eran escasos y el tiempo de viaje era largo."
build(
    OA, 3, F3,
    use="Aprenderé a distinguir qué cambió y qué continuó en el sur de Chile con la ocupación y a relacionar esos procesos con el territorio. Sirve para evitar relatos que muestren el sur como una zona transformada solo por inmigrantes.",
    prior=["Conozco la ocupación del sur y sus fuentes.", "Sé qué es una escala local y regional.", "Distingo cambio y continuidad."],
    explain=[
        "Con la ocupación, el paisaje y la economía del sur cambiaron. En Valdivia y Llanquihue se despejaron bosques para abrir campos y se fundaron pueblos y ciudades como Puerto Montt. Se desarrollaron cultivos, ganadería y pequeñas industrias. En Magallanes, Punta Arenas se transformó en puerto y se desarrolló la ganadería ovina, es decir, la crianza de ovejas.",
        "También hubo continuidades. Chiloé mantuvo su población campesina y marinera, y muchos chilotes migraron como trabajadores hacia otras zonas del sur. Los pueblos originarios no desaparecieron, aunque perdieron parte de sus tierras y de su autonomía. Y las distancias seguían siendo grandes: hubo pocos caminos y el viaje era largo, lo que hacía que muchas localidades vivieran aisladas.",
        "El territorio explica diferencias entre zonas. El clima lluvioso y el bosque de Valdivia y Llanquihue influyeron en la manera de poblar; en Magallanes, el viento, el frío y las grandes distancias favorecieron la ganadería extensiva y el comercio marítimo. Por eso no se puede hablar de un único sur: cada zona tuvo su propio proceso.",
    ],
    vocab=[("ganadería ovina", "crianza de ovejas"), ("migrar", "trasladarse de un lugar a otro para vivir o trabajar"), ("aislamiento", "situación de un lugar con pocas conexiones con otros"), ("despeje de bosque", "tala de árboles para abrir terreno de cultivo o de pastoreo"), ("autonomía", "capacidad de un pueblo de decidir sobre sus propios asuntos")],
    worked=[
        ("Clasificar", "Del cuadro de ejemplo: «se funda Puerto Montt» y «Chiloé sigue siendo una isla con población campesina y marinera». ¿Cuál es cambio y cuál continuidad?",
         ["La fundación de una ciudad es algo nuevo: cambio.", "La forma de vida de Chiloé se mantiene: continuidad."], "Puerto Montt: cambio; Chiloé campesino y marinero: continuidad"),
        ("Territorio y proceso", "¿Por qué la ganadería ovina se asoció a Magallanes y no a Llanquihue en el cuadro?",
         ["En Magallanes había grandes extensiones abiertas, viento y frío.", "En Llanquihue predominaban bosques que se despejaban para cultivos y ganadería local."], "Por las grandes extensiones abiertas de Magallanes"),
    ],
    mistakes=[
        ("Contar solo cambios y olvidar a los pueblos originarios y a Chiloé.", "El cuadro tiene continuidades importantes.", "Haz dos columnas y revisa que ambas estén completas."),
        ("Hablar del sur como si fuera una sola región.", "Valdivia, Chiloé y Magallanes son territorios distintos.", "Indica la zona de cada proceso."),
    ],
    T=[
        ("En Historia: ¿qué es la ganadería ovina?", "La crianza de ovejas", "Se desarrolló en Magallanes."),
        ("{F} ¿Qué ciudad se funda en Llanquihue según el cuadro?", "Puerto Montt", "El cuadro la menciona."),
        ("En Historia: ¿qué significa migrar?", "Trasladarse de un lugar a otro para vivir o trabajar", "Muchos chilotes lo hicieron."),
        ("{F} Clasifica como cambio o continuidad: «se despejaron bosques para abrir campos».", "Cambio", "El paisaje se transformó."),
        ("{F} Clasifica como cambio o continuidad: «los pueblos originarios continuaron, aunque con menos tierra».", "Continuidad", "El cuadro dice que su presencia continuó."),
        ("{F} Elige la actividad asociada a Punta Arenas en el cuadro. A) puerto y ganadería ovina, B) minería de plata, C) cultivo de trigo en haciendas.", "A", "El cuadro asocia Magallanes a puerto y ovejas."),
        ("=", "En una estancia de ejemplo había 2.000 ovejas y nacieron 500 corderos. ¿Cuántos animales hay en total?", "2000+500", "Se suman los nacidos a las ovejas existentes."),
        ("=", "Un grupo de 250 familias llega a una localidad del sur y 90 se van a otra zona. ¿Cuántas quedan?", "250-90", "Se restan las que se van."),
        ("Explica por qué hablar de «un único sur» es impreciso.", "Porque Valdivia, Llanquihue, Chiloé y Magallanes tuvieron procesos distintos según su clima y territorio", "El territorio genera diferencias."),
        ("{F} Una compañera dice: «El sur cambió por completo y no quedó nada de lo anterior». Corrige con un dato del cuadro.", "Chiloé mantuvo su población campesina y marinera y los pueblos originarios continuaron", "Hay continuidades claras."),
        ("{F} ¿Qué efecto de las distancias grandes y los pocos caminos se menciona?", "Muchas localidades vivían aisladas", "El cuadro lo señala como continuidad."),
        ("Evalúa la frase «la ocupación transformó el sur pero no eliminó la presencia de pueblos originarios». A) es razonable, B) es falsa porque los pueblos desaparecieron, C) es falsa porque nada cambió.", "A", "Une cambio y continuidad."),
        ("Propón una pregunta de territorio sobre Magallanes.", "Por ejemplo: ¿qué ventajas daba al comercio estar en el estrecho entre dos océanos?", "La pregunta usa el territorio."),
    ],
    ctx=("{F} Un compañero escribe: «Antes de 1840 el sur no tenía nada y después lo tuvo todo gracias a la inmigración». Con el cuadro, escribe una frase que lo matice.", "El sur ya tenía población y pueblos originarios; con la ocupación cambió el paisaje y la economía, pero hubo continuidades", "La frase debe incluir cambio y continuidad."),
    sc=[("En Historia: ¿qué es el aislamiento de un lugar?", "La situación de un lugar con pocas conexiones con otros", "Era frecuente por las distancias."),
        ("Nombra un cambio del sur en el siglo XIX.", "Por ejemplo: se fundaron pueblos como Puerto Montt", "Está en el cuadro."),
        ("Nombra una continuidad del sur en el siglo XIX.", "Por ejemplo: la presencia de pueblos originarios", "Está en el cuadro.")],
    op=("{F} Con el cuadro de ejemplo de arriba, construye una tabla con dos columnas (cambio y continuidad) y tres filas, y escribe una frase final que diferencie al menos dos zonas del sur.",
        "Cambio: fundación de Puerto Montt; cambio: ganadería ovina en Magallanes; cambio: despeje de bosques. Continuidad: Chiloé campesino y marinero; continuidad: presencia de pueblos originarios; continuidad: aislamiento. Valdivia y Llanquihue se transformaron con cultivos, y Magallanes con ovejas y puerto.",
        ["dos columnas", "tres filas", "diferencia dos zonas"], ["tabla y frase"], ["tratar el sur como una sola zona", "olvidar continuidades"], "Revisa con alguien de tu casa que cada dato esté en su columna."),
    reinforce="Escribe tres datos del cuadro y clasifícalos como cambio o continuidad.",
    extend="Escribe una pregunta sobre qué ocurrió con las familias chilotas que migraron como trabajadores.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = "Voces de ejemplo, redactadas para este cuaderno. Agente del Estado: «Queremos poblar el sur con familias que trabajen la tierra y fortalezcan nuestra presencia.» Colono alemán: «Dejé mi aldea en busca de tierra y seguridad; el trabajo aquí es duro.» Trabajador chilote: «Mi labor es despejar el bosque y construir; me pagan según el trabajo realizado.» Dirigente huilliche: «Esta tierra la usaban nuestras familias antes que llegaran los colonos y hoy tenemos menos.» Comerciante de Punta Arenas: «Los barcos que pasan por el estrecho necesitan carbón y alimentos.»"
build(
    OA, 4, F4,
    use="Aprenderé a distinguir actores, intereses y causas en la ocupación del sur y a comparar sus perspectivas. Sirve para explicar el proceso sin atribuirlo a un solo grupo y sin ocultar los conflictos.",
    prior=["Conozco la ocupación del sur y sus fuentes.", "Sé qué es la multicausalidad.", "Sé que cada actor tiene una perspectiva."],
    explain=[
        "En la ocupación del sur actuaron muchos grupos. El Estado impulsó leyes de colonización y fundó ciudades y fuertes. Los colonos europeos, como los alemanes, llegaron buscando tierra y mejores condiciones de vida. Trabajadores chilotes aportaron mano de obra para despejar bosques y construir. Comerciantes aprovecharon el paso de barcos por el estrecho. Y los pueblos originarios, como los huilliche, vieron reducidas sus tierras.",
        "Las causas fueron varias: el interés del Estado por afirmar la soberanía y poblar zonas extensas, la existencia de tierras que consideró disponibles, la salida de familias europeas por razones económicas y políticas, el comercio marítimo en el estrecho y la demanda de mano de obra. Hablamos de multicausalidad porque ninguna causa sola explica el proceso.",
        "Las perspectivas fueron distintas y a veces opuestas. Para el Estado, ocupar era un logro de desarrollo y soberanía. Para el colono, era una oportunidad con esfuerzo. Para el trabajador chilote, era un trabajo pagado y duro. Para los huilliche, fue una pérdida de tierras. Estudiar el proceso exige escuchar todas estas voces y no solo las de quienes hoy tienen más registros escritos.",
    ],
    vocab=[("colonización", "proceso de poblar y organizar un territorio con nuevos habitantes"), ("mano de obra", "trabajadores que realizan una labor"), ("conflicto de intereses", "situación en que los objetivos de dos grupos chocan"), ("pérdida de tierras", "reducción del territorio usado por un pueblo o familia"), ("agente del Estado", "persona que actúa en nombre del Estado")],
    worked=[
        ("Asociar actor e interés", "¿Qué interés expresa el colono alemán y cuál el agente del Estado?",
         ["El colono busca tierra y seguridad.", "El agente busca poblar el sur y fortalecer la presencia del Estado."], "Colono: tierra y seguridad; agente: poblar y fortalecer presencia"),
        ("Contrastar perspectivas", "¿Cómo ven la ocupación el dirigente huilliche y el agente del Estado?",
         ["El agente la ve como poblamiento y presencia.", "El dirigente la ve como reducción de la tierra de sus familias."], "El Estado, como poblamiento; el huilliche, como pérdida de tierras"),
    ],
    mistakes=[
        ("Atribuir el resultado a un solo grupo de inmigrantes.", "También participaron chilotes, otros pobladores y el Estado.", "Haz una lista de todos los actores presentes."),
        ("Pensar que los pueblos originarios fueron espectadores pasivos.", "Tenían intereses, reclamaban y se adaptaron.", "Incluye su voz y sus acciones."),
    ],
    T=[
        ("En Historia: ¿qué es la mano de obra?", "Los trabajadores que realizan una labor", "Los chilotes aportaron mano de obra."),
        ("{F} ¿Qué labor realiza el trabajador chilote?", "Despejar el bosque y construir", "Su voz lo dice."),
        ("{F} ¿Qué necesitan los barcos que pasan por el estrecho según el comerciante?", "Carbón y alimentos", "Su voz lo dice."),
        ("{F} ¿Qué dice el dirigente huilliche sobre su tierra?", "Que sus familias la usaban antes y hoy tienen menos", "Su voz lo dice."),
        ("Une cada actor con su interés: 1) agente del Estado, 2) colono alemán, 3) comerciante. a) vender a los barcos, b) poblar y fortalecer presencia, c) conseguir tierra y seguridad. Escribe las parejas.", "1-b, 2-c, 3-a", "Cada voz expresa un interés distinto."),
        ("{F} Elige el actor que vivió la ocupación como pérdida de tierras. A) el dirigente huilliche, B) el agente del Estado, C) el comerciante.", "A", "Lo dice en su voz."),
        ("=", "En una localidad de ejemplo trabajan 80 chilotes, 45 colonos y 15 funcionarios. ¿Cuántas personas son en total?", "80+45+15", "Se suman los tres grupos."),
        ("=", "En un contrato de ejemplo, un grupo despeja 36 hectáreas en 4 días con igual ritmo cada día. ¿Cuántas hectáreas despeja por día?", "36//4", "Se divide el total entre los días."),
        ("Una compañera dice: «El éxito del poblamiento fue solo de los alemanes». Menciona otro actor que contradiga esa frase.", "Los trabajadores chilotes que despejaban el bosque y construían", "Otros actores aportaron trabajo."),
        ("Explica por qué hablamos de multicausalidad al estudiar la ocupación del sur.", "Porque influyeron la soberanía, las tierras, la inmigración, el comercio marítimo y el trabajo, y no una sola causa", "Varias causas se combinaron."),
        ("{F} ¿En qué se diferencian la mirada del colono y la del dirigente huilliche?", "El colono ve una oportunidad con esfuerzo y el dirigente ve una pérdida de tierras", "Sus experiencias fueron opuestas."),
        ("Evalúa la frase «todos los habitantes del sur ganaron con la ocupación». A) es discutible porque algunos grupos perdieron tierras, B) es correcta, C) es correcta porque llegaron colonos.", "A", "Los efectos fueron desiguales."),
        ("Redacta una pregunta que contraste el interés del Estado con el de los huilliche.", "Por ejemplo: ¿qué buscaba cada uno con el uso de la tierra y quién decidía?", "La pregunta compara intereses y poder."),
    ],
    ctx=("{F} En un afiche escolar, el título dice «Los alemanes construyeron el sur». Con las voces de ejemplo, ¿qué actores agregarías y por qué?", "Agregaría a los trabajadores chilotes y al dirigente huilliche, porque aportaron trabajo y vieron reducidas sus tierras", "Un relato completo incluye a varios actores."),
    sc=[("En Historia: ¿qué es un conflicto de intereses?", "Una situación en que los objetivos de dos grupos chocan", "Describe tensiones como la de la tierra."),
        ("Nombra dos actores de la ocupación del sur.", "Por ejemplo: el Estado y los colonos", "Ambos participaron en el proceso."),
        ("¿Qué labor cumplían los chilotes en la ocupación?", "Aportaban mano de obra para despejar bosques y construir", "Es un aporte clave.")],
    op=("{F} Elige dos voces de ejemplo de arriba y escribe cinco líneas: qué busca cada una, una causa de la ocupación del sur y una diferencia de perspectiva entre ambas.",
        "El agente del Estado busca poblar el sur y fortalecer la presencia. El dirigente huilliche denuncia que sus familias tienen menos tierra. Una causa fue afirmar la soberanía en zonas extensas. El Estado ve poblamiento; el dirigente, pérdida de tierras.",
        ["dos voces", "una causa", "diferencia de perspectiva"], ["texto de cinco líneas"], ["atribuir todo a un solo grupo", "no marcar diferencia"], "Cuenta tu texto a alguien de tu casa y pídele que diga cuál es la diferencia."),
    reinforce="Haz una tabla con cinco actores y un interés para cada uno.",
    extend="Explica por qué escuchar varias voces cambia la manera de contar la ocupación del sur.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = "Dossier de ejemplo. Dato 1: una ley de 1845 autorizó traer colonos extranjeros; llegaron familias alemanas a Valdivia (1846) y a Llanquihue. Dato 2: el Estado fundó Fuerte Bulnes (1843) y Punta Arenas (1848) en el estrecho de Magallanes. Dato 3: trabajadores chilotes despejaron bosques y construyeron. Dato 4: familias de pueblos originarios vieron reducidas sus tierras. Dato 5: el estrecho era una ruta entre el Atlántico y el Pacífico."
build(
    OA, 5, F5,
    use="Aprenderé a construir un argumento sobre por qué el Estado ocupó el sur y qué papel cumplieron la inmigración y los pueblos originarios. Sirve para responder con equilibrio entre estrategia estatal, trabajo de varios grupos y costos para los pueblos originarios.",
    prior=["Conozco la ocupación, sus actores y sus fuentes.", "Sé distinguir cambio y continuidad.", "Sé escribir tesis, evidencias y límite."],
    explain=[
        "Un argumento sobre la ocupación del sur parte de una pregunta como «¿Por qué fue importante para el Estado ocupar el sur y quiénes participaron?». Una tesis posible es que el Estado ocupó el sur por razones estratégicas, mediante la inmigración y el trabajo de otros grupos, y que ese proceso tuvo un costo para los pueblos originarios.",
        "Las evidencias deben explicarse. El dato 5 y el dato 2 muestran la importancia estratégica del estrecho y la presencia estatal. El dato 1 muestra el papel de la inmigración europea. El dato 3 muestra que también hubo trabajadores chilotes, de modo que el resultado no se debe a un solo grupo. El dato 4 muestra el costo para los pueblos originarios, que perdieron parte de su tierra.",
        "El límite es importante. Con el dossier no sabemos cuántas hectáreas perdió cada comunidad ni cómo respondió cada una. Tampoco podemos afirmar que todos los colonos tuvieran la misma situación. Evita frases como «el sur estaba vacío», «todos ganaron» o «los alemanes lo hicieron todo».",
    ],
    vocab=[("tesis", "afirmación principal que se defiende"), ("evidencia", "dato que apoya la tesis"), ("costo histórico", "efecto negativo que tuvo un proceso para algún grupo"), ("estrategia", "plan para lograr un objetivo de largo plazo"), ("límite", "aquello que la evidencia no permite afirmar")],
    worked=[
        ("Elegir evidencias", "Para sostener que el sur tuvo importancia estratégica, ¿qué dos datos del dossier sirven?",
         ["El dato 2 muestra fuertes y fundación de Punta Arenas en el estrecho.", "El dato 5 explica que era una ruta entre dos océanos."], "Datos 2 y 5"),
        ("Reconocer el costo", "¿Qué dato del dossier muestra un costo del proceso para algunos grupos?",
         ["Reviso los datos que hablan de personas afectadas.", "El dato 4 dice que familias de pueblos originarios vieron reducidas sus tierras."], "El dato 4"),
    ],
    mistakes=[
        ("Escribir una tesis que omite a los pueblos originarios.", "Deja fuera un actor central y el costo del proceso.", "Incluye el dato 4."),
        ("Atribuir todo a un solo grupo de inmigrantes.", "Hubo otros actores, como trabajadores chilotes.", "Usa el dato 3 para corregir."),
    ],
    T=[
        ("En Historia: ¿qué es la estrategia?", "Un plan para lograr un objetivo de largo plazo", "La ocupación del sur respondió a una estrategia estatal."),
        ("{F} ¿Qué dato muestra el papel de la inmigración europea? A) dato 1, B) dato 4, C) dato 5.", "A", "El dato 1 menciona colonos alemanes."),
        ("{F} ¿Qué dato muestra que el trabajo no fue solo de colonos europeos?", "El dato 3", "Menciona a los trabajadores chilotes."),
        ("{F} ¿Qué dato muestra un costo para pueblos originarios?", "El dato 4", "Habla de tierras reducidas."),
        ("Elige la tesis mejor formulada. A) El sur estaba vacío y los alemanes lo poblaron, B) El Estado ocupó el sur por razones estratégicas con inmigración y trabajo de varios grupos, y con un costo para los pueblos originarios, C) Nada cambió en el sur.", "B", "Es defendible con el dossier."),
        ("Una compañera dice que el dato 1 prueba que «los alemanes hicieron todo». ¿Qué dato lo contradice?", "El dato 3, que muestra el trabajo de los chilotes", "Otros grupos también trabajaron."),
        ("=", "{F} Si el dossier tiene 5 datos y 2 se refieren al estrecho (2 y 5), ¿cuántos datos hablan de otros temas?", "5-2", "Se restan los datos del estrecho."),
        ("=", "Un grupo escribe un texto de 15 líneas: 2 de tesis, 9 de evidencias y el resto de límite. ¿Cuántas líneas son de límite?", "15-2-9", "Se restan tesis y evidencias del total."),
        ("{F} Con los datos 3 y 4, redacta una conclusión proporcional.", "Trabajadores chilotes despejaron bosques y construyeron, mientras familias de pueblos originarios vieron reducidas sus tierras", "Une dos procesos del dossier."),
        ("Explica por qué una tesis sobre la ocupación debe nombrar un costo para los pueblos originarios.", "Porque el proceso redujo sus tierras y omitirlo mostraría una versión incompleta", "El dato 4 es parte central del proceso."),
        ("Un compañero escribe: «Todos ganaron con la ocupación del sur». Señala la exageración.", "«Todos» excede la evidencia, porque el dato 4 muestra tierras reducidas para algunos", "Es una afirmación absoluta."),
        ("Evalúa este argumento: «El estrecho era una ruta clave (datos 2 y 5), y la ocupación tuvo un costo para los pueblos originarios (dato 4)». A) es sólido porque une estrategia y costo, B) es débil porque solo presenta datos sobre colonos alemanes, C) es falso porque el estrecho no tenía ningún valor para Chile.", "A", "Usa evidencias de ambos lados."),
        ("Escribe una pregunta que exigiría otra fuente para completar el argumento.", "Por ejemplo: ¿cómo respondieron las comunidades a la reducción de sus tierras?", "La pregunta indica un vacío del dossier."),
    ],
    ctx=("{F} En una exposición alguien dice «La ocupación del sur fue solo una historia de progreso». Con el dossier, escribe tu respuesta en dos frases con una evidencia.", "Fue también una historia de costos: el dato 4 muestra que familias de pueblos originarios vieron reducidas sus tierras", "La respuesta debe usar el dato 4."),
    sc=[("En Historia: ¿qué es un costo histórico?", "Un efecto negativo que tuvo un proceso para algún grupo", "Aplica a la pérdida de tierras."),
        ("Nombra un dato del dossier sobre importancia estratégica.", "Por ejemplo: el estrecho era una ruta entre el Atlántico y el Pacífico", "Es el dato 5."),
        ("¿Qué grupos participaron además de los alemanes?", "Los trabajadores chilotes, entre otros", "Es el dato 3.")],
    op=("{F} Con el dossier de ejemplo de arriba, escribe un párrafo de siete líneas que responda: «¿Por qué fue importante ocupar el sur y qué costos tuvo?». Incluye una tesis, dos evidencias explicadas y un límite.",
        "El Estado ocupó el sur por razones estratégicas: el estrecho era una ruta entre dos océanos y se fundaron Fuerte Bulnes y Punta Arenas. La inmigración europea y el trabajo de chilotes ayudaron a poblar. Pero familias de pueblos originarios vieron reducidas sus tierras. Límite: el dossier no dice cuántas hectáreas perdió cada comunidad.",
        ["tesis", "dos evidencias explicadas", "límite"], ["párrafo de siete líneas"], ["omitir a los pueblos originarios", "no explicar los datos"], "Pide a alguien de tu casa que marque tu tesis."),
    reinforce="Escribe tu tesis en una frase y las dos evidencias que la apoyan.",
    extend="Escribe una segunda tesis centrada en los pueblos originarios y el dato que necesitarías para sostenerla.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 6
F6 = "Resumen de ejemplo para evaluar proyecciones. Huellas visibles: ciudades y pueblos fundados en el siglo XIX en el sur; presencia de apellidos y tradiciones de origen europeo; ganadería ovina en Magallanes; Chiloé con trabajadores que migraron a otras zonas. Huellas menos visibles: pérdida de tierras de familias huilliche y de otros pueblos; gran disminución de la población de pueblos australes como los selk'nam por la violencia, las enfermedades y el desplazamiento; demandas de tierras que continuaron en el tiempo."
build(
    OA, 6, F6,
    use="Aprenderé a evaluar qué proyecciones dejó la ocupación del sur, es decir, qué consecuencias siguieron y qué límites tienen nuestras explicaciones. Sirve para comprender el presente del sur de Chile con memoria histórica.",
    prior=["Conozco la ocupación del sur, sus actores y su costo.", "Sé argumentar con evidencia.", "Sé que toda fuente tiene límites."],
    explain=[
        "Evaluar una proyección significa preguntar qué consecuencias de largo plazo tuvo un proceso. La ocupación del sur dejó huellas visibles: ciudades y pueblos fundados en el siglo XIX, tradiciones y apellidos de origen europeo, la ganadería ovina en Magallanes y la presencia de trabajadores chilotes en distintas zonas.",
        "También dejó huellas menos visibles. Familias huilliche y de otros pueblos perdieron parte de sus tierras, y las demandas de tierra continuaron en el tiempo. En el extremo austral, pueblos como los selk'nam sufrieron una gran disminución de su población por la violencia, las enfermedades y el desplazamiento. Estas consecuencias no se ven en un monumento, pero forman parte de la historia del sur.",
        "Al evaluar, hay que reconocer los límites de lo que sabemos: no todos los datos están disponibles, muchas voces dejaron pocos registros escritos y no todas las comunidades vivieron lo mismo. Una buena evaluación evita decir que el proceso fue solo progreso o solo despojo, y propone preguntas para seguir investigando.",
    ],
    vocab=[("proyección histórica", "consecuencia de largo plazo de un proceso"), ("huella", "marca que deja un proceso en el paisaje, la cultura o la sociedad"), ("memoria histórica", "forma en que una sociedad recuerda y valora su pasado"), ("desplazamiento", "traslado forzado o presionado de personas fuera de su lugar"), ("demanda de tierras", "reclamo de un pueblo o comunidad por recuperar o reconocer tierras")],
    worked=[
        ("Clasificar huellas", "En el resumen de ejemplo, ¿la ganadería ovina en Magallanes es una huella visible o menos visible? ¿Y la pérdida de tierras huilliche?",
         ["La ganadería ovina se ve en el paisaje y la economía: visible.", "La pérdida de tierras es un proceso social que no se ve en el paisaje: menos visible."], "Ganadería ovina: visible; pérdida de tierras: menos visible"),
        ("Reconocer un límite", "¿Por qué es difícil medir con exactitud cuánto disminuyó la población selk'nam con las fuentes de ejemplo?",
         ["El resumen menciona causas, pero no da cifras.", "Muchas voces dejaron pocos registros escritos."], "Porque faltan cifras y registros"),
    ],
    mistakes=[
        ("Evaluar el proceso solo como progreso.", "Deja fuera costos como la pérdida de tierras.", "Incluye huellas visibles y menos visibles."),
        ("Evaluar el proceso solo como despojo.", "Deja fuera la fundación de ciudades y el trabajo de varios grupos.", "Reconoce avances y costos a la vez."),
    ],
    T=[
        ("En Historia: ¿qué es una proyección histórica?", "Una consecuencia de largo plazo de un proceso", "Es lo que se evalúa en esta clase."),
        ("{F} ¿Qué actividad económica se menciona en Magallanes?", "Ganadería ovina", "El resumen la lista como huella visible."),
        ("En Historia: ¿qué es una huella?", "Una marca que deja un proceso en el paisaje, la cultura o la sociedad", "Puede ser visible o menos visible."),
        ("{F} ¿Qué causas de la disminución de población de los selk'nam menciona el resumen?", "Violencia, enfermedades y desplazamiento", "El resumen las nombra."),
        ("{F} Clasifica como huella visible o menos visible: «ciudades fundadas en el siglo XIX».", "Visible", "Se ven en el paisaje."),
        ("{F} Clasifica como huella visible o menos visible: «demandas de tierras que continuaron en el tiempo».", "Menos visible", "Es un proceso social."),
        ("=", "En una comunidad de ejemplo, antes tenía 1.000 hectáreas y hoy conserva 350. ¿Cuántas hectáreas perdió?", "1000-350", "Se resta lo que conserva a lo que tenía."),
        ("=", "Una población de ejemplo de 800 personas disminuyó a 200 en cierto periodo. ¿Cuántas personas menos hay?", "800-200", "Se resta la población final de la inicial."),
        ("Explica por qué evaluar la ocupación solo como progreso es insuficiente.", "Porque deja fuera costos como la pérdida de tierras y la disminución de población de pueblos originarios", "Una evaluación equilibrada incluye costos."),
        ("{F} Una compañera dice: «Hoy no queda ninguna huella de los pueblos originarios en el sur». Corrige con un dato del resumen.", "Hay demandas de tierras que continuaron en el tiempo", "El resumen habla de continuidad de demandas."),
        ("{F} ¿Qué límite tiene este resumen para evaluar el impacto exacto sobre las comunidades?", "No entrega cifras ni la voz de cada comunidad", "Es un vacío de la fuente."),
        ("Evalúa la frase «la ocupación del sur fue solo progreso». A) es incompleta porque dejó costos para los pueblos originarios, B) es correcta, C) es correcta porque se fundaron ciudades.", "A", "Ignora los costos."),
        ("Propón una pregunta para seguir investigando sobre el sur.", "Por ejemplo: ¿cómo se recuerdan hoy en la zona estos hechos y quiénes los cuentan?", "La pregunta amplía la mirada."),
    ],
    ctx=("{F} En una charla escolar sobre una ciudad del sur se dice «la ciudad nació de la nada en el siglo XIX». Con el resumen, escribe una frase que pida más precisión.", "Antes de la ciudad había pueblos originarios en la zona; el siglo XIX trajo colonos, trabajo de chilotes y pérdida de tierras", "La frase debe incluir a quienes ya vivían allí."),
    sc=[("En Historia: ¿qué es la memoria histórica?", "La forma en que una sociedad recuerda y valora su pasado", "Orienta cómo se cuenta el proceso."),
        ("Nombra una huella visible de la ocupación.", "Por ejemplo: ciudades fundadas en el siglo XIX", "Está en el resumen."),
        ("Nombra una huella menos visible.", "Por ejemplo: la pérdida de tierras de familias huilliche", "Está en el resumen.")],
    op=("{F} Con el resumen de ejemplo de arriba, escribe un párrafo de ocho líneas que evalúe la ocupación del sur: nombra una huella visible, una menos visible, un avance, un costo y un límite de lo que sabemos.",
        "Una huella visible es la fundación de ciudades como Puerto Montt; una menos visible es la pérdida de tierras de familias huilliche. Un avance fue el poblamiento y la ganadería; un costo, la disminución de pueblos australes. Límite: no tenemos cifras exactas ni la voz de cada comunidad. Conviene seguir investigando.",
        ["huella visible y menos visible", "avance y costo", "límite"], ["párrafo de ocho líneas"], ["decir que fue solo progreso", "omitir el límite"], "Pide a alguien de tu casa que verifique que nombraste avance y costo."),
    reinforce="Haz una tabla con dos columnas (huellas visibles y menos visibles) con dos datos en cada una.",
    extend="Escribe dos preguntas para entrevistar a un historiador o a un integrante de una comunidad sobre estos hechos.",
    materials=MAT,
)
