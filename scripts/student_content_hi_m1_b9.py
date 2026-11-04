"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 18 (cuestión social, actores y formas de organización)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 18"
MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = "Línea de tiempo: 1853, se funda la Sociedad Tipográfica de Socorros Mutuos; 1887, nace el Partido Demócrata; 1903, huelga de portuarios en Valparaíso; 1905, protestas en Santiago por el precio de la carne; 1906, ley de habitaciones obreras; 1907, matanza en la Escuela Santa María de Iquique; 1909, se funda la Federación Obrera de Chile; 1912, Luis Emilio Recabarren funda el Partido Obrero Socialista; 1920, Arturo Alessandri gana la elección presidencial; 1924, se aprueban leyes sociales."
build(
    OA, 1, F1,
    use="Aprenderé a ubicar en el tiempo la cuestión social y las formas de organización de los trabajadores, y a explicar qué fue la cuestión social. Sirve para comprender el origen de los derechos laborales y de la política social en Chile.",
    prior=["Conozco el ciclo del salitre y el orden parlamentario.", "Sé leer una línea de tiempo.", "Sé qué es un conventillo."],
    explain=[
        "Se llama cuestión social al conjunto de problemas de vida y de trabajo que enfrentaban los sectores populares hacia fines del siglo XIX y comienzos del XX. Entre ellos estaban los bajos salarios, las largas jornadas, la falta de protección ante accidentes y enfermedades, las viviendas hacinadas y las altas tasas de enfermedad y de mortalidad. Estos problemas se agravaron con el crecimiento de las ciudades y de las minas.",
        "Los factores que la originaron fueron varios: el crecimiento urbano rápido por la migración desde el campo, la expansión de la minería del salitre, la industrialización incipiente, el aumento de la población y un Estado que intervenía poco en asuntos laborales y de vivienda. Por eso la cuestión social no se explica solo por la pobreza individual: tuvo causas económicas, sociales y políticas.",
        "Los sectores populares respondieron organizándose. Crearon sociedades de socorros mutuos, que ayudaban a sus socios en caso de enfermedad o muerte; mancomunales y sociedades de resistencia, que defendían sus intereses; sindicatos y federaciones; y partidos como el Demócrata y el Obrero Socialista. También usaron la huelga, que es la suspensión colectiva del trabajo para exigir mejoras. A su vez, los gobiernos tardaron en responder y hubo episodios de represión.",
    ],
    vocab=[("cuestión social", "conjunto de problemas de vida y trabajo de los sectores populares hacia 1900"), ("huelga", "suspensión colectiva del trabajo para exigir mejoras"), ("sociedad de socorros mutuos", "organización que ayudaba a sus socios en caso de enfermedad o muerte"), ("sindicato", "organización de trabajadores para defender sus intereses"), ("represión", "uso de la fuerza por parte de las autoridades para detener una protesta")],
    worked=[
        ("Ubicar en el tiempo", "Con la línea de tiempo, ¿cuántos años pasaron entre la huelga de portuarios de Valparaíso y la matanza de la Escuela Santa María de Iquique?",
         ["Busco las fechas: 1903 y 1907.", "Resto: 1907 - 1903."], "4 años"),
        ("Clasificar una organización", "La Sociedad Tipográfica de Socorros Mutuos (1853), ¿qué tipo de organización era?",
         ["Su nombre indica ayuda entre socios.", "Las sociedades de socorros mutuos ayudaban en caso de enfermedad o muerte."], "Una sociedad de socorros mutuos"),
    ],
    mistakes=[
        ("Reducir la cuestión social a la pobreza individual.", "Tuvo causas económicas, sociales y políticas.", "Busca causas del sistema, no solo de las personas."),
        ("Presentar a los trabajadores como receptores pasivos.", "Se organizaron, hicieron huelgas y formaron partidos.", "Incluye sus acciones."),
    ],
    T=[
        ("En Historia: ¿qué es la cuestión social?", "El conjunto de problemas de vida y trabajo de los sectores populares hacia 1900", "Es el concepto central de la clase."),
        ("{F} ¿En qué año se funda la Federación Obrera de Chile?", "1909", "La línea de tiempo lo indica."),
        ("En Historia: ¿qué es una huelga?", "La suspensión colectiva del trabajo para exigir mejoras", "Fue una forma de lucha obrera."),
        ("{F} ¿Quién fundó el Partido Obrero Socialista?", "Luis Emilio Recabarren", "La línea lo señala."),
        ("{F} ¿Qué ley se aprobó en 1906? A) la ley de habitaciones obreras, B) la ley del voto femenino, C) la ley de la Constitución de 1925.", "A", "La línea lo señala."),
        ("Une cada organización con su función: 1) sociedad de socorros mutuos, 2) sindicato, 3) partido político. a) defender intereses de los trabajadores en el trabajo, b) ayudar a socios en enfermedad o muerte, c) participar en elecciones con un programa. Escribe las parejas.", "1-b, 2-a, 3-c", "Cada organización tiene un fin distinto."),
        ("{F} Ordena de más antiguo a más reciente: Partido Obrero Socialista, Partido Demócrata, Federación Obrera de Chile y matanza de la Escuela Santa María de Iquique.", "Partido Demócrata, matanza de Iquique, Federación Obrera de Chile, Partido Obrero Socialista", "Se ordenan por sus años: 1887, 1907, 1909 y 1912."),
        ("{F} ¿Qué protestas de 1905 se mencionan en la línea de tiempo?", "Las protestas en Santiago por el precio de la carne", "La línea las señala."),
        ("Una compañera dice: «La cuestión social fue solo un problema de pobreza de algunas familias». ¿Qué corrección haces?", "Tuvo causas económicas, sociales y políticas, como el crecimiento urbano y la poca intervención del Estado", "No se reduce a causas individuales."),
        ("{F} ¿Qué hecho de 1907 muestra una respuesta violenta de las autoridades a una protesta?", "La matanza en la Escuela Santa María de Iquique", "Es un ejemplo de represión."),
        ("Explica por qué los sectores populares no fueron solo receptores pasivos de reformas.", "Porque crearon organizaciones, hicieron huelgas y formaron partidos para exigir cambios", "Tuvieron capacidad de actuar."),
        ("Evalúa la frase «la cuestión social fue solo un problema de las ciudades». A) es incompleta porque también afectó a las minas y a las oficinas salitreras, B) es correcta, C) es correcta porque había conventillos.", "A", "Afectó a varios lugares."),
        ("Una persona dice: «Las protestas obreras no tuvieron ningún efecto». Da una razón para dudar usando la línea de tiempo.", "Después de ellas se aprobaron la ley de habitaciones obreras en 1906 y las leyes sociales de 1924", "Hubo respuestas legislativas."),
    ],
    ctx=("Un afiche escolar dice: «Los obreros de 1900 esperaban pasivamente que el Estado los ayudara». Escribe una frase que lo corrija con la línea de tiempo.", "Los trabajadores se organizaron en sociedades, sindicatos y partidos y usaron huelgas para exigir mejoras", "La corrección muestra su agencia."),
    sc=[("En Historia: ¿qué es un sindicato?", "Una organización de trabajadores para defender sus intereses", "Es una forma de organización obrera."),
        ("Nombra una forma de lucha obrera.", "Por ejemplo: la huelga", "Está en la explicación."),
        ("{F} ¿Qué se funda en 1887?", "El Partido Demócrata", "Está en la línea de tiempo.")],
    op=("{F} Con la línea de tiempo de arriba, escribe cinco líneas que expliquen qué fue la cuestión social y cómo respondieron los sectores populares. Nombra una causa, dos organizaciones, una forma de lucha y una fecha.",
        "La cuestión social fueron los problemas de vida y trabajo de los sectores populares hacia 1900. Una causa fue el crecimiento rápido de las ciudades. Los trabajadores crearon la Federación Obrera de Chile (1909) y el Partido Obrero Socialista (1912) y usaron huelgas, como la de portuarios de Valparaíso en 1903.",
        ["una causa", "dos organizaciones", "una forma de lucha", "una fecha"], ["texto de cinco líneas"], ["decir que fue solo pobreza individual", "no incluir fechas"], "Léele tu texto a alguien de tu casa y pídele que anote las organizaciones."),
    reinforce="Escribe las diez fechas de la línea de tiempo y, junto a cada una, una palabra que la resuma.",
    extend="Escribe una frase que explique por qué una huelga puede ser una forma de presión legítima en una sociedad.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = "Fuente A (descripción de un conventillo, texto de ejemplo): «En un patio de ejemplo viven 40 personas en 10 piezas; hay un solo grifo de agua y las habitaciones tienen poca ventilación.» Fuente B (petición de una mancomunal, texto de ejemplo): «Solicitamos jornadas más cortas, salarios justos y que no se nos pague con fichas.» Fuente C (editorial de un periódico, texto de ejemplo): «Las huelgas alteran el orden público; el gobierno debe restablecerlo.» Fuente D (tabla de ejemplo): de cada 1.000 niños nacidos en un barrio de ejemplo, murieron 300 antes de cumplir un año. Fuente E (historiadora actual, texto de ejemplo): «Las organizaciones populares fueron actores políticos y no solo víctimas.»"
build(
    OA, 2, F2,
    use="Aprenderé a leer descripciones de vivienda, peticiones obreras, editoriales y tablas de salud sobre la cuestión social, detectando intención y límites. Sirve para entender los problemas sin reducirlos a pobreza individual y reconocer la voz de los trabajadores.",
    prior=["Conozco qué fue la cuestión social.", "Distingo fuentes primarias y secundarias.", "Sé calcular porcentajes y proporciones."],
    explain=[
        "Las fuentes de la cuestión social muestran perspectivas distintas. Una descripción de conventillo permite ver las condiciones materiales de vivienda. Una petición de una organización obrera expresa las demandas de los trabajadores. Un editorial de periódico expresa la postura de un diario, que puede ver las huelgas como un problema de orden. Una tabla de mortalidad infantil cuenta casos. Una historiadora actual interpreta el conjunto.",
        "Cada una tiene límites. La descripción de ejemplo muestra un patio, no todos los conventillos. La petición de la mancomunal dice lo que los trabajadores querían, no si lo lograron. El editorial muestra la mirada de quienes defendían el orden y no la de los trabajadores. Y la tabla de mortalidad infantil muestra el resultado, pero no explica las causas por sí sola.",
        "Para evitar reducir la cuestión social a pobreza individual, hay que mirar las causas del sistema: salarios bajos, falta de servicios, hacinamiento y poca protección legal. Y para evitar mostrar a los sectores populares como receptores pasivos, hay que incluir sus peticiones y organizaciones. Contrastar las fuentes ayuda a entender el conflicto desde varias voces.",
    ],
    vocab=[("mortalidad infantil", "muertes de niños y niñas antes de cumplir un año"), ("petición", "texto en que un grupo solicita algo a las autoridades o a los empleadores"), ("orden público", "situación de calma y funcionamiento normal de la vida en la ciudad"), ("ventilación", "entrada y salida de aire en un lugar"), ("jornada", "cantidad de horas de trabajo en un día")],
    worked=[
        ("Calcular una proporción", "En la Fuente D, ¿qué porcentaje de los niños nacidos murió antes de cumplir un año?",
         ["Murieron 300 de cada 1.000.", "300 de 1.000 es el 30 %."], "El 30 %"),
        ("Identificar la perspectiva", "¿Qué perspectiva expresa la Fuente C respecto de las huelgas?",
         ["Dice que alteran el orden público.", "Pide que el gobierno lo restablezca."], "La de quienes defienden el orden público"),
    ],
    mistakes=[
        ("Tomar el editorial como descripción neutral de las huelgas.", "Expresa la postura de un diario.", "Pregunta qué intereses defiende."),
        ("Usar la tabla de mortalidad para culpar a las familias.", "La tabla muestra resultados, y las causas incluyen vivienda, agua y salarios.", "Busca causas estructurales."),
    ],
    T=[
        ("En Historia: ¿qué es la mortalidad infantil?", "Las muertes de niños y niñas antes de cumplir un año", "La Fuente D la mide."),
        ("{F} ¿Cuántas personas viven en el patio de la Fuente A?", "40", "La descripción lo indica."),
        ("En Historia: ¿qué es una petición?", "Un texto en que un grupo solicita algo a las autoridades o a los empleadores", "La Fuente B lo es."),
        ("{F} ¿La Fuente E es primaria o secundaria?", "Secundaria", "La escribe una historiadora actual."),
        ("{F} ¿Qué solicita la mancomunal de la Fuente B? A) jornadas más cortas, salarios justos y no pagar con fichas, B) más impuestos, C) menos escuelas.", "A", "La petición lo indica."),
        ("{F} Una compañera dice que la Fuente C muestra la opinión de los trabajadores. ¿Qué corrección haces?", "La Fuente C es un editorial que expresa la postura de un diario que defiende el orden público", "No es la voz de los trabajadores."),
        ("{F} ¿Qué problemas de vivienda muestra la Fuente A?", "Hacinamiento (40 personas en 10 piezas), un solo grifo de agua y poca ventilación", "La descripción los enumera."),
        ("{F} ¿Qué no puede responder la Fuente D: cuántos niños murieron o por qué murieron?", "Por qué murieron, porque la tabla solo da cifras", "Es un límite de la tabla."),
        ("{F} ¿Qué fuente muestra las demandas de los trabajadores? A) la A, B) la B, C) la C.", "B", "La petición de la mancomunal las expresa."),
        ("{F} Explica por qué conviene contrastar las Fuentes B y C.", "Porque la petición muestra lo que querían los trabajadores y el editorial muestra la postura de quienes defendían el orden", "Dos perspectivas opuestas sobre la huelga."),
        ("{F} Redacta una conclusión de una frase con las Fuentes A y D sin exagerar.", "El hacinamiento y la alta mortalidad infantil formaron parte de los problemas de vivienda y salud de un barrio de ejemplo", "Une vivienda y salud."),
        ("{F} Evalúa la frase «la Fuente D demuestra que las madres cuidaban mal a sus hijos». A) es injusta porque la tabla no muestra causas y hay factores como vivienda y agua, B) es correcta, C) es correcta porque murieron niños.", "A", "La tabla no culpa a nadie."),
        ("¿Qué otra fuente sumarías para conocer la voz de las mujeres trabajadoras? Escríbela y explica para qué.", "Por ejemplo: un testimonio de una costurera de la época, para conocer su jornada y su salario", "Completa un vacío de las fuentes."),
    ],
    ctx=("{F} Un compañero copia la Fuente C en un afiche con el título «Las huelgas solo causaron desorden». ¿Qué fuente agregarías y por qué?", "La Fuente B, porque muestra las demandas de los trabajadores", "Se necesita contrastar para ver el conflicto."),
    sc=[("En Historia: ¿qué es el orden público?", "La situación de calma y funcionamiento normal de la vida en la ciudad", "Es lo que defendía el editorial."),
        ("¿Qué mide la mortalidad infantil?", "Las muertes de niños antes de cumplir un año", "La Fuente D la mide."),
        ("¿Una tabla de mortalidad explica por sí sola las causas? Responde sí o no y por qué.", "No, porque solo muestra resultados", "Hay que buscar otras fuentes.")],
    op=("{F} Con las Fuentes A a E de arriba, escribe un párrafo de siete líneas que responda: «¿Qué problemas vivían los sectores populares y qué pedían?». Incluye un dato numérico, una petición, una postura opuesta y un límite.",
        "En un patio de ejemplo vivían 40 personas en 10 piezas, y en la tabla murieron 300 de cada 1.000 niños antes de cumplir un año. La mancomunal pedía jornadas más cortas y no ser pagada con fichas. El editorial defendía el orden público. Límite: las fuentes no dicen qué se logró.",
        ["dato numérico", "una petición", "postura opuesta", "un límite"], ["párrafo de siete líneas"], ["culpar a las familias", "no incluir la petición"], "Pide a alguien de tu casa que revise que usaste una petición y una postura opuesta."),
    reinforce="Haz una tabla con las Fuentes A a E: quién habla, qué dice y un límite.",
    extend="Escribe una pregunta que la Fuente D no permite responder.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = "Cuadro de ejemplo. Cambio: crecieron las ciudades y los campamentos mineros; surgieron mancomunales, sindicatos y partidos obreros; se hicieron huelgas importantes; se aprobaron las primeras leyes sociales (habitaciones obreras, descanso dominical, accidentes del trabajo); crecieron los sectores medios de empleados y profesionales. Continuidad: los conventillos seguían hacinados; los salarios eran bajos; el voto seguía restringido; las autoridades respondían a veces con represión; las mujeres seguían sin derecho a voto."
build(
    OA, 3, F3,
    use="Aprenderé a distinguir qué cambió y qué continuó en la sociedad chilena entre 1880 y 1925, ubicando los cambios en el territorio. Sirve para evaluar las transformaciones sociales sin suponer que resolvieron los problemas.",
    prior=["Conozco la cuestión social y sus fuentes.", "Sé distinguir cambio y continuidad.", "Sé qué es una escala."],
    explain=[
        "En el cambio de siglo, la sociedad chilena se transformó. Crecieron las ciudades, como Santiago y Valparaíso, y los campamentos mineros del norte. Surgieron nuevas formas de organización de los trabajadores: mancomunales, sindicatos y partidos obreros. Hubo huelgas importantes y se aprobaron las primeras leyes sociales, como la de habitaciones obreras (1906) y la de descanso dominical (1907). También crecieron los sectores medios: empleados, profesores y profesionales.",
        "Pero muchas condiciones continuaron. Los conventillos siguieron hacinados, los salarios eran bajos y el voto seguía restringido. Las autoridades respondieron a veces con represión, como en Iquique en 1907. Las mujeres, aunque trabajaban en fábricas, talleres y servicios, seguían sin derecho a voto. Es decir, las leyes sociales fueron un primer paso, no una solución completa.",
        "El territorio explica diferencias. En el norte salitrero predominaban campamentos, pulperías y fichas; en Valparaíso y Santiago, conventillos y talleres; en el campo, haciendas e inquilinaje. Por eso la cuestión social tuvo rostros distintos según el lugar. Para comparar, se usa un cuadro de cambio y continuidad y se agrega siempre dónde ocurre cada proceso.",
    ],
    vocab=[("ley social", "ley que protege a los trabajadores y regula vivienda, descanso o accidentes"), ("sectores medios", "grupos de empleados, profesionales y comerciantes que no son ni obreros ni grandes propietarios"), ("mancomunal", "organización de trabajadores que reunía a distintas ocupaciones de un lugar"), ("descanso dominical", "derecho a no trabajar los domingos"), ("accidente del trabajo", "lesión que sufre una persona mientras trabaja")],
    worked=[
        ("Clasificar", "Del cuadro de ejemplo: «se aprobaron las primeras leyes sociales» y «los conventillos seguían hacinados». ¿Cuál es cambio y cuál continuidad?",
         ["Las leyes sociales son una novedad: cambio.", "El hacinamiento sigue: continuidad."], "Leyes sociales: cambio; hacinamiento: continuidad"),
        ("Territorio", "¿En qué se diferencia la cuestión social en el norte salitrero y en Valparaíso?",
         ["En el norte hay campamentos, pulperías y fichas.", "En Valparaíso hay conventillos y talleres."], "Norte: campamentos y fichas; Valparaíso: conventillos y talleres"),
    ],
    mistakes=[
        ("Creer que las primeras leyes sociales resolvieron la cuestión social.", "Fueron un primer paso y los problemas siguieron.", "Revisa qué continuó después de las leyes."),
        ("Hablar de la cuestión social como si fuera igual en todo el país.", "Cambiaba según el lugar.", "Indica la zona en cada ejemplo."),
    ],
    T=[
        ("En Historia: ¿qué es una ley social?", "Una ley que protege a los trabajadores y regula vivienda, descanso o accidentes", "Fue la respuesta legislativa."),
        ("{F} ¿Qué ley se aprobó sobre el descanso, según el cuadro?", "La de descanso dominical", "El cuadro la menciona."),
        ("En Historia: ¿qué es un accidente del trabajo?", "Una lesión que sufre una persona mientras trabaja", "Fue objeto de una ley social."),
        ("{F} Clasifica como cambio o continuidad: «surgieron mancomunales y sindicatos».", "Cambio", "Son organizaciones nuevas."),
        ("{F} Clasifica como cambio o continuidad: «el voto seguía restringido».", "Continuidad", "El cuadro lo lista como continuidad."),
        ("{F} Elige el cambio. A) los salarios eran bajos, B) crecieron los sectores medios, C) las mujeres seguían sin voto.", "B", "Las otras son continuidades."),
        ("{F} ¿Qué cambio en la organización de los trabajadores muestra el cuadro?", "Surgieron mancomunales, sindicatos y partidos obreros", "El cuadro lo lista entre los cambios."),
        ("{F} ¿Qué continuidad muestra que el conflicto entre trabajadores y autoridades seguía?", "Las autoridades respondían a veces con represión", "El cuadro la lista como continuidad."),
        ("Explica por qué las leyes sociales fueron un primer paso y no una solución completa.", "Porque los conventillos seguían hacinados, los salarios eran bajos y el voto seguía restringido", "Los problemas continuaban."),
        ("{F} Una compañera dice: «Con las primeras leyes, los obreros dejaron de protestar». Corrige con un dato del cuadro.", "Hubo huelgas importantes y a veces las autoridades respondieron con represión", "El conflicto continuó."),
        ("{F} ¿Qué diferencia territorial muestra la explicación entre el norte y el campo?", "En el norte había campamentos y pulperías y en el campo haciendas e inquilinaje", "La cuestión social tenía rostros distintos."),
        ("Evalúa la frase «hubo cambios importantes, pero muchos problemas continuaron». A) es razonable, B) es falsa porque nada cambió, C) es falsa porque todo se resolvió.", "A", "Combina cambio y continuidad."),
        ("Propón una pregunta de territorio sobre la vida de una familia obrera.", "Por ejemplo: ¿cómo cambiaba la vida de una familia obrera en el norte salitrero comparada con una de Valparaíso?", "La pregunta compara lugares."),
    ],
    ctx=("{F} Un video escolar dice: «Las leyes de 1906 y 1907 terminaron con la cuestión social». Con el cuadro, escribe una frase que lo corrija.", "Las leyes fueron un primer paso, pero los conventillos hacinados, los salarios bajos y la represión continuaron", "La frase debe incluir cambio y continuidad."),
    sc=[("En Historia: ¿qué es un descanso dominical?", "El derecho a no trabajar los domingos", "Fue regulado en 1907."),
        ("Nombra un cambio del periodo.", "Por ejemplo: surgieron sindicatos y partidos obreros", "Está en el cuadro."),
        ("Nombra una continuidad del periodo.", "Por ejemplo: los conventillos seguían hacinados", "Está en el cuadro.")],
    op=("{F} Con el cuadro de ejemplo de arriba, construye una tabla de dos columnas (cambio y continuidad) con al menos cuatro filas, y escribe una frase final que compare dos lugares (por ejemplo, el norte salitrero y Valparaíso).",
        "Cambio: surgen mancomunales y sindicatos; cambio: primeras leyes sociales; cambio: crecen los sectores medios; cambio: huelgas. Continuidad: conventillos hacinados; continuidad: salarios bajos; continuidad: voto restringido. En el norte había campamentos y fichas y en Valparaíso conventillos y talleres.",
        ["dos columnas", "cuatro filas", "comparación de dos lugares"], ["tabla y frase"], ["poner todo como cambio", "no comparar lugares"], "Revisa con alguien de tu casa que cada dato esté en su columna."),
    reinforce="Escribe cuatro datos del cuadro y clasifícalos como cambio o continuidad.",
    extend="Escribe una pregunta sobre cómo vivieron las mujeres trabajadoras los cambios de este periodo.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = "Voces de ejemplo, redactadas para este cuaderno. Obrero portuario: «Pedimos mejores sueldos y jornadas más cortas.» Dirigente de una mancomunal: «Nos unimos para defendernos y ayudarnos entre trabajadores.» Industrial: «Si suben los sueldos, mis costos aumentan.» Médico de la época: «En los conventillos las enfermedades se propagan por el hacinamiento.» Profesora de una escuela pública: «Mis alumnos asisten con hambre y frío.» Político radical: «El Estado debe proteger a los trabajadores y ampliar la educación.»"
build(
    OA, 4, F4,
    use="Aprenderé a reconocer actores, causas y perspectivas de la cuestión social, incluida la agencia de los sectores populares y el protagonismo creciente de los sectores medios. Sirve para explicar por qué se transformaron las ideas de los partidos políticos.",
    prior=["Conozco la cuestión social y los cambios del periodo.", "Sé qué es la multicausalidad.", "Sé que cada voz tiene una perspectiva."],
    explain=[
        "En la cuestión social actuaron muchos grupos. Los trabajadores se organizaron y exigieron mejores salarios y condiciones. Los industriales y empresarios buscaban mantener sus costos bajos. Médicos e intelectuales describieron los problemas de salud y de vivienda. Los sectores medios, como profesores, empleados y profesionales, crecieron y empezaron a tener protagonismo político. Y el Estado y los partidos debieron decidir cómo responder.",
        "Las causas fueron varias: el crecimiento rápido de las ciudades, la expansión de la minería, la baja de salarios reales, la falta de protección legal, la ideología de que el Estado debía intervenir poco y el ejemplo de movimientos obreros de otros países. Hablamos de multicausalidad porque ninguna razón explica por sí sola la cuestión social ni el surgimiento de las organizaciones.",
        "Los partidos políticos transformaron sus ideas. El Partido Radical, apoyado por sectores medios, defendió reformas sociales y educación. El Partido Demócrata y luego el Obrero Socialista representaron a trabajadores. Hubo sectores conservadores influenciados por la doctrina social de la Iglesia que pidieron proteger a los obreros. Estas transformaciones ideológicas mostraron que el Estado debía asumir un rol social.",
    ],
    vocab=[("protagonismo", "papel destacado de un grupo en un proceso"), ("ideología", "conjunto de ideas sobre cómo debe organizarse la sociedad"), ("reforma social", "cambio en las leyes para mejorar las condiciones de vida de las personas"), ("salario real", "capacidad de compra del salario de una persona"), ("doctrina social de la Iglesia", "conjunto de ideas de la Iglesia católica sobre justicia social y trabajo")],
    worked=[
        ("Emparejar actor e interés", "¿Qué interés expresa el obrero portuario y cuál el industrial?",
         ["El obrero pide mejores sueldos y jornadas más cortas.", "El industrial teme que subir sueldos aumente sus costos."], "Obrero: mejores sueldos y jornada corta; industrial: mantener costos bajos"),
        ("Pasar de una causa a varias", "Un compañero dice: «la cuestión social se debió solo al crecimiento de las ciudades». Da otra causa.",
         ["El crecimiento urbano es una causa.", "También importó la falta de protección legal y la intervención limitada del Estado."], "La falta de protección legal y la poca intervención del Estado"),
    ],
    mistakes=[
        ("Explicar la cuestión social con una sola causa.", "Fueron varias, económicas, sociales y políticas.", "Escribe al menos tres factores."),
        ("Presentar a los sectores populares como pasivos y a los sectores medios como ausentes.", "Ambos fueron protagonistas de cambios.", "Incluye sus acciones y su papel político."),
    ],
    T=[
        ("En Historia: ¿qué es una reforma social?", "Un cambio en las leyes para mejorar las condiciones de vida de las personas", "Es lo que pedían los trabajadores y algunos partidos."),
        ("{F} ¿Qué pide el obrero portuario?", "Mejores sueldos y jornadas más cortas", "Su voz lo dice."),
        ("En Historia: ¿qué es el protagonismo de un grupo?", "El papel destacado de un grupo en un proceso", "Los sectores medios lo ganaron."),
        ("{F} ¿Por qué se propagan las enfermedades en los conventillos según el médico?", "Por el hacinamiento", "Su voz lo dice."),
        ("Une cada actor con su interés: 1) industrial, 2) dirigente de mancomunal, 3) político radical. a) unirse para defenderse y ayudarse, b) mantener costos bajos, c) que el Estado proteja a los trabajadores. Escribe las parejas.", "1-b, 2-a, 3-c", "Cada voz expresa un interés distinto."),
        ("{F} Elige el actor que representa a los sectores medios. A) la profesora de escuela pública, B) el obrero portuario, C) el industrial.", "A", "Los profesores forman parte de los sectores medios."),
        ("Explica con un ejemplo qué significa que el salario real baje.", "Que el salario alcanza para comprar menos bienes, aunque el monto en pesos sea el mismo", "El salario real mide el poder de compra."),
        ("{F} ¿Qué situación de los alumnos describe la profesora y qué muestra sobre las condiciones de vida de las familias?", "Asisten con hambre y frío, lo que muestra malas condiciones de vida", "Su voz describe un efecto de la cuestión social."),
        ("{F} Una compañera dice que los trabajadores no hicieron nada frente a sus problemas. Responde con un dato de las voces de ejemplo.", "El dirigente de la mancomunal dice que se unieron para defenderse y ayudarse", "Hay agencia en la organización."),
        ("Explica por qué hablamos de multicausalidad al estudiar la cuestión social.", "Porque influyeron el crecimiento urbano, la minería, los salarios, la falta de protección legal y las ideas sobre el papel del Estado", "Varias causas se combinaron."),
        ("{F} ¿En qué se diferencian las perspectivas del industrial y del obrero?", "El industrial teme el aumento de costos y el obrero pide mejores sueldos y jornadas", "Sus intereses chocan."),
        ("Evalúa la frase «los partidos políticos no cambiaron sus ideas ante la cuestión social». A) es falsa porque surgieron partidos obreros y algunos partidos adoptaron reformas sociales, B) es correcta, C) es correcta porque hubo conflictos.", "A", "Hubo transformaciones ideológicas."),
        ("Redacta una tesis de una frase sobre la cuestión social que incluya a los sectores populares y a los sectores medios.", "Por ejemplo: la cuestión social llevó a los sectores populares a organizarse y a los sectores medios a exigir que el Estado interviniera", "La tesis une dos actores."),
    ],
    ctx=("{F} En una dramatización escolar, un compañero hace que el obrero y el industrial digan lo mismo. Con las voces de ejemplo, ¿cómo cambiarías sus diálogos?", "El obrero pediría mejores sueldos y jornadas y el industrial diría que subir sueldos aumenta sus costos", "Cada personaje debe hablar desde su interés."),
    sc=[("En Historia: ¿qué es una ideología?", "Un conjunto de ideas sobre cómo debe organizarse la sociedad", "Los partidos las transformaron."),
        ("Nombra dos actores de la cuestión social.", "Por ejemplo: los obreros y los sectores medios", "Ambos participaron en el periodo."),
        ("¿Qué partido apoyaban los sectores medios, según la clase?", "El Partido Radical", "Defendió reformas sociales y educación.")],
    op=("{F} Elige dos voces de ejemplo de arriba y escribe cinco líneas: qué busca cada una, una causa de la cuestión social y una diferencia de perspectiva. Cierra con una tesis de una frase.",
        "El obrero portuario busca mejores sueldos y el industrial teme que suban sus costos. Una causa fue la falta de protección legal. El obrero ve necesidad y el industrial ve costos. Tesis: la cuestión social llevó a los trabajadores a organizarse y a los partidos a cambiar sus ideas sobre el rol del Estado.",
        ["dos voces", "una causa", "diferencia de perspectiva", "tesis"], ["texto de cinco líneas"], ["reducir a pobreza individual", "no incluir tesis"], "Cuenta tu texto a alguien de tu casa y pídele que identifique tu tesis."),
    reinforce="Haz una tabla con seis actores y un interés para cada uno.",
    extend="Explica por qué las ideas de los partidos políticos cambiaron frente a la cuestión social.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = "Dossier de ejemplo. Dato 1: el crecimiento de Santiago, Valparaíso y los campamentos mineros produjo conventillos hacinados, salarios bajos y alta mortalidad infantil. Dato 2: los trabajadores crearon sociedades de socorros mutuos, mancomunales, sindicatos y partidos, y realizaron huelgas, como la de portuarios en Valparaíso (1903). Dato 3: en 1907 la protesta de trabajadores salitreros en Iquique terminó en una matanza. Dato 4: entre 1906 y 1924 se aprobaron leyes sociales sobre habitaciones, descanso dominical y accidentes del trabajo. Dato 5: los sectores medios crecieron y el Partido Radical y otros grupos defendieron reformas sociales."
build(
    OA, 5, F5,
    use="Aprenderé a argumentar con evidencia cómo cambiaron la sociedad y la política en el cambio de siglo, incluidas las demandas populares y el protagonismo de los sectores medios. Sirve para responder con equilibrio entre problemas, organización y respuestas del Estado.",
    prior=["Conozco la cuestión social, sus actores y sus fuentes.", "Sé distinguir cambio y continuidad.", "Sé escribir tesis, evidencia y límite."],
    explain=[
        "Un argumento sobre la cuestión social responde a una pregunta como «¿Cómo se transformó la sociedad chilena en el cambio de siglo y qué papel tuvieron los sectores populares y los sectores medios?». Una tesis posible es que la cuestión social, originada por el crecimiento urbano y minero, llevó a los trabajadores a organizarse y a luchar, y presionó al Estado y a los partidos a cambiar de ideas y aprobar leyes sociales.",
        "Las evidencias se explican. El dato 1 muestra las condiciones que originaron la cuestión social. El dato 2 muestra la agencia de los trabajadores. El dato 3 muestra la represión que enfrentaron. El dato 4 muestra una respuesta legislativa. El dato 5 muestra el protagonismo de los sectores medios y el cambio de ideas de los partidos. Cada dato se explica con «esto muestra que…».",
        "El límite: con el dossier no sabemos cuántos trabajadores se organizaron ni qué efecto concreto tuvo cada ley. Tampoco podemos decir que el Estado respondiera siempre con represión ni que las leyes resolvieran los problemas. Evita frases como «los obreros eran pasivos» o «el Estado nunca hizo nada».",
    ],
    vocab=[("tesis", "afirmación principal que se defiende"), ("evidencia", "dato que apoya la tesis"), ("agencia", "capacidad de un grupo de actuar y tomar decisiones"), ("protagonismo", "papel destacado de un grupo en un proceso"), ("límite", "aquello que la evidencia no permite afirmar")],
    worked=[
        ("Elegir evidencias", "Para sostener que los trabajadores tuvieron agencia, ¿qué datos del dossier sirven?",
         ["El dato 2 muestra organizaciones y huelgas.", "El dato 4 muestra que sus presiones coincidieron con nuevas leyes."], "Los datos 2 y 4"),
        ("Detectar exageración", "¿Por qué excede el dossier la frase «el Estado solo respondió con represión»?",
         ["El dato 3 muestra represión en 1907.", "El dato 4 muestra leyes sociales entre 1906 y 1924."], "Porque el dato 4 muestra también respuestas legales"),
    ],
    mistakes=[
        ("Escribir una tesis que no mencione a los sectores medios.", "Omite a un actor clave del periodo.", "Incluye el dato 5."),
        ("Presentar a los trabajadores solo como víctimas.", "Se organizaron, hicieron huelgas y formaron partidos.", "Incluye el dato 2."),
    ],
    T=[
        ("En Historia: ¿qué es la agencia?", "La capacidad de un grupo de actuar y tomar decisiones", "Los trabajadores la ejercieron."),
        ("{F} ¿Qué dato muestra una respuesta legislativa? A) dato 1, B) dato 3, C) dato 4.", "C", "El dato 4 habla de leyes sociales."),
        ("{F} ¿Qué dato muestra el origen de la cuestión social?", "El dato 1", "Habla de hacinamiento, salarios bajos y mortalidad infantil."),
        ("{F} ¿Qué dato menciona la represión?", "El dato 3", "Habla de la matanza de 1907."),
        ("Elige la tesis mejor formulada. A) La cuestión social fue solo un problema de pobreza individual, B) La cuestión social llevó a los trabajadores a organizarse y a presionar por leyes y reformas, con respuestas del Estado, C) Los problemas se resolvieron en 1906.", "B", "Es defendible con el dossier."),
        ("Una compañera usa solo el dato 3 para decir que «el Estado solo reprimió». ¿Qué dato lo contradice?", "El dato 4, que muestra leyes sociales entre 1906 y 1924", "Hubo también respuestas legales."),
        ("{F} ¿Qué dato del dossier muestra el protagonismo de los sectores medios?", "El dato 5", "Menciona su crecimiento y las reformas sociales que defendieron."),
        ("Un grupo escribe una tesis con cinco datos y ningún límite. ¿Qué límite podría agregar según el dossier?", "Que el dossier no mide cuántos trabajadores se organizaron ni el efecto de cada ley", "El límite señala lo que no se puede afirmar."),
        ("{F} Con los datos 4 y 5, redacta una conclusión proporcional.", "Se aprobaron leyes sociales y crecieron los sectores medios, cuyos partidos defendieron reformas", "Une leyes y actores."),
        ("Explica por qué una buena tesis sobre la cuestión social debe incluir a los trabajadores como actores.", "Porque se organizaron, hicieron huelgas y formaron partidos para exigir cambios", "El dato 2 muestra su agencia."),
        ("Un compañero escribe: «La cuestión social se resolvió con las leyes de 1906». Señala la exageración.", "«Se resolvió» excede la evidencia, porque los problemas continuaban y el dato 3 muestra conflictos posteriores", "Las leyes fueron un primer paso."),
        ("Evalúa este argumento: «Los trabajadores se organizaron (dato 2), enfrentaron represión (dato 3) y lograron leyes (dato 4)». A) es sólido porque usa varios tipos de evidencia, B) es débil porque solo describe problemas y no menciona ninguna acción de los trabajadores, C) es falso porque el dossier muestra que los trabajadores nunca se organizaron.", "A", "Usa evidencias de agencia, represión y respuesta."),
        ("Escribe una pregunta que exigiría otra fuente para completar el argumento.", "Por ejemplo: ¿qué efecto tuvo cada ley en la vida de una familia obrera?", "La pregunta indica un vacío del dossier."),
    ],
    ctx=("{F} En un foro estudiantil alguien dice que «las leyes sociales fueron un regalo del gobierno y no una conquista de los trabajadores». Con el dossier, escribe tu respuesta en dos frases.", "El dato 2 muestra que los trabajadores se organizaron y presionaron, y el dato 4 muestra que hubo leyes en esos años, así que no se puede decir que fueran solo un regalo", "La respuesta debe usar los datos 2 y 4."),
    sc=[("En Historia: ¿qué es el protagonismo?", "El papel destacado de un grupo en un proceso", "Los sectores medios lo ganaron."),
        ("Nombra un dato del dossier sobre organización de los trabajadores.", "Por ejemplo: crearon mancomunales, sindicatos y partidos", "Es el dato 2."),
        ("¿Qué muestra el dato 5?", "Que los sectores medios crecieron y que partidos como el Radical defendieron reformas sociales", "Es parte de la respuesta política.")],
    op=("{F} Con el dossier de ejemplo de arriba, escribe un párrafo de ocho líneas que responda: «¿Cómo se transformó la sociedad chilena en el cambio de siglo y qué papel tuvieron los trabajadores y los sectores medios?». Incluye una tesis, tres evidencias explicadas y un límite.",
        "La cuestión social surgió del crecimiento urbano y minero, con conventillos hacinados y salarios bajos. Los trabajadores se organizaron en mancomunales, sindicatos y partidos, y hubo huelgas y represión, como en 1907. Entre 1906 y 1924 se aprobaron leyes sociales y los sectores medios y partidos como el Radical defendieron reformas. Límite: el dossier no mide el efecto de cada ley.",
        ["tesis", "tres evidencias explicadas", "límite"], ["párrafo de ocho líneas"], ["presentar a los trabajadores como pasivos", "no explicar los datos"], "Pide a alguien de tu casa que marque tu tesis y tus tres evidencias."),
    reinforce="Escribe tu tesis en una frase y anota las tres evidencias que la apoyan.",
    extend="Escribe una segunda tesis centrada en los sectores medios y un dato nuevo que necesitarías.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 6
F6 = "Resumen de ejemplo para evaluar proyecciones. En 1920 Arturo Alessandri ganó la elección presidencial con apoyo de sectores medios y populares y prometió reformas sociales. En 1924 se aprobaron leyes sociales sobre contrato de trabajo, accidentes y organización sindical. En 1922 el Partido Obrero Socialista, fundado en 1912, pasó a llamarse Partido Comunista de Chile. En 1925 una nueva Constitución restableció el régimen presidencial. Los conventillos siguieron existiendo y los conflictos laborales continuaron en las décadas siguientes. Las mujeres obtuvieron el derecho a votar en elecciones municipales en 1934."
build(
    OA, 6, F6,
    use="Aprenderé a evaluar las proyecciones de la cuestión social: qué leyes y organizaciones dejó, qué problemas continuaron y qué preguntas quedan abiertas. Sirve para entender el origen de la política social y de los partidos de masas del siglo XX.",
    prior=["Conozco la cuestión social, sus actores y sus argumentos.", "Sé evaluar con evidencia y límite.", "Sé qué son las leyes sociales."],
    explain=[
        "Evaluar proyecciones significa preguntar qué consecuencias de largo plazo dejó un proceso. La cuestión social dejó una nueva idea: que el Estado debía proteger a los trabajadores. Las leyes sociales de 1924 sobre contrato de trabajo, accidentes y organización sindical marcaron un inicio de legislación laboral. También dejó organizaciones y partidos de trabajadores, como el Partido Comunista (1922), nacido del Partido Obrero Socialista.",
        "En el plano político, la elección de Alessandri en 1920 mostró que sectores medios y populares podían decidir elecciones. La Constitución de 1925 restableció el régimen presidencial y dio un nuevo marco al Estado. Pero los problemas no desaparecieron: los conventillos siguieron existiendo y los conflictos laborales continuaron en las décadas siguientes. Las mujeres obtuvieron el derecho a votar en elecciones municipales en 1934, es decir, su participación política llegó mucho después.",
        "Al evaluar, hay que reconocer límites de lo que sabemos: no todas las leyes se aplicaron de inmediato ni todas las regiones tuvieron los mismos resultados. Una buena evaluación evita decir que la cuestión social «se solucionó» o que «no cambió nada», y deja preguntas abiertas para investigar, por ejemplo, el papel de las mujeres trabajadoras.",
    ],
    vocab=[("legislación laboral", "conjunto de leyes que regulan el trabajo y protegen a los trabajadores"), ("contrato de trabajo", "acuerdo escrito o verbal entre trabajador y empleador sobre condiciones de trabajo"), ("proyección", "consecuencia de largo plazo de un proceso"), ("partido de masas", "partido que busca representar a grandes sectores de la población"), ("organización sindical", "conjunto de sindicatos y federaciones de trabajadores")],
    worked=[
        ("Ordenar por fecha", "Con el resumen, ¿cuántos años pasaron entre la elección de Alessandri y el voto municipal femenino?",
         ["Busco las fechas: 1920 y 1934.", "Resto: 1934 - 1920."], "14 años"),
        ("Distinguir ley y realidad", "Las leyes de 1924 reconocían contrato de trabajo y sindicatos. ¿Garantizan por sí solas que mejoren las condiciones de todos?",
         ["Una ley establece reglas.", "Su efecto depende de que se aplique y se fiscalice."], "No: depende de que se aplique"),
    ],
    mistakes=[
        ("Decir que las leyes de 1924 resolvieron todos los problemas.", "Los conventillos y los conflictos continuaron.", "Distingue ley y realidad."),
        ("Decir que la cuestión social no cambió nada.", "Dejó leyes, organizaciones y nuevas ideas sobre el Estado.", "Reconoce los avances junto con los límites."),
    ],
    T=[
        ("En Historia: ¿qué es la legislación laboral?", "El conjunto de leyes que regulan el trabajo y protegen a los trabajadores", "Las leyes de 1924 la iniciaron."),
        ("{F} ¿Qué partido nació del Partido Obrero Socialista en 1922?", "El Partido Comunista de Chile", "El resumen lo indica."),
        ("En Historia: ¿qué es un contrato de trabajo?", "Un acuerdo entre trabajador y empleador sobre condiciones de trabajo", "Fue regulado en 1924."),
        ("{F} ¿Qué restableció la Constitución de 1925? A) el régimen presidencial, B) el régimen parlamentario, C) la monarquía.", "A", "El resumen lo señala."),
        ("{F} ¿Qué derecho obtuvieron las mujeres en 1934?", "El derecho a voto municipal", "El resumen lo indica."),
        ("Une cada proyección con su ámbito: 1) leyes de 1924, 2) Partido Comunista, 3) voto municipal femenino. a) laboral, b) de organización política, c) de derechos políticos de las mujeres. Escribe las parejas.", "1-a, 2-b, 3-c", "Cada proyección toca un ámbito."),
        ("{F} Ordena de más antiguo a más reciente: Constitución de 1925, elección de Alessandri, voto municipal femenino y cambio de nombre a Partido Comunista.", "Elección de Alessandri, Partido Comunista, Constitución de 1925, voto municipal femenino", "Se ordenan por sus años: 1920, 1922, 1925 y 1934."),
        ("{F} ¿Qué leyes de 1924 se mencionan y sobre qué temas?", "Leyes sociales sobre contrato de trabajo, accidentes y organización sindical", "El resumen las describe."),
        ("{F} Explica por qué la elección de Alessandri en 1920 muestra el peso de los sectores medios y populares.", "Porque ganó con apoyo de ambos y prometió reformas sociales", "El resumen lo señala."),
        ("{F} Una compañera dice: «Con las leyes de 1924, la cuestión social desapareció». Corrige con un dato del resumen.", "Los conventillos siguieron existiendo y los conflictos laborales continuaron", "Hay continuidades claras."),
        ("{F} ¿Qué límite tiene este resumen para evaluar el efecto de las leyes de 1924?", "No muestra cuánto se aplicaron ni cómo cambió la vida de las familias", "Es un vacío de la fuente."),
        ("Evalúa la frase «la cuestión social no dejó ninguna proyección». A) es falsa porque dejó leyes, organizaciones y nuevas ideas sobre el Estado, B) es correcta, C) es correcta porque los problemas siguieron.", "A", "Hubo proyecciones claras."),
        ("Propón una pregunta para seguir investigando el papel de las mujeres trabajadoras.", "Por ejemplo: ¿qué demandas tenían las trabajadoras de talleres y fábricas y cómo se organizaron?", "La pregunta amplía la mirada."),
    ],
    ctx=("{F} Un compañero escribe en un trabajo «los derechos laborales actuales no tienen relación con la historia de 1900». Con el resumen, escribe una frase que lo corrija.", "Las leyes de 1924, los sindicatos y los partidos de trabajadores iniciaron la legislación laboral que se desarrolló después", "La corrección muestra una proyección."),
    sc=[("En Historia: ¿qué es un partido de masas?", "Un partido que busca representar a grandes sectores de la población", "Fue una proyección política."),
        ("Nombra una proyección de la cuestión social.", "Por ejemplo: la legislación laboral de 1924", "Está en el resumen."),
        ("¿Qué problema continuó después de 1924?", "Los conventillos y los conflictos laborales", "Lo dice el resumen.")],
    op=("{F} Con el resumen de ejemplo de arriba, escribe un párrafo de ocho líneas que evalúe las proyecciones de la cuestión social: nombra una ley, una organización política, un problema que continuó, una fecha de 1934 o 1925 y un límite de lo que sabemos.",
        "Las leyes de 1924 iniciaron la legislación laboral y en 1922 el Partido Obrero Socialista pasó a ser el Partido Comunista. En 1925 se restableció el régimen presidencial. Los conventillos y los conflictos laborales continuaron y las mujeres solo obtuvieron el derecho a votar en elecciones municipales en 1934. Límite: no sabemos cuánto se aplicaron las leyes.",
        ["una ley", "una organización política", "un problema que continuó", "una fecha", "un límite"], ["párrafo de ocho líneas"], ["decir que se solucionó todo", "omitir el límite"], "Pide a alguien de tu casa que revise que incluyas un problema que continuó."),
    reinforce="Haz una tabla con dos columnas (avances y problemas pendientes) con dos datos en cada una.",
    extend="Escribe una pregunta sobre cómo se relacionan los derechos laborales de hoy con las demandas de 1900.",
    materials=MAT,
)
