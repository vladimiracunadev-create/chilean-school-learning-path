"""Material del estudiante de 6.º básico, Historia, Geografía y Ciencias Sociales: OA 05 (conformación del territorio de Chile en el siglo XIX)."""
from __future__ import annotations

from hi5_lib import build

OA5 = "HI06 OA 05"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 21 (cronología del territorio, hecha para este cuaderno). "
     "1826: la isla de Chiloé pasa a formar parte de la república de Chile. "
     "1843: Chile toma posesión del estrecho de Magallanes y funda el Fuerte Bulnes; en 1848 se funda Punta Arenas. "
     "1845: una ley de colonización invita a extranjeros a poblar el sur. 1852: llegan colonos alemanes a la zona del lago Llanquihue, y en 1853 se funda Puerto Montt. "
     "1861 a 1883: el Estado chileno ocupa la Araucanía. "
     "1879 a 1884: Guerra del Pacífico entre Chile, Perú y Bolivia. "
     "1881: tratado de límites entre Chile y Argentina, que reconoce a Chile el estrecho de Magallanes. "
     "1883: tratado de Ancón con Perú; Chile queda con la provincia de Tarapacá. "
     "1888: Chile incorpora la Isla de Pascua (Rapa Nui).")
build(
    OA5, 1, F,
    use="Aprenderé a ubicar en el tiempo y en el mapa cómo se formó el territorio de Chile en el siglo XIX. Sirve para entender cuándo se incorporó cada zona.",
    prior=["Sé que Chile se organizó como república en el siglo XIX.", "Sé leer mapas y líneas de tiempo.", "Sé ubicar el norte, el sur y las islas de Chile."],
    explain=[
        "Un territorio es un espacio gobernado por un Estado. A comienzos del siglo XIX, el territorio de Chile era mucho menos extenso que el actual en la práctica: el Estado no controlaba bien el extremo sur, la Araucanía ni el extremo norte. Durante el siglo, Chile fue ampliando y conformando su territorio por varios caminos.",
        "En el sur, se incorporó Chiloé en 1826, se ocuparon el estrecho de Magallanes en 1843 y la Araucanía entre 1861 y 1883, y se invitó a colonos europeos a vivir en Valdivia, Osorno y Llanquihue. En el norte, la Guerra del Pacífico (1879-1884) terminó con Chile en control de Tarapacá y Antofagasta. En 1888 se incorporó la Isla de Pascua, a miles de kilómetros de la costa.",
        "Para estudiar este proceso conviene ubicar cada hecho en una línea de tiempo y en un mapa, con tres preguntas: ¿cuándo?, ¿dónde? y ¿cómo se incorporó el lugar: por colonización, por ocupación, por guerra o por acuerdo? Así evitamos pensar que todo ocurrió igual ni al mismo tiempo.",
    ],
    vocab=[("territorio", "espacio gobernado por un Estado"), ("colonización", "llegada de personas para poblar y trabajar un lugar"), ("ocupación", "hecho de tomar el control de un lugar"), ("tratado", "acuerdo escrito entre países"), ("incorporar", "agregar un lugar al territorio de un país")],
    worked=[
        ("Calcular una duración", "{F} ¿Cuántos años duró la Guerra del Pacífico según los años de la ficha?", ["La ficha dice que fue de 1879 a 1884.", "Resto: 1884 − 1879 = 5."], "5 años"),
        ("Ubicar un lugar", "{F} ¿Qué zona de Chile se ocupó entre 1861 y 1883?", ["Busco el período en la ficha.", "Corresponde a la Araucanía."], "La Araucanía"),
    ],
    mistakes=[("Creer que Chile siempre tuvo el mismo territorio.", "Se mira solo el mapa actual.", "El territorio cambió durante el siglo XIX."),
              ("Pensar que todo el territorio se incorporó por guerra.", "Se piensa en un solo camino.", "Hubo colonización, ocupación, guerra y acuerdos.")],
    T=[
        ("{F} ¿En qué año se fundó el Fuerte Bulnes?", "1843", "La ficha lo indica."),
        ("{F} ¿Qué isla se incorporó a Chile en 1888?", "la Isla de Pascua (Rapa Nui)", "La ficha lo dice."),
        ("{F} ¿Qué ciudad se fundó en 1853 en la zona de Llanquihue?", "Puerto Montt", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre el inicio de la ocupación de la Araucanía y el fin de la Guerra del Pacífico?", "1884-1861", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué tratado de 1883 dejó a Chile con Tarapacá?", "el tratado de Ancón", "La ficha lo dice."),
        ("{F} Ordena de más antiguo a más reciente: Isla de Pascua, Chiloé, tratado de Ancón, Fuerte Bulnes.", "Chiloé, Fuerte Bulnes, tratado de Ancón, Isla de Pascua", "Los años son 1826, 1843, 1883 y 1888."),
        ("=", "{F} ¿Cuántos años duró la ocupación de la Araucanía?", "1883-1861", "Se resta el año de inicio al de término.", " años"),
        ("{F} Clasifica cada hecho como «sur» o «norte»: a) Fuerte Bulnes; b) Tarapacá; c) Llanquihue; d) Araucanía.", "sur: a, c y d; norte: b", "Tarapacá está en el norte."),
        ("Según la explicación de la clase, ¿en qué tres zonas del sur se invitó a vivir a colonos europeos?", "Valdivia, Osorno y Llanquihue", "La clase los nombra como zonas de colonización."),
        ("{F} Un compañero dice: «La Guerra del Pacífico ocurrió antes que la fundación de Puerto Montt». Corrígelo.", "No: Puerto Montt se fundó en 1853 y la guerra fue de 1879 a 1884", "1853 es anterior a 1879."),
        ("{F} Una alumna dice: «La Isla de Pascua se incorporó después de la Guerra del Pacífico». ¿Es correcto?", "sí, 1888 es posterior a 1884", "Las fechas lo confirman."),
        ("{F} Una línea de tiempo usa 1 cm = 10 años y parte en 1820. ¿A cuántos cm queda el año 1860?", "4 cm", "(1860 − 1820) ÷ 10 = 4."),
        ("{F} ¿Cuántos tratados menciona la ficha?", "dos (el tratado con Argentina de 1881 y el tratado de Ancón de 1883)", "Cada tratado figura con su año."),
    ],
    ctx=("Un mapa escolar muestra el territorio de Chile en 1840 y en 1890. Usa la ficha para decir dos cambios entre ambas fechas.", "Chile ocupó Magallanes y la Araucanía, y ganó Tarapacá y la Isla de Pascua", "La ficha muestra hechos entre 1843 y 1888."),
    sc=[("¿Qué es un territorio?", "un espacio gobernado por un Estado", "Es la definición de la clase."),
        ("{F} ¿En qué año se incorporó Chiloé?", "1826", "La ficha lo dice."),
        ("¿Qué tres preguntas ayudan a ubicar un hecho territorial?", "cuándo, dónde y cómo se incorporó", "Son las preguntas de la clase.")],
    op=("Dibuja un mapa muy simple de Chile en vertical, con el norte arriba. Marca con un punto y una flecha los lugares de la ficha: Tarapacá, Araucanía, Llanquihue, Magallanes, Chiloé, Isla de Pascua (al oeste, en el océano). Junto a cada punto, escribe el año. {F}",
        "Tarapacá (1883), Araucanía (1861-1883), Llanquihue (1852), Magallanes (1843), Chiloé (1826), Pascua (1888), en orden de norte a sur.",
        ["seis lugares marcados en orden de norte a sur", "años correctos", "Pascua fuera del continente"], ["mapa simple con puntos y años"], ["poner Tarapacá en el sur", "poner Pascua pegada al continente"],
        "Pide que explique en voz alta por qué dibujó Pascua tan lejos."),
    reinforce="Di en voz alta los seis lugares de la ficha de norte a sur y el año de cada uno.",
    extend="Escribe una pregunta sobre cómo vivían las personas que ya habitaban esos lugares cuando llegó el Estado de Chile.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 22 (fuentes inventadas para este cuaderno, a partir de hechos conocidos). "
     "Fuente A, carta de un colono alemán a su familia, 1853 (texto inventado): «Hemos llegado al sur de Chile; la tierra es verde, llueve mucho y hay que talar el bosque para sembrar». "
     "Fuente B, informe de un oficial chileno, 1862 (texto inventado): «Hemos fundado un fuerte para asegurar la zona; los caminos se están despejando». "
     "Fuente C, relato oral imaginado para este cuaderno, que resume lo que cuentan muchas familias mapuche (no es el testimonio de una persona real): «Después de la ocupación, nuestras familias quedaron en terrenos mucho más pequeños que los que habíamos ocupado». "
     "Fuente D, extracto adaptado del tratado de Ancón, 1883: Perú entrega a Chile la provincia de Tarapacá.")
