"""Material del estudiante de 6.º básico, Historia, Geografía y Ciencias Sociales: OA 07 (democratización de la sociedad chilena en el siglo XX)."""
from __future__ import annotations

from hi5_lib import build

OA7 = "HI06 OA 07"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 29 (cronología de la democratización en el siglo XX, hecha para este cuaderno). "
     "1920: la Ley de Instrucción Primaria Obligatoria establece que niñas y niños deben asistir a la escuela primaria. "
     "1925: entra en vigencia una nueva Constitución, que reemplaza a la de 1833. "
     "1935: las mujeres votan por primera vez, en elecciones municipales. "
     "1945: la poeta Gabriela Mistral recibe el Premio Nobel de Literatura. "
     "1949: una ley reconoce a las mujeres el derecho a votar en todas las elecciones; en 1952 votan por primera vez para elegir presidente. "
     "1965: una reforma educacional establece ocho años de educación básica obligatoria. "
     "1970: se baja la edad para votar a 18 años y pueden votar las personas que no saben leer.")
build(
    OA7, 1, F,
    use="Aprenderé a ubicar en el tiempo cómo se ampliaron el voto, la participación de la mujer y el acceso a la educación en el siglo XX. Sirve para ver que la democracia creció por etapas.",
    prior=["Sé que en el siglo XIX votaban pocos hombres.", "Sé que las mujeres no votaban en 1874.", "Sé leer una línea de tiempo y restar años."],
    explain=[
        "La democracia es una forma de gobierno en que los ciudadanos participan, sobre todo eligiendo a sus autoridades. Democratizar una sociedad es ampliar esa participación a más personas y dar a más personas acceso a derechos. En Chile, este proceso avanzó de a poco durante el siglo XX.",
        "Hubo avances en tres áreas. En el voto, las mujeres votaron por primera vez en elecciones municipales en 1935, y desde 1949 en todas las elecciones; en 1970 se bajó la edad para votar a 18 años y se permitió votar a quienes no sabían leer. En la participación pública, mujeres como Gabriela Mistral fueron reconocidas. En la educación, la ley de 1920 hizo obligatoria la escuela primaria y la reforma de 1965 estableció ocho años de educación básica obligatoria.",
        "Ubicar estos hechos en una línea de tiempo muestra que los cambios no ocurrieron de golpe. Cada ampliación del voto o de la educación incluyó a más personas, y todavía hoy se discuten nuevos desafíos. Esto nos ayuda a ver la democratización como un proceso largo y no como un solo día.",
    ],
    vocab=[("democracia", "forma de gobierno en que los ciudadanos participan, por ejemplo eligiendo a sus autoridades"), ("sufragio", "derecho a votar"), ("democratización", "proceso de ampliar la participación y los derechos a más personas"), ("obligatorio", "que todas las personas deben cumplir"), ("municipal", "relacionado con la municipalidad, el gobierno de una comuna")],
    worked=[
        ("Calcular un intervalo", "{F} ¿Cuántos años pasaron entre el primer voto de las mujeres en elecciones municipales y su derecho a votar en todas las elecciones?", ["Busco los años: 1935 y 1949.", "Resto: 1949 − 1935 = 14."], "14 años"),
        ("Ordenar hechos", "{F} ¿Qué ocurrió antes: la reforma educacional de 1965 o el Premio Nobel de Mistral?", ["El Nobel de Mistral fue en 1945.", "La reforma fue en 1965."], "El Premio Nobel de Mistral"),
    ],
    mistakes=[("Creer que las mujeres pudieron votar en todas las elecciones desde 1935.", "Se mezclan las elecciones municipales con las demás.", "En 1935 votaron en elecciones municipales y desde 1949 en todas."),
              ("Pensar que la democratización ocurrió de una vez.", "Se olvida que fue gradual.", "Se amplió por etapas: 1920, 1935, 1949, 1965 y 1970.")],
    T=[
        ("{F} ¿Qué estableció la ley de 1920?", "que la escuela primaria fuera obligatoria", "La ficha lo dice."),
        ("{F} ¿En qué año votaron las mujeres por primera vez en elecciones municipales?", "1935", "La ficha lo indica."),
        ("{F} ¿Quién recibió el Premio Nobel de Literatura en 1945?", "Gabriela Mistral", "La ficha lo dice."),
        ("=", "{F} ¿Cuántos años pasaron entre el Premio Nobel de Mistral y la reforma educacional de 1965?", "1965-1945", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Cuántos años de educación básica obligatoria estableció la reforma de 1965?", "ocho", "La ficha lo indica."),
        ("{F} ¿Qué dos cambios hubo en 1970 para votar?", "se bajó la edad a 18 años y pudieron votar quienes no sabían leer", "La ficha los menciona."),
        ("{F} Ordena de más antiguo a más reciente: voto femenino pleno, escuela primaria obligatoria, voto a los 18 años, voto en elecciones municipales.", "escuela primaria obligatoria, voto en elecciones municipales, voto femenino pleno, voto a los 18 años", "Los años son 1920, 1935, 1949 y 1970."),
        ("=", "{F} ¿Cuántos años pasaron entre la primera votación de mujeres para presidente (1952) y la reforma de 1970?", "1970-1952", "Se resta el año menor al mayor.", " años"),
        ("{F} Clasifica los hechos como «voto» o «educación»: a) 1920; b) 1949; c) 1965; d) 1970.", "voto: b y d; educación: a y c", "La ficha describe cada hecho."),
        ("{F} Un compañero dice: «Las mujeres votaron para presidente en 1935». Corrígelo.", "No: en 1935 votaron en elecciones municipales; para presidente votaron en 1952", "La ficha distingue las dos fechas."),
        ("{F} Una alumna dice: «En 1965 se hizo obligatoria la escuela primaria por primera vez». ¿Qué error hay?", "la escuela primaria ya era obligatoria desde 1920; en 1965 se estableció ocho años de básica", "1920 es anterior a 1965."),
        ("{F} Una línea de tiempo usa 1 cm = 10 años y parte en 1920. ¿A cuántos cm queda el año 1970?", "5 cm", "(1970 − 1920) ÷ 10 = 5."),
        ("{F} De los años 1920, 1925, 1935, 1945, 1949, 1965 y 1970, ¿cuántos se relacionan con el derecho a voto?", "tres (1935, 1949 y 1970)", "Los otros años tratan de educación, de una constitución o de un premio."),
    ],
    ctx=("Una placa en una plaza dice «1949». Según la ficha, ¿qué derecho se reconoció en ese año y a quiénes?", "el derecho a votar en todas las elecciones, para las mujeres", "La ficha lo indica."),
    sc=[("¿Qué es democratizar una sociedad?", "ampliar la participación y los derechos a más personas", "Es la definición de la clase."),
        ("{F} ¿En qué año se recibió el Nobel de Literatura?", "1945", "La ficha lo dice."),
        ("¿Por qué decimos que la democratización fue gradual?", "porque avanzó por etapas durante muchos años", "Cada ampliación ocurrió en una fecha distinta.")],
    op=("Dibuja una línea de tiempo desde 1920 hasta 1975. Marca los siete hechos de la ficha. Usa tres colores: uno para voto, otro para educación y otro para participación pública de las mujeres. Pinta de gris el hecho que no corresponde a ninguna de las tres. {F}",
        "Puntos en 1920, 1925, 1935, 1945, 1949, 1965 y 1970, con colores distintos.",
        ["siete hechos ordenados", "tres colores bien usados", "años correctos"], ["línea de tiempo coloreada"], ["poner 1949 antes que 1935", "pintar 1920 como voto"],
        "Pide que explique en voz alta por qué la democratización fue un proceso."),
    reinforce="Di en voz alta los hitos del voto y de la educación con su año.",
    extend="Escribe una pregunta sobre cómo vivió una mujer el día en que votó por primera vez.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 30 (fuentes inventadas para este cuaderno, basadas en hechos conocidos). "
     "Fuente A, noticia de un diario, abril de 1935 (texto inventado): «Por primera vez las mujeres acudieron a votar en las elecciones municipales; hubo largas filas en varias comunas». "
     "Fuente B, afiche de una organización de mujeres, década de 1940 (texto inventado): «Si trabajamos, estudiamos y pagamos impuestos, también queremos votar». "
     "Fuente C, extracto adaptado de la ley de 1920: los niños y niñas de las ciudades y del campo deben asistir a la escuela primaria. "
     "Fuente D, libro de historia de 2005: explica que el voto femenino se logró después de décadas de campañas de organizaciones de mujeres.")
build(
    OA7, 2, F,
    use="Aprenderé a leer fuentes sobre el voto y la educación preguntando quién habla y para qué. Sirve para entender qué pedían las personas y qué lograron.",
    prior=["Sé qué es una fuente primaria y una secundaria.", "Sé qué hitos hubo en el voto y la educación.", "Sé que cada fuente tiene un punto de vista."],
    explain=[
        "Para estudiar la democratización usamos fuentes como noticias, afiches, leyes y libros de historia. Cada una se hizo para algo. Una noticia informa; un afiche convence; una ley ordena; un libro de historia explica lo ocurrido después.",
        "La noticia de 1935 (fuente A) muestra el entusiasmo del primer voto femenino en elecciones municipales. El afiche (fuente B) muestra lo que pedía una organización de mujeres: querían votar porque ya trabajaban, estudiaban y pagaban impuestos. La ley de 1920 (fuente C) es una fuente oficial. El libro de 2005 (fuente D) es secundario y resume las campañas.",
        "Las fuentes ayudan a entender argumentos y logros, pero ninguna dice todo. Por ejemplo, el afiche no cuenta qué pensaban quienes se oponían. Además, ninguna fuente nos dice cómo vivían las mujeres del campo o de los pueblos indígenas. Por eso necesitamos varias fuentes y debemos ser prudentes al concluir.",
    ],
    vocab=[("afiche", "cartel con un mensaje para convencer o informar"), ("organización", "grupo de personas que trabaja junto por un objetivo"), ("campaña", "conjunto de acciones para lograr algo"), ("impuesto", "dinero que se paga al Estado"), ("oficial", "que viene del gobierno o de una autoridad")],
    worked=[
        ("Reconocer el propósito", "{F} ¿Para qué se hizo la fuente B?", ["Es un afiche de una organización de mujeres.", "Quiere convencer de que también tienen derecho a votar."], "Para convencer de que las mujeres deben votar"),
        ("Clasificar una fuente", "{F} ¿La fuente D es primaria o secundaria?", ["Se escribió en 2005.", "Habla de hechos de décadas antes."], "Secundaria"),
    ],
    mistakes=[("Creer que el afiche muestra lo que pensaban todos.", "Se generaliza desde un grupo.", "Muestra el punto de vista de una organización de mujeres."),
              ("Pensar que la noticia de 1935 cuenta lo que sintieron todas las mujeres.", "Se confunde la noticia con todas las experiencias.", "Una noticia resume; no cuenta cada vivencia.")],
    T=[
        ("{F} ¿Qué ocurrió en abril de 1935 según la fuente A?", "las mujeres acudieron a votar por primera vez en elecciones municipales", "La noticia lo dice."),
        ("{F} ¿Qué razones da el afiche de la fuente B para que las mujeres voten?", "que trabajan, estudian y pagan impuestos", "El afiche las enumera."),
        ("{F} ¿Quiénes deben asistir a la escuela según la fuente C?", "niñas y niños de las ciudades y del campo", "La ley lo establece."),
        ("{F} ¿Cuál de las cuatro fuentes es secundaria?", "la fuente D", "Se escribió en 2005."),
        ("=", "{F} ¿Cuántos años pasaron entre la ley de 1920 y la noticia de 1935?", "1935-1920", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué fuente de la ficha es oficial?", "la fuente C", "Es una ley."),
        ("{F} Compara A y B: ¿cuál informa un hecho y cuál busca convencer?", "A informa y B convence", "Una noticia informa y un afiche convence."),
        ("{F} Una alumna dice: «El afiche prueba que todos apoyaban el voto femenino». ¿Qué error comete?", "generaliza: el afiche muestra la opinión de una organización", "No habla por toda la sociedad."),
        ("{F} ¿Qué dato de la fuente D explica cómo se logró el voto femenino?", "después de décadas de campañas de organizaciones de mujeres", "La fuente D lo explica."),
        ("{F} ¿Qué voz falta en las cuatro fuentes?", "la de mujeres del campo y de los pueblos indígenas", "Ninguna las menciona."),
        ("{F} Para saber qué argumentaban las mujeres que pedían votar, ¿qué fuente es más útil?", "la fuente B", "El afiche contiene sus argumentos."),
        ("{F} Un compañero dice: «La fuente C prueba que todos los niños fueron a la escuela en 1920». ¿Qué error comete?", "una ley establece una obligación, pero no prueba que todos la cumplieran", "La ley no es lo mismo que la realidad."),
        ("{F} Ordena las fuentes de la más antigua a la más reciente.", "C, A, B, D", "Los años son 1920, 1935, década de 1940 y 2005."),
    ],
    ctx=("Para un trabajo, un grupo quiere saber cómo se sintió el primer voto femenino. ¿Qué fuente les sirve más y qué otra buscarían?", "la fuente A, y buscarían testimonios de mujeres que votaron", "La fuente A es la más cercana al hecho."),
    sc=[("¿Qué diferencia hay entre una noticia y un afiche?", "la noticia informa y el afiche busca convencer", "Tienen propósitos distintos."),
        ("{F} ¿Qué tipo de fuente es la A?", "primaria", "Se escribió en 1935."),
        ("¿Por qué una ley no prueba que algo se cumplió?", "porque establece una regla, pero no dice si todos la cumplieron", "Hay que revisar otras fuentes.")],
    op=("Haz una ficha de análisis con las cuatro fuentes. Anota quién habla, año, qué dice, qué propósito tiene y qué no dice. Termina con dos oraciones sobre qué lograron las mujeres según estas fuentes. {F}",
        "B: organización de mujeres, década de 1940, quiere convencer; no dice qué pensaban quienes se oponían. D: libro de 2005, explica la campaña; es secundaria.",
        ["cuatro fuentes analizadas", "propósito identificado", "límite razonable", "dos oraciones finales"], ["ficha de análisis", "dos oraciones"], ["tratar B como noticia", "no anotar límites"],
        "Pide que explique qué fuente le pareció más persuasiva."),
    reinforce="Con tus palabras, resume lo que dice cada fuente.",
    extend="Escribe una pregunta sobre qué argumentarían quienes se oponían al voto femenino en 1940, marcando que es una suposición.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 31 (actores, causas y consecuencias, hecha para este cuaderno). "
     "Actores: organizaciones de mujeres, como el Movimiento Pro Emancipación de la Mujer Chilena (1935), en el que participó Elena Caffarena; educadoras como Amanda Labarca; poetas como Gabriela Mistral; los partidos políticos; el Estado, que dictó leyes. "
     "Causas de la ampliación de derechos: las mujeres trabajaban cada vez más fuera de la casa y estudiaban; las ciudades crecieron; se organizaron campañas para pedir derechos; se reconoció que la educación era necesaria para participar. "
     "Consecuencias: más ciudadanos y ciudadanas votaron; en 1951 Inés Enríquez fue elegida como primera diputada; más niños y niñas asistieron a la escuela; creció la participación de las mujeres en profesiones y en la vida pública.")
build(
    OA7, 3, F,
    use="Aprenderé a explicar por qué se ampliaron el voto y la educación y qué consecuencias tuvo. Sirve para reconocer a los actores, sobre todo a las mujeres, y sus aportes.",
    prior=["Sé ubicar los hitos de la democratización.", "Sé distinguir causa y consecuencia.", "Sé que muchas personas participan en un cambio."],
    explain=[
        "Los derechos no aparecieron solos: personas y grupos los pidieron. En la democratización participaron organizaciones de mujeres, educadoras, escritoras, partidos políticos y el Estado. Por ejemplo, el Movimiento Pro Emancipación de la Mujer Chilena, fundado en 1935, pidió derechos para las mujeres, y en él participó Elena Caffarena.",
        "Entre las causas del cambio están que las mujeres trabajaban y estudiaban cada vez más, que las ciudades crecieron y que se organizaron campañas. Entre las consecuencias, más personas votaron, más niños y niñas asistieron a la escuela y las mujeres entraron a profesiones y a la vida pública. Por ejemplo, en 1951 Inés Enríquez fue elegida la primera diputada.",
        "Para explicar hay que distinguir lo que ayudó a que ocurriera el cambio (causa) de lo que ocurrió después (consecuencia). También hay que reconocer que la democratización tuvo límites: durante años, algunas personas, como las que no sabían leer, no podían votar. Comprender este proceso nos ayuda a valorar los derechos actuales.",
    ],
    vocab=[("movimiento", "grupo de personas que actúa junto para lograr un cambio"), ("diputada", "mujer elegida para representar a los ciudadanos en la Cámara de Diputados"), ("profesión", "trabajo para el que se estudia"), ("causa", "razón que ayuda a que algo ocurra"), ("consecuencia", "resultado de un hecho")],
    worked=[
        ("Clasificar causa y consecuencia", "{F} ¿Que Inés Enríquez fuera elegida primera diputada es causa o consecuencia?", ["Ocurre en 1951, después de las campañas.", "La ficha la lista como una consecuencia."], "Consecuencia"),
        ("Reconocer un actor", "{F} ¿Qué organización fundada en 1935 pidió derechos para las mujeres?", ["Busco una organización de mujeres.", "Es el Movimiento Pro Emancipación de la Mujer Chilena."], "El Movimiento Pro Emancipación de la Mujer Chilena"),
    ],
    mistakes=[("Pensar que los derechos se obtuvieron sin esfuerzo.", "Se ignora el trabajo de las organizaciones.", "Hubo campañas durante años para lograrlos."),
              ("Creer que solo participaron mujeres.", "Se omiten otros actores.", "También participaron partidos políticos y el Estado.")],
    T=[
        ("{F} ¿Qué persona de la ficha participó en el Movimiento Pro Emancipación de la Mujer Chilena?", "Elena Caffarena", "La ficha lo dice."),
        ("{F} ¿Qué educadora se nombra en la ficha?", "Amanda Labarca", "La ficha la nombra."),
        ("{F} ¿Quién fue elegida primera diputada en 1951?", "Inés Enríquez", "La ficha lo indica."),
        ("{F} Clasifica como causa (C) o consecuencia (K): a) las mujeres estudiaban más; b) más niñas asistieron a la escuela; c) crecieron las ciudades; d) más mujeres en profesiones.", "a: C; b: K; c: C; d: K", "Las causas son anteriores al cambio."),
        ("=", "{F} ¿Cuántos años pasaron entre la fundación del movimiento (1935) y la elección de la primera diputada?", "1951-1935", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué actores aparecen en la ficha, además de las organizaciones de mujeres?", "educadoras, poetas, los partidos políticos y el Estado", "La ficha los enumera."),
        ("{F} ¿Qué motivo del cambio se relaciona con el trabajo de las mujeres?", "las mujeres trabajaban cada vez más fuera de la casa", "La ficha lo indica."),
        ("{F} Un compañero dice: «Las mujeres obtuvieron el voto sin que nadie lo pidiera». Corrígelo.", "No: hubo organizaciones y campañas que lo pidieron", "La ficha lo indica."),
        ("{F} Una alumna dice: «En 1951 ninguna mujer podía ser candidata». ¿Qué dato lo contradice?", "que Inés Enríquez fue elegida diputada en 1951", "Ella fue elegida en 1951."),
        ("{F} ¿Cuál es una consecuencia de la ampliación de la educación?", "más niños y niñas asistieron a la escuela", "La ficha lo dice."),
        ("{F} ¿Por qué se necesita educación para participar en democracia?", "porque ayuda a informarse y a decidir con conocimiento", "La ficha dice que se reconoció su necesidad para participar."),
        ("{F} Elige la mejor explicación: A) El voto se amplió porque las mujeres pidieron derechos y cambió la sociedad. B) El voto se amplió sin motivo.", "A", "Menciona causas y actores del cambio."),
        ("{F} Da un límite de la democratización mencionado en la clase.", "durante años algunas personas, como las que no sabían leer, no podían votar", "Lo dice la explicación."),
    ],
    ctx=("En un acto escolar, un estudiante dice: «Los derechos de las mujeres fueron un regalo del Estado». Usa la ficha para responder.", "no: organizaciones de mujeres hicieron campañas durante años para pedirlos", "La ficha nombra organizaciones y campañas."),
    sc=[("¿Qué es un movimiento social?", "un grupo de personas que actúa junto para lograr un cambio", "Es la definición de la clase."),
        ("{F} ¿Quién fue la primera diputada elegida?", "Inés Enríquez", "La ficha lo dice."),
        ("¿Qué es una consecuencia?", "un resultado de un hecho", "Ocurre después del hecho.")],
    op=("Dibuja una tabla con tres columnas: «causas», «actores» y «consecuencias». Escribe al menos tres elementos en cada una, usando la ficha. Después escribe una oración que conecte una causa con una consecuencia. {F}",
        "Causas: mujeres trabajaban y estudiaban. Actores: Elena Caffarena, MEMCH. Consecuencias: más votantes, primera diputada. Oración: Como las mujeres trabajaban y estudiaban, pidieron votar.",
        ["tres elementos en cada columna", "elementos en la columna correcta", "oración que conecta causa y consecuencia"], ["tabla de tres columnas", "una oración"], ["poner la primera diputada como causa", "no mencionar a las organizaciones"],
        "Pide que cambie un elemento de columna y explique por qué quedaría mal."),
    reinforce="Di en voz alta dos causas, dos actores y dos consecuencias.",
    extend="Escribe una pregunta sobre qué desafíos enfrentó una mujer que quería estudiar en 1930.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 32 (comparación de épocas, hecha para este cuaderno). "
     "Quién podía votar en 1833: hombres mayores de 25 años (21 si estaban casados) que supieran leer y escribir y tuvieran propiedades o renta. "
     "En 1874: hombres mayores de 21 años que supieran leer y escribir. "
     "En 1949: hombres y mujeres que supieran leer y escribir, mayores de 21 años. "
     "En 1970: hombres y mujeres desde los 18 años, aunque no supieran leer. "
     "Educación: antes de 1920, muchos niños no iban a la escuela; en 1920, la primaria pasó a ser obligatoria; en 1965, se estableció ocho años de educación básica obligatoria. "
     "Mujeres en la vida pública: antes de 1935, sin voto; en 1935, voto municipal; en 1949, voto en todas las elecciones; en 1951, primera diputada.")
build(
    OA7, 4, F,
    use="Aprenderé a comparar cómo cambió quién podía votar y quién iba a la escuela entre 1833 y 1970. Sirve para describir cambios y continuidades de la democratización.",
    prior=["Sé ubicar los hitos del voto y de la educación.", "Sé comparar usando un criterio.", "Sé distinguir cambio y continuidad."],
    explain=[
        "Comparar épocas es ver qué cambió y qué siguió igual. Para la democratización podemos usar tres criterios: quién podía votar, quién iba a la escuela y qué participación tenían las mujeres. Comparamos así 1833, 1874, 1949 y 1970.",
        "En 1833 votaban pocos hombres; en 1874 se amplió a hombres que sabían leer; en 1949 votaron también las mujeres; en 1970 se bajó la edad a 18 años y se incluyó a quienes no sabían leer. En educación, la escuela primaria se hizo obligatoria en 1920 y la educación básica de ocho años, en 1965. En cada etapa más personas quedaron incluidas.",
        "Hubo cambios y continuidades. Cambió quién votaba y quién estudiaba, pero hasta 1949 las mujeres seguían sin voto en todas las elecciones, y hasta 1970 quienes no sabían leer no podían votar. Comparar permite ver el avance, pero también cuánto tardaron algunos derechos en llegar.",
    ],
    vocab=[("cambio", "algo que es distinto de antes"), ("continuidad", "algo que sigue igual a través del tiempo"), ("criterio", "aspecto que se usa para comparar"), ("analfabeto", "persona que no sabe leer ni escribir"), ("inclusión", "hecho de que más personas puedan participar")],
    worked=[
        ("Comparar un criterio", "{F} Compara quién podía votar en 1874 y en 1970.", ["En 1874, hombres mayores de 21 años que sabían leer.", "En 1970, hombres y mujeres desde los 18 años, aunque no supieran leer."], "En 1970 votaban más personas: mujeres, jóvenes de 18 y personas que no sabían leer"),
        ("Encontrar una continuidad", "{F} ¿Qué requisito se mantuvo entre 1874 y 1949 para votar?", ["Comparo los requisitos.", "En ambos casos se exigía saber leer y escribir."], "Saber leer y escribir"),
    ],
    mistakes=[("Decir que en 1949 podían votar todas las personas mayores de 18 años.", "Se mezclan los datos de 1949 y 1970.", "En 1949 la edad era 21; la baja a 18 fue en 1970."),
              ("Pensar que todos los cambios fueron simultáneos.", "Se pierde el orden de las etapas.", "El voto femenino fue en 1949 y la baja de edad en 1970.")],
    T=[
        ("{F} ¿Desde qué edad podían votar los hombres en 1874?", "desde los 21 años", "La ficha lo indica."),
        ("{F} ¿Qué cambió en 1970 respecto de la edad para votar?", "se bajó a 18 años", "La ficha lo dice."),
        ("{F} ¿Qué se exigía en 1949 para votar, además de la edad?", "saber leer y escribir", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre 1874 y 1970?", "1970-1874", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Cuántos años de educación básica obligatoria se establecieron en 1965?", "ocho", "La ficha lo dice."),
        ("{F} ¿Qué grupo pudo votar por primera vez en 1949 en todas las elecciones?", "las mujeres", "La ficha lo indica."),
        ("{F} Ordena por quiénes podían votar, de menos a más personas: 1949, 1833, 1970, 1874.", "1833, 1874, 1949, 1970", "Cada etapa incluyó a más personas."),
        ("{F} Clasifica como cambio (C) o continuidad (K) entre 1874 y 1949: a) las mujeres votan; b) se exige saber leer y escribir; c) los hombres de 21 años votan.", "a: C; b: K; c: K", "Solo las mujeres son un cambio."),
        ("{F} Una joven de 19 años que no sabe leer, ¿podía votar en 1949?", "no", "En 1949 se exigía saber leer y escribir y tener 21 años."),
        ("{F} Esa misma joven, ¿podía votar en 1970?", "sí", "En 1970 votaban desde los 18 años aunque no supieran leer."),
        ("{F} Un compañero dice: «En 1833 votaban todos los hombres». Corrígelo.", "No: solo votaban los hombres que cumplían los requisitos de edad, lectura y propiedades", "La ficha lo indica."),
        ("{F} Una alumna dice: «La educación básica obligatoria comenzó en 1965». ¿Qué error comete?", "la escuela primaria obligatoria comenzó en 1920; en 1965 se establecieron ocho años de básica", "1920 es anterior."),
        ("{F} ¿Qué conclusión se puede sacar de la comparación? A) Cada etapa incluyó a más personas, pero tardó años en llegar. B) Todos tenían los mismos derechos desde 1833.", "A", "La ficha muestra ampliación gradual."),
    ],
    ctx=("Un estudiante dice: «La democracia en Chile siempre fue igual». Usa la ficha para responderle con dos cambios.", "las mujeres pudieron votar en 1949 y en 1970 se bajó la edad a 18 años y votaron quienes no sabían leer", "La ficha muestra cambios en el voto."),
    sc=[("¿Qué se compara al comparar épocas?", "qué cambió y qué siguió igual", "Es el objetivo de comparar."),
        ("{F} ¿Qué requisito se eliminó en 1970?", "saber leer para votar", "La ficha lo dice."),
        ("¿Por qué es útil comparar 1833 y 1970?", "porque muestra cuánto se ampliaron los derechos", "Contrasta dos extremos.")],
    op=("Dibuja una tabla con cuatro filas (1833, 1874, 1949, 1970) y tres columnas: «quién podía votar», «edad mínima» y «requisito de lectura». Completa con datos de la ficha. Debajo escribe una oración que diga un cambio y otra una continuidad. {F}",
        "1949: hombres y mujeres, 21 años, saber leer y escribir. 1970: hombres y mujeres, 18 años, sin requisito de lectura. Cambio: se bajó la edad. Continuidad: el voto de los hombres se mantuvo.",
        ["cuatro filas completas", "datos correctos", "un cambio y una continuidad"], ["tabla comparativa", "dos oraciones"], ["mezclar datos de 1949 y 1970", "no anotar continuidades"],
        "Pide que explique cuál fila muestra el mayor cambio."),
    reinforce="Di en voz alta quién podía votar en cada año de la ficha.",
    extend="Escribe una pregunta sobre quiénes siguen sin poder votar hoy y por qué.",
)