build(
    OA5, 2, F,
    use="Aprenderé a interrogar fuentes sobre la formación del territorio chileno. Sirve para reconocer distintas voces, incluidas las de los pueblos que ya vivían allí.",
    prior=["Sé la diferencia entre fuente primaria y secundaria.", "Sé que cada fuente tiene un punto de vista.", "Sé ubicar hechos territoriales en el tiempo."],
    explain=[
        "Para estudiar cómo se formó el territorio de Chile usamos distintas fuentes: cartas, informes, tratados y relatos. Cada una nos cuenta el mismo proceso desde un lugar diferente. Preguntamos quién habla, cuándo, para qué y qué voces faltan.",
        "La carta del colono (fuente A) muestra la experiencia de una familia extranjera en el sur. El informe del oficial (fuente B) muestra la mirada del Estado, que quería asegurar la zona. El relato mapuche (fuente C) cuenta que, después de la ocupación, las familias quedaron en terrenos más pequeños. Y el tratado (fuente D) es un documento oficial que fija un cambio de límites.",
        "Ninguna fuente sola cuenta toda la historia. Una voz importante, la de los pueblos que habitaban los territorios, a menudo no quedó escrita en documentos oficiales. Por eso es valioso incluir relatos orales y reconocer que algunas voces faltan. Una conclusión debe ser prudente y apoyarse en varias fuentes.",
    ],
    vocab=[("colono", "persona que llega a poblar y trabajar tierras"), ("informe", "documento que cuenta lo que se hizo o vio"), ("relato oral", "historia que se transmite hablando de generación en generación"), ("pueblo originario", "pueblo que habitaba un territorio antes de la llegada del Estado actual"), ("voz", "punto de vista de un grupo que se expresa")],
    worked=[
        ("Reconocer el punto de vista", "{F} ¿Desde qué mirada habla la fuente B?", ["La escribe un oficial chileno.", "Quiere asegurar la zona para el Estado."], "Desde la mirada del Estado chileno"),
        ("Identificar una voz presente", "{F} ¿Qué cuenta la fuente C sobre las familias mapuche?", ["Habla de lo ocurrido después de la ocupación.", "Dice que quedaron en terrenos más pequeños."], "Que quedaron en terrenos mucho más pequeños"),
    ],
    mistakes=[("Creer que el informe del oficial cuenta toda la historia de la Araucanía.", "Se olvida que habla desde un lado.", "Hay que comparar con otras voces, como el relato mapuche."),
              ("Dar por falsa una fuente oral por no estar escrita.", "Se piensa que solo lo escrito sirve.", "Los relatos orales son fuentes valiosas, que se analizan igual que las demás.")],
    T=[
        ("{F} ¿Qué hay que hacer para sembrar según el colono de la fuente A?", "talar el bosque", "La carta lo dice."),
        ("{F} ¿Qué entregó Perú a Chile según la fuente D?", "la provincia de Tarapacá", "El resumen del tratado lo dice."),
        ("{F} ¿En qué año se escribió el informe de la fuente B?", "1862", "La ficha da ese año."),
        ("{F} ¿Cuál de las fuentes es un relato oral?", "la fuente C", "Se transmitió en una familia."),
        ("=", "{F} ¿Cuántos años pasaron entre la carta del colono y el tratado de Ancón?", "1883-1853", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué fuente muestra la mirada del Estado?", "la fuente B", "Es un informe de un oficial chileno."),
        ("{F} ¿Qué pérdida cuenta la fuente C?", "que las familias quedaron en terrenos mucho más pequeños", "El relato lo dice con esas palabras."),
        ("{F} Una alumna dice: «La fuente A prueba que todos los colonos tuvieron un viaje fácil». ¿Qué error comete?", "generaliza desde una sola carta", "Una carta no habla por todos."),
        ("{F} Compara A y C: ¿quién describe llegar a un lugar nuevo y quién describe perder terreno?", "A describe llegar y C describe perder terreno", "Cada una habla desde su situación."),
        ("{F} ¿Qué voz falta en las fuentes A, B y D?", "la de los pueblos originarios", "Solo la fuente C la entrega."),
        ("{F} ¿Por qué la fuente D es oficial?", "porque es el resumen de un tratado entre países", "Los tratados son documentos oficiales."),
        ("{F} Un compañero dice que la fuente C no sirve por ser oral. Respóndele.", "los relatos orales son fuentes valiosas y se analizan como las demás", "La oralidad no le quita valor."),
        ("{F} Elige la mejor pregunta para la fuente B: A) ¿Qué buscaba el Estado al fundar el fuerte? B) ¿Qué color tenía el papel?", "A", "Pregunta por el propósito."),
    ],
    ctx=("Para una exposición sobre la Araucanía, un grupo solo usa la fuente B. ¿Qué le dirías?", "que agregue la fuente C para incluir la voz de las familias mapuche", "B muestra solo la mirada del Estado."),
    sc=[("¿Qué se pregunta primero a una fuente?", "quién habla y para qué", "Autor y propósito."),
        ("{F} ¿Qué tipo de fuente es D?", "un documento oficial", "Resume un tratado."),
        ("¿Por qué es importante buscar voces que faltan?", "porque así la historia incluye a todos los grupos", "Una fuente sola es parcial.")],
    op=("Haz una ficha de análisis con las fuentes A, B, C y D. Anota quién habla, cuándo, qué dice, qué mirada tiene y qué voz falta. Termina con dos oraciones sobre qué sabes y qué no sabes aún. {F}",
        "C: familia mapuche, relato oral, dice que quedaron con terrenos más pequeños; falta la voz del Estado chileno en ese relato.",
        ["cuatro fuentes analizadas", "una voz que falta por fuente", "dos oraciones finales"], ["ficha de análisis", "dos oraciones"], ["omitir la fuente C", "no anotar voces que faltan"],
        "Pide que explique por qué incluyó la voz mapuche."),
    reinforce="Con tus palabras, resume lo que cuenta cada fuente de la ficha.",
    extend="Escribe una pregunta que te gustaría hacer a una persona mapuche actual sobre lo que se cuenta en su familia, marcando que es solo una pregunta.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 23 (causas y consecuencias, hecha para este cuaderno). "
     "Guerra del Pacífico: causas conocidas, el conflicto por la explotación del salitre en la costa del desierto de Atacama y por el cobro de un impuesto a una empresa chilena por parte de Bolivia; en 1879 Chile ocupó Antofagasta y se inició la guerra con Bolivia y Perú. "
     "Consecuencias: Chile incorporó Tarapacá y Antofagasta; Bolivia perdió su costa; la economía chilena creció con el salitre. "
     "Ocupación de la Araucanía: causas, el interés del Estado por controlar el territorio y por usar sus tierras para la agricultura; consecuencias, las familias mapuche quedaron en terrenos reducidos y llegaron colonos chilenos y extranjeros. "
     "Colonización del sur: causa, poblar zonas que el Estado veía como poco ocupadas, aunque allí vivían familias huilliche (pueblo mapuche del sur); consecuencia, el crecimiento de ciudades como Valdivia, Osorno y Puerto Montt.")
build(
    OA5, 3, F,
    use="Aprenderé a explicar causas y consecuencias de la Guerra del Pacífico, la ocupación de la Araucanía y la colonización del sur. Sirve para entender por qué cambió el territorio y a quiénes afectó.",
    prior=["Sé ubicar estos hechos en el tiempo.", "Sé qué es una causa y una consecuencia.", "Sé que un mismo hecho afecta distinto a cada grupo."],
    explain=[
        "Los cambios territoriales del siglo XIX tuvieron causas y consecuencias. Una causa es lo que ayuda a que algo ocurra; una consecuencia es lo que ocurre después. Para cada hecho conviene preguntar qué intereses había, quiénes participaron y a quiénes afectó.",
        "En el norte, la Guerra del Pacífico se relacionó con el salitre y con un conflicto por un impuesto a una empresa chilena. Como consecuencia, Chile incorporó Tarapacá y Antofagasta, y Bolivia perdió su costa. En la Araucanía, el Estado quería controlar el territorio y usar sus tierras; como consecuencia, las familias mapuche quedaron en terrenos mucho más pequeños.",
        "En el sur, la colonización buscaba poblar zonas poco ocupadas, y favoreció el crecimiento de ciudades como Valdivia, Osorno y Puerto Montt. Un mismo proceso puede ser un logro para el Estado y una pérdida para un pueblo. Por eso al explicar hay que decir quiénes ganaron y quiénes perdieron.",
    ],
    vocab=[("salitre", "mineral del desierto que se usaba como fertilizante"), ("impuesto", "dinero que se paga al Estado"), ("reducción", "terreno pequeño en que quedaron asignadas las familias mapuche"), ("consecuencia", "resultado de un hecho"), ("interés", "lo que un grupo quiere lograr")],
    worked=[
        ("Clasificar causa y consecuencia", "{F} ¿Que Bolivia perdiera su costa es causa o consecuencia?", ["Ocurre después de la guerra.", "La ficha la lista entre las consecuencias."], "Es una consecuencia"),
        ("Ver a quién afectó", "{F} ¿A quién perjudicó la ocupación de la Araucanía según la ficha?", ["Busco la consecuencia para ese territorio.", "Las familias mapuche quedaron en terrenos reducidos."], "A las familias mapuche"),
    ],
    mistakes=[("Explicar la Guerra del Pacífico con una sola causa.", "Se simplifica un conflicto complejo.", "Intervinieron el salitre, un impuesto y la ocupación de Antofagasta."),
              ("Pensar que la ocupación de la Araucanía benefició a todos.", "Se miran solo los beneficios del Estado.", "Las familias mapuche quedaron en terrenos reducidos.")],
    T=[
        ("{F} ¿Qué mineral estaba relacionado con la Guerra del Pacífico?", "el salitre", "La ficha lo indica."),
        ("{F} ¿En qué año ocupó Chile Antofagasta?", "1879", "La ficha lo dice."),
        ("{F} ¿Qué perdió Bolivia como consecuencia de la guerra?", "su costa", "La ficha lo dice."),
        ("{F} Clasifica como causa (C) o consecuencia (K): a) impuesto a una empresa chilena; b) Chile incorpora Tarapacá; c) interés del Estado por controlar la Araucanía; d) familias mapuche en terrenos reducidos.", "a: C; b: K; c: C; d: K", "Las causas son anteriores y las consecuencias posteriores."),
        ("{F} ¿Qué causa tuvo la colonización del sur?", "poblar zonas que el Estado veía como poco ocupadas", "La ficha lo dice."),
        ("{F} ¿Qué ciudades crecieron por la colonización?", "Valdivia, Osorno y Puerto Montt", "La ficha las nombra."),
        ("=", "{F} ¿Cuántos años pasaron entre la ocupación de Antofagasta y el tratado de Ancón (1883)?", "1883-1879", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué dos intereses tenía el Estado en la Araucanía?", "controlar el territorio y usar sus tierras para la agricultura", "La ficha los menciona."),
        ("{F} Un compañero dice: «Toda la economía chilena perdió con la guerra». Corrígelo con la ficha.", "no: la economía chilena creció con el salitre", "La ficha lo indica."),
        ("{F} Una alumna dice: «La colonización del sur favoreció a todos». ¿Qué pregunta le ayudaría a revisar eso?", "quiénes ganaron y quiénes perdieron", "Ayuda a ver los distintos efectos."),
        ("{F} ¿Qué grupo menciona la ficha como afectado por la ocupación de la Araucanía?", "las familias mapuche", "La ficha lo dice."),
        ("{F} Elige la mejor razón para decir que la guerra cambió el territorio: A) Chile incorporó Tarapacá y Antofagasta; B) Chile creó un nuevo mapa de colores.", "A", "A es una consecuencia territorial."),
        ("{F} ¿Qué pregunta ayuda a no ver los hechos como un logro para todos?", "quiénes ganaron y quiénes perdieron", "Señala que los efectos fueron distintos."),
    ],
    ctx=("Una compañera dice: «La ocupación de la Araucanía fue solo buena para el país». Usa la ficha para responder.", "para el Estado y los colonos hubo beneficios, pero las familias mapuche quedaron en terrenos reducidos", "Hubo ganadores y perdedores."),
    sc=[("En Historia: ¿Qué es una causa?", "lo que ayuda a que algo ocurra", "Es la definición de la clase."),
        ("{F} ¿Qué consecuencia tuvo la guerra para el territorio de Chile?", "incorporó Tarapacá y Antofagasta", "La ficha lo dice."),
        ("¿Por qué hay que preguntar quiénes ganaron y quiénes perdieron?", "porque un hecho afecta distinto a cada grupo", "No todos vivieron lo mismo.")],
    op=("Dibuja una tabla con tres filas (Guerra del Pacífico, Araucanía, colonización del sur) y tres columnas: «causa», «consecuencia» y «quién ganó o perdió». Completa con datos de la ficha. Escribe al final una oración sobre qué grupo perdió más y por qué. {F}",
        "Guerra del Pacífico: causa, salitre; consecuencia, Tarapacá y Antofagasta; ganó Chile, perdió Bolivia. Araucanía: causa, controlar el territorio; consecuencia, terrenos reducidos; perdieron las familias mapuche.",
        ["tres filas completas", "causas y consecuencias bien separadas", "ganadores y perdedores señalados"], ["tabla de tres filas", "una oración final"], ["poner una consecuencia como causa", "no mencionar a las familias mapuche"],
        "Pide que explique por qué no pone a todos como ganadores."),
    reinforce="Di en voz alta una causa y una consecuencia de cada proceso de la ficha.",
    extend="Escribe una pregunta sobre cómo vivían las familias de Antofagasta antes y después de 1879.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 24 (comparación de territorios, hecha para este cuaderno). "
     "Norte (Tarapacá y Antofagasta): incorporados tras la Guerra del Pacífico (1879-1884); había población peruana y boliviana y trabajadores chilenos del salitre; la riqueza principal era el salitre. "
     "Araucanía: ocupada entre 1861 y 1883; era territorio mapuche; los mapuche quedaron en terrenos reducidos y llegaron colonos. "
     "Sur (Valdivia, Osorno, Llanquihue): zonas que el Estado veía como poco pobladas, donde vivían familias huilliche (pueblo mapuche del sur) y a las que llegaron colonos alemanes desde mediados del siglo XIX con apoyo del Estado. "
     "Magallanes: Chile funda el Fuerte Bulnes (1843) y Punta Arenas (1848) para asegurar el estrecho, en tierras donde también vivían pueblos originarios. "
     "Isla de Pascua: incorporada en 1888 a través de un acuerdo con jefes rapa nui, cuyo sentido ha sido discutido hasta hoy.")
build(
    OA5, 4, F,
    use="Aprenderé a comparar cómo se incorporaron distintos territorios a Chile en el siglo XIX. Sirve para ver diferencias en la forma, en los actores y en las consecuencias.",
    prior=["Sé ubicar los hechos territoriales en el tiempo.", "Sé causas y consecuencias de cada proceso.", "Sé comparar usando un criterio."],
    explain=[
        "Comparar territorios es ver cómo se incorporó cada uno y qué pasó con sus habitantes. Podemos usar tres criterios: la forma de incorporación (guerra, ocupación, colonización o acuerdo), los actores que vivían o llegaron al lugar y las consecuencias para esos grupos.",
        "El norte se incorporó por guerra, y allí vivían peruanos, bolivianos y trabajadores chilenos del salitre. La Araucanía se incorporó por ocupación y era territorio mapuche. El sur se pobló con colonos alemanes y apoyo del Estado. Magallanes se aseguró fundando un fuerte y una ciudad. La Isla de Pascua se incorporó por un acuerdo cuyo sentido ha sido discutido por el pueblo rapa nui.",
        "Así vemos que no hubo un solo camino ni una sola experiencia. Para el Estado, ampliar el territorio fue un logro. Para algunos pueblos, como el mapuche, tuvo consecuencias de pérdida de tierras. Comparar con cuidado permite entender estas diferencias sin simplificar.",
    ],
    vocab=[("criterio", "aspecto que se usa para comparar"), ("acuerdo", "decisión tomada entre dos partes"), ("asegurar", "dejar un lugar bajo control firme"), ("rapa nui", "pueblo originario de la Isla de Pascua"), ("simplificar", "hacer parecer algo más fácil o más igual de lo que es")],
    worked=[
        ("Comparar la forma", "{F} Compara cómo se incorporaron el norte y la Araucanía.", ["El norte se incorporó tras la Guerra del Pacífico.", "La Araucanía se incorporó por ocupación entre 1861 y 1883."], "El norte por guerra y la Araucanía por ocupación"),
        ("Encontrar una semejanza", "{F} ¿Qué tienen en común el sur y Magallanes?", ["En ambos el Estado impulsó la presencia de población o de fundaciones.", "Eran zonas que el Estado veía como poco pobladas."], "El Estado apoyó el poblamiento de zonas poco pobladas"),
    ],
    mistakes=[("Decir que todos los territorios se incorporaron por guerra.", "Se simplifica el proceso.", "Hubo guerra, ocupación, colonización y acuerdo."),
              ("Olvidar a los pueblos que ya vivían en cada territorio.", "Se estudia solo la mirada del Estado.", "El territorio de la Araucanía era mapuche y Pascua era rapa nui.")],
    T=[
        ("{F} ¿Qué territorio se incorporó por un acuerdo en 1888?", "la Isla de Pascua", "La ficha lo dice."),
        ("{F} ¿Qué pueblo originario vivía en la Isla de Pascua?", "el pueblo rapa nui", "La ficha lo indica."),
        ("{F} ¿Qué se fundó en 1848 para asegurar el estrecho de Magallanes?", "Punta Arenas", "La ficha lo dice."),
        ("{F} ¿Qué riqueza principal tenía el norte?", "el salitre", "La ficha lo indica."),
        ("{F} ¿Quiénes llegaron al sur desde mediados del siglo XIX con apoyo del Estado?", "colonos alemanes", "La ficha lo dice."),
        ("{F} Une cada forma de incorporación (guerra, ocupación, colonización, acuerdo) con un lugar (Pascua, Araucanía, norte, sur).", "guerra: norte; ocupación: Araucanía; colonización: sur; acuerdo: Pascua", "La ficha asigna cada forma a un lugar."),
        ("=", "{F} ¿Cuántos años pasaron entre la fundación del Fuerte Bulnes y la incorporación de la Isla de Pascua?", "1888-1843", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué diferencia hay entre el norte y la Araucanía en cuanto a la población que vivía allí?", "en el norte vivían peruanos, bolivianos y trabajadores del salitre; en la Araucanía vivía el pueblo mapuche", "La ficha describe actores distintos."),
        ("{F} ¿Qué semejanza hay entre el norte y la Araucanía en cuanto al Estado?", "en ambos el Estado chileno amplió su control", "Tras la guerra y la ocupación, el control del Estado creció."),
        ("{F} Un compañero dice: «Todos los territorios se incorporaron igual». Corrígelo con dos ejemplos.", "el norte por guerra y Pascua por un acuerdo", "Las formas son distintas."),
        ("{F} Una alumna dice: «En Pascua el acuerdo fue claro para todos». ¿Qué dato de la ficha lo contradice?", "que su sentido ha sido discutido hasta hoy", "Hay discusión sobre su sentido."),
        ("{F} ¿Qué criterio usarías para comparar cómo se incorporó cada territorio?", "la forma de incorporación", "Es el primer criterio de la clase."),
        ("{F} Elige la mejor conclusión de la comparación: A) No hubo un solo camino ni una sola experiencia. B) Todos los lugares se incorporaron igual.", "A", "La ficha muestra procesos distintos."),
    ],
    ctx=("Una profesora pide una frase que compare la Araucanía con el sur. ¿Cuál es correcta? A) En ambos llegaron colonos, pero la Araucanía era territorio mapuche. B) En ambos vivían solo colonos.", "A", "La Araucanía ya tenía población mapuche."),
    sc=[("¿Cuáles son los tres criterios de la clase para comparar?", "forma de incorporación, actores y consecuencias", "Son los criterios de la explicación."),
        ("{F} ¿Qué territorio tenía como riqueza principal el salitre?", "el norte", "La ficha lo indica."),
        ("¿Por qué no hay que simplificar la historia del territorio?", "porque cada lugar tuvo una historia distinta", "Hubo varias formas y varios actores.")],
    op=("Dibuja una tabla con cinco filas (norte, Araucanía, sur, Magallanes, Isla de Pascua) y tres columnas: «forma de incorporación», «quiénes vivían o llegaron» y «consecuencia». Completa con datos de la ficha. Escribe una oración que compare dos filas. {F}",
        "Norte: guerra; peruanos, bolivianos y trabajadores del salitre; Chile amplió su territorio. Araucanía: ocupación; mapuche; terrenos reducidos. Oración: El norte se incorporó por guerra y la Araucanía por ocupación.",
        ["cinco filas completas", "datos de la ficha", "oración comparativa"], ["tabla comparativa", "oración final"], ["poner a Pascua por guerra", "dejar sin población a la Araucanía"],
        "Pide que explique cuál fila fue más difícil de completar."),
    reinforce="Di en voz alta la forma de incorporación de cada territorio.",
    extend="Escribe una pregunta que les harías a las personas rapa nui hoy sobre lo ocurrido en 1888, marcando que es solo una pregunta.",
)
